# DOC-001 Main-Paper Quantitative Evidence Map

## Scope, method, and page coverage

- **Source:** `jama_wilson_2020_oi_190154.pdf` (DOC-001), PDF pages 1-11.
- **Reusable locator:** one usable native-text file per exact source page under `.ai_paper_validation/preprocessing/native_text/JAMA2019_22343_MAIN/`.
- **Direct-source confirmation:** fresh `pdftotext -layout -f N -l N` extraction of the supplied PDF was inspected for pages 1-11; pages 1 and 4-8 contain the result-relevant evidence. The PDF remains authoritative.
- **Coverage result:** pp. 1-11 all mapped. Pages 10-11 are reference-only for this scope; page 2 supplies eligibility/time context and page 3 supplies definitions/analysis rules. No OCR was needed.

## Definitions governing every mapped result

PDF p. 3 states that analyses use patients assigned at randomization for RCTs and initially assigned patients for observational studies. Binary outcomes use OR, RD, and 95% CI; continuous outcomes use change-from-baseline where available, otherwise postintervention data; SMD is used across different measures. The stated SMD standardization direction is **higher scores represent better outcomes**. Count outcomes (more than one event per patient, including admissions and adverse events) use RR, defined as the ratio of incidence rates between intervention and control. DerSimonian-Laird random effects are used except comparisons with fewer than 3 studies, which use fixed-effect Mantel-Haenszel. I2 is the heterogeneity indicator; two-tailed P < .05 is statistically significant; post-hoc subgroup findings are exploratory owing to no multiplicity adjustment.

## Page-level result evidence

### PDF p. 1 — abstract (matched summary relationships)

21 RCTs and 12 observational studies, 51,085 patients; mean (SD) age 65.7 (2.1) years; 43% women; 434 deaths and 27 intubations. BPAP versus no device: mortality 22.31% vs 28.57%, RD -5.53% (95% CI -10.29% to -0.76%), OR 0.66 (0.51-0.87), P=.003, 13 studies/1423 patients/SOE moderate; patients with admissions 39.74% vs 75.00%, RD -35.26% (-49.39% to -21.12%), OR 0.22 (0.11-0.43), P<.001, 1 study/166/SOE low; intubation 5.34% vs 14.71%, RD -8.02% (-14.77% to -1.28%), OR 0.34 (0.14-0.83), P=.02, 3 studies/267/SOE moderate; admission count RR 0.91 (0.71-1.17), P=.47, 5 studies/326/SOE low; quality-of-life SMD 0.16 (-0.06 to 0.39), P=.15, 9/833/SOE insufficient. HMV versus no device: admission-count RR 0.50 (0.35-0.71), P<.001, 1/93/SOE low; mortality 21.84% vs 34.09%, RD -11.99% (-24.77% to 0.79%), OR 0.56 (0.29-1.08), P=.49, 2/175/SOE insufficient. Adverse-event count 0.18 vs 0.17 per patient, P=.84, 6/414.

### PDF pp. 2-3 — eligibility, population, and analysis labels

Eligible adults were at least 18 years with chronic hypercapnic respiratory failure due to COPD, NIPPV at home/assisted living for at least 1 month, comparison with usual care or another NIPPV mode/type, outcome reporting, English-language articles after 1994. Primary outcomes: mortality, all-cause hospital admission, intubation, quality of life, at longest follow-up. Secondary outcomes include respiratory admissions, ED/ICU admissions, exacerbations, daily living, dyspnea, sleep, exercise, adverse events. PaCO2 categories are 45-49, 50-51, and >=52 mm Hg; stable COPD is no recent exacerbation and recent exacerbation is <=1 month prior.

### PDF p. 4 — Figures 1 and 2, study totals, and source population

