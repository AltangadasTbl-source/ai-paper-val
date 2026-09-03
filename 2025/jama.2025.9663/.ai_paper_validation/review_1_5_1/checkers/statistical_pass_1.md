# Statistical Consistency Review — Pass 1

## Scope, evidence basis, and rules

- **Reviewer execution:** fresh `gpt-5.6-terra`, high reasoning effort; runtime agent ID: `/root/statistical_pass_1`.
- **Assigned scope:** every inferential relationship in the canonical inventory, `S001` through `S034` (34/34). This is a pass-1 review record, not an adjudication or a candidate ledger.
- **Evidence used:** direct supplied PDFs `jama_martin_2025_oi_250042_1753377747.91025.pdf` (DOC-001), `joi250042supp1_prod_1753377747.92525.pdf` (DOC-002), and `joi250042supp2_prod_1753377747.93025.pdf` (DOC-003), located with the current quantitative maps. Direct rechecks included DOC-001 PDF pp. 5, 7-9; DOC-003 pp. 12, 14, and 24; and DOC-002 PDF p. 126. In particular, the DOC-002 SAP p. 16 primary-analysis definition directly agrees with the covariates/model framing reported in DOC-001.
- **Applied framework:** interval endpoint order and point containment; direction/contrast; effect, reference, unit, and scale labels; matched repetitions after population/time/model matching; and interval/P/test compatibility only where the supplied material identifies a compatible inferential quantity. Protocol/SAP entries were retained as prospective definitions, not treated as observed-result comparators.
- **Display-zero rule:** no assigned relationship has a coherent finite-precision `P = 0`/`P = .000` display. Planned thresholds (`P < .05` and `P < .001`) are not display zeros and are not candidates.
- **Result:** one distinct source-grounded observation is emitted below without a `C` ID. No severity, validity, acceptance, correction, or disposition is assigned.

## Relationship-level pass-1 records

