# Cross-Source Quantitative Consistency Review

## Assignment and method

- Role: `qc13_cross_source_consistency_reviewer`.
- Assigned scope: every matchable quantitative result and definition in DOC-001
  (`jama_flint_2019_oi_190079.pdf`, pp. 1-10), DOC-002 (`joi180151supp1_prod.pdf`, pp. 1-7), and
  DOC-003 (`joi180151supp2_prod.pdf`, pp. 1-29), including abstract, narrative, tables, figures,
  captions, footnotes, protocol rules, and supplemental analyses.
- Matching rule: population, time, contrast, model, measure, scale, unit, reference group, analysis
  set, and displayed precision were matched before comparison. Differently defined estimands were
  retained as separate records rather than treated as conflicts.
- Evidence method: the two workflow 1.3.1 quantitative evidence maps and the current source/evidence
  inventories were used as locators. Every candidate below was then checked against the direct PDF
  page(s). No legacy candidate, checker, verifier, critic, or report output was used.
- Document-identity boundary: DOC-001 is a psychotic-depression randomized trial with DOI
  `10.1001/jama.2019.10517`; DOC-002 and DOC-003 are the protocol and supplement for an aspirin
  primary-prevention meta-analysis with DOI `10.1001/jama.2018.20578`. Consequently, no clinical
  population, outcome, treatment contrast, or statistical result in DOC-001 can truthfully be matched
  to DOC-002 or DOC-003. This package-level identity mismatch is recorded as a limitation, not turned
  into a quantitative candidate. DOC-001 internal cross-location matches and DOC-002-to-DOC-003
  matches were nevertheless reviewed completely.
- Output convention: `CS-###` labels are provisional checker labels only. They are not stable `C`
  identifiers and carry no disposition. Every candidate remains for human adjudication.

## Complete checked-match inventory

