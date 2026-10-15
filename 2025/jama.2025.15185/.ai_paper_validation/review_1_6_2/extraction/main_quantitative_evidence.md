# Main-paper quantitative evidence map

Fresh mapping stage; DOC-001, REPORT, all physical PDF pages 1–10 (printed 1523–1532). No prior candidate, checker, screening, classification, diagnostic calculation, or final-report records were used. This is factual extraction and relationship indexing, without candidate judgments.

Source: `jama_engelter_2025_oi_250066_1761597796.45511.pdf`. Source links below are relative to this extraction artifact. L = levodopa/carbidopa plus standardized rehabilitation; P = placebo plus standardized rehabilitation. A pair is always L; P. Parentheses are percentages unless explicitly identified as SD or IQR. Numerators in Table 1 use randomized denominators L 307 and P 303; adverse-event Table 2 cells are event counts, not participant counts. No rate or person-time results are printed in the main article. No numerical test statistics or standard errors are printed.

## Evidence acquisition and complete unit coverage

Reusable locators inspected: `.ai_paper_validation/document_outputs/main_article/preprocessing/normalized_text/page-001.txt` through `page-010.txt`, and reusable rendered images `page_images/page-004.png`, `page-005.png`, `page-006.png` under that preprocessing directory. Historical native/normalized engine: Poppler/pdftotext, historical version unspecified. All three reusable images were visually inspected, including complete Table 1, Figure 1, Figure 2, and Table 2.

Fresh source confirmation: `.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py text jama_engelter_2025_oi_250066_1761597796.45511.pdf --first N --last N .ai_paper_validation/review_1_6_2/preprocessing/main_current/page-N.txt`, for each N = 1 through 10. Engine: PyMuPDF 1.26.4, CPU. These ten derivatives were read alongside the reusable page text; the reusable layout preserves column order better. No new rendering or OCR was needed. Native extraction encodes the abstract eligibility ≥ symbol as a control glyph; reusable text and p2 Participants establish the intended ≥3 reading. No numeric normalization was inferred from that glyph.

| Physical page | Content inspected | Mapping disposition |
|---|---|---|
| 1 | Title, entire abstract, intervention, outcomes, results, conclusion | COMPLETE: N001–N006 and S001–S002; matching body relationships indexed below |
| 2 | Introduction, Key Points, design/oversight, eligibility, treatment | COMPLETE: N007–N012; S003–S004; primary-result matching |
| 3 | Treatment schedule, randomization, primary/secondary outcome definitions, sample size | COMPLETE: N013–N021; S005–S008 |
| 4 | Entire Table 1, all footnotes, statistical analysis text | COMPLETE: N022–N059; S009–S012 |
| 5 | Entire methods continuation, Results, Figure 1, Figure 2 | COMPLETE: N060–N067; S013–S017 |
| 6 | Entire Table 2 and footnote, adherence continuation, primary/secondary results, harms | COMPLETE: N068–N111; S018–S027 |
| 7 | Harms continuation, additional post hoc analyses, Discussion, Limitations, Conclusions start | COMPLETE: N112–N113; S028–S029; narrative matches |
| 8 | Conclusion continuation, article information, author roles and disclosures | COMPLETE: S030; no additional applicable quantitative trial relationship in administrative content |
| 9 | Disclosures, funding, sharing pointer, references 1–37 | COMPLETE: no applicable new quantitative trial relationship; bibliographic years, pages, IDs are administrative |
| 10 | References 38–49 | COMPLETE: no applicable new quantitative trial relationship; bibliographic numbers are administrative |

Total mapped: 10/10 pages; reusable-backed 10; fresh-required 0; scientific gaps 0. Relationship inventory: 113 numeric/reporting records N001–N113 and 30 statistical/design/inferential records S001–S030. Multiple related printed cells are retained in one row where they describe the same comparison; these counts are relationship records, not a count of printed scalar values.

## Numeric and reporting relationships

### Abstract, introduction, and intervention definitions

