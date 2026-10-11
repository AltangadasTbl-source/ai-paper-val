# Main-paper quantitative evidence map

Scope: DOC-001, `jama_engelter_2025_oi_250066_1761597796.45511.pdf`, physical PDF pages 1–10 (printed 1523–1532), document role REPORT. Fresh main mapping, not candidate discovery or adjudication. Local relationship keys below are extraction keys for coordinator integration; they are not stable checker N/S or candidate IDs. No legacy review conclusions were read.

Evidence: reusable pdftotext native page files `.ai_paper_validation/document_outputs/main_article/preprocessing/native_text/page-001.txt` through `page-010.txt`, all read completely; source-linked rendered images `page_images/page-004.png`, `page-005.png`, and `page-006.png`, visually inspected for table nesting, labels, flow and graphics. Historical native-text engine is pdftotext; page render engine recorded by curator is PDF page render, exact historical version unspecified. Current tooling is Poppler 26.01.0, CPU. No new derivative, OCR, or render was necessary. Reusable normalized files were not needed. Every printed result-relevant relationship is indexed below; the complete page-preserving reusable native transcription remains available at those existing paths for source text/footnote lookup. Images resolve nested table layout.

Direct sources are authoritative; native text and images remain locators. Source-page links resolve from this extraction artifact. Primary comparator direction is levodopa minus placebo for mean differences, and levodopa compared with placebo for odds ratio, as printed. Denominators not expressly printed for individual continuous secondary results are not inferred from the full analysis set.

## Page coverage

| Physical page | Printed page | Mapped content | Coverage |
|---|---:|---|---|
| [1](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=1) | 1523 | Abstract: design, population, intervention, primary effect, baseline descriptive values, mortality and adverse events | COMPLETE |
| [2](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=2) | 1524 | Key Points, historical contextual numbers, design/oversight, eligibility and treatment | COMPLETE |
| [3](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=3) | 1525 | Dose schedule, randomization, outcomes/scales/time, sample-size inputs | COMPLETE |
| [4](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4) | 1526 | All Table 1 rows and footnotes; primary analysis, intercurrent events and extra estimands | COMPLETE |
| [5](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5) | 1527 | Secondary/post hoc methods, population, therapy, complete flow, Figure 2 graphics and caption | COMPLETE |
| [6](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6) | 1528 | All Table 2 rows, primary/secondary estimates, adherence and adverse-event text | COMPLETE |
| [7](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=7) | 1529 | Adverse-event text continuation, post hoc results, statistical interpretation and conclusion start | COMPLETE |
| [8](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=8) | 1530 | Conclusion continuation mapped; article information/affiliations/disclosures: no additional applicable quantitative result | COMPLETE |
| [9](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=9) | 1531 | Funding, administrative statements and references: no applicable trial quantitative result | COMPLETE |
| [10](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=10) | 1532 | References only: no applicable trial quantitative result | COMPLETE |

Total units 10; reusable-backed 10; fresh-required 0; mapped 10; gaps none. Bibliographic identifiers, dates, reference numbering and funding identifiers remain available in reusable native text but are not quantitative relationships of trial results.

## Design, analysis and occurrence relationships

Each row is one local extraction relationship; bundled numbers in one row belong to the same design, population or reported comparison.

