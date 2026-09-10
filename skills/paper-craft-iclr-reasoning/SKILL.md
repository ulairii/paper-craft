---
name: paper-craft-iclr-reasoning
description: Plan, draft, or critique ICLR papers on LLM reasoning and test-time computation using evidence distilled from 10 accepted ICLR papers. Use for narratives, contribution framing, experiment design, result interpretation, and claim calibration involving sampling, search, verification, decomposition, or self-correction.
---

# ICLR LLM reasoning and test-time compute

Organize research facts into testable arguments. Stronger wording does not create a stronger contribution, and lessons from this corpus are not ICLR acceptance rules.

## Read first

1. Read the [corpus and scope](references/corpus.md) to establish this skill's coverage.
2. For narratives, outlines, or introductions, read the [writing playbook](references/writing-playbook.md). For experiments or results, read the [experiment playbook](references/experiment-playbook.md). For language revision, also read the [claim-language guide](references/claim-language.md).
3. Read at least two paper notes relevant to the claim: sampling P01; decomposition P02; self-correction P03/P06/P09; verification P04/P07/P08; budgets P05/P07/P08; applicability P10. Do not force irrelevant citations to meet a citation count.
4. For a complete demonstration, read the [SCoRe worked example](references/worked-example.md). Source page references use PDF page order for the recorded version.

## Establish factual boundaries

Extract the task, model and version, training/test data, intervention, feedback source, inference budget, completed results, and unknowns from the user's materials. Distinguish training rewards, verifiers actually available at test time, and test-answer oracles. Use `[to be provided]` for missing information while continuing structural work that does not depend on it. Never invent numbers, experiments, citations, or novelty.

Start with one sentence: under **conditions C**, address **failure F** using **mechanism M**, with **evidence E** supporting **claim H**. If F has not been observed, label it a hypothesis to test rather than an established finding.

## Execute by task

- **Narrative/outline:** Build the chain from problem to specific gap, diagnosis, mechanism, validation, and limits. Choose a methodological, analytical, or negative-result contribution; do not force an analytical paper to invent a method. Assign each paragraph a reader question and supporting evidence.
- **Experiment design:** Provide the claim, competing explanation, critical control, metric/figure, cost definition, and narrower conclusion if the test fails. Prioritize explanations that could overturn the central claim. Separate necessary evidence from optional extensions.
- **Result interpretation:** State the measurement, discuss possible mechanisms, explain what controls rule out, then identify remaining alternatives. Separate aggregates from difficulty slices, coverage upper bounds from deployable selection, and correlation from causation.
- **Revision:** Preserve facts, comparators, and conditions; provide revised prose and reasons for material changes. When evidence is missing, narrow the claim or identify the required experiment. English examples are newly written prose, not source quotations.

## Required checks

1. Does “self-correction” report first/later attempts, incorrect→correct and correct→incorrect transitions, and their denominators?
2. Does “efficient” account for auxiliary models, tokens, expansions, difficulty estimation, and offline training? If only calls were measured, limit the claim to calls.
3. Does “better verification” fix candidates? Does “better search” fix the selector? When training data differ, is there a separate controlled attribution experiment?
4. Has “smaller model” become “weaker model,” or “no fine-tuning” become “no additional resources”?
5. Do “optimal,” “general,” “guaranteed,” or “first” exceed the strategy set, evaluated models/tasks, theoretical assumptions, or novelty evidence?
6. Are conclusion-changing details—prompts, answer parsers, stopping rules, and test splits—hidden in appendices?

## Output contract

Deliver the requested prose, outline, or experiment table at the requested length, with a short evidence note distinguishing user facts, this skill's recommendations and their paper/section/figure sources, and unverified items. Include only substantively relevant citations in the paper itself. Writing-method sources can appear in a separate review note instead of cluttering related work.

Trace references and numbers through [corpus.json](references/corpus.json) and the individual notes. Check inconsistent source statements rather than selecting the most favorable result. The local text is sufficient to use the skill without downloading all PDFs; exact quotations or facts outside the notes require checking the source again.
