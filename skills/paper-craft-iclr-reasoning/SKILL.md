---
name: paper-craft-iclr-reasoning
description: Plan, draft, or critique ICLR papers on LLM reasoning and test-time computation using evidence distilled from 10 accepted ICLR papers. Use for narratives, contribution framing, experiment design, result interpretation, and claim calibration involving sampling, search, verification, decomposition, or self-correction.
---

# ICLR LLM reasoning 与 test-time compute

把研究事实组织成可检验的论证。不要把措辞强度当创新强度，不把本语料的经验说成 ICLR 的录用规则。

## 先读取

1. 读 [语料与边界](references/corpus.md)，确认此 skill 的范围。
2. 故事/大纲/引言任务读 [写作规则](references/writing-playbook.md)；实验/结果任务读 [实验规则](references/experiment-playbook.md)；润色同时读 [措辞规则](references/claim-language.md)。
3. 按主张读取至少两个最相关的逐篇笔记：采样 P01；分解 P02；自纠错 P03/P06/P09；验证 P04/P07/P08；预算 P05/P07/P08；适用范围 P10。不要为了引用数量强行引用不相关论文。
4. 需要完整示范时读 [SCoRe 反向拆解](references/worked-example.md)。源文定位均指固定 PDF 版本的页序。

## 建立事实边界

从用户材料提取目标任务、模型和版本、训练/测试数据、改动、反馈来源、推理预算、已完成结果及未知项。区分训练时奖励、测试时真实可用 verifier、测试答案 oracle。资料缺失时保留 `[待提供]`，继续做不依赖该信息的结构工作；不编数字、实验、引文或新颖性。

先写一句：在 **条件 C** 下，针对 **失败 F**，用 **机制 M**，以 **证据 E** 支持 **主张 H**。如果用户尚未观察到 F，把它标为待检验假设，不写成已发现事实。

## 按任务执行

- **故事/大纲**：给出问题→具体缺口→诊断→机制→验证→边界的链条。选择方法、分析或负结果型贡献；不强迫分析论文虚构新方法。每段指定一个读者问题和对应证据。
- **实验设计**：输出主张、竞争解释、关键对照、指标/图、成本口径和失败后的收缩结论。优先排除最能推翻核心主张的解释。区分必要证据和可选扩展。
- **结果解释**：先陈述测量，再解释可能机制，再说明对照排除了什么，最后限定仍未排除什么。分开平均值与难度切片、覆盖上界与可部署选择、相关与因果。
- **改写**：保留事实、比较对象和条件；输出改写及实质改动理由。没有证据时降低主张或标出所缺实验，不补造事实。英语示例是新写句子，不冒充原文引语。

## 必查项

1. “自纠错”是否同时报告首轮、后轮、错→对、对→错及分母？
2. “高效”预算是否包含辅助模型、token、展开、难度估计、离线训练成本？只测调用数就只声称调用数。
3. “验证更好”是否固定候选？“搜索更好”是否固定选择器？训练数据不同时是否另设公平归因实验？
4. “小模型”是否偷换成“弱模型”？“无需微调”是否偷换成“无需额外资源”？
5. “最优”“通用”“保证”“首次”是否超出策略集合、模型任务、理论假设或查新证据？
6. prompt、答案 parser、停止规则、测试划分等影响结论的细节是否被藏在附录？

## 输出约定

按用户请求的篇幅交付正文/大纲/实验表，并附简短证据说明：哪些是用户事实，哪些是本 skill 的建议、来自哪篇论文哪节/图表，哪些尚待验证。正文引用只放与实际论点相关的论文；写作方法的来源可放单独审阅说明，避免污染论文 related work。

文献条目与数字从 [corpus.json](references/corpus.json) 和逐篇笔记追溯；遇到不一致查源文，不自行挑更漂亮的结果。无需下载全部 PDF 即可使用本地规则；精确引语或笔记未覆盖事实需要再次核对源文。
