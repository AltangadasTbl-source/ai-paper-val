# Cross-Source Consistency Review

## Scope, method, and outcome

Reviewed the complete assigned relationship inventory: `N001`-`N059` and `S001`-`S039`. The comparison set was limited to supplied direct PDFs: the main article (abstract, narrative, tables, figures, captions, footnotes, and correction notice), protocol, results supplement, and data-sharing statement. Mapper artifacts were used as locators; the two candidate observations below were re-read against the named direct PDF pages.

For every proposed match, I first required the same population, time window, arm order/contrast, analysis set, measure, scale, and displayed precision. Planned protocol values were not treated as observed trial results. No supplied structured data file exists. No old candidate, checker, verifier, critic, quality, or final-report output was read.

**Outcome:** 2 distinct qualifying cross-source candidates, both `Pending Human Adjudication`. The two observations have provenance in four relationship IDs (`N004`, `N011`, `N032`, and `S004`); every other assigned relationship and every noncandidate comparison aspect of those four IDs has an explicit no-candidate outcome below. These are provisional checker keys only and are not stable `C` IDs or AI adjudications.

## Qualifying candidates

### CROSS-CAND-001 — Day-7 postextubation-respiratory-failure absolute difference differs within the main article

- **Category:** Cross-document numeric inconsistency.
- **Relationship provenance:** `N011`; `S004`.
- **Matched-result identity:** randomized analysis population (HFNO alone `n=302`, HFNO with NIV `n=339`); postextubation respiratory failure at day 7; contrast is HFNO with NIV minus HFNO alone; percentage-point scale.
- **Exact direct-source locations:** [main article — PDF p. 1](<../../../jama_thille_2019_oi_190108.pdf#page=1>) (abstract Results); [main article — PDF p. 6](<../../../jama_thille_2019_oi_190108.pdf#page=6>) (Results narrative); [main article — PDF p. 8](<../../../jama_thille_2019_oi_190108.pdf#page=8>) (Table 2).
- **Direct observation:** the abstract prints `21% vs 29%; difference, −8.7% (95% CI, −15.2% to −1.8%); P = .01`. The Results narrative repeats `21% vs 29%; difference, −8.7%` with the same interval and P value. Table 2 prints the same arm counts/rounded percentages, `88 (29)` and `70 (21)`, but prints `−8.5 (−15.2 to −1.8)` and `.01`.
- **Comparison logic and calculation:** the fully specified population, endpoint, day-7 window, contrast, interval, and P value match. From the displayed counts and denominators, `(70/339 − 88/302) × 100 = −8.49` percentage points, which rounds to `−8.5` at one decimal place. Thus the Table 2 point estimate agrees with the displayed counts; the `−8.7` value is a distinct printed point estimate, not a difference caused by rounding `−8.49` to one decimal place.
- **Supported alternatives:** a transcription/editing discrepancy between prose and Table 2; a calculation based on an unprinted population/denominator; or an intended definition distinction that is not labelled in either matched presentation. The supplied pages do not identify a different analysis set or outcome definition for the prose value.
- **Human verification steps:** confirm the authorial analysis output for day-7 respiratory failure, its exact denominator(s), and whether any amended endpoint-definition/data-cut produced `−8.7`; then determine which presentation should carry the resolved absolute difference. Confirm that the identical CI and P value belong to that same calculation.

### CROSS-CAND-002 — Protocol and article print different acidosis thresholds in the reintubation respiratory-failure definition

- **Category:** Measure, label, or scale inconsistency.
- **Relationship provenance:** `N004` (main outcome/reintubation definition) and `N032` (protocol reintubation definition; mapper key `SUPPORT-N009`).
- **Matched-definition identity:** reintubation ascertainment for the same HFNC-alone versus HFNC-plus-NIV randomized trial; severe respiratory failure requires at least two listed criteria; respiratory acidosis is one such criterion; pH is reported in units with the same accompanying `PaCO2 >45 mm Hg` condition.
- **Exact direct-source locations:** [main article — PDF p. 4](<../../../jama_thille_2019_oi_190108.pdf#page=4>) (Outcomes); [protocol — PDF p. 31](<../../../joi190108supp1_prod.pdf#page=31>) (section 5.4, continuation from p. 30).
- **Direct observation:** the main article defines severe respiratory failure leading to reintubation as at least two criteria and prints respiratory acidosis as `pH level below 7.25 units and PaCO2 greater than 45 mm Hg`. The protocol defines respiratory failure for reintubation as at least two criteria and prints respiratory acidosis as `pH < 7.35 units and PaCO2 > 45 mm Hg`.
- **Comparison logic:** the criterion role, measure, unit, comparator condition, and decision context match, while the displayed pH cutoff differs by `0.10` pH units (`<7.25` versus `<7.35`). This is a definition-level quantitative mismatch, not a comparison of a planned sample-size value with an observed result.
- **Supported alternatives:** the supplied protocol is version 4 dated October 17, 2017 and may predate an approved amendment or a final operational definition; the article may report an implementation-specific definition; or one document may contain a transcription/reporting discrepancy. The package supplies no amendment history or definitive case-report definition that resolves the difference.
- **Human verification steps:** retrieve the final approved protocol/amendment history and the prespecified case-report/manual definition used during enrolment; determine which cutoff governed event classification and whether the main-article and supplement descriptions should be aligned. If an amendment exists, verify its effective date and whether it applied to every analyzed participant.

## Explicit no-candidate outcomes

The following groups were compared under the stated matching rule and produced no additional qualifying candidate. “No candidate” does not say that a planned protocol statement equals an observed result; it records that no same-result conflict was established from the supplied pages.

| Relationships checked | Cross-source comparison and no-candidate result |
|---|---|
| `N001`, `N002`, `N006`-`N010`, `N012`-`N021`; `S003`, `S005`-`S022` | The abstract, Key Points, narrative, flow diagram, Table 1, Table 2, Figure 2, and Figure 3 were matched only at shared analysis set/time/contrast. Allocation and analyzed totals (`648`, `302`, `339`, `641`), primary day-7 reintubation (`55/302` versus `40/339`, `−6.4`), 48-hour/72-hour/ICU-discharge reintubation, mortality, subgroup denominators/effects, adjusted OR, and figure labels/risk sets had no additional cross-location numeric, direction, scale, reference-group, rate/count, or inferential conflict. `N011`/`S004` are excluded here because they are CROSS-CAND-001. |
| `N003`, `N004`, `N022`, `N023`; `S001`, `S002`, `S023` | Main-article intervention dose, endpoint windows, sample-size design statement, planned-test labels, correction notice, and no-applicable pages were compared with like-for-like material where present. The correction note identifies corrected intervention/exploratory/axis material but does not itself print a competing quantitative result. The main reintubation-definition component matched the protocol except for the pH cutoff documented as CROSS-CAND-002. |
| `N005`, `N027`, `N035`; `S024`-`S030` | Protocol target/sample-size and planned inferential framework were separated from observed trial results. Planned `n=650`, 80% power, 18% versus 10%, and planned methods are not contradicted by observed `648` randomized/`641` analyzed or by subsequently reported estimates: they concern different temporal roles. No candidate was created from expected rates, historical studies, unexecuted model possibilities, or a plan-versus-observation difference. |
| `N024`-`N026`, `N028`-`N031`, `N033`-`N035`; `S031`-`S039` | Results-supplement eTables/eFigure were matched to the main results at identical arm order, PaCO2 stratum, time point, and scale. eTable 1 reproduces day-7 respiratory-failure counts (`88/302`, `70/339`) and ICU-discharge reintubation counts (`59/302`, `41/339`); eTables 3-4 reproduce the primary-subgroup counts/effects after preserving distinct decimal precision; eTable 5 totals reconcile to `95/641`, `55/302`, and `40/339`; and the eFigure gives an unadjusted 90-day survival log-rank P value rather than a duplicate of a distinct main-table effect. No unmatched scale, denominator, direction, rate/count, or P-value conflict was found. |
| `N036`-`N059` | Baseline-stratum values, criteria/reason component rows, center data, protocol definitions, historical table values, and the data-sharing statement were checked for cross-document matches. Component/reason rows are expressly overlapping where relevant and were not incorrectly summed into event totals. Weighted/rounded subgroup presentations and aggregate main-table values were not called conflicts without identical precision and an asserted same-result representation. DOC-004 provides no result data. |

## Coverage and limitations

- **Completed inventory coverage:** 59 numeric/reporting relationships (`N001`-`N059`) and 39 inferential relationships (`S001`-`S039`), including all mapped abstract, narrative, Table 1/Table 2, Figure 1-3, captions/footnotes, protocol, eTables/eFigure, and the supplied data-sharing statement.
- **Direct-source confirmation:** candidates were checked on the source PDF pages linked above. Reused extraction/mapping files were locators, not candidate authority.
- **Limitations:** no raw data, analysis code, amendment log, statistical analysis plan distinct from the supplied protocol, or structured dataset was supplied. The protocol’s planned statements cannot establish an observed-result conflict without a matched final implementation/result definition. Graphical curves were not digitized where no exact plotted values were printed.
- **Excluded by scope:** general design concerns, historical-study comparisons, unlabelled model alternatives, and coherent display precision were not candidates. No candidate was based on a display-zero P value.
