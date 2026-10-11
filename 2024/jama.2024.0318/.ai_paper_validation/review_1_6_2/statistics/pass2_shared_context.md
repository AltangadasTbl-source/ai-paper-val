# Workflow 1.6.2 Candidate Ledger

Every candidate is Pending Human Adjudication. Registration follows the independent initial inclusion screen, with no target count. C001-C014 follow the screen's documented source order: earliest substantive main-report locations, then PLAN-only and results-supplement-only locations. Stable IDs are never deleted. Evidence states and classifications reflect the fresh exact-source recheck. Inclusion-audit fields remain PENDING until the required fresh audit finalizes them.

## Classification table

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | statistical_results | S_W | S_W | REPORT DOC-001 pp. 1, 3 prose vs REPORT DOC-001 p. 6 Table 2 | reproduced | PENDING | F-NUM-002 |
| C002 | statistical_results | S_C | S_C | REPORT DOC-001 pp. 1, 3 vs REPORT DOC-003 p. 15; REPORT DOC-003 p. 4 supplies the model | reproduced | PENDING | F-XS-003 |
| C003 | statistical_results | S_W | S_W | REPORT DOC-001 p. 1 abstract vs REPORT DOC-001 pp. 3, 4, 7, 8 cohort and death displays | reproduced | PENDING | F-NUM-001 |
| C004 | protocol_report | P_R | P_R, S_C, S_W | PLAN DOC-002 pp. 17, 26, 27, 29; REPORT DOC-001 pp. 2, 6; REPORT DOC-003 pp. 4, 15, 16 | reproduced | PENDING | F-XS-004 |
| C005 | protocol_report | P_R | P_R | PLAN DOC-002 pp. 18, 29 vs REPORT DOC-001 pp. 1, 2, 7 | reproduced | PENDING | F-XS-006 |
| C006 | protocol_report | P_R | P_R | PLAN DOC-002 pp. 18, 29, 30 vs REPORT DOC-001 pp. 1, 2, 8 | reproduced | PENDING | F-XS-009 |
| C007 | protocol_report | P_R | P_R | PLAN DOC-002 pp. 26, 34 vs REPORT DOC-001 pp. 2, 3 and REPORT DOC-003 p. 4 | reproduced | PENDING | F-XS-005 |
| C008 | protocol_report | P_R | P_R | PLAN DOC-002 pp. 30, 31, 34 vs REPORT DOC-001 pp. 3, 9 and REPORT DOC-003 pp. 4, 5, 6, 9; absence checked across all main/report-supplement pages | reproduced | PENDING | F-XS-008 |
| C009 | protocol_report | P_R | P_R | PLAN DOC-002 p. 27 vs REPORT DOC-001 pp. 3, 6 and REPORT DOC-003 pp. 4, 5, 15 | reproduced | PENDING | F-XS-007 |
| C010 | statistical_results | S_W | S_W | REPORT DOC-001 p. 6 medical medication OR cell vs all other binary OR cells on the same page; REPORT DOC-003 p. 4 is corroborating inference context only | reproduced | PENDING | F-ST1-007 |
| C011 | protocol_report | P_R | P_R | PLAN DOC-002 pp. 26, 34, 35 vs REPORT DOC-001 pp. 1, 7 and REPORT DOC-003 pp. 6, 17, 19, 20, 21 | reproduced | PENDING | F-XS-010 |
| C012 | plan_material | P_P | P_P | PLAN DOC-002 p. 26 A1/site definition vs PLAN DOC-002 pp. 28, 31 power/heterogeneity; REPORT DOC-001 pp. 2, 3 and REPORT DOC-003 p. 4 corroborate only | reproduced | PENDING | F-XS-011 |
| C013 | plan_material | P_P | P_P | PLAN DOC-002 p. 55 randomized/intervention rows vs PLAN DOC-002 p. 56 attached dagger footnote; PLAN DOC-002 p. 27 corroborates row totals | reproduced | PENDING | F-NUM-102 |
| C014 | statistical_results | S_W | S_W | REPORT DOC-003 p. 14 eTable 1 Other-race count, percentage, column denominator and footnotes | reproduced | PENDING | F-NUM-101 |

## C001 — Positive HbA1c point and signed interval

Pending Human Adjudication.

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT DOC-001 pp. 1, 3 prose vs REPORT DOC-001 p. 6 Table 2
**Evidence state:** reproduced
**Inclusion audit:** PENDING
**Finding IDs:** F-NUM-002
**Checker provenance including duplicate findings:** F-NUM-002, F-XS-002, F-ST1-009
**Qualifying route:** Route A, category 1
**Classification rationale:** Estimate/interval/sign consistency is statistical-results content within one REPORT. The table confirms signed changes; no PLAN comparison is part of this issue.
**Classification ambiguity:** Positive reduction magnitudes may intentionally accompany signed-change intervals.

**Positive HbA1c point / signed interval.** Included finding F-NUM-002; duplicate provenance F-XS-002, F-ST1-009. Proposed statistical_results / S_W; all relationships S_W. REPORT [main page 1 abstract HbA1c changes](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1), [page 3 Results HbA1c paragraph](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), and [page 6 Table 2 HbA1c row/footnote b](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6). The surgery point prints +1.6 in both prose locations; the CI is −1.8 to −1.3 and the table point −1.6. Even allowing rounding, positive point [1.55,1.65] and nearest possible negative upper limit [−1.35,−1.25] remain separated by at least 2.80; route A1 has no rounding exclusion. Medical +0.2 versus table −0.2 is a companion prose/table pattern; +0.2 alone is within its [−.5,.2] interval. Alternative: prose intentionally gives reduction magnitudes and intervals signed changes. Human question: which scale applies to the paired prose points and intervals?

## C002 — Year-12 HbA1c P value

Pending Human Adjudication.

**Review domain:** statistical_results
**Relationship type:** S_C
**All relationships:** S_C
**Compared document roles:** REPORT DOC-001 pp. 1, 3 vs REPORT DOC-003 p. 15; REPORT DOC-003 p. 4 supplies the model
**Evidence state:** reproduced
**Inclusion audit:** PENDING
**Finding IDs:** F-XS-003
**Checker provenance including duplicate findings:** F-XS-003, F-ST1-001
**Qualifying route:** Route B
**Classification rationale:** The same printed inferential result differs between two retrospective REPORT documents. Agreeing main p1/p3 copies do not create S_W.
**Classification ambiguity:** Different test conventions could be attached to the same displayed interval, but none is identified.

