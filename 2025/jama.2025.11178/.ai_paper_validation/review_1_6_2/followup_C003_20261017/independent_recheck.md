# Independent focused recheck of C003

Scope: existing C003 only; this is a focused follow-up, not a new package-wide review. All 20 registered outcome/time rows and all three contrasts in each row were visually inspected in the original main-article page renderings. Existing source and audit artifacts are preserved.

## Evidence authority and location

Main article PDF: jama_debar_2025_oi_250046_1755300121.13587.pdf, pages 4, 10 and 11 (journal pages 595, 601 and 602). Visual authority: existing main-4.png and document_outputs/DOC-001-MAIN/page_images/page_010.png and page_011.png. Supplement 4 PDF: joi250046supp4_prod_1755300121.15587.pdf, pages 16–18, visually inspected through existing document_outputs/DOC-005-RESULTS/page_images/page_016.png, page_017.png and page_018.png. No extraction, rendering, OCR, GPU execution or environment setup was performed in this follow-up.

[Main methods, PDF page 4](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4): “Adjusted SMD is defined as the adjusted mean difference divided by the standard deviation of the change in outcome among the usual care plus group for a given time point”.

[Table 3 footnote d, PDF page 11](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11): “The adjusted between-group mean difference divided by the standard deviation in the change in outcome at the given time point among the usual care plus group.”

These definitions specify one positive UC-change SD for a particular outcome and time point. They do not specify one SD across different outcomes or time points. Within one outcome/time row, common positive scaling preserves contrast signs and requires SMD(HC−PT) = SMD(HC−UC) − SMD(PT−UC).

## Source values and full affected-location audit

Order of contrasts is PT−UC, HC−UC, HC−PT. Table 3 headers explicitly identify these contrasts. Inputs were read from their point-estimate columns, not from group means. Rounding intervals: each one-decimal MD ±0.05; each two-decimal SMD ±0.005. The last column applies the scope's relative display-precision test to the SMD additive identity.

