# Numeric Consistency Review

## Complete scope

This review applies the numeric consistency checks to all 113 `N` relationships in `relationships/numeric_relationship_inventory.md`, reconstructed from the complete main and support maps. The checked direct-source scope is DOC-001-MAIN pp. 1-14, DOC-002 pp. 1-30, DOC-003 pp. 1-82, DOC-004 pp. 1-40, DOC-005 pp. 1-7, DOC-006 pp. 1-53, and DOC-007 p. 1. No page, result-bearing table, figure, formula group, or mapped numeric relationship was sampled or excluded by a count limit.

## Checks applied and outcomes

| Check family | Relationships checked | Reproducible rule and tolerance | Outcome |
|---|---:|---|---|
| Participant-flow, population, and analysis-unit reconciliation | N001-N003, N060, N068-N073, N079, N082-N083, N101, N113 | Reconcile only counts that have the same stated analysis population. Required identities include 958 - 606 = 352, 352 - 4 = 348, 348 - 12 = 336, 168 + 168 = 336, 170 + 166 = 336, and 101 + 24 + 79 = 204. | PASS. |
| Numerator, denominator, percentage, and missingness checks | N007-N008, N011-N016, N018-N022, N026-N028, N030-N034, N069-N072, N092-N103 | Recalculate count divided by stated denominator. Whole-percent values use nearest 1 percentage point; one-decimal values use nearest 0.1 percentage point. Do not add nested endpoints such as mRS 0-2 and mRS 0-3. | PASS. |
| Row, subgroup, and category sums | N011, N013, N015-N016, N025, N029, N038-N040, N060-N061, N067, N082-N083, N092-N093, N102 | Require a sum only for explicitly mutually exclusive and exhaustive categories. For independently rounded whole-percent mRS bars, a one-percentage-point difference from 100 is tolerated when every category is integer-feasible at the displayed denominator. | PASS. |
| Arithmetic, planned-total, and formula checks | N002-N003, N039-N047, N048, N051, N060, N082, N088-N089 | Check printed arithmetic and formula components without substituting an unreported model. Planned sample sizes are not compared as if they were observed result denominators. | PASS. |
| Population, reference group, measure, label, scale, direction, and unit checks | N004-N006, N009-N010, N014, N017, N023-N024, N035, N042-N059, N062-N067, N074-N081, N084-N091, N094-N100, N103, N110-N113 | Match population, time, contrast, reference group, unit, and effect-measure scale before comparison. A difference is eligible only if it is not explained by a stated different population, model, or definition. | One provisional candidate, below. All other applicable checks passed. |
| Rate, risk, proportion, person-time, and count distinctions | N021-N022, N042, N052, N058-N059, N062-N067, N070, N078-N081, N088-N089, N110-N111 | Check whether labels use the same quantity class as the printed value. A risk difference/reduction is an absolute scale; a risk/rate ratio is a relative dimensionless scale with null 1. | One provisional candidate, below. |
| Rounding and repeated-value checks | N007-N008, N011-N016, N018-N022, N026-N034, N061, N069-N073, N082-N084, N093-N100 | Test stated precision only; do not infer unprinted counts from a rounded graph. Repeated values are compared only after source, population, and model match. | PASS. |
| OCR-versus-direct-source confirmation | N004, N049, N087 and every provisional candidate source location | Direct PDF is controlling evidence. The rendered DOC-004 p. 18 states “a ≥4-point increase,” not “>4-point” as the reusable OCR transcribed. | PASS; the apparent NIHSS-threshold conflict is not a candidate. |
| Display-zero rule | N112 | A coherent display zero would be recorded as `DISPLAY_ZERO_NOT_CANDIDATE`; no candidate is created solely by finite display precision. | No display-zero-only candidate. |

## Provisional numeric consistency candidate

### Provisional candidate: Table 2 and Table 3 use the abbreviation aRR for incompatible absolute and relative measure labels

**Category:** Measure, label, or scale inconsistency.

**Exact source locations:**

- [DOC-001-MAIN, Table 2, PDF p. 7](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=7>).
- [DOC-001-MAIN, Table 3, PDF p. 9](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=9>).

**Direct source observation:** Direct PDF text/layout inspection of Table 2 prints “aRR, absolute risk reduction” in the abbreviation key. The same table’s footnote states, “aRR greater than 1 indicates higher rate ratio for mRS 0-2, 0-3, and 5-6 with endovascular thrombectomy.” Its aRR values include 0.94, 0.81, 0.89, 0.91, 1.00, 1.04, 1.03, and 1.05.

Direct PDF text/layout inspection of Table 3 again prints “aRR, absolute risk reduction” and separately prints “aRD, absolute risk difference.” Table 3 includes aRR values such as 1.33, 1.10, 1.20, 1.09, 1.03, 0.87, 1.18, and 1.05, and aRD values such as 0.178, negative 0.139, and 0.092.

**Printed inputs:**

- Table 2 abbreviation: `aRR = absolute risk reduction`.
- Table 2 direction sentence: `aRR greater than 1 indicates higher rate ratio`.
- Table 3 abbreviation: `aRR = absolute risk reduction`; `aRD = absolute risk difference`.
- Table 3 aRR example: `1.33 (95% CI, 0.52 to 3.44)`.
- Table 3 aRD example: `0.178 (95% CI, -0.109 to 0.465)`.

**Rule and calculation:** An absolute risk reduction or risk difference is a difference of two risks and is measured on an absolute proportion scale. Its null value is 0. A risk ratio or rate ratio is a quotient of two risks or rates and is dimensionless; its null value is 1. The printed Table 2 statement explicitly interprets values relative to 1 as a ratio. The Table 3 aRR example of 1.33 is consequently compatible with a relative ratio interpretation but not with an absolute risk-reduction interpretation; Table 3 separately labels the absolute-scale quantity as aRD and prints it as 0.178.

**Tolerance:** None. This is a categorical measure-label/scale comparison, not a rounding calculation.

**Inference distinguished from observation:** The inconsistent labels and the printed values are direct observations. The inference is only that at least one expansion or description of `aRR` may be inaccurate. The source package does not establish which wording was intended to control the final presentation.

**Alternative source-grounded interpretations:**

- `aRR` may have been intended to mean adjusted risk ratio, while “absolute risk reduction” was an abbreviation-key production error.
- “Higher rate ratio” may itself be the unintended wording, although the ratios centered on 1 and the separately printed aRD support the first interpretation.
- The authors may use a nonstandard internal expansion that needs confirmation; the displayed table does not define a mathematical alternative that reconciles an absolute reduction with values interpreted relative to 1.

**Quality-control relevance:** A data extractor could copy `aRR` as an absolute risk reduction rather than a relative risk/rate ratio, producing a wrong effect-measure class, null value, and scale for evidence synthesis or tabulation. This observation does not determine the study conclusion.

**Exact human question:** Do Tables 2 and 3 intend `aRR` to mean adjusted risk ratio (or another relative rate/risk ratio), and should the abbreviation key and the “higher rate ratio” footnote be corrected so that the reported label, null value, and scale are consistent?

## Candidate count and exclusions

- Distinct provisional candidates emitted: 1.
- No stable candidate ID, severity, validity assessment, or disposition is assigned in this checker.
- The apparent “>4” versus “at least 4” neurological-worsening conflict was excluded after direct PDF rendering showed that the SAP uses “a ≥4-point increase”; its OCR text was inaccurate.
- Rounded mRS bars, nested mRS endpoints, planned sample sizes, and explicitly different ITT/as-treated/subgroup populations were not converted into candidates because the stated rules reconcile them.
