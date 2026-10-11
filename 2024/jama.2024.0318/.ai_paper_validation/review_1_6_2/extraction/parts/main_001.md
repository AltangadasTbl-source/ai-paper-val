# Main Quantitative Evidence Map — Part 1

## Scope and provenance

Source DOC-001, role REPORT: `jama_courcoulas_2024_oi_240004_1721756962.76052.pdf`. Assigned main scope is physical PDF pages 1–11 (printed pages 654–664). This independent part owns physical pages 1–4 and 67 relationship records MAIN-001 through MAIN-067. Part 2 owns pages 5–11. Records reconstruct source evidence only; no findings or candidate judgments are assigned. Matching later occurrences are cross-references, not extra relationships in this part.

Read QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md completely; read current source inventory, source coverage, evidence asset inventory and tooling record. Canonical locators are the reusable combined layout `.ai_paper_validation/review_1_5_3/preprocessing/main/DOC-001_pp1-11_direct_layout.txt` and per-page `.ai_paper_validation/document_outputs/DOC-001/preprocessing/normalized_text/page-NNN.txt`. Curator byte comparison with direct Poppler 26.01.0 extraction establishes unchanged native/layout transcription. Reused Poppler rendered PNG pages 3 and 4 were visually inspected, including every flow box and table row. Exact retained page text is appended below for independent reconstruction. No new extraction, rendering or OCR was necessary; compute device CPU; historical derivative engine Poppler-compatible native/layout and Poppler 200-dpi PNG, exact historical version unspecified. No prior candidate/checker/report scientific input was read.

Notation: M = medical/lifestyle; B = bariatric surgery; R = Roux-en-Y gastric bypass; S = sleeve gastrectomy; A = adjustable gastric banding. All intervals are printed 95% confidence intervals unless explicitly described as SD, IQR or range. Percent signs retain source usage; no conversion between percentage-point and relative-percent quantities is imposed. Group descriptions and quantitative scale footnotes are recorded verbatim in the appropriate fields.

## Page coverage

| Physical page | Printed page | Complete content inspected | Mapping |
|---|---:|---|---|
| 1 | 654 | Abstract, including all quantitative results and conclusion | MAIN-001–MAIN-013 |
| 2 | 655 | Key Points, Methods, outcomes and start of statistical analysis | MAIN-014–MAIN-023 |
| 3 | 656 | Figure 1, all flow boxes/footnote; statistical continuation; results | MAIN-024–MAIN-039 |
| 4 | 657 | Entire Table 1 with five columns/denominators/footnotes; result continuation | MAIN-040–MAIN-067 |

## Abstract and matching-result map

All MAIN-001–013 are [DOC-001 p1 abstract](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1).

| Key | Exact quantitative relationship and context | Matching occurrence/key |
|---|---|---|
| MAIN-001 | Four US single-center randomized trials conducted May 2007–August 2013; observational follow-up through July 2022; original assignment M vs R/S/A, three surgical procedures. | p2 Study design; p3 Figure 1 |
| MAIN-002 | Primary outcome: HbA1c change from baseline to 7 years for all participants; data up to 12 years. | MAIN-015; Table 2 primary row |
| MAIN-003 | Enrolled 262 of 305 eligible (86%). | p3 narrative and Figure 1 |
| MAIN-004 | Pooled mean age 49.9 (SD 8.3) years; BMI 36.4 (3.5); 68.3% women; 31% Black; 67.2% White. | p3 narrative; Table 1 subgroup counts |
| MAIN-005 | During follow-up 25% originally randomized to M underwent bariatric surgery; median follow-up 11 years. | p7 crossover 24/96; p3 range 7–15 years |
| MAIN-006 | Year7 M HbA1c decreased by 0.2% (CI −0.5% to 0.2%), baseline 8.2%. Source phrase uses positive decrease magnitude and signed interval. | p3 narrative; Table 2 net change −0.2 |
| MAIN-007 | Year7 B HbA1c decreased by 1.6% (CI −1.8% to −1.3%), baseline 8.7%. | p3 narrative; Table 2 net change −1.6 |
| MAIN-008 | Year7 between-group HbA1c difference −1.4% (−1.8% to −1.0%), P<.001. | Key Points magnitude 1.4%; p3; Table 2 |
| MAIN-009 | Year12 between-group HbA1c difference −1.1% (−1.7% to −0.5%), P=.002. | Key Points magnitude 1.1%; p3; supplement eTable2 pointer |
| MAIN-010 | Year7 remission: M 6.2%, B 18.2%, P=.02. | p4 OR and Table 2; Figure 3 |
| MAIN-011 | Year12 remission: M 0.0%, B 12.7%, P<.001. | p4 significance; Figure 3; supplementary result match |
| MAIN-012 | Four deaths (2.2%), two in each group. No denominator is printed beside pooled 2.2%; preserve it for comparison with p7 narrative/Table 3. | p7 deaths; p8 Table 3 M2/96 B2/166 |
| MAIN-013 | Qualitative result/conclusion: fewer antidiabetes medications; no differences in major cardiovascular adverse events; anemia, fractures and gastrointestinal events more common after B; superior glycemic control, less medication and more remission after 7–12 years. | pp6–9 results/discussion; Table 2/3 |

## Report analysis specification and cross-plan matching keys

[DOC-001 p2 Methods/Key Points](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=2), continued [p3 statistical analysis](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3).

