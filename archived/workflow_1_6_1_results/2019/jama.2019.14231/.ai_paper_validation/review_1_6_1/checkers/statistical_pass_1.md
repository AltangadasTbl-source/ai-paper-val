# Statistical consistency review — pass 1

Runtime agent: `/root/statistics_one`. Fresh preset `qc161_statistical_consistency_reviewer`, model `gpt-6.1-sol`, reasoning effort `high`. Exact scope: S001,S002,S003,S004,S005,S006,S007,S008,S009,S010,S011,S012,S013,S014,S015,S016,S017,S018,S019,S020,S021,S022,S023,S024,S101,S102,S103,S104,S105,S106,S107,S108,S109,S110,S111,S112,S113,S114,S115,S116,S117,S118,S119,S120,S121,S122,S123,S124,S125,S126. All50 groups and all underlying members receive `PASS_1_COMPLETE` in [relationship inventory](../statistics/relationship_inventory.md).

The full scope and review contract were read. Source-grounded containment, interval order, direction, estimate/test logic, PH and subgroup tests, multiplicity and method logic, planned/reported design, risk sets, and sensitivity implications were reviewed. No sample-size/power inputs, noninferiority/equivalence margin, interim, or stopping rule is supplied. There is one consolidated finding and17 consolidated excluded observations. No candidate IDs or human adjudication fields are assigned here.

## Findings

### F-ST1-001

**Title:** Five individual-outcome absolute eight-year risk differences do not reconcile with the stated Kaplan–Meier risk contrast.

**Relationships:** S004,S005,S006,S007,S008, with corroborating mapped family S104. **Focus area:** B (estimate identity) and C (analysis specification). **Proposed review domain:** `statistical_results`. **Proposed relationship type:** `S_W`; all relationships `S_W`. The supplement repeats the same group-specific KM risks and corroborates one side; it does not independently add a conflicting analysis.

