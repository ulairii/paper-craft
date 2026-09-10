# 完整例子：怎样从 SCoRe 蒸馏“自纠错论文”的论证

材料：[P06 — Training Language Models to Self-Correct via Reinforcement Learning](papers/P06.md)，ICLR 2025。以下是反向分析和原创写法，不是原文逐句仿写；没有虚构一个已经做完的新方法。

## 1. 核心故事不是“RL＋两阶段”

真正值得复用的链条是：

1. 想要的能力是修改自己的错误，同时保留正确答案。
2. 离线自纠错训练面对的错误与模型实际生成的错误可能不同（§4/Fig.4，p.5）。
3. 即使转为在线训练，模型仍可能学到不作有意义修改的行为（§5/Fig.5，p.6）。
4. 因而需要分别处理错误分布与修改行为的激励；Stage I 和 Stage II 的职责由前面两个问题导出（Fig.6，p.7）。
5. 验证必须测“怎样修改”，不能只测第二轮有多准（Tables 2、4，pp.9–10）。

**蒸馏。** 如果用户的新方法有两个组件，先检查是否确有两个可区分的失败机制。没有诊断实验，就不能照着此结构把猜测写成事实。

## 2. 可迁移的引言段落职责

| 段落 | 读者需要理解什么 | 需要的证据 | 不应塞入什么 |
|---|---|---|---|
| 1 | 为什么修改能力有独立价值 | 首轮与修订任务的区别 | 通用 LLM 历史综述 |
| 2 | 已有修订训练具体在哪里失效 | 分布偏移、修改行为诊断 | 未验证的“所有方法都失败” |
| 3 | 简单补救为何不足 | 在线训练仍塌缩的对照 | 先列一串组件名称 |
| 4 | 每个训练阶段回应什么问题 | 机制与诊断的一一对应 | 完整超参数表 |
| 5 | 哪些结果支持贡献及其范围 | 净修订收益、首轮能力、关键消融 | 无条件通用性或唯一性 |

这不是要求所有 ICLR 论文都写五段，而是用一段只完成一个论证任务来安排信息。

## 3. 结果为什么不能只报一个“提升”

P06 Table 2（[官方 PDF，p.9](https://proceedings.iclr.cc/paper_files/paper/2025/file/871ac99fdc5282d0301934d23945ebaa-Paper-Conference.pdf#page=9)）给出 MATH 评估：

| 系统 | 首轮准确率 | 第二轮准确率 | 第二轮 − 首轮 |
|---|---:|---:|---:|
| 基础模型 | 52.6% | 41.4% | −11.2 pp |
| SCoRe | 60.0% | 64.4% | +4.4 pp |

因此有三个不同问题：

- SCoRe 自己一次修订净增多少？**4.4 个百分点**。
- SCoRe 的净修订收益相对基础模型改善多少？**15.6 个百分点**，即 4.4 − (−11.2)。
- SCoRe 第二轮准确率相对基础模型第二轮提高多少？**23.0 个百分点**；其中混合了首轮能力与修订行为的变化，不能全归为修订能力。

原表还给出 SCoRe 的错→对 5.8%、对→错 1.4%，分母是全部题目；净变化是 5.8 − 1.4 = 4.4 pp。若使用“错误中的纠正率”，分母应改成首轮错误数，不能复用 5.8% 这个数。百分比与百分点也不可混写。

## 4. 一段怎样解释得更有说服力

不合适的概括：

> Our two-stage framework improves self-correction by 15.6 points, demonstrating robust reasoning.

这句话遗漏指标含义，且把任务结果扩大成不明确的 robust reasoning。

下面是基于已发表数据的新写示例，**不是源文引语**：

> On the reported MATH evaluation, SCoRe increases accuracy from 60.0% on the first attempt to 64.4% after revision. Corrections and regressions account for 5.8% and 1.4% of all problems, respectively, yielding a net gain of 4.4 percentage points. The base model instead loses 11.2 points after revision. These results support improved revision behavior in this setting; the ablations separately examine which training components contribute to that behavior.

这里先测量，再解释行为，再交给消融检验训练设计。没有把准确率表本身当作两阶段机制的完整因果证明。

## 5. 实验表如何服务创新点

| 论点 | 不能缺的对照 | 结果不足时怎么收缩 |
|---|---|---|
| 在线首轮分布重要 | 去掉在线首轮样本，比较首轮与修订变化 | 只能声称当前完整训练有效，不能归因分布匹配 |
| Stage I 有独立作用 | 去掉 Stage I，其他设置尽量一致 | 若最终分数相近，不继续把它列成核心必要创新 |
| progress shaping 改变修改行为 | 去掉 shaping，报告两种转移 | 只报末轮分数无法区分保留与纠错 |
| 优于多试一次 | 匹配实际预算的独立采样与选择 | 仅匹配次数时，就限定为尝试次数对照 |

前三项对应 Table 4；最后一项由 §6.2 的采样比较进一步蒸馏，建议新论文明确 token/辅助模型成本，不能声称原文已经完成全成本对齐。

## 6. 哪些不能从此例继承

训练时使用奖励不等于测试时获得正确答案；P03 的 intrinsic self-correction 批评与 P06 的训练干预要放在同一条件表里比较。附录 A.3 的多轮平台限制“越想越好”的故事。现有消融支持所测设计，不证明 RL 是唯一办法，也不证明两个阶段对所有模型均必要。