| Key | Printed specification | Population/time/quantity to match |
|---|---|---|
| MAIN-014 | Key Points calls HbA1c between-group difference 1.4% at 7y and 1.1% at 12y and describes superior glycemic control. | Magnitudes of MAIN-008/009; no CI or P printed here |
| MAIN-015 | Primary: between-group difference in percent change in HbA1c baseline to 7y; 12y for those reaching it before closure. Statistical paragraph calls percent change and ITT. | Endpoint scale and time; Table 2 footnote b specifies net change for HbA1c |
| MAIN-016 | Secondary: change over time in HbA1c; HbA1c<7.0%; remission defined HbA1c<6.5% without diabetes medications for at least 3 months, annually assessed. | Remission threshold/window; Figure 3 abbreviated definition |
| MAIN-017 | Other secondary: between-group changes in weight, BMI, lipids, BP, medication use, major adverse cardiovascular events and microvascular complications. Results by randomized group and procedure; all outcomes hypothesized better for B. | Outcome status and reported procedure contrasts |
| MAIN-018 | Original eligibility: type2 diabetes, BMI27–45, age18–65; original randomization/operation types differed by site; intensive M based on Diabetes Prevention Program/Look AHEAD. Postoperation eating/activity guidance at least monthly first year. | Analysis population and intervention; sites Cleveland STAMPEDE, Joslin/Brigham SLIMM-T2D, Pittsburgh TRIABETES, Washington/Kaiser CROSSROADS |
| MAIN-019 | ITT primary HbA1c baseline-to-7y comparison: linear mixed-effect model; fixed group, visit, group×visit, site, baseline HbA1c; participant random intercept. Least-square means per group/visit; appropriate linear contrast for group comparison. | Primary model/covariates, random effect, adjusted group contrast |
| MAIN-020 | Per-protocol sensitivity for M-to-surgery crossover: inverse probability weighting; current treatment modeled as depending on previous treatments and outcomes. | Time-varying exposure sensitivity; supplement eFigure2 |
| MAIN-021 | Missing clinical/laboratory values recovered from electronic records; death/loss to follow-up random censoring; resulting monotone missingness considered missing at random; Supplement2 for details. | Missingness handling and analysis input recovery |
| MAIN-022 | Binary outcomes including remission and medication percentages: GEE controlling site and baseline HbA1c; sandwich standard errors. Secondary outcomes not adjusted for multiple testing. | OR results and multiplicity; no test-sidedness specified in main article |
| MAIN-023 | BMI<35 exploratory analysis uses same model set as overall cohort. Software RStudio (R Foundation) and SAS9.4. Adverse-event annual visits/quarterly calls, self-report verified with records; serious events defined death, life-threatening event, hospitalization, significant disability/incapacity or urgent intervention; events reported through12y. | Exploratory status, safety window and ascertainment; no sample-size/power inputs in main |

Source p2 conversion: HbA1c mmol/mol = 10.93×HbA1c−23.50. Table1 and Table2 repeat conversion; their other conversion constants are listed with table footnotes below. Background epidemiology/cost numbers on p2 are transcribed in the exact text appendix but are not ARMMS result relationships.

## Participant flow and narrative outcomes, physical page3

[DOC-001 p3 Figure 1/results](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3).

| Key | Printed values/relationship | Context and matching occurrence |
|---|---|---|
| MAIN-024 | Original randomized355: STAMPEDE155, SLIMM88, TRIABETES69, CROSSROADS43. Withdrew preintervention39. Eligible316: STAMPEDE145, SLIMM78, TRIABETES61, CROSSROADS32. | All four original trials and both total/component series are explicit figure boxes |
| MAIN-025 | Figure next box: excluded14, withdrew/lost12, died2; next oval305 available for long-term follow-up and randomized. | Footnote: three originally lost successfully rerecruited; retain footnote with flow |
| MAIN-026 | Below305 oval: B193, M122; B components R106, S49, A38. | Distinct original-assignment labels; do not relabel as enrolled262 |
| MAIN-027 | Enrolled ARMMS: B166, M96; Table1 enrolled procedure components R89, S41, A36. | Enrolled total262; compare group sizes across main tables/figures |
| MAIN-028 | Narrative:355 randomized;39 withdrew preintervention, more than half dissatisfied with assignment;316 eligible; between original and pooled study9 withdrew consent and2 died;305 available,262(86%) enrolled. | Narrative flow kept separately from Figure1 excluded14/12 |
| MAIN-029 | Cohort summary: age49.9(8.3),68.3% women,31% Black,67.2% White;BMI36.4(3.5);96(36.6%) BMI<35;HbA1c8.5(1.5)%;follow-up median11(range7–15)y; later enrollees not all reached12y. | Table1 weighted descriptive counterparts; eTable1 pointer |
| MAIN-030 | Figure2A narrative: B absolute HbA1c significantly lower than M at all postbaseline times, P<.001, despite higher baseline. | Repeated-series contrast; graph contains no printed per-visit P values |
| MAIN-031 | M year7 HbA1c8.0%, baseline8.2%; text “difference,0.2%” with CI−0.5 to0.2. B8.7→7.2; text “difference,1.6%” CI−1.8 to−1.3. | MAIN-006/007; Table2 signed net changes and raw means |
| MAIN-032 | Year7 adjusted group−1.4(−1.8 to−1.0)%,P<.001;year12−1.1(−1.7 to−0.5)%,P=.002. | MAIN-008/009 |
| MAIN-033 | Procedure HbA1c changes at7y:R−1.7(−2.0 to−1.3)%;S−2.0(−2.6 to−1.5)%;A−0.8(−1.3 to−0.2)%. | Figure2B; all within-procedure estimates/intervals |
| MAIN-034 | R vs S improvements not significant; A less improved than S,P=.007, and R,P=.03. | Procedure-comparison P values, not within-procedure change tests |
| MAIN-035 | PP sensitivity year7:M0.1(−0.5 to0.7)%;B−1.4(−1.7 to−1.2)%;group−1.5(−2.1 to−0.9)%,P<.001. | Accounts for25% crossover; eFigure2A pointer |
| MAIN-036 | Year1 remission M0.5%,B50.8%; B declines but remains higher over time. | Figure3 and p8 rounded 51% |
| MAIN-037 | Year7 remission M6.2%,B18.2%;B/M OR3.4(1.3–9.2),P=.02;year12 P<.001. | p4 continuation; Table2 OR3.39(1.25–9.17) |
| MAIN-038 | Year7 procedure remission:R24.5%,S15.2%,A8.9%; procedure comparisons nonsignificant. | p4 continuation; no procedure OR/CI/P printed |
| MAIN-039 | Year7 HbA1c<7:M26.7%,B54.1%;OR3.2(1.8–5.9),P<.001. Text next sentence threshold HbA1c≤6.5,similar differences,P=.002. | p4 continuation; Table2 threshold row reads HbA1c<6.5 |

