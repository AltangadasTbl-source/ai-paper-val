# Statistical Relationship Inventory — Pass 1

## Scope, evidence, and checking rules

- **Pass:** 1 of 2; **runtime agent ID:** `/root/statistical_pass_1`; **model/effort:** `gpt-5.6-terra` / `high`; **completion marker for this inventory:** `PASS_1_COMPLETE`.
- **Assigned direct-source scope:** main article PDF pp. 1-10; protocol PDF pp. 1-15; SAP excerpt PDF p. 1; results supplement PDF pp. 1-15. The mapped source coverage is complete in `source_coverage.md`.
- **Source-matched maps used:** `extraction/main_quantitative_evidence.md` and `extraction/support_quantitative_evidence.md`. Direct-source text was additionally inspected for main PDF pp. 4, 6-7; protocol pp. 5 and 12; SAP p. 1; results supplement eTable 1 (p. 2) and eTable 4 (pp. 5-7).
- **Checks applied to every applicable record:** point estimate containment in its displayed interval; endpoint order; sign/direction against the stated measure and contrast; effect-measure/scale label; matching repeated locations; and P-value/interval compatibility only as a labelled diagnostic where the source supplied a compatible 95% CI, two-sided testing statement, and common analysis description. The supplied linear-mixed-model description does **not** state covariance structure, degrees of freedom, variance estimator, or each CI/P-value calculation rule; no exact reconstruction or inferential convention was assumed.
- **Diagnostic convention:** `CI/P diagnostic` means only that a conventional two-sided normal approximation using the printed 95% interval was visually compatible or not evidently incompatible with the printed P value after rounding. It is not a reproduced test.
- **Display-zero rule:** no `P = 0`, `p = 0.000`, or equivalent display zero occurs in the assigned inferential relationships. No display-zero candidate was emitted.

## Supplied inferential definitions and limitations

| ID | Supplied definition / missing definition | Pass-1 record |
|---|---|---|
| S086 | Protocol p. 12 and SAP p. 1 state linear regression, intention-to-treat, two-tailed `P < .05`, and propensity weighting “as appropriate”; the final article instead states a linear mixed model. No source states the final model's covariance structure, degrees of freedom, CI construction, variance estimator, or estimand mapping to every table cell. | `PASS_1_COMPLETE`; retained as definition record; no candidate proposal from an unreported detail. |
| S087 | Protocol pain power basis: assumed 10-mm difference, placebo reduction `-15.5 ± 25.5` mm at 12 weeks, 90% power, alpha .05, N=234 then N=260 after 10% loss. | `PASS_1_COMPLETE`; planned calculation only; exact power-test formula and sidedness-to-CI mapping are absent. |
| S088 | Protocol effusion power basis: 96% power for 20% difference, mean `2.24 cm²`, SD change `1.35`; no exact calculation formula or allocation rule supplied. | `PASS_1_COMPLETE`; planned calculation only; missing formula recorded. |
| S089 | Protocol WOMAC power basis: 20% relative difference, 90% power, alpha .05, total N=54 at 4 weeks; no exact calculation formula supplied. | `PASS_1_COMPLETE`; planned calculation only; missing formula recorded. |

## Main article Table 2 and reliability relationships

All Table 2 entries below use the direct main PDF p. 6. The table labels the arm values and between-group result as mean (95% CI), except the named median (IQR) rows and OMERACT-OARSI RR. Main Methods pp. 4 and 7 supply the mixed-model and two-sided-P context described above. `No proposal` below is a record of completed checks, not a validity or adjudication decision.

