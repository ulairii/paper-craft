# Worked example: a training-only localization contribution

The method and results below are fictional. They illustrate how to draft from supplied evidence and are not measurements from the reference papers.

## Supplied material

A two-stage detector changes its positive-proposal threshold using a statistic of recent proposal overlap. The backbone, head, and inference procedure are unchanged. The author's validation results are: fixed threshold 38.0 AP, 59.5 AP50, 10.0 AP90; best tested constant threshold 38.5 AP, 59.0 AP50, 11.6 AP90; adaptive threshold 39.4 AP, 59.1 AP50, 14.0 AP90. A second backbone gains 1.1 AP. No regression-loss adaptation is proposed. The precise threshold statistic has not yet been supplied.

## Title

Adapting Positive-Proposal Assignment to Improving Localization

## Abstract

The quality of region proposals improves during detector training, but a fixed assignment threshold applies the same criterion throughout optimization. We study an adaptive assignment rule that updates this threshold from recent proposal overlap statistics. The rule changes training while retaining the detector's inference procedure. On the evaluated validation set, it improves AP from 38.0 to 39.4 and AP90 from 10.0 to 14.0. The best tested constant threshold reaches 38.5 AP, indicating that the adaptive rule offers a benefit beyond selecting a different fixed value. A second backbone gains 1.1 AP. The larger improvement at strict overlap reflects the method's emphasis on precise localization.

## Introduction passage

A proposal that is useful early in training may be a weak positive later, after the proposal network has improved. A fixed overlap threshold treats both stages alike. Raising the threshold throughout training can emphasize better-localized examples, but choosing a high value from the start can leave too few useful positives. We therefore use the observed proposal quality to update the assignment criterion.

This idea belongs in direct conversation with [Dynamic R-CNN](papers/P03.md), which already adapts assignment and regression to training dynamics, and [PAA](papers/P04.md), which uses model-dependent scores for assignment. The author's actual distinction must be stated here: [explain how the proposed statistic or objective differs from these existing methods]. The supplied results alone do not establish that this is a new method. A usable draft should expose that missing scientific distinction instead of inventing novelty.

## Method passage

At each update, we summarize the overlaps between recent proposals and their matched training boxes. [Define the statistic, observation window, and update rule.] The resulting threshold determines which proposals receive positive labels in subsequent training steps. Classification and regression otherwise follow the baseline detector. Because the adaptation changes only the training labels, the trained model uses the same inference procedure as the baseline.

## Results passage

Adaptive assignment improves overall AP by 1.4 points and AP90 by 4.0 points. The best tested constant threshold gives a smaller overall gain of 0.5 points. This comparison supports adapting the assignment rule over training rather than replacing the baseline threshold with another constant. The second backbone's 1.1-point gain shows that the effect is not limited to the first backbone in these experiments.

The improvement concentrates at strict overlap: AP50 changes from 59.5 to 59.1 while AP90 rises from 10.0 to 14.0. This pattern is consistent with an emphasis on precise localization. It does not establish that the method improves every aspect of classification or detection. We retain the unchanged inference procedure as a practical advantage without claiming that the unmeasured training overhead is zero.

## Why this framing works

The introduction follows a changing-distribution argument from [Dynamic R-CNN](papers/P03.md). The constant-threshold comparison makes the adaptation's value concrete. The overlap breakdown follows the explanatory style of [SABL](papers/P05.md): a mixed metric pattern can clarify the target of the contribution. The draft remains prose a researcher can develop, with the missing method definition and novelty distinction visible in place.

Use [the bibliography](references.bib) to cite these methods where their scientific relationship is discussed.
