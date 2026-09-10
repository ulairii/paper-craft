---
name: paper-craft-cvpr-3d
description: Write and revise CVPR point-cloud and 3D perception papers from existing methods and results. Distills ten accepted papers into guidance on geometric representations, LiDAR detection, point operators, masked pretraining, efficiency, and experiment interpretation.
---

# Write a CVPR 3D perception paper

Write the requested draft from the user's method and results. Find the geometric or representational obstacle that explains the contribution. Use concise placeholders for missing facts and continue through the requested sections. This specialist covers point-cloud perception; use broader writing guidance for reconstruction, rendering, or camera-only estimation unless the relevant contribution is shared.

## Choose the explanatory thread

| Main contribution | Opening question | Sources |
|---|---|---|
| A representation of unordered points | What properties must the operation respect, and what information must it preserve? | [PointNet](references/papers/P01.md) |
| Learned voxel or pillar features | How can local measurements become an efficient scene representation? | [VoxelNet](references/papers/P02.md), [PointPillars](references/papers/P03.md) |
| Proposals or refinement in 3D | Which geometry or annotation property makes the design useful here? | [PointRCNN](references/papers/P04.md) |
| A continuous geometric operator | What familiar operation is being extended, and what makes its direct implementation impractical? | [PointConv](references/papers/P05.md) |
| Combining representations | What prevents the two representations from communicating efficiently? | [PV-RCNN](references/papers/P06.md) |
| Removing expensive computation | What fails when that computation is simply removed? | [3DSSD](references/papers/P07.md) |
| A simpler output representation | Which downstream operations become simpler as a consequence? | [CenterPoint](references/papers/P08.md) |
| Pretraining on point clouds | What input unit and target make the learning objective meaningful? | [Point-BERT](references/papers/P09.md) |
| Scaling a backbone | What capability becomes practical when an expensive operation is simplified? | [Point Transformer V3](references/papers/P10.md) |

A concrete information loss, geometric ambiguity, or computational bottleneck makes the stakes clearer than a generic claim that 3D understanding is difficult.

## Make geometry explain the method

State what the sensor observes and what the model must predict. Surface returns are different from object centers; sparse measurements are different from an empty scene; an unordered input set is different from a sequence constructed from coordinates. Use these distinctions when they explain the design.

Trace information through the model in the reader's order. Name what survives each transformation and what becomes harder to recover. Introduce the equation after explaining the operation it represents. If the mathematical reformulation is the contribution, give it enough main-text space to show why it changes the computation.

Credit inherited encoders and heads plainly. A useful representation interface or a simpler prediction target can carry a strong contribution without claiming an entirely new system.

## Turn results into explanations

Organize the experimental prose around the opening question. For a sampling method, explain which instances survive. For an orientation argument, discuss the heading breakdown. For a scale argument, show what happens as the receptive field grows. Use the available evidence; do not invent the missing diagnostic or stop drafting to prescribe a large new experiment program.

Write the result, its meaning, and its boundary. A diagnostic can support an explanation without establishing a universal cause. PointPillars explains its operating point despite a more accurate competing encoder. CenterPoint discusses limited refinement gains on sparse data. Point Transformer V3 shows that larger patches eventually stop helping.

When several components or stages contribute, distinguish their roles. Stronger tracking can come from detection, association, or both. A pretrained model can improve through the learning objective and through added data. Use the comparisons the user actually has to describe the appropriate scope.

## Keep the details that carry the argument

Retain coordinate frames, prediction targets, representation transitions, and input modalities when the reader needs them to understand the method. A short runtime breakdown belongs in an efficiency argument because it identifies the source of the gain. An algebraic memory reduction belongs in an operator paper because it makes the operation feasible.

Move routine settings and broad parameter lists into compact tables or an appendix. Do not fill the main text with repeated reproducibility checks. Mention a protocol distinction at the comparison where it changes interpretation, rather than attaching the same warning to every result.

## Use plain, precise English

Prefer “preserve foreground points,” “aggregate voxel features,” “predict object centers,” and “increase the attention patch size.” Replace “holistic geometric intelligence,” “unprecedented synergy,” and “comprehensive spatial enrichment” with the operation or finding.

Keep point, voxel, pillar, patch, proposal, and object distinct. Name the axis of scaling. Do not use “invariant” when the evidence shows improved robustness, “zero-shot” for fine-tuned transfer, or “no geometric assumptions” for a model with geometric patch construction.

Use a short motivating example when it makes a mechanism understandable. Avoid turning every observation into a universal statement. A precise limitation can strengthen the central contribution by making its useful setting clear.

## Read the supporting material selectively

- [Playbook](references/playbook.md): narrative structures, section order, and result interpretation.
- [Worked example](references/worked-example.md): drafting a sampling argument from supplied results.
- [Ten source papers](references/corpus.md) and [BibTeX](references/references.bib): citations and individual craft notes.

Return usable prose first. For a full-draft request, write the draft rather than returning only an outline. Borrow explanatory structures, not source wording, and cite source papers in the manuscript when scientifically relevant.
