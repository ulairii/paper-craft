# Worked example: writing an open-vocabulary segmentation argument

All method details and results below are hypothetical teaching material, not findings from the cited papers.

## Supplied material

The author has a frozen vision-language encoder and a separately trained proposal network. The baseline pools features with proposal membership weights. The method learns a spatial pooling distribution inside each proposal. Mask proposals stay the same. On one held-out split, the baseline scores 42.0 seen-class mIoU and 25.0 novel-class mIoU; the method scores 41.6 and 29.0. Full encoder tuning scores 46.0 and 23.5. Measured latency rises from 110 to 116 ms per image under the same setup. There is no evidence about a new dataset or arbitrary free-form descriptions.

## Choose the contribution

The story is region classification under transfer, not improved proposal coverage. The strongest explanation is that a pixel can belong to a region without being equally useful for naming it. This distinction comes from [DeOP](papers/P09.md); the source-versus-target comparison follows the adaptation logic of [MasQCLIP](papers/P08.md).

## Draft title and abstract

**Learning Region Pooling for Open-Vocabulary Segmentation**

> Open-vocabulary segmentation can combine class-agnostic masks with a pretrained vision-language encoder. Yet pooling features according to mask membership gives every included location influence based on where it belongs, rather than how useful it is for classification. We learn a spatial pooling distribution within each proposed region while keeping the encoder and proposals fixed. On the evaluated split, this increases novel-class mIoU from 25.0 to 29.0, with a 0.4-point reduction on seen classes. Full encoder tuning instead improves seen-class performance while reducing novel-class accuracy. These results support adapting region aggregation as a way to improve transfer, at a measured latency increase of 6 ms per image.

## Draft method paragraph

> The proposal mask and the classification pooling distribution perform different jobs. The mask specifies the pixels assigned to a region. The pooling distribution determines how their encoder features contribute to its category representation. For each proposal, a learned module predicts spatial weights restricted to the mask and normalizes them over its pixels. Their weighted feature average is compared with text embeddings to obtain a category prediction. The original proposal supplies the output mask, so this change affects recognition without changing region boundaries. [Insert the supplied module parameterization and training objective.]

## Draft results paragraph

> The improvement is concentrated on novel categories. Learned pooling raises their mIoU by 4.0 points while reducing seen-class mIoU by 0.4 points. Updating the encoder produces the opposite tradeoff: seen-class performance rises to 46.0, but novel-class performance falls to 23.5. Because the proposals are identical, these differences arise downstream of mask generation. The comparison supports adapting aggregation while retaining the pretrained encoder in this setting; it does not establish that the learned weights always identify semantically meaningful object parts.

## Why this prose works

The abstract names the output and the changed operation, gives the gain alongside the tradeoff, and finishes with the practical implication. The method paragraph assigns clear roles before introducing missing implementation detail. The results paragraph answers the transfer question without reciting the entire table.

Avoid replacing this story with “a universal segmentation foundation model,” “free efficiency gains,” or “perfect preservation of generalization.” None follows from the supplied experiment. A clear four-point gain in the intended regime needs no inflated terminology.
