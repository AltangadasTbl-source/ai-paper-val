# Fresh Support Evidence Map: Protocol and Statistical Analysis Plan

## Scope and direct-extraction record

Assigned direct sources and complete page coverage:

| Source ID | Source | Pages | Fresh extraction | Result-relevant content |
|---|---|---|---|---|
| DOC-002 | `joi250019supp1_prod_1749674951.29554.pdf` | 1-18 | Native and layout text extracted directly from each page with `pdftotext`; complete | Protocol and amendment log |
| DOC-003 | `joi250019supp2_prod_1749674951.30054.pdf` | 1-7 | Native and layout text extracted directly from each page. Its embedded character encoding is defective, so pages 1-7 were also rendered directly for visual confirmation; complete. | Statistical analysis plan and attestation |

Fresh preprocessing outputs are under `preprocessing/support_protocol_sap/`. DOC-003 page image files are direct renders and were used to resolve the malformed embedded text; OCR was attempted but did not return usable text, so visual source reading was used. No legacy scientific extraction, candidate, checker, or report content was used.

This is an evidence map, not a candidate diagnosis. Values below are planned/protocol values unless explicitly identified as a contemporaneous amendment statement. They must only be compared with a reported trial result after population, study version, outcome, time point, and analysis definition are matched.

## DOC-002: Protocol and amendment log

### Page-level coverage

| PDF page | Coverage and result-relevant extraction |
|---:|---|
| 1 | Table of contents and publication note only; no result-relevant quantitative relationship. |
| 2 | Background comparator evidence and original protocol definitions: MAPEC 187/1084 morning vs 68/1072 bedtime events, RR 0.39 (95% CI 0.29-0.51), P < .001; stated 61% reduction. Design PROBE; community-dwelling treated hypertensive population; inclusion/exclusion definitions. These are external background data, not BedMed trial results. |
| 3 | BedMed primary, secondary, safety, tolerability, and process outcome definitions; original event-driven target, power assumptions, event-rate assumptions, planned enrollment, and follow-up duration. Detailed below. |
| 4 | Allocation and follow-up timing; interim stopping guidance; 24-hour BP and diuretic substudies; original primary Cox model covariates. |
| 5 | Recruitment/enrollment arithmetic and projected duration. |
| 6 | Data-source and quarterly event-reporting description; references only otherwise. |
| 7 | References only; no result-relevant quantitative relationship. |
| 8 | Amendment log: external-validity aggregate-comparator plan and its prespecified variables; original 24-hour BP sample-size amendment noted but no number printed on this page. |
| 9 | Amendment log: participant-code correction (3 to 5 digits); expansion from original 8750 to 11,700 participants and added BC/Manitoba enrollment. |
| 10 | Amendment log: 24-hour BP substudy explicitly specified as 151 intervention and 151 control participants, each monitored for 24 hours; other administrative/recruitment content. |
| 11 | Recruitment-advertising context and descriptive external percentages only (80%, 74%, about 58%, 89%, 68%, 72%, 22%, 47%, 67%); no BedMed outcome result. |
| 12 | Self-timing amendment: up to 2 BP medicines, one at a time, at least 1 month apart; call at 1 week after each change; eligibility and medication-count definitions. |
| 13 | Recruitment-letter substudy: over 1700 participating Canadians stated at amendment time; roughly 6400 packages, baseline 8% response, target 2 percentage-point absolute difference, alpha .05, 80% power. Also begins aggregate representativeness amendment. |
| 14 | Representativeness amendment: three aggregate cohorts; adds screening/preventive-therapy measures and all-cause hospitalization rate during the study; specialist and family-physician visits in prior year; two additional withdrawal/noncompliance cohorts. |
| 15 | External-validity administrative comparison cohort described as approximately 70,000 eligible patients at participating practices. |
| 16 | Amendment: reported events reconciled to administrative claims; study extension entails additional 6-monthly surveys through end of 2023; data-sharing amendment begins. |
| 17 | Data-sharing amendment: analytic dataset contains 3357 individuals; separate unlinked 24-hour BP worksheet contains 302 individuals; exact de-identification fields and process. |
| 18 | Completes data-sharing-request process only; no result-relevant quantitative relationship. |

### Outcome, population, and analysis definitions (direct protocol evidence)

