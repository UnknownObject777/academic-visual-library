---
name: academic-figure-workflow
description: Draw and revise academic figures from papers, code and reference images using multimodal reasoning, optional editable templates and actual render inspection. Also construct, diagnose or revise figure prompts without rendering when requested.
metadata:
  version: "0.2.0"
---

# Academic Figure Workflow

Understand the content and reference, compose, draw, inspect and repair. Use the agent's visual reasoning directly; no mandatory scene IR, prompt compiler or serial analysis pipeline.

## First priority: reference color and visual language

Read [design.md](../../design.md) before composing any figure. Inspect actual reference pixels and choose their palette, semantic color roles, accent proportions, ink, typography and mark language before layout. An uploaded reference overrides every stock template and palette. Use the four inspected examples in [style-palettes.yaml](../../assets/style-palettes.yaml) only as separate starting points, never an averaged pastel default. They are approximate tokens, not a scene IR. Arbitrary new references remain supported.

Anti-AI means avoiding unrequested generator defaults and checking reference fidelity. A correct topology with the wrong palette/style is not an accepted result. Compare actual final rendering with the reference and revise observed mismatches. Scientific accuracy remains mandatory; never borrow example claims.

## Match the requested output

| Request | Finish with |
|---|---|
| Draw or edit a figure | Rendered and inspected artifact, requested source files |
| Construct a prompt | Concise design rationale and usable prompt; no render |
| Diagnose a prompt | Specific risk, consequence and minimal correction; no file mutation |
| Revise a prompt | Allowed changes, invariants and full revised prompt; no automatic render |
| Consult on palette/style | Concrete visual advice at the requested scope |
| Editable architecture | Native draw.io/PPT objects, labels and connectors where supported |
| Editable text over an accepted raster | Follow [editable delivery](references/editable-delivery.md); distinguish the raster background from editable text |

## Read the actual source and style

View the reference image or requested PDF figure and caption; inspect relevant scientific material. A caption alone is not visual inspection. For unclear manuscript, code or reference content use [the analyzer](../academic-figure-analyzer/SKILL.md) only where needed. Explicit user architecture skips redundant source discovery.

Scientific material controls nodes, operations, labels and relationships. References control visual language. For a faithful redraw preserve original semantics; for style transfer do not import its method or claims. Observe composition, density, whitespace, mark language, surfaces, typography, strokes and color roles using [reference-style.md](references/reference-style.md). Style influences layout from the start, rather than being pasted onto a generic pipeline afterwards.

An explicit style or uploaded reference is sufficient; do not reopen selection. Without one, use established project style or a reasonable stated default for an ordinary drawing request. If the user wants to choose or asks for options, show relevant actual previews and wait for their selection. Do not force a preset menu on every first render. Arbitrary coherent references are supported as design directions, not a promise of pixel-perfect reproduction.

## Compose and draw

Identify the reader's question, indispensable mechanism path and caption-only detail. Describe critical edge endpoints, directions and meaning in ordinary language; position alone cannot establish a connection. Distinguish execution, advisory feedback, storage and exception paths when relevant. Keep training/inference and gradient boundaries accurate.

Use [visual assets](../academic-visual-assets/SKILL.md) for reusable neural modules, editable templates or device icons. Inspect only the relevant visual sheet, adapt selected objects and verify target semantics. No arbitrary panel count, mandatory icon in every box or shrinking labels to fit more content.

Honor the user's renderer and medium. Native image generation/editing uses [image execution](references/codex-image-workflow.md). Pass actual references when supported. Exact notation/editable architecture can use native vector/document objects; empirical plots require actual data. Compact renderer instructions separate scientific content, essential visible text, layout/style and forbidden implications.

Keep internal prompts internal unless requested. Explicit prompt review requires waiting for approval; otherwise draw directly. Structured output is optional only when requested or required by an actual tool. Do not invent references, source paths, modules, dimensions or measured results. Follow [missing-info-policy.md](references/missing-info-policy.md) for missing science.

## Revise and inspect the exact result

Before changing an existing render, view it and identify the allowed delta and invariants. A color edit preserves topology; an arrow correction preserves the composition and unrelated critical edges. Do not turn a distinctive figure into an equal-sized icon strip to fix one defect.

After generation or any edit, inspect the new actual file. Use [render-audit.md](references/render-audit.md). Recheck required nodes/edges, text, style and final-size readability across the full figure; a previous revision's pass does not transfer. Fix consequential observed defects locally and inspect again. No mandatory audit JSON or hash-bound spec; identify the checked file/version in a brief note when revisions could be confused.

Keep original assets and recoverable versions. Do not automatically strip provenance. If the backend stops improving, deliver the best usable result and state unresolved defects. No automatic model switching or subagents. Deliver actual files and requested editable sources; distinguish checks performed from those unavailable.
