# Cross-source consistency review

## Scope and method

This checker completed the cross-source lane over the frozen mapping inventories: numeric/reporting `N001`-`N054` and inferential/statistical `S001`-`S038`. It used only the freshly prepared native/layout page assets and the supplied direct PDFs. It did not use prior audit products as evidence.

For each possible recurrence, I first matched the study population, time point, intervention/reference contrast, analysis set, outcome definition, estimator/test, unit/scale, and displayed precision. A difference was recorded below only when those dimensions supported a reproducible unresolved mismatch. Every observation is provisional; no stable `C` identifier or adjudication is assigned here.

## Complete matching coverage

| Cross-source group | Assigned canonical relationships checked | Matched-source coverage and outcome |
|---|---|---|
| Main article: population, allocation, flow, baseline, definitions, and conclusions | N001-N017, N024-N032; S001-S005, S020-S021 | Checked abstract, methods, Figure 1, Table 1, narrative, figures/captions, and conclusion. The 778 randomized/776 analysed-completed distinction, 388-per-analysis-arm denominators, and baseline occurrences were matched by analysis set. Figure 2's log-rank P=.85 and Table 2/Cox P=.94 are different stated tests, so are not treated as a numerical conflict. Figure 3 interaction P values are subgroup-interaction tests, not the Table 2 overall P values. No additional qualifying observation. |
| Main primary mortality result | N018, N021, N029; S003, S006, S009, S011, S014 | Abstract, Table 2, results narrative, Figure 2, and Figure 3 were matched as day-28 all-cause mortality in 388 versus 388 analysed patients. Counts, percentages, risk difference, and Table 2/narrative HR agree. The Figure 3 overall HR/reference-direction display is separately recorded as XC003. |
| Main IMV result | N019, N030; S004, S007, S015 | Abstract, Table 2, narrative, Figure 3, and Supplement 2 eFigure 1 were matched as IMV by day 28 in 388 versus 388 analysed patients, allowing for the competing-risk model. Counts, percentages, risk difference, and the Table 2/narrative cause-specific HR agree. The eFigure test label and Figure 3 overall HR/reference-direction display are separately recorded as XC002 and XC004. |
| Main secondary/post-hoc outcomes | N020, N022-N028; S008, S010, S012-S019 | Abstract, Table 2, narrative, eTable, eFigures 2-3, and captions were checked. ICU infection, lengths of stay, PaO2/FiO2, comfort/dyspnea, post-hoc outcomes, and risk-set displays are either matched after their time point/measure is aligned or graphical only. The matched six-hour respiratory-rate CI has an unexplained printed upper-endpoint difference, recorded as XC001. |
| Initial protocol / original plan | N033-N040; S022-S029 | Checked protocol abstract, detailed protocol, and original statistical-plan pages. The non-inferiority design, 816 planned participants, 26% control assumption, 9% margin, different endpoints, and no-interim rule are version-specific planned material. The main article explicitly says this initial grant protocol changed to a revised superiority protocol; these are not contradictions with the report. The internally juxtaposed wording that patient-level impact is assessed while the randomisation unit is called the centre has no direct reported numeric/statistic comparator and is out of scope under the analysis-unit boundary. |
| Final/published protocol and reported main result | N041-N047; S030-S034 | Checked final patient-information and published-protocol definitions, planned sample size, eligibility, intervention, randomisation, infection definition, and interim rule against the reported trial. Planned-versus-realised centre count and planned thresholds were not equated with realised results. The revised-superiority planning total is nevertheless directly matched across sources: the main prints 779 while the published protocol prints 778 with 389 per arm; this is recorded as XC005. |
| Results supplement | N048-N053; S035-S037 | Checked eTable and all three eFigures against their main-article recurrences. eTable six-hour medians and counts agree with the narrative at the same time point; eFigure 2/3 risk sets are outcome-specific available populations and were not cross-added. eFigure 1's numerical P=.17 matches the main IMV P=.17 at displayed precision, but its printed log-rank label conflicts with the main specified Gray comparison; recorded as XC002. |
| Data-sharing statement and external/preliminary literature context | N040, N054; S038 | Checked as supplied context only. External/preliminary values and the data-availability statement are not current HIGH trial results and have no matched reported-result comparator. No qualifying observation. |

