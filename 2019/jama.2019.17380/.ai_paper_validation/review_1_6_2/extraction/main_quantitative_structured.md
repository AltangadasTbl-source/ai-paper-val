Warning: truncated output (original token count: 32116)
Total output lines: 1095

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

The complete source-matched page appendix remains preserved in main_quantitative_evidence.md. This mechanical projection preserves the entire structured map, numeric/statistical registers, all constituent table/figure rows and completeness records without duplicating the appendix.
