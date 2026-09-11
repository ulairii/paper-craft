# Worked example: from results to a software-security draft

This is a fictional authoring example. **ReuseTrace, its evaluation, and every measurement below are invented for illustration.** They are not findings from the reference papers. Bracketed placeholders identify facts an author would need to supply. The prose demonstrates writing structure, not a ready-to-submit research contribution.

## Supplied material

The fictional author supplies a hybrid fuzzer that retains concrete successful input prefixes and resumes mutation after those prefixes. It stores several prefixes for a target rather than only one. It uses the same execution and solving backend as the baseline. It does not infer path regions or automatically identify semantic protocol states.

The supplied experiment uses six source-available parsers, ten independent runs per configuration, one CPU core per run, and a 24-hour total budget including prefix collection. The baseline and two variants use the same initial seeds. Mean coverage relative to baseline is 1.12 for one retained prefix and 1.19 for multiple prefixes. Across all runs, the baseline finds 18 root-cause-distinct faults, the single-prefix variant finds 22, and the full method finds 26. Eleven of the full method's faults are absent from the baseline's collection; three baseline faults are absent from the full method's collection. Median time to a separately specified common coverage target is 9.0, 7.1, and 6.3 hours, respectively. Execution throughput falls by 8% in the full method. One simple parser has coverage ratios 1.00, 1.01, and 1.01. The author has not supplied fault confirmation status, exact parser identities, retained-prefix selection details, or novelty evidence against the closest prior methods.

## Draft title

ReuseTrace: Retaining Successful Input Prefixes for Hybrid Fuzzing

## Abstract

Hybrid fuzzing can expend substantial effort reaching a useful execution point, yet subsequent mutations may discard the input prefix that made that point reachable. We present ReuseTrace, a method that retains concrete successful prefixes and directs later mutations toward their continuations. Keeping several prefixes for a target preserves alternative starting points for further exploration. In an evaluation of six parsers with a shared execution backend and a 24-hour total budget, ReuseTrace increases mean coverage to 1.19 times the baseline and reduces median time to the specified common coverage target from 9.0 to 6.3 hours. Across ten runs per configuration, it exposes 26 distinct faults, compared with 18 for the baseline. Gains are small on the simplest parser, and execution throughput decreases by 8%. These results suggest that retaining useful input structure can improve discovery despite additional per-execution work. [Insert the specific distinction from prior prefix reuse and constrained-mutation methods before making a novelty claim.]

## Introduction

Reaching a deep parser operation often requires a valid sequence of input fields or records. A fuzzer can discover such a sequence and still spend much of its subsequent effort changing the fields that made it useful. The difficulty is therefore not only reaching an operation once, but retaining useful starting points for testing its continuations.

Consider a parser that accepts a header, several setup records, and then a payload. Once a seed reaches payload processing, mutating the header or setup records can return execution to early rejection. Retaining that prefix allows later mutations to concentrate on the payload. A single prefix, however, can restrict exploration to one setup configuration. Several successful prefixes can expose different continuations without requiring a complete model of the input format. [Replace this schematic example with a trace from one evaluated parser.]

ReuseTrace implements this idea by retaining concrete prefixes associated with a target execution point. It selects a retained prefix, mutates its continuation, and keeps new prefixes when the supplied selection procedure identifies additional useful starting points. [Describe the selection criterion and explain why it differs from ordinary seed retention.] The method reuses the baseline's execution and solving backend, so the evaluation focuses on the information preserved between exploration steps.

Prior work establishes several related ways to preserve or expose useful structure. Skyfire uses learned context to generate seeds; ProFuzzer identifies field roles relevant to an implementation; Pangolin retains path approximations for sampling and solving. IJON exposes selected program state through annotations. ReuseTrace instead stores concrete input prefixes. This distinction describes its mechanism but does not yet establish novelty. [Add the closest prefix-preserving and stateful fuzzing methods, then state the precise capability or tradeoff this method contributes.]

Our evaluation asks whether retained prefixes improve discovery, whether keeping multiple prefixes adds value, and when the additional work pays off. The full method achieves 1.19 times baseline mean coverage, compared with 1.12 for a single-prefix variant. Its fault collection is larger but not a superset of the baseline's collection. These results motivate a contribution centered on useful continuation search rather than universal replacement of existing mutation strategies.

## Method

ReuseTrace operates on a seed input and a target execution point. A retained prefix is a concrete initial segment of the input that has previously reached that point. [Define how the prefix boundary is determined and whether the method requires parsing, tracing, or author-supplied boundaries.] The remaining segment is the continuation on which the mutation procedure concentrates.

