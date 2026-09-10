# Worked example: make a localization result tell a story

This is a fictional drafting exercise inspired by the argument structure of [Cascade R-CNN](papers/P05.md), especially its introduction, Figure 1, and stage comparisons. The method description and numbers below are invented teaching inputs, not findings from that paper. Do not copy them into a real manuscript.

## Supplied material

An author has a detector with AP 40.0 and AP75 43.0. Raising the training overlap threshold gives AP 39.2 and AP75 42.6. Refining proposals before a stricter second stage gives AP 42.0 and AP75 46.1. The supplied experiment log says fewer examples meet the positive criterion when the threshold is raised directly. There is no runtime measurement or study of other datasets.

## Choose the story

A weak framing is “a new two-stage framework with superior detection performance.” It hides the informative result: the obvious attempt to improve localization fails. The stronger story is that stricter supervision needs proposals that can meet it. The stage is the implementation of that idea.

## Title

**Improving Proposals Before Tightening Localization Supervision**

This title names the design dependency. It does not invent a grand acronym or claim a general solution to detection.

## Abstract

Training a detector with stricter overlap requirements appears to be a direct way to improve localization, but it also reduces the number of positive training examples. In our experiments, raising the overlap threshold alone lowers both AP and AP75. We instead refine candidate boxes before applying stricter supervision in a second stage. On [dataset], this increases AP from 40.0 to 42.0 and AP75 from 43.0 to 46.1. The results suggest that improving the proposals supplied to stricter supervision is more useful than changing the threshold alone.

## Introduction opening

A detector can identify the correct object while placing its box imprecisely. Training with a stricter overlap threshold seems a natural response: it asks the model to prefer boxes that align more closely with the object. However, the same change reduces the number of proposals treated as positive examples. In our baseline, increasing the threshold lowers AP75 rather than improving it.

We address this mismatch by refining proposals before applying the stricter criterion. The first stage improves candidate boxes; the second learns from these improved candidates under tighter supervision. This ordering links the difficulty of the training task to the quality of the examples available to solve it.

## Method opening

The detector uses two prediction stages. The first operates on the initial proposals and outputs refined boxes. The second receives those boxes and uses a stricter overlap criterion to assign positive examples. The central change is therefore the input to stricter supervision, rather than the threshold in isolation. [Describe the supplied refinement operation and training objective here.]

This is enough to establish the idea before notation. The missing implementation cannot be reconstructed from three result rows and should remain a short placeholder until the author supplies it.

## Results paragraph

Raising the threshold alone reduces AP from 40.0 to 39.2 and AP75 from 43.0 to 42.6. Refining proposals before the stricter stage reverses this pattern, reaching 42.0 AP and 46.1 AP75. The larger gain at AP75 is consistent with improved localization. Together with the reduction in positive examples under the threshold-only change, these results motivate adapting proposal quality before tightening supervision.

## Why these choices help

The opening gives the failed alternative a purpose: it makes the proposed ordering necessary. The method paragraph explains the dependency before implementation. The results paragraph returns to the opening question instead of repeating that the method is effective. No claim about speed, cross-dataset generality, or optimal stage count is needed because none is part of the supplied evidence.

For an actual full-draft request, continue through related work, the complete supplied method, experimental setup, remaining results, and conclusion. This short example illustrates the central passages; it is not a reason to stop a requested manuscript after its introduction.
