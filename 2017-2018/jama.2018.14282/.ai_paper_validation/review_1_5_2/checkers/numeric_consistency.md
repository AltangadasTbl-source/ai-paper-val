# Numeric consistency review

## Scope, approach, and decision convention

Complete review of the frozen canonical numeric inventory, N001--N054, against the fresh mapping parts, extraction artifacts, and direct source PDFs. I applied arithmetic, mutually-exclusive subtotal, count/denominator/percentage, flow, rounding, scale/unit, population, rate-versus-count, repeated-value, and cross-location numeric checks where the printed evidence supplied a compatible identity. A displayed percentage was assessed against the displayed count and named `n = 388` denominator using nearest one-decimal rounding: a printed one-decimal percentage represents an interval of plus/minus 0.05 percentage points (before any unresolved source-specific rounding convention). No statistical inferential compatibility was used as a substitute for the separate statistical pass.

All provisional checker candidates below have status **Pending Human Adjudication**. They are observations for ledger registration; they are not C IDs, severity assignments, or dispositions.

## Explicit outcome record for every assigned relationship

| Canonical ID | Outcome | Checks completed and direct locations |
|---|---|---|
| N001 | PASS_NO_CANDIDATE | Enrollment/completion distinction reconciles: 778 randomized = 389+389 and 776 completed = 388+388; two withdrawal exclusions explain the different populations. DOC-001 pp.1,3,5. |
| N002 | PASS_NO_CANDIDATE | 1464-686=778; 524+95+67=686. DOC-001 p.3, Figure 1. |
| N003 | PASS_NO_CANDIDATE | Each arm: allocated plus not allocated =389; primary analysis 388 plus consent withdrawal exclusion =389; no loss to follow-up. DOC-001 p.3, Figure 1. |
| N004 | NO_APPLICABLE_NUMERIC_IDENTITY | Setting/time/population labels have no arithmetic comparator. DOC-001 pp.1-2. |
| N005 | PASS_NO_CANDIDATE | Eligibility thresholds retain coherent units (years, mm Hg, %, breaths/min, L/min); no reported result identity. DOC-001 p.2. |
| N006 | PASS_NO_CANDIDATE | Treatment thresholds and units are internally labelled; no incompatible quantity or rate/count substitution. DOC-001 pp.2-3. |
| N007 | PASS_NO_CANDIDATE | Outcome windows and stated scales/directions are coherent; no displayed values to sum. DOC-001 p.3. |
| N008 | PASS_NO_CANDIDATE | 259/778=33.29%, compatible with 33.3%; abstract respiratory values match the table. DOC-001 pp.1,5. |
| N009 | CANDIDATES_NC001_NC002 | Sex counts sum to 388 per arm. High-flow percentages reconcile; standard-arm 247 and 141 percentages do not meet the stated one-decimal tolerance. DOC-001 p.4, Table 1. |
| N010 | CANDIDATES_NC003_NC005 | Count/388 checks applied to each comorbidity. Most reconcile; three printed percentages do not. DOC-001 p.4, Table 1. |
| N011 | CANDIDATE_NC006 | Cancer components sum (167+127=294; 181+138=319); one nontransplant percentage does not reconcile to 98/388. DOC-001 p.4, Table 1. |
| N012 | PASS_NO_CANDIDATE | 221/294, 228/319, 26/167, 22/181, 28/167, 33/181 and poor-performance counts/388 reconcile after one-decimal rounding. DOC-001 p.4, Table 1. |
| N013 | CANDIDATES_NC007_NC008 | Four timing counts sum to 388 in both arms. The two `>=3 days` percentages do not reconcile to 20/388 under nearest one-decimal rounding. Postextubation is a separately labelled subgroup, not added. DOC-001 p.4. |
| N014 | CANDIDATES_NC009_NC013 | Goals-of-care counts each sum to 388 per arm; five printed count/percentage pairs exceed one-decimal tolerance. Other score/range labels have no conflict. DOC-001 p.4, Table 1. |
| N015 | CANDIDATE_NC014 | Respiratory units/scales are coherent. The high-flow `received standard oxygen` percentage does not reconcile to 311/388 under the stated tolerance. DOC-001 p.4. |
| N016 | PASS_NO_CANDIDATE | NIV/high-flow counts and percentages reconcile to 388 per arm. DOC-001 p.4. |
| N017 | PASS_NO_CANDIDATE | Score ranges and component counts are definitions/pooled descriptive lists; they are not stated as mutually exhaustive arm totals. DOC-001 p.4 footnotes. |
| N018 | PASS_NO_CANDIDATE | Mortality counts/388 give 35.6% and 36.1%; repeated abstract, Table 2, and narrative values agree. DOC-001 pp.1,5. |
| N019 | PASS_NO_CANDIDATE | IMV counts/388 reconcile to 38.7% and 43.8%. The displayed risk difference need not equal the crude rounded percentage difference because the source specifies competing-risk estimation; no unsupported re-derivation made. DOC-001 pp.1,5-6. |
| N020 | CANDIDATE_NC015 | Standard infection percentage reconciles; high-flow 39/388 does not reconcile to its printed 10.0% at one decimal. DOC-001 p.5, Table 2. |
| N021 | CANDIDATE_NC016 | ICU mortality pairs reconcile. Standard hospital mortality 162/388 does not reconcile to 41.7% at one decimal. DOC-001 p.5, Table 2. |
| N022 | PASS_NO_CANDIDATE | Medians/IQRs and separately defined mean differences are different estimands; no required equality. DOC-001 pp.1,5-6. |
| N023 | CANDIDATE_NC017 | The same six-hour respiratory-rate comparison is printed with identical estimate/lower CI but different upper CI in abstract vs narrative (-0.2 vs -0.3). DOC-001 pp.1,6. |
| N024 | PASS_NO_CANDIDATE | 32/778=4.11% and 37/778=4.76%; group counts 16+16 and 20+17 reconcile. Etiology counts are not asserted exhaustive. DOC-001 p.5. |
| N025 | PASS_NO_CANDIDATE | 12/388=3.09%, 30/388=7.73%, 14/30=46.67%, and 29.5+23.5+40.6+6.4=100.0%; no incompatible denominator stated. DOC-001 p.5. |
| N026 | PASS_NO_CANDIDATE | Risk-set numbers are an at-risk display, not a participant-flow partition; sequence is nonincreasing within each arm and endpoints are labelled day 30. DOC-001 p.6, Figure 2. |
| N027 | CANDIDATE_NC018 | The two reported counts use overall-trial percentages (153/776 and 31/776) while each is grammatically attributed to an arm; denominator basis needs clarification. Other duration/unit labels are coherent. DOC-001 p.6. |
| N028 | PASS_NO_CANDIDATE | 170/776=21.91% and 135/170=79.41%; reported post-hoc contrasts have no supplied count denominator for further reconciliation. DOC-001 p.6. |
| N029 | PASS_NO_CANDIDATE | ICU-time, oxygen-flow, catecholamine, and diagnosis subgroup denominators and deaths sum to all-patient totals. PaO2/FiO2 and hematologic rows leave unlabelled remainder/missing strata, so no arithmetic contradiction is established. DOC-001 p.7, Figure 3A. |
| N030 | PASS_NO_CANDIDATE | Same subgroup-total checks as N029; complete rows reconcile and incomplete dimensional rows lack a stated exhaustive/missingness rule. DOC-001 p.7, Figure 3B. |
| N031 | NO_APPLICABLE_NUMERIC_IDENTITY | Conclusion contains no new numerical effect. DOC-001 p.8. |
| N032 | NO_APPLICABLE_UNIT | Explicit no-result record. DOC-001 p.9. |
| N033 | PASS_NO_CANDIDATE | Initial-protocol planned sample size: 408x2=816; values are planned, not matched to final results. DOC-002 pp.6-7. |
| N034 | PASS_NO_CANDIDATE | Device/measurement definitions preserve units and do not state a numerical identity. DOC-002 pp.10,122-123. |
| N035 | NO_APPLICABLE_NUMERIC_IDENTITY | Planned outcome list only. DOC-002 pp.38,46-47. |
| N036 | PASS_NO_CANDIDATE | Protocol treatment thresholds are labelled consistently; no reported-result count/rate identity. DOC-002 pp.44-45. |
| N037 | PASS_NO_CANDIDATE | Planned strata/subgroups are definitions, not mutually exclusive reported data. DOC-002 pp.45-46. |
| N038 | PASS_NO_CANDIDATE | Eligibility thresholds/units coherent; no quantitative result identity. DOC-002 pp.42-43. |
| N039 | PASS_NO_CANDIDATE | `1:1`, two factors, and eight allocation lists are not inconsistent: combinations/allocation lists are not claimed to equal two. Centre wording has no concrete reported-number conflict. DOC-002 p.50. |
| N040 | PASS_NO_CANDIDATE | Preliminary cohort splits sum: 76+74+20+8=178. Values are explicitly external/preliminary, not the HIGH trial result. DOC-002 pp.29-30. |
| N041 | NO_APPLICABLE_NUMERIC_IDENTITY | Administrative planned N/duration/blood-draw context only. DOC-002 pp.72-73. |
| N042 | PASS_NO_CANDIDATE | Published-protocol 389x2=778. This planned protocol version is not directly compared to the earlier noninferiority version. DOC-002 pp.90-91. |
| N043 | PASS_NO_CANDIDATE | Eligibility population thresholds/units coherent; no reported numeric identity. DOC-002 p.98. |
| N044 | PASS_NO_CANDIDATE | Planned intervention/discharge thresholds retain coherent units. DOC-002 pp.99-100. |
| N045 | PASS_NO_CANDIDATE | Randomization stratification terms are definitions; no numerical contradiction from `eight lists` or centre wording without a stated count identity. DOC-002 p.99. |
| N046 | NO_APPLICABLE_NUMERIC_IDENTITY | Infection timing/data-collection definitions only. DOC-002 p.101. |
| N047 | PASS_NO_CANDIDATE | 686 is explicitly an interim enrollment date/status, not a final-trial total; no matched-time conflict. DOC-002 p.107. |
| N048 | CANDIDATES_NC019_NC021 | eTable has N=388 per group; each of three displayed count/percentage pairs does not reconcile using nearest one-decimal rounding. The complementary category counts themselves sum (39+349; 46+342). DOC-003 p.2, eTable. |
| N049 | NO_APPLICABLE_NUMERIC_IDENTITY | Cumulative-incidence plot has no printed risk-set/count identity. P-value display was not evaluated as a candidate. DOC-003 p.3. |
| N050 | PASS_NO_CANDIDATE | Repeated/sloped risk-set availability is nonincreasing in each arm. Different panels/time measures are not addable denominators. DOC-003 p.4, eFigure 2A. |
| N051 | PASS_NO_CANDIDATE | Risk sets need not be monotone across the H6/D1 measurement schedule as displayed; no stated participant-flow identity permits treating them as counts remaining in a cohort. No cross-panel addition made. DOC-003 p.4, eFigure 2B. |
| N052 | PASS_NO_CANDIDATE | Comfort-panel availability counts are separately measured outcomes, not a mutually exclusive flow; no stated count/proportion contradiction. DOC-003 p.5, eFigure 3A. |
| N053 | PASS_NO_CANDIDATE | Dyspnea-panel availability counts are separately measured outcomes, not a mutually exclusive flow; no stated count/proportion contradiction. DOC-003 p.5, eFigure 3B. |
| N054 | NO_APPLICABLE_UNIT | Explicit no-result/data-access record. DOC-004 p.1. |

