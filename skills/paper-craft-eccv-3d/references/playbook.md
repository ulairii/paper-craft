# Explain the geometry, then explain what the result teaches

## A concrete opening makes the contribution easier to sell

[SpiderCNN](papers/P01.md) begins from irregular sampling. [H3DNet](papers/P04.md) develops complementary geometric constraints. [SWFormer](papers/P09.md) addresses sparse observations and empty prediction locations. Their transferable move is to make the design problem visible before presenting its solution.

For an introduction, establish the task and observation condition, identify the specific mismatch, state the proposed principle, and preview the result that best expresses its value. Do not devote the first paragraph to a catalogue of applications unless those applications define the problem.

A learning paper can use the same structure with a statistical mismatch. [PointContrast](papers/P03.md) asks how scene-level pretraining transfers. [Point-MAE](papers/P06.md) separates solving reconstruction from learning a useful representation. Their contribution is clearer when the learning question precedes the loss function.

## Organize methods around roles

An effective method explanation gives each object a role, each operation a reason, and each equation a local meaning. In [PPF-FoldNet](papers/P02.md), point-pair geometry removes global rotation from the input. In [PARE-Net](papers/P10.md), invariant features support matching while equivariant features support pose. Introduce the distinction before the network blocks.

For geometric detection, follow the evidence into the output. [H3DNet](papers/P04.md) predicts primitives, fits proposals, and refines them. [SSN](papers/P05.md) constructs a compact geometric target that guides training. A list of heads would conceal why these operations belong together.

For camera fusion, explain the reference frame and the location of geometric information. [BEVFormer](papers/P07.md) gathers views and history into spatially anchored queries. [PETR](papers/P08.md) encodes calibrated coordinates in image features. These are different design arguments; do not reduce both to “enhanced 3D awareness.”

## Choose experiments that distinguish explanations

| Scientific question | Source pattern | What the paragraph should explain |
|---|---|---|
| Does a representation transfer? | PointContrast: same backbone, scratch and pretrained | Separate the learning benefit from an architecture change |
| Does geometry add more than capacity? | H3DNet: wider baseline and primitive combinations | Explain why extra parameters alone are insufficient |
| Does a proxy objective measure the desired property? | Point-MAE: reconstruction loss and downstream accuracy | Describe the disagreement and its implication |
| What does temporal information contribute? | BEVFormer: static, temporal, velocity, visibility | Connect history to the errors it helps resolve |
| Does the estimator improve independently of matching? | PARE-Net: fixed correspondences, different estimators | Attribute the pose result to the relevant stage |
| Why expand sparse support? | SWFormer: diffusion range and object extent | Connect active locations and context to localization |

These are examples of reasoning, not a mandatory test suite. Use the experiments supplied. If a proposed explanation has not been isolated, write it as a design rationale or an interpretation rather than a demonstrated cause.

A useful result paragraph answers one question, selects the decisive comparison, explains the pattern, and adds a boundary if needed. “The wider baseline remains below the geometric model” is more informative than “All components are effective.” “Lower reconstruction error does not consistently improve transfer” makes an actual scientific point.

## Use qualification to sharpen, not weaken, the story

[SSN](papers/P05.md) offers a training-time shape target; that does not make the entire detector free of additional computation. [BEVFormer](papers/P07.md) offers useful temporal fusion; that does not imply every task improves under joint training. [PARE-Net](papers/P10.md) offers strong local features; cross-domain transfer can still be limited by the coarse matching stage.

Put the benefit first and the explanation second. “The auxiliary target improves category separation and is removed after training” is clear. Follow with the remaining inference design only when cost is part of the claim. Avoid adding a generic disclaimer after every result.

The source papers also contain rhetoric and occasional numerical inconsistencies that need not become writing rules. Distill the persuasive logic, using tables and definitions to understand the result. Do not imitate every superlative or turn acceptance into proof that a particular phrase works.

## Place detail by consequence

Keep a fact in the main explanation if omitting it changes the reader's model of the method: oriented features versus coordinates, image grid versus BEV volume, aligned views versus arbitrary unlabeled clouds, training targets versus inference inputs, and online history versus future frames.

Keep a fact beside a result if it changes the comparison: normals, voting, point count, extra pretraining, evaluated classes, or timing scope. Put routine implementation values and long derivations in compact setup or supporting material. This preserves enough detail to understand the contribution without burying the argument.
