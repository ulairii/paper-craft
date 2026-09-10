# Worked example: geometry-conditioned evidence aggregation

This is a fictional example of turning supplied results into prose. Its method and numbers are illustrative and are not results from the source papers.

## Supplied material

An indoor point-cloud detector retains the same backbone and prediction head as its baseline. It replaces fixed-radius proposal aggregation with a learned extent-conditioned region. On the author's validation set, AP at 0.5 overlap changes from 41.0 to 44.2. The gain is 5.0 points for large objects and 1.1 for small objects. Merely increasing the fixed radius yields 41.8. Inference time changes from 80 to 92 ms per scene on the same hardware. No experiment isolates occlusion or tests outdoor scenes.

## Title

Extent-Conditioned Evidence Aggregation for Indoor 3D Detection

## Abstract

Point-cloud detectors must gather enough surface evidence to localize an object without including excessive surrounding clutter. A fixed aggregation radius applies the same spatial support to objects with different extents. We introduce an extent-conditioned aggregation stage that adjusts the support of each proposal while retaining the detector's backbone and prediction head. On the evaluated indoor validation set, the method improves AP at 0.5 overlap from 41.0 to 44.2, compared with 41.8 from simply enlarging the fixed radius. The larger improvement on large objects is consistent with the benefit of adapting spatial support. This accuracy gain increases inference time from 80 to 92 ms per scene.

## Introduction passage

An indoor scan observes object surfaces rather than complete volumes. The points needed to estimate a box may therefore be distributed over a region whose size depends on the object. A small aggregation radius can omit useful surfaces, while a large radius can mix them with nearby clutter. This tension motivates choosing support from the current object estimate instead of using one radius for every proposal.

We introduce an extent-conditioned aggregation stage for point-cloud detection. The stage uses the proposal's predicted extent to determine where evidence is gathered, leaving the backbone and prediction head unchanged. This design lets us study whether adapting spatial support improves detection beyond the benefit of a uniformly larger neighborhood.

The geometric motivation follows the kind of reasoning developed in [VoteNet](papers/P01.md), while the role of a changing object estimate is related to [Group-Free](papers/P06.md). A real manuscript should cite those papers where it explains the scientific relationship, using [the bibliography](references.bib), and state how the proposed operation differs.

## Method passage with missing facts left visible

For each proposal, we predict an extent vector from its current feature. We use this vector to define the region from which point features are aggregated. [Specify the region shape and the mapping from predicted extent to support.] The resulting object feature is passed to the unchanged prediction head. [Specify the extent supervision and whether the stage is repeated.] These details are needed to describe the proposed operation; inventing them would make the draft inaccurate.

## Results passage

Conditioning the aggregation region on object extent improves AP at 0.5 overlap by 3.2 points. Increasing the fixed radius produces a smaller 0.8-point gain, suggesting that the benefit is not explained by a uniformly larger neighborhood alone. The improvement is greater for large objects than small objects, consistent with the motivation that a fixed region can omit surfaces of extended objects. The available results do not separately establish how occlusion affects this behavior.

The accuracy improvement comes with an additional 12 ms per scene under the same timing setup. The method therefore offers a useful accuracy–latency tradeoff for the evaluated indoor setting. Its behavior on outdoor scans remains an open question.

## Why this framing works

The opening identifies a spatial tension before naming the method, as [VoteNet](papers/P01.md) does with surface points and empty centers. The comparison against a larger radius explains why adaptation matters. The object-size breakdown connects the result to that motivation without claiming causality. The cost sentence follows [VoTr](papers/P08.md)'s instructive tradeoff: a useful accuracy result does not need to be described as a speed improvement.
