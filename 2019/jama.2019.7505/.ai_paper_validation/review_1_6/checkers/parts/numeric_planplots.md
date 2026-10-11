# Numeric consistency checker: PLAN and supplementary methods/figures

Status: COMPLETE. Fresh runtime 01a1286f-0335-7023-bd65-6ab8f678399d, required model gpt-6.1-sol/medium. Scope and all120 relationships N361–N480 are in relationships/parts/numeric_inventory_planplots.md. Assigned PLAN 43/43 pages; REPORT eMethods 4/4 and eFigures 12/12 checked. Main pp6–10 used only for matched comparators. Distinct candidate local keys: 16. No stable C IDs, severity, evidence disposition or adjudication assigned. Sources and reused assets preserved.

The inventory checks all relevant arithmetic, totals, subgroup/threshold partitions, numerator/denominator, missingness/population, percent/rounding, effect labels/scales/units/reference groups, risk/count/person-time and repeated values. Exact source print is authoritative; direct Poppler26.01.0 text and supplied page images locate it. Statistical test/CI reconstruction remains separately tracked in the S inventory. An unchanged printed row alone, a missing model detail alone, or unusual clinical unit alone was not treated as contradiction. No external literature or old candidates read.

| Local key | Candidate | Compared roles |
|---|---|---|
| NP-P01 | Current protocol retains incompatible recruitment totals | PLAN / PLAN |
| NP-M01 | Mild respiratory failure uses equality rather than the main report's inclusive oxygen threshold | REPORT / REPORT |
| NP-F01 | Mortality figure caption attaches the percentages to another outcome | REPORT / REPORT |
| NP-F02 | Four-day median follow-up and day-five numbers at risk require incompatible time definitions | REPORT / REPORT |
| NP-F03 | Collapsed-composite forest row changes the effect label to odds ratio | REPORT / REPORT |
| NP-R01 | Mild respiratory failure: forest risk-ratio label does not reconcile with arm event proportions | REPORT / REPORT |
| NP-R02 | Moderate respiratory failure: forest risk-ratio label does not reconcile with arm event proportions | REPORT / REPORT |
| NP-R03 | Severe respiratory failure: forest risk-ratio label does not reconcile with arm event proportions | REPORT / REPORT |
| NP-R04 | Aspiration: forest risk-ratio label does not reconcile with arm event proportions | REPORT / REPORT |
| NP-R05 | Bronchospasm: forest risk-ratio label does not reconcile with arm event proportions | REPORT / REPORT |
| NP-R06 | ARDS: forest risk-ratio label does not reconcile with arm event proportions | REPORT / REPORT |
| NP-R08 | Atelectasis: forest risk-ratio label does not reconcile with arm event proportions | REPORT / REPORT |
| NP-R09 | Cardiopulmonary edema: forest risk-ratio label does not reconcile with arm event proportions | REPORT / REPORT |
| NP-R10 | Pleural effusion: forest risk-ratio label does not reconcile with arm event proportions | REPORT / REPORT |
| NP-R11 | Pneumothorax: forest risk-ratio label does not reconcile with arm event proportions | REPORT / REPORT |
| NP-R12 | Pulmonary infiltrates: forest risk-ratio label does not reconcile with arm event proportions | REPORT / REPORT |

## NP-P01 — Current protocol retains incompatible recruitment totals

