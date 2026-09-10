---
name: paper-craft-cvpr-segmentation
description: Write and revise CVPR semantic, instance, and panoptic segmentation papers from existing methods and results. Uses ten accepted papers to explain context, boundaries, feature refinement, attention, and task unification through clear narratives and experiment interpretation.
---

# Write a CVPR segmentation paper

Write the requested draft or revision from the user's material. Identify what changes for the reader: a better representation of pixels, a way to recover boundaries, a use of scene context, or a more useful relationship between segmentation tasks. Keep missing facts as concise placeholders and continue through the requested sections.

## Choose the story before naming modules

| Central contribution | Productive opening | Sources |
|---|---|---|
| Dense prediction from an existing representation | Explain how a classifier becomes a spatial predictor, then what information is still missing | [FCN](references/papers/P01.md) |
| Context resolves ambiguous labels | Start from a recognizable confusion and identify what surrounding information would resolve it | [PSPNet](references/papers/P02.md), [EncNet](references/papers/P04.md) |
| Refinement recovers fine structure | Explain which detail is lost and where useful information survives | [RefineNet](references/papers/P03.md) |
| Attention changes feature relationships | State which locations or channels exchange information and why | [DANet](references/papers/P05.md) |
| Boundary quality improves efficiently | Explain why smooth interiors and boundaries need different computation | [PointRend](references/papers/P07.md) |
| Tasks share computation or a representation | Define the particular kind of sharing and the obstacle to it | [Panoptic FPN](references/papers/P06.md), [Mask DINO](references/papers/P09.md) |
| A common architecture or trained model serves several tasks | State exactly what is common and what still changes across tasks | [Mask2Former](references/papers/P08.md), [OneFormer](references/papers/P10.md) |

Do not call every context module a new paradigm. A concrete confusion, a missing feature, or an unnecessary repeated computation usually makes the importance easier to see.

## Explain the representation in the reader's order

Tell the reader what the output groups: pixels of the same category, each object instance, or both instances and background regions. Then explain the representation that makes that grouping possible. Introduce the feature path, query, mask, or loss only when its role is clear.

For context methods, distinguish the available field of view from the operation that uses it. For refinement methods, distinguish interpolating a coarse prediction from obtaining additional spatial information. For query methods, distinguish the query representation from the pixel features it acts on.

When claiming unification, name the unit: a shared backbone, one architecture with separate training, a jointly trained model, or shared training data. These are different scientific contributions. Keep that choice consistent in the title, abstract, diagrams, and results.

## Let the result explain the idea

Select the result pattern that answers the opening problem. A boundary method needs an explanation of fine structure; a context method needs an explanation of category confusion or consistency; a train-once method needs an explanation of behavior across tasks. Write what changes and why the change matters, not a recital of all metrics.

Use a diagnostic or qualitative example when it teaches the operation. PSPNet returns to its motivating errors. PointRend shows successive refinement. OneFormer changes the task input and explains the resulting grouping. A secondary metric can decrease for a good reason when the model is explicitly asked to perform another task.

Keep comparison details where they change interpretation. For example, mention the mask annotation source when boundary quality depends on it, or separate independently trained models from one jointly trained model in a task-unification comparison. Do not turn this into a repeated verification workflow.

## Write natural academic English

Use “combine local and global features,” “recover boundaries,” and “condition the queries on the task.” Avoid “harvest momentous priors,” “facilitate comprehensive semantic enrichment,” and other wording that makes a simple operation harder to understand.

Keep semantic, instance, and panoptic terminology precise. Do not use pixel, region, mask, and instance as interchangeable synonyms. Say what is adaptive or universal. Introduce acronyms only when they save repeated explanation.

Give each paragraph one explanatory job. Prefer a concrete design rationale to repeated novelty adjectives. Confidently state a clear result, but do not turn a motivating example into a universal rule: scene context may help identify a boat without making every object on water a boat.

## Use references selectively

- [Writing playbook](references/playbook.md): story selection, section order, interpreting results, and deciding which details belong.
- [Worked example](references/worked-example.md): drafting a boundary-refinement argument from supplied material.
- [Ten accepted papers](references/corpus.md) and [BibTeX](references/references.bib): source links and individual craft notes.

Return usable prose first. A full-draft request needs a full draft, not just an outline or proposed experiments. Borrow the explanatory move, not the original wording; add scientific citations to the manuscript only when relevant to its subject.
