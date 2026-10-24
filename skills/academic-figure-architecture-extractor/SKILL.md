---
name: academic-figure-architecture-extractor
description: Inspect uploaded academic figures to explain their content, faithfully redraw them, or transfer any observed visual style to a different method.
metadata:
  version: "5.0.0"
---

# Academic Figure Reference Analysis

Look at the actual image. Separate its scientific meaning from its visual language, then use only what the current request needs.

For a PDF inspect the requested page/figure and caption; [pdf-extraction.md](references/pdf-extraction.md) describes the optional extraction helper. For local images use an image viewer. For remote or conversation images use supported viewing mechanisms. Do not invent a local path or claim inspection of inaccessible imagery.

- Explanation: describe observable components, reading order, arrow directions, groups and legend meaning. Mark unreadable labels and ambiguous crossings as uncertain.
- Faithful redraw: preserve source content, topology and labels except explicit changes.
- Style transfer: observe silhouette, density, whitespace, illustrations/marks, surfaces, typography, stroke/arrow treatment and color roles. Target method content comes from the target materials.
- Repair: locate the observed defect and what must remain intact.

Any coherent uploaded style is usable as a design reference; do not force it into a predefined class. Matching colors alone is insufficient. Exact fonts and hex values are estimates unless measured; appearance does not reveal a verified original prompt or generator. Follow [reference-style.md](../academic-figure-workflow/references/reference-style.md) when needed.

An analysis request receives concise relevant findings. A drawing request carries those findings directly into [the workflow](../academic-figure-workflow/SKILL.md) and completes the figure. No mandatory inventory, component IDs, JSON report or inter-stage schema. Save an analysis artifact only when requested or materially useful for a large reusable task.

If the reference is unavailable, ask for the missing image through an ordinary user message only when needed. Continue source-supported work; do not pretend to match a style unseen.

For editable reconstruction, distinguish reproducible geometry/text from photos, texture and data-bound charts. Report the actual editability boundary rather than promising every visible pixel as a PowerPoint object. Resolve observed style into concrete authoring values using [style-to-layout](../academic-figure-workflow/references/style-to-layout.md); keep ambiguous scientific connections unresolved until source evidence or user clarification supports them.