| Key | Location | Exact quantitative/statistical evidence and matching occurrences |
|---|---|---|
| M-D01 | p1 abstract design; p5 Results | 610 randomized, 307 levodopa and 303 placebo, allocation 1:1. Abstract: 13 stroke units/centers and 11 collaborating rehabilitation centers; visits June 14, 2019 to August 27, 2024. Results: randomized June 14, 2019 to May 21, 2024 in 13 Swiss stroke units/centers. Distinct visit and randomization calendars retained. |
| M-D02 | p1 abstract intervention; pp2–3 Trial Treatment | Levodopa/carbidopa 100 mg/25 mg versus matching placebo, administered for 39 days. Abstract says 3 times daily for 39 days. Detailed morning-afternoon-evening regimen: days 1–3, 1-0-0; days 4–6, 1-1-0; days 7–34, 1-1-1; days 35–37, 1-1-0; days 38–39, 1-0-0. Continue treatment and taper if discharged before day39. Not timed to rehabilitation; full-dose schedule 3 fixed daily time points. |
| M-D03 | p2 Participants; p1 abstract | Acute stroke ≤7 days; ischemic ≥24 hours after thrombolysis/thrombectomy where applicable or hemorrhagic stroke. Clinically meaningful hemiparesis total ≥3 on NIHSS motor arm, motor leg or limb ataxia; distal arm paresis equivalent to one item. In-hospital rehabilitation required, able to participate, previously independent daily life. |
| M-D04 | p3 Randomization | Randomization stratified by study center; computer-generated minimization, 80% probability to group minimizing imbalance; no block scheme beyond minimization. Patient-level parallel groups, double-blind, placebo-controlled superiority trial (p2). |
| M-D05 | pp1,3 Primary Outcome | FMA total affected-side score at 3 months ±14 days after randomization; between-group difference. FMA 50 items scored 0 (movement not possible), 1 (partially possible), 2 (completely possible); total 0–100 points, upper66/lower34; higher is better. Assessment at3 months rather than end of treatment day39; 6-point difference patient-relevant. |
| M-D06 | p3 Sample Size | Normal FMA, SD25 points; 548 participants for 80% power, two-sided .05, mean difference6 points at3 months. Target610 with anticipated10% dropout, at least549 available for analysis. These are printed design inputs, no reconstruction here. |
| M-D07 | p4 Statistical Analyses | Primary treatment-policy estimand, randomized group; participants dying before3 months excluded (full analysis set). Survivor missing/incomplete3-month FMA: chained-equations multiple imputation. Linear regression adjusting baseline FMA total and treatment group; estimated effect, corresponding P and95%CI; alpha .05 two-sided. Center is mentioned for randomization (D04), but not named in this model description. |
| M-D08 | p4 Statistical Analyses | Seven additional predefined estimands for five intercurrent factors: death before3-month visit; serious adverse event causing motor impairment; <80% medication; <5 rehab sessions/week; outcome assessment outside3 months ±14 days. Exact estimand details deferred to eTable2, Supplement3. |
| M-D09 | p4 Statistical Analyses | Two post hoc estimands: include deaths and set FMA0; and participants receiving≥80% medication and≥5 rehab sessions/week (eTable3, Supplement3). |
| M-D10 | p5 Statistical Analyses | Post hoc primary analysis by baseline FMA≤35 (severe) versus>35 (mild/moderate), categorization from prior research. Post hoc spline terms for baseline-to3-month nonlinearity and interactions between baseline FMA and allocation. |
| M-D11 | pp3,5 secondary methods | Secondary outcomes exploratory because multiple comparisons/type I error; regression adjusted for baseline measurements. If any outcome component missing, entire summary score multiply imputed. mRS ordinal logistic regression for better/worse outcomes; mRS and relevance-of-improvement missing data not imputed. No multiplicity-adjusted primary/secondary P rule printed beyond alpha .05. |
| M-D12 | p3 Secondary Outcomes | At3 months: PROMIS29 (7 domains×4 items; raw4–20/domain; higher better in some domains/worse in others); PROMIS10 Global Health (10–50, higher better); two custom interviewer-administered yes/no items for perceived improvement and relevance. FMA upper/lower separately, FMA unaffected-side total, NIHSS0–42 higher worse, mRS0–6 higher worse/death6, Rivermead0–15 higher better (15 yes/no items). FMA affected-side total also at5 weeks. Other motor assessments at subset of centers and preplanned6/12 months are stated not reported; details protocol. |
| M-D13 | p2 oversight; pp4–5 analysis governance | Safety review after200,400,500 enrollments. SAP finalized/signed September27,2024, before database closure October15,2024; analyses November2024–August2025. p5 says prespecified analyses followed SAP and estimand terminology led to protocol/SAP differences. R4.3.1, code Supplement5. |
| M-D14 | p5 methods | Post hoc center heterogeneity plot: centers with<50 participants grouped into one cluster (eFigure5, Supplement3). |
| M-D15 | p1 abstract; p5 Results | Overall age median(IQR)73(64–82)years; female252(41.3%); baseline FMA34(14–54). p5 NIHSS7(5–10). Table1 arm values indexed separately. |
| M-D16 | pp1,5; p5 Figure1 | At3 months28(4.6%) deaths: levodopa11(3.6%), placebo17(5.6%). Survivors582(95.4%) eligible, 296/286 by arm. Abstract lists deaths28 and eligible582(95.4%). Flow exactly610→307/303→11/17 deaths→296/286 analyzed. |
| M-D17 | p5 Figure1 | Levodopa296 analyzed:282 complete cases,14 imputed=7 withdrew+7 incomplete3-month FMA. Placebo286 analyzed:269 complete cases,17 imputed=13 incomplete3-month FMA+4 withdrew. Numbers approached not systematically recorded and not reported. |
| M-D18 | pp5–6 Results | Rehab sessions mean(SD): levodopa79(35), placebo77(37); total duration45(23)h versus44(23)h; motor-learning-based sessions47(22) versus47(23). p3 expectation≥3 rehabilitative sessions/day retained separately from estimand≥5/week. |
| M-D19 | p5 continuation p6 left bottom | Medication≥80% received by252/307(82.1%) levodopa and244/303(80.5%) placebo. |
| M-D20 | p2 Key Points; pp1,6 primary results; p7 Discussion; pp7–8 Conclusions | Key Points610 participants,3-month median68 vs64, adjusted mean difference−0.90, no significant difference. Primary exact estimate indexed R01. Discussion adjusted difference not significant and<1 point on100-point scale; no secondary differences, similar serious adverse-event/death frequency. Conclusion levodopa did not significantly improve3-month motor function. |
| M-D21 | p2 contextual background | Historical trial53 patients in2001; clinical practice114/464(25%) across4 centers; meta-analysis6RCTs/795 participants, nonsignificant estimate favoring levodopa. These describe prior studies, not ESTREL participants/results; no external sources consulted. |