**Compared locations and document roles:** [joi190055supp1_prod_16092.pdf, PDF p. 10](../../../../joi190055supp1_prod_16092.pdf#page=10) recruitment target, PLAN; [joi190055supp1_prod_16092.pdf, PDF p. 11](../../../../joi190055supp1_prod_16092.pdf#page=11) revised sample size, PLAN; [joi190055supp1_prod_16092.pdf, PDF p. 12](../../../../joi190055supp1_prod_16092.pdf#page=12) section 7 procedure total, PLAN.

**Printed inputs:** Pages 10–11 specify 2013 patients after re-estimation; page 12 says “A total of 748 patients will be included.” Page 11 labels 748 as the original total.

**Reproducible rule and calculation:** A current protocol procedure total should either match the revised current total or explicitly identify the retained historical total. 2013 − 748 = 1265 participants.

**Tolerance:** Exact integer identity; no rounding tolerance.

**Direct observation versus inference:** Both totals and the original-versus-revised history are direct printed observations. Inferring that section 7 intended the current total is diagnostic; the paragraph does not label 748 as historical.

**Alternatives:** An original paragraph may have been retained intentionally, but its current procedural framing leaves the numeric enrollment target ambiguous. No claim about actual recruitment or treatment allocation follows.

**Quality-control relevance:** An outdated target can be copied as the planned study size.

**Exact human question:** Should section 7's 748 be read as historical, and what is the intended current procedural recruitment total after the 2013-patient revision?

## NP-M01 — Mild respiratory failure uses equality rather than the main report's inclusive oxygen threshold

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 20](../../../../joi190055supp4_prod_16092.pdf#page=20) eMethods section 2.8, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) Table 3 footnote d, REPORT.

**Printed inputs:** Supplement: responding to supplemental oxygen “= 2 L/min”; moderate responds only to “> 2 L/min”. Main footnote: responding to “2 L or less” is mild; >2 is moderate.

**Reproducible rule and calculation:** Equality and an inclusive upper bound define different categories. A response at 1 L/min satisfies oxygen ≤2 L/min but not oxygen =2 L/min. Neither definition changes the shared PaO₂<60 mmHg or SpO₂<90% threshold.

**Tolerance:** Exact categorical relation; no rounding tolerance at a dose below the boundary.

**Direct observation versus inference:** The equals sign was visually confirmed on the direct-source page image; the main inclusive phrase is directly printed. The 1 L/min example is a derived counterexample, not an observed participant.

**Alternatives:** The equals sign may represent a lost ≤ glyph or an intended standard test flow. No supplied count establishes how many participants were affected.

**Quality-control relevance:** A numeric endpoint definition can change downstream interpretation of mild-event counts.

**Exact human question:** Was the supplementary equality intended to mean ≤2 L/min, or was response at exactly 2 L/min a different operational definition from the main Table 3 footnote?

## NP-F01 — Mortality figure caption attaches the percentages to another outcome

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 41](../../../../joi190055supp4_prod_16092.pdf#page=41) eFigure 11 title, y-axis, HR annotation and caption, REPORT; [joi190055supp4_prod_16092.pdf, PDF p. 40](../../../../joi190055supp4_prod_16092.pdf#page=40) eFigure 10 caption, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) Table 3 5-day mortality row, REPORT.

**Printed inputs:** Figure 11 title is probability of death in the first 5 days, axis “5-Day Mortality”, HR1.67 (0.40–6.97), P=.484. Caption names “postoperative extra-pulmonary complications” for high0.5%/low0.3%. Figure 10 extra-pulmonary rates are16.9%/15.2%. Main 5-day deaths are5/989 and3/987.

**Reproducible rule and calculation:** 100×5/989=.50556%→0.5%;100×3/987=.30395%→0.3%. Thus the Figure11 percentages identify mortality, while its caption outcome name identifies the distinct Figure10 outcome.

**Tolerance:** Percentage rounding ±.05 percentage points; incompatible outcome names have no numeric rounding tolerance.

**Direct observation versus inference:** Title, axis, caption and comparator counts are direct observations; assigning the percentages to mortality follows the printed outcome/count match.

**Alternatives:** A copied caption phrase could explain the label; the HR/CI remain coherent with mortality. No conclusion impact is inferred.

**Quality-control relevance:** The labeled percentages could be extracted under the wrong secondary outcome.

**Exact human question:** Does “postoperative extra-pulmonary complications” in the Figure11 caption refer to mortality here, and which outcome label belongs with 0.5% and0.3%?

## NP-F02 — Four-day median follow-up and day-five numbers at risk require incompatible time definitions

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 38](../../../../joi190055supp4_prod_16092.pdf#page=38) caption and all risk-table cells, REPORT; [joi190055supp4_prod_16092.pdf, PDF p. 39](../../../../joi190055supp4_prod_16092.pdf#page=39) caption and all risk-table cells, REPORT; [joi190055supp4_prod_16092.pdf, PDF p. 40](../../../../joi190055supp4_prod_16092.pdf#page=40) caption and all risk-table cells, REPORT; [joi190055supp4_prod_16092.pdf, PDF p. 41](../../../../joi190055supp4_prod_16092.pdf#page=41) caption and all risk-table cells, REPORT.

**Printed inputs:** Each caption states median follow-up4 (2–5) days. Day5 low/high at-risk counts are756/785,756/785,845/828,986/985. Baseline counts are987/989, total1976.

**Reproducible rule and calculation:** If follow-up means the observed time governing those risk tables, at least half of1976 follow-up times must be ≤4 for median4. Thus at most988 can remain at risk on day5 (even allowing both central order statistics and ties). Printed day5 sums1541,1541,1673,1971 exceed988 by553,553,685,983. Even within arms every listed day5 count exceeds half the baseline arm.

**Tolerance:** Counts exact. A median rounded to integer4 would ordinarily lie below4.5, still below5; it cannot explain >half at risk at day5. A distinct follow-up variable could reconcile the statements.

**Direct observation versus inference:** The caption and all48 risk counts are directly printed and checked. The incompatibility is conditional inference that caption follow-up and risk-table follow-up refer to the same observed time.

**Alternatives:** Median4 may refer to postoperative assessment duration while risk tables retain patients through administrative day5, or “number at risk” may be a different denominator. Neither alternative is defined locally. Event/censor timing need not be reconstructed. Identical primary/severe rows alone were not used as a candidate.

**Quality-control relevance:** Time-dependent denominators and follow-up summaries could be reused under incompatible definitions.

**Exact human question:** What exact follow-up duration has median4 (2–5), what removes patients from each Figure8–11 risk table, and how can more than half remain at risk on day5 under that duration?

## NP-F03 — Collapsed-composite forest row changes the effect label to odds ratio

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 lower Global Tests header and Collapsed Composite row, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 primary row and arm sizes, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest header “Odds Ratio (95% CI)”, collapsed composite0.93[0.83,1.04]. Main primary row has the identical tuple under “Risk Ratio”; events211/989 versus233/987. Footnote calls the estimates risk ratios.

**Reproducible rule and calculation:** Binary marginal OR=[211/(989−211)]/[233/(987−233)]=(211×754)/(778×233)=.877644; raw RR=(211/989)/(233/987)=.903748. The same printed0.93 tuple carries different effect labels. The raw diagnostics do not decide which model produced0.93.

**Tolerance:** Printed estimate ±.005; .877644 differs from0.93 by.052356 and does not round0.93. Exact matched-label distinction independent of arithmetic.

**Direct observation versus inference:** Different headers and identical tuple are direct observations. Marginal OR/RR calculations are derived diagnostics under the displayed binary counts.

**Alternatives:** The forest could intentionally use an adjusted odds model; no model identity is specified for this particular row. That alternative still requires identifying why the tuple is identical to the main RR.

**Quality-control relevance:** An effect label determines extraction scale and any later transformation.

**Exact human question:** Is the collapsed-composite forest tuple an odds ratio from a separate model or the main reported risk-ratio tuple, and which calculation and label apply?

## NP-R01 — Mild respiratory failure: forest risk-ratio label does not reconcile with arm event proportions

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Mild respiratory failure row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR0.92[0.76,1.12],99.58%CI; matched main events high135/989,low154/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(135/989)/(154/987)=0.874851. Printed 0.92 differs by0.045149. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the Mild respiratory failure forest row, what population, contrast, numerator/denominator and estimator produced0.92, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

## NP-R02 — Moderate respiratory failure: forest risk-ratio label does not reconcile with arm event proportions

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Moderate respiratory failure row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR0.83[0.59,1.17],99.58%CI; matched main events high42/989,low58/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(42/989)/(58/987)=0.722674. Printed 0.83 differs by0.107326. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the Moderate respiratory failure forest row, what population, contrast, numerator/denominator and estimator produced0.83, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

## NP-R03 — Severe respiratory failure: forest risk-ratio label does not reconcile with arm event proportions

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Severe respiratory failure row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR0.91[0.61,1.34],99.58%CI; matched main events high30/989,low36/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(30/989)/(36/987)=0.831648. Printed 0.91 differs by0.078352. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the Severe respiratory failure forest row, what population, contrast, numerator/denominator and estimator produced0.91, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

## NP-R04 — Aspiration: forest risk-ratio label does not reconcile with arm event proportions

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Aspiration row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR1.33[0.41,4.30],99.58%CI; matched main events high2/989,low1/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(2/989)/(1/987)=1.995956. Printed 1.33 differs by0.665956. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the Aspiration forest row, what population, contrast, numerator/denominator and estimator produced1.33, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

## NP-R05 — Bronchospasm: forest risk-ratio label does not reconcile with arm event proportions

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Bronchospasm row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR1.09[0.62,1.91],99.58%CI; matched main events high12/989,low10/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(12/989)/(10/987)=1.197573. Printed 1.09 differs by0.107573. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the Bronchospasm forest row, what population, contrast, numerator/denominator and estimator produced1.09, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

## NP-R06 — ARDS: forest risk-ratio label does not reconcile with arm event proportions

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 ARDS row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR1.50[0.65,3.44],99.58%CI; matched main events high3/989,low1/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(3/989)/(1/987)=2.993933. Printed 1.50 differs by1.493933. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the ARDS forest row, what population, contrast, numerator/denominator and estimator produced1.50, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

## NP-R08 — Atelectasis: forest risk-ratio label does not reconcile with arm event proportions

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Atelectasis row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR0.88[0.64,1.23],99.58%CI; matched main events high44/989,low55/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(44/989)/(55/987)=0.798382. Printed 0.88 differs by0.081618. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the Atelectasis forest row, what population, contrast, numerator/denominator and estimator produced0.88, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

## NP-R09 — Cardiopulmonary edema: forest risk-ratio label does not reconcile with arm event proportions

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Cardiopulmonary edema row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR1.31[0.87,1.98],99.58%CI; matched main events high17/989,low9/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(17/989)/(9/987)=1.885069. Printed 1.31 differs by0.575069. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the Cardiopulmonary edema forest row, what population, contrast, numerator/denominator and estimator produced1.31, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

## NP-R10 — Pleural effusion: forest risk-ratio label does not reconcile with arm event proportions

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Pleural effusion row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR1.36[1.05,1.76],99.58%CI; matched main events high43/989,low21/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(43/989)/(21/987)=2.043478. Printed 1.36 differs by0.683478. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the Pleural effusion forest row, what population, contrast, numerator/denominator and estimator produced1.36, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

## NP-R11 — Pneumothorax: forest risk-ratio label does not reconcile with arm event proportions

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Pneumothorax row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR0.50[0.04,5.96],99.58%CI; matched main events high1/989,low3/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(1/989)/(3/987)=0.332659. Printed 0.50 differs by0.167341. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the Pneumothorax forest row, what population, contrast, numerator/denominator and estimator produced0.50, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

## NP-R12 — Pulmonary infiltrates: forest risk-ratio label does not reconcile with arm event proportions

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Pulmonary infiltrates row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR0.87[0.49,1.55],99.58%CI; matched main events high14/989,low18/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(14/989)/(18/987)=0.776205. Printed 0.87 differs by0.093795. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the Pulmonary infiltrates forest row, what population, contrast, numerator/denominator and estimator produced0.87, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?


## Complete non-candidate and limitation record

All 120 relationships are checked; candidate-free entries explicitly retain the applicable rule and reason in the inventory. All 19 rescue-step rows reconcile and all15 historical rows preserve bivariate versus multivariate populations/reference groups. All 11 historical nonreference ORs are positive and inside their own CIs; exp(beta) agrees the adjusted OR at one-decimal precision and the supplied repeated REPORT score conversion round(10beta) reproduces every score. Three blank-reference coefficient/score domains plus age reference are not assigned zero without a rule. The n1627 versus1624 model difference is not unexplained arithmetic.

Original total748 is consistent with712×1.05 rounded, though direct retention inversion would yield750; absent inflation convention alone is not a candidate. Revised1912/.95 rounds2013. Exact interim totals reproduce50%/75%/100% of1912. Final efficacy-crossing sum.801 lies within rounding of80% and futility increments sum.200.99.58% reproduces the Bonferroni rule. Historical amendments explaining different numbers remain historical PLAN material.

All 48 risk counts are nonnegative integer counts, individually bounded by the appropriate baseline arm and nonincreasing across printed times. Both primary/severe row vectors repeat exactly; without event/censoring data that repetition alone does not prove a contradiction. NP-F02 instead specifies the incompatible median/risk definitions. HRs, binary proportions, count-component burden, ordinal-count ORs and GEE measures are not treated as interchangeable. “Rate” beside a percentage does not itself establish person-time incidence; no person-time denominator is printed.

All 16 forest intervals are positive/ordered and contain their point estimates. Pulmonary infection RR1.00 agrees10/989 divided by10/987=.997978 within.005, so no forest count-versus-RR candidate is emitted for that row. Different99.58% versus95% CI levels are preserved; no invalid interval identity comparison is made. The separate-model three global rows match eTable9 tuple labels exactly. Small point differences between main95% rows and forest99.58% rows are retained in the full inventory but not independently diagnosed without matching estimator details.

All plot ticks, five repeated-time labels, direction/reference lines, percentage/fraction conversions, confidence-bar labels and interaction-test labels are checked. Exact unlabeled point/interval coordinates and early stopping-curve coordinates are not supplied, so no decimal values are reconstructed from pixel positions. Peak and plateau pressure are kept distinct. The original plan's adjacent “odds ratio relative risks” phrase is preserved as ambiguity without a numerical estimate to arbitrate. Hemoglobin7mg/dL and lactate4mmol/dL appear unusual but lack a supplied conflicting conversion/measurement; no clinical-plausibility-only candidate is registered. DIC thresholds can be read hierarchically; no forced overlap arithmetic candidate.

Administrative/bibliography/qualitative PLAN pages retain explicit no-applicable mapper records, including DOC006p1. No Office/workbook/CSV source exists. No scientific unit omitted; limits concern absent exact graph coordinates, variance/model details, dropout conventions, and the caption/risk follow-up definition. All human questions are precisely attached to printed quantitative contradictions above.

