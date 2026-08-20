# Mechanical Evidence Recheck

This recheck covers every stable candidate ID in `candidate_ledger.md`: C001, C002, C003, C004, C005, C006, C007, and C008. Every cited physical PDF page was inspected directly using targeted CPU-only native/layout extraction and a fresh 200-dpi page render. Reusable text and page artifacts were used only as locators. The source PDFs were not modified. Every candidate remains **Pending Human Adjudication**.

## C001 — Shared-placebo race missingness does not reconcile with the printed denominator

- **Status:** Pending Human Adjudication.
- **Cited location found:** [DOC-001 Table 1 and footnotes a-b — PDF p. 6](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=6>) contains the shared-placebo column, all printed race rows, and the missing-race footnote.
- **Source value/text matched:** The shared-placebo header is `n = 164`. The race rows print Asian `2/160 (1.2)`, Black or African American `6/160 (3.8)`, White `151/160 (94.4)`, and multiple races `1/160 (0.6)`. Footnote b says, “Race was unknown or unreported for 3 participants.”
- **Comparator matched:** The denominator and footnote apply to the same shared-placebo column; footnote a defines that group as regimen-specific placebo plus shared placebos from other regimens.
- **Consistency rule applicable:** The number without a displayed race classification equals the group total minus the number classified when the rows are exhaustive for that display. Counts have no rounding tolerance.
- **Calculation or logical comparison reproduced:** `2 + 6 + 151 + 1 = 160`; `164 - 160 = 4`; and `4 - 3 = 1`. Thus the displayed denominator implies four participants without a displayed race classification, whereas the footnote names three unknown or unreported participants.
- **Necessary inputs available:** The group total, four race numerators, common race denominator, and footnote count are all printed.
- **Exact missing inputs or definitions:** The source does not provide participant-level race statuses, an omitted zero or nonzero race category, a reason for excluding one participant from the denominator beyond “unknown or unreported,” or a separate subset definition for footnote b.
- **Source-grounded alternative interpretation:** The denominator 160 may represent a complete-case subset that excludes one additional status not considered “unknown or unreported,” or one denominator, numerator, or footnote count may be a production error. No such distinction is printed.
- **Direct observation:** The printed group total, common denominator, category sum, and footnote count differ by one participant under the displayed identity.
- **Inferred explanation:** An omitted category, differently defined exclusion, denominator error, numerator error, or footnote error is possible, but the supplied page does not identify which explanation applies.
- **Exact remaining human question:** Do four shared-placebo participants lack a displayed race classification, or does one participant have a separately defined status that should reconcile the printed denominator of 160 with footnote b's count of 3?

## C002 — SVC values have incompatible monthly-rate and 24-week-change labels

