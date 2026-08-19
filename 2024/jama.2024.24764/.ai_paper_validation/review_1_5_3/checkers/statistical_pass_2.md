# Statistical Consistency Review — Pass 2

## Completed scope and evidence boundary

This independent pass revisited every canonical statistical relationship `S001` through `S035` after the complete cross-lane candidate ledger (`C001`-`C007`) and the mechanical evidence recheck were available. The direct supplied sources were DOC-001 (main article, pp. 1-11), DOC-002 (SAP, pp. 1-46), DOC-003 (results supplement, pp. 1-9), and DOC-004 (protocol, pp. 1-48). The stable `S` records in `statistics/relationship_inventory.md` now all bear `PASS_2_COMPLETE`.

The checks covered denominator and arithmetic implications, population and analysis-set matching, duplicate values, effect-measure/label/scale, rate-versus-count distinctions, figures, and cross-source repetition. Point-estimate containment, endpoint order, sign/direction, and interval/P-value compatibility were revisited only to the extent the printed definitions support them. No old report conclusion or web source was used.

- **Relationships completed:** 35/35 (`S001`-`S035`).
- **Existing stable-ledger implications reviewed:** 7/7 (`C001`-`C007`).
- **New candidate records emitted in pass 2 and subsequently registered:** 1 (C008).
- **Display-zero review:** No observed result is printed as `P = 0`, `p = 0.000`, or an equivalent display zero. No display-zero candidate was emitted.

## Relationship-by-relationship pass-2 record

