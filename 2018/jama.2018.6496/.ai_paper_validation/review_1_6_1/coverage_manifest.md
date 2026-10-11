# Workflow 1.6.1 Coverage Manifest

Coverage assignments were created after curation and before scientific mapping. All units are reusable-backed; no unit requires fresh extraction initially. Every page is assigned to exactly one mapper. Artifact paths are relative to this run directory. Status is finalized only after artifact-first completion.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | sources-001 | DOC-001 PDF pp. 1-11; DOC-002 PDF pp. 1-25; DOC-003 PDF pp. 1-13 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | A001 through A047; source-matched native/layout text and rendered pages | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-11; all text, tables, figures and references | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 PDF pp. 1-25; protocol, statistical plan and administrative/reference content | extraction/support_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-002 | DOC-003 PDF pp. 1-13; results, interim analysis, figures and operational instrument | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-001 | All counts, denominator, arithmetic and effect-label relationships reconstructed from M001-M110 and M073a-M073l plus U01-U45 as applicable | checkers/numeric_consistency.md | COMPLETE |
| numeric_checks | numeric-inventory-001 | Complete applicable numeric relationship inventory with mapping cross-references | relationships/numeric_relationship_inventory.md | COMPLETE |
| statistics_pass_1 | statistics-001 | S001; S002; S003; S004; S005; S006; S007; S008; S009; S010; S011; S012; S013; S014; S015; S016; S017; S018; S019; S020; S021; S022; S023; S024; S025; S026; S027; S028; S029; S030; S031; S032; S033; S034; S035; S036; S037; S038; S039; S040; S041; S042; S043; S044; S045; S046; S047; S048; S049; S050; S051; S052; S053; S054; S055; S056; S057; S058; S059; S060; S061; S062; S063; S064; S065; S066; S067; S068; S069; S070; S071; S072; S073; S074; S075; S076; S077; S078; S079; S080; S081; S082; S083; S084; S085; S086;  | checkers/statistical_pass_1.md | COMPLETE |
| statistics_pass_1 | statistics-inventory-001 | S001; S002; S003; S004; S005; S006; S007; S008; S009; S010; S011; S012; S013; S014; S015; S016; S017; S018; S019; S020; S021; S022; S023; S024; S025; S026; S027; S028; S029; S030; S031; S032; S033; S034; S035; S036; S037; S038; S039; S040; S041; S042; S043; S044; S045; S046; S047; S048; S049; S050; S051; S052; S053; S054; S055; S056; S057; S058; S059; S060; S061; S062; S063; S064; S065; S066; S067; S068; S069; S070; S071; S072; S073; S074; S075; S076; S077; S078; S079; S080; S081; S082; S083; S084; S085; S086;  | statistics/relationship_inventory.md | COMPLETE |
| cross_source_checks | cross-001 | Matched main/report-supplement results and all applicable plan/report and plan-internal design specifications | checkers/cross_source_consistency.md | COMPLETE |
| inclusion_screening | screen-initial-001 | F-XS-001; F-XS-002; F-ST1-001; F-ST1-002; F-ST1-003; numeric checker emitted no findings | screening/inclusion_screen.md | COMPLETE |
| candidate_registration | ledger-001 | C001 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001; every affected and corroborating source location | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistics-002 | S001; S002; S003; S004; S005; S006; S007; S008; S009; S010; S011; S012; S013; S014; S015; S016; S017; S018; S019; S020; S021; S022; S023; S024; S025; S026; S027; S028; S029; S030; S031; S032; S033; S034; S035; S036; S037; S038; S039; S040; S041; S042; S043; S044; S045; S046; S047; S048; S049; S050; S051; S052; S053; S054; S055; S056; S057; S058; S059; S060; S061; S062; S063; S064; S065; S066; S067; S068; S069; S070; S071; S072; S073; S074; S075; S076; S077; S078; S079; S080; S081; S082; S083; S084; S085; S086;  | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | audit-001 | C001; every screening decision, checker exclusion, relationship and source-coverage row | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001 | ../final_report_1_6_1.md | COMPLETE |
| report_generation | limitations-001 | C001; complete package definitions and tooling limitations | limitations.md | COMPLETE |

Mapping assignment scopes are disjoint by physical source page; support-001 and support-002 are separate source scopes within one durable canonical support artifact. Subsequent checkers compare these mapped scopes independently. Statistical scopes enumerate every canonical S ID, and candidate scopes enumerate every stable C ID. Planned downstream rows become COMPLETE only after their unique outputs exist.