| Outcome, month | Main PDF page | MD: PT−UC, HC−UC, HC−PT | SMD: PT−UC, HC−UC, HC−PT | Predicted HC−PT SMD interval | Printed HC−PT interval | Gap / abs printed |
|---|---:|---|---|---|---|---:|
| Pain severity,3 | 10 | -0.4, -0.4, 0.0 | -0.25, -0.34, -0.13 | [-0.100, -0.080] | [-0.135, -0.125] | 0.192308 |
| Pain severity,12 | 10 | -0.4, -0.4, 0.0 | -0.25, -0.36, -0.11 | [-0.120, -0.100] | [-0.115, -0.105] | 0.000000 |
| Pain intensity,3 | 10 | -0.3, -0.3, 0.0 | -0.21, -0.29, -0.08 | [-0.090, -0.070] | [-0.085, -0.075] | 0.000000 |
| Pain intensity,6 | 10 | -0.3, -0.3, -0.1 | -0.17, -0.27, -0.04 | [-0.110, -0.090] | [-0.045, -0.035] | 1.125000 |
| Pain intensity,12 | 10 | -0.3, -0.2, 0.0 | -0.16, -0.27, -0.03 | [-0.120, -0.100] | [-0.035, -0.025] | 2.166667 |
| Pain interference,3 | 10 | -0.5, -0.5, -0.1 | -0.25, -0.34, -0.13 | [-0.100, -0.080] | [-0.135, -0.125] | 0.192308 |
| Pain interference,6 | 10 | -0.5, -0.6, -0.1 | -0.27, -0.37, -0.14 | [-0.110, -0.090] | [-0.145, -0.135] | 0.178571 |
| Pain interference,12 | 10 | -0.5, -0.5, 0.0 | -0.26, -0.37, -0.12 | [-0.120, -0.100] | [-0.125, -0.115] | 0.000000 |
| Social role,3 | 10 | 0.8, 1.5, 0.7 | 0.12, 0.01, 0.20 | [-0.120, -0.100] | [0.195, 0.205] | 1.475000 |
| Social role,6 | 10 | 1.2, 1.5, 0.3 | 0.18, 0.06, 0.26 | [-0.130, -0.110] | [0.255, 0.265] | 1.403846 |
| Social role,12 | 10 | 1.3, 1.4, 0.1 | 0.19, 0.07, 0.27 | [-0.130, -0.110] | [0.265, 0.275] | 1.388889 |
| Physical functioning,3 | 10 | 0.4, 0.7, 0.3 | 0.09, -0.02, 0.16 | [-0.120, -0.100] | [0.155, 0.165] | 1.593750 |
| Physical functioning,6 | 10 | 0.6, 0.4, -0.3 | 0.15, 0.02, 0.22 | [-0.140, -0.120] | [0.215, 0.225] | 1.522727 |
| Physical functioning,12 | 10 | 0.9, 0.8, -0.1 | 0.20, 0.07, 0.27 | [-0.140, -0.120] | [0.265, 0.275] | 1.425926 |
| PGIC pain,3 | 11 | -0.7, -0.9, -0.3 | -0.61, -0.62, -0.37 | [-0.020, -0.000] | [-0.375, -0.365] | 0.932432 |
| PGIC pain,6 | 11 | -0.6, -0.7, -0.1 | -0.58, -0.57, -0.29 | [0.000, 0.020] | [-0.295, -0.285] | 0.982759 |
| PGIC pain,12 | 11 | -0.6, -0.6, 0.1 | -0.51, -0.54, -0.25 | [-0.040, -0.020] | [-0.255, -0.245] | 0.820000 |
| PGIC general,3 | 11 | -0.8, -1.1, -0.4 | -0.60, -0.66, -0.40 | [-0.070, -0.050] | [-0.405, -0.395] | 0.812500 |
| PGIC general,6 | 11 | -0.5, -0.7, -0.2 | -0.46, -0.50, -0.24 | [-0.050, -0.030] | [-0.245, -0.235] | 0.770833 |
| PGIC general,12 | 11 | -0.6, -0.7, -0.1 | -0.53, -0.58, -0.28 | [-0.060, -0.040] | [-0.285, -0.275] | 0.767857 |


Seventeen rows have a positive additive gap exceeding 0.05 relative to the printed HC−PT SMD. The other three rows still have a scaling discrepancy under the stated common-SD method:

- Severity at 12 months: using the HC−UC MD and SMD to bound SD, an HC−PT MD displayed as 0.0 gives an allowable HC−PT SMD interval [−0.036429, 0.036429]. Printed −0.11 has interval [−0.115, −0.105]; gap 0.068571, relative discrepancy 0.623377.
- Intensity at 3 months: corresponding interval [−0.043000, 0.043000], versus printed −0.08 interval [−0.085, −0.075]; gap 0.032000, relative discrepancy 0.400000.
- Interference at 12 months: corresponding interval [−0.029444, 0.029444], versus printed −0.12 interval [−0.125, −0.115]; gap 0.085556, relative discrepancy 0.712963.

Examples independently clear from signs or ordering:

- Social role, 3 months: MDs +0.8, +1.5, +0.7 but SMDs +0.12, +0.01, +0.20. A common positive standardizer cannot make the larger HC−UC MD have the much smaller SMD. Additive identity predicts HC−PT SMD around −0.11, whereas the table prints +0.20.
- Physical functioning, 3 months: HC−UC MD +0.7 (95% CI +0.2 to +1.2), but its SMD is −0.02. Even after rounding, MD [0.65,0.75] is positive and SMD [−0.025,−0.015] is negative. Positive division cannot reverse this sign.
- Physical functioning HC−PT at 6 and 12 months: MDs −0.3 and −0.1, respectively, but SMDs +0.22 and +0.27, respectively; the sign difference survives rounding.
- PGIC pain HC−PT at 12 months: MD +0.1 but SMD −0.25; the sign difference survives rounding.
- PGIC pain at 3 months: source SMDs are −0.61, −0.62, −0.37. A supplied working example had −0.62 for PT−UC; exact source reads −0.61. This focused note uses the source value and preserves the prior artifacts. The corrected example still fails the additive identity: predicted [−0.020,0.000], printed [−0.375,−0.365].

