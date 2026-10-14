# PLAN evidence mapping: DOC-002 physical PDF pages 33–64

Scope: exactly 32 physical PDF pages of `joi250116supp1_prod_1771885794.26255.pdf`; 22 reusable-backed pages (33–54), 10 fresh-required pages (55–64). All 32 pages were opened and visually inspected. Document role: PLAN throughout, including historical-study background bound into the protocol. Protocol footer pp33–62: Version 1.0, 4 December 2020, printed page equals physical PDF page. PDF p63 starts Statistical Analysis Plan Version 2.0, 18 May 2024 (printed SAP p1); PDF p64 is SAP p2.

The PROVIDE final study report at pp35–53 is a historical appendix, not the current ImmunoSep trial's results or analysis plan. Its sample size, interventions, outcomes, counts, tables, and figures must not be aligned to current-trial report values as if they represented the same trial. It is retained below as complete contextual mapping. Only an explicit adoption elsewhere in the current protocol could make a historical input a current prospective design comparator. No findings or candidate diagnoses are made in this mapping.

## Derivative provenance and readable coverage

Reusable images at `.ai_paper_validation/review_1_5_1/preprocessing/DOC-002/pp033_064/`: `render-33.png` through `render-42.png`, `thumb-43.jpg` through `thumb-45.jpg`, `direct_46.png` through `direct_48.png`, `hi_49.png` through `hi_54.png`. These are retained PDF renders; engine/version undocumented in their files. Visual reading used the full page images, including figure/table panels. Native/layout bulk text is glyph-corrupted and was not treated as readable authority.

New derivatives all use the supplied fallback helper, PyMuPDF 1.26.4, CPU rendering/text extraction, with no new OCR:

| Source key | New derivative | Engine / device / parameters | Fitness |
|---|---|---|---|
| DOC-002 PDF p55 | preprocessing/plan2/page-55.png | PyMuPDF 1.26.4 / CPU / 200 dpi | Readable full page; visually mapped |
| DOC-002 PDF p56 | preprocessing/plan2/page-56.png | PyMuPDF 1.26.4 / CPU / 200 dpi | Readable full page; visually mapped |
| DOC-002 PDF p57 | preprocessing/plan2/page-57.png | PyMuPDF 1.26.4 / CPU / 200 dpi | Readable full page; visually mapped |
| DOC-002 PDF p58 | preprocessing/plan2/page-58.png | PyMuPDF 1.26.4 / CPU / 200 dpi | Readable full page; visually mapped |
| DOC-002 PDF p59 | preprocessing/plan2/page-59.png | PyMuPDF 1.26.4 / CPU / 200 dpi | Readable full page; visually mapped |
| DOC-002 PDF p60 | preprocessing/plan2/page-60.png | PyMuPDF 1.26.4 / CPU / 200 dpi | Readable full page; visually mapped |
| DOC-002 PDF p61 | preprocessing/plan2/page-61.png | PyMuPDF 1.26.4 / CPU / 200 dpi | Readable full page; visually mapped |
| DOC-002 PDF p62 | preprocessing/plan2/page-62.png | PyMuPDF 1.26.4 / CPU / 200 dpi | Readable full page; visually mapped |
| DOC-002 PDF p63 | preprocessing/plan2/page-63.png | PyMuPDF 1.26.4 / CPU / 200 dpi | Readable full page; visually mapped |
| DOC-002 PDF p64 | preprocessing/plan2/page-64.png | PyMuPDF 1.26.4 / CPU / 200 dpi | Readable full page; visually mapped |
| DOC-002 PDF pp55–64 | preprocessing/plan2/native-55-64.txt | PyMuPDF 1.26.4 / CPU / native text | Glyph-corrupted; locator only, not scientific transcription |
| DOC-002 PDF pp55–64 | preprocessing/plan2/layout-55-64.txt | PyMuPDF 1.26.4 / CPU / sorted reading order | Glyph-corrupted; locator only, not scientific transcription |

Commands: `.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py render joi250116supp1_prod_1771885794.26255.pdf --page N .ai_paper_validation/review_1_6_2/preprocessing/plan2/page-N.png --dpi 200` for each N=55…64; helper `text` commands used `--first 55 --last 64`, with `--layout` for the second text derivative. All source evidence links below point to the exact direct PDF, not the derivative. Source and reused assets were untouched.

## Complete page map