## Explicit nonmatches not registered

- The initial non-inferiority plan (816 participants, 26% control mortality, 9% margin, 80% power, no interim analysis) and the revised/published superiority plan (778 participants, 30% versus 20%, 90% power, one interim) are document-version-specific. The main article expressly describes that change; they were not treated as contradictions.
- The main article's Figure 2 log-rank P=.85 and the mortality Cox/Table 2 P=.94 are different displayed inferential procedures for the same mortality curve/result and have no claim that they must be identical.
- The Figure 3 subgroup interaction P values are Gail-Simon interaction tests, not treatment-effect P values. Their numerical difference from Table 2 overall outcome P values is expected from their different questions.
- The eFigure 2 and eFigure 3 risk-set counts differ across panels at a shared displayed time because they belong to different measured outcomes and available-case populations; they are not common denominators.
- The protocol phrase calling the centre the randomisation unit is preserved as a source wording issue, but no supplied reported numeric result, denominator, or inferential statistic is tied to a centre-randomised analysis. It is therefore not registered as a cross-source quantitative candidate in this lane.

## Provisional qualifying observations

## XC001 — Respiratory-rate 95% CI upper endpoint differs between matched abstract and results narrative

- **Status:** Pending Human Adjudication
- **Category:** Cross-document numeric inconsistency
- **Exact source locations:** [DOC-001 abstract, PDF p. 1](../../../jama_azoulay_2018_oi_180109.pdf#page=1); [DOC-001 results narrative, PDF p. 6](../../../jama_azoulay_2018_oi_180109.pdf#page=6).
- **Matching dimensions / identity rule:** Adult immunocompromised HIGH participants; high-flow versus standard oxygen; respiratory rate at 6 hours after randomisation; displayed mean difference in breaths/min with a 95% CI. The locations print the same group values (25/min versus 26/min) and the same point estimate (−1.8/min), so their one-decimal CI endpoints should reproduce the same matched displayed interval unless a separately defined analysis or rounding basis is documented.
- **Direct observation:** The abstract prints `−1.8/min [95% CI, −3.2 to −0.2]`. The results narrative prints `mean difference, −1.8 [95% CI, −3.2 to −0.3]` for the same stated six-hour comparison.
- **Comparison logic:** Population, time, contrast, outcome, unit, point estimate, and CI confidence level align; the upper endpoint differs by 0.1/min at the same displayed precision.
- **Supported alternative source-grounded interpretation:** The two statements could have been rounded from separately calculated or separately rounded underlying estimates, but neither location identifies a distinct model, analysis set, or rounding convention.
- **Human verification question:** Which 95% CI endpoint was generated for the prespecified six-hour respiratory-rate comparison, and does a source analysis table/document a different calculation or rounding rule for the abstract versus narrative?

## XC002 — IMV cumulative-incidence comparison is labelled Gray test in the main article but log-rank test in the matched supplement figure

- **Status:** Pending Human Adjudication
- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** [DOC-001 statistical methods, PDF p. 4](../../../jama_azoulay_2018_oi_180109.pdf#page=4); [DOC-001 IMV results narrative, PDF p. 6](../../../jama_azoulay_2018_oi_180109.pdf#page=6); [DOC-003 eFigure 1, PDF p. 3](../../../joi180109supp2_prod.pdf#page=3).
- **Matching dimensions / identity rule:** HIGH analysed population; high-flow versus standard oxygen; invasive mechanical ventilation by day 28/cumulative incidence; death without IMV is stated as the competing risk. A figure reporting the matched cumulative-incidence comparison should carry a test label compatible with the stated comparison procedure or identify a distinct test.
- **Direct observation:** The main methods state that IMV cumulative incidence with death without IMV as a competing risk was compared using the `Gray test`. The main narrative directs the reader to eFigure 1 for the cumulative incidence and reports 150/388 versus 170/388, cause-specific HR 0.85 (95% CI, 0.68 to 1.06), `P = .17`. The eFigure is titled `Cumulative Incidence of Mechanical Ventilation` for the two HIGH groups and prints `P (log Rank test) = 0.17`.
- **Comparison logic:** The same outcome, population, contrast, event horizon, figure linkage, and displayed P value are aligned, while the source labels the corresponding comparison as Gray versus log-rank. These are distinct named tests, particularly in the presence of the expressly stated competing risk.
- **Supported alternative source-grounded interpretation:** The eFigure's log-rank P could represent a separately performed test that happens to round to .17, while the main textual P could accompany the cause-specific Cox result; neither source supplies a separate numerical P or clearly distinguishes the figure test from the stated cumulative-incidence comparison.
- **Human verification question:** Was eFigure 1 generated with a log-rank test, a Gray test, or both, and which test does each printed P=.17 refer to?

## XC003 — Day-28 mortality overall hazard ratio in Figure 3 is the reciprocal of the Table 2/narrative HR despite the figure's stated favour-direction labels

- **Status:** Pending Human Adjudication
- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** [DOC-001 Table 2, PDF p. 5](../../../jama_azoulay_2018_oi_180109.pdf#page=5); [DOC-001 primary-outcome narrative, PDF p. 5](../../../jama_azoulay_2018_oi_180109.pdf#page=5); [DOC-001 Figure 3A, PDF p. 7](../../../jama_azoulay_2018_oi_180109.pdf#page=7).
- **Matching dimensions / identity rule:** All analysed HIGH patients; all-cause day-28 mortality; 138/388 high-flow versus 140/388 standard; univariable Cox hazard ratio. Figure 3A labels the left side of its HR axis `Favors High-Flow Nasal Oxygen Therapy` and the right side `Favors Standard Oxygen Therapy`. Under that displayed direction, the all-patient HR must use the same treatment/reference orientation as Table 2's high-flow-versus-standard HR, or the figure must state an opposite reference and reverse/clarify its favour labels.
- **Direct observation:** Table 2 and the primary-outcome narrative print `HR, 0.98 (0.77 to 1.24)` for the 138/388 versus 140/388 result. Figure 3A prints the identical event counts but `1.02 (0.81-1.29)` in its all-patients row, under the stated favour-direction headers.
- **Comparison logic:** 1/0.98 = 1.0204; 1/1.24 = 0.8065 and 1/0.77 = 1.2987, which round to Figure 3A's `1.02 (0.81-1.29)`. Thus the numerical figure value is the reciprocal orientation of the Table 2/narrative value. The figure's printed left/right favour labels do not document that opposite orientation.
- **Supported alternative source-grounded interpretation:** Figure 3A may intentionally use standard-oxygen relative to high-flow as its HR orientation. If so, the supplied figure does not make that reference orientation explicit and its `Favors High-Flow`/`Favors Standard` headers require confirmation against that convention.
- **Human verification question:** What numerator/reference group was used for Figure 3A HRs, and should its favour-direction headers or HR orientation be amended to make it consistent with Table 2 and the narrative?

## XC004 — IMV overall hazard ratio in Figure 3 is the reciprocal of the Table 2/narrative cause-specific HR despite the figure's stated favour-direction labels

- **Status:** Pending Human Adjudication
- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** [DOC-001 Table 2, PDF p. 5](../../../jama_azoulay_2018_oi_180109.pdf#page=5); [DOC-001 IMV results narrative, PDF p. 6](../../../jama_azoulay_2018_oi_180109.pdf#page=6); [DOC-001 Figure 3B, PDF p. 7](../../../jama_azoulay_2018_oi_180109.pdf#page=7).
- **Matching dimensions / identity rule:** All analysed HIGH patients; invasive mechanical ventilation by day 28; 150/388 high-flow versus 170/388 standard; competing-risk outcome with a cause-specific Cox HR. Figure 3B uses the same `Favors High-Flow Nasal Oxygen Therapy` at left and `Favors Standard Oxygen Therapy` at right as Figure 3A. A directly matched all-patient HR must identify a different reference orientation if it is the reciprocal of the Table 2/narrative cause-specific HR.
- **Direct observation:** Table 2 and the IMV narrative print `cause-specific HR, 0.85 (0.68 to 1.06)` for 150/388 versus 170/388. Figure 3B prints those same all-patient counts but `1.17 (0.94-1.46)` under its stated favour-direction headers.
- **Comparison logic:** 1/0.85 = 1.1765; 1/1.06 = 0.9434 and 1/0.68 = 1.4706, which correspond to Figure 3B's printed `1.17 (0.94-1.46)` after displayed rounding. The matching values therefore use reciprocal orientations, but the figure does not identify an opposite reference group or reconcile it with its favour-direction labels.
- **Supported alternative source-grounded interpretation:** As for mortality, Figure 3B may intentionally calculate standard-oxygen relative to high-flow. That could explain the reciprocal numerical value, but the source does not explicitly state this reference direction and the favour labels need confirmation.
- **Human verification question:** What numerator/reference group was used for the Figure 3B cause-specific HRs, and are its direction labels and all-patient value correctly aligned with the Table 2/narrative convention?

## XC005 — Revised-superiority planned total is printed as 779 in the main article but 778 in the matched published protocol

- **Status:** Pending Human Adjudication
- **Category:** Cross-document numeric inconsistency
- **Exact source locations:** [DOC-001 statistical analysis, PDF p. 3](../../../jama_azoulay_2018_oi_180109.pdf#page=3); [DOC-002 published protocol, PDF p. 90](../../../joi180109supp1_prod.pdf#page=90); [DOC-002 published statistical plan, PDF p. 103](../../../joi180109supp1_prod.pdf#page=103).
- **Matching dimensions / identity rule:** Revised superiority HIGH design; day-28 mortality; anticipated 30% standard versus 20% high-flow mortality; alpha 5%; 90% power; 389 planned participants per group. With the same two-arm planned allocation printed in all matched sources, total planned N must equal 389 + 389 = 778.
- **Direct observation:** The main article states that `779 patients (389 in each group)` were required. The published protocol describes the superiority design and gives 389 patients per group, and its statistical-plan section states `we need 778 patients (389 in each group)`.
- **Comparison logic:** The assumptions, design version, allocation, and group sizes match. The main total differs from the published-protocol total by one and does not equal its own displayed group-size sum; 389 + 389 = 778.
- **Supported alternative source-grounded interpretation:** The `779` may be a main-article transcription/typographical value, potentially influenced by a calculation before equal arm allocation, but no supplied source defines an additional participant or unequal allocation that would reconcile 779 with `389 in each group`.
- **Human verification question:** What was the final sample-size-calculation total for the revised superiority protocol, and should the main article's `779` be corrected or explained relative to the two printed 389-patient arms?

## Lane summary and limitations

- **Assigned relationships checked:** 54 numeric/reporting records and 38 inferential/statistical records; all 92 were reviewed for cross-source matching where a comparator existed.
- **Provisional qualifying observations:** 5 (`XC001`-`XC005`), each `Pending Human Adjudication`.
- **Limitations:** The supplied package has no patient-level data or analysis code. Figure plots supply labels, displayed counts, and values but not underlying data. Where two different named tests or document versions plausibly explain a numerical difference, that difference was not registered unless the labels/values themselves remained unresolved as described above.
