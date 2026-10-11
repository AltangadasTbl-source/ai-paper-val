# Stable candidate ledger — Workflow 1.6.1

Pending Human Adjudication. Candidate discovery began afresh from the supplied sources and source-linked extraction assets. One issue was registered after independent inclusion screening, in source order. Assigned IDs are retained through all subsequent stages.

## Classification table

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R, S_C | REPORT main article p.3 vs PLAN protocol p.16; REPORT main article p.3 vs REPORT results supplement p.2 | reproduced | CONFIRMED | F-XS-001 |

Fresh source recheck assigned reproduced and confirmed document roles, all relationships, precedence and review domain. Fresh quality-control audit assigned CONFIRMED after reviewing every screening decision and checker exclusion.

## C001 — Composite primary endpoint uses different patient and care-opportunity weighting definitions

**Candidate statement:** The main article explicitly averages patient-specific fulfilled/eligible measure ratios, whereas the prospective protocol defines the composite as total fulfilled interventions divided by total possible interventions among eligible patients. The results supplement repeats the pooled definition and states that the randomized phase used the same endpoint definition. These summaries use different weights and the supplied Table 2 counts demonstrate numerically distinct descriptive quantities.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, S_C

**Compared document roles:** REPORT main article p.3 vs PLAN protocol p.16; REPORT main article p.3 vs REPORT results supplement p.2

**Finding IDs:** F-XS-001

**Checker provenance:** F-XS-001 from root/cross_source is the representative INCLUDE finding. Independent F-ST1-001 from root/statistics_1 and F-ST1-101 from root/statistics_1_design were consolidated as DUPLICATE_OF_INCLUDED and both map to C001. Their complete location union is preserved below. They do not create additional candidates.

**Classification rationale:** The prospective protocol is PLAN by content. Main article and results supplement are REPORT. The conflicting planned/report primary definition supplies P_R; the supplement's expressly randomized-phase definition also supplies S_C. P_R takes precedence. Opportunity-model paragraphs corroborate a separately modeled odds result and are not additional conflicts.

**Classification ambiguity:** No supplied endpoint-definition amendment is identified. The pooled language might have intended a patient-level average, but no supplied statement expressly reconciles it. This affects interpretation of the wording, rather than the document-role assignment.

**Exact source locations:**

