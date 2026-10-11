# Main quantitative evidence map — Workflow 1.6.2

Runtime task ID: /root/main_mapper. Role: fresh main_quantitative_mapper. Exact assigned scope: DOC001, jama_urashima_2019_oi_190023.pdf, PDF pp. 1–9, document role REPORT. All nine units reusable-backed; zero fresh-required units. This map transcribes evidence and relationships without candidate diagnosis or adjudication. Local M keys identify mapped relationship groups; numeric/statistical stable IDs are assigned downstream.

## Evidence and tooling

Read QUALITY_CONTROL_SCOPE.md, review_contract.md, settings.toml, source_inventory.md, evidence_asset_inventory.md, source_coverage.md, and tooling_record.md. The usable page locators are `.ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-MAIN/native_text/page-NNN.txt` for pp. 1–8 (legacy layout text corroborated by current Poppler in curator inventory), and `.ai_paper_validation/document_outputs/JAMA2019-2210-DOC-01/native_text_pages/page-009.txt` for p. 9 (legacy native engine unspecified). The reusable source-linked 150-dpi renders `.ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-MAIN/rendered_pages/page-N.png` pp. 4–8 were individually viewed for flow, tables, curves, risk sets, axes, and footnotes. No derivative created; no fresh OCR or rendering required. Compute device CPU per tooling record. Existing renders are locators, and exact PDF locations remain authoritative for recheck.

All table columns below use vitamin D first and placebo second unless otherwise stated. HRs and subdistribution HRs compare randomized vitamin D with placebo; the separately transcribed Table 2 footnote is preserved as printed. CI level 95%, ordinary significance two-sided P<.05; confidence/test conventions come from p.3. Counts are patients, ages years, times years unless specified. No person-time, standard errors, numerical test statistics, or SDs are printed for this trial in the main paper. The abstract prints mean age 66; the body prints median age 66. These are recorded as separately labeled quantities.

## Page coverage

| PDF page | Article page | Units inspected | Mapping keys | Status |
|---|---:|---|---|---|
| 1 | 1361 | Complete abstract: design, population, intervention, definitions, all efficacy/safety numbers | M001–M009 | COMPLETE |
| 2 | 1362 | Key Points; design, eligibility, randomization/blinding, intervention, outcomes; background separately identified | M010–M015 | COMPLETE |
| 3 | 1363 | Follow-up, assay, SNP definitions, sample size, complete statistical analysis through imputation continuation | M016–M025 | COMPLETE |
| 4 | 1364 | Figure 1, post hoc continuation, population, outcome events and estimates, subgroup definitions/25(OH)D changes | M026–M039 | COMPLETE |
| 5 | 1365 | Entire Table 1 including continuation and all footnotes; subgroup/PH narrative | M040–M066 | COMPLETE |
| 6 | 1366 | Entire Figure 2 including axes/curves/risk sets/caption, imputation, post hoc results, lab results, safety narrative | M067–M080 | COMPLETE |
| 7 | 1367 | Entire Table 2 and footnote; all Figure 3 panels, axes, risk sets and caption | M081–M097 | COMPLETE |
| 8 | 1368 | Entire Table 3 and footnotes, discussion, limitations, conclusion | M098–M106 | COMPLETE |
| 9 | 1369 | Article information, funder statement, data-sharing pointer, references 1–32, footer | M107 | COMPLETE — no applicable trial quantitative result |

No-applicable units: bibliographic/publication metadata, authors/affiliations, download footer on all pages, p.2 biological/background literature paragraphs, p.3 molecular storage/amplification details apart from SNP subgroup identities, p.8 external-study discussion counts, and p.9 author contributions/funding/references. External-literature numbers are preserved in the page text annex but are not this trial's result relationships. Clinical regimen descriptions without a quantitative result connection are recorded in annex, not used for an external method audit.

## Abstract, design, and statistical relationships

| Key | Exact PDF location | Relationship and source values |
|---|---|---|
| M001 | p.1 abstract Design | Single-center Japanese randomized double-blind placebo trial; enrollment January 2010, follow-up February 2018; age 30–90; digestive tract esophagus–rectum, stages I–III; 439 eligible, 15 declined, 7 excluded after operation. |
| M002 | p.1 Intervention/Results | Vitamin D3 2000 IU/d, n=251; placebo n=166; first postoperative outpatient visit until trial end. All 417 analyzed; mean age 66, male 66%, esophageal 10%, gastric 42%, colorectal 48%. |
| M003 | p.1 Main outcomes | Primary time to relapse or death; secondary overall survival time to any-cause death; baseline 25(OH)D groups 0–<20, 20–40, >40 ng/mL; interaction only low/middle because high group small. |
| M004 | p.1 Results follow-up | Follow-up 99.8%; median 3.5, IQR 2.3–5.3; maximum 7.6 years. |
| M005 | p.1 Results primary | Relapse/death 50 (20%) vs 43 (26%); 5-year relapse-free survival 77% vs 69%; HR 0.76, CI 0.50–1.14, P=.18; no significant improvement conclusion. |
| M006 | p.1 Results secondary | Death 37 (15%) vs 25 (15%); 5-year overall survival 82% vs 81%; HR 0.95, CI 0.57–1.57, P=.83. |
| M007 | p.1 Results subgroup | Baseline 20–40 ng/mL: 5-year relapse-free survival 85% vs 71%; HR 0.46, CI 0.24–0.86, P=.02; interaction P=.04. |
| M008 | p.1 Results safety | Fracture 3 (1.3%) vs 5 (3.4%); urinary stones 2 (0.9%) vs 0; abstract does not state safety denominators, linked Table3 per-protocol-until-censoring columns p.8. |
| M009 | p.1 Conclusions | Vitamin D versus placebo did not result in significant improvement in relapse-free survival at 5 years. |
| M010 | p.2 Key Points | 417 patients; vitamin D 2000 IU/d; 5-year relapse-free survival 77% vs 69%, difference not statistically significant; Meaning says supplementation did not improve relapse-free survival. Links M005/M009/M032/M067/M106. |
| M011 | p.2 Trial Design | 3:2 allocation; vitamin D3 2000 IU/d vs placebo; usual discharge 5–14 days and outpatient 1–2 weeks later; study randomization/start 2–4 weeks after surgery. |
| M012 | p.2 Participants | Histopathological epithelial carcinoma esophagus/stomach/small intestine/colon/rectum; clinical I–III; age30–90; diagnosis/initial surgery at study center; not taking vitamin D; no history urinary stones. Excludes unresectable tumors, serious postoperative complications before supplements, non-epithelial pathology, pathological stage0/IV. |
| M013 | p.2 Randomization | Computer-generated centrally administered permuted blocks of5; 3:2 without stratification; all except preparer/data-center staff blinded. Individual patients randomized. |
| M014 | p.2 Intervention | First outpatient visit after surgery to study end; oral 2000 IU/d vitamin D3 or placebo; assigned then instructed to start that day. |
| M015 | pp.2–3 Outcomes | Primary elapsed time randomization/start study medication to earliest cancer relapse or any-cause death; secondary overall survival from randomization to any-cause death, incidence relapse, cancer-specific death, noncancer death. Safety fracture, urinary stones, serious admission events, cancer de novo in organs other than primary site after start. |
| M016 | p.3 Follow-up | Examination monthly first6 months, every2 months second6 months, every3 months thereafter to5 years, then every3–6 months; adherence self-report at visits/telephone and new bottle every6 months; serum25(OH)D annually. Medically required vitamin D stops trial supplementation, follow-up continues to trial end. |
| M017 | p.3 Vitamin D measurements | Radioimmunoassay baseline/annual same calendar month; 19 separate-cohort samples blinded duplicates, assay correlation coefficient0.92. |
| M018 | p.3 SNPs | VDR FokI rs2228570, BsmI rs1544410, CDX2 rs11568820, ApaI rs7976091, TaqI rs731236; vitamin-D binding protein DBP1 rs7041 and DBP2 rs4588. Genotypes define M059–M065. |
| M019 | p.3 Sample Size | Historical cohort257 colorectal patients; highest-vs-lowest25(OH)D quartile 5-year relapse-free survival difference13%. Assumed vitamin D75% vs placebo62%; two-sided type I error .05, power80%, loss1%; total400, ratio3:2. Accrual80/year for5 years; final follow-up2 years after enrollment, total planned7 years. No printed sample-size formula. |
| M020 | p.3 Statistical Analysis | All randomized included; relapse/death outcomes by randomization regardless supplements; adverse events only continuing supplements (per protocol). Nelson–Aalen cumulative hazards and Cox PH HR/95%CI for relapse/death and total death. |
| M021 | p.3 subgroup/interactions | Prespecified baseline low<20, middle20–40, high>40 ng/mL and SNPs; exclude baseline25(OH)D missing from subgroup analyses. Cox interaction model treatment, baseline group, treatment×group, 2-way interaction low/middle only; high omitted due small n. Two-sided P<.05; multiple comparisons make subgroup findings exploratory. |
| M022 | p.3 interim | Stata14.0; annual interim after200 entries; Peto constant stopping P<.001 independent of unknown exact interim count. Compare p.4 three interim analyses, threshold not met. |
| M023 | p.3 post hoc first–third | Schoenfeld residual PH test; cumulative incidence/subdistribution HR competing-risk relapse, deaths due causes other than relapse competing; HR adjusted separately age quartiles or stage-I disease status because imbalance. |
| M024 | pp.3–4 post hoc fourth | Missing25(OH)D multivariable normal-regression MCMC multiple imputation50 repetitions, predictors age/sex, serum calcium, alkaline phosphatase, parathyroid hormone; seven missing p.6. |
| M025 | p.4 post hoc fifth–seventh | Additional subgroup cancer site, stage, pathology, sex, BMI, age; mean25(OH)D over baseline/annual samples groups<20,20–<30,30–<40,40–<50,≥50 ng/mL independent of supplement allocation with Nelson–Aalen relapse/death curves. Baseline-to1-year median25(OH)D/calcium Wilcoxon signed rank within group; change ratios Mann–Whitney between groups. |

## Patient flow, population, and narrative outcomes

