# Workflow 1.6.2 Candidate Ledger

Every candidate is Pending Human Adjudication. Registration follows the independent initial inclusion screen, with no target count. C001-C014 follow the screen's documented source order: earliest substantive main-report locations, then PLAN-only and results-supplement-only locations. Stable IDs are never deleted. Evidence states and classifications reflect the fresh exact-source recheck. Inclusion-audit fields remain PENDING until the required fresh audit finalizes them.

## Classification table

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | statistical_results | S_W | S_W | REPORT DOC-001 pp. 1, 3 prose vs REPORT DOC-001 p. 6 Table 2 | reproduced | CONFIRMED | F-NUM-002 |
| C002 | statistical_results | S_C | S_C | REPORT DOC-001 pp. 1, 3 vs REPORT DOC-003 p. 15; REPORT DOC-003 p. 4 supplies the model | reproduced | CONFIRMED | F-XS-003 |
| C003 | statistical_results | S_W | S_W | REPORT DOC-001 p. 1 abstract vs REPORT DOC-001 pp. 3, 4, 7, 8 cohort and death displays | reproduced | CONFIRMED | F-NUM-001 |
| C004 | protocol_report | P_R | P_R, S_C, S_W | PLAN DOC-002 pp. 17, 26, 27, 29; REPORT DOC-001 pp. 2, 6; REPORT DOC-003 pp. 4, 15, 16 | reproduced | CONFIRMED | F-XS-004 |
| C005 | protocol_report | P_R | P_R | PLAN DOC-002 pp. 18, 29 vs REPORT DOC-001 pp. 1, 2, 7 | reproduced | CONFIRMED | F-XS-006 |
| C006 | protocol_report | P_R | P_R | PLAN DOC-002 pp. 18, 29, 30 vs REPORT DOC-001 pp. 1, 2, 8 | reproduced | CONFIRMED | F-XS-009 |
| C007 | protocol_report | P_R | P_R | PLAN DOC-002 pp. 26, 34 vs REPORT DOC-001 pp. 2, 3 and REPORT DOC-003 p. 4 | reproduced | CONFIRMED | F-XS-005 |
| C008 | protocol_report | P_R | P_R | PLAN DOC-002 pp. 30, 31, 34 vs REPORT DOC-001 pp. 3, 9 and REPORT DOC-003 pp. 4, 5, 6, 9; absence checked across all main/report-supplement pages | reproduced | CONFIRMED | F-XS-008 |
| C009 | protocol_report | P_R | P_R | PLAN DOC-002 p. 27 vs REPORT DOC-001 pp. 3, 6 and REPORT DOC-003 pp. 4, 5, 15 | reproduced | CONFIRMED | F-XS-007 |
| C010 | statistical_results | S_W | S_W | REPORT DOC-001 p. 6 medical medication OR cell vs all other binary OR cells on the same page; REPORT DOC-003 p. 4 is corroborating inference context only | reproduced | CONFIRMED | F-ST1-007 |
| C011 | protocol_report | P_R | P_R | PLAN DOC-002 pp. 26, 34, 35 vs REPORT DOC-001 pp. 1, 7 and REPORT DOC-003 pp. 6, 17, 19, 20, 21 | reproduced | CONFIRMED | F-XS-010 |
| C012 | plan_material | P_P | P_P | PLAN DOC-002 p. 26 A1/site definition vs PLAN DOC-002 pp. 28, 31 power/heterogeneity; REPORT DOC-001 pp. 2, 3 and REPORT DOC-003 p. 4 corroborate only | reproduced | CONFIRMED | F-XS-011 |
| C013 | plan_material | P_P | P_P | PLAN DOC-002 p. 55 randomized/intervention rows vs PLAN DOC-002 p. 56 attached dagger footnote; PLAN DOC-002 p. 27 corroborates row totals | reproduced | CONFIRMED | F-NUM-102 |
| C014 | statistical_results | S_W | S_W | REPORT DOC-003 p. 14 eTable 1 Other-race count, percentage, column denominator and footnotes | reproduced | CONFIRMED | F-NUM-101 |

## C001 — Positive HbA1c point and signed interval

