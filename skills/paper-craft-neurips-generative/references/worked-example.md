# Worked example: writing a sampling paper from existing results

All methods, datasets, measurements, and names in this example are fictional. The prose demonstrates writing craft; it is not a report of an actual experiment or a template for invented results.

## Supplied evidence

The author has a fixed pretrained diffusion model and proposes an interval-allocation rule. It gives more evaluations to an intermediate denoising range, selected from a small calibration set. There is no retraining. The current record does not specify the exact rule, calibration cost, or metric uncertainty.

| Dataset A sampler | Evaluations | FID ↓ | Seconds per batch ↓ |
|---|---:|---:|---:|
| Uniform baseline | 12 | 12.0 | 1.2 |
| Proposed allocation | 12 | 7.0 | 1.2 |
| Uniform baseline | 24 | 7.1 | 2.4 |
| Proposed allocation | 24 | 6.7 | 2.4 |
| Uniform baseline | 60 | 6.5 | 6.0 |
| Proposed allocation | 60 | 6.5 | 6.0 |

At 12 evaluations, allocating more work only near the final denoising stage gives FID 9.4. On Dataset B, the uniform and proposed schedules give 10.2 and 10.0. All within-dataset comparisons use the same checkpoint, solver order, conditioning, and metric protocol. No likelihood or coverage results are supplied.

The story is improved allocation under a small evaluation budget. The Dataset B result limits the current scope. The narrative borrows the fixed-checkpoint logic of [EDM](papers/P09.md) and the operating-point emphasis of [DPM-Solver](papers/P10.md); it does not claim those papers studied this fictional rule.

## Draft

### Title

Allocating Denoising Evaluations for Faster Diffusion Sampling

### Abstract

Diffusion sampling can waste a limited evaluation budget when a fixed schedule assigns computation to intervals that contribute little to final sample quality. We introduce a calibrated allocation rule that redistributes evaluations across the denoising trajectory without retraining the model. On Dataset A, the proposed schedule reaches FID 7.0 with 12 evaluations, comparable to the uniform schedule's 7.1 with 24 evaluations, and reduces measured batch sampling time from 2.4 to 1.2 seconds. The advantage decreases as the budget grows and is small on Dataset B. These results identify evaluation allocation as a useful way to improve low-budget sampling for the tested Dataset A model, while indicating that its benefit depends on the model and data.

### 1. Introduction

Fast diffusion sampling requires more than choosing how many times to evaluate a denoiser. It also requires deciding where those evaluations should occur. Under a small budget, an evaluation assigned to an uninformative interval cannot be used where the trajectory is harder to approximate. This makes allocation a practical design choice even when the pretrained model and numerical solver remain fixed.

We study a calibrated allocation rule that concentrates evaluations in an intermediate denoising range. The rule uses [calibration statistic and selection procedure] and then fixes the schedule for generation. It changes neither the model parameters nor the solver order. The resulting comparison therefore asks a focused question: can a better schedule extract more sample quality from the same number of denoiser evaluations?

On Dataset A, the answer is positive in the low-budget regime. Twelve evaluations with the proposed allocation achieve approximately the FID of 24 uniformly allocated evaluations, with half the measured batch sampling time. The gap largely disappears at larger budgets, and the improvement on Dataset B is small. Our contribution is a useful allocation strategy and an empirical account of its operating range, rather than a claim that one schedule is best for every model.

### 2. Related work

Prior diffusion work has improved both the trained model and the procedure used to sample it. EDM separates these design choices and demonstrates sampler improvements with fixed pretrained networks [P09]. DPM-Solver exploits the structure of the diffusion ODE to improve numerical efficiency [P10]. Our study instead holds the checkpoint and solver order fixed to examine how a limited evaluation budget is distributed along the trajectory. [Add the closest scheduling methods and explain the exact difference from each.]

### 3. Method

Let the sampler use a budget of K denoiser evaluations between its initial and final noise levels. The baseline distributes those evaluations according to [the exact uniform coordinate]. Our method replaces that schedule with one derived from [calibration statistic]. It first measures [quantity] on [calibration data], then assigns interval boundaries through [allocation equation]. The schedule remains fixed when sampling new images.

This change preserves the pretrained denoiser and the numerical update rule. Its purpose is to allocate the existing budget more effectively. The calibration procedure requires [cost], which is incurred before sampling and should be distinguished from the per-batch runtime reported below. The full allocation formula and endpoint treatment must be specified before the method is reproducible.

### 4. Experiments

We compare schedules using the same checkpoint, solver order, conditioning, and evaluation protocol within each dataset. FID is computed from [sample count] generated images against [reference set]. Runtime is measured at batch size [batch size] on [hardware]. We report [uncertainty protocol when available].

**Low-budget sampling.** On Dataset A, changing only the allocation lowers FID from 12.0 to 7.0 at 12 evaluations, with the same 1.2-second batch runtime. The uniform schedule requires 24 evaluations and 2.4 seconds to reach a comparable FID of 7.1. The useful gain is therefore a better quality–time operating point, rather than a reduction in the cost of an individual evaluation.

**Where to allocate computation.** Concentrating evaluations only near the final denoising stage gives FID 9.4, compared with 7.0 for the proposed schedule at the same budget. This comparison supports the value of the selected intermediate range in this setting. It does not establish that the same range is optimal for every model or that a particular trajectory-error mechanism has been isolated.

**Budget and dataset dependence.** At 24 evaluations, the FID difference narrows to 7.1 versus 6.7. At 60 evaluations, both schedules reach 6.5. Allocation matters most when the budget leaves little room to resolve the trajectory. On Dataset B, the change from 10.2 to 10.0 is small, so the current evidence supports a strong benefit for Dataset A rather than a broad cross-dataset claim.

### 5. Conclusion

Redistributing a fixed sampling budget improves the quality–time tradeoff for the tested Dataset A diffusion model without retraining. The diminishing gain at larger budgets clarifies where the method is useful, while the small Dataset B effect motivates studying how allocation should depend on the model and data. The present results concern FID and sampling time; they do not establish changes in likelihood or distribution coverage.

## Why the draft is organized this way

The abstract names the operating point and its boundary. The introduction makes allocation a concrete problem before introducing the method. The main experiment isolates the schedule; the second explains its placement; the final comparison establishes scope. Missing method facts remain visible placeholders, while available results are written as manuscript prose.

P09 and P10 identify the source papers in this skill's [corpus](corpus.md). A real manuscript should use normal bibliography citations and include the closest scheduling work, rather than copying this example's short reference labels.
