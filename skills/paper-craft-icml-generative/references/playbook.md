# Generative models: a writing playbook

## Turn the obstacle into the reason for the design

[WGAN](papers/P03.md) uses a simple distributional example to explain why a loss can fail to supply useful information. [Normalizing Flows](papers/P02.md) isolates a restrictive posterior family after acknowledging that scalable gradient estimation already exists. [Improved DDPM](papers/P04.md) starts from gaps in likelihood, coverage, and cost despite good samples. These openings make the method necessary through reasoning, without claiming that the whole field is broken.

A productive introduction follows the actual discovery: useful existing capability → specific obstacle → observation or diagnosis → proposed change → consequence. If the work is a system, explain which capability requires its components together. If it is an analysis, explain the phenomenon it makes intelligible. If it is a new data domain, identify the domain property that changes the modeling problem.

## Choose a contribution sentence with a real object

| Vague pitch | More informative object of contribution |
|---|---|
| A novel generative framework | A posterior family, objective, conditioning interface, sampler, or composition rule |
| Better generation | Higher fidelity, wider coverage, closer condition agreement, improved utility, or reduced cost |
| Efficient learning | Less paired data, fewer teacher trajectories, cheaper density computation, or lower training cost |
| A unified system | Named tasks served by the same representation and the task-specific changes still required |
| A theoretically grounded method | The stated assumptions, result, and concrete design or prediction it motivates |

[Stochastic Backpropagation](papers/P01.md) connects a recognition model and a variational objective to joint learning. [Consistency Models](papers/P06.md) specifies a mapping that supports both one-step generation and additional refinement. Neither needs vague adjectives to make the contribution recognizable.

## Explain the operation before the architecture inventory

For a distribution transformation, follow a sample and its density. For a guided generator, follow the condition into a reverse transition. For a distilled sampler, show what the teacher supplies and what the student predicts. For an energy composition, state the target distribution before its sampler.

[AudioLDM](papers/P08.md) is particularly useful for separating representations: the CLAP embedding supplies the condition, while diffusion generates a VAE latent that is decoded into audio. Collapsing these into “the latent space” hides the insight. [DSNO](papers/P10.md) similarly needs a clear distinction between diffusion time and image space: its Fourier operation couples the trajectory along time.

Introduce mathematical assumptions beside the claim they support. Save detailed proofs for supporting material, but retain the proof idea when it explains a design choice. Universal approximation, asymptotic correctness, and empirical accuracy are different claims with different evidential roles.

## Organize experiments as a sequence of answers

An **inference paper** can show a diagnostic where approximation error is visible, then test whether the improvement benefits a learned model. Separate the bound from an estimated likelihood.

A **sampling paper** should explain the operating point. Compare quality at the relevant budget, then use runtime and component studies to explain where the saving comes from. Distinguish preparation or distillation cost from generation cost. The common-teacher comparisons in Consistency Models and the per-call measurements in DSNO make these distinctions useful to readers.

A **conditional-generation paper** should address both realism and adherence. [GLIDE](papers/P05.md) turns disagreement between a learned metric and human preference into an important result. Treat an explanation for that disagreement as a hypothesis unless the experiments isolate it.

A **new-domain paper** should show why the adaptation matters in use. [TabDDPM](papers/P07.md) combines feature-distribution comparisons with train-on-synthetic, test-on-real utility. Its strong interpolation baseline changes the question from “can a deep model win?” to “what useful tradeoff does it offer?”

A **composition paper** can first show a known target distribution where failure is visible, then distinguish correcting the procedure from merely spending more computation. [Reduce, Reuse, Recycle](papers/P09.md) extends that reasoning to richer constraints and images. Qualitative showcases illustrate capabilities; they do not by themselves establish a universal success rate.

Choose the sequence supported by the author's results. These are reusable arguments, not mandatory batteries of experiments.

## Write result paragraphs around the revealing comparison

A useful paragraph states a finding, identifies the comparison that explains it, and gives its implication. Add a boundary if it changes that implication.

For example, Improved DDPM does not need to hide the worse FID of a likelihood-focused objective. That tradeoff explains the hybrid objective. AudioLDM's augmentation can improve human judgments without improving automatic scores; the paragraph should explain what each evaluation measures and what remains uncertain. WGAN's loss can be informative within a critic setup without becoming a universal cross-model ranking metric.

Avoid repeating every table entry. Use the contrast that distinguishes the proposed account from the obvious alternative: more capacity, more sampling work, a better teacher, weaker downstream evaluators, or a different conditioning signal.

## Decide which detail earns space

Keep details that define the scientific object: latent type, corruption process, objective roles, conditioning information, teacher, adaptation, and measured resource. A sample-count or evaluation-preprocessing difference belongs in setup when it changes how scores can be compared.

Move exhaustive settings and large prompt inventories to supporting material. Give an architectural width in the main narrative only if capacity itself is part of the argument. Describe extra pretrained components once, clearly, rather than repeatedly interrupting the prose with accounting.

## Use accurate language that still sounds confident

Write “the evaluated sampler reduces generation time” rather than “the entire framework is efficient.” Write “the diffusion stage does not require paired captions” rather than “the system uses no text supervision.” Write “better recall at this operating point” rather than “complete mode coverage.”

A strong sentence can be narrow. Its force comes from making an important result easy to recognize, not from enlarging its scope beyond the evidence. The [source notes](corpus.md) give paper-specific examples and original before-and-after illustrations.
