---
name: paper-craft-eccv-detection
description: Write and revise ECCV object detection papers from existing methods and results. Distills ten accepted papers on keypoints, set prediction, dynamic training, assignment, localization, semi-supervised learning, and open-vocabulary detection into narrative and experiment-writing guidance.
---

# Write an ECCV object detection paper

Turn the author's method and results into the requested manuscript. A full-draft request calls for connected manuscript prose, with concise placeholders for missing information. Choose the story from the contribution rather than the detector acronym.

## Find the organizing question

| Contribution | Question that gives the paper direction | Sources |
|---|---|---|
| New detection representation | What does the output structure let us simplify? | [CornerNet](references/papers/P01.md), [DETR](references/papers/P02.md) |
| Training or assignment | Which fixed rule no longer matches the model's learning state? | [Dynamic R-CNN](references/papers/P03.md), [PAA](references/papers/P04.md) |
| Precise localization | Which smaller decisions make a tight box easier to predict? | [SABL](references/papers/P05.md) |
| Semi-supervised learning | What information or task structure is lost in the current teacher–student recipe? | [Dense Teacher](references/papers/P06.md), [PseCo](references/papers/P07.md) |
| Open-vocabulary detection | How do regions, labels, and language interact during learning? | [OV-DETR](references/papers/P08.md), [Grounding DINO](references/papers/P09.md) |
| Geometric priors in transformers | Which relation should be explicit instead of learned indirectly? | [Relation DETR](references/papers/P10.md) |

Open with the specific difficulty: a corner with no local evidence, duplicate predictions, improving proposals under a fixed threshold, a broad regression displacement, or pseudo labels that preserve category confidence but lose localization information. Explain the proposed principle before naming its modules.

## Build a contribution that the reader can explain back

A reformulation should state the task in its new terms. DETR treats detection as set prediction; CornerNet detects and groups corners; SABL selects a coarse boundary interval and then refines it. Name the prediction unit and show how it becomes a box.

A multi-part method needs a shared reason. PAA connects assignment, optimization, and ranking through classification and localization quality. Grounding DINO organizes language fusion by feature enhancement, query selection, and decoding. Use such an organizing map when the author's components solve connected problems; do not manufacture one for unrelated additions.

A training contribution should explain the mismatch and the adaptation. Dynamic R-CNN first describes changing proposal quality, then changes assignment and loss behavior. Distinguish a rule that depends on training observations from a manually chosen schedule.

## Use simple alternatives to make the method necessary

A convincing experiment can show why the obvious approach is insufficient. Dense Teacher's plain dense-label substitution gives a modest gain before region selection. OV-DETR's direct addition of unlabeled proposals hurts before conditional matching makes them useful. SABL's bucketing without fine regression loses precision. PseCo compares aligned views with an ordinary extra view.

When such evidence is supplied, make it the center of the relevant results paragraph: question, simple alternative, proposed change, interpretation. Do not reduce it to “all modules are effective.” If no such comparison exists, write the supported finding and keep the mechanism as a rationale rather than an observed fact.

Use breakdowns that answer the opening. Tight-box methods need overlap-dependent interpretation; semi-supervised methods need label-budget context; open-vocabulary methods need base/novel or target-dataset context. A convergence claim should distinguish progress per iteration from training time when per-step work changes.

## Preserve the details that define the claim

Keep assignment targets, query conditions, box parameterization, and training versus inference roles in the method. Explain a small detail if it makes the idea work, such as SABL's treatment of the second-nearest bucket or PseCo's pyramid-level alignment. Move ordinary schedules and layer inventories to setup or supplementary detail.

State whether results use box AP, AP50, mask AP, or another metric when introducing the comparison. For open-vocabulary work, define what is unseen and what pretrained information is available. Training without the target dataset is different from training without related concepts. For efficiency, keep the evaluated configuration and its cost together.

Treat a source paper's abstract as an argument to learn from, not a list of phrases to inherit. Anchor-free does not mean post-processing-free. Dense pseudo labels do not mean every prediction is copied. A conditional detector can reuse image features while its decoder cost still grows with vocabulary size.

## Sell the useful result in ordinary English

Prefer “predict box boundaries,” “adapt the assignment threshold,” “retain teacher scores,” “match regions to a query,” and “add relative box geometry.” Avoid “holistic localization synergy,” “unprecedented detection intelligence,” and unfamiliar substitutes for standard words.

A comparable result can establish a valuable simpler formulation. A lower AP50 can coexist with better tight-box localization. More pretraining data can help one transfer task and hurt another. Explain these patterns confidently instead of claiming every number improves or burying the central result under caveats.

End a contribution statement with what becomes possible, easier, or more accurate under the demonstrated conditions. Do not promise universal detection or guaranteed acceptance.

## Resources

- [Writing playbook](references/playbook.md): paragraph logic and useful experimental contrasts.
- [Worked example](references/worked-example.md): draft passages from hypothetical training results.
- [Ten source papers](references/corpus.md) and [BibTeX](references/references.bib).

Learn from the sources' reasoning without copying their wording. Cite source methods in a manuscript when scientifically relevant; these craft references are not a compulsory related-work list.
