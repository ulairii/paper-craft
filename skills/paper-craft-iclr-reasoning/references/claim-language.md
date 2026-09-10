# 该说什么、不该说什么

以下英文均为原创改写示范，不是论文引语。带方括号的内容必须由用户真实材料填充。改写不能替代尚未完成的实验。

| 风险表述 | 更准确的写法 / 处理 | 原因与出处 |
|---|---|---|
| Our model improves self-correction by 15.6 points in one revision. | Relative to the base model, SCoRe improves the second-minus-first accuracy gain by 15.6 percentage points on the reported MATH evaluation. | 这是 P06 Table 2 的差值之差，不是一次修订增幅；见 worked-example。 |
| Our method is four times cheaper end to end. | Excluding difficulty-estimation overhead, the evaluated allocation reaches [target] with [budget comparison]. | 仅在证据匹配时填数；P05 §3.2 的排除成本会改变含义。 |
| Smaller models reason without help from stronger models. | The system uses a [size] generator and a [size] auxiliary model; we report their standalone task performance separately. | P08 Table 2 提醒参数数不等于任务能力。 |
| LLMs cannot self-correct. | Under the evaluated models, prompts, and feedback-free setting, iterative revision does not consistently improve accuracy. | P03 的范围限制；P09 Table 1 存在反例；P06 改变训练条件。 |
| Our verifier guarantees correct reasoning. | The verifier improves final-answer selection under [candidate distribution]; this evaluation does not establish the correctness of every intermediate step. | P01 §5 与 P04 的评价对象。有形式保证时另列明确假设。 |
| Our compute-optimal policy always outperforms scaling models. | Among the evaluated allocation strategies, [policy] is preferable in [difficulty/load regime]. | P05 §7 与附录 O 不支持全局最优或任意负载。 |
| CoT is useless outside math. | In the tested single-prompt setting, gains are concentrated in math and symbolic tasks, with task-specific exceptions. | P10 §4.2；不包括所有 TTC。 |
| The ablation proves that module X explains all gains. | Holding [controls] fixed, removing X reduces [metric], supporting its contribution in this setting. | P04 的公平归因与 P08 的交叉对照；移除模块不排除全部交互。 |

## 创新怎么 sell

把“新颖、高效、通用、强大”替换成具体对比：过去的选择器评估什么、你的选择器评估什么；过去在哪种错误上失败、你的训练改变哪种转移；过去只知加算力会提升、你的分析回答预算应给谁。

可用三类句式：

- 方法型：We address [observed failure] by changing [specific decision], rather than merely increasing the number of attempts. 仅当已有等预算对照时保留后半句；否则删去。
- 分析型：We characterize how [allocation preference] changes with [difficulty and budget], yielding guidance for [decision]. 对应 P05，不暗示新算法。
- 负结果型：We isolate [confound] and reevaluate [claim] under [controlled setting]. 对应 P03/P09，不用失败证明模型本质。

“first”“state of the art”需要独立查新、明确日期及可比协议。本 skill 的历史语料不提供这样的背书。
