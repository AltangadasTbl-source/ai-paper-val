# DOC-001 Main-Article Quantitative Evidence Map

## Scope, authority, and mapping convention

- **Direct source:** `jama_debar_2025_oi_250046_1755300121.13587.pdf` (14 PDF pages).
- **Mapped scope:** every PDF page 1-14. Direct PDF native/layout extraction was inspected for the complete page range; the reusable normalized text, page map, and rendered pages were used as locators/transcription aids. The direct PDF is authoritative.
- **Location convention:** `PDF pN` is the supplied PDF page; `JAMA pNNN` is the printed page where printed. A table or figure location refers to the supplied PDF page that contains it.
- **Relationship IDs:** `N` = numeric/reporting relationship; `S` = inferential/statistical relationship. These are local, complete mapping labels, not candidate IDs or judgments. Repeated narrative/abstract occurrences are listed under the same relationship where they describe the same population, time, contrast, and model.
- **Groups:** PT = online painTRAINER; HC = health coach; UC = usual care plus. Randomized/primary-analysis population: PT 776, HC 778, UC 777; total 2331 unless a table supplies a different analysis denominator.

## Complete page coverage

| PDF page | Principal content and quantitative mapping status | Relationship labels / no-applicable record |
|---:|---|---|
| 1 | Abstract: randomized population, baseline summary, primary 3-month adjusted results and conclusion | N001-N002; matched inferential result S009 |
| 2 | Introduction and Methods eligibility context | N003; no result estimate table |
| 3 | Randomization, outcome definitions, scales, and time points | N004-N006; S003 |
| 4 | Sample-size/statistical model description; Results flow, adherence, baseline summary, primary-results lead-in | N007-N012; S004-S005 |
| 5 | Figure 1 participant flow and detailed footnotes | N011-N013 |
| 6 | Table 1 baseline characteristics, first portion | N014-N016 |
| 7 | Table 1 continuation/footnotes; primary narrative and secondary-results narrative | N017-N018; S005-S007 |
| 8 | Figure 2; adverse events; Discussion quantitative claims | N019-N020; S008 |
| 9 | Table 2 adjusted binary primary/secondary outcomes, RRs, omnibus P values, NNTs and footnotes | S009-S017 |
| 10 | Table 3 continuous outcomes: pain severity/intensity/interference, social role, physical function | S018-S032 |
| 11 | Table 3 continuation: PGIC pain/general and definitions | S033-S038 |
| 12 | Discussion/conclusions and article information; no new result-relevant numeric relationship beyond mapped results | NO_APPLICABLE_NEW_RESULT_RELATIONSHIP |
| 13 | References only | NO_APPLICABLE_RESULT_RELATIONSHIP |
| 14 | References only | NO_APPLICABLE_RESULT_RELATIONSHIP |

## Population, outcome, and analysis definitions

