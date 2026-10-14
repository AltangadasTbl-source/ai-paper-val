# Workflow 1.6.2 Coverage Manifest

Every mapping assignment is disjoint. Text shards must stay below 200000 normalized characters; each optional direct visual shard stays below 32 rendered pages. Fresh OCR is complete-page transcription from reusable images, followed by direct-source mapping and exact-source confirmation.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | sources-all | DOC-001 pp. 1-11; DOC-002 pp. 1-35; DOC-003 pp. 1-162; DOC-004 pp. 1-48; DOC-005 pp. 1-16 | source_inventory.md | COMPLETE |
| evidence_assets | reusable-all | Every eligible reused extraction, map, and page image identified by curator | evidence_asset_inventory.md | COMPLETE |
| evidence_assets | gpu-ocr-derivatives | DOC-002 pp. 1-35; DOC-003 pp. 1-162; DOC-004 pp. 1-48; 245 page transcripts and raw logs | preprocessing/gpu_ocr/derivative_manifest.md | COMPLETE |
| main_evidence_mapping | main-all | DOC-001 pp. 1-11 | extraction/main_quantitative_evidence.md | COMPLETE |
| main_evidence_mapping | main-numeric | DOC-001 Table 1 and Figure 1 numeric relationships | extraction/main_numeric_01.md | COMPLETE |
| main_evidence_mapping | main-statistics | DOC-001 all inferential result rows and method relationships | extraction/main_statistics_01.md | COMPLETE |
| support_evidence_mapping | protocol-1 | DOC-002 pp. 1-18 | extraction/parts/protocol_001_018.md | COMPLETE |
| support_evidence_mapping | protocol-2 | DOC-002 pp. 19-35 | extraction/parts/protocol_019_035.md | COMPLETE |
| support_evidence_mapping | results-all | DOC-005 pp. 1-16 | extraction/parts/results_001_016.md | COMPLETE |
| support_evidence_mapping | protocol-results-merge | Aggregate of disjoint protocol-1, protocol-2 and results-all parts | extraction/parts/protocol_results.md | COMPLETE |
| support_evidence_mapping | protocol-results-numeric | Numeric relationship transcription index for protocol and results | relationships/parts/protocol_results.md | COMPLETE |
| support_evidence_mapping | protocol-results-statistics | Statistical relationship transcription index for protocol and results | statistics/parts/protocol_results.md | COMPLETE |
| support_evidence_mapping | sap-1 | DOC-004 pp. 1-24 | extraction/parts/sap_001_024.md | COMPLETE |
| support_evidence_mapping | sap-2 | DOC-004 pp. 25-48 | extraction/parts/sap_025_048.md | COMPLETE |
| support_evidence_mapping | sap-merge | Aggregate of disjoint sap-1 and sap-2 parts | extraction/parts/sap.md | COMPLETE |
| support_evidence_mapping | manual-a-1 | DOC-003 pp. 1-27 | extraction/parts/manual_001_027.md | COMPLETE |
| support_evidence_mapping | manual-a-2 | DOC-003 pp. 28-54 | extraction/parts/manual_028_054.md | COMPLETE |
| support_evidence_mapping | manual-a-merge | Aggregate of disjoint manual-a-1 and manual-a-2 parts | extraction/parts/manual_001_054.md | COMPLETE |
| support_evidence_mapping | manual-b-1 | DOC-003 pp. 55-81 | extraction/parts/manual_055_081.md | COMPLETE |
| support_evidence_mapping | manual-b-2 | DOC-003 pp. 82-108 | extraction/parts/manual_082_108.md | COMPLETE |
| support_evidence_mapping | manual-b-index | Index of disjoint manual-b-1 and manual-b-2 mapping parts | extraction/parts/manual_055_108.md | COMPLETE |
| support_evidence_mapping | manual-c-1 | DOC-003 pp. 109-135 | extraction/parts/manual_109_135.md | COMPLETE |
| support_evidence_mapping | manual-c-2 | DOC-003 pp. 136-162 | extraction/parts/manual_136_162.md | COMPLETE |
| support_evidence_mapping | manual-c-merge | Aggregate of disjoint manual-c-1 and manual-c-2 mapping parts | extraction/parts/manual_109_162.md | COMPLETE |
| support_evidence_mapping | support-merge | Complete disjoint support mapping union | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-1 | N001, N002, N003, N004, N005, N006, N007, N008, N009, N010, N011, N012, N013, N014, N015, N016, N017, N018, N019, N020, N021, N022, N023, N024, N025, N026, N027, N028, N029, N030, N031, N032, N033, N034, N035, N036, N037, N038, N039, N040, N041, N042, N043, N044, N045, N046, N047, N048, N049, N050, N051, N052, N053, N054, N055, N056, N057, N058, N059, N060, N061, N062, N063, N064, N065, N066, N067, N068, N069, N070, N071, N072, N073, N074, N075, N076, N077, N078, N079, N080, N081, N082, N083, N084, N085, N201, N202, N203, N204, N205, N206, N207, N208, N209, N210, N211, N212, N213, N214, N215, N216, N217, N218, N219, N220, N221, N222, N223, N224, N225, N226, N227, N228, N229, N230, N231, N232, N233, N234, N235 | checkers/parts/numeric_1.md | COMPLETE |
| numeric_checks | numeric-2 | N236, N237, N238, N239, N240, N401, N402, N403, N404, N405, N406, N407, N408, N409, N410, N411, N412, N413, N414, N415, N416, N417, N418, N419, N420, N421, N422, N423, N424, N425, N426, N427, N428, N429, N430, N431, N432, N433, N434, N435, N436, N437, N438, N439, N440, N441, N442, N443, N444, N445, N446, N447, N448, N449, N450, N601, N602, N603, N604, N605, N606, N607, N608, N609, N610, N611, N612, N613, N614, N615, N616, N617, N618, N619, N620, N621, N622, N623, N624, N625, N626, N627, N628, N629, N630, N631, N632, N633, N634, N635, N636, N637, N638, N639, N640, N701, N702, N703, N704, N705, N706, N707, N708, N709, N710, N711, N712, N713, N714, N715, N716, N717, N718, N719, N720, N721, N722, N723, N724, N725 | checkers/parts/numeric_2.md | COMPLETE |
| numeric_checks | numeric-3 | N726, N727, N728, N729, N730, N731, N732, N733, N734, N735, N736, N737, N738, N739, N740, N741, N742, N743, N744, N745, N746, N747, N748, N749, N750, N751, N752, N753, N754, N755, N756, N757, N758, N801, N802, N803, N804, N805, N806, N807, N808, N809, N810, N811, N812, N813, N814 | checkers/parts/numeric_3.md | COMPLETE |
| numeric_checks | numeric-merge | Aggregate of disjoint numeric-1, numeric-2 and numeric-3 | checkers/numeric_consistency.md | COMPLETE |
| statistics_pass_1 | statistical-1-1 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S222, S223, S224, S225, S226, S227, S228, S229, S230, S231, S232, S233, S234, S235, S236, S237, S238, S239, S240, S241, S242, S243, S244, S245, S246, S247, S248, S249, S250, S251, S252, S253, S254, S255, S256, S257, S258, S259, S260, S261, S262, S263, S264, S265, S266, S267, S268, S269, S270, S271, S272 | checkers/parts/statistical_pass_1_1.md | COMPLETE |
| statistics_pass_1 | statistical-1-2 | S273, S274, S275, S276, S277, S278, S279, S401, S402, S403, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419, S420, S421, S422, S423, S424, S425, S426, S427, S428, S429, S430, S431, S432, S433, S434, S435, S601, S602, S603, S604, S605, S606, S607, S608, S609, S610, S611, S612, S613, S701, S801, S802, S803, S804, S805, S806, S807, S808, S809, S810, S811, S812, S813, S814, S815, S816, S817, S818, S819, S820, S821, S822, S823, S824, S825, S826, S827, S828, S829, S830, S831, S832, S833 | checkers/parts/statistical_pass_1_2.md | COMPLETE |
| statistics_pass_1 | statistical-1-merge | Aggregate of disjoint statistical-1-1 and statistical-1-2 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-primary | All report matched results and report versus protocol or SAP; protocol versus SAP | checkers/parts/cross_source_primary.md | COMPLETE |
| cross_source_checks | cross-manual | All relevant comparisons involving manual versus report or protocol or SAP | checkers/parts/cross_source_manual.md | COMPLETE |
| cross_source_checks | cross-merge | Aggregate of disjoint cross-primary and cross-manual comparisons | checkers/cross_source_consistency.md | COMPLETE |
| inclusion_screening | screen-initial | Every finding from three initial checkers | screening/inclusion_screen.md | COMPLETE |
| candidate_registration | ledger-all | C001, C002, C003, C004, C005, C006 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-all | C001, C002, C003, C004, C005, C006 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistical-2-merge | Aggregate of disjoint statistical-2-1 and statistical-2-2 | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | audit-all | C001, C002, C003, C004, C005, C006; all screening and excluded observations; full coverage | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-all | C001, C002, C003, C004, C005, C006 | limitations.md | COMPLETE |

