# Complete Checker Exclusions for Statistical Pass 2 and Audit

This mechanical projection preserves every Excluded observations row from the three current checker artifacts. It does not introduce scientific decisions. The canonical checker artifacts remain authoritative; exact source pages are reread by each later reviewer.

## numeric_consistency.md

| Location | Observation | Reason code |
|---|---|---|
| REPORT main pp1/4 minority 31%; Table 1 p5 race counts | Explicit race denominators 361+327+284+314=1286; all 20 directly printed minority-count inputs sum 429. Allow each minority count±.5 and each denominator±.5: recomputed proportion[100×419/1288,100×439/1284]=[32.53106,34.19003]%. Printed 31% interval[30.5,31.5]; gap 1.03106/31=.03326≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p2 enrollment 1320 versus actual 1312 | Goal differs from achieved cohort; even literal two-copy gap 7/1320=.00530≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main Table 1 p5 versus supplementary baseline medication copies | Baseline descriptive values and nonmissing denominators are matched; differences caused by treating randomized N as the response N are not reproduced; no such denominator is stated. | NOT_REPRODUCED |
| REPORT main Table 2 and supp eTables 4–9 | Crude subtraction of time-specific means, or crude ratios of printed cross-sectional geometric means, differs from adjusted/MI longitudinal change; footnotes distinguish these quantities. | MODEL_VERSUS_CRUDE |
| REPORT supplement eFigure 2 p18 versus eTable 6 p11 | Overall P.89 versus.90: intervals[.885,.895]and[.895,.905]touch; gap 0. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT supplement eFigures 2/3 pp18/19 captions | Captions say difference while plot/table label ratio; null 1/logticks and geometric change values identify multiplicative quantity immediately. No evidence of additive computation. | TERMINOLOGY_OR_WORDING |

## cross_source_consistency.md

Only apparent issues that were not emitted are listed; reconciled checks above are not exclusions. Each row has exactly one scope reason code.

