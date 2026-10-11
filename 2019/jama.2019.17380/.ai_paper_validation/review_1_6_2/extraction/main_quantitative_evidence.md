# Main-paper quantitative evidence map

Assigned scope: DOC-001, `jama_de_boer_2019_oi_190122.pdf`, physical pages 1–11 (printed pp.1899–1909), document role REPORT. All 11 reusable-backed units mapped; zero fresh-required units. This artifact records relationships and source statements only, without candidate diagnosis or judgment. Other sources are outside this agent's scope.

Evidence engines: source-matched Poppler `pdftotext -layout` and native text from review_1_5_2; canonical CPU `pdftoppm` rendered pages. Text provenance/fitness and SHA-256 are in the current evidence-asset inventory. No new extraction, rendering, OCR or Python was needed. All 11 layout-text pages read; canonical page images 7, 8, 9 visually inspected for plots, columns, axis labels and table footnotes. Exact source references below are package-root relative; appendix retains every page's complete source-matched layout text, including narrative and footnotes. Appendix text is a transcription aid; direct PDF is final authority. It is not a legacy scientific map.

## Unit completeness

| Physical page | Printed page | Complete assigned contents mapped | Evidence units | Status |
|---|---:|---|---|---|
| 1 | 1899 | Abstract: factorial design, allocations, population, baseline, completion, primary estimates/intervals, safety | N001–N005; S001–S002; appendix p1 | COMPLETE |
| 2 | 1900 | Key Points, background, eligibility, parent design, randomization, interventions, primary-outcome amendment | N006–N010; S003; appendix p2 | COMPLETE |
| 3 | 1901 | All outcome definitions, biomarkers, adherence definitions, power, models, missingness, subgroups, significance rules | N011–N012; S004–S008; appendix p3 | COMPLETE |
| 4 | 1902 | Every participant/retention/adherence/result narrative and matched supplementary pointer | N013–N020; S009–S013; appendix p4 | COMPLETE |
| 5 | 1903 | Table 1: every row, column, units, denominator footnote and conversions | N021–N041; appendix p5 | COMPLETE |
| 6 | 1904 | Figure 1: every flow branch/footnote, safety, PH statement, discussion quantitative claims | N042–N045; S014; appendix p6 | COMPLETE |
| 7 | 1905 | Figure 2: all four panels, participant rows, time/scale/box definitions; discussion claims | N046–N048; S015; appendix p7 | COMPLETE |
| 8 | 1906 | Table 2: every row/footnote; Figure 3: every subgroup, means/SD/counts, plot and interaction P | N049; S016–S032; appendix p8 | COMPLETE |
| 9 | 1907 | Figure 4: every subgroup/plot/P; Table 3: every event/rate/difference/HR/CI/P/footnote | N050; S033–S049; appendix p9 | COMPLETE |
| 10 | 1908 | Subgroup interpretation, missingness and conclusions, disclosures/references | N051; S050; appendix p10 | COMPLETE |
| 11 | 1909 | References only; no applicable current-study quantitative result | No-applicable current-study result; appendix p11 | COMPLETE |

Scientific coverage gaps: None. The graphs do not print numerical coordinates of box quantiles/outliers or forest point/interval endpoints; their graphical values and directions are retained as displays with the stated scale and printed rows, without inventing precision. No raw observations or person-time totals are supplied in the main paper. These are source content limits, not unmapped units.

## Definition and analysis keys for support matching

- Population: 1312 randomized adults with reported physician-diagnosed diabetes; parent VITAL N=25871, men ≥50/women ≥55, no clinically apparent cardiovascular disease/cancer. Ancillary exclusions: gestational-only diabetes; diabetes before age30 plus insulin >20y; known non-diabetes CKD. Individual randomized, 2×2 factorial, four groups, blocks of8 stratified age/sex/race; all receive assigned intervention. Recruitment Nov2011–Mar2014, follow-up completed Dec2017; 50 states, single coordinating center.
- Allocation key: BOTH=370; D-only=333; O-only=289; neither=320. Allocation-derived vitamin-D marginal active=703/placebo=609 and omega-3 marginal active=659/placebo=653 are separately labeled as reconstructed allocation keys, not replacements for printed figure columns. All actual printed figure columns are below.
- D regimen: cholecalciferol2000IU/d for5y. O regimen: fish oil1g/d with EPA465mg+DHA375mg. Limit other supplemental D≤800IU/d; avoid nonstudy fish oil.
- PRIMARY: eGFR change baseline→year5, CKD-EPI creatinine+cystatin C, mL/min/1.73m². Original primary change albuminuria modified in2016 when duration extended to5y (p2).
- SEC-COMP: time to ≥40% baseline eGFR decline OR kidney failure OR death. SEC-EGFR: time to ≥40% baseline eGFR decline. SEC-ACR: baseline→year5 change in urine ACR, both continuous and time to doubling with final ACR≥30mg/g. Three prespecified secondary outcomes as reported pp3/4/9.
- POSTHOC: ≥40% eGFR decline OR kidney failure; analogous ≥30% eGFR decline outcomes (pp3/4/6). Continuous urine ACR main-paper results link eTable6; subgroup urine ACR eFigures2/3; sensitivity urine ACR eTables7–9; posthoc eTable10; adverse eTable11.
- Biosamples baseline,2y,5y; kidney failure yearly questionnaire; cystatin C harmonized after calibrator lot shift to ERM-DA471/IFCC prospective QC; eAppendix explains assay modification. Do not equate pre-harmonized historical values with current eGFR.
- Full analytic population: all randomized by allocation regardless adherence/follow-up; multiple imputation M=20 for missing data including follow-up, Rubin pooling. Complete-case: relevant biosamples baseline+year5. High adherence: study pills at least two-thirds time. Urine sensitivity excludes possible UTI symptoms.
- Continuous model: random participant intercept; baseline/year2/year5 as three unordered time categories; treatment×time; age,sex and each×time; eGFR additionally baseline urine ACR and ACR×time. Year5 treatment×time P tests treatment effect; two-tailed P<.05 each intervention. Secondary end points exploratory due multiple comparisons. R3.6.0.
- Categorical model: Cox PH; HR active/placebo, null1, Schoenfeld residual PH check. eGFR outcomes omit4 missing baseline eGFR, ACR omit1 missing baseline urine ACR (Table3).
- Subgroup model adds subgroup, subgroup×time, subgroup×time×treatment; Wald test of final interaction. Vitamin-D prespecified race/ethnicity,25(OH)D,ACR,eGFR; BMI added after parent cancer interaction. Omega-3 prespecified baseline omega index and CRP; fish intake added after parent cardiovascular interaction. Main Figure4 additionally displays urine ACR. Capture these exact descriptions for plan comparison, without diagnosing them.

## Numeric relationship register

Each identifier tracks a coherent numeric relationship or display family; every constituent row/value is transcribed, so grouping is not sampling. Baseline four-column order throughout: BOTH,D-only,O-only,neither. Default cells No.(%), percentages of nonmissing responses, not automatically randomized denominators.

