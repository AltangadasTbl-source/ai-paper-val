# Initial Document-Level Record — DOC-001

## Identity and inventory

| Field | Value |
|---|---|
| Document ID | DOC-001 |
| Filename | `jama_flint_2019_oi_190079.pdf` |
| SHA-256 | `bc0a0760a27cbb664dd094b4ee12659acb000baf7c1207930f2558cb39affa45` |
| PDF pages | 10 |
| Text-layer availability | Available; successfully extracted on all 10 pages |
| Metadata author | American Medical Association |
| Likely content type | Main article |
| Article identification | Flint et al., *Effect of Continuing Olanzapine vs Placebo on Relapse Among Patients With Psychotic Depression in Remission: The STOP-PD II Randomized Clinical Trial*. JAMA. 2019;322(7):622-631. DOI: `10.1001/jama.2019.10517` |

## Heading and contents evidence

Page 1 identifies the item as `JAMA | Original Investigation` and reports the title above. It contains the structured abstract and reports 126 randomized participants. Page 3 contains `Figure 1. Flow of Participants`. Pages 5-9 contain Tables 1-5; pages 9-10 contain discussion/end matter and references.

## Extraction/OCR and audit scope

- Text extraction scope: pages 1-10.
- OCR status: not required at inventory stage because an extractable text layer is available on every page.
- Scientific audit status: **Audit target**.
- Audit-relevant pages: 1-10 (abstract, methods/results narrative, Figure 1, Tables 1-5, discussion/end matter).

## AI Training Restriction Record

Pending the separate document-level rights-screen record. This inventory record makes no rights determination.

## Processing status

Inventory completed. No source PDF modified.

## Preprocessing update — 2026-07-30

- Selected audit range: **PDF pages 1-10**. Native text was extracted page by page before any rendering; artifacts are in [`../../preprocessing/DOC-001/`](../../preprocessing/DOC-001/).
- OCR backend selection was recorded before page processing in [`../../preprocessing/ocr_backend.json`](../../preprocessing/ocr_backend.json): `rapidocr-cpu` via `/home/bulunte/venvs/stt/bin/python`, with CPU execution recorded and no CUDA use.
- Rendered pages retained only where visual evidence is needed: p3 (Figure 1 flow), pp5-9 (Tables 1-5). Completed CPU OCR is available for pp3, 5, and 6; each page's provider report and confidence are in the page manifest.
- Page 8 native extraction is corrupted/over-expanded. Its source-linked image is retained, but no completed OCR artifact was retained after the interrupted run. Downstream checks must verify any Table 4 value directly against that image; page 8 normalized native text is not a reliable table transcription.
- Page-level provenance, quality assessments, and extraction status: [`../../preprocessing/DOC-001/page_manifest.json`](../../preprocessing/DOC-001/page_manifest.json).

## Processing status

Preprocessing completed with a documented page-8 qualification; no source PDF was modified.
