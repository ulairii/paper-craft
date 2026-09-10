# ICLR reasoning / test-time compute 样例语料

10 篇均为 ICLR 正式录用论文，跨 2023–2025 年；不是同届语料。选择依据是机制代表性、控制实验和可迁移的论证价值，并非引文数排名，也不宣称每篇都是获奖论文。覆盖采样、分解、验证、修订、搜索、计算分配及负结果；它仍是一个方向簇，未来可继续拆分，每个独立发布叶子仍须各有至少 10 篇同会议论文。

已阅读全部 10 篇正文及逐篇列出的相关附录；没有声称读完全部附录、运行作者代码或复核定理证明。P01/P02 使用固定版本的已录用作者稿（PDF 有 ICLR 发表标头），其余使用官方 proceedings PDF。文件哈希、获取时间和阅读页码见 [corpus.json](corpus.json)。

| ID | 论文 / 年份 | 选入理由与阅读笔记 |
|---|---|---|
| P01 | [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://openreview.net/forum?id=1PL1NIMMrw) · 2023 | [采样与聚合：把最小改动写成明确机制](papers/P01.md) |
| P02 | [Least-to-Most Prompting Enables Complex Reasoning in Large Language Models](https://openreview.net/forum?id=WZH7099tgfM) · 2023 | [分解式推理：先定义 easy-to-hard，再展示可扩展性](papers/P02.md) |
| P03 | [Large Language Models Cannot Self-Correct Reasoning Yet](https://proceedings.iclr.cc/paper_files/paper/2024/hash/8b4add8b0aa8749d80a34ca5d941c355-Abstract-Conference.html) · 2024 | [负结果：用混淆因素组织全文](papers/P03.md) |
| P04 | [Let's Verify Step by Step](https://proceedings.iclr.cc/paper_files/paper/2024/hash/aca97732e30bcf1303bc22ac3924fd16-Abstract-Conference.html) · 2024 | [验证器监督：把最佳结果与公平归因分成两组实验](papers/P04.md) |
| P05 | [Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/hash/1b623663fd9b874366f3ce019fdfdd44-Abstract-Conference.html) · 2025 | [测试时计算：卖分配规律，同时核算决策成本](papers/P05.md) |
| P06 | [Training Language Models to Self-Correct via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2025/hash/871ac99fdc5282d0301934d23945ebaa-Abstract-Conference.html) · 2025 | [SCoRe：从行为诊断推导两阶段训练](papers/P06.md) |
| P07 | [Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/hash/98711dea460bdefe0e651ca23ec98ba2-Abstract-Conference.html) · 2025 | [PAV：反直觉主张需要交叉实验与成本账本](papers/P07.md) |
| P08 | [Mutual Reasoning Makes Smaller LLMs Stronger Problem-Solver](https://proceedings.iclr.cc/paper_files/paper/2025/hash/35514d533cdc278a7780daf0dbe7d0b7-Abstract-Conference.html) · 2025 | [rStar：候选生成与验证必须分别归因](papers/P08.md) |
| P09 | [On the self-verification limitations of large language models on reasoning and planning tasks](https://proceedings.iclr.cc/paper_files/paper/2025/hash/f3c5e56274140e0420baa3916c529210-Abstract-Conference.html) · 2025 | [自验证研究：分解判断、批评与利用批评](papers/P09.md) |
| P10 | [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ead542f13a38179d1b55b88610f959a1-Abstract-Conference.html) · 2025 | [CoT 适用范围：把 where 与 why 分开回答](papers/P10.md) |

## 使用边界

录用不证明某种写法导致录用。本项目提取的是可以检查的论证结构和实验设计建议。规则中的“应”属于我们的蒸馏建议；具体论文的做法与局限在阅读笔记内定位。不要将 10 篇的共同经验当作 ICLR 全体审稿人偏好，也不要将 2023–2025 样例当作最新全景综述。

源文中存在可核对的不一致：P07 的效率倍数在不同段落口径不同，见其笔记。保留问题，不静默选择更有利的数字。所有训练/测试划分与结果必须回到具体版本核对。
