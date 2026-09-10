# Worked example: distilling an argument for a self-correction paper from SCoRe

Source: [P06 — Training Language Models to Self-Correct via Reinforcement Learning](papers/P06.md), ICLR 2025. This is a reverse analysis and original writing demonstration, not a sentence-by-sentence imitation or an invented completed method.

## 1. The central story is more than an RL and two-stage label

The transferable argument is:

1. The desired capability is to fix one's own errors while preserving correct answers.
2. Errors in offline self-correction training may differ from those the model actually produces (Section 4/Fig. 4, p. 5).
3. Even with online training, the model may learn not to make meaningful revisions (Section 5/Fig. 5, p. 6).
4. Training therefore needs to address both the error distribution and incentives for revision. These two problems motivate the responsibilities of Stage I and Stage II (Fig. 6, p. 7).
5. Evaluation must measure how answers change, not only second-attempt accuracy (Tables 2 and 4, pp. 9–10).

**Distilled recommendation.** If a user's new method has two components, first check whether there are two distinguishable failure mechanisms. Without diagnostic experiments, copying this structure would turn hypotheses into supposed findings.

## 2. Transferable introduction paragraph roles

| Paragraph | What the reader needs to understand | Required evidence | What does not belong here |
|---|---|---|---|
| 1 | Why revision has distinct value | Difference between first-attempt solving and revision | General LLM history |
| 2 | Where existing revision training fails | Distribution-shift and revision-behavior diagnoses | An untested claim that every method fails |
| 3 | Why the simple remedy is insufficient | A control showing collapse persists online | A list of component names before motivation |
| 4 | Which problem each training stage addresses | A correspondence between diagnoses and mechanisms | Complete hyperparameter tables |
| 5 | Which results support the contribution and its scope | Net revision gain, first-attempt capability, critical ablations | Unconditional generality or uniqueness |

This does not prescribe five paragraphs for every ICLR introduction. It assigns one argumentative responsibility to each paragraph.

## 3. Why a single improvement number is insufficient

P06 Table 2 ([official PDF, p. 9](https://proceedings.iclr.cc/paper_files/paper/2025/file/871ac99fdc5282d0301934d23945ebaa-Paper-Conference.pdf#page=9)) reports the following MATH evaluation:

| System | First-attempt accuracy | Second-attempt accuracy | Second minus first |
|---|---:|---:|---:|
| Base model | 52.6% | 41.4% | −11.2 pp |
| SCoRe | 60.0% | 64.4% | +4.4 pp |

This gives three different answers:

- How much does one SCoRe revision add? **4.4 percentage points**.
- How much does SCoRe improve the net revision gain relative to the base model? **15.6 percentage points**, calculated as 4.4 − (−11.2).
- How much higher is SCoRe's second-attempt accuracy than the base model's? **23.0 percentage points**. This combines changes in first-attempt capability and revision behavior; it cannot all be attributed to revision capability.

The table also reports SCoRe's incorrect→correct transitions at 5.8% and correct→incorrect transitions at 1.4%, both over all problems. Their difference is the 4.4 pp net gain. A correction rate conditional on an initially wrong answer requires the number of first-attempt errors as its denominator; it cannot reuse 5.8%. Percentages and percentage points must also remain distinct.

## 4. A more convincing interpretation paragraph

An unsuitable summary:

> Our two-stage framework improves self-correction by 15.6 points, demonstrating robust reasoning.

This omits the metric's meaning and expands a task result into an undefined claim of robust reasoning.

The following is newly written prose based on published data, **not a source quotation**:

> On the reported MATH evaluation, SCoRe increases accuracy from 60.0% on the first attempt to 64.4% after revision. Corrections and regressions account for 5.8% and 1.4% of all problems, respectively, yielding a net gain of 4.4 percentage points. The base model instead loses 11.2 points after revision. These results support improved revision behavior in this setting; the ablations separately examine which training components contribute to that behavior.

The paragraph moves from measurement to behavior, then assigns the training-design question to ablations. The accuracy table alone does not establish the full causal account of the two-stage mechanism.

## 5. Make experiments serve contribution claims

| Claim | Critical control | How to narrow the conclusion if evidence is insufficient |
|---|---|---|
| Online first-attempt distributions matter | Remove online first-attempt samples and compare first-attempt and revision changes | Claim effectiveness of the complete training procedure, not attribution to distribution matching |
| Stage I has a distinct role | Remove Stage I while holding other settings as constant as possible | If final performance is similar, do not keep presenting it as an essential innovation |
| Progress shaping changes revision behavior | Remove shaping and report both transition directions | Final accuracy alone cannot distinguish preservation from correction |
| The method beats another independent attempt | Match actual budgets for independent sampling and selection | If only attempt counts match, limit the conclusion to that comparison |

The first three controls correspond to Table 4. The last recommendation extends the sampling comparison in Section 6.2: a new paper should make token and auxiliary-model costs explicit. Do not claim the source already performed complete cost matching.

## 6. What cannot be inherited from this example

Training rewards are not test-time access to correct answers. Compare P03's critique of intrinsic self-correction and P06's training intervention in a shared table of conditions. The multi-turn plateau in Appendix A.3 limits a story of endless improvement with more thought. The ablations support the evaluated design; they do not establish RL as the only approach or two stages as necessary for every model.
