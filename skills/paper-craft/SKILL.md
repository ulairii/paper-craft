---
name: paper-craft
description: Write research paper drafts from existing ideas, experiments, and results, or improve paper sections. Use when an author asks for a conference submission draft, story, abstract, introduction, methods, or results narrative. Select the relevant conference-and-subfield writing skill from the included catalog, then produce the requested writing.
---

# paper-craft

Turn the author's material into clear, compelling research writing. This is the shared entry point for the specialized writing skills in this collection.

## Understand the request from the available material

Identify the target conference, the research topic, and the requested output. Read the material the user provides or identifies: method descriptions, existing prose, result tables, figure captions, and experiment summaries. Infer the topic from what the work contributes, not merely a dataset or model name.

The user should not have to choose a skill or fill in a classification form. If a distinction would materially change the draft and the material cannot resolve it, ask one focused question while continuing useful writing. If no material is supplied or locatable, ask for the method and results; do not invent a paper from a conference name alone.

Respect an explicitly requested skill or writing style. If a named skill is unavailable, say so briefly and use the closest appropriate writing guidance.

## Select the writing guidance

Read [the catalog](references/catalog.md). It lists available skills, their scope, and paths. Resolve paths relative to the catalog file, not the user's working directory.

- **Conference and topic match:** Load that skill's `SKILL.md`, then only the references relevant to the deliverable. Give research-topic fit more weight than an isolated keyword.
- **Several topics match:** Choose the skill that fits the paper's central contribution as primary. Borrow a specific lesson from a secondary skill only when it helps a distinct part of the paper. Keep one coherent story and terminology.
- **Topic matches but conference differs:** Keep the user's target conference. The neighboring skill can supply topic-specific writing lessons, but describe it as a cross-conference reference rather than a matching venue skill.
- **No relevant specialist:** Use [general writing guidance](references/general-writing.md) and keep writing. A shared conference alone is insufficient to choose an unrelated specialist. Do not imply that a matching curated corpus exists.
- **A listed skill cannot be opened:** Treat it as unavailable and use the remaining appropriate guidance. Do not ask the user to repair an installation before doing useful writing.

Mention the selected guidance in at most one short sentence when useful. Do not return a routing report. Once selected, move into the writing task rather than repeatedly classifying the work.

## Write a full draft when a full draft is requested

For a request such as “I am submitting to ICLR; write a draft from my existing results”:

1. Find the central insight in the method and results. Choose the story that best connects what is difficult, what changes, and what the experiments teach.
2. Arrange the manuscript around that story. Use a suitable structure for the contribution; method papers and analytical studies need not share the same outline.
3. Produce the draft itself: a working title, abstract, introduction, appropriate background or related work, approach or study design, experiments with result interpretation, and a conclusion. Integrate a short discussion where it helps. Do not stop after an outline unless the user requested one.
4. Preserve supplied results and scientific meaning. Use brief local placeholders for missing values, citations, or descriptions. Draft supported sections fully rather than filling the whole manuscript with generic scaffolding.
5. Follow the existing manuscript format or the user's requested format. When neither is specified, use Markdown. If the user requests a file or is working in an identified paper directory, save the draft there under a clear filename without overwriting unrelated material.

For a section rewrite, title request, or sentence edit, deliver that smaller output directly. Do not impose the full-draft workflow on it.

## Keep the experience focused on writing

Use familiar, precise words; stable technical names; intuition before notation; and paragraphs that move from a point to its explanation and implication. Let experiments answer reader questions and explain the important comparisons instead of narrating every table cell.

Preserve the author's emphasis and supported conclusions. Missing details can remain placeholders; they should not automatically trigger a reproducibility audit or a prerequisite experiment plan. Follow the specialist's writing lessons without turning the task into peer review.

Lead with usable prose or the draft artifact. Add only a short explanation of major writing choices when helpful. Source papers inform the writing craft; cite them in the manuscript only when they also support its scientific discussion.
