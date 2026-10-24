# 第二期 RAG 独立检验：三篇论文与作图边界

研究议题：[三篇独立检验论文怎样覆盖不同 RAG 结构](https://github.com/UnknownObject777/academic-visual-library/issues/14)。

选择 **Self-RAG、IRCoT、RECOMP**，恰好三篇。三者均有正式 AI 会议版本。分别检验按需分支与候选选择、交替推理与资料累积、压缩与选择性增强。它们没有重复经典 RAG 与 REPLUG 两个开发案例的用途。

本研究基于仓库 `9fee65fe33143b2f71dfc5284be45c1efbc88022`。只确定选材、来源和任务范围。没有运行模型、制作图稿、创建组件或调整技能。没有执行测试与构建。

## 正式来源与采用版本

PDF 页码从文件第一页计数。以下三个正式 PDF 的目标页均已直接查看。来源只用正式出版页和论文；不采用博客解释，也不把早期预印本的图号直接套到正式版本。

| 论文 | 正式发表与稳定标识 | 本次采用的 PDF | 方法正文与目标总览图 |
| --- | --- | --- | --- |
| **Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection** | [ICLR 2024 正式出版页][self-record]；论文标识 `25f7be9694d7b32d5cc670927b8091e1` | [ICLR 正式 PDF][self-pdf]，30 页 | §3，重点 §3.1、§3.3；PDF 第 3–6 页。目标为图 1 的 Self-RAG 部分，PDF 第 2 页。图左的常规 RAG 对比不是本次任务。 |
| **Interleaving Retrieval with Chain-of-Thought Reasoning for Knowledge-Intensive Multi-Step Questions（IRCoT）** | [ACL 2023 主会长文][ircot-record]；Anthology `2023.acl-long.557`；DOI `10.18653/v1/2023.acl-long.557` | [ACL Anthology 正式 PDF][ircot-pdf]，24 页；出版页码 10014–10037 | §3、§3.1、§3.2；PDF 第 3–4 页。核心检索总览为图 2，PDF 第 4 页。最终问答阅读器由 §3.2 补充。 |
| **RECOMP: Improving Retrieval-Augmented LMs with Context Compression and Selective Augmentation** | [ICLR 2024 正式出版页][recomp-record]；论文标识 `bda88ed2892f5e61c9a9bf215c566913` | [ICLR 正式 PDF][recomp-pdf]，25 页 | §2，PDF 第 2–3 页；§3 仅用于厘清训练范围。目标为图 1 的 RECOMP 推理路径，PDF 第 2 页。 |

Self-RAG 的前期调查使用 `arXiv:2310.11511v1`。本次改用上表正式 PDF，不承诺两个版本的全文相同。RECOMP 的正式出版页标题含 **Context Compression**，正式 PDF 首页标题为 **with Compression and Selective Augmentation**，没有 Context。两者作者一致，且出版页直接链接该 PDF；记录时保留这一差异。[Self-RAG 正式 PDF][self-pdf]、[RECOMP 出版页][recomp-record]与[正式 PDF][recomp-pdf]是本次依据。

为固定采用的文件，记录下载副本的 SHA-256。副本和目标页预览不纳入仓库。

| PDF | SHA-256 |
| --- | --- |
| Self-RAG | `b1b57b5d9c1e71ebbebc2a18b625889c467e3f6bced88d049b6ee29067666e7e` |
| IRCoT | `d307211b02415e5a590e4a13165a2006ea53548d11566d33fd781ee1db80e3b6` |
| RECOMP | `0bbc7fc66d83e839f34012f91245d2bfd5fc5786bda3383aaaad606a417e40f6` |

## 各自检验什么

下表是选材判断，不是完整科学关系答案。它不指定布局、全部模块、全部连线或原图的视觉处理。

| 论文 | 与另外两篇及开发案例的差异 | 与首批图元的关系 | 主要风险 |
| --- | --- | --- | --- |
| Self-RAG | 增加检索必要性的分支，以及分段生成的评价与选择。比单次检索或固定并行集成更适合检查条件与重复过程。依据 §3.1、§3.3。[来源][self-pdf] | 文字可表示反思标记；模块与分组可表示候选；科学连接线可表示分支、选择和重复。无需复刻原图的小图标。 | 原图文字密集。容易把训练用的批评模型搬进推理图，或把反思标记误画成独立外部服务。 |
| IRCoT | 重点是多步推理中的交替过程与资料累积。不是 Self-RAG 的候选质量选择，也不是 REPLUG 的固定并行集成。依据 §3。[来源][ircot-pdf] | 重复模块、分组、带方向的连接线与简短状态文字足以表达。无需完整抄录示例问答。 | 图 2 主要呈现检索方法，没有画全 §3.2 的最终阅读器。只照图 2 描述整套问答会少一层任务范围。 |
| RECOMP | 重点是检索资料在进入语言模型前的文本压缩，以及允许空摘要的选择性增强。可检查是否保留中间变换及其含义。依据 §2。[来源][recomp-pdf] | 文档组、压缩模块、文本摘要、模型与连接线即可表达。两种压缩器是方案选项，不能静默画成顺序必经步骤。 | 图 1 同时展示对比路径与示例结果。容易误把对比当成部署中的并行执行，或把示例 token 数当通用性能。 |

三者仍有共用的检索与生成元素。结构差异指本轮任务的组织方式，不表示覆盖了全部 RAG 方法。上述可表达性是选材判断，尚未得到作图运行结果支持。

## 每篇一个方法正文作图任务

每篇只定义一个任务。生成端依据固定的正文材料，在论文绘图工作台完成一张可编辑方法总览。不得要求复刻目标原图的布局、配色、示例文字或装饰。

### Self-RAG：推理方法总览

依据 §3.1 与 §3.3，画 Self-RAG 的推理总览。范围包括有检索与无检索的情况，以及分段输出的处理。Table 1 的文字定义可以作为术语材料。§3.2 只帮助区分训练和推理，不展开训练流程。

可判定范围是 Self-RAG 的推理机制。图 1 左侧基线、训练数据构造、损失函数与实验结果不属于任务。图 1 右侧和相关方法段落由评估方交叉核查，不要求对象数量或布局与原图相同。[正文与图 1][self-pdf]

### IRCoT：检索与最终问答的推理总览

依据 §3、§3.1 和 §3.2，画完整的 IRCoT 问答推理总览。把核心交替检索过程作为重点，并交代最终问答阅读器的范围。阅读器作为整体模块，不展开两种提示策略的内部示例。

图 2 是核心检索过程的参考，不是整套问答系统的完整原图。评估方应同时使用 §3.2。不得把中间推理出现答案，等同于最终阅读器已经执行。训练、数据集、检索指标与附录提示模板不属于任务。图 1 的简化案例不另计一个任务。[§3 与图 2][ircot-pdf]

### RECOMP：压缩增强的推理总览

依据 §2，画 RECOMP 的推理总览。压缩器按功能模块表达，并说明抽取式与生成式是可选实现。范围保留选择性增强的含义，不展开 §3 的压缩器学习算法。

目标图 1 仅作为 RECOMP 路径的核查来源。无检索与普通 RALM 对比、示例答案正误、示例 token 数均不属于交付内容。评估方还需核对 §2，因为原图没有单独展开空摘要情况。[§2 与图 1][recomp-pdf]

## 生成材料与复核材料分开

- **可交给生成端**：每篇上列方法正文的纯文字摘录，以及必要的术语定义。摘录保留原意、公式和变量定义，移除目标图、图注、截图、图像链接及附录绘图材料。提供统一任务范围与已固定的通用风格要求。本研究不制作实际提示词或正文摘录包。
- **只供评估方**：完整正式 PDF、目标原图与图注、本选材报告、用于核查的额外方法段落，以及后续单独制作的关系复核表。评估方可查来源，生成端不接收这些原图或核查答案。
- **运行前固定**：实际正文摘录及校验值、提示词、风格预设、组件、技能和 Agent 流程版本。不能把选材报告中的结构提示当成补充示范。检验结果产生后，若再用这些案例修改技能，须记录用途改变，不能继续沿用原来的独立检验结论。

独立检验指三篇未用于本项目这一轮流程开发。它不表示基础模型从未见过论文。仅隐藏图片，也无法排除模型记忆原图。运行记录应保留这一限制。

## 选择结论与后续边界

保留三篇，不扩大候选集。Self-RAG 与 IRCoT 都有重复过程，但前者重点是条件与候选评价，后者重点是交替推理与资料累积。RECOMP 增加不同的中间压缩结构，因此不需要再补入一篇普通单次检索流程。

IRCoT 图 1 是简化案例，所以改选图 2。图 2 仍以检索方法为主，因此明确让 §3.2 补齐最终阅读器。RECOMP 图 2、图 3 是压缩器学习算法，不适合本轮推理总览，所以选图 1。上述范围调整没有新增论文或作图任务。

公开仓库只保存本报告与来源引用。没有复制目标原图，也没有作出原图、重绘图或外部素材可再分发的许可结论。若后续要公开打包论文图片或作者素材，仍需单独核实对应文件的使用条件。

目标仓库没有 `todo.mdx`、`pending-test.mdx` 等进度文件。本次只有研究选材，没有产品功能或待办状态变化，因此未新增进度文件或版本记录。评估方后续依据已经固定的任务范围制作复核表；本报告不提供完整关系标准答案。

[self-record]: https://proceedings.iclr.cc/paper_files/paper/2024/hash/25f7be9694d7b32d5cc670927b8091e1-Abstract-Conference.html
[self-pdf]: https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf#page=2
[ircot-record]: https://aclanthology.org/2023.acl-long.557/
[ircot-pdf]: https://aclanthology.org/2023.acl-long.557.pdf#page=4
[recomp-record]: https://proceedings.iclr.cc/paper_files/paper/2024/hash/bda88ed2892f5e61c9a9bf215c566913-Abstract-Conference.html
[recomp-pdf]: https://proceedings.iclr.cc/paper_files/paper/2024/file/bda88ed2892f5e61c9a9bf215c566913-Paper-Conference.pdf#page=2