## Table 1: every baseline row

Location p4, Table1 including right-column continuation. Heading `No. (%)`; arm denominators levodopa307, placebo303. Median(IQR) rows retain printed labels. Zeros have no percentage printed. No inference of a missing IQR is made. Affected vessel territories may overlap (footnote c).

| Key | Characteristic as printed | Levodopa | Placebo |
|---|---|---|---|
| M-B01 | Age, median(IQR), y | 72(62–81) | 74(64–84) |
| M-B02 | Median age≥80y | 90(29.3) | 112(37.0) |
| M-B03 | Sex: female | 119(38.8) | 133(43.9) |
| M-B04 | Sex: male | 188(61.2) | 170(56.1) |
| M-B05 | Prior mRS score, median(IQR) | 0 | 0 |
| M-B06 | Hypertension | 222(72.3) | 213(70.3) |
| M-B07 | Hyperlipidemia | 139(45.3) | 152(50.2) |
| M-B08 | Diabetes | 80(26.1) | 64(21.1) |
| M-B09 | Atrial fibrillation | 34(11.1) | 61(20.1) |
| M-B10 | Smoking | 68(22.1) | 59(19.5) |
| M-B11 | Coronary heart disease | 52(16.9) | 47(15.5) |
| M-B12 | Depression | 23(7.5) | 18(5.9) |
| M-B13 | Dementia | 11(3.6) | 9(3.0) |
| M-B14 | Movement disorder | 6(2.0) | 5(1.7) |
| M-B15 | Prior ischemic stroke | 39(12.7) | 43(14.2) |
| M-B16 | Prior hemorrhagic stroke | 5(1.6) | 6(2.0) |
| M-B17 | Prestroke living: home | 302(98.4) | 294(97.0) |
| M-B18 | Prestroke living: nursing home | 4(1.3) | 5(1.7) |
| M-B19 | Prestroke living: other | 1(0.3) | 4(1.3) |
| M-B20 | Stroke type: ischemic | 260(84.7) | 259(85.5) |
| M-B21 | Stroke type: hemorrhagic | 47(15.3) | 44(14.5) |
| M-B22 | Anterior cerebral artery | 37(12.1) | 31(10.2) |
| M-B23 | Middle cerebral artery | 230(74.9) | 230(75.9) |
| M-B24 | Posterior cerebral artery | 27(8.8) | 33(10.9) |
| M-B25 | Vertebrobasilar(infratentorial) | 63(20.5) | 45(14.9) |
| M-B26 | FMA affected-side total at randomization, median(IQR) | 35.0(14.8–55.3) | 33.0(13.0–52.8) |
| M-B27 | FMA affected-side upper at randomization, median(IQR) | 20.0(6.0–35.0) | 17.5(6.0–34.0) |
| M-B28 | FMA affected-side lower at randomization, median(IQR) | 15.0(6.0–21.0) | 14.0(7.0–21.0) |
| M-B29 | NIHSS at randomization, median(IQR) | 7(5–11) | 8(5–10) |
| M-B30 | mRS at randomization:0 | 2(0.7) | 0 |
| M-B31 | mRS at randomization:1 | 0 | 2(0.7) |
| M-B32 | mRS at randomization:2 | 6(2.0) | 3(1.0) |
| M-B33 | mRS at randomization:3 | 37(12.1) | 32(10.6) |
| M-B34 | mRS at randomization:4 | 170(55.4) | 169(55.8) |
| M-B35 | mRS at randomization:5 | 92(30.0) | 97(32.0) |
| M-B36 | Stroke onset to randomization, median(IQR),d | 3.0(2.0–5.0) | 3.0(2.0–5.0) |