| ID | Exact source location | Printed quantitative relationship, label, population and time |
|---|---|---|
| N001 | [p1, abstract Design](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=1) | 13 stroke units/centers; 11 collaborating rehabilitation centers in Switzerland; 610 acute ischemic/hemorrhagic stroke participants, randomized 1:1. First patient first visit June 14, 2019; last patient last visit August 27, 2024; analyses November 2024–August 2025. |
| N002 | [p1, abstract Intervention](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=1) | Levodopa/carbidopa 100/25 mg, L n=307; P n=303; described as 3 times daily for 39 days; standardized active task-oriented rehabilitation in both groups. Detailed schedule N013. |
| N003 | [p1, abstract Results](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=1) | Overall baseline n=610; median (IQR) age 73 (64–82) years; female 252 (41.3%); baseline FMA total median (IQR) 34 (14–54). Matches p5 Results. |
| N004 | [p1, abstract Results](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=1) | 28 deaths by 3 months; remaining 582 (95.4%) eligible for primary analysis. Matches detailed p5 flow N060–N064. |
| N005 | [p1, abstract Results](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=1) | 3-month FMA total median (IQR), points: L 68 (42–85); P 64 (44–83). Same result p2 Key Points (medians only), p6 Primary Outcome and p5 Figure 2B. Inferential comparison S001/S018. |
| N006 | [p1, abstract Results](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=1) | Serious adverse events L126; P129; most common infection L55; P44. These are event numbers; matched p6 Table 2 and harms narrative. |
| N007 | [p2, Introduction](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=2) | Background-only historical trial (2001) n=53; prior practice study at 4 Swiss rehabilitation centers: 114/464 (25%) received levodopa; meta-analysis 6 RCTs, 795 participants, nonsignificant point estimate favoring levodopa. No quantitative pooled estimate printed. These are supplied contextual claims, not ESTREL observations. |
| N008 | [p2, Key Points](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=2) | Trial including 610 participants; 3-month FMA medians L68 vs P64; adjusted mean between-group difference −0.90 points; no statistically significant difference. Matches abstract and p6. |
| N009 | [p2, Trial Design/Oversight](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=2) | Independent safety monitoring after enrollment of 200, 400 and 500 participants. No numerical stopping boundary printed here. |
| N010 | [p2, Trial Design/Oversight](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=2) | SAP finalized/signed September 27, 2024, before database closure October 15, 2024; report states trial adhered to protocol and results in line with SAP, Supplement 2. |
| N011 | [p2, Participants](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=2) | Acute stroke ≤7 days; ischemic stroke ≥24 h after thrombolysis/thrombectomy if applicable, or hemorrhagic stroke; clinically meaningful hemiparesis total ≥3 on NIHSS motor arm/motor leg/limb ataxia; distal arm paresis equivalent to one specified item, assessed by extra NIHSS Supplementary Scale item. Required inpatient rehabilitation, ability to participate, prior daily-life independence. Full criteria pointer eFigure 1 Supplement 3. |
| N012 | [p2, Trial Treatment](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=2) | Active oral levodopa 100 mg/carbidopa 25 mg or matching placebo, both 39 days. |
| N013 | [p3, Trial Treatment continuation](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=3) | Three phases, morning–afternoon–evening tablets: days1–3 1-0-0; days4–6 1-1-0; days7–34 1-1-1; days35–37 1-1-0; days38–39 1-0-0. Continue through day39 even after earlier discharge. |
| N014 | [p3, Trial Treatment](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=3) | Expected ≥3 rehabilitation-care sessions/day. Medication not timed to therapy; routine fixed schedule, e.g. 3 times/day during full-dose phase. |
| N015 | [p3, Primary Outcome](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=3) | FMA total affected-side motor function, 3 months ±14 days after randomization, rather than day39/end treatment. Total 50 items; each 0 movement not possible, 1 partially possible, 2 completely possible; total 0–100, upper extremity 66, lower extremity34. Higher better. |
| N016 | [p3, Secondary Outcomes](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=3) | PROMIS-29: 7 domains×4 items, raw range4–20/domain; direction differs by domain. PROMIS-10 Global Health raw10–50, higher better. Relevance of improvement: 2 custom interviewer-administered yes/no items, perceived improvement and daily-life relevance. All assessed at 3 months. |
| N017 | [p3, Secondary Outcomes](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=3) | Secondary 3-month measures: affected FMA upper/lower separately, unaffected-side FMA total, NIHSS0–42 (higher more impairment), mRS0–6 (0 no symptoms;6 death, higher worse), Rivermead Mobility Index0–15 (15 yes/no items, higher greater mobility). Additional FMA total at5 weeks. |
| N018 | [p3, Secondary Outcomes](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=3) | Other motor assessments in subsets/other preplanned time points e.g.6 and12 months are stated not reported; details protocol Supplement1. |
| N019 | [p3, Measures of harm](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=3) | All-cause mortality, any recurrent stroke, serious adverse events and prespecified events of interest possibly related to levodopa; definition pointer eTable9 Supplement3. |
| N020 | [p3, Sample Size Estimation](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=3) | Normal FMA distribution, SD25; mean difference6 points at3 months considered patient-relevant; calculated sample548, 80% power, two-sided .05. Statistical relationship S008. |
| N021 | [p3, Sample Size Estimation](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=3) | Enrollment target610 with10% anticipated dropout; at least549 available for analysis. |

