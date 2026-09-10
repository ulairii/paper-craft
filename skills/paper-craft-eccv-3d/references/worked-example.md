# Worked example: correspondence-guided masked point pretraining

This fictional example illustrates writing from supplied results. The method and numbers below are not findings from the source papers.

## Supplied material

The author combines masked reconstruction with correspondence consistency across aligned partial views. Both variants use the same encoder and downstream fine-tuning setup. On the evaluated indoor segmentation task, scratch training yields 62.0 mIoU with 10% of labels, masked pretraining yields 64.1, and the combined objective yields 66.0. With all labels, the corresponding values are 70.0, 70.5, and 71.0. The combined objective has higher reconstruction error than masked pretraining alone. No outdoor experiment or timing comparison is available.

## Title

Learning Transferable Point Features from Masked and Aligned Views

## Abstract

Masked reconstruction trains a point encoder to recover local geometry, but reconstruction accuracy does not directly measure the features' usefulness for downstream recognition. We combine reconstruction with a consistency objective over corresponding points in aligned partial views. The additional objective encourages the encoder to retain information that remains stable across observations of the same scene. On the evaluated indoor segmentation task, the combined objective reaches 66.0 mIoU with 10% of the labels, compared with 64.1 for masked pretraining and 62.0 for training from scratch. The combined model transfers better despite a higher reconstruction error. These results suggest that cross-view consistency supplies useful supervision beyond reconstruction in this setting.

## Introduction passage

A partial scan contains both scene structure and the effects of how that scene was observed. Masked reconstruction encourages an encoder to predict missing geometry from the visible points. A low reconstruction error, however, does not ensure that the resulting features remain useful when the observation changes or the model is adapted to a recognition task.

We study whether aligned views can complement this objective. Our method pairs masked reconstruction with consistency between features at corresponding scene points. Reconstruction supplies local geometric supervision; correspondence consistency encourages features to agree across different partial observations. The method uses the same encoder for both objectives, so the downstream comparison can focus on the pretraining signal.

The framing draws on [PointContrast](papers/P03.md)'s use of scene correspondences and [Point-MAE](papers/P06.md)'s distinction between reconstruction and transfer. A real manuscript should cite those scientific relationships and explain how its joint objective differs, using the [bibliography](references.bib).

## Method passage

We sample two aligned partial views of a scene and identify corresponding points in their overlap. Each view is divided into local patches, a subset of which is masked. The encoder processes the visible patches, and a decoder predicts the masked geometry. A second loss compares the encoded features associated with corresponding scene points. [Specify correspondence construction, feature sampling, consistency loss, and the weighting of the two objectives.] Alignment is available during pretraining; the downstream segmentation model operates on one scan.

## Results passage

Correspondence consistency improves the transfer of masked pretraining, with a larger benefit when labels are limited. At 10% labeled data, the combined objective improves over reconstruction alone by 1.9 mIoU points; with all labels, the gain is 0.5 points. The same encoder and fine-tuning setup are used in these comparisons. The pattern suggests that the additional pretraining signal is particularly useful when downstream supervision is scarce.

The combined objective produces higher reconstruction error while yielding better segmentation. Reconstruction accuracy therefore does not fully account for the transfer improvement in this experiment. We interpret the result as evidence that the two objectives favor different properties of the representation, rather than as proof that reconstruction is unnecessary. The current evaluation establishes this benefit for the tested indoor task; transfer to outdoor scans remains unmeasured.

## Why the story fits the evidence

The contribution is the complementary supervision and its transfer behavior, not an unsupported claim of universal invariance. The label-fraction comparison gives the result a useful regime. The reconstruction–transfer disagreement explains what the experiment teaches. Missing objective details remain explicit instead of being invented, and the prose does not add speed or outdoor claims absent from the supplied material.
