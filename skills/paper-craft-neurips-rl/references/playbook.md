# NeurIPS RL writing playbook

## Turn results into a contribution

A return table is evidence, not yet a story. Ask what the method changes and which comparison makes that change useful. [HER](papers/P01.md) changes the interpretation of replayed experience. [CQL](papers/P04.md) changes how unsupported values affect learning. [TD3+BC](papers/P08.md) asks how little complexity competitive offline learning needs. Each can support a different introduction using the same broad benchmark family.

Use this progression: concrete obstacle → observation → changed operation → consequence → evidence. For example, a rollout-allocation paper can begin with uneven model reliability across states, introduce a decision about where to generate synthetic transitions, and then show an equal-budget comparison. It need not claim to invent model-based reinforcement learning.

## Choose the experiment that explains the gain

| Intended contribution | Comparison that advances the argument | What to explain |
|---|---|---|
| Reuse of unsuccessful experience | Ordinary replay, alternative relabeling, replay mixture | Why the selected learning signal helps ([HER](papers/P01.md)) |
| Efficient human feedback | Label budget, clip duration, ongoing feedback | Human effort separately from environment interaction ([Preferences](papers/P02.md)) |
| Useful synthetic rollouts | Horizon and no-model update-ratio controls | Model use separately from extra optimization ([MBPO](papers/P03.md)) |
| Offline pessimism | Value gaps and objective variants | The behavior of the penalty, not only final return ([CQL](papers/P04.md)) |
| Decision sequence modeling | Return conditioning, context, decoder or critic variants | What formulation adds beyond the architecture ([DT](papers/P06.md), [TT](papers/P07.md)) |
| A careful combination | Directly combine the inherited methods | Why the new distribution or coupling matters ([COMBO](papers/P10.md)) |
| A simple useful method | Strong baselines, component removal, actual cost | Where simplicity retains quality ([TD3+BC](papers/P08.md)) |

These are ways to interpret supplied experiments, not a mandatory list of new experiments. If a decisive comparison is absent, write the supported result and identify the narrower interpretation.

## Explain heterogeneous outcomes

Write a result paragraph as finding → comparison → interpretation → scope. “The method improves the narrow-data tasks but changes little on broad replay data” is a scientific starting point. Explain the feature of those regimes that relates to the method. Use “consistent with” for a plausible explanation that the experiment does not isolate.

A behavior-cloning baseline that remains strong is informative. [RL Unplugged](papers/P05.md) uses task diversity to expose different algorithm behavior. [Decision Transformer](papers/P06.md) compares filtered behavior cloning to distinguish sequence conditioning from selecting good trajectories. Neither story needs every baseline to fail.

Avoid reporting a succession of table entries. Pick the comparison that changes the reader’s understanding. A plateau at long rollout horizons or a penalty that helps only narrow datasets can give the method a clearer identity than another average score.

## Keep simplicity and theory credible

A simple method should make its inherited components easy to see. “We add a behavior-cloning term to TD3” is more informative than “we introduce a novel hybrid intelligence framework.” Explain what the combination accomplishes and use the appropriate comparator. [COMBO](papers/P10.md) shows why a distribution choice can be consequential even when the surrounding ingredients are familiar.

A theory section should state the question answered by a bound and how it informs the design. [MBPO](papers/P03.md) makes the gap between pessimistic analysis and practical model generalization part of its argument. [CQL](papers/P04.md) distinguishes expected policy value from pointwise action values. Neither pattern requires presenting a neural experiment as a theorem’s exact setting.

## Choose the details that change meaning

A target return is an input, not a promised outcome. A trajectory planner using an external critic is a different system from a standalone action predictor. Offline training with online hyperparameter selection is a different access setting from fully offline selection. Reward relabeling presumes a usable target reward definition. These details belong early because they define the contribution.

Full layer counts, secondary sweeps, and routine optimizer settings usually belong later. Main-text space should explain the idea and evidence. Use an appendix reference when the reader needs implementation completeness rather than another paragraph of settings.

## Write uncertainty as part of the finding

[Statistical Precipice](papers/P09.md) demonstrates an analysis-paper story: repeated experiments and alternative summaries change what conclusions are supportable. Borrow that move when the contribution is empirical understanding. For an algorithm paper, explain the chosen summary briefly and use the evidence actually available. Do not impose an unrelated statistical tutorial on the manuscript.

A probability of improvement, normalized mean return, and success rate answer different questions. State the one relevant to the contribution. “The difference remains unresolved with the available runs” can be a precise result; it does not mean two algorithms are equivalent.

## Sentence choices

| Weak sentence | More useful sentence |
|---|---|
| Our method unlocks unprecedented decision intelligence. | Relabeled goals let the agent learn from trajectories that miss the requested target. |
| We seamlessly synergize two powerful paradigms. | We apply the conservative penalty to model-generated states while retaining the data-value term on observed transitions. |
| Our model is ten times faster. | The policy reaches the reference return with one tenth as many real environment interactions. |
| The attention map proves long-term reasoning. | The attention pattern is consistent with use of earlier context; the context-length comparison tests its practical value. |
| Our lightweight method solves offline RL. | The small modification retains competitive locomotion returns at lower measured training cost. |

These are original illustrations. Use the author's actual mechanism and measured result when drafting.