**Exact compared locations and roles:** REPORT main article [Statistical Analysis, physical PDF p.4](../../../jama_aminian_2019_oi_190103.pdf#page=4) states that Kaplan–Meier cumulative incidence estimates for eight years and absolute risk differences were calculated, with percentile intervals from1000bootstrap iterations; REPORT main article [Table2, physical p.7, five named individual-outcome rows and footnote a](../../../jama_aminian_2019_oi_190103.pdf#page=7) labels the contrast as the difference in eight-year absolute risk, nonsurgical control minus metabolic surgery. REPORT [Figure3, physical p.8](../../../jama_aminian_2019_oi_190103.pdf#page=8) displays the corresponding group curves. REPORT results supplement [eTable5, physical p.7, same five rows, Year8 surgical/nonsurgical columns](../../../joi190103supp1_prod.pdf#page=7) prints the same group risks. Main Table2 values and footnote were visually confirmed from the fresh direct-source page7 render; direct native/layout text agrees.

**Printed values, rule and reproduced calculation:** Under the stated control-minus-surgery risk contrast, subtract the two KM eight-year point estimates in percentage points. Allow each printed one-decimal risk and ARD its half-unit rounding interval,±.05percentage points. The arithmetic difference therefore spans the printed difference±.10; the reportedARD spans its printed value±.05. These sets do not overlap in any affected row.

| Table2 outcome | SurgicalKM8y % | NonsurgicalKM8y % | PrintedARD % (95%CI) | Nonsurgical minus surgery | Difference interval from rounding | PrintedARD rounding interval |
|---|---:|---:|---|---:|---|---|
| Heart failure |6.8|18.9|12.9(10.4,15.1)|12.1|[12.0,12.2]|[12.85,12.95]|
| Coronary artery disease |7.9|11.6|4.2(1.9,6.8)|3.7|[3.6,3.8]|[4.15,4.25]|
| Cerebrovascular disease |4.1|5.6|1.8(−.03,3.4)|1.5|[1.4,1.6]|[1.75,1.85]|
| Nephropathy |6.1|16.3|11.1(8.8,13.6)|10.2|[10.1,10.3]|[11.05,11.15]|
| Atrial fibrillation |7.9|13.6|6.5(4.4,8.7)|5.7|[5.6,5.8]|[6.45,6.55]|

The three remaining rows reconcile under subtraction: primary47.7−30.8=16.9, secondary27.6−17.0=10.6, mortality17.8−10.0=7.8. Every affected reportedARD lies within its own printed bootstrapCI, so this finding concerns the point-contrast identity rather than interval containment. No conditional Wald calculation or external method is required.

**Affected result or extracted value:** The eight-year absolute risk differences for heart failure, coronary artery disease, cerebrovascular disease, nephropathy, and atrial fibrillation. A data extractor can take the printedARD or derive a different point contrast from the displayed group risks; these are not interchangeable values at reported precision.

**Why context does not resolve it:** The table presents the group risks and absolute differences together, and the methods and footnote expressly identify control-minus-surgery eight-year risks. Bootstrap iterations are stated to produce the intervals; neither the table nor methods identifies a separate point estimator, adjusted-risk model, or different event/censoring rule for these five contrasts. Fully adjustedCoxHRs are labeled separately, so their adjustment cannot silently supply an alternative absolute-risk estimand. The source repeats the same KM values without choosing which quantities should govern the difference.

**Source-grounded alternatives and missing definition:** One alternative is that the ARDs come from another unstated point estimator, such as a bootstrap-derived summary rather than subtraction of the displayed original KM estimates. Another is that an unstated analysis-specific risk set or censoring definition applies to the ARDs. The supplied text establishes neither alternative and supplies no separate risks for such an estimator. The observation does not identify which printed value should be changed and does not challenge the adjustedHR analysis.

**Exact human question:** Which point estimator, eight-year group risks, and risk-set/censoring definition produced each of the five Table2 absolute risk differences, and how do those quantities relate to the adjacent Kaplan–Meier estimates?

## Excluded observations

Each row consolidates one observation/pattern and uses exactly one reason code. Reconciled ordinary relationships are documented in the inventory rather than inflated into excluded items. None is emitted as a finding.

| Location | Observation | Reason code |
|---|---|---|
| REPORT main Table2 p.7; methods p.4 | AdjustedHRs differ from crude observed-event ratios, KM-risk ratios, or rate ratios. They are expressly fully adjusted Cox estimates and use time-to-event data. | MODEL_VERSUS_CRUDE |
| REPORT main p.7 Table2 cerebrovascular row; p.8Figure3D | HR95%CI(.48,.94)/P=.02 excludes null while bootstrapARD95%CI(−.03,3.4) includes zero. AdjustedCox treatment test and fixed-time KM risk contrast are separate supplied analyses, so no identical-test contradiction follows. | CONTEXT_RESOLVES |
| REPORT main p.7 weight paragraph; p.9Figure4; supplement p.12eTable8 |29.1−8.7=20.4kg vs reported20.3kg: input rounding gives difference[20.30,20.50], overlapping reported20.3 interval[20.25,20.35].95%vs98.8% CIs and positive-reduction versus negative-change direction also reconcile. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT supplement p.12eTable8 hemoglobin5y |−.1(−.2,0), P<.001 is not reproduced as a contradiction after precision allowance. Diagnostic normal example: point−.149 and98.8% endpoints−.249/−.049 produce an approximate z3.74 and two-sidedP<.001 while rounding to the displayed cells; exact model SE/df unspecified. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT supplement p.12eTable8 protein/albumin and other one-decimal cells | Identical printed point and interval endpoints do not imply a zero-width interval before rounding; microscopic positive widths can be concealed. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT supplement p.12eTable8 other-antihypertensive1y |P=.02 with corrected98.8%CI(−5.6,.3) crossing zero is compatible with an unadjustedP and aBonferroni-correctedCI. No adjustedP label is supplied; asterisks are not a separately defined rule. | CONTEXT_RESOLVES |
| REPORT main pp.4,10Figure5; supplement p.12eTable8 | Generic “two-sample proportions test” versus caption-specific “Fisher exact test” does not establish which alternative named software routine was used; the figure supplies its test. Numerators and exact CI construction are absent. No source-established incompatible numerical test is reproduced. | TERMINOLOGY_OR_WORDING |
| REPORT main p.4; supplement pp.10,19 | A restricted spline on “observed follow-up time” could be read as a terminal-time baseline covariate rather than a time-varying coefficient, but the sources describe the latter aim. Exact implementation absent; the former reading is an unsupported assumption. | CONDITIONAL_OR_UNREPORTED |
| REPORT main p.4; supplement pp.12–13 | Spline longitudinal intervals appear narrow in a repeated-observation setting; sources do not specify covariance/variance estimator or give numericalSEs. Repeated measurements alone do not establish independent-observation treatment or a contradicted step. | CONDITIONAL_OR_UNREPORTED |
| REPORT supplement pp.19–20; PLANp.7 | E-values could be recomputed by assuming one HR-to-risk-ratio conversion, but no conversion formula/inputs are supplied. Different treatment of common/rare endpoints cannot be established from conventions alone. | CONDITIONAL_OR_UNREPORTED |
| REPORT supplement p.19E-value prose | “5-component MACE” occurs in explanatory prose whose same paragraph identifies primaryHR.61(.55,.69) and E-value2.15. The surrounding primary definition and table identify the result at once as the six-component primary endpoint. | TERMINOLOGY_OR_WORDING |
| PLANpp.3,6; REPORT main pp.3–4 and supplement p.18 | One plan sentence reverses the matching-group orientation; figure legend5:1/10:1 versus text1:5/1:10 reverses notation convention. The cohort counts and repeated control-derivation description immediately identify five controls per surgery and sensitivity ratios. | CONTEXT_RESOLVES |
| PLANpp.5–6; REPORT main pp.4–6 | Collected fields insurance/creatinine lack separate Table1 covariate rows. Collection list does not explicitly map every raw field to a separate Cox covariate; creatinine deriveseGFR and date of birth maps toage. A changed adjustment set requires an unprovided plan-to-model mapping rather than merely the absent rows. | CONDITIONAL_OR_UNREPORTED |
| REPORT main pp.5,7; PLANp.5 | Nephropathy risk sets do not equal cohort minus the Table1 history-only nephropathy row. Plan expressly adds baselineeGFR<60/dialysis exclusions; overlapping individual exclusion counts absent. | CONTEXT_RESOLVES |
| REPORT main p.4; PLANp.6; supplement p.12 | Plan says secondary endpoint multiplicity adjustment not performed; eTable8 has corrected longitudinal intervals. Seven secondary endpointHRs remain exploratory and unadjusted; longitudinal “other outcomes” are distinct from those endpoints. | CONTEXT_RESOLVES |
| REPORT main p.7; PLANp.7 | “Within90days” vs “early<90days” safety wording does not identify any boundary-day events or changed quantitative result. No separate boundary-day count is supplied. | CONDITIONAL_OR_UNREPORTED |
| REPORT main pp.5–6Table1 footnote | “Absolute value” standardized-difference description accompanies signed cells. Signs are immediately read as surgery-minus-control direction; this does not change any primary/key result, analysis-population size, or planned decision rule. | PERIPHERAL_COMPARISON |

## Diagnostic limits and completed checks

Every printed main/supplement point estimate is inside its stated interval and every lower endpoint precedes its upper endpoint. All eight endpointHRs and theirP values support their printed direction and alpha.05 inference. The main sevensecondary endpoint conclusions remain explicitly exploratory. All48 outcomeKM triples,16subgroupHRs,24time-varyingHRs,24interventionKM triples,52longitudinal triplets,16E-values,40risk-factorHRs, and120graphical sensitivity pairs were covered, as well as their repeats and all stated planning specifications.

Approximate log-Wald diagnostics for CAD,cerebrovascular,AF give P values near.002,.02,.03 from the displayed95%HR limits. Those are diagnostics only: the exact pooled-imputation statistic, numericalSE, degrees of freedom, and coefficient-test identity are not supplied. Similarly, no exact interaction test can be reconstructed from two marginal subgroupCIs without covariance; no medication test can be reconstructed without numerator counts and the precise routine; no longitudinal test can be reconstructed without variance/df details. Those unavailable reconstructions did not cause omitted relationships and do not establish method findings.

Tools were direct CPU-only Poppler (`pdftotext`), source-matched page images via `view_image`, and local artifact reads. No source/reused artifact was modified. No fallback tool capability was needed. The inventory leaves every pass2 record pending for the distinct fresh statistical reviewer.
