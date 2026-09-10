# Worked example: separating recognition from mask refinement

All methods, results, and names in this example are hypothetical. They illustrate prose built from supplied evidence, not results of the cited papers.

## Author's material

The model segments and labels objects given a box prompt. A shared frozen visual encoder supplies a semantic region branch and a high-resolution mask branch. A cross-attention alternative mixes the two streams before prediction. Training labels and the encoder are identical across variants.

| Variant | Recognition accuracy | Mask IoU | Boundary IoU |
|---|---:|---:|---:|
| Shared single stream | 71.2 | 78.4 | 53.1 |
| Early cross-attention fusion | 73.0 | 78.6 | 53.5 |
| Separate region and mask branches | 77.1 | 79.0 | 57.8 |
| Separate branches without high-resolution mask features | 76.9 | 78.2 | 53.7 |

These results use ground-truth box prompts on one benchmark. No detector-prompt evaluation or runtime measurement was supplied.

## Story choice

The contribution is a division of information between recognition and mask refinement. The useful comparison is early fusion versus separate branches, followed by removing high-resolution mask features. The story draws on the role separation in [BiSeNet](papers/P02.md), boundary-specific reasoning in [DeepLabv3+](papers/P01.md), and task-interface clarity in [OV-SAM](papers/P10.md).

## Draft abstract passage

Interactive segmentation with category prediction requires a model to recognize the prompted object and recover its boundary. These tasks use different information: recognition relies on semantic region features, while precise masks require spatial detail. We introduce a shared-encoder model with separate region-recognition and mask-refinement branches. On [benchmark], with ground-truth box prompts, the model improves recognition accuracy from 71.2% to 77.1% and boundary IoU from 53.1% to 57.8%. Overall mask IoU increases from 78.4% to 79.0%. The results show that separating the two prediction roles improves recognition and boundary quality within the evaluated setting.

## Draft introduction passage

A box prompt identifies the region of interest, but the model must still determine both its category and its pixel extent. A single feature stream must support these two decisions. Semantic features can recognize an object despite local variations, whereas mask refinement must retain those variations when they mark a boundary. This motivates a model that shares image encoding while assigning recognition and refinement to separate feature paths.

Our method extracts a semantic region representation for category prediction and retains higher-resolution features for mask refinement. Both branches use the same frozen encoder, so the design changes how its information is used. Compared with early cross-attention fusion, the separate branches improve recognition accuracy by 4.1 percentage points and boundary IoU by 4.3 points. Removing high-resolution mask features largely removes the boundary gain while leaving recognition accuracy similar, supporting the different roles assigned to the branches.

## Draft method passage

Given an image and a box prompt, the shared encoder produces a feature hierarchy. The recognition branch pools a semantic representation within the prompted region and predicts its category. The mask branch combines the prompt with higher-resolution encoder features to predict a foreground mask. The two branches share image encoding but retain separate prediction features. [Specify feature levels, the region-pooling operation, mask decoder, and training objectives.]

## Draft results passage

We first compare separate prediction branches with early feature fusion. Early cross-attention raises recognition accuracy to 73.0%, but changes boundary IoU only slightly, from 53.1% to 53.5%. Separate branches reach 77.1% recognition accuracy and 57.8% boundary IoU. The larger boundary improvement suggests that preserving spatial features through the mask path is more useful in this setting than mixing them with recognition features early.

Removing the high-resolution mask features reduces boundary IoU from 57.8% to 53.7%, while recognition accuracy changes from 77.1% to 76.9%. This contrast supports the intended division: the additional spatial information primarily benefits mask refinement. The result does not establish that the branches are independent under every condition, but it explains where the observed gain comes from.

## Draft scope passage

The present evaluation uses ground-truth boxes. It therefore measures segmentation and recognition with an accurately specified region; performance under detector errors remains an open question. The shared encoder avoids duplicate image encoding, but its runtime benefit has not been measured.

## What makes these passages useful

The prose names the actual contribution, uses a diagnostic comparison to explain it, and keeps the task interface visible. It does not call the model universally better, treat a 0.6-point mask-IoU gain as the entire story, or invent a latency result. In a real manuscript, replace placeholders with the author's facts and cite prior methods where they establish the scientific context.
