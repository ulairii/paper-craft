# Plain, precise academic English

Use this guide while writing, not as an extra review stage. The examples below are original prose inspired by the cited papers' explanatory moves; they are not source quotations or measurements of the authors' vocabulary.

## Use ordinary words for ordinary actions

| Avoid when a simpler word conveys the meaning | Prefer |
|---|---|
| utilize, employ as a decorative synonym | use |
| facilitate the selection of | select, or help select if the assistance matters |
| conduct an evaluation of | evaluate |
| effectuate an enhancement in | improve |
| a multiplicity of reasoning trajectories | several reasoning paths |
| exhibits the capability to | can |
| a non-trivial performance amelioration | an improvement; state what improved |

Keep precise technical terms. “Process supervision” is useful terminology, not jargon to remove. “Verifier” should remain “verifier” throughout the explanation unless another object has a different role. Do not replace technical distinctions with a string of vague synonyms.

## Make the mechanism the subject

**Before:** Our framework facilitates the utilization of diverse inferential trajectories for robust answer determination.

**After:** We sample several reasoning paths and select the answer they agree on most often.

The second sentence teaches the operation. It follows the explanation in [P01](papers/P01.md), Section 2/Fig. 1, without copying its wording. “Robust” can be discussed when describing results; it need not obscure the method sentence.

**Before:** A hierarchical decomposition paradigm is employed to enable enhanced complex problem-solving capabilities.

**After:** We break the problem into simpler subproblems and use each solution to solve the next.

The dependency is now visible. This is the useful writing move in [P02](papers/P02.md), Section 2/Fig. 1.

## Keep one term for one object

**Before:** The verifier scores each step. The evaluator then ranks the paths, after which the assessor chooses an answer.

**After:** The verifier scores each step and ranks the paths. We return the answer from the highest-ranked path.

This is a hypothetical method illustration. The change removes the impression that three separate models exist. Technical consistency matters more than avoiding repetition.

## Replace vague transitions with the reason for the next step

**Before:** Existing methods have limitations. Moreover, we propose a two-stage framework to address these challenges.

**After:** Training on a fixed set of mistakes can miss the errors the model produces during revision. We therefore train on the model's own attempts.

The second version connects a specific problem to an action, inspired by [P06](papers/P06.md), Section 4/Fig. 4. It illustrates one motivation, not the whole SCoRe training method. Use “therefore” only when the preceding sentence supplies the reason.

## Split overloaded sentences without flattening the prose

**Before:** We introduce a verifier that evaluates reasoning steps using progress estimates from a prover and integrates these estimates into search, which improves reasoning and offers a principled framework for effective inference.

**After:** The verifier scores a step by the progress it makes toward a solution. Search uses this score to choose which paths to extend.

This example borrows the conceptual distinction in [P07](papers/P07.md), Section 3/Fig. 2. It gives each sentence an action and removes a claim that adds no explanation. Longer sentences are useful when they express one connected comparison; short sentences are not a quota.

## Be specific and confident

**Weak through inflation:** Our groundbreaking framework demonstrates remarkable and comprehensive reasoning capabilities.

**Weak through over-hedging:** Our results may potentially suggest that the method could perhaps be useful.

**Useful form:** The gains are largest on [task slice], where [relevant difficulty] makes [method behavior] useful.

Fill the brackets from the actual work. Difficulty slices in [P02](papers/P02.md), Tables 4/12, and [P05](papers/P05.md), Figs. 3/7, show how a condition can make a result more informative. A clear supported finding does not need defensive wording.

## Give the paragraph an arc

An effective result paragraph opens with the finding, selects the comparison that explains it, and ends with what the reader should learn.

**Before:** Table 2 shows the results. Our method performs well. It improves first-attempt accuracy and second-attempt accuracy. These results demonstrate the effectiveness of our proposed framework.

**After:** SCoRe improves answers through revision. On the reported MATH evaluation, accuracy rises from 60.0% on the first attempt to 64.4% on the second. Corrections outnumber regressions, showing that the second attempt contributes beyond the stronger initial answer.

The data are from [P06](papers/P06.md), Table 2; the paragraph is newly written. The opening gives the point and the ending interprets it. The full table remains available without being read aloud.

## Edit these habits at the sentence where they occur

- Delete empty openings such as “It is important to note that.” Start with the point.
- Replace repeated “Furthermore” with the actual relationship, or simply remove it.
- Remove “novel,” “powerful,” and “effective” when the sentence can name the contribution instead.
- Avoid inventing terms such as “reasoning-enhancement orchestration mechanism” for an ordinary training or selection step.
- Use parallel grammar in contribution bullets, while keeping their content distinct.
- Put pronouns near their referents. If “this” could refer to three preceding ideas, name the idea.
- Keep quantities, comparisons, and source meanings intact during revision. Missing results can remain brief placeholders.

The goal is readable scientific prose with the author's own emphasis, not uniform short sentences or a blacklist applied without judgment.