### Table 1: all displayed baseline values

Every row below is [PDF p4, Table 1](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4), REPORT. Columns L n307; P n303. These denominators are printed at both portions of the table. Values remain descriptive baseline quantities, not adjusted comparisons.

| ID | Exact row | L | P | Unit/type and footnote context |
|---|---|---|---|---|
| N022 | Age |72 (62–81)|74 (64–84)|Median (IQR), years |
| N023 | Median age ≥80 y |90 (29.3)|112 (37.0)|Printed count (%) label retained verbatim |
| N024 | Sex: female |119 (38.8)|133 (43.9)|Count (%) |
| N025 | Sex: male |188 (61.2)|170 (56.1)|Count (%) |
| N026 | Prior mRS score |0|0|Median (IQR) heading; no IQR limits printed; footnote a0–6, higher worse |
| N027 | Hypertension |222 (72.3)|213 (70.3)|Count (%) |
| N028 | Hyperlipidemia |139 (45.3)|152 (50.2)|Count (%) |
| N029 | Diabetes |80 (26.1)|64 (21.1)|Count (%) |
| N030 | Atrial fibrillation |34 (11.1)|61 (20.1)|Count (%) |
| N031 | Smoking |68 (22.1)|59 (19.5)|Count (%) |
| N032 | Coronary heart disease |52 (16.9)|47 (15.5)|Count (%) |
| N033 | Depression |23 (7.5)|18 (5.9)|Count (%) |
| N034 | Dementia |11 (3.6)|9 (3.0)|Count (%) |
| N035 | Movement disorder |6 (2.0)|5 (1.7)|Count (%) |
| N036 | Prior stroke: ischemic |39 (12.7)|43 (14.2)|Count (%) |
| N037 | Prior stroke: hemorrhagic |5 (1.6)|6 (2.0)|Count (%) |
| N038 | Prestroke living: home |302 (98.4)|294 (97.0)|Count (%) |
| N039 | Prestroke living: nursing home |4 (1.3)|5 (1.7)|Count (%) |
| N040 | Prestroke living: other |1 (0.3)|4 (1.3)|Count (%); footnote b outside private homes/institutional care, e.g. assisted living/older-adult residences |
| N041 | Stroke type: ischemic |260 (84.7)|259 (85.5)|Count (%) |
| N042 | Stroke type: hemorrhagic |47 (15.3)|44 (14.5)|Count (%) |
| N043 | Vessel: anterior cerebral artery |37 (12.1)|31 (10.2)|Count (%); footnote c imaging, multiple territories possible |
| N044 | Vessel: middle cerebral artery |230 (74.9)|230 (75.9)|Count (%); multiple territories possible |
| N045 | Vessel: posterior cerebral artery |27 (8.8)|33 (10.9)|Count (%); multiple territories possible |
| N046 | Vessel: vertebrobasilar (infratentorial) |63 (20.5)|45 (14.9)|Count (%); multiple territories possible |
| N047 | Affected-side FMA total at randomization |35.0 (14.8–55.3)|33.0 (13.0–52.8)|Median (IQR), points; footnote d0–100, higher better |
| N048 | Affected-side FMA upper at randomization |20.0 (6.0–35.0)|17.5 (6.0–34.0)|Median (IQR), points, max66 |
| N049 | Affected-side FMA lower at randomization |15.0 (6.0–21.0)|14.0 (7.0–21.0)|Median (IQR), points, max34 |
| N050 | NIHSS at randomization |7 (5–11)|8 (5–10)|Median (IQR); footnote e0–42, higher greater deficit;7–8 moderate stroke |
| N051 | mRS at randomization:0 |2 (0.7)|0|Count (%) |
| N052 | mRS at randomization:1 |0|2 (0.7)|Count (%) |
| N053 | mRS at randomization:2 |6 (2.0)|3 (1.0)|Count (%) |
| N054 | mRS at randomization:3 |37 (12.1)|32 (10.6)|Count (%) |
| N055 | mRS at randomization:4 |170 (55.4)|169 (55.8)|Count (%); footnote f moderately severe disability, unable to walk/attend bodily needs without help |
| N056 | mRS at randomization:5 |92 (30.0)|97 (32.0)|Count (%) |
| N057 | Stroke onset to randomization |3.0 (2.0–5.0)|3.0 (2.0–5.0)|Median (IQR), days; continuation panel at upper right |
| N058 | Table1 footnote d interpretation |Approximately35 points|Same scale|Baseline FMA total around35 corresponds moderate to severe motor impairment; no additional result estimate |
| N059 | Baseline cross-location linkage |N022–N057|N003/N061|p5/abstract overall median age73(64–82), female252(41.3), FMA34(14–54), NIHSS7(5–10); group medians remain group-specific |

