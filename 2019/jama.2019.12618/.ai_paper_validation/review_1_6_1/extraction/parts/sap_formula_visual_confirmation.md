# SAP formula visual transcription supplement

Scope: DOC-004, PLAN, joi190092supp3_prod.pdf, exact PDF pages 22, 23, 24, 26, 34, 63 and 64. This bounded additional mapping supplements extraction/parts/sap_001_064.md; it does not replace that map, diagnose findings, or adjudicate candidates. Seven assigned pages were freshly rendered and visually inspected in full. No additional page is required to close the assigned formula-transcription qualification.

## Engine and derivative provenance

Direct Poppler pdftoppm 26.01.0, CPU, was used after consulting tooling_record.md. For each N in 22,23,24,26,34,63,64 the command was:

`pdftoppm -f N -l N -singlefile -r 140 -png joi190092supp3_prod.pdf .ai_paper_validation/review_1_6_1/preprocessing/sap_formula/page-N`

The outputs are preprocessing/sap_formula/page-22.png, page-23.png, page-24.png, page-26.png, page-34.png, page-63.png and page-64.png below the review directory. Each was opened with view_image. An additional directly rendered p.34 formula detail was opened with view_image:

`pdftoppm -f 34 -l 34 -singlefile -r 300 -x 1000 -y 1500 -W 700 -H 250 -png joi190092supp3_prod.pdf .ai_paper_validation/review_1_6_1/preprocessing/sap_formula/page-34-formula-detail`

No OCR or fallback environment was needed. No supplied source or reused derivative was modified. Formula expressions below transcribe printed symbols rather than substituting assumed quantile conventions.

## PDF page 22 — printed page 21, 29 January 2013

