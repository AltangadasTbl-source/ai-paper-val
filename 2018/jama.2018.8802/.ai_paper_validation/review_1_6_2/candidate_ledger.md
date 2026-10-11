# Workflow 1.6.2 Candidate Ledger

Pending Human Adjudication. Four stable candidates were initially registered after the independent screen of ten checker findings; C005 was appended after a distinct fresh pass-2 screen of F-ST2-001. The stable set now contains five candidates. Discovery used only supplied sources and usable source-linked derivatives. IDs follow main-report issue anchors in source order: composite definition p.3, primary-analysis statement pp.4–5, clinical-results origin p.5, mortality result p.8. Repeated checker observations share one candidate. No assigned ID may be deleted.

The two fresh mechanical recheckers confirmed all five classifications and assigned reproduced evidence states. The fresh quality auditor independently CONFIRMED inclusion of C001–C005 and retained every classification; all five remain Pending Human Adjudication.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R, S_C | PLAN protocol composite definition vs REPORT main composite definition; REPORT results supplement composite definition vs REPORT main composite definition | reproduced | CONFIRMED | F-XS-003, F-ST1-002 |
| C002 | statistical_results | S_W | S_W | REPORT main primary-analysis statement vs REPORT main Figure 1 primary-analysis counts and Table 2 denominators | reproduced | CONFIRMED | F-NUM-001, F-XS-001, F-ST1-004 |
| C003 | report_internal_inconsistency | S_W | S_W | REPORT main Clinical Events follow-up origin vs REPORT main outcome/method definitions and Table 3/Figure 2 time origins | reproduced | CONFIRMED | F-XS-002, F-ST1-003 |
| C004 | statistical_results | S_W | S_W | REPORT main Table 3 in-hospital death absolute-difference interval vs REPORT main paired P value and significance rule | reproduced | CONFIRMED | F-NUM-002, F-XS-004, F-ST1-001 |
| C005 | statistical_results | S_W | S_W | REPORT results supplement eTable 3 vascular-death difference/interval/P vs REPORT results supplement eTable 3 other absolute-difference rows | reproduced | CONFIRMED | F-ST2-001 |

## C001 — Primary composite definition and weighting

**Candidate statement:** The plan and results supplement define a ratio of total fulfilled to total eligible opportunities, while the main report explicitly averages patient-specific proportions for the primary composite.

