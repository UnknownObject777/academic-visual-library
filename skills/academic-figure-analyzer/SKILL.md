---
name: academic-figure-analyzer
description: Analyze manuscript content, code paths and reference images for scientifically grounded academic figures. Return concise evidence and visual findings without mandatory JSON handoffs; continue through the drawing workflow if drawing was also requested.
metadata:
  version: "0.2.0"
---

# Academic Figure Analyzer

Inspect actual content before routing: a URL may be a paper, repository or figure. Read only material needed for the requested figure. No forced serialized semantic graph or multi-source report.

## Manuscript or notes

Determine the figure's reader question, supported claims, essential operations and relationships. Distinguish mechanism, hypothesis and measured result. Headings and directories are not automatically pipeline stages. An early draft can support a mechanism diagram without fabricated experiments; a full paper does not require multiple figures when one was requested.

## Code

Trace relevant entry points, configuration and operations. Ground dimensions, execution order, gradients/stop-gradients, aggregation and inference dependencies in file/symbol evidence. Imports alone do not establish flow; code inspection is not proof of performance or that training ran. Avoid whole-repository installation and training unless actually needed.

For paper plus code, the paper/user intent defines the narrative; code verifies implementation details. Locate meaningful contradictions and distinguish proposed method from current implementation rather than silently replacing either.

## Reference image

View the image, relevant PDF page and caption. [PDF extraction](references/pdf-extraction.md) is an optional helper, not a semantic classifier. Identify transferable composition, typography, material, marks, strokes and color roles, not just a palette. Exact fonts/hex values are estimates unless measured.

For style transfer, source labels, algorithms and capabilities stay with their original method. For faithful redraw they are preserved except authorized changes. Mark unreadable labels or ambiguous arrows uncertain; never infer hidden science from familiar architecture names.

## Finish

Return concise evidence locations, findings and material uncertainty. Analysis-only requests stop there. If drawing was requested, use [the workflow](../academic-figure-workflow/SKILL.md) directly without an extra handoff or approval gate. Missing science follows [the shared policy](../academic-figure-workflow/references/missing-info-policy.md); reversible style decisions may use reasonable defaults.
