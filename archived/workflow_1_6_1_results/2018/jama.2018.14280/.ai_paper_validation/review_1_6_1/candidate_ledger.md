# Stable Candidate Ledger

Pending Human Adjudication. Discovery began with all supplied source units and eligible reusable evidence; no earlier candidate selection was used. The independent screen included two checker findings describing one issue. One stable candidate is registered in source order. The mechanical source recheck and independent inclusion audit are complete; the audit records CONFIRMED.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | statistical_results | S_W | S_W | REPORT main article Table 2 and footnote c vs REPORT main article Statistical Analysis and abstract | reproduced | CONFIRMED | F-NUM-001, F-ST1-001 |

## C001 — Binary risk-ratio definition does not reconcile with the displayed intervention event fractions

**Candidate statement:** The repeated binary risk ratios and intervals in Table 2 and the abstract do not identify the same intervention event-risk quantity as the printed low-versus-intermediate event fractions. Eight rows remain discrepant under conservative display-precision intervals; two near-null rows are corroborating occurrences only. An alternative conditional ratio tracks the printed family, but the supplied materials do not define that quantity as the reported intervention effect.

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 2 and footnote c vs REPORT main article Statistical Analysis and abstract
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-NUM-001, F-ST1-001
**Classification rationale:** The conflicting effect label, fractions and displayed estimates occur inside the main REPORT. The PLAN SAP corroborates the intended RR label and is not a conflicting comparator, so no P_R relationship is added. One repeated effect-definition pattern is registered with all occurrences.
**Classification ambiguity:** None

**Exact source locations:**