## Provisional checker candidates

### NC001 -- Standard-arm men percentage does not reconcile

- **Status:** Pending Human Adjudication
- **Canonical relationship:** N009
- **Exact source location:** DOC-001, PDF p.4, Table 1, Sex, Standard Oxygen Therapy (n=388): `247 (63.6)`.
- **Printed values and comparator:** Printed count 247 and percentage 63.6%; comparator is `247/388 x 100 = 63.6598%`.
- **Rule/calculation/tolerance:** Nearest one-decimal percentage should be 63.7%; 63.6% differs by 0.0598 percentage points, exceeding 0.05-point tolerance.
- **Direct observation vs inference:** Direct observation is the printed pair and denominator. The rounding discrepancy is derived arithmetic; it does not establish the underlying count is wrong.
- **Alternative interpretation:** The table may use a nonstandard rounding convention or a denominator not fully described despite the column heading.
- **Quality-control relevance:** A count/percentage mismatch can be copied incorrectly into structured evidence extraction.
- **Human question:** What denominator and rounding rule generated 63.6% for 247 patients?

### NC002 -- Standard-arm women percentage does not reconcile

- **Status:** Pending Human Adjudication
- **Canonical relationship:** N009
- **Exact source location:** DOC-001, PDF p.4, Table 1, Sex, Standard Oxygen Therapy (n=388): `141 (36.4)`.
- **Printed values and comparator:** 141/388 x 100 = 36.3402%; printed 36.4%.
- **Rule/calculation/tolerance:** Nearest one-decimal value is 36.3%; difference 0.0598 points exceeds 0.05.
- **Direct observation vs inference:** Printed pair is direct; rounding comparison is derived.
- **Alternative interpretation:** An unstated denominator or nonstandard rounding convention could explain it.
- **Quality-control relevance:** The paired sex distribution appears to preserve a rounded 100% total while individual pair arithmetic differs.
- **Human question:** What denominator and rounding rule generated 36.4% for 141 patients?

