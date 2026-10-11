# Stable candidate ledger

Pending Human Adjudication. Four independently included issues are registered. Stable IDs follow the first result-bearing REPORT source location: main p1 intervention description, main p5 Table1 distribution, main p5 Additional Outcomes timing result, main p7 Table2 inferential bleeding blocks. Methods and corroborating locations are retained without changing this ordering. No candidate count target is used. Exact-source recheck assigned reproduced to all four candidates; the independent audit assigned CONFIRMED to each candidate.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R | REPORT main article pp.1,3 vs PLAN final protocol pp.77,101 | reproduced | CONFIRMED | F-XS-002 |
| C002 | statistical_results | S_W | S_W | REPORT main article Table1 p.5 median vs lower quartile | reproduced | CONFIRMED | F-NUM-002 |
| C003 | statistical_results | S_C | S_C, S_W | REPORT main article pp.4,5 vs REPORT results supplement eTable7 p.11 | reproduced | CONFIRMED | F-ST1-002 |
| C004 | statistical_results | S_C | S_C, S_W | REPORT main article Table2 p.7 vs REPORT results supplement eTable6 p.10 | reproduced | CONFIRMED | F-NUM-001, F-XS-001, F-ST1-001 |

## C001 — Duration attributed to assigned normothermic management

**Candidate statement:** The report describes temperature management in both groups for7days, while the final plan specifies96hours for control/all-patient pyrexia avoidance followed by local unit/ward care; the operative randomized comparator/post-rewarming duration is unclear.
**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** REPORT main article pp.1,3 vs PLAN final protocol pp.77,101
**Finding IDs:** F-XS-002
**Classification rationale:** A reported randomized intervention duration differs from supplied final prospective plan instructions. The plan-only H post-rewarming difference is contextual, rather than an additional statistical-design relationship.
**Classification ambiguity:** Plan p77 gives H post-rewarming normothermia a7-day maximum, while p101 hands post-rewarming/all-patient management to local protocol after96hours. No later extension or actual received-duration distinction is established.
**Exact source locations:** [main p1, abstract interventions](../../jama_cooper_2018_oi_180132.pdf#page=1); [main p3, rewarming/normothermia](../../jama_cooper_2018_oi_180132.pdf#page=3); [plan p77, Version9 §12.11](../../joi180132supp1_prod.pdf#page=77); [plan p101, AppendixF §26.5](../../joi180132supp1_prod.pdf#page=101).
**Source evidence:** Main: both-group management7days; normothermia after rewarming up to7days postrandomization. Plan p77: control pyrexia avoidance up to96hours then unit protocol; p101 post-rewarming pads and pyrexia avoidance96hours then ward/unit protocol.
**Calculation:** 96h=4days;7days=168h; difference72h. The comparison distinguishes assigned temperature management from ordinary care afterward.
**Affected result or extracted value:** Comparator and post-rewarming management duration extracted alongside the primary six-month favorable GOS-E result117/240 versus111/226.
**Why context does not resolve it:** The report does not identify the96-hour handoff or a duration amendment; the supplied text does not establish whether days5–7 were assigned treatment, optional local care or a later extension.
**Alternative source-grounded interpretations:** A later operational extension, optional local normothermia beyond96hours, or an earlier duration retained in AppendixF could explain the descriptions; no explanation is selected as established.
**Human question:** Which duration describes the operative randomized comparator/post-rewarming management, and is there a supplied amendment or analysis specification explaining the report wording?

## C002 — Normothermia Injury Severity Score median and lower quartile

**Candidate statement:** The normothermia Injury Severity Score summary20.0(20.5–35.0), labeled median(IQR), does not satisfy quartile ordering, even within printed precision.
**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table1 p.5 median vs lower quartile
**Finding IDs:** F-NUM-002
**Classification rationale:** The incompatible quantities occur within one REPORT distribution row. This is an internal statistical ordering relationship, rather than a cross-location baseline comparison.
**Classification ambiguity:** None
**Exact source locations:** [main p5, Table1 Injury Severity Score row and scale footnote](../../jama_cooper_2018_oi_180132.pdf#page=5).
**Source evidence:** Normothermia20.0(20.5–35.0); hypothermia26.0(18.0–34.0). Label median(IQR); scale0–75, higher scores greater severity.
**Calculation:** Q1≤median≤Q3 is required. Median half-unit interval[19.95,20.05) lies below Q1[20.45,20.55), with minimum separation0.40; rounding does not reconcile.
**Affected result or extracted value:** Normothermia baseline Injury Severity Score median and lower quartile describing the analyzed trial population.
**Why context does not resolve it:** Neither neighboring values nor the scale footnote supplies an intended median or Q1; more than one component could require clarification.
**Alternative source-grounded interpretations:** The median or lower quartile may have a different underlying value. No replacement is inferred from another analysis population.
**Human question:** What median and IQR describe the normothermia distribution underlying Table1?

## C003 — Time-to-33°C comparison and printed P value

**Candidate statement:** Pearson diagnostics of the stated unadjusted equal-proportions chi-square method do not match the displayed P=.09 under either source-supported category interpretation; the original tested category set, implementation and result attribution remain unclear.
**Review domain:** statistical_results
**Relationship type:** S_C
**All relationships:** S_C, S_W
**Compared document roles:** REPORT main article pp.4,5 vs REPORT results supplement eTable7 p.11
**Finding IDs:** F-ST1-002
**Classification rationale:** REPORT main method/nonsignificant claim is compared with REPORT supplementary counts/P, alongside an internal supplementary count/test relationship. Precedence S_C over S_W; no conflicting PLAN comparator.
**Classification ambiguity:** Exact tested categories and chi-square implementation are unprinted. Pearson homogeneity calculations are diagnostics of the stated equal-proportions test, not reconstructed raw-data output.
**Exact source locations:** [main p4, time-to-target statistical method](../../jama_cooper_2018_oi_180132.pdf#page=4); [main p5, Additional Outcomes nonsignificant claim](../../jama_cooper_2018_oi_180132.pdf#page=5); [results supplement p11, eTable7 all categories and merged P cell](../../joi180132supp2_prod.pdf#page=11).
**Source evidence:** Counts18/49,28/67,32/59,39/65 for1–7h,8–13h,>13h,never; one P=.09. Main states unadjusted chi-square test for equal proportions and no significant difference.
**Calculation:** Four rows give favorable/unfavorable(18,31),(28,39),(32,27),(39,26),117/240 total. Pearson χ²=8.133762,df3,P=.043327. Three attained-temperature groups instead χ²=3.658952,df2,P=.160498. Neither lies in printed P half-unit interval[.085,.095). Fixed integer counts leave no percentage-rounding adjustment.
**Affected result or extracted value:** The favorable-GOS-E association with timing of reaching33°C, its extracted P value/tested categories and nonsignificant description. Randomized primary treatment comparison remains distinct; no causal timing effect is asserted.
**Why context does not resolve it:** A single merged P cell spans the four categories; neither table nor main method identifies another subset or implementation producing.09.
**Alternative source-grounded interpretations:** An unshown subset, another chi-square computation, or a differently matched analysis could explain the value. No unreported records, stratification or model are assumed.
**Human question:** Which category set and computation producedP=.09, and which displayed timing comparison does it describe?

## C004 — Bleeding RR, confidence interval and P attribution

**Candidate statement:** The two main bleeding rows attach unadjusted RRs incompatible with their event counts and P values that conflict with the matched results supplement. Diagnostic interval calculations support the same exchanged-block pattern; they do not establish the original CI construction.
**Review domain:** statistical_results
**Relationship type:** S_C
**All relationships:** S_C, S_W
**Compared document roles:** REPORT main article Table2 p.7 vs REPORT results supplement eTable6 p.10
**Finding IDs:** F-NUM-001, F-XS-001, F-ST1-001
**Classification rationale:** Both within-main count/inferential blocks and matched main-versus-supplement P assignments conflict. REPORT/REPORT relationship S_C takes precedence over S_W; a plan does not constitute a conflicting comparator.
**Classification ambiguity:** None
**Exact source locations:** [main p1, intracranial bleeding abstract safety rates](../../jama_cooper_2018_oi_180132.pdf#page=1); [main p3, unadjusted adverse-event method](../../jama_cooper_2018_oi_180132.pdf#page=3); [main p4, two-sided test convention](../../jama_cooper_2018_oi_180132.pdf#page=4); [main p5, adverse-event narrative](../../jama_cooper_2018_oi_180132.pdf#page=5); [main p7, Table2 both bleeding rows](../../jama_cooper_2018_oi_180132.pdf#page=7); [results supplement p10, eTable6 both bleeding rows](../../joi180132supp2_prod.pdf#page=10).
**Source evidence:** Intracranial47/260(18.1%) versus37/240(15.4%),RD2.7(−3.9 to9.2),RR1.23(0.43–3.5),P=.70. Extracranial8/260(3.1%) versus6/240(2.5%),RD0.6(−2.3 to3.5),RR1.17(0.79–1.74),P=.43. Supplement repeats counts and gives intracranialP=.43,extracranialP=.70.
**Calculation:** Exact unadjusted RR intracranial=(47/260)/(37/240)=1.172557; extracranial=(8/260)/(6/240)=1.230769. Both exclude their displayed RR half-unit intervals[1.225,1.235)and[1.165,1.175). Pearson χ²/P diagnostics .631872/.426669 and .152625/.696039 agree with supplementary P attachments. Diagnostic log-Wald intervals .791181–1.737769 and .433345–3.495582 resemble the opposite main interval; CI method is not assumed solely from this diagnostic.
**Affected result or extracted value:** Outcome-specific unadjusted RR,95%CI and P for intracranial bleeding (abstract safety endpoint) and the paired extracranial comparison.
**Why context does not resolve it:** Counts/RD and RR/CI/P are assigned to the same named rows under unadjusted methods; detecting a likely exchange does not establish the authoritative complete inferential attribution. Supplement supplies P but no independent RR/CI block.
**Alternative source-grounded interpretations:** An exchanged inferential block or an undisclosed alternative computation could explain the pattern. No final replacement is prescribed.
**Human question:** Which RR/CI/P belongs to each bleeding outcome according to the original adverse-event output?
