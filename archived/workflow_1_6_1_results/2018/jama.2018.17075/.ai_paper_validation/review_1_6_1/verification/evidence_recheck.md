# Mechanical evidence recheck

Pending Human Adjudication. Scope: every assigned stable ID, C001, C002, C003 and C004, including every affected location of the repeated bleeding pattern. This fresh recheck used the exact supplied PDFs as final authority. Current ledger, current screening and current checker findings supplied provenance; reusable derivatives did not determine the source reading. All nine unique cited pages were freshly extracted and rendered directly from their supplied PDFs, and all nine renders were visually inspected. No assigned location was unavailable. No source or reused artifact was modified. No web, OCR, GPU or Python scientific helper was used.

Engine: direct Poppler 25.03.0, `pdftotext -layout -f N -l N` and `pdftoppm -f N -l N -r 125 -singlefile -png`. Derivatives are below `preprocessing/recheck/`: `main-p1.txt`, `main-p1.png`, `main-p3.txt`, `main-p3.png`, `main-p4.txt`, `main-p4.png`, `main-p5.txt`, `main-p5.png`, `main-p7.txt`, `main-p7.png`, `plan-p77.txt`, `plan-p77.png`, `plan-p101.txt`, `plan-p101.png`, `results-p10.txt`, `results-p10.png`, `results-p11.txt`, and `results-p11.png`. Page numbers in links are PDF page numbers; printed page numbers are recorded only to help navigation.

Integer event and participant counts are exact discrete inputs. Displayed continuous numbers use half-unit rounding intervals. The calculations below were independently recomputed with transparent arithmetic in the agent tool context; no candidate selection or classification was automated. Pearson and log-Wald calculations are explicitly diagnostics wherever the source does not name their implementation.

| Stable ID | Evidence state | Review domain | Relationship type | All relationships | Classification change |
|---|---|---|---|---|---|
| C001 | reproduced | protocol_report | P_R | P_R | None |
| C002 | reproduced | statistical_results | S_W | S_W | None |
| C003 | reproduced | statistical_results | S_C | S_C, S_W | None |
| C004 | reproduced | statistical_results | S_C | S_C, S_W | None |

## C001 — Duration attributed to assigned normothermic management

**Location found:** Yes, every cited location was found and read directly, with fresh visual confirmation.