### NC003 -- Standard-arm heart-failure percentage does not reconcile

- **Status:** Pending Human Adjudication
- **Canonical relationship:** N010
- **Exact source location:** DOC-001, PDF p.4, Table 1, Heart failure, Standard Oxygen Therapy (n=388): `27 (6.9)`.
- **Printed values and comparator:** 27/388 x 100 = 6.9588%; printed 6.9%.
- **Rule/calculation/tolerance:** Nearest one-decimal value is 7.0%; difference 0.0588 points exceeds 0.05.
- **Direct observation vs inference:** Printed pair direct; rounding comparison derived.
- **Alternative interpretation:** Unstated denominator or source rounding convention.
- **Quality-control relevance:** Baseline proportion extraction could inherit the mismatch.
- **Human question:** What denominator and rounding rule generated 6.9% for 27 patients?

### NC004 -- High-flow liver-disease percentage conflicts with displayed count

- **Status:** Pending Human Adjudication
- **Canonical relationship:** N010
- **Exact source location:** DOC-001, PDF p.4, Table 1, Liver, High-Flow Oxygen Therapy (n=388): `45 (13.3)`.
- **Printed values and comparator:** 45/388 x 100 = 11.5979%; printed 13.3%.
- **Rule/calculation/tolerance:** Nearest one-decimal value is 11.6%; printed percentage differs by 1.7021 points, far beyond 0.05.
- **Direct observation vs inference:** Count, percentage, and denominator are direct. The numerical conflict is derived; no claim is made about which printed item is erroneous.
- **Alternative interpretation:** A denominator different from the labelled arm N, a transcription error, or an unreported population restriction could account for the pair.
- **Quality-control relevance:** This is a concrete baseline denominator/proportion inconsistency.
- **Human question:** Which value (45, 13.3%, or the displayed denominator/population) should be corrected or explained?