- **P3 primary outcome:** composite first event of all-cause death or hospital admission/ED visit for acute coronary syndrome/MI, heart failure, or stroke. The platform monitors this quarterly and the protocol says the trial ends at 406 primary events.
- **P3 secondary outcomes:** each primary component; all-cause admission; resource-intensity weight and length of stay; nursing-home admission; EQ-5D quality-of-life measures. Safety: new glaucoma diagnosis/surgery, hip fracture, self-reported vision worsening, syncope, and falls. Tolerability: overnight urinations, nocturia burden, and light-headedness/faintness. Process: proportion of baseline BP medicines switched by 6 months and 24-hour ambulatory BP at 6 months.
- **P3 original sample-size relationship:** 1:1 survival analysis, 80% power, two-sided type-I error alpha=.05, target 25% relative-risk reduction; 379 events required without useful covariates. Increasing by 7% produces 406 events for projected withdrawal/nonadherence/loss (combined 5% in pilot). Expected control event rate 2.9%; expected overall event rate 2.0%. The protocol expects 8750 enrolled over 12 months, then 22 more months follow-up, to provide 406 events.
- **P4 allocation:** simple central REDCap randomization, no stratification or blocking. Follow-up at 1 week, 6 weeks, 6 months, then every 6 months. Original plan says 31% of pilot participants chose automated online follow-up after 6 months.
- **P4 interim analysis:** independent DSMB review at 200 events (anticipated 20 months); clinical consideration of early stopping if P <= .001 for benefit or P <= .05 for harm. This is a protocol decision rule, not a reported effect estimate.
- **P4 original substudy plan:** 100 intervention and 100 control participants for 24-hour BP at 6 months; diuretic-tolerance review after enrollment of 200 participants whose only BP medicine is a diuretic.
- **P4 primary statistical method:** Cox proportional-hazards survival analysis. Original listed baseline covariates: age >=80, sex, frailty binary, cognitive impairment binary, smoking, hospitalization in prior 6 months, >=3 baseline BP medicines, diabetes, CHF, stroke/TIA, coronary artery disease, and significant renal impairment (claims diagnosis, eGFR <40, or dialysis).
- **P5 recruitment arithmetic:** estimated 250 hypertensive patients/practice; 365 physicians x 250 mailed = 91,250 mailed letters; 85% BP-medicine use and 12% interested/eligible yields stated expectation of 8750 enrolled. Projected 35/day enrollment over one year. Protocol contrasts a 25% powered relative reduction with a MAPEC-like effect and describes projected completion intervals; these are projections, not results.

### Amendment-sensitive quantities and definitions

- **P8 external-validity comparison:** aggregate (not individual-level) trial participant vs practice-population characteristics include gender, age, hospitalization within prior 6 months, proportions with diabetes/CHF/stroke-TIA/CAD/sleep apnea, >=3 BP-lowering medicines, >=4 non-BP medicines, kidney disease, plus comorbidity, rurality, attachment, and practice size; approximately 365 practices.
- **P9 enrollment version change:** the 27-Jun-2017 amendment says study-wide sample size expanded from 8750 to 11,700. This supersedes the original projection for that protocol version; neither is a final analyzed denominator without matching to an actual report population/timepoint.
- **P10 BP substudy revision:** 151 intervention plus 151 control participants, ambulatory monitor for 24 hours, replacing/clarifying the earlier P4 original 100+100 plan. This matches the later SAP process description of a consecutive Alberta-resident sample of 302, but should be matched by date/version before comparison.
- **P12 medication-change process:** up to two antihypertensives, sequentially as tolerated, at least one month between changes. "Medically simple" excludes more than two antihypertensives (alpha blockers excluded) and specified clinical/medication criteria. This is an intervention-process definition rather than a trial outcome.
- **P13 recruitment substudy:** stated equal distribution of original versus altered letters, inferable by even versus odd letter dates; approximate 6400 mailings; baseline response 8%; power calculation targets a 2% absolute response-rate difference at alpha=.05 and 80% power.
- **P14-P15 representativeness expansion:** three aggregate cohorts are trial participants, eligible patients attached to participating practices, and eligible Albertans province-wide. P15 describes the practice-attached comparison cohort as around 70,000. These are administrative comparator cohorts, not the randomized analysis population.
- **P16-P17 study-close/data sharing:** extension supplies further surveys every six months to end of 2023. Planned shared analytic data set: 3357 individuals, with birth date replaced by age in years at randomization; no Study ID, province, event dates (days since randomization used instead), or last-contact dates (censoring days/type used). Separate unlinked 24-hour BP page: 302 individuals.

## DOC-003: Statistical Analysis Plan

### Page-level coverage

| PDF page | Coverage and result-relevant extraction |
|---:|---|
| 1 | Contents/version statement: only SAP version, created before interim analysis and submitted 1-Dec-2021; no result result. |
| 2 | Primary and secondary outcome definitions; supplementary safety outcome definitions; begins nocturia definition. |
| 3 | Completes nocturia definition; cost/exploratory/process outcomes; intention-to-treat, loss-to-follow-up, withdrawal, and missing-data rules. |
| 4 | Nonadherence rule; covariate-selection limit; Table 1 begins, defining primary and several secondary analysis methods and covariates. |
| 5 | Table 1 continues: remaining secondary, safety, cost, and exploratory models; process tests. |
| 6 | Table 1 footnotes, subgroup and sensitivity analysis definitions. |
| 7 | Signed attestation dated 1-Oct-2024 that analyses used all available participants and adhered to the detailed SAP. No numerical result. |

