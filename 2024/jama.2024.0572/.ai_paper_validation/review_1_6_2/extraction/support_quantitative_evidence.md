# Support quantitative evidence: results A

Exact scope: DOC-005 physical PDF pages 1-7 (PLAN), DOC-006 physical PDF pages 1-32 (REPORT). All 39 pages mapped; reusable-backed 39; fresh-required 0; gaps 0. Mapping is rebuilt from supplied factual sources, without candidate diagnosis. Local A identifiers are coordinator-remapping keys; row suffixes identify distinct relationships.

Sources: [analysis SAP](../../../joi240006supp4_prod_1708623115.00733.pdf#page=1), [results supplement](../../../joi240006supp5_prod_1708623115.01733.pdf#page=1). Links resolve from this part; coordinator adjusts one directory upward in the merged extraction. All page references below are physical PDF pages; DOC006 printed folio is physical page minus 1 from page2 onward.

Provenance: reusable DOC005 review_1_5_3/preprocessing/support_mapper_fresh/DOC-005/by_page.txt and layout.txt; reusable DOC006 preprocessing/DOC-006-RESULTS-SUPP/native_text/page-001.txt through page-032.txt; reusable page_images/page-005.png through page-032.png, all28 inspected visually with view_image. Legacy extraction engine/version unrecorded; fitness verified by curator and source identity. No new extraction, rendering or OCR derivatives produced. Compute device CPU; tools follow tooling_record.md (Poppler26.01.0, tesseract5.5.0 available). No Office/workbook/CSV sources assigned, so formulas versus cached cells not applicable. Printed formulas below are plan definitions, not workbook formulas. Sources/reused assets preserved.

## Every-page coverage

| Source | Physical page | Applicable mapping / inspected content |
|---|---:|---|
| DOC005 | 1 | Title and contents; no independent result values |
| DOC005 | 2 | A001 version/date and prespecified secondary-analysis identity |
| DOC005 | 3 | A002-A006 aims, population, imaging, mismatch/concordance definitions, principles |
| DOC005 | 4 | A007-A010 missing data, mRS merging, models/adjustments, plot fallback |
| DOC005 | 5 | A011-A014 binary safety outcomes, thresholds, interaction, ASPECTS |
| DOC005 | 6 | A015-A017 detailed ASPECTS, mismatch, concordance analyses |
| DOC005 | 7 | A018 disclosed post hoc appendix |
| DOC006 | 1 | Title; eMethods/eFigures1-20/eTables1-13, no independent numeric result |
| DOC006 | 2 | Contents first half; no independent numeric result |
| DOC006 | 3 | Contents second half; no independent numeric result |
| DOC006 | 4 | A019 explanatory model comparison/eMethods |
| DOC006 | 5 | A020 rCBF/Tmax mismatch example and threshold maps |
| DOC006 | 6 | A021 illustrative CT/CTP/DWI labels and RAPID numeric overlay |
| DOC006 | 7 | A022 continuation DWI images; no quantitative labels beyond folio |
| DOC006 | 8 | A023 complete cohort flow/counts |
| DOC006 | 9 | A024 eFigure4 all8 time bins |
| DOC006 | 10 | A025 eFigure5a,b all16 paired rows and trend tests |
| DOC006 | 11 | A026 eFigure5c,d all16 paired rows and trend tests |
| DOC006 | 12 | A027 eFigure6a,b all8 paired rows and trend tests |
| DOC006 | 13 | A028 eFigure7 all16 forest rows |
| DOC006 | 14 | A029 eFigure8 all16 forest rows |
| DOC006 | 15 | A030 eFigure9 all16 forest rows |
| DOC006 | 16 | A031 eFigure10 all16 forest rows |
| DOC006 | 17 | A032 eFigure11 all16 forest rows |
| DOC006 | 18 | A033 eFigure12 all16 forest rows |
| DOC006 | 19 | A034 eFigure13 all16 forest rows |
| DOC006 | 20 | A035 eFigure14 all4 probability/odds panels |
| DOC006 | 21 | A036 eFigure15 all4 probability/odds panels |
| DOC006 | 22 | A037 eFigure16 all4 probability/odds panels |
| DOC006 | 23 | A038 eFigure17 all4 probability/odds panels |
| DOC006 | 24 | A039 eFigure18 all3 contour panels |
| DOC006 | 25 | A040 eFigure19 all3 contour panels |
| DOC006 | 26 | A041 eFigure20a-d; heading e deferred to page27 |
| DOC006 | 27 | A041 eFigure20e-h; heading i deferred to page28 |
| DOC006 | 28 | A041 eFigure20i-l; heading m deferred to page29 |
| DOC006 | 29 | A041 eFigure20m-p; heading q deferred to page30 |
| DOC006 | 30 | A041 eFigure20q-t |
| DOC006 | 31 | A041 eFigure20u-w; heading x deferred to page32 |
| DOC006 | 32 | A041 eFigure20x-aa |

## Prospective analysis-specific plan relationships (DOC005 PLAN)

| ID | Page | Definition/specification | Matching report key |
|---|---:|---|---|
| A001 | 2 | Prespecified secondary SELECT2 analysis; SAP version1.0.0; July7,2023 | analysis status |
| A002 | 3 | All enrolled SELECT2 patients included for imaging-specific EVT treatment effect | cohort/analysis population |
| A003 | 3 | Core-lab CT ASPECTS; automated RAPID rCBF<30% CTP / ADC<620 X 106mm/s2 MRI printed notation; all baseline NCCT manually delineated hypodensity | imaging definitions |
| A004 | 3 | Primary ischemic volume=max(CTP/MRI core, CT hypodensity); sensitivity CTP/MRI-only | composite versus perfusion core |
| A005 | 3 | Mismatch volume=critically hypoperfused Tmax>6s volume minus core; ratio printed as ratio of core and critically hypoperfused volume. Favorable profile1 ratio≥1.8 AND volume≥15mL; profile2≥1.2 AND≥10mL | mismatch definitions/eFigure1 |
| A006 | 3 | Discordant1 core<70mL and ASPECTS≤5; discordant2 core≥70mL and ASPECTS>5; concordant core≥70mL and ASPECTS≤5. As-treated all analyses; exploratory; no multiplicity adjustment | concordance/analysis population |
| A007 | 4 | Continuous covariates require no substantial deviation from linearity; otherwise transformations considered; predictive margins/marginal probabilities plots; mRS5 and6 merged for distribution analyses; Stata/R; no missing-data imputation | models/missingness |
| A008 | 4 | 90-day mRS distribution using probabilistic index model adjusted age, presentation NIHSS, LKW-to-randomization time, ischemic core volume; exclude stratification variable from covariates; mRS5/6 merged | primary shift/GenOR |
| A009 | 4 | Functional independence mRS0-2 modified Poisson robust standard errors; same four prognostic covariates; exclude stratifier; logistic if better calibrated for marginal-probability plots | mRS0-2 RR/plots |
| A010 | 4-5 | Independent ambulation mRS0-3 modified Poisson robust standard errors; same covariates/stratifier exclusion/logistic calibration fallback | mRS0-3 RR/plots |
| A011 | 5 | Additional EVT subgroup independent-ambulation predicted probabilities combining age and LKW-to-randomization time | contour plots time origin |
| A012 | 5 | Complete dependence/death mRS5-6 modified Poisson robust standard errors, same covariates/exclusion/logistic plot fallback | mRS5-6 RR/plots |
| A013 | 5 | sICH=parenchymal hemorrhage typeII or remote parenchymal hemorrhage on follow-up associated with NIHSS rise≥4 at4-hour window; few events: counts/proportions only, no further testing/modeling | safety outcome |
| A014 | 5 | Core thresholds <70/≥70, <100/≥100, <150/≥150mL; treatment interaction; ASPECTS strata0-2,3-5,6-10 | forest groups |
| A015 | 6 | Within ASPECTS3-5 repeat at each score3,4,5; ASPECTS×treatment interactions | forest ASPECTS subgroups |
| A016 | 6 | Prespecified mismatch profiles; additional volume50/100mL thresholds; interaction; continuous mismatch association in EVT | mismatch strata/models |
| A017 | 6 | Prespecified concordant/discordant imaging profiles, outcomes and treatment interactions | concordance tables |
| A018 | 7 | Appendix explicitly post hoc after SAP finalized: CT hypodensity third volume; mismatch using larger modality; significant core overestimation; follow-up infarct volume; within-patient hypodensity vs CTP/MRI | report post hoc status |

## Report definitions, flow and paired bar values

A019 DOC006p4 eMethods: head-to-head explanatory capabilities of CTP rCBF<30%, manually delineated NCCT hypodensity, composite core and CT-ASPECTS; models contain age, presentation NIHSS, LKW-to-randomization and one imaging parameter. Information criteria for functional outcomes; AUC for mRS0-2/0-3. Lower criteria/higher AUC better. BIC differences0-2 weak,2-6 positive,6-10 strong,>10 very strong. Match eTable6/model comparison and main discussion.

A020 DOC006p5 eFigure1: mismatch ratio=Tmax>6s volume / rCBF<30% volume, difference=Tmax volume minus core. Example core94mL, hypoperfusion131mL, ratio1.4, mismatch37mL. Tmax colorbar2,4,6,8,10,12. Match main imaging definitions and plan A005.

A021 DOC006p6 eFigure2: manually delineated NCCT hypodensity; CTP core rCBF<30%=13mL, Tmax>6.0s39mL, mismatch26mL, ratio3.0. Overlay hypodensity≥5 and≤12HU; follow-up DWI tissue corresponding to hypodensity. A022p7 is continuation DWI without independent quantitative labels.

A023 DOC006p8 eFigure3: eligible958; excluded606; SELECT2 352; missing90-day4; available348; imaging exclusions12 (NCCT missing/unusable6, perfusion missing/uncorrectable5, follow-up missing1); cohort336; randomized EVT168/MM168; received EVT170 (randomized168 + crossover MM2), received MM166. Exclusion categories: clot location124; age99; LKW>24h61; mRS>1 59; hemorrhage/neoplasm/AV malformations51; consent45; dissection28; IVtPA>4.5h26; other trial22; ASPECTS≤2 19; mass effect/established infarct15; life expectancy<90days13; intracranial stent11; uncertain compliance9; other24. Match main cohort/population.

A024 DOC006p9 eFigure4 pairs are CT hypodensity larger %, CTP/MRI larger %: time bins0-3h19/81;3-6h44/56;6-9h59/41;9-12h68/33;12-15h76/24;15-18h76/24;18-21h76/24;21-24h86/14. Narrative19% within3h to86%21-24h. Bin denominators not displayed.

A025-A027 pairs below are no mismatch %, mismatch %, every printed bar. Time-bin order0-3,3-6,6-9,9-12,12-15,15-18,18-21,21-24hours. Core-bin order0-49,50-99,100-149,≥150mL.

| ID/panel | PDFpage | Core definition/profile | All paired rows in stated order | Trend P |
|---|---:|---|---|---|
| A025a | 10 | CTP/MRI ratio≥1.2 AND volume≥10mL | 4/96;10/90;13/87;10/90;7/93;4/96;4/96;14/86 | .71 |
| A025b | 10 | CTP/MRI ratio≥1.8 AND volume≥15mL | 62/38;42/58;47/53;32/68;30/70;26/74;4/96;29/71 | <.001 |
| A026c | 11 | composite ratio≥1.2 AND volume≥10mL | 8/92;18/82;27/73;24/76;26/74;22/78;20/80;29/71 | .27 |
| A026d | 11 | composite ratio≥1.8 AND volume≥15mL | 73/27;60/40;74/26;56/44;65/35;63/37;32/68;71/29 | .18 |
| A027a | 12 | CTP/MRI ratio≥1.2 AND volume≥10mL | 2/98;6/94;13/87;28/73 | <.001 |
| A027b | 12 | CTP/MRI ratio≥1.8 AND volume≥15mL | 4/96;29/71;68/32;83/18 | <.001 |

## CTP/MRI and ASPECTS forests: every printed row

A028=eFigure7 DOC006p13 mRS0-2; A029=eFigure8 p14 mRS0-3; A030=eFigure9 p15 mRS5-6. All outcomes90days. Each outcome cell gives EVT count(percent); MM count(percent); RR(95%CI). N in group is total, not arm denominator. Comparison EVT/MM. Benefit to right for0-2/0-3, left for5-6. Model mapping is plan modified Poisson robust standard errors adjusted prognostic variables, omitting the stratification variable. Asterisk is a displayed unestimated result; do not synthesize an estimate.

| Row/group(total N) | A028 mRS0-2 | A029 mRS0-3 | A030 mRS5-6 |
|---|---|---|---|
| ASPECTS0-2(19) | 0(0.00);0(0.00);1.00(.37-2.72) | 0(0.00);0(0.00);1.00(.37-2.72) | 9(81.82);8(100.00);.80(.60-1.07) |
| ASPECTS3-5(277) | 31(22.30);10(7.25);3.20(1.67-6.14) | 59(42.45);27(19.57);2.22(1.55-3.16) | 57(41.01);80(57.97);.70(.56-.88) |
| ASPECTS6-10(40) | 3(16.67);2(9.09);3.22(.84-12.35) | 6(33.33);4(18.18);2.61(1.00-6.84) | 10(55.56);14(63.64);.78(.46-1.33) |
| ASPECTS3(73) | 7(15.56);2(7.14);2.49(.60-10.23) | 12(26.67);5(17.86);1.75(.74-4.11) | 22(48.89);20(71.43);.71(.49-1.04) |
| ASPECTS4(88) | 7(22.58);3(5.26);3.52(1.06-11.62) | 15(48.39);8(14.04);3.18(1.61-6.28) | 12(38.71);35(61.40);.69(.45-1.07) |
| ASPECTS5(116) | 17(26.98);5(9.43);2.93(1.20-7.17) | 32(50.79);14(26.42);1.97(1.23-3.18) | 23(36.51);25(47.17);.67(.45-1.01) |
| core<70(156) | 23(28.05);9(12.16);2.36(1.20-4.61) | 44(53.66);23(31.08);1.79(1.26-2.54) | 27(32.93);32(43.24);.75(.52-1.08) |
| core≥70(180) | 11(12.79);3(3.19);4.19(1.27-13.89) | 21(24.42);8(8.51);3.10(1.49-6.43) | 49(56.98);70(74.47);.74(.61-.91) |
| core<100(236) | 30(25.64);11(9.24);2.81(1.53-5.17) | 56(47.86);28(23.53);2.10(1.49-2.95) | 44(37.61);64(53.78);.66(.51-.86) |
| core≥100(100) | 4(7.84);1(2.04);3.39(.52-22.13) | 9(17.65);3(6.12);3.16(.99-10.10) | 32(62.75);38(77.55);.82(.65-1.04) |
| core<150(296) | 33(22.45);12(8.05);3.03(1.68-5.47) | 62(42.18);31(20.81);2.17(1.56-3.02) | 63(42.86);86(57.72);.69(.56-.85) |
| core≥150(40) | 1(4.76);0(0.00);* | 3(14.29);0(0.00);* | 13(61.90);16(84.21);.81(.56-1.19) |
| profile1.2/10 No(29) | 0(0.00);1(4.76);* | 2(25.00);4(19.05);5.99(.76-47.33) | 3(37.50);14(66.67);.58(.26-1.31) |
| profile1.2/10 Yes(307) | 34(21.25);11(7.48);3.10(1.68-5.70) | 63(39.38);27(18.37);2.32(1.66-3.25) | 73(45.62);88(59.86);.75(.62-.91) |
| profile1.8/15 No(120) | 6(10.34);2(3.23);3.54(.72-17.41) | 14(24.14);6(9.68);2.77(1.17-6.53) | 30(51.72);44(70.97);.73(.55-.95) |
| profile1.8/15 Yes(216) | 28(25.45);10(9.43);2.84(1.50-5.38) | 51(46.36);25(23.58);2.08(1.48-2.93) | 46(41.82);58(54.72);.74(.58-.95) |

| Interaction group | A028 P | A029 P | A030 P |
|---|---:|---:|---:|
| ASPECTS0-2/3-5/6-10 | .9055 | .6788 | .8204 |
| ASPECTS3/4/5 | .9543 | .8927 | .7244 |
| core70 | .4097 | .2093 | .9344 |
| core100 | .7338 | .574 | .2291 |
| core150 | not displayed | not displayed | .2056 |
| mismatch1.2/10 | not displayed | .4588 | .6255 |
| mismatch1.8/15 | .8079 | .5921 | .9485 |

Main-paper matching keys: ASPECTS/core strata treatment effect; binary functional outcomes; mismatch-profile treatment heterogeneity. Forest interaction tests are subgroup tests, not row-effect P values. Main article matcher must retain analysis-set/model agreement rather than substitute crude count ratios.

## NCCT and composite-core forests: every printed row

Exact bounded forest scope A028-A034: DOC006 physical pages13-19; eFigures7-13;112rows. This table adds64rows to48rows above. A031=eFigure10 p16 mRS distribution: EVT median[IQR];MM median[IQR];GenOR(95%CI). A032=eFigure11 p17 mRS0-2, A033=eFigure12 p18 mRS0-3, A034=eFigure13 p19 mRS5-6: EVT count(percent);MM count(percent);RR(95%CI). Largest=composite=max(CTP/MRI,CT hypodensity); NCCT=CT hypodensity. Profiles based on largest core;0=no,1=yes. EVT compared with MM at90days. Printed eFigure13 axis annotations put favors MM on left and favors EVT on right; record as printed, separate from eFigure9 labels. No individual effect P values printed. All percentages are within arm and stratum.

| Row/group(total N) | A031 mRS distribution | A032 mRS0-2 | A033 mRS0-3 | A034 mRS5-6 |
|---|---|---|---|---|
| NCCT<70(132) | 4[3-6];5[4-6];2.00(1.36-2.93) | 17(25.00);4(6.25);3.84(1.43-10.33) | 34(50.00);13(20.31);2.38(1.50-3.79) | 27(39.71);39(60.94);.68(.49-.95) |
| NCCT≥70(204) | 4[3-6];5[4-6];1.53(1.15-2.04) | 17(17.00);8(7.69);2.40(1.13-5.09) | 31(31.00);18(17.31);1.97(1.24-3.13) | 49(49.00);63(60.58);.77(.62-.97) |
| largest<70(80) | 3[2-6];4[3-6];1.88(1.11-3.16) | 14(33.33);4(10.53);3.04(1.16-7.97) | 26(61.90);12(31.58);1.85(1.19-2.90) | 14(33.33);17(44.74);.82(.49-1.37) |
| largest≥70(256) | 4[3-6];5[4-6];1.69(1.31-2.18) | 20(15.87);8(6.15);2.92(1.38-6.18) | 39(30.95);19(14.62);2.34(1.50-3.67) | 62(49.21);85(65.38);.72(.60-.88) |
| NCCT<100(207) | 3[2-6];5[4-6];2.25(1.65-3.06) | 29(28.16);8(7.69);3.72(1.85-7.45) | 52(50.49);20(19.23);2.67(1.84-3.89) | 37(35.92);60(57.69);.61(.46-.81) |
| NCCT≥100(129) | 6[4-6];6[4-6];1.25(.89-1.74) | 5(7.69);4(6.25);1.44(.39-5.25) | 13(20.00);11(17.19);1.34(.66-2.71) | 39(60.00);42(65.62);.87(.69-1.10) |
| largest<100(165) | 3[2-5];5[4-6];2.33(1.62-3.34) | 26(32.50);7(8.24);3.80(1.83-7.88) | 46(57.50);18(21.18);2.65(1.77-3.97) | 26(32.50);44(51.76);.62(.44-.86) |
| largest≥100(171) | 5[4-6];6[4-6];1.46(1.09-1.96) | 8(9.09);5(6.02);2.08(.70-6.18) | 19(21.59);13(15.66);1.64(.89-3.03) | 50(56.82);58(69.88);.78(.64-.96) |
| NCCT<150(297) | 4[3-6];5[4-6];1.70(1.33-2.19) | 33(21.85);11(7.53);3.22(1.75-5.91) | 62(41.06);29(19.86);2.24(1.60-3.13) | 69(45.70);85(58.22);.76(.62-.93) |
| NCCT≥150(39) | 4[4-6];6[5-6];2.21(1.16-4.19) | 1(5.88);1(4.55);.12(.01-1.05) | 3(17.65);2(9.09);3.70(.90-15.24) | 7(41.18);17(77.27);.55(.33-.94) |
| largest<150(273) | 4[3-6];5[4-6];1.80(1.39-2.35) | 32(23.70);11(7.97);3.29(1.79-6.06) | 59(43.70);29(21.01);2.25(1.61-3.15) | 59(43.70);78(56.52);.72(.58-.90) |
| largest≥150(63) | 5[4-6];6[5-6];1.82(1.13-2.94) | 2(6.06);1(3.33);1.58(.16-15.47) | 6(18.18);2(6.67);3.50(1.12-10.92) | 17(51.52);24(80.00);.69(.48-.97) |
| profile1.2/10 0(74) | 4[3-6];5[4-6];1.74(1.03-2.95) | 5(14.71);3(7.50);1.62(.47-5.62) | 13(38.24);7(17.50);2.11(.96-4.64) | 12(35.29);23(57.50);.67(.41-1.10) |
| profile1.2/10 1(262) | 4[3-6];5[4-6];1.81(1.39-2.35) | 29(21.64);9(7.03);3.36(1.72-6.56) | 52(38.81);24(18.75);2.26(1.59-3.21) | 64(47.76);79(61.72);.74(.61-.90) |
| profile1.8/15 0(211) | 4[3-6];5[4-6];1.64(1.23-2.18) | 21(18.92);8(8.00);2.53(1.26-5.10) | 39(35.14);18(18.00);1.99(1.28-3.10) | 50(45.05);61(61.00);.76(.60-.95) |
| profile1.8/15 1(125) | 4[3-6];5[4-6];1.94(1.30-2.88) | 13(22.81);4(5.88);3.84(1.39-10.58) | 26(45.61);13(19.12);2.46(1.53-3.93) | 26(45.61);41(60.29);.71(.53-.97) |

| Interaction group | A031 P | A032 P | A033 P | A034 P |
|---|---:|---:|---:|---:|
| NCCT70 | .2684 | .4696 | .5583 | .4646 |
| largest70 | .9413 | .9978 | .4539 | .7845 |
| NCCT100 | .0164 | .1717 | .0762 | .0664 |
| largest100 | .0707 | .2581 | .1516 | .2512 |
| NCCT150 | .8886 | .336 | .6936 | .3272 |
| largest150 | .7243 | .5126 | .9146 | .9984 |
| largest mismatch1.2/10 | .6791 | .3817 | .7419 | .7851 |
| largest mismatch1.8/15 | .6165 | .5351 | .5951 | .7981 |

## Remaining bounded statistical figure/plan scope

Separable from forests: DOC005pp1-7 A001-A018; DOC006pp1-12 A019-A027; DOC006pp20-32 A035-A041. A024-A027 contain48 paired numeric rows (8 modality/time,32 mismatch/time,8 mismatch/core). A035-A040 contain22 graph panels, no tabulated numerical fitted coordinates. Do not treat approximate visual coordinates as printed estimates.

A035 DOC006p20 eFigure14: decreasing CT ASPECTS, adjusted composite core. A/B/C probability of mRS0-2/0-3/5-6 with95%CI shading; D generalized odds of≥1point better mRS with95%CI, dashed null1. EVT cyan/MM salmon; D black. X ticks10,7.5,5,2.5,0; A probability ticks0,.2,.4,.6;B0,.2,.4,.6,.8;C.25,.50,.75,1.00;D1,2,3. As ASPECTS decreases, A EVT slightly rises/MM falls;B both fall;C both rise;D rises. Caption ASPECTS6-10 requires large CTP core for eligibility. Match main ASPECTS curve and A014-A015.

A036 DOC006p21 eFigure15 hypodensity volume: same A/B/C/D outcomes/95%CI/arms. X core-volume mL ticks0,100,200,300 all panels. A ticks0,.2,.4,.6;B0,.25,.50,.75;C.25,.50,.75,1.00;D1,2,3,4/null1. A/B decline;C rises;D declines, plotted curve goes below1 near high volumes. Printed coordinates are axis labels, no numeric fitted-point labels. Match NCCT forest/model comparison and post hoc A018.

A037 DOC006p22 eFigure16 composite volume: same A/B/C/D outcomes and95%CI. X0,100,200,300mL; A/B y0,.25,.50,.75;C.25,.50,.75,1.00;D1,2,3,4,5/null1. A/B fall,C rises,D decreases toward1. Match composite main outcomes/primary volume A004.

A038 DOC006p23 eFigure17 mismatch volume: same outcomes/arms/CI. A/B/C x-100,0,100,200,300,400mL;D x0,100,200 with axis extending into negative/above200 values. A y0,.2,.4,.6;B0,.25,.50,.75;C.25,.50,.75,1.00;D1.0,1.5,2.0,2.5/null1. A/B fall with mismatch volume,C rises,D slight decrease. Numeric negative axis values are plotted mismatch volume, not newly inferred counts. Match continuous mismatch A016.

A039 DOC006p24 eFigure18: EVT patients probability independent ambulation mRS0-3 across age and time CTP-to-reperfusion/end procedure; three core panels70,100,150mL, caption says CTP/MRI core while explanatory prose refers composite. Age ticks30,40,50,60,70,80 (range toapproximately85);time100,200,300 (no unit printed on axis). Legend intervals(0.0,0.1],(0.1,0.2],(0.2,0.3],(0.3,0.4],(0.4,0.5],(0.5,0.6],(0.6,0.7],(0.7,0.8],(0.8,0.9]. Probabilities decrease as age, time and volume increase;150mL independence very unlikely except young/rapid treatment. No point probability estimates or CIs printed. Match main age/time contour analyses; plan A011 time definition.

A040 DOC006p25 eFigure19: EVT patients independent ambulation probability, composite volume70,100,150mL; age same30-80 ticks;time LKW-to-reperfusion/end procedure ticks0,500,1000,1500 (unit not printed on axis). Same nine probability intervals. Probability declines with age/time/volume. No fitted numeric point labels/CI. Match main age/time contour analyses/A011.

## A041 eFigure20 complete assigned distribution bars

DOC006physicalpp26-32 eFigure20a-aa;27strata/54arm bars. Values are printed integer percentages in mRS0,1,2,3,4,5,6 order. A zero is explicit or represented by zero-width category; merged overlapping zero labels preserved by category order; zero-width categories are identified from color legend. Total percent may differ from100 due printed rounding. Every row gives both arm denominators. These displays retain separate5and6 categories; plan distribution modeling merges5/6. Matching main keys are core/ASPECTS/mismatch/concordance distributions and binary counts in forests. X axes0-100%, generally10point ticks (panelg20point ticks). Legends mRS0-6. EVT versus MM.

| Row | PDFpage | Stratum | EVT N / percentages0-6 | MM N / percentages0-6 |
|---|---:|---|---|---|
| a | 26 | NCCT<70 | 68 /3,6,16,25,10,9,31 | 64 /0,2,5,14,19,22,39 |
| b | 26 | NCCT≥70 | 100 /0,4,13,14,20,8,41 | 104 /0,2,6,10,22,17,43 |
| c | 26 | NCCT<100 | 103 /2,8,18,22,14,9,27 | 104 /0,3,5,12,23,21,37 |
| d | 26 | NCCT≥100 | 65 /0,0,8,12,20,8,52 | 64 /0,0,6,11,17,16,50 |
| e | 27 | NCCT<150 | 151 /1,5,15,19,13,9,37 | 146 /0,2,5,12,22,18,40 |
| f | 27 | NCCT≥150 | 17 /0,0,6,12,41,6,35 | 22 /0,0,5,5,14,23,55 |
| g | 27 | CTP/MRI<70 | 82 /2,9,17,26,13,6,27 | 74 /0,3,9,19,26,16,27 |
| h | 27 | CTP/MRI≥70 | 86 /0,1,12,12,19,10,47 | 94 /0,1,2,5,17,21,53 |
| i | 28 | CTP/MRI<150 | 147 /1,5,16,20,15,8,35 | 149 /0,2,6,13,21,19,38 |
| j | 28 | CTP/MRI≥150 | 21 /0,0,5,10,24,10,52 | 19 /0,0,0,0,16,16,68 |
| k | 28 | composite<70 | 42 /5,10,19,29,5,5,29 | 38 /0,3,8,21,24,18,26 |
| l | 28 | composite≥70 | 126 /0,3,13,15,20,10,40 | 130 /0,2,5,8,20,19,46 |
| m | 29 | composite<100 | 80 /3,9,21,25,10,9,24 | 85 /0,2,6,13,27,20,32 |
| n | 29 | composite≥100 | 88 /0,1,8,13,22,8,49 | 83 /0,1,5,10,14,18,52 |
| o | 29 | composite<150 | 135 /1,6,16,20,13,9,35 | 138 /0,2,6,13,22,19,38 |
| p | 29 | composite≥150 | 33 /0,0,6,12,30,6,45 | 30 /0,0,3,3,13,20,60 |
| q | 30 | ASPECTS0-2 | 11 /0,0,0,0,18,27,55 | 8 /0,0,0,0,0,38,63 |
| r | 30 | ASPECTS3-5 | 139 /1,6,15,20,17,6,35 | 138 /0,1,6,12,22,20,38 |
| s | 30 | ASPECTS6-10 | 18 /0,0,17,17,11,17,39 | 22 /0,5,5,9,18,9,55 |
| t | 30 | ASPECTS3 | 45 /0,4,11,11,24,9,40 | 28 /0,4,4,11,11,18,54 |
| u | 31 | ASPECTS4 | 31 /3,3,16,26,13,6,32 | 57 /0,2,4,9,25,21,40 |
| v | 31 | ASPECTS5 | 63 /2,8,17,24,13,3,33 | 53 /0,0,9,17,26,19,28 |
| w | 31 | ASPECTS<6 & CTP/MRI<70 | 76 /3,9,16,26,13,7,26 | 63 /0,2,10,19,25,17,27 |
| x | 32 | ASPECTS≥6 & CTP/MRI≥70 | 12 /0,0,8,17,8,25,42 | 11 /0,0,0,0,9,9,82 |
| y | 32 | ASPECTS<6 & CTP/MRI≥70 | 74 /0,1,12,11,20,8,47 | 83 /0,1,2,6,18,23,49 |
| z | 32 | no CTP/MRI mismatch1.2/10 | 8 /0,0,0,25,38,0,38 | 21 /0,0,5,14,14,24,43 |
| aa | 32 | CTP/MRI mismatch1.2/10 | 160 /1,5,15,18,15,9,37 | 147 /0,2,5,11,22,18,42 |

A041ends at panelaa on physicalpage32. Further panels are assigned to resultsB; not inferred here. eTables start beyond assigned scope. No scientific gap in this39page shard. Limits: native numeric text is sparse for forests; values above visually transcribed from matched images. Graphs provide curves/CI shading without printed fitted coordinates, so exact graph coordinates cannot be reconstructed as printed point estimates; full axes, direction, reference and outcomes are mapped. Contour time-axis units are not printed; do not silently assign units.

## Relationship accounting

41 local parent mapping IDs A001-A041;112 forest-row relationships (A028-A034 each16);27 distribution-stratum relationships containing54arm bars;48 paired-bar relationships(A0248,A02516,A02616,A0278);18 prospective plan relationships;5 report-definition/flow relationships(A019-A023);6 prediction-figure relationships(A035-A040,22panels). Total216 atomic relationships when each plan parent, report-definition parent, paired-bin row, forest row, distribution stratum, and prediction figure is counted once:18+5+48+112+27+6=216; arm bars and prediction panels are component values, not additional relationship rows.

## Exact physical source-page index

These relative links are anchored for this support_parts artifact; merged extraction must reduce one ../.

| Source | Physical page | Source evidence |
|---|---:|---|
| DOC005 | 1 | [SAP p1](../../../joi240006supp4_prod_1708623115.00733.pdf#page=1) |
| DOC005 | 2 | [SAP p2](../../../joi240006supp4_prod_1708623115.00733.pdf#page=2) |
| DOC005 | 3 | [SAP p3](../../../joi240006supp4_prod_1708623115.00733.pdf#page=3) |
| DOC005 | 4 | [SAP p4](../../../joi240006supp4_prod_1708623115.00733.pdf#page=4) |
| DOC005 | 5 | [SAP p5](../../../joi240006supp4_prod_1708623115.00733.pdf#page=5) |
| DOC005 | 6 | [SAP p6](../../../joi240006supp4_prod_1708623115.00733.pdf#page=6) |
| DOC005 | 7 | [SAP p7](../../../joi240006supp4_prod_1708623115.00733.pdf#page=7) |
| DOC006 | 1 | [Results p1](../../../joi240006supp5_prod_1708623115.01733.pdf#page=1) |
| DOC006 | 2 | [Results p2](../../../joi240006supp5_prod_1708623115.01733.pdf#page=2) |
| DOC006 | 3 | [Results p3](../../../joi240006supp5_prod_1708623115.01733.pdf#page=3) |
| DOC006 | 4 | [Results p4](../../../joi240006supp5_prod_1708623115.01733.pdf#page=4) |
| DOC006 | 5 | [Results p5](../../../joi240006supp5_prod_1708623115.01733.pdf#page=5) |
| DOC006 | 6 | [Results p6](../../../joi240006supp5_prod_1708623115.01733.pdf#page=6) |
| DOC006 | 7 | [Results p7](../../../joi240006supp5_prod_1708623115.01733.pdf#page=7) |
| DOC006 | 8 | [Results p8](../../../joi240006supp5_prod_1708623115.01733.pdf#page=8) |
| DOC006 | 9 | [Results p9](../../../joi240006supp5_prod_1708623115.01733.pdf#page=9) |
| DOC006 | 10 | [Results p10](../../../joi240006supp5_prod_1708623115.01733.pdf#page=10) |
| DOC006 | 11 | [Results p11](../../../joi240006supp5_prod_1708623115.01733.pdf#page=11) |
| DOC006 | 12 | [Results p12](../../../joi240006supp5_prod_1708623115.01733.pdf#page=12) |
| DOC006 | 13 | [Results p13](../../../joi240006supp5_prod_1708623115.01733.pdf#page=13) |
| DOC006 | 14 | [Results p14](../../../joi240006supp5_prod_1708623115.01733.pdf#page=14) |
| DOC006 | 15 | [Results p15](../../../joi240006supp5_prod_1708623115.01733.pdf#page=15) |
| DOC006 | 16 | [Results p16](../../../joi240006supp5_prod_1708623115.01733.pdf#page=16) |
| DOC006 | 17 | [Results p17](../../../joi240006supp5_prod_1708623115.01733.pdf#page=17) |
| DOC006 | 18 | [Results p18](../../../joi240006supp5_prod_1708623115.01733.pdf#page=18) |
| DOC006 | 19 | [Results p19](../../../joi240006supp5_prod_1708623115.01733.pdf#page=19) |
| DOC006 | 20 | [Results p20](../../../joi240006supp5_prod_1708623115.01733.pdf#page=20) |
| DOC006 | 21 | [Results p21](../../../joi240006supp5_prod_1708623115.01733.pdf#page=21) |
| DOC006 | 22 | [Results p22](../../../joi240006supp5_prod_1708623115.01733.pdf#page=22) |
| DOC006 | 23 | [Results p23](../../../joi240006supp5_prod_1708623115.01733.pdf#page=23) |
| DOC006 | 24 | [Results p24](../../../joi240006supp5_prod_1708623115.01733.pdf#page=24) |
| DOC006 | 25 | [Results p25](../../../joi240006supp5_prod_1708623115.01733.pdf#page=25) |
| DOC006 | 26 | [Results p26](../../../joi240006supp5_prod_1708623115.01733.pdf#page=26) |
| DOC006 | 27 | [Results p27](../../../joi240006supp5_prod_1708623115.01733.pdf#page=27) |
| DOC006 | 28 | [Results p28](../../../joi240006supp5_prod_1708623115.01733.pdf#page=28) |
| DOC006 | 29 | [Results p29](../../../joi240006supp5_prod_1708623115.01733.pdf#page=29) |
| DOC006 | 30 | [Results p30](../../../joi240006supp5_prod_1708623115.01733.pdf#page=30) |
| DOC006 | 31 | [Results p31](../../../joi240006supp5_prod_1708623115.01733.pdf#page=31) |
| DOC006 | 32 | [Results p32](../../../joi240006supp5_prod_1708623115.01733.pdf#page=32) |
# Support quantitative map: results B and administrative sources

Scope: DOC-006 PDF pp. 33-53 (21 pages), DOC-002 PDF pp. 1-30 (30 pages), DOC-007 PDF p. 1 (1 page). Total 52 physical pages, all mapped. All three documents are REPORT by content; none contains a prospective statistical plan. All pages are reusable-backed; fresh-required extraction units: 0. The requested 51-page count was arithmetic shorthand; the exact assignment contains 52 pages.

Only source-linked extraction assets were used. No prior scientific conclusions, candidate sets, screening, checker, classification, adjudication, or final reports were read. No candidate diagnosis is made here. Local B identifiers identify complete display groups, each including every displayed row and cell; they are not finding IDs. The full page transcriptions below preserve all numeric inputs, labels, units, confidence intervals, P values and footnotes. Interpret each cell under its row and column heading, not by proximity in a wrapped native text line.

## Provenance

Read QUALITY_CONTROL_SCOPE.md completely, workflow_1_6_2/review_contract.md completely, source_inventory.md, source_coverage.md, evidence_asset_inventory.md, tooling_record.md, and coverage_manifest.md. Reused DOC-006 native_text/page-033.txt through page-053.txt and corresponding page_images/page-033.png through page-053.png, all under .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/. Visually inspected each of the 21 complete rendered pages. Legacy text/render engines have unrecorded versions; the curator records source identity and hashes. Reused DOC-002 and DOC-007 by_page.txt/layout.txt under .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/. Their direct-layout identity is recorded in inventory.

New durable derivative: this map only. Engine: agent reading/reconstruction plus Bash cat, sed and printf for literal transcription insertion. Commands: cat exact reused native text; view_image exact reused page PNG; sed page-marker-bounded reads of DOC-002 by_page.txt; pdfimages -f 28 -l 28 -list joi240006supp1_prod_1708623114.97236.pdf (Poppler26.01.0, transient output, no raster image on p.28). No new OCR, rendering, or Python extraction was required. Compute device CPU. Sources and reused assets preserved.

## Page coverage and relationship index

| Local ID | DOC-006 physical page | Complete applicable content | Main-paper matching key |
|---|---:|---|---|
| B001 | 33-34 | eFigure20 panels ab-ag: seven-level mRS treatment distributions, mismatch presence by core definition and threshold | 90-day ordinal mRS; randomized treatment; mismatch definition; CTP/MRI vs composite core |
| B002 | 35 | eTable1 first page: all demographic, history, examination and occlusion rows | Baseline as-treated EVT170/MM166; separate from ITT168/168 |
| B003 | 36 | eTable1 continuation: every volume, time and treatment-characteristic cell; NIHSS, ASPECTS and core footnotes | Baseline units; imaging definition; treatment received |
| B004 | 37 | eTable1 continuation footnotes: manual CT delineation3readers; composite maximum definition | CT hypodensity; composite core=max(CTP/MRI core, CT hypodensity) |
| B005 | 38 | eTable2: all ITT clinical/imaging outcome counts, denominators, percentages, medians and IQRs | ITT168/168; 90-day mRS0-2,0-3,5-6; mortality; safety; infarct growth |
| B006 | 39 | eTable3: 5 ASPECTS rows ×4 outcomes, all20estimates and95%CIs | Site-investigator ASPECTS sensitivity; mRS shift/aGenOR and binary/aRR |
| B007 | 40 | eTable4: 6CTP strata×4outcomes, all22estimates/CIs and2N/A cells | CT perfusion only; rCBF<30%; core thresholds70/100/150ml |
| B008 | 41 | eTable5:4outcomes×2volume definitions×2treatment groups, all16estimates/CIs and8interaction Ps, outcome totals | As-treated170/166; ischemic volume per10ml; within-arm prognostic association |
| B009 | 42 | eTable6:3outcomes×4modalities; all12AIC/BIC rows and8AUC/CIs; preferred labels; model footnotes | Model comparison: ordinal logistic mRS; binary discrimination; AIC/BIC/AUC |
| B010 | 43-44 | eTable7: both composite mismatch thresholds, within-arm ordinal and binary results, all counts/RR/RD/CIs and8last-column Ps | As-treated mismatch vs no mismatch(reference); adjustment age/NIHSS/LKW-to-randomization/CTP-MRIcore |
| B011 | 45-46 | eTable8: imaging concordance/discordance within each treatment; all medians/counts/RR/RD/CIs and interaction Ps | Concordant ASPECTS<6/core≥70ml; discordant1 ASPECTS<6/core<70ml; discordant2 ASPECTS6-10/core≥70ml |
| B012 | 47-48 | eTable9: CTP/MRI profile-stratified EVT treatment effects; all medians/counts/aGenOR/aRR/CIs and interactions | Between-arm EVT vs MM within imaging profiles; distinguish from within-arm eTable8 |
| B013 | 49-50 | eTable10: composite profile-stratified EVT treatment effects; all medians/counts/aGenOR/aRR/CIs and interactions | Between-arm EVT vs MM; composite core; concordant/discordant profiles |
| B014 | 51 | eTable11: MRDWI follow-up growth, all3group Ns and9median/IQR cells | Follow-up modality MRDWI; MM101; mTICI0-2a24; mTICI2b-379 |
| B015 | 52 | eTable12: all4growth comparisons with4group Ns,8median/IQR cells and4Ps | Functional independence46/dependence290; independent ambulation96/noambulation240; total336 |
| B016 | 53 | eTable13: all3patient rows×5clinical values; ≥10mloverestimation threshold; N/A footnote | Ischemic core minus follow-up infarct; acquisition/reperfusion windows;3patients |

Every DOC-006 page above is COMPLETE, including footnote-only p.37 and table continuations pp.44,46,48,50. No page is omitted for sparse text. Table6 has12model rows: ordinal mRS AUC not applicable, binary outcomes8AUC/CIs. Table7's columns do not print treatment headings or a last-column heading on these pages; left/right treatment mapping follows surrounding as-treated convention and title. Preserve this limitation rather than inventing a printed label. Each ordinal ratio and binary RR/RD is adjusted as indicated; interaction P values test between-treatment interaction and are not automatically individual-arm estimate tests. Table9/10 columns explicitly run MM then EVT, while Table1/2/5/8 run EVT then MM.

## Explicit eFigure20 panel transcription (B001)

Each row is a seven-element percentage vector in legend order mRS0,1,2,3,4,5,6. Axis0%-100% in10%increments. Values below are visually read, including crowded zeros and single digits. No counts are inferred from rounded percentages. The next-page first panel continues ae heading on p.33.

| Physical page | Panel/core/threshold/presence | EVT N; mRS0-6 percentages | MM N; mRS0-6 percentages |
|---:|---|---|---|
|33|ab composite, ratio≥1.2 AND volume≥10ml absent|34;0,3,12,24,26,3,32|40;0,0,8,10,25,20,38|
|33|ac composite, ratio≥1.2 AND volume≥10ml present|134;1,5,15,17,13,10,38|128;0,2,5,12,20,19,43|
|33|ad CTP/MRI, ratio≥1.8 AND volume≥15ml absent|58;0,3,7,14,24,10,41|62;0,2,2,6,19,21,50|
|34|ae CTP/MRI, ratio≥1.8 AND volume≥15ml present|110;2,5,18,21,12,7,35|106;0,2,8,14,22,18,37|
|34|af composite, ratio≥1.8 AND volume≥15ml absent|111;1,5,13,16,20,7,38|100;0,2,6,10,21,20,41|
|34|ag composite, ratio≥1.8 AND volume≥15ml present|57;2,4,18,23,9,11,35|68;0,1,4,13,21,18,43|

## Statistical and numeric comparison structure

Each table below is a complete display group, with named key outcome/contrast/population. For statistical inventory, independently track every estimate-CI combination, each interaction test and each model-selection comparison. Reference cells and N/A cells are retained as source definitions. For numeric inventory, track every numerator/denominator/percentage triple and row/column partition without replacing printed adjusted measures with crude ratios.

B002/B003 baseline categorical counts partition sex, race, referral and occlusion groups against as-treated170/166 headers. Other rows may have variable-specific denominators; the printed cells remain authoritative and denominators absent from cells are not invented. Table1 printed CTP/MRI footnote uses rCBF<30%, ADC<620×10^-6 mm/s²; units transcribed as printed, including superscripts visible on p.36. ASPECTS10points, lower=worse injury; NIHSS42points, higher=more deficits. B004 CT delineation3readers and composite larger-of-two definition affect core measures.

B005 ITT168/168 differs by population definition from B008170/166. Binary outcomes use 90-day mRS0-2/0-3/5-6, all-cause mortality, symptomatic hemorrhage, parenchymal hemorrhage, neurological worsening and early neurological improvement. Early improvement denominators165/166 are printed explicitly. Growth measures in ml distinguish CTP/MRI, composite and CT baseline measures; each median/IQR stands separately, so do not subtract summary medians to recreate growth.

B006 site ASPECTS3-5/6-10 and individual3/4/5 strata cross four outcomes. B007 CT-perfusion-only sensitivity uses nested <70/≥70,<100/≥100,<150/≥150 groups, so totals across all six rows are not a partition. N/A means could not be evaluated.

B008 within-treatment prognostic volume effects use per10ml increments, separately for CT hypodensity/composite. mRS distribution medians4(3-6)/5(4-6); binary outcome counts34/170 vs12/166,66/170 vs30/166,77/170 vs101/166. Interaction tests belong to paired slopes across treatment groups, not effect-CI null checks within one arm.

B009 lower AIC/BIC means more parsimonious; higher AUC means better predictive value. Composite marked preferred for all three outcomes. Ordinal mRS parameters explicitly use ordinal logistic regression; AUC is NA for those4rows.

B010 mismatch presence reference=no mismatch. Composite thresholds1.2/10ml and1.8/15ml are separate analyses. First criterion groups34/136EVT and40/126MM; second112/58EVT and99/67MM. Ordinal and binary effects are adjusted for age, NIHSS, time from last known well to randomization, CTP/MRI core volume. All aRD signs and intervals are retained literally, including -0.000 and positive0.168(0.011,0.325).

B011 concordant and two discordant profiles reference concordant; analysis headers EVT163/MM156. Table8 within-arm effects differ in estimand from Table9's treatment-effect rows. Each3profile count set must be examined within its own display. Table9 explicitly prints MM1/11(9.1%) vsEVT0/12(0%) for discordant2 mRS0-2 and MM3/11(27.3%) vsEVT0/12(0%) for mRS0-3; preserve these cells as printed. Table8 prints EVT1/12(8%) vsMM0/11(0%) and EVT3/12(25%) vsMM0/11(0%) for those respective rows. No adjudication is made here.

B012/B013 effects use aGenOR for ordinal distribution, aRR for binary thresholds; printed last column is interaction P, reference concordant. N/A could not be evaluated. Core modalities differ between Table9 and10; do not equate denominators across them. Both report exact profile-specific counts and outcome medians.

B014 MRI-follow-up restriction gives101+24+79=204contributors, not the full336. B015 outcome group totals290+46=336 and240+96=336; P<0.001 printed for each of4comparisons. Test identity is not supplied in these table pages and should be matched to eMethods by its assigned mapper. B016 IDs1-3 are patient identifiers, not counts for subgroup analysis. Printed threshold≥10ml applies to ischemic-core overestimation relative to follow-up volume. N/A denotes patient with medical management.

## Complete native table-cell transcriptions, visually checked

The following physical-page records preserve every row and cell. They complement the structured index and figure transcription. Page footer numbers are printed page numbers one less than PDF physical page; evidence links use the physical PDF page. All links below are package-root-relative source paths; the coordinator resolves them relative to final-report location.

### DOC-006 physical page 35

Source: joi240006supp5_prod_1708623115.01733.pdf#page=35

```text
eTables
eTable 1. Baseline clinical and imaging characteristics of study population (as-treated),
stratified based on treatment.

                                                 Endovascular           Medical care only
                                                 thrombectomy
                                                 N=170                  N=166
 Demographics
 Age (years)                                     66.0 (59.0-75.0)       67.0 (58.0-75.0)
 Sex                    Female                   68 (40.0%)             71 (42.8%)
                        Male                     102 (60.0%)            95 (57.2%)
 Race                   Asian                    5 (2.9%)               3 (1.8%)
                        Black                    24 (14.1%)             24 (14.5%)
                        Caucasian                126 (74.1%)            123 (74.1%)
                        Native Hawaiian or       2 (1.2%)               0
                        Pacific Islander
                        Other or unknown         13 (7.6%)              16 (9.6%)
 Transferred         to Directly Presenting to   71 (41.8%)             65 (39.2%)
 thrombectomy-          thrombectomy-capable
 Capable Center         Center
                        Transferred         to   99 (58.2%)             101 (60.8%)
                        thrombectomy-
                        Capable Center
 Medical History
 H/o Hypertension                                132 (77.6%)            120 (72.3%)
 H/o Diabetes Mellitus                           50 (29.4%)             54 (32.5%)
 H/o Atrial Fibrillation                         44 (25.9%)             38 (22.9%)
 H/o Coronary Artery                             39 (23.2%)             25 (15.6%)
 Disease
 H/o Congestive Heart                            20 (11.8%)             18 (10.8%)
 Failure
 H/o Ischemic Stroke                             18 (10.6%)             13 (7.8%)
 H/o          Transient                          4 (2.4%)               8 (4.8%)
 Ischemic Attack
 Physical Examination
 Hemisphere affected                             78 (45.9%)             69 (41.6%)
 NIH Stroke Scale at                             19 (15-23)             19 (15-22)
 thrombectomy
 hospital
 Neuroimaging findings
 Occlusion location      ICA                     75 (44.1%)             64 (38.6%)
                         MCA M1                  88 (51.8%)             94 (56.6%)
                         MCA M2                  7 (4.1%)               8 (4.8%)
 Tandem occlusions                               54 (31.8%)             43 (25.9%)


                                           34

```

### DOC-006 physical page 36

Source: joi240006supp5_prod_1708623115.01733.pdf#page=36

```text
                                                     Endovascular              Medical care only
                                                     thrombectomy
 CT ASPECTS at                                       4 (3-5)                 4 (4-5)
 thrombectomy
 hospital
 Composite          core                            103 (69-140)             100 (74-136)
 volume (ml)
 CTP/MRI core volume                                70 (39-110)              77 (48-104)
 (ml)
 CT         Hypodensity                             84 (45-114)              87 (49-113)
 volume (ml)
 Critically                                         161 (117-206)            166 (119-212)
 hypoperfused
 (Tmax>6s)       volume
 (ml)
 Time metrics
 Time      from     Last                            550 (311-920)            588 (345-928)
 Known        Well     to
 Randomization
 (minutes)
 Time from Arrival to                               16 (9-27)                16 (7-24)
 CT          Acquisition
 (minutes)
 Time from Arrival to                               26 (17-42)               25 (13-36)
 CTP         Acquisition
 (minutes)
 Additional characteristics
 IV       Thrombolytics                             33 (19.4%)               28 (17.0%)
 Administered
 Tenecteplase used                                  4 (12.5%)                1 (3.7%)
 General      Anesthesia                            100 (59.5%)
 Used
Footnotes:
CT – computed tomography
MRI – Magnetic Resonance Imaging
NIH Stroke Scale – a 42 point scoring system measuring neurological deficits, with higher score
representing more neurological deficits.
Tmax – Time to maximum intensity
CT Alberta Stroke Program Early CT Score (ASPECTS) – a 10 point ordinal scoring system
measuring areas of hypoattenuation due to ischemic changes in the middle cerebral artery territory
on non-contrast CT of brain, with a point deducted for each location demonstrating
hypoattenuation. Thus, lower scores represent worse the ischemic injury.
CTP/MRI core volume – volumetric estimates obtained from CT perfusion using relative Cerebral
Blood Flow <30% threshold/MR perfusion imaging using apparent diffusion coefficient <620
X10-6 mm/s2 threshold using automated RAPIDAi processing.


                                               35

```

### DOC-006 physical page 37

Source: joi240006supp5_prod_1708623115.01733.pdf#page=37

```text
CT hypodensity volume – volumetric estimates of observed hypodensity on non-contrast CT by
manual delineation of the region of interest by consensus from 3 expert readers using ITK-SNAP
Composite core volume – the larger of CTP/MRI core volume and CT hypodensity volume
estimates.




                                             36

```

### DOC-006 physical page 38

Source: joi240006supp5_prod_1708623115.01733.pdf#page=38

```text
eTable 2. Clinical and imaging outcomes in intention-to-treat population, stratified by
treatment.



                            Endovascular                    Medical Care Only
                            Thrombectomy             Plus
                            Medical Care
                            N=168                           N=168
 Distribution of Modified 4 (3-6)                           5 (4-6)
 Rankin Scale Scores at 90d
 Follow-up

 Functional    independence    34/168 (20.2%)               12/168 (7.1%)
 (mRS 0-2) at 90-day follow-
 up
 Independent     Ambulation    65/168 (38.7%)               31/168 (18.5%)
 (mRS 0-3) at 90-day follow-
 up
 Complete dependence or        76/168 (45.2%)               102/168 (60.7%)
 death (mRS 5-6) at 90d
 follow-up
 All-cause Mortality within    62/168 (36.9%)               70/168 (41.7%)
 90-day Follow-up Period

 Symptomatic Intracerebral 0/168 (0.0%)                     2/168 (1.2%)
 hemorrhage

 Parenchymal hemorrhage        4/168 (2.4%)                 3/168 (1.8%)

 Neurological Worsening        38/168 (22.6%)               27/168 (16.1%)

 Early          Neurological   19/165 (11.5%)               13/166 (7.8%)
 Improvement
 Follow-up infarct volume      170 (123-266)                168 (109-254)
 Infarct    growth      from   100 (42-177)                 90 (53-140)
 CTP/MRI core (ml)
 Infarct    growth      from   68 (22-128)                  66 (24-110)
 composite core (ml)
 Infarct growth from CT        87 (37-152)                  73 (31-135)
 hypodensity (ml)




                                              37

```

### DOC-006 physical page 39

Source: joi240006supp5_prod_1708623115.01733.pdf#page=39

```text
   eTable 3. Sensitivity analyses using site-investigator adjudicated ASPECTS.
                     mRS            shift
ASPECTS                                    mRS 0-2 (aRR mRS 0-3 (aRR             mRS 5-6 (aRR
                     (aGenOR        with
category                                   with 95% CI)          with 95% CI)    with 95% CI)
                     95% CI)
                     aGenOR:       1.70, aRR: 2.97, 95% CI: aRR: 2.23, 95%       aRR: 0.74, 95%
ASPECTS 3-5
                     95% CI: 1.33-2.17 1.60-5.49                 CI: 1.56-3.16   CI: 0.61-0.91
                     aGenOR:       1.91, aRR: 2.93, 95% CI: aRR: 1.91, 95%       aRR: 0.60, 95%
ASPECTS 6-10
                     95% CI: 1.04-3.54 0.42-20.47                CI: 0.75-4.90   CI: 0.35-1.02
                     aGenOR:       1.88, aRR: 7.82, 95% CI: aRR: 2.53, 95%       aRR: 0.66, 95%
ASPECTS 3
                     95% CI: 1.27-2.78 1.14-53.56                CI: 1.00-6.36   CI: 0.49-0.88
                     aGenOR:       1.51, aRR: 4.11, 95% CI: aRR: 2.44, 95%       aRR: 0.94, 95%
ASPECTS 4
                     95% CI: 0.92-2.48 1.40-12.09                CI: 1.39-4.29   CI: 0.62-1.44
                     aGenOR:       1.93, aRR: 2.08, 95% CI: aRR: 2.46, 95%       aRR: 0.71, 95%
ASPECTS 5
                     95% CI: 1.25-2.98 1.02-4.22                 CI: 1.56-3.90   CI: 0.50-1.01




                                               38

```

### DOC-006 physical page 40

Source: joi240006supp5_prod_1708623115.01733.pdf#page=40

```text
   eTable 4. Sensitivity analyses evaluating EVT treatment effect across CTP core strata (restricted
   to patients who received CT Perfusion only).
CTP core (rCBF mRS                   shift
                                            mRS 0-2 (aRR mRS 0-3 (aRR mRS 5-6 (aRR
<30%)      volume (aGenOR with 95%
                                            with 95% CI)       with 95% CI)        with 95% CI)
categories           CI)
                     aGenOR: 1.73, 95% aRR: 2.26, 95% aRR: 1.76, 95% aRR: 0.77, 95%
<70ml
                     CI: 1.20-2.48          CI: 1.15-4.43      CI: 1.24-2.50       CI: 0.53-1.11
                     aGenOR: 1.61, 95% aRR: 4.12, 95% aRR: 2.89, 95% aRR: 0.75, 95%
≥70ml
                     CI: 1.21-2.15          CI: 1.25-13.63     CI: 1.39-6.02       CI: 0.61-0.92
                     aGenOR: 1.86, 95% aRR: 2.75, 95% aRR: 2.05, 95% aRR: 0.68, 95%
<100ml
                     CI: 1.40-2.49          CI: 1.49-5.07      CI: 1.45-2.89       CI: 0.52-0.88
                     aGenOR: 1.44, 95% aRR: 3.36, 95% aRR: 3.04, 95% aRR: 0.82, 95%
≥100ml
                     CI: 1.00-2.06          CI: 0.52-21.64     CI: 0.95-9.73       CI: 0.64-1.04
                     aGenOR: 1.78, 95% aRR: 2.93, 95% aRR: 2.10, 95% aRR: 0.70, 95%
<150ml
                     CI: 1.39-2.30          CI: 1.62-5.30      CI: 1.51-2.92       CI: 0.56-0.87
                     aGenOR: 1.43, 95%                                             aRR: 0.83, 95%
≥150ml                                      N/A                N/A
                     CI: 0.80-2.54                                                 CI: 0.56-1.23
   N/A – could not be evaluated




                                                 39

```

### DOC-006 physical page 41

Source: joi240006supp5_prod_1708623115.01733.pdf#page=41

```text
eTable 5. Association of extent of ischemic injury on CT hypodensity and composite core
volumes and clinical outcomes within patients receiving EVT and MM.
                           Endovascular                   Medical Care Only Interaction
                           Thrombectomy (N=170)           (N=166)                  p-value
 mRS Distribution          Median (IQR): 4 (3-6)          Median (IQR): 5 (4-6)
 CT         hypodensity
                           aGenOR: 0.95, 95% CI: aGenOR: 0.98, 95% CI:
 volume(per        10ml                                                            0.14
                           0.93-0.98                      0.95-1.00
 increment)
 Composite          core
                           aGenOR: 0.92, 95% CI: aGenOR: 0.95, 95% CI:
 volume(per        10ml                                                            0.13
                           0.88-0.95                      0.92-0.98
 increment)
 mRS 0-2                   34/170 (20.0%)                 12/166 (7.2%)
 CT         hypodensity
                           aRR: 0.93, 95% CI: 0.89- aRR: 0.97, 95% CI:
 volume(per        10ml                                                            0.53
                           0.98                           0.87-1.09
 increment)
 Composite          core
                           aRR: 0.87, 95% CI: 0.82- aRR: 0.93, 95% CI:
 volume(per        10ml                                                            0.82
                           0.93                           0.83-1.05
 increment)
 mRS 0-3                   66/170 (38.8%)                 30/166 (18.1%)
 CT         hypodensity
                           aRR: 0.97, 95% CI: 0.91- aRR: 0.97, 95% CI:
 volume(per        10ml                                                            0.32
                           1.03                           0.91-1.03
 increment)
 Composite          core
                           aRR: 0.91, 95% CI: 0.85- aRR: 0.91, 95% CI:
 volume(per        10ml                                                            0.82
                           0.98                           0.85-0.98
 increment)
 mRS 5-6                   77/170 (45.3%)                 101/166 (60.8%)
 CT         hypodensity
                           aRR: 1.04, 95% CI: 1.02- aRR: 1.03, 95% CI:
 volume(per        10ml                                                            0.76
                           1.07                           1.01-1.05
 increment)
 Composite          core
                           aRR: 1.03, 95% CI: 1.00- aRR: 1.01, 95% CI:
 volume(per        10ml                                                            0.63
                           1.05                           1.00-1.03
 increment)
Footnotes:
CT- computed tomography
CTP – CT perfusion
MRI – Magnetic resonance imaging
ASPECTS – Alberta Stroke Program Early CT Score, a 10 point ordinal scoring system measuring
areas of hypoattenuation due to ischemic changes in the middle cerebral artery territory on non-
contrast CT of brain, with a point deducted for each location demonstrating hypoattenuation. Thus,
lower scores represent worse ischemic injury.
mRS – modified Rankin Scale score, a 7 level ordinal scoring system representing functional
status, with higher scores representing worse functional status (0 being without any deficits and 6
being dead).



                                                40

```

### DOC-006 physical page 42

Source: joi240006supp5_prod_1708623115.01733.pdf#page=42

```text
    eTable 6. Evaluation parameters for regression models for functional outcomes


Outcome     Modality            AIC                BIC           AUC (with 95% CI)        Preferred
                                                                                           modality
                                                                                          (based on
                                                                                             BIC
                                                                                         conventions)
Ordinal     ASPECTS        417.2590          447.8850           NA
 mRS
               CT          412.6195          443.2454           NA
           hypodensity
             volume
            CTP/MRI        403.2944          433.9203           NA
           core volume
            Composite      398.6922          429.3182           NA                       Preferred
           core volume
mRS 0-2     ASPECTS        256.9212          276.0068           0.7106 (0.6343-0.7870)
               CT          252.1431          271.2287           0.7224 (0.6481-0.7968)
           hypodensity
             volume
            CTP/MRI        239.4032          258.4887           0.7716 (0.7062-0.8370)
           core volume
            Composite      236.5431          255.6287           0.7783 (0.7103-0.8463) Preferred
           core volume
mRS 0-3     ASPECTS        358.6683          377.7538           0.7500 (0.6937-0.8062)
               CT          352.1023          371.1878           0.7522 (0.6965-0.8079)
           hypodensity
             volume
            CTP/MRI        329.0319          348.1174           0.7952 (0.7454-0.8450)
           core volume
            Composite      324.2519          343.3374           0.7977 (0.7472-0.8482) Preferred
           core volume


    Parameters for mRS distribution were calculated using ordinal logistic regression.
    Models with lower AIC and BIC values are considered more parsimonious
    Models with higher AUC values are considered to have better predictive value.
    N/A – not applicable




                                                   41

```

### DOC-006 physical page 43

Source: joi240006supp5_prod_1708623115.01733.pdf#page=43

```text
eTable 7. Association of presence or absence of mismatch profile based on composite core
volume with clinical outcomes within patients receiving EVT and MM (as-treated analysis).
 Presence       of mRS distribution
 mismatch
 profile(mismatc No mismatch (ref) 4 (3, 6)                  5 (4, 6)
 h volume≥10ml Mismatch                  4 (3, 6)            5 (4, 6)
 &       mismatch
 ratio≥1.2)      – Effect size with aGenOR:            0.77, aGenOR:        0.69, 0.73
 based          on   uncertainty         95%   CI: 0.50-1.17 95%   CI: 0.46-1.05
 Composite core estimates
 volume
                     Functional independence (mRS 0-2)
                   No mismatch (ref) 5/34 (14.7%)         3/40 (7.5%)
                   Mismatch            29/136 (21.3%)     9/126 (7.1%)
                   Effect size with aRR: 1.02, 95%        aRR: 0.63, 95% CI: 0.47
                   uncertainty      CI:    0.48-2.15,     0.20-1.94, aRD:-
                   estimates        aRD:-0.000, 95%       0.034, 95% CI: -
                                    CI: -0.155 to         0.123 to 0.056
                                    0.154
                   Independent ambulation (mRS 0-3)
                   No mismatch (ref) 13/34 (38.2%)        7/40 (17.5%)
                   Mismatch            53/136 (39.0%)     23/126 (18.3%)
                   Effect size with aRR: 0.77, 95%        aRR: 0.68, 95% CI: 0.79
                   uncertainty      CI:    0.48-1.26,     0.33-1.38, aRD:-
                   estimates        aRD:-0.097, 95%       0.064, 95% CI: -
                                    CI: -0.263 to         0.184 to 0.055
                                    0.070
                   Complete dependence or death (mRS 5-6)
                   No mismatch (ref) 12/34 (35.3%)        23/40 (57.5%)
                   Mismatch            65/136 (47.8%)     78/126 (61.9%)
                   Effect size with aRR: 1.31, 95%        aRR: 1.29, 95% CI: 0.83
                   uncertainty      CI:    0.80-2.15,     0.93-1.79,
                   estimates        aRD:0.127, 95%        aRD:0.168, 95%
                                    CI: -0.039 to         CI: 0.011 to 0.325
                                    0.293
 Presence      of mRS distribution
 mismatch
 profile(mismatc No mismatch (ref) 4 (3, 6)               5 (4, 6)
 h volume≥15ml Mismatch            4 (3, 6)               5 (4, 6)

                                           42

```

### DOC-006 physical page 44

Source: joi240006supp5_prod_1708623115.01733.pdf#page=44

```text
 &      mismatch     Effect size with aGenOR:     0.76, aGenOR:      0.73, 0.88
 ratio≥1.8)    –     uncertainty      95% CI: 0.50-1.18 95% CI: 0.53-1.02
 based        on     estimates
 Composite core
 volume              Functional independence (mRS 0-2)
                     No mismatch (ref) 21/112 (18.8%)           8/99 (8.1%)
                     Mismatch              13/58 (22.4%)        4/67 (6.0%)
                     Effect size with aRR: 0.60, 95%            aRR: 0.44, 95% CI: 0.76
                     uncertainty      CI:    0.30-1.21,         0.15-1.26, aRD:-
                     estimates        aRD:-0.099, 95%           0.061, 95% CI: -
                                      CI: -0.224 to             0.144 to 0.022
                                      0.027
                     Independent ambulation (mRS 0-3)
                     No mismatch (ref) 39/112 (34.8%)           18/99 (18.2%)
                     Mismatch              27/58 (46.6%)        12/67 (17.9%)
                     Effect size with aRR: 0.81, 95%            aRR: 0.66, 95% CI: 0.68
                     uncertainty      CI:    0.55-1.21,         0.38-1.14, aRD: -
                     estimates        aRD: -0.076, 95%          0.091, 95% CI: -
                                      CI: -0.228 to             0.202 to 0.020
                                      0.075
                     Complete dependence or death (mRS 5-6)
                     No mismatch (ref) 51/112 (45.5%)           60/99 (60.6%)
                     Mismatch              26/58 (44.8%)        41/67 (61.2%)
                     Effect size with aRR: 1.09, 95%            aRR: 1.21, 95% CI: 0.79
                     uncertainty      CI:    0.74-1.61,         0.94-1.56,
                     estimates        aRD:0.068, 95%            aRD:0.121, 95%
                                      CI: -0.088 to             CI: -0.017 to 0.260
                                      0.224
mRS – modified Rankin Scale score, a 7 level ordinal scoring system representing functional
status, with higher scores representing worse functional status (0 being without any deficits and 6
being dead).
Analyses are adjusted for age, NIHSS, time from last known well to randomization and CTP/MRI
core volume.




                                                43

```

### DOC-006 physical page 45

Source: joi240006supp5_prod_1708623115.01733.pdf#page=45

```text
eTable 8. Association of concordance/discordance between CT ASPECTS and ischemic core
estimates on CTP/MRI, within patients receiving EVT and MM.
                         Endovascular
                                                     Medical Care Only (N=156)
                         Thrombectomy (N=163)
                                                                                  Interaction
                         Median                      Median
                                    Effect      size             Effect size with p-value
 mRS Distribution        (IQR): 4                    (IQR): 5
                                    with 95% CI                  95% CI
                         (3-6)                       (4-6)
 Concordant imaging
 profiles
 (ASPECTS<6          & 5 (4-6)      Ref              5 (4-6)     Ref
 CTP/MRI
 core≥70ml)
 Discordant imaging
 profile             –                                           aGenOR: 1.50,
                                    aGenOR: 0.91
 1(ASPECTS<6         & 3 (2-6)                       4 (3-6)     95% CI: 0.94- 0.20
                                    (0.50, 1.65)
 CTP/MRI                                                         2.40
 core<70ml)
 Discordant imaging
                                                                 aGenOR: 0.65,
 profile – 2(ASPECTS                aGenOR: 1.01
                         5 (3.5-6)                   6 (6-6)     95% CI: 0.43- 0.26
 6-10 & CTP/MRI                     (0.53-1.92)
                                                                 0.99
 core≥70ml)
                         N (%):                      N      (%):
                                    Effect      size             Effect size with
 mRS 0-2                 32/163                      10/156
                                    with 95% CI                  95% CI
                         (19.6%)                     (6.4%)
 Concordant imaging
 profiles(ASPECTS<6 10/75
                                    Ref              3/82 (4%)   Ref
 &           CTP/MRI (13%)
 core≥70ml)
 Discordant imaging                 aRR:       0.51              aRR:        1.26
 profile             –              (0.16-1.56)                  (0.17-9.43)
                         21/76
 1(ASPECTS<6         &                               7/63 (11%)                   0.78
                         (28%)      aRD: -0.055 (-               aRD: 0.040 (-
 CTP/MRI
                                    0.201, 0.092)                0.059, 0.138)
 core<70ml)
 Discordant imaging                 aRR:       0.85
 profile – 2(ASPECTS                (0.12-5.79)
                         1/12 (8%)                   0/11 (0%)   N/A              N/A
 6-10 & CTP/MRI                     aRD: 0.010 (-
 core≥70ml)                         0.395, 0.415)
                         N (%):                      N      (%):
                                    Effect      size             Effect size with
 mRS 0-3                 62/163                      27/156
                                    with 95% CI                  95% CI
                         (38.0%)                     (17.3%)
 Concordant imaging
 profiles(ASPECTS<6 18/75
                                    Ref              8/82 (10%) Ref
 &           CTP/MRI (24%)
 core≥70ml)
 Discordant imaging 41/76           aRR:       0.86 19/63        aRR:        1.24
                                                                                  0.72
 profile             – (54%)        (0.43-1.71)      (30%)       (0.38-4.07)

                                           44

```

### DOC-006 physical page 46

Source: joi240006supp5_prod_1708623115.01733.pdf#page=46

```text
 1(ASPECTS<6           &
                                        aRD: 0.043 (-                   aRD: 0.060 (-
 CTP/MRI
                                        0.125, 0.211)                   0.075, 0.196)
 core<70ml)
 Discordant imaging                     aRR:       1.19
 profile – 2(ASPECTS 3/12               (0.43-3.28)
                                                           0/11 (0%)    N/A               N/A
 6-10 & CTP/MRI (25%)                   aRD: -0.065 (-
 core≥70ml)                             0.421, 0.291)
                           N (%):                          N      (%):
                                        Effect      size                Effect size with
 mRS 5-6                   75/163                          97/156
                                        with 95% CI                     95% CI
                           (46.0%)                         (62.2%)
 Concordant imaging
 profiles(ASPECTS<6 42/75                                  59/82
                                        Ref                             Ref
 &            CTP/MRI (56%)                                (72%)
 core≥70ml)
 Discordant imaging                     aRR:       0.92                 aRR:        0.69
 profile               –                (0.57-1.48)                     (0.49-0.97)
                           25/76                           28/63
 1(ASPECTS<6           &                                                                  0.14
                           (33%)        aRD: -0.077 (- (44%)            aRD: -0.076 (-
 CTP/MRI
                                        0.244, 0.091)                   0.248, 0.096)
 core<70ml)
 Discordant imaging                     aRR:       1.08                 aRR:        1.28
 profile – 2(ASPECTS 8/12               (0.69-1.68)        10/11        (1.01-1.63)
                                                                                          0.02
 6-10 & CTP/MRI (67%)                   aRD: 0.143 (- (91%)             aRD:       0.324
 core≥70ml)                             0.212, 0.498)                   (0.165, 0.483)
Footnotes:
CT- computed tomography
CTP – CT perfusion
MRI – Magnetic resonance imaging
ASPECTS – Alberta Stroke Program Early CT Score, a 10 point ordinal scoring system measuring
areas of hypoattenuation due to ischemic changes in the middle cerebral artery territory on non-
contrast CT of brain, with a point deducted for each location demonstrating hypoattenuation. Thus,
lower scores represent worse ischemic injury.
mRS – modified Rankin Scale score, a 7 level ordinal scoring system representing functional
status, with higher scores representing worse functional status (0 being without any deficits and 6
being dead).




                                                45

```

### DOC-006 physical page 47

Source: joi240006supp5_prod_1708623115.01733.pdf#page=47

```text
   eTable 9. Estimates of EVT treatment effect and corresponding interaction terms for concordant
   and discordant imaging profiles based on CTP/MRI core volume estimates
                            mRS distribution

                                                        mRS distribution(aGenOR Interaction
                           MM             EVT
                                                        with 95% CI)            p-value
Concordant        imaging
                                                    aGenOR: 1.60, 95% CI: 1.18 to
profiles(ASPECTS<6      & 5 (4, 6)       5 (4, 6)                                   Ref
                                                    2.18
CTP/MRI core≥70ml)
Discordant imaging profile
                                                    aGenOR: 1.87, 95% CI: 1.28 to
–     1(ASPECTS<6       & 4 (3, 6)       3 (2, 6)                                   0.66
                                                    2.74
CTP/MRI core<70ml)
Discordant imaging profile
                                                    aGenOR: 2.46, 95% CI: 1.14 to
– 2(ASPECTS 6-10 & 6 (6, 6)              5 (3.5, 6)                                 0.18
                                                    5.32
CTP/MRI core≥70ml)
                           Functional independence(mRS 0-2)
                                                                                    Interaction
                           MM            EVT        aRR with 95% CI
                                                                                    p-value
Concordant        imaging
                                         10/74      aRR: 4.62, 95% CI: 1.27 to
profiles(ASPECTS<6      & 3/83 (3.6%)                                               Ref
                                         (13.5%)    16.71
CTP/MRI core≥70ml)
Discordant imaging profile
                           7/63          21/76
–     1(ASPECTS<6       &                           aRR: 2.68, 95% CI: 1.25 to 5.76 0.56
                           (11.1%)       (27.6%)
CTP/MRI core<70ml)
Discordant imaging profile
– 2(ASPECTS 6-10 & 1/11 (9.1%) 0/12 (0%)            N/A                             N/A
CTP/MRI core≥70ml)
                           Independent ambulation(mRS 0-3)
                                                                                    Interaction
                           MM            EVT        aRR with 95% CI
                                                                                    p-value
Concordant        imaging
                                         18/74
profiles(ASPECTS<6      & 8/83 (9.6%)               aRR: 2.98, 95% CI: 1.44 to 6.17 Ref
                                         (24.3%)
CTP/MRI core≥70ml)
Discordant imaging profile               41/76
                           19/63
–     1(ASPECTS<6       &                (53.9%)    aRR: 1.90, 95% CI: 1.29 to 2.78 0.38
                           (30.2%)
CTP/MRI core<70ml)
Discordant imaging profile
                           3/11
– 2(ASPECTS 6-10 &                       0/12 (0%)  N/A                             N/A
                           (27.3%)
CTP/MRI core≥70ml)
                           Complete dependence or death (mRS 5-6)
                                                                                    Interaction
                           MM            EVT        aRR with 95% CI
                                                                                    p-value
Concordant        imaging
                           60/83         41/74
profiles(ASPECTS<6      &                           aRR: 0.76, 95% CI: 0.61 to 0.95 Ref
                           (72.3%)       (55.4%)
CTP/MRI core≥70ml)

                                                46

```

### DOC-006 physical page 48

Source: joi240006supp5_prod_1708623115.01733.pdf#page=48

```text
Discordant imaging profile
                             28/63     25/76
–    1(ASPECTS<6         &                       aRR: 0.72, 95% CI: 0.49 to 1.05 0.83
                             (44.4%)   (32.9%)
CTP/MRI core<70ml)
Discordant imaging profile
                             10/11     8/12
– 2(ASPECTS 6-10 &                               aRR: 0.59, 95% CI: 0.37 to 0.96 0.40
                             (90.9%)   (66.7%)
CTP/MRI core≥70ml)
    N/A – could not be evaluated




                                            47

```

### DOC-006 physical page 49

Source: joi240006supp5_prod_1708623115.01733.pdf#page=49

```text
eTable 10. Estimates of EVT treatment effect and corresponding interaction terms for
concordant and discordant imaging profiles based on composite core volume estimates
                           mRS distribution

                                                        mRS distribution(aGenOR with Interaction
                             MM             EVT
                                                        95% CI)                      p-value
Concordant        imaging
profiles(ASPECTS<6      & 5 (4, 6)        4 (3, 6)  aGenOR: 1.65, 95% CI: 1.26 to 2.16    Ref
composite core≥70ml)
Discordant imaging profile
–     1(ASPECTS<6       & 4.5 (3, 6)      3 (2, 6)  aGenOR: 1.80, 95% CI: 1.00 to 3.22    0.61
composite core<70ml)
Discordant imaging profile
– 2(ASPECTS 6-10 & 6 (6, 6)               5 (3, 6)  aGenOR: 2.66, 95% CI: 1.34 to 5.28    0.13
composite core≥70ml)
                           Functional independence(mRS 0-2)
                                                                                          Interaction
                             MM             EVT         aRR with 95% CI
                                                                                          p-value
Concordant        imaging
                                        18/112
profiles(ASPECTS<6      & 8/118 (6.8%)             aRR: 2.88, 95% CI: 1.34 to 6.20        Ref
                                        (16.1%)
composite core≥70ml)
Discordant imaging profile
                                        13/38
–     1(ASPECTS<6       & 2/28 (7.1%)              aRR: 3.71, 95% CI: 0.93 to 14.82       0.71
                                        (34.2%)
composite core<70ml)
Discordant imaging profile
– 2(ASPECTS 6-10 & 2/12 (16.7%) 0/14 (0%) N/A                                             N/A
composite core≥70ml)
                           Independent ambulation(mRS 0-3)
                                                                                          Interaction
                             MM             EVT         aRR with 95% CI
                                                                                          p-value
Concordant        imaging
                             19/118         35/112
profiles(ASPECTS<6      &                               aRR: 2.21, 95% CI: 1.41 to 3.48   Ref
                             (16.1%)        (31.3%)
composite core≥70ml)
Discordant imaging profile
                                            24/38
–     1(ASPECTS<6       &    8/28 (28.6%)               aRR: 1.83, 95% CI: 1.04 to 3.22   0.68
                                            (63.2%)
composite core<70ml)
Discordant imaging profile
– 2(ASPECTS 6-10 &           4/12 (33.3%)   0/14 (0%)   N/A                               N/A
composite core≥70ml)
                             Complete dependence or death (mRS 5-6)
                                                                                          Interaction
                             MM             EVT         aRR with 95% CI
                                                                                          p-value
Concordant       imaging
                         74/118             53/112
profiles(ASPECTS<6    &                                 aRR: 0.75, 95% CI: 0.60 to 0.92   Ref
                         (62.7%)            (47.3%)
composite core≥70ml)

                                             48

```

### DOC-006 physical page 50

Source: joi240006supp5_prod_1708623115.01733.pdf#page=50

```text
Discordant imaging profile
                             14/28     13/38
–    1(ASPECTS<6         &                       aRR: 0.90, 95% CI: 0.52 to 1.56   0.92
                             (50.0%)   (34.2%)
composite core<70ml)
Discordant imaging profile
                             11/12     9/14
– 2(ASPECTS 6-10 &                               aRR: 0.59, 95% CI: 0.39 to 0.88   0.38
                             (91.7%)   (64.3%)
composite core≥70ml)
 N/A – could not be evaluated




                                        49

```

### DOC-006 physical page 51

Source: joi240006supp5_prod_1708623115.01733.pdf#page=51

```text
eTable 11. Estimates of infarct growth from baseline in patients with MR DWI follow-up,
stratified based on treatment arm and reperfusion status.
 Factor                                MM                 mTICI 0-2a    mTICI 2b-3
 N                                     101                24            79
 Infarct growth from CTP/MRI
                                       95 (56, 135)       125 (76, 179) 68 (37, 142)
 core (ml), median (IQR)
 Infarct growth from composite
                                       63 (22, 102)       91 (71, 142)  45 (16, 90)
 core (ml), median (IQR)
 Infarct      growth     from    CT
                                       69 (31, 122)       107 (87, 152) 60 (24, 110)
 hypodensity (ml), median (IQR)




                                          50

```

### DOC-006 physical page 52

Source: joi240006supp5_prod_1708623115.01733.pdf#page=52

```text
eTable 12. Comparison of infarct growth in study population, based on functional outcomes.
                       Functionally Dependent Functionally                    p-value
                       (mRS 3-6)                   Independent (mRS 0-2)
                       N=290                       N=46
 Infarct growth from 102 (61-167)                  45 (32-88)                 <0.001
 CTP/MRI core (ml)
 Infarct growth from 77 (31-127)                   23.5 (11-48)               <0.001
 composite core (ml)
                       No           independent Independent Ambulation p-value
                       ambulation (mRS 4-6)        (mRS 0-3)
                       N=240                       N=96
 Infarct growth from 110.5 (65.5-174.5)            65.5 (32.5-100.5)          <0.001
 CTP/MRI core (ml)
 Infarct growth from 85.5 (36-144)                 31.5 (10-67)               <0.001
 composite core (ml)




                                            51

```

### DOC-006 physical page 53

Source: joi240006supp5_prod_1708623115.01733.pdf#page=53

```text
eTable 13. Characteristics of patients demonstrating significant(≥10ml) overestimation of
ischemic core as compared to follow-up infarct volume.
                                                                        Time from CTP
         CTP       or CT                Follow-up    Time from last acquisition to
 ID      MRI core hypodensity infarct                known well to CTP reperfusion/end
         volume(ml) volume(ml) volume(ml) acquisition(minutes) of                    the
                                                                        procedure(min)
 1       162            33              143          642                77
 2       140            0               90           289                N/A
 3       93             5               11           51                 125
N/A – not applicable (patient received medical management)




                                           52

```

## Administrative per-page map (B017)

DOC-002 is REPORT administrative content. Each of its30physical pages was opened in page-marked reusable text/layout. No result-relevant numeric, statistical, endpoint, intervention, population or prospective design relation appears. Names/institutional affiliations and form instructions are administrative observations. The printed form footer v02-22 and "Nof33" are form/page metadata, not participant counts. Pages18-25 repeat flattened name/institution data; pp26-27/29-30 contain institution-name continuations. Page28 contains no native text and no raster image according to direct pdfimages -f28 -l28 -list. This assessment is based on content inspection, not source naming.

| Source | Physical page | Inspected content | Quantitative applicability | Status |
|---|---:|---|---|---|
|DOC-002|1|SELECT2 Investigators group heading; Cleveland collaborator names/institutions|No applicable relationship|COMPLETE|
|DOC-002|2|Cleveland/Houston collaborator names/institutions|No applicable relationship|COMPLETE|
|DOC-002|3|Houston collaborator names/institutions|No applicable relationship|COMPLETE|
|DOC-002|4|Houston/Kansas collaborator names/institutions|No applicable relationship|COMPLETE|
|DOC-002|5|Kansas/Baptist/Cleveland Clinic names/institutions|No applicable relationship|COMPLETE|
|DOC-002|6|Cleveland Clinic/Rush/Austin/OhioHealth names/institutions|No applicable relationship|COMPLETE|
|DOC-002|7|OhioHealth/Kaiser/Abington names/institutions|No applicable relationship|COMPLETE|
|DOC-002|8|Abington/Valley Baptist/Ascension/Iowa names/institutions|No applicable relationship|COMPLETE|
|DOC-002|9|Iowa/Semmes Murphey/Thomas Jefferson names/institutions|No applicable relationship|COMPLETE|
|DOC-002|10|Thomas Jefferson/Pennsylvania names/institutions|No applicable relationship|COMPLETE|
|DOC-002|11|Pennsylvania names/institutions|No applicable relationship|COMPLETE|
|DOC-002|12|Pennsylvania/Corewell/Ascension names/institutions|No applicable relationship|COMPLETE|
|DOC-002|13|Ascension/Westchester/Toronto/Alberta/Melbourne names/institutions|No applicable relationship|COMPLETE|
|DOC-002|14|Melbourne/Adelaide/Liverpool names/institutions|No applicable relationship|COMPLETE|
|DOC-002|15|Liverpool/Christchurch/Vall d'Hebron names/institutions|No applicable relationship|COMPLETE|
|DOC-002|16|Vall d'Hebron/Barcelona/Germans Trias/Bellvitge names/institutions|No applicable relationship|COMPLETE|
|DOC-002|17|Bellvitge/Valladolid/Basel names/institutions|No applicable relationship|COMPLETE|
|DOC-002|18|Flattened repeated Cleveland/Houston name columns|No applicable relationship|COMPLETE|
|DOC-002|19|Flattened repeated Houston/Kansas/Baptist/Clinic/Rush columns|No applicable relationship|COMPLETE|
|DOC-002|20|Flattened repeated Rush/Austin/OhioHealth/Kaiser/Abington/Valley/Ascension columns|No applicable relationship|COMPLETE|
|DOC-002|21|Flattened repeated Ascension/Iowa/Semmes/Jefferson/Pennsylvania columns|No applicable relationship|COMPLETE|
|DOC-002|22|Flattened repeated Pennsylvania/Corewell/Ascension/Westchester columns|No applicable relationship|COMPLETE|
|DOC-002|23|Flattened repeated Westchester/Toronto/Alberta/Melbourne/Adelaide/Liverpool columns|No applicable relationship|COMPLETE|
|DOC-002|24|Flattened repeated Liverpool/Christchurch/Vall d'Hebron/Barcelona/Germans Trias columns|No applicable relationship|COMPLETE|
|DOC-002|25|Flattened repeated Germans Trias/Bellvitge/Valladolid/Basel columns|No applicable relationship|COMPLETE|
|DOC-002|26|Cleveland Medical Center and Houston institution-text continuations|No applicable relationship|COMPLETE|
|DOC-002|27|Houston institution-text continuation|No applicable relationship|COMPLETE|
|DOC-002|28|No native text or raster image; administrative continuation sheet|No applicable relationship|COMPLETE|
|DOC-002|29|Pennsylvania institution-text continuation|No applicable relationship|COMPLETE|
|DOC-002|30|Pennsylvania institution-text continuation|No applicable relationship|COMPLETE|
|DOC-007|1|Data-sharing statement, bibliographic date/DOI; Data available:No|No applicable result/design relationship|COMPLETE|

Exact source locator for each administrative row: joi240006supp1_prod_1708623114.97236.pdf#page=N where N is its printed Physical page column. DOC-007: joi240006supp6_prod_1708623115.02733.pdf#page=1. DOC-007 statement identifies Sarraj, Endovascular Thrombectomy for Large Ischemic Stroke Across Ischemic Injury and Penumbra Profiles, JAMA, published February07,2024, doi:10.1001/jama.2024.0572. The only data-availability response is "No"; it supplies no participant values or analysis definition.

## Handoff counts and limitations

Mapped52/52assigned physical pages: DOC-00621/21, DOC-00230/30, DOC-0071/1. DOC-006 all13eTables (19physical pages, including continuations) and6eFigure20panels (2pages) mapped; DOC-002/00731administrative pages explicitly not applicable.17local display/administrative group IDs B001-B017. Inferential scope by independently tracked pairs/tests is approximately180relationships:20eTable3estimate-CIs;22eTable4estimate-CIs;24eTable5(16estimate-CIs+8interactions);12eTable6model-comparison rows;36eTable7(28estimate-CIs+8last-column tests);30eTable8(24estimate-CIs+6interactions);16eTable9(10estimate-CIs+6interactions);16eTable10(same structure);4eTable12P-value comparisons. These are scope counts, not findings; table7last-column heading is not printed on assigned pages, so its8values require exact method-context matching. All displayed numeric/table cells are preserved; no inferential result is omitted to satisfy a scope bound.

No scientific coverage gap. Derivative limitations: legacy engine versions unrecorded, native figure digits crowded (resolved by visual reading), DOC-006Table7treatment/last-column headings absent on its assigned pages (preserved as label ambiguity), variable-specific denominators absent in some baseline rows (not invented), exact Table12test method absent from table pages (match assigned eMethods). There are no workbook formulas/cached values, direct Office sources or CSV result sources in this disjoint scope. No model/result diagnosis or candidate selection was performed.
# Protocol support map: DOC-003, physical PDF pages 1–82

Scope: all 82 pages of `joi240006supp2_prod_1708623114.99233.pdf`. Document role: **PLAN**, determined from the prospective SELECT2 protocol and its analysis specifications. The document is dated 4 August 2021 throughout; no separate dated prior protocol is bound here. Past-study results inside the scientific background are identified as historical rationale, not SELECT2 outcomes. Every page was opened in source-matched reusable layout/native text; seven graphic/formula-bearing pages were also inspected using freshly rendered source images. No scientific candidates or adjudications are made by this map.

Reusable locators: `.ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-003/by_page.txt` and `layout.txt`; curator reports direct-source layout identity. Rendering engine: direct Poppler `pdftoppm` 26.01.0 on CPU, command `pdftoppm -f N -l N -scale-to 1400 -singlefile -png "joi240006supp2_prod_1708623114.99233.pdf" ".ai_paper_validation/review_1_6_2/preprocessing/support_protocol/page-N"`, N=13,18,21,71,78,80,81. For pages13 and18 the same command used `-scale-to 1800`; the other five used1400. Outputs are seven matching PNG files under that directory. No OCR, fallback environment, Office formula or cached workbook value applies. These fresh renders close embedded-graphic transcription gaps in the reusable text. All page numbers below are physical PDF pages and also match printed protocol pagination. Source remains final authority.

Local P keys below are mapping keys, not candidate or final statistical inventory IDs. Main-paper matching keys are semantic because this shard does not inspect another agent's disjoint main-paper source. They identify imaging selection, ischemic core/ASPECTS, mismatch, 90-day mRS, functional independence, safety, and treatment-effect heterogeneity for downstream matching.

## Complete page-level coverage

| PDF page | Content and quantitative applicability | Mapping keys |
|---:|---|---|
| 1 | Protocol title, version date 4 August 2021; prospective identity | P01 |
| 2 | Agreement/signature form; no result-relevant quantitative relationship | P01 |
| 3 | Steering, neurointerventional and core-lab personnel; no applicable relationship | P01 |
| 4 | Statistical committee and DSMB personnel; no applicable relationship | P01 |
| 5 | Contents, including imaging thresholds in headings and outcome/analysis pointers; underlying sections mapped | P02, P04, P09 |
| 6 | Contents including interim bounds, randomization and device appendices; underlying sections mapped | P09, P15, P18 |
| 7 | Synopsis aims, trial design, 8 general inclusion criteria | P02, P03 |
| 8 | Synopsis exclusions and imaging criteria; 2 primary outcomes; first secondary items | P02, P04, P05 |
| 9 | Remaining secondary/imaging outcomes, imaging assessment and all 8 balancing variables | P05, P06, P07 |
| 10 | Arms, antithrombotic dosing and follow-up schedule | P03, P08 |
| 11 | Historical trial time windows/imaging thresholds, not current results | P20 |
| 12 | Historical trial imaging/mismatch thresholds and core distributions | P20 |
| 13 | Historical SELECT treatment effects and Figure 1 mRS distribution | P20 |
| 14 | Historical SELECT safety and MR CLEAN/other cohorts | P20 |
| 15 | Historical matched-cohort outcomes; aim and discordance rationale | P20, P03 |
| 16 | Historical SELECT counts/outcomes in early-window discordance and DEFUSE3 subset | P20 |
| 17 | Explicit amendment to include >100-cc core, no perfusion-volume upper bound | P02, P19 |
| 18 | ASPECTS 0–2 exclusion rationale; historical Figure 2 mRS bars | P20 |
| 19 | Historical trial imaging-selection rationale; no new current analysis specification | P20 |
| 20 | Imaging discordance comparison rationale | P03 |
| 21 | Historical Figure 3: profile frequencies and 90-day good outcome; visually inspected | P20 |
| 22 | Second-aim 15% superiority margin, historical 48% vs 32% rates | P03 |
| 23 | Imaging-profile treatment-effect heterogeneity; favorable CT/unfavorable perfusion efficacy aim | P03 |
| 24 | RAPID definitions/assessment priority and historical agreement; extracranial ICA rationale | P06, P20 |
| 25 | Extracranial ICA historical counts; primary and second aim | P03, P20 |
| 26 | Second-aim subparts; prospective open-label trial with imaging processing | P03, P06 |
| 27 | Randomized arm definition and 0–24-hour window | P03 |
| 28 | Screening population, Table 1 all 8 general inclusion criteria | P02 |
| 29 | Table 1 general exclusions; imaging inclusion; first imaging exclusions | P02 |
| 30 | Remaining imaging exclusions; enrollment/consent | P02 |
| 31 | Remote consent procedure; no result-relevant quantitative relationship | P21 |
| 32 | Remote consent, including 15–20-minute follow-up contact; administrative | P21 |
| 33 | Consent then all 8 adaptive randomization factors/categories | P07 |
| 34 | Minimization, 1:1 arms, site imaging primary and core-lab secondary assessment | P07, P06 |
| 35 | Thrombectomy timing and devices; goal puncture within 45 minutes, required within 90 minutes of qualifying imaging | P08 |
| 36 | IA thrombolysis prohibited; extracranial stenting beyond 72 hours preferred; medical arm therapy | P08 |
| 37 | Aspirin continuation; 2 primary outcomes; safety secondary list begins | P04, P05, P08 |
| 38 | Remaining secondary and imaging outcomes; clinical and imaging assessments | P05, P06 |
| 39 | Blinded angiographic core-lab assessment continuation | P06 |
| 40 | Table 2 complete visit/assessment schedule including 365 days | P08 |
| 41 | Schedule footnotes, timing origin and blinded assessments | P08 |
| 42 | 90-day and added 365-day follow-up; neurological worsening and SAE reporting | P08, P19, P05 |
| 43 | Site approval/monitoring, annual volume ≥100; no endpoint effect estimate | P21 |
| 44 | Site surveillance every 6 months; adaptive enrichment design description | P09 |
| 45 | 6 ordered imaging/time strata, 5 cumulative subgroups, ITT primary WMW and adjusted CMH | P09, P10 |
| 46 | Projected 7-category mRS distributions, sample size/power/alpha/interim counts | P11 |
| 47 | First interim 200 and second interim 380 decision trees | P12 |
| 48 | Final 560 decision tree; simulation assumptions and group proportions | P12, P13 |
| 49 | Table 3 all 8 simulation scenarios and operating characteristics | P13 |
| 50 | Secondary logistic analyses, reporting measures, tests and subgroup list | P14 |
| 51 | Remaining subgroups, second-aim logistic/interaction models, poolability | P03, P14 |
| 52 | Site interaction pooling; feasibility; 90-day mRS multiple imputation | P14, P16 |
| 53 | Timetable and imaging risk narrative; administrative/historical exposure context | P21 |
| 54 | Radiation/contrast risk quantities; not trial estimates or analysis assumptions | P21 |
| 55 | Risk mitigation and early-window unfavorable-perfusion safety trigger | P17 |
| 56 | >20% MM-vs-EVT mortality trigger continuation, no upper core bound; Bayesian safety design | P17, P19 |
| 57 | 2-step sICH probability rules, prior, ≤100-cc monitoring schedule | P17 |
| 58 | ≤100-cc sICH threshold table, >100-cc schedule/prior | P17 |
| 59 | >100-cc sICH table; extracranial ICA monitoring/prior | P17 |
| 60 | Extracranial ICA sICH table; 2-step 90-day mortality rules | P17 |
| 61 | ≤100-cc mortality prior, schedule and table | P17 |
| 62 | >100-cc mortality table; extracranial ICA schedule/prior | P17 |
| 63 | Extracranial ICA mortality table; DSMB independent final decision | P17 |
| 64 | Blinded core-lab assessments; Tmax >6 s and relative CBF <30% definitions | P06 |
| 65 | Data management operations; no result-relevant quantitative relationship | P21 |
| 66 | Data audit; DSMB mortality/sICH/neurological deterioration definitions and procedural safety list | P05, P17 |
| 67 | Procedural safety list continuation, reporting within 24 h; DSMB monitoring cadence | P05, P21 |
| 68 | Itemized AE/SAE/device-event definitions | P05 |
| 69 | AE collection randomization through day 90; attributes | P05 |
| 70 | AE intensity/causal relationship categories and reporting; no effect estimate | P05 |
| 71 | Fully graphical study design: eligibility, arms, imaging groups, 3 imaging analyses; visually inspected | P03, P22 |
| 72 | References only; no applicable new quantitative relationship | P21 |
| 73 | References only; no applicable new quantitative relationship | P21 |
| 74 | References only; no applicable new quantitative relationship | P21 |
| 75 | References only; no applicable new quantitative relationship | P21 |
| 76 | Appendix A all 8 minimization factors/categories repeated | P07, P15 |
| 77 | General minimization algorithm definitions and imbalance function | P15 |
| 78 | Minimization formulas and weight table; visually inspected | P15 |
| 79 | Weight table continuation and probability assignment 0.9/0.5/0.1 | P15 |
| 80 | Appendix B WMW statistic, subgroup efficacy/futility rules; visually inspected | P18 |
| 81 | Final cutoff, exact boundary values and hypothesis-direction formula; visually inspected | P18 |
| 82 | Appendix C all 7 stent-retriever and 9 aspiration entries | P08 |

Coverage: 82/82 mapped; 75 reusable-backed; 7 fresh-required graphic/formula units closed by 7 targeted direct-source rendered pages. No uncovered source page.

## Prospective design and quantitative relationships

### P01 — Identity and version status

[Protocol p. 1](../../../joi240006supp2_prod_1708623114.99233.pdf#page=1) titles SELECT2 as a randomized trial optimizing endovascular patient selection, dated 4 August 2021. Pages 2–6 are agreement, personnel and contents. No version history table or distinct earlier dated protocol is present. P19 records explicit amendment descriptions embedded within this version; their existence must be retained during cross-source comparisons rather than assuming unchanged original design.

### P02 — Complete eligibility and imaging criteria

[Synopsis pp. 7–8](../../../joi240006supp2_prod_1708623114.99233.pdf#page=7), [Table 1 pp. 28–30](../../../joi240006supp2_prod_1708623114.99233.pdf#page=28): general inclusion items are (1) adults 18–85 with final acute ischemic stroke diagnosis; (2) NIHSS ≥6; (3) last known well to groin puncture or medical management 0–24 hours; (4) prestroke mRS 0–1; (5) eligible for thrombectomy or medical management; (6) signed informed consent; (7) willingness to comply with follow-up; (8) anticipated life expectancy ≥3 months.

General exclusion items: (1) inability to undergo CTA and/or CT/MR perfusion, including renal insufficiency/contrast allergy; (2) psychiatric or medical illness confounding neurological assessment; (3) IV thrombolysis beyond 4.5 hours; (4) IV thrombolysis 3–4.5 hours AND any of age >80, current anticoagulant use, both diabetes and prior stroke, NIHSS >25, or >one-third MCA ischemic involvement; (5) another investigational drug/device study.

Imaging inclusion items: (1) ICA or MCA-M1 large-vessel occlusion by MRA/CTA; carotid occlusions cervical or intracranial, with/without tandem MCA lesion; (2) large core on **at least one** of NCCT ASPECTS 3–5, CTP rCBF<30% core ≥50 cc, MRI-DWI ADC<620 core ≥50 cc. ASPECTS 0–2 excluded, footnote p.29.

Imaging exclusion items: (1) BOTH ASPECTS 6–10 AND perfusion core <50 cc; (2) NCCT ASPECTS ≤2; (3) intracranial tumor except small meningioma, acute intracranial hemorrhage, neoplasm or AVM; (4) significant mass effect/midline shift; (5) flow-limiting ICA dissection or aortic dissection; (6) same-territory intracranial stent precluding safe neurothrombectomy device deployment/removal; (7) acute symptomatic occlusions in >one vascular territory; (8) established infarct and large cerebral edema on NCCT. No perfusion-volume upper cap remains in this dated protocol, explicitly stated pp.17,56.

Main-paper matching keys: randomized population; core definition rCBF<30%/ADC<620; ASPECTS 3–5 vs 6–10; core ≥50 mL; no upper cap; 24-hour eligibility. cc and mL denote volume here; no numeric unit conversion is needed.

### P03 — Arms, aims, discordance comparison and superiority margin

[pp.7,22–27](../../../joi240006supp2_prod_1708623114.99233.pdf#page=22), p.34: randomized arms are thrombectomy **plus** medical management versus medical management alone, 1:1, prospective international multicenter assessor-blinded/open-label treatment design. Primary aim tests EVT efficacy/safety in unfavorable imaging on either modality within 24 hours. Second aim has two explicitly enumerated components: (A) compare 90-day mRS 0–2 rates **among EVT patients** with unfavorable CT/favorable perfusion versus favorable CT/unfavorable perfusion; (B) evaluate heterogeneity of randomized EVT-vs-MM effect between those discordant imaging profiles.

P.22 states prior SELECT good outcome 48% vs 32%, absolute difference 16%, and sets a **15% superiority margin** between discordance groups. If differences do not reach that margin, the text says outcome rates did not differ. P.51 specifies logistic regression, OR and 95% CI for the EVT-only good-outcome comparison and treatment×imaging-profile logistic interaction for treatment-effect heterogeneity. If significant, evaluate confounding baseline/patient characteristics. Preserve the p.51 printed contrast exactly: “favorable CTP/unfavorable CT” versus “unfavorable CT/favorable CTP”; both word orders are retained here without silently rewriting. The broader aim/diagram distinguishes the two discordant directions. The p.71 graphical labels and additional third imaging analysis are separately mapped in P22.

Main-paper matching keys: imaging discordance; core/ASPECTS interactions; 90-day functional independence; EVT-versus-MM imaging heterogeneity.

### P04 — Outcome status and 90-day primary endpoint

[Synopsis p.8](../../../joi240006supp2_prod_1708623114.99233.pdf#page=8): first primary outcome is 90-day mRS shift, second primary is favorable mRS 0–2. [Outcome section p.37](../../../joi240006supp2_prod_1708623114.99233.pdf#page=37) explicitly says “primary outcome #1” distribution of mRS at 90 days and “primary outcome #2” percentage of mRS 0–2 at 90 days. Window 90±15 days; blinded certified raters unaware of baseline clinical/radiographic features, preferably in person, telephone if necessary. The reason given for retaining distributional outcome is potential benefit across disability categories, e.g. mRS5 to4 or3, not only independence.

[Primary analysis p.45](../../../joi240006supp2_prod_1708623114.99233.pdf#page=45) identifies mRS distribution at day90. [Secondary analysis p.50](../../../joi240006supp2_prod_1708623114.99233.pdf#page=50) calls mRS0–2 at day90 the “secondary endpoint,” and supplies its adjusted logistic model. Both printed status assignments are mapped rather than reconciled by this extraction. Clinical death coded mRS6 (p.52).

Main-paper matching keys: primary ordinal mRS; functional independence mRS0–2 and its stated hierarchy; 90-day analysis population/window.

### P05 — Secondary, imaging, and safety outcomes, item by item

[pp.8–9,37–38](../../../joi240006supp2_prod_1708623114.99233.pdf#page=38): secondary outcomes: (1) safety incidence sICH per SITS-MOST, neurological worsening ≥4 NIHSS points within24h due to stroke itself, mortality, access/groin hematomas, infections, any EVT-caused vascular injury; (2) partial/complete recanalization by modified TICI, favorable reperfusion ≥2b; (3) hospital stay; (4) discharge location; (5) significant NIHSS improvement ≥8 points at24h or NIHSS0–1. Synopsis also separately names NIHSS and Neuro-QoL as secondary measures. No composite summation rule is supplied; listed safety components are retained individually.

Imaging outcomes: (1) MRI-DWI infarct volume, CT if MRI infeasible,24h–7d after randomization; (2) growth between baseline RAPID core and follow-up infarct; (3) successful reperfusion printed definition “DWI lesion volume minus Tmax>6 seconds greater than 50%”; no denominator or algebraic normalization supplied at these locations; (4) proportion with primary occlusive-lesion recanalization. Technical efficacy mTICI2b=50–75%,2c=>75–99%,3=complete. P.50 groups successful reperfusion/recanalization as binary secondary outcomes; infarct volume/growth as imaging outcomes.

[pp.66–67](../../../joi240006supp2_prod_1708623114.99233.pdf#page=66) DSMB safety definitions: stroke-related mortality at90d; sICH within24h after randomization, ≥4-point pre- versus post-deterioration NIHSS worsening associated with brain hemorrhage; significant neurological deterioration **prior to discharge**, ≥4-point worsening not attributed to sedation. Procedural items: intraprocedural mortality, vessel perforation, arterial dissection, access complication requiring surgical repair or blood transfusion, embolization, device failure. P.42 neurological worsening ≥4 points prior to discharge is reportable AE and triggers prompt CT/MRI.

[pp.68–70](../../../joi240006supp2_prod_1708623114.99233.pdf#page=68): AE is any untoward/undesirable clinical occurrence without requiring causal treatment relationship; only investigator-deemed clinically significant abnormal lab values are AEs. SAE component list: death; life-threatening experience; inpatient hospitalization/prolongation; persistent/significant disability/incapacity or congenital anomaly; medically important event jeopardizing patient/requiring intervention to prevent those outcomes. The final category explicitly includes IA thrombolytic and/or intracranial stent use. AADE is device/procedure effect identified in protocol/device instructions. UADE is serious health/safety effect, life-threatening problem or death linked to device and previously unidentified in nature/intensity/incidence, or other unanticipated serious device problem affecting rights/safety/welfare. AE collection starts randomization and runs throughday90 (p.69). Eight attributes: description,onset,resolution,seriousness,device/procedure relationship,intensity,actions,outcome. Source AE intensity categories are asymptomatic/mild, moderate, severe, life-threatening, death; causal relation unrelated,unlikely,reasonable possibility,definitely. These are source event definitions, not reviewer-assigned classifications. SAEs reported within24h of awareness (p.67) and within24h of event in REDCAP (p.42).

Main-paper matching keys: symptomatic hemorrhage; neurological worsening; mortality; reperfusion; infarct volume/growth; follow-up safety period.

### P06 — Imaging measurement and assessment hierarchy

[pp.9,24,26,34,38–39,64](../../../joi240006supp2_prod_1708623114.99233.pdf#page=64): site physician ASPECTS read independently before automated ASPECTS and overrides software if disagreement; RAPID supplies CTP mismatch. P.34 site imaging assignment final for primary analysis, explicitly planned secondary core-lab imaging assessment for discordance with site assessment. Core lab blinded to treatment and clinical variables; CT and MRI read at different times. Baseline ASPECTS, follow-up location/hemorrhage, CTA occlusion/collaterals, angiographic mTICI, core and hypoperfusion assessed. Tissue at risk Tmax>6s; irreversibly injured tissue relativeCBF<30% normal tissue; DWI core ADC<620 (eligibility sections). Perfusion imaging obtained for all randomized candidates. No current trial estimate appears in this prospective measurement specification.

Main-paper matching keys: core-lab-versus-site ASPECTS; CTP core/perfusion volumes; Tmax>6 seconds; CT/MRI selection.

### P07 — All adaptive randomization factors and their categories

[pp.9,33–34,76](../../../joi240006supp2_prod_1708623114.99233.pdf#page=33): emergency-room web-based Pocock–Simon minimization, 1:1. It balances overall arms, expressly not imaging subgroups or mutually exclusive combinations.

| Factor | Categories |
|---|---|
| Age | <60,60–69,70–79,80–85 years |
| Baseline NIHSS | 6–9,10–15,16–20,>20 |
| Center | enrolling site |
| Clot location | M1,ICA |
| Onset-to-randomization window | 0–8,9–16,17–24 h |
| CTP/MRP core | <50,50–100,>100 cc |
| Target mismatch | ratio≥1.8 AND volume≥15cc versus ratio<1.8 OR volume<15cc OR both |
| Hemisphere | right,left |

These categories are not the separate0–12/12–24h adaptive-enrichment groups in P09. P10/P14 refer to randomization variables as adjustment inputs.

### P08 — Intervention, device list and all follow-up time points

[pp.10,35–36](../../../joi240006supp2_prod_1708623114.99233.pdf#page=35): EVT femoral-puncture goal within45min of randomization and required within90min of qualifying imaging; approved stent-retriever and/or aspiration or combined approach chosen by interventionalist. ICA,MCA-M1 and if needed M2 locations. Carotid angioplasty/stenting allowed for severe proximal stenosis; IA thrombolytic prohibited. Extracranial immediate stenting discouraged, >72h preferred. Standard medical therapy in both arms; IV thrombolysis ≤3h or≤4.5h under applicable eligibility. Synopsis non-thrombolysis aspirin325mgday1 and81–325mg/daydays2–5, physician preference, unless indication for early anticoagulation. Body p.37 says81mg or325mg thereafter, equivalent regimens where unavailable, IV anticoagulation/dual antiplatelet discouraged absent documented rationale. No randomized drug-dose comparison is defined.

[Table2pp.40–41 and visit textpp.41–42](../../../joi240006supp2_prod_1708623114.99233.pdf#page=40): screening eligibility/log; enrollment consent; baseline/randomization demographics,physicalexam,vitals,labs(platelets,creatinine,glucose,INR,activatedPTT,pregnancy if applicable),medical history/medications/characteristics,NIHSS,mRS,imaging; EVT procedural data at procedure; hourlyBP through treatment+24h. Medical-arm BP starts thrombolysis if used orrandomization; EVT BP starts procedure completion. NIHSS baseline,day1(24±6h),day5–7/discharge. mRS baseline,day5–7/discharge,day30±15,day90±15,day365±60. Neuro-QoL90and365days. Postprocedure MRI(orCT)24h–7d. Central imageCRF baseline,procedure,day1,discharge. AE/SAE reporting day1,discharge,day30,day90; crossover explanations baseline; protocol deviations baseline/day1/discharge/day30/day90. Day1 visit18–30h afterprocedure; discharge visitday5–7 or discharge whicheverfirst. 30/90day mRS certified blinded rater,preferably inperson,phone if onlyoption. Body365dayvisit text also calls Neuro-QoL a360-day assessment; source wording retained. Added365dayvisit requires supplementalconsent for earlierenrollees (P19).

[AppendixCp.82](../../../joi240006supp2_prod_1708623114.99233.pdf#page=82), complete device entries:

| Device family | Clearance identifier and printed device |
|---|---|
| Stent retriever | K173352 Trevo ProVue Retriever and Trevo XP ProVue Retriever |
| Stent retriever | K162539 Solitaire2 Revascularization Device |
| Stent retriever | K173452 EmboTrapII Revascularization Device |
| Stent retriever | K203219 Trevo XP ProVue Retriever,Trevo NXT ProVue Retriever |
| Stent retriever | K193576 Solitaire Platinum and SolitaireX Revascularization Devices |
| Stent retriever | K193063 EmbotrapIII Revascularization Device |
| Stent retriever | K203592 Tigertriever and Tigertriever17 Revascularization Device |
| Aspiration | K173761 Penumbra System(Reperfusion Catheter JET7) |
| Aspiration | K173200 SOFIA Plus Aspiration Catheter |
| Aspiration | K183464 AXS Universal Aspiration System |
| Aspiration | K191768 AXS Vecta Aspiration System |
| Aspiration | K190338 Zenith Flex Aspiration System |
| Aspiration | K193380 Cerenovus Large Bore Catheter;Cerenovus Aspiration Tubing Set |
| Aspiration | K201689 Riptide Aspiration System |
| Aspiration | K202182 ZOOM Reperfusion Catheters;ZOOM Aspiration Tubing |
| Aspiration | K211476 ZOOM71 Reperfusion Catheter;ZOOM Aspiration Tubing |

### P09 — Adaptive enrichment groups and order

[pp.44–45](../../../joi240006supp2_prod_1708623114.99233.pdf#page=45): 2 interims and final; GLR/Kullback–Leibler criterion selects promising subpopulation after overall futility, allowing future accrual to selected group. Six disjoint groups ordered prior largest-to-smallest effect:

| Group | Imaging | Time window |
|---|---|---|
| G1A | ASPECTS3–5,core<50cc | 0–12h |
| G1B | ASPECTS3–5,core<50cc | 12–24h |
| G2A | ASPECTS6–10,core≥50cc | 0–12h |
| G2B | ASPECTS6–10,core≥50cc | 12–24h |
| G3A | ASPECTS3–5,core≥50cc | 0–12h |
| G3B | ASPECTS3–5,core≥50cc | 12–24h |

Five candidate cumulative populations: G1A;G1A+G1B;G1A+G1B+G2A;G1A+G1B+G2A+G2B;G1A+G1B+G2A+G2B+G3A. Overall addsG3B. No claim that these names match Figurep.71 group numbers is made; diagram numbering retained independently in P22.

### P10 — Primary model and adjustment

[Protocol p.45](../../../joi240006supp2_prod_1708623114.99233.pdf#page=45): primary mRS distribution at 90 days; null tested at interim and final analysis by a normal approximation of the Wilcoxon–Mann–Whitney test, called the GLR test. Intention-to-treat applies. Additional rank-based comparison uses generalized CMH to evaluate uniform shift after stratifying by adaptive randomization factors. Age, NIHSS, treatment time and CTP core volume are considered continuous in the adjusted analysis. Site imaging assignment is final for the primary analysis; core-lab imaging assessment is prespecified secondary (p.34). Matching keys: ordinal mRS, rank-based method, CMH, covariates and ITT.

### P11 — Sample size and complete projected outcome distribution

[Protocol p.46](../../../joi240006supp2_prod_1708623114.99233.pdf#page=46): projected mRS percentages at day90:

| Arm | mRS0 | 1 | 2 | 3 | 4 | 5 | 6 | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| EVT | 4 | 8 | 12 | 16 | 19 | 13 | 28 | 100% |
| MM | 1 | 4 | 9 | 14 | 19 | 10 | 43 | 100% |

Projected standardized effect 0.34; nonadaptive fixed design 376 total,188 per arm,90% power,5% alpha using WMW. Additional184 yields adaptive maximum560. Interims200 and380. Simulations claim around91% power for effect0.34 homogeneous across all six groups with overall one-sided Type I rate2.5%. Appendix B uses power0.9 and specifies boundaries in P18. After subgroup selection the maximum analyzed sample size becomes a random variable below560; futility becomes easier owing to reduced available patients (pp.46–47).

### P12 — Complete interim and final decision trees

[Protocol pp.47–48](../../../joi240006supp2_prod_1708623114.99233.pdf#page=47): first interim requires200 randomized patients who completed90-day follow-up. Neither bound crossed: continue overall recruitment. Efficacy crossed: stop with overall efficacy. Futility crossed: select the optimal GLR subgroup and test it; neither bound then means continue only subgroup accrual, efficacy means stop for subgroup efficacy, and futility means stop. Subgroup futility is relaxed based on expected available maximum=560 minus patients already enrolled in groups excluded from future accrual.

Second interim requires380 randomized patients who completed90-day follow-up. If overall accrual continued, repeat the first-interim tree. If restricted subgroup accrual continued, neither bound means180 further subgroup patients (560−380), efficacy means stop for subgroup efficacy, and futility means stop.

Final analysis at560 randomized with completed90-day follow-up: if overall accrual continued, test overall efficacy; if absent, select and test the optimal subgroup, declare subgroup efficacy if its bound is crossed, otherwise declare no benefit. If accrual was already restricted, test only the selected subgroup. Appendix B differentiates interim b and final c. No separate multiplicity rule for two clinical primary outcomes is printed here; the distributional adaptive design controls overall one-sided2.5%.

### P13 — Complete simulation table

[pp.48–49](../../../joi240006supp2_prod_1708623114.99233.pdf#page=49): 5000 simulated trials; adaptive maximum560 versus fixed560. Group frequencies G1A,G1B,G2A,G2B,G3A,G3B are14%,6%,14%,6%,42%,18%. Anticipated effect0.34; conservative effects0.32 or0.30.

| Scenario | G1A | G1B | G2A | G2B | G3A | G3B | Average standardized effect | Adaptive average N | Adaptive power | Fixed N | Fixed power |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 426 | 2.0% | 560 | 2.5% |
| 1 | .32 | .32 | .32 | .32 | .32 | .32 | .32 | 376 | 86.0% | 560 | 95.8% |
| 2 | .3 | .3 | .3 | .3 | .3 | .3 | .3 | 393 | 81.1% | 560 | 93.3% |
| 3 | .4 | .4 | .4 | .4 | 0 | 0 | .16 | 500 | 74.1% | 560 | 45.7% |
| 4 | .4 | .4 | .4 | .4 | −.1 | −.1 | .1 | 502 | 78.5% | 560 | 21.2% |
| 5 | .4 | .4 | .3 | .3 | 0 | −.1 | .122 | 513 | 67.1% | 560 | 29.2% |
| 6 | .5 | .5 | 0 | 0 | 0 | 0 | .1 | 503 | 70.6% | 560 | 21.2% |
| 7 | .5 | 0 | 0 | 0 | 0 | 0 | .07 | 503 | 60.5% | 560 | 12.8% |

Caption: null total Type I rate below2.5%, futility stop59.1%, average N426. Uniform effect0.32 trades power95.8% to86.0% and N560 to376. Heterogeneous scenarios are prospective adaptive-enrichment operating assumptions, not observed SELECT2 estimates.

### P14 — Secondary models, subgroups and site interaction

[Protocol pp.50–52](../../../joi240006supp2_prod_1708623114.99233.pdf#page=50): mRS0–2 at day90 uses logistic regression adjusted for adaptive-randomization variables. The text describes a difference in proportions and reports adjusted ORs with95% CIs. Binary safety outcomes and successful reperfusion/recanalization use chi-square or Fisher exact tests plus logistic regression adjusted for randomization variables. Continuous measures: mean±SD or median/IQR, two-sample t or Wilcoxon rank-sum tests, including stay and infarct volume. Discharge disposition: frequency/percentage and chi-square or Fisher exact. Secondary analyses are called exploratory.

Subgroup list, each retained: randomization factors; race; ethnicity; thrombolysis versus none; CTP versus MRI selection; witnessed versus unwitnessed onset; wake-up versus non-wake-up stroke; TICI0–2a versus2b/3; extracranial ICA occlusion; thrombolytic therapy received. Second-aim interaction is in P03. Poolability uses treatment-by-site interaction; significance prompts examination of patient characteristics and confounding; sites with fewer than5 subjects pooled geographically. No distinct cutoff or interaction model for each general subgroup is given here beyond second-aim/site models.

### P15 — Minimization formulas and complete printed weights

[AppendixApp.76–79](../../../joi240006supp2_prod_1708623114.99233.pdf#page=77): K treatment arms with1:1:…:1 allocation; S balancing variables; Q_f levels; Z_f in1,…,Q_f; new patient level l_f. Existing matching-level counts N_k(Z_f=l_f). Hypothetical imbalance I_k=D(N_1,…,N_k+1,…,N_K), where D measures variation. Overall G_k=sum(w_f I_k); choose k*=argmin G_k with highest probability. For variance D, G_k=2[sum(w_f N_k)]/(K−1)+constant, so it minimizes weighted matching-level counts. These are printed formulas, not workbook formulas.

| Factor | Printed weight |
|---|---:|
| Age | 4 |
| NIHSS | 4 |
| Clot location | 3 |
| Time window | 3 |
| Core volume | 2 |
| Target mismatch | blank cell on source p.78 |
| Hemisphere | 1 |
| Center | 1 |

Categories in P07. Source p.78 image confirms blank target-mismatch weight. First patient receives equal allocation. Thereafter, if G1>G2, assign T2 with probability p=.9; if G1=G2, probability.5; if G1<G2, probability1−p=.1. No mismatch weight is imputed.

### P16 — Missing primary outcome and follow-up

[Protocol p.52](../../../joi240006supp2_prod_1708623114.99233.pdf#page=52): seek complete follow-up, especially90-day mRS, death (mRS6), and stroke recurrence. Clinic unavailable: structured telephone interview. If clinic or telephone mRS cannot be obtained within60–120 days after randomization, multiply impute90-day mRS using an ordinal-logistic model fitted to patients with observed90-day mRS, baseline features and prior mRS scores. No imputation count, exact baseline predictor list or pooling rule appears here. Keep this60–120-day retrieval window distinct from the nominal90±15-day visit.

### P17 — Safety triggers and complete threshold tables

[Protocol pp.55–63](../../../joi240006supp2_prod_1708623114.99233.pdf#page=57): consecutive safety monitoring for early-window favorable-CT/unfavorable-perfusion patients. MM mortality increase greater than20% versus EVT prompts group enrollment halt pending DSMB (pp.55–56). The scale of this20% increase is not defined there.

Bayesian monitoring separately covers EVT core≤100cc, core>100cc, and extracranial ICA occlusion. sICH within24h, SITS-MOST, NIHSS worsening≥4: step1 checks posterior Pr(EVT sICH rate>.35 given data)>.95. If triggered, step2 checks Pr(EVT sICH rate>corresponding MM rate+.10 given data)>.95. Step2 triggers enrollment hold and DSMB meeting. Both rate priors Beta(.35,.65), center.35, effective sample size1. For≤100cc, checks at N50,100,150,200,250; EVT maximum280, expected80% in this stratum. For>100cc, first check20 then every10; expected20%=56 of280. Extracranial ICA first20 then every10; expected10%=28 of280. Threshold ranges below are inclusive. Beyond100 patients in smaller strata, recalculate with the algorithm.

| EVT N ≤100-cc stratum | sICH step1 triggering range | Mortality step1 triggering range |
|---:|---|---|
| 50 | 24–50 | 26–50 |
| 100 | 44–100 | 49–100 |
| 150 | 63–150 | 71–150 |
| 200 | 82–200 | 92–200 |
| 250 | 101–250 | 113–250 |

| EVT N in >100-cc or extracranial ICA stratum | sICH step1 range (both tables) | Mortality step1 range (both tables) |
|---:|---|---|
| 20 | 11–20 | 12–20 |
| 30 | 16–30 | 17–30 |
| 40 | 20–40 | 22–40 |
| 50 | 24–50 | 26–50 |
| 60 | 28–60 | 32–60 |
| 70 | 32–70 | 35–70 |
| 80 | 36–80 | 40–80 |
| 90 | 40–90 | 44–90 |
| 100 | 44–100 | 49–100 |

Exact locations: sICH≤100cc p.58;>100cc p.59; ICA p.60. Mortality≤100cc p.61;>100cc p.62; ICA p.63. Mortality at day90: step1 checks Pr(EVT rate>.40 given data)>.95; step2 checks Pr(EVT rate>MM rate+.10 given data)>.95. Both mortality priors Beta(.4,.6), center.4, effective size1. Same monitoring sample sizes. Step2 triggers hold and DSMB meeting. These guides do not replace DSMB independent judgment; investigators and sponsor do not receive grouped interim results (p.63).

### P18 — Rank statistic, interim/final cutoffs and printed direction

[AppendixBpp.80–81](../../../joi240006supp2_prod_1708623114.99233.pdf#page=80), direct images inspected. W_i^l is the sum of EVT Rankin-score ranks in the subgroup; J=6, Π_J overall, Π1–Π5 cumulative populations in P09. n_i^l is EVT N; n_0i^l is MM N. Printed standardized statistic:

`Z_i^l = [W_i^l − n_i^l(n_i^l+n_0i^l+1)/2] / sqrt[n_i^l n_0i^l(n_i^l+n_0i^l+1)/12]`.

Interim overall efficacy Z_J^l≥b; otherwise select a subgroup if futility Ztilde_J^l≤btilde. The tilde expression subtracts n_i^l n_0i^l theta from the numerator and uses the same denominator. Selected I-hat maximizes Z_i^l for i≠J; future accrual restricted to that group, maximumN560. Selected-group efficacy Z≥b, futility Ztilde≤btilde. Final overall stage l=3 efficacy Z_J≥c.

P.81: N560, interims200 and380, alpha.025, power.9; b=2.604, btilde=−1.897, c=2.772. Printed hypotheses: H0:P(Y≤X)=1/2; HA:P(Y≤X)=1/2+theta. theta=(Z_(1−alpha)+Z_(1−beta))/sqrt(3N)=.0791. Explicitly Y is MM Rankin score and X is EVT Rankin score. This printed direction and statistic are retained; no unstated reversed ranking or tie correction is supplied by this map.

### P19 — Disclosed amendments and historical distinction

[Protocol p.17](../../../joi240006supp2_prod_1708623114.99233.pdf#page=17) explicitly says the protocol was amended to include CTP/MRP core>100cc. Reasons: assess that population, improve generalizability, reduce dependency on perfusion selection; stringent safety monitoring. No exact amendment date or former cap appears in that paragraph. ASPECTS≤2 and edema exclusions remain, with no perfusion-volume maximum (pp.17–18,56).

[Protocol p.42](../../../joi240006supp2_prod_1708623114.99233.pdf#page=42) explicitly describes adding365-day follow-up. Earlier enrollees receive supplemental verbal or written consent remotely or in person. No amendment date is supplied there. SELECT, MR CLEAN and other prior-trial values in background are historical; this protocol does not report actual SELECT2 outcome or enrollment counts.

### P20 — Historical background values, figures and matching exclusions

These are mapped for complete opening but are historical rationale, not current SELECT2 reported results or current-trial primary effect estimates. Exact printed background transcription for all pages is preserved in the appendix below. Key quantities by location:

- pp.11–12:previousRCTearly0–6h/lateupto24h;ASPECTS≥6;core50–70ccrestriction;EXTENDIA70patients,core<70cc,mismatch>1.2and>10cc;DEFUSE3ratio≥1.8,volume≥15cc;DAWNmedian8(IQR2–18)cc,DEFUSE3 9(2–25)cc.
- p.13 SELECT: unfavorable one/both profiles about one-quarter; independence EVT 30% vs MM 13%, adjusted OR 2.92 (1.00–7.91), P=.041; ordinal adjusted OR 2.01 (1.00–4.03), P=.049. Source Figure 1 visually confirmed mRS 0–6 percentages: EVT N=62, values 8,6,16,10,24,6,29%; MM N=43, values 2,2,9,16,16,12,42%.
- p.14SELECTsICH7%vs13%,P=.26;mortality29%vs42%,P=.17. MRCLEANcore>70ccmRS0–2 8%vs0%,mortality38%vs33%;ASPECTS0–4independence9%vs0%,mortality36%vs42%;ASPECTS5–7independence32%vs13%,mortality24%vs26%. RetrospectiveASPECTS<7versus≥7mRS0–2 37%vs47%,P=.8;sICH9%vs9%,P=1;mortality20%vs22%,P=.8. MatchedcohortordinalOR2.56(2.50–8.47),P=.04 as printed.
- p.15matchedcohortindependence25%vs0%,P=.04;infarctmean(SD)87(77)vs242(120)mL,P<.001;PH2P>.99,hemicraniectomyP=.10,mortalityP=.75. Meta-analysis>1700patients/6RCT,core≥70ccindependence8%vs0%.
- p.16historicalmeta-analysis sICH0%vs12%,P=.24. SELECTASPECTS≥6core<50versus50–100:independence101/173(58%)vs6/18(33%);sICH8/173(5%)vs3/18(17%),P=.072;worsening14/173(8%)vs5/18(28%),P=.023;mortality15/173(9%)vs7/18(39%),P=.001. DEFUSE3 18/182core50–70cc.
- pp.17–18 prior 7-RCT meta-analysis: core up to 125 cc, NNT<10 for most outcomes and <5 for any improvement. Figure 2 visually confirmed ASPECTS 0–2 EVT N=0, MM N=7 (mRS 4=29%,5=29%,6=43%, preceding categories absent/zero). ASPECTS 3–5 mRS0–6: EVT N=37, 5,3,27,11,30,8,16%; MM N=27, 4,4,15,26,7,7,37%.
- p.21Figure3visuallyread:goodCT/goodCTP81%,goodmRS90d59%;poorCT/goodCTP8%,48%;goodCT/poorCTP7%,32%;poorCT/poorCTP4%,20%. These are prior SELECT core-lab profile data. p.22 uses48/32%for15%prospectivemargin(P03).
- p.24historicalRAPIDlocal/core-labmismatchagreement97%,kappa.92(CI.83–1.0);automatedASPECTSkappa.896vshuman.574/.556;RAPIDprocessing5min,2013clearance.
- p.25historicalextracranialICAcountsESCAPE40(12.7%),REVASCAT31(10.3%). Currentprotocoleligibility/rationaleisdistinctfromthesepriorcounts.

### P21 — Administrative and no-applicable material

All administrative pages were opened. Pages2–4: signatures and personnel. Pages31–32: remote consent, including15–20-minute follow-up call. Pages43–44: site monitoring, minimum100 thrombectomies per year, review every6 months. Pages52–53: feasibility30 centers,150–200 procedures per site annually,20% eligible, about30 eligible per site annually,50% consenting,560 target in nearly2 years; year1 initiation,year2 accrual,year3 primary analysis,year4 one-year follow-up. Pages53–54: CT risk context7–10mSv, US annual620millirem=6.2mSv, major contrast reaction about1/170000; these are not SELECT2 denominators. Pages65–66: data management, freezing and audit. Page67: semiannual DSMB, maximum12 months between reviews. Pages72–75: references. No supplied workbook/CSV/Office cell material in this PDF. Relevant decision rules are separately in P17.

### P22 — Graphical study design and imaging analyses

[Protocol p.71](../../../joi240006supp2_prod_1708623114.99233.pdf#page=71) directly rendered and inspected because native text only retains its heading. Eligibility: ICA/M1,within24h,baseline mRS0–1,NIHSS≥6,CT/CTA/perfusion. Exclude ASPECTS≥6 AND core<50cc, or ASPECTS≤2. Unfavorable ASPECTS3–5 OR core≥50cc. Randomize EVT+MM versus MM only.

Graphic groups: Group1 ASPECTS6–10,core≥50cc (favorable CT/unfavorable perfusion); Group2 ASPECTS3–5,core<50cc (unfavorable CT/favorable perfusion); Group3 ASPECTS3–5,core≥50cc (unfavorable both). Diagram numbering is retained separately from enrichment-group numbering in P09.

All three graphic imaging analyses: (1) EVT good-outcome rate Group2 different from Group1,15% margin; (2) treatment-effect heterogeneity between Groups2 and1; (3) EVT superior to MM in favorable-CT/unfavorable-CTP patients. Both randomized arms contribute to the imaging algorithm; line1 explicitly uses EVT patients. Matching keys: imaging discordance, subgroup interaction, good-outcome margin.

## Mapping limitations and missing definitions

No scientific coverage gaps remain. Protocol alone does not supply: target-mismatch minimization weight (blank cell); full algebra/denominator of DWI-minus-Tmax reperfusion percentage; imputation count,pooling rule,and exact baseline predictor list; dates of embedded>100cc and365-day amendments; rank/tie conventions beyond printed Appendix B; absolute/relative scale of the early-window20% mortality trigger. These are extraction limitations, not findings. Other independently assigned supplied SAPs may provide definitions. Historical Figure1/2 labels were visually confirmed with fresh direct-source renders, resolving concatenated native text.

## Complete source-linked native/layout transcription appendix

The following source-matched reusable page transcription is retained verbatim as a locator for every numeric token, footnote, reference and administrative item in all82pages. It is not treated as final visual authority; p.21/p.71graphiccontent and p.78/p.80/p.81formulas were separately read above; historical Figures 1 and 2 were also confirmed from pages13 and18.

```text
--- PAGE 1 ---
              2                                                    SELECT 2 Protocol
                                                                   4 August, 2021




                                     PROTOCOL TITLE

                                        SELECT 2:
A Randomized Controlled Trial to Optimize Patient’s Selection for Endovascular Treatment in
                                  Acute Ischemic Stroke




                                  Protocol Version Date:

                                      4 August, 2021


                              Global Principal Investigator:
                                   Amrou Sarraj, MD
                        Department of Neurology, Stroke Division
                             6431 Fannin Street, MSB 7.116
                         McGovern Mecical School at UTHealth
                                 Houston, Texas 77030




Funded by: McGovern Medical School at UTHealth at Houston through an unrestricted grant
                             from Stryker Neurovascular




                                            1

--- PAGE 2 ---
               2                                                       SELECT 2 Protocol
                                                                       4 August, 2021




                                            SELECT 2

                               AGREEMENT ON THE PROTOCOL


                                By signing below I confirm that:


   1) I have read this protocol and it contains all necessary details for conducting this study

   AND

   2) I agree to conduct the trial in compliance with this protocol and to adhere to all
      regulations that govern the conduct of the study.


________________________________________________________                   ________________
Principal Investigator’s Signature                                         Date


________________________________________________________
Principal Investigator’s Name


_________________________________________________________
Site Name




                                                2

--- PAGE 3 ---
                2                                                      SELECT 2 Protocol
                                                                       4 August, 2021



   SELECT 2 Steering Committee

Dr. Gregory Albers, Professor, Stanford University, Palo Alto, CA
Dr. Ameer Hassan, Associate Professor, The University of Texas Health Science Center – San
Antonio, Harlingen, TX
Dr. M. Shazam Hussain, Director, Stroke Program, Cleveland Clinic, Cleveland, OH
Dr. Michael Chen, Associate Professor, Rush University, Chicago, IL
Dr. Michael Abraham, Associate Professor, Kansas University Medical Center, Kansas City, MO
Dr. Maarten Lansberg, Associate Professor, Stanford University, Palo Alto, CA
Dr. Marc Ribo, Assistant Professor, Hospital Vall d'Hebron, Barcelona, Spain

Dr. Vitor Pereira, Associate Professor, Toronto General Hospital & University Network, Toronto,
Canada
Dr. Santiago Ortega-Gutierrez, Assistant Professor, The University of Iowa, Iowa City, IA
Dr. Bruce Campbell, Professor, The University of Melbourne, Melbourne, Australia

   SELECT 2 Neurointerventional Committee

Dr. Ameer Hassan, Associate Professor, The University of Texas Health Science Center – San
Antonio, Harlingen, TX
Dr. Michael Chen, Associate Professor, Rush University, Chicago, IL
Dr. Michael Abraham, Associate Professor, Kansas University Medical Center, Kansas City, MO
Dr. Vitor Pereira, Associate Professor, Toronto General Hospital, Toronto, Canada
Dr. Marc Ribo, Associate Professor, Hospital Vall d'Hebron, Barcelona, Spain
Dr. Peng R. Chen, Associate Professor, McGovern Medical School at UTHealth, Houston, TX
Dr. Santiago Ortega-Gutierrez, Assistant Professor, The University of Iowa, Iowa City, IA

   SELECT 2 Imaging Core Lab

Dr. Clark Sitton, Associate Professor, McGovern Medical School at UTHealth, Houston, TX
Dr. Roy Riascos, Professor, McGovern Medical School at UTHealth, Houston, TX

                                                3

--- PAGE 4 ---
                2                                                       SELECT 2 Protocol
                                                                        4 August, 2021

   SELECT 2 Statistical Committee

Dr. Phillip Lavori, Professor (Emeritus), Biomedical Data Science, Stanford University, Palo Alto,
CA

Dr. Chunyan Cai, Assistant Professor, Clinical and Translational Sciences, McGovern Medical
School at UTHealth, Houston, TX

   SELECT 2 Data Safety Monitoring Board

Chair: Dr. Lawrence R. Wechsler, Professor & Chair, The University of Pittsburgh School of
medicine, Pittsburgh, PA
Co-chair: Dr. Stephen Davis, The University of Melbourne, Melbourne, Australia

Statistician: Dr. Scott Hamilton, Associate Professor, Stanford University School of Medicine,
Palo Alto, CA
Voting Member: Dr. Thanh Nguyen, Associate Professor, Boston University School of Medicine,
Boston, MA
Voting Member: Dr. Johanna Fifi, Associate Professor, Mount Sinai Health System, New York
City, NY




                                                 4

--- PAGE 5 ---
                            2                                                                                                   SELECT 2 Protocol
                                                                                                                                4 August, 2021

Table of Contents
SELECT 2 Steering Committee .......................................................................................................................................3
SELECT 2 Neurointerventional Committee ....................................................................................................................3
SELECT 2 Imaging Core Lab ............................................................................................................................................3
SELECT 2 Statistical Committee .....................................................................................................................................4
SELECT 2 Data Safety Monitoring Board ........................................................................................................................4
Protocol Synopsis...........................................................................................................................................................7
             Scientific Background ....................................................................................................................................11
                Thrombectomy in Patients with Unfavorable Imaging Profiles (i.e. Large Core) ....................... 12
           Rationale for randomization in patients with favorable CT profile (ASPECTS 6-10) and
    unfavorable perfusion imaging profile (CTP: rCBF <30% volume or MRP: ADC <620 ≥50cc)................. 15
          Rationale for including patients with very large core on advanced perfusion (CTP: rCBF (<30%)
    volume or MRP: ADC < 620 >100cc) ....................................................................................................... 17
                Rationale for excluding patients with very large core on CT (ASPECTS 0-2)............................... 18
                Imaging selection for thrombectomy ......................................................................................... 19
           Thrombectomy efficacy and safety in patients with favorable CT but unfavorable perfusion
    imaging profile ........................................................................................................................................ 23
                Rationale and use of iSchemaView RAPID and iSchemaView RAPID ASPECTS ........................... 23
                Rationale for including patients with exctracranial ICA occlusion:............................................. 24
             Study Question, Aim, and Hypothesis ...........................................................................................................25
             Methods ........................................................................................................................................................26
                Study Design................................................................................................................................ 26
                Enrollment Inclusion and Exclusion Criteria ............................................................................... 28
    Table 1. The SELECT 2 study inclusion and exclusion criteria ................................................................. 28
    3.2.1.1.            Specific Neuroimaging Inclusion Criteria ............................................................................ 29
    3.2.1.2.            Specific Neuroimaging Exclusion Criteria............................................................................ 29
                Enrollment and Randomization .................................................................................................. 30
                Remote consent procedure: ....................................................................................................... 30
                Endovascular Thrombectomy ..................................................................................................... 35
                Medical Management ................................................................................................................. 36
                Outcome Measures..................................................................................................................... 37
    3.7.1.1.            Primary Outcome ................................................................................................................ 37
    3.7.1.2.            Secondary Outcomes .......................................................................................................... 37


                                                                                      5

--- PAGE 6 ---
                            2                                                                                                    SELECT 2 Protocol
                                                                                                                                 4 August, 2021

    3.7.1.3.            Imaging Outcomes .............................................................................................................. 38
                Clinical and Imaging Evaluations .............................................................................................. 38
                Table 2. Schedule of Events ........................................................................................................ 40
                    Assessment and Follow-up Visits ......................................................................................... 41
             Sources of Materials ....................................................................................................................................42
             Site Approval and Monitoring Plan.............................................................................................................43
             Sample Size Calculation and Statistical Analysis Plan ...............................................................................44
                Sample Size justification, Adaptive Enrichment Design, and Statistical Analysis Plan ............... 44
                Statistical plan for the second aim ........................................................................................... 51
                Poolability analysis across centers ........................................................................................... 51
                Feasibility of enrollment ........................................................................................................... 52
                Missing Data/Lost to Follow-up (LTFU) ....................................................................................... 52
             SELECT 2 Timetable .......................................................................................................................................53
             Risk Analysis ..................................................................................................................................................53
             Methods to mitigate risks to subjects in the trial..........................................................................................55
             Stopping rules or safety triggers for the study ..............................................................................................56
             Imaging Core Lab ...........................................................................................................................................64
             National Data Management Center ..............................................................................................................65
             Data Management Plan .................................................................................................................................65
             Compliant Handling Plan ...............................................................................................................................66
             Data Safety and Monitoring Board................................................................................................................66
             Independent Medical Safety Monitor ...........................................................................................................67
             Adverse Event Reporting ...............................................................................................................................68
             Reporting Procedures for All Adverse Events................................................................................................69
             Study Design ..................................................................................................................................................71
References ...................................................................................................................................................................72
Appendix A: Minimization Randomization Algorithm .................................................................................................76
Appendix B. Efficacy and futility bounds for interim and final analysis.......................................................................80
Appendix C. List of Approved Devices to be used in the SELECT2 Protocol: ...............................................................82




                                                                                       6

--- PAGE 7 ---
               2                                                       SELECT 2 Protocol
                                                                       4 August, 2021

Protocol Synopsis


                                           SELECT 2:
A Randomized Controlled Trial to Optimize Patient’s Selection for Endovascular Treatment in Acute
                                        Ischemic Stroke
Aims          To evaluate in acute ischemic stroke patients due to a large vessel occlusion in the
              anterior circulation (MCA M1 and ICA):

                   x   If thrombectomy, as compared to medical management, will be efficacious and
                       safe in patients with large core on either CT (ASPECTS: 3-5) or advanced
                       perfusion imaging ([rCBF<30%] on CTP or [ADC<620] on MRI: ≥50cc), treated
                       within 0-24 hours from last known well.

                   x   Second aim: to look at the correlation of imaging profiles with thrombectomy
                       clinical outcomes and treatment effect. This will be evaluated by comparing the
                       outcomes in patients with discordant imaging profile and assessing if
                       thrombectomy outcome rates and treatment effect will differ in patients with
                       discordant imaging profiles (favorable CT/unfavorable perfusion imaging and
                       unfavorable CT/favorable perfusion imaging)

                       a. Evaluate good clinical outcome (90-day mRS 0-2) rates in patients with
                          discordant imaging profile (unfavorable CT/favorable perfusion imaging vs
                          favorable CT/unfavorable perfusion imaging) treated with thrombectomy.

                       b. Evaluate the heterogeneity of thrombectomy treatment effect in patients
                          with favorable CT/unfavorable perfusion and unfavorable CT/favorable
                          perfusion imaging.
Study Design    A prospective, randomized, international, multicenter, assessor-blinded controlled
                trial
Study Sites     Up to 40 total sites, up to 30 US sites
General          1. Adults (18-85 years) with the final diagnosis of an acute ischemic stroke
Inclusion        2. NIHSS ≥ 6
Criteria         3. Last known well to groin puncture or medical management between 0 to 24
                      hours
                 4. Pre-stroke modified Rankin Scale score (mRS) of 0-1
                 5. Eligible for thrombectomy or medical management
                 6. Signed Informed Consent obtained
                 7. Subject willing to comply with the protocol follow-up requirements
                 8. Anticipated life expectancy of at least 3 months



                                                7

--- PAGE 8 ---
            2                                                   SELECT 2 Protocol
                                                                4 August, 2021

General      1. Inability to undergo CT angiography and/or CT perfusion imaging (e.g., renal
Exclusion        insufficiency, iodine/contrast allergy)
Criteria     2. Co-morbid psychiatric or medical illnesses that would confound the
                 neurological assessments
             3. Treatment with IV thrombolytic therapy beyond 4.5 hours from last known well
             4. Treated with IV thrombolytic therapy 3-4.5 hours 3-4.5 hours after last known
                 well AND any of the following:
                 1) age >80,
                 2) current anticoagulant use,
                 3) history of diabetes AND prior stroke,
                 4) NIHSS >25,
                 5) ischemic involvement of > 1/3 MCA territory
             5. Current participation in another investigational drug or device study.
Imaging     1. Proven large vessel occlusion in ICA or MCA-M1 occlusion (carotid occlusions
Inclusion       can be cervical or intracranial, with or without tandem MCA lesions) determined
Criteria        by MRA or CTA
            2. Large infarct-core lesion on at least one of the following
                2.1. Non-Contrast CT (ASPECTS of 3-5),
                2.2. CT perfusion (rCBF<30% ≥50cc),
                2.3. MRI-DWI (ADC<620 ≥50cc)
Imaging     1. Patients who have both ASPECTS of 6-10 on non-contrast CT AND core volume
Exclusion       <50 cc on perfusion imaging
Criteria    2. Patients with very large core on non-contrast CT i.e. ASPECTS ≤ 2
            3. Evidence of intracranial tumor (except small meningioma), acute intracranial
                hemorrhage, neoplasm, or arteriovenous malformation
            4. A significant mass effect with midline shift
            5. Evidence of internal carotid artery dissection that is flow limiting or aortic
                dissection
            6. Intracranial stent implanted in the same vascular territory that precludes the
                safe deployment/removal of the neurothrombectomy device
            7. Acute symptomatic arterial occlusions in more than one vascular territory
                confirmed on CTA/MRA (e.g., bilateral MCA occlusions, or an MCA and a basilar
                artery occlusion).
            8. Signs of established infarct and large area of cerebral edema on non-contrast CT
Primary      1. Modified Rankin Scale (mRS) at 90 (+/- 15) days. The primary outcome is a shift
Outcome           on 90-day mRS. 2nd primary outcome is favorable clinical outcomes: mRS score
                  of 0-2.
Secondary    1. Safety measured by the incidence of symptomatic intracranial hemorrhage
Outcomes         (sICH per SITS-MOST), mortality and groin (or arterial access site) hematomas,
                 infections or any vascular injury caused by the endovascular procedure
             2. Rates of recanalization (complete and partial) using the modified TICI system
                 (score ≥ 2b defined as favorable reperfusion)

                                          8

--- PAGE 9 ---
                2                                                    SELECT 2 Protocol
                                                                     4 August, 2021

                    3.
                     Length of hospital stay
                    4.
                     Discharge location
                    5.
                     NIHSS
                    6.
                     Neuro-QoL
Imaging             1.
                     Infarct volume on MRI DWI sequence (or CT if MRI not feasible) 24 hours to 7
Outcomes             days after randomization
                 2. Lesion growth between the RAPID identified ischemic core on baseline imaging
                     and the infarct volume
                 3. Successful reperfusion defined as DWI lesion volume minus Tmax>6 seconds
                     greater than 50%
                 4. Recanalization of the primary arterial occlusive lesion, assessed by a modified
                     Thrombolysis in Cerebral Infarction scores of 2b (50% to 75% reperfusion), 2c
                     (>75% to 99% reperfusion) or 3 (complete reperfusion).
Imaging          1. CT images will be read by the appropriately trained clinicians as well as by the
Assessments          iSchemaView automated ASPECTS. ASPECTS for patient selection will be
                     determined independently by the clinicians prior to any assessment with
                     automated ASPECTS. In cases where there is disagreement, the physician
                     reading will override the automated software reading.
                 2. CTP images with mismatch determination will be read by iSchemaView
                     automated RAPID software.
                 3. All the images will be adjudicated by a blinded core lab at McGovern Medical
                     School at UTHealth.
Randomization   Randomization will be done in the emergency room using a web-based dynamic
                randomization system. Covariate adaptive randomization will be conducted to
                balance the distribution of the randomization by age (<60, 60-69, 70-79, 80-85 years
                old), presentation NIHSS (6-9, 10-15, 16-20, >20), center, clot location (M1, ICA),
                treatment time window (0-8, 9-16, 17-24 hours from onset to randomization time),
                CTP/MRP core volume (<50cc, 50-100cc, >100cc), presence or absence of target
                mismatch profile (mismatch ratio ≥ 1.8 & mismatch volume ≥ 15 cc) and
                hemisphere (right, left).

                The randomization algorithm we are going to implement is the algorithm developed
                by Pocock and Simon (1975), i.e., minimization method. Through this algorithm, the
                assignment of a new patient to a treatment group is determined so as to minimize
                the differences between the groups in terms of these important key baseline
                variables. Unlike traditional stratified randomization, the minimization method
                works toward minimizing the total imbalance for all factors together instead of
                considering mutually exclusive subgroups, that is, we will not be creating these
                mutually exclusive subgroups during the randomization. Therefore, this approach is
                not restricted by the number of variables and the possible combinations of levels of
                balancing factors.


                                              9

--- PAGE 10 ---
                2                                                    SELECT 2 Protocol
                                                                     4 August, 2021

                Patients with large core on either CT (ASPECTS 3-5) or perfusion imaging (CTP:
                rCBF<30% or MRP: ADC<620 ≥50cc) or both within 0-24 hrs from last known well
                will be randomized into thrombectomy plus medical management vs medical
                management alone.
Interventions   Endovascular Thrombectomy: Patients randomized to endovascular thrombectomy,
                will be treated with thrombectomy stent-retrievers and/or aspiration devices
                currently cleared by the FDA. The choice of thrombectomy method, primary
                approach/technique, whether primary aspiration or primary stent-retriever with or
                without aspiration, will be left up to the interventionalist, with any of the FDA-
                approved devices approved in the study protocol or a combination of them
                (Appendix C). Standard medical therapy, based on current AHA guidelines, will also
                be provided for all patients.

                Medical Management: Patients randomized to medical management only will
                receive standard medical therapy based on current AHA guidelines. Patients will
                receive IV thrombolytic therapy available for use according to practice guidelinesif
                presented within the first 3 hours from last known well and meeting other FDA label
                criteria, or up to 4.5 hours from last-seen-normal and meeting other AHA guidelines.
                No procedures or tests required by the protocol will delay fastest possible delivery
                of thrombolytic therapy to potentially eligible subjects. For thrombolysis treated
                patients, the sites’ post-thrombolysis protocol will be followed. The non-
                thrombolysis treated patients will be treated with aspirin, 325 mg on Day 1, and 81-
                325 mg/day (investigator’s preference) on day 2-5, unless an indication for early
                anticoagulation is present (as determined by the patient’s attending physician). All
                patients will receive standard DVT prevention therapy.
Assessment      Clinical assessments will be done at baseline, 24-hours after randomization,
and Visits      day 5-7 or hospital discharge (whichever is earlier), 30 days, and 90 days:

                    1. Baseline: demographics and medical history, CT/CTA/CTP/MRP imaging,
                       lab work, hourly blood pressure, NIHSS, mRS
                    2. 24 hours (+/- 6 hrs): hourly blood pressure, NIHSS
                    3. 24 hour – 7 days post-procedure imaging (MRI or CT if MRI not feasible)
                    4. Day 5-7 or discharge (whichever is earlier): NIHSS, mRS
                    5. Day 30 (+/- 15 days): mRS
                    6. Day 90 (+/- 15 days): mRS, Neuro-QoL




                                             10

--- PAGE 11 ---
                2                                                       SELECT 2 Protocol
                                                                        4 August, 2021

Protocol

   Scientific Background

Endovascular thrombectomy efficacy and safety was established initially up to 6 hours from
stroke onset (the early time window) from several randomized controlled trials (MR CLEAN 1,
REVASCAT2, ESCAPE3, SWIFT PRIME4, and EXTEND-IA5). These trials’ inclusion criteria focused
only on patients with favorable imaging profiles (minimal ischemic changes) on CT defined as
ASPECTS ≥ 6 and on perfusion imaging defined as small core infarct with a large area of
mismatch. Later, two trials (DAWN6 and DEFUSE 37) extended the safety and efficacy up to 24
hours (the late time window). The late window trials utilized advanced perfusion images with
the same criteria of small core infarct and a large area of mismatch. As a result, these inclusion
criteria excluded patients with unfavorable imaging profiles (significant ischemic changes),
including patients with ASPECTS <6 or core infarct volume > 50-70 cc. Thus, thrombectomy
efficacy and safety in these patients with unfavorable profiles (large core) on imaging is not
established.


Moreover, the different trials used different imaging modalities for including or excluding
patients, simple imaging with non-contrast CT head (ASPECTS ≥ 6) and/or advanced perfusion
imaging with small infarct core and mismatch, with the vast majority of the patients having
favorable imaging profile on at least one modality (CT and/or perfusion imaging). Thus:


   1. The correlation between the different imaging profiles and thrombectomy outcomes is
       not established and the optimal imaging selection prior to thrombectomy is unknown.
   2. Many patients were not represented in the trials, especially those with discordance
       between the two imaging modalities.




                                                11

--- PAGE 12 ---
                2                                                       SELECT 2 Protocol
                                                                        4 August, 2021

                Thrombectomy in Patients with Unfavorable Imaging Profiles (i.e. Large Core)


Endovascular thrombectomy is safe and efficacious in selected patients with acute ischemic
strokes (AIS) due to large vessel occlusion (LVO) in the anterior circulation up to 24 hours after
the stroke onset. The majority of the early window trials used simple imaging with CT with
ASPECTS ≥ 6 as inclusion criteria2-4. EXTEND-IA5 was the only early window trial that solely used
perfusion imaging criteria (core infarct volume < 70cc with a mismatch ratio of > 1.2 &
mismatch volume > 10 cc). The trial only enrolled 70 patients. Most of the SWIFT PRIME 4
patients were included based on perfusion imaging with limited infarct core but some were
included based only ASPECTS ≥ 6. Only the Multicenter Randomized Clinical Trial of
Endovascular Treatment for Acute Ischemic Stroke in the Netherlands (MR CLEAN) trial included
a limited number of patients with an ASPECTS < 6. Based on the results of these trials, the
American Heart Association recommended the use of thrombectomy in patients with large
vessel occlusions presenting with CT ASPECTS ≥ 6 in the early treatment window (0-6 hours) 8.


Both the trials assessing thrombectomy safety and efficacy in the late time window used
perfusion imaging. The DAWN 6 only included core infarct volume of up to > 50 cc on perfusion
images and the trial excluded patients with involvement of >1/3 rd of MCA territory on simple
CT. The DEFUSE 37 trial excluded patients with ASPECTS < 6 or ischemic core volume ≥ 70 cc and
required a mismatch ratio of ≥ 1.8 and mismatch volume of ≥ 15 cc. As a result, the safety and
efficacy of late window thrombectomy is only established in patients with a small core, CT
ASPECTS ≥ 6 and an infarct core < 50 cc on perfusion imaging. In fact, most of the patients in
the late window trials had very small infarct core, with median (IQR) core infarct volume of 8 (2-
18) cc in the DAWN6 trial and 9 (2-25) cc in DEFUSE 37.


Despite the lack of data on patients with low ASPECTS, the American Heart Association has
concluded that thrombectomy may be reasonable in patients with CT ASPECTS< 6 presenting
within 6 hours of symptom onset while suggesting the need for additional randomized trial


                                                12

--- PAGE 13 ---
                2                                                           SELECT 2 Protocol
                                                                            4 August, 2021

data8. This population of patients represents a good portion of the patients encountered in
daily practice without strong evidence from randomized trials to support treatment decision.


Data from a few prospective and retrospective non-randomized studies reported reasonable
rates of good clinical and safety outcomes after thrombectomy in patients with unfavorable
imaging profiles. In our recently concluded ‘Optimizing Patient Selection for Endovascular
Treatment in Acute Ischemic Stroke (SELECT): A Prospective Multicenter Cohort Study of
Imaging Selection’, investigators were allowed to enroll patients with unfavorable imaging
profiles/large core on either CT or advanced perfusion imaging or both. The treatment decision
in these patients, thrombectomy vs. medical management, was not randomized and rather
based on the discretion of the site investigators. The study found that patients with unfavorable
imaging profile on either or both imaging modalities formed a significant proportion of the daily
clinical practice with up to 1/4th of patients demonstrating significant ischemic changes on one
or both imaging modalities. In SELECT, thrombectomy was associated with improved functional
independence in patients with an unfavorable profile on one or both imaging modalities (EVT:
30% vs MM: 13%, Adjusted OR: 2.92, 95%CI=1.00-7.91, p=0.041). Thrombectomy was also
associated with a significant shift towards better outcomes across the full distribution of
modified Rankin Scale scores (adjusted OR: 2.01, 95%CI=1.00-4.03, p=0.049). (Figure 1).


                                                                                                      mRS=0
        THROMBECTOMY (N=62)       8    6    16        10       24       6           29                mRS=1
                                                                                                      mRS=2
                                                                                                      mRS=3
                                                                                                      mRS=4
 MEDICAL MANAGEMENT (N=43)      22 9        16        16      12               42
                                                                                                      mRS=5
                                                                                                      mRS=6
                               0% 10% 20% 30% 40% 50% 60% 70% 80% 90% 100%

 Figure 1. Modified Rankin Scale (mRS) distribution bars representing 90day clinical outcomes in
 patients with unfavorable profile on one or both imaging modalities, stratified by thrombectomy vs
 medical management only.



                                                 13

--- PAGE 14 ---
                2                                                       SELECT 2 Protocol
                                                                        4 August, 2021



For safety outcomes, symptomatic intracranial hemorrhages rates (EVT: 7% vs MM only: 13%,
p=0.26) and mortality (EVT: 29% vs MM only: 42%, p=0.17) did not statistically differ between
thrombectomy and medical management only arms.


In a post-hoc analysis of the Multicenter Randomized Clinical Trial of Endovascular Treatment
for Acute Ischemic Stroke in The Netherlands (MR CLEAN), the investigators compared the rates
of good outcome in patients with CTP ischemic core volume>70 cc, who received
thrombectomy or medical management. The rate of good outcome (mRS 0-2) was 8% in the
thrombectomy vs 0% in the medical management group. The rate of mortality was 38% versus
33%, respectively10. In another secondary analysis of MR CLEAN trial, thrombectomy patients
with ASPECTS 0-4 had 9% rate of good outcome (mRS=0-2), compared to 0% in medical therapy
patients. Mortality rate was lower in the thrombectomy group (36% vs 42%). Similarly, in
patients with ASPECTS 5-7, thrombectomy patients had 32% good outcome versus 13% in
medical management patients with a slightly lower mortality rate (24% vs 26%, respectively) 11.


In a retrospective multicenter study12, the outcome rates in patients who received
thrombectomy were compared between those with CT ASPECTS<7 versus those with CT
ASPECTS≥7. The study showed similar outcomes between thrombectomy patients with
unfavorable and favorable CT profiles. There was no statistically significant difference in good
clinical outcome mRS 0-2 (ASPECTS<7=37% vs ASPECTS≥7=47%, p=0.8), symptomatic
intracerebral hemorrhage (9% vs 9%, p=1.0), or mortality (20% vs 22%, p=0.8).


Rebello et al. (2017) compared the outcomes of patients with unfavorable CTP profile [rCBF
<30%] >50 cc who underwent thrombectomy versus matched controls who had medical
management only13. The results showed that compared to medical management,
thrombectomy was statistically associated with favorable shift in the distribution of 90-day
modified Rankin scale (mRS) (odds ratio: 2.56; 95%CI: 2.50-8.47; p=0.04), higher rates of good


                                                14

--- PAGE 15 ---
                2                                                      SELECT 2 Protocol
                                                                       4 August, 2021

clinical outcome (mRS=0-2) (thrombectomy=25% vs medical therapy=0%; p=0.04), as well as
smaller infarct volumes (mean [SD], thrombectomy=87 [77] vs medical therapy=242 [120] mL;
p<0.001). There were no statistically significant differences between the groups for safety
outcomes including parenchymal hematoma type 2 (p>0.99), hemicraniectomy (p=0.10), and
90-day mortality (p=0.75).


These contrasting results with some reporting a potential signal for benefit and others
reporting no difference in good outcome rates between thrombectomy and medical
management alone, along with the lack of higher level of evidence from randomized trials
support the need for randomized trials to test the efficacy and safety of thrombectomy in
patients with unfavorable imaging profiles. The current status of inadequate evidence results in
different treatment approaches in patients with unfavorable imaging profiles, with some
patients being treated with thrombectomy while the majority receiving medical management
only.


We hypothesize that endovascular thrombectomy is safe and efficacious in patients with acute
ischemic strokes due to large vessel occlusion in the anterior circulation (ICA, MCA/M1) with
large ischemic lesion volumes on simple (non-contrast CT head) or advanced perfusion imaging
(CT or MRI perfusion) as compared to medical management only up to 24 hours.


               Rationale for randomization in patients with favorable CT profile (ASPECTS 6-
               10) and unfavorable perfusion imaging profile (CTP: rCBF <30% volume or
               MRP: ADC <620 ≥50cc)
Most of the early window (0-6 hours) trials limited the use of perfusion imaging for patient
selection. Only SWIFT PRIME4 and EXTEND – IA5 used perfusion imaging to exclude patients
with the larger ischemic core (> 50-70 cc). Recently a patient-level meta-analysis of early
window trials examining the impact of perfusion imaging parameters was published, including
more than 1700 patients from 6 randomized controlled trials14. The study demonstrated 8%
good outcome in patients with ischemic core volume of 70 cc or more treated with


                                               15

--- PAGE 16 ---
                2                                                        SELECT 2 Protocol
                                                                         4 August, 2021

thrombectomy compared to 0% in patients treated with medical management only. In a
univariate shift analysis, the study showed the benefit of thrombectomy, which disappeared
once adjusted for confounders. No difference in symptomatic ICH (EVT – 0%, MM – 12%,
p=0.24) was reported. Thus, true evidence of efficacy in this patient group is still lacking. The
recommendation for using only simple CT imaging for patient selection in the early window
(within 6 hours) was recently rescinded from the American Heart Association stroke guidelines 8.


In an analysis of our recently concluded SELECT trial within early window (thrombectomy within
6 hours of stroke onset), functional independence rates were 101/173 (58%) in patients with
ASPECTS score of 6 or more and with ischemic core volume of < 50cc. This rate reduced to 6/18
(33%) in patients with ASPECTS scores of 6 or more but ischemic core volume of 50-100 cc,
which approached the medical management only rates reported in early window
thrombectomy trials. The safety outcomes – symptomatic ICH (8/173 (5%) vs 3/18 (17%),
p=0.072), neurological worsening (14/173 (8%) vs 5/18 (28%), p=0.023) and mortality (15/173
(9%) vs 7/18 (39%), p=0.001) also significantly increased in the subgroup when ischemic core
volume was large. Thus, in these patients the outcomes changed significantly as the infarct core
volume increased on perfusion imaging: the good outcomes reduced in half, while the safety
outcomes doubled. With a limited representation of this subgroup in clinical trials assessing
thrombectomy in the early window, no conclusive evidence is available and there is equipoise
to justify randomization between thrombectomy and medical management alone.


In the late window, no randomized evidence exists for the efficacy of thrombectomy in these
patients. Two randomized controlled trials (DAWN6 & DEFUSE 37) assessing the efficacy and
safety of thrombectomy in the late window used both simple (CT) as well as advanced
perfusion imaging to exclude patients. The DAWN6 study only included patients with ischemic
core volume of up to 50cc, while the DEFUSE 37 trial included patients with up to 70 cc of
ischemic core volume. However, only 18 of the 182 randomized patients had ischemic core




                                                 16

--- PAGE 17 ---
                2                                                        SELECT 2 Protocol
                                                                         4 August, 2021

volume between 50-70cc. Thus, no substantial conclusion of efficacy and safety of
thrombectomy can be made within this subgroup for the late window as well.


               Rationale for including patients with very large core on advanced perfusion
               (CTP: rCBF (<30%) volume or MRP: ADC < 620 >100cc)
Limited non-randomized evidence of thrombectomy efficacy is available in the published
literature. A recently published study, a meta-analysis of 7 early window randomized controlled
trials by Campbell et al.14 has suggested benefit of thrombectomy in patients presenting with
infarct core of >100 cc. Campbell et al. demonstrated that although functional independence
rates remain very low, these patients continue to benefit from thrombectomy. For infarct core
volumes up to 125 cc, the number needed to treat for any benefit remains below 10 for most
functional outcomes and less than 5 for any functional improvement. In the light of these
recently available evidence, these patients may have a low likelihood of functional
independence but could still have better functional outcome than patients treated with medical
management only. Thus, the protocol was amended to include these patients in the study.
Stringent safety monitoring of mortality and symptomatic ICH is employed to ensure patient
safety. The amended inclusion criteria will allow for:

        1) Assessment of population with CTP/MRP core infarct >100cc
        2) More generalizability of the study findings
        3) No dependency on perfusion criteria, which will allow for the population to be
            treated based on non-contrast CT only. Providing data on the efficacy and safety of
            thrombectomy selection based on a non constrast CT, which is more readily
            available, would result in an increased thrombectomy availability to centers without
            perfusion imaging.

Although no upper limit is specified for infarct core volume measurements on CT or MR
perfusion imaging, the infarct size is still expected to be limited, to an extent, given imaging
exclusion criteria of “Patients with very large core on non-contrast CT i.e. ASPECTS ≤ 2” and



                                                 17

--- PAGE 18 ---
                2                                                              SELECT 2 Protocol
                                                                               4 August, 2021

patients with “signs of established infarct and large area of cerebral edema on non-contrast
CT”.

               Rationale for excluding patients with very large core on CT (ASPECTS 0-2)
There are no previously published data to describe the outcomes in this patient population. We
did not have any patients with ASPECTS 0-2 who received a thrombectomy in SELECT trial. The
90-day mRS distribution for patients with ASPECTS 0-2 is shown in Figure 2. Since, no data for
thrombectomy efficacy and safety is available, these patients were excluded from the trial.



                                            ASEPCTS 0-2                                              mRS=0
                                                                                                     mRS=1
                                                                                                     mRS=2
        THROMBECTOMY (N=0)        0
                                                                                                     mRS=3
                                                                                                     mRS=4
 MEDICAL MANAGEMENT (N=7)         0        29                   29               43
                                                                                                     mRS=5
                                 0%         20%            40%           60%    80%          100%    mRS=6


                                            ASPECTS 3-5                                             mRS=0
                                                                                                    mRS=1
                                                                                                    mRS=2
        THROMBECTOMY (N=37)           53         27         11            30      8     16
                                                                                                    mRS=3
                                                                                                    mRS=4
 MEDICAL MANAGEMENT (N=27)            44    15             26        7    7       37
                                                                                                    mRS=5
                                                                                                    mRS=6
                                   0%           20%         40%          60%     80%         100%



 Figure 2. Modified Rankin Scale (mRS) distribution bars representing 90day clinical outcomes in large core patients
 stratified by ASPECTS score.




                                                      18

--- PAGE 19 ---
                2                                                      SELECT 2 Protocol
                                                                       4 August, 2021

               Imaging selection for thrombectomy


Thrombectomy is a highly effective treatment for anterior circulation LVO patients based on the
results of several recent randomized clinical trials1-7. However, the imaging modalities and the
patient populations enrolled, varied between the studies. For example, the Multicenter
Randomized Clinical Trial of Endovascular Treatment for Acute Ischemic Stroke in the
Netherlands (MR CLEAN)1 used non-contrast head CT (NCCT) with the inclusion criteria of less
than one third of the MCA, while the Solitaire with the Intention for Thrombectomy as Primary
Endovascular Treatment trial (SWIFT PRIME)4 and the Randomized Trial of Revascularization
with Solitaire FR Device versus Best Medical Therapy in the Treatment of Acute Stroke Due to
Anterior Circulation Large Vessel Occlusion Presenting within Eight Hours of Symptom Onset
(REVASCAT)3, in spite of using NCCT, applied a more stringent inclusion criterion of the Alberta
Stroke Program Early CT Score (ASPECTS) of ≥ 6. Some of the patients in SWIFT PRIME 4 were
treated by CT-Perfusion/ iSchemaView RAPID (CTP/RAPID), while some in REVASCAT 3 were
treated based on MRI ASPECTS (≥ 7). Thrombectomy for Small Core and Anterior Circulation
Proximal Occlusion with Emphasis on Minimizing CT to Recanalization Times (ESCAPE) 2 used
more specific imaging criteria focusing on NCCT ASPECTS (≥ 6) and CT-Angiography collaterals,
as well as placing some consideration of the CT-Profusion profile. Extending the Time for
Thrombolysis in Emergency Neurological Deficits — Intra-Arterial trial (EXTEND-IA) 5 was the
sole early window trial that purely based imaging selection on advanced perfusion imaging
using CTP/RAPID.


This resulted in uncertainty in regards to optimal patient selection when it comes to imaging
modality prior to thrombectomy as reflected in the current AHA guidelines, and the guideline
recommending against using advanced perfusion imaging for patients presenting in early time
window was recently rescinded8.




                                               19

--- PAGE 20 ---
                2                                                      SELECT 2 Protocol
                                                                       4 August, 2021

The recent trials evaluating thrombectomy effectiveness in the late time window - Clinical
Mismatch in the Triage of Wake Up and Late Presenting Strokes Undergoing Neurointervention
With TREVO (DAWN)6 and Endovascular Therapy Following Imaging Evaluation For Ischemic
Stroke 3 (DEFUSE3)7 used advanced imaging perfusion (CTP and MR-Perfusion) utilizing the
RAPID software along with NCCT criteria to select patients. As a result, the recent AHA
guidelines also recommend the use of both CT and advanced perfusion imaging for patient
selection in thrombectomy8.


In conclusion, the optimal imaging selection modality prior to thrombectomy is still unknown.
Furthermore, the restrictive imaging inclusion criteria and correlation with outcomes, both
functional independence, and safety outcomes are still yet undetermined. To measure the
correlation between the two different imaging modalities and clinical outcomes, patients with
discordant imaging profiles should be compared.


The highest level of evidence comes from a randomized controlled trial comparing
thrombectomy outcome rates as well as safety parameters in patients selected by CT only vs CT
plus perfusion imaging. However, a randomized trial is not feasible given the level of evidence
from RCTs in the late window patients treated based on favorable perfusion imaging profiles
(DAWN6 and DEFUSE 37). Additionally, the current AHA guidelines recommend the use of
perfusion imaging for selection of patients in the late window 8.


Since the clinical trials evaluating thrombectomy largely included patients with favorable
profiles on both CT and perfusion imaging, the vast majority of the currently available data is on
these patients. Thus, the correlation between the thrombectomy outcome rates with different
imaging profiles, specifically with discordance profiles between CT and perfusion images, is not
well established. However, those patients with discordant imaging profiles on both modalities
are frequently encountered in real-world practice. There is currently no evidence from
randomized trials to guide the treatment decision in these patients. Many of these patients


                                                20

--- PAGE 21 ---
                2                                                            SELECT 2 Protocol
                                                                             4 August, 2021

may be excluded from the treatment based on the unfavorable profile on one imaging modality
as preferred by the treating center or physician. Moreover, it is unclear if a favorable profile on
advanced perfusion imaging with an unfavorable profile on non-contrast CT will provide
improved prognostic value of thrombectomy when compared to patients with unfavorable
perfusion imaging and favorable CT, or vice versa.


The SELECT trial was the first and only study to document discordance between imaging
selection profiles. In SELECT, we observed that the two imaging modalities (CT and CT
perfusion) had an agreement with favorable profiles in 81% of patients and an unfavorable
profile on both modalities in 4% of patients. Discordance between the two imaging modalities
was observed in 15% of patients with 7% showing favorable CT but unfavorable CTP and 8%
showing unfavorable CT but favorable CTP. The agreement between imaging modalities and
outcomes are shown in Figure 3.




 Figure 3. Illustration of patients’ imaging profiles, as determined by the core lab, and their outcomes. A (Favorable
 CT & Favorable CTP): High agreement between CT and CTP profiles prior to thrombectomy. Similar profile to
 patients enrolled in prior RCTs; B (Unfavorable CT & Favorable CTP): Patients who would have been excluded by CT
 but treated based on favorable CTP; C (Favorable CT & Unfavorable CTP): Patients who would have been excluded
 by CTP but qualified by favorable CT; D (Unfavorable CT & Unfavorable CTP).




                                                   21

--- PAGE 22 ---
               2                                                      SELECT 2 Protocol
                                                                      4 August, 2021

As shown above, discordance between imaging profiles was not uncommon and clinical
outcomes differed based on the presence and type of discordant imaging profiles. Patients with
discordant profiles showed outcomes better than patients with both imaging modalities
demonstrating an unfavorable profile.


The two groups where both imaging modalities (CT and perfusion imaging) agree:
    1. Unfavorable profiles on both: the results would not contribute to the comparison of
        imaging selection.
    2. Favorable profile on both: there is, as detailed, strong evidence from RCTs supporting
        thrombectomy in both early and late time windows; thus randomizing these patients to
        compare imaging selection for thrombectomy is unethical and not feasible.


In SELECT 2, in order to compare the outcomes between imaging selection modalities, we
propose to examine the correlation between the discordance in imaging profile and outcome
rates, both functional independence as well as safety outcomes. We also propose to examine if
there is a heterogeneity of treatment effect of thrombectomy in patients with discordant
imaging profile (favorable CT/unfavorable perfusion imaging and unfavorable CT/favorable
perfusion imaging).


Based on the SELECT trial results, patients with unfavorable CT/ favorable CTP had 48% good
outcomes vs favorable CT/unfavorable CTP with 32% good outcomes (16% absolute difference).
A superiority margin at 15% will be set between the two discordance groups and good outcome
rates between patients with discordant imaging profiles will be compared. If those differences
do not reach the statistical margin, then among patients with discordant imaging profile who
met the inclusion criteria for SELECT 2 and treated with thrombectomy, the outcome rates did
not differ.




                                              22

--- PAGE 23 ---
               2                                                      SELECT 2 Protocol
                                                                      4 August, 2021

In addition to comparing the rates of good outcomes between patients treated with
thrombectomy in patients with discordant profiles, thrombectomy treatment effect
heterogeneity will be assessed in patients with favorable CT/ unfavorable perfusion imaging
and those with unfavorable CT/favorable perfusion imaging. If no heterogeneity exists, then
thrombectomy benefit is not modified in the two scenarios when the two imaging modalities
disagree.


               Thrombectomy efficacy and safety in patients with favorable CT but
               unfavorable perfusion imaging profile



Early window trials demonstrated the superiority of thrombectomy over standard medical
management in patients selected by either favorable CT (ESCAPE and REVASCAT) or favorable
perfusion imaging (EXTEND-IA and a portion of SWIFT-PRIME). Thus, in patients with favorable
CT profile, thormbectomy is proven superior to standard medical management in early window.
Late window trials, DAWN6 and DEFUSE 37 proved thrombectomy efficacy and safety in patients
with favorable CT and perfusion imaging profiles. If thrombectomy is proven better than
medical management only in patients with favorable CT but unfavorable perfusion imaging,
then regardless of the perfusion imaging findings, patients with favorable CT would benefit
from thrombectomy and thus, should be treated with thrombectomy.



               Rationale and use of iSchemaView RAPID and iSchemaView RAPID ASPECTS


iSchemaView RAPID: At the conclusion of the CT/MR Perfusion scan, the technologist sends the
sequences from the console to RAPID for automated processing. The RAPID software was
developed based on data from DEFUSE 1 and was prospectively validated in DEFUSE 2. The
system provides fully automated processing of brain images. The RAPID output maps, which
identifies the volume and location of ischemic core and perfusion lesions, are emailed to


                                               23

--- PAGE 24 ---
                2                                                          SELECT 2 Protocol
                                                                           4 August, 2021

investigators (protected health information is automatically removed) and auto-sent to PACS
for viewing within 5 minutes of completion of the scan. Immediately after the images are
available, the investigator will review the results of the RAPID mismatch map, simple (Non-
contrast) CT and the CTA to determine assignment in the specified group. The accuracy of the
software for identifying the size and location of perfusion and diffusion lesions has been
established by extensive validation and testing on blood flow phantoms; the software received
FDA 510K clearance for clinical use in 2013. The agreement between local investigators and the
Imaging Core Lab for identification of the mismatch profile in DEFUSE 2 15 was 97%, κ 0·92; 95%
CI 0·83–1·0. Identification of core and penumbral volumes will be done in accordance with the
procedures followed in DAWN6 and DEFUSE 37 trials.


iSchemaView RAPID ASPECTS: Inter-rater reliability of ASPECTS score has been shown to be
fair16. In a recent study, Automated ASPECTS has been shown to have a much higher agreement
(k = 0.896) with the predefined gold standard sources (reporting of results by two board-
certified neuroradiologists) compared to human readers (k = 0.574 and k = 0.556) 17. The
automated ASPECTS score is included as an investigational tool in the study. ASPECTS for
patient selection will be determined independently by appropriately trained clinicians prior to
any assessment with automated ASPECTS. In case of disagreements, ASPECTS scores provided
by the clinicians will override the ASPECTS score by iSchemaView RAPID ASPECTS. In addition,
the use of perfusion imaging in all patients will also help verify if a large core is present in these
patients.


                Rationale for including patients with exctracranial ICA occlusion:


Patients with extracranial ICA occlusion, as of now, do not have a proven treatment for
revascularization and the rates of recanalization achieved by the only currently FDA approved
treatment, IV tissue plasminogen activator have been poor 18-19. Another issue with these
patients is the potential of so called “Psuedoextracranial occlusion.” In a significant proportion


                                                  24

--- PAGE 25 ---
                2                                                      SELECT 2 Protocol
                                                                       4 August, 2021

of cases with intracranial ICA occlusion, because of low flow, the contrast used for obtaining CT
angiogram does not reach the level of occlusion and thus the occlusion appears to be
extracranial on the conventional CT angiogram 20. The only way to confirm the diagnosis of
psuedoextracranial occlusion is to obtain an angiogram using fluoroscopy in the angio suite.
Such cases form a significant number of patients presenting with extracranial occlusion who
may benefit from the thrombectomy procedure, but are excluded from the trial based on the
appearance on CT angiogram. Including cases with extracranial ICA occlusion on CTA will allow
for enrollment of these patients. Randomized controlled trials such as ESCAPE and REVASCAT
reported 40 (12.7%) and 31 (10.3%) patients with extracranial ICA occlusions. EXTEND-IA in
early window and DEFUSE 3 in late time window also allowed for inclusion of patients with
extracranial ICA, though did not report the number of patients enrolled with extracranial ICA.

   Study Question, Aim, and Hypothesis

Study aims: are to evaluate in acute ischemic stroke patients due to a large vessel occlusion in
the anterior circulation (MCA M1 and ICA):

   x   Primary aim: If thrombectomy plus medical management as compared to medical
       management alone will be efficacious and safe in patients with large core on either CT
       (ASPECTS 3-5) or perfusion imaging (CTP: rCBF<30% or MRP: ADC <620 ≥50cc), treated
       within 0-24 hours from last known well. We hypothesize that patients with unfavorable
       profiles (large core) treated with thrombectomy on either imaging modality will have
       significantly better outcomes than large core patients treated with medical
       management only.


   x   Second aim: The second aim is to look at the correlation of imaging profiles with
       thrombectomy clinical outcomes and treatment effect. It will be evaluated by
       comparing the outcomes in patients with discordant imaging profile and assessing if
       thrombectomy outcome rates and treatment effect will differ in patients with



                                               25

--- PAGE 26 ---
                2                                                       SELECT 2 Protocol
                                                                        4 August, 2021

       discordant imaging profiles (favorable CT/unfavorable perfusion imaging and
       unfavorable CT/favorable perfusion imaging).


               A)     Evaluate good clinical outcome (90-day mRS 0-2) rates in patients with
               discordant imaging profile (unfavorable CT/favorable perfusion imaging vs
               favorable CT/unfavorable perfusion imaging) treated with thrombectomy.


               B)     Evaluate the heterogeneity of thrombectomy treatment effect in patients
               with favorable CT/unfavorable perfusion and unfavorable CT/favorable perfusion
               imaging.


   Methods
                Study Design


SELECT 2 is a prospective, multicenter, randomized open-label clinical trial evaluating: 1) the
efficacy and safety of thrombectomy in patients with unfavorable imaging profiles (large core)
on either CT or perfusion imaging or both treated within 0 to 24 hours from last-known-well;
and 2) the correlation between CT and CT/MR perfusion imaging profiles and 90 day clinical
outcomes (good mRS scores, 0-2) in LVO patients treated with thrombectomy within 0 to 24
hours from last-known-well.


On presentation to the EVT capable center enrolling patients in SELECT 2 trial, patients will
receive a simple (non-contrast CT), CT angiography and CT/MR Perfusion with mismatch
determination using automated RAPID software. The physicians will evaluate the CT scans and
provide ASPECTS score. The CT image will also undergo processing by iSchemaView RAPID
ASPECTS software as an investigational tool and the results will be available to the physicians
for review. ASPECTS for patient selection will be determined independently by appropriately
trained clinicians prior to any assessment with automated ASPECTS.


                                                26

--- PAGE 27 ---
               2                                                     SELECT 2 Protocol
                                                                     4 August, 2021

Patients with unfavorable imaging profiles on either CT (ASPECTS 3-5) or perfusion imaging
(CTP: rCBF<30% or MRP: ADC <620 ≥50cc) or both within 0-24 hrs from last-known-well will be
randomized into thrombectomy plus medical management vs medical management alone.




                                              27

--- PAGE 28 ---
                 2                                                         SELECT 2 Protocol
                                                                           4 August, 2021

                 Enrollment Inclusion and Exclusion Criteria


 Adult patients with AIS due to LVO in the anterior circulation (ICA and MCA occlusions in the
 M1 segment) who are normal or with minimal deficits at the time of their strokes (mRS 0-1),
 have received the pre-specified imaging profile (NCCT, CTA and CTP/MRP) prior to the
 treatment decision, and will be treated with thrombectomy (groin puncture time) plus medical
 management or medical management alone within 24 hrs from their last-known-well are
 eligible for the study (Table 1). A screening log of all patients with LVO presenting within 24
 hours of symptom onset who receive thrombectomy, in addition to non-enrolled patients who
 qualify for SELECT 2 large core definition on imaging, will be kept. Clinical data will be collected
 to evaluate which method best correlates with patient outcome after thrombectomy.
 Mechanical thrombectomy includes the use of stent retrievers ( e.g. Trevo®, Solitaire®,
 EmboTrap Revascularization Devices) and/or aspiration devices (e.g. MicroVention SOFIA
 Catheter, and Penumbra) as recommended by AHA (American Heart Association) guidelines.
 Please review Appendix C for a list of all approved devices.




            Table 1. The SELECT 2 study inclusion and exclusion criteria
Inclusion          1) Adults (18-85 years) with the final diagnosis of an acute ischemic stroke
Criteria             2) NIHSS ≥ 6
                     3) Last known well to groin puncture or medical management between 0 to 24
                     hours
                     4) Pre-stroke modified Rankin Scale score of 0-1
                     5) Eligible for thrombectomy or medical management
                     6) Signed Informed Consent obtained
                     7) Subject willing to comply with the protocol follow-up requirements
                     8) Anticipated life expectancy of at least 3 months




                                                  28

--- PAGE 29 ---
                  2                                                        SELECT 2 Protocol
                                                                           4 August, 2021

Exclusion             1) Inability to undergo CT-Angiography and/or CT/MR Perfusion imaging (e.g.,
Criteria              renal insufficiency, iodine/contrast allergy)
                      2) Co-morbid psychiatric or medical illnesses that would confound the neurological
                      assessments
                      3) Treatment with IV thrombolytic therapy beyond 4.5 hours from last known well
                      4) Treated with IV thrombolytic therapy 3-4.5 hours after last known well AND any
                      of the following:
                         - age >80
                         - current anticoagulant use
                         - history of both diabetes AND prior stroke
                         - NIHSS >25
                         - ischemic involvement of more than third of the MCA territory
                      5) Current participation in another investigational drug or device study.


            3.2.1.1. Specific Neuroimaging Inclusion Criteria
 1. Proven large vessel occlusion in ICA or MCA-M1 occlusion (carotid occlusions can be cervical
    or intracranial, with or without tandem MCA lesions) determined by MRA or CTA
 2. Large infarct-core lesion on at least one of the following
     2.1. Non-Contrast CT (ASPECTS of 3-5)*,
     2.2. CT perfusion (rCBF<30% ≥50cc),
     2.3. MRI-DWI (ADC<620 ≥50cc),


 *ASPECTS 0-2 are not included in this study due to the expected poor outcome in these patients.


              3.2.1.2.     Specific Neuroimaging Exclusion Criteria


     1. Patients who have both ASPECTS of 6-10 on non-contrast CT AND core volume <50 cc on
           perfusion imaging
     2. Patients with very large core on imaging on non contrast CT i.e. ASPECTS ≤ 2

                                                   29

--- PAGE 30 ---
                2                                                          SELECT 2 Protocol
                                                                           4 August, 2021

   3. Evidence of intracranial tumor (except small meningioma) acute intracranial
       hemorrhage, neoplasm, or arteriovenous malformation
   4. Significant mass effect with midline shift
   5. Evidence of internal carotid artery dissection that is flow limiting or aortic dissection
   6. Intracranial stent implanted in the same vascular territory that precludes the safe
       deployment/removal of the neurothrombectomy device
   7. Acute symptomatic arterial occlusions in more than one vascular territory confirmed on
       CTA/MRA (e.g., bilateral MCA occlusions, or an MCA and a basilar artery occlusion).
   8. Signs of established infarct and large area of cerebral edema on non-contrast CT



                Enrollment and Randomization

All patients who meet the clinical criteria listed above are eligible for SELECT 2 clinical enrollment.
This includes both patients who are directly admitted to the study site and patients who are
transferred from an outside hospital. The time of enrollment is the time when the informed
consent is signed by the patient or their authorized legal representative. All patients or their
surrogates will provide written informed consent. If a surrogate has provided informed consent,
an attempt will be made to assess the competence of the patient again at day 1, discharge and
at every follow-up in-person visit within 90 days of the procedure with the study team, if an in-
person visit is feasible. If the patient is able to provide consent, informed written consent
procedure will be reattempted, if an in-person visit is feasible.


                 Remote consent procedure:
A remote consent process to prevent delay in treatment is developed and included in the
SELECT 2 protocol for participating sites that may want to implement such process. This remote
consenting process will be utilized in cases when the patient himself/herself cannot provide an
informed consent with the surrogate not being present on enrollment site. The key
requirements of the process include provision of information regarding the study procedure in
entirety followed by opportunity to ask questions and provision of contact information, and

                                                  30

--- PAGE 31 ---
               2                                                       SELECT 2 Protocol
                                                                       4 August, 2021

receive completed ICF document with signature by the surrogate. An example of such process is
described below. In places where only a legally authorize representative can consent for a
research study, appropriate modifications will be made to the process described below.



   1. Provision of information regarding the study procedure in entirety followed by
       opportunity to ask question:
       1.1. This can be achieved by an audio call, a video call or a teleconferencing service. The
           identity of the surrogate should be confirmed by providing acceptable ID documents
           before providing patients’ related identifiable information.
       1.2. The surrogate should be encouraged to ask question. A contact number should be
           provided to the surrogate in case they have any further questions as they consenting
           process progress or later on.
   2. Complete ICF document:
       2.1. The treating center should transmit all pages of ICF document to the surrogate. All
           pages of ICF document, completed by the surrogate should be received by the
           treating center prior to enrollment and randomization of the patient.
       2.2. Documents with incomplete information, i.e. absence of signature, absence of full
           legal name and absence of date and time of informed consent or missing pages of ICF
           document would not be considered adequate and must be received en-block and
           completed prior to enrollment and subsequent randomization into the study.
   3. Confirmation of the identity:
           The surrogate identity should be confirmed by providing acceptable ID documents
           before any identifiable information is shared and tthe completed informed consent
           form is transmitted.
   4. Transmission of the information through a HIPAA compliant medium:
       4.1. A HIPAA compliant secure medium should be used to transmit the data to the
           surrogate and receive the ICF back from the surrogate. These can include a secure
           institutional email with implemented HIPAA security features, Adobe Sign platform

                                               31

--- PAGE 32 ---
           2                                                      SELECT 2 Protocol
                                                                  4 August, 2021

       approved for transmission of healthcare information or a fax number that is in
       possession of the intended recipient .
   4.2. If the surrogate is present at the remote site, where the patient was first received
       before being transferred to the treatment center, the secured email from the Health
       Service Provider (HSP) at remote treatment site or fax machine under direct control
       and access of the HSP for the patient at remote treatment site can be used to
       transmit the information to and from the LAR.
5. Decreasing the burden of responsibilities from the surrogate as much as possible:
   5.1. The study will ensur that ethe surrogate will receive assistance from the on-site ER
       physician/Nurse/research coordinators to decrease the burden of the consenting
       process including connecting with the surrogate, transferring the study information
       to the surrogate and returning the signed form to the study enrollment site. Use
       video conferencing if possible to establish the contact with the surrogate, provide
       ample opportunity to ask questions and answer all questions in detail. Request
       assistance from on-site healthcare personnel whenever available, provide protocol
       training to them beforehand and consider including them as the study personnel.
       Follow-up with another video call 15-20 minutes after the first contact to provide
       another opportunity to ask questions and assist in the process of signing and
       transmitting the ICF.
6. Documentation in the ICF
   6.1. A complete documentation of the consenting process including the surrogate’s
       name, relationship to the patient, method of transmission of ICF, mode of
       communication and verification of identity should be included in the ICF.




                                          32

--- PAGE 33 ---
                2                                                      SELECT 2 Protocol
                                                                       4 August, 2021

An example of such a procedure is provided below:
      Contact the appropriate surrogate by telephone/videoconferencing.
      Confirm the identity of the surrogate and how he/she is related to the patient.
      Discuss the study details, including procedures, study device and potential risks and
       benefits. Discuss the ICF and give instructions about where the surrogate needs to sign
       and date/time. The study will ensure that the surrogate will receive assistance from the
       on-site ER physician/Nurse/research coordinators to decrease the burden of the
       consenting process including connecting with the surrogate, transferring the study
       information to the surrogate and returning the signed form to the study enrollment site.
      Provide the ICF through a secure medium (Adobe Sign/email/fax).
      Provide the surrogate with a phone number to call you back in the event that she/he has
       questions. Follow-up with a phone/videoconferencing call after 15-20 minutes if they
       have any questions or need any help completing and returning the ICF.
      The surrogate should return the entire, signed and dated ICF back. The ICF is not valid and
       you cannot proceed with study enrollment unless all pages are received and appropriately
       filled out/signed/dated/timed.


After obtaining consent and ensuring all inclusion and exclusion criteria are met, randomization
will be done in the emergency room prior to treatment using a web-based dynamic
randomization system. Our randomization algorithm will be accessible to the study
investigators and staff through a separate web page accessible only through the
REDCAP database module. Covariate adaptive randomization will be used to balance the
distribution of age (<60, 60-69, 70-79, 80-85 years old), presentation NIHSS (6-9, 10-15, 16-20,
>20), center, clot location (M1, ICA), treatment time window (0-8, 9-16, 17-24 hours from onset
to randomization time), CTP/MRP core volume (<50cc, 50-100cc, >100cc), presence or absence
of target mismatch profile (mismatch ratio ≥ 1.8 & mismatch volume ≥ 15 cc) and hemisphere
(right, left) between the two treatment groups.




                                               33

--- PAGE 34 ---
                 2                                                      SELECT 2 Protocol
                                                                        4 August, 2021

The randomization algorithm we are going to implement is the algorithm developed by Pocock
and Simon (1975)27, i.e., minimization method. Through this algorithm, the assignment of a new
patient to a treatment group is determined so as to minimize the differences between the
groups in terms of these important key baseline variables. Unlike traditional stratified
randomization, the minimization method works toward minimizing the total imbalance for all
factors together instead of considering mutually exclusive subgroups, that is, we will not be
creating these mutually exclusive subgroups during the randomization. Therefore, this
approach is not restricted by the number of variables and the possible combinations of levels of
balancing factors. Further details about Randomization can be found in Appendix A.


Eligible patients will be randomized into thrombectomy plus medical management vs medical
management alone at a 1:1 ratio. The minimization algorithm is intended to balance the
baseline characteristics between the two study arms, thrombectomy vs. medical management.
The algorithm is not intended at the level of imaging profile subgroup. When a new patient is
enrolled, the site will enter the stratification factor values into the dynamic randomization
webpage and the treatment assignment will be determined immediately. An emergency 1-800
number will be provided if web-based randomization is not available due to exigent
circumstances.

The assignment of the patients based on site assessment will be considered final for the
primary analysis. A 1-800 number will be provided to the study investigators, where the case
and imaging can be discussed with highly experienced vascular neurologists. A pre-specified
secondary analysis based on core lab imaging assessment will be performed to address the
cases where the core lab assessment differs from the site imaging assessment.




                                                34

--- PAGE 35 ---
                2                                                       SELECT 2 Protocol
                                                                        4 August, 2021

                Endovascular Thrombectomy


The goal for femoral artery puncture will be within 45 minutes of randomization; femoral artery
puncture must occur within 90 minutes of the completion of the qualifying imaging. Patients
will be treated with thrombectomy devices (stent-retrievers) and/or suction (aspiration)
thrombectomy systems currently cleared by the FDA for thrombus removal in patients
experiencing an acute stroke within 24 hours of symptom onset following the published
instructions for use for these devices. The devices which will be used are FDA-approved stent
retrievers: the Trevo Retriever, the Solitaire Revascularization Device, EmboTrap
Revascularization Device and Tigertriever Revascularization Device; and/or the aspiration
devices approved by the FDA (e.g. MicroVention SOFIA Catheter, and the Penumbra
thrombectomy system) permitted in the study. Please review Appendix C for a list of all
approved devices. The choice of thrombectomy method, primary approach/technique, whether
primary aspiration or primary stent-retriever with or without aspiration, will be left up to the
interventionalist, with any of the FDA-approved devices approved in the study protocol or a
combination of them (Appendix C). The study database will collect the thrombectomy method,
and the devices used in the thrombectomy procedure.
Standard medical therapy, based on current AHA guidelines, will also be provided for all
patients. Although any cleared neurothrombectomy device (Appendix C) can be used in the
study, only the Solitaire Revascularization Device and Trevo Retriever are FDA-cleared to be
indicated as a treatment in acute ischemic stroke patients to reduce their disability from the
stroke. Individual investigators may use any of these devices or any combination of these
devices to remove thrombus from the ICA, MCA M1 segment or, if needed, from M2 segments
of the intracranial circulation. These are all approved anatomic locations for these devices. The
use of thrombectomy devices should be performed in accordance with the indications for use
and within the trial protocol. Any deviation from the on-label use of the device outside of the
SELECT 2 protocol should be recorded in the appropriate case report form in detail. If there is
severe stenosis of the common carotid artery or the proximal internal carotid artery,


                                                35

--- PAGE 36 ---
                2                                                         SELECT 2 Protocol
                                                                          4 August, 2021

investigators may also use devices for angioplasty or for stenting of the carotid artery as
deemed appropriate. The use of adjuvant intra-arterial (IA) thrombolytic medication is not
currently approved by the FDA for stroke treatment and cannot be used in SELECT 2.


Sites will use local protocols for femoral access, sedation, heparin infusion, monitoring, etc.
Sites will perform a cervical injection of the involved carotid circulation as a baseline
angiogram. At the conclusion of the procedure, a post-treatment angiogram as a cervical
injection of the involved carotid circulation will also be obtained. Imaging will cover the full
region of the normal circulation in AP and lateral projections at 2-3 films per second through
the entire venous phase. All brain imaging from stroke onset through hospital discharge,
including the MRI, CTP/MRP, and CT, as well as angiographic images obtained for the diagnostic
and therapeutic portions of the procedure, will be transmitted to the core lab. The use of
general anesthesia is left to the local investigators but discouraged by the study given the
concerns of worse outcomes associated with that.
In cases of extracranial ICA occlusions, immediate stenting will be discouraged and delayed
stenting (beyond 72 hours) will be preferred to reduce the risk of hemorrhagic transformation
because of requirements of antiplatelet therapy/heparin to prevent re-occlusion.


                Medical Management


Patients randomized to medical management alone will receive standard AHA guideline-
directed medical therapy, which will include IV thrombolytic therapy available for use
according to practice guidelines in patients presenting within the first 3 hours from last-seen-
normal and meeting other FDA label criteria, or up to 4.5 hours from last-seen-normal and
meeting other AHA guidelines. No procedures or tests required by the protocol will delay
fastest possible delivery of thrombolytic therapy to potentially eligible subjects. The study
database will collect the names of all thrombolytic drugs administered during the study, the
route, the time of start of administration, and the dose administered. For non- thrombolysis
treated patients, this will include aspirin 325 mg on day 1 followed by aspirin 81 mg or 325 mg
                                                 36

--- PAGE 37 ---
                 2                                                       SELECT 2 Protocol
                                                                         4 August, 2021

thereafter, which will be determined by treating physician, and standard deep venous
thrombosis prevention therapy. Equivelent regimens of the aspirin will be allowed in countries
where aforementioned doeses are not commercially available. Intravenous anticoagulation and
dual anti-platelet therapy will be discouraged without clear documented reasoning. Post-
thrombolysis patients will be treated based on standard study site protocols for these patients.


                Outcome Measures

            3.7.1.1.    Primary Outcome

The primary outcome #1 will be the distribution of mRS scores at 90 days. The primary
outcome #2 will be the percentage of good outcome (mRS 0-2) at 90 days. The definition of
favorable primary clinical outcomes is the patients’ functional outcomes at 90 (+/- 15) days,
measured by a modified Rankin scale (mRS) score of 0-2. The determination of mRS scores will
be performed by certified raters unaware of the treatment arm or the baseline clinical and
radiographic characteristics of the individual patient by in person interview or by telephone if
in-person visit is not possible.
The shift in the modified Rankin Scale score is better equipped to capture potential
improvement in the functional outcomes as compared to a binary (dichotomized) outcome with
intervention. Since the study population is composed of acute stroke patients with significant
ischemic changes (unfavorable imaging profiles), the potential shift across modified Rankin
Scale Score categories, not only the functional independence, is of clinical significance. For
details, a change of mRS score of 5 – completely bedridden to mRS score of 4 – ambulating with
a wheelchair and to mRS score of 3 – ambulating with a cane is a successful outcome for
thrombectomy. We will still have the dichotomized outcome as our second primary outcome.


            3.7.1.2.    Secondary Outcomes

Secondary outcome measures include: 1) safety as measured by the incidence of symptomatic
intracranial hemorrhage (sICH) (SITS-MOST)21, neurological worsening (defined as a ≥4-point


                                                37

--- PAGE 38 ---
                2                                                       SELECT 2 Protocol
                                                                        4 August, 2021

increase on the NIHSS score within 24 hours due to the stroke itself), mortality and groin (or
arterial access site) hematomas, infections or any vascular injury caused by the endovascular
procedure, 2) rates of recanalization (complete and partial) using the modified TICI system
(score ≥ 2b defined as favorable reperfusion), 3) length of hospital stay, and 4) discharge
location. 5) significant improvement of ≥8 points on NIHSS at 24 hours of presentation or an
NIHSS of 0-1


           3.7.1.3.   Imaging Outcomes

Imaging endpoints are: 1) infarct volume on MRI DWI sequence (or CT if MRI not feasible) 24
hours to 7 days after randomization; 2) lesion growth between the RAPID identified ischemic
core on baseline imaging and the infarct volume; 3) successful reperfusion defined as DWI
lesion volume minus Tmax>6 seconds greater than 50%; and 4) the proportion of subjects with
recanalization of the primary arterial occlusive lesion. The technical efficacy of the endovascular
procedure will be assessed by a modified Thrombolysis in Cerebral Infarction scores of 2b (50%
to 75% reperfusion), 2c (>75% to 99% reperfusion) or 3 (complete reperfusion). 22


                Clinical and Imaging Evaluations

Clinical assessments will be performed at baseline, 24 hours after randomization, hospital
discharge, 30 days, and 90 days (Table 2). Clinical assessments include the modified Rankin
Scale, the NIHSS, and quality of life measure (Neuro-QoL).23
CT images will be read by appropriately trained clinicians as well as by the iSchemaView
automated ASPECTS prior to randomization. ASPECTS for patient selection will be
determined independently by the clinicians prior to any assessment with automated
ASPECTS. In cases where there is disagreement, the physician reading will override the
automated software reading. CTP images with mismatch determination will be read by
iSchemaView automated RAPID software. All the images including baseline and follow-up
MRI and CT images will be assessed independent of each other and blinded to treatment
allocation at the core imaging laboratory at SELECT 2 Core Lab at McGovern Medical
                                                38

--- PAGE 39 ---
              2                                                 SELECT 2 Protocol
                                                                4 August, 2021

School at UTHealth at Houston. Angiographic studies from the endovascular procedure will
be assessed at SELECT 2 Core Lab.




                                           39

--- PAGE 40 ---
                 2                                                  SELECT 2 Protocol
                                                                    4 August, 2021

                 Table 2. Schedule of Events
                                                                           5-7 Day                Day
                                               Baseline/           Day 1   follow- Day 30 Day 90 365
                            Screenin Enrollme             Thromb
     PROCEDURES                               randomizati         (24 hrs   up (or (+/-15 (+/-15 (+/-60
                                g       nt                ectomy
                                                  on             +/-6 hrs) dischar days) days) days)
                                                                             ge)
     Screen Failure Log         X
 Inclusion and Exclusion
                               X
           Criteria
       Randomization                                X
     Informed Consent                  X
       Demographics                                 X
       Physical Exama                               X
         Vital Signsb                               X
        Baseline Labsc                              X
        Serum HCG (if
                                                    X
         applicable)
      Medical History                               X
   Baseline Medications                             X
Baseline Characteristics                            X
           NIHSSe                                   X                 X          X
 Modified Rankin Scaled                             X                            X      X    X     X
         Neuro-QoLd                                                                          X     X
       Thrombectomy
 Timepoints/Procedural                                       X
            Data
 Post Treatment Hourly
   Blood Pressure Form                              X        X        X
   (Treatment + 24 hrs)e
Baseline Imaging (Head
                                                    X
     CT/CTA/CTP/MRI)
Post Procedure Imaging
(MRI 24 hours-7 days or                                                    X
  CT if MRI not feasible)
  Image CRF completion
by core lab (CT ASPECTS
      Score, CT Angio
     ASPECTS score, CT                              X        X        X          X
  perfusion score, Angio
   mTICI, Capillary Index
         Score, Post-

                                               40

--- PAGE 41 ---
                 2                                                         SELECT 2 Protocol
                                                                           4 August, 2021

treatment/procedural,
      hemorrhage)f
       AE Reporting                                                         X           X        X     X
      SAE Reporting                                                         X           X        X     X
Crossover explanations                               X
   Protocol Deviation                                X                      X           X        X     X
 a. Physical exam at baseline as per standard of care (SOC). b. Vital Signs (BP and HR) recorded
 at baseline as per SOC. c. Labs (evaluation includes CBC with Platelets, Creatinine, Glucose, INR,
 activated PTT, and Pregnancy test (if applicable): at baseline as per SOC. d. If possible, 30 and
 90-day visits should be completed in person. The telephone is allowed if the only option. e. for
 medical arm: recording blood pressure readings starts from either thrombolytics administration
 (if applicable) or randomization, for EVT arm recording blood pressure readings starts from the
 end of the thrombectomy procedure. f.Head CT/CTA/CTP/MRI: will be read centrally.


                        Assessment and Follow-up Visits

 Baseline visit: The inclusion/exclusion page of the case report form must be completed to
 determine if the patient meets the eligibility requirements for the study. If the patient is
 eligible, then the consent form will be obtained by the patient or authorized representative.


 24-hour visit (+/- 6 hours): The items listed for this visit in Table 2 should be performed
 between 18 and 30 hours from the time of the procedure.


 Discharge visit: The items listed for this visit in Table 2 should be performed either on day 5/7
 or the day of hospital discharge (whichever comes first).


 30-day visit (+ / - 15 days): The items listed for this visit in Table 2 should be performed on day
 30 (+/-15) days. The mRS score must be performed by an mRS certified evaluator who is blinded
 to treatment allocation. If possible, this visit should be completed in person. Telephone is
 allowed if the only option.


 90-day visit (+ / - 15 days and preferably an in-person visit): The items listed for this visit in
 Table 2 should be performed on day 90 (+/- 15) days. The mRS score must be performed by an

                                                  41

--- PAGE 42 ---
                2                                                      SELECT 2 Protocol
                                                                       4 August, 2021

mRS certified evaluator who is blinded to treatment allocation. The Neuro-QoL will also be
completed on 90-day visit by an evaluator who is blinded to treatment allocation. If possible,
this visit should be completed in person. Telephone is allowed if the only option.


365-day visit (+ / - 60 days): The mRS score must be performed by an mRS certified evaluator
who is blinded to treatment allocation. The Neuro-QoL will also be completed on 360-day visit
by an evaluator who is blinded to treatment allocation. Patients who were enrolled in the study
at a date before the addition of the 365-day follow up visit, will be consented (remotely or in
person) to complete the visit. The supplemental informed consent can be obtained verbally or
in-written for patients who already provided their consents (or their LAR’s consent) to
participate in the study.


Neurological worsening: If clinical worsening (defined as a ≥4 point increase on the NIHSS
score) occurs prior to discharge, a CT scan or MRI should be obtained as soon as
possible.Neurological worsening is a reportable adverse event.

   Sources of Materials

Information on the clinical status of patients will be obtained from the patient’s medical
record. Study coordinators at the site will complete the SELECT 2 case report forms to
collect basic demographic and medical information about the patients. Data will
subsequently be entered into the REDCAP electronic data capture system. Imaging data
will be uploaded on DICOM (all patient identifiers are removed by the software prior to
exporting the data outside of the site’s firewall). All study sites will complete a screening
log that documents all acute stroke patients treated by thrombectomy in the cath lab as
well as patients who met the imaging criteria but were not enrolled in the study at their
center, and the reason for exclusion of patients not enrolled. Serious adverse events (SAEs)
will be reported within 24 hours of the event in the REDCAP electronic data capture
system.


                                               42

--- PAGE 43 ---
                2                                                         SELECT 2 Protocol
                                                                          4 August, 2021

   Site Approval and Monitoring Plan

Site approval: The University of Texas Health Science Center at Houston is the administration
center and conducts data monitoring, core image lab reading and statistical analyses. Sites are
selected for participation based on their experience in conducting clinical trials, their acute
stroke treatment, and thrombectomy volumes, and only after an extensive discussion and
vetting process by the principal investigator and documentation of interventionist experience,
prior clinical trial enrollments, well-established research infrastructure, commitment to
conducting clinical research, fast treatment times and efficient workflow. Sites will have a
requirement of at least 100 thrombectomy procedures/year. Sites will commit to
randomization and treatment criteria based on agreed upon contract. Selected sites will have
access to emergent CT/CT perfusion and/or MR imaging 24/7. Prior to activating a site, we will
verify that RAPID is functional at the site. Sites will be activated for enrollment after test cases
processed with RAPID have ensured good quality maps.


Monitoring for imaging quality: The Imaging Core Lab will monitor image quality throughout
the study. If significant inadequacies or protocol errors are noted at a site, enrollment will be
halted. Enrollment will resume after all imaging problems have been resolved and repeat
dummy runs have been obtained that demonstrate adequate image quality.


Monitoring for bias: A detailed site-monitoring plan has been developed to detect bias. This
plan will protect the study from enrollment, randomization, and treatment bias. Sites will
report their volume of endovascular stroke procedures (within 24 hrs) each month on a
screening log. If a SELECT 2 eligible patient is treated with endovascular thrombectomy outside
the SELECT 2 study, an explanation will be required detailing why the patient was not enrolled.
The second component of the plan involves tracking of patients who are consented but not
randomized. These patients will require an explanation of why the patient was not randomized
as well as documentation whether endovascular thrombectomy was performed outside of the
study. A third component involves monitoring of crossover after randomization. The Executive

                                                 43

--- PAGE 44 ---
                2                                                         SELECT 2 Protocol
                                                                          4 August, 2021

Committee will review the data described above for each site every 6 months. If evidence of
enrollment bias is suspected, it will be investigated. If confirmed, the site will be placed on
probation. If additional incidents of suspected bias are confirmed, the site will be withdrawn.
Routine monitoring of the clinical sites for the source to database verification will be performed
by the UT Houston site.


  Sample Size Calculation and Statistical Analysis Plan


                Sample Size justification, Adaptive Enrichment Design, and Statistical Analysis
                Plan


The study will implement a novel adaptive enrichment design that will not only allow the trial to
stop early for efficacy but also allow to select and evaluate the treatment effect in a most
promising subpopulation if futility rule is triggered at the interim (or final) analyses in the
overall population. This adaptive design has been developed, well-studied, and implemented
for the DEFUSE 3 studies24. The details and theory of this adaptive enrichment design are
summarized in Lai et al (2014)25 and Lai et al (2018)26. This adaptive enrichment design is an
extension of standard group sequential design with an enrichment feature 25. It will test for
efficacy or futility with two interim analyses and a final analysis. This adaptive design was
chosen because the preliminary data from the SELECT study suggest a potential heterogeneity
in thrombectomy treatment effect based on the different imaging profiles. By adopting this
adaptive design, we expect to reallocate future accrual and study treatment effects only in a
most promising subpopulation when there is evidence to show that EVT is futile in the overall
population at interim (or final) analyses. By limiting the subsequent enrollment only in the most
promising subpopulation, a larger number of patients will eventually be enrolled in this
subgroup for efficacy testing compared to traditional designs.


This design uses the Generalized Likelihood Ratio (GLR) statistic (Kullback-Leibler criterion) as
criteria to identify the subgroup, which has the best chance of showing a benefit from EVT.
                                                 44

--- PAGE 45 ---
                2                                                       SELECT 2 Protocol
                                                                        4 August, 2021

Through these criteria, it can achieve optimal balance simultaneously between the estimated
size of the treatment effect and the sample size of the subgroup. By considering the CTP core
volume and treatment time window, the patients are split into six disjoint groups, that is Group
1 (ASPECTS 3-5 and CTP/MRP core volume <50cc) at early time window 0-12 hours (denoted as
G1A), Group 1 at late time window 12-24 hours (denoted as G1B), Group 2 (ASPECTS 6-10 and
CTP/MRP core volume ≥50cc) at early time window (denoted as G2A), Group 2 at late time
window (denoted as G2B), Group 3 (ASPECTS 3-5 and CTP/MRP core volume ≥50cc) at early
time window (denoted as G3A), and Group 3 at late time window (denoted as G3B).
Considering a prior assumption that the EVT effect is largest in the patients with good imaging
profile and treated within the shortest time window, we assume that the highest effect of EVT
will be observed in G1A. Then the effects get decreased gradually in G1B, G2A, G2B, G3A, and
the lowest effect will be observed in G3B. According to this adaptive design, when a most
promising subgroup needs to be selected at the time of interim (or final) analysis, we will
compare the GLR statistic among five cumulative groups, that is, G1A, G1A+G1B (i.e., Group 1),
G1A+G1B+G2A, G1A+G1B+G2A+G2B (i.e., Group 1+Group 2), and G1A+G1B+G2A+G2B+G3A.
Primary analysis: The primary endpoint is the distribution of scores on the modified Rankin
Scale (mRS) at day 90. The null hypothesis will be tested at the interim and final analysis using a
normal approximation of the Wilcoxon-Mann-Whitney test (the GLR test). The principle of the
intention to treat will be applied for the primary analysis. An additional analysis of the primary
endpoint will be the same rank-based analysis comparing the 90-day mRs distribution between
treatment groups while stratifying for prognostically important covariates. We will use the
Generalized Cochran-Mantel-Haenszel test (CMH) to evaluate whether there is a uniform shift
on the mRS distribution from one group to the other after stratification. The CMH test will be
stratified by these variables used in the covariate adaptive randomization. For age, NIHSS,
treatment time window, and CTP core volume, we will consider them as continuous variables in
this adjusted analysis.




                                                45

--- PAGE 46 ---
                2                                                         SELECT 2 Protocol
                                                                          4 August, 2021

Power and sample size considerations Based on prior reported data, the following distributions
were projected on the mRS at 90 days in EVT and MM groups for SELECT 2 in the overall
population.

                           mRS at day 90
                           0        1       2         3      4        5        6         Total
  Endovascular group       4%       8%      12%       16%    19%      13%      28%       100%
  Medical group            1%       4%      9%        14%    19%      10%      43%       100%



This distribution corresponds to a standardized effect of 0.34 for the primary analysis. Based on
these data, the fixed sample size for a non-adaptive design requires a total of 376 patients
(188/arm) to have 90% power at an alpha of 5% (Wilcoxon-Mann-Whitney test); We add
additional 184 patients for the adaptive design to reach a maximum sample size of 560. We will
conduct two interim analyses when we reach the number of patients at 200 and 380. Through
extensive simulation studies, we have shown that with 560 patients in total for the adaptive
design, we will have around 91% power to test for a standardized effect size of 0.34 in the
overall population (assuming homogeneous EVT effect across six disjoint groups) by controlling
an overall (one-sided) Type I error rate at 2.5%.



Efficacy and futility bound At each analysis (two interim analyses and the final analysis), an
efficacy bound will be set to decide if the study should be stopped for efficacy while controlling
the overall (one-sided) Type I error rate at 2.5%. At each interim analysis, a futility bound will
be set to decide if the study should continue recruitment in the overall group, shift accrual and
testing to a subgroup, or stop the trial entirely. When the futility bound is crossed and the
optimal subgroup is selected, the maximum analyzed sample size will not be fixed but a random
variable (smaller than the fixed maximum sample size 560). Due to the reduction in the
maximum number of patients available for analysis at the end of the study, our design allows



                                                 46

--- PAGE 47 ---
                2                                                         SELECT 2 Protocol
                                                                          4 August, 2021

an easier futility stop after subgroup selection. Further details regarding efficacy and futility
bounds at interim and final analyses is provided in Appendix B.



First interim analysis (n=200 randomized and completed 90-day follow-up): The null
hypothesis is tested in the entire patient cohort:

1. If neither efficacy nor futility bound is crossed, the trial continues enrollment to the 2 nd
   interim analysis.
2. If the efficacy bound is crossed, the trial stops and efficacy is declared in the overall cohort.
3. If the futility bound is crossed, the optimal subgroup is selected based on the GLR statistic
   and the null hypothesis is tested in this selected subgroup:
   3.1. If neither bound is crossed, the trial will continue with enrollment limited to the
         selected subgroup
   3.2. If the efficacy bound is crossed, the trial stops and efficacy is declared in the selected
         subgroup
   3.3. If the futility bound is crossed, the trial stops for futility.

   Note: the futility bound is relaxed as described above, based on the expected maximum
   number of patients in the trial at completion (i.e. 560 minus the number of patients already
   enrolled in the groups that will no longer be open for enrollment).



Second interim analysis (n=380 randomized and completed 90 day follow-up): After the first
interim analysis, the trial proceeds to this stage under two scenarios: (1) continuing enrollment
in the overall population (i.e., option 1 above) and (2) limiting enrollment to a selected
subgroup (i.e., option 3.1 above). When scenario (1) happens, the testing at the 2 nd interim
analysis is identical to the first interim analysis. When scenario (2) happens, the null hypothesis
is tested in that selected subgroup:

1. If neither bound is crossed, the trial continues to the final analysis with an enrollment of
   560-380=180 additional patients limited to the selected subgroup
                                                  47

--- PAGE 48 ---
                 2                                                       SELECT 2 Protocol
                                                                         4 August, 2021

2. If the efficacy bound is crossed, the trial stops and efficacy is declared in the selected
    subgroup
3. If the futility bound is crossed, the trial stops for futility.
Final analysis (n=560 randomized and completed 90-day follow-up): After the 2nd interim
analysis, the trial proceeds to the final stage under two scenarios: (1) continuing enrollment in
the overall population and (2) limiting enrollment to a selected subgroup.

When scenario (1) happens, the null is tested in the overall population:

1. If the efficacy bound is crossed, EVT is declared efficacious in the overall population.
2. If the efficacy bound is not crossed, the optimal subgroup is selected and the null is tested
    in that group:
    2.1. If the efficacy bound is crossed, EVT is declared efficacious in that subgroup
    2.2. If the efficacy bound is not crossed, EVT will be declared of no benefit.
When scenario (2) happens, that is, limiting enrollment to a subgroup (either selected at the 1 st
or 2nd interim analyses), the null hypothesis is tested in that selected subgroup only. Efficacy or
lack thereof will be declared as per options 2.1 and 2.2 above.

Operating characteristics of the adaptive design: We have conducted simulations (5000
simulated trials) to evaluate the performance of the adaptive design (max n=560) and compare
it to a traditional fixed sample-size design (fixed n=560) under various scenarios (see Table 3,
below). For the simulations the effect size is expressed as a standardized effect with normal
approximation, where a standardized effect of 0.32 or 0.30 corresponds to a conservative
projected effect of EVT (anticipated effect 0.34; see section of Power and sample size
considerations). We assume that we will observe the number of patients in G1A, G1B, G2A,
G2B, G3A, G3B with 14%, 6%, 14%, 6%, 42%, and 18%, respectively.




                                                   48

--- PAGE 49 ---
                      2                                                       SELECT 2 Protocol
                                                                              4 August, 2021

                                                            Adaptive Design        Fixed Design
                                               Average
            Standardized effect in groups
                                                            Average
 Scenario                                      standar                             Number
            G1A, G1B, G2A, G2B, G3A, G3B                    No.          Power                    Power
                                               d. effect                           randomized
                                                            randomized

 #0         0     0    0     0    0     0      0            426          2.0%      560            2.5%

 #1         0.32 0.32 0.32 0.32 0.32 0.32      0.32         376          86.0%     560            95.8%

 #2         0.3 0.3 0.3 0.3 0.3 0.3            0.3          393          81.1%     560            93.3%

 #3         0.4 0.4 0.4 0.4        0     0     0.16         500          74.1%     560            45.7%



 #4         0.4 0.4 0.4 0.4 -0.1 -0.1          0.1          502          78.5%     560            21.2%

 #5         0.4 0.4 0.3 0.3 0           -0.1   0.122        513          67.1%     560            29.2%

 #6         0.5 0.5 0        0    0     0      0.1          503          70.6%     560            21.2%

 #7         0.5 0      0     0    0     0      0.07         503          60.5%     560            12.8%

Table 3. Under the null (Scenario #0), the adaptive design controls the total Type 1 error below 2.5%, stops
early for futility 59.1% of the time, and the average number of randomizations is 426. If the effect is
uniform across cells at 0.32 (scenario #1), the fixed-sample design is optimal, but the adaptive design
results in only a small loss of power (from 95.8% to 86.0%), but reduced the expected sample size (from
560 to 376). We observed similar findings when the effect is uniform across cells at 0.3 (scenario #2). The
adaptive design performs much better (higher power and smaller expected sample size) than the fixed-
sample design when the effect size distribution across the subgroups is in accord with the biological
assumptions (scenarios #3, #4 and #5). If the effect is concentrated only in Group 1 (scenario #6) or Group
1A (scenario #7), the adaptive design maintains power (70.6% in scenario #6 and 60.5% in scenario #7)
while the conventional design collapses (21.2% power in scenario #6 and 12.8% in scenario #7).




                                                       49

--- PAGE 50 ---
                2                                                       SELECT 2 Protocol
                                                                        4 August, 2021

Secondary analyses: Our secondary endpoint is the proportion of patients with mRS 0-2 at day
90 (indicating functional independence). The difference in the proportions of patients with mRS
0-2 between treatment arms will be assessed using logistic regression. We will adjust for the
variables we used in adaptive randomization program in the logistic regression model. Other
secondary endpoints include (1) the safety outcomes measured by the incidence of sICH,
neurological worsening, mortality, groin hematomas, infections or vascular injury, (2) infarct
volume, lesion growth, successful reperfusion, and recanalization rate, (3) length of hospital
stay, and (4) discharge disposition. The exploratory analyses on secondary outcomes will
include descriptive statistics (mean [± standard deviation, SD] or median and interquartile range
for continuous variables and frequency [percentage] for discrete variables) and appropriate test
for secondary outcome variables between two groups. For binary outcomes (e.g., sICH,
neurological worsening, mortality, groin hematomas, infections or vascular injury, successful
reperfusion, recanalization), Chi-square or Fisher’s exact test where appropriate will be used to
compare the incidence between two treatment groups for large core patients. We will also
apply the logistic regression model on these outcomes after adjusting for the variables we used
in adaptive randomization program. The adjusted odds ratio (OR), as well as 95% confidence
interval will be reported. For the length of stay, mean ± SD and median (Interquartile range) will
be calculated for each group. For continuous variables (e.g., the length of stay and infarct
volume), two sample t-test or Wilcoxon rank sum test as appropriate will be applied to
compare them between two groups. For discharge disposition, frequency and percentage of
each disposition will be reported and Chi-square test or Fisher’s exact test where appropriate
will be applied to compare its distribution between two groups.



Subgroup analyses: Subgroup analyses of the effect of thrombectomy on the primary and
secondary endpoints will be performed. Subgroups will be defined based on the stratification
variables, key demographic factors (such as race and ethnicity), thrombolysis vs. no
thrombolysis, CTP vs. MRI selection, and witnessed vs. unwitnessed symptom onset, wake-up
vs non-wake-up stroke, and TICI 0-2a vs. TICI 2b/3 results in the cath lab. An additional

                                                50

--- PAGE 51 ---
               2                                                      SELECT 2 Protocol
                                                                      4 August, 2021

subgroup analysis will be performed in patients who present with extracranial ICA occlusion.
Also, an additional subgroup analysis will be performed in patients based on thrombolytic
therapy received.



               Statistical plan for the second aim

The second aim is to compare outcomes in patients with discordant imaging profiles. Good
outcome rates (90-day mRS 0-2) will be compared between EVT patients with favorable
CTP/unfavorable CT and EVT patients with unfavorable CT/favorable CTP. Logistic
regression model will be applied and odds ratio as well as 95% CI will be calculated. If there
is a significant difference in the outcome, we will evaluate whether any patient
characteristics could be potential confounders and can explain these differences.



We will also assess the heterogeneity of the treatment effect of thrombectomy comparing
to medical management between patients with favorable CT/unfavorable CTP and patients
with unfavorable CT/favorable CTP. We will assess the heterogeneity by evaluating the
interaction effect in the logistic regression model between treatment groups (EVT vs MM)
and imaging profile (favorable CT/unfavorable CTP vs unfavorable CT/favorable CTP). If the
interaction term is statistically significant, we will examine patient characteristics and other
baseline clinical characteristics for possible correlations or confounding factors.


               Poolability analysis across centers

The data from all investigative sites will be pooled based on the assumption of comparable
clinical aspects such as the common protocol used, adequate monitoring on protocol
compliance, and the centralized data gathering and validation systems across all study
sites.




                                              51

--- PAGE 52 ---
                2                                                       SELECT 2 Protocol
                                                                        4 August, 2021

We will assess the poolability across the sites by evaluating the interaction effect between
treatment groups and sites. If the interaction term is statistically significant, we will
examine patient characteristics and other baseline clinical characteristics for possible
correlations or confounding factors. Sites with fewer than five subjects will be combined
based on geographic region.
               Feasibility of enrollment
The study is planning to involve 30 high volume centers with volumes of 150-200
thrombectomies/site/year. Based on SELECT data, roughly 20% of the patients have
unfavorable imaging profiles on either CT or CTP, with ~30 patients/site/year eligible to
participate in the study. Assuming 50% of the patients consenting to participate in the
study and at 30 sites coming onboard in a gradual fashion, the study will complete the
enrollment target (560 patients) in nearly 2 years.
                  Missing Data/Lost to Follow-up (LTFU)
All effort is put forth to ensure near complete follow-up, in particular with the assessment of
the primary outcome (mRS at 90 days), death (mRS=6), and stroke recurrence. If the primary
outcome (mRS at 90 days) cannot be assessed in the clinic, it will instead be obtained by phone
using a structured interview. If the subject’s mRS cannot be obtained in clinic or by phone
within the window of 60 to 120 days from randomization, we will use multiple imputation
method to impute 90-day mRS. Specifically, using the data from patients with available 90-day
mRS, we will build ordinal logistic regression based on patient baseline features and prior mRS
scores to impute 90-day mRS.




                                               52

--- PAGE 53 ---
                   2                                                        SELECT 2 Protocol
                                                                            4 August, 2021

   SELECT 2 Timetable




         Year 1:                                       Year 3:                             Year 4:
                              Year 2:          -Complete enrollment             -Complete data of one-year
  -Site initiations and                                                            follow up assessment
      IRB approvals         -Continue          -Data analysis for the             -Complete data analysis
   -Begin enrollment        enrollment           primary endpoint              -Publication of results of one-
                                               -Publication of results           year follow up assessment




   Risk Analysis

Description and analysis of all increased risks to the research subjects:


Potential complications of MRI scan include localized twitching sensation due to the magnetic
field changes during the scan, anxiety due to claustrophobia and allergic reaction to the
contrast agent. The allergic reaction may include headache, nausea, rash, hives, nasal
congestion, sneezing, itching or swelling. If a severe reaction occurs, swelling of the throat,
chest tightness, or a marked drop in blood pressure may occur. In addition, pain, bleeding,
bruising, coldness or inflammation at the injection site may occur. Precautions will be taken for
early detection and rapid treatment if such reactions occur.


Potential complications of CT scan include radiation exposure and allergic reaction to CT
contrast agents. The iodinated contrast administration may also result in transient and rarely
permanent renal failure due to nephrotoxicity.
                                                 53

--- PAGE 54 ---
                2                                                        SELECT 2 Protocol
                                                                         4 August, 2021

Radiation doses:
Combined scanning with comprehensive stroke imaging, which includes a non-contrast head
CT scan, perfusion imaging, and CT angiography of the cervicocranial vessels starting at the
aortic arch results in a dose of approximately 7-10 mSv (Diekmann et al. 2010). According to the
National Council on Radiation Protection and Measurement, the average annual radiation dose
per person in the U.S. is 620 millirem (6.2 milliSieverts).


Reactions to contrast agents:
Mild
Nausea, Vomiting, Headache, Cough, Nasal stuffiness, altered taste, Flushing, Itching, Rash,
Hives, Sweats, Swelling of eyes or face


Moderate
Mild hypotension, Tachycardia or Bradycardia, Bronchospasm, Wheezing, Dyspnea, Laryngeal
edema, Generalized or diffuse erythema


Severe
Cardiopulmonary arrest, clinically manifested arrhythmias, profound hypotension, Convulsions,
Unresponsiveness, Respiratory failure, Laryngeal edema. The rate of major reactions (e.g.,
anaphylaxis, death) is very low, estimated at one in 170,000 administrations.


Potential complications of endovascular thrombectomy include stroke; new clot in an artery;
total blockage of an artery; infection and pain in the region of insertion site; lack of blood flow
to the brain; rupture or puncture of an artery; significant tearing of the vessel wall; bleeding
requiring blood transfusion; allergic reaction to contrast dye; abnormal low blood pressure
requiring treatment; temporary closing of the artery (vessel spasm); formation of or
dislodgments of clots which block the arteries (embolism). In rare circumstances, the procedure
could result in death. At the puncture site in the groin, a blood clot or other blood vessel injury


                                                 54

--- PAGE 55 ---
                2                                                       SELECT 2 Protocol
                                                                        4 August, 2021

may occur and require blood transfusion or surgical repair. Infection may occur at the puncture
site; this could cause pain and require additional medications. There is some chance of an
allergic reaction or renal injury due to the x-ray contrast (dye) used during the angiogram
procedure. Minor allergic reactions may include a rash or hives. There is also the possibility of a
serious allergic reaction that could include shortness of breath and swelling, drop in blood
pressure, and even death. Patients will be closely monitored for these reactions and receive
prompt treatment to reverse any allergic reactions.

    Methods to mitigate risks to subjects in the trial

Methods to mitigate risks to subjects in the trial include the exclusion of subjects with bleeding
disorders and selection of subjects via neuroimaging to minimize the risk of symptomatic
intracranial hemorrhage. Computed Tomography (CT) scans will be performed for neurological
deterioration (≥ 4 point increase in National Institutes of Health Stroke Scale (NIHSS) score) to
identify new strokes, hemorrhage, or edema. Hospitals will follow their local standard of care
safety procedures in order to reduce the risk of kidney dysfunction caused by contrast agents.
Only investigators who are trained and experienced with the use of the devices allowed within
the trial are eligible to participate. The adaptive design will eliminate subgroups with an
unfavorable therapeutic response. Patients will be carefully screened for CT, MRI, and
endovascular treatment contraindications according to the inclusion/exclusion criteria and
excluded from enrollment if any are present. Radiation exposure during all tests will be
minimized by optimizing the imaging protocols and by limiting fluoroscopy-time during the
endovascular procedure. All CT sequences, including the CTP sequence, meet all FDA guidelines
for radiation exposure.


To address the concerns of safety in early window for patients with favorable CT / unfavorable
CTP profile in early window treated with medical management, consecutive monitoring of
safety outcomes will be carried out for these patients. If the rates of safety outcomes e.g.
mortality increases by >20% in patients treated by medical management only compared to


                                                55

--- PAGE 56 ---
                2                                                         SELECT 2 Protocol
                                                                          4 August, 2021

thrombectomy, enrollment within the group will be halted pending data safety monitoring
board recommendations.


Although no upper limit is specified for infarct core volume measurements on CT or MR
perfusion imaging, the infarct size is still expected to be limited, to an extent, given that the
imaging exclusion criteria of “Patients with very large core on non-contrast CT i.e. ASPECTS ≤ 2”
and patients with “Signs of established infarct and large area of cerebral edema on non-
contrast CT”.


To reduce the risk of hemorrhagic transformation in cases with extracranial ICA occlusion,
immediate stenting of the extracranial lesion will be strongly discouraged and stenting beyond
72 hours of procedure will be strongly encouraged. Use of dual antiplatelet therapy and heparin
will also be discouraged.

     Stopping rules or safety triggers for the study

All participating centers are carefully selected to include only centers with high-volume and
experienced interventionalists. The study PI reserves the right to terminate sites that
significantly deviate from standard-of-care. Further, sites that violate the study inclusion or fail
to produce timely data will be subject to possible termination.


The SELECT 2 has established the following two-step stopping rules for safety based on sICH
and mortality rates using Bayesian method (Thall, Simon, and Estey, 1995) 28.
Since it is plausible that the safety concerns will increase with increment in ischemic core
volume, consecutive monitoring of symptomatic ICH and mortality will be carried out in
endovascular patients with CTP/MRP core volume of >100 cc and endovascular patients with
CTP/MRP core volume ≤100cc separately.




                                                 56

--- PAGE 57 ---
                2                                                      SELECT 2 Protocol
                                                                       4 August, 2021

For sICH:
   1) Step 1 for sICH: check whether the posterior probability that the rate of symptomatic
       ICH (NIHSS worsening of 4 or more points associated with sICH per SITS-MOST definition
       assessed within 24 hours after randomization) in one of the endovascular group is >35%
       exceeds the cut-off 0.95. That is, check whether Pr{ ߨ௦ா > 0.35 | data} > 0.95, where the
       sICH rate in this endovascular group is denoted as ߨ௦ா .


In the event that Step 1 for sICH in one of the endovascular group is triggered, step 2 for sICH
for that group will be executed. Otherwise, continue the trial.


   2) Step 2 for sICH: if Step 1 for sICH in one of the endovascular group is triggered, check
       whether the posterior probability that the sICH rate in this endovascular group is higher
       than the corresponding medical management by 10% exceeds the cut-off 0.95. That is,
       check whether Pr{ ߨ௦ா > ߨ௦ெ +10% | data} > 0.95, where the sICH rate in the
       corresponding medical management group is denoted as ߨ௦ெ .
In the event that Step 2 for sICH in of the endovascular group is triggered, patient enrollment
will be placed on hold and a meeting of the DSMB will be conducted to discuss the events and
make a determination on the continuation of the trial.


For endovascular patients with CTP/MRP core volume ≤100cc, we will conduct the two-step
stopping rules for sICH after we enroll 50, 100, 150, 200, and 250 in this group (the maximum
number of patients to be enrolled into the endovascular group is 280 and we expect 80% of
patients’ CTP/MRP core volume will ≤100cc.). We assign a weakly informative prior distribution
for both ߨ௦ா and ߨ௦ெ , that is, a beta distribution with two shape parameters at 0.35 and 0.65,
which centers at 0.35 with an effective sample size of 1.




                                               57

--- PAGE 58 ---
                 2                                                       SELECT 2 Protocol
                                                                         4 August, 2021

The rule of step 1 for sICH in this group can be pre-determined in the following table.
Find your number of patients with CTP/MRP core volume ≤100cc in the endovascular group in
the left-side column. The step 1 for sICH will be triggered if the number of sICHs is in the range
in the right-side column (the range is inclusive):


 # of patients with CTP/MRP core volume         # of sICHs
 ≤100cc in the endovascular group
 50                                             24-50
 100                                            44-100
 150                                            63-150
 200                                            82-200
 250                                            101-250


For endovascular patients with CTP/MRP core volume >100cc, we will conduct the two-step
stopping rules for sICH after we enroll 20 patients in this group and then conduct monitoring
after every 10 patients in this group (We expect 20% of patients’ CTP/MRP core volume will
>100cc, that is, among 280 endovascular patients, around 56 endovascular patients are with
CTP/MRP core volume >100cc.). Similarly, we assign a weakly informative prior distribution for
both ߨ௦ா and ߨ௦ெ , that is, a beta distribution with two shape parameters at 0.35 and 0.65, which
centers at 0.35 with an effective sample size of 1.
The rule of step 1 for sICH in this group can be pre-determined in the following table.
Find your number of endovascular patients with CTP/MRP core volume >100cc in the left-side
column (we provide the table up to 100 patients, but if we enroll more than 100 patients in this
group, we will run the algorithm and identify the # of sICHs which will trigger the rule). The step
1 for sICH will be triggered if the number of sICHs is in the range in the right-side column (the
range is inclusive):




                                                 58

--- PAGE 59 ---
                 2                                                       SELECT 2 Protocol
                                                                         4 August, 2021

 # of patients with CTP/MRP core volume         # of sICHs
 >100cc in the endovascular group
 20                                             11-20
 30                                             16-30
 40                                             20-40
 50                                             24-50
 60                                             28-60
 70                                             32-70
 80                                             36-80
 90                                             40-90
 100                                            44-100


For endovascular patients with Extracranial Occlusions, we will conduct the two-step stopping
rules for sICH after we enroll 20 patients in this group and then conduct monitoring after every
10 patients in this group (We expect 10% of patients will have isolated extracranial ICA
occlusions, that is, among 280 endovascular patients, around 28 endovascular patients are with
extracranial ICA occlusions). Similarly, we assign a weakly informative prior distribution for both
ߨ௦ா and ߨ௦ெ , that is, a beta distribution with two shape parameters at 0.35 and 0.65, which
centers at 0.35 with an effective sample size of 1.
The rule of step 1 for sICH in this group can be pre-determined in the following table.
Find your number of endovascular patients with Extracranial ICA occlusions in the left-side
column (we provide the table up to 100 patients, but if we enroll more than 100 patients in this
group, we will run the algorithm and identify the # of sICHs which will trigger the rule). The step
1 for sICH will be triggered if the number of sICHs is in the range in the right-side column (the
range is inclusive):




                                                59

--- PAGE 60 ---
                  2                                                      SELECT 2 Protocol
                                                                         4 August, 2021



 # of patients with extracranial ICA             # of sICHs
 occlusions
 20                                              11-20
 30                                              16-30
 40                                              20-40
 50                                              24-50
 60                                              28-60
 70                                              32-70
 80                                              36-80
 90                                              40-90
 100                                             44-100


For mortality,
      1) Step 1 for mortality: check whether the posterior probability that the rate of mortality
         at Day 90 in one of the endovascular group is > 40% exceeds the cut-off 0.95. That is,
                            ா
         check whether Pr{ ߨ௠ > 0.40 | data} > 0.95, where the mortality rate in this
                                           ா
         endovascular group is denoted as ߨ௠ .


In the event that Step 1 for mortality in one of the endovascular group is triggered, step 2 for
mortality in this group will be executed. Otherwise, continue the trial.


      2) Step 2 for mortality: if Step 1 for mortality in one of the endovascular group is
         triggered, check whether the posterior probability that the mortality rate in this
         endovascular group is higher than the corresponding medical management by 10%
                                                               ா    ெ
         exceeds the cut-off 0.95. That is, check whether Pr{ ߨ௠ > ߨ௠ +10% | data} > 0.95, where
                                                                                         ெ
         the mortality rate in the corresponding medical management group is denoted as ߨ௠ .



                                                 60

--- PAGE 61 ---
                2                                                       SELECT 2 Protocol
                                                                        4 August, 2021

In the event that Step 2 for mortality in one of the endovascular group is triggered, patient
enrollment will be placed on hold and a meeting of the DSMB will be conducted to discuss
the events and make a determination on the continuation of the trial.


For endovascular patients with CTP/MRP core volume ≤100cc, we will conduct the two-step
stopping rules for mortality after we enroll 50, 100, 150, 200, and 250 in this group (the
maximum number of patients to be enrolled into the endovascular group is 280 and we expect
80% of patients’ CTP/MRP core volume will ≤100cc.). We assign a weakly informative prior
                       ா      ெ
distribution for both ߨ௠ and ߨ௠ , that is, a beta distribution with two shape parameters at 0.4
and 0.6, which centers at 0.4 with an effective sample size of 1.


The rule of step 1 for mortality in this group can be pre-determined in the following table.
Find your number of patients with CTP/MRP core volume ≤100cc in the endovascular group in
the left-side column. The step 1 for mortality will be triggered if the number of deaths is in the
range in the right-side column (the range is inclusive):


 # of patients with CTP/MRP core volume         # of deaths
 ≤100cc in the endovascular group
 50                                             26-50
 100                                            49-100
 150                                            71-150
 200                                            92-200
 250                                            113-250


For endovascular patients with CTP/MRP core volume >100cc, we will conduct the two-step
stopping rules for mortality after we enroll 20 patients in this group and then conduct
monitoring after every 10 patients in this group (We expect 20% of patients’ CTP/MRP core
volume will >100cc, that is, among 280 endovascular patients, around 56 endovascular patients

                                                61

--- PAGE 62 ---
                2                                                        SELECT 2 Protocol
                                                                         4 August, 2021

are with CTP/MRP core volume >100cc.). Similarly, we assign a weakly informative prior
                       ா      ெ
distribution for both ߨ௠ and ߨ௠ , that is, a beta distribution with two shape parameters at 0.4
and 0.6, which centers at 0.4 with an effective sample size of 1.


The rule of step 1 for mortality in this group can be pre-determined in the following table.
Find your number of endovascular patients with CTP/MRP core volume >100cc in the left-side
column (we provide the table up to 100 patients, but if we enroll more than 100 patients in this
group, we will run the algorithm and identify the # of deaths which will trigger the rule). The
step 1 for mortality will be triggered if the number of deaths is in the range in the right-side
column (the range is inclusive):


 # of patients with CTP/MRP core volume         # of deaths
 >100cc in the endovascular group
 20                                             12-20
 30                                             17-30
 40                                             22-40
 50                                             26-50
 60                                             32-60
 70                                             35-70
 80                                             40-80
 90                                             44-90
 100                                            49-100


For endovascular patients with Extracranial ICA occlusions, we will conduct the two-step
stopping rules for mortality after we enroll 20 patients in this group and then conduct
monitoring after every 10 patients in this group (We expect 10% of patients to have isolated
extracranial ICA occlusion, that is, among 280 endovascular patients, around 28 endovascular
patients are with extracranial ICA occlusions). Similarly, we assign a weakly informative prior

                                                 62

--- PAGE 63 ---
                2                                                        SELECT 2 Protocol
                                                                         4 August, 2021
                       ா      ெ
distribution for both ߨ௠ and ߨ௠ , that is, a beta distribution with two shape parameters at 0.4
and 0.6, which centers at 0.4 with an effective sample size of 1.


The rule of step 1 for mortality in this group can be pre-determined in the following table.
Find your number of endovascular patients with Extracranial ICA occlusions in the left-side
column (we provide the table up to 100 patients, but if we enroll more than 100 patients in this
group, we will run the algorithm and identify the # of deaths which will trigger the rule). The
step 1 for mortality will be triggered if the number of deaths is in the range in the right-side
column (the range is inclusive):


 # of patients with Extracranial ICA            # of deaths
 occlusions
 20                                             12-20
 30                                             17-30
 40                                             22-40
 50                                             26-50
 60                                             32-60
 70                                             35-70
 80                                             40-80
 90                                             44-90
 100                                            49-100


These rules only serve as guides and do not substitute for the independent decision-making of
the DSMB in the determination of whether the study should be stopped for safety reasons. The
decision to stop the study will be made by the DSMB after review of all adverse events based
on its own independent decision making. The investigators and the sponsor will not be
informed of the interim grouped results.



                                                 63

--- PAGE 64 ---
                2                                                         SELECT 2 Protocol
                                                                          4 August, 2021

   Imaging Core Lab

All baseline and follow-up CTs, CT-Angiograms (CTAs) and CTP/MRP images will be reviewed by
a central lab core at UTH. Dr. Clark Sitton, Associate Professor, Diagnostic and Interventional
Imaging and Dr. Roy Riascos, Professor, Diagnostic and Interventional Imaging at UT McGovern
Medical School will serve on the imaging core lab. All images will be sent to the central lab core
in a de-identified manner. All radiology interpretations will occur independently of any
knowledge of clinical factors. Blinding of imaging core lab at UT Houston will be ensured. We
have several neuroradiologists at the institute and the neuroradiologist for the core lab will not
participate in the care of a patient enrolled in the trial. Also, the neuroradiologists, while
evaluating images will assess the CT images at a different time than the MRIs. They will also not
be aware of the treatment and other clinical variables.


A) Parenchymal (e.g., non-contrast head CT) Imaging - the ASPECT score will be determined
(baseline study only). Follow up studies will be determined for stroke location as well as for the
presence of any hemorrhage and hemorrhage grading.

B) CT-Angiograms of the head – identify the vessel occlusion location and collateral scoring
system.

C) CTP-Advanced analysis through the RAPID software (RAPID, non-commercial research
version iSchemaView, Inc.) will be utilized to identify potentially salvageable brain tissue. Brain
tissue at risk for infarction will be distinguished from minimally hypo-perfused tissue if the time
to maximum (Tmax) delay is more than 6 seconds. Irreversibly injured brain (hypo-perfused
tissue will be diagnosed if the relative cerebral blood flow is less than 30% of that in normal
tissue.

D) Conventional Angiograms – identify and grade reperfusion using the modified TICI scoring
system.




                                                 64

--- PAGE 65 ---
                2                                                       SELECT 2 Protocol
                                                                        4 August, 2021

   National Data Management Center

Data management and site monitoring will be performed by the University of Texas at Houston
(UTH). The UTH will create the database and set up the interface on the REDCAP where clinical
site personnel will enter the data into the electronic CRF. Data quality assurance processes
include: (1) logic and rule checks built into the database; (2) monitoring by the
Data Manager at the UTH; (3) central monitoring by the statistical programmer at the
UTH; and (4) risk-based source verification monitoring by the Study Coordinators.

   Data Management Plan

Individual data elements will be collected locally and then entered into a password-protected
web-based, secure central database, REDCAP. Biostatistics/Epidemiology/Research Design
(BERD) Core at The University of Texas Health Science Center – Houston will act as the data
coordination center. Data quality will be maintained by establishing a written Data
Management Plan describing all applicable aspects of the data management process including:


Developing a database that meets all verification and validation requirements of FDA rule 21
CFR 11, including reference to all pertinent FDA-provided guidelines;

   x   Developing a Data Clarification Plan which describes

       ¾ Edit check logic for all variables specified,

       ¾ CRF pages referenced by edit check,
       ¾ Types of query responses: manual, site notification and clinical query;

       ¾ Query text;

   x   Establishing a data audit strategy and associated procedures.




                                                65

--- PAGE 66 ---
                2                                                        SELECT 2 Protocol
                                                                         4 August, 2021

The database, housed in a Zone 100 secure server at UT-Houston, will be frozen and data will
be audited prior to database lock by the statistical center. All data will be identified and
subjected to a 100% audit, with all errors corrected.

   Compliant Handling Plan

All treatments will be performed following each stroke center’s local standard of care using
FDA-approved devices and medications. Any individual patient or family member complaints
regarding adverse events or morbidity will be handled locally by each institution’s patient safety
center.


In the event dissemination of protected patient health information (PHI) or any other
confidential information occurs, local investigators are bound to report to their risk
management department as well as the coordinating site and study sponsor. On a case by case
basis, the PI reserves the right to terminate any participating centers if mismanagement of such
data is discovered.

   Data Safety and Monitoring Board

SELECT 2 will have an independent Data and Safety Monitoring Board (DSMB) to oversee study
safety. Patients in both study arms will be assessed for the incidence of stroke-related mortality
at 90 days, the incidence of symptomatic intracranial hemorrhage per SITS-MOST definition
within 24 hours after randomization (defined as a ≥ 4 point worsening of immediate pre-
deterioration NIHSS neurological status vs. post deterioration and associated with brain
hemorrhage), and the incidence of significant neurologic deterioration prior to discharge
(defined as ≥ 4 point worsening of the immediate pre-deterioration NIHSS neurological status
vs. post deterioration and not attributed to sedation). Patients in both arms will also be
assessed for intra-procedural complications including intra-procedural mortality, vessel
perforation, arterial dissection, access site complication requiring surgical repair or blood




                                                 66

--- PAGE 67 ---
                2                                                        SELECT 2 Protocol
                                                                         4 August, 2021

transfusion, embolization and device failure. SAEs will be reported within 24 hours of
awareness of the event.


The DSMB will meet in person or by teleconference, on a semi-annual basis, to monitor the
cumulative safety data during participant follow-up. In no instance will more than 12 months
elapse between DSMB reviews of cumulative safety data after the first participant has been
enrolled. The DSMB will monitor the study according to the guidelines specified in the study
protocol and the operating procedures established at the initial meeting unless the DSMB
determines during the course of the trial that modification of the guidelines is in the best
interest of the study and its participants. The DSMB charter can be found as an attachment to
the protocol.

   Independent Medical Safety Monitor

In addition to the DSMB, an independent Medical Safety Monitor (MSM) will be appointed for
the SELECT2 trial. The independent MSM will not be involved in the study and will not have
conflict of interest. He/she will be responsible for ongoing monitoring of reports of SAEs
submitted by the clinical centers in real time to ensure good clinical practice and to identify
safety concerns quickly. The MSM may suggest protocol modifications to prevent the occurance
of particular AEs, e.g., modifying the protocol to require frequent measurement of laboratory
values predictive of the event or to improve expeditious identification of the SAEs. In the event
of unexpected SAEs or an unduly high rate of SAEs, the MSM will promptly contact the DSMB.
In the event that MSM is unavailable for an extended period of time (i.e., extended vacation,
sabbatical, illness, etc.), a back-up MSM will be nominated by the study PI and approved by the
DSMB.




                                                67

--- PAGE 68 ---
               2                                                        SELECT 2 Protocol
                                                                        4 August, 2021

   Adverse Event Reporting

Consideration of adverse events will hereafter consist of adverse events, serious adverse
events, and adverse device effects, including anticipated adverse device effects and
unanticipated adverse device effects.


   x   Adverse event (AE) is defined as any untoward/undesirable clinical occurrence in a
       clinical investigation of a subject, which does not necessarily have a causal relationship
       with the treatment under investigation. An adverse event can, therefore, be any
       unfavorable and/or unintended sign, symptom, or disease temporally associated with
       the use of a device product, whether or not considered related to the device product.
       Only abnormal laboratory values that are deemed clinically significant by the
       investigator will be classified as adverse events.
   x   Serious adverse event (SAE) is defined as any untoward/undesirable adverse experience
       that results in any of the following outcomes: 1) death; 2) a life-threatening adverse
       experience; 3) inpatient hospitalization or prolongation of existing hospitalization; 4) a
       permanent/persistent or significant disability/incapacity or a congenital anomaly/birth
       defect; 5) important medical events that may not result in death, be life-threatening, or
       require hospitalization may be considered a serious adverse event when, based upon
       appropriate medical judgment, they may jeopardize the subject and may require
       medical or surgical intervention to prevent one of the outcomes listed in this definition.
       This category includes the use of intra-arterial thrombolytics and/or intracranial stents.
   x   Anticipated Adverse Device Effect (AADE) is defined as any adverse effect related to the
       device or procedure, which is identified in the protocol or the instructions for use for
       the device.
   x   Unanticipated Adverse Device Effects (UADEs) is defined as any serious adverse effect
       on health or safety or any life-threatening problem or death caused by, or associated
       with a device, if that effect, problem, or death was not previously identified in nature,
       severity, or degree of incidence in the investigational plan or application, or any other

                                                68

--- PAGE 69 ---
                 2                                                         SELECT 2 Protocol
                                                                           4 August, 2021

       unanticipated serious problem associated with a device that relates to the rights, safety,
       or welfare of subjects.

    Reporting Procedures for All Adverse Events

All Adverse Events, whether or not attributed to the study and/or the devices, observed by the
investigator or reported by the subject, will be recorded from the time of randomization
through Day 90. All recorded adverse events will be provided to the data safety monitoring
board (DSMB) at the time of review for decision-making.


The following attributes will be assigned by the reporting investigator:
1. Description of event
2. Date of onset
3. Date of resolution (if applicable)
4. Seriousness
5. Relationship to the study device and/or procedure(s)
6. Severity
7. Action(s) taken
8. Outcome(s)


Severity is defined as a measure of the intensity of a reaction, effect or experience. The
measurement(s) are described as mild, moderate, severe, life-threatening or death. The event
itself, however, may be of relatively minor medical significance. The severity of Adverse Events
is assessed according to the following index scale:


   x   Mild
   Asymptomatic or mild symptoms; clinical or diagnostic observations only; intervention not
   indicated




                                                69

--- PAGE 70 ---
                  2                                                        SELECT 2 Protocol
                                                                           4 August, 2021

   x   Moderate
   Minimal, local or noninvasive intervention indicated; limiting age-appropriate instrumental
   Activities of Daily Living.
   x   Severe
   Medically significant but not immediately life-threatening; hospitalization or prolongation of
   hospitalization indicated; disabling; limiting self-care Activities of Daily Living.
   x   Life-threatening consequences
   Urgent intervention indicated
   x   Death related to AE


The relationship of an AE to the study device or procedure will be graded as follows:
   x   Unrelated
   x   Unlikely
   x   Reasonable possibility
   x   Definitely


Serious Adverse Events All Serious Adverse Events and Unanticipated Adverse Device Effects
including deaths will be reported to the MSM, the Coordinating Center (McGovern Medical
School) and the FDA, as required.




                                                 70

--- PAGE 71 ---
          2         SELECT 2 Protocol
                    4 August, 2021

Study Design




               71

--- PAGE 72 ---
                2                                                      SELECT 2 Protocol
                                                                       4 August, 2021

References

1. Berkhemer O, Fransen P, Beumer D et al. A Randomized Trial of Intraarterial Treatment for
    Acute Ischemic Stroke. New England Journal of Medicine. 2015;372(1):11-20.
    doi:10.1056/nejmoa1411587

2. Jovin T, Chamorro A, Cobo E et al. Thrombectomy within 8 Hours after Symptom Onset in
    Ischemic Stroke. New England Journal of Medicine. 2015;372(24):2296-2306.
    doi:10.1056/nejmoa1503780

3. Goyal M, Demchuk A, Menon B et al. Randomized Assessment of Rapid Endovascular
    Treatment of Ischemic Stroke. New England Journal of Medicine. 2015;372(11):1019-1030.
    doi:10.1056/nejmoa1414905

4. Saver J, Goyal M, Bonafe A et al. Stent-Retriever Thrombectomy after Intravenous t-PA vs. t-
    PA Alone in Stroke. New England Journal of Medicine. 2015;372(24):2285-2295.
    doi:10.1056/nejmoa1415061

5. Campbell B, Mitchell P, Kleinig T et al. Endovascular Therapy for Ischemic Stroke with
    Perfusion-Imaging Selection. New England Journal of Medicine. 2015;372(11):1009-1018.
    doi:10.1056/nejmoa1414792

6. Nogueira R, Jadhav A, Haussen D et al. Thrombectomy 6 to 24 Hours after Stroke with a
    Mismatch between Deficit and Infarct. New England Journal of Medicine. 2018;378(1):11-
    21. doi:10.1056/nejmoa1706442

7. Albers G, Marks M, Kemp S et al. Thrombectomy for Stroke at 6 to 16 Hours with Selection by
    Perfusion Imaging. New England Journal of Medicine. 2018;378(8):708-718.
    doi:10.1056/nejmoa1713973

8. Powers W, Rabinstein A, Ackerson T et al. 2018 Guidelines for the Early Management of
    Patients With Acute Ischemic Stroke: A Guideline for Healthcare Professionals From the



                                               72

--- PAGE 73 ---
               2                                                       SELECT 2 Protocol
                                                                       4 August, 2021

    American Heart Association/American Stroke Association. Stroke. 2018;49(3).
    doi:10.1161/str.0000000000000158

9. Sarraj A, Hassan A, Gupta R et al. Optimizing Patient Selection For Endovascular Treatment In
    Acute Ischemic Stroke (Select): A Prospective Non-Randomized Multicenter Cohort Study
    Of Imaging Selection - European Stroke Organisation Conference: Late Breaking
    Abstracts. European Stroke Journal. 2018;3(1_suppl):587-620.
    doi:10.1177/2396987318773967

10. Borst J, Berkhemer O, Roos Y et al. Value of Computed Tomographic Perfusion–Based
    Patient Selection for Intra-Arterial Acute Ischemic Stroke Treatment. Stroke.
    2015;46(12):3375-3382. doi:10.1161/strokeaha.115.010564

11. Yoo A, Berkhemer O, Fransen P et al. Effect of baseline Alberta Stroke Program Early CT
    Score on safety and efficacy of intra-arterial treatment: a subgroup analysis of a
    randomised phase 3 trial (MR CLEAN). The Lancet Neurology. 2016;15(7):685-694.
    doi:10.1016/s1474-4422(16)00124-1

12. Logan C, Maingard J, Phan K et al. Borderline Alberta Stroke Programme Early CT Score
    Patients with Acute Ischemic Stroke Due to Large Vessel Occlusion May Find Benefit with
    Endovascular Thrombectomy. World Neurosurgery. 2018;110:e653-e658.
    doi:10.1016/j.wneu.2017.11.068

13. Rebello L, Bouslama M, Haussen D et al. Endovascular Treatment for Patients With Acute
    Stroke Who Have a Large Ischemic Core and Large Mismatch Imaging Profile. JAMA
    Neurology. 2017;74(1):34. doi:10.1001/jamaneurol.2016.3954

14. Campbell B, Majoie C, Albers G et al. Penumbral imaging and functional outcome in patients
    with anterior circulation ischaemic stroke treated with endovascular thrombectomy versus
    medical therapy: a meta-analysis of individual patient-level data. The Lancet Neurology.
    2019;18(1):46-55. doi:10.1016/s1474-4422(18)30314-4



                                               73

--- PAGE 74 ---
                2                                                      SELECT 2 Protocol
                                                                       4 August, 2021

15. Lansberg M, Straka M, Kemp S et al. MRI profile and response to endovascular reperfusion
    after stroke (DEFUSE 2): a prospective cohort study. The Lancet Neurology.
    2012;11(10):860-867. doi:10.1016/s1474-4422(12)70203-x

16. Gupta A, Schaefer P, Chaudhry Z et al. Interobserver Reliability of Baseline Noncontrast CT
    Alberta Stroke Program Early CT Score for Intra-Arterial Stroke Treatment
    Selection. American Journal of Neuroradiology. 2012;33(6):1046-1049.
    doi:10.3174/ajnr.a2942

17. Freidrich B, Monch s, Berndt M et al. Software-Based, Automated Calculation of the ASPECT
    Score In Patients Suffering From Emergent Vessel Occlusions in the Anterior Circulation –
    Clinical Feasibility And Reliability: European Stroke Organisation Conference: Late Breaking
    Abstracts. European Stroke Journal. 2018;3(1_suppl):587-620.
    doi:10.1177/2396987318773967

18. Wolpert SM, Bruckmann H, Greenlee R et al. American Journal of Neuroradiology Jan 1993,
    14 (1) 3-13.

19. Pechlaner R, Knoflach M, Matosevic B et al. Recanalization of Extracranial Internal Carotid
    Artery Occlusion after i.v. Thrombolysis for Acute Ischemic Stroke. PLoS ONE.
    2013;8(1):e55318. doi:10.1371/journal.pone.0055318.

20. Grossberg J, Haussen D, Cardoso F et al. Cervical Carotid Pseudo-Occlusions and False
    Dissections. Stroke. 2017;48(3):774-777. doi:10.1161/strokeaha.116.015427

21. Mazya M, Egido J, Ford G et al. Predicting the Risk of Symptomatic Intracerebral
    Hemorrhage in Ischemic Stroke Treated With Intravenous Alteplase. Stroke.
    2012;43(6):1524-1531. doi:10.1161/strokeaha.111.644815

22. Zaidat O, Yoo A, Khatri P et al. Recommendations on Angiographic Revascularization
    Grading Standards for Acute Ischemic Stroke. Stroke. 2013;44(9):2650-2663.
    doi:10.1161/strokeaha.113.001972


                                               74

--- PAGE 75 ---
                2                                                        SELECT 2 Protocol
                                                                         4 August, 2021

23. Cella D, Lai J, Nowinski C et al. Neuro-QOL: Brief measures of health-related quality of life
    for clinical research in neurology. Neurology. 2012;78(23):1860-1867.
    doi:10.1212/wnl.0b013e318258f744

24. Albers G, Lansberg M, Kemp S et al. A multicenter randomized controlled trial of
    endovascular therapy following imaging evaluation for ischemic stroke (DEFUSE
    3). International Journal of Stroke. 2017;12(8):896-905. doi:10.1177/1747493017701147

25. Lai T, Lavori P, Liao O. Adaptive choice of patient subgroup for comparing two
    treatments. Contemporary Clinical Trials. 2014;39(2):191-200.
    doi:10.1016/j.cct.2014.09.001

26. Lai T, Lavori P, Tsang K. Adaptive enrichment designs for confirmatory trials. Statistics in
    Medicine. 2018;38(4):613-624. doi:10.1002/sim.7946

27. Pocock SJ, Simon R. Sequential treatment assignment with balancing for prognostic factors
    in the controlled clinical tria. Biometrics. 1975;31:103–115

28. Azur MJ, Stuart EA, Frangakis C, et al. Multiple imputation by chained equations: What what
    is it and how does it work? Int J Methods Psychiatr Res. 2011;20:40-49




                                                 75

--- PAGE 76 ---
                2                                                       SELECT 2 Protocol
                                                                        4 August, 2021

Appendix A: Minimization Randomization Algorithm

Randomization will be done in the emergency room using a web-based dynamic randomization
system. Covariate adaptive randomization is planned to be developed and implemented to
balance the distributions of important key baseline variables between the two treatment arms.
The key variables include age (<60, 60-69, 70-79, 80-85 years old), presentation NIHSS (6-9, 10-
15, 16-20, >20), center, clot location (M1, ICA), treatment time window (0-8, 9-16, 17-24
hours from onset to randomization time), CTP/MRP core volume (<50cc, 50-100cc, >100cc),
presence or absence of target mismatch profile (mismatch ratio ≥ 1.8 & mismatch volume ≥
15 cc) and hemisphere (right, left).


The randomization algorithm we are going to implement is the algorithm developed by Pocock
and Simon (1975), i.e., minimization method. Through this algorithm, the assignment of a new
patient to a treatment group is determined so as to minimize the differences between the
groups in terms of these important key baseline variables. Unlike traditional stratified
randomization, the minimization method works toward minimizing the total imbalance for all
factors together instead of considering mutually exclusive subgroups, that is, we will not
creating these mutually exclusive subgroups during the randomization. Therefore, this
approach is not restricted by the number of variables and possible combinations of levels of
balancing factors.




                                                76

--- PAGE 77 ---
                      2                                                        SELECT 2 Protocol
                                                                               4 August, 2021

            Details of the minimization randomization algorithm and its implementation


                                              Part I: Specification
This section provides a general framework for a study with the implementation of the
minimization algorithm proposed by Pocock and Simon (1975).


Assumptions and Notations:
Assume there are ‫ ܭ‬treatments denoted as ܶଵ ǡ ܶଶ ǡ ǥ ǡ ܶ௄ with the randomization ratio as
1:1:…:1.
Assume there are ܵ variables to be balanced in the minimization algorithm denoted as
ܺଵ ǡ ܺଶ ǡ ǥ ǡ ܺௌ .
For the variable ܺ௙ , suppose there are ܳ௙ levels and denote the level of ܺ௙ as ܼ௙ ‫ א‬ሼͳǡ ǥ ǡ ܳ௙ ሽ.


Algorithm:
When a new patient enters to the study, denote the observed level of the variable ܺ௙ for this
patient as ݈௙ , ݂ ൌ ͳǡ ǥ ǡ ܵǤ
Step 1: Calculate the number of existing patients who are at the same level of the variable ܺ௙ as

this patient in treatment ݇, denoted as ܰ௞ ൫ܼ௙ ൌ ݈௙ ൯, ݇ ൌ ͳǡ ǥ ǡ ‫ܭ‬. So we can obtain
ܰଵ ൫ܼ௙ ൌ ݈௙ ൯,ܰଶ ൫ܼ௙ ൌ ݈௙ ൯,…,ܰ௄ ൫ܼ௙ ൌ ݈௙ ൯.


Step 2: Regarding to the variable ܺ௙ , if we assign this patient to treatment ݇, we should have

ܰ௞ ൫ܼ௙ ൌ ݈௙ ൯+1 patients at treatment ݇ who have the same level of the variable ܺ௙ as this
patient. We obtain the amount of imbalance which would arise by assigning the patient to
treatment ݇ as
                     ‫ܫ‬௞ ሺܼ௙ ൌ ݈௙ ሻ ൌ ‫ܦ‬ሺܰଵ ൫ܼ௙ ൌ ݈௙ ൯,…,ܰ௞ ൫ܼ௙ ൌ ݈௙ ൯ ൅ ͳ,…,ܰ௄ ൫ܼ௙ ൌ ݈௙ ൯ሻ.
Here, ‫ܦ‬ሺࢇሻ is a function to measure the amount of variation for any set of non-negative
integers ࢇ. Then we can calculate the overall imbalance for all ܵ variables arising when
assigning the patient to treatment ݇ by taking a weighted average, that is,

                                                       77

--- PAGE 78 ---
                 2                                                          SELECT 2 Protocol
                                                                            4 August, 2021

                              ‫ܩ‬௞ ൌ σௌ௙ୀଵ ‫ݓ‬௙ ‫ܫ‬௞ ൫ܼ௙ ൌ ݈௙ ൯ǡ ݇ ൌ ͳǡ ǥ ǡ ‫ ܭ‬,
where ‫ݓ‬௙ denotes the weight for the variable ܺ௙ .




Step 3: Find ݇ ‫ܩ = כ‬௞ and assign the patient to treatment ݇ ‫ כ‬with the highest probability
                         ௞

among all treatments.
If we consider variance function for ‫ܦ‬, according to Freedman and White (1978), the total
imbalance arising when assigning the patient to treatment ݇ can be simplified as follow
                 ‫ܩ‬௞ ൌ ʹሺσௌ௙ୀଵ ‫ݓ‬௙ ܰ௞ ൫ܼ௙ ൌ ݈௙ ൯ሻȀሺ‫ ܭ‬െ ͳሻ ൅ ܿ‫ݐ݊ܽݐݏ݊݋‬ǡ ݇ ൌ ͳǡ ǥ ǡ ‫ ܭ‬.


Therefore, ݇ ‫ = כ‬σௌ௙ୀଵ ‫ݓ‬௙ ܰ௞ ൫ܼ௙ ൌ ݈௙ ൯
                     ௞



                                Part II: Implementation in SELECT2


Two treatment groups: ܶଵ andܶଶ with 1:1 ratio.
                                       Level                                  Weight
 age                                   <60, 60-69, 70-79, 80-85 years         4
                                       old
 presentation NIHSS                    6-9, 10-15, 16-20, >20                 4
 clot location                         M1, ICA                                3
 treatment time window from            0-8, 9-16, 17-24 hours                 3
 onset to randomization time
 CTP/MRP core volume                   <50cc, 50-100cc, >100cc                2
 Target mismatch profiles              mismatch ratio ≥ 1.8 &
                                       mismatch volume ≥ 15 cc,
                                       mismatch ratio < 1.8 or
                                       mismatch volume < 15 cc or
                                       both

                                                  78

--- PAGE 79 ---
                2                                                        SELECT 2 Protocol
                                                                         4 August, 2021

 hemisphere                            right, left                         1
 center                                                                    1


For the first patient to be enrolled, we assign this patient to one of the treatments using equal
randomization. Then before we assign next patients, we will calculate ‫ܩ‬ଵ and ‫ܩ‬ଶ , if ‫ܩ‬ଵ ൐ ‫ܩ‬ଶ ,
then assign next patient to ܶଶ with a probability ‫݌‬. Here, we set ‫ ݌‬ൌ ͲǤͻ; if ‫ܩ‬ଵ ൌ ‫ܩ‬ଶ, then assign
patient to ܶଶ with probability 0.5; if ‫ܩ‬ଵ ൏ ‫ܩ‬ଶ , then assign patient to ܶଶ with probability=1-‫ ݌‬ൌ
ͲǤͳ.




References
Pocock, S.J. and Simon, R., Sequential treatment assignment with balancing for prognostic
factors in the controlled clinical trial. Biometrics. v31. 103-115.


Pocock, S.J., Allocation of Patients to Treatment in Clinical Trials. Biometrics. v35. 183-197


Freedman, L.S. and White, S.J., On the use of Pocock and Simon's method for balancing
treatment numbers over prognostic factors in the controlled clinical trial. Biometrics. v32. 691-
694




                                                     79

--- PAGE 80 ---
                 2                                                              SELECT 2 Protocol
                                                                                4 August, 2021

Appendix B. Efficacy and futility bounds for interim and final analysis

At the ݈th interim analysis, let ܹ௜௟ be the sum of the ranks of Rankin scores from the
endovascular group in the patient subgroup ȫ௜ , ݆ ൌ ͳǡ ǥ ǡ ‫ܬ‬. In our trial, we defined ‫ ܬ‬ൌ6 groups
with ȫ௃ denotes the entire patient population and ȫଵ ǥ ǡ ȫହ denote the subgroups of G1A,
G1A+G1B, G1A+G1B +G2A, G1A+G1B +G2A +G2B, G1A+G1B +G2A +G2B +G3A, respectively.
The standardized Wilcoxon statistic for patient subgroup ȫ௜ is
                                                                                     ଵȀଶ
                                    ݊௜௟ ൫݊௜௟ ൅ ݊଴௜
                                                ௟
                                                   ൅ ͳ൯     ݊௜௟ ݊଴௜
                                                                 ௟
                                                                    ൫݊௜௟ ൅ ݊଴௜
                                                                            ௟
                                                                               ൅ ͳ൯
                     ܼ௜௟ ൌ ቊܹ௜௟ െ                       ቋȀቊ                         ቋ      ǡ
                                              ʹ                         ͳʹ

where, ݊௜௟ and ݊଴௜
                ௟
                   denote the numbers of patients enrolled into the endovascular group and
medical management group at the ݈th interim analysis, respectively.
At the ݈th interim analysis, we will terminate the trial and claims efficacy for the endovascular
group if the following efficacy bound is crossed, that is,

                                                  ܼ௃௟ ൒ ܾǤ

Otherwise, we will proceed to the subgroup selection if the following futility bound is crossed,
that is,
                                                  ෪
                                                  ܼ௃௟ ൑  ܾ෨ǡ

where
                              ௟     ௟    ௟                         ௟ ௟     ௟     ௟             ଵȀଶ
              ෪            ݊௜ ൫݊௜ ൅ ݊଴௜ ൅ ͳ൯                  ݊௜ ݊଴௜ ൫݊௜ ൅ ݊଴௜ ൅ ͳ൯
              ܼ௃௟ ൌ ቊܹ௜௟ െ                   െ ݊௜௟ ݊଴௜
                                                    ௟
                                                       ߠቋ Ȁ ቊ                       ቋ                Ǥ
                                   ʹ                                    ͳʹ

When the above criteria is satisfied, a subgroup ‫ܫ‬መ with the largest value of ܼ௜௟ for ݅ ് ‫ ܬ‬is
chosen. The future enrollment of the trial will include patients of this subgroup only, while the
maximum total sample size is still N=560.

Similar to testing the efficacy and futility in the entire population, at stage ݈ ᇱ , we will terminate
the trial and claim efficacy for the endovascular group in this selected subgroup if the following
efficacy bound is crossed
                                                     ᇲ
                                                  ܼூ௟መ ൒ ܾǤ
We may also terminate for futility if

                                                  ܼ෪௟ᇲ    ෨
                                                   ூመ ൑  ܾ Ǥ




                                                     80

--- PAGE 81 ---
                2                                                        SELECT 2 Protocol
                                                                         4 August, 2021

If neither the efficacy nor futility bound for the entire population ever occurs, the trial proceeds
to the final stage and we terminate the trial and claim efficacy for the endovascular group if

                                             ܼ௃௟ୀଷ ൒ ܿǤ

Under our design setting (maximum sample size N=560 and conducting interim analysis at
N=200 and N=380 with type I error at 0.025 and power at 0.9), we obtain ܾ ൌ ʹǤ͸ͲͶǡ ܾ෨ ൌ
െͳǤͺͻ͹ǡ ܿ ൌ ʹǤ͹͹ʹ for our efficacy and futility boundaries. We assume ߠto be the projected
                                                                                                    ଵ
treatment effect given the maximum sample size for testing the hypothesis: ‫ܪ‬଴ ǣ ܲሺܻ ൑ ܺሻ ൌ ,
                                                                                                    ଶ
                    ଵ                                                           ሺ௓భషഀ ା௓భషഁ ሻ
‫ܪ‬஺ ൌ ܲሺܻ ൑ ܺሻ ൌ ൅ ߠ using the fixed-sample-size test and is calculated as                       ൌ
                    ଶ                                                               ξଷே
ͲǤͲ͹ͻͳ . Here, ܻ denotes the Rankin score in the medical management group and ܺ denotes
the Rankin score in the endovascular group. The rationale of this set-up is detailed in section
3.1 of Lai et al (2014).


Reference
Lai T, Lavori P, Liao O. Adaptive choice of patient subgroup for comparing two
treatments. Contemporary Clinical Trials. 2014;39(2):191-200. doi:10.1016/j.cct.2014.09.001

Lai T, Lavori P, Tsang K. Adaptive enrichment designs for confirmatory trials. Statistics in
Medicine. 2018;38(4):613-624. doi:10.1002/sim.7946




                                                 81

--- PAGE 82 ---
               2                                                     SELECT 2 Protocol
                                                                     4 August, 2021

Appendix C. List of Approved Devices to be used in the SELECT2 Protocol:

Stent-Retriever Devices:

   1. K173352 - Trevo ProVue Retriever and Trevo XP ProVue Retriever
   2. K162539 - Solitaire 2 Revascularization Device
   3. K173452 - EmboTrap II Revascularization Device
   4. K203219 - Trevo XP ProVue Retriever, Trevo NXT ProVue Retriever
   5. K193576 - Solitaire Platinum and Solitaire X Revascularization Devices
   6. K193063 - Embotrap III Revascularization Device
   7. K203592 - Tigertriever and Tigertriever 17 Revascularization Device




Aspiration Devices:

   1. K173761 - Penumbra System (Reperfusion Catheter JET 7)
   2. K173200 - SOFIA Plus Aspiration Catheter
   3. K183464 - AXS Universal Aspiration System
   4. K191768 - AXS Vecta Aspiration System
   5. K190338 - Zenith Flex Aspiration System
   6. K193380 - Cerenovus Large Bore Catheter; Cerenovus Aspiration Tubing Set
   7. K201689 - Riptide Aspiration System
   8. K202182 - ZOOM Reperfusion Catheters; ZOOM Aspiration Tubing
   9. K211476 - ZOOM 71 Reperfusion Catheter; ZOOM Aspiration Tubing




                                              82

```
# Support evidence map: trial SAP, DOC-004 pages 1-20

## Scope and provenance

Assigned source: `joi240006supp3_prod_1708623114.99733.pdf`, physical PDF pages 1-20 only. Content role: PLAN (trial Statistical Analysis Protocol/Plan, V1.0.0, Nov. 20, 2022). All 20 pages freshly mapped, using reusable OCR as transcription aid and individually viewing all 20 corresponding source-matched page images. Printed page numbers agree with physical PDF pages. No legacy scientific conclusions were read. Source and reused derivatives were preserved.

Reusable derivatives: `.ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-01.txt` through `page-20.txt`, and the corresponding `pages/page-01.png` through `page-20.png`. Legacy OCR/rendering engine versions are unrecorded, as recorded by the curator. Current inspection: `view_image`, all 20 PNG pages. No new extraction, rendering, or OCR was necessary; direct tools were available per tooling_record.md (Poppler 26.01.0, Tesseract 5.5.0). Compute device: CPU. Fresh-required extraction units: 0; reusable-backed units freshly scientifically mapped: 20; mapped total: 20. No workbook/formula-cache source exists in this assigned PDF scope.

Local TA keys identify evidence relationships for merging; they are neither findings nor candidate IDs. Matching keys name the main-paper quantities to align in downstream review, without claiming a comparison result. This trial SAP describes the parent SELECT 2 trial; analysis-specific SAP content is outside this shard. Pages 21-40, including subgroups, analysis adjustment details, illustrative tables and boundary appendix, are assigned separately and are not inferred here.

## Page coverage

| PDF page | Printed page | Fresh mapping | Quantitative applicability | Local keys |
|---|---:|---|---|---|
| 1 | Cover | COMPLETE | Plan identity/version; no outcome numbers | TA01 |
| 2 | 2 | COMPLETE | Approval/date statement; no outcome numbers | TA02 |
| 3 | 3 | COMPLETE | Contents only; no independent quantitative relationship | TA03 |
| 4 | 4 | COMPLETE | Contents/illustrative figure index only | TA04 |
| 5 | 5 | COMPLETE | Abbreviations and effect-measure identity | TA05 |
| 6 | 6 | COMPLETE | Design, population, timing and eligibility | TA06-TA08 |
| 7 | 7 | COMPLETE | Imaging eligibility, randomization | TA09-TA11 |
| 8 | 8 | COMPLETE | Assessment times, masking, enrichment design | TA12-TA14 |
| 9 | 9 | COMPLETE | Six groups, order/selection, interim rules | TA15-TA17 |
| 10 | 10 | COMPLETE | Sequential decision tree, sample-size input distribution | TA18-TA20 |
| 11 | 11 | COMPLETE | Size/power inputs and complete operating-characteristics table | TA21-TA23 |
| 12 | 12 | COMPLETE | Simulation narrative, actual review/stopping, adjudication | TA24-TA26 |
| 13 | 13 | COMPLETE | Primary, all secondary and first tertiary definitions | TA27-TA31 |
| 14 | 14 | COMPLETE | Remaining tertiary definitions, population/multiplicity/sensitivity | TA32-TA36 |
| 15 | 15 | COMPLETE | Pooling, summary denominators, primary outcome/hypothesis | TA37-TA40 |
| 16 | 16 | COMPLETE | Primary missingness, WMW and transformations | TA41-TA44 |
| 17 | 17 | COMPLETE | Functional independence/ambulation analyses | TA45-TA46 |
| 18 | 18 | COMPLETE | sICH and neurological worsening analyses | TA47-TA48 |
| 19 | 19 | COMPLETE | Worsening continuation, mortality, complications, reperfusion | TA49-TA52 |
| 20 | 20 | COMPLETE | Reperfusion continuation, discharge, early improvement | TA53-TA55 |

## Page 1 — cover and identity

Source: [DOC-004 PDF p. 1](../../../joi240006supp3_prod_1708623114.99733.pdf#page=1).

**TA01 (plan identity).** Title is SELECT 2: A Randomized Controlled Trial to Optimize Patient's Selection for Endovascular Treatment in Acute Ischemic Stroke. Document subtitle: Statistical Analysis Protocol. Version 1.0.0. Global principal investigator Amrou Sarraj. Institutional address is administrative; it supplies no result-relevant population, statistical rule or numeric outcome. No statistical table or figure on this page. Matching key: parent trial SAP identity.

## Page 2 — approval

Source: [DOC-004 PDF p. 2](../../../joi240006supp3_prod_1708623114.99733.pdf#page=2).

**TA02 (plan timing).** Header: SELECT 2 — Statistical Analysis Plan; V1.0.0; Nov. 20, 2022. Statement says the global principal investigator and steering committee reviewed and approved this plan prior to data lock. Signed by principal investigator, steering committee chair, steering committee member and principal statistician. No supplied data-lock date or analysis values here. Matching key: trial plan timing/version. Administrative signatures are not quantitative outcomes.

## Page 3 — contents

Source: [DOC-004 PDF p. 3](../../../joi240006supp3_prod_1708623114.99733.pdf#page=3).

**TA03 (no independent applicable numbers).** Contents locate introduction/aim/population at p. 6, neuroimaging/randomization at p. 7, blinding/design at p. 8, interim analyses p. 9, sample size p. 10, operating characteristics p. 11, 300-patient DSMB review p. 12, outcome definitions p. 13, general analysis principles p. 14, reporting p. 15, subgroup analysis p. 21 and tables/figures p. 22. The 300-patient heading is a locator, with actual disclosure mapped at TA25. No independent statistical result, formula or decision-rule inputs. No inference from contents page pointers.

## Page 4 — contents continuation

Source: [DOC-004 PDF p. 4](../../../joi240006supp3_prod_1708623114.99733.pdf#page=4).

**TA04 (no independent applicable numbers).** Index locates as-treated population p. 22, per-protocol p. 23, exploratory analyses p. 23; illustrative baseline table p. 26, clinical outcome table p. 29, ITT mRS distribution figure p. 32, alternate-population mRS distribution figure p. 33, subgroup forest plot p. 34, CONSORT p. 35, minimization appendix p. 36, efficacy/futility boundary appendix p. 39. Labels imply 90-day mRS and ITT treatment allocation, but actual templates are outside this shard. Administrative acknowledgement/reference index has no result-relevant numeric values.

## Page 5 — terminology keys

Source: [DOC-004 PDF p. 5](../../../joi240006supp3_prod_1708623114.99733.pdf#page=5).

**TA05 (statistical and imaging definitions).** EVT=endovascular thrombectomy; MM=medical management only; ITT=intention to treat; mRS=modified Rankin Scale; WMW=Wilcoxon-Mann-Whitney; ARD=average risk difference; NNT=number needed to treat; GLR=generalized likelihood ratio; CMH=Cochran-Mantel-Haenszel. ASPECTS=Alberta Stroke Program Early CT Score; rCBF=relative cerebral blood flow; ADC=apparent diffusion co-efficient; NIHSS=National Institutes of Health Stroke Scale; sICH=symptomatic intracranial hemorrhage; CTP=CT perfusion; MRP=magnetic resonance perfusion; ICA=internal carotid artery; MCA=middle cerebral artery; MRI=magnetic resonance imaging; ICH=intracranial hemorrhage; DSMB=data safety monitoring board. No numeric estimates or formula. Matching keys: effect measure identity, treatment contrast, imaging definitions.

## Page 6 — trial design and clinical population

Source: [DOC-004 PDF p. 6](../../../joi240006supp3_prod_1708623114.99733.pdf#page=6).

**TA06 (design/aim).** Investigator-initiated phase III, international, multicenter, prospective, randomized, open-label, blinded-endpoint (PROBE), superiority trial; adaptive enrichment, two parallel arms; assignment 1: 1 to EVT plus medical management versus MM alone, secure web interface, follow-up for 1 year after procedure. Aim: efficacy and safety in acute ischemic stroke with anterior circulation MCA M 1 or ICA occlusion, large core by noncontrast CT ASPECTS 3-5, or CTP rCBF<30% lesion volume ≥50 cc, or MRI diffusion ADC<620×10^-6 mm²/s lesion volume ≥50 cc; treated within 0-24 hours from last known well. Matching keys: randomized population, intervention contrast, imaging core definition, time window.

**TA07 (all inclusion criteria).** (1) Adults aged 18-85 with final acute ischemic stroke diagnosis; (2) NIHSS ≥6; (3) last known well to arterial puncture or medical management 0-24 hours; (4) prestroke mRS 0-1; (5) eligible for thrombectomy or MM; (6) signed informed consent; (7) willing to comply with follow-up requirements; (8) anticipated life expectancy ≥3 months. Criteria are plan definitions, not observed counts.

**TA08 (all clinical exclusion criteria).** (1) Cannot undergo CT angiography and/or CT/MR perfusion (examples renal insufficiency or iodine/contrast allergy); (2) psychiatric/medical comorbidity confounding neurological assessment; (3) IV thrombolytic therapy beyond 4.5 hours from last known well; (4) IV thrombolytic therapy 3-4.5 hours after last known well AND any of: age>80, current anticoagulant use, history of both diabetes AND prior stroke, NIHSS>25, ischemic involvement of more than one third of MCA territory; (5) current investigational drug/device study participation. Matching key: selection/population.

Visual/OCR note: OCR `250 cc` means the printed ≥50 cc, not 250 cc; OCR `NIHSS 26` means ≥6. ADC exponent is printed -6 and area unit mm²/s.

## Page 7 — imaging population and allocation

Source: [DOC-004 PDF p. 7](../../../joi240006supp3_prod_1708623114.99733.pdf#page=7).

**TA09 (all imaging inclusion criteria).** (1) ICA or MCA-M 1 large vessel occlusion proven by MRA/CTA; carotid occlusion may be cervical or intracranial, with or without tandem MCA lesions. (2) Large infarct core on ≥1 of: noncontrast CT ASPECTS 3-5; CTP rCBF<30% lesion ≥50 cc; MRI-DWI ADC<620×10^-6 mm²/s lesion ≥50 cc. Matching keys: ischemic core definition, ASPECTS strata, core-volume thresholds.

**TA10 (all imaging exclusion criteria).** (1) Both noncontrast CT ASPECTS 6-10 AND perfusion core<50 cc; (2) noncontrast CT very large core, ASPECTS ≤2; (3) intracranial tumor except small meningioma, acute intracranial hemorrhage, neoplasm or arteriovenous malformation; (4) significant mass effect with midline shift; (5) flow-limiting ICA dissection or aortic dissection; (6) intracranial stent in same vascular territory precluding safe deployment/removal of device; (7) acute symptomatic arterial occlusions in >1 vascular territory on CTA/MRA, examples bilateral MCA or MCA plus basilar; (8) established infarct and large cerebral edema on noncontrast CT. Visual/OCR note: printed ASPECTS ≤2, not OCR `<2`; printed CT perfusion ≥50 cc, not OCR `>50 cc`.

**TA11 (randomization).** Central REDCap module; Pocock-Simon minimization with biased coin; balances marginal distributions of stratification factors; predetermined factor weights measure imbalance and treatment assignment probability is largest for arm with smallest imbalance. Factor/weight details explicitly deferred to Appendix A (outside shard). Training for assessors in NIHSS/mRS; no additional quantitative assessment rule on page. Matching key: allocation and stratification.

## Page 8 — assessment times and adaptive design

Source: [DOC-004 PDF p. 8](../../../joi240006supp3_prod_1708623114.99733.pdf#page=8).

**TA12 (assessment schedule).** Baseline NIHSS, premorbid mRS, demographics, medical and previous stroke history, cerebral imaging. Follow-up at 24 hours, 5-7 days, 30 days, 90 days, 1 year unless death; functional outcome assessors blinded to treatment and imaging. Institutions receive reimbursement, participants receive no payment; no relevant monetary quantities are given.

**TA13 (masking).** Open-label treatment; functional assessors blinded to allocation/imaging. Only DSMB accesses interim results. Other statisticians use dummy data until code validated and full data released after enrollment, follow-up and collection complete and dataset locked. Matching key: endpoint masking/statistical access.

**TA14 (adaptive design definition).** Extension of group-sequential design with enrichment; two interim analyses and one final analysis for efficacy/futility; may stop early for efficacy or reallocate future accrual to most promising subgroup if overall futility triggered at interim (or final). GLR statistic (Kullback-Leibler criterion) identifies subgroup balancing size and treatment effect. Uses CT ASPECTS, CTP core and time window. Background DEFUSE 3 timing 6-16 hours is historical context, not SELECT 2 inclusion window. Matching key: adaptive design and subgroup selection.

## Page 9 — group partition and interim decision tree

Source: [DOC-004 PDF p. 9](../../../joi240006supp3_prod_1708623114.99733.pdf#page=9).

**TA15 (six disjoint groups).** Group 1: ASPECTS 3-5 and CTP/MRP core<50 cc. Group 2: ASPECTS 6-10 and core≥50 cc. Group 3: ASPECTS 3-5 and core≥50 cc. Each divided into A early 0-12 hours and B late 12-24 hours: G1A, G1B, G2A, G2B, G3A, G3B. Expected EVT effect decreases in that order, highest G1A and lowest G3B. Matching keys: ASPECTS/core strata and early/late interaction.

**TA16 (five enrichment alternatives).** Compare GLR among cumulative sets G1A; G1A+G1B; G1A+G1B+G2A; G1A+G1B+G2A+G2B; G1A+G1B+G2A+G2B+G3A to select most promising subgroup if needed at interim (or final). Full population contains all six groups. Match key: adaptive subgroup selection.

**TA17 (planned analyses).** Interim analyses after enrollment and 90-day follow-up completion of 200 and 380 patients; primary 90-day mRS distribution. Overall one-sided Type I error controlled at 2.5%; efficacy boundary determines stop. Futility boundary determines overall continuation, subgroup accrual/testing, or complete stop. After subgroup selection maximum analyzed n becomes random and less than fixed maximum 560, with easier futility stop. Appendix B has actual boundaries, not given on this page. First 200-patient analysis: neither boundary crossed→continue; efficacy crossed→stop/declare overall efficacy; futility crossed→select optimal GLR subgroup and test it, with neither boundary→continue limited to subgroup. Branches continue on p. 10. Matching keys: stopping/multiplicity/sample size.

## Page 10 — decision-tree continuation and hypothesized distribution

Source: [DOC-004 PDF p. 10](../../../joi240006supp3_prod_1708623114.99733.pdf#page=10).

**TA18 (remaining interim/final rules).** Selected subgroup efficacy crossed→stop/declare subgroup efficacy; subgroup futility crossed→stop for futility. If overall accrual continues, second 380-patient analysis follows same test tree as first. If subgroup only, neither boundary→continue to final with 560−380=180 further subgroup patients; efficacy crossed→stop/declare subgroup efficacy; futility crossed→stop. Final after additional 180 with 90-day follow-up tests either overall population or selected subgroup; efficacy boundary crossed→EVT efficacious; otherwise EVT not superior to standard MM. These are printed plan rules; no observed test statistic on page.

**TA19 (sample-size procedure).** Sample-size rationale Lai, Lavori and Liao (2014), implemented in R package ASSISTant; anticipated distributions based on prior SELECT observations plus expert judgment recognizing nonrandomized design/selection biases. Supplied references remain source-only contextual statements.

**TA20 (complete power-input table, not observed data).** Hypothesized mRS at day 90 in overall population:

| Treatment | mRS 0 | mRS 1 | mRS 2 | mRS 3 | mRS 4 | mRS 5 | mRS 6 | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Endovascular thrombectomy | 4% | 8% | 12% | 16% | 19% | 13% | 28% | 100% |
| Medical management | 1% | 4% | 9% | 14% | 19% | 10% | 43% | 100% |

The table retains separate categories 5 and 6. Primary-analysis category merging is explicitly specified on pp. 14-16; table is an anticipated distribution. Matching key: sample-size effect assumptions. OCR omits much of MM row; all entries above read visually.

## Page 11 — size, power and simulations

Source: [DOC-004 PDF p. 11](../../../joi240006supp3_prod_1708623114.99733.pdf#page=11).

**TA21 (power/n inputs).** Distribution TA20 corresponds to standardized difference 0.34. Nonadaptive fixed sample 376 (188/arm), 90% power, one-sided alpha 2.5%, WMW test. Add 184 for adaptive design, maximum 560. Simulations motivate increase and allow effect shrinkage to 0.30 with reasonable power. Prespecified interim n=200/380. Adaptive n=560, homogeneous effect across six groups, hypothesized standardized difference 0.34: power 91%, overall one-sided Type I error 2.5%. Matching key: primary sample size and alpha.

**TA22 (simulation setup).** 5000 simulated trials comparing adaptive max n=560 with fixed n=560. Standardized effect by normal approximation; 0.32/0.30 are conservative relative to anticipated 0.34. Group proportions G1A, G1B, G2A, G2B, G3A, G3B respectively 14%, 6%, 14%, 6%, 42%, 18%.

**TA23 (complete simulation table).** Column averages are printed values, not newly recomputed estimates. Powers in null row describe Type I error frequency.

| Scenario | G1A | G1B | G2A | G2B | G3A | G3B | Average standardized difference | Adaptive average n randomized | Adaptive power | Fixed n randomized | Fixed power |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| #0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 426 | 2.0% | 560 | 2.5% |
| #1 | 0.32 | 0.32 | 0.32 | 0.32 | 0.32 | 0.32 | 0.32 | 376 | 86.0% | 560 | 95.8% |
| #2 | 0.3 | 0.3 | 0.3 | 0.3 | 0.3 | 0.3 | 0.3 | 393 | 81.1% | 560 | 93.3% |
| #3 | 0.4 | 0.4 | 0.4 | 0.4 | 0 | 0 | 0.16 | 500 | 74.1% | 560 | 45.7% |
| #4 | 0.4 | 0.4 | 0.4 | 0.4 | -0.1 | -0.1 | 0.1 | 502 | 78.5% | 560 | 51.2% |
| #5 | 0.4 | 0.4 | 0.3 | 0.3 | 0 | -0.1 | 0.122 | 513 | 67.1% | 560 | 29.2% |
| #6 | 0.5 | 0.5 | 0 | 0 | 0 | 0 | 0.1 | 503 | 70.6% | 560 | 21.2% |
| #7 | 0.5 | 0 | 0 | 0 | 0 | 0 | 0.07 | 503 | 60.5% | 560 | 12.8% |

Printed narrative below table: under null, total Type I error below 2.5%, early futility stopping 59.1%, average randomizations 426. Uniform difference 0.32 has power 95.8% fixed versus 86.0% adaptive and expected n 560 versus 376. Continuation p. 12. Matching key: simulated operating characteristics. OCR table transcription is incomplete/unusable; numbers above taken from image.

## Page 12 — simulation continuation and actual stopping disclosure

Source: [DOC-004 PDF p. 12](../../../joi240006supp3_prod_1708623114.99733.pdf#page=12).

**TA24 (simulation interpretation).** Uniform effect 0.3 has similar findings; heterogeneous scenarios #3/#4/#5 described as higher power/smaller expected n adaptive. Group 1-only #6: adaptive 70.6% vs fixed 21.2%; G1A-only #7: adaptive 60.5% vs fixed 12.8%. Numerical copies matched to table TA23; these are simulations, not patient results.

**TA25 (DSMB/stopping history as disclosed in plan).** First interim after first 200 completed patients on Feb. 2, 2022; DSMB recommended continue. After external RESCUE JAPAN Limit signal, DSMB requested efficacy/safety review after 300 patients completed 90-day follow-up. Original specified analyses/boundaries were at 200/380. Steering committee decided to give requested data without altering design or adding interim analyses. On Sept. 9, 2022 DSMB reviewed first 300 completed patients plus available 30-day / 90-day outcomes in all patients enrolled until Sept. 1, 2022. Using prespecified interim boundaries, after examining 300 complete 90-day cases, DSMB recommended immediate enrollment stop because efficacy boundary crossed for EVT. Committee stopped recruitment and rejected no-treatment-effect null at family-wise Type I error 0.05. No test statistic, stage-specific numerical boundary or P value is printed on this page. Matching key: actual vs planned interim/stopping and type I error. The plan itself discloses this chronology; do not omit it when matching reporting to plan.

**TA26 (adjudication/data definitions).** Blinded 30-day / 90-day functional assessment; centralized imaging-lab adjudication of CT ASPECTS, occlusion location, core volume, reperfusion, infarct volume/growth; reprocess perfusion centrally when raw images available. If perfusion acquisition suboptimal, core volume estimated by imaging core-lab evaluation of CT hypodensity core. Imaging lab and independent clinical monitor centrally adjudicate hemorrhage category, neurological worsening, procedural complications. Matching keys: core-volume method, safety definitions/adjudication.

## Page 13 — complete outcome hierarchy

Source: [DOC-004 PDF p. 13](../../../joi240006supp3_prod_1708623114.99733.pdf#page=13).

**TA27 (adjudication continuation).** Symptomatic hemorrhage centrally adjudicated by imaging core-lab review and independent clinical monitor.

**TA28 (primary).** 90-day functional outcome measured by mRS score distribution. Matching key: parent trial primary 90-day mRS.

**TA29 (all secondary outcomes, items 1-10).** (1) Functional independence=mRS 0-2 at 90 days. (2) Independent ambulation=mRS 0-3 at 90 days. (3) sICH by SITS-MOST: localPH 2/remotePH hemorrhagic transformation associated with ≥4-point NIHSS increase or death within 24 hours. (4) Neurological worsening=≥4-point NIHSS increase due to stroke itself within 24 hours. (5) Mortality within 90 days. (6) Procedural complications=cumulative incidence of surgical-site hematoma, surgical-site infection, vascular injury caused by endovascular procedure, including peripheral/intracranial dissection, perforation or others. (7) Successful reperfusion in EVT=mTICI≥2 b. (8) Discharge location. (9) Early neurological improvement=NIHSS improvement≥8 points at 24 hours of presentation or NIHSS 0-1. (10) NeuroQOL quality of life at 90 days. Matching keys: outcome status and endpoint thresholds, secondary efficacy/safety.

**TA30 (all secondary outcomes, items 11-14 and footnote).** (11)1-year functional outcome by mRS score; (12)1-year functional independence=mRS 0-2; (13)1-year independent ambulation=mRS 0-3; (14)1-year NeuroQOL. Star applies to all four: unavailable at time of primary manuscript and to be reported later in separate manuscripts. Matching key: 1-year outcome status and availability disclosure.

**TA31 (tertiary, items 1-3).** (1) Infarct volume on MRI-DWI, CT if MRI infeasible, 24 hours to 7 days after randomization. (2) Lesion growth between baseline ischemic core and follow-up infarct. (3) Parenchymal hemorrhage type 2. Continued p. 14. Matching key: infarct/lesion-growth/hemorrhage outcome status.

Visual/OCR notes: NIHSS safety thresholds printed ≥4, improvement printed ≥8; OCR `>4`, `28` are not used. The hierarchy itself contains no observed outcome counts or effect estimates.

## Page 14 — hierarchy continuation and analysis principles

Source: [DOC-004 PDF p. 14](../../../joi240006supp3_prod_1708623114.99733.pdf#page=14).

**TA32 (tertiary items 4-6).** Subarachnoid hemorrhage; hemicraniectomy during index hospitalization; length of hospital stay. Footnote: some or all tertiary outcomes may be reported after primary paper. Matching key: tertiary status and deferred-reporting disclosure.

**TA33 (population and multiplicity).** Analyses based on total 352 recruited before stop described at§7.5. Outcomes/analyses prospectively primary/secondary/tertiary/exploratory. No formal adjustments to overall Type I error for secondary/tertiary/exploratory analyses; they supplement primary evidence and are interpreted in that context. All CIs 95%. Matching keys: ITT n 352 and secondary multiplicity.

**TA34 (ITT strategy).** Primary and all secondary efficacy/safety analyses ITT, randomization arm irrespective of allocated treatment received. Aim collect all outcomes for all randomized subjects. Main analysis retains randomized groups, uses all available outcomes, is valid under named plausible missingness assumption. Tipping-point analysis considers alternative missing outcomes and extreme distribution where primary results change, alternative to MAR. All individuals included in sensitivity analyses. Matching keys: analysis population and missing data.

**TA35 (ordinal category merger).** mRS 6 death merged with mRS 5 bedridden/constant care; avoid counting 6→5 shift as success. Matching key: ordinal outcome definition.

**TA36 (repeat and subgroup analyses).** Key analyses repeated as-treated and per-protocol, details in§11 outside shard. Subgroup analyses regardless of significant overall treatment effect; supplemental characterization; interpretation continues p. 15. Matching keys: sensitivity population and subgroup prespecification.

## Page 15 — pooling, display denominators and primary hypothesis

Source: [DOC-004 PDF p. 15](../../../joi240006supp3_prod_1708623114.99733.pdf#page=15).

**TA37 (pooling/software).** Pool all sites under common clinical protocol, monitoring and central validation; assess poolability by US versus non-US subgroup; details refer to§10.3.4. Primarily Stata and R. These statements do not specify actual model covariates on this page.

**TA38 (CONSORT and baseline conventions).** Report included/withdrawn/lost to follow-up/received allocated treatment/analyzed counts in CONSORT. Discrete baseline variables frequencies/percentages; denominator=patients with available data unless table indicates otherwise. If missing>5%, denominator footnote. Continuous mean(SD) or median(IQR); durations/time intervals median(IQR). Matching keys: displayed denominators and flow/summary conventions.

**TA39 (outcome display and ordinal definition).** Primary/secondary clinical outcomes for both arms in Table 2. Primary mRS distribution atday 90; merge 5/6 because same utility and avoid 6→5 treatment success. Matching key: parent trial outcome display/category merger.

**TA40 (primary null).** Day 90 mRS distribution in EVT does not differ from MM distribution. No superiority margin, adjusted covariate list or model coefficient specified here. Matching key: primary hypothesis.

## Page 16 — primary analysis and missingness

Source: [DOC-004 PDF p. 16](../../../joi240006supp3_prod_1708623114.99733.pdf#page=16).

**TA41 (primary missingness).** Prefer clinic day 90 mRS, otherwise structured telephone interview. All randomized subjects included. MAR means missingness may depend on observed but not missing data; examine important explanatory/auxiliary variables for plausibility. 30 imputations; ordinal logistic regression with explanatory/auxiliary variables to impute mRS; pooled estimates Rubin's rule. Page specifies variable categories without listing individual covariates. Matching key: primary imputation method/count/pooling.

**TA42 (tipping point).** Alternative analysis not relying on MAR; vary missing outcome values and evaluate extreme distribution where primary results change. Matching key: primary sensitivity handling.

**TA43 (WMW primary).** WMW measure of superiority with 95% CI and P value, merging mRS 5/6. Comparator: EVT versus control/MM. Matching key: parent trial primary statistical effect, not an inferred common odds ratio.

**TA44 (all transformations, printed definitions preserved).** ARD described as probability that randomly selected EVT patient has better functional outcome than randomly selected control patient; 95% CI; printed equation ARD=2(WMW−0.5). Average NNT for benefit with 95% CI, NNT=1/ARD. WMW generalized odds with 95% CI, merging mRS 5/6; no generalized-odds formula given. These are transformations expressly planned for comparability. WMW tie handling, CI calculation and individual model adjustment list are not detailed on this page. Matching keys: WMW/ARD/NNT/generalized odds identity and reported measures.

## Page 17 — functional independence and ambulation

Source: [DOC-004 PDF p. 17](../../../joi240006supp3_prod_1708623114.99733.pdf#page=17).

**TA45 (functional independence, secondary).** Proportion with mRS 0-2 atday 90; null no significant proportion difference EVT vs MM. Missing binary indicators derived from imputed 90-day mRS distribution per§10.2.3.1.3, effect estimates pooled Rubin's rule. Report proportion and relative risk with 95% CI/P using modified Poisson regression. Matching key: 90-day mRS 0-2 status/model/imputation.

**TA46 (independent ambulation, secondary).** Proportion with mRS 0-3 atday 90; same no-difference null; missingness like§10.2.3.2.3 functional independence; report proportion plus relative risk 95% CI/P using modified Poisson regression. Matching key: 90-day mRS 0-3 status/model/imputation. No explicit individual covariate list on page.

## Page 18 — sICH and neurological worsening

Source: [DOC-004 PDF p. 18](../../../joi240006supp3_prod_1708623114.99733.pdf#page=18).

**TA47 (sICH, secondary).** Proportion SITS-MOSTsICH within 24 hours. Null similar proportions EVT/MM. MAR assumption; 30 imputations via logistic regression with explanatory/auxiliary variables, pooled Rubin's rule; examine MAR plausibility with collected variables. Report proportion plus relative risk 95% CI/P by modified Poisson regression. Matching key: sICH time/definition and imputation/model.

**TA48 (neurological worsening, secondary).** Proportion with ≥4-point NIHSS increase within 24 hours due to stroke itself. Null similar EVT/MM proportions; missing handling like sICH§10.2.3.4.3 (logistic multiple imputation 30/Rubin). Analysis-method sentence continues p. 19. Matching key: neurological worsening threshold/time/method. Printed≥4 confirmed in both heading and body, despite OCR>4.

## Page 19 — mortality, complications and reperfusion

Source: [DOC-004 PDF p. 19](../../../joi240006supp3_prod_1708623114.99733.pdf#page=19).

**TA49 (neurological worsening continuation).** Proportion and relative risk 95% CI/P by modified Poisson regression. Cross-link TA48.

**TA50 (all-cause mortality, secondary).** Proportion with all-cause death within 90 days; null similar EVT/MM proportions. Missingness like functional independence§10.2.3.2.3 (derive from imputed mRS; Rubin pooling). Report mortality proportion and relative risk 95% CI/P by modified Poisson regression. Matching key: 90-day mortality status/model/missingness.

**TA51 (procedural complications, secondary).** Proportion with cumulative surgical-site hematoma, surgical-site infection, vascular injury (peripheral/intracranial dissection, perforation or other) caused by endovascular procedure. No hypothesis evaluated; missing values not imputed; report count/proportion. Matching key: procedural complication composite/status/descriptive analysis.

**TA52 (successful reperfusion, secondary).** Proportion withmTICIgrade 2 b or higher. Hypothesis/missingness/analysis continuation p. 20. TA29 explicitly restricts reperfusion to EVT group. Matching key: mTICI≥2 b reperfusion definition and population.

## Page 20 — reperfusion, discharge and early improvement

Source: [DOC-004 PDF p. 20](../../../joi240006supp3_prod_1708623114.99733.pdf#page=20).

**TA53 (reperfusion continuation).** No hypothesis evaluated; missing reperfusion not imputed; report successful reperfusion count/proportion. Cross-link TA52. Matching key: reperfusion descriptive analysis.

**TA54 (discharge location, secondary).** Proportions in six categories: (1)home; (2)other acute-care facility; (3)inpatient rehabilitation facility; (4)skilled nursing facility; (5)hospice; (6)in-hospital death. Null discharge-location proportions do not differ significantly EVT/MM. No missing-value imputation. Analysis-method section specifies proportions(%) for all six categories, with no named test in this page. Matching key: discharge status/categories/missingness.

**TA55 (early neurological improvement, secondary).** Proportion with NIHSS improvement≥8 points at 24 hours of presentation OR NIHSS 0-1. Printed hypothesis sentence states that the proportion of patients exhibiting early improvement between EVT/MM, with the comparative predicate omitted; preserve this transcription rather than supplying a test statement. Missingness/analysis continuation outside shard p. 21. Matching key: early improvement endpoint threshold/status. OCR`28` transcribed from visually confirmed≥8.

## Mapping completeness and limitations

All assigned 20 pages contain an explicit inspected record. Cover/approval/contents have identity/administrative applicability only; abbreviations provide identity keys. All result-relevant printed values, planned outcome definitions, composite components, selection criteria, available formulas, power-input distributions and operating-characteristics cells were mapped. There are no observed patient-level outcome result tables in this shard. It contains prospective definitions plus disclosed actual enrollment stopping history (TA25/TA33), which retain PLAN role.

No scientific coverage gap. Reusable engine versions unrecorded; OCR table/inequality transcription was incomplete, resolved by viewing every page image. No fresh derivative gap remains in assigned scope. The exact source remains authority for mechanical evidence recheck. Covariate specifics and numerical efficacy/futility boundaries deferred to separately assigned pp. 21-40; not counted as missing coverage here. No candidate diagnosis or disposition performed.
# Trial SAP support mapping, shard B

## Scope and provenance

- Source: DOC-004, `joi240006supp3_prod_1708623114.99733.pdf`, physical PDF pages 21–40 only; printed page numbers equal physical pages in this shard.
- Document role: PLAN, SELECT 2 Statistical Analysis Plan V1.0.0, November 20, 2022. The CONFIDENTIAL watermark and date/version repeat on pages; no amendment or alternate version is disclosed on these assigned pages.
- Complete fresh scientific mapping of 20/20 assigned units, all reusable-backed; fresh-required extraction units 0; images inspected 20/20. No source, reused asset, or other agent output modified.
- Read each assigned OCR file `review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-NN.txt` and visually inspected each corresponding `pages/page-NN.png` under `.ai_paper_validation/`. Legacy rendering/OCR engine versions unrecorded; no new derivative or OCR produced. CPU device recorded in current tooling record.
- The OCR is only a transcription aid: all quantitative thresholds, labels, and formulas below follow the page image. The assigned units contain no workbook, cached cell values, or spreadsheet formulas.
- Local relationship keys TB01–TB20 below map each page. Matching keys identify concepts for subsequent alignment with main-paper extraction; this shard has no authority to inspect unassigned main-paper pages or diagnose findings.
- Coverage gaps: none. One no-applicable page (p25, references only). Templates on pp26–35 contain illustrative placeholders rather than observed trial data. Formula subscripts and symbols on pp39–40 are recorded as printed, with explicit notation observations; no inference about their statistical consistency is made.

## Page-by-page extraction and relationship map

### TB01 — PDF p21: secondary analyses and subgroup table start

Evidence: [DOC-004 p21](../../../joi240006supp3_prod_1708623114.99733.pdf#page=21). Sections 10.2.3.10.3–10.2.4.

Early neurological improvement missing values follow symptomatic ICH section 10.2.3.4.3, which is outside this shard and must be joined to shard A. Output: proportion exhibiting early neurological improvement, and relative risk with 95% confidence interval and P value using modified Poisson regression. This page continues the early-improvement definition from prior pages; it is not a standalone new definition.

Secondary outcome: quality of life score at 90-day follow-up, measured using NeuroQoL. Outcome measure is the score distribution. Null hypothesis is no significant distribution difference between patients assigned EVT and MM. Missing data are not imputed (printed sentence says “Missing data for length of the quality of life score will not be imputed”). Summary is median (IQR); treatment effect is difference in median values with 95% CI and P value from median regression.

Section 10.2.4 prespecifies repeating primary efficacy, functional independence (mRS 0–2), and independent ambulation (mRS 0–3) analyses within subgroups; effect size and 95% CI appear in Figure 3 forest plot. Visually recovered full table rows, including rows omitted in OCR: age <70/≥70; presentation NIHSS <20/≥20; clot ICA/MCA-M1; time last known well to randomization 0–12/12–24 and 0–6/6–24 (time units supplied by later figure: hours). Matching main-paper keys: early neurological improvement; NeuroQoL; ordinal mRS; binary mRS0–2 and mRS0–3; age/NIHSS/occlusion/time subgroup analyses.

### TB02 — PDF p22: subgroup table continuation; planned displays; as-treated rationale

Evidence: [DOC-004 p22](../../../joi240006supp3_prod_1708623114.99733.pdf#page=22). Sections 10.2.4, 10.2.5, 11.1.

Subgroups continuing TB01:

| Factor | Printed strata/definition |
|---|---|
| Perfusion (rCBF <30%) lesion volume | <70/≥70 ml; <100/≥100 ml; <150/≥150 ml |
| CT ASPECTS | 6–10, 3–5, 0–2, based on core laboratory ASPECTS |
| Perfusion mismatch profile 1 | Ratio ≥1.8 AND volume ≥15 ml, present yes/no |
| Perfusion mismatch profile 2 | Ratio ≥1.2 AND volume ≥10 ml, present yes/no |
| Restricted trial population 1 | Yes/no membership in population excluding (a) ASPECTS6–10 within 6 hours of last known well AND (b) ASPECTS6–10 with rCBF<30% lesion <70 ml within 6–16 hours |
| Restricted trial population 2 | Yes/no membership in population with CT ASPECTS <6 AND perfusion rCBF<30% lesion volume ≥70; unit not printed in this row, figure p34 specifies ml |
| Hemisphere | Right/left |
| Geographic location | US sites/non-US sites |

Planned manuscript: Table1 key baseline by patient group; Table2 primary and key secondary outcomes. Figure1 Grotta stacked bars of each mRS grade by assignment in ITT. Figure2 analogous bars for as-treated and per-protocol. Figure3 primary-outcome subgroup effect sizes with 95% CIs for section10.2.4. Supplementary Figure1 CONSORT flow.

Section11.1 begins rationale that assigned EVT may not be received, e.g. spontaneous symptom resolution between randomization and procedure; continuation p23. Matching keys: imaging strata, mismatch profile, hemisphere/site interaction, analysis population and output status.

### TB03 — PDF p23: alternate populations and exploratory/tertiary imaging analyses

Evidence: [DOC-004 p23](../../../joi240006supp3_prod_1708623114.99733.pdf#page=23). Sections11.1–12.

As-treated rationale continues: no arterial occlusion on baseline angiogram after spontaneous or thrombolysis-induced recanalization; MM-assigned subjects may receive EVT. After study completion, repeat primary Wilcoxon–Mann–Whitney measure of superiority within the adaptive-design sample, classifying patients as treated. Per-protocol includes only subjects meeting every eligibility criterion, imaging eligibility determined by central core laboratory, and receiving randomized treatment.

Section12 title is “Pre-specified exploratory analyses”; text calls the following “pre-specified tertiary analyses” in patients receiving EVT or best medical management and explicitly permits their reporting or nonreporting in the primary trial manuscript. Imaging analyses individually listed:

1. Association between imaging profiles and thrombectomy clinical outcomes/treatment effect.
2. Thrombectomy efficacy by large-core definition: ASPECTS≤5 regardless of core size; ischemic core≥50 mL regardless of CT ASPECTS; ASPECTS≤5 AND core≥50 mL.
3. Functional independence by imaging modality.
4. Heterogeneity of treatment effect by imaging modality.
5. Ceiling effect of core volume on thrombectomy outcomes.
6. Ceiling effect of CT ASPECTS on thrombectomy outcomes.
7. Joint treatment modification by CT ASPECTS and perfusion rCBF<30% lesion volume.
8. Mismatch treatment effects using ratio≥1.8 AND volume≥15 ml; ratio≥1.2 AND volume≥10 ml.
9. Overestimation of baseline perfusion infarct core processed by core laboratory.
10. Total ischemic lesion volume effect on EVT efficacy and safety: union of manually delineated NCCT hypodensity volume and reprocessed CTP rCBF<30% tissue volume when technically feasible; otherwise the larger of these two volumes.
11. Age modification of association between EVT and clinical outcomes.

Matching keys: imaging analysis status; large-core modality definitions; ASPECTS/perfusion continuous and categorical effects; mismatch thresholds; ischemic lesion union/max rule; functional independence; core overestimation. No model, interaction test, spline specification, or multiplicity rule for these tertiary analyses appears on this page.

### TB04 — PDF p24: exploratory/tertiary continuation; administrative material

Evidence: [DOC-004 p24](../../../joi240006supp3_prod_1708623114.99733.pdf#page=24). Section12 continuation.

Effect modifiers individually listed: stroke severity; occlusion location; time to treatment; ischemic core volume; ASPECTS; presence of mismatch; left versus right hemisphere; transfer status. Additional tertiary analyses: workflow; time metrics; EVT cost effectiveness; adjunctive thrombolysis benefit; tandem occlusion presence; tenecteplase versus alteplase; utility-weighted mRS evaluation; discharge location; time to DNR-CC decision in subjects transitioned to comfort care. EVT-treated-only tertiary analyses: anesthesia technique, reperfusion status after thrombectomy, interventional parameters, procedural metrics. Status follows p23: tertiary/exploratory, may or may not be in primary manuscript. No numerical cutoffs, fitted models, or estimated values added here.

Acknowledgment credits randomization implementation and power/operating-characteristic analysis. Start of reference list only; acknowledgment/reference material adds no result-relevant quantitative relationship. Matching keys: interaction analyses and safety/procedural outcomes, utility-weighted mRS, discharge outcomes.

### TB05 — PDF p25: references only, no applicable quantitative relationship

Evidence: [DOC-004 p25](../../../joi240006supp3_prod_1708623114.99733.pdf#page=25). References2–10, including adaptive-design, missing-data, and historical thrombectomy publications. Titles include historical 6–16-hour and 6–24-hour windows, bibliographic year/volume/page/DOI numbers; none specifies a new SELECT2 endpoint, method, count, planned analysis, or trial result. NO_APPLICABLE_RESULT_RELEVANT_CONTENT. No external referenced source consulted.

### TB06 — PDF p26: illustrative Table1 baseline template start

Evidence: [DOC-004 p26](../../../joi240006supp3_prod_1708623114.99733.pdf#page=26). Section15 “Illustrative tables and figures.” Table1 ITT baseline stratified by allocated treatment. Columns Total, allocated EVT+MM (EVT arm), allocated MM only (MM arm); each N=xx, empty numerical cells. These are formatting plans, not observed counts.

Planned rows: age years median[IQR]; sex males/females n(%); history hypertension; congestive heart failure n(%); coronary artery disease n(%); atrial fibrillation n(%); diabetes n(%); transient ischemic attack n(%); stroke n(%); hemisphere right/left n(%); clot ICA, MCA-M1, tandem occlusions n(%); transfer to EVT-capable center n(%); IV thrombolysis total and IV alteplase n(%). Matching key: baseline ITT characteristics and denominator/population labels. Hypertension row has no explicit n(%) label on this page, while most other history rows do.

### TB07 — PDF p27: illustrative Table1 clinical/time rows

Evidence: [DOC-004 p27](../../../joi240006supp3_prod_1708623114.99733.pdf#page=27). Same empty Total/EVT/MM columns. Planned rows: IV tenecteplase n(%); NIHSS at presentation to EVT-capable center median[IQR]; general anesthesia n(%). Time rows all minutes median[IQR]: last known well to randomization; arrival to CT; arrival to CTP; arrival to arterial puncture; puncture to reperfusion/end of procedure. “Imaging parameters” heading continues p28. No observed values. Matching keys: baseline clinical/time metrics, thrombolysis/anesthesia, randomization interval.

### TB08 — PDF p28: illustrative Table1 imaging rows and units

Evidence: [DOC-004 p28](../../../joi240006supp3_prod_1708623114.99733.pdf#page=28). Empty table columns continue. Planned rows all median[IQR]: baseline CT ASPECTS; perfusion rCBF<30% lesion volume ml; tissue Tmax>6s volume ml; tissue Tmax>10s volume ml. Footnote expands NIH, ASPECTS, EVT, IQR, ml. No actual medians or counts. Matching keys: core/penumbra imaging labels, thresholds, milliliter units.

### TB09 — PDF p29: illustrative Table2 ITT clinical outcome template start

Evidence: [DOC-004 p29](../../../joi240006supp3_prod_1708623114.99733.pdf#page=29). Clinical outcomes stratified by assigned treatment. Columns assigned EVT+MM and assigned MM only, each N=xx; effect-size column with 95% CI. Empty result cells.

Planned rows: mRS90-day median[IQR]; functional independence mRS0–2 at90days n(%); independent ambulation mRS0–3 at90days n(%); symptomatic ICH within24hours n(%) marked *; neurological worsening within24hours n(%) marked #; all-cause mortality within90days n(%); procedural complications total n(%). No separate P-value column printed here. Definitions of marked rows appear p31. Matching keys: primary mRS, key binary outcomes, safety and mortality, assigned-arm denominators.

### TB10 — PDF p30: illustrative Table2 safety/procedural/discharge continuation

Evidence: [DOC-004 p30](../../../joi240006supp3_prod_1708623114.99733.pdf#page=30). Empty same arm/effect95%CI columns. Complication subrows: surgical-site hematoma n(%); surgical-site infection n(%); vascular injury due to EVT n(%) marked +. Successful reperfusion mTICI≥2b n(%). Discharge disposition n(%) categories: home; acute-care facility; inpatient rehabilitation; skilled nursing; hospice; in-hospital death. Early neurological improvement n(%) marked $; quality-of-life score begins and continues p31. No observed values. Matching keys: procedural events, mTICI, discharge categories, neurological improvement.

### TB11 — PDF p31: illustrative Table2 definition footnotes

Evidence: [DOC-004 p31](../../../joi240006supp3_prod_1708623114.99733.pdf#page=31). Quality-of-life row continues NeuroQoL median(IQR).

* Symptomatic ICH: parenchymal hemorrhage type2 OR remote parenchymal hemorrhage associated with NIHSS increase≥4 points at24-hour follow-up; SITS-MOST criteria after core laboratory hemorrhagic-transformation adjudication.

# Neurological worsening: NIHSS increase≥4 at24-hour follow-up relative to presentation at EVT-capable center.

+ Vascular injury footnote includes xx peripheral/intracranial dissection patients, xx perforation patients, xx other vascular complication patients; xx placeholders remain.

$ Early neurological improvement: NIHSS improvement≥8 points relative to presentation at EVT-capable center OR NIHSS0–1 at24-hour follow-up. Matching keys: event threshold/time/baseline comparator, safety adjudication, NeuroQoL.

### TB12 — PDF p32: illustrative Figure1 ITT mRS distribution

Evidence: [DOC-004 p32](../../../joi240006supp3_prod_1708623114.99733.pdf#page=32). Figure1 mRS90-day distribution by treatment assignment in ITT. Two bars “ASSIGNED TO EVT ARM”/“ASSIGNED TO MM ARM”; each seven XX segments, legend mRS0,1,2,3,4,5,6. Percent axis0% to100%,10% ticks. XX and equal example widths are illustration, not trial result percentages. Matching key: ordinal mRS distribution, ITT assigned-arm labels.

### TB13 — PDF p33: illustrative Figure2 alternate population mRS

Evidence: [DOC-004 p33](../../../joi240006supp3_prod_1708623114.99733.pdf#page=33). Figure2 mRS90-day distribution in predefined alternate populations. A as-treated bars “RECEIVED EVT”/“RECEIVED MM”; B per-protocol bars “ASSIGNED TO EVT ARM”/“ASSIGNED TO MM ARM”. All seven mRS0–6 segments marked XX. Both percent axes0–100 with10-point ticks. Matching key: analysis-set sensitivity output and treatment reference labels; no observed distribution values.

### TB14 — PDF p34: illustrative Figure3 complete subgroup forest plot

Evidence: [DOC-004 p34](../../../joi240006supp3_prod_1708623114.99733.pdf#page=34). ITT EVT effect across prespecified subgroups, effect size95%CI. All displayed point/CI entries are illustrative 1.00(0.50,2.00), not trial estimates. Axis ticks .4,1,2.5; left “Favors MM”, right “Favors EVT”. Table contains31 rows: age2; NIHSS2; ICA/M1 2; time0–12/12–24 and0–6/6–24 4; rCBF<30% volume70/100/150 thresholds6; CT ASPECTS6–10/3–5/0–2 3; mismatch1.8/15 yes/no2; mismatch1.2/10 yes/no2; restricted population1 yes/no2; restricted population2 yes/no2; hemisphere2; US/non-US2. Definitions exactly match TB01–TB02, with ≥70 ml unit explicit for restricted population2. Matching keys: subgroup forest effect identity/direction; each imaging/time threshold. No actual subgroup sample size, effect estimate, or P value is provided.

### TB15 — PDF p35: illustrative supplementary CONSORT flow

Evidence: [DOC-004 p35](../../../joi240006supp3_prod_1708623114.99733.pdf#page=35). All N= fields blank. Assessed, randomized, excluded: clinical inclusion unmet; clinical exclusion met; imaging inclusion unmet; imaging exclusion met; unable to obtain consent; other. Assignment EVT+MM: received EVT; did not receive EVT with access route unavailable and protocol violation/crossover. Assignment MM: received MM; did not receive MM with protocol violation/crossover. Both lost-to-follow-up boxes: unable to reach; withdrew. Analysis rows: ITT analyzed per arm; as-treated analyzed (EVT box protocol violation/crossover; MM box access route unavailable and violation/crossover); per-protocol analyzed and excluded (ASPECTS6–10 AND core<50 ml; treatment not received as assigned; other). Footnote “Not mutually exclusive.” Matching keys: participant flow, assigned/as-treated/per-protocol populations, imaging eligibility. No real count exists to sum.

### TB16 — PDF p36: AppendixA minimization general framework

Evidence: [DOC-004 p36](../../../joi240006supp3_prod_1708623114.99733.pdf#page=36). K treatments T1…TK, equal1:1:…:1 allocation; S balancing variables X1…XS; variable f has Qf levels, Zf∈{1,…,Qf}, new patient observed level lf. For treatment k, count existing participants Nk(Zf=lf). Hypothetical assignment increments only treatment k count by1. Imbalance Ik(Zf=lf)=D(N1(Zf=lf),…,Nk(Zf=lf)+1,…,NK(Zf=lf)); D measures variation of nonnegative integers. Overall weighted sum Gk=Σ(f=1…S)wfIk(Zf=lf), k1…K; wf is variable weight. Text describes “weighted average”; formula is the printed weighted sum. Matching key: randomization balancing algorithm, analysis stratification variables. This is a planned method formula, not a fitted result.

### TB17 — PDF p37: AppendixA minimization implementation

Evidence: [DOC-004 p37](../../../joi240006supp3_prod_1708623114.99733.pdf#page=37). Step3 chooses k*=argmin(k)Gk and gives highest allocation probability to k*. For variance D, printed Gk=2[ΣwfNk(Zf=lf)]/(K−1)+constant; k*=argmin(k)ΣwfNk(Zf=lf). SELECT2 uses T1/T2 allocation1:1.

| Balancing factor | Printed levels | Weight |
|---|---|---:|
| Age | <60,60–69,70–79,80–85years | 3 |
| Presentation NIHSS | 6–9,10–15,16–20,>20 | 4 |
| Clot location | M1,ICA | 3 |
| Onset to randomization | 0–8,9–16,17–24hours | 3 |
| CTP/MRP core volume | <50cc,50–100cc,101–150,151–200,>200 | 4 |
| Target mismatch profiles | 0,1 | 2 |
| Hemisphere | Right,left | 2 |
| Center | Level cell blank | 1 |
| Physician ASPECTS | 3–4,5–6,7–8,9–10 | 3 |

Image reveals target mismatch/hemisphere/center rows absent in OCR. Matching keys: minimization covariates, weighting, eligibility/core/ASPECTS stratification. Units for third and later core categories follow preceding cc labels.

### TB18 — PDF p38: AppendixA biased allocation probabilities

Evidence: [DOC-004 p38](../../../joi240006supp3_prod_1708623114.99733.pdf#page=38). First patient equal randomization. Subsequent assignments compare G1/G2: if G1>G2, assign T2 probability p=0.9; if G1=G2, assign T2 probability0.5; if G1<G2, assign T2 probability1−p=0.1. Visually confirmed every branch names T2; OCR had different treatment-label transcription in tie/lower branches. Rest consists references; bibliographic numerals add no trial relationship. Matching key: randomized treatment probability and balancing design.

### TB19 — PDF p39: AppendixB adaptive interim/stopping method

Evidence: [DOC-004 p39](../../../joi240006supp3_prod_1708623114.99733.pdf#page=39). J=6 groups; ΠJ entire population; Π1…Π5 respectively G1A; G1A+G1B; +G2A; +G2B; +G3A. Group component definitions are outside this shard. W_i^l is sum of Rankin-score ranks from EVT at interim l, subgroup Π_i. n_i^l and n_0i^l are EVT and MM enrolled numbers at interim l.

Printed standardization: Z_i^l = [W_i^l − n_i^l(n_i^l+n_0i^l+1)/2] / [n_i^l n_0i^l(n_i^l+n_0i^l+1)/12]^(1/2).

Whole-population efficacy stopping: Z_J^l≥b. Otherwise, subgroup selection if tilde(Z_J^l)≤tilde(b). Printed tilde-statistic right-hand side uses W_i^l and n_i^l,n_0i^l subscripts (despite left J): [W_i^l−n_i^l(n_i^l+n_0i^l+1)/2−n_i^l n_0i^l θ] / [n_i^l n_0i^l(n_i^l+n_0i^l+1)/12]^(1/2). Preserve that printed indexing; do not silently substitute J.

Select subgroup hat(i) with largest Z_i^l for i≠J; future enrollment only this subgroup; maximum total N remains560. At later stage l′, selected-subgroup efficacy if Z_hat(i)^(l′)≥b; may stop futility if tilde(Z_hat(i)^(l′))≤tilde(b). No observed interim statistic or operational stopping event is given. Matching keys: adaptive design, ordinal rank direction, interim efficacy/futility, enrichment, group membership, enrollment cap.

### TB20 — PDF p40: AppendixB final boundary and design inputs

Evidence: [DOC-004 p40](../../../joi240006supp3_prod_1708623114.99733.pdf#page=40). If neither whole-population efficacy/futility boundary ever occurs, proceed final stage; claim EVT efficacy if Z_J^(l=3)≥c. Maximum N560; interim N200 and380; typeI error0.025; power0.9. Printed boundaries b=2.604, tilde(b)=−1.897, c=2.772. θ projected treatment effect at maximum sample size. Printed hypotheses: H0:P(Y≤X)=1/2; HA=P(Y≤X)=1/2+θ. Y Rankin score in MM; X Rankin score in EVT. Fixed-sample projected effect θ calculation printed (Z_(1−α)+Z_(1−β))/sqrt(3N)=0.0791. Text attributes rationale to supplied reference citation only; external article not consulted. Remaining references add no SELECT2 quantitative inputs. Matching keys: maximum/sample timing/power/alpha; decision boundaries; WMW probability orientation; primary design effect.

## Cross-page joins and limitations

TB01 early-improvement missing values require section10.2.3.4.3 from shardA; TB01 subgroup repetition requires primary/functional-independence/ambulation methods in shardA. TB02–TB04 preserve planned subgroup versus tertiary/exploratory status for later report comparison. TB06–TB15 are all illustrative output plans, with no observed values. TB16–TB18 contain complete assigned minimization specification; TB19 subgroup labels require earlier-page definitions; TB19–TB20 contain full assigned appendix decision boundaries.

Every assigned unit has a page record; quantitative content is fully mapped without candidate diagnosis. The page25 no-applicable conclusion follows visual inspection. Supplied image/OCR quality is adequate for these records. Final candidate confirmation remains against exact supplied PDF locations. No source-linked extraction gap remains.
