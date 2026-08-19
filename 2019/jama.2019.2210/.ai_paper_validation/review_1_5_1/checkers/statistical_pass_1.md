# Statistical Consistency Pass 1

## Scope and result

Independent pass-1 review of every registered inferential relationship, `S001` through `S083`, in the canonical statistical relationship inventory. Direct PDFs were the authority; current evidence maps and relationship inventories were used only as locators and transcription aids. Reviewed direct sources were DOC-001 (main article, relevant PDF pp. 1-7), DOC-002 (protocol/SAP, relevant PDF pp. 14-15, 19, 23, 30-31, and 45), and DOC-003 (results supplement PDF pp. 2-4, 6-41). DOC-004 has no inferential result.

Checks applied when the printed relationship supported them were: estimate-in-interval containment; endpoint order; HR positivity and direction relative to the null of 1; repeated-result agreement; effect-measure/model/reference/scale labels; and null-crossing versus the printed two-sided `P < .05` decision threshold. Exact P-value, test-statistic, standard-error, degrees-of-freedom, covariance, and variance-estimator reconciliation was *not* inferred where the matched source did not state that the P value and interval arose from the same inferential procedure.

- Registered relationships reviewed: 83/83.
- Displayed estimate/95% CI pairs checked for containment and endpoint order: 73/73; all pass those mechanical checks.
- Matched 95% CI/null and printed-P threshold checks: 73/73; no contradictory significance-direction pairing observed under the source's two-sided `P < .05` convention.
- `DISPLAY_ZERO_NOT_CANDIDATE` records: 0. The supplied relationships contain no `P = 0`, `p = 0.000`, or equivalent finite-precision display zero. `P = 1.00` in S063 is not a display-zero result.
- Distinct pass-1 leads: 1 (`STAT1-LEAD-001`). This is a lead only, not a stable candidate ID or adjudication.

## Pass-1 lead

### STAT1-LEAD-001 — inconsistent/ambiguous upper 25(OH)D stratum label within the protocol