| Local evidence ID | PDF page | Content | Current ImmunoSep relationship / applicability | Coverage |
|---|---:|---|---|---|
| P2-001 | 33 | Protocol references1–10 | No applicable prospective result; bibliographic background | COMPLETE, reusable visual |
| P2-002 | 34 | Protocol references11–14 | No applicable prospective result; bibliographic background | COMPLETE, reusable visual |
| P2-003 | 35 | AppendixI PROVIDE final-report cover | Historical study identity, not current result | COMPLETE, reusable visual |
| P2-004 | 36 | PROVIDE introduction | Historical rationale and classification, not current result | COMPLETE, reusable visual |
| P2-005 | 37 | PROVIDE methods | Historical population and measurement methods | COMPLETE, reusable visual |
| P2-006 | 38 | PROVIDE classification and interventions | Historical thresholds/doses, context for current design only | COMPLETE, reusable visual |
| P2-007 | 39 | PROVIDE endpoints/power/analysis/results | Historical sample-size278 and endpoints, not ImmunoSep plan | COMPLETE, reusable visual |
| P2-008 | 40 | PROVIDE classification results | Historical counts and mortality, not current results | COMPLETE, reusable visual |
| P2-009 | 41 | PROVIDE clinical-stage results | Historical randomization36 and mortality, not current results | COMPLETE, reusable visual |
| P2-010 | 42 | PROVIDE discussion | Historical rationale/duration, not current results | COMPLETE, reusable visual |
| P2-011 | 43 | PROVIDE discussion/references1–5 | Historical interpretation, no current prospective numeric design | COMPLETE, reusable visual |
| P2-012 | 44 | PROVIDE references5–14 | No applicable current quantitative relationship | COMPLETE, reusable visual |
| P2-013 | 45 | PROVIDE references15–17 | No applicable current quantitative relationship | COMPLETE, reusable visual |
| P2-014 | 46 | PROVIDE Table1 | Historical descriptive/statistical table | COMPLETE, reusable visual |
| P2-015 | 47 | PROVIDE Table1 continuation | Historical descriptive/statistical table | COMPLETE, reusable visual |
| P2-016 | 48 | PROVIDE Table2 | Historical treatment-group table | COMPLETE, reusable visual |
| P2-017 | 49 | PROVIDE Table3 | Historical safety table | COMPLETE, reusable visual |
| P2-018 | 50 | PROVIDE Figure1 | Historical flow | COMPLETE, reusable visual |
| P2-019 | 51 | PROVIDE Figure2 | Historical classification development | COMPLETE, reusable visual |
| P2-020 | 52 | PROVIDE Figure3 | Historical mortality models | COMPLETE, reusable visual |
| P2-021 | 53 | PROVIDE Figure4 | Historical treatment results | COMPLETE, reusable visual |
| P2-022 | 54 | AppendixII study-site list | Administrative; no primary analysis/decision rule | COMPLETE, reusable visual |
| P2-023 | 55 | AppendixII study-site continuation | Administrative; no primary analysis/decision rule | COMPLETE, fresh visual |
| P2-024 | 56 | Monitor/pharmacovigilance contacts | Administrative; no applicable relationship | COMPLETE, fresh visual |
| P2-025 | 57 | AppendixIII eligible infection/resolution definitions | Current population eligibility and exploratory endpoint definition | COMPLETE, fresh visual |
| P2-026 | 58 | AppendixIII VAP definition/resolution | Current population eligibility and exploratory endpoint definition | COMPLETE, fresh visual |
| P2-027 | 59 | AppendixIV CPIS | Current infection eligibility score algorithm | COMPLETE, fresh visual |
| P2-028 | 60 | AppendixV SOFA | Current primary endpoint score algorithm | COMPLETE, fresh visual |
| P2-029 | 61 | AppendixVI immunotests | Current immune phenotype/randomization algorithm | COMPLETE, fresh visual |
| P2-030 | 62 | AppendixVII visit schedule | Current drug duration/measurement windows | COMPLETE, fresh visual |
| P2-031 | 63 | SAPV2.0 cover | Current plan version/date identity | COMPLETE, fresh visual |
| P2-032 | 64 | SAP abbreviations | Current statistical definitions (ITT,OR,CI,SD,TEAE) | COMPLETE, fresh visual |

## Prospective ImmunoSep design evidence

### P2-025 — Infection and resolution definitions

