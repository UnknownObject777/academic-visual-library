# Native image execution

The current tool description controls APIs, timing and display. Use native image generation/editing for the corresponding requested operation; measured charts use plotting. Respect the user's renderer.

Inspect local targets and references before calling. Describe target scientific content, the role of each supplied image, essential visible strings, actual style and requested changes in ordinary language. No prompt compiler or intermediate representation is needed.

Reference selection for the current interface:

- New image without references: omit reference selectors.
- All required images local: use `referenced_image_paths` with the complete minimal set.
- Any required image conversation-only: use `num_last_images_to_include` with the smallest recent count covering every required image, within the tool limit.

Never supply both selectors. Never invent a local path or silently omit a necessary reference when the available mechanism cannot include it. Request reattachment if necessary. For a local image edit put the target first, followed by relevant style references, and state their roles.

Follow current wrapper wait/yield and `generatedImage(result)` requirements. Do not print base64 results. Keep original assets and link only real returned/saved files. Preserve transparency unless the requested change says otherwise.

Prompt review is opt-in. If the user requested approval before rendering, show the prompt and wait; otherwise render directly. Prompt approval is not visual inspection.

Inspect the actual output using [render-audit.md](render-audit.md). Use targeted native edits for observed defects and preserve correct regions. If exact notation or complex style keeps failing, explain the limitation and use a requested or otherwise authorized suitable approach. Do not substitute Python raster manipulation for image edits unless explicitly requested. Do not claim a raster pasted into a document is an editable diagram.

Preserve metadata/provenance. Metadata cleanup is separate and only performed when requested or required by a specified export format. If rendering or inspection is unavailable, report the unfinished step honestly.