**Year-12 HbA1c P value.** Included F-XS-003; duplicate provenance F-ST1-001. Proposed statistical_results / S_C; all relationships S_C. REPORT [main page 1 abstract](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1), [page 3 Results](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), [results supplement page 15 eTable 2 HbA1c](../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), and [supplement page 4 ITT model](../../../joi240004supp2_prod_1721756962.82552.pdf#page=4). The same visit/population/contrast and −1.1 [−1.7,−.5] have .002 and <.001. This is not an interval-versus-significance issue: both tests are significant. Half-unit .002 range [.0015,.0025] and <.001 range [0,.001) have gap at least .0005 and relative discrepancy at least .25. Alternative: distinct test conventions could attach a different P value to the same interval. Main page 9 identifies the July 24 correction as the ClinicalTrials.gov link only, so that notice does not substantiate a numerical revision. Human question: which P/test belongs to this contrast?

## C003 — Pooled mortality percentage

Pending Human Adjudication.

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT DOC-001 p. 1 abstract vs REPORT DOC-001 pp. 3, 4, 7, 8 cohort and death displays
**Evidence state:** reproduced
**Inclusion audit:** PENDING
**Finding IDs:** F-NUM-001
**Checker provenance including duplicate findings:** F-NUM-001, F-XS-001
**Qualifying route:** Route A, category 3
**Classification rationale:** Count/denominator/percentage accounting is statistical-results content entirely within one REPORT.
**Classification ambiguity:** An unidentified different pooled risk set would change the denominator.

**Pooled mortality percentage.** Included F-NUM-001; duplicate provenance F-XS-001. Proposed statistical_results / S_W; all relationships S_W. REPORT [main page 1 abstract](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1), [page 3 enrollment](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), [page 4 Table 1 headers](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=4), [page 7 deaths paragraph](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=7), and [page 8 Table 3 headers/Death row](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=8). Exact 4/262 gives 1.526718%; complete half-unit range [1.333333,1.720841]% versus [2.15,2.25]% gives .429159 percentage-point gap and .195072 relative discrepancy. Independently allowing half-unit inputs in both arm counts/denominators still gives [1.140684,1.915709]%, gap .234291/2.2=.106496. Arm counts 2/96 and 2/166 individually reproduce 2.1% and 1.2%. Alternative: a separate unidentified pooled risk-set denominator. Human question: which denominator and mortality quantity produce 2.2%?

## C004 — Primary HbA1c response scale

Pending Human Adjudication.

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R, S_C, S_W
**Compared document roles:** PLAN DOC-002 pp. 17, 26, 27, 29; REPORT DOC-001 pp. 2, 6; REPORT DOC-003 pp. 4, 15, 16
**Evidence state:** reproduced
**Inclusion audit:** PENDING
**Finding IDs:** F-XS-004
**Checker provenance including duplicate findings:** F-XS-004, F-ST1-002
**Qualifying route:** Route B
**Classification rationale:** P_R is independently supported by prospective percent-response versus tabulated net-response definitions; S_W by main p2 percent label versus main p6 net-change footnote; S_C by main p2 percent label versus supplementary p15 net-change footnote. P_R outranks S_C and S_W. The plan is an actual compared specification, not mere corroboration.
**Classification ambiguity:** “Percent change” may be used loosely in main methods or may represent an undisclosed scale amendment.

**Primary HbA1c response scale.** Included F-XS-004; duplicate provenance F-ST1-002. Proposed protocol_report / P_R; all relationships P_R, S_C, S_W. PLAN [page 17 endpoint](../../../joi240004supp1_prod_1721756962.80052.pdf#page=17), [page 26 A1 response](../../../joi240004supp1_prod_1721756962.80052.pdf#page=26), [page 27 power inputs](../../../joi240004supp1_prod_1721756962.80052.pdf#page=27), and [page 29 Table A1](../../../joi240004supp1_prod_1721756962.80052.pdf#page=29); REPORT [main page 2 endpoint/methods](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=2), [main page 6 Table 2/footnote b](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), [supplement page 4 model](../../../joi240004supp2_prod_1721756962.82552.pdf#page=4), [page 15 eTable 2/footnote b](../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), and [page 16 eTable 2 continuation](../../../joi240004supp2_prod_1721756962.82552.pdf#page=16). Plan percent change is numerically instantiated by −20%/−15% power assumptions; tables explicitly distinguish net HbA1c change from other outcomes' relative change. This is quantity identity, not crude/model arithmetic; numerical display precision is inapplicable. Alternative: a scale amendment or loose main-method label. Human question: did the primary response change from relative-percent to net percentage-point HbA1c change, and what produced the primary/year-12 contrasts?

## C005 — Remission medication-free window

Pending Human Adjudication.

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN DOC-002 pp. 18, 29 vs REPORT DOC-001 pp. 1, 2, 7
**Evidence state:** reproduced
**Inclusion audit:** PENDING
**Finding IDs:** F-XS-006
**Checker provenance including duplicate findings:** F-XS-006, F-ST1-005
**Qualifying route:** Route B
**Classification rationale:** The key remission endpoint's prospective and retrospective medication-free windows differ in explicit specification. The abbreviated Figure 3 definition is not a separate REPORT conflict.
**Classification ambiguity:** An unsupplied operational definition or amendment could contain the reported duration.

**Remission medication-free window.** Included F-XS-006; duplicate provenance F-ST1-005. Proposed protocol_report / P_R; all relationships P_R. PLAN [page 18 remission item](../../../joi240004supp1_prod_1721756962.80052.pdf#page=18) and [page 29 Table A1](../../../joi240004supp1_prod_1721756962.80052.pdf#page=29); REPORT [main page 2 definition](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=2), [page 1 abstract remission rates](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1), and [page 7 Figure 3 caption](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=7). Off medication and HbA1c<6.5 match, but only report explicitly requires at least 3 months. Do not infer a plan zero-month rule or any changed event count; the added criterion affects endpoint matching. Alternatives: an operational definition, an amendment, or the later definition referenced by the report but not supplied as its plan. Human question: what prospective window underlies the key remission rates/OR?

## C006 — Cardiovascular outcome status

Pending Human Adjudication.

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN DOC-002 pp. 18, 29, 30 vs REPORT DOC-001 pp. 1, 2, 8
**Evidence state:** reproduced
**Inclusion audit:** PENDING
**Finding IDs:** F-XS-009
**Checker provenance including duplicate findings:** F-XS-009
**Qualifying route:** Route A, category 5
**Classification rationale:** This compares prospective outcome status with the report's stated secondary hierarchy; it is not a same-document count comparison.
**Classification ambiguity:** Safety and secondary status could coexist; plan p18 permits some dual-status endpoints without identifying this one.

**Cardiovascular outcome status.** Included F-XS-009. Proposed protocol_report / P_R; all relationships P_R. PLAN [page 18 secondary endpoint list/section 4.4](../../../joi240004supp1_prod_1721756962.80052.pdf#page=18), [page 29 Table A1](../../../joi240004supp1_prod_1721756962.80052.pdf#page=29), and [page 30 Table A1 continuation](../../../joi240004supp1_prod_1721756962.80052.pdf#page=30); REPORT [main page 2 other secondary outcomes](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=2), [page 1 abstract cardiovascular finding](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1), and [page 8 cardiovascular rows](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=8). Exact plan table labels major adverse cardiovascular events Safety, separately from efficacy stroke/retinopathy/nephropathy/foot-ulcer; the report explicitly labels major adverse cardiovascular events secondary. Section 4.4 says some study outcomes are also secondary, without identifying cardiovascular events as such. Preserve dual safety/secondary status as an alternative; do not invent composite changes. Human question: which prespecified hierarchy/status applies to the abstract cardiovascular outcome?

## C007 — Primary baseline adjustment

Pending Human Adjudication.

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN DOC-002 pp. 26, 34 vs REPORT DOC-001 pp. 2, 3 and REPORT DOC-003 p. 4
**Evidence state:** reproduced
**Inclusion audit:** PENDING
**Finding IDs:** F-XS-005
**Checker provenance including duplicate findings:** F-XS-005
**Qualifying route:** Route B
**Classification rationale:** The prospective primary covariate specification differs from the reported primary specification. Agreeing report methods and within-plan primary/sensitivity distinctions do not add S_C/S_W/P_P.
**Classification ambiguity:** The reported primary could be a selected planned sensitivity model or reflect an unsupplied amendment.

**Primary baseline adjustment.** Included F-XS-005. Proposed protocol_report / P_R; all relationships P_R. PLAN [page 26 A1 and its 4-dimensional site-only Z](../../../joi240004supp1_prod_1721756962.80052.pdf#page=26) and [page 34 further baseline sensitivities](../../../joi240004supp1_prod_1721756962.80052.pdf#page=34); REPORT [main page 2 statistical analysis](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=2), [page 3 continuation](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), and [supplement page 4 primary fixed effects](../../../joi240004supp2_prod_1721756962.82552.pdf#page=4). The explicit prospective primary and further-sensitivity lists differ from baseline HbA1c in the reported primary list. This is separate from missing expanded sensitivities: it concerns which specification generated the main estimate, not whether additional results were supplied. Alternative: selected planned sensitivity or amendment. Human question: which planned/amended primary specification generated −1.4 and its CI/P?

## C008 — Planned primary sensitivity package not reported

Pending Human Adjudication.

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN DOC-002 pp. 30, 31, 34 vs REPORT DOC-001 pp. 3, 9 and REPORT DOC-003 pp. 4, 5, 6, 9; absence checked across all main/report-supplement pages
**Evidence state:** reproduced
**Inclusion audit:** PENDING
**Finding IDs:** F-XS-008
**Checker provenance including duplicate findings:** F-XS-008, F-ST1-004
**Qualifying route:** Route A, category 5
**Classification rationale:** Explicitly prespecified primary sensitivity results have no supplied corresponding report results. All compared obligations are PLAN-to-REPORT, consolidated as one absent sensitivity package.
**Classification ambiguity:** Unsupplied results or a final plan amendment may exist; censoring weights could be one under the reported random-censoring assumption.

**Planned primary sensitivity package not reported.** Included F-XS-008; duplicate provenance F-ST1-004. Proposed protocol_report / P_R; all relationships P_R. PLAN [page 30 MICE/Rubin/pattern mixture and IPTW](../../../joi240004supp1_prod_1721756962.80052.pdf#page=30), [page 31 final treatment×censoring weight and postcrossover discard](../../../joi240004supp1_prod_1721756962.80052.pdf#page=31), and [page 34 extra baseline HbA1c/BMI/imbalance sensitivities](../../../joi240004supp1_prod_1721756962.80052.pdf#page=34); REPORT [main page 3 sensitivity/missingness and primary sensitivity result](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), [page 9 limitations](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=9), [supplement page 4 methods](../../../joi240004supp2_prod_1721756962.82552.pdf#page=4), [page 5 complete treatment-IPW formula](../../../joi240004supp2_prod_1721756962.82552.pdf#page=5), [page 6 missingness continuation](../../../joi240004supp2_prod_1721756962.82552.pdf#page=6), and [page 9 eFigure 2](../../../joi240004supp2_prod_1721756962.82552.pdf#page=9). Complete supplied main pages 1–11 and results supplement pages 1–22 contain no results for MICE, pattern mixture, outcomes-discarded-after-crossover, or expanded BMI/imbalance primary sensitivities. The stated treatment-IPW analysis reassigns treatment after crossover and does not equal outcome discard; its printed weight formula lacks a censoring-weight factor. MAR could make the latter factor one, which is an alternative requiring mapping to the plan, not an inferred numerical conflict. No claim about analyses actually conducted is made. Human question: where are these planned primary results or their supplied replacement/amendment?

## C009 — Planned binary A2 and reported GEE

Pending Human Adjudication.

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN DOC-002 p. 27 vs REPORT DOC-001 pp. 3, 6 and REPORT DOC-003 pp. 4, 5, 15
**Evidence state:** reproduced
**Inclusion audit:** PENDING
**Finding IDs:** F-XS-007
**Checker provenance including duplicate findings:** F-XS-007, F-ST1-003
**Qualifying route:** Route A, category 5
**Classification rationale:** The plan specifies the main key-secondary model A2; the report supplies another model family and no A2 result. Report method descriptions agree, so no REPORT-to-REPORT conflict is present.
**Classification ambiguity:** An unsupplied final analysis amendment may define the GEE replacement.

**Planned binary A2 versus reported GEE.** Included F-XS-007; duplicate provenance F-ST1-003. Proposed protocol_report / P_R; all relationships P_R. PLAN [page 27 A2/main binary secondary test](../../../joi240004supp1_prod_1721756962.80052.pdf#page=27); REPORT [main page 3 GEE/sandwich analysis](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), [page 6 binary outcome rows](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), [supplement page 4 binary GEE](../../../joi240004supp2_prod_1721756962.82552.pdf#page=4), [page 5 continuation](../../../joi240004supp2_prod_1721756962.82552.pdf#page=5), and [page 15 year-12 binary rows](../../../joi240004supp2_prod_1721756962.82552.pdf#page=15). A2 is explicitly patient-random-effect logistic and the main secondary test includes remission; GEE/sandwich is explicitly the reported family. This is an observable replacement/absence of the planned key analysis, not a preference between models or a comparison with crude odds. Alternative: a final plan amendment. Human question: which specification supports the GEE replacement and what conditioning/estimand belongs to the reported ORs?

## C010 — Medical medication OR interval pattern

Pending Human Adjudication.

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT DOC-001 p. 6 medical medication OR cell vs all other binary OR cells on the same page; REPORT DOC-003 p. 4 is corroborating inference context only
**Evidence state:** reproduced
**Inclusion audit:** PENDING
**Finding IDs:** F-ST1-007
**Checker provenance including duplicate findings:** F-ST1-007
**Qualifying route:** Route A, category 4
**Classification rationale:** One estimate/interval cell does not reproduce a method that reproduces every other binary cell within the same REPORT table. The supplementary GEE/sandwich description does not conflict with the table and adds no S_C.
**Classification ambiguity:** The anomalous cell could use an explicitly different asymmetric interval construction or contrast, neither specified in the supplied display.

**Medical medication OR interval pattern.** Included F-ST1-007. Proposed statistical_results / S_W; all relationships S_W. REPORT [main page 6 Table 2 medical medication cell, all other binary cells, and footnotes](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6); [supplement page 4 GEE/sandwich methods](../../../joi240004supp2_prod_1721756962.82552.pdf#page=4) corroborates inference but creates no conflicting S_C relationship. Independently applying sqrt(lower×upper) with every cell's actual half-unit bounds reproduces all 11 other within-group and all 6 between-group OR points: the ranges overlap each respective point interval, including the coarsely printed remission bounds and surgery HbA1c<7 upper bound 11.4. The medical medication cell alone gives [.127769323,.221641603] versus [.095,.105], gap .022769323/.10=.227693233. This is route A4, not a crude-odds comparison or a significant/nonsignificant conflict. Alternatives: a distinct asymmetric interval procedure, another contrast, or an unmatched bound; no alternate numerical value is selected. Human question: which interval construction produced .10 [.01,3.27] and why does it differ from the reproducing pattern?

## C011 — Vascular and safety test mapping

Pending Human Adjudication.

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN DOC-002 pp. 26, 34, 35 vs REPORT DOC-001 pp. 1, 7 and REPORT DOC-003 pp. 6, 17, 19, 20, 21
**Evidence state:** reproduced
**Inclusion audit:** PENDING
**Finding IDs:** F-XS-010
**Checker provenance including duplicate findings:** F-XS-010, F-ST1-008
**Qualifying route:** Route B
**Classification rationale:** This is an unresolved correspondence between prospective vascular/safety analysis and reported result tests. REPORT descriptions agree with each other, so no S_C/S_W is added. The separate baseline CMH paragraph is contextual, not proof of event strata.
**Classification ambiguity:** CMH strata are unspecified; “chi-squared” may abbreviate CMH, sparse-outcome Fisher substitution may apply, or planned composites and reported individual-row tests may differ.

**Vascular/safety test mapping.** Included F-XS-010; duplicate provenance F-ST1-008. Proposed protocol_report / P_R; all relationships P_R. PLAN [page 34 Aim 2 CMH and safety same-manner statement](../../../joi240004supp1_prod_1721756962.80052.pdf#page=34), [page 35 continuation](../../../joi240004supp1_prod_1721756962.80052.pdf#page=35), and [page 26 separate baseline CMH paragraph](../../../joi240004supp1_prod_1721756962.80052.pdf#page=26); REPORT [main page 7 event/procedure narrative](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=7), [page 1 abstract cardiovascular finding](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1), [supplement page 6 chi-squared/Fisher statement](../../../joi240004supp2_prod_1721756962.82552.pdf#page=6), [page 17 nutritional tests](../../../joi240004supp2_prod_1721756962.82552.pdf#page=17), [page 20 eTable 5 footnote b](../../../joi240004supp2_prod_1721756962.82552.pdf#page=20), and [page 21 eTable 6 footnote b](../../../joi240004supp2_prod_1721756962.82552.pdf#page=21). Exact sources name CMH prospectively and chi-squared/Fisher retrospectively without mapping them. The source's event paragraph does not name CMH strata, so site-stratified versus unstratified is not an independently established fact and must not become the candidate title or numeric premise. Alternatives: chi-squared abbreviates CMH, exact tests substitute for sparse outcomes, or planned composites and listed row tests are distinct. Reported example P values are abdominal pain .02, dysphagia .005 and pooled crossover/conversion/revision <.001. Human question: which reported tests instantiate the planned vascular/safety CMH analyses and what specification explains the mapping or change?

## C012 — Fixed site and power variance specification

Pending Human Adjudication.

**Review domain:** plan_material
**Relationship type:** P_P
**All relationships:** P_P
**Compared document roles:** PLAN DOC-002 p. 26 A1/site definition vs PLAN DOC-002 pp. 28, 31 power/heterogeneity; REPORT DOC-001 pp. 2, 3 and REPORT DOC-003 p. 4 corroborate only
**Evidence state:** reproduced
**Inclusion audit:** PENDING
**Finding IDs:** F-XS-011
**Checker provenance including duplicate findings:** F-XS-011, F-ST1-006
**Qualifying route:** Route B
**Classification rationale:** Both conflicting specifications are inside the prospective PLAN. The fixed-site REPORT model agrees with one side and is not a PLAN-to-REPORT inconsistency, so P_R is not added.
**Classification ambiguity:** A finite-site coefficient spread or a separate generative random-site model could define σ_b, but the plan does not identify either correspondence.

**Fixed site / power variance specification.** Included F-XS-011; duplicate provenance F-ST1-006. Proposed plan_material / P_P; all relationships P_P. PLAN [page 26 A1/site-term definition](../../../joi240004supp1_prod_1721756962.80052.pdf#page=26), [page 28 primary power variance components](../../../joi240004supp1_prod_1721756962.80052.pdf#page=28), and [page 31 distribution/heterogeneity paragraph](../../../joi240004supp1_prod_1721756962.80052.pdf#page=31); REPORT [main page 2](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=2), [main page 3 fixed-effect continuation](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), and [supplement page 4 fixed-site model](../../../joi240004supp2_prod_1721756962.82552.pdf#page=4) only corroborate fixed-site analysis and add no P_R relationship. A1 calls b_i fixed, whereas its power paragraph calls σ_b=.06 a variance component estimated by fitting the mixed model under A1. The separate duplicated fixed-site coefficients are not the issue because plan page 27 permits identifiability constraints. Alternatives: finite-site fixed-coefficient spread or distinct generative random-site simulation; neither parameter definition is supplied. Human question: what does σ_b=.06 represent and how does the stated simulation model correspond to fixed-site A1?

## C013 — Appendix randomization-dropout accounting

Pending Human Adjudication.

**Review domain:** plan_material
**Relationship type:** P_P
**All relationships:** P_P
**Compared document roles:** PLAN DOC-002 p. 55 randomized/intervention rows vs PLAN DOC-002 p. 56 attached dagger footnote; PLAN DOC-002 p. 27 corroborates row totals
**Evidence state:** reproduced
**Inclusion audit:** PENDING
**Finding IDs:** F-NUM-102
**Checker provenance including duplicate findings:** F-NUM-102
**Qualifying route:** Route A, category 3
**Classification rationale:** The prospective study-population enrollment accounting is inside one PLAN display continued across two pages, with a footnote explicitly attached to initiation. It bears on the planned enrollment pool; final REPORT cohort numbers are not compared.
**Classification ambiguity:** The 38 dropouts may refer to a different historical snapshot/population or category, but the attached display identifies none.

**Appendix randomization-dropout accounting.** Included F-NUM-102. Proposed plan_material / P_P; all relationships P_P. PLAN [page 55 Appendix 2 randomized/intervention rows and attached dagger](../../../joi240004supp1_prod_1721756962.80052.pdf#page=55) and [page 56 continued display/dagger text](../../../joi240004supp1_prod_1721756962.80052.pdf#page=56); [page 27 primary power population paragraph](../../../joi240004supp1_prod_1721756962.80052.pdf#page=27) corroborates 355 randomized/325 initiated, rather than creating another comparison. Exact source title is Initial Trials: Enrolled Participants and the footnote defines intervention initiation followed immediately by total 38 randomization dropouts not followed or eligible. Sums 155+69+43+45+43=355 and 154+61+38+40+32=325 give 30; half-unit sum ranges [352.5,357.5] minus [322.5,327.5] give [25,35], separated from [37.5,38.5] by .065789 relative to 38. This is count accounting within one display of the planned enrollment pool, not a comparison of unrelated historical calendars or final enrollment cohorts; route A3 applies. Alternatives: footnote refers to another historical snapshot/population or dropout is a distinct category, but neither is identified by the attached display. Do not compare this total directly with final-report population/withdrawal counts. Human question: which population/time point supplies 38, and how does it reconcile with the displayed randomization/initiation accounting?

## C014 — Other race count and percentage

Pending Human Adjudication.

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT DOC-003 p. 14 eTable 1 Other-race count, percentage, column denominator and footnotes
**Evidence state:** reproduced
**Inclusion audit:** PENDING
**Finding IDs:** F-NUM-101
**Checker provenance including duplicate findings:** F-NUM-101
**Qualifying route:** Route A, category 3
**Classification rationale:** Count/percentage/denominator conflict is within one REPORT display. The main baseline table is not a comparator, so this is not a peripheral cross-copy baseline comparison and adds no S_C.
**Classification ambiguity:** An alternative race-specific denominator or count is possible but unspecified.

**Other race count and percentage.** Included F-NUM-101. Proposed statistical_results / S_W; all relationships S_W. REPORT [supplement page 14 eTable 1 7-year N=262, race rows and footnotes](../../../joi240004supp2_prod_1721756962.82552.pdf#page=14). Footnote a explicitly says n (%), and footnote b says all study participants reached 7 years; no alternative racial denominator is printed. The exact Other entry is 4 (1.9); half-unit inputs give [1.333333,1.720841]% and printed [1.85,1.95]%, gap .129159/1.9=.067978. This within-display arithmetic is not a peripheral cross-copy baseline comparison. Neighboring 81/176 counts sum with 4 to 261, a corroborating detail rather than an independently included small-total discrepancy. Alternative: another count or an unstated denominator; no corrected value is assigned. Human question: which Other-race count, denominator and percentage apply?

# Independent initial inclusion screen

Runtime agent: /root/inclusion_screen. Run model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN. Scope: all 24 findings in checkers/numeric_consistency.md (4), checkers/cross_source_consistency.md (11), and checkers/statistical_pass_1.md (9); the merged extra statistical shard has no findings. The complete QUALITY_CONTROL_SCOPE.md and inclusion-screen contract were read. Every finding was independently compared with its exact supplied PDF locations, including source labels and footnotes. No prior-run conclusions or external evidence were used.

There are 14 distinct included issues and 10 duplicate findings. Every nonduplicate finding reproduces and qualifies by a route below; no expected number was used. The coordinator assigned stable candidate IDs C001 through C014 in the documented source order. Each duplicate row names the stable issue it duplicates. Group names below identify consolidation only and are not candidate IDs or adjudications.

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-NUM-001 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C003 |
| F-NUM-002 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-NUM-101 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C014 |
| F-NUM-102 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C013 |
| F-XS-001 | cross_source_consistency_reviewer | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C003 |
| F-XS-002 | cross_source_consistency_reviewer | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C001 |
| F-XS-003 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C002 |
| F-XS-004 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C004 |
| F-XS-005 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C007 |
| F-XS-006 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C005 |
| F-XS-007 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C009 |
| F-XS-008 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C008 |
| F-XS-009 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C006 |
| F-XS-010 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C011 |
| F-XS-011 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C012 |
| F-ST1-001 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C002 |
| F-ST1-002 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C004 |
| F-ST1-003 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C009 |
| F-ST1-004 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C008 |
| F-ST1-005 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C005 |
| F-ST1-006 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C012 |
| F-ST1-007 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C010 |
| F-ST1-008 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C011 |
| F-ST1-009 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C001 |

## One-sentence independent justifications

- **F-NUM-001 — INCLUDE:** Route A, category 3 applies because the exact REPORT abstract gives 262 participants and 4 deaths (2.2%), whereas even the full half-unit recomputed range [1.333333%, 1.720841%] is separated from printed [2.15%, 2.25%] by a relative discrepancy 0.195072, and the body supplies no alternative mortality denominator.
- **F-NUM-002 — INCLUDE:** Route A, category 1 applies because the exact REPORT abstract and Results print positive surgery 1.6 with entirely negative CI [−1.8, −1.3], while Table 2 prints −1.6 within that interval; the positive-reduction-magnitude interpretation is retained as an alternative rather than an exclusion of the printed point/interval reading.
- **F-NUM-101 — INCLUDE:** Route A, category 3 applies because the exact REPORT eTable 1 labels categorical entries n (%) and its 7-year column N=262 but prints Other 4 (1.9), whose full half-unit recomputed range [1.333333%, 1.720841%] has a relative interval gap 0.067978 from printed [1.85%, 1.95%].
- **F-NUM-102 — INCLUDE:** Route A, category 3 applies because the PLAN Appendix 2 intervention row is explicitly linked to the dagger footnote describing 38 randomization dropouts, but its five randomized counts sum 355 and initiated counts sum 325, giving a full half-unit difference range [25, 35] separated from [37.5, 38.5] by 2.5/38=0.065789 within this single display.
- **F-XS-001 — SCREENED_OUT:** The exact-source pooled-death discrepancy is the same issue as included F-NUM-001, and its additional main page 3 cohort location is retained in the merged mortality group.
- **F-XS-002 — SCREENED_OUT:** The exact-source positive surgery HbA1c point with signed negative interval is the same repeated issue as included F-NUM-002, with all three report locations retained.
- **F-XS-003 — INCLUDE:** Route B applies because the abstract-reported year-12 HbA1c ITT contrast is identically −1.1 [−1.7, −0.5] in both REPORT documents but has P=.002 versus P<.001, whose rounded intervals remain separated by at least .0005/.002=.25 without a source-identified different test, changing the P value available for extraction.
- **F-XS-004 — INCLUDE:** Route B applies because the PLAN primary endpoint/A1 and its −20% to −15% power inputs establish relative-percent HbA1c change, while the REPORT primary table expressly labels net HbA1c change despite the report methods saying percent change, leaving the primary −1.4 and year-12 −1.1 contrasts on a conflicting planned/reported quantity scale.
- **F-XS-005 — INCLUDE:** Route B applies because the PLAN A1 primary list contains group, visit, interaction and site, and reserves baseline HbA1c/BMI/imbalance terms for further sensitivity analyses, whereas the REPORT explicitly includes baseline HbA1c in the primary model generating −1.4 [−1.8, −1.0], without identifying which planned specification or amendment produced that main result.
- **F-XS-006 — INCLUDE:** Route B applies because the PLAN remission definitions state HbA1c<6.5 off medications and the REPORT explicitly adds at least 3 months medication-free, an endpoint window that can change qualification for the abstract remission rates and OR and is not supplied by the immediate annual-assessment context.
- **F-XS-007 — INCLUDE:** Route A, category 5 applies because the PLAN explicitly prespecifies mixed-effects logistic A2 as the main analysis of remission/control, including the abstract key remission result, but the REPORT supplies GEE/sandwich results instead and no planned A2 result; the distinct conditional versus population-average model descriptions also satisfy route B.
- **F-XS-008 — INCLUDE:** Route A, category 5 applies because the PLAN explicitly commits to primary MICE/Rubin, pattern-mixture, postcrossover-discard and expanded-baseline sensitivities and a treatment/censoring-weight product, but the complete supplied REPORT materials describe only MAR recovery and treatment-IPW sensitivity and provide no results for those named primary analyses.
- **F-XS-009 — INCLUDE:** Route A, category 5 applies because the PLAN Table A1 explicitly places major adverse cardiovascular events under Safety separately from vascular efficacy endpoints, while the REPORT names major adverse cardiovascular events among other secondary outcomes and reports them in the abstract, preserving generic dual safety/secondary classification as an alternative.
- **F-XS-010 — INCLUDE:** Route B applies because the PLAN explicitly specifies CMH for vascular events and the same analysis for safety, while the REPORT explicitly specifies chi-squared or Fisher tests for extractable safety/procedure P values, without mapping these result tests to the planned CMH analysis; the broad chi-squared abbreviation and sparse-event substitution possibilities are retained and no site stratum is assumed.
- **F-XS-011 — INCLUDE:** Route B applies because the PLAN A1 explicitly defines its site term b_i as fixed but the primary power paragraph supplies σ_b=.06 as a mixed-model variance component under A1, with no distinct data-generating definition, leaving the relied-on primary power specification and site-heterogeneity interpretation unresolved.
- **F-ST1-001 — SCREENED_OUT:** The exact-source matched year-12 P discrepancy is identical to included F-XS-003, including the alternate report-version/test interpretation, and all source locations remain in that group.
- **F-ST1-002 — SCREENED_OUT:** The exact-source planned relative-percent versus reported net HbA1c scale comparison is identical to included F-XS-004, with its additional year-12 footnote/model occurrence retained.
- **F-ST1-003 — SCREENED_OUT:** The exact-source planned A2 versus reported GEE replacement is identical to included F-XS-007, whose included route A, category 5 retains the planned main key-secondary analysis and all binary result locations.
- **F-ST1-004 — SCREENED_OUT:** The exact-source absent named primary sensitivity package is identical to included F-XS-008, retaining every promised analysis and the explicit censoring-weight factor comparison.
- **F-ST1-005 — SCREENED_OUT:** The exact-source added 3-month medication-free remission window is identical to included F-XS-006, retaining the report Figure 3 abbreviated definition as a corroborating location.
- **F-ST1-006 — SCREENED_OUT:** The exact-source fixed site term versus primary-power variance-component description is identical to included F-XS-011, with supplement fixed-site methods retained as corroboration rather than a conflicting REPORT relationship.
- **F-ST1-007 — INCLUDE:** Route A, category 4 applies because the exact REPORT Table 2 medical medication OR .10 [.01, 3.27] has log-symmetric center range [.127769, .221642] disjoint from point [.095, .105] by relative gap .227693, whereas the same method independently reproduces all other 17 binary OR cells under their complete display intervals.
- **F-ST1-008 — SCREENED_OUT:** The exact-source vascular/safety CMH versus reported chi-squared/Fisher analysis comparison is identical to included F-XS-010, retaining the additional nutritional table and plan continuation locations without inferring an unspecified site stratum.
- **F-ST1-009 — SCREENED_OUT:** The exact-source positive surgery 1.6 outside [−1.8, −1.3] is identical to included F-NUM-002, retaining medical 0.2 only as a companion magnitude/sign occurrence rather than another interval-containment issue.

## Consolidated issues and proposed source order

The sequence below is a locator ordering, not a grade: DOC-001 first, earliest substantive occurrence within its physical page, followed by PLAN-only issues in DOC-002 and REPORT-supplement-only issues in DOC-003. Each item lists the complete union of affected/corroborating checker locations. The coordinator assigned C001 through C014 to items 1 through 14 below after this independent screen. Links target the exact supplied sources from this file's directory.

1. **Positive HbA1c point / signed interval.** Included finding F-NUM-002; duplicate provenance F-XS-002, F-ST1-009. Proposed statistical_results / S_W; all relationships S_W. REPORT [main page 1 abstract HbA1c changes](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1), [page 3 Results HbA1c paragraph](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), and [page 6 Table 2 HbA1c row/footnote b](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6). The surgery point prints +1.6 in both prose locations; the CI is −1.8 to −1.3 and the table point −1.6. Even allowing rounding, positive point [1.55,1.65] and nearest possible negative upper limit [−1.35,−1.25] remain separated by at least 2.80; route A1 has no rounding exclusion. Medical +0.2 versus table −0.2 is a companion prose/table pattern; +0.2 alone is within its [−.5,.2] interval. Alternative: prose intentionally gives reduction magnitudes and intervals signed changes. Human question: which scale applies to the paired prose points and intervals?

2. **Year-12 HbA1c P value.** Included F-XS-003; duplicate provenance F-ST1-001. Proposed statistical_results / S_C; all relationships S_C. REPORT [main page 1 abstract](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1), [page 3 Results](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), [results supplement page 15 eTable 2 HbA1c](../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), and [supplement page 4 ITT model](../../../joi240004supp2_prod_1721756962.82552.pdf#page=4). The same visit/population/contrast and −1.1 [−1.7,−.5] have .002 and <.001. This is not an interval-versus-significance issue: both tests are significant. Half-unit .002 range [.0015,.0025] and <.001 range [0,.001) have gap at least .0005 and relative discrepancy at least .25. Alternative: distinct test conventions or report revision; main page 1 states corrected July 24, 2024 without identifying this comparison. Human question: which P/test belongs to this contrast?

3. **Pooled mortality percentage.** Included F-NUM-001; duplicate provenance F-XS-001. Proposed statistical_results / S_W; all relationships S_W. REPORT [main page 1 abstract](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1), [page 3 enrollment](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), [page 4 Table 1 headers](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=4), [page 7 deaths paragraph](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=7), and [page 8 Table 3 headers/Death row](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=8). Exact 4/262 gives 1.526718%; complete half-unit range [1.333333,1.720841]% versus [2.15,2.25]% gives .429159 percentage-point gap and .195072 relative discrepancy. Independently allowing half-unit inputs in both arm counts/denominators still gives [1.140684,1.915709]%, gap .234291/2.2=.106496. Arm counts 2/96 and 2/166 individually reproduce 2.1% and 1.2%. Alternative: a separate unidentified pooled risk-set denominator. Human question: which denominator and mortality quantity produce 2.2%?

4. **Primary HbA1c response scale.** Included F-XS-004; duplicate provenance F-ST1-002. Proposed protocol_report / P_R; all relationships P_R, S_C, S_W. PLAN [page 17 endpoint](../../../joi240004supp1_prod_1721756962.80052.pdf#page=17), [page 26 A1 response](../../../joi240004supp1_prod_1721756962.80052.pdf#page=26), [page 27 power inputs](../../../joi240004supp1_prod_1721756962.80052.pdf#page=27), and [page 29 Table A1](../../../joi240004supp1_prod_1721756962.80052.pdf#page=29); REPORT [main page 2 endpoint/methods](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=2), [main page 6 Table 2/footnote b](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), [supplement page 4 model](../../../joi240004supp2_prod_1721756962.82552.pdf#page=4), [page 15 eTable 2/footnote b](../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), and [page 16 eTable 2 continuation](../../../joi240004supp2_prod_1721756962.82552.pdf#page=16). Plan percent change is numerically instantiated by −20%/−15% power assumptions; tables explicitly distinguish net HbA1c change from other outcomes' relative change. This is quantity identity, not crude/model arithmetic; numerical display precision is inapplicable. Alternative: a scale amendment or loose main-method label. Human question: did the primary response change from relative-percent to net percentage-point HbA1c change, and what produced the primary/year-12 contrasts?

5. **Remission medication-free window.** Included F-XS-006; duplicate provenance F-ST1-005. Proposed protocol_report / P_R; all relationships P_R. PLAN [page 18 remission item](../../../joi240004supp1_prod_1721756962.80052.pdf#page=18) and [page 29 Table A1](../../../joi240004supp1_prod_1721756962.80052.pdf#page=29); REPORT [main page 2 definition](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=2), [page 1 abstract remission rates](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1), and [page 7 Figure 3 caption](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=7). Off medication and HbA1c<6.5 match, but only report explicitly requires at least 3 months. Do not infer a plan zero-month rule or any changed event count; the added criterion affects endpoint matching. Alternatives: an operational definition, an amendment, or the later definition referenced by the report but not supplied as its plan. Human question: what prospective window underlies the key remission rates/OR?

6. **Cardiovascular outcome status.** Included F-XS-009. Proposed protocol_report / P_R; all relationships P_R. PLAN [page 18 secondary endpoint list/section 4.4](../../../joi240004supp1_prod_1721756962.80052.pdf#page=18), [page 29 Table A1](../../../joi240004supp1_prod_1721756962.80052.pdf#page=29), and [page 30 Table A1 continuation](../../../joi240004supp1_prod_1721756962.80052.pdf#page=30); REPORT [main page 2 other secondary outcomes](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=2), [page 1 abstract cardiovascular finding](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1), and [page 8 cardiovascular rows](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=8). Exact plan table labels major adverse cardiovascular events Safety, separately from efficacy stroke/retinopathy/nephropathy/foot-ulcer; the report explicitly labels major adverse cardiovascular events secondary. Section 4.4 says some study outcomes are also secondary, without identifying cardiovascular events as such. Preserve dual safety/secondary status as an alternative; do not invent composite changes. Human question: which prespecified hierarchy/status applies to the abstract cardiovascular outcome?

7. **Primary baseline adjustment.** Included F-XS-005. Proposed protocol_report / P_R; all relationships P_R. PLAN [page 26 A1 and its 4-dimensional site-only Z](../../../joi240004supp1_prod_1721756962.80052.pdf#page=26) and [page 34 further baseline sensitivities](../../../joi240004supp1_prod_1721756962.80052.pdf#page=34); REPORT [main page 2 statistical analysis](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=2), [page 3 continuation](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), and [supplement page 4 primary fixed effects](../../../joi240004supp2_prod_1721756962.82552.pdf#page=4). The explicit prospective primary and further-sensitivity lists differ from baseline HbA1c in the reported primary list. This is separate from missing expanded sensitivities: it concerns which specification generated the main estimate, not whether additional results were supplied. Alternative: selected planned sensitivity or amendment. Human question: which planned/amended primary specification generated −1.4 and its CI/P?

8. **Planned primary sensitivity package not reported.** Included F-XS-008; duplicate provenance F-ST1-004. Proposed protocol_report / P_R; all relationships P_R. PLAN [page 30 MICE/Rubin/pattern mixture and IPTW](../../../joi240004supp1_prod_1721756962.80052.pdf#page=30), [page 31 final treatment×censoring weight and postcrossover discard](../../../joi240004supp1_prod_1721756962.80052.pdf#page=31), and [page 34 extra baseline HbA1c/BMI/imbalance sensitivities](../../../joi240004supp1_prod_1721756962.80052.pdf#page=34); REPORT [main page 3 sensitivity/missingness and primary sensitivity result](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), [page 9 limitations](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=9), [supplement page 4 methods](../../../joi240004supp2_prod_1721756962.82552.pdf#page=4), [page 5 complete treatment-IPW formula](../../../joi240004supp2_prod_1721756962.82552.pdf#page=5), [page 6 missingness continuation](../../../joi240004supp2_prod_1721756962.82552.pdf#page=6), and [page 9 eFigure 2](../../../joi240004supp2_prod_1721756962.82552.pdf#page=9). Complete supplied main pages 1–11 and results supplement pages 1–22 contain no results for MICE, pattern mixture, outcomes-discarded-after-crossover, or expanded BMI/imbalance primary sensitivities. The stated treatment-IPW analysis reassigns treatment after crossover and does not equal outcome discard; its printed weight formula lacks a censoring-weight factor. MAR could make the latter factor one, which is an alternative requiring mapping to the plan, not an inferred numerical conflict. No claim about analyses actually conducted is made. Human question: where are these planned primary results or their supplied replacement/amendment?

9. **Planned binary A2 versus reported GEE.** Included F-XS-007; duplicate provenance F-ST1-003. Proposed protocol_report / P_R; all relationships P_R. PLAN [page 27 A2/main binary secondary test](../../../joi240004supp1_prod_1721756962.80052.pdf#page=27); REPORT [main page 3 GEE/sandwich analysis](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), [page 6 binary outcome rows](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), [supplement page 4 binary GEE](../../../joi240004supp2_prod_1721756962.82552.pdf#page=4), [page 5 continuation](../../../joi240004supp2_prod_1721756962.82552.pdf#page=5), and [page 15 year-12 binary rows](../../../joi240004supp2_prod_1721756962.82552.pdf#page=15). A2 is explicitly patient-random-effect logistic and the main secondary test includes remission; GEE/sandwich is explicitly the reported family. This is an observable replacement/absence of the planned key analysis, not a preference between models or a comparison with crude odds. Alternative: a final plan amendment. Human question: which specification supports the GEE replacement and what conditioning/estimand belongs to the reported ORs?

10. **Medical medication OR interval pattern.** Included F-ST1-007. Proposed statistical_results / S_W; all relationships S_W. REPORT [main page 6 Table 2 medical medication cell, all other binary cells, and footnotes](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6); [supplement page 4 GEE/sandwich methods](../../../joi240004supp2_prod_1721756962.82552.pdf#page=4) corroborates inference but creates no conflicting S_C relationship. Independently applying sqrt(lower×upper) with every cell's actual half-unit bounds reproduces all 11 other within-group and all 6 between-group OR points: the ranges overlap each respective point interval, including the coarsely printed remission bounds and surgery HbA1c<7 upper bound 11.4. The medical medication cell alone gives [.127769323,.221641603] versus [.095,.105], gap .022769323/.10=.227693233. This is route A4, not a crude-odds comparison or a significant/nonsignificant conflict. Alternatives: a distinct asymmetric interval procedure, another contrast, or an unmatched bound; no alternate numerical value is selected. Human question: which interval construction produced .10 [.01,3.27] and why does it differ from the reproducing pattern?

11. **Vascular/safety test mapping.** Included F-XS-010; duplicate provenance F-ST1-008. Proposed protocol_report / P_R; all relationships P_R. PLAN [page 34 Aim 2 CMH and safety same-manner statement](../../../joi240004supp1_prod_1721756962.80052.pdf#page=34), [page 35 continuation](../../../joi240004supp1_prod_1721756962.80052.pdf#page=35), and [page 26 separate baseline CMH paragraph](../../../joi240004supp1_prod_1721756962.80052.pdf#page=26); REPORT [main page 7 event/procedure narrative](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=7), [page 1 abstract cardiovascular finding](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1), [supplement page 6 chi-squared/Fisher statement](../../../joi240004supp2_prod_1721756962.82552.pdf#page=6), [page 17 nutritional tests](../../../joi240004supp2_prod_1721756962.82552.pdf#page=17), [page 20 eTable 5 footnote b](../../../joi240004supp2_prod_1721756962.82552.pdf#page=20), and [page 21 eTable 6 footnote b](../../../joi240004supp2_prod_1721756962.82552.pdf#page=21). Exact sources name CMH prospectively and chi-squared/Fisher retrospectively without mapping them. The source's event paragraph does not name CMH strata, so site-stratified versus unstratified is not an independently established fact and must not become the candidate title or numeric premise. Alternatives: chi-squared abbreviates CMH, exact tests substitute for sparse outcomes, or planned composites and listed row tests are distinct. Reported example P values are abdominal pain .02, dysphagia .005 and pooled crossover/conversion/revision <.001. Human question: which reported tests instantiate the planned vascular/safety CMH analyses and what specification explains the mapping or change?

12. **Fixed site / power variance specification.** Included F-XS-011; duplicate provenance F-ST1-006. Proposed plan_material / P_P; all relationships P_P. PLAN [page 26 A1/site-term definition](../../../joi240004supp1_prod_1721756962.80052.pdf#page=26), [page 28 primary power variance components](../../../joi240004supp1_prod_1721756962.80052.pdf#page=28), and [page 31 distribution/heterogeneity paragraph](../../../joi240004supp1_prod_1721756962.80052.pdf#page=31); REPORT [main page 2](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=2), [main page 3 fixed-effect continuation](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), and [supplement page 4 fixed-site model](../../../joi240004supp2_prod_1721756962.82552.pdf#page=4) only corroborate fixed-site analysis and add no P_R relationship. A1 calls b_i fixed, whereas its power paragraph calls σ_b=.06 a variance component estimated by fitting the mixed model under A1. The separate duplicated fixed-site coefficients are not the issue because plan page 27 permits identifiability constraints. Alternatives: finite-site fixed-coefficient spread or distinct generative random-site simulation; neither parameter definition is supplied. Human question: what does σ_b=.06 represent and how does the stated simulation model correspond to fixed-site A1?

13. **Appendix randomization-dropout accounting.** Included F-NUM-102. Proposed plan_material / P_P; all relationships P_P. PLAN [page 55 Appendix 2 randomized/intervention rows and attached dagger](../../../joi240004supp1_prod_1721756962.80052.pdf#page=55) and [page 56 continued display/dagger text](../../../joi240004supp1_prod_1721756962.80052.pdf#page=56); [page 27 primary power population paragraph](../../../joi240004supp1_prod_1721756962.80052.pdf#page=27) corroborates 355 randomized/325 initiated, rather than creating another comparison. Exact source title is Initial Trials: Enrolled Participants and the footnote defines intervention initiation followed immediately by total 38 randomization dropouts not followed or eligible. Sums 155+69+43+45+43=355 and 154+61+38+40+32=325 give 30; half-unit sum ranges [352.5,357.5] minus [322.5,327.5] give [25,35], separated from [37.5,38.5] by .065789 relative to 38. This is count accounting within one display of the planned enrollment pool, not a comparison of unrelated historical calendars or final enrollment cohorts; route A3 applies. Alternatives: footnote refers to another historical snapshot/population or dropout is a distinct category, but neither is identified by the attached display. Do not compare this total directly with final-report population/withdrawal counts. Human question: which population/time point supplies 38, and how does it reconcile with the displayed randomization/initiation accounting?

14. **Other race count and percentage.** Included F-NUM-101. Proposed statistical_results / S_W; all relationships S_W. REPORT [supplement page 14 eTable 1 7-year N=262, race rows and footnotes](../../../joi240004supp2_prod_1721756962.82552.pdf#page=14). Footnote a explicitly says n (%), and footnote b says all study participants reached 7 years; no alternative racial denominator is printed. The exact Other entry is 4 (1.9); half-unit inputs give [1.333333,1.720841]% and printed [1.85,1.95]%, gap .129159/1.9=.067978. This within-display arithmetic is not a peripheral cross-copy baseline comparison. Neighboring 81/176 counts sum with 4 to 261, a corroborating detail rather than an independently included small-total discrepancy. Alternative: another count or an unstated denominator; no corrected value is assigned. Human question: which Other-race count, denominator and percentage apply?

## Source rereading and derivative provenance

All cited source text was reread directly using Poppler 26.01.0 `pdftotext -layout` from the exact supplied PDFs into uniquely owned preprocessing/screen_main_direct.txt (all 11 main pages), preprocessing/screen_plan_direct.txt (all 65 PLAN pages), and preprocessing/screen_report_supp_direct.txt (all 22 results-supplement pages). Source roles were confirmed from content. Named-analysis absence was checked against the complete main/report-supplement text and its complete analysis sections, supplied figure captions and result tables; searches locate observations, while the source statements and displays govern decisions.

CPU Poppler 26.01.0 `pdftoppm -f N -l N -singlefile -scale-to 2100 -png` rendered and visual rereading confirmed main physical pages 1, 3 and 6; PLAN pages 55 and 56; and REPORT supplement pages 14 and 15. Unique derivatives are preprocessing/screen_main1.png, preprocessing/screen_main3.png, preprocessing/screen_main6.png, preprocessing/screen_plan55.png, preprocessing/screen_plan56.png, preprocessing/screen_supp14.png, and preprocessing/screen_supp15.png. Current direct-source rendered PLAN pages 26, 28, 29 and 31 in extraction/protocol_first_half_visual/ were also visually reread. Complete calculation of all 18 Table 2 binary interval-center ranges used deterministic JavaScript arithmetic on visually confirmed printed source inputs; no custom Python, OCR, external sources, or raw data were used.

No scientific coverage gap remains in the assigned 24-finding screen. Model covariance, degrees of freedom, simulation implementation, any unsupplied amendment/operational manual, and alternative population definitions remain explicitly limited; no missing detail was filled by convention. Supplied sources and reusable assets remain unchanged. The screener assigned no stable candidate IDs or dispositions; the coordinator subsequently populated the associations.

Counts: 24 findings; 14 distinct INCLUDE issues; 10 SCREENED_OUT findings, all DUPLICATE_OF_INCLUDED; 0 findings screened out under other reason codes. Proposed domains for the 14 issues: statistical_results 5, protocol_report 7, plan_material 2, report_internal_inconsistency 0. Every included issue is Pending Human Adjudication.
# Mechanical evidence recheck — Workflow 1.6.2

Fresh mandatory evidence rechecker: /root/evidence_recheck; model gpt-6.1-sol; reasoning effort high; FRESH_SPAWN. Exact assigned stable scope: C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014. All are Pending Human Adjudication. This file records evidence facts and classification, without assigning an adjudication.

The complete scope and review contract, current ledger, final initial screen, direct-source text, and current source-matched page images were read. Source-derived text located passages; visually read source-matched renderings confirmed every substantive compared page and all affected numeric cells. No prior-run conclusion, external source, unsupplied amendment, raw data, or preferred alternative analysis was used.

By content, DOC-001 is the published main REPORT; DOC-002 is the prospective clinical protocol including its statistical plan and enrollment appendix (PLAN); DOC-003 is the retrospective methods/results supplement (REPORT). PDF pages below are physical pages. Links resolve from verification/ to the exact supplied PDFs. Every role, primary relationship and domain remains as provisionally registered, with specific independent reasons below. C004 has three independently established relationship types; corroborating documents for C010 and C012 add none.

## Recheck summary

| Candidate | Evidence state | Review domain | Relationship type | All relationships |
|---|---|---|---|---|
| C001 | reproduced | statistical_results | S_W | S_W |
| C002 | reproduced | statistical_results | S_C | S_C |
| C003 | reproduced | statistical_results | S_W | S_W |
| C004 | reproduced | protocol_report | P_R | P_R, S_C, S_W |
| C005 | reproduced | protocol_report | P_R | P_R |
| C006 | reproduced | protocol_report | P_R | P_R |
| C007 | reproduced | protocol_report | P_R | P_R |
| C008 | reproduced | protocol_report | P_R | P_R |
| C009 | reproduced | protocol_report | P_R | P_R |
| C010 | reproduced | statistical_results | S_W | S_W |
| C011 | reproduced | protocol_report | P_R | P_R |
| C012 | reproduced | plan_material | P_P | P_P |
| C013 | reproduced | plan_material | P_P | P_P |
| C014 | reproduced | statistical_results | S_W | S_W |

No candidate value or registered source location needed transcription correction. C002's alternative interpretation is narrowed by the direct correction notice; C011's example P-value location is made explicit at DOC-003 page 19. These contextual additions do not change the printed comparison or evidence-state category.

## C001 — Positive HbA1c point and signed interval

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT DOC-001 pp. 1, 3 prose vs REPORT DOC-001 p. 6 Table 2
**Evidence state:** reproduced
**Classification rationale:** Estimate/interval/sign consistency is statistical-results content within one REPORT. The table confirms signed changes; no PLAN comparison is part of this issue.
**Classification ambiguity:** Positive reduction magnitudes may intentionally accompany signed-change intervals.

**Location found:** Yes, every affected occurrence: [main p1 abstract](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1), [main p3 Results paragraph](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), and [main p6 Table 2 HbA1c row and footnote b](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6); all REPORT by published result content.

**Source value/text matched:** Yes. Both prose locations give surgery decrease/difference 1.6% with 95% CI −1.8% to −1.3%; both give medical 0.2% with CI −0.5% to 0.2%. On p3 surgery is explicitly parenthesized as “difference, 1.6%.”
**Comparator matched:** Yes. Table 2 prints surgery −1.6 [−1.8, −1.3] and medical −0.2 [−0.5, 0.2], under net change; the baseline/year-7 values are 8.7/7.2 and 8.2/8.0.
**Consistency rule applicable:** Yes, point containment on the same scale (Route A, category 1), and consistency of signed point copies. The baseline/year-7 crude difference is not used to replace a fitted estimate.
**Calculation or logical comparison reproduced:** Literal surgery +1.6 is outside [−1.8, −1.3] in both prose occurrences; the table's −1.6 is inside. Route A1 is exempt from rounding exclusion. Nevertheless +1.6 half-unit [1.55, 1.65] remains separated from the highest possible upper limit −1.25 by 2.80. Positive and negative surgery-point copy intervals have gap 3.10, relative 3.10/1.6=1.9375. Medical positive [0.15, 0.25] versus table negative [−0.25, −0.15] has copy gap 0.30/0.2=1.5, but medical +0.2 is contained in its printed interval and is not an additional interval-noncontainment occurrence.
**Necessary inputs available:** Yes for literal point/interval and copy comparisons.
**Exact missing inputs or definitions:** Whether prose points denote positive decrease magnitudes while their intervals retain signed-change units.
**Source-grounded alternative interpretation:** “Decreased by” on p1 and decreasing baseline-to-follow-up values on p3 support intentional reduction magnitudes; Table 2 supports signed change. This is preserved without choosing a corrected point.
**Direct observation versus inferred explanation:** Direct: the printed unsigned points and signed table/intervals. Inferred: any sign-transcription mechanism or intentional mixed-scale convention.
**Exact remaining human question:** Do the prose points and their paired intervals represent the same signed-change quantity, or a positive reduction magnitude paired with a signed-change interval?
**Determining recheck fact:** Both literal surgery-point/interval pairings remain noncontaining after exact visual reading; no source transcription was changed.

## C002 — Year-12 HbA1c P value

**Review domain:** statistical_results
**Relationship type:** S_C
**All relationships:** S_C
**Compared document roles:** REPORT DOC-001 pp. 1, 3 vs REPORT DOC-003 p. 15; REPORT DOC-003 p. 4 supplies the model
**Evidence state:** reproduced
**Classification rationale:** The same printed inferential result differs between two retrospective REPORT documents. Agreeing main p1/p3 copies do not create S_W.
**Classification ambiguity:** Different test conventions could be attached to the same displayed interval, but none is identified.

**Location found:** Yes: [main p1 abstract](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1), [main p3 year-12 result](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), [supplement p15 eTable 2 HbA1c row](../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), and [supplement p4 ITT model/visit contrasts](../../../joi240004supp2_prod_1721756962.82552.pdf#page=4); all REPORT.
**Source value/text matched:** Yes, main p1 and p3 both give year-12 surgery-minus-medical difference −1.1 [−1.7, −0.5]%, P=.002.
**Comparator matched:** Yes, eTable 2 has year-12 HbA1c difference −1.1 [−1.7, −0.5], P<.001. The report supplement identifies ITT mixed-model visit contrasts. The model, year, outcome, direction, and displayed interval match.
**Consistency rule applicable:** Yes, matching abstract key-result P values across REPORTs (Route B). This is not a significant-versus-nonsignificant interval conflict; both P readings and the interval support significance.
**Calculation or logical comparison reproduced:** P=.002 half-unit range [.0015, .0025]; P<.001 is an inequality range [0, .001), not a rounded point. Their minimum gap has infimum .0005; relative discrepancy has infimum .0005/.002=.25, above .05. Estimate half-unit [−1.15, −1.05], lower-limit [−1.75, −1.65], and upper-limit [−.55, −.45] are identical between locations. No P is reconstructed from an assumed degrees-of-freedom convention.
**Necessary inputs available:** Yes for displayed matched-result disagreement; not for fitted-test reproduction.
**Exact missing inputs or definitions:** Exact test statistic, covariance, degrees of freedom/reference distribution, and which test produced each P value.
**Source-grounded alternative interpretation:** The fitted mixed model could use distinct contrast/test conventions. Main p1 notes a July 24, 2024 correction, but [main p9 correction notice](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=9) specifically identifies the ClinicalTrials.gov link. That notice does not substantiate a numerical revision explanation for this P-value comparison.
**Direct observation versus inferred explanation:** Direct: matching effect/CI with disjoint P readings. Inferred: a particular test or numerical report-version mechanism.
**Exact remaining human question:** Which test and P value belong to the year-12 −1.1 [−1.7, −0.5] contrast, and what explains the two supplied P readings?
**Determining recheck fact:** Both P strings and the matched effect/CI are visually confirmed in their exact source cells/paragraphs.

## C003 — Pooled mortality percentage

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT DOC-001 p. 1 abstract vs REPORT DOC-001 pp. 3, 4, 7, 8 cohort and death displays
**Evidence state:** reproduced
**Classification rationale:** Count/denominator/percentage accounting is statistical-results content entirely within one REPORT.
**Classification ambiguity:** An unidentified different pooled risk set would change the denominator.

**Location found:** Yes: [main p1 abstract cohort and deaths](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1), [p3 enrolled cohort](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), [p4 Table 1 headers](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=4), [p7 death paragraph](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=7), and [p8 Table 3 headers/Death row/footnote](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=8); all REPORT.
**Source value/text matched:** Yes, abstract supplies 262 enrolled and 4 deaths (2.2%), 2 in each group.
**Comparator matched:** Yes, p3/p4 identify 96 medical and 166 surgical, total 262; p7 identifies four deaths over 12 years, two per group; Table 3 gives 2 (2.1) of 96 and 2 (1.2) of 166, with causes in its footnote.
**Consistency rule applicable:** Yes, count/percentage within the abstract display (Route A, category 3), corroborated by body population/death counts.
**Calculation or logical comparison reproduced:** Central pooled 100×4/262=1.526717557%. Conservative full half-unit count [3.5,4.5] and N [261.5,262.5] give [1.333333333,1.720841300]%; printed 2.2% gives [2.15,2.25]%. Gap .429158700 percentage points, relative .429158700/2.2=.195072136. Even independently widening both arm death counts to [1.5,2.5] and denominators to [95.5,96.5]/[165.5,166.5] gives pooled [100×3/263,100×5/261]=[1.140684411,1.915708812]%; gap .234291188/2.2=.106495994. Each arm's central fraction, 2.083333333% and 1.204819277%, agrees with 2.1% and 1.2%.
**Necessary inputs available:** Yes for enrolled-population arithmetic.
**Exact missing inputs or definitions:** Any alternative denominator/risk-set or person-time definition underlying abstract 2.2%.
**Source-grounded alternative interpretation:** Mortality could use an unreported follow-up subset rather than Table 3's enrolled cohort; the abstract supplies no such distinction.
**Direct observation versus inferred explanation:** Direct: enrolled N, deaths, and printed percentages. Inferred: denominator selection, production mechanism, or which percentage should replace another.
**Exact remaining human question:** Which population denominator and mortality quantity produce 2.2%, and how do they relate to the 262 enrolled participants and Table 3?
**Determining recheck fact:** The full half-unit intervals remain separated above .05 relative discrepancy with both conservative denominator constructions.

## C004 — Primary HbA1c response scale

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R, S_C, S_W
**Compared document roles:** PLAN DOC-002 pp. 17, 26, 27, 29; REPORT DOC-001 pp. 2, 6; REPORT DOC-003 pp. 4, 15, 16
**Evidence state:** reproduced
**Classification rationale:** P_R is independently supported by prospective percent-response versus tabulated net-response definitions; S_W by main p2 percent label versus main p6 net-change footnote; S_C by main p2 percent label versus supplementary p15 net-change footnote. P_R outranks S_C and S_W. The plan is an actual compared specification, not mere corroboration.
**Classification ambiguity:** “Percent change” may be used loosely in main methods or may represent an undisclosed scale amendment.

**Location found:** Yes: PLAN [p17 primary endpoint](../../../joi240004supp1_prod_1721756962.80052.pdf#page=17), [p26 A1 response](../../../joi240004supp1_prod_1721756962.80052.pdf#page=26), [p27 hypothesis/power assumptions](../../../joi240004supp1_prod_1721756962.80052.pdf#page=27), [p29 Table A1/Figure A1](../../../joi240004supp1_prod_1721756962.80052.pdf#page=29); REPORT [main p2 outcome/statistical methods](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=2), [main p6 Table 2/footnotes](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), [supplement p4 primary model](../../../joi240004supp2_prod_1721756962.82552.pdf#page=4), [p15 eTable 2/footnote b](../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), [p16 continued footnote c](../../../joi240004supp2_prod_1721756962.82552.pdf#page=16).
**Source value/text matched:** Yes. Plan p17/26/29 define percent change from baseline; A1 explicitly defines its response as percent change and p27 its primary β7 as mean-percent-change difference. Power p27 assumes surgical −20% at year 5 to −15% at year 7; Figure A1 repeats −15% scenarios. Main p2 also labels both primary endpoint and primary modeled response “percent change.”
**Comparator matched:** Yes. Main Table 2 footnote b expressly states net change for HbA1c, separately from relative changes for other numeric outcomes; the row gives medical −.2, surgery −1.6, contrast −1.4. Supplement eTable 2 likewise states net HbA1c change and gives −.3/−1.4/−1.1 at year 12. Supplement p4 simply calls its response “change”; p16 defines numeric differences as surgery change minus medical change but repeats year-7 wording in the year-12 display. That repeated time label is contextual and is not an additional reproduced scale comparison.
**Consistency rule applicable:** Yes, primary response/quantity identity across plan and report and within report (Route B, focus D/C). Relative-percent change requires dividing net change by baseline and multiplying by 100; net change of an HbA1c percentage is a percentage-point quantity. The source's numerical power assumptions establish the relative scale.
**Calculation or logical comparison reproduced:** Three actual comparisons: PLAN relative-percent definition vs REPORT net definition (P_R); main p2 percent definition vs main p6 net definition (S_W); main p2 percent definition vs supplement p15 net definition (S_C). Agreeing main/supplement net footnotes are not themselves a conflict. Display-precision intervals and relative numerical discrepancy are not applicable to quantity definitions. Printed baseline means are not substituted into model estimates, and no model-versus-crude discrepancy is asserted.
**Necessary inputs available:** Yes for the scale/specification comparisons.
**Exact missing inputs or definitions:** The implemented response transformation and any supplied amendment reconciling it with the prospective relative-percent response.
**Source-grounded alternative interpretation:** Main methods may use “percent” as the unit of HbA1c, while the power model genuinely uses relative percent; or the outcome scale was deliberately amended. No supplied scale amendment resolves the comparison.
**Direct observation versus inferred explanation:** Direct: response definitions and distinguishable printed net/relative footnote categories. Inferred: which implementation generated the fitted contrasts and why definitions differ.
**Exact remaining human question:** Did the primary response change from relative-percent HbA1c change to net percentage-point change, and which implemented transformation generated the primary −1.4 and year-12 −1.1 contrasts?
**Determining recheck fact:** Both scales are explicitly instantiated in supplied content, and all three asserted relationships have distinct conflicting pairs.
## C005 — Remission medication-free window

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN DOC-002 pp. 18, 29 vs REPORT DOC-001 pp. 1, 2, 7
**Evidence state:** reproduced
**Classification rationale:** The key remission endpoint's prospective and retrospective medication-free windows differ in explicit specification. The abbreviated Figure 3 definition is not a separate REPORT conflict.
**Classification ambiguity:** An unsupplied operational definition or amendment could contain the reported duration.

**Location found:** Yes: PLAN [p18 remission item 2](../../../joi240004supp1_prod_1721756962.80052.pdf#page=18), [p29 Table A1 remission row](../../../joi240004supp1_prod_1721756962.80052.pdf#page=29); REPORT [main p2 remission definition](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=2), [p1 abstract remission rates](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1), [p7 Figure 3/caption](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=7). The associated reported OR is found in [main p6 Table 2](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6).
**Source value/text matched:** Yes. Both prospective definitions require HbA1c<6.5% off/without diabetes medication and do not specify duration.
**Comparator matched:** Yes. Main p2 explicitly requires no diabetes medication for at least 3 months, assessed annually. Abstract gives 7-year 6.2%/18.2%, P=.02 and 12-year 0.0%/12.7%, P<.001; Table 2 remission contrast OR 3.39 [1.25,9.17], P=.02. Figure 3 states HbA1c<6.5% and not receiving diabetes medications without repeating duration.
**Consistency rule applicable:** Yes, matching a key endpoint window across PLAN/REPORT (Route B). Annual assessment does not itself define a prior medication-free interval.
**Calculation or logical comparison reproduced:** The threshold and medication criterion agree; the report adds an explicit ≥3-month qualification absent from the supplied prospective definitions. This does not establish a plan zero-month criterion or a changed event count. Display-precision interval arithmetic is inapplicable to this endpoint-window definition comparison; 3 months is a logical requirement, not a count-derived estimate.
**Necessary inputs available:** Yes for the definition difference; not for participant reclassification.
**Exact missing inputs or definitions:** Prospective medication-free duration, ascertainment algorithm, any operative manual/amendment, and participant medication timing.
**Source-grounded alternative interpretation:** The report cites remission-definition publications; the plan refers to a Manual of Operations for detailed algorithms. Either could motivate operational elaboration, but neither supplied plan location contains the 3-month window.
**Direct observation versus inferred explanation:** Direct: the explicit versus unspecified duration. Inferred: a changed clinical endpoint or actual number reclassified; neither is asserted as established.
**Exact remaining human question:** Was the 3-month medication-free interval prospectively specified, and which interval was applied to the reported remission rates and OR?
**Determining recheck fact:** Exact supplied PLAN definitions omit duration while the REPORT definition adds it.

## C006 — Cardiovascular outcome status

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN DOC-002 pp. 18, 29, 30 vs REPORT DOC-001 pp. 1, 2, 8
**Evidence state:** reproduced
**Classification rationale:** This compares prospective outcome status with the report's stated secondary hierarchy; it is not a same-document count comparison.
**Classification ambiguity:** Safety and secondary status could coexist; plan p18 permits some dual-status endpoints without identifying this one.

**Location found:** Yes: PLAN [p18 secondary list/section 4.4](../../../joi240004supp1_prod_1721756962.80052.pdf#page=18), [p29 Table A1 Aim 2 efficacy entries](../../../joi240004supp1_prod_1721756962.80052.pdf#page=29), [p30 Table A1 continuation/safety entry](../../../joi240004supp1_prod_1721756962.80052.pdf#page=30); REPORT [main p2 other secondary outcomes](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=2), [p1 abstract cardiovascular finding](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1), [p8 Table 3 cardiovascular rows](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=8).
**Source value/text matched:** Yes. Plan Table A1 places major adverse cardiovascular events in Aim 2 Safety, while efficacy vascular outcomes are stroke, retinopathy, nephropathy and foot ulcer. Plan p18 says some study outcomes are also secondary, without designating major cardiovascular events as such.
**Comparator matched:** Yes. Main p2 explicitly includes major adverse cardiovascular events among other secondary outcomes; the abstract reports no difference in them. Main p8 lists cardiovascular events with 96/166 denominators rather than asserting a supplied common composite definition.
**Consistency rule applicable:** Yes, prespecified outcome-status comparison (Route A, category 5). A status discrepancy remains an evidence fact even with an alternative dual hierarchy.
**Calculation or logical comparison reproduced:** PLAN explicit Safety and REPORT explicit secondary status are different stated categories for the same named major cardiovascular outcome. Generic permission for dual status does not identify that outcome's prospective secondary designation. No numerical composite difference is inferred. Display precision is inapplicable to hierarchy labels.
**Necessary inputs available:** Yes for the printed status comparison.
**Exact missing inputs or definitions:** Specific prospective dual safety/secondary designation, any hierarchy amendment, and an operative mapping of the major cardiovascular outcome to Table 3 events.
**Source-grounded alternative interpretation:** Plan p18's “some endpoints” may include major cardiovascular events, making Safety and secondary compatible; the specific mapping is absent.
**Direct observation versus inferred explanation:** Direct: the different explicit status labels. Inferred: a deliberate hierarchy change or its consequences for interpretation; not established here.
**Exact remaining human question:** What prespecified outcome status and hierarchy apply to the abstract major cardiovascular result, and does it have dual safety/secondary status?
**Determining recheck fact:** The exact Table A1 safety label and the exact report secondary label both match registration.

## C007 — Primary baseline adjustment

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN DOC-002 pp. 26, 34 vs REPORT DOC-001 pp. 2, 3 and REPORT DOC-003 p. 4
**Evidence state:** reproduced
**Classification rationale:** The prospective primary covariate specification differs from the reported primary specification. Agreeing report methods and within-plan primary/sensitivity distinctions do not add S_C/S_W/P_P.
**Classification ambiguity:** The reported primary could be a selected planned sensitivity model or reflect an unsupplied amendment.

**Location found:** Yes: PLAN [p26 A1 and Z definition](../../../joi240004supp1_prod_1721756962.80052.pdf#page=26), [p34 further baseline sensitivities](../../../joi240004supp1_prod_1721756962.80052.pdf#page=34); REPORT [main p2 fixed-effect list](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=2), [p3 fixed-effect continuation](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), [supplement p4 primary model](../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
**Source value/text matched:** Yes. A1 primary list is group, yearly visit, interaction and site; Z is explicitly a four-dimensional site indicator vector. Plan p34 adds baseline HbA1c, BMI and other baseline characteristics differing at P<.05 in further sensitivity analyses.
**Comparator matched:** Yes. Main p2/p3 and supplementary p4 explicitly include baseline HbA1c among primary fixed effects, with group, visit, interaction, site and participant random intercept.
**Consistency rule applicable:** Yes, primary-analysis covariate/specification comparison (Route B). This differs from C008's absence of the full sensitivity result package.
**Calculation or logical comparison reproduced:** Itemwise group/visit/interaction/site and participant intercept agree; baseline HbA1c occurs in the reported primary but in the plan's further sensitivity list, not its explicitly site-only Z or primary list. No fitted estimate is recomputed and no numerical effect of adjustment is claimed. Display-precision arithmetic is inapplicable to a covariate-list comparison.
**Necessary inputs available:** Yes for the specification difference.
**Exact missing inputs or definitions:** Any final primary-model designation/amendment and whether the primary −1.4 [−1.8,−1.0] contrast came from the original A1 or a selected sensitivity model.
**Source-grounded alternative interpretation:** Selection of a prespecified sensitivity as the final primary model or incompleteness of the plan's primary list, though its Z definition explicitly restricts Z to site.
**Direct observation versus inferred explanation:** Direct: compared covariate lists and primary/sensitivity placement. Inferred: implementation chronology, amendment or numerical adjustment impact.
**Exact remaining human question:** Which planned or amended primary specification generated the reported HbA1c estimate, and what designation supports baseline HbA1c as a primary covariate?
**Determining recheck fact:** Exact list comparison reproduces the changed role of the baseline HbA1c covariate.

## C008 — Planned primary sensitivity package not reported

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN DOC-002 pp. 30, 31, 34 vs REPORT DOC-001 pp. 3, 9 and REPORT DOC-003 pp. 4, 5, 6, 9; absence checked across all main/report-supplement pages
**Evidence state:** reproduced
**Classification rationale:** Explicitly prespecified primary sensitivity results have no supplied corresponding report results. All compared obligations are PLAN-to-REPORT, consolidated as one absent sensitivity package.
**Classification ambiguity:** Unsupplied results or a final plan amendment may exist; censoring weights could be one under the reported random-censoring assumption.

**Location found:** Yes: PLAN [p30 MICE/Rubin/pattern-mixture/crossover sensitivity](../../../joi240004supp1_prod_1721756962.80052.pdf#page=30), [p31 treatment×censoring weight and postcrossover discard](../../../joi240004supp1_prod_1721756962.80052.pdf#page=31), [p34 expanded baseline sensitivities](../../../joi240004supp1_prod_1721756962.80052.pdf#page=34); REPORT [main p3 methods/sensitivity estimate](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), [p9 limitations](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=9), [supplement p4 model](../../../joi240004supp2_prod_1721756962.82552.pdf#page=4), [p5 IPW formula/assignment/missingness](../../../joi240004supp2_prod_1721756962.82552.pdf#page=5), [p6 continuation](../../../joi240004supp2_prod_1721756962.82552.pdf#page=6), [p9 eFigure 2](../../../joi240004supp2_prod_1721756962.82552.pdf#page=9).
**Source value/text matched:** Yes, all promised pattern components separately: (1) MICE and Rubin combination; (2) pattern-mixture dropout analysis; (3) product of treatment and censoring weights; (4) separate per-protocol analysis discarding outcomes after crossover; (5) further baseline HbA1c, BMI and imbalance sensitivities.
**Comparator matched:** Yes. Report describes medical-record recovery and MAR random censoring, plus treatment-IPW PP analysis. Supplement p5 expressly moves crossover patients from medical before crossover to surgery after it; its complete weight expression is a treatment-history probability ratio product without a separate censoring factor. It gives 2.5%/97.5% truncation and weighted mixed model with sandwich standard errors. Main p3/eFigure 2 supply that PP comparison, −1.5 [−2.1,−.9], P<.001 at year 7; p9 limitations acknowledge MAR/IPW assumptions.
**Consistency rule applicable:** Yes, explicit planned primary analyses without supplied results (Route A, category 5). This establishes nonreporting in the supplied package, not that the analyses were never conducted.
**Calculation or logical comparison reproduced:** All five promises were matched individually against complete main pp1–11 and results-supplement pp1–22, including the contents, methods, figure captions and tables. No supplied result identifies MICE/Rubin, pattern-mixture, postcrossover-discard, or the expanded BMI/imbalance primary sensitivity model. Baseline HbA1c in the reported primary does not provide the full promised expanded sensitivity package. Reassigning postcrossover treatment preserves those outcomes and cannot instantiate an outcome-discard analysis. The printed treatment-only weight does not document the separate planned censoring factor; under random censoring that factor might be one, so no numerical weight discrepancy is asserted. Display precision is inapplicable to promised-analysis/reporting correspondence.
**Necessary inputs available:** Yes for explicit promises and complete supplied-report absence; not for numerical implementation reproduction.
**Exact missing inputs or definitions:** Corresponding sensitivity estimates/results, implemented censoring-weight definition, designation of the reported IPW method relative to each plan promise, and any supplied replacement/amendment.
**Source-grounded alternative interpretation:** MAR may justify unity censoring weights; the reported treatment-IPW analysis may replace some planned sensitivities. An unsupplied amendment or separate results may resolve nonreporting.
**Direct observation versus inferred explanation:** Direct: future-tense promises, exact reported formula/assignment, and no matching supplied results. Inferred: whether analyses were performed, why omitted, or their numerical impact.
**Exact remaining human question:** Where are the planned primary MICE, pattern-mixture, outcome-discard and expanded-baseline sensitivity results, and what supplied specification maps the treatment/censoring-weight promise to the reported IPW analysis?
**Determining recheck fact:** The named promised analyses have no matching supplied result; the reported postcrossover reassignment is explicitly distinct from discard.

## C009 — Planned binary A2 and reported GEE

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN DOC-002 p. 27 vs REPORT DOC-001 pp. 3, 6 and REPORT DOC-003 pp. 4, 5, 15
**Evidence state:** reproduced
**Classification rationale:** The plan specifies the main key-secondary model A2; the report supplies another model family and no A2 result. Report method descriptions agree, so no REPORT-to-REPORT conflict is present.
**Classification ambiguity:** An unsupplied final analysis amendment may define the GEE replacement.

**Location found:** Yes: PLAN [p27 A2/secondary-model text](../../../joi240004supp1_prod_1721756962.80052.pdf#page=27); REPORT [main p3 binary/GEE paragraph](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), [p6 Table 2 binary rows](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), [supplement p4 binary GEE](../../../joi240004supp2_prod_1721756962.82552.pdf#page=4), [p5 continuation](../../../joi240004supp2_prod_1721756962.82552.pdf#page=5), [p15 eTable 2 binary rows](../../../joi240004supp2_prod_1721756962.82552.pdf#page=15).
**Source value/text matched:** Yes. Plan calls glycemic-control and remission analysis generalized linear mixed-effects logistic, displays A2 with patient random c_ij, identifies β7 as the log OR, and calls its year-7 test the main secondary analysis. Remission and partial remission use that same analysis.
**Comparator matched:** Yes. Main and supplement state GEE controlling for site and baseline HbA1c with sandwich standard errors; supplement adds group, visit and interaction, LS estimates by visit/group, and hypothesis-generating/unadjusted secondary results. Main Table 2 and year-12 eTable 2 display remission and glycemic-control ORs, including year-7 remission 3.39 [1.25,9.17], P=.02.
**Consistency rule applicable:** Yes, planned key-secondary main analysis replaced/not reported (Route A, category 5). The model-family distinction also has focus D; no preferred analysis is proposed.
**Calculation or logical comparison reproduced:** Patient-random-effect logistic A2 and described GEE/sandwich are explicitly different analysis specifications. The supplied REPORT describes GEE for the same remission/control outcomes and gives no A2 result. No crude OR is compared with a modeled OR. Display precision is inapplicable to model-family correspondence.
**Necessary inputs available:** Yes for analysis identity; not for refitting.
**Exact missing inputs or definitions:** Final operative plan/amendment, the GEE working/link specifications, and which conditional or marginal estimand/contrast the displayed ORs represent.
**Source-grounded alternative interpretation:** A final amendment could intentionally select GEE; matching displayed ORs between model families cannot be established without underlying model outputs.
**Direct observation versus inferred explanation:** Direct: source model names, A2 patient term, and GEE variance statement. Inferred: the size or direction of any estimand difference or why GEE was selected.
**Exact remaining human question:** Which supplied specification authorizes/maps the GEE analysis in place of A2, and what conditioning and estimand apply to the reported remission/control ORs?
**Determining recheck fact:** The exact planned A2 specification and reported GEE specification both match registration.
## C010 — Medical medication OR interval pattern

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT DOC-001 p. 6 medical medication OR cell vs all other binary OR cells on the same page; REPORT DOC-003 p. 4 is corroborating inference context only
**Evidence state:** reproduced
**Classification rationale:** One estimate/interval cell does not reproduce a method that reproduces every other binary cell within the same REPORT table. The supplementary GEE/sandwich description does not conflict with the table and adds no S_C.
**Classification ambiguity:** The anomalous cell could use an explicitly different asymmetric interval construction or contrast, neither specified in the supplied display.

**Location found:** Yes: REPORT [main p6 Table 2 use-of-medications medical change column and all binary comparator cells/footnotes](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), and corroborating REPORT [supplement p4 GEE/sandwich method](../../../joi240004supp2_prod_1721756962.82552.pdf#page=4). Every lower/upper limit and displayed decimal precision was visually checked.
**Source value/text matched:** Yes. Medical medication within-group OR is 0.10 [0.01,3.27]. The table identifies binary changes as year-7-over-baseline ORs and group comparisons as surgery-over-medical ORs.
**Comparator matched:** Yes. All 11 other within-group OR cells and all six between-group OR cells are transcribed below with source precisions. The surgery HbA1c<7 upper bound is 11.4, not 11.40; coarse remission bounds and trailing decimal places are retained.
**Consistency rule applicable:** Yes, Route A, category 4: a reproducing interval-center method supports every other row of the same display. This is neither an OR-versus-crude-ratio comparison nor a significant/nonsignificant conflict. The described GEE/sandwich inference supplies source context but does not by itself prove the interval convention.
**Calculation or logical comparison reproduced:** The log-symmetric interval's center is sqrt(L×U). For each printed L/U/OR allow its own last-digit half-unit interval. The center range is [sqrt(L_min×U_min), sqrt(L_max×U_max)]. For 0.10 [0.01,3.27], L∈[.005,.015], U∈[3.265,3.275] gives center [.127769323,.221641603], separated from OR [.095,.105] by .022769323; relative .022769323/.10=.227693234. All 17 comparator center intervals overlap their own OR intervals, with gap zero. This reproduces the pattern rather than presuming the anomalous cell's missing construction.

| Cell | Printed OR [CI] | OR half-unit interval | CI-derived center interval | Gap / relative discrepancy |
|---|---|---|---|---|
| Remission MED | 10.4 [0.4, 279.4] | [10.350000,10.450000] | [9.887997775,11.213942215] | 0.000000000 / 0.000000000 |
| Remission SURG | 36.2 [1.9, 699.0] | [36.150000,36.250000] | [35.959108721,36.920827456] | 0.000000000 / 0.000000000 |
| Remission comparison | 3.39 [1.25, 9.17] | [3.385000,3.395000] | [3.377932060,3.393320645] | 0.000000000 / 0.000000000 |
| Medication MED | 0.10 [0.01, 3.27] | [0.095000,0.105000] | [0.127769323,0.221641603] | 0.022769323 / 0.227693234 |
| Medication SURG | 0.03 [0.01, 0.11] | [0.025000,0.035000] | [0.022912878,0.041533119] | 0.000000000 / 0.000000000 |
| Medication comparison | 0.09 [0.03, 0.24] | [0.085000,0.095000] | [0.076648549,0.092601296] | 0.000000000 / 0.000000000 |
| Oral/GLP1 MED | 0.53 [0.29, 0.97] | [0.525000,0.535000] | [0.524428260,0.536306815] | 0.000000000 / 0.000000000 |
| Oral/GLP1 SURG | 0.74 [0.46, 1.20] | [0.735000,0.745000] | [0.737377108,0.748548596] | 0.000000000 / 0.000000000 |
| Oral/GLP1 comparison | 0.98 [0.53, 1.82] | [0.975000,0.985000] | [0.976153164,0.988116896] | 0.000000000 / 0.000000000 |
| Insulin MED | 1.93 [1.07, 3.46] | [1.925000,1.935000] | [1.918221833,1.929993523] | 0.000000000 / 0.000000000 |
| Insulin SURG | 0.18 [0.11, 0.31] | [0.175000,0.185000] | [0.178955302,0.190328663] | 0.000000000 / 0.000000000 |
| Insulin comparison | 0.13 [0.06, 0.29] | [0.125000,0.135000] | [0.125199840,0.138473824] | 0.000000000 / 0.000000000 |
| HbA1c<7 MED | 2.77 [1.38, 5.54] | [2.765000,2.775000] | [2.758736124,2.771249718] | 0.000000000 / 0.000000000 |
| HbA1c<7 SURG | 6.42 [3.63, 11.4] | [6.415000,6.425000] | [6.414339405,6.451414574] | 0.000000000 / 0.000000000 |
| HbA1c<7 comparison | 3.22 [1.76, 5.88] | [3.215000,3.225000] | [3.211016194,3.222890783] | 0.000000000 / 0.000000000 |
| HbA1c<6.5 MED | 2.30 [1.19, 4.47] | [2.295000,2.305000] | [2.300222815,2.312493243] | 0.000000000 / 0.000000000 |
| HbA1c<6.5 SURG | 4.44 [2.46, 8.01] | [4.435000,4.445000] | [4.433088652,4.444881888] | 0.000000000 / 0.000000000 |
| HbA1c<6.5 comparison | 2.89 [1.48, 5.64] | [2.885000,2.895000] | [2.882988900,2.895310864] | 0.000000000 / 0.000000000 |

**Necessary inputs available:** Yes for the within-display reproducing center method and full rounding calculation.
**Exact missing inputs or definitions:** Cell-specific interval construction, contrast identification, and original fitted estimate/limits. No alternative numerical OR or bound is selected.
**Source-grounded alternative interpretation:** A distinct asymmetric interval convention or a different matched contrast could produce an interval not centered on the printed OR; the same-table method pattern otherwise reproduces all binary cells.
**Direct observation versus inferred explanation:** Direct: source cell and 17 comparators, all input precisions, and interval overlap/gap results. Inferred: common log-symmetric procedure or any particular production mechanism.
**Exact remaining human question:** Which interval construction and contrast produced medical medication OR .10 [.01,3.27], and why does its center relationship differ from all other binary cells?
**Determining recheck fact:** Exact visually confirmed values still have .227693234 relative interval-gap discrepancy under the method reproducing all other Table 2 OR cells.

## C011 — Vascular and safety test mapping

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN DOC-002 pp. 26, 34, 35 vs REPORT DOC-001 pp. 1, 7 and REPORT DOC-003 pp. 6, 17, 19, 20, 21
**Evidence state:** reproduced
**Classification rationale:** This is an unresolved correspondence between prospective vascular/safety analysis and reported result tests. REPORT descriptions agree with each other, so no S_C/S_W is added. The separate baseline CMH paragraph is contextual, not proof of event strata.
**Classification ambiguity:** CMH strata are unspecified; “chi-squared” may abbreviate CMH, sparse-outcome Fisher substitution may apply, or planned composites and reported individual-row tests may differ.

**Location found:** Yes: PLAN [p34 Aim 2 vascular/safety paragraph](../../../joi240004supp1_prod_1721756962.80052.pdf#page=34), [p35 power/secondary continuation](../../../joi240004supp1_prod_1721756962.80052.pdf#page=35), [p26 separate baseline-comparison CMH paragraph](../../../joi240004supp1_prod_1721756962.80052.pdf#page=26); REPORT [main p1 abstract cardiovascular statement](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1), [p7 event/procedure narrative](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=7), [supplement p6 event-test methods](../../../joi240004supp2_prod_1721756962.82552.pdf#page=6), [p17 nutritional categorical comparisons](../../../joi240004supp2_prod_1721756962.82552.pdf#page=17), [p19 eTable 5 example P cells](../../../joi240004supp2_prod_1721756962.82552.pdf#page=19), [p20 eTable 5 footnote b](../../../joi240004supp2_prod_1721756962.82552.pdf#page=20), [p21 eTable 6/footnote b](../../../joi240004supp2_prod_1721756962.82552.pdf#page=21).
**Source value/text matched:** Yes. Plan p34 says microvascular/macrovascular events will be summarized as 2×2 tables and compared by Cochran-Mantel-Haenszel, and major adverse events/complications analyzed in the same manner. It does not name the CMH strata. Plan p26 separately uses CMH for baseline categorical characteristics; its continuous baseline model includes site, which cannot be imported as an explicit event-stratum specification.
**Comparator matched:** Yes. Supplement p6 says adverse events/study outcomes are compared using chi-squared or Fisher's exact tests; eTable 5 p20 and eTable 6 p21 repeat that pair in footnote b. Nutritional eTable 3 p17 supplies MED-versus-SURG/surgical-subgroup P values and observed-data denominators, while its footnote identifies the comparison rather than a row-specific test. Visually confirmed example results: p19 abdominal pain 10/96 vs 37/166, P=.02; dysphagia 0/96 vs 12/166, P=.005; p21 crossover/conversion/revision 24/96 vs 15/166, P<.001. Main p7 maps the safety/procedure narrative to these displays and p1 gives the key cardiovascular finding.
**Consistency rule applicable:** Yes, primary/key-outcome and safety analysis mapping (Route B, focus D). No claim that a particular P fails a proven stratified-vs-unstratified calculation is made.
**Calculation or logical comparison reproduced:** Explicit prospective CMH and explicit retrospective chi-squared/Fisher labels lack a supplied test-by-outcome mapping. This reproduces the registered analysis-specification uncertainty; it does not establish that all reported tests changed. Half-unit ranges of example printed P values are [.015,.025] and [.0045,.0055], with <.001 an inequality bound; these are locators, not cross-copy numeric discrepancies. Display-gap arithmetic is inapplicable to the test-name/mapping comparison. No site-stratified result can be reconstructed because the event strata and stratum counts are absent.
**Necessary inputs available:** Yes for source specification/mapping comparison; no for identifying each executed test or reproducing a CMH statistic.
**Exact missing inputs or definitions:** CMH strata; stratified event 2×2 counts; whether chi-squared denotes CMH or an ordinary Pearson statistic; Fisher substitution rule; row/composite mapping and test-specific output.
**Source-grounded alternative interpretation:** CMH has a chi-squared reference distribution, so the broad report label may encompass it; sparse outcomes may use Fisher; planned composite analysis may coexist with row-level report tests. These alternatives remain unresolved by the supplied descriptions.
**Direct observation versus inferred explanation:** Direct: the named prospective method, broad reported pair and actual P cells. Inferred: site stratification, an unstratified execution, or numerical consequences; none is asserted.
**Exact remaining human question:** Which reported tests instantiate the planned vascular/safety CMH analysis, what strata and substitution rules apply, and what mapping or amendment explains the remaining result tests?
**Determining recheck fact:** Exact methods text confirms an unspecified CMH-to-chi-squared/Fisher mapping, retaining all source-grounded alternatives.

## C012 — Fixed site and power variance specification

**Review domain:** plan_material
**Relationship type:** P_P
**All relationships:** P_P
**Compared document roles:** PLAN DOC-002 p. 26 A1/site definition vs PLAN DOC-002 pp. 28, 31 power/heterogeneity; REPORT DOC-001 pp. 2, 3 and REPORT DOC-003 p. 4 corroborate only
**Evidence state:** reproduced
**Classification rationale:** Both conflicting specifications are inside the prospective PLAN. The fixed-site REPORT model agrees with one side and is not a PLAN-to-REPORT inconsistency, so P_R is not added.
**Classification ambiguity:** A finite-site coefficient spread or a separate generative random-site model could define σ_b, but the plan does not identify either correspondence.

**Location found:** Yes: PLAN [p26 A1/b_i/Z definition](../../../joi240004supp1_prod_1721756962.80052.pdf#page=26), [p28 primary power variance-component paragraph](../../../joi240004supp1_prod_1721756962.80052.pdf#page=28), [p31 heterogeneity/distribution paragraph](../../../joi240004supp1_prod_1721756962.80052.pdf#page=31); corroborating REPORT [main p2 primary model](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=2), [p3 fixed-effect continuation](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), [supplement p4 fixed-site model](../../../joi240004supp2_prod_1721756962.82552.pdf#page=4). PLAN [p27 identifiability clause](../../../joi240004supp1_prod_1721756962.80052.pdf#page=27) was also reread.
**Source value/text matched:** Yes. A1 explicitly calls b_i a fixed site effect, defines Z as site indicators, specifies a Gaussian patient random c_ij with variance σ_c², and defines Gaussian residual covariance Σ_e. Plan p27 permits appropriate coefficient constraints for identifiability.
**Comparator matched:** Yes. Power p28 says power under A1 is estimated by Monte Carlo and that fitted mixed-model variance components are σ_b=.06, σ_c=.15, σ_e=.10, ρ=.13 with AR(1) residual covariance, with 500 simulations. Plan p31 says site changes follow some distribution and describes the final interval as the degree of heterogeneity. REPORT models explicitly use fixed site and participant random intercept.
**Consistency rule applicable:** Yes, a logical gap in relied-on prospective primary model/power inputs (Route B, focus C/D). Duplicate site coding is not the registered issue because the identifiability clause leaves room for constraints.
**Calculation or logical comparison reproduced:** The fixed-site A1 defines no stochastic b_i distribution/σ_b² parameter, while its linked power paragraph calls σ_b=.06 a variance component fitted under that mixed model. The distribution/heterogeneity paragraph does not supply the missing parameterization or separate simulation model. This is an observable model-to-power correspondence gap, not a claim that simulation power is numerically impossible. Numeric display precision is inapplicable: half-unit σ_b [.055,.065] is still a nonzero described variance-scale quantity, while A1 lacks its definition rather than providing a competing rounded estimate. No value-zero comparison is imposed on a fixed effect.
**Necessary inputs available:** Yes for fixed/variance-component wording and model definition comparison; no for full Monte Carlo reproduction.
**Exact missing inputs or definitions:** What σ_b measures (standard deviation, variance, finite-site spread or generative parameter); simulation site distribution; relationship of generating and fitted models; complete simulation implementation and constraints.
**Source-grounded alternative interpretation:** Fixed site coefficients could have an empirical finite-site spread .06, or a separate random-site generating model could supply .06 while fitting fixed-site A1. Both can be coherent but neither is identified in the supplied power description.
**Direct observation versus inferred explanation:** Direct: fixed b_i, reported σ_b variance component, and distribution/heterogeneity claims. Inferred: random-site fitting, a numerical power consequence, or a specific implementation mechanism.
**Exact remaining human question:** What does σ_b=.06 represent, and how does the model used for the primary power simulation correspond to the fixed-site A1 analysis?
**Determining recheck fact:** Exact source A1 and linked power text reproduce the undefined fixed-site-to-variance-component correspondence; reporting context only corroborates the fixed-site side.

## C013 — Appendix randomization-dropout accounting

**Review domain:** plan_material
**Relationship type:** P_P
**All relationships:** P_P
**Compared document roles:** PLAN DOC-002 p. 55 randomized/intervention rows vs PLAN DOC-002 p. 56 attached dagger footnote; PLAN DOC-002 p. 27 corroborates row totals
**Evidence state:** reproduced
**Classification rationale:** The prospective study-population enrollment accounting is inside one PLAN display continued across two pages, with a footnote explicitly attached to initiation. It bears on the planned enrollment pool; final REPORT cohort numbers are not compared.
**Classification ambiguity:** The 38 dropouts may refer to a different historical snapshot/population or category, but the attached display identifies none.

**Location found:** Yes: PLAN [p55 Appendix 2 table title, # Randomized and Number underwent intervention† rows](../../../joi240004supp1_prod_1721756962.80052.pdf#page=55), [p56 table continuation and dagger definition/dropout statement](../../../joi240004supp1_prod_1721756962.80052.pdf#page=56), and corroborating PLAN [p27 randomized/initiated population paragraph](../../../joi240004supp1_prod_1721756962.80052.pdf#page=27).
**Source value/text matched:** Yes. The five columns represent STAMPEDE, TRIABETES, SLIMM-T2D RYGB, SLIMM-T2D LAGB and CROSSROADS. Randomized counts are 155,69,43,45,43; initiated counts are 154,61,38,40,32. The display title is “Initial Trials: Enrolled Participants.”
**Comparator matched:** Yes. Its dagger footnote first defines intervention initiation as medical/lifestyle treatment or surgery, immediately then states 38 patients dropped at randomization, were not followed, and do not qualify for ARMMS-T2D enrollment. Plan p27 explicitly reports 355 randomized and 325 initiated.
**Consistency rule applicable:** Yes, counts within one continued display and its attached definition (Route A, category 3), concerning the planned eligible enrollment pool. This is not a comparison of administrative calendars or final-report withdrawals.
**Calculation or logical comparison reproduced:** Randomized sum 155+69+43+45+43=355; initiated sum 154+61+38+40+32=325; row-accounting difference 30. Full half-unit inputs: randomized summed interval [352.5,357.5], initiated summed interval [322.5,327.5], difference [25,35]. Footnote 38 interval [37.5,38.5]; gap 2.5; relative 2.5/38=.065789474>.05. Corroborating printed total intervals [354.5,355.5] minus [324.5,325.5]=[29,31] have gap 6.5/38=.171052632; the five-column calculation is the conservative basis. Counts are actually integers, but widening them respects the workflow display rule.
**Necessary inputs available:** Yes for every five-column count and attached dropout statement.
**Exact missing inputs or definitions:** Population/time point and mutually exhaustive meaning of the 38-dropout category relative to randomized minus initiated counts.
**Source-grounded alternative interpretation:** The footnote could refer to a different historical snapshot, overlapping categories, or another enrollment pool; neither p55/p56 nor the corroborating p27 identifies that distinction.
**Direct observation versus inferred explanation:** Direct: all row cells, dagger placement and exact dropout statement. Inferred: which historical snapshot or count should change; no final report population is substituted.
**Exact remaining human question:** Which population and time point supply 38 randomization dropouts, and how do they reconcile with the attached display's 355 randomized and 325 initiated participants?
**Determining recheck fact:** The same-display totals and attached footnote remain separated above .05 relative discrepancy after the widest input rounding calculation.

## C014 — Other race count and percentage

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT DOC-003 p. 14 eTable 1 Other-race count, percentage, column denominator and footnotes
**Evidence state:** reproduced
**Classification rationale:** Count/percentage/denominator conflict is within one REPORT display. The main baseline table is not a comparator, so this is not a peripheral cross-copy baseline comparison and adds no S_C.
**Classification ambiguity:** An alternative race-specific denominator or count is possible but unspecified.

**Location found:** Yes: REPORT [supplement p14 eTable 1 7-year column, race rows and footnotes a/b](../../../joi240004supp2_prod_1721756962.82552.pdf#page=14).
**Source value/text matched:** Yes, 7-year N=262; Race Other 4 (1.9), Black 81 (30.9), White 176 (67.2). Footnote a says categorical variables are n (%); footnote b says all study participants reached 7 years.
**Comparator matched:** Yes, the same column's N=262 and its categorical n (%) definition are the denominator/quantity comparator. No race-specific denominator is printed. The 12-year Other 2 (1.5), N=130 is a different column and is not the disputed pair.
**Consistency rule applicable:** Yes, count/denominator/percentage in one display (Route A, category 3).
**Calculation or logical comparison reproduced:** Central 100×4/262=1.526717557%. Full half-unit count [3.5,4.5], N [261.5,262.5], recomputed percentage [1.333333333,1.720841300]%; printed 1.9 interval [1.85,1.95]%. Gap .129158700 percentage points; relative .129158700/1.9=.067978263>.05. Adjacent race counts sum 81+176+4=261; using even exact 261 as a race-specific denominator gives 1.53256705%, which does not explain 1.9. The one-person total difference itself is a corroborating detail, not a separate registered issue.
**Necessary inputs available:** Yes for source count, column N and percentage.
**Exact missing inputs or definitions:** Any race-specific denominator, alternative count, missing-race rule or assignment explaining 1.9%.
**Source-grounded alternative interpretation:** A distinct denominator or count could underlie the percentage; the table's footnotes instead identify the full 7-year population and n (%) entries.
**Direct observation versus inferred explanation:** Direct: exact Other cell, N and footnotes, and full rounding calculation. Inferred: which input should differ or any production mechanism.
**Exact remaining human question:** Which Other-race count, denominator and percentage apply to the 7-year population, and how should the supplied 4 (1.9) cell be read?
**Determining recheck fact:** Exact source reading preserves a .067978263 relative half-unit interval-gap discrepancy.
## Derivative provenance and scope closure

Compute device: CPU, as recorded in tooling_record.md. Direct engine: Poppler 26.01.0. No OCR, fallback environment, Office extraction, external literature, or custom Python was needed. Deterministic JavaScript arithmetic calculated the full rounding bounds after exact visual transcription; it did not select candidates or replace scientific reasoning.

Existing current-run direct-source layout text used as a locator: preprocessing/screen_main_direct.txt (DOC-001 pp1–11), preprocessing/screen_plan_direct.txt (DOC-002 pp1–65), preprocessing/screen_report_supp_direct.txt (DOC-003 pp1–22). These current-run source-extraction artifacts were not modified.

Previously rendered current-run source images visually reread:
- Main physical pages 1, 3, 6: preprocessing/screen_main1.png, preprocessing/screen_main3.png, preprocessing/screen_main6.png.
- PLAN physical pages 26, 27, 28, 29, 31: extraction/protocol_first_half_visual/page-26.png, page-27.png, page-28.png, page-29.png, page-31.png.
- PLAN physical pages 55, 56: preprocessing/screen_plan55.png, preprocessing/screen_plan56.png.
- Results-supplement physical pages 14, 15: preprocessing/screen_supp14.png, preprocessing/screen_supp15.png.
- Results-supplement physical pages 17, 19, 20, 21: preprocessing/stat_extra_source17.png, preprocessing/stat_extra_source19.png, preprocessing/stat_extra_source20.png, preprocessing/stat_extra_source21.png.

Fresh uniquely owned CPU page renderings used Poppler pdftoppm command pattern:
`pdftoppm -f N -l N -singlefile -scale-to 2100 -png SOURCE .ai_paper_validation/review_1_6_2/preprocessing/recheck_PREFIXN`.

| Source | Physical page | Engine / device | Output path |
|---|---:|---|---|
| DOC-001 | 2 | Poppler 26.01.0 pdftoppm / CPU | preprocessing/recheck_main2.png |
| DOC-001 | 4 | Poppler 26.01.0 pdftoppm / CPU | preprocessing/recheck_main4.png |
| DOC-001 | 7 | Poppler 26.01.0 pdftoppm / CPU | preprocessing/recheck_main7.png |
| DOC-001 | 8 | Poppler 26.01.0 pdftoppm / CPU | preprocessing/recheck_main8.png |
| DOC-001 | 9 | Poppler 26.01.0 pdftoppm / CPU | preprocessing/recheck_main9.png |
| DOC-002 | 17 | Poppler 26.01.0 pdftoppm / CPU | preprocessing/recheck_plan17.png |
| DOC-002 | 18 | Poppler 26.01.0 pdftoppm / CPU | preprocessing/recheck_plan18.png |
| DOC-002 | 30 | Poppler 26.01.0 pdftoppm / CPU | preprocessing/recheck_plan30.png |
| DOC-002 | 34 | Poppler 26.01.0 pdftoppm / CPU | preprocessing/recheck_plan34.png |
| DOC-002 | 35 | Poppler 26.01.0 pdftoppm / CPU | preprocessing/recheck_plan35.png |
| DOC-003 | 4 | Poppler 26.01.0 pdftoppm / CPU | preprocessing/recheck_supp4.png |
| DOC-003 | 5 | Poppler 26.01.0 pdftoppm / CPU | preprocessing/recheck_supp5.png |
| DOC-003 | 6 | Poppler 26.01.0 pdftoppm / CPU | preprocessing/recheck_supp6.png |
| DOC-003 | 9 | Poppler 26.01.0 pdftoppm / CPU | preprocessing/recheck_supp9.png |
| DOC-003 | 16 | Poppler 26.01.0 pdftoppm / CPU | preprocessing/recheck_supp16.png |

Sources for the above renderings are, respectively, jama_courcoulas_2024_oi_240004_1721756962.76052.pdf, joi240004supp1_prod_1721756962.80052.pdf, and joi240004supp2_prod_1721756962.82552.pdf. No supplied source or reused asset was altered.

Closure: every assigned ID and each affected compared location is covered. Fourteen evidence states are reproduced; zero require transcription correction; zero are not_reproduced. All classifications retain the provisional domain/type/relationship set, with specific source-content reasons. C011's additional page-19 example location and C002's page-9 contextual notice are explicit truthful additions. No scientific source-location gap remains in this recheck scope. Missing model outputs, implementation details, test mappings, prospective windows/status designations, alternative denominators and unsupplied amendments are named separately in each card and remain human questions. All stable IDs remain Pending Human Adjudication.

# Complete checker exclusions for statistical pass 2

This current-run locator preserves every original checker exclusion row verbatim. The second statistical pass must reread the cited source locations against all route A categories and the display-precision rule. No scientific decision is added here.


## numeric_consistency.md — original exclusion table

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 p3 Figure1 N026 | Arm branches193+122=315 versus parent305. Half-unit sum[314,316], parent[304.5,305.5]; relative gap8.5/305=.027869≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p1/p3 cohort summary and p4 Table1 N004/N029/N044 | White177/262=67.5573% versus67.2%. Relative discrepancy below.05 even before allowing half-unit counts; rounded input intervals overlap printed interval. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p4 Table1 β-blockers N066 | B30/166=18.0723% versus18.2%; half-unit ratio interval[17.7177,18.4290] overlaps[18.15,18.25]. Explicit subgroup35 denominator also supports30/165=18.1818%. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p3 HbA1c and p6 Table2 N031 | Raw B7.2−8.7=−1.5 versus modeled table−1.6; half-unit difference interval[−1.6,−1.4] overlaps[−1.65,−1.55]. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p4 Table1 triglycerides and urine albumin:creatinine N059/N061 | Mean(SD) label accompanies two-ended parenthetic ranges; field reader recognizes range-format summaries; no source-grounded numeric contradiction or result-changing quantity is established. | TERMINOLOGY_OR_WORDING |

## numeric_consistency.md — original exclusion table

| Location | Observation | Reason code |
|---|---|---|
| DOC-001 p6 Table2 fasting-glucose change row | MED point change lacks the percent sign printed on its interval and other cells; footnoteb explicitly specifies relative percent change and fixes the unit without changing a number. | NOTATION_OR_TYPOGRAPHY |
| DOC-003 pp15–16 eTable2 footnotesa–c | Several footnotes say year7 while the title, all value columns and footnotee say year12; this footnote template wording does not change the printed values or leave their visit unidentified. | CONTEXT_RESOLVES |
| DOC-003 p18 eTable4 Calcium difference SE | Printed SE0.0 at one decimal can represent a small positive value below0.05; groupSE0.04/0.03 and P.03 therefore do not establish an exact-zero-SE contradiction. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 p6 Table2 and DOC-003 pp15–16 eTable2 raw summaries versus adjusted changes/ORs | Arithmetic of marginal baseline/visit means and crude percentages differs from some model estimates; footnotes and supplementary mixed-model/GEE specifications identify the estimates as model-based. | MODEL_VERSUS_CRUDE |

## numeric_consistency.md — original exclusion table

| Location | Observation | Reason code |
|---|---|---|
| [PLAN p9](../../../joi240004supp1_prod_1721756962.80052.pdf#page=9), [PLAN p16](../../../joi240004supp1_prod_1721756962.80052.pdf#page=16) | BMI<35 prevalence35% versus one third: even treating one third as33.333%, printed35% lower bound34.5 gives gap1.1667/35=.03333≤.05; approximate prevalence does not reproduce beyond display threshold. | ROUNDING_OR_DISPLAY_PRECISION |
| [PLAN pp32–33](../../../joi240004supp1_prod_1721756962.80052.pdf#page=32), TableA4p33 | RYGB narrative150cm Roux limb exceptBWH75cm/approx50cm BP limb versusCROSSROADS table100–150cm/30–50cm describes historical operative ranges; it changes no primary/key-secondary result, analysis population, randomized-intervention dose/duration, or statistical decision rule. | PERIPHERAL_COMPARISON |
| [PLAN p35](../../../joi240004supp1_prod_1721756962.80052.pdf#page=35), TableA5 | Plain layout readsrho=0.11 by adjoiningrho=.1 and superscriptfootnote1. Footnote1 and surrounding autocorrelation range make the readingrho=.1 immediately clear; no numerical source substitution reproduced. | NOT_REPRODUCED |
| [PLAN p28](../../../joi240004supp1_prod_1721756962.80052.pdf#page=28), control-power paragraph | A specific extrapolation from75/63/48% and52/38/22% to39/11% would require assuming a fitted slope/intercept or which historical points define the assumed linear log-odds curves. They are not printed, and the year7 values are simulation assumptions rather than count-derived results; no unique arithmetic conflict reproduced here. The explicit trend claim remains assigned to statistical review. | CONDITIONAL_OR_UNREPORTED |
| [PLAN p35](../../../joi240004supp1_prod_1721756962.80052.pdf#page=35), detectable weight difference | Central delta.43–.47×residualSD6% gives2.58–2.82%, including statedapproximately2.8%; mandated rounded-input interval2.3375–3.0875% overlaps printed2.8±.05%. An apparent challenge that2.8 must equal.43×6 has zero interval gap. | ROUNDING_OR_DISPLAY_PRECISION |

## cross_source_consistency.md — original exclusion table

| Location | Observation | Reason code |
|---|---|---|
| Mainp4Table1 vs supplementp14eTable1 | Repeated descriptive baseline medians/IQRs,rounding and cohort-table summaries differ in some cells; these are cross-copy baseline descriptors, not primary/key results or within-display count discrepancies. | PERIPHERAL_COMPARISON |
| Mainp5Figure2 contributor rows vs supplementp12eFigure5 and medicationp10eFigure3 | Visit-specific observation counts differ across outcomes; no matched analysis-set total discrepancy follows. | PERIPHERAL_COMPARISON |
| Mainp7Figure3 contributor rows vs mainp6Table2 headers and medication narrative | Different outcome-specific measurement availability versus group headers; does not assert a different enrolled population. | PERIPHERAL_COMPARISON |
| Mainp1/p4 remissionOR3.4[1.3,9.2] vs mainp6OR3.39[1.25,9.17] | Rounded copies overlap respective half-unit intervals; relative gaps≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| Mainp8 remission51/18/6 vs mainp1/p4 50.8/18.2/6.2 | Discussion rounded percentages; half-unit intervals overlap or residual discrepancy≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| Mainp4 narrativeHbA1c≤6.5 vs mainp6Table2HbA1c<6.5 | Equality-symbol difference in adjacent explanation of same explicitly labeled table row; no different numerical result supplied. | NOTATION_OR_TYPOGRAPHY |
| Supplementp13eFigure6BMI>35 vs mainp7BMI≥35 | Figure inequality symbol omits equality while complementaryBMI<35 group and same caption values identify the intended split immediately. | NOTATION_OR_TYPOGRAPHY |
| Supplementpp15–16eTable2 year12 title/values vs year7 wording in footnotes | Reused year7 wording in footnotes; title,year12 column heads and special12year remission footnote identify the visit immediately, with no conflicting counterpart value beyond separately emittedP issue. | CONTEXT_RESOLVES |
| Mainp6/eTable2 modeled changes vs raw baseline/follow-up differences or crudeOR | AdjustedLS/GEE estimates need not equal crude summary differences or odds ratios. | MODEL_VERSUS_CRUDE |
| Protocolp17 original age≥20 vs mainp2/supplementp3 age18–65 | Historical parent-eligibility age boundaries differ; no supplied count identifies enrolled18/19yearolds or an analysis-population size change, and this is not a primary/key endpoint or decision-rule discrepancy. | PERIPHERAL_COMPARISON |
| Protocolp17 general anesthesia “or” exercise vs supplementp3 anesthesia/exercise criteria | Parent cohorts comprise surgical and lifestyle arms; descriptions do not identify a different quantitative analysis set. | TERMINOLOGY_OR_WORDING |
| Protocolp17 BMI>27 vs report BMI27–45 shorthand | Original range shorthand differs at boundary symbol; no different population count/result is attributed. | TERMINOLOGY_OR_WORDING |
| Protocolp17 pregnancy screening+baseline vs supplementp3 baseline only, willingness/compliance omitted in shortened report list | Abbreviated original-trial summary omits details; no conflicting enrolled analysis-population or outcome count supplied. | CONDITIONAL_OR_UNREPORTED |
| Protocolpp7,16 “up to13” vs report through12 | Prospective maximum follow-up description and final available report window do not replace the7year primary endpoint. | CONTEXT_RESOLVES |
| Protocolpp16–17 additional7year vs fiveyear common data-collection wording | Follow-up calendar/administrative duration varies within protocol; no change to primary7year decision rule or randomized intervention duration established. | PERIPHERAL_COMPARISON |
| Protocolp27 power325 initiated vs appendixp55 sum325 and other sections302/316 | Prospective/historical availability snapshots and final enrollment taken at different times; not conflicting final analysis-set counts. | PERIPHERAL_COMPARISON |
| Protocolp32/33 surgical counts192 vs final original-assignment/enrolled procedure counts | Planning completed-surgery snapshot and reported later assignment/enrollment sets are different quantities. | PERIPHERAL_COMPARISON |
| Protocolpp32–33 RYGB limb narrative75/150 vs tableUW100–150cm/BPlimb30–50 | Surgical construction range/approximation does not change primary/key analysis or intervention duration/dose statement in report. | PERIPHERAL_COMPARISON |
| Protocolp31 exploratory four-arm analysis vs supplementp4 “secondary analysis” | Same planned nonprimary model and four comparisons; “secondary analysis” does not designate a different outcome status or claim additional prespecification. | TERMINOLOGY_OR_WORDING |
| Protocolp29 QoL percent change vs p18change wording | QoL is nonkey and not relied on for a reported primary/key estimate; no finalQoL number conflicts. | PERIPHERAL_COMPARISON |
| Protocol secondaryrelapse/QoL/UKPDS and ancillarycostutility vs complete report | Unreported nonkey outcomes/other-paper ancillary analyses; no claim of primary/key designation or substitution; omission alone beyond mandated primary/key analysis scope. | CONDITIONAL_OR_UNREPORTED |
| Protocol exploratory taxonomy/predictor models vs report | Additional exploratory analyses absent from package; no report claim that such absent analysis was prespecified/performed. | CONDITIONAL_OR_UNREPORTED |
| Protocolp31 Bonferroni vs supplementp4 unspecified multiplicity adjustment | Report says pairwise adjustment; missing named adjustment detail alone supplies no conflicting rule/value. | CONDITIONAL_OR_UNREPORTED |
| Protocol residual covarianceAIC vs report random-intercept description | Unreported residual-covariance selection does not itself contradict printed primary model/value. | CONDITIONAL_OR_UNREPORTED |
| Protocolp36SAS9.3 vs reportSAS9.4 | Software release difference does not by itself conflict with quantitative analysis/model. | OUT_OF_FOCUS |
| Protocolp1Version6b vs footerVersion6 | Cover/footer version abbreviation; no distinct supplied statistical version or conflicting analysis inferred. | PERIPHERAL_COMPARISON |
| Mainp7 GI excess statement and supplementeTable5 nauseaP=.054 | “More” denotes higher printed counts, not explicit statistically significant nausea comparison;P applies its own event row. | CONTEXT_RESOLVES |
| Mainp7 nonsignificantSBP/LDL at7y vs supplementeFigure5 overallP=.16/.83 | Apparent alternativeP values compare overall trajectories rather than7year contrasts; the result direction reconciles after model/time matching. | NOT_REPRODUCED |

## statistical_pass_1.md — original exclusion table

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC001 Table2/DOC003 eTable2, all model estimates; DOC001 Figures2/3 and DOC003 eFigures2/3/5/6 | Crude changes/odds from raw means, percentages or contributor counts differ from adjusted LS/GEE estimates; modeled baseline loss points may differ from raw zero-change values. Source does not identify those estimates as crude. | MODEL_VERSUS_CRUDE |
| REPORT DOC003 pp15-16 eTable2 footnotes | Several copied footnotes say year7 although the table heading, columns and remission footnote identify year12; the immediate display establishes the intended visit. | CONTEXT_RESOLVES |
| REPORT DOC001 p4 narrative versus p6 glycemic-threshold row | Narrative HbA1c≤6.5 versus table HbA1c<6.5 symbol in the same matched P=.002 result; no changed printed value or boundary-subgroup result supplied. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC003 p13 eFigure6 caption versus DOC001 p7/SAP BMI analysis | BMI>35 caption versus ≥35 complement of <35 analysis; no affected boundary participant or changed result identified. | NOTATION_OR_TYPOGRAPHY |
| PLAN DOC002 pp26-27 A1 | Both gamma^T Z and b_i represent fixed-site terms, but the source explicitly permits coefficient constraints for identifiability. This is distinct from the emitted power variance-component comparison. | CONTEXT_RESOLVES |
| REPORT DOC003 pp5-6 GEE missingness assertion | General MAR handling cannot be reconstructed from GEE/sandwich description alone without the outcome/observed-case mechanism or missingness-weight implementation. No raw mechanism or conflicting numeric estimate is supplied; the concern depends on an unstated mechanism. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC002 p28 glycemic-control power projection | Diagnostic ordinary linear fit of logits to75/63/48% preliminary surgery rates predicts about34% atyear7 rather than assumed39%; source does not specify a fit to those points or require them as exact constraints. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC002 pp18,27,31-36 and61-63; complete REPORT DOC001/DOC003 | No supplied report results for non-key QOL/UKPDS/BMI, descriptive relapse, exploratory taxonomy/predictor models or ancillary ICER; absence alone does not establish missing primary/key-secondary analysis or a prespecification claim. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC002 p35 TableA5 footnote | Common SD is described as a covariance diagonal element; nearby SD6% and standardized-effect definition make the intended dispersion quantity clear without a changed printed estimate. | TERMINOLOGY_OR_WORDING |
| REPORT DOC003 p18 eTable4 calcium/albumin | Calcium contrast SE0.0 is one-decimal rounding, not established zero variance; albumin point/SE rounded inputs permit P=.72. These apparent point/SE/test mismatches vanish under complete display intervals. | ROUNDING_OR_DISPLAY_PRECISION |

## statistical_pass_1.md — original exclusion table

| Location | Observation | Reason code |
|---|---|---|
| DOC-003 REPORT p17 eTable3 hypoalbuminemia SG; p19 eTable5 diabetes-related foot ulcers, colon polyps, pneumonia and cellulitis; S147, S152, S165, S180, S181 | Consolidated apparent last-digit count-to-test diagnostic discrepancy: S147 Hypoalbuminemia SG: printed 0.60, Pearson diagnostic 0.594845193, half-unit-band gap 0.000154807, relative 0.000258011; S152 Diabetes related foot ulcers: printed 0.65, Fisher diagnostic 0.655177098, half-unit-band gap 0.000177098, relative 0.000272459; S165 Colon polyps: printed 0.46, Pearson diagnostic 0.465275185, half-unit-band gap 0.000275185, relative 0.000598229; S180 Pneumonia: printed 0.23, Pearson diagnostic 0.224655379, half-unit-band gap 0.000344621, relative 0.001498352; S181 Cellulitis: printed 0.53, Pearson diagnostic 0.535380032, half-unit-band gap 0.000380032, relative 0.000717041. All gaps are far below 0.05 after the printed P half-unit interval, and none involves a confidence interval or a contradictory stated test conclusion. | ROUNDING_OR_DISPLAY_PRECISION |

