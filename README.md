# paper-craft

从同会议、同研究方向的论文中，蒸馏科研写作、实验设计与结果解释的 skills。每个发布的细分 skill 至少有 **10 篇同会议正式录用论文**，保留逐篇阅读笔记、具体出处、反例和适用边界。

当前完成一个供审阅的试点：**ICLR · LLM reasoning & test-time compute**，包含 2023–2025 年 10 篇论文的正文与相关附录阅读。不是最新综述，不代表全部 ICLR 风格，也不以录用反推某种写法必然有效。

## 先看这个例子

1. [SCoRe 完整拆解](skills/paper-craft-iclr-reasoning/references/worked-example.md)：故事怎样从诊断推导方法、实验怎样接住创新、15.6 pp 为什么不能写成一次修订的收益。
2. [10 篇论文与逐篇笔记](skills/paper-craft-iclr-reasoning/references/corpus.md)：采样、分解、验证、修订、搜索、计算分配与负结果。
3. [写作规则](skills/paper-craft-iclr-reasoning/references/writing-playbook.md)、[实验规则](skills/paper-craft-iclr-reasoning/references/experiment-playbook.md)、[措辞示例](skills/paper-craft-iclr-reasoning/references/claim-language.md)。
4. [可调用的 SKILL.md](skills/paper-craft-iclr-reasoning/SKILL.md)。

可直接给助手这样的任务：

> 读取 skills/paper-craft-iclr-reasoning/SKILL.md，基于我提供的结果审阅引言和实验设计。先区分已有事实、机制假设和缺失证据；给出可核对的论文出处。不要编造实验。

## 项目如何扩展

以 `会议 × 细分方向` 为发布单元，避免只用会议名套同一套泛用提示词。会议与年份政策属于独立配置，科学论证规则由具体语料支持。建议后续 AI 入口覆盖 ICLR/ICML/NeurIPS，CV 覆盖 CVPR/ICCV/ECCV，安全覆盖 S&P/USENIX Security/CCS/NDSS；这些只是路线图，目前只有本 ICLR skill。

一个叶子包含：简短 SKILL 入口 → 按任务加载的规则 → 逐篇证据与版本 → 完整示例 → 验收案例。细化到 verifier、self-correction 等单独发布时，每个新叶子仍要重新满足至少 10 篇同会议论文，不把父目录十篇当作所有子方向都达标。

新语料需同时包括正结果、条件性结果和重要反例；逐篇记录故事、实验控制、解释链、细节取舍与不能照搬的结论。跨论文规律注明是我们的蒸馏，不伪装成原作者结论。完整 PDF 不随仓库再分发；本地文字为转述与分析。

## 可追溯性与检查

[corpus.json](skills/paper-craft-iclr-reasoning/references/corpus.json) 记录固定版本、SHA-256、获取时间和阅读页码。P01/P02 使用带 ICLR 发表标头的固定 arXiv 作者稿，其余为官方 proceedings PDF。读过正文和指定附录，不声称复核全部证明或复现结果。

`python scripts/validate_pilot.py` 检查语料、笔记、阅读状态和本地链接；`evals/cases.md` 提供人工验收输入与预期行为。结构检查不等于写作效果验证；尚未做独立模型盲测或用户论文 A/B 评估。

采集脚本需要 Python requests、beautifulsoup4、系统 pdftotext 及配置好的 `ssh palmetto`；下载缓存位于 scratch。使用 skill 本身只需要本仓库的文本文件。[paths.json](paths.json) 保存存储安排。重新下载后哈希变化必须重新核对，不继承旧阅读状态。
