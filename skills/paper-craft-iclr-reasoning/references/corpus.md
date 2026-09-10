# ICLR reasoning / test-time compute pilot corpus

All 10 papers were formally accepted at ICLR, spanning 2023–2025 rather than a single conference year. Selection reflects representative mechanisms, useful controls, and transferable argumentation—not citation-count rankings or a claim that every paper won an award. The corpus covers sampling, decomposition, verification, revision, search, compute allocation, and negative results. It remains a cluster of related topics; any future independently released subtopic skill must itself have at least 10 papers from the same conference.

All 10 main texts and the selected appendices listed in the individual notes have been read. This does not imply reading every appendix, running author code, or auditing proofs. P01/P02 use pinned accepted author versions with ICLR publication headers; the remaining papers use official proceedings PDFs. File hashes, retrieval timestamps, and reading coverage are recorded in [corpus.json](corpus.json).

| ID | Paper / year | Selection rationale and reading notes |
|---|---|---|
| P01 | [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://openreview.net/forum?id=1PL1NIMMrw) · 2023 | [Sampling and aggregation: explain a minimal change through its mechanism](papers/P01.md) |
| P02 | [Least-to-Most Prompting Enables Complex Reasoning in Large Language Models](https://openreview.net/forum?id=WZH7099tgfM) · 2023 | [Decomposed reasoning: define easy-to-hard generalization before claiming scalability](papers/P02.md) |
| P03 | [Large Language Models Cannot Self-Correct Reasoning Yet](https://proceedings.iclr.cc/paper_files/paper/2024/hash/8b4add8b0aa8749d80a34ca5d941c355-Abstract-Conference.html) · 2024 | [Negative results: organize the paper around confounding factors](papers/P03.md) |
| P04 | [Let's Verify Step by Step](https://proceedings.iclr.cc/paper_files/paper/2024/hash/aca97732e30bcf1303bc22ac3924fd16-Abstract-Conference.html) · 2024 | [Verifier supervision: separate best achievable performance from controlled attribution](papers/P04.md) |
| P05 | [Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/hash/1b623663fd9b874366f3ce019fdfdd44-Abstract-Conference.html) · 2025 | [Test-time compute: frame allocation insights while accounting for decision costs](papers/P05.md) |
| P06 | [Training Language Models to Self-Correct via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2025/hash/871ac99fdc5282d0301934d23945ebaa-Abstract-Conference.html) · 2025 | [SCoRe: derive two-stage training from behavioral diagnoses](papers/P06.md) |
| P07 | [Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/hash/98711dea460bdefe0e651ca23ec98ba2-Abstract-Conference.html) · 2025 | [PAV: counterintuitive claims need crossed experiments and a cost ledger](papers/P07.md) |
| P08 | [Mutual Reasoning Makes Smaller LLMs Stronger Problem-Solver](https://proceedings.iclr.cc/paper_files/paper/2025/hash/35514d533cdc278a7780daf0dbe7d0b7-Abstract-Conference.html) · 2025 | [rStar: attribute candidate generation and verification separately](papers/P08.md) |
| P09 | [On the self-verification limitations of large language models on reasoning and planning tasks](https://proceedings.iclr.cc/paper_files/paper/2025/hash/f3c5e56274140e0420baa3916c529210-Abstract-Conference.html) · 2025 | [Self-verification: separate judgment, critique generation, and critique use](papers/P09.md) |
| P10 | [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ead542f13a38179d1b55b88610f959a1-Abstract-Conference.html) · 2025 | [CoT applicability: answer where and why separately](papers/P10.md) |

## Scope and limitations

Acceptance does not establish that a writing technique caused acceptance. This project extracts inspectable argument structures and experimental recommendations. Prescriptive wording expresses our distillation; source practices and limitations are located in the individual notes. Do not treat lessons from 10 papers as the preferences of all ICLR reviewers or the 2023–2025 pilot as an up-to-date comprehensive survey.

One unresolved source discrepancy concerns P07: efficiency multipliers differ across passages, as recorded in its notes. Preserve the issue rather than silently choosing the more favorable number. Check every training/test split and result against the specific source version.
