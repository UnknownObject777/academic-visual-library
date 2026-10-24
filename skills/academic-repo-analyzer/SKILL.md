---
name: academic-repo-analyzer
description: Verify research components and meaningful data, gradient or training flow in code for academic figures and manuscript consistency. Return source-grounded findings without a mandatory serialized architecture graph.
metadata:
  version: "5.0.0"
---

# Academic Code Analysis for Figures

Inspect the relevant entry point, configuration and behavior-defining operations. Use names and README descriptions as leads, not implementation evidence. Record the inspected scope and revision when available. Repository installation, whole-project tests and training are not prerequisites for ordinary figure analysis.

Trace the paths that matter to the requested figure: data transformations, gradients and stopped gradients, branches, state updates, communication/aggregation and inference dependencies. Read more only when a figure-critical relation remains uncertain. Imports alone do not establish flow; a file is not automatically a scientific module.

Ground dimensions, formulas and optional/default branches in actual operations. Code inspection verifies implemented behavior within the inspected scope; it does not prove empirical performance or that training was run.

For an existing manuscript or diagram, check its relevant claims rather than replacing its narrative with a directory map. Locate discrepancies using file/symbol evidence and clarify proposed method versus current implementation when necessary.

Return concise findings and source pointers, or directly use them in [the drawing workflow](../academic-figure-workflow/SKILL.md) when a figure was requested. No mandatory node IDs, architecture IR or schema. User-requested machine-readable output may use the requested format. README-only sources support intent, not execution; optional benchmark helpers are unrelated to normal figure drawing.

For text-to-figure work, finish when the implementation-dependent arrows and boundaries needed by that figure are supported or clearly marked as unresolved. Pass those findings into the existing drawing task; source folders and function counts do not dictate panel count, style or a reusable architecture template.
