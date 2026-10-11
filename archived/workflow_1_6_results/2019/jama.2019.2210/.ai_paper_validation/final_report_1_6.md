# Quantitative Reporting Quality-Control Review — AMATERASU Trial, Workflow 1.6

**Pending Human Adjudication — all 15 candidates.** This report records source-grounded consistency questions. Evidence states and suggested review dispositions are mechanical pre-fills for human review. The five human adjudication fields remain blank in every card.

# Executive Quality-Control Summary

Complete review of four supplied PDFs, covering all 96 physical pages, produced **15 stable quality-control candidates, C001–C015**. Every candidate received exact-source evidence recheck and independent classification audit. Discovery restarted from supplied sources and eligible extraction assets; previous candidate selections and reports did not define the scope.

The candidates concern three percentage/denominator comparisons, four numerical or arithmetic comparisons, six measure or label comparisons, one concrete age-boundary population definition, and one matched count across report documents. Six comparisons are within the main report, six are internal to the supplied plan bundle, and three compare the main report with its results supplement. No candidate currently has a substantive REPORT-versus-PLAN discrepancy relationship.

Several comparisons remain conditional on missing definitions. In particular, an intentional sum-to-100 percentage policy can reproduce the stage distribution in C005, usual postoperative scheduling can explain C006, and common analysis-population identity must be established for C013. Their retained IDs document the human questions; they do not imply that corrections are necessarily required.

Small preventable reporting defects can matter when counts, percentages, subgroup labels or endpoint definitions are copied into systematic reviews and other evidence products. This package review establishes neither actual propagation nor a change in the paper's conclusions or serious harm. Both complete statistical passes found no additional distinct candidate after the cross-lane ledger and direct-source recheck were considered.

# Package and Reused-Evidence Provenance

The package is `2019/jama.2019.2210`. Physical PDF page numbers are used throughout, independently of printed journal pagination. Content determines document role.

| Source ID | Supplied filename | Role | Content | Physical pages |
|---|---|---|---|---:|
| DOC-001 | jama_urashima_2019_oi_190023.pdf | REPORT | Published trial article, including Methods, results, tables, figures and references | 9 |
| DOC-002 | joi190023supp1_prod.pdf | PLAN | Initial and final protocol/SAP, operational appendices and amendments | 45 |
| DOC-003 | joi190023supp2_prod.pdf | REPORT | Non-plan eTables, eFigures and subgroup results | 41 |
| DOC-004 | joi190023supp3_prod.pdf | REPORT | Retrospective data-sharing statement | 1 |

The [source inventory](review_1_6/source_inventory.md) identifies all direct sources. The [evidence-asset inventory](review_1_6/evidence_asset_inventory.md) records 289 preserved existing assets: 99 native/layout page texts, 49 normalized page texts, four combined normalized texts, 90 rendered images, 19 OCR texts, 19 OCR metadata records, four document records, two native extraction manifests and three preprocessing/backend manifests. Fitness counts are 116 USABLE, 147 DUPLICATE, 25 PARTIAL and one STALE. Derivative overlap is counted once per source page.

Preferred reusable text covered main pp. 1–8 and results pp. 1–41; an alternate native text supplied main p. 9. Historical exclusions and absolute paths were assessed as metadata, not adopted as review scope. Main p. 9 actually contains article information and references and was fully mapped. All 45 PLAN pages and the one sharing page lacked usable reusable extraction and received fresh direct native/layout extraction.

Reusable OCR and text were locators and transcription aids. The supplied source page remained final authority for candidate facts. Original preferred derivative engine versions are unspecified; alternate native extraction identifies PyMuPDF without a version, and historical OCR metadata identifies a CPU engine. New operations use recorded direct Poppler 26.01.0 tools. The rechecker confirmed candidate values against direct layout extraction and source-matched visual pages; no new blanket OCR, Office conversion, fallback environment, external literature or GPU was needed.

# Scope, Complete Coverage, and Exclusions

| Source ID | Unit type | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---:|---:|---:|---:|---|
| DOC-001 | PDF_PAGE | 9 | 9 | 0 | 9 | COMPLETE |
| DOC-002 | PDF_PAGE | 45 | 0 | 45 | 45 | COMPLETE |
| DOC-003 | PDF_PAGE | 41 | 41 | 0 | 41 | COMPLETE |
| DOC-004 | PDF_PAGE | 1 | 0 | 1 | 1 | COMPLETE |
| Total | PDF_PAGE | 96 | 50 | 46 | 96 | COMPLETE |

For every direct source, reusable plus fresh-required units equals total units and mapped units equals total units. The [source-coverage ledger](review_1_6/source_coverage.md) and [coverage manifest](review_1_6/coverage_manifest.md) retain exact page and stage assignments. Bibliographic, administrative and blank-form pages were inspected and explicitly mapped when no applicable scientific numerical relationship existed. No scientific source-unit gap remains.

Review prioritized numerical arithmetic, denominators/proportions/totals, inferential reporting, matched numerical results, effect measures/labels/scales, and rate-versus-count distinctions. Population issues were considered only when they created a concrete numerical or interpretive inconsistency. A broad methodology, clinical, novelty, misconduct or raw-data audit was outside scope. No external publication was consulted to assess supplied historical claims.

Coherent display-zero P values alone are excluded by `DISPLAY_ZERO_NOT_CANDIDATE`. Neither complete statistical pass found such an annotation in its assigned sources, and no stable candidate is based on a displayed zero P value. Missing inferential definitions alone, equal rounded imputation results, crossed cumulative-hazard curves and ordinary rounded percentage totals did not generate candidates.

# Quantitative and Statistical Relationship Coverage

The [main evidence map](review_1_6/extraction/main_quantitative_evidence.md) reconstructs 134 main bundles, M001–M134. The [support map](review_1_6/extraction/support_quantitative_evidence.md) reconstructs 86 support bundles, B001–B086, and all 87 support page keys U001–U087. Full page parts preserve the [PLAN](review_1_6/extraction/support_plan_pages.md), [results](review_1_6/extraction/support_results_pages.md) and [sharing](review_1_6/extraction/support_data_sharing.md) content.

| Review lane | Complete registered scope | Durable evidence |
|---|---|---|
| Numeric consistency | 220 bundles, N001–N220; all components within each bundle | [Numeric inventory](review_1_6/relationships/numeric_relationship_inventory.md), [checker](review_1_6/checkers/numeric_consistency.md) |
| Cross-source consistency | 67 matched groups, X01–X67, across all four sources | [Cross-source checker](review_1_6/checkers/cross_source_consistency.md) |
| Statistical pass 1 | 148 relationships: S001–S082 and S101–S166 | [Relationship inventory](review_1_6/statistics/relationship_inventory.md), [pass 1](review_1_6/checkers/statistical_pass_1.md) |
| Statistical pass 2 | The same complete 148 relationships, after ledger and recheck | [Pass 2](review_1_6/checkers/statistical_pass_2.md) |
| Exact-source recheck | Every C001–C015 | [Individual rechecks](review_1_6/verification/evidence_recheck.md) |
| Independent quality/classification audit | Every candidate, coverage row and registered statistical relationship | [Quality audit](review_1_6/quality/evidence_quality_audit.md) |

Every statistical row explicitly records PASS_1_COMPLETE and PASS_2_COMPLETE. The unused S083–S100 namespace separates disjoint source parts; it is not missing coverage. Each pass comprises 82 primary and 66 subgroup relationships, including 35 subgroup effects and 31 interaction annotations with nonestimable placeholders retained. All four statistical contribution agents are fresh, distinct, high-effort specialists.

Checks addressed arithmetic and denominator identity; positive ordered intervals and point-estimate containment; treatment/outcome direction; matching population, time, contrast, model and precision; risk-array anchors; repeated values; label/scale identity; and cross-lane/recheck implications. Hazard ratios, subdistribution hazard ratios, cumulative hazards, cumulative incidence, survival estimates, at-risk counts and event proportions were distinguished. Five-year survival estimates were not substituted with complements of full-follow-up raw event proportions.

