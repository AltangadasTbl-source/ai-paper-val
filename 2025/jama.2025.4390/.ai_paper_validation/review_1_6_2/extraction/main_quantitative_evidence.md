# Main-paper quantitative evidence map

Agent runtime: 01a12bbc-5da9-7d42-af3f-0d5325decd82. Role: fresh main quantitative mapper. Exact scope: DOC-001, all physical PDF pages 1–12, REPORT. All 12 pages are fresh-required; no historical scientific conclusions were read. Coverage and asset inventories were read; historical main assets are STALE. Values below retain the current supplied PDF reading. Mapping does not select findings or candidates.

## Derivative provenance and source authority

Source: `jama_garrison_2025_oi_250019_1749674951.29054.pdf`. Native and sorted-reading-order text: `preprocessing/main_fresh/native-1-12.txt` and `preprocessing/main_fresh/layout-1-12.txt`, generated with package-local pinned PyMuPDF 1.26.4 via supplied `pdf_tools.py text`, first 1 last 12, second command with `--layout`. Rendered current pages: `preprocessing/main_fresh/page-4.png`, `page-5.png`, `page-6.png`, `page-7.png`, `page-8.png`, `page-9.png`, supplied `pdf_tools.py render`, PyMuPDF 1.26.4, 200 dpi, CPU. All six were visually inspected to confirm table alignment, signs, rates, intervals, captions, labels, and figure risk counts. No OCR needed. Encoded ≥ symbols in native text were resolved by direct rendered-page inspection, not silently assumed. Yellow highlighting is present in the supplied source; it is not mapper annotation or a scientific judgment.

Evidence links below are relative to this extraction artifact; each physical source page ends in `#page=N`.

## Complete page coverage

| Page | Applicable evidence and mapped relationships | Status |
|---|---|---|
| 1 | Abstract design, population, summary, primary endpoint, primary estimate: N001, N002, S001 | COMPLETE |
| 2 | Key Points matching result; design/eligibility/recruitment; contextual trial quantities: N003, N004, S002 | COMPLETE |
| 3 | Allocation/intervention/follow-up; outcome definitions; linked-data coverage; sample-size/interim/stop rules: N005, N006, S003, S004, S005 | COMPLETE |
| 4 | Figure 1 entire flow; analysis/censoring; entire participant summary: N007, N008, N009, S006 | COMPLETE |
| 5 | Table 1 first page, every row: N010 | COMPLETE |
| 6 | Table 1 continued and all footnotes; target changes; primary and sensitivity results; adherence: N011, N012, S007, S008 | COMPLETE |
| 7 | Figure 2 risk table/axes/caption/covariates; ABPM and EQ-5D results; contextual discussion: N013, N014, S009, S010, S011, S012, S013, S014, S015 | COMPLETE |
| 8 | Table 2 every row, all counts/distributions/rates/differences/estimates/intervals/P values and footnotes: N015, S016–S030 | COMPLETE |
| 9 | Figure 3 every row, both arms, all rates/HR/intervals/interactions and caption: N016, S031–S049 | COMPLETE |
| 10 | Limitations, confidence-bound interpretation, ABPM refusal and contextual quantities, conclusions; administrative information: N017, S050 | COMPLETE |
| 11 | Funding, disclosures, references and provenance only; no applicable original quantitative result or analysis relationship | COMPLETE; NO_APPLICABLE_UNITS |
| 12 | References only; no applicable original quantitative result or analysis relationship | COMPLETE; NO_APPLICABLE_UNITS |

Total 12/12 pages mapped. Numeric relationships N001–N017; statistical relationships S001–S050. Full displays are grouped only where every row is explicitly transcribed below. No scientific-coverage gap.

## N001 / S001 — Abstract primary result and summary

