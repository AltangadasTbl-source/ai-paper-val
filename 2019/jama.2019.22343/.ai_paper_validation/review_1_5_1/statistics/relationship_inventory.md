# Canonical Inferential-Statistical Relationship Inventory

Two-pass completion: every canonical relationship S001-S071 has a `PASS_1_COMPLETE` record in statistical pass 1 and a `PASS_2_COMPLETE` record in statistical pass 2.

## Pass-1 scope and canonicalization

This is a fresh canonical inventory constructed from the current-run main/support evidence maps and their source-linked relationship parts. It does not use legacy candidate, checker, reviewer, or report material. A distinct relationship is keyed by the reported comparison, outcome, population/subgroup, time point, effect measure/scale, and analysis grouping. Repeated source locations are retained as provenance rather than assigned a second S ID. A multi-endpoint mapper record was split when it contains distinct reported effects.

- **Direct sources:** `jama_wilson_2020_oi_190154.pdf` (DOC-001), `joi190154supp1_prod.pdf` (DOC-002), and `joi190154supp2_prod.pdf` (DOC-003).
- **Canonical relationship count:** 71.
- **P-value display-zero count:** 0. No printed `P = 0`, `p = 0.000`, or equivalent was found in this inventory. The serious-adverse-event *incidence* printed as `0 per patient` is not a P value and is not a display-zero candidate.
- **Pass-1 completion rule:** every row below was reviewed for the source-supplied applicable checks and is explicitly marked `PASS_1_COMPLETE`. `DIRECT_MATCH` does not represent adjudication; it records only that no pass-1 observation was emitted for that relationship.

