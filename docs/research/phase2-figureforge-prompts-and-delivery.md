# FigureForge 参考研究：提示词与可编辑交付

研究议题：[FigureForge 的提示词与可编辑流程怎样用于第二期试点](https://github.com/UnknownObject777/academic-visual-library/issues/13)。

本文用于第二期方案讨论。源码事实和建议分别记录；提示词是可复制试用的草案。本次只阅读代码和资料，没有运行模型生成、浏览器编辑或 Office 验收，也没有开发正式功能。

## 研究结论

FigureForge 已提供一条有价值的参考路线：检索同类参考图，归纳共同视觉规则，再生成 SVG 或位图；位图可以继续重建为对象场景，并由同一场景生成多种文件。生成、重建、检查、局部修复和导出分别有代码支持。[参考归纳与生成](https://github.com/qwdwqfwq/topconf-paper-figure-gallery/blob/dbf360a533ee46bc7d4a8f6037717c83f21a633a/forge/index.html#L1785-L2214)、[重建与导出](https://github.com/qwdwqfwq/topconf-paper-figure-gallery/blob/dbf360a533ee46bc7d4a8f6037717c83f21a633a/forge/index.html#L5315-L5450)

第二期适合借用这套分阶段方法，并增加一个明确的前置步骤：从论文建立方法证据清单。参考图决定视觉表达，论文材料决定模块、关系、标签与科学解释。这个前置步骤是本项目的建议，不能归为 FigureForge 已完整实现的能力。

提示词可以明确内容、风格、对象范围和修订约束。直接编辑、保存、版本检查、导出与真正的对象可编辑性需要程序实现，并用实际操作证明。推荐先讨论以受支持的原生图元直接生成方法总览图；位图生成后重建可作为需要单独评估的路线。两条路线的编辑损失与人工修订成本需要分别记录。

## 固定来源与证据范围

| 来源 | 固定版本 | 本次用途 |
|---|---|---|
| topconf-paper-figure-gallery | [`dbf360a533ee46bc7d4a8f6037717c83f21a633a`](https://github.com/qwdwqfwq/topconf-paper-figure-gallery/tree/dbf360a533ee46bc7d4a8f6037717c83f21a633a) | 提示词、检索、SVG 检查、重建、局部补丁与导出源码 |
| academic-visual-library | [`9fee65fe33143b2f71dfc5284be45c1efbc88022`](https://github.com/UnknownObject777/academic-visual-library/tree/9fee65fe33143b2f71dfc5284be45c1efbc88022) | 现有原生绘图、局部修订、检查工具和交付规则 |
| 用户提供的 PPT 配图计划 | 用户在本次讨论提供的文本 | 待核查建议，不作为现有能力证明 |

源码存在只能证明有相应实现。本次没有测量真实模型在新论文上的效果。上游文档中的验证报告也要区分固定样例、模拟模型响应和真实模型运行。

## 上游实际实现了什么

| 环节 | 源码与记录 | 已看到的机制 | 对第二期的含义 |
|---|---|---|---|
| 参考检索 | [`retrieval.mjs`](https://github.com/qwdwqfwq/topconf-paper-figure-gallery/blob/dbf360a533ee46bc7d4a8f6037717c83f21a633a/forge/retrieval.mjs#L43-L124) | 概念扩展、词法匹配、图像/文本语义分数和结构线索；多路排名融合；显示命中解释，明确检索分数并非准确率 | 用作参考推荐候选。相似论文主题与适合目标方法的视觉结构仍需区分 |
| 参考归纳 | [`ANALYZE_SYS` / `buildAnalyzePrompt`](https://github.com/qwdwqfwq/topconf-paper-figure-gallery/blob/dbf360a533ee46bc7d4a8f6037717c83f21a633a/forge/index.html#L1785-L1843) | 共同布局、密度、嵌套、配色、字号、线宽、层级、代表参考与视觉描述，输出 JSON | 可以借用字段和分阶段方式；保留每项规则来自哪些参考，以及规则是否适用于目标方法 |
| 归纳结果注入生成 | [`imageStyleText` / `designContractText` / `buildPrompt`](https://github.com/qwdwqfwq/topconf-paper-figure-gallery/blob/dbf360a533ee46bc7d4a8f6037717c83f21a633a/forge/index.html#L2021-L2214) | 将颜色、字号、线型、布局等具体值编入后续提示词 | 风格预设应包含可执行的值和语义角色；仅写“高级、克制、顶会风格”不够明确 |
| SVG 原生要素 | [`buildPrompt` / `SVG_SYS`](https://github.com/qwdwqfwq/topconf-paper-figure-gallery/blob/dbf360a533ee46bc7d4a8f6037717c83f21a633a/forge/index.html#L2182-L2214) | 唯一稳定 ID、真实 `<text>`、基础形状、图层顺序、完整 SVG，限制整图位图替代 | 可借用约束；实际导入、编辑和导出支持范围要由选定编辑器决定 |
| 几何检查与修复 | [`auditGeometry` / `repairSVG` / `auditAndRepair`](https://github.com/qwdwqfwq/topconf-paper-figure-gallery/blob/dbf360a533ee46bc7d4a8f6037717c83f21a633a/forge/index.html#L2469-L2688) | 离屏渲染，用 `getBBox()` 检查标签出界、超出容器和碰撞；模型只修列出的问题；缺陷数减少才接受；截断结果保留未完成标记 | 可借用“程序定位→局部修复→重查”的流程。缺陷数量下降不能证明科学关系、风格和未修改对象均正确 |
| 位图重建 | [`editableScenePrompt`](https://github.com/qwdwqfwq/topconf-paper-figure-gallery/blob/dbf360a533ee46bc7d4a8f6037717c83f21a633a/forge/index.html#L4405-L4409)、[`materializeEditableScene` 等调用](https://github.com/qwdwqfwq/topconf-paper-figure-gallery/blob/dbf360a533ee46bc7d4a8f6037717c83f21a633a/forge/index.html#L4430-L4609) | 从像素识别独立文字、边框、路径、箭头和照片裁片；保留 ID、归属、坐标和图层 | 需要视觉模型、OCR、坐标和字体校准。照片仍为图片对象；文字轮廓可编辑与文字内容可编辑要分别说明 |
| 局部补丁 | [`snapshotVersions` / `regionObjectCatalog` / `applyRegionPatch`](https://github.com/qwdwqfwq/topconf-paper-figure-gallery/blob/dbf360a533ee46bc7d4a8f6037717c83f21a633a/forge/reconstruction-pipeline.mjs#L415-L535) | 局部对象目录与只读上下文；检查对象归属和版本；支持属性、顺序、更新及增删拆合等操作；返回冲突和拒绝结果 | 借用校验原则。哪些操作开放给第二期 Agent 仍由本项目决定；版本检查必须由程序执行 |
| 原生 PPTX | [`buildNativePptx` / `shapeXml`](https://github.com/qwdwqfwq/topconf-paper-figure-gallery/blob/dbf360a533ee46bc7d4a8f6037717c83f21a633a/forge/editable-native.mjs#L191-L285)、[实际导出调用](https://github.com/qwdwqfwq/topconf-paper-figure-gallery/blob/dbf360a533ee46bc7d4a8f6037717c83f21a633a/forge/index.html#L5880-L5901) | 将文字写为 DrawingML 文字，将形状和路径写为原生形状或自定义几何，将照片写为独立图片；当前下载入口调用此原生实现 | 上游有真正的原生对象导出。不能把该事实简化为“嵌入整张 SVG 就能逐个编辑所有对象” |
| 多格式导出 | [SVG / draw.io / VSDX 生成](https://github.com/qwdwqfwq/topconf-paper-figure-gallery/blob/dbf360a533ee46bc7d4a8f6037717c83f21a633a/forge/index.html#L3531-L3968)、[导出分发](https://github.com/qwdwqfwq/topconf-paper-figure-gallery/blob/dbf360a533ee46bc7d4a8f6037717c83f21a633a/forge/index.html#L5856-L5908) | 导出来自当前场景，draw.io 写独立对象，VSDX 写几何/文字/照片 | 同一来源可以减少各格式内容分叉；各格式的字体、曲线、层级与语义连接仍要分别检查 |
| 序列化与实际渲染 | [PPTX 回读与可选实际渲染检查](https://github.com/qwdwqfwq/topconf-paper-figure-gallery/blob/dbf360a533ee46bc7d4a8f6037717c83f21a633a/forge/index.html#L5359-L5424) | 导出后回读；区分 DrawingML 回读渲染和 Office/LibreOffice 宿主实际渲染；缺少实际渲染等条件时保留需复核状态 | 有效文件、回读一致和目标软件打开一致是不同证据，验收报告应分别记录 |
| 图像调用恢复 | [`requestImageWithRecovery`](https://github.com/qwdwqfwq/topconf-paper-figure-gallery/blob/dbf360a533ee46bc7d4a8f6037717c83f21a633a/forge/image-api.mjs#L19-L85) | 特定参考图不支持错误，且调用方允许时才剥离参考图；不自动重试模糊网络失败，避免重复计费 | 可以参考错误分类。自动剥离参考图会改变风格条件，第二期应记录实际使用的输入和变化 |

上述导出页面围绕生成、重建、检查、字体选择与下载组织。本次未从所查页面找到足以证明通用图元选择、拖拽编辑、分组编辑、撤销和保存再打开的完整工作台操作流程。因此“上游能导出对象”不能替代本项目的工作台内编辑验收。

上游对象场景也未在本次阅读中证明：全部格式都保持可跟随节点移动的语义连接、分组身份和外部编辑后无损回读。连接线的几何可编辑，与重新排版时保持连接关系，需要分开验证。[PPTX 形状实现](https://github.com/qwdwqfwq/topconf-paper-figure-gallery/blob/dbf360a533ee46bc7d4a8f6037717c83f21a633a/forge/editable-native.mjs#L191-L273)、[draw.io 连接生成](https://github.com/qwdwqfwq/topconf-paper-figure-gallery/blob/dbf360a533ee46bc7d4a8f6037717c83f21a633a/forge/index.html#L3562-L3636)

## 需要修正的迁移假设

<a id="migration-boundaries"></a>

1. **科学内容先核对。** 上游生成提示词强调视觉丰富度，允许文字后续修正，也给出固定密度倾向。本试点应明确关键标签、箭头方向、训练与推理边界先与论文核对。参考图中的小图表、数字、模块数量和标签不能自动转成目标论文事实。[上游提示词](https://github.com/qwdwqfwq/topconf-paper-figure-gallery/blob/dbf360a533ee46bc7d4a8f6037717c83f21a633a/forge/index.html#L2182-L2214)
2. **版面来自实际用途。** 上游 SVG 提示词包含固定 1600×900；附件又提出 16:9 与 4:3。这些只是来源中的选择。第二期论文图应由模板、实际插入宽度和用户用途决定版面；提示词接收确定值，不暗中设定本项目默认值。
3. **可编辑性按对象和操作说明。** 独立文字、基础形状、自由曲线、图片、分组、公式和图表分别记录支持范围。整图 SVG 嵌入 PPTX 不能自动证明每项内容都能作为原生对象编辑。当前上游实际下载入口使用原生 DrawingML 导出。[原生实现](https://github.com/qwdwqfwq/topconf-paper-figure-gallery/blob/dbf360a533ee46bc7d4a8f6037717c83f21a633a/forge/editable-native.mjs#L191-L285)
4. **阈值与循环数需要本项目决定。** 上游 SVG 几何检查有像素容差、碰撞阈值、最多两轮修复等常量；这些值取决于其画布和检查方法。第二期先定义失败类型与处理方式，再确认数值，不直接复制为项目默认值。[上游检查常量](https://github.com/qwdwqfwq/topconf-paper-figure-gallery/blob/dbf360a533ee46bc7d4a8f6037717c83f21a633a/forge/index.html#L2474-L2478)
5. **上游文档有版本差异。** `EDITABLE_EXPORT.md` 记录分块和自动精修流程，`RECONSTRUCTION-VALIDATION.md` 又记录另一组参数；固定源码还采用不同调度和需复核条件。迁移时必须跟随所选提交与实际调用入口，不能混合不同说明中的超时、并发、缓存和重试值。[导出说明](https://github.com/qwdwqfwq/topconf-paper-figure-gallery/blob/dbf360a533ee46bc7d4a8f6037717c83f21a633a/forge/EDITABLE_EXPORT.md)、[验证记录](https://github.com/qwdwqfwq/topconf-paper-figure-gallery/blob/dbf360a533ee46bc7d4a8f6037717c83f21a633a/forge/RECONSTRUCTION-VALIDATION.md)、[当前调用入口](https://github.com/qwdwqfwq/topconf-paper-figure-gallery/blob/dbf360a533ee46bc7d4a8f6037717c83f21a633a/forge/index.html#L5315-L5351)
6. **示例精度不能推广为自动能力。** 上游说明 CDTA 精确示例包含人工测量和校准；验证记录说明一部分模型响应来自固定模拟数据，并且示例仍标为需复核。本次也没有运行新论文和真实视觉模型。因此不能把示例、脚本检查或演示图写成任意论文可用的证明。[示例说明](https://github.com/qwdwqfwq/topconf-paper-figure-gallery/blob/dbf360a533ee46bc7d4a8f6037717c83f21a633a/forge/EDITABLE_EXPORT.md)、[验证范围](https://github.com/qwdwqfwq/topconf-paper-figure-gallery/blob/dbf360a533ee46bc7d4a8f6037717c83f21a633a/forge/RECONSTRUCTION-VALIDATION.md)

## 与本库已有能力怎样结合

本库已有“科学来源与视觉参考分开、原生文字与形状、局部修改、最终插入尺寸检查、实际渲染”的规则和工具。已有合成示例证明了一种原生绘图方式，不能证明论文方法正确或跨论文风格迁移效果。[原生绘图说明](https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/docs/native-ppt-figures.md)

建议在这些规则上增加可保存的参考分析结果和分阶段输入输出，复用现有提示词入口，而不是另建一套重复流程：[文字到可编辑图](https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/skills/academic-figure-workflow/prompts/text-to-editable-figure.md)、[参考风格迁移](https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/skills/academic-figure-workflow/prompts/reference-to-editable-figure.md)、[局部修订](https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/skills/academic-figure-workflow/prompts/revise-figure.md)。

现有局部 PPTX 合并工具明确限制独立形状，并拒绝不支持的分组、图像/图表或携带外部关系的替换。因此工作台不应直接假定这个工具支持任意图元编辑和任意 PPTX 往返。[局部修订边界](https://github.com/UnknownObject777/academic-visual-library/blob/9fee65fe33143b2f71dfc5284be45c1efbc88022/skills/academic-figure-workflow/references/local-revision.md)

## 高保真与可使用的验收建议

<a id="acceptance"></a>

以下是待试点确认的方法，尚未设定通过分数、样本数量或修改次数。

| 方面 | 检查对象 | 应保存的证据 | 失败时处理 |
|---|---|---|---|
| 方法事实保真 | 模块、标签、方向、条件、训练/推理边界和结果陈述 | 图中对象与论文段落、图号或代码位置的对应；作者复核记录 | 缺关键证据先澄清；保留已确认内容，定位错误对象 |
| 参考风格保真 | 布局层级、颜色角色、字体层级、线型、箭头、间距与组件一致性 | 参考分析、预设版本、同尺寸预览和人工对照评价 | 修改具体视觉规则；不得牺牲科学含义去贴合版式 |
| 编辑保真 | 改字、移动、调整形状和连线、分组、撤销、保存再打开 | 对象级修改前后记录、保留对象检查、重新打开后的当前图稿 | 明确不支持的操作或对象；禁止用整图替换掩盖编辑损失 |
| 导出保真 | 当前图稿与导出中的文字、几何、层级、图片、曲线与字体 | 导出对象清单、目标软件实际打开及编辑记录、实际渲染对照 | 将格式列为未通过；保留可用源文件和已验证格式 |
| 实际可使用 | 作者能完成一张真实任务并继续修改、保存和提交 | 工作台中的完整操作记录、问题清单、人工修改成本与最终采纳反馈 | 依据失败阶段缩小图种、组件或格式范围，再复评 |

经典复刻、风格迁移和未参与规则提炼的新论文应分别记录。复刻检查对来源图的还原；迁移检查参考画法和新方法事实是否分开；新论文检查流程是否能复用。截图好看不能替代对象编辑与实际任务完成证据。

## 提示词草案的使用方式

以下模板是本项目建议，不是上游提示词原文。工作台应保存每一步的实际输入、输出、提示词版本、模型与服务商配置，以及用户修订。

`{{变量}}` 由真实任务替换。可选信息缺失时沿用已确认上下文；关键方法证据或交付条件不明时，生成具体问题并等待回答。不得让用户填报可以从论文、当前项目或工具能力读取的信息。每次新任务的澄清交互可由工作台现有任务对话承载。

下面的中间 JSON 是讨论用结构。它不强制选用 FigureForge 的 scene schema。图稿阶段使用最终选定编辑器的真实 schema/API；在编辑决策完成前，不能把模板写成已接通的接口或可直接执行的 Agent。

### 1. 方法证据提示词

<a id="prompt-method"></a>

```text
你负责把论文方法转为配图内容依据。现在先核对方法，不设计风格。

输入：
目标论文与版本：{{paper_identity}}
方法正文、算法、原图说明或代码：{{scientific_sources}}
用户要回答的读者问题：{{reader_question_or_known_context}}
工作台中的既有确认和修改：{{confirmed_context}}
实际交付用途与已知版面：{{delivery_context}}

逐项提取输入、输出、模块、方向关系、条件、训练与推理边界。
每项附来源位置和能支持它的简短依据。不要把参考图的标签、图表、
模块数量或结果移入目标论文。不要猜测缺失的箭头、数值与科学解释。
区分论文明确陈述、合理但待确认的解释、证据冲突和缺失信息。
若缺失内容会改变方法结构，提出能直接回答的澄清问题，并停止后续作图。
已有答案直接复用；不要重复询问已确认的信息。

只输出 JSON：
{
  "status": "ready|questions_needed",
  "readerQuestion": "...",
  "entities": [{"id":"...","label":"...","role":"...","evidenceIds":["..."]}],
  "relations": [{"id":"...","from":"...","to":"...","meaning":"...","condition":"...","evidenceIds":["..."]}],
  "boundaries": [{"kind":"train|inference|optional|other","members":["..."],"evidenceIds":["..."]}],
  "evidence": [{"id":"...","source":"...","location":"...","supports":"..."}],
  "uncertainties": [{"item":"...","reason":"...","blocksDrawing":true}],
  "questions": [{"question":"...","whyNeeded":"...","knownContext":"..."}]
}
只填有依据的条目。证据不足的内容进入 uncertainties，不能伪装成 ready。
```

输出用途：用户核对图要表达什么。`questions_needed` 时先收集答案，再更新本步骤。这里增加的证据结构是本项目建议。

### 2. 参考归纳与预设提示词

<a id="prompt-style"></a>

```text
你负责提炼可复用的视觉规则。目标方法事实已经由另一步核对。

输入：
实际参考图片及来源 ID：{{reference_images_and_sources}}
目标图种和已确认的方法提纲：{{confirmed_method_brief}}
用户已选规范、视觉预设和实际用途：{{known_style_and_delivery}}

观察每张实际图片。分别记录布局、阅读方向、嵌套、密度、留白、
颜色语义、字体层级、边框、箭头、图标和重复组件。
提炼共同规则，并说明每项规则来自哪些参考。参考不一致时保留分歧，
不要把不兼容的规则混在一起。测不到的尺寸和字体写 unknown。
只提炼可见画法，不引入参考论文的科学事实、数字、标签或专属标识。
根据目标方法说明哪些规则可沿用、哪些需要调整。
不要为了复制面板数量或填满空白而建议无依据的模块、图表或公式。

只输出 JSON：
{
  "referenceGroups": [{"id":"...","referenceIds":["..."],"sharedGrammar":"..."}],
  "visualRules": [{"key":"...","value":"...","unit":"...|unknown","referenceIds":["..."],"scope":"..."}],
  "tokens": {"colorRoles":{},"typography":{},"strokes":{},"spacing":{}},
  "components": [{"name":"...","visualParts":["..."],"meaningRestrictions":"...","referenceIds":["..."]}],
  "representativeIds": ["实际输入中的ID"],
  "conflicts": [{"rule":"...","alternatives":["..."],"impact":"..."}],
  "adaptationsForTarget": [{"rule":"...","change":"...","reason":"..."}],
  "unknowns": ["..."]
}
```

输出用途：形成可保存、可再次装载的视觉预设候选。会议投稿要求与从图片归纳的视觉偏好分别保存，不把“顶会风格”当成官方规范。

### 3. 版式规划提示词

<a id="prompt-layout"></a>

```text
根据已确认方法和视觉规则，规划一张可编辑的方法总览图。

输入：
已确认的方法证据提纲：{{confirmed_method_brief}}
已确认的视觉预设和组件：{{confirmed_visual_preset}}
实际画布尺寸、插入宽度与文字要求：{{confirmed_page_spec}}
编辑器支持的对象、分组、连接和字体：{{editor_capabilities}}
必须保留的现有内容：{{preserved_content}}

先建立阅读路径，再安排模块、连接和注释。方法事实优先；视觉规则与
目标方法冲突时列明原因并调整布局。使用实际可用字体和组件。
标签来自已确认提纲。缩写或措辞变化必须附原文映射，不能改变含义。
模块数量来自方法。空间不足时报告拥挤位置，并给出有依据的精简建议。
禁止靠编造图表、实验数据、公式、模块或占位数字增加视觉丰富度。

只输出 JSON：
{
  "status":"ready|questions_needed|unsupported",
  "canvas":{},
  "readingPath":["..."],
  "regions":[{"id":"...","purpose":"...","bounds":{},"entityIds":["..."]}],
  "objects":[{"id":"...","kind":"受支持的对象类型","entityOrRelationId":"...","label":"...","bounds":{},"styleTokenRefs":["..."]}],
  "connections":[{"id":"...","relationId":"...","sourceObjectId":"...","targetObjectId":"...","route":"..."}],
  "layerOrder":["..."],
  "wordingChanges":[{"original":"...","proposed":"...","reason":"..."}],
  "unsupportedParts":[{"item":"...","neededOperation":"..."}],
  "questions":["..."]
}
使用输入的实际尺寸，不设通用比例或固定面板数。此结构是布局草案，
还没有替代编辑器的原生图稿格式。
```

输出用途：检查内容覆盖、空间安排和编辑器支持范围，避免直接在长 SVG 里混合解释科学事实与决定版式。

### 4. 原生图稿生成提示词

<a id="prompt-author"></a>

```text
使用选定编辑器的原生图稿 schema 或受支持 API，实现已确认的版式。

输入：
当前图稿版本和原生图稿：{{current_revision_and_scene}}
已确认的方法提纲、视觉预设与布局：{{approved_inputs}}
编辑器的真实 schema/API、可用字体与组件：{{native_editor_schema_and_tools}}
该格式的编辑与导出限制：{{known_format_limits}}

只使用工具实际支持的对象与属性。关键标签保留真实文字，模块、
边框和连线分别保留身份。沿用稳定 ID、分组和已有方法证据对应。
背景先于前景，图片只用于已声明的照片或不可分解素材。
禁止把整张方法图替换为一张图片，也不能把关键文字转成轮廓来冒充
可改字的文字。生成中遇到不支持的组件，列出对象及限制，保留可用草稿。
只有工具实际写出的文件才可以报告为已创建。没有测量或渲染工具时，
不能声称文字没有溢出、连接正确或导出已验证。

若当前调用只接受结构化文本：输出符合输入 schema 的完整原生图稿，
不输出额外解释。若当前调用使用工具：通过真实工具创建图稿，再返回
{"status":"draft|blocked","revision":"实际版本","artifacts":[],
 "unsupportedParts":[],"checksActuallyRun":[],"checksStillNeeded":[]}。
不要自行创造编辑器字段；证据和检查记录可写入调用方支持的独立记录。
```

输出用途：得到能被实际编辑器读取的图稿。填写真实 schema/API 是工作台接入的必要条件；本草案本身没有实现该接入。

### 5. 内容、风格与交付审查提示词

<a id="prompt-review"></a>

```text
审查当前版本，提供可定位的问题。审查范围必须与手头证据一致。

输入：
当前图稿及其实际渲染：{{current_scene_and_render}}
方法证据提纲：{{confirmed_method_brief}}
视觉预设与实际参考图：{{visual_preset_and_reference_images}}
程序测量报告：{{mechanical_checks}}
导出文件对象报告、目标软件渲染和编辑记录：{{export_evidence_or_missing}}
本任务的交付条件：{{accepted_delivery_requirements}}

分别检查方法事实、参考风格、编辑保真和导出保真。
方法检查逐项核对标签、模块、箭头与边界。视觉检查按预设具体规则判断。
几何问题引用程序提供的测量；模型目测问题标为 visual_review。
检查对象缺失、重叠、遮挡、字体替代和未授权的内容变化。
明确哪些对象只有图片编辑能力，哪些文字仍可改字。
目标软件没有实际打开或实际编辑记录时，把相应结论写为 unverified。
缺少证据不能自动记为通过，也不要把图像相似分数当成科学正确率。

只输出 JSON：
{
  "status":"needs_revision|needs_review|ready_for_user_review",
  "dimensions":[{"name":"method|style|editing|export","state":"pass|fail|unverified","evidence":["..."]}],
  "findings":[{"id":"...","kind":"...","objectIds":["..."],"sourceOrRule":"...","observed":"...","suggestedChange":"...","basis":"measured|source_check|visual_review"}],
  "missingEvidence":["..."],
  "preserveObjectIds":["..."],
  "nextAction":"..."
}
即使所有已执行检查通过，也只报告对应范围，不替用户宣称论文已可投稿。
```

输出用途：给下一步提供局部问题清单。程序应先确认检查报告对应当前版本；旧版本报告不能批准新图稿。

### 6. 基于当前版本的局部修改提示词

<a id="prompt-patch"></a>

```text
根据用户请求和审查问题，修改当前图稿中的指定对象。

输入：
当前图稿版本与对象目录：{{current_revision_and_object_catalog}}
允许修改的对象及操作：{{editable_selection_and_supported_operations}}
只读上下文、用户手动编辑和保留要求：{{read_only_context_and_user_edits}}
本轮修改要求与方法证据：{{change_request_and_evidence}}
程序检查反馈：{{validation_feedback}}

以当前图稿为依据，保留所有未选对象。优先修改现有对象属性，不整图重画。
沿用已有 ID。新对象使用调用方允许的身份分配方式，附方法依据。
修改连接方向、标签或方法边界时，要能对应用户要求和科学来源。
任何操作只能使用输入的真实补丁 schema/API。不要删除或重建对象来绕过限制。
当前输入版本过旧、对象归属不符、所需对象不在可修改范围时，返回冲突，
请求调用方读取最新内容；禁止猜测用户刚刚改了什么。
若请求会改变未选对象，列出需要扩大范围的原因，等待调用方处理。

只输出调用方支持的补丁。若使用讨论用外层结构，可返回：
{"baseRevision":"输入的当前版本","operations":[],
 "uncertainties":[],"conflicts":[],"expectedAffectedIds":[]}。
operations 的实际字段必须来自输入 schema；这里没有规定项目最终协议。
空补丁是有效结果。应用补丁、检查版本、创建新版本和撤销由程序执行。
```

输出用途：让 Agent 修改与用户操作基于同一份当前图稿。接受候选前重新检查方法、风格、几何和未选对象；对比实际变化，而不只比较缺陷数。

## 交付包建议

<a id="delivery"></a>

建议一次可复用案例保留以下内容，最终字段与格式由相关议题确认：

- **来源与权利记录**：论文身份及版本、方法位置、参考图来源与用途、组件许可、署名要求、用户授权共享范围。
- **方法与风格依据**：方法提纲、对象与证据对应、参考归纳、预设版本、实际版面和字体。
- **当前可编辑源**：工作台项目中的当前图稿、图元身份、分组和关系；外部源文件及其格式版本。
- **预览与导出**：与当前版本对应的预览、用户需要的已验证格式；各格式的对象编辑范围和限制。
- **生成与修改记录**：提示词版本、输入引用、模型与服务商标识、实际参数、修订请求、补丁、冲突和用户编辑。未知用量保留未知，不保存 API Key。
- **检查与采纳记录**：方法复核、视觉对照、程序检查、目标软件实际打开与编辑、保存再打开结果，以及作者完成真实任务后的反馈。

所有预览、导出和检查应引用同一个图稿版本。工作台能显示一张图、下载文件或解析 JSON，只能证明对应步骤完成。交付条件还应覆盖用户继续改图、重新打开以及最终格式在目标软件中的使用。

## 建议补入哪些决策议题

| 议题 | 需要补充的具体讨论 |
|---|---|
| 首个子领域与配图任务的输入输出边界 | 选受支持组件组成的方法总览；明确图稿版面、关键标签与交付格式；经典复刻和新论文任务分别记录 |
| 试点怎样算成功，失败后先缩小哪项能力 | 使用方法、风格、编辑和导出四类证据；失败时按事实错误、风格不稳、编辑损失、格式损失定位 |
| 一个可复现的配图案例应保存哪些内容 | 采用交付包草案，绑定当前版本；记录失败与人工修改，不只保存成品截图 |
| 投稿规范、视觉预设和领域组件怎样组合 | 保留来源和适用范围；具体 token 与组件样式可复用，方法语义由目标论文决定 |
| 多篇参考论文怎样归纳成可复用风格包 | 用参考归纳模板产生候选，并用未参与提炼的论文检验；不能把某张论文的事实固化成通用组件 |
| 技能与 Agent 负责哪些步骤，用户在哪些位置修订 | 六阶段输入输出、关键缺项澄清、当前版本局部修改、程序校验与用户复核职责 |
| 工作台内的图元编辑与智能体改图怎样共用一份图稿 | 选定编辑器实际 schema/API、图元操作与原生导出支持；确定版本、保留对象、保存和重新打开 |
| 用户贡献怎样进入可复用资产与下一轮改进 | 贡献可核查的参考归纳、组件、提示词改动和失败修复案例；附来源、使用限制和复用证据 |
| 第二期按什么顺序实施，何时扩大到其他领域 | 先跑通一个完整方法图的原生编辑和交付，再增加风格和图种；按真实失败调整能力范围 |

以上均为研究建议，需要用户参与的议题保持开放。本次没有替用户选定子领域、图稿标准、目标格式、通过分数或任何运行参数。

## 代码与素材复用边界

上游 MIT 许可覆盖代码、网站与工具，复制相应代码需保留许可和版权通知。论文图片与第三方材料保留各自权利；仓库代码许可没有统一授权全部图片再次分发。建设资产包时应保留论文和图片来源，分别确认用途与可分发范围。[LICENSE](https://github.com/qwdwqfwq/topconf-paper-figure-gallery/blob/dbf360a533ee46bc7d4a8f6037717c83f21a633a/LICENSE)、[NOTICE](https://github.com/qwdwqfwq/topconf-paper-figure-gallery/blob/dbf360a533ee46bc7d4a8f6037717c83f21a633a/NOTICE.md)、[图片政策](https://github.com/qwdwqfwq/topconf-paper-figure-gallery/blob/dbf360a533ee46bc7d4a8f6037717c83f21a633a/IMAGES_POLICY.md)

本文件只提供研究和原创提示词草案，没有复制上游代码、论文图像或模型文件。
