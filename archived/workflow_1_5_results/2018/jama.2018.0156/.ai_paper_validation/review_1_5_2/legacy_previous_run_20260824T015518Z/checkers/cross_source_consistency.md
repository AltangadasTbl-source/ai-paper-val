# Cross-source consistency review

## Scope and method

This independent lane compared every canonical numeric relationship `N001`–`N098` and every canonical statistical relationship `S001`–`S055` against the newly prepared native-text/layout-text evidence and, only where explicitly authorized, the supplied OCR provenance assets. It did not use an old audit output, run OCR, or use web evidence.

For every proposed difference, the comparison first matched the population, analysis set, time point, treatment contrast, model/test, endpoint, unit/scale, reference group, and printed precision. Planned protocol/SAP inputs, administrative deadlines, blank forms, and externally cited studies were not substituted for observed CAAM results.

## Distinct cross-source candidate propositions

### CROSS-CAND-001 — Per-protocol ETI ROSC percentage conflicts with its displayed numerator, denominator, and signed risk difference

- **Locations:** [main article Table 2, PDF p. 6](../../../jama_jabre_2018_oi_180004.pdf#page=6), Per-Protocol Analysis, “Return of spontaneous circulation”; supporting fresh layout transcription `preprocessing/pymupdf_layout_text/DOC-001_jama_jabre_2018_oi_180004.txt` lines 549-567; canonical relationships `N022` and `S008`.
- **Matched comparison:** Per-protocol population, ROSC outcome (not survival or CPC), BMV minus ETI risk-difference column, and percentage scale.
- **Printed values:** BMV `342 (34.4)` of `n=995`; ETI `377 (30.0)` of `n=943`; printed BMV-minus-ETI difference `−5.6` percentage points (95% CI `−9.9 to −1.3`), `P=.01`.
- **Comparison logic:** `342 / 995 × 100 = 34.37%`, compatible with `34.4%`. `377 / 943 × 100 = 39.98%`, which rounds to `40.0%`, not `30.0%`. The count-derived difference is `34.37 − 39.98 = −5.61` percentage points, compatible with the printed `−5.6`; it is incompatible with `34.4 − 30.0 = +4.4` percentage points. Thus the ETI printed percentage conflicts with both its own count/denominator and the table's signed difference/CI direction.
- **Supported alternative(s):** The supplied evidence supports `40.0%` as the percentage consistent with the displayed `377/943` and `−5.6` difference. It does not establish whether the error was confined to the percentage glyph or arose upstream in a source table.
- **Human verification question:** In the publisher-quality Table 2 source, should the ETI per-protocol ROSC display read `377 (40.0)` rather than `377 (30.0)`? Confirm the underlying PP ROSC count and the risk-difference computation.

### CROSS-CAND-002 — Per-protocol day-28 survival CI is incompatible with the displayed event rates and accompanying P value at its stated percentage-point scale

- **Locations:** [main article Table 2, PDF p. 6](../../../jama_jabre_2018_oi_180004.pdf#page=6), Per-Protocol Analysis, “Survival at 28 d”; fresh simple/layout transcriptions `preprocessing/pymupdf_simple_text/DOC-001_jama_jabre_2018_oi_180004.txt` lines 776-783 and `preprocessing/pymupdf_layout_text/DOC-001_jama_jabre_2018_oi_180004.txt` lines 549-551; canonical `N021` and `S008`.
- **Matched comparison:** Per-protocol population, day-28 survival (not the primary CPC<=2 endpoint), BMV minus ETI absolute percentage-difference column, and two-sided 95% CI/P-value display.
- **Printed values:** BMV `54/995 (5.4%)`; ETI `51/943 (5.4%)`; printed difference `0.1` percentage points, 95% CI `−10 to 9.7`, `P=.99`.
- **Comparison logic:** The count-derived rates are `5.427%` and `5.408%`, a difference of `+0.018864` percentage points, which rounds to `0.0`, not the printed `0.1`; that distinct point-display issue is registered separately as C002. As a diagnostic approximation only, a standard unpooled binomial calculation from these two displayed numerators/denominators gives an approximate 95% risk-difference interval of about `−2.00 to 2.04` percentage points (standard error about `1.03` percentage points), not a span of `−10 to 9.7` percentage points. The same-row `P=.99` is retained as observed near-null context; it does not independently identify the CI variance or prove the printed span incompatible. The table footnote says the P values were calculated using chi-square or Fisher exact tests, and the supplied SAP says the secondary rate outcomes use percentage/difference estimates and 95% CIs, but neither gives the row-specific CI construction. The displayed CI scale/span therefore requires source verification against the matched counts and rates without asserting a replacement interval.
- **Supported alternative(s):** The evidence supports that the printed interval requires source verification. The supplied sources do **not** identify the intended lower/upper limits or prove that a decimal point alone accounts for the display; no replacement interval is asserted here.
- **Human verification question:** What are the generated 95% BMV-minus-ETI risk-difference CI limits for PP day-28 survival, and does the publisher table omit/misplace a decimal or contain another transcription error?

## Explicit coverage register — numeric relationships

| Relationship IDs reviewed | Cross-source result after matching controls |
|---|---|
| N001-N002 | Allocation/completion totals reconcile: arm sums and completion rounding agree across abstract, figure, and narrative. |
| N003-N009 | ITT primary, survival/admission/ROSC, and actual-treatment safety values reconcile across the matched abstract/narrative/tables with their row-specific denominators. |
| N010-N013 | Figure receipt/analysis branches reconcile where branches are non-overlapping; rescue-event rows explicitly permit multiple reasons and were not converted into persons. |
| N014-N019 | Table 1 count percentages, category totals, row-specific denominators, and continuous-measure labels/units are compatible with the displayed values. |
| N020 | ITT CPC categories total their matched denominators and CPC 1+2 yields the primary numerators. |
| N021 | PP survival and CPC distribution counts/percentages are internally compatible; the CI issue is separately recorded in CROSS-CAND-002. |
| N022 | PP admission is compatible; PP ROSC has the separate percentage conflict in CROSS-CAND-001. |
| N023-N024 | Table 3 preserves distinct row denominators; complication counts/percentages and scale labels are compatible. |
| N025 | Centre 5 population and CCF percentage are coherent; the pause arithmetic is coherent, but the named count-versus-seconds label remains the separately registered NUM-CAND-003/C004 issue. No additional cross-source proposition is created. |
| N026-N029 | Planned design values are distinct from observed results; hierarchy/PP model values and discussion repeat are matched to their proper analysis sets. |
| N030-N046 | Protocol V1.3 endpoint, secondary inventory, planned recruitment/sample-size/interim, centre/follow-up, administrative, and mRS-scale definitions match only like-for-like main/SAP content; no concrete numeric conflict. |
| N047-N052 | Protocol V1.4 scales, IDS/VAS/Han units, and blank SAE identifier fields remain definition/instrument evidence, not observed rates; no conflict. |
| N053-N084 | Repeated protocol endpoint/NI/design/analysis/missingness and recruitment statements are genuine planned-definition overlaps. The `5/centre/month` recruitment target is a rounded operational target, not an asserted equality to 2,000/20/24; no candidate. |
| N085-N093 | Later forms/amendment/SAP scales, centre amendment, endpoint, analysis-set, rounding, and missing-data statements agree with the appropriately versioned protocol content. |
| N094-N095 | eTable 1 centre counts total BMV 1018 and ETI 1022; one-decimal percentages are compatible. Centre labels are compatible with the amendment context and do not infer zero-participant centres. |
| N096-N098 | eTable 2 post-hoc rows use their own denominators; count-derived percentages, signed differences, CIs, and SAP direction/end-point labels are compatible after population matching. |

## Explicit coverage register — statistical relationships

| Relationship IDs reviewed | Cross-source result after matching controls |
|---|---|
| S001-S003 | ITT, hierarchical, and PP noninferiority results match only the corresponding endpoint, population, model, contrast, and one-sided 97.5% CI rule; no additional conflict. |
| S004-S007 | ITT day-28 survival/admission/ROSC and CPC-distribution estimates use matched two-sided rate/difference displays; no conflict. |
| S008-S009 | PP secondary and CPC-distribution displays reviewed. S008 includes CROSS-CAND-001 and CROSS-CAND-002; S009 is otherwise coherent. |
| S010-S017 | Safety, secondary-analysis, post-hoc CCF/pause, and design/interpretive records reconcile after retaining row-specific denominators, tests, units, and planned-versus-observed distinction. |
| S018-S031 | V1.3 protocol NI, population, missingness, and analysis rules are planned definitions; compatible with matched main/SAP definitions and not substituted for trial results. |
| S032-S045 | V1.4/V2 repetitions and external background statistics are appropriately labelled; no eligible within-package CAAM conflict. |
| S046-S052 | SAP native text controls over duplicate authorized OCR. Its direction, margin, ITT/PP/AT, rounding, and test/CI rules are compatible with matching displays. |
| S053 | eTable 1 is a denominator/contribution table, not an inferential comparison; arithmetic and rounding reconcile. |
| S054-S055 | eTable 2 post-hoc comparisons use distinct analysis populations. Their signed BMV-minus-ETI differences, counts, and CIs are coherent; no cross-population substitution made. |

## Limitations

- This review is limited to supplied local evidence. It does not determine the intended correction, source-data value, or whether either candidate arose before publication.
- DOC-002 p. 134 is empty in the fresh text assets and lacks authorized OCR; its absence is already recorded in the canonical inventories and it provided no matchable relationship.
- Authorized OCR was used only as documented for DOC-002 pp. 52, 108-109, and 126-133; readable native protocol/SAP text controls where the sources duplicate each other.

**Lane count:** 153/153 assigned canonical relationships explicitly covered (98 numeric; 55 statistical); 2 distinct candidate propositions; 151 relationship records with no additional qualifying cross-source candidate.