MAIN-037–039 are owned here because they continue the p3 primary results paragraph onto p4; exact source location is [p4 lower narrative](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=4), not p3.

## Table1 entire row map, physical page4

[DOC-001 p4 Table1](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=4). N262; column order M96 | B166 | R89 | S41 | A36. Default denominator is column n unless the cell explicitly states another n or fraction. Parentheses retain the source dispersion or percent label; no silent relabeling. Twenty-eight quantitative rows, each with all five cells:

| Key | Row and printed unit/summary label | M | B | R | S | A |
|---|---|---|---|---|---|---|
| MAIN-040 | Age,y; under Demographics,No.(%) heading | 51.4(6.8) | 49.0(9.0) | 49.1(9.0) | 48.3(7.7) | 49.6(10.3) |
| MAIN-041 | Women,No.(%) | 62(64.6) | 117(70.5) | 61(68.5) | 32(78.0) | 24(66.7) |
| MAIN-042 | Men,No.(%) | 34(35.4) | 49(29.5) | 28(31.5) | 9(22.0) | 12(33.3) |
| MAIN-043 | Black,No.(%) | 35(36.5) | 46(27.7) | 23(25.8) | 13(31.7) | 10(27.8) |
| MAIN-044 | White,No.(%) | 59(61.5) | 118(71.1) | 64(71.9) | 28(68.3) | 26(72.2) |
| MAIN-045 | Other race,No.(%) | 2(2.1) | 2(1.2) | 2(2.3) | 0 | 0 |
| MAIN-046 | Waist,cm,mean(SD) | 113.7(9.6),n95 | 115.0(9.9) | 116.1(9.9) | 113.3(10.2) | 114.5(9.7) |
| MAIN-047 | Weight,kg,mean(SD) | 105.6(15.5) | 103.5(15.3) | 105.2(15.3) | 100.2(16.7) | 103.1(13.0) |
| MAIN-048 | BMI,mean(SD) | 36.2(3.4) | 36.6(3.6) | 37.0(3.4) | 36.3(4.2) | 35.9(3.2) |
| MAIN-049 | BMI<35,No.(%) | 40(41.7) | 56(33.7) | 26(29.2) | 15(36.6) | 15(41.7) |
| MAIN-050 | Systolic BP,mmHg,mean(SD) | 129.7(15.8) | 134.4(17.7) | 135.0(18.4) | 135.8(19.9) | 131.6(12.7) |
| MAIN-051 | Diastolic BP,mmHg,mean(SD) | 79.5(9.6) | 80.4(10.0) | 80.7(9.8) | 81.9(12.2) | 78.2(7.2) |
| MAIN-052 | Diabetes duration,y,mean(SD) | 8.8(5.2) | 8.3(5.5) | 8.8(5.9) | 7.8(4.6) | 7.5(5.1) |
| MAIN-053 | HbA1c,%,mean(SD) | 8.2(1.2) | 8.7(1.7) | 8.7(1.6) | 9.4(1.6) | 8.2(1.8) |
| MAIN-054 | HbA1c<7.0%,No.(%) | 11(11.5) | 20(12.0) | 9(10.1) | 0 | 11(30.6) |
| MAIN-055 | Fasting glucose,mg/dL,mean(SD) | 156.5(50.0),n95 | 172.0(69.7) | 171.0(69.5) | 172.1(66.1) | 174.6(75.9) |
| MAIN-056 | Total cholesterol,mg/dL,mean(SD) | 172.6(38.5),n95 | 179.6(44.8) | 176.1(40.7) | 191.2(46.8) | 174.9(50.7) |
| MAIN-057 | HDL,mg/dL,mean(SD) | 44.3(13.2),n95 | 42.9(11.6) | 43.6(11.8) | 45.5(12.2) | 38.1(9.0) |
| MAIN-058 | LDL,mg/dL,mean(SD) | 96.3(33.2),n94 | 100.3(34.2),n159 | 96.3(31.8),n88 | 110.8(41.0) | 97.8(28.7),n30 |
| MAIN-059 | Triglycerides,mg/dL,printed mean(SD) label | 140.0(92.5–221.5),n95 | 145.0(103.0–231.8) | 143.0(100.0–239.0) | 160.0(120.0–214.0) | 142.5(94.0–251.5) |
| MAIN-060 | Serum creatinine,mg/dL,mean(SD) | 0.7(0.2),n95 | 0.7(0.2) | 0.7(0.2) | 0.7(0.2) | 0.8(0.2) |
| MAIN-061 | Urine albumin:creatinine ratio,printed mean(SD) label | 6.0(4.0–14.5),n74 | 9.0(4.0–22.5),n119 | 7.5(3.0–28.0),n62 | 9.0(7.0–22.0) | 6.0(3.8–12.2),n16 |
| MAIN-062 | Statins,No.(%) | 71(74.0) | 121(72.9) | 66(74.2) | 31(75.6) | 24(66.7) |
| MAIN-063 | ACEi/ARB,No.(%) | 65(67.7) | 108(65.1) | 63(70.8) | 25(61.0) | 20(55.6) |
| MAIN-064 | ACEi,No.(%) | 59(61.5) | 78(47.0) | 47(52.8) | 17(41.5) | 14(38.9) |
| MAIN-065 | Insulin,No.(%) | 36(37.5) | 82(49.4) | 46(51.7) | 17(41.5) | 19(52.8) |
| MAIN-066 | β-blockers,No.(%) | 16(16.7) | 30(18.2) | 15(16.9) | 6(14.6) | 9/35(25.7) |
| MAIN-067 | ARB,No.(%) | 8(8.3) | 30(18.1) | 16(18.0) | 8(19.5) | 6(16.7) |

