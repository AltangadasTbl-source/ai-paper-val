# Independent inclusion screen — Workflow 1.6.2

Fresh initial inclusion specialist: `/root/inclusion_screen_initial`, gpt-6.1-sol / high. Exact scope: F-NUM-001 through F-NUM-005, F-XS-001 through F-XS-015, and F-ST1-001 through F-ST1-009: 29 findings. Decisions were made from the supplied sources and the complete QUALITY_CONTROL_SCOPE.md and inclusion-screen contract, independently of checker confidence. No earlier candidate or report conclusions were read. No candidate count was used as a target.

The 29 decisions produce 18 distinct included issues and 11 screened-out duplicate findings. Every included issue remains Pending Human Adjudication. The coordinator assigned stable candidate IDs in source order; included and duplicate rows now carry their linked candidate ID. The descriptive issue keys below preserve the independent screening handoff.

## Screening decisions

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-NUM-001 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C013 |
| F-NUM-002 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C012 |
| F-NUM-003 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C017 |
| F-NUM-004 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C016 |
| F-NUM-005 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C014 |
| F-XS-001 | cross_source_consistency_reviewer | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C012 |
| F-XS-002 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C018 |
| F-XS-003 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C002 |
| F-XS-004 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C003 |
| F-XS-005 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C008 |
| F-XS-006 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C009 |
| F-XS-007 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C010 |
| F-XS-008 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C007 |
| F-XS-009 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-XS-010 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C006 |
| F-XS-011 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C011 |
| F-XS-012 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C005 |
| F-XS-013 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C004 |
| F-XS-014 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C015 |
| F-XS-015 | cross_source_consistency_reviewer | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C014 |
| F-ST1-001 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C008 |
| F-ST1-002 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C009 |
| F-ST1-003 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C010 |
| F-ST1-004 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C007 |
| F-ST1-005 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C011 |
| F-ST1-006 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C006 |
| F-ST1-007 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C018 |
| F-ST1-008 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C001 |
| F-ST1-009 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C001 |

## One-sentence source-grounded justifications

