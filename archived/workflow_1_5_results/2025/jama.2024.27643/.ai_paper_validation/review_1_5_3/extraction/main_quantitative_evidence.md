# Main-Paper Quantitative Evidence Map — DOC-001

## Scope, authority, and coverage

- **Source:** `DOC-001`, `jama_berry_2025_oi_240158_1742927563.7361.pdf`, PDF pp. 1-12.
- **Scope completed:** every assigned PDF page. Reused source-matched page-native text was used as a locator; direct `pdftotext -layout` extraction of all 12 PDF pages and direct visual inspection of PDF pp. 5-8 were used for authority/confirmation. The direct layout outputs are retained only under `preprocessing/main/` for this mapper.
- **Relationship-count convention:** 20 numeric/reporting relationships (`MN01`-`MN20`) and 19 inferential/statistical relationships (`MS01`-`MS19`) are mapped below, for 39 relationships total. Repeated appearances of the exact same result are cross-referenced rather than counted again. These are mapper-local identifiers for later stable-inventory assignment; they are not candidate IDs or judgments.
- **No diagnosis performed:** this is an evidence reconstruction only. No candidate, severity, validity, or adjudication label is assigned.

## Page-by-page applicability

| PDF page | Result-relevant content | Mapping status |
|---|---|---|
| 1 | Abstract: design, populations, intervention counts, primary result, adverse-event counts/percentages, conclusion | Mapped |
| 2 | Key Points and methods: trial design, 54 sites, dates, allocation ratio, outcomes | Mapped |
| 3 | Outcome scales, sample-size/power statement, analysis populations, model/test labels | Mapped |
| 4 | Statistical threshold/hierarchy; participant results, primary and secondary results | Mapped |
| 5 | Figure 1 participant flow | Mapped |
| 6 | Table 1 baseline values | Mapped |
| 7 | Figure 2/Table 2 survival results and exploratory time-to-event outcomes | Mapped |
| 8 | Figure 3 NfL results, safety, and opening Discussion text | Mapped |
| 9 | Discussion, limitations, conclusion, and article-information start | Mapped |
| 10 | Author contributions/disclosures; no applicable result relationship | No applicable result relationship |
| 11 | Disclosures/references; no applicable result relationship | No applicable result relationship |
| 12 | References; no applicable result relationship | No applicable result relationship |

## Population, scale, and analysis definitions

| ID | Exact PDF location | Direct source evidence and mapping |
|---|---|---|
| MN01 | [DOC-001 PDF p. 1](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=1>), Abstract; p. 2, Trial Design; p. 4, Trial Participants | Phase 2/3, multicenter, randomized, double-blind platform-trial regimen C at 54 US sites, July 2020-March 2022, final follow-up March 17, 2022. Of 161 regimen-randomized participants, CNM-Au8 had 120 (61 at 60 mg daily; 59 at 30 mg daily) and regimen-specific placebo had 41. An additional 123 concurrently randomized placebo participants from other regimens were combined in analyses; the shared placebo group is 164 in Table 1/Figure 1 but has 162 in the death/PAV time-to-event denominator because two lacked follow-up. |
| MN02 | [PDF p. 1](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=1>), Abstract; [PDF p. 2](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=2>), Key Points/interventions | Allocation was 3:3:2 (CNM-Au8 60 mg : CNM-Au8 30 mg : matching placebo), each for 24 weeks. The primary combined-dose contrast is CNM-Au8 30/60 mg pooled versus shared placebo; regimen-only contrasts use the 41 regimen-C placebos. |
| MN03 | [PDF p. 2](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=2>), Outcomes; [PDF p. 3](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=3>), Primary/secondary methods | Primary endpoint: change from baseline through week 24 in disease severity based on ALSFRS-R and survival, via a Bayesian shared parameter model. The disease rate ratio (DRR) is the ratio of ALSFRS-R slopes in the function component or HR in the survival component; DRR <1 indicates benefit/slowing. ALSFRS-R total is 0-48, higher is better. Secondary endpoints: CAFS joint-rank test (higher rank is better), SVC in percent predicted normal (PPN; higher is better), and survival free of PAV. |
| MS01 | [PDF p. 3](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=3>), Sample Size Calculation | Simulation-based sample-size statement: 160 per regimen, 3:1 active:placebo randomization with shared concurrently enrolling controls, approximately 80% power to detect 30% slowing in ALS progression common to mortality/function, at 1-sided type-I error <2.5%. |
| MS02 | [PDF p. 3](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=3>), analysis methods; [PDF p. 4](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4>), hierarchy | CAFS used Wilcoxon rank-sum. SVC used repeated-measures linear mixed and random-slopes models, centered covariates: symptom-onset months, prebaseline ALSFRS-R slope (delta-FRS), baseline riluzole/edaravone and interactions with time. Death/PAV used Cox proportional hazards adjusted for prebaseline slope, symptom-onset months, baseline riluzole/edaravone, age; PAV is ventilation >22 h/day for >7 consecutive days. Primary Bayesian success criterion was posterior probability DRR <1 of >=0.979. If primary significant, sequential secondary testing was CAFS, SVC, survival at two-tailed P <.05; after first failed endpoint, lower endpoints could not be declared significant. Nominal secondary P values are unadjusted. |