[PDF p. 1](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=1). Randomized 3357, bedtime 1677, morning 1680, ratio 1:1; 56.4% female; median age 67 years; 53.7% monotherapy; median follow-up 4.6 years in each arm. Composite first all-cause death or hospitalization/ED visit for stroke, acute coronary syndrome, or heart failure. Rates bedtime 2.3 vs morning 2.4 per 100 patient-years. Adjusted HR bedtime vs morning 0.96 (95% CI 0.77–1.19), P=.70. Individual components, all-cause hospitalizations/ED visits, and safety outcomes stated not different, specifically falls/fractures, new glaucoma, 18-month cognitive decline. Conclusion safe but no reduction in cardiovascular risk; administration time does not affect risks/benefits. Recruitment 436 primary care clinicians, 5 Canadian provinces, March 31, 2017–May 26, 2022; final follow-up December 22, 2023. Compare matched p.2 Key Points, p.6 primary narrative, p.7 Figure 2, p.8 Table 2, p.9 all-patients row.

## N002 — Abstract endpoint and intervention population

[PDF p. 1](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=1). Community-dwelling adults with hypertension taking ≥1 once-daily antihypertensive. All once-daily antihypertensives shifted to bedtime versus morning. Safety includes visual, cognitive, fall/fracture outcomes; secondary all-cause unplanned hospitalization/ED visits. Trial described multicenter open-label pragmatic randomized with blinded endpoint assessment.

## N003 / S002 — Key Points and trial context

[PDF p. 2](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=2). Key Points: 3357, median 4.6 years, primary 2.3 vs 2.4 per 100 patient-years, adjusted HR .96, no visual/cognitive/fall/fracture difference, safe but no cardiovascular reduction. Context only, not BedMed data: MAPEC 2000–2009, n2156, 61% MACE reduction; Hygia 2008–2018, n19084, 45% reduction; TIME 2011–2021, n21104, no benefit. Those contextual external findings are mapped as supplied-paper statements and are not independently reviewed with external literature.

## N004 — Design and eligibility

[PDF p. 2](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=2). Parallel PROBE design. 436 clinicians=429 family physicians+7 nurse practitioners; 5 provinces; 7 ethics boards. Inclusion age ≥18, hypertension, ≥1 once-daily BP medication; additional more-than-once-daily BP medicines allowed, diuretics eligible. Predefined interim assessment of 6-month diuretic bedtime adherence among monotherapy participants; approximately three-fourths adherent, no enrollment change. Exclusions disruptive shift work, glaucoma, continuing-care facilities. Recruitment 76.5% via clinician mailed invitation. All numbers serve population/implementation context, not outcome denominators.

## N005 — Allocation and outcome ascertainment

[PDF p. 3](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=3). Central 1:1 permuted blocks sizes 10 or 12, province-stratified. Research assistants recommended one timing change/week. Bedtime on readying for bed; morning on arising; dinnertime or lunchtime fallback respectively if intolerant. Follow-up 1 week, 6 weeks, 6 months and every 6 months, telephone or 6-monthly email except 18-month Short Blessed Test. New glaucoma → morning use irrespective allocation, 43 bedtime participants. Medication-level adherence assesses timing rather than forgotten doses. Administrative linked data available 92.6%, absent 7.4%; 90.3% of absent-data participants resided Ontario/Saskatchewan. Blinded 3-physician adjudication of self-report and administrative outcomes.

## N006 / S003 — Endpoint definitions and status

[PDF p. 3](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=3). Primary first occurrence all-cause death, hospitalization/ED ACS, stroke, or heart failure. Secondary: ≥2-point Short Blessed Test worsening at 18 months; time to each primary component, all-cause unplanned hospitalization/ED visit, nursing-home admission, nonvertebral fracture, new glaucoma. Other safety: vision much worse once or slightly worse ≥2 occasions; new impairment consistent with dementia (18-month Short Blessed Test newly ≥10 or administrative new dementia); prior-month lightheadedness/fainting/falling; time to hip fracture; nocturia. Also examined 12-month EQ-5D-5L health score. Some secondary outcomes altered from initial protocol/registry while blinded; p.3 points to supplementary Section 5 rationale. Match status/definitions only against supplied plan and supplementary maps, not assumptions.

## S004 — Sample-size inputs

[PDF p. 3](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=3). Event-driven, detect or exclude 25% reduction HR≤.75, power .8, time-to-event survival, 1:1, type I probability .05, required 379 events; increase 7% to 406 events for withdrawals/loss projected 5%. No preferred analysis inferred. Printed inputs are complete source-grounded quantities for reproduction.

## S005 — Interim and stopping rules

