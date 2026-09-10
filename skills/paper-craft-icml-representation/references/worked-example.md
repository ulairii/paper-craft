# Worked example: when a better pretraining loss is not a better representation

The study, method name, and findings below are fictional writing illustrations. They are not results reported by the source papers. Bracketed fields require the author's facts.

## Supplied material

An author observes that stronger view invariance lowers pretraining loss but harms a downstream task that depends on color. A modified head produces similar pretraining accuracy and better frozen-feature transfer. The author has a transformation-prediction diagnostic, two downstream datasets, and a small range of augmentation strengths.

## Find the story

The useful contribution is the separation of information needed by the pretraining objective from information needed downstream. “A new head improves accuracy” hides that insight. This framing borrows the explanatory use of the projection head from [SimCLR](papers/P01.md) and the metric-to-intervention sequence from [Alignment and Uniformity](papers/P03.md), without attributing the fictional findings to either paper.

## Possible title

Preserving Task-Relevant Information under Strong View Invariance

## Abstract passage

Self-supervised objectives encourage representations to ignore differences between augmented views. Some of those differences, however, may remain useful for downstream tasks. We study this tension by varying augmentation strength and measuring both pretraining performance and the information retained by the encoder. In [setting], stronger invariance improves [pretraining measure] while reducing [downstream measure]. We introduce [head design], which separates the features used for view agreement from those retained for transfer. With the same encoder and training data, the method improves [result] on [tasks]. The results suggest that the location at which invariance is imposed matters as much as its strength.

## Introduction transition

The pretraining objective rewards agreement between two views, but downstream prediction may require distinguishing information that those views do not share. This creates a mismatch between success on the training task and usefulness of the learned representation. Our initial experiments expose that mismatch: as [augmentation] becomes stronger, [proxy result] improves while [transfer result] declines. We therefore ask whether the model can satisfy the view-agreement objective without discarding the information needed for transfer.

## Method passage

The encoder maps an image to a representation used by the downstream classifier. A separate head maps that representation to the embedding on which the view-agreement loss is computed. Our change is [operation]. This allows [mechanism] while preserving [information] in the encoder output. The downstream task uses the encoder representation; the additional head is used only during pretraining.

This paragraph needs the actual operation and mechanism. Naming an intended effect does not substitute for explaining how the design implements it.

## Results passage

The largest benefit appears at the stronger augmentation settings, where the baseline's pretraining performance and transfer accuracy diverge. At [setting], the two methods obtain similar [pretraining measure], but the proposed head improves [transfer measure] by [difference]. The transformation-prediction diagnostic also recovers more [information] from the encoder representation. Together, these comparisons support the intended separation between view agreement and information retention. The smaller gain on [second task] suggests that the benefit depends on which discarded information the downstream task requires.

This is a finding–comparison–interpretation paragraph. It does not narrate every table row or claim that a diagnostic establishes every part of the mechanism.

## A concise scope paragraph

The study evaluates [augmentation family] and [task families]. It therefore establishes the tradeoff in these settings, while leaving other invariances and downstream uses open. The added head changes pretraining by [cost or operation]; inference uses the same encoder as the baseline.

## If the contribution were theory instead

Lead with the same observed mismatch, specify a simplified model, derive a prediction about retained information, and test that prediction. Use [Contrastive Inversion](papers/P08.md) for making assumptions and recovery meaning explicit, or [Stepwise Learning](papers/P10.md) for extending a simplified account through progressively more realistic observations. Do not invent a method or a performance win merely to fit an empirical-paper template.
