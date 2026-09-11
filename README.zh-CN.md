<div align="center">

<br>
<img src="assets/paper-craft-icon.png" alt="paper-craft — 墨青底色上的折纸字母 p" width="144" height="144">

<h1>paper-craft</h1>
<p><a href="README.md">English</a> · <strong>简体中文</strong></p>
<p><strong>从优秀论文中蒸馏科研写作方法。</strong></p>
<p><sub>22 个细分方向 &nbsp; / &nbsp; 8 个会议 &nbsp; / &nbsp; 每个方向至少 10 篇参考论文</sub></p>

<p>
  <a href="#快速开始">快速开始</a> ·
  <a href="#写作技能库">浏览技能</a> ·
  <a href="#写作示例">写作示例</a> ·
  <a href="#贡献技能">参与贡献</a>
</p>

<br>
</div>

---

将研究想法、初稿或实验结果组织成一篇主线清晰的论文。paper-craft 提炼已发表论文如何引出问题、突出核心洞见、安排实验、解释发现，以及如何用准确、自然的英文表达。

每个 skill 聚焦一个**会议与细分研究方向**，参考至少 **10 篇该会议的正式录用论文**，并附论文引用、逐篇阅读笔记和具体写作示例。技能正文与论文分析使用英文，便于直接服务英文科研写作。

## 能帮助你写什么

| 论文部分 | 写作重点 |
|:---|:---|
| **故事与贡献** | 找到核心洞见，讲清研究价值。 |
| **标题与摘要** | 让贡献容易识别，避免夸大和空泛措辞。 |
| **引言与方法** | 把问题、直觉和设计连成一条清晰的主线。 |
| **实验与结果** | 围绕问题组织实验，解释结果说明了什么。 |
| **句子与段落** | 减少生僻措辞、模糊论断和信息过载，让表达清楚自然。 |

## 快速开始

**1. 一条命令安装。**

需要 Git 和 Python 3。请在尚无 `paper-craft` 克隆目录的位置运行：

```bash
git clone https://github.com/ulairii/paper-craft.git && python3 paper-craft/scripts/install.py
```

**2. 将入口和研究材料交给助手。**

```text
读取 ~/.local/share/paper-craft/skills/paper-craft/SKILL.md。

目标会议：ICLR。根据以下方法描述和已有实验结果，写一份完整的英文论文初稿。
找到核心故事，解释关键比较，使用自然、准确的学术英文。

[粘贴方法和实验结果，或提供文件路径]
```

安装脚本会输出入口文件的绝对路径；如果助手不能展开 `~`，请使用该路径。助手会根据材料选择适配的会议与方向 skill，再完成写作。也可以只要求写一个章节、列大纲或润色句子。

### 安装到支持 skills 的助手

默认安装目录为 `~/.local/share/paper-craft/skills`，使用上面的 prompt 显式加载入口。如果希望助手自动发现技能，请安装到该助手配置的 skills 目录：

```bash
python3 paper-craft/scripts/install.py --dest /path/to/your/assistant/skills
```

已经克隆仓库时，在仓库根目录运行 `python3 scripts/install.py` 即可。脚本会一起复制入口和所有方向技能，保留相对路径，并拒绝覆盖已有技能目录。需要与旧版并行试用新版时，请指定一个新目录，再加载新入口。

也可以直接让助手读取克隆目录中的 `paper-craft/skills/paper-craft/SKILL.md`。技能本身不需要 Python 环境、论文下载或 API key；Python 仅用于可选的安装脚本。

### 如何选择适配的 skill

[统一入口](skills/paper-craft/SKILL.md)通过[方向目录](skills/paper-craft/references/catalog.md)，匹配目标会议、研究核心贡献和写作任务。助手从材料中判断方向，无需用户挑选文件夹。

跨方向工作会选择一个主要 skill，在有帮助的地方借用其他方向的写作经验。没有适配方向时，会使用通用写作方法，并简要说明覆盖缺口。仅指定 ICLR，不会使所有工作都被归为大模型推理。

需要让助手加载或安装入口；仅克隆仓库不会自动启用技能。

## 写作技能库

可以按下面的研究领域浏览，也可以让[统一入口](skills/paper-craft/SKILL.md)自动选择。每个“论文”链接都包含参考文献清单和逐篇阅读笔记；详细覆盖范围见[方向目录](skills/paper-craft/references/catalog.md)。

