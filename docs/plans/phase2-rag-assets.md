# 第二期 RAG 案例与能力包规范

本文件是已采用的实施规范和包结构样例。产品接入、完整案例、模型效果与真实使用仍需实施验收。

授权依据：[剩余规划问题采用推荐方案](https://github.com/UnknownObject777/academic-visual-library/issues/1#issuecomment-6386551244)。入口：[第二期地图](https://github.com/UnknownObject777/academic-visual-library/issues/1)。

## 案例包

一个案例对应一个明确的作图任务。`case.json` 是索引，原生图稿是当前可编辑内容。预览、导出、检查和修订记录都引用图稿版本。

```text
case.json
input/method.md
input/references.json
derived/evidence.json
derived/reference-analysis.json
derived/layout.json
source/figure.drawio
preview/figure.png
exports/figure.svg
exports/figure.pdf
exports/figure.pptx
runs/<run-id>/request.json
runs/<run-id>/response.json
runs/<run-id>/changes.json
reviews/acceptance.json
```

这是目录职责，不要求在任务开始时创建空文件。缺少产物保持 `pending` 或 `failed`，不能列为已生成。目录可以打包为 ZIP；文件压缩和 JSON 校验使用成熟库。

`case.json` 的首版结构如下。示例不是已经运行的 RAG 案例。

```json
{
  "schemaVersion": 1,
  "id": "rag-development-overview",
  "split": "development",
  "taskType": "method-overview",
  "status": "draft",
  "paper": {
    "id": "neurips-2020-rag",
    "title": "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks",
    "sourceUrl": "https://proceedings.neurips.cc/paper/2020/file/6b493230205f780e1bc26945df7481e5-Paper.pdf",
    "adoptedFileSha256": null
  },
  "input": { "method": "input/method.md", "readerQuestion": null, "references": "input/references.json" },
  "figure": { "format": "drawio", "path": null, "revision": null },
  "capabilities": { "publicationProfile": null, "visualPreset": null, "componentPack": null, "workflow": null },
  "artifacts": [],
  "runs": [],
  "reviews": [],
  "sharing": { "state": "private", "selectedFiles": [], "rightsReviewed": false }
}
```

实际产物条目记录 `kind`、相对路径、图稿版本、文件校验值、生成工具与状态。运行条目记录提示词版本、完整输入引用、模型标识、工具版本、实际参数和可获得的用量。未知用量保留未知。

方法证据记录来源位置、可确认的模块和关系，以及图稿对象 ID。未知或冲突进入待确认项。参考图分别标明用于科学核查还是视觉参考。科学事实不得从风格参考自动复制。

用户修改和 Agent 修改分别记录：基于的图稿版本、修改请求、对象范围、修改前后版本、实际变化、检查结果与接受原因。消息记录继续沿工作台已有的 thread、turn、item 归属规则。图稿版本与消息存储版本分开管理。

私有运行记录保留完整内容。公开贡献包只包含用户选择且允许分享的文件，不包含 API Key、认证内容或未授权原文。不能按数量或大小静默裁剪历史。

### 入库要求

可作为完整案例发布时，需要来源完整、任务范围明确、原生源文件可打开、预览与导出对应当前版本、编辑和方法核查有记录。失败案例也可贡献，但明确失败阶段，不能混入已通过案例。

RAG、REPLUG 属于开发集合。Self-RAG、IRCoT、RECOMP 属于本轮独立检验集合。检验报告和目标原图不进入作图输入。使用检验结果改规则后，记录集合用途变化。

## 能力包

采用 JSON 清单、Markdown 规则和原生组件文件。清单使用 JSON Schema 描述，实施时用成熟校验库验证。首版清单版本为 1；不编写旧字段迁移或兼容分支。

| 包类型 | 内容 | 科学内容的来源 |
|---|---|---|
| 投稿规范 | 官方来源、适用版本、实际版面、字体和文件要求 | 不定义目标方法 |
| 视觉预设 | 颜色角色、字体层级、线型、间距、布局规则与示例 | 不定义目标方法 |
| 领域组件 | 原生组件、端口、参数、功能、适用条件与证据 | 来源明确的科学语义 |
| 执行技能 | 阶段提示词、工具要求、输入输出与检查流程 | 读取目标方法证据 |

共同清单字段为 `schemaVersion`、`id`、`kind`、`version`、`title`、`appliesTo`、`sourceRefs`、`license`、`files`、`requiredCapabilities`、`examples` 和 `limitations`。

每个包的附属路径相对于包根目录。装载前检查清单和引用，随后把说明、组件目录和必要文件提供给实际运行时。工作台显示已装载的包和版本，便于用户替换或修改。只注入一段说明文字，不能算组件文件已装载。

冲突处理顺序是：当前用户明确要求与方法证据、目标投稿要求、用户选定视觉预设、组件的可配置样式。科学关系和发表要求发生冲突时，记录冲突并澄清；不能用配色或版式改变方法。

新建组件和清单沿本仓库 MIT 许可发布，保留依赖署名。论文图片和第三方材料分别记录使用条件。未知条件的参考仅保存来源与待核实状态，不默认打包再分发。

## 风格提炼与种子样例

种子样例：[rag-structured.seed.json](examples/rag-structured.seed.json)。颜色引用现有 `technical_vector` 配置，保留其“近似参考重建”的来源状态。它是包结构样例，不是多篇 RAG 参考图已分析完成的结果，也不是官方会议风格。

本期先用用户手选的同类参考。按框架、流程、架构等视觉功能分组，分别输出共同规则、特例、未知项、代表参考和来源。参考张数和代表图数量由实际材料决定，不新增硬性数量限制。

归纳结果包含颜色语义、字体角色、线宽、留白、层级、布局约束、组件画法和适用条件。不同参考有分歧时保留差异，不强行平均。测不到的字体或尺寸标为未知。

用户可以直接修改这些规则，并保存为自己的预设。后续生成使用方法证据、已选预设和可用组件。布局适应目标方法，不能固定所有论文的模块数量或拓扑。

实施展示需同时提供：参考分析与预设、可编辑图稿、修改后的图稿、对应预览与导出。先用 RAG 建设，再用 REPLUG 检查复用。三篇独立检验按已确认协议另行运行。

提示词直接复用[六阶段草案](https://github.com/UnknownObject777/academic-visual-library/blob/313f44d42ab3a26a9062f2ec1b053c18237def01/docs/research/phase2-figureforge-prompts-and-delivery.md)。生成阶段补充实际编辑器格式；草案中的讨论用 JSON 不成为第二份图稿源。

## 社区与改进流程

社区先使用本仓库的 GitHub Issue 和 PR。首批贡献类型为案例、预设、原生组件、提示词改进、失败修复记录和规范来源补充。暂不建设独立社区平台。

贡献模板需要：用途、来源、版本、允许分享的范围、原生文件、预览、运行和修改记录、检查结果、适用限制。失败修复需提供修改前后与仍未解决的问题。

流程为：用户选择分享材料 → 导出贡献包 → Issue/PR → 维护者核对来源和可打开性 → 熟悉领域的人核对科学内容 → 检查视觉与编辑范围 → 同条件复评 → 发布包版本与署名 → 工作台加载和再次使用。

同一材料的修订通过版本记录维护。不同设计方案可并存并标注用途。覆盖已有包需要维护者审核，不静默替换。案例和规则复评必须保留失败结果和人工成本。

独立检验内容与开发、贡献材料分别管理。真实贡献后记录是否有人装载、修改和再次使用；没有这些记录时，社区价值保持待验证。

## 实施交接

本仓库负责包格式、提示词、来源、组件、案例和贡献模板。工作台负责装载、编辑、Agent 读写、保存与导出。实际任务和两仓库的输出共同验收。

本次仅新增规范与种子样例。没有模型调用、原图复制、正式产品功能或新的运行时限制。TODO 与待验收事项没有完成功能可迁移，因此未修改现有功能进度文件。

## 实施事项入口

- [二期实施：案例与能力包格式、种子预设和组件规范](https://github.com/UnknownObject777/academic-visual-library/issues/15)
- [二期实施：图稿节点内的 diagrams.net 编辑、版本与保存](https://github.com/UnknownObject777/paperfigure-workbench/issues/37)
- [二期实施：装载投稿规范、视觉预设、组件与技能包](https://github.com/UnknownObject777/paperfigure-workbench/issues/38)
- [二期实施：当前图稿导出 SVG、矢量 PDF 与原生 PPTX](https://github.com/UnknownObject777/paperfigure-workbench/issues/39)
- [二期实施：六阶段作图与 Agent 基于当前对象的局部修改](https://github.com/UnknownObject777/paperfigure-workbench/issues/40)
- [二期实施：RAG、REPLUG 开发案例与社区贡献入口](https://github.com/UnknownObject777/academic-visual-library/issues/16)
- [二期实施：三方案比较、独立检验与真实使用验收](https://github.com/UnknownObject777/paperfigure-workbench/issues/41)

这些事项保持待实施状态，原生依赖关系保存在 GitHub。规划地图关闭不改变它们的完成状态。
