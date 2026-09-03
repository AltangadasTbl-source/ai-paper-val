# Main-Article Quantitative Evidence Map — DOC-001

Scope: `jama_engelter_2025_oi_250066_1761597796.45511.pdf`, PDF pages 1-10. This is an extraction and relationship inventory, not a candidate assessment. Native page text was used as a source-linked locator for all pages; the supplied rendered page images were visually checked for pp. 4-6 (Table 1, Figures 1-2, and Table 2). The direct PDF was queried with `pdftotext -layout -f 1 -l 10` to confirm source identity and page content. All locations below are direct-PDF locations.

## Page-completeness record

| PDF page | Mapped result-relevant content | Extraction disposition |
|---:|---|---|
| 1 | Abstract: trial population, allocation, intervention duration/dose, primary outcome scale, primary result, mortality/analysis total, and serious-event counts | MAPPED |
| 2 | Key Points repeat the primary outcome; background/design quantities and eligibility threshold are contextual quantitative definitions | MAPPED |
| 3 | Treatment schedule, outcome ranges/time points, randomization, sample-size calculation | MAPPED |
| 4 | Table 1 baseline counts/proportions/medians and analysis-model definitions | MAPPED; rendered table visually confirmed |
| 5 | Results participant flow, rehabilitation exposure, adherence, Figure 1 and Figure 2 labels/scales | MAPPED; rendered figures visually confirmed |
| 6 | Table 2 adverse-event counts; primary and secondary outcome estimates, intervals, and denominators | MAPPED; rendered table visually confirmed |
| 7 | Adverse-event totals and discussion restatement of primary-result direction/100-point scale | MAPPED |
| 8 | Conclusion restates the 3-month comparison; no new result-relevant numeric value | MAPPED — no new numeric relationship |
| 9 | Administrative text and references; no article-result numeric/statistical relationship | MAPPED — NO_APPLICABLE_RESULT_RELATIONSHIP |
| 10 | References only; no article-result numeric/statistical relationship | MAPPED — NO_APPLICABLE_RESULT_RELATIONSHIP |

## Numeric and reporting relationships

### MN001 — Trial allocation, intervention, and analysis population

- **Locations:** [PDF p.1](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=1); [PDF p.5](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5), Figure 1.
- **Population/time/contrast:** acute ischemic or hemorrhagic stroke with clinically meaningful hemiparesis; levodopa/carbidopa plus standardized rehabilitation versus placebo plus standardized rehabilitation; randomized through 3 months.
- **Printed values:** 610 randomized 1:1: levodopa/carbidopa 100 mg/25 mg, n=307; placebo, n=303; three times daily for 39 days. Figure 1 repeats 307 and 303.
- **Match key:** `randomized|all randomized|levodopa vs placebo|n=610|39 days`.

### MN002 — Abstract baseline summary and three-month eligibility

- **Location:** [PDF p.1](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=1), Abstract Results.
- **Printed values:** median (IQR) age 73 (64-82) years; 252/610 (41.3%) female; median baseline FMA total 34 (14-54); 28 deaths by 3 months; 582/610 (95.4%) eligible for primary analysis.
- **Measure/scale:** FMA total range 0-100 points; fewer points indicate worse motor function.
- **Match key:** `all randomized|baseline summary|3-month survival eligibility`.

### MN003 — Primary descriptive outcome repeated in abstract, Key Points, and results

- **Locations:** [PDF p.1](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=1), Abstract; [PDF p.2](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=2), Key Points; [PDF p.6](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6), Primary Outcome.
- **Population/time/contrast:** primary-analysis survivors at 3 months; levodopa versus placebo.
- **Printed values:** median (IQR) FMA total 68 (42-85) points versus 64 (44-83) points.
- **Measure/direction:** FMA 0-100, higher is better motor function; medians are descriptive and distinct from adjusted mean difference.
- **Match key:** `primary FMA total|3 months|survivors|levodopa-placebo`.

### MN004 — Mortality and participant-flow accounting

- **Locations:** [PDF p.5](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5), Results and Figure 1; abstract p.1.
- **Printed values:** 28/610 (4.6%) died: 11/307 (3.6%) levodopa and 17/303 (5.6%) placebo; survivors eligible for primary analysis: 296 and 286, total 582/610 (95.4%). Figure 1: levodopa 282 complete cases, 14 imputed (7 withdrew and 7 incomplete 3-month FMA); placebo 269 complete cases, 17 imputed (13 incomplete 3-month FMA and 4 withdrew).
- **Match key:** `flow|death before 3-month visit|primary analysis|treatment arm`.

### MN005 — Rehabilitation exposure and adherence

- **Location:** [PDF p.5](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5), Results.
- **Printed values:** levodopa mean (SD) 79 (35) therapy sessions, 45 (23) hours total, 47 (22) motor-learning sessions; placebo 77 (37), 44 (23), and 47 (23), respectively. Medication adherence >=80%: levodopa 252/307 (82.1%), placebo 244/303 (80.5%).
- **Match key:** `rehabilitation exposure/adherence|randomized treatment arm`.

