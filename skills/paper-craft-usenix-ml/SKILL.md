---
name: paper-craft-usenix-ml
description: Draft and revise USENIX Security machine learning security papers from methods and existing results. Distills ten accepted papers on adversarial inputs, poisoning, inference, watermarking, defenses, and forensics into clear narratives, contribution framing, experiment explanations, and manuscript prose.
---

# Write a USENIX Security machine learning security paper

Produce the requested manuscript prose from the supplied methods and results. For a full draft, write connected sections and mark specific missing facts with placeholders. Choose the argumentative structure that fits the contribution; an attack, a defense, and a measurement study need different stories.

## Find the change in understanding

| Contribution | Organizing question | Source examples |
|---|---|---|
| New attack surface | What ordinary operation gives the attacker influence that earlier work did not consider? | [CommanderSong](references/papers/P01.md), [Local Model Poisoning](references/papers/P05.md), [PoisonedEncoder](references/papers/P09.md) |
| Hidden information | What does the model reveal beyond its intended prediction? | [Stolen Memories](references/papers/P04.md) |
| Constructive reuse | How does an apparent weakness enable a useful protection? | [AttriGuard](references/papers/P02.md), [Watermarking by Backdooring](references/papers/P03.md) |
| Defense | Which failure mechanism does each design choice remove, and what useful behavior remains? | [PatchGuard](references/papers/P06.md), [FLAME](references/papers/P07.md) |
| Incident response | What can be learned after a known attack that prevention methods do not answer? | [Poison Forensics](references/papers/P08.md) |
| Comparative measurement | What relationship appears when several risks are studied under common conditions? | [ML-Doctor](references/papers/P10.md) |

State this change in one plain sentence before introducing the system name. A new control surface, a useful reduction, a mechanism explaining leakage, or a better security–utility tradeoff can carry the contribution. The number of modules is rarely the reason the result matters.

## Give the opening a concrete causal chain

Start with a recognizable action and consequence: a provider collects unlabeled images, two crops become a positive pair, and an association survives into a downstream classifier. Or begin with a surprising observation: a correctly classified example can still leak membership through the features used to classify it.

Explain the previous assumption, the observation it misses, and the insight that addresses it. Credit prior methods for what they accomplish. Replace “existing methods are inadequate” with the specific missing capability. Introduce only the background needed to follow this chain; do not open with a generic history of deep learning.

Frame contributions around capabilities or knowledge. “We show that crop-based pretraining can associate a chosen image with a reference class” conveys more than “We propose a novel optimization framework.” Use “first” only for a well-supported, precisely scoped literature claim, never as a substitute for explaining the difference.

## Make the method follow from the insight

Use a small running example before notation. Explain the input, transformation, and output, then use equations where they clarify an objective, condition, or guarantee. PoisonedEncoder's construction is compelling because it exploits the training objective; its simplicity is an advantage. Stolen Memories uses an idealized model to explain the signal before approximating it in neural networks.

For a defense, connect failure causes to interventions. PatchGuard bounds the number of corrupted features and prevents those features from dominating aggregation. FLAME's filtering and clipping reduce the amount of noise needed later. Explain that interaction rather than describing independent modules in implementation order.

For forensics or measurement, define what the output means. Recovering associated training records differs from identifying a person. Behavioral agreement with a target model differs from recovering its exact parameters. Keep these distinctions close to the method so the story stays easy to follow.

## Turn experiments into explanatory paragraphs

Order the evaluation around questions: Does the capability work? Which observation or design choice explains it? Under what conditions does it remain useful? What does it cost? Select the questions supported by the user's existing results and write the answers; do not replace a requested draft with an experiment checklist.

Write finding → decisive comparison → explanation → consequence. Pair attack success with ordinary task performance, or privacy inference with the utility of the released data. For a multi-stage defense, an imperfect intermediate detector can still support a successful final outcome; explain what the next stage contributes.

Use ablations to distinguish plausible explanations. A naive combination can reveal why coordination matters. A removed component can expose the useful behavior that a defense sacrifices. An unexpected weak result can motivate a focused analysis: destination-class accuracy, ineffective poison samples, or a model-dependent feature choice. Say “suggests” when the experiment supports an explanation without isolating it.

## Keep meaning-changing details in the main text

State attacker control, knowledge, target, and budget compactly. Explain whether an input changes at inference time, whether a budget is per target or shared, and whether the defender needs clean data or access to individual updates. A threat model should help the reader picture the operation.

Define the result's denominator and outcome: recognized words, executed commands, selected members, corrupted targets, certified images, recovered records, or agreeing predictions. Put a guarantee's assumptions beside the guarantee. Distinguish added defense cost from the cost of changing the underlying architecture. These details explain the contribution; they need not become a repeated verification ritual.

Move full parameter grids, routine software configuration, secondary derivations, and repeated metric variants to the appendix. Keep an appendix result in the main argument when it materially explains the headline—for example, the extra training responsible for part of a defense's gain. Describe limits as the conditions of usefulness rather than a generic list of possible failures.

## Use ordinary English to make the contribution memorable

Prefer “learn,” “reveal,” “combine,” “remove,” “retain,” “recover,” and “compare.” Avoid “unprecedented paradigm,” “sophisticated orchestration,” “seamless protection,” and “holistic superiority.” Use established technical vocabulary where it adds precision, and give each symbol one job. A named system does not need repeated metaphors.

Sell the insight through its consequence: what can now be inferred, prevented, explained, or investigated? Do not inflate an empirical result into an unrestricted guarantee or treat a borrowed technique as newly invented. Accepted papers provide examples of effective argument construction; their acceptance does not prove that a particular phrase or rhetorical choice caused it.

## Resources

- [Writing playbook](references/playbook.md): paragraph structures, contribution stories, and detail choices.
- [Worked example](references/worked-example.md): manuscript prose from fictional supplied experiments.
- [Ten source papers](references/corpus.md) and [BibTeX](references/references.bib).

Borrow argumentative moves, not sentences. Cite sources in a manuscript when they supply relevant prior work, methods, or evidence; inspiration about writing alone does not require a technical citation.