| ID | Source location | Relationship and exact printed quantities |
|---|---|---|
| N001 | [p1](../../../jama_de_boer_2019_oi_190122.pdf#page=1) abstract design/intervention | N1312;2×2; allocation370,333,289,320;5y;D2000IU/d;O1g/d;50states;Nov2011–Mar2014;Dec2017 completion |
| N002 | p1 results | Mean age67.6y;women46%;minority31%;934(71%) completed |
| N003 | p1 results | Baseline eGFR85.8 SD22.1 mL/min/1.73m² |
| N004 | p1 adverse | Kidney stones58=D32+placebo26;GI bleeding45=O28+placebo17 |
| N005 | p1 matched claims | Primary D and O change/CI match S001–S002 and Table2; narrative no significant interaction |
| N006 | [p2](../../../jama_de_boer_2019_oi_190122.pdf#page=2) Key Points | N1312;5y;D−12.3 vs−13.1;O−12.2 vs−13.1;no significant difference |
| N007 | p2 background/design | Background CKD>25%;parent25871;approximately two-thirds baseline blood;50states;1center |
| N008 | p2 eligibility | Men≥50y;women≥55y;goal1320;exclusion before30y+insulin>20y;gestational diabetes/known other CKD |
| N009 | p2 regimen/randomization | Four factorial groups;D2000IU;capsule1g with EPA465mg+DHA375mg;other D≤800IU/d;blocks8;age/sex/race stratification |
| N010 | p2 outcome amendment | Original primary albuminuria;current primary baseline→year5 eGFR;duration extended5y in2016 |
| N011 | [p3](../../../jama_de_boer_2019_oi_190122.pdf#page=3) outcomes/covariates | Baseline,2y,5y;40% threshold;ACR doubling+≥30mg/g;posthoc30%;adherence≥two-thirds;omega index EPA+DHA as percent total fatty acids |
| N012 | p3 sample size |1320;80%power;difference≥2.3mL/min/1.73m²;two-sidedα.05;80%return;surrogate≥.75/year=≥3.75/5y;preliminary-change distributions referred to plan |
| N013 | [p4](../../../jama_de_boer_2019_oi_190122.pdf#page=4) baseline narrative |Age67.6;median diagnosed-duration6–10y;46%women;31%minority;20%insulin;<10%DPP4 or GLP1;80%antihypertensive;61%RAS;85.8mean eGFR;165(13%)eGFR<60;117(9%)ACR≥30 including24(2%)≥300 |
| N014 | p4 retention blood |1090(83%)≥1 follow-up of1312;934(71%randomized,76%alive)year5 |
| N015 | p4 retention urine |1091(83%)≥1follow-up;945(72%randomized,77%alive)year5 |
| N016 | p4 adherence |D/placebo92%,88%at2/5y;O/placebo91%,89%at2/5y;defined≥two-thirds |
| N017 | p4 medications |DPP4 9%baseline→14%year5;ARB20%→29%;5%initiatedSGLT2;changes similar by group;biguanide/sulfonylurea/insulin/ACE stable |
| N018 | p4 observed overall eGFR |Baseline85.8(SD22.1),year2 80.0(21.5),year5 73.5(21.9) |
| N019 | p4 secondary components |Composite164;80measured≥40%decline;11kidney failure;80deaths;some meet multiple components |
| N020 | p4 urine ACR narrative |Year2 geometric mean5.1CI4.6–5.7mg/g;year5 9.2CI8.4–10.1;approximately3-fold baseline→year5 |
| N021 | [p5](../../../jama_de_boer_2019_oi_190122.pdf#page=5) Table1 denominators |370,333,289,320;all percentages nonmissing responses;race denominators361,327,284,314 |
| N022 | Table1 sex/age |Female184(50),143(43),131(45),151(47);male186(50),190(57),158(55),169(53);age meanSD67.4(7.3),67.4(6.7),68.2(6.7),67.5(6.9)y |
| N023 | Table1 race white/black |White240(66),211(65),199(70),207(66);black73(20),75(23),59(21),71(23) |
| N024 | Table1 remaining race |Hispanic20(6),21(6),16(6),18(6);Asian/Pacific13(4),8(2),7(2),7(2);American Indian/Alaska6(2),4(1),1(<1),2(1);other9(2),8(2),2(1),9(3) |
| N025 | Table1 education |More than high school303(82),283(85),243(84),270(85) |
| N026 | Table1 diabetes duration<1/1–2/3–5y |13(4),15(5),5(2),9(3);52(14),43(13),45(16),37(12);78(21),72(22),62(22),78(24) |
| N027 | Table1 diabetes duration6–10/11–20/>20y |107(29),83(25),74(26),96(30);90(24),82(25),69(24),74(23);29(8),37(11),33(11),25(8) |
| N028 | Table1 smoking/alcohol |Smoking22(6),17(5),15(5),25(8);alcohol191(53),184(56),151(53),168(54) |
| N029 | Table1 biguanides/sulfonylureas |247(67),222(67),199(69),221(69);109(29),100(30),85(29),99(31) |
| N030 | Table1 insulin/TZD |67(18),68(20),57(20),66(21);32(9),32(10),24(8),36(11) |
| N031 | Table1 DPP4/GLP1 |33(9),26(8),22(8),34(11);9(2),14(4),16(6),9(3) |
| N032 | Table1 antihypertensive/countclasses |293(80),263(80),231(81),258(81);class meanSD1.4(1.2),1.4(1.1),1.4(1.1),1.4(1.2) |
| N033 | Table1 ACE-or-ARB/ACE |223(60),205(62),177(61),198(62);163(44),148(44),121(42),133(42) |
| N034 | Table1 diuretic/beta blocker |111(30),87(26),82(28),84(26);91(25),74(22),62(21),68(21) |
| N035 | Table1 calcium blocker/ARB/MRA |75(20),76(23),58(20),66(21);67(18),64(19),60(21),69(22);2(1),3(1),0,4(1) |
| N036 | Table1 lipid medications |250(69),238(73),199(71),223(71) |
| N037 | Table1 supplemental D/calcium |D≥800IU/d146(39),138(41),124(43),128(40);Ca≥1200mg/d84(23),66(20),81(28),81(25) |
| N038 | Table1 BMI/creatinine/cystatin |BMI31.4(6.5),31.8(6.6),30.8(6.6),31.6(7.3)kg/m²;creatinine0.8(.3),.9(.3),.8(.2),.9(.2)mg/dL;cystatinC .9(.3)mg/L all4 |
| N039 | Table1 urine ACR medianIQR |2.9(.5–7.6),2.8(.5–8.8),2.9(.5–7.1),3.2(1.0–6.7)mg/g |
| N040 | Table1 25OH D meanSD/categories |29.6(10.6),29.0(9.8),30.2(10.3),30.1(9.9)ng/mL;<20:62(17),48(15),41(15),44(14);20–<30:109(31),121(38),87(32),116(37);≥30:184(52),148(47),146(53),151(49) |
| N041 | Table1 footnotes |Creatinine×88.4→μmol/L;BMIkg/m²;No.(%)unless otherwise indicated;percentage nonmissing;ACR albumin-creatinine,IQR interquartile |
| N042 | [p6](../../../jama_de_boer_2019_oi_190122.pdf#page=6) Figure1 top |3244assessed;1932excluded=438not criteria+1494declined;1312randomized |
| N043 | Figure1 allocated/returned/completed |370,333,289,320assigned and received;303,280,242,265≥1blood;260,236,212,226completed |
| N044 | Figure1 missing/death/analysis |Lost110,97,77,94;no finalblood89,78,56,75;death21,19,21,19;primary370,333,289,320;complete259,236,211,226;excluded111,97,78,94;all randomized adverse assessment. Two additional baseline missing outside lost groups(first+third);1baseline missing amonglost in second/fourth,footnotes a/b |
| N045 | p6 adverse/discussion |Safety repeatsN004;decline12.7over5y;aging2–3over5y;powered2.3difference |
| N046 | [p7](../../../jama_de_boer_2019_oi_190122.pdf#page=7) Figure2 panelsA/B |Both printed panels:placebo607,459,438;active701,531,496 at0,2,5y. PanelA D,PanelB O. eGFRlinear axis0,50,100,150,200;time0–5. Colors active/placebo, box medians visually decline over time |
| N047 | Figure2 panelsC/D |Both panels:placebo609,463,440;active702,529,505 at0,2,5y. PanelC D,PanelD O. ACRlog axis .1,1,10,100,1000,10000mg/g;time0–5;box medians rise over time |
| N048 | Figure2 caption/discussion |Center median;top/bottom first/third quartiles as printed;whiskersmostextreme within1.5×IQR;circlesbeyond1.5×IQR;counts contributors;3foldACR;priorDtrials51–63participants |
| N049 | [p8](../../../jama_de_boer_2019_oi_190122.pdf#page=8) prior-study narrative |17trials,total626;priorMI2344,19%diabetes;2.1mL/min/1.73m²attenuationover3.3y;CAD262treated1y. Background only |
| N050 | [p9](../../../jama_de_boer_2019_oi_190122.pdf#page=9) discussion |PriorCADdiabetics79;CKDcutoffs eGFR<60/ACR≥30;25OH D<30;normalBMI;notselecteddeficiency/CKD;subgroupnotpowered |
| N051 | [p10](../../../jama_de_boer_2019_oi_190122.pdf#page=10) limitations/conclusions |71%final serum;83%postrandomization serum;primary missingness accounted;completecase similar;5y no significantdifference |

## Inferential-statistical relationship register

All intervals below are printed 95%CI; eGFR quantities use mL/min/1.73m². A graph-only interval is not numerically printed and is not replaced by a calculated crude CI. Subgroup table values are printed column labels followed exactly; the forest estimate separately means adjusted active-minus-placebo change, positive favors active, null0.

| ID | Location | Exact inferential relationship |
|---|---|---|
| S001 | p1 abstract;pp2/4matching;Table2p8 |D change−12.3CI−13.4,−11.2;placebo−13.1CI−14.2,−11.9;difference.9CI−.7,2.5;nonsignificant5y |
| S002 | p1 abstract;pp2/4matching;Table2p8 |Ochange−12.2CI−13.3,−11.1;placebo−13.1CI−14.2,−12.0;difference.9CI−.7,2.6;nonsignificant5y |
| S003 | p2 outcomes |Primary changealbuminuria changedtoeGFRin2016;5yextension disclosed;not slope coefficient |
| S004 | p3 sample size |1320→80%power for≥2.3difference;α.05two-sided;80%followups;preliminarychange distributions in plan;clinicalsurrogate≥.75/year≥3.75/5y |
| S005 | p3 continuous model/test |Randomintercept;3categoricaltimes;treatment×time;age/sex+timeinteraction;baselineACR+timeinteractiononlyeGFR;year5interactionP;2tailedP<.05;secondaryexploratory |
| S006 | p3 missingness/populations |Allrandomized;MI20,Rubin;completecasebaseline+year5;highadherence;ACRexcludeUTIsymptoms |
| S007 | p3 subgroup plan/method |D race/25OHD/ACR/eGFRprespecified;BMIadded;Oomegain­dex/CRPprespecified;fishadded;subgroupmain/time/threewayinteraction;Waldthreewaytest |
| S008 | p3 categorical method |CoxPH;Schoenfeldresidualtest;R3.6.0 |
| S009 | p4 biomarkers |Year2 D25OHD41.4SD11.0vs29.8SD11.1ng/mL,P<.001;Oindex3.6SD1.0%vs2.3SD.8%,P<.001 |
| S010 | p4 overall change |Fullanalytic−12.7CI−13.6,−11.7;932baseline/year5eGFR−12.4CI−13.3,−11.4 |
| S011 | p4 interaction/sensitivity |D×OP.42;primarysensitivitiescompletecase/highadherence similar;no subgroupheterogeneity;year2biomarkerchange notsignificantlycorrelatedwith5yeGFRchange |
| S012 | p4 secondary narrative |3prespecifiednone significant;compositeHRD.92CI.68,1.25;O1.11CI.81,1.50;40%declinenotsignificant;ACRnotreatmentdifference;subgroup/sensitivitysimilar |
| S013 | p4 posthoc narrative |40%decline/kidneyfailureand30%declinecomposites notprespecified;notsignificant;matchesdefinitionp3 |
| S014 | p6 PH/discussion |NostatisticallysignificantPHviolations anysecondary;nosignificantprimary/sensitivity/secondarydifference;5ychange akin eGFRslope |
| S015 | p7 discussion |95%CIsexcluded3.75differenceover5y;insufficientcompositeevents;HRsclose1;secondarynullsupportsprimary;albuminuriaapproximately3fold |
| S016 | Table2p8 Dbaseline |Active n701,eGFR86.3CI84.6–88.0;placebo607,85.3CI83.7–87.0;fourmissingbaseline |
| S017 | Table2 Dyear2 |Active531,80.6CI78.8–82.4;change−5.2CI−6.2,−4.2;placebo459,79.3CI77.3–81.2;change−6.1CI−7.1,−5.1;difference.9CI−.6,2.5;noPprinted |
| S018 | Table2 Dyear5 |Active496,74.3CI72.3–76.2;change−12.3CI−13.4,−11.2;placebo438,72.5CI70.6–74.5;change−13.1CI−14.2,−11.9;difference.9CI−.7,2.5;P.25 |
| S019 | Table2 Obaseline/year2 |Baselineactive657,85.7CI84.1–87.3;placebo651,86.0CI84.2–87.8. Year2active499,79.4CI77.6–81.2;change−5.7CI−6.8,−4.7;placebo491,80.6CI78.6–82.5;change−5.5CI−6.5,−4.6;difference−.3CI−1.8,1.3;noPprinted |
| S020 | Table2 Oyear5/footnotes |Active472,73.7CI71.8–75.6;change−12.2CI−13.3,−11.1;placebo462,73.2CI71.1–75.3;change−13.1CI−14.2,−12.0;difference.9CI−.7,2.6;P.27. Modeledage/sex/baselineACRadjustedMI;changesMIallparticipants;positivehigher/slowerdecline;Ptest5ychange |
| S021 | Figure3p8 overall |Printedplacebo703,−13.1SD14.4;D609,−12.3SD14.8;adjustedforestpositivemarker,intervalspans0 |
| S022 | Figure3 white |Placebo451,−12.1SD13.7;D406,−11.7SD13.5;forestpositive,intervalspans0;raceinteractionP.58sharedblack |
| S023 | Figure3 black |Placebo148,−15.9SD16.0;D130,−14.7SD17.1;forestpositive,intervalspans0;P.58 |
| S024 | Figure3 ACR<30 |Placebo635,−12.4SD14.2;D559,−11.8SD14.4;forestpositive,intervalspans0;ACRinteractionP.36 |
| S025 | Figure3 ACR≥30 |Placebo67,−20.4SD15.0;D50,−17.3SD17.4;forestpositive,intervalspans0;P.36 |
| S026 | Figure3 25OHD<20 |Placebo110,−14.6SD13.9;D85,−12.2SD17.1;forestpositive,intervalspans0;25OHDinteractionP.15 |
| S027 | Figure3 25OHD20–<30 |Placebo230,−14.7SD15.2;D203,−12.4SD14.0;forestpositive,intervalspans0;P.15 |
| S028 | Figure3 25OHD≥30 |Placebo332,−11.5SD13.9;D297,−12.3SD14.6;forestnegative,intervalspans0;P.15 |
| S029 | Figure3 eGFR≥60/<60 |≥60:placebo612,−14.1SD14.4;D531,−13.7SD14.5;positiveforest. <60:placebo89,−5.8SD12.4;D76,−3.0SD13.6;positiveforest. Bothintervalsspannull;interactionP.18 |
| S030 | Figure3 BMI<25/25–<30 |<25:placebo87,−12.9SD13.2;D87,−10.5SD11.7;25–<30:placebo228,−12.3SD14.1;D205,−12.2SD14.4;bothforestpositive,span0;BMIinteractionP.79 |
| S031 | Figure3 BMI≥30 |Placebo364,−13.7SD15.0;D294,−12.8SD15.7;forestpositive,span0;P.79. Source lacks closingparenthesisafter15.0;valuepreserved |
| S032 | Figure3 Oassignment/plotcaption |Oplacebo:printedplacebo333,−13.2SD14.9;D320,−13.0SD14.7;Oactive:printedplacebo370,−12.9SD13.9;D289,−11.7SD14.9;bothpositiveforest,span0;P.42. Plotaxis−4,−2,0,2,4,6,8,10;active−placebo95%CI;adjustedage/sex/baselineACR;baseline→year5 |
| S033 | Figure4p9 overall |Printedplacebo659,−13.1SD14.8;O653,−12.2SD14.5;positiveforest,intervalspans0 |
| S034 | Figure4 EPA/DHA≤2.2% |Placebo332,−13.3SD15.0;O347,−12.5SD14.6;positiveforest,span0;omegaindexinteractionP.72 |
| S035 | Figure4 EPA/DHA>2.2% |Placebo308,−12.9SD14.6;O292,−11.9SD14.4;positiveforest,span0;P.72 |
| S036 | Figure4 ACR<30 |Placebo596,−12.6SD14.8;O598,−11.5SD13.8;positiveforest,span0;ACRinteractionP.70 |
| S037 | Figure4 ACR≥30 |Placebo62,−18.1SD14.2;O55,−19.1SD18.3;markerat/near0,intervalspans0;P.70 |
| S038 | Figure4 hsCRP≤.2mg/dL |Placebo334,−12.9SD14.3;O335,−11.5SD13.4;positiveforest,span0;CRPinteractionP.73 |
| S039 | Figure4 hsCRP>.2mg/dL |Placebo323,−13.3SD15.3;O316,−13.0SD15.5;positiveforest,span0;P.73 |
| S040 | Figure4 fish<1.5servings/week |Placebo354,−13.4SD15.3;O329,−11.8SD14.7;positiveforest,span0;fishinteractionP.51 |
| S041 | Figure4 fish≥1.5servings/week |Placebo295,−12.9SD14.3;O310,−12.7SD14.3;positiveforest,span0;P.51 |
| S042 | Figure4 Dassignment/plotcaption |Dplacebo:printedplacebo289,−13.2SD14.9;O320,−12.9SD13.9;Dactive:printedplacebo370,−13.0SD14.7;O333,−11.7SD14.9;bothpositiveforest,span0;P.42. Axis−6,−4,−2,0,2,4,6;active−placebo95%CI;age/sex/baselineACRadjustment;baseline→year5 |
| S043 | Table3p9 Dcomposite |Eventsactive85/placebo79;ratesper100person-years2.5CI2.0–3.0/2.7CI2.1–3.3;rate difference−.2CI−1.0,.6;HR.92CI.68–1.25;P.61 |
| S044 | Table3 D40%decline |Events42/38;rates1.6CI1.1–2.1/1.7CI1.2–2.1;difference−.1CI−.7,.6;HR.97CI.63–1.51;P.90 |
| S045 | Table3 DACRdoubling+≥30 |Events111/74;rates4.4CI3.6–5.2/3.3CI2.5–4.0;difference1.1CI.0,2.2;HR1.34CI1.00–1.80;P.05 |
| S046 | Table3 Ocomposite |Events86/78;rates2.7CI2.2–3.3/2.5CI1.9–3.0;difference.3CI−.5,1.1;HR1.11CI.81–1.50;P.52 |
| S047 | Table3 O40%decline |Events40/40;rates1.6CI1.1–2.1/1.6CI1.2–2.1;difference.0CI−.7,.7;HR.99CI.64–1.54;P.97 |
| S048 | Table3 OACRdoubling+≥30 |Events96/89;rates4.0CI3.2–4.8/3.7CI3.0–4.5;difference.3CI−.8,1.4;HR1.08CI.81–1.44;P.60 |
| S049 | Table3 labels/footnotes |Prespecifiedsecondary:composite,40%decline,ACRchange;ACRanalyzedtime-doubling≥30here/continuous eTable6;CoxHR;omit4baselineeGFR/1baselineACRmissing;PnullHR1;person-time denominatorsnotprinted |
| S050 | pp9–10 subgroup/conclusion |FavoredDpointestimatesCKD/lowD/normalBMI;CIsnullcrossing;interactionnotsignificant;hypothesisgenerating. Modestmeasurements limit slopes/time-to-event;eventsinsufficient;subgroupnotpowered;missingnessMI+completecase;no5ydifference |

## Matching-occurrence map

Primary D and O claims: abstract p1, Key Points p2, narrative p4, Table2p8, Figure3/4overall p8/9, discussion pp6–7 and conclusion p10. Continuous estimates, measured contributor counts and full-imputed population are separate keys.

Allocation/analysis flow: p1allocation↔Table1p5↔Figure1p6; sample goal1320pp2/3 is a separate planned-size key from actual1312. Baseline summary p1/p4↔Table1; baseline eGFRp4↔Table2; missingbaselinefourFigure1footnotes↔Table2footnoted↔Table3footnoteb.

Retention: abstract934p1↔p4blood934↔Figure1completed934; completecase932p4↔Figure1completecasegroups; Figure2participants are data contributors by panel/time as caption defines. Every printed panel is retained independently.

Categorical composite/40%decline/ACRdoubled: p3definitions↔p4narrative↔Table3p9; Figure1deaths↔p4componentdeaths; componentoverlap explicit. Safety abstractp1↔p6text; both referenceeTable11. Prespecified versus posthoc status: p3↔p4↔Table3a and eTable10pointer. Subgroup definitions: p3↔Figure3/4 and pp9–10 interpretation; figures' adjusted model labels distinct from printed group descriptives.

## Complete page-linked source-matched text appendix

The following text is included to preserve every quantitative occurrence, table row, footnote, matching claim, administrative number and no-applicable reference unit. It was copied from the source-matched reusable layout asset with `awk` form-feed segmentation; no legacy conclusions were read.

### Physical page 1

[Supplied PDF page 1](../../../jama_de_boer_2019_oi_190122.pdf#page=1)

```text
                   Research



                   JAMA | Original Investigation

                   Effect of Vitamin D and Omega-3 Fatty Acid Supplementation
                   on Kidney Function in Patients With Type 2 Diabetes
                   A Randomized Clinical Trial
                   Ian H. de Boer, MD, MS; Leila R. Zelnick, PhD; John Ruzinski, BS; Georgina Friedenberg, MPH; Julie Duszlak, BS;
                   Vadim Y. Bubes, PhD; Andrew N. Hoofnagle, MD, PhD; Ravi Thadhani, MD, MPH; Robert J. Glynn, PhD, ScD;
                   Julie E. Buring, ScD; Howard D. Sesso, ScD, MPH; JoAnn E. Manson, MD, DrPH


                                                                                                                                         Editorial page 1866
                      IMPORTANCE Chronic kidney disease (CKD) is a common complication of type 2 diabetes                                Supplemental content
                      that can lead to end-stage kidney disease and is associated with high cardiovascular risk.
                      Few treatments are available to prevent CKD in type 2 diabetes.                                                    CME Quiz at
                                                                                                                                         jamanetwork.com/learning
                      OBJECTIVE To test whether supplementation with vitamin D3 or omega-3 fatty acids prevents
                      development or progression of CKD in type 2 diabetes.

                      DESIGN, SETTING, AND PARTICIPANTS Randomized clinical trial with a 2 × 2 factorial design
                      conducted among 1312 adults with type 2 diabetes recruited between November 2011 and
                      March 2014 from all 50 US states as an ancillary study to the Vitamin D and Omega-3 Trial
                      (VITAL), coordinated by a single center in Massachusetts. Follow-up was completed in
                      December 2017.

                      INTERVENTIONS Participants were randomized to receive vitamin D3 (2000 IU/d) and
                      omega-3 fatty acids (eicosapentaenoic acid and docosahexaenoic acid; 1 g/d) (n = 370),
                      vitamin D3 and placebo (n = 333), placebo and omega-3 fatty acids (n = 289), or 2 placebos
                      (n = 320) for 5 years.

                      MAIN OUTCOMES AND MEASURES The primary outcome was change in glomerular filtration
                      rate estimated from serum creatinine and cystatin C (eGFR) from baseline to year 5.

                      RESULTS Among 1312 participants randomized (mean age, 67.6 years; 46% women; 31% of
                      racial or ethnic minority), 934 (71%) completed the study. Baseline mean eGFR was 85.8
                      (SD, 22.1) mL/min/1.73 m2. Mean change in eGFR from baseline to year 5 was −12.3 (95% CI,
                      −13.4 to −11.2) mL/min/1.73 m2 with vitamin D3 vs −13.1 (95% CI, −14.2 to −11.9) mL/min/1.73 m2
                      with placebo (difference, 0.9 [95% CI, −0.7 to 2.5] mL/min/1.73 m2). Mean change in
                      eGFR was −12.2 (95% CI, −13.3 to −11.1) mL/min/1.73 m2 with omega-3 fatty acids vs −13.1
                      (95% CI, −14.2 to −12.0) mL/min/1.73 m2 with placebo (difference, 0.9 [95% CI, −0.7
                                                                                                                                     Author Affiliations: Division of
                      to 2.6] mL/min/1.73 m2). There was no significant interaction between the 2 interventions.                     Nephrology, Department of
                      Kidney stones occurred among 58 participants (n = 32 receiving vitamin D3 and n = 26                           Medicine, University of Washington,
                      receiving placebo) and gastrointestinal bleeding among 45 (n = 28 receiving omega-3 fatty                      Seattle (de Boer, Zelnick, Hoofnagle);
                                                                                                                                     Kidney Research Institute, University
                      acids and n = 17 receiving placebo).
                                                                                                                                     of Washington, Seattle (de Boer,
                      CONCLUSIONS AND RELEVANCE Among adults with type 2 diabetes, supplementation with                              Zelnick, Ruzinski); Puget Sound VA
                                                                                                                                     Healthcare System, Seattle,
                      vitamin D3 or omega-3 fatty acids, compared with placebo, resulted in no significant                           Washington (de Boer); Division of
                      difference in change in eGFR at 5 years. The findings do not support the use of vitamin D                      Preventive Medicine, Brigham and
                      or omega-3 fatty acid supplementation for preserving kidney function in patients with                          Women’s Hospital, Boston,
                                                                                                                                     Massachusetts (Friedenberg,
                      type 2 diabetes.
                                                                                                                                     Duszlak, Bubes, Glynn, Buring, Sesso,
                      TRIAL REGISTRATION ClinicalTrials.gov Identifier: NCT01684722                                                  Manson); Department of Laboratory
                                                                                                                                     Medicine, University of Washington,
                                                                                                                                     Seattle (Hoofnagle); Department of
                                                                                                                                     Biomedical Sciences, Cedars-Sinai
                                                                                                                                     Medical Center, Los Angeles,
                                                                                                                                     California (Thadhani); Harvard T. H.
                                                                                                                                     Chan School of Public Health,
                                                                                                                                     Boston, Massachusetts (Glynn,
                                                                                                                                     Buring, Sesso, Manson).
                                                                                                                                     Corresponding Author: Ian H.
                                                                                                                                     de Boer, MD, MS, University of
                                                                                                                                     Washington, 325 Ninth Ave,
                      JAMA. 2019;322(19):1899-1909. doi:10.1001/jama.2019.17380                                                      PO Box 359606, Seattle, WA 98104
                      Published online November 8, 2019. Corrected on June 3, 2020.                                                  (deboer@u.washington.edu).



                                                                                                                                                                (Reprinted) 1899
                                                            © 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.​com by University of Arizona Health Sciences Library user on 08/​24/​2026

```

### Physical page 2

[Supplied PDF page 2](../../../jama_de_boer_2019_oi_190122.pdf#page=2)

```text
                   Research Original Investigation                        Effect of Vitamin D and Omega-3 Fatty Acid Supplementation on Kidney Function in Type 2 Diabetes




                   A
                           mong individuals with type 2 diabetes, chronic kid-
                           ney disease (CKD) is common and associated with poor                  Key Points
                           health outcomes.1 In this population, the prevalence
                                                                                                 Question In adults with type 2 diabetes, do vitamin D or omega-3
                   of CKD (defined as persistently reduced glomerular filtration                 fatty acid supplements help prevent development or progression
                   rate [GFR] or elevated urinary albumin excretion) is more than                of kidney disease?
                   25%, increases with duration of diabetes, and has remained
                                                                                                 Findings In this 2 × 2 factorial randomized clinical trial that
                   relatively stable despite advances in diabetes care.2-4 Type 2
                                                                                                 included 1312 participants with type 2 diabetes, there was no
                   diabetes is the leading cause of end-stage kidney disease                     significant difference in the change in estimated glomerular
                   (ESKD) requiring dialysis or kidney transplant in the United                  filtration rate at 5 years with vitamin D3 supplementation vs
                   States, and among patients with diabetes, CKD is associated                   placebo (−12.3 vs −13.1 mL/min/1.73 m2) or with omega-3 fatty acid
                   with markedly increased risks of cardiovascular events                        supplementation vs placebo (−12.2 vs −13.1 mL/min/1.73 m2).
                   and mortality.5                                                               Meaning These findings do not support the use of vitamin D
                       Vitamin D and omega-3 fatty acid supplements are inter-                   or omega-3 fatty acid supplementation for preserving kidney
                   ventions that may have the potential to prevent the develop-                  function in adults with type 2 diabetes.
                   ment and progression of CKD in type 2 diabetes.6 In animal
                   experimental models, 1,25-dihydroxyvitamin D3 (the active
                   hormone generated from vitamin D3) and its analogues sup-                 protocol available in Supplement 1). The study was approved by
                   press the renin-angiotensin system, reduce kidney inflamma-               the Partners Human Research Committee. Participants provided
                   tion and fibrosis, exert prosurvival effects on podocytes, and            written informed consent and received a stipend.
                   reduce albuminuria and glomerulosclerosis,7,8 while omega-3
                   fatty acids have anti-inflammatory, antithrombotic, and vas-              Study Population
                   cular properties that may help prevent CKD.9 In humans,                   The parent trial enrolled men aged 50 years or older and women
                   lower circulating concentrations of 25-hydroxyvitamin D                   aged 55 years or older without clinically apparent cardiovas-
                   (25[OH]D, used to assess vitamin D sufficiency), lower di-                cular disease or cancer.16 For this study, we recruited poten-
                   etary intake of fish (an important source of omega-3 fatty                tial participants who additionally reported a physician diag-
                   acids), and lower plasma polyunsaturated omega-3 fatty acid               nosis of diabetes at baseline and agreed to provide blood and
                   concentrations have been associated with increased risk                   urine samples.6 We contacted consecutive potentially eli-
                   of albuminuria and GFR decline in many studies.9-12                       gible individuals during the parent trial’s placebo run-in phase
                       However, clinical trials evaluating the kidney effects of             until the enrollment goal of 1320 participants was met. We
                   vitamin D and omega-3 fatty acid supplements have been of                 excluded those who reported a diagnosis of diabetes only dur-
                   short duration, evaluated only urine albumin excretion as an              ing pregnancy, a diagnosis of diabetes prior to age 30 years
                   outcome, or examined kidney outcomes as secondary post hoc                treated with insulin for more than 20 years, or a known cause
                   analyses.12-15 Therefore, the Vitamin D and Omega-3 Trial to              of CKD other than diabetes.
                   Prevent and Treat Diabetic Kidney Disease (VITAL-DKD) was
                   conducted to assess the efficacy and safety of vitamin D and              Interventions
                   omega-3 fatty acids for prevention and treatment of CKD in                As part of the parent trial, participants were randomly as-
                   patients with type 2 diabetes.                                            signed to 1 of 4 treatment groups in a 2 × 2 factorial design:
                                                                                             (1) vitamin D plus omega-3 fatty acids; (2) vitamin D plus pla-
                                                                                             cebo omega-3 fatty acids; (3) omega-3 fatty acids plus placebo
                                                                                             vitamin D; or (4) both placebos.16 Vitamin D3 (cholecalciferol,
                   Methods                                                                   2000 IU) and matching inert placebo were provided by
                   Study Design                                                              Pharmavite LLC. Omega-3 fatty acids (fish oil, 1-g capsules con-
                   This study was designed as an ancillary study to the Vitamin              taining 465 mg of eicosapentaenoic acid [EPA] plus 375 mg of
                   D and Omega-3 Trial (VITAL).6 The parent trial was a random-              docosahexaenoic acid [DHA]) and matching inert placebo were
                   ized, double-blind, placebo-controlled trial of vitamin D and             provided by ProNova. Participants were asked to limit vitamin
                   marine omega-3 fatty acids for primary prevention of cardio-              D intake from all supplemental sources combined to no more
                   vascular disease and cancer (N = 25 871). 16 A single site                than 800 IU/d and to forgo use of nonstudy fish oil supple-
                   (Brigham and Women’s Hospital Department of Preventive                    ments. Randomization occurred from November 2011, through
                   Medicine, Boston, Massachusetts) enrolled participants from               March 2014. Assignments were computer generated in blocks
                   throughout the United States through mail and telephone con-              of 8 stratified by age, sex, and race. Treatment assignments were
                   tacts, dispensed study medications by mail, and ascertained               concealed to both participants and investigators.
                   outcomes remotely. Participants were enrolled from 50 states.
                   Baseline blood samples were collected by the parent trial for             Outcomes
                   approximately two-thirds of participants, with follow-up blood            The primary outcome of this study was change in estimated GFR
                   samples and urine samples collected only among a subset of                (eGFR) from baseline to study year 5. The original primary out-
                   generally healthy participants living in Boston.                          come was change in albuminuria but was modified when the
                       For this study, we enrolled a subset of parent trial participants     study duration was extended to 5 years in 2016, allowing suf-
                   with type 2 diabetes at baseline to ascertain CKD outcomes (trial         ficient time to assess meaningful differences in eGFR.6

           1900    JAMA November 19, 2019 Volume 322, Number 19 (Reprinted)                                                                                     jama.com

                                                         © 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.​com by University of Arizona Health Sciences Library user on 08/​24/​2026

```

### Physical page 3

[Supplied PDF page 3](../../../jama_de_boer_2019_oi_190122.pdf#page=3)

```text
                   Effect of Vitamin D and Omega-3 Fatty Acid Supplementation on Kidney Function in Type 2 Diabetes                       Original Investigation Research



                        Prespecified secondary outcomes included time to the                       sis plan in Supplement 1).6 A difference in change of at least
                   composite outcome of at least a 40% decrease in eGFR from                       2.3 mL/min/1.73 m2 over 5 years was judged by investigators
                   baseline, kidney failure, or death; time to at least a 40% de-                  to include the smallest differences of clinical relevance and
                   crease in eGFR from baseline;17 and change in urine albumin-                    captures changes more recently suggested as a surrogate out-
                   creatinine ratio (ACR) from baseline to study year 5 (analyzed                  come for ESKD (≥0.75 mL/min/1.73 m2 per year, equivalent to
                   as a continuous variable and as time to doubling of urine ACR                   ≥3.75 mL/min/1.73 m2 over 5 years).20,21
                   to a final urine ACR ≥30 mg/g18). Post hoc analyses examined
                   time to a composite outcome of at least a 40% decrease in                       Data Analysis
                   eGFR from baseline or kidney failure as well as outcomes                        We used linear mixed models to summarize changes in
                   using at least a 30% decline in eGFR instead of at least a 40%                  eGFR and urine ACR over time and to test whether these
                   decline in eGFR. Kidney failure was ascertained yearly by ques-                 changes differed by treatment assignment. Random inter-
                   tionnaire. Urine was collected from first morning voids, and                    cepts were included in the linear mixed models to account for
                   albumin and creatinine were measured on a Beckman DXC                           the correlation within participant. Time was modeled as 3 non-
                   chemistry analyzer.6                                                            ordered variables (baseline, year 2, and year 5), with interac-
                        Blood and urine samples were collected by mail prior to                    tion terms included for treatment × time. Terms for linear age,
                   randomization (baseline), 2 years after randomization, and                      sex, and their interactions with time were also included. Mod-
                   5 years after randomization.6 Serum creatinine and cystatin C                   els with eGFR as the outcome additionally adjusted for base-
                   were measured using a modified Jaffe reaction and immuno-                       line urine ACR and its interaction with time. The P value for
                   turbidimetric assay, respectively. Creatinine results are trace-                interaction of treatment with time (year 5) was used to test
                   able to isotope dilution mass spectrometry. A shift in cystatin                 treatment effects. A 2-tailed P < .05 was considered signifi-
                   C values was identified with change in calibrator lot. Cystatin                 cant for each intervention. Because of the potential for type I
                   C concentrations were therefore harmonized across the                           error due to multiple comparisons, findings for analyses of sec-
                   study and to the European Reference Materials (ERM-DA471/                       ondary end points should be interpreted as exploratory.
                   IFCC) using a prospective quality control plan,6 resulting in                        For primary analyses, all participants were analyzed
                   slightly different values than those previously reported                        according to their randomized treatment group, regardless
                   (eAppendix in Supplement 2).6 We calculated eGFR from                           of adherence or follow-up (full analytic population). Multiple
                   the serum concentrations of creatinine and cystatin C using                     imputation (M = 20) was used for missing data, including
                   the Chronic Kidney Disease Epidemiology Collaboration                           missing data for follow-up outcome measurements, to mini-
                   (CKD-EPI) equation.19                                                           mize potential bias due to loss to follow-up; estimates were
                                                                                                   combined across imputations using Rubin rules.22 Second-
                   Covariates                                                                      ary analyses were restricted to participants who returned the
                   Baseline demographics, duration of diabetes, comorbidities,                     relevant biosamples at baseline and year 5 (complete case
                   smoking and alcohol use, weight, and height were ascer-                         population), were restricted to those who reported high
                   tained by self-report. Race and ethnicity were self-reported                    adherence to study medications, or excluded participants
                   by participants using fixed categories to ensure that a diverse                 who reported symptoms of possible urinary tract infection at
                   population was enrolled and to facilitate exploring racial and                  the time of urine collection (for analyses of change in urine
                   ethnic heterogeneity in treatment effects. Body mass index                      albumin excretion only).
                   was calculated as weight divided by height squared. Medica-                          For the vitamin D intervention, prespecified subgroup
                   tion use at baseline and follow-up was ascertained using a                      analyses were defined based on race and ethnicity and base-
                   detailed questionnaire that listed all glucose- and blood                       line 25(OH)D concentrations, urine ACR, and eGFR6; body
                   pressure–lowering medications available at the time of                          mass index was added when the parent trial reported interac-
                   administration, updated throughout the study. Adherence to                      tion by body mass index with regard to incident cancer.23 For
                   study medications was assessed by self-report, with a subset                    the omega-3 fatty acid intervention, prespecified subgroup
                   of highly adherent participants defined as reporting use of                     analyses were defined based on baseline omega-3 index and
                   study medications at least two-thirds of the time. At baseline                  C-reactive protein6; dietary fish intake was added when the
                   and year 2, serum 25(OH)D concentrations and the plasma                         parent trial reported interaction by dietary fish intake with re-
                   omega-3 index (EPA plus DHA as a percentage of total fatty                      gard to cardiovascular events.24 For each of these subgroups,
                   acids) were measured by liquid chromatography–tandem                            we added linear terms for the subgroup, subgroup × time in-
                   mass spectrometry. C-reactive protein was measured on a                         teraction, and subgroup × time × treatment interaction to the
                   Beckman DXC chemistry analyzer.                                                 model used in primary analyses; a Wald test of the subgroup
                                                                                                   × time × treatment coefficient tested whether there was a sig-
                   Sample Size                                                                     nificant interaction in treatment effect. We examined second-
                   A sample of 1320 participants provided 80% power to detect                      ary categorical outcomes using Cox proportional hazards
                   a difference in change in eGFR from baseline to end of study                    models and tested the proportional hazards assumption using
                   of at least 2.3 mL/min/1.73 m2, comparing each active treat-                    Schoenfeld residuals.
                   ment with placebo, at a 2-sided α = .05, assuming distribu-                          All analyses were conducted using the R version 3.6.0
                   tions of change in eGFR observed in preliminary data and                        computing environment (R Foundation for Statistical Com-
                   80% of participants returning follow-up samples (see analy-                     puting).

                   jama.com                                                                                   (Reprinted) JAMA November 19, 2019 Volume 322, Number 19      1901

                                                             © 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.​com by University of Arizona Health Sciences Library user on 08/​24/​2026

```

### Physical page 4

[Supplied PDF page 4](../../../jama_de_boer_2019_oi_190122.pdf#page=4)

```text
                   Research Original Investigation                     Effect of Vitamin D and Omega-3 Fatty Acid Supplementation on Kidney Function in Type 2 Diabetes



                                                                                          −12.4 (95% CI, −13.3 to −11.4) mL/min/1.73 m2 among the 932
                   Results                                                                participants with eGFR data at both baseline and year 5.
                                                                                          Mean change in eGFR from baseline to year 5 was −12.3 (95%
                   Participant Characteristics                                            CI, −13.4 to −11.2) mL/min/1.73 m2 with vitamin D3 vs −13.1
                   At baseline, participants enrolled in this study had a mean age        (95% CI, −14.2 to −11.9) mL/min/1.73 m2 with placebo. Mean
                   of 67.6 years and a median duration of diagnosed diabetes of           change in eGFR was −12.2 (95% CI, −13.3 to −11.1) mL/min/
                   6 to 10 years (Table 1); 46% were women, and 31% were of               1.73 m2 with omega-3 fatty acids vs −13.1 (95% CI, −14.2 to
                   racial or ethnic minority. Biguanides, followed by sulfonyl-           −12.0) mL/min/1.73 m2 with placebo. At year 5, there was no
                   ureas, were the most commonly used glucose-lowering                    significant difference in change in eGFR according to
                   medications, with insulin use reported by 20%. Less than 10%           treatment (0.9 [95% CI, −0.7 to 2.5] mL/min/1.73 m2 compar-
                   of participants reported using a dipeptidyl peptidase 4 inhibi-        ing vitamin D with placebo; 0.9 [95% CI, −0.7 to 2.6] mL/min/
                   tor or glucagon-like peptide 1 receptor agonist, and sodium-           1.73 m 2 comparing omega-3 fatty acids with placebo)
                   glucose cotransporter 2 inhibitors were not yet commercially           (Table 2), and there was no significant interaction between
                   available. Antihypertensive medications were used by 80% of            treatment assignments (P = .42).
                   participants, including 61% using a renin-angiotensin system               Similar results were observed when analyses were re-
                   inhibitor. Mean baseline eGFR was 85.8 mL/min/1.73 m2, and             stricted to participants who provided serum samples at
                   eGFR was less than 60 mL/min/1.73 m2 for 165 participants              baseline and year 5 or to participants who reported consis-
                   (13%). Urine ACR was at least 30 mg/g for 117 participants (9%),       tent high adherence to study medications (eTables 4 and 5 in
                   including 24 (2%) with an ACR of at least 300 mg/g.                    Supplement 2). No significant subgroup heterogeneity was
                                                                                          observed for the effect of either vitamin D or omega-3 fatty
                   Retention and Adherence                                                acids on change in eGFR (Figure 3 and Figure 4). Neither change
                   At least 1 follow-up blood sample was provided by 1090 (83%)           in serum 25(OH)D nor change in omega-3 index from base-
                   of the 1312 participants who were randomized, including 934            line to year 2 significantly correlated with change in eGFR
                   (71% of randomized participants; 76% of those alive) 5 years           from baseline to year 5 (eFigure 1 in Supplement 2).
                   after randomization (Figure 1). At least 1 follow-up urine sample
                   was provided by 1091 participants (83%), including 945 (72%            Secondary Outcomes
                   of randomized participants; 77% of those alive) 5 years after          Of 3 prespecified secondary outcomes, none differed signifi-
                   randomization.                                                         cantly by treatment assignment for either intervention. The
                        Adherence to at least two-thirds of study medications was         composite outcome of at least a 40% decline in eGFR, kidney
                   reported by 92% and 88% of participants at 2 and 5 years, re-          failure, or death occurred in 164 participants (80 with mea-
                   spectively, after randomization for vitamin D (or matching             sured decline in eGFR ≥40%, 11 reporting kidney failure, and
                   placebo) and by 91% and 89%, respectively, at 2 and 5 years            80 deaths, with some participants meeting multiple compo-
                   for omega-3 fatty acids (or matching placebo) (eTable 1 in             nents) and did not differ significantly by treatment assign-
                   Supplement 2). Two years after randomization, mean serum               ment (hazard ratio, 0.92 [95% CI, 0.68-1.25] comparing vita-
                   25(OH)D concentrations were 41.4 (SD, 11.0) ng/mL for par-             min D with placebo; hazard ratio, 1.11 [95% CI, 0.81-1.50]
                   ticipants assigned to vitamin D and 29.8 (SD, 11.1) ng/mL for          comparing omega-3 fatty acids with placebo). The secondary
                   participants assigned to vitamin D placebo (P < .001). Two years       outcome of at least 40% decline in eGFR also did not differ
                   after randomization, mean omega-3 indexes were 3.6% (SD,               significantly by treatment assignment (Table 3).
                   1.0%) for participants assigned to omega-3 fatty acids and                  The geometric mean urine ACR was 5.1 mg/g (95% CI, 4.6-
                   2.3% (SD, 0.8%) for participants assigned to omega-3 fatty acid        5.7 mg/g) at year 2 and 9.2 mg/g (95% CI, 8.4-10.1 mg/g) at year
                   placebo (P < .001).                                                    5 (Figure 2). Urine ACR increased approximately 3-fold from
                        Regardless of treatment assignment, proportions of par-           baseline to year 5, but there was no significant difference in
                   ticipants using biguanides, sulfonylureas, insulin, and                change in urine ACR according to assignment to vitamin D or
                   angiotensin-converting enzyme inhibitors remained rela-                placebo or to omega-3 fatty acids or placebo (Table 3 and
                   tively stable over the course of the study (eTables 2 and 3 in         eTable 6 in Supplement 2). Similar results were observed in rel-
                   Supplement 2). Use of dipeptidyl peptidase 4 inhibitors (9%            evant subgroups, when analyses were restricted to partici-
                   at baseline and 14% at year 5) and angiotensin II receptor             pants who provided urine samples at baseline and year 5, when
                   blockers (20% at baseline and 29% at year 5) increased mod-            analyses were restricted to those reporting consistent adher-
                   estly, and 5% of participants initiated a sodium-glucose               ence to study medications, and when participants who re-
                   cotransporter 2 inhibitor, with similar changes according to           ported symptoms of possible urinary tract infection at the time
                   treatment assignment.                                                  of urine collection were excluded (eFigures 2 and 3 and
                                                                                          eTables 7, 8, and 9 in Supplement 2).
                   Primary Outcome: Change in eGFR
                   Mean eGFR was 85.8 (SD, 22.1) mL/min/1.73 m2 at baseline,              Exploratory and Post Hoc Outcomes
                   80.0 (SD, 21.5) mL/min/1.73 m2 at year 2, and 73.5 (SD, 21.9)          A composite outcome of at least a 40% eGFR decline or kid-
                   mL/min/1.73 m 2 at year 5 (Figure 2). Mean change in                   ney failure as well as composite outcomes including an eGFR
                   eGFR from baseline to year 5 was −12.7 (95% CI, −13.6 to               decline of at least 30% were not prespecified and did not dif-
                   −11.7) mL/min/1.73 m2 in the full analytic population and              fer significantly according to treatment assignment (eTable 10

           1902    JAMA November 19, 2019 Volume 322, Number 19 (Reprinted)                                                                                  jama.com

                                                       © 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.​com by University of Arizona Health Sciences Library user on 08/​24/​2026

```

### Physical page 5

[Supplied PDF page 5](../../../jama_de_boer_2019_oi_190122.pdf#page=5)

```text
                   Effect of Vitamin D and Omega-3 Fatty Acid Supplementation on Kidney Function in Type 2 Diabetes                                      Original Investigation Research




                   Table 1. Baseline Characteristics of Participants in the Vitamin D and Omega-3 Trial to Prevent and Treat Diabetic Kidney Diseasea

                                                                                       Treatment Group, No. (%)
                                                                                       Vitamin D3 and           Vitamin D3               Omega-3 Fatty Acids         Two
                                                                                       Omega-3 Fatty Acids      and Placebo              and Placebo                 Placebos
                    Characteristics                                                    (n = 370)                (n = 333)                (n = 289)                   (n = 320)
                    Demographics
                      Sex
                         Female                                                        184 (50)                     143 (43)             131 (45)                    151 (47)
                         Male                                                          186 (50)                     190 (57)             158 (55)                    169 (53)
                      Age, mean (SD), y                                                67.4 (7.3)                   67.4 (6.7)           68.2 (6.7)                  67.5 (6.9)
                      Race/ethnicity                                                   361                          327                  284                         314
                         Non-Hispanic white                                            240 (66)                     211 (65)             199 (70)                    207 (66)
                         Non-Hispanic black                                            73 (20)                      75 (23)              59 (21)                     71 (23)
                         Hispanic                                                      20 (6)                       21 (6)               16 (6)                      18 (6)
                         Asian/Pacific Islander                                        13 (4)                       8 (2)                7 (2)                       7 (2)
                         American Indian/Alaska Native                                 6 (2)                        4 (1)                1 (<1)                      2 (1)
                         Other                                                         9 (2)                        8 (2)                2 (1)                       9 (3)
                      More than high school education                                  303 (82)                     283 (85)             243 (84)                    270 (85)
                    Medical history and lifestyle
                      Duration of diabetes, y
                         <1                                                            13 (4)                       15 (5)               5 (2)                       9 (3)
                         1-2                                                           52 (14)                      43 (13)              45 (16)                     37 (12)
                         3-5                                                           78 (21)                      72 (22)              62 (22)                     78 (24)
                         6-10                                                          107 (29)                     83 (25)              74 (26)                     96 (30)
                         11-20                                                         90 (24)                      82 (25)              69 (24)                     74 (23)
                         >20                                                           29 (8)                       37 (11)              33 (11)                     25 (8)
                      Current smoking                                                  22 (6)                       17 (5)               15 (5)                      25 (8)
                      Current alcohol use                                              191 (53)                     184 (56)             151 (53)                    168 (54)
                    Medication and supplement use at randomization
                      Glucose-lowering medications
                         Biguanides                                                    247 (67)                     222 (67)             199 (69)                    221 (69)
                         Sulfonylureas                                                 109 (29)                     100 (30)             85 (29)                     99 (31)
                         Insulin                                                       67 (18)                      68 (20)              57 (20)                     66 (21)
                         Thiazolidinediones                                            32 (9)                       32 (10)              24 (8)                      36 (11)
                         Dipeptidyl peptidase 4 inhibitors                             33 (9)                       26 (8)               22 (8)                      34 (11)
                         Glucagon-like peptide 1 receptor agonists                     9 (2)                        14 (4)               16 (6)                      9 (3)
                      Antihypertensive medications                                     293 (80)                     263 (80)             231 (81)                    258 (81)
                         No. of classes, mean (SD)                                     1.4 (1.2)                    1.4 (1.1)            1.4 (1.1)                   1.4 (1.2)
                         ACE inhibitors or ARBs                                        223 (60)                     205 (62)             177 (61)                    198 (62)
                         ACE inhibitors                                                163 (44)                     148 (44)             121 (42)                    133 (42)
                         Diuretics                                                     111 (30)                     87 (26)              82 (28)                     84 (26)
                         β-Blockers                                                    91 (25)                      74 (22)              62 (21)                     68 (21)
                         Calcium channel blockers                                      75 (20)                      76 (23)              58 (20)                     66 (21)
                         Angiotensin II receptor blockers                              67 (18)                      64 (19)              60 (21)                     69 (22)
                         Mineralocorticoid receptor antagonists                        2 (1)                        3 (1)                0                           4 (1)
                      Cholesterol-lowering medications                                 250 (69)                     238 (73)             199 (71)                    223 (71)
                      Supplemental vitamin D (≥800 IU/d) at randomization              146 (39)                     138 (41)             124 (43)                    128 (40)
                      Supplemental calcium (≥1200 mg/d) at randomization               84 (23)                      66 (20)              81 (28)                     81 (25)
                    Physical characteristics
                      Body mass index, mean (SD)b                                      31.4 (6.5)                   31.8 (6.6)           30.8 (6.6)                  31.6 (7.3)
                    Laboratory values at baseline
                      Serum creatinine, mean (SD), mg/dL                               0.8 (0.3)                    0.9 (0.3)            0.8 (0.2)                   0.9 (0.2)
                      Cystatin C, mean (SD), mg/L                                      0.9 (0.3)                    0.9 (0.3)            0.9 (0.3)                   0.9 (0.3)
                      Urine ACR, median (IQR), mg/g                                    2.9 (0.5-7.6)                2.8 (0.5-8.8)        2.9 (0.5-7.1)               3.2 (1.0-6.7)
                      25-hydroxyvitamin D, mean (SD), ng/mL                            29.6 (10.6)                  29.0 (9.8)           30.2 (10.3)                 30.1 (9.9)
                         <20                                                           62 (17)                      48 (15)              41 (15)                     44 (14)
                         20 to <30                                                     109 (31)                     121 (38)             87 (32)                     116 (37)
                         ≥30                                                           184 (52)                     148 (47)             146 (53)                    151 (49)
                                                                                                       a
                   Abbreviations: ACE, angiotensin-converting enzyme; ACR, albumin-creatinine              Data are reported as No. (%) of participants unless otherwise indicated.
                   ratio; IQR, interquartile range.                                                        Percentages are calculated as percentage of nonmissing responses.
                                                                                                       b
                   SI conversion factor: To convert creatinine to μmol/L, multiply by 88.4.                Calculated as weight in kilograms divided by height in meters squared.



                   jama.com                                                                                          (Reprinted) JAMA November 19, 2019 Volume 322, Number 19              1903

                                                                © 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.​com by University of Arizona Health Sciences Library user on 08/​24/​2026

```

### Physical page 6

[Supplied PDF page 6](../../../jama_de_boer_2019_oi_190122.pdf#page=6)

```text
                   Research Original Investigation                                      Effect of Vitamin D and Omega-3 Fatty Acid Supplementation on Kidney Function in Type 2 Diabetes




                   Figure 1. Participant Flow in the Vitamin D and Omega-3 Trial to Prevent and Treat Diabetic Kidney Disease

                                                                                        3244 Potential participants assessed
                                                                                             for eligibility


                                                                                                                 1932 Excluded
                                                                                                                       438 Did not meet inclusion criteria
                                                                                                                      1494 Declined to participate



                                                                                                    1312 Randomized



                        370 Randomized to vitamin D and            333 Randomized to vitamin D                 289 Randomized to placebo                     320 Randomized to 2 placebos
                            omega-3 fatty acids                        and placebo                                 and omega-3 fatty acids                       320 Received intervention as
                            370 Received intervention as               333 Received intervention as                289 Received intervention as                      randomized
                                randomized                                  randomized                                  randomized


                        303 Returned at least 1 blood              280 Returned at least 1 blood               242 Returned at least 1 blood                 265 Returned at least 1 blood
                            sample after randomization                 sample after randomization                  sample after randomization                    sample after randomization


                           260 Completed study                        236 Completed study                         212 Completed study                          226 Completed study
                           110 Lost to follow-up                       97 Lost to follow-up                        77 Lost to follow-up                         94 Lost to follow-up
                               89 Did not provide final                   78 Did not provide final                    56 Did not provide final                     75 Did not provide final
                                  blood sample                               blood sample                                blood sample                                 blood sample
                               21 Died                                    19 Died                                     21 Died                                      19 Died


                         370 Included in primary analysis           333 Included in primary analysis            289 Included in primary analysis             320 Included in primary analysis
                         259 Included in complete case              236 Included in complete case               211 Included in complete case                226 Included in complete case
                             analysis                                   analysis                                    analysis                                     analysis
                         111 Excluded                                97 Excluded (lost to follow-up)a            78 Excluded                                  94 Excluded (lost to follow-up)b
                             110 Lost to follow-up                                                                  77 Lost to follow-up
                                                                    333 Included in assessment of                                                            320 Included in assessment of
                                1 Missing baseline eGFR                 adverse events                                1 Missing baseline eGFR                    adverse events
                         370 Included in assessment of                                                          289 Included in assessment of
                             adverse events                                                                         adverse events


                   eGFR indicates estimated glomerular filtration rate.
                   a
                       Of the 97 lost to follow-up, 1 was also missing baseline eGFR.
                   b
                       Of the 94 lost to follow-up, 1 was also missing baseline eGFR.


                   in Supplement 2). There were no statistically significant                                 gether, these results suggest that neither vitamin D nor omega-3
                   violations of the proportional hazards assumption for any                                 fatty acids have appreciable kidney benefits among the broad
                   secondary outcome.                                                                        population of patients with diagnosed type 2 diabetes.
                                                                                                                  This study assessed change in eGFR over 5 years as the pri-
                   Adverse Events                                                                            mary outcome because this is a clinically relevant outcome with
                   Adverse events were similar comparing both vitamin D and                                  which treatment effects could be assessed with high power.
                   omega-3 fatty acid supplementation with respective place-                                 Progressive GFR decline leads to ESKD, and faster eGFR de-
                   bos (eTable 11 in Supplement 2). For example, kidney stones                               cline—even within the “normal range” of eGFR—is associated
                   occurred among 58 participants (32 receiving vitamin D3 and                               with increased risk of ESKD, cardiovascular events, and death.25
                   26 receiving placebo) and gastrointestinal bleeding occurred                              Change in eGFR over 5 years is akin to eGFR slope, a primary
                   among 45 participants (28 receiving omega-3 fatty acids and                               outcome of many prior clinical trials that meets many criteria
                   17 receiving placebo).                                                                    for a surrogate outcome.20,21
                                                                                                                  In the setting of type 2 diabetes, 5 years is sufficient time
                                                                                                             for substantial eGFR decline to occur with standard treat-
                                                                                                             ments. Mean eGFR in the study population decreased by
                   Discussion                                                                                12.7 mL/min/1.73 m2 over 5 years. This magnitude of eGFR de-
                   Among adults with type 2 diabetes in this randomized clinical                             cline is more than expected with aging alone (2-3 mL/min/
                   trial, neither vitamin D nor omega-3 fatty acid supplementa-                              1.73 m2 over 5 years19) and probably reflects cumulative ef-
                   tion significantly slowed eGFR decline over 5 years. Results were                         fects of relatively long-standing type 2 diabetes. Changes in
                   consistent in sensitivity analyses restricted to participants with                        medications over the course of the study could also affect
                   complete data or to participants who were adherent to study                               change in eGFR, but medication changes were small in this
                   interventions, and secondary outcomes of large changes in                                 study and similar across randomized groups. The study was
                   eGFR and change in urine albumin excretion also showed no                                 powered to detect even modest differences in change in eGFR,
                   statistically significant differences between groups. Alto-                               as little as 2.3 mL/min/1.73 m2, but neither intervention had

           1904    JAMA November 19, 2019 Volume 322, Number 19 (Reprinted)                                                                                                            jama.com

                                                                   © 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.​com by University of Arizona Health Sciences Library user on 08/​24/​2026

```

### Physical page 7

[Supplied PDF page 7](../../../jama_de_boer_2019_oi_190122.pdf#page=7)

```text
                   Effect of Vitamin D and Omega-3 Fatty Acid Supplementation on Kidney Function in Type 2 Diabetes                                                                                   Original Investigation Research




                   Figure 2. Distributions of eGFR and Urine ACR Over the Course of the Study According to Treatment Assignment

                   A eGFR by vitamin D vs placebo                                                                           B                     eGFR by omega-3 fatty acids vs placebo
                                                               200                                                                                                     200
                                                                                                   Vitamin D   Placebo                                                                                 Omega-3 fatty acids   Placebo




                                       eGFR, mL/min/1.73 m2                                                                                    eGFR, mL/min/1.73 m2
                                                               150                                                                                                     150



                                                               100                                                                                                     100



                                                                50                                                                                                      50



                                                                 0                                                                                                       0
                                                                     0     1   2               3          4       5                                                            0        1       2              3        4       5
                                                                                     Time, y                                                                                                         Time, y
                   No. of participants                                                                                     No. of participants
                    Placebo                                          607       459                              438         Placebo                                           607              459                             438
                    Vitamin D                                        701       531                              496         Omega-3                                           701              531                             496
                                                                                                                              fatty acids


                    C                  Urine ACR by vitamin D vs placebo                                                    D Urine ACR by omega-3 fatty acids vs placebo

                                                     10 000                                                                                                  10 000


                                                              1000                                                                                                    1000




                     Urine ACR, mg/g                                                                                         Urine ACR, mg/g
                                                               100                                                                                                     100


                                                                10                                                                                                      10


                                                                 1                                                                                                       1


                                                               0.1                                                                                                     0.1
                                                                     0     1   2               3          4       5                                                            0        1       2              3        4       5
                                                                                     Time, y                                                                                                         Time, y
                   No. of participants                                                                                     No. of participants
                    Placebo                                          609       463                              440         Placebo                                           609              463                             440
                    Vitamin D                                        702       529                              505         Omega-3                                           702              529                             505
                                                                                                                              fatty acids


                   ACR indicates urine albumin-creatinine ratio; eGFR, estimated glomerular                              range (IQR) of the nearest quartile; circles show all points lying beyond 1.5× the
                   filtration rate. The center horizontal line in each box indicates the median;                         IQR of the nearest quartile. Urine ACR plots are shown on a log scale. Numbers
                   top and bottom box borders indicate the first and third quartiles, respectively.                      shown are participants contributing data at each time point.
                   Whiskers depict the most extreme observation within 1.5× the interquartile



                   such an effect, and 95% confidence intervals excluded differ-                                         outcomes support the overall lack of effect for the primary
                   ences in eGFR decline that may be considered a reasonable                                             outcome and suggest that neither vitamin D nor omega-3 fatty
                   surrogate outcome (0.75 mL/min/1.73 m2 per year,20,21 equiva-                                         acids have kidney effects in this study population.
                   lent to 3.75 mL/min/1.73 m2 over 5 years).                                                                In a meta-analysis of short-term clinical trials, treatment
                       A composite outcome of decline in eGFR of at least 40%,                                           with 1,25-dihydroxyvitamin D3 or a 1,25-diydroxyvitamin D3
                   development of kidney failure, or death was evaluated as a                                            analogue reduced urine albumin excretion, compared with
                   secondary outcome. There were insufficient numbers of events                                          placebo.26 However, their long-term effects on eGFR are not
                   to effectively evaluate treatment effects on this outcome,                                            known, and these treatments are associated with adverse
                   which is conceptually similar to the primary outcome but is                                           effects such as hypercalcemia. Supplemental forms of vita-
                   considered a valid surrogate outcome for ESKD.17 Nonethe-                                             min D, such as vitamin D3, may be more appropriate for wide-
                   less, hazard ratios for this outcome were close to 1 for both                                         spread use for prevention. Prior clinical trials of vitamin D3
                   vitamin D and omega-3 fatty acids. Urine albumin excretion,                                           assessing kidney outcomes have been small (range, 51-63
                   a marker of kidney damage that is complementary to eGFR,                                              participants) and of short duration.15,27,28 The results of this
                   was low in the study population but did increase approxi-                                             study suggest little or no effect of vitamin D3 supplements on
                   mately 3-fold over the course of the study. However, mean                                             CKD in the setting of type 2 diabetes but do not address
                   urine albumin excretion was also not significantly affected by                                        uncertainty regarding the long-term kidney effects of
                   vitamin D or omega-3 fatty acids. Null results for secondary                                          1,25-dihydroxyvitamin D3.

                   jama.com                                                                                                                                            (Reprinted) JAMA November 19, 2019 Volume 322, Number 19         1905

                                                                                     © 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.​com by University of Arizona Health Sciences Library user on 08/​24/​2026

```

### Physical page 8

[Supplied PDF page 8](../../../jama_de_boer_2019_oi_190122.pdf#page=8)

```text
                   Research Original Investigation                                    Effect of Vitamin D and Omega-3 Fatty Acid Supplementation on Kidney Function in Type 2 Diabetes




                   Table 2. Primary Outcome: Effects of Vitamin D and Omega-3 Fatty Acids on Change in eGFR From Baseline to Year 5
                                                                                                                                                                            Difference in Change
                                      Active Intervention                                           Placebo                                                                 From Baselinea
                                                eGFR,                eGFR Change From                     eGFR,                      eGFR Change From                       Mean Difference
                                                Mean (95% CI),       Baseline, Mean (95% CI),             Mean (95% CI),             Baseline, Mean (95% CI),               (95% CI),
                                      No.       mL/min/1.73 m2       mL/min/1.73 m2b                No.   mL/min/1.73 m2             mL/min/1.73 m2b                        mL/min/1.73 m2         P Valuec
                       Vitamin D
                       Baselined      701       86.3 (84.6-88.0)                                    607   85.3 (83.7-87.0)
                       Year 2         531       80.6 (78.8-82.4)     −5.2 (−6.2 to −4.2)            459   79.3 (77.3-81.2)           −6.1 (−7.1 to −5.1)                    0.9 (−0.6 to 2.5)
                       Year 5         496       74.3 (72.3-76.2)     −12.3 (−13.4 to −11.2)         438   72.5 (70.6-74.5)           −13.1 (−14.2 to −11.9)                 0.9 (−0.7 to 2.5)      .25
                       Omega-3 Fatty Acids
                       Baselined      657       85.7 (84.1-87.3)                                    651   86.0 (84.2-87.8)
                       Year 2         499       79.4 (77.6-81.2)     −5.7 (−6.8 to −4.7)            491   80.6 (78.6-82.5)           −5.5 (−6.5 to −4.6)                    −0.3 (−1.8 to 1.3)
                       Year 5         472       73.7 (71.8-75.6)     −12.2 (−13.3 to −11.1)         462   73.2 (71.1-75.3)           −13.1 (−14.2 to −12.0)                 0.9 (−0.7 to 2.6)      .27
                   Abbreviation: eGFR, estimated glomerular filtration rate.                                       accounts for missing data using multiple imputation.
                   a                                                                                           b
                       Modeled difference, with positive values indicating higher eGFR at year 5                   Change from baseline summarized over all participants using multiple
                       (slower decline in eGFR from baseline) among participants randomized to the                 imputation.
                       active intervention compared with those randomized to the corresponding                 c
                                                                                                                   Test of the difference in change in eGFR from baseline to year 5.
                       placebo intervention. Derived from a linear mixed model that includes                   d
                                                                                                                   Four participants were missing baseline eGFR values.
                       adjustment for age, sex, and baseline urine albumin-creatinine ratio and



                   Figure 3. Effects of Vitamin D vs Placebo on Change in eGFR Among Participant Subgroups

                                                     Placebo                                  Vitamin D
                                                     No. of       Mean (SD) Change in         No. of       Mean (SD) Change in                 Favors       Favors                               P Value for
                                                     Participants eGFR, mL/min/1.73 m2        Participants eGFR, mL/min/1.73 m2               Placebo       Vitamin D                            Interaction
                         Overall                     703          –13.1 (14.4)                609          –12.3 (14.8)
                         Race/ethnicity
                          White                      451           –12.1 (13.7)               406             –11.7 (13.5)
                                                                                                                                                                                                 .58
                          Black                      148           –15.9 (16.0)               130             –14.7 (17.1)
                         Baseline urine ACR, mg/g
                          <30                        635           –12.4 (14.2)               559             –11.8 (14.4)
                                                                                                                                                                                                 .36
                          ≥30                        67            –20.4 (15.0)               50              –17.3 (17.4)
                         Baseline 25-hydroxyvitamin D, ng/mL
                          <20                        110           –14.6 (13.9)               85              –12.2 (17.1)
                          20 to <30                  230           –14.7 (15.2)               203             –12.4 (14.0)                                                                       .15
                          ≥30                        332           –11.5 (13.9)               297             –12.3 (14.6)
                         Baseline eGFR, mL/min/1.73 m2
                          ≥60                        612           –14.1 (14.4)               531             –13.7 (14.5)
                                                                                                                                                                                                 .18
                          <60                        89            –5.8 (12.4)                76              –3.0 (13.6)
                         Body mass index
                          <25                        87            –12.9 (13.2)               87              –10.5 (11.7)
                          25 to <30                  228           –12.3 (14.1)               205             –12.2 (14.4)                                                                       .79
                          ≥30                        364           –13.7 (15.0                294             –12.8 (15.7)
                         Omega-3 fatty acid randomization group
                          Placebo                    333           –13.2 (14.9)               320             –13.0 (14.7)
                                                                                                                                                                                                 .42
                          Omega-3 fatty acids        370           –12.9 (13.9)               289             –11.7 (14.9)

                                                                                                                                         –4    –2       0      2        4       6     8    10
                                                                                                                                                  Difference in eGFR Change,
                                                                                                                                         Active – Placebo (95% CI), mL/min/1.73 m2


                   ACR indicates urine albumin-creatinine ratio; eGFR, estimated glomerular                    baseline to year 5 comparing active treatment with placebo, adjusted for age,
                   filtration rate. Body mass index is calculated as weight in kilograms divided by            sex, and baseline urine ACR.
                   height in meters squared. Estimates are differences in change in eGFR from



                        A meta-analysis of 17 small clinical trials (a total of 626                            infarction (19% with diabetes), EPA plus DHA added to mar-
                   participants with varied causes of CKD, including diabetes)                                 garine was reported to attenuate eGFR decline by 2.1 mL/min/
                   suggested that omega-3 fatty acid supplementation reduced                                   1.73 m2 over 3.3 years compared with placebo, although a
                   albuminuria but did not have significant effects on eGFR.12 Two                             similar effect was not observed in a treatment group that ad-
                   trials among those with preexisting coronary heart disease                                  ditionally received linoleic acid.13 Among 262 participants with
                   assessed the effects of omega-3 fatty acids on eGFR or albu-                                stable coronary artery disease, EPA plus DHA treatment for
                   minuria post hoc. Among 2344 older adults with myocardial                                   1 year was reported to reduce urinary albumin excretion only

           1906    JAMA November 19, 2019 Volume 322, Number 19 (Reprinted)                                                                                                                            jama.com

                                                                   © 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.​com by University of Arizona Health Sciences Library user on 08/​24/​2026

```

### Physical page 9

[Supplied PDF page 9](../../../jama_de_boer_2019_oi_190122.pdf#page=9)

```text
                   Effect of Vitamin D and Omega-3 Fatty Acid Supplementation on Kidney Function in Type 2 Diabetes                                                   Original Investigation Research




                   Figure 4. Effects of Omega-3 Fatty Acids vs Placebo on Change in eGFR Among Participant Subgroups

                                                      Placebo                                   Omega-3 Fatty Acids
                                                      No. of       Mean (SD) Change in          No. of       Mean (SD) Change in                        Favors       Favors Omega-3        P Value for
                                                      Participants eGFR, mL/min/1.73 m2         Participants eGFR, mL/min/1.73 m2                      Placebo       Fatty Acids           Interaction
                         Overall                      659          –13.1 (14.8)                 653          –12.2 (14.5)
                         Baseline EPA/DHA, %
                           ≤2.2                       332           –13.3 (15.0)                347            –12.5 (14.6)
                                                                                                                                                                                           .72
                           >2.2                       308           –12.9 (14.6)                292            –11.9 (14.4)
                         Baseline urine ACR, mg/g
                           <30                        596           –12.6 (14.8)                598            –11.5 (13.8)
                                                                                                                                                                                           .70
                           ≥30                        62            –18.1 (14.2)                55             –19.1 (18.3)
                         Baseline hsCRP, mg/dL
                           ≤0.2                       334           –12.9 (14.3)                335            –11.5 (13.4)
                                                                                                                                                                                           .73
                           >0.2                       323           –13.3 (15.3)                316            –13.0 (15.5)
                         Baseline fish intake
                           <1.5 servings/wk           354           –13.4 (15.3)                329            –11.8 (14.7)
                                                                                                                                                                                           .51
                           ≥1.5 servings/wk           295           –12.9 (14.3)                310            –12.7 (14.3)
                         Vitamin D randomization group
                           Placebo                    289           –13.2 (14.9)                320            –12.9 (13.9)
                                                                                                                                                                                           .42
                           Vitamin D                  370           –13.0 (14.7)                333            –11.7 (14.9)


                                                                                                                                          –6     –4     –2       0       2     4      6
                                                                                                                                                    Difference in eGFR Change,
                                                                                                                                           Active – Placebo (95% CI), mL/min/1.73 m2


                   ACR indicates urine albumin-creatinine ratio; DHA, docosahexaenoic acid;                     in eGFR from baseline to year 5 comparing active treatment with placebo,
                   eGFR, estimated glomerular filtration rate; EPA, eicosapentaenoic acid;                      adjusted for age, sex, and baseline urine ACR.
                   hsCRP, high-sensitivity C-reactive protein. Estimates are differences in change



                   Table 3. Secondary Outcomes: Effects of Vitamin D and Omega-3 Fatty Acids on Change in eGFR and Urine Albumin Excretiona

                                                         Active Intervention                    Placebo                                    Difference in
                                                                    Incidence Rate                            Incidence Rate               Incidence Rate             Active vs Placebo,
                                                         No. of     per 100 Person-Years        No. of        per 100 Person-Years         per 100 Person-Years       Hazard Ratio
                       Outcomes                          Events     (95% CI)                    Events        (95% CI)                     (95% CI)                   (95% CI)b             P Valuec
                       Vitamin D Intervention
                       ≥40% Decline in eGFR,             85         2.5 (2.0-3.0)               79            2.7 (2.1-3.3)                −0.2 (−1.0 to 0.6)         0.92 (0.68-1.25)      .61
                       kidney failure during study,
                       or death
                       ≥40% Decline in eGFR              42         1.6 (1.1-2.1)               38            1.7 (1.2-2.1)                −0.1 (−0.7 to 0.6)         0.97 (0.63-1.51)      .90
                       Doubling in urine ACR             111        4.4 (3.6-5.2)               74            3.3 (2.5-4.0)                1.1 (0.0 to 2.2)           1.34 (1.00-1.80)      .05
                       and ≥30 mg/g
                       Omega-3 Intervention
                       ≥40% Decline in eGFR,             86         2.7 (2.2-3.3)               78            2.5 (1.9-3.0)                0.3 (−0.5 to 1.1)          1.11 (0.81-1.50)      .52
                       kidney failure during study,
                       or death
                       ≥40% Decline in eGFR              40         1.6 (1.1-2.1)               40            1.6 (1.2-2.1)                0.0 (−0.7 to 0.7)          0.99 (0.64-1.54)      .97
                       Doubling in urine ACR             96         4.0 (3.2-4.8)               89            3.7 (3.0-4.5)                0.3 (−0.8 to 1.4)          1.08 (0.81-1.44)      .60
                       and ≥30 mg/g
                   Abbreviations: eGFR, estimated glomerular filtration rate;                                       ⱖ30 mg/g and in eTable 6 in Supplement 2 as a continuous variable).
                   ACR, albumin-creatinine ratio.                                                               b
                                                                                                                    Hazard ratios are from a Cox regression model; eGFR outcomes exclude 4
                   a
                       Prespecified secondary outcomes include time to the composite outcome of                     participants who were missing baseline eGFR data and urine ACR outcome
                       ⱖ40% decrease in eGFR from baseline, kidney failure, or death, time to 40%                   excludes 1 participant who was missing baseline urine ACR data.
                       decrease in eGFR from baseline, and change in urine ACR from baseline to study           c
                                                                                                                    Test of the null hypothesis that hazard ratio = 1.
                       year 5 (analyzed in this table as time to doubling of urine ACR to a final urine ACR




                   among the subset of participants with diabetes (n = 79), al-                                 ence or severity of CKD or on evidence of vitamin D or omega-3
                   though multiple testing was not addressed.14 These studies                                   fatty acid deficiency. There were few participants with these
                   were exploratory in nature and were not confirmed by the                                     characteristics, and the trial was not powered to assess these
                   results of the current study.                                                                specific participants. Point estimates from subgroup analy-
                       The results of this study apply to relatively healthy adults                             ses among patients with evidence of CKD (eGFR <60 mL/min/
                   with type 2 diabetes. Participants with known cardiovascular                                 1.73 m2 or urine ACR ≥30 mg/g), serum 25(OH)D concentra-
                   disease, cancer, and ESKD were excluded from the VITAL trial.16                              tion less than 30 ng/mL, or normal body mass index at baseline
                   Furthermore, participants were not selected based on pres-                                   were in favor of the vitamin D intervention, but the 95%

                   jama.com                                                                                                   (Reprinted) JAMA November 19, 2019 Volume 322, Number 19                   1907

                                                                     © 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.​com by University of Arizona Health Sciences Library user on 08/​24/​2026

```

### Physical page 10

[Supplied PDF page 10](../../../jama_de_boer_2019_oi_190122.pdf#page=10)

```text
                   Research Original Investigation                                  Effect of Vitamin D and Omega-3 Fatty Acid Supplementation on Kidney Function in Type 2 Diabetes



                   confidence intervals around these estimates crossed the null                          was limited to assess effects among subgroups who may
                   and tests for interaction were not statistically significant, so                      derive more benefit from the study interventions than the
                   these observations are purely hypothesis generating, and                              overall type 2 diabetes population. Fourth, not all partici-
                   speculation should be viewed with caution.                                            pants returned a serum sample to calculate final (year 5)
                        Strengths of this study include the rigorous randomized                          eGFR, but 71% did so, and 83% returned a serum sample
                   design, the relatively large sample size and long duration                            after randomization. The primary analytic approach
                   of follow-up for the interventions studied, good adherence                            accounted for missing data to minimize bias, and a complete
                   to study medications to enhance internal validity, and consis-                        case approach yielded similar results.
                   tent results in sensitivity analyses and evaluation of second-
                   ary outcomes.

                                                                                                         Conclusions
                   Limitations
                   This study has several limitations. First, there were modest                          Among adults with type 2 diabetes, supplementation with
                   numbers of eGFR and urine ACR measurements collected                                  vitamin D3 or omega-3 fatty acids, compared with placebo,
                   per participant, limiting evaluation of slopes and time-to-                           resulted in no significant difference in change in eGFR at
                   event analyses. Second, there were insufficient numbers of                            5 years. The findings do not support the use of vitamin D or
                   events for widely accepted surrogate kidney end points,                               omega-3 fatty acid supplementation for preserving kidney
                   which were evaluated as secondary outcomes. Third, power                              function in patients with type 2 diabetes.


                   ARTICLE INFORMATION                                      Funding/Support: This study was funded by grant          2. de Boer IH, Rue TC, Hall YN, Heagerty PJ, Weiss
                   Accepted for Publication: October 4, 2019.               R01DK088762 from the National Institute of               NS, Himmelfarb J. Temporal trends in the
                                                                            Diabetes and Digestive and Kidney Diseases. The          prevalence of diabetic kidney disease in the United
                   Published Online: November 8, 2019.                      parent trial was funded by grants U01CA138962            States. JAMA. 2011;305(24):2532-2539. doi:10.
                   doi:10.1001/jama.2019.17380                              and R01CA138962, which include support from the          1001/jama.2011.861
                   Correction: This article was corrected on June 3,        National Cancer Institute; National Heart, Lung, and     3. Zelnick LR, Weiss NS, Kestenbaum BR, et al.
                   2020, for additional conflict of interest disclosures.   Blood Institute; Office of Dietary Supplements;          Diabetes and CKD in the United States population,
                   Author Contributions: Dr de Boer had full access         National Institute of Neurological Disorders and         2009-2014. Clin J Am Soc Nephrol. 2017;12(12):
                   to all of the data in the study and takes                Stroke; and National Center for Complementary            1984-1990. doi:10.2215/CJN.03700417
                   responsibility for the integrity of the data and the     and Integrative Health. Additional support was
                                                                            provided by an unrestricted fund from the                4. Afkarian M, Zelnick LR, Hall YN, et al. Clinical
                   accuracy of the data analysis.                                                                                    manifestations of kidney disease among US adults
                   Concept and design: de Boer, Thadhani, Manson.           Northwest Kidney Centers. Pharmavite, Pronova
                                                                            BioPharma/BASF, and Quest Diagnostics provided           with diabetes, 1988-2014. JAMA. 2016;316(6):602-
                   Acquisition, analysis, or interpretation of data: de                                                              610. doi:10.1001/jama.2016.10924
                   Boer, Zelnick, Ruzinski, Friedenberg, Duszlak,           study medications and diagnostic serivces.
                   Bubes, Hoofnagle, Glynn, Buring, Sesso, Manson.          Role of the Funder/Sponsor: The funding/                 5. Afkarian M, Sachs MC, Kestenbaum B, et al.
                   Drafting of the manuscript: de Boer, Zelnick,            supporting organizations had no role in the design       Kidney disease and increased mortality risk in type
                   Friedenberg, Hoofnagle, Thadhani.                        and conduct of the study; collection, management,        2 diabetes. J Am Soc Nephrol. 2013;24(2):302-308.
                   Critical revision of the manuscript for important        analysis, and interpretation of the data;                doi:10.1681/ASN.2012070718
                   intellectual content: Zelnick, Ruzinski, Duszlak,        preparation, review, or approval of the                  6. de Boer IH, Zelnick LR, Lin J, et al. Vitamin D and
                   Bubes, Hoofnagle, Thadhani, Glynn, Buring, Sesso,        manuscript; or decision to submit the                    omega-3 trial to prevent and treat diabetic kidney
                   Manson.                                                  manuscript for publication.                              disease: rationale, design, and baseline
                   Statistical analysis: Zelnick, Glynn.                    Additional Contributions: We are indebted to the         characteristics. Contemp Clin Trials. 2018;74:11-17.
                   Obtained funding: de Boer, Thadhani, Manson.             VITAL participants and to the entire VITAL research      doi:10.1016/j.cct.2018.09.014
                   Administrative, technical, or material support: de       group and staff for their dedicated collaboration.       7. Zhang Z, Zhang Y, Ning G, Deb DK, Kong J, Li YC.
                   Boer, Friedenberg, Duszlak, Bubes, Hoofnagle,            Voting members of the VITAL Data and Safety              Combination therapy with AT1 blocker and vitamin
                   Sesso, Manson.                                           Monitoring Board include Lawrence S. Cohen, MD           D analog markedly ameliorates diabetic
                   Supervision: de Boer, Hoofnagle, Manson.                 (Yale University School of Medicine); Theodore           nephropathy: blockade of compensatory renin
                   Conflict of Interest Disclosures: Dr de Boer             Colton, ScD (Boston University); Mark A. Espeland,       increase. Proc Natl Acad Sci U S A. 2008;105(41):
                   reported receipt of consulting fees from Boehringer      PhD (Wake Forest University); Craig Henderson,           15896-15901. doi:10.1073/pnas.0803751105
                   Ingelheim and Ironwood and equipment and                 MD (University of California, San Francisco); Alice H.   8. Ito I, Waku T, Aoki M, et al. A nonclassical vitamin
                   supplies for research from Medtronic and Abbott.         Lichtenstein, ScD (Tufts University); Rebecca A.         D receptor pathway suppresses renal fibrosis. J Clin
                   Dr Hoofnagle reported that his laboratory received       Silliman, MD, PhD (Boston University); and Nanette       Invest. 2013;123(11):4579-4594. doi:10.1172/JCI67804
                   payment for services from DiaSorin Inc. Dr               K. Wenger, MD (chair; Emory University); these
                   Thadhani reported holding a patent pending on            members received a stipend for their service.            9. Shapiro H, Theilla M, Attal-Singer J, Singer P.
                   measurement of bioavailable vitamin D and                Ex officio members at the National Institutes of         Effects of polyunsaturated fatty acid consumption
                   receiving payment for services or consulting for         Health include Josephine Boyington, PhD, MPH;            in diabetic nephropathy. Nat Rev Nephrol. 2011;7(2):
                   Fresenius Medical Care North America, Alnylam,           Rebecca B. Costello, PhD; Cindy D. Davis, PhD;           110-121. doi:10.1038/nrneph.2010.156
                   Agios Pharmaceuticals, Bayer, Genzyme, and Pfizer        Peter Greenwald, MD; Gabriela Riscuta, MD; and           10. de Boer IH, Katz R, Chonchol M, et al. Serum
                   and a grant for research from Fisher Scientific. Dr      Harold Seifried, PhD.                                    25-hydroxyvitamin D and change in estimated
                   Glynn reported receipt of grants from Pfizer, Kowa,      Data Sharing Statement: See Supplement 3.                glomerular filtration rate. Clin J Am Soc Nephrol.
                   Novartis, AstraZeneca, and Amarin. Dr Buring                                                                      2011;6(9):2141-2149. doi:10.2215/CJN.02640311
                   reported that her spouse is a member of the              REFERENCES                                               11. de Boer IH, Sachs MC, Cleary PA, et al; Diabetes
                   scientific advisory board of Pharmavite, which                                                                    Control and Complication Trial/Epidemiology of
                   provided the vitamin D pills and packaging for the       1. Tuttle KR, Bakris GL, Bilous RW, et al. Diabetic
                                                                            kidney disease: a report from an ADA consensus           Diabetes Interventions and Complications Study
                   trial. Dr Sesso reported receipt of grants from Pure                                                              Research Group. Circulating vitamin D metabolites
                   Encapsulations. Dr Manson reported receipt of            conference. Diabetes Care. 2014;37(10):2864-2883.
                                                                            doi:10.2337/dc14-1296                                    and kidney disease in type 1 diabetes. J Clin
                   grants from the National Institutes of Health. No                                                                 Endocrinol Metab. 2012;97(12):4780-4788.
                   other disclosures were reported.                                                                                  doi:10.1210/jc.2012-2852


           1908    JAMA November 19, 2019 Volume 322, Number 19 (Reprinted)                                                                                                      jama.com

                                                                 © 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.​com by University of Arizona Health Sciences Library user on 08/​24/​2026

```

### Physical page 11

[Supplied PDF page 11](../../../jama_de_boer_2019_oi_190122.pdf#page=11)

```text
                   Effect of Vitamin D and Omega-3 Fatty Acid Supplementation on Kidney Function in Type 2 Diabetes                                       Original Investigation Research



                   12. Miller ER III, Juraschek SP, Appel LJ, et al. The     a scientific workshop sponsored by the National           prevention of cancer and cardiovascular disease.
                   effect of n-3 long-chain polyunsaturated fatty acid       Kidney Foundation and the US Food and Drug                N Engl J Med. 2019;380(1):33-44. doi:10.1056/
                   supplementation on urine protein excretion and            Administration. Am J Kidney Dis. 2014;64(6):821-835.      NEJMoa1809944
                   kidney function: meta-analysis of clinical trials. Am J   doi:10.1053/j.ajkd.2014.07.030                            24. Manson JE, Cook NR, Lee IM, et al; VITAL
                   Clin Nutr. 2009;89(6):1937-1945. doi:10.3945/             18. Jun M, Turin TC, Woodward M, et al. Assessing         Research Group. Marine n-3 fatty acids and
                   ajcn.2008.26867                                           the validity of surrogate outcomes for ESRD:              prevention of cardiovascular disease and cancer.
                   13. Hoogeveen EK, Geleijnse JM, Kromhout D, et al.        a meta-analysis. J Am Soc Nephrol. 2015;26(9):            N Engl J Med. 2019;380(1):23-32. doi:10.1056/
                   Effect of omega-3 fatty acids on kidney function          2289-2302. doi:10.1681/ASN.2014040396                     NEJMoa1811403
                   after myocardial infarction: the Alpha Omega Trial.       19. Inker LA, Schmid CH, Tighiouart H, et al;             25. Coresh J, Turin TC, Matsushita K, et al. Decline
                   Clin J Am Soc Nephrol. 2014;9(10):1676-1683.              CKD-EPI Investigators. Estimating glomerular              in estimated glomerular filtration rate and
                   doi:10.2215/CJN.10441013                                  filtration rate from serum creatinine and cystatin C.     subsequent risk of end-stage renal disease and
                   14. Elajami TK, Alfaddagh A, Lakshminarayan D,            N Engl J Med. 2012;367(1):20-29. doi:10.1056/             mortality. JAMA. 2014;311(24):2518-2531. doi:10.
                   Soliman M, Chandnani M, Welty FK.                         NEJMoa1114248                                             1001/jama.2014.6634
                   Eicosapentaenoic and docosahexaenoic acids                20. Inker LA, Heerspink HJL, Tighiouart H, et al.         26. de Borst MH, Hajhosseiny R, Tamez H, Wenger
                   attenuate progression of albuminuria in patients          GFR slope as a surrogate end point for kidney             J, Thadhani R, Goldsmith DJ. Active vitamin D
                   with type 2 diabetes mellitus and coronary artery         disease progression in clinical trials: a meta-analysis   treatment for reduction of residual proteinuria:
                   disease. J Am Heart Assoc. 2017;6(7):e004740.             of treatment effects of randomized controlled             a systematic review. J Am Soc Nephrol. 2013;24(11):
                   doi:10.1161/JAHA.116.004740                               trials. J Am Soc Nephrol. 2019;30(9):1735-1745.           1863-1871. doi:10.1681/ASN.2013030203
                   15. Momeni A, Mirhosseini M, Kabiri M, Kheiri S.          doi:10.1681/ASN.2019010007                                27. Kim MJ, Frankel AH, Donaldson M, et al. Oral
                   Effect of vitamin D on proteinuria in type 2 diabetic     21. Greene T, Ying J, Vonesh EF, et al. Performance       cholecalciferol decreases albuminuria and urinary
                   patients. J Nephropathol. 2017;6(1):10-14. doi:10.        of GFR slope as a surrogate end point for kidney          TGF-β1 in patients with type 2 diabetic nephropathy
                   15171/jnp.2017.03                                         disease progression in clinical trials: a statistical     on established renin-angiotensin-aldosterone
                   16. Manson JE, Bassuk SS, Lee IM, et al. The              simulation. J Am Soc Nephrol. 2019;30(9):1756-1769.       system inhibition. Kidney Int. 2011;80(8):851-860.
                   Vitamin D and Omega-3 Trial (VITAL): rationale            doi:10.1681/ASN.2019010009                                doi:10.1038/ki.2011.224
                   and design of a large randomized controlled trial         22. Rubin DB. Multiple Imputation for Nonresponse         28. Ahmadi N, Mortazavi M, Iraj B, Askari G.
                   of vitamin D and marine omega-3 fatty acid                in Surveys. New York, NY: John Wiley & Sons; 1987.        Whether vitamin D3 is effective in reducing
                   supplements for the primary prevention of cancer          doi:10.1002/9780470316696                                 proteinuria in type 2 diabetic patients?
                   and cardiovascular disease. Contemp Clin Trials.                                                                    J Res Med Sci. 2013;18(5):374-377.
                   2012;33(1):159-171. doi:10.1016/j.cct.2011.09.009         23. Manson JE, Cook NR, Lee IM, et al; VITAL
                                                                             Research Group. Vitamin D supplements and
                   17. Levey AS, Inker LA, Matsushita K, et al. GFR
                   decline as an end point for clinical trials in CKD:




                   jama.com                                                                                            (Reprinted) JAMA November 19, 2019 Volume 322, Number 19               1909

                                                                   © 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.​com by University of Arizona Health Sciences Library user on 08/​24/​2026

```
