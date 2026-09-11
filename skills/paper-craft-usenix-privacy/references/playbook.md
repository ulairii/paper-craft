# Writing browser privacy and web measurement papers

The ten [source papers](corpus.md) offer several ways to make a privacy contribution persuasive. These are interpretations of the published arguments, not claims about the reviewers' reasons for acceptance.

## Start with what becomes visible

A strong opening gives the reader a small mechanism they can understand. In [Fingerprinting in Style](papers/P06.md), a stylesheet can be inaccessible while its effects remain visible. In [Human Touch](papers/P07.md), a translation extension becomes observable after text selection. Both openings make the missing observation dimension concrete before describing the collection pipeline.

Use that move when the contribution is a new signal. Write a short example with an actor, a permitted action, and an observable consequence. Then explain why the consequence distinguishes something that matters. Avoid beginning with a catalogue of APIs or a generic statement that privacy is important.

For a measurement contribution, make the question equally concrete. [When Sally Met Trackers](papers/P09.md) changes the perspective from websites containing trackers to users encountering them. A small site-count example can explain why those quantities differ: a tracker on one frequently visited site may see more activity than a tracker on many rarely visited sites. This observation earns the need for telemetry.

## Give each kind of evidence a role

| Evidence | Question it answers | Useful narrative move |
|---|---|---|
| Trigger and control | What causes the observation? | Walk through one informative case before scale. |
| Collection-wide measurement | How much of the defined population exhibits it? | Carry the filtering denominator into the result. |
| Comparison with existing signals | What does the new channel add? | Explain overlap and complementarity. |
| User or visit distribution | Who experiences the effect and how often? | Show heterogeneity after the aggregate. |
| Functional testing | What useful behavior remains? | Connect failures to the design boundary. |
| Adapted adversary | Which information survives the defense? | Use the residual signal to refine the explanation. |

The cross-device study [P01](papers/P01.md) demonstrates why these roles matter. A paired-device case, a matching experiment, downstream inference, and a reach estimate contribute different pieces of the argument. The manuscript is stronger when it gives each piece the right job instead of turning all of them into repeated claims of large-scale tracking.

## Explain the distinction that motivates the design

[Rendered Private](papers/P04.md) distinguishes visual equivalence from identical computation. [CloakX](papers/P05.md) distinguishes an extension's public identifiers from the behavior they support. [Simulacrum](papers/P08.md) distinguishes state visible to the user from state observable by a webpage. [WebGraph](papers/P10.md) distinguishes mutable resource properties from storage and sharing actions.

These distinctions are useful writing structures. State the two objects in ordinary language, explain why confusing them creates the problem, and describe the operation that separates or reconnects them. The design sections can then follow the decisions required to maintain that relationship.

A code example should preserve the relevant dependency. For sharing, show the identifier being read and transmitted. For an event, show the trigger and the change it causes. For a defense, show which observer receives which state. Omit setup code and unrelated API arguments. Put exhaustive variants in the appendix.

## Turn breadth into understanding

A large matrix becomes useful when rows and columns represent a reasoned taxonomy. The cookie-policy study [P03](papers/P03.md) relates request contexts to enforcement behavior and underlying causes. The reader learns where a policy is interpreted differently, where an implementation fails, and where an extension's interface limits what it can enforce.

Follow a broad table with two or three contrasts that explain it. Do not give every cell its own sentence. A common cause can connect many cases, while an exception can identify a different layer of responsibility. Describe what the taxonomy teaches before listing vendor responses or individual versions.

In ecosystem measurements, use overlap to explain marginal value. If two trackers see many of the same visits, combining their data adds less than their individual coverage suggests. The direction of the gain can differ: a smaller organization may gain substantially from a larger one while the reverse adds little. [P01](papers/P01.md), [P09](papers/P09.md).

## Write the interpretation, not a second table

A result paragraph can take this form:

> The new signal adds most coverage among extensions that remain inactive until a page event occurs. The passive baseline detects [X] extensions, while event-triggered observation adds [Y] previously missed cases. Inspection of [N] cases shows that the distinguishing change occurs only after [ACTION]. This supports adding that interaction to the observation model; it does not require replacing the passive detector.

This is an original template, not a source quotation. It combines a result with the mechanism that makes it interesting. Use the author's actual evidence and omit the inspection sentence if no such analysis exists.

For a defense, explain the residual cases. [Simulacrum](papers/P08.md) first evaluates the existing detector and then a detector adapted to remaining partial fingerprints. The change in protection rate identifies information still visible to the page. [WebGraph](papers/P10.md) shows that a representation can resist the motivating content mutations while facing a different tradeoff under more capable graph mutations. Both provide a useful structure: result, changed conditions, residual signal, implication.

## Choose details by the question they resolve

Keep a detail in the main paper if it changes the answer to “what did this experiment show?”

- A cohort's operating system and opt-in recruitment define the measured population.
- An eight-day observation window defines what “all encountered trackers” means.
- A later crawl changes direct observation into an estimate based on a temporal join.
- A browser-controlled action differs from one a webpage can generate.
- Functionality loss can explain why a defense's strong protection rate is not its whole contribution.
- An offline classifier's processing cost has a different meaning from a browser's interactive delay.

Move complete country lists, long property inventories, all wrapper functions, and secondary breakdowns later. Keep one example that explains why the detail exists. Appendices should deepen the argument rather than contain the only explanation of a central quantity.

## Use confident language with a clear object

| Vague or inflated | More informative |
|---|---|
| “We comprehensively unveil an alarming privacy landscape.” | “We measure how frequently the studied users encounter tracking organizations.” |
| “Our unprecedented fingerprint exposes every user.” | “The new signal distinguishes [N] extensions in the eligible collection.” |
| “The system seamlessly guarantees privacy.” | “The defense hides [SIGNAL] while preserving [TESTED FUNCTIONALITY].” |
| “The model understands tracking semantics.” | “The representation records storage accesses and shared identifiers.” |
| “The overhead is negligible.” | “The median delay is [TIME] in [POPULATION], with [FAILURES] affecting functionality.” |
| “The data proves that privacy causes security risk.” | “The measured groups differ in tracker exposure and vendor-assigned risk scores.” |

Technical precision need not make prose hesitant. State demonstrated findings directly. Use a short qualifying phrase for the population or observation boundary. Avoid stacking “may possibly potentially” when one accurate verb—such as “estimates”—already expresses the uncertainty.

## Build a draft from the evidence already supplied

Choose a title naming the new observation or protection mechanism. Write an abstract that gives the problem, insight, method, principal result, and practical consequence. Develop the introduction around one example and the gap it reveals. Explain the method through meaningful operations. Organize results around the contribution's questions, then discuss remaining scope and implications.

For missing information, use a factual placeholder such as `[CRAWL DATES]`, `[ELIGIBLE EXTENSION COUNT]`, or `[MEASURED FUNCTIONALITY]`. Continue writing the supported sections. Do not substitute a list of requested experiments for a manuscript the author asked to draft. The [worked example](worked-example.md) demonstrates this behavior.
