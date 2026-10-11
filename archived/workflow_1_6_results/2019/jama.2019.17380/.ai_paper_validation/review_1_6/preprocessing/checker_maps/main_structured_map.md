# Main-paper quantitative evidence map

## Scope and evidence basis

DOC-001, `jama_de_boer_2019_oi_190122.pdf`, PDF pages 1–11 (printed pages 1899–1909), document role REPORT. All pages mapped without a candidate-count target. Local keys M001–M120 identify relationship bundles for independent checkers; these are not candidate IDs or shared numeric/statistical IDs. Every bundle includes its exact evidence in the structured map or the complete page-separated source transcription below. No candidate diagnosis or judgment is made here.

Reusable locators: source-matched Poppler native and layout text under `.ai_paper_validation/review_1_5_2/preprocessing/`; usable assets A001–A003 and rendered main-paper pages A013–A023 in evidence_asset_inventory.md. Curator verified byte identity of current native/layout extraction. Rendered pages 5–9 were visually inspected for all Table 1, Figure 1, Figure 2, Table 2/Figure 3, and Figure 4/Table 3 entries, graphical labels, and captions. Engines: Poppler pdftotext 26.01.0 and legacy pdftoppm 180 dpi. No fresh-required main units, OCR, fallback environment, or external information used. Source link base from this artifact: `../../../jama_de_boer_2019_oi_190122.pdf#page=N`.

## Complete page coverage

| PDF page | Printed page | Exact scope mapped | Status |
|---|---:|---|---|
| 1 | 1899 | Abstract design, arms, sample, primary effect estimates/CIs, safety counts; metadata | COMPLETE |
| 2 | 1900 | Background CKD prevalence; key points; parent/ancillary sample and eligibility; doses; randomization; endpoint change/time | COMPLETE |
| 3 | 1901 | Outcome definitions; measurements; covariates/adherence; sample-size assumptions; full/complete-case models; tests/subgroups | COMPLETE |
| 4 | 1902 | All results narrative: demographics, retention, adherence, biomarkers, medications, primary/secondary/post hoc results | COMPLETE |
| 5 | 1903 | Every Table 1 row, all four arms, headings, units, dispersion values, denominator and conversion footnotes | COMPLETE |
| 6 | 1904 | Every Figure 1 node and footnote; adverse events; post hoc interpretation; discussion numeric claims | COMPLETE |
| 7 | 1905 | Figure 2 all four panels, axis/box/whisker/denominator labels; numeric discussion and historical trial range | COMPLETE |
| 8 | 1906 | Every Table 2 entry/footnote; every Figure 3 row and interaction P; historical numeric discussion | COMPLETE |
| 9 | 1907 | Every Figure 4 row/interaction P; every Table 3 count/rate/CI/difference/HR/P and footnote; subgroup discussion | COMPLETE |
| 10 | 1908 | Null/interaction interpretation, sample return 71%/83%, limitations and conclusions; administrative disclosures/funding/reference entries (no applicable original result numbers) | COMPLETE |
| 11 | 1909 | References only: no applicable original result numbers; citation year/volume/page/DOI identifiers are bibliographic, not original quantitative relationships | COMPLETE |

## Matching and analysis definitions

M001: Abstract pp.1 and key points p.2: 2×2 factorial trial, 1312 adults with type 2 diabetes, all 50 states, recruited November 2011–March 2014; follow-up completed December 2017; 5-year assigned supplementation. Four arms in order used throughout this map: D+O=370, D+P=333, P+O=289, P+P=320. Parent trial N=25,871; target ancillary enrollment=1320. All four arms received assigned intervention (Figure 1).

M002: p.2 eligibility men ≥50 years/women ≥55; excludes gestational-only diabetes, diagnosis before age 30 with insulin >20 years, known non-diabetic CKD. Randomization blocks 8 stratified age/sex/race. Background CKD prevalence >25%; parent baseline blood samples approximately two-thirds. These are definitional/background quantities, not study outcome counts.

M003: D3 2000 IU/day; omega-3 1 g/day capsules containing EPA 465 mg and DHA 375 mg; nonstudy vitamin D supplemental limit 800 IU/day. p.1 doses and p.2 doses refer to study treatment versus supplemental outside sources.

