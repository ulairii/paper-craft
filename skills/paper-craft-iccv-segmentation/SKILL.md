---
name: paper-craft-iccv-segmentation
description: Write and revise ICCV segmentation papers from existing methods and results. Distills ten accepted papers on spatial decoding, structured refinement, efficient context, query-based masks, open-vocabulary transfer, and promptable segmentation into narrative and experiment-writing guidance.
---

# Write an ICCV segmentation paper

Turn the supplied method and results into the requested manuscript prose. Choose the argument that explains what changes about producing, identifying, or using a mask. For a full-draft request, write the draft and use concise placeholders for missing facts.

## Choose the story from the contribution

| Central contribution | Organizing question | Sources |
|---|---|---|
| Spatial decoding or refinement | What spatial information is lost, and how is it recovered? | [Deconvolution](references/papers/P01.md), [CRF-RNN](references/papers/P02.md), [Mask R-CNN](references/papers/P03.md) |
| Efficient context | How does information reach a pixel, and what representation makes that affordable? | [CCNet](references/papers/P04.md), [EMANet](references/papers/P05.md) |
| Query or transformer masks | What does the shared representation already provide, and what must the mask head add? | [QueryInst](references/papers/P06.md), [Segmenter](references/papers/P07.md) |
| Open-vocabulary segmentation | Is the bottleneck finding regions, naming them, or preserving transfer during adaptation? | [MasQCLIP](references/papers/P08.md), [DeOP](references/papers/P09.md) |
| Promptable segmentation | What counts as a valid response, and how does that definition shape model and evaluation? | [Segment Anything](references/papers/P10.md) |

Begin with the consequence the reader can recognize: a fragmented object, a shifted boundary, an unseen region with no proposal, or a valid mask penalized by a single annotation. Move from that consequence to the proposed principle. Avoid starting with a stack of acronyms.

## Explain the operation at the right scale

For an iterative method, explain one update before the unrolled network. CRF-RNN maps mean-field inference into neural operations; EMANet explains assignments, basis updates, and reconstruction. Define the intermediate representation by what it means, then introduce its notation.

For attention, follow information through the model. CCNet's two-hop path is clearer than saying it captures “rich global dependencies.” A compact basis, a query slot, and a class embedding have different meanings; name the actual role.

For open-vocabulary methods, explain proposal coverage separately from region classification. MasQCLIP improves both, whereas DeOP focuses on making the one-pass classification stream effective. “Better features” is too vague to connect these changes to the problem.

For a broad system contribution, make its parts necessary to one another. SAM's promptable task requires ambiguity-aware outputs and fast interaction; these support collecting the data that trains the model. This is a coherent story even though it includes more than one artifact.

## Let the experiments answer the opening question

Build the results narrative around the relevant distinction: local detail versus whole-image context; post-processing versus joint learning; connectivity versus cost; encoding versus decoding; seen-class adaptation versus novel-class transfer; annotation agreement versus prompt validity.

Explain comparisons in that order. A simple strong baseline is valuable: Segmenter's linear decoder reveals what the encoder already achieves. QueryInst's component combinations show why parallel supervision and dynamic mask heads work together. DeOP's unsuccessful simple baseline explains why the added mechanisms are needed.

Use breakdowns to explain the result. Object size can expose the effect of patch resolution. Base and novel categories reveal adaptation tradeoffs. Number of prompts reveals when ambiguity matters. Avoid repeating every table cell or ending every paragraph with “demonstrating effectiveness.”

When evidence is limited to aggregate scores, write a clear aggregate finding. Do not invent a mechanism experiment, human study, or favorable subset. Keep a proposed explanation distinct from a measured observation without turning the draft into an audit.

## Make detail earn its place

Keep spatial alignment, mask targets, query identity, prompt source, and the training/inference distinction when they define the idea. Keep the evaluation setting beside the result: base–novel and cross-dataset transfer differ; one CLIP pass can coexist with a separate proposal backbone; a fast prompt response can exclude image encoding.

Move routine schedules and layer lists to a compact setup paragraph or appendix. Place an equation beside its operational explanation. Include a small design choice when it changes the logic, such as which mask receives the training loss or which parameters stay frozen during transfer.

## Sell a clear contribution in ordinary English

Prefer “restore boundary detail,” “refine pixel assignments,” “reuse the image embedding,” “classify proposed regions,” and “reduce attention cost.” Avoid “holistic semantic synergy,” “unprecedented mask intelligence,” and ornamental substitutes for common technical words.

Be explicit about the output: class labels, class-agnostic regions, instance masks, or prompt-conditioned masks. “Universal” should name the demonstrated tasks and training arrangement. A proposed extension is not an evaluated result.

Mixed results can strengthen the explanation. Deconvolution and FCN make different errors; Segmenter acknowledges sharper CNN boundaries; MasQCLIP trades some base accuracy for novel coverage; SAM's benefit narrows with more prompts. State the useful regime confidently instead of forcing every metric into a universal-win story.

## Resources

- [Writing playbook](references/playbook.md): paragraph construction and evidence choices.
- [Worked example](references/worked-example.md): a draft from hypothetical open-vocabulary results.
- [Ten source papers](references/corpus.md), [individual notes](references/papers/P01.md), and [BibTeX](references/references.bib).

Borrow the reasoning behind the presentation, not the source wording. Cite source methods in the manuscript when scientifically relevant; the corpus is a craft reference, not a mandatory related-work list.