| ID | Relationship (estimate, interval, P) | Cross-location / label checks | Pass-1 result |
|---|---|---|---|
| S001 | Primary knee-pain VAS, 24 wk: difference `-0.3 (-6.9 to 6.4)`, `P=.94`; arm changes `-19.9 (-24.7 to -15.2)` and `-20.2 (-24.9 to -15.5)`. | Matches abstract p. 1 and Results p. 7; VAS 0-100, higher=worse. Contrast orientation is not explicitly defined by the heading. | `PASS_1_COMPLETE`; containment/order/sign and repeated values checked; CI/P diagnostic compatible; no proposal. |
| S002 | Effusion-synovitis volume: difference `-1.75 (-3.13 to -0.37)`, `P=.01`; arm changes `0.81 (-0.17 to 1.79)` and `-0.94 (-1.92 to 0.04)`. | Matches Results p. 7; median (IQR) endpoint label and mL scale supplied. Contrast orientation is not explicitly defined. | `PASS_1_COMPLETE`; checks completed; CI/P diagnostic compatible; no proposal. |
| S003 | WOMAC total pain: `3.0 (-24 to 31)`, `P=.81`. | Supplement eTable 4 p. 5 repeats 24-wk result; 0-500, higher=worse. | `PASS_1_COMPLETE`; checks completed; no proposal. |
| S004 | WOMAC weight-bearing pain: `3 (-10 to 16)`, `P=.70`. | eTable 4 p. 5 repeats 24-wk result; 0-300, higher=worse. | `PASS_1_COMPLETE`; checks completed; no proposal. |
| S005 | WOMAC non-weight-bearing pain: `2 (-10 to 14)`, `P=.70`. | eTable 4 p. 5 repeats 24-wk result; 0-200, higher=worse. | `PASS_1_COMPLETE`; checks completed; no proposal. |
| S006 | WOMAC function: `51 (-31 to 133)`, `P=.22`. | eTable 4 p. 5 repeats 24-wk result; 0-1700, higher=worse. | `PASS_1_COMPLETE`; checks completed; no proposal. |
| S007 | Hand-pain VAS: `1.3 (-4.8 to 7.3)`, `P=.69`. | eTable 4 p. 6 repeats 24-wk result; 0-100, higher=worse. | `PASS_1_COMPLETE`; checks completed; no proposal. |
| S008 | Back-pain VAS: `-1.3 (-7.9 to 5.2)`, `P=.69`. | eTable 4 p. 6 repeats 24-wk result; 0-100, higher=worse. | `PASS_1_COMPLETE`; checks completed; no proposal. |
| S009 | Lower-limb strength, N: `-2.2 (-7.9 to 3.4)`, `P=.44`. | eTable 4 p. 6 repeats 24-wk result; 0-250 N, higher=greater strength. | `PASS_1_COMPLETE`; checks completed; no proposal. |
| S010 | AQoL-6D: `-0.01 (-0.04 to 0.01)`, `P=.38`. | eTable 4 p. 6 repeats 24-wk result; scale -0.04 to 1.0, higher=better health. | `PASS_1_COMPLETE`; checks completed; no proposal. |
| S011 | OMERACT-OARSI responder RR: `1.14 (0.84 to 1.55)`, `P=.39`; `50/107 (47%)` versus `45/110 (41%)`. | eTable 4 pp. 6-7 repeats 24-wk result and identifies log-binomial RR. | `PASS_1_COMPLETE`; RR interval contains 1; label/scale and CI/P diagnostic checked; no proposal. |
| S012 | hsCRP: `0.64 (-0.56 to 1.84)`, `P=.30`. | eTable 4 p. 6 repeats 24-wk result; median (IQR), mg/dL. | `PASS_1_COMPLETE`; checks completed; no proposal. |
| S013 | Triglycerides: `0.15 (-0.04 to 0.33)`, `P=.11`. | eTable 4 p. 6 repeats 24-wk result; p. 7 narrative separately gives 12-wk `0.24 (0.07 to 0.42)`, P=.01. | `PASS_1_COMPLETE`; time points distinguished; checks completed; no proposal. |
| S014 | HDL cholesterol: `-0.03 (-0.09 to 0.03)`, `P=.32`. | eTable 4 p. 6 repeats 24-wk result. | `PASS_1_COMPLETE`; checks completed; no proposal. |
| S015 | LDL cholesterol: `0.01 (-0.14 to 0.17)`, `P=.90`. | eTable 4 p. 6 repeats 24-wk result. | `PASS_1_COMPLETE`; checks completed; no proposal. |
| S016 | Fasting glucose: `0.04 (-0.23 to 0.30)`, `P=.79`. | eTable 4 p. 6 repeats 24-wk result; distinct from 12-wk cell. | `PASS_1_COMPLETE`; checks completed; no proposal. |
| S017 | ICOAP constant pain: `2.95 (-2.29 to 8.18)`, `P=.27`. | Main PDF p. 6 only; ICOAP 0-100, higher=worse. | `PASS_1_COMPLETE`; checks completed; no proposal. |
| S018 | ICOAP intermittent pain: `1.5 (-3.8 to 6.9)`, `P=.62`. | Main PDF p. 6 only; ICOAP 0-100, higher=worse. | `PASS_1_COMPLETE`; checks completed; no proposal. |
| S019 | ICOAP total pain: `2.05 (-2.64 to 6.74)`, `P=.39`. | Main PDF p. 6 only; ICOAP 0-100, higher=worse. | `PASS_1_COMPLETE`; checks completed; no proposal. |
| S020 | Effusion-synovitis reliability ICC `0.96 (0.94 to 0.97)`, n=50. | Main PDF p. 4 identifies ICC scale 0-1 and higher as perfect agreement. | `PASS_1_COMPLETE`; point is contained and endpoints ordered; CI method is not supplied; no proposal. |