| S ID | Provisional-ID provenance | Exact direct-source location(s) | Canonical inferential relationship | Pass-1 completion/result |
|---|---|---|---|---|
| S001 | MS001 | DOC-001 pp. 1, 4, 5 | BPAP vs no device; mortality; OR 0.66; abstract/narrative CI 0.51-0.87, Figure 1 CI 0.50-0.87; P=.003; 13 studies/1423 | PASS_1_COMPLETE — CROSS_LOCATION_OBSERVATION CS-001 |
| S002 | MS002 | DOC-001 pp. 1, 4, 6 | HMV vs no device; mortality; OR 0.56 (0.29-1.08), P=.49; 2 studies/175 | PASS_1_COMPLETE — DIAGNOSTIC_OBSERVATION P1-OBS-002 |
| S003 | MS003 | DOC-001 pp. 1, 5 | BPAP vs no device; intubation; OR 0.34 (0.14-0.83), P=.02 | PASS_1_COMPLETE — DIRECT_MATCH |
| S004 | MS004 | DOC-001 pp. 1, 4, 5 | BPAP vs no device; all-cause admission count; RR 0.91 (0.71-1.17), P=.47 | PASS_1_COMPLETE — DIRECT_MATCH |
| S005 | MS005 | DOC-001 pp. 1, 5 | BPAP vs no device; quality of life; SMD 0.16, Figure 4 CI -0.06 to 0.38; abstract/narrative CI -0.06 to 0.39, P=.15 | PASS_1_COMPLETE — OBSERVATION P1-OBS-001 |
| S006 | MS006 | DOC-001 pp. 1, 5, 6 | BPAP vs no device; patients with all-cause admission; OR 0.22 (0.11-0.43), P<.001 | PASS_1_COMPLETE — DIRECT_MATCH |
| S007 | MS007 | DOC-001 pp. 1, 4, 6 | HMV vs no device; all-cause admission count; RR 0.50 (0.35-0.71), P<.001 | PASS_1_COMPLETE — DIRECT_MATCH |
| S008 | MS008 | DOC-001 pp. 1, 8 | NIPPV vs no device; adverse-event count; RR 1.08 (0.52-2.21), P=.84 | PASS_1_COMPLETE — DIRECT_MATCH |
| S009 | MS009 | DOC-001 p. 6 | BPAP vs no device; respiratory-admission patients; RD -1% (-14% to 13%), OR 0.98 (0.56-1.71), P=.94 | PASS_1_COMPLETE — DIRECT_MATCH |
| S010 | MS010 | DOC-001 p. 6 | BPAP vs no device; emergency-department visit count; RR 0.72 (0.60-0.85), P<.001 | PASS_1_COMPLETE — DIRECT_MATCH |
| S011 | MS011 | DOC-001 p. 6 | BPAP vs no device; ICU-admission count; RR 0.43 (0.18-1.05), P=.06 | PASS_1_COMPLETE — DIRECT_MATCH |
| S012 | MS012 | DOC-001 p. 6 | BPAP vs no device; ICU-admission patients; RD -24% (-36% to -13%), OR 0.18 (0.07-0.46), P=.001 | PASS_1_COMPLETE — DIRECT_MATCH |
| S013 | MS013 | DOC-001 p. 6 | BPAP vs no device; COPD-exacerbation count; RR 0.85 (0.67-1.07), P=.17 | PASS_1_COMPLETE — DIRECT_MATCH |
| S014 | MS014 | DOC-001 p. 6 | BPAP vs no device; COPD-exacerbation patients; RD -4% (-30% to 22%), OR 0.84 (0.26-2.68), P=.17 | PASS_1_COMPLETE — DIRECT_MATCH |
| S015 | MS015 | DOC-001 p. 6 | BPAP vs no device; activities of daily living; SMD 0.09 (-0.13 to 0.31), P=.41 | PASS_1_COMPLETE — DIRECT_MATCH |
| S016 | MS016 | DOC-001 p. 6 | BPAP vs no device; dyspnea; SMD 0.24 (0.03-0.45), P=.02 | PASS_1_COMPLETE — DIRECT_MATCH |
| S017 | MS017 | DOC-001 p. 6 | BPAP vs no device; sleep quality; SMD 0.12 (-0.06 to 0.30), P=.19 | PASS_1_COMPLETE — DIRECT_MATCH |
| S018 | MS018 | DOC-001 p. 6 | BPAP vs no device; 6-minute walk distance; mean difference 23.83 m (-12.44 to 60.10), P=.20 | PASS_1_COMPLETE — DIRECT_MATCH |
| S019 | MS019 | DOC-001 p. 6 | BPAP vs no device; shuttle walk distance; mean difference 72 m (12.9-131), P=.01 | PASS_1_COMPLETE — DIRECT_MATCH |
| S020 | MS020; SS009 | DOC-001 p. 6; DOC-003 pp. 19, 43 | BPAP vs CPAP; COPD-exacerbation patients; RD -0.23 (-0.50 to 0.03), OR 0.38 (0.12-1.22), P=.10; effectiveness total 49 | PASS_1_COMPLETE — OBSERVATION P1-OBS-004 |
| S021 | MS021; SS012 | DOC-001 pp. 6-7; DOC-003 p. 43 | BPAP <=6 months vs >6 months; 6-minute walk, 43% increase vs 11% decrease, P=.04; 1 RCT/26 | PASS_1_COMPLETE — DIRECT_MATCH |
| S022 | MS022; SS013 | DOC-001 p. 7; DOC-003 p. 44 | BPAP-S adherent vs nonadherent; all-cause admissions, 0.4 vs 1.0 per patient, P=.006/<.01 | PASS_1_COMPLETE — DIRECT_MATCH |
| S023 | MS023; SS013 | DOC-001 p. 7; DOC-003 p. 44 | BPAP-S adherent vs nonadherent; ICU admissions, 0.6 vs 1.2 per patient, P=.37 | PASS_1_COMPLETE — DIRECT_MATCH |
| S024 | MS024; SS013 | DOC-001 p. 7; DOC-003 p. 43 | High- vs low-intensity HMV/BPAP mix; CAT QOL WMD 2.30; main CI -2.23 to 6.83, supplement CI -2.35 to 6.95 | PASS_1_COMPLETE — OBSERVATION P1-OBS-005 |
| S025 | MS025; SS010 | DOC-001 p. 7; DOC-003 p. 43 | Volume-assured BPAP vs BPAP-ST; mortality; RD -0.05 (-0.21 to 0.11), OR 0.47 (0.04-5.69), P=.56 | PASS_1_COMPLETE — DIRECT_MATCH |
| S026 | MS026; SS010 | DOC-001 p. 7; DOC-003 p. 43 | Volume-assured BPAP vs BPAP-ST; SGRQ QOL; WMD -4.70 (-15.97 to 6.57), P=.41 | PASS_1_COMPLETE — DIRECT_MATCH |
| S027 | MS027; SS010 | DOC-001 p. 7; DOC-003 p. 43 | Volume-assured BPAP vs BPAP-ST; shuttle walk; WMD -4.00 m (-54.24 to 46.24), P=.88 | PASS_1_COMPLETE — DIRECT_MATCH |
| S028 | MS028; SS010 | DOC-001 p. 7; DOC-003 p. 43 | Volume-assured BPAP vs BPAP-ST; Epworth sleep quality; WMD -2.70 (-6.07 to 0.67), P=.12 | PASS_1_COMPLETE — DIRECT_MATCH |
| S029 | MS029; SS014 | DOC-001 p. 7; DOC-003 p. 44 | Home telemedicine vs hospital BPAP-ST initiation; mortality; RD 0.03 (-0.07 to 0.13), OR 2.13 (0.18-24.67), P=.55 | PASS_1_COMPLETE — DIRECT_MATCH |
| S030 | MS030; SS014 | DOC-001 p. 7; DOC-003 p. 44 | Home telemedicine vs hospital BPAP-ST initiation; SRIQ QOL; WMD -1.20 (-9.92 to 7.52), P=.79 | PASS_1_COMPLETE — DIRECT_MATCH |
| S031 | MS031; SS014 | DOC-001 p. 7; DOC-003 p. 44 | Home telemedicine vs hospital BPAP-ST initiation; MRC dyspnea; WMD 0.10 (-0.50 to 0.70), P=.74 | PASS_1_COMPLETE — DIRECT_MATCH |
| S032 | MS032; SS014 | DOC-001 p. 7; DOC-003 p. 44 | Home telemedicine vs hospital BPAP-ST initiation; 6-minute walk; WMD -19.00 m (-64.60 to 29.60), P=.41 | PASS_1_COMPLETE — DIRECT_MATCH |
| S033 | MS033; SS014 | DOC-001 p. 7; DOC-003 p. 44 | Home telemedicine vs hospital BPAP-ST initiation; all-cause admissions; WMD -0.10 (-0.60 to 0.40), P=.40 | PASS_1_COMPLETE — DIRECT_MATCH |
| S034 | MS034; SS011 | DOC-001 p. 7; DOC-003 p. 43 | Pressure-controlled vs pressure-support HMV; SRIQ QOL; WMD -0.14 (-4.90 to 4.60), P=.95 | PASS_1_COMPLETE — DIRECT_MATCH |
| S035 | MS035; SS011 | DOC-001 p. 7; DOC-003 p. 43 | Pressure-controlled vs pressure-support HMV; 6-minute walk; WMD 14 m (-42 to 70), P=.58 | PASS_1_COMPLETE — DIRECT_MATCH |
| S036 | MS036 | DOC-001 p. 7 | Stable COPD vs no device; mortality; OR 0.62 (0.42-0.92), P=.02 | PASS_1_COMPLETE — DIRECT_MATCH |
| S037 | MS036 | DOC-001 p. 7 | Stable COPD vs no device; all-cause admission count; RR 0.84 (0.59-1.18), P=.31 | PASS_1_COMPLETE — DIRECT_MATCH |
| S038 | MS036 | DOC-001 p. 7 | Stable COPD vs no device; intubation; OR 0.43 (0.08-2.46), P=.34 | PASS_1_COMPLETE — DIRECT_MATCH |
| S039 | MS036 | DOC-001 p. 7 | Stable COPD vs no device; quality of life; SMD 0.24 (-0.06 to 0.54), no P printed | PASS_1_COMPLETE — DIRECT_MATCH |
| S040 | MS037 | DOC-001 p. 7 | Recent exacerbation vs no device; mortality; OR 0.66 (0.41-1.06), P=.09 | PASS_1_COMPLETE — DIRECT_MATCH |
| S041 | MS037 | DOC-001 p. 7 | Recent exacerbation vs no device; quality of life; SMD -0.03 (-0.25 to 0.20), P=.82 | PASS_1_COMPLETE — DIRECT_MATCH |
| S042 | MS037 | DOC-001 p. 7 | Recent exacerbation vs no device; all-cause admission count; RR 0.59 (0.43-0.81), P=.001 | PASS_1_COMPLETE — DIRECT_MATCH |
| S043 | MS037 | DOC-001 p. 7 | Recent exacerbation vs no device; intubation; OR 0.31 (0.11-0.89), P=.03 | PASS_1_COMPLETE — DIRECT_MATCH |
| S044 | MS038 | DOC-001 p. 7 | PaCO2 >=52 mm Hg subgroup; QOL SMD 0.18 (-0.05 to 0.40), 2 studies/311 | PASS_1_COMPLETE — DIRECT_MATCH |
| S045 | MS038 | DOC-001 p. 7 | PaCO2 50-51 mm Hg subgroup; QOL SMD 0.97 (0.36-1.58), 1 study/49 | PASS_1_COMPLETE — DIRECT_MATCH |
| S046 | MS038 | DOC-001 p. 7 | PaCO2 45-49 mm Hg subgroup; QOL SMD -0.06 (-0.28 to 0.17), 2 studies/102 | PASS_1_COMPLETE — DIRECT_MATCH |
| S047 | MS039 | DOC-001 pp. 7-8 | RCT-only NIPPV vs no device; mortality; OR 0.72 (0.49-1.05) | PASS_1_COMPLETE — DIRECT_MATCH |
| S048 | MS039 | DOC-001 pp. 7-8 | Observational-only NIPPV vs no device; mortality; OR 0.58 (0.35-0.96) | PASS_1_COMPLETE — DIRECT_MATCH |
| S049 | MS040 | DOC-001 pp. 7-8 | RCT-only NIPPV vs no device; intubation; OR 0.48 (0.04-5.64) | PASS_1_COMPLETE — DIRECT_MATCH |
| S050 | MS040 | DOC-001 pp. 7-8 | Observational-only NIPPV vs no device; intubation; OR 0.32 (0.12-0.83) | PASS_1_COMPLETE — DIRECT_MATCH |
| S051 | MS041 | DOC-001 pp. 7-8 | RCT-only NIPPV vs no device; all-cause admission count; RR 0.92 (0.67-1.26) | PASS_1_COMPLETE — DIRECT_MATCH |
| S052 | MS041 | DOC-001 pp. 7-8 | Observational-only NIPPV vs no device; all-cause admission count; RR 0.65 (0.40-1.06) | PASS_1_COMPLETE — DIRECT_MATCH |
| S053 | MS042 | DOC-001 p. 8 | RCT-only NIPPV vs no device; quality of life; SMD 0.10 (-0.09 to 0.29) | PASS_1_COMPLETE — OBSERVATION P1-OBS-003 |
| S054 | MS042 | DOC-001 p. 8 | Observational-only NIPPV vs no device; quality of life; SMD 0.97 (0.36-1.58) | PASS_1_COMPLETE — OBSERVATION P1-OBS-003 |
| S055 | MS043 | DOC-001 p. 8 | NIPPV adverse-event pooled total incidence; 0.21 per patient (0.12-0.37) | PASS_1_COMPLETE — DIRECT_MATCH |
| S056 | MS043 | DOC-001 p. 8 | NIPPV serious-adverse-event pooled incidence; 0 per patient (0.00-0.01) | PASS_1_COMPLETE — DIRECT_MATCH; non-P display zero, not a candidate |
| S057 | MS043 | DOC-001 p. 8 | NIPPV nonserious-adverse-event pooled incidence; 0.24 per patient (0.12-0.47) | PASS_1_COMPLETE — DIRECT_MATCH |
| S058 | SS001 | DOC-002 p. 11 | Protocol meta-analysis eligibility and model rule: >2 same-PICOTS studies with point estimates/dispersion; DL random effects if k>18, otherwise DL plus Knapp-Hartung variance adjustment | PASS_1_COMPLETE — DEFINITION_RECORDED |
| S059 | SS002 | DOC-002 p. 11 | Protocol heterogeneity, subgroup, sensitivity, and funnel/Egger rules | PASS_1_COMPLETE — DEFINITION_RECORDED |
| S060 | SS003 | DOC-003 p. 17 | Strength-of-evidence definitions and eight modifying domains | PASS_1_COMPLETE — DEFINITION_RECORDED |
| S061 | SS004 | DOC-003 p. 34 | Murphy eligibility/titration/usage parameter relationship | PASS_1_COMPLETE — DIRECT_MATCH |
| S062 | SS005 | DOC-003 pp. 34-35 | Oscroft IVAPS vs BPAP-ST threshold/titration/usage parameter relationship | PASS_1_COMPLETE — DIRECT_MATCH |
| S063 | SS006 | DOC-003 pp. 34-40 | Physiologic eligibility and titration target rules | PASS_1_COMPLETE — DIRECT_MATCH |
| S064 | SS007 | DOC-003 pp. 37-40 | Measured adherence/use definition and reported use relationship | PASS_1_COMPLETE — DIRECT_MATCH |
| S065 | SS008 | DOC-003 p. 43 | HMV vs CPAP; all-cause hospital admissions; fewer with HMV, P<.001, 39,700 patients | PASS_1_COMPLETE — DIRECT_MATCH |
| S066 | SS008 | DOC-003 p. 43 | HMV vs CPAP; respiratory-cause hospital admissions; fewer with HMV, P=.01, 39,700 patients | PASS_1_COMPLETE — DIRECT_MATCH |
| S067 | SS008 | DOC-003 p. 43 | HMV vs BPAP; all-cause hospital admissions; fewer with HMV, P<.001, 9,471 patients | PASS_1_COMPLETE — DIRECT_MATCH |
| S068 | SS010 | DOC-003 p. 43 | Volume-assured BPAP vs BPAP-ST; MRC dyspnea; WMD -0.70 (-1.60 to 0.20) | PASS_1_COMPLETE — DIRECT_MATCH |
| S069 | SS012 | DOC-003 p. 43 | BPAP <=6 months vs >6 months; SGRQ QOL, 57 vs 53, P=.80 | PASS_1_COMPLETE — DIRECT_MATCH |
| S070 | SS012 | DOC-003 p. 43 | BPAP <=6 months vs >6 months; ICU-admission patients; RD 0.08 (-0.23 to 0.38), OR 1.65 (0.23-11.99) | PASS_1_COMPLETE — DIRECT_MATCH |
| S071 | SS014 | DOC-003 p. 44 | Home telemedicine vs hospital BPAP-ST initiation; exacerbations; no significant difference | PASS_1_COMPLETE — DIRECT_MATCH |