- **F-NUM-001 — FIGURE2_CONTRIBUTORS:** Route A, category 2 qualifies because source Figure 2 B/D prints vitamin-D contributor rows under omega-3 labels, including 701/702 active baseline participants exceeding the 659 allocated omega-3 participants, and the matched contributor-count discrepancies survive display precision.
- **F-NUM-002 — FOREST_COUNT_ATTRIBUTION:** Route A, category 2 qualifies because source Figures 3/4 and eFigures 2/3 repeatedly pair opposite-arm allocation counts with treatment-specific outcome columns, with the vitamin-D overall 703 versus allocated placebo 609 yielding conservative relative gap 0.15189.
- **F-NUM-003 — PAIRED_URINE_ACCOUNTING:** Route A, category 3 qualifies because eTable 7 title/body N=944 implies 367 baseline-sample exclusions rather than footnote 320, with recomputed interval [366,368] versus [319.5,320.5] and relative gap 0.14219.
- **F-NUM-004 — SGLT2_PERCENTAGE:** Route A, category 3 qualifies because eTable 2 explicitly uses nonmissing responses and prints same-column year-5 313(74%) and 21(4%), which imply incompatible response-denominator intervals and a percentage gap 0.30622/4=0.07655.
- **F-NUM-005 — VITAMIN_D_UNIT_EQUIVALENCE:** Route A, category 2 qualifies because supplied plan pp.15/21 pair 2000 IU with 40 µg while p.21 also pairs 2000 IU with 50 µg, leaving conservative conversion-adjusted interval gap 8.97526/40=0.22438.
- **F-XS-001:** Duplicate of included F-NUM-002, FOREST_COUNT_ATTRIBUTION, adding eTable 11 and main abstract allocation corroboration to the same four-figure pattern without a separate count rule.
- **F-XS-002 — ACR_FAVOR_DIRECTION:** Route A, category 2 qualifies because both supplied ACR forest images label the ratio active/placebo but call ratios below 1 favorable to placebo and ratios above 1 favorable to active treatment, reversing the direction for less albuminuria progression.
- **F-XS-003 — AGE_ELIGIBILITY:** Route B qualifies because planned men≥60/women≥65 versus reported men≥50/women≥55 defines different target populations for the primary eGFR contrasts, exceeds display precision, and has no supplied eligibility amendment.
- **F-XS-004 — DIABETES_EXCLUSION:** Route B qualifies because the plan's diagnosis-before-30 plus initial-insulin exclusion and the report's diagnosis-before-30 plus insulin-duration>20-years exclusion are different Boolean population definitions for the primary type-2-diabetes treatment contrasts, with no supplied reconciliation.
- **F-XS-005 — PRIMARY_ANALYSIS_POPULATION:** Route A, category 5 qualifies because the latest plan requires at least one follow-up biosample for the primary analysis, whereas the report expressly analyzes every randomized participant regardless of follow-up and Figure 1 retains all 1312.
- **F-XS-006 — IMPUTATION_COUNT:** Route B qualifies because the latest plan explicitly specifies 10 imputations and the report 20 for the same primary eGFR missing-data/pooling step, a reproduced specification gap of 9 between half-unit intervals that changes the extracted analysis specification.
- **F-XS-007 — PRIMARY_COVARIATES:** Route A, category 5 qualifies because the report's adjusted primary eGFR model replaces the supplied primary Equation 2 with age, sex, baseline ACR and time interactions, while the plan reserves added baseline terms for conditional sensitivity analyses and does not report the original primary-model result.
- **F-XS-008 — ADHERENCE_ANALYSIS_SET:** Route B qualifies because planned continuous adherence≥80% differs from reported use≥2/3 on≥4 of 6 questionnaires for primary-outcome sensitivity results, with conservative threshold relative gap 0.16042 and a distinct continuity rule.
- **F-XS-009 — DOCUMENTED_OUTCOME_REVISION:** Route A, category 5 qualifies because original primary ACR/secondary eGFR status and the original composite components change in the supplied amendment and report, with the explicit 2016 disclosure retained as the supported prospective-amendment interpretation.
- **F-XS-010 — CATEGORICAL_ACR_PRESPECIFICATION:** Route A, category 5 qualifies because the report calls standalone time to ACR doubling with final ACR≥30 prespecified, whereas the supplied latest plan specifies continuous ACR and the older plan specifies ACR doubling only inside a different composite.
- **F-XS-011 — BIOAVAILABLE_SUBGROUP:** Route A, category 5 qualifies because the supplied latest plan separately prespecifies total and bioavailable 25(OH)D subgroup analyses of the primary outcome, while the full report inventory and source Figure 3 contain only the total-concentration subgroup result.
- **F-XS-012 — EGFR_ESTIMATOR_IDENTITY:** Route B qualifies because the original plan explicitly gives the 177.6-based equation linked to its 2008 reference 145 while the report identifies the CKD-EPI equation linked to its 2012 reference 19, changing the estimator identity for the primary eGFR endpoint without a supplied replacement specification.
- **F-XS-013 — RANDOMIZATION_STRATA:** Route B qualifies narrowly as a planned-versus-reported statistical design specification because plan age-only stratification and report age/sex/race stratification describe different randomized designs attached to the primary contrasts, without a supplied revision or any inferred omission of analysis adjustment.
- **F-XS-014 — INTERACTION_TIME_SPECIFICATION:** Route B qualifies because source plan Equation 1 contains no common time effect and fixes the double-placebo mean over time, whereas Equation 2 permits common change, leaving the actual planned interaction model behind the reported P=.42 and its marginal-comparison decision unclear.
- **F-XS-015:** Duplicate of included F-NUM-005, VITAMIN_D_UNIT_EQUIVALENCE, with main p.2 corroborating only the IU dose and adding no conflicting report microgram value.
- **F-ST1-001:** Duplicate of included F-XS-005, PRIMARY_ANALYSIS_POPULATION, retaining its blood-only and unsupplied blood/urine-union alternatives rather than asserting a union denominator.
- **F-ST1-002:** Duplicate of included F-XS-006, IMPUTATION_COUNT, with the same supplied 10-versus-20 primary imputation setting.
- **F-ST1-003:** Duplicate of included F-XS-007, PRIMARY_COVARIATES, with the same primary fixed-effect term and sensitivity-role comparison.
- **F-ST1-004:** Duplicate of included F-XS-008, ADHERENCE_ANALYSIS_SET, with the same consumption threshold and questionnaire-continuity population definition.
- **F-ST1-005:** Duplicate of included F-XS-011, BIOAVAILABLE_SUBGROUP, with the same unreported prespecified primary-outcome biomarker subgroup.
- **F-ST1-006:** Duplicate of included F-XS-010, CATEGORICAL_ACR_PRESPECIFICATION, with the same standalone time-to-doubling versus continuous/composite-component distinction.
- **F-ST1-007:** Duplicate of included F-XS-002, ACR_FAVOR_DIRECTION, preserving both image axes and every plotted row without combining the independent count-column pattern.
- **F-ST1-008:** Duplicate of included F-XS-009, DOCUMENTED_OUTCOME_REVISION, preserving the hierarchy/time component of the same explicitly documented endpoint-amendment pattern.
- **F-ST1-009:** Duplicate of included F-XS-009, DOCUMENTED_OUTCOME_REVISION, preserving the composite component/threshold part of that same documented endpoint-amendment pattern.

