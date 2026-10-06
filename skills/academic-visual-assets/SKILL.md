---
name: academic-visual-assets
description: Browse bundled visual previews and reuse editable neural-network templates, standard module shapes, equipment icons and palettes in reference-led academic figures. Use for draw.io/PPT architecture drawing, visual asset selection or consistent network-module styling.
metadata:
  version: "0.1.0"
---

# Academic Visual Assets

Use the model's visual understanding to select and adapt actual assets. Templates are editable starting points, not a scientific authority or a mandatory style catalogue.

## Style before assets

Read [design.md](../../design.md): selected reference colors and mark language override all bundled shapes and default fills. View the matching image in [the four style profiles](../../assets/style-palettes.yaml); adapt assets to it before composing. Anti-default review is a required visual check, not a claim of human authorship.

## Look before choosing

Inspect the user's target content and uploaded style. View the relevant PNG sheet in [the visual catalogue](references/catalog.md), then open only the selected source template or icon. The sheets are for visual selection, not a full-catalogue context dump.

- Network templates: `../../assets/drawio/models/`, original library `../../assets/drawio/nn-model-library.xml`.
- Editable module sheet: `../../assets/drawio/modules.drawio` and `../../assets/pptx/modules.pptx`.
- Editable network slides: `../../assets/pptx/network-models.pptx`.
- Recolorable equipment/system SVGs: `../../assets/icons/`.
- Drag-and-drop SVG device library for draw.io: `../../assets/drawio/device-icons.xml` (vector image assets with editable labels, not native primitive paths).
- Reference-derived color roles: [style-palettes.yaml](../../assets/style-palettes.yaml).
- Legacy template color examples: `../../assets/palettes.json`; never select these automatically.

The repository has 37 entries, including one without an upstream title. Do not invent its model identity. Previews and PPT slides use a limited primitive renderer; original draw.io preserves upstream geometry/styles and remains authoritative. Neither upstream labels nor dimensions automatically describe the user's method.

## Adapt the material, not the method

Use only the modules supported by target content. Verify residual connections, pre/post normalization, attention masks, concatenation versus addition, channel/resolution changes and train/inference roles against the current method or code. Whole-network examples may be pedagogical abstractions, not canonical implementations.

Keep a coherent visual representation for repeated module types. Convolution blocks, tensor stacks, tokens, attention and operators can reuse geometry, but all colors, sizes, strokes and text must adapt to the user's inspected style. Read [module and color conventions](references/modules-and-color.md) when needed. A network-device icon depicts physical infrastructure; it is not a substitute for a neural operation.

For draw.io work edit actual XML/native shapes directly when that is sufficient. This plugin does not require a YAML/JSON scene IR or the separate drawio academic overlay. An existing supported tool may have its own input format; that tool format does not justify adding a new analysis pipeline.

PPT uses native shapes/text/connectors. Inserted SVG icons remain vector picture assets unless converted to editable native paths; do not call them fully editable primitives. Reuse slide objects, not a flattened slide image. SVG is useful for scalable output but does not imply PPT native-object editability.

## Tools and completion

Use existing draw.io/document tools when available, or modify the native source with available file tools. `../../scripts/drawio_assets.py INPUT.drawio --svg OUTPUT.svg --pptx OUTPUT.pptx` supports only the simple shapes present in this library and fails on unsupported shapes. It does not reconstruct arbitrary uploaded diagrams, preserve all draw.io styles, or replace a general renderer. Locate the available Python/document runtime; optional PPT export needs python-pptx. Export exact final appearance through the target editor when that requirement matters.

Use the native image tool for requested image generation/editing and for complex illustration where appropriate. Do not claim this plugin adds new model vision abilities; it supplies reusable visual context and editable material. Continue through [the figure workflow](../academic-figure-workflow/SKILL.md), inspect actual final-size output, and deliver the requested sources and previews.

Retain [third-party notices](../../THIRD_PARTY_NOTICES.md) and asset provenance when distributing this library or derived template bundles. The templates' “IEEE palette” is an upstream convention, not an IEEE requirement. No external MCP, paid API, automatic model switching or runtime network fetch is required by this asset library.
