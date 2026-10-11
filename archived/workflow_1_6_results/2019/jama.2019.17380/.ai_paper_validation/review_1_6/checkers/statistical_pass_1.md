# Workflow 1.6 statistical pass 1

Lossless assembly of disjoint fresh specialist shards; original parts remain preserved. Source paths are rebased to this canonical artifact.


# Statistical pass 1 — main article and historical plan checker

- Runtime task: /root/stats_pass1_main_plan; fresh qc16_statistical_consistency_reviewer, gpt-6.1-sol/high, FRESH_SPAWN. Coordinator records exact runtime ID.
- Exact registered scope: S001-S120 in statistics/parts/pass1_main_plan_inventory.md, each PASS_1_COMPLETE. The 120-relationship context bound caused an explicit additional PLAN shard, never a finding limit.
- Relationship count: 120. Local candidate count: 6. These are discovery records, not stable C IDs or adjudications.
- Sources: DOC-001 REPORT; DOC-002 PLAN, including historical background; DOC-003 REPORT. No old candidates/checks/reports or external evidence used.
- Engines: direct Poppler 26.01.0 pdftotext; supplied source-matched renders plus fresh Poppler protocol pp5/9 renders inspected visually. No Python extraction, OCR, installation or GPU required.

## Pass1 coverage and results

S001-S024 independently cover every Table2 marginal estimate/CI, within-arm change/CI and contrast/CI; each of the two year5 P values is paired to its actual contrast. S025-S048 cover every Table3 incidence estimate/CI, incidence difference/CI and CoxHR/CI/P. All point estimates lie within printed ordered intervals. Absolute differences use zero; HR uses one. Rates retain /100person-years, not percentage or event counts. Tables2/3 labels are coherent. Primary abstract p1, key-points p2 and narrative p4 repeat the year5 estimates/intervals without a new numerical mismatch. Narrative composite HRs match Table3.

S049-S074 cover all26 Figure3/4 graphical estimates/95%CIs individually: all points inside drawn intervals; all intervals cross zero; positive differences favor active assignment; negative differences favor placebo. S075-S084 cover10 independent subgroup/assignment interaction tests. The D-by-O P=.42 repeats in narrative and both figures and is one matched test. All interaction Ps exceed.05 and agree with no statistically significant heterogeneity. No individual-effect CI is used to infer an interaction P.

S085-S090 cover overall full/complete-case eGFR change intervals, two marker-treatment tests and overall geometric ACR mean intervals. S091-S094 cover two QC and two biomarker-eGFR correlations. Correlation range/sign checks are coherent. Before/after calibration r=.999 is compatible with positive affine transformations and does not establish identity agreement by itself. The QC image explicitly distinguishes offset before calibration and identity agreement after. Correlation analytic N/CI/P absent; no exact nonsignificance calculation invented.

S095-S104 cover all10 historical PLAN Figure2 rate/interval arrows, not nine. S105-S113 cover every historical Figure7 study, Combined and Overall estimate/CI and Overall P=.01. Study/Combined intervals cross zero; Overall interval is negative and P=.01/narrative significant agree directionally. Effect measure and model are not supplied: do not interpret negative estimates as risk or hazard ratios. S114-S118 cover all printed historic Italian/Japanese/paricalcitol test relations in pp7/8; shared P<.001 in three-arm dose trial is not allocated to invented pairwise tests. S119 retains main historical2.1 eGFR attenuation without absent CI/P. S120 retains main sample/power relation matching amended plan, separate from original4-year power.

Detailed missing definitions L1-L17 are in the inventory and apply explicitly to each row. Exact CI-P-statistic compatibility requires supplied consistent model/test/sidedness/variance/df. Main mixed model and imputation definitions are supplied but no exact Rubin df/SE; Cox nullHR1/model supplied but variance/test construction absent. This is a limitation, not a candidate. No diagnostic approximation replaced a reported test.

Rounding checks: Table2 D year5 rounded changes -12.3-(-13.1)=0.8 versus modeled difference0.9 can reconcile with up to0.05 rounding per displayed change; both are separately modeled quantities. O year2 -5.7-(-5.5)=-0.2 versus-0.3 has overlapping rounding windows and no candidate. Table3 O composite rates2.7-2.5=0.2 versus difference0.3 likewise has overlap: unrounded difference can be[0.10,0.30], while displayed0.3 represents[0.25,0.35]. A CoxHR is not required to equal the crude displayed incidence-rate ratio.

Boundary non-candidate: Table3 D ACRdoubling HR1.34 [1.00,1.80], P=.05, and narrative “none differed significantly” are compatible with a true lower CI rounded to1.00 and P rounded to.05. No independent contradiction is supplied by rounding alone. No exact boundary classification or replacement P prescribed.

DISPLAY_ZERO_NOT_CANDIDATE exclusion applied; no P=0/p=0.000 occurs in assigned scope. Very small printed inequalities remain as supplied; no reconstructed tail probability used to criticize formatting.

## STAT-MP01 — Figure3 overall assignment counts conflict with randomized intervention identities