Figure 1 mortality is fully transcribed in `parts/main_numeric_relationships.md` (MN001); it gives 13 BPAP/no-device study rows, 2 HMV/no-device rows, event/patient denominators, individual OR/95% CI/weight, and BPAP, HMV, and all-NIPPV pooled ORs. Figure 2 admission counts is fully transcribed in MN002: 5 BPAP/no-device and 1 HMV/no-device rows, group patient counts, RR/95% CI/weight, and pooled rows. The p. 4 narrative reports 6222 search citations plus 83 additional citations; 33 studies/34 articles; 51,085 patients; mean (SD) age 65.7 (2.1); 43% women; 21 RCTs and 12 observational studies; country counts US 4, Canada 1, Europe 23, Asia 3, Africa 1, Australia 1; all enrolled at home and none in assisted living.

### PDF p. 5 — Figures 3 and 4 and BPAP primary results

Figure 3 intubation (MN003) has three BPAP/no-device rows: Casanova 1/26 vs 2/26, OR 0.48 (0.04-5.65), 13.4%; Galli 5/78 vs 16/88, 0.31 (0.11-0.89), 73.2%; Tsolaki 1/27 vs 2/22, 0.38 (0.03-4.55), 13.4%; pooled I2=0.0%, heterogeneity P=.94, OR 0.34 (0.14-0.83), weight 100%.

Figure 4 quality of life (MN004) has nine rows with group counts, scale, SMD/95% CI and weights, and a pooled I2=61.7%, heterogeneity P=.007, SMD 0.16 (-0.06 to 0.38), 100%. The page narrative gives all BPAP primary result values reproduced at p. 1 and identifies 15 RCTs and 6 observational studies. It also lists significant secondary directions and study/patient counts: ED visits 1/195; patients with ICU admissions 1/166; dyspnea 6/468; shuttle walk 1/45. It lists nonsignificant outcomes and study/patient counts: respiratory admissions 1/201; ICU admission count 2/81; COPD exacerbation count 4/352; patients with exacerbation 1/52; daily living 3/318; sleep 2/120; 6-min walk 7/271.

### PDF p. 6 — Table 1 and combined/device comparisons

Table 1 is fully transcribed in MN005, including all outcome labels, study populations, estimates, intervals, P values, I2, and footnotes. It reports HMV/no-device admission-count RR 0.50 (0.35-0.71), P<.001, 1/93/SOE low, and mortality 21.84% vs 34.09%, RD -11.99% (-24.77% to 0.79%), OR 0.56 (0.29-1.08), P=.49, 2/175/SOE insufficient. Combined NIPPV/no-device: mortality 22.26% vs 29.20%, RD -6.29% (-11.50% to -1.08%), OR 0.65 (0.48-0.88), P<.01, 15/1598/SOE moderate; admission patients 39.74% vs 75.00%, RD -35.26% (-49.39% to -21.12%), OR .22 (.11-.43), P<.001, 1/166/SOE low; intubation 5.34% vs 14.71%, RD -8.02% (-14.77% to -1.28%), OR .34 (.14-.83), P=.02, 3/267/SOE moderate; quality SMD .16 (-.06 to .39), 9/833/SOE insufficient; admission count RR .75 (.52-1.10), 6/419/SOE low.

Other comparisons: observational HMV vs BPAP/CPAP, 48,856 patients, fewer all-cause admissions and HMV vs CPAP fewer respiratory-admission patients (no estimates displayed); BPAP vs CPAP RCT, 49 patients, COPD-exacerbation patients 30.43% vs 53.85%, RD -23% (-50% to 3%), OR .38 (.12-1.22), P=.10; RCT n=26, >6 months BPAP 43% increase vs <6 months 11% reduction in 6-min walk, P=.04; observational n=54, adherent threshold >=4 h/day on >=70% of days.

### PDF p. 7 — other comparisons and subgroup results

