# ICCV segmentation writing playbook

## Build the introduction around one unresolved decision

A segmentation paper becomes easier to follow when the reader knows which decision is difficult. Deconvolution asks how to recover object structure from compressed features. CRF-RNN asks how recognition can adapt to refinement. MasQCLIP asks how a model trained on base masks can both propose and name novel regions. SAM asks what a valid output should be when a prompt is ambiguous.

Use four connected moves: describe the desired behavior, identify why the current formulation obstructs it, introduce the change in principle, and state what the results establish. Application lists and broad claims about the importance of segmentation rarely explain the contribution.

Original opening pattern:

> Class-agnostic proposals make it possible to separate region localization from category recognition. However, a region's membership weights need not identify the features that best distinguish its category. We therefore learn a separate pooling distribution for classification while retaining the original mask for localization.

This borrows the explanatory distinction in [DeOP, §§3–4](papers/P09.md). It is useful only when it matches the author's method.

## Give a simple baseline credit

[Segmenter](papers/P07.md) demonstrates that a linear decoder already performs well. This makes the transformer encoder's contribution visible and gives the mask decoder an honest incremental role. [QueryInst](papers/P06.md) starts from a natural mask-head extension and explains why persistent query identities create a better path for supervision.

Do not weaken the baseline rhetorically to make the method seem necessary. Explain what it gets right and what remains unresolved. A targeted contribution is more memorable than a claim that the entire previous architecture is inadequate.

## Explain iterations and information flow

For a recurrent method, write one iteration as an action sequence with a purpose. [CRF-RNN](papers/P02.md) translates message passing and compatibility into familiar operations. [EMANet](papers/P05.md) alternates pixel responsibilities and basis updates before reconstruction. The familiar algorithm helps only if the mapping is explicit.

For spatial context, show how one output receives information. [CCNet](papers/P04.md) uses a two-hop path to motivate sparse recurrence. This establishes connectivity; it does not establish numerical equivalence to dense attention. State the precise property that the explanation demonstrates.

## Turn a result into a paragraph

A useful paragraph answers a question, reports the relevant comparison, and explains its implication. For example:

> Does the gain come from more training or broader supervision? Extending base-only training improves seen-category accuracy but reduces novel-category performance. Adding the mined masks instead improves novel-category performance, suggesting that the added supervision, rather than the longer schedule alone, changes transfer behavior.

This is an original illustration of the logic in [MasQCLIP, Table 4](papers/P08.md). Use the actual direction and magnitude in the author's results. Do not substitute this narrative when the comparison is absent.

For a context method, report quality and resource use together. For an iterative method, separate training depth from evaluation iterations. For a transfer method, show source and target behavior. Each choice follows the paper's question rather than a fixed experiment template.

## Use disagreement to sharpen the interpretation

[Deconvolution](papers/P01.md) makes an ensemble persuasive by showing where each component fails. [Mask R-CNN](papers/P03.md) supports useful joint outputs without requiring every task to benefit. [Segmenter](papers/P07.md) acknowledges a boundary-quality limitation. These observations help define the method's role.

[SAM](papers/P10.md) compares automatic overlap, oracle mask choice, and human judgments because ambiguous prompts admit multiple valid masks. Its human study supplies rating criteria and matched inputs. The transferable writing lesson is to explain what an evaluation measures and why another view is useful, not to dismiss a lower benchmark score as an annotation problem by default.

## Select details by whether they change understanding

| Detail | Keep in the main argument when… |
|---|---|
| Coordinate rounding or patch size | It changes the spatial information available to prediction. |
| A frozen projection or backbone | Preserving pretrained transfer is part of the method. |
| Prompt selection and output choice | They define the difficulty of the evaluated task. |
| Number of passes or precomputed embeddings | They determine what the efficiency claim includes. |
| A training schedule | Extra training is a competing explanation for the gain. |
| Routine optimizer values | Usually summarize once; they rarely need repeated interpretation. |

Use direct verbs and stable terminology. “Classify the region” is clearer than “unlock semantic identification capacity.” Explain novelty through the changed decision, representation, or interface; do not rely on unusual vocabulary to make a familiar operation appear new.
