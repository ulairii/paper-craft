# Try paper-craft

First ask your assistant to read `skills/paper-craft/SKILL.md` from your clone, or invoke the installed `paper-craft` entry point. It selects the writing guidance from your target conference and material; you do not need to name a specialist.

## Write a full submission draft

```text
I am submitting to ICLR. Write a full draft from the method description
and experiment results in these files. Find the central insight and make
the experiment section explain it. Use plain academic English and save
the manuscript as draft.md. Keep brief placeholders for missing details.

[Paths to the method description and results]
```

The entry point infers the research topic from the files. It loads a matching specialist when available and uses general guidance otherwise. The output should be a manuscript draft, not only a proposed outline.

## Find the story

```text
Here is my method and the main result. Suggest two ways to frame the paper,
explain which is more compelling, and draft an introduction outline.
Focus on the insight a reader should remember.

[Method and results]
```

## Improve an introduction

```text
Rewrite this introduction so the problem leads naturally to the method.
Use familiar, precise words. Keep the technical terms consistent and give
each paragraph one clear purpose. Preserve my claims and emphasis.

[Introduction]
```

## Make a method easier to understand

```text
Rewrite this method section with intuition before equations.
Explain each component by its role before introducing its acronym.
Keep the technical content, but make the design easy to follow.

[Method section]
```

## Turn tables into a results narrative

```text
Use these tables to draft the experiment section. Organize it around
what each experiment teaches about the method. Explain the most informative
comparisons without reading every table cell aloud.

[Tables and brief descriptions]
```

## Remove awkward academic prose

```text
Edit this paragraph for clear academic English. Remove inflated wording,
unnecessary synonyms, and vague transitions. Return the revised paragraph
and briefly explain the two most useful changes.

[Paragraph]
```

## Write titles and an abstract

```text
Give me three titles: one naming the mechanism, one emphasizing the finding,
and one emphasizing the problem. Choose the strongest and write an abstract
that makes the central insight clear before the implementation details.

[Idea, method, and main findings]
```
