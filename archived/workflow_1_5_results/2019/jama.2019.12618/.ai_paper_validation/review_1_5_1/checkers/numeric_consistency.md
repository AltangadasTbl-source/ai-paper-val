# Canonical numeric consistency review — N001–N282

This canonical artifact losslessly consolidates the assigned numeric-consistency shards in sequence: N001–N094, N095–N188, and N189–N282. Each shard retains its own scope, source provenance, calculations, outcomes, candidate drafts, and limitations.

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

# Numeric consistency check: N095–N188

## Scope, evidence, and method

This shard checks exactly `N095` through `N188` (94 relationships) in the global numeric relationship inventory. Direct authority was `joi190092supp2_prod.pdf` for protocol records and `joi190092supp3_prod.pdf` for SAP records. I used the named page-complete source maps as locators and their documented direct-PDF extraction/visual confirmation; no legacy candidate, ledger, report, or disposition was used.

Each record was examined for applicable arithmetic, totals, numerator/denominator/percentage identities, missingness/population identity, rounding, unit/scale/reference labels, rate-versus-count distinctions, repeated values, and cross-location matching. These pages state protocol/SAP definitions and planning quantities, not accrued result tables. Therefore a same-subject, same-population, same-timepoint observed-result comparator is generally absent. A procedural repetition, a revision-history change, or differing chart branch is not treated as a contradiction.

**Tolerance.** Exact identities use zero tolerance unless the source states a rounded value; decimal planning displays use their stated precision (one decimal: plus or minus 0.05; whole percent: plus or minus 0.5 percentage point). Schedule windows and thresholds are interpreted as printed inclusive/exclusive bounds. No candidate draft was generated merely from a definition without a matched conflicting reported result.

## Coverage records

