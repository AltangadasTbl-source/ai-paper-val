# Independent inclusion screen — statistical pass 2

Runtime agent ID: /root/pass_2_screener. Fresh qc162_inclusion_screener, gpt-6.1-sol / high; independent of the initial inclusion screener and both statistical checkers. Assigned scope: every new finding in checkers/statistical_pass_2.md, comprising F-ST2-001 only. This agent owns this artifact only; the coordinator appends its row and assigns the stable candidate ID in the canonical screening log.

Read completely: QUALITY_CONTROL_SCOPE.md and the inclusion-screen section of workflow_1_6_2/review_contract.md. Supplied-source authority: CPU Poppler pdftotext -layout reread the main article PDF pp.3 and 6 directly; the current direct-source p.6 render preprocessing/recheck-main-p6.png was visually inspected. Reusable text was not substituted for source confirmation. The assigned checker finding was examined independently rather than treated as a decision. No old review conclusions, external literature, raw data, GPU processing, new extraction helper, or source/reused-asset mutation was used.

## Screening row for coordinator append

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-ST2-001 | statistics_pass_2 | pass_2 | INCLUDE | MEETS_THRESHOLD | C007 |

**One-sentence justification:** F-ST2-001 is included by Route A, category 1 because the source-confirmed age-adjusted relapse-free-survival HR 0.66, 95% CI 0.43–0.99 and P=.048 have no joint rounding-compatible symmetric log-Wald solution, whereas all five other complete effect/CI/P triples on the same page do, with the unspecified actual CI/test constructions retained for human review.

## Exact source locations and document roles

All comparison locations are REPORT content within one supplied document:

