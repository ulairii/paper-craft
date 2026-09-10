# Writing an ICML reinforcement-learning argument

The source papers offer several ways to make a contribution convincing. Choose the one supported by the author's material. Their acceptance does not establish which writing choice caused it.

## 1. Open with a difficulty the reader can picture

A broad account of RL applications rarely distinguishes a paper. Give the reader a concrete failure or tradeoff first, then explain its importance.

[BCQ](papers/P06.md) makes the lack of corrective interaction central: an offline learner can assign high values to unsupported actions but cannot collect data to repair those estimates. [TD3](papers/P05.md) shows how an actor can exploit inaccurate values, making the critic's error a policy problem. [CURL](papers/P07.md) turns a representation question into the gap between learning from pixels and learning from state information.

A useful introduction sequence is:

1. Describe the desired capability and the condition that makes it difficult.
2. Identify the existing approach's specific limitation under that condition.
3. State the insight that changes the problem.
4. Explain the proposed operation and its useful consequence.
5. Preview the strongest supplied evidence and its scope.

For an empirical paper, the insight can be an interaction. [The replay study](papers/P08.md) asks why larger memory helps Rainbow but not DQN. That question gives the study direction without inventing a new architecture.

## 2. Give each contribution a role

A list of three modules is a description, not yet an argument. Explain the difficulty each one addresses and how they work together. TD3 connects clipped estimates, delayed actor updates, and target smoothing to related effects of approximation error. Its component experiments show why interactions matter; they do not imply that each addition independently helps every task.

An integration can be the main contribution. [SAC](papers/P04.md) combines reuse of experience with stochastic entropy-based learning to address sample cost and brittle training. [TD-MPC](papers/P09.md) assigns local consequences to model rollouts and longer-term outcomes to a terminal value function. In both cases, describe the division of work before listing network names.

For a new learning target, use a short conceptual comparison. [Distributional RL](papers/P03.md) distinguishes the return distribution from its expectation. Explain what information becomes available, how the target is learned, and what the experiment says about its value.

## 3. Put the reader's decision path before notation

For an actor–critic method, introduce the critic's estimate and how the actor uses it. For an offline method, show how candidate actions remain related to the dataset. For a planner, walk through observation, latent rollout, reward estimate, terminal value, and selected action. TD-MPC describes inference before model training, which gives every objective a recognizable purpose.

A theory-to-algorithm bridge should be short and explicit. [TRPO](papers/P01.md) tells the reader which ideal quantities become tractable approximations. Keep the assumption and the practical relaxation together. The theorem motivates a design; the experiments establish what its implementation does in the evaluated setting.

Do not reproduce standard RL background at textbook length. Define the notation needed to understand the change and cite familiar machinery. Full proof details belong after the main argument unless the proof technique is itself the contribution.

## 4. Give experiments different jobs

| Question in the story | Useful supplied evidence | Example |
|---|---|---|
| Does the proposed failure occur? | A direct diagnostic linked to behavior | TD3 value estimates and rollout-based reference values |
| Does the method help? | Return or success at a stated interaction budget | SAC control curves; BCQ offline settings |
| What changes learning efficiency? | Return versus experience, separately from time | A3C frame and wall-clock curves |
| Which interaction matters? | Additions to a base and removals from the full method | Replay capacity × multi-step targets |
| What does more computation buy? | A trained model evaluated at different planning budgets | TD-MPC planning horizon and iterations |
| What does adaptation contribute? | Starting quality, final score, and online budget | ODT offline and online comparisons |
| Where does the method fall short? | A relevant task or regime with a different outcome | BCQ's simple covered tasks; CURL's remaining state gap |

These are options for organizing existing results, not a compulsory checklist. Choose the evidence that advances the actual claim. More plots are useful only when they answer another question.

## 5. Write interpretation instead of reciting the table

Use a paragraph with four moves: question, observation, explanation, implication. For example:

> We next ask whether delaying the actor helps when the critic changes rapidly. At the same interaction budget, the delayed variant achieves higher return on [tasks], while [task] changes little. The gain coincides with lower disagreement in the value estimates. This pattern supports delaying policy updates in the evaluated high-error regime, although it does not isolate disagreement as the sole cause.

The text should tell the reader what the pattern means. Do not list every score already visible in the table. Describe an exception when it distinguishes mechanisms or narrows the useful regime.

The replay paper tests a variance explanation and retains only partial support: turning off sticky actions reduces, but does not remove, the benefit of larger buffers. That is a complete and useful scientific paragraph. It does not need to end in a claim that the phenomenon has been fully explained.

## 6. Make efficiency and adaptation claims legible

[A3C](papers/P02.md) separates speed from data efficiency. [CURL](papers/P07.md) separately defines return at a fixed budget and steps to reach a reference score. TD-MPC reports both time per fixed amount of experience and time to solve; a method can improve sample efficiency without reducing cost per sample.

For offline-to-online learning, [ODT](papers/P10.md) makes adaptation gains part of the story rather than relying only on final ranks. Preserve what the comparison actually measures: unequal starting quality, different pretraining schedules, or extra offline data can explain part of an apparent gain. If exact starting-checkpoint results are missing, draft the final-budget comparison and leave the adaptation delta unspecified.

A privileged state baseline, simulator-based planner, or pure-online baseline answers a particular question. Name its role. It is not automatically an equal-information competitor or a formal upper bound.

## 7. Keep necessary detail without drowning the paper

In the main text, retain facts that change what the result means: whether the learner can collect new data, the observation modality, the batch's origin, the training objective versus the reported reward, and the action-selection protocol. Put curve selection and the meaning of an uncertainty band in the caption rather than making the reader infer them.

Keep a parameter in the method when it defines a scientific tradeoff. BCQ's perturbation bound determines departure from demonstrated behavior; SAC's reward scale affects stochasticity; TD-MPC's planning horizon changes local lookahead. Routine hidden-layer sizes and exhaustive grids can go in the appendix.

Do not copy a source paper's strongest adjective when its detailed results support a narrower claim. State the actual gain confidently. Useful phrases include “improves early learning,” “reduces estimated-value error,” “matches the final score with fewer interactions,” and “benefits from adaptation on the tested tasks.”

## 8. Draft with the evidence already available

For a full-draft request, produce abstract, introduction, related work, method, experimental setup, results, and discussion as prose, adapting section order to the contribution. Reuse supplied notation and reported numbers. Use short placeholders such as “[evaluation policy]” or “[return at 200k interactions]” for missing facts.

Choose a modest, supported interpretation over an invented experiment. The writing should make the existing result's importance clear, while keeping prospective explanations and future work distinct from completed findings.
