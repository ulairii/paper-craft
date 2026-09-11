---
name: paper-craft-usenix-software
description: Draft and revise USENIX Security software-security papers from methods and existing results. Distills ten accepted papers on fuzzing, symbolic execution, firmware emulation, input structure, sanitizer guidance, and driver generation into contribution framing, method exposition, and experimental interpretation.
---

# Write a USENIX Security software-security paper

Write the manuscript the author requests. For a full draft, produce connected section prose with specific placeholders for missing facts. This specialist focuses on vulnerability discovery and program analysis; use the supplied results to decide which contribution the paper can develop.

## Find the decision that changes the outcome

| Central change | Story to develop | Source examples |
|---|---|---|
| Analysis or execution engine | Which measured cost prevents useful exploration, and why does this design reduce it? | [QSYM](references/papers/P01.md), [SymCC](references/papers/P06.md) |
| Search allocation | Which inputs, mutations, or targets deserve effort? | [MOPT](references/papers/P02.md), [FuzzGuard](references/papers/P07.md), [ParmeSan](references/papers/P08.md) |
| Deployment environment | Which compatibility and throughput requirements must be met together? | [FIRM-AFL](references/papers/P03.md) |
| Cooperation | What intermediate information lets one component extend another's progress? | [EnFuzz](references/papers/P04.md) |
| Inferred structure | What useful knowledge can be recovered with less manual specification? | [GRIMOIRE](references/papers/P05.md), [GREYONE](references/papers/P09.md) |
| Driver generation | Which API ordering and state dependencies normally require an expert? | [FuzzGen](references/papers/P10.md) |

A specialized engine, a useful combination, or lower manual effort can carry the contribution. Identify that useful difference before inventing a new framework name. A learned filter for ordinary programs belongs here when program exploration carries the contribution; attacks on or defenses of ML models call for ML-security guidance.

## Build the opening around a concrete obstacle

Start with what prevents the current workflow from reaching useful behavior: repeated interpretation, invalid library state, an expensive emulation boundary, or mutations that miss the relevant input bytes. Explain the consequence, give the observation behind the method, and introduce the changed operation. Use one short example when it makes that operation obvious.

Map the important challenges to the method's decisions. FuzzGuard's cold start, changing distribution, and model cost explain why a predictor needs surrounding mechanisms. FIRM-AFL's environment requirements explain why a faster execution mode alone is insufficient. Avoid a generic opening about the growing importance of cybersecurity.

Contribution bullets should name a capability, design principle, or finding. “We implement a system and evaluate it extensively” consumes space without explaining the insight.

## Explain the method at the right level

Show the data and control flow needed to understand the change. For hybrid analysis, distinguish execution, constraint reasoning, candidate generation, and concrete replay. For a library driver, show how initialization creates state that later calls reuse. For guidance, define the signal, the decision it changes, and when that signal is updated.

Credit inherited engines, optimizers, emulators, and instrumentation. A shared backend can sharpen the contribution, as in SymCC. Explain a heuristic by what it approximates and why that approximation is useful in this workflow. Introduce equations only after their quantities have an operational meaning.

Use short code or trace examples that preserve the relevant dependency. Omit casts, complete field initialization, and routine bookkeeping when they obscure the idea. Keep details that determine applicability—source access, bootability, library semantics, supported bug classes—beside the method they qualify.

## Let the experiments explain the contribution

Lead with the evidence that answers the paper's central question. Then explain why the method helps through the available component, workload, or resource comparisons. Reusing the same backend tests execution design; sharing versus not sharing tests cooperation; changing the guidance sanitizer with detection fixed tests the search signal.

Use paragraph structure: finding → decisive comparison → mechanism or plausible explanation → useful scope. Describe important exceptions. A manual driver that finds more bugs in one component can reveal a breadth–depth tradeoff; an execution speedup that shrinks on solver-heavy programs explains where the system spends time.

Keep practical discoveries and controlled comparisons distinct in their narrative roles. A new vulnerability case makes the benefit concrete. Time-to-exposure, coverage, and component experiments explain comparative behavior. Use the author's existing evidence; do not turn a drafting request into an open-ended experimental campaign.

## Keep the details that change the reader's interpretation

State what a reported number counts: crashes, deduplicated faults, confirmed vulnerabilities, assigned CVEs, or a union across runs and configurations. Explain the input access and resource budget where they define the comparison. Separate automatic targets from manually supplied bug locations, and execution time from preprocessing or generation time.

Keep one informative vulnerability case in the main text: required state, missed condition, changed exploration, and observed fault or impact. Put long bug inventories, complete settings, and secondary per-program tables in the appendix. A detail belongs in the main text when removing it changes the apparent contribution.

## Use plain, confident academic English

Prefer “compile,” “infer,” “prioritize,” “share,” “replay,” “generate,” and “reach.” Define established technical terms when needed. Avoid decorative language such as “synergistic vulnerability intelligence,” “unprecedented prowess,” and “seamlessly unlocks.” Give every paragraph one job.

Sell the concrete consequence: less execution work, broader API exploration, reduced specification effort, or faster exposure on the evaluated targets. Use “suggests” or “is consistent with” for explanations not isolated by an experiment. Describe what works directly, without converting finite results into complete analysis, universal dominance, or guaranteed exploitability.

## Resources

- [Writing playbook](references/playbook.md): story shapes, explanatory comparisons, detail placement, and sentence choices.
- [Worked example](references/worked-example.md): manuscript prose from fictional supplied results.
- [Ten source papers](references/corpus.md) and [BibTeX](references/references.bib).

Borrow argumentative moves, not sentences. Cite a source in the manuscript when it supplies relevant prior work or technical context, rather than citing every writing inspiration.