### NC005 -- Standard-arm kidney-disease percentage conflicts with displayed count

- **Status:** Pending Human Adjudication
- **Canonical relationship:** N010
- **Exact source location:** DOC-001, PDF p.4, Table 1, Kidney disease, Standard Oxygen Therapy (n=388): `69 (20.4)`.
- **Printed values and comparator:** 69/388 x 100 = 17.7835%; printed 20.4%.
- **Rule/calculation/tolerance:** Nearest one-decimal value is 17.8%; printed percentage differs by 2.6165 points, far beyond 0.05.
- **Direct observation vs inference:** Printed values direct; arithmetic comparison derived.
- **Alternative interpretation:** A different unreported denominator or transcription/column-placement error may explain it.
- **Quality-control relevance:** Concrete baseline denominator/proportion inconsistency.
- **Human question:** Which value (69, 20.4%, or the displayed denominator/population) should be corrected or explained?

### NC006 -- Standard-arm nontransplant immunosuppression percentage does not reconcile

- **Status:** Pending Human Adjudication
- **Canonical relationship:** N011
- **Exact source location:** DOC-001, PDF p.4, Table 1, Non-transplant-related reasons, Standard Oxygen Therapy (n=388): `98 (25.2)`.
- **Printed values and comparator:** 98/388 x 100 = 25.2577%; printed 25.2%.
- **Rule/calculation/tolerance:** Nearest one-decimal value is 25.3%; difference 0.0577 points exceeds 0.05.
- **Direct observation vs inference:** Printed pair direct; rounding comparison derived.
- **Alternative interpretation:** Unstated denominator or nonstandard rounding convention.
- **Quality-control relevance:** Baseline proportion mismatch.
- **Human question:** What denominator and rounding rule generated 25.2% for 98 patients?

