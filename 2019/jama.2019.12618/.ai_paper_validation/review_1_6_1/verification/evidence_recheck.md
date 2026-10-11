# Mechanical evidence recheck

Fresh evidence rechecker: `/root/evidence_rechecker`, `gpt-6.1-sol`, reasoning effort `high`. Assigned stable IDs: C001 and C002. Complete QUALITY_CONTROL_SCOPE.md and workflow_1_6_1/review_contract.md were read. Current ledger, current inclusion screen and all cited included findings supplied the assigned locations; no prior-run conclusions were used. Every affected location was read directly from the supplied PDF and independently inspected in a newly rendered page image. Reusable derivatives were locators only.

| ID | Locations complete | Review domain | Relationship type | All relationships | Evidence state | Classification change |
|---|---|---|---|---|---|---|
| C001 | Yes; main p.4 methods, main p.6 table, dose-definition footnote and matching prose | statistical_results | S_W | S_W | reproduced | None |
| C002 | Yes; main p.6 narrative, main p.7 model 4 and footnote e; SAP pp.31,71 definitions and pp.72,80,81 context | protocol_report | P_R | P_R | reproduced | None |

Evidence states record recheck facts only. Both stable IDs remain Pending Human Adjudication. No disposition, replacement result or preferred analysis is assigned.

## C001 — Missed-dose summaries and stated Welch comparison

**Evidence state:** reproduced.

### Location, source-value and comparator checks

