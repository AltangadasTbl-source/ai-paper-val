# Coverage Manifest

Created before scientific mapping. Reusable coverage and fresh-required scope are disjoint. Each artifact cell is one plain relative path. Planned rows are finalized to COMPLETE after durable evidence is checked; relationship/candidate scopes are enumerated when IDs are assigned.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | inventory-001 | DOC-001 PDF pp. 1–9; DOC-002 PDF pp. 1–26; DOC-003 PDF pp. 1–24; DOC-004 PDF pp. 1–11 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | Every retained eligible source-linked text/OCR/table/rendered-page/map artifact; 34 uniquely reusable pages | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1–9, all reusable-backed units | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 PDF pp. 1–26 fresh GPU OCR; DOC-003 PDF pp. 1–24 (reusable pp. 7–22, fresh pp. 1–6 and 23–24); DOC-004 PDF pp. 1–11 (reusable p. 1 and pp. 4–11, fresh pp. 2–3) | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-001 | Every main and support count/denominator/result-display relationship; IDs assigned by checker | checkers/numeric_consistency.md | COMPLETE |
| statistics_pass_1 | stat1-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, S113, S114, S115, S116, S117, S118, S119, S120, S121, S122, S123, S124 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-001 | All matched REPORT/REPORT, PLAN/REPORT and result-relevant PLAN/PLAN relationships | checkers/cross_source_consistency.md | COMPLETE |
| inclusion_screening | screen-001 | Every initial checker finding; no count target | screening/inclusion_screen.md | COMPLETE |
| candidate_registration | candidates-001 | C001 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | stat2-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, S113, S114, S115, S116, S117, S118, S119, S120, S121, S122, S123, S124 | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-001 | C001; all coverage and screening decisions | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001; full provenance and summaries | limitations.md | COMPLETE |
| source_inventory | identity-main | DOC-001 PDF p. 1 identity native locator | preprocessing/curator-DOC-001-p1.txt | COMPLETE |
| source_inventory | identity-protocol | DOC-002 PDF p. 1 native fitness locator | preprocessing/curator-DOC-002-p1.txt | COMPLETE |
| source_inventory | identity-protocol-visual | DOC-002 PDF p. 1 direct rendered identity | preprocessing/curator-DOC-002-p1.png | COMPLETE |
| source_inventory | identity-SAP | DOC-003 PDF p. 1 identity native locator | preprocessing/curator-DOC-003-p1.txt | COMPLETE |
| source_inventory | identity-results | DOC-004 PDF p. 1 identity native locator | preprocessing/curator-DOC-004-p1.txt | COMPLETE |
| support_evidence_mapping | protocol-001-png | DOC-002 PDF p. 1 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-001.png | COMPLETE |
| support_evidence_mapping | protocol-001-gpu-ocr.log | DOC-002 PDF p. 1 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-001-gpu-ocr.log | COMPLETE |
| support_evidence_mapping | protocol-001-gpu-ocr.txt | DOC-002 PDF p. 1 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-001-gpu-ocr.txt | COMPLETE |
| support_evidence_mapping | protocol-002-png | DOC-002 PDF p. 2 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-002.png | COMPLETE |
| support_evidence_mapping | protocol-002-gpu-ocr.log | DOC-002 PDF p. 2 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-002-gpu-ocr.log | COMPLETE |
| support_evidence_mapping | protocol-002-gpu-ocr.txt | DOC-002 PDF p. 2 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-002-gpu-ocr.txt | COMPLETE |
| support_evidence_mapping | protocol-003-png | DOC-002 PDF p. 3 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-003.png | COMPLETE |
| support_evidence_mapping | protocol-003-gpu-ocr.log | DOC-002 PDF p. 3 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-003-gpu-ocr.log | COMPLETE |
| support_evidence_mapping | protocol-003-gpu-ocr.txt | DOC-002 PDF p. 3 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-003-gpu-ocr.txt | COMPLETE |
| support_evidence_mapping | protocol-004-png | DOC-002 PDF p. 4 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-004.png | COMPLETE |
| support_evidence_mapping | protocol-004-gpu-ocr.log | DOC-002 PDF p. 4 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-004-gpu-ocr.log | COMPLETE |
| support_evidence_mapping | protocol-004-gpu-ocr.txt | DOC-002 PDF p. 4 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-004-gpu-ocr.txt | COMPLETE |
| support_evidence_mapping | protocol-005-png | DOC-002 PDF p. 5 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-005.png | COMPLETE |
| support_evidence_mapping | protocol-005-gpu-ocr.log | DOC-002 PDF p. 5 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-005-gpu-ocr.log | COMPLETE |
| support_evidence_mapping | protocol-005-gpu-ocr.txt | DOC-002 PDF p. 5 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-005-gpu-ocr.txt | COMPLETE |
| support_evidence_mapping | protocol-006-png | DOC-002 PDF p. 6 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-006.png | COMPLETE |
| support_evidence_mapping | protocol-006-gpu-ocr.log | DOC-002 PDF p. 6 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-006-gpu-ocr.log | COMPLETE |
| support_evidence_mapping | protocol-006-gpu-ocr.txt | DOC-002 PDF p. 6 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-006-gpu-ocr.txt | COMPLETE |
| support_evidence_mapping | protocol-007-png | DOC-002 PDF p. 7 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-007.png | COMPLETE |
| support_evidence_mapping | protocol-007-gpu-ocr.log | DOC-002 PDF p. 7 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-007-gpu-ocr.log | COMPLETE |
| support_evidence_mapping | protocol-007-gpu-ocr.txt | DOC-002 PDF p. 7 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-007-gpu-ocr.txt | COMPLETE |
| support_evidence_mapping | protocol-008-png | DOC-002 PDF p. 8 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-008.png | COMPLETE |
| support_evidence_mapping | protocol-008-gpu-ocr.log | DOC-002 PDF p. 8 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-008-gpu-ocr.log | COMPLETE |
| support_evidence_mapping | protocol-008-gpu-ocr.txt | DOC-002 PDF p. 8 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-008-gpu-ocr.txt | COMPLETE |
| support_evidence_mapping | protocol-009-png | DOC-002 PDF p. 9 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-009.png | COMPLETE |
| support_evidence_mapping | protocol-009-gpu-ocr.log | DOC-002 PDF p. 9 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-009-gpu-ocr.log | COMPLETE |
| support_evidence_mapping | protocol-009-gpu-ocr.txt | DOC-002 PDF p. 9 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-009-gpu-ocr.txt | COMPLETE |
| support_evidence_mapping | protocol-010-png | DOC-002 PDF p. 10 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-010.png | COMPLETE |
| support_evidence_mapping | protocol-010-gpu-ocr.log | DOC-002 PDF p. 10 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-010-gpu-ocr.log | COMPLETE |
| support_evidence_mapping | protocol-010-gpu-ocr.txt | DOC-002 PDF p. 10 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-010-gpu-ocr.txt | COMPLETE |
| support_evidence_mapping | protocol-011-png | DOC-002 PDF p. 11 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-011.png | COMPLETE |
| support_evidence_mapping | protocol-011-gpu-ocr.log | DOC-002 PDF p. 11 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-011-gpu-ocr.log | COMPLETE |
| support_evidence_mapping | protocol-011-gpu-ocr.txt | DOC-002 PDF p. 11 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-011-gpu-ocr.txt | COMPLETE |
| support_evidence_mapping | protocol-012-png | DOC-002 PDF p. 12 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-012.png | COMPLETE |
| support_evidence_mapping | protocol-012-gpu-ocr.log | DOC-002 PDF p. 12 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-012-gpu-ocr.log | COMPLETE |
| support_evidence_mapping | protocol-012-gpu-ocr.txt | DOC-002 PDF p. 12 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-012-gpu-ocr.txt | COMPLETE |
| support_evidence_mapping | protocol-013-png | DOC-002 PDF p. 13 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-013.png | COMPLETE |
| support_evidence_mapping | protocol-013-gpu-ocr.log | DOC-002 PDF p. 13 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-013-gpu-ocr.log | COMPLETE |
| support_evidence_mapping | protocol-013-gpu-ocr.txt | DOC-002 PDF p. 13 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-013-gpu-ocr.txt | COMPLETE |
| support_evidence_mapping | protocol-014-png | DOC-002 PDF p. 14 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-014.png | COMPLETE |
| support_evidence_mapping | protocol-014-gpu-ocr.log | DOC-002 PDF p. 14 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-014-gpu-ocr.log | COMPLETE |
| support_evidence_mapping | protocol-014-gpu-ocr.txt | DOC-002 PDF p. 14 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-014-gpu-ocr.txt | COMPLETE |
| support_evidence_mapping | protocol-015-png | DOC-002 PDF p. 15 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-015.png | COMPLETE |
| support_evidence_mapping | protocol-015-gpu-ocr.log | DOC-002 PDF p. 15 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-015-gpu-ocr.log | COMPLETE |
| support_evidence_mapping | protocol-015-gpu-ocr.txt | DOC-002 PDF p. 15 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-015-gpu-ocr.txt | COMPLETE |
| support_evidence_mapping | protocol-016-png | DOC-002 PDF p. 16 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-016.png | COMPLETE |
| support_evidence_mapping | protocol-016-gpu-ocr.log | DOC-002 PDF p. 16 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-016-gpu-ocr.log | COMPLETE |
| support_evidence_mapping | protocol-016-gpu-ocr.txt | DOC-002 PDF p. 16 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-016-gpu-ocr.txt | COMPLETE |
| support_evidence_mapping | protocol-017-png | DOC-002 PDF p. 17 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-017.png | COMPLETE |
| support_evidence_mapping | protocol-017-gpu-ocr.log | DOC-002 PDF p. 17 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-017-gpu-ocr.log | COMPLETE |
| support_evidence_mapping | protocol-017-gpu-ocr.txt | DOC-002 PDF p. 17 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-017-gpu-ocr.txt | COMPLETE |
| support_evidence_mapping | protocol-018-png | DOC-002 PDF p. 18 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-018.png | COMPLETE |
| support_evidence_mapping | protocol-018-gpu-ocr.log | DOC-002 PDF p. 18 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-018-gpu-ocr.log | COMPLETE |
| support_evidence_mapping | protocol-018-gpu-ocr.txt | DOC-002 PDF p. 18 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-018-gpu-ocr.txt | COMPLETE |
| support_evidence_mapping | protocol-019-png | DOC-002 PDF p. 19 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-019.png | COMPLETE |
| support_evidence_mapping | protocol-019-gpu-ocr.log | DOC-002 PDF p. 19 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-019-gpu-ocr.log | COMPLETE |
| support_evidence_mapping | protocol-019-gpu-ocr.txt | DOC-002 PDF p. 19 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-019-gpu-ocr.txt | COMPLETE |
| support_evidence_mapping | protocol-020-png | DOC-002 PDF p. 20 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-020.png | COMPLETE |
| support_evidence_mapping | protocol-020-gpu-ocr.log | DOC-002 PDF p. 20 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-020-gpu-ocr.log | COMPLETE |
| support_evidence_mapping | protocol-020-gpu-ocr.txt | DOC-002 PDF p. 20 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-020-gpu-ocr.txt | COMPLETE |
| support_evidence_mapping | protocol-021-png | DOC-002 PDF p. 21 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-021.png | COMPLETE |
| support_evidence_mapping | protocol-021-gpu-ocr.log | DOC-002 PDF p. 21 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-021-gpu-ocr.log | COMPLETE |
| support_evidence_mapping | protocol-021-gpu-ocr.txt | DOC-002 PDF p. 21 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-021-gpu-ocr.txt | COMPLETE |
| support_evidence_mapping | protocol-022-png | DOC-002 PDF p. 22 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-022.png | COMPLETE |
| support_evidence_mapping | protocol-022-gpu-ocr.log | DOC-002 PDF p. 22 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-022-gpu-ocr.log | COMPLETE |
| support_evidence_mapping | protocol-022-gpu-ocr.txt | DOC-002 PDF p. 22 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-022-gpu-ocr.txt | COMPLETE |
| support_evidence_mapping | protocol-023-png | DOC-002 PDF p. 23 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-023.png | COMPLETE |
| support_evidence_mapping | protocol-023-gpu-ocr.log | DOC-002 PDF p. 23 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-023-gpu-ocr.log | COMPLETE |
| support_evidence_mapping | protocol-023-gpu-ocr.txt | DOC-002 PDF p. 23 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-023-gpu-ocr.txt | COMPLETE |
| support_evidence_mapping | protocol-024-png | DOC-002 PDF p. 24 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-024.png | COMPLETE |
| support_evidence_mapping | protocol-024-gpu-ocr.log | DOC-002 PDF p. 24 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-024-gpu-ocr.log | COMPLETE |
| support_evidence_mapping | protocol-024-gpu-ocr.txt | DOC-002 PDF p. 24 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-024-gpu-ocr.txt | COMPLETE |
| support_evidence_mapping | protocol-025-png | DOC-002 PDF p. 25 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-025.png | COMPLETE |
| support_evidence_mapping | protocol-025-gpu-ocr.log | DOC-002 PDF p. 25 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-025-gpu-ocr.log | COMPLETE |
| support_evidence_mapping | protocol-025-gpu-ocr.txt | DOC-002 PDF p. 25 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-025-gpu-ocr.txt | COMPLETE |
| support_evidence_mapping | protocol-026-png | DOC-002 PDF p. 26 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-026.png | COMPLETE |
| support_evidence_mapping | protocol-026-gpu-ocr.log | DOC-002 PDF p. 26 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-026-gpu-ocr.log | COMPLETE |
| support_evidence_mapping | protocol-026-gpu-ocr.txt | DOC-002 PDF p. 26 fresh derivative; PyMuPDF CPU render / RapidOCR CUDA OCR | preprocessing/doc002-page-026-gpu-ocr.txt | COMPLETE |
| numeric_checks | numeric-inventory | N001, N002, N003, N004, N005, N006, N007, N008, N009, N010, N011, N012, N013, N014, N015, N016, N017, N018, N019, N020, N021, N022, N023, N024, N025, N026, N027, N028, N029, N030, N031, N032, N033, N034, N035, N036, N037, N038, N039, N040, N041, N042, N043, N044, N045, N046, N047, N048, N049, N050, N051, N052, N053, N054, N055, N056, N057, N058, N059, N060, N061, N062, N063, N064, N065, N066, N067, N068, N069, N070, N071, N072, N073, N074, N075, N076, N077, N078, N079, N080, N101, N102, N103, N104, N105, N106, N107, N108, N109, N110, N111 | relationships/numeric_relationship_inventory.md | COMPLETE |
| statistics_pass_1 | stat-inventory | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, S113, S114, S115, S116, S117, S118, S119, S120, S121, S122, S123, S124 | statistics/relationship_inventory.md | COMPLETE |
| support_evidence_mapping | sap-fresh-1 | DOC-003 PDF p. 1 fresh native layout, PyMuPDF 1.26.4 CPU | preprocessing/support-mapper-sap-1.txt | COMPLETE |
| support_evidence_mapping | sap-fresh-2 | DOC-003 PDF p. 2 fresh native layout, PyMuPDF 1.26.4 CPU | preprocessing/support-mapper-sap-2.txt | COMPLETE |
| support_evidence_mapping | sap-fresh-3 | DOC-003 PDF p. 3 fresh native layout, PyMuPDF 1.26.4 CPU | preprocessing/support-mapper-sap-3.txt | COMPLETE |
| support_evidence_mapping | sap-fresh-4 | DOC-003 PDF p. 4 fresh native layout, PyMuPDF 1.26.4 CPU | preprocessing/support-mapper-sap-4.txt | COMPLETE |
| support_evidence_mapping | sap-fresh-5 | DOC-003 PDF p. 5 fresh native layout, PyMuPDF 1.26.4 CPU | preprocessing/support-mapper-sap-5.txt | COMPLETE |
| support_evidence_mapping | sap-fresh-6 | DOC-003 PDF p. 6 fresh native layout, PyMuPDF 1.26.4 CPU | preprocessing/support-mapper-sap-6.txt | COMPLETE |
| support_evidence_mapping | sap-fresh-23 | DOC-003 PDF p. 23 fresh native layout, PyMuPDF 1.26.4 CPU | preprocessing/support-mapper-sap-23.txt | COMPLETE |
| support_evidence_mapping | sap-fresh-24 | DOC-003 PDF p. 24 fresh native layout, PyMuPDF 1.26.4 CPU | preprocessing/support-mapper-sap-24.txt | COMPLETE |
| support_evidence_mapping | results-fresh-2 | DOC-004 PDF p. 2 fresh native layout, PyMuPDF 1.26.4 CPU | preprocessing/support-mapper-result-2.txt | COMPLETE |
| support_evidence_mapping | results-fresh-3 | DOC-004 PDF p. 3 fresh native layout, PyMuPDF 1.26.4 CPU | preprocessing/support-mapper-result-3.txt | COMPLETE |
| cross_source_checks | cross-main3-render | DOC-001 PDF p. 3 analysis specification, direct render | preprocessing/cross-checker-main3.png | COMPLETE |
| cross_source_checks | cross-main7-render | DOC-001 PDF p. 7 clinical event display, direct render | preprocessing/cross-checker-main7.png | COMPLETE |
| cross_source_checks | cross-SAP20-render | DOC-003 PDF p. 20 clinical event analysis plan, direct render | preprocessing/cross-checker-sap20.png | COMPLETE |
| cross_source_checks | cross-SAP-layout | DOC-003 PDF pp. 5–23 planned analysis definitions, fresh layout | preprocessing/cross-checker-sap5-23.txt | COMPLETE |
| numeric_checks | numeric-documentation | Documentation and link repair of all 91 N groups and eight exclusions; audit-located N104 diagnostic transcriptions repaired without source or candidate changes | quality/numeric_documentation_repair.md | COMPLETE |
| inclusion_screening | screen-main1-render | F-XS-001; DOC-001 PDF p. 1 prespecified claim scope | preprocessing/screen-initial-main1.png | COMPLETE |
| inclusion_screening | screen-main5-render | F-XS-001; DOC-001 PDF p. 5 clinical estimates | preprocessing/screen-initial-main5.png | COMPLETE |
| inclusion_screening | screen-SAP5-render | F-XS-001; DOC-003 PDF p. 5 additional-analysis clause | preprocessing/screen-initial-sap5.png | COMPLETE |
| inclusion_screening | screen-SAP21-render | F-XS-001; DOC-003 PDF p. 21 additional-analysis clause | preprocessing/screen-initial-sap21.png | COMPLETE |
| inclusion_screening | screen-power-computation | F-ST1-001; all 24 Table 4 power cells and 12 sample-size cells, full conservative interval arithmetic | preprocessing/screen-initial-power-computation.json | COMPLETE |
| evidence_recheck | recheck-power-computation | C001; independent all-cell power and sample-size calculations with full rounding enclosure | preprocessing/recheck-initial-power-computation.json | COMPLETE |
| statistics_pass_2 | stat2-computations | S001, S003, S004, S005, S006, S007, S008, S009, S015, S113, S116, S117, S118, S119, S120, S121, S122; independent source-derived power, sample-size and P-value calculations | preprocessing/stat2-independent-computations.json | COMPLETE |
| evidence_quality | audit-SAP12-render | DOC-003 PDF p. 12; outcome-status screening and exclusion audit | preprocessing/audit-sap-12.png | COMPLETE |
| evidence_quality | audit-SAP14-render | DOC-003 PDF p. 14; endpoint and imputation-context exclusion audit | preprocessing/audit-sap-14.png | COMPLETE |
| evidence_quality | audit-SAP18-render | DOC-003 PDF p. 18; prespecified subgroup and method audit | preprocessing/audit-sap-18.png | COMPLETE |
| evidence_quality | audit-SAP19-render | DOC-003 PDF p. 19; sensitivity and method audit | preprocessing/audit-sap-19.png | COMPLETE |
| evidence_quality | audit-computations | C001; all 24 Table 4 power cells, full rounding enclosure and N104 diagnostic transcription audit | preprocessing/audit-independent-computations.json | COMPLETE |
| report_generation | report-markdown | C001; complete final Markdown report | ../final_report_1_6_2.md | COMPLETE |
| report_generation | report-html | C001; standalone HTML report with embedded CSS and table of contents | ../final_report_1_6_2.html | COMPLETE |