| Exact supplied-source location | Role by content | Source text matched | Function in comparison |
|---|---|---|---|
| [Main PDF p. 1, abstract Interventions; printed p. 2211](../../../jama_cooper_2018_oi_180132.pdf#page=1) | REPORT: completed trial intervention and result summary | Both groups had temperature managed for 7 days; normothermia targeted 37°C using surface wraps when required; other care was at treating-physician discretion. | Reported both-group duration. |
| [Main PDF p. 3, Rewarming and Normothermia; printed p. 2213](../../../jama_cooper_2018_oi_180132.pdf#page=3) | REPORT: delivered randomized intervention methods | After reaching 37°C, patients were maintained normothermic with automated wraps, if required, up to 7 days postrandomization. Control ICU target was 37°C ± 0.5°C, with wraps permitted for pyrexia or refractory intracranial hypertension. | Reported post-rewarming duration and control-care context. |
| [Plan PDF p. 77, Version 9, §12.11; printed p. 25 of 86](../../../joi180132supp1_prod.pdf#page=77) | PLAN: prospective rewarming and control-arm instructions | Maximum protocolized hypothermia was 7 days; post-rewarming normothermia with pads had a maximum of 7 days or ICU discharge. Control pyrexia above 38°C was to be avoided up to 96 hours postrandomization, after which unit protocol applied. | Control 96-hour comparator; hypothermia 7-day statement corroborates part of report context. |
| [Plan PDF p. 101, Version 9, Appendix F, §26.5 infection/post-rewarming bullets; printed p. 49 of 86](../../../joi180132supp1_prod.pdf#page=101) | PLAN: prospective cooling and rewarming instructions | Pads available/on patient for a total of 96 hours; after rewarming, normothermia with pads for 96 hours postrandomization then ward protocol; all-patient pyrexia avoidance up to 96 hours then unit protocol. Maximum hypothermia separately remained 7 days. | All-patient and post-rewarming 96-hour handoff. |

**Source value/text matched:** Yes. The report's 7-day wording is printed in the abstract and post-rewarming paragraph; the latter explicitly uses the postrandomization anchor.

**Comparator matched:** Yes. The plan's control instruction explicitly uses 96 hours postrandomization and a subsequent unit-protocol handoff; Appendix F repeats a 96-hour postrandomization handoff for post-rewarming/all-patient management. The plan does not state that ordinary care ends at 96 hours.

**Consistency rule applicable:** Compare duration attributed to assigned comparator/post-rewarming management with prospective trial instructions using the same postrandomization anchor. Maximum hypothermia duration and ongoing ordinary ICU care are distinct quantities and are not substituted for comparator duration.

**Calculation or logical comparison reproduced:** Yes, within that bounded comparison. 96 hours = 4 days; 7 days = 168 hours; difference = 72 hours. These are intervention prescriptions rather than estimates rounded from measurements. Even a conservative half-unit display allowance gives 7 days in [6.5, 7.5) days, or [156, 180) hours, versus 96 hours in [95.5, 96.5) hours. The intervals are disjoint. Arithmetic does not establish what care patients actually received after the handoff.

**Necessary inputs available:** Both report descriptions, both final-plan instructions, explicit handoff and time anchor, and distinction between normothermia and maximum hypothermia are supplied. The affected extraction is the comparator/post-rewarming duration accompanying the six-month favorable GOS-E treatment contrast. The main p. 1 abstract confirms favorable counts 117 and 111; main p. 4 Figure 1 confirms primary-analysis denominators 240 and 226.

**Exact missing inputs or definitions:** Operative assignment of days 5–7 to trial-prescribed versus local care; any amendment extending the control/all-patient period; whether the Appendix F period was superseded; actual duration received by patient and arm. No absent amendment or adherence record is inferred.

**Source-grounded alternative interpretation:** The report may summarize temperature management that continued under local care beyond the plan's 96-hour handoff. Alternatively a later operational extension may have applied, or Appendix F may preserve an earlier instruction. Main-plan hypothermia post-rewarming text itself gives a 7-day maximum. These supplied contextual facts limit the claim: it is an unclear duration attribution, not evidence that control patients ceased temperature management at 96 hours or that every patient's treatment lasted 7 days.

**Direct observation versus inferred explanation:** Direct: the report and final plan assign different durations to the comparator/all-patient management description. Inferred and unestablished: extension, retained older appendix language, or local-care continuation as the explanation. No effect change is deduced.

**Exact remaining human question:** Which period represents the operative randomized control and post-rewarming temperature-management instruction, and what supplied amendment or operational specification distinguishes trial-assigned management from local care during days 5–7?

**Compared document roles:** REPORT main pp. 1 and 3 versus PLAN Version 9 p. 77 and Appendix F p. 101, confirmed by retrospective trial reporting versus prospective instructions.

**Relationship type:** P_R

**All relationships:** P_R

**Review domain:** protocol_report

**Classification rationale:** This is report-versus-plan intervention-duration attribution under focus area D. The plan-only hypothermia post-rewarming difference is retained as context, not a separately registered statistical-design relationship. A plan passage corroborating the report's hypothermia maximum does not create another relationship.

**Classification ambiguity:** The plan's main hypothermia post-rewarming paragraph permits 7 days whereas Appendix F specifies a 96-hour handoff. The supplied cited content does not select an amendment or actual received-duration explanation. This ambiguity does not change either document's role or the primary P_R relationship. No classification correction is required.

**Evidence state:** reproduced

**Determining recheck fact:** The source-confirmed report 7-day description and source-confirmed plan 96-hour comparator/all-patient handoff remain different beyond display precision; the registered duration attribution is unresolved within these supplied passages. This evidence state is a record of the bounded comparison, not a determination of intervention adherence.

## C002 — Normothermia Injury Severity Score median and lower quartile

**Location found:** Yes. [Main PDF p. 5, Table 1 Injury Severity Score row, both treatment columns, IQR abbreviation and footnote h; printed p. 2215](../../../jama_cooper_2018_oi_180132.pdf#page=5) was freshly extracted, rendered and visually read. The normothermia column is headed n = 240. All quantities are REPORT baseline summaries of the completed trial.

**Source value/text matched:** Yes. The normothermia row prints median 20.0, with (20.5–35.0) on the line below. It is explicitly labeled median (IQR); IQR is expanded as interquartile range.

**Comparator matched:** Yes. The lower IQR endpoint is 20.5 in the same normothermia cell. The other arm prints 26.0 (18.0–34.0), and footnote h defines a 0–75 injury severity scale, with higher scores indicating greater severity. The line wrapping does not change column attribution.

**Consistency rule applicable:** For a common distribution, its lower quartile Q1 cannot exceed its median: Q1 ≤ median ≤ Q3. The printed median and IQR purport to summarize that same distribution. This is an internal quantile relationship, not a cross-location comparison of peripheral baseline descriptions.

**Calculation or logical comparison reproduced:** Yes. Median 20.0 allows [19.95, 20.05), Q1 20.5 allows [20.45, 20.55), and Q3 35.0 allows [34.95, 35.05). Even the median's upper display bound is 0.40 below Q1's lower bound. The displayed values themselves differ by 0.5. No combination within the half-unit intervals restores Q1 ≤ median. The opposite arm satisfies ordering and does not provide an intended replacement for the normothermia cell.

**Necessary inputs available:** Median label, both endpoints, display precision, arm attribution, and scale definition are supplied. Participant-level scores are not needed for the monotonicity check.

**Exact missing inputs or definitions:** Underlying normothermia score distribution or authoritative summary output identifying the intended median and quartiles. The table does not provide a competing value that settles which numeric component requires clarification.

**Source-grounded alternative interpretation:** The intended median or lower quartile may have another underlying value. A line/column reassignment is not supported by the fresh source render. No summary from a different population is used as a replacement.

**Direct observation versus inferred explanation:** Direct: the normothermia median is below the printed lower quartile beyond display precision. Inferred and unestablished: how that combination arose or which component differs from the original summary.

**Exact remaining human question:** What median, first quartile and third quartile describe the normothermia Injury Severity Score distribution underlying Table 1?

**Compared document roles:** REPORT main Table 1 median versus REPORT main Table 1 lower quartile, within one distribution cell.

**Relationship type:** S_W

**All relationships:** S_W

**Review domain:** statistical_results

**Classification rationale:** One REPORT document contains an incompatible numerical quantile summary; estimate/order logic belongs to statistical_results. No other document is a conflicting comparator.

**Classification ambiguity:** None. No classification correction is required.

**Evidence state:** reproduced

**Determining recheck fact:** Fresh source visual confirmation matches 20.0 (20.5–35.0), and the half-unit intervals cannot satisfy the source-labeled median/IQR ordering.

## C003 — Time-to-33°C comparison and printed P value

**Location found:** Yes, all cited locations were found with direct source extraction and fresh visual inspection.

| Exact supplied-source location | Role by content | Matched content |
|---|---|---|
| [Main PDF p. 4, Statistical Analysis, timing paragraph and significance paragraph; printed p. 2214](../../../jama_cooper_2018_oi_180132.pdf#page=4) | REPORT: trial analysis methods | Favorable outcome by time for cooled patients to reach 33°C was compared with an unadjusted chi-square test for equal proportions; frequency/percentage reporting. SAS 9.4 and two-sided P < .05 are specified. |
| [Main PDF p. 5, Additional Outcomes; printed p. 2215](../../../jama_cooper_2018_oi_180132.pdf#page=5) | REPORT: trial result narrative | Results were not significantly different between groups for time to target temperature, citing eTable 7. |
| [Results-supplement PDF p. 11, eTable 7, every row and merged P cell; printed appendix p. 10](../../../joi180132supp2_prod.pdf#page=11) | REPORT: completed-trial grouped outcome counts and test result | Time rows 1–7 h, 8–13 h, >13 h and Never; n = 49, 67, 59 and 65; favorable counts 18, 28, 32 and 39. One P = .09 appears in a merged cell spanning all four rows. |

**Source value/text matched:** Yes. The eTable 7 values and category alignment were visually confirmed: 18 [36.7 (22.8–50.7)], 28 [41.8 (29.6–53.9)], 32 [54.2 (41.2–67.3)] and 39 [60.0 (47.8–72.2)]. The heading identifies hypothermia patients and approximate tertiles, plus a separate Never row.

**Comparator matched:** Yes. The main method supplies the unadjusted equal-proportions chi-square family; the main narrative supplies the nonsignificant claim and exact eTable 7 citation. The merged P value does not visually select only one row or a stated alternative subset.

**Consistency rule applicable:** Diagnose whether the displayed category counts yield the displayed P under the direct Pearson homogeneity realization of the stated equal-proportions comparison, considering both all displayed categories and the three attained-temperature categories. This is a method/result attribution check. Pearson is not explicitly named in the source, so the diagnostic is not equated to a fully reconstructed original SAS computation.

**Calculation or logical comparison reproduced:** Yes, as the registered bounded diagnostic. All four rows give favorable/unfavorable cells (18,31), (28,39), (32,27), (39,26), totaling 117 favorable and 123 unfavorable, N = 240. With pooled favorable probability 117/240 = .4875, Pearson sum (O−E)²/E = 8.133762156 over eight cells. The displayed 4 × 2 table has diagnostic df = 3, yielding upper-tail P ≈ .0433268. Restricting to attained-temperature rows gives 78 favorable/175, statistic 3.658952245, diagnostic df = 2 and P = .160497627. These reproduce the ledger's calculations. Printed P = .09 allows [.085, .095); neither diagnostic probability lies inside it. Exact integer counts are not varied as rounded percentages. The percentages themselves reconcile with the counts within their half-unit intervals and supply no rounding explanation of the test mapping. The four-category diagnostic is below .05 and the three-category diagnostic is above .05; neither establishes which analysis was actually performed.

**Necessary inputs available:** All displayed contingency counts, category labels, P attachment, stated test family, significance convention and linked nonsignificant narrative are supplied. They suffice for both stated diagnostics and the unresolved printed result mapping.

**Exact missing inputs or definitions:** Exact tested category set; whether Never was included; exact chi-square implementation, correction and degrees of freedom used in SAS; original analysis output establishing the intended P attribution. No unreported subset, records, stratification, covariance or alternative model is asserted. The package does not establish that every possible chi-square implementation must yield either diagnostic P.

**Source-grounded alternative interpretation:** The main phrase about patients achieving 33°C permits testing the three attained-temperature groups, while the table's merged cell suggests the four displayed groups. Neither Pearson diagnostic yields .09. Another computation or unshown subset could explain .09, but neither is defined in the cited content. The printed P and nonsignificant claim do agree with each other; the unresolved element is their relationship to the supplied counts and method.

**Direct observation versus inferred explanation:** Direct: counts, labels, merged .09, method family and nonsignificant narrative. Reproduced diagnostic: .0433268 or .1604976 under the two explicitly bounded Pearson category readings. Inferred and unestablished: actual software choice, category omission, or another source of the mapping. No causal timing effect or change to the randomized primary treatment contrast is inferred.

**Exact remaining human question:** Which category set, chi-square computation and degrees of freedom produced P = .09, and which displayed favorable-GOS-E timing comparison and nonsignificant statement does that output describe?

**Compared document roles:** REPORT main methods/narrative pp. 4–5 versus REPORT results supplement eTable 7 p. 11; internally, REPORT eTable 7 counts versus P.

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Review domain:** statistical_results

**Classification rationale:** The count/test logic is internal to the results supplement, with its stated method and nonsignificant interpretation in a distinct REPORT document. S_C takes precedence over S_W; no PLAN location supplies a conflicting side.

**Classification ambiguity:** The exact category set and chi-square implementation are missing. This limits numerical reconstruction and leaves the registered result attribution unclear; it does not alter the content-based REPORT roles or statistical_results domain. No classification correction is required.

**Evidence state:** reproduced

**Determining recheck fact:** Exact source counts and .09 match, and both explicitly bounded Pearson diagnostics remain outside the .09 display interval. The state records that bounded diagnostic/result-attribution inconsistency; it does not claim reconstruction of an unspecified original chi-square implementation.

## C004 — Bleeding RR, confidence interval and P attribution

**Location found:** Yes, all six cited pages and both repeated rows were directly reread and freshly rendered. This is one pattern retaining both bleeding outcomes and all contextual occurrences.

| Exact supplied-source location | Role by content | Source/comparator matched |
|---|---|---|
| [Main PDF p. 1, abstract Results; printed p. 2211](../../../jama_cooper_2018_oi_180132.pdf#page=1) | REPORT: completed-trial abstract safety result | Increased intracranial bleeding 18.1% versus 15.4%, H versus N. No RR/CI/P for bleeding is printed here. |
| [Main PDF p. 3, Outcomes and Statistical Analysis; printed p. 2213](../../../jama_cooper_2018_oi_180132.pdf#page=3) | REPORT: trial outcomes and analysis specification | Adverse-event window within 10 days of randomization; comparison by unadjusted chi-square equal-proportions tests, with relative risks/risk differences and 95% CIs; randomized groups excluding consent withdrawals. |
| [Main PDF p. 4, Statistical Analysis; printed p. 2214](../../../jama_cooper_2018_oi_180132.pdf#page=4) | REPORT: analysis convention | SAS 9.4; two-sided P < .05; no multiple-comparison adjustment; secondary outcomes exploratory. |
| [Main PDF p. 5, Adverse Events; printed p. 2215](../../../jama_cooper_2018_oi_180132.pdf#page=5) | REPORT: completed-trial adverse-event narrative | Within-10-day intracranial bleeding 18.1% versus 15.4%; cites Table 2 and eTable 6. No independent bleeding RR/CI/P printed here. |
| [Main PDF p. 7, Table 2, both bleeding rows, headers and ITT note; printed p. 2217](../../../jama_cooper_2018_oi_180132.pdf#page=7) | REPORT: completed-trial inferential adverse-event results | Intracranial 47/260 (18.1) versus 37/240 (15.4), RD 2.7 (−3.9 to 9.2), RR 1.23 (0.43–3.5), P .70. Extracranial 8/260 (3.1) versus 6/240 (2.5), RD 0.6 (−2.3 to 3.5), RR 1.17 (0.79–1.74), P .43. |
| [Results-supplement PDF p. 10, eTable 6, cerebral/non-cerebral bleeding rows and arm headers; printed appendix p. 9](../../../joi180132supp2_prod.pdf#page=10) | REPORT: completed-trial adverse-event results | H/N headers n = 260/240; intracranial 47 (18.1) versus 37 (15.4), P .43; extracranial 8 (3.1) versus 6 (2.5), P .70. No RR/CI block is supplied in eTable 6. |

**Source value/text matched:** Yes, each Table 2 count, percentage, difference, interval, RR and P, its row alignment and 95% confidence header match the ledger. Intracranial upper RR limit is printed 3.5, with one decimal. It was not normalized to two decimals. The abstract and narrative percentage repetitions also match.

**Comparator matched:** Yes. Identical named bleeding outcomes and arm count pairs appear in eTable 6, with explicit n = 260/240 headers and the opposite P assignments. The main unadjusted adverse-event method applies; the separately named adjusted primary-outcome model is not applied to these bleeding rows.

**Consistency rule applicable:** The explicitly unadjusted H-versus-N risk ratio equals (H event count/H denominator)/(N event count/N denominator). Identically matched outcomes and event sets under one stated analysis should have compatible outcome-specific P assignments. CI/test diagnostics may illuminate the pattern, but an unprinted CI estimator cannot be reconstructed solely from convention.

**Calculation or logical comparison reproduced:** Yes. Independently recomputed intracranial RR = (47/260)/(37/240) = 1.172557173, outside its printed 1.23 interval [1.225,1.235). Extracranial RR = (8/260)/(6/240) = 1.230769231, outside its printed 1.17 interval [1.165,1.175). Counts are exact, not half-unit continuous inputs. Intracranial risks 18.076923% and 15.416667% round to 18.1% and 15.4%; their difference 2.660256 percentage points rounds to 2.7. Extracranial risks 3.076923% and 2.5% give difference .576923 percentage points, rounding to .6. Thus counts, percentages and risk differences retain their count-consistent outcome assignments.

Even using only rounded intracranial percentages, permissible RR is bounded by 18.05/15.45 to 18.15/15.35 = 1.168285 to 1.182410, disjoint from the printed 1.23 interval. Rounded extracranial percentages allow RR from 3.05/2.55 to 3.15/2.45 = 1.196078 to 1.285714, disjoint from the printed 1.17 interval. Source P .70 allows [.695,.705), while .43 allows [.425,.435); the same outcome's main and supplementary intervals do not overlap. This cross-source mismatch does not depend on test implementation.

For diagnostic Pearson two-arm checks, pooled p = (a+b)/(n+m) and chi-square = (a/n−b/m)² / [p(1−p)(1/n+1/m)]. Intracranial statistic .631871801 gives df 1 P ≈ .4266694; extracranial .152625153 gives P ≈ .6960393. These align with the supplementary P assignments, but they do not substitute for original output. Diagnostic log-Wald 95% intervals using SE(log RR) = sqrt(1/a−1/n+1/b−1/m) are .791181–1.737769 and .433345–3.495582. They fit the opposite main rows' printed endpoint precision: [.785,.795), [1.735,1.745) for .79–1.74 and [.425,.435), [3.45,3.55) for .43–3.5. Exact CI implementation is not supplied; this interval resemblance supports a possible exchanged block but is not an independent source-authorized reassignment.

**Necessary inputs available:** Every event count and denominator, treatment direction, relative-risk label, explicit unadjusted method, 95% confidence level, two-sided significance convention, adverse-event window and matched supplementary row is available. These establish the RR identity and cross-source P discrepancy without raw data or a preferred CI method.

**Exact missing inputs or definitions:** Original outcome-specific adverse-event inferential output, exact CI construction, and any disclosed alternative analysis population/computation explaining Table 2's inferential blocks. The supplement supplies no independent RR/CI block. Its counts and P cannot alone authorize a final complete replacement block.

**Source-grounded alternative interpretation:** The paired RR/CI/P blocks may have exchanged row attribution while counts and risk differences remained on their count-consistent rows. An undisclosed different computation might instead explain some components. The supplied table does not identify a different population or adjusted adverse-event model. Neither explanation is asserted as established.

**Direct observation versus inferred explanation:** Direct: both complete main bleeding rows, matching supplementary count rows, disjoint P attachments, and unadjusted methods. Reproduced arithmetic: unadjusted risk-ratio identities do not match their own printed rows. Diagnostic: Pearson P and log-Wald interval resemblance to opposite rows. Inferred and unestablished: how the pattern arose and which complete inferential output is authoritative. Both printed P values remain nonsignificant, and no change to the neurologic primary conclusion is asserted.

**Exact remaining human question:** Which RR, 95% CI and P value belong to each 10-day intracranial and extracranial bleeding outcome in the original adverse-event output, given the matching counts, count-consistent risk differences and supplementary P attachments?

**Compared document roles:** REPORT main Table 2 versus REPORT main methods/counts, and REPORT main Table 2 versus REPORT results supplement eTable 6; abstract/narrative are REPORT corroboration of intracranial event rates.

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Review domain:** statistical_results

**Classification rationale:** The main within-report count/estimate incompatibility is S_W; the directly conflicting P attachments across two completed-trial REPORT documents are S_C. S_C has precedence over S_W. Counts, estimates, intervals and tests require statistical_results even though outcome-specific attribution is also implicated. No PLAN location is a conflicting comparator.

**Classification ambiguity:** None regarding roles, precedence or review domain. Original output and CI implementation remain missing evidence inputs rather than classification ambiguity. No classification correction is required.

**Evidence state:** reproduced

**Determining recheck fact:** Fresh visual reading confirms both complete rows and the reversed supplementary P attachments; exact unadjusted RRs remain outside their own displayed half-unit intervals. Every repeated location is retained under one ID.

Completion: C001, C002, C003 and C004 each have all cited locations found, classification confirmed and exactly one evidence state. Four reproduced; zero reproduced_after_transcription_correction; zero not_reproduced. No source-value or page transcription correction was needed. Remaining human questions concern operative duration attribution, the intended quantile summary, timing-test category/implementation mapping and original bleeding inferential output. All IDs remain Pending Human Adjudication.