[PDF p. 3](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=3), [PDF p. 6](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=6). Five-member board; only interim May 18, 2022 with 155 primary outcomes and all outcomes analyzed; October 28, 2022 discussion after TIME. Consider stopping if primary benefit P≤.001 or any harm P≤.05; continued each occasion. Investigators blinded except adherence and 24-hour ABPM. Early stop solely funding constraints. Before interim target 406→255 to match MAPEC; interim intended at half targeted events; later no-cost extension; final 336 primary outcomes. No interim estimate/P printed in main source; named evidence absence retained.

## N007 — Figure 1 screening and allocation flow

[PDF p. 4](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=4). Assessed 5073; excluded 1716: not interested1249; not eligible375 (glaucoma/high intraocular pressure207, no BP medication68, no hypertension43, no fixed sleep32, nonparticipating province14, only twice-daily BP medicines8, no medication-timing control3); physician advice87; other5. Randomized3357: bedtime1677, morning1680; included primary analysis1677/1680. Bedtime interview withdrawals266=213 electronic+53 no electronic; lost63=59 electronic+4 no electronic. Morning withdrawals244=202 electronic+42 no electronic; lost58=56 electronic+2 no electronic. No ≥1 BP medication allocated-time use at 6 months: bedtime177 among1518 respondents, morning53 among1567. Figure wording retained exactly: “Did not take at least 1 BP medication at the allocated time at 6 mo.”

## N008 — Results population and follow-up losses

[PDF p. 4](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=4). Screen5073/randomized3357; arms1677/1680. Overall female56%, median age67, diabetes18%, CAD11%, CKD7%, about half monotherapy; drug classes ACE36%, ARB30%, CCB29%, diuretic27%, combination18%, beta17%, other1%. Median4.6years. Total all-follow-up loss101/3357 (3.0%): bedtime57/1677 (3.4%), morning44/1680 (2.6%). Active-follow-up loss but administrative tracking530/3357 (15.8%): bedtime272/1677 (16.2%), morning258/1680 (15.4%). Match Figure 1 component sums; p.10 repeats overall3%.

## N009 / S006 — Analysis populations and censoring

[PDF p. 4](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=4). Primary ITT/as-randomized Cox proportional hazards. Most other outcomes Cox or Poisson. Secondary survival ITT; other analyses available-data only; no missing-value imputation. Two-sided P<.05. All-follow-up loss censored last telephone/email; administratively trackable active-follow-up dropouts censored latest healthcare contact among hospitalization, ED, physician, dispensing, continuing care, labs. Post hoc per-protocol sensitivity excludes baseline beta-blocker or diuretic (poor timing adherence); diuretic–nondiuretic combination agents not excluded. Software SAS9.4 and R4.3.2. Primary Figure 2 adjustment covariates fully listed under S009.

## N010 / N011 — Complete Table 1

[PDF p. 5](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=5), [PDF p. 6](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=6). Every cell below is Bedtime/Morning; denominators1677/1680. Counts parenthesized percentages unless explicitly median(IQR).

