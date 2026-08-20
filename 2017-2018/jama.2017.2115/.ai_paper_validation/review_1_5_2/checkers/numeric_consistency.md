# Numeric consistency lane

## Scope, sources, and decision rule

This lane independently checked all 69 canonical relationships, N001--N069, in `relationships/numeric_relationship_inventory.md`. Checks used only the supplied PDFs and the fresh native/layout/OCR/rendered assets under `preprocessing/`, with direct-PDF page locations below. No prior audit output was consulted. A relationship is retained as a non-candidate where its printed values reconcile within stated precision, where population/time/model distinctions explain a difference, or where insufficient inputs prevent a numeric calculation. Planning-document values (DOC-002) were not equated to final-trial values (DOC-001) without an identical population, time, and estimand.

Arithmetic tolerance: exact for displayed integer sums; for a displayed percentage rounded to one decimal, +/-0.05 percentage point, to two decimals +/-0.005 percentage point; and for differences rounded to one decimal or two decimals, +/-0.05 or +/-0.005 in the displayed unit. Confidence intervals, Kaplan--Meier estimates, Cox models, power, and graphical coordinates were checked for internal compatibility only unless their underlying inputs were printed.

## Complete relationship check register

| IDs checked | Completion and checks applied | Result |
|---|---|---|
| N001--N003 | Randomized-arm sum: 1156 + 1147 = 2303. Completion and 12-month biomarker values retained separately from baseline/design quantities; units and time points are explicit. | Checked; no candidate. |
| N004--N008 | 45 + 64 = 109; 45/1156 = 3.893% and 64/1147 = 5.580%; placebo minus treatment = 1.687 percentage points, agreeing with 1.69% within rounding. The KM estimates and Cox HR are distinct estimands/analysis populations, not denominator errors. Safety counts are later reconciled in N040. | Checked; no candidate. |
| N009--N012 | Eligibility, counties, block size, dose (3 x 500 mg = 1500 mg/d), visit cadence, first-event rule, and ascertainment labels are internally coherent. | Checked; no candidate. |
| N013--N016 | Prior-study 20/288 = 6.94% and 13/446 = 2.91%, agreeing with 6.9% and 2.9%; 2.9/6.9 is approximately 0.42, compatible with “about 40%.” Annual figures are planning-rate statements and are not labeled as simple four-year proportion/4 calculations. Power scenarios, truncation, and post-hoc population/model labels contain no printed contradiction. | Checked; no candidate. |
| N017--N020 | Figure 1: 791 = 60+186+200+96+239+10; 2843+2303 = 5146. Treatment partial-withdrawal components 15+7+19+7+25 = 73 and placebo 9+9+10+6+26 = 60. Primary-analysis counts equal assigned minus no-follow-up: 1156-54 = 1102; 1147-52 = 1095. 2064/2303 = 89.62%, and 89.0%/90.2% group completion values are compatible with 0.012 placebo-minus-treatment difference. | Checked; no candidate. |
| N021--N024 | Table 1 denominators/percentages checked. Race-category counts sum to each assigned group: 1149+4+3 = 1156 and 1142+4+1 = 1147; Hispanic is separately labeled ethnicity and need not add to race. Surgical-menopause and oophorectomy rows are not mutually exclusive categories. Continuous-variable units and BMI scale are consistently labeled. | Checked; no candidate. |
| N025--N027, N030 | Table 2 differences reconcile: 43.9-31.6 = 12.3; 44.3-31.7 = 12.6; 45.1-32.4 = 12.7; 42.5-30.9 = 11.6; 43.6-31.6 = 12.0. Narrative 36-month values equal Table 2. The baseline placebo N=1146 is explicitly footnoted/unavailable rather than a population contradiction. | Checked; no candidate. |
| N028 | Vitamin-D row: 740-869 = -129 IU/d, compatible with displayed model-based -128.1. Calcium difference is 500-512 = -12.0. The displayed placebo calcium denominator is separately assessed as NCAND-001 below. | Checked; one candidate proposal. |
| N029 | 127.2-126.8 = 0.4 and 680.2-672.1 = 8.1. The conversion factor is unit-explicit and no incompatible converted value is printed. A missing typographic “to” in one CI separator is not a numeric contradiction. | Checked; no candidate. |
| N031--N035 | Figure 2 initial risk sets equal primary-analysis counts (1102/1095), and subsequent decreases are compatible with time-to-event censoring. Breast totals are reconciled with Table 3 in N036. 99+10 = 109 first primaries; second primaries are expressly excluded. Adherence differences (75.4-76.6 = -1.2; 57.7-59.4 = -1.7) are compatible with more precise displayed -1.17 and -1.7. | Checked; no candidate. |
| N036--N038 | Every Table 3 row/period/group total was checked. In particular total cancers: year 1, 11+12 = 23; years 2--4, 34+52 = 86; years 1--4, 45+64 = 109; and each year-1-plus-years-2--4 total equals its years-1--4 cell. Site sums reproduce group totals: treatment 45 and placebo 64, with “other” footnote sites supplying the residual category. | Checked; no candidate. |
| N039--N041 | 304/2303 = 13.20% and 474/2303 = 20.58%, compatible with displayed 13.2%/20.6%; group percentages/differences are compatible with integer group counts at their shown precision. Calculi: 16/1156 = 1.38%, 10/1147 = 0.87%, difference 0.51 points. Post-hoc denominators are 1156-84 = 1072 and 1147-78 = 1069; 34/1072 = 3.17%, 52/1069 = 4.86%, difference 1.69 points. | Checked; no candidate. |
| N042, N067--N069 | The supplied linear coefficient gives exp[-0.017 x (55-30)] = exp(-0.425) = 0.654, consistent with HR 0.65 for the labeled 30--55-ng/mL comparison. Main text and eFigure 2 repeat the same model/scale; eFigure 2C is explicitly an HR-scale rendering. P=.03 is not display zero and no candidate is based on P formatting. | Checked; no candidate. |
| N043--N047 | Assigned-dose comparisons retain their source/context labels. N046 repeats 1.4%/0.9% from N040 exactly; conclusion does not introduce a contradictory numerical claim. External-study values are not cross-source identity checks. | Checked; no candidate. |
| N048--N049 | Protocol n=2300, four-year schedule, dose labels, and 1:2 nested case-control plan are internally coherent planning quantities. They differ from final trial eligibility/dose by document purpose and are not treated as an error. | Checked; no candidate. |
| N050 | Table 4 cohort entry: 383+767+767+383 = 2300; finishes: 333+667+667+333 = 2000; 2300-2000 = 300; 300/2300 = 13.04%, compatible with 13.0%. Project-year visits sum 3430+4443+4290+4143+3018 = 19324. | Checked; no candidate. |
| N051--N056 | Protocol rate, power, pilot, recruitment, validation, schedule, and measurement values are planning/context quantities. Table 5 power grid is internally ordered as expected across lower annual rates/effect sizes; Table 6 reported CIs contain their RRs and their P/power labels are not arithmetically contradicted by printed inputs. | Checked; no candidate. |
| N057 | 600 mg twice daily = 1200 mg/d. Attrition arithmetic: 2000 / (1-0.13) = 2298.9, compatible with planned n=2300. Two distinct printed unit/direction conflicts are proposed below. | Checked; two candidate proposals. |
| N058--N060 | Censoring/person-time definitions preserve the correct person-year denominator and rate-versus-risk labels. Interim alpha values are a stated spending rule, not additive independent P values; no contradiction is printed. | Checked; no candidate. |
| N061--N063 | 25 cases/y x 3 years = 75; 5+20 = 25/y; 5/1000 = 0.5% and 20/1000 = 2%. The 1:2 matching and quarterly-QC definitions have consistent units/threshold labels. | Checked; no candidate. |
| N064 | 75.7-62.3 = 13.4 nmol/L. Pilot/WHI/adherence/protocol-power figures are explicitly historical or planning context and have no same-estimand final-study identity claim. | Checked; no candidate. |
| N065--N066 | eFigure 1 exclusions/risk sets duplicate the correctly reconciled N041 denominators and Figure 2 time-to-event pattern. eFigure 2A's 6--107-ng/mL range and 30--55-ng/mL data-density statement do not imply an unprinted rate/count. | Checked; no candidate. |