### NC007 -- High-flow `>=3 days after ICU admission` percentage does not reconcile

- **Status:** Pending Human Adjudication
- **Canonical relationship:** N013
- **Exact source location:** DOC-001, PDF p.4, Table 1, Randomization, `>=3 days after`, High-Flow (n=388): `20 (5.1)`.
- **Printed values and comparator:** 20/388 x 100 = 5.1546%; printed 5.1%.
- **Rule/calculation/tolerance:** Nearest one-decimal value is 5.2%; difference 0.0546 points exceeds 0.05.
- **Direct observation vs inference:** Direct printed pair; derived rounding comparison.
- **Alternative interpretation:** A rounding policy or denominator other than displayed n=388 may be intended.
- **Quality-control relevance:** Timing-distribution proportion mismatch.
- **Human question:** What denominator and rounding rule generated 5.1% for 20 high-flow patients?

### NC008 -- Standard-arm `>=3 days after ICU admission` percentage does not reconcile

- **Status:** Pending Human Adjudication
- **Canonical relationship:** N013
- **Exact source location:** DOC-001, PDF p.4, Table 1, Randomization, `>=3 days after`, Standard Oxygen (n=388): `20 (5.1)`.
- **Printed values and comparator:** 20/388 x 100 = 5.1546%; printed 5.1%.
- **Rule/calculation/tolerance:** Nearest one-decimal value is 5.2%; difference 0.0546 points exceeds 0.05.
- **Direct observation vs inference:** Direct printed pair; derived rounding comparison.
- **Alternative interpretation:** A rounding policy or denominator other than displayed n=388 may be intended.
- **Quality-control relevance:** Timing-distribution proportion mismatch.
- **Human question:** What denominator and rounding rule generated 5.1% for 20 standard-oxygen patients?

### NC009 -- Standard-arm vasopressor percentage does not reconcile

- **Status:** Pending Human Adjudication
- **Canonical relationship:** N014
- **Exact source location:** DOC-001, PDF p.4, Table 1, Vasopressors at randomization, Standard Oxygen (n=388): `39 (10.0)`.
- **Printed values and comparator:** 39/388 x 100 = 10.0515%; printed 10.0%.
- **Rule/calculation/tolerance:** Nearest one-decimal value is 10.1%; difference 0.0515 points exceeds 0.05.
- **Direct observation vs inference:** Direct printed pair; derived rounding comparison.
- **Alternative interpretation:** Unstated denominator/rounding rule.
- **Quality-control relevance:** Baseline proportion mismatch.
- **Human question:** What denominator and rounding rule generated 10.0% for 39 patients?

### NC010 -- High-flow do-not-intubate percentage does not reconcile