Pending Human Adjudication.

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT DOC-001 pp. 1, 3 prose vs REPORT DOC-001 p. 6 Table 2
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-NUM-002
**Checker provenance including duplicate findings:** F-NUM-002, F-XS-002, F-ST1-009
**Qualifying route:** Route A, category 1
**Classification rationale:** Estimate/interval/sign consistency is statistical-results content within one REPORT. The table confirms signed changes; no PLAN comparison is part of this issue.
**Classification ambiguity:** Positive reduction magnitudes may intentionally accompany signed-change intervals.

**Positive HbA1c point / signed interval.** Included finding F-NUM-002; duplicate provenance F-XS-002, F-ST1-009. Proposed statistical_results / S_W; all relationships S_W. REPORT [main page 1 abstract HbA1c changes](../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1), [page 3 Results HbA1c paragraph](../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), and [page 6 Table 2 HbA1c row/footnote b](../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6). The surgery point prints +1.6 in both prose locations; the CI is −1.8 to −1.3 and the table point −1.6. Even allowing rounding, positive point [1.55,1.65] and nearest possible negative upper limit [−1.35,−1.25] remain separated by at least 2.80; route A1 has no rounding exclusion. Medical +0.2 versus table −0.2 is a companion prose/table pattern; +0.2 alone is within its [−.5,.2] interval. Alternative: prose intentionally gives reduction magnitudes and intervals signed changes. Human question: which scale applies to the paired prose points and intervals?

## C002 — Year-12 HbA1c P value

Pending Human Adjudication.

**Review domain:** statistical_results
**Relationship type:** S_C
**All relationships:** S_C
**Compared document roles:** REPORT DOC-001 pp. 1, 3 vs REPORT DOC-003 p. 15; REPORT DOC-003 p. 4 supplies the model
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-XS-003
**Checker provenance including duplicate findings:** F-XS-003, F-ST1-001
**Qualifying route:** Route B
**Classification rationale:** The same printed inferential result differs between two retrospective REPORT documents. Agreeing main p1/p3 copies do not create S_W.
**Classification ambiguity:** Different test conventions could be attached to the same displayed interval, but none is identified.

