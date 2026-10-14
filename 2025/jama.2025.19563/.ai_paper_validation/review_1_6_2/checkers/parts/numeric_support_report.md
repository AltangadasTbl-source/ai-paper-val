# Numeric consistency review: DOC-003 REPORT results supplement

Scope: every assigned quantitative relationship on all PDF pages 1–69 of `joi250084supp2_prod_1765403089.61751.pdf`. Read `QUALITY_CONTROL_SCOPE.md`, the complete 1.6.2 contract, tooling record, and both complete fresh results mapping parts. Numeric inventory N201–N256 covers all 56 numeric blocks and every constituent count, percentage, total and figure row. The inventory also records coherent checks, distinguishing participants from events and mutually exclusive categories from overlaps. Model, interval and test logic remains assigned to the statistical reviewer; no alternative analysis is proposed.

Direct source confirmation: newly rendered PDF p37, bundled `pdf_tools.py render`, user-authorized `/home/juliz/venvs/stt/bin/python`, PyMuPDF 1.28.0, 200 dpi, CPU. Derivative: `preprocessing/numeric-support-p037.png`. No fresh OCR or new package installation was needed. The direct PDF remains final authority.

## Findings

### F-NUM-201

**Title:** Two version-exposure percentages do not reconcile with the stated AI primary-analysis denominator.

**Source locations and document roles:** REPORT [DOC-003 PDF p37, eTable1b](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=37), rows `11.100.131 (September 2023)` and `122.100.407 (December 2024)`, each printed `5 (5)`, column headed `Number of Participants Exposed (% of Primary Analysis population assigned to AI-DPP)`. REPORT [DOC-003 PDF p27, cohort definition](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=27) defines primary analysis as all randomized participants; REPORT [DOC-003 PDF p41, eTable4](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=41) prints AI randomized N=183. REPORT [DOC-003 PDF p34, eFigure3](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=34) also prints 183 as AI primary-outcome denominator. These latter locations establish the named denominator; both affected percentage cells lie in the same display.

**Relationship:** N227; proposed relationship type S_W; all relationships S_W.

**Printed inputs:** Each affected row n=5, displayed percentage 5%; AI randomized/primary-analysis denominator 183. The preceding seven exposure rows use percentages consistent with183: 58(32),102(56),109(60),103(56),99(54),105(57),104(57).

**Rule and reproduced calculation:** Percent of the named arm population is 100n/N. Central calculation100×5/183=2.73224%. For the required conservative display-precision rule, n∈[4.5,5.5],N∈[182.5,183.5], giving recomputed percentage [2.45232%,3.01370%]. Printed5% has interval[4.5%,5.5%]. Their gap is4.5−3.01370=1.48630 percentage points; relative discrepancy1.48630/5=.297260, above.05. Both rows independently reproduce the same pattern and are consolidated here. Even allowing half-unit input intervals, they do not reconcile.

**Focus area:** A (counts and denominators).

**Proposed review domain:** statistical_results.

**Qualifying route:** Route A, category 3.

**Affected result or extracted value:** The percentages of AI primary-analysis participants exposed to the September2023 and December2024 application versions; an extractor could take either printed5% or the percentage represented by5of183.

**Why context does not resolve it:** Route A category3 applies to the count/denominator/percentage relationship in a display. The column explicitly names the full AI primary-analysis population. Its seven preceding rows reproduce that denominator, and neither affected row supplies a smaller denominator or a revised meaning for its percentage.

**Alternatives:** A later-version subgroup denominator near100 might explain5%, or one of the printed counts or percentages might represent a different quantity. The supplied display does not identify any such change. Version exposures overlap and need not sum to183; this overlap does not alter the percentage denominator named in the column.

**Exact human question:** What denominator and exposure counts apply to the September2023 and December2024 version rows, and which percentages should be extracted for those two versions?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-003 p55 eTable12, Human A+B combination | Printed10(19%) among59 composite achievers versus central16.949%. Conservative half-unit count/denominator inputs produce[15.9664%,17.9487%]; printed19 has[18.5%,19.5%], gap.55128pp/19=.02901≤.05. Other combinations, totals and component marginals reconcile. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-003 p39 eTable3, Not Hispanic or Latino | Printed343(93.5%) among368 versus central93.2065%; half-unit recomputed[92.9444%,93.4694%] overlaps printed[93.45%,93.55%]. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-003 p36 eTable1a, August2022 starting version | Printed60(32.76%) among183 versus central32.7869%; half-unit input interval includes32.76 and no reproduced discrepancy remains. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-003 p8 device table versus p46/p51 completion totals | Follow-up device entries282+30+0=312 versus313 completers; sum-input interval[310.5,313.5] overlaps313 half-unit interval[312.5,313.5], relative gap0. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-003 baseline actigraphy footnotes pp40,43,45,47,54 versus p49 eTable8b | Repeated baseline footnotes say n=3 without valid data; missingness table gives8+5=13. This comparison concerns baseline observation counts across locations; total randomized and endpoint-eligible analysis sizes remain explicitly368 and260. No source establishes that the same missingness category is meant or that a primary/key secondary result changes. | PERIPHERAL_COMPARISON |
| REPORT DOC-003 p34 eFigure3, all four adjusted rows | Adjusted RD−2.0,−3.4,.3,−1.6 differ from crude count differences, including equal A1C counts35/130 in both arms; the figure explicitly specifies age adjustment. | MODEL_VERSUS_CRUDE |
| REPORT DOC-003 p59 eTable16 MI sensitivity | MI-pooled percentages32.2/31.9 differ by.3pp while displayedRD is−1.1pp; a crude difference of pooled arm percentages need not reproduce a separately modeled/pool-combined estimate. Numeric comparison alone does not establish method identity; statistical reviewer owns the supplied-method check. | MODEL_VERSUS_CRUDE |
| REPORT DOC-003 p61 eTables18a–b | Two distinct activity-imputation scenarios produce identical58/183 and60/185 primary counts. They can coincide when their additionally affected participants do not change the composite; individual participant outcomes are not supplied to contradict that possibility. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-003 pp39–54 baseline BMI displays | Median BMI appears under a count/percentage-style heading in one baseline display; units and the fractional median/IQR pattern identify a continuous BMI summary immediately, without changing printed values. | NOTATION_OR_TYPOGRAPHY |

## Completion and limitations

Completed all56 numeric blocks,N201–N256,with one finding containing both affected rows and9excluded observations. Every categorical total, numerator/denominator/percentage pair, subgroup partition, composite marginal, missing-outcome total and adverse-event condition/grade total was checked in the complete inventory. Neither outcome overlap nor multiple events per participant was treated as mutually exclusive.

No numeric scientific coverage gaps. Model reconstruction is limited by unavailable raw participant data and the unsupplied R helper function; those do not restrict printed arithmetic checks. The native figure extractions omit plotted numbers, but complete fresh visual mappings cover every plotted row. No C IDs, severity, adjudication, or correction was assigned.
