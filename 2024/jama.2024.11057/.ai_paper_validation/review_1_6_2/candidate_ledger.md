# Workflow 1.6.2 Candidate Ledger

Pending Human Adjudication. Five distinct issues were included by the fresh independent initial screener. IDs are assigned in source order by the first affected REPORT location retained in the screening groups: article p. 1, p. 2, p. 3, p. 4, then results-supplement p. 14. Duplicate findings retain provenance and all affected locations; they do not create additional IDs. No old candidate selection or count target was used. The fresh evidence rechecker reproduced all five registered observations and confirmed their classifications. The fresh quality-control auditor confirmed inclusion for all five IDs, retained their classifications and evidence states, and found no additional qualifying issue.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R | PLAN protocol p. 5 vs REPORT article pp. 1, 4-6 and results supplement p. 14 | reproduced | CONFIRMED | F-XS-002 |
| C002 | statistical_results | S_W | S_W | REPORT article p. 2 vs REPORT article p. 4; p. 6 corroborates counts | reproduced | CONFIRMED | F-ST1-004 |
| C003 | protocol_report | P_R | P_R, S_C | REPORT article p. 3 vs PLAN protocol pp. 2, 4 and REPORT results supplement p. 2 | reproduced | CONFIRMED | F-XS-001 |
| C004 | protocol_report | P_R | P_R | PLAN protocol pp. 5-6 vs REPORT article pp. 4-5 and results supplement pp. 6, 15 | reproduced | CONFIRMED | F-XS-003 |
| C005 | statistical_results | S_W | S_W | REPORT results supplement p. 14 IPRW OR cell vs REPORT same-display five other OR cells; p. 5 supplies method context | reproduced | CONFIRMED | F-ST1-001 |

## C001 — Primary estimate attribution to planned baseline adjustment

**Candidate statement:** The protocol specifies baseline-confounder adjustment for primary estimates, while the supplied report does not identify how that planned adjustment relates to its printed primary effects.

**Review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R. **Qualifying route:** Route B. Focus areas C/D.

**Finding provenance:** Included F-XS-002 from cross_source_consistency_reviewer; duplicate F-ST1-002 from statistics_pass_1 is retained as corroborating checker provenance. Both findings' location lists are merged here.

