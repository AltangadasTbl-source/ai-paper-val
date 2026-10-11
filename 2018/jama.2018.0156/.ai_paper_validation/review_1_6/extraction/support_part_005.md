# Support mapping part 005 — SAP, DOC-002 PDF pages 126–134

## Scope, authority, method, and coverage

Exact disjoint source scope: `joi180004supp1_prod.pdf`, PDF pages 126, 127, 128, 129, 130, 131, 132, 133, and 134. These are the nine pages of the Statistical Analysis Plan (SAP), version 1, dated 18 February 2015 in the footer. Every location in this shard is **PLAN**, determined from its prospective analysis-plan content, including sample-size background data. No reported trial outcome counts occur in this shard. No other scientific source units were inspected.

Read the current quantitative scope, complete review contract, tooling record, source coverage, and relevant evidence-asset inventory. Reused the hash-matched supplied OCR text `preprocessing/joi180004supp1_prod/ocr_pages/page_126.txt` through `page_133.txt` and corresponding `images/page_126.png` through `page_133.png` beneath `.ai_paper_validation/`. Visually inspected each of the eight supplied page images. OCR served as transcription aid; source-looking page images determined signs, complete sentences, and numerical inputs. Historical OCR provenance is as recorded by the curator; no historical engine was invoked and no new OCR was run. All pre-existing assets remain unchanged.

Fresh-required page 134 was rendered from the direct source using **Poppler pdftoppm 25.03.0** and visually inspected in full. Exact executed command:

```bash
pdftoppm -f 134 -l 134 -singlefile -r 110 -png joi180004supp1_prod.pdf .ai_paper_validation/review_1_6/preprocessing/support005/page-134
```

Fresh derivative: `.ai_paper_validation/review_1_6/preprocessing/support005/page-134.png`. No environment or packages were needed. Page 134 has a SAP header and footer, with an empty body: it is **not a completely blank sheet**, but contains no result-relevant quantitative relationship. Its absence of body content was observed visually, not inferred from native-text failure.

| PDF page | SAP printed page | Content and mapped status | Evidence mode |
|---|---:|---|---|
| 126 | 1 of 9 | COMPLETE: signed approval, version and date; administrative only | Reused OCR and visual image inspection |
| 127 | 2 of 9 | COMPLETE: table of contents; administrative numeric section/page references only | Reused OCR and visual image inspection |
| 128 | 3 of 9 | COMPLETE: 28-day primary objective and design/population definitions | Reused OCR and visual image inspection |
| 129 | 4 of 9 | COMPLETE: objectives, cancelled interim analyses, sample-size inputs | Reused OCR and visual image inspection |
| 130 | 5 of 9 | COMPLETE: hypothesis inequalities, alpha, ITT/PP/AT definitions | Reused OCR and visual image inspection |
| 131 | 6 of 9 | COMPLETE: primary, secondary, and safety endpoint definitions | Reused OCR and visual image inspection |
| 132 | 7 of 9 | COMPLETE: missingness, summaries, confidence and rounding rules | Reused OCR and visual image inspection |
| 133 | 8 of 9 | COMPLETE: primary, secondary, safety analyses and software | Reused OCR and visual image inspection |
| 134 | 9 of 9 | COMPLETE: empty body; no applicable quantitative relationship | Fresh direct-source Poppler rendering and full visual inspection |

Coverage totals: 9 assigned pages; 8 reusable-backed pages; 1 fresh-required page; 9 mapped pages; 0 scientific coverage gaps. Below are 26 local mapping groups, without stable global numeric/statistical IDs or candidate diagnosis. Matching keys describe what a coordinator can align with independently mapped main-paper evidence; no unassigned main-paper location was opened here.

## Administrative units and translations