## Participant flow and completion

| ID | Exact PDF location | Population/time/contrast | Printed quantities and matching claim |
|---|---|---|---|
| MN04 | [PDF p. 4](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4>), Trial Participants; [PDF p. 5](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=5>), Figure 1 | Master-protocol screening to focal regimen | Figure 1: 815 assessed; 128 excluded (121 did not meet inclusion/met exclusion criteria, 4 terminated early in screening, 2 withdrew consent, 1 timed out). Of 163 last assigned to focal regimen, 2 excluded (1 died, 1 timed out), leaving 161 randomized within focal regimen. Narrative matches: 163 screened, 1 died before regimen screening visit, 1 timed out, 161 randomized. |
| MN05 | [PDF p. 5](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=5>), Figure 1 | Focal regimen, 24-week follow-up | Randomized: 59 CNM-Au8 30 mg, 61 CNM-Au8 60 mg, 41 placebo. Discontinued follow-up: 4 (3 terminated early, 1 died), 6 (2 terminated early, 3 died, 1 withdrew), and 6 (2 terminated early, 3 died, 1 withdrew, 1 lost), respectively. Completed 24-week follow-up: 55, 55, and 35, respectively. All 59, 61, and 41 were included in primary analysis. |
| MN06 | [PDF p. 5](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=5>), Figure 1; [PDF p. 4](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4>) | Shared controls | Other regimens: 524 last assigned; 32 excluded (10 timed out, 9 declined consent, 7 terminated early, 5 did not meet criteria, 1 died); 123 randomized to placebo and 369 to active regimen. The 164 shared-placebo randomized group shown in the figure includes 41 regimen-C placebo plus 123 other-regimen placebo. The 164-placebo branch had 27 discontinue follow-up (17 terminated early, 3 died, 2 withdrew, 3 lost, 2 study terminated by sponsor), 137 completed 24 weeks, and 164 included in primary analysis. |
| MN07 | [PDF p. 1](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=1>), Abstract; [PDF p. 4](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4>) | Trial completion/assigned drug | Abstract: 145/161 (90%) regimen-randomized participants completed trial. Narrative: within the analysis population, completed on assigned drug: placebo 85%, CNM-Au8 92%, 30 mg 93%, 60 mg 90%. Before week 24, trial drug was discontinued by 5 placebo and 6 active (3 each dose); RCT deaths were 1 regimen placebo, 1 at 30 mg, and 3 at 60 mg. |

## Baseline Table 1 — every displayed quantitative value

**Exact source location:** [DOC-001 PDF p. 6, Table 1](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=6>). Columns are CNM-Au8 30 mg (n=59), CNM-Au8 60 mg (n=61), shared placebo (n=164), and regimen-specific placebo (n=41). Values are no. (%) unless marked mean (SD) or median (IQR). Shared placebo includes regimen-specific placebo plus other-regimen shared placebos. Race was unknown/unreported for 3 participants and ethnicity for 1.