| Global ID | Exact source location; printed inputs | Reproducible check and result | Direct observation versus inference; alternatives; QC relevance and human question |
|---|---|---|---|
| N095 | Protocol `joi190092supp2_prod.pdf#page=57` (printed 56): weekly eligible-screened/enrolled/ineligible/follow-up reports; biweekly enrollment reports; twice-yearly chart review. | No counts or denominator are printed. Rate/count/total check is not computable. | Direct: monitoring cadence only. Inference: it cannot establish an observed flow total. Alternative: later report may use another period. QC relevance only if a reported flow total is matched. Human question: which accrued report, if any, supplies these counts? |
| N096 | Protocol `#page=58` (printed 57): BCVA letters and Snellen equivalent each visit; photographs baseline, 6, 12 months, or failure. | Label/scale check: letter score and Snellen equivalent are distinct outputs; no values to compare. | Direct procedural repetition of earlier scale/schedule. Alternative: two measures may legitimately coexist. Human question: was any reported value a letter score or a Snellen line? |
| N097 | Protocol `#page=59` (printed 58): twice-yearly site visits; monthly investigator calls; weekly DCC meetings. | Administrative intervals have no total or study-result denominator. | Direct cadence, not result. Alternative: calendar scheduling may vary. Human question: none absent a claimed monitoring count. |
| N098 | Protocol `#page=60` (printed 59): interim analysis at 1/3 completion; conservative stopping rule unspecified. | Fraction check: 1/3 is a timing fraction, but total completion count/rule is absent. No inferential or total reconciliation possible. | Direct plan; not an observed interim. Alternative: completion may refer to participants rather than records. Human question: what unit defines completion if matched to an interim claim? |
| N099 | Protocol `#page=61` (printed 60): Oregon/Aravind visits every 4–6 months. | Range is internally coherent; no reported count/rate. | Direct administrative plan. Alternative: visit count depends on duration. Human question: none absent a reported total. |
| N100 | Protocol `#page=71` (manual 7): historical incidence >50/100,000 person-years, prevalence about 115/100,000 persons, up to 10% blindness, about 30,000/year. | Unit check separates incidence/person-time, prevalence/persons, proportion, and annual count; no common denominator permits summing/comparing them. | Direct background values, not trial results. Alternative: source populations/eras differ. Human question: none for trial-result QC. |
| N101 | Protocol `#page=72` (manual 8): planned 216 patients; 6-month Phase I then 6 more months for successes; failures switch/follow 6 months. | Population/time check: 216 is planned enrollment, not an observed analysis N; phase clocks are distinct. | Direct plan. Alternative: attrition and phase entry change later denominators. Human question: does a matched result identify planned versus enrolled/randomized population? |
| N102 | Protocol `#page=72` (manual 8): primary comparison is proportion with corticosteroid-sparing control at 6 months. | Measure check: proportion, not count/rate; numerator and denominator are not printed. | Direct estimand definition. Alternative: later SAP may specify ITT coding. Human question: which analysis population is used in any matched result? |
| N103 | Protocol `#page=73` (manual 9): 216 planned, 108 per arm. | Arithmetic: 108 + 108 = 216 exactly (tolerance 0). | Direct values reconcile. Alternative: site blocks need not yield final equal observed arms. Human question: none unless final arm Ns are represented as planned allocation. |
| N104 | Protocol `#page=73` (manual 9): success at 6 months requires control, prednisone 7.5 mg/day, and <=2 topical drops/day. | Composite-definition check: 7.5 mg/day and <=2 drops/day are thresholds with different units; no arithmetic comparison allowed. | Direct definition. Alternative: later wording can clarify inclusive boundaries. Human question: does a matched outcome apply every composite component? |
| N105 | Protocol `#page=73` (manual 9): enumerated secondary domains/outcomes. | Completeness/label check: named outcomes include counts, continuous changes, rate, and QoL but contain no numerical inputs. | Direct endpoint list. Alternative: each has its own population/timepoint. Human question: which named outcome is being matched? |
| N106 | Protocol `#page=74` (manual 10): >=2+ baseline inflammation; two-step reductions (2+ to 0.5+, 3+ to 1+, 4+ to 2+); >=1+ to 0. | Ordinal-scale check: each stated transition decreases exactly two grade steps under the printed half-grade scale; not a percentage or mean difference. | Direct scale definitions. Alternative: different AC/haze scales must not be substituted. Human question: which grading scale applies to any matched reduction? |
| N107 | Protocol `#page=74` (manual 10): timeline dates Dec 2011–Nov 2018; enrolment/follow-up Aug 2013–Apr 2017. | Calendar-span ordering check: all listed periods progress chronologically; table is a planned timeline, not accrued follow-up. | Direct planned dates. Alternative: timeline revisions may change dates. Human question: none absent a contradictory stated actual date. |
| N108 | Protocol `#page=75-77` (manual 11-13): activity within 180 days >=2+; at enrolment >=1+; steroid/injection windows. | Population/threshold check: 180-day historical eligibility and enrolment activity use different thresholds/time anchors, so they are not interchangeable denominators. | Direct definitions. Alternative: qualifying alternative criteria can overlap. Human question: which criterion supplied an enrolled participant’s eligibility? |
| N109 | Protocol `#page=76-77` (manual 12-13): 1 mg/kg or 60 mg/day, whichever less; age <16 excludes; IOP <5 mm Hg >3 months. | Unit/inequality check: mg/kg and mg/day use a minimum rule, not addition; all thresholds have distinct units/time conditions. | Direct definitions. Alternative: patient weight determines dose. Human question: none without individual values. |
| N110 | Protocol `#page=77` (manual 13): WBC <=2500, platelets <=75000, Hb <6.5 g/dL, AST/ALT >2 ULN, creatinine >=2 mg/dL. | Threshold-label check: inequalities and units are printed consistently; values are exclusion definitions, not events. | Direct definitions. Alternative: on-study safety table has different categories. Human question: is a proposed comparison eligibility or on-study safety? |
| N111 | Protocol `#page=78-79` (manual 14-15): equal numbers intended at each site; 5-character ID (site digit + checksum + 001 sequence). | Structure check: 1+1+3 = 5 characters exactly. Equal allocation is intention, not observed subgroup sum. | Direct allocation/identifier rule. Alternative: blocks can leave incomplete final blocks. Human question: none absent a claimed realized site balance. |
| N112 | Protocol `#page=80` (manual 16), Table 2: both-eye control; <=0.5+ cells/haze; 7.5 mg prednisone; <=2 drops; no post-90-day injection/failure. | Composite and unit check: thresholds are distinct conjunctive conditions; no numerator/denominator is reported. | Direct endpoint definition. Alternative: cystoid macular edema alone is explicitly insufficient. Human question: were all Table-2 conditions used in a matched result? |
| N113 | Protocol `#page=80-81` (manual 16-17): 28 days to regain eligibility; repeat tests 1–2 weeks; persistent threshold 28 days becomes serious. | Timing check: 1–2 weeks lies within 28 days; no contradiction. | Direct prospective rule. Alternative: repeat recommendation is not a mandated exact date. Human question: was a specific event assessed under this rule? |
| N114 | Protocol `#page=81` (manual 17), Table 3: non-serious/serious lab bands. | Boundary check: WBC (>1000,<2500) vs <=1000; platelets 20000–75000 vs <20000; Hb >=6.5,<9 vs <6.5; AST/ALT 2–<5 vs >=5; creatinine >=1.5,<2 vs >=2. Adjacent bands do not overlap; labels preserve units. | Direct table. Alternative: eligibility values are a separate pre-entry rule. Human question: which table governs a matched lab record? |
| N115 | Protocol `#page=82-83` (manual 18-19): failures return for 6-month visit; success thresholds repeat. | Population check: dropout, failure, discontinuation are explicitly nonidentical; no observed flow count exists. | Direct flow definition. Alternative: returned visit need not imply primary-analysis inclusion. Human question: what analysis-set rule applies to a matched count? |
| N116 | Protocol `#page=84` (manual 20), Tables 4-5: MTX 7.5 mg BID weekly=15 mg/week, then 12.5 mg BID=25 mg/week; MMF 500 mg BID then 1.5 g BID. | Arithmetic: 7.5×2=15 and 12.5×2=25 mg/week; 1.5 g×2=3 g/day. Reductions are ordered downward. | Direct dosing schedule reconciles. Alternative: BID weekly MTX means two doses on the weekly dosing day. Human question: none absent a conflicting dose label. |
| N117 | Protocol `#page=85-87` (manual 21-23): MTX pill schedules and MMF 1+1 then 3+3 pills. | Arithmetic: 3+3=6 and 5+5=10 MTX pills/week; 1+1=2 and 3+3=6 MMF pills/day. With stated tablet strengths, narrative equals printed doses. | Direct pill/dose reconciliation. Alternative: packaging may include buffer. Human question: none absent a dispensing claim. |
| N118 | Protocol `#page=87` (manual 23): 14-day supply 12 MTX/28 MMF; maintenance 50 MTX/200 monthly MMF. | Arithmetic: introductory MTX 6 pills/week×2=12; MMF 2/day×14=28. Maintenance needs 10×4=40 MTX pills/28 days and 6×30=180 MMF pills; stated 50/200 allow supply buffer. | Direct quantities reconcile; month length/dispensing buffer explains surplus. Human question: are supplies intended exactly 28 or 30 days in a matched record? |
| N119 | Protocol `#page=88-91` (manual 24-27): prednisone 1 mg/kg or 60 mg/day less; 2–4-week taper; 7.5 mg/day hold; drug effect 6–8 weeks. | Unit/schedule check: ranges and minimum-dose rule are internally compatible; no observed exposure denominator. | Direct prospective schedule. Alternative: taper individualized within printed ranges. Human question: none without a patient regimen. |
| N120 | Protocol `#page=90-91` (manual 26-27): 7.5-to-0 taper and topical 6,4,3,2,1,0 drops/day; mild <=1+, severe >=2+. | Ordering check: dose/drop sequence declines monotonically; severity partitions at 1+/2+ without gap. | Direct rule. Alternative: phase-I/II and rescue context matters. Human question: which phase applies to a matched taper result? |
| N121 | Protocol `#page=91` (manual 27): calcium 500 mg TID; vitamin D 400–800 IU daily; one 40-mg periocular or 4-mg intravitreal injection allowed first 90 days. | Arithmetic: 500×3=1500 mg/day calcium. Injection doses have different route/units and are not comparable. | Direct treatment definition. Alternative: allowance is per phase. Human question: was an injection within its 90-day phase window? |
| N122 | Protocol `#page=92-95` (manual 28-31): visit windows baseline through month 12; week 2 +3 days; month 6 -15/+30; Phase-II within 14 days. | Window check: 2 weeks = 14 days; asymmetric month-6 window is not a contradiction. | Direct schedule. Alternative: phase/time origin varies after failure. Human question: which visit date anchors a matched outcome? |
| N123 | Protocol `#page=96` (manual 32): form schedule across Phase I/II and treatment failure. | Schedule/presence check only; parenthesized cells are conditional and no completion numerators are printed. | Direct collection plan. Alternative: form applicable only in indicated phase. Human question: was a missing form applicable? |
| N124 | Protocol `#page=97` (printed 33): baseline up to 14 days; labs 4 weeks/90 days; >=1+ inflammation. | Time/threshold labels are distinct; 14 days is not equated to 4 weeks/90 days. | Direct definition. Alternative: test-specific lab window. Human question: which baseline input/window is at issue? |
| N125 | Protocol `#page=98` (printed 34): CBC differential percentages; labs within 4 weeks versus 90 days. | Unit check: neutrophil/lymphocyte percentages are not absolute counts; two windows are assay-specific. | Direct definition. Alternative: site-limited CD4. Human question: was a percentage incorrectly compared with a count? |
| N126 | Protocol `#page=99` (printed 35): Phase-I month 9/12; Phase-II 6 months; failure and scheduled assessments. | Population/timepoint check: Phase I and II clocks differ; no total/percentage printed. | Direct schedule. Alternative: failure may occur before scheduled measure. Human question: which phase/timepoint is a matched value from? |
| N127 | Protocol `#page=100` (printed 36): Phase-II baseline same day to 2 weeks after Phase-I failure; SAE nonentrant followed 6 months. | Range/order check: zero to 14 days is coherent. | Direct transition rule. Alternative: follow-up does not equal Phase-II analysis entry. Human question: did a matched denominator include nonentrants? |
| N128 | Protocol `#page=102` (printed 38): SF-36/NEI-VFQ-25 all patients; IND-VFQ Indian patients only; baseline/6-month/failure timing. | Population/scale check: India-only IND-VFQ cannot share an all-patient denominator without explicit restriction. | Direct instrument population. Alternative: phase-I extension adds 12-month form. Human question: which instrument population is reported? |
| N129 | Protocol `#page=102` (printed 38): remove contacts 30 minutes; final refinement at 4 m. | Measurement-condition check; no outcome number. | Direct operational rule. Alternative: initial refraction may begin elsewhere. Human question: none absent a measurement-method conflict. |
| N130 | Protocol `#page=103` (printed 39): letter-chart bands, 4 m/1 m threshold, lens increments. | Scale/unit check: 20/200 and 6/60 are paired acuity labels; 4-m/1-m branches are distinct. | Direct chart branch. Alternative: Tumbling-E has its own procedure. Human question: which chart was used? |
| N131 | Protocol `#page=104` (printed 40): high-acuity lens probes/changes. | Increment check: -0.37-D probe triggers -0.25-D lens change; no reported result. | Direct operational definition. Alternative: conditional on at least one-letter improvement. Human question: none without a refraction record. |
| N132 | Protocol `#page=105` (printed 41): five power-to-axis bands; 0.5-D cylinder change needs opposite 0.25-D sphere change. | Spherical-equivalent arithmetic: half of 0.5 D is 0.25 D, opposite sign; exact. | Direct source-visual-confirmed table. Alternative: applies only at cylinder >=1.00 D. Human question: was this branch applicable? |
| N133 | Protocol `#page=106` (printed 42): middle-acuity ±1.00-D sphere/cylinder rule. | Unit/threshold check: lens diopters, not acuity letters; condition is one-letter improvement. | Direct procedure. Alternative: only 20/100–20/200 band. Human question: which acuity band applies? |
| N134 | Protocol `#page=107` (printed 43): identical axis table; 0.25-D per 0.5-D rule. | Repetition check: agrees with N132; a same-rule duplicate, not an independent result. | Direct same chart’s middle-band continuation. Alternative: cross-cylinder magnitude differs by band. Human question: none. |
| N135 | Protocol `#page=108` (printed 44): <20/200 at 1 m; add +0.75 D. | Branch/unit check: 1-m accommodation correction is a lens adjustment, not an acuity score. | Direct definition. Alternative: triggered only after stated 4-m failure. Human question: was trigger met? |
| N136 | Protocol `#page=109` (printed 45): low-acuity axis table and 0.25-D per 0.5-D correction. | Arithmetic repeats N132 exactly under low-acuity branch. | Direct repetition. Alternative: low-band cylinder refinement is ±1.00 D. Human question: none. |
| N137 | Protocol `#page=110` (printed 46): 14 lines; geometric letter sizes/arithmetic logMAR; row 3 0.8 logMAR/45 letters/20/125. | Scale check: labels describe calibrated row, not three interchangeable outcome values. | Direct calibration. Alternative: report may use letters or logMAR. Human question: which scale was analyzed? |
| N138 | Protocol `#page=111` (printed 47): 4 m=157.5 in; 1 m=39 3/8 in; tube decline 5% then 5%. | Conversion check: 4 m×39.37=157.48 in, rounds 157.5; 1 m=39.37 in, rounds 39 3/8. Sequential declines are condition specifications, not 10% asserted total decline. | Direct values reconcile with rounding. Alternative: fixture geometry affects lane length. Human question: none. |
| N139 | Protocol `#page=112` (printed 48): <20 letters at 4 m triggers 1 m; no letters at 1 m triggers low vision; 3/5 count fingers. | Threshold check: this is the letter-chart branch, distinct from N150 Tumbling-E thresholds. 3/5 is a proportion criterion, no patient denominator. | Direct rule. Alternative: chart-specific protocol. Human question: which chart branch applies? |
| N140 | Protocol `#page=113` (printed 49): hand motion 4/5; light 4 presentations; Snellen >=4/5; biostatistician score calculation. | Proportion checks: 4/5 and 4 of 5 are criteria, not observed percentages. Score formula is absent here. | Direct missing-definition observation. Alternative: Tumbling-E formula cannot be assumed. Human question: what formula applies to letter-chart visits? |
| N141 | Protocol `#page=114` (printed 50): Tumbling-E, 30-min removal, 4 m; <20/200 trigger 1 m. | Chart/threshold check: same general branch structure but a distinct instrument. | Direct definition. Alternative: no comparison to letter-chart scoring without chart identity. Human question: which instrument was used at site/visit? |
| N142 | Protocol `#page=115` (printed 51): Tumbling-E trial-lens bands. | Unit and paired Snellen/metric-band check; no reported numerical outcome. | Direct procedure. Alternative: lenses may vary conditional on response. Human question: none. |
| N143 | Protocol `#page=116` (printed 52): same five-band axis table and 0.25-D correction. | Exact arithmetic/repetition check passes as for N132. | Direct source-visual-confirmed definition. Alternative: high-acuity branch only. Human question: none. |
| N144 | Protocol `#page=117` (printed 53): middle-band ±1.00-D procedure. | Conditional/refraction-unit check; no aggregate result. | Direct definition. Alternative: band change allowed after improvement. Human question: none. |
| N145 | Protocol `#page=118` (printed 54): middle-band axis and correction. | Exact repeated 0.25-D per 0.5-D identity passes. | Direct source-visual-confirmed definition. Alternative: chart is Tumbling-E. Human question: none. |
| N146 | Protocol `#page=119` (printed 55): low-band 1-m +0.75 D; ±2.00 sphere. | Unit/branch check, no count or percentage. | Direct procedure. Alternative: trigger requires missing >=2 letters. Human question: none. |
| N147 | Protocol `#page=120` (printed 56): low-band axis rule. | Exact repeated five-band/0.25-per-0.5 identity passes. | Direct source-visual-confirmed definition. Alternative: low-band cross-cylinder magnitude. Human question: none. |
| N148 | Protocol `#page=121` (printed 57): 14 Tumbling-E lines; geometric size/arithmetic logMAR. | Scale check: letter/character score versus logMAR must not be conflated. | Direct definition. Alternative: sites could use letter or E chart. Human question: which score conversion was used? |
| N149 | Protocol `#page=122` (printed 58): calibration values and 4 m/1 m distances. | Conversion and label checks pass as N138; row calibration is not an outcome estimate. | Direct definition. Alternative: dimensional rounding. Human question: none. |
| N150 | Protocol `#page=123` (printed 59): stop <=3; <10 letters at 4 m/1 m; first 6 rows. | Branch check: values differ from N139 because Tumbling-E uses a different stated procedure; no same-measure contradiction. | Direct definition. Alternative: N139 letter-chart threshold. Human question: which chart was used? |
| N151 | Protocol `#page=124` (printed 60): 3/5 count fingers; 4/5 hand motion; score = 4-m letters +30 if >=10 first-line letters; otherwise 1-m letters/low vision conversion. | Formula check: +30 is conditional; not applied to 1-m/low-vision cases. No numeric visit input is supplied. | Direct formula. Alternative: Visual Acuity Calculation Table absent. Human question: what conversion values were used for low vision? |
| N152 | Protocol `#page=125` (printed 61): highest score 100; >=4/5 Snellen; certification 18±2 months, >=2 technicians. | Ceiling/boundary check: score rule does not exceed printed 100 under absent row data; 18±2 describes a 16–20 month window. | Direct definition. Alternative: certification is QA, not participant N. Human question: none. |
| N153 | Protocol `#page=125` (printed 61): cataract grades 1,2,3; halves permitted. | Ordinal-scale check: 1.5 permitted and is not a count or percentage. | Direct definition. Alternative: not interchangeable with inflammation grades. Human question: which grading scale is reported? |
| N154 | Protocol `#page=126` (printed 62): cataract categories and SUN cells 0/<1 through 4+/>50 in 1×1 mm. | Boundary check: SUN intervals are ordered without overlap; >=1+ eligibility maps to >=6 cells, not a Miami/NEI score. | Direct table. Alternative: cell grades are ordinal. Human question: which inflammation component is intended? |
| N155 | Protocol `#page=127` (printed 63): flare/vitreous cells distinct; NEI used for outcomes; Miami separately assessed. | Measure/scale check: no rate/count interchange; NEI and Miami cannot be numerically equated. | Direct distinction. Alternative: media opacity can make grade unreliable. Human question: which haze scale is a matched result on? |
| N156 | Protocol `#page=128` (printed 64): NEI grades 0 to 4+. | Order/label check: NEI 0–4+ has six displayed categories including 0.5+, unlike Miami 0–8. | Direct scale table. Alternative: ordinal labels are not interval values. Human question: none. |
| N157 | Protocol `#page=129`, Miami figure: nine ordered points 0–8. | Count check: inclusive integers 0 through 8 give 9 points exactly. | Direct visual confirmation. Alternative: photographic Miami, not NEI outcome scale. Human question: which scale is reported? |
| N158 | Protocol `#page=129`: >=1+ AC inflammation/haze and/or lesions define activity. | Logical operator check: alternatives define activity; isolated macular edema excluded. | Direct definition. Alternative: eligibility/failure contexts may differ. Human question: which context applies? |
| N159 | Protocol `#page=129-130`: 80% certification; 5 patients; >1-grade discrepancy; 5 consecutive within one level; double zero not counted. | Sequence/count check: five consecutive qualifying patients required; zero-zero exclusion prevents treating all reviewed patients as qualifying. | Direct QA rule. Alternative: calibration is not an outcome result. Human question: none. |
| N160 | Protocol `#page=130`: 20°×20° scan, 49 sections/16 ART; 30°×5°, 7 sections/25 ART. | Unit check: angular dimensions, section count, and frames are different quantities; no invalid total. | Direct acquisition rule. Alternative: per-eye, not per-patient. Human question: what unit underlies a matched thickness value? |
| N161 | Protocol `#page=131`: repeats scans; quality score >=20. | Repeated-value check: scan parameters agree with N160; quality cutoff is device-specific. | Direct repetition. Alternative: cannot compare numerically with Zeiss >=5. Human question: which scanner was used? |
| N162 | Protocol `#page=131`: central subfield thickness recorded for each eye. | Analysis-unit check: eye-level measure is not a patient count; no thickness values printed. | Direct definition. Alternative: later patient-level analysis may model correlated eyes. Human question: what analysis unit is reported? |
| N163 | Protocol `#page=132`: example IDs encode patient/visit/date; clinic ID four letters. | Identifier parsing check: examples are locator strings, not dates/values for analysis. | Direct convention. Alternative: anonymized identifiers. Human question: none. |
| N164 | Protocol `#page=133`: Zeiss Macular Cube 512×218 HD; one cube and one raster per eye. | Unit/product-label check: 512×218 is scan setting, not thickness/rate. | Direct visual confirmation. Alternative: device-specific. Human question: which device generated a matched value? |
| N165 | Protocol `#page=133`: DOB entered 1/1/2000 for anonymization. | Provenance check: fixed date is not participant age/baseline date. | Direct anonymization convention. Alternative: record system requires placeholder. Human question: was any analysis accidentally based on this field? |
| N166 | Protocol `#page=134`: Zeiss signal >=5; at least two OCT operators/site. | Threshold/unit check: signal >=5 is device scale, not comparable to Heidelberg >=20. | Direct visual confirmation. Alternative: operator count is staffing, not sample N. Human question: which quality scale applies? |
| N167 | Protocol `#page=135`: photos baseline/6/12/failure; NEI and Miami used. | Timepoint/scale check: both scales stated, no observed grade; distinguish photography schedule from participant count. | Direct definition. Alternative: failure can replace scheduled visit. Human question: clinical versus photographic grade? |
| N168 | Protocol `#page=135`: CD4 only UCSF/AEH/KKESH at baseline, 3,6,12 months; baseline labs up to four weeks. | Population check: CD4 denominator is site-limited, not all randomized; timepoints ordered. | Direct definition. Alternative: missing CD4 elsewhere is structural. Human question: what site-population denominator is claimed? |
| N169 | Protocol `#page=135`: AST/ALT twice ULN, one month normalization, otherwise failure/follow to 6 months. | Threshold/time check: no event numerator; one-month allowance and 6-month follow-up are different clocks. | Direct rule. Alternative: laboratory versus nonlab SAE. Human question: which rule applies? |
| N170 | Protocol `#page=136`: IOP >24 mm Hg; AST/ALT >=2,<5 ULN vs >=5; creatinine >=1.5,<2 vs >=2; WBC <2.5. | Boundary check: AST/ALT and creatinine bands partition at 5 and 2, respectively; units retained. IOP >24 differs from any >=24 definition. | Direct visual confirmation. Alternative: separate source versions may change wording; no observed AE comparator here. Human question: which version/threshold governed reported AEs? |
| N171 | Protocol `#page=136`: AEs each visit; SAE report within 24 hours. | Cadence/time check, no AE count/rate. | Direct definition. Alternative: reporting deadline not event-time denominator. Human question: none. |
| N172 | Protocol `#page=137`: SAE-related failure judgment; 6-month follow-up; death within 24 h; arm reports every 6 months. | Population/rate check: arm-specific reports do not state counts or person-time. | Direct rule. Alternative: causality judgment conditions failure. Human question: none absent an AE table. |
| N173 | Protocol `#page=138`: cross-check 24 h; send 10 days; double entry; 5 error classes. | Count check: five named classes are enumerated; procedural targets are not observed missingness. | Direct data-QA plan. Alternative: delay target versus completion. Human question: none. |
| N174 | Protocol `#page=139`: one column/variable, one row/observation; `NA`; logMAR unit required. | Unit/missingness check: `NA` is a missing-value code, not zero; logMAR must retain label. | Direct data definition. Alternative: row may be eye or patient depending dataset. Human question: what row unit and missingness handling apply? |
| N175 | Protocol `#page=139`: 3 error categories; >30-day delay triggers response. | Count/range check: three categories are stated; delay threshold is not missingness percentage. | Direct QA plan. Alternative: categories can overlap in a record. Human question: none. |
| N176 | Protocol `#page=140`: weekly screened/enrolled/ineligible/follow-up; monthly overall/site enrollment. | No printed numerator/denominator; site subtotal cannot be tested. | Direct monitoring plan. Alternative: report period determines totals. Human question: which period/site denominator is matched? |
| N177 | Protocol `#page=141`: missed doses/pill counts every follow-up; audits twice yearly. | Measure check: pill count/adherence is not an AE rate or treatment exposure duration without values. | Direct plan. Alternative: self-report and pill counts can differ. Human question: none. |
| N178 | Protocol `#page=142`: letter count and Snellen each visit; both-eye OCT. | Scale/unit check: letters and Snellen are distinct; both-eye imaging does not yield two independent participants. | Direct procedure. Alternative: eye-level analysis requires correlation handling. Human question: which scale/unit is reported? |
| N179 | Protocol `#page=143`: both-eye photos baseline/6/12/failure. | Unit/timepoint check: two eyes per participant and failure alternative prevent direct summing as patient visits. | Direct schedule. Alternative: image availability differs from grade usability. Human question: what denominator is used? |
| N180 | Protocol `#page=145`: site visits every 4–6 months. | Range definition only; no count. | Direct administrative plan. Alternative: duration controls realized count. Human question: none. |
| N181 | Protocol `#page=148`: Hb exclusion <=10 changed to <=9; week 2 ±3 days; labs months 7,8,10,11; timeline -3 months. | Revision check: explicitly marked changed values belong to successive protocol versions, not same-version conflict. 2×3+1=7-day week-2 window. | Direct revision history. Alternative: final-version date must be matched. Human question: which protocol version governed the reported population? |
| N182 | Protocol `#page=149`: injection past 4 weeks; taper 14 days to 4 weeks; labs 14 days to 4 weeks; infection 60 to 90 days. | Revision check: old/new windows are explicit changes, not simultaneous eligibility thresholds. | Direct revision history. Alternative: enrollment date determines version. Human question: which version applies to a matched participant? |
| N183 | Protocol `#page=150`: activity window 90 to 180 days; >=2+; >=10 mg/day >=90 days; injection 4 weeks–180 days. | Revision and inequality check: 90/180-day values are version changes; thresholds have distinct eligibility alternatives. | Direct revision history. Alternative: overlapping qualification routes. Human question: which version/route is used? |
| N184 | Protocol `#page=151`: 7.5 mg/day; VKH >=4 weeks; exam/VA <=7 days; injection first 90 days; lab windows revised. | Unit/timepoint check: 7.5 mg/day dose and time windows are nonadditive definitions. | Direct revision history. Alternative: phase-specific injection allowance. Human question: which revision controls the outcome definition? |
| N185 | Protocol `#page=152`: Month 6 removed from months-6–12 table; prior therapy <12 months; forms due 10 not 7 days. | Revision check: removed/changed schedule entries are historical changes, not two concurrent values. | Direct revision history. Alternative: final schedule may be elsewhere. Human question: which protocol version is authoritative? |
| N186 | Protocol `#page=153`: non-serious lab threshold >=28 days becomes serious/failure; CD4 at three sites, baseline/3/6/12; Phase II normally within 2 weeks. | Timing check: 2 weeks=14 days; threshold duration is separate from visit schedule. Site-limited CD4 denominator noted. | Direct revision history. Alternative: exceptional Phase-II permission outside window. Human question: which exception/version applies? |
| N187 | SAP `joi190092supp3_prod.pdf#page=5`: Phase III planned comparison of MMF vs MTX. | Contrast-label check: two treatment arms; no sample size/effect result on this page. | Direct plan. Alternative: later documents may abbreviate drugs. Human question: is any matched result first-line rather than rescue? |
| N188 | SAP `joi190092supp3_prod.pdf#page=6`: Aim 1 difference in 6-month treatment-success proportion, ITT. | Measure/population check: difference in proportions requires matched treatment-specific ITT denominators; neither numerator nor denominator is printed here. | Direct estimand. Alternative: protocol wording may use success proportion rather than difference. Human question: what exact ITT denominator and missingness convention support a matched result? |

