---
name: paper-craft-iccv-3d
description: Write and revise ICCV 3D perception papers from methods and existing results. Distills ten accepted papers on point clouds, registration, real-scan recognition, geometric detection, sparse attention, superpoints, and camera-based BEV detection into narrative and experiment-writing guidance.
---

# Write an ICCV 3D perception paper

Write the requested manuscript prose from the supplied method and results. For a full draft, produce a draft with short placeholders for missing facts. Identify what is observed, what must be predicted, and which mismatch the contribution addresses.

## Choose a story that fits the contribution

| Contribution | Opening question | Sources |
|---|---|---|
| Geometric detection | Where is the evidence relative to the prediction target? | [VoteNet](references/papers/P01.md), [Group-Free](references/papers/P06.md) |
| Registration | Which unknown should be learned, and which geometric step is already solvable? | [Deep Closest Point](references/papers/P02.md) |
| Real-scan benchmark | What does a clean benchmark leave untested? | [ScanObjectNN](references/papers/P03.md) |
| Attention or a simpler backbone | Which property of the representation makes the operator useful? | [Point Transformer](references/papers/P04.md), [3DETR](references/papers/P05.md), [VoTr](references/papers/P08.md) |
| Efficient geometric representation | What computation can be avoided, and what information is retained or lost? | [RangeDet](references/papers/P07.md), [Superpoint Transformer](references/papers/P09.md) |
| Camera-based BEV detection | Which useful functions of dense BEV can sparse queries provide? | [SparseBEV](references/papers/P10.md) |

Start with a recognizable consequence: an empty box center, missing scan surfaces, range-dependent object scale, insufficient spatial support, or redundant point-level computation. Explain the proposed principle before listing modules. A rendering or reconstruction contribution needs other dedicated guidance; this corpus does not cover every 3D task.

## Explain the representation before the architecture

Name the computational element and what it represents: a surface seed, a vote, a soft correspondence, an object query, an occupied voxel, a range-image cell, or a superpoint. Follow one prediction through the transformation. Define an equation beside the operation it expresses.

For a decomposition, explain why each part has its role. Deep Closest Point learns correspondence and retains rigid alignment by SVD. For attention, specify which elements exchange information and how geometry affects their interaction. “Captures rich spatial dependencies” does not explain an operator.

Define broad names locally. Group-Free removes hard proposal-level grouping, while its backbone retains local grouping. 3DETR reduces task-specific design but still aggregates points. SparseBEV uses sparse detection queries with dense image features. Clear scope makes an ambitious contribution more persuasive.

## Give experiments an explanatory order

Present the main task result, then the comparison that tests the proposed principle, then the regime that explains its value or cost. Use the supplied evidence; do not fabricate analyses to complete a preferred story.

VoteNet compares grouping surface seeds with grouping votes. Point Transformer separates weighting, position encoding, and neighborhood size. RangeDet tests range-based versus area-based assignment. Superpoint Transformer compares quality against the cost of changing the prediction unit. Adapt this logic to the user's actual contribution.

Choose breakdowns that follow from the opening: object extent, observation distance, scan completeness, background, overlap, partition boundaries, or temporal availability. Explain what the pattern means instead of narrating every cell. A single aggregate result can be stated plainly when no breakdown is available.

Name alternative explanations when they materially affect the paragraph. A module combination can show compatibility rather than an independent benefit of every part. A category correlation suggests a mechanism; it does not establish one. Write the measured result first, followed by the appropriate interpretation.

## Keep the details that change the reader's understanding

State the observation condition: native LiDAR view, merged point cloud, clean synthetic shape, real scan, or camera sequence. Describe additional inputs such as normals, height, pose, or training masks when they matter to the claim.

Keep prediction units, assignment semantics, coordinate transformations, and inference-time information in the main explanation. Place layer inventories, routine schedules, and full descriptor lists in setup or supplementary material. Do not bury future-frame access, the use of preprocessing, or a different model variant in a footnote to a headline result.

Use cost measures that fit the benefit. Fewer parameters do not imply faster inference. A precomputed partition has a cost even when training is fast. Explain the tradeoff in a sentence; avoid making the manuscript a repetitive verification exercise.

## Write a confident, concrete contribution

Prefer “gather evidence near object centers,” “estimate correspondences,” “expand spatial support,” “preserve metric geometry,” and “classify geometric regions.” Avoid ornamental terms such as “holistic geometric synergy” and “unprecedented spatial intelligence.” Use established technical terms when they carry a precise meaning.

Sell simplification through what becomes easier to understand or reuse; sell efficiency through the computation removed; sell a benchmark through the failure it reveals. None requires claiming to win every metric.

Use limitations to explain the design. Geometry-only detection can struggle with texture-dependent objects. Region-level prediction cannot undo a bad partition. Constant-velocity sampling is an approximation. These statements help the reader understand when the contribution is useful.

## Resources

- [Writing playbook](references/playbook.md): paragraph structure and result explanations.
- [Worked example](references/worked-example.md): manuscript prose from hypothetical geometric detection results.
- [Ten source papers](references/corpus.md) and [BibTeX](references/references.bib).

Borrow the reasoning, not the wording. Cite these methods in the manuscript when scientifically relevant; the craft corpus is not a mandatory related-work list.
