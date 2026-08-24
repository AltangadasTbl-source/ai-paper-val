# DOC-001 Main-Article Quantitative Evidence Mapping

## Scope and evidence basis

- **Source:** `jama_de_boer_2019_oi_190122.pdf` (DOC-001), PDF pp. 1-11.
- **Evidence used:** fresh page-addressable Acrobat native text, `preprocessing/native_text/DOC-001-acrobat-native.txt`, only.
- **Mapping boundary:** all result-relevant main-article numbers, including abstract, methods definitions that govern a result, narrative results, Tables 1-3, Figures 1-4, captions, and footnotes. Reference-list bibliographic quantities are not study results and are excluded.
- **Text handling note:** the native extractor renders typographic minus signs as a preceding period in several table/narrative values (for example `.12.3` where the figure text preserves `–12.3`). In this artifact, a minus sign is used only where directly preserved elsewhere on the same fresh page or clearly indicated by “decline”; the literal extractor form remains available in the cited source asset. No visual renderer/layout text was available.

## Abstract and trial definition (PDF p. 1)

- Design/population: 2 × 2 factorial randomized trial; 1312 adults with type 2 diabetes; recruitment November 2011-March 2014 across all 50 US states; follow-up completed December 2017; planned treatment duration 5 years.
- Four randomized cells: vitamin D3 2000 IU/d plus omega-3 fatty acids 1 g/d, n=370; vitamin D3 plus placebo, n=333; placebo plus omega-3 fatty acids, n=289; two placebos, n=320. Omega-3 capsule contents were EPA plus DHA.
- Randomized population: mean age 67.6 years; 46% women; 31% racial/ethnic minority; 934/1312 (71%) completed study. Baseline mean eGFR 85.8 (SD 22.1) mL/min/1.73 m².
- Primary result, vitamin D comparison: mean eGFR change baseline-year 5 −12.3 (95% CI −13.4 to −11.2) versus −13.1 (−14.2 to −11.9) mL/min/1.73 m²; difference 0.9 (−0.7 to 2.5) mL/min/1.73 m².
- Primary result, omega-3 comparison: −12.2 (−13.3 to −11.1) versus −13.1 (−14.2 to −12.0); difference 0.9 (−0.7 to 2.6) mL/min/1.73 m². Text states no significant interaction between interventions.
- Safety counts: kidney stones 58 (vitamin D 32, placebo 26); gastrointestinal bleeding 45 (omega-3 28, placebo 17).

## Methods quantities and result definitions (PDF pp. 2-3)

- Parent VITAL trial N=25 871. Main-study enrolment goal 1320; final randomized population 1312. Parent eligibility: men ≥50 years and women ≥55 years.
- Intervention formulation: vitamin D3/cholecalciferol 2000 IU; omega-3 capsule 1 g containing EPA 465 mg plus DHA 375 mg. Participants were asked to limit nonstudy supplemental vitamin D to ≤800 IU/d. Randomization November 2011-March 2014, computer-generated blocks of 8, stratified by age, sex, and race.
- Primary outcome: change in eGFR baseline to year 5. Original primary outcome was albuminuria, changed when duration extended to 5 years in 2016.
- Prespecified secondary outcomes: time to composite ≥40% eGFR decrease, kidney failure, or death; time to ≥40% eGFR decrease; change in urine ACR baseline-year 5, including time to ACR doubling with final ACR ≥30 mg/g. Post hoc: ≥40% eGFR decrease or kidney failure, and analogous ≥30% decline outcomes.
- Collection times: baseline, 2 years, and 5 years after randomization. Highly adherent subset: reported medication use at least two-thirds of the time. Omega-3 index: EPA+DHA as percentage of total fatty acids. BMI: weight/height².
- Sample-size relationship: 1320 gives 80% power for ≥2.3 mL/min/1.73 m² eGFR-change difference for each active-placebo comparison, two-sided α=.05, assuming 80% follow-up samples. The stated 5-year 2.3 difference is compared with a suggested surrogate threshold ≥0.75 mL/min/1.73 m²/year, equivalent to ≥3.75 over 5 years.
- Primary model: linear mixed model, random intercept; time as three nonordered values (baseline/year 2/year 5); treatment×time; age/sex and their time interactions; eGFR model additionally baseline ACR and ACR×time. Treatment effect P value is treatment×year-5 interaction; two-tailed P<.05 significance criterion. Missing data: M=20 imputations, Rubin rules. Secondary categorical outcomes: Cox proportional-hazards models; proportionality assessed with Schoenfeld residuals.

