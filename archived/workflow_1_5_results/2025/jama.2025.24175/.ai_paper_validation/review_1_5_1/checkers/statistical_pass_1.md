# Statistical Consistency Review — Pass 1

**Pass:** 1 (independent statistical review)  
**Scope:** S001-S051, with cross-lane implications checked against the current N001-N125 mapping.  
**Source authority:** Direct supplied PDFs. Current 1.5.1 mapping artifacts were locators; the result-bearing main-paper Table 2 and Supplement 1 pp. 48, 51-52 and Supplement 2 pp. 22 and 51-53 were directly reviewed/render-confirmed. No legacy candidate, checker, or report artifact was used.  
**Completion:** Every assigned S ID below is marked `PASS_1_COMPLETE`. Six distinct candidate proposals are reported for coordinator registration; all are **Pending Human Adjudication**.

## Method and interpretive limits

For each relationship I checked printed point-estimate containment, interval ordering, sign/direction, effect-measure/contrast labels, matched repetitions, and compatible test/P-value relations. Exact recomputation was limited to cases where the source printed a compatible test and all needed inputs. Log-scale interval-to-P diagnostics are identified as diagnostics, not replacements for the reported analysis. I did not infer sidedness, covariance, variance estimator, adjustment, or an unprinted estimand.

`P<.001`, `P<.0001`, and similar threshold displays were retained as finite-precision notation. No display-zero P-value candidate was emitted.

## Complete relationship records