| Characteristic | Bedtime | Morning |
|---|---|---|
| Age median(IQR), years | 67(60–73) | 67(61–73) |
| Age≥75 | 370(22.1) | 369(22.0) |
| Female | 950(56.6) | 943(56.1) |
| Male | 727(43.4) | 737(43.9) |
| Asian | 42(2.5) | 34(2.0) |
| Black | 7(.4) | 7(.4) |
| Hispanic/Latino | 5(.3) | 4(.2) |
| Indigenous | 29(1.7) | 22(1.3) |
| Southeast Asian/Indian | 17(1.0) | 20(1.2) |
| White | 1565(93.3) | 1587(94.5) |
| More than one race | 9(.5) | 5(.3) |
| Declined race | 3(.2) | 1(<.1) |
| Alberta | 1200(71.5) | 1200(71.4) |
| British Columbia | 235(14.0) | 236(14.0) |
| Manitoba | 130(7.8) | 131(7.8) |
| Ontario | 74(4.4) | 75(4.5) |
| Saskatchewan | 38(2.3) | 38(2.3) |
| Early bird | 881(52.5) | 859(51.1) |
| Night owl | 477(28.5) | 495(29.5) |
| Neither | 319(19.0) | 326(19.4) |
| Current smoker | 122(7.3) | 121(7.2) |
| Exercise days/week median(IQR) | 3(0–5) | 3(0–5) |
| Never exercises | 434(25.9) | 458(27.3) |
| BMI median(IQR), kg/m² | 28.8(25.7–33.0) | 28.9(25.7–32.9) |
| Physically frail | 299(17.8) | 307(18.3) |
| EQ-5D health median(IQR) | 80(70–90) | 80(75–90) |
| Short Blessed≤3 | 1376(82.1) | 1403(83.5) |
| Short Blessed4–6 | 248(14.8) | 224(13.3) |
| Short Blessed7–9 | 33(2) | 29(1.7) |
| Short Blessed≥10 | 19(1.1) | 23(1.4) |
| Declined cognition | 1(<.1) | 1(<.1) |
| Sleep apnea | 377(22.5) | 341(20.3) |
| Diabetes | 289(17.2) | 311(18.5) |
| Coronary artery disease | 172(10.3) | 188(11.2) |
| Chronic kidney disease | 119(7.1) | 129(7.7) |
| COPD | 86(5.1) | 80(4.8) |
| Stroke | 75(4.5) | 75(4.5) |
| Heart failure | 28(1.7) | 32(1.9) |
| Hip fracture | 22(1.3) | 27(1.6) |
| No listed comorbidity | 876(52.2) | 877(52.2) |
| One BP medication | 895(53.4) | 908(54.0) |
| Two BP medications | 588(35.1) | 577(34.3) |
| Three BP medications | 155(9.2) | 170(10.1) |
| ≥Four BP medications | 39(2.3) | 25(1.5) |
| ACE inhibitor | 584(34.8) | 631(37.6) |
| ARB | 536(32) | 471(28) |
| CCB | 479(28.2) | 489(29.1) |
| Diuretic | 446(26.6) | 472(28.1) |
| Combination pill | 315(18.8) | 300(17.9) |
| Beta-blocker | 289(17.2) | 278(16.5) |
| Other class | 26(1.6) | 21(1.3) |

Footnotes p.6: race self-selected supplied categories; chronotype naturally early bird/night owl. Exercise number days past week ≥30minutes vigorous enough to raise breathing rate; never exercises described answered0minutes. BMI kg/m². Tilburg physical frailty subscale0–8, ≥3 frail. EQ-5D health0–100 higher better. Short Blessed weighted6-item test0–28,5–9 questionable,≥10 dementia-consistent impairment. No tests/P values in baseline table. Rows with multiple medication classes/comorbidities need not partition arm total; categorical sex/province/chronotype/medication-number/cognitive groups do.

## S007 / S008 — Primary and sensitivity narrative

[PDF p. 6](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=6). Primary median4.6years each;2.3vs2.4/100patient-years; adjustedHR .96(.77–1.19),P=.70; unadjustedHR .94(.76–1.17). States individual components and all predefined subgroups not significantly different and no PH violations (supplement Section5). Post hoc per-protocol n1042/1023, no baseline beta/diuretic, median4.7years,1.7vs1.8/100patient-years; unadjustedHR .94(.68–1.28),adjustedHR .90(.65–1.23),P=.50. Direction bedtime versus morning; source identifies sensitivity as post hoc.

## N012 — Adherence narrative

[PDF p. 6](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=6). Six-month medication-level timing83% bedtime vs95% morning; participant ≥1 medication timing88%vs97%. Per-allocation medication alternatives1% morning lunchtime,5% bedtime dinnertime. At72months ≥1 medication per allocation70%vs88%. Twice-daily beta-blockers often unchanged; nocturia affects bedtime diuretic adherence. Denominators not printed here; locate supplemental tables rather than infer.

## N013 / S009 — Figure 2 complete display and primary model