| statistics_pass_1 | statistical-status-1 | Explicit completion receipts for the first disjoint statistical shard | statistics/parts/pass_1_status_1.md | COMPLETE |
| statistics_pass_1 | statistical-status-2 | Explicit completion receipts for the second disjoint statistical shard | statistics/parts/pass_1_status_2.md | COMPLETE |
| numeric_checks | numeric-status-2 | Explicit numeric completion receipts for numeric shard 2 | relationships/parts/numeric_status_2.md | COMPLETE |

| statistics_pass_2 | statistical-2-1 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S222, S223, S224, S225, S226, S227, S228, S229, S230, S231, S232, S233, S234, S235, S236, S237, S238, S239, S240, S241, S242, S243, S244, S245, S246, S247, S248, S249, S250, S251, S252, S253, S254, S255, S256, S257, S258, S259, S260, S261, S262, S263, S264, S265, S266, S267, S268, S269, S270, S271, S272 | checkers/parts/statistical_pass_2_1.md | COMPLETE |
| statistics_pass_2 | statistical-2-2 | S273, S274, S275, S276, S277, S278, S279, S401, S402, S403, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419, S420, S421, S422, S423, S424, S425, S426, S427, S428, S429, S430, S431, S432, S433, S434, S435, S601, S602, S603, S604, S605, S606, S607, S608, S609, S610, S611, S612, S613, S701, S801, S802, S803, S804, S805, S806, S807, S808, S809, S810, S811, S812, S813, S814, S815, S816, S817, S818, S819, S820, S821, S822, S823, S824, S825, S826, S827, S828, S829, S830, S831, S832, S833 | checkers/parts/statistical_pass_2_2.md | COMPLETE |

