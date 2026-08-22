# Numeric consistency review — N001–N094

## Scope and method

This shard covers exactly `N001`–`N094` in `.ai_paper_validation/review_1_5_1/relationships/numeric_relationship_inventory.md`.  Direct authority was `jama_rathinam_2019_oi_190092.pdf` for N001–N039 and `joi190092supp2_prod.pdf` for N040–N094.  The mapped evidence artifacts were used as locators; the two candidate comparisons were re-read in direct PDF text at the cited PDF pages.  Percentages were checked as `100 × count / stated denominator`, accepting the printed precision's usual half-last-unit rounding interval.  Category sums were tested only where categories are stated or defined as mutually exclusive.  Repeated values were compared only after population, time point, treatment actually received versus original assignment, and measurement scale were matched.

## Explicit relationship coverage

| ID | Status | Checks applied and result |
|---|---|---|
| N001 | CHECKED_NO_CANDIDATE | Screening count, sites, and dates are descriptive; 265 agrees with Figure 1. |
| N002 | CHECKED_NO_CANDIDATE | 107 + 109 = 216; assigned-dose units/frequencies are coherent. Main p. 2 also states block sizes 4 and 6, used as cross-document provenance for C003. |
| N003 | CHECKED_NO_CANDIDATE | Dose, weight-or-60-mg cap, daily/weekly frequency, and endpoint thresholds have compatible units. |
| N004 | CHECKED_NO_CANDIDATE | Patient-level composite definition, eye condition, ordinal grade, dose, and drop-count thresholds are compatible. |
| N005 | CHECKED_NO_CANDIDATE | 135 / 216 = 62.5%; 194 / 216 = 89.81%, printed 89.8%. |
| N006 | CHECKED_NO_CANDIDATE | 216 + 49 = 265; exclusions 31 + 11 + 6 + 1 = 49. |
| N007 | CHECKED_NO_CANDIDATE | 107 + 109 = 216; 206 + 201 = 407.  One unexposed MMF patient explains 109 randomized versus 108 allocated. |
| N008 | CHECKED_NO_CANDIDATE | MTX: 107 − 9 − 2 = 96; MMF: 109 − 10 − 1 = 98; 96 + 98 = 194 and 22 / 216 = 10.2%. |
| N009 | CHECKED_NO_CANDIDATE | MTX: 60 + 20 + 9 + 3 + 2 + 2 = 96; MMF: 29 + 54 + 11 + 2 + 2 = 98. |
| N010 | CANDIDATE_DRAFT_02 | Continued-success denominators reconcile (60 + 54 = 114); switching narrative contains a distinct stated-eligible-total versus printed arm-denominator mismatch, detailed below. |
| N011 | CHECKED_NO_CANDIDATE | Sex sums 75 + 32 = 107 and 60 + 49 = 109; all displayed percentages reconcile within 0.05 percentage point. |
| N012 | CHECKED_NO_CANDIDATE | Each race percentage reconciles to arm N.  Categories need not sum because the table footnote says seven patients had more than one heritage. |
| N013 | CHECKED_NO_CANDIDATE | Diagnosis counts sum to 107 and 109 respectively; every percentage reconciles to arm N. |
| N014 | CHECKED_NO_CANDIDATE | Anatomic counts sum to 107 and 109; narrative 46 + 170 = 216 and 21.3% + 78.7% = 100.0%. |
| N015 | CHECKED_NO_CANDIDATE | Previous-immunosuppression counts 8 + 7 = 15; 15 / 216 = 6.9%; dose units/medians are consistently labelled. |
| N016 | CHECKED_NO_CANDIDATE | Grade counts sum to assessed eyes (205 and 201), not all eyes; assessment percentages and grade percentages reconcile to 205/201. |
| N017 | CHECKED_NO_CANDIDATE | Both anterior-vitreous and haze grade sums equal assessed eyes (202 and 200); all percentages reconcile to assessed, not enrolled, eyes. |
| N018 | CHECKED_NO_CANDIDATE | Lesion proportions 125/202 = 61.9% and 119/200 = 59.5%; edema percentages reconcile to 206 and 201.  Units and exclusions are labelled. |
| N019 | CHECKED_NO_CANDIDATE | 64 + 32 = 96; 56 + 42 = 98; successes total 120; success and failure percentages reconcile at stated precision. |
| N020 | CHECKED_NO_CANDIDATE | Each arm's efficacy/intolerability/safety reasons sum to failures (32, 42); percentages reconcile after integer rounding. |
| N021 | CHECKED_NO_CANDIDATE | Subtype denominators sum to primary-analysis N (18 + 78 = 96; 22 + 76 = 98); successes sum to 64 and 56. |
| N022 | CHECKED_NO_CANDIDATE | Continued groups: 48/60 = 80.0%, 40/54 = 74.1%; switched-treatment Table 2 denominators (29, 20) are actual switched-treatment groups, unlike prose's original-arm switch-flow denominators. |
| N023 | CHECKED_NO_CANDIDATE | Mean percent missed doses is labelled a proportion of expected doses; no count denominator is claimed, so no count-rate conversion is warranted. |
| N024 | CHECKED_NO_CANDIDATE | Negative logMAR change is correctly identified as gain; thickness values retain µm and stated edema Ns (42, 55). |
| N025 | CHECKED_NO_CANDIDATE | Narrative medians/IQRs match Table 2 values under sign-versus-wording convention (a reduction of 26 µm corresponds to −26 µm). |
| N026 | CHECKED_NO_CANDIDATE | Dose reductions: 21/107 = 19.6%, 15/109 = 13.8%; patients and eyes are separately labelled. |
| N027 | CHECKED_NO_CANDIDATE | 22/36 = 61.1%, 15/39 = 38.5%; 36 + 39 = 75, matching Figure 2; precision differences are rounding only. |
| N028 | CHECKED_NO_CANDIDATE | 66/107 = 61.7%, 59/109 = 54.1%; imputation is explicitly a different analysis population, not a flow total. |
| N029 | CHECKED_CROSS_SOURCE_CANDIDATE_CONTEXT | Table 3 headers show randomized 107/109 and footnote one unexposed MMF patient, but displayed MMF percentages such as 19 (17.6) reconcile to treated N=108, not header n=109; see C006. |
| N030 | CHECKED_CROSS_SOURCE_CANDIDATE_CONTEXT | Table 3 nonzero MMF percentages follow treated N=108 at displayed precision; overlapping AE rows are not additive. The header-to-percentage denominator convention is the C006 question. |
| N031 | CHECKED_NO_CANDIDATE | 1/107 and 1/109 each print 0.9%; zero cells have no false implied denominator. |
| N032 | CHECKED_NO_CANDIDATE | Each laboratory count/percentage reconciles to arm N; ALT/AST 14 (13.0%) and 8 (7.4%) agrees with abstract/narrative. |
| N033 | CHECKED_NO_CANDIDATE | 3/107 = 2.8%, 2/109 = 1.8% printed 1.9%; threshold/duration label is distinct from nonserious category. |
| N034 | CHECKED_CROSS_SOURCE_CANDIDATE_CONTEXT | Systemic-AE rows are not mutually exclusive; MMF fatigue 59 (54.6) reconciles to treated N=108 rather than header n=109, contributing to C006. |
| N035 | CHECKED_NO_CANDIDATE | All continued systemic-AE percentages reconcile to arm N; temperature/time, rate, and count labels are not conflated. |
| N036 | CHECKED_NO_CANDIDATE | All serious-systemic row percentages reconcile to arm N; event-type rows can overlap and therefore do not test against narrative aggregate. |
| N037 | CHECKED_NO_CANDIDATE | Narrative 14 serious events and 5 drug-related events are event aggregates, whereas Table 3 rows are patients reporting at least one event; no common additive denominator is asserted. |
| N038 | CHECKED_NO_CANDIDATE | Matched abstract, Key Points, table, narrative, and conclusion repeats preserve primary percentages/direction and ALT/AST values. |
| N039 | CHECKED_NO_CANDIDATE | Limitation statements add no incompatible numeric result; country/subgroup qualifiers do not change the underlying population labels. |
| N040 | CHECKED_NO_CANDIDATE | External epidemiology is explicitly non-FAST background; no trial-result comparator exists. |
| N041 | CHECKED_NO_CANDIDATE | Planned 108 + 108 = 216.  Planned allocation is not a contradiction of observed 107/109 randomization. |
| N042 | CHECKED_NO_CANDIDATE | Phase I/II time definitions distinguish 6-month randomized, 12-month continued, and switched-treatment populations. |
| N043 | CHECKED_NO_CANDIDATE | Outcome inventory distinguishes rates/proportions, times, changes, and binary outcomes; no observed total is asserted. |
| N044 | CANDIDATE_DRAFT_01 | The same timeline says enrollment continues through May 2015 but maximum 12-month plus 1-month follow-up finishes through July 2015; direct calendar ordering does not reconcile, detailed below. |
| N045 | CHECKED_NO_CANDIDATE | Eligibility windows, grades, and one-eye rule are compatible labelled thresholds. |
| N046 | CHECKED_NO_CANDIDATE | Prednisone dose/rule and recurrence windows retain units and timing; no reported count is involved. |
| N047 | CHECKED_NO_CANDIDATE | Exclusion cutoffs retain correct units and inequalities; no observed denominator is asserted. |
| N048 | CHECKED_NO_CANDIDATE | Controlled-inflammation components use compatible 0.5+ grades and separate lesions from macular edema. |
| N049 | CHECKED_NO_CANDIDATE | Failure, dropout, and safety/intolerability categories are explicitly distinguished; no flow arithmetic conflict is printed. |
| N050 | CHECKED_NO_CANDIDATE | Laboratory ranges, durations, and units establish category boundaries; endpoint inclusivity is explicitly labelled. |
| N051 | CHECKED_NO_CANDIDATE | MTX and MMF introductory/maintenance/reduction doses and BID/weekly frequencies are internally coherent. |
| N052 | CHECKED_NO_CANDIDATE | Supply quantities/times are prospective schedule quantities, not adherence totals or person-time rates. |
| N053 | CHECKED_NO_CANDIDATE | Prednisone sequence and <=7.5 mg/day endpoint are compatible units; taper schedule does not claim observed use. |
| N054 | CHECKED_NO_CANDIDATE | Optional taper bands and topical frequency preserve their separate route/time units. |
| N055 | CHECKED_NO_CANDIDATE | Mild/severe grade thresholds and 4-week/one-week decision timing are prospective definitions. |
| N056 | CHECKED_NO_CANDIDATE | Calcium and vitamin-D doses retain mg versus IU and daily frequency. |
| N057 | CHECKED_NO_CANDIDATE | Visit windows and prior-14-day laboratory allowance are time definitions, not missingness counts. |
| N058 | CHECKED_NO_CANDIDATE | Month 6/9/12 windows are consistently defined from baseline/treatment administration. |
| N059 | CHECKED_NO_CANDIDATE | Switch, serious-AE exit, and 7-day Baseline-II timing define different populations without a displayed total conflict. |
| N060 | CHECKED_NO_CANDIDATE | Form/visit schedule provides availability definitions only; no completed-form count is claimed. |
| N061 | CHECKED_NO_CANDIDATE | Baseline and follow-up laboratory variable list and 14-day window are coherent. |
| N062 | CHECKED_NO_CANDIDATE | QoL instruments, country populations, and time points are explicitly segregated. |
| N063 | CHECKED_NO_CANDIDATE | Snellen equivalents, VA strata, and 4-m/1-m testing distances are compatible scale labels. |
| N064 | CHECKED_NO_CANDIDATE | Cylinder-power bands are ordered, non-overlapping, and paired with decreasing axis-step sizes. |
| N065 | CHECKED_NO_CANDIDATE | 0.5-D cylinder and 0.25-D opposite-sign sphere rule is a procedural relation, not an outcome total. |
| N066 | CHECKED_NO_CANDIDATE | Poor-VA lens changes and one-letter criterion have coherent units/scale. |
| N067 | CHECKED_NO_CANDIDATE | Repeated axis-step scale matches N064; intentional procedural duplicate, not a duplicated result. |
| N068 | CHECKED_NO_CANDIDATE | Very-poor-VA +/-2.00-D procedure is consistently labelled. |
| N069 | CHECKED_NO_CANDIDATE | Repeated axis/sphere refinement matches N064–N065; intentional procedural duplicate. |
| N070 | CHECKED_NO_CANDIDATE | 14-line charts and geometric letter progression are scale definitions, not patient counts. |
| N071 | CHECKED_NO_CANDIDATE | 0.8 logMAR, 45 letters, and 20/125 are explicitly calibration equivalents, not competing measurements. |
| N072 | CHECKED_NO_CANDIDATE | Lamp degradation, burn-in, distances, and inch/cm conversions are internally compatible at printed precision. |
| N073 | CHECKED_NO_CANDIDATE | <=3, <10, and first-six-row stopping/retest rules preserve their threshold direction. |
| N074 | CHECKED_NO_CANDIDATE | 3/5 count-fingers and 4/5 hand-motion criteria are distinct tests; 1-m and 0.5-m distances are labelled. |
| N075 | CHECKED_NO_CANDIDATE | Score boundary rules and maximum 100 apply to specified testing circumstances; no unsupported conversion was inferred. |
| N076 | CHECKED_NO_CANDIDATE | Snellen >=4/5 line rule is correctly distinct from total-letter score. |
| N077 | CHECKED_NO_CANDIDATE | Certification 18 +/- 2 months and minimum two technicians are administrative thresholds, not an observed total. |
| N078 | CHECKED_NO_CANDIDATE | SUN grade sequence is ordered and cell bands do not overlap under stated <, ranges, and > boundaries. |
| N079 | CHECKED_NO_CANDIDATE | MUST scale is separately labelled 1 mm x 0.5 mm and explicitly excluded from controlled-inflammation criterion. |
| N080 | CHECKED_NO_CANDIDATE | NEI haze 0–4+ ordinal scale is distinct from Davis 0–8 and is consistently labelled. |
| N081 | CHECKED_NO_CANDIDATE | Planned NEI/Davis comparison supplies no observed correlation to calculate. |
| N082 | CHECKED_NO_CANDIDATE | Direct visual check confirms nine ordered Davis panels labelled 0–8; no scale mismatch. |
| N083 | CHECKED_NO_CANDIDATE | Observer timing and primary-observer selection define measurement source, not a result denominator. |
| N084 | CHECKED_NO_CANDIDATE | SD-OCT thickness/change and consistent-device constraint retain outcome/unit distinction. |
| N085 | CHECKED_NO_CANDIDATE | Heidelberg scan dimensions, sections, frames, and >=20 score are device-specific quality requirements. |
| N086 | CHECKED_NO_CANDIDATE | Central subfield thickness is consistently named from the Thickness Map. |
| N087 | CHECKED_NO_CANDIDATE | Zeiss 512 x 218 and >=5 signal-strength scale are device-specific; not numerically compared with Heidelberg >=20. |
| N088 | CHECKED_NO_CANDIDATE | 14-day baseline-lab window, 2× ULN trigger, and one-month re-eligibility interval are coherent prospective thresholds. |
| N089 | CHECKED_NO_CANDIDATE | Nonserious IOP/lab threshold units and inequalities are separately labelled. |
| N090 | CHECKED_NO_CANDIDATE | Serious AST/ALT >=5× ULN and 24-h reporting interval are internally compatible. |
| N091 | CHECKED_NO_CANDIDATE | 48-h completion and 24-h review targets are administrative timing rules, not observed completeness. |
| N092 | CHECKED_NO_CANDIDATE | Two-entry/two- and three-working-day targets are prospective data-quality rules. |
| N093 | CHECKED_NO_CANDIDATE | `NA`, one-row/one-column data structure, <48-h target, and logMAR unit are consistent definitions. |
| N094 | CHECKED_NO_CANDIDATE | Planned monthly monitoring/recruitment/compliance/retention reporting contains no accrued count or rate. |

