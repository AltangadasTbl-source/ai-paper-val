# Independent inclusion screen

Stage: initial inclusion_screener. Runtime ID: `01a128e7-44e6-7420-bb8e-ffde83b45eed`; model/effort/start: `gpt-6.1-sol/high/FRESH_SPAWN`.

The complete normative scope and review contract, including the inclusion-screen section, and all three canonical checker artifacts were read. The numeric checker has no finding IDs; the cross-source and statistical pass 1 checkers each supply one finding. Decisions below follow independent direct-source rereading, without a finding-count target or prior-run scientific conclusions.

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-XS-001 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-ST1-001 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C001 |

- **F-XS-001:** [REPORT Table 1, main article p.5](../../../jama_urashima_2019_oi_190023.pdf#page=5) prints placebo DBP1 TG 57 whereas [REPORT eFigure 3Q, results supplement p.23](../../../joi190023supp2_prod.pdf#page=23) prints 59 at zero years since randomization beside the named relapse-or-death HR 1.00 (95% CI 0.44–2.24), and this difference changes the displayed subgroup analysis-population size without a table, caption, or [main methods p.3](../../../jama_urashima_2019_oi_190023.pdf#page=3) population rule that lets a field reader identify the intended extracted subgroup count at once.
- **F-ST1-001:** Independent rereading reproduces the same 57/59 placebo TG discrepancy and its 148/150 DBP1 category-total consequence, with unchanged TT and GG placebo initial counts of 82 and 9 in [eFigure 3P, p.22](../../../joi190023supp2_prod.pdf#page=22) and [eFigure 3R, p.24](../../../joi190023supp2_prod.pdf#page=24), so it independently meets the count/extraction threshold and is consolidated with F-XS-001 into the same issue rather than a second candidate.

## Consolidation and scope decision

One proposed included issue, **DBP1 TG placebo subgroup population**, contains finding IDs `F-XS-001` and `F-ST1-001`; both INCLUDE rows received coordinator-assigned C001. All affected evidence locations are main article Table 1 p.5 and results supplement eFigures 3P–3R pp.22,23,24; main methods p.3 supplies contextual definitions. All compared documents are REPORT; proposed review domain is `statistical_results`, primary relationship `S_C`, all relationships `S_C`. No PLAN content supplies a conflicting count.

The comparison tiers were applied before the four inclusion criteria. Descriptive baseline counts and later time-specific contributors ordinarily are peripheral; here the zero-year risk row explicitly describes the starting population for the displayed DBP1 TG relapse-or-death subgroup analysis. The exception for a change to the size of an analysis population applies to this named subgroup population and does not require a change to the entire 417-person randomized population. Accordingly the numeric shard's peripheral rationale for this same observation does not resolve the exception; no additional numeric finding is created by this screen.

The four criteria hold: (1) direct-source text and full-page images reproduce the exact counts and 59−57=2, with 82+57+9=148 versus 82+59+9=150; (2) this is focus area A and an analysis-population exception to the peripheral comparison tier; (3) the identical genotype/allocation labels and matching vitamin D counts do not identify a reason for the additional two placebo participants, and the reported imputation procedure concerns baseline 25(OH)D rather than genotype membership; (4) the extractable placebo sample size accompanying eFigure 3Q's HR can be 57 or 59 depending on which source population applies. Participant counts are exact integers; even treating them as whole-unit displays gives disjoint half-unit intervals, so rounding cannot reconcile them.

A distinct genotype-available subset, later genotype ascertainment, or a displayed count requiring reconciliation could explain the observation, but none is stated in the immediate source context. This screen does not assume that the printed initial risk count proves the actual Cox model membership, does not infer an altered HR or interaction P value, and does not claim changed primary all-population conclusions. The issue is the unresolved link between participant classification and the displayed starting subgroup population.

## Evidence method and limits

Direct local Poppler `pdftotext -layout` 26.01.0 reread main article pp.3–5 and results supplement pp.22–24. Direct local Poppler `pdftoppm` 26.01.0 freshly rendered main p.5 at scale 1800 and results pp.22–24 at scale 1500; all four full-page images were visually inspected. Unique derivatives: `screening/direct_source/main-5.png`, `screening/direct_source/results-22.png`, `screening/direct_source/results-23.png`, and `screening/direct_source/results-24.png`. No derivative/source disagreement was found; no OCR, fallback environment, external evidence, or scientific Python reasoning was needed. Supplied sources and reusable assets were preserved.

Screened findings: **2**; INCLUDE finding rows: **2**; consolidated included issues: **1**; SCREENED_OUT findings: **0** (all screened-out reason-code counts zero). No source-page screening limitation. Actual genotype records and model membership are not supplied; the remaining human question is which placebo DBP1 TG population belongs with eFigure 3Q and what population rule reconciles its initial risk count with Table 1. Candidate C001 is registered by the coordinator and remains Pending Human Adjudication.

## Coordinator audit follow-up

The fresh quality-control auditor independently confirmed both INCLUDE decisions for C001. Its audit of the numeric shard's excluded DBP1 observation found that limiting the analysis-population exception to the full trial population was narrower than the normative scope. That observation is the same already registered issue C001; original checker provenance is preserved, and no additional finding, candidate or screening decision is added. All other checker exclusions were reviewed without a new qualifying issue. Final audit facts are recorded in quality/evidence_quality_audit.md.
