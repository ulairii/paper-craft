# Worked example: writing from existing fuzzing results

This is a fictional teaching example. All method details and measurements below are invented supplied material, not results from the source papers. Bracketed items identify missing facts; they must not become fabricated details in a real draft.

## Supplied material

The method ranks sanitizer-derived targets using a pilot estimate of progress per unit execution cost. It changes target scheduling in an existing fuzzer. Mutation operators, detection instrumentation, seeds, and total one-core budget stay the same across variants. Target acquisition takes two minutes and the pilot takes five minutes; both are charged to the proposed method's 24-hour budget.

Across ten repeats on twelve parsers, the baseline and proposed method both expose the same nine known bugs. Three other bugs remain untriggered in every run of both methods. Median discovery time falls on seven of the nine exposed bugs and rises on two. A representative slow-parser bug falls from 6.0 to 3.8 hours. Removing cost normalization gives 5.6 hours; shuffling the target scores gives 5.9 hours. Final edge coverage is similar. The new-bug campaign has three maintainer-confirmed findings, one with a CVE; the campaign's versions and duration are missing.

## Title

Cost-Aware Target Scheduling for Sanitizer-Guided Fuzzing

## Abstract

Sanitizer checks provide useful fuzzing targets, but reaching different checks can require substantially different execution effort. We introduce a target scheduler that combines observed search progress with execution cost. A short pilot estimates this signal, after which the scheduler allocates effort within an existing fuzzing engine. Across twelve parsers, the scheduler and baseline expose the same nine known bugs; median discovery time decreases for seven and increases for two. On a representative slow-parser target, discovery time falls from 6.0 to 3.8 hours. Removing cost normalization or shuffling target scores largely removes this gain, while final edge coverage remains similar. These results support cost-aware allocation as a way to accelerate selected discoveries without increasing the execution budget. A separate campaign yields three maintainer-confirmed findings.

## 1. Introduction

A fuzzer can spend much of its budget pursuing a target that is expensive to reach. Sanitizer instrumentation identifies checks associated with possible faults, but does not say how much execution effort each check deserves. Treating those targets alike can delay a useful discovery even when the fuzzer already has suitable mutations and enough program coverage.

Our observation is that target selection can use information available during search. Progress toward a check and the cost of producing that progress jointly describe a scheduling opportunity. A target with modest progress may still be productive if it is inexpensive to explore. Conversely, a frequently approached target may consume substantial time without exposing a fault.

We introduce a scheduler that estimates this relationship during a short pilot and uses it to rank subsequent target exploration. The change concerns allocation within an existing engine: it preserves the baseline's mutation operators and runtime bug detection. This makes the scheduler easy to describe and lets the experiments focus on whether the allocation signal is useful.

The evaluation shows a selective benefit. Both methods expose nine of twelve known bugs, with lower median discovery time on seven of those nine under cost-aware scheduling. Similar final coverage suggests that the change primarily affects when useful behavior is reached. Comparisons that remove cost normalization or shuffle the scores support the role of the proposed ranking. Three separately confirmed findings demonstrate practical relevance on [campaign targets and versions].

## 2. Design

The scheduler takes the baseline's candidate targets and seed queue as input. Target acquisition follows [existing mechanism and citation]. During a five-minute pilot, the system records [definition of progress] and the execution time associated with each target. It computes a score using [actual score formula], then selects targets according to [selection rule]. The score therefore expresses the measured relationship between progress and cost rather than an assumed ordering of bug likelihood.

The underlying fuzzer mutates the selected seeds and executes them with the same detection instrumentation as the baseline. New observations update the scores according to [update rule]. Targets without a reliable pilot estimate receive [fallback treatment]. These details determine how the scheduler continues exploring while using the information already collected.

The scheduling mechanism does not change which failures the sanitizer can detect. Its purpose is to allocate a fixed budget so that some failures become observable earlier. The implementation requires [source or binary interface and supported environment]. Target acquisition and pilot execution are included in the total budget reported below.

## 3. Evaluation

We evaluate whether the scheduling signal changes discovery time within a fixed budget. Each method runs ten times per parser for 24 hours on one core, using the same initial seeds, mutation operators, and detection instrumentation. We use [target versions and seed construction] and report per-bug median discovery time across the repeats. The three bugs never triggered by either method are reported as unresolved within the budget, rather than assigned a discovery time.

Both methods expose the same nine known bugs. Cost-aware scheduling lowers median discovery time for seven and increases it for two. The result is therefore an allocation benefit on a subset of the targets, rather than an increase in the number of known bugs reached in this experiment. [Insert the supplied per-target table and available variation summaries.] Final edge coverage is similar, which is consistent with changing the order of useful exploration more than its eventual breadth.

The slow-parser example makes the scheduling effect concrete. Median discovery time falls from 6.0 to 3.8 hours with the full score, but is 5.6 hours without cost normalization and 5.9 hours with shuffled scores. These comparisons support both the cost term and the association between a score and its target. The two slower cases should be interpreted using [available target-level observations]; the current results alone do not identify their cause.

A separate campaign produces three maintainer-confirmed findings, including one assigned CVE. On [representative program], [valid input state and scheduler behavior] leads to [observed fault]. The finding demonstrates practical use beyond known-bug reproduction. Its comparative significance depends on [campaign duration, versions, and baseline campaign information], which are not supplied here.

## 4. Related work

ParmeSan uses sanitizer instrumentation to identify fuzzing targets. MOPT adapts the distribution over mutation operators. EnFuzz exchanges seeds among different engines. Our scheduling decision operates over sanitizer-derived targets and combines progress with execution cost. This positions the change by the decision it makes, while retaining the underlying fuzzing engine. Relevant citations are [ParmeSan](papers/P08.md), [MOPT](papers/P02.md), and [EnFuzz](papers/P04.md); a real manuscript should also discuss the closest target-scheduling methods beyond this teaching corpus.

## 5. Discussion and conclusion

Cost-aware target scheduling improves discovery time for seven of the nine exposed bugs in the evaluated parsers, while two become slower and three remain untriggered. The component comparisons support the usefulness of the allocation signal on the representative slow-parser target. The method retains the baseline's detection scope and execution budget. Its practical contribution is a focused scheduling change whose benefit can be explained through how search effort is distributed.

## Writing choices to reuse

The opening identifies a decision before naming the system. The method explains the score's operational meaning before requesting its formula. The evaluation separates comparative discovery time, explanatory variants, and practical findings. The conclusion states a useful result without changing the claim to universal improvement. These moves draw on [ParmeSan](papers/P08.md), [MOPT](papers/P02.md), [SymCC](papers/P06.md), and [FuzzGen](papers/P10.md).
