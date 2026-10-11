# Support mapping shard: DOC-002 PDF pages 22–42

## Scope, source authority, and processing

Assigned and completed scope: all 21 pages of `joi190079supp1_prod.pdf`, PDF pp.22–42, exclusively. Document role: PLAN throughout; these pages contain prospective eligibility, protection, oversight and pharmacotherapy instructions, historical contextual data, and bibliography. This map reports supplied material, without candidate selection or adjudication. No Office, workbook, CSV, cached values, or formulas occur in this assigned scope.

Reusable aid read in full: `.ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-002_pp22-42_layout.txt`. A direct Poppler `pdftotext -layout -f 22 -l 42 joi190079supp1_prod.pdf` extraction was generated at `.ai_paper_validation/review_1_6_2/preprocessing/support_appendix_mapping/direct_pp22-42_layout.txt` and byte-compared with the reusable layout aid: identical. Source authority is the supplied PDF, not earlier conclusions. Exact page 41 table and surrounding dose rules were visually read from a fresh CPU Poppler `pdftoppm -f 41 -l 41 -singlefile -scale-to 1600 -png` render at `preprocessing/support_appendix_mapping/p41.png`. OCR was unnecessary. Engine: available direct Poppler tools, CPU. Reused assets remain unchanged. No scientific or derivative gap remains in these units.

Numeric relationship IDs: N211–N236 (26); statistical specification IDs: S081–S084 (4). These IDs describe relationships and are not findings. Matching keys are semantic keys for the main mapper/checkers; this shard did not open unassigned main-paper pages. All numeric quantities retain the source's scale and units.

## Complete page ledger

| PDF page | Source content opened | Relevant relationship IDs or explicit applicability |
|---|---|---|
| 22 | Exclusion criteria 5–12; rationale 1–4 | N211, N212; eligibility and permitted interventions |
| 23 | Rationale 5–12 | N213, N214; historical treatment/recruitment context distinguished from trial data |
| 24 | Sources of materials, potential risks, recruitment | N215, N216; projected RCT relapse risk and historical safety context |
| 25 | Consent, stabilization capacity, nonresponse rule | N217, N218; RCT entry after stabilization |
| 26 | Clinical worsening, RCT monitoring, relapse/suicide management, adverse effects | N219, N220, N221 |
| 27 | Metabolic monitoring, confidentiality, genetic data sharing, potential benefits | N222; operational thresholds; confidentiality has no quantitative analysis specification |
| 28 | DSMB and recruitment of women/minorities | S081, N223; no formal efficacy stopping boundary printed here |
| 29 | Demographic recruitment context, cultural competence, historical Table 5, resource sharing | N224, N225; Table 5 refers to original STOP-PD, not STOP-PD II |
| 30 | Database and biomaterial sharing, diagnostic assessment, rating reliability | N226; no new trial result; genetic shipping/logistics explicitly mapped below |
| 31 | Database history, dissemination and consent, references 1–10 | N227; bibliography portion not applicable to trial numeric results or planned statistical rules |
| 32 | References 11–33 | No applicable new trial numeric/statistical relationship; citation years, volumes, pages and follow-up durations in titles identify external publications only |
| 33 | References 34–54 | No applicable new trial numeric/statistical relationship; bibliographic metadata only |
| 34 | References 55–74 | No applicable new trial numeric/statistical relationship; bibliographic metadata and gene names only |
| 35 | References 75–89 | No applicable new trial numeric/statistical relationship; bibliographic metadata and gene variants only |
| 36 | References 90–112 | No applicable new trial numeric/statistical relationship; instrument citations and bibliographic metadata only |
| 37 | References 113–136 | No applicable new trial numeric/statistical relationship; instrument/metabolic/pharmacokinetic citations and bibliographic metadata only |
| 38 | References 137–159 | No applicable new trial numeric/statistical relationship; statistical/missing-data references are citations rather than additional analysis instructions |
| 39 | References 160–163, appendix A1 and A1.1–A1.2 | N228, N229, N230; acute titration and dose adjustment |
| 40 | A1.2 continuation, dosing rationale, lorazepam/benztropine, A2, A3 opening | N230, N231, N232, N233, N234; S082 |
| 41 | A3.1 sertraline, A3.2 blinded-switch table, A3.3 olanzapine/placebo adjustments, A3.4 opening | N234, N235, N236; S083, S084 |
| 42 | A3.4 continuation, historical benztropine count, Preskorn reference | N232; bibliographic reference not applicable to trial numeric/statistical relationships |

