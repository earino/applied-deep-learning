---
title: "Week 4 Memo Rubric"
subtitle: "Error Diagnosis — Slices, Calibration, Cross-Model Analysis"
author: "ECBS5200 — Practical Deep Learning Engineering"
titlepage: false
toc: false
geometry: margin=1in
---

# Week 4 Technical Note — Rubric

**ECBS5200 — Practical Deep Learning Engineering for Applied ML**

**Deliverable:** Week 4 Technical Note
**Format:** 2–3 pages maximum (not counting tables, figures, or experiment log)
**Total points:** 100

## Overview

The Week 4 Technical Note demonstrates that you can take two trained models with similar aggregate metrics, apply a diagnostic toolkit, and reach defensible conclusions about which to trust and for what. You are not graded on *which* model you recommend — you are graded on whether your conclusions are supported by evidence, whether you know the limits of that evidence, and whether you can say "I don't know" when the data doesn't settle the question.

## Rubric

### 1. Slice Analysis — Where Do the Models Differ? (20 points)

*Focus: subset-level evaluation, interpretation of null and non-null axes.*

| Level | Points | Criteria |
|---|---|---|
| **Excellent** | 18–20 | **Evidence:** Reports per-slice macro F1 for at least 4 of the 6 axes in the homework, for both models, with slice sizes. Cites specific numeric deltas to support claims. Discusses BOTH a signal-bearing axis and the null-result axis. **Reasoning:** For the signal axis, offers a plausible mechanistic story about why the gap appears where it does, grounded in what the slice represents (e.g., "the decoder's advantage on redacted text is consistent with its more heterogeneous pretraining data"). For the null axis, treats the null as evidence, not silence. |
| **Satisfactory** | 12–17 | Reports at least 2–3 slice axes with numbers, but either omits the null result, offers interpretations without specific numbers, or discusses only where the gap is biggest without engaging with where it vanishes. |
| **Needs Improvement** | 0–11 | Reports aggregate F1 without per-slice breakdown, or reports per-slice numbers without interpretation. Missing the null-result axis entirely. |

**What we're looking for:** Slice analysis is useful only insofar as you can read it. A table of numbers is not the deliverable — the *interpretation of those numbers* is. We specifically reward students who treat a null-result axis as informative ("opener_I showed essentially identical performance on both models — whatever advantage the decoder has, it doesn't come from personal-framing complaints").

### 2. Calibration — Which Can You Trust? (20 points)

*Focus: ECE measurement, temperature scaling, ranking robustness.*

| Level | Points | Criteria |
|---|---|---|
| **Excellent** | 18–20 | **Evidence:** Reports ECE for both models pre-scaling and post-scaling. Reports the fitted T values. Confirms macro F1 is unchanged by scaling (T-invariance). **Reasoning:** Answers the ranking question directly — if one model is better-calibrated pre-scaling, is that still true post-scaling? Articulates the practical implication: if you use confidence as a deployment gate (e.g., "only act on predictions above 0.9"), which model's confidence can you trust? |
| **Satisfactory** | 12–17 | Reports pre/post ECE numbers and T values, but the ranking question is treated superficially ("both are similar after scaling") without engaging with the practical consequence. |
| **Needs Improvement** | 0–11 | Missing ECE measurement, or reports only pre-scaling ECE, or reports temperature scaling changing macro F1 (indicates implementation error). |

**What we're looking for:** Graduate-level calibration literacy. The memo should reflect that ECE is a binned estimator with caveats (cite Chidambaram 2024 if you read it), that temperature scaling is only one of several fixes, and that calibration quality should be evaluated separately from classification quality. A student who concludes "temperature scaling fixes everything" has over-read the result.

### 3. Confusion-Matrix Insight — Where Do Rare-Class Errors Land? (25 points)

*Focus: tier-level error distribution + per-class drill-down + operational implications.*

| Level | Points | Criteria |
|---|---|---|
| **Excellent** | 22–25 | **Evidence:** Reports the tier-level breakdown (tail → head / mid / tail-other percentages) for at least one model. Reports confusion patterns for the 3 worst-performing classes with specific class-pair examples. **Reasoning:** Characterizes whether confusions are semantically coherent (similar-topic classes confused with each other) or arbitrary, with specific class pairs as evidence. Draws an operational conclusion — e.g., "these confusions suggest class-family merges rather than class weighting would be the right intervention" — that is supported by the observed confusion pattern. |
| **Satisfactory** | 15–21 | Reports the tier breakdown and some per-class confusions but the characterization of the confusion pattern stays surface-level ("the model gets confused between similar classes") without specific pairs, or misses the operational implication. |
| **Needs Improvement** | 0–14 | Missing the tier breakdown or the per-class drill-down. Observations not supported by specific class names / numbers from the student's own runs. |

