# Protocol Statistical Relationship Inventory

All identifiers are provisional `PS` keys for coordinator reconciliation. All are planned statistical relationships except the explicitly labelled background citations.

| Provisional key | Planned or observed | Statistical definition or relationship | Exact source location | Main/results matching key |
|---|---|---|---|---|
| PS001 | Planned | Sample size uses a two-sample survivor-function log-rank test, Freedman method: null H0 S1(t)=S2(t); alpha=0.0500 two-sided; power=0.8000; survivor functions s1=0.6200 and s2=0.7500; displayed h ratio=0.6018; p1=0.4000; withdrawal=1.00%; E=120; N=400; N1=160; N2=240. Stata command: `st power log rank 0.62 0.75, n ratio(1.5) wd prob (0.01)`. | DOC-002 PDF p. 30 | Design-stage RFS power calculation; do not equate with observed HR, event count, or study N. |
| PS002 | Planned | Annual interim analyses are planned after entry of 200 patients; Peto stopping-boundary significance threshold is P<0.001. The final SAP does not state that an interim analysis occurred. | DOC-002 PDF p. 31 | Interim analysis; threshold and timing only. |
| PS003 | Planned | RFS and OS: intent-to-treat Kaplan-Meier survival curves and Cox proportional-hazards model; effect measure HR with 95% CI. | DOC-002 PDF pp. 19, 31 | Endpoint=RFS or OS; population=ITT; model=Cox; effect=HR; CI=95%. |
| PS004 | Planned | Changes in 25(OH)D levels use Wilcoxon signed-rank tests. | DOC-002 PDF p. 31; initial plan p. 14 | Biomarker=25(OH)D; within-person/change analysis; test=Wilcoxon signed-rank. |
| PS005 | Planned | Baseline/patient-characteristic comparisons: Student t test for normally distributed continuous variables, Mann-Whitney test for non-normal continuous variables, and chi-square tests for dichotomous outcomes. | DOC-002 PDF p. 31; initial plan p. 14 | Baseline characteristics; contrast=Vitamin D vs placebo; test conditional on variable distribution/type. |
| PS006 | Planned | Relapse and safety outcomes are to be evaluated using risk ratio (RR). | DOC-002 PDF p. 31; initial plan p. 14 | Outcome=relapse/safety; effect=RR; distinguish from HR for time-to-event endpoints. |
| PS007 | Planned | All reported P values are two-sided; P<0.05 is the stated statistical-significance convention. | DOC-002 PDF p. 31; initial plan p. 14 | General P-value convention; interpret only with matched model/endpoint. |
| PS008 | Planned | Subgroup interaction: P for interaction is computed using multiplicative variables; results are not corrected for multiple comparisons. Page 31 defines 25(OH)D strata as <20, >=20 to <=40, and >40 ng/mL; p. 23 prints the high stratum as `high (40 ng/mL)` without an inequality. VDR strata are FokI/BsmI/CDX2/TaqI/ApaI and DBP strata are DBP1/DBP2. | DOC-002 PDF p. 31; pp. 23, 27 | Subgroup/interactions; model interaction P; no multiplicity adjustment; retain both printed cutoff labels. |
| PS009 | Planned/version history | Initial SAP (2008-12-25) has blank sample-size and interim-analysis sections, while final SAP specifies the 400-person calculation and interim plan. Change summary states target N=400 was fixed before trial start (2009-10-08). | DOC-002 PDF pp. 14-15, 30-31, 45 | Protocol-version comparator; not a conflicting observed result. |
| PS010 | Background only, not trial result | External background citation reports FokI genotype median-survival comparison with log-rank P=0.005. This is not a study analysis plan or observed AMATERASU result. | DOC-002 PDF pp. 3, 6, 18, 21-22 | No main-paper match; background-only statistical citation. |
| PS011 | Background only, not trial result | External COPD genetic association: rs7041 homozygous at-risk T-allele carriers have 25% lower 25(OH)D; cited P<0.0001. This is not an AMATERASU result. | DOC-002 PDF p. 22 | No main-paper match; background-only statistical citation. |

## Statistical no-applicable units and limitations

- DOC-004 PDF p. 1 reports availability conditions only; it has no observed or planned statistical result.
- The source supplies no observed treatment effect, confidence interval, P value, subgroup result, sensitivity result, model coefficient, standard error, or analyzed denominator. Consequently these records are comparison keys and definitions for matching elsewhere, not inferential consistency conclusions.
- The protocol does not specify covariate adjustment, proportional-hazards diagnostics, missing-data method, or the exact interaction model parameterization beyond multiplicative variables. Those omissions must not be filled by inference.
