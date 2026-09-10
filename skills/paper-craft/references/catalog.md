# Writing skill catalog

Use this catalog to choose guidance from the paper's central contribution. Only available skills appear below. Paths are relative to this file; keep the sibling skill folders together when installing the collection.

## Available specialists

| Skill | Conference | Research area | Suitable tasks | Entry point |
|---|---|---|---|---|
| `paper-craft-iclr-reasoning` | ICLR | LLM reasoning and test-time compute | Full drafts; story and contribution framing; titles and abstracts; introductions and methods; experiment narratives; prose revision | [SKILL.md](../../paper-craft-iclr-reasoning/SKILL.md) |

### ICLR: LLM reasoning and test-time compute

**Select when the contribution concerns:** reasoning-path sampling and aggregation, chain-of-thought, self-consistency, problem decomposition, self-correction, process or outcome supervision for reasoning, reasoning verifiers, search over reasoning paths, or allocation of inference computation.

**Useful signals in the material:** comparisons of sampling and search; best-of-N answer selection; process rewards; revisions across attempts; sequential versus parallel inference; analysis of reasoning behavior. These are clues, not a keyword score.

**Distinguish nearby work:** using an LLM does not by itself make a paper a reasoning paper. Representation learning, retrieval systems, visual generation, general model compression, and security attacks need their own guidance when those topics carry the main contribution. Mentioning GSM8K or a verifier in one experiment is not enough to override that contribution.

**Source collection:** [10 accepted ICLR papers from 2023–2025](../../paper-craft-iclr-reasoning/references/corpus.md).

## How selection should work

| Request and material | Appropriate behavior |
|---|---|
| “Draft my ICLR submission,” with a method for allocating compute between search and revision | Load the ICLR reasoning skill and write the draft. |
| “Draft my ICLR submission,” with a contrastive image representation method | Use general guidance; the available reasoning skill does not match this topic. |
| “Draft my NeurIPS submission,” with process-reward reasoning experiments | Use reasoning lessons as a cross-conference reference while retaining NeurIPS as the target. |
| “Draft my ICLR submission,” with no identified method or results | Ask for the material needed to write; do not infer reasoning from the conference alone. |

## Adding a specialist

Create a sibling folder under `skills/` with a practical `SKILL.md` and its own source references. Each released specialist needs at least 10 accepted papers from its conference and research area.

Add a table row and a concise selection profile here: conference, topic, suitable tasks, entry point, positive topic signals, and distinctions from overlapping skills. The profile should describe the contribution that makes a paper belong, not list every benchmark in the field. Link its source collection.

When two skills overlap, explain the distinction in their profiles so the entry point can choose a primary skill. Keep planned skills out of this catalog until their files and writing lessons are available. Domain skills live in directories on the same Git branch; the entry point does not switch branches to discover them.
