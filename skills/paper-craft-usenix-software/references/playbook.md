# USENIX Security software-security writing playbook

## Give the work a recognizable center

A system with several components still needs a single reason to exist. [QSYM](papers/P01.md) specializes execution for hybrid fuzzing. [ParmeSan](papers/P08.md) uses sanitizer checks as search targets. [FuzzGen](papers/P10.md) recovers API knowledge needed to generate drivers. State the changed decision in one sentence, then use the architecture to explain how that decision becomes practical.

A useful introduction progression is: concrete workflow → obstacle → observation → changed operation → demonstrated consequence. For a driver-generation paper, begin with the initialization sequence needed to enter a library. For an execution paper, begin with measured cost. For an allocation paper, begin with uneven yield across choices. The opening should make the eventual method feel motivated before its name appears.

A small example often does more than an abstract taxonomy. FuzzGen's decoder example preserves the steps and shared state while omitting low-level initialization details. [GRIMOIRE](papers/P05.md) makes coarse input structure intelligible through fragments that survive generalization. Use an example that reveals the missing information, then explain how the method obtains it.

## Sell the specific form of novelty

| Contribution | Persuasive emphasis | Closest useful comparison |
|---|---|---|
| A specialized component | A workflow permits a cheaper or more effective design | Same surrounding system, alternate component ([SymCC](papers/P06.md)) |
| Adaptive allocation | The useful choice changes across programs or search stages | Fixed policy and other simultaneous changes separated ([MOPT](papers/P02.md)) |
| Cooperation | Intermediate discoveries become useful to another search process | Same members without exchange ([EnFuzz](papers/P04.md)) |
| Reduced manual knowledge | Approximate inferred structure is sufficient for useful exploration | Expert-informed method and a complementary combination ([GRIMOIRE](papers/P05.md)) |
| Practical compatibility | Two requirements must hold together | Compatibility evidence plus execution measurements ([FIRM-AFL](papers/P03.md)) |
| New use of an existing signal | A familiar detector also changes where to search | Hold detection fixed and vary guidance ([ParmeSan](papers/P08.md)) |

These comparisons explain the papers' arguments. Use them to interpret available results, rather than require every manuscript to run every experiment. When the most direct comparison is absent, keep the observed gain and narrow the explanation.

## Explain why an experiment is in the paper

A throughput benchmark asks how much execution work a system can perform. A known-bug experiment asks how quickly a specified fault becomes observable. A new-bug campaign establishes practical usefulness on selected versions. An input-generation or dependency analysis asks what information the method obtains. Introduce each experiment with the question it answers, then explain the result in those terms.

[GREYONE](papers/P09.md) links inferred dependencies to byte prioritization and conformance-guided seed evolution. Its component comparisons give the intermediate representation a practical meaning. FuzzGen links the number of consumers to API breadth and graph complexity. These are stronger explanations than simply repeating that the overall system wins more table entries.

A result paragraph should select one comparison and explain its consequence. For example: “Sharing seeds improves the ensemble over the same members searching independently. The trace shows one engine producing an input that lets another pass the later check. This supports cooperation as a source of the gain.” Fill in the actual trace and measurements; do not invent them.

## Make exceptions useful to the story

A smaller gain on solver-heavy programs explains an execution optimization's scope. A manual driver that finds more bugs in one component explains the value of concentrated exploration. An ensemble member that works well on small binaries but poorly on large programs motivates a different composition. These findings can sharpen the contribution rather than be hidden in the appendix.

Distinguish an observed pattern from its proposed cause. A curve that flattens does not by itself prove a particular optimization failure. Write the plausible explanation and identify the experiment that directly tests it, if one exists. [SymCC](papers/P06.md) decomposes time; [FuzzGen](papers/P10.md) relates repeated decoder calls to state depth; ParmeSan varies the sanitizer used for guidance. Their explanatory comparisons make the interpretation concrete.

## Separate useful automation from claims of completeness

Automation has stages. A generated driver may still need crash triage; an inferred grammar need not express the full language; a reachability filter may defer useful inputs. Explain which human decision is automated and what information the system receives. This makes the practical improvement visible without requiring an impossible “zero knowledge” story.

[FuzzGuard](papers/P07.md) demonstrates why the timing protocol belongs near the result: replaying a recorded sequence measures avoided execution work, while a live feedback-driven campaign also changes which inputs appear next. Use that distinction to choose the right sentence. “The filter reduces processing time for these sequences” is a useful result with a clear subject and outcome.

## Decide what stays in the main text

Keep information that changes the method or comparison: source versus binary access, supported environment, initial valid inputs, supplied target locations, inherited backend, worker budget, and whether the cost includes preprocessing. Explain the kind of bug report counted. A list of CVEs can live in the appendix once the main text gives a representative discovery and an accurate aggregate.

Move routine instrumentation flags, full mutation inventories, large tables of target versions, and exhaustive API attributes to supporting material. A brief code listing should preserve the state transition or dependency needed for the argument. Avoid turning a method section into a build manual.

## Sentence choices

| Vague or inflated | More useful |
|---|---|
| We propose a novel holistic fuzzing framework. | We prioritize mutations using the input bytes that influence unexplored branches. |
| Our system seamlessly synergizes complementary engines. | Each engine shares coverage-increasing seeds with the other engines during search. |
| Our approach needs no knowledge and guarantees valid tests. | The generator infers API ordering and shared arguments from existing library consumers. |
| We find hundreds of vulnerabilities. | The campaign produces [crash count] reports, corresponding to [deduplicated count] faults and [confirmed count] confirmed vulnerabilities. |
| The ablation proves every module is indispensable. | Removing target selection increases time to the tested bugs, supporting its role in directing search. |
| More coverage proves better security. | The generated drivers reach additional API behavior; targeted manual drivers still find more bugs in some components. |

These are original illustrations. Use the author's actual mechanism, evidence, and terminology in the draft.
