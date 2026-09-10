# Worked example: turn a feature tradeoff into a draft

All methods, datasets, and numbers in this example are fictional. They demonstrate writing decisions and must not be reused as research results. Bracketed fields identify facts the author would need to supply. The story uses the joint-task framing of [VICRegL](papers/P10.md), task-dependent invariance of [InfoMin](papers/P06.md), and complementary-comparison structure of [GraphCL](papers/P09.md).

## Supplied material

The author proposes a representation objective with a global agreement term and two local matching terms. One local term uses known crop coordinates; the other uses feature similarity. All rows use the same encoder, pretraining data, training duration, and frozen readout protocols. The author has not supplied uncertainty estimates or complete matching equations.

| Configuration | Classification top-1 (%) | Segmentation mIoU | Training hours |
|---|---:|---:|---:|
| Global baseline | 74.0 | 48.0 | 10.0 |
| Add coordinate matching | 73.9 | 52.0 | 11.0 |
| Add feature matching | 73.8 | 50.5 | 11.2 |
| Add both, weak local weight | 73.8 | 54.0 | 12.0 |
| Add both, strong local weight | 72.5 | 55.0 | 12.0 |

A second segmentation dataset gives 30.0 mIoU for the baseline and 30.2 for the weak-weight combined model. These results support a substantial gain on the first dataset and a small change on the second. They do not support uniform transfer superiority.

## Title

**Balancing Global Agreement and Local Correspondence in Visual Representations**

The title names the scientific choice. An acronym would add little until the author has a reason to use one.

## Abstract draft

Global agreement objectives encourage image representations to ignore differences between augmented views, but do not explicitly train local features to preserve correspondence. We study whether local matching can improve dense prediction while retaining useful global features. Our objective combines global agreement with two complementary signals: coordinate matching identifies corresponding image locations, while feature matching associates similar regions across locations. Under a common pretraining and frozen-readout protocol, the combined objective improves segmentation from 48.0 to 54.0 mIoU on [Dataset A], with classification changing from 74.0% to 73.8%. Stronger local weighting raises segmentation to 55.0 mIoU but reduces classification to 72.5%, exposing the balance between the two tasks. The gain is smaller on [Dataset B]. These findings identify a useful operating point for local matching and show how its benefits depend on the downstream task.

## Introduction draft

Visual representations support tasks with different information requirements. Image classification often benefits from ignoring where an object appears within a crop. Segmentation also requires features that distinguish locations. A global agreement objective encourages consistency across views, but provides no direct local correspondence signal. This raises a practical question: can local matching improve dense prediction without substantially reducing the usefulness of the global representation?

We investigate this question by adding coordinate-based and feature-based matching to a fixed global objective. The two signals serve different purposes. Coordinate matching uses the known transformation between crops to identify corresponding locations. Feature matching allows regions to be associated through their learned appearance, including regions at different coordinates. We combine these local terms with global agreement so that the encoder continues to learn an image-level representation while receiving direct supervision at local feature positions.

Our experiments show that the combination improves frozen segmentation on [Dataset A] more than either matching term alone. With a weak local weight, mIoU increases by 6.0 points while classification decreases by 0.2 percentage points. Increasing the local weight yields a further segmentation gain at a larger classification cost. The results therefore motivate a balance between objectives, rather than maximizing the local term. Transfer to [Dataset B] changes only slightly, indicating that the benefit depends on the downstream setting.

The contribution is an empirical account of this balance, together with a simple objective that exposes it. The component comparisons test the complementary value of the two matching signals, and the weight comparison shows how the chosen balance affects the resulting features. [Add scientifically relevant citations to global objectives, local matching, and task-dependent invariance.]

## Method draft

For each training image, we sample two augmented views and encode them into spatial feature maps. A pooled representation supplies the global agreement objective. The local objective operates on pairs of spatial features selected in two ways. Coordinate matching maps feature locations back to the original image and pairs corresponding positions across views. Feature matching selects pairs using [distance, candidate set, selection rule, and gradient treatment]. The encoder is shared across the two views.

We train with

\[
\mathcal{L}=\mathcal{L}_{\mathrm{global}}+
\lambda\left(\mathcal{L}_{\mathrm{coordinate}}+
\mathcal{L}_{\mathrm{feature}}\right).
\]

Here, the global term is [baseline objective and citation], and each local term applies [pairwise loss and normalization] to its selected matches. The scalar \(\lambda\) controls the emphasis on local correspondence. [Define the matching sets and loss equations from the actual implementation; specify treatment of non-overlapping views.] At evaluation, classification uses [pooled feature layer], while segmentation uses [spatial feature layer and readout]. Both evaluations freeze the pretrained encoder.

## Results draft

**Local matching improves dense prediction with a small classification change.** Under the same encoder, data, and training duration, adding both matching terms increases frozen segmentation from 48.0 to 54.0 mIoU on [Dataset A]. Classification changes from 74.0% to 73.8%. This operating point preserves most of the measured global capability while providing substantially more useful features for the evaluated segmentation task. Training takes 12.0 hours, compared with 10.0 hours for the global baseline. [Report run count and uncertainty when available.]

**The two matching signals provide complementary gains.** Coordinate matching alone reaches 52.0 mIoU, while feature matching reaches 50.5. Combining them reaches 54.0, exceeding either individual addition under the supplied protocol. This comparison supports retaining both signals in the objective. It does not by itself establish which visual patterns each term learns; that explanation would require the author's correspondence analysis.

**The local weight controls a measurable tradeoff.** Increasing the local weight improves segmentation by another 1.0 mIoU, but classification falls from 73.8% to 72.5%. We therefore use the weak-weight configuration when both tasks matter. The strong-weight setting remains useful when the application prioritizes [Dataset A] segmentation over global classification.

**Transfer gains depend on the target dataset.** On [Dataset B], the weak-weight model reaches 30.2 mIoU compared with 30.0 for the baseline. This small change contrasts with the 6.0-point gain on [Dataset A]. The available results establish the main benefit on [Dataset A]; they leave open which dataset properties determine whether local matching helps. [Add a dataset-specific explanation only if supported by further supplied analysis.]

## Conclusion draft

Adding coordinate and feature matching to a global objective improves the accessibility of local information on [Dataset A] while retaining most classification accuracy. The component and weight comparisons reveal both the value of combining the signals and the cost of emphasizing them too strongly. The small change on [Dataset B] motivates further study of when local correspondence translates into better transfer.

## Why this draft works

The abstract, introduction, method, and experiments all develop the same question. The result paragraph leads with the useful capability, then explains the comparison and its implication. The method gives the terms distinct jobs. The second dataset defines scope without displacing the main finding. Essential unknowns remain specific placeholders, so the author receives usable prose rather than a request to complete every experiment before writing.