## Results supplement eTable 1

Source: results supplement PDF p. 2. Each record encompasses both printed arm change estimates and CIs, the absolute between-group difference and CI, and P. The table does not define the sign orientation of the term “absolute between group difference”; no orientation was inferred.

| ID | Analysis and printed result | Pass-1 result |
|---|---|---|
| S021 | Original data: krill `-19.93 (-24.67 to -15.20)`, placebo `-20.21 (-24.87 to -15.54)`, difference `-0.27 (-6.92 to 6.38)`, `P=.94`. | `PASS_1_COMPLETE`; all intervals ordered/contain points; matches main S001 to reported precision; CI/P diagnostic compatible; no proposal. |
| S022 | + age: krill `-19.95 (-24.68 to -15.21)`, placebo `-20.21 (-24.88 to -15.55)`, difference `-0.26 (-6.91 to 6.38)`, `P=.94`. | `PASS_1_COMPLETE`; all checks completed; CI/P diagnostic compatible; no proposal. |
| S023 | Multiple imputation: krill `-19.94 (-24.56 to -15.32)`, placebo `-20.29 (-24.9 to -15.68)`, difference `-0.35 (-6.79 to 6.09)`, `P=.92`. | `PASS_1_COMPLETE`; all checks completed; CI/P diagnostic compatible; no proposal. |

## Results supplement eTable 4 — complete endpoint/time inventory

Source: results supplement PDF pp. 5-7. Each row is one stable inferential relationship and explicitly encompasses **all printed arm-level final, baseline, and change estimates/intervals in that source row**, plus the printed between-group estimate/interval/P value listed below. The source calls most arm values mean (95% CI), except hsCRP (median [IQR]); it supplies endpoint scales and no-imputation/baseline-adjustment notes. The arm-to-arm direction of “between-group difference in change” is not explicitly stated. A `No proposal` entry means containment, endpoint order, sign/label, cross-location, and applicable CI/P diagnostic checks were performed; it is not an adjudication.

