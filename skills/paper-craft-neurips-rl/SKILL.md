---
name: paper-craft-neurips-rl
description: Draft and revise NeurIPS reinforcement-learning papers from methods and existing results. Distills ten accepted papers on sparse rewards, human preferences, model-based control, offline RL, sequence policies, and empirical evaluation into narrative, method exposition, and experimental interpretation.
---

# Write a NeurIPS reinforcement-learning paper

Produce the manuscript the author requests. For a full draft, write connected section prose and mark missing facts with specific placeholders. Let the existing evidence determine the contribution and the strength of the story.

## Find the central contribution

| Contribution | Story to develop | Examples |
|---|---|---|
| A learning signal | How does previously unhelpful experience become useful? | [HER](references/papers/P01.md), [Human preferences](references/papers/P02.md) |
| A model-use decision | When and how should synthetic experience affect learning? | [MBPO](references/papers/P03.md), [COMBO](references/papers/P10.md) |
| An offline objective | What specific failure of policy or value learning does the objective address? | [CQL](references/papers/P04.md) |
| A benchmark | Which consequential comparisons become possible? | [RL Unplugged](references/papers/P05.md) |
| A decision formulation | What is represented, predicted, and decoded into actions? | [Decision Transformer](references/papers/P06.md), [Trajectory Transformer](references/papers/P07.md) |
| A simple baseline | What quality and practical benefit require only a small change? | [TD3+BC](references/papers/P08.md) |
| An empirical explanation | What accepted conclusion changes after a better analysis? | [Statistical Precipice](references/papers/P09.md) |

Choose the useful difference from prior work. A new replay operation, a careful combination, or a stronger simple baseline can carry a paper. Do not inflate those contributions into a universal RL paradigm.

## Open with a concrete decision problem

Explain the obstacle and its consequence before introducing the method name: sparse failure signals provide little guidance, a learned model becomes unreliable over long rollouts, or offline value estimates favor unsupported actions. Give the observation that suggests the solution, then state the changed operation and the result it enables.

Use one short example when it clarifies the operation, as HER does with an achieved but unintended goal. Avoid a long history of reinforcement learning. Contribution bullets should name a mechanism, capability, or finding; “we propose a method and conduct extensive experiments” communicates none of these.

## Explain the algorithm through its interfaces

State what data are available, what signal is learned, and how the agent chooses an action. For preference learning, connect comparisons, reward learning, and policy updates. For model-based learning, explain where rollouts start and where their transitions enter the update. For sequence policies, distinguish predicting an action conditioned on a target from jointly predicting trajectories and searching them.

Introduce the objective only after the reader understands its terms. Explain the contribution of each changed term in ordinary language. Credit the inherited optimizer, model, and data construction. Keep theoretical assumptions beside the interpretation of a result; move extended proofs after the main argument. An ideal policy-update analysis and its practical neural implementation need not be identical, but their relationship should be clear.

## Make each experiment advance the story

Lead with the result that establishes the contribution, then explain it through a targeted comparison. MBPO contrasts rollout lengths and update ratios; COMBO compares with a direct combination of its parent methods; TD3+BC compares quality alongside training cost. These experiments answer different scientific questions.

Organize the result section by questions rather than by a list of datasets. Explain what changes across data quality, reward sparsity, context, or model horizon. A strong behavior-cloning baseline can sharpen the contribution by revealing when policy improvement adds value. A setting where the method stops helping can define a useful operating regime.

Give resource claims the correct unit: human labels, environment interactions, training time, and action-selection latency are different resources. Describe statistical summaries when they affect the conclusion, using available runs. Do not turn drafting into an open-ended demand for more experiments.

## Put consequential details in the main argument

Keep reward access, offline versus online selection, external critics, privileged observations, assisted initial states, and reward relabeling close to the claims they explain. State whether “seeds” means trained models or repeated evaluation episodes. Explain normalization when interpreting score differences.

Put full architectures, optimizer inventories, secondary sweeps, and lengthy task specifications in the appendix. Retain a detail in the main text when removing it would change what the reader thinks the method does or what an experiment demonstrates.

## Use direct academic English

Prefer “relabel,” “predict,” “penalize,” “plan,” “condition on,” and “learn from.” Use established terminology; avoid decorative expressions such as “holistic decision intelligence,” “unprecedented policy prowess,” or “seamlessly synergizes.” Give each paragraph one point and end with what the evidence means.

Sell the consequence with a specific scope: fewer real interactions on the tested tasks, competitive offline control with a small modification, or planning made possible by a trajectory model. Separate the observed finding from its possible explanation. State the result confidently without converting a finite experiment into a universal guarantee.

## Resources

- [Writing playbook](references/playbook.md): openings, experiment narratives, and sentence-level choices.
- [Worked example](references/worked-example.md): a manuscript from fictional supplied results.
- [Ten source papers](references/corpus.md) and [BibTeX](references/references.bib).

Borrow argumentative moves, not source sentences. Cite source papers in a manuscript when scientifically relevant. Use representation or generative-model guidance when reusable features or synthesis, rather than decision-making, carries the contribution.
