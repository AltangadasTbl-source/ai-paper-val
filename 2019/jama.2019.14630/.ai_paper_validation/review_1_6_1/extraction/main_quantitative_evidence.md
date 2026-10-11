# Main-paper quantitative evidence: Workflow 1.6.1

Status: COMPLETE. Scope: DOC-001, all 14 PDF pages of `jama_saynorea_2019_oi_190106_1635377898.43062.pdf`, document role REPORT. All 14 units are reusable-backed; fresh-required units 0; mapped units 14. Scientific mapping was reconstructed afresh. No earlier narrative extraction, finding, candidate, screening, adjudication, or report was used. This artifact records evidence and relationships, without diagnoses or candidate judgments.

Relationship keys M001–M052 are local numeric/context keys; MS001–MS075, MS076a–MS076k, and MS077–MS079 are local statistical/display keys. They are provisional evidence keys for the coordinator/checkers to merge into their canonical N/S inventories, not candidate IDs. One row can contain the two randomized arms of the same matched relationship. Repeated narrative occurrences are explicitly cross-referenced. All source links below are relative to this extraction directory.

## Source coverage and provenance

Canonical native layout reused: `.ai_paper_validation/document_outputs/DOC-001/main_layout.txt`, 140131 bytes, all 14 pages; curator recorded byte-identical agreement with direct Poppler pdftotext 26.01.0 -layout output. Per-page native layout `.ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/page-001.txt` through `page-011.txt` also reused. Retained page images of PDF pp. 4, 5, 7, and 10 were visually inspected where needed; their original rendering executable/version is undocumented. Existing OCR was not required for any ambiguous value. No new OCR, Python scientific extraction, GPU, or web access was used.

New derivatives, direct CPU engine Poppler pdftoppm 26.01.0:

| Source unit | Relative derivative path from run root | Command |
|---|---|---|
| DOC-001 p. 6 | preprocessing/main-figure2-p006.png | pdftoppm -f 6 -l 6 -singlefile -scale-to 2200 -png source.pdf output-prefix |
| DOC-001 p. 9 | preprocessing/main-figure3-p009.png | pdftoppm -f 9 -l 9 -singlefile -scale-to 2200 -png source.pdf output-prefix |

Both new figure renders were visually inspected in full. Existing `.ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/doc001-p007.png` and `doc001-p010.png` were visually inspected for Table 3 and Figure 4. Source and reused assets were preserved.

| PDF page | Printed page | Exact source | Mapped evidence unit | Status |
|---:|---:|---|---|---|
| 1 | 1486 | [PDF p. 1](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=1) | Abstract: eligibility, randomization, intervention, analysis/completion claim, primary scores and contrast | COMPLETE |
| 2 | 1487 | [PDF p. 2](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=2) | Key Points; trial/design, eligibility, stratification, cluster allocation, intervention dose/contact | COMPLETE |
| 3 | 1488 | [PDF p. 3](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=3) | Figure 1 entire flow; allocation gifts; questionnaires; measurement schedule; primary endpoint | COMPLETE |
| 4 | 1489 | [PDF p. 4](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4) | Table 1 all cells; endpoints/thresholds; complete analysis methods; population and imputation narrative | COMPLETE |
| 5 | 1490 | [PDF p. 5](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=5) | Table 2 all score, change, SD, CI, P, imputation and scale footnotes; primary narrative begins | COMPLETE |
| 6 | 1491 | [PDF p. 6](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=6) | Figure 2 four complete score distributions and caption; primary relative increase; PDQS/food narrative | COMPLETE |
| 7 | 1492 | [PDF p. 7](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=7) | Table 3 first 11 variables, all baseline/change/CI/P rows | COMPLETE |
| 8 | 1493 | [PDF p. 8](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=8) | Table 3 cholesterol/sodium and footnotes; food/nutrient/risk-factor narrative and contact contrast | COMPLETE |
| 9 | 1494 | [PDF p. 9](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=9) | Figure 3 all 22 risk-factor/time panels with two arms, axes and box-plot definition; primary discussion | COMPLETE |
| 10 | 1495 | [PDF p. 10](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=10) | Figure 4 all 11 risk-factor distributions, meaningful-change percentages, CIs, P and thresholds | COMPLETE |
| 11 | 1496 | [PDF p. 11](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=11) | Discussion, contacts, interim conclusion and limitation context; supplied correction note with endpoint times | COMPLETE |
| 12 | 1497 | [PDF p. 12](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=12) | Context only: supervision, disclosures, funding and group collaborators; no applicable trial quantitative relationship | COMPLETE; NO_APPLICABLE |
| 13 | 1498 | [PDF p. 13](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=13) | Context only: collaborators, data-sharing pointer, acknowledgments and references 1–6; no applicable trial quantitative relationship | COMPLETE; NO_APPLICABLE |
| 14 | 1499 | [PDF p. 14](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=14) | Context only: references 7–34; bibliographic/background study numbers are not reported trial results | COMPLETE; NO_APPLICABLE |