| Stable ID | PASS_1_COMPLETE record |
|---|---|
| S001 | **PASS_1_COMPLETE.** DOC-001 p. 2 supplies a two-sided `P < .05`, 95% CI, no-multiplicity convention and covariate/site-clustering context. It is a coherent analysis convention. No observed estimate is supplied here; no interval/P calculation applies. |
| S002 | **PASS_1_COMPLETE.** DOC-001 p. 2 identifies logistic, Fine-Gray, ordered-logistic, Cox, marginal-standardisation, and imputation roles. These labels match Table 2 outcome families. The source does not state one universal variance/test mapping for all transformed measures; none was inferred. |
| S003 | **PASS_1_COMPLETE.** DOC-001 p. 2 states diagnosis/COVID/ethnicity interactions are tested on the OR scale and identifies post-hoc strata. Figure 3 uses adjusted multilevel logistic OR-scale interaction tests, consistent with that definition. No within-subgroup effect was misread as an interaction test. |
| S004 | **PASS_1_COMPLETE.** The primary adjusted RD `0.7` lies within `-0.7` to `2.0`; RR `1.02 (0.98-1.06)` and OR `1.04 (0.97-1.11)` contain their nulls. DOC-001 pp. 1, 5, and 7 repeat the multiply-imputed RD and `P=.28` with matched population/contrast. The OR/CI is diagnostically compatible with `P=.28` under the stated logistic model. No discrepancy found. |
| S005 | **PASS_1_COMPLETE.** DOC-001 p. 7 gives Fine-Gray sHR `1.00 (0.96-1.04), P=.97`; estimate lies in ordered CI and direction is neutral. The near-null CI is diagnostically compatible with the P value. No discrepancy found. |
| S006 | **PASS_1_COMPLETE.** DOC-001 p. 7 gives Fine-Gray sHR `0.98 (0.94-1.02), P=.27`; estimate lies in ordered CI and direction/competing-risk label are consistent. A log-scale diagnostic is compatible at printed precision. No discrepancy found. |
| S007 | **PASS_1_COMPLETE.** DOC-001 p. 7 reports POR available-case `1.00 (0.95-1.06)` and imputed `1.01 (0.96-1.07), P=.64`; all CIs are ordered and contain estimates/null. The table does not explicitly identify which estimation scale/model output the single P value tests; therefore no exact P/CI reconciliation was asserted. |
| S008 | **PASS_1_COMPLETE.** ICU-discharge RDs (`0.2 [-1.2,1.6]`; imputed `-0.1 [-1.3,1.1]`) are ordered, contain their estimates/null, and respect conservative-minus-usual direction. `P=.94` has no printed effect-scale/test linkage beyond the table's logistic-model framework, so an exact RD/P test was not inferred. |
| S009 | **PASS_1_COMPLETE.** Acute-hospital-discharge RDs (`0.9 [-0.6,2.3]`; `0.5 [-0.8,1.9]`) are internally ordered and directionally labelled. The single `P=.46` is not explicitly assigned to an RD-scale test; missing exact test-scale/variance definition recorded. No discrepancy found. |
| S010 | **PASS_1_COMPLETE.** Sixty-day RDs (`1.1 [-0.2,2.5]`; `0.8 [-0.6,2.2]`) are ordered and contain estimates/null. The imputed RD has a diagnostic Wald-style relation compatible with `P=.25`; exact P-scale/test mapping is not printed. |
| S011 | **PASS_1_COMPLETE.** One-year RDs (`1.0 [-0.7,2.6]`; `3.3 [-0.7,7.3]`) are ordered and contain estimates/null. Available-linkage denominators are explicitly distinct from all-randomized denominators. The table does not state whether `P=.34` is an RD-scale, logistic-coefficient, or other test; no unsupported P/CI contradiction was registered. |
| S012 | **PASS_1_COMPLETE.** DOC-001 p. 7 footnote specifies site/stratum/COVID/splines/date adjustment, imputation, and 1-hour censoring. DOC-002 SAP PDF p. 126 directly supplies the same primary adjustment covariates, marginal-RD strategy, and site random-effect context. No cross-source model-label conflict found. |
| S013 | **PASS_1_COMPLETE.** All diagnosis-subgroup RDs contain estimates and their CIs; ORs are positive and CIs contain estimates. Stratum event counts sum to the stated primary outcome totals. `P=.67` is explicitly an adjusted OR-scale interaction test, not a within-stratum test. No discrepancy found. |
| S014 | **PASS_1_COMPLETE.** COVID-stratum RDs/ORs have ordered intervals containing estimates; signs correspond to conservative-minus-usual event proportions. The two strata sum to primary denominators/deaths. `P=.11` is an OR-scale interaction test. No discrepancy found. |
| S015 | **PASS_1_COMPLETE.** Ethnicity-stratum intervals are ordered and contain estimates; the printed `-0` RD is coherent rounded signed display, not a display-zero P value. Outcome-available ethnicity denominators are explicitly a smaller subset and must not be compared to Table 1 linkage denominators as though identical. `P=.64` is an OR-scale interaction test. |
| S016 | **PASS_1_COMPLETE.** DOC-003 p. 12 and DOC-001 p. 5 match adjusted HR `1.01 (0.96-1.05)`; DOC-003 gives `P=.82`, censoring and linkage restrictions. Estimate/CI direction is neutral and a log-scale diagnostic is compatible at printed precision. Missing exact Cox variance/tie/censoring implementation prevents an exact reconstruction. |
| S017 | **PASS_1_COMPLETE.** DOC-003 p. 14 predicted-risk-tertile ORs `1.19`, `1.00`, `1.09` lie within ordered CIs; all labels identify adjusted ORs and `P=.18` as interaction. No discrepancy found. |
| S018 | **PASS_1_COMPLETE.** DOC-003 p. 14 APACHE-II-tertile ORs `1.04`, `1.06`, `1.06` lie within ordered CIs; `P=.98` is the adjusted OR-scale interaction. No discrepancy found. |
| S019 | **PASS_1_COMPLETE.** DOC-003 p. 14 PaO2/FIO2-subgroup ORs `1.15`, `1.00`, `0.98`, `1.11` lie within ordered CIs; `P=.36` is the adjusted OR-scale interaction. No discrepancy found. |
| S020 | **PASS_1_COMPLETE.** DOC-003 p. 14 data-collection ORs and CIs are ordered and estimates are contained; the enhanced-first-10 OR `1.43 (1.08-1.90)` has a direction consistent with its positive RD. The displayed `.18` and `.03` occur in an interaction-P column; the supplied footnote defines them as interaction tests, so they were not inappropriately tested against individual treatment-effect CIs. |
| S021 | **PASS_1_COMPLETE.** DOC-003 p. 24 explicitly defines single PaO2/FIO2 imputation, outcome-specific imputation models, complete-case ethnicity subgroup handling, and ICU/hospital censoring. Counts and the 13,052 one-year-reached population match main-paper qualifiers. No missingness/model identity conflict found. |
| S022 | **PASS_1_COMPLETE.** DOC-002 p. 26 is prospective v1.1 design: 34% to 31.5%, 2.5 percentage points, two-sided alpha .05, 90% power, n=16,500, 5% allowance. It is not an observed result and the sample-size formula/variance assumptions are not supplied; no reconstruction or cross-version contradiction asserted. |
| S023 | **PASS_1_COMPLETE.** DOC-002 pp. 12-13 labels external historical evidence as RR `0.91 (0.75-1.09)`, hyperoxia RR `1.21 (1.03-1.43)`, and OR `1.22 (1.12-1.33)`. Each estimate is within an ordered CI and RR/OR labels are distinguished. These are not UK-ROX results. |
| S024 | **PASS_1_COMPLETE.** DOC-002 original/final protocol and SAP entries are prospective. Version-specific 34%-to-31.5% versus 37%-to-34.5% scenarios and 5% versus 6% allowances are explicitly different planning versions, not matched result repetitions. Primary endpoint/ITT/adjustment/effect labels are coherent when version-matched. |
| S025 | **PASS_1_COMPLETE.** DOC-002 planned binomial/Poisson, normal, Wilcoxon, Kaplan-Meier/Cox/shared-frailty methods are prospective and distinguish binary, continuous, duration, and survival scales. No completed result or P/CI pair is supplied to test. |
| S026 | **PASS_1_COMPLETE.** DOC-002 prospective subgroup and interim definitions label Peto-Haybittle `P<.001` at 4,500/10,000 as a stopping threshold. It is not a reported P value or display-zero result. No discrepancy found. |
| S027 | **PASS_1_COMPLETE.** DOC-002 specifies prospective ITT mean incremental cost/QALY/NMB at 90 days with 95% CIs, multilevel modelling, sensitivity and lifetime analyses. No observed economic estimate is supplied; no interval/P compatibility check applies. |
| S028 | **PASS_1_COMPLETE.** DOC-002 traffic-light thresholds are prospective operational progression definitions, not an effect estimate or inferential result. No candidate applies. |
| S029 | **PASS_1_COMPLETE.** DOC-002 pp. 88-112 are prospective SHEAP opening material and contain no observed inferential result. The source labels plan identity/version; no comparator is supplied. |
| S030 | **PASS_1_COMPLETE.** DOC-002 p. 87 records v1.8 addition of ordinal 30-day DAWOS; p. 88 identifies SHEAP v1.0 as linked to v1.5. This is a documented version constraint, not an unqualified contradictory outcome statement. No completed result is supplied. |
| S031 | **PASS_1_COMPLETE.** DOC-002 p. 120 supplies prospective two-sided `P<.05`, 95% CI, and no-multiplicity convention; p. 119 separately supplies interim `P<.001`. Their distinct purposes are explicit; neither is a display-zero P value. |
| S032 | **PASS_1_COMPLETE.** DOC-002 pp. 119, 124, and 126 prospectively define 90-day all-cause mortality, ITT, site/Mega-ROX/calendar-time adjustment, 95% CI/P reporting, and no futility rule. The supplied final SAP p. 126 details the covariates/marginal-RD model that align with DOC-001. No model/estimand conflict found. |
| S033 | **PASS_1_COMPLETE.** DOC-002 p. 121 explicitly permits re-randomisation after >=90 days and defines ITT/known-primary-outcome inclusion regardless of adherence. This establishes, rather than contradicts, the population rule. No result-level conflict found. |
| S034 | **PASS_1_COMPLETE.** DOC-002 pp. 127-131 contain planned subgroup, sensitivity, economic, and lifetime analyses only; no observed estimate, CI, P value, statistic, or result repetition is supplied for reconciliation. |

