"""
ECBS5200 — Shared data loading utilities.

Single import for all course notebooks and scripts:

    from utils.data_utils import load_course_data, LABEL_LIST, NUM_LABELS

Handles dataset loading, label merging, class filtering, canonical
train/val/test splitting, and slice assignment. Never solve these
problems twice.
"""

import json
import re
from pathlib import Path
from datasets import load_dataset

# ---------------------------------------------------------------------------
# Paths (relative to repo root)
# ---------------------------------------------------------------------------
_DATA_DIR = Path(__file__).resolve().parent.parent / "data"
_MERGE_MAP_PATH = _DATA_DIR / "label_merge_mapping.json"
_TRAIN_INDICES_PATH = _DATA_DIR / "train_indices.json"
_VAL_INDICES_PATH = _DATA_DIR / "val_indices.json"
_LABEL_LIST_PATH = _DATA_DIR / "label_list.json"

# ---------------------------------------------------------------------------
# Constants (loaded once at import time)
# ---------------------------------------------------------------------------
with open(_LABEL_LIST_PATH) as f:
    LABEL_LIST: list[str] = json.load(f)

NUM_LABELS: int = len(LABEL_LIST)  # 113

LABEL_TO_ID: dict[str, int] = {label: i for i, label in enumerate(LABEL_LIST)}
ID_TO_LABEL: dict[int, str] = {i: label for i, label in enumerate(LABEL_LIST)}

with open(_MERGE_MAP_PATH) as f:
    _MERGE_MAP: dict[str, str] = {
        k: v for k, v in json.load(f).items() if not k.startswith("_")
    }

# ---------------------------------------------------------------------------
# Dataset name
# ---------------------------------------------------------------------------
DATASET_NAME = "determined-ai/consumer_complaints_medium"
TEXT_COLUMN = "Consumer Complaint"
LABEL_COLUMN = "Issue"
MAX_LENGTH = 128


def _apply_merge(label: str) -> str:
    """Map a raw Issue label to its canonical merged form."""
    return _MERGE_MAP.get(label, label)


# ---------------------------------------------------------------------------
# Slice assignment
# ---------------------------------------------------------------------------
_VALID_CLASSES = set(LABEL_LIST)

# Rare = bottom quartile by class frequency (computed lazily)
_rare_classes: set[str] | None = None


def _get_rare_classes(labels: list[str]) -> set[str]:
    """Classes whose total count puts them in the bottom quartile."""
    from collections import Counter
    counts = Counter(labels)
    sorted_counts = sorted(counts.values())
    q25 = sorted_counts[len(sorted_counts) // 4]
    return {label for label, c in counts.items() if c <= q25}


def assign_slices(text: str, label: str, rare_classes: set[str]) -> dict[str, str]:
    """
    Assign slice tags to a single example. Returns a dict of slice names
    to slice values. Used for per-slice evaluation in Weeks 4-5.

    Slices:
        frequency:  "rare" | "common"
        length:     "short" | "medium" | "long"  (word-count terciles: <35, 35-65, >65)
        redaction:  "redacted" | "clean"  (contains XXXX)
        numeric:    "numeric" | "non_numeric"  (contains dollar amounts or numbers with 4+ digits)
    """
    word_count = len(text.split())

    return {
        "frequency": "rare" if label in rare_classes else "common",
        "length": (
            "short" if word_count < 35
            else "long" if word_count > 65
            else "medium"
        ),
        "redaction": "redacted" if "XXXX" in text else "clean",
        "numeric": (
            "numeric"
            if re.search(r"\$\d|(?<!\w)\d{4,}(?!\w)", text)
            else "non_numeric"
        ),
    }


# ---------------------------------------------------------------------------
# Main loading function
# ---------------------------------------------------------------------------
def load_course_data(
    include_slices: bool = False,
    tokenizer=None,
    max_length: int = MAX_LENGTH,
):
    """
    Load and return the canonical course dataset splits.

    Returns:
        (train_ds, val_ds, test_ds) — HuggingFace Dataset objects with columns:
            - text (str): complaint text
            - label (int): integer label ID (into LABEL_LIST)
            - label_name (str): human-readable label
            + slice columns if include_slices=True
            + input_ids, attention_mask if tokenizer is provided

    Usage:
        from utils.data_utils import load_course_data, LABEL_LIST, NUM_LABELS

        train_ds, val_ds, test_ds = load_course_data()
        train_ds, val_ds, test_ds = load_course_data(include_slices=True)
        train_ds, val_ds, test_ds = load_course_data(tokenizer=tokenizer)
    """
    # Load raw dataset
    ds = load_dataset(DATASET_NAME)

    # Load canonical indices
    with open(_TRAIN_INDICES_PATH) as f:
        train_indices = json.load(f)
    with open(_VAL_INDICES_PATH) as f:
        val_indices = json.load(f)

    # Process a split: merge labels, filter to valid classes, add integer labels
    def _process(dataset, indices=None):
        if indices is not None:
            dataset = dataset.select(indices)

        # Apply merge and filter
        def _transform(example):
            merged = _apply_merge(example[LABEL_COLUMN])
            if merged not in _VALID_CLASSES:
                return {"_keep": False, "text": "", "label": -1, "label_name": ""}
            return {
                "_keep": True,
                "text": example[TEXT_COLUMN],
                "label": LABEL_TO_ID[merged],
                "label_name": merged,
            }

        dataset = dataset.map(_transform, remove_columns=dataset.column_names)
        dataset = dataset.filter(lambda x: x["_keep"])
        dataset = dataset.remove_columns(["_keep"])
        return dataset

    train_ds = _process(ds["train"], train_indices)
    val_ds = _process(ds["train"], val_indices)
    test_ds = _process(ds["test"])

    # Optional: assign slices
    if include_slices:
        rare = _get_rare_classes(train_ds["label_name"])

        def _add_slices(example):
            slices = assign_slices(example["text"], example["label_name"], rare)
            return {f"slice_{k}": v for k, v in slices.items()}

        train_ds = train_ds.map(_add_slices)
        val_ds = val_ds.map(_add_slices)
        test_ds = test_ds.map(_add_slices)

    # Optional: tokenize
    if tokenizer is not None:
        def _tokenize(batch):
            return tokenizer(
                batch["text"],
                padding="max_length",
                truncation=True,
                max_length=max_length,
            )

        train_ds = train_ds.map(_tokenize, batched=True)
        val_ds = val_ds.map(_tokenize, batched=True)
        test_ds = test_ds.map(_tokenize, batched=True)

    return train_ds, val_ds, test_ds