## Population, flow, intervention and endpoint definitions

I = intervention: energy-reduced Mediterranean diet, physical activity promotion and behavioral support. C = control: Mediterranean diet without energy restriction. All subsequent table contrasts are I minus C unless the original label specifies otherwise. BMI means kg/m²; food consumption is g/week; kcal/day is energy intake. Reported CIs are 95% unless explicitly described as IQR. A displayed SD is not a standard error.

| Key | Location | Complete numeric/context relationship |
|---|---|---|
| M001 | p. 1 abstract design/interventions; p. 2 Methods | 6874 enrolled/randomized; 23 Spanish research centers; enrollment September 2013–December 2016; final collection March 2019. Abstract age 55–75 y. Methods: men 55–75 y, women 60–75 y; no baseline cardiovascular disease, initial BMI 27–40, at least 3 metabolic syndrome criteria. |
| M002 | p. 2 Methods; p. 3 Figure 1 | Allocation 1:1, I 3406/C 3468; stratified center/sex/age (<65, 65–70, >70 y), blocks of 6. Couples sharing household randomized as clusters with couple as allocation unit. |
| M003 | p. 3 Figure 1 top | Assessed 9677; excluded 2803 for not meeting inclusion criteria; randomized 6874. |
| M004 | p. 3 Figure 1 I branch | Randomized I 3406; excluded 134: 106 baseline energy outside limits and 28 incomplete baseline food-frequency questionnaire; main analysis I 3272. |
| M005 | p. 3 Figure 1 C branch | Randomized C 3468; excluded 157: 132 baseline energy outside limits and 25 incomplete baseline food-frequency questionnaire; main analysis C 3311. |
| M006 | p. 3 Figure 1 main analysis | I 2892 individually randomized + 380 randomized by couples; C 2909 individually randomized + 402 randomized by couples. These are participant counts, not reported numbers of couples. |
| M007 | p. 3 Figure 1 six-month branches | I unavailable nutritional information 410; I completer sensitivity n=2862. C unavailable 428; C sensitivity n=2883. |
| M008 | p. 3 Figure 1 twelve-month branches | I unavailable nutritional information 439; I completer sensitivity n=2833. C unavailable 368; C sensitivity n=2943. |
| M009 | p. 4 Results | Recruited/randomized 6874; baseline questionnaire exclusions total 53 (I28/C25); energy exclusions total 238 (I106/C132); analyzed 6583, men 3406, women 3177, I3272/C3311. Imputed nutritional values 12.7% at 6 mo and 12.2% at 12 mo. |
| M010 | p. 1 abstract Results | Wording reports among 6874 randomized, mean(SD) age 65.0(4.9) y, 3406 [52%] men; 6583 [96%] completed 12-mo follow-up and included in main analysis. Retain this exact population/completion wording independently of M009. |
| M011 | pp. 1–3 intervention | Both arms free extra-virgin olive oil 1 L/mo and nuts 125 g/mo (abstract); p. 3 specifically almonds 125 g/mo, recommended total mixed nuts 500 g/mo. I estimated energy reduction approximately 30% or 600 kcal/d. I group session + individual interview + telephone call monthly first year; C 2 educational sessions/year and individual visit/call/group session every 6 mo. |
| M012 | pp. 8, 11 discussion | Six-month contacts 18 I versus 3 C, interaction 6-fold higher I; p. 11 first-year contacts 36. Pilot results previously reported for 626 participants (pp. 2, 8). |
| M013 | pp. 3–4 assessment | 143-item semi-quantitative food-frequency questionnaire baseline, 6 and 12 mo, recalling preceding 6 mo; 4 dietary scores. Weight/waist/height twice per visit, blood pressure 3 times; fasting lipids baseline/6/12 mo. |
| M014 | pp. 1–6 endpoint scales | Primary interim endpoint baseline-to-12-mo er-MedDiet 17-item score, range 0–17, higher better, clinically important difference 1 point. MDS 0–9 (1-point threshold); MEDAS 14 items, range 0–14 (1-point threshold); PDQS 0–42 (likely 2-point threshold). Secondary score directions higher=better. |
| M015 | p. 4 Outcomes | Other outcomes: nutrients (energy, percentage energy from macronutrients/alcohol, fiber, long-chain Ω-3, dietary cholesterol, sodium), listed foods (olive oils, nuts, fruit, vegetables, cereals, legumes, fish, red/processed meat, pastries, yogurt/fermented dairy, low/whole-fat dairy, red wine), and body weight/waist/BMI/total/HDL/LDL/non-HDL cholesterol/total:HDL ratio/triglycerides/systolic/diastolic pressure. Any favorable dietary change means any change in desirable direction. |
| M016 | p. 4 Outcomes; p. 10 Figure 4 | Methods clinically meaningful: reduction at least 5% for BMI/weight/waist/total cholesterol/LDL/non-HDL/total:HDL ratio; HDL increase at least 5%; triglyceride reduction 10%; systolic reduction at least 5 mm Hg and diastolic at least 2.5 mm Hg. Figure 4 literal thresholds are preserved separately below. |
| M017 | p. 11 supplied Correction paragraph | November 1, 2021 correction note concerns eTable 1 in Supplement 2 and bone density/body composition measured by DXA at 1- and 3-year follow-up. This is supplied amendment context, not a new result. |

