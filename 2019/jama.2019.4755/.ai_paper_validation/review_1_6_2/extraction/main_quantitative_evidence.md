# Main quantitative evidence map

## Scope, provenance, and coverage

Source: DOC-001, `jama_brenner_2019_oi_190039.pdf`, PDF pages 1-7 (printed pages 1686-1692). Document role: REPORT, assigned by content as the final randomized trial report. Complete assigned scope, no sampling. Main-paper numeric relationships use N001-N043; statistical relationships use S001-S049. Relationships group cells where a shared population, time, and contrast applies; every printed result cell is retained below. No candidate selection or scientific judgments are made here.

Locators use PDF pages, section/table/row labels, and columns; all page links below point to the supplied PDF. `source_coverage.md`, `source_inventory.md`, and `evidence_asset_inventory.md` were read before finalizing. They assign all seven main pages reusable-backed, zero fresh-required. Canonical USABLE assets A040-A046, `.ai_paper_validation/document_outputs/doc-799606a72443/normalized_pages/page-1.txt` through `page-7.txt`, were read for full page coverage and all result transcriptions. Earlier native page text A001-A007, `.ai_paper_validation/document_outputs/D01/native_pages/page-1.txt` through `page-7.txt`, was also read in full; it drops many letter `t` glyphs and is PARTIAL, superseded by the canonical layer. Reusable PARTIAL OCR A022 page-5.txt and USABLE rendering A021 page-5.png were used as additional table locators; the page-5 image was inspected for every table cell and the blank Men third-row test label in Table 3. OCR loses some count cells, so canonical native text plus image, rather than OCR alone, supplies the values. Engines: reusable Poppler native text (historical version not recorded); reusable historical PDF rasterization (version not recorded) and RapidOCR ONNX Runtime CPU as recorded in the evidence-asset inventory; no new OCR or rendering performed by this mapper. Compute device: CPU.

| Unit | Result-relevant scope | Coverage |
|---|---|---|
| PDF p1 | Abstract design, population, intervention, endpoints, all printed results, conclusion | COMPLETE |
| PDF p2 | Key Points; outcome and population definitions; sample schedule; allocation context | COMPLETE |
| PDF p3 | Randomization; sampling; endpoints; power; analysis methods; all narrative counts | COMPLETE |
| PDF p4 | Figure, Table 1, primary/secondary narrative, adverse events | COMPLETE |
| PDF p5 | Every Table 2 and Table 3 cell and footnote; site sensitivity analysis; conclusion | COMPLETE |
| PDF p6 | Numerical design/limitation and conclusion statements | COMPLETE |
| PDF p7 | Funding, acknowledgments, data-sharing pointer, references | COMPLETE; no applicable current-trial result relationship |

Bibliographic page numbers, reference citation numbers, grant-free administrative addresses, and numerical results attributed solely to other studies are not current-trial result relationships. The p2 background gives approximately 860000 annual worldwide CRC deaths, FIT CRC sensitivity 70%-80%, specificity >90%; these are context, not trial outputs. The p7 reference titles and bibliographic numbers were inspected and contain no additional current-trial results.

## Numeric/reporting relationship inventory

A = aspirin; P = placebo. Unless otherwise stated A/P ordering is consistent. Counts are participants unless a sample/event unit is named. A computed denominator is explicitly labeled derived rather than printed.