### MN006 — Table 1 baseline demographic and clinical characteristics

- **Location:** [PDF p.4](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4), Table 1, visually confirmed.
- **Population/columns:** randomized levodopa n=307; placebo n=303. Values are No. (%) except stated medians (IQR). Multiple affected-vessel territories may apply per participant.
- **Printed paired values (levodopa; placebo):** age 72 (62-81); 74 (64-84) years; age >=80 years 90 (29.3); 112 (37.0). Female 119 (38.8); 133 (43.9); male 188 (61.2); 170 (56.1). Prior mRS median 0; 0. Hypertension 222 (72.3); 213 (70.3); hyperlipidemia 139 (45.3); 152 (50.2); diabetes 80 (26.1); 64 (21.1); atrial fibrillation 34 (11.1); 61 (20.1); smoking 68 (22.1); 59 (19.5); coronary heart disease 52 (16.9); 47 (15.5); depression 23 (7.5); 18 (5.9); dementia 11 (3.6); 9 (3.0); movement disorder 6 (2.0); 5 (1.7). Prior ischemic stroke 39 (12.7); 43 (14.2); prior hemorrhagic stroke 5 (1.6); 6 (2.0). Home 302 (98.4); 294 (97.0); nursing home 4 (1.3); 5 (1.7); other living situation 1 (0.3); 4 (1.3). Index ischemic stroke 260 (84.7); 259 (85.5); hemorrhagic stroke 47 (15.3); 44 (14.5). Anterior cerebral artery 37 (12.1); 31 (10.2); middle cerebral artery 230 (74.9); 230 (75.9); posterior cerebral artery 27 (8.8); 33 (10.9); vertebrobasilar/infratentorial 63 (20.5); 45 (14.9).
- **Match key:** `Table 1|baseline|randomized group|No (%)`.

### MN007 — Table 1 baseline severity, mRS distribution, and time

- **Location:** [PDF p.4](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4), Table 1, visually confirmed.
- **Printed paired values (levodopa; placebo):** affected-side FMA total median (IQR) 35.0 (14.8-55.3); 33.0 (13.0-52.8); FMA upper extremity 20.0 (6.0-35.0); 17.5 (6.0-34.0); FMA lower extremity 15.0 (6.0-21.0); 14.0 (7.0-21.0); NIHSS 7 (5-11); 8 (5-10). mRS categories 0: 2 (0.7); 0; 1: 0; 2 (0.7); 2: 6 (2.0); 3 (1.0); 3: 37 (12.1); 32 (10.6); 4: 170 (55.4); 169 (55.8); 5: 92 (30.0); 97 (32.0). Time stroke onset to randomization, median (IQR), days: 3.0 (2.0-5.0); 3.0 (2.0-5.0).
- **Definitions:** FMA total 0-100 (upper maximum 66; lower maximum 34), higher better; NIHSS 0-42 higher deficit; mRS 0-6 higher disability.
- **Match key:** `Table 1|baseline severity|mRS|FMA|NIHSS|time to randomization`.

### MN008 — Primary-outcome scale, timing, and planned sample size

- **Location:** [PDF p.3](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=3), Outcomes and Sample Size Estimation.
- **Printed values:** primary FMA total at 3 months +/-14 days after randomization; 50 items scored 0/1/2; total range 0-100, upper 66/lower 34. Assumed SD 25 points; calculated n=548 gives 80% power at two-sided alpha=.05 to detect a 6-point difference; planned enrollment n=610 for anticipated 10% dropout (at least 549 available for analysis).
- **Match key:** `primary outcome|FMA total|3 months|sample size`.

### MN009 — Outcome definitions and scales

- **Location:** [PDF p.3](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=3), Secondary Outcomes.
- **Printed definitions:** PROMIS-29 seven domains x four items, raw domain range 4-20; PROMIS-10 raw range 10-50; FMA upper/lower and unaffected-side total; NIHSS 0-42; mRS 0-6; Rivermead Mobility Index 0-15; each listed as 3-month outcome, plus FMA total at 5 weeks. Higher direction is explicitly stated as better only for PROMIS-10, FMA, and Rivermead; higher NIHSS/mRS is worse; PROMIS-29 varies by domain.
- **Match key:** `secondary outcome|scale definition|3 months/5 weeks`.

### MN010 — Serious adverse-event overall totals and treatment comparison

- **Locations:** [PDF p.1](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=1), abstract; [PDF p.6](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6), Table 2 and Adverse Events; [PDF p.7](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=7), Adverse Events.
- **Printed values:** 255 serious adverse events in 177/610 participants; 126 levodopa and 129 placebo. Most common serious adverse event infection: 55 versus 44. Prespecified adverse events of interest: 146 events in 115/610 participants, 79 levodopa and 67 placebo.
- **Measure:** events are counts; Table 2 headers use event totals n=126 and n=129, not participant denominators.
- **Match key:** `serious adverse events|event count|treatment arm`.