## Table 1: every baseline cell

Source: p. 4 Table 1, baseline characteristics of participants included in the main analyses. Default denominators I3272/C3311; education has explicit I3240/C3285. No baseline P value is printed. Counts are No.(%) and continuous values mean(SD) unless marked median(IQR).

| Key | Characteristic / unit | I | C |
|---|---|---|---|
| M018 | Men, No.(%) | 1702(52) | 1704(51) |
| M019 | Women, No.(%) | 1570(48) | 1607(49) |
| M020 | Age, y | 65.0(4.9) | 65.0(4.9) |
| M021 | Current smoker, No.(%) | 436(13) | 379(11) |
| M022 | Former smoker, No.(%) | 1366(42) | 1486(45) |
| M023 | Education denominators | 3240 | 3285 |
| M024 | Primary education or less, No.(%) | 1540(48) | 1647(50) |
| M025 | Secondary education, No.(%) | 997(31) | 902(28) |
| M026 | University education, No.(%) | 703(21) | 736(22) |
| M027 | Weight, kg | 86.7(13.0) | 86.4(13.0) |
| M028 | BMI, kg/m² | 32.5(3.4) | 32.5(3.5) |
| M029 | Waist circumference, cm | 108(9.6) | 108(9.7) |
| M030 | Physical activity, median(IQR), MET min/week | 1709(839–3202) | 1902(867–3371) |

Footnote: BMI calculated weight in kg / height in m squared; IQR interquartile range; MET metabolic equivalent. Table does not print a never-smoker row; no unreported category count has been supplied here.

## Statistical methods and result attribution

| Key | Location | Full analysis definition |
|---|---|---|
| MS001 | p. 4 Statistical Analysis | Sample size calculation done for overall-trial primary composite nonfatal myocardial infarction/nonfatal stroke/cardiovascular death; no numerical power/sample-size inputs for this interim dietary endpoint printed. Database dated March 12, 2019. |
| MS002 | p. 4 Statistical Analysis | Principal analyses include all randomized with baseline nutritional data regardless incomplete follow-up, multiple imputation of follow-up only. Excluded incomplete baseline food-frequency questionnaire and energy outside women 500–3500 kcal/d or men 800–4000 kcal/d. |
| MS003 | p. 4 Statistical Analysis | Iterative Markov chain Monte Carlo, Stata mi, 8 imputations for each missing measurement; predictors sex, age, smoking, education, BMI, physical activity, study arm, energy intake and baseline value of imputed variable. |
| MS004 | p. 4 Statistical Analysis; pp. 5, 8 table footnotes | Mixed-effects linear models changes baseline to 6/12 mo in all randomized participants and completer-only analyses. Three-level mixed linear model with random intercepts site, participant, cluster family; table footnotes specify site and intracluster correlations (couples) as random factors. |
| MS005 | p. 4 Statistical Analysis | All secondary analyses exploratory; no additional type I error adjustment. Two-sided tests; P<.05 deemed statistically significant; Stata 15.0. No test statistics or standard errors are printed in the main article. |
| MS006 | p. 4 Statistical Analysis | Post hoc sensitivity 1 completers at 6/12 mo, eTables 3–5; sensitivity 2 replace all missing with baseline values, eTables 6–8. Secondary analyses described as complete information at each follow-up visit. |
| MS007 | p. 5 Table 2 a | er-MedDiet imputed values 463 at 6 mo, 517 at 12 mo. MDS/MEDAS/PDQS 838 at 6 mo, 807 at 12 mo. Header multiple imputation/all randomized included participants, I3272/C3311. |
| MS008 | p. 8 Table 3 a,b | All energy intake variables 838 imputed at 6 mo, 807 at 12 mo. Multiple-imputation table I3272/C3311; mixed-effect models site and couples random factors. |
| MS009 | p. 5 Table 2 d | MDS threshold rationale from previous observational fully adjusted model: 2 points about 1 SD associated 25% mortality relative reduction; coefficient log(0.75)=−0.2877; 1 point about 0.5 SD corresponds 13% reduction, HR exp(−0.2877/2)=0.87. These are rationale quantities, not trial effect estimates. |
| MS010 | p. 5 Table 2 e | MEDAS threshold rationale, prior observational PREDIMED assessment with confounder control: 1 point, 10% composite cardiovascular reduction, multivariable HR0.90(0.85–0.96); 6% mortality reduction, HR0.94(0.89–0.99); unpublished investigator data 2019. Not current randomized results. |