Table1 footnote a: other includes two identifying as Asian and two reporting more than one race. Abbreviations: ACEi angiotensin-converting enzyme inhibitor; ARB angiotensin receptor blocker; BMI body mass index; BP blood pressure; HDL/LDL high-/low-density lipoprotein cholesterol. SI conversion factors: HbA1c×10.93−23.50; glucose×0.0555 to mmol/L; cholesterol×0.0259 to mmol/L; triglycerides×0.0113 to mmol/L; creatinine×88.4 to μmol/L. Five subgroup column totals allow sex/race/subprocedure sums; explicit cell denominators above must be retained for percentage arithmetic. Serum/waist/lipid missing-n cells and all zero cells are explicitly mapped.

Page4 lower medication paragraph is mapped in Part2 MAIN-093 because its quantitative claim continues through page6. It prints unchanged M use P=.19 at7y and0.12 at12y; B baseline162/166(97.6%) to year1 62/163(38.0%). No page4 quantitative relationship is omitted by that cross-reference.

## Exact reusable layout transcription appendix (physical pages1–4)

The following four blocks retain all printed numeric text, captions, source headings and footnotes. They are locator evidence, not final source authority.

### Physical PDF page 001

```text
                Research


              JAMA | Original Investigation

              Long-Term Outcomes of Medical Management vs Bariatric Surgery
              in Type 2 Diabetes
              Anita P. Courcoulas, MD; Mary Elizabeth Patti, MD; Bo Hu, PhD; David E. Arterburn, MD; Donald C. Simonson, MD, ScD;
              William F. Gourash, PhD; John M. Jakicic, PhD; Ashley H. Vernon, MD; Gerald J. Beck, PhD; Philip R. Schauer, MD;
              Sangeeta R. Kashyap, MD; Ali Aminian, MD; David E. Cummings, MD; John P. Kirwan, PhD


                                                                                                                                     Editorial page 643
                 IMPORTANCE Randomized clinical trials of bariatric surgery have been limited in size, type of                       Multimedia
                 surgical procedure, and follow-up duration.
                                                                                                                                     Supplemental content
                 OBJECTIVE To determine long-term glycemic control and safety of bariatric surgery compared
                 with medical/lifestyle management of type 2 diabetes.

                 DESIGN, SETTING, AND PARTICIPANTS ARMMS-T2D (Alliance of Randomized Trials of Medicine
                 vs Metabolic Surgery in Type 2 Diabetes) is a pooled analysis from 4 US single-center
                 randomized trials conducted between May 2007 and August 2013, with observational
                 follow-up through July 2022.

                 INTERVENTION Participants were originally randomized to undergo either medical/lifestyle
                 management or 1 of the following 3 bariatric surgical procedures: Roux-en-Y gastric bypass,
                 sleeve gastrectomy, or adjustable gastric banding.

                 MAIN OUTCOME AND MEASURES The primary outcome was change in hemoglobin A1c (HbA1c)
                 from baseline to 7 years for all participants. Data are reported for up to 12 years.

                 RESULTS A total of 262 of 305 eligible participants (86%) enrolled in long-term follow-up for
                 this pooled analysis. The mean (SD) age of participants was 49.9 (8.3) years, mean (SD) body
                 mass index was 36.4 (3.5), 68.3% were women, 31% were Black, and 67.2% were White.
                 During follow-up, 25% of participants randomized to undergo medical/lifestyle management
                 underwent bariatric surgery. The median follow-up was 11 years. At 7 years, HbA1c decreased
                 by 0.2% (95% CI, −0.5% to 0.2%), from a baseline of 8.2%, in the medical/lifestyle group and
                 by 1.6% (95% CI, −1.8% to −1.3%), from a baseline of 8.7%, in the bariatric surgery group.
                 The between-group difference was −1.4% (95% CI, −1.8% to −1.0%; P < .001) at 7 years and
                 −1.1% (95% CI, −1.7% to −0.5%; P = .002) at 12 years. Fewer antidiabetes medications were
                 used in the bariatric surgery group. Diabetes remission was greater after bariatric surgery
                 (6.2% in the medical/lifestyle group vs 18.2% in the bariatric surgery group; P = .02) at 7
                 years and at 12 years (0.0% in the medical/lifestyle group vs 12.7% in the bariatric surgery
                 group; P < .001). There were 4 deaths (2.2%), 2 in each group, and no differences in major
                 cardiovascular adverse events. Anemia, fractures, and gastrointestinal adverse events were
                 more common after bariatric surgery.

                 CONCLUSION AND RELEVANCE After 7 to 12 years of follow-up, individuals originally randomized
                 to undergo bariatric surgery compared with medical/lifestyle intervention had superior glycemic
                 control with less diabetes medication use and higher rates of diabetes remission.

                 TRIAL REGISTRATION ClinicalTrials.gov Identifier: NCT02328599




                                                                                                                                Author Affiliations: Author
                                                                                                                                affiliations are listed at the end of this
                                                                                                                                article.
                                                                                                                                Corresponding Author: Anita P.
                                                                                                                                Courcoulas, MD, Department of
                                                                                                                                Surgery, University of Pittsburgh,
                                                                                                                                UPMC Magee-Womens Hospital,
                 JAMA. 2024;331(8):654-664. doi:10.1001/jama.2024.0318                                                          300 Halket St, Ste C-400, Pittsburgh,
                 Corrected on July 24, 2024.                                                                                    PA 15213 (courcoulasap@upmc.edu).


        654                                                                                                                                    (Reprinted) jama.com

                                                      © 2024 American Medical Association. All rights reserved.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/29/2026

```

