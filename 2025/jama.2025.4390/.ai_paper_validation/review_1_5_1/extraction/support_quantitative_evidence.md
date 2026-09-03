# Canonical Support Quantitative Evidence

## Fresh-source merge scope and provenance

This canonical map merges, without candidate selection, the complete fresh direct-source evidence maps for DOC-002 (protocol), DOC-003 (SAP), and DOC-004 (results supplement). The component maps remain preserved and are part of this canonical map's auditable evidence record; all page-level transcriptions, continuation tables, visual-confirmation notes, and limitations are retained at the exact paths below.

| Component artifact | Direct-source scope | Complete relationships retained |
|---|---|---|
| `extraction/parts/support_protocol_sap.md` | DOC-002 pp. 1-18; DOC-003 pp. 1-7 | Protocol/SAP outcomes, definitions, planning/revisions, analysis rules, model types, covariates, censoring, sensitivity/subgroup rules |
| `extraction/parts/support_results_001_024.md` | DOC-004 pp. 1-24 | Adjudication counts; ABPM methods/flow; statistical framework; baseline medication figure; page-complete no-applicable units |
| `extraction/parts/support_results_025_049.md` | DOC-004 pp. 25-49 | Retention, class adherence, recruitment/interview tables, baseline/retention tables, medication tables, timing-change table, ABPM table |

The direct-source component text is authoritative for full cell-level values. This canonical document assigns its cross-package relationship identifiers below and preserves all mapped values, exact source pages, definitions, match keys, and mapper provenance through the indicated component heading.

## DOC-002 protocol and DOC-003 SAP relationship register

| Canonical relationship | Exact location(s) | Values, definitions, and main-paper match key | Mapper provenance |
|---|---|---|---|
| SUP-P01 primary outcome/planned event target | DOC-002 p.3 | First death or hospital/ED ACS/MI, HF, or stroke; trial ends at 406 primary events. Match: primary composite definition/event target. | `support_protocol_sap.md`, DOC-002 P3 |
| SUP-P02 original power/sample plan | DOC-002 p.3 | 1:1 survival, 80% power, alpha .05, 25% relative reduction; 379 events +7%=406; expected control 2.9%, overall 2.0%; 8750 enrolled, 12-month enrollment plus 22-month follow-up. | DOC-002 P3 |
| SUP-P03 original allocation/follow-up/interim plan | DOC-002 p.4 | Central simple REDCap randomization/no stratification or blocks; contacts 1 week, 6 weeks, 6 months, then 6-monthly; 200-event DSMB review; benefit P<=.001/harm P<=.05. | DOC-002 P4 |
| SUP-P04 original ABPM/diuretic substudies | DOC-002 p.4 | Original ABPM 100+100 at 6 months; diuretic review after 200 monotherapy-diuretic participants. | DOC-002 P4 |
| SUP-P05 original covariate set | DOC-002 p.4 | Cox: age >=80, sex, binary frailty/cognitive impairment, smoking, prior hospitalization, >=3 BP medicines, diabetes, CHF, stroke/TIA, CAD, renal impairment. | DOC-002 P4 |
| SUP-P06 recruitment projection | DOC-002 p.5 | 365x250=91,250 mailed; 85% use BP medicine and 12% interested/eligible => projected 8750; 35/day. | DOC-002 P5 |
| SUP-P07 amendment enrollment revision | DOC-002 p.9 | 27-Jun-2017 enrollment expands 8750 to 11,700. Version-specific plan, not final analyzed denominator. | DOC-002 P9 |
| SUP-P08 ABPM amendment | DOC-002 p.10 | 151 intervention +151 control, 24-hour monitoring; revision of original 100+100 and match to later 302-person sample. | DOC-002 P10 |
| SUP-P09 letter-recruitment substudy | DOC-002 p.13 | >1700 Canadians; about 6400 packages; 8% baseline response; target 2-point difference, alpha .05, 80% power. | DOC-002 P13 |
| SUP-P10 representativeness/data-sharing values | DOC-002 pp.14-17 | Three aggregate cohorts; practice comparator about 70,000; 6-month surveys through 2023; planned analytic dataset 3357 and separate ABPM dataset 302. | DOC-002 P14-P17 |
| SUP-S01 SAP outcomes and definitions | DOC-003 pp.2-3 | MACE time-to-first-event; primary components; definitions for cognition, vision, hypotension, nocturia, costs, EQ-5D, and 302-person ABPM process measure. | `support_protocol_sap.md`, DOC-003 P2-P3 |
| SUP-S02 SAP ITT/censoring/missingness | DOC-003 p.3 | ITT; claims-based follow-up/censoring conventions; withdrawal handling; analysis-specific missing-data imputation/exclusion rule; nonadherence exception for on-treatment harms. | DOC-003 P3 |
| SUP-S03 SAP model/covariate rule | DOC-003 pp.4-6 | Maximum 1 covariate/10 dichotomous events or /20 randomized continuous participants; Cox for time-to-event outcomes, Poisson for stated safety outcomes, linear regression for costs/QoL, specified tests for nocturia; no stepwise selection. | DOC-003 P4-P6 |
| SUP-S04 SAP subgroup/sensitivity definitions | DOC-003 p.6 | Primary subgroups include age, sex, frailty, polypharmacy, health score, resistant hypertension, CHF, diabetes, CAD, stroke/TIA, apnea, CKD/dialysis, sedentary; withdrawal/loss sensitivity uses Fisher exact. | DOC-003 P6 |

