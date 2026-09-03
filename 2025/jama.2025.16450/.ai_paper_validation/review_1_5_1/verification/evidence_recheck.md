# Exact-Source Evidence Recheck

All stable IDs `C001` through `C010` were rechecked separately against the cited direct PDF pages. The PDF pages were rendered from the supplied sources for visual inspection; the text layer and prior extraction artifacts were used only as locators and transcription aids. The rendered page images are derivative aids under `preprocessing/recheck/` and are not substituted for the direct PDFs cited below. Every ID remains **Pending Human Adjudication**.

## C001 — eTable 4 expands RR as risk difference although the table reports relative risk

- **Location found:** DOC-005, [PDF p. 7, eTable 4 header and rows](<../../../joi250072supp4_prod_1761000786.6988.pdf#page=7>), and [PDF p. 8, abbreviations and model text](<../../../joi250072supp4_prod_1761000786.6988.pdf#page=8>).
- **Source value/text matched:** Yes. Page 7 prints `Relative Risk (RR) or Mean Difference (MD)` and ratio-form entries including PDA `RR: 0.86 (0.75, 0.99)`. Page 8 prints `RR = risk difference`.
- **Comparator matched:** Yes. The p. 8 analysis text says that binary outcomes report relative risks estimated by robust Poisson regression unless otherwise noted.
- **Consistency rule applicable:** Yes. `RR` cannot simultaneously expand to relative risk and risk difference in the same table because the measures use different scales and null values.
- **Calculation or logical comparison reproduced:** From the displayed PDA counts, `(159/319)/(175/308) = 0.8772`, a crude ratio, while `100 × (159/319 - 175/308) = -6.97` percentage points, a crude difference. The adjusted table entry `.86` is presented on the ratio scale and is compatible in direction with the crude ratio, not with a risk-difference expansion.
- **Necessary inputs available:** The header, abbreviation line, binary-model description, counts, denominators, and displayed estimate are available. Exact reproduction of the adjusted `.86` would additionally require individual or stratum-level observations, the pooled-center mapping, and the fitted robust-Poisson output; those inputs are not supplied, but they are not needed to establish the label conflict.
- **Source-grounded alternative interpretation:** The isolated p. 8 expansion may be a localized abbreviation-line transcription, while the header, model text, and estimates consistently use relative risk.
- **Direct observation versus inferred explanation:** The conflicting printed expansions and ratio-form values are direct observations. A localized production or copyediting cause is inferred and is not established by the package.
- **Exact remaining human question:** Should `RR` in the p. 8 abbreviation line be understood as `relative risk`, consistent with the p. 7 header, model description, and ratio-scale entries?
- **State:** Pending Human Adjudication.

## C002 — Eligibility upper gestational-age bound differs across supplied trial documents

- **Location found:** DOC-002, [PDF p. 4, Eligibility Criteria](<../../../joi250072supp1_prod_1761000786.68881.pdf#page=4>); DOC-003, [PDF p. 7, Eligibility Criteria](<../../../joi250072supp2_prod_1761000786.6938.pdf#page=7>); DOC-004, [PDF p. 8, background population](<../../../joi250072supp3_prod_1761000786.6988.pdf#page=8>) and [PDF p. 15, Inclusion Criteria](<../../../joi250072supp3_prod_1761000786.6988.pdf#page=15>); DOC-001, [PDF p. 2, Participants](<../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=2>).
- **Source value/text matched:** No for the ledger's DOC-002 transcription. Direct visual inspection of DOC-002 p. 4 shows `22 0/7 – 28 6/7 weeks gestation`, not `22 0/7 – 27 6/7`.
- **Comparator matched:** Yes. DOC-003 p. 7 and DOC-004 pp. 8 and 15 also print `22 0/7 – 28 6/7`; DOC-001 p. 2 prints 22 weeks 0 days through 28 weeks 6 days.
- **Consistency rule applicable:** The rule is applicable in principle because matched eligibility bounds should agree, but the claimed disagreement is not reproduced at the cited pages.
- **Calculation or logical comparison reproduced:** The visually read upper bounds are all 28 weeks 6 days, so their pairwise boundary difference is 0 days, not 7 days.
- **Necessary inputs available:** All cited eligibility passages and their version headers are available for this comparison. No cited direct-source input is missing. What is missing is any supplied page that prints the ledger's asserted `27 6/7` upper bound.
- **Source-grounded alternative interpretation:** The earlier extraction likely misread the custom-encoded digit `8` as `7`; that explanation is an inference from the direct-page disagreement with the prior transcription.
- **Direct observation versus inferred explanation:** The `28 6/7` text on every cited direct page is a direct observation. A font-decoding or transcription mechanism is inferred.
- **Exact remaining human question:** Does any other supplied direct-source passage support `27 6/7`, or should this ID be adjudicated on the basis that every cited page prints an upper bound of `28 6/7`?
- **State:** Pending Human Adjudication.

## C003 — First-dose poractant alfa volume differs across supplied trial documents

- **Location found:** DOC-002, [PDF p. 4, Study Intervention/Methods](<../../../joi250072supp1_prod_1761000786.68881.pdf#page=4>); DOC-003, [PDF p. 7, summary](<../../../joi250072supp2_prod_1761000786.6938.pdf#page=7>) and [PDF p. 12, Study Intervention and Comparison](<../../../joi250072supp2_prod_1761000786.6938.pdf#page=12>); DOC-004, [PDF p. 8, background treatment description](<../../../joi250072supp3_prod_1761000786.6988.pdf#page=8>); DOC-001, [PDF p. 2, Randomization](<../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=2>); DOC-005, [PDF p. 4, eTable 2 footnote c](<../../../joi250072supp4_prod_1761000786.6988.pdf#page=4>).
- **Source value/text matched:** No for the ledger's DOC-002 transcription. Direct visual inspection of DOC-002 p. 4 shows poractant alfa/Curosurf `2.5 ml/kg` for the intervention and active-control first dose, not `1.25 mL/kg`.
- **Comparator matched:** Yes. DOC-003 pp. 7 and 12, DOC-004 p. 8, DOC-001 p. 2, and DOC-005 p. 4 all identify `2.5 mL/kg` for dose 1. DOC-003 and DOC-005 distinguish `1.25 mL/kg` as dose 2.
- **Consistency rule applicable:** The dose-and-order identity rule is applicable in principle, but the claimed first-dose disagreement is not reproduced from the cited direct pages.
- **Calculation or logical comparison reproduced:** The first-dose values compare as `2.5 / 2.5 = 1`, with a difference of `0 mL/kg`. The supplied `1.25 mL/kg` value is explicitly attached to dose 2 in DOC-003 and DOC-005.
- **Necessary inputs available:** Dose number, volume per kilogram, arm context, and first-versus-second-dose wording are present. No cited comparison input is missing. What is missing is a supplied direct-source passage assigning `1.25 mL/kg` to the first dose.
- **Source-grounded alternative interpretation:** The earlier extraction may have transferred the second-dose value to the first-dose sentence or misread the custom-encoded `2.5`; the mechanism is not directly documented.
- **Direct observation versus inferred explanation:** The consistent `2.5 mL/kg` first-dose and `1.25 mL/kg` second-dose statements are direct observations. An extraction/transcription cause is inferred.
- **Exact remaining human question:** Does any other supplied direct-source location assign `1.25 mL/kg` to dose 1, or should this ID be adjudicated using the cited pages' consistent `2.5 mL/kg` first-dose value?
- **State:** Pending Human Adjudication.

## C004 — Severe-NDI GMFCS cutoff differs between the manual and SAP

- **Location found:** DOC-003, [PDF p. 14, secondary-outcome definition](<../../../joi250072supp2_prod_1761000786.6938.pdf#page=14>) and [PDF p. 16, NDI table](<../../../joi250072supp2_prod_1761000786.6938.pdf#page=16>); DOC-004, [PDF p. 10, Secondary Efficacy Outcomes](<../../../joi250072supp3_prod_1761000786.6988.pdf#page=10>) and [PDF p. 33, outcome-definition table](<../../../joi250072supp3_prod_1761000786.6988.pdf#page=33>).
- **Source value/text matched:** Yes. The manual prints GMFCS `3-5` in both the narrative example on p. 14 and the severe column of the NDI table on p. 16.
- **Comparator matched:** Yes. The SAP prints GMFCS `4-5` on p. 10 and `level 4-5` on p. 33.
- **Consistency rule applicable:** Yes. These categorical cutoffs define different membership for GMFCS level 3 when used as a component of severe NDI.
- **Calculation or logical comparison reproduced:** The manual set is `{3, 4, 5}` and the SAP set is `{4, 5}`. Their exact set difference is `{3}`; the cutoff shifts by one GMFCS level.
- **Necessary inputs available:** The category definitions and endpoint context are available. Missing inputs are the governing version/amendment decision, the implemented follow-up algorithm, and the number and treatment assignment of assessed children at GMFCS level 3; without those, the numerical effect on the endpoint cannot be quantified.
- **Source-grounded alternative interpretation:** The manual p. 14 calls its definition an example in light of transition to BSID-IV, while the later-dated SAP states a planned definition. This supports a possible versioned definition change, but the package does not explicitly state that the GMFCS cutoff was amended from 3-5 to 4-5.
- **Direct observation versus inferred explanation:** The two cutoffs are direct observations. Version precedence and any effect on eventual endpoint classification are inferred possibilities.
- **Exact remaining human question:** Which GMFCS cutoff governed the trial's severe-NDI endpoint, and is there a supplied amendment or implementation record explaining the change from `3-5` to `4-5`?
- **State:** Pending Human Adjudication.

## C005 — Severe-NDI cognitive instrument edition differs within supplied definitions

- **Location found:** DOC-003, [PDF p. 14, secondary-outcome definition](<../../../joi250072supp2_prod_1761000786.6938.pdf#page=14>) and [PDF p. 16, follow-up description](<../../../joi250072supp2_prod_1761000786.6938.pdf#page=16>); DOC-004, [PDF p. 10, Secondary Efficacy Outcomes](<../../../joi250072supp3_prod_1761000786.6988.pdf#page=10>), [PDF p. 33, outcome-definition table](<../../../joi250072supp3_prod_1761000786.6988.pdf#page=33>), and [PDF p. 34, table continuation](<../../../joi250072supp3_prod_1761000786.6988.pdf#page=34>).
- **Source value/text matched:** Yes for the manual's `BSID IV` wording. The manual pp. 14 and 16 identify BSID-IV and a cognitive threshold below 70.
- **Comparator matched:** No for the ledger's claimed SAP `Bayley-III` transcription. SAP p. 10 prints `BSID IV < 70`; SAP p. 33 prints `Bayley's Scale for Infant Development, 4th edition (BSID-IV) cognitive score < 70`. Page 34 continues the same outcome definition and does not print Bayley-III.
- **Consistency rule applicable:** Instrument-edition identity is applicable in principle, but the claimed edition disagreement is not reproduced at the cited direct pages.
- **Calculation or logical comparison reproduced:** `4th edition` and `BSID-IV` identify the same edition, and all cited passages retain the `<70` cognitive threshold. There is no III-versus-IV difference among the cited text.
- **Necessary inputs available:** Instrument name, edition, threshold, and endpoint context are available. No cited comparison input is missing. What is missing is any supplied cited passage that prints `Bayley-III` for this endpoint.
- **Source-grounded alternative interpretation:** The earlier extraction likely decoded the roman numeral `IV` as `III` or carried text from another template; the specific mechanism is not established by the direct sources.
- **Direct observation versus inferred explanation:** The repeated BSID-IV/4th-edition wording is directly observed. An extraction or template carry-forward mechanism is inferred.
- **Exact remaining human question:** Does another supplied direct-source passage identify Bayley-III for severe NDI, or should this ID be adjudicated on the basis that all cited passages identify BSID-IV?
- **State:** Pending Human Adjudication.

## C006 — First interim nominal alpha differs tenfold between protocol and SAP

- **Location found:** DOC-002, [PDF p. 29, section 5.5.2.2 Efficacy](<../../../joi250072supp1_prod_1761000786.68881.pdf#page=29>); DOC-004, [PDF p. 26, section 7.4.2 Efficacy](<../../../joi250072supp3_prod_1761000786.6988.pdf#page=26>).
- **Source value/text matched:** No for the ledger's protocol transcription. Direct visual inspection of DOC-002 p. 29 shows first-look alpha `0.000015` at 25%, not `0.00015`.
- **Comparator matched:** Yes. DOC-004 p. 26 also prints `0.000015` at 25%, followed by `0.0030`, `0.0183`, and `0.0440`; DOC-002 prints the same schedule.
- **Consistency rule applicable:** A same-look nominal-alpha identity rule is applicable, but the asserted tenfold difference is not reproduced from the direct pages.
- **Calculation or logical comparison reproduced:** `0.000015 / 0.000015 = 1`; the difference is 0. Counting decimal places in the printed protocol confirms four zeros after the decimal before `15`, the same as the SAP.
- **Necessary inputs available:** Both planned schedules, look percentages, and nominal alphas are present. No cited comparison input is missing. What is missing is a supplied cited passage printing `0.00015` for the 25% efficacy look.
- **Source-grounded alternative interpretation:** The earlier extraction likely dropped one zero when transcribing the custom-encoded protocol page.
- **Direct observation versus inferred explanation:** The identical printed schedules are direct observations. A dropped-zero transcription mechanism is inferred.
- **Exact remaining human question:** Does any other supplied protocol page state `0.00015`, or should this ID be adjudicated using the identical `0.000015` values on the two cited pages?
- **State:** Pending Human Adjudication.

## C007 — Final primary-analysis alpha differs between the article and prospective documents

- **Location found:** DOC-001, [PDF p. 3, Sample Size Estimation and Statistical Analysis](<../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=3>) and [PDF p. 7, Table 2 footnote b](<../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=7>); DOC-002, [PDF p. 29, efficacy schedule](<../../../joi250072supp1_prod_1761000786.68881.pdf#page=29>); DOC-004, [PDF p. 26, efficacy schedule](<../../../joi250072supp3_prod_1761000786.6988.pdf#page=26>).
- **Source value/text matched:** Yes. The article p. 3 states the primary analysis was performed at alpha `.049`, and Table 2 footnote b states sequential testing was performed at alpha `.049`.
- **Comparator matched:** Yes. The protocol and SAP print planned final alpha `.0440` after the listed 25%, 50%, and 75% efficacy looks.
- **Consistency rule applicable:** Conditionally. A single executed primary threshold should be traceable to the prespecified alpha-spending framework, but a planned fixed-look value and a realized boundary need not be numerically identical when information timing or the number of performed looks changes.
- **Calculation or logical comparison reproduced:** `.049 - .0440 = .0050`. The observed ratio is `.049/.0440 = 1.1136`. This is not a rounding-only difference.
- **Necessary inputs available:** The article's executed alpha and the prospective nominal schedule are available. Missing inputs are the realized information fractions, exact dates and efficacy status of each look, accumulated alpha spending, the Lan-DeMets boundary output, and any amendment or recovery of unspent alpha. The SAP itself says exact alpha depends on timing and prior analyses and that alpha not spent at unperformed looks may be recovered.
- **Source-grounded alternative interpretation:** The `.049` threshold may be a realized Lan-DeMets boundary after early stopping and fewer or differently timed efficacy looks, rather than a contradiction of the prospective `.0440` value for the originally planned final look.
- **Direct observation versus inferred explanation:** The `.049` and `.0440` values and the SAP's timing caveat are direct observations. A recalculated realized boundary is an inference because its inputs/output are absent.
- **Exact remaining human question:** What realized information fractions and alpha-spending output produced `.049`, and how was that executed threshold derived from or amended relative to the prospective `.0440` final-look value?
- **State:** Pending Human Adjudication.

## C008 — Trial center count differs between final and prospective documents

- **Location found:** DOC-001, [PDF p. 1, Design, Setting, and Participants](<../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=1>); DOC-002, [PDF p. 29, safety-model discussion](<../../../joi250072supp1_prod_1761000786.68881.pdf#page=29>); DOC-004, [PDF p. 8, background and protocol history](<../../../joi250072supp3_prod_1761000786.6988.pdf#page=8>).
- **Source value/text matched:** Yes. The final article states the trial was conducted in `17 centers` of the US Neonatal Research Network.
- **Comparator matched:** Yes. The protocol says there are `15 centers` in the NRN for the planned model, and the SAP says all `15 NRN centers plan to participate`.
- **Consistency rule applicable:** Conditionally. Setting counts should agree when they refer to the same operational period, but a prospective count of planned sites and a final count of participating sites can differ if activation changed over time.
- **Calculation or logical comparison reproduced:** `17 - 15 = 2` additional centers in the final report relative to the prospective count.
- **Necessary inputs available:** The three counts and their prospective-versus-final contexts are available. Missing inputs are a center-by-center activation/enrollment list, enrollment contribution by center, amendment history, and the definition of whether a center means an NRN center, hospital, or pooled analysis unit.
- **Source-grounded alternative interpretation:** DOC-004 explicitly uses future-tense `plan to participate`, while DOC-001 describes completed conduct; two centers may have been added after the prospective documents were written.
- **Direct observation versus inferred explanation:** The 17 and 15 counts and their tenses are direct observations. Later site activation or a difference in counting units is inferred.
- **Exact remaining human question:** Which centers actually enrolled participants, when were any additional centers activated, and do `15` and `17` use the same center-counting definition?
- **State:** Pending Human Adjudication.

## C009 — Table 3 RR label conflicts with a stated common-OR approximation

- **Location found:** DOC-001, [PDF p. 8, Table 3 open-label-surfactant row and footnote g](<../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=8>).
- **Source value/text matched:** Yes. The row prints `RR: 0.69 (0.33 to 1.46)` for 13/312 versus 18/299.
- **Comparator matched:** Yes. Footnote g says relative risk was estimated by Mantel-Haenszel methods, `approximated by the common OR`, after robust-Poisson convergence issues, stratified by gestational-age strata and pooled center.
- **Consistency rule applicable:** Yes. Relative risk and odds ratio are distinct effect measures. If an odds ratio is used as a numerical approximation, the row label and footnote should make the reported estimator and target measure unambiguous.
- **Calculation or logical comparison reproduced:** The crude risk ratio is `(13/312)/(18/299) = 0.6921`, which rounds to the displayed `.69`. The crude odds ratio is `[13 × (299-18)]/[(312-13) × 18] = 0.6787`, which rounds to `.68`. Neither crude calculation identifies the stated stratified Mantel-Haenszel/common-OR quantity.
- **Necessary inputs available:** Overall counts, denominators, displayed interval, label, and estimator wording are available. Missing inputs are the cross-classified stratum counts, common-OR estimate/output, Mantel-Haenszel weighting details, and exact interval construction; therefore the stratified point estimate and interval cannot be independently reproduced.
- **Source-grounded alternative interpretation:** The estimand may remain relative risk while a common OR was used only as a rare-event numerical approximation after nonconvergence. The footnote may be intended to disclose that approximation without relabeling the target measure, but its wording does not resolve which measure the printed `.69` formally represents.
- **Direct observation versus inferred explanation:** The `RR` row label and common-OR wording are direct observations. The distinction between target estimand and substituted estimator is an inferred reading.
- **Exact remaining human question:** Is `.69 (0.33 to 1.46)` formally a Mantel-Haenszel relative risk, a common odds ratio, or an odds-ratio approximation to a relative-risk target, and which effect-measure label should accompany it?
- **State:** Pending Human Adjudication.

## C010 — eTable 3 relative-risk header conflicts with odds-ratio approximation footnote

- **Location found:** DOC-005, [PDF p. 5, eTable 3 header and marked rows](<../../../joi250072supp4_prod_1761000786.6988.pdf#page=5>) and [PDF p. 6, continuation and footnote b](<../../../joi250072supp4_prod_1761000786.6988.pdf#page=6>).
- **Source value/text matched:** Yes. The effect column is headed `Relative Risk (95% CI) or P-value`. Marked rows include endotracheal tube blockage `0.73 (0.16, 3.28)`, prolonged hypoxemia plus bradycardia `0.65 (0.11, 3.90)`, and serious-event hyperglycemia `2.64 (0.69, 10.05)`.
- **Comparator matched:** Yes. Footnote b says relative risk was approximated by the crude, unadjusted odds ratio with exact 95% confidence intervals because of low event prevalence.
- **Consistency rule applicable:** Yes. The table-level header names relative risk, while the marked-row method names odds ratio; the intended measure and approximation should remain distinguishable.
- **Calculation or logical comparison reproduced:** Using the table group denominators, crude odds ratios are `(3×309)/(319×4) = 0.7265`, `(2×310)/(320×3) = 0.6458`, and `(8×310)/(314×3) = 2.6327`, close to the displayed `.73`, `.65`, and `2.64`. This supports that the marked point estimates are odds-ratio approximations, subject to any row-specific missingness not printed.
- **Necessary inputs available:** Event counts, group sizes, marked-row estimates, header, and footnote are available. Exact CI reproduction would require the precise exact-interval algorithm, tail convention, and confirmation of row-specific nonmissing denominators; these are not fully stated.
- **Source-grounded alternative interpretation:** The header may identify the target measure for the table while footnote b transparently discloses an odds-ratio approximation for exceptional sparse rows. That reading explains the method but leaves the row-level effect-measure label potentially ambiguous.
- **Direct observation versus inferred explanation:** The header, superscript marks, estimates, and footnote are direct observations. The intended distinction between target measure and approximation is inferred.
- **Exact remaining human question:** For superscript-b rows, should the displayed effect be understood and extracted as an odds ratio, or as an explicitly labeled odds-ratio approximation to relative risk?
- **State:** Pending Human Adjudication.

## Recheck completeness and limitations

- Stable IDs covered: `C001`-`C010` (10/10).
- Direct-source relationships reproduced as stated in the ledger: `C001`, `C004`, `C007`, `C008`, `C009`, and `C010`.
- Direct-source transcription discrepancies requiring human review: `C002` (DOC-002 p. 4 prints `28 6/7`), `C003` (DOC-002 p. 4 prints first dose `2.5 mL/kg`), `C005` (DOC-004 p. 33 prints 4th edition/BSID-IV), and `C006` (DOC-002 p. 29 prints `0.000015`). The asserted contradictions for these four IDs are not reproduced at the cited pages.
- Model-level reconstruction remains limited where individual/stratum-level data, fitted-model output, exact interval algorithms, realized alpha-spending information, amendment history, or site-activation records are not supplied. These limits do not prevent direct comparison of the printed text and values recorded above.
- Every ID remains **Pending Human Adjudication**.
