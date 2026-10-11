# Main-paper quantitative evidence map

Scope: DOC-001, `jama_cooper_2018_oi_180132.pdf`, PDF pages 1–10 (journal pages 2211–2220). Document role: REPORT throughout. This is a source-linked extraction, without candidate diagnosis or disposition. Provisional numeric IDs M-N001–M-N062 and statistical IDs M-S001–M-S036 are for coordinator consolidation. A row can group the components of a single displayed relationship; all components remain explicit.

## Evidence basis and coverage

Read the complete QUALITY_CONTROL_SCOPE.md and workflow_1_6_1/review_contract.md, current source inventory, coverage ledger, DOC-001 evidence-asset rows and tooling record. Used only source-matched, unchanged reusable assets under `.ai_paper_validation/review_1_5_2/preprocessing/`: `native_text/DOC-001.txt`, `layout_text/DOC-001.txt`, and page PNGs. Native text is curator-confirmed byte-identical to direct-source Poppler pdftotext output. Layout text retains all labels although Figure 2 axis-line placement differs. Visual inspection of pages 1, 4, 5, 6, 7 and 8 established abstract/flow/table/figure alignment. The image engine is legacy renderer unrecorded, locally readable/source-matched, as recorded by curator; no new derivative or OCR was produced. Every page was read in text; figures/tables were also inspected visually. All ten pages are reusable-backed; zero fresh-required pages; zero scientific coverage gaps.

Links below are relative to this extraction artifact. H = hypothermia and C = normothermia throughout. The reference group for H/C risk ratios, odds ratios and hazard ratios is C unless specifically stated otherwise. Absolute differences in Table 2 are H minus C in percentage points. A dash in an extraction field means no numeric item printed there, not zero.

| PDF page | Journal page | Source position and mapped contents | Basis | Status |
|---|---:|---|---|---|
| 1 | 2211 | Abstract design, flow, baseline summary, exposure, primary result and two adverse-event rates | Native/layout plus page image | COMPLETE |
| 2 | 2212 | Key Points; background quantitative context; design; interim schedule; eligibility; follow-up; randomization begins | Native/layout | COMPLETE |
| 3 | 2213 | Randomization, intervention temperatures/durations/rewarming; endpoints; sample size and primary/sensitivity method begins | Native/layout | COMPLETE |
| 4 | 2214 | Figure 1 complete flow; statistical methods, subgroup/compliance definitions; baseline/process results | Native/layout plus page image | COMPLETE |
| 5 | 2215 | Table 1 all rows/footnotes; primary/secondary/additional outcomes; adverse events; per-protocol discussion begins | Native/layout plus page image | COMPLETE |
| 6 | 2216 | Figure 2 both panels, all contributing counts, axes and data definitions; per-protocol/as-treated pneumonia; subgroup/post hoc claims | Native/layout plus page image | COMPLETE |
| 7 | 2217 | Table 2 all results and footnotes; Figure 3 distribution and legend; post hoc conclusion; discussion | Native/layout plus page image | COMPLETE |
| 8 | 2218 | Discussion exposure summaries, adverse events and limitations; outcome conclusion; correction note | Native/layout plus page image | COMPLETE |
| 9 | 2219 | Article information, investigators, funding, references 1–19; no additional trial quantitative result | Native/layout, no-applicable result unit explicitly mapped | COMPLETE |
| 10 | 2220 | References 19–33; no additional trial quantitative result | Native/layout, no-applicable result unit explicitly mapped | COMPLETE |

## Numeric relationships: design, flow and exposure

