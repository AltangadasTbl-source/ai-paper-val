# Workflow 1.6.2 Coverage Manifest

Assignments are disjoint by source page. Reusable image-backed plan units receive page-by-page mapping and CPU OCR where text is unusable. Status advances only after durable completion. Runtime identifiers in the execution manifest are canonical tool task identifiers with the leading slash removed.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | inventory-001 | DOC-001 pp. 1-10; DOC-002 pp. 1-94; DOC-003 pp. 1-18; DOC-004 pp. 1-27; DOC-005 pp. 1-8; DOC-006 p. 1; DOC-007 p. 1 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | Every reused extraction, page image, table and source map for all seven direct sources | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-10 | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-results | DOC-004 PDF pp. 1-27; DOC-005 PDF pp. 1-8; DOC-006 PDF p. 1; DOC-007 PDF p. 1 | extraction/support_results_administrative.md | COMPLETE |
| support_evidence_mapping | protocol-001 | DOC-002 PDF pp. 1-24 | extraction/support_protocol_001.md | COMPLETE |
| support_evidence_mapping | protocol-002 | DOC-002 PDF pp. 25-48 | extraction/support_protocol_002.md | COMPLETE |
| support_evidence_mapping | protocol-003 | DOC-002 PDF pp. 49-72 | extraction/support_protocol_003.md | COMPLETE |
| support_evidence_mapping | protocol-004 | DOC-002 PDF pp. 73-94 | extraction/support_protocol_004.md | COMPLETE |
| support_evidence_mapping | sap-001 | DOC-003 PDF pp. 1-18 | extraction/support_sap.md | COMPLETE |
| support_evidence_mapping | support-merged | Complete union of all six disjoint support parts | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-001 | Every numeric relationship across all mapped units; stable N IDs assigned by checker | checkers/numeric_consistency.md | COMPLETE |
| numeric_checks | numeric-support | DOC-004 complete numeric display relationships; N IDs from N121 onward | checkers/numeric_support_part.md | COMPLETE |
| numeric_checks | numeric-inventory | Main numeric relationships from N001 onward | relationships/numeric_relationship_inventory.md | COMPLETE |
| numeric_checks | numeric-support-inventory | Support numeric relationships from N121 onward | relationships/numeric_support_part.md | COMPLETE |
| statistics_pass_1 | statistics-001 | Every statistical relationship across all mapped units; stable S IDs assigned by checker | checkers/statistical_pass_1.md | PENDING |
| statistics_pass_1 | statistics-inventory | Every statistical relationship; stable S IDs assigned by checker | statistics/relationship_inventory.md | PENDING |
| cross_source_checks | cross-001 | Every matching REPORT result and PLAN/REPORT design relationship across all mapped units | checkers/cross_source_consistency.md | PENDING |
| cross_source_checks | cross-plan | PLAN-internal design comparisons across both protocol versions and SAP/addendum | checkers/cross_plan_part.md | COMPLETE |
| inclusion_screening | screening-001 | Every finding from numeric, cross-source and statistical pass 1 checkers | screening/inclusion_screen.md | PENDING |
| candidate_registration | registration-001 | Stable candidate set pending independent screening | candidate_ledger.md | PENDING |
| evidence_recheck | recheck-001 | Stable candidate set pending independent screening | verification/evidence_recheck.md | PENDING |
| statistics_pass_2 | statistics-002 | Complete statistical relationship set pending pass 1 inventory | checkers/statistical_pass_2.md | PENDING |
| evidence_quality | quality-001 | Every source unit, relationship, screening decision and stable candidate | quality/evidence_quality_audit.md | PENDING |
| report_generation | report-001 | Every stable candidate and full completed scope | limitations.md | PENDING |
