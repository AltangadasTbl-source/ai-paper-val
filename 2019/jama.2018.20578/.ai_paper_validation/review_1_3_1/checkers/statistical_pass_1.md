# Statistical Consistency Review — Pass 1

## Completion statement

Pass 1 independently checked every stable statistical relationship `S001`-`S053` in `statistics/relationship_inventory.md`. Discovery continued through the full scope after each proposal; no candidate count, top-N boundary, or legacy finding was used. Every `S` record is marked `PASS_1_COMPLETE`.

Direct PDFs were used to confirm the printed evidence for each proposal below. Current extraction maps were locators and transcription aids only. These are proposals for coordinator duplicate-merging and later human adjudication, not dispositions or corrections.

## Check coverage

| Check | Exact scope | Result |
|---|---|---|
| Point-estimate containment and endpoint order | All HR, RR, ARD/ARR, raw-change, treatment-by-time, sensitivity, study-level forest, and pooled intervals in `S002`-`S009` and `S026`-`S053` | All estimates were contained and all endpoints ordered. Null-boundary reporting generated `SP1-003`; no reversed interval was found. |
| Sign and direction | Treatment contrasts, ARD/ARR rules, efficacy/safety directions, narrative repetitions, event-count directions | Directions agreed except for no source-supported contradiction. Scale/unit and reciprocal issues are separately proposed below. |
| Effect/scale/interval labels | HR, RR, ARD, ARR, NNT, NNH, CI, CrI, measurement units | Proposals `SP1-001`, `SP1-004`, `SP1-005`, and `SP1-006`. |
| DIC/model selection | All 44 population-outcome rows on DOC-003 pp. 5-6 | 43 rows follow the printed rule; one proposal (`SP1-002`). |
| Statistical significance/NNT presence | All 44 eTable 3 ARDs and all 18 displayed NNT/NNH entries | One printed null-boundary/NNT proposal (`SP1-003`); one multi-row reciprocal proposal (`SP1-007`). |
| P/test/statistic/SE compatibility | Cox HR/CI/P results, Holm-adjusted secondary results, Egger coefficient/SE/t/P, forest heterogeneity | Checked only under supplied definitions. Rounded-value diagnostics were compatible except for the separately described proposals. Missing raw P values, covariance, df, unrounded values, and rounding rules were not inferred. |
| Cross-location repetition | DOC-001 abstract/results; DOC-002 protocol/DOC-003 methods; DIC selection/forest model context | Numeric repetitions agreed. Distinct HR, RR, adjusted trajectory, raw change, log-rank, and ARD estimands were not falsely equated. |

## Candidate proposals

### SP1-001 — HbA1c daily-rate estimate is printed with a mass-concentration unit while the table identifies HbA1c as percent