| Stable ID | Direct evidence and check | Calculation / compatibility assessment | Status |
|---|---|---|---|
| S001 | DOC-001 PDF p. 6 Table 2: OR 2.48 (1.42-4.32), P=.002; abstract p. 1 gives matched counts/difference/P. | 2.48 is inside ordered CI. Table uses Fisher/Mantel-Haenszel while eTable logistic output is separately mapped; no cross-model equality assumed. | PASS_1_COMPLETE — no proposal. |
| S002 | DOC-001 p. 6: adjusted logistic OR 2.49 (1.42-4.36), covariates named. | Estimate lies within ordered CI; source does not print the model P value/SE. | PASS_1_COMPLETE — no proposal. |
| S003 | DOC-001 p. 6 Table 2: 28-day OR 0.78 (0.49-1.26), P=.34; p. 7 repeats counts/P. | CI crosses 1 and direction agrees with 57/131 versus 72/145. | PASS_1_COMPLETE — no proposal. |
| S004 | DOC-001 p. 6: 90-day OR 1.05 (0.63-1.75), P=.90. | Estimate lies within ordered CI and is close to null; no incompatible supplied comparator. | PASS_1_COMPLETE — no proposal. |
| S005 | DOC-001 p. 6 Table 2 prints 52/131 versus 34/145, OR 2.15 (1.28-3.61), P=.004; p. 7 narrative prints 51/131 versus 34/145, P=.004. | Table counts yield crude OR `(52×111)/(79×34)=2.15` (rounded), matching the table estimate; 51/131 is a non-rounding cross-location numerator conflict. | PASS_1_COMPLETE — candidate proposal P1-01. |
| S006 | DOC-001 p. 6 Table 2: OR 3.76 (1.72-8.22), P=.001; p. 7 narrative: same counts and `P<.001`. | Estimate is contained; a finite P in the interval 0.0005-0.000999 can display as both `.001` (three-decimal rounding) and `<.001`. | PASS_1_COMPLETE — no proposal. |
| S007 | DOC-001 p. 6 Table 2/footnote c: worse infection-disposition OR 0.59 (0.38-0.91), P=.02. | Estimate is contained; OR direction agrees with the stated precision-versus-placebo worse-outcome contrast. Ordinal-model details are stated but SE/test statistic is absent. | PASS_1_COMPLETE — no proposal. |
| S008 | DOC-001 p. 7: MALS 12/25 vs 4/23, P=.04; SII 34/106 vs 22/122, P=.02. | Matched eTable values use additional precision (.034 and .020); the apparent difference is compatible with display precision and the reported Fisher framework. | PASS_1_COMPLETE — no proposal. |
| S009 | DOC-001 p. 6 names Fisher, Mantel-Haenszel OR/CI, Cox HR/CI, and ordinal regression frameworks. | Definitions support the distinct measures; no estimate/interval pair is conflated. | PASS_1_COMPLETE — no proposal. |
| S010 | DOC-001 p. 8 narrative names significant CCI/SOFA interactions for primary and 28-day outcomes and no 90-day interaction. | Direct eFigures 7-9 provide the matched interaction displays; the 28-day B-panel content is evaluated at S049. | PASS_1_COMPLETE — candidate implication carried to P1-05 only. |
| S011 | DOC-001 p. 8 reports significant adverse-event differences but prints no statistic/effect/P value. | No compatible inferential quantity is supplied to reconstruct. | PASS_1_COMPLETE — no proposal; missing exact event/test definitions. |
| S012 | DOC-001 p. 5 sample-size plan: 40% vs 20%, 5% significance, 90% power, 117/group, 15% dropout, 280 planned. | Design parameters are internally stated; no actual-test compatibility rule is supplied here. | PASS_1_COMPLETE — no proposal. |
| S013 | DOC-002 p. 24-26: protocol v7 SOFA mean-difference plan, two-sided t test, alpha .05, 80% power, SD 3.210, 112/arm. | Planned mean endpoint differs from later observed binary endpoint/model wording, but source/version/estimand continuity is not established. | PASS_1_COMPLETE — no proposal; version/endpoint-change definition absent. |
| S014 | DOC-002 p. 27: planned Welch t test for SOFA mean differences. | Planned test only; no observed estimate or compatible output at this location. | PASS_1_COMPLETE — no proposal. |
| S015 | DOC-002 p. 27: planned mortality Fisher/log-rank and OR/CI analyses. | Planned analysis definitions; later report distinguishes binary OR and survival models. | PASS_1_COMPLETE — no proposal. |
| S016 | DOC-002 p. 27: planned reversal/infection Fisher and OR/CI analyses. | Planned framework is not itself an observed inferential result. | PASS_1_COMPLETE — no proposal. |
| S017 | DOC-002 p. 27: biomarker analysis has no effect size, multiplicity rule, model, or threshold. | Missing definitions precisely preclude compatibility checking. | PASS_1_COMPLETE — no proposal. |
| S018 | DOC-002 p. 47 Table 1: ANOVA continuous and Pearson chi-square categorical tests. | Test labels match displayed variable types; individual values were assessed under S022/S023. | PASS_1_COMPLETE — no proposal. |
| S019 | DOC-002 p. 48 Table 2: APACHE II 18.2±8.7 (n=21) vs 30.5±9.4 (n=15), Student t-test `P=.376`. | Direct two-sample diagnostic: pooled SD ≈9.00, SE≈3.04, `t≈4.05` (34 df), two-sided `P≈.0003`; Welch gives `t≈3.99`, `P≈.0004`. Neither is compatible with `.376` at printed precision. | PASS_1_COMPLETE — candidate proposal P1-02. |
| S020 | DOC-002 pp. 39-40: planned descriptive/t-test/Mann-Whitney/ROC/Cox framework. | A plan, rather than a single observed output; no unambiguous same-version comparator. | PASS_1_COMPLETE — no proposal. |
| S021 | DOC-002 pp. 40-41 and p. 52: classification/mortality Cox outputs including HRs/CIs. | Direct p. 52 printed Cox rows have ordered CIs containing HRs. Exact model covariate/variance/test details are not fully specified for P-value diagnostics. | PASS_1_COMPLETE — no proposal. |
| S022 | DOC-002 p. 47 Table 1: APACHE II/SOFA `P<.0001`. | Threshold notation is not `P=0` and is not an independent inconsistency. | PASS_1_COMPLETE — no proposal; finite-precision threshold retained. |
| S023 | DOC-002 p. 51 Figure 2C: `<5000` 69 deaths/34 survival (103), `≥5000` 37/52 (89), printed `RR_death ... 2.82 (1.58-5.14), P<.0001`. Direct p. 52 Figure 3 prints HR 2.82 (1.58-5.14) for immunoparalysis. | The printed counts give risk ratio `(69/103)/(37/89)=1.61`; their odds ratio is `(69×52)/(34×37)=2.85`, compatible with 2.82. The Figure 2 value/CI exactly repeat Figure 3's HR but carry an RR label. | PASS_1_COMPLETE — candidate proposal P1-03. |
| S024 | DOC-002 p. 52 Figure 3: log-rank/Cox HR outputs; ordered CIs contain each printed HR. | P-value/CI diagnostics are not forced because Cox test form and displayed rounding are not fully specified; no independent contradiction found. | PASS_1_COMPLETE — no proposal. |
| S025 | DOC-002 p. 53 Figure 4: log-rank and within-group P values; exact bar heights not printed. | No numerical effect/interval can be inferred from bar geometry. | PASS_1_COMPLETE — no proposal. |
| S026 | DOC-002 p. 66 SAP: descriptive measure/dispersion rules. | Rules distinguish mean/SD, median/quartiles, and frequencies; no result output on this page. | PASS_1_COMPLETE — no proposal. |
| S027 | DOC-002 p. 67 SAP: raw primary responder Fisher exact with OR/95% CI. | Compatible with the main paper's raw binary-analysis labels; no claim of identity with logistic output. | PASS_1_COMPLETE — no proposal. |
| S028 | DOC-002 p. 67 SAP: stepwise logistic confirmatory model, covariates, 2-sided P<.05. | Matches the reported adjusted-model framework; source does not furnish a same-model P/SE pair beyond mapped output. | PASS_1_COMPLETE — no proposal. |
| S029 | DOC-002 p. 67 SAP: stratum Fisher/Mantel-Haenszel OR and Breslow-Day/Tarone. | Definitions permit distinct stratum analyses; no printed interaction numerical result on this page. | PASS_1_COMPLETE — no proposal. |
| S030 | DOC-002 p. 68 SAP: survivor-only mean SOFA-to-day-9 Student t test. | Survivor-only population is explicitly distinct from all-participant binary responder endpoint. | PASS_1_COMPLETE — no proposal. |
| S031 | DOC-002 p. 68 SAP: 28-day KM/Cox HR and frequency/Fisher OR analyses. | HR and OR are explicitly separate effect measures. | PASS_1_COMPLETE — no proposal. |
| S032 | DOC-002 p. 68 SAP: 90-day KM/Cox HR and frequency/Fisher OR analyses. | Same measure distinction; no output contradiction on this rules page. | PASS_1_COMPLETE — no proposal. |
| S033 | DOC-002 p. 69 SAP: day-15 responder Fisher/Mantel-Haenszel and survivor-only mean-SOFA t test. | Source explicitly distinguishes binary/responder and survivor-only continuous analyses. | PASS_1_COMPLETE — no proposal. |
| S034 | DOC-002 p. 70 SAP: reversal/infection Fisher/Mantel-Haenszel and safety Fisher; two-sided P<.05. | Rules only; no test statistic/estimate pair is present. | PASS_1_COMPLETE — no proposal. |
| S035 | DOC-002 p. 71 SAP: Breslow-Day/Tarone subgroup OR comparisons. | No result estimate/P is printed here; no compatibility calculation applicable. | PASS_1_COMPLETE — no proposal. |
| S036 | DOC-002 p. 72 SAP: subgroup threshold P<.05. | Threshold only; sidedness is not restated on this page (explicitly missing). | PASS_1_COMPLETE — no proposal. |
| S037 | DOC-003 p. 21 eTable 9: univariate OR 2.48 (1.42-4.31), P=.001; adjusted 2.49 (1.42-4.36), P=.001. | Both estimates are contained. Main Table 2 raw Fisher/Mantel-Haenszel P=.002 is not required to equal logistic P=.001. | PASS_1_COMPLETE — no proposal. |
| S038 | DOC-003 p. 21 eTable 9: covariate univariate/adjusted OR/CI/P pairs. | Every printed OR lies in its ordered CI; all CIs cross 1 with non-significant displayed P values. | PASS_1_COMPLETE — no proposal. |
| S039 | DOC-003 p. 22 eTable 10: MALS OR 4.38 (1.15-16.64), P=.034; SII 2.15 (1.16-3.97), P=.020. | Both estimates are contained and directions agree with printed event/total contrasts. | PASS_1_COMPLETE — no proposal. |
| S040 | DOC-003 p. 22 eTable 10: SII day-15 40/106 vs 29/122, printed OR `1.194` (1.09-3.45), P=.030. | `1.194` lies in the CI but printed counts yield crude OR `(40×93)/(66×29)=1.94`; log-CI center is about 1.94 and P=.030 is compatible with that scale, not 1.194. This is a printed point-estimate inconsistency. | PASS_1_COMPLETE — candidate proposal P1-04. |
| S041 | DOC-003 p. 46 eFigure 2: sensitivity OR 2.72 (1.47-5.05), P=.001. | Estimate lies within ordered CI; sensitivity population is explicitly distinct from primary analysis. | PASS_1_COMPLETE — no proposal. |
| S042 | DOC-003 p. 47 eFigure 3: 28-day HR 0.83 (0.59-1.18), P=.298. | Estimate lies within CI; direction and non-significant P are compatible. | PASS_1_COMPLETE — no proposal. |
| S043 | DOC-003 p. 48 eFigure 4: 90-day HR 0.84 (0.63-1.12), P=.231. | Estimate lies within CI; direction and non-significant P are compatible. | PASS_1_COMPLETE — no proposal. |
| S044 | DOC-003 p. 49 eFigure 5: worse-disposition ordinal OR 0.59 (0.38-0.91), P=.018. | Estimate is contained and label/contrast direction is stated. Ordinal-model variance definition is not supplied for exact diagnostic reconstruction. | PASS_1_COMPLETE — no proposal. |
| S045 | DOC-003 p. 50 eFigure 6: Cox HR 2.38 (1.50-3.77), `P=<.001`, censored at day 28. | Estimate lies within CI. The inequality is finite-precision threshold notation, not `P=0`; no independent contradiction is present. | PASS_1_COMPLETE — DISPLAY_ZERO_NOT_CANDIDATE / no proposal. |
| S046 | DOC-003 p. 51 eFigure 7A: primary-endpoint subgroup event/totals and P values. | P values have named event/total contrasts; graphical forest values are not transcribed. No incompatible supplied relation found. | PASS_1_COMPLETE — no proposal. |
| S047 | DOC-003 p. 51 eFigure 7B: primary-endpoint interaction rows (0.47/1.85/0.22/5.79/0.56/3.08 with CIs/Ps). | All printed estimates are contained in their CIs. Exact duplicate comparison with 28-day panel is evaluated under S049. | PASS_1_COMPLETE — candidate implication carried to P1-05 only. |
| S048 | DOC-003 p. 52 eFigure 8A: 28-day mortality subgroup event/totals/P values. | Source supplies no printed forest numbers; provided P values align with their named subgroup contrasts. | PASS_1_COMPLETE — no proposal. |
| S049 | DOC-003 p. 52 eFigure 8B: caption says 28-day mortality but all six OR/CI/P rows exactly repeat primary-endpoint eFigure 7B on p. 51. | Both panels name different outcomes and A-panels have different event/total data; exact six-row duplication is therefore an independent cross-location/output contradiction. | PASS_1_COMPLETE — candidate proposal P1-05. |
| S050 | DOC-003 p. 53 eFigure 9A: 90-day mortality subgroup event/totals/P values. | P values map to the named groups; no source-grounded conflict with the distinct B-panel output. | PASS_1_COMPLETE — no proposal. |
| S051 | DOC-003 p. 53 eFigure 9B: APACHE interaction OR 0.11 with 95% CI 0.36-3.42, P=.86. | The point estimate is below the printed lower CI endpoint (`0.11 < 0.36`); endpoint ordering itself is normal. No model convention can make a reported point estimate fall outside its own stated CI. | PASS_1_COMPLETE — candidate proposal P1-06. |

