# AI Paper Validation Workflow

The project root contains one article package: one main article and zero or more supplementary files.
The root thread acts as the `Coordinator`. It owns package inventory, task routing, candidate selection,
and final consolidation. Child agents must not modify source PDFs.

## Workflow

1. Run `package_inventory` to identify source PDFs and classify likely main article, results supplement,
   protocol, SAP, and administrative files.
2. Run `ai_use_restriction_checker` for every source PDF before full-text model-mediated processing.
3. Run `pdf_preprocessor`. It may write derived artifacts only under `.ai_paper_validation/`.
4. Run `main_text_extractor` and `results_supplement_extractor` in parallel.
5. Run `table_arithmetic_checker`, `figure_flow_checker`, and `statistical_consistency_checker` in parallel.
6. Deduplicate and prioritize the returned evidence. Send no more than 10 candidate issues to
   `evidence_verifier`.
7. Send verified findings to `critic`. The critic may retain no more than 10 final issues.
8. Send accepted findings to `report_generator`.
9. Submit the report for `Human Adjudication`.

## Long Supplement Handling

Protocol, SAP, administrative, author-list, and data-sharing sections are not default audit targets.
The coordinator must use the package manifest to restrict extraction, OCR, rendering, and checking to
main-article pages and result-relevant supplementary pages. A protocol/SAP page may be opened only
for a specific parent-requested comparison.

This exemption does not apply to the `AI Training Restriction` screen: every supplied PDF requires a
document-level rights record, even when its scientific content is not audited.

## OCR Backend Selection

Before selective OCR, run `scripts/detect_ocr_backend.py` using `~/venvs/stt/bin/python` when that
interpreter exists; otherwise use the active Python interpreter. Save its JSON output under
`.ai_paper_validation/preprocessing/ocr_backend.json`. The selector recognizes an RTX 5070 Laptop
GPU and other NVIDIA GPUs, validates RapidOCR's actual CUDA execution providers, and otherwise
falls back to RapidOCR CPU or Tesseract CPU.

Use `scripts/ocr_page.py` for every rendered page that needs OCR. A manifest may report GPU OCR
only when its selected backend is `rapidocr-cuda` and its detector, classifier, and recognizer all
report `CUDAExecutionProvider`. CPU fallback is valid; record it explicitly. If no backend is
available, preprocessing must fail when OCR is required.

## AI Training Restriction Screen

This is a separate compliance screen, not a reporting-error category and not part of the `10 / 10 / 2`
limits. For every supplied PDF, retain an `AI Training Restriction Record` with exact file and page
locations, quoted language, and one of these statuses:

- `Explicit AI Training Restriction`
- `Conditional / Permission Required`
- `No AI Training Restriction Located in Provided Materials`
- `Not Stated / Undetermined`

Search only supplied files, including embedded metadata and copyright, license, rights-and-permissions,
and terms pages. Distinguish a restriction on training, fine-tuning, or model improvement from a
restriction on OCR, inference, text-and-data mining, or redistribution. Do not infer permission from
silence and do not provide legal advice. An explicit or conditional restriction requires `Human
Compliance Review` before model-mediated processing not already approved by the institution.

## Limits

- Maximum candidate issues per article package: 10.
- Maximum final issues per article package: 10.
- Maximum verification rounds per candidate: 2.
- The workflow ends after one verification stage and one critic stage.

## Evidence Standard

Each final issue must be a self-contained evidence card for a human reviewer. It requires a
one-sentence issue statement; category and severity; exact location for every cited item (document
ID and filename, PDF page, and table, figure, panel, row, column, footnote, or section/paragraph
label when available); labelled verbatim source excerpts or values with units; a direct
reported-versus-comparator comparison; and a reproducible calculation or logical chain with inputs,
formula or rule, result, units, and any rounding tolerance considered. It must also state the bounded
impact on the reported total, statement, or interpretation, and give numbered verification steps that
say what a human should check and which result would confirm or resolve the issue. The workflow must
classify a finding with unavailable necessary evidence as `Rejected` or `Uncertain`, naming the
missing evidence rather than implying a conclusion. Derived artifacts must retain a page-level link
to their source PDF.

The coordinator must preserve a document-level output for every supplied PDF under
`.ai_paper_validation/document_outputs/<document_id>/`, including its inventory classification,
rights record, extraction/OCR scope, processing status, and each agent response or an explicit
`Not Audited by Design` record. Preserve source PDFs unchanged. The final report must include a
separate `AI Training Restriction Summary` table and must not merge it into the scientific issue list.

## Scope

Allowed issue categories are `Arithmetic inconsistency`, `Cross-document inconsistency`,
`Statistical reporting inconsistency`, `Participant flow inconsistency`, and `Presentation inconsistency`.

Do not assess research misconduct, raw-data validity, clinical appropriateness, general methodological
limitations, novelty, or information not contained in the article package. Do not use web search,
external retrieval, or unstated external knowledge.