## Results narrative (PDF p. 4 and continuation p. 6)

- Baseline: mean age 67.6 years; median diabetes duration 6-10 years; 46% women; 31% minority; insulin 20%; antihypertensive medication 80%, including renin-angiotensin inhibitor 61%; mean eGFR 85.8; eGFR <60 in 165 (13%); ACR ≥30 mg/g in 117 (9%), including ACR ≥300 mg/g in 24 (2%).
- Retention: ≥1 postrandomization blood sample 1090/1312 (83%); year-5 blood sample 934/1312 (71%) and 76% of those alive. ≥1 urine sample 1091 (83%); year-5 urine sample 945 (72% randomized; 77% alive).
- Adherence at 2/5 years: vitamin-D assignment 92%/88%; omega-3 assignment 91%/89%. At year 2: serum 25(OH)D 41.4 (SD 11.0) ng/mL active vitamin D vs 29.8 (11.1) placebo, P<.001; omega-3 index 3.6% (1.0%) active vs 2.3% (0.8%) placebo, P<.001. DPP-4 inhibitor use 9% baseline/14% year 5; ARB 20%/29%; SGLT2 inhibitor initiated by 5%.
- Overall eGFR: baseline 85.8 (SD 22.1), year 2 80.0 (21.5), year 5 73.5 (21.9) mL/min/1.73 m². Baseline-year-5 mean change −12.7 (95% CI −13.6 to −11.7) full analytic population; −12.4 (−13.3 to −11.4) among 932 with eGFR at both times.
- Treatment primary results repeat the abstract values. Interaction of randomized treatments P=.42. Narrative states no significant subgroup heterogeneity and no significant correlation of change in 25(OH)D or omega-3 index baseline-year 2 with eGFR change baseline-year 5.
- Secondary outcomes: composite ≥40% eGFR decline/kidney failure/death occurred in 164: measured ≥40% decline 80, kidney failure 11, deaths 80, with overlaps. HR 0.92 (0.68-1.25) vitamin D and 1.11 (0.81-1.50) omega-3. Geometric mean ACR: 5.1 (4.6-5.7) mg/g at year 2; 9.2 (8.4-10.1) at year 5; narrative says approximately threefold baseline-year-5 increase and no assignment difference. All three prespecified secondary outcomes did not significantly differ; post-hoc ≥40%/≥30% composites also did not significantly differ.
- Discussion repeats overall eGFR decrease 12.7 over 5 years, expected age-only decrease 2-3 over 5 years, detectable difference 2.3, and stated surrogate threshold 0.75/year = 3.75/5 years. PDF p. 10 repeats 71% final serum and 83% any postrandomization serum.

## Table 1: baseline characteristics (PDF p. 5)

Columns, in order: D3+omega-3 n=370; D3+placebo n=333; omega-3+placebo n=289; two placebos n=320. Values are No. (%) unless noted; percentage denominator is nonmissing responses.

