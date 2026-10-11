# Statistical consistency review — pass 1 main and plan shard

Runtime agent: root/statistics_one_main; gpt-6.1-sol/high; FRESH_SPAWN. Status: PASS_1_COMPLETE for all 118 assigned records, S001–S118. Scope: all 89 main-paper statistical/display relationships and 29 shared result-relevant protocol/SAP design families. The statistical inventory part retains all source-valued main rows, every table time point and both Figure 3 time panels. Findings below passed checker self-screening; the independent inclusion screener decides whether each becomes a candidate. No candidate ID or adjudication is assigned here.

Read completely: AGENTS.md, QUALITY_CONTROL_SCOPE.md, PERFORMANCE_PROFILE.md, workflow_1_6_1/review_contract.md, report_spec.md and settings.toml; current tooling, source and coverage records; the entire assigned current main/protocol maps and SAP design/semantic views. Supplied sources and current source-linked extraction only. Tools: recorded direct CPU Poppler26.01.0 pdftotext layout, source-matched retained renders; no new preprocessing needed, web, old conclusions, custom Python or GPU.

## Findings

### F-ST1-001 — Planned completer-first analysis and reported imputation-first one-year weight analysis

**Relationships:** S110; related S002, S006, S112. Proposed relationship type P_R; all relationships P_R. REPORT DOC-001 methods and REPORT DOC-004 eTable 9 are compared with PLAN DOC-003 SAP. The report documents corroborate the same reporting side.

**Exact source locations and document roles:**

