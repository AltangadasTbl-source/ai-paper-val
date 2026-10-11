# Statistical relationship inventory — pass 1 support outcomes shard

Fresh runtime identity: `/root/statistics_1_outcomes`; model `gpt-6.1-sol`; reasoning effort `high`; stage `statistics_pass_1`; start mode `FRESH_SPAWN`. Coordinator holds the spawn-return runtime ID for the execution manifest. Assigned scope is exclusively REPORT DOC-004 physical pp.21–23, eTables5–7, with exact associated method/footnote text and matched main REPORT context. No PLAN family, baseline table, or figure is independently assigned here. There are 66 printed estimate/95% CI tuples and three associated method relationships: S320–S388, 69 total. Every record below is PASS_1_COMPLETE; pass 2 requires a different fresh runtime.

Sources: `joi170166supp3_prod.pdf` pp.21–23 and main context `jama_huffman_2018_oi_170166.pdf` pp.3,7–9. Reusable layout text and current support/main maps were locator aids. Source-page layout was checked directly with Poppler 25.03.0 `pdftotext -layout -f 21 -l 23 joi170166supp3_prod.pdf -`; all three source-matched page images were visually inspected. Sources and reusable assets were preserved. No OCR engine, GPU, web, old candidate/report conclusions, or Python scientific/extraction helper was used.

## Shared check definitions

For every printed tuple, check lower ≤ point estimate ≤ upper, endpoint order, and positive OR limits; all 66 satisfy these at the printed precision. Direction refers to intervention versus control; a negative marginal RD corresponds to OR below1 and a positive RD to OR above1. All paired directions in eTable7 agree. No P value, test statistic, standard error, interval-construction method, variance estimator, covariance, or degrees of freedom is supplied with these tuples. Confidence level95% is explicit. The article gives two-sided decision thresholds, but that does not establish a particular Wald or likelihood-ratio construction for these sensitivity/exploratory intervals. No unreported test is inferred, no interval-derived P value is substituted, and no diagnostic approximation is treated as an analysis reproduction.

eTable5 model keys: G=GRACE covariates; T=transfer status; I=insurance status; A=prehospital aspirin. Every column additionally accounts for hospital clustering and temporal trends. GRACE variables are age, gender, STEMI/NSTEMI status, systolic pressure, heart rate, creatinine, in-hospital heart failure, cardiogenic shock, cardiac arrest. Clinical-event OR below1 favors fewer events; process/advice OR above1 favors more receipt. All intervals in the clinical-event rows include1. Medication rows exclude1 above it; advice intervals include1. No row-specific significance assertion is printed.

eTable6 model key X=clustering, temporal trends and exposure-time interaction as labelled. The main article pp.3,8 describes a post hoc examination of time spent/exposed × intervention and says overall effects were similar. Exposure coding, unit, centering/reference value, the interaction coefficient, and its test are not printed. Preserve these as missing definitions; the table and article identify an interaction-adjusted sensitivity analysis, not an unchanged primary-model occurrence. Every clinical/advice/in-hospital medication interval includes1; discharge medication excludes1 above it.

eTable7 model keys C=cluster-only mixed-effects logistic model with hospital random effect; P=primary analysis additionally including temporal trends. RD is marginal intervention minus control in percentage points; OR is intervention/control. Expanded composite adds incident in-hospital heart failure, cardiogenic shock or cardiac arrest to30-day MACE. Printed arm denominators10066/11308 and component populations are retained; composite components are not assumed disjoint. The primary expanded result and cluster expanded result exactly match main pp.8–9.

## All estimate/interval records

In the Check cell, `contained; ordered` explicitly records both checks. Method and missing-definition checks for each tuple also use the shared definitions and the corresponding S386/S387/S388 record.