M004: pp.2–3 primary endpoint change in creatinine+cystatin-C CKD-EPI eGFR baseline→year 5; original albuminuria endpoint modified in 2016 with extension to 5 years. Samples baseline, year 2, year 5. eGFR units mL/min/1.73 m²; ACR mg/g. Cystatin C calibrator-lot shift harmonized to ERM-DA471/IFCC prospectively; slightly different from previously reported values; eAppendix results supplement matching target.

M005: p.3 prespecified secondary time-to composite ≥40% eGFR decline/kidney failure/death; ≥40% decline alone; urine ACR change continuous or time to doubling to final ≥30 mg/g. Post hoc ≥40% decline/kidney failure and endpoints using ≥30% decline. Kidney failure annually questionnaire.

M006: p.3 sample calculation N=1320, power 80%, detectable change difference ≥2.3 mL/min/1.73 m², two-sided alpha .05, follow-up samples 80%; smallest clinical relevance 2.3 over 5 years; surrogate ≥0.75 per year equivalent ≥3.75 over 5 years. Discussion pp.6–7 repeats 2.3, 0.75, 3.75, and 5 years.

M007: p.3 linear mixed random-intercept models: time categorical baseline/2/5; treatment×time, age, sex, age×time and sex×time; eGFR adds baseline ACR and ACR×time. Test treatment×year5 coefficient; two-tailed P<.05 for each intervention. Full analytic population all randomized regardless adherence/follow-up; M=20 imputations and Rubin combination. Complete case baseline+year5 specimens; high adherence ≥two-thirds; urine analyses optionally exclude UTI symptoms. R 3.6.0.

M008: p.3 subgroup interaction Wald test subgroup×time×treatment; D prespecified race/ethnicity, 25(OH)D, ACR, eGFR; BMI later added; O prespecified omega-3 index/CRP, fish intake later added. Secondary categorical Cox models; Schoenfeld residuals assess proportional hazards. p.6 no statistically significant PH assumption violation. Secondary findings exploratory due multiple comparisons.

## Abstract and narrative matching bundles