**Exact source locations:** PLAN [protocol p. 5, Primary Analysis](../../joi240078supp1_prod_1739900423.22574.pdf#page=5); REPORT [article p. 1, abstract](../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=1), [p. 4, Statistical Methods](../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=4), [p. 5, Vaping Cessation](../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=5), [p. 6, Table 2](../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=6); REPORT [results supplement p. 14, eTable 5 Missing=Vaping](../../joi240078supp2_prod_1739900423.24574.pdf#page=14). PLAN [protocol p. 15, disclosed amendments](../../joi240078supp1_prod_1739900423.22574.pdf#page=15) is amendment context.

**Reported-versus-comparator:** Plan says all estimates will be adjusted for baseline confounders of the intervention-outcome relationship. Report describes ordinary logistic regression and ITT missing=vaping, with primary RR 1.35 (1.17-1.57) and OR 1.57 (1.26-1.95), without an identifiable primary baseline-covariate formula, selection rule, or adjusted estimate attribution.

**Reasoning procedure and calculation:** Compare the affirmative primary-model specification with the model/result labels across the complete report. Numerical precision does not decide a categorical model-attribution comparison. Counts 287/759 and 208/744 reproduce marginal RR 1.35254 and OR 1.56690; that arithmetic is supporting context only and does not prove the actual model omitted covariates. The independent screen uses Route B rather than asserting that the planned analysis was never performed.

**Affected result or extracted value:** Adjustment identity of the primary seven-month RR 1.35 and OR 1.57.

**Why context does not resolve it:** The report does not connect an identifiable baseline adjustment to these estimates; CCA/IPRW are separately labeled sensitivities. The affirmative prospective specification leaves a focused primary-result extraction question.

**Alternative source-grounded interpretations:** Undisclosed covariates may have been used; no factors may have met an undisclosed confounder-selection rule; or the analysis specification may have changed. No primary-model amendment is identified in the supplied amendment page.

**Classification rationale:** The substantive comparison is PLAN versus REPORT. Report sources agree with each other, so no S_C relationship is added merely for corroboration. **Classification ambiguity:** Actual primary model formula and covariate selection are unavailable.

**Exact remaining human question:** Which model and baseline covariates generated the printed primary estimates, and how does that model correspond to the protocol's adjustment commitment?

**Potential downstream evidence impact:** An extractor could label the primary estimate's adjustment status differently. No effect-size change or conclusion change is established.

## C002 — Retention test population and waitlist exclusion

**Candidate statement:** The report says waitlist participants were excluded from significance tests, but presents retention P values alongside comparisons of all three groups without specifying the tested contrast.

**Review domain:** statistical_results. **Relationship type:** S_W. **All relationships:** S_W. **Qualifying route:** Route B. Focus area C.

**Finding provenance:** Included F-ST1-004 from statistics_pass_1. The cross-source checker considered the same observation in its exclusions; the independent screener reread the complete paragraph and included this named test-population attribution issue.

**Exact source locations:** REPORT [article p. 2, waitlist discussion](../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=2), [p. 4, Results retention paragraph](../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=4); [p. 6, flow figure](../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=6) corroborates counts.

**Reported-versus-comparator:** One-month I 609/759, C 636/744, W 152/178 with P=.02; seven-month I 521/759, C 543/744, W 132/178 with P=.11 and no difference between groups. The earlier statement excludes waitlist from significance tests.

**Reasoning procedure and calculation:** Compare test-population statements, not per-time-point count copies. Three-group Pearson diagnostics give chi-square 8.108584, P=.0173478 and chi-square 4.327096, P=.1149167, compatible with the printed P values. The actual method/contrast is not identified, so these diagnostics do not establish the authors' test. Rounding cannot resolve test group membership.

**Affected result or extracted value:** Which comparison generated retention P=.02 and P=.11.

**Why context does not resolve it:** The retention paragraph describes all three groups without a narrower contrast or a retention-only exemption from the exclusion statement.

**Alternative source-grounded interpretations:** Waitlist exclusion may apply only to cessation tests, or the P values may belong to a separate two-arm comparison. The exact test and contrast are unavailable.

**Classification rationale:** Both substantive statements are in the same REPORT; the issue concerns statistical-test specification. **Classification ambiguity:** The tested contrast and intended scope of waitlist exclusion are unreported.

**Exact remaining human question:** Which groups and tests generated each retention P value, and what scope was intended for the waitlist exclusion?

**Potential downstream evidence impact:** A reader could assign the retention tests to different populations. No abstinence-effect or significance change is asserted.

## C003 — Prequit intervention duration across supplied documents

**Candidate statement:** For participants who set a quit date, the main article prints six prequit weeks while the protocol and results supplement print one.

**Review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R, S_C. **Qualifying route:** Route B. Focus area D.

**Finding provenance:** Included F-XS-001 from cross_source_consistency_reviewer; duplicate F-ST1-005 from statistics_pass_1 retains all locations and statistical provenance.

**Exact source locations:** REPORT [article p. 3, intervention description](../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=3); PLAN [protocol p. 2, program description](../../joi240078supp1_prod_1739900423.22574.pdf#page=2) and [p. 4, intervention assignment](../../joi240078supp1_prod_1739900423.22574.pdf#page=4); REPORT [results supplement p. 2, eAppendix A](../../joi240078supp2_prod_1739900423.24574.pdf#page=2). PLAN [protocol p. 15](../../joi240078supp1_prod_1739900423.22574.pdf#page=15) supplies disclosed-amendment context.

**Reported-versus-comparator:** Main six weeks before/eight after; plan one week before/eight after; supplement one week preceding/eight afterward. All concern the same quit-date branch, distinct from the four-week no-date branch.

**Reasoning procedure and calculation:** Main half-unit interval [5.5,6.5] versus [0.5,1.5] weeks gives minimum gap 4 weeks; relative discrepancy 4/1=4.00, above .05. Nominal total windows are 14 versus 9 weeks. Current-source visual inspection confirms six is a printed duration, not a reference marker.

**Affected result or extracted value:** Intervention duration/exposure associated with the primary seven-month abstinence result.

**Why context does not resolve it:** Neither the common eight-week postquit component nor the four-week no-date branch identifies which prequit schedule was delivered.

**Alternative source-grounded interpretations:** A later program version may have expanded the schedule, or an operational window may differ from the stated treatment period; no such duration amendment or distinction is supplied.

**Classification rationale:** Main versus PLAN and main versus another REPORT are substantive duration comparisons; P_R precedes S_C. **Classification ambiguity:** Operative delivered schedule and any duration amendment are unavailable.

**Exact remaining human question:** Which prequit schedule was delivered to participants setting a quit date, and how does it correspond to the prospective and retrospective descriptions?

**Potential downstream evidence impact:** An intervention extractor could record one or six prequit weeks; the candidate does not establish a different trial effect.

## C004 — Planned moderator selection and reported testing family

**Candidate statement:** The supplied plan's outcome-association condition is not connected to the report's all-characteristic moderator testing family.

**Review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R. **Qualifying route:** Route B. Focus areas C/D.

**Finding provenance:** Included F-XS-003 from cross_source_consistency_reviewer; duplicate F-ST1-003 from statistics_pass_1 preserves its evidence and provenance.

**Exact source locations:** PLAN [protocol p. 5, Primary Analysis](../../joi240078supp1_prod_1739900423.22574.pdf#page=5), [p. 6, continuation](../../joi240078supp1_prod_1739900423.22574.pdf#page=6); REPORT [article p. 4, Statistical Methods](../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=4), [p. 5, Moderator Results](../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=5), [results supplement p. 6, eAppendix D](../../joi240078supp2_prod_1739900423.24574.pdf#page=6), and [p. 15, eTable 6](../../joi240078supp2_prod_1739900423.24574.pdf#page=15). PLAN [protocol p. 15](../../joi240078supp1_prod_1739900423.22574.pdf#page=15) provides amendment context.

**Reported-versus-comparator:** Plan says interactions are examined for moderators found associated with the primary outcome after entering main effects. Report examines all Table 1 characteristics one at a time, with treatment/moderator main effects and interaction, using a 25-variable Holm family.

**Reasoning procedure and calculation:** Compare the selection condition and reported family specification. Holm arithmetic reproduces: the lowest nominal .010 becomes adjusted .250. The candidate concerns the connection to the planned gate, not the correction arithmetic or a preferred variable-selection strategy. Display precision does not determine an analysis selection rule.

**Affected result or extracted value:** Interpretation of the no-adjusted-significant-moderator conclusion and its multiplicity family.

**Why context does not resolve it:** The report does not state whether the association condition selected all variables, was bypassed, or was replaced.

**Alternative source-grounded interpretations:** All variables may have met the planned condition; the plan's broad language may authorize exploratory expansion; or a fuller analysis specification may have superseded the supplied plan.

**Classification rationale:** The substantive specification differs between PLAN and REPORT; report sources agree, so P_R only. **Classification ambiguity:** Association-gate definition/results and any updated family specification are unavailable.

**Exact remaining human question:** Was the association condition used, and which specification determined the reported 25-variable testing family?

**Potential downstream evidence impact:** A reader could interpret the moderator family differently when assessing the reported primary-outcome moderation analysis. No alternative preferred analysis is proposed.

## C005 — Weighted odds-ratio upper confidence limit in eTable 5

**Candidate statement:** The weighted 30-day abstinence OR upper limit does not reproduce the log-symmetric construction that reproduces the other five odds-ratio rows of the same display.

**Review domain:** statistical_results. **Relationship type:** S_W. **All relationships:** S_W. **Qualifying route:** Route A, category 4. Focus areas B/C.

**Finding provenance:** Included F-ST1-001 from statistics_pass_1.

**Exact source locations:** REPORT [results supplement p. 14, eTable 5, 30-day IPRW OR and all five comparator OR cells](../../joi240078supp2_prod_1739900423.24574.pdf#page=14); REPORT [p. 5, eAppendix C](../../joi240078supp2_prod_1739900423.24574.pdf#page=5) supplies survey-weighted logistic method context.

**Reported-versus-comparator:** Printed OR 1.92 (95% CI, 1.50-2.24), P<.001. Comparator triples (OR,lower,upper): (1.98,1.55,2.52), (1.57,1.26,1.95), (2.65,1.90,3.70), (2.61,1.87,3.65), (2.34,1.69,3.22).

**Reasoning procedure and calculation:** A log-symmetric interval satisfies upper=OR squared/lower. This construction reproduces all five comparator cells under half-unit input/output intervals, including the other weighted row. OR [1.915,1.925] and lower [1.495,1.505] yield upper [2.436694352,2.478678930]. Printed upper [2.235,2.245] is disjoint by 0.191694352; residual relative discrepancy is 0.191694352/2.24=0.085577836, above .05. Central diagnostic upper is 2.4576; it is not a proposed final correction.

**Affected result or extracted value:** Upper 95% confidence limit of the weighted 30-day abstinence OR.

**Why context does not resolve it:** Route A category 4 applies to a within-display result not reproduced by a construction that reproduces the other rows. No distinct construction for this row is identified.

**Alternative source-grounded interpretations:** An asymmetric or row-specific confidence-interval procedure could explain the displayed bounds; actual weighted covariance, degrees of freedom, and interval engine are unavailable.

**Classification rationale:** All conflicting construction comparators belong to one REPORT display, so S_W and statistical_results. **Classification ambiguity:** Row-specific interval construction is unavailable.

**Exact remaining human question:** Which construction produced upper limit 2.24, and how does it relate to the other five odds-ratio intervals?

**Potential downstream evidence impact:** A synthesis could copy 2.24 as the weighted OR upper limit. Both printed interval and P<.001 indicate a positive significant association; no significance reversal or propagation is asserted.
