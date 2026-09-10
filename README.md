# paper-craft

Research writing, experiment design, and result-interpretation skills distilled from papers in the same conference and research area. Each released subfield skill requires **at least 10 formally accepted papers from one conference**, with individual reading notes, precise sources, counterexamples, and scope boundaries.

The current reviewable pilot is **ICLR · LLM reasoning & test-time compute**, based on the main texts and selected appendices of 10 papers from 2023–2025. It is not a current comprehensive survey or a representation of all ICLR writing, and acceptance does not establish that a writing technique caused acceptance.

## Start with the example

1. [SCoRe worked example](skills/paper-craft-iclr-reasoning/references/worked-example.md): how diagnoses motivate a method, how experiments support novelty, and why 15.6 pp is not the gain from one revision.
2. [The 10 papers and individual notes](skills/paper-craft-iclr-reasoning/references/corpus.md): sampling, decomposition, verification, revision, search, compute allocation, and negative results.
3. [Writing playbook](skills/paper-craft-iclr-reasoning/references/writing-playbook.md), [experiment playbook](skills/paper-craft-iclr-reasoning/references/experiment-playbook.md), and [claim-language examples](skills/paper-craft-iclr-reasoning/references/claim-language.md).
4. [The callable SKILL.md](skills/paper-craft-iclr-reasoning/SKILL.md).

Example request to an assistant:

> Read skills/paper-craft-iclr-reasoning/SKILL.md and review my introduction and experiment design using the results I provide. First distinguish established facts, mechanism hypotheses, and missing evidence. Give traceable paper references. Do not invent experiments.

## Extending the project

Release skills by **conference × subfield**, rather than applying one generic prompt under different conference names. Conference/year policies belong in separate configuration; scientific argumentation principles require support from the specific corpus. Proposed future coverage includes ICLR/ICML/NeurIPS for AI, CVPR/ICCV/ECCV for computer vision, and S&P/USENIX Security/CCS/NDSS for security. This is a roadmap; only the ICLR pilot currently exists.

Each leaf contains a concise SKILL entry point, task-specific playbooks, per-paper evidence and versions, a worked example, and acceptance cases. If verification or self-correction becomes an independent skill, each new leaf still needs at least 10 papers from the same conference. Ten papers in a parent directory do not satisfy every child subfield.

New corpora should include positive results, conditional results, and important counterexamples. Each paper's notes should cover its story, experimental controls, interpretation chain, detail placement, and conclusions that cannot be copied. Label cross-paper recommendations as our distillation rather than attributing them to source authors. Full PDFs are not redistributed in the repository; local prose is paraphrase and analysis.

## Provenance and checks

[corpus.json](skills/paper-craft-iclr-reasoning/references/corpus.json) records source versions, SHA-256 hashes, retrieval times, and pages read. P01/P02 use pinned arXiv author versions with ICLR publication headers; the remaining papers use official proceedings PDFs. Coverage includes the main texts and specified appendices, not verification of every proof or reproduction of results.

`python scripts/validate_pilot.py` checks corpus records, notes, reading status, and local links. `evals/cases.md` supplies manual acceptance inputs and expected behavior. Structural checks do not establish writing effectiveness; no independent-model blind test or A/B evaluation on a user's paper has been performed.

The collection script requires Python requests and beautifulsoup4, system pdftotext, and a configured `ssh palmetto` connection. Download caches live on scratch. Using the skill itself only requires the repository's text files. [paths.json](paths.json) records storage locations. If a new download changes a hash, recheck the source rather than carrying forward the previous reading status.
