# Worked example: from supplied results to a draft

All method descriptions and numbers below are fictional teaching material, not results from the reference papers. The draft demonstrates how to build a specific RL story without inventing missing experiments.

## Supplied material

An author proposes allocating a fixed number of synthetic transitions according to a score computed from a learned dynamics model. The exact score is not yet supplied. The baseline uses uniform allocation. Both systems use the same real dataset, model, policy optimizer, and synthetic-transition budget.

| Dataset regime | Uniform allocation | Proposed allocation | Shuffled allocation scores |
|---|---:|---:|---:|
| Narrow data | 42 | 58 | 44 |
| Mixed data | 63 | 68 | 64 |
| Broad data | 80 | 81 | 80 |

Scores are fictional mean normalized returns over five trained models. Per-run scores, task identities, normalization references, and uncertainty estimates are not supplied. Training takes 2.0 hours for uniform allocation and 2.1 hours for the proposed method on the same unspecified hardware. No online fine-tuning is used. Hyperparameter-selection access is not specified.

## Draft

### Title

Allocating Synthetic Experience for Offline Policy Learning

### Abstract

Model-based offline reinforcement learning augments a fixed dataset with synthetic transitions, but a fixed generation budget need not be equally useful across starting states. We study allocation of that budget using a score derived from the learned dynamics model. The resulting procedure changes where synthetic experience is generated while retaining the model, policy optimizer, and total transition budget. In the supplied evaluation, allocation improves mean normalized return from 42 to 58 on narrow data and from 63 to 68 on mixed data, with little change on broad data. Shuffling the allocation scores reduces these gains. These results suggest that the assignment of synthetic experience matters most in the evaluated restricted-data regime, at a small increase in measured training time.

### 1. Introduction

A learned dynamics model can provide additional transitions for an offline policy learner. Once a generation budget is fixed, however, the learner still faces an allocation decision: from which states should those transitions begin? Uniform allocation treats starting states alike even when their usefulness for policy learning differs.

We investigate whether changing this allocation improves the use of a fixed synthetic-data budget. Our method assigns generation effort using a score computed from the learned dynamics model. It leaves the remaining learning pipeline unchanged, making allocation the central design choice. [Insert the specific observation motivating the score once its definition is supplied.]

The experiments compare score-based allocation with uniform allocation and a control that shuffles scores across starting states. The largest improvement occurs on narrow data, while the broad-data result changes little. This pattern identifies a useful regime for allocation and motivates examining the relationship between dataset coverage and synthetic experience. Our contribution is the allocation rule and its controlled evaluation, rather than a new dynamics-model family or policy optimizer.

### 2. Related work

Short model rollouts can improve the use of real interactions, as demonstrated by MBPO [P03]. Offline model-based learning additionally needs to manage the consequences of learning from a fixed dataset; COMBO [P10] studies conservative value regularization on model-generated states. Our work concerns a different choice within model-based learning: how to allocate a fixed generation budget across starting states. The shared model and optimizer allow the experiments to focus on that choice. [Add the scientifically closest allocation methods from the author's literature review.]

### 3. Method

We consider offline policy learning from a fixed transition dataset. A dynamics model is trained on that dataset and supplies synthetic transitions for the policy learner. Both the proposed method and the uniform baseline use the same model and learning objective.

Let the eligible starting states be drawn from [specify the source distribution]. For each state, we compute [insert the score definition, its required inputs, and the reason it should identify useful starting states]. We convert these scores into allocation probabilities using [insert the transformation and any normalization or clipping]. Synthetic rollouts begin from the resulting distribution until the fixed transition budget is exhausted.

The allocation changes the distribution of generated experience while preserving its total amount. [Specify rollout length, how model and real transitions enter policy updates, and the underlying optimizer.] No online fine-tuning is used. [Specify hyperparameter-selection access separately from policy training.]

### 4. Experiments

We ask whether informed allocation improves offline learning at a fixed synthetic-transition budget, and whether its benefit varies with the supplied data regime. [Insert task identities, data-construction details, and the normalization reference.] Reported means use five independently trained models. [Insert the available per-run uncertainty summaries.]

**Allocation matters most on narrow data.** The proposed allocation raises mean normalized return from 42 to 58 in the narrow-data setting. The improvement is smaller on mixed data, from 63 to 68, and nearly absent on broad data, from 80 to 81. Thus the observed benefit is concentrated in the more restricted dataset regime. This pattern is consistent with allocation becoming less consequential when the available data already support effective learning; it does not isolate coverage as the sole explanation.

**The association between scores and states contributes to the gain.** Shuffling the scores lowers the narrow-data result from 58 to 44, close to the uniform baseline of 42. The corresponding mixed-data result falls from 68 to 64. Because the generation budget and surrounding learner remain fixed, this comparison supports the usefulness of the assignment encoded by the scores. It does not by itself establish that the scores are calibrated estimates of model error.

**The gain incurs modest measured training overhead.** Training time increases from 2.0 to 2.1 hours in the supplied measurement. The method therefore improves return at a fixed synthetic-transition budget rather than reducing that budget or wall-clock time. [Insert the hardware and timing scope.] No conclusion about action-selection latency follows from this measurement.

### 5. Conclusion

Allocating synthetic experience by a learned-model score improves offline policy learning in the evaluated narrow-data regime. The equal-budget comparison and shuffled-score control support the importance of where synthetic experience is generated. Limited change on broad data defines a boundary of the observed benefit and motivates further study of when allocation is useful.

## Craft behind the draft

[MBPO](papers/P03.md) informs the separation of model use from extra optimization. [COMBO](papers/P10.md) informs the focus on a specific distribution choice and its natural comparator. [TD3+BC](papers/P08.md) informs the direct quality–cost explanation. [Statistical Precipice](papers/P09.md) informs the distinction between reported means and uncertainty not supplied by the author.

The draft uses a contribution, mechanism, evidence, and interpretation in connected prose. Missing factual inputs remain localized placeholders; the writing task still produces a usable manuscript.
