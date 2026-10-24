# Resolve style into reusable authoring values

Use when a figure's style must stay stable across creation and revisions. Keep only decisions that affect this figure: actual reference, physical size, font/glyph coverage, final-size hierarchy, ink, semantic fills/strokes/opacities, arrow head/shaft dimensions, corner treatment, whitespace and asset treatment. A short note and a code style object suffice; no mandatory specification artifact.

Take exact values from user choices or flat reference regions when possible; identify estimates. Reuse roles across the main figure and insets, including outline color and opacity. Read the [reference profiles](style-library/assets/style-palettes.yaml) only when selecting one, together with its actual image. A new paper does not inherit FedPCR's three clients, four cases, server, LOSS, gray outlines or black text by default.

## Layout and repeated panels

Derive the graph before placing it. Reserve the focal mechanism's space first; compress context without removing required dependencies. Choose a composition appropriate to sequence, comparison, hierarchy, loop or shared scene.

For repeated panels define frame, header, content viewport, incoming arrow, feature/output anchor and margins once. Position instances relative to their frames. Normalize offsets before checking alignment: independent centering of every complete flow moves comparable outputs into different columns. Reserve a consistent output slot for blocked cases without adding a nonexistent arrow.

Use one underlying geometry for an overview and insets. Share class overlap and query positions before applying affine transforms. Different conceptual point locations can be intentional; state their illustrative nature when relevant. Never alter evidence to make a layout more symmetrical.

## Arrows

One constructor defines each semantic family: shaft width/color, head length/width, endpoint gap and direction. Use the same specification for straight, orthogonal and curved variants. Connect visible endpoints to their real source/destination without misleading crossings.

Uniformity depends on meaning. If arrow strength encodes weight, preserve that distinction unless the user changes it. When uniform arrows are explicitly requested, use another agreed supported mark for any necessary distinction. Blocked outputs remain blocked.

## Physical typography

Use millimeters for insertion size and points for type. On an oversized existing deck:

`final font pt = deck font pt × insertion width / deck width`.

For CSS-pixel authoring: `px = mm × 96 / 25.4`; `font px = font pt × 96 / 72`.

About 9–10 pt is a practical starting target for dense paper diagrams, then checked against the actual template and render; it is not a universal journal rule. Resolve single-column versus spanning width from the template/context and state any assumption. A double-column paper does not automatically require a full-width figure. Values such as 88/90/178/182 mm belong to particular templates.

Expand/reposition text boxes after increasing type. Verify actual glyphs, equations, subscripts and non-Latin labels. A named font may lack glyphs. DPI metadata cannot increase pixel resolution or fix text that is too small at insertion size.
