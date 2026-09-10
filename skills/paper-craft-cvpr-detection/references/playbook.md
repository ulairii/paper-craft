# Detection writing: from a result table to an argument

## Find what the result changes

A higher AP score is a result, but it does not by itself name the contribution. Ask what made the gain possible or what the pattern teaches. The selected papers provide several distinct answers:

- [R-CNN](papers/P01.md) makes a strong classification representation usable for detection by solving localization and adaptation problems.
- [FPN](papers/P04.md) supplies semantic strength at finer feature resolutions.
- [Cascade R-CNN](papers/P05.md) explains why stricter supervision alone does not yield tighter detections.
- [ATSS](papers/P06.md) changes the useful distinction between detector families.
- [EfficientDet](papers/P07.md) makes a range of resource budgets the object of the paper.

Write the contribution as a change plus a reason: “We select positives from each object's candidate distribution, because a fixed overlap threshold does not adapt to that distribution.” This is an original illustration of the ATSS writing move, not a quotation. The actual draft must describe the user's rule.

## Write an introduction with a visible dependency

A representation paper can move from a desired property, through a missing property in existing features, to the operation that supplies it. FPN's introduction and Figures 1–2 make spatial resolution and semantic strength concrete before introducing the path design.

A diagnosis paper can begin with an apparent solution and its failure. Cascade R-CNN's introduction and Figure 1 explain why raising a training threshold is insufficient. ATSS §3 goes further: an experiment precedes the proposed method because the experiment changes the question that the method should answer.

An efficiency paper can show the operating range immediately. YOLO's introduction previews speed, error behavior, and transfer, all of which return in §4. EfficientDet Figure 1 puts accuracy against computation, making a family of models meaningful before their individual configurations appear.

These are alternatives, not a mandatory five-paragraph template. Omit a broad history of computer vision unless it helps explain the present tension. End the introduction with distinct contributions: the central idea, the main finding, and a resource or extension only if it is substantial.

## Explain the unfamiliar operation, abbreviate inherited machinery

R-CNN §2.1 cites the existing architecture and explains the region interface. Sparse R-CNN Figures 3–4 instead spend space on dynamic interaction because readers need to understand how proposal features generate instance-specific parameters. Main-text detail should follow explanatory difficulty, not lines of code.

Use a small example before a new abstraction. YOLO9000 §4 introduces overlapping labels such as dog and a breed before the hierarchy. Dynamic Head §3 assigns a physical meaning to the tensor dimensions before applying attention along them.

Keep the distinction that prevents the most likely misunderstanding close to the method. For DN-DETR, the denoising targets are training inputs and their queries disappear during inference. For FPN, predictions use multiple pyramid levels, which distinguishes it from a similar-looking top-down representation with a single output. These are concise explanatory sentences, not an audit procedure.

## Arrange results as reader questions

| Central story | Useful order | Source locations |
|---|---|---|
| A failure explains the new method | Show the failure; compare the natural alternative; explain the successful intervention; show its useful scope | Cascade R-CNN §§3–5; Sparse R-CNN Tables 3–5 |
| A new distinction explains old results | Separate the candidate explanations; present the decisive comparison; show the design implied by it | ATSS §3 and Tables 1–2, followed by §4 |
| A representation supplies missing information | Show system usefulness; explain the contribution of the feature paths; demonstrate another relevant use | FPN §5.1.1, Tables 1–2, and §6 |
| A model family improves efficiency | Show the frontier; explain fusion and scaling separately; identify practical operating choices | EfficientDet Figures 1, 4, 6 and Tables 4–5 |
| A training change accelerates convergence | Show the trajectory; explain the proposed source of difficulty; compare short and full schedules | DN-DETR Figures 1–2, 5; Tables 1–3; supplement §§7.1–7.2 |

Use the order that fits the user's available evidence. A writing request does not require commissioning all experiments in this table.

## Interpret instead of announcing effectiveness

Weak: “Table 3 demonstrates the effectiveness of all components and the superiority of the full model.”

Stronger, using an original hypothetical example: “The largest improvement appears at the stricter overlap threshold. This pattern is consistent with the refinement stage improving box alignment, rather than simply finding additional objects.”

The second version names a pattern and relates it to a mechanism. It also avoids claiming that a table rules out every alternative explanation. If the data contain no scale-specific pattern, do not invent one to fit a feature-pyramid story.

A useful paragraph often needs only one or two numbers. Let the table carry the complete values. Mention configurations where they change the interpretation: YOLO's combination experiment answers complementarity, while its standalone model answers real-time prediction. DN-DETR's supplementary timing table distinguishes shorter training schedules from measured minutes. Those distinctions improve the explanation without turning every paragraph into a qualification list.

## Give failure and diminishing returns a role

YOLO9000 Table 7 explains why transferred objectness helps some new categories more than others. Sparse R-CNN's proposal traces illustrate refinement, rather than serving only as attractive successful detections. Dynamic Head Table 2 shows that adding blocks eventually stops helping. The prose can use such results to define an operating choice or explain a learned behavior.

Avoid claiming that every extra component improves every metric. YOLO9000's development table includes a change that improves recall while initially lowering AP. A clear explanation of that tradeoff is more useful than a forced monotonic success narrative.

## Choose what to leave out

Keep the bottleneck, changed operation, essential interfaces, and evidence interpretation in the main argument. Put long configuration lists, exhaustive variants, and exploratory side tasks in supporting material when they would interrupt it. FPN §3 explicitly sets aside more complex connections; DN-DETR's supplement separates preliminary tasks from the main convergence contribution.

Do not copy every stylistic habit of influential papers. Dramatic adjectives, repeated claims of novelty, and awkward grammar do not become good writing because the paper was accepted. Distill the explanatory decision: a useful contrast, a memorable example, a well-placed diagnostic, or a clear implication.
