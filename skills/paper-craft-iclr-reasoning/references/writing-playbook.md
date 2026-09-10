# Make the idea easy to follow and worth remembering

These lessons interpret the writing choices of the source papers. They explain why an argument is persuasive; they do not claim access to the reasons behind acceptance decisions.

## 1. Find the sentence the reader should remember

Before choosing a title or outlining sections, finish: “The useful insight is that ...” Give the paper one center of gravity.

| Paper | Memorable insight, paraphrased | Writing lesson |
|---|---|---|
| [P01](papers/P01.md), Section 2/Fig. 1 | Different reasoning paths can converge on the same answer. | A small intervention can carry a strong story when its intuition is easy to grasp. |
| [P02](papers/P02.md), Sections 1–2 | Solving a complex problem can depend on solving its simpler parts first. | Describe a dependency, then let the method's sequence follow it. |
| [P04](papers/P04.md), Sections 1–2 | Supervising intermediate steps and supervising outcomes are different learning choices. | A clear conceptual distinction can be the paper's organizing idea. |
| [P07](papers/P07.md), Section 3/Fig. 2 | A promising state and a step that makes progress are different things. | Put the unfamiliar distinction beside a familiar one before formalizing it. |
| [P05](papers/P05.md), Sections 2–3 | The useful question is how to spend extra inference compute. | An analysis can sell a better decision, even without a new algorithm. |

Do not make the reader infer the central insight from an acronym or a list of components. Reuse the concept across the abstract, introduction, and experiments, while giving each section a different explanatory job.

## 2. Titles: name a concept, an action, or a finding

The source titles offer different strategies:

- **Name the mechanism.** Self-Consistency and Least-to-Most give a compact handle to a comprehensible operation ([P01](papers/P01.md), [P02](papers/P02.md)). A name works when explaining it also explains the idea.
- **Use a concrete action.** Let's Verify Step by Step makes the supervision choice immediately legible ([P04](papers/P04.md)). Memorable need not mean ornate.
- **State the finding.** The compute-allocation and CoT-applicability titles tell readers what the analysis teaches ([P05](papers/P05.md), [P10](papers/P10.md)).

For a new paper, try one title of each applicable type. Choose the title that conveys the most specific useful idea. An acronym followed by “a novel unified framework” usually tells the reader less.

## 3. Abstracts: compress the argument, not the table of contents

A useful sequence is problem → unresolved tension → insight → approach → main finding. Allocate sentences according to what is hard to understand; this is not a rigid five-sentence template.

[P01](papers/P01.md), abstract and Sections 1–2, pairs a short decoding explanation with concrete improvements. [P05](papers/P05.md), abstract and Section 1, makes the allocation question carry the paper. [P06](papers/P06.md), abstract and Sections 4–5, connects the difficulty of learning self-correction to the training approach.

Introduce the action before its acronym. Select the result that best explains the contribution rather than listing every benchmark. A final sentence should tell the reader what the finding changes, not repeat “extensive experiments demonstrate effectiveness.”

## 4. Introductions: make the next paragraph necessary

A productive progression is:

1. A concrete capability or decision matters.
2. An existing approach gets part of the way, but leaves a specific tension.
3. A new way to view that tension suggests an insight.
4. The method implements that insight, or the study investigates it.
5. The main findings explain why the insight matters.

The easy-to-hard framing in [P02](papers/P02.md), Section 1, makes decomposition feel motivated. In [P06](papers/P06.md), Sections 4–5, the diagnoses give each training stage a reason to exist. [P03](papers/P03.md), Section 2/Table 1, uses a different structure: a small set of confounds provides a roadmap for revisiting a popular claim.

Write the transition itself. “However, existing methods remain limited” leaves the reader waiting. A transition such as “Training on fixed mistakes leaves the model unprepared for the mistakes it generates itself” identifies the problem the next paragraph can solve. This example is original prose inspired by P06.

## 5. Methods: teach the idea in the order a reader can understand it

Start with the central decision. Explain the input and desired outcome, give the intuition, and then introduce the operations and notation.

- [P01](papers/P01.md), Fig. 1/Section 2: paths → answers → aggregation. The conceptual picture prepares the reader for the aggregation alternatives.
- [P02](papers/P02.md), Fig. 1/Tables 1–3: decomposition → dependent solving. The worked prompt shows what the dependency means.
- [P08](papers/P08.md), Fig. 2/Section 3: generation → selection. Each part addresses a recognizable part of the task.
- [P07](papers/P07.md), Fig. 2/Section 3: a simple example distinguishes value from progress before the more technical argument.

Define symbols where they are used. Put an equation immediately after the sentence that explains its purpose. Describe a component by what it does before assigning it an elaborate name. The method section should feel like learning an idea, not touring the implementation.

## 6. Contributions: give each bullet a different job

A method, a finding, and a useful dataset can be separate contributions. “We propose X,” “We introduce the components of X,” and “We combine them into framework X” describe one contribution three times.

[P04](papers/P04.md) connects a supervision comparison with a data contribution. [P05](papers/P05.md) makes analytical guidance the contribution. [P10](papers/P10.md) separates the question of where CoT helps from the question of why. Let the work determine the contribution type; do not force every paper to sell architectural novelty.

Replace evaluative adjectives with content: what changed, what became possible, or what was learned. Preserve a confident finding when the material supports it.

## 7. Detail: explain now, expand later

The main-text question is: “Does the reader need this to understand the idea or interpret the result?”

| Keep near the argument | Expand in the appendix | Usually cut |
|---|---|---|
| A short example that makes a dependency clear | Complete prompts for every task | A general history of LLMs |
| The role of each training stage | Full optimizer and hyperparameter tables | Repeated descriptions of the same contribution |
| What a plotted axis or comparison means | Additional runs, traces, and task tables | Prose that reads every table cell |
| A task condition that explains a surprising result | Detailed implementation choices | Decorative equations and inflated component names |

[P02](papers/P02.md) uses method examples to teach decomposition while placing extensive prompts in appendices. [P06](papers/P06.md) uses its main figures to explain training behavior and puts full configurations and prompts in Appendices B–C. [P05](papers/P05.md) keeps budget and difficulty central because they are the subject of the paper. Follow the role of a detail, not a blanket rule that every technical detail deserves main-text space.

## 8. End with understanding

[P10](papers/P10.md), Sections 4–5, moves from where CoT helps to planning and execution. [P09](papers/P09.md), Section 4, separates verification, critique generation, and critique use. Both demonstrate a useful analytical move: replace a broad question with distinctions the reader can use.

A discussion should state what the reader can now reason about or choose differently. Explain a meaningful boundary once, where it helps that decision. Avoid repeating a disclaimer after every result or ending with an empty promise of future work.
