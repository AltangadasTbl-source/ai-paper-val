# Statistical Relationship Inventory — Passes 1 and 2

## Scope and methods

This fresh, source-first inventory covers every inferential relationship mapped in DOC-001 (main article), DOC-002 (protocol), and DOC-003 (online supplement). Exact supplied PDF pages and the current fresh native/layout text and rendered-page assets were checked. PASS 1 checked point-estimate containment, endpoint order, count-to-estimate direction, effect-measure and reference-group labels, matched repeated occurrences, and P/interval compatibility only where the supplied documents define a compatible method. No web material or prior audit derivative was used.

`PASS_1_COMPLETE` means the listed relationship was checked; it is not an adjudication. `DIAGNOSTIC_ONLY` marks a check that cannot establish an exact numerical discrepancy because the supplied source does not provide all model, CI, or variance inputs. No coherent finite-precision display-zero P value occurs in the supplied result displays.

| ID | Exact supplied location(s) | Inferential relationship / match fields | PASS 1 result |
|---|---|---|---|
| S001 | DOC-001 PDF p. 4, Sample Size Calculation | n=300 (150/group), 80% power, 50% relative reduction from 25%, two-sided alpha .05. | PASS_1_COMPLETE — planned-design assertion; simulation/formula inputs absent, so exact power is DIAGNOSTIC_ONLY. Protocol comparison is S027. |
| S002 | DOC-001 PDF p. 4, Statistical Analysis | Dichotomous chi-square with continuity correction; equal-variance t test for means; two-sided significance rule; no multiplicity adjustment. | PASS_1_COMPLETE — method definition used only for compatible rows; the extracted `P.05` typography does not define a new result contradiction. |
| S003 | DOC-001 PDF p. 4, Statistical Analysis | ITT; bootstrap 95% CIs for risk differences/unadjusted RRs; KM/Cox for any and spontaneous delivery; Wald interactions. | PASS_1_COMPLETE — labels agree with Table 2, Figure 2, and eTable 3 except the separate repeated-HR issue in S022/S024. |
| S004 | DOC-001 PDF pp. 1, 4, 5 | SPTB <34: 11/150 vs 23/150; RD -8.0% (-15.7 to -0.4); RR 0.48 (0.24-0.95); P=.04. | PASS_1_COMPLETE — count direction, estimate containment, RR and RD CI order, repeated abstract/text/table values, and compatible significance direction reconcile. |
| S005 | DOC-001 PDF p. 5, Table 2 | SPTB <37: 30/150 vs 49/150; RD -12.7% (-22.9 to -2.3); RR 0.61 (0.41-0.91); P=.02. | PASS_1_COMPLETE — reconciles. |
| S006 | DOC-001 PDF p. 5, Table 2 | SPTB <32: 10/150 vs 14/150; RD -2.6% (-4.1 to 9.4); RR 0.71 (0.33-1.56); P=.52. | PASS_1_COMPLETE — point is contained; non-null CIs and P direction are compatible. Bootstrap details preclude exact CI reproduction. |
| S007 | DOC-001 PDF p. 5, Table 2 | SPTB <28: 6/150 vs 9/150; RD -2.0% (-3.5 to 7.7); RR 0.67 (0.24-1.83); P=.60. | PASS_1_COMPLETE — reconciles subject to the stated bootstrap CI method. |
| S008 | DOC-001 PDF p. 5, Table 2 | Gestational-age mean difference 1.4 wk (0.6 to 2.3), P=.001. | PASS_1_COMPLETE — estimate is contained and direction/CI exclude zero consistently with P; group-level variance inputs for exact reproduction are absent. |
| S009 | DOC-001 PDF p. 5, Table 2 | Randomization-to-delivery mean difference 10.0 d (3.8 to 16.2), P=.002. | PASS_1_COMPLETE — containment and direction/P compatibility pass; exact variance inputs absent. |
| S010 | DOC-001 PDF p. 5, Table 2 | PPROM <34: 2/150 vs 2/150; RD 0 (-3.6 to 3.6); RR 1.00 (0.14-7.01); P>.99. | PASS_1_COMPLETE — null point estimates, intervals, counts, and P direction reconcile. |
| S011 | DOC-001 PDF p. 5, Table 2 | Cesarean: 45/150 vs 57/150; RD -8.0% (-3.2 to 19.0); RR 0.79 (0.57-1.09); P=.18. | PASS_1_COMPLETE — **proposal P02**: printed RD is outside its printed ordered CI; see checker. RR/P independently have compatible non-null direction. |
| S012 | DOC-001 PDF p. 5, Table 2 | Operative vaginal delivery: 5/150 vs 10/150; RD -3.4% (-2.1 to 9.1); RR 0.50 (0.18-1.43); P=.29. | PASS_1_COMPLETE — **proposal P03**: printed RD is outside its printed ordered CI; see checker. RR/P independently have compatible non-null direction. |
| S013 | DOC-001 PDF p. 5, Table 2 | Spontaneous vaginal delivery: 100/150 vs 83/150; RD 11.4% (-0.1 to 22.6); RR 1.20 (1.00-1.45); P=.06. | PASS_1_COMPLETE — counts, direction, containment, and borderline non-null P direction reconcile. |
| S014 | DOC-001 PDF pp. 1, 5 | Vaginal discharge: 130/150 vs 69/150; RD 40.7% (30.1 to 50.3); RR 1.88 (1.57-2.27); P<.001. | PASS_1_COMPLETE — repeated abstract/Table 2/narrative values reconcile. The inequality P display is not a display-zero. |
| S015 | DOC-001 PDF p. 5, Table 2 | Pelvic discomfort: 5/150 vs 1/150; RD 2.7% (-1.0 to 7.0); RR 5.00 (0.59-42.29); P=.22. | PASS_1_COMPLETE — reconciles. |
| S016 | DOC-001 PDF p. 5, Table 2 | Chorioamnionitis: 5/150 vs 7/150; RD -1.4% (-3.7 to 6.6); RR 0.71 (0.23-2.20); P=.77. | PASS_1_COMPLETE — reconciles. |
| S017 | DOC-001 PDF p. 5, Table 2 | Birth-weight mean difference 245.3 g (69.2 to 421.4), P=.006. | PASS_1_COMPLETE — containment and sign/P direction pass; exact variance inputs are not supplied. |
| S018 | DOC-001 PDF p. 5, Table 2 | NICU: 15/150 vs 28/150; RD -8.7% (-17.1 to -0.3); RR 0.54 (0.30-0.96); P=.04. | PASS_1_COMPLETE — reconciles. |
| S019 | DOC-001 PDF p. 5, Table 2 | Neonatal death: 1/150 vs 3/150; RD -1.3% (-2.1 to 5.1); RR 0.33 (0.04-3.17); P=.61. | PASS_1_COMPLETE — reconciles. |
| S020 | DOC-001 PDF p. 5, Table 2 | Perinatal death: 2/150 vs 4/150; RD -1.4% (-2.5 to 5.6); RR 0.50 (0.09-2.69); P=.68. | PASS_1_COMPLETE — reconciles. |
| S021 | DOC-001 PDF p. 5, Table 2 | Composite perinatal outcome: 22/150 vs 48/150; RD -17.3% (-27.0 to -7.3); RR 0.46 (0.29-0.72); P=.01. | PASS_1_COMPLETE — counts, estimate, labels, and inference direction reconcile. |
| S022 | DOC-001 PDF p. 5, Primary Outcome narrative | Cox/KM spontaneous-delivery analysis to 34 wk: HR 0.36; 95% CI 0.54-0.87. | PASS_1_COMPLETE — **proposal P01**: point estimate is not contained in its own CI and conflicts with the matched Figure 2 panel-B HR; see checker. |
| S023 | DOC-001 PDF p. 6, Figure 2 panel A | Any-delivery Cox/KM: HR 0.70 (0.55-0.88). | PASS_1_COMPLETE — point contained and label/event type is distinct from panel B. |
| S024 | DOC-001 PDF p. 6, Figure 2 panel B | Spontaneous-delivery-only Cox/KM: HR 0.68 (0.54-0.87). | PASS_1_COMPLETE — point contained; exact event and identical CI make this the direct S022 comparator. |
| S025 | DOC-001 PDF p. 6, subgroup narrative | Wald interaction: progesterone P=.56; CL <=10 versus >10 mm P=.46. | PASS_1_COMPLETE — exact matches to DOC-003 eTable 3 interactions (S049-S050); no exact Wald-model inputs for reproduction. |
| S026 | DOC-001 PDF pp. 4-5 | Secondary outcomes exploratory; no multiplicity adjustment. | PASS_1_COMPLETE — interpretation label agrees with Table 2 footnote and DOC-003 eTable 2; no candidate from multiplicity status alone. |
| S027 | DOC-002 PDF pp. 12-13, Sample Size | Protocol planned 50% reduction from 25% control risk for SPTB through 33 6/7 weeks; 300/150 per group by simulation. | PASS_1_COMPLETE — same broad planned power target as S001; `33 6/7` and `<34 weeks` are wording-compatible, while simulation inputs are insufficient for exact recalculation. |
| S028 | DOC-002 PDF p. 14, Primary analysis | Planned ITT, two-tailed 5%, 95% CI and adjusted logistic OR for SPTB <34 with cervical length covariate. | PASS_1_COMPLETE — main article explicitly reports a change from planned OR to unadjusted RR; it labels the change, so this is not itself a contradictory matched estimate. |
| S029 | DOC-002 PDF p. 14, Secondary analysis | KM SPTB <34 with gestational-age time scale, spontaneous-delivery event, elective-delivery censoring, HR. | PASS_1_COMPLETE — aligns with DOC-001 panel B/event definition; DOC-001 additionally reports a distinct any-delivery panel. No protocol HR is supplied for numerical comparison. |
| S030 | DOC-003 PDF p. 3, eTable 2 header/footnotes | Post hoc overall PTB/component outcomes; RR/95% CI; continuity-corrected chi-square P values; no multiplicity adjustment. | PASS_1_COMPLETE — explicitly exploratory and measure-labelled; all 13 row-level results are S031-S043. |
| S031 | DOC-003 PDF p. 3, eTable 2 | Overall PTB <37: 35/150 vs 53/150; RD -12.0 (-22.5 to -1.2); RR .66 (.46-.95); P=.03. | PASS_1_COMPLETE — reconciles; endpoint is overall (spontaneous plus indicated), not Table 2 SPTB <37. |
| S032 | DOC-003 PDF p. 3, eTable 2 | Overall PTB <34: 14/150 vs 26/150; RD -8.0 (-16.1 to -0.1); RR .54 (.29-.99); P=.04. | PASS_1_COMPLETE — reconciles; distinct from primary spontaneous endpoint. |
| S033 | DOC-003 PDF p. 3, eTable 2 | Overall PTB <32: 11/150 vs 15/150; RD -2.7 (-4.2 to +9.7); RR .73 (.35-1.54); P=.54. | PASS_1_COMPLETE — reconciles. |
| S034 | DOC-003 PDF p. 3, eTable 2 | Overall PTB <28: 7/150 vs 9/150; RD -1.3 (-4.4 to +7.1); RR .78 (.30-2.03); P=.80. | PASS_1_COMPLETE — reconciles. |
| S035 | DOC-003 PDF p. 3, eTable 2 | Iatrogenic PTB <34: 3/150 vs 3/150; RD 0 (-4.1 to +4.1); RR 1.00 (.21-4.88); P=1.00. | PASS_1_COMPLETE — reconciles; P=1.00 is not a display-zero. |
| S036 | DOC-003 PDF p. 3, eTable 2 | Birth weight <2500 g: 28/150 vs 45/150; RD -11.3 (-1.1 to +21.2); RR .62 (.41-.94); P=.03. | PASS_1_COMPLETE — **proposal P04**: RD is outside printed ordered CI; its CI includes zero whereas the reported RR/P direction is non-null. |
| S037 | DOC-003 PDF p. 3, eTable 2 | Birth weight <1500 g: 10/150 vs 15/150; RD -3.3 (-3.5 to +10.2); RR .67 (.31-1.44); P=.40. | PASS_1_COMPLETE — reconciles. |
| S038 | DOC-003 PDF p. 3, eTable 2 | NEC: 3/150 vs 4/150; RD -.7 (-3.5 to +5.0); RR .75 (.17-3.29); P=.99. | PASS_1_COMPLETE — reconciles. |
| S039 | DOC-003 PDF p. 3, eTable 2 | IVH grade 3/4: 4/150 vs 6/150; RD -1.3 (-3.5 to +6.2); RR .67 (.19-2.31); P=.75. | PASS_1_COMPLETE — reconciles. |
| S040 | DOC-003 PDF p. 3, eTable 2 | RDS: 14/150 vs 31/150; RD -11.4 (-19.9 to -2.9); RR .45 (.25-.81); P=.01. | PASS_1_COMPLETE — reconciles. |
| S041 | DOC-003 PDF p. 3, eTable 2 | BPD: 8/150 vs 12/150; RD -2.7 (-3.5 to +9.0); RR .67 (.28-1.58); P=.49. | PASS_1_COMPLETE — reconciles. |
| S042 | DOC-003 PDF p. 3, eTable 2 | ROP requiring therapy: 1/150 vs 9/150; RD -5.3 (-10.4 to -.9); RR .11 (.01-.87); P=.02. | PASS_1_COMPLETE — reconciles. |
| S043 | DOC-003 PDF p. 3, eTable 2 | Blood-culture proven sepsis: 9/150 vs 13/150; RD -2.7 (-3.8 to +9.3); RR .69 (.31-1.57); P=.50. | PASS_1_COMPLETE — reconciles. |
| S044 | DOC-003 PDF p. 4, eTable 3 header/footnotes | Post hoc SPTB <34 subgroups; within-row continuity-corrected chi-square P, Wald interaction P. | PASS_1_COMPLETE — all four subgroup rows and both interactions are S045-S050; supplied source gives no Wald covariates/SEs. |
| S045 | DOC-003 PDF p. 4, eTable 3 | Progesterone: 10/133 vs 21/125; RD -9.3 (-17.7 to -1.0); RR .45 (.22-.91); P=.04. | PASS_1_COMPLETE — counts, denominators, direction, containment, and P direction reconcile. |
| S046 | DOC-003 PDF p. 4, eTable 3 | No progesterone: 1/17 vs 2/25; RD -2.1 (-21.8 to +21.0); RR .74 (.07-7.48); P=.99. | PASS_1_COMPLETE — denominators complement S045 to group N=150; row reconciles. |
| S047 | DOC-003 PDF p. 4, eTable 3 | TVU CL <=10 mm: 3/56 vs 10/42; RD -18.4 (-34.6 to -3.3); RR .23 (.07-.77); P=.02. | PASS_1_COMPLETE — denominators match DOC-001 baseline category; row reconciles. |
| S048 | DOC-003 PDF p. 4, eTable 3 | TVU CL >10 mm: 8/94 vs 13/108; RD -3.5 (-5.8 to +12.5); RR .71 (.31-1.63); P=.56. | PASS_1_COMPLETE — denominators complement S047 and row reconciles. |
| S049 | DOC-003 PDF p. 4; DOC-001 PDF p. 6 | Progesterone-by-treatment Wald interaction P=.56. | PASS_1_COMPLETE — repeated locations agree; no model inputs to reproduce exactly. |
| S050 | DOC-003 PDF p. 4; DOC-001 PDF p. 6 | CL-category-by-treatment Wald interaction P=.46. | PASS_1_COMPLETE — repeated locations agree; no model inputs to reproduce exactly. |

