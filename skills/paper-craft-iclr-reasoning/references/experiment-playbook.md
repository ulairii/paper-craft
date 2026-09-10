# Claim-driven experiments and result interpretation

These recommendations are distilled from the corpus. They do not imply that every source paper performed every suggested check.

| Intended claim | Main competing explanation | Critical controls and metrics | Interpretation and boundary | Evidence |
|---|---|---|---|---|
| Aggregation is more reliable | More sampling alone explains the gain | Fix candidates; compare majority voting, likelihood ranking, and learned verification; plot budget curves | Attribute to selection, without guaranteeing faithful intermediate reasoning | [P01](papers/P01.md), Sections 3.4–5 |
| Decomposition improves complex reasoning | More demonstrations or a friendlier representation | Match demonstrations/representation; slice by composition length or solution steps | Test easy-to-hard generalization; do not use another task's large gains to embellish a small aggregate gain | [P02](papers/P02.md), Tables 4/12/13 |
| The model learns self-correction | A stronger first attempt, an oracle, or more attempts | First/final accuracy, all four correctness transitions, matched-budget resampling, and test-feedback removal | Separate net revision gains from base capability; state denominators | [P03](papers/P03.md), Fig. 1; [P06](papers/P06.md), Tables 2/4 |
| Process supervision beats outcome supervision | Data quantity, annotation quality, or generator differences | Best-system results plus matched data/generator/capacity experiments | Give each comparison its own conclusion; do not conflate them | [P04](papers/P04.md), Figs. 3–4 |
| A verifier better measures progress | Search changed or a stronger prover supplied the gain | Fix search; vary rewards; cross base/prover strength; use a random-reward control when relevant | Establish conditions for complementarity, not universal weak-over-strong superiority | [P07](papers/P07.md), Fig. 5; [P08](papers/P08.md), Tables 4–6 |
| Compute allocation is better | Difficulty uses answers or uncounted sampling | Strategy×budget×difficulty; separate oracle/predicted difficulty; include routing cost | Bound claims by searched strategies; post hoc bins are not deployable routing | [P05](papers/P05.md), Section 3.2, Appendix O; [P10](papers/P10.md), Appendix G |
| Self-verification fails | Weak prompts or one error type masking another | Verifier confusion matrix, stronger prompts, sound verifier, separate critique generation/use | Locate the failing component and retain counterexamples | [P09](papers/P09.md), Section 4, Appendix A; [P03](papers/P03.md), Section 5 |
| CoT improves a task family | Parsing, planning, or execution changed | Same-model prompt controls, instance slices, planning/execution separation, invalid-output statistics | Do not generalize single-prompt findings to all TTC | [P10](papers/P10.md), Sections 4–5, Appendices F/H |

## Cost ledger

Distinguish generation calls, auxiliary-model calls, input/output tokens, search expansions, difficulty estimation, offline data generation/training, and actual latency. State which quantities are measured, estimated, or excluded. Match accounting precision to the efficiency claim; unrelated metrics need not be required.

A rollout in [P08](papers/P08.md) contains multiple calls. [P05](papers/P05.md) excludes difficulty-estimation overhead from its main accounting. [P07](papers/P07.md) distinguishes sample efficiency from verifier overhead. Equal N, equal parameter counts, or no fine-tuning therefore do not establish fairness. For total deployment cost claims, report accuracy within a budget or complete cost to reach target accuracy, together with assumptions for amortizing offline investment.

## Uncertainty and denominators

Distinguish repeated sampling, independent training seeds, and bootstrapping a fixed test set; they quantify different uncertainty. Record test size, treatment of parsing failures, and model/data versions. Do not mechanically require many seeds for a low-impact display, but small differences central to a claim need an appropriate uncertainty analysis. P01's sampling repetitions are not training seeds; P02's small-sample, overlapping error categories are not population error rates.

## Interpretation paragraph template

> Under [task, model, budget], [comparison] yields [observation]. Because this control holds [variables] fixed, the result supports [narrow claim]. It is consistent with [mechanism hypothesis], but [uncontrolled factor] remains unresolved, so it does not establish [stronger claim]. The change under [counterexample condition] further limits the applicable scope.

This is an original writing scaffold, not a quotation. Do not copy it mechanically into every paragraph. When mechanism evidence is absent, an accurate performance description is a valid stopping point.