**Candidate statement:** Figure3 places703 participants under Placebo and609 under Vitamin D, while supplied randomized arms imply vitaminD703 and placebo609. This count assignment conflicts with the figure's displayed treatment labels.
**Primary category:** Denominator, proportion, or total inconsistency.
**Compared locations and document roles:** REPORT [DOC-001 Figure3 PDFp8](../../../jama_de_boer_2019_oi_190122.pdf#page=8) overall N and headers versus REPORT [DOC-001 abstract PDFp1](../../../jama_de_boer_2019_oi_190122.pdf#page=1) four randomized arms; corroborating REPORT Table2 p8 active/placebo year5 changes.
**Source evidence:** Figure3 Placebo N703, meanchange-13.1(SD14.4); VitaminD N609, change-12.3(SD14.8). Abstract D+O370,D+placebo333,placebo+O289,doubleplacebo320.
**Calculation/rule:** ActiveD370+333=703; Dplacebo289+320=609. Count printed under placebo exceeds the entire randomized Dplacebo population by94; both overall printed Ns are reversed. Count tolerance zero. Right-hand change-12.3 matches Table2 activeD, so changing both whole-column treatment labels would create a different mean-label conflict.
**S relationships:** S049-S063; the directly registered count contradiction is overall S049. Remaining subgroup counts require exact numeric-lane comparator support before separate registration; do not infer subgroup denominators.
**Alternatives and missing inputs:** Missing source model output does not erase randomized population identity. N may have been placed under wrong headers; raw output would establish intended labels. No claim about fitted CI computation or effect conclusion.
**Human question:** Which assignment populations do the Figure3 N columns represent, and were count columns placed under the wrong treatment labels?
**Classification information:** REPORT versus REPORT inside main; S_W. No PLAN comparator. Pending Human Adjudication.

## STAT-MP02 — Figure4 overall assignment counts conflict with randomized intervention identities

**Candidate statement:** Figure4 places659 participants under Placebo and653 under Omega-3 Fatty Acids, while randomized arms imply activeomega3=659 and omega3placebo=653.
**Primary category:** Denominator, proportion, or total inconsistency.
**Compared locations and document roles:** REPORT [DOC-001 Figure4 PDFp9](../../../jama_de_boer_2019_oi_190122.pdf#page=9) versus REPORT [DOC-001 abstract PDFp1](../../../jama_de_boer_2019_oi_190122.pdf#page=1) randomized arms; REPORT Table2 p8 corroborates displayed meanchange treatment identity.
**Source evidence:** Overall Placebo659/-13.1(SD14.8); Omega3 653/-12.2(SD14.5).
**Calculation/rule:** ActiveO370+289=659; Oplacebo333+320=653. Figure placeboN exceeds entire randomized Oplacebo count by6; Ns reversed. Zero count tolerance. Means remain in intended Table2 placebo/active order.
**S relationships:** S064-S074; directly contradicted overall record S064. Distinct figure/population/values from STAT-MP01, so not automatically merged for a shared apparent cause.
**Alternatives and missing inputs:** Source model output absent; erroneous N placement is plausible but not adjudicated. Whole-column header swap would reverse correct meanchanges.
**Human question:** Which assignment populations do Figure4 N columns denote?
**Classification information:** REPORT versus REPORT within main; S_W. Pending Human Adjudication.

## STAT-MP03 — Omega3 correlation x-axis names DHA/EPA while matched result defines sum percentage index

**Candidate statement:** eFigure1 describes omega-3 index changes but labels its right x-axis “Change in DHA/EPA (Year2-BL)”; the main Methods explicitly defines the omega-3 index as EPA plus DHA as a percentage of total fatty acids. A ratio label and a sum percentage index denote different measures.
**Primary category:** Measure, label, or scale inconsistency.
**Compared locations and document roles:** REPORT [DOC-003 eFigure1 PDFp17](../../../joi190122supp2_prod.pdf#page=17) caption and right-axis label versus REPORT [DOC-001 Methods PDFp3](../../../jama_de_boer_2019_oi_190122.pdf#page=3) omega-3 index definition and REPORT [DOC-001 Results PDFp4](../../../jama_de_boer_2019_oi_190122.pdf#page=4) narrative correlation.
**Source evidence:** eFigure1 caption names changes in omega-3 index; right correlationr=-.02, x-axis DHA/EPA without percentage units. Main definition: EPA plusDHA as%totalfattyacids.
**Calculation/rule:** DHA/EPA is a quotient if slash is mathematical; index=100*(EPA+DHA)/(totalfattyacids). These expressions are not identical. No numerical transform or p-value recalculated.
**S relationships:** S094.
**Alternatives and missing inputs:** Slash may be shorthand listing two constituents rather than division; supplied plotting code/data do not settle the intended variable. Consequently the registered issue is a conditional measure-label inconsistency, not a claim r itself is wrong.
**Human question:** Does the right panel plot the omega-3 percentage index change or a DHA-to-EPA ratio change, and was the slash intended as listing shorthand?
**Classification information:** S_C for main definition versus results-supplement axis; S_W for supplement caption versus its axis. Primary precedence S_C; all relationships S_C,S_W. Both documents REPORT. Pending Human Adjudication.

## STAT-MP04 — Figure2 quartile border order conflicts with increasing vertical scales

**Candidate statement:** Figure2 caption says top and bottom borders show first and third quartiles respectively, but each vertical axis increases upward and the first quartile cannot exceed the third.
**Primary category:** Measure, label, or scale inconsistency.
**Compared locations and document roles:** REPORT [DOC-001 Figure2 PDFp7](../../../jama_de_boer_2019_oi_190122.pdf#page=7), caption “top and bottom box borders indicate the first and third quartiles, respectively” versus increasing eGFR axes0-to200 and increasing urineACR log axes0.1-to10000 on the same source page.
**Calculation/rule:** Q1<=median<=Q3, monotone vertical scale; top border>=bottom border. Assigning top=Q1 and bottom=Q3 reverses displayed order except for a zero-height box, whereas the printed boxes have nonzero height. No exact quartile coordinates invented.
**S relationship:** None; descriptive boxplot/IQR relationship retained for numeric-lane cross-reference, not mislabeled inferentialCI.
**Alternatives and missing inputs:** Caption word order may be transposed. Exact quartiles are absent but are not needed for the order rule; logarithmic ACR scale remains monotonic.
**Human question:** Which quartile was intended for each box border in Figure2?
**Classification information:** S_W, REPORT within main. Pending Human Adjudication.

## STAT-MP05 — Figure2B omega3 eGFR participant rows repeat vitaminD rows

**Candidate statement:** Figure2B labels omega3/placebo eGFR contributor counts as the vitaminD counts rather than the matched omega3 counts in Table2.
**Primary category:** Denominator, proportion, or total inconsistency.
**Compared locations and document roles:** REPORT [DOC-001 Figure2 PDFp7](../../../jama_de_boer_2019_oi_190122.pdf#page=7) PanelB versus REPORT [DOC-001 Table2 PDFp8](../../../jama_de_boer_2019_oi_190122.pdf#page=8), omega3 rows, matching measured eGFR by assignment and baseline/year2/year5.
**Source evidence:** PanelB printed placebo607,459,438; omega3 701,531,496. Table2 omega3 placebo651,491,462; active657,499,472. PanelA vitaminD counts exactly match PanelB's repeated values.
**Calculation/rule:** PanelB active-minus-Table2 discrepancy44,32,24 and placebo discrepancy-44,-32,-24 across three times. Count tolerance zero; same measure/time/source cannot be matched by rounding. Baseline active701 exceeds randomized omega3active659.
**S relationships:** Table2 measured mean/CI S013-S016,S020-S021 supply the matched count-population context; boxplot is descriptive and needs numeric-lane ID.
**Alternatives and missing inputs:** Counts might have been copied across panels; graph plotting/source count output absent. Do not assume the graphical distributions are also copied.
**Human question:** What are the actual contributor counts for PanelB's plotted omega3 and placebo groups at each time?
**Classification information:** S_W, REPORT within main. Pending Human Adjudication.

## STAT-MP06 — Figure2D omega3 ACR participant rows repeat vitaminD rows

**Candidate statement:** Figure2D prints omega3/placebo urineACR participant counts that reproduce vitaminD PanelC counts and disagree with matched omega3 rows in eTable6.
**Primary category:** Cross-document numeric inconsistency.
**Compared locations and document roles:** REPORT [DOC-001 Figure2 PDFp7](../../../jama_de_boer_2019_oi_190122.pdf#page=7) PanelD versus REPORT [DOC-003 eTable6 PDFp11](../../../joi190122supp2_prod.pdf#page=11), matching baseline/year2/year5 ACR contributor N for omega3 assignment. PanelC is within-main duplicate corroboration only.
**Source evidence:** PanelD placebo609,463,440; omega3 702,529,505. eTable6 omega3 placebo653,490,467; active658,502,478. eTable6 vitaminD active702,529,505; placebo609,463,440.
**Calculation/rule:** PanelD active discrepancies44,27,27; placebo-44,-27,-27. Zero count tolerance. Baseline active702 exceeds randomized omega3active659. eTable6 and Figure2 supply observational N while modeled change uses imputation; that distinction does not explain copied observational N.
**S relationships:** Non-inferential contributor identity; reference supplemental ACR statistical shard's eTable6 marginals at canonical merge, never recreate its owned S records.
**Alternatives and missing inputs:** Source plot output absent; copied count-row values plausible. No claim plotted ACR boxes or model estimates were copied.
**Human question:** Which participant counts correspond to the plotted PanelD groups, and why do PanelD and eTable6 differ for the same assignment/time?
**Classification information:** S_C, different REPORT documents. Main PanelC merely corroborates repetition and is not an additional discrepancy relationship. Pending Human Adjudication.

## Handoff limits

All six candidates require exact-source mechanical recheck and stable registration by coordinator; no severity, evidence-state adjudication or final correction is assigned here. Candidates may duplicate independently discovered numeric/cross-source records only when exact compared values/locations/rule agree. Figure3 and Figure4 overall count discrepancies are different comparisons. Main Figure2 eGFR and ACR copied-count discrepancies are different outcomes/documents and remain separate absent a genuine identity rule.

No candidate is emitted solely for absent inferential definitions, graphical endpoint precision, shared calibrationr, coherent threshold-rounded HR/P or finite precision zero notation. No claim paper conclusions are wrong. Bounded downstream concern is extraction of wrong assignment N, contributor N, quartile description or biomarker measure if human review confirms the labels/counts.



# Statistical Pass 1 Supplemental Other Checker

Fresh runtime task /root/stats_pass1_supp_other; runtime ID 01a12888-e292-76a0-adff-3db29980b844; required model gpt-6.1-sol/high; FRESH_SPAWN. This agent performs pass 1 only. Exact assigned scope: DOC-003 REPORT eTables4/5 pp9/10, eTable10 p15, eFigures2/3 pp18/19. All 117 relationships S201–S317 are PASS_1_COMPLETE: 48 eGFR estimate/CI fields, 32 rate/difference/HR-CI fields with 8 HR-P pairings, 26 graphical ratio-CI fields with 2 overall-P pairings, 11 independent interaction P fields. Four eGFR year 5 contrast-P fields are likewise paired, not separately counted.

All80 numeric intervals contain their point estimate and have ordered endpoints. All26 graphical CIs visibly contain their plotted point and cross1; precise plotted values are absent. All paired reported P values are>.05 and qualitatively agree with printed null inclusion. All11 interaction Ps are>.05; their nulls differ from individual subgroup-effect nulls. Exact test/interval/SE compatibility is unavailable for named D1/D2/D3 definitions in the companion inventory; no model convention is substituted. No display-zero P value occurs; no zero-only candidate was emitted. Nine local candidates follow, each Pending Human Adjudication. These are provisional observations, with no severity, validity or acceptance assignment.

## Per-relationship source-grounded results

The source location, complete printed values, model/population definitions and missing-definition codes for each ID are in statistics/parts/pass1_supp_other_inventory.md. Each record below carries its own pass1 check; the evidence is not reduced to a pooled cell or subgroup.

| S ID | Exact field | Check result | Status |
|---|---|---|---|
| S201 | DOC-003 REPORT eTable4 p9; Vitamin D; Baseline; MA | Ordered CI and estimate contained; Positive eGFR arithmetic mean and CI; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S202 | DOC-003 REPORT eTable4 p9; Vitamin D; Baseline; MP | Ordered CI and estimate contained; Positive eGFR arithmetic mean and CI; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S203 | DOC-003 REPORT eTable4 p9; Vitamin D; Year2; MA | Ordered CI and estimate contained; Positive eGFR arithmetic mean and CI; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S204 | DOC-003 REPORT eTable4 p9; Vitamin D; Year2; MP | Ordered CI and estimate contained; Positive eGFR arithmetic mean and CI; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S205 | DOC-003 REPORT eTable4 p9; Vitamin D; Year2; CA | Ordered CI and estimate contained; Negative absolute change and wholly negative CI agree with eGFR loss; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S206 | DOC-003 REPORT eTable4 p9; Vitamin D; Year2; CP | Ordered CI and estimate contained; Negative absolute change and wholly negative CI agree with eGFR loss; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S207 | DOC-003 REPORT eTable4 p9; Vitamin D; Year2; D | Ordered CI and estimate contained; Difference CI spans0; direction matches active-minus-placebo eGFR change. Year2 has no paired P; do not supply one. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S208 | DOC-003 REPORT eTable4 p9; Vitamin D; Year5; MA | Ordered CI and estimate contained; Positive eGFR arithmetic mean and CI; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S209 | DOC-003 REPORT eTable4 p9; Vitamin D; Year5; MP | Ordered CI and estimate contained; Positive eGFR arithmetic mean and CI; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S210 | DOC-003 REPORT eTable4 p9; Vitamin D; Year5; CA | Ordered CI and estimate contained; Negative absolute change and wholly negative CI agree with eGFR loss; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S211 | DOC-003 REPORT eTable4 p9; Vitamin D; Year5; CP | Ordered CI and estimate contained; Negative absolute change and wholly negative CI agree with eGFR loss; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S212 | DOC-003 REPORT eTable4 p9; Vitamin D; Year5; D | Ordered CI and estimate contained; Difference CI spans0; direction matches active-minus-placebo eGFR change. Paired P>.05, qualitatively coherent; exact P reconciliation unavailable D1. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S213 | DOC-003 REPORT eTable4 p9; Omega-3; Baseline; MA | Ordered CI and estimate contained; Positive eGFR arithmetic mean and CI; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S214 | DOC-003 REPORT eTable4 p9; Omega-3; Baseline; MP | Ordered CI and estimate contained; Positive eGFR arithmetic mean and CI; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S215 | DOC-003 REPORT eTable4 p9; Omega-3; Year2; MA | Ordered CI and estimate contained; Positive eGFR arithmetic mean and CI; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S216 | DOC-003 REPORT eTable4 p9; Omega-3; Year2; MP | Ordered CI and estimate contained; Positive eGFR arithmetic mean and CI; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S217 | DOC-003 REPORT eTable4 p9; Omega-3; Year2; CA | Ordered CI and estimate contained; Negative absolute change and wholly negative CI agree with eGFR loss; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S218 | DOC-003 REPORT eTable4 p9; Omega-3; Year2; CP | Ordered CI and estimate contained; Negative absolute change and wholly negative CI agree with eGFR loss; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S219 | DOC-003 REPORT eTable4 p9; Omega-3; Year2; D | Ordered CI and estimate contained; Difference CI spans0; direction matches active-minus-placebo eGFR change. Year2 has no paired P; do not supply one. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S220 | DOC-003 REPORT eTable4 p9; Omega-3; Year5; MA | Ordered CI and estimate contained; Positive eGFR arithmetic mean and CI; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S221 | DOC-003 REPORT eTable4 p9; Omega-3; Year5; MP | Ordered CI and estimate contained; Positive eGFR arithmetic mean and CI; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S222 | DOC-003 REPORT eTable4 p9; Omega-3; Year5; CA | Ordered CI and estimate contained; Negative absolute change and wholly negative CI agree with eGFR loss; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S223 | DOC-003 REPORT eTable4 p9; Omega-3; Year5; CP | Ordered CI and estimate contained; Negative absolute change and wholly negative CI agree with eGFR loss; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S224 | DOC-003 REPORT eTable4 p9; Omega-3; Year5; D | Ordered CI and estimate contained; Difference CI spans0; direction matches active-minus-placebo eGFR change. Paired P>.05, qualitatively coherent; exact P reconciliation unavailable D1. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S225 | DOC-003 REPORT eTable5 p10; Vitamin D; Baseline; MA | Ordered CI and estimate contained; Positive eGFR arithmetic mean and CI; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S226 | DOC-003 REPORT eTable5 p10; Vitamin D; Baseline; MP | Ordered CI and estimate contained; Positive eGFR arithmetic mean and CI; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S227 | DOC-003 REPORT eTable5 p10; Vitamin D; Year2; MA | Ordered CI and estimate contained; Positive eGFR arithmetic mean and CI; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S228 | DOC-003 REPORT eTable5 p10; Vitamin D; Year2; MP | Ordered CI and estimate contained; Positive eGFR arithmetic mean and CI; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S229 | DOC-003 REPORT eTable5 p10; Vitamin D; Year2; CA | Ordered CI and estimate contained; Negative absolute change and wholly negative CI agree with eGFR loss; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S230 | DOC-003 REPORT eTable5 p10; Vitamin D; Year2; CP | Ordered CI and estimate contained; Negative absolute change and wholly negative CI agree with eGFR loss; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S231 | DOC-003 REPORT eTable5 p10; Vitamin D; Year2; D | Ordered CI and estimate contained; Difference CI spans0; direction matches active-minus-placebo eGFR change. Year2 has no paired P; do not supply one. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S232 | DOC-003 REPORT eTable5 p10; Vitamin D; Year5; MA | Ordered CI and estimate contained; Positive eGFR arithmetic mean and CI; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S233 | DOC-003 REPORT eTable5 p10; Vitamin D; Year5; MP | Ordered CI and estimate contained; Positive eGFR arithmetic mean and CI; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S234 | DOC-003 REPORT eTable5 p10; Vitamin D; Year5; CA | Ordered CI and estimate contained; Negative absolute change and wholly negative CI agree with eGFR loss; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S235 | DOC-003 REPORT eTable5 p10; Vitamin D; Year5; CP | Ordered CI and estimate contained; Negative absolute change and wholly negative CI agree with eGFR loss; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S236 | DOC-003 REPORT eTable5 p10; Vitamin D; Year5; D | Ordered CI and estimate contained; Difference CI spans0; direction matches active-minus-placebo eGFR change. Paired P>.05, qualitatively coherent; exact P reconciliation unavailable D1. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S237 | DOC-003 REPORT eTable5 p10; Omega-3; Baseline; MA | Ordered CI and estimate contained; Positive eGFR arithmetic mean and CI; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S238 | DOC-003 REPORT eTable5 p10; Omega-3; Baseline; MP | Ordered CI and estimate contained; Positive eGFR arithmetic mean and CI; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S239 | DOC-003 REPORT eTable5 p10; Omega-3; Year2; MA | Ordered CI and estimate contained; Positive eGFR arithmetic mean and CI; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S240 | DOC-003 REPORT eTable5 p10; Omega-3; Year2; MP | Ordered CI and estimate contained; Positive eGFR arithmetic mean and CI; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S241 | DOC-003 REPORT eTable5 p10; Omega-3; Year2; CA | Ordered CI and estimate contained; Negative absolute change and wholly negative CI agree with eGFR loss; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S242 | DOC-003 REPORT eTable5 p10; Omega-3; Year2; CP | Ordered CI and estimate contained; Negative absolute change and wholly negative CI agree with eGFR loss; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S243 | DOC-003 REPORT eTable5 p10; Omega-3; Year2; D | Ordered CI and estimate contained; Difference CI spans0; direction matches active-minus-placebo eGFR change. Year2 has no paired P; do not supply one. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S244 | DOC-003 REPORT eTable5 p10; Omega-3; Year5; MA | Ordered CI and estimate contained; Positive eGFR arithmetic mean and CI; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S245 | DOC-003 REPORT eTable5 p10; Omega-3; Year5; MP | Ordered CI and estimate contained; Positive eGFR arithmetic mean and CI; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S246 | DOC-003 REPORT eTable5 p10; Omega-3; Year5; CA | Ordered CI and estimate contained; Negative absolute change and wholly negative CI agree with eGFR loss; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S247 | DOC-003 REPORT eTable5 p10; Omega-3; Year5; CP | Ordered CI and estimate contained; Negative absolute change and wholly negative CI agree with eGFR loss; no paired test supplied. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S248 | DOC-003 REPORT eTable5 p10; Omega-3; Year5; D | Ordered CI and estimate contained; Difference CI spans0; direction matches active-minus-placebo eGFR change. Paired P>.05, qualitatively coherent; exact P reconciliation unavailable D1. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S249 | DOC-003 REPORT eTable10 p15; Vitamin D; ≥40% eGFR decline or kidney failure; IA | Ordered CI and estimate contained; Positive incidence rate per100 person-years, distinct from observed event count; person-time/CI construction absent D2. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S250 | DOC-003 REPORT eTable10 p15; Vitamin D; ≥40% eGFR decline or kidney failure; IP | Ordered CI and estimate contained; Positive incidence rate per100 person-years, distinct from observed event count; person-time/CI construction absent D2. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S251 | DOC-003 REPORT eTable10 p15; Vitamin D; ≥40% eGFR decline or kidney failure; ID | Ordered CI and estimate contained; Rate difference spans0; sign compatible with rounded arm rates (three one-decimal operands allow ±0.15 arithmetic discrepancy); no test printed for this difference. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S252 | DOC-003 REPORT eTable10 p15; Vitamin D; ≥40% eGFR decline or kidney failure; HR | Ordered CI and estimate contained; Positive active/placebo Cox HR; CI spans1 and paired P>.05; directions agree with arm rates. Exact P reconciliation unavailable D2. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S253 | DOC-003 REPORT eTable10 p15; Vitamin D; ≥30% eGFR decline, kidney failure, or death; IA | Ordered CI and estimate contained; Positive incidence rate per100 person-years, distinct from observed event count; person-time/CI construction absent D2. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S254 | DOC-003 REPORT eTable10 p15; Vitamin D; ≥30% eGFR decline, kidney failure, or death; IP | Ordered CI and estimate contained; Positive incidence rate per100 person-years, distinct from observed event count; person-time/CI construction absent D2. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S255 | DOC-003 REPORT eTable10 p15; Vitamin D; ≥30% eGFR decline, kidney failure, or death; ID | Ordered CI and estimate contained; Rate difference spans0; sign compatible with rounded arm rates (three one-decimal operands allow ±0.15 arithmetic discrepancy); no test printed for this difference. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S256 | DOC-003 REPORT eTable10 p15; Vitamin D; ≥30% eGFR decline, kidney failure, or death; HR | Ordered CI and estimate contained; Positive active/placebo Cox HR; CI spans1 and paired P>.05; directions agree with arm rates. Exact P reconciliation unavailable D2. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S257 | DOC-003 REPORT eTable10 p15; Vitamin D; ≥30% eGFR decline or kidney failure; IA | Ordered CI and estimate contained; Positive incidence rate per100 person-years, distinct from observed event count; person-time/CI construction absent D2. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S258 | DOC-003 REPORT eTable10 p15; Vitamin D; ≥30% eGFR decline or kidney failure; IP | Ordered CI and estimate contained; Positive incidence rate per100 person-years, distinct from observed event count; person-time/CI construction absent D2. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S259 | DOC-003 REPORT eTable10 p15; Vitamin D; ≥30% eGFR decline or kidney failure; ID | Ordered CI and estimate contained; Rate difference spans0; sign compatible with rounded arm rates (three one-decimal operands allow ±0.15 arithmetic discrepancy); no test printed for this difference. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S260 | DOC-003 REPORT eTable10 p15; Vitamin D; ≥30% eGFR decline or kidney failure; HR | Ordered CI and estimate contained; Positive active/placebo Cox HR; CI spans1 and paired P>.05; directions agree with arm rates. Exact P reconciliation unavailable D2. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S261 | DOC-003 REPORT eTable10 p15; Vitamin D; ≥30% eGFR decline; IA | Ordered CI and estimate contained; Positive incidence rate per100 person-years, distinct from observed event count; person-time/CI construction absent D2. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S262 | DOC-003 REPORT eTable10 p15; Vitamin D; ≥30% eGFR decline; IP | Ordered CI and estimate contained; Positive incidence rate per100 person-years, distinct from observed event count; person-time/CI construction absent D2. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S263 | DOC-003 REPORT eTable10 p15; Vitamin D; ≥30% eGFR decline; ID | Ordered CI and estimate contained; Rate difference spans0; sign compatible with rounded arm rates (three one-decimal operands allow ±0.15 arithmetic discrepancy); no test printed for this difference. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S264 | DOC-003 REPORT eTable10 p15; Vitamin D; ≥30% eGFR decline; HR | Ordered CI and estimate contained; Positive active/placebo Cox HR; CI spans1 and paired P>.05; directions agree with arm rates. Exact P reconciliation unavailable D2. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S265 | DOC-003 REPORT eTable10 p15; Omega-3; ≥40% eGFR decline or kidney failure; IA | Ordered CI and estimate contained; Positive incidence rate per100 person-years, distinct from observed event count; person-time/CI construction absent D2. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S266 | DOC-003 REPORT eTable10 p15; Omega-3; ≥40% eGFR decline or kidney failure; IP | Ordered CI and estimate contained; Positive incidence rate per100 person-years, distinct from observed event count; person-time/CI construction absent D2. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S267 | DOC-003 REPORT eTable10 p15; Omega-3; ≥40% eGFR decline or kidney failure; ID | Ordered CI and estimate contained; Rate difference spans0; sign compatible with rounded arm rates (three one-decimal operands allow ±0.15 arithmetic discrepancy); no test printed for this difference. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S268 | DOC-003 REPORT eTable10 p15; Omega-3; ≥40% eGFR decline or kidney failure; HR | Ordered CI and estimate contained; Positive active/placebo Cox HR; CI spans1 and paired P>.05; directions agree with arm rates. Exact P reconciliation unavailable D2. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S269 | DOC-003 REPORT eTable10 p15; Omega-3; ≥30% eGFR decline, kidney failure, or death; IA | Ordered CI and estimate contained; Positive incidence rate per100 person-years, distinct from observed event count; person-time/CI construction absent D2. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S270 | DOC-003 REPORT eTable10 p15; Omega-3; ≥30% eGFR decline, kidney failure, or death; IP | Ordered CI and estimate contained; Positive incidence rate per100 person-years, distinct from observed event count; person-time/CI construction absent D2. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S271 | DOC-003 REPORT eTable10 p15; Omega-3; ≥30% eGFR decline, kidney failure, or death; ID | Ordered CI and estimate contained; Rate difference spans0; sign compatible with rounded arm rates (three one-decimal operands allow ±0.15 arithmetic discrepancy); no test printed for this difference. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S272 | DOC-003 REPORT eTable10 p15; Omega-3; ≥30% eGFR decline, kidney failure, or death; HR | Ordered CI and estimate contained; Positive active/placebo Cox HR; CI spans1 and paired P>.05; directions agree with arm rates. Exact P reconciliation unavailable D2. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S273 | DOC-003 REPORT eTable10 p15; Omega-3; ≥30% eGFR decline or kidney failure; IA | Ordered CI and estimate contained; Positive incidence rate per100 person-years, distinct from observed event count; person-time/CI construction absent D2. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S274 | DOC-003 REPORT eTable10 p15; Omega-3; ≥30% eGFR decline or kidney failure; IP | Ordered CI and estimate contained; Positive incidence rate per100 person-years, distinct from observed event count; person-time/CI construction absent D2. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S275 | DOC-003 REPORT eTable10 p15; Omega-3; ≥30% eGFR decline or kidney failure; ID | Ordered CI and estimate contained; Rate difference spans0; sign compatible with rounded arm rates (three one-decimal operands allow ±0.15 arithmetic discrepancy); no test printed for this difference. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S276 | DOC-003 REPORT eTable10 p15; Omega-3; ≥30% eGFR decline or kidney failure; HR | Ordered CI and estimate contained; Positive active/placebo Cox HR; CI spans1 and paired P>.05; directions agree with arm rates. Exact P reconciliation unavailable D2. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S277 | DOC-003 REPORT eTable10 p15; Omega-3; ≥30% eGFR decline; IA | Ordered CI and estimate contained; Positive incidence rate per100 person-years, distinct from observed event count; person-time/CI construction absent D2. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S278 | DOC-003 REPORT eTable10 p15; Omega-3; ≥30% eGFR decline; IP | Ordered CI and estimate contained; Positive incidence rate per100 person-years, distinct from observed event count; person-time/CI construction absent D2. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S279 | DOC-003 REPORT eTable10 p15; Omega-3; ≥30% eGFR decline; ID | Ordered CI and estimate contained; Rate difference spans0; sign compatible with rounded arm rates (three one-decimal operands allow ±0.15 arithmetic discrepancy); no test printed for this difference. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S280 | DOC-003 REPORT eTable10 p15; Omega-3; ≥30% eGFR decline; HR | Ordered CI and estimate contained; Positive active/placebo Cox HR; CI spans1 and paired P>.05; directions agree with arm rates. Exact P reconciliation unavailable D2. NO_CANDIDATE for interval/order/sign. | PASS_1_COMPLETE |
| S281 | DOC-003 REPORT eFigure2 p18; Overall; graphical active/placebo ratio and95%CI | Point visibly within ordered positive graphical CI; CI crosses1; no endpoint reconstructed. D3 exact P/ratio unavailable. Direction labels→STAT-UO01; ratio caption→STAT-UO03; comparator caption→STAT-UO08; N labels→STAT-UO05; matched P→STAT-UO07. | PASS_1_COMPLETE |
| S282 | DOC-003 REPORT eFigure2 p18; White; graphical active/placebo ratio and95%CI | Point visibly within ordered positive graphical CI; CI crosses1; no endpoint reconstructed. D3 exact P/ratio unavailable. Direction labels→STAT-UO01; ratio caption→STAT-UO03; comparator caption→STAT-UO08; Adjusted ratio need not equal quotient of descriptive geometric means; no such equality imposed. | PASS_1_COMPLETE |
| S283 | DOC-003 REPORT eFigure2 p18; Black; graphical active/placebo ratio and95%CI | Point visibly within ordered positive graphical CI; CI crosses1; no endpoint reconstructed. D3 exact P/ratio unavailable. Direction labels→STAT-UO01; ratio caption→STAT-UO03; comparator caption→STAT-UO08; Adjusted ratio need not equal quotient of descriptive geometric means; no such equality imposed. | PASS_1_COMPLETE |
| S284 | DOC-003 REPORT eFigure2 p18; Baseline ACR<30 mg/g; graphical active/placebo ratio and95%CI | Point visibly within ordered positive graphical CI; CI crosses1; no endpoint reconstructed. D3 exact P/ratio unavailable. Direction labels→STAT-UO01; ratio caption→STAT-UO03; comparator caption→STAT-UO08; Adjusted ratio need not equal quotient of descriptive geometric means; no such equality imposed. | PASS_1_COMPLETE |
| S285 | DOC-003 REPORT eFigure2 p18; Baseline ACR≥30 mg/g; graphical active/placebo ratio and95%CI | Point visibly within ordered positive graphical CI; CI crosses1; no endpoint reconstructed. D3 exact P/ratio unavailable. Direction labels→STAT-UO01; ratio caption→STAT-UO03; comparator caption→STAT-UO08; Adjusted ratio need not equal quotient of descriptive geometric means; no such equality imposed. | PASS_1_COMPLETE |
| S286 | DOC-003 REPORT eFigure2 p18; Baseline 25(OH)D<20 ng/mL; graphical active/placebo ratio and95%CI | Point visibly within ordered positive graphical CI; CI crosses1; no endpoint reconstructed. D3 exact P/ratio unavailable. Direction labels→STAT-UO01; ratio caption→STAT-UO03; comparator caption→STAT-UO08; Adjusted ratio need not equal quotient of descriptive geometric means; no such equality imposed. | PASS_1_COMPLETE |
| S287 | DOC-003 REPORT eFigure2 p18; Baseline 25(OH)D20–<30 ng/mL; graphical active/placebo ratio and95%CI | Point visibly within ordered positive graphical CI; CI crosses1; no endpoint reconstructed. D3 exact P/ratio unavailable. Direction labels→STAT-UO01; ratio caption→STAT-UO03; comparator caption→STAT-UO08; Adjusted ratio need not equal quotient of descriptive geometric means; no such equality imposed. | PASS_1_COMPLETE |
| S288 | DOC-003 REPORT eFigure2 p18; Baseline 25(OH)D≥30 ng/mL; graphical active/placebo ratio and95%CI | Point visibly within ordered positive graphical CI; CI crosses1; no endpoint reconstructed. D3 exact P/ratio unavailable. Direction labels→STAT-UO01; ratio caption→STAT-UO03; comparator caption→STAT-UO08; Adjusted ratio need not equal quotient of descriptive geometric means; no such equality imposed. | PASS_1_COMPLETE |
| S289 | DOC-003 REPORT eFigure2 p18; Baseline eGFR≥60; graphical active/placebo ratio and95%CI | Point visibly within ordered positive graphical CI; CI crosses1; no endpoint reconstructed. D3 exact P/ratio unavailable. Direction labels→STAT-UO01; ratio caption→STAT-UO03; comparator caption→STAT-UO08; Adjusted ratio need not equal quotient of descriptive geometric means; no such equality imposed. | PASS_1_COMPLETE |
| S290 | DOC-003 REPORT eFigure2 p18; Baseline eGFR<60; graphical active/placebo ratio and95%CI | Point visibly within ordered positive graphical CI; CI crosses1; no endpoint reconstructed. D3 exact P/ratio unavailable. Direction labels→STAT-UO01; ratio caption→STAT-UO03; comparator caption→STAT-UO08; Adjusted ratio need not equal quotient of descriptive geometric means; no such equality imposed. | PASS_1_COMPLETE |
| S291 | DOC-003 REPORT eFigure2 p18; BMI<25 kg/m²; graphical active/placebo ratio and95%CI | Point visibly within ordered positive graphical CI; CI crosses1; no endpoint reconstructed. D3 exact P/ratio unavailable. Direction labels→STAT-UO01; ratio caption→STAT-UO03; comparator caption→STAT-UO08; Adjusted ratio need not equal quotient of descriptive geometric means; no such equality imposed. | PASS_1_COMPLETE |
| S292 | DOC-003 REPORT eFigure2 p18; BMI25–<30 kg/m²; graphical active/placebo ratio and95%CI | Point visibly within ordered positive graphical CI; CI crosses1; no endpoint reconstructed. D3 exact P/ratio unavailable. Direction labels→STAT-UO01; ratio caption→STAT-UO03; comparator caption→STAT-UO08; Adjusted ratio need not equal quotient of descriptive geometric means; no such equality imposed. | PASS_1_COMPLETE |
| S293 | DOC-003 REPORT eFigure2 p18; BMI≥30 kg/m²; graphical active/placebo ratio and95%CI | Point visibly within ordered positive graphical CI; CI crosses1; no endpoint reconstructed. D3 exact P/ratio unavailable. Direction labels→STAT-UO01; ratio caption→STAT-UO03; comparator caption→STAT-UO08; Adjusted ratio need not equal quotient of descriptive geometric means; no such equality imposed. | PASS_1_COMPLETE |
| S294 | DOC-003 REPORT eFigure2 p18; Omega-3 randomization Placebo; graphical active/placebo ratio and95%CI | Point visibly within ordered positive graphical CI; CI crosses1; no endpoint reconstructed. D3 exact P/ratio unavailable. Direction labels→STAT-UO01; ratio caption→STAT-UO03; comparator caption→STAT-UO08; Adjusted ratio need not equal quotient of descriptive geometric means; no such equality imposed. | PASS_1_COMPLETE |
| S295 | DOC-003 REPORT eFigure2 p18; Omega-3 randomization Omega-3; graphical active/placebo ratio and95%CI | Point visibly within ordered positive graphical CI; CI crosses1; no endpoint reconstructed. D3 exact P/ratio unavailable. Direction labels→STAT-UO01; ratio caption→STAT-UO03; comparator caption→STAT-UO08; Adjusted ratio need not equal quotient of descriptive geometric means; no such equality imposed. | PASS_1_COMPLETE |
| S296 | DOC-003 REPORT eFigure3 p19; Overall; graphical active/placebo ratio and95%CI | Point visibly within ordered positive graphical CI; CI crosses1; no endpoint reconstructed. D3 exact P/ratio unavailable. Direction labels→STAT-UO02; ratio caption→STAT-UO04; comparator caption→STAT-UO09; N labels→STAT-UO06. | PASS_1_COMPLETE |
| S297 | DOC-003 REPORT eFigure3 p19; Baseline EPA/DHA≤2.2; graphical active/placebo ratio and95%CI | Point visibly within ordered positive graphical CI; CI crosses1; no endpoint reconstructed. D3 exact P/ratio unavailable. Direction labels→STAT-UO02; ratio caption→STAT-UO04; comparator caption→STAT-UO09; Adjusted ratio need not equal quotient of descriptive geometric means; no such equality imposed. | PASS_1_COMPLETE |
| S298 | DOC-003 REPORT eFigure3 p19; Baseline EPA/DHA>2.2; graphical active/placebo ratio and95%CI | Point visibly within ordered positive graphical CI; CI crosses1; no endpoint reconstructed. D3 exact P/ratio unavailable. Direction labels→STAT-UO02; ratio caption→STAT-UO04; comparator caption→STAT-UO09; Adjusted ratio need not equal quotient of descriptive geometric means; no such equality imposed. | PASS_1_COMPLETE |
| S299 | DOC-003 REPORT eFigure3 p19; Baseline ACR<30 mg/g; graphical active/placebo ratio and95%CI | Point visibly within ordered positive graphical CI; CI crosses1; no endpoint reconstructed. D3 exact P/ratio unavailable. Direction labels→STAT-UO02; ratio caption→STAT-UO04; comparator caption→STAT-UO09; Adjusted ratio need not equal quotient of descriptive geometric means; no such equality imposed. | PASS_1_COMPLETE |
| S300 | DOC-003 REPORT eFigure3 p19; Baseline ACR≥30 mg/g; graphical active/placebo ratio and95%CI | Point visibly within ordered positive graphical CI; CI crosses1; no endpoint reconstructed. D3 exact P/ratio unavailable. Direction labels→STAT-UO02; ratio caption→STAT-UO04; comparator caption→STAT-UO09; Adjusted ratio need not equal quotient of descriptive geometric means; no such equality imposed. | PASS_1_COMPLETE |
| S301 | DOC-003 REPORT eFigure3 p19; Baseline hsCRP≤0.2 mg/dL; graphical active/placebo ratio and95%CI | Point visibly within ordered positive graphical CI; CI crosses1; no endpoint reconstructed. D3 exact P/ratio unavailable. Direction labels→STAT-UO02; ratio caption→STAT-UO04; comparator caption→STAT-UO09; Adjusted ratio need not equal quotient of descriptive geometric means; no such equality imposed. | PASS_1_COMPLETE |
| S302 | DOC-003 REPORT eFigure3 p19; Baseline hsCRP>0.2 mg/dL; graphical active/placebo ratio and95%CI | Point visibly within ordered positive graphical CI; CI crosses1; no endpoint reconstructed. D3 exact P/ratio unavailable. Direction labels→STAT-UO02; ratio caption→STAT-UO04; comparator caption→STAT-UO09; Adjusted ratio need not equal quotient of descriptive geometric means; no such equality imposed. | PASS_1_COMPLETE |
| S303 | DOC-003 REPORT eFigure3 p19; Fish intake<1.5 servings/week; graphical active/placebo ratio and95%CI | Point visibly within ordered positive graphical CI; CI crosses1; no endpoint reconstructed. D3 exact P/ratio unavailable. Direction labels→STAT-UO02; ratio caption→STAT-UO04; comparator caption→STAT-UO09; Adjusted ratio need not equal quotient of descriptive geometric means; no such equality imposed. | PASS_1_COMPLETE |
| S304 | DOC-003 REPORT eFigure3 p19; Fish intake≥1.5 servings/week; graphical active/placebo ratio and95%CI | Point visibly within ordered positive graphical CI; CI crosses1; no endpoint reconstructed. D3 exact P/ratio unavailable. Direction labels→STAT-UO02; ratio caption→STAT-UO04; comparator caption→STAT-UO09; Adjusted ratio need not equal quotient of descriptive geometric means; no such equality imposed. | PASS_1_COMPLETE |
| S305 | DOC-003 REPORT eFigure3 p19; Vitamin D randomization Placebo; graphical active/placebo ratio and95%CI | Point visibly within ordered positive graphical CI; CI crosses1; no endpoint reconstructed. D3 exact P/ratio unavailable. Direction labels→STAT-UO02; ratio caption→STAT-UO04; comparator caption→STAT-UO09; Adjusted ratio need not equal quotient of descriptive geometric means; no such equality imposed. | PASS_1_COMPLETE |
| S306 | DOC-003 REPORT eFigure3 p19; Vitamin D randomization Vitamin D; graphical active/placebo ratio and95%CI | Point visibly within ordered positive graphical CI; CI crosses1; no endpoint reconstructed. D3 exact P/ratio unavailable. Direction labels→STAT-UO02; ratio caption→STAT-UO04; comparator caption→STAT-UO09; Adjusted ratio need not equal quotient of descriptive geometric means; no such equality imposed. | PASS_1_COMPLETE |
| S307 | DOC-003 REPORT eFigure2 p18; Race; subgroup-block interaction | P within[0,1]; >.05, coherent with narrative absence of significant subgroup heterogeneity; do not compare directly with individual subgroup CI because distinct null. NO_CANDIDATE; exact compatibility unavailable D3. | PASS_1_COMPLETE |
| S308 | DOC-003 REPORT eFigure2 p18; Baseline ACR; subgroup-block interaction | P within[0,1]; >.05, coherent with narrative absence of significant subgroup heterogeneity; do not compare directly with individual subgroup CI because distinct null. NO_CANDIDATE; exact compatibility unavailable D3. | PASS_1_COMPLETE |
| S309 | DOC-003 REPORT eFigure2 p18; Baseline25(OH)D; subgroup-block interaction | P within[0,1]; >.05, coherent with narrative absence of significant subgroup heterogeneity; do not compare directly with individual subgroup CI because distinct null. NO_CANDIDATE; exact compatibility unavailable D3. | PASS_1_COMPLETE |
| S310 | DOC-003 REPORT eFigure2 p18; Baseline eGFR; subgroup-block interaction | P within[0,1]; >.05, coherent with narrative absence of significant subgroup heterogeneity; do not compare directly with individual subgroup CI because distinct null. NO_CANDIDATE; exact compatibility unavailable D3. | PASS_1_COMPLETE |
| S311 | DOC-003 REPORT eFigure2 p18; BMI; subgroup-block interaction | P within[0,1]; >.05, coherent with narrative absence of significant subgroup heterogeneity; do not compare directly with individual subgroup CI because distinct null. NO_CANDIDATE; exact compatibility unavailable D3. | PASS_1_COMPLETE |
| S312 | DOC-003 REPORT eFigure2 p18; Omega-3 randomization; subgroup-block interaction | P within[0,1]; >.05, coherent with narrative absence of significant subgroup heterogeneity; do not compare directly with individual subgroup CI because distinct null. NO_CANDIDATE; exact compatibility unavailable D3. | PASS_1_COMPLETE |
| S313 | DOC-003 REPORT eFigure3 p19; Baseline EPA/DHA; subgroup-block interaction | P within[0,1]; >.05, coherent with narrative absence of significant subgroup heterogeneity; do not compare directly with individual subgroup CI because distinct null. NO_CANDIDATE; exact compatibility unavailable D3. | PASS_1_COMPLETE |
| S314 | DOC-003 REPORT eFigure3 p19; Baseline ACR; subgroup-block interaction | P within[0,1]; >.05, coherent with narrative absence of significant subgroup heterogeneity; do not compare directly with individual subgroup CI because distinct null. NO_CANDIDATE; exact compatibility unavailable D3. | PASS_1_COMPLETE |
| S315 | DOC-003 REPORT eFigure3 p19; Baseline hsCRP; subgroup-block interaction | P within[0,1]; >.05, coherent with narrative absence of significant subgroup heterogeneity; do not compare directly with individual subgroup CI because distinct null. NO_CANDIDATE; exact compatibility unavailable D3. | PASS_1_COMPLETE |
| S316 | DOC-003 REPORT eFigure3 p19; Fish intake; subgroup-block interaction | P within[0,1]; >.05, coherent with narrative absence of significant subgroup heterogeneity; do not compare directly with individual subgroup CI because distinct null. NO_CANDIDATE; exact compatibility unavailable D3. | PASS_1_COMPLETE |
| S317 | DOC-003 REPORT eFigure3 p19; Vitamin D randomization; subgroup-block interaction | P within[0,1]; >.05, coherent with narrative absence of significant subgroup heterogeneity; do not compare directly with individual subgroup CI because distinct null. NO_CANDIDATE; exact compatibility unavailable D3. | PASS_1_COMPLETE |

## Candidate observations

Distinct captions, figures, comparator labels and treatment-assignment populations are kept separate before stable IDs. Common likely production causes do not constitute duplicate evidence. The coordinator may merge checker duplicates only when printed evidence, comparator and consistency rule are identical. A main-report location that only corroborates the direction or GM assignment does not create a new cross-document discrepancy relationship.

### STAT-UO01 — eFigure2 favor-direction arrows conflict with the printed ACR ratio orientation

- Status: Pending Human Adjudication.
- Relationships: S281–S295.
- Proposed primary category: Measure, label, or scale inconsistency.
- Compared locations and document roles: REPORT DOC-003 p18 graph ratio header and axis arrows; REPORT DOC-001 p3 adverse doubling-ACR definition is corroborative only.
- Provisional primary relationship: S_W; all discrepancy relationships: S_W.
- Exact source evidence: DOC-003 p18 eFigure2 header: “Ratio of change, active/placebo (95% CI)”; axis ticks0.5,0.7,1,1.3,1.7; lower-left arrow “Favors Placebo”; lower-right “Favors Vitamin D”. Caption outcome is urine ACR baseline-to-year5. DOC-001 p3 treats doubling ACR to≥30 mg/g as adverse secondary outcome; p2 describes hoped-for reduction of albuminuria.
- Reported versus comparator: An active/placebo ratio below1 represents a smaller proportional ACR increase in active assignment; above1 represents a larger increase. The arrows name the opposite assignment for those sides.
- Reproducible consistency rule: For positive ACR changes, R=active-change/placebo-change; R<1 means lower active proportional ACR change. Use the supplied kidney-outcome direction rather than an assumed convention. This is a direction-label comparison, not a CI/P calculation.
- Calculation and tolerance: If R=.7 on the printed axis, active proportional change is .7 times placebo; if R=1.3, active is1.3 times placebo. These are axis-label examples, not reconstructed effect estimates. No rounding tolerance affects the categorical arrow identity.
- Source-grounded alternatives: An inverted plotted contrast (placebo/active), or an outcome transformation where increase meant improvement, could explain the arrows, but conflicts with the printed active/placebo header and supplied ACR definition. The page does not disclose either alternative.
- Missing definitions: No precise plotted endpoint is needed. Missing production label/contrast provenance prevents selecting which printed element should change.
- Direct observation versus inferred mechanism: Values and labels above are source-visible; alternatives are conditional explanations and are not asserted as the production mechanism.
- Exact remaining human question: Is the plotted estimand active/placebo ACR change, as headed, and which side was intended to favor vitamin D?
- Evidence links: [DOC-003 PDF p18](../../../joi190122supp2_prod.pdf#page=18); [DOC-001 PDF p3](../../../jama_de_boer_2019_oi_190122.pdf#page=3); [DOC-001 PDF p2](../../../jama_de_boer_2019_oi_190122.pdf#page=2).

### STAT-UO02 — eFigure3 favor-direction arrows conflict with the printed ACR ratio orientation

- Status: Pending Human Adjudication.
- Relationships: S296–S306.
- Proposed primary category: Measure, label, or scale inconsistency.
- Compared locations and document roles: REPORT DOC-003 p19 graph ratio header and axis arrows; REPORT DOC-001 p3 adverse doubling-ACR definition corroborates only.
- Provisional primary relationship: S_W; all discrepancy relationships: S_W.
- Exact source evidence: DOC-003 p19 eFigure3 header: “Ratio of change, active/placebo (95% CI)”; scale0.5,0.7,1,1.3,1.7; left “Favors Placebo”, right “Favors Omega-3”.
- Reported versus comparator: Below1 means smaller active proportional ACR increase, while above1 means larger active increase; the favored-assignment arrows give the opposite orientation.
- Reproducible consistency rule: The same supplied positive-ratio and adverse-ACR definition as STAT-UO01, applied to a different figure and intervention. Distinct source labels remain a separate candidate.
- Calculation and tolerance: Axis R<1 implies active-change<placebo-change; R>1 implies active-change>placebo-change. Direct categorical contrast; no statistical approximation or endpoint reconstruction.
- Source-grounded alternatives: Plot could intentionally use placebo/active despite the header, or the favor labels could have been copied from eGFR figures where a positive difference favors active treatment. Neither mechanism is established by supplied model output.
- Missing definitions: Actual plot-generation contrast metadata not supplied; the direction mismatch itself is source-visible.
- Direct observation versus inferred mechanism: Values and labels above are source-visible; alternatives are conditional explanations and are not asserted as the production mechanism.
- Exact remaining human question: Do the eFigure3 points and intervals use active/placebo and are the favor labels aligned with that estimand?
- Evidence links: [DOC-003 PDF p19](../../../joi190122supp2_prod.pdf#page=19); [DOC-001 PDF p3](../../../jama_de_boer_2019_oi_190122.pdf#page=3).

### STAT-UO03 — eFigure2 caption names a difference while its graph is labeled as a ratio

- Status: Pending Human Adjudication.
- Relationships: S281–S295.
- Proposed primary category: Measure, label, or scale inconsistency.
- Compared locations and document roles: REPORT DOC-003 p18 caption versus same-page graphical effect-measure header.
- Provisional primary relationship: S_W; all discrepancy relationships: S_W.
- Exact source evidence: DOC-003 p18 caption: “Estimates are difference in change in urine ACR from baseline to year 5”; plot header: “Ratio of change, active/placebo (95% CI)”; vertical null is1 and ratio-scale ticks are0.5,0.7,1,1.3,1.7.
- Reported versus comparator: Arithmetic difference of proportional changes has null0; ratio of changes has null1. The caption and explicit graph header give distinct measures.
- Reproducible consistency rule: Identify the printed effect measure and null scale, without transforming an unreported interval or assuming the model contrast. Model may use a log difference whose exponentiation is a ratio; such an interpretation needs labeling.
- Calculation and tolerance: Identity comparison: equal-arm changes produce difference0 but ratio1. The displayed graph's null is1. No numeric tolerance applies.
- Source-grounded alternatives: “Difference” might be loose shorthand for treatment effect or an underlying log-scale difference. The printed caption does not state a log-scale difference or exponentiation; the graph expressly states a ratio.
- Missing definitions: Plot generation or caption intention absent; no SE/df needed to reproduce competing labels.
- Direct observation versus inferred mechanism: Values and labels above are source-visible; alternatives are conditional explanations and are not asserted as the production mechanism.
- Exact remaining human question: Should the caption refer to a ratio of ACR changes, or is an underlying log-difference definition intended?
- Evidence links: [DOC-003 PDF p18](../../../joi190122supp2_prod.pdf#page=18).

### STAT-UO04 — eFigure3 caption names a difference while its graph is labeled as a ratio

- Status: Pending Human Adjudication.
- Relationships: S296–S306.
- Proposed primary category: Measure, label, or scale inconsistency.
- Compared locations and document roles: REPORT DOC-003 p19 caption versus same-page graphical effect-measure header.
- Provisional primary relationship: S_W; all discrepancy relationships: S_W.
- Exact source evidence: DOC-003 p19 caption says “Estimates are difference in change in urine ACR from baseline to year 5”; graph header says “Ratio of change, active/placebo (95% CI)”; reference line1.
- Reported versus comparator: Difference and ratio give different numeric scales and different nulls; the figure simultaneously names both.
- Reproducible consistency rule: Measure/null identity as STAT-UO03, but a separate printed caption/graph and intervention.
- Calculation and tolerance: Equal positive changes imply difference0 and ratio1; the graph identifies1 as its null. This is a categorical label comparison, not interval inversion.
- Source-grounded alternatives: A loose treatment-effect use of “difference” or an underlying log-scale difference is possible, but not explicitly identified in the caption.
- Missing definitions: Exact caption intention and plot estimand transformation absent.
- Direct observation versus inferred mechanism: Values and labels above are source-visible; alternatives are conditional explanations and are not asserted as the production mechanism.
- Exact remaining human question: Which displayed measure is intended for eFigure3 and should the caption identify a ratio or a transformed log-difference?
- Evidence links: [DOC-003 PDF p19](../../../joi190122supp2_prod.pdf#page=19).

### STAT-UO05 — eFigure2 overall participant Ns oppose the randomized assignment totals

- Status: Pending Human Adjudication.
- Relationships: S281.
- Proposed primary category: Denominator, proportion, or total inconsistency.
- Compared locations and document roles: REPORT DOC-003 p18 overall N columns versus REPORT DOC-001 p5 Table1 factorial cohort headers; REPORT DOC-003 p11 eTable6 year5 GM labels corroborative.
- Provisional primary relationship: S_C; all discrepancy relationships: S_C.
- Exact source evidence: DOC-003 p18 eFigure2 prints Placebo N703 and Active intervention N609. DOC-001 p5 Table1 factorial arm Ns are vitaminD+omega3=370, vitaminD+placebo=333, omega3+placebo=289, doubleplacebo=320. Thus vitamin D assigned totals are active703, placebo609. DOC-003 p11 eTable6 year5 geometric change is active2.97 and placebo3.02, matching the figure's active/Placebo GM labels while its Ns are reversed.
- Reported versus comparator: Figure overall Ns: placebo703/active609; Table1 totals: placebo289+320=609/active370+333=703. These are exact integer identities.
- Reproducible consistency rule: Aggregate mutually exclusive factorial arms by vitamin D assignment. The main report p3 says full analytic population follows randomized treatment regardless of adherence/follow-up. Figure does not disclose a differently defined population.
- Calculation and tolerance: 703−609=94 for each arm label (opposite signs); total1312 still reconciles, so a correct grand total does not reconcile arm attribution. No rounding tolerance. The figure also labels Omega3-randomization placebo row Ns333 and320 versus active rows370 and289, internally consistent with N columns belonging to opposite vitaminD cohorts.
- Source-grounded alternatives: Ns may denote a distinct figure population or the N column alone may have been transferred from reversed group ordering; no population definition supports placebo exceeding its enrolled609. Entire GM columns need not be reversed because eTable6 corroborates their displayed assignment.
- Missing definitions: Figure-specific N definition and imputed/subgroup membership provenance absent. No raw participant file supplied.
- Direct observation versus inferred mechanism: Values and labels above are source-visible; alternatives are conditional explanations and are not asserted as the production mechanism.
- Exact remaining human question: What do eFigure2 Ns count, and are the N columns assigned to the intended treatment labels independently of the GM and modeled ratio columns?
- Evidence links: [DOC-003 PDF p18](../../../joi190122supp2_prod.pdf#page=18); [DOC-001 PDF p5](../../../jama_de_boer_2019_oi_190122.pdf#page=5); [DOC-001 PDF p3](../../../jama_de_boer_2019_oi_190122.pdf#page=3); [DOC-003 PDF p11](../../../joi190122supp2_prod.pdf#page=11).

### STAT-UO06 — eFigure3 overall participant Ns oppose the randomized assignment totals

- Status: Pending Human Adjudication.
- Relationships: S296.
- Proposed primary category: Denominator, proportion, or total inconsistency.
- Compared locations and document roles: REPORT DOC-003 p19 overall N columns versus REPORT DOC-001 p5 Table1 factorial headers; REPORT DOC-003 p11 year5 geometric changes corroborate GM assignment only.
- Provisional primary relationship: S_C; all discrepancy relationships: S_C.
- Exact source evidence: DOC-003 p19 eFigure3 prints Placebo N659 and Active intervention N653. DOC-001 p5 factorial Ns370,333,289,320 imply omega3 active370+289=659 and placebo333+320=653. DOC-003 p11 omega3 geometric changes are active2.94 and placebo3.05, matching figure GM columns but not the displayed N assignment.
- Reported versus comparator: Figure placebo659/active653 versus randomized placebo653/active659.
- Reproducible consistency rule: Exact aggregation by omega3 randomization; report's full-population statement applies unless a distinct figure population is disclosed. Same totals do not reconcile crossed assignment labels.
- Calculation and tolerance: Placebo N differs+6 and active N−6; grand total1312 matches. No rounding. Figure vitaminD-randomization placebo Ns289/320 and vitaminD Ns370/333 follow opposite omega3 group Ns.
- Source-grounded alternatives: An undisclosed population or N-specific layout reversal could explain the print. Whole-column reversal is not justified because eTable6 confirms the current GM labels.
- Missing definitions: Specific figure-N definition, missingness and plot-generation source absent.
- Direct observation versus inferred mechanism: Values and labels above are source-visible; alternatives are conditional explanations and are not asserted as the production mechanism.
- Exact remaining human question: Are eFigure3 N columns labeled with the intended omega3 assignment, and which figure population do they describe?
- Evidence links: [DOC-003 PDF p19](../../../joi190122supp2_prod.pdf#page=19); [DOC-001 PDF p5](../../../jama_de_boer_2019_oi_190122.pdf#page=5); [DOC-001 PDF p3](../../../jama_de_boer_2019_oi_190122.pdf#page=3); [DOC-003 PDF p11](../../../joi190122supp2_prod.pdf#page=11).

### STAT-UO07 — eFigure2 and eTable6 print different overall vitamin D ACR treatment P values

- Status: Pending Human Adjudication.
- Relationships: S281.
- Proposed primary category: Statistical reporting inconsistency.
- Compared locations and document roles: REPORT DOC-003 p18 eFigure2 overall P versus REPORT DOC-003 p11 eTable6 vitaminD year5 P.
- Provisional primary relationship: S_W; all discrepancy relationships: S_W.
- Exact source evidence: DOC-003 p18 eFigure2 overall row prints P0.89 in the column headed p-value for interaction; same row GM changes placebo3.02 and active2.97. DOC-003 p11 eTable6 vitaminD year5 GM changes placebo3.02 and active2.97, modeled ratio0.99(0.84,1.17), P0.90. Both sources identify age/sex-adjusted change from baseline toyear5.
- Reported versus comparator: Printed overall P0.89 versus0.90 for apparently matching intervention/time/continuous outcome and age/sex adjustment. Figure-specific overall test/null is not separately defined.
- Reproducible consistency rule: Repeated outputs for the same exact fitted contrast and same rounding precision should agree; this check is conditional on confirming that the overall figure P tests the eTable6 contrast. Shared rounding alone does not make two distinct displayed values the same; however model/test differences could.
- Calculation and tolerance: Displayed difference .01. At two-decimal nearest rounding, .89 nominally represents[.885,.895), .90[.895,.905); these are adjacent disjoint bins except a shared boundary under unspecified tie rules. This is a display comparison, not normal/SE tail reconstruction.
- Source-grounded alternatives: Overall P may derive from a subgroup-expanded model, different imputation pooling, or a different test despite matching GM summaries. The figure header calls it interaction P, and the overall row has no subgroup; intended null is unclear. Therefore exact mismatch is conditional, not proof of statistical incompatibility.
- Missing definitions: Figure overall test/null, underlying unrounded P, exact fit/imputation/df alignment and rounding method not supplied.
- Direct observation versus inferred mechanism: Values and labels above are source-visible; alternatives are conditional explanations and are not asserted as the production mechanism.
- Exact remaining human question: Does eFigure2 overall P0.89 repeat the eTable6 vitaminD year5 test P0.90, and if so why do displayed values differ; if not, what separate test or model does it represent?
- Evidence links: [DOC-003 PDF p18](../../../joi190122supp2_prod.pdf#page=18); [DOC-003 PDF p11](../../../joi190122supp2_prod.pdf#page=11).

### STAT-UO08 — eFigure2 caption gives a time point as the active-assignment comparator

- Status: Pending Human Adjudication.
- Relationships: S281–S295.
- Proposed primary category: Measure, label, or scale inconsistency.
- Compared locations and document roles: REPORT DOC-003 p18 caption comparator versus same-page graph active/placebo heading.
- Provisional primary relationship: S_W; all discrepancy relationships: S_W.
- Exact source evidence: DOC-003 p18 caption reads “comparing the active treatment assignment to year 5, adjusted for age and sex.” The same-page graph labels the contrast active/placebo; the prior clause already defines baseline-to-year5 time.
- Reported versus comparator: Caption comparison active treatment assignment versus year5 versus graph comparison active treatment assignment versus placebo.
- Reproducible consistency rule: A treatment-assignment ratio compares two assignments; a follow-up year describes its measurement time. Distinct comparator identities cannot both define the printed active/placebo treatment contrast. This differs from the difference-versus-ratio measure rule.
- Calculation and tolerance: Categorical comparator identity only, no estimated endpoint or rounding tolerance.
- Source-grounded alternatives: Year5 may be a duplicated time phrase and the caption may intend active versus placebo at year5. That is a plausible editorial origin, not a supplied correction.
- Missing definitions: Caption intention absent; graph supplies explicit comparator but no production metadata.
- Direct observation versus inferred mechanism: Values and labels above are source-visible; alternatives are conditional explanations and are not asserted as the production mechanism.
- Exact remaining human question: Does the caption intend active versus placebo at year5, and what comparator should a reader attach to the reported ratio?
- Evidence links: [DOC-003 PDF p18](../../../joi190122supp2_prod.pdf#page=18).

### STAT-UO09 — eFigure3 caption gives a time point as the active-assignment comparator

- Status: Pending Human Adjudication.
- Relationships: S296–S306.
- Proposed primary category: Measure, label, or scale inconsistency.
- Compared locations and document roles: REPORT DOC-003 p19 caption comparator versus same-page active/placebo effect heading.
- Provisional primary relationship: S_W; all discrepancy relationships: S_W.
- Exact source evidence: DOC-003 p19 caption reads “comparing the active treatment assignment to year 5, adjusted for age and sex.” Graph heading is “Ratio of change, active/placebo (95% CI)”.
- Reported versus comparator: Active assignment compared with year5 in caption; active assignment compared with placebo in graph.
- Reproducible consistency rule: Assignment-contrast and time-point labels have distinct identities. This is a concrete comparator-label question for the reported ratio, not a broad prose critique.
- Calculation and tolerance: Direct label identity; no arithmetic tolerance, inferential approximation, or exact graphical endpoint needed.
- Source-grounded alternatives: A repeated follow-up phrase could be a copy error; intended graph contrast remains explicit. The source does not specify caption correction.
- Missing definitions: Caption/plot production intent absent.
- Direct observation versus inferred mechanism: Values and labels above are source-visible; alternatives are conditional explanations and are not asserted as the production mechanism.
- Exact remaining human question: What treatment comparator is intended in the eFigure3 caption, and does it match the active/placebo ratio heading?
- Evidence links: [DOC-003 PDF p19](../../../joi190122supp2_prod.pdf#page=19).

## Complete-scope limitations

The graph publishes no numeric point/CI endpoints and no per-subgroup test coefficient/SE/df; all plots were still inspected. Main article supplies2-tailed testing, random-intercept models and Rubin pooling, but does not supply per-cell variance components/dfs or Cox test construction. Descriptive geometric mean ratios need not algebraically reproduce adjusted graphical ratios, and no candidate is created by such a comparison. Similar sensitivity results belong to different populations; equal event counts or rate endpoints across distinct composites are not automatically duplicates. The eFigure2 overall P comparison remains explicitly conditional on test/model alignment. This shard performed no raw-data, external-literature or broad methodological audit. Candidate statements concern printed reporting consistency only; no conclusion effect is inferred.



# Statistical Pass 1: Supplement ACR Checker Part

- Agent: /root/stats_pass1_supp_acr, fresh gpt-6.1-sol/high; runtime ID tracked by coordinator.
- Exact scope: DOC-003 REPORT, joi190122supp2_prod.pdf pp. 11–14, eTables 6, 7, 8, and 9; all 96 estimate/95% CI fields plus 8 year-5 P values paired to contrasts.
- Inventory: statistics/parts/pass1_supp_acr_inventory.md; S401–S496, each PASS_1_COMPLETE.
- Independent emitted candidates: 1 (STAT-UA01); no stable C ID assigned by this checker.
- Limitations: exact table-specific marginal/change CI estimators, contrast test statistic, SE, reference distribution, df, covariance, variance estimator and MI pooling output unavailable. No source-coverage gap.
- Provenance: direct Poppler 26.01.0 pdftotext -layout -f 11 -l 14 joi190122supp2_prod.pdf -; source-matched current maps; visual source-matched reusable p12 render. No old candidates or report conclusions read, no web, no OCR required.

## Scope accounting

| Table and page | Relationships | Marginal GM/95% CI | Within-assignment ratio/95% CI | Active/placebo ratio/95% CI | Paired P | Completed |
|---|---|---:|---:|---:|---:|---|
| eTable6 p11 | S401–S424 | 12 | 8 | 4 | 2 | PASS_1_COMPLETE |
| eTable7 p12 | S425–S448 | 12 | 8 | 4 | 2 | PASS_1_COMPLETE |
| eTable8 p13 | S449–S472 | 12 | 8 | 4 | 2 | PASS_1_COMPLETE |
| eTable9 p14 | S473–S496 | 12 | 8 | 4 | 2 | PASS_1_COMPLETE |
| Total | 96 independent fields | 48 | 32 | 16 | 8 | PASS_1_COMPLETE |

Individual records, values, fields, row N, role, model and footnote definitions are retained in the inventory. A year-5 P remains integral to its D record. Baseline reference constants are recorded as 1.0 (Ref.) and do not inflate the interval count.

## Completed statistical checks and absence of other candidates

Every one of 96 points is contained in its positive, correctly ordered printed 95% CI. GM values use mg albumin/g creatinine; CA/CP/D use dimensionless ratios. Within-assignment change refers to baseline with reference1, and D compares active change against corresponding placebo change with null1. All 32 nonbaseline within-assignment ratios and lower endpoints exceed1; larger follow-up ACR geometric means are directionally compatible with increase. No negative-ratio or swapped-endpoint contradiction occurs.

All 16 active/placebo CIs include1 at printed precision. Eight year-5 P values (.90,.64,.77,.44,.87,.94,.90,.80 in table/intervention order) exceed.05. The interval/P observation is a qualitative diagnostic only: printed same-contrast 95% CI and P do not furnish the full inferential definition required to calculate exact P from the interval. No CI/P candidate is emitted on an assumed normal distribution, assumed df, assumed covariance, or assumed MI pooling rule. The two rounded1.00 year-2 lower endpoints receive no significance interpretation and have no printed P.

All label, reference, direction, duplicate-value and matched-repeat checks in the inventory are complete. Distinct sensitivity populations remain distinct; repeated rounded estimates do not by themselves establish duplication. Mixed-model adjusted contrast estimates are not required to equal divisions of separately imputed unadjusted summaries. Generic units boilerplate mentioning SD does not supersede explicit95% CI headers. No display-zero P occurs; the display-zero exclusion was applied.

## STAT-UA01 — ACR complete-case population count differs between title/arm totals and inclusion footnote

**Candidate statement:** eTable7 labels the baseline/year-5 available-measurement ACR analysis N=944 and prints active/placebo arm counts summing to944 for both assignments at baseline and year5. Its footnote says991 participants donated both urine samples and “were included in this analysis.” These reported inclusion totals differ by47.

**Suggested primary category for registration:** Denominator, proportion, or total inconsistency.

**Compared document roles and exact locations:**

1. REPORT DOC-003 results supplement [PDF p12](../../../joi190122supp2_prod.pdf#page=12), eTable7 title: “Among Participants With Available Baseline and Year 5 Measurements (N = 944*)”.
2. REPORT DOC-003 same [PDF p12](../../../joi190122supp2_prod.pdf#page=12), eTable7 Vitamin D baseline and year5 N columns:504 active,440 placebo; omega-3 baseline and year5 N columns:477 active,467 placebo.
3. REPORT DOC-003 same [PDF p12](../../../joi190122supp2_prod.pdf#page=12), eTable7 footnote*:1,312 enrolled;1,311 donated baseline urine;991 also donated year5 urine “and were included in this analysis”;320 baseline-only participants excluded;1 without baseline urine excluded.

**Relationship role rationale:** all discrepancy endpoints lie within one non-plan results supplement, so S_W. No PLAN comparator is implicated. Classification ambiguity: donation versus analyzable measurement may be different populations, but the footnote expressly calls991 included in this analysis.

**Relationships affected:** population key P7 and all eTable7 field records S425–S448. No estimate/CI containment contradiction is alleged.

**Printed rule and reproducible calculation:** active and corresponding placebo assignment arms partition a factorial-assignment comparison;504+440=944 and477+467=944. The footnote's own arithmetic is coherent:1,311−320=991;1,312−320−1=991. But991−944=47. A complete-case analysis described by a single N cannot simultaneously have included totals944 and991 without a supplied distinction.

**Tolerance:** integer count identities; rounding tolerance0 participants. This is not an interval- or P-value approximation.

**Direct observation versus inference:** the title944, four arm totals944 and explicit footnote991 are direct printed observations confirmed by current direct PDF text and the source-matched rendered p12 page. The numerical difference47 is exact arithmetic. A copied footnote or an extra47-person assay/missing-measurement exclusion is a possible explanation, not a supplied fact.

**Source-grounded alternatives and missing definitions:** the table could include only participants with analyzable ACR values, while991 donated urine; donor status and available measured ACR need not be identical. The source provides no47-person attrition bridge and says991 were included, leaving the label conflict. The MI footnotes might use a larger inferential population than displayed complete-case N, but no such distinct991-person modeling population is identified in the title or footnote. No participant-level assay-validity record or model N is supplied.

**Exact human question:** Which population and exclusion rule generated eTable7's geometric means, change ratios, CIs and P values:944 with analyzable baseline/year5 ACR,991 donors, or different descriptive/model populations? What supplied record accounts for47 people between donation and reported available measurements?

**Human verification steps:** open source PDF p12; read title and all four baseline/year5 assignment totals; read footnote* and its exclusions; identify any stated distinction between donated urine and analyzable paired ACR or between descriptive and MI model N. Recompute both independent sums and footnote remainder. Preserve the candidate pending that definition.

**Quality-control relevance:** the printed population attached to an ACR complete-case sensitivity result is inconsistent. If confirmed, a downstream extractor could copy the wrong analysis sample size or available-case definition. This does not establish that the estimates or the paper conclusion are wrong.

**Status:** Pending Human Adjudication. No severity, validity, acceptance, or correction assigned.

## Handoff

Complete assigned scope: all96 ACR estimate/95% CI fields, all8 paired P values, all baseline reference constants, model/scale/population footnotes and within-scope repetitions. One candidate, STAT-UA01. Coordinator may merge this with a genuine numeric-lane duplicate before C IDs. Fresh pass2 must revisit every S record using complete cross-lane ledger and recheck; this pass1 agent must not serve as pass2.



# Statistical Pass 1 PLAN Extension Checker

- Runtime agent ID: 01a1288b-cbda-7140-94f6-958da8f7a6b8
- Model: gpt-6.1-sol
- Reasoning effort: high
- Start mode: FRESH_SPAWN
- Task: /root/stats_pass1_plan_extension
- Exact scope: DOC-002 PLAN pp. 17-23 and 31-33 formulas, inferential rules, power and monitoring; p. 9 total-PUFA, omega-3 and omega-6 InCHIANTI tests; p. 6 Figure3 survival strata; p. 7 Figure5 curves and stars.
- Relationships: 95, S601-S695, all PASS_1_COMPLETE.
- Local candidates: 3, STAT-PE01, STAT-PE02, STAT-PE03.
- Inventory artifact: statistics/parts/pass1_plan_extension_inventory.md.
- Human status: Pending Human Adjudication.

This fresh shard is separate from primary pass 1 and all supplemental-result shards. It cannot serve as pass 2. Canonical S merge and stable C registration belong to the coordinator. Every relationship is listed individually in the inventory, including all twelve Table2 power cells and all three distinct InCHIANTI tests. No candidate-count threshold was used.

## Applied check coverage

For every record, check printed interval endpoint ordering and point containment when endpoints exist, sign/direction, scale/unit/effect measure, matchable cross-location repetition, and supplied inferential definitions. This extension has no printed numeric estimate-CI pair for the three historical InCHIANTI tests or planned coefficients. Historical survival and ACR curves were inspected visually, with graphical domain/direction checks and no reconstruction of unprinted exact coordinates or CI endpoints. Power cells were separately checked for [0,1] bounds, direction with effect magnitude, exact narrative repetitions and printed four-year units.

Exact P/CI/test/statistic/SE compatibility is unavailable when definitions are missing. Neither sidedness nor df, covariance, variance estimator or power algorithm was supplied for original ANCOVA cells; none was inferred. Addendum explicitly supplies two-sided alpha.05 but not simulation covariance and implementation. The monitoring diagnostic 2×standard-normal upper-tail(3)≈.0026998 agrees with printed P=.0027 to four decimals; it is explicitly a conditional two-sided standard-normal diagnostic, not a claim the source named sidedness. No candidate relies on a reconstructed test or normal approximation.

All locations compared below are PLAN by content. Protocol background/historical results stay PLAN. No REPORT location contributes to these three discrepancies, so each provisional relationship is P_P only; coordinator determines stable classification. No P display zero occurs; coherent display zeros would be DISPLAY_ZERO_NOT_CANDIDATE. No candidate concerns literal-zero formatting or unreported definitions alone.

## STAT-PE01 — Original eGFR outcome called dichotomous and continuous

**Linked relationship:** S617.

**Candidate statement:** The original protocol calls the same eGFR-change outcome a secondary dichotomous outcome and immediately states it is analyzed as a continuous variable. The printed variable-type label conflicts with the displayed change formula and subsequent continuous ANCOVA specification.

**Compared locations and roles:**
- PLAN [DOC-002 PDF p.17, VI.c opening sentence](../../../joi190122supp1_prod.pdf#page=17): “As a secondary dichotomous outcome” followed by change in eGFR from baseline to year4, “analyzed as a continuous variable.”
- PLAN [DOC-002 PDF p.17, VI.c change definition](../../../joi190122supp1_prod.pdf#page=17): eGFR4−eGFR0, without a binary threshold for this continuous outcome.
- PLAN [DOC-002 PDF p.18, VI.e and Equation4](../../../joi190122supp1_prod.pdf#page=18): ACR and eGFR changes “are continuous variables” tested using ANCOVA; eGFR4 is modeled on baseline eGFR and treatment assignment.

**Printed versus comparator:** “dichotomous” versus “continuous,” for the same baseline-to-year4 eGFR change. The separate binary composite endpoint on p17 is a different outcome and is not used as a comparator.

**Rule and calculation:** A single specified analysis variable cannot simultaneously carry mutually different dichotomous and continuous type labels under the same stated definition. The formula eGFR4−eGFR0 carries no threshold-based two-category coding, and Equation4 has continuous eGFR outcome. This is a direct label identity comparison, not a reconstruction of fitted data. Rounding tolerance: not applicable.

**Direct observation versus inference:** Both labels and the unthresholded formula are directly printed and visually confirmed. A copied word from the next composite paragraph is a possible explanation only; no production mechanism is asserted.

**Missing definition:** No additional mathematical input is required for the wording conflict. Whether the word “dichotomous” was intended to refer to another secondary outcome requires author clarification.

**Alternative supplied-source interpretation:** The following composite paragraph is dichotomous and could be the intended referent; the opening sentence explicitly names eGFR change and continuous analysis, leaving a local wording question.

**Human question:** Which outcome does “secondary dichotomous” modify, and what variable-type label was intended for the eGFR4−eGFR0 ANCOVA outcome?

**Provisional classification:** Measure, label, or scale inconsistency; P_P; all relationships P_P; compared PLAN versus PLAN; derived review domain plan_material. No evidence-state or disposition assignment made by this checker.

**Source confirmation:** Exact p17/p18 source-matched rendered pages visually inspected. Native/layout transcription agrees.

**Bounded relevance:** A data extractor could copy an incorrect continuous/binary endpoint label from protocol metadata; no effect on paper conclusions is inferred.

## STAT-PE02 — Table2 co-primary label differs from original endpoint hierarchy

**Linked relationship:** S618; corroborating power values S643-S654 and repeated narrative S655.

**Candidate statement:** Table2 titles urine ACR and eGFR as co-primary outcomes, while the same original protocol explicitly labels ACR primary and eGFR secondary.

**Compared locations and roles:**
- PLAN [DOC-002 PDF p.17, VI.b](../../../joi190122supp1_prod.pdf#page=17): primary outcome is baseline-to-year4 urine ACR change.
- PLAN [DOC-002 PDF p.17, VI.c](../../../joi190122supp1_prod.pdf#page=17): eGFR change from baseline to year4 is in secondary study outcomes.
- PLAN [DOC-002 PDF p.19, Table2 title and VI.h narrative](../../../joi190122supp1_prod.pdf#page=19): “Study power for co-primary study outcomes, by effect size”; columns urine ACR and estimated GFR. Nearby prose also calls them co-primary continuous outcomes.

**Printed versus comparator:** The same original four-year ACR/eGFR pair has primary/secondary hierarchy in VI.b/VI.c, versus co-primary hierarchy in the power table and prose. Numerical90% entries17% ACR and2.6eGFR agree between table and narrative; the candidate is the inferential endpoint label, not a numeric power mismatch.

**Rule and calculation:** Match same plan version, baseline-to-year4 time and continuous outcomes. “Co-primary” places both outcomes in the primary tier; “primary ACR/secondary eGFR” places eGFR in a different tier. Direct label comparison; no numerical calculation or rounding tolerance needed.

**Direct observation versus inference:** Hierarchy words are directly observed on p17/p19 and visually confirmed. No multiplicity violation or actual analysis departure is inferred. The explicit p31-33 amendment changes hierarchy/time later and does not resolve differing labels within the original plan.

**Missing definition:** Whether “co-primary” was a generic power-table descriptor, an intended original hierarchy, or an unreconciled wording carryover is not specified. Original alpha.05 without correction is printed but does not adjudicate the labeling question.

**Alternative supplied-source interpretation:** Power was calculated for both continuous outcomes; “co-primary” might have been used informally to group their calculations. VI.b/VI.c remain formally different labels.

**Human question:** Which endpoint hierarchy should be extracted for the June28,2010 original protocol, and was the p19 co-primary label intended to supersede p17?

**Provisional classification:** Measure, label, or scale inconsistency; P_P; all relationships P_P; PLAN versus PLAN; derived review domain plan_material. No evidence state or suggested disposition assigned here.

**Source confirmation:** Original p17 and p19 source-matched rendered pages visually inspected; exact title and text match current extraction.

**Bounded relevance:** Protocol-based extraction could classify eGFR as primary or secondary depending on which supplied section is copied. No protocol-violation or conclusion-impact judgment made.

## STAT-PE03 — Exponentiated ACR coefficient labeled as relative contrast of percent changes

**Linked relationship:** S623; same parallel omega3 interpretation tracked S625.

**Candidate statement:** The original plan defines percent change as (ACR4−ACR0)/ACR0, then states that exp(beta2)−1 from an ANCOVA of log(ACR4) represents the relative difference in that percent change. At a common baseline, the supplied equation identifies an exponentiated follow-up ratio; the relative difference between the defined changes is generally a different quantity.

**Compared locations and roles:**
- PLAN [DOC-002 PDF p.17, VI.b](../../../joi190122supp1_prod.pdf#page=17): percent change is summarized as (ACR4−ACR0)/ACR0.
- PLAN [DOC-002 PDF p.18, VI.e Equation3 and following coefficient definition](../../../joi190122supp1_prod.pdf#page=18): log(ACR4)=beta0+beta1log(ACR0)+beta2(vitamin D)+e; log is explicitly natural log in the prior equation. “[exp(beta2)−1] represents the relative difference in percent change in albuminuria” comparing active vitaminD to placebo; accompanying95%CI/P assess treatment effect.
- PLAN [DOC-002 PDF p.18, parallel equations statement](../../../joi190122supp1_prod.pdf#page=18): same form is proposed for omega3. This is shared provenance, not another distinct candidate.

**Rule and calculation:** Hold the supplied baseline and the fitted equation's non-treatment components fixed. Let B be the common positive baseline ACR; P and A the exponentiated modeled log-follow-up values for placebo and active treatment. Equation3 gives q=A/P=exp(beta2). Defined changes are cP=(P−B)/B and cA=(A−B)/B. For cP nonzero, their relative difference is (cA−cP)/cP=(A−P)/(P−B)=(q−1)×P/(P−B), which is generally different from q−1. Multiplying both c values by100 to report percentage units does not remove the difference. No covariance or inferential convention is needed for this algebraic scale distinction. Tolerance: exact algebra, no rounding.

**Labeled diagnostic example:** Hypothetical values B=100, P=200, A=100 give q=.5 and exp(beta2)−1=−.5, while defined change is1 (100%) for placebo and0 for active; relative difference in changes is−1 (−100%). These are demonstration inputs, not observed study data and not a reconstructed treatment estimate.

**Direct observation versus inference:** Both the change formula and coefficient label are directly printed and visually confirmed. The derivation is a deterministic identity using the supplied equation at common baseline. It does not assume beta1=1, fit a model, infer an SE or prescribe a new estimate.

**Missing definition:** The protocol does not define whether “relative difference in percent change” is informal shorthand for a baseline-adjusted geometric follow-up ratio, a ratio of fold changes, or the literal relative difference of the VI.b defined changes. Link-function prediction versus arithmetic means, retransformation and exact estimand mapping are unreported; the demonstration concerns exponentiated fitted log values, not arithmetic-mean predictions.

**Alternative supplied-source interpretation:** If the phrase informally refers to the ratio of follow-up/baseline fold changes, q−1 can express a proportional contrast at common baseline. That requires distinguishing fold change ACR4/ACR0 from the printed fractional increment (ACR4−ACR0)/ACR0.

**Human question:** Was exp(beta2)−1 intended as a baseline-adjusted proportional follow-up difference or ratio-of-fold-changes contrast, and how should its label distinguish it from a literal relative difference between VI.b defined percent changes?

**Provisional classification:** Measure, label, or scale inconsistency; P_P; all relationships P_P; PLAN versus PLAN; derived review domain plan_material. No evidence-state or disposition assignment made.

**Source confirmation:** Exact p17 formula and p18 Equation3/label visually confirmed in source-matched renders; current native/layout transcription agrees.

**Bounded relevance:** An extractor could treat the coefficient as a relative contrast of percentage increments instead of the modeled multiplicative ACR contrast. No actual numerical treatment estimate or paper conclusion is adjudicated.

## Non-candidate records and precise limitations

- S601-S603: three independent bounded P<.0001 tests have coherent direction but no coefficients, CIs or exact test definitions; no contradiction inferred.
- S604-S615: Figure3 survival [0,1] domain and Figure5 positive ACR/direction are coherent. N691 is total historical sample, not a risk-set denominator. Star thresholds, groups, error-bar type, CI levels and curve coordinates are unprinted.
- S640-S666: Original power domain, monotonicity, time units and exact table/narrative values reconcile. Original ANCOVA sidedness, df, power algorithm and percent-effect orientation are absent. No assumption that composite incidence equals sum of overlapping component incidences.
- S656: Dilution arithmetic17/.8=21.25 and2.6/.8=3.25 is diagnostic; published21%/3.2 may reflect rounding or imperfectly specified dilution, and no supplied rounding rule establishes a contradiction.
- S667-S668: Z3/P.0027 agrees with an explicitly conditional two-sided standard-normal diagnostic; repeated-look exact familywise alpha cannot be calculated from the supplied schedule/variance information.
- S669: Plan10 imputations is retained literally. Report comparison belongs to matched cross-source checking, rather than an independent emitted record here.
- S670: Equation1 omits a separately printed common time term while Equation2 prints one. Missing intended coding/constraints/error definitions create an implementation limitation, not a candidate solely from an omitted model term.
- S671-S676: Categorical times0,2,5, interaction threshold.05,95%CI and year5-only inference are retained literally; no scalar/joint interaction test or unprinted year2 P inferred.
- S678-S684: Original versus amended subgroup directions are version-keyed; an explicitly disclosed amendment is not automatically a same-result contradiction.
- S688-S691:2000replications,1058(80%) and80%power at2.3 are coherent with graphic direction. Inverse1058/.8=1322.5 is only a diagnostic treating rounded80% exact; no printed denominator in this section creates an impossible sample. Simulation covariance/algorithm and exact curve points absent.
- S692-S695: Four safety incidence comparisons are prospective rules, with no observed counts/rates/person-time/P/CI or test. Neither incidence-rate nor proportion interpretation is forced.

All95 relationship records are PASS_1_COMPLETE. Fresh pass2 must revisit S601-S695 using the complete cross-lane ledger and mechanical recheck, including the three local candidates after stable registration. Candidate discovery remains uncapped; there are no severity/validity/adjudication labels.



