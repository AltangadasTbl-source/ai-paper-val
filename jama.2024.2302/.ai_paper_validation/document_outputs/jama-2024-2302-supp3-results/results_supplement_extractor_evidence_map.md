# Results Supplement Evidence Map — jama-2024-2302-supp3-results

## Processing result

- **Document:** `joi240020supp3_prod_1710443209.75411.pdf` (results supplement; PDF pp. 2–5 audited only).
- **Evidence source:** retained 300-dpi renders in `preprocessing/page_images/page-002.png` through `page-005.png`. Native PDF glyph mappings on these pages are corrupted and were not used as the authoritative wording.
- **Not audited by design:** PDF p. 1 and pp. 6–8. Protocol (`jama-2024-2302-supp1-protocol`) and SAP (`jama-2024-2302-supp2-sap`) were not opened or scientifically audited; they remain **Not Audited by Design** absent a parent-requested protocol-to-report comparison.
- **Scope outcome:** eTable 1 provides enrollment/refusal accounting; eTable 2 provides a frequentist primary SAE analysis and a major secondary hospital-days analysis. No subgroup analysis, sensitivity analysis, figure/flow diagram, or individual adverse-event-type table occurs on audited pp. 2–5.

## eTable 1 — Additional information related to trial enrollment

| PDF page | Table section / source cell(s) | Visually verified evidence | Accounting / cross-document anchor |
|---|---|---|---|
| 2–3 | `Determined at site level to be ineligible due to “associated factor affecting the timing of hernia repair”` | p. 2: incarceration during NICU 10; multiple prior abdominal operations 5; severe respiratory disease 5; hernia contains ovary, preferred early 4; severe cardiac disease 4; airway anomaly requiring operation 2; research team contacted too close to anticipated discharge, enrollment not feasible 2; associated undescended testicle 2; viral upper respiratory infection 2; COVID restriction (no elective operation allowed) 2; transferring to nonparticipating hospital closer to home 2; on anticoagulant therapy 1; very large hernia, surgeon preferred early repair 1; infant considered too small 1; unsure if hydrocele or hernia, prefer to wait 1; want to coordinate for ophthalmology procedure 1; coordinating with neurosurgery (shunt placement) 1. p. 3 continuation: planning for G tube placement 1; severe pulmonary hypertension 1; unexplained thrombocytopenia 1; await discontinuation of steroids 1; believed hernia was causing feeding intolerance 1. | The displayed row counts total **51**, but this section supplies no printed section denominator; treat 51 only as a row-sum anchor, not a stated enrollment total. |
| 3 | `Reasons for refusal of randomization by parents/guardians (n=613)` | Preferred early repair 280; preferred late repair 196; preferred that physician decided timing of hernia repair 71; no reason given 66. | 280 + 196 + 71 + 66 = **613**, agreeing with the printed denominator. |
| 3 | `Reasons for refusal of randomization by physician (n=37)` | Preferred early repair 14; preferred late repair 14; no reason given 9. | 14 + 14 + 9 = **37**, agreeing with the printed denominator. |
| 3–4 | `“Other reasons” for eligible infants not being consented (n=16)` | p. 3: non-English speaking and consent forms only available in English 4; COVID restrictions 4; custody issues 3. p. 4 continuation: hernia incarceration concerns while in NICU 2; insurance reasons 1; medically unstable 1; transfer for cardiac surgery 1. | 4 + 4 + 3 + 2 + 1 + 1 + 1 = **16**, agreeing with the printed denominator. |

## eTable 2 — Frequentist primary and major secondary outcome analyses

| PDF page / exact table row | Early repair | Late repair | Effect estimate(s) and P value(s) | Analysis statement / comparison anchor |
|---|---:|---:|---|---|
| 5, `Infant had ≥ 1 SAE` (Primary outcome) | 44/159 (28%) | 27/149 (18%) | Risk difference **−9.0%** (95% CI, **−16.5% to −2.0%**), **P=.01**; relative risk **0.65** (95% CI, **0.46–0.92**), **P=.01**. | Group denominators are 159 early and 149 late (total **308**); this is the core SAE cross-document anchor. No individual SAE-type rows appear in audited pages. |
| 5, `Total hospital days during study period, median (IQR)` (Secondary outcome) | 19.0 (9.8, 35) | 16.0 (7, 38) | Relative risk **0.91** (95% CI, **0.74–1.12**), **P=.36**. The risk-difference and adjacent P-value cells are blank for this row. | Major secondary-outcome cross-document anchor. |
| 5, note beneath eTable 2 | — | — | Primary outcome: logistic mixed-effect model; total hospital days: negative binomial mixed model. All models included gestational-age group as covariate and center as random intercept. Frequentist and Bayesian analyses used the same models **except** the frequentist primary analysis, which used a generalized estimating equation logistic model (exchangeable center correlation) because the mixed-effect model did not converge. | Supports comparison of reported analysis/model wording, without consulting the SAP or protocol. |

## Unreadable or uncertain values

- **None in the visually inspected table cells.** Values and labels above were read from the page renders, not inferred from corrupted native glyphs.
- The direction convention for the displayed primary-outcome risk difference is **not explicitly defined in eTable 2**; retain it exactly as printed (−9.0%) rather than inferring a contrast direction.

## Candidate-issue status

No error diagnosis is made in this extraction. The table provides the source values and arithmetic anchors for downstream checks only.