## DOC-004 pp.1-24 relationship register

| Canonical relationship | Exact location(s) | Values/definition/match key | Mapper provenance |
|---|---|---|---|
| SUP-R01 adjudication counts | pp.10-12, Fig.3-1 | Exact rejected/total/accepted counts for death, ACS, HF, stroke, unplanned hospital/ED, hip fracture, glaucoma, non-vertebral fracture; reporting sources overlap and must not be summed. Match: accepted outcome counts/ascertainment, not allocation effect. | `support_results_001_024.md`, R-D004-001 |
| SUP-R02 ABPM methods/flow | pp.18-19, Fig.4-1 | 151/151 analyzed; median 9.6 months (IQR 7.1-29.2); minimum 5 overnight/8 daytime readings; 346/356 invited, arm-specific consent/inadequacy/repeat/replacement flow and reason sums. Match: ABPM population/timepoint. | R-D004-002 |
| SUP-R03 support analysis framework | pp.20-21 | Count/percent and mean/median plus SD/IQR rules; covariate modal/mean replacement and no outcome imputation; Cox/reduced models; full primary covariates; 1000-pattern PH check; secondary-outcome changes. | R-D004-003 |
| SUP-R04 baseline medicine figure | pp.23-24, eFig.2 | Exact morning/bedtime counts by named ACEI, ARB, CCB, diuretic, beta-blocker, other, and combination medicines. Medicines are nonexclusive, not participant denominators. | R-D004-004 |

## DOC-004 pp.25-49 relationship register

| Canonical relationship | Exact location(s) | Values/definition/match key | Mapper provenance |
|---|---|---|---|
| SUP-R05 withdrawal/loss trajectory | p.25, eFig.3 | End text unable-to-follow: bedtime 3.4%, morning 2.6%; dashed all withdrawal/loss visually about 19.6%/17.9% and explicitly approximate. | `support_results_025_049.md`, SR025-R01 |
| SUP-R06 six-month class timing adherence | p.26, eFig.4 | Exact AM/PM class triplets (as allocated/off allocation/twice+) for ACEI, ARB, beta blocker, CCB, combination, diuretic, other; match eTable 6. | SR026-R02 |
| SUP-R07 recruitment methods | p.27, eTable1 | Randomized N=3357 (morning 1680/bedtime1677), class counts/percentages; 436 PCPs, 41,128 letters, median 77.5 letters/PCP, 6.2% randomized. | SR027-R03 |
| SUP-R08 interview mode | p.28, eTable2 | Exact online/phone/total interviews at week 1, week 6, months 6-72, and 18-month SBT. | SR028-R04 |
| SUP-R09 expanded baseline | pp.29-32, eTable3 | Exact bedtime/morning/overall baseline counts and percentages, demographics, measures, comorbidity, medication counts/classes, definitions. | SR029-R05 |
| SUP-R10 completion/loss baseline comparison | pp.33-36, eTable4 | Completed/death n=2726 vs withdrew/lost n=631; exact page-cell values and unadjusted p-values retained in mapper artifact. | SR033-R06 |
| SUP-R11 unable-to-follow allocation comparison | pp.37-40, eTable5 | Morning n=44 vs bedtime n=57; baseline values/p-values, including printed Other ethnicity row 40 (90.9%) vs 53 (93.0%) duplicating the preceding White row. | SR037-R07 |
| SUP-R12 six-month medication use | pp.41-42, eTable6 | Exclusion/missing interview counts; 1514/1567 morning vs 1341/1518 bedtime at allocation; dose percentages 94.2/83.5; complete medication/class timing cells and dose rule. | SR041-R08 |
| SUP-R13 longitudinal timing adherence | pp.43-44, eTable7 | Exact months 6-72 arm-specific participant/Rx denominator, at-allocation count/percent, dose percent, timing distributions and rules. | SR043-R09 |
| SUP-R14 timing-change success/failure | pp.45-48, eTable8 | Exact medicine-level class/timing success and failure values/reasons; cells and multiple-response rule. | SR045-R10 |
| SUP-R15 ABPM results | p.49, eTable9 | Bedtime/morning N=151/151; awake/sleep SBP/DBP means, differences/CIs/P values, dipping and control counts/percentages/definitions. | SR049-R11 |

## Completion and limitations

All support units DOC-002 pp.1-18, DOC-003 pp.1-7, and DOC-004 pp.1-49 are mapped. The three cited component maps preserve every direct transcription and page-complete no-applicable record. DOC-003 encoding and figure-heavy DOC-004 units required direct rendered-page confirmation as documented in those artifacts. Planning/amendment quantities are explicitly version-specific and must not be treated as final-result contradictions without a matched cross-source check.
