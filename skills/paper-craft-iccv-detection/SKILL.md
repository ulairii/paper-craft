---
name: paper-craft-iccv-detection
description: Write and revise ICCV object detection papers from existing results. Uses ten accepted papers to develop explanations of detector simplification, spatial alignment, loss design, anchor-free prediction, pseudo-label reliability, and transformer matching and supervision.
---

# Write an ICCV detection paper

Write the requested draft or revision using the supplied method and results. Identify the precise failure, unnecessary complexity, or learning mismatch that the contribution changes. Continue through the requested sections with concise placeholders for missing facts.

## Find the argument behind the component

| Contribution | Strong explanatory move | Sources |
|---|---|---|
| A simpler detector or training process | Inventory the concrete costs, then show which design removes them | [Fast R-CNN](references/papers/P01.md) |
| Adaptive sampling or spatial alignment | Show what the fixed representation loses and why the task needs it | [Deformable ConvNets](references/papers/P02.md), [Mask R-CNN](references/papers/P03.md) |
| A loss function | Diagnose the aggregate training effect before writing the formula | [Focal Loss](references/papers/P04.md) |
| Anchor-free prediction | Address the concrete objections to the simpler formulation | [FCOS](references/papers/P05.md) |
| Additional object evidence | Explain why the current prediction can look plausible while being wrong | [Keypoint-triplet CenterNet](references/papers/P06.md) |
| Classification–localization alignment | Connect disagreement to which box is selected | [TOOD](references/papers/P07.md) |
| Semi-supervised detection | Separate reliable class information from reliable localization | [Soft Teacher](references/papers/P08.md) |
| Transformer training | Identify which representation receives too little supervision or which assignment preference conflicts | [Co-DETR](references/papers/P09.md), [Stable Matching](references/papers/P10.md) |

Do not make a list of module names stand in for the contribution. A small change can carry a substantial paper when its necessity and consequences are explained.

## Introduce the smallest convincing example

Use an example that exposes the mechanism: a box with plausible corners but no corresponding object inside; an RoI whose rounding shifts mask coordinates; a prediction with high confidence but poor localization. Explain the example before generalizing to the proposed operation.

Keep the example's role clear. It motivates the design; the experiments establish its usefulness. A two-prediction thought experiment does not prove a unique global optimum, and an attention map does not prove semantic understanding.

For a loss or matching method, distinguish the training target, matching cost, and inference score. They perform different jobs. Stable Matching explains why using the training loss directly as a matching cost can favor an undesirable candidate.

## Let experiments complete the explanation

Begin with the result that answers the opening problem. Then explain the diagnostic that clarifies why it changes. Focal Loss examines the distribution of loss contributions; FCOS measures assignment coverage and ambiguity; TOOD examines agreement between confidence and localization; Soft Teacher studies two notions of pseudo-label reliability.

Use component comparisons to assign roles, not merely to say every row helps. An inherited improvement, a new learning rule, and a longer training recipe should not all become evidence for the same innovation. When the user has only aggregate results, write the supported performance finding and keep mechanism language appropriately limited.

Treat counterexamples as information. Fast R-CNN finds that more proposals can hurt. Co-DETR finds that more diverse auxiliary heads can stop helping. Mask R-CNN shows that adding a task can benefit one output while slightly harming another. Explain the useful setting rather than forcing a universal-win narrative.

## Place detail according to its explanatory value

Keep alignment conventions, assignment rules, supervision sources, and training-versus-inference paths visible when they define the idea. Put the formula next to its interpretation. Explain a small implementation choice when it changes the scientific comparison, such as the initialization that makes a cross-entropy baseline train successfully.

Use compact settings tables or an appendix for routine configuration. State the relevant evaluation distinction once, where it changes the meaning of a result: proposal time excluded from latency, extra annotations, NMS, augmentation, or a different amount of training data. These details should support the prose, not become repeated audit instructions.

## Write plainly and sell the specific contribution

Prefer “reduce the loss from easy negatives,” “preserve spatial alignment,” “weight uncertain background labels,” and “add positive training queries.” Avoid “unprecedented feature synergy,” “holistic object intelligence,” and “a priceless optimization paradigm.”

Keep classification, localization, matching, and ranking distinct. Define “alignment” by the quantities involved. Say exactly what “end-to-end,” “anchor-free,” or “training-only” means for the described system. A simpler design still has parameters; a training-only branch still consumes training resources.

Use confident language for a clear measured result. Use a proposed explanation as an explanation, not as an established cause. Credit the inherited detector openly; improving a critical interface or objective is a legitimate contribution.

## Supporting material

- [Playbook](references/playbook.md): opening logic, method explanation, result paragraphs, and detail selection.
- [Worked example](references/worked-example.md): turning alignment results into manuscript prose.
- [Ten source papers](references/corpus.md) and [BibTeX](references/references.bib): citations and individual craft notes.

Deliver usable prose first. A full-draft request requires a draft rather than only an outline or an experiment plan. Borrow the writing logic, not the wording, and add manuscript citations when the scientific relationship warrants them.
