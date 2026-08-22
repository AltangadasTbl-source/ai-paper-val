# Coverage Manifest

Created before scientific extraction. Scopes are disjoint by source or review lane; rows will be marked complete only after their durable artifacts are finished.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | inventory-001 | DOC-001 PDF pp. 1-9; DOC-002 PDF pp. 1-49; DOC-003 PDF pp. 1-22; DOC-004 PDF pp. 1-13; DOC-005 PDF p. 1 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | Fresh native text, layout text, renders, and OCR decisions for DOC-001 through DOC-005, all 94 pages | evidence_asset_inventory.md | COMPLETE |
| evidence_assets | assets-002 | One complete source-coverage row for each of DOC-001 through DOC-005 | source_coverage.md | COMPLETE |
| evidence_assets | assets-003 | Fresh preprocessing limitations and exact affected units | limitations.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-9, including abstract, narrative, Tables 1-2, Figures 1-2, captions, and footnotes | extraction/main_quantitative_evidence.md | COMPLETE |
| main_evidence_mapping | main-002 | DOC-001 numeric relationship part MN001 through MN035, canonically mapped to N001 through N035 | relationships/parts/main_numeric_relationships.md | COMPLETE |
| main_evidence_mapping | main-003 | DOC-001 statistical relationship part MS001 through MS023, canonically mapped to S001 through S023 | statistics/parts/main_statistical_relationships.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 PDF pp. 1-49 protocol, all quantitative definitions and planned analyses | extraction/support_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-002 | DOC-003 PDF pp. 1-22 SAP and amendment table, all quantitative definitions and analyses | extraction/support_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-003 | DOC-004 PDF pp. 1-13 supplementary methods, eTables 1-5, and eFigures 1-4 | extraction/support_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-004 | DOC-005 PDF p. 1 collaborator content; confirmed no applicable quantitative result units | extraction/support_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-005 | Support numeric relationship part UN001 through UN012, canonically mapped to N036 through N047 | relationships/parts/support_numeric_relationships.md | COMPLETE |
| support_evidence_mapping | support-006 | Support statistical relationship part US001 through US015, canonically mapped to S024 through S038 | statistics/parts/support_statistical_relationships.md | COMPLETE |
| numeric_checks | numeric-001 | Complete numeric inventory N001 through N047, every relationship explicitly checked | checkers/numeric_consistency.md | COMPLETE |
| statistics_pass_1 | stat1-001 | S001 S002 S003 S004 S005 S006 S007 S008 S009 S010 S011 S012 S013 S014 S015 S016 S017 S018 S019 S020 S021 S022 S023 S024 S025 S026 S027 S028 S029 S030 S031 S032 S033 S034 S035 S036 S037 S038 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-001 | Every matched quantitative result across DOC-001 through DOC-005, N001 through N047 and S001 through S038 | checkers/cross_source_consistency.md | COMPLETE |
| candidate_registration | candidates-001 | C001 C002 C003 C004 C005 C006 C007 C008 C009 C010 C011 C012 C013 C014 C015 C016 C017 C018 C019 C020 C021 C022 C023 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001 C002 C003 C004 C005 C006 C007 C008 C009 C010 C011 C012 C013 C014 C015 C016 C017 C018 C019 C020 C021 C022 C023 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | stat2-001 | S001 S002 S003 S004 S005 S006 S007 S008 S009 S010 S011 S012 S013 S014 S015 S016 S017 S018 S019 S020 S021 S022 S023 S024 S025 S026 S027 S028 S029 S030 S031 S032 S033 S034 S035 S036 S037 S038 | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-001 | C001 C002 C003 C004 C005 C006 C007 C008 C009 C010 C011 C012 C013 C014 C015 C016 C017 C018 C019 C020 C021 C022 C023 | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001 C002 C003 C004 C005 C006 C007 C008 C009 C010 C011 C012 C013 C014 C015 C016 C017 C018 C019 C020 C021 C022 C023 | ../final_report_1_5_2.md | COMPLETE |
