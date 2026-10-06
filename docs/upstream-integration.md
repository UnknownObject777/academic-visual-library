# Upstream integration, v0.2.0

Reviewed `Azhi-ss/academic-figure-skills` at commit `2c7f9e3ccde9171927f6b8f068c16d15d0f5612a` on 2026-10-06. In particular: workflow/analyzer entry points, prompt-design logic and editable-PPT delivery guidance. This is an independently packaged, attributed extension rather than a claim that the upstream project has no comparable capabilities.

| Recent upstream direction | Integrated here |
|---|---|
| Analyzer/workflow split | Two core skills plus one optional visual-assets skill; no five-stage mandatory chain |
| Construct/diagnose/revise output modes | Explicit stopping points; prompt-only does not trigger generation |
| Style affects composition early | Inspect reference before layout; preserve observable visual grammar |
| Delta and invariants | Local edits preserve scientific paths, labels and unrelated composition |
| Each new render needs new checks | Re-inspect the whole required node/edge content, never reuse an old pass |
| Editable text in PPT | Distinguish text overlays from native objects and raster background |

Deliberate adaptations: no mandatory FigureSpec/audit serialization; no mandatory first-render style menu when the request supports a reasonable default; no automatic subagent dispatch; no automatic provenance stripping. Explicit review and style-selection requests remain binding.

New material: visually browsable native network/module assets, SVG device library, four separate reference-derived style profiles with actual previews, object-level editable PPT sources and a limited draw.io primitive renderer. These assets complement native image generation rather than replacing it for every visual style.

A local structure/render validation is not a controlled comparison of model output quality. Future evidence should evaluate reference-style fidelity, topology accuracy, label correctness and editability on shared inputs, with actual produced artifacts and disclosed model/tool versions.

User-driven revision: palette and visual language moved to the first workflow decision, backed by `design.md` and role-based YAML tokens. Reference fidelity is checked independently of scientific topology. Generic promotional decoration is no longer a default.