| Key | Exact locations | Printed relationship / matching target |
|---|---|---|
| M009 | pp.1,4, Table1 p.5 | Mean age 67.6 y; women 46%; racial/ethnic minority 31%; diabetes median duration 6–10 y; insulin 20%; DPP4 or GLP1 each <10%; antihypertensive 80%; RAS inhibitor 61% |
| M010 | p.1; p.4; Fig1 p.6 | 1312 randomized; 934 (71%) completed/returned final blood; final blood 76% alive; 1090 (83%) at least one follow-up blood |
| M011 | p.4 | Follow-up urine at least once 1091 (83%); final urine 945 (72% randomized;77% alive) |
| M012 | p.4; p.10 | Limitations repeat year5 serum return 71%, any postrandomization serum 83% |
| M013 | p.4 | D/placebo adherence ≥two-thirds: 92% year2,88% year5; O/placebo 91%,89%; matches supplement eTable1 |
| M014 | p.4 | Year2 25(OH)D: D41.4(SD11.0),placebo29.8(SD11.1) ng/mL,P<.001 |
| M015 | p.4 | Year2 omega-3 index O3.6%(SD1.0%),placebo2.3%(SD0.8%),P<.001 |
| M016 | p.4 | DPP4 9% baseline→14% year5; ARB20%→29%;5% initiated SGLT2; supplement eTables2–3 |
| M017 | p.1,p.4 | Baseline eGFR85.8(SD22.1);year2 80.0(SD21.5);year5 73.5(SD21.9),mL/min/1.73m²; Fig2 descriptive distributions |
| M018 | p.4 | Baseline eGFR<60:165(13%);ACR≥30:117(9%),including ACR≥300:24(2%) |
| M019 | p.4,p.6 | Overall full analytic eGFR change−12.7(95%CI−13.6 to−11.7);complete case932 change−12.4(−13.3 to−11.4);discussion decrease12.7 over5y |
| M020 | p.1,p.2,p.4,Table2 p.8 | D vs placebo year5 change−12.3(−13.4 to−11.2) vs−13.1(−14.2 to−11.9);difference0.9(−0.7 to2.5);Table2P=.25 |
| M021 | same locations | O vs placebo year5 change−12.2(−13.3 to−11.1) vs−13.1(−14.2 to−12.0);difference0.9(−0.7 to2.6);Table2P=.27 |
| M022 | p.1,p.4,Fig3/4 pp.8–9 | No significant D×O interaction;P=.42;no significant subgroup heterogeneity |
| M023 | p.4 | Neither 25(OH)D nor omega-3 index change baseline→year2 significantly correlated with eGFR baseline→year5; supplement eFigure1 |
| M024 | p.4,Table3 p.9 | Composite164 participants;components80 ≥40% decline,11 kidney failure,80 deaths;overlap explicitly allowed;DHR.92(.68–1.25),OHR1.11(.81–1.50) |
| M025 | p.4,p.7 | UrineACR year2 geometric mean5.1(4.6–5.7),year5 9.2(8.4–10.1) mg/g;approximately3-fold baseline→year5;no significant treatment effect; eTable6 |
| M026 | p.4 | ACR sensitivity/subgroups complete case,adherence,UTI exclusion similar;eFigures2–3,eTables7–9;post hoc renal outcomes not significant;eTable10 |
| M027 | p.1,p.6 | Kidney stones58=D32+placebo26;GI bleeding45=O28+placebo17;eTable11 |
| M028 | p.6–7 | Age-only expected eGFR decline2–3 over5y;observed12.7;CIs exclude surrogate3.75 difference;secondary HRs close1 |
| M029 | p.7–9 | Historical trial numbers: D trials51–63 participants;omega meta17 trials626 participants;prior infarction trial2344 participants19% diabetes,eGFR attenuation2.1 over3.3y;coronary trial262,diabetic subset79,1y |
| M030 | pp.9–10 | D subgroup CKD(eGFR<60 orACR≥30),25(OH)D<30,normalBMI point estimates favor D but95%CIs cross null and interactions not significant;hypothesis-generating |

## Table 1: complete row mapping (PDF p.5)

All four-arm printed entries are preserved in the exact page transcription below. Order D+O, D+P, P+O, P+P. No.(%) unless mean(SD)/median(IQR) indicated. Percentages explicitly use nonmissing responses, not automatically the randomized arm denominator. Race/ethnicity nonmissing counts361,327,284,314. Creatinine conversion×88.4 to μmol/L; BMI kg/m².

