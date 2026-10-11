# Complete Initial Finding Index for Quality Audit

This source-preserving mechanical view includes all three initial checker findings, copied from the canonical checker artifacts. Every finding has one independent screening decision. No pass-2 finding was emitted. All source links resolve from this directory with the canonical checker depth.

## Source: checkers/numeric_consistency.md

### F-NUM-001

The abstract describes the main-analysis population as having completed 12-month follow-up without distinguishing that population from participants with observed follow-up information.

**Exact source locations and document roles:**

- REPORT DOC-001 [PDF p. 1, abstract Results](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=1): “Among 6874 randomized participants” and “6583 (96%) completed the 12-month follow-up and were included in the main analysis.”
- REPORT DOC-001 [PDF p. 3, Figure 1, main-analysis boxes and 12-month information/sensitivity boxes](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=3): 3272 intervention and 3311 control included in main analyses; 439 and 368 without available nutritional information at 12 months; 2833 and 2943 in the 12-month sensitivity analyses.
- REPORT DOC-001 [PDF p. 4, Statistical Analysis and Results](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4): principal analyses include randomized participants with baseline nutritional data regardless of incomplete information at follow-up; 53 baseline questionnaire exclusions and 238 energy exclusions; 6583 analyzed with multiple imputation.
- REPORT DOC-001 [PDF p. 5, Table 2 header and footnote a](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=5): main denominators 3272 and 3311; 517 er-MedDiet values imputed at 12 months, and 807 MDS/MEDAS/PDQS values imputed at 12 months.

**Printed inputs:** 6874 randomized; 6583 stated completers and main-analysis participants; 3272 and 3311 main-analysis arm totals; 53 and 238 baseline exclusions; 439 and 368 missing nutritional-information counts; 2833 and 2943 nutritional completers; 517 missing primary-score values filled by imputation.

**Rule and calculation:** A baseline-eligible analysis count including imputed follow-up information is distinct from an observed follow-up outcome count. The number 6583 is exactly reconstructed by 6874 − 53 − 238 = 6583 and 3272 + 3311 = 6583. Nutritional completeness gives 2833 + 2943 = 5776, equivalently 6583 − 439 − 368 = 5776. For the primary er-MedDiet score, the reported 517 imputed values imply 6583 − 517 = 6066 non-imputed values at 12 months. With randomized denominator 6874, these three quantities are 95.7667%, 84.0268%, and 88.2456%, respectively. They describe distinct populations. No claim is made that absence of nutritional information establishes absence from the follow-up visit.

**Display-precision check:** The 96% itself reconciles with 6583/6874 because 95.7667% lies inside the whole-percentage interval 95.5–96.5%. The observation concerns the completion attribution, not that rounded percentage. Even allowing half-unit intervals around each integer tally, the primary non-imputed count lies between 6065 and 6067 and nutritional completeness between 5775 and 5777; neither overlaps the displayed 6583 interval 6582.5–6583.5.

**Focus area:** A, counts and denominators.

**Proposed review domain:** statistical_results.

**Proposed relationship type:** S_W. All compared locations are within REPORT DOC-001.

**Affected result or extracted value:** The observed 12-month completion count and percentage for the primary dietary-adherence analysis, and whether 6583 can be extracted as complete observed follow-up rather than as the multiple-imputation analysis population.

**Why context does not resolve it:** The abstract uses one number for completion and analysis without stating that completion means attendance rather than observed dietary information. The body clearly identifies the analysis population but retains different observed-information counts for the primary questionnaire and food-frequency-based measures. It does not identify a visit-attendance count that independently supports 6583 as completed follow-up. A reader can identify the analyzed denominator but cannot choose an observed primary follow-up completion count from the abstract's statement alone.

**Alternative source-grounded interpretations:** The intended 6583 may denote only baseline-eligible participants retained in the imputed main analysis. Alternatively, all 6583 may have attended some 12-month follow-up while dietary measurements remained incomplete; the package does not give a count or definition establishing that attendance interpretation. Primary-score availability and nutritional-information completeness must remain separate and do not themselves establish withdrawal or loss to clinical follow-up.

**Exact human question:** Does “6583 (96%) completed the 12-month follow-up” refer to visit attendance or to inclusion in the multiple-imputation analysis, and what count and denominator should be extracted for observed 12-month primary er-MedDiet follow-up completeness?

**Direct-source confirmation:** The abstract and Figure 1 were visually inspected in fresh Poppler pdftoppm 26.01.0 renders; Table 1/methods and Table 2 were visually inspected in source-linked retained renders. Fresh direct Poppler pdftotext 26.01.0 layouts of pp. 1–4 and p. 5 confirm the quoted values. Derivatives: preprocessing/numeric-main-p001.png, preprocessing/numeric-main-p003.png, preprocessing/numeric-main-p001-004.txt, preprocessing/numeric-main-p005.txt. Rendered derivatives serve as direct-source visual confirmation, not independent document comparators.


## Source: checkers/statistical_pass_1.md

### F-ST1-001 — Planned completer-first analysis and reported imputation-first one-year weight analysis

**Relationships:** S110; related S002, S006, S112. Proposed relationship type P_R; all relationships P_R. REPORT DOC-001 methods and REPORT DOC-004 eTable 9 are compared with PLAN DOC-003 SAP. The report documents corroborate the same reporting side.