## Candidate drafts

**Count: 0.** No distinct candidate draft is emitted from N095–N188. All checked numbers either reconcile under their printed rule, are protocol/SAP planning definitions without a matched observed-result comparator, or are explicitly version/chart/phase-specific alternatives. There is consequently no candidate-specific source comparison, calculation, or adjudication question to record in this shard.

## Limitations

- This exact slice has no accrued numerical result table, arm-level observed total, or paired cross-document result occurrence in scope; it cannot establish a planned-versus-observed discrepancy without a population/timepoint/model-matched result source.
- Low-vision conversion values referenced by the protocol’s Visual Acuity Calculation Table are not on these pages; no conversion was assumed.
- Threshold changes in revision history were retained as version-specific alternatives. The final protocol version applicable to any individual reported result would need confirmation before comparison.

# Numeric consistency review: N189--N282

## Scope, evidence, and checking rule

This shard covers exactly the 94 inventory relationships N189--N282.  I used the inventory as the scope crosswalk and the named extraction shards as locators, then rechecked the two proposed discrepancies against the direct supplied PDF.  The SAP records are prospective definitions, assumptions, and planning quantities rather than observed results; a planned value was not treated as inconsistent merely because the supplied package does not contain an observed matched result.  For displayed count/percentage cells, the rule was `100 x count / stated column N`, rounded to one decimal by ordinary half-up/nearest one-decimal display (tolerance 0.05 percentage points, subject to the displayed rounding convention).  For whole-percent enrollment values the tolerance is 0.5 percentage points.  For verbal approximations (`about`, `approximately`, `~`) I did not manufacture a numeric tolerance or candidate without a conflicting same-definition value.