### SAP outcome definitions and reporting keys

- **Primary (P2):** MACE, first occurrence of all-cause death or hospital admission/ED visit for ACS/MI, stroke, or CHF. Unless otherwise stated outcomes are recorded over study duration.
- **Secondary (P2):** each primary component; all-cause hospitalization/ED visit; LTC admission; nonvertebral fracture; new glaucoma diagnosis; and cognitive decline at 18 months, defined as >=2-point worsening from baseline on Short Blessed Test.
- **Supplementary safety (P2-P3):** vision = much worse at any follow-up or slightly worse on >=2 occasions (reported every six months); cognition = newly >=10 on Short Blessed Test at 18 months or new dementia diagnosis; symptomatic hypotension = recent light-headedness/feeling faint without loss of consciousness, fainting, falling, or hip fracture; nocturia = change in overnight urinations/week and burden categories at 6 weeks and 6 months.
- **Cost (P3):** acute-care cost is estimated from each hospital admission's resource-intensity weight and length of stay; total care cost = acute-care cost + medication costs + physician billings. Both are claims-derived; persons without claims data are excluded from that analysis.
- **Exploratory/process (P3):** EQ-5D-5L overall-health score at 12 months; proportion of BP medication doses at allocated time at 6 months (twice-daily medicine = one-half AM and one-half PM dose); sleep-time systolic BP at six months in a consecutive sample of 302 Alberta residents. Investigators may view aggregate process and 24-hour BP data but otherwise remain outcome-blinded.

### SAP analysis rules and methods

- **P3 intention-to-treat and censoring:** a lost participant with claims continues as active and survival data are censored at later of last medical service or death indication; without claims, censor at last successful telephone/email contact. Withdrawal retains claims follow-up if consented; otherwise censor at withdrawal date. Missing data are imputed from subsequent/preceding follow-up or the participant is excluded, analysis-specific and aiming to minimize bias or be conservative when unavoidable. Nonadherence does not exclude participants except harms meaningful only on treatment.
- **P4 covariate-selection rule:** maximum one covariate per 10 outcome events for dichotomous outcomes and one per 20 randomized participants for continuous outcomes; prespecified baseline covariates selected in listed order, no stepwise addition/subtraction.
- **P4-P6 Table 1 models:** primary MACE, all-cause mortality, stroke hospitalization, MI/ACS hospitalization, CHF hospitalization, all-cause hospital/ED visit, nonvertebral fracture, LTC admission, new glaucoma diagnosis, and hip fracture use Cox proportional hazards; 18-month cognitive decline, worsening vision, new dementia-consistent impairment, and the grouped light-headedness/syncope/falling outcomes use Poisson regression; nocturnal-urination change uses Mann-Whitney or t test; major nocturia burden uses Fisher exact; acute and total costs and overall-health score use multiple linear regression. Exact covariate lists are visually confirmed in Table 1 (pp.4-6), including predefined measures/footnotes below.
- **P6 covariate measurement labels:** physical-frailty score is Tilburg physical-frailty subscale, continuous 0-8; overall health is EQ-5D-5L, continuous 0-100; CKD excludes dialysis; exercise days asks days in prior week with >=30 minutes vigorous enough to raise breathing rate, continuous 0-7.
- **P6 subgroup analysis:** repeat primary analysis for presence/absence of age >=75, sex, physical frailty >=3, polypharmacy >=5 medicines, overall-health score <=75, resistant hypertension >=3 BP-lowering medicines, CHF, diabetes, CAD, stroke/TIA, sleep apnea, CKD with/without dialysis, and sedentary status (zero exercise days/week).
- **P6 sensitivity analysis:** by treatment group, compare baseline characteristics of those censored for withdrawal/loss to follow-up with those not censored that way using Fisher exact test.

## Matching cautions for downstream cross-source review

1. Different documents deliberately show several planned/revised quantities: original 8750 vs amended 11,700 enrollment, 100+100 vs amended 151+151 BP monitoring, and an eventual 302-person Alberta BP sample. Treat these as version- and population-specific planning/revision statements, not direct contradictions.
2. The SAP primary effect is a time-to-first-event Cox analysis of MACE. A main-paper result must be matched to its outcome definition, analysis population, follow-up/censoring convention, adjustment set, and effect-measure scale before comparison.
3. Protocol/SAP values on external background trials, recruitment projections, aggregate administrative cohorts, and data-sharing files are not randomized trial result denominators.

## Extraction limitations

DOC-003 embedded PDF text has malformed font encoding. Direct rendered pages were visually inspected to confirm every page and transcribe its material evidence; fresh native/layout text is retained as an auxiliary locator. Targeted Tesseract was attempted but generated no usable output. No source page is unmapped.