## Candidate proposals for coordinator registration

These are proposals only. They have no stable C ID and are not adjudications.

### P1-01 — Day-15 SOFA numerator differs between matched Table 2 and narrative

- **Category:** Cross-document numeric inconsistency.
- **Evidence:** DOC-001 p. 6 Table 2: 52/131; DOC-001 p. 7 narrative: 51/131, same outcome/comparison/P=.004.
- **Rule/calculation:** `(52×111)/(79×34)=2.15` rounded, matching the printed Table-2 OR 2.15; a one-person numerator difference is not rounding.
- **Human question:** Which day-15 numerator is source-correct, and should the narrative/table/effect analysis be harmonized?

### P1-02 — APACHE II Table 2 P value is incompatible with printed means, SDs, and Student t-test label

- **Category:** Statistical reporting inconsistency.
- **Evidence:** DOC-002 p. 48: 18.2±8.7 (n=21) versus 30.5±9.4 (n=15), `P=.376`, footnote Student t test.
- **Diagnostic calculation:** pooled-SD t≈4.05 (34 df; two-sided P≈.0003); Welch t≈3.99 (about 29 df; P≈.0004).
- **Human question:** Is a mean, SD, group allocation, or P value misprinted? The source does not state a nonstandard transformation or alternative analysis that would yield `.376`.