| ID | Exact location | Printed quantities, labels, units, and matching context |
|---|---|---|
| N001 | [p1 abstract Design/Interventions/Results](../../../jama_brenner_2019_oi_190039.pdf#page=1); p2 Key Points; p3 Results; p4 Figure | 2422 randomized/recruited; A 1208, P 1214; adult age 40-80 years; mean [SD] age 59.6 [7.9] years; 1219 men (50%) in abstract's randomized-patient sentence. p3 states trial-population mean age 59.6. A single 300-mg aspirin tablet versus placebo, 2 days before scheduled primary fecal sampling. |
| N002 | p1 abstract Design; [p2 Trial Design and Trial Population](../../../jama_brenner_2019_oi_190039.pdf#page=2) | 14 gastroenterology practices + 4 hospitals; 18 centers; enrollment June 2013-November 2016; final follow-up January 27, 2017 (abstract). No recent aspirin/other antithrombotic medications. CRC or advanced adenoma defined as adenoma >=1 cm, tubulovillous/villous component, or high-grade dysplasia. |
| N003 | p1 abstract Results; [p3 Results](../../../jama_brenner_2019_oi_190039.pdf#page=3) | 2134 included in analysis; p3 288 dropped out/excluded. 78% primary screening/22% diagnostic colonoscopy in abstract; p3 78% screening. Advanced neoplasms 224 (10.5%), CRC 8 (0.4%), advanced adenoma 216 (10.1%). p3 93.6% ages 45-74. Matched with N019-N022 and Figure N006-N009. |
| N004 | p2 Trial Design; p3 Laboratory Methods/Outcomes | 2 FITs; 4 kits for each test; baseline then samples scheduled 2, 3, 4 days after medication, 1 sample per scheduled day, 4 overall; later-day postponement allowed; samples before bowel preparation; colonoscopy within 3 months of recruitment. Storage 2-8 degrees C; shipping median 4 days, IQR 3-5 days; quantitative analytic range 0.03-142 micrograms Hb/g feces. |
| N005 | p3 Randomization | Randomized block design: each block 20 tablets, 10 assigned to each group; aspirin 300 mg, no enteric coating; placebo cellulose/lactose monohydrate/magnesium stearate. Two independent blinded colonoscopy/histology reviewers. |
| N006 | [p4 Figure, top and allocation boxes](../../../jama_brenner_2019_oi_190039.pdf#page=4) | 2422 randomized; A1208 ->1131 received as randomized, 77 did not receive or dropped out; P1214 ->1153 received as randomized, 61 did not receive or dropped out. Each arm's received count is also underwent-colonoscopy count: A1131/P1153. Eligibility-assessed count not collected (footnote a). |
| N007 | p4 Figure, aspirin analysis/exclusion box | A1075 included; 56 excluded from primary analysis: 32 no stool samples, 2 samples sent after colonoscopy, 20 history of blood in stool, 2 aspirin takers. |
| N008 | p4 Figure, placebo analysis/exclusion box | P1059 included; 94 excluded from primary analysis: 56 no stool samples, 30 history of blood in stool, 5 history of CRC, 3 aspirin takers. |
| N009 | p4 Figure footnotes b/c; p3 Statistical Analyses | Those with no sample or information considered dropouts; completed colonoscopy considered followed up. Withdrawn consent or no samples/information excluded; no precolonoscopy samples excluded from primary analysis. Figure totals map to N001/N003 without silently changing the populations. |
| N010 | p4 Table 1 header and Sex | A n=1075/P n=1059; Men 547 (50.9)/528 (49.9); Women 528 (49.1)/531 (50.1). |
| N011 | p4 Table 1 Age <45 y | A26 (2.4)/P30 (2.8). |
| N012 | p4 Table 1 Age 45-49 y | A63 (5.9)/P52 (4.9). |
| N013 | p4 Table 1 Age 50-54 y | A165 (15.3)/P164 (15.5). |
| N014 | p4 Table 1 Age 55-59 y | A315 (29.3)/P318 (30.0). |
| N015 | p4 Table 1 Age 60-64 y | A232 (21.6)/P216 (20.4). |
| N016 | p4 Table 1 Age 65-69 y | A144 (13.4)/P153 (14.4). |
| N017 | p4 Table 1 Age 70-74 y | A92 (8.6)/P83 (7.8). |
| N018 | p4 Table 1 Age >=75 y | A38 (3.5)/P43 (4.1). All age bins cross-reference N003 93.6% aged45-74 and N001 mean age. |
| N019 | p4 Table 1 Primary indication and footnote a | Screening A805 (77.9)/P794 (78.2); diagnostic A228 (22.1)/P221 (21.8); missing indication A42/P44. Printed arm headers n1075/1059; nonmissing derived denominators 1033/1015. |
| N020 | p4 Table 1 Most advanced finding: CRC | A3 (0.3)/P5 (0.5), totals connect to abstract/body 8 CRC. |
| N021 | p4 Table 1 Most advanced finding: advanced adenoma | A112 (10.4)/P104 (9.8); totals connect to 216 adenoma and 224 advanced neoplasms including CRC. |
| N022 | p4 Table 1 Most advanced finding: nonadvanced adenoma and none | Nonadvanced adenoma A286 (26.6)/P280 (26.4); none of above A674 (62.7)/P670 (63.3). Four mutually labeled finding rows refer to most advanced finding. |
| N023 | p3 Results paragraph referring to eTable2 | Day2 scheduled valid quantitative samples A1030 (95.8%)/P1012 (95.6%); qualitative A974 (90.6%)/P969 (91.5%). Match N024-N032 confusion counts by test and schedule; group populations1075/1059. |
| N024 | [p5 Table2 all, quantitative10.2](../../../jama_brenner_2019_oi_190039.pdf#page=5) | A TP45 FN67 TN755 FP163; P TP31 FN71 TN807 FP103. Derived disease denominators112/102, disease-negative918/910, totals1030/1012. S001/S002. |
| N025 | p5 Table2 all, quantitative17.0 | A TP32 FN80 TN842 FP76; P TP23 FN79 TN863 FP47. Derived denominators112/102 and918/910, totals1030/1012. S003/S004. |
| N026 | p5 Table2 all, qualitative10.2 | A TP35 FN66 TN732 FP141; P TP22 FN78 TN798 FP71. Derived disease denominators101/100, disease-negative873/869, totals974/969. S005/S006. |
| N027 | p5 Table2 men, quantitative10.2 | A TP33 FN44 TN360 FP90; P TP15 FN39 TN387 FP68. Derived disease77/54; disease-negative450/455; totals527/509. S007/S008. |
| N028 | p5 Table2 men, quantitative17.0 | A TP25 FN52 TN408 FP42; P TP13 FN41 TN424 FP31. Derived disease77/54; disease-negative450/455; totals527/509. S009/S010. |
| N029 | p5 Table2 men, qualitative10.2 | A TP28 FN43 TN354 FP74; P TP12 FN43 TN400 FP48. Derived disease71/55; disease-negative428/448; totals499/503. S011/S012. |
| N030 | p5 Table2 women, quantitative10.2 | A TP12 FN23 TN395 FP73; P TP16 FN32 TN420 FP35. Derived disease35/48; disease-negative468/455; totals503/503. S013/S014. |
| N031 | p5 Table2 women, quantitative17.0 | A TP7 FN28 TN434 FP34; P TP10 FN38 TN439 FP16. Derived disease35/48; disease-negative468/455; totals503/503. S015/S016. |
| N032 | p5 Table2 women, qualitative10.2 | A TP7 FN23 TN378 FP67; P TP10 FN35 TN398 FP23. Derived disease30/45; disease-negative445/421; totals475/466. S017/S018. |
| N033 | p5 Table2 caption/header/footnote | Detecting advanced neoplasms at day2 after single300-mg dose or placebo; intention-to-screen. TP=true-positive; FN=false-negative; TN=true-negative; FP=false-positive; Hb=hemoglobin. Cutoff units micrograms Hb/g, 10.2 and17.0 quantitative,10.2 qualitative. Sensitivity=TP/(TP+FN), specificity=TN/(TN+FP) are relationship reconstruction definitions, not verbatim equations in source. |
| N034 | p5 Table3 caption/header/footnote | PPV and NPV for same advanced-neoplasm/day2/intention-to-screen setting; PPV=TP/(TP+FP), NPV=TN/(TN+FN) used as reconstruction keys from matching Table2 counts. Caption labels positive and negative predictive values, column difference95%CI; no individual-value CIs or P values printed. Men third-row Test cell is blank in source image, cutoff10.2; sequence and matching Table2 counts locate qualitative test; blank label retained. |
| N035 | p4 Secondary End Points, multiple-day paragraph | Combining positivity on >=1 sample among up to3 samples scheduled days2,3,4 gives higher sensitivity/lower specificity in both arms, little change in between-arm sensitivity differences. No numerical cells here; pointer eTable3. |
| N036 | p4 Secondary End Points, per-protocol paragraph | Samples actually collected exactly2 days posttablet; men sensitivity differences23.2 pp (95%CI5.0 to39.5) at quantitative lower cutoff and22.5 pp (4.5 to38.6) for qualitative test. Specificity differences described as similar to intention-to-screen. eTable4 pointer. S045. |
| N037 | p4 Secondary End Points, PPV/NPV paragraph | Table3 and eTable5 provide PPV/NPV day2; overall no significant differences, neither intention-to-screen nor per-protocol. S046 retains inference wording against Table3. |
| N038 | p4 Adverse Events | Aspirin11 adverse events in7 participants,2 serious events in2 participants requiring hospitalization (acute appendicitis; acute suppurative cholangitis accompanied by acute kidney injury), considered unrelated to trial drug. Placebo6 adverse events in5 participants;0 serious events reported. All recovered completely. No rates or denominators printed for events. |
| N039 | p6 Discussion and Limitations | Designed for24% absolute sensitivity increase; not powered for smaller differences. Primary analysis sample sizes reduced approximately4% due to exclusions; diagnostic colonoscopy22%. This preserves the stated population/quantity labels, rather than assigning a denominator to the4% phrase. |
| N040 | p6 Discussion dose and timing | Trial300 mg; possible future75 mg/100 mg discussed as research options, not randomized interventions. Primary analysis2 days; multiple-day collection described as not improving diagnostic performance. |
| N041 | p1 abstract; p2 Key Points; p5 Discussion; p6 Conclusions | Repeated main conclusion: single aspirin dose versus placebo did not significantly increase quantitative FIT sensitivity at2 predefined cutoffs among adults40-80 without aspirin/antithrombotic medication use. Match S001/S003. |
| N042 | p2 Trial Design/p3 Outcomes | Quantitative test FOB Gold Tube Screen; qualitative FD Hb/Hp Complex quick. Quantitative17-microgram cutoff manufacturer-defined;10.2 cutoff of qualitative test. Both quantitative cutoffs primary. Stool/feces terms and units retained as matching keys. |
| N043 | p3 Statistical Analyses/p5 Tables2-3 | Analysis by randomized group; main intention-to-screen based on scheduledday2; prespecified per-protocol based on actualday2. Sex-specific analyses secondary; qualitative diagnostic outcomes secondary; no reassignment of primary population from the table captions. |

## Complete statistical result cells

Every effect below is the aspirin minus placebo difference. Sensitivity/specificity/PPV/NPV values are percentages and differences percentage points. Intervals are printed95% confidence intervals. The quantitative day2 sensitivity rows are primary; specificity, qualitative test, sex-specific, predictive-value, combined-sample, and per-protocol outcomes are reported secondary/exploratory as detailed in S039/S042. Tables2-3 report no P values; P values elsewhere are listed only for the correctly matched rows. Inferential methods applicable to these rows are S037-S043. All table rows are PDF p5.

| ID | Exact row/outcome | A value | P value | Difference (95%CI) | Printed test/matched narrative |
|---|---|---:|---:|---|---|
| S001 | Table2 all quantitative10.2 sensitivity, N024 |40.2|30.4|9.8 (-3.1 to22.2)|p1 abstract,p2 KeyPoints,p3-4 Primary End Point: P=.14; p2 KeyPoints nonsignificant |
| S002 | Table2 all quantitative10.2 specificity,N024 |82.2|88.7|-6.4 (-9.6 to-3.2)|p4 Secondary End Points P<.001 |
| S003 | Table2 all quantitative17.0 sensitivity,N025 |28.6|22.5|6.0 (-5.7 to17.5)|p1 abstract,p2 KeyPoints,p4 Primary End Point P=.32 |
| S004 | Table2 all quantitative17.0 specificity,N025 |91.7|94.8|-3.1 (-5.4 to-0.8)|p4 Secondary End Points P=.008 |
| S005 | Table2 all qualitative10.2 sensitivity,N026 |34.7|22.0|12.7 (0.1 to24.7)|p4 Secondary End Points P=.048, higher by12.7 pp |
| S006 | Table2 all qualitative10.2 specificity,N026 |83.8|91.8|-8.0 (-11.0 to-4.9)|p4 Secondary End Points P<.001, lower by8.0 pp |
| S007 | Table2 men quantitative10.2 sensitivity,N027 |42.9|27.8|15.1 (-1.6 to30.6)|p4 male-direction narrative; no row P printed |
| S008 | Table2 men quantitative10.2 specificity,N027 |80.0|85.1|-5.1 (-10.0 to-0.1)|p4 male-direction narrative; no row P printed |
| S009 | Table2 men quantitative17.0 sensitivity,N028 |32.5|24.1|8.4 (-7.5 to23.3)|p4 lower end of male sensitivity range |
| S010 | Table2 men quantitative17.0 specificity,N028 |90.7|93.2|-2.5 (-6.1 to1.1)|p4 lower-magnitude end of male specificity decrease range |
| S011 | Table2 men qualitative10.2 sensitivity,N029 |39.4|21.8|17.6 (1.3 to32.6)|p4 upper end of male sensitivity range |
| S012 | Table2 men qualitative10.2 specificity,N029 |82.7|89.3|-6.6 (-11.2 to-2.0)|p4 upper-magnitude end of male specificity decrease range |
| S013 | Table2 women quantitative10.2 sensitivity,N030 |34.3|33.3|1.0 (-19.1 to21.4)|p4 women sensitivity described as similar |
| S014 | Table2 women quantitative10.2 specificity,N030 |84.4|92.3|-7.9 (-12.0 to-3.8)|p4 women specificity described as lower |
| S015 | Table2 women quantitative17.0 sensitivity,N031 |20.0|20.8|-0.8 (-17.9 to17.2)|p4 women sensitivity described as similar |
| S016 | Table2 women quantitative17.0 specificity,N031 |92.7|96.5|-3.7 (-6.7 to-0.8)|p4 women specificity described as lower |
| S017 | Table2 women qualitative10.2 sensitivity,N032 |23.3|22.2|1.1 (-17.7 to20.9)|p4 women sensitivity described as similar |
| S018 | Table2 women qualitative10.2 specificity,N032 |84.9|94.5|-9.6 (-13.5 to-5.5)|p4 women specificity described as lower |
| S019 | Table3 all quantitative10.2 PPV,N024 |21.6|23.1|-1.5 (-10.7 to7.4)|p4 overall no significant PPV/NPV differences |
| S020 | Table3 all quantitative10.2 NPV,N024 |91.8|91.9|-0.1 (-2.7 to2.5)|same narrative; no P printed |
| S021 | Table3 all quantitative17.0 PPV,N025 |29.6|32.9|-3.2 (-17.2 to10.5)|same narrative; no P printed |
| S022 | Table3 all quantitative17.0 NPV,N025 |91.3|91.6|-0.3 (-2.8 to2.3)|same narrative; no P printed |
| S023 | Table3 all qualitative10.2 PPV,N026 |19.9|23.7|-3.8 (-14.4 to6.5)|same narrative; no P printed |
| S024 | Table3 all qualitative10.2 NPV,N026 |91.7|91.1|0.6 (-2.1 to3.3)|same narrative; no P printed |
| S025 | Table3 men quantitative10.2 PPV,N027 |26.8|18.1|8.8 (-3.0 to19.8)|no P printed |
| S026 | Table3 men quantitative10.2 NPV,N027 |89.1|90.8|-1.7 (-5.9 to2.4)|no P printed |
| S027 | Table3 men quantitative17.0 PPV,N028 |37.3|29.5|7.8 (-10.3 to24.8)|no P printed |
| S028 | Table3 men quantitative17.0 NPV,N028 |88.7|91.2|-2.5 (-6.4 to1.4)|no P printed |
| S029 | Table3 men third row10.2 PPV,N029; Test cell blank |27.5|20|7.5 (-6.4 to20.2)|no P printed; blank source label retained |
| S030 | Table3 men third row10.2 NPV,N029; Test cell blank |89.2|90.3|-1.1 (-5.3 to3.0)|no P printed |
| S031 | Table3 women quantitative10.2 PPV,N030 |14.1|31.4|-17.3 (-31.8 to-2.5)|no P printed |
| S032 | Table3 women quantitative10.2 NPV,N030 |94.5|92.9|1.6 (-1.7 to4.8)|no P printed |
| S033 | Table3 women quantitative17.0 PPV,N031 |17.1|38.5|-21.4 (-42.2 to0.8)|no P printed |
| S034 | Table3 women quantitative17.0 NPV,N031 |93.9|92|1.9 (-1.4 to5.2)|no P printed |
| S035 | Table3 women qualitative10.2 PPV,N032 |9.5|30.3|-20.8 (-37.8 to-4.0)|no P printed |
| S036 | Table3 women qualitative10.2 NPV,N032 |94.3|91.9|2.3 (-1.1 to5.8)|no P printed |

## Statistical method, decision, and narrative relationships

| ID | Exact source location | Complete source-grounded method/design/result relationship |
|---|---|---|
| S037 | p3 Sample Size and Power Calculations; p6 Discussion/Limitations | Assumed advanced-neoplasm prevalence10%;90% power,2-sided alpha=.05; day2 sensitivity60% versus36%, difference24 percentage points. No explicit target total sample size is printed in this subsection. p6 repeats24% absolute increase and limits interpretation of smaller effects. |
| S038 | p3 Statistical Analyses | Analyzed according to randomized group; consent withdrawals/no sample or information excluded; no precolonoscopy stool samples excluded from primary analysis. Scheduledday2 intention-to-screen; actualexactlyday2 prespecified per-protocol. Relate to Figure counts N006-N009 and valid diagnostic denominators N023-N032. |
| S039 | p3 Outcomes | Primary quantitative sensitivity at17 and10.2 micrograms Hb/g feces, scheduledday2; secondary quantitative specificity/PPV/NPV, gain from combining >=1 positive sample among days2-4, qualitative sensitivity/specificity/PPV/NPV, sex-specific diagnostic measures of both tests, serious adverse events. Further secondary likelihood ratios and area under curve explicitly not reported in article. |
| S040 | p3 Statistical Analyses | Wald-adjusted CIs for sensitivity and specificity: Agresti-Coull adjustment. Differences: Agresti-Caffo adjustment, PropCIs package. R3.4.0. Individual sensitivity/specificity CIs are not displayed in main Table2; difference95%CIs are. Main Table3 has difference95%CIs; the method sentence explicitly names sensitivity and specificity, not a separate PPV/NPV method. |
| S041 | p3 Statistical Analyses; p4 sex paragraph | Interaction P values from generalized linear model fitted to binomial data. p4 interaction between sex and intervention all statistically nonsignificant, range .08-.49. Individual interaction P values and coefficients not printed in main article. Do not assign range endpoints to specific outcomes. |
| S042 | p3 Statistical Analyses | Statistical significance defined2-sidedP<.05. No multiple-testing adjustments; secondary-outcome analyses regarded exploratory. Matched tests S001-S006 haveP=.14,<.001,.32,.008,.048,<.001 respectively. No specific test statistic/SE or explicit P-value computation formula printed for these rows. |
| S043 | p3 Sensitivity Analysis; p5 Sensitivity Analysis | Each outcome of main intention-to-screen analysis: generalized linear mixed model with random intercept for site via lme4. Likelihood-ratio test for null random-intercept variance0. p5 reports P .16-.50, never statistically significant; model without random intercept retained. No outcome-specific values in main article; eTable6 pointer. |
| S044 | p4 Secondary End Points, sex paragraph | Men sensitivity higher by8.4 (95%CI-7.5 to23.3) through17.6 (1.3 to32.6) pp; specificity lower by2.5 (95%CI-6.1 to1.1) through6.6 (-11.2 to-2.0) pp. Women sensitivity similar, specificity lower. Link each row to S007-S018, retain sign conventions for difference versus magnitude of decrease. |
| S045 | p4 Secondary End Points, per-protocol paragraph | Compared with intention-to-screen, men's sensitivity difference greater: quantitative10.2 +23.2 pp (5.0 to39.5); qualitative +22.5 pp (4.5 to38.6), actualday2. Specificity differences similar. No per-protocol row counts or arm-specific sensitivities printed in article narrative; those remain supplied supplement scope. |
| S046 | p4 Secondary End Points, PPV/NPV paragraph | Overall no significant differences in predictive values in intention-to-screen or per-protocol. Matched main overall rows S019-S024; sex-specific rows S025-S036 separately retained without assigning overall wording to them. |
| S047 | p4 Secondary End Points, multi-sample paragraph; p6 Discussion | >=1 positive among up to3 samples days2-4: sensitivities higher and specificities lower in both arms, little change in between-arm sensitivity differences. p6 says sensitivity analyses do not suggest multiple-day fecal sampling improves diagnostic performance. No numerical main-article values to append. |
| S048 | p1 Conclusions; p2 Key Points; p5 Discussion; p6 Conclusions | Main statistical conclusion no significant increase in primary quantitative sensitivity at2 predefined cutoffs; match S001/S003 and their CIs/P values. Scope adult40-80 without recent aspirin/antithrombotics, single oral dose. |
| S049 | p6 Limitations | Secondary analyses multiple without adjustment; reduced primary-analysis sample sizes approximately4% due to exclusions; stated unrelated to treatment group; sensitivity samples limited by low advanced-neoplasm prevalence. The4% claim is retained as printed without inferring whether denominator is valid tests, randomized participants, or postcolonoscopy analysis group. No additional numerical estimate/CI/test supplied. |

## Reconstruction keys and remaining data boundaries

Table2 count rows provide all numerators and denominators for sensitivity, specificity, PPV, and NPV. Quantitative thresholds share within-arm disease and disease-negative denominators; sex strata supply component counts for the all-participant row. Qualitative and quantitative samples have different valid-sample totals; Table1 colonoscopy findings use the entire analyzed population rather than valid-test subsets. No person-time rates, hazard/odds/risk ratios, mean differences, reported standard errors, or test statistics occur in current-trial results. Means/SD and shipping median/IQR are preserved in N001/N004. Figures consist solely of the participant-flow display; there are no graphical outcome axes to map. Every assigned direct-source page is mapped: 7 total, 7 reusable-backed, 0 fresh-required, 7 mapped. No scientific coverage gaps remain. The curator's durable inventory confirms reuse eligibility; historical extraction character corruption and OCR cell omissions are locator limitations closed by the USABLE normalized native layer and image.
