# Focused C008 source recheck

Date: 2026-10-17. Runtime task ID: `/root/c008_focused_recheck`. This is a bounded follow-up, not a new workflow pass or a complete package review. Existing sources and audit artifacts were preserved. The scope document and review contract were read; scientific conclusions below derive from the inspected source pages rather than an earlier report conclusion.

## Exact scope and direct observations

Visually inspected the existing source-page images for main article PDF pages 4 and 9 (printed pages 595 and 600), plus Supplement 4 PDF pages 4, 5, 11, and 14. No new rendering or OCR was performed. All compared material is REPORT content.

Main article Table 2, PDF page 9, health coach versus painTRAINER comparison:

| Outcome | Follow-up | Adjusted RR (95% CI) | Adjusted NNT (95% CI) |
|---|---:|---|---|
| Pain severity | 6 months | 1.13 (0.98–1.30) | 24 (12–186) |
| Pain severity | 12 months | 1.07 (0.96–1.19) | 41 (17–76) |
| Pain intensity | 3 months | 1.11 (0.93–1.33) | 37 (14–57) |
| Pain intensity | 12 months | 1.05 (0.92–1.20) | 63 (18–38) |
| Pain-related interference | 6 months | 1.10 (0.96–1.27) | 26 (11–67) |
| Pain-related interference | 12 months | 1.07 (0.97–1.18) | 39 (16–79) |

Each of these six RR intervals contains 1; every corresponding printed NNT interval has two finite positive endpoints. These printed readings are confirmed. The 6-month pain-intensity row, RR 1.18 (1.00–1.40), NNT 21 (11–5524), is a separate boundary case: a displayed RR limit of 1.00 does not reveal whether the unrounded limit exceeds 1. The 12-month pain-intensity point estimate 63 outside 18–38 is the separate point-containment candidate C009; it must not be treated as proof of the general C008 mechanism.

## Source sentences and interpretive limits

Main article PDF page 4, Statistical Analysis:

> “For the primary analysis comparing study groups on MCID in pain severity (binary outcome), we applied modified Poisson regression to estimate adjusted RRs and 95% CIs.”

> “Generalized estimating equations (GEE) with a working independence correlation matrix and robust sandwich standard errors were used to account for clustering at the highest level (either within-person or within-healthcoach).”

> “Adjusted number needed to treat, defined as 1 divided by the difference in adjusted percent improvement between groups, was also included to guide evaluation of the clinical meaningfulness of these binary outcome findings.”

Main article PDF page 9, Table 2 footnote b:

> “Adjusted mean percentage and adjusted RR were calculated from a modified Poisson regression model fit using generalized estimating equations for each binary outcome. Adjusted mean percentage assumes the mean of the covariate distribution to calculate randomized population average effects.”

Footnote d:

> “Number needed to treat (NNT) to gain 1 additional 30% improvement, ie, 1 over the difference in the adjusted percent with an 30% improvement or greater.”

Footnote e:

> “If CIs for the absolute risk difference contain zero the NNT confidence limits appear nonsensical and include infinity due to division by zero. In these cases, the estimate is interpreted as being consistent with an NNT from the lower limit (positive number) to infinity, and a number needed to harm from the upper limit (negative number) to negative infinity.”

Footnote c explicitly calls the P value an omnibus Wald test for any difference among all three groups. It is not a pairwise health-coach versus painTRAINER P value and does not establish that pairwise significance.

Supplement 4 PDF page 5 states that the estimation model uses GEE with Poisson errors and robust sandwich standard errors and that the joint imputation-and-analysis variance-covariance matrix is calculated as described in the cited method. This does not, by itself, specify the construction of the risk-difference confidence interval, its transformation, or whether it is obtained by inversion of the same confidence set as the RR interval. Supplement 4 pages 11 and 14 repeat the NNT definition and the interpretation when a risk-difference interval contains zero; page 11 also displays positive-to-negative NNT limits for several complete-case comparisons. These pages show that the authors recognize the interval crossing-zero case. The focused inspection did not locate enough information to reproduce the six main-table RD intervals.

## Statistical assessment

For the same two positive risks, RR = 1 and RD = 0 describe the same equality null. On the NNT scale, no difference corresponds to infinite NNT, not NNT = 0. A finite positive interval printed as an NNT-benefit interval ordinarily corresponds, under reciprocal endpoint transformation, to a positive RD interval. For example, NNT 24 (12–186) corresponds approximately to RD endpoints 1/186 = 0.005376 and 1/12 = 0.083333, or 0.5376–8.3333 percentage points. This is a diagnostic interpretation of the printed endpoints, not a reconstruction of the authors' actual unrounded interval.

Nevertheless, confidence intervals constructed separately for log(RR) and RD need not exclude their nulls on exactly the same observations in finite samples. The shared equality null does not prove that separately constructed intervals are inversions of an identical test. The six readings therefore support a candidate about divergent certainty of benefit and an unresolved confidence-interval construction; they do not establish which interval should be changed or an exact algebraic contradiction under a known common procedure.

Missing inputs are the actual adjusted-risk covariance, RD variance calculation, interval construction (including transformation or test inversion), unrounded estimates and limits, and any distinct estimand/standardization mapping used for RR versus NNT. Ask: **For these six comparisons, how were the RD/NNT 95% CIs constructed, and how should their finite positive limits be reconciled with the matched RR intervals containing 1?**

## Bounded downstream implications

- Direct NNT-based benefit statements, risk-difference extraction obtained from these intervals, and NNT-threshold or decision models may express greater certainty of incremental benefit than the matched RR intervals support. This can matter for interpretation and reuse.
- RR-based meta-analysis does not change merely because this NNT issue is identified; its reported RR inputs remain available. No replacement values or new standard errors can be derived defensibly from this focused review.
- A quantitative impact on a pooled estimate, heterogeneity, statistical significance, clinical decision, or cost-effectiveness result has not been demonstrated. It requires the downstream analysis and clarified source estimates.
- These six main-table rows concern health coach versus painTRAINER. None is the 3-month primary pain-severity contrast. They do not establish a change in either active intervention's primary comparison with usual care.

Counts: six C008 matched comparisons visually confirmed; one boundary row distinguished; one separate C009 containment observation distinguished. No new finding or stable candidate ID was created. Candidate status remains Pending Human Adjudication. Scope limitation: this bounded follow-up does not certify a complete search of every supplementary methods page or source file. An attempted direct `pdftotext` command was unavailable; it produced no extraction or scientific artifact, and visual source images supplied the evidence above.