| ID | Direct observations and exact source locations |
|---|---|
| N001 | **Trial population and allocation.** The abstract reports 2331 eligible randomized individuals: mean age 58.8 years (SD 14.3), 1712 (74%) women, and 1030 (44%) rural/medically underserved; HC n=778, PT n=776, UC n=777. The trial enrolled from January 2021-February 2023, with follow-up concluding April 2024. **Locations:** PDF p1/JAMA p592, Abstract; PDF p4/JAMA p595, Results; Table 1, PDF pp6-7/JAMA pp597-598. |
| N002 | **Abstract matched primary result.** At 3 months adjusted percentages attaining a >=30% pain-severity decrease were HC 32.0% (95% CI 29.3%-35.0%), PT 26.6% (23.4%-30.2%), UC 20.8% (18.0%-24.0%); HC vs UC RR 1.54 (1.30-1.82), PT vs UC RR 1.28 (1.06-1.55), HC vs PT RR 1.20 (1.03-1.40). **Location:** PDF p1/JAMA p592, Abstract Results. Matched Table 2 record: S009. |
| N003 | **Eligibility/scales relevant to denominators.** Adults had high-impact chronic pain and PEG score >=12 (PEG: 3 items, each 0-10, total 0-30; higher=worse); screening criteria also include other clinical exclusions. **Locations:** PDF p2/JAMA p593, Methods; Figure 1 footnote a, PDF p5/JAMA p596. |
| N004 | **Randomization and stratification.** Individual 1:1:1 allocation was stratified by sex, baseline pain severity (<7 vs >=7), clinical site, and rural/medically underserved residence; random permuted blocks of 3, 6, or 9. **Location:** PDF p3/JAMA p594, Methods; Figure 1 footnote b, PDF p5/JAMA p596. |
| N005 | **Outcome/time/scale definitions.** Primary outcome is >=30% decrease from prerandomization baseline to 3 months in 11-item BPI-SF pain severity (mean of 11 items, range 0-10; higher=worse); 6 and 12 months are secondary primary-outcome time points. Pain intensity is the 4-item BPI-SF subscale and interference is the 7-item subscale, both range 0-10. **Location:** PDF p3/JAMA p594, Main Outcomes/Primary and Secondary Outcomes; Table 2 footnotes f-i, PDF p9/JAMA p600. |
| N006 | **Other continuous outcome scales.** PROMIS Social Roles 4a and Physical Function 6b are standardized T scores (mean 50, SD 10; higher=better; <=40 denotes moderate-to-severe limitation); PGIC pain and general are 1-7, where 1=much better, 4=no change, 7=much worse. **Locations:** PDF p3/JAMA p594, Secondary Outcomes; Table 3 footnotes f-i, PDF p11/JAMA p602. |
| N007 | **Design target.** Planned n=2331 (777/group), 90% power to detect a 7.5% difference (RR 1.5) for each intervention versus UC at a 15% UC outcome rate and 80% retention; multiple comparisons controlled with Fisher least significant difference; 10,000 simulations used modified Poisson regression. **Location:** PDF p4/JAMA p595, Sample Size. |
| S003 | **Stated statistical methods.** Binary outcomes used modified Poisson regression for adjusted RRs/95% CIs and GEE with working independence/robust sandwich SEs. Models included group, time, and group×time, adjusted for baseline pain severity, stratification variables, multisite pain, and co-occurring mental health condition. Adjusted percentages are centered at mean covariates; NNT=1/(difference in adjusted percentage). Continuous outcomes used linear GEE for adjusted means, differences, and SMDs; SMD=adjusted difference divided by UC SD of change at the time point. Tests were two-sided, alpha=.05. **Location:** PDF p4/JAMA p595, Statistical Analysis. |

## Participant flow, follow-up, baseline, and safety