The sources supply general Cox, 95% interval and two-sided reporting conventions, but omit row-specific P-test choice, interval construction, covariance/variance and many interaction contrasts. Exact CI/P equivalence was therefore not imposed. Ordered intervals and qualitative null screens were checked without replacing the published analysis. Paired rank-test P values were not reconstructed from marginal medians, and equal rounded complete-case/imputed results were not treated as proof of copying. Both pass-2 contributions completed their entire scopes and emitted zero additional distinct candidates.

# Document-Role Classification Summary

Relationships are assigned by the content of the conflicting locations: P_R means REPORT versus PLAN; P_P means solely within PLAN material; S_C means between different REPORT documents; S_W means within one REPORT document. A source that only corroborates one side does not create an additional discrepancy relationship. Where multiple genuine relationships exist, precedence is P_R > P_P > S_C > S_W.

| Relationship type | Meaning | Candidate count |
|---|---|---:|
| P_R | REPORT-versus-PLAN discrepancy | 0 |
| P_P | PLAN-internal discrepancy | 6 |
| S_C | Between different REPORT documents | 3 |
| S_W | Within one REPORT document | 6 |
| Total | All stable IDs | 15 |

| Mechanically derived review domain | Candidate count |
|---|---:|
| protocol_report | 0 |
| plan_material | 6 |
| statistical_results | 5 |
| report_internal_inconsistency | 4 |
| Total | 15 |

| Evidence state | Candidate count |
|---|---:|
| recorded_candidate | 15 |
| not_reproduced | 0 |
| repaired_residual | 0 |
| record_input_error | 0 |
| Total | 15 |

All fifteen mechanically derive suggested review disposition `retain`; `exclude` and `discuss` each have zero. This is a pre-fill, not an adjudication. `recorded_candidate` includes a confirmed printed comparison that remains conditional on a named missing definition. It does not mean that a human reviewer has established an error.

Primary-category counts are numerical/arithmetic four; denominator/proportion/total three; measure/label/scale six; analysis-unit/population one; cross-document numerical one; statistical-reporting zero; and rate-versus-count zero, totaling fifteen. C014 is S_C: PLAN CDX2 material corroborates the main REPORT identity and does not add P_R.

# Candidate Index

| ID | Candidate | Category | Relationship type | Review domain | Evidence state |
|---|---|---|---|---|---|
| C001 | Baseline vitamin D 142 (58) | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C002 | ApaI GT 61 (40) | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C003 | HR direction footnote | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C004 | Figure 3C displayed risk rows | Numeric or arithmetic inconsistency | S_W | statistical_results | recorded_candidate |
| C005 | Pooled stage II 26% | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C006 | Timing window versus IQR | Numeric or arithmetic inconsistency | S_W | statistical_results | recorded_candidate |
| C007 | Initial daily dose | Numeric or arithmetic inconsistency | P_P | plan_material | recorded_candidate |
| C008 | RFS AND/OR definition | Measure, label, or scale inconsistency | P_P | plan_material | recorded_candidate |
| C009 | Omitted high-group inequality | Measure, label, or scale inconsistency | P_P | plan_material | recorded_candidate |
| C010 | Age-90 eligibility boundary | Analysis-unit or population inconsistency | P_P | plan_material | recorded_candidate |
| C011 | De novo cancer endpoint status | Measure, label, or scale inconsistency | P_P | plan_material | recorded_candidate |
| C012 | Initial target chronology | Numeric or arithmetic inconsistency | P_P | plan_material | recorded_candidate |
| C013 | DBP1 TG 57 versus 59 | Cross-document numeric inconsistency | S_C | report_internal_inconsistency | recorded_candidate |
| C014 | CDK2 versus CDX2/Cdx2 | Measure, label, or scale inconsistency | S_C | report_internal_inconsistency | recorded_candidate |
| C015 | Older-than-median age label | Measure, label, or scale inconsistency | S_C | report_internal_inconsistency | recorded_candidate |

# Candidate Evidence Cards

## C001 — Vitamin D middle-baseline count and percentage

**Pending Human Adjudication.**

**Candidate statement:** The vitamin D middle-baseline cell prints 142 (58), whereas the displayed measured-category counts imply 57.2581% under a common denominator and conventional nearest-integer rounding. The denominator and rounding policy require confirmation.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article baseline vitamin D cells vs REPORT main article subgroup totals and missingness

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All conflicting values are observed participant summaries in the same published REPORT. No conflicting PLAN or second REPORT is needed.

**Classification ambiguity:** None in document role or relationship. The common cell denominator and nearest-rounding rule are conditional definitions.