| ID | Exact source location | Printed relationship and context | Matching locations / statistical link |
|---|---|---|---|
| M-N001 | [p1 abstract design/interventions](../../../jama_cooper_2018_oi_180132.pdf#page=1), [p4 Figure 1 and Patient Characteristics](../../../jama_cooper_2018_oi_180132.pdf#page=4) | 511 randomized; H 266; C 245. Out-of-hospital 231 and in-hospital 280 in Figure 1; text out-of-hospital 231 (45%). Figure caption says screened totals were not recorded. Initial run-in 8 patients without randomization excluded. | p2 Key Points 511 adults; p2 design planned 510; M-S024 sample-size specification |
| M-N002 | [p4 Figure 1](../../../jama_cooper_2018_oi_180132.pdf#page=4) | H primary outcome 240; no data available 16; consent withdrawn 6; lost to follow-up 4. C primary outcome 226; no data available 13; consent withdrawn 5; lost to follow-up 1. The three exclusion rows are separate printed lines. | p1 completed primary evaluation 466; p4 Results H240/C226; M-S001 |
| M-N003 | [p4 Figure 1 and Results](../../../jama_cooper_2018_oi_180132.pdf#page=4), [p5 Table 1 headings](../../../jama_cooper_2018_oi_180132.pdf#page=5) | Eleven consent withdrawals (H6/C5), leaving 500 evaluable/ongoing-consent participants. Baseline ITT population H260/C240. Six-month mortality population H256/C239. | p1 500 ongoing consent; M-S004 vs M-S005 populations |
| M-N004 | [p4 Patient Characteristics](../../../jama_cooper_2018_oi_180132.pdf#page=4) | Full trial protocol 293 participants: H132/C161 (eTable 8 pointer). | p5 per-protocol/as-treated text, M-S019–M-S021 |
| M-N005 | [p1 abstract Results](../../../jama_cooper_2018_oi_180132.pdf#page=1), [p4 Patient Characteristics](../../../jama_cooper_2018_oi_180132.pdf#page=4) | Abstract: mean age 34.5 y (SD13.4); 402 men (80.2%). Results: mean age34.5 (SD13.4); median GCS6 (IQR4–7); diffuse brain injury70.6%; injury-to-randomization median1.9 h (IQR1.0–2.7). | Table 1 grouped rows M-N015–M-N042 |
| M-N006 | [p1 Interventions](../../../jama_cooper_2018_oi_180132.pdf#page=1), [pp2–3 methods](../../../jama_cooper_2018_oi_180132.pdf#page=3) | H target33–35°C, at least72 h and up to7 d if intracranial pressure elevated; C37°C, both managed7 d. Induction up to2000 mL 4°C 0.9% saline; initial35°C then33°C after bleeding assessment. Maintenance33°C or35°C if bleeding concerns; general H target33±0.5°C, C37±0.5°C. | p8 discussion at least72 h; M-S026 intervention rules |
| M-N007 | [p3 Rewarming](../../../jama_cooper_2018_oi_180132.pdf#page=3) | At72 h assess ICP; <20 mm Hg allows controlled rewarming up to0.25°C/h; sustained >20 mm Hg prompts recooling/reassessment. Maximum hypothermia7 d; after reaching37°C maintain normothermia up to7 d after randomization. | p1 gradual rewarming; p8 discussion; M-S026 |
| M-N008 | [p4 Patient Characteristics](../../../jama_cooper_2018_oi_180132.pdf#page=4) | H initial35°C achieved by233 (89.6%); injury-to-target median2.5 h (IQR0.8–5.5). Final33°C achieved by186 (71.5%); median10.1 h (IQR6.8–15.9). Percentages appear in evaluable-H context260. | eTable2 pointer; p8 >10 h; M-N009/M-N010 |
| M-N009 | [p4 Patient Characteristics](../../../jama_cooper_2018_oi_180132.pdf#page=4) | H85 evaluable (33%) received <48 h at33–35°C; 27% never reached final33°C because of complications/physician decisions. | eFigures3/4 and eTable3; p8 Limitations M-N011 |
| M-N010 | [p4 Patient Characteristics](../../../jama_cooper_2018_oi_180132.pdf#page=4), [p1 abstract](../../../jama_cooper_2018_oi_180132.pdf#page=1) | Until rewarming H hypothermia median72.2 h (IQR69.8–77.3); rewarming to normothermia median22.5 h (IQR16–27); 34 patients had rewarming paused because increased ICP. Abstract induction median1.8 h (IQR1.0–2.7), rewarming22.5 (16–27). | p8 discussion induction1.8 h, target >10 h, rewarming22.5 h, paused34; eFigure1 pointer |
| M-N011 | [p8 Limitations](../../../jama_cooper_2018_oi_180132.pdf#page=8) | Never reaching33°C discussed as19% having hypothermia withdrawn early and a further13% not reaching33°C. Percentages printed without numeric denominators in this paragraph. | M-N008/M-N009 for source-grounded definitions; no assumption about denominator or nesting made |
| M-N012 | [p2 Participants/Data Collection](../../../jama_cooper_2018_oi_180132.pdf#page=2) | Five out-of-hospital/paramedic agencies and14 EDs screened; estimated age18–60 y; GCS<9, intubation actual/imminent; exclusions SBP<90 mm Hg or sustained HR>120/min, GCS3 and unreactive pupils; ED enrollment up to3 h after injury. Follow-up death or6 mo; temperature/ICP hourly first96 h. | Participant criteria affect population; p3 outcome scale; p5 Table1 definitions |
| M-N013 | [p2 design/oversight](../../../jama_cooper_2018_oi_180132.pdf#page=2) | Six countries (Australia, New Zealand, France, Switzerland, Saudi Arabia, Qatar); first enrolled2010-12-05, last2017-11-10, final follow-up2018-05-15. Planned blinded interim analyses after125/250 recruits, additional safety at300/350/400/450 after Eurotherm3235 publication. | p1 dates and6 countries; M-S025 |
| M-N014 | [p2–3 randomization](../../../jama_cooper_2018_oi_180132.pdf#page=3) | Individual allocation1:1; variable permuted blocks2 and4; strata out-of-hospital vs ED, ambulance service/geographic regions. Clinicians unblinded; primary assessors blinded structured telephone questionnaires. | M-S027 analysis strata |

## Numeric relationships: complete Table 1

All below are [PDF p5 Table 1](../../../jama_cooper_2018_oi_180132.pdf#page=5), REPORT, intent-to-treat population H n260/C n240, H then C. Counts use those group denominators unless explicitly shown otherwise. Values are descriptive, with no P value/CI printed in Table 1.

| ID | Row/position | H printed value | C printed value | Unit, scale or denominator definition |
|---|---|---|---|---|
| M-N015 | Men | 207 (79.6) | 194 (80.8) | n (%) |
| M-N016 | Women | 53 (20.4) | 46 (19.2) | n (%) |
| M-N017 | Age | 35.0 (13.5) | 34.1 (13.4) | mean(SD), years |
| M-N018 | Overall GCS | 6 (4–7) | 6 (4–7) | median(IQR), highest reliable score before randomization; scale3–15; lower = lower consciousness; score6 unconscious |
| M-N019 | Motor GCS | 3 (1–4) | 3 (2–5) | median(IQR) |
| M-N020 | One/both pupils reacting | 220 (84.6) | 202 (84.2) | n(%); footnote some patients GCS>3 with small unreactive pupils |
| M-N021 | Hypotension out-of-hospital or ED | 26/257 (10.1) | 27/239 (11.3) | SBP<90 mm Hg |
| M-N022 | Hypoxia out-of-hospital or ED | 37/256 (14.5) | 39/237 (16.5) | SpO2<90% |
| M-N023 | Temperature at scene | 36.0 (1.2) | 35.9 (1.0) | mean(SD), °C; available H162/C143 (footnote e) |
| M-N024 | CT Marshall diffuse injury I | 18 (6.9) | 17 (7.1) | normal findings |
| M-N025 | CT Marshall diffuse injury II | 152 (58.5) | 128 (53.3) | diffuse injury |
| M-N026 | CT Marshall diffuse injury III/IV | 18 (6.9) | 20 (8.3) | radiologic increased-ICP signs |
| M-N027 | CT Marshall evacuated mass lesion V | 69 (26.5) | 72 (30.0) | first CT categorized; evacuation<24 h after injury classified V even if first CT before surgery |
| M-N028 | CT Marshall nonevacuated mass lesion VI | 3 (1.2) | 3 (1.3) | Marshall scale I–VI; V/VI mass lesion |
| M-N029 | Probability unfavorable outcome6 mo: IMPACT-TBI (core+CT) | 0.46 (0.24) | 0.46 (0.23) | mean(SD) probability0–1, 1=100%; unfavorable GOS-E≤4; validated GCS<13; age,motor,pupils,hypoxia,hypotension,CT |
| M-N030 | Injury Severity Score | 26.0 (18.0–34.0) | 20.0 (20.5–35.0) | median(IQR), printed literally; range0–75; higher greater injury severity;27=severe injury/multitrauma |
| M-N031 | Cause: motor vehicle | 84 (32.3) | 89 (37.1) | n(%) |
| M-N032 | Cause: motorcycle | 29 (11.2) | 18 (7.5) | n(%) |
| M-N033 | Cause: bicycle | 20 (7.7) | 20 (8.3) | n(%) |
| M-N034 | Cause: pedestrian | 28 (10.8) | 37 (15.4) | n(%) |
| M-N035 | Cause: hit by object | 24 (9.2) | 16 (6.7) | n(%) |
| M-N036 | Cause: fall/jump | 60 (23.1) | 54 (22.5) | n(%) |
| M-N037 | Cause: other | 15 (5.8) | 6 (2.5) | n(%) |
| M-N038 | Positive blood ethanol | 92/208 (44.2) | 89/193 (46.1) | n/N(%) |
| M-N039 | Blood ethanol>51 mg/dL | 74/208 (35.6) | 69/193 (35.8) | n/N(%), threshold mg/dL |
| M-N040 | Injury-to-randomization time | 1.8 (1.0–2.7) | 2.0 (1.1–2.8) | median(IQR), h |

## Numeric relationships: complete Figure 2, other outcome counts and graphical distribution

| ID | Source and unit | Complete printed relationship / visual context |
|---|---|---|
| M-N041 | [p6 Figure2A](../../../jama_cooper_2018_oi_180132.pdf#page=6) | Hourly temperature °C, first4 d/96 h postrandomization, overall N500. X ticks0,6,12,18,24,30,36,42,48,54,60,66,72,78,84,90,96 h. Y ticks28,30,32,34,36,38,40,42°C. H darker blue boxes; C pale boxes. Median line connects each6-h block. H graphical median approximately36°C at0, falls to approximately33–34°C by12–18 h, remains approximately33°C through72 h and rises to approximately36°C by96 h; C approximately36°C initially and37°C after12 h. All boxes/whiskers visually inspected; no exact temperature quantiles printed, so graph is not converted into fabricated exact numbers. |
| M-N042 | [p6 Figure2A patient counts](../../../jama_cooper_2018_oi_180132.pdf#page=6) | At0 and right-hand ticks6–96: H162,258,260,258,253,248,242,238,236,229,225,227,223,197,193,185,185; C143,234,238,234,231,224,222,217,214,208,205,202,200,190,189,187,183. Exact interval table below. |
| M-N043 | [p6 Figure2B](../../../jama_cooper_2018_oi_180132.pdf#page=6) | ICP mm Hg, same0–96 h x-axis ticks; y0,5,10,15,20,25,30,35 mm Hg. No0-h ICP box/count;16 blocks ending6–96 h. H/C trajectories approximately11–14 mm Hg, broadly overlapping IQRs; medians near12 mm Hg for both over most later intervals. Exact plotted quantiles not printed. |
| M-N044 | [p6 Figure2B patient counts](../../../jama_cooper_2018_oi_180132.pdf#page=6) | At interval right-hand ticks6–96: H133,193,194,188,192,189,188,187,183,178,176,175,172,167,164,159; C132,181,181,179,183,178,176,173,173,167,166,162,158,151,150,142. |
| M-N045 | [p6 Figure2 caption](../../../jama_cooper_2018_oi_180132.pdf#page=6) | Observed data, no imputation; box25th–75th percentiles; line median; whiskers largest/smallest within1.5×IQR. Interval includes right-hand hour, e.g.1–6 then7–12. Unique patients per interval, up to6 hourly observations each. Median observations/patient: temperature6 (IQR5–6), ICP6 (IQR6–6). |
| M-N046 | [p5 Adverse Events](../../../jama_cooper_2018_oi_180132.pdf#page=5) | Three propofol-related infusion syndrome diagnoses: H2/C1; C patient receiving nonprotocolized late-rescue H for refractory ICP; one of these3 died. p8 discussion repeats3 episodes. No comparative inference printed. |
| M-N047 | [p7 Figure3](../../../jama_cooper_2018_oi_180132.pdf#page=7) | Two stacked distributions of GOS-E1–8 at6 months after randomization, H/C. X0–100% by10%. Black death1; then vegetative2; lower/upper severe disability3/4; gold/orange lower/upper moderate disability5/6; yellow lower/upper good recovery7/8. Each width corresponds to proportion at that score, dashed boundary favorable vs unfavorable. No score-specific counts/percentages printed; graphical favorable totals align visually with approximately49% and are linked to M-S001 exact117/240 and111/226. Figure death widths describe outcome-evaluation set and are not assigned the separately printed mortality denominators. |
| M-N048 | [p3 Outcomes](../../../jama_cooper_2018_oi_180132.pdf#page=3) | GOS-E1 death,2 vegetative,3–4 severe disability,5–6 moderate disability,7–8 good recovery; favorable5–8, unfavorable1–4, primary6 mo after injury. Mortality discharge/6 mo; adverse events within10 d; mechanical ventilation/ICU/hospital duration also reported. Sliding dichotomy, complier-average causal effect, quality of life and cost-effectiveness explicitly not reported here. |
| M-N049 | [p3 Statistical Analysis](../../../jama_cooper_2018_oi_180132.pdf#page=3) | Planned500,364 evaluable, baseline favorable50%, absolute improvement15 percentage points,82% power,2-sided P=.05. Final510 during2017 after blinded review combined consent-withdrawn/lost-follow-up proportion. | 
| M-N050 | [p3 sample-size motivation](../../../jama_cooper_2018_oi_180132.pdf#page=3) | Historical2007 meta-analysis favorable improvement46%, RR1.46 (95%CI1.12–1.92), P=.006. Prior subgroup early H <45 y on arrival favorable increase50%, P=.02. These are supplied historical design motivations, not POLAR outcomes. |
| M-N051 | [p2 Introduction](../../../jama_cooper_2018_oi_180132.pdf#page=2), [p7 Discussion](../../../jama_cooper_2018_oi_180132.pdf#page=7) | Background approximately50% death/severe disability; prior large trial n392; two subsequent trials stopped≤50% planned recruitment. Prior meta-analysis parameters33–35°C,>48 h cooling,<0.25°C/h rewarming; repeated p8 discussion. No raw background source beyond supplied printed text used. |
| M-N052 | [p4 analysis compliance](../../../jama_cooper_2018_oi_180132.pdf#page=4) | Per-protocol/as-treated cooling compliance≤35°C for>48 h within96 h randomization; sensitivity majority first72 h instead96 h. All analyses initially exclude failure eligibility criteria. | 

### Exact Figure 2 alignment table

| Time/interval h | Temperature H | Temperature C | ICP H | ICP C |
|---|---:|---:|---:|---:|
| 0 only | 162 | 143 | — | — |
| 1–6 | 258 | 234 | 133 | 132 |
| 7–12 | 260 | 238 | 193 | 181 |
| 13–18 | 258 | 234 | 194 | 181 |
| 19–24 | 253 | 231 | 188 | 179 |
| 25–30 | 248 | 224 | 192 | 183 |
| 31–36 | 242 | 222 | 189 | 178 |
| 37–42 | 238 | 217 | 188 | 176 |
| 43–48 | 236 | 214 | 187 | 173 |
| 49–54 | 229 | 208 | 183 | 173 |
| 55–60 | 225 | 205 | 178 | 167 |
| 61–66 | 227 | 202 | 176 | 166 |
| 67–72 | 223 | 200 | 175 | 162 |
| 73–78 | 197 | 190 | 172 | 158 |
| 79–84 | 193 | 189 | 167 | 151 |
| 85–90 | 185 | 187 | 164 | 150 |
| 91–96 | 185 | 183 | 159 | 142 |

## Statistical relationships: all printed trial estimates, intervals and P values

Table 2 is [PDF p7](../../../jama_cooper_2018_oi_180132.pdf#page=7), titled Primary and Secondary Outcomes, Adverse Events, and Subgroups. Its footnote says intention-to-treat; n/N(%) unless otherwise indicated. Primary binary, mortality and adverse-event comparisons are stated to be unadjusted χ² equal-proportions tests (p3), 2-sided P<.05 (p4), with RR and risk difference and95% CIs. All Table 2 CI levels below are95%; the source reports no numeric χ² statistics or standard errors. Outcome contrasts H vs C; differences H−C. The printed estimates are transcribed without recalculation or reassignment to neighboring rows.

| ID | Outcome/population and time | H n/N (%) | C n/N (%) | Absolute difference pp (95% CI) | RR (95% CI) | P | Exact source / matching claim |
|---|---|---|---|---|---|---|---|
| M-S001 | Primary favorable GOS-E5–8, observed6-mo primary evaluation set | 117/240 (48.8) | 111/226 (49.1) | −0.4 (−9.4 to8.7) | 0.99 (0.82–1.19) | .94 | p7 Table2; p5 Primary Outcome exact same; p1 abstract prints risk difference **0.4%** with CI−9.4% to8.7%, RR/P same; p2 Key Points48.8/49.1 and nonsignificant; p7 Figure3/p8 conclusion no neurologic benefit |
| M-S002 | Severity-adjusted favorable6-mo GOS-E using IMPACT-TBI | — | — | — | 0.98 (0.87–1.11) | .75 | p7 Table2; p5 result similar after IMPACT-TBI extended adjustment; hierarchical multivariable log-binomial/random strata p3–4 |
| M-S003 | Ordinal6-mo GOS-E | — | — | — | **OR**0.97 (0.71–1.34) | .88 | [p5 Secondary Outcomes](../../../jama_cooper_2018_oi_180132.pdf#page=5); ordinal logistic, proportional odds justified score test p4; no adjusted ordinal estimate printed main |
| M-S004 | Hospital death, ITT observed hospital mortality | 52/260 (20.0) | 43/239 (18.0) | 2.0 (−4.9 to8.9) | 1.11 (0.77–1.60) | .57 | p7 Table2; mortality discharge endpoint p3 |
| M-S005 | Death6 mo, mortality set distinct from primary evaluation | 54/256 (21.1) | 44/239 (18.4) | 2.7 (−4.3 to9.7) | 1.15 (0.80–1.64) | .45 | p7 Table2; p5 Secondary Outcomes repeats entire row; p4 Figure1 denominators |
| M-S006 | Time to death, censored6 mo/last known contact | — | — | — | **HR**1.13 (0.76–1.69) | .54 | [p5 Secondary Outcomes](../../../jama_cooper_2018_oi_180132.pdf#page=5), eFigure2 pointer; Cox PH, KM/log-rank description p4 |
| M-S007 | Pneumonia within10 d randomization | 143/260 (55.0) | 123/240 (51.3) | 3.8 (−5.0 to12.5) | 1.07 (0.91–1.27) | .40 | p7 Table2; p1 abstract/p5 narrative repeat rates; eTable6 pointer |
| M-S008 | Bacteremia within10 d | 19/260 (7.3) | 12/240 (5.0) | 2.3 (−1.9 to6.5) | 1.46 (0.72–2.95) | .29 | p7 Table2 |
| M-S009 | Other infection within10 d | 36/260 (13.8) | 38/240 (15.8) | −2.0 (−8.2 to4.3) | 0.87 (0.57–1.33) | .53 | p7 Table2 |
| M-S010 | New/increased intracranial bleeding within10 d | 47/260 (18.1) | 37/240 (15.4) | 2.7 (−3.9 to9.2) | 1.23 (0.43–3.5) | .70 | p7 Table2 exact row visually aligned; p1/p5 repeat rates |
| M-S011 | New significant extracranial bleeding within10 d | 8/260 (3.1) | 6/240 (2.5) | 0.6 (−2.3 to3.5) | 1.17 (0.79–1.74) | .43 | p7 Table2 exact row visually aligned |
| M-S012 | Favorable6-mo GOS-E, surgically removed hematoma YES | 22/66 (33.3) | 27/68 (39.7) | −6.4 (−22.6 to9.9) | 0.84 (0.54–1.32) | .44 | p7 Table2; footnote c interaction.43; primary set partition |
| M-S013 | Same subgroup NO | 95/174 (54.6) | 84/158 (53.2) | 1.4 (−9.3 to12.2) | 1.03 (0.84–1.25) | .79 | p7 Table2; same interaction.43 |
| M-S014 | Favorable6-mo GOS-E, any intracranial mass lesion MarshallV+VI YES | 22/69 (31.9) | 28/71 (39.4) | −7.6 (−23.4 to8.3) | 0.81 (0.52–1.27) | .35 | p7 Table2; footnote d interaction.33; primary set partition |
| M-S015 | Same subgroup NO | 95/171 (55.6) | 83/155 (53.5) | 2.0 (−8.8 to12.8) | 1.04 (0.85–1.27) | .72 | p7 Table2; same interaction.33 |
| M-S016 | Treatment×surgically evacuated hematoma interaction | Subgroup M-S012 | Subgroup M-S013 | — | — | .43 | p7 Table2 footnote c; logistic treatment/subgroup interaction p4; p6 no significant interaction |
| M-S017 | Treatment×any intracranial hematoma interaction | Subgroup M-S014 | Subgroup M-S015 | — | — | .33 | p7 Table2 footnote d; p4 interaction method; p6 no significant interaction |
| M-S018 | Pneumonia per-protocol (population defined compliance/eligibility),10 d | 70.5% (no n/N main text) | 57.1% (no n/N main text) | 13.3% (2.4% to24.2%) | 1.23 (1.04–1.47) | .02 | [p6 continuation Per-Protocol and As-Treated Analyses](../../../jama_cooper_2018_oi_180132.pdf#page=6); explicitly unadjusted RR; eTable9 pointer; p8 discussion increased pneumonia |
| M-S019 | Pneumonia as-treated,10 d | 70.7% (no n/N main text) | 54.6% (no n/N main text) | 16.1% (5.7% to26.5%) | 1.29 (1.09–1.53) | .003 | p6 continuation; explicitly unadjusted RR; eTable11 pointer |

## Statistical relationships: methods and complete narrative claims without new numeric estimates

These entries preserve claims and specifications needed for checking. They are not inferred numeric results. Sidedness2-sided and significance threshold P<.05 apply to main-paper analyses, except historical context and sample-size P=.05 inputs. Secondary outcomes explicitly exploratory because no multiple-comparison adjustment. Main paper prints no numerical test statistics or standard errors for any relationship.

| ID | Exact source location | Complete method/result relationship; named missing numeric information |
|---|---|---|
| M-S020 | [p5 Per-Protocol and As-Treated Analyses](../../../jama_cooper_2018_oi_180132.pdf#page=5), [p6 continuation](../../../jama_cooper_2018_oi_180132.pdf#page=6) | No significant baseline differences in per-protocol/as-treated groups; favorable primary outcomes not different between either set of groups (eTables8–11). No primary effect estimates/CIs/P printed here. Pneumonia M-S018/M-S019 separately reported increased. |
| M-S021 | [p6 Per-Protocol continuation](../../../jama_cooper_2018_oi_180132.pdf#page=6) | Per-protocol/as-treated sensitivity analyses remain consistent (eFigures5/7). Cooling compliance sensitivity majority first72 h instead96 h per p4. No numeric main-paper estimates printed. |
| M-S022 | [p6 Post hoc Analyses](../../../jama_cooper_2018_oi_180132.pdf#page=6), [p7 continuation](../../../jama_cooper_2018_oi_180132.pdf#page=7) | Missing-primary-outcome scenarios show no significant H/C differences (eTable12); evaluable adequate-cooling-dose vs controls shows no significant favorable proportion differences (eTable13). Main paper gives no scenario counts/effect estimates/P values. |
| M-S023 | [p5 Additional Outcomes](../../../jama_cooper_2018_oi_180132.pdf#page=5) | No significant between-group differences for time to reach target (eTable7), mechanical ventilation days, ICU/hospital stays, mean6-mo GOS-E and unfavorable GOS-E among survivors (eTable5). Method p4: cooled time-to33°C relationship with favorable outcome via unadjusted χ² equal proportions; no time-category cutpoints or numeric results in main paper. |
| M-S024 | [p3 Statistical Analysis](../../../jama_cooper_2018_oi_180132.pdf#page=3) | Sample-size relationship M-N049:500 planned allows withdrawals/dropouts/consent/crossover and interim analyses;364 evaluable detects15-point improvement from50% with82% power,2-sided P=.05. Final510 after blinded withdrawal/loss review2017. No explicit numeric attrition allowance, interim alpha spending or formula in main paragraph; supplied plan source assigned to support mapper. |
| M-S025 | [p2 Trial Design and Oversight](../../../jama_cooper_2018_oi_180132.pdf#page=2), [p3 Statistical Analysis](../../../jama_cooper_2018_oi_180132.pdf#page=3) | Blinded planned interim conduct/progress/safety125/250 then safety300/350/400/450; sample size allowed interims. Main paper states no numeric stopping boundary or observed interim test result; Supplement1 referenced. |
| M-S026 | [p3 treatment and rewarming](../../../jama_cooper_2018_oi_180132.pdf#page=3) | Intervention definition M-N006/M-N007 connects primary contrast early prophylactic H vs controlled C: at least72 h at33°C (35°C with bleeding concerns), ICP-dependent up to7 d, target rewarming≤0.25°C/h and recurrence-triggered recooling. Life-threatening presumed bleeding permits35°C or C; both groups can receive other ICP treatment, C cooling wraps for pyrexia/refractory ICP. |
| M-S027 | [p3 Statistical Analysis](../../../jama_cooper_2018_oi_180132.pdf#page=3), [p4 continuation](../../../jama_cooper_2018_oi_180132.pdf#page=4) | All a-priori analyses according to randomized group excluding withdrawn consent unless otherwise indicated; no missing-data imputation. Binary primary/mortality/AE: unadjusted χ² equal proportions, frequency(%), RR/RD95%CI. Sensitivity hierarchic multivariable log-binomial adjusts extended IMPACT-TBI probability and randomization strata(location/site) as random effects; adjusted RR95%CI M-S002. Extended IMPACT factors age,motor GCS,pupils,CT Marshall,hypotension,hypoxia. p8 note says article updated2018-11-12 to correct mention of IMPACT-TBI in Methods. |
| M-S028 | [p4 Statistical Analysis](../../../jama_cooper_2018_oi_180132.pdf#page=4), [p5 result](../../../jama_cooper_2018_oi_180132.pdf#page=5) | Ordinal GOS-E logistic regression, proportional-odds assumption justified by score test, OR95%CI. Source does not print score-test statistic/P or exact numeric coding direction. Outcome scale/order is defined M-N048 and Figure3. Result M-S003 unadjusted H vs C. |
| M-S029 | [p4 Statistical Analysis](../../../jama_cooper_2018_oi_180132.pdf#page=4), [p5 result](../../../jama_cooper_2018_oi_180132.pdf#page=5) | Survival Cox proportional hazards censored6 mo/last contact, Kaplan–Meier and corresponding log-rank test; PH visually assessed using log-cumulative hazard plots. M-S006 HR/P in main narrative; no attribution of the printed P to a specific Cox coefficient vs log-rank computation beyond method wording. |
| M-S030 | [p4 Statistical Analysis](../../../jama_cooper_2018_oi_180132.pdf#page=4) | Prespecified evacuated hematoma/any significant intracranial hematoma effect heterogeneity by logistic treatment×subgroup interaction; M-S012–M-S017. Cooling-time-to33°C/favorable comparison unadjusted χ² equal proportions reported frequencies(%); no main numerical result. |
| M-S031 | [p4 analysis compliance](../../../jama_cooper_2018_oi_180132.pdf#page=4) | Prespecified per-protocol/as-treated both first exclude eligibility failures; cooling compliance≤35°C >48 h in96 h; noncompliers excluded(per-protocol) or transferred opposite group(as-treated). Sensitivity majority first72 h replaces96 h; post hoc missingness and adequate-dose analyses. Connects full protocol293(H132/C161) M-N004 and outcomes M-S018–M-S023. |
| M-S032 | [p4 Statistical Analysis end](../../../jama_cooper_2018_oi_180132.pdf#page=4) | SAS9.4;2-sided P<.05; no multiple-comparison adjustment, all secondary outcomes exploratory. No noninferiority/equivalence margin in the main report; trial primary question is effectiveness/improvement rather than a printed margin-based claim. |
| M-S033 | [p4 Results](../../../jama_cooper_2018_oi_180132.pdf#page=4), [p5 continuation](../../../jama_cooper_2018_oi_180132.pdf#page=5), [p6 Figure2](../../../jama_cooper_2018_oi_180132.pdf#page=6) | Core temperature described significantly lower in H first96 h; ICP similar during induction/maintenance/rewarming and therapy intensity similar (eFigure1/eTable4). Figure2 observed boxplots without imputation; main paper supplies no P/test/model for either trajectory claim, no numerical summary of mean daily ICP. p8 repeats no ICP/therapy-intensity effect. |
| M-S034 | [p1 conclusion](../../../jama_cooper_2018_oi_180132.pdf#page=1), [p2 Key Points](../../../jama_cooper_2018_oi_180132.pdf#page=2), [p7 Discussion](../../../jama_cooper_2018_oi_180132.pdf#page=7), [p8 Conclusions](../../../jama_cooper_2018_oi_180132.pdf#page=8) | H did not improve favorable6-mo neurologic outcomes; Key Points rates48.8%/49.1% nonsignificant. Discussion says no benefit in secondary outcomes including mortality, predefined subgroups/per-protocol/as-treated. Conclusion tied to M-S001 rather than an equivalence claim. |
| M-S035 | [p3 sample-size motivation](../../../jama_cooper_2018_oi_180132.pdf#page=3) | Historical RR1.46,CI1.12–1.92,P=.006 and<45-y subgroup50% improvement,P=.02 underpin15-point hypothesized effect. These supplied-source historical associations are kept distinct from POLAR estimates; neither model/test/sidedness of original historical studies reconstructed. |
| M-S036 | [p5 Patient Characteristics/Table1](../../../jama_cooper_2018_oi_180132.pdf#page=5), [p4 Results](../../../jama_cooper_2018_oi_180132.pdf#page=4) | Baseline groups described similar in all respects; Table1 all descriptive rows M-N015–M-N040, no comparative P values. Numeric quartile/median ordering remains literal (ISS C20.0,IQR20.5–35.0); no diagnostic calculation or judgment performed. |

## Numeric result cross-reference rows

To make every printed inferential outcome numerator and percentage traceable in the numeric inventory, these IDs refer to the full inferential rows above rather than repeating their effect estimates. Each includes both trial arms and the linked group difference/ratio, where printed.

| ID | Numeric relationship | Full evidence row |
|---|---|---|
| M-N053 | Favorable6-mo117/240(48.8%) vs111/226(49.1%) | M-S001; all abstract/Key Points/narrative/Table2/Figure3 locations preserved |
| M-N054 | Hospital mortality52/260(20.0%) vs43/239(18.0%) | M-S004 |
| M-N055 | Six-month mortality54/256(21.1%) vs44/239(18.4%) | M-S005 |
| M-N056 | Pneumonia143/260(55.0%) vs123/240(51.3%) | M-S007 |
| M-N057 | Bacteremia19/260(7.3%),12/240(5.0%); other infection36/260(13.8%),38/240(15.8%) | M-S008/M-S009 |
| M-N058 | Intracranial bleeding47/260(18.1%),37/240(15.4%); extracranial8/260(3.1%),6/240(2.5%) | M-S010/M-S011 |
| M-N059 | Surgically evacuated YES22/66(33.3%),27/68(39.7%); NO95/174(54.6%),84/158(53.2%) | M-S012/M-S013; strata partition primary evaluation populations |
| M-N060 | Any mass lesion YES22/69(31.9%),28/71(39.4%); NO95/171(55.6%),83/155(53.5%) | M-S014/M-S015; strata partition primary evaluation populations |
| M-N061 | Per-protocol pneumonia70.5% vs57.1% | M-S018; main article does not print n/N |
| M-N062 | As-treated pneumonia70.7% vs54.6% | M-S019; main article does not print n/N |

## Matching and extraction boundaries

No old finding, candidate, checker, screening, classification, recheck, quality or final-report record was read. All listed relationships are descriptive extraction inputs for fresh downstream review. Every numeric-bearing trial row in Tables1/2, all flow counts, all printed Figure2 contributor counts, axes and caption definitions, every Figure3 category, all main-paper effect estimates/intervals/P values and method specifications are represented. Repeated narrative occurrences are linked to their result rows. The main report provides no event person-time rates, person-time quantities, numerical test statistics or numerical standard errors; its use of “rates” for pneumonia/bleeding refers to the displayed proportions. No exact pointwise graphical quantiles are printed in Figures2/3; visual ranges above are approximate locator descriptions only, not extracted exact outcome values. Pages9/10 add references and article information, no applicable trial-result numeric unit.

Limits: no direct scientific-coverage gap. Graphical distributions cannot yield source-printed exact category proportions or hourly quantiles because these are unlabelled. Numeric cells in supplementary result tables are outside this disjoint main-paper scope and must be matched by support mapping rather than assumed. Evidence links resolve to the supplied10-page PDF. No source or reused artifact was changed.
