# Worked example: explain confidence–localization alignment

The following method and numbers are hypothetical teaching material. They are not findings from the source papers.

## Supplied material

An ICCV submission changes the classification target of a detector to include localization quality. The baseline reaches 41.0 AP, 60.2 AP50, and 44.0 AP75. The new target reaches 42.2 AP, 60.5 AP50, and 46.1 AP75. The mean IoU of the ten highest-scoring predictions per object rises from 0.63 to 0.66. Adding a feature-fusion block gives a further 0.2 AP. The author has not supplied a matching-stability experiment or results on another detector.

## Find the contribution

The strongest evidence concerns how confidence ranks localized boxes. It does not yet establish that the training process becomes more stable. The feature-fusion block is a secondary improvement, not the central idea.

This framing draws on the decision-level alignment explanation in [TOOD](papers/P07.md) and the distinction between classification targets and matching costs in [Stable Matching](papers/P10.md). The example does not assume that the same target works in every assignment regime.

## Draft abstract

Object detectors use classification confidence to select predictions, but a high class score does not necessarily identify a well-localized box. We introduce a classification target that incorporates localization quality, encouraging confidence to reflect both recognition and box accuracy. On [dataset and split], the new target improves detection AP from 41.0 to 42.2, with a larger gain at the stricter overlap threshold: AP75 rises from 44.0 to 46.1. The mean IoU of the highest-scoring predictions also increases from 0.63 to 0.66. These results support using localization quality in the classification target to improve the selection of accurate boxes.

## Draft introduction passage

The final detection decision depends on more than whether a model recognizes an object. When several predictions overlap, their scores determine which boxes are retained. A confident but poorly localized prediction can therefore displace a more accurate one.

We address this mismatch in the classification target. Instead of assigning every positive prediction the same target confidence, we incorporate its localization quality through [target definition]. This encourages the score used for selection to reflect the quality of the predicted box. The assignment rule and inference procedure remain [describe the supplied configuration].

## Draft results passage

The proposed target improves AP by 1.2 points. The gain is concentrated at the stricter overlap threshold: AP75 increases by 2.1 points, compared with 0.3 points for AP50. This pattern is consistent with improved selection of accurately localized boxes rather than only improved recognition at a loose overlap threshold.

The ranking analysis provides more direct support for this interpretation. Among the ten highest-scoring predictions per object, mean IoU rises from 0.63 to 0.66. Adding the feature-fusion block brings a further 0.2 AP, so we treat it as a complementary refinement rather than attributing its gain to the target change.

## What to retain and what to avoid

The method needs the target formula, how its localization value is obtained during training, and the assignment regime. The experimental paragraph needs the setting under which the baseline and proposed target are compared. Long optimizer lists can be placed elsewhere.

Avoid “we eliminate unstable matching”: matching stability was not measured. Avoid “we improve every aspect of detection”: the evidence is narrower and more informative. A clear ranking contribution is sufficient; it does not need an unsupported optimization story.