| Key | Exact PDF location | Relationship and source values |
|---|---|---|
| M026 | p.4 Fig1 upper | 439 assessed;22 excluded =15 declined +5 did not meet inclusion +2 other reasons;417 randomized. |
| M027 | p.4 Fig1 vitamin D branch | 251 randomized,251 received as randomized;1 lost within6 months;23 stopped =14 nonmedical (3 within1y,9 between1–2y,2 after2y) +9 medical (4 within1y,5 between1–2y);251 primary analysis. Lost patient shown separately from23 stops. |
| M028 | p.4 Fig1 placebo branch | 166 randomized,166 received as randomized;19 stopped =10 nonmedical (2 within1y,7 between1–2y,1 after2y) +9 medical (4 within1y,5 between1–2y);166 primary analysis. |
| M029 | p.4 Study Population | 3 interims, stopping rule not met, entries exceeded400;417 total =251(60%) +166(40%); enrollment January2010–April2016; median randomization/start23.5 days postoperation, IQR13–44. All surviving followed February2018 except1 lost at1 month;99.8% follow-up. Nonmedical15(6.0%) vs10(6.0%), vitaminD includes lost1; medical9(3.6%) vs9(5.4%);10.3% stopped before censoring; all417 efficacy analyses. |
| M030 | p.4 follow-up | Vitamin D median3.5(IQR2.3–5.4), max7.6; placebo median3.5(2.3–5.0), max7.4 years. |
| M031 | p.4 characteristics narrative | All Japanese; women34%, median age66, medianBMI22; esophagus9.6%, stomach41.7%, small bowel0.5%, colorectal48.2%; stageI44%, II26%, III30%; age medians D67(61–75) vs P64(58–71); stageI46% vs40%. |
| M032 | p.4 primary outcome | Relapse/death50(20%) vs43(26%);5-year relapse-free77% vs69%; HR0.76 CI0.50–1.14 P=.18; supplementation did not significantly reduce risk; links p.1/p.2/Fig2A. |
| M033 | p.4 death | 37(15%)/251 vs25(15%)/166 died;5-year overall82% vs81%; HR0.95 CI0.57–1.57 P=.83; links p.1/Fig2B. |
| M034 | p.4 component outcomes | Relapse41(16%) vs36(22%); cancer-specific death27(11%) vs16(10%); noncancer death10(4%) vs9(5%). Denominators251/166. Estimates Table2. |
| M035 | p.4 subgroup population | Low<20 n173; middle20–40 n232; high>40 n5; high not further analyzed small sample. Baseline missing7 p.6; Table1 gives low102/71, middle142/90, high4/1. |
| M036 | p.4 subgroup lab | Vitamin D middle median26.5(IQR23–30) to45(36–57) ng/mL after1year; low16(13–18) to36(27–47). Pointer eFig2. |
| M037 | pp.4–5 subgroup relapse/death | Middle5-year85% vs71%, HR0.46 CI0.24–0.86 P=.02; lowHR1.15 CI0.65–2.05 no significant difference; interactionP=.04. Fig3 gives lowP=.63. |
| M038 | p.5 subgroup death | MiddleHR0.60 CI0.28–1.30, lowHR1.36 CI0.66–2.81; both nonsignificant; interactionP=.13. Fig3 adds middleP=.20, lowP=.41. |
| M039 | pp.5–6 PH/imputation | PH assumption tests nonsignificant;7 missing25(OH)D; multiple-imputed results consistent primary (eTable2 pointer). SNP subgroup associations not significant (eFig3A–U pointer). No numerical PH test statistic/P printed here. |

## Table 1 — all counts and percentages

Exact source for every row is DOC001 PDF p.5 Table1, REPORT. Headers vitaminD n251; placebo n166. Values are count (percentage). Category-specific available-data denominators are not explicitly printed as separate headers; retain counts unchanged. Percentages may not sum100 because rounding (footnote a). BMI kilograms/meters squared (b). Other pathology includes neuroendocrine n4, adenoid cystic n1, unclassified n1 (c).

| Key | Characteristic/category | Vitamin D | Placebo |
|---|---|---|---|
| M040 | Sex male; female | 173(69);78(31) | 103(62);63(38) |
| M041 | Age y35–59;60–65;66–73;74–90 | 51(20);55(22);63(25);82(33) | 50(30);41(25);48(29);27(16) |
| M042 | BMI15.0–19.7;19.8–21.8;21.9–23.7;23.8–37.3 | 63(25);62(25);59(24);65(26) | 36(22);43(26);45(27);41(25) |
| M043 | Other-cancer history | 9(4) | 7(4) |
| M044 | Hypertension | 103(41) | 58(35) |
| M045 | Diabetes mellitus | 44(18) | 24(14) |
| M046 | Endocrine disease | 33(13) | 18(11) |
| M047 | Cardiovascular disease | 22(9) | 9(5) |
| M048 | Chronic kidney disease | 5(2) | 1(1) |
| M049 | Asthma | 3(1.2) | 0(0.0) |
| M050 | Orthopedic disease | 1(0.4) | 1(0.6) |
| M051 | Site esophagus;stomach;small bowel;colorectal | 22(9);106(42);1(0.4);122(49) | 18(11);68(41);1(0.6);79(48) |
| M052 | StageI;II;III | 115(46);63(25);73(29) | 67(40);48(29);51(31) |
| M053 | Adenocarcinoma | 226(90) | 147(88) |
| M054 | Squamous cell carcinoma | 22(9) | 16(10) |
| M055 | Other pathology | 3(1) | 3(2) |
| M056 | Baseline25(OH)D low<20;middle20–40;high>40 ng/mL | 102(41);142(58);4(1.6) | 71(44);90(56);1(0.6) |
| M057 | Adjuvant chemotherapy | 88(35) | 60(36) |
| M058 | Table footnotes/denominator context | Footnotes a,b,c above; no separate available-data denominator table. Genotypes are baseline SNP subgroups. | Same footnotes |
| M059 | FokI CC;CT;TT | 92(38);117(48);36(15) | 57(36);75(48);25(16) |
| M060 | BsmI AA;AG;GG | 14(6);42(18);175(76) | 8(5);23(15);119(79) |
| M061 | Cdx2 GG;GA;AA | 89(39);103(45);38(17) | 49(33);77(51);24(16) |
| M062 | ApaI GG;GT;TT | 96(42);104(45);31(13) | 69(46);61(40);20(13) |
| M063 | TaqI TT;TC;CC | 172(74);54(23);5(2) | 115(77);31(21);4(3) |
| M064 | DBP1 TT;TG;GG | 134(58);87(38);10(4) | 82(55);57(39);9(6) |
| M065 | DBP2 CC;CA;AA | 115(50);91(39);25(11) | 81(54);58(39);11(7) |
| M066 | Matching narrative | Sex/site/stage counts match target relationships M002/M031; age quartiles underpin post hoc age adjustment M023/M070; stageI underpins M071; baseline/SNP counts underpin M021/M035–M039 and supplement subgroup mappings. | No inference or candidate diagnosis applied |

## Figure 2 and post hoc narrative

| Key | Exact PDF location | Relationship and values |
|---|---|---|
| M067 | p.6 Fig2A | Nelson–Aalen cumulative hazard relapse/death; HR0.76 CI0.50–1.14 P=.18. X years after randomization0–6 in1-year ticks; Y0–0.8 in0.2 ticks. At risk years0,1,2,3,4,5,6: placebo166,148,113,84,54,34,16; vitaminD251,222,176,130,93,65,35. Curves labeled placebo/vitaminD, placebo higher late. |
| M068 | p.6 Fig2B | Nelson–Aalen cumulative hazard death; HR0.95 CI0.57–1.57 P=.83. Same axes; at risk P166,160,128,94,62,42,20; D251,245,196,145,104,73,37. Curves cross, both labeled. |
| M069 | p.6 Fig2C/caption/narrative | Relapse cumulative incidence with deaths from causes other than relapse competing; subdistributionHR0.75 CI0.48–1.17 P=.21, no significant difference. Axes x0–6 years y0–0.8(0.2 ticks); no displayed risk-set numbers for panelC. Curve placebo higher late. Caption median observation relapse/death P3.0(IQR1.9–4.5), D3.3(1.9–5.3); deaths P3.5(2.3–5.0), D3.5(2.3–5.4); competing relapse P3.0(1.9–4.5), D3.3(1.9–5.3). |
| M070 | p.6 age adjustment | Adjusted age-quartile relapse/deathHR0.66 CI0.43–0.99 P=.048 significantly less; deathHR0.81 CI0.48–1.36 P=.42 not significantly different; rationale older D group (Table1). |
| M071 | p.6 stageI adjustment | More stageI in D; stage-I-status adjusted analyses no significant differences. No main-paper effect/CI/P printed for this adjustment. |
| M072 | p.6 subgroup competing relapse | Middle subdistributionHR0.44 CI0.21–0.89 P=.02 significantly lower; lowHR1.18 CI0.64–2.19 no significant difference; two-way interactionP=.04; Table2 supplies lowP=.59. |
| M073 | p.6 further subgroups | No significant interaction associations sex men/women; age≤65/>65; BMI<25/≥25; sites esophagus/gastric/colorectal; stageI/II/III; adenocarcinoma/nonadenocarcinoma. eFigs4–9 pointers; no main-paper numerical interaction values for these. |
| M074 | p.6 vitaminD25(OH)D | Baseline median21(IQR16–27) to1-year41(33–55)ng/mL, P<.001, significantly increased; Wilcoxon signed rank (M025). |
| M075 | p.6 placebo25(OH)D | Baseline21(IQR15–27) to1-year20(15–27)ng/mL, P=.91, not significant; Wilcoxon signed rank. |
| M076 | p.6 between-group25(OH)D | Change ratio1year87% D vs0% P, P<.001; Mann–Whitney (M025), not stated ratio of printed group medians. D levels remain high over4years, P low; eFig2. Mean-level analyses eTable1/eFig1A/B. |
| M077 | p.6 vitaminDcalcium | Baseline9.3(IQR8.9–9.6) to1-year9.3(9.1–9.6)mg/dL, P=.09, not significant. |
| M078 | p.6 placebocalcium | Baseline9.3(IQR9.0–9.6) to1-year9.3(9.1–9.5)mg/dL, P=.44, not significant. |
| M079 | p.6 between-groupcalcium | Change ratio0% both D and P, P=.10; Mann–Whitney. |
| M080 | p.6 adverse events | Per protocol continuing until censoring fracture3(1.3%) vs5(3.4%); stones2(0.9%) vs0; no hypercalcemia during follow-up. Table3 denominators227/147. |

## Table 2 — inferential rows and direction statement

All exact locations DOC001 PDF p.7 Table2 REPORT. Columns total population, baseline<20ng/mL, baseline20–40ng/mL; interaction low/middle. Relapse uses subdistributionHR; death rows HR. Confidence level95%. Preserve separately printed footnote, without substituting a direction interpretation.

| Key | Outcome/population | Estimate (95% CI) | P |
|---|---|---|---|
| M081 | Relapse total | 0.75(0.48–1.17) | .21 |
| M082 | Relapse low | 1.18(0.64–2.19) | .59 |
| M083 | Relapse middle | 0.44(0.21–0.89) | .02; interaction .04 |
| M084 | Cancer-specific death total | 1.09(0.58–2.01) | .80 |
| M085 | Cancer-specific death low | 1.45(0.63–3.38) | .38 |
| M086 | Cancer-specific death middle | 0.78(0.29–2.10) | .63; interaction .35 |
| M087 | Noncancer death total | 0.70(0.29–1.73) | .44 |
| M088 | Noncancer death low | 1.11(0.26–4.65) | .89 |
| M089 | Noncancer death middle | 0.39(0.11–1.39) | .15; interaction .27 |
| M090 | Footnote a | Printed: “Hazard ratio (HR) values greater than 1 indicate that vitamin D supplementation was associated with a decreased probability of the outcome.” | Exact source wording preserved; matching treatment contrast defined pp.3–4 and Fig2/3 |

## Figure 3 — all panels and caption

Exact source DOC001 PDF p.7 Figure3 REPORT. X years after randomization0,1,2,3,4,5,6; Y cumulative hazard0–0.5 by0.1; Nelson–Aalen. All four panels have visibly printed risk-set rows. Caption text is independently transcribed below. Risk-set arrays ordered years0–6, placebo first then vitaminD.

