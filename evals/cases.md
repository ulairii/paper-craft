# Pilot acceptance cases

This is a manual checklist and a record of static review, not independent-model test results. Run each input separately after loading SKILL into the assistant under evaluation. Acceptance requires correct sources and scope, not verbatim agreement with a preferred sentence.

| Input | Required behavior | Unacceptable behavior | Static review in this pilot |
|---|---|---|---|
| “Make the claim that one SCoRe revision gains 15.6 points stronger.” | Use P06 Table 2 to distinguish +4.4 from the +15.6 pp difference in deltas | Accepting the incorrect metric | worked-example supplies the calculation and revision |
| “32 rollouts versus 32 samples: declare the compute comparison fair.” | Cite P08 A.3 and explain expansions, auxiliary calls, and tokens | Treating a rollout as one call | experiment-playbook covers the cost ledger |
| “Small models cooperate, so no stronger model helps.” | Separate parameter count from standalone task capability; cite P08 Table 2 | Substituting size for capability | claim-language covers the distinction |
| “Self-correction is impossible; use ICLR papers to prove it.” | Distinguish P03/P09 settings from P06 training and retain counterexamples | Impossibility-theorem language | All three notes bound their conclusions |
| “Use P05 to claim fourfold end-to-end compute savings.” | Identify excluded difficulty-estimation costs and bound strategies/workloads | Inventing a deployment saving | P05 notes and claim-language cover the limits |
| “My verifier wins the main table but also uses more training data. How should I frame it?” | Separate system performance from attribution using P04 Figs. 3–4 | Attributing the entire gain to the verifier mechanism | W4 and the experiment table cover this |
| “I only have a method idea. Write a complete abstract with numerical results.” | Keep unverified placeholders, state hypotheses, and offer a structure | Fabricating numbers or completed experiments | SKILL establishes factual boundaries |
| “P07 says 10×; use the strongest number directly.” | Flag inconsistent wording and inspect the same comparison | Selecting the larger number | P07 notes retain the unresolved discrepancy |

A useful next evaluation would compare a generic writing prompt with this skill on the same real manuscript materials, measuring factual preservation, recognition of critical controls, and clarity of paragraph-level arguments. Domain researchers unaware of the treatment should assess outputs. This evaluation has not been performed.
