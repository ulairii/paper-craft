# Worked example: foreground-preserving sampling

This is an original teaching example with hypothetical methods and numbers. It does not report results from the cited papers.

## Supplied material

The author targets CVPR with a point-based LiDAR detector. Removing feature upsampling reduces measured latency from 72 to 43 ms, but moderate car AP falls from 79.0 to 72.5. At the retained point budget, 82% of annotated instances retain at least one interior point. A new sampling rule combines learned foreground relevance with spatial coverage. Without upsampling it reaches 78.6 AP, retains points in 94% of instances, and runs in 46 ms. Foreground-only selection retains 96% of instances but reaches 76.8 AP. Small pedestrian results and the second dataset are not supplied.

## Choose the contribution

The strongest story is that better sampling makes a cheaper prediction path useful. It is not “a detector that improves everything”: the original detector remains slightly more accurate. The foreground-only result also gives the spatial coverage term a role beyond an extra ablation row.

The argument borrows the failed-simplification structure of [3DSSD](papers/P07.md) and the operating-point framing of [PointPillars](papers/P03.md). These references inspire the writing move; they do not supply the invented results.

## Draft abstract

Point-based 3D detectors often restore features at discarded points before predicting objects. Removing this upsampling reduces computation, but can leave small or sparsely observed instances without a retained point. We propose a sampling rule that combines learned foreground relevance with spatial coverage, allowing detection directly from the reduced point set. On [dataset and split], the proposed detector reaches 78.6 moderate car AP at a measured latency of 46 ms, compared with 79.0 AP at 72 ms for the detector with upsampling. Instance retention rises from 82% to 94% relative to the reduced detector with conventional sampling. The results show that changing which points survive can recover much of the accuracy lost when feature upsampling is removed.

## Draft introduction passage

Downsampling makes point-cloud processing affordable, but it also determines which objects remain represented in later layers. A detector can recover features at discarded locations through upsampling. Simply removing that stage is therefore not sufficient: faster inference may come at the cost of losing the points needed to detect an instance.

We address this problem at the sampling step. Our sampler combines a learned estimate of foreground relevance with spatial coverage. Foreground relevance helps preserve object observations, while spatial coverage keeps the surrounding information used by the prediction network. This design lets the detector operate on the reduced point set without restoring features at every input location.

## Draft results passage

Removing upsampling lowers latency from 72 to 43 ms, but reduces moderate car AP from 79.0 to 72.5. The proposed sampler recovers AP to 78.6 at 46 ms. Thus, it retains most of the original detector's accuracy while reducing its measured inference cost.

The instance-retention analysis helps explain this recovery. Conventional sampling preserves at least one interior point for 82% of instances, compared with 94% for the proposed sampler. Retention alone, however, does not account for the final performance: foreground-only selection reaches 96% retention but a lower AP of 76.8. This pattern is consistent with spatial coverage supplying useful context in addition to preserving foreground observations.

## Details and boundaries

The experiment section needs the dataset, point budget, latency measurement setting, and definition of instance retention. These facts explain the comparison and can be stated once. It does not need a repeated verification paragraph beneath each result.

The supplied results support a car-detection operating point and a plausible explanation involving context. They do not establish improved pedestrian detection, generalization to another sensor, or a causal proof that background context explains the difference. Keep those boundaries in the prose rather than filling them with invented evidence.