Table1 footnotes: (a)mRS0=no symptoms,6=death, higher worse; (b)other living arrangements outside private home/institutional care, such as assisted living/older adult residences; (c)imaging-defined vascular territory, multiple territories per person; (d)FMA0–100 upper66/lower34 higher better, baseline approximately35 corresponds moderate/severe motor impairment; (e)NIHSS0–42 higher deficit,7–8 moderate severity; (f)most mRS4, unable to walk without assistance or attend bodily needs without help. These define population/scale and permitted overlapping totals.

## Primary, secondary, figure and interpretation relationships

All CIs below explicitly95%. Secondary mean differences adjusted for baseline measurements (D11); continuous result denominators are not printed in p6 narrative. Primary full analysis set and imputation described in D07/D16/D17. No secondary P values or test statistics/standard errors printed in the main narrative. Outcomes at3 months unless stated otherwise.

| Key | Location/outcome | Arm descriptions | Effect/test and matching narrative |
|---|---|---|---|
| M-R01 | pp1,6 primary FMA affected-side total at3mo | Median(IQR)68(42–85) levodopa;64(44–83) placebo | Baseline-adjusted mean difference−0.90 points,95%CI−3.78 to1.98,P=.54; p6 estimand1 eTable2/eFigure4 Supplement3; p2 Key Points matches median68/64 and difference−0.90; p7 says not significant and<1 point on100-point scale. |
| M-R02 | p5 Figure2 A baseline | Levodopa vs placebo dots/boxplots, y0,20,40,60,80,100 | Baseline FMA total; no explicit printed medians beyond plotted lines. Exact baseline values Table1 B26; all plotted points not enumerated as patient data. |
| M-R03 | p5 Figure2 B3mo | Levodopa vs placebo dots/boxplots, y0,20,40,60,80,100 |3-month total; medians/IQR are R01. Caption boxes IQR, median line, whiskers most extreme within1.5×IQR (Tukey adjacent values). No CI/mean comparison in this plot. |
| M-R04 | p5 Figure2 C change baseline→3mo | Levodopa vs placebo dots/boxplots, y−60,−40,−20,0,20,40,60,80,100 | Change FMA total score, distinct from endpoint panelB; no printed exact change summary/CI/P. Same box/whisker definition R03. |
| M-R05 | p6 PROMIS29 | Mean(SD)66(14) vs65(14) | Adjusted mean difference−0.37 points,CI−3.34 to2.61. |
| M-R06 | p6 PROMIS10 | Mean(SD)28(6) both arms | Adjusted mean difference0.18,CI−0.98 to1.33. |
| M-R07 | p6 patient-reported relevance of motor improvement |51/276(18%) levodopa;52/270(19%) placebo | Counts are no improvement OR no relevant improvement; no effect/CI/P printed in main. Outcome missing not imputed. |
| M-R08 | p6 FMA upper affected side | Mean(SD)39(19) both arms | Adjusted mean difference−0.73 points,CI−2.97 to1.50. |
| M-R09 | p6 FMA lower affected side | Mean(SD)23(7) both arms | Adjusted mean difference−0.13 points,CI−1.02 to0.77. |
| M-R10 | p6 FMA total unaffected side | Mean(SD)90(10) vs89(10) | Adjusted mean difference0.63,CI−0.72 to1.99. |
| M-R11 | p6 NIHSS | Mean(SD)4(3) both arms | Adjusted mean difference−0.14 points,CI−0.61 to0.33. |
| M-R12 | p6 Rivermead Mobility Index | Mean(SD)10(5) both arms | Adjusted mean difference−0.33,CI−1.04 to0.37. |
| M-R13 | p6 mRS | Median(IQR)3.0(2.0–4.0) both arms | Ordinal logistic regression for odds of better functional outcomes: adjusted OR0.93,CI0.69–1.23 levodopa compared with placebo. Methods p5 refer to better or worse outcomes; p6 explicitly better. Missing mRS not imputed. |
| M-R14 | p6 FMA affected-side total at5weeks | Mean(SD)57(27) levodopa;56(26) placebo | Adjusted mean difference0.02 points,CI−2.81 to2.84; results pointer eTable4 Supplement3. |
| M-R15 | pp6–7 additional analyses | Seven additional estimands, post hoc estimands and baseline≤35/>35 subgroup | p6 states results similar to primary(eTables2–3/eFigures4,7). p7 nonlinear baseline→3mo association did not impact primary treatment effect, no baseline×treatment interaction(eTables7–8/eFigures6–7). No estimates/P in main for these statements; exact supplemental results require support map. |

