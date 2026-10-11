# Cross-source consistency review

Status: COMPLETE. Controls read completely: QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md. Assignment: all matched report results and all statistical design relationships across DOC-001 through DOC-005, using the complete fresh main and support maps over 94 supplied PDF pages. No structured spreadsheet, CSV, or Office source was supplied. No old scientific conclusions or external sources were used. Source-linked reusable native/layout text was used for navigation; finding statements were reread in direct supplied PDFs with Poppler pdftotext 25.03.0. This artifact proposes findings and domains only; it assigns no candidate IDs or adjudications.

## Coverage and matching record

Population, outcome, time origin/window, contrast/reference group, analysis set, model, measure, and precision were matched before comparing quantities. The main map's M001–M100 and every constituent in the support map's 20 plan families, five result tables, four figures, and complete criterion lists were reviewed. Counts here are evidence-map groupings, not limits on discovery.

| Relationship scope | Completed comparison |
|---|---|
| Abstract, Key Points, main primary narrative, Table 2, supplementary eFigure 1 | Day-28 VFD median 21 (0–26) in each group; 475/480 complete cases; mean difference −0.27 (−1.74 to 1.19), P=.71. Abstract, narrative, and table agree; cumulative curve is the same primary distribution, without exact individual coordinates. Means and medians remain distinct quantities. |
| All abstract key secondary results versus Table 2 and narrative | ICU/hospital stay; day-28/day-90 mortality; ARDS, pneumonia, atelectasis, and pneumothorax estimates, intervals, P values, and reported distributions agree. Figure 2B repeats day-90 HR 1.07 (0.87–1.31), P=.54. |
| Main Table 2 versus Figure 2A/C/D and caption | Liberation and length-of-stay hazard ratios are matched to time-to-event analyses; Table 2 mean differences are matched to t test/inverse-Gaussian GLM. Different measures and observation-time summaries are not treated as copies of the same result. All curve labels, direction, risk-table cells, caption values, and footnotes were checked. |
| Main flow/abstract/narrative | 961 randomized, 477/484 allocation, 475/480 primary complete cases, six missing primary outcomes. “Considered” and ITT language do not mean every randomized subject supplied complete-case data. |
| Main physiologic narrative versus eTables 1–3 and eFigures 2–4 | Each occasion and mode is kept separate. Tidal-volume separation, lower driving pressures, higher carbon dioxide/lower pH, and mode-dependent respiratory-rate claims were compared with their corresponding rows and figure panels. No single-day contributor total was treated as an analysis-population total. |
| Main co-intervention narrative versus eTable 4 | Need/duration comparisons for sedatives, analgesics, blockers, fluids, blood products, and rescue interventions matched; the planned ascertainment window versus the reported three-day window is retained below. RASS scores are not quantities of drug administered. |
| Main subgroup narrative versus every eTable 5 pair | All eight displayed subgroup pairs were checked itemwise: pneumonia, sepsis, PaO2/FiO2, LIPS, admission reason, SAPS II, prior-ventilation duration, and intubation location. ICU-location estimates −2.50 (−4.63 to −0.36) and 1.45 (−0.52 to 3.43), interaction P=.01 agree numerically. |
| Eligibility criteria, item by item | Four protocol inclusions and twelve exclusions were compared with SAP pp6–7 and report pp2–3: participating ICU, invasive ventilation, one-hour allocation, expected >24-hour ventilation; age, previous enrollment, other interventional trial, ARDS/low PaO2/FiO2 exception, >12-hour ventilation, pregnancy, intracranial pressure, COPD III/IV, status asthmaticus, restrictive disease, thromboembolism, pneumectomy/lobectomy. The PaO2/FiO2 exception is retained below. Other-trial participants are visibly not enrolled in Figure 1. |
| Primary endpoint and success criteria, item by item | Day 28, alive, invasive ventilation, unassisted interval ≥24 hours, repeated ventilation/free periods, tracheostomy criteria, and zero days for prolonged ventilation were compared. The ICU-admission/randomization origin is retained below. All extubation criteria were compared separately: cooperation, cough, oxygenation/FiO2, respiratory rate, distress, support threshold, blood pressure, heart rate, arrhythmia, temperature, ≥30-minute duration. |
| Intervention specifications | PBW formulas, initial 6/10 mL/kg, titration 1 mL/kg/hour, low minimum 4, pressure-support minimum 5 cm H2O, plateau/maximum airway limit 25, permitted tolerance exceptions, prohibitions on extra sedation, 28-day duration, and resumption after reintubation compared. Achieved tidal volumes are not assigned targets. |
| Primary model, covariates, sensitivity and per-protocol criteria | Original Cox model, updated primary t test; four covariates age/LIPS/SAPS II/PaO2/FiO2; center/intubation random effects; low >6 and high <8 in first two days with each tolerance/pressure exception checked separately. Changes/omissions are retained below. |
| Nine planned subgroup criteria and mediation | All nine SAP subgroups were compared with the report's eight; respiratory-rate subgroup and mechanical-power mediation are retained below, along with model changes. Driving pressure/flow derivations were checked as plan context, not assumed to have been analyzed. |
| Secondary outcome hierarchy, components and definitions | Every protocol/SAP secondary item was compared separately; added day-28 mortality and newly listed secondary outcomes retained below. ARDS severity eligibility for the endpoint and sedation/blocker window retained separately. Pneumonia/VAP and atelectasis descriptions matched to supplied definitions. |
| Missing data and analysis population | SAP complete-case rule and >1% primary-missing trigger agree with report <1%: 6/961=0.624%. ITT assigned-group rule and consent exclusions agree. Economic >10% imputation belongs to an economic analysis, not the primary outcome. |
| Power and hypothesis | Total 952, 476/group, difference one day, SD 5, power 80%, two-sided .05, superiority direction agree across documents. Original plan's t-test power versus Cox analysis is retained with primary model finding. Numeric reproduction belongs to the statistical and numeric lanes. No noninferiority/equivalence margin is supplied. |
| Interim, stopping and multiplicity | Safety monitoring after first 150, continuation, absence of efficacy interim tests, two-sided .05 and no multiplicity adjustment compared. No numerical efficacy stopping boundary or alpha-spending rule is stated. Safety-review meeting calendars are peripheral. |
| Economic/administrative and non-result pages | Economic primary/secondary ICER labels, cost inputs, bootstrap, Monte Carlo, subgroup and missingness specifications were reviewed within their economic context; report explicitly defers the cost analysis. DOC-005 p1 has no result/design quantity. Covers, references, and administrative units were closed by their maps. |

