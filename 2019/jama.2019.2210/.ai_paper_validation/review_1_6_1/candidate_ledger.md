# Workflow 1.6.1 Candidate Ledger

Pending Human Adjudication. Discovery began from supplied evidence, independently of prior candidates. Two included checker findings describe one issue; source order assigns C001. No candidate-count target applies. Classification was confirmed by mechanical recheck and independently audited for inclusion.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | statistical_results | S_C | S_C | REPORT main article Table 1 p.5 vs REPORT results supplement eFigures 3P–3R pp.22–24 | reproduced | CONFIRMED | F-XS-001, F-ST1-001 |

## C001 — DBP1 TG placebo subgroup population does not reconcile across report documents

**Candidate statement:** Main Table 1 reports 57 placebo participants with DBP1 TG, while the same named subgroup's zero-year risk row in eFigure 3Q reports 59. The associated placebo DBP1 category totals are 148 and 150. The supplied context does not state a population rule explaining the difference.

**Review domain:** statistical_results
**Relationship type:** S_C
**All relationships:** S_C
**Compared document roles:** REPORT main article Table 1 p.5 vs REPORT results supplement eFigures 3P–3R pp.22–24
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-XS-001, F-ST1-001
**Classification rationale:** The conflicting participant classifications and starting risk counts occur in two different REPORT documents. Both concern counts/analysis populations, so statistical_results applies. PLAN genotype definitions only provide context and do not create a competing relationship.
**Classification ambiguity:** None

**Exact source locations:** [Main article PDF p.5, Table 1, DBP1 rows](../../jama_urashima_2019_oi_190023.pdf#page=5); [results supplement PDF p.23, eFigure 3Q, placebo No. at risk at year0](../../joi190023supp2_prod.pdf#page=23). Corroborating category counts: [results p.22, eFigure 3P, TT](../../joi190023supp2_prod.pdf#page=22) and [results p.24, eFigure 3R, GG](../../joi190023supp2_prod.pdf#page=24). Context: [main p.3, subgroup/analysis methods](../../jama_urashima_2019_oi_190023.pdf#page=3).

**Source evidence:** Table 1 placebo DBP1 TT82(55), TG57(39), GG9(6); vitamin D TT134(58), TG87(38), GG10(4). Supplement eFigures 3P/3Q/3R placebo initial risk counts82/59/9, vitamin D134/87/10. eFigure 3Q reports relapse-or-death HR1.00 (95%CI0.44–2.24), P=.99 and interactionP=.49.

**Reported-versus-comparator:** Main baseline TG57 versus initial plotted TG59; main placebo category sum148 versus plotted category sum150. Vitamin D category sum231 agrees. TT and GG placebo counts agree.

**Reasoning procedure:** Match allocation, DBP1 genotype, endpoint and zero-year time origin. Compare exact participant counts, distinguishing initial subgroup population from later contributors. Apply the explicit analysis-population exception to peripheral comparisons. Consolidate the two-person difference and category-total consequence as one issue.

**Calculation:** 59−57=2;82+57+9=148;82+59+9=150;134+87+10=231 in both locations. Whole-participant counts are exact; even half-unit display intervals [56.5,57.5] and [58.5,59.5] do not overlap.

**Affected result or extracted value:** The placebo DBP1 TG starting subgroup population accompanying the reported relapse-or-death HR1.00, and the placebo DBP1 genotype-available population total. No difference in the printed HR, P value or whole-trial efficacy population is asserted.

**Why context does not resolve it:** Neither Table 1 nor the supplement caption states a different genotype analysis set, reclassification or added participants. Baseline 25(OH)D imputation addresses a separate variable. The matching allocation/genotype labels and agreeing adjacent categories do not select a reconciliation for the additional two placebo participants.

**Alternative source-grounded interpretations:** Baseline classification and plotted analysis may use different genotype-available sets, or a displayed count may require reconciliation. The package supplies no genotype membership/model records establishing either explanation. The printed zero-year risk count does not independently prove Cox model membership.

**Mechanical evidence recheck:** reproduced. The fresh rechecker matched every cited source cell and risk row, confirmed exact arithmetic and disjoint integer display intervals, and retained REPORT/REPORT roles, S_C and statistical_results. No transcription correction was needed. Genotype-set and model-membership definitions remain absent; the zero-year risk row alone does not prove Cox model membership. Full facts are in [the recheck artifact](verification/evidence_recheck.md).
**Potential downstream evidence impact:** A data extractor could take57 or59 as the subgroup placebo population, or148 or150 as the genotyped placebo total. Actual changes to pooled estimates, trial conclusions or clinical decisions are not established.
**Human verification steps:** Reread the cited cells/risk rows; inspect genotype classification and model-membership records; determine the population rule linking Table 1 to the subgroup curve and associated HR; adjudicate the unresolved count relationship without assuming a replacement value.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __
