# 论文风格包的装载方式与边界

对应研究议题：[open-design 的装载方式如何用于论文风格包](https://github.com/UnknownObject777/academic-visual-library/issues/4)。

研究结论：现有绘图工具已经能接收可复用的样式值。第二期可以先研究“说明、参数、组件、例子、来源证据”的组合。自动发现、版本选择和画布装载仍需后续实现。具体包格式与人工确认方式尚未决定。

本次仅阅读源码和核对一手资料，没有运行生成、测试或构建，也没有修改技能或执行系统。

## 核实范围

| 仓库 | 固定快照 | 核实重点 |
|---|---|---|
| academic-visual-library | [9fee65fe][academic-root]，插件 v0.3.0 | 参考风格、原生 PPT 绘图、技能入口、素材改造与检查边界 |
| open-design | [6b60b567][od-root] | 设计包清单、运行时读取、提示词组合、技能附属文件复制、来源与修订 |
| paperfigure-workbench | [1588dc44][wb-root] | 能力块组合器、实际对话输入路径 |

以下“已实现”仅说明源码或文档中存在相应机制。它不代表本研究完成了运行验证，也不证明论文配图效果。

## open-design 可以借鉴的机制

| 机制 | 已核实的行为 | 对论文配图的启发 |
|---|---|---|
| 包的发现与声明 | 新设计包以 `manifest.json` 声明身份、来源和文件。核心文件为 `DESIGN.md` 与 `tokens.css`。清单还可声明使用说明、组件、预览、字体及来源文件。 | 一个可分享单元应能说明自己是什么、适用什么、需要读哪些文件。[包说明][od-guide]、[清单定义][od-schema] |
| 说明与实际值分开 | `DESIGN.md` 解释设计意图；`tokens.css` 提供实际值。组件摘要来自组件样例，部分文件是派生结果。 | 规则、实际值、可编辑样例应相互对应，避免多份独立维护的数值。[包说明][od-guide] |
| 轻量注入，按需读资料 | 组合器依次加入使用说明、设计正文、参数与组件摘要；复杂资料通过清单索引按需读取。读取器检查请求文件是否属于声明范围。 | 不必把所有参考论文、图片和组件一次塞进上下文。[读取器][od-read]、[组合器][od-prompt] |
| 技能附属文件可访问 | 活跃技能在运行前复制到项目的 `.od-skills/`。提示词提供相对路径与绝对路径备用说明。设计包正文则直接进入提示词，不走同一套复制流程。 | 执行技能与视觉预设可以组合使用，但不必共用完全相同的装载方式。[技能协议][od-skills]、[路径说明代码][od-preamble]、[运行前处理][od-stage] |
| 来源证据有结构 | 清单的 GitHub 来源可记录分支和提交。参数证据记录值、来源位置与用途；提取报告也保存扫描文件和警告。 | 参考图的观测值和解释应能返回来源，不把推测写成作者原始设计规则。[清单定义][od-schema]、[证据收集器][od-evidence] |
| 格式版本与内容标识不同 | `schemaVersion` 表示包格式。运行上下文另有内容摘要；用户设计系统还有待接受、已接受或已拒绝的修订记录。 | 包格式版本、风格内容版本、某次作图所用内容需要分别识别。[清单定义][od-schema]、[内容摘要][od-digest]、[修订记录][od-revisions] |

需要保留两个边界：

- open-design 的参数提取器主要扫描代码和样式文本。它不等于“从论文 PDF 自动恢复作者设计系统”。多篇论文中的图片分析和科学组件归纳仍需另行验证。[证据收集器][od-evidence]
- open-design 内置的 `paper` 包归类为“Retro & Nostalgic”。这个名字不表示它符合学术论文投稿规范。[Paper 包清单][od-paper]

## 现有 academic-visual-library 能承接什么

| 现有能力 | 事实与限制 |
|---|---|
| 参考图决定视觉语言 | 工作流先读科学材料，再观察参考图。当前参考风格参数明确标为近似重建，不能当作作者原始参数或 IEEE 规范。[工作流][academic-workflow]、[参考参数][academic-palettes] |
| 具体值可以复用 | `createFigure({widthMm,heightMm,style}, artifact)` 接收字体、字号、颜色、线宽和箭头几何等样式值。组件几何和相对布局已有辅助函数。函数中也有实现默认值；这些值不等于所有论文都适用的规范。[绘图工具][academic-native] |
| 已有原生 PPT 路线 | 原生对象、真实文字、局部替换、实际尺寸检查和导出工具已经存在。合成例子展示了这条路线；它不是发表论文的重建案例，也不是跨论文评测结果。[原生 PPT 说明][academic-ppt] |
| 已有可编辑素材 | 技能支持选择并改造 draw.io、PPT 和 SVG 素材。它要求把模块关系与目标方法核对。SVG 图片在 PPT 内仍可能只是图片对象，不能直接称为原生形状。[素材技能][academic-assets] |
| 可直接沿用现有格式 | 工作流允许短说明和代码中的样式对象。draw.io 可直接编辑 XML，PPT 可使用原生对象；现有技能不要求先建立统一场景格式。[工作流][academic-workflow]、[素材技能][academic-assets] |
| 多参考图已有处理原则 | 参考图可以各自承担配色、构图或插画等角色；科学关系来自目标方法。相互矛盾的参考不能未经判断就混合。[参考迁移][academic-reference] |

本快照没有提供一个可自动发现、选择、提取、版本管理并导入论文风格包的独立执行器。现有能力是 Agent 阅读参考材料，再使用现有工具绘制。不能把“技能能阅读文件”写成“已实现完整风格包管理”。

## 画布工作台的真实边界

`CapabilityBlock` 与 `composePrompt` 已有类型和文本组合逻辑。该文件明确说明能力内容属于预留位置。[组合器][wb-prompt]

本次检索非测试 TypeScript、TSX 和 MJS 源码时，没有发现这个组合器的正式调用方。实际 `buildTurnInput` 负责加入历史、当前用户消息和本地图片，然后交给 `turn/start`。[实际输入路径][wb-runtime]

因此，当前证据只能支持“预留了接口”。本快照不能证明工作台已经扫描外部能力包、复制附属文件、选择风格预设或把包内容加入实际执行。原生 Codex 自己的技能发现能力，也不等于工作台已经实现这些功能。

## 建议区分的四类内容

以下是供后续议题选择的组织方式，尚非已确定的包规范。

| 内容 | 保存什么 | 不能从它推出什么 |
|---|---|---|
| 投稿规范 | 目标会议或期刊、提交阶段、规范来源、适用版本、图形类型、尺寸/文字/文件要求与例外 | 某篇论文的配色、圆角和布局就是官方要求 |
| 视觉预设 | 字体角色、语义颜色、线条、箭头、间距、密度、分组与布局原则，以及观察证据 | 同一风格必然具有相同模块、箭头和科学关系 |
| 领域组件 | 可编辑几何、科学含义、输入输出、允许的连接方式、适用条件与反例 | 一个外观相似的模块可以替代另一种科学操作 |
| 执行技能 | 阅读证据、选择预设与组件、绘制、检查、局部修订、导出和说明限制的过程 | 机械检查通过就代表科学正确或风格一致 |

官方资料支持把出版要求单独保存。例如，IEEE 的图形页面分别讨论分辨率、尺寸、文件格式和灰度可理解性；Nature 的图形指南要求文字与线条可编辑，并区分文字、照片和导出要求。它们的适用对象与提交阶段需要随记录一起保留。[IEEE 图形指南][ieee]、[Nature 图形指南][nature]

同一个规则记录可以保存“目标来源、页面或条款、适用对象、要求或建议、核实版本”。这只是建议字段，尚未选择序列化格式。不能把某个会议要求、工具默认值或一张参考图的特征改写成所有领域的通则。

## 从多篇论文归纳时，需要留下什么证据

这部分属于研究建议，不表示现有系统已经实现自动提炼。

自动归纳已有研究先例。PaperBanana 在附录 F.2 中分批分析参考图的颜色、形状和字体，再合并局部报告形成风格指南。这提供了一种可研究的归纳过程；该过程本身不证明已形成可执行参数或可编辑组件包，统一指南也不等于保留了不同参考风格的差异。[原论文附录][paperbanana]

| 观察或判断 | 建议保留的记录 | 处理原则 |
|---|---|---|
| 从原生文件直接读取 | 论文稳定标识、版本、图号、对象或参数位置、原始值 | 说明来源是原生对象，而非像素估计 |
| 从图片估计颜色或几何 | 原图和区域、估计方法、观测值、误差或不确定性 | 标明近似值，不冒称作者原始参数 |
| 多张图反复出现的特征 | 哪些图支持、哪些图不支持、适用范围 | 反复出现是归纳依据，不是全领域规则 |
| 颜色或形状的科学含义 | 图注、方法文本或代码证据，以及观察者解释 | 参考图只提供外观时，不能顺带移植它的科学含义 |
| 局部特例或冲突 | 相互冲突的规则、各自来源、最终选择与理由 | 不静默平均参数；必要时形成不同预设或明确条件 |
| 尚未确认的推断 | 推断内容、理由、待核实信息 | 与已观察事实分开，允许用户修正 |

这些建议延续了现有技能“科学材料、风格参考与被编辑图稿分开”和“不同参考各有明确作用”的原则。[参考迁移][academic-reference]

可归纳的不只是颜色。还应讨论什么情况下使用并列对比、闭环、主图与细节图，以及标签、箭头与留白如何协作。规则应描述适用条件，不为新论文预定科学拓扑。[样式到布局][academic-layout]

检验提炼是否有用，需要在未参与提炼的方法上作图。保持目标方法的科学关系，检查预设是否仍可使用，组件缺失在哪里，用户需要修改什么。具体任务、数量和接受标准由评测与试点议题确定。

## 两种最小组合选项

### 选项 A：先使用现有技能目录与编辑源文件

把风格说明、少量 YAML 或代码样式值、可编辑组件、对照预览和来源说明放在一个可明确引用的目录中。Agent 读取选定内容，再将值交给现有 PPT 工具，或直接编辑 SVG/draw.io 源文件。

- 能沿用现有作图路线，适合先检验案例与组件是否有帮助。
- 尚无自动发现、安装、切换或版本锁定；使用者需要明确指定目录和内容版本。
- 不应为每种输出建立各自独立维护的颜色与字体表。可以在作者脚本中转换物理单位或读取共用值。
- SVG 进入 PPT 后的编辑程度，仍需按实际对象说明。

### 选项 B：在已验证的目录内容上增加最小清单

增加身份、适用范围、内容版本、来源和文件索引，再实现少量发现与读取逻辑。执行技能和预设保持独立，通过一次作图选择组合。

- 可以支持以后按包选择、复现旧结果和接入工作台。
- 需要新开发，当前仓库没有完整实现。
- 先只传短说明、参数和组件索引，图片与完整案例按需读取。
- 是否复制到作图工作区、哪些内容需要冻结，以及如何确认用户提炼结果，需要用户决定。

两种选项都不要求复制 open-design 全部网页参数、HTML 组件格式或插件市场。值得借鉴的是文件分工、可追溯来源、轻量索引和执行时可访问，而不是网页样式字段本身。

## 后续仍需用户决定

- 首个试点的实际输出格式，以及允许出现哪些非原生对象。
- 投稿规范、预设和组件能否单独贡献与升级。
- 用户提供多篇论文时，是先人工选择一致的参考组，还是允许系统提出分组供确认。
- 哪些提炼结果需要确认，怎样显示无法确定的数值与科学含义。
- 先采用明确引用的目录，还是先做可发现的包与装载入口。
- 一次作图如何记录所用规则、组件和工具版本，才能进入后续案例与评价。

研究已经补齐机制与可选方案。包格式、人工确认方式与社区审核规则留在对应决策议题中，本研究没有代替用户作出选择。

[academic-root]: https://github.com/UnknownObject777/academic-visual-library/tree/9fee65fe33143b2f71dfc5284be45c1efbc88022
[academic-workflow]: https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/skills/academic-figure-workflow/SKILL.md
[academic-palettes]: https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/assets/style-palettes.yaml
[academic-native]: https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/skills/academic-figure-workflow/scripts/figure-native.mjs
[academic-ppt]: https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/docs/native-ppt-figures.md
[academic-assets]: https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/skills/academic-visual-assets/SKILL.md
[academic-reference]: https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/skills/academic-figure-workflow/references/reference-style.md
[academic-layout]: https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/skills/academic-figure-workflow/references/style-to-layout.md
[od-root]: https://github.com/nexu-io/open-design/tree/6b60b567ac8bef60cbedd2f4c89cc494b4dbb361
[od-guide]: https://github.com/nexu-io/open-design/blob/6b60b567ac8bef60cbedd2f4c89cc494b4dbb361/docs/design-systems.md
[od-schema]: https://github.com/nexu-io/open-design/blob/6b60b567ac8bef60cbedd2f4c89cc494b4dbb361/design-systems/_schema/manifest.schema.ts
[od-read]: https://github.com/nexu-io/open-design/blob/6b60b567ac8bef60cbedd2f4c89cc494b4dbb361/apps/daemon/src/design-systems/index.ts#L561-L662
[od-prompt]: https://github.com/nexu-io/open-design/blob/6b60b567ac8bef60cbedd2f4c89cc494b4dbb361/apps/daemon/src/prompts/system.ts#L1275-L1325
[od-skills]: https://github.com/nexu-io/open-design/blob/6b60b567ac8bef60cbedd2f4c89cc494b4dbb361/docs/skills-protocol.md#L140-L149
[od-preamble]: https://github.com/nexu-io/open-design/blob/6b60b567ac8bef60cbedd2f4c89cc494b4dbb361/apps/daemon/src/skills.ts#L532-L588
[od-stage]: https://github.com/nexu-io/open-design/blob/6b60b567ac8bef60cbedd2f4c89cc494b4dbb361/apps/daemon/src/server.ts#L11320-L11354
[od-evidence]: https://github.com/nexu-io/open-design/blob/6b60b567ac8bef60cbedd2f4c89cc494b4dbb361/apps/daemon/src/design-systems/token-evidence.ts
[od-digest]: https://github.com/nexu-io/open-design/blob/6b60b567ac8bef60cbedd2f4c89cc494b4dbb361/apps/daemon/src/design-systems/index.ts#L709-L742
[od-revisions]: https://github.com/nexu-io/open-design/blob/6b60b567ac8bef60cbedd2f4c89cc494b4dbb361/apps/daemon/src/design-systems/index.ts#L1480-L1514
[od-paper]: https://github.com/nexu-io/open-design/blob/6b60b567ac8bef60cbedd2f4c89cc494b4dbb361/design-systems/paper/manifest.json
[wb-root]: https://github.com/UnknownObject777/paperfigure-workbench/tree/1588dc44475306a4e044574c284617bbe4d24596
[wb-prompt]: https://github.com/UnknownObject777/paperfigure-workbench/blob/1588dc44475306a4e044574c284617bbe4d24596/daemon/src/agents/prompt.ts
[wb-runtime]: https://github.com/UnknownObject777/paperfigure-workbench/blob/1588dc44475306a4e044574c284617bbe4d24596/daemon/src/agent/runtime.ts#L322-L333
[ieee]: https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/
[nature]: https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/
[paperbanana]: https://arxiv.org/html/2601.23265v2#A6.SS2

