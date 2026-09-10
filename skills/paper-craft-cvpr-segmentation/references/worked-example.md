# Worked example: a boundary result with a clear motivation

This fictional example borrows the explanatory move of [PointRend](papers/P07.md): different image regions need different prediction effort. It is not a description of PointRend's results. The numbers and method below are invented teaching inputs.

## Supplied material

The author has a coarse segmentation model with mIoU 78.0 and a boundary score of 60.0. An uncertainty-guided refinement module raises these to 78.6 and 64.0. Uniform refinement at the same number of evaluated points gives 78.2 and 61.0. The module reuses coarse predictions in unselected locations. No runtime measurements or thin-object breakdown are supplied.

## Framing

The story is where to spend refinement effort, not simply increasing output resolution. The matched point-count comparison makes that choice informative. Do not rename the method a rendering system unless the actual design and explanation use that connection.

## Title

**Refining Uncertain Boundaries for Image Segmentation**

## Abstract

Coarse segmentation predictions can represent broad regions well while losing detail near object boundaries. We refine a selected set of uncertain locations and reuse the coarse prediction elsewhere. On [dataset], uncertainty-guided refinement improves the boundary score from 60.0 to 64.0 and mIoU from 78.0 to 78.6. Uniform refinement with the same number of evaluated points reaches a boundary score of 61.0. These results indicate that selecting where to refine contributes more to boundary quality than distributing the same prediction effort uniformly.

## Introduction opening

A segmentation map contains broad regions with similar labels and narrow regions where the label changes. A coarse prediction can describe the interiors adequately while smoothing those transitions. Refining every output location gives both regions the same attention, even though their need for additional prediction differs.

We use uncertainty in the coarse prediction to choose locations for refinement. The method preserves the coarse output elsewhere and updates only the selected locations. This makes the allocation of refinement effort part of the segmentation method rather than an incidental consequence of the output grid.

## Method opening

Given a coarse prediction, the module computes [the supplied uncertainty rule] and selects [the supplied number or selection rule] of output locations. A refinement predictor combines [the supplied features] at each selected location to update its label probabilities. Unselected locations retain the interpolated coarse prediction. [Add the supplied training objective and explain whether training uses the same selection procedure.]

The placeholders mark facts the result table cannot establish. They do not prevent drafting the argument or justify inventing a particular sampler.

## Results paragraph

Uncertainty-guided refinement raises the boundary score by 4.0 points, compared with 1.0 point for uniform refinement at the same point count. The corresponding mIoU improvements are 0.6 and 0.2 points. The larger difference in the boundary measure is consistent with the module improving the regions that coarse prediction handles poorly. The uniform comparison further indicates that selecting locations matters, beyond evaluating additional points.

## Detail choices

The point count belongs near the comparison because allocation is the central question. The boundary measure needs its actual definition in the experimental setup. A claim of faster inference does not follow from these inputs, nor does a specific improvement on thin objects. Those extra claims are unnecessary to make the supported finding interesting.

For a real full-draft request, continue with related work, the complete supplied method, setup, remaining experiments, and conclusion. This example focuses on the passages that carry the story.
