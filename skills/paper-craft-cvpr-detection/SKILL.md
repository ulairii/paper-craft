---
name: paper-craft-cvpr-detection
description: Draft and revise CVPR object detection papers from methods and existing results. Distills narrative, method explanation, experiment organization, and clear language from ten accepted CVPR papers on detectors, assignment, feature pyramids, sparse proposals, and convergence.
---

# Write a CVPR object detection paper

Turn the supplied method and results into the requested prose. Find the change in how detection should be understood or performed, then make that change easy to follow. For a full-draft request, write the sections, using short placeholders where facts are missing. Do not replace the draft with a review or an experiment checklist.

## Choose the central argument

Read the actual contribution, not just the dataset name. A detector paper can make its strongest case through an explanation, a representation, a tradeoff, or a training change. Choose the structure that makes the available results meaningful:

| Material suggests | Build the story around | Learn from |
|---|---|---|
| A naive change unexpectedly fails | The failure, its cause, and the design that answers it | [Cascade R-CNN](references/papers/P05.md), [Sparse R-CNN](references/papers/P08.md) |
| Two method families differ less than expected | The operational distinction that better explains their behavior | [ATSS](references/papers/P06.md) |
| An existing representation lacks one property | The missing property and the simplest way to supply it | [R-CNN](references/papers/P01.md), [FPN](references/papers/P04.md) |
| The useful contribution is a resource tradeoff | The operating range and who benefits from it | [YOLO](references/papers/P02.md), [EfficientDet](references/papers/P07.md) |
| Several improvements share a purpose | A small set of reader goals or a common representation | [YOLO9000](references/papers/P03.md), [Dynamic Head](references/papers/P09.md) |
| Training behavior improves before final accuracy does | The optimization difficulty and how the intervention changes it | [DN-DETR](references/papers/P10.md) |

Do not force a module-heavy narrative onto an analytical contribution. ATSS makes its diagnosis before introducing the algorithm because the diagnosis explains why that algorithm is useful.

## Make the method legible

Explain the detector's changed decision before its layers: which regions are represented, how features are combined, which examples become positives, or which targets a query learns. Introduce notation after those objects have meaning.

Give each component a reason. FPN's connections answer the semantic-resolution tension; Cascade R-CNN's stages answer a changing proposal distribution. If a component has no role in the central explanation, describe it briefly as a supporting choice rather than inventing a separate novelty claim.

Use one overview to establish the relevant interface. A box-proposal method should distinguish boxes from proposal features. An assignment method should distinguish training selection from inference. A training method should explain which auxiliary inputs disappear at test time. These details belong in prose because they help readers understand the idea.

## Let experiments complete the introduction

Make each major question promised in the introduction return in the results. Select the most informative comparison, explain its pattern, and state its implication for the idea. Do not narrate every AP column.

- For localization quality, explain behavior at stricter overlaps and connect it to the proposed refinement mechanism.
- For multiscale representation, explain the scale-dependent pattern and the role of each feature path.
- For efficiency, show the useful accuracy–resource tradeoff; distinguish prediction speed from training convergence when writing.
- For a conceptual diagnosis, put the comparison that changes the reader's understanding early, even before the method when appropriate.
- For broad applicability, make the different detector interfaces understandable, then explain what remains common across them.

A failure can advance the story. YOLO's error profile motivates a complementary detector combination; Sparse R-CNN's weak naive replacement explains why learned proposal features matter. Use such results to teach, not to apologize.

## Write plain, concrete English

Prefer “choose positive examples” to “perform adaptive positive-sample determination,” and “combine feature levels” to “exploit hierarchical synergies.” Keep necessary technical terms, but avoid decorative adjectives such as superior, remarkable, and comprehensive when a concrete finding can do their work.

Keep names stable. Do not alternate between proposal, query, anchor, and candidate as stylistic synonyms when they denote different things. Define high-quality as tighter localization if that is what the experiment measures. Explain what is sparse, adaptive, or unified instead of leaving the title adjective to carry the claim.

Give each paragraph one question or conclusion. Use a transition that explains why the next step follows. A strong result needs a clear statement, not a string of “may potentially suggest” qualifiers; an unexplored extension belongs in a future-work sentence, not the results.

## Load only useful supporting material

- [Writing and experiment playbook](references/playbook.md): opening moves, section order, detail selection, and result paragraphs.
- [Worked draft example](references/worked-example.md): a localization story written from supplied results.
- [Ten-paper source collection](references/corpus.md) and [BibTeX](references/references.bib): explicit references and individual reading notes.

Borrow explanatory structure, not source wording. Cite these papers in the user's manuscript when they are scientifically relevant; do not insert them just because their writing informed the draft. Return the requested writing first, with only a brief explanation of major editorial choices when useful.