[PDF page 126](../../../joi180004supp1_prod.pdf#page=126): SAP approval version 1. Footer 18.FEB.2015. The prepared-by signature date appears handwritten 20 February 2015, clinician date is printed 20 FEB 2015, and biometrics signature date appears handwritten 23 February 2015. Handwritten dates are provenance observations, not trial quantitative outcomes. Signature footnote states that the signatures indicate approval of the plan for analysis and reporting. No numerical analysis relationship is applicable on this page.

[PDF page 127](../../../joi180004supp1_prod.pdf#page=127): administrative contents page, with section and internal-page references. Translations of its French template text: the parenthesis in the contents heading means “to adapt”; the bookmark error means “Error! Bookmark not defined.” No quantitative result or inferential relationship is applicable. The contents lists “Full Analysis Set” and “Observed Cases” and includes other/safety analysis-set template entries; actual analysis-set definitions on page 130 are transcribed below. Section numbers and page references are navigation rather than outcomes.

[PDF page 134](../../../joi180004supp1_prod.pdf#page=134): header “Protocol CAAM / Statistical Analysis Plan”; footer SAP, 18.FEB.2015, page 9 of 9. The body is empty. Explicit no-applicable quantitative unit, freshly mapped.

## Quantitative and statistical relationship groups

### Local group 01 — intervention contrast and endpoint time

[PDF page 128, introduction](../../../joi180004supp1_prod.pdf#page=128), repeated in [page 129, primary objective](../../../joi180004supp1_prod.pdf#page=129). Trial compares two airway-management techniques: tracheal intubation (TI) and bag-valve-mask ventilation (BVM). Primary endpoint is survival at **28 days with favorable neurological function** in out-of-hospital cardiac arrest (OHCA) patients. Introductory wording gives TI versus BVM; the mathematical difference used for inference on page 133 is BVM minus TI. Match key: primary outcome, BVM/TI, 28-day favorable neurological survival.

### Local group 02 — design and analysis identity

[PDF page 128, section 2.1](../../../joi180004supp1_prod.pdf#page=128). Multicenter prospective open randomized controlled noninferiority trial, OHCA, physician-staffed emergency medical services. No cluster-level numerical denominator is stated here. Intervention group is assigned at patient level under the population definitions on page 130. Match key: randomized patient, OHCA, ventilation assignment and noninferiority analysis; do not invent allocation ratio, center model, or covariate adjustment.

### Local group 03 — secondary objective time and safety classes

[PDF page 129, section 2.2](../../../joi180004supp1_prod.pdf#page=129). Compare survival rate at **hospital admission** and at **28 days**, and neurological outcomes, TI versus BVM. Estimate immediate adverse events and serious adverse events related to TI and BVM. Evaluate difficulty of intubation and difficulty of BVM ventilation. These are endpoint and timing keys rather than reported estimates; no event numerator, denominator, or interval is printed.

### Local group 04 — interim analysis and multiplicity

[PDF page 129, section 3](../../../joi180004supp1_prod.pdf#page=129). Interim analyses had been planned but were cancelled because of rapid enrollment. Consequently **only final analysis** was done and **no adjustment for multiplicity** was done. No numerical interim boundary or number of originally scheduled looks is given on this page. Match key: final analysis, multiplicity/alpha adjustment.

### Local group 05 — sample-size background success proportions

[PDF page 129, sample-size paragraph](../../../joi180004supp1_prod.pdf#page=129). Confidence-interval approach to noninferiority. Historical sample-size assumptions: favorable neurological survival rate **3% for BVM** (Hasegawa study, cited as JAMA 2013), and **2% for TI** (Gueugniaud study, cited as NEJM 2008). These remain PLAN background inputs, not trial results. Match key: power calculation, assumed BVM/TI primary-event probabilities. No outside study was accessed.

### Local group 06 — sample-size margin, power, alpha, recruitment, and simulation method

[PDF page 129, sample-size paragraph](../../../joi180004supp1_prod.pdf#page=129). Printed noninferiority margin **1%**; **956 patients per group**; power **0.8**; type I error **0.025**; total recruitment target **2,000 patients**. Basis: **5000 simulations** using the **Newcomb-Wilson score method**. Printed citation reads Statistics in Medicine **1988, 17:873–890**. These are direct transcriptions, including the printed citation year, not externally corrected references. There is no printed attrition percentage or explicit formula connecting 956/group to the recruitment target. Match key: anticipated sample size, margin, power, sidedness, simulation score-CI method. The central sample-size sentence (956/group, 0.8, 0.025, 2000) is omitted by the supplied OCR, but fully legible and recovered through visual inspection.

### Local group 07 — null hypothesis, exact sign and scale

[PDF page 130, section 4.1](../../../joi180004supp1_prod.pdf#page=130). Printed null: **H0: π_BVM − π_TI ≤ −0.01**, followed by “success rate of the BVM is inferior to TI.” The π symbols denote success proportions; subtraction is on an absolute proportion scale, and −0.01 corresponds to −1 percentage point. Match key: BVM minus TI success risk difference, null threshold, noninferiority margin. Preserve the minus sign and non-strict inequality.

### Local group 08 — alternative hypothesis, exact sign and scale

[PDF page 130, section 4.1](../../../joi180004supp1_prod.pdf#page=130). Printed alternative: **H1: π_BVM − π_TI ≥ 0.01**, followed by “success rate of the BVM is not inferior to TI.” Visual inspection shows **no minus sign before 0.01**, and the inequality is **≥**. This is an exact source transcription, without normalization to another formulation. Match key: alternative hypothesis, BVM minus TI success proportion difference. Checker must retain the literal printed alternative when aligning with local groups 07 and 20.

### Local group 09 — hierarchical testing and general sidedness

[PDF page 130, sections 4.1–4.2](../../../joi180004supp1_prod.pdf#page=130). If noninferiority is demonstrated, a **test of difference** will be carried out. “All tests will be two-sided with an alpha value at **0.05**.” No superiority statistic, difference-test formula, or separate alpha is specified here. Match key: noninferiority/difference test order, two-sided alpha.

### Local group 10 — ITT definition and denominator assignment

[PDF page 130, section 5 and 5.1](../../../joi180004supp1_prod.pdf#page=130). Main analysis based on both ITT and PP because the trial is noninferiority. ITT includes **all randomized cardiac-arrest patients aged ≥18 years**, regardless of treatment given, any ventilation technique received, or whether treatment was adequately received. Analyze by **randomization group**. Match key: primary denominator, randomized adult ITT; no actual ITT count appears on this page.

### Local group 11 — PP definition

[PDF page 130, sections 5 and 5.2](../../../joi180004supp1_prod.pdf#page=130). PP includes **all randomized and treated patients without major protocol violations/deviations**. Main criterion also analyzed in PP. No list of major deviations, actual exclusions, or PP count appears here. Match key: primary PP denominator, treatment and major-deviation exclusions.

### Local group 12 — AT definition

[PDF page 130, section 5.3](../../../joi180004supp1_prod.pdf#page=130). As-treated (AT) main criterion analysis uses randomized cardiac-arrest patients aged **≥18**, grouped according to **ventilation technique actually received**. Distinguish actual-treatment regrouping from randomization grouping. No AT count or rescue-treatment attribution rule is printed. Match key: AT outcome denominators and exposure assignment.

### Local group 13 — primary neurological success scale

[PDF page 131, section 6.1](../../../joi180004supp1_prod.pdf#page=131). Primary criterion: **survival at day 28** with favorable neurological function, defined as **Glasgow-Pittsburgh Cerebral Performance Categories (CPC) ≤2**. Success combines survival and neurological cutoff; not all day-28 survival. Match key: favorable neurological survival numerator, time point, CPC dichotomy.

### Local group 14 — secondary efficacy definitions and intubated subset

[PDF page 131, section 6.1](../../../joi180004supp1_prod.pdf#page=131). Secondary endpoints: survival at hospital admission; survival at **28 days**; return of spontaneous circulation (ROSC), called “rate”; **Intubation Difficulty Scale score**, analyzed in **intubated patients**. No person-time definition is supplied for the rates, and no numerical scale bounds for the difficulty score are stated here. Match key: survival/ROSC proportions and intubated subset difficulty score.

### Local group 15 — safety event and quantitative difficulty labels

[PDF page 131, section 6.2](../../../joi180004supp1_prod.pdf#page=131). Safety occurrence need not be causally related to research/product. TI complications during advanced CPR: failure, esophageal intubation, mainstem intubation, vomiting, pulmonary aspiration, dental trauma, extubation. BVM ventilation difficulty measured with **visual analog scale (VAS)**; no VAS units or bounds specified here. BVM complications during advanced CPR: failure, regurgitation of gastric content, gastric inflation. **Han’s mask ventilation classification** also listed, with no grade definitions on this page. Match key: airway complication event labels, procedure-specific denominator, VAS and Han scale. No event count or rate is reported.

### Local group 16 — primary missing-outcome handling and conditional sensitivity

[PDF page 132, section 7](../../../joi180004supp1_prod.pdf#page=132). ITT missing primary outcome imputed by **worst-case principle (no success)**. If large differences occur between PP and ITT populations, sensitivity analyses with different missing-data replacement methods, **including multiple imputation**, will be carried out. “Large” is not numerically defined; no imputation model, number of imputations, or concrete result is printed. Match key: ITT success numerator, missing failure assignment, PP/ITT sensitivity and multiple-imputation analysis.

### Local group 17 — secondary missing-outcome handling

[PDF page 132, section 7](../../../joi180004supp1_prod.pdf#page=132). **No imputation for secondary criteria**. Cross-reference group 19’s non-missing categorical denominator. Match key: secondary endpoint available-case denominator; actual missing totals absent here.

### Local group 18 — continuous summaries, confidence level and precision

[PDF page 132, section 8.1.1](../../../joi180004supp1_prod.pdf#page=132). Continuous variables: number of observations, mean, SD, minimum, maximum, **25%, 50%, 75% quantiles**, **two-sided 95% CIs**. Means, medians, minimum, maximum, and SD to be presented to **one further decimal place**; the reference precision meant by “further” is not specified on the page. No model for the continuous CIs is given. Match key: continuous descriptive rows, sample size, IQR/median, units and precision.

### Local group 19 — categorical counts, percentages and rounding denominator

[PDF page 132, section 8.1.2](../../../joi180004supp1_prod.pdf#page=132). Absolute and relative frequencies (percentages). Percentages based on **all non-missing values (=100%)**; rounded to **one decimal place**; totals may therefore not equal **100%** exactly. This is categorical count/proportion terminology, not person-time incidence. Match key: categorical table denominators, missing observations and displayed totals.

### Local group 20 — primary CI decision rule, sign, exactness and populations

[PDF page 133, section 8.2.1](../../../joi180004supp1_prod.pdf#page=133). Calculate **95% two-sided CI** for **Π_bag − Π_tracheal**. Conclude noninferiority if the **lower CI limit is higher than −0.01** (strict **>**, not ≥). Exact rather than asymptotic CI used if necessary. Analysis in **ITT, PP, and AT**. Source references EMEA guidelines but gives no further exact-CI formula or trigger. Match key: primary BVM–TI absolute success-proportion difference, confidence level, lower limit, margin, ITT/PP/AT. Header spells abbreviations “BMV over TI”; mathematical arm labels are bag and tracheal. Do not substitute a one-sided confidence level.

### Local group 21 — secondary categorical tests and effect measures

[PDF page 133, secondary analyses, printed section 8.2.3](../../../joi180004supp1_prod.pdf#page=133). **Chi-square test on proportions** for all secondary criteria expressed as rates. Present corresponding **95% CIs on odds ratios and differences**. Separate the OR multiplicative scale from the difference absolute scale. No covariance adjustment, continuity correction, or OR/difference CI construction method appears here. Match key: secondary outcome test, OR/difference measure labels and confidence level. A standalone section marker 8.2.2 precedes the printed secondary heading; navigation detail does not supply an additional analysis.

### Local group 22 — secondary continuous tests

[PDF page 133, secondary analyses](../../../joi180004supp1_prod.pdf#page=133). **t test or Mann–Whitney** for quantitative secondary criteria, depending on Gaussian versus non-Gaussian distribution. No variance assumption, distribution-assessment rule, or rank-effect estimate is stated. Match key: continuous outcome test and Gaussian/non-Gaussian analysis label.

### Local group 23 — secondary population and significance definitions

[PDF page 133, secondary analyses](../../../joi180004supp1_prod.pdf#page=133). Secondary analyses also in **PP and AT** populations. Statistical tests **2-tailed**, type I error **0.05**, and **P<0.05** considered significant. “Also” is retained; this sentence does not give counts or endpoint-specific denominator assignments. Match key: secondary ITT/PP/AT, tail and significance threshold.

### Local group 24 — software identity

[PDF page 133, secondary analyses](../../../joi180004supp1_prod.pdf#page=133). Tests performed with **SAS version 9.4**, SAS Institute, Cary, North Carolina. No procedure names or settings printed. Match key: software/version identity and inference implementation.

### Local group 25 — safety categorical analyses and populations

[PDF page 133, printed section 8.2.4](../../../joi180004supp1_prod.pdf#page=133). Safety analysis in **ITT and AT**. Serious and nonserious adverse events tabulated per group. All **dichotomized** endpoints analyzed by **chi-square or Fisher exact test on proportions**, with **95% CI for the odds ratio**. No person-time denominator, RR, rate ratio, or exact CI formula appears here. Match key: safety denominator, actual/randomized grouping, dichotomization, categorical test, OR confidence level.

### Local group 26 — quantitative safety/secondary analysis rule

[PDF page 133, final paragraph](../../../joi180004supp1_prod.pdf#page=133). Beneath safety analyses, quantitative secondary criteria again use **t test or Mann–Whitney**, according to Gaussian versus non-Gaussian distribution. Preserve its location rather than converting it into a different safety-specific estimand. Match key: quantitative adverse-event/difficulty measures and secondary test choice; no numerical inferential result printed.

## Transcription safeguards and absent categories

1. The supplied OCR page 129 dropped the sentence containing 956/group, power 0.8, alpha 0.025, and target 2,000. Visual image recovers those printed inputs. The simulator count is **5000**, not the OCR rendering “5oo0”.
2. The alternative on page 130 is visibly **≥0.01**; the null is **≤−0.01**. Page 133’s decision rule visibly requires the lower CI limit to be **higher than −0.01**. Preserve all three source forms independently for checker work.
3. The mathematical difference on page 133 uses the bag and tracheal success proportions; no printed hazard ratio, relative risk, person-time incidence, standardized mean difference, regression coefficient, covariate-adjusted model, or test statistic/SE appears in these nine pages.
4. There are no trial result tables, figures, numerical subgroup effects, observed sensitivity results, workbook formulas, cached spreadsheet values, CSV records, or Office paragraph groups in this shard. Sensitivity and population analyses are plan definitions, fully mapped above.
5. All body statistical language is already English. French template terms on the contents page were translated above; no French clinical endpoint required translation in this scope.
6. There is no missing scientific unit or unreadable numerical body text after visual mapping. Source-level direct confirmation remains mandatory for any later stable candidate citing these source locations.
