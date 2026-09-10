# ICLR generative models: writing playbook

## Find the smallest explanation that carries the paper

Begin with the problem made visible by the results. “Generation is expensive” is broad; “the same denoiser loses quality when its stochastic sampler is shortened” points toward a sampler contribution. DDIM uses the dependence on noisy marginals to explain how sampling can change without retraining ([P05](papers/P05.md)). Its contribution can be stated in a sentence before the full variational construction appears.

A system paper needs a different opening. SDXL attaches design choices to small-image artifacts, cropped objects, aspect ratios, and local detail ([P09](papers/P09.md)). Group a system around these problems, then explain how the final pipeline combines the remedies. Do not disguise an integrated empirical result as an isolated theorem about one component.

For a methods paper, distinguish the obstacle from the technique. AEVB's reparameterization matters because it supplies useful gradients for latent-variable learning ([P01](papers/P01.md)). Flow Matching's conditional regression matters because the marginal target cannot be evaluated directly ([P07](papers/P07.md)). The opening should make the need for the technique clear before naming it.

## Make the abstract a short argument

A useful order is: concrete limitation; key observation; construction; strongest result with its setting; resulting capability or useful regime. Omit a historical tour of deep learning. If the contribution is a tradeoff, state the tradeoff. BigGAN's truncation controls fidelity and variety rather than maximizing both simultaneously ([P04](papers/P04.md)).

Prefer “At 16 network evaluations, the sampler improves FID from [A] to [B] using the same denoiser” to “Extensive experiments demonstrate remarkable efficiency.” If the supplied evidence is about iterations, do not silently convert it into wall-clock savings. If several configurations supply different best results, keep them distinct.

## Give formulas a role in the narrative

Introduce each equation with the question it answers and follow it with its practical consequence. For a surrogate objective, use this progression:

1. Define the quantity the method wants to optimize.
2. Identify the inaccessible expectation, posterior, or vector field.
3. Construct a target that can be sampled or evaluated.
4. Explain the equivalence, bound, or approximation connecting the two.
5. State what training and inference now require.

Flow Matching demonstrates this progression with conditional and marginal fields ([P07](papers/P07.md)). Real NVP uses a complementary construction: the desired inverse and determinant determine the structure of a coupling layer ([P02](papers/P02.md)). In both cases, the mathematics answers a practical question.

Keep theoretically different objects distinct. Rectified Flow separates the first fitted flow, a new coupling produced by reflow, and distillation of a final mapping ([P08](papers/P08.md)). A reader should know which stage produces the claimed one-step behavior.

## Give each experiment one job

A strong main-result paragraph does more than announce a winning cell. Name the useful regime, identify the most revealing comparison, and explain what follows. For example: “The advantage is largest at short trajectories. With the same denoiser, [method] improves [metric] at [budget], while the gap narrows at [larger budget]. This supports its use when latency limits the number of updates.”

Separate three common questions:

| Question | Useful evidence | What the paragraph explains |
|---|---|---|
| Does the proposed change help? | Same model or matched configuration with the change varied | The specific behavior changed |
| Why might it help? | A mechanism-sensitive intervention or measurement | Agreement with the proposed explanation |
| Where is it useful? | Budget, scale, data, or task variation | The useful regime and its boundary |

Spectral Normalization uses singular-value measurements and a dimension sweep to investigate its capacity explanation ([P03](papers/P03.md)). BigGAN follows a spectral observation with interventions that fail to remove collapse ([P04](papers/P04.md)). A failed intervention can improve the paper by narrowing the explanation.

Use the experiments already available. If a necessary result is missing, write a specific placeholder or narrow the sentence. Do not make an author wait through repeated speculative experiment planning before receiving a draft.

## Explain metric disagreements instead of smoothing them away

Likelihood concerns density modeling; reconstruction measures recovery of a particular input; FID compares feature distributions; a reward measures what its definition rewards. They are not interchangeable measures of a single “quality.”

The score-SDE paper uses different configurations for best likelihood and best samples ([P06](papers/P06.md)). Flow Matching's super-resolution result improves perceptual distribution metrics while lowering reconstruction metrics ([P07](papers/P07.md)). SDXL reports that COCO FID and user preferences rank models differently ([P09](papers/P09.md)). DDPO shows that successful reward optimization can eventually produce undesirable outputs ([P10](papers/P10.md)).

Write the conclusion at the level of the evidence: “preferred for prompt adherence in this study,” “lower FID at this budget,” or “higher predicted aesthetic reward.” Then explain why that outcome matters for the intended use.

## Keep the main text selective

Retain the details that define the scientific comparison: conditional versus unconditional generation, external supervision, the model being reused, sampling evaluations, and the operating point. Put routine constants and repeated examples elsewhere. A lengthy hyperparameter inventory before the method's idea makes the contribution harder to understand.

A caption should identify the comparison and tell readers what to look for. An example should illustrate a described behavior, such as retained high-level structure or a cropping effect. Do not infer a general success rate from a few displayed samples.

## Replace decoration with the contribution

| Vague wording | More useful wording |
|---|---|
| “A novel and elegant generative paradigm” | “A conditional regression objective for learning the transport field” |
| “Negligible overhead” | “Adds [measured cost] under [setting]” |
| “Optimal transport guarantees superior samples” | “The conditional paths are straight; the experiments examine whether this improves coarse-step sampling” |
| “More stable and better in every respect” | “Improves the tested stability measure, with [quality or cost consequence]” |
| “Human-aligned without supervision” | “Fine-tuned with a pretrained reward model, without collecting additional annotations” |

Use direct claims where results are clear. Reserve “suggests” and “may” for explanations or extensions that remain uncertain. The goal is a readable argument with a definite contribution, not a paragraph of praise followed by a paragraph of disclaimers.
