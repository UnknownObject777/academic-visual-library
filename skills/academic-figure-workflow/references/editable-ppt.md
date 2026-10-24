# Native editable PowerPoint execution

Read for PPT figure creation/revision. The available presentations skill owns runtime discovery, supported APIs, markers and finalization. Read its current installed instructions instead of hardcoding a versioned runtime path. Explicit PPT file delivery uses its file-authoring branch; a bound native session is useful when appropriate to the requested output.

## Native authoring

Use native shapes, paths, connectors and real text for the mechanism. A full-slide image plus invisible text is not native editability. Photos/textures may remain raster with disclosed scope. Editable plotted paths differ from data-bound editable charts. Use supported native equations where available; otherwise disclose the separately editable equation source rather than claiming native equation editing.

[figure-native.mjs](../scripts/figure-native.mjs) uses millimeter geometry and point typography directly. Import the available artifact library in the build environment and pass it to the helper:

```js
import * as artifact from '@oai/artifact-tool';
import { createFigure, gridCells, viewport } from '/absolute/skill/scripts/figure-native.mjs';
const figure = createFigure({widthMm:182, heightMm:90,
  style:{font:'Times New Roman',fontPt:9.5,ink:'#000000',
    outline:'#8A8A8A',lineMm:0.22,arrowMm:0.28,headMm:1.15}}, artifact);
const c = figure.addCanvas();
c.rect('encoder',12,22,33,13,{fill:'#FFFFFF'});
c.text('encoder-label','Encoder',12,22,33,13);
c.arrow('encoded',[[45,28.5],[60,28.5]]);
await figure.saveDraft('/absolute/private-build/candidate.pptx');
```

These values and topology are examples, not defaults for all papers. The helper contains primitives, not a manuscript compiler. Names enable local selection without a user-maintained ID manifest. `gridCells` supplies relative slots; `viewport` preserves aspect ratio for shared semantic geometry. Duplicate detail canvases from the same composition/geometry rather than pasting raster crops.

For an oversized prior deck, measure with `audit_pptx.py --target-width-mm`. Physical resizing alone preserves the same tiny insertion-size text. Increase required fonts and repair their boxes/layout through the source authoring route; do not blindly resize unknown charts or master-dependent text.

## Render and export

Render every final canvas through an available presentation renderer. On Windows with PowerPoint:

```powershell
& /absolute/skill/scripts/export_powerpoint.ps1 -InputPptx /absolute/final.pptx -OutDir /absolute/private-render -PythonPath /absolute/runtime/python.exe -Dpi 600
```

This exporter opens a unique temporary read-only copy, records actual text bounds, exports physically sized PNGs and sets DPI metadata without resampling. It closes only that copy, never an already-open user deck or the application. Inspect PNGs and the private text-bounds report. On other platforms use the supported available renderer; an unavailable renderer is an unfinished visual check, not a pass. Shape exports and slide exports can differ in background/transparency.

`audit_pptx.py final.pptx --require-native --min-font-pt 9 --target-width-mm 182` checks requested mechanical conditions. Add `--font` or `--text-color` only for real project constraints. Alignment options compare positions relative to panel frames. Its native-object counts cannot prove scientific truth, fidelity or absence of visual collisions.

Finalize through current presentation instructions. Deliver the native deck plus requested publication export, stating insertion width and external/raster assets. Keep build scripts, runtime links and validation records private unless requested. Render after the final edit and retain the previous usable revision.