## Candidate proposals

### NCAND-001 — Impossible printed placebo participant count in Table 2 outside-study calcium row

- **Exact source:** DOC-001, PDF p.5 (printed journal p.1238), Table 2, “Outside of Study Supplement Intake (Visit 2 to Visit 9),” “Calcium, mg/d”; direct layout asset `preprocessing/layout_text/DOC-001.txt`, table line showing `1099 ... 1994 ...`.
- **Direct observation:** The treatment calcium row prints N=1099, mean 500 (95% CI 475 to 525); the placebo calcium row prints N=1994, mean 512 (489 to 536); printed between-group difference is -12.0 (-46.0 to 22.0). The adjacent placebo vitamin-D row prints N=1094. The total randomized placebo arm is 1147 (DOC-001 PDF p.1 and p.4).
- **Rule/calculation:** A group-specific participant count cannot exceed the assigned group population. 1994 > 1147 by 847 participants. It also differs from the adjacent placebo outside-supplement N=1094 by 900. The means themselves reconcile: 500-512=-12.0 mg/d.
- **Tolerance:** Exact for an integer participant count; no rounding tolerance can reconcile 1994 with a 1147-person arm.
- **Inference and alternative:** The impossibility is directly observed in the printed table. The likely source-grounded alternative is a transposition/typographical error for 1094 (the adjacent placebo outside-study row), but the source does not explicitly confirm that correction; the candidate is not a claim that 1094 is the final value.
- **Quality-control relevance:** The denominator identifies the sample underlying a longitudinal supplement-intake comparison and affects interpretability/reuse of the table.
- **Human question:** What is the correct placebo participant count for the outside-study calcium-intake row, and should the published Table 2 be corrected?