## Table 2: baseline scores and every follow-up/change contrast

Source p. 5 Table 2. Baseline and follow-up score values are mean(SD); change values also displayed with SD. Between-group columns are mixed-effect differences of changes (95% CI), with I–C direction and P. Score row has no CI or P; change row contains inferential comparison. Refer to M014 for all ranges and MS007 for imputations.

| Key | Score baseline mean(SD), I / C |
|---|---|
| M031 | er-MedDiet 8.5(2.6) / 8.6(2.7) |
| M032 | MDS 4.3(1.7) / 4.3(1.6) |
| M033 | MEDAS 7.6(1.9) / 7.6(1.9) |
| M034 | PDQS 21.1(3.7) / 21.1(3.7) |

| Key | Score | Time | I score(SD) | C score(SD) | I change(SD) | C change(SD) | I–C difference(95% CI) | P |
|---|---|---|---|---|---|---|---|---|
| MS011 | er-MedDiet | 6 mo | 12.9(2.8) | 10.8(2.8) | 4.4(3.4) | 2.2(3.5) | 2.2(2.0–2.3) | <.001 |
| MS012 | er-MedDiet | 12 mo | 13.2(2.7) | 11.1(2.8) | 4.7(3.5) | 2.5(3.4) | 2.2(2.1–2.4) | <.001 |
| MS013 | MDS | 6 mo | 5.0(1.6) | 4.6(1.6) | 0.7(2.4) | 0.3(2.5) | 0.4(0.3–0.5) | <.001 |
| MS014 | MDS | 12 mo | 5.1(1.6) | 4.5(1.6) | 0.8(2.5) | 0.2(2.4) | 0.6(0.5–0.7) | <.001 |
| MS015 | MEDAS | 6 mo | 10.6(1.8) | 9.6(1.9) | 3.0(2.4) | 2.0(2.5) | 1.0(0.9–1.1) | <.001 |
| MS016 | MEDAS | 12 mo | 10.8(1.7) | 9.7(1.9) | 3.2(2.4) | 2.1(2.5) | 1.1(1.0–1.2) | <.001 |
| MS017 | PDQS | 6 mo | 27.8(3.6) | 25.8(3.7) | 6.7(6.8) | 4.7(7.4) | 2.0(1.6–2.3) | <.001 |
| MS018 | PDQS | 12 mo | 28.0(3.5) | 25.5(3.6) | 6.9(7.0) | 4.4(7.0) | 2.4(2.1–2.8) | <.001 |

## Table 3: every energy/nutrient baseline and change row

Table title baseline energy/nutrient intake and their changes by randomized treatment. Main header multiple imputation/all randomized participants I3272/C3311. Protein/carbohydrate/fat/fatty-acid/alcohol headings literally use `%/d`; narrative describes these as percentages of energy intake. Mean(SD) for all baselines except alcohol, long-chain Ω-3 and sodium median(IQR). Every change uses mean(SD), including those three. Units preserved; no conversion between daily and weekly displayed units performed.

| Key | Page | Variable / unit | Baseline I | Baseline C |
|---|---:|---|---|---|
| M035 | 7 | Total energy, kcal/d | 2355(555) | 2369(555) |
| M036 | 7 | Total protein, %/d | 16.8(2.8) | 16.8(2.8) |
| M037 | 7 | Total carbohydrate, %/d | 40.7(6.8) | 40.4(6.9) |
| M038 | 7 | Total fat, %/d | 39.5(6.6) | 39.7(6.5) |
| M039 | 7 | SFA, %/d | 9.9(2.0) | 10.0(2.0) |
| M040 | 7 | MUFA, %/d | 20.5(4.7) | 20.6(4.6) |
| M041 | 7 | MUFA:SFA ratio | 2.1(0.5) | 2.1(0.5) |
| M042 | 7 | PUFA, %/d | 6.4(1.9) | 6.4(1.8) |
| M043 | 7 | Total alcohol, %/d, median(IQR) | 1.0(0–4) | 2.0(0–4) |
| M044 | 7 | Fiber, g/wk | 184(62.7) | 182(59.9) |
| M045 | 7 | Long-chain Ω-3, g/wk, median(IQR) | 5(4–9) | 5(4–9) |
| M046 | 8 | Cholesterol, mg/wk | 2651(793) | 2687(825) |
| M047 | 8 | Sodium, g/wk, median(IQR) | 22(18–27) | 22(18–27) |