## Source-supplied definitions and explicit gaps

DOC-001 p. 3 supplies the outcome estimand labels (OR/RD for binary outcomes; SMD for differing continuous instruments; RR for event-count incidence rates), a standardized SMD direction (higher is better), 95% CIs, random-effects DerSimonian-Laird and fixed-effect Mantel-Haenszel selection, two-tailed P<.05 significance, and exploratory status/no multiplicity adjustment. DOC-002 p. 11 gives a planned but nonidentical model rule. These rules were retained as evidence, not silently reconciled.

The package does **not** supply the exact effect-test statistic, degrees of freedom, confidence-interval construction, continuity correction, final study weights, variance estimator, covariance for change scores, or the calculation mapping a rounded displayed CI to each displayed P value. Therefore, pass 1 uses a threshold-direction screen (95% interval excluding/crossing the relevant null versus P<.05/P>=.05 where printed) and labels the one numerical interval-to-P calculation as a diagnostic, not an exact compatibility rule.

## Pass-1 observation index

| Local checker ID | S ID(s) | Observation type | Status |
|---|---|---|---|
| P1-OBS-001 | S005 | Cross-location interval endpoint difference | Recorded in `checkers/statistical_pass_1.md` |
| P1-OBS-002 | S002 | Diagnostic interval-to-P discrepancy with missing exact effect-test definition | Recorded in `checkers/statistical_pass_1.md`; no candidate emitted in pass 1 |
| P1-OBS-003 | S053, S054 | Cross-location standardized-QOL direction-label contradiction | Recorded in `checkers/statistical_pass_1.md` |
| P1-OBS-004 | S020 | Cross-table participant-total difference | Recorded in `checkers/statistical_pass_1.md` |
| P1-OBS-005 | S024 | Cross-document CI endpoint difference | Recorded in `checkers/statistical_pass_1.md` |

Every S record above is `PASS_1_COMPLETE`; pass 2 must revisit all 71 S IDs against the complete candidate ledger and mechanical-recheck facts.