| ID | Characteristic | 30 mg | 60 mg | Shared placebo | Regimen-specific placebo |
|---|---|---:|---:|---:|---:|
| MN08 | Female; male | 26 (44.1); 33 (55.9) | 23 (37.7); 38 (62.3) | 49 (29.9); 115 (70.1) | 12 (29.3); 29 (70.7) |
| MN09 | Race: Asian; Black/African American; White; multiple races | blank; blank; 59 (100.0); blank | blank; blank; 61 (100.0); blank | 2/160 (1.2); 6/160 (3.8); 151/160 (94.4); 1/160 (0.6) | blank; 2 (4.9); 38 (92.7); 1 (2.4) |
| MN10 | Not Hispanic or Latino | 56 (94.9) | 60/60 (100.0) | 157/163 (96.3) | 38 (92.7) |
| MN11 | Age, mean (SD), y; BMI, mean (SD) | 57.7 (10.2); 27.4 (5.3) | 58.6 (9.9); 26.6 (4.8) | 57.2 (11.3); 27.3 (5.0) | 57.0 (11.7); 28.4 (5.5) |
| MN12 | Bulbar onset | 10 (16.9) | 8 (13.1) | 29 (17.7) | 6 (14.6) |
| MN13 | El Escorial: clinically definite; clinically probable; clinically probable laboratory-supported; clinically possible ALS | 28 (47.5); 22 (37.3); 8 (13.6); 1 (1.7) | 30 (49.2); 21 (34.4); 8 (13.1); 2 (3.3) | 66 (40.2); 40 (24.4); 42 (25.6); 16 (9.8) | 14 (34.1); 10 (24.4); 16 (39.0); 1 (2.4) |
| MN14 | King's stage: 1; 2; 3; 4a/4b nutritional failure; 4b respiratory failure | 3 (5.1); 18 (30.5); 22 (37.3); 1 (1.7); 15 (25.4) | 10 (16.4); 18 (29.5); 19 (31.1); blank; 14 (23.0) | 34 (20.7); 39 (23.8); 45 (27.4); 1 (0.6); 45 (27.4) | 9 (22.0); 11 (26.8); 7 (17.1); blank; 14 (34.1) |
| MN15 | Baseline riluzole use; edaravone use | 45 (76.3); 12 (20.3) | 49 (80.3); 16 (26.2) | 126 (76.8); 41 (25.0) | 32 (78.0); 10 (24.4) |
| MN16 | Months since symptom onset, mean (SD); months since diagnosis, mean (SD) | 21.2 (8.6); 9.8 (5.2) | 24.2 (8.5); 11.1 (6.6) | 21.9 (8.7); 10.3 (6.1) | 21.9 (8.5); 10.0 (5.6) |
| MN17 | SVC PPN, mean (SD); ALSFRS-R total, bulbar, fine motor, gross motor, combined motor, respiratory mean (SD) | 74.4 (16.0); 34.5 (5.8), 9.8 (2.1), 7.3 (2.7), 7.2 (2.8), 14.4 (4.9), 10.3 (2.4) | 76.0 (16.3); 34.0 (7.3), 10.0 (2.5), 6.9 (3.4), 6.7 (3.2), 13.6 (5.7), 10.5 (2.0) | 76.0 (16.5); 35.1 (6.7), 10.0 (2.3), 7.6 (3.1), 7.3 (3.1), 14.9 (5.4), 10.2 (2.1) | 76.1 (16.8); 36.1 (5.91), 10.6 (2.1), 7.8 (3.4), 7.3 (2.8), 15.1 (5.4), 10.3 (2.0) |
| MN18 | Prebaseline ALSFRS-R slope, points/month mean (SD); serum NfL median (IQR), pg/mL; plasma NfL median (IQR), pg/mL | 0.8 (0.6); 67.6 (44.3-91.6); 92.2 (59.7-120.6) | 0.7 (0.5); 62.5 (44.4-95.1); 75.0 (51.0-110.9) | 0.7 (0.4); NA; NA | 0.6 (0.4); 51.6 (33.0-76.4); 75.7 (48.5-105.8) |

