# Numeric consistency review

Reviewer runtime: 01a12959-5a05-7980-8b19-ced046b9cf42. Model: gpt-6.1-sol. Reasoning effort: medium. Fresh mandatory numeric stage. Source-only review; no earlier candidate sets, screening, audit conclusions or reports used.

## Completed scope

All 120 stable N relationships (N001–N098, N301–N322) and numeric applicability in all 211 stable S relationships (S001–S123, S301–S388) were completed. No N/S identifiers were reassigned. The [numeric inventory](../relationships/numeric_relationship_inventory.md) records every N check; three disjoint source-bounded parts explicitly record every S check: [main S001–S120](../relationships/numeric_main_s_001_120.md), [main S121–S123](../relationships/numeric_main_s_121_123.md), and [support S301–S388](../relationships/numeric_support_s_301_388.md). Each part has ≤120 relationships and <200000 characters.

Checks covered randomized, treated, analyzed, followed-up and per-protocol totals; exclusion reasons; every baseline table count and conditional denominator; surgery, anesthetic and drug partitions; every main and per-protocol outcome event/percentage pair; all subgroup contributors/events; component count means; survival risk counts; percentages and precision; and effect-measure identity. Model-specific inferential analyses are retained without imposing crude-risk identities on explicit Cox, GEE, mixed-effect or proportional-odds models.

Scientific sources: DOC-001 main REPORT; DOC-002 protocol PLAN; DOC-003 amendment PLAN; DOC-004 SAP PLAN; DOC-005 results support REPORT; DOC-006 data-sharing REPORT with no numeric result. New main/support mapper parts were read completely as quantitative records, with exact source transcriptions consulted where needed. Direct Poppler pdftotext 26.01.0 rereading of main pp1,4,8–10, support p 29 and SAPp3 confirmed source locations. Existing rendered source images visually checked main pp1,8–10 and support pp29,42; historical rendering engine is unrecorded. No new derivative, OCR, GPU processing or source modification was performed.

Three qualifying findings are emitted below. Other apparent issues are recorded once in the Excluded observations table. No candidate IDs or adjudications are assigned.

## Findings

### F-NUM-001

**Title:** Repeated binary effect estimates track treatment allocation conditional on event status rather than the stated intervention risk contrast.

