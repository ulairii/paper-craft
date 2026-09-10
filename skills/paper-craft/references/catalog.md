# Writing skill catalog

Use this catalog to choose guidance from the paper's central contribution. Only available skills appear below. Paths are relative to this file; keep the sibling skill folders together when installing the collection.

## Available specialists

| Skill | Conference | Research area | Suitable tasks | Entry point |
|---|---|---|---|---|
| `paper-craft-iclr-reasoning` | ICLR | LLM reasoning and test-time compute | Full drafts; story and contribution framing; titles and abstracts; introductions and methods; experiment narratives; prose revision | [SKILL.md](../../paper-craft-iclr-reasoning/SKILL.md) |
| `paper-craft-cvpr-detection` | CVPR | Object detection | Full drafts; localization, representation, assignment, efficiency, and convergence stories; method and result explanation; prose revision | [SKILL.md](../../paper-craft-cvpr-detection/SKILL.md) |
| `paper-craft-cvpr-segmentation` | CVPR | Semantic, instance, and panoptic segmentation | Full drafts; context and boundary stories; task unification; method and experiment prose; revision | [SKILL.md](../../paper-craft-cvpr-segmentation/SKILL.md) |
| `paper-craft-cvpr-3d` | CVPR | Point-cloud and 3D perception | Full drafts; geometric representations; LiDAR detection; pretraining and scaling narratives; result explanation; revision | [SKILL.md](../../paper-craft-cvpr-3d/SKILL.md) |
| `paper-craft-iccv-detection` | ICCV | Object detection | Full drafts; simplification, alignment, loss and matching stories; semi-supervised detection; method and result prose; revision | [SKILL.md](../../paper-craft-iccv-detection/SKILL.md) |
| `paper-craft-iccv-segmentation` | ICCV | Semantic, instance, open-vocabulary, and promptable segmentation | Full drafts; spatial refinement, context, mask representations, transfer and prompt narratives; revision | [SKILL.md](../../paper-craft-iccv-segmentation/SKILL.md) |
| `paper-craft-iccv-3d` | ICCV | Point clouds, geometric detection, registration, and camera BEV | Full drafts; observation and representation stories; geometric aggregation; efficiency tradeoffs; experiment prose; revision | [SKILL.md](../../paper-craft-iccv-3d/SKILL.md) |

### CVPR: object detection

**Select when the contribution concerns:** box detection, region or query representations, feature pyramids for detectors, positive-sample assignment, localization refinement, detector efficiency, or detector training convergence.

**Useful signals in the material:** box AP and overlap-dependent results; region proposals; sparse or dense detection heads; matching and assignment; detector accuracy–speed curves. Select based on the proposed change, not the presence of COCO alone.

**Distinguish nearby work:** mask prediction and pixel labeling belong to segmentation when they carry the contribution. Point-cloud geometry and 3D box prediction belong to 3D perception. An LLM that happens to describe objects is not automatically a detector paper.

**Source collection:** [10 accepted CVPR papers from 2014–2022](../../paper-craft-cvpr-detection/references/corpus.md), with [BibTeX](../../paper-craft-cvpr-detection/references/references.bib).

### CVPR: segmentation

**Select when the contribution concerns:** semantic pixel labeling, instance masks, panoptic grouping, mask boundaries, scene context for segmentation, or unifying segmentation tasks.

**Useful signals in the material:** mask quality and boundary results; feature refinement for dense labels; context-dependent category confusion; task-conditioned masks; joint semantic, instance, and panoptic predictions.

**Distinguish nearby work:** use detection as primary when box localization or detector assignment carries the contribution and masks are secondary. Use segmentation as primary when mask representation, boundary quality, or grouping semantics is the insight. Point sampling in a 2D mask is different from 3D point-cloud perception.

**Source collection:** [10 accepted CVPR papers from 2015–2023](../../paper-craft-cvpr-segmentation/references/corpus.md), with [BibTeX](../../paper-craft-cvpr-segmentation/references/references.bib).

### CVPR: 3D perception

**Select when the contribution concerns:** point-cloud representations, LiDAR-based 3D detection, point operators, voxel or pillar encoding, geometric sampling, point-cloud pretraining, or scalable 3D backbones.

**Useful signals in the material:** sparse sensor returns, coordinate transformations, point retention, voxel-to-point aggregation, 3D proposals, geometric tokenization, or neighborhood and receptive-field scaling.

**Distinguish nearby work:** prefer this specialist over 2D detection or segmentation when geometry or the point-cloud representation carries the contribution, even if the output is boxes or masks. A rendering, reconstruction, or camera-only depth paper is outside this corpus's dedicated coverage; use general guidance and borrow a particular lesson only when it fits.

**Source collection:** [10 accepted CVPR papers from 2017–2024](../../paper-craft-cvpr-3d/references/corpus.md), with [BibTeX](../../paper-craft-cvpr-3d/references/references.bib).

### ICCV: object detection

