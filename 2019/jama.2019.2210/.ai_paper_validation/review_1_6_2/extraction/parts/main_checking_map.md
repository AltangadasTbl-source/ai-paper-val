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