- **Status:** Pending Human Adjudication
- **Canonical relationship:** N014
- **Exact source location:** DOC-001, PDF p.4, Table 1, Goals of care, Do not intubate, High-Flow (n=388): `13 (3.3)`.
- **Printed values and comparator:** 13/388 x 100 = 3.3505%; printed 3.3%.
- **Rule/calculation/tolerance:** Nearest one-decimal value is 3.4%; difference 0.0505 points exceeds 0.05.
- **Direct observation vs inference:** Direct printed pair; derived rounding comparison.
- **Alternative interpretation:** Unstated denominator/rounding rule.
- **Quality-control relevance:** Care-limitation baseline proportion mismatch.
- **Human question:** What denominator and rounding rule generated 3.3% for 13 patients?

### NC011 -- High-flow do-not-resuscitate percentage does not reconcile

- **Status:** Pending Human Adjudication
- **Canonical relationship:** N014
- **Exact source location:** DOC-001, PDF p.4, Table 1, Goals of care, Do not resuscitate, High-Flow (n=388): `3 (0.7)`.
- **Printed values and comparator:** 3/388 x 100 = 0.7732%; printed 0.7%.
- **Rule/calculation/tolerance:** Nearest one-decimal value is 0.8%; difference 0.0732 points exceeds 0.05.
- **Direct observation vs inference:** Direct printed pair; derived rounding comparison.
- **Alternative interpretation:** Unstated denominator/rounding rule.
- **Quality-control relevance:** Care-limitation baseline proportion mismatch.
- **Human question:** What denominator and rounding rule generated 0.7% for 3 patients?

### NC012 -- Standard-arm do-not-resuscitate percentage does not reconcile

- **Status:** Pending Human Adjudication
- **Canonical relationship:** N014
- **Exact source location:** DOC-001, PDF p.4, Table 1, Goals of care, Do not resuscitate, Standard Oxygen (n=388): `1 (0.2)`.
- **Printed values and comparator:** 1/388 x 100 = 0.2577%; printed 0.2%.
- **Rule/calculation/tolerance:** Nearest one-decimal value is 0.3%; difference 0.0577 points exceeds 0.05.
- **Direct observation vs inference:** Direct printed pair; derived rounding comparison.
- **Alternative interpretation:** Unstated denominator/rounding rule.
- **Quality-control relevance:** Care-limitation baseline proportion mismatch.
- **Human question:** What denominator and rounding rule generated 0.2% for 1 patient?

### NC013 -- Standard-arm unknown-goals percentage does not reconcile

- **Status:** Pending Human Adjudication
- **Canonical relationship:** N014
- **Exact source location:** DOC-001, PDF p.4, Table 1, Goals of care, Unknown, Standard Oxygen (n=388): `27 (6.9)`.
- **Printed values and comparator:** 27/388 x 100 = 6.9588%; printed 6.9%.
- **Rule/calculation/tolerance:** Nearest one-decimal value is 7.0%; difference 0.0588 points exceeds 0.05.
- **Direct observation vs inference:** Direct printed pair; derived rounding comparison.
- **Alternative interpretation:** Unstated denominator/rounding rule.
- **Quality-control relevance:** Baseline distribution mismatch.
- **Human question:** What denominator and rounding rule generated 6.9% for 27 patients?

### NC014 -- High-flow standard-oxygen-use percentage does not reconcile

- **Status:** Pending Human Adjudication
- **Canonical relationship:** N015
- **Exact source location:** DOC-001, PDF p.4, Table 1, `Received standard oxygen therapy before randomization`, High-Flow (n=388): `311 (80.1)`.
- **Printed values and comparator:** 311/388 x 100 = 80.1546%; printed 80.1%.
- **Rule/calculation/tolerance:** Nearest one-decimal value is 80.2%; difference 0.0546 points exceeds 0.05.
- **Direct observation vs inference:** Direct printed pair; derived rounding comparison.
- **Alternative interpretation:** Unstated denominator/rounding rule.
- **Quality-control relevance:** Baseline-treatment proportion mismatch.
- **Human question:** What denominator and rounding rule generated 80.1% for 311 patients?

