# 第二期试点：现有能力与经典论文候选

研究议题：[现有能力与经典论文候选能支撑怎样的首个试点](https://github.com/UnknownObject777/academic-visual-library/issues/2)。

本研究只提供选型事实。第二期优化技能与 Agent 的使用效果，不训练或微调基础模型。首个子领域、验收标准、样本数量和贡献规则，仍由后续议题确定。

## 研究依据与证据范围

- 本仓库基线为 `9fee65fe33143b2f71dfc5284be45c1efbc88022`，插件版本为 v0.3.0。以下仓库链接均固定到该提交。
- 论文候选来自 Foundations-of-LLMs 的[经典论文列表][foundations-list]。列表版本固定为 `1109bfa8e1c5b83fd25f66435601eef2a5905d5b`。
- 核对了仓库源码、检查脚本、合成示例及预览。没有执行项目测试、构建或新的画图任务。
- 直接查看了 LoRA、Adapter、Prefix-Tuning、QLoRA、RAG、REPLUG、Self-RAG、RETRO 的目标 PDF 页。论文版本和图号见下表。Atlas 只核对了论文正文与图注，未完成目标图的视觉检查。
- “代码存在”“已有示例”“效果经过比较”分开记录。已有检查代码，不等于本研究重新执行通过。

## v0.3.0 已经具备什么

| 能力 | 当前证据 | 能说明什么，尚不能说明什么 |
| --- | --- | --- |
| 技能入口 | [插件清单][plugin]；[主流程][workflow]；[原生 PPT 指南][native-guide] | 实际有七个技能目录。主流程、内容分析、资产浏览之外，还有设计、稿件分析、参考图分析、代码分析入口。五个 v5 入口沿用已有用法，并非必须串行调用的五个 Agent。 |
| 论文到图的工作规则 | [主流程][workflow] | 已要求从正文、图注和必要代码确认标签、关系与训练/推理边界。参考图决定视觉处理，目标论文决定科学关系。这是操作规则，尚非真实论文任务的成功率证据。 |
| 原生可编辑 PPT | [figure-native.mjs][native-code] | 已提供毫米几何、字号、文本、形状、折线/曲线箭头、相对布局和等比例视图工具。依赖当前 Codex 提供的文稿运行环境，并非脱离宿主也能运行的完整 Agent 服务。 |
| 局部修改与机械检查 | [局部替换工具][patch-code]；[PPT 检查工具][audit-code]；[PowerPoint 导出][export-code] | 已能限制替换范围，保留未选对象，检查最终尺寸下的文字、字体、相对对齐、箭头和包内变化。PowerPoint 导出会使用临时副本，并读取实际文字边界。机械检查仍要求单独的科学与视觉复核。 |
| 真实可见的执行示例 | [示例文字][fixture-text]；[绘制代码][fixture-code]；[PPT][fixture-ppt]；[PNG][fixture-png] | 已展示材料筛选的主动学习循环。指南记录了 PowerPoint 渲染与文字边界检查。这是合成描述，不是已发表论文，不是实验结果，也不是跨领域有效性的证据。 |
| 可复用素材与风格参数 | [资产入口][asset-skill]；[风格参数][palette]；[来源记录][provenance] | 有 37 份网络结构条目、20 个模块原语、10 个 SVG 图标，以及 draw.io/PPT 素材。四套风格参数是参考图的近似重建。模板不是已认证的科学真值，参数也不是 IEEE 官方配色。 |
| 检查代码与持续检查配置 | [素材检查][bundle-tests]；[原生几何检查][native-tests]；[PPT/PNG 检查][ppt-tests]；[工作流配置][ci] | 有素材解析、原生对象、来源、链接检查；有几何检查与 11 项 PPT/PNG 检查。配置会调用这些工具。它们不评估论文理解、参考风格一致性或新论文上的效果。 |

因此，二期可以从现有原生绘图和修改工具开始。无需重写一套文本到 PPT 的底层能力。当前也不能继续沿用“只有三个技能、没有执行工具、没有示例”的旧描述。

## 两个候选子领域有什么不同

此处的参数高效微调，指论文题材。它不表示要微调本项目使用的模型。

| 比较项 | 参数高效微调 | 检索增强生成 |
| --- | --- | --- |
| 适合解释的问题 | 哪些参数更新；新增模块位于哪里；前向、梯度和更新路径如何区分 | 查询怎样获得资料；资料怎样进入生成；何时检索、选择、重排或反馈 |
| 重复出现的组件 | 冻结/可训练模块、特征条、投影、加法、残差、训练状态 | 查询、文档、检索器、索引、生成器、并行分支、选择和循环 |
| 科学检查的优势 | 局部关系明确。容易针对模块位置、分支和训练状态写具体检查项 | 总览图与用户需求更接近。容易检查缺失步骤、条件分支和资料去向 |
| 容易出现的假进步 | 只会重画 LoRA 的小模块，却声称会生成完整方法总览 | 把不同方法都画成“检索→生成”，省略各方法的关键差别 |
| 当前工具适配 | 原生形状、共享箭头、细节视图可直接复用 | 原生形状和流程布局可复用。长文本、并行分支与循环会增加排版难度 |
| 可以检验的迁移 | 相同视觉处理能否表达不同适配位置和训练机制 | 相同文档/生成组件能否表达不同检索与生成组织方式 |

以上适用性是研究判断，不是跑图后的比较结果。若优先验证科学关系与组件复用，可先比较参数高效微调候选。若优先验证完整方法总览，可先比较 RAG 与 REPLUG。研究不替用户选择。

## 代表论文与具体任务

PDF 页按文件从 1 开始计数。图号只属于所列版本。会议发表信息与实际查看的 PDF 版本分别记录，避免混用。

### 参数高效微调候选

| 论文与稳定标识 | 发表与目标图 | 可检查的关系、可复用内容 | 对当前试点的适用边界 |
| --- | --- | --- | --- |
| **LoRA: Low-Rank Adaptation of Large Language Models**；`arXiv:2106.09685v2`；OpenReview `nZeVKeeFYf9` | ICLR 2022；实际查看 [arXiv v2 图 1，PDF 第 1 页][lora-pdf] | 预训练分支与 A/B 分支共同接收输入，再相加；只训练 A/B。可复用并行分支、参数状态、加法与投影。 | 很适合小范围关系检查和组件抽取。但图 1 是局部重参数化图，单独成功不能证明完整方法总览能力。ICLR 发表信息见[论文页][lora-record]。 |
| **Parameter-Efficient Transfer Learning for NLP**；`pmlr-v97-houlsby19a`；`arXiv:1902.00751` | ICML 2019；[正式 PDF 图 2，第 3 页][adapter-pdf] | 展示 Adapter 在 Transformer 层中的两个插入位置，以及降维、非线性、升维和内部残差。图注还说明 Layer Norm 等参数参与训练。 | 适合总览加细节，以及重复组件。不能把它简化成“只更新 Adapter，其他全部冻结”。图 1 是性能曲线，当前方法图任务应选图 2。 |
| **Prefix-Tuning: Optimizing Continuous Prompts for Generation**；`2021.acl-long.353`；DOI `10.18653/v1/2021.acl-long.353` | ACL-IJCNLP 2021；[正式 PDF 图 2，第 4 页][prefix-pdf] | 区分自回归模型与编码器—解码器模型；前缀、输入与目标区域不同；前缀作用于各层激活，不只是可见自然语言提示词。 | 适合验证特征条与分组组件，以及更换拓扑后保持风格。原图包含较多索引和示例文字，不能靠缩小文字解决。 |
| **QLoRA: Efficient Finetuning of Quantized LLMs**；`arXiv:2305.14314`；NeurIPS 论文标识 `1feb87871436031bdc0f2beaa62a049b` | [NeurIPS 2023][qlora-record]；[正式 PDF 图 1，第 3 页][qlora-pdf] | 并排比较全量微调、LoRA、QLoRA；区分基座、Adapter、优化器状态；参数更新、梯度、分页是不同箭头。正文区分 4-bit 存储与计算精度。 | 适合作为 LoRA 后的变化任务，检查复用组件时是否保留新增语义。但它不是普通数据处理流水图；不能把所有箭头解释为前向数据流，也不能称所有计算均为 4-bit。 |

### 检索增强生成候选

| 论文与稳定标识 | 发表与目标图 | 可检查的关系、可复用内容 | 对当前试点的适用边界 |
| --- | --- | --- | --- |
| **Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks**；`arXiv:2005.11401`；NeurIPS 论文标识 `6b493230205f780e1bc26945df7481e5` | NeurIPS 2020；[正式 PDF 图 1，第 2 页][rag-pdf] | 查询编码器、文档索引、MIPS、候选文档、生成与边缘化；训练路径另行标示。方法正文区分 RAG-Sequence 与 RAG-Token。 | 很贴近方法总览。可复用文档、检索器、索引和生成器。不能把原方法替换为泛泛的“把资料拼在提示词前”；若不画两种变体，必须写清所画范围。 |
| **REPLUG: Retrieval-Augmented Black-Box Language Models**；`2024.naacl-long.463`；DOI `10.18653/v1/2024.naacl-long.463` | [NAACL 2024][replug-record]；[正式 PDF 图 2，第 3 页][replug-pdf] | 每份检索文档分别与上下文组合，经同一个黑盒模型得到输出分布，再集成。可复用文档、生成器、并行分支与汇合。 | 图 2 是明确的推理总览，比只选图 1 的概念对比更接近任务。不能画成把所有文档一次性拼接。检索器训练方案属于另一范围，需另读相关正文。 |
| **Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection**；`arXiv:2310.11511v1`；OpenReview `hSyW5go0v8` | 作者[官方仓库][selfrag-repo]确认 ICLR 2024；本研究查看 [arXiv v1 图 1，第 2 页][selfrag-pdf] | 需要/无需检索的分支、并行生成、反思标记、候选选择与重复生成。可复用检索/文档组件，但要新增选择和循环关系。 | 适合作为更复杂的方法变化。原图文字较密，不能作为最简单的首次任务。v1 图 2 是训练样例，并非完整训练系统图。会议 PDF 与 v1 的图号一致性仍需正式采样时核对。 |
| **Improving Language Models by Retrieving from Trillions of Tokens（RETRO）**；`pmlr-v162-borgeaud22a`；`arXiv:2112.04426` | ICML 2022；[正式 PDF 图 2，第 4 页][retro-pdf] | 冻结检索器、编码器、分块交叉注意力，以及总览和细节的对应；关键是分块位置与因果关系。 | 可作为提高难度后的候选。它不是普通检索问答流程，连线和下标更密。先完成 RAG/REPLUG，也不能据此声称已经支持 RETRO。 |
| **Atlas: Few-shot Learning with Retrieval Augmented Language Models**；`JMLR 24(251)`；`arXiv:2208.03299` | [JMLR 2023，期刊论文][atlas-record]；[正式 PDF 图 1，第 3 页][atlas-pdf] | 图注说明预训练与微调均使用检索；正文描述检索器与 Fusion-in-Decoder。 | 可作为放宽会议范围后的候选，不能计入纯 AI 会议样本。当前只核对了正文与图注；图 2 是任务输入输出例子，不是方法结构图。 |

列表中的 QLoRA、REPLUG、Self-RAG 曾标为 arXiv 材料。上表依据正式论文页或作者信息补充发表状态。候选的身份依赖稳定标识，不能只保留列表标题和年份。

### 著名但不应直接入选的内容

- **综述与教材插图**：适合找主题与视觉参考，通常没有单一方法的关系真值。不能把综述分类图当成一个方法的标准答案。
- **性能曲线、排行榜、资源数字**：需要真实数据及其出处。本次方法总览不能把这些内容当成装饰补入。
- **只有局部模块的图**：LoRA 图 1 可以验证局部能力。若把局部图任务改为整套训练/推理总览，需要补充正文证据和新的目标定义。
- **只有标题相近的论文**：列表存在两个不同含义的 DoRA。未来采样需要用论文标识区分，不能按简称自动合并。

经典论文适合发现常见结构错误。它们可能已出现在基础模型的训练语料中，因此“本项目未用过的论文”不等于“模型从未见过的论文”。新论文检验至少要独立于本项目开发案例；更强的泛化结论还需要额外设计。

## 后续贡献协议需要保留的来源信息

以下是来源记录需求，不判断某项使用是否获得授权。对许可、权利归属和可再分发范围尚未核实的内容，保留待核实状态。

| 对象 | 应保留的记录 | 仍需逐项核实 |
| --- | --- | --- |
| 原论文图、截图、裁剪参考图 | 论文稳定标识、版本、出版页/PDF 链接、图号、页码、图注；原文件与裁剪关系；获取副本的校验值；原文展示的署名及许可链接 | 目标图是否含第三方素材；论文版本的使用条件；贡献者是否能公开打包原图。 |
| 根据论文重新绘制的图 | 科学内容来源；原图与新图分别标识；重绘者、修改说明；参考图提供的是风格还是科学关系；编辑源文件与预览对应版本 | 与原图和原素材有关的使用条件，贡献者是否能按所选条件分发重绘文件。不能仅写“重新画过”。 |
| 作者提供的 PPT/SVG/draw.io 等源文件 | 作者发布位置、仓库及固定提交、原始文件名、校验值、许可证和授权说明；外部字体、图片、图标来源 | 代码仓库的许可是否明确覆盖这些文件；文件是否包含单独声明的第三方内容。不能把“能下载源文件”当作来源条件已经核清。 |
| 新建通用组件或风格包 | 贡献者、可编辑源文件、依赖素材与许可、设计参考、功能含义、可改参数、适用/不适用例子，以及验证记录 | 哪些来自已有资产，哪些由贡献者新建；组件的科学适用范围；所用字体/图标/参考图的条件。 |

已发现的来源事实：Foundations-of-LLMs 的[仓库许可证][foundations-license]标题为 `Attribution-NonCommercial-NoDerivatives 4.0 International`。它不是本研究对所列各篇论文或其插图作出的许可结论。ACL Anthology 的[论文页][prefix-record]另列材料使用说明。实际贡献应回到被使用文件及对应版本核实。

本仓库已有[来源清单][provenance]和[第三方声明][notices]，可沿用记录思路。它们记载了素材来源，不证明未来导入的论文图片也具有相同条件。

## 无需重复建设，真正缺的证据是什么

第一版无需重写原生形状、共享箭头、PPT 局部修改、最终尺寸检查、PNG 导出、素材目录及基础来源记录。也无需为了启动试点，先引入一套强制的中间场景格式。现有[主流程][workflow]允许具体风格值保存在绘图代码中。

真正缺少的证据是：

1. **真实论文的完整案例**。同一案例需要关联输入、目标范围、科学关系出处、风格参考、生成源文件、最终预览、检查与修订。当前合成循环示例只证明较窄的执行路径。
2. **固定输入下的比较**。至少区分基础做法、当前技能，以及新增资产/风格处理后的表现。模型、工具、提示、人工修改与失败记录都应可追溯。具体规模和评价标准仍待决定。
3. **分别判断科学与视觉**。科学关系正确、风格接近、印刷尺寸可读、对象可编辑，是不同结论。PPT 检查通过不能替代前三项。
4. **同一资产在不同论文上的复用**。要证明重复组件保留了含义，也要证明不同论文没有套上同一布局。仅增加组件数量或展示好看的重绘图，不能回答这个问题。
5. **开发之外的检验**。选定样本用途后，再分配开发案例与独立检验案例。不能一边用检验案例改技能，一边仍称它为独立检验。
6. **真实贡献和复用记录**。尚未见正式的案例贡献、风格包贡献及审核流程。社区是否有效，需要看别人能否提交、核实、加载、修改和再次使用，而不是只统计上传数量。

这些证据需求不预先规定必须多 Agent、自动评分或微调模型。应先找出失败来自理解、布局、组件、执行还是检查，再决定需要调整哪部分。

## 本研究交给后续议题的选择

- 参数高效微调与检索增强生成，哪个更符合首批用户和当前效果问题。
- 首次验收针对完整总览、局部机制，还是总览加细节；选中的图要与任务范围一致。
- 风格预设如何区分出版物要求、参考图的视觉处理、科学组件语义；不能把会议名称当成统一配色。
- 样本用途、评价者、可接受结果、投入与停止条件；本研究未设定数量或通过分数。
- 哪些来源条件能够支持公开贡献，哪些材料只保留引用或等待补充说明。

本研究没有选定子领域，没有制作论文样本，没有验证新 Agent 的效果，也没有作出来源使用的法律结论。

[plugin]: https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/.codex-plugin/plugin.json
[workflow]: https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/skills/academic-figure-workflow/SKILL.md
[native-guide]: https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/docs/native-ppt-figures.md
[native-code]: https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/skills/academic-figure-workflow/scripts/figure-native.mjs
[patch-code]: https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/skills/academic-figure-workflow/scripts/patch_native_shapes.py
[audit-code]: https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/skills/academic-figure-workflow/scripts/audit_pptx.py
[export-code]: https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/skills/academic-figure-workflow/scripts/export_powerpoint.ps1
[fixture-text]: https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/skills/academic-figure-workflow/examples/active-learning.md
[fixture-code]: https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/skills/academic-figure-workflow/examples/active-learning.mjs
[fixture-ppt]: https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/assets/examples/active-learning.pptx
[fixture-png]: https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/assets/examples/active-learning.png
[asset-skill]: https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/skills/academic-visual-assets/SKILL.md
[palette]: https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/assets/style-palettes.yaml
[provenance]: https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/assets/provenance.json
[notices]: https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/THIRD_PARTY_NOTICES.md
[bundle-tests]: https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/tests/test_bundle.py
[native-tests]: https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/skills/academic-figure-workflow/tests/test_native.mjs
[ppt-tests]: https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/skills/academic-figure-workflow/tests/test_pptx_tools.py
[ci]: https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/.github/workflows/validate.yml
[foundations-list]: https://github.com/ZJU-LLMs/Foundations-of-LLMs/blob/1109bfa8e1c5b83fd25f66435601eef2a5905d5b/%E5%A4%A7%E6%A8%A1%E5%9E%8B%E7%BB%8F%E5%85%B8%E8%AE%BA%E6%96%87%E5%88%97%E8%A1%A8/readme.md
[foundations-license]: https://github.com/ZJU-LLMs/Foundations-of-LLMs/blob/1109bfa8e1c5b83fd25f66435601eef2a5905d5b/LICENSE.md
[lora-pdf]: https://arxiv.org/pdf/2106.09685v2#page=1
[lora-record]: https://openreview.net/forum?id=nZeVKeeFYf9
[adapter-pdf]: https://proceedings.mlr.press/v97/houlsby19a/houlsby19a.pdf#page=3
[prefix-record]: https://aclanthology.org/2021.acl-long.353/
[prefix-pdf]: https://aclanthology.org/2021.acl-long.353.pdf#page=4
[qlora-record]: https://proceedings.neurips.cc/paper_files/paper/2023/hash/1feb87871436031bdc0f2beaa62a049b-Abstract-Conference.html
[qlora-pdf]: https://proceedings.neurips.cc/paper_files/paper/2023/file/1feb87871436031bdc0f2beaa62a049b-Paper-Conference.pdf#page=3
[rag-pdf]: https://proceedings.neurips.cc/paper/2020/file/6b493230205f780e1bc26945df7481e5-Paper.pdf#page=2
[replug-record]: https://aclanthology.org/2024.naacl-long.463/
[replug-pdf]: https://aclanthology.org/2024.naacl-long.463.pdf#page=3
[selfrag-repo]: https://github.com/AkariAsai/self-rag
[selfrag-pdf]: https://arxiv.org/pdf/2310.11511v1#page=2
[retro-pdf]: https://proceedings.mlr.press/v162/borgeaud22a/borgeaud22a.pdf#page=4
[atlas-record]: https://jmlr.org/papers/v24/23-0037.html
[atlas-pdf]: https://jmlr.org/papers/volume24/23-0037/23-0037.pdf#page=3