For each target, the method stores a set of retained prefixes. At a mutation step, it selects one prefix and combines it with a mutated continuation. Execution then determines whether the new input reaches the target and whether it contributes useful behavior. [Specify prefix selection, continuation operators, and how input-length changes are handled.] Keeping multiple prefixes allows the same continuation search to begin from different observed setups.

The retained prefixes are concrete observations. They are not a symbolic characterization of every input that can reach the target, nor a model of all parser states. A changed continuation can affect checks involving earlier fields, so preserving the prefix alone does not guarantee that execution reaches the intended point. [Describe the existing fallback behavior for such inputs.] This account separates the method's intended benefit from a stronger validity guarantee it does not provide.

ReuseTrace uses the same execution and constraint-solving backend as the baseline. Prefix collection and selection add work around that backend. The design is useful only if this extra work improves the value of subsequent executions enough to offset its cost. The evaluation therefore reports throughput alongside coverage and discovery time.

## Evaluation

We evaluate three configurations: the baseline, a variant retaining one prefix per target, and the full method retaining several prefixes. All configurations use the same initial seeds and backend. Each runs on one CPU core for 24 hours, including prefix collection, with ten independent runs. [List parser versions, input interfaces, hardware, and the fault-detection mechanism.] Coverage is reported relative to the baseline, and fault counts are unions across runs after root-cause deduplication.

### Retained prefixes improve continuation search

The single-prefix variant achieves 1.12 times baseline mean coverage, while the full method reaches 1.19 times baseline coverage. The comparison indicates that retaining a useful prefix contributes to the gain and that preserving alternatives adds a further benefit. [Insert per-parser results and variation across runs.] It does not by itself establish which individual prefix property causes the additional coverage.

Median time to the specified common coverage target decreases from 9.0 hours for the baseline to 7.1 hours for the single-prefix variant and 6.3 hours for the full method. [Define the target and how runs that do not reach it are handled.] These timings support the practical value of continuation search under the measured budget.

### Better discovery does not require higher throughput

ReuseTrace executes 8% fewer inputs per unit time than the baseline. Its coverage and time-to-target results nevertheless improve. The useful change is therefore in the behavior reached by those executions, rather than in raw execution speed. On the simplest parser, the full method reaches only 1.01 times baseline coverage. This small gain is consistent with fewer continuation barriers to exploit, although the supplied results do not isolate that explanation.

### The fault collections overlap without containment

Across all runs, ReuseTrace exposes 26 distinct faults, compared with 22 for the single-prefix variant and 18 for the baseline. Eleven faults appear only in ReuseTrace's collection relative to the baseline, while three baseline faults are absent from ReuseTrace's collection. The larger total therefore reflects a different and broader observed collection, not a strict superset. [Report the affected versions and confirmation status before describing any faults as new vulnerabilities.]

[Insert one actual case: the prefix needed to reach the relevant operation, the continuation mutation, the faulty operation, and its observed consequence. Explain how the recorded trace supports the role of prefix reuse. Do not substitute an invented vulnerability for missing evidence.]

## Related work

Input-structure methods provide an important comparison point. Skyfire learns contextual production information for seed generation, while ProFuzzer uses execution responses to infer field roles. ReuseTrace's concrete-prefix approach should be compared in terms of the information required and the continuations it makes available, rather than described as recovering equivalent semantics.

Hybrid and state-guided methods address nearby search problems. Pangolin retains an approximation of a path's solution region; IJON lets analysts expose progress signals; FuzzUSB coordinates multiple input channels using extracted states. These papers suggest useful comparison dimensions, including retained information, manual input, and supported interactions. [Add the closest directly competing methods and explain the actual distinction established by the author's literature review.]

## Limitations

The evaluation covers six source-available parsers under one budget. It does not establish behavior on concurrent protocols, firmware, or targets requiring different input interfaces. Concrete prefixes cover observed setups and can miss alternatives. The three faults found only by the baseline illustrate this practical limit. The supplied evidence also lacks confirmation status for the reported faults and a complete novelty comparison against prior prefix reuse techniques.

## Conclusion

ReuseTrace retains successful input prefixes to focus later mutation on their continuations. Under the evaluated setup, multiple retained prefixes improve coverage and discovery time despite lower execution throughput. The fault collections also show that the method complements, rather than contains, the baseline's observed discoveries.

## Why this draft takes this shape

The opening borrows the representation-and-search connection from [Angora](papers/P02.md) and [Pangolin](papers/P08.md), while the experiment prose separates the objective from its proxies as in [SAVIOR](papers/P09.md). The structure-versus-implementation distinction draws on [ProFuzzer](papers/P06.md). The hypothetical result values and ReuseTrace method come only from this fictional example.

The manuscript cites prior work where it supplies technical context. Writing inspiration is explained here for users of the skill; it need not become a separate section in their papers.