- PLAN DOC-003 [SAP p.9, Table 1, primary body-weight row](../../../../joi190106supp2_prod_1635377898.49605.pdf#page=9): body weight change is scheduled at month 6, year 1 and year 6.
- PLAN DOC-003 [SAP p.13, lines305–308](../../../../joi190106supp2_prod_1635377898.49605.pdf#page=13): ITT analyses using full data and multiple imputation.
- PLAN DOC-003 [SAP p.26, lines777–780](../../../../joi190106supp2_prod_1635377898.49605.pdf#page=26): “Main analyses will be based on an intention-to-treat approach with completers only.” The following sentence calls repeated ITT with multiple imputation the sensitivity analysis.
- REPORT DOC-001 [main p.4, Statistical Analysis](../../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4): principal analyses include all randomized participants with baseline nutritional data using multiple imputation; completer analyses are secondary/post hoc sensitivity analyses. The Outcomes section lists body weight among cardiovascular risk factors.
- REPORT DOC-004 [results p.23, eTable 9, weight row and population headings](../../../../joi190106supp3_prod_1635377898.49725.pdf#page=23): multiple-imputation population I3272/C3311, between-group weight change −2.9 kg (95% CI −3.2 to −2.6), P<.001; completers I2840/C2946, −3.1 kg (95% CI −3.4 to −2.7), P<.001.
- REPORT DOC-004 [results p.24, eTable 9 footnote](../../../../joi190106supp3_prod_1635377898.49725.pdf#page=24): baseline mean(SD), 12-month changes mean(95% CI), mixed models with site and couple correlations as random factors; imputed body weight 4.7%.

**Printed values/statements:** The plan places complete-data ITT first and MI as sensitivity. The article places MI first and labels the completer analysis post hoc. eTable 9 supplies both weight contrasts, which differ as shown above.

**Rule and calculation:** Compare the prespecified primary/sensitivity designation for the same one-year weight outcome, not the final CV endpoint or dietary score hierarchy. The SAP explicitly includes year-1 weight reporting. The identities main=completer and sensitivity=MI in the plan are reversed in the report methods. The populations differ by (3272+3311)−(2840+2946)=797 participants. The point-estimate difference between the two reported contrasts is 0.2 kg. Under half-unit rounding at one decimal, MI lies in [−2.95,−2.85) and completer in [−3.15,−3.05); these point-estimate intervals are disjoint. Both estimates are inside their respective ordered CIs and both P values agree in direction; this finding concerns analysis priority, not a claim that the two analyses should produce equal results. No test, covariance or missing-data estimator is inferred.

**Focus area:** D, planned versus reported statistical design, analysis population and missing-data analysis priority.

**Proposed review domain:** protocol_report.

**Affected result or extracted value:** The one-year body-weight between-group contrast selected as the prespecified main analysis: MI −2.9 kg versus complete-data −3.1 kg, with the corresponding CI and analysis population.

**Why context does not resolve it:** Both analyses are printed, so their numerical identification is clear, but neither the methods paragraph nor eTable 9 states that the SAP's completer-first designation was revised or inapplicable to the year-1 weight assessment. The SAP's explicit year-1 weight schedule prevents resolving this simply by assuming it covers only final CV outcomes. A reader can copy the report's principal analysis, but cannot determine from the immediate supplied text whether that is also the planned principal weight analysis.

**Alternative source-grounded interpretations and missing definitions:** The report may intentionally prioritize MI for this preliminary article and preserve completers as a reported sensitivity; alternatively, the plan's completer-first rule may have a narrower intended application than its general wording. The supplied SAP version is July2019 and the paper uses a March2019 database; the package does not link this difference to a specified amendment of weight-analysis priority. The scope of any report-specific exception is the missing definition. This does not imply a protocol violation or recommend a preferred missing-data analysis.

**Exact human question:** Was multiple imputation intentionally selected as the principal one-year weight analysis in place of the SAP's completer-first designation, and which reported contrast should be identified as the prespecified main weight result?

### F-ST1-002 — Planned ancillary multiplicity interval is absent for the reported one-year waist result

**Relationships:** S109; related S005, S059, S108. Proposed relationship type P_R; all relationships P_R. PLAN DOC-003 is compared with REPORT DOC-001 methods/waist result and REPORT DOC-004 eTable 9. The two report documents corroborate the same nominal-interval reporting side.

**Exact source locations and document roles:**

- PLAN DOC-003 [SAP p.9, Table 1, secondary waist row](../../../../joi190106supp2_prod_1635377898.49605.pdf#page=9): waist changes are scheduled at month 6, year 1 and year 6.
- PLAN DOC-003 [SAP p.12, lines282–291 and comparison footnote](../../../../joi190106supp2_prod_1635377898.49605.pdf#page=12): secondary outcomes receive nominal 95% CIs and ancillary Bonferroni (1−alpha/m) CIs, with m=27. The footnote lists change in waist circumference as comparison2. The paragraph says the reports will primarily focus on nominal intervals but also add the adjusted intervals as ancillary analyses.
- REPORT DOC-001 [main p.4, Statistical Analysis](../../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4): all secondary analyses are exploratory and no additional adjustment is conducted for type I error; tests are two-sided, P<.05.
- REPORT DOC-001 [main p.8, Risk Factors](../../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=8): one-year waist difference −3.3 cm, 95% CI −3.6 to −2.9, P<.001.
- REPORT DOC-004 [results p.23, eTable 9 waist row](../../../../joi190106supp3_prod_1635377898.49725.pdf#page=23): MI waist difference −3.3 (−3.6 to −2.9); completer waist difference −3.3 (−3.7 to −3.0), both P<.001; table title expressly 95% CIs.
- REPORT DOC-004 [results p.24, eTable 9 model footnote](../../../../joi190106supp3_prod_1635377898.49725.pdf#page=24): changes use mixed models with site and couple random factors, mean(95% CI).

**Printed values/statements:** The SAP promises both forms of interval for the explicitly listed waist outcome. The report states no additional adjustment and prints only nominal 95% waist intervals. No supplied main or result supplement table/figure prints an ancillary multiplicity-adjusted waist interval.

**Rule and calculation:** Compare the same prespecified secondary waist analysis and planned reporting rule. With the plan's alpha=.05 and m=27, the planned ancillary confidence level is 1−.05/27=.998148148, or 99.8148148%. The reported interval is 95%. This is a confidence-level/reporting-rule comparison; an adjusted interval cannot be calculated from the package without a supplied standard error/test construction and degrees of freedom. The report's P<.001 would be below the diagnostic Bonferroni per-comparison threshold .05/27≈.00185185, so no change in statistical significance is asserted. Figure 4 proportions are a different analysis and are not substituted for the continuous waist contrast.

**Focus area:** D, planned versus reported multiplicity and prespecified ancillary analysis reporting.

**Proposed review domain:** protocol_report.

**Affected result or extracted value:** The confidence interval and multiplicity status attached to the one-year secondary waist-circumference change, particularly whether an ancillary 99.8148% interval was planned and should accompany the nominal 95% interval.

**Why context does not resolve it:** The exploratory designation explains the report's use of nominal inference but does not say whether the explicit ancillary SAP promise for the same scheduled year-1 waist outcome was revised or restricted. The plan itself already prioritizes nominal intervals; therefore prioritizing them does not account for the absence of the additional promised interval. The missing interval affects extraction of planned versus reported inferential precision without implying that the nominal estimate is unusable.

**Alternative source-grounded interpretations and missing definitions:** The ancillary rule might have been intended only for a later comprehensive clinical-outcome report; alternatively, a report-specific decision may have omitted it for the preliminary secondary waist analysis. The SAP includes both year-1 waist reporting and waist in the m=27 roster, and neither supplied location defines such an exception. The applicable report/time scope of the ancillary rule is the remaining missing definition. No preferred adjustment is proposed.

**Exact human question:** Does the SAP's ancillary Bonferroni interval rule apply to the reported year-1 waist result, and if so, was its omission intentional or is the adjusted interval available elsewhere in the supplied analyses?

## Excluded observations

Each observed pattern is listed once with one reason code. Routine relationships that reconcile remain in the inventory. No excluded observation receives a finding ID.

| Location | Observation | Reason code |
|---|---|---|
| REPORT M p.7 Table3 alcohol12mo; M p.4 | CI−0.4 to0.1 contains zero despite P=.01; the upper limit remains positive within [.05,.15), so rounding cannot remove the crossing. Model, sidedness and95% level are stated, but test/CI construction, MI pooling and DF are not. Normal-Wald diagnostic from half-width.25 gives SE≈.1276,z≈1.57,P≈.117; this is not the source's identified test and cannot establish exact compatibility. | CONDITIONAL_OR_UNREPORTED |
| REPORT M p.7 Table3 alcohol6mo | Upper0 may represent a small negative unrounded limit; the proposed CI/P mismatch does not survive rounding. Both time rows remain separately covered. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT M pp.5,7–8 Tables2–3 | Modeled contrasts differ from crude rounded subtraction, including PDQS12mo2.4 versus6.9−4.4=2.5 and fiber6mo23 versus40−16=24. The source explicitly labels mixed models. | MODEL_VERSUS_CRUDE |
| REPORT M p.7 MUFA:SFA12mo | Printed CI0.2–0.2 allows positive unrounded width; P<.001 need not conflict with a tightly estimated nonzero contrast. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT M p.6 erMedDiet relative increase | 4.7/8.5*100≈55.29% matches55% and interval55–56%; exact relative-change CI formula is not stated and no alternative inference substituted. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT M p.10 Figure4 axes/caption | Axis95%CI wording is resolved by explicit median/IQR/1.5-IQR boxplot caption; separate proportion columns have95% CIs. | CONTEXT_RESOLVES |
| REPORT M pp.4,10; PLAN A pp.11,25 | Methods>=5% or at least5mmHg versus figure>5%/>5mmHg and absent diastolic comparison symbol: threshold meaning is clear, with no exact-boundary counts establishing changed classification. | CONTEXT_RESOLVES |
| REPORT M p.10 Figure4 | Numerators, denominators, proportion estimator/test and household variance absent. Importing nutritional denominators or reconstructing counts from CIs needs unestablished mapping. | CONDITIONAL_OR_UNREPORTED |
| REPORT M pp.6,9–10 Figure2/3/4 | Unlabeled frequencies/quantiles cannot be treated as exact printed numbers; median/IQR distributions and modeled mean95% CIs are distinct summaries. | CONTEXT_RESOLVES |
| REPORT M p.4 and pp.7–8 | Complete-only “secondary analyses” immediately elaborated as completer sensitivity, while tables explicitly labelMI. The displayed population is identifiable. | TERMINOLOGY_OR_WORDING |
| REPORT M pp.1,3–5 | Abstract6583 completion wording versus nutritional follow-up availability: missing nutrition does not establish an absent follow-up visit; no exact completion-event definition supplied. MI analysis population itself is explicit. | CONDITIONAL_OR_UNREPORTED |
| PLAN P p.54; PLAN A p.7 weight power | Required337/arm versus diagnostic normal equal-arm calculationceil251.16=252 forSD8,difference2,power.80,alpha.05.337 corresponds to about90% under that diagnostic. Source does not specify calculation test/formula, cluster inflation, weight dropout or variance/correlation definitions; unique contradiction cannot be established. | CONDITIONAL_OR_UNREPORTED |
| PLAN P pp.53–54; PLAN A pp.6–7 CV power | Prose control10% versus figure overall10%, curve position versus2400/arm. Exact CV target power/formula/censoring or figure inflation mapping absent. | CONDITIONAL_OR_UNREPORTED |
| PLAN A p.7 HR; PLAN P p.53 | Native extraction joins citation2 to HR0.70; visual source shows superscript citation, not a third decimal HR0.702. | NOTATION_OR_TYPOGRAPHY |
| PLAN P pp.4,23,42; REPORT M p.3 | Original run-in weight and nut supply explicitly superseded by amendments;125g free almonds versus500g recommended total is stated. | CONTEXT_RESOLVES |
| PLAN P pp.38,46; PLAN A p.24; REPORT M pp.3–5 | Arm-specific17/14-item counseling does not preclude common17-item outcome; protocol explicitly collects17-item score in control. Article interim diet endpoint is distinct from final CV outcome. | CONTEXT_RESOLVES |
| PLAN P pp.52–53; PLAN A p.8; REPORT M pp.4,11 | Applying3/5/8-year stopping limits to one-year dietary report assumes an unestablished clinical stopping look. No such decision reported. | CONDITIONAL_OR_UNREPORTED |
| PLAN A p.26; REPORT M p.4; REPORT R p.24 | Plan20/MICE/lost>=2years versus report8/MCMC for first-year nutrition and MICE for risk outcomes. Common missingness/estimand/time/outcome model is not established. | CONDITIONAL_OR_UNREPORTED |
| PLAN A pp.25–26; REPORT M p.4; REPORT R pp.23–24 | Additional planned adjusted weight model versus abbreviated report random-effects footnote: current table is not identified as that additional analysis; unreported fixed covariates alone do not establish replacement. | CONDITIONAL_OR_UNREPORTED |
| PLAN P p.52; PLAN A pp.25–26 | Different CV strata/covariate descriptions across plan versions have no matching CV result here and do not change a current key result, analysis size or asserted decision. | PERIPHERAL_COMPARISON |
| PLAN P p.52; PLAN A p.26; REPORT M pp.4,11 | Additional clinical subgroup/per-protocol/first-household-member analyses absent in preliminary diet report do not identify replacement of a matched prespecified dietary analysis. Weight priority difference separately emitted. | CONDITIONAL_OR_UNREPORTED |
| PLAN P pp.18,24–28,74–75; PLAN A pp.14–16; REPORT M pp.1–3 | Diabetes quota25% versus27%, calendars/sites, auxiliary schedules and other baseline/screening comparisons do not change assigned main-analysis size or decision rule. | PERIPHERAL_COMPARISON |
| PLAN P p.54; PLAN A p.6; REPORT M pp.2–3 | Prospective target6000 and achieved6874 have distinct quantity roles; additional recruitment is not a conflicting count. | CONTEXT_RESOLVES |
| PLAN A pp.12–13,26–27 | General adherence includes weight loss, while weight-specific per-protocol censoring has explicit exceptions/two-consecutive-year rules; no one-year per-protocol effect asserted. | CONTEXT_RESOLVES |
| REPORT M p.5 score rationale | log(.75)=−.2877 andexp(−.2877/2)≈.866=HR.87/13% reduction reconcile. Historical observational HRs do not identify current trial RR/HR. | CONTEXT_RESOLVES |

## Limitations and completion counts

Relationships118; pass-1 completed118. Findings2: F-ST1-001 and F-ST1-002. Excluded observations25. No scientific source/relationship gap in this shard. Exact inference limits: named test/CI/MI-pooling details and Figure4 denominators absent; sample-size formula, weight inflation and CV target power absent; unlabeled graphics cannot provide exact counts/quantiles. Diagnostics are explicitly labeled. Findings require independent inclusion screening.

Durable outputs: statistics/parts/pass1_main_inventory.md and checkers/parts/statistical_pass_1_main.md. No canonical merge edited. Pass2 requires a newly spawned different runtime agent with complete ledger/screen/recheck context.