| ID | Direct observations and exact source locations |
|---|---|
| N008 | **Screening/enrollment narrative.** Of 7628 screened, 2331 were eligible and randomized and 2210 completed the trial. Main exclusions named: 2993 no high-impact chronic pain and 411 recent/current behavioral treatment. **Location:** PDF p4/JAMA p595, Results. |
| N009 | **Follow-up/adherence narrative.** Any follow-up: PT 643/776 (83%), HC 690/778 (89%), UC 703/777 (90%). Three-month completion: PT 70%, HC 82%, UC 80%. At least one session: PT 527 (68%), HC 660 (85%); >=6 sessions: PT 371 (43%), HC 548 (70%). **Location:** PDF p4/JAMA p595, Results. |
| N010 | **Baseline summary narrative.** Almost 40% were >=65 years; 74% women; 75% White non-Hispanic; 44% rural/medically underserved; 33% had any negative social determinant. Mean musculoskeletal conditions 2.5 (SD 1.3), 73% had multiple conditions, 25.5% pain severity >=7, 47.8% depression, 27.8% moderate-to-severe anxiety, 43.3% moderate-to-severe sleep disturbance, and long-term opioid treatment 9.6% among sites reporting pharmacy data. **Location:** PDF p4/JAMA p595, Results. |
| N011 | **Figure 1 recruitment flow.** 62,125 mailed; 54,497 excluded before screening (36,656 unreachable; 17,803 declined screening; 38 deceased); 7628 screened; 4481 ineligible: 2993 no high-impact chronic pain, 245 PEG <12, and 1243 one-or-more further reasons (411 behavioral treatment, 273 planned surgery, 189 no internet/telephone, 121 non-English speaking, 95 cognitive/hearing impairment, 34 substance-use treatment). Then 3147 eligible; 672 excluded (339 declined, 333 unreachable); 2475 consented; 142 excluded (118 unreachable, 24 declined baseline); 2333 randomized. **Location:** Figure 1, PDF p5/JAMA p596. |
| N012 | **Figure 1 allocation, sessions, follow-up and attrition.** Randomized: PT 776; HC 778; UC 779 (777 mailed guide; 2 randomized in error, excluded because they did not meet EHR eligibility). PT: 371 completed 6-8 sessions, 156 completed 1-5, 249 none; HC: 548, 112, 118, respectively. 3/6/12-month completions: PT 542/547/583, HC 635/621/639, UC 621/622/639. Any follow-up: 643/690/703. Withdrawn: 43/45/16; died: 3/7/7. Included in primary analysis: 776/778/777. **Location:** Figure 1, PDF p5/JAMA p596. |
| N013 | **Figure 1 additional provider/attrition context.** Twelve HC providers; median patients/provider 69 (IQR 52-76; range 24-110). Figure footnote specifies follow-up assessment regardless of sessions and notes people who died/withdrew may have completed prior follow-up. **Location:** Figure 1 footnotes d, f, g, PDF p5/JAMA p596. |
| N014 | **Table 1 baseline characteristics—demographics.** PT/HC/UC respectively: age mean (SD) 58.8 (13.9)/58.8 (14.5)/58.8 (14.3); age >=65: 291/776 (37.5)/305/778 (39.2)/304/777 (39.1); female 571/776 (73.6)/572/778 (73.5)/569/777 (73.2); male 205/776 (26.4)/206/778 (26.5)/208/777 (26.8). College degree+ 332/770 (43.1)/347/767 (45.2)/344/770 (44.7); not employed 400/769 (52.0)/416/771 (54.0)/418/769 (54.4); income <$50,000 266/671 (39.6)/217/643 (33.7)/251/681 (36.9); married/partnered 484/761 (63.6)/512/768 (66.7)/511/771 (66.3). **Location:** Table 1, PDF p6/JAMA p597. |
| N015 | **Table 1 baseline characteristics—race/residence/social determinants.** PT/HC/UC: American Indian/Alaska Native 6/751 (0.8)/11/760 (1.4)/11/755 (1.5); Asian 10/751 (1.3)/6/760 (0.8)/11/755 (1.5); Black non-Hispanic 119/751 (15.8)/118/760 (15.5)/113/755 (15.0); Hispanic 21/751 (2.8)/26/760 (3.4)/30/755 (4.0); Native Hawaiian/Pacific Islander 1/751 (0.1)/0/760/1/755 (0.1); White non-Hispanic 573/751 (76.3)/572/760 (75.3)/554/755 (73.4); >=1 race 21/751 (2.8)/27/760 (3.6)/35/755 (4.6). Rural/medically underserved 340/776 (43.8)/345/778 (44.3)/345/777 (44.4); any negative social determinant 261/763 (34.2)/231/766 (30.2)/266/769 (34.6); financial strain 198/770 (25.7)/170/771 (22.0)/199/771 (25.8); housing instability 134/766 (17.5)/101/763 (13.2)/129/767 (16.8); food insecurity 116/769 (15.1)/100/773 (12.9)/117/768 (15.2); transportation insecurity 57/772 (7.4)/56/774 (7.2)/57/773 (7.4). **Location:** Table 1, PDF p6/JAMA p597. |
| N016 | **Table 1 baseline characteristics—pain/treatment/conditions.** PT/HC/UC: pain severity >=7: 195/776 (25.1)/199/778 (25.6)/200/777 (25.7); pain duration >5 years 532/775 (68.6)/536/778 (68.9)/541/777 (69.6); hip/knee/foot 494/776 (63.7)/487/778 (62.6)/495/777 (63.7); back 402/775 (51.9)/401/777 (51.6)/422/777 (54.3); hand/arm/shoulder 298/774 (38.5)/301/778 (38.7)/284/777 (36.6); neck 202/776 (26.0)/207/778 (26.6)/213/777 (27.4); widespread 141/775 (18.2)/176/775 (22.7)/143/777 (18.4); headache/migraine 95/775 (12.3)/131/778 (16.8)/117/777 (15.1); abdominal/pelvic/genital 58/775 (7.5)/73/777 (9.4)/66/775 (8.5); toothache/jaw 37/776 (4.8)/54/777 (6.9)/52/777 (6.7). Musculoskeletal conditions median (IQR) 2.0 (1-3) each; encounters median (IQR) 6.0 (3-12)/6.0 (3-13)/6.0 (3-11); long-term opioid use 43/569 (7.6)/60/566 (10.6)/60/562 (10.7). **Location:** Table 1, PDF p6/JAMA p597. |
| N017 | **Table 1 baseline characteristics—health conditions and outcomes.** PT/HC/UC: anxiety/depression diagnosis 300/776 (38.7)/322/778 (41.4)/343/777 (44.1); moderate/severe depression 373/775 (48.1)/373/777 (48.0)/370/777 (47.6); anxiety 206/774 (26.6)/218/778 (28.0)/224/777 (28.8); sleep disturbance 332/772 (43.0)/331/775 (42.7)/342/772 (44.3); substance-use disorder 31/776 (4.0)/31/778 (4.0)/24/777 (3.1); Charlson median (IQR) 0.0 (0-1.25)/1.0 (0-2)/1.0 (0-2). Baseline pain severity mean (SD) 5.8 (1.6)/5.9 (1.7)/5.9 (1.6); intensity 5.4 (1.6)/5.6 (1.7)/5.5 (1.6); interference 6.0 (1.9)/6.0 (1.9)/6.1 (1.9); social limitation 258/758 (34.0)/283/770 (36.8)/277/765 (36.2); physical limitation 563/764 (73.7)/566/770 (73.5)/580/773 (75.0). **Location:** Table 1, PDF pp6-7/JAMA pp597-598. |
| N018 | **Table 1 denominator/definition qualifiers.** Missing values are excluded from denominators; most measures marked c/d are self-report. EHR-based items and coding/scale cut points are defined in Table 1 footnotes. Long-term opioid use is reported for 3 of 4 sites because Essentia EHR data could not be reported. **Location:** Table 1 footnotes, PDF p7/JAMA p598. |
| N019 | **Safety/adverse events.** Hospitalizations: 183 participants (7.9%) and 247 events. UC 63 participants/82 events (8.1%), PT 55/81 (7.1%), HC 65/84 (8.4%). Deaths: 17 (0.7%): UC 7 (0.9%), PT 3 (0.4%), HC 7 (0.9%). No hospitalization/death was identified as related/possibly related. Patient-initiated adverse events: HC 16 (2.0%), PT 1 (0.1%), UC 0; nonserious events were not systematically collected. **Location:** PDF p8/JAMA p599, Adverse Events. |
| N020 | **Figure 2 observed assessment Ns.** Plot values are adjusted percentages (Table 2); observed numbers at 3/6/12 months are UC 621/622/639, PT 542/547/583, HC 635/621/639. The primary outcome is at 3 months; whiskers are 95% CIs. **Location:** Figure 2, PDF p8/JAMA p599. |