### MN011 — Table 2 serious adverse-event classifications

- **Location:** [PDF p.6](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6), Table 2, visually confirmed.
- **Printed paired event counts (levodopa; placebo):** infection 55;44 (pulmonary 27;17, urinary tract 15;15, abdominal 5;7, meningoencephalitis/encephalitis 0;2, unspecified 1;2, other infection 11;9); stroke 16;19 (ischemic 15;18, hemorrhagic 1;1); major extracranial bleeding 5;10; cardiac event 12;3 (acute coronary syndrome 5;1, heart failure 5;2, arrhythmia 2;0); cancer/malignant neoplasm 4;7; trauma 4;5 (fall 4;5); kidney failure 6;2; epileptic seizure 3;6; deep vein thrombosis/pulmonary embolism 3;4; electrolyte disorder 2;2; fracture 1;3; traumatic intracerebral hemorrhage 0;0; other/none above 32;34.
- **Match key:** `Table 2|serious adverse event classification|event count|treatment arm`.

### MN012 — Table 2 prespecified adverse events of interest

- **Location:** [PDF p.6](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6), Table 2, visually confirmed.
- **Printed paired event counts (levodopa; placebo):** confusion 12;9; nausea 11;7; postural hypotension syncope 10;4; hallucinations 3;10; depression 6;9; vomiting 8;5; arrhythmias 5;3; dizziness 4;4; fatigue 4;2; abnormal dreams 1;3; anxiety 3;3; insomnia 1;4; dry mouth 3;2; dyskinesia 3;1; taste disturbances 3;0; drowsiness including sudden onset of sleep 1;0; psychoses 1;1.
- **Footnote:** possibly related to levodopa according to prior research; medical-chart review and patient self-report during study visits.
- **Match key:** `Table 2|prespecified adverse event of interest|event count|treatment arm`.

### MN013 — Secondary descriptive outcomes at 3 months

- **Location:** [PDF p.6](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6), Secondary Outcomes.
- **Printed values:** PROMIS-29 mean (SD) 66 (14) vs 65 (14); PROMIS-10 28 (6) vs 28 (6); no improvement/no relevant improvement 51/276 (18%) vs 52/270 (19%); FMA upper 39 (19) vs 39 (19); FMA lower 23 (7) vs 23 (7); unaffected-side FMA total 90 (10) vs 89 (10); NIHSS 4 (3) vs 4 (3); Rivermead 10 (5) vs 10 (5); mRS median (IQR) 3.0 (2.0-4.0) both groups.
- **Order:** levodopa; placebo. **Match key:** `secondary outcomes|3 months|levodopa-placebo`.

### MN014 — Five-week FMA secondary outcome

- **Location:** [PDF p.6](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6), Secondary Outcomes.
- **Printed values:** FMA total mean (SD) at 5 weeks 57 (27) levodopa and 56 (26) placebo points.
- **Match key:** `FMA total|5 weeks|secondary outcome|levodopa-placebo`.

### MN015 — Narrative interpretation and conclusion cross-reference

- **Locations:** [PDF p.7](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=7), Discussion; [PDF p.8](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=8), Conclusions; p.1 abstract.
- **Printed narrative claims:** adjusted 3-month FMA difference was not statistically significant and less than 1 point on a 100-point scale; frequency of serious adverse events or death was similar in both groups; levodopa did not significantly improve motor function at 3 months.
- **Match key:** `primary conclusion|FMA 3 months|levodopa-placebo`.

## Cross-source match inventory

| Match family | Occurrences to compare later | Exact key |
|---|---|---|
| Allocation | Abstract p.1; Results/Figure 1 p.5 | 610, 307, 303 |
| Death/primary-analysis eligibility | Abstract p.1; Results/Figure 1 p.5 | 28; 582; 95.4%; 296/286 |
| Primary descriptive FMA | Abstract p.1; Key Points p.2; Results p.6; Figure 2 p.5 scale/plot | medians 68 vs 64; 3 months |
| Primary adjusted effect | Abstract p.1; Results p.6; Discussion p.7 | FMA, adjusted baseline, levodopa-placebo |
| Serious-event totals/infection | Abstract p.1; Table 2/Results p.6; narrative p.7 | 126/129; infection 55/44 |
| Conclusions | Abstract p.1; Discussion p.7; Conclusions p.8 | no significant 3-month motor benefit |

## Mapping limitations

No scientific-coverage gap within DOC-001. Native text was adequate on every page. Visual confirmation was required and completed for the table/figure pages 4-6. Figure 2 provides plotted distributions and a scale but does not print additional point estimates beyond the narrative primary result; it is retained as a matching visual occurrence.