### Participant flow, rehabilitation exposure and figures

| ID | Exact source location | Printed relationship |
|---|---|---|
| N060 | [p5, Results/Figure1](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5) | Randomized610 = L307; P303;13 Swiss stroke units/centers. Recruitment June14,2019–May21,2024; last-visit calendar in abstract is separately labeled. |
| N061 | [p5, Results](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5) | Overall age73(64–82) years, female252(41.3%), NIHSS7(5–10), baseline FMA34(14–54); medians/IQR except female. |
| N062 | [p5, Results/Figure1](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5) | Deaths before3-month assessment total28(4.6%); L11(3.6%); P17(5.6%). Primary eligible/analyzed582(95.4%), L296;P286. |
| N063 | [p5, Figure1 L branch](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5) | L307 randomized;11 died;296 analyzed:282 complete cases and14 imputed; imputed comprise7 withdrew and7 incomplete3-month FMA. |
| N064 | [p5, Figure1 P branch](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5) | P303 randomized;17 died;286 analyzed:269 complete cases and17 imputed; imputed comprise13 incomplete3-month FMA and4 withdrew. Approached count not systematically recorded/not reported (figure caption). |
| N065 | [p5, Results](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5) | Rehabilitation exposure mean(SD): sessions L79(35);P77(37); total hours L45(23);P44(23); motor-learning sessions L47(22);P47(23). No exposure-specific participant denominator printed in paragraph. |
| N066 | [pp5–6, Results continuation](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6) | Received ≥80% medication: L252(82.1%);P244(80.5%); randomized denominators307/303. |
| N067 | [p5, Figure2 panels A/B/C](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5) | Dot/boxplots, L left and P right in each panel: A baseline FMA total; B3-month total; C change baseline to3 months. A/B y-axis0,20,40,60,80,100; C−60,−40,−20,0,20,40,60,80,100. Horizontal lines medians, boxes IQR, whiskers most extreme values within1.5×IQR from lower/upper quartiles (Tukey adjacent values). No exact change median/IQR or per-panel n printed; no individual-point digitization substituted for reported values. B matches N005; A matches N047. |

### Table 2: all adverse-event cells

Every row below is [PDF p6, Table2](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6), REPORT. Heading “Events, No.”; serious events column totals L126/P129. Prespecified-interest section separately prints L n79/P n67. Subtype indentation is retained in row labels. The table does not state that all subtype rows are mutually exclusive. Footnote a: prespecified events possibly related to levodopa according to prior research; collected through medical chart review and patient self-report during study visits.