| Role | Exact affected or supporting location | Evidence link |
|---|---|---|
| REPORT | Table 2, ICU mortality | [Main PDF p. 6](../../jama_simonis_2018_oi_180108.pdf#page=6) |
| REPORT | Table 2, hospital mortality | [Main PDF p. 6](../../jama_simonis_2018_oi_180108.pdf#page=6) |
| REPORT | Table 2, development of ARDS | [Main PDF p. 6](../../jama_simonis_2018_oi_180108.pdf#page=6) |
| REPORT | Table 2, development of pneumonia | [Main PDF p. 6](../../jama_simonis_2018_oi_180108.pdf#page=6) |
| REPORT | Table 2, pneumothorax | [Main PDF p. 6](../../jama_simonis_2018_oi_180108.pdf#page=6) |
| REPORT | Table 2, atelectasis; corroborating under the conservative count test | [Main PDF p. 6](../../jama_simonis_2018_oi_180108.pdf#page=6) |
| REPORT | Table 2, extrapulmonary infection | [Main PDF p. 6](../../jama_simonis_2018_oi_180108.pdf#page=6) |
| REPORT | Table 2, extrapulmonary sepsis | [Main PDF p. 6](../../jama_simonis_2018_oi_180108.pdf#page=6) |
| REPORT | Table 2, delirium | [Main PDF p. 6](../../jama_simonis_2018_oi_180108.pdf#page=6) |
| REPORT | Table 2, need for tracheostomy; corroborating under the conservative count test | [Main PDF p. 6](../../jama_simonis_2018_oi_180108.pdf#page=6) |
| REPORT | Abstract Results, ARDS | [Main PDF p. 1](../../jama_simonis_2018_oi_180108.pdf#page=1) |
| REPORT | Abstract Results, pneumonia | [Main PDF p. 1](../../jama_simonis_2018_oi_180108.pdf#page=1) |
| REPORT | Abstract Results, severe atelectasis; precision nuance retained | [Main PDF p. 1](../../jama_simonis_2018_oi_180108.pdf#page=1) |
| REPORT | Abstract Results, pneumothorax | [Main PDF p. 1](../../jama_simonis_2018_oi_180108.pdf#page=1) |
| REPORT | Table 2, footnote c; RR, interval and test specification | [Main PDF p. 6](../../jama_simonis_2018_oi_180108.pdf#page=6) |
| REPORT | Statistical Analysis, binary outcome specification | [Main PDF p. 4](../../jama_simonis_2018_oi_180108.pdf#page=4) |
| PLAN corroboration | SAP Secondary outcomes, RR/Wald/chi-square specification; no conflicting plan side | [SAP PDF p. 13](../../joi180108supp2_prod.pdf#page=13) |

**Source evidence:**

| Table 2 outcome | Low event/total | Intermediate event/total | Reported RR (95% CI) | Event-risk ratio at printed counts | Alternative conditional ratio |
|---|---|---|---|---|---|
| ICU mortality | 132/450 | 115/458 | 1.11 (0.96–1.27) | 1.168232 | 1.110840 |
| Hospital mortality | 151/477 | 140/484 | 1.06 (0.93–1.22) | 1.094400 | 1.066452 |
| ARDS | 17/448 | 23/462 | 0.86 (0.59–1.24) | 0.762228 | 0.857889 |
| Pneumonia | 19/450 | 17/462 | 1.07 (0.78–1.47) | 1.147451 | 1.072699 |
| Pneumothorax | 8/448 | 6/462 | 1.16 (0.73–1.84) | 1.375000 | 1.163636 |
| Atelectasis | 51/449 | 52/464 | 1.00 (0.81–1.23) | 1.013534 | 1.007708 |
| Extrapulmonary infection | 20/448 | 28/463 | 0.84 (0.60–1.18) | 0.738202 | 0.840148 |
| Extrapulmonary sepsis | 12/448 | 16/463 | 0.87 (0.56–1.33) | 0.775112 | 0.867955 |
| Delirium | 149/343 | 132/361 | 1.15 (0.99–1.34) | 1.188025 | 1.156162 |
| Need for tracheostomy | 54/477 | 52/484 | 1.03 (0.84–1.26) | 1.053701 | 1.029707 |

**Reported-versus-comparator:** RR labels and effect values versus the treatment-event risk contrast supplied by the adjacent arm-specific fractions; all compared locations are in REPORT material.

**Reasoning procedure:** Match event, assessment population, low/reference group and effect definition. Check all fractions and repeated abstract values directly. Compare R=(a/n)/(c/m) with each two-decimal RR interval, retaining half-unit intervals for every displayed count. Evaluate Q=[a/(a+c)]/[(n−a)/(n+m−a−c)] only as a diagnostic alternative, not as an assertion about computation code. A chi-square P value is symmetric under contingency-table transposition, so this finding does not assert a separate P-value contradiction.

**Calculation:** For ARDS, R=(17/448)/(23/462)=0.762228, conservative half-unit range 0.722479–0.803849, disjoint from reported 0.855–0.865. Q=(17/40)/(431/870)=0.857889; diagnostic log-Wald interval 0.594560–1.237844 tracks printed 0.59–1.24. For pneumothorax, R=1.375000, half-unit range 1.187291–1.597257, disjoint from reported 1.155–1.165; Q=1.163636. ICU/hospital mortality, pneumonia, infection, sepsis and delirium also remain discrepant. Atelectasis and tracheostomy overlap under the conservative precision test and are corroborating locations only. Full row precision bounds and CI diagnostics are preserved in checkers/numeric_consistency.md.

**Affected result or extracted value:** Binary intervention RRs and 95% CIs, particularly the abstract ARDS, pneumonia and pneumothorax effects, used in downstream effect extraction.

**Why context does not resolve it:** The methods, footnote and abstract give no alternate conditioning or established binary model that identifies the displayed effect quantity. A reader can calculate the column-count event ratio but cannot identify which definition generated the printed effect and interval. Nearby Cox, GLM and mixed-model descriptions apply to separately identified outcomes.

**Alternative source-grounded interpretations:** The displayed effects may reflect the diagnostic reverse-conditioned quantity, or an additional binary model whose coding, adjustment and estimand are unstated. Neither mechanism is asserted; binary computation code and a complete effect definition are unavailable.

**Mechanical evidence recheck:** Direct source recheck matched all ten Table 2 rows, four abstract repetitions, methods and corroborating SAP text; reproduced the eight robust count-based discrepancies and documented overlapping corroborating rows and diagnostic limitations. See verification/evidence_recheck.md.

**Potential downstream evidence impact:** If confirmed by human review, clarification could change the binary effect quantity and interval extracted for evidence synthesis. No change in the primary conclusion or the secondary nonsignificance statements is established by this observation.

**Human verification steps:** Inspect every Table 2 RR row and footnote c, the p. 4 binary analysis paragraph and repeated p. 1 results; clarify outcome/group coding, denominator conditioning, reference group and any adjustment behind the effect and interval. No replacement analysis or final value is selected here.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

Recheck precision nuance: the abstract's rounded atelectasis percentages (11.4%/11.2%) imply an event-risk ratio range 1.008889–1.026906, disjoint from the printed RR interval 0.995–1.005. The deliberately broader count-half-unit test for its Table 2 fraction overlaps. Both facts are retained; this row remains corroborating in the registered eight-robust-row pattern, with no new issue or inferred computation code.
