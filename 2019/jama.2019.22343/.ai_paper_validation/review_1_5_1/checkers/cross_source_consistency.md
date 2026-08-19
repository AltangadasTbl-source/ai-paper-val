# Cross-Source Consistency Check

## Scope and method

This checker independently compared the source-linked current-run maps and all four
provisional relationship inventories: main numeric relationships MN001-MN013, main
statistical relationships MS001-MS043, support numeric relationships SN001-SN014,
and support statistical relationships SS001-SS014.  Direct PDF text was checked again
at each location used below.  The direct sources were [DOC-001 main article](../../../jama_wilson_2020_oi_190154.pdf), [DOC-002 trial protocol](../../../joi190154supp1_prod.pdf), and [DOC-003 results supplement](../../../joi190154supp2_prod.pdf).

A comparison was made only after matching the stated population, time point, contrast,
analysis set, model where stated, effect measure, scale/unit, reference direction, and
printed precision.  A decimal difference is recorded when the matched locations print
different values at the displayed precision; it is not described as a correction.  The
observations below are local checker observations only, have no stable candidate IDs,
and are all pending human adjudication.

## Qualifying candidate observations

### CS-001 — BPAP mortality pooled confidence-interval lower limit differs between the forest plot and repeated summaries

- **Category:** Cross-document numeric inconsistency.
- **Exact linked locations:** [DOC-001 PDF p. 1, abstract](../../../jama_wilson_2020_oi_190154.pdf#page=1); [PDF p. 4, Figure 1](../../../jama_wilson_2020_oi_190154.pdf#page=4); [PDF p. 5, BPAP results narrative](../../../jama_wilson_2020_oi_190154.pdf#page=5).
- **Matched result:** BPAP versus no device, mortality at longest follow-up, 13 studies and 1423 patients, pooled odds ratio.
- **Printed values:** The abstract and p. 5 narrative print OR 0.66 (95% CI, **0.51**-0.87); Figure 1 prints OR 0.66 (95% CI, **0.50**-0.87).  The point estimate, upper limit, population, contrast, study count, and direction agree.
- **Comparison logic:** These are three displays of the same pooled effect at two decimal places.  The lower endpoint differs by 0.01 at the displayed precision.
- **Supported alternative interpretation:** A common unrounded interval endpoint may have been formatted differently in the forest plot and prose/abstract.  The supplied sources do not state a distinct analysis set, model, or confidence-level convention for these displays.
- **Human verification steps:** Inspect the meta-analysis output used for Figure 1 and the abstract/table manuscript values; determine the unrounded lower endpoint and whether one display was manually rounded or transcribed differently.

### CS-002 — BPAP quality-of-life pooled confidence-interval upper limit differs between Figure 4 and repeated summaries

- **Category:** Cross-document numeric inconsistency.
- **Exact linked locations:** [DOC-001 PDF p. 1, abstract](../../../jama_wilson_2020_oi_190154.pdf#page=1); [PDF p. 5, Figure 4](../../../jama_wilson_2020_oi_190154.pdf#page=5); [PDF p. 5, BPAP results narrative](../../../jama_wilson_2020_oi_190154.pdf#page=5).
- **Matched result:** BPAP versus no device, quality of life at longest follow-up, 9 studies and 833 patients, standardized mean difference.
- **Printed values:** The abstract and narrative print SMD 0.16 (95% CI, -0.06 to **0.39**); Figure 4 prints SMD 0.16 (95% CI, -0.06 to **0.38**).  The I2 value (61.7%), heterogeneity P value (.007), point estimate, study count, population, contrast, and stated direction agree.
- **Comparison logic:** The upper confidence limit differs by 0.01 at the printed two-decimal precision for an otherwise identical pooled result.
- **Supported alternative interpretation:** The two locations may have rounded a common unprinted endpoint differently.  No supplied source identifies a different model, follow-up, or analysis population for Figure 4 versus the prose and abstract.
- **Human verification steps:** Reproduce or inspect the stored pooled SMD output and verify which upper endpoint was intended for the forest plot and which for the abstract/narrative.

### CS-003 — Quality-of-life direction statement conflicts with the main analysis standardization rule and the supplement’s instrument-specific directions

- **Category:** Measure, label, or scale inconsistency.
- **Exact linked locations:** [DOC-001 PDF p. 3, Data Synthesis and Analysis](../../../jama_wilson_2020_oi_190154.pdf#page=3); [DOC-001 PDF p. 5, Figure 4](../../../jama_wilson_2020_oi_190154.pdf#page=5); [DOC-001 PDF p. 8, Table 2 footnote b](../../../jama_wilson_2020_oi_190154.pdf#page=8); [DOC-003 PDF p. 15, eTable 3](../../../joi190154supp2_prod.pdf#page=15).
- **Matched result/label:** Quality-of-life standardized mean differences for NIPPV versus no device, including the RCT and observational results in Table 2. The methods state that directions were standardized and higher scores represent **better outcomes**. Figure 4 labels negative SMDs “Favors NIPPV” and positive SMDs “Favors No NIPPV.” Table 2 footnote b states, “Higher scores indicate **worse** quality of life.”
- **Comparison logic:** The standardized direction, SMD sign under the group subtraction, figure favor labels, and table footnote must use one coherent polarity or state distinct contexts. eTable 3 confirms mixed native directions. The package does not state the subtraction order or a reversion to native-scale direction in Table 2.
- **Supported alternative interpretation:** Table 2 may describe selected original scales and Figure 4 may use a control-minus-intervention subtraction orientation. Neither distinction is stated, and the original scales do not share one direction.
- **Human verification steps:** Check the sign-recoding and group-subtraction specification. Confirm the intended Figure 4 favor labels and whether Table 2 footnote b describes native scales, standardized SMD direction, or both.

### CS-004 — The high-versus-low intensity quality-of-life interval differs between the main narrative and eTable 10

- **Category:** Cross-document numeric inconsistency.
- **Exact linked locations:** [DOC-001 PDF p. 7, other-comparisons narrative](../../../jama_wilson_2020_oi_190154.pdf#page=7); [DOC-003 PDF p. 43, eTable 10](../../../joi190154supp2_prod.pdf#page=43).
- **Matched result:** One RCT (reference 25), 14 patients; high-intensity pressure-controlled HMV/BPAP mix versus low-intensity pressure-support HMV/BPAP mix; COPD Assessment Test quality of life; WMD 2.30.
- **Printed values:** The main narrative prints WMD 2.30 (95% CI, **-2.23 to 6.83**; P = .32).  eTable 10 prints WMD 2.30 (95% CI, **-2.35 to 6.95**; I2 = N/A).  Both label the CAT as higher=worse and identify one RCT/14 patients.
- **Comparison logic:** The point estimate, population, contrast, outcome scale, analysis size, and direction match, but both confidence limits differ by 0.12 at the displayed two-decimal precision.
- **Supported alternative interpretation:** The supplement and narrative could have been created from differently rounded or updated single-study calculations.  The package supplies no statement of a different time point, analysis set, or model that would explain the changed interval.
- **Human verification steps:** Inspect the single-study calculation/data-extraction sheet for reference 25, identify the intended confidence interval and its calculation convention, and reconcile both printed displays.

### CS-005 — Cheung 2010 participant total in eTable 6 does not equal the matched eTable 10 effectiveness total

- **Category:** Denominator, proportion, or total inconsistency.
- **Exact linked locations:** [DOC-003 PDF p. 19, eTable 6 Cheung 2010 row](../../../joi190154supp2_prod.pdf#page=19); [DOC-003 PDF p. 43, eTable 10 BPAP versus CPAP row](../../../joi190154supp2_prod.pdf#page=43); [DOC-001 PDF p. 6, BPAP-versus-CPAP narrative](../../../jama_wilson_2020_oi_190154.pdf#page=6).
- **Matched result:** Cheung 2010, reference 17, RCT in China, BPAP-ST versus CPAP, exacerbation outcome.  eTable 10 and the main narrative both identify this comparison as one RCT with 49 patients and print 30.43% versus 53.85%, RD -0.23 (95% CI, -0.50 to 0.03), and OR 0.38 (95% CI, 0.12 to 1.22).
- **Printed values:** eTable 6 lists CPAP **24 patients** and BPAP-ST **23 patients**, for a displayed baseline total of **47**.  The matched eTable 10 and main narrative print **49 patients**.
- **Comparison logic:** 24 + 23 = 47, which is two fewer than the repeated 49-patient effectiveness total.  The author/year, reference number, contrast, disease state, and comparison match; the source does not identify a different analysis population.
- **Supported alternative interpretation:** The 49 may be an enrolled/randomized total while the eTable 6 groups are a baseline or analyzed subset, possibly excluding two participants.  The package does not state that distinction for these two tables.
- **Human verification steps:** Check the Cheung trial extraction and participant-flow records for randomized, baseline, and outcome-analysis denominators.  Confirm whether two participants were omitted from the displayed eTable 6 groups or whether one total was transcribed incorrectly.

### CS-006 — Reported meta-analysis model rule differs from the protocol rule for comparisons with 3 through 18 studies

- **Category:** Statistical reporting inconsistency.
- **Exact linked locations:** [DOC-002 PDF p. 11, Data Synthesis](../../../joi190154supp1_prod.pdf#page=11); [DOC-001 PDF p. 3, Data Synthesis and Analysis](../../../jama_wilson_2020_oi_190154.pdf#page=3); [DOC-001 PDF p. 4, Figures 1 and 2](../../../jama_wilson_2020_oi_190154.pdf#page=4); [DOC-001 PDF p. 5, Figures 3 and 4](../../../jama_wilson_2020_oi_190154.pdf#page=5).
- **Matched method/results:** Both sources describe the meta-analysis rule used for the same review.  The protocol states DerSimonian-Laird random effects if the number of included studies is larger than 18, and otherwise DerSimonian-Laird random effects **with Knapp-Hartung variance adjustment**.  The main article states that DerSimonian-Laird random effects were used except when fewer than 3 studies were included, when fixed-effect Mantel-Haenszel was used.
- **Comparison logic:** The stated rules assign different methods to comparisons containing 3-18 studies: the protocol specifies Knapp-Hartung-adjusted random effects, while the article’s stated exception is only fewer than 3 studies and does not state Knapp-Hartung adjustment.  Several displayed primary pooled results have 3-15 studies (for example, BPAP mortality 13, BPAP admissions 5, BPAP intubation 3, quality of life 9, and combined mortality 15), so this is a concrete model-definition discrepancy affecting reported estimates/intervals rather than a general protocol-design concern.
- **Supported alternative interpretation:** The analysis plan may have been amended or the article’s concise method description may have omitted the Knapp-Hartung adjustment.  The supplied package contains no amendment or explicit statement resolving the difference.
- **Human verification steps:** Review the dated analysis plan and analysis code/output for each 3-18-study synthesis.  Determine whether Knapp-Hartung adjustment was used, whether the protocol rule was formally changed, and which description should accompany the displayed estimates and intervals.

## Diagnostic-only observation without stable candidate registration

### CS-007 — HMV mortality P value diagnostic from rounded estimate and confidence interval

- **Category:** Statistical reporting inconsistency.
- **Exact linked locations:** [DOC-001 PDF p. 1, abstract](../../../jama_wilson_2020_oi_190154.pdf#page=1); [DOC-001 PDF p. 4, Figure 1 HMV subtotal](../../../jama_wilson_2020_oi_190154.pdf#page=4); [DOC-001 PDF p. 6, HMV results narrative](../../../jama_wilson_2020_oi_190154.pdf#page=6).
- **Matched result:** HMV versus no device, mortality at longest follow-up, two observational studies and 175 patients, pooled OR 0.56 (95% CI, 0.29-1.08).  The abstract and narrative print P = .49.  Figure 1 prints the same OR and interval; its P = .01 is explicitly within “I2 = 84.3%; P = .01” and is therefore the heterogeneity P value, not the pooled-effect P value.
- **Comparison logic:** As a diagnostic only, treating the rounded 95% CI as a normal two-sided log-OR interval gives SE about (log(1.08)-log(0.29))/(2 x 1.96) = 0.335 and z about |log(0.56)|/0.335 = 1.73, corresponding to a two-sided P near .08. The source does not supply the exact compatible effect test, variance construction, weights, or continuity rule, so this arithmetic does not meet the stable-candidate threshold and does not replace the reported analysis.
- **Supported alternative interpretation:** The P value may arise from a differently calculated statistic, adjustment, confidence-level convention, or another quantity not identified in the supplied text.  No standard error, effect-test label in the forest plot, or exact pooling variance is supplied.
- **Human verification steps:** Inspect the output for the HMV mortality synthesis and identify the statistic and null hypothesis behind P = .49.  Verify whether the P value, OR/CI, RD/CI, or its location in the abstract/narrative needs reconciliation.

## Checked matched results without a qualifying observation

- **Primary BPAP/no-device results other than CS-001 and CS-002:** mortality point estimate/upper limit, admission-patient risk/OR/RD, intubation, admission-count rate ratio, and study/patient totals agree across the abstract, narrative, Table 1/Figures 1-4 where the same result is printed.  The abstract’s 0.18 versus 0.17 adverse-event rates and the narrative RR 1.08 describe the same direct-comparison rate relationship; the pooled 0.21 incidence is a different all-NIPPV quantity and was not treated as a conflict.
- **HMV/no-device and combined-NIPPV/no-device primary results:** matched mortality and admission-count values agree between the abstract, narrative, Table 1, and relevant forest plot.  The Figure 1 P values are heterogeneity P values and were not compared as pooled-effect P values.
- **Other-comparison results repeated in DOC-001 and eTable 10:** BPAP-volume-assured versus BPAP-ST mortality and all listed WMDs; pressure-controlled versus pressure-support HMV SRIQ/6-minute walk; BPAP duration comparison; home telemedicine versus hospital initiation; and the high/low-intensity point estimate/scale/sample size agree.  CS-004 is limited to the differing high/low-intensity interval.
- **Adherence comparison:** DOC-001 prints 0.4 versus 1.0 per patient and P = .006; DOC-003 prints 0.4 versus 1.0 and P < .01.  The latter is compatible with the former at its stated threshold; DOC-003’s shorter label does not establish rate-versus-count confusion because the main narrative supplies the per-patient unit.
- **Instrument directions:** eTable 10’s native-scale statements for SGRQ, ESS, MRC, and SRIQ agree with eTable 3.  They are not interchangeable with standardized SMD orientation; that distinction is the subject of CS-003.
- **Counts and flow:** DOC-001’s 6,222 citations plus 83 additional citations, 33 studies/34 articles, 21 RCTs/12 observational studies, and 51,085 patients agree with DOC-003 eFigure 1 and the matched supplement tables where applicable.  The HMV-versus-CPAP/BPAP totals 39,700 and 9,471 reconcile to their eTable 6 group components.
- **Protocol eligibility/time definitions:** adults, home/assisted-living setting, treatment duration of at least one month, and literature period from 1995 are compatible with the main article’s eligibility description.  No distinct result value used a mismatched population/time definition.
- **Display-zero review:** DOC-001’s serious adverse-event pooled incidence of 0 per patient (95% CI, 0.00-0.01) was reviewed as finite displayed precision and is `DISPLAY_ZERO_NOT_CANDIDATE`; it has no independent supplied-source contradiction.

## Unmatched or non-comparable relationships

- Baseline-characteristic rows in eTable 6, titration/actual-usage rows in eTable 7, search-string counts/dates, risk-of-bias matrices, and protocol administrative thresholds did not have a same-result comparator in the article and were not converted into candidate observations.
- The protocol’s planned search wording, subgroup options, sensitivity analyses, and publication-bias rules have no directly repeated numeric result counterpart beyond the meta-analysis-model rule in CS-006.
- The package does not provide raw data, source-study participant-flow tables, analysis code, standard errors, or a dated protocol amendment. These absences limit resolution of CS-004 through CS-006 and the diagnostic-only CS-007.

## Completion record

- **Matched-result sets checked:** 31 (including 14 primary/secondary main-result sets, 10 other-comparison/eTable 10 sets, 4 count/flow sets, and 3 protocol-to-main definition sets).
- **Qualifying local checker observations:** 6 (CS-001 through CS-006).
- **Diagnostic-only observations without stable candidate registration:** 1 (CS-007).
- **Checked non-candidate sets:** 24.
- **Limitations:** Comparisons were restricted to supplied PDFs and printed precision.  No legacy candidate/checker/reviewer/final output or external source was used.  Where a calculation is diagnostic (CS-007), it is explicitly identified and requires source-output confirmation.
