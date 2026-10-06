# Academic Visual Library

**看参考图，用可编辑素材，直接完成学术绘图。**

![宣传海报](assets/poster.png)

这个 Codex 插件把模型的多模态理解、原生图像工具，以及 draw.io／PPT／SVG 素材放在同一条轻量流程中：看材料和参考图 → 选择部件 → 绘制 → 对照检查 → 局部修正。

## 我们改进了什么

- **风格不限于菜单。** 上传图直接决定构图、笔触、材质、字体、密度与配色。
- **标准模块可复用。** 内置37个网络条目、20个模块原型、10个SVG图标，提供真实draw.io和原生PPT对象。
- **充分使用模型能力。** 默认不要求先填FigureSpec、JSON场景图、prompt hash和多阶段IR；需要编辑器原生格式时直接操作该格式。
- **保留科研约束。** 参考图提供画法，论文和代码提供机制；核对残差、归一化、梯度与训练/推理边界。
- **每次改图重新看图。** 明确允许变化和必须保留的内容，不把上版验收结论直接搬到新图。

三个入口：`academic-figure-workflow`负责绘制与修订，`academic-figure-analyzer`按需理解资料，`academic-visual-assets`看缩略图并选择素材。没有强制串行流水线。

## 安装与使用

```bash
codex plugin marketplace add UnknownObject777/academic-visual-library
codex plugin add academic-visual-library@academic-visual-library
```

插件入口未刷新时重新进入客户端或会话。使用当前会话可用的原生图像、文件和文档工具，不额外要求付费API或MCP服务。

可以直接说：

> 参考这张图的视觉风格绘制我们的框架，使用可编辑网络模块。残差连接和归一化顺序按代码核验，交付draw.io或PPT。

> 只改Attention区域的箭头；保留其他模块、标签、颜色与布局，改完检查整图。

> 分析这个prompt为什么容易画乱，先不要生图。

[浏览实际素材](skills/academic-visual-assets/references/catalog.md) · [模块PPT](assets/pptx/modules.pptx) · [整网PPT](assets/pptx/network-models.pptx)

## 致谢与定位

本项目受 [Azhi-ss/academic-figure-skills](https://github.com/Azhi-ss/academic-figure-skills) 启发，并参考其最新的分析/绘图分工、参考图驱动设计、局部修订约束与新图重新审核思路。感谢上游工作；保留相关MIT许可和来源。

我们的进一步改进围绕**多模态直接判断、轻量流程、素材视觉检索、原生对象级编辑和明确的交付边界**展开。对于需要结构准确、模块一致、可编辑源稿的网络图，这是我们的主要设计方向。“更好”体现为这些具体能力和使用体验，不冒称已通过跨模型评测证明全面领先。

## 已验证与限制

已检查37个模板解析、38页PPT原生对象、素材hash、内部链接，并用真实PowerPoint渲染检查模块页。内置网络条目包含36个具名示意和1个未命名条目，不能把模板当作目标模型的实现证明。

预览/PPT转换工具只支持当前素材库的基本形状，可能简化draw.io外观；不是通用draw.io转换器。最终图稿需在目标编辑器与实际论文尺寸下验收。SVG图片、原生对象和栅格插画的可编辑程度分别说明，不能混称。配色是可选约定，不是IEEE强制标准。

海报由Imagegen生成，用于解释产品流程，不是实验结果，也不是原生可编辑图稿。尚未完成跨模型质量评测或所有任意风格的端到端验证。

详见 [英文文档](README.md)、[上游融合记录](docs/upstream-integration.md) 和 [第三方许可](THIRD_PARTY_NOTICES.md)。
