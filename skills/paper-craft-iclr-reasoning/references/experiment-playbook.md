# Experiments that carry the paper's story

An experiment section should help the reader understand the contribution. Start with what each experiment teaches, then select the tables, figures, and explanations that make that lesson clear.

## Choose the questions before arranging the tables

| Kind of paper | A useful experimental story | Source example |
|---|---|---|
| A simple inference change | Does it help? What about the change matters? How does behavior evolve with more samples? | [P01](papers/P01.md), Tables 2–3 and Figs. 2–3 |
| A decomposition method | Does the method handle increasingly complex combinations? Where is the gain concentrated? | [P02](papers/P02.md), Tables 4/12 |
| A training method motivated by failures | Do the diagnosed behaviors change? How do the stages contribute? What happens over further revisions? | [P06](papers/P06.md), Figs. 3–6 and Table 4 |
| A supervision comparison | What performance can the system reach? What do the controlled comparisons teach about supervision? | [P04](papers/P04.md), Figs. 3–4 |
| A compute-allocation analysis | Which strategy works at which budget and difficulty? How should that affect a practical choice? | [P05](papers/P05.md), Figs. 3/7/8 |
| A counterintuitive finding | When does the surprising relationship appear? What comparison makes it understandable? | [P07](papers/P07.md), Fig. 5 |
| A two-part system | How do candidate generation and selection each shape the final result? | [P08](papers/P08.md), Tables 4–5 |
| A capability analysis | Which part of the task succeeds or fails? What explains differences across tasks? | [P09](papers/P09.md), Section 4; [P10](papers/P10.md), Sections 4–5 |

Choose the sequence suited to the work. It need not contain every row or a universal set of experiments. If an author already has results, first organize those results into the strongest coherent explanation.

## Make subsection headings express questions or findings

“Main Results,” “Ablations,” and “More Analysis” label containers. More informative headings tell the reader why the material is there:

- “Does agreement help beyond drawing more samples?” — inspired by P01's sampling and ranking comparisons.
- “Where does decomposition help most?” — inspired by P02's complexity slices.
- “How does problem difficulty change the best allocation?” — inspired by P05.
- “What does the second attempt contribute?” — inspired by P06's revision metrics.

These are original heading suggestions, not source headings. Use a finding as the heading when it is established and central; use a question when introducing an investigation.

## Explain results in three moves

1. **Give the finding.** State the result the subsection exists to communicate.
2. **Choose the revealing comparison.** Use one or two numbers, a trend, or a task slice. Let the table carry the remaining values.
3. **Explain the implication.** Connect the observation to the insight that motivated the method or study.

For example, a paragraph about P02 should explain why gains at greater compositional length matter to easy-to-hard generalization. A paragraph about P05 should explain why a change in strategy ranking changes allocation decisions. A paragraph about P06 should explain what revision adds beyond the initial answer. “This demonstrates effectiveness” misses all three opportunities.

## Use ablations to explain design choices

An ablation is most useful to the narrative when the reader already understands why the component exists. [P06](papers/P06.md), Table 4, follows the earlier explanation of its training stages. [P08](papers/P08.md), Table 4, makes generation and selection separately visible. [P07](papers/P07.md), Fig. 5, gives the surprising prover-strength relationship room to be understood.

Introduce the question in ordinary language, state the comparison briefly, then explain what it teaches about the design. Avoid a catalog of removed components followed by a repeated claim that each is effective. Suggest a new experiment only if it fills a specific gap in the story the author wants to tell.

## Let a figure teach one idea

Use a compact example to introduce an unfamiliar mechanism, as in P01/P02. Use a curve when change with budget is the idea, as in P05. Use a behavioral breakdown when final accuracy hides the phenomenon, as in P06. Match the figure to the reader's question.

A caption should explain what is compared and what to notice. The prose should explain why that observation matters. Do not duplicate the entire caption in the paragraph. These recommendations follow the explanatory roles of the cited figures, not a prescription to copy their visual design.

## Put details where they earn their space

Explain the dataset and metric enough for the comparison to make sense. If the contribution concerns efficiency, explain the budget. If it concerns revision, explain what counts as a revision. If neither is central to a requested paragraph, do not append a general cost or verification checklist.

Keep long prompts, exhaustive settings, and additional traces in appendices. A short main-text example may still be essential when it teaches the mechanism, as in P02. Relevant limitations should sharpen an interpretation: P10's task differences explain applicability; P05's difficult problems explain where an allocation rule stops helping. State the useful boundary once rather than surrounding every finding with disclaimers.