| ID | Endpoint, week: between-group result (95% CI), P | Pass-1 result |
|---|---|---|
| S024 | Knee-pain VAS, 4: `-0.4 (-4.9 to 4.1)`, `.85` | `PASS_1_COMPLETE`; no proposal. |
| S025 | Knee-pain VAS, 8: `-0.8 (-5.6 to 4.0)`, `.75` | `PASS_1_COMPLETE`; no proposal. |
| S026 | Knee-pain VAS, 12: `-0.1 (-5.2 to 5.1)`, `.98` | `PASS_1_COMPLETE`; no proposal. |
| S027 | Knee-pain VAS, 16: `0.3 (-5.3 to 5.9)`, `.91` | `PASS_1_COMPLETE`; no proposal. |
| S028 | Knee-pain VAS, 20: `-0.5 (-6.7 to 5.6)`, `.87` | `PASS_1_COMPLETE`; no proposal. |
| S029 | Knee-pain VAS, 24: `-0.3 (-6.9 to 6.4)`, `.94` | `PASS_1_COMPLETE`; matches S001; no proposal. |
| S030 | WOMAC total pain, 4: `-5 (-23 to 13)`, `.59` | `PASS_1_COMPLETE`; no proposal. |
| S031 | WOMAC total pain, 8: `-3 (-22 to 16)`, `.77` | `PASS_1_COMPLETE`; no proposal. |
| S032 | WOMAC total pain, 12: `-3 (-24 to 18)`, `.76` | `PASS_1_COMPLETE`; no proposal. |
| S033 | WOMAC total pain, 16: `-1 (-24 to 22)`, `.92` | `PASS_1_COMPLETE`; no proposal. |
| S034 | WOMAC total pain, 20: `5 (-21 to 30)`, `.72` | `PASS_1_COMPLETE`; no proposal. |
| S035 | WOMAC total pain, 24: `3 (-24 to 31)`, `.81` | `PASS_1_COMPLETE`; matches S003; no proposal. |
| S036 | WOMAC weight-bearing pain, 4: `3 (-10 to 16)`, `.66` | `PASS_1_COMPLETE`; one duplicated arm-change pair is separately recorded in proposal SP1-01; between-group interval/P itself checked. |
| S037 | WOMAC weight-bearing pain, 8: `1 (-12 to 14)`, `.88` | `PASS_1_COMPLETE`; no proposal. |
| S038 | WOMAC weight-bearing pain, 12: `0.0 (-13 to 13)`, `.99` | `PASS_1_COMPLETE`; finite-precision zero point estimate, not a P display zero; no proposal. |
| S039 | WOMAC weight-bearing pain, 16: `0.0 (-14 to 13)`, `.97` | `PASS_1_COMPLETE`; finite-precision zero point estimate, not a P display zero; no proposal. |
| S040 | WOMAC weight-bearing pain, 20: `4 (-10 to 17)`, `.60` | `PASS_1_COMPLETE`; no proposal. |
| S041 | WOMAC weight-bearing pain, 24: `3 (-10 to 16)`, `.70` | `PASS_1_COMPLETE`; matches S004; no proposal. |
| S042 | WOMAC non-weight-bearing pain, 4: `-5 (-13 to 3)`, `.25` | `PASS_1_COMPLETE`; no proposal. |
| S043 | WOMAC non-weight-bearing pain, 8: `-3 (-12 to 6)`, `.52` | `PASS_1_COMPLETE`; no proposal. |
| S044 | WOMAC non-weight-bearing pain, 12: `-2 (-11 to 7)`, `.64` | `PASS_1_COMPLETE`; no proposal. |
| S045 | WOMAC non-weight-bearing pain, 16: `0 (-10 to 10)`, `.94` | `PASS_1_COMPLETE`; no proposal. |
| S046 | WOMAC non-weight-bearing pain, 20: `1 (-10 to 12)`, `.82` | `PASS_1_COMPLETE`; no proposal. |
| S047 | WOMAC non-weight-bearing pain, 24: `2 (-10 to 14)`, `.70` | `PASS_1_COMPLETE`; matches S005; no proposal. |
| S048 | WOMAC function, 4: `-19 (-73 to 35)`, `.48` | `PASS_1_COMPLETE`; linked to duplicated arm-change comparison in SP1-01; no separate proposal. |
| S049 | WOMAC function, 8: `-4 (-62 to 53)`, `.88` | `PASS_1_COMPLETE`; no proposal. |
| S050 | WOMAC function, 12: `10 (-52 to 72)`, `.75` | `PASS_1_COMPLETE`; no proposal. |
| S051 | WOMAC function, 16: `22 (-47 to 90)`, `.53` | `PASS_1_COMPLETE`; no proposal. |
| S052 | WOMAC function, 20: `33 (-43 to 109)`, `.39` | `PASS_1_COMPLETE`; no proposal. |
| S053 | WOMAC function, 24: `51 (-31 to 133)`, `.22` | `PASS_1_COMPLETE`; matches S006; no proposal. |
| S054 | Hand-pain VAS, 4: `-1.6 (-6.1 to 2.9)`, `.49` | `PASS_1_COMPLETE`; no proposal. |
| S055 | Hand-pain VAS, 8: `3.8 (-0.9 to 8.6)`, `.12` | `PASS_1_COMPLETE`; no proposal. |
| S056 | Hand-pain VAS, 12: `-0.1 (-5.0 to 4.9)`, `.98` | `PASS_1_COMPLETE`; no proposal. |
| S057 | Hand-pain VAS, 16: `0.4 (-4.9 to 5.7)`, `.89` | `PASS_1_COMPLETE`; no proposal. |
| S058 | Hand-pain VAS, 20: `1.7 (-4.1 to 7.5)`, `.57` | `PASS_1_COMPLETE`; no proposal. |
| S059 | Hand-pain VAS, 24: `1.3 (-4.8 to 7.3)`, `.69` | `PASS_1_COMPLETE`; matches S007; no proposal. |
| S060 | Back-pain VAS, 4: `-1.4 (-5.9 to 3.0)`, `.53` | `PASS_1_COMPLETE`; linked to duplicate-result comparison in SP1-02; no separate proposal. |
| S061 | Back-pain VAS, 8: `3.9 (-0.9 to 8.6)`, `.11` | `PASS_1_COMPLETE`; no proposal. |
| S062 | Back-pain VAS, 12: `4.1 (-0.8 to 9.1)`, `.10` | `PASS_1_COMPLETE`; no proposal. |
| S063 | Back-pain VAS, 16: `4.3 (-0.9 to 9.6)`, `.11` | `PASS_1_COMPLETE`; no proposal. |
| S064 | Back-pain VAS, 20: `-0.3 (-6.0 to 5.3)`, `.91` | `PASS_1_COMPLETE`; no proposal. |
| S065 | Back-pain VAS, 24: `-1.3 (-7.9 to 5.2)`, `.69` | `PASS_1_COMPLETE`; matches S008; no proposal. |
| S066 | Lower-leg strength, 12: `-1.4 (-5.9 to 3.0)`, `.53` | `PASS_1_COMPLETE`; exact duplicate comparison with S060 in SP1-02. |
| S067 | Lower-leg strength, 24: `-2.2 (-7.9 to 3.4)`, `.44` | `PASS_1_COMPLETE`; matches S009; no proposal. |
| S068 | AQoL-6D, 12: `-0.0003 (-0.02 to 0.02)`, `.98` | `PASS_1_COMPLETE`; no proposal. |
| S069 | AQoL-6D, 24: `-0.01 (-0.04 to 0.01)`, `.38` | `PASS_1_COMPLETE`; matches S010; no proposal. |
| S070 | OMERACT-OARSI RR, 4: `0.85 (0.50 to 1.46)`, `.57` | `PASS_1_COMPLETE`; RR/log-binomial label supplied; no proposal. |
| S071 | OMERACT-OARSI RR, 8: `0.87 (0.57 to 1.32)`, `.51` | `PASS_1_COMPLETE`; no proposal. |
| S072 | OMERACT-OARSI RR, 12: `0.98 (0.69 to 1.39)`, `.90` | `PASS_1_COMPLETE`; no proposal. |
| S073 | OMERACT-OARSI RR, 16: `0.94 (0.66 to 1.33)`, `.72` | `PASS_1_COMPLETE`; no proposal. |
| S074 | OMERACT-OARSI RR, 20: `1.06 (0.77 to 1.48)`, `.71` | `PASS_1_COMPLETE`; no proposal. |
| S075 | OMERACT-OARSI RR, 24: `1.14 (0.84 to 1.55)`, `.39` | `PASS_1_COMPLETE`; matches S011; no proposal. |
| S076 | hsCRP, 12: `0.07 (-1.19 to 1.33)`, `.92` | `PASS_1_COMPLETE`; exact duplicate comparison with S084 in SP1-03. |
| S077 | hsCRP, 24: `0.64 (-0.56 to 1.84)`, `.30` | `PASS_1_COMPLETE`; matches S012; no proposal. |
| S078 | Triglycerides, 12: `0.24 (0.07 to 0.42)`, `.01` | `PASS_1_COMPLETE`; matches main p. 7 narrative; no proposal. |
| S079 | Triglycerides, 24: `0.15 (-0.04 to 0.33)`, `.11` | `PASS_1_COMPLETE`; matches S013; no proposal. |
| S080 | HDL, 12: `-0.01 (-0.07 to 0.05)`, `.76` | `PASS_1_COMPLETE`; no proposal. |
| S081 | HDL, 24: `-0.03 (-0.09 to 0.03)`, `.32` | `PASS_1_COMPLETE`; matches S014; no proposal. |
| S082 | LDL, 12: `-0.14 (-0.29 to 0.005)`, `.06` | `PASS_1_COMPLETE`; no proposal. |
| S083 | LDL, 24: `0.01 (-0.14 to 0.17)`, `.90` | `PASS_1_COMPLETE`; matches S015; no proposal. |
| S084 | Fasting glucose, 12: `0.07 (-1.19 to 1.33)`, `.92` | `PASS_1_COMPLETE`; exact duplicate comparison with S076 in SP1-03. |
| S085 | Fasting glucose, 24: `0.04 (-0.23 to 0.30)`, `.79` | `PASS_1_COMPLETE`; matches S016; no proposal. |

