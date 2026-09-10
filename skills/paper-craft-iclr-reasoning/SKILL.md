---
name: paper-craft-iclr-reasoning
description: Write and improve ICLR papers on LLM reasoning and test-time compute using writing craft distilled from 10 accepted papers. Use to find the paper's story, frame its contribution, structure introductions and experiments, explain results, and replace awkward academic prose with clear English.
---

# Writing ICLR papers on LLM reasoning

Help the author make the idea easy to understand, its importance easy to see, and its experiments easy to follow. Learn from how the source papers turn technical work into a compelling argument. Default to producing usable prose.

## Start with the writing task

Read the user's draft, idea, or results and identify the requested deliverable. Find the central insight: what should the reader understand after reading this paper that they did not understand before? Offer two possible framings if the material supports distinct stories, choose the better fit, and write.

Use available facts. Keep a short placeholder for a missing result and continue drafting. Preserve numbers and meaning. Do not turn a writing request into a review report, reproducibility audit, or a queue of experiments the author must complete first.

## Write in this style

- **Use familiar, precise words.** Prefer “use,” “show,” “choose,” and “improve” to “utilize,” “elucidate,” “facilitate the selection of,” and “effectuate an enhancement.” Keep necessary terms such as process supervision and self-consistency; plain English does not mean imprecise English.
- **Name the actor and action.** Write “The verifier scores each step,” not “Step-level evaluative assessment is conducted.” Use active voice when it makes responsibility clearer; do not mechanically rewrite every passive sentence.
- **Keep technical names stable.** Once you call something a verifier, do not cycle through evaluator, assessor, critic, and judge just for variety. Introduce an acronym only when it earns repeated use. Avoid invented compound labels for ordinary ideas.
- **Give each paragraph one job.** Open with its point, develop it with a mechanism or example, and end with the implication that makes the next paragraph necessary. Vary sentence length; split sentences carrying several independent claims.
- **Make transitions carry reasoning.** Explain why a limitation motivates the next design choice. Repeated “Moreover,” “Furthermore,” and “Importantly” cannot supply that connection.
- **Put intuition before machinery.** Explain the decision the method changes before its equations, training stages, or search operators. Introduce notation where readers need it.
- **Make novelty concrete.** Replace “a novel and powerful framework” with what changes, why that change matters, and what it lets the reader do or understand. Confident verbs are welcome when supported; do not bury a clear finding under repeated “may potentially suggest.”
- **Select results, then interpret them.** Explain the comparison that advances the story. Do not narrate every table cell or end each paragraph with “demonstrating the effectiveness of our method.”
- **Choose details by reader need.** Keep information needed to understand the contribution near the argument; put long prompts, exhaustive settings, and extra traces in the appendix. Mention cost when efficiency is the point, not as a compulsory detour in every writing task.

These are editorial recommendations distilled from the papers' explanatory choices, not claims that every source follows every rule. See the [language guide](references/claim-language.md) for original before/after examples.

## Build the story

Choose the structure that fits the work; do not force every paper into a multi-component method story.

| Story | What makes it compelling | Source examples |
|---|---|---|
| A simple change unlocks a capability | One recognizable bottleneck, one understandable intervention | Self-consistency [P01](references/papers/P01.md); least-to-most [P02](references/papers/P02.md) |
| A diagnosis makes the method necessary | Each component answers a failure the reader already understands | SCoRe [P06](references/papers/P06.md); rStar [P08](references/papers/P08.md) |
| A better distinction changes the design | Make two previously conflated choices explicit | Process supervision [P04](references/papers/P04.md); rewarding progress [P07](references/papers/P07.md) |
| An analysis gives a useful decision rule | Organize around when and why, not a list of scores | Compute allocation [P05](references/papers/P05.md); CoT applicability [P10](references/papers/P10.md) |
| A surprising result changes our understanding | Explain what assumption fails and what replaces it | Self-correction [P03](references/papers/P03.md); self-verification [P09](references/papers/P09.md) |

For an introduction, move from the concrete problem to the unresolved tension, the key insight, how the method realizes it, and the most informative finding. Keep contribution bullets distinct: an idea, a finding, or a resource—not three descriptions of the same system.

For an abstract, compress that same story. For a title, name the concept or finding the reader should remember. For a method section, follow the idea's dependencies rather than implementation order. For experiments, order reader questions so that results explain the contribution.

## Load references as needed

- Story, title, abstract, introduction, method: [writing playbook](references/writing-playbook.md).
- Word choice, sentence flow, paragraph revision: [language guide](references/claim-language.md).
- Experiment organization and result explanation: [experiment playbook](references/experiment-playbook.md).
- A complete demonstration: [SCoRe writing example](references/worked-example.md).
- Source selection: [10-paper reading list](references/corpus.md), then the relevant individual notes.

Use source examples to make advice specific. Do not require a fixed number of reference reads before a small edit, or repeatedly reopen papers for facts already covered in the notes. Add source pointers when explaining a writing choice; put citations in the manuscript only when scientifically relevant. Borrow the rhetorical move, not the author's wording.

## Deliver the writing

Lead with the requested draft, rewrite, outline, or experiment narrative. When useful, follow it with two or three concrete explanations of the most important writing choices and their source examples. For a local edit, return the edited passage without adding a generic checklist. Explain a missing fact briefly only when it materially affects the passage.
