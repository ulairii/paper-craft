# Worked example: a sampler contribution

All methods, datasets, measurements, and numbers below are fictional. They illustrate writing decisions and must not be reused as experimental evidence.

## Supplied material

The author has a pretrained image denoiser and a sampler that reallocates its evaluation times using a pilot trajectory. The pilot evaluations count toward the total budget. Training, conditioning, and the denoiser are fixed. Lower FID is better.

| Sampler | Total network evaluations | FID on Dataset A | Seconds per image |
|---|---:|---:|---:|
| Uniform | 16 | 12.0 | 0.40 |
| Reallocated | 16 | 9.2 | 0.42 |
| Uniform | 32 | 8.8 | 0.80 |
| Reallocated | 32 | 8.5 | 0.82 |
| Uniform | 64 | 8.1 | 1.60 |
| Reallocated | 64 | 8.1 | 1.62 |

At 16 evaluations, removing the trajectory-dependent allocation gives FID 11.7. Reconstruction error against a high-step reference also decreases. Dataset B shows no clear benefit. Multiple-seed uncertainty and the exact allocation equation are not supplied.

## Draft abstract

Diffusion sampling with a limited number of network evaluations requires choosing where to spend those evaluations along the denoising trajectory. We propose a sampler that uses a short pilot trajectory to allocate the remaining evaluations to intervals with larger estimated integration error. The procedure reuses a pretrained denoiser and includes the pilot calls in its evaluation budget. On Dataset A, it reduces FID from 12.0 to 9.2 at 16 evaluations, with a small increase in measured latency. The advantage narrows as the budget increases and is absent on Dataset B. These results identify trajectory-dependent allocation as a useful option for low-budget sampling in the evaluated setting.

## Draft introduction passage

A fixed sampling grid spends its evaluations according to a schedule chosen before generation. Under a small evaluation budget, this may allocate too few updates to the portions of a trajectory that are harder to integrate. We investigate whether a short pilot trajectory can supply enough information to improve that allocation while preserving the same total number of denoiser calls.

Our method estimates the relative integration difficulty of candidate intervals and allocates the remaining evaluations accordingly. It changes the sampling schedule while retaining the pretrained denoiser. The key question is therefore whether information from the pilot is worth the evaluations it consumes. We answer this question by comparing the samplers at equal total evaluation counts and reporting their measured latency.

The strongest result occurs at 16 evaluations, where the proposed allocation reduces FID by 2.8 on Dataset A. Removing trajectory dependence largely removes this gain. At 64 evaluations, the samplers attain the same FID, and Dataset B shows no clear benefit. The contribution is a sampling rule for a specific constrained regime, supported by an experiment that links its advantage to the allocation decision.

## Draft method passage

Let a pretrained denoiser define the vector field used by the sampler. We first spend [PILOT EVALUATIONS] calls on a coarse trajectory and compute an interval score using [ERROR ESTIMATOR]. The score determines how the remaining calls are distributed through [ALLOCATION RULE AND EQUATION]. We then generate the final sample on the resulting grid. The complete procedure uses the stated budget, including every pilot and final-trajectory call.

The pilot supplies information about where additional evaluations may be useful; it does not train or modify the denoiser. The allocation rule [STATE ITS HANDLING OF MINIMUM INTERVALS AND REMAINING BUDGET] defines the method. Routine solver settings are reported in [SETUP LOCATION].

## Draft results passage

**The gain is concentrated at low evaluation budgets.** At 16 evaluations, trajectory-dependent allocation reduces FID from 12.0 to 9.2, while latency rises from 0.40 to 0.42 seconds per image. It approaches the quality of the 32-evaluation uniform sampler, which attains FID 8.8 at 0.80 seconds. At 64 evaluations, both methods attain FID 8.1. Thus, the result supports better use of a small evaluation budget rather than lower per-call cost or uniformly better asymptotic quality.

**The allocation decision explains much of the measured advantage.** Removing trajectory dependence raises FID from 9.2 to 11.7 at the same 16-evaluation budget, close to the uniform sampler's 12.0. The lower error against the high-step reference is consistent with improved numerical integration. That error measures agreement with a reference trajectory; the FID comparison provides separate evidence about generated samples. [ADD UNCERTAINTY FROM THE AVAILABLE REPEATED RUNS.] Dataset B does not show the same benefit, so the evidence does not establish a dataset-independent advantage.

## Why this structure works

The same-denoiser comparison follows the sampler-focused argument in [DDIM](papers/P05.md). Separating numerical error from sample quality follows [Flow Matching](papers/P07.md). Reporting the narrowing advantage across budgets follows the useful-regime explanation in [Rectified Flow](papers/P08.md). These are writing influences, not citations that establish the fictional method's novelty. A real related-work section must position the actual allocation rule against scientifically relevant prior methods.