## Table 2: every adverse-event row and nesting

p6 Table2 title `Adverse Events Stratified by Group`; heading `Events, No.`. Columns are event totals, serious126/129 and prespecified-interest79/67, rather than counts of all randomized participants. Nested subtype totals are printed under infection, stroke, cardiac event and trauma; no mutually exclusive claim is supplied here. Table footnote: interest events possibly related to levodopa according to prior research; collected through medical chart review and patient self-report during study visits.

| Key | Row and nesting | Levodopa events | Placebo events |
|---|---|---:|---:|
| M-A01 | Serious events: infection |55|44|
| M-A02 | Infection: pulmonary |27|17|
| M-A03 | Infection: urinary tract |15|15|
| M-A04 | Infection: abdominal |5|7|
| M-A05 | Infection: meningoencephalitis/encephalitis |0|2|
| M-A06 | Infection: unspecified |1|2|
| M-A07 | Infection: other |11|9|
| M-A08 | Serious events: stroke |16|19|
| M-A09 | Stroke: ischemic |15|18|
| M-A10 | Stroke: hemorrhagic |1|1|
| M-A11 | Serious events: major extracranial bleeding |5|10|
| M-A12 | Serious events: cardiac event |12|3|
| M-A13 | Cardiac event: acute coronary syndrome |5|1|
| M-A14 | Cardiac event: heart failure |5|2|
| M-A15 | Cardiac event: arrhythmia |2|0|
| M-A16 | Serious events: cancer/malignant neoplasm |4|7|
| M-A17 | Serious events: trauma |4|5|
| M-A18 | Trauma: fall |4|5|
| M-A19 | Serious events: kidney failure |6|2|
| M-A20 | Serious events: epileptic seizure |3|6|
| M-A21 | Serious events: deep vein thrombosis/pulmonary embolism |3|4|
| M-A22 | Serious events: electrolyte disorder |2|2|
| M-A23 | Serious events: fracture |1|3|
| M-A24 | Serious events: traumatic intracerebral hemorrhage |0|0|
| M-A25 | Serious events: other(none of above) |32|34|
| M-A26 | Prespecified-interest: confusion |12|9|
| M-A27 | Prespecified-interest: nausea |11|7|
| M-A28 | Prespecified-interest: postural hypotension syncope |10|4|
| M-A29 | Prespecified-interest: hallucinations |3|10|
| M-A30 | Prespecified-interest: depression |6|9|
| M-A31 | Prespecified-interest: vomiting |8|5|
| M-A32 | Prespecified-interest: arrhythmias |5|3|
| M-A33 | Prespecified-interest: dizziness |4|4|
| M-A34 | Prespecified-interest: fatigue |4|2|
| M-A35 | Prespecified-interest: abnormal dreams |1|3|
| M-A36 | Prespecified-interest: anxiety |3|3|
| M-A37 | Prespecified-interest: insomnia |1|4|
| M-A38 | Prespecified-interest: dry mouth |3|2|
| M-A39 | Prespecified-interest: dyskinesia |3|1|
| M-A40 | Prespecified-interest: taste disturbances |3|0|
| M-A41 | Prespecified-interest: drowsiness(including sudden onset sleep) |1|0|
| M-A42 | Prespecified-interest: psychoses |1|1|