| numeric_checks | relationships-parts-assigned_n_1 | Explicit bounded relationship assignment roster | relationships/parts/assigned_n_1.md | COMPLETE |
| numeric_checks | relationships-parts-assigned_n_2 | Explicit bounded relationship assignment roster | relationships/parts/assigned_n_2.md | COMPLETE |
| numeric_checks | relationships-parts-assigned_n_3 | Explicit bounded relationship assignment roster | relationships/parts/assigned_n_3.md | COMPLETE |
| support_evidence_mapping | relationships-parts-manual_a | Completed mapper relationship transcription supplement | relationships/parts/manual_a.md | COMPLETE |
| statistics_pass_1 | statistics-parts-assigned_s_1 | Explicit bounded relationship assignment roster | statistics/parts/assigned_s_1.md | COMPLETE |
| statistics_pass_1 | statistics-parts-assigned_s_2 | Explicit bounded relationship assignment roster | statistics/parts/assigned_s_2.md | COMPLETE |
| support_evidence_mapping | statistics-parts-manual_a | Completed mapper relationship transcription supplement | statistics/parts/manual_a.md | COMPLETE |

| statistics_pass_2 | statistical-status-2-1 | Explicit completion receipts for disjoint second-pass shard 1 | statistics/parts/pass_2_status_1.md | COMPLETE |
| statistics_pass_2 | statistical-status-2-2 | Explicit completion receipts for disjoint second-pass shard 2 | statistics/parts/pass_2_status_2.md | COMPLETE |

| evidence_quality | audit-part-audit_calculations-json | Independent audit receipt and supporting calculation or exclusion record | quality/parts/audit_calculations.json | COMPLETE |
| evidence_quality | audit-part-audit_excluded_observations-md | Independent audit receipt and supporting calculation or exclusion record | quality/parts/audit_excluded_observations.md | COMPLETE |
| evidence_quality | audit-part-audit_local_link_issues-json | Independent audit receipt and supporting calculation or exclusion record | quality/parts/audit_local_link_issues.json | COMPLETE |
| evidence_quality | audit-part-audit_mechanical_receipt-json | Independent audit receipt and supporting calculation or exclusion record | quality/parts/audit_mechanical_receipt.json | COMPLETE |
| evidence_quality | audit-part-audit_post_repair_links-json | Independent audit receipt and supporting calculation or exclusion record | quality/parts/audit_post_repair_links.json | COMPLETE |
| evidence_quality | audit-part-audit_reused_hash_check-log | Independent audit receipt and supporting calculation or exclusion record | quality/parts/audit_reused_hash_check.log | COMPLETE |
| evidence_quality | audit-part-audit_source_unit_receipt-json | Independent audit receipt and supporting calculation or exclusion record | quality/parts/audit_source_unit_receipt.json | COMPLETE |
| evidence_quality | audit-part-audit_sources_hash_check-log | Independent audit receipt and supporting calculation or exclusion record | quality/parts/audit_sources_hash_check.log | COMPLETE |
| evidence_quality | audit-part-coordinator_artifact_repairs-md | Independent audit receipt and supporting calculation or exclusion record | quality/parts/coordinator_artifact_repairs.md | COMPLETE |

| report_generation | complete-markdown | Complete six-candidate report assembly and metadata | ../final_report_1_6_2.md | COMPLETE |

| report_generation | standalone-html | Complete standalone HTML with embedded CSS and table of contents | ../final_report_1_6_2.html | COMPLETE |

| report_generation | final-closure | Mechanical final artifact, anchor and completion receipt | completion_record.md | COMPLETE |
