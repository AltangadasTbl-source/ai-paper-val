# Support statistical relationship inventory

Scope: DOC-002 through DOC-007. These are provisional `US` relationship IDs; no candidate assessment was performed.

| Provisional ID | Direct source location | Definition / model / statistical relationship | Match key |
|---|---|---|---|
| US001 | DOC-003#page=2 | SAP objective: levodopa/carbidopa 100/25 mg three times daily versus placebo added to standardized rehabilitation; primary functional recovery at three months measured by Fugl-Meyer Motor Assessment (FMMA/FMA). | `primary FMA three months levodopa placebo`. |
| US002 | DOC-003#page=2 | SAP secondary objective concerns survival and general health. | `secondary survival general health`. |
| US003 | DOC-002#page=8-10; DOC-003#page=2 | Protocol/SAP specify planned primary endpoint and eligibility/timing definitions; these are analysis-plan comparators, not observed outcome results. | `protocol-SAP primary endpoint`. |
| US004 | DOC-004#page=6 | Analyses used R version 4.3.1; page lists data-processing, modeling, and visualization packages. | `software R 4.3.1`. |
| US005 | DOC-004#page=7 | Multiple imputation used 100 chained-equation imputations; estimates and variances were combined using Rubin rules. | `MI 100 chained equations Rubin rules`. |
| US006 | DOC-004#page=12-13 | eTable 2 identifies estimands by population, endpoint, intercurrent-event strategy, participant count, and mean difference on FMA [CI]. | `estimand FMA mean difference CI`. |
| US007 | DOC-004#page=14 | eTable 3 identifies post hoc estimand models including change from baseline. | `post hoc FMA change baseline`. |
| US008 | DOC-004#page=15 | Secondary-outcome table reports group means (SD), standardized mean difference, and mean difference [CI]. | `secondary FMA SMD mean difference CI`. |
| US009 | DOC-004#page=18 | eTable 7 includes a baseline-FMA × treatment interaction; eTable 8 models baseline FMA with splines of 3 degrees of freedom without interaction. | `baseline interaction spline 3df`. |
| US010 | DOC-004#page=23-24 | Forest plot displays FMA-total-score three-month estimands and effect direction (favoring placebo vs favoring levodopa). | `forest FMA three months estimands`. |
| US011 | DOC-004#page=26 | Nonlinear association between baseline and three-month FMA is represented by spline model. | `nonlinear baseline 3-month FMA spline`. |
| US012 | DOC-004#page=27 | Forest plot legend defines post hoc death-imputed-zero and adherence/rehabilitation-exclusion analyses plus subgroup analysis. | `PH1 death zero PH2 adherence rehab PH3 subgroup`. |

No displayed zero P-value was used as a candidate. No P-value compatibility calculation was attempted where test sidedness, variance convention, adjustment, or exact model inputs were not supplied in the mapped page.
