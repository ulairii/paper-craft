# Writing a software-security contribution for IEEE S&P

This playbook extracts authoring moves from the [ten source papers](corpus.md). They are examples of effective exposition in accepted work, not a formula for acceptance.

## Choose the missing link

A useful opening identifies a gap in the current reasoning about the task. Skyfire distinguishes passing a grammar from passing semantic checks. ProFuzzer distinguishes file-format meaning from the behavior of a particular implementation. Both make a representation useful by explaining which distinction the existing workflow lacks. See [P01](papers/P01.md) and [P06](papers/P06.md).

CollAFL and IJON instead expose a gap in observation. Different behaviors can look identical under the feedback available to the search. The writer should show two such behaviors before presenting a richer representation. CollAFL preserves known edges; IJON lets an analyst expose selected state. Their mechanisms are different, but both explain why more searching under the old signal may make little progress. See [P03](papers/P03.md) and [P07](papers/P07.md).

SAVIOR changes the objective: reaching code and triggering a fault are distinct achievements. Pangolin changes what survives between stages: a satisfying point and a useful approximation of its region carry different information. These stories let a paper stand on a specific conceptual change without inventing a broad claim that existing fuzzers do nothing useful. See [P09](papers/P09.md) and [P08](papers/P08.md).

## Let one example do several jobs

Choose an example small enough to remember and rich enough to expose the method's defining dependency. Introduce it in the problem, revisit it when defining the method, and use its logic to explain an experiment or practical finding.

For input methods, a handful of fields can show what must remain valid and what should change. For hybrid search, nested branches show which progress a later mutation can destroy. For stateful testing, an ordered exchange across two channels can show why neither independent channel mutation nor state tracking alone suffices. Angora, Pangolin, and FuzzUSB offer these three forms in [P02](papers/P02.md), [P08](papers/P08.md), and [P10](papers/P10.md).

Do not introduce a new toy system for every component. Avoid filling the example with casts, allocation cleanup, or unrelated branches. Keep a detail when it explains the mechanism: T-Fuzz's preservation of instruction addresses matters because it supports mapping transformed traces back to the original program. See [P04](papers/P04.md).

## Explain why the representation is the right one

Before a definition, say what the reader needs the object to do. Before an equation, explain its inputs and the decision it controls. After the equation, return to the running example.

NEUZZ's branch predictor is useful because it supplies input gradients for a mutation procedure. The key exposition is the connection between prediction and search, not a generic description of neural networks. ProFuzzer's field labels are useful because different roles call for different mutations; they are not intended as a complete programming-language type system. See [P05](papers/P05.md) and [P06](papers/P06.md).

An approximation can be a strong contribution when its purpose is clear. Describe what it preserves, what it can merge or miss, and why the resulting decision is still useful. Avoid taking a familiar theorem about approximation or sampling and turning it into a guarantee about the entire testing system.

## Make components form an argument

Use a causal chain rather than a component inventory:

1. State the obstacle.
2. Explain the observation that makes it tractable.
3. Describe the changed operation.
4. Explain the consequence of that operation for the next stage.

T-Fuzz is a good model: program transformation reaches new code, but it also creates artificial crashes, so reconstruction follows naturally. FuzzUSB's channel control makes inputs available, while state guidance makes their order useful. Pangolin uses the same approximation twice, giving its two improvements a common explanation. See [P04](papers/P04.md), [P10](papers/P10.md), and [P08](papers/P08.md).

Credit standard components in this chain. Combining established tools can be worthwhile when the new connection changes a meaningful decision. Calling the combination “synergistic” adds no explanation.

## Write experiments as answers

A result paragraph should do more than state that one row is larger:

> The gain is largest on drivers whose data handling depends on a sequence of requests. Enabling multiple channels improves coverage, but state-guided input generation adds a further increase. This pattern is consistent with the method's purpose: channel access supplies the inputs, while state guidance places them in a useful order.

This original illustration borrows the explanatory structure of FuzzUSB; it reports no new measurements. Replace it with the author's actual comparisons and name the relevant table.

Match the experiment to the claim:

| Claim being developed | Informative evidence in this corpus | Writing purpose |
|---|---|---|
| Better search decisions | Fixed input pool with different searches in Angora | Separate input quality from the decision applied to it |
| Better information and its use | Feedback change followed by selection variants in CollAFL | Explain two sources of improvement |
| Useful representation | Model alternatives and concrete mutation cases in NEUZZ | Connect representation choice to downstream behavior |
| Reuse pays off | Solver comparison, sampling comparison, and warm-up curves in Pangolin | Explain benefits and initial cost separately |
| Better fault discovery | Reached-code and triggered-fault curves in SAVIOR | Evaluate the objective rather than requiring every proxy to improve |
| Better state exploration | Same commands but more message combinations in IJON | Show that the missing dimension is sequence, not command variety |

Use the evidence already supplied. If a proposed mechanism has no isolating comparison, write “is consistent with” or “may explain,” or omit the causal claim. A drafting skill should help produce the paper, not replace writing with repeated experimental demands.

## Explain exceptions where they are informative

A slower start can reveal the cost of learning or analysis. A near-tie on a small target can reveal little remaining search space. A benchmark reversal can reveal that the methods exploit different structure. ProFuzzer's LAVA-M comparison and Pangolin's warm-up discussion demonstrate how to make such differences part of the contribution's scope. See [P06](papers/P06.md) and [P08](papers/P08.md).

Avoid declaring a benchmark irrelevant merely because the method loses. Explain what the benchmark exercises and which capability the result speaks to. Likewise, do not call an unsupported explanation established simply because it sounds plausible.

## Choose what belongs in the main paper

Keep information whose removal changes the apparent contribution: source or binary access, analyst effort, the usable input channels, the meaning of an abstract state, a materially adapted baseline, and the unit of the headline result. These facts should be brief and close to the claim they define.

Keep one case that shows the mechanism in action. SAVIOR's consequence-based cases explain why sanitizer violations differ in importance. FuzzUSB's interleaving explains why both state and channel control matter. A long list of CVEs cannot perform either job. See [P09](papers/P09.md) and [P10](papers/P10.md).

Move complete inventories, repeated per-target tables, full helper APIs, and low-level instrumentation into supporting material. Do not push an essential access condition or a central metric definition into the appendix merely to preserve an impressive abstract.

## Replace vague praise with a useful statement

| Weak sentence | More useful direction |
|---|---|
| “Our intelligent framework comprehensively understands software.” | Identify the field role, branch relation, or state signal the method recovers. |
| “The modules seamlessly work together.” | Explain the information one stage supplies and the decision it changes in the next. |
| “The extensive results prove superiority.” | State the principal gain and the workload or budget under which it appears. |
| “Only one line is required.” | State what the annotation expresses; discuss analyst effort separately. |
| “We found hundreds of vulnerabilities.” | Name the measured unit and explain the practical consequences supported by triage. |

Use confident verbs for demonstrated operations and measured findings. Reserve uncertainty for actual uncertainty. Plain language strengthens a technical story because readers can see the contribution without decoding the prose.
