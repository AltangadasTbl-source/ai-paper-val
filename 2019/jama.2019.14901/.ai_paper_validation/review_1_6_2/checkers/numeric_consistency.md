# Numeric consistency review

Scope: all69 mapped source pages;45 stable grouped numeric relationships N001–N038 and N201–N207. All count, numerator/denominator, percentage, total, subgroup and matched-result arithmetic in main Table1/Table2, Figure1–3, narrative/abstract, supplementary eTables1–5 and survival risk sets, protocol historical table and image-only appendix are covered by [numeric inventory](../relationships/numeric_relationship_inventory.md). Complete map transcriptions preserve every subrow. No old finding, candidate, screening, verifier, critic or report conclusion was read. Source-only review; no external literature. One consolidated finding, four affected cells. Five excluded observations. No scientific coverage gap. Inferential S IDs and statistical tests are owned by the statistical reviewer; counts in their printed results are checked here.

## Reproduction and derivative provenance

The four affected cells were confirmed visually against a fresh rendering of the exact supplied PDF page. The nonhypercapnic day90 cell was also visually confirmed, then independently screened under the mandatory half-unit-input rule. The rendering engine was direct Poppler pdftoppm26.01.0 on CPU, PNG, single page, scaled to1800 pixels; no OCR was used and no source/reused asset was changed.

| Source location | Command | New derivative |
|---|---|---|
| joi190108supp2_prod.pdf PDF p.4 | pdftoppm -f 4 -l 4 -scale-to 1800 -png -singlefile joi190108supp2_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/numeric-results-p4 | preprocessing/numeric-results-p4.png |
| joi190108supp2_prod.pdf PDF p.7 | pdftoppm -f 7 -l 7 -scale-to 1800 -png -singlefile joi190108supp2_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/numeric-results-p7 | preprocessing/numeric-results-p7.png |

Protocol p.17 historical Table1 was directly read using pdftotext -f17 -l17 -layout joi190108supp1_prod.pdf - (Poppler26.01.0; output to tool stream, no persisted derivative). All other evidence locators are the newly completed source maps and curator-inventoried source-matched text/raster assets. JavaScript arithmetic evaluated printed values and interval bounds; no Python review orchestration or candidate classification was used.

## Findings

### F-NUM-001

**Title:** Four hypercapnic cough and secretion percentages do not reconcile with their explicit numerators and denominators.

