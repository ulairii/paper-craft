# Worked example: explain a critic-stability result

This fictional example illustrates writing choices. The numbers below are invented for teaching and must not be presented as experimental evidence. The proposed method is also fictional.

## Author material

An author has a continuous-control actor–critic method that delays actor updates when the two critics disagree. The supplied comparison uses the same replay data and one million environment interactions per run. Across five runs, mean returns are 4,200 for the base method, 4,500 for a fixed-delay variant, and 4,850 for the adaptive-delay variant. Mean absolute critic error against rollout-based return estimates is 170, 130, and 95 respectively. The adaptive method takes 12% more training time than the base method. The author has no ablation that matches the number of actor updates between the two delay strategies, and has tested only one task family.

## Choose the contribution

The strongest story is that actor updates should account for the critic's changing reliability. The results connect an adaptive schedule with improved return and lower critic error. They do not establish that the schedule beats all alternatives, that disagreement is a calibrated uncertainty estimate, or that it saves wall-clock time.

This structure borrows the diagnostic-first argument of [TD3](papers/P05.md), the explicit distinction between practical behavior and ideal reasoning in [TRPO](papers/P01.md), and the separation of learning and execution efficiency in [A3C](papers/P02.md).

## Draft abstract

Actor–critic methods update the policy using a value estimate whose accuracy can change during training. A fixed update schedule therefore may apply policy updates when the critic is still unreliable. We propose an adaptive schedule that delays actor updates when two critics disagree and resumes them when their estimates become more consistent. In the evaluated continuous-control task family, the method improves mean return from 4,200 to 4,850 at one million environment interactions, compared with 4,500 for a fixed-delay variant. The gain is accompanied by lower critic error against rollout-based estimates, at a 12% increase in training time. These results motivate adapting the policy-update schedule to the critic's learning state.

## Draft introduction passage

An actor improves its policy by following the critic's estimates. When those estimates are inaccurate, the same update can favor actions that appear valuable only because of prediction error. Delaying actor updates gives the critic more time to learn, but a fixed delay treats all stages of training alike. This motivates a schedule that responds to the critic's current state rather than using the same interval throughout training.

Our method uses disagreement between two critics to decide when to postpone an actor update. This signal is available within the existing actor–critic architecture and changes how its components interact. We evaluate whether the resulting schedule improves return under a fixed interaction budget and whether that improvement accompanies more accurate value estimates.

## Draft method passage

At each training iteration, the method first updates both critics using a batch from the replay buffer. It then computes their mean absolute disagreement on [the states and actions used by the method]. If this statistic exceeds [the scheduling threshold or rule], the actor update is postponed; otherwise, the actor is updated using [the policy objective]. The schedule is intended to reduce policy updates during periods of inconsistent value estimation. Agreement alone does not imply accurate values, so the experiments separately measure error against rollout-based return estimates.

The two placeholders request facts needed to describe the actual method. They do not ask the author to invent a new design after seeing the results.

## Draft results passage

At one million environment interactions, adaptive delay achieves a mean return of 4,850, compared with 4,200 for the base method and 4,500 for fixed delay. The ordering is accompanied by a reduction in mean absolute critic error from 170 to 130 and 95, respectively. Together, these results support adapting actor updates to the critic's learning state in this task family. Because the schedules also change the number of actor updates, this comparison does not isolate whether the gain comes from their timing or their frequency.

The improvement concerns return at a fixed interaction budget. Adaptive delay increases training time by 12%, so the result does not establish a wall-clock speedup. A complete caption would specify [how returns are aggregated over evaluations] and [the variability across the five runs].

## Draft discussion passage

The results suggest that the critic's changing reliability can inform when to update the actor. The present evaluation covers one continuous-control task family, and disagreement is used as a practical signal rather than a calibrated measure of uncertainty. A comparison with matched actor-update counts would help distinguish adaptive timing from the effect of making fewer updates. The current evidence nevertheless shows a useful return–computation tradeoff under a fixed interaction budget.

## What changed in the writing

“Robust and efficient adaptive optimization” became a concrete operation and a measured consequence. The numerical result is stated directly; the mechanism is described with appropriate scope. The missing comparison limits the interpretation without preventing the author from obtaining usable draft prose.