**What we're looking for:** This section carries the most weight because it asks the hardest question — not *that* models fail, but *how* they fail. We want evidence the student looked at specific confused class pairs in their own data and extracted a pattern. A student who cites "Advertising and marketing, including promotional offers" being confused with "Rewards" (4 times) is showing exactly the kind of specific-evidence work the rubric rewards. A student who says "the model confuses similar classes" in the abstract has not done the work.

### 4. Is the Gap Real? Bootstrap & Noise Floor (20 points)

*Focus: statistical inference with noise-aware claims.*

| Level | Points | Criteria |
|---|---|---|
| **Excellent** | 18–20 | **Evidence:** Reports the 95% bootstrap CI for the encoder-vs-decoder macro F1 difference, with specific endpoints. Reports the fraction of resamples where one model exceeded the other. Notes the val-count histogram and how many classes sit in the n≤4 zone. **Reasoning:** Answers the "is the gap real?" question quantitatively — does the CI exclude zero, and if so, by how much. Acknowledges that bootstrap CIs capture only data-side variability (not model-side seed variability). Grades their own confidence: wide CI → weaker claim, narrow CI → stronger claim. |
| **Satisfactory** | 12–17 | Reports the CI endpoints but doesn't connect width-of-CI to strength-of-claim. Omits the n≤4 context. Treats "excludes zero" as a binary pass/fail without engaging with effect size. |
| **Needs Improvement** | 0–11 | Missing bootstrap analysis, or reports a point estimate without a CI, or treats the point estimate as the full answer. |

**What we're looking for:** Noise-floor aware claims. A student who writes "the decoder's macro F1 advantage is within the bootstrap CI [+0.011, +0.048], excluding zero with 99% consistency, but the lower bound is small enough that a factor-of-2 difference in deployment cost would dominate this quality gap" is showing the exact reasoning we want. A student who writes "the decoder is 0.03 better than the encoder" has not engaged with the noise floor at all.

### 5. Your Confidence in the Week 3 Deployment Recommendation (15 points)

*Focus: synthesis — how does a week of diagnostic evidence change (or fail to change) the Week 3 recommendation?*

| Level | Points | Criteria |
|---|---|---|
| **Excellent** | 13–15 | **Evidence:** References their own Week 3 memo's deployment recommendation. Cites at least two diagnostic findings from Sections 1–4 above that either confirm or complicate that recommendation. **Reasoning:** Articulates whether their confidence in the Week 3 recommendation has gone UP, DOWN, or shifted sideways (onto different axes than they originally considered). Names specifically what evidence would change their mind. |
| **Satisfactory** | 8–12 | Acknowledges the Week 3 recommendation but the synthesis with Week 4 findings is loose — cites a finding without tying it to the recommendation, or concludes "it depends" without specifying on what. |
| **Needs Improvement** | 0–7 | Missing synthesis. Either ignores Week 3 entirely, or treats Week 4's analysis as independent of the prior deployment question. |

**What we're looking for:** Intellectual honesty about updating (or not) in response to evidence. A student whose Week 3 recommendation was "deploy the decoder" and whose Week 4 diagnostic work makes them MORE confident in that — with specific supporting evidence — earns full marks. So does a student whose confidence shifts sideways: "I still recommend the decoder for accuracy-critical use cases, but the calibration finding means I'd add a post-hoc calibration step before deployment that I hadn't previously considered." A student who ignores their prior position or refuses to commit to a conclusion loses credit not for the conclusion but for the lack of engagement.

## General Notes

- **Conciseness is valued.** A tight 2-page memo covering all five sections clearly will score higher than a 5-page memo that buries insights in filler.
- **Exact numbers will vary.** Different bootstrap seeds, different qualitative tags, different class samples will produce different results. We grade reasoning about YOUR results, not whether you match specific targets.
- **No single right answer.** The deployment recommendation, the slice-pattern interpretation, the confusion-pattern characterization are all genuinely open. We grade the quality of the argument, not the conclusion.
- **Intellectual honesty is rewarded.** A student who writes "the bootstrap CI barely excludes zero, so I'm treating this as weak evidence" earns credit for engineering maturity — never loses credit for caution. A student who says "I don't know whether the gap is deployment-relevant without more data" with a reasoned justification is showing exactly what we want.
- **Tables and figures do not count toward the page limit.** Use them.
- **Readings can be cited.** If your argument uses a paper from `readings/week4/` (Guo 2017 on ECE, Oakden-Rayner 2020 on hidden stratification, etc.), name the author in-line. We are not grading citation format.
- **AI tools are allowed** for coding, experimentation, and drafting prose, but you must understand and be able to explain every claim in your memo.