| ID | Event row | L | P |
|---|---|---:|---:|
| N068 | Serious adverse events: column heading totals |126|129|
| N069 | Infection |55|44|
| N070 | Infection: pulmonary |27|17|
| N071 | Infection: urinary tract |15|15|
| N072 | Infection: abdominal |5|7|
| N073 | Infection: meningoencephalitis/encephalitis |0|2|
| N074 | Infection: unspecified |1|2|
| N075 | Infection: other |11|9|
| N076 | Stroke |16|19|
| N077 | Stroke: ischemic |15|18|
| N078 | Stroke: hemorrhagic |1|1|
| N079 | Major extracranial bleeding |5|10|
| N080 | Cardiac event |12|3|
| N081 | Cardiac: acute coronary syndrome |5|1|
| N082 | Cardiac: heart failure |5|2|
| N083 | Cardiac: arrhythmia |2|0|
| N084 | Cancer/malignant neoplasm |4|7|
| N085 | Trauma |4|5|
| N086 | Trauma: fall |4|5|
| N087 | Kidney failure |6|2|
| N088 | Epileptic seizure |3|6|
| N089 | Deep vein thrombosis/pulmonary embolism |3|4|
| N090 | Electrolyte disorder |2|2|
| N091 | Fracture |1|3|
| N092 | Traumatic intracerebral hemorrhage |0|0|
| N093 | Other (none of the above) |32|34|
| N094 | Prespecified adverse events of interest: heading totals |79|67|
| N095 | Confusion |12|9|
| N096 | Nausea |11|7|
| N097 | Postural hypotension syncope |10|4|
| N098 | Hallucinations |3|10|
| N099 | Depression |6|9|
| N100 | Vomiting |8|5|
| N101 | Arrhythmias |5|3|
| N102 | Dizziness |4|4|
| N103 | Fatigue |4|2|
| N104 | Abnormal dreams |1|3|
| N105 | Anxiety |3|3|
| N106 | Insomnia |1|4|
| N107 | Dry mouth |3|2|
| N108 | Dyskinesia |3|1|
| N109 | Taste disturbances |3|0|
| N110 | Drowsiness (including sudden onset of sleep) |1|0|
| N111 | Psychoses |1|1|

| ID | Exact source location | Printed relationship |
|---|---|---|
| N112 | [pp6–7, Adverse Events narrative](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=7) |255 serious events in177/610 participants;126 L and129 P; infection L55/P44 most common.146 prespecified-interest events in115/610 participants;79 L and67 P; most common L confusion12, P hallucinations10. Narrative links Table2 and eTables5/6 Supplement3 for severity/outcomes. Event and affected-person counts explicitly distinct. |
| N113 | [p7, Discussion/Limitations](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=7) |Primary adjusted difference described as <1 point on100-point scale. Trial exclusively Swiss; FMA interrater reliability not systematically assessed across entire population; no levodopa serum levels; therapy homogeneity across centers unassessed; genetic variation not accounted for. No new quantitative estimate supplied. |

## Statistical, estimand, model and interpretation relationships

All entries concern REPORT content in DOC-001. Location links preserve physical PDF page. Quantitative estimates below are L relative to P. “Mean difference” is reported adjusted and must remain distinct from crude differences in printed means/medians. Unless a row says otherwise, secondary outcomes are at3 months, adjusted for baseline measurements (p5 methods), with exploratory interpretation owing to multiple comparisons (p3). Secondary-result paragraph prints CIs but no P values; none is supplied here by inference. Primary analysis n582 survivors, L296/P286; secondary per-outcome n generally not printed in main article except relevance-of-improvement response counts. The main article states missing mRS and relevance data are not imputed.