**Exact source locations:** PLAN [protocol p.16, lines216–220](../../joi180070supp1_prod.pdf#page=16); REPORT [results supplement p.2, eAppendix](../../joi180070supp2_prod.pdf#page=2); REPORT [main p.3, composite-definition paragraph](../../jama_wang_2018_oi_180070.pdf#page=3); REPORT [main p.7, Table 2 composite row](../../jama_wang_2018_oi_180070.pdf#page=7). Corroborating opportunity-level analysis: PLAN [p.18](../../joi180070supp1_prod.pdf#page=18) and [p.19](../../joi180070supp1_prod.pdf#page=19); REPORT [main p.4](../../jama_wang_2018_oi_180070.pdf#page=4).

**Source evidence and calculation:** Plan/supplement Σr_i/Σk_i weights patient proportions by their eligible-opportunity counts; main Σ(r_i/k_i)/n weights patients equally. Patient-dependent eligibility is described. The formulas are distinct, though particular data can yield the same result. No trial-level numeric difference is inferred. Table 2 reports 88.2 (15.1)% vs84.8 (18.2)%, adjusted difference3.5 (0.7–6.4) percentage points, P=.02; abstract contrast3.54 (0.68–6.40).

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Primary composite outcome definition, weighting, descriptive means and adjusted difference.

**Why context does not resolve it:** Category5 covers the changed composite definition. The opportunity-level OR analysis does not identify the weighting of the descriptive composite or adjusted difference.

**Classification rationale:** The prospective protocol is PLAN; the main and results supplement are distinct REPORT documents. Actual differing definitions create P_R and S_C; P_R has precedence, with protocol_report domain. Opportunity-model passages only distinguish estimands.

**Classification ambiguity:** Aggregate wording may have intended patient averaging, or descriptive and inferential estimands may intentionally differ; no connecting definition or amendment is supplied.

**Alternative source-grounded interpretations and human question:** Which weighting generated each planned/reported composite, and how does the supplement's same-endpoint statement reconcile them? Patient-level eligibility and adjusted-difference construction are absent. No preferred analysis or correction is proposed.

**Checker provenance:** cross_source_consistency_reviewer /root/cross F-XS-003; statistics_pass_1 /root/stat1 F-ST1-002; numeric-tail N140 corroboration without a separate finding. Independent screen includes both findings in one issue.

## C002 — Primary-analysis population counts

**Candidate statement:** The main Results assigns4800 patients to the primary analysis, while Figure1 labels2003 intervention and1977 control patients as included in the primary analysis and Table2 uses2400 per arm.

**Exact source locations:** REPORT [main p.4, Results opening and follow-up paragraph](../../jama_wang_2018_oi_180070.pdf#page=4); REPORT [main p.5, Figure1 lower analysis and follow-up boxes](../../jama_wang_2018_oi_180070.pdf#page=5); REPORT [main p.7, Table2 all-or-none row](../../jama_wang_2018_oi_180070.pdf#page=7); corroborating REPORT [abstract p.1](../../jama_wang_2018_oi_180070.pdf#page=1).

**Source evidence and calculation:** 2003+1977=3980; 2400−397=2003 and2400−423=1977, also the twelve-month completers. Figure sum rounding interval[3979,3981] versus4800 interval[4799.5,4800.5] gives gap818.5/4800=.1705208>.05. Arm gaps396/2400=.165 and422/2400=.1758333 exceed.05. Co-primary all-or-none fractions1290/2400 and1147/2400 use the full randomized population.

**Qualifying route:** Route B.

**Affected result or extracted value:** Participant count and analysis population attached to the co-primary adherence results.

**Why context does not resolve it:** Both sources explicitly label primary analysis. Identifying3980 as follow-up completers explains its origin but does not reconcile the named primary-analysis populations; an extractor can select3980 or4800.

**Classification rationale:** All conflicting locations are within one REPORT, so S_W. Counts and denominators direct this candidate to statistical_results, despite earlier checker proposals emphasizing population attribution.

**Classification ambiguity:** Figure boxes may intend the twelve-month clinical follow-up analysis rather than inpatient adherence. Actual computational exclusions are not inferred.

**Alternative source-grounded interpretations and human question:** Which population do Figure1's analysis boxes denote, and how does it reconcile with4800 primary-analysis patients and2400-per-arm denominators?

**Checker provenance:** numeric_consistency_reviewer /root/numeric F-NUM-001; cross_source_consistency_reviewer /root/cross F-XS-001; statistics_pass_1 /root/stat1 F-ST1-004. Independent screen includes all three in one issue.

## C003 — Clinical follow-up time origin

**Candidate statement:** The Clinical Events paragraph attributes the Table3 clinical results to3,6,12 months after discharge, while the outcome/method definitions, Table3 disability footnote and Figure2 use symptom onset.

**Exact source locations:** REPORT [main p.5, Clinical Events paragraph](../../jama_wang_2018_oi_180070.pdf#page=5); REPORT [main p.3, secondary-outcome definitions](../../jama_wang_2018_oi_180070.pdf#page=3); REPORT [main p.4, time-to-event methods](../../jama_wang_2018_oi_180070.pdf#page=4); REPORT [main p.8, Table3 footnote and Figure2 axes/caption](../../jama_wang_2018_oi_180070.pdf#page=8); supporting REPORT [main p.6, length of stay](../../jama_wang_2018_oi_180070.pdf#page=6). Corroborating PLAN [protocol p.16](../../joi180070supp1_prod.pdf#page=16) and [p.19](../../joi180070supp1_prod.pdf#page=19).

**Source evidence and calculation:** Discharge and symptom onset are different time origins. Median hospital stays13 and12 days are supporting context, not patient-specific conversions. No event-rate recalculation or numerical relative discrepancy is applicable.

**Qualifying route:** Route B.

**Affected result or extracted value:** Time horizon for key secondary vascular results (differences−2.03,−2.18,−3.13 percentage points) and disability/mortality results at3,6,12 months.

**Why context does not resolve it:** The same Table3 results are explicitly assigned to different origins, without stated separate windows. This concerns result attribution and the extracted time horizon.

**Classification rationale:** Differing result-attribution statements are in one REPORT, so S_W/report_internal_inconsistency. The plan only corroborates onset, adding no P_R relationship.

**Classification ambiguity:** Discharge wording may be informal posthospital contact language or may indicate a distinct window.

**Alternative source-grounded interpretations and human question:** Which origin governs Table3 clinical results and the corresponding disability/survival analyses, and does discharge wording denote a distinct window? Individual outcome/contact dates are absent.

**Checker provenance:** cross_source_consistency_reviewer /root/cross F-XS-002; statistics_pass_1 /root/stat1 F-ST1-003; numeric-tail N141 corroboration without new finding. Independent screen includes both findings in one issue.

## C004 — In-hospital mortality interval and P value

**Candidate statement:** Table3 pairs an adjusted in-hospital mortality absolute-difference95%CI crossing zero with P=.009 under the stated two-sided P<.05 rule.

**Exact source locations:** REPORT [main p.8, Table3 Death/In hospital row and separate P columns](../../jama_wang_2018_oi_180070.pdf#page=8); REPORT [main p.4, Data Analysis significance/CI rules](../../jama_wang_2018_oi_180070.pdf#page=4); contextual REPORT [main p.5, mortality narrative](../../jama_wang_2018_oi_180070.pdf#page=5).

**Source evidence and calculation:** 11/2400(0.5%) versus23/2400(1.0%); adjusted difference−0.7 percentage points,95%CI[−1.1,+0.2], P=.009. Zero is included while.009<.05. Endpoint half-unit ranges[−1.15,−1.05] and[.15,.25] remain opposite in sign; P range[.0085,.0095] remains below.05. RouteA1 is never excluded by relative display precision. Separate HR0.96(0.90–1.02), P=.14 must not be substituted for the difference's test.

**Qualifying route:** Route A, category 1.

**Affected result or extracted value:** In-hospital mortality adjusted absolute-difference interval/P and its null-exclusion reading.

**Why context does not resolve it:** Category1 requires inclusion of reproduced interval/test conflicts; the separate HR and nonsignificant mortality narrative do not reconcile the printed difference pair.

**Classification rationale:** One REPORT's interval/P pairing under its significance rule is S_W/statistical_results.

**Classification ambiguity:** None concerning document role or relationship; inferential construction is unspecified.

**Alternative source-grounded interpretations and human question:** Which analyses produced this interval and P, and how should the readings reconcile? Distinct CI/test constructions may be intended; the HR may underpin the mortality narrative. Neither alternative removes the routeA1 candidate. No correction is proposed.

**Checker provenance:** numeric_consistency_reviewer /root/numeric F-NUM-002; cross_source_consistency_reviewer /root/cross F-XS-004; statistics_pass_1 /root/stat1 F-ST1-001. Independent screen includes all three in one issue.

## C005 — Three-month vascular-death interval and P relationship

**Candidate statement:** The eTable3 three-month vascular-death adjusted difference, interval and paired P value do not reconcile under the two-sided normal-Wald relationship supported by every other absolute-difference row of the display, including full printed-input rounding allowances.

**Exact source locations:** REPORT [results supplement p.6, eTable3 three-month vascular-death absolute-difference/CI/P columns and all eleven other difference rows](../../joi180070supp2_prod.pdf#page=6); REPORT [results supplement p.7, adjustment footnote](../../joi180070supp2_prod.pdf#page=7). Corroborating REPORT [main p.4, 95% confidence and two-sided test rules](../../jama_wang_2018_oi_180070.pdf#page=4). Comparison rows are ischemic stroke, hemorrhagic stroke and myocardial infarction at3,6,12 months, plus vascular death at6 and12 months. Statistical relationships S059/S117 track the observation and shared inference rule.

**Source evidence and calculation:** Intervention46/2400(1.9%) versuscontrol67/2400(2.8%); adjusted difference−1.43 percentage points,95%CI[−2.33,−0.54], paired P=.001. Separate HR0.62(0.42–0.92), P=.02 is a different test. Diagnostic q=1.959963984540054, SE=(U−L)/(2q), z=|b|/SE andP=2Φ(−|z|) gives centralP=.001738787. Inputs b∈[−1.435,−1.425], L∈[−2.335,−2.325], U∈[−.545,−.535] give conservativeP∈[.001576789,.001913909]. PrintedP∈[.0005,.0015], so gap.000076789/.001=.076789>.05. Enforcing exact symmetric-Wald centering givesP∈[.001576789,.001777726], still disjoint. All eleven other difference rows overlap their printed P intervals under both the independent-input and centered calculations. Independent accurate normal integration refines pass2's approximations without changing the conclusion.

**Qualifying route:** Route A, category 1.

**Affected result or extracted value:** Numerical P value and inferential precision paired with the three-month vascular-death adjusted absolute difference; the printed significance conclusion is unchanged.

**Why context does not resolve it:** RouteA1 covers estimate/interval/P conflicts; the same display supports the diagnostic relationship in every comparison row. The actual difference-specific confidence/test construction is not stated, and the separate HR/P does not identify it. The method is empirically supported and explicitly diagnostic, rather than asserted as the authors' actual undisclosed procedure.

**Classification rationale:** The differing tuple and supporting comparison rows are within one REPORT results supplement, so S_W/statistical_results. Main inferential conventions and the adjustment footnote corroborate the applicable comparison and do not add a conflicting S_C relationship.

**Classification ambiguity:** None for roles/domain/relationship. A separate confidence or test construction may explain the tuple, and remains a human question rather than an asserted implementation fact.

**Alternative source-grounded interpretations and human question:** Which difference-specific confidence-interval and testing procedures produced−1.43(−2.33 to−0.54) withP=.001, and how does the pairing reconcile with the normal-Wald relationship supported by all eleven other rows? A different test, variance estimator, confidence construction, dataset or estimand may be intended; raw model output and patient-level event data are absent. No intended numeric replacement or preferred analysis is proposed.

**Checker provenance:** statistics_pass_2 /root/stat2 F-ST2-001; distinct independent inclusion_screener_pass_2 /root/screen2, INCLUDE. This is distinct from C004's in-hospital mortality null-crossing conflict; no repeated cause is demonstrated. C005 was appended without changing any existing stable ID and remains Pending Human Adjudication.