## Findings

### F-XS-001

**Observation:** The primary endpoint's time origin changes from ICU admission to randomization.

**Exact linked locations and roles:** PLAN [DOC-002 p10, summary primary endpoint](../../../joi180108supp1_prod.pdf#page=10), [p19, power endpoint](../../../joi180108supp1_prod.pdf#page=19), and [p33, primary analysis](../../../joi180108supp1_prod.pdf#page=33); REPORT [DOC-001 p4, Outcomes](../../../jama_simonis_2018_oi_180108.pdf#page=4), [p6, Table 2 primary result](../../../jama_simonis_2018_oi_180108.pdf#page=6). PLAN [DOC-003 p8, endpoint definition](../../../joi180108supp2_prod.pdf#page=8) specifies days 1–28 without naming the changed origin.

**Printed statements and comparison logic:** The protocol repeatedly says “day 28 after ICU admission.” The report defines the days “calculated from the moment of randomization.” ICU admission and randomization are separate events; the one-hour target does not make them identical. This is an endpoint-window comparison, not a rounded printed estimate. Display-precision interval arithmetic is not applicable to two event origins.

**Focus area:** D. **Proposed review domain:** protocol_report. **Primary relationship:** P_R. **All relationships:** P_R.

**Qualifying route:** Route B.

**Affected result or extracted value:** The day-28 VFD endpoint behind mean difference −0.27 (95% CI −1.74 to 1.19), P=.71, and its follow-up horizon.

**Why context does not resolve it:** B1: the primary endpoint time origin is in focus. B2: the supplied change matrix discusses model changes but does not specify this origin change. B3: a reproducible endpoint definition needs the same start and end events, particularly for patients randomized after arrival.

**Supported alternatives and classification ambiguity:** Randomization may have been the intended operational origin throughout, or the endpoint may have been amended from ICU admission; the supplied pages do not give that amendment explicitly. The reported endpoint is clear, but its correspondence with the earlier planned endpoint is not.

**Exact human question:** Was day-28 ventilator-free time defined from ICU admission or from randomization in the analysis, and was the change of origin prospectively specified?

### F-XS-002

**Observation:** The protocol's additional low-oxygenation eligibility condition is absent from the updated eligibility definition.

**Exact linked locations and roles:** PLAN [DOC-002 p17, exclusion list](../../../joi180108supp1_prod.pdf#page=17), [p18, explicit exception](../../../joi180108supp1_prod.pdf#page=18); PLAN [DOC-003 pp6–7, eligibility/exclusions](../../../joi180108supp2_prod.pdf#page=6), [p7](../../../joi180108supp2_prod.pdf#page=7); REPORT [DOC-001 p2, Patients](../../../jama_simonis_2018_oi_180108.pdf#page=2), [p5, Table 1 oxygenation distribution](../../../jama_simonis_2018_oi_180108.pdf#page=5), [DOC-004 p9, oxygenation subgroup](../../../joi180108supp3_prod.pdf#page=9).

**Printed statements and comparison logic:** The original protocol excludes clinical ARDS and also PaO2/FiO2 <200 mm Hg, permitting the latter only when the attending explicitly states no ARDS and no direct ARDS risk factor is present. The updated SAP and report list clinical ARDS according to Berlin without that additional restriction. These are different criterion sets: for a patient with PaO2/FiO2 <200, no clinical ARDS, but a direct ARDS risk factor, the earlier stated rule excludes and the updated list does not. This is logical criterion comparison; rounding is not applicable.

**Focus area:** D. **Proposed review domain:** protocol_report. **Primary relationship:** P_R. **All relationships:** P_R, P_P.

**Qualifying route:** Route B.

**Affected result or extracted value:** Eligibility of the primary-analysis population and interpretation of the PaO2/FiO2 ≤200 subgroup, whose mean differences are −0.87 (−3.21 to 1.47) versus 0.87 (−1.62 to 3.36).

**Why context does not resolve it:** B1: this alters an explicit population-defining criterion. B2: “clinical ARDS” does not logically reproduce the protocol's additional direct-risk-factor condition in non-ARDS patients. B3: whether low-oxygenation patients with direct risk factors were eligible determines the population to which the primary and subgroup results apply. No numerical change in randomized population size is asserted.

**Supported alternatives and classification ambiguity:** The extra precaution may have remained operationally enforced but been omitted from the later summary, or it may have been removed by amendment. The supplied protocol is version 3.2; no dated itemized eligibility amendment is supplied. P_R has precedence over the also-present P_P comparison.

**Exact human question:** Was the original PaO2/FiO2 <200 exception, including absence of a direct ARDS risk factor, enforced for enrolled patients, or was it changed before enrollment/analysis?

### F-XS-003

**Observation:** The originally specified primary Cox analysis is replaced by a t-test mean-difference analysis.

**Exact linked locations and roles:** PLAN [DOC-002 p33, primary analysis](../../../joi180108supp1_prod.pdf#page=33), [p19, t-test power specification](../../../joi180108supp1_prod.pdf#page=19); PLAN [DOC-003 p12, updated primary analysis](../../../joi180108supp2_prod.pdf#page=12), [p21, change matrix primary row](../../../joi180108supp2_prod.pdf#page=21); REPORT [DOC-001 p2, update disclosure](../../../jama_simonis_2018_oi_180108.pdf#page=2), [p4, Statistical Analysis](../../../jama_simonis_2018_oi_180108.pdf#page=4), [p6, Table 2](../../../jama_simonis_2018_oi_180108.pdf#page=6).

**Printed statements and comparison logic:** Original primary VFD analysis is Cox regression with possible imbalance modeled. Updated SAP specifies Student's t test and mean difference; the report gives mean difference −0.27 (−1.74 to 1.19), P=.71 from t tests. The matrix explicitly records that replacement and lists no post-hoc primary modification. Original power uses means 23/24, common SD5, a two-group t test, and 397/group before inflation, whereas the original primary-analysis section specifies Cox regression. Models and effect measures differ; this is not display precision. The Cox HR for time to liberation in Figure 2A is a separate time-to-event analysis and does not restore the original primary VFD analysis.

**Focus area:** D. **Proposed review domain:** protocol_report. **Primary relationship:** P_R. **All relationships:** P_R, P_P.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** The prespecified primary analysis and effect measure for day-28 VFD; the reported result is a mean difference, not a primary Cox effect.

**Why context does not resolve it:** Route A category 5 applies to the planned primary analysis replaced in the report. The disclosed update identifies the reported analysis and must accompany the finding; it does not eliminate the planned-versus-reported comparison.

**Supported alternatives and classification ambiguity:** The November 24, 2017 SAP may represent the definitive prospective amendment before database lock, as stated in the report and matrix. The original t-test power and Cox analysis could also have been intended for different roles. No claim about timing relative to unblinding is made beyond supplied statements. The original-model/power comparison is P_P; the primary report-plan comparison is P_R.

**Exact human question:** Should the supplied pre-lock SAP be regarded as the governing amendment for the primary t-test analysis, and how was the original Cox-analysis specification related to its t-test power calculation?

### F-XS-004

**Observation:** Secondary-outcome status is assigned to additions relative to the earlier outcome lists.

**Exact linked locations and roles:** PLAN [DOC-002 pp26–27, complete endpoint lists](../../../joi180108supp1_prod.pdf#page=26), [p27](../../../joi180108supp1_prod.pdf#page=27); PLAN [DOC-003 p9, updated secondary list](../../../joi180108supp2_prod.pdf#page=9), [p21, change matrix secondary outcomes](../../../joi180108supp2_prod.pdf#page=21); REPORT [DOC-001 p1, abstract secondary outcomes](../../../jama_simonis_2018_oi_180108.pdf#page=1), [p4, Outcomes](../../../jama_simonis_2018_oi_180108.pdf#page=4), [p6, Table 2 secondary block](../../../jama_simonis_2018_oi_180108.pdf#page=6).

**Printed statements and comparison logic:** Day-28 mortality is absent from the original protocol secondary list but is secondary in the updated SAP and report; report p4 explicitly discloses the addition. Extrapulmonary infection, extrapulmonary sepsis, and need of tracheostomy are absent from both original and updated secondary lists but appear under Table 2 “Secondary outcomes.” The matrix expressly lists those three in “MODIFICATIONS POST-HOC,” defined as considered in neither earlier plan. Their table results are RR0.84 (0.60–1.18), P=.28; RR0.87 (0.56–1.33), P=.50; and RR1.03 (0.84–1.26), P=.78. Itemwise status comparison establishes this pattern; no rounding calculation is applicable.

**Focus area:** D. **Proposed review domain:** protocol_report. **Primary relationship:** P_R. **All relationships:** P_R, P_P.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Prespecification/status extraction for day-28 mortality and the three additional Table 2 outcomes.

**Why context does not resolve it:** Route A category 5 covers changes in prespecified outcome status and planned-versus-reported outcomes. The amendment/post-hoc matrix makes the changes transparent and supports an alternative classification; its disclosure is retained rather than treating these outcomes as prospectively specified by default.

**Supported alternatives and classification ambiguity:** Day-28 mortality may properly be considered a prospectively amended secondary endpoint under the governing SAP. The three additional outcomes may be intended as post-hoc exploratory secondary outcomes, consistent with the report's general statement that secondary analyses are exploratory. Their table status should not be extracted as original prespecification. P_P applies to the added day-28 outcome between plans; P_R applies to report additions.

**Exact human question:** How should day-28 mortality and the three post-hoc additions be labeled for original, amended, and post-hoc outcome prespecification in evidence extraction?

### F-XS-005

**Observation:** Several prespecified analyses of the primary endpoint have no reported result.

**Exact linked locations and roles:** PLAN [DOC-002 p33, per-protocol plan](../../../joi180108supp1_prod.pdf#page=33); PLAN [DOC-003 pp13–15, per-protocol, subgroups and exploratory analyses](../../../joi180108supp2_prod.pdf#page=13), [p14](../../../joi180108supp2_prod.pdf#page=14), [p15](../../../joi180108supp2_prod.pdf#page=15); PLAN [DOC-003 pp21–22, change matrix](../../../joi180108supp2_prod.pdf#page=21), [p22](../../../joi180108supp2_prod.pdf#page=22); REPORT [DOC-001 p4, methods](../../../jama_simonis_2018_oi_180108.pdf#page=4), [p6, results](../../../jama_simonis_2018_oi_180108.pdf#page=6), [DOC-004 p9, all subgroup rows](../../../joi180108supp3_prod.pdf#page=9).

**Printed statements and comparison logic:** Four primary-endpoint analysis families were itemwise searched throughout both REPORT documents: (1) per-protocol VFD, excluding low-arm >6 mL/kg during first two days without permitted dyspnea/asynchrony/acidosis exception, and high-arm <8 without pressure-limit exception; (2) zero-inflated GLM sensitivity adjusted for age, LIPS, SAPS II, PaO2/FiO2; (3) high/low respiratory-rate VFD subgroup, median of first two days; (4) mechanical-power mediation of treatment effect on VFD, deriving driving pressure and flow from recorded variables. The report supplies ITT/complete-case primary results, center/intubation-location GLMM sensitivity P=.72, and eight other subgroup pairs, but no result for these four families. The matrix confirms “Not reporting the GLM with adjustment for covariates,” per-protocol “Not described,” and mediation “None”; it lists respiratory rate as in-paper even though the actual report has no corresponding row/result. Absence was checked against complete REPORT scope, not a sampled display. Rounding is not applicable.

**Focus area:** D. **Proposed review domain:** protocol_report. **Primary relationship:** P_R. **All relationships:** P_R, P_P.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Prespecified robustness, per-protocol, respiratory-rate subgroup and mediation analyses of day-28 VFD; the only supplied sensitivity P=.72 concerns the stratification-random-effects model.

**Why context does not resolve it:** Route A category 5 expressly includes a planned primary analysis that is not reported. Labeling analyses exploratory does not supply their results. The matrix acknowledges several omissions, but does not state that the missing analyses were prospectively withdrawn or provide their results.

**Supported alternatives and classification ambiguity:** These analyses may have been performed for a later report, abandoned, or considered unsuitable; no choice among those explanations is inferred. The matrix's “IN THE PAPER” respiratory-rate entry may refer to an unavailable display or may describe intended rather than supplied reporting. The same missing-primary-analysis pattern is consolidated here with every identified family and location; the matrix respiratory-rate column versus SAP/report also entails P_P.

**Exact human question:** Were the four planned primary-endpoint analysis families performed, and where can their results or a documented decision not to perform/report them be found, including the respiratory-rate subgroup listed as in-paper?

### F-XS-006

**Observation:** The reported primary-endpoint subgroup model replaces the planned zero-inflated model with a Gaussian model.

**Exact linked locations and roles:** PLAN [DOC-003 p14, subgroup interaction model](../../../joi180108supp2_prod.pdf#page=14), [p22, model change matrix](../../../joi180108supp2_prod.pdf#page=22); REPORT [DOC-001 p4, subgroup methods](../../../jama_simonis_2018_oi_180108.pdf#page=4), [p6, ICU-location interaction](../../../jama_simonis_2018_oi_180108.pdf#page=6), [DOC-004 p9, eTable 5](../../../joi180108supp3_prod.pdf#page=9).

**Printed statements and comparison logic:** SAP p14 specifies subgroup-by-arm interactions using GLMs “considering zero-inflated distributions.” Main p4 specifies Gaussian distributions. Matrix p22 identifies this as a post-hoc change “according to the CLT.” All eight reported subgroup pairs are affected: pneumonia, sepsis, oxygenation, LIPS, admission reason, SAPS II, prior-ventilation duration, and intubation location. The primary endpoint and subgroup definitions match; the model distributions do not. No numeric recalculation or display-precision difference is asserted.

**Focus area:** D. **Proposed review domain:** protocol_report. **Primary relationship:** P_R. **All relationships:** P_R.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** All eTable 5 primary-endpoint subgroup mean differences/intervals and interaction tests, including location interaction P=.01 and ICU subgroup −2.50 (−4.63 to −0.36).

**Why context does not resolve it:** Route A category 5 applies to the planned primary-endpoint subgroup analysis replaced in reporting. The explicit CLT rationale identifies the replacement, but the prospective zero-inflated analysis is not reported.

**Supported alternatives and classification ambiguity:** Gaussian modeling may have been intentionally substituted as disclosed in the matrix. This is a planned-versus-reported record, not a preference for either model and not a claim that its result would differ numerically. The matrix's post-hoc column is content classified PLAN within the supplied SAP bundle.

**Exact human question:** Were the zero-inflated subgroup analyses performed alongside the disclosed Gaussian analyses, and should the reported subgroup results be identified as arising from a post-hoc model change?

### F-XS-007

**Observation:** The reported sedative and neuromuscular-blocker comparisons cover three days rather than the planned ascertainment through day 28 or ICU discharge.

**Exact linked locations and roles:** PLAN [DOC-002 p27, cumulative-use/duration endpoints](../../../joi180108supp1_prod.pdf#page=27), [p28, endpoint collection window](../../../joi180108supp1_prod.pdf#page=28); REPORT [DOC-001 p4, secondary outcomes](../../../jama_simonis_2018_oi_180108.pdf#page=4), [p6, no-difference claim](../../../jama_simonis_2018_oi_180108.pdf#page=6), [DOC-004 p8, eTable 4 title and rows](../../../joi180108supp3_prod.pdf#page=8).

**Printed statements and comparison logic:** The protocol specifies cumulative sedative and NMBA use/duration, with daily collection to day 28 or ICU discharge, whichever first. eTable 4 explicitly covers “during the first three days.” Sedative infusion 320 (70.6%) versus 333 (72.1%), days 0.6 (0.3–1.5) versus 0.6 (0.0–1.5), P=.76; blockade 53 (11.7%) versus 60 (13.0%), days 0.0 (0.0–0.3) in both, P=.55. Main p6 states no difference in need, duration, and amount without restating that restriction. A cumulative three-day endpoint is not the planned cumulative 28-day/discharge endpoint. This is a window/specification comparison, not numeric rounding.

**Focus area:** D. **Proposed review domain:** protocol_report. **Primary relationship:** P_R. **All relationships:** P_R.

**Qualifying route:** Route B.

**Affected result or extracted value:** Sedative and neuromuscular-blocker cumulative need/duration comparisons, which must be extracted with their three-day horizon rather than as full planned ICU-course outcomes.

**Why context does not resolve it:** B1: report-plan endpoint windows are in focus. B2: the eTable makes the reported window clear but does not explain whether or why it replaces the planned window. B3: the general no-difference claim and the days-of-administration values concern a materially shorter period than the planned cumulative endpoints. The comparison is about endpoint definition, not contributor counts at individual time points.

**Supported alternatives and classification ambiguity:** Three-day data may be an intentional early-intervention summary while complete cumulative data exist elsewhere; none are supplied. The report's statement about “amount” may refer to information outside the displayed need/duration rows, but no drug-dose values are supplied. No assertion about the direction or significance of an unavailable full-course result is made.

**Exact human question:** Do the no-difference statements about cumulative sedative/blocker use and duration apply only to the first three days, and where are the planned day-28-or-ICU-discharge cumulative results or their amended endpoint specification?

### F-XS-008

**Observation:** The planned ARDS ascertainment list is restricted to moderate/severe ARDS while the endpoint lists and report use new ARDS without that restriction.

**Exact linked locations and roles:** PLAN [DOC-002 p26, development of ARDS endpoint](../../../joi180108supp1_prod.pdf#page=26), [p28, pulmonary-complication collection](../../../joi180108supp1_prod.pdf#page=28), [p48, Berlin severity criteria](../../../joi180108supp1_prod.pdf#page=48); PLAN [DOC-003 p9, new ARDS endpoint](../../../joi180108supp2_prod.pdf#page=9); REPORT [DOC-001 p1, abstract ARDS](../../../jama_simonis_2018_oi_180108.pdf#page=1), [p4, new ARDS outcome](../../../jama_simonis_2018_oi_180108.pdf#page=4), [p6, Table 2](../../../jama_simonis_2018_oi_180108.pdf#page=6).

**Printed statements and comparison logic:** Protocol p26 names development of ARDS and cites Appendix I; p28 specifies collection of “Moderate or severe ARDS (yes or no).” Appendix I separately defines mild as 200<PaO2/FiO2≤300, moderate as 100<PaO2/FiO2≤200, and severe as ≤100 mm Hg, with PEEP≥5. SAP and report say “new ARDS” without a severity restriction. The reported incidence is 17/448 (3.8%) versus 23/462 (5.0%), RR0.86 (0.59–1.24), P=.38. The criterion sets differ as to mild ARDS; printed labels do not establish which severity range the reported event counts use. This is a criterion/threshold comparison, not display rounding.

**Focus area:** D. **Proposed review domain:** protocol_report. **Primary relationship:** P_R. **All relationships:** P_R, P_P.

**Qualifying route:** Route B.

**Affected result or extracted value:** Key secondary new-ARDS event counts, percentages and risk ratio, and the severity threshold an extractor should attach to them.

**Why context does not resolve it:** B1: an endpoint threshold is in focus and the ARDS result is in the abstract. B2: the supplied Berlin table includes all three severity grades while the collection item explicitly names two. B3: inclusion of mild events changes the quantity counted; no severity breakdown is supplied to determine the reported definition.

**Supported alternatives and classification ambiguity:** “New ARDS” may be shorthand for newly developed moderate/severe ARDS, or all Berlin grades may have been counted under an amended endpoint. The protocol's generic endpoint and restricted collection item also conflict inside PLAN material; P_R takes precedence.

**Exact human question:** Do the reported 17 and 23 new-ARDS events include mild ARDS or only moderate/severe ARDS, and which planned ascertainment definition governed those counts?

## Excluded observations

Only apparent issues considered and not emitted appear here. Reconciled comparisons are recorded above, not counted as excluded observations.

| Location | Observation | Reason code |
|---|---|---|
| REPORT [DOC-001 p2](../../../jama_simonis_2018_oi_180108.pdf#page=2); PLAN [DOC-002 p20](../../../joi180108supp1_prod.pdf#page=20), [DOC-003 p6](../../../joi180108supp2_prod.pdf#page=6) | “Intermediate” versus “higher/high/conventional” names for the same comparator strategy and target. | TERMINOLOGY_OR_WORDING |
| REPORT [DOC-001 p4](../../../jama_simonis_2018_oi_180108.pdf#page=4); REPORT [DOC-004 p9](../../../joi180108supp3_prod.pdf#page=9); PLAN [DOC-003 p14](../../../joi180108supp2_prod.pdf#page=14) | Medical versus clinical admission subgroup names resolve to the same medical/surgical contrast. | TERMINOLOGY_OR_WORDING |
| REPORT [DOC-001 p6](../../../jama_simonis_2018_oi_180108.pdf#page=6); REPORT [DOC-004 p9](../../../joi180108supp3_prod.pdf#page=9) | Subgroup mean-difference interval called IQR in narrative and 95% CI in eTable 5; identical endpoints and mean-difference context identify the interval at once. No printed value is changed. | TERMINOLOGY_OR_WORDING |
| REPORT [DOC-001 pp1–2](../../../jama_simonis_2018_oi_180108.pdf#page=1); [p2](../../../jama_simonis_2018_oi_180108.pdf#page=2); PLAN [DOC-003 p6](../../../joi180108supp2_prod.pdf#page=6) | Expected ventilation >24 hours and expected not extubated within next 24 hours describe the same eligibility concept; start-of-ventilation versus allocation phrasing alone does not establish a distinct analyzed population. | TERMINOLOGY_OR_WORDING |
| PLAN [DOC-002 p17](../../../joi180108supp1_prod.pdf#page=17); REPORT [DOC-001 p3](../../../jama_simonis_2018_oi_180108.pdf#page=3) | Other-study participation is called an exclusion in the plan but grouped with eligible-not-enrolled in flow. All 348 are visibly outside randomization and no included analysis-population size changes. | PERIPHERAL_COMPARISON |
| PLAN [DOC-002 p23](../../../joi180108supp1_prod.pdf#page=23); REPORT [DOC-001 p3](../../../jama_simonis_2018_oi_180108.pdf#page=3) | Pressure-support extubation wording uses <7/<12 versus ≤7/≤12 and reassessment next day versus following shift; no supplied primary/key result, analysis-population size, or statistical decision rule changes. | PERIPHERAL_COMPARISON |
| PLAN [DOC-002 pp31–32](../../../joi180108supp1_prod.pdf#page=31); PLAN [DOC-003 pp10–11](../../../joi180108supp2_prod.pdf#page=10) | DSMB meeting calendar differs; safety continuation decisions agree and no efficacy decision threshold changes. | PERIPHERAL_COMPARISON |
| PLAN [DOC-003 p12](../../../joi180108supp2_prod.pdf#page=12); REPORT [DOC-004 pp5–8](../../../joi180108supp3_prod.pdf#page=5) | Adherence/physiologic display plan mentions seven days; supplied tables/figures summarize three. This concerns peripheral descriptive occasions, not a changed randomized-intervention duration, primary analysis, or key-secondary endpoint. | PERIPHERAL_COMPARISON |
| PLAN [DOC-002 p17](../../../joi180108supp1_prod.pdf#page=17); PLAN [DOC-003 pp3,6](../../../joi180108supp2_prod.pdf#page=3); REPORT [DOC-001 pp2,4](../../../jama_simonis_2018_oi_180108.pdf#page=2) | Five versus six sites and August 22 versus August 20 recruitment endpoints are administrative comparisons. | PERIPHERAL_COMPARISON |
| REPORT [DOC-001 p2](../../../jama_simonis_2018_oi_180108.pdf#page=2); PLAN [DOC-003 p8](../../../joi180108supp2_prod.pdf#page=8) | Acceptance of tidal volume >8 versus >6 at minimum pressure support does not establish prohibition of intermediate values or a different achieved-dose estimate; both allow above-target spontaneous volumes. | CONDITIONAL_OR_UNREPORTED |
| REPORT [DOC-001 p6, Table 2](../../../jama_simonis_2018_oi_180108.pdf#page=6); PLAN [DOC-003 p8](../../../joi180108supp2_prod.pdf#page=8) | Survivor ventilation-duration rows beneath the primary block could appear additional primary outcomes, but the primary definition remains VFD and these rows describe its ventilation-duration component. | CONTEXT_RESOLVES |
| REPORT [DOC-001 p4](../../../jama_simonis_2018_oi_180108.pdf#page=4); PLAN [DOC-003 p9](../../../joi180108supp2_prod.pdf#page=9) | Secondary outcomes described as exploratory after no multiplicity adjustment retain their secondary outcome labels; this does not establish status demotion. | TERMINOLOGY_OR_WORDING |
| REPORT [DOC-001 p4](../../../jama_simonis_2018_oi_180108.pdf#page=4); PLAN [DOC-002 pp27,34–35](../../../joi180108supp1_prod.pdf#page=27) | Economic analysis is explicitly deferred; primary cost-effectiveness means primary within an ancillary economic analysis, not the trial's primary or abstract key-secondary analysis. | PERIPHERAL_COMPARISON |
| PLAN [DOC-002 pp10,15,27](../../../joi180108supp1_prod.pdf#page=10); PLAN [DOC-003 p9](../../../joi180108supp2_prod.pdf#page=9); REPORT [DOC-001 p4](../../../jama_simonis_2018_oi_180108.pdf#page=4) | Incomplete non-key outcome lists omit asynchrony and several selected-center secondary measurements. The report explicitly discloses unavailable weakness/EAdi/VOC measurements without assigning a different outcome status. No primary/key-secondary result is missing on this basis. | CONDITIONAL_OR_UNREPORTED |

## Counts and limitations

Eight findings; fourteen excluded observations. Coverage: all 94 direct-source pages through complete maps, 100 main relationship groupings, 20 plan families with each eligibility/endpoint/analysis-set/subgroup criterion separately checked, all abstract and primary/key-secondary counterparts, all five supplementary tables and four supplementary figures. No scientific-coverage gap. Intrinsic limitations: exact curve event coordinates and subgroup sample sizes are not supplied; no dated itemized eligibility amendment log is supplied; the report supplies no numerical results for the four omitted primary-endpoint analysis families. Figure content relied on source-linked visual mapping already completed by the mappers, while finding text was checked in direct PDFs. No new OCR, rendering, or derivative was required.