| Key | Page | Variable | Time | I change(SD) | C change(SD) | I–C difference(95% CI) | P |
|---|---:|---|---|---|---|---|---|
| MS019 | 7 | Energy | 6 mo | −173(537) | −76(501) | −97(−122 to −72) | <.001 |
| MS020 | 7 | Energy | 12 mo | −176(543) | −74(501) | −102(−129 to −75) | <.001 |
| MS021 | 7 | Protein | 6 mo | 1.2(2.9) | 0.2(2.7) | 1.0(0.9–1.2) | <.001 |
| MS022 | 7 | Protein | 12 mo | 1.1(3.0) | 0(2.7) | 1.1(1.0–1.3) | <.001 |
| MS023 | 7 | Carbohydrate | 6 mo | −3.4(7.0) | −1.9(6.8) | −1.5(−1.8 to −1.1) | <.001 |
| MS024 | 7 | Carbohydrate | 12 mo | −3.7(6.9) | −2.3(6.8) | −1.4(−1.8 to −1.0) | <.001 |
| MS025 | 7 | Total fat | 6 mo | 2.5(7.1) | 1.9(6.9) | 0.6(0.3–1.0) | <.001 |
| MS026 | 7 | Total fat | 12 mo | 2.9(7.1) | 2.4(6.9) | 0.5(0.1–0.9) | .007 |
| MS027 | 7 | SFA | 6 mo | −1.0(2.0) | −0.6(2.0) | −0.5(−0.6 to −0.4) | <.001 |
| MS028 | 7 | SFA | 12 mo | −0.9(2.0) | −0.6(1.9) | −0.4(−0.5 to −0.3) | <.001 |
| MS029 | 7 | MUFA | 6 mo | 3.5(5.6) | 2.4(5.3) | 1.1(0.9–1.4) | <.001 |
| MS030 | 7 | MUFA | 12 mo | 3.9(5.6) | 3.0(5.3) | 0.9(0.6–1.2) | <.001 |
| MS031 | 7 | MUFA:SFA ratio | 6 mo | 0.6(0.7) | 0.4(0.6) | 0.3(0.2–0.3) | <.001 |
| MS032 | 7 | MUFA:SFA ratio | 12 mo | 0.7(0.7) | 0.5(0.7) | 0.2(0.2–0.2) | <.001 |
| MS033 | 7 | PUFA | 6 mo | 1.3(2.3) | 0.8(2.1) | 0.5(0.4–0.6) | <.001 |
| MS034 | 7 | PUFA | 12 mo | 1.3(2.2) | 0.8(2.1) | 0.4(0.3–0.5) | <.001 |
| MS035 | 7 | Alcohol | 6 mo | −0.3(3.0) | −0.1(3.0) | −0.2(−0.4 to 0) | .01 |
| MS036 | 7 | Alcohol | 12 mo | −0.3(3.0) | −0.1(3.0) | −0.2(−0.4 to 0.1) | .01 |
| MS037 | 7 | Fiber | 6 mo | 40(70.8) | 16(60.6) | 23(20–27) | <.001 |
| MS038 | 7 | Fiber | 12 mo | 37(68.5) | 18(62.8) | 19(16–23) | <.001 |
| MS039 | 7 | Long-chain Ω-3 | 6 mo | 1.1(3.9) | 0.5(3.6) | 0.6(0.4–0.8) | <.001 |
| MS040 | 7 | Long-chain Ω-3 | 12 mo | 1.1(4.1) | 0.4(3.6) | 0.7(0.5–0.9) | <.001 |
| MS041 | 8 | Cholesterol | 6 mo | −224(779) | −169(780) | −54(−94 to −14) | .008 |
| MS042 | 8 | Cholesterol | 12 mo | −216(823) | −209(784) | −7(−49 to 35) | .74 |
| MS043 | 8 | Sodium | 6 mo | −3.0(6.8) | −1.8(6.5) | −1.2(−1.6 to −0.9) | <.001 |
| MS044 | 8 | Sodium | 12 mo | −3.2(7.1) | −1.9(6.9) | −1.3(−1.6 to −0.9) | <.001 |

Table 3 abbreviations: SFA saturated, MUFA monounsaturated, PUFA polyunsaturated fatty acids. Footnotes recorded in MS008 apply to every row, including p. 7 continuation.

## Matching narrative occurrences and additional intervals

All below belong to REPORT DOC-001. Each sentence retains its group/time attribution. Differences are changes from baseline unless described otherwise. Narrative comparisons to supplemental eTables/eFigures are pointers for the support map, not a claim that those supplemental cells were read by this mapper.

