---
name: paper-craft-sp-software
description: Draft and revise IEEE S&P software-security papers from methods and existing results. Distills ten accepted papers on fuzzing, input semantics, program transformation, learned feedback, hybrid analysis, state exploration, and USB gadget testing into narrative, method exposition, and experimental interpretation.
---

# Write an IEEE S&P software-security paper

Produce the manuscript the author requests. A full-draft request calls for connected section prose, with specific placeholders for missing facts. Use the actual method and results to choose the contribution; this specialist focuses on vulnerability discovery and program analysis.

## Find the observation that makes the method necessary

| What changes | Central writing question | Examples |
|---|---|---|
| Input representation | What task-relevant information does byte mutation discard? | [Skyfire](references/papers/P01.md), [ProFuzzer](references/papers/P06.md) |
| Search procedure | What prevents promising inputs from reaching the next condition? | [Angora](references/papers/P02.md) |
| Feedback | Which distinct behaviors look identical to the search? | [CollAFL](references/papers/P03.md), [IJON](references/papers/P07.md) |
| Object of mutation | What new behavior becomes available, and how does it relate to the original program? | [T-Fuzz](references/papers/P04.md) |
| Learned surrogate | What useful decision becomes possible through this representation? | [NEUZZ](references/papers/P05.md) |
| Information passed between stages | What previous work is lost, and how can both stages reuse it? | [Pangolin](references/papers/P08.md) |
| Search objective | Why is the usual proxy insufficient for the desired outcome? | [SAVIOR](references/papers/P09.md) |
| Target interface | Why does the new target require more than adapting an existing tool? | [FuzzUSB](references/papers/P10.md) |

Select one primary story. A neural network used for program exploration belongs here; attacks on or defenses of learning systems call for ML-security guidance. Do not force an exploit mitigation or cryptographic protocol into this fuzzing corpus.

## Build the opening from a concrete obstacle

State the operation the current workflow struggles with, its consequence, and the observation that changes the approach. Show a small input, branch example, or interaction sequence when that makes the observation understandable. Return to it in the method and results.

Make each important challenge explain a design decision. FuzzUSB's channels and states explain two different capabilities. T-Fuzz's transformation creates a need for reconstruction. Pangolin's retained region explains both sampling and subsequent solving. This is stronger than listing modules and then asserting that they work together.

Frame novelty as the useful difference from the closest approach. Name the information recovered, decision changed, or behavior exposed. Credit inherited engines and established techniques. A new name, more implementation code, and an extensive evaluation do not by themselves explain an intellectual contribution.

## Explain the method through the decision it changes

Introduce the relevant object before its notation: a field, predicate, coverage entry, progress signal, or feasible region. Explain how the method obtains it, uses it, and updates it. Use established technical terms where precise; do not rename ordinary operations to make them sound novel.

Preserve the distinction between an approximation and the program behavior it represents. Explain why the approximation is useful. Keep only the assumptions that define the capability beside the method: required source access, valid seeds, analyst participation, supported fault conditions, or control over input channels.

Shorten illustrative code to the dependency that matters. A field flowing into allocation or two channels accessing one object can explain the contribution more clearly than a complete routine. Move bookkeeping, full APIs, and repetitive pseudocode out of the main narrative unless they supply the insight.

## Give each experimental paragraph an explanatory job

Lead with the principal result, identify the decisive comparison, and explain what it says about the method. Follow with the most informative component or workload differences. Use the supplied evidence; missing experiments should become precise limitations or placeholders rather than an open-ended prerequisite to writing.

Choose comparisons that match the story. Feedback-only versus feedback-plus-policy distinguishes observation from action. Equal input pools isolate mutation decisions. Sampling and solving experiments explain different uses of a shared abstraction. Paired coverage and fault curves can show that a better security outcome does not require winning every coverage metric.

Explain important exceptions through the method. Probing can delay easy targets; cached summaries can pay off after warm-up; state feedback can help most where sequences matter. Treat unisolated explanations as plausible interpretations. Do not make every paragraph repeat the table or end with a generic claim of effectiveness.

## Make the practical value concrete

Keep one informative fault case in the main text: required input or state, why previous exploration misses it, what the method changes, and the observed consequence. The case should explain the method rather than merely supply another vulnerability identifier.

Use the actual unit of the result: new edges, retained seeds, crash classes, triggered checks, impactful faults, confirmed reports, or CVEs. Include baseline adaptations and material resource or access differences where they change interpretation. Place complete inventories and secondary settings in supporting material.

## Write plain, confident English

Prefer “infer,” “retain,” “sample,” “prioritize,” “transform,” “reach,” and “trigger.” Avoid decorative phrases such as “holistic semantic intelligence,” “unprecedented prowess,” and “seamlessly unlocks.” Give each paragraph one point and connect sentences through the same concrete objects.

Sell the insight with an understandable consequence. Replace “comprehensive, efficient, and robust framework” with what becomes possible and under which conditions. Do not copy inflated language merely because it appears in an accepted paper. Borrow argument structure, not sentences or implied guarantees.

## Resources

- [Writing playbook](references/playbook.md): narrative choices, experiment paragraphs, and detail placement.
- [Worked draft](references/worked-example.md): full manuscript prose from fictional supplied results.
- [Ten source papers](references/corpus.md), [BibTeX](references/references.bib), and [individual reading notes](references/papers/P01.md).

Cite relevant prior work in the manuscript. Writing inspiration alone does not require citing every source paper in the author's draft.
