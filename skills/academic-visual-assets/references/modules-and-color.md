# Consistent modules and color

Standardize reusable visual vocabulary, not an architecture's scientific details. Begin with the uploaded reference and the established paper style; adapt prefab shapes to it. Without a reference use the small palette examples, not a venue-to-color rule.

| Module | Useful visual starting point | Verify before drawing |
|---|---|---|
| Convolution / feature map | plane or tensor stack | operator, channels/resolution and stride only if supported |
| Pooling | compact reduction block | pooling type and actual reduction |
| Normalization / activation | compact labelled operation | LN vs BN, activation type and pre/post order |
| MLP / projection | layer stack or labelled block | map dimensions, shared weights and purpose |
| Attention | token interaction plus labelled operation | Q/K/V sources, cross/self attention, mask and head information |
| Add / concat | small operator node | addition needs compatible shapes; concat requires the correct axis |
| Skip / residual | distinct bypass edge | actual endpoints and where the operation joins |
| Loss / stop-gradient | explicit training mark | gradient direction, stopped branch and training-only boundary |
| Client / server / router | equipment icon or native schematic | logical role versus physical device, communication direction |

Do not transplant ResNet dimensions or a post-norm Transformer into a different implementation. Generic module primitives intentionally omit unknown tensor dimensions. Geometry is reusable; semantics still need evidence.

For a paper-wide style, maintain a small set of repeatable colors, strokes, label hierarchy and arrow meanings in the actual templates or existing project style note. No mandatory design-token manifest. The same operation should look related across figures; multiple roles need distinguishable labels/shape/line style, not necessarily a new hue each.

Recolor SVG strokes/fills and native draw.io/PPT shapes while preserving geometry. Match the reference's material and drawing language as well as color. Contrasting text must use the actual background; soft fills alone do not certify readability. Check grayscale when important. Font sizes are assessed at final publication size, not from the zoomed editing canvas.