| Key | Exact location | Complete result and matching table/figure occurrence |
|---|---|---|
| MS045 | p. 1 abstract; p. 5 Primary Outcome continuing p. 6 | er-MedDiet baseline I8.5(2.6), C8.6(2.7); 12-mo I13.2(2.7), C11.1(2.8). Within I increase4.7(95%CI4.6–4.8), within C2.5(2.3–2.6); I–C2.2(2.1–2.4), P<.001. Matching means/change contrast MS012; eFigure1 pointer p.6. |
| MS046 | p. 2 Key Points; pp. 9–10 discussion | In 6874-participant ongoing trial, 17-item er-MedDiet changes 4.7 vs2.5 points, range0–17, clinically important1 point; significant greater I adherence at12mo. Discussion repeats change in17-item score primary endpoint and significantly greater I increase. |
| MS047 | p. 6 Primary Outcome | Intervention er-MedDiet improvement 55% relative increase(95%CI55%–56%), P<.001 over12mo; Figure2 distribution I shows greater improvement. |
| MS048 | p. 6 Other Dietary Scores | Baseline PDQS21.1(3.7) both;12-mo within C4.4(4.2–4.7), P<.001 and within I6.9(6.6–7.1), P<.001; between2.4(2.1–2.8), P<.001, matching MS018. Maintained in post hoc sensitivities; pointers eFigure1,eTable3,eTable6. |
| M048 | p. 6 Foods and Food Groups | Refined grains baseline779g/wk both; pastries baseline I121/C114g/wk; vegetables baseline I2168/C2130g/wk (sentence continues p.8). |
| MS049 | p. 6 Foods and Food Groups | Refined grains12mo I−535g/wk(−559 to−510), C−226(−249 to−203); between−309(−340 to−277), P<.001; eTable2 pointer. |
| MS050 | p. 6 Foods and Food Groups | Pastries12mo C−60g/wk(−67 to−53), P<.001; I−109(−116 to−102), P<.001; between−49(−59 to−39), P<.001. |
| MS051 | p. 6 Foods and Food Groups | Red meat12mo between−39g/wk(−51 to−28), P<.001. |
| MS052 | pp. 6–8 Foods and Food Groups continuation | Vegetables12mo within C137g/wk(100–175), I347(306–389); between210(157–263), P<.001. |
| MS053 | p. 8 Foods and Food Groups | Fruit12mo between197g/wk(118–276), P<.001. |
| M049 | p. 8 Foods and Food Groups | Nuts baseline60g/wk both. |
| MS054 | p. 8 Foods and Food Groups | Nuts12mo between35g/wk(27–43), P<.001; similar post hoc sensitivities eTables4/7; primary foods eTable2. |
| MS055 | p. 8 Energy Intake and Nutrients | Baseline energy C2369(555), I2355(555)kcal/d;12mo between−102kcal/d(−129 to−75), P<.001 (MS020); pointers Table3/eTables5/8. |
| MS056 | p. 8 Energy Intake and Nutrients | Both groups carbohydrate percentage decreased;12mo between−1.4%(−1.8 to−1.0), P<.001 (MS024). |
| MS057 | p. 8 Energy Intake and Nutrients | MUFA baseline C20.6%(4.6), I20.5%(4.7);12mo within C3.0%(2.8%–3.2%), P<.001; I3.9%(3.7%–4.1%), P<.001; between0.9%(0.6%–1.2%), P<.001 (MS030). |
| MS058 | p. 8 Energy Intake and Nutrients | Any favorable dietary-change proportion significantly greater I for most comparisons; pointer eFigure2. eFigure3 standardized energy/nutrient differences in baseline-SD units at6/12mo. No extra percentages or numeric standardized estimates printed here. |
| M050 | p. 8 Risk Factors | Baseline waist108cm both; systolic pressure C139/I140mmHg. |
| MS059 | p. 8 Risk Factors | Waist12mo between−3.3cm(−3.6 to−2.9), P<.001; systolic12mo between−1.9mmHg(−2.7 to−1.1), P<.001. Figures3/4 and eTable9 pointers. Narrative favorable changes body weight/waist/BMI/HDL/non-HDL/total:HDL/triglycerides/systolic/diastolic, with exceptions such as LDL. |
| MS060 | pp. 1, 8, 11 Conclusions/Discussion | Greater diet-adherence increase after12mo I vsC; further long-term cardiovascular evaluation needed. Preliminary/exploratory interim analysis; all secondary analyses exploratory. Dietary/nutrient/risk-factor improvements are reported; p.11 no meaningful between-group extra-virgin olive oil difference. No exact additional effect size printed. |

## Figure 2: all four distributions

