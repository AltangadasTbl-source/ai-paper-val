# Direct-source inventory

Inventory scope: current paper package only; every supplied PDF, DOC, DOCX, XLS, XLSX, and CSV. Three PDF direct sources were found; no supplied Office or CSV sources. Workflow controls and audit derivatives are not direct scientific sources.

| Source ID | Source path | Format | Document role | Role basis from content | Unit type | Total units |
|---|---|---|---|---|---|---:|
| DOC-001 | jama_wang_2018_oi_180070.pdf | PDF | REPORT | Main randomized clinical trial article, abstract, methods, reported results, tables and figures, discussion and references | PDF_PAGE | 10 |
| DOC-002 | joi180070supp1_prod.pdf | PDF | PLAN | Prospective GOLDEN BRIDGE-AIS protocol dated 2014/4/17; trial organization, intervention, outcomes, data handling and statistical analysis specifications | PDF_PAGE | 25 |
| DOC-003 | joi180070supp2_prod.pdf | PDF | REPORT | Supplementary online content: eAppendix baseline survey, performance-measure specifications and eTables 2–4 of reported observations and sensitivity results | PDF_PAGE | 9 |

No mixed REPORT/PLAN physical bundle was identified. Supplement 1 is PLAN by content despite its filename. Supplement 2 specifies performance measures within non-plan supporting results material and is REPORT.

Current counts were independently obtained with direct `pdfinfo` 25.03.0. The legacy metadata files give the same page counts and byte sizes (505453, 735518, 334922 respectively). Stable source identity is recorded in `source_hashes_before.sha256`; all paths there are package-relative and refer to supplied source bytes. No source or pre-existing asset was modified.

Curation checked every individual PDF page against its reusable native-text page using direct `pdftotext -f N -l N SOURCE -`, form-feed segmentation of legacy text with `awk`, ordered alphanumeric normalization with `tr -cd '[:alnum:]'`, and SHA-256 with `sha256sum` 9.7. All 44 page pairs matched exactly after that normalization. This check establishes page correspondence and broad extraction fitness; symbols, table alignment, figure content and candidate evidence remain subject to mapper inspection and exact-source recheck. Legacy TSV page keys independently cover the full 10/25/9 page sets.

Downstream assignments: main mapper covers DOC-001 pp. 1–10; support mapper covers DOC-002 pp. 1–25 and DOC-003 pp. 1–9. All units require fresh scientific mapping even when transcription assets are reused. Native text is usable across the source universe, with page images available for diagrams and dense displays. No scientific extraction gap remains at curation. Missing legacy images: DOC-001 p. 10 and DOC-002 pp. 22–25; render these directly if visual inspection needs arise. DOC-002 p. 5 has limited native text but a readable complete reusable flow-diagram image; its embedded labels require visual mapping from that image.
