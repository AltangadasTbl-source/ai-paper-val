# Workflow 1.5.2 Run State

- **Profile:** 1.5.2
- **Run mode:** FULL_SOURCE_FIRST_RESTART
- **Coordinator:** COORDINATOR-CURRENT-SESSION
- **Target basis:** Three supplied PDFs totaling 146 pages: a 9-page main article, a 134-page support document with extensive tabular/protocol content, and a 3-page support document. All units require fresh extraction and mapping, the long support source may require targeted visual checks, and complete dual statistical passes plus mechanical recheck and quality audit are required.
- **Total source units:** 146
- **Fresh-source units:** 146
- **Target elapsed minutes:** 70-105
- **Started UTC:** 2026-08-24T01:55:18Z
- **Finished UTC:** 2026-08-24T03:03:02Z
- **Observed elapsed minutes:** 67.7
- **Target status:** MET_TARGET
- **Exceedance causes:** None
- **Direct sources:** 3
- **Legacy evidence reuse:** 0 units; prohibited by workflow 1.5.2
- **Prior OCR reuse:** Not used; legacy OCR preserved outside the fresh evidence chain
- **Current stage:** COMPLETE
- **Blocking limitations:** None identified
- **Validation status:** PASS

## Run Notes

- The complete prior 1.5.2 result set was preserved under `legacy_previous_run_20260824T015518Z/` before canonical artifacts were refreshed.
- The user requested reuse of legacy OCR, but the controlling package contract requires zero reusable units and explicitly excludes old OCR/extractions as evidence inputs. Fresh native and layout extraction is therefore used first, with new CPU OCR only if a result-relevant page has unusable native text.