## Binary primary and secondary outcome relationships (Table 2)

**Shared direct observations/labels (S009-S017):** Table 2 analysis Ns are PT 643, HC 690, UC 703 (participants with any follow-up). Percentages, RRs, and NNTs are adjusted; adjusted percentage/RR use modified Poisson GEE and mean covariate distribution. Omnibus P is the 3-group Wald test; pairwise comparisons are to be compared only if omnibus P<.05 under least-significant-difference approach. NNT is 1 over the adjusted percentage difference; CIs crossing zero can yield the stated nonsensical/infinite NNT interpretation. **Location:** Table 2 and footnotes a-e, PDF p9/JAMA p600.

| ID | Outcome/time; adjusted percentage PT / HC / UC (95% CI) | PT vs UC RR; HC vs UC RR; HC vs PT RR (95% CI); omnibus P | NNT PT vs UC; HC vs UC; HC vs PT (95% CI) | Matched occurrences |
|---|---|---|---|---|
| S009 | **Primary pain severity, 3 mo:** 26.6 (23.4-30.2) / 32.0 (29.3-35.0) / 20.8 (18.0-24.0) | 1.28 (1.06-1.55); 1.54 (1.30-1.82); 1.20 (1.03-1.40); <.001 | 18 (10-71); 9 (7-14); 19 (11-102) | Abstract PDF p1; primary narrative PDF p7; Figure 2 PDF p8; Table 2 PDF p9 |
| S010 | **Secondary pain severity, 6 mo:** 32.9 (29.5-36.7) / 37.1 (34.1-40.5) / 22.9 (20.0-26.1) | 1.44 (1.21-1.70); 1.62 (1.39-1.90); 1.13 (0.98-1.30); <.001 | 10 (7-19); 8 (6-11); 24 (12-186) | Table 2 PDF p9; primary narrative PDF p7 |
| S011 | **Secondary pain severity, 12 mo:** 35.9 (32.4-39.7) / 38.3 (36.8-39.9) / 27.1 (24.1-30.5) | 1.32 (1.13-1.54); 1.41 (1.25-1.59); 1.07 (0.96-1.19); <.001 | 12 (8-26); 9 (7-13); 41 (17-76) | Table 2 PDF p9; primary narrative PDF p7 |
| S012 | **Pain intensity, 3 mo:** 24.3 (21.2-27.8) / 27.0 (24.0-30.5) / 17.7 (15.1-20.7) | 1.37 (1.12-1.69); 1.53 (1.26-1.86); 1.11 (0.93-1.33); <.001 | 16 (10-43); 11 (8-20); 37 (14-57) | Table 2 PDF p9 |
| S013 | **Pain intensity, 6 mo:** 26.9 (23.7-30.5) / 31.8 (28.3-35.7) / 21.1 (18.3-24.3) | 1.27 (1.06-1.54); 1.51 (1.26-1.80); 1.18 (1.00-1.40); <.001 | 18 (10-76); 10 (7-17); 21 (11-5524) | Table 2 PDF p9 |
| S014 | **Pain intensity, 12 mo:** 32.1 (28.7-35.8) / 33.7 (31.2-36.3) / 26.4 (23.4-29.8) | 1.21 (1.03-1.43); 1.28 (1.11-1.47); 1.05 (0.92-1.20); .003 | 18 (10-106); 14 (9-31); 63 (18-38) | Table 2 PDF p9 |
| S015 | **Pain-related interference, 3 mo:** 30.6 (27.3-34.4) / 35.6 (33.7-37.6) / 23.4 (20.5-26.8) | 1.31 (1.10-1.55); 1.52 (1.32-1.75); 1.16 (1.02-1.32); <.001 | 14 (9-40); 9 (7-12); 21 (12-100) | Table 2 PDF p9 |
| S016 | **Pain-related interference, 6 mo:** 37.0 (33.5-40.9) / 40.9 (37.0-45.1) / 24.3 (21.3-27.6) | 1.52 (1.30-1.79); 1.68 (1.43-1.98); 1.10 (0.96-1.27); <.001 | 8 (6-13); 7 (5-9); 26 (11-67) | Table 2 PDF p9 |
| S017 | **Pain-related interference, 12 mo:** 39.6 (36.1-43.5) / 42.3 (40.6-44.0) / 30.6 (27.4-34.2) | 1.29 (1.12-1.49); 1.38 (1.23-1.55); 1.07 (0.97-1.18); <.001 | 12 (8-25); 9 (7-13); 39 (16-79) | Table 2 PDF p9 |