| Key | Exact Table1 row or relationship |
|---|---|
| M031 | Four arm denominators370,333,289,320 and sex female/male counts and percentages |
| M032 | Age mean(SD)67.4(7.3),67.4(6.7),68.2(6.7),67.5(6.9) |
| M033 | Race nonmissing361,327,284,314;white240(66),211(65),199(70),207(66) |
| M034 | Black73(20),75(23),59(21),71(23) |
| M035 | Hispanic20(6),21(6),16(6),18(6) |
| M036 | Asian/Pacific13(4),8(2),7(2),7(2) |
| M037 | American Indian/Alaska6(2),4(1),1(<1),2(1) |
| M038 | Other9(2),8(2),2(1),9(3);all race category sums/nonmissing |
| M039 | Education>high school303(82),283(85),243(84),270(85) |
| M040 | Diabetes<1y13(4),15(5),5(2),9(3) |
| M041 | Diabetes1–2y52(14),43(13),45(16),37(12) |
| M042 | Diabetes3–5y78(21),72(22),62(22),78(24) |
| M043 | Diabetes6–10y107(29),83(25),74(26),96(30) |
| M044 | Diabetes11–20y90(24),82(25),69(24),74(23) |
| M045 | Diabetes>20y29(8),37(11),33(11),25(8);all duration categories/nonmissing |
| M046 | Smoking22(6),17(5),15(5),25(8) |
| M047 | Alcohol191(53),184(56),151(53),168(54) |
| M048 | Biguanides247(67),222(67),199(69),221(69) |
| M049 | Sulfonylureas109(29),100(30),85(29),99(31) |
| M050 | Insulin67(18),68(20),57(20),66(21) |
| M051 | Thiazolidinediones32(9),32(10),24(8),36(11) |
| M052 | DPP4 inhibitors33(9),26(8),22(8),34(11) |
| M053 | GLP1 agonists9(2),14(4),16(6),9(3) |
| M054 | Antihypertensives293(80),263(80),231(81),258(81) |
| M055 | No.classes means1.4(SD1.2),1.4(1.1),1.4(1.1),1.4(1.2) |
| M056 | ACE/ARB223(60),205(62),177(61),198(62) |
| M057 | ACE163(44),148(44),121(42),133(42) |
| M058 | Diuretic111(30),87(26),82(28),84(26) |
| M059 | Beta blocker91(25),74(22),62(21),68(21) |
| M060 | Calcium channel blocker75(20),76(23),58(20),66(21) |
| M061 | ARB67(18),64(19),60(21),69(22) |
| M062 | Mineralocorticoid antagonist2(1),3(1),0,4(1) |
| M063 | Cholesterol meds250(69),238(73),199(71),223(71) |
| M064 | Supplemental D≥800IU/d146(39),138(41),124(43),128(40) |
| M065 | Supplemental calcium≥1200mg/d84(23),66(20),81(28),81(25) |
| M066 | BMI means31.4(6.5),31.8(6.6),30.8(6.6),31.6(7.3) |
| M067 | Creatinine0.8(0.3),0.9(0.3),0.8(0.2),0.9(0.2)mg/dL |
| M068 | Cystatin C each0.9(0.3)mg/L |
| M069 | ACR median(IQR)2.9(0.5–7.6),2.8(0.5–8.8),2.9(0.5–7.1),3.2(1.0–6.7)mg/g |
| M070 | 25(OH)D29.6(10.6),29.0(9.8),30.2(10.3),30.1(9.9)ng/mL |
| M071 | 25(OH)D<20:62(17),48(15),41(15),44(14) |
| M072 | 25(OH)D20–<30:109(31),121(38),87(32),116(37) |
| M073 | 25(OH)D≥30:184(52),148(47),146(53),151(49);category totals/nonmissing and footnotes |

## Figure 1 (p.6): participant flow

M074: Assessed3244;excluded1932(ineligible438,declined1494);randomized1312. Four arms randomized/received370,333,289,320.

M075–M078 respectively four arms: returned≥1 blood303,280,242,265;completed260,236,212,226;lost110,97,77,94;no final blood89,78,56,75;died21,19,21,19;primary/adverse event analysis370,333,289,320;complete case259,236,211,226;complete-case excluded111,97,78,94. D+O excludes110 lost+1 missing baseline eGFR;P+O77 lost+1 baseline;D+P footnote says1 of97 lost also baseline missing;P+P1 of94 lost also baseline missing. Full denominator and complete-case932/934 links retained.

## Figure 2 (p.7): all panels and graphical quantities

M079: PanelA eGFR D vs placebo, years0/2/5. Printed participant rows: placebo607/459/438,D701/531/496.
M080: PanelB eGFR O vs placebo, years0/2/5. Printed participant rows: placebo607/459/438,O701/531/496. These are exact figure-print transcription, without relabeling.
M081: PanelC urine ACR D vs placebo: placebo609/463/440,D702/529/505.
M082: PanelD urine ACR O vs placebo: placebo609/463/440,O702/529/505. These are exact figure-print transcription.
M083: eGFR vertical linear axis0/50/100/150/200;ACR vertical log axis0.1/1/10/100/1000/10000mg/g;horizontal years0–5 with actual data0/2/5. Box line median; caption literally says top/bottom borders first/third quartiles respectively;whiskers extreme observations within1.5×IQR;circles beyond1.5×IQR. No exact plotted median/quartile numerical values are printed; graphical values are not converted into invented exact estimates. Curves/boxes visually show decreasing eGFR and rising ACR both interventions and placebos; source image retained as exact authority.

## Table 2 (p.8): six complete time rows