| Match ID | Matched locations and exact relationship scope | Result |
|---|---|---|
| XM-001 | DOC-001 pp. 1-2: 36-week design, 4 centers, November 2011-June 2017 study period, and June 13, 2017 final follow-up | Matched at displayed precision; no candidate. |
| XM-002 | DOC-001 pp. 1, 3-5: randomized total 126, allocations 64/62, all-randomized analysis, and arm headers | Matched; 64 + 62 = 126 and both arms are retained in the primary analysis. |
| XM-003 | DOC-001 pp. 1-2 and 6: relapse results 13 (20.3%) and 34 (54.8%), with denominators 64 and 62 | Matched at displayed precision; no cross-location candidate. |
| XM-004 | DOC-001 pp. 1 and 6-7: primary Cox result HR 0.25, 95% CI 0.13-0.48, P<.001 | Matched. The Figure 2 log-rank P<.001 on p. 7 is a different named test and was not equated to the adjusted Cox result. |
| XM-005 | DOC-001 pp. 1 and 7: all 8 adjusted daily-rate estimates and CIs for weight, waist, total cholesterol, LDL, HDL, triglyceride, glucose, and HbA1c | Numeric vectors match. The HbA1c unit conflicts with Table 4's scale; candidate CS-001. |
| XM-006 | DOC-001 pp. 1 and 3: abstract 114/126 completion statement against mutually labeled branch outcomes in Figure 1 | The 114 equals 126 minus 12 discontinuations; relapse is an outcome-ending state under the stated follow-up rule. No cross-location mismatch was assigned, but the paper does not explicitly define “completed” in the abstract. |
| XM-007 | DOC-001 pp. 3 and 6-8: relapse totals and Table 3 event-type counts, including psychiatric hospitalization 6/13 and 11/34 | Narrative and table counts match; Table 3 expressly permits more than one event per relapse, so event-type sums were not treated as mutually exclusive totals. |
| XM-008 | DOC-001 pp. 4, 7-8: planned NNT 5 for a prespecified 20% risk difference versus observed HR-based NNT 2.8 repeated in Results/Discussion | The two NNTs have different stated bases and contexts; the repeated observed value matches. No cross-source candidate. |
| XM-009 | DOC-001 pp. 1, 7-8: adjusted treatment-by-time daily rates versus Table 4 unadjusted within-arm baseline-to-termination changes | Population and measures overlap, but estimand, model, missingness handling, and time contrast differ. They were not treated as conflicting quantities. |
| XM-010 | DOC-001 pp. 7 and 9: narrative statement of no significant incident-high metabolic differences versus all 4 Table 5 risk-difference intervals | Direction and interval inclusion of zero match; no candidate. |
| XM-011 | DOC-001 pp. 4 and 6: AIMS, Barnes, and Simpson-Angus range statements | Item, global, and head-dropping-excluded total scales are differently labeled. No cross-location conflict was assigned. |
| XM-012 | DOC-002 pp. 2-4 against DOC-003 pp. 2-4 and 7-9: population, aspirin/no-aspirin contrast, primary composite, secondary efficacy/safety outcomes, and trial eligibility concepts | Matched. Trial-specific outcome heterogeneity is explicitly mapped in eTable 1 rather than silently normalized. |
| XM-013 | DOC-002 pp. 3 and 7 against DOC-003 p. 2: search dates | The final November 1, 2018 date matches the documented protocol change. Earlier January 2015/August 31, 2018 dates are identified as earlier search/update stages, not simultaneous final dates. |
| XM-014 | DOC-002 pp. 5-6 against DOC-003 pp. 3-4: extracted HR/event/follow-up inputs, Bayesian Poisson/log-link approach, GeMTC/R 3.4.1, and HR/95% CrI reporting | Matched. DOC-003 adds JAGS 4.3.0, chain counts, iterations, priors, and convergence threshold without contradicting the protocol. |
| XM-015 | DOC-002 p. 6 against DOC-003 pp. 4-6: DIC model-selection rule and every one of the 44 population-outcome rows | Forty-three selected models follow the printed displayed rule. The all-patient incident-cancer row does not at the displayed I2 precision; candidate CS-002. |
| XM-016 | DOC-002 p. 6 against DOC-003 pp. 4 and 22-26: additional frequentist analysis, aspirin/no-aspirin contrast, RR label, 95% CI label, and 11 forest-plot outcome blocks | Matched. All 130 printed study rows and 22 pooled fixed/random records were included in the identity/definition review; outcome-definition gaps explicitly printed in eTable 1 were not inferred. One ASCEND total-stroke use conflicts with the supplied definition map; candidate CS-004. |
| XM-017 | DOC-002 p. 6 against DOC-003 pp. 4 and 15: ARD calculation direction and all 44 eTable 3 ARD cells | All signs follow the printed convention (negative favors aspirin; positive favors no aspirin). The displayed scale needed to connect ARD to the 18 printed NNT/NNH values is not stated; candidate CS-006. |
| XM-018 | DOC-002 p. 6 against DOC-003 p. 18: dose, blinding, publication-year, and asymptomatic-PAD sensitivity scopes | The 4 column labels implement the 3 original exclusions plus the documented PAD addition. All 44 HR/CrI cells were checked for consistent effect-measure and interval labels. Cancer outcomes extend beyond the protocol's cardiovascular/bleeding wording but are explicitly labeled exploratory; no numeric conflict was assigned. |
| XM-019 | DOC-002 p. 7 against DOC-003 pp. 10-14: overall risk-of-bias rule against all 13 trial rows and 7 domains | The 4 high overall ratings correspond to a high blinding rating; the other 9 overall ratings are low, and no row has 3 unclear domains. Rule and table match. |
| XM-020 | DOC-002 p. 7 and DOC-003 pp. 10-14 against DOC-003 p. 20: requested tabular and graphical risk-of-bias summaries | Six of 7 graphical domain summaries reproduce the 13 categorical table rows. Detection bias does not; candidate CS-003. |
| XM-021 | DOC-002 p. 7 against DOC-003 pp. 9, 16, and 24: ASCEND stroke-definition change, eTable 1 outcome mapping, Bayesian total-stroke table, and frequentist total-stroke/ischemic-stroke plots | eTable 1 and eTable 4 consistently exclude ASCEND from total stroke, but the total-stroke forest plot includes its ischemic-stroke record; candidate CS-004. After ASCEND is removed, the 12 forest rows also differ from eTable 4 by 2 events in each arm; candidate CS-005. The separate planned primary-composite sensitivity result excluding ASCEND is not identifiable in the supplied supplement and is recorded as a limitation rather than a conflict. |
| XM-022 | DOC-003 pp. 3-4 against pp. 15-17: low-risk (<10%), high-risk (at least 10%), diabetes, and all-participant analysis sets | Group names and thresholds match. The stated WHS exclusion from high-risk event-rate calculations addresses its missing high-risk subgroup count. |
| XM-023 | DOC-003 pp. 5-6 against p. 16: selected models for total stroke in all, low-risk, high-risk, and diabetes populations | The model-selection rows are fixed, random, fixed, and fixed, respectively; eTable 4 uses the same population/outcome partitions and labels HR/95% CrI. No conflicting model label is printed. |
| XM-024 | DOC-003 pp. 15-16: all-patient total-stroke ARD -0.09 (-0.20 to 0.04) versus ARR 0.10 (-0.03 to 0.22) | Opposite signs are consistent with the distinct printed labels and directions: ARD is aspirin minus no aspirin, while ARR is consistent with no aspirin minus aspirin. The estimates also arise from differently labeled analyses. The unexplained ARR abbreviation is a clarity limitation, not a numeric candidate here. |
| XM-025 | DOC-003 pp. 7-9 against pp. 22-26: all 13 trial identities and 11 outcome-definition columns against the 130 displayed forest-plot study rows | Every displayed trial name was matched. “Not specified,” “not defined,” “not reported,” and blank definition cells constrain verification and were not filled by inference. Aside from the ASCEND total-stroke issue in CS-004, no direct definition conflict was established from supplied evidence. |
| XM-026 | DOC-003 p. 19: study-flow components across identification, deduplication, screening, exclusions, added articles, publications, and trials | 668 + 717 = 1,385; 1,385 - 235 = 1,150; the 8 exclusion categories sum to 1,131; 1,150 - 1,131 + 2 = 21 publications. The final 13-trial count is a different unit and is clearly labeled. No candidate. |
| XM-027 | DOC-003 p. 20: all 7 risk-of-bias graphical domains against eTable 2 | Sequence, attrition, and reporting are 13/13 low; allocation is 10 low/3 unclear; blinding and overall are 9 low/4 high. These 6 domains match. Detection is separately recorded in CS-003. |
| XM-028 | DOC-003 p. 21: funnel-plot primary-outcome points and printed Egger coefficient -0.47, SE 0.77, t=-0.59, P=.57 | Ten points are visibly distinguishable, but overlapping points cannot be excluded and no point coordinates are printed. No cross-location candidate was assigned from point count alone. |
| XM-029 | DOC-003 pp. 22-26: 11 outcome blocks, 130 study rows, fixed/random pooled results, totals, I2, tau-squared, and heterogeneity P values | Effect measure, arm direction, and printed precision are internally consistent across captions and blocks. Pooled fixed and random estimates are distinct model outputs, not duplicates. CS-004 is the sole outcome-definition conflict found in this vector. |
| XM-030 | DOC-001 versus DOC-002/DOC-003: every registered population/time/contrast/model/measure key | No truthful scientific match exists because the direct PDFs concern different studies and DOIs. Cross-paper numeric comparison would be invalid; the absence of a matching main aspirin article and of the STOP-PD II supplements limits package-level verification. |