[PDF p. 7](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=7). Cumulative first composite incidence percentage vs years since randomization0–6; main y-axis0–100 by20, inset0–20 by5. Risk rows at years0,1,2,3,4,5,6: bedtime1677,1623,1514,1229,1002,674,245; morning1680,1624,1506,1219,1000,667,263. No exact curve coordinates printed beyond axes; morning curve mostly above bedtime, both near15% at6years, crossing near late follow-up. Do not digitize inferential values. HR .96(.77–1.19); unadjusted .94(.76–1.17). Median follow-up caption bedtime4.6(IQR2.9–5.4),morning4.6(2.8–5.4) “patient-years.” Covariates stated predefined protocol stage: age,sex,physical frailty,current smoking,number non-BP medicines,EQ-5D health,hospitalization prior6months,HF,diabetes,CAD,stroke/TIA,CKD,dialysis,BMI>35,BMI<20,sleep apnea,exercise days,province. Match p.4 Cox/ITT and p.8 primary.

## N014 / S010–S015 — ABPM and one-year health

[PDF p. 7](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=7). Prespecified consecutive volunteer ABPM sample151/151,total302,median9.6months after randomization;90%power to detect MAPEC overnight systolic difference. All BP units mmHg; contrasts bedtime minus morning.

| ID | Outcome | Bedtime | Morning | Difference and95%CI | P |
|---|---|---|---|---|---|
| S010 | Daytime systolic | 133.8 | 136.2 | Not printed | .15 |
| S011 | Daytime diastolic | 75.2 | 75.6 | Not printed | .72 |
| S012 | Overnight systolic | 116.5 | 123.9 | −7.4(−11.2 to−3.7) | <.001 |
| S013 | Overnight diastolic | 62.9 | 65.5 | −2.7(−4.9 to−.4) | .02 |
| S014 | Daytime controlled BP <130/80 | 41.1% | 32.5% | Not printed | .12 |
| S015 | One-year EQ-5D0–100 | Mean78.9,SD15.2 | Mean79.5,SD14.6 | Absolute difference−.75(−1.69 to.19) | .12 |

Method not detailed for these comparisons in main text; do not label crude/unadjusted unless supplied matching supplementary evidence provides that definition. p.7 narrative says daytime nonsignificant, overnight means lower bedtime, secondary/safety and1-year health no difference.

## N015 / S016–S030 — Complete Table 2

[PDF p. 8](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=8). Arms bedtime1677,morning1680. Count is number in survival rows; percent/proportion and denominator appear where printed. Time column explicitly “Patient-years of follow-up, median(IQR)”; rates per100patient-years. Difference is event-rate difference or percentage-point difference. Blank cells retained as dash, not zero. Every CI95%; comparison bedtime versus morning. HR unless RR identified in row.

| ID | Outcome | Bedtime count or distribution | B time | B rate | Morning count or distribution | M time | M rate | Difference | Effect95%CI | P |
|---|---|---|---|---|---|---|---|---|---|---|
| S016 | Primary composite | 163 | 4.6(2.9–5.4) | 2.30 | 173 | 4.6(2.8–5.4) | 2.44 | −.14 | HR.96(.77–1.19) | .70 |
| S017 | All-cause mortality | 81 | 4.7(3.1–5.5) | 1.11 | 94 | 4.7(3.1–5.5) | 1.28 | −.18 | HR.90(.67–1.22) | .50 |
| S018 | Stroke hospitalization/ED | 27 | 4.7(3.0–5.5) | .37 | 32 | 4.7(3.0–5.5) | .44 | −.07 | HR.86(.52–1.44) | .57 |
| S019 | MI/ACS hospitalization/ED | 48 | 4.7(3.0–5.5) | .67 | 39 | 4.6(2.9–5.5) | .54 | .13 | HR1.25(.82–1.91) | .30 |
| S020 | HF hospitalization/ED | 30 | 4.7(3.0–5.5) | .41 | 43 | 4.7(2.9–5.5) | .59 | −.18 | HR.72(.45–1.15) | .17 |
| S021 | All-cause unplanned hospitalization/ED | 993 | 2.2(1.0–4.0) | 23.26 | 1047 | 2.2(.9–3.9) | 25.15 | −1.89 | HR.93(.85–1.02) | .10 |
| S022 | Nonvertebral fracture | 152 | 4.5(2.8–5.4) | 2.18 | 166 | 4.5(2.8–5.4) | 2.40 | −.22 | HR.92(.74–1.14) | .44 |
| S023 | Hip fracture | 20 | 4.7(3.0–5.5) | .27 | 31 | 4.6(2.9–5.5) | .43 | −.15 | HR.65(.37–1.15) | .14 |
| S024 | Falling | Mean4.9,SD11.7 | — | — | Mean5.0,SD11.2 | — | — | — | RR.96(.86–1.07) | .47 |
| S025 | Syncope | Mean.6,SD3.8 | — | — | Mean.6,SD4.1 | — | — | — | RR1.28(.93–1.75) | .12 |
| S026 | Lightheadedness | Mean18.8,SD25.2 | — | — | Mean20.3,SD26.2 | — | — | — | RR.95(.90–1.00) | .06 |
| S027 | New glaucoma | 43 | 4.7(3.0–5.5) | .60 | 39 | 4.6(2.9–5.5) | .54 | .06 | HR1.13(.73–1.74) | .58 |
| S028 | Subjective vision worsening | 420(25.0%) | — | — | 411(24.5%) | — | — | .5 | RR1.02(.89–1.17) | .74 |
| S029 | Cognitive decline18months | 376/1446(26.0%) | — | — | 395/1493(26.5%) | — | — | −.5 | RR.98(.85–1.13) | .82 |
| S030 | New dementia-consistent impairment; nursing home (two separately named results) | Dementia89(5.3%);nursing38 | Nursing4.7(3.0–5.5) | Nursing.52 | Dementia83(4.9%);nursing26 | Nursing4.7(3.0–5.5) | Nursing.36 | Dementia.4;nursing.17 | DementiaRR1.12(.83–1.51);nursingHR1.38(.83–2.27) | Dementia.48;nursing.21 |