### P1-03 — Figure 2C calls an HR-sized value a relative risk

- **Category:** Measure, label, or scale inconsistency.
- **Evidence:** DOC-002 p. 51 Figure 2C labels `RR_death` 2.82 (1.58-5.14) from 69/103 versus 37/89; DOC-002 p. 52 Figure 3 prints HR 2.82 (1.58-5.14) for immunoparalysis.
- **Calculation:** crude risk ratio is 1.61; crude odds ratio is 2.85, compatible with 2.82. The identical value/CI is also the p. 52 HR.
- **Human question:** Should Figure 2C label the reported association HR/OR rather than RR, or are its displayed count rows/value from different analyses?

### P1-04 — eTable 10 SII day-15 OR point estimate is inconsistent with its counts/CI/P value

- **Category:** Statistical reporting inconsistency.
- **Evidence:** DOC-003 p. 22: 40/106 versus 29/122; OR 1.194 (1.09-3.45), P=.030.
- **Calculation:** the counts give OR 1.94; log-CI midpoint is approximately 1.94. Both support a likely 1.94-scale estimate, whereas 1.194 does not.
- **Human question:** Is `1.194` a decimal/transcription error (for example, 1.94), or do the counts/CI/P value belong to a different defined analysis?

### P1-05 — eFigure 8B repeats eFigure 7B's primary-endpoint interaction table under a 28-day mortality label

