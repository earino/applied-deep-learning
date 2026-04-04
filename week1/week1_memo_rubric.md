# Week 1 Technical Note — Rubric

**ECBS5200 — Practical Deep Learning Engineering for Applied ML**

**Deliverable:** Week 1 Technical Note
**Format:** 2-3 pages maximum (not counting tables, figures, or experiment log)
**Total points:** 100

---

## Overview

The Week 1 Technical Note demonstrates that you can audit a dataset, establish meaningful baselines, run a first fine-tuning experiment, and reason clearly about what the results mean. Engineering judgment and clear reasoning matter more than hitting specific numbers. This is a tight technical memo — write concisely and let your tables and figures do the heavy lifting.

---

## Rubric

### 1. Data Audit (20 points)

| Level | Points | Criteria |
|---|---|---|
| **Excellent** | 18-20 | Summarizes the 113-class label distribution concisely, identifies the extreme long tail (top class ~23%, many classes under 0.1%), notes relevant text characteristics (redaction patterns, length distribution), and draws at least one implication for modeling (e.g., rare classes will be hard to learn, class weighting may be needed). |
| **Satisfactory** | 12-17 | Describes the class distribution and mentions imbalance, but observations stay surface-level. May note redaction or text length without connecting them to modeling consequences. |
| **Needs Improvement** | 0-11 | Missing or superficial. Lists basic statistics (e.g., "there are 113 classes") without analysis. Does not identify the long-tail problem or its implications. |

**What we're looking for:** Evidence that you explored the data and thought about what it means for the task ahead — not just that you ran `value_counts()`.

---

### 2. Baseline Results and Interpretation (20 points)

| Level | Points | Criteria |
|---|---|---|
| **Excellent** | 18-20 | Reports TF-IDF + Logistic Regression accuracy and macro F1 correctly, explains *why* these two metrics tell different stories (accuracy dominated by common classes, macro F1 exposes that 70 classes get F1=0), and uses this to set a clear bar for the neural model. |
| **Satisfactory** | 12-17 | Reports both metrics but explanation of the gap is vague or incomplete. May state that macro F1 is "better for imbalanced data" without explaining the mechanism (i.e., that 70/113 classes are completely missed). |
| **Needs Improvement** | 0-11 | Reports only accuracy, or reports both metrics without interpretation. Does not explain what the gap between accuracy and macro F1 reveals. |

**What we're looking for:** Interpretation, not just numbers. The key insight is that 54% accuracy hides the fact that TF-IDF ignores the majority of classes entirely.

---

### 3. Fine-Tuning Results (25 points)

| Level | Points | Criteria |
|---|---|---|
| **Excellent** | 22-25 | Reports neural model metrics (accuracy and macro F1) from a completed training run, describes observed learning curves (training loss, validation metrics over steps/epochs), identifies the best checkpoint and explains why it was selected, and compares meaningfully to the TF-IDF baseline — especially on macro F1. |
| **Satisfactory** | 15-21 | Reports metrics and shows some learning curve information, but analysis is thin. May not clearly identify best checkpoint rationale or may compare only on accuracy without discussing macro F1 improvement. |
| **Needs Improvement** | 0-14 | Metrics are missing, reported without context, or only from a partial (QUICK_MODE) run. No learning curve discussion. No meaningful comparison to baseline. |

**What we're looking for:** Evidence that you ran the training, monitored it, understand what the learning curves show, and can articulate whether and how the neural model improves over the classical baseline. Specific numbers will vary depending on hyperparameters and random seeds — that is expected and fine.

---

### 4. Experiment Log (20 points)

| Level | Points | Criteria |
|---|---|---|
| **Excellent** | 18-20 | Includes a clear pandas DataFrame or formatted table showing all runs (baseline and neural), with columns for model name, key hyperparameters, accuracy, macro F1, and any other relevant metrics. The log is complete enough that someone could reproduce the comparison. |
| **Satisfactory** | 12-17 | Log exists but is incomplete (missing runs, missing columns) or poorly formatted. Enough information to see what was tried, but not enough to fully reconstruct the experimental picture. |
| **Needs Improvement** | 0-11 | No experiment log, or a log that is just a code dump / raw output rather than a structured summary. |

**What we're looking for:** The habit of systematic experiment tracking. This is Week 1, so the log will be short — that's fine. What matters is that it's structured, readable, and includes the metrics that matter.

---

### 5. Identified Risks and Open Questions (15 points)

| Level | Points | Criteria |
|---|---|---|
| **Excellent** | 13-15 | Identifies at least two specific, grounded risks or open questions that follow from the Week 1 results. Examples: rare-class performance may not improve without class weighting or oversampling; truncation at 128 tokens may lose information for longer complaints; overfitting risk on small classes; whether more epochs help or hurt. Shows forward-looking engineering thinking. |
| **Satisfactory** | 8-12 | Identifies at least one risk or question, but it is generic ("the model could overfit") rather than tied to specific observations from the data or results. |
| **Needs Improvement** | 0-7 | Missing, or lists only vague concerns with no connection to the actual data or experiments. |

**What we're looking for:** Evidence that you're thinking ahead. The best memos don't just report what happened — they identify what to worry about and what to try next.

---

## General Notes

- **Conciseness is valued.** A tight 2-page memo that covers all five sections with clear reasoning will score higher than a 5-page memo that buries insights in filler.
- **Exact numbers will vary.** Different random seeds, hyperparameters, and training durations will produce different results. We are grading your ability to reason about the results you got, not whether you hit a specific target.
- **Week 1 does NOT require a decoder comparison.** The decoder reference system is introduced in class as motivation, but a formal encoder-vs-decoder comparison is a Week 4 deliverable.
- **AI tools are allowed** for coding and experimentation, but you must understand and be able to explain everything in your memo. If you cannot explain a result or design choice, it should not be in your submission.
- **Tables and figures do not count toward the page limit.** Use them. A well-labeled table is worth more than a paragraph of prose describing the same information.