**Select when the contribution concerns:** detector training or inference, spatial alignment, adaptive feature sampling, dense losses, anchor-free prediction, classification–localization agreement, semi-supervised box detection, or transformer matching and supervision.

**Useful signals in the material:** box AP, assignment coverage, confidence versus overlap, pseudo-box reliability, per-layer matching, positive training queries, and shared detector computation.

**Distinguish nearby work:** select the ICCV corpus when ICCV is the target; related CVPR lessons can supplement a particular mechanism. Use a segmentation specialist when masks or pixel grouping carry the central contribution, and a 3D specialist when point-cloud geometry carries it. A mask experiment alone does not determine the primary topic.

**Source collection:** [10 accepted ICCV papers from 2015–2023](../../paper-craft-iccv-detection/references/corpus.md), with [BibTeX](../../paper-craft-iccv-detection/references/references.bib).

### ICCV: segmentation

**Select when the contribution concerns:** spatial mask refinement, structured pixel prediction, efficient context for segmentation, query-based instance masks, transformer semantic segmentation, open-vocabulary region classification, or promptable mask prediction.

**Useful signals in the material:** mask or boundary quality, pixel relationships, class embeddings, mask proposal coverage, seen-versus-novel segmentation, prompt ambiguity, and segmentation transfer.

**Distinguish nearby work:** use detection when box assignment or localization is the main contribution. Use this specialist for 2D mask representations and task interfaces, including open-vocabulary masks; a general vision-language representation paper needs its own representation-learning guidance. Point-cloud geometry belongs to 3D perception.

**Source collection:** [10 accepted ICCV papers from 2015–2023](../../paper-craft-iccv-segmentation/references/corpus.md), with [BibTeX](../../paper-craft-iccv-segmentation/references/references.bib).

### ICCV: 3D perception

**Select when the contribution concerns:** point-cloud detection or recognition, rigid registration, real-scan benchmarks, point or voxel attention, range-view LiDAR detection, superpoint segmentation, or sparse camera-based BEV detection.

**Useful signals in the material:** surface-to-center geometry, cross-cloud correspondence, incomplete observations, metric neighborhoods, range-dependent scale, region-level prediction, and temporal projection into camera views.

**Distinguish nearby work:** use this specialist when 3D geometry or sensor representation carries the contribution, even if the outputs are boxes or labels. Use 2D detection or segmentation for contributions primarily about image-space boxes or masks. Rendering, reconstruction, and general depth estimation are outside this corpus's dedicated coverage.

**Source collection:** [10 accepted ICCV papers from 2019–2023](../../paper-craft-iccv-3d/references/corpus.md), with [BibTeX](../../paper-craft-iccv-3d/references/references.bib).

### ICLR: LLM reasoning and test-time compute

**Select when the contribution concerns:** reasoning-path sampling and aggregation, chain-of-thought, self-consistency, problem decomposition, self-correction, process or outcome supervision for reasoning, reasoning verifiers, search over reasoning paths, or allocation of inference computation.

**Useful signals in the material:** comparisons of sampling and search; best-of-N answer selection; process rewards; revisions across attempts; sequential versus parallel inference; analysis of reasoning behavior. These are clues, not a keyword score.

**Distinguish nearby work:** using an LLM does not by itself make a paper a reasoning paper. Representation learning, retrieval systems, visual generation, general model compression, and security attacks need their own guidance when those topics carry the main contribution. Mentioning GSM8K or a verifier in one experiment is not enough to override that contribution.

**Source collection:** [10 accepted ICLR papers from 2023–2025](../../paper-craft-iclr-reasoning/references/corpus.md).

## How selection should work

| Request and material | Appropriate behavior |
|---|---|
| “Draft my CVPR submission,” with point sampling and LiDAR box results | Load the CVPR 3D perception skill and write the draft. |
| “Draft my CVPR submission,” with detector assignment and box-localization results | Load the CVPR detection skill and write the draft. |
| “Draft my ICLR submission,” with a method for allocating compute between search and revision | Load the ICLR reasoning skill and write the draft. |
| “Draft my ICLR submission,” with a contrastive image representation method | Use general guidance; the available reasoning skill does not match this topic. |
| “Draft my NeurIPS submission,” with process-reward reasoning experiments | Use reasoning lessons as a cross-conference reference while retaining NeurIPS as the target. |
| “Draft my ICLR submission,” with no identified method or results | Ask for the material needed to write; do not infer reasoning from the conference alone. |

## Adding a specialist

Create a sibling folder under `skills/` with a practical `SKILL.md` and its own source references. Each released specialist needs at least 10 accepted papers from its conference and research area.

Add a table row and a concise selection profile here: conference, topic, suitable tasks, entry point, positive topic signals, and distinctions from overlapping skills. The profile should describe the contribution that makes a paper belong, not list every benchmark in the field. Link its source collection.

When two skills overlap, explain the distinction in their profiles so the entry point can choose a primary skill. Keep planned skills out of this catalog until their files and writing lessons are available. Domain skills live in directories on the same Git branch; the entry point does not switch branches to discover them.