[Direct PLAN PDF p57](../../../joi250116supp1_prod_1771885794.26255.pdf#page=57), AppendixIII. Eligibility requires criteria1–3: all of criterion1, at least2 listed items from criterion2, at least1 listed item from criterion3. Primary bacteremia has no criterion2 or3; criterion1 is at least1 positive blood culture plus inability to identify a primary infection site despite clinical/radiology investigation; resolution is sterile blood cultures after7days.

Community-acquired pneumonia: new chest X-ray infiltrate; criterion2 lists new/worsening cough, dyspnea, auscultatory findings compatible with pulmonary consolidation; criterion3 lists procalcitonin ≥0.25ng/mL, hypoxemia (partial oxygen pressure ≤60mmHg or saturation ≤90% in ambient air), respiratory rate ≥20breaths/min. Resolution requires none of the criterion2 findings that made the patient eligible AND none of criterion3 findings that made the patient eligible.

Hospital-acquired pneumonia: onset >48hours after hospital admission plus new/evolving chest X-ray infiltrate; criterion2 lists new/worsening cough or dyspnea, purulent tracheobronchial secretions, auscultatory findings compatible with pulmonary consolidation (last text continues p58). Criterion3 and resolution conditions as for community-acquired pneumonia.

Matching main-paper keys: qualifying infection type, infection-resolution endpoint, endpoint status (table expressly calls resolution criteria exploratory study endpoint), resolution window. No current dose/model/covariate/power/multiplicity statement appears on this page.

### P2-026 — Ventilator-associated pneumonia

[Direct PLAN PDF p58](../../../joi250116supp1_prod_1771885794.26255.pdf#page=58), AppendixIII continuation. Criterion1: onset >48hours from start of mechanical ventilation AND new/evolving chest X-ray infiltrate. Criterion2: purulent tracheobronchial secretions and auscultatory findings compatible with pulmonary consolidation. Criterion3: procalcitonin ≥0.25ng/mL or Clinical Pulmonary Infection Score (CPIS) ≥6. The printed cross-reference says AppendixII below; actual CPIS table is AppendixIV at p59. Resolution requires none of criterion2 findings that made eligibility AND none of criterion3 findings that made eligibility. No current primary inferential specification appears here.

Matching keys: VAP eligibility, CPIS≥6, infection-resolution components/status. The appendix pointer is retained as a locator detail, without diagnosis.

### P2-027 — CPIS scoring table

[Direct PLAN PDF p59](../../../joi250116supp1_prod_1771885794.26255.pdf#page=59), AppendixIV. Six variables, each0–2points; CPIS is sum of each variable score. Transcription preserves printed logical operators; no normalization to external criteria.

| Variable / unit | 0points | 1point | 2points |
|---|---|---|---|
| Tracheal secretions | Rare | Abundant | Purulent |
| Leukocyte count (/mm³) | >4000 AND <11000 | <4000 AND >11000 | <4000 OR >11000 + band forms |
| Temperature (°C) | >36.5 AND <38.4 | >38.5 AND <38.9 | >39 OR <36 |
| pO₂/FiO₂ ratio (mmHg) | >240 OR ARDS | dash | ≤240 AND no ARDS |
| Chest radiograph | No infiltrate | Diffuse infiltrate | Localised infiltrate |
| Culture of tracheal aspirate | Negative | dash | Positive |

Footnote: ARDS=acute respiratory distress syndrome. Matching keys: CPIS algorithm and VAP eligibility from P2-026; these are population-defining operational scoring elements. No numeric inference/test result or power statement.

### P2-028 — SOFA scoring table

[Direct PLAN PDF p60](../../../joi250116supp1_prod_1771885794.26255.pdf#page=60), AppendixV. Six variables each0–4points; SOFA is the sum. Preserve source units/operators as printed.

| Variable / printed unit | 0points | 1point | 2points | 3points | 4points |
|---|---|---|---|---|---|
| PaO₂/FiO₂ (mmHg) | ≥400 | <400 | <300 | <200 | <100 |
| Platelets (per mm³) | ≥150 | <150 | <100 | <50 | <20 |
| Hypotension | MAP≥70mmHg | MAP<70mmHg | Dobutamine whatever dose | Adrenaline≤0.1 or noradrenaline≤0.1 | Adrenaline>0.1 or noradrenaline>0.1 |
| Glasgow Coma Scale | 15 | 13–14 | 10–12 | 6–9 | <6 |
| Bilirubin (mg/dL) | <1.2 | 1.2–1.9 | 2.0–5.9 | 6.0–11.9 | ≥12 |
| Creatinine (mg/dL) or urine output | <1.2 | 1.2–1.9 | 2.0–3.4 | 3.5–4.9 or <500mL/day | ≥5.0 or <200mL/day |

Vasopressor footnote: µg/kg/min. The printed table contains no respiratory-support qualification alongside the respiratory bins. This is a literal table map, not a proposed interpretation. Matching keys: total SOFA, component scores, change in SOFA, primary endpoint definition. No interval/P/test or missing-data rule appears on this page.

### P2-029 — Immunotests guiding randomization

[Direct PLAN PDF p61](../../../joi250116supp1_prod_1771885794.26255.pdf#page=61), AppendixVI. Every patient screened at2serial time points on2consecutive days. Four possible ferritin/HLA-DR combinations:

| Ferritin | HLA-DR | Printed classification |
|---|---|---|
| >4420ng/mL | ≥5000AB/C | Fulminant hyper-inflammation |
| >4420ng/mL | <5000AB/C | Fulminant hyper-inflammation |
| ≤4420ng/mL | ≥5000AB/C | Unclassified |
| ≤4420ng/mL | <5000AB/C | Sepsis-associated immunoparalysis |

Header labels HLA-DR `(AB/CD14-cell)`; legend gives `<5000 AB/C` and `≥5000 AB/C`. Text states four combinations and that only some combinations may allow enrollment; it does not add numerical dose, analysis-model, stopping, or multiplicity criteria. Matching keys: immune phenotype strata, ferritin4420, HLA-DR5000, treatment allocation algorithm, analysis-population eligibility. A reader should use current protocol/SAP statements for trial inclusion rather than historical PROVIDE30% threshold.

### P2-030 — Study-visit schedule

[Direct PLAN PDF p62](../../../joi250116supp1_prod_1771885794.26255.pdf#page=62), AppendixVII. Columns: day0, each day1–15, day21, day28, day90.

| Procedure | Marked days |
|---|---|
| Obtain informed consent | 0 |
| Study drug | 1–15, every day |
| SOFA score | 1–15, every day;21 |
| Medical history | 1 |
| Clinical state of infection | 6–15, every day;21 |
| Survival | 28;90 |
| Vital signs | 1–15, every day;21 |
| Laboratory tests | 1–15, every day;21 |
| Microbiology | 1–15, every day;21 |
| Blood collection | 1;2;4;7;15;21;28;90 |
| Microbiome samples | 1;2;4;7;15;21;28;90 |
| Co-administered medication | 1–15, every day;21 |
| Adverse events | 2–15, every day;21;28;90 |

Matching keys: current randomized-intervention15day duration; SOFA measurement window/day21; infection assessment days6–21; mortality days28/90; longitudinal sampling days. No dose amounts, imputation, model/covariate, sensitivity/subgroup, power, multiplicity, interim, or stopping specification appears in this schedule.

### P2-031 and P2-032 — SAP identity and definitions

[Direct PLAN PDF p63](../../../joi250116supp1_prod_1771885794.26255.pdf#page=63): ImmunoSep Statistical Analysis Plan, Version2.0, 18May2024, EudraCT2020-005768-74. Authors listed: Frank Bloos, Konstantina Dakou, EvangelosJ.Giamarellos-Bourboulis, Miltiades Kyprianou, Alexander Vlaar. Cover has no numerical prospective analysis rule.

[Direct PLAN PDF p64](../../../joi250116supp1_prod_1771885794.26255.pdf#page=64): abbreviations include ITT=intent-to-treat; OR=odds ratio; CI=confidence interval; SD=standard deviation; ROC=receiver operator characteristics; TEAE=treatment-emergent adverse events; SOFA=sequential organ failure assessment; MALS=macrophage activation-like syndrome. APACHE,CCI,HISS,AE,RCT,VAP also expanded. No additional definition of analysis inclusion/denominator, test, effect estimation, or hypothesis appears on glossary page. Matching keys: SAPV2.0 date/version, OR effect-measure label, ITT population, TEAE safety outcome. Inferential content continues outside this shard at physical pp65–72.

## Historical PROVIDE appendix, fully distinguished from prospective ImmunoSep

### P2-001 through P2-004 — Introductory and bibliographic units

[PDF p33](../../../joi250116supp1_prod_1771885794.26255.pdf#page=33) and [p34](../../../joi250116supp1_prod_1771885794.26255.pdf#page=34): protocol references, no applicable prospective quantity. Citation years, journal volumes/pages, and reference numbering are bibliographic, not endpoint counts.

[PDF p35](../../../joi250116supp1_prod_1771885794.26255.pdf#page=35): AppendixI final PROVIDE report cover, EudraCT2017-002171-26; no current endpoint quantity. [PDF p36](../../../joi250116supp1_prod_1771885794.26255.pdf#page=36): PROVIDE introduction, historical rationale states3–4% hyper-inflammation associated with first10days mortality; classification objectives MALS, immunosuppression, unclassified; anakinra/rhIFNγ respectively targeted MALS/immunoparalysis. These are historical/contextual statements.

### P2-005 through P2-009 — PROVIDE narrative methods/results

[PDF p37](../../../joi250116supp1_prod_1771885794.26255.pdf#page=37): PROVIDE double-blind/double-dummy, November2017–December2019,14Greek sites (9ICUs,5internal medicine). Age≥18; sepsis SOFA≥2 for new admission or increase≥2 for hospitalized; septic shock MAP<65mmHg despite fluids with lactate>2mmol/L needing vasopressors. Chronic prednisone exclusion≥0.4mg/kg/day for>15days.28day daily observation. Blood10mL within24h(day1), repeated24h later(day2); ferritin assay lower limit75ng/mL. Historical eligible infection sources: CAP/HAP/VAP/primary bacteremia/acute cholangitis.

[PDF p38](../../../joi250116supp1_prod_1771885794.26255.pdf#page=38): ferritin>4420ng/mL both samples or day2 regardless flow cytometry=MALS; immunoparalysis HLA-DR/CD14/CD45<30% both days or day2, conditional ferritin≤4420ng/mL; otherwise intermediate. HLA-DR expressed as percentage and molecules/cell. PBMC final volume200µL, density2.5×10^6/mL; LPS10ng/mL, PHA5µg/mL;48h culture37°C,5%CO₂; TNFα in duplicate, limit20pg/mL. Septic-shock MALS/immunoparalysis eligible intervention stage. MALS: anakinra200mg IV in20mL q8h for7days plus0.5mL0.9%NaCl SC q48h for15days. Immunoparalysis:20mL0.9%NaCl IV q8h7days plus rhIFNγ100µg in0.5mL SC q48h15days. Placebo saline IV/SC matched.

[PDF p39](../../../joi250116supp1_prod_1771885794.26255.pdf#page=39): anakinra100mg q8h if creatinine clearance<30mL/min; daily adverse events. Observation endpoint immune classification versus28day outcome; intervention primary28day mortality; secondary90day mortality/secondary infections/appropriateness of immune classification using entire screened cohort; exploratory SOFA change among survivors end of treatment. Historical power: MALS mortality60%→35%, immunoparalysis50%→35%, sample278,80%power,10%significance. Qualitative percentages/95%CIs/Fisher exact; quantitative mean±SD orSE/Student t or Mann–Whitney; ROC/Youden; multivariate stepwise Cox described with RR95%CI; P<.05. Result cohort240: MALS44/177(24.9%) septic shock versus4/63(6.3%) without shock,P=.001.

[PDF p40](../../../joi250116supp1_prod_1771885794.26255.pdf#page=40): only2 patients fulfilled original30% immunoparalysis cutoff; ROC suggests<5000HLA-DR/monocyte predicts28day mortality; patients<5000 had reduced PBMC TNFα. Intermediate subgroup89:21(23.6%) ferritin1000–4420ng/mL;23(25.9%) HLA-DR5000–8000. Revised cohort240: MALS48(20.0%), immunoparalysis103(42.9%), intermediate89(37.1%); classification repeatability88.5%. MALS28day mortality79.1%,95%CI65.7–88.3%.

[PDF p41](../../../joi250116supp1_prod_1771885794.26255.pdf#page=41): immunoparalysis mortality66.9%,95%CI56.4–74.4%; intermediate41.6%,CI31.9–51.9%. Adjusted HR immunoparalysis versus intermediate1.79(1.19–2.68); MALS versus intermediate2.39(1.49–3.84). Randomized36=immunotherapy15+placebo21; first2Dec2017,last1Dec2019; prematurely stopped slow enrollment December2019.1immunoparalysis per arm; rest MALS.28day deaths placebo18,85.7%(65.4–95.1%); immunotherapy14,93.3%(70.2–98.8%);90day mortality same. Exploratory day7alive/no baseline SOFA increase: placebo5(25%) versus anakinra64.3%; ALT/INR improved day7. No adverse-event incidence difference stated.

### P2-010 through P2-013 — PROVIDE discussion and references

[PDF p42](../../../joi250116supp1_prod_1771885794.26255.pdf#page=42): historical discussion cites other study30% reduction in28day mortality and28day anakinra versus PROVIDE7day duration; immunoparalysis43%; historical rhIFNγ series9patients,9reversed phenotype,8clinical resolution;6healthy-volunteer endotoxemia study. [PDF p43](../../../joi250116supp1_prod_1771885794.26255.pdf#page=43): PROVIDE7day anakinra interpretation, no new current prospective design, followed references1–5. [PDF p44](../../../joi250116supp1_prod_1771885794.26255.pdf#page=44): references5–14 only. [PDF p45](../../../joi250116supp1_prod_1771885794.26255.pdf#page=45): references15–17 only. These pages explicitly have no applicable current-trial inferential quantity.

### P2-014 and P2-015 — Historical PROVIDE Table1

[PDF p46](../../../joi250116supp1_prod_1771885794.26255.pdf#page=46) and [p47](../../../joi250116supp1_prod_1771885794.26255.pdf#page=47). Column order intermediateN89 / immunoparalysisN103 / MALSN48. Counts(%) or mean±SD as printed. P denotes table comparison, not current ImmunoSep.

| Row | Intermediate | Immunoparalysis | MALS | P |
|---|---|---|---|---|
| Age,y | 71.7±16.5 | 74.2±12.5 | 70.8±14.2 | .308* |
| Male | 50(56.2) | 63(61.2) | 29(60.4) | .767** |
| CCI | 4.8±2.3 | 5.2±2.4 | 4.9±2.3 | .398* |
| Septic shock | 55(61.8) | 78(75.7) | 44(91.7) | .001** |
| APACHEII | 21.1±8.7 | 24.9±8.5 | 29.5±9.2 | <.0001* |
| SOFA | 9.4±4.0 | 11.0±3.8 | 13.8±3.5 | <.0001* |
| CRP,mg/L | 108.4±105.7 | 108.6±102.1 | 96.8±104.8 | .843* |
| CAP | 40(44.9) | 45(43.7) | 19(39.6) | .740** |
| HAP | 21(23.5) | 21(20.4) | 12(25.0) | .407** |
| VAP | 8(9.0) | 15(14.6) | 5(10.4) | .465** |
| Primary bacteremia | 13(14.6) | 16(15.5) | 10(20.8) | .620** |
| Acute cholangitis | 7(7.9) | 6(5.8) | 2(4.2) | .676** |
| Gram-negative pathogens | 19(21.3) | 23(19.4) | 11(22.9) | .825** |
| E.coli | 1(1.1) | 1(0.9) | 1(2.1) | .840** |
| A.baumannii | 3(3.3) | 7(6.7) | 1(2.1) | .338** |
| K.pneumoniae | 5(5.6) | 2(1.9) | 4(8.4) | .182** |
| S.aureus | 2(2.2) | 6(5.8) | 2(4.2) | .465** |
| C.albicans | 4(4.5) | 2(1.9) | 2(4.2) | .578** |
| Type2diabetes | 27(30.7) | 27(26.2) | 16(33.3) | .639** |
| Chronic heart failure | 17(19.1) | 28(27.2) | 17(35.4) | .105** |
| Chronic renal disease | 9(10.1) | 12(11.7) | 5(10.4) | .938** |
| COPD | 21(23.6) | 25(24.3) | 12(25.0) | .983** |
| Piperacillin/tazobactam | 35(42.7) | 37(37.8) | 13(27.7) | .236** |
| Carbapenems | 25(30.5) | 34(34.3) | 21(44.7) | .261** |
| Tigecycline | 11(13.4) | 19(19.4) | 12(25.5) | .223** |
| Colistin,p47 | 25(30.5) | 34(34.3) | 25(53.2) | .029** |
| Vancomycin,p47 | 17(20.7) | 24(24.2) | 9(19.1) | .690** |

Footnotes p47: *=ANOVA,**=Pearson chi-square. Abbreviations APACHE,CCI,CRP,SD,SOFA expanded. These rows are historical plan background; no current-trial counterparts are assigned.

### P2-016 — Historical PROVIDE Table2

[PDF p48](../../../joi250116supp1_prod_1771885794.26255.pdf#page=48). Columns placeboN21 / immunotherapyN15.

| Row | Placebo | Immunotherapy | P |
|---|---|---|---|
| Age,y mean±SD | 69.7±10.8 | 70.6±15.1 | .838* |
| Male | 12(57.1) | 10(66.7) | .733** |
| CCI | 4.3±2.2 | 5.7±2.2 | .062* |
| APACHEII | 18.2±8.7 | 30.5±9.4 | .376* |
| SOFA | 14.5±2.8 | 14.3±3.1 | .843* |
| CAP | 10(47.6) | 2(13.3) | .040** |
| HAP | 6(28.6) | 8(58.3) | .175** |
| Ventilation-associated pneumonia | 3(14.3) | 3(20.0) | .677 |
| Other infection | 2(13.3) | 2(13.3) | 1.00 |
| Type2diabetes | 6(28.6) | 6(40.0) | .499** |
| Chronic heart failure | 4(19.0) | 8(53.3) | .071** |
| Chronic renal disease | 0(0) | 4(26.6) | .023** |
| COPD | 7(33.3) | 3(20.0) | .468** |
| Piperacillin/tazobactam | 3(14.3) | 2(13.3) | 1.00** |
| Carbapenems | 10(47.6) | 12(80.0) | .083* |
| Tigecycline | 6(28.6) | 3(20.0) | .705** |
| Colistin | 13(61.9) | 10(66.7) | 1.00* |
| Vancomycin | 3(14.3) | 4(26.7) | .418** |
| Antimicrobials per ESCMID | 18(85.7) | 12(80.0) | .677** |
| Hydrocortisone replacement | 19(90.5) | 10(80.0) | .639** |

Footnotes *=Student t;**=Fisher exact. Percentages, P values, and marks above preserve historical printed values rather than being recalculated or silently normalized.

### P2-017 — Historical PROVIDE Table3

[PDF p49](../../../joi250116supp1_prod_1771885794.26255.pdf#page=49). Columns placeboN21 / personalized immunotherapyN15. At least1SAE4(19.0)/4(16.7),P=.694. Ventricular tachycardia0(0)/2(13.3),P=.167; digital ischemia same; acute myocardial infarction1(4.8)/0(0),P=1.00; brain-tumor metastasis same; obstructive ileus same; pulmonary embolism same. At least1AE2(9.5)/0(0),P=.500. GradeIhyperkalemia1(4.8)/0(0),P=1.00; GradeIIIγGT increase same. Source header `p-value*`, row `SAE**`; printed footnotes `*this does not include the number of deaths`, `**by the Fisher exact test`. AE,γGT,SAE defined. Historical only.

### P2-018 — Historical PROVIDE Figure1

[PDF p50](../../../joi250116supp1_prod_1771885794.26255.pdf#page=50): initial273; excluded33=intra-abdominal infection24+missing clinical data3+withdrew consent2+corticosteroids2+lymphoma1+SLE1. Screened240=septic shock177+no shock63. Shock classification MALS44(24.8%),immunoparalysis2(1.1%),intermediate132(74.0%); no-shock MAS4(6.3%),immunoparalysis0(0%),intermediate59(93.7%). Excluded deceased before randomization10; randomized36=placebo21+immunotherapy15, all received intervention. Lost follow-up0both; early death termination18placebo/11immunotherapy. Analyzed21/15,analysis exclusions0/0. Caption states two-stage PROVIDE trial. No current-trial flow mapping.

### P2-019 — Historical PROVIDE Figure2

[PDF p51](../../../joi250116supp1_prod_1771885794.26255.pdf#page=51). Classification-development panels:

- A: percentage HLA-DR ROC AUCday1 .63(.50–.70),P=.065;day2 .59(.49–.70),P=.087.
- B: number HLA-DR/monocyte ROC AUCday1 .64(.53–.75),P=.015;day2 .65(.54–.75),P=.012.
- C: `<5000 HLA-DR/cell` death69,survival34,total103;sensitivity65.1%,PPV67.0%. `≥5000` death37,survival52,total89;specificity60.5%,NPV58.4%. Totals death106,survival86,N192. Printed RRdeath with<5000=2.82(1.58–5.14),P<.0001.
- D: TNFα pg/mL,mean±SE, intermediateN40 versus<5000N43;medium/LPS/PHA bars;LPS P=.005,PHA P=.025; bars show unnumbered means, so no exact value is inferred from bar height.
- E: immunoparalysisN103 versus MALSN48; platelets P=.013,aPTT P=.017,ALT P=.002,AST P<.0001. Bars are unnumbered; units displayed platelets/mm³,aPTTs,ALT/ASTU/L.

Caption defines ROC predictors at days1/2;28day mortality; intermediate=ferritin≤4420ng/mL AND HLA-DR≥5000/monocyte; LPS/PHA stimulation; coagulation/liver-function comparisons. AUC,NPV,PPV,CI,RR defined. All historical, not ImmunoSep analyses.

### P2-020 — Historical PROVIDE Figure3

[PDF p52](../../../joi250116supp1_prod_1771885794.26255.pdf#page=52). A: survival0–28days;total log-rank30.20,P<.0001; displayed pairwise log-rank14.53,P<.0001 and5.08,P=.024. B: Cox analysis table survivalN96,deathN144. Intermediate52(54.2)/37(25.7),referenceHR1. Immunoparalysis34(35.4)/69(47.9),univariateHR2.82(1.58–5.14),P<.0001;adjusted1.79(1.19–2.68),P=.005. MALS10(10.4)/38(26.4),univariateHR3.08(1.45–1.65) as visually printed, P=.003;adjusted2.39(1.49–3.84),P<.0001. APACHEII≥27:25(26.0)/69(47.9),HR2.18(1.57–3.02),P<.0001;adjusted1.48(.95–2.10),P=.024. SOFA≥8:60(62.5)/133(92.4),HR4.19(2.26–7.76),P<.0001;adjusted2.39(1.37–4.16),P=.002. Chronic heart failure17(17.7)/45(31.3),HR2.11(1.12–3.97),P=.024;adjustedNS. Septic shock54(56.3)/123(85.4),HR2.77(1.74–4.40),P<.0001;adjustedNS. Cutoffs starred as Youden index of mortality ROC. Caption calls HRs hazard ratios and estimates95%CIs. No candidate assessment is made; historical rows do not describe current-trial results or analysis.

### P2-021 — Historical PROVIDE Figure4

[PDF p53](../../../joi250116supp1_prod_1771885794.26255.pdf#page=53). A:28day survival curves placebo/immunotherapy,log-rank.199,P=.656. B:day7survival without SOFA increase,placeboN20 / immunotherapyN14,percent±95%CI,P=.035; bars correspond25%/64.3% narrative p41. C:ALTU/L day1/day7;placeboP=.886,immunotherapyP=.036;D:INR day1/day7;placeboP=.173,immunotherapyP=.043. No exact unnumbered bar means/limits inferred. Caption describes within-arm days1/7 comparisons. No current-trial counterpart.

### P2-022 through P2-024 — Administrative appendix

[PDF p54](../../../joi250116supp1_prod_1771885794.26255.pdf#page=54): AppendixII sites France(Lyon),Germany(Jena),Greek list begins (Athens/Larissa/Ioannina/Alexandroupolis). [PDF p55](../../../joi250116supp1_prod_1771885794.26255.pdf#page=55): Greek list continues (Thessaloniki/Piraeus/Larissa/Elefsis/Athens),Netherlands(Amsterdam/Nijmegen),Romania(Cluj-Napoca),Switzerland(Lausanne). Named sites/investigators are administrative, not statistical strata or sample-size allocations here. [PDF p56](../../../joi250116supp1_prod_1771885794.26255.pdf#page=56): monitor and pharmacovigilance contacts only. All3units were inspected, with no applicable outcome/model/power/stopping statement.

## Completion and matching boundaries

32/32 assigned pages mapped;22reusable+10fresh=32. Scientific coverage gaps: none. Readable full-page visual inspection replaces unusable text extraction. No OCR was required. Historical figure panels are mapped by their explicit numbers and labels; no graph-derived continuous measurement was fabricated. Numeric transcription is source-linked; source remains final authority for checker/recheck. No workbook/Office source assigned; formulas/cached workbook values not applicable.

Current-trial relationships in this shard: infection-resolution definitions/status, CPIS score/eligibility, SOFA score/primary-endpoint components, immune phenotype and randomization screening thresholds, treatment/measurement schedule, SAP identity and statistical abbreviations. Primary analysis model/covariates, power, missing data, sensitivity/subgroup, multiplicity/interim/stopping are absent from the prospective current-trial content on these32pages and belong to the other assigned protocol/SAP shards. Historical PROVIDE analysis statements are kept distinct and cannot fill those current-trial fields.