## Provisional candidates

## CS-001 — HbA1c daily-rate effect is labeled in mg/dL while the paper's HbA1c table uses percent

- **Primary category:** Measure, label, or scale inconsistency.
- **Exact source locations:** [DOC-001 p. 1](../../../jama_flint_2019_oi_190079.pdf#page=1),
  [DOC-001 p. 7](../../../jama_flint_2019_oi_190079.pdf#page=7), and
  [DOC-001 p. 8](../../../jama_flint_2019_oi_190079.pdf#page=8).
- **Direct observation:** The abstract reports the HbA1c daily-rate contrast as `-0.0002 mg/dL`
  (95% CI, `-0.0021 to 0.0016`). The Results narrative repeats the same estimate, interval, and
  `mg/dL` unit. Table 4 labels HbA1c as `HbA1c, %` and reports baseline/termination values near
  5.7-5.9 on that percentage scale. The same abstract and Results passages use `mg/dL` appropriately
  for cholesterol, triglyceride, and glucose, making the HbA1c unit a specific printed label rather
  than a shared table heading.
- **Comparison logic:** A result for HbA1c must state the same measurement scale used for that outcome,
  unless an explicit conversion or alternate assay unit is supplied. No HbA1c conversion to mg/dL is
  given. The estimate's magnitude is compatible with a daily change in HbA1c percentage points, while
  `mg/dL` is the glucose/lipid concentration unit used in adjacent results.
- **Supported alternative:** The estimate and CI may be numerically correct with only the unit copied
  from an adjacent metabolic outcome. A different HbA1c scale is possible only if a definition absent
  from the supplied paper is intended.
- **Human verification:** Check the analysis output/data dictionary and the article's intended unit for
  the treatment-by-time HbA1c coefficient; determine whether both p. 1 and p. 7 should state percentage
  points per day rather than mg/dL.

## CS-002 — Printed model-selection rule and all-patient incident-cancer model disagree at I2 = 25%

- **Primary category:** Statistical reporting inconsistency.
- **Exact source locations:** [DOC-003 p. 4](../../../joi180151supp2_prod.pdf#page=4) and
  [DOC-003 p. 5](../../../joi180151supp2_prod.pdf#page=5).
- **Direct observation:** eMethods states that when fixed and random DIC values are within 3 units, a
  random-effects model is favored if fixed-effect `I2 >25%`. For all-patient incident cancer, eMethods
  3 prints fixed DIC `27.06`, random DIC `27.93`, `I2 = 25%`, and selected model `random`.
- **Comparison logic:** The DIC difference is `|27.93 - 27.06| = 0.87`, so the within-3 branch applies.
  At the displayed value, `25%` does not satisfy the printed strict inequality `>25%`; the rule would
  select fixed effects, yet the row says random. All other 43 rows were checked against the same rule
  and agree at displayed precision.
- **Supported alternative:** The model may have been selected using an unrounded I2 value slightly
  above 25%, while the table displays 25%. Alternatively, the intended threshold may have been
  `I2 >=25%`. Neither explanation is printed.
- **Human verification:** Inspect the unrounded fixed-effect I2 and the analysis code; confirm whether
  the inequality text or the selected-model cell should be revised.

## CS-003 — Detection-bias graph represents 9 low/4 unclear trials, while eTable 2 contains 8 low/5 unclear

- **Primary category:** Denominator, proportion, or total inconsistency.
- **Exact source locations:** eTable 2 on [DOC-003 p. 10](../../../joi180151supp2_prod.pdf#page=10),
  [p. 11](../../../joi180151supp2_prod.pdf#page=11),
  [p. 12](../../../joi180151supp2_prod.pdf#page=12),
  [p. 13](../../../joi180151supp2_prod.pdf#page=13), and
  [p. 14](../../../joi180151supp2_prod.pdf#page=14); eFigure 2 on
  [DOC-003 p. 20](../../../joi180151supp2_prod.pdf#page=20).
- **Direct observation:** The 13 detection-bias cells in eTable 2 are low for TPT, PPP, POPADAD, JPAD,
  AAA, JPPP, ARRIVE, and ASPREE (8 trials), and unclear for British Doctors' Study, Physicians' Health
  Study, HOT, WHS, and ASCEND (5 trials). eFigure 2 draws the detection-bias boundary at the same
  approximately 69% low/31% unclear position used for the 9/4 blinding split, rather than the
  approximately 62%/38% split implied by 8/5.
- **Comparison logic:** With 13 trials, the table implies `8/13 = 61.5%` low and `5/13 = 38.5%`
  unclear. The graph depicts approximately `9/13 = 69.2%` low and `4/13 = 30.8%` unclear. The other
  6 graph domains reconcile to the categorical table counts.
- **Supported alternative:** One detection-bias cell in the table may have been intended as low, or the
  graph may have been generated from an earlier classification set. The graph has no numeric labels,
  but its boundary is visually aligned with the exact 9/4 blinding and overall-risk boundaries.
- **Human verification:** Recompute the risk-of-bias graph directly from the 13 final categorical rows
  and identify which source (table or graphic) reflects the intended final assessment.

## CS-004 — ASCEND ischemic-stroke events are included in the total-stroke forest plot despite explicit exclusion from total stroke

- **Primary category:** Measure, label, or scale inconsistency.
- **Exact source locations:** eTable 1 on [DOC-003 p. 9](../../../joi180151supp2_prod.pdf#page=9),
  eTable 4 on [DOC-003 p. 16](../../../joi180151supp2_prod.pdf#page=16), and the total-stroke and
  ischemic-stroke forest plots on [DOC-003 p. 24](../../../joi180151supp2_prod.pdf#page=24). The
  protocol explanation is on [DOC-002 p. 7](../../../joi180151supp1_prod.pdf#page=7).
- **Direct observation:** eTable 1 states for ASCEND under all strokes: `Not included in analysis - only
  reports ischemic stroke`. eTable 4 consequently reports total stroke from 12 studies, with aspirin
  `1116/73,883` and no aspirin `1136/72,317`. The eFigure 4 total-stroke plot nevertheless contains an
  ASCEND row `240/7740` versus `263/7740`; the exact same ASCEND row is also included in the separate
  ischemic-stroke plot immediately below.
- **Comparison logic:** Adding the ASCEND denominators to eTable 4's 12-study denominators produces
  the 13-study total-stroke forest denominators exactly (`73,883 + 7,740 = 81,623` and
  `72,317 + 7,740 = 80,057`). Thus a measure explicitly classified as ischemic stroke is also labeled
  and pooled as total stroke in that forest plot, contrary to the supplied outcome-definition table
  and the 12-study total-stroke analysis. The separate event-total discrepancy after ASCEND removal is
  recorded in CS-005 rather than merged with this measure-definition issue.
- **Supported alternative:** The frequentist forest plot may have intentionally used a broader
  available-event convention than the Bayesian total-stroke analysis, but no such exception is stated
  in its caption. It may instead be a copied row or analysis-set error.
- **Human verification:** Check the frequentist analysis code and intended total-stroke dataset;
  determine whether ASCEND should be removed from the total-stroke forest plot or whether the outcome
  label/caption and definition table require qualification.

## CS-005 — Twelve non-ASCEND total-stroke forest rows do not reproduce eTable 4's event totals

- **Primary category:** Numeric or arithmetic inconsistency.
- **Exact source locations:** eTable 4 on
  [DOC-003 p. 16](../../../joi180151supp2_prod.pdf#page=16) and the total-stroke forest plot on
  [DOC-003 p. 24](../../../joi180151supp2_prod.pdf#page=24).
- **Direct observation:** eTable 4 reports 12 total-stroke studies with aspirin `1116/73,883` and no
  aspirin `1136/72,317`. The p. 24 forest plot contains the same 12 non-ASCEND study identities plus
  ASCEND. Summing the 12 non-ASCEND forest rows gives aspirin `1118/73,883` and no aspirin
  `1134/72,317`.
- **Comparison logic:** The participant totals match exactly, establishing the same 12-study analysis
  set at the displayed denominator level, but the event counts differ by 2 in opposite directions:
  forest minus eTable 4 is `+2` for aspirin and `-2` for no aspirin. The values do not reconcile by
  rounding because they are integer event counts.
- **Supported alternative:** The Bayesian table and frequentist forest plot may use different event
  adjudications or an unreported outcome-data revision despite identical study identities and
  denominators. No such distinction is supplied on either page.
- **Human verification:** Recompute the 12-study total-stroke event totals from the final analysis
  dataset and determine which two arm-specific counts belong in eTable 4 and the frequentist forest
  plot; document any legitimate analysis-set distinction.

## CS-006 — eTable 3 omits the ARD scale needed to reproduce its NNT and NNH values

- **Primary category:** Measure, label, or scale inconsistency.
- **Exact source locations:** protocol ARD rule on
  [DOC-002 p. 6](../../../joi180151supp1_prod.pdf#page=6), supplemental ARD/NNT method on
  [DOC-003 p. 4](../../../joi180151supp2_prod.pdf#page=4), and eTable 3 on
  [DOC-003 p. 15](../../../joi180151supp2_prod.pdf#page=15).
- **Direct observation:** The protocol and supplemental method define the ARD direction but do not
  state whether displayed ARDs are proportions or percentage points. eTable 3 likewise gives no unit.
  It prints, for example, all-patient composite ARD `-0.41` with NNT `242`, and all-patient major
  bleeding ARD `0.47` with NNH `210`.
- **Comparison logic:** Treating `0.41` as a unitless risk proportion gives a reciprocal near `2.44`,
  not `242`. Treating it as `0.41` percentage points gives `1/0.0041 = 243.9`, compatible with NNT 242
  after use of an unrounded ARD. Similarly, `0.47` percentage points gives `1/0.0047 = 212.8`, near
  NNH 210, whereas a proportion would give about 2.13. The 18 printed NNT/NNH values therefore imply a
  percentage-point scale that the table and methods never label.
- **Supported alternative:** The conventional intended presentation may be percentage points, with
  NNT/NNH calculated from unrounded estimates. If so, the calculations can be coherent; the candidate
  concerns the absent scale label, not a claim that the underlying NNT/NNH calculations are wrong.
- **Human verification:** Confirm the stored unrounded ARDs and add the intended unit or scaling rule
  (for example, percentage points) so that a reader can reproduce NNT/NNH without guessing a factor of
  100.

## Limitations and unresolved matchability

1. The package does not contain a main aspirin-meta-analysis article matching DOC-002/DOC-003, and it
   does not contain the STOP-PD II supplement referenced by DOC-001. Therefore abstract-to-supplement
   verification across the supplied document set is impossible; incompatible studies were not forced
   into numeric comparisons.
2. The planned sensitivity analysis excluding ASCEND from the primary composite is stated in DOC-002
   p. 7, but no clearly labeled result for that analysis is present in DOC-003. Absence of a result was
   not treated as a quantitative inconsistency.
3. Several eTable 1 definitions are explicitly absent or unspecified. Forest-plot rows using those
   outcomes were checked for identity and printed values, but a definition-level match cannot be
   asserted beyond the supplied text.
4. eFigure 2 has an axis but no numeric percentage labels; CS-003 uses exact table counts and the
   graph's boundary alignment with other exact 9/4 domains. eFigure 3 has no point coordinates, so
   visually overlapping studies cannot be excluded.
5. eTable 4's `ARR` abbreviation is not expanded. Its sign is consistent with risk reduction and is
   opposite to the explicitly directed ARD in eTable 3, so it was not treated as a numeric conflict.

## Completion counts

- Direct sources covered: 3/3 PDFs, 46/46 pages through the complete evidence maps and targeted direct
  page confirmation.
- DOC-001 internal matched relationship groups checked: 11.
- DOC-002-to-DOC-003 matched relationship groups checked: 18.
- DIC/model-selection rows checked: 44/44 (43 no-candidate; 1 candidate).
- Risk-of-bias table rows/domains checked: 13 trials x 7 domains; graphical domains checked: 7/7
  (6 no-candidate; 1 candidate).
- ARD cells checked: 44/44; NNT/NNH entries checked: 18/18.
- Sensitivity HR/CrI cells checked: 44/44.
- Frequentist forest-plot outcome blocks checked: 11/11; study rows checked: 130/130; pooled
  fixed/random records checked: 22/22.
- Provisional candidates emitted: 6 (`CS-001` through `CS-006`).
- Unreviewed assigned matched units: 0.
