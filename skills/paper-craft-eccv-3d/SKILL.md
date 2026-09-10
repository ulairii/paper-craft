---
name: paper-craft-eccv-3d
description: Write and revise ECCV 3D perception papers from methods and existing experiments. Distills ten accepted papers on point operators, registration, scene and masked pretraining, geometric detection, camera fusion, and sparse attention into story, method, and result-writing guidance.
---

# Write an ECCV 3D perception paper

Turn the supplied method and experiments into the requested manuscript prose. A full-draft request calls for a draft, with short placeholders where essential facts are missing. Find the geometric or learning principle that connects the method to its useful result.

## Choose the argument before the section outline

| Central contribution | Productive opening | Sources |
|---|---|---|
| Point operator | Which property of irregular samples does the operator address? | [SpiderCNN](references/papers/P01.md) |
| Registration | Which information should ignore rotation, and which should retain it? | [PPF-FoldNet](references/papers/P02.md), [PARE-Net](references/papers/P10.md) |
| Representation learning | What makes pretraining transfer, beyond solving its training objective? | [PointContrast](references/papers/P03.md), [Point-MAE](references/papers/P06.md) |
| Geometric detection | What useful constraint is missing from the current representation? | [H3DNet](references/papers/P04.md), [SSN](references/papers/P05.md) |
| Camera-based 3D detection | Where should geometry enter, and how should views or time meet? | [BEVFormer](references/papers/P07.md), [PETR](references/papers/P08.md) |
| Sparse processing | How can occupied surfaces support prediction at empty locations? | [SWFormer](references/papers/P09.md) |

Describe the obstacle in physical or statistical terms before naming modules. A point set is irregular; a surface may hide an object center; a descriptor must survive rotation; low reconstruction error may not imply useful transfer. These are more informative openings than “3D perception has attracted increasing attention.”

This corpus focuses on perception and registration. Rendering, reconstruction, and general depth estimation need other primary guidance when they carry the contribution.

## Give each representation a meaning

Name what one element represents: a sampled neighborhood, a point-pair relation, a primitive, a shape coefficient, a masked patch, a physical BEV location, or an oriented feature vector. Follow that element through one operation before listing the full architecture.

Explain an equation through its role. A rotation-invariant score chooses comparable features; an equivariant vector retains orientation for pose estimation. A point's feature can contain more information than its coordinates. A position embedding can encode camera geometry while remaining on an image grid.

For transferred ideas, explain the adaptation. Point-MAE's important story is how point patches and positional information change masked learning. For simpler interfaces, explain what moves: PETR places geometry in image features. Neither requires claiming that all components are new.

## Make the experiments advance the idea

Lead with the task result. Follow with the comparison that clarifies the contribution, then a regime or tradeoff that explains its value. Work from the author's existing results; do not invent missing experiments or delay drafting until every possible analysis exists.

Useful patterns include the following: hold the backbone fixed to explain pretraining; widen the baseline to distinguish geometry from capacity; fix correspondences to compare pose estimators; remove history to identify temporal benefit; compare transfer performance against reconstruction loss. Choose the pattern that answers the paper's own question.

Explain informative differences rather than narrating every row. Large-object gains can connect spatial support to localization. Low-label gains can explain pretraining's value. Velocity gains can explain history. A reconstruction–transfer disagreement can reveal that a proxy objective is incomplete.

## Keep details that define the scientific result

State the observation and supervision conditions when they matter: normals, aligned views, semantic labels, calibration, past frames, object categories, or extra pretraining. Keep prediction units, coordinate conventions, correspondence meaning, and the use of geometry in the method.

Place routine widths, schedules, and long loss expansions in setup or supporting material. Distinguish auxiliary training targets from inference components. Explain whether a speed result measures an encoder, a complete system, or one representative input. These details belong once in the right place, not in repeated verification paragraphs.

## Write a strong contribution in ordinary English

Prefer “combine geometric constraints,” “transfer across tasks,” “encode camera geometry,” “activate empty locations,” and “estimate a pose hypothesis.” Avoid “holistic spatial synergy,” “universal geometric intelligence,” and decorative synonyms for standard operations.

Use established terms precisely. Invariant and equivariant are different. SWFormer's voxel diffusion is occupancy expansion, not generative diffusion. Removing explicit depth prediction does not remove calibration. A local representation's transfer result does not automatically describe the full pipeline.

State the useful result confidently, then explain a boundary if it changes the interpretation. Mixed results can sharpen the story: a better representation need not reconstruct better; shared tasks need not all improve; a more accurate geometric model can cost more. Sell the insight that the evidence makes clear.

## Resources

- [Writing playbook](references/playbook.md): story structure, explanatory comparisons, and detail placement.
- [Worked example](references/worked-example.md): draft passages for a point-cloud pretraining contribution.
- [Ten source papers](references/corpus.md) and [BibTeX](references/references.bib).

Borrow argumentative moves, not source wording. Cite these papers in the manuscript when scientifically relevant; a writing corpus is not a required related-work list.