| Exact supplied-source location | Location found | Printed source content matched | Role confirmed from content | Comparison function |
|---|---|---|---|---|
| [Main PDF p.4, Statistical Analyses, upper-right paragraph](../../../jama_rathinam_2019_oi_190092.pdf#page=4) | Yes | Missed doses were compared by group using a Welch t test; significance is described using a 2-sided P value below .05. The permutation statement concerns the primary outcome. | REPORT; retrospective methods describing the reported trial analysis | Stated test and sidedness |
| [Main PDF p.6, Table 2, patient-level missed-dose row](../../../jama_rathinam_2019_oi_190092.pdf#page=6) | Yes | Label: “Missed doses, mean (SD), %”; methotrexate 4.6 (1.0); mycophenolate mofetil 4.3 (0.5); P value .87. Group headings show n=96 and n=98, but this recheck does not impose those counts on the adherence test. | REPORT; observed trial-results table | Numerical summaries and reported P |
| [Main PDF p.6, Table 2, footnote j](../../../jama_rathinam_2019_oi_190092.pdf#page=6) | Yes | Missed doses over total expected doses throughout a patient's enrollment in the trial. The missed-dose row's superscript is i, while this semantic definition is printed as footnote j; its content identifies the adherence quantity directly. | REPORT; definition attached to reported outcomes | Patient-level proportion and percent scale |
| [Main PDF p.6, right-column paragraph immediately above “Subgroup and Sensitivity Analyses”](../../../jama_rathinam_2019_oi_190092.pdf#page=6) | Yes | Mean (SD) proportion of expected doses missed: 4.6% (1.0%) for weekly methotrexate and 4.3% (0.5%) for daily mycophenolate mofetil, P=.87. | REPORT; observed adherence result | Independent repeated source occurrence of all summaries and P |

The source values and comparator match the ledger without transcription correction. Both occurrences explicitly label the dispersion SD. The shifted footnote pointer is immediate contextual information, not part of the registered numerical inconsistency. The footnote k mixed-effects P-value statement applies to the separate eye-level block; it does not supply another method for the patient-level adherence row.

### Consistency rule and calculation reproduced

**Rule applicable:** Yes. For an ordinary two-group Welch comparison of the displayed patient-level mean and sample SD summaries, the absolute t statistic is the absolute mean difference divided by the square root of s1²/n1+s2²/n2. The Welch–Satterthwaite degrees of freedom use those same sample variances and group sizes. At least two observations per group are needed for the reported positive sample SDs and this test. No actual adherence denominator, assumed trial follow-up size, primary-outcome model or Wald approximation is used.

**Display-precision interval check:** Both means and both SDs are printed to one decimal place. The full conservative closed half-unit intervals, in percentage points, are:

| Printed input | Allowed interval |
|---|---|
| Methotrexate mean 4.6 | [4.55,4.65] |
| Mycophenolate mofetil mean 4.3 | [4.25,4.35] |
| Methotrexate SD 1.0 | [.95,1.05] |
| Mycophenolate mofetil SD .5 | [.45,.55] |
| Printed P=.87 | [.865,.875] |

Endpoint inclusion only enlarges the permissible rounding sets. Under every combination in these sets, the absolute mean difference is at least .20 percentage points. Because n1,n2 are each at least 2, the largest possible standard error is sqrt((1.05²+.55²)/2)=.8381527307120105 percentage points. Therefore the absolute t statistic is at least .23861999450875768.

The degrees-of-freedom bound is also independent of group size. Put a=s1²/n1 and b=s2²/n2, both positive. The denominator in the Welch degrees-of-freedom expression is a²/(n1−1)+b²/(n2−1). For n1,n2≥2 it is no larger than a²+b², which is no larger than (a+b)². Thus the Welch degrees of freedom are at least 1. At a fixed positive statistic, the df=1 Student t distribution gives the largest two-sided tail among df≥1. Its tail is the Cauchy tail, so P is no larger than 1−(2/pi)atan(.23861999450875768)=.8508783587237214. This is an exact conservative compatibility bound under the stated test, rather than a sample-size-specific reconstruction.

The upper bound .8508783587237214 is below the smallest value .865 that rounds to the printed .87, with separation .014121641276278574. Hence no allowed rounding combination and no valid group sizes reconcile the printed P with the stated Welch comparison of those mean/SD summaries. Converting percentages to proportions scales the numerator and standard error equally and leaves the statistic unchanged. The compatible bound itself is not proposed as a replacement P value.

### Inputs, alternatives and limits

**Necessary inputs available:** Yes, for the universal compatibility check: both means, both positively valued SDs, displayed precision, named Welch method, two-sided testing context and patient-level missed/expected-dose scale. The group sizes need only meet the mathematical requirement n1,n2≥2.

**Exact missing inputs or definitions:** Actual adherence-analysis group sizes; unrounded adherence summaries; patient-level adherence observations and missingness; the analysis output generating the displayed P; and any unreported transformation or alternative dispersion definition. Their absence prevents reconstruction of the exact intended P, but does not weaken the universal incompatibility bound under the printed method and SD label.

**Source-grounded alternative interpretation:** The supplied sources distinguish an explicit Welch adherence comparison from primary-outcome permutation inference and eye-level mixed models. A different adherence summary variable, a dispersion measure other than the printed SD, or another comparison could have generated .87. None is specified for this result. The recheck does not select such an explanation or infer a replacement number.

**Direct observation versus inferred explanation:** The method sentence, both mean (SD) occurrences, the missed/expected-dose definition and .87 are direct source observations. Nonoverlap of the permissible P ranges is a reproduced mathematical implication. Explanations involving another summary, dispersion or analysis are possibilities, not observed facts.

**Affected result or extracted value:** The adherence mean/SD summaries 4.6 (1.0)% versus 4.3 (.5)% and their printed comparison P=.87. The table and prose repeat the same unresolved pattern; no claim about a changed primary-outcome conclusion is made.

**Exact remaining human question:** Which patient-level adherence summaries and dispersion measure were used in the stated two-sided Welch comparison, and which comparison P value belongs to those summaries?

### Classification confirmation

**Compared document roles:** Every compared location is REPORT, confirmed from the retrospective trial analysis and observed-result content. All are in the same main article.

**Primary relationship type:** S_W. **All relationships:** S_W. **Review domain:** statistical_results. **Classification rationale:** This is a within-report numerical test/method compatibility issue, falling under focus B/C. No PLAN content is a conflicting comparator and no second REPORT is implicated. Any plan corroboration would not create another relationship. Precedence P_R > P_P > S_C > S_W therefore selects S_W from the sole actual relationship.

**Classification corrections:** None. **Classification ambiguity:** None in the supplied material.

**Determining recheck fact:** Exact source mean (SD) labels and values in both table and prose, coupled with the stated two-sided Welch comparison, yield the conservative P upper bound .8508783587237214, outside [.865,.875]. No source transcription correction was needed; evidence state is reproduced.

## C002 — Per-protocol adherence criterion in report versus supplied SAP

**Evidence state:** reproduced.

### Location, source-value and comparator checks

| Exact supplied-source location | Location found | Printed source content matched | Role confirmed from content | Comparison function |
|---|---|---|---|---|
| [Main PDF p.6, right-column adherence sensitivity paragraph](../../../jama_rathinam_2019_oi_190092.pdf#page=6) | Yes | A sensitivity analysis of the primary model included only patients who missed less than 20% of their doses and did not substantially change the result. | REPORT; observed primary-outcome sensitivity | Actual reported eligibility cutoff |
| [Main PDF p.7, Figure 2, model 4](../../../jama_rathinam_2019_oi_190092.pdf#page=7) | Yes | Analysis label “Per protocol”; methotrexate 61/90 (68), mycophenolate 54/94 (57); OR 1.56 (95% CI .84–2.96); P=.17. The figure title identifies six-month primary-outcome sensitivity analyses. | REPORT; observed primary-outcome sensitivity | Named population and exact reported result |
| [Main PDF p.7, Figure 2, footnote e](../../../jama_rathinam_2019_oi_190092.pdf#page=7) | Yes | Primary model with patients who missed less than 20% of study medication, n=184. | REPORT; definition of the displayed model 4 | Independently repeated cutoff and analysis count |
| [Original SAP PDF p.31, §4.1; printed plan p.30, dated 29 January 2013](../../../joi190092supp3_prod.pdf#page=31) | Yes | Per-protocol efficacy includes the ITT population excluding major protocol deviations or medication noncompliance, defined as less than 50% of study drug received by self report or pill counts at study visits. | PLAN; prospective analysis-population specification | Original planned definition |
| [Final SAP PDF p.71, §4.1; printed plan p.30, dated 9 March 2017](../../../joi190092supp3_prod.pdf#page=71) | Yes | Same per-protocol population and below-50%-received noncompliance definition. | PLAN; prospective analysis-population specification | Final supplied planned definition |
| [Final SAP PDF p.72, §4.2; printed plan p.31](../../../joi190092supp3_prod.pdf#page=72) | Yes | Major deviations include never receiving study drug, subsequent ineligibility, never returning for follow-up, visits outside windows, and specified corticosteroid injections. No >80%-received adherence replacement is stated here. | PLAN; prospective deviation and analysis-population context | Additional planned exclusions, not an independent conflicting threshold |
| [Final SAP PDF p.80, §11 revision history; printed plan p.39](../../../joi190092supp3_prod.pdf#page=80) | Yes | 13 January 2015 additions to secondary analyses and updated site stratification. No adherence-population amendment appears on this page. | PLAN; disclosed plan revision history | Amendment context |
| [Final SAP PDF p.81, revision-history continuation; printed plan p.40](../../../joi190092supp3_prod.pdf#page=81) | Yes | Changes to identifiers, primary random-site model, noninferiority analysis, injection sensitivity, major-deviation injections and REDCap randomization. No adherence-population amendment appears on this page. | PLAN; disclosed plan revision history | Amendment context |

Every repeated included-finding occurrence and every cited contextual page matches the ledger without transcription correction. The SAP dates and printed plan page numbers establish which bound plan version is read; all evidence links use the exact PDF page rather than the printed plan pagination.

### Consistency rule and logical comparison reproduced

**Rule applicable:** Yes. Compare the actual reported eligibility criterion for the primary-outcome analysis labeled per protocol with the prospective SAP definition of the per-protocol efficacy population. Keep additional major-deviation exclusions distinct from the adherence component, and distinguish a definition difference from an actual participant-membership difference.

The report requires missed doses <20%. On a matching expected-dose fraction, if a is received and m is missed, m=1−a and m<.20 corresponds to a>.80. Both supplied SAP versions exclude a<.50 under their adherence component, leaving a≥.50 before major-deviation and other eligibility conditions. The complement conversion is arithmetic, not an assumption that every participant's self report, pill count and operational denominator agree. The direct source observation is already that the explicitly written selection rules differ; any difference in their operational adherence definitions would itself require clarification rather than establish equality from the supplied content.

**Display-precision interval check:** These percentages are explicit selection cutoffs, not rounded outcome estimates. Their exact stated rules do not reconcile. Even treating each printed whole-percent cutoff as a conservative half-unit interval would leave report missed <[19.5,20.5]%, corresponding to a received cutoff between 79.5% and 80.5%, versus SAP received <[49.5,50.5]% as the exclusion. The nearest cutoff values are still separated by 29 percentage points. Thus display rounding cannot equate the definitions. The report strict inequality and SAP exclusion strict inequality are also retained: report >80% received versus SAP ≥50% received on the matched metric.

The reported model's counts themselves reconcile: 90+94=184. The printed success fractions 61/90 and 54/94 give 67.777...% and 57.446...%, both within the displayed whole-percent intervals [67.5,68.5] and [56.5,57.5]. OR 1.56 lies within [.84,2.96]. These ancillary checks identify the exact affected model; the model-based OR is not treated as a crude recomputation. No count, OR, interval or P for the SAP-defined population is inferred.

### Inputs, alternatives and limits

**Necessary inputs available:** Yes, for comparison of the written eligibility definitions and identification of the reported model: both SAP definitions, report narrative and figure cutoff, primary-outcome figure designation, n=184 and the reported OR/CI/P. SAP major-deviation conditions and supplied revision-history pages are available and were read.

**Exact missing inputs or definitions:** Participant-level received/missed-dose values and their denominators and time windows; rules for reconciling self report with pill counts; the precise deviation exclusions applied to model 4; the actual analysis-set listing; any operative amendment not included in the package; and a separate result under the supplied SAP-defined population. These omissions prevent calculation of an alternative population count or effect and prevent deciding why the definition changed. They are not independent numerical inconsistencies registered here.

**Source-grounded alternative interpretation:** Main p.6 explicitly calls the result a sensitivity analysis; it could be an additional stricter-adherence sensitivity labeled per protocol in Figure 2 rather than the supplied SAP-defined per-protocol analysis. Another possibility is an operative amendment absent from the supplied sources. A differing operational definition or period for dose receipt may also require reconciliation. Neither the final population definition nor the cited revision history selects or documents one of these explanations. No alternative estimate or preferred threshold is proposed.

**Direct observation versus inferred explanation:** The report <20%-missed criterion, “Per protocol” label, n=184 result, both SAP <50%-received exclusions and supplied amendment entries are direct observations. Their numerical complements and cutoff separation are reproduced arithmetic. Actual inclusion of any participant between the cutoffs, changed effect magnitude, omission of the planned analysis, and existence of an undisclosed amendment are not established and are not asserted.

**Affected result or extracted value:** Interpretation of the six-month primary-outcome sensitivity labeled per protocol, n=184, OR 1.56 (95% CI .84–2.96), P=.17, as the supplied prospectively defined population or an additional adherence sensitivity. The recheck concerns its analysis-population definition and prespecified status, not the direction or magnitude of an unavailable alternative result.

**Exact remaining human question:** Is Figure 2 model 4 the prespecified SAP per-protocol efficacy analysis or an additional adherence sensitivity, and which operative adherence definition, dose denominator/period and major-deviation exclusions explain its <20%-missed criterion and n=184 relative to the supplied SAP's <50%-received exclusion?

### Classification confirmation

**Compared document roles:** Main p.6 and p.7 locations are REPORT, confirmed from observed trial-result and model-description content. SAP pp.31,71,72,80,81 are PLAN, confirmed from prospective population/deviation specifications and plan amendment history.

**Primary relationship type:** P_R. **All relationships:** P_R. **Review domain:** protocol_report. **Classification rationale:** This is a REPORT versus PLAN primary-outcome analysis-population definition comparison under focus D. The original and final SAP definitions agree, so there is no P_P conflict. The main narrative and figure agree with each other, so their corroboration does not create S_W. No different REPORT is in conflict, so S_C does not apply. P_R is the sole actual relationship and therefore is primary under P_R > P_P > S_C > S_W.

**Classification corrections:** None. **Classification ambiguity:** No role or relationship ambiguity is identified. A possible operative amendment absent from the supplied package is an unresolved explanation; the cited supplied amendment pages do not disclose a matching adherence-threshold change. This possibility does not alter the confirmed classification of the supplied comparison.

**Determining recheck fact:** Exact visual confirmation finds the report <20%-missed criterion in both narrative and model footnote, the per-protocol label and result, and identical <50%-received noncompliance exclusions in the original and final SAP. The cited final-plan context contains no matching replacement. The written definitions remain distinct beyond display precision; evidence state is reproduced without source transcription correction.

## Direct-tool provenance and completion

Tooling record confirms direct Poppler tools are available, version 26.01.0; no fallback is needed. For main pages 4,6,7 and SAP pages 31,71,72,80,81, this fresh agent ran direct `pdftotext -layout -f N -l N "SOURCE.pdf" "OUTPUT.txt"` and direct `pdftoppm -f N -l N -singlefile -scale-to 1800 -png "SOURCE.pdf" "OUTPUT_PREFIX"`. Eight newly rendered pages were individually inspected with view_image. All derivatives are below `.ai_paper_validation/review_1_6_1/preprocessing/evidence_recheck/`; no GPU, OCR, additional Python or external source was used. Ordinary JavaScript arithmetic independently reproduced the numerical bounds and count checks.

| Source PDF | Exact source pages | Newly generated layout paths, relative to review_1_6_1 | Newly generated image paths, relative to review_1_6_1 |
|---|---|---|---|
| jama_rathinam_2019_oi_190092.pdf | 4 | preprocessing/evidence_recheck/main-p4-layout.txt | preprocessing/evidence_recheck/main-p4.png |
| jama_rathinam_2019_oi_190092.pdf | 6 | preprocessing/evidence_recheck/main-p6-layout.txt | preprocessing/evidence_recheck/main-p6.png |
| jama_rathinam_2019_oi_190092.pdf | 7 | preprocessing/evidence_recheck/main-p7-layout.txt | preprocessing/evidence_recheck/main-p7.png |
| joi190092supp3_prod.pdf | 31 | preprocessing/evidence_recheck/sap-p31-layout.txt | preprocessing/evidence_recheck/sap-p31.png |
| joi190092supp3_prod.pdf | 71 | preprocessing/evidence_recheck/sap-p71-layout.txt | preprocessing/evidence_recheck/sap-p71.png |
| joi190092supp3_prod.pdf | 72 | preprocessing/evidence_recheck/sap-p72-layout.txt | preprocessing/evidence_recheck/sap-p72.png |
| joi190092supp3_prod.pdf | 80 | preprocessing/evidence_recheck/sap-p80-layout.txt | preprocessing/evidence_recheck/sap-p80.png |
| joi190092supp3_prod.pdf | 81 | preprocessing/evidence_recheck/sap-p81-layout.txt | preprocessing/evidence_recheck/sap-p81.png |

Completed: 2/2 assigned IDs, every repeated-pattern source location and every cited contextual location. Classification changes: 0. Source transcription corrections: 0. Evidence states: reproduced=2. No scientific-coverage gap remains in this assigned scope. Missing adherence output and participant-level/operative-population definitions remain precisely named human questions; no replacement result is inferred. All supplied sources, reusable artifacts, ledger and screening records were preserved.
