---
name: paper-craft-neurips-generative
description: Draft and revise NeurIPS generative-model papers from methods and existing experiments. Distills ten accepted papers on GANs, flows, VAEs, diffusion training, guidance, and fast sampling into contribution framing, clear explanations, and experimental narratives.
---

# Write a NeurIPS generative-model paper

Write the manuscript requested by the author. A full-draft request calls for connected section prose, with specific placeholders where facts are missing. Choose the scientific story that the supplied experiments can tell most clearly.

## Choose the contribution before choosing the opening

| Contribution | Central question | Examples |
|---|---|---|
| A learning principle | What new way of learning a distribution becomes possible? | [GANs](references/papers/P01.md) |
| A training repair or recipe | Which obstacle prevents a promising model from working well? | [Improved GANs](references/papers/P02.md), [WGAN-GP](references/papers/P03.md) |
| An architectural building block | Which restriction does the changed operation remove? | [Glow](references/papers/P04.md), [Spline flows](references/papers/P05.md), [NVAE](references/papers/P07.md) |
| A training connection | How does a different objective or parameterization change what the model learns? | [DDPM](references/papers/P06.md) |
| Controllable synthesis | What useful fidelity–diversity balance becomes available? | [Classifier guidance](references/papers/P08.md) |
| A clearer design space | Which choices can be understood and improved separately? | [EDM](references/papers/P09.md) |
| Faster sampling | Which computation is unnecessary or can be approximated better? | [DPM-Solver](references/papers/P10.md) |

Use the strongest supported contribution, even when it is a simple operation, a better recipe, or an explanation of a tradeoff. Do not manufacture a new probabilistic family to make an architecture paper sound important.

## Make the problem concrete

Open with the specific obstacle and its consequence: clipping restricts the critic, scalar affine maps limit a flow, or a general solver approximates a term with a known solution. Explain the key observation, then state what the method changes and what the experiments establish.

Give the reader one reason to care before giving several equations. Credit inherited objectives, architectures, and numerical methods. Present the innovation as the useful change within that context. A contribution bullet should name a capability, mechanism, or insight, rather than announce that the paper contains a method and experiments.

## Explain the method in the order that reveals the idea

Describe the modeled distribution, the learning signal, and the generation procedure. For adversarial methods, explain the roles of generator and critic. For flows, align transformation, inverse, and density computation. For a VAE, explain latent dependencies and posterior inference. For diffusion, distinguish the trained prediction from the sampler that uses it.

Show the equation that makes the change precise. Explain which part is inherited, which part changes, and why the change addresses the opening obstacle. Keep extended algebra in the appendix once the main text has explained its result. Do not call an exact reformulation an exact numerical sampler.

## Give the experiments a narrative

Lead with the result that establishes the central contribution. Follow with the comparison that explains it, then the evidence that shows where it is useful. A sampler paper can hold the pretrained network fixed; a training paper can hold the sampler fixed. A recipe paper should explain the different jobs of its components.

Interpret quality, likelihood, coverage, and cost as distinct outcomes. A lower FID, better likelihood, or sharper selected image answers a different question. When metrics disagree, explain what that reveals about the model. DDPM's rate-distortion account and guidance's fidelity–diversity curves are examples of making disagreement informative.

Use a quality–cost curve for a sampling contribution and paired fidelity–coverage measurements for a guidance contribution when those results are available. Explain interactions and diminishing returns. Do not turn the result section into a list of rows that outperform a baseline.

## Place details where they explain a claim

Keep conditioning information, bit depth, sample selection, temperature, guidance scale, and evaluation reference close to results they materially change. Distinguish training cost from sampling cost. For solvers, distinguish steps from network evaluations; for cascades, explain the stages being counted.

Put full model inventories, secondary sweeps, routine optimization settings, and extra galleries in supporting material. Preserve a main-text detail when it explains the method or the meaning of an experiment. Draft from the available evidence; a writing request should not become an indefinite experiment-planning exercise.

## Write with concrete language

Prefer “generate,” “denoise,” “mix channels,” “estimate,” “condition,” and “reduce evaluations.” Use established technical terms and define them once. Avoid decorative phrases such as “unprecedented generative prowess,” “holistic synthesis synergy,” or unusual synonyms for familiar operations.

Sell the useful consequence confidently: a stable training recipe, a reusable invertible transformation, or comparable quality with fewer evaluations. State the tested scope in the same sentence. Distinguish an observed improvement from the proposed explanation for it. A clear, bounded result is more memorable than an unsupported claim of universal superiority.

## Resources

- [Writing playbook](references/playbook.md): narrative patterns, result interpretation, and detail placement.
- [Worked example](references/worked-example.md): a draft built from fictional supplied experiments.
- [Ten source papers](references/corpus.md) and [BibTeX](references/references.bib).

Borrow argumentative moves, not sentences. Cite a corpus paper in the manuscript when it is scientifically relevant. Use a representation or reinforcement-learning specialist when feature transfer or policy learning carries the contribution.
