# Writing playbook: machine learning security at USENIX Security

## Choose the story before choosing section titles

An **attack paper** can begin with an overlooked operation in an otherwise ordinary pipeline. [PoisonedEncoder](papers/P09.md) makes random cropping carry the explanation: the operation that creates useful positive pairs also creates an unwanted association. Show the pipeline location and control available to the attacker, then explain why the operation has the reported consequence. Describe the simple mechanism directly before deciding whether formal optimization adds understanding.

A **practical attack paper** can organize itself around obstacles. [CommanderSong](papers/P01.md) ties physical transmission, human perception, and delivery to different design choices and tests. Avoid calling a demonstration “practical” and leaving the reader to infer which obstacle it addresses. Each transition should answer why the next experiment is needed to complete the capability already introduced.

A **privacy inference paper** benefits from a surprising example. [Stolen Memories](papers/P04.md) asks what feature use reveals even when the final prediction looks ordinary. A simplified model then explains the signal. The mathematical account earns its place by resolving the puzzle; it does not need to claim that every assumption remains exact in the later neural-network approximation.

A **defense paper** can turn a diagnosis into a design. [PatchGuard](papers/P06.md) provides a particularly clear pattern: two failure causes, two interventions, then an adversary dilemma. [FLAME](papers/P07.md) uses a different form: early stages make a later protection less costly. Explain the relationship between stages before listing their implementation.

A **constructive reuse paper** can borrow an attack's mechanism for a different purpose. [AttriGuard](papers/P02.md) uses adversarial changes for privacy; [watermarking by backdooring](papers/P03.md) uses an unusual response as a verification signal. The novelty lies in making the new purpose work under its requirements. Organize the evaluation by those requirements rather than suggesting that every underlying technique is new.

A **forensics paper** starts from a different point in the lifecycle. [Poison Forensics](papers/P08.md) receives a known incident and searches for associated records. Explain how that extra observation changes the question and makes a new method possible. A **comparative paper**, such as [ML-Doctor](papers/P10.md), instead aligns conditions so relationships between risks become visible. Its scientific contribution is the resulting knowledge, with the software serving that purpose.

## Write an introduction as four connected moves

1. Establish one concrete operation whose consequence matters. Use an example short enough to retain throughout the method.
2. Explain the precise assumption or missing question in prior work. [Local Model Poisoning](papers/P05.md) distinguishes finite-run attack behavior from the conditions addressed by robustness analyses.
3. State the insight and why it suggests the method. Give the reader the causal connection, not only the method's name.
4. Summarize the evidence and the useful conclusion. Use a small number of representative findings that support the contribution's scope.

A possible defense opening is: “A client can submit an update that preserves ordinary predictions while changing behavior on a chosen trigger. Removing visibly unusual updates addresses only part of this problem. We observe that the remaining updates require much less noise to suppress once their magnitude is bounded. This motivates a defense in which filtering and clipping reduce the cost of the final intervention.” This is an original illustration inspired by the structure of [FLAME](papers/P07.md), not a description of a new proven mechanism.

## Explain results with a reason for the comparison

A useful paragraph has a finding, evidence, interpretation, and consequence. For example: “Combining all three stages reduces the tested attack success while retaining ordinary accuracy. The filtering-only variant retains substantial attack success, whereas noise alone causes a larger accuracy loss. These comparisons suggest that early stages reduce the burden on the final intervention. The benefit therefore comes from coordinating the protections rather than maximizing the detector's standalone accuracy.” Fill this form only with supplied evidence; leave a precise placeholder when a needed number is absent.

For an unexpected outcome, use observation → candidate explanation → focused evidence → narrower conclusion. [Poison Forensics](papers/P08.md) investigates lower recall by removing missed poison samples and comparing with an equally sized random removal. [PoisonedEncoder](papers/P09.md) relates destination-class attack differences to classifier behavior. Such paragraphs explain what the result teaches, instead of apologizing that a score is imperfect.

For practical costs, tie the statistic to the decision. In [PatchGuard](papers/P06.md), incremental masking latency and the cost of the underlying architecture answer different questions. In [AttriGuard](papers/P02.md), a modification budget is a proxy; recommendation quality measures a task users value. Choose the quantity that completes the paper's useful claim.

## Allocate detail by its explanatory role

| Keep in the main argument | Usually move to supporting material |
|---|---|
| The attacker's actual control and the defender's required information | Complete software options and routine training configuration |
| The example explaining the mechanism | More examples of the same already-established pattern |
| The definition of the headline metric and budget | Full alternate-metric grids |
| The essential condition of a guarantee | Secondary proofs and algebraic details |
| A comparison explaining the source of the improvement | Sensitivity sweeps that confirm the same operating behavior |
| A cost or failure case that changes usefulness | Exhaustive per-instance outputs |

Length is not the deciding factor. A short implementation choice can be central: restoring an output layer determines what the [watermark transfer experiment](papers/P03.md) demonstrates. A long formula can be secondary if a small example already explains the mechanism.

## Frame claims with useful verbs

| Vague or inflated wording | More informative direction |
|---|---|
| “A novel and sophisticated framework” | Name the observation and operation it enables. |
| “Perfect privacy” | State the inference reduced, the information available, and the utility retained. |
| “Completely robust” | State the certified condition or the evaluated attack family. |
| “No overhead” | Name the measured operation and comparison baseline. |
| “We identify the attacker” | State whether the output is a record, a source, or an identity. |
| “The best overall security” | Explain how each measured risk responds to the change. |

Precision should sharpen the positive contribution, not bury it under qualifications. The reader should finish a paragraph knowing what was learned and why it matters. Avoid repeating access assumptions in every sentence once they have been clearly established for the section.

## From a results folder to a full draft

Use the user's prompt, method description, and results to select the story. Identify the central finding and the experiments that explain it. Then write the abstract, introduction, method or study design, evaluation, related work, and discussion as prose. Keep figure and table references attached to claims they support. Mark unavailable factual details specifically, such as `[number of participating clients per round]` or `[source for the stated baseline]`.

Do not invent experiments, convert desired outcomes into observations, or substitute a review report for a draft. Missing evidence can narrow a sentence while the rest of the manuscript proceeds. Consult the [worked example](worked-example.md) for an end-to-end illustration.