- **Relationships:** S023.
- **Exact source locations:** [DOC-002 protocol/SAP PDF p. 23](<../../../joi190023supp1_prod.pdf#page=23>) and [PDF p. 31](<../../../joi190023supp1_prod.pdf#page=31>).
- **Printed comparator:** p. 23 states that subgroup analyses were stratified as `low (<20 ng/mL), middle, (>= 20 to <= 40 ng/mL) or high (40 ng/mL)`; p. 31 states `low, <20 ng/mL; middle, >=20 to <=40 ng/mL; high, >40 ng/mL`.
- **Rule and calculation:** A three-stratum cutoff specification must state whether a value exactly equal to 40 ng/mL belongs to the middle or high stratum. The p. 31 rule assigns 40 to middle and reserves high for `>40`; p. 23 supplies no inequality for high and is therefore not the same explicit label. No numeric derivation is used.
- **Why this is a lead:** The two locations provide different precision for the same named cutoff scheme, leaving the p. 23 upper-stratum boundary ambiguous relative to p. 31. The source itself is needed to determine whether p. 23 is shorthand or a labeling omission. No observed effect estimate is asserted to be wrong.
- **Human question:** Was `high (40 ng/mL)` intended as `>40 ng/mL`, consistent with the final SAP and main article, or did it denote a different inclusion rule?

## Relationship-level records

| S ID | Direct source location(s) | Pass-1 checks and result | Status |
|---|---|---|---|
| S001 | DOC-001 pp. 1, 4, 6 (Figure 2A) | HR 0.76 lies in 0.50-1.14; endpoints ordered; CI crosses 1 and P=.18; abstract, narrative, and figure agree. Cox HR label/direction retained. Exact P/CI identity not calculated because the source does not state the P-value test/variance rule. | PASS_1_COMPLETE |
| S002 | DOC-001 pp. 1, 4, 6 (Figure 2B) | HR 0.95 lies in 0.57-1.57; ordered CI crosses 1 and P=.83; repeated locations agree. Cox HR label/direction retained; exact P/CI identity not supplied. | PASS_1_COMPLETE |
| S003 | DOC-001 pp. 1, 4-5, 7 (Figure 3A) | HR 0.46 lies in 0.24-0.86; ordered CI excludes 1 and P=.02; narrative/figure agree. Middle baseline stratum and Cox-HR label match the source. Exact P/CI identity not supplied. | PASS_1_COMPLETE |
| S004 | DOC-001 pp. 4-5, 7 (Figure 3B) | HR 1.15 lies in 0.65-2.05; ordered CI crosses 1 and P=.63; locations agree. Direction is distinct from S003 because the baseline stratum differs. Exact P/CI identity not supplied. | PASS_1_COMPLETE |
| S005 | DOC-001 pp. 1, 5, 7 (Figure 3) | Interaction P=.04 is separately labelled from within-stratum HR P values. Main methods define a Cox interaction comparison of low versus middle strata; no interval/statistic is printed for this interaction. | PASS_1_COMPLETE |
| S006 | DOC-001 pp. 5, 7 (Figure 3C) | HR 0.60 lies in 0.28-1.30; ordered CI crosses 1 and P=.20; locations agree. Cox-HR outcome/direction labels match. Exact P/CI identity not supplied. | PASS_1_COMPLETE |
| S007 | DOC-001 pp. 5, 7 (Figure 3D) | HR 1.36 lies in 0.66-2.81; ordered CI crosses 1 and P=.41; locations agree. Cox-HR outcome/direction labels match. Exact P/CI identity not supplied. | PASS_1_COMPLETE |
| S008 | DOC-001 pp. 5, 7 (Figure 3) | Interaction P=.13 is distinct from within-stratum P values and follows the explicitly described low-versus-middle Cox interaction. No interval/statistic is printed. | PASS_1_COMPLETE |
| S009 | DOC-001 pp. 6-7 (Figure 2C/Table 2) | Subdistribution HR 0.75 lies in 0.48-1.17; ordered CI crosses 1 and P=.21; figure/table agree. It is explicitly a competing-risk subdistribution HR, not the ordinary Cox HR in S001. Exact P/CI identity not supplied. | PASS_1_COMPLETE |
| S010 | DOC-001 pp. 6-7 (Table 2) | Low HR 1.18 lies in 0.64-2.19 with P=.59; middle HR 0.44 lies in 0.21-0.89 with P=.02; both endpoint orders and null/P threshold pairings are coherent. P=.04 is explicitly interaction P. Subdistribution-HR label retained. | PASS_1_COMPLETE |
| S011 | DOC-001 p. 7 (Table 2) | Total/low/middle HRs 1.09/1.45/0.78 each lie in their ordered CIs, all cross 1, and P=.80/.38/.63 is non-significant. The table footnote defines HR>1 as lower outcome probability with vitamin D; no direction conflict observed. Interaction P=.35 is separately labelled. | PASS_1_COMPLETE |
| S012 | DOC-001 p. 7 (Table 2) | Total/low/middle HRs 0.70/1.11/0.39 each lie in their ordered CIs, all cross 1, and P=.44/.89/.15 is non-significant. Direction footnote and separately printed interaction P=.27 are retained. | PASS_1_COMPLETE |
| S013 | DOC-001 p. 6 | Age-adjusted HRs 0.66 (0.43-0.99), P=.048 and 0.81 (0.48-1.36), P=.42 pass containment/order and null/P threshold checks. They are adjustment-specific results, not duplicates of S001/S002. Stage-I-adjusted claims have no printed estimate/interval/statistic. | PASS_1_COMPLETE |
| S014 | DOC-001 p. 6 | Within-group Wilcoxon and between-group Mann-Whitney labels are supplied; printed P values are compatible with the stated `P < .05` convention. No matched test statistics, paired sample sizes, sidedness per P, or distributional inputs are supplied for exact reconstruction. `<.001` is not a display-zero notation. | PASS_1_COMPLETE |
| S015 | DOC-001 pp. 3, 6 | Qualitative claims (PH test, 50 imputations, and subgroup interaction summaries) have no printed statistic, SE, interval, or matched numeric comparator. No model detail is inferred; no numerical contradiction is supplied. | PASS_1_COMPLETE |
| S016 | DOC-002 p. 30 | Planned log-rank/Freedman output is internally arithmetically coherent: N1=160 plus N2=240 equals N=400, matching the 3:2 allocation and p1=.4000. Alpha is explicitly two-sided. The displayed h ratio is accepted as the stated software output; no unreported calculation convention is inferred. | PASS_1_COMPLETE |
| S017 | DOC-002 p. 31 | Planned annual interim analyses after 200 entries and Peto P<.001 boundary are clearly labelled as planned. The source does not give occurrence dates or a result for a specific interim test, so no observed-result comparison is made. | PASS_1_COMPLETE |
| S018 | DOC-002 pp. 19, 31 | Planned ITT Kaplan-Meier/Cox HR with 95% CI label matches the main article's reported RFS/OS Cox-HR framework; a plan does not by itself require identical post hoc analyses. | PASS_1_COMPLETE |
| S019 | DOC-002 pp. 14, 31 | Wilcoxon signed-rank is a planned within-person 25(OH)D test and matches the main article's named within-group test. No test statistic, sample size, or pairing detail for exact recheck is supplied. | PASS_1_COMPLETE |
| S020 | DOC-002 pp. 14, 31 | Planned test types are conditional on variable type/distribution. No matched reported baseline comparison is assigned here, so no test-result reconciliation is available or inferred. | PASS_1_COMPLETE |
| S021 | DOC-002 pp. 14, 31 | The protocol plans RR for relapse/safety, whereas the main article reports a separately identified post hoc competing-risk subdistribution HR for relapse. The source does not print the same matched result under both measures; this is not an effect-measure contradiction. | PASS_1_COMPLETE |
| S022 | DOC-002 pp. 14, 31 | Two-sided P-value and P<.05 conventions are explicitly supplied. They support null/P threshold screening only, not inference of the individual P-value test, df, variance estimator, or CI construction. | PASS_1_COMPLETE |
| S023 | DOC-002 pp. 23, 27, 31 | p. 31 gives `<20`, `>=20 to <=40`, and `>40`; p. 23 gives high as `(40 ng/mL)` without an inequality. This is recorded in STAT1-LEAD-001. Interaction multiplicative-variable/no-multiplicity labels otherwise match p. 31. | PASS_1_COMPLETE |
| S024 | DOC-002 pp. 14-15, 30-31, 45 | Differences in planned fields are explicitly versioned and the change summary states the target was fixed before trial start. No unlabelled duplicate or observed-result contradiction is present. | PASS_1_COMPLETE |
| S025 | DOC-002 pp. 3, 6, 18, 21-22 | The cited external FokI log-rank P=.005 is explicitly background, not an AMATERASU trial result. No inappropriate main-result match is made. | PASS_1_COMPLETE |
| S026 | DOC-002 p. 22 | The cited external genetic-association P<.0001 is background only. No AMATERASU result, model, or comparator is supplied. | PASS_1_COMPLETE |
| S027 | DOC-003 p. 4 (eTable 1) | HR 0.62 lies in 0.37-1.02; endpoints ordered; CI crosses 1 and P=.06. Unadjusted HR, reference `<20`, and outcome labels are explicit. Exact P/CI identity not supplied. | PASS_1_COMPLETE |
| S028 | DOC-003 p. 4 (eTable 1) | AHR 0.61 lies in 0.37-1.01; endpoints ordered; CI crosses 1 and P=.05. AHR is separately footnoted as adjusted with vitamin D supplementation; no exact test/CI construction is printed. | PASS_1_COMPLETE |
| S029 | DOC-003 p. 4 (eTable 1) | HR 0.66 lies in 0.35-1.24; ordered CI crosses 1 and P=.20. Unadjusted model/reference/outcome label retained. | PASS_1_COMPLETE |
| S030 | DOC-003 p. 4 (eTable 1) | AHR 0.64 lies in 0.34-1.20; ordered CI crosses 1 and P=.16. AHR adjustment footnote is retained; exact P/CI identity not supplied. | PASS_1_COMPLETE |
| S031 | DOC-003 p. 4 (eTable 1) | HR 0.47 lies in 0.27-0.84; ordered CI excludes 1 and P=.01. Unadjusted model/reference/outcome label retained. | PASS_1_COMPLETE |
| S032 | DOC-003 p. 4 (eTable 1) | AHR 0.44 lies in 0.24-0.82; ordered CI excludes 1 and P=.009. AHR adjustment footnote retained. | PASS_1_COMPLETE |
| S033 | DOC-003 p. 4 (eTable 1) | HR 0.39 lies in 0.18-0.84; ordered CI excludes 1 and P=.02. It exactly matches the separately repeated S048 annotation. | PASS_1_COMPLETE |
| S034 | DOC-003 p. 4 (eTable 1) | AHR 0.33 lies in 0.15-0.74; ordered CI excludes 1 and P=.007. AHR adjustment footnote retained. | PASS_1_COMPLETE |
| S035 | DOC-003 p. 4 (eTable 1) | HR 0.29 lies in 0.11-0.74; ordered CI excludes 1 and P=.01. It exactly matches the separately repeated S047 annotation. | PASS_1_COMPLETE |
| S036 | DOC-003 p. 4 (eTable 1) | AHR 0.26 lies in 0.10-0.71; ordered CI excludes 1 and P=.008. AHR adjustment footnote retained. | PASS_1_COMPLETE |
| S037 | DOC-003 p. 4 (eTable 1) | HR 0.44 lies in 0.17-1.16; ordered CI crosses 1 and P=.10. Unadjusted model/reference/outcome label retained. | PASS_1_COMPLETE |
| S038 | DOC-003 p. 4 (eTable 1) | AHR 0.34 lies in 0.12-0.96; ordered CI excludes 1 and P=.04. AHR adjustment footnote retained. | PASS_1_COMPLETE |
| S039 | DOC-003 p. 4 (eTable 1) | HR 0.44 lies in 0.21-0.96; ordered CI excludes 1 and P=.04. Unadjusted model/reference/outcome label retained. | PASS_1_COMPLETE |
| S040 | DOC-003 p. 4 (eTable 1) | AHR 0.40 lies in 0.18-0.92; ordered CI excludes 1 and P=.03. AHR adjustment footnote retained. | PASS_1_COMPLETE |
| S041 | DOC-003 p. 4 (eTable 1) | HR 0.55 lies in 0.24-1.29; ordered CI crosses 1 and P=.17. Unadjusted model/reference/outcome label retained. | PASS_1_COMPLETE |
| S042 | DOC-003 p. 4 (eTable 1) | AHR 0.43 lies in 0.17-1.08; ordered CI crosses 1 and P=.07. AHR adjustment footnote retained. | PASS_1_COMPLETE |
| S043 | DOC-003 p. 6 (eTable 2) | HR 1.15 lies in 0.65-2.05; ordered CI crosses 1 and P=.63. Multiple-imputation/baseline-stratum label matches main S004. No additional adjustment label is printed. | PASS_1_COMPLETE |
| S044 | DOC-003 p. 6 (eTable 2) | HR 0.46 lies in 0.24-0.86; ordered CI excludes 1 and P=.02. Multiple-imputation/baseline-stratum label matches main S003. | PASS_1_COMPLETE |
| S045 | DOC-003 p. 6 (eTable 2) | HR 1.36 lies in 0.66-2.81; ordered CI crosses 1 and P=.41. Multiple-imputation/baseline-stratum label matches main S007. | PASS_1_COMPLETE |
| S046 | DOC-003 p. 6 (eTable 2) | HR 0.60 lies in 0.28-1.30; ordered CI crosses 1 and P=.20. Multiple-imputation/baseline-stratum label matches main S006. | PASS_1_COMPLETE |
| S047 | DOC-003 p. 2 (eFigure 1A) | HR 0.29 lies in 0.11-0.74; ordered CI excludes 1 and P=.01. The values exactly repeat S035. Figure title shorthand `~20` is not proven discordant with eTable 1 reference `<20`; no boundary definition for the tilde is supplied. | PASS_1_COMPLETE |
| S048 | DOC-003 p. 3 (eFigure 1B) | HR 0.39 lies in 0.18-0.84; ordered CI excludes 1 and P=.02. The values exactly repeat S033. The `~20` title shorthand is not treated as an independent contradictory stratum definition. | PASS_1_COMPLETE |
| S049 | DOC-003 p. 7 (eFigure 3A) | HR 0.65 lies in 0.34-1.26; ordered CI crosses 1 and P=.20; interaction P=.65 is distinct. Figure lacks model, adjustment, P-test, CI-construction, and HR-reference orientation details. | PASS_1_COMPLETE |
| S050 | DOC-003 p. 8 (eFigure 3B) | HR 0.77 lies in 0.42-1.43; ordered CI crosses 1 and P=.41; interaction P=.90 is distinct. Missing figure-level model/test/reference details are not inferred. | PASS_1_COMPLETE |
| S051 | DOC-003 p. 9 (eFigure 3C) | HR 0.97 lies in 0.32-2.88; ordered CI crosses 1 and P=.95; interaction P=.67 is distinct. Missing figure-level model/test/reference details are not inferred. | PASS_1_COMPLETE |
| S052 | DOC-003 p. 10 (eFigure 3D) | HR 0.44 lies in 0.03-7.16; endpoints ordered, CI crosses 1, and P=.56; interaction P=.66 is distinct. Missing figure-level model/test/reference details are not inferred. | PASS_1_COMPLETE |
| S053 | DOC-003 p. 11 (eFigure 3E) | HR 0.60 lies in 0.24-1.48; ordered CI crosses 1 and P=.27; interaction P=.50 is distinct. Missing figure-level model/test/reference details are not inferred. | PASS_1_COMPLETE |
| S054 | DOC-003 p. 12 (eFigure 3F) | HR 0.86 lies in 0.52-1.41; ordered CI crosses 1 and P=.55; interaction P=.38 is distinct. Missing figure-level model/test/reference details are not inferred. | PASS_1_COMPLETE |
| S055 | DOC-003 p. 13 (eFigure 3G) | HR 0.69 lies in 0.34-1.38; ordered CI crosses 1 and P=.29; interaction P=.64 is distinct. Missing figure-level model/test/reference details are not inferred. | PASS_1_COMPLETE |
| S056 | DOC-003 p. 14 (eFigure 3H) | HR 0.72 lies in 0.39-1.32; ordered CI crosses 1 and P=.28; interaction P=.63 is distinct. Missing figure-level model/test/reference details are not inferred. | PASS_1_COMPLETE |
| S057 | DOC-003 p. 15 (eFigure 3I) | HR 1.82 lies in 0.48-6.88; ordered CI crosses 1 and P=.38; interaction P=.19 is distinct. Missing figure-level model/test/reference details are not inferred. | PASS_1_COMPLETE |
| S058 | DOC-003 p. 16 (eFigure 3J) | HR 1.00 lies in 0.49-2.05; ordered CI crosses 1 and P=.99; interaction P=.35 is distinct. Missing figure-level model/test/reference details are not inferred. | PASS_1_COMPLETE |
| S059 | DOC-003 p. 17 (eFigure 3K) | HR 0.70 lies in 0.38-1.27; ordered CI crosses 1 and P=.24; interaction P=.63 is distinct. Missing figure-level model/test/reference details are not inferred. | PASS_1_COMPLETE |
| S060 | DOC-003 p. 18 (eFigure 3L) | HR 0.53 lies in 0.15-1.84; ordered CI crosses 1 and P=.32; interaction P=.49 is distinct. Missing figure-level model/test/reference details are not inferred. | PASS_1_COMPLETE |
| S061 | DOC-003 p. 19 (eFigure 3M) | HR 0.87 lies in 0.52-1.46; ordered CI crosses 1 and P=.60; interaction P=.35 is distinct. Missing figure-level model/test/reference details are not inferred. | PASS_1_COMPLETE |
| S062 | DOC-003 p. 20 (eFigure 3N) | HR 0.49 lies in 0.22-1.10; ordered CI crosses 1 and P=.08; interaction P=.20 is distinct. Missing figure-level model/test/reference details are not inferred. | PASS_1_COMPLETE |
| S063 | DOC-003 p. 21 (eFigure 3O) | HR and CI are printed as dashes, with P=1.00 and interaction P=dash. No point/interval or P/test compatibility can be reconstructed because estimability, event pattern, model, and test definition are absent. `P=1.00` is not a display-zero issue. | PASS_1_COMPLETE |
| S064 | DOC-003 p. 22 (eFigure 3P) | HR 0.71 lies in 0.42-1.22; ordered CI crosses 1 and P=.22; interaction P=.63 is distinct. Figure-level model/adjustment/P-test/CI/reference definitions are absent. | PASS_1_COMPLETE |
| S065 | DOC-003 p. 23 (eFigure 3Q) | HR 1.00 lies in 0.44-2.24; ordered CI crosses 1 and P=.99; interaction P=.49 is distinct. Figure-level model/adjustment/P-test/CI/reference definitions are absent. | PASS_1_COMPLETE |
| S066 | DOC-003 p. 24 (eFigure 3R) | HR 0.65 lies in 0.14-2.92; ordered CI crosses 1 and P=.57; interaction P=.91 is distinct. Figure-level model/adjustment/P-test/CI/reference definitions are absent. | PASS_1_COMPLETE |
| S067 | DOC-003 p. 25 (eFigure 3S) | HR 0.60 lies in 0.34-1.05; ordered CI crosses 1 and P=.07; interaction P=.16 is distinct. Figure-level model/adjustment/P-test/CI/reference definitions are absent. | PASS_1_COMPLETE |
| S068 | DOC-003 p. 26 (eFigure 3T) | HR 1.19 lies in 0.55-2.60; ordered CI crosses 1 and P=.66; interaction P=.16 is distinct. Figure-level model/adjustment/P-test/CI/reference definitions are absent. | PASS_1_COMPLETE |
| S069 | DOC-003 p. 27 (eFigure 3U) | HR 0.80 lies in 0.20-3.20; ordered CI crosses 1 and P=.75; interaction P=1.00 is distinct. Figure-level model/adjustment/P-test/CI/reference definitions are absent. | PASS_1_COMPLETE |
| S070 | DOC-003 p. 28 (eFigure 4A) | HR 0.59 lies in 0.37-0.97; ordered CI excludes 1 and P=.04; interaction P=.13 is distinct. Figure-level model/adjustment/P-test/CI/reference definitions are absent. | PASS_1_COMPLETE |
| S071 | DOC-003 p. 29 (eFigure 4B) | HR 1.18 lies in 0.56-2.51; ordered CI crosses 1 and P=.66; interaction P=.13 is distinct. Figure-level model/adjustment/P-test/CI/reference definitions are absent. | PASS_1_COMPLETE |
| S072 | DOC-003 p. 30 (eFigure 5A) | HR 0.86 lies in 0.44-1.68; ordered CI crosses 1 and P=.65; interaction P=.48 is distinct. Figure-level model/adjustment/P-test/CI/reference definitions are absent. | PASS_1_COMPLETE |
| S073 | DOC-003 p. 31 (eFigure 5B) | HR 0.63 lies in 0.37-1.05; ordered CI crosses 1 and P=.07; interaction P=.48 is distinct. Figure-level model/adjustment/P-test/CI/reference definitions are absent. | PASS_1_COMPLETE |
| S074 | DOC-003 p. 32 (eFigure 6A) | HR 0.75 lies in 0.49-1.16; ordered CI crosses 1 and P=.20; interaction P=.87 is distinct. Figure-level model/adjustment/P-test/CI/reference definitions are absent. | PASS_1_COMPLETE |
| S075 | DOC-003 p. 33 (eFigure 6B) | HR 0.88 lies in 0.22-3.55; ordered CI crosses 1 and P=.86; interaction P=.87 is distinct. Figure-level model/adjustment/P-test/CI/reference definitions are absent. | PASS_1_COMPLETE |
| S076 | DOC-003 p. 34 (eFigure 7A) | HR 1.01 lies in 0.42-2.44; ordered CI crosses 1 and P=.99; interaction P=.65 is distinct. Figure-level model/adjustment/P-test/CI/reference definitions are absent. | PASS_1_COMPLETE |
| S077 | DOC-003 p. 35 (eFigure 7B) | HR 0.84 lies in 0.40-1.76; ordered CI crosses 1 and P=.64; interaction P=.88 is distinct. Figure-level model/adjustment/P-test/CI/reference definitions are absent. | PASS_1_COMPLETE |
| S078 | DOC-003 p. 36 (eFigure 7C) | HR 0.69 lies in 0.39-1.24; ordered CI crosses 1 and P=.22; interaction P=.66 is distinct. Figure-level model/adjustment/P-test/CI/reference definitions are absent. | PASS_1_COMPLETE |
| S079 | DOC-003 p. 37 (eFigure 8A) | HR 0.39 lies in 0.14-1.13; ordered CI crosses 1 and P=.08; interaction P=.14 is distinct. Figure-level model/adjustment/P-test/CI/reference definitions are absent. | PASS_1_COMPLETE |
| S080 | DOC-003 p. 38 (eFigure 8B) | HR 1.20 lies in 0.51-2.80; ordered CI crosses 1 and P=.68; interaction P=.23 is distinct. Figure-level model/adjustment/P-test/CI/reference definitions are absent. | PASS_1_COMPLETE |
| S081 | DOC-003 p. 39 (eFigure 8C) | HR 0.86 lies in 0.51-1.46; ordered CI crosses 1 and P=.58; interaction P=.62 is distinct. Figure-level model/adjustment/P-test/CI/reference definitions are absent. | PASS_1_COMPLETE |
| S082 | DOC-003 p. 40 (eFigure 9A) | HR 0.70 lies in 0.43-1.13; ordered CI crosses 1 and P=.14; interaction P=.47 is distinct. Figure-level model/adjustment/P-test/CI/reference definitions are absent. | PASS_1_COMPLETE |
| S083 | DOC-003 p. 41 (eFigure 9B) | HR 1.18 lies in 0.54-2.60; ordered CI crosses 1 and P=.68; interaction P=.47 is distinct. Figure-level model/adjustment/P-test/CI/reference definitions are absent. | PASS_1_COMPLETE |

## Cross-location and definition notes

- S033/S048 and S035/S047 are exact, intended repeated presentations of the same estimate, CI, and P value. They were not treated as independent estimates or a duplicate-value inconsistency.
- S003/S004/S006/S007 and S043-S046 are matched baseline-25(OH)D main/supplement results; the supplement explicitly identifies multiple imputation, so it is not a competing duplicate analysis.
- S009/S010 are competing-risk subdistribution HRs and must not be compared as if they were the ordinary Cox HRs for S001/S003/S004.
- S049-S083 print an HR, 95% CI, P, and P interaction, but their figure pages omit the individual model, covariate-adjustment set, test, degrees of freedom, P-value sidedness, confidence-interval construction, and HR reference orientation. The protocol's general two-sided convention does not supply enough matched definition to calculate an exact P from an interval; no such approximation was used.
- S014 has named nonparametric test families but no per-test statistic, exact paired/cross-group analysis population, or distributional inputs. S015 and S063 are unreconstructable for the stated missing definitions.
- No candidate was produced merely for a P-value display convention. There are no display-zero P values in the assigned S inventory.

## Pass-1 limitations

This pass does not infer sidedness, degrees of freedom, covariance, denominator, variance estimator, multiple-comparison adjustment, model formula, or estimand mapping from convention alone. It does not recalculate an exact tail probability from rounded estimates or intervals. All statements remain pass-1 quality-control observations pending the coordinator's duplicate merge, candidate-ledger construction, and direct-source mechanical recheck.
