# DOC-002 Support Quantitative Evidence Mapping — PDF pp. 85-112

## Scope and direct-source method

- **Direct source:** `joi250042supp1_prod_1753377747.92525.pdf` (DOC-002), PDF pp. 85-112 inclusive (28 pages).
- **Scope status:** COMPLETE for the assigned PDF-page range. These pages contain the tail of Trial Protocol v1.8 / protocol appendices and the beginning of the Statistical and Health Economic Analysis Plan (SHEAP), Version 1.0.
- **Method:** direct PDF page inspection, with fresh CPU raster rendering and visual inspection for pp. 85-88. The PDF's native/layout text uses a nonstandard glyph mapping and was used only to locate sections; it was not treated as authoritative transcription. No reusable DOC-002 extraction exists.
- **Boundary:** protocol version history and planned-analysis specifications are not final trial results. They are mapped as definitions and prospective comparators only.

## Page map

| PDF pages | Direct-source content | Result-relevant status |
|---|---|---|
| 85 | Trial Protocol v1.8, Appendix 2 oxygen-therapy graphic: usual care, no upper SpO2 alarm, clinical team sets oxygenation target and lower alarm limit; printed protocol footer identifies v1.8, 14 October 2024, internal p. 44. | Definition/context; no analysed result. |
| 86 | Trial Protocol v1.8, Appendix 3 expected adverse events; expected SAEs through critical-care discharge after randomisation include sinus tachycardia, supraventricular tachycardia, atrial fibrillation, myocardial ischaemia/infarction, and mesenteric ischaemia; refers SAE recording/reporting to section 3.7. | Safety-definition context; no count or effect estimate. |
| 87 | Trial Protocol summary of changes (v1.1 through v1.8). | Historical definition/context. |
| 88 | SHEAP title/approval page: UK-ROX, “Statistical and Health Economic Analysis Plan (Version 1.0)”; REC 20/SC/0423; sponsor ICNARC; funder reference NIHR130508; ISRCTN13384956; protocol v1.5 dated 12 April 2022. | Version identity / prospective-plan context. |
| 89-112 | SHEAP opening contents and introductory/methods sections: rationale, objectives/outcomes, study design/population, planned statistical analysis and health-economic-analysis framework, with prospective definitions and planned reporting. | Prospective definitions/analysis-plan material; no completed trial-result table, participant count, effect estimate, CI, or P value identified in this assigned segment. |

## Numeric and reporting relationships

### D2D-N001 — Protocol oxygen-target amendment history

- **Exact source:** DOC-002 PDF p. 87, “Protocol v1.2, 19 March 2021.”
- **Printed relationship:** conservative oxygen therapy changed from an SpO2 target range **90-93%** to an SpO2 target **90 ±2%**.
- **Definition/matching note:** both expressions describe a 90%-centred target; 90 ±2% corresponds arithmetically to 88%-92%, not 90%-93%. However, this is a recorded protocol amendment, not two co-presented final-study results. It must not be compared with outcome reporting without matching protocol version, treatment implementation, and measurement rule.
- **Candidate observation:** none registered from this page alone; the source explicitly says the target changed.

### D2D-N002 — Protocol v1.8 secondary-outcome definition

- **Exact source:** DOC-002 PDF p. 87, “Protocol v1.8, 14 October 2024.”
- **Printed relationship:** a clinical secondary outcome was added: “Days alive and free from organ support at 30 days,” ordinal with death worst; organ support is receipt of respiratory, cardiovascular, or renal support within critical care according to the Critical Care Minimum Dataset.
- **Definition/matching note:** outcome time horizon is 30 days; this is not interchangeable with mortality at 30 days or a raw organ-support count.
- **Candidate observation:** none; this is an explicit prospective definition/amendment.

### D2D-N003 — SHEAP/protocol version linkage

- **Exact source:** DOC-002 PDF p. 88.
- **Printed relationship:** SHEAP v1.0 states the linked protocol version is **v1.5 (12 April 2022)**.
- **Definition/matching note:** SHEAP v1.0 predates protocol v1.8, so later-protocol outcomes/definitions (including D2D-N002) should not automatically be assumed present in the original SHEAP without a revised SAP or documented amendment.
- **Candidate observation:** no inconsistency asserted. This is an important version-control matching constraint for cross-source review.

### D2D-N004 — Expected-SAE scope

- **Exact source:** DOC-002 PDF p. 86.
- **Printed relationship:** Appendix 3 defines a list of expected SAEs observable up to critical-care discharge following randomisation.
- **Definition/matching note:** the denominator, event counting rule, and analysis population are not supplied on this page. A later safety table can be compared only after those elements and the event window are matched.
- **Candidate observation:** none.

## Statistical relationships

### D2D-S001 — SHEAP is prospective, not an analysed-result source

- **Exact source:** DOC-002 PDF pp. 88-112, SHEAP Version 1.0 opening material.
- **Printed/statistical context:** the document sets out planned clinical and health-economic analyses for UK-ROX.
- **Mapping implication:** planned outcomes, analysis populations, model labels, confidence intervals, and P-value conventions in this section are prospective definitions. They may support a later check of whether an analysed result is labelled consistently with its plan, but do not constitute a numeric comparator by themselves.
- **Status:** mapped; no candidate observation in the assigned pages.

### D2D-S002 — Outcome/time-horizon distinction

- **Exact source:** DOC-002 PDF p. 87 (v1.8 amendment) and p. 88 (SHEAP linked to v1.5).
- **Printed/statistical context:** the added ordinal “days alive and free from organ support at 30 days” outcome has a defined 30-day horizon and death-as-worst ordering, whereas the SHEAP title page records an earlier linked protocol version.
- **Mapping implication:** cross-document comparison must distinguish a later added ordinal secondary outcome from mortality and from any original SHEAP-defined outcome set; no inferential result is printed here.
- **Status:** mapped; no candidate observation.

## Candidate observations and exclusions

- **Provisional candidates:** 0. No `C`-candidate observation is registered from this scope.
- **Why no candidate was registered:** no pair of matched final reported values, tables, estimates, denominators, confidence intervals, or P values occurs in the assigned pages. The visible numeric statements are protocol/SHEAP identities, dates, target definitions, and planned outcome definitions.
- **No-applicable units:** all 28 pages were inspected and mapped. Pages 85-87 contain protocol appendices/change history; pp. 88-112 contain SHEAP opening/prospective-plan material rather than completed-results evidence.

## Limitations for downstream checking

The source PDF native extraction is glyph-mapped. Visual direct-PDF inspection was used for authoritative transcription of the page-specific printed material cited above. The SHEAP pages should be paired with the final main-paper and results-supplement locations by the eventual cross-source reviewer; no result comparison was attempted in this extraction scope.
