# C009 — Independent focused source recheck

Scope: C009 only; one affected location. All source and prior audit artifacts were preserved. This is a fresh follow-up note, not a replacement of the canonical ledger or evidence record.

## Exact source and direct observation

- Location found: main article, Table 2, PDF page 9, printed JAMA page 600; secondary outcome **Pain intensity**, **12 months**, **Health coach vs painTRAINER**, adjusted NNT (95% CI) column.
- Exact supplied source: [Main article, Table 2](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9).
- Source tuple matched visually: **63 (18–38)**. The column heading explicitly labels the interval **95% CI**. The point estimate 63 exceeds the printed upper endpoint 38.
- Comparator matched visually in the same row: adjusted improvement proportions **33.7%** for Health coach and **32.1%** for painTRAINER; corresponding RR **1.05 (0.92–1.20)**. The RR null-coverage question is C008 context and is not merged into C009.
- Visual authority: existing full-page source render `preprocessing/initial_screen/main_p9.png` was inspected directly. No fresh extraction or OCR was required. The inspected image is a page rendering, not an OCR transcription. Main methods page 4 and results supplement page 5 were also visually inspected using existing renders.

## Stated rule and reproduction

Main article PDF page 4, Statistical Analysis, defines adjusted NNT as “1 divided by the difference in adjusted percent improvement between groups.” Table 2 footnote d repeats the reciprocal adjusted-risk-difference definition. Footnote e explains that an absolute-risk-difference interval containing zero yields NNT limits involving infinity, with positive benefit and negative harm branches. These supplied definitions support reading the printed tuple as the adjusted NNT and its uncertainty interval for this same contrast.

The printed point **63** lies above **38**, the upper endpoint. Half-unit display intervals are **[62.5, 63.5)** for 63 and **[37.5, 38.5)** for 38; their minimum separation is **24**. Thus display precision cannot make the point fall inside the printed interval. Using the displayed point as the reference, the minimum separation is **24/63 = 38.10%**. Scope route A category 1 explicitly registers a point outside its interval; this does not depend on choosing an RR-based interval method.

The displayed improvement proportions give a risk difference of **1.6 percentage points**, so the reciprocal is **100/1.6 = 62.5**. Reporting that as integer **63** is compatible with the point value. Allowing both proportions their half-unit intervals gives a difference from **1.50 to 1.70 percentage points**, hence an NNT from approximately **58.82 to 66.67**. This overlaps the display interval for 63, but remains above the entire displayed upper endpoint interval for 38. This check supports the point's compatibility with the marginal proportions; it does not identify an intended replacement interval.

## Available and missing inputs

Necessary inputs for the direct observation are available: the NNT point, both limits, 95% label, contrast, time point, outcome, and reciprocal-risk-difference definition. Necessary inputs for an independently reconstructed confidence interval are not available in the inspected descriptions: unrounded adjusted risks and risk difference; the relevant contrast variance/covariance; the exact RD interval construction; and the transformation, endpoint, and rounding steps used to generate this NNT interval. Results Supplement 4 page 5 explains joint imputation/estimation variance-covariance handling, but does not give the row-specific risk-difference interval or an explicit NNT interval recipe.

The coordinator separately inspected Supplement 4 PDF page 15, eTable 9: it has no NNT columns and is explicitly unadjusted without imputation or weighting, so it cannot supply a replacement adjusted NNT interval. As a diagnostic only, the reciprocal limits 18–38 imply approximately **2.63–5.56 percentage points** of risk difference, whereas the displayed same-row point proportions differ by **1.6 percentage points**; these are not independently reconstructed author estimates.

## Alternative interpretation and limits

A separately constructed noncentral or bias-adjusted interval can, in principle, exclude its reported point estimator. No such alternative NNT construction is specified in the inspected supplied methods. Therefore this note does not assert a universal theorem that every conceivable confidence interval must contain every point estimator. Under the supplied reciprocal-risk-difference framing, however, the displayed tuple remains unreconciled. A limit transcription, a result alignment issue, or a different interval procedure are possible explanations, not observations established by the source. Neither **18**, **38**, nor **63** is replaced or assigned an intended value.

Direct observation: the source prints 63 (18–38), with the same-row proportions supporting a point near 63. Inference: the uncertainty interval may have been produced or displayed differently from the point; its mechanism cannot be identified from the inspected material.

## Classification and evidence state

- Compared content roles: **REPORT / REPORT**; both point and interval are result entries in the same main-article table.
- Primary relationship: **S_W**. All relationships: **S_W**. No plan comparison is needed; corroborating methods do not add another relationship.
- Review domain: **statistical_results**, because the issue concerns an estimate and its interval.
- Classification correction: none.
- Evidence state: **reproduced**. Determining fact: visual confirmation of the printed 63 (18–38), whose point remains separated from the upper endpoint after half-unit precision allowances, and whose reciprocal-risk-difference explanation is not supplied by an alternative method.
- Status: **Pending Human Adjudication**.
- Exact remaining human question: What are the intended adjusted NNT point and 95% interval for the 12-month pain-intensity Health-coach versus painTRAINER comparison, and what unrounded risk difference, uncertainty interval, and transformation generated them?

## Bounded downstream impact

The issue directly affects extraction and interpretation of this secondary comparison's NNT uncertainty, including any absolute-benefit or cost-per-additional-responder calculation relying on its limits. A point near 63 conveys substantially less additional benefit than values 18–38; treating 18–38 as a routine interval around 63 would misrepresent their relationship. The available source does not determine a replacement standard error, interval, or cost result. No evidence here establishes that the RR estimate, its interval, the primary 3-month outcome, or the paper's overall conclusions change. Statistical significance and the RR-versus-NNT null-coverage question remain separate from C009.
