# paper-craft

**Research writing skills learned from strong papers.**

Turn an idea, rough draft, or set of results into a paper with a clear story. paper-craft distills how published papers introduce a problem, make an insight memorable, organize experiments, explain findings, and write precise, natural English.

Each skill focuses on a **conference and research area**, drawing on at least **10 papers accepted at that conference**. The lessons come with paper references and concrete writing examples.

## What it helps you write

- **The story:** find the insight that makes the work worth reading.
- **Titles and abstracts:** make the contribution recognizable without inflated language.
- **Introductions and methods:** connect the problem, intuition, and design so readers can follow the idea.
- **Experiments and results:** organize around questions and explain what the findings mean.
- **Better sentences:** replace awkward words, vague claims, and overloaded paragraphs with clear prose.

## Get started

Clone the repository:

```bash
git clone https://github.com/ulairii/paper-craft.git
```

Give your assistant the skill file and the material you want to work on:

```text
Read paper-craft/skills/paper-craft-iclr-reasoning/SKILL.md.

Help me rewrite the introduction below. Find the central insight,
make the motivation flow into the method, and use plain academic English.
Return the rewritten introduction with a short explanation of the main changes.

[Paste your draft here]
```

Use the path to your clone if you are working elsewhere. If your assistant supports installing skills from folders, copy the entire `skills/paper-craft-iclr-reasoning/` directory into its configured skills location, including `references/`.

The skill is a collection of Markdown instructions and reading notes. Using it requires no paper downloads, Python environment, API keys, or access to the author's machines.

## Available skills

| Skill | Source papers | Focus |
|---|---|---|
| [ICLR · LLM reasoning and test-time compute](skills/paper-craft-iclr-reasoning/SKILL.md) | [10 ICLR papers, 2023–2025](skills/paper-craft-iclr-reasoning/references/corpus.md) | Sampling, decomposition, verification, self-correction, search, and compute allocation |

## A small example

An abstract opening that hides the idea:

> We propose a novel and effective two-stage reinforcement learning framework to enhance the self-correction capabilities of large language models.

A more informative opening:

> A model that revises its answer must learn both when to change it and what to change. We train these behaviors in two stages: first improving revision, then jointly optimizing the initial answer and its correction.

The second version gives the reader a problem and a design rationale before introducing the machinery. This is an original writing illustration inspired by SCoRe, not a quotation from the paper. The [full worked example](skills/paper-craft-iclr-reasoning/references/worked-example.md) develops the introduction, method, and experiment story.

## Explore the writing lessons

- [Story and section structure](skills/paper-craft-iclr-reasoning/references/writing-playbook.md)
- [Plain English, terminology, and paragraph flow](skills/paper-craft-iclr-reasoning/references/claim-language.md)
- [Experiments that tell the story](skills/paper-craft-iclr-reasoning/references/experiment-playbook.md)
- [Example requests](examples/prompts.md)
- [Paper-by-paper reading notes](skills/paper-craft-iclr-reasoning/references/corpus.md)

## Contribute a skill

Choose a conference and a focused research area. Read at least 10 accepted papers from that conference and distill their writing choices: how the story starts, where the insight appears, how experiments advance the argument, and which details help the reader. Include source locations and original before/after examples, rather than a list of generic writing tips.

Keep the `SKILL.md` practical and put deeper analysis in `references/`. Explain what makes the papers persuasive; acceptance alone cannot establish which writing choices caused it.

Future coverage is intended for ICLR, ICML, and NeurIPS; CVPR, ICCV, and ECCV; and S&P, USENIX Security, CCS, and NDSS, with skills for individual research areas. Currently, only the ICLR skill above is available.