- REPORT [main article PDF p.1, abstract Results](../../jama_wang_2018_oi_180070.pdf#page=1): composite 88.2% versus 84.8%; adjusted difference 3.54% (95% CI 0.68%–6.40%), P=.02.
- REPORT [main article PDF p.2, Key Points](../../jama_wang_2018_oi_180070.pdf#page=2): same composite percentages and improvement statement.
- REPORT [main article PDF p.3, Outcomes](../../jama_wang_2018_oi_180070.pdf#page=3): each patient's eligible-measure fraction calculated and then averaged.
- REPORT [main article PDF p.4, Data Analysis](../../jama_wang_2018_oi_180070.pdf#page=4): separate care-opportunity binary observations and adjusted ORPA analysis; corroborating analytical context.
- REPORT [main article PDF p.5, primary Results](../../jama_wang_2018_oi_180070.pdf#page=5): composite percentages, adjusted difference and ORPA 1.39 (1.12–1.72), P=.003.
- REPORT [main article PDF p.7, Table 2](../../jama_wang_2018_oi_180070.pdf#page=7): composite mean (SD), both inference columns and all nine performed/eligible count rows.
- PLAN [protocol PDF p.16, lines 216–220](../../joi180070supp1_prod.pdf#page=16): pooled total-intervention composite definition.
- PLAN [protocol PDF p.18, lines 266–274](../../joi180070supp1_prod.pdf#page=18) and [p.19, lines 275–279](../../joi180070supp1_prod.pdf#page=19): separate care-opportunity odds model, corroborating analytical context.
- REPORT [results supplement PDF p.2, eAppendix](../../joi180070supp2_prod.pdf#page=2): same-randomized-endpoint statement and pooled definition; baseline 80.2% and 79.5% are context, not compared randomized values.

**Source evidence and reported-versus-comparator:** Main Table 2 reports patient composite means 88.2% (SD 15.1) and 84.8% (SD 18.2). The protocol/supplement define a pooled fulfilled/possible intervention ratio. Both quantities are coherent; neither is presumed to be the intended planned definition without clarification.

**Reasoning procedure:** Let a_i be fulfilled eligible opportunities and b_i eligible opportunities for patient i. The main definition is U=(1/n)Σ(a_i/b_i). The protocol/supplement definition is W=Σa_i/Σb_i=Σ[b_i/Σb_j](a_i/b_i). U gives equal patient weights; W gives weights proportional to eligibility. Sum the exact Table 2 integer pairs across all nine measures to test the pooled descriptive definition. Keep adjusted difference and ORPA separate from this arithmetic.

**Calculation:**

| Measure | Intervention fulfilled/eligible | Control fulfilled/eligible |
|---|---|---|
| rtPA | 46/212 | 23/204 |
| Early antithrombotics | 2307/2353 | 2253/2330 |
| Dysphagia | 2255/2328 | 2040/2139 |
| DVT | 178/645 | 66/592 |
| Discharge antithrombotics | 2272/2324 | 2141/2305 |
| AF anticoagulation | 63/155 | 39/137 |
| Lipid-lowering | 1415/1481 | 1439/1547 |
| Antihypertensive | 1510/1838 | 1372/1771 |
| Antidiabetic | 653/728 | 557/663 |
| Total | 10699/12064 | 9930/11688 |

Pooled percentages are 88.6853448% and 84.9589322%, displaying as 88.7% and 85.0%. These lie outside the printed patient-mean half-unit intervals 88.15%–88.25% and 84.75%–84.85%. The integer counts are exact trial counts, not estimates. No adjusted effect is required to equal a crude ratio or difference; the reported adjusted difference 3.54 percentage points and ORPA 1.39 remain separately labeled results. Numerical size or significance of an alternative adjusted analysis cannot be determined.

**Affected result or extracted value:** The composite co-primary percentages 88.2% versus 84.8%, their patient-average versus opportunity-weighted meaning, and their correspondence with the prespecified endpoint. Extraction of the accompanying adjusted absolute difference requires clarity about its target summary.

**Why context does not resolve it:** The main text supplies an explicit patient-average definition; the plan and supplement supply an explicit pooled definition, and the supplement says it applies to the randomized phase. The separate opportunity-level ORPA model explains that inference but does not reconcile the competing descriptive endpoint definitions or identify how the adjusted absolute difference maps to them.

**Alternative source-grounded interpretations:** The report may use a patient-average descriptive endpoint where the plan described pooled weighting; alternatively, the plan/supplement may use pooled language as shorthand for patient averaging. No supplied amendment or explicit reconciliation selects between these interpretations. No preferred analysis is proposed.

**Remaining human question:** Which aggregation was prespecified and used for the randomized composite, and how does it relate to the reported adjusted absolute-difference analysis?

**Potential downstream evidence impact:** If the candidate is confirmed, a data extractor could label the primary composite as either a patient-average adherence score or an opportunity-level adherence proportion. These represent different endpoint summaries. No propagation, changed statistical significance or changed paper conclusion is established.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

**Evidence state:** reproduced

**Mechanical evidence recheck:** Every ten cited PDF page locations and all nine count rows were confirmed from exact-source text and direct source-page renders. No registration transcription or classification required amendment. In addition to exact sums, allowing ±0.5 for every displayed numerator and denominator yields pooled ranges 88.6149894%–88.7557527% and 84.8877486%–85.0301708%. Both remain outside the respective printed-mean intervals. Participant fractions, an endpoint-definition reconciliation and the exact target of the adjusted difference are unavailable. Full separate mechanical facts appear in verification/evidence_recheck.md.

**Human verification steps:** Read main p.3, protocol p.16 and supplement p.2 together; establish whether the pooled wording is literal or shorthand for patient averaging. Confirm all nine Table 2 event/eligibility pairs, reproduce the pooled totals and display intervals, and distinguish descriptive means from the separately adjusted absolute difference and opportunity-based ORPA. Seek clarification of the planned aggregation and the actual target of the adjusted difference before adjudicating validity, importance or action.

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Exact competing primary endpoint definitions are reproduced, are in focus D, are not explicitly reconciled by the opportunity-model context, and can affect the weighting interpretation and extraction of the named primary composite. All screening decisions and checker exclusions were audited; no additional qualifying issue or classification change was identified. This is an inclusion-threshold audit, with human adjudication still pending.