### NC015 -- High-flow ICU-acquired-infection percentage does not reconcile

- **Status:** Pending Human Adjudication
- **Canonical relationship:** N020
- **Exact source location:** DOC-001, PDF p.5, Table 2, ICU-acquired infection, High-Flow (n=388): `39 (10.0)`.
- **Printed values and comparator:** 39/388 x 100 = 10.0515%; printed 10.0%.
- **Rule/calculation/tolerance:** Nearest one-decimal value is 10.1%; difference 0.0515 points exceeds 0.05.
- **Direct observation vs inference:** Direct count/percentage/arm n; derived arithmetic. It does not determine whether the count, percentage, or denominator definition needs change.
- **Alternative interpretation:** The infection proportion may use an unstated at-risk or competing-event population, though Table 2 labels the arm `n=388` and `No. (%)`.
- **Quality-control relevance:** Outcome proportion mismatch could affect evidence extraction.
- **Human question:** Does the ICU-infection percentage use an unstated denominator, and if not should 10.0% be 10.1%?

### NC016 -- Standard-arm hospital-mortality percentage does not reconcile

- **Status:** Pending Human Adjudication
- **Canonical relationship:** N021
- **Exact source location:** DOC-001, PDF p.5, Table 2, Hospital mortality, Standard Oxygen (n=388): `162 (41.7)`.
- **Printed values and comparator:** 162/388 x 100 = 41.7526%; printed 41.7%.
- **Rule/calculation/tolerance:** Nearest one-decimal value is 41.8%; difference 0.0526 points exceeds 0.05.
- **Direct observation vs inference:** Printed pair direct; rounding comparison derived.
- **Alternative interpretation:** An unstated denominator or rounding convention could be used.
- **Quality-control relevance:** Mortality outcome proportion mismatch.
- **Human question:** What denominator and rounding rule generated 41.7% for 162 patients?

### NC017 -- Respiratory-rate confidence-interval upper limit differs between matched occurrences

- **Status:** Pending Human Adjudication
- **Canonical relationship:** N023
- **Exact source locations:** DOC-001 PDF p.1 abstract: `-1.8/min [95% CI, -3.2 to -0.2]`; DOC-001 PDF p.6 secondary-outcomes narrative: `mean difference, -1.8 [95% CI, -3.2 to -0.3]` for respiratory rate at six hours, 25/min vs 26/min.
- **Printed values and comparator:** Same population/time/contrast/estimate/lower endpoint; differing upper endpoints -0.2 versus -0.3 per min.
- **Rule/calculation/tolerance:** Matched repeated numeric results should agree at the displayed precision. Difference is 0.1/min, one printed last-place unit; no rounding tolerance bridges two values both printed to one decimal.
- **Direct observation vs inference:** Both strings are direct observations; matching them as the same result is supported by identical comparison/time/estimate and is an inference stated here.
- **Alternative interpretation:** One occurrence may have been rounded from a more precise interval differently, or the two calculations may have an unreported distinction.
- **Quality-control relevance:** A repeated secondary-effect interval could be copied inconsistently.
- **Human question:** Which upper 95% CI endpoint is the intended six-hour respiratory-rate result, and are the analyses identical?

### NC018 -- Arm-attributed support-needs percentages use the overall-trial denominator

