# Workflow 1.6.1 Candidate Ledger

Pending Human Adjudication. Four stable candidates are registered after the independent initial inclusion screen. Five INCLUDE finding rows map to four issues; one duplicate finding is retained as provenance. IDs are assigned in source order: article p1 primary endpoint, p1 efficacy/airway output populations, p3 safety rule, and p3 post-hoc specification. No count target controlled discovery or registration. Classification below is confirmed by the mechanical rechecker and independently audited; stable IDs are never deleted.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R | PLAN final protocol/amendment vs REPORT main article/results supplement primary endpoint | reproduced | CONFIRMED | F-XS-001 |
| C002 | protocol_report | P_R | P_R | PLAN SAP population-output requirements vs REPORT main article/results supplement identified analyses | reproduced | CONFIRMED | F-XS-002, F-ST1-003 |
| C003 | statistical_results | S_W | S_W | REPORT main article safety definition vs REPORT main article flow/safety tables | reproduced | CONFIRMED | F-NUM-001 |
| C004 | statistical_results | S_C | S_C | REPORT main article ITT/reassignment specification vs REPORT results supplement post-hoc population | reproduced | CONFIRMED | F-ST1-002 |

## C001 — Amended primary success definition and reported CPC threshold

**Status:** Pending Human Adjudication.

**Candidate statement:** The final protocol adds unchanged pre-existing neurological disability as a primary favorable-survival condition, while the report explicitly counts CPC1/2 only.

**Finding IDs:** F-XS-001. Duplicate provenance: F-ST1-001, screened out as DUPLICATE_OF_INCLUDED and mapped to this stable ID. Checker provenance: cross_source_consistency_reviewer and statistics_pass_1; independent inclusion_screener.