**Locations and roles:** REPORT [joi190108supp2_prod.pdf, PDF p.4, eTable2](../../../joi190108supp2_prod.pdf#page=4), final two rows, the two hypercapnic columns (HFNC alone and HFNC with NIV). All compared quantities occur within this single display. N203 tracks the relationship. REPORT [main Table1 PDF p.6](../../../jama_thille_2019_oi_190108.pdf#page=6) corroborates aggregate counts and denominators but does not create the inconsistency or an additional cross-document relationship.

**Printed inputs:** Ineffective cough, No./total No.(%): hypercapnic HFNC alone14/45(69), HFNC with NIV16/59(73). Abundant secretions, No./total No.(%): hypercapnic HFNC alone20/46(57), HFNC with NIV23/61(62). Column participant totals48 and63 are separately printed; row-specific denominators are explicit45,59,46,61.

**Rule and calculation:** A row labeled No./total No.(%) states a percentage100×numerator/denominator. For each integer numerator n and denominator d, recomputed interval is [100(n−.5)/(d+.5),100(n+.5)/(d−.5)]; the whole-percentage printed interval is [p−.5,p+.5]. The intervals remain separated even under these permissive half-unit input bounds.

| Row / group | Printed pair | Direct ratio,% | Recomputed half-unit interval,% | Printed percentage interval,% | Gap,percentage points | Relative discrepancy |
|---|---|---:|---|---|---:|---:|
| Ineffective cough / HFNC alone |14/45(69)|31.1111|[29.6703,32.5843]|[68.5,69.5]|35.9157|0.52052|
| Ineffective cough / HFNC with NIV |16/59(73)|27.1186|[26.0504,28.2051]|[72.5,73.5]|44.2949|0.60678|
| Abundant secretions / HFNC alone |20/46(57)|43.4783|[41.9355,45.0549]|[56.5,57.5]|11.4451|0.20079|
| Abundant secretions / HFNC with NIV |23/61(62)|37.7049|[36.5854,38.8430]|[61.5,62.5]|22.6570|0.36544|

Each relative discrepancy exceeds0.05. The same within-display count/percentage rule fails across the same hypercapnic block in adjacent rows; this is one consolidated reporting pattern with all four locations, not four separate findings.

**Focus area:** A, counts and denominators.

**Proposed review domain:** statistical_results.

**Proposed relationship type / all relationships:** S_W / S_W.

**Qualifying route:** Route A, category 3.

**Affected result or extracted value:** Baseline prevalence of ineffective cough and abundant secretions in hypercapnic patients in each randomized arm; an extractor could take69%/73% or57%/62%, whereas the explicit ratios are approximately31%/27% or43%/38%.

**Why context does not resolve it:** The reproduced cells meet the always-register category for counts within one display. Even if the intended percentage can be reconstructed, its printed reading changes magnitude beyond the display-precision threshold and remains an extractable number.

**Source-grounded alternatives:** The adjacent previous-page lung-disease row prints33/48(69) and46/63(73), matching the cough percentage pair. This suggests a possible copied pair but does not establish how the four cells arose. The numerators and available denominators recombine with the nonhypercapnic rows to the main table: cough51+14=65 and70+16=86,239+45=284 and263+59=322; secretions101+20=121 and91+23=114,242+46=288 and265+61=326. An alternative population or percentage definition is not identified in the row labels/footnotes. The observed fact is the arithmetic inconsistency; the production mechanism is an inference and is not needed for inclusion.

**Exact human question:** For the hypercapnic cough and secretion cells in eTable2, which values should be used as the counts, available denominators and percentages, and do the displayed percentages refer to the explicitly printed numerator/denominator pairs or to another population?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 pp.1,4 abstract/results versus p.5 Table1 |219 women in randomized/completion narrative compared with analyzed-arm107+109=216. Even taking them as matched copies, summed-input interval[215,217] versus[218.5,219.5] leaves gap1.5/219=0.00685, below0.05; randomized and analyzed groups also differ by seven secondary exclusions. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 pp.1,6 narrative versus p.8 Table2 ARF difference |Narrative−8.7pp versus table−8.5pp. Half-unit copy intervals[−8.75,−8.65] and[−8.55,−8.45] leave gap.10/8.7=.01149, below0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-003 p.7 eTable4 day90 mortality |Printed difference−3.8pp versus100(50/276−54/254)=−3.1439pp. Half-unit inputs yield[−3.596663,−2.691302] and printed interval[−3.85,−3.75]; gap.153337/3.8=.040352, below0.05. Exact-count arithmetic alone would overstate the qualifying discrepancy. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 pp.7–8 time-to-reintubation/stay rows; REPORT DOC-003 pp.6–7 stay rows |Displayed difference need not equal subtraction of the two rounded medians: main ICU .5 vs12−11=1;hospital2.3 vs25−23=2;time−5 vs33−39=−6;hypercapnic ICU .6 vs13−13=0,hospital2.5 vs26−24=2;nonhypercapnic ICU .5 vs12−11=1. No source states these are simple differences of medians or supplies a common reproducing estimator for them. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002 pp.11,32 |Administrative total duration51 months versus components39+12 or36+12. This does not change a primary/key secondary result, analysis-population size or planned decision rule. | PERIPHERAL_COMPARISON |

## Completion and limitations

All45 grouped numeric relationships are complete. Within-displays, all percentage-bearing rows in Table1, Table2 and eTables1–5 were checked with their truthful denominators. All30 center numerator/denominator row sums and full columns reconcile to95/641,55/302,40/339. Every supplementary binary outcome numerator recombines across strata to the main table, including mortality among reintubated patients and the composite union identities. All eight main risk-set positions reconcile to the two stratum risk sets. Adjusted OR is expressly model-based, so it is not compared to a crude risk ratio as an identity requirement; no observed mislabeled OR/RR/RD/HR is reproduced. Plan intervention/endpoint decisions and statistical-method/inferential tests are covered by their independent lanes, with numeric plan/page mapping fully consulted here.

No raw data, participant-level weights or observations are supplied, so summary mean/SD/median reconstruction is unavailable. This is a reproducibility boundary, not a scientific source-coverage gap. Fresh render paths/engines are above. Neither source nor reusable assets were modified. Findings:1 consolidated issue; affected cells:4; excluded observations:5. No stable candidate IDs or dispositions assigned.