**Locations and roles:** REPORT [main Table3, PDF p9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), [continued Table3/Figure2, PDF p10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), [main binary-method specification, PDF p4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), [primary/mild/pleural narrative, PDF p8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), and [primary abstract, PDF p1](../../../jama_bluth_2019_oi_190055_16092.pdf#page=1). REPORT [support eTable8, PDF p29](../../../joi190055supp4_prod_16092.pdf#page=29) has a generic Effect Estimate heading; REPORT [support eFigure12, PDF p42](../../../joi190055supp4_prod_16092.pdf#page=42) labels component effects Risk Ratio and collapsed composite Odds Ratio. PLAN SAP confirms intended analysis terminology only and is not a side of this reporting inconsistency.

**Printed inputs:** Main Table3 has reference patients high 989 and low 987, and explicitly labels its binary estimates Risk Ratio; note b describes RRs and Wald likelihood ratio approximation, with χ² tests in note c. For pleural effusion,43/989(4.3%) versus21/987(2.1%), printedRR1.35(1.14–1.62). For intraoperative hypoxemia,49/989(5.0%) versus134/987(13.6%), printedRR.51(.40–.65). For hypotension,313/989(31.6%) versus170/987(17.2%), printedRR1.43(1.31–1.56). Every binary row and its printed effect is preserved in the full diagnostic table below. No source-specified adjusted model is being equated to a crude ratio.

**Rule and calculation:** For counts a/b in randomized arms of sizes nH/nL, the event-risk contrast is (a/nH)/(b/nL). Diagnostic reconstruction of a transposed 2×2 table instead gives [a/(a+b)]/[(nH−a)/(nH+nL−a−b)], a ratio of probabilities of receiving high PEEP among participants with versus without an event. This diagnostic yields1.35795 for pleural effusion, .51074 for hypoxemia and1.43123 for hypotension, close to the printed 1.35/.51/1.43 across many rows. The latter quantity is not risk of the outcome under high versus low PEEP. This is a repeated source-supported effect-identity observation, not an assertion about the authors' computational code.

Apply half-unit input intervals independently: event-risk ratio lower=(a−.5)/(nH+.5) divided by (b+.5)/(nL−.5); upper=(a+.5)/(nH−.5) divided by (b−.5)/(nL+.5), when b>.5. Printed effects have ±.005 intervals. For pleural effusion, recomputed[1.97075,2.11980] vs printed[1.345,1.355]; gap .61575, relative gap .45611. For hypoxemia, recomputed[.35950,.37041] vs[.505,.515]; gap .13459, relative .26390. For hypotension, recomputed[1.82729,1.84769] vs[1.425,1.435]; relative gap .27433. These substantially exceed .05.

**Focus area:** C, statistical method logic/effect-measure identity; associated counts under A.

**Proposed review domain:** statistical_results. Proposed primary relationship S_C, with S_W also present (main table/narrative/figure and main versus results support); REPORT compared with REPORT.

**Qualifying route:** Route B. The effect label and orientation bear directly on extraction; source numerical reconstruction supports a different conditional contrast. Several individual rows also support Route A, category4 if the displayed binary method is taken as unadjusted event-risk estimation. Registration does not rely on that additional route.

**Affected result or extracted value:** Intervention risk ratios for moderate respiratory failure, atelectasis, pleural effusion, cardiopulmonary edema, ARDS, gastrointestinal failure, extrapulmonary infection, unexpected ICU admission/readmission, hypoxemia, hypotension, bradycardia, in-hospital mortality and rescue strategy, plus repeated corresponding per-protocol/figure effects. Hypoxemia.51 versus count-derived.36493 and pleural effusion1.35 versus2.04348 would yield different extracted relative magnitudes. PrimaryRR.93 alone does not exceed the required .05 numeric display threshold; its repeated locations corroborate the common pattern rather than establish an independent numeric finding.

**Why context does not resolve it:** The printed column defines risk of the outcome under the intervention contrast, but multiple substantial mismatches systematically reconstruct a different conditional probability. Immediate context supplies no adjustment, alternative risk denominator or effect definition accounting for these values. A reader cannot know which estimand the printed interval describes. The generic eTable8 heading does not supply the missing definition; it is retained as generic rather than silently relabeled.

**Alternatives:** An unreported adjusted/marginal estimator could theoretically differ from crude risks; that possibility is retained, but no source passage connects such an estimator to these table values. The systematic transposed-table diagnostic across common and rare outcomes needs an explicit denominator/estimand definition. Figure2/subcomponent GLMs and eFigure12 Bonferroni intervals may be model based; their occurrences corroborate the shared numerical pattern and are not independently forced to equal crude ratios. A transcription or display-stage transformation could also produce the pattern.

**Exact human question:** What outcome, conditioning variable, arm/reference orientation and denominator define the binary Risk Ratio/Effect Estimate columns and corresponding forest plots, and which source-described computation produces their point estimates and intervals?

### Complete point-estimate diagnostic table for F-NUM-001

Rows above .05 independently support the numeric magnitude discrepancy when interpreted as the stated intervention event-risk contrast. Rows at most .05 remain corroborating occurrences of one repeated effect-definition pattern; they are not independent qualifying numeric discrepancies. Diagnostic transposed estimates are not proposed corrections. Exact zero cells retain undefined crude estimates rather than a fabricated finite value.

| ID | Outcome/location | High; low events/total | Printed effect | Event-risk contrast | Half-unit recomputed interval | Relative discrepancy | Transposed-table diagnostic | Display threshold |
|---|---|---|---:|---:|---|---:|---:|---|
| S054 | Primary pulmonary complication composite≤5postoperative days | 211/989; 233/987 | 0.93 | 0.90375 | [0.89877, 0.90876] | 0.01747 | 0.93579 | At most 0.05 |
| S055 | Component mild respiratory failure | 135/989; 154/987 | 0.92 | 0.87485 | [0.86791, 0.88184] | 0.03604 | 0.92277 | At most 0.05 |
| S056 | Component moderate respiratory failure | 42/989; 58/987 | 0.83 | 0.72267 | [0.70725, 0.73838] | 0.10436 | 0.83202 | Above 0.05 |
| S057 | Component severe respiratory failure | 30/989; 36/987 | 0.90 | 0.83165 | [0.80577, 0.85829] | 0.04079 | 0.90530 | At most 0.05 |
| S058 | Component atelectasis | 44/989; 55/987 | 0.88 | 0.79838 | [0.78141, 0.81569] | 0.06740 | 0.88277 | Above 0.05 |
| S059 | Component pleural effusion | 43/989; 21/987 | 1.35 | 2.04348 | [1.97075, 2.11980] | 0.45611 | 1.35795 | Above 0.05 |
| S060 | Component new pulmonary infiltrates | 14/989; 18/987 | 0.87 | 0.77620 | [0.72752, 0.82773] | 0.04284 | 0.87231 | At most 0.05 |
| S061 | Component cardiopulmonary edema | 17/989; 9/987 | 1.31 | 1.88507 | [1.73158, 2.05674] | 0.31800 | 1.31173 | Above 0.05 |
| S062 | Component bronchospasm | 12/989; 10/987 | 1.09 | 1.19757 | [1.09192, 1.31446] | 0.00000 | 1.09091 | At most 0.05 |
| S063 | Component pulmonary infection | 10/989; 10/987 | 0.99 | 0.99798 | [0.90202, 1.10415] | 0.00000 | 0.99898 | At most 0.05 |
| S064 | Component aspiration pneumonitis | 2/989; 1/987 | 1.33 | 1.99596 | [0.99697, 4.99494] | 0.00000 | 1.33266 | At most 0.05 |
| S065 | Component ARDS | 3/989; 1/987 | 1.50 | 2.99393 | [1.66161, 6.99292] | 0.10441 | 1.50000 | Above 0.05 |
| S066 | Component pneumothorax | 1/989; 3/987 | 0.50 | 0.33266 | [0.14242, 0.59939] | 0.00000 | 0.49899 | At most 0.05 |
| S067 | Secondary severe pulmonary composite | 116/989; 134/987 | 0.91 | 0.86392 | [0.85613, 0.87178] | 0.03651 | 0.91737 | At most 0.05 |
| S068 | Secondary extrapulmonary composite | 167/989; 150/987 | 1.06 | 1.11108 | [1.10296, 1.11927] | 0.03581 | 1.06324 | At most 0.05 |
| S069 | Extrapulmonary systemic inflammatory response syndrome | 93/989; 83/987 | 1.06 | 1.11822 | [1.10443, 1.13219] | 0.03719 | 1.06154 | At most 0.05 |
| S070 | Extrapulmonary sepsis | 18/989; 15/987 | 1.09 | 1.19757 | [1.12561, 1.27457] | 0.02808 | 1.09147 | At most 0.05 |
| S071 | Extrapulmonary severe sepsis | 7/989; 10/987 | 0.82 | 0.69858 | [0.61717, 0.78868] | 0.03210 | 0.82143 | At most 0.05 |
| S072 | Extrapulmonary septic shock | 7/989; 8/987 | 0.93 | 0.87323 | [0.76239, 0.99899] | 0.00000 | 0.93191 | At most 0.05 |
| S073 | Extrapulmonary gastrointestinal failure | 65/989; 56/987 | 1.07 | 1.15837 | [1.13813, 1.17899] | 0.05900 | 1.07845 | Above 0.05 |
| S075 | Extrapulmonary acute kidney failure | 31/989; 32/987 | 0.98 | 0.96679 | [0.93562, 0.99899] | 0.00000 | 0.98259 | At most 0.05 |
| S077 | Extrapulmonary infection | 29/989; 23/987 | 1.11 | 1.25832 | [1.20909, 1.30978] | 0.08476 | 1.11771 | Above 0.05 |
| S078 | Extrapulmonary hepatic failure | 9/989; 9/987 | 0.99 | 0.99798 | [0.89202, 1.11652] | 0.00000 | 0.99898 | At most 0.05 |
| S079 | Extrapulmonary coma | 2/989; 2/987 | 0.99 | 0.99798 | [0.59818, 1.66498] | 0.00000 | 0.99899 | At most 0.05 |
| S080 | Extrapulmonary disseminated intravascular coagulation | 1/989; 0/987 | 2.00 | Undefined | [0.99697, Infinity] | 0.00000 | 1.99899 | At most 0.05 |
| S082 | Secondary impaired wound healing | 22/989; 26/987 | 0.91 | 0.84444 | [0.80886, 0.88146] | 0.02587 | 0.91382 | At most 0.05 |
| S083 | Secondary unexpected ICU admission/readmission | 41/989; 32/987 | 1.12 | 1.27866 | [1.24238, 1.31613] | 0.10480 | 1.12743 | Above 0.05 |
| S085 | Secondary intraoperative hypoxemia | 49/989; 134/987 | 0.51 | 0.36493 | [0.35950, 0.37041] | 0.26390 | 0.51074 | Above 0.05 |
| S086 | Secondary intraoperative hypotension | 313/989; 170/987 | 1.43 | 1.83745 | [1.82729, 1.84769] | 0.27433 | 1.43123 | Above 0.05 |
| S087 | Secondary intraoperative bradycardia | 98/989; 59/987 | 1.27 | 1.65766 | [1.63369, 1.68206] | 0.28243 | 1.27433 | Above 0.05 |
| S088 | Secondary in-hospital mortality | 12/989; 5/987 | 1.41 | 2.39515 | [2.08457, 2.77497] | 0.47487 | 1.41538 | Above 0.05 |
| S089 | Post hoc rescue strategy for desaturation | 59/989; 166/987 | 0.49 | 0.35470 | [0.35029, 0.35915] | 0.25683 | 0.49371 | Above 0.05 |
| S090 | Post hoc need for vasoactive drugs | 491/989; 439/987 | 1.10 | 1.11619 | [1.11266, 1.11973] | 0.00696 | 1.10892 | At most 0.05 |
| S344 | p.29 PP collapsed primary PPC | 186/917; 209/912 | 0.92 | 0.88510 | [0.87965, 0.89058] | 0.02654 | 0.92374 | At most 0.05 |
| S345 | p.29 PP mild respiratory failure | 119/917; 140/912 | 0.90 | 0.84537 | [0.83790, 0.85289] | 0.04679 | 0.90395 | At most 0.05 |
| S346 | p.29 PP moderate respiratory failure | 38/917; 51/912 | 0.84 | 0.74104 | [0.72339, 0.75905] | 0.09042 | 0.84519 | Above 0.05 |
| S347 | p.29 PP severe respiratory failure | 25/917; 35/912 | 0.83 | 0.71039 | [0.68563, 0.73590] | 0.10734 | 0.82633 | Above 0.05 |
| S348 | p.29 PP ARDS | 3/917; 1/912 | 1.50 | 2.98364 | [1.65577, 6.96945] | 0.10051 | 1.49754 | Above 0.05 |
| S349 | p.29 PP bronchospasm | 11/917; 10/912 | 1.04 | 1.09400 | [0.99346, 1.20524] | 0.00000 | 1.04531 | At most 0.05 |
| S350 | p.29 PP infiltrates | 14/917; 14/912 | 0.99 | 0.99455 | [0.92495, 1.06939] | 0.00000 | 0.99723 | At most 0.05 |
| S351 | p.29 PP infection | 10/917; 9/912 | 1.05 | 1.10505 | [0.99346, 1.22990] | 0.00000 | 1.05031 | At most 0.05 |
| S352 | p.29 PP aspiration | 2/917; 1/912 | 1.33 | 1.98909 | [0.99346, 4.97818] | 0.00000 | 1.33042 | At most 0.05 |
| S353 | p.29 PP pleural effusion | 38/917; 18/912 | 1.37 | 2.09960 | [2.01377, 2.19040] | 0.46626 | 1.36872 | Above 0.05 |
| S354 | p.29 PP atelectasis | 38/917; 50/912 | 0.85 | 0.75586 | [0.73772, 0.77438] | 0.08308 | 0.85528 | Above 0.05 |
| S355 | p.29 PP cardiopulmonary edema | 15/917; 7/912 | 1.36 | 2.13117 | [1.92069, 2.37421] | 0.40860 | 1.36590 | Above 0.05 |
| S356 | p.29 PP pneumothorax | 1/917; 2/912 | 0.66 | 0.49727 | [0.19869, 0.99564] | 0.00000 | 0.66448 | At most 0.05 |

Figure2 additional affected/corroborating locations: S092 nonlaparoscopic79/240 vs74/253,1.09; S093 laparoscopic130/740 vs156/727,.88; S094 BMI<40:76/336 vs94/376,.93; S095 BMI≥40:135/653 vs139/611,.94; S096 SpO2<96:88/317 vs112/342,.88; S097 SpO2≥96:123/672 vs121/645,.99; S098 peripheral32/126 vs25/126,1.16; S099 upper abdominal179/863 vs208/861,.90; S100 waist-to-hip<1:97/467 vs100/457,.97,≥1:98/447 vs112/449,.92; S101 all 211/989 vs233/987,.93. These GLM subgroup entries are retained as model-labelled supporting occurrences.

eFigure12 all twelve component occurrences: S373 mild.92; S374 moderate.83; S375 severe.91; S376 aspiration1.33; S377 bronchospasm1.09; S378 ARDS1.50; S379 infection1.00; S380 atelectasis.88; S381 cardiopulmonary edema1.31; S382 pleural effusion1.36; S383 pneumothorax.50; S384 infiltrates.87. The main corresponding event counts are in the table above. S385 collapsed composite.93 is under an Odds Ratio header; the other three global OR rows are explicit fitted-model quantities and not part of the transposition finding.

### F-NUM-002

**Title:** Abstract hypoxemia upper confidence limit has the opposite sign to its matching table limit.

**Locations and roles:** REPORT [main abstract Results, PDF p1](../../../jama_bluth_2019_oi_190055_16092.pdf#page=1) compared with REPORT [main Table3 hypoxemia, PDF p9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), relation S_W. Relationship S085.

**Printed inputs:** Abstract5.0% vs13.6%, difference−8.6% [95%CI−11.1% to6.1%], P<.001. Table3 same49/989 and134/987, difference−8.6% [95%CI−11.1% to−6.1%], P<.001. The visual PDF image confirms a positive abstract6.1; this is not an OCR-only sign reading.

**Rule and calculation:** Matching outcome/population/contrast, but upper bounds have opposite signs. Abstract upper-limit half-unit interval[6.05,6.15]; table[−6.15,−6.05]. Gap12.10 percentage points; divided by reference magnitude6.1 gives relative1.98361>.05. The abstract interval crosses null0 despite P<.001; the table interval excludes0. The interval-versus-P conflict is independent of display precision under Route A category1.

**Focus area:** B, estimate/test logic and numerical direction. **Proposed review domain:** statistical_results. Relationship S_W, REPORT versus REPORT.

**Qualifying route:** Route A, category2 (printed sign changes significance), and Route A, category1 (abstract interval versus P).

**Affected result or extracted value:** Upper95% limit of the high-minus-low hypoxemia absolute risk difference, and its inferred significance in abstract extraction.

**Why context does not resolve it:** Route A categories1/2 always register this reproduced printed-number/sign conflict. The intended bound may be inferred from the table, but an extractor may still take the positive abstract limit.

**Alternatives:** A missing sign at abstract display is consistent with all remaining values. Distinct analyses are not indicated: printed percentages, contrast estimate, lower limit and P all match.

**Exact human question:** Which signed upper95% confidence limit belongs to the reported hypoxemia risk difference and should be extracted from the abstract?

### F-NUM-003

**Title:** Two binary-outcome confidence intervals exclude the null while their accompanying tests are nonsignificant.

**Locations and roles:** REPORT [main Table3 disseminated intravascular coagulation, PDF p9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), S080; REPORT [main Table3 test footnotes, PDF p10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10); REPORT [support eTable8 per-protocol cardiopulmonary edema, PDF p29](../../../joi190055supp4_prod_16092.pdf#page=29), S355. Each conflict is internal to its own REPORT display; proposed relationship S_W. Main-versus-support documents supply two occurrences of the same interval/test compatibility pattern, not opposing versions of one event result.

**Printed inputs:** DIC high 1(.1%) versus low 0, Risk Ratio2.00(95%CI1.91–2.09), P>.99; absolute difference .1% (−.1 to.3%). PP cardiopulmonary edema15/917(1.6%) versus7/912(.8%), effect 1.36(95%CI1.02–1.82), P .09. eTable8 heading is generic Effect Estimate, not explicitly OR/RR, but its positive multiplicative estimate and source binary-analysis specification establish null1. Main note c attributes P to χ²; main note b labels interval RR from Wald likelihood ratio approximation.

**Rule and calculation:** At95% confidence and two-sided.05, the multiplicative null1 is excluded by DIC[1.91,2.09] and PP edema[1.02,1.82], whereas both associated tests are nonsignificant. For the printed limits, DIC lower rounding interval[1.905,1.915] and PP lower[1.015,1.025] remain above1; P>.99 and.09±.005 remain above .05. Route A category1 does not permit excluding this conflict as rounding. The DIC risk-difference interval includes0, giving another displayed inferential reading. No unreported raw data or inferential convention is needed to reproduce these contradictions.

**Focus area:** B. **Proposed review domain:** statistical_results.

**Qualifying route:** Route A, category1.

**Affected result or extracted value:** DIC relative-effect interval and PP cardiopulmonary-edema effect interval, and the significance readings associated with them.

**Why context does not resolve it:** Route A category1 always registers an interval-versus-test conflict even if distinct inferential procedures are given. Supplied method wording does not state a confidence/test construction explaining opposite null-inclusion decisions.

**Alternatives:** Different interval and hypothesis-test procedures, including asymptotic interval versus sparse-data test, may give different decisions. That is a source-grounded possibility from the named Wald/χ² procedures and sparse event counts; it is recorded for human assessment and does not erase this always-register observation. The effect-definition pattern F-NUM-001 may relate to these intervals, but its diagnostic is not proof of their computational provenance.

**Exact human question:** Which estimand, interval construction and hypothesis test generated each of these paired interval/P entries, and how should a reader interpret their opposing null-inclusion results?

## Excluded observations

Only apparent discrepancies considered and not emitted are listed; ordinary reconciled checks remain in the inventories.

| Location | Observation | Reason code |
|---|---|---|
| Main REPORT Table2p8, S038/S039 | Monitoring632/982(64.9%) and651/984(67.7%); reversal724/982(74.3%) and723/984(75.2%) do not reproduce exact percentages from explicit denominators. Half-unit intervals give relative residuals at most.0212, below.05. The row differences also overlap input precision intervals. | ROUNDING_OR_DISPLAY_PRECISION |
| Main REPORT Table2p7, S001/S003/S005/S018/S020/S023/S026/S027/S029, and Table2p8 S049/S050 | Small differences between printed group means and printed high-minus-low differences fit half-unit input intervals or residual relative gap≤.05. E.g.7.3−7.1 range[.1,.3] overlaps difference.1±.05;12.0−4.0 range[7.9,8.1] overlaps7.9±.05. | ROUNDING_OR_DISPLAY_PRECISION |
| Main REPORT abstractp1 versus Figure1p3, N001 | Abstract describes randomized group n989/n987 while flow randomization is1011/1002. Pairwise half-unit gaps21/989=.02123 and14/987=.01418 are≤.05; nearby complete-case counts identify final analyzed groups. | ROUNDING_OR_DISPLAY_PRECISION |
| Main REPORT abstract/Resultsp1/p4, N009 | Women1381(69.9%) attached to randomized2013 rather than completed1976 would yield68.6041%; even this alternative has relative gap<.05. Abdominal90.1% uses observed incision denominators; no qualifying percentage discrepancy. | ROUNDING_OR_DISPLAY_PRECISION |
| Main REPORT Table1p6, N073 | White blood cells8224/8347 appear under ×10^9/L, whereas immediate clinical-unit interpretation is per microliter; unit annotation apparent discrepancy changes no printed numeral. | NOTATION_OR_TYPOGRAPHY |
| Main REPORT Table2p8, S040–S042/S044 | Some contrasts differ from subtraction of medians (e.g.total fluid medians1.5/1.6 but contrast.02). No source states the contrast is a difference of medians; this discrepancy depends on an unsupported statistic assumption. | CONDITIONAL_OR_UNREPORTED |
| Main REPORT Table1p5 versus Figure2p10, N019/N020 andS094/S095 | BMI category counts differ by1/2 because Table1 includes40 in35–40, while Figure2 includes40 in≥40; each partition reconciles989/987. | CONTEXT_RESOLVES |
| Support REPORT eFigures8/9pp38–39, N320/S369/S370 | Primary/severe plots repeat identical at-risk rows despite different event incidences. Contributor counts at individual times are peripheral; no initial analysis-population size or primary event total conflicts, and endpoint/censoring timing does not supply a required equality. | PERIPHERAL_COMPARISON |
| Support REPORT eFigure11p41, S372 | Caption refers to extra-pulmonary complications, but title, y-axis, mortality parenthetical and5-dayHR1.67 identify mortality at once. | CONTEXT_RESOLVES |
| PLAN amendment DOC-003p1, N312 | Historical June2013 versus June2014 version date is administrative and does not change a supplied planned decision rule. | OUT_OF_FOCUS |
| Support REPORT eTable9p30, S357–S361/S386–S388 | Mixed-effect, proportional-odds and GEE ORs differ from crude event-risk ratios; methods explicitly establish different fitted quantities. | MODEL_VERSUS_CRUDE |

## Limitations

No scientific coverage gap. Raw participant data are not supplied, so fitted adjusted estimands, survival censoring and unlabelled precise graphic coordinates cannot be reconstructed beyond printed information. Historical rendered-image engines are unrecorded; images were used as source locators alongside direct supplied PDF text and source-linked visual reading. Source roles and exact locations are retained; findings remain questions for independent inclusion screening and human adjudication.