## Included-issue handoff

The keys are linkage labels, not candidate IDs. Findings recorded as duplicates retain their provenance and every location in the indicated issue; the coordinator should put the eventual candidate ID into each corresponding duplicate row. Proposed domains and relationships below follow content roles; corroborating locations do not create additional relationships. No final evidence state is assigned at this screening stage.

### FIGURE2_CONTRIBUTORS

- **Finding IDs:** F-NUM-001. **Route:** A2. **Focus:** A. **Proposed domain:** statistical_results. **Relationships:** S_C, S_W; primary S_C. **Compared roles:** REPORT main and REPORT results supplement.
- **Complete locations:** main [p.7 Figure 2 A–D and contributor caption](../../../jama_de_boer_2019_oi_190122.pdf#page=7), [p.8 Table 2 omega-3 rows](../../../jama_de_boer_2019_oi_190122.pdf#page=8), supplement [p.11 eTable 6 omega-3 rows](../../../joi190122supp2_prod.pdf#page=11); main [p.1 allocation](../../../jama_de_boer_2019_oi_190122.pdf#page=1) corroborates the cap.
- **Retained scope/calculation:** all B/D placebo/active contributor cells at baseline, year 2 and year 5, and A/C as the source of the repeated rows; eGFR B active 701/531/496 and placebo 607/459/438 compare with 657/499/472 and 651/491/462, while ACR D active 702/529/505 and placebo 609/463/440 compare with 658/502/478 and 653/490/467; eGFR year-5 differences alone are below 0.05 and retained only as occurrences of the established pattern, while baseline/year-2 eGFR and all ACR differences survive the rule.
- **Human question/alternative:** which source-defined participant populations accompany the plotted omega-3 distributions; an unstated graph population cannot explain baseline active counts exceeding randomized allocation, and graph values themselves are not recomputed.

### FOREST_COUNT_ATTRIBUTION

- **Finding IDs:** F-NUM-002; duplicate F-XS-001. **Route:** A2. **Focus:** A. **Proposed domain:** statistical_results. **Relationships:** S_C, S_W; primary S_C. **Compared roles:** REPORT main and REPORT results supplement.
- **Complete locations:** main [p.8 Figure 3 and Table 2](../../../jama_de_boer_2019_oi_190122.pdf#page=8), [p.9 Figure 4](../../../jama_de_boer_2019_oi_190122.pdf#page=9), supplement [p.18 eFigure 2](../../../joi190122supp2_prod.pdf#page=18), [p.19 eFigure 3](../../../joi190122supp2_prod.pdf#page=19), main [p.1 allocation](../../../jama_de_boer_2019_oi_190122.pdf#page=1), [p.5 Table 1 allocations/race/25(OH)D](../../../jama_de_boer_2019_oi_190122.pdf#page=5), [p.6 Figure 1](../../../jama_de_boer_2019_oi_190122.pdf#page=6), supplement [p.11 eTable 6 overall outcome changes](../../../joi190122supp2_prod.pdf#page=11), [p.16 eTable 11 marginal allocations](../../../joi190122supp2_prod.pdf#page=16).
- **Retained scope/calculation:** all count columns in all four forest figures, with direct comparator support for overall D 703/609, white 451/406, black 148/130, D categories 110/85, 230/203, 332/297 and factorial strata; the Figure 4/eFigure 3 D-placebo stratum 289/320 conflicts with assigned 320/289 (gap 30/320=0.09375 and 30/289=0.10381), and the D-active stratum 370/333 conflicts with 333/370 (gap 36/333=0.10811 and 36/370=0.09730); the omega overall 659/653 difference alone is subthreshold, and unsupported external replacements for other subgroup counts are not asserted.
- **Human question/alternative:** determine which counts accompany each treatment-specific outcome column; overall outcome changes match the report's current treatment labels, so exchanging complete outcome columns is not established as a resolution.

### PAIRED_URINE_ACCOUNTING

- **Finding IDs:** F-NUM-003. **Route:** A3. **Focus:** A. **Proposed domain:** statistical_results. **Relationships:** S_W. **Compared roles:** REPORT within results supplement.
- **Complete location:** supplement [p.12 eTable 7 title, baseline/year-5 rows and full footnote](../../../joi190122supp2_prod.pdf#page=12).
- **Retained scope/calculation:** title N=944 and 504+440=477+467=944 versus footnote baseline 1311, included 991, excluded 320 and no-baseline 1; the exclusion comparison [366,368] versus [319.5,320.5] qualifies (gap 45.5/320=0.14219), whereas 991-versus-944 alone is below 0.05 and does not supply a separate basis.
- **Human question/alternative:** what inclusion/exclusion filter reconciles the table body with the expressly included footnote population; an additional 47-person filter is not supplied.

### SGLT2_PERCENTAGE

- **Finding IDs:** F-NUM-004. **Route:** A3. **Focus:** A. **Proposed domain:** statistical_results. **Relationships:** S_W. **Compared roles:** REPORT within results supplement.
- **Complete location:** supplement [p.7 eTable 2 year-5 vitamin-D-placebo biguanide/SGLT2 rows, all SGLT2 cells and response-denominator footnote](../../../joi190122supp2_prod.pdf#page=7).
- **Retained scope/calculation:** source footnote gives response N=916 at year 5 and no medication-specific exception; 313(74%) implies D-placebo response interval [419.4631,426.5306], yielding 21-count percentage interval [4.80622,5.12560] versus printed [3.5,4.5], gap 0.30622/4=0.07655; the same-cell denominator interval required by 21(4%) is [455.5556,614.2857], disjoint from the biguanide-derived interval; 25(6%) active does not independently exceed the threshold under full half-unit allowances.
- **Human question/alternative:** what exact respondent denominator produced 21(4%), and was a medication-specific response set used despite the common table footnote; the inference of a shared response denominator is supported by that footnote and other same-column rows, rather than imposed from randomized N.

### VITAMIN_D_UNIT_EQUIVALENCE

- **Finding IDs:** F-NUM-005; duplicate F-XS-015. **Route:** A2. **Focus:** D. **Proposed domain:** plan_material. **Relationships:** P_P. **Compared roles:** PLAN within one protocol bundle.
- **Complete locations:** plan [p.15 §V.e.1 study pill](../../../joi190122supp1_prod.pdf#page=15), [p.21 §VII.a dose and paired-unit upper-limit statements](../../../joi190122supp1_prod.pdf#page=21); main [p.2 2000-IU intervention](../../../jama_de_boer_2019_oi_190122.pdf#page=2) corroborates only IU and supplies no conflicting report microgram dose.
- **Retained scope/calculation:** 2000 IU(40 µg) versus 50 µg or 2000 IU; comparator conversion interval [49.47526,50.52526] versus [39.5,40.5] gives 8.97526/40=0.22438; no external conversion or separate safety critique is used.
- **Human question/alternative:** which microgram equivalent belongs to the planned IU dose, and which printed equivalence should govern extraction; the source alone does not select one final equivalent.

### ACR_FAVOR_DIRECTION

- **Finding IDs:** F-XS-002; duplicate F-ST1-007. **Route:** A2. **Focus:** B. **Proposed domain:** statistical_results. **Relationships:** S_W. **Compared roles:** REPORT within results supplement.
- **Complete locations:** supplement [p.18 eFigure 2 ratio header, ticks and both favor arrows](../../../joi190122supp2_prod.pdf#page=18), [p.19 eFigure 3 corresponding header/ticks/arrows](../../../joi190122supp2_prod.pdf#page=19), [p.11 eTable 6 ratio/change definition](../../../joi190122supp2_prod.pdf#page=11); main [p.3 ACR progression definition](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [p.4 ACR increase narrative](../../../jama_de_boer_2019_oi_190122.pdf#page=4), plan [p.11 slower-progression hypotheses](../../../joi190122supp1_prod.pdf#page=11) and [p.17 ACR progression definition](../../../joi190122supp1_prod.pdf#page=17) corroborate the quantity and benefit direction only.
- **Retained scope/calculation:** both shared axes and all plotted overall/subgroup rows; active/placebo follow-up/baseline ACR-change ratio below 1 means less increase with active, opposite the printed left-arrow placebo label; this compares a printed ratio definition with its direction, not adjusted effects with crude ratios.
- **Human question/alternative:** do the arrows or the active/placebo reference text define the intended direction; neither production explanation is assigned as a final correction.

### AGE_ELIGIBILITY

- **Finding IDs:** F-XS-003. **Route:** B. **Focus:** D. **Proposed domain:** protocol_report. **Relationships:** P_R. **Compared roles:** PLAN versus REPORT.
- **Complete locations:** plan [p.4 abstract](../../../joi190122supp1_prod.pdf#page=4), [p.11 aims/population](../../../joi190122supp1_prod.pdf#page=11), [p.12 Table 1/population](../../../joi190122supp1_prod.pdf#page=12), [p.31 amendment dates](../../../joi190122supp1_prod.pdf#page=31), [p.32 amended analysis](../../../joi190122supp1_prod.pdf#page=32), [p.33 continuation](../../../joi190122supp1_prod.pdf#page=33); main [p.2 Study Population](../../../jama_de_boer_2019_oi_190122.pdf#page=2).
- **Retained scope/calculation:** men≥60/women≥65 versus men≥50/women≥55, with conservative half-unit gaps 9/60=0.150 and 9/65=0.13846; this concerns which target population the primary eGFR contrasts represent, without estimating how many participants change eligibility.
- **Human question/alternative:** which eligibility amendment connects the explicit age limits; a later parent-trial revision is possible but absent from this package.

### DIABETES_EXCLUSION

- **Finding IDs:** F-XS-004. **Route:** B. **Focus:** D. **Proposed domain:** protocol_report. **Relationships:** P_R. **Compared roles:** PLAN versus REPORT.
- **Complete locations:** plan [p.12 eligibility Table 1 and narrative](../../../joi190122supp1_prod.pdf#page=12), [p.14 enrollment algorithm](../../../joi190122supp1_prod.pdf#page=14); main [p.2 Study Population](../../../jama_de_boer_2019_oi_190122.pdf#page=2).
- **Retained scope/comparison:** both use diagnosis before age 30, but initial insulin treatment and insulin duration>20 years are logically different additional criteria defining the primary-analysis cohort; no participant-level membership difference is calculated.
- **Human question/alternative:** which type-1 exclusion proxy was implemented and where was its revision specified; a pragmatic later proxy is possible but not supplied.

### PRIMARY_ANALYSIS_POPULATION

- **Finding IDs:** F-XS-005; duplicate F-ST1-001. **Route:** A5. **Focus:** D. **Proposed domain:** protocol_report. **Relationships:** P_R. **Compared roles:** PLAN versus REPORT.
- **Complete locations:** plan [p.32 §15c](../../../joi190122supp1_prod.pdf#page=32); main [p.3 Data Analysis](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [p.4 retention](../../../jama_de_boer_2019_oi_190122.pdf#page=4), [p.6 Figure 1 primary-analysis boxes](../../../jama_de_boer_2019_oi_190122.pdf#page=6), [p.8 Table 2 footnotes](../../../jama_de_boer_2019_oi_190122.pdf#page=8).
- **Retained scope/comparison:** planned inclusion conditional on≥1 follow-up biosample versus reported unconditional all-randomized analysis N=1312 for both primary contrasts; observed blood 1090 and urine 1091 corroborate follow-up loss, but their unsupplied union is not asserted to be either count.
- **Human question/alternative:** which final analysis plan removed the follow-up condition; an unsupplied all-randomized amendment or blood/urine-union definition remains possible.

### IMPUTATION_COUNT

- **Finding IDs:** F-XS-006; duplicate F-ST1-002. **Route:** B. **Focus:** D. **Proposed domain:** protocol_report. **Relationships:** P_R. **Compared roles:** PLAN versus REPORT.
- **Complete locations:** plan [p.32 §15c](../../../joi190122supp1_prod.pdf#page=32); main [p.3 Data Analysis](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [p.8 Table 2 footnotes](../../../jama_de_boer_2019_oi_190122.pdf#page=8).
- **Retained scope/calculation:** primary eGFR Rubin pooling uses 10 datasets in plan and M=20 in report; intervals [9.5,10.5]/[19.5,20.5] give gap 9, relative to plan 0.90 and relative to report 0.45; the specific extracted primary missing-data specification changes, with no claim of a quantified SE or conclusion effect.
- **Human question/alternative:** was 20 a subsequent implementation amendment, and which prospective pooling specification accompanies the primary results.

### PRIMARY_COVARIATES

- **Finding IDs:** F-XS-007; duplicate F-ST1-003. **Route:** A5, also B. **Focus:** D. **Proposed domain:** protocol_report. **Relationships:** P_R. **Compared roles:** PLAN versus REPORT.
- **Complete locations:** plan [p.32 §15e Equation 2 and sensitivity clause](../../../joi190122supp1_prod.pdf#page=32), [p.33 continuation](../../../joi190122supp1_prod.pdf#page=33); main [p.3 Data Analysis](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [p.8 Table 2 footnote a](../../../jama_de_boer_2019_oi_190122.pdf#page=8); supplement [p.9 eTable 4](../../../joi190122supp2_prod.pdf#page=9), [p.10 eTable 5](../../../joi190122supp2_prod.pdf#page=10).
- **Retained scope/comparison:** plan primary treatment/time/treatment×time/random-intercept terms versus report primary added age/sex/baseline-ACR and time interactions; conditional imbalance sensitivity terms do not identify those added terms as the supplied primary model, and reported sensitivity tables also use adjusted models rather than providing its unadjusted primary counterpart.
- **Human question/alternative:** which final plan makes these fixed covariates primary; the recorded conditional sensitivity clause or a later amendment may explain the implementation, without a preferred model proposed.

### ADHERENCE_ANALYSIS_SET

- **Finding IDs:** F-XS-008; duplicate F-ST1-004. **Route:** B. **Focus:** D. **Proposed domain:** protocol_report. **Relationships:** P_R. **Compared roles:** PLAN versus REPORT.
- **Complete locations:** plan [p.19 §VI.g](../../../joi190122supp1_prod.pdf#page=19), [p.33 §15g](../../../joi190122supp1_prod.pdf#page=33); main [p.3 Covariates/Data Analysis](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [p.4 sensitivity narrative](../../../jama_de_boer_2019_oi_190122.pdf#page=4); supplement [p.6 eTable 1 definitions](../../../joi190122supp2_prod.pdf#page=6), [p.10 eTable 5 definition](../../../joi190122supp2_prod.pdf#page=10), [p.13 eTable 8 definition](../../../joi190122supp2_prod.pdf#page=13).
- **Retained scope/calculation:** continuous≥80% versus≥2/3 use on≥4/6 questionnaires, N=1032 for each reported sensitivity set; [79.5,80.5]% versus exact 66.6667% gives minimum gap 12.8333 percentage points/80=0.16042, alongside a separate continuity difference; primary eGFR sensitivity contrasts 0.89(−0.74,2.52) and 0.42(−1.22,2.06) and parallel ACR sensitivity results are affected.
- **Human question/alternative:** which plan authorized the reported consumption/continuity threshold; later operational questionnaire choices may explain it, but no plan-threshold population size is invented.

### DOCUMENTED_OUTCOME_REVISION

- **Finding IDs:** F-XS-009; duplicates F-ST1-008 and F-ST1-009. **Route:** A5. **Focus:** D. **Proposed domain:** protocol_report. **Relationships:** P_R, P_P; primary P_R. **Compared roles:** original PLAN, amended PLAN and REPORT.
- **Complete locations:** plan [p.11 aims](../../../joi190122supp1_prod.pdf#page=11), [p.17 §§VIb–c hierarchy/composite](../../../joi190122supp1_prod.pdf#page=17), [p.19 Table 2 hierarchy](../../../joi190122supp1_prod.pdf#page=19), [p.31 submitted/implemented dates](../../../joi190122supp1_prod.pdf#page=31), [p.32 §15b amendment](../../../joi190122supp1_prod.pdf#page=32); main [p.1 primary outcome](../../../jama_de_boer_2019_oi_190122.pdf#page=1), [p.2 Outcomes/disclosed 2016 change](../../../jama_de_boer_2019_oi_190122.pdf#page=2), [p.3 secondary definitions](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [p.4 composite result](../../../jama_de_boer_2019_oi_190122.pdf#page=4), [p.9 Table 3](../../../jama_de_boer_2019_oi_190122.pdf#page=9).
- **Retained scope/comparison:** original four-year continuous ACR primary/eGFR secondary changes to five-year eGFR primary/ACR secondary; original composite ACR doubling+final≥30, absolute eGFR loss≥12, ESRD/death changes to relative eGFR loss≥40%, ESRD/kidney failure/death without ACR progression; both constituent observations are retained as one endpoint-revision pattern and affect primary 0.9 contrasts plus composite HRs 0.92 and 1.11.
- **Human question/alternative/classification ambiguity:** the source directly supports an amendment submitted March 2, 2015 and implemented February 24, 2016, and the report discloses the primary revision; latest-plan/report agrees, original-plan/report and plan-version definitions differ, so the candidate records the documented original-versus-amended status/definition for human adjudication rather than asserting an undisclosed departure; original Table 2 co-primary wording and the addendum's prior two-year description are retained as history, not additional issues.

### CATEGORICAL_ACR_PRESPECIFICATION

- **Finding IDs:** F-XS-010; duplicate F-ST1-006. **Route:** A5. **Focus:** D. **Proposed domain:** protocol_report. **Relationships:** P_R. **Compared roles:** PLAN versus REPORT.
- **Complete locations:** plan [p.17 original composite](../../../joi190122supp1_prod.pdf#page=17), [p.32 §15b/e amended endpoints](../../../joi190122supp1_prod.pdf#page=32), [p.33 categorical model continuation](../../../joi190122supp1_prod.pdf#page=33); main [p.3 prespecified outcomes](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [p.4 secondary narrative](../../../jama_de_boer_2019_oi_190122.pdf#page=4), [p.9 Table 3/footnote a](../../../jama_de_boer_2019_oi_190122.pdf#page=9).
- **Retained scope/comparison:** standalone Cox time to ACR doubling and final≥30 is called prespecified for HRs 1.34(1.00,1.80), P=.05 and 1.08(.81,1.44), P=.60; latest plan lists continuous ACR and the original composite component does not specify a standalone categorical event-time analysis.
- **Human question/alternative:** which prospective material specifies the standalone analysis; an alternate analysis of continuous ACR or unsupplied amendment is possible, and no separate CI/P candidate is inferred from the boundary display.

### BIOAVAILABLE_SUBGROUP

- **Finding IDs:** F-XS-011; duplicate F-ST1-005. **Route:** A5. **Focus:** D. **Proposed domain:** protocol_report. **Relationships:** P_R. **Compared roles:** PLAN versus REPORT.
- **Complete locations:** plan [p.33 §15f](../../../joi190122supp1_prod.pdf#page=33); main [p.3 subgroup methods](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [p.8 Figure 3](../../../jama_de_boer_2019_oi_190122.pdf#page=8), [p.9 interpretation](../../../jama_de_boer_2019_oi_190122.pdf#page=9), [p.10 interpretation/disclosures](../../../jama_de_boer_2019_oi_190122.pdf#page=10); supplement [p.18 eFigure 2](../../../joi190122supp2_prod.pdf#page=18).
- **Retained scope/comparison:** total and bioavailable are separate planned primary eGFR subgroup dimensions; Figure 3 provides only total 25(OH)D categories <20,20–<30,≥30, and a direct full-report text search plus subgroup-image readings finds no second bioavailable result; the main p.10 bioavailable patent disclosure is not an analysis result.
- **Human question/alternative:** was the bioavailable-defined subgroup performed or prospectively removed; unavailable assays or an unsupplied amendment are not established by the supplied evidence.

### EGFR_ESTIMATOR_IDENTITY

- **Finding IDs:** F-XS-012. **Route:** B. **Focus:** D. **Proposed domain:** protocol_report. **Relationships:** P_R. **Compared roles:** PLAN versus REPORT.
- **Complete locations:** plan [p.17 explicit Equation 1](../../../joi190122supp1_prod.pdf#page=17), [p.32 amended primary eGFR](../../../joi190122supp1_prod.pdf#page=32), [p.30 reference 145](../../../joi190122supp1_prod.pdf#page=30); main [p.3 eGFR construction](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [p.11 reference 19](../../../jama_de_boer_2019_oi_190122.pdf#page=11); supplement [p.2 QC methods](../../../joi190122supp2_prod.pdf#page=2), [p.3 harmonization](../../../joi190122supp2_prod.pdf#page=3), [p.4 continuation](../../../joi190122supp2_prod.pdf#page=4) corroborates calibration history, not equation replacement.
- **Retained scope/comparison:** plan coefficient 177.6 with powers −0.65/−0.57/−0.20 and sex/race multipliers, cited to Stevens et al. 2008, versus report equation cited to Inker et al. 2012; no external coefficients or participant eGFR recalculations are imported, and the discrepancy concerns the supplied estimator identity for primary change and decline endpoints.
- **Human question/alternative:** which final plan specified the report's equation; the original most-precise-methods wording may have allowed updating, but does not itself identify the later named equation as a dated primary estimator specification.

### RANDOMIZATION_STRATA

- **Finding IDs:** F-XS-013. **Route:** B. **Focus:** D. **Proposed domain:** protocol_report. **Relationships:** P_R. **Compared roles:** PLAN versus REPORT.
- **Complete locations:** plan [p.14 §IVc](../../../joi190122supp1_prod.pdf#page=14), [p.31 addendum dates](../../../joi190122supp1_prod.pdf#page=31), [p.32 amended analysis](../../../joi190122supp1_prod.pdf#page=32), [p.33 continuation](../../../joi190122supp1_prod.pdf#page=33); main [p.2 Interventions](../../../jama_de_boer_2019_oi_190122.pdf#page=2).
- **Retained scope/comparison:** age-group-only versus age/sex/race stratification, both with blocks of 8 and the same factorial assignments; inclusion is limited to the explicit planned-versus-reported statistical randomization specification attached to the primary randomized eGFR contrasts and extracted design, not a critique of the allocation choice, an assertion of changed participant counts, or inferred absent covariate adjustment.
- **Human question/alternative:** which final prospective allocation specification added sex/race strata; later parent-trial procedures may explain the report, but the supplied addendum has no randomization revision.

### INTERACTION_TIME_SPECIFICATION

- **Finding IDs:** F-XS-014. **Route:** B. **Focus:** C/D. **Proposed domain:** plan_material. **Relationships:** P_P. **Compared roles:** PLAN Equation 1 versus PLAN Equation 2 within the same addendum.
- **Complete locations:** plan [p.32 §15d Equation 1 and §15e Equation 2](../../../joi190122supp1_prod.pdf#page=32); main [p.3 reported categorical-time model](../../../jama_de_boer_2019_oi_190122.pdf#page=3) and [p.4 interaction P=.42](../../../jama_de_boer_2019_oi_190122.pdf#page=4) corroborate the analysis using the planned decision and do not establish a second relationship.
- **Retained scope/comparison:** setting both treatment indicators to zero removes every printed Equation 1 time term, leaving a constant double-placebo fixed mean, while Equation 2 includes common categorical time; random intercepts do not introduce common fixed change, so the explicit planned interaction equation and primary model provide different time specifications for the interaction/marginal-analysis decision.
- **Human question/alternative:** what exact time specification generated P=.42; an implemented but unprinted common time term or an intentional restriction remains possible, and this is a complete model-term discrepancy rather than an isolated missing glyph or a preferred-analysis proposal.

## Source rereading and derivative record

Direct supplied-PDF rereading used CPU Poppler `pdftotext -layout -f N -l N`, producing uniquely owned derivatives in `preprocessing/inclusion_initial/`: main-1.txt through main-11.txt; plan-4.txt, plan-11.txt, plan-12.txt, plan-14.txt, plan-15.txt, plan-17.txt, plan-19.txt, plan-21.txt, plan-31.txt, plan-32.txt and plan-33.txt; supp-2.txt, supp-3.txt, supp-4.txt, supp-6.txt, supp-7.txt, supp-9.txt, supp-10.txt, supp-11.txt, supp-12.txt, supp-13.txt, supp-16.txt, supp-18.txt and supp-19.txt. Additional direct `pdftotext -layout -f 28 -l 30` produced plan-references-28-30.txt, confirming reference 145 on physical p.30. Full supplementary text was searched directly with `pdftotext -layout ... - | rg` for the subgroup-result absence check. Native output on supplement pp.18–19 contains only captions; both exact-source CPU renderings `preprocessing/numeric_checker/supp2-18.png` and `preprocessing/numeric_checker/supp2-19.png` were visually reread for every count/header/ratio/arrow and subgroup definition. Source-matched reusable `review_1_5_2/preprocessing/rendered_pages/joi190122supp1_prod-p32.png` was visually reread for the full equations, including absence/presence of the time main effect. Engine and device: direct Poppler extraction/rendering, CPU; no fresh OCR, Python or web.

No cited source location was unavailable. Supplied aggregate evidence lacks implemented model code, individual subgroup records, exact arm-specific medication responder denominators, a blood/urine follow-up union and any later complete plan; these are named alternatives/input limitations, not scientific coverage gaps. All sources and reusable derivatives were preserved.

Counts: 29 findings decided; 18 INCLUDE rows / 18 distinct included issues; 11 SCREENED_OUT rows, all DUPLICATE_OF_INCLUDED; zero screened-out findings under other reason codes. Proposed domains: statistical_results 5, protocol_report 11, plan_material 2, report_internal_inconsistency 0.
