# Statistical Consistency Review — Pass 1

## Scope and method

This fresh-source pass covers every assigned inferential relationship: `S001`–`S050` and `S501`–`S513` (63 total). It used the canonical statistical and numeric relationship inventories, the current-run evidence maps, current-run native/layout text, and the four supplied PDFs. No old audit output, web source, OCR text, or unsupplied model convention was used.

For each relationship, the review checked printed point-estimate containment and endpoint ordering; estimate sign/direction against the named contrast; effect-measure/scale labels; matching repeated locations; and denominator/arithmetic or cross-source implications where the supplied source defined a comparable result. Interval/P-value/test/statistic/SE reconciliation was deliberately not performed where the PDF did not supply the needed same-test, sidedness, degrees of freedom, covariance, variance estimator, or multiplicity rule. The recorded calculations below are diagnostic display comparisons, not reconstructions of the reported models.

No supplied result prints `P = 0`, `p = 0.000`, or an equivalent display-zero P value. Therefore there is no `DISPLAY_ZERO_NOT_CANDIDATE` record in this pass. Printed numeric point estimates of `0.0` are not P values and were not treated as display zeros.

## Pass-1 candidate proposals (not stable IDs)

These are distinct proposals for the coordinator's duplicate merge and stable-ID registration. Each remains **Pending Human Adjudication**; this pass assigns no severity, validity, correction, or acceptance.

### P1-S008-01 — In-hospital beta-blocker risk-difference upper endpoint differs between Table 2 and Results text