| Key | Additional event/participant relationship | Locations |
|---|---|---|
| M-A43 |255 serious events in177/610 participants;126 levodopa and129 placebo. Infection most common55/44. | p6 Adverse Events; abstract p1 repeats126/129 and infection55/44; Table2 headers and A01 |
| M-A44 |146 prespecified-interest events in115/610 participants,79 levodopa and67 placebo. Most common confusion12 levodopa/hallucinations10 placebo. | p6 text continues p7; Table2 headers and A26/A29. eTables5–6 Supplement3 hold severity/outcomes. |

## Handoff scope and limitations

Local relationship count:116 =21 design/occurrence +36 baseline +15 primary/secondary/figure +44 adverse-event relationships. Every relationship is source-located; the coordinator may split bundled inferential/design relationships when assigning stable N/S keys. Every continuous effect and CI, all printed P values, all counts/percentages and outcome-scale definitions are covered. There are no reported main-paper rates, person-time quantities, explicit test statistics or standard errors to add. No scientific gaps. Exact participant-level coordinates in dotplots cannot be read as raw data and are not needed for the printed-summary review; plotted distributions, axes, panels and caption were inspected. Some continuous secondary narrative denominators are unprinted; this is a source reporting limitation, not a missing mapping unit. No screening, candidate diagnosis, inclusion decision or scientific adjudication is supplied by this mapper.

## Complete page-preserving native transcription locator

For downstream lookup use the ten existing native page files named in the evidence paragraph, without copying or modifying them. They contain complete source text, repeated publication headers, footnotes and references. The structured relationships above resolve native extraction ordering and indentation; no old quantitative extraction conclusions are needed.
