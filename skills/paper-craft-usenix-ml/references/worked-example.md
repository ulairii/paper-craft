# Worked example: explaining a defense from supplied experiments

This example is fictional. The method, numbers, and provisional name below illustrate writing; they are not findings from the reference papers. Bracketed items are missing facts to obtain from the author. The prose borrows the interaction-oriented explanation of [FLAME](papers/P07.md), the diagnosis-to-design progression of [PatchGuard](papers/P06.md), and the differentiated interpretation of [ML-Doctor](papers/P10.md).

## Supplied material

The author describes a federated-learning defense, provisionally called UpdateFilter. It filters updates by their direction, clips the retained updates, and adds noise to the aggregate. The server observes individual updates, clients have equal weight, and fewer than half the participating clients are compromised. The supplied experiments use one image-classification dataset and three targeted poisoning attacks, with results averaged over five runs. Exact attack names, model, client count, noise settings, variability, and selection procedure are missing.

| Setting | Attack A success | Attack B success | Attack C success | Ordinary accuracy |
|---|---:|---:|---:|---:|
| No attack, no defense | — | — | — | 84.0% |
| Attacks, no defense | 92.0% | 88.0% | 74.0% | 83.8% |
| Filtering only | 20.0% | 36.0% | 49.0% | 83.1% |
| Noise only | 4.0% | 7.0% | 12.0% | 74.5% |
| Full defense | 3.0% | 5.0% | 9.0% | 82.4% |

Ordinary accuracy in the attacked rows is the supplied mean across the three attack settings. A separate adaptation experiment, for Attack B only, aligns malicious updates with benign directions. Success rises from 5.0% to 18.0%; ordinary accuracy is 81.9%. Server processing is 0.8 seconds per round without the defense and 1.1 seconds with it. No theorem, privacy guarantee, multi-dataset experiment, or end-to-end latency measurement is supplied.

## Draft

### Title

Coordinating Update Filtering and Noise for Federated Backdoor Defense

### Abstract

Targeted poisoning can change a federated model's behavior on attacker-chosen inputs while preserving ordinary accuracy. Filtering unusual updates leaves some malicious contributions in the aggregate, whereas suppressing them with noise can damage the main task. We study a defense that combines directional filtering, clipping, and aggregate noise to reduce this tension. On [dataset and model], the combined defense lowers success of three evaluated attacks from 92%, 88%, and 74% to 3%, 5%, and 9%, respectively. Its mean ordinary accuracy is 82.4%, compared with 74.5% for noise alone and 84.0% in the unattacked reference setting. An adaptation that aligns malicious updates with benign directions increases one attack's success to 18%, showing the remaining dependence on update separation. These results support coordinating the interventions to retain more task accuracy at low attack success in the studied setting.

### 1. Introduction

Federated training gives clients control over the updates submitted to a shared model. A compromised client can use that control to introduce targeted errors while retaining ordinary predictions. The resulting update may be harmful even when its main-task accuracy appears normal. A defense therefore needs to limit the malicious contribution without discarding the information that makes collaborative training useful.

Two direct responses illustrate the difficulty. Filtering can remove updates whose direction differs from the main group, but less distinctive updates may remain. Adding noise can suppress remaining contributions, but excessive noise also damages useful information. Our experiments exhibit both behaviors: filtering alone leaves substantial attack success, while noise alone lowers ordinary accuracy.