## Continuous secondary outcome relationships (Table 3)

**Shared direct observations/labels (S018-S038):** Table 3 values are adjusted mean change from baseline (95% CI), adjusted between-group mean difference (95% CI), and adjusted SMD (95% CI). SMD uses the UC SD of change at that time. Omnibus P is a 3-group Wald test, and stated pairwise-comparison condition is omnibus P<.05. Outcome-specific analysis Ns are: pain severity/intensity/interference PT/HC/UC=643/690/703; social roles=636/683/696; physical function=639/684/699; PGIC pain/general=640/687/702. **Locations:** Table 3 and footnotes, PDF pp10-11/JAMA pp601-602.

In each following row, group change is `PT / HC / UC`; adjusted differences are `PT-UC; HC-UC; HC-PT`; SMDs use the same contrast order.

| ID | Outcome/time; group adjusted change (95% CI) | Differences (95% CI); P | SMDs (95% CI) |
|---|---|---|---|
| S018 | Pain severity 3 mo: -1.2 (-1.3 to -1.0) / -1.2 (-1.3 to -1.1) / -0.8 (-0.9 to -0.6) | -0.4 (-0.6 to -0.2); -0.4 (-0.6 to -0.3); -0.0 (-0.2 to 0.1); <.001 | -0.25 (-0.28 to -0.02); -0.34 (-0.36 to -0.13); -0.13 (-0.15 to 0.08) |
| S019 | Pain severity 6 mo: -1.3 (-1.4 to -1.1) / -1.4 (-1.5 to -1.3) / -0.9 (-1.0 to -0.8) | -0.4 (-0.6 to -0.2); -0.5 (-0.7 to -0.4); -0.1 (-0.3 to 0.1); <.001 | -0.26 (-0.34 to -0.08); -0.36 (-0.43 to -0.19); -0.12 (-0.19 to 0.04) |
| S020 | Pain severity 12 mo: -1.5 (-1.6 to -1.3) / -1.4 (-1.6 to -1.3) / -1.1 (-1.2 to -0.9) | -0.4 (-0.6 to -0.2); -0.4 (-0.6 to -0.2); 0.0 (-0.2 to 0.2); <.001 | -0.25 (-0.24 to 0.01); -0.36 (-0.35 to -0.12); -0.11 (-0.11 to 0.12) |
| S021 | Pain intensity 3 mo: -0.9 (-1.0 to -0.8) / -0.9 (-1.0 to -0.8) / -0.6 (-0.7 to -0.5) | -0.3 (-0.5 to -0.1); -0.3 (-0.5 to -0.2); -0.0 (-0.2 to 0.2); <.001 | -0.21 (-0.21 to -0.01); -0.29 (-0.30 to -0.11); -0.08 (-0.09 to 0.09) |
| S022 | Pain intensity 6 mo: -1.0 (-1.1 to -0.9) / -1.1 (-1.2 to -1.0) / -0.7 (-0.9 to -0.6) | -0.2 (-0.4 to -0.1); -0.3 (-0.5 to -0.2); -0.1 (-0.3 to 0.1); <.001 | -0.17 (-0.23 to -0.06); -0.27 (-0.32 to -0.17); -0.04 (-0.10 to 0.05) |
| S023 | Pain intensity 12 mo: -1.1 (-1.3 to -1.0) / -1.1 (-1.3 to -1.0) / -0.9 (-1.0 to -0.8) | -0.2 (-0.4 to -0.1); -0.2 (-0.4 to -0.1); 0.0 (-0.2 to 0.2); .01 | -0.16 (-0.16 to 0.00); -0.27 (-0.26 to -0.12); -0.03 (-0.03 to 0.11) |
| S024 | Pain interference 3 mo: -1.3 (-1.4 to -1.1) / -1.4 (-1.5 to -1.2) / -0.8 (-1.0 to -0.7) | -0.5 (-0.7 to -0.3); -0.5 (-0.7 to -0.3); -0.1 (-0.3 to 0.2); <.001 | -0.25 (-0.28 to -0.03); -0.34 (-0.37 to -0.13); -0.13 (-0.15 to 0.07) |
| S025 | Pain interference 6 mo: -1.5 (-1.6 to -1.3) / -1.6 (-1.8 to -1.4) / -1.0 (-1.1 to -0.8) | -0.5 (-0.7 to -0.3); -0.6 (-0.8 to -0.4); -0.1 (-0.4 to 0.1); <.001 | -0.27 (-0.34 to -0.08); -0.37 (-0.44 to -0.19); -0.14 (-0.21 to 0.04) |
| S026 | Pain interference 12 mo: -1.6 (-1.8 to -1.5) / -1.6 (-1.8 to -1.5) / -1.2 (-1.3 to -1.0) | -0.5 (-0.7 to -0.3); -0.5 (-0.7 to -0.3); 0.0 (-0.2 to 0.2); <.001 | -0.26 (-0.25 to 0.01); -0.37 (-0.36 to -0.11); -0.12 (-0.12 to 0.12) |
| S027 | Social role 3 mo: 1.5 (1.0 to 2.1) / 2.2 (1.7 to 2.7) / 0.7 (0.3 to 1.2) | 0.8 (0.0 to 1.5); 1.5 (0.8 to 2.2); 0.7 (-0.0 to 1.4); <.001 | 0.12 (-0.23 to 0.11); 0.01 (-0.12 to -0.00); 0.20 (0.29 to 0.19) |
| S028 | Social role 6 mo: 2.2 (1.6 to 2.8) / 2.5 (2.0 to 3.1) / 1.0 (0.5 to 1.5) | 1.2 (0.4 to 1.9); 1.5 (0.8 to 2.2); 0.3 (-0.4 to 1.1); <.001 | 0.18 (-0.23 to -0.05); 0.06 (-0.11 to -0.06); 0.26 (0.30 to 0.15) |
| S029 | Social role 12 mo: 2.6 (2.0 to 3.2) / 2.7 (2.2 to 3.3) / 1.4 (0.8 to 1.9) | 1.3 (0.5 to 2.1); 1.4 (0.6 to 2.1); 0.1 (-0.7 to 0.9); .001 | 0.19 (-0.21 to 0.01); 0.07 (-0.09 to -0.10); 0.27 (0.28 to 0.12) |
| S030 | Physical function 3 mo: 1.4 (1.1 to 1.8) / 1.7 (1.4 to 2.1) / 1.0 (0.7 to 1.4) | 0.4 (-0.1 to 0.9); 0.7 (0.2 to 1.2); 0.3 (-0.2 to 0.8); .02 | 0.09 (-0.16 to 0.07); -0.02 (-0.05 to -0.04); 0.16 (0.22 to 0.15) |
| S031 | Physical function 6 mo: 2.0 (1.6 to 2.4) / 1.8 (1.4 to 2.1) / 1.4 (1.0 to 1.7) | 0.6 (0.1 to 1.2); 0.4 (-0.1 to 0.9); -0.3 (-0.8 to 0.3); .05 | 0.15 (-0.09 to -0.06); 0.02 (-0.03 to -0.18); 0.22 (0.16 to 0.05) |
| S032 | Physical function 12 mo: 2.2 (1.8 to 2.7) / 2.1 (1.7 to 2.5) / 1.3 (0.9 to 1.7) | 0.9 (0.3 to 1.5); 0.8 (0.2 to 1.4); -0.1 (-0.7 to 0.5); .004 | 0.20 (-0.18 to -0.03); 0.07 (-0.04 to -0.16); 0.27 (0.25 to 0.09) |
| S033 | PGIC pain 3 mo: 2.2 (2.1 to 2.3) / 2.0 (1.9 to 2.1) / 2.9 (2.8 to 3.0) | -0.7 (-0.8 to -0.6); -0.9 (-1.0 to -0.8); -0.2 (-0.3 to -0.1); <.001 | -0.62 (-0.81 to -0.19); -0.62 (-0.76 to -0.25); -0.37 (-0.51 to -0.05) |
| S034 | PGIC pain 6 mo: 2.2 (2.1 to 2.3) / 2.1 (2.0 to 2.2) / 2.8 (2.7 to 2.9) | -0.6 (-0.8 to -0.5); -0.7 (-0.8 to -0.5); -0.1 (-0.2 to 0.1); <.001 | -0.54 (-0.59 to -0.05); -0.55 (-0.60 to -0.16); -0.29 (-0.33 to 0.06) |
| S035 | PGIC pain 12 mo: 2.2 (2.1 to 2.3) / 2.2 (2.1 to 2.4) / 2.8 (2.7 to 2.9) | -0.6 (-0.8 to -0.5); -0.6 (-0.7 to -0.4); 0.1 (-0.1 to 0.2); <.001 | -0.55 (-0.50 to 0.05); -0.57 (-0.54 to -0.08); -0.29 (-0.25 to 0.14) |
| S036 | PGIC general 3 mo: 2.0 (1.9 to 2.1) / 1.6 (1.5 to 1.7) / 2.7 (2.6 to 2.8) | -0.7 (-0.8 to -0.6); -1.1 (-1.2 to -1.0); -0.4 (-0.5 to -0.3); <.001 | -0.66 (-1.04 to -0.38); -0.66 (-0.98 to -0.42); -0.40 (-0.67 to -0.18) |
| S037 | PGIC general 6 mo: 2.1 (2.0 to 2.2) / 1.8 (1.7 to 1.9) / 2.5 (2.5 to 2.6) | -0.5 (-0.6 to -0.3); -0.7 (-0.9 to -0.6); -0.2 (-0.4 to -0.1); <.001 | -0.46 (-0.69 to -0.24); -0.50 (-0.70 to -0.32); -0.24 (-0.41 to -0.07) |
| S038 | PGIC general 12 mo: 2.0 (1.9 to 2.1) / 1.9 (1.8 to 2.0) / 2.6 (2.5 to 2.7) | -0.6 (-0.7 to -0.4); -0.7 (-0.8 to -0.5); -0.1 (-0.3 to 0.0); <.001 | -0.53 (-0.64 to -0.11); -0.58 (-0.67 to -0.22); -0.28 (-0.36 to 0.03) |

