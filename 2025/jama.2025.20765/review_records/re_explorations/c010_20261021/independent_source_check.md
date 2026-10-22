# Independent source check: planned male/female primary-outcome subgroup analysis

Date: 2026-10-21. Scope: a bounded source-only follow-up, not a complete Workflow 1.6.2 review. This note was developed without reading earlier candidate, checker, screening, recheck, audit, final-report, or re-exploration conclusions. No new candidate ID is assigned.

The supplied SAP specifies male/female subgroup analyses of the primary treatment effect, using a separate mixed-effects model for each subgroup and reporting RRs and 95% CIs. The main article and results supplement do not supply the male/female treatment-effect results, and the complete report-text searches did not locate a corresponding amendment, nonestimation statement, or reason for nonreporting. This supports a planned-versus-reported analysis reporting issue under Route A, category 5. It does not establish that the analyses were not performed or that the SAP was finalized before outcome data were available.

## Exact source evidence

PDF pages below are physical PDF pages. SAP printed pages and line numbers are those visible on the source page. Main article and results-supplement pages have no printed line numbers; sections and table rows provide the locations. Quotations retain source wording, with line-wrap hyphenation joined.

| Role and source location | Exact English source quotation or printed content | Source-based reading |
|---|---|---|
| PLAN: [SAP PDF p92](../../../joi250093supp1_prod_1768590553.08963.pdf#page=92), printed p15, §38 “Sub-group Analyses,” lines 2936–2939 | “We will perform sensitivity analyses to evaluate how stable the primary treatment effect remains across important subgroups.” | The stated target is the primary treatment effect; the SAP describes this analysis as a sensitivity analysis. |
| PLAN: [SAP PDF p93](../../../joi250093supp1_prod_1768590553.08963.pdf#page=93), printed p16, §38, line 2942 | “gender (male vs. female), and smoking duration (<24 years vs. ≥24 years).” | Male/female is an explicit planned subgroup factor, alongside age, education, occupation, and smoking duration. |
| PLAN: same page, lines 2943–2946 | “Each subgroup will have its own mixed-effects model applied while accounting for clustering at site level through a random intercept. We will compute both the relative risk (RR) and the 95% confidence intervals (CIs) for smoking cessation.” | The plan calls for subgroup-specific treatment estimates and intervals; adding sex as a covariate does not supply these outputs. |
| PLAN: same page, lines 2946–2952 | “Researchers will assess the treatment effect's consistency between subgroups through qualitative comparison of RRs and CIs. The researchers will disclose any missing confidence intervals while analyzing subgroup results with caution due to limited statistical power alongside their exploratory analysis nature.” | The planned comparison is qualitative; no interaction-test requirement is inferred. The SAP explicitly anticipates disclosure of missing CIs and acknowledges limited power and exploratory interpretation. |
| PLAN: [SAP PDF p98](../../../joi250093supp1_prod_1768590553.08963.pdf#page=98), printed p21, line 3014/table heading; [continuation p99](../../../joi250093supp1_prod_1768590553.08963.pdf#page=99), printed p22, table above lines 3016–3017 | Heading: “sub-groups for verified abstinence at 6 months”; columns “Variable,” “Category,” “RR,” “CI95%”; continuation rows “Gender,” “Male,” “Female,” with blank RR/CI cells. | This is a planned table shell with unfilled result cells, not reported male/female estimates or evidence of nonestimation. |
| REPORT: [main PDF p3](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3), printed p338, right column, Statistical Analysis, final paragraph | “We compared the primary outcome between the following prespecified subgroups: age (<40 years and ≥40 years); education (no formal education, primary, secondary or higher); employment (active, dependent, retired); and smoking duration (<24 years and ≥24 years).” | This report-methods list omits male/female and contains no explanation for that omission. |
| REPORT: same page, Statistical Analysis, second paragraph | “A mixed-effects model was used to assess the effect of mHealth on abstinence outcomes, incorporating fixed effects for the intervention and relevant covariates selected post hoc (age, sex, education, occupation, and smoking duration) and random effects for clusters.” | Sex appears as an adjustment covariate, which is distinct from estimating the intervention contrast separately within male and female subgroups. |
| REPORT: [main PDF p5](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5), printed p340, Table 1, “Sex, No. (%)” rows | Male: mHealth “698 (96.9),” usual care “345 (95.8)”; female: mHealth “22 (3.1),” usual care “15 (4.2).” | There are 37 female participants across the two arms. These are baseline counts, not abstinence counts or sex-specific treatment RRs. |
| REPORT: same page, right column, Secondary Outcomes, final paragraph | “Subgroup analyses demonstrated that the treatment effect remained consistent across age, education, employment, ability to read Short Message Service messages, and smoking duration categories (eTable 8 in Supplement 2).” | The subgroup narrative omits male/female; it does not claim consistency across sex. |
| REPORT: [results supplement PDF p12](../../../joi250093supp2_prod_1768590553.09463.pdf#page=12), printed p12, eTable 8 | “Unadjusted Relative Risks among sub-groups for verified abstinence at month 6”; columns “Variable,” “Category,” “RR,” “95CI%.” | This is the direct reported counterpart for the planned month-6 abstinence subgroup table, but it has no sex/gender, male, or female result rows or missing-CI explanation. |
| REPORT: [main PDF p8](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=8), printed p343, right column, Limitations, first point | “First, participants were almost entirely male (>96%). This is not surprising, given that in Bangladesh and Pakistan, 97.8% and 91.4%, respectively, of all adult individuals who smoke are men.” | This acknowledges the population composition. It does not say the planned male/female subgroup models were unestimable, omitted, withdrawn, or amended. |

## Complete reported subgroup-table categories

The following categories are visually confirmed in results-supplement eTable 8, physical/printed p12. The education threshold below follows the image, whose symbol is ≥.

| Variable | Categories printed in eTable 8 |
|---|---|
| All | Overall row; RR 2.890, 95% CI 1.983–4.709 |
| Age | <40; ≥40 |
| Education | No formal education; Primary (year 1-5); Secondary or above (year ≥6) |
| Occupation | Active in job/business; Dependent or retired |
| Smoking Duration | <24 Years; ≥24 Years |
| Reading SMS | Yes; No |

There are 11 subgroup-category rows under five factors, plus the overall row. No male/female category or nonestimation footnote appears in this display. Reading SMS is recorded only to describe the complete table; this note does not assess its planning status as an additional issue.

## Searches and potential counterparts

The complete main article (9 physical PDF pages) and results supplement (16 physical PDF pages) were searched using the existing full layout-text locators and independently using `pdftotext -layout` on each original PDF with output to stdout only. Search terms covered sex, female, male, gender, men/women, subgroup/sub-group, nonestimation/estimability, amendment/deviation, convergence, sparsity, omission, and statements that models could not be estimated. Search hits were examined in their local paragraphs and displays. No male/female primary-outcome treatment-effect counterpart or explicit explanation for its absence was located elsewhere in those reports.

Two apparent substitutes do not provide the planned contrasts:

- Results-supplement [eTable 7, physical/printed pp10–11](../../../joi250093supp2_prod_1768590553.09463.pdf#page=10), “Cluster Characteristics and Associated Unadjusted Relative Risks,” has the cluster-characteristic column “Male, n(%)” and a [bottom-row RR of 0.83 (95% CI 0.34–2.02), p11](../../../joi250093supp2_prod_1768590553.09463.pdf#page=11). This is a reported association with cluster composition, not two intervention contrasts estimated within male and female participants.
- Sex adjustment is also stated in main Table 2, [physical p6/printed p341, footnote a](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6), and results-supplement [p14, footnote e](../../../joi250093supp2_prod_1768590553.09463.pdf#page=14). Those adjustment descriptions do not replace subgroup-specific results. Main Table 2 footnote f explicitly says: “Mixed-effects models could not be estimated for treatment default and treatment failure due to very low numbers of events across clusters.” That explanation concerns those two TB outcomes, not male/female abstinence subgroups.

## Scope assessment, alternatives, and limits

The cross-document comparison concerns explicitly specified exploratory/sensitivity subgroup analyses of the primary outcome, not separate co-primary endpoints, so it meets the eligible plan-versus-report comparison tier rather than the peripheral descriptive tier. Roles are PLAN for the SAP and REPORT for both article and results supplement. Primary relationship and all relationships: `P_R`; review domain: `protocol_report`; focus area: D. The two report documents corroborate the reporting gap and do not create a separate report-versus-report inconsistency.

Qualifying route: **Route A, category 5**, because a planned subgroup analysis of the primary treatment effect lacks a reported counterpart in the supplied reports. The reproduced observation is about reporting completeness, not an arithmetic discrepancy; display-precision intervals and relative discrepancy are not applicable. The specific unavailable extraction is the male- and female-specific intervention RR and 95% CI for verified abstinence at month 6, with the corresponding ability to assess the SAP's planned qualitative consistency comparison.

A source-grounded possible explanation is sparse female participation: the baseline table contains 22 and 15 female participants, and the Limitations paragraph acknowledges the male predominance. This might motivate nonestimation or cautious reporting, but the supplied reports do not state that causal link or supply outcome events by sex. Neither estimability nor subgroup effects can be reconstructed from these baseline counts. The SAP's exploratory/limited-power wording supports caution and explicitly anticipates disclosure of missing CIs; it does not cancel the male/female specification. No formal interaction test is inferred or requested.

The supplied SAP's future-tense statements establish its written specification, not the timing of finalization relative to data access. This bounded check does not establish historical prespecification, an undisclosed amendment, whether models were attempted or completed, or any effect on the overall intervention estimate. It supports only that the specified male/female primary-outcome analysis and an explicit explanation for its absence were not found in the supplied article and results supplement.

## Inspection record

Visually inspected existing source-matched images: SAP physical pp92, 93, 98, 99; main physical pp3, 5, 6, 8; results-supplement physical pp10, 11, 12, 14. Source-native/layout text served only as a search/transcription aid. Full main/results text was searched; this is not a page-by-page visual audit of every report page or a complete search of every plan version. `QUALITY_CONTROL_SCOPE.md` and the review contract's complete Inclusion screen section were read. No external evidence, earlier scientific conclusions, renders, OCR, installations, preprocessing derivatives, or files outside this assigned note were used or created.

Bounded result count: one distinct planned-versus-reported relationship assessed; one reporting issue meets Route A, category 5; zero additional issues registered; zero formal checker finding IDs assigned or screened in this source-only assignment. No severity or disposition is assigned.
