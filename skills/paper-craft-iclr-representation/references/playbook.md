# From representation results to a persuasive paper

## Start with the smallest consequential distinction

A strong opening gives the reader a reason to care about the proposed change. DIM distinguishes information quantity from usefulness ([P01](papers/P01.md)). Dimensional Collapse distinguishes constant outputs from occupation of a smaller subspace ([P06](papers/P06.md)). FILIP distinguishes independently computed features from the interaction used to compare them ([P09](papers/P09.md)). Each distinction is concrete enough to predict an experiment.

Build the introduction in four moves: establish the desired capability; expose the limitation relevant to it; explain the design idea; summarize the evidence and consequence. Avoid a long history of self-supervised learning before revealing the problem. For a familiar architecture, spend the novelty budget on the learning principle or observation that changes how it is used.

The contribution sentence should have a subject, a change, and a consequence. For example: “We regularize the local features independently, allowing different encoders to learn a shared prediction target.” Replace this illustration with the author's actual mechanism and demonstrated consequence.

## Choose an evidence sequence

| Story | Useful sequence | What the sequence explains |
|---|---|---|
| A new objective | Downstream result → targeted component comparison → representation diagnostic | Whether the proposed signal adds useful information |
| A scientific finding | Observed phenomenon → simplified analysis → controlled intervention → realistic setting | Which mechanism can explain the observation |
| A scale contribution | Feasible full baseline → constrained approximation → larger application | Where a resource constraint changes the available methods |
| Local pretraining | Global result → local probe → dense transfer → illustrative example | Whether local features, rather than only global recognition, improve |
| Data efficiency | Quality across data budgets → matched-data baseline → training-cost comparison | Whether fewer examples and extra computation are being confused |

Use the sequence that the available material supports. If an important comparison is missing, narrow the claim or leave a specific placeholder. Keep writing the parts that are supported.

BGRL's scale progression is useful because each regime adds a question; its largest-scale result also changes the learning protocol ([P04](papers/P04.md)). DeCLIP's matched-data baseline helps distinguish its objective from filtering and collection ([P10](papers/P10.md)). These are ways to make an argument intelligible, not instructions to run every experiment in either paper.

## Give each component a reason to exist

VICReg explains agreement, variation, and redundancy before giving the combined loss ([P05](papers/P05.md)). iBOT explains how global self-distillation and local masked prediction provide complementary signals ([P08](papers/P08.md)). Follow that order: desired property, failure of the simpler setup, operation that addresses it, mathematical definition.

Acknowledge reuse directly. “We use the existing tokenizer to define prediction targets” is clearer than implying the tokenizer is new. BEiT's distinction between raw patch inputs and discrete output targets is central to understanding its contribution ([P07](papers/P07.md)). A long derivation of familiar machinery would obscure it.

## Explain results without inflating them

A useful paragraph begins with the result that changes the reader's understanding. Follow it with the comparison that supports that reading and the implication for use or mechanism.

**Weak:** “Table 3 demonstrates the effectiveness and superiority of all proposed components.”

**Stronger:** “Hardness helps most at intermediate settings. At higher hardness, accuracy falls, consistent with the increased influence of false negatives that the correction does not fully remove.”

The second sentence follows the reasoning in Hard Negatives ([P03](papers/P03.md)); it does not claim that the diagnostic establishes the only possible cause. Similarly, DGI's random-initialization comparison separates architecture from training ([P02](papers/P02.md)), while its PPI results limit a broad claim about matching supervised learning.

For an explanation paper, be explicit about the algorithm's role. DirectCLR is an empirical consequence of a restricted projector analysis. Its advantage over a linear projector remains meaningful even though a nonlinear projector performs better ([P06](papers/P06.md)). That is a clear scientific story without a universal performance claim.

## Decide what belongs in the main text

Keep facts that determine the interpretation: which representation is evaluated, what labels or external models provide supervision, what baseline has changed, and which resource is counted. These often need only a phrase in a caption or result sentence.

Move facts needed to repeat the run but not to understand the insight into setup or an appendix. Examples include complete prompt lists, detailed learning-rate schedules, and full parameter grids. Keep an unusual setting in the main discussion when its role is the contribution itself.

Do not hide inconvenient protocols. BEiT's fine-tuning results and linear probes answer different questions ([P07](papers/P07.md)). FILIP's precomputed tokens still require token comparisons ([P09](papers/P09.md)). iBOT's extra training memory is compatible with a useful quality–time tradeoff ([P08](papers/P08.md)). State the relevant distinction once and let the contribution stand on its actual benefit.

## Prefer exact language over impressive language

| Vague wording | More useful wording |
|---|---|
| Learns superior semantics | Improves frozen patch classification under the stated protocol |
| Eliminates information collapse | Maintains the measured feature variation during these runs |
| Requires no extra computation | Reuses the encoded batch features |
| Universally data-efficient | Reaches the stated accuracy with fewer distinct training pairs |
| Fully explains deep learning dynamics | Explains the observed mechanism in the stated linear model |
| All components are indispensable | The component improves the reported combination in this ablation |

These are choices of meaning, not a banned-word game. A standard technical term is appropriate when it is the shortest precise description. Prefer one useful claim over several inflated synonyms for the same result.