| Key | Panel/relationship | Printed values |
|---|---|---|
| M091 | A relapse/death middle20–40 | HR0.46 CI0.24–0.86 P=.02; P90,83,63,49,30,18,9; D142,132,111,85,58,38,20. Placebo curve higher late. |
| M092 | B relapse/death low<20 | HR1.15 CI0.65–2.05 P=.63; P71,61,46,31,20,13,5; D102,84,61,43,33,26,15. VitaminD curve higher initially/middle, curves cross later. |
| M093 | C death middle20–40 | HR0.60 CI0.28–1.30 P=.20; P90,88,70,51,34,22,11; D142,139,115,88,61,41,20. Placebo curve higher late. |
| M094 | D death low<20 | HR1.36 CI0.66–2.81 P=.41; P71,68,54,39,24,17,7; D102,100,75,54,40,31,17. VitaminD curve higher late. |
| M095 | Caption subgroup/weighting statement | Only5 patients high>40ng/mL, not evaluated. Printed: “Numbers at risk for panel C are not given because of weighting.” Preserved independently of visible panel rows. |
| M096 | Caption relapse/death observation times | Middle P3.4(IQR1.9–4.5), D3.8(2.4–5.3); low P2.8(1.8–4.4), D2.5(1.6–5.2) years. |
| M097 | Caption death observation times | Middle P3.5(IQR2.3–5.0), D3.8(2.5–5.4); low P3.4(2.1–5.0), D3.3(1.9–5.4) years. |

## Table 3 — safety populations and all cells

Exact source DOC001 PDF p.8 Table3 REPORT. All entries count(percentage), no CIs/tests. Per-protocol adherent-until-censoring Dn227/Pn147; per-protocol adherent1year Dn243/Pn160; randomized irrespective adherence Dn251/Pn166. All repeated outcome counts are matched only within their designated analysis population.

| Key | Outcome | Until censoring D/P | 1year D/P | Randomized D/P |
|---|---|---|---|---|
| M098 | Population denominators | 227/147 | 243/160 | 251/166 |
| M099 | Fracture | 3(1.3)/5(3.4) | 3(1.2)/6(3.8) | 3(1.2)/6(3.6) |
| M100 | Urinary stones | 2(0.9)/0(0.0) | 4(1.6)/2(1.3) | 4(1.6)/4(2.4) |
| M101 | Severe adverse events | 19(8.4)/9(6.1) | 20(8.2)/13(8.1) | 21(8.4)/15(9.0) |
| M102 | Cancer de novo | 15(6.6)/8(5.4) | 16(6.6)/9(5.6) | 16(6.4)/9(5.4) |
| M103 | Footnotes a–d | a: Per protocol continues study medication until censorship or for more than1year; rationale more sensitive safety;1 lost vitaminD considered nonadherent. b: randomized independent adherence. c: events resulting admission. d: new cancer in organs other than primary site after study medication start. | Same definitions | Same definitions |

## Discussion/conclusion and no-applicable page

| Key | Exact source location | Mapped claim/context |
|---|---|---|
| M104 | p.8 Discussion | Overall no reduced risks relapse/death, any-cause death, relapse. VitaminD effective only middle20–40ng/mL subgroup but exploratory/cautious because null total-population primary and multiplicity; hypothesized benefit low-baseline subgroup. Safety exploratory, not powered significant differences. Dose2000IU/d restated. External-study samples155,64studies/44165patients,8cohorts,VITAL25871,3RCTs are supplied discussion background, not AMATERASU results. |
| M105 | p.8 Limitations | Post hoc cancer site/stage/pathology subgroups; exams every1–6months; approximately10% stopped medication/self-reported adherence;5high-baseline patients too few; prespecified20/40ng/mL cutoffs;7missing baseline25(OH)D, imputed results consistent; no central independent blinded radiology. No extra inferential statistic reported. |
| M106 | p.8 Conclusions | No significant improvement in5-year relapse-free survival with vitaminD vs placebo; matches abstract conclusion and overall primary. |
| M107 | p.9 article info/references | Complete page inspected. Author contributions, funding, no funder role, data-sharing pointer Supplement3,32references and publication metadata; no applicable trial result/statistical-design relationship. COMPLETE no-applicable unit. |

## Matching-occurrence index for downstream checks

- Overall enrollment/allocation: M001/M002/M010/M011/M013/M026–M029, Table1 headers(M040–M065), Figure2 baseline risk sets(M067/M068), Table3 randomization(M098).
- Primary outcome/results: M003/M005/M009/M010/M015/M020/M032/M067/M104/M106.
- Overall death: M006/M015/M020/M033/M068; component deaths M034/M084–M089.
- Relapse competing-risk: M015/M023/M034/M069/M072/M081–M083.
- Baseline subgroups: M003/M007/M021/M035/M037/M038/M056/M072/M082/M083/M085/M086/M088/M089/M091–M097; missing M024/M039/M105.
- Safety: M008/M015/M020/M027–M029/M080/M098–M103/M104/M105.
- Lab change and subgroup levels: M016/M017/M024/M025/M036/M074–M079; unit/scale/within-vs-between tests preserved.
- Design/sample size/interim: M011–M024/M029 and source-linked plan evidence mapped separately by support mapper.

## Completeness and limitations

Covered9/9pages,107local relationship/unit records M001–M107; no scientific coverage gap. Composite rows preserve every constituent cell; M107 explicitly identifies a no-applicable unit. No numerical PH-test values or stage-I-adjusted estimates appear in main paper, and individual-level lab change ratios cannot be recovered from printed group medians alone; these are source reporting boundaries, not diagnoses. Figure curves inspected visually; exact ordinate values along unlabeled step segments are not digitized because source does not print them. Printed axes, relative curve patterns, point estimates, intervals, tests, risk sets, captions, and footnotes are fully mapped.

## Page-specific reusable text annex

The following source-linked locator text preserves complete reading context, including non-applicable passages. It remains a derivative transcription aid; authoritative evidence links refer to the supplied PDF. Each page has one truthful link relative to this artifact.

### DOC001 PDF page 1