| ID | Exact source location | Reconstructed relationship and matching claims |
|---|---|---|
| S001 | [p1, abstract outcomes/results](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=1) |Primary adjusted mean between-group FMA total difference at3 months −0.90 points,95%CI−3.78 to1.98,P=.54. Scale0–100, fewer worse;6-point difference patient-relevant. Descriptive medians68 vs64 are N005. Matches S018. |
| S002 | [p1, abstract conclusion](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=1) |No significant motor-function improvement at3 months from levodopa added to standardized inpatient rehabilitation; does not support adjunct use for motor recovery. Reference S001; repeated p2 Key Points and pp7–8 conclusion. |
| S003 | [p2, Trial Design](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=2) |Randomized double-blind placebo-controlled multicenter parallel-group superiority trial; participant is randomized unit. |
| S004 | [p2, Oversight](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=2) |Safety reviews after200/400/500 enrollment; SAP finalized September27,2024 before database closure October15,2024; report claims protocol adherence/SAP alignment. No stopping calculation or numerical efficacy interim decision printed. |
| S005 | [p3, Randomization](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=3) |1:1 assignment, stratified by center; computer-generated minimization,80% probability to group minimizing imbalance within center; no block scheme beyond minimization. |
| S006 | [p3, Outcomes](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=3) |Primary affected-side FMA total at3 months±14days after randomization; separate5-week secondary FMA; not end-of39-day treatment as primary. Definitions/scales N015–N018. |
| S007 | [p3, Secondary Outcomes](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=3) |All listed3-month secondary outcomes and5-week FMA considered purely exploratory because of potential type I error from multiple comparisons; no familywise correction rule printed. Other planned subset/6-/12-month motor assessments stated not reported. |
| S008 | [p3, Sample Size](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=3) |Normal FMA, SD25, mean difference6,80% power,two-sided α.05,calculated548;target610 anticipating10% dropout and≥549 evaluable. No model-adjusted variance assumption or alternative sample-size formula printed. Inputs retained for checkers, no recomputation judged here. |
| S009 | [p4, Statistical Analyses primary](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4) |Named treatment policy estimand; randomized-group analysis; deaths before3 months excluded, called full analysis set. Missing/incomplete survivor3-month FMA imputed using chained equations. Linear regression with treatment plus baseline FMA total; report estimate,P,95%CI;two-sided α=.05. Main article lists no center covariate in this model sentence. |
| S010 | [p4, additional estimands](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4) |7 additional predefined estimands address5 intercurrent factors: death; motor-impairing serious event (recurrent stroke/fracture);<80% medication;<5 rehab sessions/week; assessment outside3months±14days. Details eTable2 Supplement3. |
| S011 | [p4, post hoc estimands](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4) |Post hoc all-deaths analysis assigns FMA0 to deaths before3months; details eTable3. |
| S012 | [p4, post hoc estimands](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4) |Post hoc adherent subset receives≥80% medication AND≥5rehab sessions/week; details eTable3. |
| S013 | [p5, Methods continuation](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5) |Post hoc primary analysis repeated by baseline FMA≤35 severe vs>35 mild–moderate; dichotomized population based on prior categorization. |
| S014 | [p5, Secondary methods](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5) |Secondary outcomes regression adjusted for baseline measurements; any missing component leads entire summary score to multiple imputation. mRS ordinal logistic regression estimates odds of better/worse outcome across categories; mRS and relevance-of-improvement missing data not imputed. |
| S015 | [p5, exploratory heterogeneity](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5) |Post hoc center treatment-effect heterogeneity plot eFigure5; centers with<50participants grouped as one cluster. No center-specific estimate printed in main article. |
| S016 | [p5, nonlinearity/interaction](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5) |Post hoc spline terms for baseline-to3-month FMA association; tests baseline FMA×treatment interactions. No numerical spline/interaction statistic here. |
| S017 | [p5, Prespecification/software](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5) |Prespecified analyses described as SAP-based before database closure; report says SAP/protocol differences concern emerging estimand terminology, general statistical considerations aligned. Analyses R4.3.1; main code Supplement5. |
| S018 | [p6, Primary Outcome](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6) |Affected FMA total at3months: medians(IQR)L68(42–85),P64(44–83); baseline-FMA-adjusted mean difference−0.90,95%CI−3.78 to1.98,P=.54;estimand1 eTable2/eFigure4 Supplement3. Seven additional estimands,post hoc estimands and dichotomized-baseline subgroup analysis described similar to primary; links eTables2/3,eFigures4/7. Figure2 is descriptive dot/box display, not an adjusted-effect plot. |
| S019 | [p6, Secondary Outcomes PROMIS-29](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6) |Mean(SD) score L66(14),P65(14),points; adjusted mean difference−0.37,95%CI−3.34 to2.61. No aggregate-score range defined beyond domain range in p3. |
| S020 | [p6, PROMIS-10](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6) |Mean(SD)28(6) points both groups; adjusted mean difference0.18,95%CI−0.98 to1.33. |
| S021 | [p6, relevance of motor improvement](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6) |No improvement OR no relevant improvement: L51/276(18%),P52/270(19%). Counts/denominators are observed respondents; no effect estimate/CI/P printed. p5 says no missing-data imputation for this endpoint. |
| S022 | [p6, affected FMA upper](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6) |Mean(SD)39(19)points both groups; adjusted mean difference−0.73,95%CI−2.97 to1.50. |
| S023 | [p6, affected FMA lower](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6) |Mean(SD)23(7)points both groups; adjusted mean difference−0.13,95%CI−1.02 to0.77. |
| S024 | [p6, unaffected-side FMA total](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6) |Mean(SD)L90(10),P89(10)points; adjusted mean difference0.63,95%CI−0.72 to1.99. |
| S025 | [p6, NIHSS/Rivermead](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6) |NIHSS mean(SD)4(3)both groups; adjusted mean difference−0.14,95%CI−0.61 to0.33. Rivermead mean(SD)10(5)both groups; adjusted mean difference−0.33,95%CI−1.04 to0.37. These are distinct named endpoints retained together because printed consecutively; both require statistical pass coverage. |
| S026 | [p6, mRS](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6) |Ordinal logistic regression, adjusted odds ratio0.93,95%CI0.69–1.23 for L versus P; narrative describes odds of achieving better functional outcomes. Median(IQR)mRS3.0(2.0–4.0)both groups. p5 methods describe odds better or worse across categories. |
| S027 | [p6, 5-week FMA total](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6) |Mean(SD)L57(27),P56(26)points; adjusted mean difference0.02,95%CI−2.81 to2.84. All secondary-result details pointer eTable4 Supplement3. |
| S028 | [p7, Additional Post Hoc Analyses](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=7) |Nonlinear baseline-to3-month FMA association reported; did not impact primary treatment effect; no baseline-FMA×treatment interaction detected. Links eTables7/8,eFigures6/7 Supplement3. No P value or statistic printed here. |
| S029 | [p7, Discussion](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=7) |Neither motor-recovery benefit nor harm; adjusted3-month difference nonsignificant and<1 point on100-point scale; serious events/death similar; no secondary outcome difference; all additional estimands consistent with primary. These statements match S018–S028 and N062/N068–N112 for downstream narrative-to-result review; no quantitative claim supplied for unreported external-study comparisons. |
| S030 | [pp7–8, Conclusions](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=8) |Levodopa added to standardized rehabilitation did not significantly improve3-month motor function relative to placebo; results do not support adjunct use for motor recovery after acute stroke. Same claim abstract/Key Points, S002. |