| S ID | REPORT source page/table | Outcome | Model/effect | Printed estimate (95% CI) | Check and null relation | Pass 1 |
|---|---|---|---|---|---|---|
| S320 | DOC-004 p.21 eTable5 | 30-day MACE | G OR | 1.06 (0.77–1.44) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S321 | DOC-004 p.21 eTable5 | 30-day MACE | T OR | 0.98 (0.80–1.21) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S322 | DOC-004 p.21 eTable5 | 30-day MACE | I OR | 0.97 (0.79–1.20) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S323 | DOC-004 p.21 eTable5 | 30-day MACE | A OR | 0.99 (0.80–1.22) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S324 | DOC-004 p.21 eTable5 | 30-day mortality | G OR | 0.98 (0.67–1.43) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S325 | DOC-004 p.21 eTable5 | 30-day mortality | T OR | 0.94 (0.74–1.19) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S326 | DOC-004 p.21 eTable5 | 30-day mortality | I OR | 0.93 (0.73–1.18) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S327 | DOC-004 p.21 eTable5 | 30-day mortality | A OR | 0.95 (0.75–1.20) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S328 | DOC-004 p.21 eTable5 | 30-day cardiovascular mortality | G OR | 1.00 (0.68–1.47) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S329 | DOC-004 p.21 eTable5 | 30-day cardiovascular mortality | T OR | 0.94 (0.74–1.19) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S330 | DOC-004 p.21 eTable5 | 30-day cardiovascular mortality | I OR | 0.93 (0.73–1.18) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S331 | DOC-004 p.21 eTable5 | 30-day cardiovascular mortality | A OR | 0.95 (0.75–1.20) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S332 | DOC-004 p.21 eTable5 | In-hospital mortality | G OR | 1.07 (0.65–1.76) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S333 | DOC-004 p.21 eTable5 | In-hospital mortality | T OR | 0.92 (0.70–1.22) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S334 | DOC-004 p.21 eTable5 | In-hospital mortality | I OR | 0.91 (0.69–1.20) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S335 | DOC-004 p.21 eTable5 | In-hospital mortality | A OR | 0.93 (0.71–1.23) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S336 | DOC-004 p.21 eTable5 | 30-day reinfarction | G OR | 1.39 (0.74–2.60) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S337 | DOC-004 p.21 eTable5 | 30-day reinfarction | T OR | 1.38 (0.86–2.21) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S338 | DOC-004 p.21 eTable5 | 30-day reinfarction | I OR | 1.39 (0.87–2.22) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S339 | DOC-004 p.21 eTable5 | 30-day reinfarction | A OR | 1.40 (0.87–2.24) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S340 | DOC-004 p.21 eTable5 | 30-day stroke | G OR | 0.93 (0.46–1.89) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S341 | DOC-004 p.21 eTable5 | 30-day stroke | T OR | 1.23 (0.70–2.14) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S342 | DOC-004 p.21 eTable5 | 30-day stroke | I OR | 1.21 (0.70–2.12) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S343 | DOC-004 p.21 eTable5 | 30-day stroke | A OR | 1.23 (0.70–2.15) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S344 | DOC-004 p.21 eTable5 | 30-day major GUSTO bleeding | G OR | 2.90 (0.77–10.87) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S345 | DOC-004 p.21 eTable5 | 30-day major GUSTO bleeding | T OR | 2.33 (0.93–5.88) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S346 | DOC-004 p.21 eTable5 | 30-day major GUSTO bleeding | I OR | 2.26 (0.89–5.71) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S347 | DOC-004 p.21 eTable5 | 30-day major GUSTO bleeding | A OR | 2.35 (0.93–5.92) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S348 | DOC-004 p.21 eTable5 | Optimal in-hospital medication | G OR | 2.19 (1.83–2.62) | contained; ordered; above1 | PASS_1_COMPLETE |
| S349 | DOC-004 p.21 eTable5 | Optimal in-hospital medication | T OR | 1.47 (1.29–1.66) | contained; ordered; above1 | PASS_1_COMPLETE |
| S350 | DOC-004 p.21 eTable5 | Optimal in-hospital medication | I OR | 1.45 (1.28–1.64) | contained; ordered; above1 | PASS_1_COMPLETE |
| S351 | DOC-004 p.21 eTable5 | Optimal in-hospital medication | A OR | 1.47 (1.30–1.66) | contained; ordered; above1 | PASS_1_COMPLETE |
| S352 | DOC-004 p.21 eTable5 | Optimal discharge medication | G OR | 1.50 (1.27–1.78) | contained; ordered; above1 | PASS_1_COMPLETE |
| S353 | DOC-004 p.21 eTable5 | Optimal discharge medication | T OR | 1.61 (1.42–1.82) | contained; ordered; above1 | PASS_1_COMPLETE |
| S354 | DOC-004 p.21 eTable5 | Optimal discharge medication | I OR | 1.61 (1.43–1.83) | contained; ordered; above1 | PASS_1_COMPLETE |
| S355 | DOC-004 p.21 eTable5 | Optimal discharge medication | A OR | 1.61 (1.42–1.82) | contained; ordered; above1 | PASS_1_COMPLETE |
| S356 | DOC-004 p.21 eTable5 | Tobacco cessation advice | G OR | 0.84 (0.42–1.67) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S357 | DOC-004 p.21 eTable5 | Tobacco cessation advice | T OR | 1.05 (0.67–1.66) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S358 | DOC-004 p.21 eTable5 | Tobacco cessation advice | I OR | 1.05 (0.66–1.66) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S359 | DOC-004 p.21 eTable5 | Tobacco cessation advice | A OR | 1.07 (0.68–1.69) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S360 | DOC-004 p.22 eTable6 | 30-day MACE | X OR | 1.14 (0.76–1.70) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S361 | DOC-004 p.22 eTable6 | 30-day mortality | X OR | 0.98 (0.63–1.52) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S362 | DOC-004 p.22 eTable6 | 30-day cardiovascular mortality | X OR | 1.00 (0.64–1.56) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S363 | DOC-004 p.22 eTable6 | In-hospital mortality | X OR | 1.43 (0.83–2.46) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S364 | DOC-004 p.22 eTable6 | 30-day reinfarction | X OR | 2.81 (0.79–9.94) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S365 | DOC-004 p.22 eTable6 | 30-day stroke | X OR | 2.06 (0.58–7.36) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S366 | DOC-004 p.22 eTable6 | 30-day major GUSTO bleeding | X OR | 2.53 (0.50–12.94) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S367 | DOC-004 p.22 eTable6 | Optimal in-hospital medication | X OR | 0.87 (0.70–1.07) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S368 | DOC-004 p.22 eTable6 | Optimal discharge medication | X OR | 1.45 (1.12–1.88) | contained; ordered; above1 | PASS_1_COMPLETE |
| S369 | DOC-004 p.22 eTable6 | Tobacco cessation advice | X OR | 0.99 (0.37–2.66) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S370 | DOC-004 p.23 eTable7 | Expanded 30-day MACE | C RD, percentage points | −0.86 (−1.72 to −0.01) | contained; ordered; below0; direction agrees S371 | PASS_1_COMPLETE |
| S371 | DOC-004 p.23 eTable7 | Expanded 30-day MACE | C OR | 0.89 (0.80–1.00) | contained; ordered; point below1; endpoint at displayed1 | PASS_1_COMPLETE |
| S372 | DOC-004 p.23 eTable7 | Expanded 30-day MACE | P RD, percentage points | −1.34 (−2.72 to0.04) | contained; ordered; includes0; direction agrees S373 | PASS_1_COMPLETE |
| S373 | DOC-004 p.23 eTable7 | Expanded 30-day MACE | P OR | 0.84 (0.70–1.00) | contained; ordered; point below1; endpoint at displayed1 | PASS_1_COMPLETE |
| S374 | DOC-004 p.23 eTable7 | In-hospital heart failure | C RD, percentage points | −0.03 (−0.45 to0.40) | contained; ordered; includes0; direction agrees S375 | PASS_1_COMPLETE |
| S375 | DOC-004 p.23 eTable7 | In-hospital heart failure | C OR | 0.99 (0.79–1.24) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S376 | DOC-004 p.23 eTable7 | In-hospital heart failure | P RD, percentage points | −0.52 (−1.22 to0.17) | contained; ordered; includes0; direction agrees S377 | PASS_1_COMPLETE |
| S377 | DOC-004 p.23 eTable7 | In-hospital heart failure | P OR | 0.76 (0.54–1.07) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S378 | DOC-004 p.23 eTable7 | In-hospital cardiogenic shock | C RD, percentage points | −0.06 (−0.42 to0.30) | contained; ordered; includes0; direction agrees S379 | PASS_1_COMPLETE |
| S379 | DOC-004 p.23 eTable7 | In-hospital cardiogenic shock | C OR | 0.96 (0.77–1.21) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S380 | DOC-004 p.23 eTable7 | In-hospital cardiogenic shock | P RD, percentage points | −0.20 (−0.80 to0.40) | contained; ordered; includes0; direction agrees S381 | PASS_1_COMPLETE |
| S381 | DOC-004 p.23 eTable7 | In-hospital cardiogenic shock | P OR | 0.89 (0.62–1.27) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S382 | DOC-004 p.23 eTable7 | In-hospital cardiac arrest | C RD, percentage points | 0.16 (−0.31 to0.62) | contained; ordered; includes0; direction agrees S383 | PASS_1_COMPLETE |
| S383 | DOC-004 p.23 eTable7 | In-hospital cardiac arrest | C OR | 1.08 (0.87–1.33) | contained; ordered; includes1 | PASS_1_COMPLETE |
| S384 | DOC-004 p.23 eTable7 | In-hospital cardiac arrest | P RD, percentage points | −0.20 (−0.94 to0.55) | contained; ordered; includes0; direction agrees S385 | PASS_1_COMPLETE |
| S385 | DOC-004 p.23 eTable7 | In-hospital cardiac arrest | P OR | 0.91 (0.65–1.28) | contained; ordered; includes1 | PASS_1_COMPLETE |