[Supplied main PDF page 1](../../../jama_urashima_2019_oi_190023.pdf#page=1)

```text
                Research


              JAMA | Original Investigation

              Effect of Vitamin D Supplementation on Relapse-Free Survival
              Among Patients With Digestive Tract Cancers
              The AMATERASU Randomized Clinical Trial
              Mitsuyoshi Urashima, MD; Hironori Ohdaira, MD; Taisuke Akutsu, MD; Shinya Okada, MD; Masashi Yoshida, MD;
              Masaki Kitajima, MD; Yutaka Suzuki, MD


                                                                                                                              Visual Abstract
                 IMPORTANCE Randomized clinical trials of vitamin D supplementation for secondary                             Editorial page 1354
                 prevention in patients with cancer are needed, given positive results of observational studies.
                                                                                                                              Related article page 1370

                 OBJECTIVE To determine whether postoperative vitamin D3 supplementation can improve                          Video and Supplemental
                 survival of patients with digestive tract cancers overall and in subgroups stratified by                     content
                 25-hydroxyvitamin D (25[OH]D) levels.                                                                        CME Quiz at
                                                                                                                              jamanetwork.com/learning
                 DESIGN, SETTING, AND PARTICIPANTS The AMATERASU trial, a randomized, double-blind,
                 placebo-controlled trial conducted at a single university hospital in Japan. Enrollment began
                 in January 2010 and follow-up was completed in February 2018. Patients aged 30 to 90 years
                 with cancers of the digestive tract from the esophagus to the rectum, stages I to III, were
                 recruited. Of 439 eligible patients, 15 declined and 7 were excluded after operation.

                 INTERVENTIONS Patients were randomized to receive oral supplemental capsules of vitamin
                 D (2000 IU/d; n = 251) or placebo (n = 166) from the first postoperative outpatient visit to
                 until the end of the trial.

                 MAIN OUTCOMES AND MEASURES The primary outcome was relapse-free survival time to
                 relapse or death. The secondary outcome was overall survival time to death due to any cause.
                 Subgroups analyzed had baseline serum 25(OH)D levels of 0 to less than 20 ng/mL, 20 to
                 40 ng/mL, and greater than 40 ng/mL; because of small sample size for the highest-baseline-
                 level group, interactions were tested only between the low- and middle-baseline-level groups.

                 RESULTS All 417 randomized patients (mean age, 66 years; male, 66%; esophageal cancer,
                 10%; gastric cancer, 42%; colorectal cancer, 48%) were included in the analyses. There was
                 99.8% follow-up over a median 3.5 (interquartile range, 2.3-5.3) years, with maximal
                 follow-up of 7.6 years. Relapse or death occurred in 50 patients (20%) randomized to vitamin
                 D and 43 patients (26%) randomized to placebo. Death occurred in 37 (15%) in the vitamin D
                 group and 25 (15%) in the placebo group. The 5-year relapse-free survival was 77% with
                 vitamin D vs 69% with placebo (hazard ratio [HR] for relapse or death, 0.76; 95% CI,
                 0.50-1.14; P = .18). The 5-year overall survival in the vitamin D vs placebo groups was 82% vs
                 81% (HR for death, 0.95; 95% CI, 0.57-1.57; P = .83). In the subgroup of patients with baseline
                 serum 25(OH)D levels between 20 and 40 ng/mL, the 5-year relapse-free survival was 85%                   Author Affiliations: Division of
                                                                                                                          Molecular Epidemiology, Jikei
                 with vitamin D vs 71% with placebo (HR for relapse or death, 0.46; 95% CI, 0.24-0.86;                    University School of Medicine,
                 P = .02; P = .04 for interaction). Fractures occurred in 3 patients (1.3%) in the vitamin D group        Tokyo, Japan (Urashima, Akutsu);
                 and 5 (3.4%) in the placebo group. Urinary stones occurred in 2 patients (0.9%) in the                   Department of Surgery, International
                                                                                                                          University of Health and Welfare
                 vitamin D group and 0 in the placebo group.
                                                                                                                          Hospital, Tochigi, Japan (Ohdaira,
                                                                                                                          Yoshida, Kitajima, Suzuki);
                 CONCLUSIONS AND RELEVANCE Among patients with digestive tract cancer, vitamin D                          Department of Pathology,
                 supplementation, compared with placebo, did not result in significant improvement in                     International University of Health
                                                                                                                          and Welfare Hospital, Tochigi, Japan
                 relapse-free survival at 5 years.                                                                        (Okada).
                                                                                                                          Corresponding Author: Mitsuyoshi
                 TRIAL REGISTRATION UMIN Identifier: UMIN000001977                                                        Urashima, MD, Division of Molecular
                                                                                                                          Epidemiology, Jikei University School
                                                                                                                          of Medicine, Nishi-shimbashi 3-25-8,
                                                                                                                          Minato-ku, Tokyo 105-8461, Japan
                 JAMA. 2019;321(14):1361-1369. doi:10.1001/jama.2019.2210                                                 (urashima@jikei.ac.jp).



                                                                                                                                                      (Reprinted) 1361
                                                      © 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/30/2026

```

### DOC001 PDF page 2

[Supplied main PDF page 2](../../../jama_urashima_2019_oi_190023.pdf#page=2)

```text
               Research Original Investigation                        Effect of Vitamin D Supplementation on Relapse-Free Survival in Patients With Digestive Tract Cancers




               S
                      erum levels of 25-hydroxyvitamin D (25[OH]D), a precur-
                      sor of activated vitamin D, increase in response to exposure             Key Points
                      to sunlight, a vitamin D–rich diet, or vitamin D supplemen-
                                                                                               Question Does vitamin D supplementation improve survival
               tation. Cancer cells are believed to take up and activate 25(OH)D               among patients with digestive tract cancers?
               within the cell, which binds to the vitamin D receptor to regulate
                                                                                               Findings In this randomized clinical trial that included 417 patients
               gene expression and consequently suppresses cancer growth.1,2                   with digestive tract cancers (from esophagus to rectum), the
                    In 1989, the risk of colon cancer was estimated to be 70%                  5-year relapse-free survival rate for those randomized to
               lower in people with serum 25(OH)D levels of 20 ng/mL or more                   vitamin D, 2000 IU/d, vs placebo was 77% vs 69%, a difference
               compared with those with levels less than 20 ng/mL.3 In a co-                   that was not statistically significant.
               hort study, higher 25(OH)D levels were associated with lower                    Meaning Vitamin D supplementation did not improve
               total cancer incidence and lower total cancer mortality, par-                   relapse-free survival among patients with digestive tract cancer.
               ticularly digestive system cancer mortality.4 Similar results
               have been found in colorectal cancer.5-7                                    ach, small intestine, colon, and rectum), clinical stages I to III;
                    However, 2 randomized clinical trials (RCTs) using vitamin D           aged 30 to 90 years at entry; diagnosis and initial surgery at
               and calcium to prevent cancer incidence generated conflicting               the International University of Health and Welfare Hospital;
               conclusions: one concluded that supplementation with calcium                not taking vitamin D supplements or active vitamin D; and no
               and vitamin D (400 IU/d) for 7 years had no effect on the incidence         history of urinary tract stones. The exclusion criteria com-
               of colorectal cancer in postmenopausal women,8 whereas another              prised tumors that were not resectable by surgery, serious post-
               demonstratedthatcancerincidencewaslowerinpostmenopausal                     operative complications before starting supplementation,
               women taking calcium plus vitamin D (1100 IU/d) than in those               pathological diagnosis other than epithelial carcinoma (such
               taking placebo.9 However, these RCTs focused on primary pre-                as malignant lymphoma and sarcoma), and pathological stage
               vention for participants without cancer; to our knowledge, no RCT           0 or IV. Collaborating surgeons preoperatively described the
               of secondary prevention for relapse or death has been conducted.            trial to eligible patients and their families at outpatient clin-
                    Single-nucleotide polymorphisms (SNPs) of the vitamin D                ics and asked them to participate in the trial. All clinical data
               receptor have been associated with the prognosis of patients                were collected at the International University of Health and
               with cancer.10-12 In addition, SNPs of vitamin D binding pro-               Welfare Hospital and monitored at the Division of Molecular
               tein have been associated with 25(OH)D levels.13,14 Therefore,              Epidemiology, Jikei University School of Medicine.
               a randomized, double-blind, placebo-controlled trial was con-
               ducted to assess whether vitamin D3 supplementation can im-                 Randomization and Blinding
               prove survival of patients with digestive tract cancers from the            Computer-generated and centrally administered randomiza-
               esophagus to the rectum after surgical resection. Subgroup                  tion used permuted blocks of 5. Participants were random-
               analyses were also done based on serum 25(OH)D cutoff levels                ized in a 3:2 ratio without stratification. Increasing the likeli-
               of 20 and 40 ng/mL as well as the presence of relevant SNPs.                hood of randomization to the vitamin D group was done in an
                                                                                           effort to increase willingness to participate. With the excep-
                                                                                           tion of M.U. and the staff of the data monitoring center at the
                                                                                           Jikei University School of Medicine, who prepared the bottles
               Methods
                                                                                           of vitamin D or placebo according to randomization assign-
               Trial Design                                                                ments, all other surgeons, the clinical research coordinator,
               This was a double-blind, placebo-controlled trial to compare the            and participants at the International University of Health and
               effects of vitamin D3 supplementation, 2000 IU/d, or placebo at             Welfare Hospital were blinded to group assignment.
               an allocation ratio of 3:2. Patients at the International University
               of Health and Welfare Hospital (Ohtawara, Tochigi prefecture,               Intervention
               Japan) surgically treated for digestive tract cancer between the            At the first outpatient visit after surgery, enrolled patients were
               esophagus and the rectum are usually discharged 5 to 14 days af-            randomly assigned to receive either vitamin D3 supplementation,
               ter the operation and visit the outpatient clinic 1 to 2 weeks later        2000 IU/d, or placebo, and were asked to take the study medica-
               if there are no major complications. Therefore, in this study, pa-          tion from that day until the end of the trial. Both study medica-
               tients who did not meet exclusion criteria were randomized and              tions were purchased from Zenyaku Pharmaceutical Co Ltd,
               started supplementation at the first outpatient visit between 2 and         Tokyo, Japan.
               4 weeks after operation. The trial protocol was approved by the
               ethics committee of the International University of Health and              Outcomes
               Welfare Hospital. Written informed consent was obtained from                The primary outcome was relapse-free survival, defined as
               each patient who decided to participate before surgery. There was           elapsed time from the date of randomization (ie, time from start-
               no external data and safety monitoring committee for this study.            ing the study medication to the earliest date of cancer relapse or
               The full protocol for this trial is available in Supplement 1.              death due to any cause). Secondary outcomes comprised over-
                                                                                           all survival, defined as elapsed time from the date of random-
               Participants                                                                ization (ie, time from starting the study medication to the date
               The inclusion criteria included a histopathological diagnosis               of death due to any cause), as well as incidence of relapse, cancer-
               of epithelial carcinoma of the digestive tract (esophagus, stom-            specific death, and noncancer death. Safety outcomes comprised

        1362   JAMA April 9, 2019 Volume 321, Number 14 (Reprinted)                                                                                              jama.com

                                                    © 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/30/2026

```

### DOC001 PDF page 3

[Supplied main PDF page 3](../../../jama_urashima_2019_oi_190023.pdf#page=3)

```text
              Effect of Vitamin D Supplementation on Relapse-Free Survival in Patients With Digestive Tract Cancers                          Original Investigation Research



              bone fractures, urinary stones, serious events requiring admis-                    relapse-free survival in the highest quartile of 25(OH)D levels was
              sion, and new (de novo) cancer arising in organs other than the                    calculated to be 13% better than in the lowest quartile. Consid-
              site of the primary cancer after starting study medication.                        ering approximate survival data for digestive tract cancer in Japan,
                                                                                                 the 5-year relapse-free survival rates would be 75% and 62% in
              Follow-up                                                                          the vitamin D and placebo groups, respectively, with a 2-side type I
              Patients were periodically examined as outpatients by computed                     error of .05 and a power of 80%, assuming a 1% loss to follow-up.
              tomography, magnetic resonance imaging, positron emission to-                      It was estimated that 400 patients with digestive tract cancers di-
              mography, and other procedures to exclude cancer relapse as re-                    vided in a 3:2 ratio would be sufficient to detect this difference.
              quired by a surgeon in charge. This generally occurred every                       Assuming that 80 patients per year could participate in this trial,
              month for the first 6 months, every 2 months for the second 6                      the accrual period was estimated to be 5 years to enroll 400 par-
              months, and every 3 months thereafter until 5 years. After 5 years,                ticipants. With final patient follow-up 2 years after enrollment,
              follow-up continued to occur every 3 to 6 months depending on                      the total duration of the planned trial was 7 years.
              a patient’s condition as judged by the surgeon in charge. A clini-
              cal research coordinator interviewed participants about self-                      Statistical Analysis
              reported adherence at every visit to the outpatient clinic of the                  All patients who underwent randomization were included in this
              International University of Health and Welfare Hospital. The co-                   analysis. Relapse- and death-related outcomes were assessed ac-
              ordinator sometimes made telephone calls to participants to con-                   cording to randomization group whether or not supplements were
              firm their health condition and adherence, and again confirmed                     taken, whereas adverse events were assessed only in patients who
              their adherence when she provided a new bottle of trial medi-                      continued to take the supplements (per protocol). The effects of
              cation every 6 months. Moreover, levels of 25(OH)D were mea-                       vitamin D and placebo on risk of relapse or death and total deaths
              sured annually in blood samples to determine changes in the                        were estimated using Nelson-Aalen cumulative hazard curves for
              vitamin D and placebo groups. Preoperative and postoperative                       outcomes. A Cox proportional hazards model was used to deter-
              chemotherapy was administered to patients with stage II and III                    minehazardratios(HRs)and95%confidenceintervals.Subgroups
              esophageal cancer. Postoperative chemotherapy was admin-                           were prespecified according to 25(OH)D levels at baseline—low
              istered to patients with stage II and III gastric cancer15 and all                 (<20 ng/mL), middle (20-40 ng/mL), or high (>40 ng/mL)—and
              patients with stage III colorectal cancer.16 Local radiation or                    by SNPs of vitamin D receptor and vitamin D binding protein. Pa-
              molecular-targeting therapy was combined with chemotherapy                         tients with missing data for 25(OH)D levels at baseline were not
              for selected patients with relapse. When vitamin D supplemen-                      included in the subgroup analyses. To clarify whether vitamin D
              tation was medically required for conditions such as bone frac-                    supplementation significantly affected these subgroups, P values
              ture or osteoporosis, trial supplementation was stopped, but the                   for interaction were analyzed based on a Cox regression model
              patients were followed up until the end of the study.                              that included treatment allocation, baseline 25(OH)D group, and
                                                                                                 treatment allocation and baseline 25(OH)D group multiplied to-
              Vitamin D Measurements                                                             gether as an interaction variable by 2-way interaction tests com-
              Serum levels of 25(OH)D were measured using radioimmuno-                           paring the low and middle subgroups; the high-baseline-level sub-
              assay (SRL Inc, Hachioji, Tokyo, Japan) as previously described17                  group was not included because of the small number of patients
              and every year (within the same calendar month) after starting                     in that subgroup. Values with a 2-sided P < .05 were considered
              supplements. Using 19 serum samples obtained from a differ-                        statistically significant. However, because of the potential for
              ent cohort, blinded duplicates were tested for this 25(OH)D assay                  type I error due to multiple comparisons, findings for subgroup
              and the correlation coefficient was 0.92.                                          analyses should be interpreted as exploratory.
                                                                                                      All data were analyzed using Stata version 14.0 (StataCorp).
              SNP Analyses of Vitamin D Receptor                                                 Annual interim analyses were planned after entry of 200 pa-
              and Vitamin D Binding Protein                                                      tients. Statistical significance at the interim analysis was set at
              Analyses were conducted of particular SNPs associated with the                     P<.001 according to Peto stopping boundaries20 because it uses
              vitamin D receptor. These included FokI (rs2228570); BsmI                          constant but stringent stopping levels independent of the num-
              (rs1544410); CDX2 (rs11568820); ApaI (rs7976091); and TaqI                         ber of interim analyses that could not be exactly predicted.
              (rs731236) because they have been reported to be associated with                        There were a number of post hoc analyses. First, the pro-
              function of the vitamin D receptor.18 Moreover, among SNPs of                      portional hazards assumption was tested using Schoenfeld
              vitamin D binding protein, DBP1 (rs7041) and DBP2 (rs4588) were                    residuals.21 Second, to evaluate the effects of vitamin D supple-
              chosen because these SNPs are missense mutations that influence                    mentation on relapse, cumulative incidence functions were ap-
              serum levels of 25(OH)D.13,14 DNA was extracted from peripheral                    plied by considering patient deaths due to causes other than
              blood samples and stored at −80°C. DNA fragments were ampli-                       relapse as a competing risk; competing risk regression was per-
              fied by polymerase chain reaction. The SNPs were determined by                     formed using subdistribution HRs and 95% confidence
              direct sequencing, for which the detailed methods were described                   intervals.22 Third, because patients in the vitamin D group were
              in a previous article19 and in eAppendix 1 in Supplement 1.                        older and had more stage I disease than in the placebo group,
                                                                                                 HRs were adjusted by age quartiles or stage I disease status.
              Sample Size                                                                        Fourth, multiple imputation was performed with a Markov
              When raw data from the cohort of 257 patients with colorectal can-                 chain Monte Carlo technique using multivariable normal re-
              cer were studied at the Jikei University School of Medicine,7 5-year               gression repeated 50 times for missing 25(OH)D data using

              jama.com                                                                                                (Reprinted) JAMA April 9, 2019 Volume 321, Number 14     1363

                                                          © 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/30/2026

```

### DOC001 PDF page 4

[Supplied main PDF page 4](../../../jama_urashima_2019_oi_190023.pdf#page=4)

```text
               Research Original Investigation                                  Effect of Vitamin D Supplementation on Relapse-Free Survival in Patients With Digestive Tract Cancers



                                                                                                     in the vitamin D group and 10 (6.0%) in the placebo group
               Figure 1. Patient Flow Through the AMATERASU Trial
                                                                                                     (Figure 1). In addition, 9 (3.6%) in the vitamin D group and 9
                                                                                                     (5.4%) in the placebo group stopped trial medication for medi-
                                      439 Patients assessed for eligibility
                                                                                                     cal reasons such as swallowing disorder, fracture and osteopo-
                                                             22 Excluded
                                                                                                     rosis, and urinary stones. Therefore, 10.3% of participants
                                                                15 Declined to participate           stopped taking study medication before censoring, but all 417 pa-
                                                                 5 Did not meet inclusion criteria   tients were included in the efficacy analyses.
                                                                 2 Other reasons
                                                                                                          The median and maximum follow-up periods respectively
                                                                                                     were 3.5 (IQR, 2.3-5.4) years and 7.6 years in the vitamin D group
                                               417 Randomized                                        and 3.5 (IQR, 2.3-5.0) years and 7.4 years in the placebo group.
                                                                                                     Table 1 shows the characteristics of the patients, all of whom were
                251 Randomized to receive vitamin D          166 Randomized to receive placebo       Japanese. Of the 417 participants, 34% were women. The median
                    251 Received vitamin D as                   166 Received placebo as              age was 66 years and the median body mass index was 22. Per-
                        randomized                                   randomized
                                                                                                     centages of cancer sites were as follows: esophagus, 9.6%; stom-
                   1 Lost to follow-up within 6 mo              19 Stopped study medication
                                                                                                     ach, 41.7%; small bowel, 0.5%; and colorectal, 48.2%. Disease
                  23 Stopped study medication                      10 Nonmedical reasons             stages were I, II, and III in 44%, 26%, and 30% of patients, respec-
                     14 Nonmedical reasons                            2 Within 1 y                   tively. The median age of patients was 67 (IQR, 61-75) years in the
                        3 Within 1 y                                  7 Between 1 and 2 y
                        9 Between 1 and 2 y                           1 After 2 y                    vitamin D group and 64 (IQR, 58-71) years in the placebo group.
                        2 After 2 y                                 9 Medical reasons                The percentage of patients with stage I disease was 46% in the
                      9 Medical reasons                               4 Within 1 y
                        4 Within 1 y                                  5 Between 1 and 2 y            vitamin D group and 40% in the placebo group.
                        5 Between 1 and 2 y

                                                                                                     Effects of Vitamin D Supplementation
                  251 Included in primary analysis            166 Included in primary analysis       Relapse or death occurred in 50 patients (20%) taking vita-
                                                                                                     min D and 43 patients (26%) taking placebo. Among the par-
                                                                                                     ticipants, 37 (15%) of 251 in the vitamin D group and 25 (15%)
               patient age and sex and serum levels of calcium, alkaline phos-                       of 166 in the placebo group died. Relapse, cancer-specific death,
               phatase, and parathyroid hormone.                                                     and noncancer death respectively occurred in 41 (16%), 27
                    Fifth, subgroup analyses for cancer site, stages, major pathol-                  (11%), and 10 (4%) patients in the vitamin D group and in 36
               ogy, sex, body mass index, and age were performed. Sixth, be-                         (22%), 16 (10%), and 9 (5%) patients in the placebo group.
               cause levels of 25(OH)D were not increased among all patients                              The primary outcome of 5-year relapse-free survival in the
               randomized to vitamin D supplementation, participants were                            vitamin D group vs placebo group was 77% vs 69%. Vitamin D
               stratified by their mean 25(OH)D levels over the course of the trial,                 supplementation did not significantly reduce risk of relapse
               including at baseline and during annual blood sampling, inde-                         or death compared with placebo (HR, 0.76; 95% CI, 0.50-1.14;
               pendent of vitamin D supplementation (<20, 20 to <30, 30 to <40,                      P = .18) (Figure 2A). The secondary outcome of 5-year overall
               40 to <50, or ≥50 ng/mL). Nelson-Aalen cumulative hazard curves                       survival was 82% in the vitamin D group vs 81% in the pla-
               of relapse or death were drawn by these stratified groups (eFig-                      cebo group (HR for death, 0.95; 95% CI, 0.57-1.57; P = .83)
               ure 1, A and B, and eTable 1 in Supplement 2). Seventh, changes                       (Figure 2B). Hazard ratios for cancer-specific death and non-
               in the median levels of serum 25(OH)D and calcium from base-                          cancer death are shown in Table 2.
               line to 1 year in each group was analyzed using Wilcoxon signed
               rank test; change ratios at 1 year were compared between the vi-                      Associations With Prespecified Subgroups:
               tamin D and placebo groups using the Mann-Whitney test.                               25(OH)D Levels and SNPs
                                                                                                     Patients were divided into prespecified subgroups according
                                                                                                     to low (<20 ng/mL [n = 173]), middle (20-40 ng/mL [n = 232]),
                                                                                                     or high (>40 ng/mL [n = 5]) serum levels of 25(OH)D at base-
               Results                                                                               line. Because of the small number of patients in the high-
               Study Population                                                                      baseline-level subgroup, further analyses within this sub-
               There were 3 interim analyses, but the trial was continued un-                        group were not conducted. Vitamin D supplementation
               til the number of entries exceeded 400 because the stopping rule                      increased median 25(OH)D levels from 26.5 (IQR, 23-30) ng/mL
               was not met. Figure 1 shows the flow of the 417 patients with di-                     to 45 (IQR, 36-57) ng/mL after 1 year in the middle-baseline-
               gestive tract cancers who were randomized to receive vitamin D                        level subgroup, whereas they increased from 16 (IQR,
               supplementation (n = 251 [60%]) or placebo (n = 166 [40%]) be-                        13-18) ng/mL to 36 (IQR, 27-47) ng/mL in the low-baseline-
               tween January 2010 and April 2016. At a median 23.5 (interquar-                       level subgroup (eFigure 2 in Supplement 2).
               tile range [IQR], 13-44) days after operation, participants were                           In the middle-baseline-level subgroup, 5-year relapse-
               randomized and started study medication. All surviving patients                       free survival was significantly higher in the vitamin D group
               were followed up until February 2018 except 1 patient who was                         than in the placebo group (85% vs 71%; HR for relapse or death,
               lost to follow-up at 1 month (follow-up rate, 99.8%). The num-                        0.46; 95% CI, 0.24-0.86; P = .02) (Figure 3A). There was no sig-
               ber of participants who stopped trial medication for nonmedi-                         nificant difference for relapse-free survival in the low-baseline-
               cal reasons, including the 1 patient lost to follow-up, was 15 (6.0%)                 level subgroup (HR, 1.15; 95% CI, 0.65-2.05) (Figure 3B). There

        1364   JAMA April 9, 2019 Volume 321, Number 14 (Reprinted)                                                                                                        jama.com

                                                             © 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/30/2026

```

### DOC001 PDF page 5

[Supplied main PDF page 5](../../../jama_urashima_2019_oi_190023.pdf#page=5)

```text
              Effect of Vitamin D Supplementation on Relapse-Free Survival in Patients With Digestive Tract Cancers                                Original Investigation Research




              Table 1. Participant Characteristics                                               Table 1. Participant Characteristics (continued)

                                          No. (%) of Participantsa                                                              No. (%) of Participantsa
                                          Vitamin D                  Placebo                                                    Vitamin D                  Placebo
               Characteristics            (n = 251)                  (n = 166)                       Characteristics            (n = 251)                  (n = 166)
               Male                       173 (69)                   103 (62)                        Single-nucleotide
                                                                                                     polymorphism
               Female                     78 (31)                    63 (38)
                                                                                                       FokI
               Age quartile, y
                                                                                                         CC                     92 (38)                    57 (36)
                 35-59                    51 (20)                    50 (30)
                                                                                                         CT                     117 (48)                   75 (48)
                 60-65                    55 (22)                    41 (25)
                                                                                                         TT                     36 (15)                    25 (16)
                 66-73                    63 (25)                    48 (29)
                                                                                                       BsmI
                 74-90                    82 (33)                    27 (16)
                                                                                                         AA                     14 (6)                     8 (5)
               Body mass index
               quartileb                                                                                 AG                     42 (18)                    23 (15)
                 15.0-19.7                63 (25)                    36 (22)                             GG                     175 (76)                   119 (79)
                 19.8-21.8                62 (25)                    43 (26)                           Cdx2
                 21.9-23.7                59 (24)                    45 (27)                             GG                     89 (39)                    49 (33)
                 23.8-37.3                65 (26)                    41 (25)                             GA                     103 (45)                   77 (51)
               History of                 9 (4)                      7 (4)                               AA                     38 (17)                    24 (16)
               other cancers
                                                                                                       ApaI
               Comorbid
               conditions                                                                                GG                     96 (42)                    69 (46)
                 Hypertension             103 (41)                   58 (35)                             GT                     104 (45)                   61 (40)
                 Diabetes                 44 (18)                    24 (14)                             TT                     31 (13)                    20 (13)
                 mellitus
                                                                                                       TaqI
                 Endocrine                33 (13)                    18 (11)
                 disease                                                                                 TT                     172 (74)                   115 (77)
                 Cardiovascular           22 (9)                     9 (5)                               TC                     54 (23)                    31 (21)
                 disease
                                                                                                         CC                     5 (2)                      4 (3)
                 Chronic kidney           5 (2)                      1 (1)
                 disease                                                                               DBP1
                 Asthma                   3 (1.2)                    0 (0.0)                             TT                     134 (58)                   82 (55)
                 Orthopedic               1 (0.4)                    1 (0.6)                             TG                     87 (38)                    57 (39)
                 disease
                                                                                                         GG                     10 (4)                     9 (6)
               Site of cancer
                                                                                                       DBP2
                 Esophagus                22 (9)                     18 (11)
                                                                                                         CC                     115 (50)                   81 (54)
                 Stomach                  106 (42)                   68 (41)
                                                                                                         CA                     91 (39)                    58 (39)
                 Small bowel              1 (0.4)                    1 (0.6)
                                                                                                         AA                     25 (11)                    11 (7)
                 Colorectal               122 (49)                   79 (48)
                                                                                                 a
               Cancer stage                                                                          Percentages may not sum to 100% because of rounding.
                                                                                                 b
                                                                                                     Calculated as weight in kilograms divided by height in meters squared.
                 I                        115 (46)                   67 (40)
                                                                                                 c
                                                                                                     Neuroendocrine tumor (n=4); adenoid cystic carcinoma (n=1); unclassified (n=1).
                 II                       63 (25)                    48 (29)
                 III                      73 (29)                    51 (31)
               Pathology                                                                         was a significant 2-way interaction between the middle and
                 Adenocarcinoma           226 (90)                   147 (88)                    low subgroups (P = .04 for interaction). Overall survival was
                 Squamous cell            22 (9)                     16 (10)                     not significantly different between the vitamin D and pla-
                 carcinoma
                                                                                                 cebo groups in both the middle subgroup (HR for death, 0.60;
                 Otherc                   3 (1)                      3 (2)                       95% CI, 0.28-1.30) (Figure 3C) and the low subgroup (HR for
               Baseline                                                                          death, 1.36; 95% CI, 0.66-2.81) (Figure 3D) (P = .13 for interac-
               25-hydroxyvitamin D
               level, ng/mL                                                                      tion). Subgroup analyses between the middle and low sub-
                 Low: <20                 102 (41)                   71 (44)                     groups for cancer-specific death and noncancer death are
                 Middle: 20-40            142 (58)                   90 (56)                     shown in Table 2.
                                                                                                     Significant associations were not seen between sub-
                 High: >40                4 (1.6)                    1 (0.6)
                                                                                                 groups of SNPs (eFigure 3, A-U, in Supplement 2).
               Adjuvant                   88 (35)                    60 (36)
               chemotherapy

                                                                                 (continued)
                                                                                                 Post Hoc Analyses
                                                                                                 Results of the proportional hazards assumption test were not sig-
                                                                                                 nificant, supporting validity of the Cox proportional hazards

              jama.com                                                                                                 (Reprinted) JAMA April 9, 2019 Volume 321, Number 14            1365

                                                          © 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/30/2026

```

### DOC001 PDF page 6

[Supplied main PDF page 6](../../../jama_urashima_2019_oi_190023.pdf#page=6)

```text
               Research Original Investigation                                                                                 Effect of Vitamin D Supplementation on Relapse-Free Survival in Patients With Digestive Tract Cancers



                                                                                                                                                         Using methods for competing-risk analysis, the cumula-
               Figure 2. Effect of Vitamin D Supplementation on Outcomes
                                                                                                                                                    tive incidence of relapse was compared, and there was no sig-
                A Relapse or death                                                                                                                  nificant difference (subdistribution HR, 0.75; 95% CI, 0.48-
                                                                                                                                                    1.17; P = .21) (Figure 2C). In the subgroup with middle baseline
                                                               0.8




                       Cumulative Hazard of Relapse or Death
                                                                         Hazard ratio, 0.76; 95% CI, 0.50-1.14; P = .18                             levels of 25(OH)D, the cumulative incidence of relapse was sig-
                                                                                                                                                    nificantly lower in the vitamin D group than in the placebo
                                                               0.6                                                                                  group (subdistribution HR, 0.44; 95% CI, 0.21-0.89; P = .02)
                                                                                                                                                    (Table 2). There was no significant difference for the cumula-
                                                               0.4                                                                                  tive incidence of relapse in the low-baseline-level subgroup
                                                                                                                                                    (subdistribution HR, 1.18; 95% CI, 0.64-2.19). There was a sig-
                                                                                                  Placebo
                                                                                                                                                    nificant 2-way interaction between the middle- and low-
                                                               0.2
                                                                                                     Vitamin D                                      baseline-level subgroups (P = .04 for interaction).
                                                                                                                                                         Because patients were older in the vitamin D group than
                                                                0
                                                                     0            1           2              3          4           5         6     in the placebo group (Table 1), HRs were adjusted by age quar-
                                                                                            Years After Randomization                               tile. In this adjusted analysis, the cumulative hazard of re-
               No. at risk                                                                                                                          lapse or death was significantly less in the vitamin D group
                Placebo    166                                                  148          113             84        54          34        16
                Vitamin D 251                                                   222          176            130        93          65        35
                                                                                                                                                    compared with the placebo group, with an adjusted HR of 0.66
                                                                                                                                                    (95% CI, 0.43-0.99; P = .048). In contrast, the cumulative haz-
                B   Death                                                                                                                           ard of death was not significantly different, with an adjusted
                                                                                                                                                    HR of 0.81 (95% CI, 0.48-1.36; P = .42). Patients with stage I
                                                               0.8
                                                                         Hazard ratio, 0.95; 95% CI, 0.57-1.57; P = .83                             cancer were more prevalent in the vitamin D group; analyses
                                                                                                                                                    adjusted for stage I disease status did not show any signifi-




                       Cumulative Hazard of Death
                                                               0.6                                                                                  cant differences.
                                                                                                                                                         Interactions between vitamin D supplementation and the
                                                               0.4                                                                                  following subgroups were examined, but no significant asso-
                                                                                                                                                    ciations were found: men vs women (eFigure 4, A and B, in
                                                                                                                                                    Supplement 2); age 65 years or younger vs older than 65 years
                                                               0.2
                                                                                        Placebo                                                     (eFigure 5, A and B, in Supplement 2); body mass index less
                                                                                                    Vitamin D                                       than 25 vs 25 or higher (eFigure 6, A and B, in Supplement 2);
                                                                0
                                                                     0            1           2              3          4           5         6     site of cancer: esophageal, gastric, or colorectal (eFigure 7, A-C,
                                                                                            Years After Randomization                               in Supplement 2); disease stage: I, II, or III (eFigure 8, A-C, in
               No. at risk                                                                                                                          Supplement 2); and adenocarcinoma vs nonadenocarcinoma
                Placebo    166                                                  160          128             94         62         42        20
                Vitamin D 251                                                   245          196            145        104         73        37
                                                                                                                                                    (eFigure 9, A and B, in Supplement 2).
                                                                                                                                                         Median 25(OH)D levels increased significantly in the vi-
                C   Relapse by competing-risk analysis                                                                                              tamin D group, from 21 (IQR, 16-27) ng/mL to 41 (IQR,
                                                                                                                                                    33-55) ng/mL (P < .001), but did not change significantly in the
                                                               0.8
                                                                         Subdistribution hazard ratio, 0.75; 95% CI, 0.48-1.17; P = .21             placebo group, from 21 (IQR, 15-27) ng/mL to 20 (IQR, 15-27)




                        Cumulative Incidence of Relapse
                                                                                                                                                    ng/mL (P = .91). The change ratio of 25(OH)D level was 87% in
                                                               0.6                                                                                  the vitamin D group vs 0% in the placebo group 1 year after
                                                                                                                                                    starting study medication (P < .001). Levels of 25(OH)D in the
                                                               0.4                                                                                  vitamin D group remained high over 4 years of trial follow-
                                                                                                                                                    up, while those in the placebo group remained low (eFigure 2
                                                                                                                              Placebo               in Supplement 2). Analyses by mean 25(OH)D level during the
                                                               0.2
                                                                                                                  Vitamin D                         trial are shown in eTable 1 and eFigure 1, A and B. Changes in
                                                                                                                                                    median serum calcium levels were not significantly different
                                                                0
                                                                     0            1           2              3          4           5         6     in the vitamin D group (from 9.3 [IQR, 8.9-9.6] mg/dL to 9.3
                                                                                             Years After Randomization                              [IQR, 9.1-9.6] mg/dL; P = .09) or in the placebo group (from 9.3
                                                                                                                                                    [IQR, 9.0-9.6] mg/dL to 9.3 [IQR, 9.1-9.5] mg/dL; P = .44). The
               Nelson-Aalen cumulative hazard curves are shown for (A) relapse or death and                                                         change ratio of calcium was 0% in both the vitamin D and pla-
               (B) total deaths. In panel C, the cumulative incidence of relapse is compared between
                                                                                                                                                    cebo groups (P = .10).
               the vitamin D and placebo groups by considering patient deaths due to causes
               otherthanrelapseasthecompetingrisk.Medianobservationtimesforrelapseordeath
               were, for placebo, 3.0 (interquartile range [IQR], 1.9-4.5) years, and for vitamin D,                                                Adverse Events
               3.3 (IQR, 1.9-5.3) years; for total deaths, for placebo, 3.5 (IQR, 2.3-5.0) years,                                                   In the per-protocol analysis of participants continuing to take
               and for vitamin D, 3.5 (IQR, 2.3-5.4) years; and for relapse by competing-risk analysis,
               for placebo, 3.0 (IQR, 1.9-4.5) years, and for vitamin D, 3.3 (IQR, 1.9-5.3) years.                                                  study medication until censoring, fractures occurred in 3 pa-
                                                                                                                                                    tients (1.3%) in the vitamin D group and 5 patients (3.4%) in
               models used in the analyses. There were 7 patients with missing                                                                      the placebo group; urinary stones occurred in 2 (0.9%) vs 0 pa-
               25(OH)D levels, and results using multiple imputation were con-                                                                      tients, respectively (Table 3). No patients developed hyper-
               sistent with the primary results (eTable 2 in Supplement 2).                                                                         calcemia during the follow-up period.

        1366   JAMA April 9, 2019 Volume 321, Number 14 (Reprinted)                                                                                                                                                       jama.com

                                                                                                            © 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/30/2026

```

### DOC001 PDF page 7

[Supplied main PDF page 7](../../../jama_urashima_2019_oi_190023.pdf#page=7)

```text
              Effect of Vitamin D Supplementation on Relapse-Free Survival in Patients With Digestive Tract Cancers                                                                                                                                  Original Investigation Research




              Table 2. Effect of Vitamin D Supplementation on Relapse, Cancer-Specific Death,
              and Noncancer Deatha

                                                                                                              Baseline Serum 25-Hydroxyvitamin D Level, ng/mL                                                              P Value
                                                                                     Total Study                                                                                                                           for
               Outcomes                                                              Population               <20                                20-40                                                                     Interaction
               Relapse                                                                                                                                                                                                     .04
                   Subdistribution HR                                                0.75 (0.48-1.17)         1.18 (0.64-2.19)                   0.44 (0.21-0.89)
                   (95% CI)
                   P value                                                           .21                      .59                                .02
               Cancer-specific death                                                                                                                                                                                       .35
                   HR (95% CI)                                                       1.09 (0.58-2.01)         1.45 (0.63-3.38)                   0.78 (0.29-2.10)
                   P value                                                           .80                      .38                                .63
                                                                                                                                                                                                                                              a
                                                                                                                                                                                                                                                  Hazard ratio (HR) values greater
               Noncancer death                                                                                                                                                                                             .27
                                                                                                                                                                                                                                                  than 1 indicate that vitamin D
                   HR (95% CI)                                                       0.70 (0.29-1.73)         1.11 (0.26-4.65)                   0.39 (0.11-1.39)                                                                                 supplementation was associated
                                                                                                                                                                                                                                                  with a decreased probability
                   P value                                                           .44                      .89                                .15
                                                                                                                                                                                                                                                  of the outcome.



              Figure 3. Subgroup Analysis

               A Relapse or death, baseline 25 (OH)D level 20-40 ng/mL                                                                                   B   Relapse or death, baseline 25 (OH)D level <20 ng/mL

                                                              0.5                                                                                                                                       0.5




                      Cumulative Hazard of Relapse or Death                                                                                                     Cumulative Hazard of Relapse or Death
                                                                        Hazard ratio, 0.46; 95% CI, 0.24-0.86; P = .02                                                                                            Hazard ratio, 1.15; 95% CI, 0.65-2.05; P = .63

                                                              0.4                                                                                                                                       0.4
                                                                                                                                  Placebo
                                                                                                                                                                                                                                     Vitamin D
                                                              0.3                                                                                                                                       0.3
                                                                                                                                                                                                                                                      Placebo

                                                              0.2                                                                                                                                       0.2

                                                                                                                            Vitamin D
                                                              0.1                                                                                                                                       0.1


                                                               0                                                                                                                                         0
                                                                    0            1           2           3            4      5              6                                                                 0            1           2             3           4       5           6
                                                                                           Years After Randomization                                                                                                                 Years After Randomization
              No. at risk                                                                                                                               No. at risk
               Placebo    90                                                    83           63          49           30     18              9           Placebo    71                                                    61          46            31           20      13           5
               Vitamin D 142                                                   132          111          85           58     38             20           Vitamin D 102                                                    84          61            43           33      26          15


               C   Death, baseline 25 (OH)D level 20-40 ng/mL                                                                                            D Death, baseline 25 (OH)D level <20 ng/mL

                                                              0.5                                                                                                                                       0.5
                                                                        Hazard ratio, 0.60; 95% CI, 0.28-1.30; P = .20                                                                                            Hazard ratio, 1.36; 95% CI, 0.66-2.81; P = .41




                      Cumulative Hazard of Death                                                                                                                Cumulative Hazard of Death
                                                              0.4                                                                                                                                       0.4


                                                              0.3                                                                                                                                       0.3
                                                                                                                                                                                                                                                     Vitamin D
                                                                                                                            Placebo
                                                              0.2                                                                                                                                       0.2
                                                                                                                                                                                                                                                            Placebo
                                                              0.1                                                                                                                                       0.1
                                                                                                          Vitamin D
                                                               0                                                                                                                                         0
                                                                    0            1           2           3            4      5              6                                                                 0            1           2             3           4       5           6
                                                                                           Years After Randomization                                                                                                                 Years After Randomization
              No. at risk                                                                                                                               No. at risk
               Placebo    90                                                    88           70          51           34     22             11           Placebo    71                                                    68          54            39           24      17          7
               Vitamin D 142                                                   139          115          88           61     41             20           Vitamin D 102                                                   100          75            54           40      31          17


              Nelson-Aalen cumulative hazard curves are shown for relapse or death in the                                                              were, for placebo, 3.4 (interquartile range [IQR], 1.9-4.5) years, and for
              subgroups of (A) middle (20-40 ng/mL) and (B) low (<20 ng/mL) serum                                                                      vitamin D, 3.8 (IQR, 2.4-5.3) years; and in the low 25(OH)D subgroup, for
              hydroxyvitamin D (25[OH]D) baseline levels and for total deaths in the                                                                   placebo, 2.8 (IQR, 1.8-4.4) years, and for vitamin D, 2.5 (IQR, 1.6-5.2) years.
              subgroups of (C) middle and (D) low serum 25(OH)D baseline levels. There were                                                            Median observation times for total deaths in the middle 25(OH)D subgroup
              only 5 patients with high (>40 ng/mL) 25(OH)D baseline levels; this group was                                                            were, for placebo, 3.5 (IQR, 2.3-5.0) years, and for vitamin D, 3.8 (IQR, 2.5-5.4)
              not evaluated. Numbers at risk for panel C are not given because of weighting.                                                           years; and in the low 25(OH)D subgroup, for placebo, 3.4 (IQR, 2.1-5.0 years),
              Median observation times for relapse or death in the middle 25(OH)D subgroup                                                             and for vitamin D, 3.3 (IQR, 1.9-5.4) years.



              jama.com                                                                                                                                                                                            (Reprinted) JAMA April 9, 2019 Volume 321, Number 14                    1367

                                                                                                        © 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/30/2026

```

### DOC001 PDF page 8

[Supplied main PDF page 8](../../../jama_urashima_2019_oi_190023.pdf#page=8)

```text
               Research Original Investigation                                   Effect of Vitamin D Supplementation on Relapse-Free Survival in Patients With Digestive Tract Cancers




               Table 3. Safety Outcomes

                                              No. (%) of Participants
                                              Per Protocola
                                              Adherent Until Censoring                        Adherent for 1 y                             By Randomization Groupb
                   Outcomes                   Vitamin D (n = 227)     Placebo (n = 147)       Vitamin D (n = 243)    Placebo (n = 160)     Vitamin D (n = 251)   Placebo (n = 166)
                   Fracture                   3 (1.3)                 5 (3.4)                 3 (1.2)                6 (3.8)               3 (1.2)               6 (3.6)
                   Urinary stones             2 (0.9)                 0 (0.0)                 4 (1.6)                2 (1.3)               4 (1.6)               4 (2.4)
                   Severe adverse eventsc     19 (8.4)                9 (6.1)                 20 (8.2)               13 (8.1)              21 (8.4)              15 (9.0)
                   Cancer de novod            15 (6.6)                8 (5.4)                 16 (6.6)               9 (5.6)               16 (6.4)              9 (5.4)
               a                                                                                       b
                   Safety outcomes were analyzed per protocol (ie, patients who continued to take        Analyzed according to randomization group independent of adherence.
                                                                                                       c
                   study medication until censorship or for more than 1 year) because per-protocol       Adverse events that resulted in admission.
                                                                                                       d
                   analysis is considered to be more sensitive for safety outcomes. One participant      Cancer that appeared de novo in organs other than the site of the primary
                   lost to follow-up in the vitamin D group was considered nonadherent.                  cancer after starting study medication.



                                                                                                       cancer (although with a nonsignificant interaction test).24 It
               Discussion                                                                              is possible that the optimal range of serum 25(OH)D levels with
                                                                                                       respect to survival may be quite different among types of can-
               Among patients with digestive tract cancer, vitamin D supple-                           cers. In addition, the supplement dosage of 2000 IU/d in the
               mentation, compared with placebo, did not reduce risks of re-                           trial may have been insufficient to increase vitamin D levels
               lapse or death, death due to any cause, or relapse.                                     sufficiently in the subgroup with low 25(OH)D levels.
                    A similar RCT that included 155 patients found that 1200 IU/d                           Findings regarding adverse events must also be consid-
               of vitamin D supplementation did not improve relapse-free sur-                          ered exploratory because the study was not designed with suf-
               vival or overall survival of patients with non–small cell lung                          ficient power to detect significant differences. However, the
               cancer.23 However, a meta-analysis of 64 observational stud-                            relatively high dosage of vitamin D did not appear to be asso-
               ies with a total of 44 165 patients with cancer found higher                            ciated with frequent adverse events.
               25(OH)D levels to be associated with better progression-free and
               overall survival.24 In addition, a meta-analysis of individual par-                     Limitations
               ticipant data from 8 cohort studies in Europe and the United                            This trial has several limitations. First, the study population in-
               States found higher cancer mortality in patients in the lowest                          cluded patients with a mixture of cancers with biological and
               quintiles of 25(OH)D levels among people with a history of                              clinical differences. Although post hoc subgroup analyses were
               cancer.25 Discrepancies between the results of these RCTs and                           performed for each tumor type and stage and for adenocarcinoma
               meta-analyses of observational studies suggest that higher                              vs nonadenocarcinoma, the sample size may have been too small
               25(OH)D levels can be largely confounded by healthy lifestyles26                        to detect significant differences in each subgroup. Second, pa-
               that include daily physical activity.27,28                                              tients were periodically examined (every 1-6 months) as outpa-
                    The recent VITAL study, an RCT that also used a vitamin D                          tients by computed tomography, magnetic resonance imaging,
               dosage of 2000 IU/d for primary prevention of cancer, enrolled                          positron emission tomography, and other procedures to exclude
               25 871 participants without a history of cancer. In that study, there                   cancer relapse as deemed necessary. This variability in follow-
               was no reduction in risk of cancer mortality, but a post hoc analy-                     up mode and timing may have led to inaccuracy in measured time
               sissuggestedapossiblebenefitofvitaminDafterexclusionofearly                             to relapse. Third, approximately 10% of the participants stopped
               follow-up data.29 A meta-analysis30 of 3 other RCTs8,31,32 found                        taking study medication during the trial, and adherence was
               that vitamin D supplementation was significantly associated with                        based only on patient self-report, which may have caused a bias
               lower total cancer mortality, even though each individual trial had                     toward null results. Fourth, only 5 patients had high levels of
               null results. The study population in the current trial included dis-                   25(OH)D at baseline, too few to allow statistical evaluation. Fifth,
               tinct entities with biological and clinical differences—eg, esoph-                      the prespecified 25(OH)D cutoffs of 20 ng/mL and 40 ng/mL were
               ageal cancer, gastric cancer, or colorectal cancer; stage I, II, or III                 based on published reports of primary prevention of incident can-
               cancer; and adenocarcinoma and nonadenocarcinoma. However,                              cer, but these cutoff points might be inappropriate in a clinical
               the power may have been too low to detect differences in these                          trial of secondary prevention of cancer relapse and death. Sixth,
               subgroups. It may therefore be useful to include the data in this                       7 patients had missing 25(OH)D levels, although multiple impu-
               trial in an individual patient data meta-analysis.                                      tation produced consistent results. Seventh, radiological images
                    In the current study, vitamin D was effective only in a sub-                       were not reviewed centrally by a blinded independent third party,
               group of patients with middle (20-40 ng/mL) serum 25(OH)D                               although the trial was double blinded.
               levels at baseline. However, this finding must be considered
               exploratory and interpreted with caution in the context of the
               null findings for the primary outcome measures in the total
               population, as well as the potential for type I error due to mul-
                                                                                                       Conclusions
               tiple comparisons. It was hypothesized that vitamin D would                             Among patients with digestive tract cancer, vitamin D supple-
               be effective in the subgroup with low 25(OH)D at baseline, as                           mentation, compared with placebo, did not result in signifi-
               was observed in an RCT for a subgroup of patients with lung                             cant improvement in relapse-free survival at 5 years.

        1368   JAMA April 9, 2019 Volume 321, Number 14 (Reprinted)                                                                                                          jama.com

                                                               © 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/30/2026

```

### DOC001 PDF page 9

[Supplied main PDF page 9](../../../jama_urashima_2019_oi_190023.pdf#page=9)

```text
ARTICLE INFORMATION
Accepted for Publication: February 18, 2019.
Author Contributions: Dr Urashima had full access
to all of the data in the study and takes
responsibility for the integrity of the data and the
accuracy of the data analysis.
Concept and design: Urashima, Ohdaira, Yoshida,
Kitajima, Suzuki.
Acquisition, analysis, or interpretation of data:
Urashima, Akutsu, Okada, Yoshida.
Drafting of the manuscript: Urashima, Ohdaira,
Yoshida, Kitajima.
Critical revision of the manuscript for important
intellectual content: Akutsu, Okada, Suzuki.
Statistical analysis: Urashima, Yoshida.
Obtained funding: Urashima, Yoshida.
Administrative, technical, or material support:
Ohdaira, Akutsu, Okada, Suzuki.
Supervision: Okada, Kitajima.
Conflict of Interest Disclosures: None reported.
Funding/Support: This research was supported by
the Ministry of Education, Culture, Sports, Science,
and Technology in the Japan-Supported Program
for the Strategic Research Foundation at Private
Universities, funding from the International
University of Health and Welfare Hospital, and Jikei
University School of Medicine.
Role of the Funder/Sponsor: None of the funding
organizations had any role in the design and
conduct of the study; collection, management,
analysis, and interpretation of the data;
preparation, review, or approval of the manuscript;
or decision to submit the manuscript for
publication.
Data Sharing Statement: See Supplement 3.
REFERENCES
1. Bikle D. Nonclassic actions of vitamin D. J Clin
Endocrinol Metab. 2009;94(1):26-34. doi:10.1210/
jc.2008-1454
2. van Harten-Gerritsen AS, Balvers MGJ, Witkamp
RF, Kampman E, van Duijnhoven FJB. Vitamin D,
inflammation, and colorectal cancer progression:
a review of mechanistic studies and future
directions for epidemiological studies. Cancer
Epidemiol Biomarkers Prev. 2015;24(12):1820-1828.
doi:10.1158/1055-9965.EPI-15-0601
3. Garland CF, Comstock GW, Garland FC,
Helsing KJ, Shaw EK, Gorham ED. Serum
25-hydroxyvitamin D and colon cancer: eight-year
prospective study. Lancet. 1989;2(8673):1176-1178.
doi:10.1016/S0140-6736(89)91789-3
4. Giovannucci E, Liu Y, Rimm EB, et al. Prospective
study of predictors of vitamin D status and cancer
incidence and mortality in men. J Natl Cancer Inst.
2006;98(7):451-459. doi:10.1093/jnci/djj101
5. Ng K, Meyerhardt JA, Wu K, et al. Circulating
25-hydroxyvitamin d levels and survival in patients
with colorectal cancer. J Clin Oncol. 2008;26(18):
2984-2991. doi:10.1200/JCO.2007.15.1027
6. Ng K, Wolpin BM, Meyerhardt JA, et al.
Prospective study of predictors of vitamin D status
and survival in patients with colorectal cancer. Br J
Cancer. 2009;101(6):916-923. doi:10.1038/sj.bjc.
6605262
7. Mezawa H, Sugiura T, Watanabe M, et al. Serum
vitamin D levels and survival of patients with
colorectal cancer: post-hoc analysis of a
prospective cohort study. BMC Cancer. 2010;10(1):
347. doi:10.1186/1471-2407-10-347
8. Wactawski-Wende J, Kotchen JM, Anderson GL,
et al; Women’s Health Initiative Investigators.
Calcium plus vitamin D supplementation and the
risk of colorectal cancer. N Engl J Med. 2006;354
(7):684-696. doi:10.1056/NEJMoa055222
9. Lappe JM, Travers-Gustafson D, Davies KM,
Recker RR, Heaney RP. Vitamin D and calcium
supplementation reduces cancer risk: results of a
randomized trial. Am J Clin Nutr. 2007;85(6):1586-
1591. doi:10.1093/ajcn/85.6.1586
10. Heist RS, Zhou W, Wang Z, et al. Circulating
25-hydroxyvitamin D, VDR polymorphisms, and
survival in advanced non-small-cell lung cancer.
J Clin Oncol. 2008;26(34):5596-5602. doi:10.
1200/JCO.2008.18.0406
11. Tamez S, Norizoe C, Ochiai K, et al. Vitamin D
receptor polymorphisms and prognosis of patients
with epithelial ovarian cancer. Br J Cancer. 2009;101
(12):1957-1960. doi:10.1038/sj.bjc.6605414
12. Hama T, Norizoe C, Suga H, et al. Prognostic
significance of vitamin D receptor polymorphisms
in head and neck squamous cell carcinoma. PLoS One.
2011;6(12):e29634. doi:10.1371/journal.pone.
0029634
13. Janssens W, Bouillon R, Claes B, et al. Vitamin D
deficiency is highly prevalent in COPD and
correlates with variants in the vitamin D-binding
gene. Thorax. 2010;65(3):215-220. doi:10.1136/thx.
2009.120659
14. Sinotte M, Diorio C, Bérubé S, Pollak M,
Brisson J. Genetic polymorphisms of the vitamin D
binding protein and plasma concentrations of
25-hydroxyvitamin D in premenopausal women.
Am J Clin Nutr. 2009;89(2):634-640. doi:10.3945/
ajcn.2008.26445
15. Japanese Gastric Cancer Association. Japanese
gastric cancer treatment guidelines 2010 (ver 3).
Gastric Cancer. 2011;14(2):113-123. doi:10.1007/
s10120-011-0042-4
16. Watanabe T, Itabashi M, Shimada Y, et al;
Japanese Society for Cancer of the Colon and
Rectum. Japanese Society for Cancer of the Colon
and Rectum (JSCCR) guidelines 2010 for the
treatment of colorectal cancer. Int J Clin Oncol.
2012;17(1):1-29. doi:10.1007/s10147-011-0315-2
17. Hollis BW, Kamerud JQ, Selvaag SR, Lorenz JD,
Napoli JL. Determination of vitamin D status by
radioimmunoassay with an 125I-labeled tracer. Clin
Chem. 1993;39(3):529-533.
18. Uitterlinden AG, Fang Y, Van Meurs JB, Pols HA,
Van Leeuwen JP. Genetics and biology of vitamin D
receptor polymorphisms. Gene. 2004;338(2):143-
156. doi:10.1016/j.gene.2004.05.014
19. Suzuki M, Yoshioka M, Hashimoto M, et al.
25-hydroxyvitamin D, vitamin D receptor gene
polymorphisms, and severity of Parkinson’s disease.
Mov Disord. 2012;27(2):264-271. doi:10.1002/mds.
24016
20. Schulz KF, Grimes DA. Multiplicity in
randomised trials II: subgroup and interim analyses.
Lancet. 2005;365(9471):1657-1661. doi:10.1016/
S0140-6736(05)66516-6
21. Hess KR. Graphical methods for assessing
violations of the proportional hazards assumption
in Cox regression. Stat Med. 1995;14(15):1707-1723.
doi:10.1002/sim.4780141510
22. Fine JP, Gray RJ. A proportional hazards model
for the subdistribution of a competing risk. J Am
Stat Assoc. 1999;94(446):496-509. doi:10.1080/
01621459.1999.10474144
23. Akiba T, Morikawa T, Odaka M, et al. Vitamin D
supplementation and survival of patients with
non-small cell lung cancer: a randomized,
double-blind, placebo-controlled trial. Clin Cancer
Res. 2018;24(17):4089-4097. doi:10.1158/1078-
0432.CCR-18-0483
24. Vaughan-Shaw PG, O’Sullivan F, Farrington SM,
et al. The impact of vitamin D pathway genetic
variation and circulating 25-hydroxyvitamin D on
cancer outcome: systematic review and
meta-analysis. Br J Cancer. 2017;116(8):1092-1110.
doi:10.1038/bjc.2017.44
25. Schöttker B, Jorde R, Peasey A, et al;
Consortium on Health and Ageing: Network of
Cohorts in Europe and the United States. Vitamin D
and mortality: meta-analysis of individual
participant data from a large consortium of cohort
studies from Europe and the United States. BMJ.
2014;348:g3656. doi:10.1136/bmj.g3656
26. Van Blarigan EL, Fuchs CS, Niedzwiecki D, et al.
Association of survival with adherence to the
American Cancer Society nutrition and physical
activity guidelines for cancer survivors after colon
cancer diagnosis: the CALGB 89803/Alliance Trial.
JAMA Oncol. 2018;4(6):783-790. doi:10.1001/
jamaoncol.2018.0126
27. Skender S, Böhm J, Schrotz-King P, et al. Plasma
25-hydroxyvitamin D3 levels in colorectal cancer
patients and associations with physical activity.
Nutr Cancer. 2017;69(2):229-237. doi:10.1080/
01635581.2017.1265131
28. Morales-Oyarvide V, Meyerhardt JA, Ng K.
Vitamin D and physical activity in patients with
colorectal cancer: epidemiological evidence and
therapeutic implications. Cancer J. 2016;22(3):223-
231. doi:10.1097/PPO.0000000000000197
29. Manson JE, Cook NR, Lee I-M, et al; VITAL
Research Group. Vitamin D supplements and
prevention of cancer and cardiovascular disease.
N Engl J Med. 2019;380(1):33-44. doi:10.1056/
NEJMoa1809944
30. Keum N, Giovannucci E. Vitamin D
supplements and cancer incidence and mortality:
a meta-analysis. Br J Cancer. 2014;111(5):976-980.
doi:10.1038/bjc.2014.294
31. Avenell A, MacLennan GS, Jenkinson DJ, et al;
RECORD Trial Group. Long-term follow-up for
mortality and cancer in a randomized
placebo-controlled trial of vitamin D(3) and/or
calcium (RECORD trial). J Clin Endocrinol Metab.
2012;97(2):614-622. doi:10.1210/jc.2011-1309
32. Trivedi DP, Doll R, Khaw KT. Effect of four
monthly oral vitamin D3 (cholecalciferol)
supplementation on fractures and mortality in men
and women living in the community: randomised
double blind controlled trial. BMJ. 2003;326(7387):
469. doi:10.1136/bmj.326.7387.469
Effect of Vitamin D Supplementation on Relapse-Free Survival in Patients With Digestive Tract Cancers
Original Investigation Research
jama.com
(Reprinted)
JAMA
April 9, 2019
Volume 321, Number 14
1369
© 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/30/2026

```
