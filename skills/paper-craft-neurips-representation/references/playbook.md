# NeurIPS representation learning: writing playbook

## Find the sentence that gives the paper a purpose

A representation paper needs a useful question before it needs a method name. [BYOL](papers/P02.md) asks whether useful learning requires negatives. [InfoMin](papers/P06.md) asks which information different views should share. [VICRegL](papers/P10.md) asks how to retain useful local information alongside global invariance. Each question gives the method and experiments a common purpose.

Write a provisional central sentence from the author's results: “The current view construction removes information needed for localization,” or “A label-aware positive set improves classification without changing the inference model.” Use it to choose the opening, method order, and leading figure. Revise it if a different finding is more informative.

## Five useful narrative patterns

### Observation → explanation → design

The [transfer analysis](papers/P08.md) starts with a familiar account of transfer, then disrupts spatial structure to ask what that account misses. Model comparisons and interpolation develop the explanation, while early-checkpoint transfer supplies a practical consequence. An empirical discovery paper can use this sequence without inventing an algorithmic contribution.

Introduce each analysis with the question left by the previous finding. End with what the new observation changes in the reader's understanding. Keep alternative explanations close to the relevant experiment, rather than adding a generic limitations paragraph after an overconfident story.

### Simple idea → consequential choice → useful result

[SupCon](papers/P05.md) makes multiple positives intuitive, then compares two plausible loss formulations. [Debiased Contrastive Learning](papers/P07.md) exposes an oracle gap, derives a feasible correction, and shows a compact implementation. Simplicity is persuasive when the paper explains why the exact choice matters.

Use one equation to highlight the changed operation. Follow it with an interpretation in familiar language. Extended algebra belongs in the appendix when the reader already understands what it establishes.

### Shared principle → complementary components → stronger recipe

[AMDIM](papers/P01.md) names its changes to cross-view prediction, feature scales, and encoder capacity. [SwAV](papers/P03.md) separates swapped prediction, online assignments, and multicrop. These papers offer a way to write a combination honestly and positively: show why the pieces work together and which benefit each supplies.

A recipe's final score establishes the combined capability. A controlled component comparison explains part of that capability. Give each its own sentence rather than assigning the entire gain to the most novel term.

### Large teacher → scarce labels → compact student

[SimCLRv2](papers/P04.md) connects model scaling to an appealing use case: better performance with fewer labels, followed by distillation into a smaller model. Explain the stages as a flow of information. Readers should understand how task-agnostic features become task-specific predictions and then a deployable student.

Place labeled-data use and teacher cost where the stages are introduced. This keeps the label-efficiency contribution strong without confusing it with training efficiency or a smaller total dataset.

### Domain tension → targeted invariance → measured tradeoff

[InfoMin](papers/P06.md) and [GraphCL](papers/P09.md) make augmentation a scientific choice: a transformation can remove nuisance variation or remove the signal itself. [VICRegL](papers/P10.md) makes a related tension measurable by reporting classification and segmentation together.

Explain one domain example before listing transformations. A bond change and a social-network edge change can mean different things. A view that is useful for object identity need not preserve location. Let experiments show which distinction matters in the author's setting.

## Give experiments different jobs

| Job | What the result paragraph should explain | Examples |
|---|---|---|
| Establish capability | What can the learned features do under the stated readout? | BYOL transfer; SupCon classification |
| Expose the problem | What does an oracle or intervention reveal? | Debiased negatives; block-shuffled transfer |
| Explain a design | Which comparison connects a component to its intended role? | SupCon objective alternatives; VICRegL matching |
| Reveal an interaction | When does the same choice help or hurt? | InfoMin frequency separation; GraphCL augmentation pairs |
| Show practical value | What quality is obtained for a given label, model, or resource budget? | SimCLRv2 stages; SwAV crop configurations |

Use the experiments already supplied. If a missing fact prevents a sentence, leave a specific placeholder and continue drafting the sections that can be written. Additional experiments may be useful suggestions, but they are not the manuscript.

## Interpret the result, not just the ranking

A strong result paragraph can be short:

> Local matching improves frozen segmentation by [gain] while classification changes by [difference]. Combining location and feature matching outperforms either alone, supporting their complementary roles in the proposed objective. The remaining gap under [condition] suggests that [specific boundary].

This is an original writing pattern, not a quotation. Replace every placeholder with the author's evidence. Do not add a mechanism claim unless the comparison actually distinguishes it.

Explain metric disagreements when they are informative. [SwAV](papers/P03.md) shows why a lower assignment loss need not yield better features. [SupCon](papers/P05.md) separates classification improvements from broadly comparable transfer. [VICRegL](papers/P10.md) distinguishes accessible information under frozen readouts from performance after adaptation. These are useful findings, not distractions to hide.

## Place details by their explanatory value

The main method needs the positive or target construction, the changed operation, and the representation used downstream. A multistage story needs supervision at each stage. A transfer analysis needs the intervention and the measured quantity. Full optimizer grids, long proof steps, and additional galleries usually belong in supporting material.

A figure should answer a question. A method figure can show what each branch predicts; a pairwise matrix can show augmentation interactions; a two-axis result can show a tradeoff. A selected qualitative example illustrates an established finding. Explain what its marks represent: a displayed feature location is not necessarily a small receptive field.

## Make the language do useful work

| Vague wording | More useful wording |
|---|---|
| “We learn superior semantics.” | “The frozen features improve [task] under [readout].” |
| “A synergistic multicomponent framework.” | “One term matches locations; the other connects similar features across locations.” |
| “The mechanism is proven by ablations.” | “Removing the predictor causes collapse in this setting, supporting its role in the proposed explanation.” |
| “More augmentation is always better.” | “The gain increases until the transformation removes information needed for the task.” |
| “The model is efficient.” | “The deployed student uses [size], after distillation from [teacher].” |

Use one stable term for each concept. Avoid renaming familiar operations to make them sound novel. Contribution bullets should state outcomes or insights, not merely list the existence of a method, experiments, and code.
