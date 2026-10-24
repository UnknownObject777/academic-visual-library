# PDF figure extraction

Use a PDF-capable reader first to locate the requested figure and caption. A diagram drawn with vector primitives may not appear among embedded raster images; render its page when needed.

The bundled [extract_pdf_figures.py](../scripts/extract_pdf_figures.py) can extract image candidates with Poppler or PyMuPDF. Resolve its absolute installed path and use the available Python interpreter. The command shape is:

```text
python "<absolute-skill-dir>/scripts/extract_pdf_figures.py" "<paper.pdf>" -o "<output-directory>"
```

Inspect `--help` for the current options. Supported options include `--backend auto|pdfimages|pymupdf`, `--pages 1-3|all`, `--dpi`, `--min-side`, and `--min-pixels`. The size filters can discard small valid diagrams; adjust them to the requested figure. Page rendering and embedded extraction may have different backend requirements.

Read `extract-report.json`, then inspect relevant candidates. The helper does not detect architectures or verify semantics. Record the page/figure, caption, original source, and actual local image path. If no extraction backend is available, use a directly viewable PDF page or request an exported figure.
