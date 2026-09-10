---
name: paper-craft-neurips-representation
description: Draft and revise NeurIPS representation-learning papers from methods and existing experiments. Distills ten accepted papers on self-supervision, contrastive learning, graph representations, local features, label efficiency, and transfer into clear contribution framing and experimental narratives.
---

# Write a NeurIPS representation-learning paper

Produce the manuscript the author asks for. When asked for a full draft, write connected section prose, using short placeholders for missing facts. Find the most useful learning insight in the supplied results and make it the organizing idea.

## Choose a story that fits the work

| Contribution | Organizing question | Source examples |
|---|---|---|
| A simpler learning objective | Which familiar component can be removed, or which small change matters? | [BYOL](references/papers/P02.md), [SupCon](references/papers/P05.md), [Debiased Contrastive Learning](references/papers/P07.md) |
| A stronger recipe | Why do these choices work together? | [AMDIM](references/papers/P01.md), [SwAV](references/papers/P03.md) |
| Better use of labels or model capacity | What becomes possible with the available supervision? | [SimCLRv2](references/papers/P04.md) |
| Appropriate invariance | Which changes preserve the task, and which remove useful information? | [InfoMin](references/papers/P06.md), [GraphCL](references/papers/P09.md) |
| An explanation of transfer | What familiar explanation fails to account for the observations? | [Transfer analysis](references/papers/P08.md) |
| Local and global features | What useful balance does the method offer? | [VICRegL](references/papers/P10.md) |

Do not force every contribution into a new architecture or highest-score narrative. A simple objective, a useful recipe, an explanatory finding, or a better tradeoff can each support a strong paper.

## Make the opening earn the method

Start with a specific unresolved issue. Explain its consequence for learning or use, then introduce the observation or idea that changes the situation. State the contribution with concrete nouns and verbs: which samples are compared, which features are predicted, which information is preserved, or which stage becomes more effective.

Give inherited components credit. For an adaptation, identify the domain-specific obstacle. For a recipe, explain the complementary jobs of the components. For a discovery, let each finding motivate the next question. A short example often communicates the issue more effectively than a broad claim about the importance of representation learning.

## Explain the learning signal before the notation

Describe the inputs, how positives or targets are formed, and what the network learns from them. Distinguish encoder features from projected embeddings and global summaries from local feature maps. State what is retained for downstream use.

Introduce equations when they make the change precise. A difference in positive sets, averaging, matching, or target updates can deserve a central equation even when the overall pipeline is familiar. Explain the job of each term before presenting implementation constants.

For an analytical paper, connect observation, simplified setting, explanation, and testable consequence. State the assumptions needed to understand the result; place extended derivations in supporting material.

## Turn existing experiments into a connected account

Choose the leading result to match the contribution: a controlled objective comparison, a label-efficiency curve, a local/global tradeoff, or a revealing transfer intervention. Follow with the experiment that explains the result, then the evidence that establishes its useful scope.

Give each paragraph a finding, the comparison that makes it informative, and the implication for the central idea. Explain differences among linear probes, fine-tuning, dense prediction, and training loss when they reveal something about the features. Avoid a table-by-table recital of scores.

An interaction can be the story: stronger augmentation may help one task and erase useful signal in another. A tradeoff can be the contribution: a substantial dense-prediction gain may justify a small classification loss. Write these findings directly rather than burying them among exceptions.

## Keep the details that readers need at that point

Keep supervision, pretraining data, evaluation regime, feature layer, and comparison scale near the claims they define. In a multistage method, state which stage uses labels and which model is deployed. For efficiency, name the saved resource and the operating point.

Put full schedules, auxiliary benchmark tables, derivations, and secondary sweeps in setup or appendices. Retain a detail in the main narrative when it explains the learning behavior or changes the meaning of the result. Draft from available evidence; do not turn a writing request into an open-ended list of experiments to run.

## Use ordinary, precise English

Prefer “predict,” “match,” “retain,” “remove,” “adapt,” and “transfer.” Use established technical terms when useful, defining them once. Avoid unusual synonyms such as “semantemes” and decorative phrases such as “holistic representational synergy” or “unprecedented semantic prowess.”

Sell the strongest supported insight confidently. Say what the representation enables rather than calling it universally better. Distinguish a demonstrated capability from a proposed explanation. “Learns without negative pairs” can be a strong result even when the full reason it avoids collapse remains open.

## Resources

- [Writing playbook](references/playbook.md): narrative patterns and experimental interpretation.
- [Worked example](references/worked-example.md): manuscript prose from fictional supplied results.
- [Ten source papers](references/corpus.md) and [BibTeX](references/references.bib).

Borrow argumentative moves, not sentences. Cite source papers in a manuscript when scientifically relevant; this collection is not a mandatory related-work list. Use a generative or reinforcement-learning specialist when sample synthesis or policy learning carries the contribution.
