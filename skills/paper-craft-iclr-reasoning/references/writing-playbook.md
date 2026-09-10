# Writing principles distilled from the papers

These are our recommendations, not author quotations or conference requirements. Each principle identifies its evidence and the conditions under which it should not be copied.

## W1: Frame a recognizable failure, not just the importance of the field

**Observation.** [P02](papers/P02.md), Section 1, defines an easy-to-hard generalization gap. [P06](papers/P06.md), Section 4, distinguishes distribution shift from behavioral collapse. These diagnoses give method components testable responsibilities.

**Recommendation.** The second introduction paragraph should explain which existing approach fails, under what conditions, and how. If evidence is missing, pose a research question rather than asserting that existing methods universally fail. One opening paragraph can establish task value; half a page of AI history is unnecessary.

**Boundary.** [P05](papers/P05.md) contributes compute-allocation insights without needing an invented module. A gap can be an unresolved relationship.

## W2: Order the method by problem dependencies, not code directories

**Observation.** [P02](papers/P02.md), Fig. 1, moves from decomposition to dependent solving. [P08](papers/P08.md), Fig. 2, moves from candidate generation to consistency-based selection. [P06](papers/P06.md), Fig. 11, makes the design logic explicit.

**Recommendation.** Each method subsection should state its input, the previously established problem it addresses, how it changes a decision, and where its output goes. Equations should precisely distinguish mechanisms; examples should clarify behavior that equations leave unintuitive. Background equations that do not explain a decision difference can be omitted.

**Boundary.** Component names and polished overview figures cannot replace behavioral evidence. Three system components do not automatically constitute three independent innovations.

## W3: Write contributions as new knowledge plus the evidence that establishes it

**Observation.** [P04](papers/P04.md) compares supervision types through controlled experiments. [P05](papers/P05.md) analyzes budget allocation. [P03](papers/P03.md) isolates evaluation confounds. [P10](papers/P10.md) separates where from why.

**Recommendation.** For methods, state which decision changes and why it helps. For analyses, state the conditional relationship revealed and how it is measured. For negative results, state the explanation ruled out and the remaining scope. Extensive experiments, state-of-the-art performance, and priority claims do not by themselves explain the knowledge gained.

**Boundary.** Do not promise “first” without a systematic novelty check. This pilot corpus cannot provide a complete novelty assessment for a user's new project.

## W4: Give each experiment subsection a question, not merely a dataset

**Observation.** [P04](papers/P04.md), Sections 3/4, separate best performance from attribution. [P07](papers/P07.md), Fig. 5, tests prover strength and complementarity. [P06](papers/P06.md), Table 4, tests training components.

**Recommendation.** A useful sequence is effectiveness, source of gains, conditions of effectiveness, then cost and failure. Within a paragraph, move from question to controlled design, key observation, interpretation, and remaining limits. Do not read every table cell aloud; select comparisons and counterexamples that change the conclusion.

**Boundary.** Not every paper needs the same four sections. Build the smallest sufficient evidence chain for the central claim. Ten more benchmarks cannot replace one missing critical control.

## W5: Use boundaries to make claims precise

**Observation.** Hard problems and high inference loads alter the model/compute tradeoff in [P05](papers/P05.md). [P09](papers/P09.md) includes cases where self-critique helps. [P10](papers/P10.md) limits its scope to single-prompt CoT.

**Recommendation.** Put decisive conditions near the headline. Replace unconditional superiority with the evaluated budget/task range and the conditions where the advantage disappears. A useful limitation guides a choice; a generic statement that there is room for improvement does not.

**Boundary.** Do not defend an overbroad title simply because it appeared in an accepted paper, or elevate a negative result into an impossibility theorem. Accepted papers also need auditing.

## W6: Keep decisive details; move recoverable detail out of the main argument

| Information | Needed in the main text when | Usually suitable for an appendix | Source |
|---|---|---|---|
| Prompts | Instructions are the intervention, or feedback conveys correctness | Full long demonstrations and all task templates | P02 Sections 2–3; P03 Section 5 |
| Budgets | The headline concerns compute, speed, or fair comparison | Expanded hardware details and per-task token tables | P05 Section 3.2; P08 A.3 |
| Data | Splits or extra supervision change the comparison's meaning | Complete annotation and quality-control procedures | P04 Section 2.4, Appendices B/C |
| Failure examples | They expose a key failure mechanism; explain selection | More trajectories and complete error records | P01 Section 5; P02 Section 7.4 |
| Hyperparameters | They define the search space, sampling budget, selection, or stopping | Complete training configurations not decisive for the claim | P05 Appendix O; P06 Appendix B |

Suitable for an appendix does not mean optional to record. Irrelevant model tutorials, table-by-table repetition, and repeated promotional sentences can be deleted. Negative results, costs, and extra supervision should not disappear.