- **Status:** Pending Human Adjudication
- **Canonical relationship:** N027
- **Exact source location:** DOC-001, PDF p.6, Post Hoc Outcomes: `vasopressors and renal replacement therapy were needed in 153 patients (19.7%) randomized to high-flow oxygen therapy and 31 patients (4.0%) randomized to standard oxygen therapy`.
- **Printed values and comparator:** 153/776=19.7% and 31/776=4.0%, whereas counts attributed to their 388-person arms would be 39.4% and 8.0%, respectively.
- **Rule/calculation/tolerance:** The printed percentages exactly use the combined completed-trial denominator 776, not either named arm denominator 388. A percentage attached to an arm-labelled count normally requires an explicit denominator basis; this is a denominator/label observation, not a claim that the counts are false.
- **Direct observation vs inference:** The sentence and arithmetic are direct/derived respectively. The ambiguity about intended presentation is unresolved.
- **Alternative interpretation:** Authors may intentionally report each arm's count as a percentage of all 776 completers; the text lacks an explicit overall-denominator label.
- **Quality-control relevance:** A data extractor can mistakenly treat 19.7% and 4.0% as within-arm risks.
- **Human question:** Were 19.7% and 4.0% intentionally calculated over all 776 patients, and should the denominator be stated or arm-specific percentages reported?

### NC019 -- eTable high-flow invasive-MV percentage does not reconcile

- **Status:** Pending Human Adjudication
- **Canonical relationship:** N048
- **Exact source location:** DOC-003, PDF p.2, eTable, High-flow oxygen therapy (N=388), Invasive mechanical ventilation: `39 (10.0)`.
- **Printed values and comparator:** 39/388 x 100 = 10.0515%; printed 10.0%.
- **Rule/calculation/tolerance:** Nearest one-decimal result is 10.1%; difference 0.0515 points exceeds 0.05.
- **Direct observation vs inference:** Direct eTable pair; derived rounding comparison.
- **Alternative interpretation:** An unstated denominator or rounding convention could account for the display.
- **Quality-control relevance:** Six-hour intervention-event percentage mismatch.
- **Human question:** What denominator and rounding rule generated 10.0% for 39 high-flow participants?

### NC020 -- eTable standard-arm invasive-MV percentage does not reconcile

- **Status:** Pending Human Adjudication
- **Canonical relationship:** N048
- **Exact source location:** DOC-003, PDF p.2, eTable, Standard Oxygen (N=388), Invasive mechanical ventilation: `46 (11.8)`.
- **Printed values and comparator:** 46/388 x 100 = 11.8557%; printed 11.8%.
- **Rule/calculation/tolerance:** Nearest one-decimal result is 11.9%; difference 0.0557 points exceeds 0.05.
- **Direct observation vs inference:** Direct eTable pair; derived rounding comparison.
- **Alternative interpretation:** Unstated denominator or rounding convention.
- **Quality-control relevance:** Six-hour intervention-event percentage mismatch.
- **Human question:** What denominator and rounding rule generated 11.8% for 46 standard-oxygen participants?

### NC021 -- eTable standard-oxygen-only percentage does not reconcile

- **Status:** Pending Human Adjudication
- **Canonical relationship:** N048
- **Exact source location:** DOC-003, PDF p.2, eTable, Standard Oxygen (N=388), Standard oxygen only: `342 (88.2)`.
- **Printed values and comparator:** 342/388 x 100 = 88.1443%; printed 88.2%.
- **Rule/calculation/tolerance:** Nearest one-decimal result is 88.1%; difference 0.0557 points exceeds 0.05.
- **Direct observation vs inference:** Direct eTable pair; derived rounding comparison.
- **Alternative interpretation:** An unstated denominator or nonstandard rounding convention could account for the display.
- **Quality-control relevance:** Six-hour support-use percentage mismatch.
- **Human question:** What denominator and rounding rule generated 88.2% for 342 standard-oxygen participants?

## Limitations

- This lane did not perform the two mandatory inferential-statistical passes; it only recorded numeric identities and one matched repeated-value observation.
- Several one-decimal discrepancies are small and may reflect a source-specific rounding convention or an unstated denominator. They remain candidate observations rather than corrections.
- Risk-set displays in the supplement do not state a participant-flow/missingness mechanism sufficient to treat all time-point availability counts as a single decreasing denominator.
- Protocol versions intentionally differ in planned sample size, framework, and targets; they were not treated as conflicting reported results.

**Coverage:** 54/54 canonical N IDs. **Provisional checker candidates:** 21 (NC001--NC021). **No display-zero-only candidate was emitted.**