The remaining other-comparison, stable/recent-exacerbation, PaCO2, and study-design results are transcribed in MN006-MN010 and MS021-MS038. Directly printed values include: adherent/nonadherent admissions 0.4 vs 1.0 per patient, P=.006; ICU admissions .6 vs 1.2, P=.37. High/low intensity n=14: QOL WMD 2.30 (-2.23 to 6.83), P=.32. BPAP mode RCT n=40: mortality 5.00% vs 10.00%, RD -5% (-21 to 11), OR .47 (.04-5.69), P=.56; QOL WMD -4.70 (-15.97 to 6.57), P=.41; shuttle WMD -4.00 m (-54.24 to 46.24), P=.88; sleep WMD -2.70 (-6.07 to .67), P=.12. Home/hospital RCT n=67: mortality 6.06% vs 2.94%, RD 3% (-7 to 13), OR 2.13 (.18-24.67), P=.55; QOL -1.20 (-9.92 to 7.52), P=.79; dyspnea .10 (-.50 to .70), P=.74; 6-min -19.00 m (-64.60 to 29.60), P=.41; admission number -.10 (-.60 to .40), P=.40. HMV-mode RCT n=17: QOL -.14 (-4.90 to 4.60), P=.95; 6-min 14 (-42 to 70), P=.58. Stable versus acute patients have survival 52.6 vs 28.6 months, P=.03.

### PDF p. 8 — Table 2, adverse events, discussion label

Table 2 is fully transcribed in MN011/MS039-MS043. It reports post-hoc design-specific primary outcomes, all with explicit study count/patient denominator/estimate/CI/I2. Adverse events: 11/33 studies reported rates; direct NIPPV/no-device comparison in 6 studies gave RR 1.08 (.52-2.21), P=.84, I2=36.7%; NIPPV pooled incidence total .21 per patient (.12-.37), I2=75.2%; serious 0 (.00-.01), I2=89.6%; nonserious .24 (.12-.47), I2=82.5%. The discussion re-states BPAP direction (lower mortality, admission, intubation; no QOL difference) and HMV direction (lower admission but not mortality), and says RCT-only results were not statistically significant.

### PDF p. 9 — discussion/conclusion and limitations

No new numeric result estimate beyond repeated conclusion statements. Quantitative context: 12/31 included studies had low PaCO2 threshold >45 or >46 mm Hg; three mortality-benefit studies used >50, >52.5, >53; 65% of included studies did not evaluate adverse events or use a consistent reporting approach. Conclusions reproduce the p. 1 claims.

### PDF pp. 10-11 — no applicable result units

Reference lists only; no paper-result counts, estimates, denominators, intervals, P values, tests, model labels, or matching numeric claims to map.

## Candidate observations for later independent checking (no stable IDs or adjudication)

1. **Quality-of-life pooled interval transcription difference.** Direct PDF p. 5 Figure 4 prints SMD 0.16 (95% CI -0.06 to **0.38**); p. 5 narrative and p. 1 abstract print the matched SMD 0.16 (95% CI -0.06 to **0.39**). Same outcome, BPAP/no-device comparison, 9 studies/833 patients. Direct observation is the 0.01 upper-limit difference. The source does not state an alternate population/model explaining it; a rounding/display-level difference remains a possible source-grounded explanation.
2. **HMV mortality P value versus printed estimate/interval.** Direct PDF pp. 1 and 6 print HMV/no-device OR 0.56 (95% CI 0.29-1.08) and P=.49 (two observational studies/175 patients). PDF p. 4 Figure 1 prints the same OR/CI but does not print the effect-test P (its P=.01 is explicitly the HMV heterogeneity P). Under the stated two-tailed analysis convention, a log-OR diagnostic based on the printed 95% CI gives an approximate two-sided P near .08, not .49. This is a diagnostic only; the exact pooling variance/test convention is not printed. Human question: does P=.49 correspond to another analysis/quantity, or is one displayed inferential value incorrect?
3. **Quality-of-life direction label conflict.** PDF p. 3 says direction was standardized so higher scores represent better outcomes. PDF p. 8 Table 2 footnote b says higher scores indicate worse quality of life. Figure 4 labels negative SMDs “Favors NIPPV” and positive SMDs “Favors No NIPPV,” while the group-subtraction order is not stated. Direct observation is a non-reconciled polarity description across locations. Human question: what sign transformations and subtraction convention were used, and which table footnote and figure favor labels were intended for the standardized SMDs?

## Limitations

This mapper did not use legacy candidate/checker/report conclusions and did not inspect support-source units. Figure-derived study-level values are exact printed transcriptions; no external source study was consulted. The source does not give all meta-analytic standard errors, exact effect-test P values in the forest plots, or complete model variance details, so interval-to-P diagnostics are explicitly approximate.