[Source](../../../../joi190092supp3_prod.pdf#page=22). No displayed sample-size formula appears on this page. Section 3.4.1 states target sample size 216, approximately 80% power, difference of 20% in the proportion achieving control of inflammation at six months between methotrexate and mycophenolate mofetil. The model-validation material on this page is already mapped in the original extraction.

## PDF page 23 — printed page 22, 29 January 2013

[Source](../../../../joi190092supp3_prod.pdf#page=23). Equation (5) is printed:

`2N = 4(Z_{alpha} + Z_{beta})^2 pbar(1-pbar) / (p_c-p_i)^2`.

Here alpha and beta are Greek subscripts on capital Z. The alpha subscript is simply alpha, with no printed /2 or 1-minus component; beta is simply beta. The numerator p symbols carry bars. The adjacent text explicitly defines alpha as significance level 0.05, two sided; beta as one minus power, desired power 80%; p_c as methotrexate success probability 0.4; p_i as mycophenolate mofetil success probability 0.6; and `pbar = (p_i+p_c)/2`. Text assumes 10% loss to follow-up in the first six months and states approximately 108 per group, `2 x 108 = 216`. The primary objective is superiority of mycophenolate to methotrexate; clinically meaningful effect is 20%.

The table is visually confirmed in full:

| Success Drug A | 80% power detectable effect | 80% power success Drug B | 90% power detectable effect | 90% power success Drug B |
|---:|---:|---:|---:|---:|
| 20% | 18% | 38% | 21% | 41% |
| 30% | 20% | 50% | 23% | 53% |
| 40% | 20% | 60% | 23% | 63% |
| 50% | 20% | 70% | 22% | 72% |
| 60% | 19% | 79% | 21% | 81% |

The 40% row is bold. The page also states simulation confirms adequate logistic-regression sample sizes, and final critical value will be adjusted slightly because of interim analysis. Sample-size reassessment is considered subject to DSMB approval.

## PDF page 24 — printed page 23, 29 January 2013

[Source](../../../../joi190092supp3_prod.pdf#page=24). Survival sample-size expression is printed:

`N = (Z_{alpha}+Z_{beta})^2 [phi(lambda_C)+phi(lambda_I)] / (lambda_I-lambda_C)^2`.

Both lambda subscripts are capital C and capital I. As in Equation (5), the Z subscripts are Greek alpha and beta with no /2 or 1-minus term. The auxiliary expression is printed:

`phi(u) = u^2 / (1-e^{-uT})`.

Lambda_C is defined as methotrexate hazard; lambda_I as mycophenolate hazard; T is censoring time, 6 months. Adjacent text describes approximately 3.5-month median success time for mycophenolate, then explicitly states in its parenthetical note `lambda_C is log(2)/3.5 mo. for this calculation`. Both statements are retained as printed. With 10% loss, 108 in each group is stated to provide 80% power to detect difference of 2.47 months in the expected difference. Alpha 0.05, two sided, is explicit.

Other numeric context: anatomic subgroup difference 25% with power in excess of 80% by Equation (5); additional 5% loss from 6 to 12 months beyond initial 10%, approximately 78% power for 20% difference at 12 months; vision change SD 6.5 letters, sample size 108, approximately 80% power for 2.63-letter difference using R power.t.test. QoL section begins with SF-36 raw SD 8.4 points; its continuation lies in the existing full map rather than this assigned visual scope.

## PDF page 26 — printed page 25, 29 January 2013

[Source](../../../../joi190092supp3_prod.pdf#page=26). Rescue availability is printed:

`n_j = N_0 r_1 (1-s_j) r_2`.

N_0 is randomized per treatment; r_1 is Aim 1 retention; s_j is success under initial treatment j; r_2 is Aim 2 retention. Source inputs: N_0=108, r_1=0.9; initial drug A success 60%, initial drug B success 40%; an additional 5% loss in Aim 2, r_2=0.95.

| Initial/second treatment | Expected enrollment SA/2 | Expected to complete SA/2 |
|---|---:|---:|
| B/A | 58.3 | 55.4 |
| A/B | 38.9 | 36.9 |

Text states `n_1=58` enrolled in rescue (rounding down), `n_0=38` in other rescue regimen. Rescue power expression is printed:

`1-beta = Phi( |p_1-p_0| / sqrt[p_0(1-p_0)/n_0 + p_1(1-p_1)/n_1] - z_{alpha/2} )`.

The absolute-value bars around p_1-p_0 are present. Lowercase z has Greek alpha/2 subscript; unlike Equation (5), /2 is actually printed here. Phi is capital Greek Phi and is defined as the standard-normal cumulative distribution function. Source defines p_0 as methotrexate rescue after mycophenolate failure and p_1 as mycophenolate rescue after methotrexate failure. Historical mycophenolate rescue success 42%; assumptions yield power 0.87 if methotrexate rescue success is 0.15. The next sentence continues on the subsequent page, outside this bounded visual assignment, and is already present in the full mapping.

## PDF page 34 — printed page 33, 29 January 2013

[Source](../../../../joi190092supp3_prod.pdf#page=34). The displayed Hwang-Shih-deCani expression uses italic Latin a and g glyphs:

`a^*(t) = a(1-e^{-gt}) / (1-e^{-g})`.

The superscript star attaches to a; numerator exponent is minus g times t, and denominator exponent is minus g. Immediately following prose refers to Greek gamma and states gamma=-5.623626 exactly. This artifact preserves the printed equation glyphs and the prose parameter name separately. The planned spending values are approximately 0.001 at t=1/3 and approximately 0.0075 at t=2/3; overall alpha is 0.05. The intended interim looks are approximately one-third and two-thirds, with precise fractions dependent on available data at DSMB meetings; additional efficacy looks allowed under flexible spending. R gsDesign v.2.7-04 or higher. Spending function, including gamma, cannot change after trial starts. Enrollment projection context: 15 American patients at t=1/3 and 30 at t=2/3. No numeric harm stopping formula is displayed; harm stopping is DSMC judgment.

## PDF page 63 — printed page 22, 9 March 2017

[Source](../../../../joi190092supp3_prod.pdf#page=63). Equation (5) is the same visible expression as PDF p.23:

`2N = 4(Z_{alpha}+Z_{beta})^2 pbar(1-pbar) / (p_c-p_i)^2`.

Capital Z subscripts are Greek alpha and beta, with neither /2 nor 1-minus printed. The target is 216, power approximately 80%, primary six-month success difference 20%, superiority of mycophenolate to methotrexate. Text immediately below explicitly states alpha 0.05, two sided; beta one minus power, desired 80%. Definition of p_c starts at bottom and continues on PDF p.64.

## PDF page 64 — printed page 23, 9 March 2017

[Source](../../../../joi190092supp3_prod.pdf#page=64). No new displayed sample-size equation appears. The definition continuing p.63 gives p_c=0.4 for methotrexate, p_i=0.6 for mycophenolate, and `pbar=(p_i+p_c)/2`; 10% first-six-month follow-up loss, approximately 108 per group, total 216. The five-row 80%/90% sensitivity table exactly matches the fully transcribed PDF p.23 table above, including the bold 40% row. Interim-adjusted final critical value, simulation confirmation, DSMB-conditional baseline-predictor reassessment and prespecified type I error control are repeated. Subgroup statement gives in excess of 80% power for 25% success difference by Equation (5). Secondary-outcome heading starts at bottom; no survival equation appears on this page.

## Completion

Seven of seven assigned pages visually mapped; seven full-page new renders and one targeted detail render; zero unusable pages; zero unresolved formula transcription gaps within this assignment. Existing source-linked main map remains unchanged. Additional source page needed for this bounded repair: none. This record does not assert a formula quantile convention absent from the supplied text and makes no checker or candidate determination.
