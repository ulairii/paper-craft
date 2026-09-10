# Writing example: make a two-stage method feel motivated

Source: [SCoRe — Training Language Models to Self-Correct via Reinforcement Learning](papers/P06.md), ICLR 2025. This example studies how the paper connects a desired behavior, diagnoses, a training design, and experiments. All sample prose below is original, not quoted from the authors.

## Find the story behind the components

A description such as “a two-stage RL framework for self-correction” names the machinery. The more useful story starts with the behavior: a model should repair wrong answers while retaining correct ones.

SCoRe then distinguishes two difficulties. Offline training can expose the model to errors different from its own; online training can still collapse into unhelpful revision behavior. These diagnoses give the training stages a purpose before their objectives are introduced (Sections 4–5, Figs. 3–6). Appendix Fig. 11 makes the design logic explicit.

The writing lesson is to make the reader want the mechanism before explaining its implementation.

## Turn that insight into an opening

**Before**

> We propose a novel and effective two-stage reinforcement learning framework to enhance the self-correction capabilities of large language models.

**After**

> A model that revises its answer must learn both when to change it and what to change. We train these behaviors in two stages: first improving revision, then jointly optimizing the initial answer and its correction.

The revision replaces adjectives with the problem and the design rationale. It introduces the stages through their roles. The technical details can now answer a question the reader understands.

This is a short conceptual opening, not a complete account of SCoRe's objectives. A full method description would next explain the first-attempt constraint and progress-based reward shaping.

## Give the introduction a progression

| Paragraph | Reader's question | Writing move |
|---|---|---|
| 1 | Why is revision a distinct capability? | Explain fixing mistakes and preserving correct answers. |
| 2 | Why is learning that behavior difficult? | Introduce the mismatch between fixed training errors and the model's own errors. |
| 3 | Why is the obvious remedy insufficient? | Explain that online training alone can still yield unhelpful revision behavior. |
| 4 | What is the insight behind the method? | Give each stage a role in learning useful revision. |
| 5 | What should I remember from the results? | Explain the revision gain and what the component comparisons reveal. |

This progression is an outline for this particular story, not a requirement that introductions always contain five paragraphs.

## Write a transition that carries the reasoning

**Before**

> Existing methods suffer from several limitations. To overcome these challenges, we propose a two-stage framework.

**After**

> Training on the model's own attempts addresses the mismatch in training errors, but it does not by itself encourage useful revisions. We therefore first train the model to improve its second attempt before jointly optimizing both attempts.

The revised transition names what the first remedy accomplishes and what remains. “Therefore” has an actual connection to express. This paraphrases the motivation across Sections 4–5; the source contains the full training formulation.

## Explain the method through its roles

A useful method-section order is:

1. Explain the two-attempt interaction.
2. Introduce why first-attempt behavior matters during revision training.
3. Explain Stage I's constraint and second-attempt objective.
4. Explain the move to joint optimization and progress-based shaping in Stage II.
5. Present the equations and operational details alongside the roles they formalize.

This lets the explanation prepare readers for the notation. Starting with two objective equations and only later explaining why there are two stages reverses that teaching order.

## Make the experiments complete the story

The most useful question is what the second attempt contributes. Table 2 reports SCoRe's MATH accuracy rising from 60.0% to 64.4%. The same table separates corrections from regressions. Table 4 then examines the training components.

A result paragraph can say:

> SCoRe improves answers through revision. On the reported MATH evaluation, accuracy rises from 60.0% on the first attempt to 64.4% on the second. Corrections outnumber regressions, showing that the second attempt contributes beyond the stronger initial answer. The component comparisons then examine how the training stages support this behavior.

The paragraph selects the numbers needed for its point and explains their meaning. It leaves other comparisons in the table instead of repeating every cell. The first-to-second gain is 4.4 percentage points; other reported improvements use different comparisons and should retain their own labels.

## What to borrow for another paper

Borrow the sequence: desired behavior → specific difficulty → why a simple remedy is insufficient → motivated design → experiments that explain the behavior. Use it only when it fits the author's actual work. Keep the idea, vocabulary, and emphasis specific to that work; the value lies in the reasoning between paragraphs, not in copying SCoRe's surface wording.