UpdateFilter combines directional filtering, clipping, and aggregate noise. Its rationale is that the earlier interventions reduce the contribution the final intervention must suppress. This rationale follows the interaction-oriented approach explored by FLAME [P07]; the present draft must establish its own technical difference through [the author's specific new mechanism or finding relative to FLAME and other relevant methods]. Combining these ingredients alone is not sufficient to establish novelty.

We evaluate whether the combined intervention improves the observed balance between targeted attack success and ordinary accuracy. Across three attacks on [dataset], it retains substantially more accuracy than the noise-only variant while obtaining lower attack success. A separate alignment experiment identifies a remaining weakness when malicious updates resemble benign ones more closely.

### 2. Setting and defense

The server receives individual updates from [number] clients per round and assigns each client equal aggregation weight. The attacker controls [fraction] of participating clients, below one half, and seeks to induce [targeted behavior] while retaining ordinary accuracy. The evaluation uses [attack names, attacker knowledge, and training budget]. These conditions define the setting in which the results below apply.

UpdateFilter first compares update directions and retains [selection rule]. It then clips retained updates using [clipping rule] and adds [noise distribution and scale] to their aggregate. Directional filtering targets contributions that differ from the main group; clipping bounds the magnitude of those that remain. The noise stage acts on the resulting aggregate. Figure [number] should illustrate these operations with the same example used to explain the attacker.

The mechanism is empirical in this study. We do not derive a certificate that all permitted malicious updates are suppressed. The experiments instead examine the complete outcome and compare it with variants that retain only filtering or only noise. They do not separately isolate the contribution of clipping.

### 3. Evaluation

We run each setting five times on [dataset and architecture] and report mean attack success and ordinary accuracy. Attack success is [precise target-input denominator]; ordinary accuracy is measured on [held-out population]. Table 1 reports each attack separately and averages ordinary accuracy across the three attacked settings. Report [run-to-run variability] alongside these means in the final table.

**The combination retains more ordinary accuracy at low attack success.** Without defense, the attacks succeed on 92%, 88%, and 74% of their target inputs. UpdateFilter reduces these rates to 3%, 5%, and 9%, with mean ordinary accuracy of 82.4%. Relative to the unattacked reference, this is a 1.6 percentage-point accuracy loss. The result demonstrates a useful operating point for these attacks rather than complete removal of targeted behavior.

**The variants explain why the combination is useful.** Filtering alone retains 83.1% ordinary accuracy but leaves attack success between 20% and 49%. Noise alone reduces success to between 4% and 12%, at an ordinary accuracy of 74.5%. The full defense retains 7.9 percentage points more accuracy than noise alone and reduces attack success further in all three settings. These comparisons support the rationale that the interventions work better together. A separate clipping ablation would be needed to assign the gain among the individual stages.

**Alignment exposes a remaining dependence on update direction.** When Attack B is adapted to align malicious updates with benign directions, its success rises from 5% to 18%, while ordinary accuracy is 81.9%. The change indicates that the original result depends partly on separation in update space. It also shows why the adapted outcome belongs beside the main result: low attack success under the original construction does not describe every use of the attacker's control.

**Server processing adds 0.3 seconds per round.** The measured operation takes 1.1 seconds with UpdateFilter and 0.8 seconds without it. This is a server-side processing measurement; total training time additionally depends on client computation, communication, and the number of rounds. The supplied results do not determine that end-to-end cost.

### 4. Related work

FLAME [P07] coordinates filtering, clipping, and noise for federated backdoor defense. Local Model Poisoning [P05] studies accuracy degradation through crafted client updates, illustrating a different attacker objective from the targeted behavior evaluated here. PatchGuard [P06] concerns localized adversarial image patches rather than federated updates; it exemplifies a different defense setting in which bounding corruption and limiting its aggregate influence are connected explicitly.

The final related-work section should explain [the actual algorithmic or empirical distinction from the closest federated defenses]. It should cite additional papers required by the author's method, rather than treating this writing corpus as an exhaustive literature review.

### 5. Discussion and conclusion

The experiments support a specific conclusion: coordinated interventions retain more ordinary accuracy than the evaluated noise-only variant at lower success rates for the three tested attacks. The aligned adaptation leaves more residual success, identifying update separation as a condition deserving further study. The current evidence comes from one dataset and an aggregation server that sees individual updates.

The resulting contribution is an empirical account of the tradeoff and its mechanism. Broader deployment claims require additional settings, and a privacy claim would require its own definition and support. Within the studied setting, the full defense supplies a better observed operating point and the adaptation experiment clarifies where that benefit weakens.

## Reference keys used in the draft

- **P05:** [Local Model Poisoning Attacks to Byzantine-Robust Federated Learning](papers/P05.md), USENIX Security 2020.
- **P06:** [PatchGuard](papers/P06.md), USENIX Security 2021.
- **P07:** [FLAME](papers/P07.md), USENIX Security 2022.

Use the full entries in [references.bib](references.bib) when converting this illustration to a manuscript format. Preserve only technically relevant citations in the actual paper. A writing example cannot supply a missing research contribution.