### Physical PDF page 002

```text
              Long-Term Outcomes of Medical Management vs Bariatric Surgery in Type 2 Diabetes                                          Original Investigation Research




              T
                     ype 2 diabetes is a progressive multifactorial disease af-
                     fecting an estimated 10% of the world’s population, or                      Key Points
                     more than 500 million adults.1 In the US, type 2 diabe-
                                                                                                 Question What is the long-term durability of glycemic control and
              tes accounts for $237 billion in direct medical costs and                          safety of bariatric surgery compared with medical/lifestyle
              $90 billion in lost productivity annually, while care for people                   management of type 2 diabetes?
              with diabetes accounts for 1 in 4 US health care dollars.2 Sev-
                                                                                                 Findings Bariatric surgery led to superior glycemic control
              eral small randomized clinical trials (RCTs) and larger obser-
                                                                                                 compared with medical/lifestyle intervention (between-group
              vational studies indicate that bariatric surgery is superior to                    difference in hemoglobin A1c of 1.4% at 7 years and 1.1% at 12
              medical and lifestyle therapies for treatment of type 2                            years), with less diabetes medication usage and higher rates of
              diabetes.3-5 To date, RCTs have been limited in number, sample                     diabetes remission.
              size, single site, operation type, severity of obesity, and
                                                                                                 Meaning These results combined with existing evidence support
              follow-up duration. Thus, despite the growing body of evi-                         the use of bariatric surgery for treatment of type 2 diabetes in
              dence, most clinicians and payers do not recommend bariat-                         people with obesity.
              ric surgery for type 2 diabetes unless an individual has a body
              mass index (BMI) of 35 or higher,6 and less than 1% of those
              with a BMI of 35 or higher consider or pursue surgical                         Program and Look AHEAD interventions. Patients who
              treatment.7 Moreover, despite the recent advent of medica-                     underwent an operation had standard postoperative care,
              tions that achieve a degree of weight loss approaching that of                 which included guidance on eating and activity, at least
              some bariatric surgical procedures, these agents are costly, do                monthly, in the first year. Observational follow-up was con-
              not have proven long-term efficacy, and require long-term use                  ducted through July 2022. Data from extended follow-up
              to maintain weight loss.                                                       were pooled and harmonized across sites for this analysis.
                   The Alliance of Randomized Trials of Medicine vs                          Additional details are provided in Supplement 2.
              Metabolic Surgery in Type 2 Diabetes (ARMMS-T2D) consor-
              tium pooled long-term observational results from 4 US                          Primary and Secondary Outcomes
              single-center randomized trials to determine the efficacy,                     The primary outcome was the between-group difference
              durability, and safety of bariatric surgery compared with                      in the percent change in HbA1c from baseline to 7 years. Addi-
              medical/lifestyle treatment for type 2 diabetes. 8 To our                      tionally, data up to 12 years are reported for participants who
              knowledge, this represents the largest pooled analysis with                    reached that follow-up point before study closure. Second-
              the longest follow-up to date. We previously reported results                  ary outcomes included change over time in HbA1c, HbA1c less
              from ARMMS-T2D at 3 years, demonstrating that bariatric                        than 7.0%, and diabetes remission (HbA1c <6.5% without dia-
              surgery is more effective and durable than medical/lifestyle                   betes medications for at least 3 months, assessed annually).21,22
              intervention for type 2 diabetes remission, even in those with                 Other secondary outcomes were between-group differences
              a BMI of 25 to less than 35.9 Herein, we report long-term                      in change in weight, BMI, lipid levels, blood pressure, medi-
              follow-up of participants in ARMMS-T2D at the primary end                      cation use, major adverse cardiovascular events, and micro-
              point of 7 years, and up to 12 years, after randomization.                     vascular complications. Main results are presented by
                                                                                             randomized group as well as by surgical procedure type.
                                                                                             For all outcomes, we hypothesized better results for bariatric
                                                                                             surgery vs medical/lifestyle treatment. Throughout, to con-
              Methods                                                                        vert HbA 1 c to mmol/mol, use the following equation:
              Study design                                                                   10.93 × HbA1c − 23.50.
              Randomized trials were conducted from May 1, 2007, to August                        Adverse events related to the original interventions were
              30, 2013, in the US at 4 centers: Cleveland Clinic (STAMPEDE),                 collected during annual study visits and at quarterly tele-
              Joslin Diabetes Center/Brigham and Women’s Hospital                            phone calls by patient self-report, with verification by medi-
              (SLIMM-T2D), University of Pittsburgh (TRIABETES), and                         cal record review. Serious adverse events were defined as
              University of Washington/Kaiser Permanente Washington                          those resulting in death, a life-threatening event, hospitaliza-
              (CROSSROADS).10-20 Written consent was obtained from par-                      tion, significant disability, incapacity, or need for urgent
              ticipants at each center, ethics approval was obtained to pool                 medical or surgical intervention to prevent a serious out-
              study results, and the pooled study analysis was registered at                 come. Events with specific relevance, including revisional
              clinicaltrials.gov (NCT02328599). The protocol is provided                     metabolic/bariatric procedures, severe hyperglycemia or
              in Supplement 1. Race and ethnicity were included in each                      hypoglycemia, and nutritional deficiencies are reported
              study because they may contribute to differential outcomes                     up to 12 years.
              from the interventions. Participants self-identified their race
              and ethnicity based on fixed categories. Original study eligi-                 Statistical Analysis
              bility included diagnosis of type 2 diabetes, BMI of 27 to 45,                 The primary statistical analysis followed the intention-to-
              and age of 18 to 65 years. Randomization protocol and opera-                   treat principle comparing the change in HbA1c from baseline
              tion types differed by site. Although medical/lifestyle inter-                 to 7 years between the 2 groups. Percent change in HbA1c was
              ventions differed by site, they were all intensive compared                    assessed using a linear mixed-effect model, which included
              with usual care and were based on the Diabetes Prevention                      group, visit, group × visit interaction, site, and baseline HbA1c

              jama.com                                                                                    (Reprinted) JAMA February 27, 2024 Volume 331, Number 8         655

                                                       © 2024 American Medical Association. All rights reserved.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/29/2026

```

