---
name: paper-craft-icml-representation
description: Write and revise ICML representation-learning papers from methods and existing results. Distills ten accepted papers on contrastive learning, non-contrastive learning, language-image transfer, identifiability, robustness, and dynamics into narrative, experiment explanation, and plain academic prose.
---

# Write an ICML representation-learning paper

Turn the author's material into the requested manuscript prose. For a full draft, write the sections with concise placeholders for missing facts. Find the learning insight, useful interface, or scientific explanation that makes the work worth reading.

## Choose the contribution's argument

| Contribution | Organizing question | Sources |
|---|---|---|
| Learning method or recipe | What should the representation preserve, and what should it ignore? | [SimCLR](references/papers/P01.md), [Barlow Twins](references/papers/P04.md) |
| Data efficiency | How much labeled data is needed for a useful result? | [CPCv2](references/papers/P02.md) |
| Explanatory objective | Which measurable properties explain useful features? | [Alignment and Uniformity](references/papers/P03.md) |
| Derived algorithm | What does the analysis suggest changing in training? | [DirectPred](references/papers/P05.md) |
| Transfer interface or scale | What new task becomes possible, and what enables it? | [CLIP](references/papers/P06.md), [ALIGN](references/papers/P07.md) |
| Scientific explanation | Which conditions or mechanisms explain the observed behavior? | [Contrastive Inversion](references/papers/P08.md), [Data Determines](references/papers/P09.md), [Stepwise Learning](references/papers/P10.md) |

A familiar loss combined with a revealing experiment can carry a contribution. A theory paper can contribute an explanatory picture without introducing a winning algorithm. Do not force either into a “novel module achieves state of the art” template.

This corpus centers on self-supervised and language–image representations. Generating samples or maximizing reward calls for a different primary specialist when that carries the contribution.

## Make the representation and its use concrete

Explain what provides the supervision: augmented views, neighboring patches, paired captions, or a specified latent pairing process. Say what agreement means and what prevents an uninformative representation. Follow one example through the encoder, projection or prediction head, and downstream use.

Explain loss terms by their jobs before presenting the whole expression. Distinguish feature-coordinate correlation from sample similarity. Separate the representation used downstream from an embedding optimized only during pretraining.

For theory, introduce the observable puzzle first. State the simplified setting, give the idea of the argument, and extract a prediction. Keep assumptions close to the result. Exact solutions in a linear model and qualitative agreement in a deep network are complementary contributions with different meanings.

## Make experiments answer the central question

Lead with the result that matters for the claimed use: transfer quality, label savings, task specification, or an explained phenomenon. Then use the author's existing comparisons to explain it. Do not turn drafting into a demand for every possible experiment.

For a method, compare the design choices that define its mechanism. For a scale claim, explain how model capacity interacts with data size and quality. For an empirical explanation, organize around plausible competing causes. For theory, move from the exact setting through controlled changes to more realistic observations.

A result paragraph should state the finding, identify the revealing comparison, and explain its implication. Loss reduction, instance discrimination accuracy, geometric diagnostics, and downstream accuracy can disagree; that disagreement may be the most interesting result.

## Place scientific conditions where readers need them

Keep supervision, pairing, trainable downstream components, and the measured representation in the main explanation. Label zero-shot, frozen-feature, and fine-tuned results clearly. State which resource a saving concerns: labels, images, training operations, or inference cost.

Move long schedules, prompt inventories, and derivations to setup or supporting material. Include a detail in the central story when changing it would change the meaning of the claim. Describe it once in the appropriate place.

## Sell the insight in ordinary English

Prefer “align paired views,” “reduce redundant coordinates,” “retain information for transfer,” “specify a classifier with text,” and “predict when directions emerge.” Avoid ornamental phrases such as “holistic representational synergy” or “universal semantic intelligence.” Use standard technical terms when they carry exact meaning.

Replace vague adjectives with consequences. “Simple” may describe an objective without implying faster training. “Zero-shot” names an adaptation protocol without implying unseen concepts. “Decorrelation” does not automatically establish independence. “Identifiable” needs its permitted ambiguity.

Write the supported contribution confidently. Use mixed results to sharpen its domain of usefulness. A clean explanation of why a method helps in one meaningful regime sells the work better than a sweeping claim that its own tables contradict.

## Resources

- [Writing playbook](references/playbook.md): story selection, experiment logic, and prose moves.
- [Worked example](references/worked-example.md): manuscript passages for an explanatory learning study.
- [Ten source papers](references/corpus.md) and [BibTeX](references/references.bib).

Borrow argumentative moves, not source sentences. Cite corpus papers in a manuscript when scientifically relevant; the reading list is not a mandatory related-work section.