Footnote a: falling/syncope/lightheadedness distributions are mean(SD) percentage of interviews reporting ≥1 occurrence prior30days; cognitive denominator separate because not all took18month test. Footnote b: difference absolute event rate or percentage of participants. Footnote c: all effects HR except falling,syncope,lightheadedness,subjective vision,cognitive18months,new dementia are RR. Footnote d: vision much worse at any point/slightly worse≥2occasions. Footnote e: cognitive≥2point worsening vs baseline18month Short Blessed, weighted6items0–28,5–9 questionable,≥10 dementia-consistent. Footnote f: dementia physician diagnosis any follow-up or18month score newly≥10. Footnote g: nursing group facility without personal medication-timing control. No standard errors/test statistics or total person-time printed in this table. Components count first component occurrences, and are not stated mutually exclusive; do not sum components as unique primary participants without qualification.

## N016 / S031–S049 — Complete Figure 3

[PDF p. 9](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9). Title same primary composite. Column headings literally “No. of events” and “Rate per100 patient-years” for each arm. Source prints all-patients bedtime163,71.0;morning173,71.0;HR.96(.77–1.19). Each row below prints count/rate for Bedtime then Morning, HR95%CI, and subgroup interactionP. Preserve71.0 and all subgroup rates exactly; no inferred relabeling. Left ofHR1 favors bedtime,right favors morning; HR axis ticks.3,.5,1,2,3. All plotted points/intervals match their printed row directions; HFYes interval extends below plotting range with arrow. Caption: prespecified subgroup interactionP from Cox with same primary covariates, characteristic and characteristic×randomization interaction; health score EQ-5D; all confidence intervals unadjusted. InteractionP tests heterogeneity, not within-subgroup effect. Model covariates S009.