| Characteristic | 370 | 333 | 289 | 320 |
|---|---:|---:|---:|---:|
| Female / male | 184 (50) / 186 (50) | 143 (43) / 190 (57) | 131 (45) / 158 (55) | 151 (47) / 169 (53) |
| Age mean (SD), y | 67.4 (7.3) | 67.4 (6.7) | 68.2 (6.7) | 67.5 (6.9) |
| Race/ethnicity nonmissing N | 361 | 327 | 284 | 314 |
| Non-Hispanic white | 240 (66) | 211 (65) | 199 (70) | 207 (66) |
| Non-Hispanic black | 73 (20) | 75 (23) | 59 (21) | 71 (23) |
| Hispanic | 20 (6) | 21 (6) | 16 (6) | 18 (6) |
| Asian/Pacific Islander | 13 (4) | 8 (2) | 7 (2) | 7 (2) |
| American Indian/Alaska Native | 6 (2) | 4 (1) | 1 (<1) | 2 (1) |
| Other | 9 (2) | 8 (2) | 2 (1) | 9 (3) |
| More than high-school education | 303 (82) | 283 (85) | 243 (84) | 270 (85) |
| Diabetes duration <1 / 1-2 / 3-5 / 6-10 / 11-20 / >20 y | 13 (4) / 52 (14) / 78 (21) / 107 (29) / 90 (24) / 29 (8) | 15 (5) / 43 (13) / 72 (22) / 83 (25) / 82 (25) / 37 (11) | 5 (2) / 45 (16) / 62 (22) / 74 (26) / 69 (24) / 33 (11) | 9 (3) / 37 (12) / 78 (24) / 96 (30) / 74 (23) / 25 (8) |
| Current smoking / alcohol | 22 (6) / 191 (53) | 17 (5) / 184 (56) | 15 (5) / 151 (53) | 25 (8) / 168 (54) |
| Biguanides / sulfonylureas / insulin | 247 (67) / 109 (29) / 67 (18) | 222 (67) / 100 (30) / 68 (20) | 199 (69) / 85 (29) / 57 (20) | 221 (69) / 99 (31) / 66 (21) |
| Thiazolidinediones / DPP-4 inhibitors / GLP-1 agonists | 32 (9) / 33 (9) / 9 (2) | 32 (10) / 26 (8) / 14 (4) | 24 (8) / 22 (8) / 16 (6) | 36 (11) / 34 (11) / 9 (3) |
| Any antihypertensive; classes mean (SD) | 293 (80); 1.4 (1.2) | 263 (80); 1.4 (1.1) | 231 (81); 1.4 (1.1) | 258 (81); 1.4 (1.2) |
| ACE inhibitor or ARB / ACE inhibitor | 223 (60) / 163 (44) | 205 (62) / 148 (44) | 177 (61) / 121 (42) | 198 (62) / 133 (42) |
| Diuretic / beta-blocker / calcium-channel blocker / ARB / MRA | 111 (30) / 91 (25) / 75 (20) / 67 (18) / 2 (1) | 87 (26) / 74 (22) / 76 (23) / 64 (19) / 3 (1) | 82 (28) / 62 (21) / 58 (20) / 60 (21) / 0 | 84 (26) / 68 (21) / 66 (21) / 69 (22) / 4 (1) |
| Cholesterol lowering / vitamin D ≥800 IU/d / calcium ≥1200 mg/d | 250 (69) / 146 (39) / 84 (23) | 238 (73) / 138 (41) / 66 (20) | 199 (71) / 124 (43) / 81 (28) | 223 (71) / 128 (40) / 81 (25) |
| BMI mean (SD), kg/m² | 31.4 (6.5) | 31.8 (6.6) | 30.8 (6.6) | 31.6 (7.3) |
| Creatinine mean (SD), mg/dL | 0.8 (0.3) | 0.9 (0.3) | 0.8 (0.2) | 0.9 (0.2) |
| Cystatin C mean (SD), mg/L | 0.9 (0.3) | 0.9 (0.3) | 0.9 (0.3) | 0.9 (0.3) |
| Urine ACR median (IQR), mg/g | 2.9 (0.5-7.6) | 2.8 (0.5-8.8) | 2.9 (0.5-7.1) | 3.2 (1.0-6.7) |
| 25(OH)D mean (SD), ng/mL | 29.6 (10.6) | 29.0 (9.8) | 30.2 (10.3) | 30.1 (9.9) |
| 25(OH)D <20 / 20-<30 / ≥30 ng/mL | 62 (17) / 109 (31) / 184 (52) | 48 (15) / 121 (38) / 148 (47) | 41 (15) / 87 (32) / 146 (53) | 44 (14) / 116 (37) / 151 (49) |

## Figure 1 flow (PDF p. 6)