**Exact source locations:** PLAN [final protocol p71 §4.1.1](../../joi180004supp1_prod.pdf#page=71) and [primary-endpoint amendment p110](../../joi180004supp1_prod.pdf#page=110), versus REPORT [main p1 abstract endpoint/results](../../jama_jabre_2018_oi_180004.pdf#page=1), [p3 Outcomes](../../jama_jabre_2018_oi_180004.pdf#page=3), [p4 Primary Outcome](../../jama_jabre_2018_oi_180004.pdf#page=4), [p6 Table2 CPC block/footnote b](../../jama_jabre_2018_oi_180004.pdf#page=6), and [results supplement p3 both endpoint labels](../../joi180004supp2_prod.pdf#page=3). Historical corroboration, without a separate conflict relationship: PLAN [original endpoint p15](../../joi180004supp1_prod.pdf#page=15), [SAP endpoint p122](../../joi180004supp1_prod.pdf#page=122), and [scanned counterpart p131](../../joi180004supp1_prod.pdf#page=131).

**Source evidence:** Final protocol first states CPC≤2, then says survival with the same degree of pre-randomization neurological disability is favorable. Amendment p110 expressly adds that provision. The report defines CPC1/2 success. Its ITT numerators are35+9=44 and37+6=43; PP43=35+8 and40=34+6.

**Reasoning procedure and calculation:** Compare sufficient success conditions for the same primary day28 endpoint. The extra PLAN condition is absent from REPORT coding; categorical definitions cannot be reconciled by half-unit display precision. No baseline CPC>2 participant or changed success count is assumed.

**Affected result or extracted value:** The primary endpoint definition attached to ITT44/1018 versus43/1022, PP43/995 versus40/943, their noninferiority results, and the sensitivity endpoint labels.

**Why context does not resolve it:** Immediate context identifies strict CPC1/2 values but does not explain whether the amended rule was applied, withdrawn, or irrelevant to the analyzed survivors.

**Classification rationale:** The conflicting definitions are final PLAN versus REPORT, hence P_R/protocol_report. The REPORT sources agree with each other. Original PLAN/SAP chronology corroborates the older rule without adding P_P or S_C.

**Classification ambiguity:** The historical SAP retains the prior wording; actual implementation or later withdrawal of the disability provision is not supplied.

**Alternative source-grounded interpretations:** The amended rule may have been applied with abbreviated reporting, a later decision may have restored the strict threshold, or both rules may produce identical observed counts.

**Human question:** Which primary success-coding rule governed pre-existing neurological disability and produced the printed ITT/PP numerators?

**Potential downstream evidence impact:** If confirmed, extraction could attach a different endpoint definition to the primary favorable-survival contrast; no change in event totals or trial conclusion is asserted.

## C002 — Planned additional-population outputs and identified reported analyses

**Status:** Pending Human Adjudication.

**Candidate statement:** Prespecified AT primary/key-secondary efficacy and randomized-group ITT safety outputs are not identifiable among the supplied report's named populations.

**Finding IDs:** F-XS-002, F-ST1-003. Checker provenance: cross_source_consistency_reviewer and statistics_pass_1; independent inclusion_screener. One repeated population-output reporting pattern retains both the narrower safety and broader efficacy manifestations.

**Exact source locations:** PLAN [SAP p121 §§5.1–5.3](../../joi180004supp1_prod.pdf#page=121), [p124 §§8.2.1/8.2.3/8.2.4](../../joi180004supp1_prod.pdf#page=124), [scanned analysis sets p130](../../joi180004supp1_prod.pdf#page=130), and [scanned methods p133](../../joi180004supp1_prod.pdf#page=133), versus REPORT [main p1 abstract efficacy/airway outcomes](../../jama_jabre_2018_oi_180004.pdf#page=1), [p3 Statistical Analysis](../../jama_jabre_2018_oi_180004.pdf#page=3), [p4 Figure/primary/adverse-event results](../../jama_jabre_2018_oi_180004.pdf#page=4), [p6 Tables2/3/post-hoc continuation](../../jama_jabre_2018_oi_180004.pdf#page=6), and [results supplement p3 eTable2](../../joi180004supp2_prod.pdf#page=3). Full REPORT article pp1–9 and results supplement pp1–3 were mapped/searched for the planned outputs.

**Source evidence:** SAP requires primary noninferiority analysis for ITT/PP/AT, secondary PP/AT, and safety ITT/AT. Report Table2 identifies ITT/PP; the center model is post-hoc ITT. Safety uses actual treatment, with14 ETI-assigned BMV recipients moved to BMV safety; full safety groups1028/999 differ from ITT1018/1022. Difficulty186/1027 versus134/996; failure69/1028 versus21/996; regurgitation156/1027 versus75/999. eTable2 labels one-way BMV-before-ROSC reassignment ITT, with41/863 versus45/1174, conventional P=.31, RD0.9%,95%CI[−0.9,2.7]. It supplies no identified AT noninferiority output or complete actual-technique mapping.

**Reasoning procedure and calculation:** Match explicitly planned population/output requirements to supplied population labels and contrasts. Randomized-group and actual-treatment safety cannot coincide under the explicit14-person reassignment. Neither rounded displays nor the one-way efficacy reassignment establish the complete SAP AT mapping or its NI result. No alternative population counts are reconstructed.

**Affected result or extracted value:** AT primary favorable-survival NI, AT day28/hospital-admission survival and ROSC, and ITT difficulty/failure/regurgitation contrasts—primary or abstract-listed secondary outcomes.

**Why context does not resolve it:** The SAP adds these identified outputs beyond the supplied ITT/PP efficacy and actual-treatment safety, while the report supplies neither identified counterparts nor an express replacement. Crossover-specific event counts and complete AT handling are unavailable.

**Classification rationale:** Explicit PLAN SAP requirements are compared with jointly identified REPORT outputs: P_R/protocol_report. Agreement/absence across REPORT sources does not add S_C.

**Classification ambiguity:** The SAP contains original-date and final-analysis wording; a later reporting decision or fuller output mapping is possible but not identified by supplied amendments.

**Alternative source-grounded interpretations:** Planned outputs may have been produced but not supplied, superseded by a later decision, or represented by an abbreviated sensitivity result with an unreported mapping. Nonperformance is not asserted.

**Human question:** Where are the planned AT efficacy and ITT safety outputs, or what documented change or complete mapping identifies their supplied counterparts?

**Potential downstream evidence impact:** If confirmed, an extractor could lack a planned population-specific contrast or equate the available actual-treatment/sensitivity result with a distinct randomized or AT result; no realized downstream reuse is asserted.

## C003 — Direct ETI crossover and safety membership accounting

**Status:** Pending Human Adjudication.

**Candidate statement:** The BMV-assigned participant directly intubated without receiving BMV is absent from both explicitly enumerated safety sets under the stated all-treated actual-treatment rule.

**Finding IDs:** F-NUM-001. Checker provenance: numeric_consistency_reviewer; independent inclusion_screener.

**Exact source locations:** REPORT [main p3 safety-population rule](../../jama_jabre_2018_oi_180004.pdf#page=3), [p4 Figure treatment/safety branches and total](../../jama_jabre_2018_oi_180004.pdf#page=4), and [p6 Table3 safety denominators](../../jama_jabre_2018_oi_180004.pdf#page=6).

**Source evidence:** BMV allocation1020:1014 received BMV;6 did not, including1 directly intubated because massive regurgitation prevented BMV. BMV safety1028 is explicitly1014+14 ETI-assigned BMV recipients. ETI safety999 is1023−14−9−1 from its randomized branch. Report total2027=1028+999. Safety is all treated by actual treatment, with failed ETI attributed to ETI.

**Reasoning procedure and calculation:** The999 ETI contributors are exhausted by the randomized-ETI branch. The never-BMV direct ETI recipient is absent from the BMV1028 sum and additional to that ETI branch. Applying the stated membership rule implies one further ETI contributor unless an additional exclusion applies.999+1=1000 and1028+1000=2028 are rule implications, not proposed replacement values. Participant counts within half-unit intervals retain their exact integer values; no fractional-patient relaxation removes the membership gap.

**Affected result or extracted value:** ETI safety-population size/membership and Table3 adverse-event denominator interpretation, including regurgitation75/999. No event numerator adjustment is asserted.

**Why context does not resolve it:** Neither safety box states an exclusion or placement for the direct ETI crossover. Outcome-specific missing observations and overlapping PP/rescue reasons do not identify this participant's overall safety membership.

**Classification rationale:** One REPORT contains the safety definition, flow and tables: S_W/statistical_results. A SAP corroborating or defining another population is not a conflicting comparator here.

**Classification ambiguity:** None in document roles or relationship; participant eligibility/membership remains unresolved.

**Alternative source-grounded interpretations:** An unstated additional exclusion may account for the published totals, or the participant may have been included under incompletely described accounting.

**Human question:** Was this directly intubated BMV-assigned participant included in ETI safety, and which membership or exclusion rule reconciles the stated999 ETI/2027 total?

**Potential downstream evidence impact:** If confirmed, safety-population attribution or a copied denominator could differ; the package cannot establish the participant's event outcomes or a replacement rate.

## C004 — Post-hoc reassignment population and success totals

**Status:** Pending Human Adjudication.

**Candidate statement:** The stated ITT155-person reassignment does not account for three participants and one primary success absent from the displayed post-hoc cohort.

**Finding IDs:** F-ST1-002. Checker provenance: statistics_pass_1; independent inclusion_screener.

**Exact source locations:** REPORT [main p3 post-hoc specification](../../jama_jabre_2018_oi_180004.pdf#page=3), [p4 continuation/ITT Figure/primary counts](../../jama_jabre_2018_oi_180004.pdf#page=4), [p6 post-hoc continuation](../../jama_jabre_2018_oi_180004.pdf#page=6), and REPORT [results supplement p3 eTable2 second analysis](../../joi180004supp2_prod.pdf#page=3).

**Source evidence:** Starting ITT1018+1022=2040, with44+43=87 favorable successes. Main describes155 BMV-before-ROSC intubations considered in ETI; supplement labels the same ITT reassignment and displays41/863 versus45/1174, RD0.9%,95%CI[−0.9,2.7],P=.31.

**Reasoning procedure and calculation:** Pure reassignment preserves participant/success totals.1018−155=863, but1022+155=1177 differs from1174.863+1174=2037 versus2040, and41+45=86 versus87. Pure exclusion155 would instead yield1885. Printed fractions yield100×(41/863−45/1174)=0.91782 percentage points, compatible with0.9 after rounding. Exact integer totals retain the three-person/one-success discrepancy under half-unit precision.

**Affected result or extracted value:** Post-hoc primary favorable-survival denominators863/1174, successes41/45 and interpretation of the0.9% contrast and interval.

**Why context does not resolve it:** Reassignment context resolves isolated exclusion wording but supplies no further three-person/one-success disposition. Original eligibility exclusions already precede the2040 ITT starting set.

**Classification rationale:** Main REPORT starting population/specification is compared with a different REPORT's resulting counts: S_C/statistical_results. Following independent screening, all relationships are S_C only; the isolated main exclusion wording is context-resolved and not an independent S_W conflict.

**Classification ambiguity:** An additional unreported exclusion or different starting population may account for the displayed cohort; no participant identities are assumed.

**Alternative source-grounded interpretations:** The cohort may include further exclusions, a count may belong to a different starting set, or155 may describe combined reassignment and exclusion.

**Human question:** What complete membership transformation takes ITT1018/1022 with44/43 successes to863/1174 with41/45?

**Potential downstream evidence impact:** If confirmed, an extractor could apply the post-hoc effect to a differently defined population or copy a population count without its transformation; no corrected count or conclusion is selected.