- **Related relationship:** `S006`.
- **Proposed primary category:** `Measure, label, or scale inconsistency`.
- **Exact source evidence:** [DOC-001 p. 1](../../../jama_flint_2019_oi_190079.pdf#page=1) prints the abstract daily-rate result as “HbA1c levels (-0.0002 mg/dL; 95% CI, -0.0021 to 0.0016).” [DOC-001 p. 8](../../../jama_flint_2019_oi_190079.pdf#page=8), Table 4, labels the HbA1c measure “HbA1c, %” and prints baseline/termination values around 5.7-5.9.
- **Direct observation:** the exact same named analyte has `mg/dL` attached to its adjusted daily-rate estimate in the abstract and `%` attached to its raw level in Table 4.
- **Reproducible logic:** `mg/dL` is a mass-concentration scale, whereas `%` is the displayed HbA1c scale in this source. The estimate/CI numbers repeat in the results without a restated unit, so the package supplies no source statement that converts this coefficient to `mg/dL`.
- **Alternative source-grounded interpretations:** the abstract may have carried the unit pattern from adjacent glucose/lipid outcomes; alternatively the model coefficient may use another HbA1c scale that was not restated. The supplied table supports percent but does not establish the intended coefficient label conclusively.
- **Exact human question:** should the abstract HbA1c daily-rate estimate be labelled in percentage points per day (or another HbA1c scale) rather than `mg/dL`?

### SP1-002 — The all-patient incident-cancer model selection does not follow the printed DIC/I2 tie rule at the stated threshold

- **Related relationships:** `S020`, with forest-context cross-reference `S049`.
- **Proposed primary category:** `Statistical reporting inconsistency`.
- **Exact source evidence:** [DOC-003 p. 4](../../../joi180151supp2_prod.pdf#page=4) says that when fixed and random DIC values are within 3 units, random effects are favored if fixed-effect `I2 >25%`. [DOC-003 p. 5](../../../joi180151supp2_prod.pdf#page=5), eMethods 3, prints for all-patient incident cancer: fixed DIC 27.06, random DIC 27.93, fixed-effect I2 25%, selected model `random`.
- **Direct observation:** the DIC difference is 0.87, so the within-3 branch applies; the printed I2 equals 25%, not greater than 25%, yet the printed selected model is random.
- **Reproducible logic:** under the exact strict inequality printed on p. 4, an I2 of 25% does not satisfy `>25%`. The other all-patient within-3 rows at I2 below 25 select fixed, while the incident-cancer row selects random.
- **Alternative source-grounded interpretations:** an unrounded I2 could exceed 25% while displaying as 25%; the intended threshold may have been `>=25%`; or the model label may be wrong. No unrounded I2 or exception is supplied.
- **Exact human question:** was the unrounded incident-cancer I2 greater than 25%, was the intended rule inclusive at 25%, or should this row's selected-model label be fixed?

### SP1-003 — A low-risk all-MI NNT is printed although the displayed ARD confidence interval reaches 0.00

- **Related relationship:** `S029`.
- **Proposed primary category:** `Statistical reporting inconsistency`.
- **Exact source evidence:** [DOC-003 p. 4](../../../joi180151supp2_prod.pdf#page=4) says NNT/NNH values were calculated for outcomes with a statistically significant risk reduction/increase. [DOC-003 p. 15](../../../joi180151supp2_prod.pdf#page=15), eTable 3, prints low-risk all myocardial infarction ARD `-0.27 (-0.49 to 0.00)` and NNT `366`; its footnote says NNT/NNH values are reported only for statistically significant ARDs.
- **Direct observation:** at the displayed precision, the 95% CI includes the null endpoint 0.00 while an NNT is present under an exclude-null reporting rule.
- **Reproducible logic:** a two-sided 95% CI that includes 0 does not meet the table's stated interval-based significance condition. Unlike the rounded-to-null CrI values on pp. 16 and 18, this row has no footnote giving an unrounded endpoint.
- **Alternative source-grounded interpretations:** the unrounded upper endpoint may be slightly below zero and round to 0.00; the NNT may use an unrounded significant result; or the NNT may have been retained despite a null-reaching interval.
- **Exact human question:** what is the unrounded upper ARD confidence limit for low-risk all MI, and does it exclude zero under the analysis used to decide whether NNT 366 should be displayed?

### SP1-004 — The diabetes total-stroke HR endpoint is labelled as both a credible and a confidence limit

- **Related relationship:** `S037`.
- **Proposed primary category:** `Measure, label, or scale inconsistency`.
- **Exact source evidence:** [DOC-003 p. 16](../../../joi180151supp2_prod.pdf#page=16), eTable 4, labels the HR column `HR (95% CrI)` and prints the diabetes HR `0.78 (0.61 to 1.00)*`; the asterisk footnote says `Upper confidence interval 1.004`.
- **Direct observation:** the column explicitly identifies a Bayesian credible interval (`CrI`), while the footnote calls the same upper endpoint a confidence interval.
- **Reproducible logic:** CI and CrI are distinct inferential labels in this package: the adjacent ARR is labelled 95% CI and the HR is labelled 95% CrI. The footnote attaches 1.004 to the starred HR/CrI cell.
- **Alternative source-grounded interpretations:** “confidence interval” may be informal wording intended to mean interval endpoint; alternatively the HR interval may have been frequentist, but the methods and column header support a Bayesian CrI.
- **Exact human question:** should the footnote read `upper credible interval limit 1.004` (or equivalent), or is the HR interval type in the header incorrect?

### SP1-005 — The <=100-mg all-MI sensitivity endpoint is labelled as both a credible and a confidence limit

- **Related relationship:** `S038`.
- **Proposed primary category:** `Measure, label, or scale inconsistency`.
- **Exact source evidence:** [DOC-003 p. 18](../../../joi180151supp2_prod.pdf#page=18), eTable 6, states `Data presented as Hazard Ratio (95% CrI)`, prints all-MI HR `0.87 (0.76 to 1.00)*` for aspirin dose <=100 mg, and footnotes `Upper confidence interval 0.9989`.
- **Direct observation:** the table defines a 95% credible interval but the asterisk calls the exact endpoint a confidence interval.
- **Reproducible logic:** the footnote is unambiguously attached to the starred 1.00 endpoint in a table explicitly labelled 95% CrI.
- **Alternative source-grounded interpretations:** “confidence interval” may be informal wording; alternatively the sensitivity table might use frequentist intervals despite the CrI label, but the source provides no such exception.
- **Exact human question:** is 0.9989 the upper credible limit, or should the table's interval-type label be CI rather than CrI?

### SP1-006 — eTable 3 does not state the ARD unit needed to interpret the displayed values and their NNT/NNH reciprocals

- **Related relationships:** `S025`-`S036`.
- **Proposed primary category:** `Measure, label, or scale inconsistency`.
- **Exact source evidence:** [DOC-003 p. 4](../../../joi180151supp2_prod.pdf#page=4) defines absolute risk difference and its direction but does not state a display unit. [DOC-003 p. 15](../../../joi180151supp2_prod.pdf#page=15), eTable 3, labels columns only `ARD`, gives values such as composite `-0.41` with NNT `242`, and provides no `%`, percentage-point, proportion, per-100, or other unit in the title, headers, body, or footnote.
- **Direct observation:** the NNT scale implies that `-0.41` is approximately 0.41 percentage points: treating it as a proportion would imply an NNT near 2.4, while treating it as percentage points implies an NNT near 244 before unrounded-value effects.
- **Reproducible logic:** the numeric meaning changes by a factor of 100 depending on whether the displayed ARD is a proportion or percentage points. The accompanying NNTs help infer the intended scale but do not replace an explicit label.
- **Alternative source-grounded interpretations:** the journal/table convention may intend percentage points; the ARDs may have been multiplied by 100 for display; or another scaling convention may have been used. The package does not state it.
- **Exact human question:** what is the explicit unit/scale of every ARD in eTable 3, and should the table label it as percentage points (if that is the intended scale)?

### SP1-007 — Three major-bleeding NNHs do not reciprocally reconcile with the displayed two-decimal ARDs under ordinary rounding bounds

- **Related relationship:** `S034`.
- **Proposed primary category:** `Numeric or arithmetic inconsistency`.
- **Exact source evidence:** [DOC-003 p. 15](../../../joi180151supp2_prod.pdf#page=15), eTable 3, prints major-bleeding ARD/NNH pairs: all patients `0.47` / `210`, high risk `0.64` / `152`, and diabetes `0.80` / `121`. [DOC-003 p. 4](../../../joi180151supp2_prod.pdf#page=4) states that NNT/NNH is calculated for statistically significant risk changes but does not give an integer-rounding convention.
- **Direct observation:** if the ARDs are percentage points as implied by the table, the printed point values give simple reciprocals of about 213, 156, and 125, respectively, before any stated integer-rounding rule. More strongly, ordinary nearest-two-decimal rounding bounds do not reach the printed NNHs: 0.47 permits reciprocal values above about 210.5, 0.64 permits about 155.0-157.5, and 0.80 permits about 124.2-125.8; the printed values are 210, 152, and 121.
- **Reproducible logic:** NNH is the reciprocal of absolute risk increase under the table's stated ARD-to-NNH relationship. The low-risk pair `0.40` / `249` and the other outcome pairs can be compatible with unrounded ARDs, so this is not merely the absence of a universal exact reciprocal at displayed precision.
- **Alternative source-grounded interpretations:** NNH may have been calculated from a different unrounded risk contrast than the ARD point estimate; the ARDs may use nonstandard display rounding; NNH may use an unstated method; or one or more values may be transcribed incorrectly in the source.
- **Exact human question:** what unrounded ARDs and NNH rounding method produced 210, 152, and 121, and are those NNHs derived from the same ARD estimand displayed in their cells?

## Noncandidate diagnostics and limitations

- All interval endpoints were ordered and every point estimate was contained.
- Rounded-log-CI Wald checks for DOC-001 Cox results were used only as diagnostics; the reported Cox model/test was not reconstructed from convention.
- Holm-adjusted P values could not be exactly recalculated because raw P values, full coefficient precision, and adjustment ordering inputs are absent.
- The eTable 4 diabetes HR upper CrI of 1.00 was not treated as excluding 1 because its source footnote gives unrounded 1.004. The eTable 6 <=100-mg all-MI upper CrI of 1.00 was treated as excluding 1 because its source footnote gives unrounded 0.9989. The interval-type label issues remain separately recorded in SP1-004 and SP1-005.
- Forest plots report frequentist RR/CIs while the Bayesian tables report HR/CrIs. They are distinct measures/models and were not compared as if numerically identical.
- Exact ARD reconstruction is limited by absent unrounded pooled RRs, baseline risks, ARDs, scale label, and NNT/NNH rounding rule.
- Statistical pass 2 remains required for all `S001`-`S053` after candidate registration and mechanical evidence recheck.

## Pass 1 counts

- Stable `S` relationships completed: 53.
- Unique candidate proposals: 7 (`SP1-001`-`SP1-007`).
- Relationships left incomplete: 0.

## Validator-explicit pass-1 completion register

This register restates completion with every stable relationship ID as a literal token. It does not replace the detailed checks or candidate proposals above.

| S ID | Pass-1 status |
|---|---|
| S001 | PASS_1_COMPLETE |
| S002 | PASS_1_COMPLETE |
| S003 | PASS_1_COMPLETE |
| S004 | PASS_1_COMPLETE |
| S005 | PASS_1_COMPLETE |
| S006 | PASS_1_COMPLETE |
| S007 | PASS_1_COMPLETE |
| S008 | PASS_1_COMPLETE |
| S009 | PASS_1_COMPLETE |
| S010 | PASS_1_COMPLETE |
| S011 | PASS_1_COMPLETE |
| S012 | PASS_1_COMPLETE |
| S013 | PASS_1_COMPLETE |
| S014 | PASS_1_COMPLETE |
| S015 | PASS_1_COMPLETE |
| S016 | PASS_1_COMPLETE |
| S017 | PASS_1_COMPLETE |
| S018 | PASS_1_COMPLETE |
| S019 | PASS_1_COMPLETE |
| S020 | PASS_1_COMPLETE |
| S021 | PASS_1_COMPLETE |
| S022 | PASS_1_COMPLETE |
| S023 | PASS_1_COMPLETE |
| S024 | PASS_1_COMPLETE |
| S025 | PASS_1_COMPLETE |
| S026 | PASS_1_COMPLETE |
| S027 | PASS_1_COMPLETE |
| S028 | PASS_1_COMPLETE |
| S029 | PASS_1_COMPLETE |
| S030 | PASS_1_COMPLETE |
| S031 | PASS_1_COMPLETE |
| S032 | PASS_1_COMPLETE |
| S033 | PASS_1_COMPLETE |
| S034 | PASS_1_COMPLETE |
| S035 | PASS_1_COMPLETE |
| S036 | PASS_1_COMPLETE |
| S037 | PASS_1_COMPLETE |
| S038 | PASS_1_COMPLETE |
| S039 | PASS_1_COMPLETE |
| S040 | PASS_1_COMPLETE |
| S041 | PASS_1_COMPLETE |
| S042 | PASS_1_COMPLETE |
| S043 | PASS_1_COMPLETE |
| S044 | PASS_1_COMPLETE |
| S045 | PASS_1_COMPLETE |
| S046 | PASS_1_COMPLETE |
| S047 | PASS_1_COMPLETE |
| S048 | PASS_1_COMPLETE |
| S049 | PASS_1_COMPLETE |
| S050 | PASS_1_COMPLETE |
| S051 | PASS_1_COMPLETE |
| S052 | PASS_1_COMPLETE |
| S053 | PASS_1_COMPLETE |