### Physical PDF page 003

```text
              Research Original Investigation                                                        Long-Term Outcomes of Medical Management vs Bariatric Surgery in Type 2 Diabetes



                                                                                                         cohort. All analyses were performed using RStudio (R Foun-
              Figure 1. Assembly of the Trials in the Alliance of Randomized Trials
              of Medicine vs Metabolic Surgery in Type 2 Diabetes (ARMMS-T2D)
                                                                                                         dation) and SAS version 9.4 (SAS Institute).


                                     355 Patients randomized in 4 original trials
                                         155 In STAMPEDE
                                          88 In SLIMM-T2D                                                Results
                                          69 In TRIABETES
                                          43 In CROSSROADS                                               The 4 original trials included 355 individuals with type 2 dia-
                                                                                                         betes who were randomized to undergo bariatric surgery vs
                                                                   39 Withdrew before intervention       medical/lifestyle intervention for management of type 2 dia-
                                                                                                         betes (Figure 1).8 Randomization occurred at time of entry into
                                         316 Eligible for ARMMS-T2D trial                                the original trials; 39 individuals withdrew before the inter-
                                             145 From STAMPEDE                                           vention (more than half due to dissatisfaction with assigned
                                              78 From SLIMM-T2D
                                              61 From TRIABETES
                                                                                                         treatment group), leaving 316 eligible for the pooled analysis.
                                              32 From CROSSROADS                                         Between the end of the original trials and the beginning of the
                                                                                                         pooled analysis, 9 participants withdrew their consent and 2
                                                                      14 Excluded                        died. Of the 305 individuals available, 262 (86%) enrolled
                                                                         12 Withdrew or lost to          (Figure 1). Baseline characteristics of participants in the
                                                                            follow-upa
                                                                          2 Died                         medical/lifestyle (n = 96) and surgical (n = 166) groups are
                                                                                                         shown in Table 1. Mean (SD) age was 49.9 (8.3) years, 68.3%
                                                                                                         of participants were women, 31% were Black, and 67.2% were
                                           305 Available for long-term
                                               follow-up and randomized                                  White. Mean (SD) BMI was 36.4 (3.5) (eFigure 1 in Supple-
                                                                                                         ment 2) and 96 participants (36.6%) had a baseline BMI less
                                                                                                         than 35. Mean (SD) baseline HbA1c was 8.5% (1.5%). Median
                   193 Randomized to undergo                    122 Randomized to undergo                (range) follow-up was 11 (7-15) years; some participants with
                       bariatric surgery                            medical/lifestyle intervention
                       106 Roux-en-Y gastric bypass                                                      later enrollment did not reach 12 years of follow-up. A com-
                        49 Sleeve gastrectomy                                                            parison of patient characteristics with 7 and 12 years of
                        38 Adjustable gastric banding
                                                                                                         follow-up is shown in eTable 1 in Supplement 2.
                                                                                                              Absolute values for HbA1c over 12 years are shown in
                      166 Enrolled in ARMMS-T2D                    96 Enrolled in ARMMS-T2D
                                                                                                         Figure 2A. Despite higher baseline values, the bariatric sur-
                                                                                                         gery group had significantly lower HbA1c levels than the medi-
              a
                  Three participants who were lost to follow-up in the original trials were
                                                                                                         cal/lifestyle group at all points after baseline (P < .001;
                  successfully rerecruited into ARMMS-T2D.8
                                                                                                         Figure 2A). At 7 years, mean HbA1c decreased to 8.0% from a
                                                                                                         baseline of 8.2% (difference, 0.2% [95% CI, −0.5% to 0.2%])
                                                                                                         in the medical/lifestyle group and from 8.7% to 7.2% (differ-
              as fixed effects, as well as a random intercept at the partici-                            ence, 1.6% [95% CI, −1.8% to −1.3%]) in the bariatric surgery
              pant level. Least-square means were derived at each visit by                               group (Table 2). The between-group difference was −1.4%
              group, and the group comparison was performed by applying                                  (95% CI, −1.8% to −1.0%; P < .001) at 7 years (Table 2) and −1.1%
              appropriate linear contrast to the model. A per-protocol sen-                              (95% CI, −1.7% to −0.5%; P = .002) at 12 years (eTable 2 in
              sitivity analysis was also conducted to account for crossover                              Supplement 2). At year 7, there were no significant differ-
              from the medical/lifestyle group to the surgical group using                               ences in the improvements in mean HbA1c from baseline be-
              the inverse probability weighting approach,23-25 where the                                 tween Roux-en-Y gastric bypass (difference, −1.7% [95% CI,
              model for the inverse probability weight assumed the current                               −2.0% to −1.3%]) and sleeve gastrectomy (difference, −2.0%
              treatment depended on the previous treatments and out-                                     [95% CI, −2.6% to −1.5%]); HbA1c improvement after adjust-
              comes. Missing clinical or laboratory data were recovered using                            able gastric banding (−0.8% [95% CI, −1.3% to −0.2%]) was less
              the participants’ electronic medical record, as described in                               than for sleeve gastrectomy (P = .007) and Roux-en-Y gastric
              Supplement 2. Death or loss to follow-up were assumed to be                                bypass (P = .03) (Figure 2B). A per-protocol sensitivity analy-
              random censoring events, and the monotone missing data                                     sis accounting for the 25% crossover from medical/lifestyle in-
              caused by these events were also considered missing at ran-                                tervention to a surgical intervention showed a change in mean
              dom. Further details about handling of missing data are pro-                               HbA 1c of 0.1% (95% CI, −0.5% to 0.7%) for the medical/
              vided in Supplement 2. Binary outcomes, such as diabetes re-                               lifestyle group and −1.4% (95% CI, −1.7% to −1.2%) for the bar-
              mission and use of medications for diabetes, were summarized                               iatric surgery group at 7 years, with a between-group differ-
              as percentages and analyzed using the generalized estimat-                                 ence of −1.5% (95% CI, −2.1% to −0.9%; P < .001; eFigure 2A
              ing equation approach controlling for site and baseline HbA1c;                             in Supplement 2).
              standard errors of parameter estimates were obtained from the                                   Overall, 0.5% of participants in the medical/lifestyle
              sandwich method. The results of secondary outcomes were not                                group achieved remission of diabetes at 1 year, compared
              adjusted for multiple testing. Exploratory analyses were per-                              with 50.8% in the bariatric surgery group (Figure 3). Over
              formed to investigate the subgroup of participants with BMI                                time, the percentage achieving remission decreased in the
              less than 35 using the same set of models as for the overall                               bariatric surgery group, but remission rates remained higher

        656   JAMA February 27, 2024 Volume 331, Number 8 (Reprinted)                                                                                                      jama.com

                                                                © 2024 American Medical Association. All rights reserved.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/29/2026

```

