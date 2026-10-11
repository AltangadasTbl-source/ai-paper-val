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
**Compared locations and document roles:** REPORT [DOC-001 Figure3 PDFp8](../../../../jama_de_boer_2019_oi_190122.pdf#page=8) overall N and headers versus REPORT [DOC-001 abstract PDFp1](../../../../jama_de_boer_2019_oi_190122.pdf#page=1) four randomized arms; corroborating REPORT Table2 p8 active/placebo year5 changes.
**Source evidence:** Figure3 Placebo N703, meanchange-13.1(SD14.4); VitaminD N609, change-12.3(SD14.8). Abstract D+O370,D+placebo333,placebo+O289,doubleplacebo320.
**Calculation/rule:** ActiveD370+333=703; Dplacebo289+320=609. Count printed under placebo exceeds the entire randomized Dplacebo population by94; both overall printed Ns are reversed. Count tolerance zero. Right-hand change-12.3 matches Table2 activeD, so changing both whole-column treatment labels would create a different mean-label conflict.
**S relationships:** S049-S063; the directly registered count contradiction is overall S049. Remaining subgroup counts require exact numeric-lane comparator support before separate registration; do not infer subgroup denominators.
**Alternatives and missing inputs:** Missing source model output does not erase randomized population identity. N may have been placed under wrong headers; raw output would establish intended labels. No claim about fitted CI computation or effect conclusion.
**Human question:** Which assignment populations do the Figure3 N columns represent, and were count columns placed under the wrong treatment labels?
**Classification information:** REPORT versus REPORT inside main; S_W. No PLAN comparator. Pending Human Adjudication.

## STAT-MP02 — Figure4 overall assignment counts conflict with randomized intervention identities

**Candidate statement:** Figure4 places659 participants under Placebo and653 under Omega-3 Fatty Acids, while randomized arms imply activeomega3=659 and omega3placebo=653.
**Primary category:** Denominator, proportion, or total inconsistency.
**Compared locations and document roles:** REPORT [DOC-001 Figure4 PDFp9](../../../../jama_de_boer_2019_oi_190122.pdf#page=9) versus REPORT [DOC-001 abstract PDFp1](../../../../jama_de_boer_2019_oi_190122.pdf#page=1) randomized arms; REPORT Table2 p8 corroborates displayed meanchange treatment identity.
**Source evidence:** Overall Placebo659/-13.1(SD14.8); Omega3 653/-12.2(SD14.5).
**Calculation/rule:** ActiveO370+289=659; Oplacebo333+320=653. Figure placeboN exceeds entire randomized Oplacebo count by6; Ns reversed. Zero count tolerance. Means remain in intended Table2 placebo/active order.
**S relationships:** S064-S074; directly contradicted overall record S064. Distinct figure/population/values from STAT-MP01, so not automatically merged for a shared apparent cause.
**Alternatives and missing inputs:** Source model output absent; erroneous N placement is plausible but not adjudicated. Whole-column header swap would reverse correct meanchanges.
**Human question:** Which assignment populations do Figure4 N columns denote?
**Classification information:** REPORT versus REPORT within main; S_W. Pending Human Adjudication.

## STAT-MP03 — Omega3 correlation x-axis names DHA/EPA while matched result defines sum percentage index

**Candidate statement:** eFigure1 describes omega-3 index changes but labels its right x-axis “Change in DHA/EPA (Year2-BL)”; the main Methods explicitly defines the omega-3 index as EPA plus DHA as a percentage of total fatty acids. A ratio label and a sum percentage index denote different measures.
**Primary category:** Measure, label, or scale inconsistency.
**Compared locations and document roles:** REPORT [DOC-003 eFigure1 PDFp17](../../../../joi190122supp2_prod.pdf#page=17) caption and right-axis label versus REPORT [DOC-001 Methods PDFp3](../../../../jama_de_boer_2019_oi_190122.pdf#page=3) omega-3 index definition and REPORT [DOC-001 Results PDFp4](../../../../jama_de_boer_2019_oi_190122.pdf#page=4) narrative correlation.
**Source evidence:** eFigure1 caption names changes in omega-3 index; right correlationr=-.02, x-axis DHA/EPA without percentage units. Main definition: EPA plusDHA as%totalfattyacids.
**Calculation/rule:** DHA/EPA is a quotient if slash is mathematical; index=100*(EPA+DHA)/(totalfattyacids). These expressions are not identical. No numerical transform or p-value recalculated.
**S relationships:** S094.
**Alternatives and missing inputs:** Slash may be shorthand listing two constituents rather than division; supplied plotting code/data do not settle the intended variable. Consequently the registered issue is a conditional measure-label inconsistency, not a claim r itself is wrong.
**Human question:** Does the right panel plot the omega-3 percentage index change or a DHA-to-EPA ratio change, and was the slash intended as listing shorthand?
**Classification information:** S_C for main definition versus results-supplement axis; S_W for supplement caption versus its axis. Primary precedence S_C; all relationships S_C,S_W. Both documents REPORT. Pending Human Adjudication.

## STAT-MP04 — Figure2 quartile border order conflicts with increasing vertical scales

**Candidate statement:** Figure2 caption says top and bottom borders show first and third quartiles respectively, but each vertical axis increases upward and the first quartile cannot exceed the third.
**Primary category:** Measure, label, or scale inconsistency.
**Compared locations and document roles:** REPORT [DOC-001 Figure2 PDFp7](../../../../jama_de_boer_2019_oi_190122.pdf#page=7), caption “top and bottom box borders indicate the first and third quartiles, respectively” versus increasing eGFR axes0-to200 and increasing urineACR log axes0.1-to10000 on the same source page.
**Calculation/rule:** Q1<=median<=Q3, monotone vertical scale; top border>=bottom border. Assigning top=Q1 and bottom=Q3 reverses displayed order except for a zero-height box, whereas the printed boxes have nonzero height. No exact quartile coordinates invented.
**S relationship:** None; descriptive boxplot/IQR relationship retained for numeric-lane cross-reference, not mislabeled inferentialCI.
**Alternatives and missing inputs:** Caption word order may be transposed. Exact quartiles are absent but are not needed for the order rule; logarithmic ACR scale remains monotonic.
**Human question:** Which quartile was intended for each box border in Figure2?
**Classification information:** S_W, REPORT within main. Pending Human Adjudication.

## STAT-MP05 — Figure2B omega3 eGFR participant rows repeat vitaminD rows

**Candidate statement:** Figure2B labels omega3/placebo eGFR contributor counts as the vitaminD counts rather than the matched omega3 counts in Table2.
**Primary category:** Denominator, proportion, or total inconsistency.
**Compared locations and document roles:** REPORT [DOC-001 Figure2 PDFp7](../../../../jama_de_boer_2019_oi_190122.pdf#page=7) PanelB versus REPORT [DOC-001 Table2 PDFp8](../../../../jama_de_boer_2019_oi_190122.pdf#page=8), omega3 rows, matching measured eGFR by assignment and baseline/year2/year5.
**Source evidence:** PanelB printed placebo607,459,438; omega3 701,531,496. Table2 omega3 placebo651,491,462; active657,499,472. PanelA vitaminD counts exactly match PanelB's repeated values.
**Calculation/rule:** PanelB active-minus-Table2 discrepancy44,32,24 and placebo discrepancy-44,-32,-24 across three times. Count tolerance zero; same measure/time/source cannot be matched by rounding. Baseline active701 exceeds randomized omega3active659.
**S relationships:** Table2 measured mean/CI S013-S016,S020-S021 supply the matched count-population context; boxplot is descriptive and needs numeric-lane ID.
**Alternatives and missing inputs:** Counts might have been copied across panels; graph plotting/source count output absent. Do not assume the graphical distributions are also copied.
**Human question:** What are the actual contributor counts for PanelB's plotted omega3 and placebo groups at each time?
**Classification information:** S_W, REPORT within main. Pending Human Adjudication.

## STAT-MP06 — Figure2D omega3 ACR participant rows repeat vitaminD rows

**Candidate statement:** Figure2D prints omega3/placebo urineACR participant counts that reproduce vitaminD PanelC counts and disagree with matched omega3 rows in eTable6.
**Primary category:** Cross-document numeric inconsistency.
**Compared locations and document roles:** REPORT [DOC-001 Figure2 PDFp7](../../../../jama_de_boer_2019_oi_190122.pdf#page=7) PanelD versus REPORT [DOC-003 eTable6 PDFp11](../../../../joi190122supp2_prod.pdf#page=11), matching baseline/year2/year5 ACR contributor N for omega3 assignment. PanelC is within-main duplicate corroboration only.
**Source evidence:** PanelD placebo609,463,440; omega3 702,529,505. eTable6 omega3 placebo653,490,467; active658,502,478. eTable6 vitaminD active702,529,505; placebo609,463,440.
**Calculation/rule:** PanelD active discrepancies44,27,27; placebo-44,-27,-27. Zero count tolerance. Baseline active702 exceeds randomized omega3active659. eTable6 and Figure2 supply observational N while modeled change uses imputation; that distinction does not explain copied observational N.
**S relationships:** Non-inferential contributor identity; reference supplemental ACR statistical shard's eTable6 marginals at canonical merge, never recreate its owned S records.
**Alternatives and missing inputs:** Source plot output absent; copied count-row values plausible. No claim plotted ACR boxes or model estimates were copied.
**Human question:** Which participant counts correspond to the plotted PanelD groups, and why do PanelD and eTable6 differ for the same assignment/time?
**Classification information:** S_C, different REPORT documents. Main PanelC merely corroborates repetition and is not an additional discrepancy relationship. Pending Human Adjudication.

## Handoff limits

All six candidates require exact-source mechanical recheck and stable registration by coordinator; no severity, evidence-state adjudication or final correction is assigned here. Candidates may duplicate independently discovered numeric/cross-source records only when exact compared values/locations/rule agree. Figure3 and Figure4 overall count discrepancies are different comparisons. Main Figure2 eGFR and ACR copied-count discrepancies are different outcomes/documents and remain separate absent a genuine identity rule.

No candidate is emitted solely for absent inferential definitions, graphical endpoint precision, shared calibrationr, coherent threshold-rounded HR/P or finite precision zero notation. No claim paper conclusions are wrong. Bounded downstream concern is extraction of wrong assignment N, contributor N, quartile description or biomarker measure if human review confirms the labels/counts.

