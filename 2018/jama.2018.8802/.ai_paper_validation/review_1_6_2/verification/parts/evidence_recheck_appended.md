## C005 — Three-month vascular-death interval and P relationship

**Appended recheck provenance:** Runtime agent /root/recheck5; model gpt-6.1-sol; reasoning effort high; start mode FRESH_SPAWN. Assigned stable ID C005 only, including every affected location and all eleven supporting difference rows. Finding F-ST2-001; independent pass-2 screening INCLUDE. The complete QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read. This card records evidence facts; C005 remains **Pending Human Adjudication**.

**Location found; source value/text matched; comparator matched:** Yes for every location below and every tuple in the twelve-row calculation table. Exact supplied-source rendering controls signs, column pairing and display precision; extraction is a transcription aid. Direct CPU Poppler 25.03.0 extraction and fresh rendering of supplement pp.6–7 were used. The existing current-run direct-source main p.4 extraction and rendering were reread and visually inspected. No legacy scientific conclusions, web, OCR, unapproved Python, nested agents, source changes or reused-asset changes were used.

| Exact supplied-source location | Role by content | Source-confirmed content and comparison function |
|---|---|---|
| [Results supplement p.6, eTable 3, three-month vascular-death row](../../../../joi180070supp2_prod.pdf#page=6) | REPORT: completed-trial secondary-outcome results | Intervention 46/2400 (1.9%); control 67/2400 (2.8%); adjusted absolute difference −1.43 percentage points, 95% CI −2.33 to −0.54; its immediately adjacent P is printed **0.001**. These are the registered compared values. The separate HR 0.62 (0.42–0.92) has its own P=.02; that separate P is not substituted for the difference P. |
| [Results supplement p.6, all eleven other eTable 3 absolute-difference rows](../../../../joi180070supp2_prod.pdf#page=6) | REPORT: same completed-trial results display | Ischemic stroke, hemorrhagic stroke and myocardial infarction at 3, 6 and 12 months, plus vascular death at 6 and 12 months. Every estimate, endpoint and adjacent difference P is reproduced in the full numerical table below. These are comparator rows supporting the diagnostic relationship, not eleven additional registered inconsistencies. |
| [Results supplement p.7, eTable 3 footnote a](../../../../joi180070supp2_prod.pdf#page=7) | REPORT: explanation of completed-trial adjusted results | Adjustment is for patient and hospital characteristics: age, gender, ischemic-stroke history, hypertension, diabetes, hyperlipidemia, atrial fibrillation, coronary disease/previous myocardial infarction, ever smoking, admission NIHSS, hospital grade, region, stroke unit, teaching status and neurological-ward beds. This confirms adjusted quantities and does not prescribe the difference-specific CI/test formula. Footnote * permits multiple types of new vascular event per patient; no disjoint-count assumption is used. |
| [Main p.4, Data Analysis](../../../../jama_wang_2018_oi_180070.pdf#page=4) | REPORT: completed-trial analysis description | Comparative outcomes have adjusted cumulative incidences and absolute differences with 95% CIs. A P value less than .05 is significant; all tests are two-sided. Clinical vascular events/mortality are time-to-event outcomes, with multivariable Cox models described. The page does not name the absolute-difference CI/test construction, covariance estimator or a distinct construction for this row. This corroborates confidence level, sidedness and adjustment; it is not a conflicting cross-document value. |

**Consistency rule applicable:** Yes for a source-supported diagnostic under focus B and Route A, category 1. The two-sided normal-Wald relation is empirically supported by all eleven other absolute-difference rows of the same display after full half-unit input allowances. The method is labelled diagnostic because its exact use by the authors is not stated. The supplied scope treats a numerical interval/P conflict under a same-display supported relationship as registerable even when the undisclosed construction remains a human question. No crude count ratio is substituted for the adjusted difference. Both the printed CI and P indicate significance below .05; no significance reversal is claimed.

**Calculation or logical comparison reproduced:** Yes. With q=Φ⁻¹(.975)=1.959963984540054, use SE=(U−L)/(2q), z=|b|/SE, and diagnostic P=2Φ(−z). For b=−1.43, L=−2.33 and U=−0.54, central SE=0.456641043948, z=3.131562567477 and P=0.001738787319.

Normal tails were independently evaluated in JavaScript by composite Simpson integration of the standard-normal density from 0 to z using 20,000 subintervals. Repeating the decisive lower bound with 10,000 subintervals changed P by approximately 8.44×10⁻¹⁵. These calculations refine the checker's approximate normal-tail numbers and agree with the independently screened values; they do not recreate patient-level model estimation.

**Display-precision interval check:** Every displayed estimate and CI endpoint in these rows has two decimal places and receives ±.005. For C005:
- b∈[−1.435,−1.425], L∈[−2.335,−2.325], U∈[−0.545,−0.535].
- Independent attainable width U−L∈[1.780,1.800], SE∈[0.454089976663,0.459192111232], and |z|∈[3.103276308855,3.160166649230].
- Conservative independently varying input P envelope: [0.001576789229,0.001913908588].
- Printed 0.001 receives ±.0005, so its interval is [0.000500000000,0.001500000000].
- Minimum interval gap=0.000076789229; relative discrepancy=gap/0.001=0.076789228826>0.05. The two intervals do not overlap. Route A category 1 is not screened out as rounding; the explicit gap also exceeds the general display threshold.

A symmetric-Wald construction additionally requires b=(L+U)/2. To avoid claiming support merely from inconsistent independent choices, intersect the endpoint rectangle with 2b_low≤L+U≤2b_high. Evaluate the linear-fractional magnitude |q(L+U)/(U−L)| at all feasible rectangle vertices and intersections of each rectangle edge with both sum boundaries. This yields the centered C005 P envelope [0.001576789229,0.001777726117], still disjoint from the printed P interval. All eleven comparison rows retain overlap when this same centering constraint is applied.

**Complete same-display comparator calculation:** All source tuples below were directly matched to the fresh p.6 rendering and layout extraction. Actual printed P precision is retained: ischemic stroke at 3 months prints **0.40**, and hemorrhagic stroke at 12 months prints **0.80**, each with ±.005 rather than ±.05. The screen's rendered numerical tuples abbreviated them as 0.4 and 0.8, but its actual P intervals already used ±.005. Thus this table restores the true printed notation without changing C005's registered source values, comparator interval calculations or evidence state. The estimates −0.10, −1.40, −0.80 and 0.30 also retain their actual two-decimal display.

| Relationship; eTable 3 difference row | Printed b (L to U); paired P | Central diagnostic P | Independent-input P envelope | Printed P interval | Centered-Wald P envelope | Centered comparison |
|---|---|---:|---|---|---|---|
| S053; Ischemic stroke, 3 months | -0.57 (-1.91 to 0.76); 0.40 | 0.402683322 | [0.396798477, 0.408575678] | [0.395000000, 0.405000000] | [0.396798477, 0.402683322] | Overlap; gap 0 |
| S055; Hemorrhagic stroke, 3 months | -0.35 (-0.92 to 0.22); 0.23 | 0.228788052 | [0.218142721, 0.239603511] | [0.225000000, 0.235000000] | [0.222207459, 0.235506219] | Overlap; gap 0 |
| S057; Myocardial infarction, 3 months | -0.10 (-0.36 to 0.17); 0.48 | 0.459537248 | [0.428638325, 0.490435101] | [0.475000000, 0.485000000] | [0.459537248, 0.490435101] | Overlap; gap 0 |
| S059; Vascular death, 3 months | -1.43 (-2.33 to -0.54); 0.001 | 0.001738787 | [0.001576789, 0.001913909] | [0.000500000, 0.001500000] | [0.001576789, 0.001777726] | No overlap; gap 0.000076789 |
| S061; Ischemic stroke, 6 months | -1.40 (-2.82 to 0.02); 0.05 | 0.053315228 | [0.051641210, 0.055022111] | [0.045000000, 0.055000000] | [0.052469670, 0.054172138] | Overlap; gap 0 |
| S063; Hemorrhagic stroke, 6 months | -0.25 (-0.80 to 0.30); 0.38 | 0.372986726 | [0.359117819, 0.386923907] | [0.375000000, 0.385000000] | [0.363502921, 0.382622273] | Overlap; gap 0 |
| S065; Myocardial infarction, 6 months | -0.03 (-0.35 to 0.29); 0.86 | 0.854212231 | [0.827605378, 0.880159945] | [0.855000000, 0.865000000] | [0.830257707, 0.878301920] | Overlap; gap 0 |
| S067; Vascular death, 6 months | -1.06 (-2.08 to -0.04); 0.04 | 0.041667550 | [0.039733005, 0.043661214] | [0.035000000, 0.045000000] | [0.040671937, 0.042673706] | Overlap; gap 0 |
| S069; Ischemic stroke, 12 months | -1.84 (-3.45 to -0.23); 0.03 | 0.025093595 | [0.024256456, 0.025950216] | [0.025000000, 0.035000000] | [0.024644060, 0.025547363] | Overlap; gap 0 |
| S071; Hemorrhagic stroke, 12 months | -0.08 (-0.71 to 0.55); 0.80 | 0.803450268 | [0.789811729, 0.816932748] | [0.795000000, 0.805000000] | [0.791441212, 0.815505906] | Overlap; gap 0 |
| S073; Myocardial infarction, 12 months | -0.13 (-0.46 to 0.21); 0.45 | 0.446906154 | [0.422666664, 0.471171043] | [0.445000000, 0.455000000] | [0.446906154, 0.471171043] | Overlap; gap 0 |
| S075; Vascular death, 12 months | -1.94 (-3.26 to -0.62); 0.004 | 0.003969780 | [0.003744049, 0.004205958] | [0.003500000, 0.004500000] | [0.003834005, 0.004108833] | Overlap; gap 0 |

For each of the eleven comparison rows the independent-input and centered intervals overlap the printed P interval, hence the discrepancy and relative discrepancy are both zero. For S059/C005 both constructions have the same lower bound and the positive gap reported above. Rounded central values alone do not establish compatibility for several comparison rows; their half-unit input envelopes are essential.

**Necessary inputs available:** Yes for direct-source tuple matching and the supported diagnostic: all twelve adjusted absolute-difference/95%-CI/P tuples, printed decimal precision, 95% confidence level, two-sided tests, adjustment context and exact column pairing are supplied. The complete same-display comparison is available and reproduced.

**Exact missing inputs or definitions:** The actual difference-specific confidence-interval formula, paired P-value test and null statistic, whether CI and P use the same variance estimator/estimand/model dataset, model covariance and unrounded output, and patient-level event/censoring times with covariate/cluster records. These prevent asserting the authors' construction or recreating the fitted adjusted estimates. They do not prevent reproducing the displayed tuple and diagnostic mismatch supported by the other rows.

**Source-grounded alternative interpretation:** The P may derive from a test, variance estimator, confidence construction, dataset or estimand distinct from the displayed difference interval. The source's adjusted time-to-event and Cox context supports the possibility of several inferential procedures, while the separate HR/P pair visibly supplies a distinct contrast. No row-specific difference procedure is identified, and the HR P=.02 is not the printed P adjacent to the difference. An alternative method could explain the tuple, but its identity and linkage are not supplied. No intended replacement value or preferred analysis is proposed.

**Direct observation versus inferred explanation:** Direct observation is the p.6 tuple −1.43 (−2.33 to −0.54) with adjacent 0.001, the eleven supporting tuples, and the p.7/main p.4 context. The calculated fact is disjoint diagnostic versus printed P intervals under the empirically supported normal-Wald relation, including exact symmetric centering. That this relation was actually used by the authors, that a different dataset was used, or how the printed tuple was produced are explanations requiring evidence; none is asserted. The extracted numerical P and its relationship to the adjusted difference's inferential precision are affected, while the displayed significance conclusion is unchanged.

**Classification confirmation:** All source and comparator locations are **REPORT** by their completed-trial content. Primary relationship type **S_W**; all relationships **S_W**; review domain **statistical_results**. The conflicting tuple and all supporting difference rows lie within one results supplement; this is an estimate/interval/test issue. Main p.4 merely corroborates inference conventions and p.7 merely explains adjustment. Neither adds a conflicting S_C relationship. No PLAN content is compared, so P_R/P_P are absent. S_W is therefore the highest and only applicable relationship under precedence P_R > P_P > S_C > S_W. No classification correction is needed. **Classification ambiguity:** None for source roles, relationship or domain; the actual inference construction remains unresolved.

**Evidence state:** **reproduced**. Determining recheck fact: direct current-PDF rendering and extraction confirm C005's registered tuple and pairing; the independently reproduced normal-Wald P envelope remains above the printed P interval with relative gap 0.076789228826, while all eleven support rows overlap under the same calculation. No registered C005 value or source location required transcription correction. Restoring trailing zeros in the support-screen presentation is transparently documented above and does not change the already-correct half-unit arithmetic.

**Exact remaining human question:** Which difference-specific confidence-interval and testing procedures produced −1.43 (95% CI −2.33 to −0.54) with P=0.001 for three-month vascular death, and how does that pairing reconcile with the two-sided normal-Wald relationship supported by all eleven other absolute-difference rows of eTable 3?

### C005 derivative provenance

Compute device CPU, as recorded in tooling_record.md. Source PDFs and every pre-existing derivative remain unchanged. The four uniquely named new derivatives below were generated directly from supplied supplement pages; both PNGs were visually inspected. Main p.4 derivatives were generated earlier in this same workflow by /root/recheck; both were reread here, with the PNG visually inspected.

| Supplied source | Physical PDF page | Derivative below preprocessing/ | Engine | Version | Device | Operation |
|---|---:|---|---|---|---|---|
| joi180070supp2_prod.pdf | 6 | recheck5-supp-p6.txt | pdftotext, Poppler | 25.03.0 | CPU | Fresh direct layout extraction |
| joi180070supp2_prod.pdf | 6 | recheck5-supp-p6.png | pdftoppm, Poppler | 25.03.0 | CPU | Fresh direct rendering, 150 dpi |
| joi180070supp2_prod.pdf | 7 | recheck5-supp-p7.txt | pdftotext, Poppler | 25.03.0 | CPU | Fresh direct layout extraction |
| joi180070supp2_prod.pdf | 7 | recheck5-supp-p7.png | pdftoppm, Poppler | 25.03.0 | CPU | Fresh direct rendering, 150 dpi |
| jama_wang_2018_oi_180070.pdf | 4 | recheck-main-p4.txt | pdftotext, Poppler | 25.03.0 | CPU | Existing current-run direct layout extraction, reread |
| jama_wang_2018_oi_180070.pdf | 4 | recheck-main-p4.png | pdftoppm, Poppler | 25.03.0 | CPU | Existing current-run direct rendering, 120 dpi, visually inspected |

Fresh commands, separately instantiated for N=6 and N=7:
```text
pdftotext -layout -f N -l N joi180070supp2_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/recheck5-supp-pN.txt
pdftoppm -f N -l N -singlefile -r 150 -png joi180070supp2_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/recheck5-supp-pN
```
Both engines report version 25.03.0. All four extraction/render commands completed with exit code 0. No OCR or fallback capability was needed. Derivative limits: none affecting transcription; actual model data and difference-specific constructions remain unavailable as named above. Local evidence links are relative to this unique part's location; merging into verification/evidence_recheck.md requires changing source links from ../../../../ to ../../../.

