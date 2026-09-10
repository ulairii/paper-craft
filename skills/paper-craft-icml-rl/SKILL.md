---
name: paper-craft-icml-rl
description: Write and revise ICML reinforcement-learning papers from methods and existing results. Distills ten accepted papers on policy optimization, actor–critic learning, offline RL, visual control, replay, planning, and online adaptation into narrative, experiment interpretation, and clear academic prose.
---

# Write an ICML reinforcement-learning paper

Produce the manuscript the author requested. For a full draft, write connected section prose with short factual placeholders where information is missing. Start by identifying what the method changes about learning or decision making, and why that change matters under the author's data and interaction budget.

## Choose the argument that fits the evidence

| Contribution | Narrative to develop | Sources |
|---|---|---|
| Policy optimization | A useful theoretical principle becomes a practical update through explicit approximations | [TRPO](references/papers/P01.md), [SAC](references/papers/P04.md) |
| Learning instability | A measured failure reveals the role of each proposed change | [TD3](references/papers/P05.md), [BCQ](references/papers/P06.md) |
| New prediction target | The richer object retains information that helps learning | [Distributional RL](references/papers/P03.md) |
| Efficient learning | Separate better use of experience from faster processing | [A3C](references/papers/P02.md), [CURL](references/papers/P07.md) |
| Empirical understanding | A surprising interaction becomes an explanation and a useful design lesson | [Experience Replay](references/papers/P08.md) |
| Planning and adaptation | Explain what each component or stage contributes to the decision | [TD-MPC](references/papers/P09.md), [ODT](references/papers/P10.md) |

Use a concrete opening: the actor exploits critic error; an offline learner cannot collect corrective data; visual observations make useful state information difficult to learn; short-horizon planning misses delayed rewards. Introduce that difficulty before the algorithm's acronym or list of modules.

## Make the method follow from the problem

Explain each component as a response to an identified difficulty. Follow the action-selection path before presenting every training loss when that makes a hybrid system easier to understand. Distinguish what is observed, what is predicted, what chooses actions, and what is available only during training.

For theory-motivated algorithms, show the short bridge from ideal update to implemented approximation. State the theorem's setting near its conclusion, then explain the practical relaxation and its purpose. Do not let a tabular guarantee silently become a neural-control guarantee.

Credit reused ingredients. The contribution may be a new combination, a better learning target, a setting that requires different behavior, or an empirical explanation. Explain the relationship that makes the contribution useful instead of claiming that every component is new.

## Turn the supplied results into an argument

Lead each results paragraph with the question its comparison answers. Report the result, interpret the pattern, and connect it to the contribution. A return curve can establish usefulness; a value-error diagnostic can explain why; a component comparison can reveal an interaction; an exception can locate the regime where the method helps.

Choose among sample efficiency, final return, stability across runs, wall-clock time, offline-data use, and adaptation gain. These are different claims. For planning, distinguish additional inference computation from training. For finetuning, discuss starting performance alongside final performance. For visual control, label a state-based reference as privileged information.

Use available evidence to draft now. If a missing comparison limits an explanation, state the narrower conclusion or use a brief placeholder. Do not turn a manuscript request into an open-ended experimental assignment.

## Include the details that carry scientific meaning

Keep the interaction setting, observation access, source of offline data, evaluation policy, and budget in the main setup. Put the meaning of an axis or aggregate beside the corresponding result. A frame, an agent decision, a gradient update, and a second are not interchangeable units.

Keep a design parameter prominent when it defines the method's behavior, such as an action constraint, entropy scale, or planning horizon. Move full layer inventories, tuning tables, routine update details, and extended proofs to supporting material. Explain an important condition once at its point of use.

## Sell the consequence in plain English

Prefer “reuse collected experience,” “reduce value overestimation,” “restrict unsupported actions,” “learn useful visual features,” and “estimate return beyond the planning horizon.” Avoid decorative phrases such as “holistic decision intelligence,” “synergistic policy orchestration,” and “unprecedented robustness.”

Replace “our method is effective” with the observable change and the setting where it matters. State a supported finding directly. Use “suggests” for a plausible mechanism with partial evidence, not for every result. Do not write that all prior methods fail when the evidence concerns one data regime or one implementation.

## Resources

- [Writing playbook](references/playbook.md): narrative choices, experiment paragraphs, and necessary detail.
- [Worked example](references/worked-example.md): drafting a critic-stability paper from supplied results.
- [Ten accepted ICML papers](references/corpus.md) and [BibTeX](references/references.bib).

Borrow the papers' argument structures, not their sentences. Cite source papers in the manuscript when they are scientifically relevant; the collection is not a mandatory citation list. Use the representation specialist when transferable representations, rather than control performance, are the main contribution.
