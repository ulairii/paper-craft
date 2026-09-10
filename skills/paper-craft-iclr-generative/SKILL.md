---
name: paper-craft-iclr-generative
description: Draft and revise ICLR generative-model papers from methods and existing experiments. Distills ten accepted papers on variational models, flows, GANs, diffusion, sampling, text-to-image systems, and reward fine-tuning into clear contribution framing, method explanations, and experimental narratives.
---

# Write an ICLR generative-model paper

Produce the manuscript requested by the author. For a full draft, write connected section prose, using concise placeholders for missing facts. Find the contribution in the supplied method and results, then explain why it matters. Use the existing evidence to write; do not replace drafting with a recurring review or experiment checklist.

## Choose the contribution before choosing the structure

| Contribution | Organizing question | Examples |
|---|---|---|
| Tractable learning or inference | Which inaccessible quantity becomes computable, and why? | [AEVB](references/papers/P01.md), [Flow Matching](references/papers/P07.md) |
| Useful model properties | Which combination of capabilities becomes available? | [Real NVP](references/papers/P02.md) |
| Training behavior | Which mechanism explains the observed improvement or failure? | [Spectral Normalization](references/papers/P03.md), [BigGAN](references/papers/P04.md) |
| Sampling efficiency | What changes in the sampling process, and at which budgets does it help? | [DDIM](references/papers/P05.md), [Rectified Flow](references/papers/P08.md) |
| Unifying formulation | Which new choices or capabilities follow from the connection? | [Score SDE](references/papers/P06.md) |
| System design or adaptation | Which concrete output problem does each change address? | [SDXL](references/papers/P09.md), [DDPO](references/papers/P10.md) |

A useful combination of properties, a clearer learning formulation, or an informative explanation can be the contribution even when it does not win every metric. Sell the scientific change and its consequence rather than inventing a universal superiority claim.

## Explain the obstacle, then the construction

Introduce the distributions, inputs, conditions, and intended output before writing the loss. Explain what is difficult: posterior inference, a Jacobian, adversarial dynamics, repeated sampling evaluations, or a mismatch between training and use.

Give each mathematical step a purpose. For a tractable surrogate, describe the ideal target, why it is inaccessible, the computable replacement, and the relationship that makes the replacement useful. State assumptions where they explain that relationship. Put extended derivations in supporting material.

Separate the learned model, training objective, and sampling procedure. For multi-stage methods, say what each stage changes and what it takes as input. Credit inherited components before identifying the modification. A familiar component can be valuable because of how it addresses the paper's problem; it does not need a new acronym.

## Turn the experiments into a progression

Start with the result that answers the central question. Follow it with a comparison that explains the source of the gain, then a consequence or boundary that tells readers when the method is useful. Use one main finding per paragraph: finding, comparison, interpretation. Avoid narrating every table entry.

Use quality–cost curves for a sampling contribution, behavior across settings for stability, and targeted output or user-preference evidence for a system improvement. Distinguish likelihood, perceptual fidelity, coverage, reconstruction, and reward. If they disagree, explain the difference in what they measure.

A mathematical property should lead to an experimental prediction. Straighter trajectories suggest better coarse integration; a freer spectrum suggests a useful capacity difference. Present observed agreement as evidence for the explanation, not as proof that no other mechanism matters.

## Place details where they change the meaning

Keep conditioning and label access, data regime, important model changes, and sampling budget near the corresponding results. Define the resource being saved: network evaluations, latency, training examples, gradient updates, or reward queries. A headline result assembled from different models or operating points is not one configuration.

Move full schedules, architecture inventories, bucket lists, secondary sweeps, and repeated sample galleries to setup or appendices. Retain a detail in the main story when it explains the construction or changes how a result is interpreted. Describe it once at the point where it becomes useful.

## Write plainly and sell precisely

Prefer “estimate,” “condition,” “sample,” “reuse,” “fit,” “reduce,” and “trade off.” Keep established technical terms when needed, but explain them with familiar words. Avoid decorative phrases such as “unparalleled generative prowess,” “holistic synergy,” and “revolutionary paradigm.” Replace “highly efficient” with the measured saving and its quality consequence.

Use “simulation-free training” when sampling still uses a numerical solver. Distinguish exact model formulas from finite numerical estimates, conditional OT from globally optimal transport, and higher reward from user benefit. These distinctions should sharpen the central claim rather than bury every sentence under qualifications.

Write limitations as informative boundaries: what changes outside the useful regime, what the current comparison cannot distinguish, and which extension remains untested. Preserve the main contribution confidently within those boundaries.

## Resources

- [Writing playbook](references/playbook.md): narrative structures and paragraph patterns.
- [Worked example](references/worked-example.md): manuscript prose from fictional sampling results.
- [Ten source papers](references/corpus.md) and [BibTeX](references/references.bib).

Borrow argumentative moves, not sentences. Cite source papers in a manuscript when scientifically relevant; this collection is not a mandatory related-work list. Use the representation specialist when transferable features carry the contribution, and the reasoning specialist when the contribution is LLM inference rather than generative image modeling.
