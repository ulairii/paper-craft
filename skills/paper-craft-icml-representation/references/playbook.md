# Representation learning: a writing playbook

## Start with a tension the results can resolve

A useful opening identifies a mismatch: a pretraining objective improves while transfer stalls; labels are expensive although images are plentiful; language makes recognition flexible but the source of robustness is unclear; several objectives reach similar performance although their dynamics are poorly understood. Choose the tension that the supplied work actually addresses.

[SimCLR](papers/P01.md) makes a compact framework valuable through findings about how its parts interact. [CPCv2](papers/P02.md) gives improvement a practical unit: labeled examples needed for a target accuracy. [Data Determines](papers/P09.md) makes an apparent explanation into a question and evaluates competing answers. These are distinct stories, not interchangeable introduction templates.

Build an introduction as a connected argument: current capability → unresolved obstacle → your observation → design or analysis → resulting contribution. A short finding can bridge the obstacle and method better than a long list of prior methods. Related work should identify what the new account changes, rather than imply every predecessor failed.

## Choose how the contribution earns attention

For a **method study**, make a small number of design choices intelligible. Explain how each changes the learning problem. The useful contribution can be a recipe plus an understanding of its interactions, as in SimCLR, or a principle translated into a readable objective, as in [Barlow Twins](papers/P04.md).

For a **new interface**, explain the use before the machinery. [CLIP](papers/P06.md) lets language descriptions specify recognition tasks. This motivates zero-shot evaluation naturally. A reader should know what they can now ask the model to do before encountering the complete training recipe.

For a **scale study**, identify the bottleneck and show a tradeoff. [ALIGN](papers/P07.md) compares noisy and clean data at relevant sizes, then examines capacity. “Larger is better” is less informative than explaining when size compensates for lower quality and which models benefit.

For an **explanatory paper**, separate the phenomenon, account, and test. [Alignment and Uniformity](papers/P03.md) turns an account into measurable quantities. [Contrastive Inversion](papers/P08.md) gives recovery a mathematical meaning. [Stepwise Learning](papers/P10.md) turns an exact simplified solution into a qualitative prediction for practical networks. The analysis need not justify every feature of a modern model to contribute an informative picture.

## Let the experimental sequence carry the reasoning

| Story | Lead evidence | Explanatory follow-up | Productive interpretation |
|---|---|---|---|
| Better representations | Downstream performance with a stated adaptation protocol | Change the pairing, objective, or head | Identify which information is preserved or lost |
| Label efficiency | Accuracy across label fractions | Fixed features versus fine-tuning; another task | Explain the annotation saving and the role of adaptation |
| Noisy-data scaling | Quality–size comparisons | Capacity interaction and transfer tasks | Explain when scale compensates for noise |
| Robustness explanation | Shifted performance relative to in-distribution performance | Competing causes with a shared image collection | Identify the supported cause and remaining alternatives |
| Training dynamics | A visible trajectory or spectral pattern | Exact model, controlled extension, practical networks | Separate quantitative prediction from qualitative persistence |

Use this table to organize evidence already available, not as a checklist of experiments the author must run. If an important comparison is missing, narrow the sentence or mark a short factual placeholder and continue drafting.

Distinguish a baseline's purpose. An identity encoder can show that inversion is nontrivial; supervised recovery can show representational capacity. A wider competing head can test whether a gain comes from capacity. A random-prompt control can expose a misleading robustness statistic. One label, “baseline,” should not hide these different questions.

## Explain a table instead of reading it aloud

Write the main finding first. Pick the comparison that makes its meaning clear, then connect it to the hypothesis. If a second result limits that explanation, state the limit where it helps the reader.

A method can improve transfer while solving the proxy task less accurately. A joint objective can help visual tasks and lose on a text task. A more flexible interface can struggle with counting. These are opportunities to explain what the representation captures, not invitations to surround every claim with weak hedges.

When discussing a theory, distinguish four verbs: **derive** an exact result, **predict** an observable consequence, **observe** it in a broader setting, and **suggest** an extension. [DirectPred](papers/P05.md) shows how an analysis can motivate a concrete update; Stepwise Learning leaves proposed speedups as future directions. Do not turn the latter into a demonstrated algorithmic gain.

## Keep the detail that changes the scientific sentence

The reader needs to know the positive-pair construction, supervision source, role of each head, downstream adaptation, and assumptions behind a recovery or dynamics statement. Without these, “better representations” is underspecified.

The reader usually does not need every augmentation probability, prompt string, optimizer constant, or proof manipulation in the opening argument. Give the intuition first, preserve necessary conditions beside the claim, and move the rest to a well-named subsection or appendix.

## Edit for recognizable meaning

| Weak sentence | Clearer direction |
|---|---|
| We exploit semantic synergies to obtain superior representations. | State which views agree and what information the encoder should retain. |
| Our simple method is computationally efficient. | Identify the simplified component and the measured cost separately. |
| The model learns without any supervision. | Name the pairs, captions, or transformations supplying the training signal. |
| The theory explains all modern self-supervised learning. | Name the exact setting and the broader behavior observed experimentally. |
| Extensive experiments verify effectiveness. | State the most informative finding and what it explains. |

These lessons are interpretations of the [ten cited papers](corpus.md). They are ways to make an argument understandable, not rules that guarantee acceptance.
