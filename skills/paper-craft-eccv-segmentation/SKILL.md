---
name: paper-craft-eccv-segmentation
description: Write and revise ECCV segmentation papers from existing methods and results. Distills ten accepted papers on boundaries, efficient context, multi-task parsing, instance masks, axial attention, open-vocabulary transfer, and interactive segmentation into narrative and experiment-writing guidance.
---

# Write an ECCV segmentation paper

Turn the supplied method and experiments into the requested manuscript. For a full draft, produce connected section prose with concise placeholders for missing facts. Choose a story that explains the contribution, then use the results to develop that story.

## Identify what changes for the reader

| Contribution | Organizing question | Sources |
|---|---|---|
| Context and spatial detail | What information is lost, and where should it be recovered? | [DeepLabv3+](references/papers/P01.md), [BiSeNet](references/papers/P02.md) |
| Context aggregation | Which pixels or regions should exchange information? | [PSANet](references/papers/P03.md), [OCR](references/papers/P05.md) |
| Heterogeneous task learning | Which annotation and feature structure lets these tasks share a model? | [UPerNet](references/papers/P04.md) |
| Instance representation | Where does the model encode the identity of each instance? | [SOLO](references/papers/P06.md), [CondInst](references/papers/P07.md) |
| Attention as a building block | Which spatial interactions become feasible at the available cost? | [Axial-DeepLab](references/papers/P08.md) |
| Open-vocabulary transfer | What mismatch prevents pretrained recognition from working at the desired granularity? | [Simple baseline](references/papers/P09.md) |
| Interactive segmentation and recognition | What does the user provide, and what does the combined model return? | [Open-Vocabulary SAM](references/papers/P10.md) |

A useful introduction moves from a concrete difficulty to a design principle. Blurred boundaries motivate a decoder; similar-looking instances motivate instance-conditioned prediction; image-level pretraining motivates region-level recognition. Avoid opening with a long list of model families followed by an unexplained new module.

## Explain the principle before the machinery

For a representation paper, state the prediction unit first. SOLO indexes masks by location and scale. CondInst encodes instance information in generated filters and relative coordinates. Explain how that unit yields the final masks before presenting losses and layer counts.

For a context paper, name the information source and destination. OCR summarizes soft semantic regions and relates them to pixels. PSANet separates collecting from distributing context. Use this account to introduce equations; do not make the reader reconstruct the method from symbols.

For a combined system, give each part a distinct role. BiSeNet separates spatial detail from context. UPerNet matches tasks to semantic feature levels. OV-SAM transfers segmentation and recognition capabilities through different adapters. A list of named components is useful only after their shared purpose is clear.

## Make experiments continue the argument

Organize each substantive results paragraph around a question, comparison, finding, and explanation. The main benchmark establishes usefulness; a focused experiment explains the contribution.

If boundary recovery motivates the paper, interpret boundary-sensitive results when available, as DeepLabv3+ does with trimaps. If long-range context motivates it, use attention-span or scale experiments, as Axial-DeepLab does. If pretrained transfer is central, distinguish proposal quality from recognition and the method from pretraining data, as the simple open-vocabulary baseline does.

Use simple alternatives to explain necessity. More decoder layers need not help. Absolute coordinates need not replace relative coordinates. A shared encoder alone need not preserve recognition. State which choice changes the result and what that comparison teaches; avoid a sequence of “our module is effective” sentences.

A successful simplification can be a contribution at comparable accuracy. SOLO's representation is valuable without winning every size category. CondInst's small mask head matters because it changes how instance prediction works, not because every parameter count should become a headline.

## Keep details that change the scientific meaning

Keep the prediction target, assignment rule, context unit, supervision source, and task interface in the main account. Explain semantic-class regions versus object instances, source labels versus missing labels, and human prompts versus detector proposals where relevant. Put routine schedules and exhaustive widths in setup or supporting material.

State the evaluated operating point alongside an efficiency result. Input resolution, backbone, and single- versus multi-scale inference can change the comparison. Axial-DeepLab demonstrates that fewer operations can coexist with slower execution; describe the actual benefit plainly.

For open-vocabulary results, explain what is unseen relative to segmentation training and what pretrained knowledge is available. Separate cross-dataset transfer from within-dataset class splits. For interactive methods, point and box inputs define different amounts of information. These details help the reader understand the result; they are not a separate audit procedure.

## Sell the contribution in ordinary English

Prefer “retain spatial detail,” “pool features within a region,” “generate a mask head,” “classify image crops,” and “share an encoder.” Avoid “affluent context,” “holistic semantic synergy,” “unprecedented understanding,” and ornamental substitutes for familiar terms.

Make the central result specific and confident. Explain why a comparable result with a simpler representation matters. Describe a gain concentrated on boundaries, stuff, or novel classes where that pattern appears. Do not weaken every sentence with “may,” but keep an untested mechanism as a rationale rather than a finding.

Describe failed choices briefly when they clarify the design. More prompt-training examples can hurt; joint learning can help one task while hurting another. Such patterns are useful material for explaining the method, not reasons to turn the manuscript into a review report.

## Resources

- [Writing playbook](references/playbook.md): section and paragraph patterns.
- [Worked example](references/worked-example.md): manuscript passages from hypothetical results.
- [Ten source papers](references/corpus.md) and [BibTeX](references/references.bib).

Learn the reasoning without copying source phrasing. Cite a source method in the manuscript when scientifically relevant; the craft corpus is not a compulsory related-work list.
