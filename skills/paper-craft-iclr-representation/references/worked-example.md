# Worked example: make a local-feature contribution concrete

This is a fictional teaching example. All numbers below are invented and must not appear in a real manuscript as experimental evidence. The method name is a placeholder, not a published system.

## Material supplied by an imagined author

The author has an image-pretraining method that balances the contribution of different patch targets. The same encoder, data, and training schedule are used throughout. Evaluation gives:

| Variant | Frozen image classification | Frozen linear segmentation | Full segmentation fine-tuning |
|---|---:|---:|---:|
| Global objective | 74.0 | 30.0 | 44.0 |
| Global + equally weighted local prediction | 74.3 | 32.2 | 44.8 |
| Global + balanced local prediction | 74.4 | 34.1 | 45.5 |

The final variant takes 8% more training time than the global baseline and 1% more than equal weighting. A texture-heavy evaluation subset shows no improvement. There are no repeated-run estimates yet. The exact balancing formula and dataset identity must be supplied.

## Title and abstract

**Balancing Local Prediction Targets for Transferable Patch Features**

“Image-level agreement provides a useful pretraining signal, but it does not directly determine which information individual patches retain. We study how the distribution of local prediction targets affects the resulting features. Our method, [METHOD], balances [DEFINE THE TARGET CONTRIBUTION] while retaining the global objective. With the same encoder, data, and schedule, it improves frozen linear segmentation from 30.0 to 34.1 mIoU and full segmentation fine-tuning from 44.0 to 45.5 mIoU on [DATASET]. The corresponding image-classification change is smaller, from 74.0% to 74.4%. These results support a contribution in local transfer, with an 8% training-time increase over the global baseline.”

The abstract leads with the meaningful difference in the results. It does not sell a large global-recognition gain or claim that balancing improves every kind of feature.

## Introduction passage

“Representations used for dense prediction must preserve information at individual image locations. A global recognition score offers only an indirect measure of that capability. In our baseline, adding local prediction improves segmentation more than image classification, suggesting that the local objective provides information not fully reflected in the global score. We therefore investigate how the distribution of local targets affects the features learned at each patch.

“We propose [METHOD], which balances [TARGET CONTRIBUTION] during local prediction. The global objective retains its existing role, while the modified local term changes [PRECISE OPERATION]. Our experiments separate the addition of local prediction from its weighting: equal weighting already improves transfer, and balancing provides a further gain. The strongest effect appears in frozen segmentation, where adaptation cannot rewrite the encoder features.”

This follows the distinction-driven openings in [DIM](papers/P01.md) and [Dimensional Collapse](papers/P06.md), and the local-evidence reasoning in [iBOT](papers/P08.md). Their experiments are not evidence for this fictional method.

## Method passage

“Given an image, the encoder produces a global representation and a sequence of patch features. The global objective aligns [DEFINE THE PAIRED VIEWS]. The local objective predicts [DEFINE TARGETS] from [DEFINE VISIBLE INPUT]. We assign each local target a weight determined by [FORMULA AND NORMALIZATION], so that [STATE THE INTENDED BALANCING EFFECT]. The total loss combines the unchanged global term with this weighted local term using [COEFFICIENT]. At transfer time, [STATE WHICH FEATURES AND HEADS ARE RETAINED].”

The passage explains the roles before introducing a full loss expression, following [VICReg](papers/P05.md). Its placeholders request scientific definitions, not routine implementation logs.

## Result passage

“The clearest benefit of balancing is in frozen local transfer. Equal weighting raises linear segmentation from 30.0 to 32.2 mIoU, and balancing increases it further to 34.1. Full fine-tuning also improves, although the difference is smaller. The image-classification results change by only 0.4 percentage points relative to the global baseline. This pattern supports a benefit in the usefulness of patch features rather than a broad improvement in every representation metric.

“Balancing adds 1% training time relative to equal weighting; the complete method costs 8% more than the global baseline. It provides no gain on the texture-heavy subset. The current results therefore support improved local transfer in the evaluated setting, while leaving its behavior on texture-dominated tasks unresolved. [ADD REPEATED-RUN VARIATION WHEN AVAILABLE.]”

The cost comparison follows the concrete resource accounting in [FILIP](papers/P09.md) and [DeCLIP](papers/P10.md). It states the useful result without calling extra computation free or inventing statistical significance.

## What the draft does not yet establish

The table does not explain why balancing helps. If the author has a target-distribution diagnostic, use it to connect the intervention with the proposed explanation. Otherwise present that explanation as a hypothesis. Do not manufacture an ablation, assume causal semantic disentanglement, or replace the requested prose with a request to run a long experiment suite.
