# Readiness Quiz — Moodle Import Instructions

## Quick setup

1. In your Moodle course, go to **Question bank** > **Import**
2. Select format: **GIFT format**
3. Upload `quiz.gift`
4. Click **Import**

This creates 20 questions organized into categories by module.

## Creating the quiz activity

1. **Add an activity** > **Quiz**
2. Name: "Pre-Work Readiness Quiz"
3. Recommended settings for "only counts if it's good":

### Option A: Practice quiz (doesn't count)
- Grade category: set to **exclude from final grade**
- Attempts allowed: **Unlimited**
- Grading method: **Highest grade**
- This lets students retry until they understand the material

### Option B: Counts only if helpful (recommended)
- Grade category: fold into **Participation (5%)**
- Attempts allowed: **Unlimited**
- Grading method: **Highest grade**
- Set the quiz weight very low (e.g., 1 out of 20 participation points)
- Students who do it get a small boost; students who skip it lose almost nothing

### Option C: Minimum threshold gate
- Attempts allowed: **Unlimited**
- Add a **completion condition**: "Receive a grade" with minimum grade of 70%
- Make Week 1 materials conditionally available: "Readiness Quiz must be complete"
- This ensures everyone did the pre-work without making the grade punitive

## Question breakdown

| Module | Questions |
|--------|-----------|
| 01 Tokenization | 4 |
| 02 Pretrained Encoders | 2 |
| 03 Train vs Eval Mode | 3 |
| 04 Confusion Matrices | 3 |
| 05 Calibration | 3 |
| 06 LoRA/PEFT | 2 |
| 07 Quantization | 2 |
| 08 Distillation | 3 |
| **Total** | **22** |
