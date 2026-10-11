# Stable Candidate Ledger

Pending Human Adjudication. Candidate discovery used supplied sources and eligible reusable evidence, with complete current mapping. Five initial findings were independently screened: four INCLUDE finding rows represent two distinct issues, and one finding was screened out. IDs are assigned in source order by the first relevant REPORT location: main p.4 for C001, then main p.6 for C002. All assigned IDs remain stable.

## Classification table

Evidence states reflect completed direct-source recheck, and inclusion-audit fields reflect the completed independent audit. No AI adjudication is assigned.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | statistical_results | S_W | S_W | REPORT main p.4 statistical methods vs REPORT main p.6 adherence table and prose | reproduced | CONFIRMED | F-ST1-001 |
| C002 | protocol_report | P_R | P_R | PLAN SAP pp.31,71 population definitions vs REPORT main pp.6,7 per-protocol sensitivity | reproduced | CONFIRMED | F-NUM-001, F-XS-001, F-ST1-002 |

## C001 — Missed-dose summaries and stated Welch comparison do not reconcile

**Candidate statement:** The main article describes a two-sided Welch t test for missed-dose percentages, but reports mean (SD) 4.6 (1.0)% versus 4.3 (0.5)% with P=.87 in both table and prose. These summaries and P value do not reconcile for any valid Welch sample sizes, including all allowed display intervals.

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main p.4 statistical methods vs REPORT main p.6 adherence table and prose
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-ST1-001
**Classification rationale:** Both the stated comparison method and its numerical summaries are printed within the main REPORT. No PLAN or second REPORT is a conflicting comparator. The issue concerns estimate/test and method logic.
**Classification ambiguity:** None
**Status:** Pending Human Adjudication
**Relationship inventory references:** S017.

