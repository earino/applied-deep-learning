# ECBS5200 Pre-Work: Getting Ready for Practical Deep Learning Engineering

**Due before:** Wednesday, April 8, 2026 (first day of class)
**Expected time:** 2–3 hours total

---

## What this is

Before we start the course, you need to be comfortable with a handful of concepts that we'll use from Day 1. This pre-work isn't a mini-course — it's a warm-up. Each module gives you just enough intuition to hit the ground running.

## What's inside

There are **8 short modules**, each with:
- A short slide deck (~8–12 minutes to watch or read)
- A Kaggle notebook you can run yourself (~10–15 minutes)

| # | Module | What you'll learn |
|---|--------|-------------------|
| 01 | Tokenization & Truncation | How text becomes numbers, and what gets lost |
| 02 | Pretrained Encoders for Classification | What a pretrained model is, and how we bolt on a classifier |
| 03 | Train vs Eval Mode | Why `model.eval()` exists and what breaks if you forget it |
| 04 | Confusion Matrices & Macro-F1 | How to read model errors and why accuracy lies |
| 05 | Calibration Basics | What "90% confident" actually means (and when it doesn't) |
| 06 | LoRA/PEFT Basics | The idea of training only a small part of a big model |
| 07 | Quantization Basics | Making models smaller by using less-precise numbers |
| 08 | The Distillation Idea | Teaching a small model to mimic a big one |

After completing all 8 modules, take the **Readiness Quiz** on Moodle.

## How to use the notebooks

All notebooks run on **Kaggle** with no GPU required (CPU is fine for pre-work).

1. Go to [kaggle.com](https://www.kaggle.com) and sign in (create a free account if you don't have one)
2. Create a new notebook
3. Copy the notebook content or upload the `.ipynb` file
4. Run all cells — everything should work out of the box

## About the dataset

Several modules use the dataset we'll work with all semester: **consumer complaints** submitted to the U.S. Consumer Financial Protection Bureau. You'll classify complaint text into issue categories. Getting familiar with this data now means you can focus on the engineering decisions from Day 1.

## The readiness quiz

The quiz on Moodle covers all 8 modules. It's designed to check that you understood the key ideas, not to trick you. If you did the modules, you'll be fine.

---

*Questions? Post on the Moodle forum or email the instructor.*
