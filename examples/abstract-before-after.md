# Same results, a clearer abstract

This is an **authored writing demonstration with fictional results**, not a benchmark or a recorded comparison between models. Both versions below were written for this example. They show the editorial choices paper-craft teaches; they do not measure the effect of installing a skill.

## The material

**Target:** ICLR. **Topic:** LLM reasoning and test-time compute.

- Method: generate an initial answer, estimate uncertainty, and spend the remaining token budget revising uncertain answers. Keep confident answers unchanged.
- Evaluation: one fictional held-out reasoning set, with the same model and an average budget of 2,000 generated tokens per problem for every strategy. Uncertainty estimation is included in this budget.
- Accuracy: initial answers only, 58%; uniform revision, 62%; uncertainty-directed revision, 66%.
- On a separately identified easy subset, uniform and directed revision both reach 88%.
- No latency measurements, second dataset, or component ablations are supplied. The results do not establish why the method works or whether the uncertainty estimator is better than other routing rules.

## Before: the contribution is buried

> We present a novel and effective framework for improving large language model reasoning through uncertainty-aware adaptive refinement. The framework integrates answer generation, uncertainty estimation, and iterative revision to enhance performance under a fixed computational budget. On a held-out reasoning set, the proposed framework achieves 66% accuracy, compared with 62% for uniform revision and 58% for initial answers, at an average budget of 2,000 generated tokens per problem. Both revision strategies achieve 88% accuracy on the easy subset. These results demonstrate the effectiveness of our framework for reasoning.

## After: the result explains the story

> Under a fixed generation budget, which answers should a reasoning model revise? We use uncertainty to direct revision toward answers that may benefit from further computation, while retaining confident answers. On a held-out reasoning set, this strategy reaches 66% accuracy, compared with 62% for uniform revision and 58% for initial answers, with each strategy using an average of 2,000 generated tokens per problem. Both revision strategies reach 88% on the easy subset, so the aggregate advantage does not extend to that subset. The results support allocating revision effort selectively in this setting; they leave open whether uncertainty is more useful than other allocation rules.

## What changed

| Writing choice | Why it helps |
|:---|:---|
| Open with a decision under a constraint | The reader understands the problem before meeting the components. |
| Explain uncertainty by the action it changes | The method has a purpose beyond being a named framework. |
| Put the comparison beside its budget | The accuracy difference has an interpretable context. |
| Give the easy-subset result a role | An exception sharpens the scope of the finding. |
| State what remains unresolved | The draft distinguishes an observed gain from an explanation of its cause. |

The revision also removes unsupported novelty language. A real submission would need the dataset, evaluation protocol, uncertainty rule, and relevant prior work to be specified.

## Try the comparison yourself

Use the material above, or replace it with your own. For an actual comparison, use two fresh assistant sessions with the same model and settings.

**Session A — plain request:**

```text
Write a research paper abstract from the following material.
Preserve the results and do not invent missing facts.

[Paste the material]
```

**Session B — with paper-craft:**

```text
Read ~/.local/share/paper-craft/skills/paper-craft/SKILL.md.
Write a research paper abstract from the following material.
Preserve the results and do not invent missing facts.

[Paste the same material]
```

Use your actual installation path. Compare whether the drafts explain the problem, connect the method to it, and interpret the same evidence. Keep both original outputs if you share the comparison; one example cannot establish a general performance advantage.

## Explore the underlying lessons

The [ICLR reasoning specialist](../skills/paper-craft-iclr-reasoning/SKILL.md) draws on [ten accepted papers](../skills/paper-craft-iclr-reasoning/references/corpus.md). Its [writing playbook](../skills/paper-craft-iclr-reasoning/references/writing-playbook.md) and [experiment playbook](../skills/paper-craft-iclr-reasoning/references/experiment-playbook.md) develop these principles. The fictional method above is not attributed to any one source paper.