| ID | Subgroup | Yes or first category B count/rate; M count/rate; HR(CI) | No or second category B count/rate; M count/rate; HR(CI) | InteractionP |
|---|---|---|---|---|
| S031 | Sex (male;female) | 80/30.5;94/30.4;.81(.59–1.09) | 83/40.5;79/40.6;1.17(.86–1.61) | .10 |
| S032 | Age≥75 | 77/14.9;81/14.5;.92(.67–1.27) | 86/56.1;92/56.5;.97(.72–1.31) | .87 |
| S033 | Physical frailty | 47/12.4;50/12.7;1.15(.75–1.76) | 116/58.6;123/58.3;.88(.68–1.14) | .22 |
| S034 | Polypharmacy | 80/23.0;91/22.4;.90(.66–1.22) | 83/48.0;82/48.6;1.03(.75–1.40) | .49 |
| S035 | Overall health≤75 | 91/28.5;77/25.1;1.11(.81–1.51) | 72/42.5;96/45.9;.83(.61–1.13) | .14 |
| S036 | Resistant hypertension | 33/7.7;46/7.0;.71(.45–1.14) | 130/63.3;127/64.0;1.06(.83–1.36) | .07 |
| S037 | Heart failure | 6/1.1;15/1.1;.36(.10–1.25) | 157/69.8;158/69.9;1.00(.80–1.24) | .16 |
| S038 | Diabetes | 37/12.5;50/12.5;.71(.45–1.12) | 126/58.5;123/58.5;1.08(.84–1.39) | .05 |
| S039 | CAD | 38/7.0;46/7.3;.88(.55–1.39) | 125/63.9;127/63.7;.97(.75–1.24) | .93 |
| S040 | Stroke/TIA | 16/4.6;25/4.8;.78(.38–1.61) | 147/66.4;148/66.2;.97(.77–1.23) | .57 |
| S041 | Sleep apnea | 37/16.0;38/14.4;.76(.47–1.22) | 126/55.0;135/56.6;1.00(.78–1.28) | .54 |
| S042 | CKD | 19/4.8;25/4.8;1.12(.55–2.29) | 144/66.2;148/66.2;.95(.76–1.20) | .97 |
| S043 | Sedentary | 50/17.7;60/18.3;.88(.60–1.29) | 113/53.2;113/52.7;.99(.76–1.29) | .69 |
| S044 | ACE inhibitor | 54/24.4;78/25.8;.74(.52–1.05) | 109/46.6;95/45.2;1.14(.86–1.51) | .05 |
| S045 | ARB | 56/22.8;39/19.7;1.07(.70–1.64) | 107/48.2;134/51.3;.93(.72–1.20) | .44 |
| S046 | Beta-blocker | 59/11.6;55/10.9;1.04(.71–1.52) | 104/59.4;118/60.1;.91(.70–1.19) | .54 |
| S047 | CCB | 64/19.2;75/19.8;.92(.65–1.30) | 99/51.7;98/51.2;.99(.74–1.31) | .66 |
| S048 | Diuretic | 50/18.6;63/19.6;.91(.62–1.33) | 113/52.4;110/51.4;.97(.74–1.27) | .43 |
| S049 | Combination BP medicines | 20/14.1;23/13.4;.95(.49–1.85) | 143/56.9;150/57.6;.93(.74–1.17) | .72 |

## N017 / S050 — Discussion quantitative interpretation

[PDF p. 7](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=7), [PDF p. 10](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=10). Main claims no death/MACE/hypotensive/visual/cognition/falls/fracture difference. Contextual Spanish registry35129morning/6723evening,median9.7years,adjusted no mortality difference; MAPEC61%MACE/57%all-cause reduction,Hygia45%/45%; Cochrane3deaths/24serious adverse events; MAPEC9years/Hygia10years annual48hourABPM. BedMed57% declined ABPM,total302 volunteers; BedMed nocturnal systolic difference−7.4,contextual review−2.3,crossover−1.7nonsignificant. Supplied discussion says all-cause mortality .80/100patient-yearsTIME vs1.20BedMed,50%higher. Main limitation: primaryCI rules out25%reduction; “BedMed excluded a hazard ratio≤0.76; TIME excluded a hazard ratio≤0.82”; CI no overlap with MAPEC/Hygia;436practices,3%withdrawal/loss. Match .76 lower unadjustedCI(S007/S009),.77adjustedCI(S001/S016),sample-powerHR≤.75(S004). These are mapped readings, without mapper diagnosis or external corroboration. Conclusion repeats safe/no cardiovascular reduction/preferences. Pages10–12 administrative/reference material has no additional original inferential results beyond those above.

## Coverage limitations

No scientific-coverage limitations. Native text adequate; visual inspection resolved horizontal/rotated table alignment and encoded comparison symbols. Total person-time, some ABPM methods/denominators, and individual interim results are not printed in main paper; these are source absences, not omitted mapping units. Matching supplied support evidence is handled by disjoint support mappers. Neither statistical pass is performed by this mapper; all statistical inventory rows remain pending fresh pass1/pass2 review.