- **Status:** Pending Human Adjudication.
- **Cited location found:** [DOC-001 Secondary Efficacy Outcomes — PDF p. 4](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4>) and [DOC-004 eTable 3A — PDF p. 16](<../../../joi240158supp3_prod_1742927563.7911.pdf#page=16>) contain the cited SVC estimates and labels.
- **Source value/text matched:** The article calls the mean change in SVC “over 24 weeks” `-9.32 PPN per month` for pooled CNM-Au8 and `-8.53 PPN per month` for shared placebo, with difference `-0.78 PPN/month` and 95% CI `-4.25 to 2.68`. eTable 3A prints SVC `(% predicted)` under `24-week Change Estimate` with the same values `-9.32`, `-8.53`, and `-0.78`, and the same CI.
- **Comparator matched:** Both locations identify pooled CNM-Au8 `n=120` versus shared placebo `n=164`, the 24-week SVC outcome, and the same estimate, contrast, interval, and cited supplemental table.
- **Consistency rule applicable:** A cumulative 24-week change and a change rate per month are different time scales and cannot carry the same numeric value without a stated conversion or estimand convention.
- **Calculation or logical comparison reproduced:** Using the ledger's explicit diagnostic convention of `4.345 weeks/month`, 24 weeks is `24 / 4.345 = 5.52` months. A rate of `-9.32 PPN/month` implies about `-9.32 x 5.52 = -51.4 PPN` over 24 weeks; a total change of `-9.32 PPN` over 24 weeks implies about `-9.32 / 5.52 = -1.69 PPN/month`. The same-scale labels therefore do not reconcile by rounding.
- **Necessary inputs available:** The time horizon, repeated values, populations, endpoint label, difference, interval, and the article's monthly unit are printed.
- **Exact missing inputs or definitions:** The sources do not define whether the model estimand is a week-24 cumulative change, a monthly slope, or another parameter; they also do not supply a month-length conversion convention or explain why eTable 3A's `24-week Change Estimate` would contain monthly rates.
- **Source-grounded alternative interpretation:** “Per month” may be an editorial unit attached to values intended as week-24 changes, or the eTable heading may omit an intended rate convention. The source supplies no conversion that selects either interpretation.
- **Direct observation:** Identical numeric estimates appear with a monthly-rate label in the article and a 24-week-change label in eTable 3A.
- **Inferred explanation:** A label-production error or an unreported estimand convention is possible; the diagnostic conversion does not establish which label was intended.
- **Exact remaining human question:** Are `-9.32`, `-8.53`, and `-0.78` monthly rates in PPN or cumulative 24-week changes in percent-predicted SVC, and what model definition should govern both displays?

## C003 — Shared-placebo ALSFRS-R credible-interval endpoints differ for the cited primary model

- **Status:** Pending Human Adjudication.
- **Cited location found:** [DOC-001 Primary Efficacy Outcome — PDF p. 4](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4>) and [DOC-004 eTable 2 — PDF p. 15](<../../../joi240158supp3_prod_1742927563.7911.pdf#page=15>) contain the shared-placebo ALSFRS-R slope and 95% credible interval.
- **Source value/text matched:** The article prints `-1.03 points per month` with 95% CrI `-1.176 to -0.892`. eTable 2 prints median and mean `-1.03` for `Regimen C placebo w/ sharing`, with 95% CrI `(-1.181, -0.894)`.
- **Comparator matched:** The article explicitly cites eTable 2; both locations name the primary Bayesian shared-parameter model, ALSFRS-R slope in points per month, and the shared-placebo component.
- **Consistency rule applicable:** A repeated estimate for the same model component should reproduce the same credible-interval endpoints at the same three-decimal precision unless a distinct analysis is identified.
- **Calculation or logical comparison reproduced:** Lower endpoints differ by `|-1.176 - (-1.181)| = 0.005`; upper endpoints differ by `|-0.892 - (-0.894)| = 0.002`. The point estimate remains `-1.03` in both locations.
- **Necessary inputs available:** Both interval endpoint pairs, the point estimate, group, unit, model name, and cross-reference are printed.
- **Exact missing inputs or definitions:** The supplied pages do not include posterior draws, unrounded quantiles, software output, analysis date, data lock, or a model-version identifier that could distinguish the two interval pairs.
- **Source-grounded alternative interpretation:** The pages may reflect different posterior runs or production versions with an unchanged rounded slope, but neither page labels such a distinction.
- **Direct observation:** Both three-decimal interval endpoints differ across the matched displays.
- **Inferred explanation:** A different model run, data cut, posterior summary, or transcription is possible but not established by the supplied sources.
- **Exact remaining human question:** Which posterior run and unrounded 95% credible interval is authoritative for the shared-placebo ALSFRS-R slope in the primary Bayesian model?

## C004 — Pooled-active ALSFRS-R credible-interval endpoints differ for the cited primary model

- **Status:** Pending Human Adjudication.
- **Cited location found:** [DOC-001 Primary Efficacy Outcome — PDF p. 4](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4>) and [DOC-004 eTable 2 — PDF p. 15](<../../../joi240158supp3_prod_1742927563.7911.pdf#page=15>) contain the pooled-active ALSFRS-R slope and 95% credible interval.
- **Source value/text matched:** The article prints `-1.00 points per month` with 95% CrI `-1.153 to -0.858` for the combined 30-mg and 60-mg CNM-Au8 groups. eTable 2 prints median and mean `-1.00` for `Pooled CNM-Au8`, with 95% CrI `(-1.143, -0.847)`.
- **Comparator matched:** The article cites eTable 2; both locations identify the pooled CNM-Au8 component of the primary Bayesian shared-parameter model and use the same unit.
- **Consistency rule applicable:** The same model component repeated to three-decimal interval precision should have the same endpoints unless a distinct analysis is identified.
- **Calculation or logical comparison reproduced:** Lower endpoints differ by `|-1.153 - (-1.143)| = 0.010`; upper endpoints differ by `|-0.858 - (-0.847)| = 0.011`. The point estimate remains `-1.00` in both locations.
- **Necessary inputs available:** Both endpoint pairs, the common point estimate, pooled group, unit, model name, and article-to-table citation are printed.
- **Exact missing inputs or definitions:** Posterior draws, unrounded quantiles, analysis version, run date, data lock, and production history are absent.
- **Source-grounded alternative interpretation:** An undocumented posterior rerun or production update could retain the rounded point estimate while changing interval endpoints; the pages do not identify one.
- **Direct observation:** The matched pooled-active intervals differ at both printed endpoints.
- **Inferred explanation:** A model-run difference or transcription is possible but cannot be selected from the supplied evidence.
- **Exact remaining human question:** Which posterior output and unrounded 95% credible interval should be used for pooled CNM-Au8 in the primary Bayesian shared-parameter model?

## C005 — Bayesian mortality event rates differ between article text and cited eTable 2

- **Status:** Pending Human Adjudication.
- **Cited location found:** [DOC-001 Primary Efficacy Outcome — PDF p. 4](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4>) and [DOC-004 eTable 2 — PDF p. 15](<../../../joi240158supp3_prod_1742927563.7911.pdf#page=15>) contain the model-estimated mortality event rates.
- **Source value/text matched:** The article prints `0.007 events per month` for shared placebo and `0.006 events per month` for combined CNM-Au8. eTable 2 prints median and mean `0.010` for shared placebo and `0.009` for pooled CNM-Au8 under `Mortality Event Rate (events per month)`.
- **Comparator matched:** The article explicitly attributes these rates to the Bayesian shared-parameter model and cites eTable 2; group, measure label, and monthly unit match.
- **Consistency rule applicable:** Repetitions of the same model component and unit should have the same displayed rate unless a different event definition, posterior summary, or analysis is labelled.
- **Calculation or logical comparison reproduced:** `0.010 - 0.007 = 0.003 events/month` for shared placebo and `0.009 - 0.006 = 0.003 events/month` for pooled active. The displayed three-decimal pairs cannot be one value under a common deterministic rounding convention.
- **Necessary inputs available:** Both rate pairs, group labels, monthly unit, model name, and direct cross-reference are printed.
- **Exact missing inputs or definitions:** The sources do not supply unrounded posterior rates, the event variable used in each output, posterior-summary selection, model version, analysis date, or a statement distinguishing mortality alone from a death/PAV composite within this model component.
- **Source-grounded alternative interpretation:** One display may use another posterior run, summary, or event definition, but neither page labels an alternate analysis or time scale.
- **Direct observation:** Each matched group differs by `0.003 events/month` across the article and eTable 2.
- **Inferred explanation:** A changed model run, event definition, data cut, or transcription is possible but not demonstrated.
- **Exact remaining human question:** Do the article and eTable 2 intentionally use different event definitions or Bayesian outputs, and which unrounded monthly rates apply to the primary shared-parameter model?

## C006 — Plasma NfL confidence intervals differ across Figure 3, narrative, and eTable 3B

- **Status:** Pending Human Adjudication.
- **Cited location found:** [DOC-001 Figure 3A and Biomarker Analyses — PDF p. 8](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=8>) and [DOC-004 eTable 3B — PDF p. 17](<../../../joi240158supp3_prod_1742927563.7911.pdf#page=17>) contain all three interval displays.
- **Source value/text matched:** Figure 3A prints `-9.5%` with 95% CI `-17.8% to -0.5%` and `P = .04`. The article narrative prints `-9.5%` with 95% CI `-17.8 to -0.4%` and `P = .04`. eTable 3B prints `-9.5`, 95% CI `-18.0, 0`, and `P = 0.04` for plasma NfL percentage change.
- **Comparator matched:** All displays concern pooled CNM-Au8 versus regimen placebo at week 24; the article and eTable also repeat active `-2.3%` and placebo `+7.9%`, and all three repeat the point estimate and P value.
- **Consistency rule applicable:** A repeated interval for the same outcome, time point, population, contrast, and confidence level should reproduce the same endpoints unless a distinct analysis or display-precision rule is identified.
- **Calculation or logical comparison reproduced:** Figure versus narrative upper endpoints differ by `0.1` percentage point. eTable versus Figure differs by `0.2` at the lower endpoint and `0.5` at the upper endpoint; eTable versus narrative differs by `0.2` and `0.4`. The eTable's displayed upper endpoint is the null value `0`, whereas both article endpoints are below zero.
- **Necessary inputs available:** The point estimate, three endpoint pairs, confidence level, P values, arm changes, populations, time point, and log-transform/back-transformation note are printed.
- **Exact missing inputs or definitions:** The unrounded interval endpoints, interval-construction method, output version, table-specific rounding convention, and analysis-run identifiers are absent.
- **Source-grounded alternative interpretation:** eTable 3B may round an unrounded negative endpoint to `0` at coarser precision, and Figure 3 and the prose may have been rounded or transcribed independently. A distinct run is also possible. None is labelled.
- **Direct observation:** The same point estimate and P value are accompanied by three different printed 95% confidence intervals.
- **Inferred explanation:** Independent rounding, production transcription, or an alternate analysis run could explain the differences; the supplied sources do not identify the mechanism. The displayed `0` is not treated as a separate P/CI contradiction because its unrounded value and table precision are unavailable.
- **Exact remaining human question:** What unrounded plasma-NfL confidence interval underlies Figure 3A, the article narrative, and eTable 3B, and were these intended as one output or as separately labelled analyses?

## C007 — Serum NfL regimen-only values and contrast do not reconcile across displays

- **Status:** Pending Human Adjudication.
- **Cited location found:** [DOC-001 Figure 3B and Biomarker Analyses — PDF p. 8](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=8>) and [DOC-004 eTable 3B — PDF p. 17](<../../../joi240158supp3_prod_1742927563.7911.pdf#page=17>) contain the serum-NfL arm changes, contrast, interval, and P value.
- **Source value/text matched:** The article prints regimen placebo `+30.8%`, pooled CNM-Au8 `+0.4%`, and treatment difference `-23.2%` with 95% CI `-39.5% to -2.5%` and `P = .03`. eTable 3B prints regimen placebo `+26.8%`, pooled CNM-Au8 `+0.4%`, and difference `-26.4%` with 95% CI `-50.3% to -2.6%` and `P = 0.03`.
- **Comparator matched:** Both displays identify serum NfL percentage change at week 24, pooled CNM-Au8 `n=120` versus regimen placebo `n=41`, and a log-transformed model back-transformed to the original scale; both print the same active value and P value.
- **Consistency rule applicable:** Matched repetitions of one regimen-only model result should agree in arm changes, treatment contrast, and interval unless the source labels different model runs, populations, processing rules, or contrast definitions. For back-transformed log models, a ratio-based contrast and a simple percentage-point subtraction are not interchangeable.
- **Calculation or logical comparison reproduced:** Across sources, placebo change differs by `30.8 - 26.8 = 4.0` percentage points and the treatment contrast differs by `|-23.2 - (-26.4)| = 3.2` points. The article values reproduce a geometric-mean-ratio contrast: `[(1 + 0.004) / (1 + 0.308) - 1] x 100 = -23.24%`, which rounds to `-23.2%`. In eTable 3B, simple subtraction gives `0.4 - 26.8 = -26.4` points, while the analogous ratio calculation gives `[(1.004 / 1.268) - 1] x 100 = -20.8%`, not `-26.4%`. These are diagnostics using rounded marginal changes, not substitutes for the fitted-model contrast.
- **Necessary inputs available:** Both rounded arm changes, contrasts, intervals, P values, populations, time point, and the source's log-transform/back-transformation statement are printed.
- **Exact missing inputs or definitions:** The source does not provide unrounded least-squares means, covariance information, model coefficients, exact contrast formula, specimen inclusion, plate-handling rule, outlier rule, model version, or analysis date for each display.
- **Source-grounded alternative interpretation:** The article's `-23.2%` can be read as a ratio of geometric mean changes rather than crude subtraction, so `0.4 - 30.8 = -30.4` is not the only applicable internal rule. eTable 3B may instead print a percentage-point difference, or one display may come from another insufficiently labelled ERO run. The source does not explain why the two displays use different placebo changes, contrast values, and intervals.
- **Direct observation:** Placebo change, treatment contrast, and both interval endpoints differ between the matched displays; active change and P value agree.
- **Inferred explanation:** Different contrast scales, plate/sample processing, model runs, populations, or production versions are possible, but none is identified on the cited pages.
- **Exact remaining human question:** Which regimen-only serum-NfL output is intended, what exact back-transformed contrast formula and analysis population produced it, and why do Figure 3/article text and eTable 3B print different placebo changes, contrasts, and intervals?

## C008 — Discussion total of 13 events conflicts with the 14 events displayed in Table 2

- **Status:** Pending Human Adjudication.
- **Cited location found:** [DOC-001 Table 2 — PDF p. 7](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=7>) and [DOC-001 Discussion — PDF p. 9](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=9>) contain the event counts and narrative total.
- **Source value/text matched:** Table 2 reports `5/120` for pooled CNM-Au8 and `9/162` for shared placebo in the PAV-free survival comparison. The Discussion states “a total of 13 events in the RCT period in the shared placebo group and the combined CNM-Au8 groups.”
- **Comparator matched:** The Discussion names the shared-placebo and combined CNM-Au8 groups used in Table 2's pooled-active comparison and discusses the same RCT-period exploratory survival analysis. Table 2 and Figure 2 define the displayed events as death or PAV; the Discussion uses only the word “events.”
- **Consistency rule applicable:** If the Discussion total uses Table 2's death/PAV endpoint, populations, and RCT-period cutoff, the total must equal the two mutually exclusive group event counts.
- **Calculation or logical comparison reproduced:** `5 + 9 = 14`, which differs from the narrative total of 13 by one event.
- **Necessary inputs available:** The two group numerators, denominators, Table 2 endpoint label, Discussion populations, and narrative total are printed.
- **Exact missing inputs or definitions:** The Discussion does not define “events,” list the 13 events, specify an alternative cutoff, or state whether one death/PAV event is excluded. The participant-level event list and exact event dates are not supplied.
- **Source-grounded alternative interpretation:** The Discussion may use a narrower event definition, a different cutoff, or a subset that excludes one Table 2 event. It does not state such a distinction.
- **Direct observation:** The two Table 2 numerators sum to 14, while the Discussion prints 13 for the named groups.
- **Inferred explanation:** An alternate definition, cutoff, exclusion, or transcription could account for one event, but the supplied article does not establish which.
- **Exact remaining human question:** Which participant-level event list, death/PAV definition, and RCT cutoff underlie the Discussion total of 13, and does that total intentionally exclude one of the 14 events counted in Table 2?

## Recheck scope summary

- Stable IDs covered: C001, C002, C003, C004, C005, C006, C007, C008.
- Direct PDF pages inspected: DOC-001 pp. 4, 6, 7, 8, and 9; DOC-004 pp. 15, 16, and 17.
- Remaining matters are limited to the exact human questions and missing definitions recorded separately above.
- All eight candidates remain Pending Human Adjudication.