### NCAND-002 — Protocol's ≥70-year vitamin-D “limit” has an internally incompatible direction

- **Exact source:** DOC-002, PDF p.7, section “5. Intervention”; direct native asset `preprocessing/native_text/DOC-002.txt`: “limit that to no more than 400 IU/day if they are < 70 years of age and to more than 600 IU/day if they are ≥ 70.”
- **Direct observation:** In one sentence governed by “limit,” the <70 condition supplies an upper bound (“no more than 400 IU/day”), while the ≥70 condition supplies a lower-bound phrase (“more than 600 IU/day”).
- **Rule/calculation:** A limiting instruction requires an upper constraint; “more than 600 IU/day” sets the opposite inequality (>600), not a maximum. This is a direction/label contradiction, not a recalculation of intake.
- **Tolerance:** Not applicable; inequality direction is categorical.
- **Inference and alternative:** Directly observed wording. A plausible source-grounded alternative is that “no more than 600 IU/day” was intended, because the sentence describes limits and calls both values recommended intake levels, but that repair is inferential and unconfirmed.
- **Quality-control relevance:** The stated allowable co-intervention quantity is part of the protocol's exposure definition.
- **Human question:** Was the ≥70-year instruction intended to be “no more than 600 IU/day,” or another explicit maximum?

### NCAND-003 — Protocol calcium target changes unit from 1200 mg/day to 1200 g/day

- **Exact source:** DOC-002, PDF p.7, section “5. Intervention”; direct native asset `preprocessing/native_text/DOC-002.txt`. The same paragraph states Group 1 receives calcium “(1200 mg/d)” and “600 mg caplets” twice daily, then states: “Recommended levels of calcium intake were ... set as 1,200 g/day ... the level of supplementation that we are including.”
- **Direct observation:** The active regimen and two-caplet calculation specify 1200 mg/day; the immediately following claimed identical supplementation level prints 1200 g/day.
- **Rule/calculation:** 600 mg x 2/day = 1200 mg/day = 1.2 g/day. Printed 1200 g/day is 1,000 x 1.2 g/day and 1,000-fold larger than 1200 mg/day. Thus the assertion that 1200 g/day is “the level of supplementation” conflicts with the printed regimen.
- **Tolerance:** Exact unit conversion (1000 mg = 1 g); no rounding tolerance can bridge a factor of 1000.
- **Inference and alternative:** The conflicting units are direct observations. A likely typographical alternative is “1,200 mg/day” (or “1.2 g/day”), but the source does not expressly correct it.
- **Quality-control relevance:** A dose unit is a core exposure label; the conflict could mislead protocol interpretation or structured extraction.
- **Human question:** Should the protocol sentence say 1,200 mg/day (1.2 g/day), rather than 1,200 g/day?

## Individual completion index

Each identifier below was individually checked under the applicable grouped-register row above; this index makes the full assigned-ID completion explicit.

| IDs completed | Register row(s) |
|---|---|
| N001; N002; N003 | N001--N003 |
| N004; N005; N006; N007; N008 | N004--N008 |
| N009; N010; N011; N012 | N009--N012 |
| N013; N014; N015; N016 | N013--N016 |
| N017; N018; N019; N020 | N017--N020 |
| N021; N022; N023; N024 | N021--N024 |
| N025; N026; N027; N030 | N025--N027, N030 |
| N028 | N028 |
| N029 | N029 |
| N031; N032; N033; N034; N035 | N031--N035 |
| N036; N037; N038 | N036--N038 |
| N039; N040; N041 | N039--N041 |
| N042; N067; N068; N069 | N042, N067--N069 |
| N043; N044; N045; N046; N047 | N043--N047 |
| N048; N049 | N048--N049 |
| N050 | N050 |
| N051; N052; N053; N054; N055; N056 | N051--N056 |
| N057 | N057 |
| N058; N059; N060 | N058--N060 |
| N061; N062; N063 | N061--N063 |
| N064 | N064 |
| N065; N066 | N065--N066 |

## Limitations and lane conclusion

All 69 assigned IDs were completed. Three distinct document-grounded candidate proposals were retained. Most outputs are rounded summaries, model estimates, or planning statements without sufficient raw inputs to independently recompute confidence intervals, power, Kaplan--Meier estimates, or Cox regression; those were assessed only for printed internal consistency and labeling. No candidate was generated solely from a displayed P-value convention, and no candidate has a severity, validity determination, or disposition.