Source p. 6. Complete direct visual derivative `preprocessing/main-figure2-p006.png`. Histogram x score ticks 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17; y No. of Patients ticks0,50,100,150,200,250,300,350,400,450. Dark I panels upper row; pale C lower row. Left baseline/right12mo. Histogram bins are single score values; bar heights carry no exact printed count labels, so precise bin counts cannot be reconstructed as printed numerical values. All bars and boxplot marks were visually inspected; no bins sampled or excluded. No model/denominator printed on this figure beyond arm/time.

Caption: middle line median er-MedDiet, boxes IQR, whiskers extreme observed values within1.5×IQR of nearer quartile; dots outside this range. These are distribution summaries, not CI limits.

| Key | Panel | Full graph relationship / visual locator |
|---|---|---|
| MS061 | Baseline energy-reduced/I | Central score distribution around8; box median visually at8, Q1 about7 and Q3 about10, whiskers about5.5–14.5; outer dots scores1–5 and15–16. Exact frequencies unlabeled. |
| MS062 | 12-month energy-reduced/I | Distribution shifted higher, peak about14; box median about13, Q1 about11 and Q3 about15, whiskers about9–17; outer dots scores3–8. Exact frequencies unlabeled. |
| MS063 | Baseline energy-unrestricted/C | Central score distribution around8; box median about8, Q1 about7 and Q3 about10, whiskers about5.5–14.5; outer dots scores1–5 and15–17. Exact frequencies unlabeled. |
| MS064 | 12-month energy-unrestricted/C | Distribution shifted higher with central scores10–12; box median about11, Q1 about9 and Q3 about13, whiskers about7–17; outer dots scores3–6. Exact frequencies unlabeled. |

Graphical readings above are approximate positions only, explicitly separated from printed Table2 means/SDs and narrative CIs. Whisker positions need not be integer ticks because graphics are offset around histogram categories. Source contains no numeric box summary table or bin labels.

## Figure 3: every risk-factor/time panel

Source p. 9. Direct visual derivative `preprocessing/main-figure3-p009.png`. Eleven outcomes in two time columns (6mo left,12mo right), each two horizontal box plots I upper/C lower. Every panel x ticks−3,−2,−1,0,1,2,3, scale baseline SD of that factor. All plotted marks were visually read. Caption median within-group observed change, box IQR, whiskers extremes within1.5×IQR of nearer quartile; common baseline-SD units for comparability. No exact numerical median/quartile/whisker labels, confidence intervals, P values, raw denominators or counts accompany the plots. The complete graph is preserved as visual evidence; approximate positions are not treated as precise extracted estimates.

| Key | Outcome | 6mo graphical direction, I / C | 12mo graphical direction, I / C |
|---|---|---|---|
| MS065 | Body weight | negative / near0-negative | negative / near0-negative |
| MS066 | Waist circumference | negative / near0-negative | negative / near0-negative |
| MS067 | Body mass index | negative / near0-negative | negative / near0-negative |
| MS068 | Serum cholesterol | near0-negative / near0 | near0-negative / near0-negative |
| MS069 | HDL cholesterol | positive / near0-positive | positive / positive |
| MS070 | LDL cholesterol | near0-negative / near0-negative | near0-negative / near0-negative |
| MS071 | Non-HDL cholesterol | negative / near0-negative | negative / negative |
| MS072 | Total cholesterol:HDL ratio | negative / near0-negative | negative / negative |
| MS073 | Triglycerides | negative / negative | negative / near0-negative |
| MS074 | Systolic blood pressure | negative / negative | negative / negative |
| MS075 | Diastolic blood pressure | negative / negative | negative / negative |

This table enumerates22 panels/44 group distributions. It does not equate median box-plot position with mixed-model mean change in the prose or results supplement.

## Figure 4: all percentages, intervals, tests and boxplot scales

Source p. 10 retained source-matched render `doc001-p010.png` visually inspected in full. Meaningful-change columns literal heading Patients With Clinically Meaningful Changes,%(95%CI), I/C rows. No event numerator or exact contributing denominator printed for these percentages. Each P is printed once beside paired group plots. Figure does not name the test for these proportion comparisons. Main Methods provide two-sided P<.05 general convention. Caption boxes/median/whiskers/dots represent observed distributions as Figure3, with raw change units. Axis labels literally append `(95% CI)`; this label is retained independently of caption's boxplot definition. No numerical median/quartile/whisker labels supplied. Every one of11 plot pairs inspected; no numerical reconstruction from pixels presented as a printed value.

