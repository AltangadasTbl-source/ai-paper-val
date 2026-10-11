# Quantitative Reporting Quality-Control Consistency Review — Workflow 1.6

**Pending Human Adjudication**

Every candidate in this report awaits human review. Evidence states describe the source recheck; suggested review dispositions are mechanical pre-fills for that review. They do not decide validity, importance, action, or acceptance.

## Executive Quality-Control Summary

Complete review of the six supplied PDFs, comprising 100 physical pages, produced **106 stable quality-control candidates**. All 106 receive complete evidence cards and remain Pending Human Adjudication. Fresh numeric, statistical, and cross-document discovery used source-matched reusable extraction and rendered pages, followed by direct-source recheck and an independent evidence-quality audit.

The classification table records 91 candidates as `recorded_candidate` and 15 as `record_input_error`. The latter preserve comparisons whose original input or alignment premise is unsupported by the supplied evidence; they require discussion rather than being presented as established discrepancies. The mechanically suggested dispositions are consequently 91 `retain` and 15 `discuss`. These counts describe review records, not 106 established reporting errors.

The candidates concern printed numbers, denominators, statistical intervals or comparisons, effect labels and scales, matched report locations, and internal plan quantities or monitoring displays. Several questions depend on an unreported estimator, denominator, rounding convention, scale origin, or time definition. Small preventable reporting defects can matter for downstream evidence extraction if confirmed. This report makes no claim that a candidate propagated into another evidence product, changed a conclusion, or caused serious harm.

## Package and Reused-Evidence Provenance

The supplied package is the 2019 JAMA paper package identified by `jama.2019.7505`. Physical PDF page numbers below are one-based and include cover, reference, and administrative pages. Document roles follow content rather than supplement numbering.

| Source ID | Actual supplied filename | Content role | Physical pages | Reusable pages | Fresh-required extraction pages | Freshly mapped pages |
|---|---|---|---:|---:|---:|---:|
| DOC-001 | [jama_bluth_2019_oi_190055_16092.pdf](<../jama_bluth_2019_oi_190055_16092.pdf#page=1>) | REPORT — main article | 14 | 14 | 0 | 14 |
| DOC-002 | [joi190055supp1_prod_16092.pdf](<../joi190055supp1_prod_16092.pdf#page=1>) | PLAN — protocol and historical/background planning material | 36 | 36 | 0 | 36 |
| DOC-003 | [joi190055supp2_prod_16092.pdf](<../joi190055supp2_prod_16092.pdf#page=1>) | PLAN — protocol amendments | 3 | 3 | 0 | 3 |
| DOC-004 | [joi190055supp3_prod_16092.pdf](<../joi190055supp3_prod_16092.pdf#page=1>) | PLAN — updated statistical analysis plan | 3 | 3 | 0 | 3 |
| DOC-005 | [joi190055supp4_prod_16092.pdf](<../joi190055supp4_prod_16092.pdf#page=1>) | REPORT — non-plan methods and results supplement | 43 | 43 | 0 | 43 |
| DOC-006 | [joi190055supp5_prod_16092.pdf](<../joi190055supp5_prod_16092.pdf#page=1>) | PLAN — prospective data-sharing/access statement | 1 | 1 | 0 | 1 |
| **Total** | **Six PDFs** | **Two REPORT; four PLAN** | **100** | **100** | **0** | **100** |

The [source inventory](review_1_6/source_inventory.md) records identities and content-role reasons. The [evidence asset inventory](review_1_6/evidence_asset_inventory.md) lists 85 reused assets: six native-text files, six layout-text files, six PDF-information records, and 67 rendered pages. All native/layout page segments matched current direct-source extraction after whitespace removal; all 67 renders matched direct source-page rendering. Eighty-three assets were usable; two text assets were partial for embedded figure pixels, with exact-page renders closing those gaps. All 12 supplementary figures had reusable page images.

Reusable assets below `review_1_5_2/preprocessing/` supplied locators and transcription aids. Existing candidate selections, dispositions, classifications, and final reports supplied no discovery scope. Direct PDFs remained the evidence authority. Native/layout and image validation used local Poppler 26.01.0; reused-image equivalence was checked at 150 dpi. These are current validation engines, rather than inferred historical extraction commands. No Office or structured-data source was supplied.

## Scope, Complete Coverage, and Exclusions

The [source coverage ledger](review_1_6/source_coverage.md) records complete mapping for all 100 of 100 unique source pages. Reusable plus fresh-required extraction units partition each source, and mapped units equal total units for every source. Zero fresh-required extraction units means usable preprocessing already existed; scientific mapping and candidate discovery were fresh for every page. Optional missing renders, OCR, or dedicated table derivatives did not leave an uncovered scientific unit.

Review included numeric identities and arithmetic; numerator, denominator, percentage and total agreement; effect estimates, intervals, P values, tests, labels, scales and directions; matched locations across supplied documents; and plan/report comparisons with concrete quantitative consequences. Population or analysis-unit definitions were included when they affected a reported number, statistic, denominator, label, or interpretation. Administrative and reference pages were inspected and mapped even when they supplied no quantitative relationship.

This is reporting quality control. General study-design, clinical, novelty, misconduct and raw-data audits were outside scope. Only supplied package evidence was used. Coherent display-zero P values alone were excluded under `DISPLAY_ZERO_NOT_CANDIDATE`; they do not justify a candidate. No candidate was selected or omitted to meet a count or timing target. The [coverage manifest](review_1_6/coverage_manifest.md) records disjoint scopes and durable artifacts.

## Quantitative and Statistical Relationship Coverage

| Review lane | Relationships or groups | Completed scope |
|---|---:|---|
| Numeric narrative and baseline | 102 | N001–N102 |
| Numeric main outcomes and partitions | 120 | N121–N240 |
| Numeric supplementary result tables | 119 | N241–N359 |
| Numeric plan, methods and plots | 120 | N361–N480 |
| **Numeric total** | **461** | **Every registered relationship checked** |
| Statistical main article | 105 | S001–S105; both passes complete |
| Statistical result tables | 86 | S121–S206; both passes complete |
| Statistical plan and other plots | 116 | S241–S356; both passes complete |
| Statistical physiology plots | 66 | S401–S466; both passes complete |
| **Statistical total** | **373** | **PASS_1_COMPLETE and PASS_2_COMPLETE for every relationship** |
| Cross-source matched groups | 34 | All six supplied documents represented |

Reserved ID-block gaps reflect shard capacity, not omitted relationships. Compound numeric records preserve their individual printed cells and applicable rules. The physiology scope includes 60 plotted mean/interval relationships and six printed interaction tests. Both statistical passes used fresh, distinct high-effort agents and complete disjoint scopes; pass 2 considered the complete cross-lane ledger and all recheck facts and added no new distinct candidate.

Durable records include the [relationship coverage summary](review_1_6/relationship_coverage_summary.md), [numeric inventory](review_1_6/relationships/numeric_relationship_inventory.md), [statistical inventory](review_1_6/statistics/relationship_inventory.md), [numeric checker](review_1_6/checkers/numeric_consistency.md), [cross-source checker](review_1_6/checkers/cross_source_consistency.md), [statistical pass 1](review_1_6/checkers/statistical_pass_1.md), and [statistical pass 2](review_1_6/checkers/statistical_pass_2.md). Every stable ID also appears in the [candidate ledger](review_1_6/candidate_ledger.md), [mechanical recheck](review_1_6/verification/evidence_recheck.md), and [quality audit](review_1_6/quality/evidence_quality_audit.md).

## Document-Role Classification Summary

`S_W` denotes a discrepancy within one REPORT document. `S_C` denotes a discrepancy between different REPORT documents. `P_R` denotes a PLAN–REPORT discrepancy without implying a proven protocol violation. `P_P` denotes a discrepancy solely within PLAN material, including historical or background material inside a plan bundle. Mixed substantive relationships follow `P_R` > `P_P` > `S_C` > `S_W`; a corroborating document alone does not create another discrepancy relationship.

| Primary relationship type | Candidates |
|---|---:|
| S_W | 79 |
| S_C | 18 |
| P_R | 1 |
| P_P | 8 |
| **Total** | **106** |

| Mechanically derived review domain | Candidates |
|---|---:|
| statistical_results | 37 |
| report_internal_inconsistency | 60 |
| protocol_report | 1 |
| plan_material | 8 |
| **Total** | **106** |

| Mechanical evidence state | Candidates | Suggested review disposition |
|---|---:|---|
| recorded_candidate | 91 | retain |
| record_input_error | 15 | discuss |
| not_reproduced | 0 | exclude |
| repaired_residual | 0 | retain |
| **Total** | **106** | **Mechanical pre-fill only** |

Each summary independently reconciles to 106. Classification fields in each card reproduce the final ledger classification table exactly. `recorded_candidate` may retain a conditional question pending a named missing definition; it does not establish validity. The 15 input-error records remain visible under their stable IDs with the unsupported premise explained. Human adjudication is required for every state and suggested disposition.

## Candidate Index

| ID | Candidate | Category | Relationship type | Review domain | Evidence state |
|---|---|---|---|---|---|
| C001 | abstract randomized-group populations equal analyzed populations | Analysis-unit or population inconsistency | S_W | statistical_results | recorded_candidate |
| C002 | matched hypoxemia confidence-limit sign differs | Statistical reporting inconsistency | S_W | statistical_results | recorded_candidate |
| C003 | complementary surgical-approach rows switch denominators — H arm | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C004 | complementary surgical-approach rows switch denominators — L arm | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C005 | Reflux,n/N(%), high group | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C006 | Diabetes,n/N(%), high group | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C007 | Diabetes oral medication,n/N(%), high group | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C008 | Obstructive-sleep-apnea header-denominator input error | Denominator, proportion, or total inconsistency | S_W | statistical_results | record_input_error |
| C009 | Tobacco never,n/N(%), high group | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C010 | Tobacco never,n/N(%), low group | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C011 | Tobacco previous,n/N(%), high group | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C012 | Tobacco current,n/N(%), low group | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C013 | Antibiotic prophylaxis,n/N(%), high group | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C014 | Antibiotic prophylaxis,n/N(%), low group | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C015 | Monitoring displayed percentages versus absolute difference | Numeric or arithmetic inconsistency | S_W | statistical_results | recorded_candidate |
| C016 | Reversal displayed percentage direction versus absolute difference | Numeric or arithmetic inconsistency | S_W | statistical_results | recorded_candidate |
| C017 | Any recruitment,No.(%): absolute difference versus exact printed risks | Numeric or arithmetic inconsistency | S_W | statistical_results | recorded_candidate |
| C018 | Heat rate label versus beats-per-minute measurements | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C019 | Noninvasive ventilation,No.(%): L printed percentage identity | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C020 | Noninvasive ventilation,No.(%): absolute difference versus exact printed risks | Numeric or arithmetic inconsistency | S_W | statistical_results | recorded_candidate |
| C021 | Monitoring neuromuscular function,n/N(%): H printed percentage identity | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C022 | Monitoring neuromuscular function,n/N(%): L printed percentage identity | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C023 | Reversal,n/N(%): H printed percentage identity | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C024 | Reversal,n/N(%): L printed percentage identity | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C025 | Reversal,n/N(%): absolute difference versus exact printed risks | Numeric or arithmetic inconsistency | S_W | statistical_results | recorded_candidate |
| C026 | Unsupported total-fluids median/effect alignment | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | record_input_error |
| C027 | Primary PPC within5days: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C028 | Mild respiratory failure: absolute difference versus exact printed risks | Numeric or arithmetic inconsistency | S_W | statistical_results | recorded_candidate |
| C029 | Mild respiratory failure: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C030 | Moderate respiratory failure: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C031 | Severe respiratory failure: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C032 | Atelectasis: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C033 | Pleural effusion: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C034 | New pulmonary infiltrates: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C035 | Cardiopulmonary edema: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C036 | Bronchospasm: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C037 | Pulmonary infection: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C038 | Aspiration pneumonitis: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C039 | ARDS: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C040 | Pneumothorax: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C041 | Severe postoperative PPC: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C042 | Postoperative extrapulmonary composite: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C043 | Systemic inflammatory response syndrome: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C044 | Sepsis: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C045 | Severe sepsis: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C046 | Septic shock: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C047 | Gastrointestinal failure: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C048 | Acute kidney failure: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C049 | Kidney failure,n/N(%): H printed percentage identity | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C050 | Kidney loss,n/N(%): H printed percentage identity | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C051 | Extrapulmonary infection: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C052 | Hepatic failure: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C053 | Coma: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C054 | Disseminated intravascular coagulation: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C055 | Impaired postoperative wound healing: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C056 | Unexpected ICU admission/readmission: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C057 | Intraoperative hypoxemia: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C058 | Intraoperative hypotension: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C059 | Intraoperative bradycardia: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C060 | Mortality during hospital stay: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C061 | Post hoc rescue strategy for desaturation: absolute difference versus exact printed risks | Numeric or arithmetic inconsistency | S_W | statistical_results | recorded_candidate |
| C062 | Post hoc rescue strategy for desaturation: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C063 | Post hoc vasoactive drugs: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C064 | Nonlaparoscopic: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C065 | Laparoscopic: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C066 | BMI<40: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C067 | BMI≥40: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C068 | SpO2<96%: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C069 | SpO2≥96%: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C070 | Peripheral incision: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C071 | Upper abdominal: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C072 | Waist-to-hip<1.0: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C073 | Waist-to-hip ratio assigned a length unit | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C074 | Waist-to-hip≥1.0: labeled RR versus printed patient risks | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C075 | Mortality figure caption attaches percentages to extrapulmonary complications | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C076 | Collapsed-composite effect labeled OR in supplement and RR in main | Measure, label, or scale inconsistency | S_C | report_internal_inconsistency | recorded_candidate |
| C077 | Synthetic-colloid count comparison P differs | Statistical reporting inconsistency | S_C | statistical_results | recorded_candidate |
| C078 | Mild respiratory-failure oxygen boundary equals2 versus at most2 | Analysis-unit or population inconsistency | S_C | statistical_results | recorded_candidate |
| C079 | Emergency-procedure counts differ between main and surgical supplement | Cross-document numeric inconsistency | S_C | report_internal_inconsistency | recorded_candidate |
| C080 | Hypoxemia duration-qualifier omission and unresolved event-field identity | Analysis-unit or population inconsistency | S_C | statistical_results | record_input_error |
| C081 | Hypotension duration-qualifier omission and unresolved event-field identity | Analysis-unit or population inconsistency | S_C | statistical_results | record_input_error |
| C082 | conditional thoracic VAS mean/SD bound | Numeric or arithmetic inconsistency | P_R | protocol_report | recorded_candidate |
| C083 | conditional event-count mean versus component total | Denominator, proportion, or total inconsistency | S_C | statistical_results | recorded_candidate |
| C084 | Conditional follow-up/time-origin reconciliation question — eFigure8 | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C085 | Conditional follow-up/time-origin reconciliation question — eFigure9 | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C086 | Conditional follow-up/time-origin reconciliation question — eFigure10 | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C087 | Conditional follow-up/time-origin reconciliation question — eFigure11 | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C088 | Mild respiratory failure: modeled-versus-crude comparator input error | Measure, label, or scale inconsistency | S_C | report_internal_inconsistency | record_input_error |
| C089 | Moderate respiratory failure: modeled-versus-crude comparator input error | Measure, label, or scale inconsistency | S_C | report_internal_inconsistency | record_input_error |
| C090 | Severe respiratory failure: modeled-versus-crude comparator input error | Measure, label, or scale inconsistency | S_C | report_internal_inconsistency | record_input_error |
| C091 | Aspiration: modeled-versus-crude comparator input error | Measure, label, or scale inconsistency | S_C | report_internal_inconsistency | record_input_error |
| C092 | Bronchospasm: modeled-versus-crude comparator input error | Measure, label, or scale inconsistency | S_C | report_internal_inconsistency | record_input_error |
| C093 | ARDS: modeled-versus-crude comparator input error | Measure, label, or scale inconsistency | S_C | report_internal_inconsistency | record_input_error |
| C094 | Atelectasis: modeled-versus-crude comparator input error | Measure, label, or scale inconsistency | S_C | report_internal_inconsistency | record_input_error |
| C095 | Cardiopulmonary edema: modeled-versus-crude comparator input error | Measure, label, or scale inconsistency | S_C | report_internal_inconsistency | record_input_error |
| C096 | Pleural effusion: modeled-versus-crude comparator input error | Measure, label, or scale inconsistency | S_C | report_internal_inconsistency | record_input_error |
| C097 | Pneumothorax: modeled-versus-crude comparator input error | Measure, label, or scale inconsistency | S_C | report_internal_inconsistency | record_input_error |
| C098 | Pulmonary infiltrates: modeled-versus-crude comparator input error | Measure, label, or scale inconsistency | S_C | report_internal_inconsistency | record_input_error |
| C099 | Revised PLAN target versus retained procedural total | Numeric or arithmetic inconsistency | P_P | plan_material | recorded_candidate |
| C100 | Conditional futility-region comparison at look 1 | Statistical reporting inconsistency | P_P | plan_material | recorded_candidate |
| C101 | Conditional futility-region comparison at look 2 | Statistical reporting inconsistency | P_P | plan_material | recorded_candidate |
| C102 | Conditional futility-region comparison at look 3 | Statistical reporting inconsistency | P_P | plan_material | recorded_candidate |
| C103 | Original primary-analysis effect label combines OR and RR | Measure, label, or scale inconsistency | P_P | plan_material | recorded_candidate |
| C104 | Conditional efficacy-sign comparison at look 1 | Statistical reporting inconsistency | P_P | plan_material | recorded_candidate |
| C105 | Conditional efficacy-sign comparison at look 2 | Statistical reporting inconsistency | P_P | plan_material | recorded_candidate |
| C106 | Conditional efficacy-sign comparison at look 3 | Statistical reporting inconsistency | P_P | plan_material | recorded_candidate |

## Candidate Evidence Cards

## C001 — abstract randomized-group populations equal analyzed populations

Pending Human Adjudication.

**Candidate statement:** The abstract labels group sizes 989 and 987 as randomized, whereas Figure 1 reports allocation sizes 1011 and 1002; the smaller sizes match the analyzed population.

**Category:** Analysis-unit or population inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** Abstract INTERVENTIONS and RESULTS (p. 1); Figure 1 allocation and primary-analysis boxes (p. 3); Statistical Analysis and Results population descriptions (p. 4). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 1](<../jama_bluth_2019_oi_190055_16092.pdf#page=1>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 3](<../jama_bluth_2019_oi_190055_16092.pdf#page=3>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>)

**Source evidence:** Abstract: randomized high n=989 and low n=987; Figure 1: 1011 and 1002 randomized/allocated, 989 and 987 included in primary analysis; Results: 2013 randomized, 1976 analyzed.

**Reported-versus-comparator:** Explicit allocation counts 1011/1002 and total 2013 versus abstract randomized-labelled counts 989/987. Exact population-label and allocation-count identity; randomized denominators and analyzed denominators must be distinguished when their printed values differ.

**Reasoning procedure:** Read the printed components at the linked source locations, distinguish observed values from conditional calculations, and apply the comparison rule above. Exact integer counts and population labels have zero arithmetic tolerance; the applicability of a shared population is considered separately.

**Calculation:** 989 + 987 = 1976; 1011 + 1002 = 2013; high difference 22, low difference 15; 22 + 15 = 37 = 2013 − 1976.

**Alternative source-grounded interpretations:** The abstract can be read as a compressed description of analyzed treatment groups; its RESULTS explicitly distinguishes 2013 randomized from 1976 completing the trial. That does not make the INTERVENTIONS n values the allocation counts. Direct: the population labels and four arm counts. Inferred: analyzed sizes may have been inserted into the allocation description; no production mechanism is established.

**Mechanical evidence recheck:** The exact source retains randomized wording with analysis sizes and separately prints larger allocation sizes. Evidence state recorded_candidate. This field reports the completed source recheck; it is not human adjudication.

**Quality-control relevance:** This candidate identifies a reproducible numeric, denominator, display or measure-label comparison within the supplied REPORT. Small preventable reporting defects can matter for downstream evidence extraction; the named population, estimand or display questions bound this observation.

**Potential downstream evidence impact:** An extractor preparing a systematic review or meta-analysis could copy randomized allocation sizes 989/987 instead of 1011/1002, thereby conflating allocated and analyzed denominators by 37 patients. If human review confirms a reporting defect, documenting its definition or correction could improve extraction consistency. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:**

1. Open the linked physical PDF page(s) and inspect the named row, heading, reference population and applicable footnotes.
2. Transcribe the printed inputs exactly, retaining signs, units, slash denominators and header-versus-row distinctions.
3. Reproduce the comparison and calculation above under its stated rule and tolerance; then test the source-grounded alternatives without assigning an unstated denominator or estimator.
4. Resolve the specific question: None for literal count/label comparison. Intended abstract referent remains unnamed. Should the abstract INTERVENTIONS n values describe the allocated groups (1011/1002) or the analyzed groups (989/987)?
5. Record the human decision in the blank fields below; the suggested review disposition is a mechanical pre-fill, not an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — matched hypoxemia confidence-limit sign differs

Pending Human Adjudication.

**Candidate statement:** The abstract and Table 3 give opposite signs for the upper confidence limit of the same hypoxemia difference: +6.1% versus −6.1%.

**Category:** Statistical reporting inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** Abstract RESULTS hypoxemia sentence (p. 1); Table 3 Intraoperative adverse events, Hypoxemia row (p. 9). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 1](<../jama_bluth_2019_oi_190055_16092.pdf#page=1>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>)

**Source evidence:** Abstract difference −8.6%, 95% CI −11.1% to +6.1%, P<.001; Table 3 difference −8.6%, 95% CI −11.1 to −6.1, P<.001.

**Reported-versus-comparator:** Signed upper CI limit +6.1 in the abstract versus −6.1 in Table 3 for the matched outcome/contrast. Matched-report identity at equal precision; no CI/P convention is needed to compare the endpoint signs.

**Reasoning procedure:** Read the printed components at the linked source locations, distinguish observed values from conditional calculations, and apply the comparison rule above. Matched signed endpoints have zero identity tolerance; ±0.05 percentage point endpoint rounding cannot reconcile a 12.2-point gap.

**Calculation:** +6.1 − (−6.1) = 12.2 percentage points. The abstract interval includes zero and the table interval does not. Endpoint rounding cannot reconcile the sign difference.

**Alternative source-grounded interpretations:** An omitted minus sign is a plausible explanation. If the abstract refers to a different analysis, its identity and model must be supplied; the printed point difference and P value match the table. Direct: both endpoints and matched contrast. Inferred: omitted minus sign; no inference that one CI must be adopted.

**Mechanical evidence recheck:** Fresh direct extraction and visual rendering both show positive 6.1 in the abstract and negative −6.1 in Table 3. Evidence state recorded_candidate. This field reports the completed source recheck; it is not human adjudication.

**Quality-control relevance:** This candidate identifies a reproducible numeric, denominator, display or measure-label comparison within the supplied REPORT. Small preventable reporting defects can matter for downstream evidence extraction; the named population, estimand or display questions bound this observation.

**Potential downstream evidence impact:** An extractor preparing a systematic review or meta-analysis could copy an upper confidence limit of +6.1% instead of −6.1%, changing the extracted interval’s null-crossing description. If human review confirms a reporting defect, documenting its definition or correction could improve extraction consistency. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:**

1. Open the linked physical PDF page(s) and inspect the named row, heading, reference population and applicable footnotes.
2. Transcribe the printed inputs exactly, retaining signs, units, slash denominators and header-versus-row distinctions.
3. Reproduce the comparison and calculation above under its stated rule and tolerance; then test the source-grounded alternatives without assigning an unstated denominator or estimator.
4. Resolve the specific question: None for the literal sign mismatch. A distinct abstract model/population is not identified. Which signed upper CI limit belongs to the abstract hypoxemia difference, and is the abstract intended to repeat Table 3?
5. Record the human decision in the blank fields below; the suggested review disposition is a mechanical pre-fill, not an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — complementary surgical-approach rows switch denominators — H arm

Pending Human Adjudication.

**Candidate statement:** The H-arm abdominal and nonabdominal rows use denominators 986 and 987 although their counts sum to 986. A discrepancy depends on the rows being one complementary classification.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** Table 1 Surgical approach, Type of abdominal incision and Nonabdominal H cells; footnotes a and i (p. 6). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 6](<../jama_bluth_2019_oi_190055_16092.pdf#page=6>)

**Source evidence:** H: abdominal 894/986, nonabdominal 92/987. Footnote a permits characteristics not assessed in all patients; i defines abdominal open and endoscopic categories.

**Reported-versus-comparator:** The same arm's two printed denominators 986 and 987 and complementary-labelled category sum. A single mutually exclusive/exhaustive abdominal-versus-nonabdominal classification has one observed denominator. Applicability is conditional on these rows being one classification, rather than independently missing binary indicators.

**Reasoning procedure:** Read the printed components at the linked source locations, distinguish observed values from conditional calculations, and apply the comparison rule above. Exact integer counts and population labels have zero arithmetic tolerance; the applicability of a shared population is considered separately.

**Calculation:** 894 + 92 = 986; printed denominators differ by one (986 versus 987). The sum equals 986 and differs from 987 by one.

**Alternative source-grounded interpretations:** Footnote a allows missingness; independent category-specific indicators could have distinct observed denominators. It does not expressly define such separate indicators. A denominator transposition is an inferred explanation, not established. Direct: numerator/denominator cells, category labels and footnotes. Conditional derivation: one shared classification denominator. Inferred: transposed denominators or differently missing indicators.

**Mechanical evidence recheck:** The source reproduces the denominator switch and count sum; the same-classification question remains as registered pending its named definition. Evidence state recorded_candidate. This field reports the completed source recheck; it is not human adjudication.

**Quality-control relevance:** This candidate identifies a reproducible numeric, denominator, display or measure-label comparison within the supplied REPORT. Small preventable reporting defects can matter for downstream evidence extraction; the named population, estimand or display questions bound this observation.

**Potential downstream evidence impact:** An extractor preparing a systematic review or meta-analysis could copy H surgical-approach denominators 986 and 987 without knowing whether the two categories share one observed population. If human review confirms a reporting defect, documenting its definition or correction could improve extraction consistency. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:**

1. Open the linked physical PDF page(s) and inspect the named row, heading, reference population and applicable footnotes.
2. Transcribe the printed inputs exactly, retaining signs, units, slash denominators and header-versus-row distinctions.
3. Reproduce the comparison and calculation above under its stated rule and tolerance; then test the source-grounded alternatives without assigning an unstated denominator or estimator.
4. Resolve the specific question: Both printed fractions and footnotes are available. Missing: whether the two categories share one observed surgical-approach variable and, if so, its common denominator. For the H arm, are abdominal and nonabdominal entries categories of one mutually exclusive variable; if so, which common denominator applies, and if not, what explains the separate denominators?
5. Record the human decision in the blank fields below; the suggested review disposition is a mechanical pre-fill, not an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — complementary surgical-approach rows switch denominators — L arm

Pending Human Adjudication.

**Candidate statement:** The L-arm abdominal and nonabdominal rows use denominators 987 and 986 although their counts sum to 986. A discrepancy depends on the rows being one complementary classification.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** Table 1 Surgical approach, Type of abdominal incision and Nonabdominal L cells; footnotes a and i (p. 6). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 6](<../jama_bluth_2019_oi_190055_16092.pdf#page=6>)

**Source evidence:** L: abdominal 884/987, nonabdominal 102/986. Footnote a permits characteristics not assessed in all patients; i defines abdominal open and endoscopic categories.

**Reported-versus-comparator:** The same arm's two printed denominators 987 and 986 and complementary-labelled category sum. A single mutually exclusive/exhaustive abdominal-versus-nonabdominal classification has one observed denominator. Applicability is conditional on these rows being one classification, rather than independently missing binary indicators.

**Reasoning procedure:** Read the printed components at the linked source locations, distinguish observed values from conditional calculations, and apply the comparison rule above. Exact integer counts and population labels have zero arithmetic tolerance; the applicability of a shared population is considered separately.

**Calculation:** 884 + 102 = 986; printed denominators differ by one (987 versus 986). The sum equals 986 and differs from 987 by one.

**Alternative source-grounded interpretations:** Footnote a allows missingness; independent category-specific indicators could have distinct observed denominators. It does not expressly define such separate indicators. A denominator transposition is an inferred explanation, not established. Direct: numerator/denominator cells, category labels and footnotes. Conditional derivation: one shared classification denominator. Inferred: transposed denominators or differently missing indicators.

**Mechanical evidence recheck:** The source reproduces the denominator switch and count sum; the same-classification question remains as registered pending its named definition. Evidence state recorded_candidate. This field reports the completed source recheck; it is not human adjudication.

**Quality-control relevance:** This candidate identifies a reproducible numeric, denominator, display or measure-label comparison within the supplied REPORT. Small preventable reporting defects can matter for downstream evidence extraction; the named population, estimand or display questions bound this observation.

**Potential downstream evidence impact:** An extractor preparing a systematic review or meta-analysis could copy L surgical-approach denominators 987 and 986 without knowing whether the two categories share one observed population. If human review confirms a reporting defect, documenting its definition or correction could improve extraction consistency. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:**

1. Open the linked physical PDF page(s) and inspect the named row, heading, reference population and applicable footnotes.
2. Transcribe the printed inputs exactly, retaining signs, units, slash denominators and header-versus-row distinctions.
3. Reproduce the comparison and calculation above under its stated rule and tolerance; then test the source-grounded alternatives without assigning an unstated denominator or estimator.
4. Resolve the specific question: Both printed fractions and footnotes are available. Missing: whether the two categories share one observed surgical-approach variable and, if so, its common denominator. For the L arm, are abdominal and nonabdominal entries categories of one mutually exclusive variable; if so, which common denominator applies, and if not, what explains the separate denominators?
5. Record the human decision in the blank fields below; the suggested review disposition is a mechanical pre-fill, not an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Reflux,n/N(%), high group

Pending Human Adjudication.

**Candidate statement:** The H-arm reflux percentage 33.6% does not follow nearest one-decimal rounding of the explicit fraction 332/986; truncation reproduces the display.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** Table 1 Gastroesophageal reflux, H cell (p. 5). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 5](<../jama_bluth_2019_oi_190055_16092.pdf#page=5>)

**Source evidence:** H cell 332/986 (33.6%); the row prints No./total No. (%) or inherits that explicit parent label.

**Reported-versus-comparator:** Printed percentage 33.6% versus the same cell's exact fraction 332/986. Percentage identity 100 × printed numerator / printed denominator, followed by nearest one-decimal rounding (±0.05 percentage point). This tests the displayed n/N (%) cell; the actual production/display rule is not explicitly stated.

**Reasoning procedure:** Read the printed components at the linked source locations, distinguish observed values from conditional calculations, and apply the comparison rule above. Nearest one-decimal display tolerance is ±0.05 percentage point; applicability depends on the stated fraction/population and display rule. Truncation is evaluated separately.

**Calculation:** 100 × 332/986 = 33.671399594%; nearest one-decimal = 33.7%; printed = 33.6%; absolute gap = 0.071399594 percentage point. One-decimal truncation gives 33.6%, reproducing this display.

**Alternative source-grounded interpretations:** The actual display might truncate rather than round, or the percentage might use a different population. Other explicit n/N rows round upward (for example reflux low 343/986 →34.8%), so a universal truncation convention is not supplied. Printed denominator/numerator reuse remains an inferred mechanism. Direct: all three components of the cell. Derived: division and nearest-rounding gap. Inferred: production/transcription cause; none is established.

**Mechanical evidence recheck:** The exact printed n/N and percentage match the registration; the nearest-rounding mismatch reproduces and remains conditional on the named display rule. Evidence state recorded_candidate. This field reports the completed source recheck; it is not human adjudication.

**Quality-control relevance:** This candidate identifies a reproducible numeric, denominator, display or measure-label comparison within the supplied REPORT. Small preventable reporting defects can matter for downstream evidence extraction; the named population, estimand or display questions bound this observation.

**Potential downstream evidence impact:** An extractor preparing a systematic review or meta-analysis could copy the H reflux percentage 33.6% together with a fraction that gives 33.671399594%. If human review confirms a reporting defect, documenting its definition or correction could improve extraction consistency. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:**

1. Open the linked physical PDF page(s) and inspect the named row, heading, reference population and applicable footnotes.
2. Transcribe the printed inputs exactly, retaining signs, units, slash denominators and header-versus-row distinctions.
3. Reproduce the comparison and calculation above under its stated rule and tolerance; then test the source-grounded alternatives without assigning an unstated denominator or estimator.
4. Resolve the specific question: Necessary fraction and printed percentage are available. Missing: actual rounding/truncation rule and whether any printed component uses a different population; no alternative denominator is assigned. What exact observed denominator and display rule generated the H-group Gastroesophageal reflux percentage 33.6%, and which count/population definition should be used for extraction?
5. Record the human decision in the blank fields below; the suggested review disposition is a mechanical pre-fill, not an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Diabetes,n/N(%), high group

Pending Human Adjudication.

**Candidate statement:** The H-arm diabetes percentage 29.7% does not follow nearest one-decimal rounding of 294/988; truncation reproduces the display.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** Table 1 Diabetes, H cell (p. 5). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 5](<../jama_bluth_2019_oi_190055_16092.pdf#page=5>)

**Source evidence:** H cell 294/988 (29.7%); the row prints No./total No. (%) or inherits that explicit parent label.

**Reported-versus-comparator:** Printed percentage 29.7% versus the same cell's exact fraction 294/988. Percentage identity 100 × printed numerator / printed denominator, followed by nearest one-decimal rounding (±0.05 percentage point). This tests the displayed n/N (%) cell; the actual production/display rule is not explicitly stated.

**Reasoning procedure:** Read the printed components at the linked source locations, distinguish observed values from conditional calculations, and apply the comparison rule above. Nearest one-decimal display tolerance is ±0.05 percentage point; applicability depends on the stated fraction/population and display rule. Truncation is evaluated separately.

**Calculation:** 100 × 294/988 = 29.757085020%; nearest one-decimal = 29.8%; printed = 29.7%; absolute gap = 0.057085020 percentage point. One-decimal truncation gives 29.7%, reproducing this display.

**Alternative source-grounded interpretations:** The actual display might truncate rather than round, or the percentage might use a different population. Other explicit n/N rows round upward (for example reflux low 343/986 →34.8%), so a universal truncation convention is not supplied. Printed denominator/numerator reuse remains an inferred mechanism. Direct: all three components of the cell. Derived: division and nearest-rounding gap. Inferred: production/transcription cause; none is established.

**Mechanical evidence recheck:** The exact printed n/N and percentage match the registration; the nearest-rounding mismatch reproduces and remains conditional on the named display rule. Evidence state recorded_candidate. This field reports the completed source recheck; it is not human adjudication.

**Quality-control relevance:** This candidate identifies a reproducible numeric, denominator, display or measure-label comparison within the supplied REPORT. Small preventable reporting defects can matter for downstream evidence extraction; the named population, estimand or display questions bound this observation.

**Potential downstream evidence impact:** An extractor preparing a systematic review or meta-analysis could copy the H diabetes percentage 29.7% with the explicit fraction 294/988. If human review confirms a reporting defect, documenting its definition or correction could improve extraction consistency. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:**

1. Open the linked physical PDF page(s) and inspect the named row, heading, reference population and applicable footnotes.
2. Transcribe the printed inputs exactly, retaining signs, units, slash denominators and header-versus-row distinctions.
3. Reproduce the comparison and calculation above under its stated rule and tolerance; then test the source-grounded alternatives without assigning an unstated denominator or estimator.
4. Resolve the specific question: Necessary fraction and printed percentage are available. Missing: actual rounding/truncation rule and whether any printed component uses a different population; no alternative denominator is assigned. What exact observed denominator and display rule generated the H-group Diabetes percentage 29.7%, and which count/population definition should be used for extraction?
5. Record the human decision in the blank fields below; the suggested review disposition is a mechanical pre-fill, not an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Diabetes oral medication,n/N(%), high group

Pending Human Adjudication.

**Candidate statement:** The H-arm oral-medication percentage 71.0% does not follow nearest one-decimal rounding of 209/294; truncation reproduces the display.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** Table 1 Diabetes — Take oral medication, H cell (p. 5). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 5](<../jama_bluth_2019_oi_190055_16092.pdf#page=5>)

**Source evidence:** H cell 209/294 (71.0%); the row prints No./total No. (%) or inherits that explicit parent label.

**Reported-versus-comparator:** Printed percentage 71.0% versus the same cell's exact fraction 209/294. Percentage identity 100 × printed numerator / printed denominator, followed by nearest one-decimal rounding (±0.05 percentage point). This tests the displayed n/N (%) cell; the actual production/display rule is not explicitly stated.

**Reasoning procedure:** Read the printed components at the linked source locations, distinguish observed values from conditional calculations, and apply the comparison rule above. Nearest one-decimal display tolerance is ±0.05 percentage point; applicability depends on the stated fraction/population and display rule. Truncation is evaluated separately.

**Calculation:** 100 × 209/294 = 71.088435374%; nearest one-decimal = 71.1%; printed = 71.0%; absolute gap = 0.088435374 percentage point. One-decimal truncation gives 71.0%, reproducing this display.

**Alternative source-grounded interpretations:** The actual display might truncate rather than round, or the percentage might use a different population. Other explicit n/N rows round upward (for example reflux low 343/986 →34.8%), so a universal truncation convention is not supplied. Printed denominator/numerator reuse remains an inferred mechanism. Direct: all three components of the cell. Derived: division and nearest-rounding gap. Inferred: production/transcription cause; none is established.

**Mechanical evidence recheck:** The exact printed n/N and percentage match the registration; the nearest-rounding mismatch reproduces and remains conditional on the named display rule. Evidence state recorded_candidate. This field reports the completed source recheck; it is not human adjudication.

**Quality-control relevance:** This candidate identifies a reproducible numeric, denominator, display or measure-label comparison within the supplied REPORT. Small preventable reporting defects can matter for downstream evidence extraction; the named population, estimand or display questions bound this observation.

**Potential downstream evidence impact:** An extractor preparing a systematic review or meta-analysis could copy the nested H oral-medication percentage 71.0% with the explicit fraction 209/294. If human review confirms a reporting defect, documenting its definition or correction could improve extraction consistency. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:**

1. Open the linked physical PDF page(s) and inspect the named row, heading, reference population and applicable footnotes.
2. Transcribe the printed inputs exactly, retaining signs, units, slash denominators and header-versus-row distinctions.
3. Reproduce the comparison and calculation above under its stated rule and tolerance; then test the source-grounded alternatives without assigning an unstated denominator or estimator.
4. Resolve the specific question: Necessary fraction and printed percentage are available. Missing: actual rounding/truncation rule and whether any printed component uses a different population; no alternative denominator is assigned. What exact observed denominator and display rule generated the H-group Diabetes — Take oral medication percentage 71.0%, and which count/population definition should be used for extraction?
5. Record the human decision in the blank fields below; the suggested review disposition is a mechanical pre-fill, not an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — Obstructive-sleep-apnea header-denominator input error

Pending Human Adjudication.

**Candidate statement:** The registered comparison contains a record_input_error: it treated header n=987 as the exact observed denominator for 264 (26.8%) low-group obstructive-sleep-apnea cases. The source permits missing characteristics and does not supply that row denominator; a percentage contradiction is not established.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** statistical_results

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** The registration assigned the group header as an exact row denominator despite source footnote a's missingness qualification; the residual percentage issue cannot be settled without the observed denominator.

**Exact source locations:** Table 1 Obstructive sleep apnea, L cell (p. 5); low-group n=987 header (p. 5) and missing-characteristics footnote a (p. 6). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 5](<../jama_bluth_2019_oi_190055_16092.pdf#page=5>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 6](<../jama_bluth_2019_oi_190055_16092.pdf#page=6>)

**Source evidence:** L cell 264 (26.8%); 987 is the group header, not an explicit cell denominator. Footnote a says some characteristics were not assessed in all patients.

**Reported-versus-comparator:** The registered comparator uses header n=987 as though it were the row's exact observed denominator. That alignment is not supplied. 100 × n/N is applicable only after the variable's observed denominator N is established. Header population cannot silently replace a variable denominator when the table explicitly permits missingness.

**Reasoning procedure:** Read the printed components at the linked source locations, distinguish observed values from conditional calculations, and apply the comparison rule above. Nearest one-decimal display tolerance is ±0.05 percentage point; applicability depends on the stated fraction/population and display rule. Truncation is evaluated separately.

**Calculation:** 100 × 264/987 = 26.747720365%; nearest one-decimal = 26.7%; printed = 26.8%; absolute gap = 0.052279635 percentage point. This reproduces only the header-denominator diagnostic, not a confirmed row-denominator contradiction. 100 × 264/986 = 26.774847870%, which rounds to 26.8%.

**Alternative source-grounded interpretations:** A variable-specific denominator of 986 is arithmetically compatible with the display and with footnote a's missingness allowance, but the source does not assert 986 for this row. Direct: 264 (26.8), header 987 and missingness footnote. Inferred: treating 987 as this variable's observed denominator; the alternative 986 is a diagnostic, not a source count.

**Mechanical evidence recheck:** The registration assigned the group header as an exact row denominator despite source footnote a's missingness qualification; the residual percentage issue cannot be settled without the observed denominator. Evidence state record_input_error. This field reports the completed source recheck; it is not human adjudication.

**Quality-control relevance:** The quality-control issue is the unsupported input alignment in the registered comparison. Retaining the stable ID and its record_input_error state prevents a conditional diagnostic from being presented as a confirmed source contradiction.

**Potential downstream evidence impact:** An extractor preparing a systematic review or meta-analysis could copy an unsupported obstructive-sleep-apnea denominator 987 reconstructed from the group header. If human review confirms a reporting defect, documenting its definition or correction could improve extraction consistency. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:**

1. Open the linked physical PDF page(s) and inspect the named row, heading, reference population and applicable footnotes.
2. Transcribe the printed inputs exactly, retaining signs, units, slash denominators and header-versus-row distinctions.
3. Reproduce the comparison and calculation above under its stated rule and tolerance; then test the source-grounded alternatives without assigning an unstated denominator or estimator.
4. Resolve the specific question: Missing: exact observed denominator for obstructive sleep apnea and actual display rule. The source provides the count and overall group population, not that row denominator. What exact observed denominator and display rule generated the L-group Obstructive sleep apnea percentage 26.8%, and which count/population definition should be used for extraction?
5. Record the human decision in the blank fields below; the suggested review disposition is a mechanical pre-fill, not an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C009 — Tobacco never,n/N(%), high group

Pending Human Adjudication.

**Candidate statement:** The H-arm never-tobacco cell 549/987 (55.5%) does not reconcile under nearest one-decimal rounding or simple truncation of its explicit fraction.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** Table 1 Tobacco use — Never, H cell (p. 5). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 5](<../jama_bluth_2019_oi_190055_16092.pdf#page=5>)

**Source evidence:** H cell 549/987 (55.5%); the row prints No./total No. (%) or inherits that explicit parent label.

**Reported-versus-comparator:** Printed percentage 55.5% versus the same cell's exact fraction 549/987. Percentage identity 100 × printed numerator / printed denominator, followed by nearest one-decimal rounding (±0.05 percentage point). This tests the displayed n/N (%) cell; the actual production/display rule is not explicitly stated.

**Reasoning procedure:** Read the printed components at the linked source locations, distinguish observed values from conditional calculations, and apply the comparison rule above. Nearest one-decimal display tolerance is ±0.05 percentage point; applicability depends on the stated fraction/population and display rule. Truncation is evaluated separately.

**Calculation:** 100 × 549/987 = 55.623100304%; nearest one-decimal = 55.6%; printed = 55.5%; absolute gap = 0.123100304 percentage point. One-decimal truncation gives 55.6%, and does not reproduce this display.

**Alternative source-grounded interpretations:** Simple one-decimal truncation does not reproduce this cell, as shown above. A different percentage population or another display procedure would need to be identified. Other explicit n/N rows round upward (for example reflux low 343/986 →34.8%), so a universal truncation convention is not supplied. Printed denominator/numerator reuse remains an inferred mechanism. Direct: all three components of the cell. Derived: division and nearest-rounding gap. Inferred: production/transcription cause; none is established.

**Mechanical evidence recheck:** The exact printed n/N and percentage match the registration; the nearest-rounding mismatch reproduces and remains conditional on the named display rule. Evidence state recorded_candidate. This field reports the completed source recheck; it is not human adjudication.

**Quality-control relevance:** This candidate identifies a reproducible numeric, denominator, display or measure-label comparison within the supplied REPORT. Small preventable reporting defects can matter for downstream evidence extraction; the named population, estimand or display questions bound this observation.

**Potential downstream evidence impact:** An extractor preparing a systematic review or meta-analysis could copy the H never-tobacco percentage 55.5% with the explicit fraction 549/987. If human review confirms a reporting defect, documenting its definition or correction could improve extraction consistency. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:**

1. Open the linked physical PDF page(s) and inspect the named row, heading, reference population and applicable footnotes.
2. Transcribe the printed inputs exactly, retaining signs, units, slash denominators and header-versus-row distinctions.
3. Reproduce the comparison and calculation above under its stated rule and tolerance; then test the source-grounded alternatives without assigning an unstated denominator or estimator.
4. Resolve the specific question: Necessary fraction and printed percentage are available. Missing: actual rounding/truncation rule and whether any printed component uses a different population; no alternative denominator is assigned. What exact observed denominator and display rule generated the H-group Tobacco use — Never percentage 55.5%, and which count/population definition should be used for extraction?
5. Record the human decision in the blank fields below; the suggested review disposition is a mechanical pre-fill, not an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C010 — Tobacco never,n/N(%), low group

Pending Human Adjudication.

**Candidate statement:** The L-arm never-tobacco percentage 53.2% does not follow nearest one-decimal rounding of 525/985; truncation reproduces the display.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** Table 1 Tobacco use — Never, L cell (p. 5). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 5](<../jama_bluth_2019_oi_190055_16092.pdf#page=5>)

**Source evidence:** L cell 525/985 (53.2%); the row prints No./total No. (%) or inherits that explicit parent label.

**Reported-versus-comparator:** Printed percentage 53.2% versus the same cell's exact fraction 525/985. Percentage identity 100 × printed numerator / printed denominator, followed by nearest one-decimal rounding (±0.05 percentage point). This tests the displayed n/N (%) cell; the actual production/display rule is not explicitly stated.

**Reasoning procedure:** Read the printed components at the linked source locations, distinguish observed values from conditional calculations, and apply the comparison rule above. Nearest one-decimal display tolerance is ±0.05 percentage point; applicability depends on the stated fraction/population and display rule. Truncation is evaluated separately.

**Calculation:** 100 × 525/985 = 53.299492386%; nearest one-decimal = 53.3%; printed = 53.2%; absolute gap = 0.099492386 percentage point. One-decimal truncation gives 53.2%, reproducing this display.

**Alternative source-grounded interpretations:** The actual display might truncate rather than round, or the percentage might use a different population. Other explicit n/N rows round upward (for example reflux low 343/986 →34.8%), so a universal truncation convention is not supplied. Printed denominator/numerator reuse remains an inferred mechanism. Direct: all three components of the cell. Derived: division and nearest-rounding gap. Inferred: production/transcription cause; none is established.

**Mechanical evidence recheck:** The exact printed n/N and percentage match the registration; the nearest-rounding mismatch reproduces and remains conditional on the named display rule. Evidence state recorded_candidate. This field reports the completed source recheck; it is not human adjudication.

**Quality-control relevance:** This candidate identifies a reproducible numeric, denominator, display or measure-label comparison within the supplied REPORT. Small preventable reporting defects can matter for downstream evidence extraction; the named population, estimand or display questions bound this observation.

**Potential downstream evidence impact:** An extractor preparing a systematic review or meta-analysis could copy the L never-tobacco percentage 53.2% with the explicit fraction 525/985. If human review confirms a reporting defect, documenting its definition or correction could improve extraction consistency. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:**

1. Open the linked physical PDF page(s) and inspect the named row, heading, reference population and applicable footnotes.
2. Transcribe the printed inputs exactly, retaining signs, units, slash denominators and header-versus-row distinctions.
3. Reproduce the comparison and calculation above under its stated rule and tolerance; then test the source-grounded alternatives without assigning an unstated denominator or estimator.
4. Resolve the specific question: Necessary fraction and printed percentage are available. Missing: actual rounding/truncation rule and whether any printed component uses a different population; no alternative denominator is assigned. What exact observed denominator and display rule generated the L-group Tobacco use — Never percentage 53.2%, and which count/population definition should be used for extraction?
5. Record the human decision in the blank fields below; the suggested review disposition is a mechanical pre-fill, not an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C011 — Tobacco previous,n/N(%), high group

Pending Human Adjudication.

**Candidate statement:** The H-arm previous-tobacco percentage 27.6% does not follow nearest one-decimal rounding of 273/987; truncation reproduces the display.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** Table 1 Tobacco use — Previous, H cell (p. 5). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 5](<../jama_bluth_2019_oi_190055_16092.pdf#page=5>)

**Source evidence:** H cell 273/987 (27.6%); the row prints No./total No. (%) or inherits that explicit parent label.

**Reported-versus-comparator:** Printed percentage 27.6% versus the same cell's exact fraction 273/987. Percentage identity 100 × printed numerator / printed denominator, followed by nearest one-decimal rounding (±0.05 percentage point). This tests the displayed n/N (%) cell; the actual production/display rule is not explicitly stated.

**Reasoning procedure:** Read the printed components at the linked source locations, distinguish observed values from conditional calculations, and apply the comparison rule above. Nearest one-decimal display tolerance is ±0.05 percentage point; applicability depends on the stated fraction/population and display rule. Truncation is evaluated separately.

**Calculation:** 100 × 273/987 = 27.659574468%; nearest one-decimal = 27.7%; printed = 27.6%; absolute gap = 0.059574468 percentage point. One-decimal truncation gives 27.6%, reproducing this display.

**Alternative source-grounded interpretations:** The actual display might truncate rather than round, or the percentage might use a different population. Other explicit n/N rows round upward (for example reflux low 343/986 →34.8%), so a universal truncation convention is not supplied. Printed denominator/numerator reuse remains an inferred mechanism. Direct: all three components of the cell. Derived: division and nearest-rounding gap. Inferred: production/transcription cause; none is established.

**Mechanical evidence recheck:** The exact printed n/N and percentage match the registration; the nearest-rounding mismatch reproduces and remains conditional on the named display rule. Evidence state recorded_candidate. This field reports the completed source recheck; it is not human adjudication.

**Quality-control relevance:** This candidate identifies a reproducible numeric, denominator, display or measure-label comparison within the supplied REPORT. Small preventable reporting defects can matter for downstream evidence extraction; the named population, estimand or display questions bound this observation.

**Potential downstream evidence impact:** An extractor preparing a systematic review or meta-analysis could copy the H previous-tobacco percentage 27.6% with the explicit fraction 273/987. If human review confirms a reporting defect, documenting its definition or correction could improve extraction consistency. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:**

1. Open the linked physical PDF page(s) and inspect the named row, heading, reference population and applicable footnotes.
2. Transcribe the printed inputs exactly, retaining signs, units, slash denominators and header-versus-row distinctions.
3. Reproduce the comparison and calculation above under its stated rule and tolerance; then test the source-grounded alternatives without assigning an unstated denominator or estimator.
4. Resolve the specific question: Necessary fraction and printed percentage are available. Missing: actual rounding/truncation rule and whether any printed component uses a different population; no alternative denominator is assigned. What exact observed denominator and display rule generated the H-group Tobacco use — Previous percentage 27.6%, and which count/population definition should be used for extraction?
5. Record the human decision in the blank fields below; the suggested review disposition is a mechanical pre-fill, not an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C012 — Tobacco current,n/N(%), low group

Pending Human Adjudication.

**Candidate statement:** The L-arm current-tobacco percentage 18.8% does not follow nearest one-decimal rounding of 186/985; truncation reproduces the display.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** Table 1 Tobacco use — Current, L cell (p. 5). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 5](<../jama_bluth_2019_oi_190055_16092.pdf#page=5>)

**Source evidence:** L cell 186/985 (18.8%); the row prints No./total No. (%) or inherits that explicit parent label.

**Reported-versus-comparator:** Printed percentage 18.8% versus the same cell's exact fraction 186/985. Percentage identity 100 × printed numerator / printed denominator, followed by nearest one-decimal rounding (±0.05 percentage point). This tests the displayed n/N (%) cell; the actual production/display rule is not explicitly stated.

**Reasoning procedure:** Read the printed components at the linked source locations, distinguish observed values from conditional calculations, and apply the comparison rule above. Nearest one-decimal display tolerance is ±0.05 percentage point; applicability depends on the stated fraction/population and display rule. Truncation is evaluated separately.

**Calculation:** 100 × 186/985 = 18.883248731%; nearest one-decimal = 18.9%; printed = 18.8%; absolute gap = 0.083248731 percentage point. One-decimal truncation gives 18.8%, reproducing this display.

**Alternative source-grounded interpretations:** The actual display might truncate rather than round, or the percentage might use a different population. Other explicit n/N rows round upward (for example reflux low 343/986 →34.8%), so a universal truncation convention is not supplied. Printed denominator/numerator reuse remains an inferred mechanism. Direct: all three components of the cell. Derived: division and nearest-rounding gap. Inferred: production/transcription cause; none is established.

**Mechanical evidence recheck:** The exact printed n/N and percentage match the registration; the nearest-rounding mismatch reproduces and remains conditional on the named display rule. Evidence state recorded_candidate. This field reports the completed source recheck; it is not human adjudication.

**Quality-control relevance:** This candidate identifies a reproducible numeric, denominator, display or measure-label comparison within the supplied REPORT. Small preventable reporting defects can matter for downstream evidence extraction; the named population, estimand or display questions bound this observation.

**Potential downstream evidence impact:** An extractor preparing a systematic review or meta-analysis could copy the L current-tobacco percentage 18.8% with the explicit fraction 186/985. If human review confirms a reporting defect, documenting its definition or correction could improve extraction consistency. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:**

1. Open the linked physical PDF page(s) and inspect the named row, heading, reference population and applicable footnotes.
2. Transcribe the printed inputs exactly, retaining signs, units, slash denominators and header-versus-row distinctions.
3. Reproduce the comparison and calculation above under its stated rule and tolerance; then test the source-grounded alternatives without assigning an unstated denominator or estimator.
4. Resolve the specific question: Necessary fraction and printed percentage are available. Missing: actual rounding/truncation rule and whether any printed component uses a different population; no alternative denominator is assigned. What exact observed denominator and display rule generated the L-group Tobacco use — Current percentage 18.8%, and which count/population definition should be used for extraction?
5. Record the human decision in the blank fields below; the suggested review disposition is a mechanical pre-fill, not an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C013 — Antibiotic prophylaxis,n/N(%), high group

Pending Human Adjudication.

**Candidate statement:** The H-arm antibiotic-prophylaxis cell 938/987 (94.8%) does not reconcile under nearest one-decimal rounding or simple truncation of its explicit fraction.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** Table 1 Antibiotic prophylaxis, H cell (p. 6). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 6](<../jama_bluth_2019_oi_190055_16092.pdf#page=6>)

**Source evidence:** H cell 938/987 (94.8%); the row prints No./total No. (%) or inherits that explicit parent label.

**Reported-versus-comparator:** Printed percentage 94.8% versus the same cell's exact fraction 938/987. Percentage identity 100 × printed numerator / printed denominator, followed by nearest one-decimal rounding (±0.05 percentage point). This tests the displayed n/N (%) cell; the actual production/display rule is not explicitly stated.

**Reasoning procedure:** Read the printed components at the linked source locations, distinguish observed values from conditional calculations, and apply the comparison rule above. Nearest one-decimal display tolerance is ±0.05 percentage point; applicability depends on the stated fraction/population and display rule. Truncation is evaluated separately.

**Calculation:** 100 × 938/987 = 95.035460993%; nearest one-decimal = 95.0%; printed = 94.8%; absolute gap = 0.235460993 percentage point. One-decimal truncation gives 95.0%, and does not reproduce this display.

**Alternative source-grounded interpretations:** Simple one-decimal truncation does not reproduce this cell, as shown above. A different percentage population or another display procedure would need to be identified. Other explicit n/N rows round upward (for example reflux low 343/986 →34.8%), so a universal truncation convention is not supplied. Printed denominator/numerator reuse remains an inferred mechanism. Direct: all three components of the cell. Derived: division and nearest-rounding gap. Inferred: production/transcription cause; none is established.

**Mechanical evidence recheck:** The exact printed n/N and percentage match the registration; the nearest-rounding mismatch reproduces and remains conditional on the named display rule. Evidence state recorded_candidate. This field reports the completed source recheck; it is not human adjudication.

**Quality-control relevance:** This candidate identifies a reproducible numeric, denominator, display or measure-label comparison within the supplied REPORT. Small preventable reporting defects can matter for downstream evidence extraction; the named population, estimand or display questions bound this observation.

**Potential downstream evidence impact:** An extractor preparing a systematic review or meta-analysis could copy the H antibiotic-prophylaxis percentage 94.8% with the explicit fraction 938/987. If human review confirms a reporting defect, documenting its definition or correction could improve extraction consistency. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:**

1. Open the linked physical PDF page(s) and inspect the named row, heading, reference population and applicable footnotes.
2. Transcribe the printed inputs exactly, retaining signs, units, slash denominators and header-versus-row distinctions.
3. Reproduce the comparison and calculation above under its stated rule and tolerance; then test the source-grounded alternatives without assigning an unstated denominator or estimator.
4. Resolve the specific question: Necessary fraction and printed percentage are available. Missing: actual rounding/truncation rule and whether any printed component uses a different population; no alternative denominator is assigned. What exact observed denominator and display rule generated the H-group Antibiotic prophylaxis percentage 94.8%, and which count/population definition should be used for extraction?
5. Record the human decision in the blank fields below; the suggested review disposition is a mechanical pre-fill, not an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C014 — Antibiotic prophylaxis,n/N(%), low group

Pending Human Adjudication.

**Candidate statement:** The L-arm antibiotic-prophylaxis cell 949/985 (96.1%) does not reconcile under nearest one-decimal rounding or simple truncation of its explicit fraction.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** Table 1 Antibiotic prophylaxis, L cell (p. 6). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 6](<../jama_bluth_2019_oi_190055_16092.pdf#page=6>)

**Source evidence:** L cell 949/985 (96.1%); the row prints No./total No. (%) or inherits that explicit parent label.

**Reported-versus-comparator:** Printed percentage 96.1% versus the same cell's exact fraction 949/985. Percentage identity 100 × printed numerator / printed denominator, followed by nearest one-decimal rounding (±0.05 percentage point). This tests the displayed n/N (%) cell; the actual production/display rule is not explicitly stated.

**Reasoning procedure:** Read the printed components at the linked source locations, distinguish observed values from conditional calculations, and apply the comparison rule above. Nearest one-decimal display tolerance is ±0.05 percentage point; applicability depends on the stated fraction/population and display rule. Truncation is evaluated separately.

**Calculation:** 100 × 949/985 = 96.345177665%; nearest one-decimal = 96.3%; printed = 96.1%; absolute gap = 0.245177665 percentage point. One-decimal truncation gives 96.3%, and does not reproduce this display.

**Alternative source-grounded interpretations:** Simple one-decimal truncation does not reproduce this cell, as shown above. A different percentage population or another display procedure would need to be identified. Other explicit n/N rows round upward (for example reflux low 343/986 →34.8%), so a universal truncation convention is not supplied. Printed denominator/numerator reuse remains an inferred mechanism. Direct: all three components of the cell. Derived: division and nearest-rounding gap. Inferred: production/transcription cause; none is established.

**Mechanical evidence recheck:** The exact printed n/N and percentage match the registration; the nearest-rounding mismatch reproduces and remains conditional on the named display rule. Evidence state recorded_candidate. This field reports the completed source recheck; it is not human adjudication.

**Quality-control relevance:** This candidate identifies a reproducible numeric, denominator, display or measure-label comparison within the supplied REPORT. Small preventable reporting defects can matter for downstream evidence extraction; the named population, estimand or display questions bound this observation.

**Potential downstream evidence impact:** An extractor preparing a systematic review or meta-analysis could copy the L antibiotic-prophylaxis percentage 96.1% with the explicit fraction 949/985. If human review confirms a reporting defect, documenting its definition or correction could improve extraction consistency. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:**

1. Open the linked physical PDF page(s) and inspect the named row, heading, reference population and applicable footnotes.
2. Transcribe the printed inputs exactly, retaining signs, units, slash denominators and header-versus-row distinctions.
3. Reproduce the comparison and calculation above under its stated rule and tolerance; then test the source-grounded alternatives without assigning an unstated denominator or estimator.
4. Resolve the specific question: Necessary fraction and printed percentage are available. Missing: actual rounding/truncation rule and whether any printed component uses a different population; no alternative denominator is assigned. What exact observed denominator and display rule generated the L-group Antibiotic prophylaxis percentage 96.1%, and which count/population definition should be used for extraction?
5. Record the human decision in the blank fields below; the suggested review disposition is a mechanical pre-fill, not an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C015 — Monitoring displayed percentages versus absolute difference

Pending Human Adjudication.

**Candidate statement:** The monitoring percentages 64.9% and 67.7% subtract to −2.8 percentage points, whereas the reported difference is −1.8. Their population and estimand alignment requires clarification; the explicit fractions instead reproduce −1.8.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** Table 2 Monitoring of neuromuscular function row, percentages and Absolute Difference column (p. 8); neighboring Neuromuscular blockade row and footnote d as context. [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../jama_bluth_2019_oi_190055_16092.pdf#page=8>)

**Source evidence:** H 632/982 (64.9%); L 651/984 (67.7%); absolute difference -1.8 (−6.0 to 2.4), P=.40. Parent blockade counts H974/L961.

**Reported-versus-comparator:** Registered comparator: subtraction of the PRINTED percentages 64.9−67.7 versus reported absolute difference -1.8. For the same reported proportions and H-minus-L contrast, the absolute difference should agree with percentage subtraction within 0.15 percentage point joint rounding tolerance. Different populations/estimands can break the identity and must be named.

**Reasoning procedure:** Read the printed components at the linked source locations, distinguish observed values from conditional calculations, and apply the comparison rule above. Joint tolerance is 0.15 percentage point when two percentages and their difference are each displayed to one decimal under nearest rounding.

**Calculation:** 64.9 − 67.7 = -2.8 percentage points; printed difference -1.8; gap 1.0 percentage points. Exact printed fractions give 100 × (632/982 − 651/984) = -1.800084 percentage points. Parent-population percentages 100 × 632/974 = 64.887064% and 100 × 651/961 = 67.741935% round to the attached percentages. The exact fraction difference rounds to −1.8.

**Alternative source-grounded interpretations:** The percentages can use the blockade population while the fraction/difference uses another evaluable population. Neighboring counts support that arithmetic explanation, but source footnote d defines included monitoring methods only and does not define the denominator mapping. Direct: the same-row percentages, fractions, signed difference and parent counts. Derived: subtraction/division. Inferred: parent-denominator reuse or mixed populations; no production mechanism is asserted.

**Mechanical evidence recheck:** The registered PRINTED-percentage subtraction comparator reproduces beyond joint display tolerance; the required common-population definition remains unresolved. Evidence state recorded_candidate. This field reports the completed source recheck; it is not human adjudication.

**Quality-control relevance:** This candidate identifies a reproducible numeric, denominator, display or measure-label comparison within the supplied REPORT. Small preventable reporting defects can matter for downstream evidence extraction; the named population, estimand or display questions bound this observation.

**Potential downstream evidence impact:** An extractor preparing a systematic review or meta-analysis could copy monitoring percentages 64.9%/67.7% and difference −1.8 as though all three summarize the same population. If human review confirms a reporting defect, documenting its definition or correction could improve extraction consistency. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:**

1. Open the linked physical PDF page(s) and inspect the named row, heading, reference population and applicable footnotes.
2. Transcribe the printed inputs exactly, retaining signs, units, slash denominators and header-versus-row distinctions.
3. Reproduce the comparison and calculation above under its stated rule and tolerance; then test the source-grounded alternatives without assigning an unstated denominator or estimator.
4. Resolve the specific question: Percentages, printed n/N, difference and neighboring counts are available. Missing: whether percentages and absolute difference use the same population/estimand; actual display rule and denominators for inference. For monitoring, which population and estimand define each displayed percentage and the absolute difference/CI/P, and are those quantities intended to be directly comparable?
5. Record the human decision in the blank fields below; the suggested review disposition is a mechanical pre-fill, not an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C016 — Reversal displayed percentage direction versus absolute difference

Pending Human Adjudication.

**Candidate statement:** The reversal percentages 74.3% and 75.2% subtract to −0.9 percentage points, whereas the reported difference is +0.2. Their population and estimand alignment requires clarification. The exact slash fractions produce +0.251478, nearest +0.3; +0.2 is compatible with truncation.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** Table 2 Reversal row, percentages and Absolute Difference column (p. 8); neighboring Neuromuscular blockade row and footnote d as context. [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../jama_bluth_2019_oi_190055_16092.pdf#page=8>)

**Source evidence:** H 724/982 (74.3%); L 723/984 (75.2%); absolute difference 0.2 (−3.6 to 4.1), P=.90. Parent blockade counts H974/L961.

**Reported-versus-comparator:** Registered comparator: subtraction of the PRINTED percentages 74.3−75.2 versus reported absolute difference 0.2. For the same reported proportions and H-minus-L contrast, the absolute difference should agree with percentage subtraction within 0.15 percentage point joint rounding tolerance. Different populations/estimands can break the identity and must be named.

**Reasoning procedure:** Read the printed components at the linked source locations, distinguish observed values from conditional calculations, and apply the comparison rule above. Joint tolerance is 0.15 percentage point when two percentages and their difference are each displayed to one decimal under nearest rounding.

**Calculation:** 74.3 − 75.2 = -0.9 percentage points; printed difference 0.2; gap 1.1 percentage points, with opposite signs. Exact printed fractions give 100 × (724/982 − 723/984) = 0.251478 percentage points. Parent-population percentages 100 × 724/974 = 74.332649% and 100 × 723/961 = 75.234131% round to the attached percentages. The exact fraction difference rounds to +0.3, so the registration's separate statement that it is compatible with +0.2 under nearest rounding is not reproduced; C025 owns that comparator. Truncation toward zero of +0.251477820 gives +0.2, a conditional alternative documented separately in C025.

**Alternative source-grounded interpretations:** The percentages can use the blockade population while the fraction/difference uses another evaluable population. Neighboring counts support that arithmetic explanation, but source footnote d defines included monitoring methods only and does not define the denominator mapping. Direct: the same-row percentages, fractions, signed difference and parent counts. Derived: subtraction/division. Inferred: parent-denominator reuse or mixed populations; no production mechanism is asserted.

**Mechanical evidence recheck:** The registered PRINTED-percentage subtraction comparator reproduces beyond joint display tolerance; the required common-population definition remains unresolved. Evidence state recorded_candidate. This field reports the completed source recheck; it is not human adjudication.

**Quality-control relevance:** This candidate identifies a reproducible numeric, denominator, display or measure-label comparison within the supplied REPORT. Small preventable reporting defects can matter for downstream evidence extraction; the named population, estimand or display questions bound this observation.

**Potential downstream evidence impact:** An extractor preparing a systematic review or meta-analysis could copy reversal percentages 74.3%/75.2% and positive difference +0.2 without documenting their different possible denominator mappings. If human review confirms a reporting defect, documenting its definition or correction could improve extraction consistency. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:**

1. Open the linked physical PDF page(s) and inspect the named row, heading, reference population and applicable footnotes.
2. Transcribe the printed inputs exactly, retaining signs, units, slash denominators and header-versus-row distinctions.
3. Reproduce the comparison and calculation above under its stated rule and tolerance; then test the source-grounded alternatives without assigning an unstated denominator or estimator.
4. Resolve the specific question: Percentages, printed n/N, difference and neighboring counts are available. Missing: whether percentages and absolute difference use the same population/estimand; actual display rule and denominators for inference. For reversal, which population and estimand define each displayed percentage and the absolute difference/CI/P, and are those quantities intended to be directly comparable?
5. Record the human decision in the blank fields below; the suggested review disposition is a mechanical pre-fill, not an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C017 — Any recruitment,No.(%): absolute difference versus exact printed risks

Pending Human Adjudication.

**Candidate statement:** Recruitment difference 97.1 does not follow nearest one-decimal rounding of the count/header calculation, conditional on headers 989/987 being the row denominators and the effect being a raw risk difference. Truncation reconciles that calculation.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** Table 2 Received alveolar recruitment maneuvers row and H989/L987 headers (p. 7); any-recruitment definition footnote b (p. 8). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 7](<../jama_bluth_2019_oi_190055_16092.pdf#page=7>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../jama_bluth_2019_oi_190055_16092.pdf#page=8>)

**Source evidence:** H972 (98.3%), L11 (1.1%); headers H989/L987; difference97.1 (96.1 to98.2), P<.001.

**Reported-versus-comparator:** Reported absolute difference97.1 versus count/header-defined H-minus-L risk difference. Conditional identity of count/header-defined risk difference with the displayed difference under nearest one-decimal rounding. Group-header denominators and an unadjusted effect are required; actual computation/display convention is unnamed.

**Reasoning procedure:** Read the printed components at the linked source locations, distinguish observed values from conditional calculations, and apply the comparison rule above. Nearest one-decimal display tolerance is ±0.05 percentage point; applicability depends on the stated fraction/population and display rule. Truncation is evaluated separately.

**Calculation:** 100 × (972/989 − 11/987) = 97.166603664 percentage points, nearest97.2; printed97.1; gap 0.066603664 exceeds0.05. Subtracting already-rounded98.3−1.1=97.2 yields a0.1 gap, within the separate0.15 joint-rounding bound. Truncation of the exact calculation yields97.1.

**Alternative source-grounded interpretations:** Truncation reproduces97.1; a different complete-case denominator or effect estimator could also explain it. The displayed-count diagnostic does not determine which explanation applies. Direct: counts/header/difference and any-recruitment definition. Derived: exact arithmetic and rounding. Inferred: truncation or other computation; no fitted quantity is replaced.

**Mechanical evidence recheck:** The named count/header nearest-rounding comparator reproduces the small registered gap; the actual computation/display rule remains the registered missing definition. Evidence state recorded_candidate. This field reports the completed source recheck; it is not human adjudication.

**Quality-control relevance:** This candidate identifies a reproducible numeric, denominator, display or measure-label comparison within the supplied REPORT. Small preventable reporting defects can matter for downstream evidence extraction; the named population, estimand or display questions bound this observation.

**Potential downstream evidence impact:** An extractor preparing a systematic review or meta-analysis could copy recruitment difference 97.1 with assumed row denominators 989/987 and an assumed nearest-rounding rule. If human review confirms a reporting defect, documenting its definition or correction could improve extraction consistency. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:**

1. Open the linked physical PDF page(s) and inspect the named row, heading, reference population and applicable footnotes.
2. Transcribe the printed inputs exactly, retaining signs, units, slash denominators and header-versus-row distinctions.
3. Reproduce the comparison and calculation above under its stated rule and tolerance; then test the source-grounded alternatives without assigning an unstated denominator or estimator.
4. Resolve the specific question: Displayed counts, group headers and difference available. Missing: exact procedure-row analysis denominators, whether the effect is a raw risk difference, and its display rule. Was recruitment difference97.1 calculated from972/989 and11/987 then truncated, or from different denominators/estimand? Which computation/display rule defines this reported difference?
5. Record the human decision in the blank fields below; the suggested review disposition is a mechanical pre-fill, not an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C018 — Heat rate label versus beats-per-minute measurements

Pending Human Adjudication.

**Candidate statement:** The Table 2 heading “Heat rate” accompanies beats/min measurements, while the article defines bradycardia using “heart rate” in the same unit; the intended measure heading requires confirmation.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** Table 2 Heat rate heading and its three rows (p. 7); Table 3 bradycardia footnote k (p. 10). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 7](<../jama_bluth_2019_oi_190055_16092.pdf#page=7>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>)

**Source evidence:** Heading Heat rate, mean(SD), beats/min; H/L after intubation76.5(15.8)/76.0(14.3), first hour72.6(13.4)/73.1(14.0), last hour73.5(13.0)/74.9(13.8). Footnote k defines bradycardia as heart rate<50beats/min or relative decrease.

**Reported-versus-comparator:** Printed Heat rate spelling/unit versus the article's heart-rate definition in beats/min. Measurement-label/unit identity; the physiological rate indexed by beats/min and bradycardia is heart rate.

**Reasoning procedure:** Read the printed components at the linked source locations, distinguish observed values from conditional calculations, and apply the comparison rule above. This is an exact label/unit comparison, with no numeric rounding tolerance and no re-estimation.

**Calculation:** No numeric estimate is recomputed. The printed label lacks the r in Heart while accompanying beat/min measurements and bradycardia definition specify heart rate.

**Alternative source-grounded interpretations:** Readers can recover heart rate from the unit and context. A dropped letter is plausible but is an inferred explanation, not a separate numerical finding. Direct: Heat rate spelling, beats/min, numeric rows and heart rate wording in footnote k. Inferred: missing-letter mechanism.

**Mechanical evidence recheck:** Fresh text and current-source rendering confirm Heat rate in the heading; footnote k explicitly states heart rate with the same unit. Evidence state recorded_candidate. This field reports the completed source recheck; it is not human adjudication.

**Quality-control relevance:** This candidate identifies a reproducible numeric, denominator, display or measure-label comparison within the supplied REPORT. Small preventable reporting defects can matter for downstream evidence extraction; the named population, estimand or display questions bound this observation.

**Potential downstream evidence impact:** An extractor preparing a systematic review or meta-analysis could copy “Heat rate” as a variable label for the three beats/min rows. If human review confirms a reporting defect, documenting its definition or correction could improve extraction consistency. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:**

1. Open the linked physical PDF page(s) and inspect the named row, heading, reference population and applicable footnotes.
2. Transcribe the printed inputs exactly, retaining signs, units, slash denominators and header-versus-row distinctions.
3. Reproduce the comparison and calculation above under its stated rule and tolerance; then test the source-grounded alternatives without assigning an unstated denominator or estimator.
4. Resolve the specific question: All label/unit/definition inputs available. Author-intended heading is the remaining confirmation. Is Table 2 Heat rate intended as Heart rate, with all three rows indexed under that measure?
5. Record the human decision in the blank fields below; the suggested review disposition is a mechanical pre-fill, not an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C019 — Noninvasive ventilation,No.(%): L printed percentage identity

Pending Human Adjudication.

**Candidate statement:** The noninvasive-ventilation low cell prints 264 (26.8%), without a slash denominator. A nearest-rounding gap occurs only if header n=987 is the row denominator; the row-specific denominator and display rule are unreported.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** Table 2 Use of noninvasive ventilation, low cell and low-group header (p. 7); completed-analysis complete-case statement (p. 4) as context. [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 7](<../jama_bluth_2019_oi_190055_16092.pdf#page=7>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>)

**Source evidence:** Low cell264(26.8%); low-group header n987. The source does not print264/987 in the cell.

**Reported-versus-comparator:** 26.8% versus264/header987; the registered fraction is explicitly reconstructed using the header, as the original card says. Percentage identity using the displayed group header as the default reference, conditional on987 being the row denominator; nearest one-decimal rounding.

**Reasoning procedure:** Read the printed components at the linked source locations, distinguish observed values from conditional calculations, and apply the comparison rule above. Nearest one-decimal display tolerance is ±0.05 percentage point; applicability depends on the stated fraction/population and display rule. Truncation is evaluated separately.

**Calculation:** 100 ×264/987=26.747720365%, nearest26.7%; printed26.8; gap0.052279635 percentage point exceeds0.05 by0.002279635. At denominator986,100 ×264/986=26.774847870%, rounding26.8.

**Alternative source-grounded interpretations:** An unreported row denominator986 would reconcile nearest rounding. It is an arithmetic possibility, not a supplied observed denominator; no production method is inferred. Direct:264(26.8) and header987. Derived: header-denominator diagnostic. Inferred: row-specific986 or alternate display; neither is asserted as actual.

**Mechanical evidence recheck:** The source confirms264(26.8) and header987; the original record explicitly uses the header rather than claiming an explicit slash denominator. Its conditional header-denominator discrepancy reproduces and remains as registered pending the row denominator. No original transcription or location is disproven, so repaired_residual does not apply. Evidence state recorded_candidate. This field reports the completed source recheck; it is not human adjudication.

**Quality-control relevance:** This candidate identifies a reproducible numeric, denominator, display or measure-label comparison within the supplied REPORT. Small preventable reporting defects can matter for downstream evidence extraction; the named population, estimand or display questions bound this observation.

**Potential downstream evidence impact:** An extractor preparing a systematic review or meta-analysis could copy 26.8% and a reconstructed denominator 987 for the low-group noninvasive-ventilation row. If human review confirms a reporting defect, documenting its definition or correction could improve extraction consistency. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:**

1. Open the linked physical PDF page(s) and inspect the named row, heading, reference population and applicable footnotes.
2. Transcribe the printed inputs exactly, retaining signs, units, slash denominators and header-versus-row distinctions.
3. Reproduce the comparison and calculation above under its stated rule and tolerance; then test the source-grounded alternatives without assigning an unstated denominator or estimator.
4. Resolve the specific question: Count, percentage and header available. Missing: variable-specific complete-case denominator and rounding rule. Table 2 supplies no denominator override for this row; complete-case methods do not identify one. What exact denominator and display rule produced26.8% for264 noninvasive-ventilation users, and is the printed header987 intended as this row's reference population?
5. Record the human decision in the blank fields below; the suggested review disposition is a mechanical pre-fill, not an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C020 — Noninvasive ventilation,No.(%): absolute difference versus exact printed risks

Pending Human Adjudication.

**Candidate statement:** The noninvasive-ventilation difference 0.9 differs from nearest rounding of a count/header calculation, conditional on the headers being row denominators and the effect being a raw risk difference. Printed-percentage subtraction and truncation both reconcile 0.9.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** Table 2 Use of noninvasive ventilation row and headers (p. 7); complete-case analysis statement (p. 4). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 7](<../jama_bluth_2019_oi_190055_16092.pdf#page=7>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>)

**Source evidence:** H274(27.7%), L264(26.8%); headers989/987; difference0.9(−3.0 to4.9), P.64.

**Reported-versus-comparator:** 0.9 versus raw H-minus-L count/header-defined risk difference. Conditional raw risk-difference identity with nearest one-decimal display; group-header denominators and raw-difference estimator must apply.

**Reasoning procedure:** Read the printed components at the linked source locations, distinguish observed values from conditional calculations, and apply the comparison rule above. Nearest one-decimal display tolerance is ±0.05 percentage point; applicability depends on the stated fraction/population and display rule. Truncation is evaluated separately.

**Calculation:** 100 × (274/989−264/987)=0.957031910 percentage points; nearest1.0; printed0.9; gap0.057031910 exceeds0.05. Printed27.7−26.8=0.9 agrees exactly with the reported difference. Truncation of the exact count/header calculation yields0.9.

**Alternative source-grounded interpretations:** Subtraction of displayed percentages, truncation of raw risks, or another complete-case population could produce0.9. The printed-percentage subtraction is coherent and does not disprove the separate exact count/header rounding comparison. Direct: row counts, percentages, headers and signed difference. Derived: exact arithmetic. Inferred: display/analysis mechanism; none is assigned.

**Mechanical evidence recheck:** The registered exact count/header nearest-rounding gap reproduces; a different displayed-percentage comparator reconciles, and actual computation remains unspecified. Evidence state recorded_candidate. This field reports the completed source recheck; it is not human adjudication.

**Quality-control relevance:** This candidate identifies a reproducible numeric, denominator, display or measure-label comparison within the supplied REPORT. Small preventable reporting defects can matter for downstream evidence extraction; the named population, estimand or display questions bound this observation.

**Potential downstream evidence impact:** An extractor preparing a systematic review or meta-analysis could copy difference 0.9 as a raw count/header risk difference without preserving its unresolved denominator and display convention. If human review confirms a reporting defect, documenting its definition or correction could improve extraction consistency. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:**

1. Open the linked physical PDF page(s) and inspect the named row, heading, reference population and applicable footnotes.
2. Transcribe the printed inputs exactly, retaining signs, units, slash denominators and header-versus-row distinctions.
3. Reproduce the comparison and calculation above under its stated rule and tolerance; then test the source-grounded alternatives without assigning an unstated denominator or estimator.
4. Resolve the specific question: Counts, header populations and difference available. Missing: exact row-specific analysis populations and raw-versus-other difference/display convention. Was0.9 computed from exact274/989 and264/987 risks, from rounded percentages, or from another population/estimand; what display rule applies?
5. Record the human decision in the blank fields below; the suggested review disposition is a mechanical pre-fill, not an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C021 — Monitoring neuromuscular function,n/N(%): H printed percentage identity

Pending Human Adjudication.

**Candidate statement:** The monitoring H cell 632/982 (64.9%) has an attached percentage differing from division of its explicit fraction; division by the neighboring blockade count 974 reproduces the percentage diagnostically.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** Table 2 Monitoring of neuromuscular function, H No./total No.(%) cell; preceding Neuromuscular blockade row; footnote d (p. 8). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../jama_bluth_2019_oi_190055_16092.pdf#page=8>)

**Source evidence:** H 632/982 (64.9%); neighboring H blockade count974.

**Reported-versus-comparator:** Same-cell printed64.9% versus exact explicit fraction632/982. 100 × printed n/N identity and nearest one-decimal display (±0.05 percentage point); explicit n/N cell supplies the comparison denominator.

**Reasoning procedure:** Read the printed components at the linked source locations, distinguish observed values from conditional calculations, and apply the comparison rule above. Nearest one-decimal display tolerance is ±0.05 percentage point; applicability depends on the stated fraction/population and display rule. Truncation is evaluated separately.

**Calculation:** 100 ×632/982=64.358452138%; nearest64.4%; printed64.9%; gap0.541547862 percentage point. Alternative parent calculation100 ×632/974=64.887063655%, rounding64.9%.

**Alternative source-grounded interpretations:** The parent blockade count reproduces the percentage under nearest rounding. Source footnote d only defines monitoring methods and does not specify the percent denominator; parent reuse remains diagnostic. Direct: explicit n/N, attached percentage and parent count. Derived: the two division results. Inferred: mixed-denominator generation or transcription; none is asserted.

**Mechanical evidence recheck:** Direct extraction and rendering reproduce explicit n/N and its incompatible attached percentage; the parent-denominator calculation does not change what is printed. Evidence state recorded_candidate. This field reports the completed source recheck; it is not human adjudication.

**Quality-control relevance:** This candidate identifies a reproducible numeric, denominator, display or measure-label comparison within the supplied REPORT. Small preventable reporting defects can matter for downstream evidence extraction; the named population, estimand or display questions bound this observation.

**Potential downstream evidence impact:** An extractor preparing a systematic review or meta-analysis could copy monitoring H numerator 632, denominator 982 and percentage 64.9% as one population summary. If human review confirms a reporting defect, documenting its definition or correction could improve extraction consistency. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:**

1. Open the linked physical PDF page(s) and inspect the named row, heading, reference population and applicable footnotes.
2. Transcribe the printed inputs exactly, retaining signs, units, slash denominators and header-versus-row distinctions.
3. Reproduce the comparison and calculation above under its stated rule and tolerance; then test the source-grounded alternatives without assigning an unstated denominator or estimator.
4. Resolve the specific question: All explicit cell inputs are available. Missing: actual percent denominator and display rule; whether the percentage intentionally uses the parent blockade population although the slash fraction has a different denominator. Which denominator generated64.9% forH 632/982 inMonitoring of neuromuscular function, and does the n/N cell intentionally combine a different reference population with a parent-blockade percentage?
5. Record the human decision in the blank fields below; the suggested review disposition is a mechanical pre-fill, not an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C022 — Monitoring neuromuscular function,n/N(%): L printed percentage identity

Pending Human Adjudication.

**Candidate statement:** The monitoring L cell 651/984 (67.7%) has an attached percentage differing from division of its explicit fraction; division by the neighboring blockade count 961 reproduces the percentage diagnostically.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** Table 2 Monitoring of neuromuscular function, L No./total No.(%) cell; preceding Neuromuscular blockade row; footnote d (p. 8). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../jama_bluth_2019_oi_190055_16092.pdf#page=8>)

**Source evidence:** L 651/984 (67.7%); neighboring L blockade count961.

**Reported-versus-comparator:** Same-cell printed67.7% versus exact explicit fraction651/984. 100 × printed n/N identity and nearest one-decimal display (±0.05 percentage point); explicit n/N cell supplies the comparison denominator.

**Reasoning procedure:** Read the printed components at the linked source locations, distinguish observed values from conditional calculations, and apply the comparison rule above. Nearest one-decimal display tolerance is ±0.05 percentage point; applicability depends on the stated fraction/population and display rule. Truncation is evaluated separately.

**Calculation:** 100 ×651/984=66.158536585%; nearest66.2%; printed67.7%; gap1.541463415 percentage point. Alternative parent calculation100 ×651/961=67.741935484%, rounding67.7%.

**Alternative source-grounded interpretations:** The parent blockade count reproduces the percentage under nearest rounding. Source footnote d only defines monitoring methods and does not specify the percent denominator; parent reuse remains diagnostic. Direct: explicit n/N, attached percentage and parent count. Derived: the two division results. Inferred: mixed-denominator generation or transcription; none is asserted.

**Mechanical evidence recheck:** Direct extraction and rendering reproduce explicit n/N and its incompatible attached percentage; the parent-denominator calculation does not change what is printed. Evidence state recorded_candidate. This field reports the completed source recheck; it is not human adjudication.

**Quality-control relevance:** This candidate identifies a reproducible numeric, denominator, display or measure-label comparison within the supplied REPORT. Small preventable reporting defects can matter for downstream evidence extraction; the named population, estimand or display questions bound this observation.

**Potential downstream evidence impact:** An extractor preparing a systematic review or meta-analysis could copy monitoring L numerator 651, denominator 984 and percentage 67.7% as one population summary. If human review confirms a reporting defect, documenting its definition or correction could improve extraction consistency. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:**

1. Open the linked physical PDF page(s) and inspect the named row, heading, reference population and applicable footnotes.
2. Transcribe the printed inputs exactly, retaining signs, units, slash denominators and header-versus-row distinctions.
3. Reproduce the comparison and calculation above under its stated rule and tolerance; then test the source-grounded alternatives without assigning an unstated denominator or estimator.
4. Resolve the specific question: All explicit cell inputs are available. Missing: actual percent denominator and display rule; whether the percentage intentionally uses the parent blockade population although the slash fraction has a different denominator. Which denominator generated67.7% forL 651/984 inMonitoring of neuromuscular function, and does the n/N cell intentionally combine a different reference population with a parent-blockade percentage?
5. Record the human decision in the blank fields below; the suggested review disposition is a mechanical pre-fill, not an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C023 — Reversal,n/N(%): H printed percentage identity

Pending Human Adjudication.

**Candidate statement:** The reversal H cell 724/982 (74.3%) has an attached percentage differing from division of its explicit fraction; division by the neighboring blockade count 974 reproduces the percentage diagnostically.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** Table 2 Reversal, H No./total No.(%) cell; preceding Neuromuscular blockade row; footnote d (p. 8). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../jama_bluth_2019_oi_190055_16092.pdf#page=8>)

**Source evidence:** H 724/982 (74.3%); neighboring H blockade count974.

**Reported-versus-comparator:** Same-cell printed74.3% versus exact explicit fraction724/982. 100 × printed n/N identity and nearest one-decimal display (±0.05 percentage point); explicit n/N cell supplies the comparison denominator.

**Reasoning procedure:** Read the printed components at the linked source locations, distinguish observed values from conditional calculations, and apply the comparison rule above. Nearest one-decimal display tolerance is ±0.05 percentage point; applicability depends on the stated fraction/population and display rule. Truncation is evaluated separately.

**Calculation:** 100 ×724/982=73.727087576%; nearest73.7%; printed74.3%; gap0.572912424 percentage point. Alternative parent calculation100 ×724/974=74.332648871%, rounding74.3%.

**Alternative source-grounded interpretations:** The parent blockade count reproduces the percentage under nearest rounding. Source footnote d only defines monitoring methods and does not specify the percent denominator; parent reuse remains diagnostic. Direct: explicit n/N, attached percentage and parent count. Derived: the two division results. Inferred: mixed-denominator generation or transcription; none is asserted.

**Mechanical evidence recheck:** Direct extraction and rendering reproduce explicit n/N and its incompatible attached percentage; the parent-denominator calculation does not change what is printed. Evidence state recorded_candidate. This field reports the completed source recheck; it is not human adjudication.

**Quality-control relevance:** This candidate identifies a reproducible numeric, denominator, display or measure-label comparison within the supplied REPORT. Small preventable reporting defects can matter for downstream evidence extraction; the named population, estimand or display questions bound this observation.

**Potential downstream evidence impact:** An extractor preparing a systematic review or meta-analysis could copy reversal H numerator 724, denominator 982 and percentage 74.3% as one population summary. If human review confirms a reporting defect, documenting its definition or correction could improve extraction consistency. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:**

1. Open the linked physical PDF page(s) and inspect the named row, heading, reference population and applicable footnotes.
2. Transcribe the printed inputs exactly, retaining signs, units, slash denominators and header-versus-row distinctions.
3. Reproduce the comparison and calculation above under its stated rule and tolerance; then test the source-grounded alternatives without assigning an unstated denominator or estimator.
4. Resolve the specific question: All explicit cell inputs are available. Missing: actual percent denominator and display rule; whether the percentage intentionally uses the parent blockade population although the slash fraction has a different denominator. Which denominator generated74.3% forH 724/982 inReversal, and does the n/N cell intentionally combine a different reference population with a parent-blockade percentage?
5. Record the human decision in the blank fields below; the suggested review disposition is a mechanical pre-fill, not an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C024 — Reversal,n/N(%): L printed percentage identity

Pending Human Adjudication.

**Candidate statement:** The reversal L cell 723/984 (75.2%) has an attached percentage differing from division of its explicit fraction; division by the neighboring blockade count 961 reproduces the percentage diagnostically.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** Table 2 Reversal, L No./total No.(%) cell; preceding Neuromuscular blockade row; footnote d (p. 8). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../jama_bluth_2019_oi_190055_16092.pdf#page=8>)

**Source evidence:** L 723/984 (75.2%); neighboring L blockade count961.

**Reported-versus-comparator:** Same-cell printed75.2% versus exact explicit fraction723/984. 100 × printed n/N identity and nearest one-decimal display (±0.05 percentage point); explicit n/N cell supplies the comparison denominator.

**Reasoning procedure:** Read the printed components at the linked source locations, distinguish observed values from conditional calculations, and apply the comparison rule above. Nearest one-decimal display tolerance is ±0.05 percentage point; applicability depends on the stated fraction/population and display rule. Truncation is evaluated separately.

**Calculation:** 100 ×723/984=73.475609756%; nearest73.5%; printed75.2%; gap1.724390244 percentage point. Alternative parent calculation100 ×723/961=75.234131113%, rounding75.2%.

**Alternative source-grounded interpretations:** The parent blockade count reproduces the percentage under nearest rounding. Source footnote d only defines monitoring methods and does not specify the percent denominator; parent reuse remains diagnostic. Direct: explicit n/N, attached percentage and parent count. Derived: the two division results. Inferred: mixed-denominator generation or transcription; none is asserted.

**Mechanical evidence recheck:** Direct extraction and rendering reproduce explicit n/N and its incompatible attached percentage; the parent-denominator calculation does not change what is printed. Evidence state recorded_candidate. This field reports the completed source recheck; it is not human adjudication.

**Quality-control relevance:** This candidate identifies a reproducible numeric, denominator, display or measure-label comparison within the supplied REPORT. Small preventable reporting defects can matter for downstream evidence extraction; the named population, estimand or display questions bound this observation.

**Potential downstream evidence impact:** An extractor preparing a systematic review or meta-analysis could copy reversal L numerator 723, denominator 984 and percentage 75.2% as one population summary. If human review confirms a reporting defect, documenting its definition or correction could improve extraction consistency. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:**

1. Open the linked physical PDF page(s) and inspect the named row, heading, reference population and applicable footnotes.
2. Transcribe the printed inputs exactly, retaining signs, units, slash denominators and header-versus-row distinctions.
3. Reproduce the comparison and calculation above under its stated rule and tolerance; then test the source-grounded alternatives without assigning an unstated denominator or estimator.
4. Resolve the specific question: All explicit cell inputs are available. Missing: actual percent denominator and display rule; whether the percentage intentionally uses the parent blockade population although the slash fraction has a different denominator. Which denominator generated75.2% forL 723/984 inReversal, and does the n/N cell intentionally combine a different reference population with a parent-blockade percentage?
5. Record the human decision in the blank fields below; the suggested review disposition is a mechanical pre-fill, not an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C025 — Reversal,n/N(%): absolute difference versus exact printed risks

Pending Human Adjudication.

**Candidate statement:** The reversal difference +0.2 differs from nearest rounding of the exact slash-fraction difference +0.251477820 by a small amount: nearest rounding gives +0.3, whereas truncation gives +0.2. This comparator is distinct from C016’s subtraction of printed percentages.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** Table 2 Reversal H/L explicit n/N cells and Absolute Difference column (p. 8). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../jama_bluth_2019_oi_190055_16092.pdf#page=8>)

**Source evidence:** H724/982(74.3%); L723/984(75.2%); difference+0.2(−3.6 to4.1), P.90.

**Reported-versus-comparator:** +0.2 versus difference of the two exact printed fractions. H-minus-L raw risk difference, nearest one-decimal display (±0.05 percentage point), conditional on that being the difference estimand. Explicit slash denominators, rather than overall headers, define this arithmetic comparator.

**Reasoning procedure:** Read the printed components at the linked source locations, distinguish observed values from conditional calculations, and apply the comparison rule above. Nearest one-decimal display tolerance is ±0.05 percentage point; applicability depends on the stated fraction/population and display rule. Truncation is evaluated separately.

**Calculation:** 100 ×(724/982−723/984)=0.251477820 percentage points; nearest+0.3; printed+0.2; gap0.051477820 exceeds0.05 by0.001477820. Truncation yields+0.2. The printed-percentage difference74.3−75.2=−0.9 is the separate C016 comparator.

**Alternative source-grounded interpretations:** Truncation toward zero reconciles the exact count-defined difference; an estimator with different denominators could also yield0.2. Neither mechanism is source-stated. Direct: exact fractions and+0.2. Derived: risk difference and nearest-rounding boundary. Inferred: actual truncation or alternative estimator.

**Mechanical evidence recheck:** The exact fraction comparison reproduces the registered small nearest-rounding gap; the separate registration statement calling it nearest-rounding compatible is not sustained. Evidence state recorded_candidate. This field reports the completed source recheck; it is not human adjudication.

**Quality-control relevance:** This candidate identifies a reproducible numeric, denominator, display or measure-label comparison within the supplied REPORT. Small preventable reporting defects can matter for downstream evidence extraction; the named population, estimand or display questions bound this observation.

**Potential downstream evidence impact:** An extractor preparing a systematic review or meta-analysis could copy reversal difference +0.2 with an assumed nearest-rounding convention rather than preserving the coherent truncation alternative. If human review confirms a reporting defect, documenting its definition or correction could improve extraction consistency. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:**

1. Open the linked physical PDF page(s) and inspect the named row, heading, reference population and applicable footnotes.
2. Transcribe the printed inputs exactly, retaining signs, units, slash denominators and header-versus-row distinctions.
3. Reproduce the comparison and calculation above under its stated rule and tolerance; then test the source-grounded alternatives without assigning an unstated denominator or estimator.
4. Resolve the specific question: Exact fractions and effect available. Missing: row effect estimand and display/truncation rule. Was reversal difference+0.2 calculated from724/982 and723/984 then truncated, or from another effect/population; what computation and display rule defines it?
5. Record the human decision in the blank fields below; the suggested review disposition is a mechanical pre-fill, not an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C026 — Unsupported total-fluids median/effect alignment

Pending Human Adjudication.

**Candidate statement:** The registered comparison contains a record_input_error: it assumed the generic total-fluids Absolute Difference +0.02 L must subtract the displayed medians 1.5 and 1.6 L. The source does not define it as a difference of medians; a confirmed effect inconsistency is not established.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** report_internal_inconsistency

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** The comparison aligns a generic effect cell to median subtraction without source support; no literal median-difference claim exists, and the residual cannot be settled without the estimand.

**Exact source locations:** Table 2 Total fluids median(IQR),L and Absolute Difference cell; full Table 2 footnotes (p. 8); Statistical Analysis (p. 4) as context. [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../jama_bluth_2019_oi_190055_16092.pdf#page=8>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>)

**Source evidence:** Medians H1.5L (IQR1.0–2.5), L1.6L (IQR1.0–2.5); Absolute Difference+0.02L (95%CI−0.11 to0.14), P.79. Column/footnotes do not say difference of medians.

**Reported-versus-comparator:** Registered subtraction of displayed medians1.5−1.6 versus+0.02, conditional on an assumed median-difference estimand. Subtracting medians is applicable only if the effect is a difference of group medians. The source does not supply that alignment; an absolute difference can instead target a mean or other location contrast.

**Reasoning procedure:** Read the printed components at the linked source locations, distinguish observed values from conditional calculations, and apply the comparison rule above. Conditional nearest-rounding bins are ±0.05 L for each median and ±0.005 L for the effect; the prerequisite median-difference estimand is unsupported.

**Calculation:** Median subtraction gives−0.10L. Nearest-rounding bins for1.5 and1.6 permit a true median difference in approximately(−0.20,0.00)L; the+0.02 effect bin is[0.015,0.025)L. These do not overlap IF the effect is a median difference. This cannot test a mean or rank-shift contrast.

**Alternative source-grounded interpretations:** A mean difference or rank-based shift can coexist with opposite-signed displayed median subtraction. Neither the Table 2 footnotes nor the main statistical description assigns total-fluids effects a median-difference meaning. Direct: median/IQR labels and generic Absolute Difference header. Derived: conditional median arithmetic. Unsupported inference: that the effect must subtract those medians; this is not stated.

**Mechanical evidence recheck:** The comparison aligns a generic effect cell to median subtraction without source support; no literal median-difference claim exists, and the residual cannot be settled without the estimand. Evidence state record_input_error. This field reports the completed source recheck; it is not human adjudication.

**Quality-control relevance:** The quality-control issue is the unsupported input alignment in the registered comparison. Retaining the stable ID and its record_input_error state prevents a conditional diagnostic from being presented as a confirmed source contradiction.

**Potential downstream evidence impact:** An extractor preparing a systematic review or meta-analysis could copy +0.02 L as an unsupported difference of medians instead of retaining an unspecified location-effect estimand. If human review confirms a reporting defect, documenting its definition or correction could improve extraction consistency. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:**

1. Open the linked physical PDF page(s) and inspect the named row, heading, reference population and applicable footnotes.
2. Transcribe the printed inputs exactly, retaining signs, units, slash denominators and header-versus-row distinctions.
3. Reproduce the comparison and calculation above under its stated rule and tolerance; then test the source-grounded alternatives without assigning an unstated denominator or estimator.
4. Resolve the specific question: Printed medians and effect available; necessary missing input is the total-fluids effect estimand and procedure. Group means/distributions or rank-shift inputs are absent, so an alternative effect cannot be reconstructed. What estimand and procedure generated+0.02L for total fluids, and is it intended as a mean difference, rank-based shift, or difference of medians?
5. Record the human decision in the blank fields below; the suggested review disposition is a mechanical pre-fill, not an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C027 — Primary PPC within5days: labeled RR versus printed patient risks

Pending Human Adjudication.

**Candidate statement:** The primary PPC risk ratio 0.93 differs from the H/L event-risk ratio 0.903748096 computed from 211/989 and 233/987. The point-estimate formula, conditioning, adjustment and display convention require clarification; a distinct reverse-conditioning diagnostic can reproduce the printed point.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** Table 3 Primary postoperative pulmonary complications within five days row, No.of Events(%), H989/L987 headers and Risk Ratio column (p. 9); footnotes a/b (p. 10); completed-analysis RR statement (p. 4); abstract RESULTS(p. 1), Primary Outcome narrative(p. 8), Figure 2 All patients row(p. 10). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 1](<../jama_bluth_2019_oi_190055_16092.pdf#page=1>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../jama_bluth_2019_oi_190055_16092.pdf#page=8>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>)

**Source evidence:** H events211; L events233; reference populations H989/L987; printed RR0.93 (95%CI0.83 to1.04). Footnote a: number of reference patients unless otherwise indicated. Footnote b: data are risk ratios unless otherwise indicated; RRs/CIs calculated using the Wald likelihood ratio approximation test.

**Reported-versus-comparator:** Printed outcome risk-ratio label/point0.93 versus same-row H/L event-risk ratio(211/989)/(233/987). For the stated event, high-versus-low patient risk ratio divides high event risk by low event risk. Identity follows the event/reference labels and Table 3 reference-patient footnote. A different adjusted/standardized estimand or reversed conditioning requires its definition; no interval/P diagnostic is used to replace the point estimate.

**Reasoning procedure:** Read the printed components at the linked source locations, distinguish observed values from conditional calculations, and apply the comparison rule above. The point-display tolerance under nearest two-decimal rounding is ±0.005. It does not license substituting a different conditioning or adjusted estimand.

**Calculation:** (211/989)/(233/987)=0.903748096, nearest two-decimal0.90; printed0.93; signed gap0.026251904 exceeds0.005. Reverse-conditioning diagnostic: [211/(211+233)]/[(778)/(1532)]=0.935790546; truncating THAT quantity to two decimals gives0.93, exactly the printed point. This is risk of high-group membership conditional on event versus no event, a different contrast from event risk conditional on treatment.

**Alternative source-grounded interpretations:** The reverse-conditioning diagnostic computed solely from the printed 2×2 counts plus truncation reproduces this point. It is a source-grounded numerical explanation, not evidence that the authors used that coding. A differently defined adjusted/standardized RR could also differ from the crude event ratio, but its target/formula must be supplied. The Wald-approximation wording alone does not define a different point contrast. Direct: count/reference cells, risk-ratio heading, point/interval and generic calculation wording. Derived: event-risk identity and reverse-conditioning diagnostic. Inferred: swapped coding, truncation, or adjustment; no production cause is asserted. All four 2×2 cells are positive: 211, 778, 233 and 754. Generic zero-cell corrections are therefore not an explanation. Truncating the stated event-risk ratio itself gives 0.90, not 0.93; only the separately defined reverse-conditioning diagnostic described above reproduces 0.93 with truncation.

**Mechanical evidence recheck:** The direct source reproduces the labeled point and exact reference counts; the event-risk identity discrepancy remains. An alternative reverse-conditioning diagnostic reproduces the display but does not reconcile its stated event-risk interpretation. Evidence state recorded_candidate. This field reports the completed source recheck; it is not human adjudication.

**Quality-control relevance:** This candidate identifies a reproducible numeric, denominator, display or measure-label comparison within the supplied REPORT. Small preventable reporting defects can matter for downstream evidence extraction; the named population, estimand or display questions bound this observation.

**Potential downstream evidence impact:** An extractor preparing a systematic review or meta-analysis could copy RR 0.93 and its interval as the H/L patient event-risk contrast without resolving the exact point-estimate definition. If human review confirms a reporting defect, documenting its definition or correction could improve extraction consistency. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:**

1. Open the linked physical PDF page(s) and inspect the named row, heading, reference population and applicable footnotes.
2. Transcribe the printed inputs exactly, retaining signs, units, slash denominators and header-versus-row distinctions.
3. Reproduce the comparison and calculation above under its stated rule and tolerance; then test the source-grounded alternatives without assigning an unstated denominator or estimator.
4. Resolve the specific question: Counts, reference populations, label, CI, and generic named approximation available. Missing: exact point-estimate formula, event/reference coding, whether an adjusted/standardized estimand is intended, and display rule. No row-specific covariate adjustment is identified for this Table 3 point. For Primary postoperative pulmonary complications within five days, what exact formula, outcome/reference orientation and display rule produced RR0.93? Is it intended as H/L event risk, a reversed-conditioning contrast, or a specifically defined adjusted/model quantity?
5. Record the human decision in the blank fields below; the suggested review disposition is a mechanical pre-fill, not an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C028 — Mild respiratory failure: absolute difference versus exact printed risks

**Candidate statement:** For mild respiratory failure, the printed −1.9 percentage-point difference differs slightly from the nearest one-decimal display of the exact High-minus-Low count-defined difference. The observation depends on the computation and display convention: subtracting the displayed percentages or truncating the exact difference reproduces −1.9. Status: Pending Human Adjudication.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../jama_bluth_2019_oi_190055_16092.pdf#page=8>), Primary Outcome narrative, mild respiratory failure counts/percentages and signed difference; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3 Mild respiratory failure row and High PEEP 989/Low PEEP 987 headers; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnote a on reference patients.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Mild respiratory failure; 135(13.7); 154(15.6); −1.9(−5.1 to1.2); RR0.92(0.80 to1.05); .22. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O02-RD; checkers/numeric_consistency.md :: NB-MILD-DIFF. Numeric relationship: N181. Additional matched narrative relationship: N022.

**Reported-versus-comparator:** Reported −1.9 percentage points (95% CI −5.1 to 1.2), repeated in the narrative, versus the derived count-defined High-minus-Low risk difference −1.952685211 percentage points, whose nearest one-decimal display is −2.0. The separate displayed-percentage comparator, 13.7−15.6, equals −1.9.

**Reasoning procedure:** Use the exact printed integers and reference populations to compute 100×(135/989−154/987). Under nearest one-decimal display, the absolute tolerance is 0.05 percentage point. This rule is conditional on a raw count-defined difference and nearest rounding; neither the exact difference estimator nor the display convention is fully specified. The 0.15-percentage-point allowance when comparing already rounded summaries does not change the exact integer calculation.

**Calculation:** 100×(135/989−154/987)=−1.952685211 percentage points; printed-minus-derived=+0.052685211 percentage point. The gap exceeds 0.05 by only 0.002685211. Nearest rounding gives −2.0; truncation toward zero gives −1.9; 13.7−15.6=−1.9.

**Alternative source-grounded interpretations:** Displayed-percentage subtraction and truncation toward zero both reconcile the printed −1.9. A specifically defined fitted or adjusted difference or different analysis denominator could also differ from the crude calculation, but the package does not give a row-specific point formula/display rule. These are alternatives for human reconciliation, not identified production mechanisms or proposed corrections.

**Mechanical evidence recheck:** The direct-source recheck found the narrative and Table 3 cells, matched 135 (13.7%), 154 (15.6%), −1.9 (−5.1 to 1.2), and the reference populations, and reproduced the tiny conditional nearest-rounding gap. The named missing inputs are the raw-versus-model difference formula and rounding/truncation convention. State recorded_candidate records that comparison pending the definition; it does not establish an arithmetic error. The suggested retain disposition is a mechanical pre-fill for human review. Document roles and S_W classification were confirmed.

**Quality-control relevance:** Clarifying the mild respiratory failure difference −1.9 percentage points and its interpretation as an exact count-defined effect supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the mild respiratory failure difference −1.9 percentage points and its interpretation as an exact count-defined effect. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../jama_bluth_2019_oi_190055_16092.pdf#page=8>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and confirm the matched row, narrative and reference-patient rule.
2. Recompute the exact count-defined difference, displayed-percentage subtraction and truncation alternatives.
3. Determine whether −1.9 was obtained from exact risks, rounded summaries or a fitted estimand, and identify its actual display convention.
4. Decide which calculation and value an extractor should use; record the human decision in the fields below.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C029 — Mild respiratory failure: labeled RR versus printed patient risks

**Candidate statement:** For mild respiratory failure, the printed risk ratio 0.92 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Mild respiratory failure row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description. REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../jama_bluth_2019_oi_190055_16092.pdf#page=8>), Primary Outcome narrative, additionally matched mild respiratory failure counts and reported effect.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Mild respiratory failure; 135(13.7); 154(15.6); −1.9(−5.1 to1.2); RR0.92(0.80 to1.05); .22. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O02-RR; checkers/numeric_consistency.md :: NB-RR-MILD; checkers/statistical_pass_1.md :: RR-O02; checkers/cross_source_consistency.md :: XR02. Numeric relationship: N181. The direct-source recheck additionally confirmed the matched Primary Outcome narrative on PDF p. 8.

**Reported-versus-comparator:** Reported risk ratio 0.92 (95% CI 0.80 to1.05) versus the derived clinical event-risk ratio (135/989)/(154/987)=0.874850630, nearest display 0.87. Printed-minus-derived=0.045149370; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (135/989)/(154/987)=0.874850630; nearest 0.87; printed 0.92; signed gap 0.045149370. Reverse-conditioning diagnostic q=[135/(135+154)]/[(854)/(1687)]=0.922769301; nearest 0.92, truncation 0.92.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 135, Low PEEP 154, reference patients 989/987, risk ratio 0.92 (0.80 to1.05) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the mild respiratory failure risk ratio 0.92, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the mild respiratory failure risk ratio 0.92, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Mild respiratory failure row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (135/989)/(154/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 0.92. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C030 — Moderate respiratory failure: labeled RR versus printed patient risks

**Candidate statement:** For moderate respiratory failure, the printed risk ratio 0.83 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Moderate respiratory failure row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Moderate respiratory failure; 42(4.2); 58(5.9); −1.6(−3.6 to0.3); RR0.83(0.65 to1.05); .10. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O03-RR; checkers/statistical_pass_1.md :: RR-O03; checkers/cross_source_consistency.md :: XR03. Numeric relationship: N182.

**Reported-versus-comparator:** Reported risk ratio 0.83 (95% CI 0.65 to1.05) versus the derived clinical event-risk ratio (42/989)/(58/987)=0.722673547, nearest display 0.72. Printed-minus-derived=0.107326453; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (42/989)/(58/987)=0.722673547; nearest 0.72; printed 0.83; signed gap 0.107326453. Reverse-conditioning diagnostic q=[42/(42+58)]/[(947)/(1876)]=0.832016895; nearest 0.83, truncation 0.83.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 42, Low PEEP 58, reference patients 989/987, risk ratio 0.83 (0.65 to1.05) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the moderate respiratory failure risk ratio 0.83, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the moderate respiratory failure risk ratio 0.83, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Moderate respiratory failure row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (42/989)/(58/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 0.83. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C031 — Severe respiratory failure: labeled RR versus printed patient risks

**Candidate statement:** For severe respiratory failure, the printed risk ratio 0.90 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Severe respiratory failure row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Severe respiratory failure; 30(3.0); 36(3.6); −0.6(−2.2 to1.0); RR0.90(0.69 to1.18); .45. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O04-RR; checkers/statistical_pass_1.md :: RR-O04; checkers/cross_source_consistency.md :: XR04. Numeric relationship: N183.

**Reported-versus-comparator:** Reported risk ratio 0.90 (95% CI 0.69 to1.18) versus the derived clinical event-risk ratio (30/989)/(36/987)=0.831648129, nearest display 0.83. Printed-minus-derived=0.068351871; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (30/989)/(36/987)=0.831648129; nearest 0.83; printed 0.90; signed gap 0.068351871. Reverse-conditioning diagnostic q=[30/(30+36)]/[(959)/(1910)]=0.905299080; nearest 0.91, truncation 0.90.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 30, Low PEEP 36, reference patients 989/987, risk ratio 0.90 (0.69 to1.18) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the severe respiratory failure risk ratio 0.90, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the severe respiratory failure risk ratio 0.90, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Severe respiratory failure row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (30/989)/(36/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 0.90. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C032 — Atelectasis: labeled RR versus printed patient risks

**Candidate statement:** For atelectasis, the printed risk ratio 0.88 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Atelectasis row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Atelectasis; 44(4.4); 55(5.6); −1.1(−3.0 to0.8); RR0.88(0.70 to1.10); .25. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O05-RR; checkers/statistical_pass_1.md :: RR-O05; checkers/cross_source_consistency.md :: XR05. Numeric relationship: N184.

**Reported-versus-comparator:** Reported risk ratio 0.88 (95% CI 0.70 to1.10) versus the derived clinical event-risk ratio (44/989)/(55/987)=0.798382204, nearest display 0.80. Printed-minus-derived=0.081617796; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (44/989)/(55/987)=0.798382204; nearest 0.80; printed 0.88; signed gap 0.081617796. Reverse-conditioning diagnostic q=[44/(44+55)]/[(945)/(1877)]=0.882774838; nearest 0.88, truncation 0.88.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 44, Low PEEP 55, reference patients 989/987, risk ratio 0.88 (0.70 to1.10) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the atelectasis risk ratio 0.88, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the atelectasis risk ratio 0.88, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Atelectasis row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (44/989)/(55/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 0.88. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C033 — Pleural effusion: labeled RR versus printed patient risks

**Candidate statement:** For pleural effusion, the printed risk ratio 1.35 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Pleural effusion row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description. REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../jama_bluth_2019_oi_190055_16092.pdf#page=8>), Primary Outcome narrative, additionally matched pleural effusion counts and reported effect.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Pleural effusion; 43(4.3); 21(2.1); 2.2(0.7 to3.8); RR1.35(1.14 to1.62); .005. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O06-RR; checkers/numeric_consistency.md :: NB-RR-EFFUSION; checkers/statistical_pass_1.md :: RR-O06; checkers/cross_source_consistency.md :: XR06. Numeric relationship: N185. The direct-source recheck additionally confirmed the matched Primary Outcome narrative on PDF p. 8.

**Reported-versus-comparator:** Reported risk ratio 1.35 (95% CI 1.14 to1.62) versus the derived clinical event-risk ratio (43/989)/(21/987)=2.043478261, nearest display 2.04. Printed-minus-derived=-0.693478261; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (43/989)/(21/987)=2.043478261; nearest 2.04; printed 1.35; signed gap -0.693478261. Reverse-conditioning diagnostic q=[43/(43+21)]/[(946)/(1912)]=1.357954545; nearest 1.36, truncation 1.35.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 43, Low PEEP 21, reference patients 989/987, risk ratio 1.35 (1.14 to1.62) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the pleural effusion risk ratio 1.35, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the pleural effusion risk ratio 1.35, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Pleural effusion row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (43/989)/(21/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 1.35. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C034 — New pulmonary infiltrates: labeled RR versus printed patient risks

**Candidate statement:** For new pulmonary infiltrates, the printed risk ratio 0.87 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, New pulmonary infiltrates row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: New pulmonary infiltrates; 14(1.4); 18(1.8); −0.4(−1.5 to0.7); RR0.87(0.59 to1.29); .47. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O07-RR; checkers/statistical_pass_1.md :: RR-O07; checkers/cross_source_consistency.md :: XR07. Numeric relationship: N186.

**Reported-versus-comparator:** Reported risk ratio 0.87 (95% CI 0.59 to1.29) versus the derived clinical event-risk ratio (14/989)/(18/987)=0.776204921, nearest display 0.78. Printed-minus-derived=0.093795079; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (14/989)/(18/987)=0.776204921; nearest 0.78; printed 0.87; signed gap 0.093795079. Reverse-conditioning diagnostic q=[14/(14+18)]/[(975)/(1944)]=0.872307692; nearest 0.87, truncation 0.87.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 14, Low PEEP 18, reference patients 989/987, risk ratio 0.87 (0.59 to1.29) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the new pulmonary infiltrates risk ratio 0.87, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the new pulmonary infiltrates risk ratio 0.87, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named New pulmonary infiltrates row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (14/989)/(18/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 0.87. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C035 — Cardiopulmonary edema: labeled RR versus printed patient risks

**Candidate statement:** For cardiopulmonary edema, the printed risk ratio 1.31 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Cardiopulmonary edema row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Cardiopulmonary edema; 17(1.7); 9(0.9); 0.8(−0.2 to1.8); RR1.31(0.99 to1.74); .12. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O08-RR; checkers/statistical_pass_1.md :: RR-O08; checkers/cross_source_consistency.md :: XR08. Numeric relationship: N187.

**Reported-versus-comparator:** Reported risk ratio 1.31 (95% CI 0.99 to1.74) versus the derived clinical event-risk ratio (17/989)/(9/987)=1.885069093, nearest display 1.89. Printed-minus-derived=-0.575069093; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (17/989)/(9/987)=1.885069093; nearest 1.89; printed 1.31; signed gap -0.575069093. Reverse-conditioning diagnostic q=[17/(17+9)]/[(972)/(1950)]=1.311728395; nearest 1.31, truncation 1.31.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 17, Low PEEP 9, reference patients 989/987, risk ratio 1.31 (0.99 to1.74) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the cardiopulmonary edema risk ratio 1.31, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the cardiopulmonary edema risk ratio 1.31, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Cardiopulmonary edema row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (17/989)/(9/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 1.31. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C036 — Bronchospasm: labeled RR versus printed patient risks

**Candidate statement:** For bronchospasm, the printed risk ratio 1.09 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Bronchospasm row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Bronchospasm; 12(1.2); 10(1.0); 0.2(−0.7 to1.1); RR1.09(0.74 to1.60); .67. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O09-RR; checkers/statistical_pass_1.md :: RR-O09; checkers/cross_source_consistency.md :: XR09. Numeric relationship: N188.

**Reported-versus-comparator:** Reported risk ratio 1.09 (95% CI 0.74 to1.60) versus the derived clinical event-risk ratio (12/989)/(10/987)=1.197573306, nearest display 1.20. Printed-minus-derived=-0.107573306; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (12/989)/(10/987)=1.197573306; nearest 1.20; printed 1.09; signed gap -0.107573306. Reverse-conditioning diagnostic q=[12/(12+10)]/[(977)/(1954)]=1.090909091; nearest 1.09, truncation 1.09.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 12, Low PEEP 10, reference patients 989/987, risk ratio 1.09 (0.74 to1.60) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the bronchospasm risk ratio 1.09, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the bronchospasm risk ratio 1.09, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Bronchospasm row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (12/989)/(10/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 1.09. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C037 — Pulmonary infection: labeled RR versus printed patient risks

**Candidate statement:** For pulmonary infection, the printed risk ratio 0.99 differs from nearest rounding of the count-defined High/Low event-risk ratio, but truncation of that clinical ratio itself reproduces 0.99. This remains a conditional display/definition question. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Pulmonary infection event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Pulmonary infection row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Pulmonary infection; 10(1.0); 10(1.0); 0(−0.9 to0.9); RR0.99(0.64 to1.55); >.99. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O10-RR; checkers/statistical_pass_1.md :: RR-O10; checkers/cross_source_consistency.md :: XR10. Numeric relationship: N189.

**Reported-versus-comparator:** Reported risk ratio 0.99 (95% CI 0.64 to1.55) versus the derived clinical event-risk ratio (10/989)/(10/987)=0.997977755, nearest display 1.00. Printed-minus-derived=-0.007977755; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (10/989)/(10/987)=0.997977755; nearest 1.00; printed 0.99; signed gap -0.007977755. Reverse-conditioning diagnostic q=[10/(10+10)]/[(979)/(1956)]=0.998978550; nearest 1.00, truncation 0.99. Truncating the clinical ratio 0.997977755 itself gives 0.99.

**Alternative source-grounded interpretations:** Truncation of the clinical event-risk ratio itself reproduces 0.99, so reversed conditioning is not required to explain this display. The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 10, Low PEEP 10, reference patients 989/987, risk ratio 0.99 (0.64 to1.55) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. It also confirmed that clinical-ratio truncation reconciles the printed point. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the pulmonary infection risk ratio 0.99, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the pulmonary infection risk ratio 0.99, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Pulmonary infection row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (10/989)/(10/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 0.99. Check specifically whether the clinical ratio was truncated to 0.99. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C038 — Aspiration pneumonitis: labeled RR versus printed patient risks

**Candidate statement:** For aspiration pneumonitis, the printed risk ratio 1.33 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Aspiration pneumonitis event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Aspiration pneumonitis row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Aspiration pneumonitis; 2(0.2); 1(0.1); 0.1(−0.2 to0.4); RR1.33(0.60 to2.97); >.99. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O11-RR; checkers/statistical_pass_1.md :: RR-O11; checkers/cross_source_consistency.md :: XR11. Numeric relationship: N190.

**Reported-versus-comparator:** Reported risk ratio 1.33 (95% CI 0.60 to2.97) versus the derived clinical event-risk ratio (2/989)/(1/987)=1.995955511, nearest display 2.00. Printed-minus-derived=-0.665955511; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (2/989)/(1/987)=1.995955511; nearest 2.00; printed 1.33; signed gap -0.665955511. Reverse-conditioning diagnostic q=[2/(2+1)]/[(987)/(1973)]=1.332657886; nearest 1.33, truncation 1.33.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 2, Low PEEP 1, reference patients 989/987, risk ratio 1.33 (0.60 to2.97) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the aspiration pneumonitis risk ratio 1.33, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the aspiration pneumonitis risk ratio 1.33, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Aspiration pneumonitis row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (2/989)/(1/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 1.33. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C039 — ARDS: labeled RR versus printed patient risks

**Candidate statement:** For ards, the printed risk ratio 1.50 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Acute respiratory distress syndrome event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, ARDS row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: ARDS; 3(0.3); 1(0.1); 0.2(−0.2 to0.6); RR1.50(0.85 to2.64); .62. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O12-RR; checkers/statistical_pass_1.md :: RR-O12; checkers/cross_source_consistency.md :: XR12. Numeric relationship: N191.

**Reported-versus-comparator:** Reported risk ratio 1.50 (95% CI 0.85 to2.64) versus the derived clinical event-risk ratio (3/989)/(1/987)=2.993933266, nearest display 2.99. Printed-minus-derived=-1.493933266; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (3/989)/(1/987)=2.993933266; nearest 2.99; printed 1.50; signed gap -1.493933266. Reverse-conditioning diagnostic q=[3/(3+1)]/[(986)/(1972)]=1.500000000; nearest 1.50, truncation 1.50.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 3, Low PEEP 1, reference patients 989/987, risk ratio 1.50 (0.85 to2.64) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the ards risk ratio 1.50, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the ards risk ratio 1.50, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named ARDS row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (3/989)/(1/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 1.50. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C040 — Pneumothorax: labeled RR versus printed patient risks

**Candidate statement:** For pneumothorax, the printed risk ratio 0.50 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Pneumothorax event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Pneumothorax row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Pneumothorax; 1(0.1); 3(0.3); −0.2(−0.6 to0.2); RR0.50(0.09 to2.72); .37. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O13-RR; checkers/statistical_pass_1.md :: RR-O13; checkers/cross_source_consistency.md :: XR13. Numeric relationship: N192.

**Reported-versus-comparator:** Reported risk ratio 0.50 (95% CI 0.09 to2.72) versus the derived clinical event-risk ratio (1/989)/(3/987)=0.332659252, nearest display 0.33. Printed-minus-derived=0.167340748; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (1/989)/(3/987)=0.332659252; nearest 0.33; printed 0.50; signed gap 0.167340748. Reverse-conditioning diagnostic q=[1/(1+3)]/[(988)/(1972)]=0.498987854; nearest 0.50, truncation 0.49.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. Here q=0.498987854 nearest-rounds to 0.50 and truncates to 0.49. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 1, Low PEEP 3, reference patients 989/987, risk ratio 0.50 (0.09 to2.72) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the pneumothorax risk ratio 0.50, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the pneumothorax risk ratio 0.50, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Pneumothorax row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (1/989)/(3/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 0.50. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C041 — Severe postoperative PPC: labeled RR versus printed patient risks

**Candidate statement:** For severe postoperative ppc, the printed risk ratio 0.91 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Severe postoperative pulmonary complications event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Severe postoperative PPC row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Severe postoperative PPC; 116(11.7); 134(13.6); −1.8(−4.8 to1.1); RR0.91(0.80 to1.05); .22. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O14-RR; checkers/statistical_pass_1.md :: RR-O14; checkers/cross_source_consistency.md :: XR14. Numeric relationship: N193.

**Reported-versus-comparator:** Reported risk ratio 0.91 (95% CI 0.80 to1.05) versus the derived clinical event-risk ratio (116/989)/(134/987)=0.863921042, nearest display 0.86. Printed-minus-derived=0.046078958; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (116/989)/(134/987)=0.863921042; nearest 0.86; printed 0.91; signed gap 0.046078958. Reverse-conditioning diagnostic q=[116/(116+134)]/[(873)/(1726)]=0.917369989; nearest 0.92, truncation 0.91.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 116, Low PEEP 134, reference patients 989/987, risk ratio 0.91 (0.80 to1.05) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the severe postoperative ppc risk ratio 0.91, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the severe postoperative ppc risk ratio 0.91, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Severe postoperative PPC row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (116/989)/(134/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 0.91. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C042 — Postoperative extrapulmonary composite: labeled RR versus printed patient risks

**Candidate statement:** For postoperative extrapulmonary composite, the printed risk ratio 1.06 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Postoperative extrapulmonary complications event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Postoperative extrapulmonary composite row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Postoperative extrapulmonary composite; 167(16.9); 150(15.2); 1.7(−1.5 to4.9); RR1.06(0.95 to1.19); .31. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O15-RR; checkers/statistical_pass_1.md :: RR-O15; checkers/cross_source_consistency.md :: XR15. Numeric relationship: N194.

**Reported-versus-comparator:** Reported risk ratio 1.06 (95% CI 0.95 to1.19) versus the derived clinical event-risk ratio (167/989)/(150/987)=1.111081901, nearest display 1.11. Printed-minus-derived=-0.051081901; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (167/989)/(150/987)=1.111081901; nearest 1.11; printed 1.06; signed gap -0.051081901. Reverse-conditioning diagnostic q=[167/(167+150)]/[(822)/(1659)]=1.063241152; nearest 1.06, truncation 1.06.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 167, Low PEEP 150, reference patients 989/987, risk ratio 1.06 (0.95 to1.19) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the postoperative extrapulmonary composite risk ratio 1.06, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the postoperative extrapulmonary composite risk ratio 1.06, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Postoperative extrapulmonary composite row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (167/989)/(150/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 1.06. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C043 — Systemic inflammatory response syndrome: labeled RR versus printed patient risks

**Candidate statement:** For systemic inflammatory response syndrome, the printed risk ratio 1.06 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Systemic inflammatory response syndrome event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Systemic inflammatory response syndrome row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Systemic inflammatory response syndrome; 93(9.4); 83(8.4); 1.0(−1.5 to3.5); RR1.06(0.91 to1.22); .44. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O16-RR; checkers/statistical_pass_1.md :: RR-O16; checkers/cross_source_consistency.md :: XR16. Numeric relationship: N195.

**Reported-versus-comparator:** Reported risk ratio 1.06 (95% CI 0.91 to1.22) versus the derived clinical event-risk ratio (93/989)/(83/987)=1.118216039, nearest display 1.12. Printed-minus-derived=-0.058216039; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (93/989)/(83/987)=1.118216039; nearest 1.12; printed 1.06; signed gap -0.058216039. Reverse-conditioning diagnostic q=[93/(93+83)]/[(896)/(1800)]=1.061536120; nearest 1.06, truncation 1.06.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 93, Low PEEP 83, reference patients 989/987, risk ratio 1.06 (0.91 to1.22) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the systemic inflammatory response syndrome risk ratio 1.06, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the systemic inflammatory response syndrome risk ratio 1.06, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Systemic inflammatory response syndrome row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (93/989)/(83/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 1.06. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C044 — Sepsis: labeled RR versus printed patient risks

**Candidate statement:** For sepsis, the printed risk ratio 1.09 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Sepsis event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Sepsis row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Sepsis; 18(1.8); 15(1.5); 0.3(−0.8 to1.4); RR1.09(0.79 to1.49); .60. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O17-RR; checkers/statistical_pass_1.md :: RR-O17; checkers/cross_source_consistency.md :: XR17. Numeric relationship: N196.

**Reported-versus-comparator:** Reported risk ratio 1.09 (95% CI 0.79 to1.49) versus the derived clinical event-risk ratio (18/989)/(15/987)=1.197573306, nearest display 1.20. Printed-minus-derived=-0.107573306; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (18/989)/(15/987)=1.197573306; nearest 1.20; printed 1.09; signed gap -0.107573306. Reverse-conditioning diagnostic q=[18/(18+15)]/[(971)/(1943)]=1.091470836; nearest 1.09, truncation 1.09.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 18, Low PEEP 15, reference patients 989/987, risk ratio 1.09 (0.79 to1.49) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the sepsis risk ratio 1.09, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the sepsis risk ratio 1.09, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Sepsis row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (18/989)/(15/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 1.09. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C045 — Severe sepsis: labeled RR versus printed patient risks

**Candidate statement:** For severe sepsis, the printed risk ratio 0.82 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Severe sepsis event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Severe sepsis row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Severe sepsis; 7(0.7); 10(1.0); −0.3(−1.1 to0.5); RR0.82(0.46 to1.45); .46. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O18-RR; checkers/statistical_pass_1.md :: RR-O18; checkers/cross_source_consistency.md :: XR18. Numeric relationship: N197.

**Reported-versus-comparator:** Reported risk ratio 0.82 (95% CI 0.46 to1.45) versus the derived clinical event-risk ratio (7/989)/(10/987)=0.698584429, nearest display 0.70. Printed-minus-derived=0.121415571; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (7/989)/(10/987)=0.698584429; nearest 0.70; printed 0.82; signed gap 0.121415571. Reverse-conditioning diagnostic q=[7/(7+10)]/[(982)/(1959)]=0.821432850; nearest 0.82, truncation 0.82.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 7, Low PEEP 10, reference patients 989/987, risk ratio 0.82 (0.46 to1.45) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the severe sepsis risk ratio 0.82, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the severe sepsis risk ratio 0.82, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Severe sepsis row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (7/989)/(10/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 0.82. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C046 — Septic shock: labeled RR versus printed patient risks

**Candidate statement:** For septic shock, the printed risk ratio 0.93 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Septic shock event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Septic shock row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Septic shock; 7(0.7); 8(0.8); −0.1(−0.9 to0.7); RR0.93(0.54 to1.60); .79. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O19-RR; checkers/statistical_pass_1.md :: RR-O19; checkers/cross_source_consistency.md :: XR19. Numeric relationship: N198.

**Reported-versus-comparator:** Reported risk ratio 0.93 (95% CI 0.54 to1.60) versus the derived clinical event-risk ratio (7/989)/(8/987)=0.873230536, nearest display 0.87. Printed-minus-derived=0.056769464; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (7/989)/(8/987)=0.873230536; nearest 0.87; printed 0.93; signed gap 0.056769464. Reverse-conditioning diagnostic q=[7/(7+8)]/[(982)/(1961)]=0.931907671; nearest 0.93, truncation 0.93.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 7, Low PEEP 8, reference patients 989/987, risk ratio 0.93 (0.54 to1.60) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the septic shock risk ratio 0.93, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the septic shock risk ratio 0.93, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Septic shock row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (7/989)/(8/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 0.93. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C047 — Gastrointestinal failure: labeled RR versus printed patient risks

**Candidate statement:** For gastrointestinal failure, the printed risk ratio 1.07 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Gastrointestinal failure event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Gastrointestinal failure row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Gastrointestinal failure; 65(6.6); 56(5.7); 0.9(−1.2 to3.0); RR1.07(0.90 to1.28); .40. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O20-RR; checkers/statistical_pass_1.md :: RR-O20; checkers/cross_source_consistency.md :: XR20. Numeric relationship: N199.

**Reported-versus-comparator:** Reported risk ratio 1.07 (95% CI 0.90 to1.28) versus the derived clinical event-risk ratio (65/989)/(56/987)=1.158367037, nearest display 1.16. Printed-minus-derived=-0.088367037; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (65/989)/(56/987)=1.158367037; nearest 1.16; printed 1.07; signed gap -0.088367037. Reverse-conditioning diagnostic q=[65/(65+56)]/[(924)/(1855)]=1.078449787; nearest 1.08, truncation 1.07.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 65, Low PEEP 56, reference patients 989/987, risk ratio 1.07 (0.90 to1.28) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the gastrointestinal failure risk ratio 1.07, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the gastrointestinal failure risk ratio 1.07, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Gastrointestinal failure row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (65/989)/(56/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 1.07. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C048 — Acute kidney failure: labeled RR versus printed patient risks

**Candidate statement:** For acute kidney failure, the printed risk ratio 0.98 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Acute kidney failure event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Acute kidney failure row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Acute kidney failure; 31(3.1); 32(3.2); −0.1(−1.6 to1.4); RR0.98(0.76 to1.26); .89. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O25-RR; checkers/statistical_pass_1.md :: RR-O25; checkers/cross_source_consistency.md :: XR21. Numeric relationship: N204.

**Reported-versus-comparator:** Reported risk ratio 0.98 (95% CI 0.76 to1.26) versus the derived clinical event-risk ratio (31/989)/(32/987)=0.966790950, nearest display 0.97. Printed-minus-derived=0.013209050; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (31/989)/(32/987)=0.966790950; nearest 0.97; printed 0.98; signed gap 0.013209050. Reverse-conditioning diagnostic q=[31/(31+32)]/[(958)/(1913)]=0.982586075; nearest 0.98, truncation 0.98.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 31, Low PEEP 32, reference patients 989/987, risk ratio 0.98 (0.76 to1.26) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the acute kidney failure risk ratio 0.98, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the acute kidney failure risk ratio 0.98, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Acute kidney failure row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (31/989)/(32/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 0.98. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C049 — Kidney failure,n/N(%): H printed percentage identity

**Candidate statement:** For the nested kidney failure category, the High PEEP cell 7/31 (22.5%) does not match nearest one-decimal rounding of its explicit quotient. Truncation reproduces the printed percentage, so this is a conditional display-rule question. Status: Pending Human Adjudication.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Failure count/denominator versus REPORT main article same-cell percentage; REPORT main article PDF p. 10 footnotes f/g define the row

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3 Acute kidney failure subcategory Failure, explicit High PEEP 7/31 (22.5%) cell compared with its own numerator/denominator; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>), footnotes f/g defining No./total No. and kidney stage categories.

**Source evidence:** Direct printed nested row: Failure; High PEEP 7/31 (22.5%); Low PEEP 5/32 (15.6%). No separate risk ratio or absolute difference is printed for this subcategory; the class comparison P .97 is shared by the kidney-stage block. The denominator here is explicitly 31 for High PEEP and 32 for Low PEEP, not the randomized reference population. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O28-PCT-H. Numeric relationship: N207.

**Reported-versus-comparator:** Reported High PEEP 22.5% versus 100×7/31=22.580645161%, nearest one-decimal 22.6%. The signed printed-minus-exact gap is -0.080645161 percentage point.

**Reasoning procedure:** Divide the explicit nested numerator 7 by its explicit denominator 31 and multiply by 100. Nearest one-decimal rounding permits 0.05 percentage point at a tie; the observed non-tie gap exceeds that bound. Applicability is conditional on nearest rounding. No requirement that rounded subcategory percentages sum exactly to 100 is imposed.

**Calculation:** 100×7/31=22.580645161%; nearest 22.6%; truncation 22.5%; printed 22.5%; absolute gap 0.080645161 percentage point, exceeding 0.05 by 0.030645161. The nearest-rounding interval for 22.5% is [22.45%,22.55%), excluding the exact quotient.

**Alternative source-grounded interpretations:** Truncation of the explicit 7/31 quotient gives the printed 22.5% and coherently reconciles the display. A differently defined denominator or a transcribed cell would require supporting information; the supplied row already specifies 31 and gives no replacement denominator. The actual display rule is missing, so no percentage correction is assigned.

**Mechanical evidence recheck:** The direct-source recheck matched the Failure cell, explicit 7/31 fraction, printed 22.5% and location, and reproduced the registered nearest-rounding comparison. The quotient inputs are available; the missing input is the calculation/display convention. State recorded_candidate retains that conditional question, with suggested retain disposition as a mechanical pre-fill for human review. The roles are REPORT/REPORT within Table 3; classification S_W was confirmed.

**Quality-control relevance:** Clarifying the kidney failure category percentage 22.5% or the explicit 7/31 denominator supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the kidney failure category percentage 22.5% or the explicit 7/31 denominator. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and confirm the Failure row and its explicit nested denominator 31.
2. Calculate 100×7/31 and compare nearest rounding with truncation.
3. Establish whether 22.5% was deliberately truncated or arose from a different documented denominator/display procedure.
4. Choose the documented interpretation for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C050 — Kidney loss,n/N(%): H printed percentage identity

**Candidate statement:** For the nested kidney loss category, the High PEEP cell 2/31 (6.4%) does not match nearest one-decimal rounding of its explicit quotient. Truncation reproduces the printed percentage, so this is a conditional display-rule question. Status: Pending Human Adjudication.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Loss count/denominator versus REPORT main article same-cell percentage; REPORT main article PDF p. 10 footnotes f/g define the row

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3 Acute kidney failure subcategory Loss, explicit High PEEP 2/31 (6.4%) cell compared with its own numerator/denominator; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>), footnotes f/g defining No./total No. and kidney stage categories.

**Source evidence:** Direct printed nested row: Loss; High PEEP 2/31 (6.4%); Low PEEP 2/32 (6.2%). No separate risk ratio or absolute difference is printed for this subcategory; the class comparison P .97 is shared by the kidney-stage block. The denominator here is explicitly 31 for High PEEP and 32 for Low PEEP, not the randomized reference population. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O29-PCT-H. Numeric relationship: N208.

**Reported-versus-comparator:** Reported High PEEP 6.4% versus 100×2/31=6.451612903%, nearest one-decimal 6.5%. The signed printed-minus-exact gap is -0.051612903 percentage point.

**Reasoning procedure:** Divide the explicit nested numerator 2 by its explicit denominator 31 and multiply by 100. Nearest one-decimal rounding permits 0.05 percentage point at a tie; the observed non-tie gap exceeds that bound. Applicability is conditional on nearest rounding. No requirement that rounded subcategory percentages sum exactly to 100 is imposed.

**Calculation:** 100×2/31=6.451612903%; nearest 6.5%; truncation 6.4%; printed 6.4%; absolute gap 0.051612903 percentage point, exceeding 0.05 by 0.001612903. The nearest-rounding interval for 6.4% is [6.35%,6.45%), excluding the exact quotient by only 0.001612903 percentage point. The Low PEEP 2/32=6.25% permits tie conventions displaying 6.2%; it is not an additional contradiction.

**Alternative source-grounded interpretations:** Truncation of the explicit 2/31 quotient gives the printed 6.4% and coherently reconciles the display. A differently defined denominator or a transcribed cell would require supporting information; the supplied row already specifies 31 and gives no replacement denominator. The actual display rule is missing, so no percentage correction is assigned.

**Mechanical evidence recheck:** The direct-source recheck matched the Loss cell, explicit 2/31 fraction, printed 6.4% and location, and reproduced the registered nearest-rounding comparison. The quotient inputs are available; the missing input is the calculation/display convention. State recorded_candidate retains that conditional question, with suggested retain disposition as a mechanical pre-fill for human review. The roles are REPORT/REPORT within Table 3; classification S_W was confirmed.

**Quality-control relevance:** Clarifying the kidney loss category percentage 6.4% or the explicit 2/31 denominator supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the kidney loss category percentage 6.4% or the explicit 2/31 denominator. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and confirm the Loss row and its explicit nested denominator 31.
2. Calculate 100×2/31 and compare nearest rounding with truncation.
3. Establish whether 6.4% was deliberately truncated or arose from a different documented denominator/display procedure.
4. Choose the documented interpretation for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C051 — Extrapulmonary infection: labeled RR versus printed patient risks

**Candidate statement:** For extrapulmonary infection, the printed risk ratio 1.11 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Extrapulmonary infection event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Extrapulmonary infection row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Extrapulmonary infection; 29(2.9); 23(2.3); 0.6(−0.8 to2.0); RR1.11(0.87 to1.42); .40. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O30-RR; checkers/statistical_pass_1.md :: RR-O30; checkers/cross_source_consistency.md :: XR22. Numeric relationship: N209.

**Reported-versus-comparator:** Reported risk ratio 1.11 (95% CI 0.87 to1.42) versus the derived clinical event-risk ratio (29/989)/(23/987)=1.258319778, nearest display 1.26. Printed-minus-derived=-0.148319778; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (29/989)/(23/987)=1.258319778; nearest 1.26; printed 1.11; signed gap -0.148319778. Reverse-conditioning diagnostic q=[29/(29+23)]/[(960)/(1924)]=1.117708333; nearest 1.12, truncation 1.11.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 29, Low PEEP 23, reference patients 989/987, risk ratio 1.11 (0.87 to1.42) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the extrapulmonary infection risk ratio 1.11, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the extrapulmonary infection risk ratio 1.11, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Extrapulmonary infection row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (29/989)/(23/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 1.11. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C052 — Hepatic failure: labeled RR versus printed patient risks

**Candidate statement:** For hepatic failure, the printed risk ratio 0.99 differs from nearest rounding of the count-defined High/Low event-risk ratio, but truncation of that clinical ratio itself reproduces 0.99. This remains a conditional display/definition question. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Hepatic failure event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Hepatic failure row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Hepatic failure; 9(0.9); 9(0.9); 0(−0.8 to0.8); RR0.99(0.63 to1.59); >.99. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O31-RR; checkers/statistical_pass_1.md :: RR-O31; checkers/cross_source_consistency.md :: XR23. Numeric relationship: N210.

**Reported-versus-comparator:** Reported risk ratio 0.99 (95% CI 0.63 to1.59) versus the derived clinical event-risk ratio (9/989)/(9/987)=0.997977755, nearest display 1.00. Printed-minus-derived=-0.007977755; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (9/989)/(9/987)=0.997977755; nearest 1.00; printed 0.99; signed gap -0.007977755. Reverse-conditioning diagnostic q=[9/(9+9)]/[(980)/(1958)]=0.998979592; nearest 1.00, truncation 0.99. Truncating the clinical ratio 0.997977755 itself gives 0.99.

**Alternative source-grounded interpretations:** Truncation of the clinical event-risk ratio itself reproduces 0.99, so reversed conditioning is not required to explain this display. The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 9, Low PEEP 9, reference patients 989/987, risk ratio 0.99 (0.63 to1.59) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. It also confirmed that clinical-ratio truncation reconciles the printed point. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the hepatic failure risk ratio 0.99, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the hepatic failure risk ratio 0.99, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Hepatic failure row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (9/989)/(9/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 0.99. Check specifically whether the clinical ratio was truncated to 0.99. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C053 — Coma: labeled RR versus printed patient risks

**Candidate statement:** For coma, the printed risk ratio 0.99 differs from nearest rounding of the count-defined High/Low event-risk ratio, but truncation of that clinical ratio itself reproduces 0.99. This remains a conditional display/definition question. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Coma event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Coma row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Coma; 2(0.2); 2(0.2); 0(−0.4 to0.4); RR0.99(0.37 to2.66); >.99. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O32-RR; checkers/statistical_pass_1.md :: RR-O32; checkers/cross_source_consistency.md :: XR24. Numeric relationship: N211.

**Reported-versus-comparator:** Reported risk ratio 0.99 (95% CI 0.37 to2.66) versus the derived clinical event-risk ratio (2/989)/(2/987)=0.997977755, nearest display 1.00. Printed-minus-derived=-0.007977755; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (2/989)/(2/987)=0.997977755; nearest 1.00; printed 0.99; signed gap -0.007977755. Reverse-conditioning diagnostic q=[2/(2+2)]/[(987)/(1972)]=0.998986829; nearest 1.00, truncation 0.99. Truncating the clinical ratio 0.997977755 itself gives 0.99.

**Alternative source-grounded interpretations:** Truncation of the clinical event-risk ratio itself reproduces 0.99, so reversed conditioning is not required to explain this display. The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 2, Low PEEP 2, reference patients 989/987, risk ratio 0.99 (0.37 to2.66) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. It also confirmed that clinical-ratio truncation reconciles the printed point. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the coma risk ratio 0.99, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the coma risk ratio 0.99, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Coma row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (2/989)/(2/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 0.99. Check specifically whether the clinical ratio was truncated to 0.99. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C054 — Disseminated intravascular coagulation: labeled RR versus printed patient risks

**Candidate statement:** For disseminated intravascular coagulation, Table 3 prints a finite risk ratio 2.00 although the printed Low PEEP event risk is zero. The crude High/Low event-risk quotient has no finite value; interpreting the reported estimate requires its point formula, outcome/reference orientation and zero-cell or fitted-estimator rule. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Disseminated intravascular coagulation event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Disseminated intravascular coagulation row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Disseminated intravascular coagulation; 1(0.1); 0; 0.1(−0.1 to0.3); RR2.00(1.91 to2.09); >.99. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O33-RR; checkers/statistical_pass_1.md :: RR-O33; checkers/cross_source_consistency.md :: XR25. Numeric relationship: N212.

**Reported-versus-comparator:** Reported risk ratio 2.00 (95% CI 1.91 to2.09) versus (1/989)/(0/987), which has no finite crude event-risk value because its denominator risk is zero. A finite fitted or corrected estimate requires an additional stated procedure.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** High event risk=1/989; Low event risk=0/987=0; their quotient is undefined as a finite number (unbounded in an extended ratio interpretation). No rounding tolerance can turn this crude quotient into 2.00. Diagnostic q=[1/(1+0)]/[(989−1)/(1976−1−0)]=1.998987854, nearest 2.00, truncation 1.99.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. Here q=1.998987854 nearest-rounds to 2.00 and truncates to 1.99. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. A continuity or fitted zero-cell procedure could provide a finite estimate but its exact rule and variance method are not supplied. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 1, Low PEEP 0, reference patients 989/987, risk ratio 2.00 (1.91 to2.09) and the method/footnote locations. It reproduced the registered nonfinite crude quotient versus finite reported-point comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions, together with the zero-cell and variance procedures. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the disseminated intravascular coagulation risk ratio 2.00, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the disseminated intravascular coagulation risk ratio 2.00, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Disseminated intravascular coagulation row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (1/989)/(0/987) and identify the zero-denominator issue; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, zero-cell rule, variance method, fitted adjustment and display convention produced 2.00. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C055 — Impaired postoperative wound healing: labeled RR versus printed patient risks

Pending Human Adjudication.

**Candidate statement:** The labeled RR 0.91 does not equal the crude High/Low event-risk ratio from the printed counts under nearest two-decimal rounding. Whether it represents a different fitted or conditioned estimand remains unresolved.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Impaired postoperative wound healing event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](../jama_bluth_2019_oi_190055_16092.pdf#page=9); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10). The compared row and its context are identified in Compared document roles.

**Source evidence:** H 22/989; L 26/987; printed RR0.91(0.66 to1.24). Complete source-row components: Impaired postoperative wound healing; 22(2.2); 26(2.6); −0.4(−1.8 to0.9); RR0.91(0.66 to1.24); .55.

**Reported-versus-comparator:** (22/989)/(26/987) = 0.844443; nearest two-decimal display 0.84; printed RR 0.91 differs by 0.065557.

**Reasoning procedure:** Divide the printed High PEEP event risk by the printed Low PEEP event risk. Integer counts and denominators are exact; nearest two-decimal comparison uses tolerance 0.005. The arithmetic is a diagnostic comparator and does not replace a fitted estimate. Table 3 footnotes describe reference patients, RR labeling, Wald likelihood-ratio approximation and χ² P tests; they do not supply the exact row-point estimator. CI and P are not assumed to share a particular test.

**Calculation:** (22/989)/(26/987)=0.844443, nearest two decimals 0.84; printed minus diagnostic=0.065557. Absolute discrepancy exceeds 0.005. q=[22/(22+26)]/[(989−22)/(989+987−22−26)]=0.913823 is reverse conditioning of treatment allocation on event status, not the High/Low event risk contrast. All arithmetic agrees with the current recheck. q similarity does not establish table transposition or the production estimator.

**Alternative source-grounded interpretations:** An adjusted or standardized estimate, a differently oriented/reference-coded contrast, or a different row denominator could explain the display only if supported by the original estimator definition. Row-specific estimator, orientation, adjustment and display procedure are not supplied. All four event/nonevent cells are positive, so a generic zero-cell explanation does not reconcile this comparison. Reverse-conditioned q is a different estimand and establishes no author coding or production mechanism.

**Mechanical evidence recheck:** The directly confirmed event counts and denominators yield 0.844443, outside the nearest-rounding interval for printed 0.91. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain. Source-matched recheck and audit confirmed the count/point tuple and reproduced the diagnostic. The remaining question is the named estimator definition.

**Quality-control relevance:** This is a quantitative reporting consistency question tied to a printed number, measure, endpoint or calculation convention. The suggested review disposition is a mechanical pre-fill for human review, not an adjudication.

**Potential downstream evidence impact:** If a label/estimand discrepancy is confirmed, an extractor could copy the point estimate as a crude event RR or pair it with the displayed counts under an inappropriate estimand. Small preventable reporting defects can matter for downstream evidence extraction. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:** Inspect the original row output and variable coding; identify event orientation, reference group, denominator, estimator, any adjustment and display procedure that produced 0.91; determine whether the printed RR purports to equal the displayed High/Low event-risk contrast; document the actual estimand for extraction.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C056 — Unexpected ICU admission/readmission: labeled RR versus printed patient risks

Pending Human Adjudication.

**Candidate statement:** The labeled RR 1.12 does not equal the crude High/Low event-risk ratio from the printed counts under nearest two-decimal rounding. Whether it represents a different fitted or conditioned estimand remains unresolved.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Unexpected need for ICU admission or readmission event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](../jama_bluth_2019_oi_190055_16092.pdf#page=9); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10). The compared row and its context are identified in Compared document roles.

**Source evidence:** H 41/989; L 32/987; printed RR1.12(0.91 to1.38). Complete source-row components: UnexpectedICU admission/readmission; 41(4.1); 32(3.2); 0.9(−0.8 to2.6); RR1.12(0.91 to1.38); .29.

**Reported-versus-comparator:** (41/989)/(32/987) = 1.278659; nearest two-decimal display 1.28; printed RR 1.12 differs by -0.158659.

**Reasoning procedure:** Divide the printed High PEEP event risk by the printed Low PEEP event risk. Integer counts and denominators are exact; nearest two-decimal comparison uses tolerance 0.005. The arithmetic is a diagnostic comparator and does not replace a fitted estimate. Table 3 footnotes describe reference patients, RR labeling, Wald likelihood-ratio approximation and χ² P tests; they do not supply the exact row-point estimator. CI and P are not assumed to share a particular test.

**Calculation:** (41/989)/(32/987)=1.278659, nearest two decimals 1.28; printed minus diagnostic=-0.158659. Absolute discrepancy exceeds 0.005. q=[41/(41+32)]/[(989−41)/(989+987−41−32)]=1.127435 is reverse conditioning of treatment allocation on event status, not the High/Low event risk contrast. All arithmetic agrees with the current recheck. q similarity does not establish table transposition or the production estimator.

**Alternative source-grounded interpretations:** An adjusted or standardized estimate, a differently oriented/reference-coded contrast, or a different row denominator could explain the display only if supported by the original estimator definition. Row-specific estimator, orientation, adjustment and display procedure are not supplied. All four event/nonevent cells are positive, so a generic zero-cell explanation does not reconcile this comparison. Reverse-conditioned q is a different estimand and establishes no author coding or production mechanism.

**Mechanical evidence recheck:** The directly confirmed event counts and denominators yield 1.278659, outside the nearest-rounding interval for printed 1.12. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain. Source-matched recheck and audit confirmed the count/point tuple and reproduced the diagnostic. The remaining question is the named estimator definition.

**Quality-control relevance:** This is a quantitative reporting consistency question tied to a printed number, measure, endpoint or calculation convention. The suggested review disposition is a mechanical pre-fill for human review, not an adjudication.

**Potential downstream evidence impact:** If a label/estimand discrepancy is confirmed, an extractor could copy the point estimate as a crude event RR or pair it with the displayed counts under an inappropriate estimand. Small preventable reporting defects can matter for downstream evidence extraction. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:** Inspect the original row output and variable coding; identify event orientation, reference group, denominator, estimator, any adjustment and display procedure that produced 1.12; determine whether the printed RR purports to equal the displayed High/Low event-risk contrast; document the actual estimand for extraction.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C057 — Intraoperative hypoxemia: labeled RR versus printed patient risks

Pending Human Adjudication.

**Candidate statement:** The labeled RR 0.51 does not equal the crude High/Low event-risk ratio from the printed counts under nearest two-decimal rounding. Whether it represents a different fitted or conditioned estimand remains unresolved.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Intraoperative hypoxemia event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](../jama_bluth_2019_oi_190055_16092.pdf#page=9); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10). The compared row and its context are identified in Compared document roles.

**Source evidence:** H 49/989; L 134/987; printed RR0.51(0.40 to0.65). Complete source-row components: Intraoperative hypoxemia; 49(5.0); 134(13.6); −8.6(−11.1 to−6.1); RR0.51(0.40 to0.65); <.001.

**Reported-versus-comparator:** (49/989)/(134/987) = 0.364932; nearest two-decimal display 0.36; printed RR 0.51 differs by 0.145068.

**Reasoning procedure:** Divide the printed High PEEP event risk by the printed Low PEEP event risk. Integer counts and denominators are exact; nearest two-decimal comparison uses tolerance 0.005. The arithmetic is a diagnostic comparator and does not replace a fitted estimate. Table 3 footnotes describe reference patients, RR labeling, Wald likelihood-ratio approximation and χ² P tests; they do not supply the exact row-point estimator. CI and P are not assumed to share a particular test.

**Calculation:** (49/989)/(134/987)=0.364932, nearest two decimals 0.36; printed minus diagnostic=0.145068. Absolute discrepancy exceeds 0.005. q=[49/(49+134)]/[(989−49)/(989+987−49−134)]=0.510737 is reverse conditioning of treatment allocation on event status, not the High/Low event risk contrast. All arithmetic agrees with the current recheck. q similarity does not establish table transposition or the production estimator.

**Alternative source-grounded interpretations:** An adjusted or standardized estimate, a differently oriented/reference-coded contrast, or a different row denominator could explain the display only if supported by the original estimator definition. Row-specific estimator, orientation, adjustment and display procedure are not supplied. All four event/nonevent cells are positive, so a generic zero-cell explanation does not reconcile this comparison. Reverse-conditioned q is a different estimand and establishes no author coding or production mechanism.

**Mechanical evidence recheck:** The directly confirmed event counts and denominators yield 0.364932, outside the nearest-rounding interval for printed 0.51. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain. Source-matched recheck and audit confirmed the count/point tuple and reproduced the diagnostic. The remaining question is the named estimator definition.

**Quality-control relevance:** This is a quantitative reporting consistency question tied to a printed number, measure, endpoint or calculation convention. The suggested review disposition is a mechanical pre-fill for human review, not an adjudication.

**Potential downstream evidence impact:** If a label/estimand discrepancy is confirmed, an extractor could copy the point estimate as a crude event RR or pair it with the displayed counts under an inappropriate estimand. Small preventable reporting defects can matter for downstream evidence extraction. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:** Inspect the original row output and variable coding; identify event orientation, reference group, denominator, estimator, any adjustment and display procedure that produced 0.51; determine whether the printed RR purports to equal the displayed High/Low event-risk contrast; document the actual estimand for extraction.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C058 — Intraoperative hypotension: labeled RR versus printed patient risks

Pending Human Adjudication.

**Candidate statement:** The labeled RR 1.43 does not equal the crude High/Low event-risk ratio from the printed counts under nearest two-decimal rounding. Whether it represents a different fitted or conditioned estimand remains unresolved.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Intraoperative hypotension event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](../jama_bluth_2019_oi_190055_16092.pdf#page=9); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10). The compared row and its context are identified in Compared document roles.

**Source evidence:** H 313/989; L 170/987; printed RR1.43(1.31 to1.56). Complete source-row components: Intraoperative hypotension; 313(31.6); 170(17.2); 14.4(10.7 to18.2); RR1.43(1.31 to1.56); <.001.

**Reported-versus-comparator:** (313/989)/(170/987) = 1.837453; nearest two-decimal display 1.84; printed RR 1.43 differs by -0.407453.

**Reasoning procedure:** Divide the printed High PEEP event risk by the printed Low PEEP event risk. Integer counts and denominators are exact; nearest two-decimal comparison uses tolerance 0.005. The arithmetic is a diagnostic comparator and does not replace a fitted estimate. Table 3 footnotes describe reference patients, RR labeling, Wald likelihood-ratio approximation and χ² P tests; they do not supply the exact row-point estimator. CI and P are not assumed to share a particular test.

**Calculation:** (313/989)/(170/987)=1.837453, nearest two decimals 1.84; printed minus diagnostic=-0.407453. Absolute discrepancy exceeds 0.005. q=[313/(313+170)]/[(989−313)/(989+987−313−170)]=1.431233 is reverse conditioning of treatment allocation on event status, not the High/Low event risk contrast. All arithmetic agrees with the current recheck. q similarity does not establish table transposition or the production estimator.

**Alternative source-grounded interpretations:** An adjusted or standardized estimate, a differently oriented/reference-coded contrast, or a different row denominator could explain the display only if supported by the original estimator definition. Row-specific estimator, orientation, adjustment and display procedure are not supplied. All four event/nonevent cells are positive, so a generic zero-cell explanation does not reconcile this comparison. Reverse-conditioned q is a different estimand and establishes no author coding or production mechanism.

**Mechanical evidence recheck:** The directly confirmed event counts and denominators yield 1.837453, outside the nearest-rounding interval for printed 1.43. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain. Source-matched recheck and audit confirmed the count/point tuple and reproduced the diagnostic. The remaining question is the named estimator definition.

**Quality-control relevance:** This is a quantitative reporting consistency question tied to a printed number, measure, endpoint or calculation convention. The suggested review disposition is a mechanical pre-fill for human review, not an adjudication.

**Potential downstream evidence impact:** If a label/estimand discrepancy is confirmed, an extractor could copy the point estimate as a crude event RR or pair it with the displayed counts under an inappropriate estimand. Small preventable reporting defects can matter for downstream evidence extraction. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:** Inspect the original row output and variable coding; identify event orientation, reference group, denominator, estimator, any adjustment and display procedure that produced 1.43; determine whether the printed RR purports to equal the displayed High/Low event-risk contrast; document the actual estimand for extraction.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C059 — Intraoperative bradycardia: labeled RR versus printed patient risks

Pending Human Adjudication.

**Candidate statement:** The labeled RR 1.27 does not equal the crude High/Low event-risk ratio from the printed counts under nearest two-decimal rounding. Whether it represents a different fitted or conditioned estimand remains unresolved.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Intraoperative bradycardia event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](../jama_bluth_2019_oi_190055_16092.pdf#page=9); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10). The compared row and its context are identified in Compared document roles.

**Source evidence:** H 98/989; L 59/987; printed RR1.27(1.11 to1.45). Complete source-row components: Intraoperative bradycardia; 98(9.9); 59(6.0); 3.9(1.5 to6.3); RR1.27(1.11 to1.45); .001.

**Reported-versus-comparator:** (98/989)/(59/987) = 1.657658; nearest two-decimal display 1.66; printed RR 1.27 differs by -0.387658.

**Reasoning procedure:** Divide the printed High PEEP event risk by the printed Low PEEP event risk. Integer counts and denominators are exact; nearest two-decimal comparison uses tolerance 0.005. The arithmetic is a diagnostic comparator and does not replace a fitted estimate. Table 3 footnotes describe reference patients, RR labeling, Wald likelihood-ratio approximation and χ² P tests; they do not supply the exact row-point estimator. CI and P are not assumed to share a particular test.

**Calculation:** (98/989)/(59/987)=1.657658, nearest two decimals 1.66; printed minus diagnostic=-0.387658. Absolute discrepancy exceeds 0.005. q=[98/(98+59)]/[(989−98)/(989+987−98−59)]=1.274329 is reverse conditioning of treatment allocation on event status, not the High/Low event risk contrast. All arithmetic agrees with the current recheck. q similarity does not establish table transposition or the production estimator.

**Alternative source-grounded interpretations:** An adjusted or standardized estimate, a differently oriented/reference-coded contrast, or a different row denominator could explain the display only if supported by the original estimator definition. Row-specific estimator, orientation, adjustment and display procedure are not supplied. All four event/nonevent cells are positive, so a generic zero-cell explanation does not reconcile this comparison. Reverse-conditioned q is a different estimand and establishes no author coding or production mechanism.

**Mechanical evidence recheck:** The directly confirmed event counts and denominators yield 1.657658, outside the nearest-rounding interval for printed 1.27. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain. Source-matched recheck and audit confirmed the count/point tuple and reproduced the diagnostic. The remaining question is the named estimator definition.

**Quality-control relevance:** This is a quantitative reporting consistency question tied to a printed number, measure, endpoint or calculation convention. The suggested review disposition is a mechanical pre-fill for human review, not an adjudication.

**Potential downstream evidence impact:** If a label/estimand discrepancy is confirmed, an extractor could copy the point estimate as a crude event RR or pair it with the displayed counts under an inappropriate estimand. Small preventable reporting defects can matter for downstream evidence extraction. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:** Inspect the original row output and variable coding; identify event orientation, reference group, denominator, estimator, any adjustment and display procedure that produced 1.27; determine whether the printed RR purports to equal the displayed High/Low event-risk contrast; document the actual estimand for extraction.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C060 — Mortality during hospital stay: labeled RR versus printed patient risks

Pending Human Adjudication.

**Candidate statement:** The labeled RR 1.41 does not equal the crude High/Low event-risk ratio from the printed counts under nearest two-decimal rounding. Whether it represents a different fitted or conditioned estimand remains unresolved.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Mortality during hospital stay event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](../jama_bluth_2019_oi_190055_16092.pdf#page=9); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10). The compared row and its context are identified in Compared document roles.

**Source evidence:** H 12/989; L 5/987; printed RR1.41(0.95 to1.81). Complete source-row components: Mortality during hospital stay; 12(1.2); 5(0.5); 0.7(−0.1 to1.5); RR1.41(0.95 to1.81); .09.

**Reported-versus-comparator:** (12/989)/(5/987) = 2.395147; nearest two-decimal display 2.40; printed RR 1.41 differs by -0.985147.

**Reasoning procedure:** Divide the printed High PEEP event risk by the printed Low PEEP event risk. Integer counts and denominators are exact; nearest two-decimal comparison uses tolerance 0.005. The arithmetic is a diagnostic comparator and does not replace a fitted estimate. Table 3 footnotes describe reference patients, RR labeling, Wald likelihood-ratio approximation and χ² P tests; they do not supply the exact row-point estimator. CI and P are not assumed to share a particular test.

**Calculation:** (12/989)/(5/987)=2.395147, nearest two decimals 2.40; printed minus diagnostic=-0.985147. Absolute discrepancy exceeds 0.005. q=[12/(12+5)]/[(989−12)/(989+987−12−5)]=1.415377 is reverse conditioning of treatment allocation on event status, not the High/Low event risk contrast. All arithmetic agrees with the current recheck. q similarity does not establish table transposition or the production estimator.

**Alternative source-grounded interpretations:** An adjusted or standardized estimate, a differently oriented/reference-coded contrast, or a different row denominator could explain the display only if supported by the original estimator definition. Row-specific estimator, orientation, adjustment and display procedure are not supplied. All four event/nonevent cells are positive, so a generic zero-cell explanation does not reconcile this comparison. Reverse-conditioned q is a different estimand and establishes no author coding or production mechanism.

**Mechanical evidence recheck:** The directly confirmed event counts and denominators yield 2.395147, outside the nearest-rounding interval for printed 1.41. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain. Source-matched recheck and audit confirmed the count/point tuple and reproduced the diagnostic. The remaining question is the named estimator definition.

**Quality-control relevance:** This is a quantitative reporting consistency question tied to a printed number, measure, endpoint or calculation convention. The suggested review disposition is a mechanical pre-fill for human review, not an adjudication.

**Potential downstream evidence impact:** If a label/estimand discrepancy is confirmed, an extractor could copy the point estimate as a crude event RR or pair it with the displayed counts under an inappropriate estimand. Small preventable reporting defects can matter for downstream evidence extraction. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:** Inspect the original row output and variable coding; identify event orientation, reference group, denominator, estimator, any adjustment and display procedure that produced 1.41; determine whether the printed RR purports to equal the displayed High/Low event-risk contrast; document the actual estimand for extraction.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C061 — Post hoc rescue strategy for desaturation: absolute difference versus exact printed risks

Pending Human Adjudication.

**Candidate statement:** The printed rescue-strategy absolute difference −10.8 percentage points differs from nearest rounding of the exact displayed count-defined risks; displayed-percentage subtraction and truncation reconcile it.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 continued rescue-strategy counts/denominators versus REPORT main article same row Absolute Difference; REPORT main article footnote a supplies reference-denominator context

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10). The cited source, Table3, prints59(6.0%)/989 and166(16.8%)/987 with−10.8(−13.6 to−8.1) percentage points. Recheck matches exact cells and physical pagination.

**Source evidence:** High PEEP 59/989 (6.0%); Low PEEP 166/987 (16.8%); absolute difference −10.8 (−13.6 to −8.1) percentage points; RR 0.49 (0.39–0.62); P <.001.

**Reported-versus-comparator:** Printed −10.8 versus exact-risk difference −10.853021 percentage points, nearest one-decimal −10.9; printed-percentage subtraction gives −10.8.

**Reasoning procedure:** Compute 100 × (High events/High patients − Low events/Low patients), and compare under nearest one-decimal rounding. The conditional tolerance is 0.05 percentage point, not the 0.15 bound for subtraction of two rounded inputs.

**Calculation:** 100 × (59/989 − 166/987) = −10.853021 percentage points; printed minus exact = +0.053021. The approximate rounding interval [−10.85, −10.75) excludes the exact difference. 6.0 − 16.8 = −10.8.

**Alternative source-grounded interpretations:** Subtracting displayed percentages or truncating the exact difference toward zero gives −10.8. A different denominator or fitted estimand is possible but unreported. No universally specified rounding convention establishes an unconditional defect.

**Mechanical evidence recheck:** The direct source confirms the registered cells and −10.8 difference. Exact count-based nearest rounding gives −10.9, but displayed-percentage subtraction/truncation gives −10.8; the original conditional display question remains. Evidence state recorded_candidate, mechanical suggestion retain. Current source recheck and assigned audit confirm the printed facts above; the evidence state reflects the limits of the comparator. Exact remaining human question: Inspect the original rescue-row calculation and unrounded output; determine whether −10.8 uses rounded percentages, truncation, or another denominator/estimand; document the calculation and display convention for extraction.

**Quality-control relevance:** This is a quantitative reporting consistency question tied to a printed number, measure, endpoint or calculation convention. The suggested review disposition is a mechanical pre-fill for human review, not an adjudication.

**Potential downstream evidence impact:** If confirmed, an extractor could copy an absolute difference without its calculation/display convention. Small preventable reporting defects can matter for downstream evidence extraction. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:** Inspect the original rescue-row calculation and unrounded output; determine whether −10.8 uses rounded percentages, truncation, or another denominator/estimand; document the calculation and display convention for extraction.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C062 — Post hoc rescue strategy for desaturation: labeled RR versus printed patient risks

Pending Human Adjudication.

**Candidate statement:** The labeled RR 0.49 does not equal the crude High/Low event-risk ratio from the printed counts under nearest two-decimal rounding. Whether it represents a different fitted or conditioned estimand remains unresolved.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Post hoc rescue strategy for desaturation event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10). The compared row and its context are identified in Compared document roles.

**Source evidence:** H 59/989; L 166/987; printed RR0.49(0.39 to0.62). Complete source-row components: Post hoc rescue strategy for desaturation; 59(6.0); 166(16.8); −10.8(−13.6 to−8.1); RR0.49(0.39 to0.62); <.001.

**Reported-versus-comparator:** (59/989)/(166/987) = 0.354703; nearest two-decimal display 0.35; printed RR 0.49 differs by 0.135297.

**Reasoning procedure:** Divide the printed High PEEP event risk by the printed Low PEEP event risk. Integer counts and denominators are exact; nearest two-decimal comparison uses tolerance 0.005. The arithmetic is a diagnostic comparator and does not replace a fitted estimate. Table 3 footnotes describe reference patients, RR labeling, Wald likelihood-ratio approximation and χ² P tests; they do not supply the exact row-point estimator. CI and P are not assumed to share a particular test.

**Calculation:** (59/989)/(166/987)=0.354703, nearest two decimals 0.35; printed minus diagnostic=0.135297. Absolute discrepancy exceeds 0.005. q=[59/(59+166)]/[(989−59)/(989+987−59−166)]=0.493711 is reverse conditioning of treatment allocation on event status, not the High/Low event risk contrast. All arithmetic agrees with the current recheck. q similarity does not establish table transposition or the production estimator.

**Alternative source-grounded interpretations:** An adjusted or standardized estimate, a differently oriented/reference-coded contrast, or a different row denominator could explain the display only if supported by the original estimator definition. Row-specific estimator, orientation, adjustment and display procedure are not supplied. All four event/nonevent cells are positive, so a generic zero-cell explanation does not reconcile this comparison. Reverse-conditioned q is a different estimand and establishes no author coding or production mechanism.

**Mechanical evidence recheck:** The directly confirmed event counts and denominators yield 0.354703, outside the nearest-rounding interval for printed 0.49. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain. Source-matched recheck and audit confirmed the count/point tuple and reproduced the diagnostic. The remaining question is the named estimator definition.

**Quality-control relevance:** This is a quantitative reporting consistency question tied to a printed number, measure, endpoint or calculation convention. The suggested review disposition is a mechanical pre-fill for human review, not an adjudication.

**Potential downstream evidence impact:** If a label/estimand discrepancy is confirmed, an extractor could copy the point estimate as a crude event RR or pair it with the displayed counts under an inappropriate estimand. Small preventable reporting defects can matter for downstream evidence extraction. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:** Inspect the original row output and variable coding; identify event orientation, reference group, denominator, estimator, any adjustment and display procedure that produced 0.49; determine whether the printed RR purports to equal the displayed High/Low event-risk contrast; document the actual estimand for extraction.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C063 — Post hoc vasoactive drugs: labeled RR versus printed patient risks

Pending Human Adjudication.

**Candidate statement:** The labeled RR 1.10 does not equal the crude High/Low event-risk ratio from the printed counts under nearest two-decimal rounding. Whether it represents a different fitted or conditioned estimand remains unresolved.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Post hoc need for vasoactive drugs event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10). The compared row and its context are identified in Compared document roles.

**Source evidence:** H 491/989; L 439/987; printed RR1.10(1.01 to1.21). Complete source-row components: Post hoc vasoactive drugs; 491(49.6); 439(44.5); 5.2(0.8 to9.6); RR1.10(1.01 to1.21); .02.

**Reported-versus-comparator:** (491/989)/(439/987) = 1.116189; nearest two-decimal display 1.12; printed RR 1.10 differs by -0.016189.

**Reasoning procedure:** Divide the printed High PEEP event risk by the printed Low PEEP event risk. Integer counts and denominators are exact; nearest two-decimal comparison uses tolerance 0.005. The arithmetic is a diagnostic comparator and does not replace a fitted estimate. Table 3 footnotes describe reference patients, RR labeling, Wald likelihood-ratio approximation and χ² P tests; they do not supply the exact row-point estimator. CI and P are not assumed to share a particular test.

**Calculation:** (491/989)/(439/987)=1.116189, nearest two decimals 1.12; printed minus diagnostic=-0.016189. Absolute discrepancy exceeds 0.005. q=[491/(491+439)]/[(989−491)/(989+987−491−439)]=1.108922 is reverse conditioning of treatment allocation on event status, not the High/Low event risk contrast. All arithmetic agrees with the current recheck. q similarity does not establish table transposition or the production estimator.

**Alternative source-grounded interpretations:** An adjusted or standardized estimate, a differently oriented/reference-coded contrast, or a different row denominator could explain the display only if supported by the original estimator definition. Row-specific estimator, orientation, adjustment and display procedure are not supplied. All four event/nonevent cells are positive, so a generic zero-cell explanation does not reconcile this comparison. Reverse-conditioned q is a different estimand and establishes no author coding or production mechanism.

**Mechanical evidence recheck:** The directly confirmed event counts and denominators yield 1.116189, outside the nearest-rounding interval for printed 1.10. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain. Source-matched recheck and audit confirmed the count/point tuple and reproduced the diagnostic. The remaining question is the named estimator definition.

**Quality-control relevance:** This is a quantitative reporting consistency question tied to a printed number, measure, endpoint or calculation convention. The suggested review disposition is a mechanical pre-fill for human review, not an adjudication.

**Potential downstream evidence impact:** If a label/estimand discrepancy is confirmed, an extractor could copy the point estimate as a crude event RR or pair it with the displayed counts under an inappropriate estimand. Small preventable reporting defects can matter for downstream evidence extraction. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:** Inspect the original row output and variable coding; identify event orientation, reference group, denominator, estimator, any adjustment and display procedure that produced 1.10; determine whether the printed RR purports to equal the displayed High/Low event-risk contrast; document the actual estimand for extraction.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C064 — Nonlaparoscopic: labeled RR versus printed patient risks

Pending Human Adjudication.

**Candidate statement:** The labeled RR 1.09 does not equal the crude High/Low event-risk ratio from the printed counts under nearest two-decimal rounding. Whether it represents a different fitted or conditioned estimand remains unresolved.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Figure 2 Nonlaparoscopic surgery event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Methods PDF p. 4 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](../jama_bluth_2019_oi_190055_16092.pdf#page=4). The compared row and its context are identified in Compared document roles.

**Source evidence:** H 79/240; L 74/253; printed 1.09(0.90-1.32). Complete source-row components: Nonlaparoscopic; 79/240; 74/253; 1.09(0.90-1.32); .08 shared withF02.

**Reported-versus-comparator:** (79/240)/(74/253) = 1.125394; nearest two-decimal display 1.13; printed RR 1.09 differs by -0.035394.

**Reasoning procedure:** Divide the printed High PEEP event risk by the printed Low PEEP event risk. Integer counts and denominators are exact; nearest two-decimal comparison uses tolerance 0.005. The arithmetic is a diagnostic comparator and does not replace a fitted estimate. Methods p.4 concerns binomial GLM treatment-by-subgroup heterogeneity; it does not identify the plotted row-point estimator. The interaction P value is not paired with the row CI as a common test.

**Calculation:** (79/240)/(74/253)=1.125394, nearest two decimals 1.13; printed minus diagnostic=-0.035394. Absolute discrepancy exceeds 0.005. q=[79/(79+74)]/[(240−79)/(240+253−79−74)]=1.090407 is reverse conditioning of treatment allocation on event status, not the High/Low event risk contrast. All arithmetic agrees with the current recheck. q similarity does not establish table transposition or the production estimator.

**Alternative source-grounded interpretations:** An adjusted or standardized estimate, a differently oriented/reference-coded contrast, or a different row denominator could explain the display only if supported by the original estimator definition. Row-specific estimator, orientation, adjustment and display procedure are not supplied. All four event/nonevent cells are positive, so a generic zero-cell explanation does not reconcile this comparison. Reverse-conditioned q is a different estimand and establishes no author coding or production mechanism.

**Mechanical evidence recheck:** The directly confirmed event counts and denominators yield 1.125394, outside the nearest-rounding interval for printed 1.09. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain. Source-matched recheck and audit confirmed the count/point tuple and reproduced the diagnostic. The remaining question is the named estimator definition.

**Quality-control relevance:** This is a quantitative reporting consistency question tied to a printed number, measure, endpoint or calculation convention. The suggested review disposition is a mechanical pre-fill for human review, not an adjudication.

**Potential downstream evidence impact:** If a label/estimand discrepancy is confirmed, an extractor could copy the point estimate as a crude event RR or pair it with the displayed counts under an inappropriate estimand. Small preventable reporting defects can matter for downstream evidence extraction. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:** Inspect the original row output and variable coding; identify event orientation, reference group, denominator, estimator, any adjustment and display procedure that produced 1.09; determine whether the printed RR purports to equal the displayed High/Low event-risk contrast; document the actual estimand for extraction.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C065 — Laparoscopic: labeled RR versus printed patient risks

Pending Human Adjudication.

**Candidate statement:** The labeled RR 0.88 does not equal the crude High/Low event-risk ratio from the printed counts under nearest two-decimal rounding. Whether it represents a different fitted or conditioned estimand remains unresolved.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Figure 2 Laparoscopic surgery event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Methods PDF p. 4 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](../jama_bluth_2019_oi_190055_16092.pdf#page=4). The compared row and its context are identified in Compared document roles.

**Source evidence:** H 130/740; L 156/727; printed 0.88(0.77-1.01). Complete source-row components: Laparoscopic; 130/740; 156/727; 0.88(0.77-1.01); same.08.

**Reported-versus-comparator:** (130/740)/(156/727) = 0.818694; nearest two-decimal display 0.82; printed RR 0.88 differs by 0.061306.

**Reasoning procedure:** Divide the printed High PEEP event risk by the printed Low PEEP event risk. Integer counts and denominators are exact; nearest two-decimal comparison uses tolerance 0.005. The arithmetic is a diagnostic comparator and does not replace a fitted estimate. Methods p.4 concerns binomial GLM treatment-by-subgroup heterogeneity; it does not identify the plotted row-point estimator. The interaction P value is not paired with the row CI as a common test.

**Calculation:** (130/740)/(156/727)=0.818694, nearest two decimals 0.82; printed minus diagnostic=0.061306. Absolute discrepancy exceeds 0.005. q=[130/(130+156)]/[(740−130)/(740+727−130−156)]=0.880030 is reverse conditioning of treatment allocation on event status, not the High/Low event risk contrast. All arithmetic agrees with the current recheck. q similarity does not establish table transposition or the production estimator.

**Alternative source-grounded interpretations:** An adjusted or standardized estimate, a differently oriented/reference-coded contrast, or a different row denominator could explain the display only if supported by the original estimator definition. Row-specific estimator, orientation, adjustment and display procedure are not supplied. All four event/nonevent cells are positive, so a generic zero-cell explanation does not reconcile this comparison. Reverse-conditioned q is a different estimand and establishes no author coding or production mechanism.

**Mechanical evidence recheck:** The directly confirmed event counts and denominators yield 0.818694, outside the nearest-rounding interval for printed 0.88. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain. Source-matched recheck and audit confirmed the count/point tuple and reproduced the diagnostic. The remaining question is the named estimator definition.

**Quality-control relevance:** This is a quantitative reporting consistency question tied to a printed number, measure, endpoint or calculation convention. The suggested review disposition is a mechanical pre-fill for human review, not an adjudication.

**Potential downstream evidence impact:** If a label/estimand discrepancy is confirmed, an extractor could copy the point estimate as a crude event RR or pair it with the displayed counts under an inappropriate estimand. Small preventable reporting defects can matter for downstream evidence extraction. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:** Inspect the original row output and variable coding; identify event orientation, reference group, denominator, estimator, any adjustment and display procedure that produced 0.88; determine whether the printed RR purports to equal the displayed High/Low event-risk contrast; document the actual estimand for extraction.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C066 — BMI<40: labeled RR versus printed patient risks

Pending Human Adjudication.

**Candidate statement:** The labeled RR 0.93 does not equal the crude High/Low event-risk ratio from the printed counts under nearest two-decimal rounding. Whether it represents a different fitted or conditioned estimand remains unresolved.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Figure 2 Body mass index <40 event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Methods PDF p. 4 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](../jama_bluth_2019_oi_190055_16092.pdf#page=4). The compared row and its context are identified in Compared document roles.

**Source evidence:** H 76/336; L 94/376; printed 0.93(0.77-1.13). Complete source-row components: BMI<40; 76/336; 94/376; 0.93(0.77-1.13); .97 shared withF04.

**Reported-versus-comparator:** (76/336)/(94/376) = 0.904762; nearest two-decimal display 0.90; printed RR 0.93 differs by 0.025238.

**Reasoning procedure:** Divide the printed High PEEP event risk by the printed Low PEEP event risk. Integer counts and denominators are exact; nearest two-decimal comparison uses tolerance 0.005. The arithmetic is a diagnostic comparator and does not replace a fitted estimate. Methods p.4 concerns binomial GLM treatment-by-subgroup heterogeneity; it does not identify the plotted row-point estimator. The interaction P value is not paired with the row CI as a common test.

**Calculation:** (76/336)/(94/376)=0.904762, nearest two decimals 0.90; printed minus diagnostic=0.025238. Absolute discrepancy exceeds 0.005. q=[76/(76+94)]/[(336−76)/(336+376−76−94)]=0.931946 is reverse conditioning of treatment allocation on event status, not the High/Low event risk contrast. All arithmetic agrees with the current recheck. q similarity does not establish table transposition or the production estimator.

**Alternative source-grounded interpretations:** An adjusted or standardized estimate, a differently oriented/reference-coded contrast, or a different row denominator could explain the display only if supported by the original estimator definition. Row-specific estimator, orientation, adjustment and display procedure are not supplied. All four event/nonevent cells are positive, so a generic zero-cell explanation does not reconcile this comparison. Reverse-conditioned q is a different estimand and establishes no author coding or production mechanism.

**Mechanical evidence recheck:** The directly confirmed event counts and denominators yield 0.904762, outside the nearest-rounding interval for printed 0.93. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain. Source-matched recheck and audit confirmed the count/point tuple and reproduced the diagnostic. The remaining question is the named estimator definition.

**Quality-control relevance:** This is a quantitative reporting consistency question tied to a printed number, measure, endpoint or calculation convention. The suggested review disposition is a mechanical pre-fill for human review, not an adjudication.

**Potential downstream evidence impact:** If a label/estimand discrepancy is confirmed, an extractor could copy the point estimate as a crude event RR or pair it with the displayed counts under an inappropriate estimand. Small preventable reporting defects can matter for downstream evidence extraction. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:** Inspect the original row output and variable coding; identify event orientation, reference group, denominator, estimator, any adjustment and display procedure that produced 0.93; determine whether the printed RR purports to equal the displayed High/Low event-risk contrast; document the actual estimand for extraction.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C067 — BMI≥40: labeled RR versus printed patient risks

Pending Human Adjudication.

**Candidate statement:** The labeled RR 0.94 does not equal the crude High/Low event-risk ratio from the printed counts under nearest two-decimal rounding. Whether it represents a different fitted or conditioned estimand remains unresolved.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Figure 2 Body mass index ≥40 event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Methods PDF p. 4 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](../jama_bluth_2019_oi_190055_16092.pdf#page=4). The compared row and its context are identified in Compared document roles.

**Source evidence:** H 135/653; L 139/611; printed 0.94(0.82-1.08). Complete source-row components: BMI≥40; 135/653; 139/611; 0.94(0.82-1.08); same.97.

**Reported-versus-comparator:** (135/653)/(139/611) = 0.908755; nearest two-decimal display 0.91; printed RR 0.94 differs by 0.031245.

**Reasoning procedure:** Divide the printed High PEEP event risk by the printed Low PEEP event risk. Integer counts and denominators are exact; nearest two-decimal comparison uses tolerance 0.005. The arithmetic is a diagnostic comparator and does not replace a fitted estimate. Methods p.4 concerns binomial GLM treatment-by-subgroup heterogeneity; it does not identify the plotted row-point estimator. The interaction P value is not paired with the row CI as a common test.

**Calculation:** (135/653)/(139/611)=0.908755, nearest two decimals 0.91; printed minus diagnostic=0.031245. Absolute discrepancy exceeds 0.005. q=[135/(135+139)]/[(653−135)/(653+611−135−139)]=0.941648 is reverse conditioning of treatment allocation on event status, not the High/Low event risk contrast. All arithmetic agrees with the current recheck. q similarity does not establish table transposition or the production estimator.

**Alternative source-grounded interpretations:** An adjusted or standardized estimate, a differently oriented/reference-coded contrast, or a different row denominator could explain the display only if supported by the original estimator definition. Row-specific estimator, orientation, adjustment and display procedure are not supplied. All four event/nonevent cells are positive, so a generic zero-cell explanation does not reconcile this comparison. Reverse-conditioned q is a different estimand and establishes no author coding or production mechanism.

**Mechanical evidence recheck:** The directly confirmed event counts and denominators yield 0.908755, outside the nearest-rounding interval for printed 0.94. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain. Source-matched recheck and audit confirmed the count/point tuple and reproduced the diagnostic. The remaining question is the named estimator definition.

**Quality-control relevance:** This is a quantitative reporting consistency question tied to a printed number, measure, endpoint or calculation convention. The suggested review disposition is a mechanical pre-fill for human review, not an adjudication.

**Potential downstream evidence impact:** If a label/estimand discrepancy is confirmed, an extractor could copy the point estimate as a crude event RR or pair it with the displayed counts under an inappropriate estimand. Small preventable reporting defects can matter for downstream evidence extraction. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:** Inspect the original row output and variable coding; identify event orientation, reference group, denominator, estimator, any adjustment and display procedure that produced 0.94; determine whether the printed RR purports to equal the displayed High/Low event-risk contrast; document the actual estimand for extraction.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C068 — SpO2<96%: labeled RR versus printed patient risks

Pending Human Adjudication.

**Candidate statement:** The labeled RR 0.88 does not equal the crude High/Low event-risk ratio from the printed counts under nearest two-decimal rounding. Whether it represents a different fitted or conditioned estimand remains unresolved.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Figure 2 Peripheral oxygen saturation <96% event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Methods PDF p. 4 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](../jama_bluth_2019_oi_190055_16092.pdf#page=4). The compared row and its context are identified in Compared document roles.

**Source evidence:** H 88/317; L 112/342; printed 0.88(0.74-1.06). Complete source-row components: SpO2<96%; 88/317; 112/342; 0.88(0.74-1.06); .35 shared withF06.

**Reported-versus-comparator:** (88/317)/(112/342) = 0.847679; nearest two-decimal display 0.85; printed RR 0.88 differs by 0.032321.

**Reasoning procedure:** Divide the printed High PEEP event risk by the printed Low PEEP event risk. Integer counts and denominators are exact; nearest two-decimal comparison uses tolerance 0.005. The arithmetic is a diagnostic comparator and does not replace a fitted estimate. Methods p.4 concerns binomial GLM treatment-by-subgroup heterogeneity; it does not identify the plotted row-point estimator. The interaction P value is not paired with the row CI as a common test.

**Calculation:** (88/317)/(112/342)=0.847679, nearest two decimals 0.85; printed minus diagnostic=0.032321. Absolute discrepancy exceeds 0.005. q=[88/(88+112)]/[(317−88)/(317+342−88−112)]=0.881921 is reverse conditioning of treatment allocation on event status, not the High/Low event risk contrast. All arithmetic agrees with the current recheck. q similarity does not establish table transposition or the production estimator.

**Alternative source-grounded interpretations:** An adjusted or standardized estimate, a differently oriented/reference-coded contrast, or a different row denominator could explain the display only if supported by the original estimator definition. Row-specific estimator, orientation, adjustment and display procedure are not supplied. All four event/nonevent cells are positive, so a generic zero-cell explanation does not reconcile this comparison. Reverse-conditioned q is a different estimand and establishes no author coding or production mechanism.

**Mechanical evidence recheck:** The directly confirmed event counts and denominators yield 0.847679, outside the nearest-rounding interval for printed 0.88. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain. Source-matched recheck and audit confirmed the count/point tuple and reproduced the diagnostic. The remaining question is the named estimator definition.

**Quality-control relevance:** This is a quantitative reporting consistency question tied to a printed number, measure, endpoint or calculation convention. The suggested review disposition is a mechanical pre-fill for human review, not an adjudication.

**Potential downstream evidence impact:** If a label/estimand discrepancy is confirmed, an extractor could copy the point estimate as a crude event RR or pair it with the displayed counts under an inappropriate estimand. Small preventable reporting defects can matter for downstream evidence extraction. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:** Inspect the original row output and variable coding; identify event orientation, reference group, denominator, estimator, any adjustment and display procedure that produced 0.88; determine whether the printed RR purports to equal the displayed High/Low event-risk contrast; document the actual estimand for extraction.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C069 — SpO2≥96%: labeled RR versus printed patient risks

Pending Human Adjudication.

**Candidate statement:** The labeled RR 0.99 does not equal the crude High/Low event-risk ratio from the printed counts under nearest two-decimal rounding. Whether it represents a different fitted or conditioned estimand remains unresolved.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Figure 2 Peripheral oxygen saturation ≥96% event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Methods PDF p. 4 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](../jama_bluth_2019_oi_190055_16092.pdf#page=4). The compared row and its context are identified in Compared document roles.

**Source evidence:** H 123/672; L 121/645; printed 0.99(0.86-1.13). Complete source-row components: SpO2≥96%; 123/672; 121/645; 0.99(0.86-1.13); same.35.

**Reported-versus-comparator:** (123/672)/(121/645) = 0.975686; nearest two-decimal display 0.98; printed RR 0.99 differs by 0.014314.

**Reasoning procedure:** Divide the printed High PEEP event risk by the printed Low PEEP event risk. Integer counts and denominators are exact; nearest two-decimal comparison uses tolerance 0.005. The arithmetic is a diagnostic comparator and does not replace a fitted estimate. Methods p.4 concerns binomial GLM treatment-by-subgroup heterogeneity; it does not identify the plotted row-point estimator. The interaction P value is not paired with the row CI as a common test.

**Calculation:** (123/672)/(121/645)=0.975686, nearest two decimals 0.98; printed minus diagnostic=0.014314. Absolute discrepancy exceeds 0.005. q=[123/(123+121)]/[(672−123)/(672+645−123−121)]=0.985241 is reverse conditioning of treatment allocation on event status, not the High/Low event risk contrast. All arithmetic agrees with the current recheck. q similarity does not establish table transposition or the production estimator.

**Alternative source-grounded interpretations:** An adjusted or standardized estimate, a differently oriented/reference-coded contrast, or a different row denominator could explain the display only if supported by the original estimator definition. Row-specific estimator, orientation, adjustment and display procedure are not supplied. All four event/nonevent cells are positive, so a generic zero-cell explanation does not reconcile this comparison. Reverse-conditioned q is a different estimand and establishes no author coding or production mechanism.

**Mechanical evidence recheck:** The directly confirmed event counts and denominators yield 0.975686, outside the nearest-rounding interval for printed 0.99. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain. Source-matched recheck and audit confirmed the count/point tuple and reproduced the diagnostic. The remaining question is the named estimator definition.

**Quality-control relevance:** This is a quantitative reporting consistency question tied to a printed number, measure, endpoint or calculation convention. The suggested review disposition is a mechanical pre-fill for human review, not an adjudication.

**Potential downstream evidence impact:** If a label/estimand discrepancy is confirmed, an extractor could copy the point estimate as a crude event RR or pair it with the displayed counts under an inappropriate estimand. Small preventable reporting defects can matter for downstream evidence extraction. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:** Inspect the original row output and variable coding; identify event orientation, reference group, denominator, estimator, any adjustment and display procedure that produced 0.99; determine whether the printed RR purports to equal the displayed High/Low event-risk contrast; document the actual estimand for extraction.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C070 — Peripheral incision: labeled RR versus printed patient risks

Pending Human Adjudication.

**Candidate statement:** The labeled RR 1.16 does not equal the crude High/Low event-risk ratio from the printed counts under nearest two-decimal rounding. Whether it represents a different fitted or conditioned estimand remains unresolved.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Figure 2 Peripheral incision event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Methods PDF p. 4 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](../jama_bluth_2019_oi_190055_16092.pdf#page=4). The compared row and its context are identified in Compared document roles.

**Source evidence:** H 32/126; L 25/126; printed 1.16(0.89-1.53). Complete source-row components: Peripheral incision; 32/126; 25/126; 1.16(0.89-1.53); .11 shared withF08.

**Reported-versus-comparator:** (32/126)/(25/126) = 1.280000; nearest two-decimal display 1.28; printed RR 1.16 differs by -0.120000.

**Reasoning procedure:** Divide the printed High PEEP event risk by the printed Low PEEP event risk. Integer counts and denominators are exact; nearest two-decimal comparison uses tolerance 0.005. The arithmetic is a diagnostic comparator and does not replace a fitted estimate. Methods p.4 concerns binomial GLM treatment-by-subgroup heterogeneity; it does not identify the plotted row-point estimator. The interaction P value is not paired with the row CI as a common test.

**Calculation:** (32/126)/(25/126)=1.280000, nearest two decimals 1.28; printed minus diagnostic=-0.120000. Absolute discrepancy exceeds 0.005. q=[32/(32+25)]/[(126−32)/(126+126−32−25)]=1.164614 is reverse conditioning of treatment allocation on event status, not the High/Low event risk contrast. All arithmetic agrees with the current recheck. q similarity does not establish table transposition or the production estimator.

**Alternative source-grounded interpretations:** An adjusted or standardized estimate, a differently oriented/reference-coded contrast, or a different row denominator could explain the display only if supported by the original estimator definition. Row-specific estimator, orientation, adjustment and display procedure are not supplied. All four event/nonevent cells are positive, so a generic zero-cell explanation does not reconcile this comparison. Reverse-conditioned q is a different estimand and establishes no author coding or production mechanism.

**Mechanical evidence recheck:** The directly confirmed event counts and denominators yield 1.280000, outside the nearest-rounding interval for printed 1.16. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain. Source-matched recheck and audit confirmed the count/point tuple and reproduced the diagnostic. The remaining question is the named estimator definition.

**Quality-control relevance:** This is a quantitative reporting consistency question tied to a printed number, measure, endpoint or calculation convention. The suggested review disposition is a mechanical pre-fill for human review, not an adjudication.

**Potential downstream evidence impact:** If a label/estimand discrepancy is confirmed, an extractor could copy the point estimate as a crude event RR or pair it with the displayed counts under an inappropriate estimand. Small preventable reporting defects can matter for downstream evidence extraction. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:** Inspect the original row output and variable coding; identify event orientation, reference group, denominator, estimator, any adjustment and display procedure that produced 1.16; determine whether the printed RR purports to equal the displayed High/Low event-risk contrast; document the actual estimand for extraction.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C071 — Upper abdominal: labeled RR versus printed patient risks

Pending Human Adjudication.

**Candidate statement:** The labeled RR 0.90 does not equal the crude High/Low event-risk ratio from the printed counts under nearest two-decimal rounding. Whether it represents a different fitted or conditioned estimand remains unresolved.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Figure 2 Upper abdominal incision event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Methods PDF p. 4 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](../jama_bluth_2019_oi_190055_16092.pdf#page=4). The compared row and its context are identified in Compared document roles.

**Source evidence:** H 179/863; L 208/861; printed 0.90(0.80-1.02). Complete source-row components: Upper abdominal; 179/863; 208/861; 0.90(0.80-1.02); same.11.

**Reported-versus-comparator:** (179/863)/(208/861) = 0.858583; nearest two-decimal display 0.86; printed RR 0.90 differs by 0.041417.

**Reasoning procedure:** Divide the printed High PEEP event risk by the printed Low PEEP event risk. Integer counts and denominators are exact; nearest two-decimal comparison uses tolerance 0.005. The arithmetic is a diagnostic comparator and does not replace a fitted estimate. Methods p.4 concerns binomial GLM treatment-by-subgroup heterogeneity; it does not identify the plotted row-point estimator. The interaction P value is not paired with the row CI as a common test.

**Calculation:** (179/863)/(208/861)=0.858583, nearest two decimals 0.86; printed minus diagnostic=0.041417. Absolute discrepancy exceeds 0.005. q=[179/(179+208)]/[(863−179)/(863+861−179−208)]=0.904102 is reverse conditioning of treatment allocation on event status, not the High/Low event risk contrast. All arithmetic agrees with the current recheck. q similarity does not establish table transposition or the production estimator.

**Alternative source-grounded interpretations:** An adjusted or standardized estimate, a differently oriented/reference-coded contrast, or a different row denominator could explain the display only if supported by the original estimator definition. Row-specific estimator, orientation, adjustment and display procedure are not supplied. All four event/nonevent cells are positive, so a generic zero-cell explanation does not reconcile this comparison. Reverse-conditioned q is a different estimand and establishes no author coding or production mechanism.

**Mechanical evidence recheck:** The directly confirmed event counts and denominators yield 0.858583, outside the nearest-rounding interval for printed 0.90. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain. Source-matched recheck and audit confirmed the count/point tuple and reproduced the diagnostic. The remaining question is the named estimator definition.

**Quality-control relevance:** This is a quantitative reporting consistency question tied to a printed number, measure, endpoint or calculation convention. The suggested review disposition is a mechanical pre-fill for human review, not an adjudication.

**Potential downstream evidence impact:** If a label/estimand discrepancy is confirmed, an extractor could copy the point estimate as a crude event RR or pair it with the displayed counts under an inappropriate estimand. Small preventable reporting defects can matter for downstream evidence extraction. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:** Inspect the original row output and variable coding; identify event orientation, reference group, denominator, estimator, any adjustment and display procedure that produced 0.90; determine whether the printed RR purports to equal the displayed High/Low event-risk contrast; document the actual estimand for extraction.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C072 — Waist-to-hip<1.0: labeled RR versus printed patient risks

Pending Human Adjudication.

**Candidate statement:** The labeled RR 0.97 does not equal the crude High/Low event-risk ratio from the printed counts under nearest two-decimal rounding. Whether it represents a different fitted or conditioned estimand remains unresolved.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Figure 2 Waist-to-hip ratio <1.0 event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Methods PDF p. 4 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](../jama_bluth_2019_oi_190055_16092.pdf#page=4). The compared row and its context are identified in Compared document roles.

**Source evidence:** H 97/467; L 100/457; printed 0.97(0.83-1.13). Complete source-row components: Waist-to-hip<1.0; 97/467; 100/457; 0.97(0.83-1.13); .65 shared withF10.

**Reported-versus-comparator:** (97/467)/(100/457) = 0.949229; nearest two-decimal display 0.95; printed RR 0.97 differs by 0.020771.

**Reasoning procedure:** Divide the printed High PEEP event risk by the printed Low PEEP event risk. Integer counts and denominators are exact; nearest two-decimal comparison uses tolerance 0.005. The arithmetic is a diagnostic comparator and does not replace a fitted estimate. Methods p.4 concerns binomial GLM treatment-by-subgroup heterogeneity; it does not identify the plotted row-point estimator. The interaction P value is not paired with the row CI as a common test.

**Calculation:** (97/467)/(100/457)=0.949229, nearest two decimals 0.95; printed minus diagnostic=0.020771. Absolute discrepancy exceeds 0.005. q=[97/(97+100)]/[(467−97)/(467+457−97−100)]=0.967472 is reverse conditioning of treatment allocation on event status, not the High/Low event risk contrast. All arithmetic agrees with the current recheck. q similarity does not establish table transposition or the production estimator.

**Alternative source-grounded interpretations:** An adjusted or standardized estimate, a differently oriented/reference-coded contrast, or a different row denominator could explain the display only if supported by the original estimator definition. Row-specific estimator, orientation, adjustment and display procedure are not supplied. All four event/nonevent cells are positive, so a generic zero-cell explanation does not reconcile this comparison. Reverse-conditioned q is a different estimand and establishes no author coding or production mechanism.

**Mechanical evidence recheck:** The directly confirmed event counts and denominators yield 0.949229, outside the nearest-rounding interval for printed 0.97. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain. Source-matched recheck and audit confirmed the count/point tuple and reproduced the diagnostic. The remaining question is the named estimator definition.

**Quality-control relevance:** This is a quantitative reporting consistency question tied to a printed number, measure, endpoint or calculation convention. The suggested review disposition is a mechanical pre-fill for human review, not an adjudication.

**Potential downstream evidence impact:** If a label/estimand discrepancy is confirmed, an extractor could copy the point estimate as a crude event RR or pair it with the displayed counts under an inappropriate estimand. Small preventable reporting defects can matter for downstream evidence extraction. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:** Inspect the original row output and variable coding; identify event orientation, reference group, denominator, estimator, any adjustment and display procedure that produced 0.97; determine whether the printed RR purports to equal the displayed High/Low event-risk contrast; document the actual estimand for extraction.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C073 — Waist-to-hip ratio assigned a length unit

Pending Human Adjudication.

**Candidate statement:** Figure 2 attaches cm to the named waist-to-hip ratio, although a ratio of same-unit circumferences is dimensionless.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Figure 2 heading and REPORT main Table 1 ratio row

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both primary discrepancy locations are completed-trial content within one REPORT document, so S_W applies. Corroborating documents do not add a discrepancy relationship.

**Classification ambiguity:** None

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 5](../jama_bluth_2019_oi_190055_16092.pdf#page=5). The cited source, Figure2, says “Waist-to-hip ratio, cm” above<1.0/≥1.0. The cited source, Table1, prints ratio means1.01/1.00 and the same thresholds. Exact text and pagination agree with recheck.

**Source evidence:** Figure 2 prints “Waist-to-hip ratio, cm”, with <1.0/≥1.0 rows. Table 1 prints ratio means 1.01/1.00 and the same thresholds. Figure rows: High 97/467 and 98/447; Low 100/457 and 112/449; RR 0.97 (0.83–1.13) and 0.92 (0.78–1.08); shared interaction P .65.

**Reported-versus-comparator:** Printed length unit cm versus the dimensionless unit implied by the named circumference ratio.

**Reasoning procedure:** Divide waist circumference by hip circumference expressed in the same length units; those units cancel. Check the Figure 2 heading against Table 1 variable identity.

**Calculation:** cm/cm = 1 (dimensionless). This is an exact dimensional identity; numeric rounding tolerance does not apply.

**Alternative source-grounded interpretations:** The unit may be inherited from a circumference variable, or the figure may use a different measurement. Actual measurement construction is unreported; the named ratio and 1.0 thresholds support the dimensionless reading.

**Mechanical evidence recheck:** recorded_candidate. The directly printed ratio heading carries cm; the dimensional comparison reproduces. Diagnostic: Length/length has dimension 1; cm is a length unit, so it cannot denote that ratio. Classification S_W; all S_W; report_internal_inconsistency; no role/type code correction. Current source recheck and assigned audit confirm the printed facts above; the evidence state reflects the limits of the comparator. Exact remaining human question: Compare the variable dictionary and Figure 2 source heading with Table 1; confirm whether the plotted variable is the waist-to-hip ratio or a length measurement; specify its unit.

**Quality-control relevance:** This is a quantitative reporting consistency question tied to a printed number, measure, endpoint or calculation convention. The suggested review disposition is a mechanical pre-fill for human review, not an adjudication.

**Potential downstream evidence impact:** If confirmed, a downstream extractor could record the wrong unit for this subgroup variable. Small preventable reporting defects can matter for downstream evidence extraction. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:** Compare the variable dictionary and Figure 2 source heading with Table 1; confirm whether the plotted variable is the waist-to-hip ratio or a length measurement; specify its unit.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C074 — Waist-to-hip≥1.0: labeled RR versus printed patient risks

Pending Human Adjudication.

**Candidate statement:** The labeled RR 0.92 does not equal the crude High/Low event-risk ratio from the printed counts under nearest two-decimal rounding. Whether it represents a different fitted or conditioned estimand remains unresolved.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Figure 2 subgroup counts/point and REPORT main Methods model

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both primary discrepancy locations are completed-trial content within one REPORT document, so S_W applies. Corroborating documents do not add a discrepancy relationship.

**Classification ambiguity:** Point-estimator alignment is unresolved; document roles/type remain within one REPORT.

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](../jama_bluth_2019_oi_190055_16092.pdf#page=4). The compared row and its context are identified in Compared document roles.

**Source evidence:** H 98/447; L 112/449; printed 0.92(0.78-1.08). Complete source-row components: Waist-to-hip≥1.0; 98/447; 112/449; 0.92(0.78-1.08); same.65.

**Reported-versus-comparator:** (98/447)/(112/449)=0.878915, nearest two decimals 0.88; printed minus diagnostic=0.041085. Absolute discrepancy exceeds 0.005.

**Reasoning procedure:** Divide the printed High PEEP event risk by the printed Low PEEP event risk. Integer counts and denominators are exact; nearest two-decimal comparison uses tolerance 0.005. The arithmetic is a diagnostic comparator and does not replace a fitted estimate. Methods p.4 concerns binomial GLM treatment-by-subgroup heterogeneity; it does not identify the plotted row-point estimator. The interaction P value is not paired with the row CI as a common test.

**Calculation:** (98/447)/(112/449)=0.878915, nearest two decimals 0.88; printed minus diagnostic=0.041085. Absolute discrepancy exceeds 0.005. q=[98/(98+112)]/[(447−98)/(447+449−98−112)]=0.917287 is reverse conditioning of treatment allocation on event status, not the High/Low event risk contrast. All arithmetic agrees with the current recheck. q similarity does not establish table transposition or the production estimator.

**Alternative source-grounded interpretations:** An adjusted or standardized estimate, a differently oriented/reference-coded contrast, or a different row denominator could explain the display only if supported by the original estimator definition. Row-specific estimator, orientation, adjustment and display procedure are not supplied. All four event/nonevent cells are positive, so a generic zero-cell explanation does not reconcile this comparison. Reverse-conditioned q is a different estimand and establishes no author coding or production mechanism.

**Mechanical evidence recheck:** recorded_candidate. Counts, RR label and point are confirmed; the registered conditional point-estimator/label question remains. The Methods GLM sentence explicitly concerns heterogeneity, so it does not independently identify or disprove the row-point estimator. Diagnostic: (98/447)/(112/449) = 0.878915; rounds to 0.88, versus 0.92. Classification S_W; all S_W; report_internal_inconsistency; no role/type code correction. Source-matched recheck and audit confirmed the count/point tuple and reproduced the diagnostic. The remaining question is the named estimator definition.

**Quality-control relevance:** This is a quantitative reporting consistency question tied to a printed number, measure, endpoint or calculation convention. The suggested review disposition is a mechanical pre-fill for human review, not an adjudication.

**Potential downstream evidence impact:** If a label/estimand discrepancy is confirmed, an extractor could copy the point estimate as a crude event RR or pair it with the displayed counts under an inappropriate estimand. Small preventable reporting defects can matter for downstream evidence extraction. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:** Inspect the original row output and variable coding; identify event orientation, reference group, denominator, estimator, any adjustment and display procedure that produced 0.92; determine whether the printed RR purports to equal the displayed High/Low event-risk contrast; document the actual estimand for extraction.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C075 — Mortality figure caption attaches percentages to extrapulmonary complications

Pending Human Adjudication.

**Candidate statement:** The eFigure 11 mortality title and axis conflict with a caption naming postoperative extrapulmonary complications.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eFigure 11 title/axis/caption and eFigure 10; REPORT main mortality row corroborates

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both primary discrepancy locations are completed-trial content within one REPORT document, so S_W applies. Corroborating documents do not add a discrepancy relationship.

**Classification ambiguity:** None

**Exact source locations:** [joi190055supp4_prod_16092.pdf — PDF p. 41](../joi190055supp4_prod_16092.pdf#page=41); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10); [joi190055supp4_prod_16092.pdf — PDF p. 40](../joi190055supp4_prod_16092.pdf#page=40). The cited source, eFigure11, title/axis name death/5-day mortality and printHR1.67(0.40–6.97),P.484. Caption labels0.5%/0.3% “postoperative extra-pulmonary complications.” The source-matched render visually confirms the mismatch. The cited source gives actual extrapulmonary16.9%/15.2%. The cited source five-day mortality5(0.5%)/3(0.3%),HR1.67(0.40–6.97),P.48 merely corroborates.

**Source evidence:** eFigure 11 title/axis identify death/5-day mortality; HR 1.67 (0.40–6.97), P .484; its caption calls 0.5%/0.3% “postoperative extra-pulmonary complications.” eFigure 10 gives extrapulmonary 16.9%/15.2%. Main five-day mortality is 5 (0.5%)/3 (0.3%), HR 1.67 (0.40–6.97), P .48.

**Reported-versus-comparator:** Same-page mortality title/axis versus extrapulmonary caption; the caption percentages and HR match mortality corroboration rather than eFigure 10 extrapulmonary percentages.

**Reasoning procedure:** Match endpoint names, five-day horizon, arm percentages and HR/CI across eFigure 11 title, axis and caption; use eFigure 10 and main mortality row as identity checks.

**Calculation:** The 0.5%/0.3% caption percentages and 1.67 (0.40–6.97) HR match mortality. Extrapulmonary percentages are 16.9%/15.2%. P .484 and .48 differ only in display precision and are not the mismatch.

**Alternative source-grounded interpretations:** A copied caption endpoint word or an incorrect figure title/axis could explain the label difference. The underlying endpoint code is absent, so the direction of correction is unresolved.

**Mechanical evidence recheck:** recorded_candidate. Direct render shows mortality title/axis and an extra-pulmonary caption on the same page. Diagnostic: 0.5%/0.3% and HR/CI match mortality; extra-pulmonary comparator is 16.9%/15.2%. Classification S_W; all S_W; report_internal_inconsistency; no role/type code correction. Current source recheck and assigned audit confirm the printed facts above; the evidence state reflects the limits of the comparator. Exact remaining human question: Inspect the endpoint code and source plotting data for eFigure 11; compare its title/axis/caption with eFigure 10 and main Table 3; identify the endpoint actually plotted.

**Quality-control relevance:** This is a quantitative reporting consistency question tied to a printed number, measure, endpoint or calculation convention. The suggested review disposition is a mechanical pre-fill for human review, not an adjudication.

**Potential downstream evidence impact:** If confirmed, the caption could cause mortality data to be extracted under an extrapulmonary endpoint. Small preventable reporting defects can matter for downstream evidence extraction. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:** Inspect the endpoint code and source plotting data for eFigure 11; compare its title/axis/caption with eFigure 10 and main Table 3; identify the endpoint actually plotted.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C076 — Collapsed-composite effect labeled OR in supplement and RR in main

Pending Human Adjudication.

**Candidate statement:** The identical collapsed-composite estimate and interval appear under an OR heading in the results supplement and an RR label in the main article; heading scope and estimator identity require reconciliation.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT supplement eFigure 12 global heading versus REPORT main primary table/abstract; PLAN final SAP corroborates RR

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R. 

**Classification ambiguity:** Cross-report estimator identity is conditional; SAP corroborates RR and creates no P_R discrepancy.

**Exact source locations:** [joi190055supp4_prod_16092.pdf — PDF p. 42](../joi190055supp4_prod_16092.pdf#page=42); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](../jama_bluth_2019_oi_190055_16092.pdf#page=9); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 1](../jama_bluth_2019_oi_190055_16092.pdf#page=1); [joi190055supp3_prod_16092.pdf — PDF p. 2](../joi190055supp3_prod_16092.pdf#page=2). The cited source, eFigure12 lower Global Tests heading says Odds Ratio(95%CI), including Collapsed Composite0.93[0.83,1.04]. Source-matched render confirms. The cited source, primary row, and The cited source, call the identical display RR. PLAN final SAP p.2 corroborates intended RR; it is not a conflicting comparator.

**Source evidence:** eFigure 12 lower Global Tests heading: “Odds Ratio (95% CI)”; Collapsed Composite 0.93 [0.83, 1.04]. Main Table 3 primary PPC row and abstract: RR 0.93 (0.83–1.04), full-arm 989/987 five-day composite, High versus Low. Final SAP p.2 corroborates intended RR.

**Reported-versus-comparator:** Supplement OR heading versus main RR label for a matched point/interval; the SAP corroboration is not a discrepancy comparator.

**Reasoning procedure:** Check whether the Global Tests heading applies to Collapsed Composite and whether population, endpoint, horizon, contrast and estimator are identical across displays.

**Calculation:** RR = pH/pL; OR = [pH/(1−pH)]/[pL/(1−pL)]. These are distinct measures. Identical two-decimal points and intervals alone do not prove identical fitted estimators; there is no arithmetic tolerance for the label question.

**Alternative source-grounded interpretations:** The collapsed row may be an unstated exception to the OR heading, or separately fitted OR and RR displays could coincide. No row exception or estimator derivation is supplied.

**Mechanical evidence recheck:** recorded_candidate. The literal OR header above collapsed composite is confirmed in the current render; main labels identical display RR. Diagnostic: RR=pH/pL; OR=[pH/(1−pH)]/[pL/(1−pL)]. Identical point and CI are printed under the two headings. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction. Current source recheck and assigned audit confirm the printed facts above; the evidence state reflects the limits of the comparator. Exact remaining human question: Inspect the collapsed-row model output and heading scope; determine the actual estimator, contrast and any row exception; reconcile its label with main Table 3 and the abstract.

**Quality-control relevance:** This is a quantitative reporting consistency question tied to a printed number, measure, endpoint or calculation convention. The suggested review disposition is a mechanical pre-fill for human review, not an adjudication.

**Potential downstream evidence impact:** If confirmed, an extractor could assign the composite estimate to the wrong effect-measure field. Small preventable reporting defects can matter for downstream evidence extraction. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:** Inspect the collapsed-row model output and heading scope; determine the actual estimator, contrast and any row exception; reconcile its label with main Table 3 and the abstract.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C077 — Synthetic-colloid count comparison P differs

Pending Human Adjudication.

**Candidate statement:** The matched synthetic-colloid binary receipt counts have two different displayed P values; identical analysis and test conventions are unconfirmed.

**Category:** Statistical reporting inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT main Table 2 receipt row versus REPORT results supplement eTable 3 receipt row

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R. 

**Classification ambiguity:** None

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](../jama_bluth_2019_oi_190055_16092.pdf#page=8); [joi190055supp4_prod_16092.pdf — PDF p. 24](../joi190055supp4_prod_16092.pdf#page=24). The cited source, Table2 binary receipt row74/989 vs56/987 printsP.09. The cited source, eTable3 same binary receipt counts printsP0.10. Native source reads confirm. Adjacent amount-row P.09 and main recipient-median P.50 concern different quantities and are excluded from alignment.

**Source evidence:** Main Table 2 binary receipt: 74/989 (7.5%) versus 56/987 (5.7%), P .09. Results eTable 3 binary receipt: the same 74/56 and 989/987 headers, P 0.10. Adjacent amount-row P .09 and main recipient-median P .50 refer to different quantities.

**Reported-versus-comparator:** Main binary-row P .09 versus supplement binary-row P .10 at the same two-decimal precision.

**Reasoning procedure:** Match the binary receipt row, arm counts and reference populations; compare its displayed P values without substituting a reconstructed tail test or neighboring amount/median result.

**Calculation:** 0.10 − 0.09 = 0.01. This exact displayed difference does not establish equal test conventions or a source error.

**Alternative source-grounded interpretations:** Different continuity corrections, exact-test conventions or analysis sets may explain the displays. Original unrounded outputs and row-specific tests are absent.

**Mechanical evidence recheck:** recorded_candidate. Direct native source confirms different P values for the same printed binary receipt counts. Diagnostic: 0.10−0.09 = 0.01; displays have the same two-decimal precision. No tail test is substituted. Classification S_C; all S_C; statistical_results; no role/type code correction. Current source recheck and assigned audit confirm the printed facts above; the evidence state reflects the limits of the comparator. Exact remaining human question: Inspect each binary receipt test and unrounded output; verify analysis population and correction/exact-test convention; determine whether .09 and .10 intentionally come from different analyses.

**Quality-control relevance:** This is a quantitative reporting consistency question tied to a printed number, measure, endpoint or calculation convention. The suggested review disposition is a mechanical pre-fill for human review, not an adjudication.

**Potential downstream evidence impact:** If confirmed, a downstream evidence table could copy inconsistent P values for binary receipt. Small preventable reporting defects can matter for downstream evidence extraction. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:** Inspect each binary receipt test and unrounded output; verify analysis population and correction/exact-test convention; determine whether .09 and .10 intentionally come from different analyses.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C078 — Mild respiratory-failure oxygen boundary equals2 versus at most2

Pending Human Adjudication.

**Candidate statement:** The literal mild respiratory-failure oxygen boundaries =2 L/min and ≤2 L/min differ; any effect on patient classification or the reported counts depends on the operational test.

**Category:** Analysis-unit or population inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT main Table 3 footnote versus REPORT supplement eMethods definition

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R. 

**Classification ambiguity:** Operational equivalence of an exact-2 L test and a ≤2 response criterion is unresolved.

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10); [joi190055supp4_prod_16092.pdf — PDF p. 20](../joi190055supp4_prod_16092.pdf#page=20). The cited source, footnote d, says responding to2L or less; The cited source, eMethods, prints supplemental oxygen=2L/min. Current source text and direct source recheck image agree on the equality symbol. Main mild component counts135/989 and154/987 are tied to this endpoint label.

**Source evidence:** Main Table 3 footnote d: responding to “2 L or less” supplemental oxygen. Results eMethods: responding to supplemental oxygen =2 L/min; moderate responds only to >2 L/min. Main mild component counts are 135/989 and 154/987, within the 12-component composite.

**Reported-versus-comparator:** Literal main ≤2 criterion versus supplement =2 criterion; observed count differences are not established.

**Reasoning procedure:** Compare the named endpoint boundaries as sets while distinguishing an equality-valued response rule from a standardized test administered at exactly 2 L/min.

**Calculation:** A response at 1 L/min satisfies ≤2 but not literal =2. This logical example is not an observed patient reclassification; no revised 135/154 count can be calculated.

**Alternative source-grounded interpretations:** The equality symbol may substitute for ≤, or all responses may have been evaluated at a standardized 2 L/min test. A patient responding below 2 could also respond at 2, making operational definitions equivalent.

**Mechanical evidence recheck:** recorded_candidate. Current source image confirms =2, while main prints 2 L or less. Diagnostic: A response at 1 L/min satisfies ≤2 but not =2. No revised count is inferable. Classification S_C; all S_C; statistical_results; no role/type code correction. Current source recheck and assigned audit confirm the printed facts above; the evidence state reflects the limits of the comparator. Exact remaining human question: Inspect the CRF, endpoint dictionary and oxygen-testing procedure; determine how responses below 2 L/min were classified and which boundary produced 135/154; document any operational equivalence.

**Quality-control relevance:** This is a quantitative reporting consistency question tied to a printed number, measure, endpoint or calculation convention. The suggested review disposition is a mechanical pre-fill for human review, not an adjudication.

**Potential downstream evidence impact:** If confirmed, different copied endpoint boundaries could affect eligibility or endpoint extraction; actual count effects remain unestablished. Small preventable reporting defects can matter for downstream evidence extraction. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:** Inspect the CRF, endpoint dictionary and oxygen-testing procedure; determine how responses below 2 L/min were classified and which boundary produced 135/154; document any operational equivalence.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C079 — Emergency-procedure counts differ between main and surgical supplement

Pending Human Adjudication.

**Candidate statement:** Main and supplemental emergency-procedure counts differ, conditional on the still-unconfirmed identity of the field, assessment time and population.

**Category:** Cross-document numeric inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT main baseline Table 1 emergency procedure versus REPORT supplement surgical priority eTable 6

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R. 

**Classification ambiguity:** Emergency timing/category and available-case identity remain unconfirmed.

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 5](../jama_bluth_2019_oi_190055_16092.pdf#page=5); [joi190055supp4_prod_16092.pdf — PDF p. 27](../joi190055supp4_prod_16092.pdf#page=27). The cited source, Table1, emergency21/20; The cited source, eTable6 priority, emergency13/11,urgent9/13,elective962/958,headers989/987. Exact current source reads reproduce values and physical pagination.

**Source evidence:** Main Table 1 Emergency procedure: High 21 (2.1%), Low 20 (2.0%). Results eTable 6 Priority of surgery: emergency 13 (1.3%)/11 (1.1%), urgent 9 (0.9%)/13 (1.3%), elective 962/958; arm headers 989/987.

**Reported-versus-comparator:** Main emergency 21/20 versus supplement emergency 13/11; neither urgency pooling nor field identity is supplied.

**Reasoning procedure:** Compare displayed counts only after verifying category, timing and population identity. Sum the three priority categories as a completeness diagnostic, not a recovered denominator.

**Calculation:** 21−13 = 8 High and 20−11 = 9 Low. Emergency plus urgent = 22/24, not 21/20. Priority totals 13+9+962 = 984 and 11+13+958 = 982, five below each full-arm header.

**Alternative source-grounded interpretations:** Different assessment times, urgency mappings or available-case subsets may explain the counts. The category sums suggest incomplete observations but do not identify missing records or establish identical fields.

**Mechanical evidence recheck:** recorded_candidate. Exact repeated emergency counts differ as registered; the missing mapping remains the named conditional question. Diagnostic: Main−supplement emergency =8 high/9 low; emergency+urgent =22/24; priority totals =984/982. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction. Current source recheck and assigned audit confirm the printed facts above; the evidence state reflects the limits of the comparator. Exact remaining human question: Locate the emergency definition, assessment time, urgency crosswalk and observed denominator for each table; inspect a cross-tabulation; reconcile 21/20 with 13/11 if they are the same field or document their distinct identities.

**Quality-control relevance:** This is a quantitative reporting consistency question tied to a printed number, measure, endpoint or calculation convention. The suggested review disposition is a mechanical pre-fill for human review, not an adjudication.

**Potential downstream evidence impact:** If confirmed, an extractor could copy different emergency subgroup counts under the same label. Small preventable reporting defects can matter for downstream evidence extraction. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:** Locate the emergency definition, assessment time, urgency crosswalk and observed denominator for each table; inspect a cross-tabulation; reconcile 21/20 with 13/11 if they are the same field or document their distinct identities.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C080 — Hypoxemia duration-qualifier omission and unresolved event-field identity

Pending Human Adjudication.

**Candidate statement:** record_input_error: the registered hypoxemia comparison inferred a conflicting duration rule from omission of a qualifier. The source confirms omission but supplies no affirmative no-duration rule or identity of event fields/windows.

**Category:** Analysis-unit or population inconsistency

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Compared document roles:** REPORT main Methods/count footnote versus REPORT supplement eMethods; PLAN protocol duration/RM fields corroborate the two descriptions

**Review domain:** statistical_results

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R. A within-main REPORT comparison is also registered; S_C takes precedence over S_W.

**Classification ambiguity:** Original S_C plus S_W comparison is retained as the registered relationship; plan corroboration adds no P_R/P_P discrepancy.

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 3](../jama_bluth_2019_oi_190055_16092.pdf#page=3); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 1](../jama_bluth_2019_oi_190055_16092.pdf#page=1); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](../jama_bluth_2019_oi_190055_16092.pdf#page=9); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10); [joi190055supp4_prod_16092.pdf — PDF p. 21](../joi190055supp4_prod_16092.pdf#page=21); [joi190055supp1_prod_16092.pdf — PDF p. 12](../joi190055supp1_prod_16092.pdf#page=12); [joi190055supp1_prod_16092.pdf — PDF p. 19](../joi190055supp1_prod_16092.pdf#page=19). The cited source Methods statesSpO2≤92% for>1 minute. The cited source Table3 prints49/134; The cited source event footnote and The cited source eMethods omit the duration qualifier. PLAN protocol pp.12/19 distinguish duration-qualified secondary parameters and recruitment-related event fields; these corroborate possible field differences without constituting a discrepancy comparator.

**Source evidence:** Main Methods p.3 states SpO2 ≤92% for >1 minute. Table 3 p.9 reports High/Low 49/134 (5.0%/13.6%). Main p.10 footnote and results eMethods p.21 omit duration. The main footnote also allows a further drop when already below the threshold (>5% when previously <92%). Protocol p.12 duration-qualified secondary parameters and p.19 recruitment-related fields corroborate possible field differences.

**Reported-versus-comparator:** Printed duration-qualified Methods versus abbreviated footnote/eMethods wording; omission does not affirm that brief episodes were counted or that these are identical fields.

**Reasoning procedure:** A missing qualifier establishes a textual omission, not the logical negation of the qualified rule. Compare count definitions only after confirming event variable, filtering and observation window.

**Calculation:** The >1 minute qualifier is printed in Methods and is not repeated in the other descriptions. A further drop from an already below-threshold baseline still meets the threshold. No revised 49/134 numerator or residual count discrepancy can be derived.

**Alternative source-grounded interpretations:** Footnote/eMethods may abbreviate a duration-filtered Methods variable, or recruitment-only and whole intraoperative event fields may differ. The package does not settle field identity, window or filtering.

**Mechanical evidence recheck:** record_input_error. The comparison treats omission of a qualifier as a different operational rule, but source supplies no affirmative no-duration rule or field identity; residual count discrepancy cannot be settled. Diagnostic: Printed duration appears in body and is not repeated in footnote/eMethods. No count change can be calculated. The below-baseline drop clause does not itself contradict the threshold because the patient remains below it. Classification S_C; all S_C, S_W; statistical_results; no role/type code correction. Current source recheck and assigned audit confirm the printed facts above; the evidence state reflects the limits of the comparator. Exact remaining human question: Identify the exact variable and event window that generated 49/134; inspect its duration filter and event dictionary; distinguish recruitment-only events from whole intraoperative episodes; determine whether the footnote/eMethods abbreviate the Methods rule.

**Quality-control relevance:** This is a quantitative reporting consistency question tied to a printed number, measure, endpoint or calculation convention. The suggested review disposition is a mechanical pre-fill for human review, not an adjudication.

**Potential downstream evidence impact:** The current evidence does not demonstrate a changed numerator or conflicting operational definition. An extractor should retain the unresolved duration/window mapping instead of treating shorthand omission as a confirmed new rule. Small preventable reporting defects can matter for downstream evidence extraction. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:** Identify the exact variable and event window that generated 49/134; inspect its duration filter and event dictionary; distinguish recruitment-only events from whole intraoperative episodes; determine whether the footnote/eMethods abbreviate the Methods rule.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C081 — Hypotension duration-qualifier omission and unresolved event-field identity

Pending Human Adjudication.

**Candidate statement:** record_input_error: the registered hypotension comparison inferred a conflicting duration rule from omission of a qualifier. The source confirms omission but supplies no affirmative no-duration rule or identity of event fields/windows.

**Category:** Analysis-unit or population inconsistency

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Compared document roles:** REPORT main Methods/count footnote versus REPORT supplement eMethods; PLAN protocol duration/RM fields corroborate the two descriptions

**Review domain:** statistical_results

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R. A within-main REPORT comparison is also registered; S_C takes precedence over S_W.

**Classification ambiguity:** Original S_C plus S_W comparison is retained as the registered relationship; plan corroboration adds no P_R/P_P discrepancy.

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 3](../jama_bluth_2019_oi_190055_16092.pdf#page=3); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](../jama_bluth_2019_oi_190055_16092.pdf#page=9); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10); [joi190055supp4_prod_16092.pdf — PDF p. 21](../joi190055supp4_prod_16092.pdf#page=21); [joi190055supp1_prod_16092.pdf — PDF p. 12](../joi190055supp1_prod_16092.pdf#page=12); [joi190055supp1_prod_16092.pdf — PDF p. 19](../joi190055supp1_prod_16092.pdf#page=19). The cited source Methods statessystolic pressure<90mmHg for>2 minutes. The cited source Table3 prints313/170; The cited source event footnote and The cited source eMethods omit the duration qualifier. PLAN protocol pp.12/19 distinguish duration-qualified secondary parameters and recruitment-related event fields; these corroborate possible field differences without constituting a discrepancy comparator.

**Source evidence:** Main Methods p.3 states systolic pressure <90 mm Hg for >2 minutes. Table 3 p.9 reports High/Low 313/170 (31.6%/17.2%). Main p.10 footnote and results eMethods p.21 omit duration. The main footnote also allows a further drop when already below the threshold (>10 mm Hg when previously <90). Protocol p.12 duration-qualified secondary parameters and p.19 recruitment-related fields corroborate possible field differences.

**Reported-versus-comparator:** Printed duration-qualified Methods versus abbreviated footnote/eMethods wording; omission does not affirm that brief episodes were counted or that these are identical fields.

**Reasoning procedure:** A missing qualifier establishes a textual omission, not the logical negation of the qualified rule. Compare count definitions only after confirming event variable, filtering and observation window.

**Calculation:** The >2 minutes qualifier is printed in Methods and is not repeated in the other descriptions. A further drop from an already below-threshold baseline still meets the threshold. No revised 313/170 numerator or residual count discrepancy can be derived.

**Alternative source-grounded interpretations:** Footnote/eMethods may abbreviate a duration-filtered Methods variable, or recruitment-only and whole intraoperative event fields may differ. The package does not settle field identity, window or filtering.

**Mechanical evidence recheck:** record_input_error. The comparison treats omission of a qualifier as a different operational rule, but source supplies no affirmative no-duration rule or field identity; residual count discrepancy cannot be settled. Diagnostic: Printed duration appears in body and is not repeated in footnote/eMethods. No count change can be calculated. The below-baseline drop clause does not itself contradict the threshold because the patient remains below it. Classification S_C; all S_C, S_W; statistical_results; no role/type code correction. Current source recheck and assigned audit confirm the printed facts above; the evidence state reflects the limits of the comparator. Exact remaining human question: Identify the exact variable and event window that generated 313/170; inspect its duration filter and event dictionary; distinguish recruitment-only events from whole intraoperative episodes; determine whether the footnote/eMethods abbreviate the Methods rule.

**Quality-control relevance:** This is a quantitative reporting consistency question tied to a printed number, measure, endpoint or calculation convention. The suggested review disposition is a mechanical pre-fill for human review, not an adjudication.

**Potential downstream evidence impact:** The current evidence does not demonstrate a changed numerator or conflicting operational definition. An extractor should retain the unresolved duration/window mapping instead of treating shorthand omission as a confirmed new rule. Small preventable reporting defects can matter for downstream evidence extraction. No actual propagation, conclusion change or serious harm is established.

**Human verification steps:** Identify the exact variable and event window that generated 313/170; inspect its duration filter and event dictionary; distinguish recruitment-only events from whole intraoperative episodes; determine whether the footnote/eMethods abbreviate the Methods rule.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C082 — conditional thoracic VAS mean/SD bound

Pending Human Adjudication.

**Candidate statement:** Conditional on zero-origin 0–10 cm scores on the same postoperative VAS, the low-PEEP Day 2 thoracic mean/SD tuple exceeds the bounded-support moment limit even after rounding. A 10 cm line length alone does not establish those endpoints or the postoperative scale identity.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT supplement eTable 7 thoracic summary versus PLAN protocol VAS scale/assessment

**Review domain:** protocol_report

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** The reported completed-trial summary is REPORT and the prospective measurement definition is PLAN; the substantive conditional scale comparison is P_R.

**Classification ambiguity:** P_R is conditional scale-to-report comparison; numerical endpoints and postoperative identity are not printed.

**Exact source locations:**

- [joi190055supp4_prod_16092.pdf results supplement, physical PDF p.28](../joi190055supp4_prod_16092.pdf#page=28), eTable 7, VAS thoracic – cm, mean (SD), No., Day 2, low PEEP cell: REPORT.
- [joi190055supp1_prod_16092.pdf protocol, physical PDF p.17](../joi190055supp1_prod_16092.pdf#page=17), printed protocol p.16, version 2.6, actual organ function evaluation bullet defining “Visual Analogue Scale (10 cm): evaluation for dyspnea, thoracic and abdominal rest and incident pain”: PLAN.
- [joi190055supp1_prod_16092.pdf protocol, physical PDF p.20](../joi190055supp1_prod_16092.pdf#page=20), printed protocol p.19, postoperative assessment continuation bullet “VAS evaluation for dyspnea, thoracic and abdominal rest and incident pain”: PLAN.

**Source evidence:** eTable 7 low PEEP day-2 thoracic VAS mean 1.4 cm, SD 3.9 cm, n = 841; high PEEP mean 1.3 cm, SD 0.8 cm, n = 838; P = .34. Arm headings are high989 and low987. The protocol specifies a 10 cm VAS for the same named symptoms and repeats the assessment postoperatively. It does not explicitly print the numerical scoring endpoints or a normalization rule.

**Reported-versus-comparator:** eTable 7 low PEEP day-2 thoracic VAS mean 1.4 cm, SD 3.9 cm, n = 841; high PEEP mean 1.3 cm, SD 0.8 cm, n = 838; P = .34. Arm headings are high989 and low987. The protocol specifies a 10 cm VAS for the same named symptoms and repeats the assessment postoperatively. It does not explicitly print the numerical scoring endpoints or a normalization rule. 

**Reasoning procedure:** The mean, SD, n, cm unit, mean(SD) header and protocol 10 cm scale wording are direct source observations. The numerical 0–10 support and zero-origin scoring convention are explicitly conditional inferences from that supplied line-length and cm-unit description. They are not independently printed endpoints. Protocol p.17 describes baseline organ-function assessment; p.20 repeats the same named VAS postoperatively but does not restate its length. Applying the 10 cm definition to eTable 7 is an identity question retained for human review. Numerical scoring origin/endpoints, postoperative identity with the baseline-defined scale, transformation and SD convention. Human question: Were postoperative thoracic scores zero-origin 0–10 cm scores on the protocol line, and does the low Day 2 tuple correctly read mean1.4, SD3.9, n841; if different, what origin/range/transformation was used?

**Calculation:** Conditional on the reported cm scores being distance along the supplied 10 cm line, measured from a zero origin and bounded 0–10 cm, any sample with mean m and sample SD s obeys s² ≤ n/(n−1) × m × (10−m). At the printed mean, the maximum sample SD is sqrt(841/840 × 1.4 × 8.6) = 3.47194 cm, below 3.9 cm. With rounding admitted, m can range from 1.35 to 1.45; the largest permitted bound on that interval is sqrt(841/840 × 1.45 × 8.55) = 3.52310 cm. The printed SD interval begins at 3.85 cm. Thus even the most permissive rounding leaves a gap of at least 3.85 − 3.52310 = 0.32690 cm. Display tolerance: Mean/SD displayed to one decimal permit ±0.05 cm; n = 841 is exact. The n/(n−1) factor allows the usual sample SD convention and is slightly more permissive than population SD. This calculation is a moment bound, not a reconstructed P value.

**Alternative source-grounded interpretations:** A transformed or shifted scoring convention, a differently normalized postoperative scale, a larger allowed range, a different underlying statistic despite the mean(SD) label, or a transcription error could explain the display. Without zero origin, a line of length10 alone permits SD up to about5.00 cm and does not establish the mean-dependent contradiction. An alternative 0-based scale would need an upper endpoint at least11.66026 cm even with the rounding allowances, to accommodate the minimum printed SD3.85 at mean1.45. No external VAS convention is used.

**Mechanical evidence recheck:** recorded_candidate. Direct source confirms the tuple and 10 cm plan description; the registered bounded-support question remains conditional on its explicitly missing origin/scale identity. Diagnostic: At m1.4,n841, maximum SD=3.47194. Allowing mean rounding up to1.45 gives 3.52310, below minimum rounding-consistent SD3.85 by 0.32690 cm. Classification P_R; all P_R; protocol_report; no role/type code correction. Necessary missing inputs: Numerical scoring origin/endpoints, postoperative identity with the baseline-defined scale, transformation and SD convention. Human question: Were postoperative thoracic scores zero-origin 0–10 cm scores on the protocol line, and does the low Day 2 tuple correctly read mean1.4, SD3.9, n841; if different, what origin/range/transformation was used? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (retain) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** The reported dispersion may be reused as a summary SD in quantitative evidence synthesis. The candidate is confined to the consistency of that reported summary with the supplied scale definition; it is not a raw-data or clinical plausibility audit.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the thoracic VAS SD into a quantitative synthesis. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Open the exact source pages above and compare the cited cells or statements. Recompute the stated arithmetic or logical diagnostic using the printed inputs, retaining the named conditions and display tolerance. Resolve this source-specific question: “Were the postoperative thoracic VAS scores in eTable 7 recorded as 0–10 cm distance scores on the protocol’s 10 cm scale, and does the low-PEEP Day 2 cell correctly report mean 1.4 cm, SD 3.9 cm and n = 841; if a different origin, range or transformation was used, what was it?” Record the human assessment in the five blank fields below.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C083 — conditional event-count mean versus component total

Pending Human Adjudication.

**Candidate statement:** The high-arm count summary 0.35 differs from the nearest-rounded mean 353/989 = 0.36 only if the unlabeled first statistic is the mean of the same twelve component indicators in the displayed population. The summary statistic, aggregation and realized denominator are not supplied; randomized denominators provide a coherent alternative.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT supplement eTable 9 count summary versus REPORT main Table 3 component numerators; REPORT main randomized denominator is an alternative; PLAN SAP count definition corroborates

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.

**Classification ambiguity:** First summary and realized count aggregation are not explicitly defined. SAP corroborates count concept without a P_R discrepancy.

**Exact source locations:**

- [joi190055supp4_prod_16092.pdf results supplement, physical PDF p.30](../joi190055supp4_prod_16092.pdf#page=30), eTable 9, Sensitivity analysis for the primary outcome, Count events row, high/low summary cells and n = 989/987 headings: REPORT.
- [jama_bluth_2019_oi_190055_16092.pdf main article, physical PDF p.9](../jama_bluth_2019_oi_190055_16092.pdf#page=9), printed p.2300, Table 3, all 12 Components of the Primary Outcome, high/low No. of Events columns and n = 989/987 headings: REPORT.
- DOC-005 p.30 model footnotes referring to all12 components are corroborative REPORT context, not a new discrepancy relationship.
- [jama_bluth_2019_oi_190055_16092.pdf main article, physical PDF p.3](../jama_bluth_2019_oi_190055_16092.pdf#page=3), Figure 1 randomized high 1011/low 1002, REPORT: source-grounded alternative denominator, not an additional discrepancy relationship. Corroborative PLAN count-definition context: [joi190055supp3_prod_16092.pdf — physical PDF p. 3](../joi190055supp3_prod_16092.pdf#page=3), sensitivity-analysis paragraph.

**Source evidence:** eTable 9 Count events row gives high0.35 (0.88), low0.38 (0.86), above separately labeled Median (IQR)0 (0–0) for both arms. The Count events row does not explicitly say mean(SD). Main Table 3 high component counts, in its printed order, are mild135, moderate42, severe30, atelectasis44, pleural effusion43, new infiltrates14, cardiopulmonary edema17, bronchospasm12, pulmonary infection10, aspiration2, ARDS3, pneumothorax1. Low counts in the same order are154,58,36,55,21,18,9,10,10,1,1,3.

**Reported-versus-comparator:** eTable 9 Count events row gives high0.35 (0.88), low0.38 (0.86), above separately labeled Median (IQR)0 (0–0) for both arms. The Count events row does not explicitly say mean(SD). Main Table 3 high component counts, in its printed order, are mild135, moderate42, severe30, atelectasis44, pleural effusion43, new infiltrates14, cardiopulmonary edema17, bronchospasm12, pulmonary infection10, aspiration2, ARDS3, pneumothorax1. Low counts in the same order are154,58,36,55,21,18,9,10,10,1,1,3. 

**Reasoning procedure:** Direct images confirm all12 main component counts, populations, and the eTable 9 summary0.35 (0.88). The arithmetic sum and conditional mean identity are derived. Interpreting the unlabeled first summary as mean(SD), and interpreting “Count events” as counting each of the same12 binary components, are named inferences rather than printed definitions. First summary statistic label, actual event grouping/time rule, analysis n, missing-participant treatment and rounding convention. Human question: Is 0.35(0.88) the mean(SD) of these twelve component counts among989 high participants; if so how does353/989 reconcile, and otherwise what statistic/grouping/window/denominator and participant handling define it?

**Calculation:** Conditional on “Count events” summary0.35/0.38 being the arithmetic mean of the number of these same12 binary components per participant in the displayed full-arm populations, the mean must equal the sum of all component numerators divided by n. Overlap between components does not defeat this identity; each counted component contributes separately. High sum135 + 42 + 30 + 44 + 43 + 14 + 17 + 12 + 10 + 2 + 3 + 1 = 353; 353 / 989 = 0.356926, which rounds to0.36. Low sum154 + 58 + 36 + 55 + 21 + 18 + 9 + 10 + 10 + 1 + 1 + 3 = 376; 376 / 987 = 0.380952, which rounds to0.38 and reconciles. Display tolerance: At two-decimal rounding,0.35 ordinarily implies a mean in [0.345,0.355), hence a total in [341.205,351.095) at n989; integer totals compatible with that interval are342–351. The printed component total353 exceeds the largest compatible integer total by2. The exact mean exceeds the upper rounding boundary0.355 by0.001926. Counts and denominator have zero tolerance. The low-arm summary is within its rounding interval.

**Alternative source-grounded interpretations:** The summary may use a different statistic, component grouping (for example collapsing multiple respiratory-failure severities to one event), time rule, population, event definition, weighting or complete-case denominator. Main Figure 1 supplies randomized high 1011/low 1002: 353/1011 = 0.349159 and 376/1002 = 0.375250, which round to 0.35/0.38. Thus a count calculation using all randomized participants could explain both summary means, but that denominator differs from eTable 9 headings 989/987 and requires the population and missing-participant handling to be named. This is an arithmetic alternative, not proof that the authors used it. Truncation rather than rounding would also produce 0.35 from 0.356926 but is not stated. Different component overlap is not by itself an explanation if the count is the sum of those same 12 indicators; alternative grouping would change the count definition and should be specified.

**Mechanical evidence recheck:** recorded_candidate. Count tuple and component totals are confirmed; arithmetic reproduces the registered conditional high-arm rounding question. Diagnostic: High sum353;353/989=0.356926→0.36, versus0.35. Low sum376;376/987=0.380952→0.38. High two-decimal0.35 permits integer totals342–351 under ordinary rounding. Alternative353/1011=0.349159→0.35 and376/1002=0.375250→0.38. Classification S_C; all S_C; statistical_results; no role/type code correction. Necessary missing inputs: First summary statistic label, actual event grouping/time rule, analysis n, missing-participant treatment and rounding convention. Human question: Is 0.35(0.88) the mean(SD) of these twelve component counts among989 high participants; if so how does353/989 reconcile, and otherwise what statistic/grouping/window/denominator and participant handling define it? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (retain) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** Event burden means and their dispersions can be extracted separately from binary-composite risks; a missing aggregation definition or mismatched displayed mean can lead to an incorrect extracted endpoint. No claim about treatment effect or conclusion follows.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the count-burden summary with the wrong statistic or population. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Open the exact source pages above and compare the cited cells or statements. Recompute the stated arithmetic or logical diagnostic using the printed inputs, retaining the named conditions and display tolerance. Resolve this source-specific question: “Is 0.35 (0.88) in the high-PEEP Count events row the mean (SD) of the count of the same 12 primary-outcome components reported in main Table 3 among 989 participants; if so, how does it reconcile with 353 component occurrences and 353/989 = 0.356926, and if not, what statistic, grouping, time rule and denominator does it represent?” Record the human assessment in the five blank fields below.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C084 — Conditional follow-up/time-origin reconciliation question — eFigure8

Pending Human Adjudication.

**Candidate statement:** The median follow-up and day-five risk counts require reconciliation only under an assumed common time origin and follow-up convention; the missing definitions prevent an unconditional incompatibility claim.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT supplement eFigure 8 PPC caption versus same-page risk table

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both primary discrepancy locations are completed-trial content within one REPORT document, so S_W applies. Corroborating documents do not add a discrepancy relationship.

**Classification ambiguity:** Caption and risk-table times may use different inclusive origins or assessment summaries; no raw follow-up reconstruction is possible.

**Exact source locations:** [joi190055supp4_prod_16092.pdf — physical PDF p. 38](../joi190055supp4_prod_16092.pdf#page=38), eFigure 8 PPC, caption median follow-up and same-page baseline/day-5 risk-table cells (REPORT). This card concerns this endpoint alone.

**Source evidence:** The caption prints median follow-up 4 (2–5) days. Baseline high/low risk counts are 989/987 (total 1976); at day 5 they are 785/756 (total 1541).

**Reported-versus-comparator:** The day-5 risk total 1541 is compared with the conditional upper count 988 beyond four elapsed days if the caption is an ordinary median of the same observed follow-up variable on the same time origin.

**Reasoning procedure:** The caption and risk cells are direct observations. The order-statistic comparison is derived and conditional: caption follow-up, risk-table time, origin and inclusive-day convention must identify the same observed-time variable. Without that mapping, incompatibility is not established.

**Calculation:** 1976 / 2 = 988; 785 + 756 = 1541; 1541 − 988 = 553. Under the shared elapsed-time interpretation, a median of four days cannot coexist with more than half observed beyond day 4. Counts are exact; ordinary integer rounding of median 4 remains below 4.5 elapsed days. This diagnostic does not apply unchanged if postoperative day 5 corresponds to four elapsed days.

**Alternative source-grounded interpretations:** Inclusive postoperative numbering may label four elapsed days as day 5. The caption may summarize assessment duration while endpoint ascertainment continues, or may use a different follow-up statistic. The risk table may use a different removal rule. The caption statistic, origin/inclusiveness, assessment-versus-ascertainment mapping, and endpoint-specific event/censor/risk definitions are missing. No patient-level trajectory is reconstructed.

**Mechanical evidence recheck:** recorded_candidate. Both cited displays are confirmed; registered conditional time-definition question remains, and the missing definition prevents an unconditional incompatibility claim. Diagnostic: 1976/2=988; day-five total1541 exceeds988 by553. This is a conditional order-statistic diagnostic; inclusive postoperative day numbering can map four elapsed days to day5. Classification S_W; all S_W; statistical_results; no role/type code correction. Necessary missing inputs: Caption variable and calculation (ordinary or another follow-up summary), origin, inclusive-day convention, risk-time mapping and whether assessment duration differs from endpoint ascertainment. Human question: For eFigure 8 PPC, what variable/origin/inclusiveness defines median4(2–5), what time is day5 in the risk table, and are both the same observed-time summary? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (retain) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** Time-dependent denominators and follow-up summaries could be reused under incompatible definitions.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the follow-up duration or time-dependent risk denominator into an endpoint summary. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Open eFigure 8 on physical PDF p. 38; confirm the caption and baseline/day-5 risk cells. Ask which variable and calculation define median 4 (2–5), what time origin and inclusive convention define day 5, and which endpoint-specific events or censoring remove patients. Determine whether caption and risk-table times refer to the same observed-time summary before applying the conditional bound. Record the assessment below.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C085 — Conditional follow-up/time-origin reconciliation question — eFigure9

Pending Human Adjudication.

**Candidate statement:** The median follow-up and day-five risk counts require reconciliation only under an assumed common time origin and follow-up convention; the missing definitions prevent an unconditional incompatibility claim.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT supplement eFigure 9 severe PPC caption versus same-page risk table

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both primary discrepancy locations are completed-trial content within one REPORT document, so S_W applies. Corroborating documents do not add a discrepancy relationship.

**Classification ambiguity:** Caption and risk-table times may use different inclusive origins or assessment summaries; no raw follow-up reconstruction is possible.

**Exact source locations:** [joi190055supp4_prod_16092.pdf — physical PDF p. 39](../joi190055supp4_prod_16092.pdf#page=39), eFigure 9 severe PPC, caption median follow-up and same-page baseline/day-5 risk-table cells (REPORT). This card concerns this endpoint alone.

**Source evidence:** The caption prints median follow-up 4 (2–5) days. Baseline high/low risk counts are 989/987 (total 1976); at day 5 they are 785/756 (total 1541).

**Reported-versus-comparator:** The day-5 risk total 1541 is compared with the conditional upper count 988 beyond four elapsed days if the caption is an ordinary median of the same observed follow-up variable on the same time origin.

**Reasoning procedure:** The caption and risk cells are direct observations. The order-statistic comparison is derived and conditional: caption follow-up, risk-table time, origin and inclusive-day convention must identify the same observed-time variable. Without that mapping, incompatibility is not established.

**Calculation:** 1976 / 2 = 988; 785 + 756 = 1541; 1541 − 988 = 553. Under the shared elapsed-time interpretation, a median of four days cannot coexist with more than half observed beyond day 4. Counts are exact; ordinary integer rounding of median 4 remains below 4.5 elapsed days. This diagnostic does not apply unchanged if postoperative day 5 corresponds to four elapsed days.

**Alternative source-grounded interpretations:** Inclusive postoperative numbering may label four elapsed days as day 5. The caption may summarize assessment duration while endpoint ascertainment continues, or may use a different follow-up statistic. The risk table may use a different removal rule. The caption statistic, origin/inclusiveness, assessment-versus-ascertainment mapping, and endpoint-specific event/censor/risk definitions are missing. No patient-level trajectory is reconstructed.

**Mechanical evidence recheck:** recorded_candidate. Both cited displays are confirmed; registered conditional time-definition question remains, and the missing definition prevents an unconditional incompatibility claim. Diagnostic: 1976/2=988; day-five total1541 exceeds988 by553. This is a conditional order-statistic diagnostic; inclusive postoperative day numbering can map four elapsed days to day5. Classification S_W; all S_W; statistical_results; no role/type code correction. Necessary missing inputs: Caption variable and calculation (ordinary or another follow-up summary), origin, inclusive-day convention, risk-time mapping and whether assessment duration differs from endpoint ascertainment. Human question: For eFigure 9 severe PPC, what variable/origin/inclusiveness defines median4(2–5), what time is day5 in the risk table, and are both the same observed-time summary? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (retain) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** Time-dependent denominators and follow-up summaries could be reused under incompatible definitions.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the follow-up duration or time-dependent risk denominator into an endpoint summary. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Open eFigure 9 on physical PDF p. 39; confirm the caption and baseline/day-5 risk cells. Ask which variable and calculation define median 4 (2–5), what time origin and inclusive convention define day 5, and which endpoint-specific events or censoring remove patients. Determine whether caption and risk-table times refer to the same observed-time summary before applying the conditional bound. Record the assessment below.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C086 — Conditional follow-up/time-origin reconciliation question — eFigure10

Pending Human Adjudication.

**Candidate statement:** The median follow-up and day-five risk counts require reconciliation only under an assumed common time origin and follow-up convention; the missing definitions prevent an unconditional incompatibility claim.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT supplement eFigure 10 extrapulmonary caption versus same-page risk table

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both primary discrepancy locations are completed-trial content within one REPORT document, so S_W applies. Corroborating documents do not add a discrepancy relationship.

**Classification ambiguity:** Caption and risk-table times may use different inclusive origins or assessment summaries; no raw follow-up reconstruction is possible.

**Exact source locations:** [joi190055supp4_prod_16092.pdf — physical PDF p. 40](../joi190055supp4_prod_16092.pdf#page=40), eFigure 10 extrapulmonary complications, caption median follow-up and same-page baseline/day-5 risk-table cells (REPORT). This card concerns this endpoint alone.

**Source evidence:** The caption prints median follow-up 4 (2–5) days. Baseline high/low risk counts are 989/987 (total 1976); at day 5 they are 828/845 (total 1673).

**Reported-versus-comparator:** The day-5 risk total 1673 is compared with the conditional upper count 988 beyond four elapsed days if the caption is an ordinary median of the same observed follow-up variable on the same time origin.

**Reasoning procedure:** The caption and risk cells are direct observations. The order-statistic comparison is derived and conditional: caption follow-up, risk-table time, origin and inclusive-day convention must identify the same observed-time variable. Without that mapping, incompatibility is not established.

**Calculation:** 1976 / 2 = 988; 828 + 845 = 1673; 1673 − 988 = 685. Under the shared elapsed-time interpretation, a median of four days cannot coexist with more than half observed beyond day 4. Counts are exact; ordinary integer rounding of median 4 remains below 4.5 elapsed days. This diagnostic does not apply unchanged if postoperative day 5 corresponds to four elapsed days.

**Alternative source-grounded interpretations:** Inclusive postoperative numbering may label four elapsed days as day 5. The caption may summarize assessment duration while endpoint ascertainment continues, or may use a different follow-up statistic. The risk table may use a different removal rule. The caption statistic, origin/inclusiveness, assessment-versus-ascertainment mapping, and endpoint-specific event/censor/risk definitions are missing. No patient-level trajectory is reconstructed.

**Mechanical evidence recheck:** recorded_candidate. Both cited displays are confirmed; registered conditional time-definition question remains, and the missing definition prevents an unconditional incompatibility claim. Diagnostic: 1976/2=988; day-five total1673 exceeds988 by685. This is a conditional order-statistic diagnostic; inclusive postoperative day numbering can map four elapsed days to day5. Classification S_W; all S_W; statistical_results; no role/type code correction. Necessary missing inputs: Caption variable and calculation (ordinary or another follow-up summary), origin, inclusive-day convention, risk-time mapping and whether assessment duration differs from endpoint ascertainment. Human question: For eFigure 10 extrapulmonary, what variable/origin/inclusiveness defines median4(2–5), what time is day5 in the risk table, and are both the same observed-time summary? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (retain) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** Time-dependent denominators and follow-up summaries could be reused under incompatible definitions.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the follow-up duration or time-dependent risk denominator into an endpoint summary. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Open eFigure 10 on physical PDF p. 40; confirm the caption and baseline/day-5 risk cells. Ask which variable and calculation define median 4 (2–5), what time origin and inclusive convention define day 5, and which endpoint-specific events or censoring remove patients. Determine whether caption and risk-table times refer to the same observed-time summary before applying the conditional bound. Record the assessment below.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C087 — Conditional follow-up/time-origin reconciliation question — eFigure11

Pending Human Adjudication.

**Candidate statement:** The median follow-up and day-five risk counts require reconciliation only under an assumed common time origin and follow-up convention; the missing definitions prevent an unconditional incompatibility claim.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT supplement eFigure 11 mortality caption versus same-page risk table

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both primary discrepancy locations are completed-trial content within one REPORT document, so S_W applies. Corroborating documents do not add a discrepancy relationship.

**Classification ambiguity:** Caption and risk-table times may use different inclusive origins or assessment summaries; no raw follow-up reconstruction is possible.

**Exact source locations:** [joi190055supp4_prod_16092.pdf — physical PDF p. 41](../joi190055supp4_prod_16092.pdf#page=41), eFigure 11 mortality, caption median follow-up and same-page baseline/day-5 risk-table cells (REPORT). This card concerns this endpoint alone.

**Source evidence:** The caption prints median follow-up 4 (2–5) days. Baseline high/low risk counts are 989/987 (total 1976); at day 5 they are 985/986 (total 1971).

**Reported-versus-comparator:** The day-5 risk total 1971 is compared with the conditional upper count 988 beyond four elapsed days if the caption is an ordinary median of the same observed follow-up variable on the same time origin.

**Reasoning procedure:** The caption and risk cells are direct observations. The order-statistic comparison is derived and conditional: caption follow-up, risk-table time, origin and inclusive-day convention must identify the same observed-time variable. Without that mapping, incompatibility is not established.

**Calculation:** 1976 / 2 = 988; 985 + 986 = 1971; 1971 − 988 = 983. Under the shared elapsed-time interpretation, a median of four days cannot coexist with more than half observed beyond day 4. Counts are exact; ordinary integer rounding of median 4 remains below 4.5 elapsed days. This diagnostic does not apply unchanged if postoperative day 5 corresponds to four elapsed days.

**Alternative source-grounded interpretations:** Inclusive postoperative numbering may label four elapsed days as day 5. The caption may summarize assessment duration while endpoint ascertainment continues, or may use a different follow-up statistic. The risk table may use a different removal rule. The caption statistic, origin/inclusiveness, assessment-versus-ascertainment mapping, and endpoint-specific event/censor/risk definitions are missing. No patient-level trajectory is reconstructed.

**Mechanical evidence recheck:** recorded_candidate. Both cited displays are confirmed; registered conditional time-definition question remains, and the missing definition prevents an unconditional incompatibility claim. Diagnostic: 1976/2=988; day-five total1971 exceeds988 by983. This is a conditional order-statistic diagnostic; inclusive postoperative day numbering can map four elapsed days to day5. Classification S_W; all S_W; statistical_results; no role/type code correction. Necessary missing inputs: Caption variable and calculation (ordinary or another follow-up summary), origin, inclusive-day convention, risk-time mapping and whether assessment duration differs from endpoint ascertainment. Human question: For eFigure 11 mortality, what variable/origin/inclusiveness defines median4(2–5), what time is day5 in the risk table, and are both the same observed-time summary? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (retain) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** Time-dependent denominators and follow-up summaries could be reused under incompatible definitions.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the follow-up duration or time-dependent risk denominator into an endpoint summary. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Open eFigure 11 on physical PDF p. 41; confirm the caption and baseline/day-5 risk cells. Ask which variable and calculation define median 4 (2–5), what time origin and inclusive convention define day 5, and which endpoint-specific events or censoring remove patients. Determine whether caption and risk-table times refer to the same observed-time summary before applying the conditional bound. Record the assessment below.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C088 — Mild respiratory failure: modeled-versus-crude comparator input error

Pending Human Adjudication.

**Candidate statement:** This retained record has evidence state record_input_error: its original comparator equated a planned GLM sensitivity estimate with a crude arm risk ratio without a supplied equivalence rule.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context

**Review domain:** report_internal_inconsistency

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Exact source locations:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Mild respiratory failure row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT. Corroborative PLAN context: [joi190055supp3_prod_16092.pdf — physical PDF p. 3](../joi190055supp3_prod_16092.pdf#page=3), sensitivity analysis specifying individual-component generalized linear models and Bonferroni confidence intervals.

**Source evidence:** Forest RR0.92[0.76,1.12],99.58%CI; matched main events high135/989,low154/987. The SAP explicitly specifies a GLM sensitivity analysis; the realized link, formula, adjustment/standardization, event and contrast coding, population and estimator output are not supplied.

**Reported-versus-comparator:** Original registered comparison, retained as history: Forest RR0.92[0.76,1.12],99.58%CI; matched main events high135/989,low154/987. The comparator is the crude ratio of these main-table risks; its identity with the sensitivity estimate is an unsupported premise.

**Reasoning procedure:** The forest tuple, risk-ratio header and main event counts are direct observations. The SAP independently identifies a planned sensitivity GLM. Calculate the crude ratio only as a diagnostic; matching endpoint names does not establish the same model, estimand or population. The original registration assumed that equivalence without a supplied rule, so this is record_input_error rather than an established contradiction of the fitted estimate.

**Calculation:** Historical conditional crude diagnostic: Under an explicitly crude arm-risk definition RR=(high events/high n)/(low events/low n)=(135/989)/(154/987)=0.874851. Printed 0.92 differs by0.045149. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR. Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005. Confidence-level adjustment does not turn a fitted model estimate into a crude ratio; the arithmetic difference does not reproduce or disprove the GLM output.

**Alternative source-grounded interpretations:** A model-defined ratio, adjustment or probability standardization, different event/contrast coding, or a different realized analysis population may explain the difference. The supplied SAP provides the GLM context, but not the realized link/formula, adjustment, population, coding or output. A crude mismatch alone therefore does not establish a wrong estimate or label. Forest intervals are positive, ordered and contain the printed points; their display width or clipping is not a separate contradiction.

**Mechanical evidence recheck:** record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (135/989)/(154/987)=0.874851; absolute distance from0.92=0.045149, larger than .005. Interval is positive, ordered and contains its printed point (0.76≤0.92≤1.12). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction. Necessary missing inputs: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Mild respiratory failure, what realized GLM/link/contrast/adjustment/population produced0.92, and does its RR mean the crude main-arm ratio or a model-defined ratio? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (discuss) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** This stable record documents an unsupported estimator-alignment input in the original registration and the remaining estimand-definition question. Human review must distinguish a modeled sensitivity effect from a crude main-table risk ratio before extraction.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the modeled sensitivity estimate as a crude arm risk ratio. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Confirm the endpoint-specific forest tuple on supplement p. 42 and matched component counts on main p. 9, including footnote b on p. 10. Read the SAP sensitivity paragraph on p. 3. Ask For Mild respiratory failure, what realized GLM/link/contrast/adjustment/population produced0.92, and does its RR mean the crude main-arm ratio or a model-defined ratio? Obtain the realized model specification and output, then assess whether any like-for-like discrepancy remains. The mechanical discuss suggestion does not fill the human Action field.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C089 — Moderate respiratory failure: modeled-versus-crude comparator input error

Pending Human Adjudication.

**Candidate statement:** This retained record has evidence state record_input_error: its original comparator equated a planned GLM sensitivity estimate with a crude arm risk ratio without a supplied equivalence rule.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context

**Review domain:** report_internal_inconsistency

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Exact source locations:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Moderate respiratory failure row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT. Corroborative PLAN context: [joi190055supp3_prod_16092.pdf — physical PDF p. 3](../joi190055supp3_prod_16092.pdf#page=3), sensitivity analysis specifying individual-component generalized linear models and Bonferroni confidence intervals.

**Source evidence:** Forest RR0.83[0.59,1.17],99.58%CI; matched main events high42/989,low58/987. The SAP explicitly specifies a GLM sensitivity analysis; the realized link, formula, adjustment/standardization, event and contrast coding, population and estimator output are not supplied.

**Reported-versus-comparator:** Original registered comparison, retained as history: Forest RR0.83[0.59,1.17],99.58%CI; matched main events high42/989,low58/987. The comparator is the crude ratio of these main-table risks; its identity with the sensitivity estimate is an unsupported premise.

**Reasoning procedure:** The forest tuple, risk-ratio header and main event counts are direct observations. The SAP independently identifies a planned sensitivity GLM. Calculate the crude ratio only as a diagnostic; matching endpoint names does not establish the same model, estimand or population. The original registration assumed that equivalence without a supplied rule, so this is record_input_error rather than an established contradiction of the fitted estimate.

**Calculation:** Historical conditional crude diagnostic: Under an explicitly crude arm-risk definition RR=(high events/high n)/(low events/low n)=(42/989)/(58/987)=0.722674. Printed 0.83 differs by0.107326. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR. Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005. Confidence-level adjustment does not turn a fitted model estimate into a crude ratio; the arithmetic difference does not reproduce or disprove the GLM output.

**Alternative source-grounded interpretations:** A model-defined ratio, adjustment or probability standardization, different event/contrast coding, or a different realized analysis population may explain the difference. The supplied SAP provides the GLM context, but not the realized link/formula, adjustment, population, coding or output. A crude mismatch alone therefore does not establish a wrong estimate or label. Forest intervals are positive, ordered and contain the printed points; their display width or clipping is not a separate contradiction.

**Mechanical evidence recheck:** record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (42/989)/(58/987)=0.722674; absolute distance from0.83=0.107326, larger than .005. Interval is positive, ordered and contains its printed point (0.59≤0.83≤1.17). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction. Necessary missing inputs: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Moderate respiratory failure, what realized GLM/link/contrast/adjustment/population produced0.83, and does its RR mean the crude main-arm ratio or a model-defined ratio? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (discuss) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** This stable record documents an unsupported estimator-alignment input in the original registration and the remaining estimand-definition question. Human review must distinguish a modeled sensitivity effect from a crude main-table risk ratio before extraction.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the modeled sensitivity estimate as a crude arm risk ratio. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Confirm the endpoint-specific forest tuple on supplement p. 42 and matched component counts on main p. 9, including footnote b on p. 10. Read the SAP sensitivity paragraph on p. 3. Ask For Moderate respiratory failure, what realized GLM/link/contrast/adjustment/population produced0.83, and does its RR mean the crude main-arm ratio or a model-defined ratio? Obtain the realized model specification and output, then assess whether any like-for-like discrepancy remains. The mechanical discuss suggestion does not fill the human Action field.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C090 — Severe respiratory failure: modeled-versus-crude comparator input error

Pending Human Adjudication.

**Candidate statement:** This retained record has evidence state record_input_error: its original comparator equated a planned GLM sensitivity estimate with a crude arm risk ratio without a supplied equivalence rule.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context

**Review domain:** report_internal_inconsistency

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Exact source locations:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Severe respiratory failure row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT. Corroborative PLAN context: [joi190055supp3_prod_16092.pdf — physical PDF p. 3](../joi190055supp3_prod_16092.pdf#page=3), sensitivity analysis specifying individual-component generalized linear models and Bonferroni confidence intervals.

**Source evidence:** Forest RR0.91[0.61,1.34],99.58%CI; matched main events high30/989,low36/987. The SAP explicitly specifies a GLM sensitivity analysis; the realized link, formula, adjustment/standardization, event and contrast coding, population and estimator output are not supplied.

**Reported-versus-comparator:** Original registered comparison, retained as history: Forest RR0.91[0.61,1.34],99.58%CI; matched main events high30/989,low36/987. The comparator is the crude ratio of these main-table risks; its identity with the sensitivity estimate is an unsupported premise.

**Reasoning procedure:** The forest tuple, risk-ratio header and main event counts are direct observations. The SAP independently identifies a planned sensitivity GLM. Calculate the crude ratio only as a diagnostic; matching endpoint names does not establish the same model, estimand or population. The original registration assumed that equivalence without a supplied rule, so this is record_input_error rather than an established contradiction of the fitted estimate.

**Calculation:** Historical conditional crude diagnostic: Under an explicitly crude arm-risk definition RR=(high events/high n)/(low events/low n)=(30/989)/(36/987)=0.831648. Printed 0.91 differs by0.078352. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR. Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005. Confidence-level adjustment does not turn a fitted model estimate into a crude ratio; the arithmetic difference does not reproduce or disprove the GLM output.

**Alternative source-grounded interpretations:** A model-defined ratio, adjustment or probability standardization, different event/contrast coding, or a different realized analysis population may explain the difference. The supplied SAP provides the GLM context, but not the realized link/formula, adjustment, population, coding or output. A crude mismatch alone therefore does not establish a wrong estimate or label. Forest intervals are positive, ordered and contain the printed points; their display width or clipping is not a separate contradiction.

**Mechanical evidence recheck:** record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (30/989)/(36/987)=0.831648; absolute distance from0.91=0.078352, larger than .005. Interval is positive, ordered and contains its printed point (0.61≤0.91≤1.34). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction. Necessary missing inputs: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Severe respiratory failure, what realized GLM/link/contrast/adjustment/population produced0.91, and does its RR mean the crude main-arm ratio or a model-defined ratio? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (discuss) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** This stable record documents an unsupported estimator-alignment input in the original registration and the remaining estimand-definition question. Human review must distinguish a modeled sensitivity effect from a crude main-table risk ratio before extraction.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the modeled sensitivity estimate as a crude arm risk ratio. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Confirm the endpoint-specific forest tuple on supplement p. 42 and matched component counts on main p. 9, including footnote b on p. 10. Read the SAP sensitivity paragraph on p. 3. Ask For Severe respiratory failure, what realized GLM/link/contrast/adjustment/population produced0.91, and does its RR mean the crude main-arm ratio or a model-defined ratio? Obtain the realized model specification and output, then assess whether any like-for-like discrepancy remains. The mechanical discuss suggestion does not fill the human Action field.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C091 — Aspiration: modeled-versus-crude comparator input error

Pending Human Adjudication.

**Candidate statement:** This retained record has evidence state record_input_error: its original comparator equated a planned GLM sensitivity estimate with a crude arm risk ratio without a supplied equivalence rule.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context

**Review domain:** report_internal_inconsistency

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Exact source locations:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Aspiration row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT. Corroborative PLAN context: [joi190055supp3_prod_16092.pdf — physical PDF p. 3](../joi190055supp3_prod_16092.pdf#page=3), sensitivity analysis specifying individual-component generalized linear models and Bonferroni confidence intervals.

**Source evidence:** Forest RR1.33[0.41,4.30],99.58%CI; matched main events high2/989,low1/987. The SAP explicitly specifies a GLM sensitivity analysis; the realized link, formula, adjustment/standardization, event and contrast coding, population and estimator output are not supplied.

**Reported-versus-comparator:** Original registered comparison, retained as history: Forest RR1.33[0.41,4.30],99.58%CI; matched main events high2/989,low1/987. The comparator is the crude ratio of these main-table risks; its identity with the sensitivity estimate is an unsupported premise.

**Reasoning procedure:** The forest tuple, risk-ratio header and main event counts are direct observations. The SAP independently identifies a planned sensitivity GLM. Calculate the crude ratio only as a diagnostic; matching endpoint names does not establish the same model, estimand or population. The original registration assumed that equivalence without a supplied rule, so this is record_input_error rather than an established contradiction of the fitted estimate.

**Calculation:** Historical conditional crude diagnostic: Under an explicitly crude arm-risk definition RR=(high events/high n)/(low events/low n)=(2/989)/(1/987)=1.995956. Printed 1.33 differs by0.665956. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR. Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005. Confidence-level adjustment does not turn a fitted model estimate into a crude ratio; the arithmetic difference does not reproduce or disprove the GLM output.

**Alternative source-grounded interpretations:** A model-defined ratio, adjustment or probability standardization, different event/contrast coding, or a different realized analysis population may explain the difference. The supplied SAP provides the GLM context, but not the realized link/formula, adjustment, population, coding or output. A crude mismatch alone therefore does not establish a wrong estimate or label. Forest intervals are positive, ordered and contain the printed points; their display width or clipping is not a separate contradiction.

**Mechanical evidence recheck:** record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (2/989)/(1/987)=1.995956; absolute distance from1.33=0.665956, larger than .005. Interval is positive, ordered and contains its printed point (0.41≤1.33≤4.30). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction. Necessary missing inputs: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Aspiration, what realized GLM/link/contrast/adjustment/population produced1.33, and does its RR mean the crude main-arm ratio or a model-defined ratio? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (discuss) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** This stable record documents an unsupported estimator-alignment input in the original registration and the remaining estimand-definition question. Human review must distinguish a modeled sensitivity effect from a crude main-table risk ratio before extraction.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the modeled sensitivity estimate as a crude arm risk ratio. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Confirm the endpoint-specific forest tuple on supplement p. 42 and matched component counts on main p. 9, including footnote b on p. 10. Read the SAP sensitivity paragraph on p. 3. Ask For Aspiration, what realized GLM/link/contrast/adjustment/population produced1.33, and does its RR mean the crude main-arm ratio or a model-defined ratio? Obtain the realized model specification and output, then assess whether any like-for-like discrepancy remains. The mechanical discuss suggestion does not fill the human Action field.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C092 — Bronchospasm: modeled-versus-crude comparator input error

Pending Human Adjudication.

**Candidate statement:** This retained record has evidence state record_input_error: its original comparator equated a planned GLM sensitivity estimate with a crude arm risk ratio without a supplied equivalence rule.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context

**Review domain:** report_internal_inconsistency

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Exact source locations:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Bronchospasm row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT. Corroborative PLAN context: [joi190055supp3_prod_16092.pdf — physical PDF p. 3](../joi190055supp3_prod_16092.pdf#page=3), sensitivity analysis specifying individual-component generalized linear models and Bonferroni confidence intervals.

**Source evidence:** Forest RR1.09[0.62,1.91],99.58%CI; matched main events high12/989,low10/987. The SAP explicitly specifies a GLM sensitivity analysis; the realized link, formula, adjustment/standardization, event and contrast coding, population and estimator output are not supplied.

**Reported-versus-comparator:** Original registered comparison, retained as history: Forest RR1.09[0.62,1.91],99.58%CI; matched main events high12/989,low10/987. The comparator is the crude ratio of these main-table risks; its identity with the sensitivity estimate is an unsupported premise.

**Reasoning procedure:** The forest tuple, risk-ratio header and main event counts are direct observations. The SAP independently identifies a planned sensitivity GLM. Calculate the crude ratio only as a diagnostic; matching endpoint names does not establish the same model, estimand or population. The original registration assumed that equivalence without a supplied rule, so this is record_input_error rather than an established contradiction of the fitted estimate.

**Calculation:** Historical conditional crude diagnostic: Under an explicitly crude arm-risk definition RR=(high events/high n)/(low events/low n)=(12/989)/(10/987)=1.197573. Printed 1.09 differs by0.107573. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR. Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005. Confidence-level adjustment does not turn a fitted model estimate into a crude ratio; the arithmetic difference does not reproduce or disprove the GLM output.

**Alternative source-grounded interpretations:** A model-defined ratio, adjustment or probability standardization, different event/contrast coding, or a different realized analysis population may explain the difference. The supplied SAP provides the GLM context, but not the realized link/formula, adjustment, population, coding or output. A crude mismatch alone therefore does not establish a wrong estimate or label. Forest intervals are positive, ordered and contain the printed points; their display width or clipping is not a separate contradiction.

**Mechanical evidence recheck:** record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (12/989)/(10/987)=1.197573; absolute distance from1.09=0.107573, larger than .005. Interval is positive, ordered and contains its printed point (0.62≤1.09≤1.91). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction. Necessary missing inputs: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Bronchospasm, what realized GLM/link/contrast/adjustment/population produced1.09, and does its RR mean the crude main-arm ratio or a model-defined ratio? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (discuss) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** This stable record documents an unsupported estimator-alignment input in the original registration and the remaining estimand-definition question. Human review must distinguish a modeled sensitivity effect from a crude main-table risk ratio before extraction.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the modeled sensitivity estimate as a crude arm risk ratio. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Confirm the endpoint-specific forest tuple on supplement p. 42 and matched component counts on main p. 9, including footnote b on p. 10. Read the SAP sensitivity paragraph on p. 3. Ask For Bronchospasm, what realized GLM/link/contrast/adjustment/population produced1.09, and does its RR mean the crude main-arm ratio or a model-defined ratio? Obtain the realized model specification and output, then assess whether any like-for-like discrepancy remains. The mechanical discuss suggestion does not fill the human Action field.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C093 — ARDS: modeled-versus-crude comparator input error

Pending Human Adjudication.

**Candidate statement:** This retained record has evidence state record_input_error: its original comparator equated a planned GLM sensitivity estimate with a crude arm risk ratio without a supplied equivalence rule.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context

**Review domain:** report_internal_inconsistency

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Exact source locations:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../joi190055supp4_prod_16092.pdf#page=42) eFigure12 ARDS row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT. Corroborative PLAN context: [joi190055supp3_prod_16092.pdf — physical PDF p. 3](../joi190055supp3_prod_16092.pdf#page=3), sensitivity analysis specifying individual-component generalized linear models and Bonferroni confidence intervals.

**Source evidence:** Forest RR1.50[0.65,3.44],99.58%CI; matched main events high3/989,low1/987. The SAP explicitly specifies a GLM sensitivity analysis; the realized link, formula, adjustment/standardization, event and contrast coding, population and estimator output are not supplied.

**Reported-versus-comparator:** Original registered comparison, retained as history: Forest RR1.50[0.65,3.44],99.58%CI; matched main events high3/989,low1/987. The comparator is the crude ratio of these main-table risks; its identity with the sensitivity estimate is an unsupported premise.

**Reasoning procedure:** The forest tuple, risk-ratio header and main event counts are direct observations. The SAP independently identifies a planned sensitivity GLM. Calculate the crude ratio only as a diagnostic; matching endpoint names does not establish the same model, estimand or population. The original registration assumed that equivalence without a supplied rule, so this is record_input_error rather than an established contradiction of the fitted estimate.

**Calculation:** Historical conditional crude diagnostic: Under an explicitly crude arm-risk definition RR=(high events/high n)/(low events/low n)=(3/989)/(1/987)=2.993933. Printed 1.50 differs by1.493933. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR. Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005. Confidence-level adjustment does not turn a fitted model estimate into a crude ratio; the arithmetic difference does not reproduce or disprove the GLM output.

**Alternative source-grounded interpretations:** A model-defined ratio, adjustment or probability standardization, different event/contrast coding, or a different realized analysis population may explain the difference. The supplied SAP provides the GLM context, but not the realized link/formula, adjustment, population, coding or output. A crude mismatch alone therefore does not establish a wrong estimate or label. Forest intervals are positive, ordered and contain the printed points; their display width or clipping is not a separate contradiction.

**Mechanical evidence recheck:** record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (3/989)/(1/987)=2.993933; absolute distance from1.50=1.493933, larger than .005. Interval is positive, ordered and contains its printed point (0.65≤1.50≤3.44). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction. Necessary missing inputs: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For ARDS, what realized GLM/link/contrast/adjustment/population produced1.50, and does its RR mean the crude main-arm ratio or a model-defined ratio? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (discuss) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** This stable record documents an unsupported estimator-alignment input in the original registration and the remaining estimand-definition question. Human review must distinguish a modeled sensitivity effect from a crude main-table risk ratio before extraction.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the modeled sensitivity estimate as a crude arm risk ratio. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Confirm the endpoint-specific forest tuple on supplement p. 42 and matched component counts on main p. 9, including footnote b on p. 10. Read the SAP sensitivity paragraph on p. 3. Ask For ARDS, what realized GLM/link/contrast/adjustment/population produced1.50, and does its RR mean the crude main-arm ratio or a model-defined ratio? Obtain the realized model specification and output, then assess whether any like-for-like discrepancy remains. The mechanical discuss suggestion does not fill the human Action field.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C094 — Atelectasis: modeled-versus-crude comparator input error

Pending Human Adjudication.

**Candidate statement:** This retained record has evidence state record_input_error: its original comparator equated a planned GLM sensitivity estimate with a crude arm risk ratio without a supplied equivalence rule.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context

**Review domain:** report_internal_inconsistency

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Exact source locations:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Atelectasis row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT. Corroborative PLAN context: [joi190055supp3_prod_16092.pdf — physical PDF p. 3](../joi190055supp3_prod_16092.pdf#page=3), sensitivity analysis specifying individual-component generalized linear models and Bonferroni confidence intervals.

**Source evidence:** Forest RR0.88[0.64,1.23],99.58%CI; matched main events high44/989,low55/987. The SAP explicitly specifies a GLM sensitivity analysis; the realized link, formula, adjustment/standardization, event and contrast coding, population and estimator output are not supplied.

**Reported-versus-comparator:** Original registered comparison, retained as history: Forest RR0.88[0.64,1.23],99.58%CI; matched main events high44/989,low55/987. The comparator is the crude ratio of these main-table risks; its identity with the sensitivity estimate is an unsupported premise.

**Reasoning procedure:** The forest tuple, risk-ratio header and main event counts are direct observations. The SAP independently identifies a planned sensitivity GLM. Calculate the crude ratio only as a diagnostic; matching endpoint names does not establish the same model, estimand or population. The original registration assumed that equivalence without a supplied rule, so this is record_input_error rather than an established contradiction of the fitted estimate.

**Calculation:** Historical conditional crude diagnostic: Under an explicitly crude arm-risk definition RR=(high events/high n)/(low events/low n)=(44/989)/(55/987)=0.798382. Printed 0.88 differs by0.081618. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR. Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005. Confidence-level adjustment does not turn a fitted model estimate into a crude ratio; the arithmetic difference does not reproduce or disprove the GLM output.

**Alternative source-grounded interpretations:** A model-defined ratio, adjustment or probability standardization, different event/contrast coding, or a different realized analysis population may explain the difference. The supplied SAP provides the GLM context, but not the realized link/formula, adjustment, population, coding or output. A crude mismatch alone therefore does not establish a wrong estimate or label. Forest intervals are positive, ordered and contain the printed points; their display width or clipping is not a separate contradiction.

**Mechanical evidence recheck:** record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (44/989)/(55/987)=0.798382; absolute distance from0.88=0.081618, larger than .005. Interval is positive, ordered and contains its printed point (0.64≤0.88≤1.23). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction. Necessary missing inputs: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Atelectasis, what realized GLM/link/contrast/adjustment/population produced0.88, and does its RR mean the crude main-arm ratio or a model-defined ratio? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (discuss) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** This stable record documents an unsupported estimator-alignment input in the original registration and the remaining estimand-definition question. Human review must distinguish a modeled sensitivity effect from a crude main-table risk ratio before extraction.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the modeled sensitivity estimate as a crude arm risk ratio. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Confirm the endpoint-specific forest tuple on supplement p. 42 and matched component counts on main p. 9, including footnote b on p. 10. Read the SAP sensitivity paragraph on p. 3. Ask For Atelectasis, what realized GLM/link/contrast/adjustment/population produced0.88, and does its RR mean the crude main-arm ratio or a model-defined ratio? Obtain the realized model specification and output, then assess whether any like-for-like discrepancy remains. The mechanical discuss suggestion does not fill the human Action field.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C095 — Cardiopulmonary edema: modeled-versus-crude comparator input error

Pending Human Adjudication.

**Candidate statement:** This retained record has evidence state record_input_error: its original comparator equated a planned GLM sensitivity estimate with a crude arm risk ratio without a supplied equivalence rule.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context

**Review domain:** report_internal_inconsistency

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Exact source locations:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Cardiopulmonary edema row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT. Corroborative PLAN context: [joi190055supp3_prod_16092.pdf — physical PDF p. 3](../joi190055supp3_prod_16092.pdf#page=3), sensitivity analysis specifying individual-component generalized linear models and Bonferroni confidence intervals.

**Source evidence:** Forest RR1.31[0.87,1.98],99.58%CI; matched main events high17/989,low9/987. The SAP explicitly specifies a GLM sensitivity analysis; the realized link, formula, adjustment/standardization, event and contrast coding, population and estimator output are not supplied.

**Reported-versus-comparator:** Original registered comparison, retained as history: Forest RR1.31[0.87,1.98],99.58%CI; matched main events high17/989,low9/987. The comparator is the crude ratio of these main-table risks; its identity with the sensitivity estimate is an unsupported premise.

**Reasoning procedure:** The forest tuple, risk-ratio header and main event counts are direct observations. The SAP independently identifies a planned sensitivity GLM. Calculate the crude ratio only as a diagnostic; matching endpoint names does not establish the same model, estimand or population. The original registration assumed that equivalence without a supplied rule, so this is record_input_error rather than an established contradiction of the fitted estimate.

**Calculation:** Historical conditional crude diagnostic: Under an explicitly crude arm-risk definition RR=(high events/high n)/(low events/low n)=(17/989)/(9/987)=1.885069. Printed 1.31 differs by0.575069. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR. Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005. Confidence-level adjustment does not turn a fitted model estimate into a crude ratio; the arithmetic difference does not reproduce or disprove the GLM output.

**Alternative source-grounded interpretations:** A model-defined ratio, adjustment or probability standardization, different event/contrast coding, or a different realized analysis population may explain the difference. The supplied SAP provides the GLM context, but not the realized link/formula, adjustment, population, coding or output. A crude mismatch alone therefore does not establish a wrong estimate or label. Forest intervals are positive, ordered and contain the printed points; their display width or clipping is not a separate contradiction.

**Mechanical evidence recheck:** record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (17/989)/(9/987)=1.885069; absolute distance from1.31=0.575069, larger than .005. Interval is positive, ordered and contains its printed point (0.87≤1.31≤1.98). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction. Necessary missing inputs: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Cardiopulmonary edema, what realized GLM/link/contrast/adjustment/population produced1.31, and does its RR mean the crude main-arm ratio or a model-defined ratio? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (discuss) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** This stable record documents an unsupported estimator-alignment input in the original registration and the remaining estimand-definition question. Human review must distinguish a modeled sensitivity effect from a crude main-table risk ratio before extraction.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the modeled sensitivity estimate as a crude arm risk ratio. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Confirm the endpoint-specific forest tuple on supplement p. 42 and matched component counts on main p. 9, including footnote b on p. 10. Read the SAP sensitivity paragraph on p. 3. Ask For Cardiopulmonary edema, what realized GLM/link/contrast/adjustment/population produced1.31, and does its RR mean the crude main-arm ratio or a model-defined ratio? Obtain the realized model specification and output, then assess whether any like-for-like discrepancy remains. The mechanical discuss suggestion does not fill the human Action field.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C096 — Pleural effusion: modeled-versus-crude comparator input error

Pending Human Adjudication.

**Candidate statement:** This retained record has evidence state record_input_error: its original comparator equated a planned GLM sensitivity estimate with a crude arm risk ratio without a supplied equivalence rule.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context

**Review domain:** report_internal_inconsistency

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Exact source locations:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Pleural effusion row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT. Corroborative PLAN context: [joi190055supp3_prod_16092.pdf — physical PDF p. 3](../joi190055supp3_prod_16092.pdf#page=3), sensitivity analysis specifying individual-component generalized linear models and Bonferroni confidence intervals.

**Source evidence:** Forest RR1.36[1.05,1.76],99.58%CI; matched main events high43/989,low21/987. The SAP explicitly specifies a GLM sensitivity analysis; the realized link, formula, adjustment/standardization, event and contrast coding, population and estimator output are not supplied.

**Reported-versus-comparator:** Original registered comparison, retained as history: Forest RR1.36[1.05,1.76],99.58%CI; matched main events high43/989,low21/987. The comparator is the crude ratio of these main-table risks; its identity with the sensitivity estimate is an unsupported premise.

**Reasoning procedure:** The forest tuple, risk-ratio header and main event counts are direct observations. The SAP independently identifies a planned sensitivity GLM. Calculate the crude ratio only as a diagnostic; matching endpoint names does not establish the same model, estimand or population. The original registration assumed that equivalence without a supplied rule, so this is record_input_error rather than an established contradiction of the fitted estimate.

**Calculation:** Historical conditional crude diagnostic: Under an explicitly crude arm-risk definition RR=(high events/high n)/(low events/low n)=(43/989)/(21/987)=2.043478. Printed 1.36 differs by0.683478. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR. Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005. Confidence-level adjustment does not turn a fitted model estimate into a crude ratio; the arithmetic difference does not reproduce or disprove the GLM output.

**Alternative source-grounded interpretations:** A model-defined ratio, adjustment or probability standardization, different event/contrast coding, or a different realized analysis population may explain the difference. The supplied SAP provides the GLM context, but not the realized link/formula, adjustment, population, coding or output. A crude mismatch alone therefore does not establish a wrong estimate or label. Forest intervals are positive, ordered and contain the printed points; their display width or clipping is not a separate contradiction.

**Mechanical evidence recheck:** record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (43/989)/(21/987)=2.043478; absolute distance from1.36=0.683478, larger than .005. Interval is positive, ordered and contains its printed point (1.05≤1.36≤1.76). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction. Necessary missing inputs: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Pleural effusion, what realized GLM/link/contrast/adjustment/population produced1.36, and does its RR mean the crude main-arm ratio or a model-defined ratio? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (discuss) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** This stable record documents an unsupported estimator-alignment input in the original registration and the remaining estimand-definition question. Human review must distinguish a modeled sensitivity effect from a crude main-table risk ratio before extraction.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the modeled sensitivity estimate as a crude arm risk ratio. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Confirm the endpoint-specific forest tuple on supplement p. 42 and matched component counts on main p. 9, including footnote b on p. 10. Read the SAP sensitivity paragraph on p. 3. Ask For Pleural effusion, what realized GLM/link/contrast/adjustment/population produced1.36, and does its RR mean the crude main-arm ratio or a model-defined ratio? Obtain the realized model specification and output, then assess whether any like-for-like discrepancy remains. The mechanical discuss suggestion does not fill the human Action field.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C097 — Pneumothorax: modeled-versus-crude comparator input error

Pending Human Adjudication.

**Candidate statement:** This retained record has evidence state record_input_error: its original comparator equated a planned GLM sensitivity estimate with a crude arm risk ratio without a supplied equivalence rule.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context

**Review domain:** report_internal_inconsistency

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Exact source locations:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Pneumothorax row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT. Corroborative PLAN context: [joi190055supp3_prod_16092.pdf — physical PDF p. 3](../joi190055supp3_prod_16092.pdf#page=3), sensitivity analysis specifying individual-component generalized linear models and Bonferroni confidence intervals.

**Source evidence:** Forest RR0.50[0.04,5.96],99.58%CI; matched main events high1/989,low3/987. The SAP explicitly specifies a GLM sensitivity analysis; the realized link, formula, adjustment/standardization, event and contrast coding, population and estimator output are not supplied.

**Reported-versus-comparator:** Original registered comparison, retained as history: Forest RR0.50[0.04,5.96],99.58%CI; matched main events high1/989,low3/987. The comparator is the crude ratio of these main-table risks; its identity with the sensitivity estimate is an unsupported premise.

**Reasoning procedure:** The forest tuple, risk-ratio header and main event counts are direct observations. The SAP independently identifies a planned sensitivity GLM. Calculate the crude ratio only as a diagnostic; matching endpoint names does not establish the same model, estimand or population. The original registration assumed that equivalence without a supplied rule, so this is record_input_error rather than an established contradiction of the fitted estimate.

**Calculation:** Historical conditional crude diagnostic: Under an explicitly crude arm-risk definition RR=(high events/high n)/(low events/low n)=(1/989)/(3/987)=0.332659. Printed 0.50 differs by0.167341. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR. Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005. Confidence-level adjustment does not turn a fitted model estimate into a crude ratio; the arithmetic difference does not reproduce or disprove the GLM output.

**Alternative source-grounded interpretations:** A model-defined ratio, adjustment or probability standardization, different event/contrast coding, or a different realized analysis population may explain the difference. The supplied SAP provides the GLM context, but not the realized link/formula, adjustment, population, coding or output. A crude mismatch alone therefore does not establish a wrong estimate or label. Forest intervals are positive, ordered and contain the printed points; their display width or clipping is not a separate contradiction.

**Mechanical evidence recheck:** record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (1/989)/(3/987)=0.332659; absolute distance from0.50=0.167341, larger than .005. Interval is positive, ordered and contains its printed point (0.04≤0.50≤5.96). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction. Necessary missing inputs: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Pneumothorax, what realized GLM/link/contrast/adjustment/population produced0.50, and does its RR mean the crude main-arm ratio or a model-defined ratio? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (discuss) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** This stable record documents an unsupported estimator-alignment input in the original registration and the remaining estimand-definition question. Human review must distinguish a modeled sensitivity effect from a crude main-table risk ratio before extraction.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the modeled sensitivity estimate as a crude arm risk ratio. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Confirm the endpoint-specific forest tuple on supplement p. 42 and matched component counts on main p. 9, including footnote b on p. 10. Read the SAP sensitivity paragraph on p. 3. Ask For Pneumothorax, what realized GLM/link/contrast/adjustment/population produced0.50, and does its RR mean the crude main-arm ratio or a model-defined ratio? Obtain the realized model specification and output, then assess whether any like-for-like discrepancy remains. The mechanical discuss suggestion does not fill the human Action field.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C098 — Pulmonary infiltrates: modeled-versus-crude comparator input error

Pending Human Adjudication.

**Candidate statement:** This retained record has evidence state record_input_error: its original comparator equated a planned GLM sensitivity estimate with a crude arm risk ratio without a supplied equivalence rule.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context

**Review domain:** report_internal_inconsistency

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Exact source locations:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Pulmonary infiltrates row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT. Corroborative PLAN context: [joi190055supp3_prod_16092.pdf — physical PDF p. 3](../joi190055supp3_prod_16092.pdf#page=3), sensitivity analysis specifying individual-component generalized linear models and Bonferroni confidence intervals.

**Source evidence:** Forest RR0.87[0.49,1.55],99.58%CI; matched main events high14/989,low18/987. The SAP explicitly specifies a GLM sensitivity analysis; the realized link, formula, adjustment/standardization, event and contrast coding, population and estimator output are not supplied.

**Reported-versus-comparator:** Original registered comparison, retained as history: Forest RR0.87[0.49,1.55],99.58%CI; matched main events high14/989,low18/987. The comparator is the crude ratio of these main-table risks; its identity with the sensitivity estimate is an unsupported premise.

**Reasoning procedure:** The forest tuple, risk-ratio header and main event counts are direct observations. The SAP independently identifies a planned sensitivity GLM. Calculate the crude ratio only as a diagnostic; matching endpoint names does not establish the same model, estimand or population. The original registration assumed that equivalence without a supplied rule, so this is record_input_error rather than an established contradiction of the fitted estimate.

**Calculation:** Historical conditional crude diagnostic: Under an explicitly crude arm-risk definition RR=(high events/high n)/(low events/low n)=(14/989)/(18/987)=0.776205. Printed 0.87 differs by0.093795. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR. Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005. Confidence-level adjustment does not turn a fitted model estimate into a crude ratio; the arithmetic difference does not reproduce or disprove the GLM output.

**Alternative source-grounded interpretations:** A model-defined ratio, adjustment or probability standardization, different event/contrast coding, or a different realized analysis population may explain the difference. The supplied SAP provides the GLM context, but not the realized link/formula, adjustment, population, coding or output. A crude mismatch alone therefore does not establish a wrong estimate or label. Forest intervals are positive, ordered and contain the printed points; their display width or clipping is not a separate contradiction.

**Mechanical evidence recheck:** record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (14/989)/(18/987)=0.776205; absolute distance from0.87=0.093795, larger than .005. Interval is positive, ordered and contains its printed point (0.49≤0.87≤1.55). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction. Necessary missing inputs: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Pulmonary infiltrates, what realized GLM/link/contrast/adjustment/population produced0.87, and does its RR mean the crude main-arm ratio or a model-defined ratio? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (discuss) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** This stable record documents an unsupported estimator-alignment input in the original registration and the remaining estimand-definition question. Human review must distinguish a modeled sensitivity effect from a crude main-table risk ratio before extraction.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the modeled sensitivity estimate as a crude arm risk ratio. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Confirm the endpoint-specific forest tuple on supplement p. 42 and matched component counts on main p. 9, including footnote b on p. 10. Read the SAP sensitivity paragraph on p. 3. Ask For Pulmonary infiltrates, what realized GLM/link/contrast/adjustment/population produced0.87, and does its RR mean the crude main-arm ratio or a model-defined ratio? Obtain the realized model specification and output, then assess whether any like-for-like discrepancy remains. The mechanical discuss suggestion does not fill the human Action field.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C099 — Revised PLAN target versus retained procedural total

Pending Human Adjudication.

**Candidate statement:** The same protocol version explicitly revises the total to 2013 but retains a future-tense procedure statement of 748. The initial 748 is historical in section 6.4; whether section 7.2 intentionally retains historical wording requires human confirmation.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol current procedure total versus PLAN protocol revised sample/recruitment target; PLAN amendment corroborates

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R.

**Classification ambiguity:** Historical intent of section7.2 is not stated; no REPORT comparator creates P_R.

**Exact source locations:** PLAN [joi190055supp1_prod_16092.pdf — physical PDF p. 10, printed p. 9](../joi190055supp1_prod_16092.pdf#page=10), current recruitment target; [physical PDF p. 11, printed p. 10](../joi190055supp1_prod_16092.pdf#page=11), version 2.6 section 6.4; [physical PDF p. 12, printed p. 11](../joi190055supp1_prod_16092.pdf#page=12), section 7.2. Corroborative PLAN [joi190055supp2_prod_16092.pdf — physical PDF p. 2](../joi190055supp2_prod_16092.pdf#page=2), revised sample target.

**Source evidence:** The current recruitment statement gives 2013. Section 6.4 explicitly distinguishes initial 748 from revised total 2013. Section 7.2 states, “In total,748 patients will be included.” The amendment corroborates the revised total.

**Reported-versus-comparator:** Section 7.2 future-tense total 748 versus the same version’s explicitly revised total 2013; the historical 748 in section 6.4 is not itself conflicting.

**Reasoning procedure:** Directly compare the same-version current-total statements and their historical qualifiers. The rule is identity of the intended current planned enrollment total, conditional on section 7.2 remaining an operative procedure. No REPORT conflict or actual enrollment error is inferred.

**Calculation:** 2013 − 748 = 1265 participants. Both printed totals are exact integers; no rounding tolerance applies. The subtraction quantifies the displayed difference and does not establish the historical intent of section 7.2.

**Alternative source-grounded interpretations:** Section 7.2 may be an unupdated procedural paragraph or an intentionally retained historical passage without an explicit historical label. The intended status of that future-tense paragraph is missing. The amendment supplies the revision; this record does not accuse an unlogged amendment.

**Mechanical evidence recheck:** recorded_candidate. Current source confirms future-tense748 alongside explicitly revised2013 in the same PLAN version. Diagnostic: 2013−748=1265. The initial748 is explicitly historical in section6.4, but section7.2 retains a current future-tense total. Classification P_P; all P_P; plan_material; no role/type code correction. Necessary missing inputs: Whether section7.2 was intended as retained historical text despite future tense. Human question: In version2.6, does section7.2 still prescribe748 or retain a historical paragraph; what current total was intended? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (retain) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** A plan summary requires a distinguishable current sample target and historical procedure wording.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the retained enrollment target into a plan summary. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Read version 2.6 sections 6.4 and 7.2 alongside the current recruitment statement and amendment. Ask whether section 7.2 was intended to prescribe 748 or retain a historical paragraph, and which current target was intended. Record the answer below; do not change an actual enrolled total based on this wording comparison.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C100 — Conditional futility-region comparison at look 1

Pending Human Adjudication.

**Candidate statement:** Under a common signed-Z definition, the look-1 table inequality Z < 0.225 differs from the central graphical futility set. Missing contrast, sign/magnitude mapping and rule priority prevent an unconditional monitoring-error inference.

**Category:** Statistical reporting inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol monitoring table look1 versus PLAN protocol boundary figure at enrollment956; PLAN amendment and REPORT supplement repeated graphic corroborate

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R.

**Classification ambiguity:** Different benefit-oriented and treatment-risk-oriented Z can reconcile design. Corroborating REPORT graphic does not add P_R; both discrepancy locations remain PLAN.

**Exact source locations:** [joi190055supp1_prod_16092.pdf PDF p.22](../joi190055supp1_prod_16092.pdf#page=22), PLAN, look1 Z-futility cell; [joi190055supp1_prod_16092.pdf PDF p.23](../joi190055supp1_prod_16092.pdf#page=23), PLAN, central pink Futility region at enrollment956. [joi190055supp4_prod_16092.pdf PDF p.31](../joi190055supp4_prod_16092.pdf#page=31), REPORT, corroborates the central graphical region. [joi190055supp2_prod_16092.pdf PDF p.3](../joi190055supp2_prod_16092.pdf#page=3), PLAN, confirms that the table and figure were introduced for the same revised monitoring design.

**Source evidence:** The table gives Z<0.225. The plot marks the pink Futility area between a negative inner boundary and its positive counterpart. Values below the negative inner boundary are outside the graphical futility area.

**Reported-versus-comparator:** Look 1, N = 956: printed table futility Z < 0.225, versus a central pink graphical Futility region between negative and positive inner boundaries. The plot does not independently print exact boundary coordinates.

**Reasoning procedure:** The inequality, signed axis and colored region are direct. Any statement that the graphical boundary is exactly±0.225 is a magnitude alignment only. Apply the logical comparison only if table and plot use the same signed statistic and contrast. Contrast/sign definitions, efficacy-oriented versus risk-oriented convention, magnitude transformation and harm/futility/efficacy priority are missing. No observed stopping Z path is supplied, so no actual trial decision is inferred.

**Calculation:** Witness Z = −4 satisfies −4 < 0.225, but is outside the central pink graphical region at N = 956. Under a common signed Z, the sets differ. The witness avoids exact boundary digitization; no numerical tolerance is assigned to an unprinted graphical coordinate.

**Alternative source-grounded interpretations:** The table could summarize a one-sided alternative-oriented rule, while the figure additionally partitions efficacy/harm; it might also intend |Z| in the table. No absolute-value notation or rule-priority/sign-conversion explanation is supplied. At look3 the efficacy and futility table entries form complementary regions of a single signed statistic, whereas the figure includes both harm and efficacy outer tails.

**Mechanical evidence recheck:** recorded_candidate. Current table and render reproduce the registered conditional direction/region comparison; sign-convention mapping remains the precise missing definition. Diagnostic: Z=−4 satisfies Z<+0.225 but lies outside the pink central region at N956. Thus these sets differ under a common signed-Z interpretation. Classification P_P; all P_P; plan_material; no role/type code correction. Necessary missing inputs: Z contrast/sign definition in each display, efficacy-oriented versus risk-oriented convention, magnitude/absolute-value transformation and rule priority (including harm). Human question: At look1 N956, are table and plot the same signed Z; if different, what contrasts/sign transformation and futility/harm rule priority map the one-sided inequality to central region? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (retain) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** Extraction of a futility stopping region requires the sign and rule definition. This is distinct from PP-Z1's efficacy-tail sign comparison because it compares a different cell and interval-region rule.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the stopping-boundary sign or region into a monitoring-plan summary. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Open the exact source pages above and compare the cited cells or statements. Recompute the stated arithmetic or logical diagnostic using the printed inputs, retaining the named conditions and display tolerance. Resolve this source-specific question: Is the table's Z a signed statistic, a magnitude, or a one-sided alternative-oriented convention? What mapping/rule priority relates the tabulated futility inequality to the figure's central region? Record the human assessment in the five blank fields below.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C101 — Conditional futility-region comparison at look 2

Pending Human Adjudication.

**Candidate statement:** Under a common signed-Z definition, the look-2 table inequality Z < 0.929 differs from the central graphical futility set. Missing contrast, sign/magnitude mapping and rule priority prevent an unconditional monitoring-error inference.

**Category:** Statistical reporting inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol monitoring table look2 versus PLAN protocol boundary figure at enrollment1434; PLAN amendment and REPORT supplement repeated graphic corroborate

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R.

**Classification ambiguity:** Different benefit-oriented and treatment-risk-oriented Z can reconcile design. Corroborating REPORT graphic does not add P_R; both discrepancy locations remain PLAN.

**Exact source locations:** [joi190055supp1_prod_16092.pdf PDF p.22](../joi190055supp1_prod_16092.pdf#page=22), PLAN, look2 Z-futility cell; [joi190055supp1_prod_16092.pdf PDF p.23](../joi190055supp1_prod_16092.pdf#page=23), PLAN, central pink Futility region at enrollment1434. [joi190055supp4_prod_16092.pdf PDF p.31](../joi190055supp4_prod_16092.pdf#page=31), REPORT, corroborates the central graphical region. [joi190055supp2_prod_16092.pdf PDF p.3](../joi190055supp2_prod_16092.pdf#page=3), PLAN, confirms that the table and figure were introduced for the same revised monitoring design.

**Source evidence:** The table gives Z<0.929. The plot marks the pink Futility area between a negative inner boundary and its positive counterpart. Values below the negative inner boundary are outside the graphical futility area.

**Reported-versus-comparator:** Look 2, N = 1434: printed table futility Z < 0.929, versus a central pink graphical Futility region between negative and positive inner boundaries. The plot does not independently print exact boundary coordinates.

**Reasoning procedure:** The inequality, signed axis and colored region are direct. Any statement that the graphical boundary is exactly±0.929 is a magnitude alignment only. Apply the logical comparison only if table and plot use the same signed statistic and contrast. Contrast/sign definitions, efficacy-oriented versus risk-oriented convention, magnitude transformation and harm/futility/efficacy priority are missing. No observed stopping Z path is supplied, so no actual trial decision is inferred.

**Calculation:** Witness Z = −4 satisfies −4 < 0.929, but is outside the central pink graphical region at N = 1434. Under a common signed Z, the sets differ. The witness avoids exact boundary digitization; no numerical tolerance is assigned to an unprinted graphical coordinate.

**Alternative source-grounded interpretations:** The table could summarize a one-sided alternative-oriented rule, while the figure additionally partitions efficacy/harm; it might also intend |Z| in the table. No absolute-value notation or rule-priority/sign-conversion explanation is supplied. At look3 the efficacy and futility table entries form complementary regions of a single signed statistic, whereas the figure includes both harm and efficacy outer tails.

**Mechanical evidence recheck:** recorded_candidate. Current table and render reproduce the registered conditional direction/region comparison; sign-convention mapping remains the precise missing definition. Diagnostic: Z=−4 satisfies Z<+0.929 but lies outside the pink central region at N1434. Thus these sets differ under a common signed-Z interpretation. Classification P_P; all P_P; plan_material; no role/type code correction. Necessary missing inputs: Z contrast/sign definition in each display, efficacy-oriented versus risk-oriented convention, magnitude/absolute-value transformation and rule priority (including harm). Human question: At look2 N1434, are table and plot the same signed Z; if different, what contrasts/sign transformation and futility/harm rule priority map the one-sided inequality to central region? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (retain) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** Extraction of a futility stopping region requires the sign and rule definition. This is distinct from PP-Z2's efficacy-tail sign comparison because it compares a different cell and interval-region rule.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the stopping-boundary sign or region into a monitoring-plan summary. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Open the exact source pages above and compare the cited cells or statements. Recompute the stated arithmetic or logical diagnostic using the printed inputs, retaining the named conditions and display tolerance. Resolve this source-specific question: Is the table's Z a signed statistic, a magnitude, or a one-sided alternative-oriented convention? What mapping/rule priority relates the tabulated futility inequality to the figure's central region? Record the human assessment in the five blank fields below.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C102 — Conditional futility-region comparison at look 3

Pending Human Adjudication.

**Candidate statement:** Under a common signed-Z definition, the look-3 table inequality Z < 2.012 differs from the central graphical futility set. Missing contrast, sign/magnitude mapping and rule priority prevent an unconditional monitoring-error inference.

**Category:** Statistical reporting inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol monitoring table look3 versus PLAN protocol boundary figure at enrollment1912; PLAN amendment and REPORT supplement repeated graphic corroborate

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R.

**Classification ambiguity:** Different benefit-oriented and treatment-risk-oriented Z can reconcile design. Corroborating REPORT graphic does not add P_R; both discrepancy locations remain PLAN.

**Exact source locations:** [joi190055supp1_prod_16092.pdf PDF p.22](../joi190055supp1_prod_16092.pdf#page=22), PLAN, look3 Z-futility cell; [joi190055supp1_prod_16092.pdf PDF p.23](../joi190055supp1_prod_16092.pdf#page=23), PLAN, central pink Futility region at enrollment1912. [joi190055supp4_prod_16092.pdf PDF p.31](../joi190055supp4_prod_16092.pdf#page=31), REPORT, corroborates the central graphical region. [joi190055supp2_prod_16092.pdf PDF p.3](../joi190055supp2_prod_16092.pdf#page=3), PLAN, confirms that the table and figure were introduced for the same revised monitoring design.

**Source evidence:** The table gives Z<2.012. The plot marks the pink Futility area between a negative inner boundary and its positive counterpart. Values below the negative inner boundary are outside the graphical futility area.

**Reported-versus-comparator:** Look 3, N = 1912: printed table futility Z < 2.012, versus a central pink graphical Futility region between negative and positive inner boundaries. The plot does not independently print exact boundary coordinates.

**Reasoning procedure:** The inequality, signed axis and colored region are direct. Any statement that the graphical boundary is exactly±2.012 is a magnitude alignment only. Apply the logical comparison only if table and plot use the same signed statistic and contrast. Contrast/sign definitions, efficacy-oriented versus risk-oriented convention, magnitude transformation and harm/futility/efficacy priority are missing. No observed stopping Z path is supplied, so no actual trial decision is inferred.

**Calculation:** Witness Z = −4 satisfies −4 < 2.012, but is outside the central pink graphical region at N = 1912. Under a common signed Z, the sets differ. The witness avoids exact boundary digitization; no numerical tolerance is assigned to an unprinted graphical coordinate.

**Alternative source-grounded interpretations:** The table could summarize a one-sided alternative-oriented rule, while the figure additionally partitions efficacy/harm; it might also intend |Z| in the table. No absolute-value notation or rule-priority/sign-conversion explanation is supplied. At look3 the efficacy and futility table entries form complementary regions of a single signed statistic, whereas the figure includes both harm and efficacy outer tails.

**Mechanical evidence recheck:** recorded_candidate. Current table and render reproduce the registered conditional direction/region comparison; sign-convention mapping remains the precise missing definition. Diagnostic: Z=−4 satisfies Z<+2.012 but lies outside the pink central region at N1912. Thus these sets differ under a common signed-Z interpretation. Classification P_P; all P_P; plan_material; no role/type code correction. Necessary missing inputs: Z contrast/sign definition in each display, efficacy-oriented versus risk-oriented convention, magnitude/absolute-value transformation and rule priority (including harm). Human question: At look3 N1912, are table and plot the same signed Z; if different, what contrasts/sign transformation and futility/harm rule priority map the one-sided inequality to central region? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (retain) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** Extraction of a futility stopping region requires the sign and rule definition. This is distinct from PP-Z3's efficacy-tail sign comparison because it compares a different cell and interval-region rule.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the stopping-boundary sign or region into a monitoring-plan summary. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Open the exact source pages above and compare the cited cells or statements. Recompute the stated arithmetic or logical diagnostic using the printed inputs, retaining the named conditions and display tolerance. Resolve this source-specific question: Is the table's Z a signed statistic, a magnitude, or a one-sided alternative-oriented convention? What mapping/rule priority relates the tabulated futility inequality to the figure's central region? Record the human assessment in the five blank fields below.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C103 — Original primary-analysis effect label combines OR and RR

Pending Human Adjudication.

**Candidate statement:** Original primary-analysis effect label combines OR and RR; the compared display or definition requires human reconciliation under the stated rule.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol primary-analysis sentence containing both measure terms; PLAN updated SAP is later explanatory context

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R.

**Classification ambiguity:** Later SAP may supersede original wording; it does not remove the original PLAN-internal label question.

**Exact source locations:** [joi190055supp1_prod_16092.pdf PDF p.23](../joi190055supp1_prod_16092.pdf#page=23), PLAN, same primary-efficacy-analysis sentence. Both compared labels are PLAN content. [joi190055supp3_prod_16092.pdf PDF p.2](../joi190055supp3_prod_16092.pdf#page=2), PLAN, subsequently specifies risk ratio and is an explanatory later-plan comparator; it does not remove the original sentence's displayed labels. Planning probabilities for the illustration: PLAN [joi190055supp1_prod_16092.pdf — physical PDF p. 11, printed p. 10](../joi190055supp1_prod_16092.pdf#page=11), sample-size assumptions.

**Source evidence:** Original primary phrase is “odds ratio relative risks” with corresponding95% confidence interval calculated using logistic regression. The adjacent words were confirmed in the PDF image; they are not a locator/OCR repair.

**Reported-versus-comparator:** Original primary phrase is “odds ratio relative risks” with corresponding95% confidence interval calculated using logistic regression. The adjacent words were confirmed in the PDF image; they are not a locator/OCR repair. 

**Reasoning procedure:** Two different effect-measure terms printed together are direct. The planned-probability calculation illustrates distinction; it does not establish which effect was intended. Intended measure(s), contrast and logistic postprocessing for original sentence. Human question: Which measure(s), contrast and postprocessing did the original primary sentence intend, and which measure labels its interval?

**Calculation:** OR=[pH/(1−pH)]/[pL/(1−pL)] and RR=pH/pL are distinct scales. Within the original declared sample assumptions pH=.30,pL=.40, RR=.75 while OR=(.30/.70)/(.40/.60)=.642857. This illustrative calculation uses supplied planning probabilities; it is not an observed-result recalculation. The probabilities are supplied planning assumptions, not observed trial rates. Arithmetic is exact at the supplied two-decimal inputs; 0.642857 is a rounded diagnostic. Logistic regression alone does not determine whether a postprocessed estimate is an OR or RR.

**Alternative source-grounded interpretations:** The phrase may represent an unfinished replacement of OR by RR, or may intend two effects. Logistic regression can be followed by probability standardization, so its mention alone does not identify the effect.

**Mechanical evidence recheck:** recorded_candidate. Current render confirms adjacent odds ratio relative risks; source-label ambiguity reproduces without relying on an OCR error. Diagnostic: For supplied assumptions RR=.30/.40=.75; OR=(.30/.70)/(.40/.60)=.642857. This illustrates scale difference, not an observed-result recalculation. Classification P_P; all P_P; plan_material; no role/type code correction. Necessary missing inputs: Intended measure(s), contrast and logistic postprocessing for original sentence. Human question: Which measure(s), contrast and postprocessing did the original primary sentence intend, and which measure labels its interval? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (retain) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** A reader extracting the original plan cannot uniquely label the effect from this sentence.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the effect-measure label into an extraction of the original plan. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Open the exact source pages above and compare the cited cells or statements. Recompute the stated arithmetic or logical diagnostic using the printed inputs, retaining the named conditions and display tolerance. Resolve this source-specific question: Which measure(s), contrast and logistic postprocessing were intended by the original sentence, and which label belongs to the associated interval? The later SAP gives RR but should not silently rewrite the preserved original source. Record the human assessment in the five blank fields below.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C104 — Conditional efficacy-sign comparison at look 1

Pending Human Adjudication.

**Candidate statement:** Under a common signed-Z definition, the look-1 table inequality Z ≥ 2.75 has the opposite orientation to the negative graphical Efficacy region. Missing contrast, sign/magnitude mapping and rule priority prevent an unconditional monitoring-error inference.

**Category:** Statistical reporting inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol monitoring table look1 versus PLAN protocol boundary figure at enrollment956; PLAN amendment and REPORT supplement repeated graphic corroborate

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R.

**Classification ambiguity:** Different benefit-oriented and treatment-risk-oriented Z can reconcile design. Corroborating REPORT graphic does not add P_R; both discrepancy locations remain PLAN.

**Exact source locations:** [joi190055supp1_prod_16092.pdf PDF p.22](../joi190055supp1_prod_16092.pdf#page=22), PLAN, statistical-analysis table, look1 efficacy; [joi190055supp1_prod_16092.pdf PDF p.23](../joi190055supp1_prod_16092.pdf#page=23), PLAN, stopping-boundary figure, Efficacy region at enrollment956. [joi190055supp4_prod_16092.pdf PDF p.31](../joi190055supp4_prod_16092.pdf#page=31), REPORT, reproduces the negative-Z efficacy graphical orientation and corroborates the figure side; [joi190055supp2_prod_16092.pdf PDF p.3](../joi190055supp2_prod_16092.pdf#page=3), PLAN, amendment explicitly introduces the same table/figure but adds no signed contrast definition. The REPORT location corroborates rather than creates an additional discrepancy.

**Source evidence:** The table calls the look1 efficacy boundary Z≥2.75. The plotted region labelled Efficacy lies below zero and its corresponding outer boundary is at a negative ordinate. Harm lies above zero. Exact graphical ordinate coordinates are not independently printed; the sign is directly visible.

**Reported-versus-comparator:** Look 1, N = 956: printed table efficacy Z ≥ 2.75, versus a graphical Efficacy region below zero, with Harm above zero. The plot does not independently print exact boundary coordinates.

**Reasoning procedure:** Printed positive table inequality and negative labelled region are direct source observations. Interpreting the plotted magnitude as exactly2.75 is diagnostic only. Apply the logical comparison only if table and plot use the same signed statistic and contrast. Contrast/sign definitions, efficacy-oriented versus risk-oriented convention, magnitude transformation and harm/futility/efficacy priority are missing. No observed stopping Z path is supplied, so no actual trial decision is inferred.

**Calculation:** The table inequality Z ≥ +2.75 points toward positive Z. The graph labels the negative outer region Efficacy and the positive region Harm. Those orientations differ if the same signed statistic is intended. No exact negative boundary magnitude is claimed from the plot; this is a sign comparison without a P-tail reconstruction or graphical-digitization tolerance.

**Alternative source-grounded interpretations:** The table may use an efficacy-oriented Z and the figure may use a treatment-risk-oriented Z. That can reconcile the intended design, but neither the table nor figure declares this sign reversal. A nonnegative absolute statistic would require a distinct labelled convention because the figure is explicitly signed.

**Mechanical evidence recheck:** recorded_candidate. Current table and render reproduce the registered conditional direction/region comparison; sign-convention mapping remains the precise missing definition. Diagnostic: Z≥+2.75 points toward positive values while the graphical Efficacy region is negative. Exact plotted magnitude is not independently printed and is not asserted as a numeric source value. Classification P_P; all P_P; plan_material; no role/type code correction. Necessary missing inputs: Z contrast/sign definition in each display, efficacy-oriented versus risk-oriented convention, magnitude/absolute-value transformation and rule priority (including harm). Human question: At look1 N956, are table and plot the same signed Z; if different, what contrasts/sign transformation and efficacy/harm rule priority map the positive tabulated efficacy inequality to negative graphical efficacy tail? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (retain) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** Sign conventions can affect extraction of efficacy versus harm boundaries. No conclusion about the actual trial decision follows because no observed stopping Z path is supplied.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the stopping-boundary sign or region into a monitoring-plan summary. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Open the exact source pages above and compare the cited cells or statements. Recompute the stated arithmetic or logical diagnostic using the printed inputs, retaining the named conditions and display tolerance. Resolve this source-specific question: Are the table and figure meant to use the same signed Z? If different, what are the two contrast/sign definitions? Review the source generating table and plot rather than assume high-minus-low or low-minus-high. Record the human assessment in the five blank fields below.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C105 — Conditional efficacy-sign comparison at look 2

Pending Human Adjudication.

**Candidate statement:** Under a common signed-Z definition, the look-2 table inequality Z ≥ 2.432 has the opposite orientation to the negative graphical Efficacy region. Missing contrast, sign/magnitude mapping and rule priority prevent an unconditional monitoring-error inference.

**Category:** Statistical reporting inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol monitoring table look2 versus PLAN protocol boundary figure at enrollment1434; PLAN amendment and REPORT supplement repeated graphic corroborate

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R.

**Classification ambiguity:** Different benefit-oriented and treatment-risk-oriented Z can reconcile design. Corroborating REPORT graphic does not add P_R; both discrepancy locations remain PLAN.

**Exact source locations:** [joi190055supp1_prod_16092.pdf PDF p.22](../joi190055supp1_prod_16092.pdf#page=22), PLAN, statistical-analysis table, look2 efficacy; [joi190055supp1_prod_16092.pdf PDF p.23](../joi190055supp1_prod_16092.pdf#page=23), PLAN, stopping-boundary figure, Efficacy region at enrollment1434. [joi190055supp4_prod_16092.pdf PDF p.31](../joi190055supp4_prod_16092.pdf#page=31), REPORT, reproduces the negative-Z efficacy graphical orientation and corroborates the figure side; [joi190055supp2_prod_16092.pdf PDF p.3](../joi190055supp2_prod_16092.pdf#page=3), PLAN, amendment explicitly introduces the same table/figure but adds no signed contrast definition. The REPORT location corroborates rather than creates an additional discrepancy.

**Source evidence:** The table calls the look2 efficacy boundary Z≥2.432. The plotted region labelled Efficacy lies below zero and its corresponding outer boundary is at a negative ordinate. Harm lies above zero. Exact graphical ordinate coordinates are not independently printed; the sign is directly visible.

**Reported-versus-comparator:** Look 2, N = 1434: printed table efficacy Z ≥ 2.432, versus a graphical Efficacy region below zero, with Harm above zero. The plot does not independently print exact boundary coordinates.

**Reasoning procedure:** Printed positive table inequality and negative labelled region are direct source observations. Interpreting the plotted magnitude as exactly2.432 is diagnostic only. Apply the logical comparison only if table and plot use the same signed statistic and contrast. Contrast/sign definitions, efficacy-oriented versus risk-oriented convention, magnitude transformation and harm/futility/efficacy priority are missing. No observed stopping Z path is supplied, so no actual trial decision is inferred.

**Calculation:** The table inequality Z ≥ +2.432 points toward positive Z. The graph labels the negative outer region Efficacy and the positive region Harm. Those orientations differ if the same signed statistic is intended. No exact negative boundary magnitude is claimed from the plot; this is a sign comparison without a P-tail reconstruction or graphical-digitization tolerance.

**Alternative source-grounded interpretations:** The table may use an efficacy-oriented Z and the figure may use a treatment-risk-oriented Z. That can reconcile the intended design, but neither the table nor figure declares this sign reversal. A nonnegative absolute statistic would require a distinct labelled convention because the figure is explicitly signed.

**Mechanical evidence recheck:** recorded_candidate. Current table and render reproduce the registered conditional direction/region comparison; sign-convention mapping remains the precise missing definition. Diagnostic: Z≥+2.432 points toward positive values while the graphical Efficacy region is negative. Exact plotted magnitude is not independently printed and is not asserted as a numeric source value. Classification P_P; all P_P; plan_material; no role/type code correction. Necessary missing inputs: Z contrast/sign definition in each display, efficacy-oriented versus risk-oriented convention, magnitude/absolute-value transformation and rule priority (including harm). Human question: At look2 N1434, are table and plot the same signed Z; if different, what contrasts/sign transformation and efficacy/harm rule priority map the positive tabulated efficacy inequality to negative graphical efficacy tail? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (retain) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** Sign conventions can affect extraction of efficacy versus harm boundaries. No conclusion about the actual trial decision follows because no observed stopping Z path is supplied.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the stopping-boundary sign or region into a monitoring-plan summary. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Open the exact source pages above and compare the cited cells or statements. Recompute the stated arithmetic or logical diagnostic using the printed inputs, retaining the named conditions and display tolerance. Resolve this source-specific question: Are the table and figure meant to use the same signed Z? If different, what are the two contrast/sign definitions? Review the source generating table and plot rather than assume high-minus-low or low-minus-high. Record the human assessment in the five blank fields below.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C106 — Conditional efficacy-sign comparison at look 3

Pending Human Adjudication.

**Candidate statement:** Under a common signed-Z definition, the look-3 table inequality Z ≥ 2.012 has the opposite orientation to the negative graphical Efficacy region. Missing contrast, sign/magnitude mapping and rule priority prevent an unconditional monitoring-error inference.

**Category:** Statistical reporting inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol monitoring table look3 versus PLAN protocol boundary figure at enrollment1912; PLAN amendment and REPORT supplement repeated graphic corroborate

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R.

**Classification ambiguity:** Different benefit-oriented and treatment-risk-oriented Z can reconcile design. Corroborating REPORT graphic does not add P_R; both discrepancy locations remain PLAN.

**Exact source locations:** [joi190055supp1_prod_16092.pdf PDF p.22](../joi190055supp1_prod_16092.pdf#page=22), PLAN, statistical-analysis table, look3 efficacy; [joi190055supp1_prod_16092.pdf PDF p.23](../joi190055supp1_prod_16092.pdf#page=23), PLAN, stopping-boundary figure, Efficacy region at enrollment1912. [joi190055supp4_prod_16092.pdf PDF p.31](../joi190055supp4_prod_16092.pdf#page=31), REPORT, reproduces the negative-Z efficacy graphical orientation and corroborates the figure side; [joi190055supp2_prod_16092.pdf PDF p.3](../joi190055supp2_prod_16092.pdf#page=3), PLAN, amendment explicitly introduces the same table/figure but adds no signed contrast definition. The REPORT location corroborates rather than creates an additional discrepancy.

**Source evidence:** The table calls the look3 efficacy boundary Z≥2.012. The plotted region labelled Efficacy lies below zero and its corresponding outer boundary is at a negative ordinate. Harm lies above zero. Exact graphical ordinate coordinates are not independently printed; the sign is directly visible.

**Reported-versus-comparator:** Look 3, N = 1912: printed table efficacy Z ≥ 2.012, versus a graphical Efficacy region below zero, with Harm above zero. The plot does not independently print exact boundary coordinates.

**Reasoning procedure:** Printed positive table inequality and negative labelled region are direct source observations. Interpreting the plotted magnitude as exactly2.012 is diagnostic only. Apply the logical comparison only if table and plot use the same signed statistic and contrast. Contrast/sign definitions, efficacy-oriented versus risk-oriented convention, magnitude transformation and harm/futility/efficacy priority are missing. No observed stopping Z path is supplied, so no actual trial decision is inferred.

**Calculation:** The table inequality Z ≥ +2.012 points toward positive Z. The graph labels the negative outer region Efficacy and the positive region Harm. Those orientations differ if the same signed statistic is intended. No exact negative boundary magnitude is claimed from the plot; this is a sign comparison without a P-tail reconstruction or graphical-digitization tolerance.

**Alternative source-grounded interpretations:** The table may use an efficacy-oriented Z and the figure may use a treatment-risk-oriented Z. That can reconcile the intended design, but neither the table nor figure declares this sign reversal. A nonnegative absolute statistic would require a distinct labelled convention because the figure is explicitly signed.

**Mechanical evidence recheck:** recorded_candidate. Current table and render reproduce the registered conditional direction/region comparison; sign-convention mapping remains the precise missing definition. Diagnostic: Z≥+2.012 points toward positive values while the graphical Efficacy region is negative. Exact plotted magnitude is not independently printed and is not asserted as a numeric source value. Classification P_P; all P_P; plan_material; no role/type code correction. Necessary missing inputs: Z contrast/sign definition in each display, efficacy-oriented versus risk-oriented convention, magnitude/absolute-value transformation and rule priority (including harm). Human question: At look3 N1912, are table and plot the same signed Z; if different, what contrasts/sign transformation and efficacy/harm rule priority map the positive tabulated efficacy inequality to negative graphical efficacy tail? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (retain) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** Sign conventions can affect extraction of efficacy versus harm boundaries. No conclusion about the actual trial decision follows because no observed stopping Z path is supplied.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the stopping-boundary sign or region into a monitoring-plan summary. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Open the exact source pages above and compare the cited cells or statements. Recompute the stated arithmetic or logical diagnostic using the printed inputs, retaining the named conditions and display tolerance. Resolve this source-specific question: Are the table and figure meant to use the same signed Z? If different, what are the two contrast/sign definitions? Review the source generating table and plot rather than assume high-minus-low or low-minus-high. Record the human assessment in the five blank fields below.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

A confirmed reporting defect could be copied into a review's event counts, denominators, effect estimate, interval, outcome definition, scale or plan/report classification. Even a small preventable discrepancy can complicate evidence extraction, comparison or synthesis. Each card identifies a bounded possible extraction consequence and the source fact needed to settle it. A conditional calculation, an unsupported alignment premise, or a plan-display discrepancy should retain its qualifications when reused.

This report does not establish that any candidate propagated into a systematic review, meta-analysis, guideline or later publication. It does not claim that a paper-level conclusion changed or serious harm occurred. Human review can resolve a candidate by confirming the intended value or definition, documenting a coherent alternative, or seeking a source clarification.

## Limitations and Missing Definitions

All 100 supplied pages are mapped; limitations concern interpretation and missing definitions rather than an unresolved scientific-coverage gap. The [complete limitations record](review_1_6/limitations.md) documents absent participant-level data and analysis code, estimator/orientation/adjustment and variance/test definitions, row-specific denominators, modeled sensitivity estimands, display conventions, VAS origin, follow-up time origin and signed monitoring mappings.

Diagnostic arithmetic remains separate from author analysis. Some near-boundary displays reconcile under truncation or displayed-percentage subtraction. Header denominators are conditional where complete-case counts are absent; crude proportions are not automatically the comparator for modeled sensitivity estimates. A line length alone does not establish scale endpoints. Duration shorthand, time-origin conventions and signed-versus-magnitude monitoring notation require source clarification before stronger interpretation. Fifteen input-error records explicitly foreground their unsupported comparison premises. These bounds remain attached to the relevant evidence cards.

## Human Adjudication Checklist

For each stable ID, inspect the linked physical source pages and confirm the printed inputs, matching population, time, contrast and model. Reproduce the stated arithmetic or logical comparison using the applicable source rule. Check whether an alternative estimator, denominator, rounding convention, scale definition or time origin reconciles the observation. Resolve the named missing definition before accepting a conditional inference. Review document roles and substantive discrepancy relationships, then decide how the record should be handled.

Every card is Pending Human Adjudication. Fill the five blank human fields—validity, importance, action, initials and notes—after reviewing the evidence. The suggested review disposition is a mechanical pre-fill and does not replace that decision. Stable IDs preserve traceability even where the original input premise is unsupported.

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

### Local sources, tools and integrity

The [routing preflight](review_1_6/routing_preflight.md) records PASS for the fixed model/effort matrix, all nine named presets, coordinator inference and interactive CLI mode, with the explicitly authorized current-provider exception. The actual provider is OpenAI. All roles use `gpt-6.1-sol`, with medium effort for ordinary specialists and high effort for the coordinator, statistical passes, recheck and audit. The prescribed launch command is recorded; session metadata establishes CLI origin but does not retain the original argument list.

The [tooling record](review_1_6/tooling_record.md) reports direct PDF, rendering, OCR, Office and Pandoc tools available. Review used local CPU tools and source-matched reusable assets. No fallback environment was needed or created. Evidence links retain actual supplied filenames and physical PDF page anchors.

Integrity records: [source hashes before](review_1_6/source_hashes_before.sha256), [source hashes after](review_1_6/source_hashes_after.sha256), [reused-artifact hashes before](review_1_6/reused_artifact_hashes_before.sha256), and [reused-artifact hashes after](review_1_6/reused_artifact_hashes_after.sha256). The coordinator completes final hash comparisons after assembly and preserves every direct source and reused artifact.

The unchanged bundled validator has a hard-coded OpenRouter-provider requirement. Its [raw result](review_1_6/bundled_review_validation.json) is preserved; the [effective result](review_1_6/review_validation.json) applies only the exact provider exception authorized by the user. A raw provider error is not a raw PASS, and no scientific, coverage, model, effort, evidence or classification defect is waived. Final rendering, hash checks and validation are performed by the coordinator after Markdown assembly; these linked records supply their actual outcomes.

### Complete agent execution

The following table reproduces every actual agent in the [execution manifest](review_1_6/agent_execution_manifest.md). Mandatory specialists use fresh distinct runtime IDs; optional shards are included individually.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a12860-4d9e-7813-a9cd-5dbb5c6af8bd | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a12862-f7ad-7551-ab1e-66f2cc059ac9 | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a12865-83bc-7193-a84f-4b50723c87df | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a12865-a268-78b2-a07f-00e0c025a3f4 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_results_mapper | 01a12865-c12b-7a31-89c7-c49c23109703 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_results.md |
| statistics_pass_1_tables | 01a12869-c9f0-7231-9b70-dfd2c3c00bcf | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_tables.md |
| statistics_pass_1 | 01a1286a-7f32-78f0-97b4-3d1c28e5d86a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| statistics_pass_1_planplots | 01a1286a-aaa7-7290-810f-a2d4d4fd7c2d | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_planplots.md |
| numeric_consistency_reviewer | 01a1286a-d1a0-78a3-b596-ad02e44f539b | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_outcomes_reviewer | 01a1286a-f70e-7670-b0f7-a0db7e2ab04a | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_outcomes.md |
| cross_source_consistency_reviewer | 01a1286b-1eb0-7130-a796-b8279d3825a7 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1_physiology | 01a1286e-45eb-7ef2-8182-8840841190aa | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_physiology.md |
| numeric_support_tables | 01a1286e-c7cc-7cd0-a901-f092deade378 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_support_tables.md |
| numeric_planplots | 01a1286f-0335-7023-bd65-6ab8f678399d | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_planplots.md |
| candidate_merge_assistant | 01a12870-972e-7163-b211-c2c7bad04043 | gpt-6.1-sol | medium | FRESH_SPAWN | registration/merged_ledger_draft.md |
| evidence_rechecker | 01a12876-834d-72c3-aa7a-72e0443797df | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| evidence_rechecker_002 | 01a12876-ab30-7b53-8bfc-b7bc2088a3a9 | gpt-6.1-sol | high | FRESH_SPAWN | verification/parts/evidence_recheck_002.md |
| evidence_rechecker_003 | 01a12876-d8b5-7051-8ce1-2e81d211e001 | gpt-6.1-sol | high | FRESH_SPAWN | verification/parts/evidence_recheck_003.md |
| statistics_pass_2 | 01a1287e-9c64-7632-9439-3c68158cf2a8 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_tables | 01a1287e-ba43-7b21-b1b2-b2d070518e84 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_tables.md |
| statistics_pass_2_planplots | 01a1287e-d520-7c43-b095-ff4a2a023a37 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_planplots.md |
| statistics_pass_2_physiology | 01a1287e-ec48-7660-9bfb-6580f407aaac | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_physiology.md |
| quality_control_auditor | 01a12883-e976-7ed2-b7e6-12b82f985685 | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| quality_control_auditor_002 | 01a12884-0826-7953-abc6-b66e49bc9867 | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/evidence_quality_audit_002.md |
| quality_control_auditor_003 | 01a12884-27d8-78e0-9cf7-2f6ace5503dc | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/evidence_quality_audit_003.md |
| quality_control_auditor_004 | 01a12884-46a0-7540-a1ce-6ae64caf97fc | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/evidence_quality_audit_004.md |
| report_cards_001 | 01a12889-1b3f-7ea2-9cb1-75a3e13d3495 | gpt-6.1-sol | medium | FRESH_SPAWN | report_parts/cards_001.md |
| report_cards_002 | 01a12889-42cd-7782-b77c-75adabac90a5 | gpt-6.1-sol | medium | FRESH_SPAWN | report_parts/cards_002.md |
| report_cards_003 | 01a12889-621a-7b00-ab47-d0b441e27a72 | gpt-6.1-sol | medium | FRESH_SPAWN | report_parts/cards_003.md |
| report_cards_004 | 01a12889-8865-73b1-aa1b-031dd60ca7b4 | gpt-6.1-sol | medium | FRESH_SPAWN | report_parts/cards_004.md |
| report_generator | 01a1288a-1b2a-7372-a4ff-91c17b5e1e75 | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

### Reproducibility performance

The exact performance fields below are copied from [run_state.md](review_1_6/run_state.md). The coordinator finalizes their values immediately after complete Markdown assembly. Fresh-source units count missing usable preprocessing, whereas fresh scientific reconstruction covered all 100 pages. The target is a planning range and does not limit coverage or candidate inclusion. Local rendering and mechanical validation lie outside the review timing window; any later model-based repair requires updated finish and elapsed values.

- **Target basis:** Six readable PDFs contain 100 physical pages with source-matched reusable native/layout extraction for every page and 67 reusable renders, including all 12 supplementary result plots. There are no Office conversions or OCR gaps. The main article, protocol/amendment/SAP sources, and a dense results supplement require complete fresh relationship mapping, two distinct statistical passes, recheck, audit and report stages. Relative to the 102-page/81-fresh-page calibration, preprocessing is much lighter but inferential and cross-document coverage still requires several agent waves. A 30-45 minute range is selected for this package; it is a planning estimate, not a timeout.
- **Total source units:** 100
- **Fresh-source units:** 0
- **Target elapsed minutes:** 30-45
- **Started UTC:** 2026-10-11T00:35:12Z
- **Finished UTC:** 2026-10-11T01:20:54Z
- **Observed elapsed minutes:** 45.70
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Complete uncapped recheck, audit and report production for 106 candidates, two independent 373-relationship statistical passes, and source/classification wording repairs required additional specialist waves. The 45-minute upper estimate was exceeded by 0.70 minute; no coverage or candidate was omitted.