- **Relationships:** `S008`.
- **Category proposed:** Cross-document numeric inconsistency / Statistical reporting inconsistency.
- **Exact source locations:** [Table 2, PDF p. 6](../../../jama_huffman_2018_oi_170166.pdf#page=6), in-hospital beta-blocker row; [Results text, PDF p. 7](../../../jama_huffman_2018_oi_170166.pdf#page=7), beta-blocker sentence.
- **Printed values:** Table 2 reports adjusted risk difference `6.25 (4.10 to 8.40)`; the narrative reports `6.25% [95% CI, 4.10%-8.10%]`. Both identify the intervention-versus-control beta-blocker result and show the same point estimate and lower endpoint.
- **Reproducible rule:** The same matched estimate, contrast, measure, and stated 95% interval should repeat the same displayed endpoints at the stated precision. The upper endpoints `8.40%` and `8.10%` differ by `0.30` percentage points.
- **Alternative source-grounded interpretations:** One occurrence may be a transcription/display error; alternatively, the table and narrative may refer to distinct analyses, but neither location supplies a different population, adjustment set, time point, or estimand that identifies such a distinction.
- **Human question:** Which upper 95% CI endpoint belongs to the named adjusted beta-blocker risk difference? **Pending Human Adjudication.**

### P1-S021-01 — Discharge beta-blocker adjusted estimates differ between Table 2 and Results text

- **Relationships:** `S021`.
- **Category proposed:** Cross-document numeric inconsistency / Statistical reporting inconsistency.
- **Exact source locations:** [Table 2, PDF p. 6](../../../jama_huffman_2018_oi_170166.pdf#page=6), discharge beta-blocker row; [Results text, PDF p. 7](../../../jama_huffman_2018_oi_170166.pdf#page=7), discharge-treatment sentence.
- **Printed values:** Table 2 reports adjusted risk difference `6.69 (4.43 to 8.95)` and OR `1.48 (1.30-1.68)`. The narrative reports adjusted risk difference `6.63% [95% CI, 4.43%-8.95%]` and adjusted OR `1.47 [95% CI, 1.30-1.68]` for the same named outcome.
- **Reproducible rule:** Repeated matched estimates should agree at their printed precision when the population, contrast, measure, and interval are unchanged. The repeated risk-difference point estimates differ by `0.06` percentage points and the OR point estimates by `0.01`; both intervals are printed identically.
- **Alternative source-grounded interpretations:** One occurrence may be a transcription or rounding inconsistency. A distinct analysis could explain it only if a different adjustment, population, time point, or estimand existed; neither printed occurrence states one.
- **Human question:** Do both narrative point estimates describe the Table 2 adjusted discharge beta-blocker analysis, and if so which printed values should be retained? **Pending Human Adjudication.**

### P1-S505-01 — Planned and reported age-subgroup cutpoints do not match while the article calls the results prespecified

- **Relationships:** `S505`, with the matched reported subgroup display in `S037`–`S039`.
- **Category proposed:** Measure, label, or scale inconsistency / Cross-document numeric inconsistency.
- **Exact source locations:** [SAP PDF p. 7](../../../joi170166supp2_prod.pdf#page=7), section 7.5.2; [Figure 3, main article PDF p. 9](../../../jama_huffman_2018_oi_170166.pdf#page=9); [main Methods, PDF p. 3](../../../jama_huffman_2018_oi_170166.pdf#page=3), which says prespecified participant-level results are reported.
- **Printed values/statements:** The SAP lists age subgroups `(<65 years and >65 years)`. Figure 3, titled “by Prespecified Subgroups,” instead displays `<50`, `50-69`, and `≥70` years.
- **Reproducible rule:** A result described as prespecified should have a source-identifiable mapping to the supplied prespecified subgroup definition. The supplied age cutpoints are neither the same two strata nor an explicit recoding of them.
- **Alternative source-grounded interpretations:** The analysis plan may have been amended, another prespecification document may exist outside the supplied package, or the article may use “prespecified” at a broader category level rather than for its exact cutpoints. Those possibilities are not defined in the supplied sources.
- **Human question:** Was there a prespecified amendment or documented analysis rule authorizing the Figure 3 age categories? **Pending Human Adjudication.**

### P1-S507-01 — eTable 1 comparison columns and difference footnote name incompatible groups

- **Relationships:** `S507`.
- **Category proposed:** Measure, label, or scale inconsistency.
- **Exact source location:** [Supplement 3 eTable 1, PDF p. 17](../../../joi170166supp3_prod.pdf#page=17).
- **Printed values/statements:** The table title and columns identify `Complete Follow Up, n=21,079` and `Missing Follow Up, n=295`; its difference column contains, for example, age `-0.6 (-2.0 to 0.8)`. Footnote `a` says `Difference = intervention minus control`.
- **Reproducible rule:** A footnote defining a difference must name the two groups printed in that table’s comparison columns. Complete versus missing follow-up and intervention versus control are distinct supplied population partitions.
- **Alternative source-grounded interpretations:** Footnote `a` may have been carried forward from another table; the values may be correctly computed for complete-versus-missing follow-up despite the mismatched label. The supplied table does not state the intended comparator for its difference column elsewhere.
- **Human question:** What groups do the displayed eTable 1 differences and CIs compare? **Pending Human Adjudication.**

## Complete relationship records

`No candidate proposed` means no independent supplied-source contradiction was identified under the applicable stated rule. It does not assert an unreported model property.

| S ID | PASS-1 record | Checks and source-defined limitation |
|---|---|---|
| S001 | PASS_1_COMPLETE — No candidate proposed | Planning inputs are internally repeated. The supplied design-effect/sample-size calculation and distributional inputs are insufficient to reconstruct 80% power. |
| S002 | PASS_1_COMPLETE — No candidate proposed | Main threshold labels agree with the planned interim/final values. The supplied text does not define a recalculation distribution beyond named z boundaries. |
| S003 | PASS_1_COMPLETE — No candidate proposed | Direction and units of the two troponin medians are clear. Test type, sidedness, and variance rule for `P<.001` are not supplied. |
| S004 | PASS_1_COMPLETE — No candidate proposed | RD lies within ordered CI; OR lies within ordered CI and has direction compatible with intervention-versus-control label. |
| S005 | PASS_1_COMPLETE — No candidate proposed | RD and OR each lie within ordered CIs; all intervals cross their stated nulls. |
| S006 | PASS_1_COMPLETE — No candidate proposed | Containment, endpoint ordering, and intervention-minus-control sign label are compatible. |
| S007 | PASS_1_COMPLETE — No candidate proposed | Containment, endpoint ordering, and effect labels are compatible. |
| S008 | PASS_1_COMPLETE — P1-S008-01 proposed | Both occurrences are otherwise label-, direction-, and point-estimate-compatible; cross-location CI upper endpoint mismatch is recorded above. |
| S009 | PASS_1_COMPLETE — No candidate proposed | RD/OR containment and ordered endpoints are compatible with supplied Table 2 labels. |
| S010 | PASS_1_COMPLETE — No candidate proposed | RD/OR containment and ordered endpoints are compatible with supplied Table 2 labels. |
| S011 | PASS_1_COMPLETE — No candidate proposed | Both adjusted fields are printed `Nonestimable`; no rule or competing estimate is supplied to support further reconciliation. |
| S012 | PASS_1_COMPLETE — No candidate proposed | Negative RD is contained in ordered CI; OR below 1 is contained in ordered CI and matches direction label. |
| S013 | PASS_1_COMPLETE — No candidate proposed | RD and OR are contained in ordered CIs; their null-crossing pattern is compatible. |
| S014 | PASS_1_COMPLETE — No candidate proposed | Quantile-model beta and marginal difference are separately labelled and need not agree numerically; both are CI-contained. |
| S015 | PASS_1_COMPLETE — No candidate proposed | RD/OR containment, endpoint ordering, and direction are compatible. |
| S016 | PASS_1_COMPLETE — No candidate proposed | Quantile-model beta and marginal difference are separately labelled; both intervals are ordered and contain their estimates. |
| S017 | PASS_1_COMPLETE — No candidate proposed | RD/OR containment, endpoint ordering, and direction are compatible. |
| S018 | PASS_1_COMPLETE — No candidate proposed | RD/OR containment, endpoint ordering, and direction are compatible. |
| S019 | PASS_1_COMPLETE — No candidate proposed | RD/OR containment, endpoint ordering, and direction are compatible. |
| S020 | PASS_1_COMPLETE — No candidate proposed | RD/OR containment and ordered endpoints are compatible. |
| S021 | PASS_1_COMPLETE — P1-S021-01 proposed | Table/narrative intervals agree, but both repeated point estimates differ; candidate recorded above. |
| S022 | PASS_1_COMPLETE — No candidate proposed | RD/OR containment and ordered endpoints are compatible. |
| S023 | PASS_1_COMPLETE — No candidate proposed | RD/OR containment and ordered endpoints are compatible with the EF-restricted discharge population. |
| S024 | PASS_1_COMPLETE — No candidate proposed | Both adjusted fields are `Nonestimable`; no competing estimate or supplied estimation rule permits a contradiction check. |
| S025 | PASS_1_COMPLETE — No candidate proposed | Table, abstract, and narrative primary estimates match at printed precision; RDs/ORs are contained in ordered CIs. |
| S026 | PASS_1_COMPLETE — No candidate proposed | Table/narrative repeated mortality estimates match; RD and OR intervals contain their point estimates. |
| S027 | PASS_1_COMPLETE — No candidate proposed | Cluster and temporal estimates are distinct named models; all printed intervals are ordered and contain estimates. |
| S028 | PASS_1_COMPLETE — No candidate proposed | Cluster and temporal estimates are distinct named models; all printed intervals are ordered and contain estimates. |
| S029 | PASS_1_COMPLETE — No candidate proposed | Cluster and temporal estimates are distinct named models; all printed intervals are ordered and contain estimates. |
| S030 | PASS_1_COMPLETE — No candidate proposed | Cluster and temporal estimates are distinct named models; all printed intervals are ordered and contain estimates. |
| S031 | PASS_1_COMPLETE — No candidate proposed | Cluster and temporal estimates are distinct named models; all printed intervals are ordered and contain estimates. |
| S032 | PASS_1_COMPLETE — No candidate proposed | Positive RDs and ORs above 1 match intervention-minus-control/intervention-versus-control labels and their ordered CIs. |
| S033 | PASS_1_COMPLETE — No candidate proposed | Positive RDs and ORs above 1 match intervention-minus-control/intervention-versus-control labels and their ordered CIs. |
| S034 | PASS_1_COMPLETE — No candidate proposed | Equal printed cluster/temporal point values are not duplicate-result contradictions because their CIs/models differ and are labelled separately. |
| S035 | PASS_1_COMPLETE — No candidate proposed | Narrative and eTable 7 expanded-outcome results match; displayed intervals are ordered and contain estimates. |
| S036 | PASS_1_COMPLETE — No candidate proposed | Figure is explicitly unadjusted and graphical; marker/control definitions and 95% CI label are clear, but exact plotted values are unavailable for numerical compatibility testing. |
| S037 | PASS_1_COMPLETE — No candidate proposed | Figure 3 adjusted RD/OR estimates are contained in ordered CIs; direction label is compatible with named intervention/control columns. |
| S038 | PASS_1_COMPLETE — No candidate proposed | Figure 3 adjusted RD/OR estimates are contained in ordered CIs; direction label is compatible. |
| S039 | PASS_1_COMPLETE — No candidate proposed | Figure 3 adjusted RD/OR estimates are contained in ordered CIs; direction label is compatible. |
| S040 | PASS_1_COMPLETE — No candidate proposed | Figure 3 adjusted RD/OR estimates are contained in ordered CIs; adjusted results need not reproduce crude rate differences. |
| S041 | PASS_1_COMPLETE — No candidate proposed | Figure 3 adjusted RD/OR estimates are contained in ordered CIs; adjusted results need not reproduce crude rate differences. |
| S042 | PASS_1_COMPLETE — No candidate proposed | Figure 3 adjusted RD/OR estimates are contained in ordered CIs; adjusted results need not reproduce crude rate differences. |
| S043 | PASS_1_COMPLETE — No candidate proposed | Figure 3 adjusted RD/OR estimates are contained in ordered CIs; adjusted results need not reproduce crude rate differences. |
| S044 | PASS_1_COMPLETE — No candidate proposed | Figure 3 adjusted RD/OR estimates are contained in ordered CIs; adjusted results need not reproduce crude rate differences. |
| S045 | PASS_1_COMPLETE — No candidate proposed | Figure 3 adjusted RD/OR estimates are contained in ordered CIs; adjusted results need not reproduce crude rate differences. |
| S046 | PASS_1_COMPLETE — No candidate proposed | Figure 3 adjusted RD/OR estimates are contained in ordered CIs; adjusted results need not reproduce crude rate differences. |
| S047 | PASS_1_COMPLETE — No candidate proposed | Figure 3 adjusted RD/OR estimates are contained in ordered CIs; adjusted results need not reproduce crude rate differences. |
| S048 | PASS_1_COMPLETE — No candidate proposed | Figure 3 adjusted RD/OR estimates are contained in ordered CIs; adjusted results need not reproduce crude rate differences. |
| S049 | PASS_1_COMPLETE — No candidate proposed | Figure 3 adjusted RD/OR estimates are contained in ordered CIs; adjusted results need not reproduce crude rate differences. |
| S050 | PASS_1_COMPLETE — No candidate proposed | Figure 3 adjusted RD/OR estimates are contained in ordered CIs; adjusted results need not reproduce crude rate differences. |
| S501 | PASS_1_COMPLETE — No candidate proposed | Protocol and SAP both define the planned stepped-wedge comparison; their planned schedule is compatible. |
| S502 | PASS_1_COMPLETE — No candidate proposed | Repeated planned power inputs agree. Design effect, correlation structure, and power-calculation algorithm are not supplied, so no diagnostic reconstruction was performed. |
| S503 | PASS_1_COMPLETE — No candidate proposed | ITT, complete-case, and multiple-imputation analyses are separately named; no reported estimate/test is supplied for direct compatibility checks. |
| S504 | PASS_1_COMPLETE — No candidate proposed | The SAP primary model has a random hospital effect and fixed four-month time effect; it matches the main paper’s named primary-model structure. |
| S505 | PASS_1_COMPLETE — P1-S505-01 proposed | Planned age cutpoints and Figure 3 prespecified age labels differ; candidate recorded above. |
| S506 | PASS_1_COMPLETE — No candidate proposed | The SAP prints the O’Brien-Fleming z/P thresholds together. No model-specific tail-probability definition beyond the printed boundary is supplied, so no convention-based recalculation was used. |
| S507 | PASS_1_COMPLETE — P1-S507-01 proposed | eTable 1’s complete/missing columns conflict with its intervention/control difference footnote; candidate recorded above. |
| S508 | PASS_1_COMPLETE — No candidate proposed | Each displayed marginal difference is within an ordered 95% CI; model and intervention-minus-control direction are expressly defined. |
| S509 | PASS_1_COMPLETE — No candidate proposed | eTable 5’s four columns are separately adjusted sensitivity models. Similar values to Table 3 were not treated as duplicates because covariate models differ. |
| S510 | PASS_1_COMPLETE — No candidate proposed | eTable 6 is expressly a time-exposure interaction model; its ORs/ordered CIs are self-contained and not directly comparable to base-effect ORs. |
| S511 | PASS_1_COMPLETE — No candidate proposed | eTable 7 RDs/ORs are contained in ordered CIs and its cluster-only versus temporal models are explicitly distinguished; narrative expanded-MACE result matches. |
| S512 | PASS_1_COMPLETE — No candidate proposed | The supplied residual definition, zero reference, CI rule, and left/right direction agree. Exact graphical values are not printed. |
| S513 | PASS_1_COMPLETE — No candidate proposed | eFigures are labelled unadjusted and their exact point values are graphical only; direction/scale labels are compatible, but numerical interval checks are unavailable. |

## Pass-1 totals and limitations

- **Relationships completed:** 63/63 (`S001`–`S050`, `S501`–`S513`).
- **Candidate proposals:** 4 (`P1-S008-01`, `P1-S021-01`, `P1-S505-01`, `P1-S507-01`), all **Pending Human Adjudication**.
- **No-candidate relationship records:** 59.
- **Display-zero P-value records:** 0 (no such supplied P-value display).
- **Key limitations:** Exact test-statistic/P-value/SE reconciliation was not applicable without a supplied compatible test and inferential specification. Graphical eFigure and Figure 2 values lack exact printed labels. Power and stopping-boundary recalculation was not undertaken because the required detailed design and distributional definitions are not supplied. Differences between crude rates and model-adjusted RDs/ORs were not treated as contradictions.