## Numeric and design relationship map

| ID | Exact PLAN location | Supplied values, definitions, and conditions | Matching report key / comparison use |
|---|---|---|---|
| N211 | [p.22](../../../../joi190079supp1_prod.pdf#page=22), lines 1037–1059 | Type 1 diabetes defined as insulin-dependent onset <35 years and/or prior documented ketoacidosis. Exclude acute/unstable medical illness within last 3 months; grand mal seizure within past 12 months; past sertraline intolerance including heart rate <50 bpm or serum sodium ≤129 mmol/L. Exclude requirement for psychotropics besides sertraline, olanzapine, lorazepam or mood-stabilizing anticonvulsants; pregnancy/breast-feeding and immediate ECT need. | Eligibility/population; eligibility restrictions affect the pool before randomization, not observed randomized count by themselves |
| N212 | [p.22](../../../../joi190079supp1_prod.pdf#page=22), lines 1060–1088 | Index-episode nonresponse exclusion: ≥6-week trial of sertraline ≥150 mg/day with olanzapine ≥15 mg/day. Age ≥18; moderate-to-severe depression and delusions required, with or without hallucinations. Ongoing improvement on other pre-study treatment excluded. | Acute eligibility; definition of adequate previous combined treatment |
| N213 | [p.23](../../../../joi190079supp1_prod.pdf#page=23), lines 1090–1125 | Recent substance abuse/dependence exclusion uses past 3 months rather than DSM-IV 12-month diagnostic period; history >3 months allowed. Dementia and specified other disorders excluded; stable chronic illness allowed. Historical STOP-PD: no more than 7 of 259 had Type 1 diabetes. | Eligibility and historical population context; 7/259 is not current trial count |
| N214 | [p.23](../../../../joi190079supp1_prod.pdf#page=23), lines 1133–1141 | Historical STOP-PD: only 5% received ≥3-week adequate combined antidepressant/antipsychotic trial during index episode before that study. Historical context supports expectation of limited recruitment impact. | Historical contextual percentage, not current trial event or eligibility count |
| N215 | [p.24](../../../../joi190079supp1_prod.pdf#page=24), lines 1159–1184 | Historical STOP-PD side effects >10%: weight gain, sedation, gastrointestinal symptoms, ≥1 fall, orthostatic dizziness. External absolute mortality-risk context 0.9% over 2–3 years current olanzapine use. Projected overall RCT relapse risk approximately 25%. External ECT relapse context up to 50% within 6 months. | Primary relapse projection (25%) may match sample-size assumptions; historical/external risks must not become trial results |
| N216 | [p.24](../../../../joi190079supp1_prod.pdf#page=24), lines 1146–1157, 1188–1199 | Three material sources: interview/informant scales, medical/pharmacy records, blood tests for genetics/metabolic measures/drug plasma levels. Screening targeted within 24 hours admission. | Measurement provenance; administrative screening target not a statistical outcome |
| N217 | [p.25](../../../../joi190079supp1_prod.pdf#page=25), lines 1205–1248 | Surrogate consent plus assent allowed for open-label acute/stabilization phases. Consent capacity reassessed at stabilization entry and at end of 8-week stabilization; capacity and written participant consent required for randomized phase. Sustained remission or near remission required by end stabilization. | Randomization eligibility, 8-week stabilization; no new remission-score definition on this page |
| N218 | [pp.25–26](../../../../joi190079supp1_prod.pdf#page=25), lines 1252–1258 | Not meeting remission criteria after 12 weeks acute sertraline/olanzapine: ineligible for stabilization and RCT, leave study at week 12. Significant worsening in acute/stabilization operationalized CGI change score 6 or 7, prompting withdrawal. | Acute duration ≤12 weeks, pre-randomization attrition, clinical worsening definition |
| N219 | [p.26](../../../../joi190079supp1_prod.pdf#page=26), lines 1260–1273 | RCT in-person research weekly first 8 weeks; remainder every 2 weeks alternating research and clinical assessments. Clinical worsening prompts urgent assessment for relapse or dose/lorazepam change. Relapse referral within 48–72 hours; projected average 3 relapse cases/year/site. | Relapse follow-up/ascertainment schedule; projected service need not observed event count |
| N220 | [p.26](../../../../joi190079supp1_prod.pdf#page=26), lines 1275–1291 | Suicide high risk: current plan, index-episode attempt, or ≥1 lifetime serious attempt requiring inpatient medical treatment. Imminent risk excluded, high risk starts as inpatient. SSI each visit. Research psychiatrist weekly first 6 acute weeks then every 2 weeks remainder acute/stabilization. Current plan or current attempt triggers removal and clinical management. | Safety/withdrawal and primary relapse component matching; use core plan definition when identifying actual endpoint |
| N221 | [p.26](../../../../joi190079supp1_prod.pdf#page=26), lines 1293–1308 | Current ideation without current plan/attempt, SSI items 4 or 5 score 1 or 2, may remain at psychiatrist discretion; extra weekly clinical visits until ideation ends/removal. Side effects monitored every assessment; minimum-dose reductions and benztropine permitted. | Safety thresholds and follow-up; do not equate ideation alone with current plan/attempt |
| N222 | [p.27](../../../../joi190079supp1_prod.pdf#page=27), lines 1310–1316 | Metabolic measures at acute week 4 then every 8 study weeks. PCP referral for fasting glucose >100 mg/dL, triglycerides >150 mg/dL, total cholesterol >200 mg/dL and/or LDL >130 mg/dL. | Metabolic timing and referral thresholds; thresholds are clinical referral rules, not an automatic endpoint-status or diagnostic-definition substitution |
| N223 | [p.28](../../../../joi190079supp1_prod.pdf#page=28), lines 1401–1419 | Anticipated 50% elderly; female:male approximately 2:1 at all sites. Four-site racial composition context: Westchester 13% African American and 13% Hispanic; Pittsburgh population 67% white, 27.1% African American, 2.8% Asian, 1.3% Hispanic. | Anticipated recruitment composition; peripheral context, not achieved randomized group demographics |
| N224 | [p.29](../../../../joi190079supp1_prod.pdf#page=29), lines 1420–1453 | McKeesport context 72% white, 25% African American, 0% Asian, 1.5% Hispanic; Toronto approximately 40% visible minority, previous STOP-PD Toronto sample 34% Asian/Black/Hispanic. Massachusetts expected Hispanic 15–20%; Worcester 2000 census 15.2%, 52% increase from 1990. Training five core modules plus 12 ethnic-specific. Previous STOP-PD overall 84.2% white, 11.2% Black, 4.6% Asian; 11.6% Hispanic/Latino. | Recruitment/background and training; no current efficacy relationship |
| N225 | [p.29](../../../../joi190079supp1_prod.pdf#page=29), Table 5 | Historical STOP-PD 12-week study completion, fully transcribed below. Columns: number randomized, % completing week 6, % completing week 12; race and ethnicity categories form separate partitions. | Historical baseline/context; within-display count/percentage relationships available, not STOP-PD II results |
| N226 | [p.30](../../../../joi190079supp1_prod.pdf#page=30), lines 1489–1519 | Biomaterial shipping ongoing during proposed 38 months recruitment, approximately 10 samples/month; DNA to Toronto within 4 months receipt; clinical transfer every 6 months. Annual primary-measure rater reliability evaluation. Historical 5-year STOP-PD GRID HAM-D ICC 0.93–0.98, DAS conviction ICC 0.69–0.84. | Logistics versus measure reliability; ICCs are historical reliability, not intervention effects |
| N227 | [p.31](../../../../joi190079supp1_prod.pdf#page=31), lines 1520–1547 | Database system has tracked >170000 rating scales over >20 years. Diagnostic/remaining clinical data submitted ≤6 months generation; genotype data by accepted manuscript or award end, whichever first; diagnostic/clinical and genotype release eligible 12 months receipt. | Administrative data sharing, explicitly not statistical analysis specification |
| N228 | [p.39](../../../../joi190079supp1_prod.pdf#page=39), Appendix A1 lines 1967–1980 | Nonpermitted psychotropics withdrawn ≤4 days when feasible before study meds; anticonvulsants up to 10 days, overlapping first acute week; withdrawal symptoms allow slower taper up to 10 days. Existing eligible sertraline/olanzapine continued and adjusted to target. Permitted drugs: olanzapine, sertraline, PRN lorazepam, PRN benztropine for EPSE. | Concomitant treatment and washout |
| N229 | [p.39](../../../../joi190079supp1_prod.pdf#page=39), A1 lines 1982–2000 | Open-label acute/stabilization; sertraline morning 50-mg tablets, olanzapine evening 5-mg tablets. Start 50/5 mg/day; day 4 increase to 100/10; day 7 targets 150/15, as tolerated. Side effects permit slower/downward titration; goal targets by day 14. Inadequate psychosis after 7 days 15-mg olanzapine: increase to 20 mg/day. No partial depressive improvement (17-item HAM-D below 16 defines partial improvement) after 4 weeks 150-mg sertraline: increase to 200 mg/day. | Acute treatment dose ranges, dose escalation, HAM-D partial-improvement rule |
| N230 | [pp.39–40](../../../../joi190079supp1_prod.pdf#page=40), A1.2 | Side effects may halt titration or reduce one/both drugs; resume targets when side effects resolve. Unable to tolerate sertraline 150 or olanzapine 15 after further attempt: lower maintenance allowed, minimum sertraline 50 and olanzapine 5 mg/day. | Dose tolerability and permitted minima |
| N231 | [p.40](../../../../joi190079supp1_prod.pdf#page=40), A1.3 | Historical STOP-PD end week 2 average sertraline 150 mg/day both ages; olanzapine younger 14 mg/day, older 13 mg/day. Current target 150/15; repeat escalation to olanzapine 20 after 7 days 15 with inadequate psychosis response. | Historical dosing feasibility separated from target and achieved current dose |
| N232 | [pp.40,42](../../../../joi190079supp1_prod.pdf#page=40), A1.4–A1.5 and A3.4 | Lorazepam starts 0.5–2 mg/day PRN, maximum 3 mg/day throughout; early withdrawal attempted, continuation allowed in RCT for insomnia/anxiety. EPSE olanzapine reduction by 5-mg increments to minimum 10 mg/day for this maneuver; persistent EPSE allows benztropine maximum 2 mg/day, continuing into RCT if needed. Neither lorazepam nor benztropine within 12 hours cognitive tests. Historical STOP-PD benztropine 5/259 (1.9%). | Concomitant treatment, cognition assessment, EPSE context; 10-mg EPSE maneuver minimum retains context distinct from general 5-mg tolerability minimum |
| N233 | [p.40](../../../../joi190079supp1_prod.pdf#page=40), A2 | Open-label stabilization 8 weeks after remission criteria. Worsening depressive symptoms: sertraline +50 mg every 7 days, max 200 mg/day. Relapse of delusions/hallucinations by SCID: leave stabilization. Worsening nondelusional worry: olanzapine +5 mg every 7 days, max 20. Side effects: reductions 50-mg sertraline /5-mg olanzapine every 7 days, minima 50/5 mg/day. | Stabilization duration, sustained psychosis remission/randomization eligibility, dose ranges |
| N234 | [pp.40–41](../../../../joi190079supp1_prod.pdf#page=41), A3 and A3.1 | Eligible participants randomized after stabilization to continue olanzapine or switch placebo. Open-label sertraline throughout RCT; maintain dose at randomization; pre-RCT exposure min 10/max 20 weeks. Side effects after PI discussion allow reductions 50 mg every 7 days to minimum 50 mg/day. No sertraline increase at any time in RCT because it confounds H1 testing. | Randomized intervention versus constant concomitant sertraline; dose-change rules |
| N235 | [p.41](../../../../joi190079supp1_prod.pdf#page=41), A3.2 table | Four-week substitution of bottle B blinded olanzapine/placebo for bottle A open-label olanzapine; tablets 5 mg. Full 5-by-4 pair table below, visually checked. Blinding excludes statistician and pharmacists only. | Four-week blinded taper, dose at randomization, placebo exposure time |
| N236 | [p.41](../../../../joi190079supp1_prod.pdf#page=41), A3.3 | Maintain randomization olanzapine/placebo dose as goal, allow adverse-effect/clinical-worsening adjustment: 1 tablet (=5 mg) every 7 days, range 5–20 mg/day; PI discussion/reason recorded. Primary aim is clinically relevant olanzapine range preventing relapse, not a specific fixed dose. | Randomized intervention dose range and flexibility |

## Complete tables

### Historical Table 5 (N225), PDF p.29, line 1455

Caption: Percentage of Participants Completing the 12-Week STOP-PD Study by Ethnicity and Race. This is historical original STOP-PD contextual evidence inside the PLAN document.

| Race/ethnicity | Number randomized | % completers week 6 | % completers week 12 |
|---|---:|---:|---:|
| Asian | 12 | 75.0 | 50.0 |
| Black or African American | 29 | 75.9 | 51.7 |
| White | 218 | 74.8 | 55.5 |
| Hispanic or Latino | 30 | 80.0 | 53.3 |
| Not Hispanic or Latino | 229 | 73.8 | 55.0 |

Race denominator partition 12+29+218; ethnicity partition 30+229. Percentages refer to completers within each category and time point; completion numerators are not separately printed. No P values, effect estimates, confidence intervals, or model labels are supplied in this display. Do not combine race and ethnicity rows as one partition.

### Blinded-switch table (N235), PDF p.41, lines 2091–2092

Caption: Schedule of Randomized, Double-Blind Switch of Open-Label Olanzapine to ‘Blinded’ Olanzapine Or Placebo. Column groups are number of open-label pills at start. Each cell lists Bottle A / Bottle B daily pill counts. Bottle A = open-label olanzapine; Bottle B = blinded olanzapine or placebo; 5 mg/tablet. Total pill count stays at the starting count within each column; active dose depends on arm and bottle allocation.

| Switch week | Start 4 pills: A/B | Start 3 pills: A/B | Start 2 pills: A/B | Start 1 pill: A/B |
|---|---|---|---|---|
| Week 1 | 3/1 | 2/1 | 1/1 | 1/0 |
| Week 2 | 2/2 | 2/1 | 1/1 | 1/0 |
| Week 3 | 1/3 | 1/2 | 1/1 | 1/0 |
| Week 4 | 1/3 | 1/2 | 1/1 | 1/0 |
| Thereafter | 0/4 | 0/3 | 0/2 | 0/1 |

No dose fraction, percentage, or inferential quantity is printed in this table. Full placebo-only substitution occurs after week 4 for all starting doses. The 1-pill group remains on the open-label pill through week 4 as printed.

## Inferential/statistical specification relationships

| ID | Exact PLAN location | Supplied specification | Matching key and boundaries |
|---|---|---|---|
| S081 | [p.28](../../../../joi190079supp1_prod.pdf#page=28), section 4.6 lines 1366–1391 | NIMH DSMB monitors safety/progress/retention and can recommend continuation, modification, termination based on balance adverse events/benefit. Quarterly reports; SAE notification within 48 hours. Blinded data sent for DSMB interim analysis if requested. | Interim/stopping oversight; this page does not print a numerical efficacy boundary, information fraction, or alpha-spending rule. Conditional DSMB authority is preserved rather than converted into a fixed interim test. |
| S082 | [p.40](../../../../joi190079supp1_prod.pdf#page=40), A1.5 lines 2033–2039 | Benztropine prescription will be taken into account in secondary statistical analyses of EPSE. | EPSE secondary-analysis covariate/specification; no coefficient, test, functional form or estimate given on this page. |
| S083 | [p.41](../../../../joi190079supp1_prod.pdf#page=41), A3.1 lines 2067–2081 | Sertraline increases prohibited because of H1 confounding; reductions allowed to avoid forced attrition. Changes carefully recorded and reported descriptively for each treatment arm. | Primary relapse intervention/control interpretation and descriptive reporting of sertraline dose changes; not an additional efficacy hypothesis. |
| S084 | [p.41](../../../../joi190079supp1_prod.pdf#page=41), A3.3 lines 2094–2105 | Primary treatment question uses a clinically relevant olanzapine range, not one fixed dose; dose changes recorded and reported descriptively per arm. | Randomized intervention definition and descriptive reporting of olanzapine/placebo dose changes; no new statistical method specified here. |

## Limits and completion

All 21 assigned pages were read, including all bibliography pages and administrative content. Every applicable table is transcribed in full. No trial effect estimate, CI, P value, model result, sensitivity-result table, subgroup-result table, figure, or statistical formula occurs in these assigned pages. Historical numeric material is explicitly identified, preserving its denominators and units. Statistical comparison and inclusion screening belong to subsequent agents; this map makes no candidate diagnosis. Gaps: none. Source and reusable assets were not modified.