| S ID | Pass-2 recheck result | Cross-lane/recheck implication |
|---|---|---|
| S001 | Sample-size arithmetic and the planned 25% to 15% contrast remain internally consistent across DOC-001, DOC-002, and DOC-004. | No ledger implication. |
| S002 | The final binary-outcome RR/RD labels, control reference, model family, and stated CI convention remain compatible. Final fallback/convergence selection is not supplied. | No ledger implication. |
| S003 | The 112/394 versus 108/394 result, RD, RR, CI ordering, direction, and repeated values agree. The labelled log-RR diagnostic remains compatible with `P=.78`; no exact reconstruction is asserted without final model inputs. | C005 concerns mortality, not the primary SSI denominator or effect. |
| S004 | Per-protocol RR/CI containment and the main/supplement repetition remain compatible; the supplement has no P comparator. | No ledger implication. |
| S005 | All six sensitivity RRs remain within ordered CIs and correctly oriented around the RR null. Their separately printed sensitivity definitions preclude treating them as duplicate primary values. | No ledger implication. |
| S006 | UK-only LOS ratio 0.91 (0.82-1.02) is contained in its ordered positive CI and directionally labelled correctly. | C007 remains the separate effect-measure/model difference. The stated UK-only planned population is relevant to the new pass-2 record below. |
| S007 | The SAP/protocol adjusted-mean-difference (or skewed unadjusted-median-difference) plan and final log-transformed ratio-of-geometric-means report remain distinct supplied descriptions. | Reaffirms C007 without adjudication. |
| S008 | All-country LOS ratio 0.96 (0.88-1.06) is contained in its ordered positive CI. The final article explicitly includes Australian sites, while the SAP and protocol specify UK-only LOS analysis/reporting. | New `SP2-CAND-001` below; distinct from C007 because it concerns analysis population, not effect measure/model. |
| S009 | Main and supplement day-30 SF-12 PCS values match at displayed precision; scale, reference, direction, CI, and P are compatible. | C006's covariance/SE specification remains separate. |
| S010 | Main and supplement day-30 SF-12 MCS values match at displayed precision; scale, reference, direction, CI, and P are compatible. | C006's covariance/SE specification remains separate. |
| S011 | Pain day-7 MD is contained in the ordered CI; lower-is-better direction, 1-10 scale, and qualitative CI/P relation are compatible. The normal-CI result is a diagnostic approximation only. | No ledger implication. |
| S012 | Pain day-30 MD is contained in the ordered CI; CI crossing zero and `P=.61` are qualitatively compatible. | No ledger implication. |
| S013 | Readmission counts, RD/RR labels, endpoints, directions, and main narrative/table repetitions remain compatible. | No ledger implication. |
| S014 | Wound-complication counts, RD/RR labels, endpoints, directions, and main narrative/table repetitions remain compatible. | No ledger implication. |
| S015 | Figure 2's overall event counts and RR/CI duplicate Table 3 and eFigure 3 at displayed precision. | No ledger implication. |
| S016 | Every contamination-subgroup RR is contained in its ordered CI; the family interaction P has no compatible printed statistic/SE/CI comparator. | No ledger implication. |
| S017 | Both stoma-subgroup RRs are contained in ordered CIs and direction labels are compatible; no interaction-test reconstruction is possible from supplied inputs. | No ledger implication. |
| S018 | All surgical-procedure subgroup RRs are contained in ordered CIs and direction labels are compatible; no interaction-test reconstruction is possible from supplied inputs. | No ledger implication. |
| S019 | All BMI subgroup RRs are contained in ordered CIs; observed category bounds and labels remain compatible. | No ledger implication. |
| S020 | Both incision-length subgroup RRs are contained in ordered CIs and correctly directed. | No ledger implication. |
| S021 | All skin-preparation subgroup RRs are contained in ordered CIs and correctly directed. | No ledger implication. |
| S022 | UK and Australian subgroup RRs are contained in ordered CIs and correctly directed. These are primary-outcome subgroups, not the LOS-analysis population rule. | No ledger implication. |
| S023 | All assessment-method subgroup RRs are contained in ordered CIs and correctly directed. | No ledger implication. |
| S024 | Both UK pandemic subgroup RRs are contained in ordered CIs and correctly directed. | No ledger implication. |
| S025 | SAP/protocol two-sided 95% CI and 5% final-test conventions agree. The planned interim boundary is not an observed result. | No ledger implication. |
| S026 | The SAP's unstructured covariance plus robust sandwich SE and the main article's independent covariance are distinct named specifications for the same QoL model family. | Reaffirms C006 without adjudication; neither the supplement nor recheck supplies the final covariance/variance estimator. |
| S027 | SF-12 PCS repeated-measures estimates are contained in ordered CIs, directional/scale labels agree, and the day-30 repetition matches S009. | C006 does not create an observable value mismatch here; covariance and SE remain unreported. |
| S028 | SF-12 MCS repeated-measures estimates are contained in ordered CIs, directional/scale labels agree, and the day-30 repetition matches S010. | C006 does not create an observable value mismatch here; covariance and SE remain unreported. |
| S029 | Each EQ-5D index estimate is contained in its ordered CI; the printed scale/reference/direction and qualitative CI/P relations agree. | C006 does not create an observable value mismatch here; covariance and SE remain unreported. |
| S030 | Each EQ-5D health-score estimate is contained in its ordered CI; the printed scale/reference/direction and qualitative CI/P relations agree. | C006 does not create an observable value mismatch here; covariance and SE remain unreported. |
| S031 | Repeated-measures reference group, direction, adjustment terms, and treatment-by-time label remain compatible across sources. | C006 remains isolated to the covariance/variance-estimation difference. |
| S032 | The supplied source hierarchy and overlap rule explain why eTable 6 timepoint counts do not form mutually exclusive primary totals. | No rate/count or denominator implication from C001-C005. |
| S033 | Tipping-point plot null and direction labels agree with the narrative. No numerical coordinates, CI, statistic, or SE are supplied for additional compatibility testing. | No ledger implication. |
| S034 | The final article's longitudinal model statement is internally coherent with the results tables. | C006 remains the cross-document model-specification issue. |
| S035 | The final article's log-transformed LOS model is internally coherent with both reported ratios. | C007 remains the effect-measure/model issue; the all-country population issue is separately recorded in `SP2-CAND-001`. |

