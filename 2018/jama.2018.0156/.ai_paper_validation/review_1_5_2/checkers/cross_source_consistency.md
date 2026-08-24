# Cross-Source Consistency Review

## Scope and method

This lane reviewed all current canonical relationships: numeric `N001`--`N051` and statistical `S001`--`S038`. Evidence was limited to freshly prepared assets for the three supplied direct sources: DOC-001 (main article), DOC-002 (protocol versions, amendments, and SAP), and DOC-003 (eTables). No web source, legacy audit derivative, or new OCR was used.

For every comparison, the review first matched the analysis population, endpoint, time point, treatment contrast, model or test, measure, unit, reference group, version, and displayed precision. Planned values were not compared as if they were observed results. The records below are candidate signals for human adjudication, not stable candidate IDs or judgments.

## Qualifying candidate signals

### XSC-01 -- Per-protocol ETI ROSC percentage does not match its printed numerator, denominator, or signed difference

- **Category:** Denominator, proportion, or total inconsistency; cross-document numeric consistency check.
- **Exact locations:** [DOC-001 Table 2, PDF p. 6](../../../jama_jabre_2018_oi_180004.pdf#page=6), Per-Protocol Analysis, Return of spontaneous circulation; mapped in `N019` and `S013`.
- **Matched result:** Per-protocol participants, ROSC, BMV minus ETI percentage-point contrast.
- **Printed values:** BMV `342/995 (34.4%)`; ETI `377/943 (30.0%)`; difference `-5.6` percentage points (95% CI `-9.9` to `-1.3`), `P=.01`.
- **Comparison logic and calculation:** `342/995 = 34.37%`, which rounds to `34.4%`. `377/943 = 39.98%`, which rounds to `40.0%`, not `30.0%`. The count-derived contrast is `34.37 - 39.98 = -5.61` percentage points, agreeing with printed `-5.6`; the two displayed percentages instead imply `+4.4` percentage points.
- **Supported alternative:** The displayed count, denominator, signed difference, and CI direction all support an ETI percentage of `40.0%`. They do not establish whether only the percentage display or an upstream result was affected.
- **Human verification question:** Confirm the PP ROSC numerator, denominator, and published percentage in the production table; should the ETI display be `377 (40.0%)`?

### XSC-02 -- Per-protocol day-28-survival confidence-interval display requires verification against its matched counts and scale

- **Category:** Statistical reporting inconsistency.
- **Exact locations:** [DOC-001 Table 2, PDF p. 6](../../../jama_jabre_2018_oi_180004.pdf#page=6), Per-Protocol Analysis, Survival at 28 d; mapped in `N020` and `S010`.
- **Matched result:** Per-protocol participants, all-cause survival at day 28, BMV minus ETI percentage-point contrast, two-sided 95% CI.
- **Printed values:** BMV `54/995 (5.4%)`; ETI `51/943 (5.4%)`; difference `0.1` percentage points, 95% CI `-10 to 9.7`, `P=.99`.
- **Comparison logic and calculation:** The count-derived rates are `5.427%` and `5.408%` (difference `+0.019` percentage points). As a diagnostic approximation, the unpooled binomial standard error from the printed counts is about `1.03` percentage points, giving an approximate two-sided 95% risk-difference interval of `-2.00` to `2.04` percentage points. The displayed interval spans `19.7` percentage points despite a roughly 1,000-per-arm population. The SAP specifies a 95% CI for secondary proportion differences but does not supply this row's exact CI method, so this approximation does not establish a replacement value.
- **Supported alternative:** A decimal-place, transcription, or method/population-label explanation remains possible; no intended interval is recoverable from supplied evidence alone.
- **Human verification question:** Retrieve the generated PP day-28-survival risk-difference CI and confirm the intended endpoints and precision of both displayed limits.

### XSC-03 -- Main article reports 20 EMS centres whereas the supplied eTable lists 21 contributing investigator centres

- **Category:** Cross-document numeric inconsistency.
- **Exact locations:** [DOC-001 Methods, PDF p. 2](../../../jama_jabre_2018_oi_180004.pdf#page=2) states that the trial involved `20` prehospital EMS centres (`15` in France and `5` in Belgium); [DOC-003 eTable 1, PDF p. 2](../../../joi180004supp2_prod.pdf#page=2) lists 21 distinct investigator-centre rows: 1, 24, 5, 9, 12, 17, 13, 8, 3, 14, 22, 11, 15, 23, 16, 18, 20, 25, 7, 6, and 2. Mapped in `N044`.
- **Matched result:** Trial contributing-centre count, not the protocol's planned-centre total. The eTable is explicitly identified by the main article as the detailed source for inclusions by investigator centre.
- **Printed values and calculation:** The eTable has 21 labelled contributor rows; its BMV and ETI contributions sum respectively to the main ITT totals `1018` and `1022`. Centre 2 contributes `0` BMV and `3` ETI cases, so all 21 rows contain at least one participant across the two arms.
- **Comparison logic:** On the ordinary reading of `EMS centers` and `investigator centre`, the reported counts differ by one for the same enrolled trial. The supplied files do not state a one-to-many mapping that would make 21 investigator-centre rows correspond to 20 EMS centres.
- **Supported alternative:** One EMS centre may have been represented by more than one investigator-centre record, or the terms may be administrative rather than coextensive. The protocol amendment's planned 25-centre version is not used as the comparator.
- **Human verification question:** Provide the trial centre master list and identify whether the 21 eTable rows represent 20 EMS centres; if so, state the mapping or correct the relevant published count.

### XSC-04 -- Published primary-endpoint definition omits the later protocol's baseline-neurologic-disability qualification

- **Category:** Measure, label, or scale inconsistency.
- **Exact locations:** [DOC-001 abstract, PDF p. 1](../../../jama_jabre_2018_oi_180004.pdf#page=1) and [Methods, PDF p. 3](../../../jama_jabre_2018_oi_180004.pdf#page=3) define favorable outcome as CPC `1 or 2`; [DOC-002 amendment comparison, PDF p. 110](../../../joi180004supp1_prod.pdf#page=110), protocol v1.4 dated 22 September 2015, retains CPC `<=2` but states that, for neurologic disability before randomization, survival with the same degree of disability is considered favorable. Mapped in `N041`, `N051`, and `S037`.
- **Matched result:** Primary 28-day favorable-neurologic-survival endpoint. The comparison preserves the amendment version and is not a comparison to the earlier SAP alone.
- **Printed statements:** The main article's definition is CPC 1--2 with no baseline-disability qualification. The amendment explicitly adds the qualification to avoid bias from the pre-arrest neurologic state.
- **Comparison logic:** The later protocol text expands or qualifies the outcome classification beyond a CPC 1--2-only rule. The main article presents only the latter rule while reporting the primary counts `44/1018` and `43/1022`; supplied sources do not say whether any participant's classification depended on the qualification.
- **Supported alternative:** The article may use a concise description while its analysis implemented the amended definition, or no participant required the qualification. Neither alternative can be confirmed from the supplied package.
- **Human verification question:** Which primary-endpoint algorithm was applied to the reported primary counts, and were pre-randomization neurologic-disability cases adjudicated under the v1.4 qualification?

### XSC-05 -- Protocol's composite technique-failure definition is not reconcilable with the smaller ETI failure count if the article uses the same endpoint

- **Category:** Measure, label, or scale inconsistency.
- **Exact locations:** [DOC-002 amended protocol comparison, PDF p. 110](../../../joi180004supp1_prod.pdf#page=110) defines technique failure as 28-day mortality, regurgitation during the procedure, or failure to ventilate/intubate; [DOC-001 abstract, PDF p. 1](../../../jama_jabre_2018_oi_180004.pdf#page=1), [Results, PDF p. 4](../../../jama_jabre_2018_oi_180004.pdf#page=4), and [Table 3, PDF p. 6](../../../jama_jabre_2018_oi_180004.pdf#page=6) report ETI failure `21/996 (2.1%)`; Table 2 reports ITT ETI 28-day deaths `54/1022`. Mapped in `N012`, `N015`, `N022`, `N051`, `S015`, and `S037`.
- **Matched comparison:** The issue is definitional, not a direct comparison of ITT and safety rates. The safety ETI group has `999` people; only `24` of the `1023` ETI-randomized patients are excluded from that actual-treatment group in the flow diagram.
- **Comparison logic and calculation:** The flow shows 24 participants outside the 999-person ETI safety display, and the failure row has a further three-person denominator reduction to 996. Under a conservative conditional alignment, `54 - 24 - 3 = 27`, still exceeding 21. This supports a definition/population question if the article row is the protocol composite, but exact participant-set alignment is not mechanically established from aggregate ITT and actual-treatment displays.
- **Supported alternative:** The article's `BMV or ETI failure` may be a narrower procedural-failure measure, rather than the protocol's composite `technique failure`; a revised final analysis specification could also define it differently. The supplied sources do not define the article's row sufficiently to resolve this.
- **Human verification question:** What exact analysis definition and source population produced the Table 3 `failure` row, and was it intentionally distinct from the amended protocol's composite technique-failure endpoint?

## Complete coverage register

| Relationships reviewed | Matched-source result |
|---|---|
| N001-N008 | Allocation, analysis-set, baseline denominator, component-total, and one-decimal percentage relationships reconcile after retaining stated row denominators and overlapping-exclusion footnotes. |
| N009-N018 | ITT and PP primary/survival/admission/CPC results reconcile across abstract, narrative, figure, and Table 2 when population and endpoint are matched. |
| N019-N020 | XSC-01 and XSC-02 recorded above. |
| N021-N028 | Safety/adverse-event, CCF/pauses, scale, unit, analysis-set, and time-window records reconcile after retaining their row-specific denominators and measures. |
| N029-N040 | Original and early revised protocol endpoint, scale, population, planned recruitment, and analysis definitions have no additional qualifying contradiction after planned-versus-observed and version matching. |
| N041-N043 | Primary-endpoint and noninferiority definitions support XSC-04; the published primary result and margin conclusion otherwise match the appropriate rule. |
| N044-N045 | eTable 1 denominators and rounded percentages reconcile; its 21 contributor rows support XSC-03. |
| N046-N050 | eTable 2 post-hoc results, VAS, IDS, mRS, and CPC records reconcile with their distinct populations, contrasts, and scale definitions. |
| N051 | Versioned complication/failure definitions support XSC-04 and XSC-05; later additions are not otherwise treated as contradictions. |
| S001-S020 | Main primary, secondary, safety, post-hoc, and scale relationships reviewed. XSC-01, XSC-02, and XSC-05 are the applicable signals; all other like-for-like statistical displays are coherent at shown precision. |
| S021-S029 | Original/revised protocol ITT/PP, margin, CI, test, interim, sample-size, safety, and missing-data statements are planned definitions and have no additional matched conflict. |
| S030-S034 | SAP primary rule, analysis-set, missing-data, rounding, and secondary/safety test definitions are compatible with the matched published results. |
| S035-S036 | eTable 2 post-hoc P values, confidence intervals, counts, and percentage-point differences are coherent at displayed precision. |
| S037-S038 | Versioned endpoint/safety definitions reviewed: S037 contributes to XSC-04/XSC-05; fresh visual confirmation shows the IDS bands are coherent (`0<IDS<=5` slight and `IDS>5` difficult), with no scale contradiction. |

## Versioned noncontradictions and limitations

- The protocol's planned 2,000 participants, 20 centres, interim timing, and sample-size assumptions are not observed-result denominators. The later protocol administrative plan for up to 25 centres is likewise not used to contradict the final eTable contributor count.
- SAP version 1 (18 February 2015) predates the later v1.4/v2 amendments. Its narrower safety list is recorded as versioned provenance, not a standalone discrepancy.
- The supplied sources do not contain participant-level baseline neurologic-disability data, a centre crosswalk, or a final analysis-data dictionary defining the Table 3 failure row. Those omissions are why XSC-03 through XSC-05 retain explicit human questions.

**Lane count:** 89 of 89 current canonical relationships explicitly reviewed (51 numeric; 38 statistical). Five distinct qualifying candidate signals were emitted; the remaining relationship records had no additional qualifying cross-source inconsistency after matching controls.