- Screening: 3244 assessed; 1932 excluded = 438 not meeting inclusion criteria + 1494 declined; 1312 randomized.
- Cell 370 D3+omega-3: 370 received/randomized/primary/adverse-event; 303 ≥1 blood after randomization; 259 complete case; 260 completed; 110 lost; 89 did not provide final blood; 21 died; 111 excluded from complete case (110 lost + 1 baseline eGFR missing).
- Cell 333 D3+placebo: 333 received/randomized/primary/adverse-event; 280 ≥1 blood; 236 complete case and completed; 97 lost; 78 no final blood; 19 died; 97 excluded (footnote: 1 of 97 also baseline eGFR missing).
- Cell 289 placebo+omega-3: 289 received/randomized/primary/adverse-event; 242 ≥1 blood; 211 complete case; 212 completed; 77 lost; 56 no final blood; 21 died; 78 excluded (77 lost + 1 baseline eGFR missing).
- Cell 320 two placebos: 320 received/randomized/primary/adverse-event; 265 ≥1 blood; 226 complete case and completed; 94 lost; 75 no final blood; 19 died; 94 excluded (footnote: 1 of 94 also baseline eGFR missing).

## Figure 2 and Table 2 primary eGFR results (PDF pp. 7-8)

- Figure 2 shows eGFR axes 0-200 mL/min/1.73 m² and ACR axes 0.1-10 000 mg/g on log scale. At times 0, 2, 5, contributors are vitamin-D/placebo eGFR 701/607, 531/459, 496/438; omega-3/placebo eGFR identical 701/607, 531/459, 496/438; vitamin-D/placebo ACR 702/609, 529/463, 505/440; omega-3/placebo ACR identical 702/609, 529/463, 505/440. Caption defines median/quartiles, 1.5×IQR whiskers/outliers, and counts as data contributors.
- Table 2 vitamin D: baseline active n=701 eGFR 86.3 (84.6-88.0), placebo n=607 85.3 (83.7-87.0); year 2 active n=531 eGFR 80.6 (78.8-82.4), change −5.2 (−6.2 to −4.2), placebo n=459 79.3 (77.3-81.2), change −6.1 (−7.1 to −5.1), difference 0.9 (−0.6 to 2.5); year 5 active n=496 74.3 (72.3-76.2), change −12.3 (−13.4 to −11.2), placebo n=438 72.5 (70.6-74.5), change −13.1 (−14.2 to −11.9), difference 0.9 (−0.7 to 2.5), P=.25.
- Table 2 omega-3: baseline active n=657 eGFR 85.7 (84.1-87.3), placebo n=651 86.0 (84.2-87.8); year 2 active n=499 79.4 (77.6-81.2), change −5.7 (−6.8 to −4.7), placebo n=491 80.6 (78.6-82.5), change −5.5 (−6.5 to −4.6), difference −0.3 (−1.8 to 1.3); year 5 active n=472 73.7 (71.8-75.6), change −12.2 (−13.3 to −11.1), placebo n=462 73.2 (71.1-75.3), change −13.1 (−14.2 to −12.0), difference 0.9 (−0.7 to 2.6), P=.27.
- Table 2 footnotes: positive difference means higher year-5 eGFR/slower decline active vs corresponding placebo; linear mixed model adjusts age, sex, baseline ACR and uses multiple imputation; values for changes are all participants with multiple imputation; P tests year-5 difference; four baseline eGFR values missing.

## Figures 3-4 subgroups (PDF pp. 8-9)