**Year-12 HbA1c P value.** Included F-XS-003; duplicate provenance F-ST1-001. Proposed statistical_results / S_C; all relationships S_C. REPORT [main page 1 abstract](../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1), [page 3 Results](../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), [results supplement page 15 eTable 2 HbA1c](../../joi240004supp2_prod_1721756962.82552.pdf#page=15), and [supplement page 4 ITT model](../../joi240004supp2_prod_1721756962.82552.pdf#page=4). The same visit/population/contrast and −1.1 [−1.7,−.5] have .002 and <.001. This is not an interval-versus-significance issue: both tests are significant. Half-unit .002 range [.0015,.0025] and <.001 range [0,.001) have gap at least .0005 and relative discrepancy at least .25. Alternative: distinct test conventions could attach a different P value to the same interval. Main page 9 identifies the July 24 correction as the ClinicalTrials.gov link only, so that notice does not substantiate a numerical revision. Human question: which P/test belongs to this contrast?

## C003 — Pooled mortality percentage

Pending Human Adjudication.

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT DOC-001 p. 1 abstract vs REPORT DOC-001 pp. 3, 4, 7, 8 cohort and death displays
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-NUM-001
**Checker provenance including duplicate findings:** F-NUM-001, F-XS-001
**Qualifying route:** Route A, category 3
**Classification rationale:** Count/denominator/percentage accounting is statistical-results content entirely within one REPORT.
**Classification ambiguity:** An unidentified different pooled risk set would change the denominator.

**Pooled mortality percentage.** Included F-NUM-001; duplicate provenance F-XS-001. Proposed statistical_results / S_W; all relationships S_W. REPORT [main page 1 abstract](../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1), [page 3 enrollment](../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), [page 4 Table 1 headers](../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=4), [page 7 deaths paragraph](../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=7), and [page 8 Table 3 headers/Death row](../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=8). Exact 4/262 gives 1.526718%; complete half-unit range [1.333333,1.720841]% versus [2.15,2.25]% gives .429159 percentage-point gap and .195072 relative discrepancy. Independently allowing half-unit inputs in both arm counts/denominators still gives [1.140684,1.915709]%, gap .234291/2.2=.106496. Arm counts 2/96 and 2/166 individually reproduce 2.1% and 1.2%. Alternative: a separate unidentified pooled risk-set denominator. Human question: which denominator and mortality quantity produce 2.2%?

## C004 — Primary HbA1c response scale

Pending Human Adjudication.

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R, S_C, S_W
**Compared document roles:** PLAN DOC-002 pp. 17, 26, 27, 29; REPORT DOC-001 pp. 2, 6; REPORT DOC-003 pp. 4, 15, 16
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-XS-004
**Checker provenance including duplicate findings:** F-XS-004, F-ST1-002
**Qualifying route:** Route B
**Classification rationale:** P_R is independently supported by prospective percent-response versus tabulated net-response definitions; S_W by main p2 percent label versus main p6 net-change footnote; S_C by main p2 percent label versus supplementary p15 net-change footnote. P_R outranks S_C and S_W. The plan is an actual compared specification, not mere corroboration.
**Classification ambiguity:** “Percent change” may be used loosely in main methods or may represent an undisclosed scale amendment.

**Primary HbA1c response scale.** Included F-XS-004; duplicate provenance F-ST1-002. Proposed protocol_report / P_R; all relationships P_R, S_C, S_W. PLAN [page 17 endpoint](../../joi240004supp1_prod_1721756962.80052.pdf#page=17), [page 26 A1 response](../../joi240004supp1_prod_1721756962.80052.pdf#page=26), [page 27 power inputs](../../joi240004supp1_prod_1721756962.80052.pdf#page=27), and [page 29 Table A1](../../joi240004supp1_prod_1721756962.80052.pdf#page=29); REPORT [main page 2 endpoint/methods](../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=2), [main page 6 Table 2/footnote b](../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), [supplement page 4 model](../../joi240004supp2_prod_1721756962.82552.pdf#page=4), [page 15 eTable 2/footnote b](../../joi240004supp2_prod_1721756962.82552.pdf#page=15), and [page 16 eTable 2 continuation](../../joi240004supp2_prod_1721756962.82552.pdf#page=16). Plan percent change is numerically instantiated by −20%/−15% power assumptions; tables explicitly distinguish net HbA1c change from other outcomes' relative change. This is quantity identity, not crude/model arithmetic; numerical display precision is inapplicable. Alternative: a scale amendment or loose main-method label. Human question: did the primary response change from relative-percent to net percentage-point HbA1c change, and what produced the primary/year-12 contrasts?

## C005 — Remission medication-free window

Pending Human Adjudication.

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN DOC-002 pp. 18, 29 vs REPORT DOC-001 pp. 1, 2, 7
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-XS-006
**Checker provenance including duplicate findings:** F-XS-006, F-ST1-005
**Qualifying route:** Route B
**Classification rationale:** The key remission endpoint's prospective and retrospective medication-free windows differ in explicit specification. The abbreviated Figure 3 definition is not a separate REPORT conflict.
**Classification ambiguity:** An unsupplied operational definition or amendment could contain the reported duration.

**Remission medication-free window.** Included F-XS-006; duplicate provenance F-ST1-005. Proposed protocol_report / P_R; all relationships P_R. PLAN [page 18 remission item](../../joi240004supp1_prod_1721756962.80052.pdf#page=18) and [page 29 Table A1](../../joi240004supp1_prod_1721756962.80052.pdf#page=29); REPORT [main page 2 definition](../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=2), [page 1 abstract remission rates](../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1), and [page 7 Figure 3 caption](../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=7). Off medication and HbA1c<6.5 match, but only report explicitly requires at least 3 months. Do not infer a plan zero-month rule or any changed event count; the added criterion affects endpoint matching. Alternatives: an operational definition, an amendment, or the later definition referenced by the report but not supplied as its plan. Human question: what prospective window underlies the key remission rates/OR?

## C006 — Cardiovascular outcome status

Pending Human Adjudication.

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN DOC-002 pp. 18, 29, 30 vs REPORT DOC-001 pp. 1, 2, 8
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-XS-009
**Checker provenance including duplicate findings:** F-XS-009
**Qualifying route:** Route A, category 5
**Classification rationale:** This compares prospective outcome status with the report's stated secondary hierarchy; it is not a same-document count comparison.
**Classification ambiguity:** Safety and secondary status could coexist; plan p18 permits some dual-status endpoints without identifying this one.

**Cardiovascular outcome status.** Included F-XS-009. Proposed protocol_report / P_R; all relationships P_R. PLAN [page 18 secondary endpoint list/section 4.4](../../joi240004supp1_prod_1721756962.80052.pdf#page=18), [page 29 Table A1](../../joi240004supp1_prod_1721756962.80052.pdf#page=29), and [page 30 Table A1 continuation](../../joi240004supp1_prod_1721756962.80052.pdf#page=30); REPORT [main page 2 other secondary outcomes](../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=2), [page 1 abstract cardiovascular finding](../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1), and [page 8 cardiovascular rows](../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=8). Exact plan table labels major adverse cardiovascular events Safety, separately from efficacy stroke/retinopathy/nephropathy/foot-ulcer; the report explicitly labels major adverse cardiovascular events secondary. Section 4.4 says some study outcomes are also secondary, without identifying cardiovascular events as such. Preserve dual safety/secondary status as an alternative; do not invent composite changes. Human question: which prespecified hierarchy/status applies to the abstract cardiovascular outcome?

## C007 — Primary baseline adjustment

Pending Human Adjudication.

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN DOC-002 pp. 26, 34 vs REPORT DOC-001 pp. 2, 3 and REPORT DOC-003 p. 4
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-XS-005
**Checker provenance including duplicate findings:** F-XS-005
**Qualifying route:** Route B
**Classification rationale:** The prospective primary covariate specification differs from the reported primary specification. Agreeing report methods and within-plan primary/sensitivity distinctions do not add S_C/S_W/P_P.
**Classification ambiguity:** The reported primary could be a selected planned sensitivity model or reflect an unsupplied amendment.

**Primary baseline adjustment.** Included F-XS-005. Proposed protocol_report / P_R; all relationships P_R. PLAN [page 26 A1 and its 4-dimensional site-only Z](../../joi240004supp1_prod_1721756962.80052.pdf#page=26) and [page 34 further baseline sensitivities](../../joi240004supp1_prod_1721756962.80052.pdf#page=34); REPORT [main page 2 statistical analysis](../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=2), [page 3 continuation](../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), and [supplement page 4 primary fixed effects](../../joi240004supp2_prod_1721756962.82552.pdf#page=4). The explicit prospective primary and further-sensitivity lists differ from baseline HbA1c in the reported primary list. This is separate from missing expanded sensitivities: it concerns which specification generated the main estimate, not whether additional results were supplied. Alternative: selected planned sensitivity or amendment. Human question: which planned/amended primary specification generated −1.4 and its CI/P?

## C008 — Planned primary sensitivity package not reported

Pending Human Adjudication.

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN DOC-002 pp. 30, 31, 34 vs REPORT DOC-001 pp. 3, 9 and REPORT DOC-003 pp. 4, 5, 6, 9; absence checked across all main/report-supplement pages
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-XS-008
**Checker provenance including duplicate findings:** F-XS-008, F-ST1-004
**Qualifying route:** Route A, category 5
**Classification rationale:** Explicitly prespecified primary sensitivity results have no supplied corresponding report results. All compared obligations are PLAN-to-REPORT, consolidated as one absent sensitivity package.
**Classification ambiguity:** Unsupplied results or a final plan amendment may exist; censoring weights could be one under the reported random-censoring assumption.

**Planned primary sensitivity package not reported.** Included F-XS-008; duplicate provenance F-ST1-004. Proposed protocol_report / P_R; all relationships P_R. PLAN [page 30 MICE/Rubin/pattern mixture and IPTW](../../joi240004supp1_prod_1721756962.80052.pdf#page=30), [page 31 final treatment×censoring weight and postcrossover discard](../../joi240004supp1_prod_1721756962.80052.pdf#page=31), and [page 34 extra baseline HbA1c/BMI/imbalance sensitivities](../../joi240004supp1_prod_1721756962.80052.pdf#page=34); REPORT [main page 3 sensitivity/missingness and primary sensitivity result](../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), [page 9 limitations](../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=9), [supplement page 4 methods](../../joi240004supp2_prod_1721756962.82552.pdf#page=4), [page 5 complete treatment-IPW formula](../../joi240004supp2_prod_1721756962.82552.pdf#page=5), [page 6 missingness continuation](../../joi240004supp2_prod_1721756962.82552.pdf#page=6), and [page 9 eFigure 2](../../joi240004supp2_prod_1721756962.82552.pdf#page=9). Complete supplied main pages 1–11 and results supplement pages 1–22 contain no results for MICE, pattern mixture, outcomes-discarded-after-crossover, or expanded BMI/imbalance primary sensitivities. The stated treatment-IPW analysis reassigns treatment after crossover and does not equal outcome discard; its printed weight formula lacks a censoring-weight factor. MAR could make the latter factor one, which is an alternative requiring mapping to the plan, not an inferred numerical conflict. No claim about analyses actually conducted is made. Human question: where are these planned primary results or their supplied replacement/amendment?

## C009 — Planned binary A2 and reported GEE

Pending Human Adjudication.

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN DOC-002 p. 27 vs REPORT DOC-001 pp. 3, 6 and REPORT DOC-003 pp. 4, 5, 15
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-XS-007
**Checker provenance including duplicate findings:** F-XS-007, F-ST1-003
**Qualifying route:** Route A, category 5
**Classification rationale:** The plan specifies the main key-secondary model A2; the report supplies another model family and no A2 result. Report method descriptions agree, so no REPORT-to-REPORT conflict is present.
**Classification ambiguity:** An unsupplied final analysis amendment may define the GEE replacement.

**Planned binary A2 versus reported GEE.** Included F-XS-007; duplicate provenance F-ST1-003. Proposed protocol_report / P_R; all relationships P_R. PLAN [page 27 A2/main binary secondary test](../../joi240004supp1_prod_1721756962.80052.pdf#page=27); REPORT [main page 3 GEE/sandwich analysis](../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), [page 6 binary outcome rows](../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), [supplement page 4 binary GEE](../../joi240004supp2_prod_1721756962.82552.pdf#page=4), [page 5 continuation](../../joi240004supp2_prod_1721756962.82552.pdf#page=5), and [page 15 year-12 binary rows](../../joi240004supp2_prod_1721756962.82552.pdf#page=15). A2 is explicitly patient-random-effect logistic and the main secondary test includes remission; GEE/sandwich is explicitly the reported family. This is an observable replacement/absence of the planned key analysis, not a preference between models or a comparison with crude odds. Alternative: a final plan amendment. Human question: which specification supports the GEE replacement and what conditioning/estimand belongs to the reported ORs?

## C010 — Medical medication OR interval pattern

Pending Human Adjudication.

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT DOC-001 p. 6 medical medication OR cell vs all other binary OR cells on the same page; REPORT DOC-003 p. 4 is corroborating inference context only
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-ST1-007
**Checker provenance including duplicate findings:** F-ST1-007
**Qualifying route:** Route A, category 4
**Classification rationale:** One estimate/interval cell does not reproduce a method that reproduces every other binary cell within the same REPORT table. The supplementary GEE/sandwich description does not conflict with the table and adds no S_C.
**Classification ambiguity:** The anomalous cell could use an explicitly different asymmetric interval construction or contrast, neither specified in the supplied display.

**Medical medication OR interval pattern.** Included F-ST1-007. Proposed statistical_results / S_W; all relationships S_W. REPORT [main page 6 Table 2 medical medication cell, all other binary cells, and footnotes](../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6); [supplement page 4 GEE/sandwich methods](../../joi240004supp2_prod_1721756962.82552.pdf#page=4) corroborates inference but creates no conflicting S_C relationship. Independently applying sqrt(lower×upper) with every cell's actual half-unit bounds reproduces all 11 other within-group and all 6 between-group OR points: the ranges overlap each respective point interval, including the coarsely printed remission bounds and surgery HbA1c<7 upper bound 11.4. The medical medication cell alone gives [.127769323,.221641603] versus [.095,.105], gap .022769323/.10=.227693233. This is route A4, not a crude-odds comparison or a significant/nonsignificant conflict. Alternatives: a distinct asymmetric interval procedure, another contrast, or an unmatched bound; no alternate numerical value is selected. Human question: which interval construction produced .10 [.01,3.27] and why does it differ from the reproducing pattern?

## C011 — Vascular and safety test mapping

Pending Human Adjudication.

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN DOC-002 pp. 26, 34, 35 vs REPORT DOC-001 pp. 1, 7 and REPORT DOC-003 pp. 6, 17, 19, 20, 21
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-XS-010
**Checker provenance including duplicate findings:** F-XS-010, F-ST1-008
**Qualifying route:** Route B
**Classification rationale:** This is an unresolved correspondence between prospective vascular/safety analysis and reported result tests. REPORT descriptions agree with each other, so no S_C/S_W is added. The separate baseline CMH paragraph is contextual, not proof of event strata.
**Classification ambiguity:** CMH strata are unspecified; “chi-squared” may abbreviate CMH, sparse-outcome Fisher substitution may apply, or planned composites and reported individual-row tests may differ.

**Vascular/safety test mapping.** Included F-XS-010; duplicate provenance F-ST1-008. Proposed protocol_report / P_R; all relationships P_R. PLAN [page 34 Aim 2 CMH and safety same-manner statement](../../joi240004supp1_prod_1721756962.80052.pdf#page=34), [page 35 continuation](../../joi240004supp1_prod_1721756962.80052.pdf#page=35), and [page 26 separate baseline CMH paragraph](../../joi240004supp1_prod_1721756962.80052.pdf#page=26); REPORT [main page 7 event/procedure narrative](../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=7), [page 1 abstract cardiovascular finding](../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1), [supplement page 6 chi-squared/Fisher statement](../../joi240004supp2_prod_1721756962.82552.pdf#page=6), [page 17 nutritional tests](../../joi240004supp2_prod_1721756962.82552.pdf#page=17), [page 19 eTable 5 abdominal pain and dysphagia cells](../../joi240004supp2_prod_1721756962.82552.pdf#page=19), [page 20 eTable 5 footnote b](../../joi240004supp2_prod_1721756962.82552.pdf#page=20), and [page 21 eTable 6 footnote b](../../joi240004supp2_prod_1721756962.82552.pdf#page=21). Exact sources name CMH prospectively and chi-squared/Fisher retrospectively without mapping them. The source's event paragraph does not name CMH strata, so site-stratified versus unstratified is not an independently established fact and must not become the candidate title or numeric premise. Alternatives: chi-squared abbreviates CMH, exact tests substitute for sparse outcomes, or planned composites and listed row tests are distinct. Reported example P values are abdominal pain .02, dysphagia .005 and pooled crossover/conversion/revision <.001. Human question: which reported tests instantiate the planned vascular/safety CMH analyses and what specification explains the mapping or change?

## C012 — Fixed site and power variance specification

Pending Human Adjudication.

**Review domain:** plan_material
**Relationship type:** P_P
**All relationships:** P_P
**Compared document roles:** PLAN DOC-002 p. 26 A1/site definition vs PLAN DOC-002 pp. 28, 31 power/heterogeneity; REPORT DOC-001 pp. 2, 3 and REPORT DOC-003 p. 4 corroborate only
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-XS-011
**Checker provenance including duplicate findings:** F-XS-011, F-ST1-006
**Qualifying route:** Route B
**Classification rationale:** Both conflicting specifications are inside the prospective PLAN. The fixed-site REPORT model agrees with one side and is not a PLAN-to-REPORT inconsistency, so P_R is not added.
**Classification ambiguity:** A finite-site coefficient spread or a separate generative random-site model could define σ_b, but the plan does not identify either correspondence.

**Fixed site / power variance specification.** Included F-XS-011; duplicate provenance F-ST1-006. Proposed plan_material / P_P; all relationships P_P. PLAN [page 26 A1/site-term definition](../../joi240004supp1_prod_1721756962.80052.pdf#page=26), [page 28 primary power variance components](../../joi240004supp1_prod_1721756962.80052.pdf#page=28), and [page 31 distribution/heterogeneity paragraph](../../joi240004supp1_prod_1721756962.80052.pdf#page=31); REPORT [main page 2](../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=2), [main page 3 fixed-effect continuation](../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), and [supplement page 4 fixed-site model](../../joi240004supp2_prod_1721756962.82552.pdf#page=4) only corroborate fixed-site analysis and add no P_R relationship. A1 calls b_i fixed, whereas its power paragraph calls σ_b=.06 a variance component estimated by fitting the mixed model under A1. The separate duplicated fixed-site coefficients are not the issue because plan page 27 permits identifiability constraints. Alternatives: finite-site fixed-coefficient spread or distinct generative random-site simulation; neither parameter definition is supplied. Human question: what does σ_b=.06 represent and how does the stated simulation model correspond to fixed-site A1?

## C013 — Appendix randomization-dropout accounting

Pending Human Adjudication.

**Review domain:** plan_material
**Relationship type:** P_P
**All relationships:** P_P
**Compared document roles:** PLAN DOC-002 p. 55 randomized/intervention rows vs PLAN DOC-002 p. 56 attached dagger footnote; PLAN DOC-002 p. 27 corroborates row totals
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-NUM-102
**Checker provenance including duplicate findings:** F-NUM-102
**Qualifying route:** Route A, category 3
**Classification rationale:** The prospective study-population enrollment accounting is inside one PLAN display continued across two pages, with a footnote explicitly attached to initiation. It bears on the planned enrollment pool; final REPORT cohort numbers are not compared.
**Classification ambiguity:** The 38 dropouts may refer to a different historical snapshot/population or category, but the attached display identifies none.

**Appendix randomization-dropout accounting.** Included F-NUM-102. Proposed plan_material / P_P; all relationships P_P. PLAN [page 55 Appendix 2 randomized/intervention rows and attached dagger](../../joi240004supp1_prod_1721756962.80052.pdf#page=55) and [page 56 continued display/dagger text](../../joi240004supp1_prod_1721756962.80052.pdf#page=56); [page 27 primary power population paragraph](../../joi240004supp1_prod_1721756962.80052.pdf#page=27) corroborates 355 randomized/325 initiated, rather than creating another comparison. Exact source title is Initial Trials: Enrolled Participants and the footnote defines intervention initiation followed immediately by total 38 randomization dropouts not followed or eligible. Sums 155+69+43+45+43=355 and 154+61+38+40+32=325 give 30; half-unit sum ranges [352.5,357.5] minus [322.5,327.5] give [25,35], separated from [37.5,38.5] by .065789 relative to 38. This is count accounting within one display of the planned enrollment pool, not a comparison of unrelated historical calendars or final enrollment cohorts; route A3 applies. Alternatives: footnote refers to another historical snapshot/population or dropout is a distinct category, but neither is identified by the attached display. Do not compare this total directly with final-report population/withdrawal counts. Human question: which population/time point supplies 38, and how does it reconcile with the displayed randomization/initiation accounting?

## C014 — Other race count and percentage

Pending Human Adjudication.

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT DOC-003 p. 14 eTable 1 Other-race count, percentage, column denominator and footnotes
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-NUM-101
**Checker provenance including duplicate findings:** F-NUM-101
**Qualifying route:** Route A, category 3
**Classification rationale:** Count/percentage/denominator conflict is within one REPORT display. The main baseline table is not a comparator, so this is not a peripheral cross-copy baseline comparison and adds no S_C.
**Classification ambiguity:** An alternative race-specific denominator or count is possible but unspecified.

**Other race count and percentage.** Included F-NUM-101. Proposed statistical_results / S_W; all relationships S_W. REPORT [supplement page 14 eTable 1 7-year N=262, race rows and footnotes](../../joi240004supp2_prod_1721756962.82552.pdf#page=14). Footnote a explicitly says n (%), and footnote b says all study participants reached 7 years; no alternative racial denominator is printed. The exact Other entry is 4 (1.9); half-unit inputs give [1.333333,1.720841]% and printed [1.85,1.95]%, gap .129159/1.9=.067978. This within-display arithmetic is not a peripheral cross-copy baseline comparison. Neighboring 81/176 counts sum with 4 to 261, a corroborating detail rather than an independently included small-total discrepancy. Alternative: another count or an unstated denominator; no corrected value is assigned. Human question: which Other-race count, denominator and percentage apply?

