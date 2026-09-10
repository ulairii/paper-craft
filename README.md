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

Give your assistant the shared entry point and the material you want to work on:

```text
Read paper-craft/skills/paper-craft/SKILL.md.

I am submitting to ICLR. Write a full paper draft from my method and
existing experiment results. Find the central story, explain the important
comparisons, and use plain academic English.

[Paste your method and results, or provide their file paths]
```

Use the path to your clone if you are working elsewhere. The assistant reads your material, selects the appropriate conference-and-subfield skill, and writes the requested draft. You can also ask for a single section, an outline, or a sentence edit.

If your assistant supports installing skills from folders, copy **all folders inside `skills/` together** into its configured skills location, preserving their names and `references/` directories. Invoke the `paper-craft` entry point using your assistant's supported invocation method. The entry point uses relative paths to load the specialists; copying only its folder provides general guidance but omits the specialist content.

The skill is a collection of Markdown instructions and reading notes. Using it requires no paper downloads, Python environment, API keys, or access to the author's machines.

## One entry point, specialized writing lessons

[paper-craft](skills/paper-craft/SKILL.md) uses a [catalog](skills/paper-craft/references/catalog.md) to match the target conference, central research topic, and writing task. It infers the topic from the supplied work rather than asking you to choose a directory.

If the work spans several areas, it chooses one primary skill and draws on another only where useful. If no specialist fits, it continues with general writing guidance and briefly notes the coverage gap. An ICLR target alone does not cause every paper to be treated as LLM reasoning.

The entry point must be loaded or installed in your assistant; cloning a repository alone does not activate it.

### Available specialists

| Skill | Source papers | Focus |
|---|---|---|
| [ICLR · LLM reasoning and test-time compute](skills/paper-craft-iclr-reasoning/SKILL.md) | [10 ICLR papers, 2023–2025](skills/paper-craft-iclr-reasoning/references/corpus.md) | Sampling, decomposition, verification, self-correction, search, and compute allocation |
| [ICLR · Representation learning](skills/paper-craft-iclr-representation/SKILL.md) | [10 ICLR papers, 2019–2022](skills/paper-craft-iclr-representation/references/corpus.md) · [BibTeX](skills/paper-craft-iclr-representation/references/references.bib) | Information objectives, graphs, collapse, masked pretraining, local features, and language–image alignment |
| [CVPR · Object detection](skills/paper-craft-cvpr-detection/SKILL.md) | [10 CVPR papers, 2014–2022](skills/paper-craft-cvpr-detection/references/corpus.md) · [BibTeX](skills/paper-craft-cvpr-detection/references/references.bib) | Localization, feature pyramids, assignment, sparse proposals, efficiency, and convergence |
| [CVPR · Segmentation](skills/paper-craft-cvpr-segmentation/SKILL.md) | [10 CVPR papers, 2015–2023](skills/paper-craft-cvpr-segmentation/references/corpus.md) · [BibTeX](skills/paper-craft-cvpr-segmentation/references/references.bib) | Dense prediction, context, boundaries, refinement, and task unification |
| [CVPR · 3D perception](skills/paper-craft-cvpr-3d/SKILL.md) | [10 CVPR papers, 2017–2024](skills/paper-craft-cvpr-3d/references/corpus.md) · [BibTeX](skills/paper-craft-cvpr-3d/references/references.bib) | Point-cloud geometry, LiDAR detection, representations, pretraining, and scaling |
| [ICCV · Object detection](skills/paper-craft-iccv-detection/SKILL.md) | [10 ICCV papers, 2015–2023](skills/paper-craft-iccv-detection/references/corpus.md) · [BibTeX](skills/paper-craft-iccv-detection/references/references.bib) | Spatial alignment, dense losses, anchor-free prediction, pseudo labels, and transformer training |
| [ICCV · Segmentation](skills/paper-craft-iccv-segmentation/SKILL.md) | [10 ICCV papers, 2015–2023](skills/paper-craft-iccv-segmentation/references/corpus.md) · [BibTeX](skills/paper-craft-iccv-segmentation/references/references.bib) | Spatial refinement, efficient context, query masks, open-vocabulary transfer, and prompting |
| [ICCV · 3D perception](skills/paper-craft-iccv-3d/SKILL.md) | [10 ICCV papers, 2019–2023](skills/paper-craft-iccv-3d/references/corpus.md) · [BibTeX](skills/paper-craft-iccv-3d/references/references.bib) | Geometric detection, registration, real scans, sparse representations, and camera BEV |
| [ECCV · Object detection](skills/paper-craft-eccv-detection/SKILL.md) | [10 ECCV papers, 2018–2024](skills/paper-craft-eccv-detection/references/corpus.md) · [BibTeX](skills/paper-craft-eccv-detection/references/references.bib) | Output reformulation, adaptive training, precise boxes, semi-supervised and open-vocabulary learning |
| [ECCV · Segmentation](skills/paper-craft-eccv-segmentation/SKILL.md) | [10 ECCV papers, 2018–2024](skills/paper-craft-eccv-segmentation/references/corpus.md) · [BibTeX](skills/paper-craft-eccv-segmentation/references/references.bib) | Spatial detail, context units, instance representations, heterogeneous tasks, and open-vocabulary interaction |
| [ECCV · 3D perception](skills/paper-craft-eccv-3d/SKILL.md) | [10 ECCV papers, 2018–2024](skills/paper-craft-eccv-3d/references/corpus.md) · [BibTeX](skills/paper-craft-eccv-3d/references/references.bib) | Point operators, registration, pretraining, geometric detection, camera fusion, and sparse attention |
| [ICML · Representation learning](skills/paper-craft-icml-representation/SKILL.md) | [10 ICML papers, 2020–2023](skills/paper-craft-icml-representation/references/corpus.md) · [BibTeX](skills/paper-craft-icml-representation/references/references.bib) | Contrastive learning, language–image transfer, data efficiency, identifiability, robustness, and dynamics |
| [ICML · Generative models](skills/paper-craft-icml-generative/SKILL.md) | [10 ICML papers, 2014–2023](skills/paper-craft-icml-generative/references/corpus.md) · [BibTeX](skills/paper-craft-icml-generative/references/references.bib) | Variational models, flows, GANs, diffusion, consistency, conditioning, new modalities, and sampling |
| [ICML · Reinforcement learning](skills/paper-craft-icml-rl/SKILL.md) | [10 ICML papers, 2015–2022](skills/paper-craft-icml-rl/references/corpus.md) · [BibTeX](skills/paper-craft-icml-rl/references/references.bib) | Policy optimization, value learning, offline RL, visual control, replay, planning, and adaptation |

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

Add the new folder alongside the existing skills and register it in the [catalog](skills/paper-craft/references/catalog.md), including its conference, topic signals, supported writing tasks, and distinctions from neighboring topics. Keep specialist directories together on the same Git branch. Users continue to call `paper-craft` as the collection grows.

Future coverage is intended for ICLR, ICML, and NeurIPS; CVPR, ICCV, and ECCV; and S&P, USENIX Security, CCS, and NDSS, with skills for individual research areas. Available specialists are listed above; the catalog contains only usable skills with completed writing lessons.
