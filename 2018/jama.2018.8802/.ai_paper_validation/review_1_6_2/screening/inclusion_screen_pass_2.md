# Independent pass-2 inclusion screen

Runtime agent: /root/screen2. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN. Stage: inclusion_screener_pass_2.

Assigned scope: the sole new finding F-ST2-001 in checkers/statistical_pass_2.md, its empirical-support table, relationships S059/S117, and all twelve absolute-difference rows of eTable 3. The complete QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read. No legacy scientific conclusions, external sources, additional findings, nested agents, OCR, Python calculation, fresh rendering, or source/asset changes were used. Only this pass-2 working artifact is written; the coordinator appends its row to the canonical screening table and assigns the stable ID.

## Screening table

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-ST2-001 | statistics_pass_2 | pass_2 | INCLUDE | MEETS_THRESHOLD | C005 |

F-ST2-001 qualifies by Route A, category 1: the source-confirmed three-month vascular-death adjusted difference −1.43 (95% CI −2.33 to −0.54) and adjacent P=.001 do not reconcile under the two-sided normal-Wald relationship empirically supported by every other difference row of the same display, with independently recomputed half-unit diagnostic P bounds [0.001576789, 0.001913909] versus printed [0.0005, 0.0015] and relative gap 0.076789, while the actual unreported confidence/test construction remains a human question.

## Direct-source confirmation and scope

