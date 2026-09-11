---
name: paper-craft-usenix-privacy
description: Draft and revise USENIX Security privacy and measurement papers from methods and existing results. Distills ten accepted papers on web tracking, browser fingerprinting, cookie policies, user exposure, and privacy defenses into narrative, contribution framing, experiment explanation, and plain academic English.
---

# Write a USENIX Security privacy and measurement paper

Produce the requested manuscript prose. For a full draft, write connected sections from the supplied evidence and use specific placeholders where facts are missing. This collection focuses on browser privacy and web measurement; choose the story that matches the contribution.

## Find the observation that changes the reader's understanding

| Contribution | Central question | Source examples |
|---|---|---|
| Newly observable signal | What can the page learn that earlier observation methods missed? | [Fp-Scanner](references/papers/P02.md), [Fingerprinting in Style](references/papers/P06.md), [Human Touch](references/papers/P07.md) |
| Ecosystem measurement | Which population, unit, or time dimension reveals a new pattern? | [Cross-device tracking](references/papers/P01.md), [When Sally Met Trackers](references/papers/P09.md) |
| Policy analysis | Which enforcement assumptions fail in which contexts, and why? | [Cookie Jar](references/papers/P03.md) |
| Privacy defense | What useful behavior is preserved while its observable signal changes? | [Rendered Private](references/papers/P04.md), [CloakX](references/papers/P05.md), [Simulacrum](references/papers/P08.md) |
| Robust detection | Which behavior remains informative when an adversary changes appearances? | [WebGraph](references/papers/P10.md) |

A larger crawl alone rarely explains the insight. Develop the new observation, distinction, causal mechanism, or useful tradeoff that the data makes visible. An ML classifier used to study tracking belongs here when privacy exposure or blocking carries the contribution.

## Open with an ordinary action and its hidden consequence

Use one concrete example: selecting text activates an extension; a hidden style changes a page-created element; two device histories reveal complementary activity; a shared identifier connects two requests. Explain what the observer can see, why it matters, and which previous assumption leaves this behavior unaccounted for.

Then name the contribution. “We add interaction-triggered behavior to extension analysis” is more informative than “We present a comprehensive and unprecedented framework.” Credit earlier methods for the channels they cover. Describe the added capability directly.

For measurement papers, introduce the question before the dataset size. Site prevalence, a person's repeated encounters, and the fraction of that person's visits potentially visible to a tracker are different questions. Make the chosen unit the organizing idea of the paper.

## Explain the method as a sequence of meaningful operations

For a new signal, show trigger → observable change → attribution → identification. A small control example often explains attribution better than a long pipeline diagram. For a measurement, show source population → observations → mapping or join → reported quantity. Explain what the mapping adds and what it assumes.

For a defense, state the relationship it preserves. UniGL separates visual similarity from identical computation. Simulacrum separates user-visible state from page-readable state. WebGraph represents storage and sharing actions. Introduce the mechanisms as solutions to maintaining that relationship.

Use established technical terms and define them in context. Keep necessary distinctions—page scripts versus extension scripts, actual user events versus synthetic events, website counts versus visit counts—near the operation they explain. Move full API inventories and routine implementation detail to supporting material.

## Make each result paragraph advance the story

Write finding → decisive evidence → explanation → implication. A table should answer a question, and the following paragraph should explain the answer. Do not restate every cell.

For discovery papers, connect a representative case to breadth and then to additional coverage beyond earlier channels. For measurement papers, follow the main population trend with the subgroup or overlap that explains it. For defenses, connect protection to the observable signal, then discuss the functionality and cost needed to retain it.

Use the available adapted-attacker or component results to explain the mechanism. Simulacrum's remaining partial fingerprints and WebGraph's stronger mutation experiments show how residual signals refine the contribution. An exception can explain a boundary rather than become a sentence apologizing for the entire method.

## Keep details that determine what the result means

Name the counted object and comparison population: extensions, extension versions, fingerprints, people, domains, visits, requests, or organizations. State observation windows and separate later crawls from contemporaneous telemetry. Describe cooperation assumptions beside estimates that depend on shared data.

Use the verb that matches the evidence: a signal is observable, an extension is detectable, a visit is potentially exposed, or an identity is linked. Move between these levels only when the supplied results provide the connection. Sensitive-site visits motivate privacy consequences without proving a person's health status or beliefs.

Place sampling, consent and data handling concisely in methodology when human data is involved. Keep long country tables, complete property lists, and code listings in the appendix. Include functional breakage and timing populations in the main evaluation when they determine the defense's practical tradeoff.

## Write plainly and sell the useful difference

Prefer “observe,” “trigger,” “distinguish,” “link,” “hide,” “preserve,” and “estimate.” Avoid ornate phrases such as “pervasive privacy dystopia,” “seamless reality orchestration,” or “unprecedented protection.” A memorable system name does not need a metaphor in every paragraph.

State the positive result precisely. A new channel, additional coverage, a user-centered measurement, or a stronger privacy–functionality tradeoff can be a substantial contribution. Use “suggests” for an explanation not isolated by the experiment. Describe historical browser behavior as historical; this corpus is a source of writing craft, not current browser compatibility advice.

## Resources

- [Writing playbook](references/playbook.md): story forms, result paragraphs, and detail choices.
- [Worked example](references/worked-example.md): a draft from fictional supplied results.
- [Ten source papers](references/corpus.md) and [BibTeX](references/references.bib).

Borrow argumentative moves, not source sentences. Cite a paper in the manuscript when it supplies relevant prior work, a method, or evidence; writing inspiration alone does not require a technical citation.
