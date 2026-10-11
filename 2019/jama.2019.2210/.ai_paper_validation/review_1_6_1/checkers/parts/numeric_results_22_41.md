# Numeric consistency review: results supplement pages 22–41

Runtime agent ID: 01a128e0-08d6-7511-a772-13eef531d888. Scope: DOC-003 physical PDF pp.22–41, R-N301–R-N320 → N117–N136; REPORT content. Complete scope/contract read. All 20 exact-page reusable images were visually inspected; fresh mapper text and canonical main/support maps provided locators and matching context. No old candidate/report conclusions or external evidence were used. All 160 risk entries, their row alignment, labels, time axes, nonnegative/nonincreasing rules, eight collection partitions, and source-grounded HR identity were checked. Full inputs and exact componentwise calculations are in [the assigned inventory](../../relationships/parts/numeric_results_22_41.md).

## Findings

No observation in this complete shard meets all four inclusion criteria. Qualifying findings: 0; no F-NUM-201 ID is assigned. Collection sums reconcile exactly or describe source-defined partial subgroup coverage; no result-bearing extraction ambiguity remains under the applicable numeric rules.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| [REPORT DOC-003 pp.22–24 DBP1](../../../../joi190023supp2_prod.pdf#page=23) vs [REPORT DOC-001 p.5 Table1](../../../../jama_urashima_2019_oi_190023.pdf#page=5) | DBP1 TG placebo baseline risk count59 versus descriptive Table1 genotype count57; collection baseline P150 versus main descriptive sum148. Exact integers differ, but this is baseline subgroup description/risk-table comparison; no named primary/key-secondary result or full analysis-population size changes. Consolidated single observation for the same difference. | PERIPHERAL_COMPARISON |
| REPORT DOC-003 pp.22–27 DBP collections; REPORT DOC-001 p.6 overall | Genetic-category risk sums P150/D231 below randomized P166/D251. Claiming every randomized person has available genotype data is not established; the category sums are not stated full-trial analysis denominators. | CONDITIONAL_OR_UNREPORTED |
| [REPORT DOC-003 pp.32–33 BMI](../../../../joi190023supp2_prod.pdf#page=32), REPORT DOC-001 p.5 | BMI risk baseline totals P165/D249 agree with main available category sums. Difference from randomized P166/D251 is resolved by available BMI population; all residual time vectors remain nonnegative/nonincreasing. | CONTEXT_RESOLVES |
| [REPORT DOC-003 pp.34–36 site](../../../../joi190023supp2_prod.pdf#page=34), REPORT DOC-001 p.5 | Three displayed sites total P165/D250; main Table1 additionally includes small-bowel P1/D1. This partial figure collection does not claim to contain that category, and residual risk vectors are coherent. | CONTEXT_RESOLVES |
| [REPORT DOC-003 p.30 age caption](../../../../joi190023supp2_prod.pdf#page=30) | Caption says younger than median (≤65) while title says age65 and younger; explicit numeric threshold ≤65 and opposite >65 panel establish intended split. | TERMINOLOGY_OR_WORDING |
| [REPORT DOC-003 p.33 BMI title/caption](../../../../joi190023supp2_prod.pdf#page=33) | ASCII >= and superscript/ordinary m2 notation describe the same ≥25 kg/m² threshold. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC-003 pp.22–41, particularly [p.27](../../../../joi190023supp2_prod.pdf#page=27), [p.33](../../../../joi190023supp2_prod.pdf#page=33), [p.34](../../../../joi190023supp2_prod.pdf#page=34), [p.38](../../../../joi190023supp2_prod.pdf#page=38), [p.41](../../../../joi190023supp2_prod.pdf#page=41) | Terminal cumulative-hazard ordering or ratio need not equal whole-follow-up Cox HR; HR is model-based, step heights are not exact printed event probabilities, and some curves cross. One consolidated quantity-identity observation covers all locations. | MODEL_VERSUS_CRUDE |
| REPORT DOC-003 pp.22–41 risk rows | Risk-set reductions cannot be converted into exact relapse/death counts without censoring histories; an asserted event numerator derived solely by baseline-minus-final risk counts would depend on an unsupported no-censoring assumption. | CONDITIONAL_OR_UNREPORTED |

## Completion and limitations

20/20 numeric relationships complete, 20/20 pages inspected, 160 printed risk entries checked, eight collection calculations completed, 0 findings, 8 excluded observations. Source-derived count partition checks require no rounding relaxation because their inputs are exact integers. Two-decimal HR inputs retain half-unit 0.005 intervals when relevant; no crude ratio or digitized coordinate was substituted for a modeled HR. No scientific coverage gap. Exact event/censoring histories and individual model coefficients are absent and were not inferred. This shard neither duplicates core local N checks nor adjudicates inferential S relationships.
