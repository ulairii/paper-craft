---
name: paper-craft-iclr-representation
description: Draft and revise ICLR representation-learning papers from methods and existing experiments. Distills ten accepted papers on information objectives, graph learning, contrastive negatives, collapse, masked pretraining, and language-image alignment into contribution framing, experimental narratives, and clear academic prose.
---

# Write an ICLR representation-learning paper

Write the manuscript the author requested. For a full draft, produce section prose with concise placeholders for missing facts. Use the results to identify a learning insight, explanatory finding, or useful capability, then build the paper around it.

## Choose the argument that fits the contribution

| Main contribution | Central question | Sources |
|---|---|---|
| Information or supervision design | What useful signal does the existing objective miss? | [DIM](references/papers/P01.md), [DGI](references/papers/P02.md), [DeCLIP](references/papers/P10.md) |
| Training objective | What tension or unwanted behavior does the objective address? | [Hard Negatives](references/papers/P03.md), [VICReg](references/papers/P05.md) |
| Scientific explanation | What observation contradicts the expected behavior, and what explains it? | [Dimensional Collapse](references/papers/P06.md) |
| Scale or efficiency | Which useful setting becomes feasible, and at what quality? | [BGRL](references/papers/P04.md), [FILIP](references/papers/P09.md) |
| Masked or local representations | What should the model predict, and what information does that teach? | [BEiT](references/papers/P07.md), [iBOT](references/papers/P08.md) |

Competitive accuracy can support a contribution about a clearer objective or a more useful interface. An explanatory paper can contribute a finding even when its resulting algorithm is not the strongest baseline. Do not force either into a leaderboard story.

## Explain the learning problem before the machinery

Identify the inputs, the supervision available during pretraining, and the representation used downstream. Distinguish encoder features from projection embeddings and local tokens from global summaries. Use one concrete example to explain which two things are being aligned or predicted.

Describe each loss term through its job. In a combination, explain why the terms belong together: class-level agreement may supply semantics while masked prediction teaches local structure. Name inherited components and state the change that matters. Repeating an established loss with new symbols does not clarify novelty.

For theory, start with the phenomenon. State the simplified setting, the mechanism it reveals, and the prediction that can be examined. Keep the assumptions needed to understand the result in the main explanation; place extended proofs in supporting material.

## Turn results into an argument

Choose the leading experiment to match the contribution. Use transfer for useful features, local probes for local representations, quality–resource curves for efficiency, or controlled dynamics for an explanation. Then explain the comparisons already present in the author's results. Drafting should not become an open-ended experiment checklist.

Give each result paragraph a finding, a revealing comparison, and an implication. A table need not be narrated cell by cell. Explain disagreements between metrics when they reveal what a representation retains: better reconstruction, less collapse, stronger linear probes, and better full fine-tuning are different outcomes.

For a combination, say whether the ablation adds components in sequence or independently tests their effects. For a scale story, explain the change of regime, including a move from frozen features to semi-supervised training. Use selected examples to illustrate the quantitative finding rather than replacing it.

## Keep the details that change the meaning

State whether evaluation is zero-shot, frozen-feature, or fully fine-tuned. Keep auxiliary tokenizer data, label use, model size, and important protocol changes next to the results they qualify. Define whether savings concern distinct examples, labels, encoder passes, memory, or time.

Move full schedules, prompt inventories, secondary sweeps, and routine architectural constants to setup or appendices. A detail belongs in the main story when it explains why the method works or changes what the result means. Explain it once, where readers need it.

## Write the contribution in ordinary English

Prefer concrete verbs: “align,” “predict,” “preserve,” “reduce,” “separate,” and “reuse.” Use standard terms such as “dimensional collapse” when you define the phenomenon. Avoid unusual synonyms and phrases such as “holistic semantic synergy,” “unprecedented representational prowess,” or “universally optimal features.”

Replace “better representations” with the demonstrated capability. Replace “free” with the actual saved operation. “Does not require normalization” and “uses no normalization in the reported configuration” mean different things. Decorrelation is not automatically independence; an illustrative attention map is not a localization guarantee.

Sell the strongest supported insight confidently. Use a mixed result to define where the method is useful, not as a reason to hide the contribution under qualifications. Preserve the scientific difference between a measured finding and the proposed explanation for it.

## Resources

- [Writing playbook](references/playbook.md): story structures and experiment interpretation.
- [Worked example](references/worked-example.md): connected manuscript prose from a fictional result set.
- [Ten source papers](references/corpus.md) and [BibTeX](references/references.bib).

Borrow argumentative moves, not source sentences. Cite these papers in a manuscript when scientifically relevant; they are not a mandatory related-work list. This corpus concerns transferable representations. Sample synthesis and LLM inference-time reasoning call for their own primary specialists when they carry the contribution.