**Exact source locations:** [jama_urashima_2019_oi_190023.pdf — p. 5, Table 1 baseline 25(OH)D rows and rounding footnote](../jama_urashima_2019_oi_190023.pdf#page=5); [p. 4, pooled baseline strata](../jama_urashima_2019_oi_190023.pdf#page=4); [p. 6, missing baseline values](../jama_urashima_2019_oi_190023.pdf#page=6).

**Source evidence:** Vitamin D low 102 (41), middle 142 (58), high 4 (1.6); randomized arm n=251. Placebo counts are 71, 90 and 1. Pooled strata are 173, 232 and 5; seven baseline values are missing overall. The table permits percentage totals differing from 100 because of rounding.

**Reported-versus-comparator:** Printed middle percentage 58% versus 142/248 × 100 = 57.2581% for the complete displayed vitamin D categories. This concerns an individual cell, not a rounded column total.

**Reasoning procedure:** Sum mutually exclusive measured categories, reconcile overall measured totals with missingness, and compare the cell's derived proportion with its printed precision. Keep the measured denominator distinct from randomized n=251.

**Calculation:** 102+142+4=248; 71+90+1=162; 248+162=410=417−7. The difference from 58 is 0.7419 percentage point, exceeding a 0.5-point nearest-integer tolerance. Using 251 gives 56.5737%. Excluding the high category gives 142/244=58.1967%, but 102/244=41.8033% would conventionally round to 42 rather than the accompanying 41.

**Alternative source-grounded interpretations:** A cell-specific denominator, unconventional rounding policy or count/percentage transcription could explain the display. The generic rounding footnote does not establish the exact algorithm. The package does not select an explanation.

**Mechanical evidence recheck:** Direct layout and visual recheck confirmed that the cell prints 58, the counts and missingness match, and the conditional calculation reproduces. The exact denominator/rounding definition is unavailable. Provenance: NM-01; N022 and N051–N053; [individual recheck](review_1_6/verification/evidence_recheck.md).

**Quality-control relevance:** A baseline subgroup percentage and its apparent measured denominator need a reproducible reporting rule.

**Potential downstream evidence impact:** If confirmed, this cell could be copied into a baseline-composition evidence table with an inconsistent percentage or denominator. No actual copying or outcome impact is established.

**Human verification steps:** Inspect the three Table 1 cells and missingness locations; obtain the percentage denominator and rounding algorithm; determine whether all baseline categories use the same measured population. The unresolved question is which rule produced 142 (58).

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Placebo ApaI GT count and percentage

**Pending Human Adjudication.**

**Candidate statement:** ApaI GT placebo 61 (40) differs from conventional nearest-integer rounding of the displayed measured-genotype proportion, although uniform truncation can reproduce the full row.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article placebo ApaI genotype counts vs REPORT main article ApaI percentage

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** The counts, percentages and rounding footnote are within one REPORT table.

**Classification ambiguity:** None in roles or relationships. The denominator and rounding convention are unresolved.

**Exact source locations:** [jama_urashima_2019_oi_190023.pdf — p. 5, Table 1 ApaI placebo rows and footnote a](../jama_urashima_2019_oi_190023.pdf#page=5).

**Source evidence:** Placebo GG 69 (46), GT 61 (40), TT 20 (13), with randomized placebo header n=166. The footnote attributes possible percentage-total differences to rounding.

**Reported-versus-comparator:** Printed GT 40% versus 61/150 × 100 = 40.6667%, which conventionally rounds to 41%.

**Reasoning procedure:** Derive a measured denominator from the mutually exclusive genotype counts and test individual displayed precision. Do not treat the printed percentage total of 99% as an independent inconsistency.

**Calculation:** 69+61+20=150. The GT difference is 0.6667 percentage point, greater than 0.5. Other proportions are 46.0000% and 13.3333%. Using randomized n=166 gives 36.7470%, not 40%.

**Alternative source-grounded interpretations:** Uniform integer truncation produces exactly 46, 40 and 13, and the generic rounding footnote does not explicitly exclude it. Different cell denominators or a count/percentage transcription also remain possible.

**Mechanical evidence recheck:** Direct and visual inspection confirmed GT 61 (40) and the neighboring counts; the nearest-rounding comparison reproduced conditionally. Denominator and precise percentage policy remain missing. Provenance: NM-02; N064–N066; [recheck](review_1_6/verification/evidence_recheck.md).

**Quality-control relevance:** Percentage extraction should preserve the row's actual population and rounding convention.

**Potential downstream evidence impact:** If confirmed, an extractor could copy an inconsistent genotype percentage or assume an inappropriate denominator. The reported treatment effect is not shown to change.

**Human verification steps:** Confirm denominator 150 or identify the intended alternative; obtain the row's truncation/rounding policy; check which count or percentage definition accounts for GT 61 (40).

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Table 2 hazard-ratio direction footnote

**Pending Human Adjudication.**

**Candidate statement:** Table 2 links HR values greater than 1 with decreased outcome probability, while the article interprets the same adverse-outcome treatment contrast's HR 0.44 as lower relapse incidence with vitamin D.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 2 direction footnote vs REPORT main article relapse interpretation

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** The common direction footnote and explicit adverse-endpoint interpretation conflict within the published REPORT.

**Classification ambiguity:** None. A hypothetical reciprocal reference is an interpretive alternative, not a different document relationship.

**Exact source locations:** [jama_urashima_2019_oi_190023.pdf — p. 7, Table 2 footnote a and adverse-outcome rows](../jama_urashima_2019_oi_190023.pdf#page=7); [p. 6, competing-risk narrative](../jama_urashima_2019_oi_190023.pdf#page=6); [p. 3, treatment/model definitions](../jama_urashima_2019_oi_190023.pdf#page=3).

**Source evidence:** The footnote states that HR values greater than 1 indicate vitamin D associated with decreased probability of the outcome. Table outcomes are relapse, cancer-specific death and noncancer death. Middle-baseline relapse subdistribution HR is 0.44 (95% CI 0.21–0.89), P=.02; the narrative explicitly calls its cumulative relapse incidence lower with vitamin D than placebo. Total relapse HR is 0.75 (0.48–1.17), P=.21.

**Reported-versus-comparator:** Greater-than-1/decreased direction in the footnote versus below-1/lower adverse-outcome direction in the matched narrative.

**Reasoning procedure:** Retain the source's vitamin-D-versus-placebo contrast and adverse endpoint; compare the direction label independently of inference. An HR is not equated numerically with an event-probability ratio.

**Calculation:** 0.44<1 accompanies lower relapse incidence. For a hazard numerator/reference ratio, below 1 identifies the lower numerator hazard; the footnote assigns the decreased direction to the opposite inequality.

**Alternative source-grounded interpretations:** A reciprocal reference or favorable survival endpoint could explain the footnote in isolation, but neither is assigned to these adverse-event rows and the narrative specifies the treatment direction. A reversed inequality or carried-over footnote is a possible explanation only.

**Mechanical evidence recheck:** The source footnote, effect triplet, treatment definitions and lower-incidence interpretation were found and confirmed visually/directly. No estimate correction or exact P-test reconstruction follows from this direction comparison. Provenance: NM-03, XC01, ST1-A; N104; S003, S010, S011, S013–S015 and S017–S019; [recheck](review_1_6/verification/evidence_recheck.md).

**Quality-control relevance:** A common effect-direction label should agree with the treatment reference and endpoint interpretation.

**Potential downstream evidence impact:** If confirmed, a reader or evidence extractor could attach the opposite direction to the listed treatment effects. No reversed synthesis or changed conclusion is established.

**Human verification steps:** Confirm original model coding and treatment reference; determine the intended inequality in footnote a; align its wording with the explicit 0.44 lower-relapse interpretation without assuming that any numerical estimate is erroneous.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Figure 3C risk rows and caption absence claim

**Pending Human Adjudication.**

**Candidate statement:** Figure 3C displays two at-risk number sequences, while its caption states that panel C numbers at risk are not given because of weighting.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Figure 3C risk rows vs REPORT main article Figure 3 caption

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Numeric presence and the panel-specific absence statement are within the same REPORT figure/caption.

**Classification ambiguity:** None in roles. The intended raw-versus-effective weighted risk quantity is unspecified.

**Exact source locations:** [jama_urashima_2019_oi_190023.pdf — p. 7, Figure 3C and Figure 3 caption](../jama_urashima_2019_oi_190023.pdf#page=7).

**Source evidence:** Panel C is death among baseline 20–40 ng/mL participants, with HR 0.60 (0.28–1.30), P=.20. At years 0–6, placebo values are 90/88/70/51/34/22/11 and vitamin D values are 142/139/115/88/61/41/20. The caption says panel C numbers at risk are not given because of weighting.

**Reported-versus-comparator:** Fourteen labeled risk values are present versus the caption's statement of their absence.

**Reasoning procedure:** Establish panel identity from endpoint, baseline group and effect annotation; compare the specific caption with the two displayed sequences. Do not infer weighting status from integer formatting.

**Calculation:** Two rows × seven time points = 14 displayed values, rather than zero. No rounding tolerance is involved in presence-versus-absence.

**Alternative source-grounded interpretations:** The caption may refer to another panel/version or to weighted effective numbers while raw counts are shown. The source provides no explicit distinction and no original weighting specification.

**Mechanical evidence recheck:** Direct extraction and visual inspection confirmed the correct panel, all fourteen integers and the caption. Their raw/effective meaning remains unavailable. Provenance: NM-04, XC02, ST1-B; N114/N116 and S007; [recheck](review_1_6/verification/evidence_recheck.md).

**Quality-control relevance:** Figure captions should identify the quantities actually displayed so that risk populations and model descriptions can be extracted consistently.

**Potential downstream evidence impact:** If confirmed, a reader could omit displayed risk rows or incorrectly describe their weighting status. No erroneous HR or survival calculation is inferred.

**Human verification steps:** Inspect panel C and the caption together; obtain the figure's weighting and at-risk definitions; determine whether the caption refers to raw counts, effective counts, another panel or a prior figure version.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Pooled stage II narrative percentage

**Pending Human Adjudication.**

**Candidate statement:** Narrative stage II 26% differs from independent nearest-integer rounding of 111/417, but an intentional sum-to-100 largest-remainder allocation reproduces the complete printed 44%/26%/30% distribution.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article stage II narrative vs REPORT main article Table 1 stage counts

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** The stage summary and its count comparator are within one REPORT document.

**Classification ambiguity:** None in classification. The exact narrative percentage policy remains unresolved and can reconcile the printed distribution.

**Exact source locations:** [jama_urashima_2019_oi_190023.pdf — p. 4, Study Population stage percentages](../jama_urashima_2019_oi_190023.pdf#page=4); [p. 5, Table 1 stage counts](../jama_urashima_2019_oi_190023.pdf#page=5).

**Source evidence:** Narrative stages I/II/III are 44%/26%/30%. Table vitamin D/placebo counts are I 115/67, II 63/48, III 73/51; arm totals are 251/166.

**Reported-versus-comparator:** Stage II 26% versus 111/417 × 100 = 26.6187%, independently nearest-rounded to 27%. The whole printed percentage distribution is also considered.

**Reasoning procedure:** Pool matching stage counts, verify exhaustive total, test independent nearest rounding, then examine whether the complete distribution uses an adjusted sum-to-100 policy. Keep the reporting-rule question separate from disease-stage count accuracy.

**Calculation:** I=182, II=111, III=124; total 417. Exact proportions are 43.6451%, 26.6187%, 29.7362%. Independent rounding gives 44/27/30, sum 101. Printed 44/26/30 sums 100. Floors 43/26/29 sum 98; allocating two remaining percentage points to the largest fractional remainders, III (.7362) and I (.6451), yields exactly 44/26/30. The independent stage II difference is 0.6187 point, exceeding 0.5 only under that specified independent-rounding rule.

**Alternative source-grounded interpretations:** An intentional largest-remainder or other sum-to-100 adjustment fully explains the displayed distribution without changing a count. A different narrative population, stage definition, selective truncation or transcription could also be considered, but none is documented. The stage mix is not established to be erroneous.

**Mechanical evidence recheck:** Both locations and all six counts were visually/directly confirmed. The conditional nearest-rounding comparison reproduced; the audit independently demonstrated the largest-remainder explanation. Provenance: NM-05; N020/N045–N047; [recheck](review_1_6/verification/evidence_recheck.md).

**Quality-control relevance:** The policy that links stage counts to narrative percentages should be reproducible, especially when independent cell rounding and total-constrained rounding differ.

**Potential downstream evidence impact:** An extractor could copy stage proportions or apply an incompatible percentage convention. No altered stage-adjusted model, count or conclusion is inferred.

**Human verification steps:** Confirm the shared 417-person stage population; determine whether the narrative intentionally uses a sum-to-100 policy; document that policy before judging the 26% cell or suggesting any change.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Postoperative timing window and reported IQR

**Pending Human Adjudication.**

**Candidate statement:** The described 2–4-week postoperative initiation window does not bound the reported IQR of 13–44 days if it is a strict realized range; surrounding usual-schedule language offers an important alternative interpretation.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Methods postoperative timing vs REPORT main article Results timing IQR

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** The published Methods timing statement is REPORT content, compared with participant Results in that same REPORT.

**Classification ambiguity:** None in roles; whether the phrase is a realized range or intended/usual schedule is unresolved.

**Exact source locations:** [jama_urashima_2019_oi_190023.pdf — p. 2, Trial Design](../jama_urashima_2019_oi_190023.pdf#page=2); [p. 4, Study Population timing](../jama_urashima_2019_oi_190023.pdf#page=4).

**Source evidence:** Patients were randomized and started supplementation at their first outpatient visit between 2 and 4 weeks after operation. Preceding text says patients are usually discharged 5–14 days after operation and visit 1–2 weeks later if no major complications. Results give median 23.5 days, IQR 13–44, for randomization and medication initiation after operation.

**Reported-versus-comparator:** A conditional strict range of 14–28 days versus first/third quartiles 13 and 44 days for the described timing distribution.

**Reasoning procedure:** Convert weeks to days and apply the requirement that quartiles lie inside a distribution's realized bounds only if the Methods phrase actually specifies those bounds. Read the full scheduling context before interpreting the range.

**Calculation:** 2×7=14; 4×7=28. Q1 is one day below 14; Q3 is sixteen days above 28. Whole-day rounding does not bridge the upper difference. These calculations do not establish a strict scheduling requirement.

**Alternative source-grounded interpretations:** The explicit usually/no-major-complications context supports an expected schedule with variable recovery and clinical visits rather than a universal observed range. Different timing definitions or an editorial range summary also require clarification. Actual visit dates and the intended window definition are absent.

**Mechanical evidence recheck:** Both timing statements, shared operative anchor and usual-discharge/visit context were confirmed directly. The logical comparison reproduces only under a strict realized-range interpretation. Provenance: NM-06; N003/N019; [recheck](review_1_6/verification/evidence_recheck.md).

**Quality-control relevance:** A schedule description should be distinguishable from an empirical timing range when quantitative trial characteristics are summarized.

**Potential downstream evidence impact:** An extractor could describe all participants as initiating within 14–28 days without the qualification supported by the observed IQR. No eligibility violation, adherence problem, survival-origin shift or outcome effect is established.

**Human verification steps:** Confirm whether 2–4 weeks denotes a usual schedule or a strict realized range; match timing anchors; consult actual dates only if necessary to clarify the intended description. Preserve the source's usual context in any evidence summary.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Initial-plan daily dose versus capsule strength

**Pending Human Adjudication.**

**Candidate statement:** Within the supplied initial-plan material, 1200 IU/day and two 600-IU capsules conflict with a preparation strength of 1000 IU/capsule plus two capsules/day.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN initial protocol daily-dose specification vs PLAN initial protocol capsule strength

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both conflicting specifications are within the bound PLAN's initial version. The disclosed later final/report dose is context, not a conflicting REPORT comparator.

**Classification ambiguity:** Historical translation or retrospective consolidation could have retained later-strength wording in the initial version. This does not add P_R.

**Exact source locations:** [joi190023supp1_prod.pdf — p. 9, initial intervention](../joi190023supp1_prod.pdf#page=9); [p. 4, two capsules/day](../joi190023supp1_prod.pdf#page=4); [p. 12, preparation strength](../joi190023supp1_prod.pdf#page=12). Repeated1200 statements: [p. 3](../joi190023supp1_prod.pdf#page=3), [p. 7](../joi190023supp1_prod.pdf#page=7), [p. 8](../joi190023supp1_prod.pdf#page=8). Amendment context: [p. 45](../joi190023supp1_prod.pdf#page=45).

**Source evidence:** Initial intervention is 1200 IU/day as two 600-IU capsules. Initial preparation text supplies 1000 IU/capsule and another clause gives two per day. The amendment explicitly discloses 1200→2000 IU before trial initiation.

**Reported-versus-comparator:** Initial stated1200 versus strength/count-derived 2000 IU/day within the supplied initial version.

**Reasoning procedure:** Match the historical version and calculate daily dose from capsule number and capsule strength. Keep the disclosed initial-to-final change separate from this internal-version comparison.

**Calculation:** 2×600=1200; 2×1000=2000; difference 800 IU/day. These are exact integer specifications, not rounded observed exposures.

**Alternative source-grounded interpretations:** The initial version may have incorporated later preparation wording during translation or consolidation. The p.45 amendment explains the final/report 2000 dose; the package does not establish which wording belonged to the original archived initial version.

**Mechanical evidence recheck:** Dose, strength, capsule number, version locations and amendment were confirmed from the direct PLAN. The within-version arithmetic reproduced; actual dispensed exposure is not established. Provenance: NS-A, XC05; N136/N137; [recheck](review_1_6/verification/evidence_recheck.md).

**Quality-control relevance:** Historical intervention specifications should internally reconcile capsule strength, number and daily amount.

**Potential downstream evidence impact:** An extractor could record conflicting historical planned doses or incorrectly infer an undisclosed report/plan change. No actual dosing error or protocol violation is claimed.

**Human verification steps:** Compare the original archived initial version with the supplied translation; determine which capsule strength belongs to that date; retain the explicitly disclosed pretrial dose change when describing the final intervention.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — PLAN RFS event/censor conjunction

**Pending Human Adjudication.**

**Candidate statement:** PLAN RFS definitions require no relapse AND survival for the non-event state, whereas the supplied censor instructions use relapse-free OR alive.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN initial and final RFS endpoint definitions vs PLAN initial and final censor instructions

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All conflicting endpoint/censor clauses are PLAN content in initial and final versions of one bound bundle. Main REPORT endpoint language only corroborates one side.

**Classification ambiguity:** None in relationships. Editorial or translation use of OR may differ from implemented event coding.

**Exact source locations:** [joi190023supp1_prod.pdf — p. 9, initial primary outcome](../joi190023supp1_prod.pdf#page=9); [p. 25, final primary outcome](../joi190023supp1_prod.pdf#page=25); [p. 13, initial censor instruction](../joi190023supp1_prod.pdf#page=13); [p. 29, final censor instruction](../joi190023supp1_prod.pdf#page=29).

**Source evidence:** RFS is time to earliest relapse or all-cause death; the outcome definition's non-event censor state is no relapse AND alive. Reporting clauses instead describe relapse-free OR alive.

**Reported-versus-comparator:** AND versus OR for the same named non-event/censor definition, repeated in both supplied plan versions.

**Reasoning procedure:** Define R as relapse-free and A as alive. Compare conjunctions for each truth-value combination against the earliest-relapse-or-death event definition; separate printed instructions from actual implementation.

**Calculation:** R AND A differs from R OR A for (R=false,A=true) and (R=true,A=false). Literal OR includes an alive relapsed person and a dead relapse-free person in the stated non-event category. The rules agree when both values are equal.

**Alternative source-grounded interpretations:** OR may be informal editorial or translation wording with intended AND. The package supplies no event/censor records or implementation code to determine actual coding.

**Mechanical evidence recheck:** All four locations, exact conjunctions and earliest-event meaning were confirmed. The logical difference reproduces; implemented miscensoring is not inferred. Provenance: NS-C, XC06, ST1-C; N149/S049; [recheck](review_1_6/verification/evidence_recheck.md).

**Quality-control relevance:** Endpoint and censor labels determine what a quantitative survival outcome means and should use a consistent logical rule.

**Potential downstream evidence impact:** If confirmed, an evidence table could copy a different RFS non-event definition. No changed survival estimate or actual miscensoring is established.

**Human verification steps:** Confirm the intended conjunction in both archived versions; compare the actual event/censor specification if available; clarify the supplied wording without inferring implementation from the translation alone.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C009 — Final-plan high-baseline inequality

**Pending Human Adjudication.**

**Candidate statement:** The final PLAN design prints high(40 ng/mL) without an inequality, while its subgroup-analysis definition explicitly gives high >40 ng/mL.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN final high-baseline subgroup design label vs PLAN final subgroup-analysis boundary

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** The discrepant repeated threshold labels are both final PLAN content. REPORT high >40 corroborates the explicit analysis definition only.

**Classification ambiguity:** None in role or relationship. The meaning of the omitted inequality is unresolved.

**Exact source locations:** [joi190023supp1_prod.pdf — p. 23, final design baseline categories](../joi190023supp1_prod.pdf#page=23); [p. 31, final subgroup analysis](../joi190023supp1_prod.pdf#page=31).

**Source evidence:** Design low <20, middle ≥20 to ≤40, high(40 ng/mL), with no symbol before 40 in the high label. Analysis explicitly supplies high >40.

**Reported-versus-comparator:** Omitted high-category relation to 40 versus the explicit strict greater-than 40 definition.

**Reasoning procedure:** Inspect the source glyph rather than silently normalizing extraction, then compare repeated numerical category definitions. Treat any equality reading as hypothetical only.

**Calculation:** If high(40) were interpreted as high =40, exactly 40 would overlap inclusive middle and above 40 membership would remain unspecified. No equals sign is actually printed, and no implemented high =40 grouping is shown.

**Alternative source-grounded interpretations:** High(40) may be shorthand for above a40 threshold or an editing omission. The p.31 definition supplies an intended-looking boundary but does not explain the design label's missing inequality.

**Mechanical evidence recheck:** Direct text and visual image confirmed the missing glyph and explicit>40 comparator; the audit independently re-inspected the source-matched design image. The direct observation is the omitted definition, not participant reassignment. Provenance: NS-D, XC07, ST1-D; N153/S051; [recheck](review_1_6/verification/evidence_recheck.md).

**Quality-control relevance:** Repeated numerical stratum labels should be explicit enough to preserve disjoint threshold definitions.

**Potential downstream evidence impact:** An extractor could transcribe an ambiguous high-category cutoff. No changed subgroup count or treatment estimate is inferred.

**Human verification steps:** Confirm the intended high boundary and original design symbol; determine whether>40 was intended throughout; consult subgroup coding only if needed, without assuming equality was implemented.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C010 — PLAN age-90 eligibility boundary

**Pending Human Adjudication.**

**Candidate statement:** PLAN age 30–90 wording and a prospective registration form's30≤age<90 differ at exactly 90 if the prose range is inclusive.

**Category:** Analysis-unit or population inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN eligibility age range vs PLAN registration-form upper age boundary

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Eligibility clauses and the prospective registration form are PLAN by content. This secondary category qualifies through a concrete numerical population boundary, rather than a general design concern.

**Classification ambiguity:** The prose range's inclusivity and exact-versus-completed-age convention are unresolved. REPORT range/quartile wording is corroborative context only.

**Exact source locations:** [joi190023supp1_prod.pdf — p. 9, initial inclusion](../joi190023supp1_prod.pdf#page=9); [p. 24, final inclusion](../joi190023supp1_prod.pdf#page=24); [p. 38, registration form](../joi190023supp1_prod.pdf#page=38).

**Source evidence:** Initial and final text give age 30–90 years; the form gives30≤age<90. Main reported age range and the74–90 quartile endpoint do not establish any individual's age or inclusion.

**Reported-versus-comparator:** A conditionally inclusive upper endpoint90 versus a strictly exclusive upper endpoint90 in the form.

**Reasoning procedure:** Compare the membership of the exact boundary value under the two numerical definitions. Do not infer enrollment of a90-year-old from an aggregate quartile range.

**Calculation:** Under inclusive range semantics,90 belongs to[30,90] and does not belong to[30,90). This is one boundary-value membership difference; affected participant counts are unavailable.

**Alternative source-grounded interpretations:** Approximate prose, completed-age versus exact-age convention, or independently updated form wording may reconcile intent. The approved version and age policy are not supplied sufficiently to settle this.

**Mechanical evidence recheck:** All three locations and the strict upper glyph were confirmed directly/visually, with independent audit image confirmation. The membership comparison remains conditional on range semantics. Provenance: NS-E, XC08; N156; [recheck](review_1_6/verification/evidence_recheck.md).

**Quality-control relevance:** Numerical eligibility labels should communicate a consistent upper boundary for the described study population.

**Potential downstream evidence impact:** A review could copy inclusive or exclusive age 90 eligibility inconsistently. No participant is declared ineligible and no count or inference change is established.

**Human verification steps:** Confirm the approved numerical upper boundary, form version and age convention; determine whether the prose means inclusive 90 or an approximate range; examine individual ages only if an actual membership question remains.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C011 — Final-plan de novo cancer endpoint label

**Pending Human Adjudication.**

**Candidate statement:** The final PLAN synopsis describes de novo cancer as an adverse event rather than an outcome, while its outcome clause and amendment classify it as tertiary.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN final de novo cancer synopsis vs PLAN final tertiary-outcome clause and amendment

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All conflicting endpoint-status definitions are PLAN content. Main safety counts provide quantitative context, not a conflicting prospective label.

**Classification ambiguity:** Simultaneous safety and tertiary roles can coexist; the explicit not-an-outcome wording and amendment separation create the bounded question.

**Exact source locations:** [joi190023supp1_prod.pdf — p. 19, final synopsis](../joi190023supp1_prod.pdf#page=19); [p. 25, tertiary outcome](../joi190023supp1_prod.pdf#page=25); [p. 45, approved change](../joi190023supp1_prod.pdf#page=45). Quantitative context: [jama_urashima_2019_oi_190023.pdf — p. 8, Table 3](../jama_urashima_2019_oi_190023.pdf#page=8).

**Source evidence:** The final synopsis includes cancer arising after supplementation as an adverse event, not an outcome. The final outcome section defines de novo cancer in organs other than the primary as tertiary. The amendment separates it from secondary/safety and inserts it as tertiary. Main Table 3 counts are 15/8 for adherent-until-censoring participants and 16/9 for all randomized participants, vitamin D/placebo.

**Reported-versus-comparator:** Not-an-outcome status versus tertiary-outcome status for the matched de novo event/site/time definition in the final plan.

**Reasoning procedure:** Match event identity and final-version context before comparing labels; distinguish conflicting wording from the possible legitimate dual classification of an event.

**Calculation:** No numerical effect calculation is needed. The same named event is excluded from outcome status in one final clause and included as tertiary in another. The15/8 and 16/9 counts use different declared adherence populations and are not themselves this mismatch.

**Alternative source-grounded interpretations:** A stale synopsis, intended not-primary/secondary wording or dual safety/tertiary classification could explain the text. Compilation history and exact intended final label are missing.

**Mechanical evidence recheck:** All final clauses, amendment and context counts were confirmed. The retained label question does not establish missed events or erroneous counts. Provenance: NS-F, XC09; N151; [recheck](review_1_6/verification/evidence_recheck.md).

**Quality-control relevance:** Endpoint status determines how quantitatively reported events are described and categorized in an evidence table.

**Potential downstream evidence impact:** A reviewer could classify the same reported counts as a tertiary efficacy outcome or solely a safety event without knowing the intended final designation. No estimate or conclusion change is established.

**Human verification steps:** Confirm the final approved endpoint designation and synopsis compilation; clarify whether not-an-outcome meant not-primary/secondary or a broader exclusion; preserve the declared analysis populations for any counts extracted.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C012 — Initial n=400 versus amendment history of blank sample size

**Pending Human Adjudication.**

**Candidate statement:** The supplied initially dated PLAN synopsis contains target 400, while its amendment history says the sample size was blank at that initial date and fixed to 400 later.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN initial sample-size synopsis vs PLAN amendment history for that initial date

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Initial-version target and retrospective amendment chronology are both PLAN material in the bound bundle. Achieved trial enrollment is not a comparator.

**Classification ambiguity:** Blank may refer specifically to the calculation section, or the initial synopsis may have been retrospectively completed. Original version compilation is unresolved.

**Exact source locations:** [joi190023supp1_prod.pdf — p. 2, initial date2008.12.25](../joi190023supp1_prod.pdf#page=2); [p. 3, participant target](../joi190023supp1_prod.pdf#page=3); [p. 14, blank calculation headings](../joi190023supp1_prod.pdf#page=14); [p. 45, sample-size amendment history](../joi190023supp1_prod.pdf#page=45).

**Source evidence:** The initial synopsis gives total 400, vitamin D 240 and placebo 160. Amendment text says sample size was blank at 2008.12.25 and fixed 400 at 2009.10.8. Detailed sample-size/calculation headings on p.14 are blank.

**Reported-versus-comparator:** Explicit presence of target 400 in the supplied initial synopsis versus the history's assertion of absence at its date, conditional on what blank denotes.

**Reasoning procedure:** Align the initial date with the amendment account and distinguish a target number from a detailed calculation. Blank headings alone are not the candidate.

**Calculation:** 240+160=400. That numerical target is present in the initially dated synopsis; its absence is described retrospectively. Achieved 417 is a different population/time quantity and does not enter this comparison.

**Alternative source-grounded interpretations:** The amendment may mean only the calculation section was blank, or the initial synopsis may have been updated during translation/consolidation. The package lacks the archived dated version needed to resolve chronology.

**Mechanical evidence recheck:** Date, target, allocation, empty headings and amendment wording were confirmed from direct source. The presence/absence question remains conditional on section/version meaning. Provenance: NS-B, XC10; N142; [recheck](review_1_6/verification/evidence_recheck.md).

**Quality-control relevance:** A planned target and its change chronology should have a stable, traceable numerical description.

**Potential downstream evidence impact:** An extractor could record an inconsistent original target or sample-size change date. No actual power deficit, enrollment error or protocol violation is inferred.

**Human verification steps:** Inspect the archived 2008.12.25 version; establish whether blank refers to the target or only its calculation; identify retrospective synopsis updates before describing the change history.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C013 — DBP1 TG placebo count across REPORT documents

**Pending Human Adjudication.**

**Candidate statement:** Main Table 1 DBP1 TG placebo count 57 differs from the corresponding supplemental year-zero risk count 59; whether both displays use the same population must first be established.

**Category:** Cross-document numeric inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT main article DBP1 TG placebo baseline count vs REPORT results supplement year-zero risk count

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** The baseline table and non-plan results figure are different REPORT documents. This is a conditional matched-count comparison, not a PLAN discrepancy.

**Classification ambiguity:** Roles and relationship are clear; common genotype availability and model-population identity are unreported.

**Exact source locations:** [jama_urashima_2019_oi_190023.pdf — p. 5, Table 1 DBP1 TG](../jama_urashima_2019_oi_190023.pdf#page=5); [joi190023supp2_prod.pdf — p. 23, eFigure 3Q DBP1 TG](../joi190023supp2_prod.pdf#page=23).

**Source evidence:** Main vitamin D 87 (38), placebo 57 (39). Supplemental risks at 0/2/4/6 years: placebo 59/43/21/6; vitamin D 87/63/37/9. Effect HR 1.00 (0.44–2.24), P=.99; interaction P=.49. Neighboring placebo DBP1 TT82 and GG 9 agree with their matching panels.

**Reported-versus-comparator:** Main placebo TG57 versus supplemental year-zero TG59, with vitamin D 87 matching across displays.

**Reasoning procedure:** Match marker, genotype, treatment arm and baseline/year-zero anchor; compare counts only conditionally on a shared genotype/model population. Establish printed-count correctness and population definitions before asking about individual membership.

**Calculation:** 59−57=2. Placebo genotype sums are 82+57+9=148 in the main table and 82+59+9=150 in the supplement; the total difference restates the same TG-cell comparison and is not another stable candidate.

**Alternative source-grounded interpretations:** A table/plot count transcription may involve no actual additional participants. Different genotype availability or model analysis sets could also account for the pair. The package lacks a population crosswalk and explicit genotype-model fitting sets.

**Mechanical evidence recheck:** Direct visual/native confirmation established 57 and 59, matching vitamin D 87 and the panel identity. Common-population alignment remains conditional. No HR, CI, P or interaction error is inferred. Provenance: XC03, SG-B; N071/N197, S117/S152; [recheck](review_1_6/verification/evidence_recheck.md).

**Quality-control relevance:** A subgroup sample size attached to an effect should match its baseline definition or explicitly identify a different analysis set.

**Potential downstream evidence impact:** An extractor could attach 57 or59 to the same subgroup estimate without the intended population definition. No estimate correction, bias or conclusion change is established.

**Human verification steps:** First confirm the correct printed counts and whether both displays refer to the same DBP1 TG placebo population; identify any different genotype/model exclusions. Only if the difference reflects actual membership should a participant crosswalk identify the two records. The primary question is which count or analysis-set definition explains 57 versus 59.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C014 — CDK2 versus CDX2/Cdx2 effect labels

**Pending Human Adjudication.**

**Candidate statement:** Three supplemental effects are labeled CDK2 GG/GA/AA, while their six matching baseline population anchors are labeled Cdx2 in the main table and CDX2 rs11568820 in main Methods.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT main article CDX2/Cdx2 identity vs REPORT results supplement CDK2 subgroup labels; PLAN corroboration only

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** The independent conflicting identities are main REPORT CDX2/Cdx2 and results REPORT CDK2. PLAN methods/PCR corroborate the main identity; corroboration does not create a discrepancy relationship or invoke P_R precedence.

**Classification ambiguity:** Numeric-support NS-G previously framed a direct PLAN-versus-REPORT comparison as P_R. Exact-source recheck and audit supersede that framing with S_C because the PLAN confirms one side of the same REPORT mismatch. No substantive mixed discrepancy remains.

**Exact source locations:** [jama_urashima_2019_oi_190023.pdf — p. 3, CDX2 rs11568820 Methods](../jama_urashima_2019_oi_190023.pdf#page=3); [p. 5, Cdx2 GG/GA/AA](../jama_urashima_2019_oi_190023.pdf#page=5); [joi190023supp2_prod.pdf — p. 13, eFigure 3G](../joi190023supp2_prod.pdf#page=13), [p. 14, eFigure 3H](../joi190023supp2_prod.pdf#page=14), [p. 15, eFigure 3I](../joi190023supp2_prod.pdf#page=15). PLAN corroboration: [joi190023supp1_prod.pdf — p. 12](../joi190023supp1_prod.pdf#page=12), [p. 27](../joi190023supp1_prod.pdf#page=27), [p. 36](../joi190023supp1_prod.pdf#page=36).

**Source evidence:** Main vitamin D/placebo pairs are GG 89/49, GA 103/77, AA 38/24. Supplemental CDK2 labels have those identical year-zero pairs. GG HR 0.69 (0.34–1.38), P=.29, interaction .64; GA HR 0.72 (0.39–1.32), P=.28, interaction .63; AA HR 1.82 (0.48–6.88), P=.38, interaction .19. PLAN text prints CDX2/Cdx2.

**Reported-versus-comparator:** Repeated CDK2 effect labels versus CDX2/Cdx2 identity in the matched main genotype populations.

**Reasoning procedure:** Align all three genotype levels, both arms and year-zero anchors; then compare marker strings and the supplied rs identifier. Retain every distinct effect annotation while recording one repeated marker-identity rule.

**Calculation:** Six of six arm/genotype counts match:89=89,49=49,103=103,77=77,38=38,24=24. The discrepant letter is K versus X, not capitalization. No numerical HR recalculation follows from the identity comparison.

**Alternative source-grounded interpretations:** A repeated label transcription or a genuinely different marker with coincidentally identical populations could explain the figures. The package does not provide the original SNP-variable-to-figure mapping; external nomenclature was not consulted.

**Mechanical evidence recheck:** Direct glyph/image inspection confirmed CDK2 in all three panels and CDX2/Cdx2 in the main and corroborating PLAN locations, with all six matched counts. Classification was confirmed S_C, with the earlier P_R framing explicitly resolved. Provenance: NS-G, XC04, SG-A; N061–N063/N155/N187–N189/N220; S107–S109/S142–S144; [recheck](review_1_6/verification/evidence_recheck.md).

**Quality-control relevance:** Effect estimates should remain attached to a consistent marker identity across report documents.

**Potential downstream evidence impact:** If confirmed, a genetic subgroup review could attribute the three effects to a different marker. No effect estimate is shown to be numerically wrong and no downstream attribution error is known to have occurred.

**Human verification steps:** Obtain the original SNP-variable/rs-to-figure mapping; confirm which marker generated GG, GA and AA effects; inspect all three labels together and retain their separate effect estimates and interaction annotations.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C015 — Age>65 labeled older than median 66

**Pending Human Adjudication.**

**Candidate statement:** A supplemental age >65 subgroup is described as older than the median, while the main report gives overall median 66. Strictly older-than 66 and integer age >65 are different definitions if 66 is the relevant exact median.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT main article overall age median vs REPORT results supplement older-than-median subgroup label

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Overall median and supplemental subgroup wording appear in different REPORT documents. This is a median-relative label question rather than a PLAN eligibility comparison.

**Classification ambiguity:** The exact median precision, analysis-specific median and strict-versus-at-or-above meaning are unresolved; the fixed cutoff itself is explicitly printed.

**Exact source locations:** [joi190023supp2_prod.pdf — p. 31, eFigure 5B caption and risks](../joi190023supp2_prod.pdf#page=31); [jama_urashima_2019_oi_190023.pdf — p. 4, overall median age](../jama_urashima_2019_oi_190023.pdf#page=4); [p. 5, Table 1 age quartiles](../jama_urashima_2019_oi_190023.pdf#page=5). Context: [joi190023supp2_prod.pdf — p. 30, age ≤65 panel](../joi190023supp2_prod.pdf#page=30).

**Source evidence:** Caption older than median (>65 years), placebo 75/vitamin D 145 at year zero; HR 0.63 (0.37–1.05), P=.07, interaction .48. Main overall median age 66. Table age 66–73 and 74–90 counts are vitamin D 63/82 and placebo 48/27. The companion≤65 younger-than-median wording is contextual and need not itself conflict with median 66.

**Reported-versus-comparator:** Older-than-median description for>65 versus reported median 66; the cutoff's counts match the main table.

**Reasoning procedure:** Separate numerical cutoff and effect from its median-relative description. Compare strict inequalities only conditionally on the relevant exact median and integer-age convention; reconcile counts with the displayed age quartiles.

**Calculation:** Vitamin D 63+82=145; placebo 48+27=75, matching the figure. Integer age >65 includes 66, whereas strict age >66 excludes 66. The number of participants exactly 66 and any alternative effect estimate are not supplied.

**Alternative source-grounded interpretations:** At-or-above median wording may have been intended; an unrounded or analysis-specific median or approximate language could explain the phrase. Age precision and intended strictness remain missing. No HR error or incorrect fixed cutoff is established.

**Mechanical evidence recheck:** Caption, overall median, quartile counts and effect annotation were directly confirmed. The label comparison remains conditional on median precision/semantics. Provenance: XC11, SG-C; S124/S125/S158; [recheck](review_1_6/verification/evidence_recheck.md).

**Quality-control relevance:** An age subgroup's fixed threshold and its median-relative interpretation should communicate the same population definition.

**Potential downstream evidence impact:** A review could copy the effect as strictly above-median age when the printed cutoff includes the reported median under integer-age semantics. No participant reassignment, alternate HR or conclusion change is inferred.

**Human verification steps:** Confirm the relevant unrounded median and age convention; determine whether older means strictly above or at/above median; preserve the actual >65 cutoff and 145/75 population anchors when describing HR 0.63.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

# Downstream Evidence-Chain Considerations

If a human reviewer confirms a reporting defect, its bounded relevance lies in the particular value or definition that could be reused: baseline percentages, genotype sample sizes, effect direction, marker attribution, numerical subgroup boundaries, timing summaries, endpoint status or historical planned dose/target. Such details can enter extraction tables, systematic reviews, meta-analyses or guidelines even when a primary paper's conclusion remains unchanged.

This report does not establish that any candidate propagated, affected a synthesis or changed a clinical decision. Plan-internal historical discrepancies require version context. Conditional rounding and scheduling questions should be resolved using their source-grounded alternatives before a correction is considered. Counts, effect measures and analysis populations must be kept distinct during extraction.

# Limitations and Missing Definitions

The [complete limitations record](review_1_6/limitations.md) distinguishes interpretation limits from source-unit coverage, which is complete.

- No raw participant observations, event/censor records, original model code or unrounded analysis output is supplied. Printed comparisons cannot establish implemented miscensoring, actual boundary membership or changed estimates.
- Row-specific coefficient P tests, CI construction, variance/covariance, fitting/tie options and many interaction contrasts/statistics are absent. Exact CI/P identities were not assumed from convention.
- The article specifies 50 imputation repetitions, but pooled subgroup membership, covariance/variance and unrounded fits are unavailable. Equal rounded results do not establish copying. DBP1 genotype/model population alignment remains conditional.
- Paired ranks, ties, tested sample sizes and exact/asymptotic rank-test conventions are absent. Marginal medians and quartiles cannot reproduce signed-rank/Mann–Whitney P values or a median of individual change ratios.
- Exact annual boxplot statistics, whisker rules, annual denominators and numerical curve coordinates are not printed. All figures were mapped, but approximate coordinates were not promoted into exact arithmetic evidence.
- Percentage denominators/rounding algorithms, historical plan compilation, original weighting, intended-versus-realized schedule, age-boundary conventions, median precision and original SNP/figure mapping remain named candidate-specific questions.
- Historical derivative versions and absolute roots are incompletely documented. Current source hashes, physical pages, fresh extraction engines and exact-source confirmations anchor this run. Imperfect blank-form Unicode did not prevent reading its numerical definitions.
- The user authorized the current openai provider. This provider-only override leaves fixed models, reasoning efforts and fresh-agent requirements intact. The unchanged stock validator hardcodes openrouter; its result is retained separately, and only that exact provider-field error may be waived in the disclosed provider-aware result. Interactive CLI metadata is captured; exact shell launch flags are not independently preserved.

No source-unit omission remains hidden behind these limitations. Interpretation gaps do not authorize deleting a stable candidate or filling human adjudication fields.

# Human Adjudication Checklist

For every C001–C015, review the exact PDF locations and both compared statements; confirm common population, date, endpoint, contrast and numerical convention; distinguish source observation from inferred explanation; consider the card's alternatives; and resolve the named missing definition using an original record where necessary. Record the human decision in the five blank fields rather than treating `recorded_candidate` or `retain` as an adjudication.

Percentage questions require a documented reporting policy; historical PLAN questions require original version context; subgroup counts require matching analysis populations; direction and identity labels require model/variable reference confirmation. Candidate-specific evidence does not itself establish paper-level impact. All fifteen IDs remain traceable regardless of the eventual human decision.

# Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

## Source integrity and local tooling

Initial SHA-256 records cover [all four direct sources](review_1_6/source_hashes_before.sha256) and [all 289 reused assets](review_1_6/reused_artifact_hashes_before.sha256). The exact-source rechecker, statistical pass 2 and auditor independently confirmed the preserved source identities; the audit also checked all reused-asset and workflow-control hashes. The coordinator's [final integrity check](review_1_6/integrity_check.md) confirms identical [source after-hashes](review_1_6/source_hashes_after.sha256) and [reused-asset after-hashes](review_1_6/reused_artifact_hashes_after.sha256). No supplied source, reusable derivative or earlier audit artifact was modified by this review.

The [tooling record](review_1_6/tooling_record.md) documents Linux and available direct pdfinfo, pdftotext, pdftoppm, pdftocairo, Tesseract, LibreOffice and Pandoc. Recorded versions include Poppler 26.01.0, Tesseract 5.5.0 CPU and Pandoc 3.7.0.2. Fresh native/layout extraction closed all 46 uncovered pages, producing 92 page derivatives. Candidate recheck used targeted current-source rendering and source-matched existing images. Fallback environment NOT_NEEDED, packages None, capabilities None, removal NOT_CREATED. No global installation, GPU or external network source was used.

## Routing and validation provenance

The [routing preflight](review_1_6/routing_preflight.md) records PASS for the fixed role matrix, all nine named presets, successful coordinator inference and interactive CLI execution. Actual provider is openai under the explicit user instruction to use the current provider. The [authorized override record](review_1_6/authorized_provider_override.md) discloses that difference from the unchanged workflow's openrouter setting. The workflow-required launch command is recorded with the separate limitation that actual shell flags are not independently captured.

Final mechanical checks are recorded in [review_validation.json](review_1_6/review_validation.json), with the unchanged stock-validator result retained in [review_validation_stock.json](review_1_6/review_validation_stock.json). The coordinator finalizes timing and hashes, renders HTML, and executes validation after complete Markdown assembly; these linked records provide the completion status. The authorized wrapper may remove only the exact provider-field error when runtime provider, preflight and explicit authorization agree; every other validator error remains operative. An authorized provider-aware PASS must not be described as an unmodified stock-validator PASS.

## Agent execution

The [execution manifest](review_1_6/agent_execution_manifest.md) records every actual agent exactly once, including the current coordinator. All specialists are fresh spawns using gpt-6.1-sol; ordinary roles use medium effort and statistical/recheck/audit roles use high effort. Optional shards preserve their role contracts and do not substitute for mandatory stages.

| Stage | Runtime agent ID | Model | Reasoning effort | Start mode |
|---|---|---|---|---|
| coordinator | 01a1285e-f91a-72f0-948c-939d2c0abf5e | gpt-6.1-sol | high | CURRENT_SESSION |
| reuse_asset_curator | 01a12863-2648-7f93-810c-dab43d6aa39d | gpt-6.1-sol | medium | FRESH_SPAWN |
| main_quantitative_mapper | 01a12865-6081-79f1-b75e-7630d977e2a1 | gpt-6.1-sol | medium | FRESH_SPAWN |
| support_quantitative_mapper | 01a12865-82e1-73f0-9079-eba0a604c91d | gpt-6.1-sol | medium | FRESH_SPAWN |
| numeric_consistency_reviewer | 01a12868-d20d-7603-b09d-5a1375e78ae9 | gpt-6.1-sol | medium | FRESH_SPAWN |
| cross_source_consistency_reviewer | 01a12869-2b05-7b33-8375-ced02e4b8999 | gpt-6.1-sol | medium | FRESH_SPAWN |
| statistics_pass_1 | 01a12869-5568-7b03-ad14-728b9a27f354 | gpt-6.1-sol | high | FRESH_SPAWN |
| numeric_support_shard | 01a12869-0016-7623-8936-bbcb5dbab14a | gpt-6.1-sol | medium | FRESH_SPAWN |
| statistics_pass_1_subgroups_shard | 01a1286a-1a24-7f92-8ff0-5dbc424e0a2b | gpt-6.1-sol | high | FRESH_SPAWN |
| evidence_rechecker | 01a12871-ca61-7202-ac02-70750e754741 | gpt-6.1-sol | high | FRESH_SPAWN |
| statistics_pass_2 | 01a12879-149b-7932-b43b-ecb0574c8c9d | gpt-6.1-sol | high | FRESH_SPAWN |
| statistics_pass_2_subgroups_shard | 01a12879-3236-7643-9db8-9feeafeb4227 | gpt-6.1-sol | high | FRESH_SPAWN |
| quality_control_auditor | 01a1287e-9d22-7262-ab75-67bc0bbc91b9 | gpt-6.1-sol | high | FRESH_SPAWN |
| report_generator | 01a12884-74cc-7691-841a-20c995829672 | gpt-6.1-sol | medium | FRESH_SPAWN |

The two primary statistical IDs and both subgroup IDs are distinct. Each pass's canonical artifact preserves all disjoint parts. Report generation owns this complete Markdown; the manifest's mandated primary path `limitations.md` records the report-stage companion artifact. The coordinator renders standalone HTML after Markdown assembly.

## Reproducibility performance

- **Target basis:** Four native-text PDFs with 96 physical pages; 50 pages have reusable native/layout text, with overlapping normalized/OCR assets and 45 unique rendered source pages. Fresh mapping is required for 45 protocol/SAP pages spanning initial/final plans, appendices and amendments, plus one administrative data-sharing page. No Office conversion or blanket OCR is expected. The article, extensive subgroup figures, report/plan comparisons, two fresh statistical passes, evidence recheck, audit and report require sequential specialist waves after parallel mapping and checks. Reuse reduces preprocessing while plan-version and figure relationships retain substantive review burden.
- **Total source units:** 96
- **Fresh-source units:** 46
- **Target elapsed minutes:** 35-55
- **Started UTC:** 2026-10-11T00:35:42Z
- **Finished UTC:** 2026-10-11T01:20:56Z
- **Observed elapsed minutes:** 45.23
- **Target status:** MET_TARGET
- **Exceedance causes:** None

The coordinator fills these final performance values immediately after complete Markdown assembly and copies them identically from [run_state.md](review_1_6/run_state.md). Local HTML rendering and mechanical validation are outside the measured review duration; later model-based repairs advance the recorded finish time.