## Distinct source-grounded candidate drafts

### Candidate draft 01 — protocol timeline end date is incompatible with its enrollment end date and stated maximum follow-up

- **Category:** Numeric or arithmetic inconsistency.
- **Exact source location:** `joi190092supp2_prod.pdf`, PDF p. 11 (printed MOP p. 10), Table 1, “Timeline for study completion.”
- **Printed inputs:** “November 2012 through May 2015 (2.5 years)” for enrollment; “Through December 2015” to finish 6-month follow-up plus one-month window; and “Through July 2015” to finish follow-up, “Maximum of 12 months + 1 month visit window period.”
- **Rule and calculation:** The latest enrollment date is May 2015.  A maximum 12-month follow-up plus a one-month window after that latest enrollment must end no earlier than June 2016 (May 2015 + 13 months).  The printed “Through July 2015” end point is approximately 11 months before the latest possible 12-month completion and is also earlier than the separately printed December 2015 completion of 6-month follow-up.
- **Tolerance:** Calendar months/dates, not rounded quantities; no rounding tolerance can reconcile an end date preceding both the stated six-month completion and the latest-enrollee maximum-follow-up period.
- **Direct observation versus inference:** Direct observation is the three printed timeline entries.  The calendar comparison is a deterministic inference from the explicitly stated latest enrollment and 12-month-plus-one-month duration; it does not assume actual recruitment behavior.
- **Alternative source-grounded interpretation:** This September 2012 MOP may contain a typographical year in the July entry, or the “maximum” schedule may have been intended only for an earlier enrollment cohort.  The table supplies neither qualification.
- **Quality-control relevance:** The inconsistency can misstate planned observation duration and database-lock sequencing for readers matching protocol periods to reported follow-up.
- **Exact human question:** Did the Table 1 entry “Through July 2015” omit or misprint its year, or does a supplied protocol amendment define a restricted cohort/schedule that makes it compatible with enrollment through May 2015?