The current supplied [results supplement PDF p.6, eTable 3](../../../joi180070supp2_prod.pdf#page=6) was reread directly with CPU `pdftotext -layout -f 6 -l 7 joi180070supp2_prod.pdf -`, Poppler 25.03.0, to stdout; no duplicate derivative was saved. Its reusable page image .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-p06.png was visually inspected to confirm signs, row order and the two separate estimate/P column pairs. The historical renderer/version is unrecorded; direct current-PDF extraction independently confirms the values.

The three-month vascular-death row prints intervention 46/2400 (1.9%), control 67/2400 (2.8%), adjusted absolute difference −1.43 percentage points with 95% CI −2.33 to −0.54, and immediately adjacent P=0.001. Its separate HR is 0.62 (0.42–0.92), with a separate P=.02. The HR P is not the test paired with the absolute difference.

The [supplement adjustment footnote, PDF p.7](../../../joi180070supp2_prod.pdf#page=7), read in the same direct extraction, states adjustment for patient and hospital characteristics: age, gender, ischemic-stroke history, hypertension, diabetes, hyperlipidemia, atrial fibrillation, coronary disease/previous myocardial infarction, ever smoking, admission NIHSS, hospital grade, region, stroke unit, teaching status and neurological-ward beds.

The [main article Data Analysis, PDF p.4](../../../jama_wang_2018_oi_180070.pdf#page=4) was reread through this run's exact-source layout derivative preprocessing/recheck-main-p4.txt, produced directly by CPU Poppler 25.03.0. It states adjusted cumulative incidences and absolute differences with 95% CIs, P<.05 significance and two-sided tests; it describes time-to-event outcomes and Cox modeling, but does not name the difference-specific CI/test formula or identify a distinct construction for this eTable 3 row.

These locations are REPORT by content. The conflicting tuple is wholly within the results supplement: proposed primary relationship S_W; all relationships S_W; proposed review domain statistical_results; focus B. The main article supplies corroborating inferential conventions and adds no S_C conflict. This is a same-row estimate/interval/P check, rather than a cross-location comparison of peripheral secondary values, and route A1 cannot be removed under PERIPHERAL_COMPARISON. No crude recomputation of adjusted effects is used.

## Independent numerical reproduction

The diagnostic uses q=1.959963984540054, SE=(U−L)/(2q), z=|b|/SE and P=2Φ(−z). Normal probabilities were evaluated independently in JavaScript by composite Simpson integration of the standard-normal density, using 20,000 subintervals; a 10,000-subinterval repeat at the decisive lower P bound differs by approximately 1.5×10⁻¹⁴. This numerical check reconstructs a supported relationship from printed values and does not assert the authors used this undisclosed exact test or CI construction.

For S059, central SE=0.45664104, z≈3.13156257 and P=0.001738787. Half-unit inputs are b∈[−1.435,−1.425], L∈[−2.335,−2.325], U∈[−0.545,−0.535]. Their independently attainable width range is [1.780,1.800], giving z∈[3.103276309,3.160166649] and diagnostic P∈[0.001576789,0.001913909]. Printed .001 permits [0.0005,0.0015]; the minimum gap is 0.000076789 and relative gap is 0.076789>0.05. The independently evaluated normal tails refine the checker's approximate values by about 1.3×10⁻⁷ without changing its observation.

A symmetric-Wald construction also requires b=(L+U)/2. To test whether the broad independent-input envelope overstates support from other rows, the allowed (L,U) rectangle was intersected with the constraint 2b_low≤L+U≤2b_high; extrema of |q(L+U)/(U−L)| were evaluated at each permitted rectangle vertex and each intersection with those two linear boundaries. Its constrained S059 P envelope is [0.001576789,0.001777726], still disjoint from the printed P interval. Each of the other eleven difference rows retains overlap under this stricter, centered construction as well.

The complete same-display comparison follows; every printed tuple was read independently from the p.6 source and image, all b/L/U inputs receive ±.005, and each P receives half of its last displayed unit.

| Relationship; difference row | Printed b (L to U); paired P | Central diagnostic P | Independent-input P envelope | Printed P interval | Centered-Wald P envelope | Centered comparison |
|---|---|---:|---|---|---|---|
| S053; Ischemic stroke, 3 months | -0.57 (-1.91 to 0.76); 0.40 | 0.402683322 | [0.396798477, 0.408575678] | [0.395000000, 0.405000000] | [0.396798477, 0.402683322] | Overlap |
| S055; Hemorrhagic stroke, 3 months | -0.35 (-0.92 to 0.22); 0.23 | 0.228788052 | [0.218142721, 0.239603511] | [0.225000000, 0.235000000] | [0.222207459, 0.235506219] | Overlap |
| S057; Myocardial infarction, 3 months | -0.10 (-0.36 to 0.17); 0.48 | 0.459537248 | [0.428638325, 0.490435101] | [0.475000000, 0.485000000] | [0.459537248, 0.490435101] | Overlap |
| S059; Vascular death, 3 months | -1.43 (-2.33 to -0.54); 0.001 | 0.001738787 | [0.001576789, 0.001913909] | [0.000500000, 0.001500000] | [0.001576789, 0.001777726] | No overlap |
| S061; Ischemic stroke, 6 months | -1.40 (-2.82 to 0.02); 0.05 | 0.053315228 | [0.051641210, 0.055022111] | [0.045000000, 0.055000000] | [0.052469670, 0.054172138] | Overlap |
| S063; Hemorrhagic stroke, 6 months | -0.25 (-0.80 to 0.30); 0.38 | 0.372986726 | [0.359117819, 0.386923907] | [0.375000000, 0.385000000] | [0.363502921, 0.382622273] | Overlap |
| S065; Myocardial infarction, 6 months | -0.03 (-0.35 to 0.29); 0.86 | 0.854212231 | [0.827605378, 0.880159945] | [0.855000000, 0.865000000] | [0.830257707, 0.878301920] | Overlap |
| S067; Vascular death, 6 months | -1.06 (-2.08 to -0.04); 0.04 | 0.041667550 | [0.039733005, 0.043661214] | [0.035000000, 0.045000000] | [0.040671937, 0.042673706] | Overlap |
| S069; Ischemic stroke, 12 months | -1.84 (-3.45 to -0.23); 0.03 | 0.025093595 | [0.024256456, 0.025950216] | [0.025000000, 0.035000000] | [0.024644060, 0.025547363] | Overlap |
| S071; Hemorrhagic stroke, 12 months | -0.08 (-0.71 to 0.55); 0.80 | 0.803450268 | [0.789811729, 0.816932748] | [0.795000000, 0.805000000] | [0.791441212, 0.815505906] | Overlap |
| S073; Myocardial infarction, 12 months | -0.13 (-0.46 to 0.21); 0.45 | 0.446906154 | [0.422666664, 0.471171043] | [0.445000000, 0.455000000] | [0.446906154, 0.471171043] | Overlap |
| S075; Vascular death, 12 months | -1.94 (-3.26 to -0.62); 0.004 | 0.003969780 | [0.003744049, 0.004205958] | [0.003500000, 0.004500000] | [0.003834005, 0.004108833] | Overlap |

## Inclusion rationale and remaining human question

The diagnostic is empirically supported across all eleven comparison rows, including the sparse myocardial-infarction rows where the central recomputation alone would be insufficient and half-unit rounding is essential. The supplied scope explicitly permits a same-display reproducing method despite its unreported construction and excludes conditional observations only when the same display does not support the assumed method. F-ST2-001 is an interval/P compatibility issue under route A category 1; category 4 supplies the same-display methodological principle but is not substituted for category 1 because this finding concerns the paired P rather than solely an estimate or interval. The conservative gap independently exceeds the general .05 display rule as well. The printed CI excludes zero and P is below .05, so no reversal of significance is claimed; the affected extracted quantity is the numerical P and its relationship to the adjusted difference's inferential precision.

Possible explanations include a distinct test, confidence construction, variance estimator, dataset or estimand. None is separately specified for this row, and none is assumed absent as a factual claim. The numerical discrepancy and same-display support justify registration under the required doubt-about-printed-numbers rule, while the missing construction remains for human adjudication. This is distinct from the existing in-hospital mortality null-crossing candidate C004; the other stable candidates concern composite weighting, primary-analysis counts and time origin, so no same issue or repeated-pattern duplicate is demonstrated.

Exact human question: Which difference-specific confidence-interval and testing procedures produced −1.43 (−2.33 to −0.54) with P=.001 for three-month vascular death, and how does the pairing reconcile with the two-sided normal-Wald relationship supported by all eleven other absolute-difference rows of this eTable?

Counts: 1 finding screened; 1 included issue; 0 screened out; screened-out counts by reason code: none. Candidate ID remains PENDING for coordinator assignment; any assigned candidate remains Pending Human Adjudication. Limits: actual model covariance/output, difference-specific CI/test construction and patient-level event data are not supplied; historical page-image engine is unrecorded. These limits constrain inferential explanation, not direct-source reproduction of the printed tuple or the complete supported diagnostic calculation.


Coordinator formatting refinement from the fresh C005 recheck: support-table printed P strings0.40 and0.80 retain their actual trailing zeros; numerical values and the already-used±0.005 allowances are unchanged. C005 is reproduced without a source-value or location correction.
