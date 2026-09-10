---
name: paper-craft-icml-generative
description: Write and revise ICML generative-model papers from methods and existing experiments. Distills ten accepted papers on variational models, flows, GANs, diffusion, consistency, conditional generation, new modalities, and sampling into story, method, and results-writing guidance.
---

# Write an ICML generative-model paper

Write the requested manuscript from the author's material. A full-draft request calls for connected section prose, using short factual placeholders where needed. Identify what the work makes easier to model, learn, generate, or control.

## Choose the contribution before choosing the outline

| Contribution | Story to develop | Sources |
|---|---|---|
| Probabilistic learning or inference | Which approximation blocks useful learning, and how is it changed? | [Stochastic Backpropagation](references/papers/P01.md), [Normalizing Flows](references/papers/P02.md) |
| Training objective | Why does the existing objective give a poor signal? | [WGAN](references/papers/P03.md), [Improved DDPM](references/papers/P04.md) |
| Conditional generation | What does the user specify, and how well does the output follow it? | [GLIDE](references/papers/P05.md), [AudioLDM](references/papers/P08.md) |
| Fast generation | Which sequential work is replaced, and which useful capability is retained? | [Consistency Models](references/papers/P06.md), [DSNO](references/papers/P10.md) |
| New data type | What property of the data requires an adaptation? | [TabDDPM](references/papers/P07.md), [AudioLDM](references/papers/P08.md) |
| Composition and reuse | Why does combining good models fail, and what repairs it? | [Reduce, Reuse, Recycle](references/papers/P09.md) |

Lead with a concrete difficulty: restrictive posteriors, an uninformative loss, expensive sequential sampling, mixed feature types, missing paired data, or incompatible sampling dynamics. “Generative models have achieved remarkable success” does little work unless the next sentence identifies the unresolved problem.

## Explain what the model represents

Distinguish the data distribution, approximate posterior, score, energy, trajectory, conditioning embedding, and generated latent. Use only the objects needed for the contribution. Follow one example from input or noise through the important operation to the output.

Explain an equation through its purpose. A Jacobian accounts for a density transformation; a critic supplies a learning signal; a variance parameter changes reverse transitions; a boundary condition prevents an uninformative solution; an aligned embedding transfers conditioning across modalities. Put the full derivation after the reader understands the idea.

For an adaptation, identify the nontrivial change. Numerical and categorical columns need different corruption processes. A pretrained language–audio space separates alignment from synthesis. Temporal operator learning predicts a trajectory jointly. Naming a familiar model in a new domain is not the whole contribution.

## Let each experiment advance the argument

Begin with the result that answers the opening question, then explain it with the most revealing supplied comparisons. A toy distribution can clarify a mathematical failure before a real-data experiment tests usefulness. A shared teacher can isolate a distillation change. A quality–cost curve can show the regime where a sampler matters.

Treat likelihood, perceptual quality, diversity, condition agreement, downstream utility, and computation as different outcomes. If they disagree, explain the disagreement instead of calling everything “performance.” Strong papers often contribute a better tradeoff rather than simultaneous improvement on every metric.

Use existing evidence to write now. If a crucial comparison is unavailable, narrow the claim or insert a short placeholder; do not replace the manuscript task with an endless experiment checklist.

## Keep the conditions that change the meaning

State the conditioning and adaptation protocol, teacher dependence, generated representation, and relevant costs. Distillation and direct training are different settings. One model evaluation is not a fixed runtime. Audio-only generator training can rely on a text-supervised pretrained encoder. A conditional editing result may require fine-tuning or several sampling steps.

Keep these facts near their scientific use. Move long schedules, prompt lists, architecture inventories, and derivations into setup or supporting material. An important detail belongs once in the right place, not in repeated verification paragraphs.

## Sell what becomes possible in clear English

Prefer “enrich the posterior,” “reduce sampling steps,” “retain coverage,” “follow the text condition,” “model mixed feature types,” and “compose existing models.” Avoid decorative language such as “holistic distributional synergy” or “unprecedented universal generative intelligence.”

Name the useful consequence instead of relying on “novel,” “effective,” or “powerful.” Attribute known tools and concurrent work. A new combination can be valuable because the paper explains why it works.

Use theory and observations at their proper scope. Approximation capacity does not establish exact finite-model learning. A diagnostic of disclosure risk is not a privacy guarantee. A lower critic loss is not a universal quality metric. State a supported result confidently, and explain a boundary when it helps the reader understand the contribution.

## Resources

- [Writing playbook](references/playbook.md): argument structures, explanatory experiments, and detail placement.
- [Worked example](references/worked-example.md): passages for a fast conditional-generation paper.
- [Ten source papers](references/corpus.md) and [BibTeX](references/references.bib).

Borrow writing logic, not source sentences. Cite these papers when scientifically relevant to the manuscript; the corpus is not a mandatory citation list.