### Candidate draft 02 — stated eligible failure total does not reconcile with the printed arm-specific switching denominators

- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source locations:** `jama_rathinam_2019_oi_190092.pdf`, PDF p. 7, “Prespecified 12-Month Outcomes”; PDF p. 6, Table 2, 6-month treatment-failure rows; PDF p. 3, Figure 1, 12-month switching flow.
- **Printed inputs:** PDF p. 7 says: “Forty-nine of the 68 eligible patients in whom treatment failed in the first 6 months and who did not have a serious laboratory adverse event switched”; it then says “20 of the 32 (62.5%)” originally randomized to MTX and “29 of the 42 (69.0%)” originally randomized to MMF switched.  Table 2 prints 32/96 and 42/98 failures; Figure 1 prints 20 switched to MMF and 29 switched to MTX.
- **Rule and calculation:** The printed switching numerators reconcile: 20 + 29 = 49.  The printed arm-specific denominators also reconcile to all failures: 32 + 42 = 74.  However, the same sentence identifies 68 as the eligible no-serious-laboratory-AE failure population.  If 20/32 and 29/42 are denominators for that stated eligible switching population, their total is 74, exceeding 68 by 6; if six failures were ineligible, the source does not identify why they remain in the displayed switching denominators.
- **Tolerance:** Exact integer counts; 74 − 68 = 6, so rounding is inapplicable.  The individual percentages are arithmetically correct: 20/32 = 62.5% and 29/42 = 69.0%.
- **Direct observation versus inference:** Direct observation is the p. 7 eligible total, arm fractions, Table 2 failure totals, and Figure 1 switching counts.  The potential inconsistency is the denominator identity implied by the sentence’s linkage of “68 eligible patients” to the immediately following arm-specific switching fractions.
- **Alternative source-grounded interpretation:** The 32 and 42 may intentionally be denominators of all original-arm failures, while 68 is a separate cross-arm eligibility count after excluding six failures; the prose may be reporting switching uptake among all failures rather than among eligible failures.  The supplied article does not explicitly label the two fraction denominators as all failures versus eligible failures.
- **Quality-control relevance:** The ambiguity/mismatch affects the denominator a data extractor would attach to the 62.5% and 69.0% switching proportions and to the Phase-II population.
- **Exact human question:** Are the printed denominators 32 and 42 intended to be all six-month failures or only the 68 eligible no-serious-laboratory-AE failures, and how are the six excluded failures allocated by original treatment arm?

## Summary and limitations

All 94 assigned N relationships received an explicit status.  Two distinct drafts are retained for human review; no stable candidate ID, severity, validity, disposition, or adjudication is assigned here.  Limitations: this numeric shard does not independently assess inferential `S` relationships, and prospective protocol definitions without observed quantities cannot support unreported-count arithmetic.