[人工智能与机器学习](#人工智能与机器学习) · [计算机视觉](#计算机视觉) · [安全与隐私](#安全与隐私)

### 人工智能与机器学习

涵盖学习目标、模型设计、推理、生成与控制。

| 会议 | 写作方向 | 参考文献 |
|:---|:---|:---|
| **ICLR** | [大模型推理与测试时计算](skills/paper-craft-iclr-reasoning/SKILL.md) | [论文 · 2023–2025](skills/paper-craft-iclr-reasoning/references/corpus.md) |
| **ICLR** | [表征学习](skills/paper-craft-iclr-representation/SKILL.md) | [论文 · 2019–2022](skills/paper-craft-iclr-representation/references/corpus.md) · [BibTeX](skills/paper-craft-iclr-representation/references/references.bib) |
| **ICLR** | [生成模型](skills/paper-craft-iclr-generative/SKILL.md) | [论文 · 2014–2024](skills/paper-craft-iclr-generative/references/corpus.md) · [BibTeX](skills/paper-craft-iclr-generative/references/references.bib) |
| **ICML** | [表征学习](skills/paper-craft-icml-representation/SKILL.md) | [论文 · 2020–2023](skills/paper-craft-icml-representation/references/corpus.md) · [BibTeX](skills/paper-craft-icml-representation/references/references.bib) |
| **ICML** | [生成模型](skills/paper-craft-icml-generative/SKILL.md) | [论文 · 2014–2023](skills/paper-craft-icml-generative/references/corpus.md) · [BibTeX](skills/paper-craft-icml-generative/references/references.bib) |
| **ICML** | [强化学习](skills/paper-craft-icml-rl/SKILL.md) | [论文 · 2015–2022](skills/paper-craft-icml-rl/references/corpus.md) · [BibTeX](skills/paper-craft-icml-rl/references/references.bib) |
| **NeurIPS** | [表征学习](skills/paper-craft-neurips-representation/SKILL.md) | [论文 · 2019–2022](skills/paper-craft-neurips-representation/references/corpus.md) · [BibTeX](skills/paper-craft-neurips-representation/references/references.bib) |
| **NeurIPS** | [生成模型](skills/paper-craft-neurips-generative/SKILL.md) | [论文 · 2014–2022](skills/paper-craft-neurips-generative/references/corpus.md) · [BibTeX](skills/paper-craft-neurips-generative/references/references.bib) |
| **NeurIPS** | [强化学习](skills/paper-craft-neurips-rl/SKILL.md) | [论文 · 2017–2021](skills/paper-craft-neurips-rl/references/corpus.md) · [BibTeX](skills/paper-craft-neurips-rl/references/references.bib) |

### 计算机视觉

涵盖目标检测、分割与三维感知，分别提炼各会议论文的写作方法。

| 会议 | 写作方向 | 参考文献 |
|:---|:---|:---|
| **CVPR** | [目标检测](skills/paper-craft-cvpr-detection/SKILL.md) | [论文 · 2014–2022](skills/paper-craft-cvpr-detection/references/corpus.md) · [BibTeX](skills/paper-craft-cvpr-detection/references/references.bib) |
| **CVPR** | [分割](skills/paper-craft-cvpr-segmentation/SKILL.md) | [论文 · 2015–2023](skills/paper-craft-cvpr-segmentation/references/corpus.md) · [BibTeX](skills/paper-craft-cvpr-segmentation/references/references.bib) |
| **CVPR** | [三维感知](skills/paper-craft-cvpr-3d/SKILL.md) | [论文 · 2017–2024](skills/paper-craft-cvpr-3d/references/corpus.md) · [BibTeX](skills/paper-craft-cvpr-3d/references/references.bib) |
| **ICCV** | [目标检测](skills/paper-craft-iccv-detection/SKILL.md) | [论文 · 2015–2023](skills/paper-craft-iccv-detection/references/corpus.md) · [BibTeX](skills/paper-craft-iccv-detection/references/references.bib) |
| **ICCV** | [分割](skills/paper-craft-iccv-segmentation/SKILL.md) | [论文 · 2015–2023](skills/paper-craft-iccv-segmentation/references/corpus.md) · [BibTeX](skills/paper-craft-iccv-segmentation/references/references.bib) |
| **ICCV** | [三维感知](skills/paper-craft-iccv-3d/SKILL.md) | [论文 · 2019–2023](skills/paper-craft-iccv-3d/references/corpus.md) · [BibTeX](skills/paper-craft-iccv-3d/references/references.bib) |
| **ECCV** | [目标检测](skills/paper-craft-eccv-detection/SKILL.md) | [论文 · 2018–2024](skills/paper-craft-eccv-detection/references/corpus.md) · [BibTeX](skills/paper-craft-eccv-detection/references/references.bib) |
| **ECCV** | [分割](skills/paper-craft-eccv-segmentation/SKILL.md) | [论文 · 2018–2024](skills/paper-craft-eccv-segmentation/references/corpus.md) · [BibTeX](skills/paper-craft-eccv-segmentation/references/references.bib) |
| **ECCV** | [三维感知](skills/paper-craft-eccv-3d/SKILL.md) | [论文 · 2018–2024](skills/paper-craft-eccv-3d/references/corpus.md) · [BibTeX](skills/paper-craft-eccv-3d/references/references.bib) |

### 安全与隐私

涵盖软件测试、隐私测量与机器学习系统安全。

| 会议 | 写作方向 | 参考文献 |
|:---|:---|:---|
| **IEEE S&P** | [软件安全](skills/paper-craft-sp-software/SKILL.md) | [论文 · 2017–2022](skills/paper-craft-sp-software/references/corpus.md) · [BibTeX](skills/paper-craft-sp-software/references/references.bib) |
| **USENIX Security** | [软件安全](skills/paper-craft-usenix-software/SKILL.md) | [论文 · 2018–2020](skills/paper-craft-usenix-software/references/corpus.md) · [BibTeX](skills/paper-craft-usenix-software/references/references.bib) |
| **USENIX Security** | [隐私与测量](skills/paper-craft-usenix-privacy/SKILL.md) | [论文 · 2017–2022](skills/paper-craft-usenix-privacy/references/corpus.md) · [BibTeX](skills/paper-craft-usenix-privacy/references/references.bib) |
| **USENIX Security** | [机器学习安全](skills/paper-craft-usenix-ml/SKILL.md) | [论文 · 2018–2022](skills/paper-craft-usenix-ml/references/corpus.md) · [BibTeX](skills/paper-craft-usenix-ml/references/references.bib) |

## 写作示例

**哪些答案值得再修改一次？** 一项虚构研究在相同模型和 token 预算下，比较均匀分配与按不确定性分配修改次数。写作的重点，是让这个比较讲清论文贡献。

**修改前：介绍任务，列出组件。**

> We study uncertainty-aware revision for improving the reasoning accuracy of large language models under a fixed generation budget. The approach consists of initial answer generation, uncertainty estimation, and selective revision.

**修改后：先建立方法要解决的决策问题。**

> Revising a language model's answers consumes tokens that could be spent on other problems. Under a fixed generation budget, a revision strategy must therefore decide which answers deserve another attempt. We study uncertainty as a signal for this decision: retain confident answers and direct the remaining budget toward revising uncertain ones.

[阅读两版完整摘要与具体修改理由 →](examples/abstract-before-after.md)

两版均为使用同一组虚构结果编写的教学示例，并非模型实测输出。示例说明哪些结果应进入摘要、哪些细节应留在正文，以及这样安排的原因。

如果 paper-craft 对你的写作有帮助，欢迎点个 star。

## 深入阅读写作方法

- [故事与章节结构](skills/paper-craft-iclr-reasoning/references/writing-playbook.md)
- [自然英文、术语与段落衔接](skills/paper-craft-iclr-reasoning/references/claim-language.md)
- [让实验推进论文论证](skills/paper-craft-iclr-reasoning/references/experiment-playbook.md)
- [常见写作请求](examples/prompts.md)
- [逐篇论文阅读笔记](skills/paper-craft-iclr-reasoning/references/corpus.md)

## 贡献技能

选择一个会议和明确的细分研究方向，阅读至少 10 篇该会议的正式录用论文，提炼它们的写作选择：故事如何开始、洞见在哪里出现、实验如何推进论证、哪些细节帮助读者理解。请附来源位置和原创的修改前后示例，让建议落到具体表达上。

将可直接使用的写作指导放在 `SKILL.md`，深入分析放在 `references/`。解释文章为何有说服力；单凭录用事实，无法确定哪些写作选择导致了录用。

将新技能放在 `skills/` 下，与现有技能并列，并在[方向目录](skills/paper-craft/references/catalog.md)中登记会议、主题信号、支持的写作任务，以及与相邻方向的区别。所有方向保留在同一 Git 分支中。随着技能库扩展，用户仍只需使用 `paper-craft` 入口。

技能库正继续扩展 AI、计算机视觉和安全方向，包括 S&P 的更多主题、CCS 和 NDSS。[写作技能库](#写作技能库)列出了当前可用的全部方向。

## 分享 paper-craft

可以使用[中英文发布文案](docs/launch-posts.md)向研究社区介绍项目，或将[摘要对比示例](examples/abstract-before-after.md)分享给同事。欢迎反馈实际写作体验和使用案例。