## Matched narrative claims and mapping notes

| ID | Direct observation, source location, and relationship cross-reference |
|---|---|
| S004 | **Primary-outcome narrative.** Groups differed at 3 months (P<.001); narrative reproduces UC 20.8% (18.0%-24.0%), PT 26.6% (23.4%-30.2%), and HC 32.0% (29.3%-35.0%). **Location:** PDF p4/JAMA p595. Matched S009. |
| S005 | **Secondary narrative.** The article states both active groups had better secondary pain/function outcomes at 3 months persisting over 12 months, with modest attenuation; it specifies 3-month pain-severity SMD PT -0.26 and HC -0.36 versus UC. **Location:** PDF p7/JAMA p598. Matched S018 (Table 3 printed SMDs are separately transcribed exactly there). |
| S006 | **Primary narrative RRs.** PT vs UC RR 1.28 (1.06-1.55), HC vs UC 1.54 (1.30-1.82), HC vs PT 1.20 (1.03-1.40). At 6 and 12 months, HC vs PT is stated no longer significant. **Location:** PDF p7/JAMA p598. Matched S009-S011. |
| S007 | **Table-3/narrative linkage.** Narrative says continuous secondary-outcome patterns were similar, and gives 3-month pain-severity SMD PT -0.26, HC -0.36. **Location:** PDF p7/JAMA p598. Full printed continuous outcomes S018-S038. |
| S008 | **Discussion/conclusion numeric time claim.** Discussion and conclusion describe greater pain-severity improvement at 3 months, sustained through 6 and 12 months; the conclusion does not print a new estimate. **Locations:** PDF pp8,12/JAMA pp599,603. Cross-reference S009-S011 and S018-S038. |

## Mapping limitations and boundaries

- PDF p9-11 table text is rotation-sensitive in raw native extraction. Canonical coordinate-reconstructed reusable text and direct-source rendered-page inspection were used to map the printed table values. No OCR substitution was used as authority.
- Pages 12-14 contain no newly reported study-result relationship requiring an additional `N`/`S` item; their coverage is explicit in the page table.
- This is an evidence map only. It reports observations and cross-references without a consistency diagnosis, candidate selection, or judgment.
