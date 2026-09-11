# Choosing which answers to revise

**Same evidence. A more coherent argument.**

An authored editing example using fictional research material. Both abstracts were written for this demonstration; they are not recorded outputs from a model comparison.

## The abstract

### Before — the method and results are listed

> We study uncertainty-aware revision for improving the reasoning accuracy of large language models under a fixed generation budget. The approach consists of initial answer generation, uncertainty estimation, and selective revision. Answers with high uncertainty receive additional revision, while confident answers are retained. We evaluate the approach on a held-out reasoning set using the same model and an average budget of 2,000 generated tokens per problem. Uncertainty-directed revision achieves 66% accuracy, compared with 62% for uniform revision and 58% for initial answers alone. On an easy subset, both revision strategies achieve 88% accuracy. The evaluation shows that uncertainty-directed revision improves overall accuracy over uniform revision under the specified budget. These findings support further investigation of uncertainty-aware methods for language model reasoning.

### After — the comparison carries the contribution

> Revising a language model's answers consumes tokens that could be spent on other problems. Under a fixed generation budget, a revision strategy must therefore decide which answers deserve another attempt. We study uncertainty as a signal for this decision: retain confident answers and direct the remaining budget toward revising uncertain ones. On a held-out reasoning set, this allocation reaches 66% accuracy, compared with 62% when revision effort is distributed uniformly, at the same average budget of 2,000 generated tokens per problem, including uncertainty estimation. The four-percentage-point gain comes from changing how revision effort is allocated while keeping the model and token budget fixed. This comparison makes the allocation of revision effort a concrete design choice for reasoning under a budget.

The revision gives the reader one connected argument: **revision has an opportunity cost → allocation is the decision → uncertainty supplies a rule → the matched-budget comparison tests that rule.** It improves the presentation of the supplied contribution without claiming a new algorithm or a broader empirical result.

## Why the revision works

| Editorial choice | What it accomplishes |
|:---|:---|
| Start with the cost of another attempt | Establishes a concrete tension without a generic introduction to LLMs. |
| Make allocation the central decision | Gives initial generation, uncertainty estimation, and revision a shared purpose. |
| Describe the action in ordinary words | “Retain” and “direct” tell the reader what the method does. |
| Select the 66% versus 62% comparison | Isolates the result most relevant to the story: how to distribute revision effort. |
| Keep the budget beside the result | Makes the gain interpretable and makes clear that uncertainty estimation is included. |
| End with the implication of the comparison | Leaves the reader with a design choice rather than a generic effectiveness claim or future-work sentence. |

The first version is deliberately plausible: its facts are useful and its sentences are readable. The revision changes their hierarchy and connections, rather than making the first version look worse through exaggerated jargon.

## What belongs outside this abstract

**The initial-answer baseline belongs in the results section.** It establishes the benefit of adding revision. The uniform-revision baseline asks the more specific question this abstract centers on: whether the allocation of that effort matters.

**The easy-subset tie belongs in the analysis.** It shows that the overall advantage is not present on every subset. The abstract reports an aggregate result on one held-out set; it does not claim that every problem benefits. If differences across difficulty levels were the paper's central discovery, that result would deserve abstract space instead.

**The mechanism remains a question for the paper.** These results support the comparison between the two supplied allocation strategies. They do not establish that uncertainty identifies correctable errors, that its ranking is optimal, or that it beats every other routing signal. The abstract avoids those claims without appending a list of unperformed experiments.

## The shared research material

**Target:** ICLR. **Topic:** LLM reasoning and test-time compute.

**Method:** generate initial answers, estimate uncertainty, retain confident answers, and allocate the remaining generation budget to revising uncertain answers. Allocation operates across a set of problems, so individual problems need not receive the same number of tokens.

**Evaluation:** one fictional held-out reasoning set, one fixed model, and an average generation budget of 2,000 tokens per problem for each strategy. Uncertainty estimation is included in the directed strategy's budget. This is a token-budget comparison; no latency or FLOP measurements are supplied.

| Strategy | Overall accuracy | Accuracy on the easy subset |
|:---|---:|---:|
| Initial answers only | 58% | Not supplied |
| Uniform revision | 62% | 88% |
| Uncertainty-directed revision | 66% | 88% |

The material does not specify the model, dataset, uncertainty estimator, or statistical variability. There is no second dataset or component ablation. A real manuscript would need those method and evaluation details. The fictional values are held fixed across the two versions; the editing demonstration supplies no evidence about paper-craft's performance.

## Try it on your own work

Provide a target conference, a short method description, and a result table. Include what the important comparisons hold fixed. Then ask:

```text
Read ~/.local/share/paper-craft/skills/paper-craft/SKILL.md.

Write an abstract from the material below. Find the central research
question, explain the method as a response to it, and select the result
that best establishes the contribution. Preserve the supplied facts.
After the abstract, briefly explain what you left out and why.

[Target conference, method, and results]
```

Use your actual installation path. To compare with a plain request, use two fresh sessions with the same model, settings, material, and writing instructions; omit only the skill-loading instruction in one session. Keep the original outputs when sharing a comparison.

## Source lessons

The [ICLR reasoning specialist](../skills/paper-craft-iclr-reasoning/SKILL.md) draws on [ten accepted ICLR papers](../skills/paper-craft-iclr-reasoning/references/corpus.md). Its [writing playbook](../skills/paper-craft-iclr-reasoning/references/writing-playbook.md) explains how an abstract compresses an argument; its [experiment playbook](../skills/paper-craft-iclr-reasoning/references/experiment-playbook.md) explains how to select a comparison and interpret its consequence. These are the writing lessons applied here, not sources for the fictional method or results.