The source-corrected PGIC working example is not a change to the registered candidate's core source transcription: C003's ledger does not itself print that working triple.

## Supplement check and missing inputs

[Supplement 4 eTable 10, PDF page 16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16) supplies unadjusted change-score medians, quartiles and model-based unadjusted MDs. [eTable 11, PDF pages 17–18](../../../joi250046supp4_prod_1755300121.15587.pdf#page=17) supplies unadjusted raw-score medians, quartiles, MDs and linear-GEE footnote. They do not supply the actual UC change-score SDs required by the main article's adjusted SMD formula. These are different reported quantities; their MDs must not replace adjusted Table 3 values. A median/IQR cannot establish the actual SD without additional distributional assumptions, which are not justified here.

Inputs available: adjusted MDs, adjusted SMDs, their contrast headers, outcome/time labels, and explicit standardizer definition. Inputs absent: exact unrounded fitted contrasts, exact UC-change SD per outcome/time point, effective samples and missing-data treatment used to construct each standardizer, fitted code, and any alternative implemented SMD definition. These absences prevent identification of replacement SMDs but do not prevent sign and common-scaling checks.

Source-grounded alternative interpretation: the implemented SMD construction or contrast assignment may differ from the stated common-UC-SD definition. The package evidence inspected here does not disclose which alternative was used. This is an explanation requiring confirmation, not a direct observation. Direct observations are the printed points, stated formula, and failure of their identities after allowing display precision.

## Classification and evidence fact

Location found: yes, main methods and all 20 registered Table 3 rows. Source value/text matched: yes, with the working-example clarification above. Comparator matched: yes, corresponding adjusted MD and SMD columns under identical outcome, time and contrast labels. Applicable rule: common positive standardizer, additive contrasts, sign preservation, and displayed-input rounding intervals. Calculations reproduced: yes, as recorded above. Actual SD inputs are not necessary for these identity checks, but are necessary for numerical replacement estimates.

Every conflicting location is REPORT by content. Primary relationship S_W; all relationships S_W. Review domain statistical_results. The supplementary results tables corroborate context and missing-input assessment and do not introduce a conflicting REPORT-to-REPORT relationship. No classification correction is warranted.

Evidence state: reproduced. Determining fact: the source-printed MD/SMD points do not satisfy the common positive UC-change-SD construction, including several sign discrepancies and 20 outcome/time rows with additive or scaling discrepancies beyond display precision. Status remains Pending Human Adjudication. Do not interpret the finding as establishing that every SMD cell in those rows differs from its intended value.

Exact remaining human question: Which standardizer and contrast mapping actually generated each adjusted SMD in Table 3, and what source-supported SMD point estimates and associated uncertainty should a downstream extractor use?

## Downstream impact

An SMD-based synthesis of secondary continuous outcomes can be materially affected in magnitude, ordering and sometimes direction. The social-role example has +0.12 versus +0.01 despite MDs +0.8 versus +1.5; physical-functioning HC−UC at 3 months has a positive MD but a negative SMD. Until construction is clarified, one cannot choose a replacement SMD or calculate the effect on a pooled result. The consequence depends on outcome, time point, chosen comparison, weights and other studies; statistical significance of any pooled estimate is not established here.

The principal binary outcome is attainment of the MCID in pain severity, modeled using modified Poisson regression and reported as adjusted RRs. C003 concerns the secondary continuous-outcome SMD construction. Its evidence does not establish a change in the primary RR estimates or trial-level principal conclusion.

C010 concerns SMD point estimates versus their printed confidence intervals. It is a separate registered issue. C003 is reproduced here from point-estimate construction without relying on that interval issue.

