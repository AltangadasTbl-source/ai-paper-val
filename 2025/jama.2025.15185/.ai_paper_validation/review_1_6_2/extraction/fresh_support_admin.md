# Fresh administrative and analysis-code support map

Scope DOC-005 pages 1–8; DOC-006 page 1; DOC-007 page 1, all REPORT by published package content. All ten pages opened via allowed complete older factual layouts, with code visually inspected in `.ai_paper_validation/review_1_5_1/preprocessing/support_mapper/doc006/page-1.png`. Reused layouts: same directory `DOC-005-layout.txt`, `DOC-006-layout.txt`, `DOC-007-layout.txt`. Legacy engine unrecorded. No new derivative engine used, no Office/workbook source, formula caches not applicable.

| Key | Direct source location | Applicable relationship / no-applicable reason |
|---|---|---|
| AD01 | joi250066supp4_prod_1761597796.4751.pdf#page=1 | Nonauthor collaborators: Aarau, Baden, Lausanne names and roles; footer version02-22,1of8; no trial count, endpoint, test or analysis definition. |
| AD02 | joi250066supp4_prod_1761597796.4751.pdf#page=2 | Collaborators Lausanne, Fribourg, Hirslanden; footer2of8; no applicable quantitative relationship. |
| AD03 | joi250066supp4_prod_1761597796.4751.pdf#page=3 | Collaborators Bern and Basel; footer3of8; no applicable quantitative relationship. |
| AD04 | joi250066supp4_prod_1761597796.4751.pdf#page=4 | Basel collaborators; footer4of8; no applicable quantitative relationship. |
| AD05 | joi250066supp4_prod_1761597796.4751.pdf#page=5 | Basel and Zurich collaborators; footer5of8; no applicable quantitative relationship. |
| AD06 | joi250066supp4_prod_1761597796.4751.pdf#page=6 | Graubünden, Münsterlingen, StGallen, FelixPlatter collaborators; footer6of8; no applicable quantitative relationship. |
| AD07 | joi250066supp4_prod_1761597796.4751.pdf#page=7 | FelixPlatter and Rheinfelden collaborators; footer7of8; no applicable quantitative relationship. |
| AD08 | joi250066supp4_prod_1761597796.4751.pdf#page=8 | Rheinfelden and Valens collaborators; footer8of8; no applicable quantitative relationship. |
| AD09 | joi250066supp5_prod_1761597796.4751.pdf#page=1 | ESTREL Main Analysis Code,35numbered lines. See full implementation transcription below; matches main primary baseline-adjusted linear model, randomized treatment, MI pooling and diagnostics. |
| AD10 | joi250066supp6_prod_1761597796.4801.pdf#page=1 | Data sharing statement: ClinicalTrials.govNCT03735901,BASEC2018-02021;data available field No;trial data may be available on reasonable request with detailed study proposal, objectives andSAP, approval by corresponding author/sponsor,steering committee andeachcenter PI subject to ethics/consent. No result-relevant numerical relationship; identifiers administrative. |

## AD09 implementation relationships

These are printed R formulas, not executed results or workbook caches. No raw data or imputation object is supplied in this source.

- Lines4–5 load `ggplot2` and `mice`.
- Lines8–10: `load("dat/dat.rda")` raw data; `load("dat/mice0.rds")` imputations on FAS; `N.imp <- length(mice0$imp[[1]])` number of imputations used. This source does not print an evaluated N.imp.
- Lines13–16 graph raw data with medication as x, `my.data[, ep]` as y, boxplot plus jitter, white outliers, `theme_bw()` and `ylab(ep.name)`.
- Lines19–23 define `fma_affected.Visit_3` primary endpoint, `fma_affected.Visit_1.cent` centered baseline, medication according to randomization. Formula: `model <- with(mice0, lm(fma_affected.Visit_3 ~ fma_affected.Visit_1.cent + medication))`.
- Line26 `summary(pool(model))` pools and returns model. No coefficients, confidence intervals or P values printed in code PDF.
- Lines29–35 diagnostics: `par(mfrow = c(2,2))`; loop `for(i in c(1:N.imp))`; fit `lm(fma_affected.Visit_3 ~ fma_affected.Visit_1.cent + medication, data = complete(my.data = mice0, i))`; `plot(m, main = paste0("Imputation: ", i))`; reset `par(mfrow = c(1,1))`.

All ten assigned units mapped. Eight collaborator pages and sharing page have no applicable trial quantitative relationships; code page supplies five implementation relationships. No scientific coverage gap.
