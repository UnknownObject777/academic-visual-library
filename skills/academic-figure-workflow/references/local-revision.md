# Local revision of a native figure

Begin from the latest usable editable source and inspect its render. Recover accepted decisions from current conversation/history; the newest explicit correction supersedes older case-specific choices. Identify changed objects, preserved regions and linked detail canvases without demanding a user-authored manifest.

Edit native objects through the supported API when round-tripping is faithful. If it disturbs untouched content, author native replacements and use [patch_native_shapes.py](../scripts/patch_native_shapes.py) to merge a narrow selection into a copy:

```text
python patch_native_shapes.py --baseline current.pptx --replacement native-replacements.pptx --output private-candidate.pptx --slide 1 --prefix mechanism-
```

Replacement and baseline slides must have identical physical dimensions. This helper handles standalone shapes/text without external relationship dependencies. It rejects unsupported groups, images/charts and relationship-bearing replacements rather than silently corrupting assets; use the document API and explicit relationship checks for those. Existing unselected objects and non-slide package parts remain preserved, new IDs cannot collide, and removal requires `--allow-remove`. That option is a script safeguard, not a new human approval gate.

Choose narrow prefixes or exact `--name` selectors. For a connector outside the edited region, include its exact name only when it belongs to the requested change. Run `audit_pptx.py candidate.pptx --baseline current.pptx --allow-prefix mechanism-` (repeat selectors as needed) and inspect changed and untouched regions in the final render.

## Repairs demonstrated in the conversation

- Uniform arrows use shared shaft/head dimensions and target gaps. Preserve necessary weight meaning elsewhere; absent/blocked outputs stay absent.
- Aligned panels compare relative offsets, shared column anchors and row baselines, reserving empty output slots where needed.
- Larger fonts are measured at insertion width; expand boxes and recheck braces/arrows nearby.
- Semantic palette, fill opacity and outlines propagate to main and inset views.
- Independent detail canvases reuse native source geometry and synchronized labels.

FedPCR's top server, three client roles, four cases and LOSS placement are case-specific. Reuse the preservation, typography and alignment mechanics, not its scientific labels or layout.