Table 1 footnotes define BMI as kg/m²; PPN as percent predicted normal; NfL as neurofilament light; ALSFRS-R scores range 0-48 with higher scores indicating better function. The narrative on [PDF p. 4](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4>) reports mean age 57.7 years, 37.9% female, 98% non-Hispanic/Latino White among regimen-randomized participants, and summarizes pooled active versus shared-placebo clinical categories (definite ALS 48% vs 40%; possible/probable laboratory-supported 16% vs 35%; King's stage 1 11% vs 21%) and BMI 27.0 versus 28.4.

## Primary and secondary efficacy

| ID | Exact location | Population, outcome, time, model/contrast | Printed result and matching claim |
|---|---|---|---|
| MS03 | [PDF p. 1](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=1>), Abstract; [PDF p. 2](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=2>), Key Points; [PDF p. 4](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4>), Primary Efficacy; [PDF p. 7](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=7>), Figure 2 | Week 24 primary Bayesian shared-parameter model; combined 30/60-mg CNM-Au8 versus shared placebo | DRR 0.97, 95% CrI 0.783-1.175; posterior probability DRR <1 = 0.65. Narrative/abstract says no benefit or harm/no significant benefit. Figure 2A labels adjusted modeled ALSFRS-R progression and uses shared placebo, pooled CNM-Au8, regimen-C placebo. |
| MS04 | [PDF p. 4](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4>) | Regimen-only primary sensitivity/alternate contrast | DRR 0.96, 95% CrI 0.709-1.357, limiting placebo to within-regimen placebo participants. |
| MS05 | [PDF p. 4](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4>) | Bayesian functional and mortality model | Estimated ALSFRS-R mean slope: shared placebo -1.03 points/month (95% CrI -1.176 to -0.892); pooled active -1.00 (95% CrI -1.153 to -0.858). Model-estimated mortality event rate: 0.007 events/month shared placebo and 0.006 pooled active. |
| MS06 | [PDF p. 4](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4>) | Secondary CAFS, shared placebo vs pooled active | Mean rank 143.9 shared placebo and 140.5 pooled CNM-Au8; P=.51. Sensitivity analysis adjusted for baseline NfL: P=.88. |
| MS07 | [PDF p. 4](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4>) | Secondary SVC over 24 weeks, PPN/month, pooled active vs shared placebo | Reported mean change: pooled active -9.32 PPN/month (30 mg -7.84; 60 mg -10.79) vs shared placebo -8.53; difference -0.78 PPN/month (95% CI -4.25 to 2.68). Baseline-NfL sensitivity: pooled active -1.73 (95% CI -2.18 to -1.29) vs placebo -1.55 (95% CI -1.94 to -1.17). |
| MS08 | [PDF p. 4](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4>); [PDF p. 7](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=7>), Table 2/Figure 2B | Death or PAV to week 24 and adjusted Cox model | Proportions: 1/59 (30 mg), 4/61 (60 mg), 9/162 shared placebo. Four of 41 regimen placebos and two shared placebos were excluded from time-to-event analysis for no follow-up (one PAV at baseline; one early termination at baseline). Pooled active vs shared placebo adjusted HR 0.46 (95% CI 0.12-1.49); baseline-NfL sensitivity HR 0.45 (95% CI 0.11-1.50). |

## Table 2 and Figure 2 — survival and graphical denominators

**Exact source locations:** [DOC-001 PDF p. 7, Figure 2 and Table 2](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=7>). Table 2 is PAV-free survival, adjusted Cox regression. Its footnote says models adjust for age, sex, symptom-onset time, prebaseline ALSFRS-R slope, baseline riluzole and baseline edaravone; CIs use profile log-likelihood.

| ID | Contrast | Observed proportions (active; placebo) | Adjusted HR (95% CI) | P value |
|---|---|---|---|---:|
| MS09 | Pooled CNM-Au8 vs shared placebo | 5/120; 9/162 | 0.46 (0.12-1.49) | .22 |
| MS10 | CNM-Au8 30 mg vs shared placebo | 1/59; 9/162 | 0.06 (0.002-0.56) | .04 |
| MS11 | CNM-Au8 60 mg vs shared placebo | 4/61; 9/162 | 0.96 (0.25-3.08) | .95 |
| MS12 | Pooled CNM-Au8 vs regimen-C placebo | 5/120; 4/41 | 0.25 (0.05-1.09) | .06 |
| MS13 | CNM-Au8 30 mg vs regimen-C placebo | 1/59; 4/41 | 0.03 (0.0004-0.36) | .03 |
| MS14 | CNM-Au8 60 mg vs regimen-C placebo | 4/61; 4/41 | 0.47 (0.10-2.16) | .32 |

Figure 2A has ALSFRS-R risk counts at weeks 0, 4, 8, 12, 16, 20, 24: shared placebo 154, 151, 148, 147, 145, 140, 140; pooled CNM-Au8 115, 115, 111, 112, 109, 110, 111; regimen-C placebo 37, 36, 36, 37, 35, 35, 34. Figure 2B exposed participants at weeks 0, 4, 8, 12, 16, 20, 24, 28 are shared placebo 164, 162, 162, 160, 158, 155, 115, 0 with events 1, 0, 0, 1, 2, 3, 2, 1; pooled active 120, 120, 120, 120, 118, 115, 91, 1 with events 0, 0, 0, 0, 2, 3, 0, 0. Panel A excludes ALSFRS-R data after death/PAV; panel B depicts death/PAV solid Kaplan-Meier and dashed model-estimated exponential curves.

## Exploratory time-to-event, biomarker, safety, and narrative results

| ID | Exact location | Population/outcome/contrast | Printed result and matching narrative claim |
|---|---|---|---|
| MS15 | [PDF p. 6](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=6>) | Additional exploratory time-to-event analyses, active vs regimen placebo | Assisted ventilation: 16 active (18%) vs 9 placebo (31%), HR 0.40 (95% CI 0.17-1.01). Gastrostomy: 14 (12%) vs 7 (17%), HR 0.37 (0.14-1.04). First ALS-related-SAE hospitalization: 5 (4%) vs 3 (7%), HR 0.23 (0.04-1.33). First SAE hospitalization: 14 (12%) vs 7 (18%), HR 0.48 (0.18-1.33). Narrative calls these exploratory and says other analysis populations did not show statistically significant differences. |
| MS16 | [PDF p. 8](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=8>), Figure 3/text | Serum NfL, baseline to week 24, regimen placebo vs pooled active | Serum: placebo geometric mean +30.8%, 43.1 to 56.5 pg/mL; pooled active +0.4%, 60.6 to 60.8 pg/mL; treatment difference -23.2% geometric mean ratio (95% CI -39.5% to -2.5%), P=.03. Figure 3 has evaluable counts active 112/107/97/95 at weeks 0/8/12/24 and placebo 39/32/33/33. Values were natural-log transformed; shown difference is least-squares means and percentages are back-transformed. |
| MS17 | [PDF p. 8](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=8>), Figure 3/text | Serum NfL post hoc sensitivity | Excluding very low values (<4 pg/mL or <2% of a participant maximum) excluded 1 baseline placebo observation. Geometric mean change was +0.8% active and +11.6% placebo; difference -9.7% (95% CI -18.5% to 0.1%), P=.05. Narrative says magnitude, not direction, was sensitive to an outlier. |
| MS18 | [PDF p. 8](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=8>), Figure 3/text | Plasma NfL, baseline to week 24, regimen placebo vs pooled active | Placebo geometric mean +7.9%, 72.8 to 78.5 pg/mL; pooled active -2.3%, 80.3 to 78.5 pg/mL; treatment difference -9.5% geometric mean ratio (95% CI -17.8% to -0.4%), P=.04. Figure 3 displays -9.5% (95% CI -17.8% to -0.5%), P=.04, and evaluable counts active 118/111/110/105 at weeks 0/4/8/24; placebo 41/38/35/34. Caption says plasma was assessed baseline, weeks 4, 8, 16, 24 and serum baseline, weeks 8, 12, 16, 24. |
| MN19 | [PDF p. 8](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=8>) | Safety population, trial-period treatment-emergent AEs | Safety population: 120 received CNM-Au8 and 163 shared-placebo participants. At least one treatment-emergent AE: 93% pooled active vs 90% shared placebo. AEs >=5 percentage points more common with active: diarrhea 19% vs 7%, nausea 14.2% vs 8.6%; >=5 points less common: fatigue 10.8% vs 18.4%, muscular weakness 20% vs 27.6%. These values match the abstract counts: diarrhea 23/120 (19%) vs 12/163 (7%); nausea 17/120 (14.2%) vs 14/163 (8.6%); fatigue 12/120 (10.8%) vs 30/163 (18.4%); muscular weakness 24/120 (20%) vs 45/163 (27.6%). |
| MS19 | [PDF p. 8](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=8>) | Serious treatment-emergent AEs | Serious treatment-emergent AE percentages: 9% shared placebo, 10% 30 mg, 16% 60 mg, 17% regimen placebo; P=.31. No SAEs and no deaths were considered related to trial drug. |
| MN20 | [PDF p. 9](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=9>), Discussion/Conclusion | Matching narrative claims | Discussion says the 24-week RCT did not demonstrate slowing with pooled or individual doses and no benefit on key secondary endpoints at 24 weeks. It calls survival analyses hypothesis-generating and states 13 total RCT-period events in shared placebo plus pooled active. It describes exploratory estimates as not statistically significant and notes many exploratory outcomes lacked multiplicity control. Limitations identify 24-week duration and a CNM-Au8 elimination half-life of 28 days. Conclusion says CNM-Au8 did not improve the primary efficacy outcome in this 24-week RCT. |

## Explicit no-applicable units and extraction limitations

- PDF pp. 10-12 were directly checked. They contain author contributions/disclosures and references; no new result-relevant count, estimate, interval, P value, model output, or matching results claim is present. PDF p. 9 contains the mapped Discussion, limitations, conclusion, and the start of article information.
- No OCR was needed: native text was readable; direct PDF visual confirmation was performed for layout-sensitive pp. 5-8.
- This map records the exact printed Figure 3 plasma-CI endpoint difference between its caption/text (text `-0.4%`) and figure annotation (`-0.5%`) as source evidence without a diagnostic judgment; subsequent checkers must retain both exact locations and apply their own scope.