**Exact source locations and document roles:**

- PLAN DOC-003 [SAP p.9, Table 1, primary body-weight row](../../../joi190106supp2_prod_1635377898.49605.pdf#page=9): body weight change is scheduled at month 6, year 1 and year 6.
- PLAN DOC-003 [SAP p.13, lines305–308](../../../joi190106supp2_prod_1635377898.49605.pdf#page=13): ITT analyses using full data and multiple imputation.
- PLAN DOC-003 [SAP p.26, lines777–780](../../../joi190106supp2_prod_1635377898.49605.pdf#page=26): “Main analyses will be based on an intention-to-treat approach with completers only.” The following sentence calls repeated ITT with multiple imputation the sensitivity analysis.
- REPORT DOC-001 [main p.4, Statistical Analysis](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4): principal analyses include all randomized participants with baseline nutritional data using multiple imputation; completer analyses are secondary/post hoc sensitivity analyses. The Outcomes section lists body weight among cardiovascular risk factors.
- REPORT DOC-004 [results p.23, eTable 9, weight row and population headings](../../../joi190106supp3_prod_1635377898.49725.pdf#page=23): multiple-imputation population I3272/C3311, between-group weight change −2.9 kg (95% CI −3.2 to −2.6), P<.001; completers I2840/C2946, −3.1 kg (95% CI −3.4 to −2.7), P<.001.
- REPORT DOC-004 [results p.24, eTable 9 footnote](../../../joi190106supp3_prod_1635377898.49725.pdf#page=24): baseline mean(SD), 12-month changes mean(95% CI), mixed models with site and couple correlations as random factors; imputed body weight 4.7%.

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

- PLAN DOC-003 [SAP p.9, Table 1, secondary waist row](../../../joi190106supp2_prod_1635377898.49605.pdf#page=9): waist changes are scheduled at month 6, year 1 and year 6.
- PLAN DOC-003 [SAP p.12, lines282–291 and comparison footnote](../../../joi190106supp2_prod_1635377898.49605.pdf#page=12): secondary outcomes receive nominal 95% CIs and ancillary Bonferroni (1−alpha/m) CIs, with m=27. The footnote lists change in waist circumference as comparison2. The paragraph says the reports will primarily focus on nominal intervals but also add the adjusted intervals as ancillary analyses.
- REPORT DOC-001 [main p.4, Statistical Analysis](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4): all secondary analyses are exploratory and no additional adjustment is conducted for type I error; tests are two-sided, P<.05.
- REPORT DOC-001 [main p.8, Risk Factors](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=8): one-year waist difference −3.3 cm, 95% CI −3.6 to −2.9, P<.001.
- REPORT DOC-004 [results p.23, eTable 9 waist row](../../../joi190106supp3_prod_1635377898.49725.pdf#page=23): MI waist difference −3.3 (−3.6 to −2.9); completer waist difference −3.3 (−3.7 to −3.0), both P<.001; table title expressly 95% CIs.
- REPORT DOC-004 [results p.24, eTable 9 model footnote](../../../joi190106supp3_prod_1635377898.49725.pdf#page=24): changes use mixed models with site and couple random factors, mean(95% CI).

**Printed values/statements:** The SAP promises both forms of interval for the explicitly listed waist outcome. The report states no additional adjustment and prints only nominal 95% waist intervals. No supplied main or result supplement table/figure prints an ancillary multiplicity-adjusted waist interval.

**Rule and calculation:** Compare the same prespecified secondary waist analysis and planned reporting rule. With the plan's alpha=.05 and m=27, the planned ancillary confidence level is 1−.05/27=.998148148, or 99.8148148%. The reported interval is 95%. This is a confidence-level/reporting-rule comparison; an adjusted interval cannot be calculated from the package without a supplied standard error/test construction and degrees of freedom. The report's P<.001 would be below the diagnostic Bonferroni per-comparison threshold .05/27≈.00185185, so no change in statistical significance is asserted. Figure 4 proportions are a different analysis and are not substituted for the continuous waist contrast.

**Focus area:** D, planned versus reported multiplicity and prespecified ancillary analysis reporting.

**Proposed review domain:** protocol_report.

**Affected result or extracted value:** The confidence interval and multiplicity status attached to the one-year secondary waist-circumference change, particularly whether an ancillary 99.8148% interval was planned and should accompany the nominal 95% interval.

**Why context does not resolve it:** The exploratory designation explains the report's use of nominal inference but does not say whether the explicit ancillary SAP promise for the same scheduled year-1 waist outcome was revised or restricted. The plan itself already prioritizes nominal intervals; therefore prioritizing them does not account for the absence of the additional promised interval. The missing interval affects extraction of planned versus reported inferential precision without implying that the nominal estimate is unusable.

**Alternative source-grounded interpretations and missing definitions:** The ancillary rule might have been intended only for a later comprehensive clinical-outcome report; alternatively, a report-specific decision may have omitted it for the preliminary secondary waist analysis. The SAP includes both year-1 waist reporting and waist in the m=27 roster, and neither supplied location defines such an exception. The applicable report/time scope of the ancillary rule is the remaining missing definition. No preferred adjustment is proposed.

**Exact human question:** Does the SAP's ancillary Bonferroni interval rule apply to the reported year-1 waist result, and if so, was its omission intentional or is the adjusted interval available elsewhere in the supplied analyses?