## Source-grounded observation emitted for candidate registration/recheck

### SP1-O001 — Extraneous arterial-pressure unit attached to usual-group SpO2 value

- **Applicable check domain:** measure, label, and scale consistency; identified while checking the article’s treatment-effect/statistical context (`S004`, `S012`) and the matched oxygen-exposure evidence.
- **Exact source location:** DOC-001, `jama_martin_2025_oi_250042_1753377747.91025.pdf#page=6`, Oxygen Exposure paragraph (printed p. 403).
- **Direct printed evidence:** the conservative group is stated as “median SpO2 of `93.3% (2.8%)` and the median PaO2 of `71.5 (13.9) mm Hg`,” whereas the paired usual-group text is “`95.1% (2.4%) mm Hg` and `79.5 (17.9) mm Hg`, respectively.”
- **Comparator and reproducible rule:** the sentence explicitly pairs SpO2 and PaO2 using “respectively.” SpO2 is a percent measure and PaO2 is mm Hg; attaching `mm Hg` immediately after the usual-group SpO2 result gives that result both `%` and `mm Hg`, unlike its conservative counterpart and the pair’s stated scale definitions.
- **Direct observation versus inference:** direct observation is the source’s unit string. A typesetting/unit carryover is only a possible explanation and is not asserted.
- **Human question:** should the `mm Hg` following `95.1% (2.4%)` be removed or repositioned so that it labels only PaO2? Confirm against the production source and any authoritative corrected version. This observation needs mechanical recheck before stable candidate registration.

## Limitations and excluded inferences

- Several Table 2 secondary-outcome P values are displayed once beside available/imputed effect columns without an explicit statement of the exact scale/test to which each P applies. No contradiction was inferred from a rough RD/CI calculation where the supplied logistic-model test could be on another scale.
- Exact reconstruction is unavailable where the source does not supply a variance estimator, covariance structure, test statistic, sidedness at the individual-result level, or a direct P-to-effect-scale linkage. Any calculations noted above are labelled diagnostic and were not used to manufacture a candidate.
- Planning documents and their version history establish definitions but do not provide observed effects. Version changes were treated as documented changes, not discrepancies.
- No web, legacy candidate ledger, legacy checker, or prior report conclusion was used.

## Pass-1 totals

- **Relationships assigned/completed:** 34/34 (`S001`-`S034`).
- **Distinct source-grounded observations emitted:** 1 (`SP1-O001`), without a stable candidate ID.
- **Display-zero exclusions recorded:** 0 applicable display-zero results; 2 prospective threshold conventions distinguished from display zeros (`S026`, `S031`).