## Pass-2 relationship completion record

An independent fresh statistical review revisited every S record after registration of C001-C010 and mechanical recheck. `PASS_2_COMPLETE` records a source-grounded check and not an adjudication. P/CI/test calculations were not treated as interchangeable when the sources specify bootstrap CIs, continuity-corrected chi-square P values, Cox analyses, or Wald interactions without all matching inputs.

| ID | PASS 2 result |
|---|---|
| S001 | PASS_1_COMPLETE; PASS_2_COMPLETE — planned n=300/150-per-arm, 25% baseline risk, 50% relative reduction, 80% power, and two-sided .05 remain compatible with the protocol plan; simulation inputs/code are missing, so exact power remains DIAGNOSTIC_ONLY. |
| S002 | PASS_1_COMPLETE; PASS_2_COMPLETE — chi-square, equal-variance t-test, and two-sided-rule labels were retained; no same-model contradiction is supplied. |
| S003 | PASS_1_COMPLETE; PASS_2_COMPLETE — ITT, bootstrap risk-difference/RR CIs, and Cox/KM definitions match the relevant displays; C001 remains the separate matched-HR conflict. |
| S004 | PASS_1_COMPLETE; PASS_2_COMPLETE — 11/150 versus 23/150, negative RD/RR direction, ordered containing CIs, and matched abstract/text/table repetition reconcile. |
| S005 | PASS_1_COMPLETE; PASS_2_COMPLETE — <37-week counts, negative RD, RR below 1, and P direction reconcile. |
| S006 | PASS_1_COMPLETE; PASS_2_COMPLETE — <32-week estimate is contained in its ordered RD CI and the non-null RR/CI/P direction is compatible; bootstrap details preclude exact CI reproduction. |
| S007 | PASS_1_COMPLETE; PASS_2_COMPLETE — <28-week count direction, estimate containment, labels, and non-null inference direction reconcile. |
| S008 | PASS_1_COMPLETE; PASS_2_COMPLETE — gestational-age mean difference is contained in its CI and direction agrees with P=.001; outcome SD/variance inputs are missing for exact test reproduction. |
| S009 | PASS_1_COMPLETE; PASS_2_COMPLETE — latency mean difference is contained in its CI and direction agrees with P=.002; exact variance inputs are missing. |
| S010 | PASS_1_COMPLETE; PASS_2_COMPLETE — equal PPROM counts, null RD/RR, containing CIs, and P>.99 reconcile. |
| S011 | PASS_1_COMPLETE; PASS_2_COMPLETE — C009 remains: the printed -8.0% RD is outside [-3.2, 19.0]; counts establish negative direction, while RR/CI and P are separately non-null compatible. |
| S012 | PASS_1_COMPLETE; PASS_2_COMPLETE — C003 and C010 remain distinct: printed count arithmetic and the -3.4% RD versus [-2.1, 9.1] containment rule are separate; no source establishes a replacement estimate/CI. |
| S013 | PASS_1_COMPLETE; PASS_2_COMPLETE — spontaneous-vaginal counts, positive RD, ordered containing CI, RR, and P=.06 direction reconcile. |
| S014 | PASS_1_COMPLETE; PASS_2_COMPLETE — discharge counts, positive RD/RR direction, CIs, and matched abstract/narrative/table values reconcile. |
| S015 | PASS_1_COMPLETE; PASS_2_COMPLETE — pelvic-discomfort direction, point containment, RR scale, and non-null P direction reconcile. |
| S016 | PASS_1_COMPLETE; PASS_2_COMPLETE — chorioamnionitis inferential display is internally coherent; C004 concerns only the distinct exact-fraction rounding diagnostic. |
| S017 | PASS_1_COMPLETE; PASS_2_COMPLETE — birth-weight mean difference, ordered containing CI, and P=.006 direction reconcile; outcome variance data are absent. |
| S018 | PASS_1_COMPLETE; PASS_2_COMPLETE — NICU counts, negative RD/RR direction, containing CIs, and P=.04 reconcile. |
| S019 | PASS_1_COMPLETE; PASS_2_COMPLETE — neonatal-death display has coherent direction, containing CIs, and non-null P. |
| S020 | PASS_1_COMPLETE; PASS_2_COMPLETE — perinatal-death inferential display is coherent; C005 is a separate exact-fraction rounding diagnostic. |
| S021 | PASS_1_COMPLETE; PASS_2_COMPLETE — composite-perinatal counts, negative RD/RR, CIs, and P=.01 reconcile; components are not summed because overlap is defined as possible. |
| S022 | PASS_1_COMPLETE; PASS_2_COMPLETE — C001 is confirmed by mechanical recheck: narrative HR 0.36 is outside 0.54-0.87 and conflicts with Figure 2B HR 0.68 with identical CI. |
| S023 | PASS_1_COMPLETE; PASS_2_COMPLETE — Figure 2A HR 0.70 (0.55-0.88) is contained and remains distinct any-delivery analysis. |
| S024 | PASS_1_COMPLETE; PASS_2_COMPLETE — Figure 2B HR 0.68 (0.54-0.87) is contained and is the exact C001 comparator. |
| S025 | PASS_1_COMPLETE; PASS_2_COMPLETE — interaction P=.56/.46 repetitions match eTable 3; Wald model inputs are not supplied. |
| S026 | PASS_1_COMPLETE; PASS_2_COMPLETE — exploratory/no-multiplicity label agrees across supplied table/footnote contexts; no discrepancy is inferred from this label. |
| S027 | PASS_1_COMPLETE; PASS_2_COMPLETE — protocol 33 6/7-week wording is compatible with <34 weeks; planned simulation cannot be recalculated from supplied inputs. |
| S028 | PASS_1_COMPLETE; PASS_2_COMPLETE — planned adjusted logistic OR and reported unadjusted RR are explicitly distinguished, so are not a matched-effect conflict. |
| S029 | PASS_1_COMPLETE; PASS_2_COMPLETE — protocol spontaneous-event/elective-censoring definition matches Figure 2B context; no protocol HR is supplied. |
| S030 | PASS_1_COMPLETE; PASS_2_COMPLETE — eTable 2 labels post hoc RR/CI and continuity-corrected chi-square P values; its row-level records follow. |
| S031 | PASS_1_COMPLETE; PASS_2_COMPLETE — overall <37-week PTB has coherent count direction, containing RD/RR CIs, and P direction; endpoint is not SPTB <37. |
| S032 | PASS_1_COMPLETE; PASS_2_COMPLETE — overall <34-week PTB counts reconcile to spontaneous plus iatrogenic rows and inferential display is coherent. |
| S033 | PASS_1_COMPLETE; PASS_2_COMPLETE — overall <32-week point is contained, labels/direction reconcile, and P direction is non-null. |
| S034 | PASS_1_COMPLETE; PASS_2_COMPLETE — overall <28-week point is contained, labels/direction reconcile, and P direction is non-null. |
| S035 | PASS_1_COMPLETE; PASS_2_COMPLETE — equal iatrogenic counts, null point/RR, containing CIs, and P=1.00 reconcile. |
| S036 | PASS_1_COMPLETE; PASS_2_COMPLETE — C006 remains: -11.3% lies outside [-1.1, +21.2]; negative count/RR direction corroborates but does not reconstruct a bootstrap RD CI. |
| S037 | PASS_1_COMPLETE; PASS_2_COMPLETE — <1500-g point/CI/RR/P direction reconcile. |
| S038 | PASS_1_COMPLETE; PASS_2_COMPLETE — NEC point/CI/RR/P direction reconcile. |
| S039 | PASS_1_COMPLETE; PASS_2_COMPLETE — IVH point/CI/RR/P direction reconcile. |
| S040 | PASS_1_COMPLETE; PASS_2_COMPLETE — RDS inferential display is coherent; C007 is a distinct fraction-rounding diagnostic. |
| S041 | PASS_1_COMPLETE; PASS_2_COMPLETE — BPD point/CI/RR/P direction reconcile. |
| S042 | PASS_1_COMPLETE; PASS_2_COMPLETE — ROP point/CI/RR/P direction reconcile. |
| S043 | PASS_1_COMPLETE; PASS_2_COMPLETE — sepsis point/CI/RR/P direction reconcile. |
| S044 | PASS_1_COMPLETE; PASS_2_COMPLETE — eTable 3 correctly distinguishes continuity-corrected within-row P values from Wald interactions; all component records follow. |
| S045 | PASS_1_COMPLETE; PASS_2_COMPLETE — progesterone subgroup counts, RD/RR directions, CIs, P, and complements reconcile. |
| S046 | PASS_1_COMPLETE; PASS_2_COMPLETE — no-progesterone subgroup counts, RD/RR directions, CIs, P, and complements reconcile. |
| S047 | PASS_1_COMPLETE; PASS_2_COMPLETE — <=10-mm subgroup inferential display is coherent; C008 is a separate near-boundary exact-fraction rounding diagnostic. |
| S048 | PASS_1_COMPLETE; PASS_2_COMPLETE — >10-mm subgroup counts, complements, point/CI/RR/P direction reconcile. |
| S049 | PASS_1_COMPLETE; PASS_2_COMPLETE — progesterone interaction P=.56 matches main narrative; Wald inputs remain absent. |
| S050 | PASS_1_COMPLETE; PASS_2_COMPLETE — cervical-length interaction P=.46 matches main narrative; Wald inputs remain absent. |

## Pass-1 completion record

- **Inventory count:** 50 stable S IDs (S001-S050).
- **PASS_1_COMPLETE count:** 50.
- **Relationship-level display-zero status:** No `P = 0`, `P = 0.000`, or equivalent result display was found. `DISPLAY_ZERO_NOT_CANDIDATE` is therefore not applicable to an individual S record in this package.
- **Candidate-proposal count:** 4 distinct proposals, described in `checkers/statistical_pass_1.md`; no stable C ID is assigned here.
- **Required pass-2 state:** Every S001-S050 requires `PASS_2_COMPLETE` after the cross-lane ledger and mechanical recheck are available.

## Pass-2 completion record

- **Inventory count:** 50 stable S IDs (S001-S050).
- **PASS_1_COMPLETE count:** 50.
- **PASS_2_COMPLETE count:** 50.
- **Pass-2 new candidate proposals:** 0. C001-C010 were reviewed against their source evidence and mechanical recheck; C001, C006, C009, and C010 remain the applicable inferential/cross-location containment candidates, while the other ledger entries are distinct arithmetic candidates.
- **Display-zero status:** No `P = 0`, `P = 0.000`, or equivalent was found; no candidate relies on a display-zero convention.