Direct sources: `joi190092supp3_prod.pdf` (SAP; physical PDF pages cited below) and `joi190092supp1_prod.pdf` (Supplementary Results; physical PDF pages cited below).  The direct recheck used `pdftotext -layout` on Supplementary Results pp. 5, 14--15 and visual confirmation of p. 15.  Reusable evidence locators were `parts/support_sap_pp001_032.md`, `parts/support_sap_pp033_064.md`, `parts/support_sap_pp065_083.md`, and `parts/support_supp_results_pp001_016.md`.

## Complete relationship register

`PASS` means that the applicable source-grounded arithmetic, total/subgroup, denominator/percentage, population, measure/label/scale/unit, rate-versus-count, duplicate-value, and direct-source checks found no candidate draft. `NOT APPLICABLE` means the mapped relationship is a single planned definition/administrative convention with no displayed arithmetic or matched same-definition observed comparator in this assigned scope; this is not a scientific-coverage omission.

| N ID | Direct source location and printed relationship checked | Applied check and reproducible result | Outcome |
|---|---|---|---|
| N189 | SAP p. 6, Phase I continuation, months 9/12 | Schedule/phase and removal rule are internally singular; no count/denominator comparator. | NOT APPLICABLE |
| N190 | SAP p. 7, 5-month success sustained >=28 days to month 6 | Time threshold and endpoint labels agree within the definition. | PASS |
| N191 | SAP p. 7, secondary outcome/time inventory | Endpoint names are distinct; no repeated-value or unit conflict is displayed. | PASS |
| N192 | SAP p. 7, 12-month steroid-discontinuation control | Measure is explicitly a probability, not a count/rate. | PASS |
| N193 | SAP p. 8, Aim 2 rescue success fraction at 6 months | Population (initial-treatment failures), time, and fraction label are aligned. | PASS |
| N194 | SAP p. 8, Aim 2 every-4-week follow-up to 6 months | Visit cadence and endpoint are a definition; no arithmetic comparator. | NOT APPLICABLE |
| N195 | SAP p. 8, four sites/two treatment arms | Site count and two-arm labels are distinct dimensions; no total is asserted. | PASS |
| N196 | SAP p. 9, blocks 4 with probability 2/3 and 6 with 1/3 | `2/3 + 1/3 = 1`; probabilities are complete and site-stratified. | PASS |
| N197 | SAP p. 10, five-character ID; sites 1--4; example 4J101 | ID specification is internally consistent: one digit + one letter + three digits = five. | PASS |
| N198 | SAP pp. 11--12, eye classes A--E | Five named categories agree with A--E enumeration. | PASS |
| N199 | SAP p. 12, patient randomization and 25 bilateral types | `5 x 5 = 25`; patient/eye units are expressly separated. | PASS |
| N200 | SAP p. 12, 5x5 eligibility table | Rule is at least one class-C eye; table and stated patient criterion agree. | PASS |
| N201 | SAP p. 12, month-6 eye-scoring table | Baseline E=NA and A--D rules are displayed as definitions, not totals. | PASS |
| N202 | SAP p. 13, both-eye patient success and visit schedule | Patient outcome is expressly distinguished from eye observations. | PASS |
| N203 | SAP p. 13, worst observed value for unavailable field | Missing-field handling and eye-level secondary population are explicit; no numeric contradiction. | PASS |
| N204 | SAP p. 14, unassessable/LOCF/failure rule at visits 6/12 | Baseline versus follow-up assessment rules use compatible time labels. | PASS |
| N205 | SAP pp. 14--15, principal-variable inventory | BSCVA is two observations/patient; other outcomes retain their stated patient/eye units. | PASS |
| N206 | SAP p. 15, location coding 0/1 and outcome window -2 to +4 weeks | Two codes and window endpoints are explicit; no unit/scale conflict. | PASS |
| N207 | SAP p. 16, `X1i=0/1`, `Yi=1/0`, missingness and AE discontinuation | Treatment, outcome, and missing/failure coding are differentiated, not conflated. | PASS |
| N208 | SAP pp. 16--17, mutually exclusive site indicators and site-1 baseline | Exactly one site indicator equals 1 per patient; stated reference is compatible. | PASS |
| N209 | SAP p. 17, anatomy subgroups and stratum RRs | Three-level enrollment and two-level history variables are separately named. | PASS |
| N210 | SAP pp. 18--20, secondary-outcome definitions | Each measure retains an outcome/time/unit label; no displayed duplicate expected to differ. | PASS |
| N211 | SAP p. 19, BSCVA eligible eyes, LOCF, logMAR 2.0 fallback | Eye-level population and 2.0 fallback are explicit; no incompatible denominator. | PASS |
| N212 | SAP p. 20, edema fraction and thickness adjusted for baseline | Fraction and micron thickness are separate measures; no rate/count conflation. | PASS |
| N213 | SAP p. 21, rescue success proportions with 95% CI | Contrast paths and success-proportion measure are separately stated. | PASS |
| N214 | SAP p. 22, planned diagnostic/sensitivity methods | Methods are alternatives, not repeated estimates. | NOT APPLICABLE |
| N215 | SAP pp. 22--23, total 216; 108/group; pc=.4; pi=.6; 20 points; 10% loss | `108 + 108 = 216`; `.6 - .4 = .20`; `(.6+.4)/2=.5`. Power is explicitly approximate/model-based. | PASS |
| N216 | SAP p. 23, 80%/90% power sensitivity table | In every row, printed Drug-B rate equals Drug-A rate plus printed effect after whole-percent rounding (e.g., 20+18=38; 60+19=79). | PASS |
| N217 | SAP p. 24, >80% power/25 points; 5% additional loss; ~78%/20 points | `10% + 5%` are sequential planned loss assumptions; values are labelled approximate. | PASS |
| N218 | SAP p. 24, 108/group; 10% loss; 2.47 months; median 3.5; alpha .05 | Time unit is months throughout; `lambda_C=log(2)/3.5` carries reciprocal-month scale. | PASS |
| N219 | SAP pp. 24--25, BSCVA SD 6.5; 108/group; 2.63 letters; QOL SD 8.4, r=.6, corrected SD 6.72 | `8.4 x sqrt(1-.6^2)=8.4 x .8=6.72`; BSCVA is letters and QOL points, not merged. | PASS |
| N220 | SAP p. 25, discontinuation 13/5% versus 4/5%; edema 19 vs 38%; thickness 65 microns | `19 x 2 = 38`; reason-specific discontinuation rates and micron thickness retain distinct labels. | PASS |
| N221 | SAP pp. 25--27, Aim-2 availability N0=108, r1=.9, r2=.95; 58.3/55.4 and 38.9/36.9 | Enrollment: `108*.9*(1-.4)=58.32` and `108*.9*(1-.6)=38.88`; completion times `.95` = `55.404`, `36.936`; displayed one-decimal values and floor text 58/38 reconcile. | PASS |
| N222 | SAP pp. 26--27, rescue power scenarios | Each row preserves its stated sample sizes, success paths, and approximate power; reversed .15/.42 row is a distinct contrast, not a duplicate. | PASS |
| N223 | SAP pp. 28--29, four missing-data analyses; 10 regression and 10 hot-deck imputations; visits 1:6 | Four methods and ten-replication counts are explicit; complete-case primary label is not a numerical contradiction. | PASS |
| N224 | SAP p. 29, ~three-fourths Aravind; alpha .05 | Approximate site share and alpha are different measures; no conflicting total. | PASS |
| N225 | SAP p. 30, 7--8/month for 2.5 years; 25% lower accrual; 3y3m; looks 1/3,2/3 | `2.5 years / .75 = 3.33 years` = 3 years 4 months approximately, compatible with the stated planning duration rounding. | PASS |
| N226 | SAP p. 30, analysis timing and R >=2.12 | Phase/time labels are distinct; version threshold is not a numeric result. | NOT APPLICABLE |
| N227 | SAP p. 31, analysis populations and per-protocol <50% receipt | Screening/safety/ITT/per-protocol populations are definitions; no reported count claimed. | PASS |
| N228 | SAP p. 31, deviation counts/percentages and discontinuation test | Count/percentage description is distinct from Fisher/chi-square test labels. | PASS |
| N229 | SAP p. 32, `NA`, coding, units | Missing-value label and examples retain unambiguous logMAR/thickness units. | PASS |
| N230 | SAP p. 32, monthly monitoring and final disposition frequencies | Frequency/count categories are planned outputs without displayed totals. | NOT APPLICABLE |
| N231 | SAP pp. 33--34, interim looks ~1/3 and ~2/3, subject 72 | Two looks and information fractions agree; "about" limits exact calendar arithmetic. | PASS |
| N232 | SAP pp. 35--36, pooled AE proportions versus recurrent-event rates | Directly distinguishes subject proportion from all/recurrent-event rate and randomized-arm exposure. | PASS |
| N233 | SAP p. 37, `NA` = not available | Missing-value label is singular and does not imply zero or a count. | PASS |
| N234 | SAP pp. 45--46, ITT 6-month success and Phase I months 6--12 | Population, endpoint, and phase/time labels are aligned. | PASS |
| N235 | SAP pp. 47--48, secondary endpoint inventory | Time-to-event, proportion, rate, scales, and discontinuation categories are distinct. | PASS |
| N236 | SAP p. 48, rescue failure/switch/4-week visits/6-month success | Failure population and rescue time origin are explicit. | PASS |
| N237 | SAP pp. 49--50, nine sites; blocks 4 at 2/3 and 6 at 1/3 | `2/3+1/3=1`; text correctly warns block distribution differs from person distribution. | PASS |
| N238 | SAP p. 50, site 1--9 plus checksum and 001 | One site digit + one letter + three digits = five characters. | PASS |
| N239 | SAP pp. 52--54, patient assignment/primary analysis; 5x5 tables | `5 x 5=25` table structure; patient and eye analysis units are explicitly separated. | PASS |
| N240 | SAP pp. 53--54, unavailable-field rule and schedules | Months 9/12 apply to Phase I; 6-month schedule applies to both phases as stated. | PASS |
| N241 | SAP pp. 54--55, baseline counts/percentages and outcome inventory | Two BSCVA observations/patient is marked eye-level; patient outcome counts are not conflated. | PASS |
| N242 | SAP p. 56, outcome windows -2 to +4 weeks | Same window width is used consistently for named 6- and 12-month endpoints. | PASS |
| N243 | SAP p. 56, 0/1 treatment and outcome coding | Reference/treatment and success/failure/missing coding are explicit and nonconflicting. | PASS |
| N244 | SAP pp. 57--58, anatomy/country/site coding | Two-level history, three-level enrollment, and country/site indicators retain distinct scales. | PASS |
| N245 | SAP pp. 58--60, endpoint definitions | Patient fraction, per-eye BSCVA, ordinal haze, and four-category discontinuation remain correctly labelled. | PASS |
| N246 | SAP p. 60, 10% non-inferiority margin and lower 95% CI wording | Direct observation: wording lacks contrast orientation; no matched reported value permits arithmetic contradiction. Human question only if used for a result: what signed contrast does the lower limit represent? | NOT APPLICABLE |
| N247 | SAP pp. 61--62, rescue proportions/95% CIs and LTFU sensitivity | Rescue paths and comparison population are distinguished. | PASS |
| N248 | SAP pp. 63--64, 2N formula; pc=.4, pi=.6, alpha=.05, 80%, 108/group/216 | Same reconciliation as N215: `2N=216`, `.6-.4=.2`, `pbar=.5`; 10% loss is a stated planning assumption. | PASS |
| N249 | SAP p. 64, sensitivity table and >80%/25-point subgroup plan | Each displayed Drug-B rate equals Drug-A plus effect at shown precision; subgroup statement is approximate. | PASS |
| N250 | SAP p. 65, additional 5% loss plus 10%; ~78% for 20% | Sequential loss periods and 12-month endpoint are explicit; approximate power needs no forced exact reconstruction. | PASS |
| N251 | SAP p. 65, 6-month censoring, median 3.5 months, 108/group, 2.47 months | All time quantities use months; treatment direction is declared in source. | PASS |
| N252 | SAP p. 65, BSCVA SD 6.5 letters and 2.63-letter difference | BSCVA retains its letters scale and direction; no QOL scale is combined with it. | PASS |
| N253 | SAP p. 65, QOL SD 8.4, r=.6, corrected SD 6.72, 2.57 points | `8.4 x sqrt(1-.6^2)=6.72`; QOL points and 0--100 scale are explicit. | PASS |
| N254 | SAP p. 65, discontinuation reason-specific rates 13/5 vs 4/5 | Tolerability and safety proportions are not added or mislabeled as a recurrent-event rate. | PASS |
| N255 | SAP p. 66, 61%; edema 38% and 19/38%; thickness 65/160/100 microns | `19 x 2=38`; proportion and micron measures are distinct. | PASS |
| N256 | SAP p. 66, rescue success probabilities/95% CI by failure reason | Probability, CI, initial drug, and reason stratum are all named. | PASS |
| N257 | SAP p. 66, availability formula N0=108, r1=.9, sj=.6/.4, r2=.95 | Formula has the correct complement `(1-sj)` for initial failure and labels group paths. | PASS |
| N258 | SAP p. 67, B/A 58.3/55.4 and A/B 38.9/36.9; floor 58/38 | `108*.9*.6=58.32`, then `*.95=55.404`; `108*.9*.4=38.88`, then `*.95=36.936`; one-decimal table and floor text reconcile. | PASS |
| N259 | SAP p. 67, p0=.15, p1=.42, power .87; 17-point ~80% statement | `.42-.15=.27`; separate 17-point statement is explicitly a different scenario, not a contradictory repeat. | PASS |
| N260 | SAP pp. 67--68, seven rescue-power sensitivity rows | Each row retains stated orientation; power is approximate/model-based and no two same-input rows disagree. | PASS |
| N261 | SAP p. 68, four missing-data analyses and complete-case primary | Endpoint is six-month success in each alternative; no denominator/count is printed. | PASS |
| N262 | SAP p. 68, 10 MI and 10 hot-deck replications; visit 1:6 | Replication counts and repeated-measure index are internally consistent. | PASS |
| N263 | SAP p. 70, injection 90 days after enrollment | 90-day sensitivity threshold and failure/success classification are explicit. | PASS |
| N264 | SAP p. 70, ~three-fourths; alpha .05; 7--8/month; 2.5y/3y3m; 1/3,2/3 looks | Mixed measures retain their units; calendar statement is approximate planning, not an exact total. | PASS |
| N265 | SAP p. 70, final-analysis timing and <50% per-protocol criterion | Populations, phases, and adherence threshold are stated without a reported count conflict. | PASS |
| N266 | SAP p. 71, counts/percentages and literal "2 N Fisher's exact test" | The text is a test-label wording, not a reported numerical result. No inferred correction/candidate was made. | NOT APPLICABLE |
| N267 | SAP p. 72, rectangular data/`NA`/units/monthly monitoring | Columns/rows and missing/unit conventions are not conflicting values. | PASS |
| N268 | SAP p. 73, DSMC 5--7 people, annual, 1/3/2/3, 6 months after 72nd | Ranges and approximate information fractions are labelled as such; no total/denominator mismatch. | PASS |
| N269 | SAP p. 74, t=1/3 -> 15; t=2/3 -> 30; gamma -5.623626; alpha .001/.0075 | With `alpha=.05`, `a*(t)=.05(1-exp(-gamma*t))/(1-exp(-gamma))` gives .000997 at 1/3 and .00750 at 2/3; matches stated approximate values. | PASS |
| N270 | SAP p. 75, SAE report within 24 hours; total/serious event outputs | Hours is a reporting deadline, while total/serious are count categories; no rate/count mix-up. | PASS |
| N271 | SAP p. 76, four pooled AE subject proportions and `NA` convention | Four categories are subject proportions, not recurrent-event rates; `NA` means unavailable. | PASS |
| N272 | SAP p. 79, randomization seed at least eight digits | Administrative threshold; no result count or comparator. | NOT APPLICABLE |
| N273 | SAP p. 80, revisions and nine recruiting sites | Nine-site statement is a revision definition; no matched observed total is in this relationship. | NOT APPLICABLE |
| N274 | SAP p. 81, REDCap dates 18/17 January 2017 | Chronology is internally ordered: 17 January precedes 18 January. | PASS |
| N275 | Supplementary Results p. 8, nine center counts totaling 216 and whole percentages | `65+36+35+34+21+11+9+3+2=216`; all nine `count/216` values round to printed whole percentages and sum to 100% after rounding. | PASS |
| N276 | Supplementary Results p. 10, eTable 4, N=107/108, 20 AE cells | Every printed cell satisfies `count/N x100` to one decimal (e.g., 9/107=8.4%, 19/108=17.6%); event rows are nonexclusive, so row sums are not expected. | PASS |
| N277 | Supplementary Results p. 11, eTable 5, N=107/108, 20 AE cells | All 20 count/percentage cells reconcile to one decimal; 5/107=4.7% and 5/108=4.6% correctly differ by denominator. | PASS |
| N278 | Supplementary Results p. 12, eTable 6, N=107/108, 52 AE cells | All 52 cells reconcile to one decimal; displayed 0 (0.0) cells are coherent count/percentage pairs. | PASS |
| N279 | Supplementary Results p. 14, eTable 8, N=62/56, 48 AE cells | All 48 cells reconcile to one decimal. A label comparison is separately recorded as Candidate Draft 2 below. | PASS except Candidate Draft 2 |
| N280 | Supplementary Results pp. 15--16, eTable 9, N=29/20, 46 AE cells | All cells except Mycophenolate serious-systemic diarrhea reconcile to one decimal; that direct-source mismatch is Candidate Draft 1 below. | Candidate Draft 1 |
| N281 | Supplementary Results p. 15, eTable 9 serious diarrhea, MMF N=20, `1 (3.4)` | Direct recheck: `1/20 x100=5.0%`, not 3.4%; see Candidate Draft 1. | Candidate Draft 1 |
| N282 | Supplementary Results pp. 5 and 14, eTable 1 definition versus eTable 8 serious-ocular row | Direct recheck: serious ocular hypertension requires surgery, while `>24 mm Hg` is non-serious; see Candidate Draft 2. | Candidate Draft 2 |

