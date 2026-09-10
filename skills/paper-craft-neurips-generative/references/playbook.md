# NeurIPS generative models: writing playbook

## Choose a reason for the paper to exist

A generative-model paper can introduce a learning principle, remove an obstacle, expose a useful design choice, or improve an operating point. [GANs](papers/P01.md) makes a new learning interaction understandable. [NVAE](papers/P07.md) shows how architecture strengthens a familiar statistical family. [DPM-Solver](papers/P10.md) exploits mathematical structure to reduce sampling work. These are different stories, and each calls for a different opening and leading experiment.

Write a provisional central sentence from the author's evidence. For example: “Most of the gain comes from allocating evaluations differently, so existing checkpoints can benefit.” That sentence implies a fixed-checkpoint experiment, a quality–cost figure, and a method section centered on allocation. It does not require a broad claim about replacing diffusion models.

## Four narrative patterns worth borrowing

### A sound principle has a practical obstacle

[WGAN-GP](papers/P03.md) retains the motivation for Wasserstein learning and diagnoses weight clipping. The diagnosis makes the replacement feel necessary. A small controlled example explains the issue before large-scale results establish usefulness.

Use this pattern when an existing idea fails for an identifiable reason. Name the failure, show what it prevents, and explain why the proposed change targets it. A result paragraph should connect the repair to the observed behavior, not merely state that the final model scores better.

### A small operation changes what the model can express

[Glow](papers/P04.md) centers learned invertible mixing; [Neural Spline Flows](papers/P05.md) centers flexible scalar transformations. Both give mathematical tractability a practical role. The reader can see how a local operation changes the capabilities of a larger architecture.

Explain the old operation, its restriction, and the new operation in that order. A compact table aligning forward computation, inverse, and determinant can be more useful than several pages of architecture description. Credit the prior mathematical construction and explain the adaptation that makes it useful here.

### A common representation reveals independent improvements

[EDM](papers/P09.md) uses a design table to make a crowded literature understandable. It first changes samplers on existing networks, then changes training with a fixed sampler. The experimental sequence mirrors the conceptual separation.

A unification paper should give the reader something useful before its best score: a clearer way to compare methods, a reusable formulation, or a previously hidden degree of freedom. Explain how that perspective leads to a new choice. An unexplained extra hyperparameter is not automatically worth adding; EDM's appendix discusses a small solver-parameter improvement that the authors leave out of the final design.

### A metric disagreement reveals what the model is doing

[DDPM](papers/P06.md) develops a compression interpretation when strong samples do not coincide with leading likelihood. [Classifier guidance](papers/P08.md) uses precision and recall to explain what stronger conditioning changes. These papers give less favorable measurements an explanatory role.

State the observation first, then the interpretation and its limit. For example: “Increasing guidance improves precision but reduces recall; the intermediate setting gives the best FID.” Do not describe this as improvement on every axis. The tradeoff itself can be a useful capability.

## Make each experiment answer a different question

| Question | Useful comparison | How to write the implication |
|---|---|---|
| Does the principle work? | Representative synthesis and an appropriate quantitative measure | Explain the demonstrated capability, as in GANs. |
| Why does the repair help? | A controlled failure case and a targeted replacement | Connect the change to the obstacle, as in WGAN-GP. |
| Which part of the recipe matters? | Components compared under a common setting | Explain different roles, as in Improved GANs and NVAE. |
| Is the building block useful beyond one model? | Insertion into several relevant architectures or tasks | State where flexibility helps and where it adds little, as in spline flows. |
| Is the improvement in training or sampling? | Fix one while changing the other | Separate the contributions, as in EDM. |
| Is sampling practically faster? | Quality versus evaluations, supported by runtime | State the operating point, as in DPM-Solver. |
| What does control change? | Fidelity and coverage across a control parameter | Explain the useful balance, as in classifier guidance. |

Use the supplied experiments to answer the questions they actually address. Missing facts can receive specific placeholders. Suggestions for further experiments should be short and separate from the requested manuscript.

## Write result paragraphs that advance the argument

Start with the finding, identify the informative comparison, and explain its consequence. An original pattern is:

> With the same pretrained network, [sampler] reaches [quality] using [evaluations], compared with [baseline budget]. The matched-order comparison retains this advantage, suggesting that exploiting [structure] contributes beyond increasing solver order. The smaller gain at [larger budget] places the main benefit in the few-evaluation regime.

Use the author's evidence for every filled value. A convergence-order result supports a numerical statement under its assumptions; it does not prove perceptual quality. A capacity comparison supports a parameter-efficiency statement; it does not automatically establish faster training. These distinctions make the explanation sharper without turning the prose into a checklist.

## Decide what belongs in the main text

The main method should include the object being modeled, the changed operation, and the connection between training and generation. A setting belongs beside a result if changing it changes the result's meaning: lower temperature, classifier guidance, selected samples, image bit depth, or a different reference distribution.

Full optimizer inventories and extended derivations usually belong in supporting material. A detail can move forward when it becomes the explanation: NVAE's normalization recalibration matters for its samples; spline inversion matters for tractability; DPM-Solver's network-evaluation count matters for speed. Placement follows the reader's question, not a fixed quota of implementation details.

## Use plain language to sell a precise contribution

| Weak or inflated wording | More useful wording |
|---|---|
| “A revolutionary generative paradigm.” | “A generator learns from a discriminator that distinguishes its samples from data.” |
| “All components synergistically improve performance.” | “Feature matching helps classification; minibatch discrimination improves the synthesis recipe.” |
| “Exact generation in ten steps.” | “The solver integrates the linear term analytically and approximates the remaining neural-network integral.” |
| “Better quality without compromise.” | “Guidance raises precision while reducing recall, with the best FID at an intermediate scale.” |
| “Universally optimal design.” | “The same sampler improves several pretrained models; stochastic settings remain model-dependent.” |

Keep one name for each concept. Avoid renaming standard operations to manufacture novelty. Make the contribution memorable through the obstacle removed and the capability gained.
