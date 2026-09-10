# Building a detection paper around an explanation

## A small change needs a clear reason

The apparent size of a code change is not the size of the idea. [Mask R-CNN](papers/P03.md) explains why adding a mask branch demands alignment that classification can tolerate losing. [Focal Loss](papers/P04.md) explains how many individually easy examples can dominate a training objective. [Stable Matching](papers/P10.md) explains a conflicting preference using two candidate predictions.

A useful opening moves from a task to a specific obstacle, then to the principle that addresses it. Name the implementation after the reader understands the principle. Avoid beginning with “we propose modules A, B, and C” and postponing their relationship until the ablations.

For a simplification paper, address the obvious objection. [FCOS](papers/P05.md) explains why per-location detection need not fail through low assignment coverage or overlapping targets. [Fast R-CNN](papers/P01.md) explains why sharing computation during training is possible even when many RoIs come from a small number of images. The objection gives the result intellectual value.

## Give related work an argumentative role

Organize related methods by how they handle the obstacle. For geometric adaptation, distinguish fixed grids, static learned offsets, and offsets conditioned on the input, as [Deformable ConvNets](papers/P02.md) does. For transformer training, distinguish supervision of the encoder from additional positive queries in the decoder, as [Co-DETR](papers/P09.md) does.

Describe the closest alternative accurately and specifically. “Existing detectors ignore geometry” is usually both broader and less helpful than “the training target does not use localization quality to supervise class confidence.” Do not copy a source paper's historical dismissal of an entire family into a new manuscript.

## Order the method by decisions

Explain the prediction unit, its target, the information used to produce it, and how the final result is selected. Then describe the new operation at the step where it acts.

For an alignment method, distinguish three questions: what the model learns to predict, which prediction is matched to an object, and how predictions are ranked at inference. A single word such as “quality” can obscure different roles. [TOOD](papers/P07.md) connects classification–localization agreement to box selection. [Stable Matching](papers/P10.md) explains why a loss and matching cost cannot necessarily share the same form.

For pseudo-labeling, say what a score can actually indicate. [Soft Teacher](papers/P08.md) separates missing foreground labels from uncertain box locations. This gives its two mechanisms separate jobs. Calling both “confidence enhancement” would hide the reasoning.

For a new framework, state which components are inherited. [Mask R-CNN](papers/P03.md) and [Focal Loss](papers/P04.md) make strong contributions without claiming that their backbones and detection heads are entirely new.

## Write a result paragraph that moves beyond the table

Start with the important change. Explain why that comparison answers the question. Add the pattern that helps interpret it, then the scope that matters.

For example, a higher AP after adding a classification–localization target is the outcome. Better localization among the highest-scoring boxes supports the ranking explanation. Different gains at strict and loose overlap thresholds refine the interpretation. None of these requires listing every table cell in prose.

Use a diagnostic suited to the claim:

| Claim being explained | Source of a useful writing pattern |
|---|---|
| Easy examples dominate the objective | [Focal Loss](papers/P04.md), loss-contribution distributions |
| A simpler assignment retains useful coverage | [FCOS](papers/P05.md), best possible recall and ambiguous locations |
| Interior evidence rejects implausible boxes | [CenterNet](papers/P06.md), low-overlap error analysis and center-keypoint oracle |
| Confidence agrees better with localization | [TOOD](papers/P07.md), ranking agreement and retained-box analysis |
| Extra training heads improve representation learning | [Co-DETR](papers/P09.md), feature diagnostics and separated encoder/decoder contributions |
| Matching becomes more consistent across layers | [Stable Matching](papers/P10.md), adjacent-layer assignment changes |

Use this as a guide to explaining available evidence, not a requirement to run every diagnostic. If a desired mechanism remains untested, draft the observed result and identify the explanation as tentative.

## Keep the inconvenient result when it teaches the design

[Fast R-CNN](papers/P01.md) shows why a proposal-recall proxy does not always predict final AP as the proposal count changes. [Co-DETR](papers/P09.md) uses the saturation and decline from adding heads to discuss conflicting supervision. [Mask R-CNN](papers/P03.md) reports that keypoint supervision does not improve every other output.

Such findings can define a useful contribution more clearly than another superiority sentence. Explain why the chosen configuration makes sense. Do not automatically turn a modest negative result into a new module or another page of experiments.

## Choose precise language over inherited rhetoric

Replace “eliminates instability” with the measured behavior, such as “reduces assignment changes between adjacent decoder layers,” when that is what the evidence establishes. Replace “free improvement” with “no added inference branch” when training still costs more. Replace “universal alignment” with the specific relation between confidence and localization.

Reported configurations matter. Co-DETR's core training scheme and its strongest systems do not all use the same post-processing. Stable Matching's main experiments expose an NMS contribution. Fast R-CNN's single-stage training still consumes proposals. These distinctions belong in the relevant method or comparison sentence, not in an intrusive verification workflow.