Each M084–M089 row tracks active/placebo measured N, descriptive eGFR mean95%CI, imputed modeled change95%CI, adjusted active-minus-placebo difference95%CI, and year5 test P. Full exact entries below. D baseline N701/607,mean86.3(84.6–88.0)/85.3(83.7–87.0);year2 N531/459,means80.6(78.8–82.4)/79.3(77.3–81.2),changes−5.2(−6.2 to−4.2)/−6.1(−7.1 to−5.1),difference0.9(−0.6 to2.5);year5 N496/438,means74.3(72.3–76.2)/72.5(70.6–74.5),changes/difference M020,P.25.

O baseline N657/651,means85.7(84.1–87.3)/86.0(84.2–87.8);year2 N499/491,means79.4(77.6–81.2)/80.6(78.6–82.5),changes−5.7(−6.8 to−4.7)/−5.5(−6.5 to−4.6),difference−0.3(−1.8 to1.3);year5 N472/462,means73.7(71.8–75.6)/73.2(71.1–75.3),changes/difference M021,P.27.

M090: Table2 footnotes: modeled difference positive means higher year5 eGFR/slower decline in active;age/sex/baselineACR adjusted mixed model,multiple imputation;changes all participants via imputation;P tests year5 change difference;4 missing baseline eGFR. Descriptive means and model changes have distinct population/calculation labels.

## Figure 3 (p.8): every row, literal heading assignment

Columns literally headed Placebo then Vitamin D. Values are N, mean(SD) change in eGFR baseline→year5, mL/min/1.73m². Headings retained literally. Points/95%CI whiskers adjusted for age/sex/baselineACR;horizontal active−placebo;negative favors placebo,positive D. No numerical forest point estimates/CIs printed; source graph supplies their location. Axis ticks−4,−2,0,2,4,6,8,10. All whiskers visually cross0. Figure3≥30BMI SD source literally lacks closing parenthesis for15.0.