## Cross-location and cross-document matching keys

- Primary result: N005/N008/S001/S018, p1 abstract, p2 Key Points, p5 Figure2B, p6 result, p7 Discussion and pp7–8 conclusion. Model/population keys: S009, survivor full analysis set N062–N064, baseline-adjusted treatment coefficient,3months±14days, affected FMA total0–100. Compare with Supplement3 estimand1 eTable2/eFigure4 and supplied SAP/protocol/code through support map; those documents were not read by this main mapper.
- Baseline: N003/N061 overall; N022–N059 group Table1; p5 Figure2A. Supplement3 eTable1 pointer. No overall median should be reconstructed by averaging group medians.
- Flow: N001/N002/N004/N060–N064; trial allocation, deaths, survivor population, imputed and observed components retained separately.
- Intervention and exposure: N002/N012–N014/N065/N066; distinguish nominal39-day trial treatment, phased dose, fixed timing, daily expectation and weekly adherence thresholds S010/S012.
- Secondary outcome status and scale: N016–N018/S006/S007/S014/S019–S027; compare endpoint,3-month vs5-week time, affected vs unaffected side, adjusted difference vs odds ratio, and observed-response denominators; Supplement3 eTable4. No reported secondary P values were inferred.
- Harms: N006/N019/N068–N112, p1/p6/p7; event counts versus affected participants; serious versus prespecified-interest sections; subtype hierarchy. Supplement3 eTables5/6/9 pointers.
- Additional analyses: S010–S013/S015–S018/S028;7additional predefined estimands,2post hoc estimands,post hoc dichotomization,center heterogeneity,spline and interaction analyses; status labels are preserved for protocol/SAP comparison.
- Sample size/randomization: N020/N021/S003/S005/S008; all supplied assumptions retained for independent reconstruction.

## Limitations of this map

No source-unit coverage gap remains. Exact individual plotted values, change-distribution summaries, per-secondary-outcome analysis denominators (other than relevance respondents), numerical spline/interaction tests, and statistical test statistics/standard errors are not printed in the main article; no values were invented. Supplement-specific values and PLAN–REPORT comparisons belong to the independent support map and checker stages. Current fresh source-confirmation derivatives use PyMuPDF1.26.4 CPU; reusable graphics retain their historical render engine provenance and were left unchanged.