### Physical PDF page 004

```text
              Long-Term Outcomes of Medical Management vs Bariatric Surgery in Type 2 Diabetes                                                     Original Investigation Research




              Table 1. Baseline Characteristics of Participants by Group (N = 262)

                                                                                 Bariatric surgery type
                                                                                 Roux-en-Y          Sleeve               Adjustable
                                         Medical/lifestyle   Bariatric surgery   gastric bypass     gastrectomy          gastric banding
               Characteristic            (n = 96)            (n = 166)           (n = 89)           (n = 41)             (n = 36)
               Demographics, No. (%)
               Age, y                    51.4 (6.8)          49.0 (9.0)          49.1 (9.0)         48.3 (7.7)           49.6 (10.3)
               Sex
                 Women                   62 (64.6)           117 (70.5)          61 (68.5)          32 (78.0)            24 (66.7)
                 Men                     34 (35.4)           49 (29.5)           28 (31.5)          9 (22.0)             12 (33.3)
               Race
                 Black                   35 (36.5)           46 (27.7)           23 (25.8)          13 (31.7)            10 (27.8)
                 White                   59 (61.5)           118 (71.1)          64 (71.9)          28 (68.3)            26 (72.2)
                 Othera                  2 (2.1)             2 (1.2)             2 (2.3)            0                    0
               Anthropometrics, mean (SD)
               Waist, cm                 113.7 (9.6)         115.0 (9.9)         116.1 (9.9)        113.3 (10.2)         114.5 (9.7)
                                         [n = 95]
               Weight, kg                105.6 (15.5)        103.5 (15.3)        105.2 (15.3)       100.2 (16.7)         103.1 (13.0)
               BMI                       36.2 (3.4)          36.6 (3.6)          37.0 (3.4)         36.3 (4.2)           35.9 (3.2)
               BMI <35                   40 (41.7)           56 (33.7)           26 (29.2)          15 (36.6)            15 (41.7)
               Systolic BP, mm Hg        129.7 (15.8)        134.4 (17.7)        135.0 (18.4)       135.8 (19.9)         131.6 (12.7)
               Diastolic BP, mm Hg       79.5 (9.6)          80.4 (10.0)         80.7 (9.8)         81.9 (12.2)          78.2 (7.2)
               Diabetes duration, y      8.8 (5.2)           8.3 (5.5)           8.8 (5.9)          7.8 (4.6)            7.5 (5.1)
               Laboratory
               HbA1c, mean (SD), %       8.2 (1.2)           8.7 (1.7)           8.7 (1.6)          9.4 (1.6)            8.2 (1.8)
               HbA1c <7.0%, No. (%) 11 (11.5)                20 (12.0)           9 (10.1)           0                    11 (30.6)
               Fasting glucose,          156.5 (50.0)        172.0 (69.7)        171.0 (69.5)       172.1 (66.1)         174.6 (75.9)
               mean (SD), mg/dL          [n = 95]
               Total cholesterol,        172.6 (38.5)        179.6 (44.8)        176.1 (40.7)       191.2 (46.8)         174.9 (50.7)
               mean (SD), mg/dL          [n = 95]
               HDL, mean (SD),           44.3 (13.2)         42.9 (11.6)         43.6 (11.8)        45.5 (12.2)          38.1 (9.0)
               mg/dL                     [n = 95]                                                                                           Abbreviations: ACEi,
               LDL, mean (SD),           96.3 (33.2)         100.3 (34.2)        96.3 (31.8)        110.8 (41.0)         97.8 (28.7)        angiotensin-converting enzyme
               mg/dL                     [n = 94]            [n = 159]           [n = 88]                                [n = 30]           inhibitor; ARB, angiotensin receptor
               Triglycerides, mean       140.0               145.0               143.0              160.0                142.5              blocker; BMI, body mass index;
               (SD), mg/dL               (92.5-221.5)        (103.0-231.8)       (100.0-239.0)      (120.0-214.0)        (94.0-251.5)       BP, blood pressure; HDL,
                                         [n = 95]                                                                                           high-density lipoprotein cholesterol;
               Serum creatinine,         0.7 (0.2)           0.7 (0.2)           0.7 (0.2)          0.7 (0.2)            0.8 (0.2)          LDL, low-density lipoprotein
               mean (SD), mg/dL          [n = 95]                                                                                           cholesterol.
               Urine                     6.0 (4.0-14.5)      9.0 (4.0-22.5)      7.5 (3.0-28.0)     9.0 (7.0-22.0)       6.0 (3.8-12.2)     SI conversion factors: To convert
               albumin:creatinine        [n = 74]            [n = 119]           [n = 62]                                [n = 16]           hemoglobin A1c (HbA1c) to mmol/mol,
               ratio, mean (SD)
                                                                                                                                            multiply by 10.93 and subtract 23.50;
               Medication use, No. (%)                                                                                                      glucose to mmol/L, multiply by
               Statins                   71 (74.0)           121 (72.9)          66 (74.2)          31 (75.6)            24 (66.7)          0.0555; cholesterol to mmol/L,
                                                                                                                                            multiply by 0.0259; triglycerides to
               ACEi/ARB                  65 (67.7)           108 (65.1)          63 (70.8)          25 (61.0)            20 (55.6)
                                                                                                                                            mmol/L, multiply by 0.0113;
               ACEi                      59 (61.5)           78 (47.0)           47 (52.8)          17 (41.5)            14 (38.9)          creatinine to μmol/L, multiply by
               Insulin                   36 (37.5)           82 (49.4)           46 (51.7)          17 (41.5)            19 (52.8)          88.4.
                                                                                                                                            a
               β-Blockers                16 (16.7)           30 (18.2)           15 (16.9)          6 (14.6)             9/35 (25.7)            Including 2 patients identifying as
                                                                                                                                                Asian race and 2 patients who
               ARB                       8 (8.3)             30 (18.1)           16 (18.0)          8 (19.5)             6 (16.7)
                                                                                                                                                reported more than 1 race.

              than in the medical/lifestyle group. At year 7, remission was                          of participants in the bariatric surgery group (odds ratio, 3.2
              6.2% in the medical/lifestyle group compared with 18.2% in                             [95% CI, 1.8-5.9]; P < .001; Table 2). Similar differences were
              the bariatric surgery group (odds ratio, 3.4 [95% CI, 1.3-9.2];                        observed using the threshold of HbA1c less than or equal to
              P = .02; Figure 3), with the difference remaining statistically                        6.5% (P = .002; Table 2). Moreover, improved glycemic con-
              significant at 12 years (P < .001). Rates of remission were                            trol in the bariatric surgery group was achieved using fewer
              24.5% in the Roux-en-Y gastric bypass subgroup, 15.2% in the                           medications. Rates of diabetes medication use at baseline
              sleeve gastrectomy group, and 8.9% in the adjustable gastric                           were similar between the groups (Table 2; eFigure 3 in
              banding group; comparisons between surgical procedures                                 Supplement 2) and did not change significantly over time
              were not statistically significant.                                                    in the medical/lifestyle group (P = .19 at year 7 and 0.12 at
                  At 7 years, 26.7% of participants in the medical/lifestyle                         year 12); in contrast, medication usage was reduced from
              group had an HbA1c less than 7.0%, compared with 54.1%                                 97.6% (162/166) at baseline to 38.0% (62/163) at year 1 in the

              jama.com                                                                                               (Reprinted) JAMA February 27, 2024 Volume 331, Number 8          657

                                                             © 2024 American Medical Association. All rights reserved.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/29/2026

```