| Local key | Outcome | Literal favorable-change threshold | I %(95%CI) | C %(95%CI) | P | Axis unit; full tick range and step |
|---|---|---|---|---|---|---|
| MS076a | Body weight | Reduction >5% | 40.6(38.7–42.5) | 12.2(11.0–13.5) | <.001 | kg;−15 to10, step5 |
| MS076b | Waist circumference | Reduction >5% | 39.5(37.6–41.3) | 13.5(12.2–14.8) | <.001 | cm;−20 to10, step5 |
| MS076c | BMI | Reduction >5% | 40.5(38.6–42.4) | 12.5(11.3–13.8) | <.001 | kg/m²;−10 to10, step5 |
| MS076d | Total cholesterol | Reduction >5% | 37.5(35.7–39.4) | 34.3(32.5–36.1) | .02 | mg/dL;−100 to100, step50 |
| MS076e | HDL cholesterol | Increase >5% | 45.6(43.7–47.6) | 40.0(38.1–41.8) | <.001 | mg/dL;−25 to25, step5 |
| MS076f | LDL cholesterol | Reduction >5% | 41.4(39.5–43.3) | 40.2(38.3–42.1) | .36 | mg/dL;−100 to100, step50 |
| MS076g | Non-HDL cholesterol | Reduction >5% | 43.6(41.7–45.5) | 37.5(35.7–39.4) | <.001 | mg/dL;−100 to100, step50 |
| MS076h | Total cholesterol/HDL ratio | Reduction >5% | 48.4(46.5–50.4) | 41.3(39.4–43.2) | <.001 | ratio;−3 to3, step1 |
| MS076i | Triglycerides | Reduction >10% | 47.3(45.4–49.2) | 38.2(36.3–40.0) | <.001 | mg/dL;−250 to200, step50 |
| MS076j | Systolic blood pressure | Reduction >5 mm Hg | 47.5(45.6–49.5) | 41.8(39.9–43.7) | <.001 | mm Hg;−50 to40, step10 |
| MS076k | Diastolic blood pressure | Reduction 2.5 mm Hg | 48.1(46.2–50.1) | 44.3(42.4–46.2) | .005 | mm Hg;−30 to20, step10 |

All axes include zero reference. Graphical medians I vsC: weight/waist/BMI are more negative I; total/LDL/non-HDL/ratio/triglycerides and pressures show negative changes both; HDL positive both. Exact graphical quantiles not numerically labeled. No displayed OR/RR/RD is associated with percentages in Figure4.

## Consolidated footnotes, follow-up context and absent quantity classes

| Key | Location | Context needed for correct extraction |
|---|---|---|
| M051 | pp. 4–10 | Trial analysis population main I3272/C3311. Table2 uses all randomized included participants with MI; Table3 all randomized participants with MI. Completer counts specifically belong to sensitivity analyses (M007–M008), not presumed figure denominators. Imputed score counts differ by score (MS007) from food-frequency nutritional counts (MS008). |
| M052 | pp. 11–14 | p.11 conclusion12mo interim trial; limitations self-report/recall/social desirability, food incentives/generalizability, unknown long-term outcome relation and multifaceted intervention. p.12–14 numerical funding IDs, citation years/volumes/pages, reference-title study counts and historical studies are contextual bibliographic/admin material, not current trial effect data. No applicable additional numerical trial relationship on these units. |
| MS077 | pp. 5–10 captions/footnotes | Scales, definitions, I–C contrasts and boxplot semantics above are integral to each relationship. CIs in Tables2–3 mixed-model differences; SD in group columns; IQR only where labeled. Figure3 baseline-SD standardized observed change distinct from Figure4 raw-unit distributions. |
| MS078 | pp. 4, 6, 8, 11 narrative | Completer and baseline-observation-carried-forward analyses are post hoc; eTables3–8 and eFigure1 cross-reference matching claims. Main article claims similar dietary/food/nutrient sensitivity results; exact supplementary values are assigned to support mapper. |
| MS079 | pp. 1–14 full inspection | No trial person-time, incidence rate, event-rate denominator, current-trial OR/RR/HR, standard error or test statistic printed. HRs on p.5 are previous observational rationale (MS009–MS010). No exact numeric bin frequencies or unlabeled boxplot quantiles are supplied. These are explicitly absent classes, not coverage gaps. |

## Handoff counts and limitations

Mapped pages14/14; reusable14; fresh-required0; context-only no-applicable pages12–14. Local numeric/context relationships52 (M001–M052). Local statistical/display relationships89: MS001–MS075 (75), MS076a–MS076k (11), MS077–MS079 (3). Family counts: methods/rationale10; score follow-up contrasts8; nutrient follow-up contrasts26; narrative/attribution relationships16; score-distribution panels4; standardized risk-factor families11 (22 time panels); meaningful-change proportion contrasts11; consolidated statistical context3. No scientific source-unit gaps.

Limitations: unlabelled histogram bin heights and boxplot quantiles are graphical only and do not provide exact numerical source counts/quantiles; entire displays inspected and preserved. Figure4 does not print its exact proportion denominators/test-specific method. These missing printed details are recorded without inferring them. Retained rendering engine versions unknown; new render engine recorded above. No value, model or source was silently normalized. Candidate diagnosis and inclusion judgments belong to the checker stages.
