# From 3D observations to a persuasive argument

## Introductions: make the mismatch visible

An effective opening connects the input to a difficulty in the output. VoteNet's surfaces and empty centers provide a spatial example. ScanObjectNN supplies an observational example: clean CAD recognition does not test clutter and missing surfaces. RangeDet supplies a representational example: image-grid proximity and metric geometry are not interchangeable. See [P01](papers/P01.md), [P03](papers/P03.md), and [P07](papers/P07.md).

Build the introduction in four moves. State the task under its observation conditions. Explain a specific limitation of the existing representation or operation. Introduce the principle that addresses it. Preview the most relevant result and its useful regime. The contribution paragraph should name a change, a consequence, and evidence, rather than rename each module as a contribution.

For a simpler model, start with the question the simplification makes answerable. [3DETR](papers/P05.md) makes a comparatively generic transformer a useful detection baseline. For an analytic–learned decomposition, identify the uncertain component. [Deep Closest Point](papers/P02.md) learns matching while retaining the rigid solver. Neither story needs an inflated claim that all prior work is obsolete.

## Methods: move through meanings, not tensor names

Explain the input representation, one update, and the resulting prediction before giving the full hierarchy. [Point Transformer](papers/P04.md) provides an operator-to-block-to-network progression. [Group-Free](papers/P06.md) makes object–object and object–point attention distinct, then explains how refined boxes change later positional information.

A useful paragraph has an object, an operation, and a reason: “Each query represents a candidate object. It aggregates encoded point features using its current box geometry. Updating that geometry lets later stages gather evidence for the refined candidate.” Add equations where they disambiguate the operation. Do not substitute a long equation for this explanation.

Define what a simplification preserves. [VoTr](papers/P08.md) expands attention support without densely processing all space. [Superpoint Transformer](papers/P09.md) reduces the prediction elements but retains region geometry and adjacency. [SparseBEV](papers/P10.md) keeps detection sparse while obtaining image features from dense backbones. The remaining ingredients explain how the proposed economy works.

## Experiments: answer the question that justified the design

| Opening problem | Explanatory comparison | Useful interpretation |
|---|---|---|
| Surface evidence is far from box centers | Seed aggregation versus vote aggregation | Relocating the evidence helps the prediction stage |
| A general operator needs point geometry | Scalar/vector weights and position placement | Identify the useful geometric adaptation |
| Range images distort metric relationships | Pixel differences versus metric differences | Test the representation-specific explanation |
| Sparse convolutions have limited support | Local versus dilated support and distance breakdown | Connect context to observation sparsity |
| Point-level computation is redundant | Region granularity, preprocessing cost, and quality | Show the practical information–cost tradeoff |
| Temporal detection needs alignment | No alignment, ego alignment, and object alignment | Attribute the observed increments separately |

These are argument patterns, not required experiment checklists. Write from the experiments the author has. If the method has only aggregate evidence, explain that result and keep the proposed mechanism at the level of a rationale.

A results paragraph should first answer its question. Then use the most informative comparison, explain the pattern, and state a boundary if it changes the conclusion. Avoid “Table 4 shows the effectiveness of every component.” Prefer “Adding dilated support improves distant-object detection, consistent with the need to aggregate sparse observations over a larger region.” Use that wording only if the author's actual breakdown supports it.

## Let mixed results refine the contribution

A lower parameter count with lower throughput is an accuracy–cost tradeoff, as [VoTr](papers/P08.md) illustrates. A strong region model with unrecoverable partition errors is an efficiency–resolution tradeoff, as [Superpoint Transformer](papers/P09.md) explains. A stronger future-frame model is an offline result, as distinguished from online configurations in [SparseBEV](papers/P10.md).

State the benefit first, then the specific constraint. “The region representation reduces training cost, but boundaries merged during partitioning cannot be recovered by the classifier” is more informative than either an unqualified success claim or a generic limitations paragraph.

## Decide which detail belongs in the main text

Keep a detail when removing it changes the scientific claim: synthetic versus real observations, partial overlap, camera versus LiDAR input, supervised foreground masks, prediction granularity, extra temporal information, or preprocessing cost. Put routine implementation values in a concise setup section or appendix. A baseline adaptation belongs beside the comparison when it explains what that baseline actually tests, such as VoteNet's BoxNet objectness labels.

Do not mechanically repeat a source paper's rhetoric. “Invariant,” “group-free,” “fully sparse,” and “state of the art” require a defined scope. The transferable craft is the concrete argument supported by the source, not every adjective its authors used.
