# Reference fidelity comes first

Color and visual language are the first design decisions, before layout or template selection. Scientific truth remains binding: a style reference never supplies the target method's claims or topology.

## Working rule

Inspect the actual reference pixels. Identify dominant canvas/fill/ink colors, accent area, saturation, contrast, color-to-role relationships, typography, border weight, corners, shadows and diagram density. Briefly state the observed direction before drawing. If exact colors matter, sample flat interior areas; JPEG edges and shading are not source hex values. Read [style-palettes.yaml](assets/style-palettes.yaml) for four reference-derived starting points and view the linked image. These are approximate reconstructed tokens, not recovered author specifications or IEEE standards.

Priority: user's explicit color changes → uploaded/selected reference → established project identity → a deliberately chosen bundled profile. Never average profiles into one rainbow palette. Four profiles are examples, not a limit on supported styles. If several references conflict, assign a specific role to each (e.g. palette from A, geometry from B) instead of unconsciously blending them.

Preserve color semantics: the same role receives the same treatment; visually distinct paths need distinct marks as well as color when necessary. Large fills, small accents and dark anchors have different jobs. Match their relative area and contrast, not merely a list of hex codes. Adapt template colors before rendering; a template's stock colors have no priority.

## Four observed references

| Reference | Palette behavior | Visual language to preserve |
|---|---|---|
| [Technical vector](assets/style-references/modern_technical_vector_deepseek_mla.jpg) | Pale blue/neutral/lilac regions; saturated green, cyan and amber tensor bars; black paths | Dense technical labeling, orthogonal wiring, segmented tensors and a warm attention heatmap |
| [Illustrated modular](assets/style-references/illustrated_modular_agentic_matribo.jpg) | Blue reasoning / peach execution / green memory; purple feedback, coral exception | Ink outlines, drawn scientific objects, asymmetric functional zones and a recoverable loop |
| [Airy mathematical flow](assets/style-references/pastel_airy_ui_agentic_bo.jpg) | White space dominates; peach surrogate, ice-blue agent, charcoal evaluation, gray storage | Serif mathematics, dashed scope, context layering, restrained soft shadows and thin arrows |
| [Contrast and ablation](assets/style-references/contrast_ablation_kan.jpg) | Purple baseline against green comparison; colored curves only at the mechanism | Two balanced semantic fields, black node outlines, gray edges and explicit local mechanism differences |

These are the first four gallery examples in Azhi-ss/academic-figure-skills at the recorded commit. Upstream currently offers six examples. Their images are included under its repository MIT license; retain [the notices](THIRD_PARTY_NOTICES.md). Do not import KAN efficiency statements or other example claims into unrelated work.

## Anti-default review

“Anti-AI” here means resisting unrequested generator defaults, not asserting that a color proves human authorship. Pastel, purple and rounded corners can be appropriate when the reference uses them. Reject them when they replace the selected reference. Do not add generic cream backgrounds, blue-purple gradients, floating equal-sized cards, leaves, mountains, sparkles, glossy 3D modules or oversized editorial titles without support from the request/reference.

Compare the final render and reference side by side at thumbnail and reading size: palette dominance, accent proportions, dark anchors, line character, typography and density. Topology can pass while style fails. A style mismatch requires a revision; do not waive it because the result is attractive. State unresolved deviations honestly. Use ordinary prose and a small token file when useful; no mandatory scene serialization or audit IR.