## Candidate Draft 1 — eTable 9 MMF serious-diarrhea percentage

- **Category:** Denominator, proportion, or total inconsistency.
- **Exact supplied-source locations:** `joi190092supp1_prod.pdf#page=15`, eTable 9, Mycophenolate Mofetil column header `(N=20)`, column subtitle `Number of Patients Reporting at Least One Event (%)`, Serious Systemic row `Diarrhea`.
- **Printed inputs:** the direct PDF prints `1 (3.4)` in that cell. The same table prints `1 (5.0)` for the MMF low-hemoglobin cell, and its methotrexate N=29 column prints 1 (3.4) in several cells; these are internal rounding comparators, not substitute denominators.
- **Rule, calculation, and tolerance:** expected percent is `100 x 1 / 20 = 5.0%` to one decimal. Under the stated one-decimal tolerance (0.05 percentage points), a printed 3.4% corresponds to a denominator about 29.4 and cannot be a rounded 1/20 percentage. The difference is 1.6 percentage points.
- **Direct observation versus inference:** Direct observation is the N=20 header and printed `1 (3.4)`. The inference is that the displayed percentage does not reconcile if the common column denominator applies. It does not establish the underlying event count, an alternative risk set, or a correction.
- **Source-grounded alternatives:** an unprinted event-specific denominator near 29, an erroneous header, a transposed/copy-forward percentage from the N=29 column, or a typesetting error could explain the mismatch. The table supplies no alternative denominator or exception note.
- **Quality-control relevance:** A count/percentage mismatch can be extracted incorrectly as a risk/proportion in downstream evidence tables; the scope of that risk is limited to the reported table cell.
- **Exact human question:** Does the MMF serious-diarrhea cell use an unprinted denominator or denominator definition, or should the printed percentage for 1 event in the N=20 column be 5.0%?

