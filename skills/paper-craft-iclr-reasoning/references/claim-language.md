# What to claim and what to avoid

All English examples below are original revisions, not quotations from the papers. Bracketed content must be filled from the user's actual materials. Rewording cannot substitute for an unperformed experiment.

| Risky wording | More accurate wording or action | Reason and source |
|---|---|---|
| Our model improves self-correction by 15.6 points in one revision. | Relative to the base model, SCoRe improves the second-minus-first accuracy gain by 15.6 percentage points on the reported MATH evaluation. | P06 Table 2 reports a difference in deltas, not the gain from a single revision; see the worked example. |
| Our method is four times cheaper end to end. | Excluding difficulty-estimation overhead, the evaluated allocation reaches [target] with [budget comparison]. | Fill numbers only when supported; the excluded cost in P05 Section 3.2 changes the claim's meaning. |
| Smaller models reason without help from stronger models. | The system uses a [size] generator and a [size] auxiliary model; we report their standalone task performance separately. | P08 Table 2 shows why parameter count is not task capability. |
| LLMs cannot self-correct. | Under the evaluated models, prompts, and feedback-free setting, iterative revision does not consistently improve accuracy. | P03 has scope limits; P09 Table 1 includes exceptions; P06 changes training conditions. |
| Our verifier guarantees correct reasoning. | The verifier improves final-answer selection under [candidate distribution]; this evaluation does not establish the correctness of every intermediate step. | P01 Section 5 and P04's evaluation target. State explicit assumptions separately if a formal guarantee exists. |
| Our compute-optimal policy always outperforms scaling models. | Among the evaluated allocation strategies, [policy] is preferable in [difficulty/load regime]. | P05 Section 7 and Appendix O do not establish global optimality or dominance at every workload. |
| CoT is useless outside math. | In the tested single-prompt setting, gains are concentrated in math and symbolic tasks, with task-specific exceptions. | P10 Section 4.2 does not cover all TTC. |
| The ablation proves that module X explains all gains. | Holding [controls] fixed, removing X reduces [metric], supporting its contribution in this setting. | P04's controlled attribution and P08's crossed controls; removing a component does not eliminate all interactions. |

## How to frame novelty

Replace “novel,” “efficient,” “general,” and “powerful” with a concrete contrast: what the previous selector evaluates versus yours; which error transition your training changes; or how your analysis determines where to allocate compute beyond observing that more compute can help.

Three useful forms:

- Method: We address [observed failure] by changing [specific decision], rather than merely increasing the number of attempts. Keep the second clause only with a matched-budget control; otherwise remove it.
- Analysis: We characterize how [allocation preference] changes with [difficulty and budget], yielding guidance for [decision]. This follows P05's contribution type without implying a new algorithm.
- Negative result: We isolate [confound] and reevaluate [claim] under [controlled setting]. This follows P03/P09 without using failure to assert the nature of models.

“First” and “state of the art” require a separate literature check, a stated date, and comparable protocols. This skill's historical corpus does not provide that endorsement.