## Associated method records

| S ID | Exact locations and roles | Source-grounded method check, missing definitions, and matched implications | Pass 1 |
|---|---|---|---|
| S386 | REPORT DOC-004 p.21 eTable5 title/footnotes a–e; REPORT DOC-001 p.3 Statistical Analysis and Outcomes, p.8 Secondary and Post Hoc Analyses | Four separate sensitivity adjustments are explicitly distinguished, not assumed simultaneous. Hospital clustering/time and GRACE covariates align with the main model description. MACE and GUSTO definitions match; optimal medication eligibility/discharge and baseline-smoker counseling populations are explicit. Main30-day death0.94(0.74–1.19) and GRACE0.98(0.67–1.43) each include1; the main statement of no material change is coherent with those results. GRACE-column analytic sample, covariate missingness implementation, row SEs/tests and interval construction are not supplied here. No sample count or handling method is invented, and these absences alone do not establish a contradiction. No relevant superiority, equivalence, noninferiority or stopping conclusion is printed in this table. | PASS_1_COMPLETE |
| S387 | REPORT DOC-004 p.22 eTable6 title/footnotes a–d; REPORT DOC-001 p.3 Statistical Analysis and p.8 post hoc interaction paragraph; corroborative REPORT DOC-004 p.21 eTable5 medication footnote | Post hoc exposure-time interaction analysis is identified in both locations; compare it as a different model, not a repeated primary-model estimate. Exposure unit/coding, centering/reference, coefficient-specific estimand, interaction coefficient/test and covariance are absent, so no conditional effect at a chosen time or interaction P value is recoverable. Main description of overall similar effects does not assert unchanged values for every exploratory process measure. In-hospital medication0.87(0.70–1.07) differs from other sensitivity models, but model identity differs. Heparin versus anticoagulant naming is not evidence of a quantity-changing definition absent source evidence that alternate drugs change this composite. Missing items and secondary-row comparison are self-screened in the checker. No superiority/noninferiority/equivalence or stopping decision is asserted. | PASS_1_COMPLETE |
| S388 | REPORT DOC-004 p.23 eTable7 title/header/footnote a; REPORT DOC-001 p.3 Statistical Analysis and pp.8–9 expanded-endpoint narrative | Mixed-effects logistic model with hospital random effect explicitly accounts for clustered design; primary additionally accounts for temporal trends. OR and marginal RD are distinctly defined and paired point directions agree for all eight model/outcome pairs. Printed counts/percentages reconcile at one decimal: control/intervention expanded919/795 with9.1/7.0%; HF227/191 with2.3/1.7%; shock217/170 with2.2/1.5%; arrest206/237 with2.0/2.1%, denominators10066/11308. Counts do not reconstruct modeled estimates. Main expanded OR0.89(0.80–1.00), primary OR0.84(0.70–1.00), primary RD−1.34(−2.72 to0.04), and rates exactly match. OR upper1.00 has rounding interval[0.995,1.005], so it does not settle whether an unrounded limit crossed1. No exact P/SE/test statistic is printed; no assumption of disjoint event components or identical RD/OR interval construction is made. ICC values0.15/0.23/0.25/0.20 are each within[0,1]; the source does not supply their estimation equation, so no reconstructed variance is asserted. | PASS_1_COMPLETE |

## Pass-1 completion and limitations

69 of69 assigned statistical relationships completed; 66 of66 printed estimate/CI tuples checked. Zero emitted findings. Every exclusion and its single reason code appears once in `checkers/parts/statistical_support_outcomes.md`. Missing model quantities above limit numerical reproduction, not coverage. No direct-source unit in this shard is omitted. All S320–S388 require explicit PASS_2_COMPLETE entries by a different fresh pass-2 agent after the ledger, independent screening and mechanical evidence recheck exist.