## Candidate Draft 2 — eTable 8 serious-ocular hypertension label

- **Category:** Measure, label, or scale inconsistency.
- **Exact supplied-source locations:** `joi190092supp1_prod.pdf#page=5`, eTable 1, Ocular Hypertension row; and `joi190092supp1_prod.pdf#page=14`, eTable 8, Serious Ocular row `Ocular hypertension >24mm Hg` (methotrexate `1 (1.6)`, mycophenolate `0 (0.0)`).
- **Printed inputs:** eTable 1 defines non-serious ocular hypertension as `>= 24 mm Hg` and serious ocular hypertension as `Surgery required (laser or incisional)`. eTable 8 places `Ocular hypertension >24mm Hg` under `Serious Ocular`. Its footnote points to “eFigure 2,” not eTable 1; eTable 1 is a separate supplied comparator.
- **Rule and tolerance:** The eTable 8 severity label should meet the eTable 1 serious criterion when the footnote adopts that definition. A pressure threshold alone matches the non-serious criterion; the distinction is categorical, so no numeric rounding tolerance applies.
- **Direct observation versus inference:** Direct observations are the two printed definitions/labels and eTable 8 placement. The inference is that the serious-section row label lacks the surgery-required condition and therefore does not reconcile with the referenced criterion. This does not establish whether the event was surgery-required.
- **Source-grounded alternatives:** The eTable 8 row may abbreviate a surgery-required event, the eTable 1 definition may have been revised for the continuing-after-success cohort, or the row may carry the non-serious pressure label in error. No cohort-specific definition appears; p. 14 footnote a points to “eFigure 2,” whose content is not present in the supplied supplement text.
- **Quality-control relevance:** Severity labels define which events populate serious-AE counts/proportions. A label/definition mismatch can alter how a reader classifies the displayed event, without establishing any clinical or trial-conclusion consequence.
- **Exact human question:** Was the eTable 8 serious-ocular event surgery-required and incompletely labelled, did this cohort use a different seriousness definition, or was `Ocular hypertension >24mm Hg` placed under the wrong severity heading?

## Limitations

The SAP relationships are planning/design records, so the supplied SAP pages generally contain no observed numerical result from which to compute a new cross-document inconsistency.  Model-based power statements are marked approximate and were only checked for displayed input identity, arithmetic that the source itself makes reproducible, units, and measure labels; no unreported variance, sidedness, or implementation detail was assumed.  Supplementary Results eTables contain no workbook, raw data, person-time, CIs, estimates, or cell-specific alternate denominators beyond those printed.