- Figure 3 vitamin-D vs placebo, displayed raw mean (SD) eGFR change active/placebo and participant count active/placebo: White 451 −12.1 (13.7) / 406 −11.7 (13.5); Black 148 −15.9 (16.0) /130 −14.7 (17.1); overall 703 −13.1 (14.4)/609 −12.3 (14.8); ACR <30:635 −12.4 (14.2)/559 −11.8 (14.4), ≥30:67 −20.4 (15.0)/50 −17.3 (17.4); eGFR ≥60:612 −14.1 (14.4)/531 −13.7 (14.5), <60:89 −5.8 (12.4)/76 −3.0 (13.6); omega-3 randomization placebo:333 −13.2 (14.9)/320 −13.0 (14.7), omega-3:370 −12.9 (13.9)/289 −11.7 (14.9); 25(OH)D <20:110 −14.6 (13.9)/85 −12.2 (17.1), 20-<30:230 −14.7 (15.2)/203 −12.4 (14.0), ≥30:332 −11.5 (13.9)/297 −12.3 (14.6); BMI <25:87 −12.9 (13.2)/87 −10.5 (11.7), 25-<30:228 −12.3 (14.1)/205 −12.2 (14.4), ≥30:364 −13.7 (15.0)/294 −12.8 (15.7). Interaction P values in native segment order: .58, .36, .15, .18, .79, .42; alignment to the six displayed subgroup families is layout-sensitive without a renderer.
- Figure 4 omega-3 vs placebo: baseline EPA/DHA ≤2.2%: active 332 −13.3 (15.0), placebo 347 −12.5 (14.6); >2.2:308 −12.9 (14.6), 292 −11.9 (14.4); overall 659 −13.1 (14.8), 653 −12.2 (14.5). ACR <30:596 −12.6 (14.8),598 −11.5 (13.8); ≥30:62 −18.1 (14.2),55 −19.1 (18.3). Fish <1.5/wk:354 −13.4 (15.3),329 −11.8 (14.7); ≥1.5/wk:295 −12.9 (14.3),310 −12.7 (14.3). hsCRP ≤0.2 mg/dL:334 −12.9 (14.3),335 −11.5 (13.4); >0.2:323 −13.3 (15.3),316 −13.0 (15.5). Vitamin-D placebo:289 −13.2 (14.9),320 −12.9 (13.9); vitamin-D:370 −13.0 (14.7),333 −11.7 (14.9). Interaction P values in native segment order: .72, .70, .73, .51, .42; association with the five subgroup families is layout-sensitive without a renderer. Both figure captions define estimates as adjusted active-placebo differences in change baseline-year 5 (age, sex, baseline ACR); Figure 3 adds BMI formula.

## Table 3 secondary outcomes (PDF p. 9)

Columns are active events/rate (95% CI), placebo events/rate (95% CI), active-minus-placebo incidence-rate difference (95% CI), HR (95% CI), P. Rates are per 100 person-years.

| Intervention and outcome | Active | Placebo | Rate difference | HR | P |
|---|---|---|---|---|---:|
| Vitamin D: ≥40% decline/kidney failure/death | 85; 2.5 (2.0-3.0) | 79; 2.7 (2.1-3.3) | −0.2 (−1.0 to 0.6) | 0.92 (0.68-1.25) | .61 |
| Vitamin D: ≥40% eGFR decline | 42; 1.6 (1.1-2.1) | 38; 1.7 (1.2-2.1) | −0.1 (−0.7 to 0.6) | 0.97 (0.63-1.51) | .90 |
| Vitamin D: ACR doubling and ≥30 mg/g | 111; 4.4 (3.6-5.2) | 74; 3.3 (2.5-4.0) | 1.1 (0.0-2.2) | 1.34 (1.00-1.80) | .05 |
| Omega-3: ≥40% decline/kidney failure/death | 86; 2.7 (2.2-3.3) | 78; 2.5 (1.9-3.0) | 0.3 (−0.5 to 1.1) | 1.11 (0.81-1.50) | .52 |
| Omega-3: ≥40% eGFR decline | 40; 1.6 (1.1-2.1) | 40; 1.6 (1.2-2.1) | 0.0 (−0.7 to 0.7) | 0.99 (0.64-1.54) | .97 |
| Omega-3: ACR doubling and ≥30 mg/g | 96; 4.0 (3.2-4.8) | 89; 3.7 (3.0-4.5) | 0.3 (−0.8 to 1.4) | 1.08 (0.81-1.44) | .60 |

Table 3 footnotes: prespecified outcomes and ACR alternative continuous analysis are defined above; HR is Cox model; eGFR outcomes exclude four baseline eGFR-missing participants and ACR outcome excludes one baseline ACR-missing participant; P tests HR=1.

## Mapping limitations

All 11 DOC-001 pages have usable page-addressable native text. No layout extraction or permitted renderer was available. Thus the Figure 3/4 interaction-P assignment and graphical plotted effect/CI coordinates cannot be mechanically tied to specific rows from the segment order alone; all printed raw counts/mean(SD) and P sequences are preserved above. This is a source-access limitation, not a candidate or judgment.
