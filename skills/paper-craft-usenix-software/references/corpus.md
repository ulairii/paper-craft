# USENIX Security software security: source papers

Ten accepted USENIX Security papers on fuzzing, symbolic execution, firmware emulation, input structure, learned filtering, sanitizer guidance, data-flow analysis, and driver generation. This collection focuses on vulnerability discovery and program analysis.

All ten main texts and relevant appendices were read; exact coverage is recorded in the metadata. PDF page 1 is the USENIX cover. Figure discussion uses text and captions. These notes interpret writing craft in published papers, rather than establish what caused acceptance.

[BibTeX](references.bib) · [Source metadata and reading coverage](corpus.json)

| ID | Paper | Venue | Writing lesson |
|---|---|---|---|
| [P01](papers/P01.md) | [QSYM : A Practical Concolic Execution Engine Tailored for Hybrid Fuzzing](https://www.usenix.org/conference/usenixsecurity18/presentation/yun) | USENIX Security 2018 | Start with the measured bottleneck, then explain the specialization |
| [P02](papers/P02.md) | [MOPT: Optimized Mutation Scheduling for Fuzzers](https://www.usenix.org/conference/usenixsecurity19/presentation/lyu) | USENIX Security 2019 | Make an overlooked allocation decision into the research question |
| [P03](papers/P03.md) | [FIRM-AFL: High-Throughput Greybox Fuzzing of IoT Firmware via Augmented Process Emulation](https://www.usenix.org/conference/usenixsecurity19/presentation/zheng) | USENIX Security 2019 | Organize a systems contribution around competing practical requirements |
| [P04](papers/P04.md) | [EnFuzz: Ensemble Fuzzing with Seed Synchronization among Diverse Fuzzers](https://www.usenix.org/conference/usenixsecurity19/presentation/chen-yuanliang) | USENIX Security 2019 | Explain cooperation through information exchanged during search |
| [P05](papers/P05.md) | [GRIMOIRE: Synthesizing Structure while Fuzzing](https://www.usenix.org/conference/usenixsecurity19/presentation/blazytko) | USENIX Security 2019 | Sell a lower-information method through its useful complementarity |
| [P06](papers/P06.md) | [Symbolic execution with SymCC: Don't interpret, compile!](https://www.usenix.org/conference/usenixsecurity20/presentation/poeplau) | USENIX Security 2020 | Make the component boundary sharpen the novelty |
| [P07](papers/P07.md) | [FuzzGuard: Filtering out Unreachable Inputs in Directed Grey-box Fuzzing through Deep Learning](https://www.usenix.org/conference/usenixsecurity20/presentation/zong) | USENIX Security 2020 | Give a learned model a specific decision in the system |
| [P08](papers/P08.md) | [ParmeSan: Sanitizer-guided Greybox Fuzzing](https://www.usenix.org/conference/usenixsecurity20/presentation/osterlund) | USENIX Security 2020 | Repurpose an existing signal and align the evidence with its new role |
| [P09](papers/P09.md) | [GREYONE: Data Flow Sensitive Fuzzing](https://www.usenix.org/conference/usenixsecurity20/presentation/gan) | USENIX Security 2020 | Make the research questions match the decisions the method changes |
| [P10](papers/P10.md) | [FuzzGen: Automatic Fuzzer Generation](https://www.usenix.org/conference/usenixsecurity20/presentation/ispoglou) | USENIX Security 2020 | Explain automation by showing which expert knowledge is recovered |
