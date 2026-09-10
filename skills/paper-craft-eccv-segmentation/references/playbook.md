# Writing an ECCV segmentation manuscript

## Choose a contribution sentence

A contribution sentence should explain the changed prediction process and its purpose. Choose the form that fits the work, rather than combining every form into a grand claim.

| Story | Useful sentence structure | Read |
|---|---|---|
| Complementary information | “We separate X from Y so that each can be processed at an appropriate resolution.” | [BiSeNet](papers/P02.md) |
| Better context unit | “We summarize X into Y, then use Y to refine each prediction.” | [OCR](papers/P05.md) |
| New output representation | “We represent each instance by X, allowing masks to be predicted through Y.” | [SOLO](papers/P06.md), [CondInst](papers/P07.md) |
| Broader task | “We combine these annotations through X, while preserving the supervision available for each task.” | [UPerNet](papers/P04.md) |
| Transfer | “We align the recognition unit with pretraining by X.” | [Simple baseline](papers/P09.md) |
| Interaction | “Given X from the user, the model returns Y using a shared representation.” | [OV-SAM](papers/P10.md) |

These are drafting structures, not source quotations. Replace X and Y with concrete operations and objects.

## Introduction: make the design feel motivated

The first paragraph should identify the task and one consequential obstacle. “Dense prediction requires both spatial detail and context” becomes useful when the next sentence explains why the current computation discards one or makes the other expensive. [DeepLabv3+](papers/P01.md) and [BiSeNet](papers/P02.md) show two ways to develop that tension.

The next paragraph should describe the prevailing solution only as far as needed to explain the gap. CondInst's account of ROI cropping makes its alternative legible: instance specificity can live in the prediction function. Do not call all earlier methods complicated or ineffective; identify the particular dependency the new method changes.

Then state the principle and give a short operational overview. Follow with the most informative result and its implication. Keep contribution bullets parallel: a formulation, a method that realizes it, and evidence of its value. Three small architectural additions do not automatically constitute three independent scientific contributions.

## Method: follow the information

Introduce inputs and outputs in task terms before tensor notation. Then show the transformation that carries the idea. For [PSANet](papers/P03.md), the relevant distinction is the direction of context transfer. For [OCR](papers/P05.md), it is pixels → soft class regions → refined pixels. For [SOLO](papers/P06.md), it is location/scale indexing → associated category and mask.

Use an equation where it removes ambiguity: an assignment rule, normalized region aggregation, or the dependence of generated parameters on an instance. Explain its consequence in the following sentence. Avoid decorating an ordinary concatenation with a new name and several symbols.

Include a detail in the main method when removing it would leave the reader with the wrong model. Relative coordinates in CondInst and label availability in UPerNet qualify. Exact optimizer momentum generally does not. A short setup paragraph or supplementary table can carry routine choices.

## Results: turn a table into an explanation

A useful paragraph has a direction: “We ask whether ...”; “Compared with ...”; “The change is concentrated in ...”; “This pattern supports ...”. Vary the prose naturally; do not repeat these stems mechanically.

| Question raised by the story | Evidence that answers it | Interpretation to develop |
|---|---|---|
| Does refinement help where detail is lost? | Boundary-band or size-dependent results | Connect the gain to the target region, rather than only overall mIoU. |
| Is broad context doing useful work? | Context alternatives, attention span, scale stress | Explain the regime where broader interaction helps. |
| Does the representation separate instances? | Coordinate, grid, assignment, and oracle-mask experiments | Distinguish representational feasibility from remaining mask errors. |
| Does transfer help beyond a larger pretrained model? | Same-pretraining comparisons and proposal/classifier separation | Attribute the architecture's contribution without erasing pretraining's role. |
| Does a joint model preserve both capabilities? | Separate mask and recognition metrics, controlled prompt sources | Explain which capability improves and which stays comparable. |

These are options for interpreting supplied experiments, not a demand to run every experiment before drafting.

Use the strongest relevant comparison as the paragraph's anchor. The [simple baseline](papers/P09.md) strengthens an FCN alternative with sliding windows; [CondInst](papers/P07.md) distinguishes original from improved Mask R-CNN. A well-supported gain over a credible alternative is more persuasive than several weak comparisons.

## Describe cost and scope without draining the story

Cost belongs to a configuration. [Axial-DeepLab](papers/P08.md) reduces operations but reports slower execution; [BiSeNet](papers/P02.md) offers different speed–accuracy points. Say which benefit the author's result establishes, and return to why that benefit matters.

Scope can sharpen a positive claim. The point/box interface in [OV-SAM](papers/P10.md) makes interactive recognition a concrete capability. Calling the same result unrestricted automatic scene understanding obscures that capability. Likewise, name the unseen label set or cross-dataset setting where it gives meaning to a transfer result.

## Revise the language

Replace praise with the operation: “powerful dynamic instance intelligence” becomes “a generated mask head for each instance.” Replace vague gain claims with the observed pattern: “improves all aspects” becomes “improves boundary accuracy while keeping overall mIoU comparable,” when that is what the supplied results show.

Keep standard vocabulary even when an accepted paper uses awkward English. Learn its argumentative structure, not its unusual adjectives. End paragraphs with what the finding teaches about the design, not another synonym for “effective.”