## Complete cross-lane ledger and mechanical-recheck implications

| Stable ID | Statistical-pass-2 implication |
|---|---|
| C001 | Smoking denominators concern Table 1 descriptive percentages. They do not alter a printed inferential relationship, CI, P value, or model in S001-S035. |
| C002 | Operating-surgeon level totals concern descriptive Table 2 multi-response/analysis-unit definition. No linked inferential relationship is printed. |
| C003 | Fascia-closing surgeon level totals concern descriptive Table 2 multi-response/analysis-unit definition. No linked inferential relationship is printed. |
| C004 | Skin-closing surgeon level totals concern descriptive Table 2 multi-response/analysis-unit definition. No linked inferential relationship is printed. |
| C005 | Figure 1's 25 reported deaths versus 24 mortality-within-30-days observations have an unresolved time-window distinction. No mortality effect estimate, CI, or P value is printed, and the primary/secondary inferential relationships are not thereby recalculated. |
| C006 | The SAP/final longitudinal covariance and variance-estimation specifications differ. This directly relates to S026 and gives a missing-definition limitation for S009-S010 and S027-S031, not a basis to recompute their P values. |
| C007 | The planned and final LOS effect measure/model differ. This directly relates to S006-S008, S007, and S035. It is separate from the pass-2 finding about the all-country LOS population. |

## New candidate record (no C ID assigned)

### SP2-CAND-001 — Reported all-country length-of-stay analysis differs from the stated UK-only SAP/protocol population

- **Category:** Analysis-unit or population inconsistency.
- **Direct observation:** The SAP says LOS will be analysed for UK-randomised patients only and that all patients randomised from Australia will be excluded (DOC-002 p.25; also defines LOS as UK-only at p.18). The protocol says LOS after surgery will be reported for UK patients only (DOC-004 p.25). The final article reports the UK-only LOS result and additionally states, “When the Australian sites were included,” presenting ratio of geometric means 0.96 (95% CI, 0.88-1.06), `P=.21` (DOC-001 pp.1,6,8).
- **Consistency rule:** A prespecified endpoint-specific analysis population is part of the reported result identity. An Australia-inclusive LOS estimate is not the same population as the specified UK-only analysis.
- **Direct comparison:** This is distinct from C007: C007 compares effect measure/model (mean or median difference versus ratio of geometric means); this record compares the stated UK-only population with the reported Australia-inclusive result.
- **Necessary inputs and missing definitions:** The planned population statement and final all-country result are supplied. The package does not supply an amendment, a final analysis-plan revision, a stated rationale for adding Australian LOS data, or the all-country model's result-specific SE/df/estimand mapping.
- **Alternative source-grounded interpretation:** The all-country analysis may be an additional, documented or otherwise intended analysis, while the UK-only result remains reported. No supplied source establishes whether that expansion was prespecified or amended.
- **Exact human question:** Was the Australia-inclusive LOS analysis prespecified or documented in an amendment/final SAP, and how should its analysis population and relation to the UK-only endpoint be labelled for extraction and interpretation?
- **Status:** Pending Human Adjudication.

## Limitations

- The supplied sources do not provide result-specific SEs, degrees of freedom, covariance estimates, variance-estimator output, selected convergence/fallback model, multiplicity implementation, or all estimand mappings. Exact CI/P/test-statistic reconstruction is therefore not inferred from convention.
- The canonical evidence recheck confirms the printed C001-C008 inputs and retains the named unresolved definitions; it does not supply an amendment, analysis dataset, or participant-level data.
- The tipping-point figures do not provide numerical coordinate data.
- No coherent finite-precision display-zero P-value notation was present. None was treated as a candidate.

## Handoff

The coordinator appended the new record as C008 without renumbering C001-C007 and completed a fresh mechanical recheck. No existing stable ID was deleted, suppressed, or adjudicated.