**Exact source locations:** [Main PDF p.4 — Statistical Analyses](../../jama_rathinam_2019_oi_190092.pdf#page=4); [main PDF p.6 — Table 2 missed-dose row and matching paragraph](../../jama_rathinam_2019_oi_190092.pdf#page=6). All table and prose occurrences of the pattern are consolidated.

**Source evidence:** Methods identify a Welch t test for missed-dose comparison and two-sided testing. Table 2 labels the summaries “Missed doses, mean (SD), %” and gives 4.6 (1.0), 4.3 (0.5), P=.87; prose repeats mean (SD) and the same values. The footnote defines each patient's missed doses relative to expected doses throughout enrollment. The current checker and independent screener directly read and visually inspected p.6.

**Reported-versus-comparator:** Reported P=.87, whose two-decimal rounding interval is [.865,.875], versus an upper bound .8508783587 on P under the explicitly stated Welch comparison using all permissible rounded mean/SD inputs and any valid group sizes.

**Reasoning procedure:** Permit the full half-unit interval around each one-decimal mean and SD. A valid sample SD/Welch test requires each group to have at least two observations. Bound the smallest mean difference and largest possible standard error without assuming actual adherence sample sizes. Welch degrees of freedom are at least one. The df=1 Student t tail is a conservative upper bound on the two-sided P for the resulting positive statistic.

**Calculation:** Means are within [4.55,4.65] and [4.25,4.35]; SDs within [.95,1.05] and [.45,.55] percentage points. Absolute difference >=.20; SE <=sqrt((1.05^2+.55^2)/2)=.8381527307; |t| >=.2386199945; df>=1. Therefore P<=1−(2/pi)atan(.2386199945)=.8508783587, below the printed P interval. Endpoint inclusion makes the bound conservative. Percent-to-proportion conversion cancels in the test statistic. This is an analytic compatibility bound under the source-stated method, not an assumed-denominator reconstruction.

**Affected result or extracted value:** The adherence comparison P=.87 and the mean/SD summaries 4.6 (1.0)% versus 4.3 (0.5)%.
**Why context does not resolve it:** Table and prose repeat the values and SD label, and the methods expressly identify Welch. Neither rounding, missing sample sizes nor units resolves the discrepancy, and the package does not identify which reported summary or test value should be interpreted differently.
**Alternative source-grounded interpretations:** A different dispersion quantity, adherence variable or comparison method may underlie the printed P. None is established by the supplied materials. No replacement result is inferred.
**Mechanical evidence recheck:** Fresh direct-source recheck found all cited locations and reproduced the stated comparison; no transcription or classification correction. Complete separate facts are recorded in verification/evidence_recheck.md.
**Potential downstream evidence impact:** If confirmed, an extractor could copy an adherence P value or dispersion statistic that does not match the stated comparison. No primary-outcome conclusion change is asserted.
**Human verification steps:** Check the printed method and both p.6 occurrences; establish the actual adherence summaries, dispersion definition and comparison result from the corresponding analysis output.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Reported per-protocol adherence criterion differs from the supplied SAP

**Candidate statement:** The supplied original and final SAP define noncompliance for the per-protocol efficacy population as receipt below 50% of study drug, while the article labels a primary-outcome sensitivity per protocol and includes only patients missing less than 20% of doses.

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN SAP pp.31,71 population definitions vs REPORT main pp.6,7 per-protocol sensitivity
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-NUM-001, F-XS-001, F-ST1-002
**Classification rationale:** The conflict compares the REPORT's named analysis population with its definition in prospective PLAN material. Original and final SAP versions agree on the disputed threshold and do not create a plan-internal conflict; table/prose/figure corroboration within the article does not create a separate report-internal relationship.
**Classification ambiguity:** None
**Status:** Pending Human Adjudication
**Relationship inventory references:** N040, N078; S022, S065.

**Exact source locations:** [Main PDF p.6 — sensitivity narrative](../../jama_rathinam_2019_oi_190092.pdf#page=6); [main PDF p.7 — Figure 2 model 4 and footnote e](../../jama_rathinam_2019_oi_190092.pdf#page=7); [SAP PDF p.31 — original §4.1](../../joi190092supp3_prod.pdf#page=31); [SAP PDF p.71 — final §4.1](../../joi190092supp3_prod.pdf#page=71). Related definition and amendment context: [SAP PDF p.72 — major deviations](../../joi190092supp3_prod.pdf#page=72), [SAP PDF p.80 — changes](../../joi190092supp3_prod.pdf#page=80), [SAP PDF p.81 — changes continuation](../../joi190092supp3_prod.pdf#page=81). All cited occurrences from the three included findings are retained.

**Source evidence:** The SAP per-protocol efficacy population excludes major deviations or noncompliance, explicitly receipt below 50% by self-report or pill counts. The main narrative includes only participants missing less than 20%; Figure 2 calls model 4 “Per protocol,” repeats that cutoff and gives n=184, 61/90 versus 54/94, OR 1.56 (95% CI .84–2.96), P=.17. The supplied change summary does not reconcile the adherence definition.

**Reported-versus-comparator:** Report eligibility is missed doses <20%, equivalent to receipt >80% on the matching expected-dose fraction; SAP adherence eligibility is receipt >=50%, before its additional exclusions. The criteria differ by 30 percentage points.
**Reasoning procedure:** Compare the explicit selection rules for the same named primary-outcome sensitivity population. Distinguish original/final plan versions, disclosed changes and additional major-deviation conditions. Do not infer a participant-level membership difference or an unreported alternative estimate.
**Calculation:** If a is fraction received and m=1−a is fraction missed, the report requires m<.20, hence a>.80; the SAP excludes a<.50. Explicit cutoffs are selection rules rather than rounded outcome estimates. The printed n=90+94=184 itself reconciles.
**Affected result or extracted value:** Interpretation of the n=184 per-protocol primary-outcome sensitivity and OR 1.56 (.84–2.96), P=.17 as the prospectively defined analysis population.
**Why context does not resolve it:** The article clearly identifies its actual cutoff but does not explain the different definition of its named per-protocol population relative to either supplied SAP version. The immediate source context supplies no corresponding amendment or separately reported estimate under the SAP definition.
**Alternative source-grounded interpretations:** This may be an additional stricter-adherence sensitivity labeled per protocol, or an amendment absent from the supplied package may have changed the threshold. Application of other major-deviation exclusions is unreported. These possibilities do not establish an alternative count or effect.
**Mechanical evidence recheck:** Fresh direct-source recheck found all cited locations and reproduced the stated comparison; no transcription or classification correction. Complete separate facts are recorded in verification/evidence_recheck.md.
**Potential downstream evidence impact:** If confirmed, an extractor could attribute this estimate to the SAP-defined per-protocol population or classify it as prespecified under a population definition that differs from the supplied plan. No direction or magnitude of an alternative result is asserted.
**Human verification steps:** Match the model 4 inclusion rule and deviation exclusions to the operative SAP definition; establish whether the displayed result is the prespecified per-protocol estimate or an additional sensitivity, and document any operative amendment.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __
