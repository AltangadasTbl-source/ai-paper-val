# Statistical Consistency Check — Pass 1

## Completion and evidence boundary

Fresh PASS 1 checked S001-S050 in `statistics/relationship_inventory.md` against the supplied PDFs only. The fresh main and support quantitative evidence maps, source PDF pages, fresh layout text, and rendered result pages were used. This is a quality-control candidate-proposal record, not an adjudication. All proposal records are **Pending Human Adjudication** if registered by the coordinator.

Checks applied: CI endpoint order and point containment; count-to-risk-difference/RR direction; effect labels and reference direction; matched abstract/text/table/figure/supplement repetitions; and P/CI/test compatibility only where the source specifies a matching procedure. Bootstrap CIs, Cox-model inputs, and Wald-model inputs were not reverse engineered where absent.

## Candidate proposals for coordinator registration

### P01 — Textual spontaneous-delivery Cox HR is incompatible with its CI and Figure 2

- **Suggested category:** Statistical reporting inconsistency; Cross-document numeric inconsistency.
- **Exact source locations:** DOC-001 `jama_saccone_2017_oi_170144.pdf#page=5`, Primary Outcome narrative; DOC-001 `jama_saccone_2017_oi_170144.pdf#page=6`, Figure 2 panel B (Spontaneous delivery only).
- **Direct observation:** The narrative prints “hazard ratio, **0.36**; 95% CI, **0.54-0.87**” for the survival analysis to 34 weeks. Figure 2 panel B prints “Hazard ratio, **0.68**; 95% CI, **0.54-0.87**” for spontaneous delivery only.
- **Comparator and rule:** For a reported HR with a numerical CI on the same HR scale, the point estimate must lie between the ordered endpoints. Matched spontaneous-delivery locations also should reproduce the same HR when they show the same CI and analysis label.
- **Calculation / reproducible comparison:** `0.36 < 0.54`; the narrative HR is outside `[0.54, 0.87]`. Its printed CI exactly equals the panel-B CI, while the panel-B point estimate is `0.68`, not `0.36`.
- **Inference boundary:** The source does not provide Cox coefficient/SE data, so this record does not infer which displayed HR is intended or whether a transcription/production process caused the mismatch.
- **Alternative source-grounded interpretation:** Panel A is a distinct any-delivery analysis (HR 0.70, CI 0.55-0.88), but panel B and the narrative are both expressly spontaneous-delivery survival analyses with the same 0.54-0.87 CI; the event-definition distinction therefore does not reconcile 0.36 with the quoted CI/panel B.
- **Human question:** Which HR and CI pair was output for the spontaneous-delivery Cox analysis to 34 weeks, and should either printed location be corrected?

### P02 — Cesarean risk-difference point estimate is outside printed interval

- **Suggested category:** Statistical reporting inconsistency.
- **Exact source location:** DOC-001 `jama_saccone_2017_oi_170144.pdf#page=5`, Table 2, “Cesarean delivery, No. (%)”.
- **Direct observation:** Pessary 45/150 (30.0%) and control 57/150 (38.0%); printed between-group difference **-8.0% (-3.2 to 19.0)**. The same row prints RR 0.79 (0.57-1.09), P=.18.
- **Comparator and rule:** A point estimate must fall within its own ordered printed 95% CI.
- **Calculation / reproducible comparison:** `-8.0 < -3.2`; hence `-8.0` is outside `[-3.2, 19.0]`. The displayed arm percentages independently yield `30.0 - 38.0 = -8.0` percentage points, confirming the reported point-estimate direction.
- **Inference boundary:** The bootstrap resampling details are not supplied, so this check does not attempt to calculate a replacement CI. The RR CI and P value independently include the null and are compatible with each other; they do not repair the RD containment failure.
- **Alternative source-grounded interpretation:** The printed interval may have an endpoint/sign/order transcription issue, but the supplied sources do not identify the intended endpoints.
- **Human question:** Does the Table 2 Cesarean risk-difference CI belong to the printed -8.0% estimate and, if so, what are its verified signed endpoints?

### P03 — Operative-vaginal-delivery risk-difference point estimate is outside printed interval

- **Suggested category:** Statistical reporting inconsistency.
- **Exact source location:** DOC-001 `jama_saccone_2017_oi_170144.pdf#page=5`, Table 2, “Operative vaginal delivery, No. (%)”.
- **Direct observation:** Pessary 5/150 (3.3%) and control 10/150 (6.7%); printed between-group difference **-3.4% (-2.1 to 9.1)**. The same row prints RR 0.50 (0.18-1.43), P=.29.
- **Comparator and rule:** A point estimate must fall within its own ordered printed 95% CI.
- **Calculation / reproducible comparison:** `-3.4 < -2.1`; hence `-3.4` is outside `[-2.1, 9.1]`. The displayed arm percentages give `3.3 - 6.7 = -3.4` percentage points after rounding.
- **Inference boundary:** No bootstrap draws or exact CI construction inputs are supplied; this is a containment finding, not a reconstructed CI.
- **Alternative source-grounded interpretation:** An endpoint/sign/order transcription issue could explain the display, but the supplied package does not state a verified alternative interval.
- **Human question:** Does the Table 2 operative-vaginal risk-difference CI belong to the printed -3.4% estimate and, if so, what are its verified signed endpoints?

### P04 — Birth-weight-under-2500-g risk-difference point estimate is outside printed interval

- **Suggested category:** Statistical reporting inconsistency.
- **Exact source location:** DOC-003 `joi170144supp2_prod.pdf#page=3`, eTable 2, “Birth weight <2,500 grams”.
- **Direct observation:** Pessary 28/150 (18.7%) and control 45/150 (30.0%); printed difference **-11.3% (-1.1 to +21.2)**, RR 0.62 (0.41 to 0.94), P=.03. The table labels `RR` relative risk and specifies continuity-corrected chi-square P values.
- **Comparator and rule:** A point estimate must lie in its own ordered CI. A displayed CI that includes zero also has a different null-direction implication from this row’s RR CI and P value, although CI methods need not be assumed identical.
- **Calculation / reproducible comparison:** `18.7 - 30.0 = -11.3` percentage points after rounding, but `-11.3 < -1.1`, so the printed point is outside `[-1.1, +21.2]`. The printed RD CI includes zero; RR 0.62 (0.41-0.94) excludes one and P=.03 is below .05.
- **Inference boundary:** The package does not state the risk-difference CI construction method. No exact replacement interval or causal explanation is inferred. The candidate is based on direct RD/CI non-containment; the RR/P comparison is corroborating context only.
- **Alternative source-grounded interpretation:** A sign or endpoint-order transcription issue could reconcile the output, but no supplied record gives the intended interval.
- **Human question:** What verified risk-difference CI corresponds to the eTable 2 -11.3% estimate, and are the displayed signs/endpoints correct?

## Complete no-proposal / missing-definition record

- **S001, S027:** The sample-size statements are planned simulations. The common n=300, 150/group, 25% baseline, and 50% reduction target reconcile at the supplied conceptual level. Simulation code, allocation assumptions, and complete inputs are absent; no exact power claim was tested.
- **S002-S003, S026, S028-S030, S044:** Analysis definitions, effect labels, ITT population, exploratory/no-multiplicity labels, and the explicit protocol OR-to-reported-RR change were checked. No candidate is proposed solely for a protocol-versus-report analysis change that the main source directly describes.
- **S004-S010, S013-S021:** Printed counts, point estimates, CIs, effect directions, labels, and supplied compatible P/test rules reconcile. Exact bootstrap or mean-outcome CI reproduction is not possible from supplied inputs where noted in the inventory.
- **S023-S025, S029, S049-S050:** The two Figure 2 panels have distinct supplied event definitions; panel-B HR/CI is internally coherent. Main-text and eTable 3 interaction P values agree. Cox/Wald coefficients, covariance, and SE inputs are not supplied.
- **S031-S035, S037-S043:** Every eTable 2 row other than P04 has an ordered CI containing its point estimate and a count/RR/P direction compatible with the stated continuity-corrected chi-square test at displayed precision. Overall PTB was not equated with spontaneous PTB.
- **S045-S048:** All eTable 3 subgroup rows reconcile. Progesterone denominators (133+17 and 125+25) and cervical-length denominators (56+94 and 42+108) each equal 150; their labels and SPTB <34 endpoint agree with the table footnotes and matched main baseline denominators.

## Display-zero determination

No result relationship in DOC-001, DOC-002, or DOC-003 displays `P = 0`, `p = 0.000`, or an equivalent. Consequently no proposal concerns display-zero notation; no display-zero tail probability was calculated or criticized.

## Pass-1 totals and limitations

- **Explicit complete PASS 1 scope:** S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050.
- **Stable relationship scope:** S001-S050, all `PASS_1_COMPLETE`.
- **Distinct candidate proposals:** 4 (P01-P04); no C IDs assigned.
- **Limitations:** The package does not supply bootstrap replicates/CI method details, individual outcome variance data, Cox coefficients/SEs, Wald model covariates/SEs, or protocol simulation code. These absent inputs are not inferred from convention.
- **Pass-2 requirement:** Revisit all S001-S050 after the full cross-lane candidate ledger and mechanical evidence recheck exist; then update every inventory record to `PASS_2_COMPLETE` in a distinct fresh statistical-agent run.