- **Category:** Cross-document numeric inconsistency.
- **Evidence:** DOC-003 p. 51 eFigure 7B primary endpoint; p. 52 eFigure 8B 28-day mortality. Both print the same six OR/CI/P rows: 0.47/1.85/0.22/5.79/0.56/3.08 and corresponding CIs/Ps.
- **Rule:** The captions name different outcomes and their A panels show different event/total values; verbatim repetition of the complete interaction table cannot represent matched different outputs without an explicitly stated identity, which is absent.
- **Human question:** Does eFigure 8B need its own 28-day-mortality interaction output, or is its caption/outcome label wrong?

### P1-06 — eFigure 9B APACHE interaction estimate is outside its stated CI

- **Category:** Statistical reporting inconsistency.
- **Evidence:** DOC-003 p. 53: APACHE II ≥25 × precision immunotherapy OR 0.11, 95% CI 0.36-3.42, P=.86.
- **Rule:** A printed confidence interval must contain its stated point estimate on the reported ratio scale; 0.11 is below 0.36.
- **Human question:** Which of the point estimate or CI endpoints is correct for this interaction?

## Limitations

- DOC-002 protocol pages use embedded fonts. Direct rendering, rather than native/OCR text, was used for the relevant tables/figures.
- Planned protocol/SAP definitions and observed trial outputs are not presumed to be identical across versions or estimands.
- For Cox/ordinal models without a named variance/test convention, P-value versus CI diagnostics were not used to create candidates.
- Graphical forest-plot positions were never treated as exact numerical estimates when no printed number was available.
