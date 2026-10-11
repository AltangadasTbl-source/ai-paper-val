# Support quantitative evidence: results A

Exact scope: DOC-005 physical PDF pages 1-7 (PLAN), DOC-006 physical PDF pages 1-32 (REPORT). All 39 pages mapped; reusable-backed 39; fresh-required 0; gaps 0. Mapping is rebuilt from supplied factual sources, without candidate diagnosis. Local A identifiers are coordinator-remapping keys; row suffixes identify distinct relationships.

Sources: [analysis SAP](../../../../joi240006supp4_prod_1708623115.00733.pdf#page=1), [results supplement](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=1). Links resolve from this part; coordinator adjusts one directory upward in the merged extraction. All page references below are physical PDF pages; DOC006 printed folio is physical page minus 1 from page2 onward.

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
| DOC005 | 1 | [SAP p1](../../../../joi240006supp4_prod_1708623115.00733.pdf#page=1) |
| DOC005 | 2 | [SAP p2](../../../../joi240006supp4_prod_1708623115.00733.pdf#page=2) |
| DOC005 | 3 | [SAP p3](../../../../joi240006supp4_prod_1708623115.00733.pdf#page=3) |
| DOC005 | 4 | [SAP p4](../../../../joi240006supp4_prod_1708623115.00733.pdf#page=4) |
| DOC005 | 5 | [SAP p5](../../../../joi240006supp4_prod_1708623115.00733.pdf#page=5) |
| DOC005 | 6 | [SAP p6](../../../../joi240006supp4_prod_1708623115.00733.pdf#page=6) |
| DOC005 | 7 | [SAP p7](../../../../joi240006supp4_prod_1708623115.00733.pdf#page=7) |
| DOC006 | 1 | [Results p1](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=1) |
| DOC006 | 2 | [Results p2](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=2) |
| DOC006 | 3 | [Results p3](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=3) |
| DOC006 | 4 | [Results p4](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=4) |
| DOC006 | 5 | [Results p5](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=5) |
| DOC006 | 6 | [Results p6](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=6) |
| DOC006 | 7 | [Results p7](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=7) |
| DOC006 | 8 | [Results p8](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=8) |
| DOC006 | 9 | [Results p9](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=9) |
| DOC006 | 10 | [Results p10](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=10) |
| DOC006 | 11 | [Results p11](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=11) |
| DOC006 | 12 | [Results p12](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=12) |
| DOC006 | 13 | [Results p13](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=13) |
| DOC006 | 14 | [Results p14](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=14) |
| DOC006 | 15 | [Results p15](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=15) |
| DOC006 | 16 | [Results p16](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=16) |
| DOC006 | 17 | [Results p17](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=17) |
| DOC006 | 18 | [Results p18](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=18) |
| DOC006 | 19 | [Results p19](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=19) |
| DOC006 | 20 | [Results p20](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=20) |
| DOC006 | 21 | [Results p21](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=21) |
| DOC006 | 22 | [Results p22](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=22) |
| DOC006 | 23 | [Results p23](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=23) |
| DOC006 | 24 | [Results p24](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=24) |
| DOC006 | 25 | [Results p25](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=25) |
| DOC006 | 26 | [Results p26](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=26) |
| DOC006 | 27 | [Results p27](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=27) |
| DOC006 | 28 | [Results p28](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=28) |
| DOC006 | 29 | [Results p29](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=29) |
| DOC006 | 30 | [Results p30](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=30) |
| DOC006 | 31 | [Results p31](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=31) |
| DOC006 | 32 | [Results p32](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=32) |