- [Main article PDF p.6, right column, age-quartile-adjusted relapse/death paragraph](../../../jama_urashima_2019_oi_190023.pdf#page=6): adjusted HR 0.66, 95% CI 0.43–0.99 and P=.048; adjacent adjusted-death result HR 0.81, CI 0.48–1.36 and P=.42.
- [Main article PDF p.6, Figure 2A](../../../jama_urashima_2019_oi_190023.pdf#page=6): HR 0.76, CI 0.50–1.14 and P=.18.
- [Main article PDF p.6, Figure 2B](../../../jama_urashima_2019_oi_190023.pdf#page=6): HR 0.95, CI 0.57–1.57 and P=.83.
- [Main article PDF p.6, Figure 2C and matching relapse narrative](../../../jama_urashima_2019_oi_190023.pdf#page=6): subdistribution HR 0.75, CI 0.48–1.17 and P=.21.
- [Main article PDF p.6, middle-baseline relapse paragraph](../../../jama_urashima_2019_oi_190023.pdf#page=6): subdistribution HR 0.44, CI 0.21–0.89 and P=.02.
- [Main article PDF p.3, Statistical Analysis and post hoc analyses](../../../jama_urashima_2019_oi_190023.pdf#page=3): Cox proportional-hazards models, HRs and 95% confidence intervals, two-sided P<.05 significance, age-quartile adjustment, and the competing-risk analysis with subdistribution HRs and confidence intervals; the paragraph does not identify the row-specific Wald, score, or likelihood-ratio test or the construction of its interval.

The same-page comparator results corroborate a reproducing calculation; they are not separate discrepant locations. No PLAN document is a conflicting side. Cross-location tier check: this concerns the numerical interval/test mapping for the adjusted primary relapse/death outcome, not a peripheral descriptive comparison or an administrative detail.

## Independent numerical reproduction

The explicit diagnostic calculation uses b=ln(H), q=1.959963984540054, L=exp(b−q×SE), U=exp(b+q×SE), and two-sided P=2Φ(−abs(b)/SE). This is a diagnostic construction, not an assertion about the authors' actual inference. Joint symmetry enforces H²=L×U. Each printed HR and endpoint permits its own half-unit rounding interval; their rounded centers are not inserted as if unrounded inputs.

For the target result, the HR interval is [.655,.665), the lower-limit interval [.425,.435), the upper-limit interval [.985,.995), and the printed P interval [.0475,.0485). Maximizing the diagnostic P over these joint constraints requires H=.655 and U=.995, with L=H²/U=.4311809045. This gives SE=.2133240737, abs(b)/SE=1.9834612942 and P=.0473159264. The opposite bound uses H=.655 and L=.435, with U=.9862643678, giving P=.0427447292. Conservatively allowing both closed endpoints therefore bounds the diagnostic P by [.0427447292,.0473159264]; half-open rounding endpoints cannot increase the upper bound. The extremal choices follow from the monotonicity of −q ln(H)/(ln(U)−ln(H)) and the lower-bound constraint U≥H²/.435.

The lower endpoint of the printed P interval remains greater than this diagnostic upper bound: .0475−.0473159264=.0001840736, with relative gap .0001840736/.048=.0038348668. The independently integrated normal tail differs from the checker's displayed approximation by approximately 0.0000000044 at the upper bound; this numerical precision difference does not alter the interval separation. Both calculations reproduce the same diagnostic finding.

The following independently recomputed examples show that all five other complete same-page triples permit the same method after rounding. They are compatible unrounded examples, not estimates extracted from the authors' data.

| Same-page relationship | Printed HR (95% CI); P | Compatible H | Compatible L | Compatible U | Diagnostic P |
|---|---|---:|---:|---:|---:|
| S001, Figure 2A | .76 (.50–1.14); .18 | .755025 | .5022468674 | 1.135025 | .1766867098 |
| S002, Figure 2B | .95 (.57–1.57); .83 | .945025 | .5706440796 | 1.565025 | .8261090011 |
| S003, Figure 2C | .75 (.48–1.17); .21 | .746525 | .4750252094 | 1.173200 | .2050072667 |
| S009, middle-baseline relapse narrative | .44 (.21–.89); .02 | .435025 | .2138320958 | .885025 | .0216170314 |
| S017, adjacent age-adjusted death | .81 (.48–1.36); .42 | .805025 | .4778889836 | 1.356100 | .4150037372 |

Arithmetic was independently evaluated in JavaScript using composite Simpson integration of the standard-normal density from the positive test statistic to 10 with 20,000 subintervals; the omitted tail is negligible for the displayed precision. No Python review orchestration or external statistical convention was used.

## Independent inclusion reasoning and limits

**Reproduction:** The exact supplied source confirms all three target numbers, the stated 95% interval, the age-adjusted primary-outcome attribution and the two-sided significance level. The joint rounding calculation retains a positive separation between the diagnostic P interval and the printed P interval. The same-page reproducing examples support this diagnostic method; the finding does not rest only on an unsupported conventional approximation.

**Qualifying route:** Route A, category 1, interval versus P value or test. This category covers a P value that does not jointly reproduce from the printed estimate and interval under the supported diagnostic construction. Under the normative scope, its relative gap below .05 does not authorize ROUNDING_OR_DISPLAY_PRECISION, and unknown inferential construction is recorded as the human question rather than used to suppress a reproduced numeric conflict. It is independent of the existing denominator, direction-label and planned-analysis patterns; no duplicate finding is identified within the assigned pass-2 output.

**Affected interpretation or extraction:** The source's age-quartile-adjusted relapse-free-survival treatment comparison, particularly the mapping of the extracted .048 P value to HR .66 and CI .43–.99. The printed interval excludes 1 and the printed P is below .05, so their nominal significance agrees; this screen does not claim a significance reversal or a changed clinical conclusion.

**Immediate context and alternatives:** The nearby significant-effect sentence confirms nominal significance but does not identify the exact interval/test mapping. A score or likelihood-ratio P value with a Wald confidence interval could explain the numbers; another interval construction or a separate test could also do so. The source does not specify the row's unrounded coefficient, standard error, covariance or variance estimator, test statistic, degrees of freedom, CI construction, or named two-sided test. Stata use alone supplies none of these definitions. The candidate must retain these alternatives and must not state that all valid Cox analyses necessarily require the diagnostic P interval, that the actual method was log-Wald, or that a replacement P value is established.

**Human question:** Which confidence-interval and two-sided test constructions, and which unrounded coefficient/standard error or test statistic, jointly produced the age-adjusted HR .66, CI .43–.99 and P=.048?

**Provisional classification:** Review domain statistical_results; relationship type S_W; all relationships S_W; compared roles REPORT main article p.6 target versus REPORT main article p.6 comparator displays and REPORT main article p.3 method description. No precedence ambiguity; the unspecified inferential construction is an evidence limitation, not a document-role ambiguity. Stable candidate registration, evidence-state assignment and inclusion audit belong to the coordinator's subsequent stages. Any registered candidate remains Pending Human Adjudication.

## Completion

Findings screened: 1. Included issues: 1. Screened-out findings: 0; counts for all screened-out reason codes are zero. Every assigned finding has exactly one screening decision. Exact source locations and calculations were independently reread; no scientific-coverage limitation applies to the assigned finding. The unreported row-specific inferential inputs remain a bounded reproduction limitation. No candidate-count target, comparison with other papers, severity, disposition, or proposed correction was used.