## Protocol historical inferential statements

| ID | Relationship | Pass-1 result |
|---|---|---|
| S090 | Protocol p. 5 attributes pilot WOMAC change `-38.35 ± 21.06` versus `-0.6 ± 15.89`, `p=.01`, to an external 90-participant 30-day study. | `PASS_1_COMPLETE`; only a historical external-study statement; test/model/CI definition absent, so no compatibility reconstruction; no proposal. |
| S091 | Protocol p. 5 attributes pilot CRP change `-30.9% ± 1.0` versus `+25.1% ± 1.05`, `p=.008`, to the same external study. | `PASS_1_COMPLETE`; only a historical external-study statement; test/model/CI definition absent; no proposal. |

## Pass-1 coverage summary

- **Stable S IDs:** S001-S091 (91 total), every record marked `PASS_1_COMPLETE`.
- **Direct result-estimate relationships:** 85 (19 main Table 2, 1 ICC, 3 eTable 1, 62 eTable 4).
- **Definitions/planned or historical inferential statements:** 6 (S086-S091).
- **Candidate proposals:** 3 distinct unadjudicated proposals, documented in `checkers/statistical_pass_1.md`; no C IDs assigned.
- **Explicit limitations:** contrast orientation is not defined for the displayed between-group differences; final-model covariance, degrees of freedom, variance estimator, exact CI/P calculation, and estimand mapping are not supplied; source-based normal-approximation observations are diagnostics only.