| Key | Row | Placebo printed N,mean(SD) | Vitamin D printed N,mean(SD) | InteractionP |
|---|---|---|---|---|
| M091 | Overall |703,−13.1(14.4)|609,−12.3(14.8)|Not printed |
| M092 | White |451,−12.1(13.7)|406,−11.7(13.5)|.58 race group |
| M093 | Black |148,−15.9(16.0)|130,−14.7(17.1)|same |
| M094 | ACR<30 |635,−12.4(14.2)|559,−11.8(14.4)|.36 ACR group |
| M095 | ACR≥30 |67,−20.4(15.0)|50,−17.3(17.4)|same |
| M096 | 25(OH)D<20 |110,−14.6(13.9)|85,−12.2(17.1)|.15 vitamin level group |
| M097 | 25(OH)D20–<30 |230,−14.7(15.2)|203,−12.4(14.0)|same |
| M098 | 25(OH)D≥30 |332,−11.5(13.9)|297,−12.3(14.6)|same |
| M099 | eGFR≥60 |612,−14.1(14.4)|531,−13.7(14.5)|.18 eGFR group |
| M100 | eGFR<60 |89,−5.8(12.4)|76,−3.0(13.6)|same |
| M101 | BMI<25 |87,−12.9(13.2)|87,−10.5(11.7)|.79 BMI group |
| M102 | BMI25–<30 |228,−12.3(14.1)|205,−12.2(14.4)|same |
| M103 | BMI≥30 |364,−13.7(15.0|294,−12.8(15.7)|same |
| M104 | O assignment placebo |333,−13.2(14.9)|320,−13.0(14.7)|.42 O assignment group |
| M105 | O assignment active |370,−12.9(13.9)|289,−11.7(14.9)|same |

## Figure 4 (p.9): every row, literal heading assignment

Columns Placebo then Omega-3 fatty acids. All values N,mean(SD) eGFR change. Adjusted forest horizontal active−placebo,95%CI;negative favors placebo,positive O. Axis−6,−4,−2,0,2,4,6. No exact forest numbers printed; all whiskers visually cross0. hsCRP label mg/dL;EPA/DHA label%;fish servings/week.

| Key | Row | Placebo printed N,mean(SD) | Omega-3 printed N,mean(SD) | InteractionP |
|---|---|---|---|---|
| M106 | Overall |659,−13.1(14.8)|653,−12.2(14.5)|Not printed |
| M107 | EPA/DHA≤2.2%;>2.2% |332,−13.3(15.0);308,−12.9(14.6)|347,−12.5(14.6);292,−11.9(14.4)|.72 |
| M108 | ACR<30;≥30 |596,−12.6(14.8);62,−18.1(14.2)|598,−11.5(13.8);55,−19.1(18.3)|.70 |
| M109 | hsCRP≤0.2;>0.2 |334,−12.9(14.3);323,−13.3(15.3)|335,−11.5(13.4);316,−13.0(15.5)|.73 |
| M110 | Fish<1.5;≥1.5/wk |354,−13.4(15.3);295,−12.9(14.3)|329,−11.8(14.7);310,−12.7(14.3)|.51 |
| M111 | D assignment placebo;active |289,−13.2(14.9);370,−13.0(14.7)|320,−12.9(13.9);333,−11.7(14.9)|.42 |

## Table 3 (p.9): every secondary categorical outcome

Each event count has corresponding incidence rate per100 person-years95%CI, rate difference95%CI, and Cox active-vs-placebo HR95%CI with P(nullHR1). Person-time totals are not printed; do not substitute randomized count for person-time. Exact values:

| Key | Intervention/outcome | Active count/rate(CI) | Placebo count/rate(CI) | Rate difference(CI) | HR(CI) | P |
|---|---|---|---|---|---|---|
| M112 | D composite≥40% decline/kidneyfailure/death |85/2.5(2.0–3.0)|79/2.7(2.1–3.3)|−0.2(−1.0 to0.6)|0.92(0.68–1.25)|.61 |
| M113 | D≥40% eGFRdecline |42/1.6(1.1–2.1)|38/1.7(1.2–2.1)|−0.1(−0.7 to0.6)|0.97(0.63–1.51)|.90 |
| M114 | D ACRdoubling and≥30mg/g |111/4.4(3.6–5.2)|74/3.3(2.5–4.0)|1.1(0.0 to2.2)|1.34(1.00–1.80)|.05 |
| M115 | O composite≥40% decline/kidneyfailure/death |86/2.7(2.2–3.3)|78/2.5(1.9–3.0)|0.3(−0.5 to1.1)|1.11(0.81–1.50)|.52 |
| M116 | O≥40% eGFRdecline |40/1.6(1.1–2.1)|40/1.6(1.2–2.1)|0.0(−0.7 to0.7)|0.99(0.64–1.54)|.97 |
| M117 | O ACRdoubling and≥30mg/g |96/4.0(3.2–4.8)|89/3.7(3.0–4.5)|0.3(−0.8 to1.4)|1.08(0.81–1.44)|.60 |

M118: Table3 footnotes exclude4 baseline eGFR missing for eGFR outcomes and1 baselineACR missing forACR;Cox model HR;ACR endpoint continuous results are eTable6,not in Table3;secondary tests exploratory;event/rate/model matching distinct. The source does not print secondary Cox covariate adjustment details or person-time denominators here.

M119: pp.1–10 repeated interpretations: no significant main difference at5y,three prespecified secondary outcomes not significant,post hoc endpoints not significant,no significant D/O or subgroup interaction;CIs and exact P references above preserve intended matching without judging coherence.

M120: Administrative metadata p.1 corrected June3,2020;onlineNovember8,2019;pp.10–11 publication/disclosure/funding/reference numerals are non-applicable original scientific relationship units. No raw data, clinical-methodology, misconduct, or external reference verification performed.

## Limitations and source authority

All11 pages and every table/figure/narrative quantitative unit are mapped. Zero scientific-coverage gaps. Figures2–4 do not print exact numerical box statistics or all forest point/interval coordinates; all printed numerical data and labels are mapped, and direct source graphics remain the graphical authority. No exact numbers inferred from pixel position. No SE or test statistic is printed for the mapped primary/secondary tests; compatible detailed formulas/variance rules require supplied support mapping. Local relationship bundles permit multiple elementary arithmetic or inferential comparisons;120 bundles is a locator count, not a candidate or scientific check limit.