| Location | Observation | Reason code |
|---|---|---|
| REPORT [main p.7 Figure2](../../../jama_de_boer_2019_oi_190122.pdf#page=7) versus [p.8 Table2](../../../jama_de_boer_2019_oi_190122.pdf#page=8) and [supplement p.11](../../../joi190122supp2_prod.pdf#page=11) | Omega panel participant rows repeat vitaminD contributor counts. These are contributors at individual time points; no change of the full analytic population or primary effect attribution is established by the contributor rows alone. | PERIPHERAL_COMPARISON |
| REPORT [main p.4 medication narrative](../../../jama_de_boer_2019_oi_190122.pdf#page=4) versus [supplement p.7 eTable2](../../../joi190122supp2_prod.pdf#page=7) | Insulin use is described as relatively stable despite20%baseline versus16%year5. This qualitative description does not change a primary/key secondary result or leave a printed medication percentage unidentified. | TERMINOLOGY_OR_WORDING |
| PLAN [p.16 EPA:DHA40:30](../../../joi190122supp1_prod.pdf#page=16) versus REPORT [main p.2 EPA465/DHA375](../../../jama_de_boer_2019_oi_190122.pdf#page=2) | Planned ratio interval[39.5/30.5,40.5/29.5]=[1.2951,1.3729]; reported ratio interval[464.5/375.5,465.5/374.5]=[1.2370,1.2430]. Gap.0521 divided by reference40/30 is.0391, at most.05. Total840mg also agrees. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN [p.33 follow-up1058/80%](../../../joi190122supp1_prod.pdf#page=33) versus REPORT [main p.3 target1320](../../../jama_de_boer_2019_oi_190122.pdf#page=3) | Nominal .80×1320=1056 versus1058. Rounded80% interval with1320 half-unit gives[1049.0025,1063.0025], overlapping printed1058. No target/assumption discrepancy survives display precision. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT [main p.3 secondary “exploratory” interpretation](../../../jama_de_boer_2019_oi_190122.pdf#page=3) versus PLAN [p.32 secondary status](../../../joi190122supp1_prod.pdf#page=32) | Interpretation as exploratory due multiplicity does not relabel the explicitly prespecified secondary outcomes as post-hoc outcomes. This is inferential caution wording, not a reproduced change of outcome status. | TERMINOLOGY_OR_WORDING |
| PLAN [p.14 “diabetes of hypertension”](../../../joi190122supp1_prod.pdf#page=14) | Malformed connecting word in a screening sentence; no cohort count or reported hypertensive-CKD inclusion is supplied to establish a changed analysis population. The symbol/word ambiguity alone does not qualify. | TERMINOLOGY_OR_WORDING |
| PLAN [p.12 baseline samples required](../../../joi190122supp1_prod.pdf#page=12) versus REPORT [main pp.2–3 agreement to provide/baseline missing](../../../jama_de_boer_2019_oi_190122.pdf#page=2) | Four missing baseline eGFR measurements do not establish that required samples were never returned rather than unavailable for assays; no claim of enrolling participants who refused samples is printed. | CONDITIONAL_OR_UNREPORTED |
| PLAN [p.19 adherence/biomarker LMM predecessor](../../../joi190122supp1_prod.pdf#page=19), [p.33 LMM biomarker replacement](../../../joi190122supp1_prod.pdf#page=33) versus REPORT [supplement p.17 correlations](../../../joi190122supp2_prod.pdf#page=17) | Two plotted correlations r=−.05/−.02 alone do not identify their underlying adjustment or establish a specific replacement model. This reviewer does not infer unreported regression details from r; the primary/secondary exploratory distinction needs source-grounded statistical follow-up. | CONDITIONAL_OR_UNREPORTED |
| PLAN [p.17 “secondary dichotomous ... continuous”](../../../joi190122supp1_prod.pdf#page=17) | The displayed eGFR subtraction, no-transformation rationale and analysis equation identify the continuous quantity immediately. No printed number changes. | TERMINOLOGY_OR_WORDING |
| REPORT [supplement pp.18–19 captions “difference”](../../../joi190122supp2_prod.pdf#page=18) | Captions use generic difference while table/forest headers explicitly state ratioactive/placebo with null1. The quantitative measure is apparent from immediate headers; this wording is separate from F-XS-002's reversed favor direction. | TERMINOLOGY_OR_WORDING |
| PLAN [p.23 parent interim rule](../../../joi190122supp1_prod.pdf#page=23) versus REPORT [main p.3 final alpha](../../../jama_de_boer_2019_oi_190122.pdf#page=3) | No ancillary interim statistic or stopping decision is reported. Inferring a conflict from absent ancillary monitoring details would depend on treating the parent cancer/CVD monitoring plan as an ancillary outcome decision. | CONDITIONAL_OR_UNREPORTED |

## statistical_pass_1.md

Only apparent issues intentionally not emitted are listed; reconciled checks appear below.

| Location | Observation | Reason code |
|---|---|---|
| REPORT mainp8 Table 2; supppp9–14 eTables 4–9 | Raw arithmetic on rounded arm means/changes need not equal the explicitly adjusted/imputed treatment contrast; no source says the contrast is crude. | MODEL_VERSUS_CRUDE |
| REPORT mainp9 Table 3 and suppp15 eTable 10 | HR need not equal the ratio of event counts or rounded incidence rates; it is explicitly from Cox regression. | MODEL_VERSUS_CRUDE |
| REPORT suppp12 eTable 7; p13 eTable 8 | Some normal diagnostics from central printed ratio/CI values differ from printed P, but half-unit estimate/endpoint rounding permits reconciliation; no exact Rubin df is supplied. For eTable 8 D, ratio1.015 within printed1.02±.005 andSE≈.092 givesP≈.871, compatible with.87. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT mainp8 Figure 3 BMI≥30 | A closing parenthesis is missing afterSD15.0; the numeric value and interpretation remain evident. | NOTATION_OR_TYPOGRAPHY |
| PLANp33 section15g vs REPORT suppp17 eFigure 1 | Planned biomarker-replacement LMM versus printed correlations r−.05/−.02: the figure does not identify a regression coefficient or state that correlations replaced the planned model. Nonreporting alone does not establish a conflict for this exploratoryanalysis. | CONDITIONAL_OR_UNREPORTED |
| PLANp32 Equation 1 versus Equation 2 | Equation 1 lacks a time-main term; adding one would assume an unrestricted interaction model not independently required by a supplied statement. A stated constrained model is not questioned merely because another model could be preferred. | OUT_OF_FOCUS |
| PLANp17 versus p19 Table 2/narrative, with amendedp32 | Originalsecondary versus co-primary eGFR terminology: the final relied-on plan explicitly replaces prior endpoints with year 5 eGFR primary; no ambiguity in the current primary decision rule or extracted estimand remains. | CONTEXT_RESOLVES |
| REPORT mainp3 clinical relevance wording | Detectable2.3difference and surrogate3.75difference are distinct stated thresholds, and the report's confidence-limit claim explicitly uses3.75; wording does not assert their numeric equivalence. | TERMINOLOGY_OR_WORDING |