## Pass-2 completion update — all stable S records

Pass 2 independently revisited every record against the complete candidate ledger (`C001` through `C016`), mechanical recheck, numeric and cross-source checker facts, and the canonical source mappings. The original `PASS_1_COMPLETE` result is preserved for every relationship. Each row below is the explicit pass-2 update for its corresponding stable S record; it does not adjudicate any candidate.

| ID | Pass-2 reconciliation | Pass-2 record |
|---|---|---|
| S001 | Primary 24-week VAS; C012 confirms the independently printed Key Points sign conflict. Containment/order, scale, repeat locations, and diagnostic CI/P compatibility otherwise remain as mapped. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; associated existing C012; no new proposal. |
| S002 | Effusion volume; interval/order, mL label, repeated Results value, and diagnostic CI/P relation rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S003 | WOMAC total pain, 24 weeks; Table 2/eTable 4 match retained. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S004 | WOMAC weight-bearing pain, 24 weeks; Table 2/eTable 4 match retained. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S005 | WOMAC non-weight-bearing pain, 24 weeks; Table 2/eTable 4 match retained. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S006 | WOMAC function, 24 weeks; Table 2/eTable 4 match retained. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S007 | Hand-pain VAS, 24 weeks; Table 2/eTable 4 match retained. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S008 | Back-pain VAS, 24 weeks; Table 2/eTable 4 match retained. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S009 | Strength, 24 weeks; Table 2/eTable 4 match retained. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S010 | AQoL-6D, 24 weeks; Table 2/eTable 4 match retained. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S011 | OMERACT-OARSI RR, 24 weeks; RR label/reference and interval around 1 rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S012 | hsCRP, 24 weeks; metric, interval/order, and repeated value rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S013 | Triglycerides, 24 weeks; distinguished from 12-week result. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S014 | HDL, 24 weeks; Table 2/eTable 4 match retained. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S015 | LDL, 24 weeks; Table 2/eTable 4 match retained. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S016 | Fasting glucose, 24 weeks; distinguished from 12-week result. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S017 | ICOAP constant pain; containment/order/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S018 | ICOAP intermittent pain; containment/order/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S019 | ICOAP total pain; containment/order/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S020 | ICC reliability estimate; scale 0-1 and interval containment/order rechecked; CI method remains absent. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S021 | eTable 1 original-data primary result; C012 comparator and rounded negative sign retained. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; associated existing C012; no new proposal. |
| S022 | eTable 1 age sensitivity; containment/order and diagnostic CI/P relation rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S023 | eTable 1 multiple-imputation sensitivity; containment/order and diagnostic CI/P relation rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S024 | Knee-pain VAS, 4 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S025 | Knee-pain VAS, 8 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S026 | Knee-pain VAS, 12 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S027 | Knee-pain VAS, 16 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S028 | Knee-pain VAS, 20 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S029 | Knee-pain VAS, 24 weeks; maps to S001/S021 and carries C012's cross-location sign comparator. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; associated existing C012; no new proposal. |
| S030 | WOMAC total pain, 4 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S031 | WOMAC total pain, 8 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S032 | WOMAC total pain, 12 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S033 | WOMAC total pain, 16 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S034 | WOMAC total pain, 20 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S035 | WOMAC total pain, 24 weeks; maps to S003. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S036 | Week-4 weight-bearing-pain row; C009's mechanically confirmed repeated arm-change pair is retained. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; associated existing C009; no new proposal. |
| S037 | WOMAC weight-bearing pain, 8 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S038 | WOMAC weight-bearing pain, 12 weeks; finite-precision estimate 0.0 is not a P-value display zero. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S039 | WOMAC weight-bearing pain, 16 weeks; finite-precision estimate 0.0 is not a P-value display zero. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S040 | WOMAC weight-bearing pain, 20 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S041 | WOMAC weight-bearing pain, 24 weeks; maps to S004. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S042 | WOMAC non-weight-bearing pain, 4 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S043 | WOMAC non-weight-bearing pain, 8 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S044 | WOMAC non-weight-bearing pain, 12 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S045 | WOMAC non-weight-bearing pain, 16 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S046 | WOMAC non-weight-bearing pain, 20 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S047 | WOMAC non-weight-bearing pain, 24 weeks; maps to S005. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S048 | Week-4 WOMAC function row; C009's mechanically confirmed repeated pair is retained. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; associated existing C009; no new proposal. |
| S049 | WOMAC function, 8 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S050 | WOMAC function, 12 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S051 | WOMAC function, 16 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S052 | WOMAC function, 20 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S053 | WOMAC function, 24 weeks; maps to S006. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S054 | Hand-pain VAS, 4 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S055 | Hand-pain VAS, 8 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S056 | Hand-pain VAS, 12 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S057 | Hand-pain VAS, 16 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S058 | Hand-pain VAS, 20 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S059 | Hand-pain VAS, 24 weeks; maps to S007. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S060 | Week-4 back-pain VAS; C010's mechanically confirmed complete duplicate is retained. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; associated existing C010; no new proposal. |
| S061 | Back-pain VAS, 8 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S062 | Back-pain VAS, 12 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S063 | Back-pain VAS, 16 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S064 | Back-pain VAS, 20 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S065 | Back-pain VAS, 24 weeks; maps to S008. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S066 | Week-12 lower-leg strength; C010's mechanically confirmed complete duplicate is retained. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; associated existing C010; no new proposal. |
| S067 | Lower-leg strength, 24 weeks; maps to S009. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S068 | AQoL-6D, 12 weeks; containment/order/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S069 | AQoL-6D, 24 weeks; maps to S010. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S070 | OMERACT-OARSI RR, 4 weeks; RR label/reference and interval around 1 rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S071 | OMERACT-OARSI RR, 8 weeks; RR label/reference and interval around 1 rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S072 | OMERACT-OARSI RR, 12 weeks; RR label/reference and interval around 1 rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S073 | OMERACT-OARSI RR, 16 weeks; RR label/reference and interval around 1 rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S074 | OMERACT-OARSI RR, 20 weeks; RR label/reference and interval around 1 rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S075 | OMERACT-OARSI RR, 24 weeks; maps to S011; RR label/reference and interval around 1 rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S076 | Week-12 hsCRP; C011's mechanically confirmed duplicate contrast/CI/P is retained. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; associated existing C011; no new proposal. |
| S077 | hsCRP, 24 weeks; maps to S012. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S078 | Triglycerides, 12 weeks; cross-source narrative match retained. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S079 | Triglycerides, 24 weeks; maps to S013. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S080 | HDL, 12 weeks; containment/order/sign/scale rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S081 | HDL, 24 weeks; maps to S014. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S082 | LDL, 12 weeks; endpoint order/containment and diagnostic CI/P relation rechecked. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S083 | LDL, 24 weeks; maps to S015. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S084 | Week-12 fasting glucose; C011's mechanically confirmed duplicate contrast/CI/P is retained. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; associated existing C011; no new proposal. |
| S085 | Fasting glucose, 24 weeks; maps to S016. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S086 | Protocol/SAP-versus-final-model definition; missing final covariance, df, variance, CI/P rule, and cell estimand remain explicitly unresolved. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S087 | Protocol pain power basis; exact power-test formula and sidedness/CI mapping remain absent. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S088 | Protocol effusion power basis; exact formula/allocation rule remains absent. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S089 | Protocol WOMAC power basis; exact formula remains absent. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S090 | Historical external pilot WOMAC statement; compatible test/model/CI definition remains absent. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |
| S091 | Historical external pilot CRP statement; compatible test/model/CI definition remains absent. | `PASS_1_COMPLETE`; `PASS_2_COMPLETE`; no new proposal. |

### Pass-2 inventory summary

- **Stable S IDs revisited:** 91 (`S001` through `S091`, each individually recorded above).
- **Existing-ledger implications:** C009 (S036/S048), C010 (S060/S066), C011 (S076/S084), and C012 (S001/S021/S029) are retained as source-grounded existing candidates. C001-C008 and C013-C016 contribute population, denominator, count, or cross-reference context but do not establish a new statistical inconsistency for an S record.
- **New pass-2 proposals:** 0. No candidate ID is created or renumbered here.
- **Display-zero review:** no P-value display zero occurred. The `0`, `0.0`, and `-0.0003` entries are finite-precision point estimates, not candidate-generating P-value notation.
