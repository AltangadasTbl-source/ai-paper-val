### F-NUM-002

**Observation:** A post hoc paragraph assigns counts and pooled-population percentages to two randomized arms.

**Exact source locations and document roles:** REPORT [main article physical p.6, Post Hoc Outcomes, first paragraph](../../../../jama_azoulay_2018_oi_180109.pdf#page=6). REPORT [p.5, Patients](../../../../jama_azoulay_2018_oi_180109.pdf#page=5) and [p.3, Figure 1](../../../../jama_azoulay_2018_oi_180109.pdf#page=3) establish randomized 389/389 and analyzed 388/388, pooled 776. Relationships N059, N008, N009; corresponding main mapper S059.

**Printed inputs:** “In the overall population,” vasopressors and renal replacement therapy needed in 153 patients(19.7%) randomized to H and 31 patients(4%) randomized to C; no statistical difference between groups. Both analysis arms 388; randomized arms 389.

**Rule and calculation:** H 153/388=39.4330%; half-unit interval[39.2535,39.6129]% versus printed 19.7 interval[19.65,19.75]%, relative gap 19.5035/19.7=.990027. C 31/388=7.9897%; half-unit interval[7.8507,8.1290]% versus printed integer 4 interval[3.5,4.5]%, relative gap 3.3507/4=.837677. Using 389 randomized denominators instead of 388 does not remove either discrepancy. Conversely,153/776=19.7165% with half-unit interval[19.6394,19.7937]% and 31/776=3.9948% with interval[3.9279,4.0619]%, both overlapping printed percentages. The count order could therefore belong to two therapies in the overall population rather than to two randomized groups; the printed sentence explicitly attaches them to the groups.

**Focus area:** A, counts and denominators.
**Proposed review domain:** statistical_results.
**Proposed relationship:** S_W; all relationships S_W.
**Qualifying route:** Route A, category 3.
**Affected result or extracted value:** Group-specific vasopressor and renal replacement counts/risks during follow-up and their attribution to the randomized intervention.
**Why context does not resolve it:** An always-register within-paragraph count/denominator/percentage conflict is reproduced. The pooled denominator reproduces the percentages, but does not identify which therapies and arm-specific quantities the sentence is reporting.
**Alternatives:** 153 and 31 might be overall counts for vasopressors and renal replacement, respectively, with arm labels attached in the sentence; alternatively they could be genuine arm counts with pooled percentages. The source provides no independent arm-by-therapy table to distinguish them. The statement of no group difference is retained; it is not recomputed under an assumed event cross-tabulation.
**Exact human question:** Do 153(19.7%) and 31(4%) describe vasopressors and renal replacement therapy in the entire 776-patient population, or separate randomized groups, and what are the arm-specific therapy counts and denominators?

### F-NUM-003

**Observation:** Figure 3 binary subgroup counts leave unreconciled denominators and events compared with its “All patients” rows.

**Exact source locations and document roles:** REPORT [main article physical p.7, Figure 3A and 3 B](../../../../jama_azoulay_2018_oi_180109.pdf#page=7), PaO2:FIO2<200 and≥200 rows in both arms/both panels; hematologic malignancy No and Yes rows in H in both panels; All patients rows. REPORT [p.4, Table 1, hematologic malignancy](../../../../jama_azoulay_2018_oi_180109.pdf#page=4) confirms 167 H and 181 C among 388/arm. REPORT [p.3, Statistical Analysis](../../../../jama_azoulay_2018_oi_180109.pdf#page=3) states no participants excluded from analyses because of missing/incomplete data; it gives no subgroup-specific available-case rule. Numeric relationships N072, N076; main mapper S033, S034, S041, S042, S046, S047, S054, S055.

**Printed inputs:** All patients H 138/388, C 140/388 deaths; H 150/388, C 170/388 IMV. PaO2:FIO2 subgroups: H denominators 237+65, C 251+35; deaths H 99+16, C 95+10; IMV H 99+27, C 117+13. Hematologic malignancy H denominators 199+167, deaths 66+64, IMV61+78. The same subgroup denominators recur in both panels.

**Rule and calculation:** Sum the half-unit intervals for each two-category partition; compare with the half-unit All patients value. This consolidates the same unaccounted subgroup-population pattern across both panels.

| Displayed comparison | Central subgroup sum versus All patients | Sum interval | All-patient interval | Relative gap |
|---|---|---|---|---:|
| PaO2:FIO2 H denominator, panels A and B | 237+65=302 versus 388 | [301,303] | [387.5,388.5] |84.5/388=.217784|
| PaO2:FIO2 C denominator, panels A and B |251+35=286 versus 388|[285,287]|[387.5,388.5]|100.5/388=.259021|
| PaO2:FIO2 H deaths, panel A |99+16=115 versus 138|[114,116]|[137.5,138.5]|21.5/138=.155797|
| PaO2:FIO2 C deaths, panel A |95+10=105 versus 140|[104,106]|[139.5,140.5]|33.5/140=.239286|
| PaO2:FIO2 H IMV, panel B |99+27=126 versus 150|[125,127]|[149.5,150.5]|22.5/150=.150000|
| PaO2:FIO2 C IMV, panel B |117+13=130 versus 170|[129,131]|[169.5,170.5]|38.5/170=.226471|
| Hematologic malignancy H denominator, panels A and B |199+167=366 versus 388|[365,367]|[387.5,388.5]|20.5/388=.052835|
| Hematologic malignancy H IMV, panel B |61+78=139 versus 150|[138,140]|[149.5,150.5]|9.5/150=.063333|

H No hematologic malignancy would be 388−167=221, with subtraction interval[220,222], whereas printed 199 allows[198.5,199.5]; gap 20.5/199=.103015. The other subgroup partitions (ICU timing, oxygen flow, catecholamines, unknown diagnosis) reproduce both all-patient denominators and event counts. Standard-arm hematologic and H hematologic-death subtotals also differ numerically, but their relative half-unit gaps do not exceed 0.05; they are recorded once in excluded observations.

**Focus area:** A, counts and denominators.
**Proposed review domain:** statistical_results.
**Proposed relationship:** S_W; all relationships S_W.
**Qualifying route:** Route A, category 3.
**Affected result or extracted value:** PaO2:FIO2 and hematologic-malignancy subgroup analysis populations and their day-28 death/IMV event counts.
**Why context does not resolve it:** Counts within the same result display do not reconcile above the prescribed threshold. Binary partitions are printed alongside all-patient totals; the caption supplies no missing-covariate stratum, restricted population definition, or accounting for the absent patients/events.
**Alternatives:** The partitions may be available-case analyses with missing subgroup-defining variables, despite the report's general no-exclusion statement, or may represent a restricted diagnostic population. This could explain some count deficits but is not a supplied definition. A count transcription or alternate subgroup definition is another possibility. No raw-data inference about which patients are missing is made.
**Exact human question:** Which analysis populations and missing-covariate rules underlie the PaO2:FIO2 and hematologic-malignancy subgroup rows, and how do their displayed denominators and events account for the all-patient totals in Figure 3?

### F-NUM-004

**Observation:** The same all-patient IMV counts are accompanied by contrasting HR directions in Table 2 and Figure 3B.

**Exact source locations and document roles:** REPORT [main article physical p.5, Table 2, invasive mechanical ventilation](../../../../jama_azoulay_2018_oi_180109.pdf#page=5), REPORT [p.6, Secondary Outcomes, first paragraph](../../../../jama_azoulay_2018_oi_180109.pdf#page=6), and REPORT [p.7, Figure 3B, All patients row and favors labels](../../../../jama_azoulay_2018_oi_180109.pdf#page=7). REPORT [p.4, Statistical Analysis](../../../../jama_azoulay_2018_oi_180109.pdf#page=4) describes high-flow versus standard-oxygen Cox effect estimates for the subgroup display. Relationships N065, N077; main mapper S015, S056, S057.

**Printed inputs:** H 150/388 andC170/388 IMV in both displays. Table 2 and narrative cause-specific HR0.85(95%CI0.68–1.06). Figure 3B All patients HR1.17(0.94–1.46). Figure labels HR<1 as favoring H andHR>1 as favoring C. There is no explicit alternative numerator/reference statement in its caption.

**Rule and calculation:** Compare matched all-patient results and direction/reference labels, not Cox versus crude ratios. Table 2 HR interval from display precision[.845,.855]; Figure 3 HR[1.165,1.175]; interval gap.310, relative gap.310/.85=.364706>0.05. Lower limits[.675,.685] versus[.935,.945] have relative gap.250/.68=.367647; upper limits[1.055,1.065] versus[1.455,1.465] have relative gap.390/1.06=.367925. Inverting Table 2 gives 1/.85=1.17647 and reciprocalCI[1/1.06,1/.68]=[.94340,1.47059], approximately matching Figure 3. This is a diagnostic about contrast reversal, not proof of the computation used and not a proposed correction.

**Focus area:** B, direction and estimate identity; C, which Cox contrast produces the reported number.
**Proposed review domain:** statistical_results.
**Proposed relationship:** S_W; all relationships S_W.
**Qualifying route:** Route B.
**Affected result or extracted value:** The all-patient day-28 IMV hazard ratio and its treatment/reference direction, which could be extracted as 0.85 or 1.17.
**Why context does not resolve it:** The printed population, event counts and outcome match, while HR directions reverse and Figure 3 uses the same favors convention as a high-flow/standard contrast. A different Cox estimand or reference coding is not defined alongside the figure. Reversing reference coding would also require reconciling its favors labels.
**Alternatives:** Figure 3 could reverse treatment coding, or use a different hazard/competing-event model from the cause-specific model explicitly named in Table 2. The source does not specify a distinct all-patient model in Figure 3. No crude event ratio is used to demand numerical equality with a Cox estimate.
**Exact human question:** What event model and treatment/reference coding produced Figure 3B's all-patient HR1.17(0.94–1.46), and how should its direction and favors labels be reconciled with Table 2 and the narrative HR0.85(0.68–1.06)?

### F-XS-002

The forest plots use effect directions that do not reconcile with the corresponding overall IMV HR and their favors labels.

- **Locations and roles:** REPORT [main p.5, Table 2 IMV](../../../../jama_azoulay_2018_oi_180109.pdf#page=5); REPORT [main p.6, Secondary Outcomes](../../../../jama_azoulay_2018_oi_180109.pdf#page=6); REPORT [main p.7, Figure 3A and3B, all13 rows of each panel, headings/axes/caption](../../../../jama_azoulay_2018_oi_180109.pdf#page=7). Keys S015, S031–S057.
- **Printed values:** Table 2/narrative IMV 150/388 versus170/388, HR .85(.68, 1.06). Figure 3B repeats150/388 versus170/388 but HR 1.17(.94, 1.46); its left side favors HFNO and right side favors standard. Figure 3A all-patient HR 1.02(.81, 1.29) versus Table 2 mortality.98(.77, 1.24). Affected Figure 3 rows in both panels are ICU-time0–1/≥2, PaO2/FiO2<200/≥200, flow≤9/>9, catecholaminesNo/Yes, unknown diagnosisNo/Yes, hematologic malignancyNo/Yes, and all patients.
- **Calculation and precision:** IMV copied-HR intervals [.845, .855] and[1.165, 1.175] have gap .310; relative discrepancy.310/.85=.3647. Reciprocating the Table 2 HR interval yields point[1.1696, 1.1834], lower-limit range approximately[.9390, .9479], upper-limit range[1.4599, 1.4815], consistent with the forest's printed reciprocal reading. This is a reference-direction diagnostic, not a crude-risk replacement of Cox. The mortality .98/1.02 numerical copy alone falls below5% and is not independently registered; it supports the recurring reference pattern. Subgroup curves/raw times are unavailable, so no subgroup Cox recomputation is asserted.
- **Focus area:** B. **Proposed review domain:** statistical_results. **Relationship type:** S_W. **All relationships:** S_W.
- **Qualifying route:** Route A, category2.
- **Affected result or extracted value:** Direction/reference of all Figure 3 mortality and IMV forest estimates, especially overall IMV 1.17(.94, 1.46) versus.85(.68, 1.06).
- **Why context does not resolve it:** Category2 applies to the reproduced overall IMV reversal. The printed favors labels invite the opposite interpretation from a reciprocal contrast; they do not identify a reference change.
- **Supported alternatives:** Figure 3 may use standard/HFNO while Table 2 uses HFNO/standard; in that case its favors headings require clarification. A different model is possible but not described as a different overall comparison.
- **Exact human question:** Which treatment is the numerator/reference in each Figure 3 panel, and should the figure's HRs and favors headings be interpreted with the same contrast as Table 2?

### F-XS-007

The planned longitudinal joint analyses are not supplied alongside the reported symptom and oxygenation results.

- **Locations and roles:** PLAN [p.55, lines 825–826](../../../../joi180109supp1_prod.pdf#page=55), [p.82, lines 1314–1315](../../../../joi180109supp1_prod.pdf#page=82), [p.105, lines 1745–1747](../../../../joi180109supp1_prod.pdf#page=105); REPORT [main p.4, Wilcoxon methods](../../../../jama_azoulay_2018_oi_180109.pdf#page=4), [p.6, oxygenation/comfort/dyspnea results](../../../../jama_azoulay_2018_oi_180109.pdf#page=6); REPORT [supplement p.4, eFigure 2](../../../../joi180109supp2_prod.pdf#page=4) and [p.5, eFigure 3](../../../../joi180109supp2_prod.pdf#page=5). Keys S-P 2-026, S312, P4-20, S008, S023, S024, R4-05, R4-06, R4-07.
- **Printed specifications:** Plan longitudinal oxygenation, dyspnea and comfort joint models accounting for right censoring. Article Wilcoxon rank-sum for symptom scores, nonsignificance at each time and oxygenation advantage untilday4; supplement displays repeated observations without joint-model results.
- **Comparison logic:** All three are abstract-reported key secondary outcomes. Complete supplied reports contain no named joint-model result. Wilcoxon symptom tests and time-specific graphs do not reproduce the planned longitudinal censoring-aware analysis. No graph-bar confidence convention is assumed. Precision not applicable.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route A, category5.
- **Affected result or extracted value:** Interpretation of oxygenation benefit and null comfort/dyspnea effects as prespecified longitudinal analyses versus time-specific comparisons.
- **Why context does not resolve it:** Category5 applies to the absent planned key-secondary joint analyses.
- **Supported alternatives:** Joint models may underlie an unlabelled oxygenation comparison; alternatively they were replaced by available-case/time-specific tests. Neither model components nor joint estimates are supplied.
- **Exact human question:** Were the prespecified joint longitudinal models for oxygenation, dyspnea and comfort fitted, and where are their estimates or the documented replacement analysis?

### F-XS-008

The planned ICU-stay survival and survivor/decedent analyses are not reported.

- **Locations and roles:** PLAN [p.54, lines 822–824](../../../../joi180109supp1_prod.pdf#page=54), [p.82, lines 1311–1313](../../../../joi180109supp1_prod.pdf#page=82), [p.105, lines 1742–1745](../../../../joi180109supp1_prod.pdf#page=105); REPORT [main p.4, Wilcoxon ICU-stay method](../../../../jama_azoulay_2018_oi_180109.pdf#page=4), [p.5, Table 2](../../../../jama_azoulay_2018_oi_180109.pdf#page=5), [p.6, secondary outcomes](../../../../jama_azoulay_2018_oi_180109.pdf#page=6). Keys S-P 2-025, S311, P4-19, S008, S019.
- **Printed specifications/values:** Plan ICU stay overall and separately in survivors/deceased, using Kaplan–Meier and competing-risk estimators. Report Wilcoxon, aggregate medians 8(4–14)/6(4–13), mean difference .6(−1, 2.2), P .07; Table 2 says stay effect could not be expressed byHR.
- **Comparison logic:** ICU stay is abstract-reported key secondary. No supplied survivor/decedent results or planned survival/competing-risk ICU-stay estimates accompany the aggregate Wilcoxon result. Absence is anchored to explicit planned analyses; precision not applicable.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route A, category5.
- **Affected result or extracted value:** ICU-stay effect and its handling of mortality-associated stay distributions.
- **Why context does not resolve it:** Category5 applies; a pooled stay summary does not supply the planned subgroup/estimator results.
- **Supported alternatives:** Planned separate/survival analyses may be available elsewhere or replaced; the plan's former/latter wording leaves estimator allocation unclear, but the entire specified strategy is absent rather than clarified by report.
- **Exact human question:** Were the planned overall and survivor/decedent ICU-stay analyses with Kaplan–Meier/competing-risk estimators performed, and where are their results or documented replacement?

### F-XS-010

The initially prespecified intubated-mortality analysis receives post hoc status in the report.

- **Locations and roles:** PLAN [p.38, secondary objectives including post-intubation mortality](../../../../joi180109supp1_prod.pdf#page=38), [p.45, lines 675–676](../../../../joi180109supp1_prod.pdf#page=45), [p.47, line 699](../../../../joi180109supp1_prod.pdf#page=47), [p.103, secondary list](../../../../joi180109supp1_prod.pdf#page=103); REPORT [main p.4, secondary exploratory and intubated-subset post hoc methods](../../../../jama_azoulay_2018_oi_180109.pdf#page=4), [p.6, Post Hoc Outcomes](../../../../jama_azoulay_2018_oi_180109.pdf#page=6), [p.8, secondary exploratory statement](../../../../jama_azoulay_2018_oi_180109.pdf#page=8). Keys S-P 2-003, S-P 2-010, P4-12, S010, S026.
- **Printed specifications/values:** Initial plan explicitly prespecifies intubated-patient day 28 mortality and labels mortality after HFNO versus control secondary. Report calls intubated-subset analyses post hoc, displaying55.3%/52.3%, RD 3(−8.5, 14.5), P .65. The final plan omits this endpoint from its seven named secondary outcomes.
- **Comparison logic:** Compare analysis/outcome status item by item. Intubated mortality occurs prospectively in initial plan despite report post hoc classification. This is status, not a numeric discrepancy; rounding not applicable. The separate multiplicity-related exploratory wording is excluded below because endpoints remain explicitly secondary in the report.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route A, category5.
- **Affected result or extracted value:** Prespecification/status of intubated mortality55.3% versus52.3%, RD 3(−8.5, 14.5), P .65.
- **Why context does not resolve it:** Category5 applies to outcome/analysis status changes. The report discloses different initial secondary endpoints and explains exploratory interpretation, but those disclosures do not supply the status correspondence for each analysis.
- **Supported alternatives:** Intubated mortality may have been removed before final plan and reintroduced post hoc. The report discloses earlier secondary endpoint revisions, but does not identify the status history of this matching analysis.
- **Exact human question:** Was the initially prespecified secondary intubated-mortality analysis removed before being reintroduced as the reported post hoc analysis, and where is that status change documented?

### F-XS-014

Two subgroup analyses described as predefined are not contained in the supplied prospective plans.

- **Locations and roles:** REPORT [main p.7, Figure 3 title and unknown-diagnosis/hematologic-malignancy rows inA/B](../../../../jama_azoulay_2018_oi_180109.pdf#page=7); REPORT [main p.4, subgroup methods](../../../../jama_azoulay_2018_oi_180109.pdf#page=4); PLAN [p.45, complete subgroup list](../../../../joi180109supp1_prod.pdf#page=45), [p.53, interaction statement](../../../../joi180109supp1_prod.pdf#page=53), [p.82, interaction strategy](../../../../joi180109supp1_prod.pdf#page=82), [p.98, final stratification list start](../../../../joi180109supp1_prod.pdf#page=98), [p.99, final list continuation](../../../../joi180109supp1_prod.pdf#page=99), [p.104, subsets-defined-above statement](../../../../joi180109supp1_prod.pdf#page=104). Keys S009, S039–S042, S052–S055, S-P 2-010, S-P 2-016, S308, P4-06, P4-15, P4-17.
- **Printed statements:** Figure 3 calls its mortality/IMV groups predefined and includes unknown diagnosisNo/Yes and hematologic malignancyNo/Yes; the latterIMV interactionP=.01 and effects1.61(1.16, 2.23)/.89(.65, 1.22). Initial complete subgroup list includes oxygenation, other organ failure, peri-intubation, postextubation, intubated andDNI. Final list specifiesICUtime, oxygenflow, shock; final analysis refers to subsets defined above. No plan text prespecifies diagnosis or hematologic-malignancy interactions.
- **Comparison logic:** Search/match complete supplied plan inventory and source-linked subgroup paragraphs; compare explicit predefinition claim to absence from all supplied prospective subgroup lists. A broad intention to analyze intubation predictors is not a prespecified named treatment interaction. Precision not applicable to prespecification status.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route A, category5.
- **Affected result or extracted value:** Prespecification of unknown-diagnosis and hematologic-malignancy mortality/IMV subgroups, especially hematologic-malignancyIMV interactionP=.01.
- **Why context does not resolve it:** Category5 applies to analyses described as prespecified without supplied plan support. Initial PaO2/FiO2 subgroup support was found and is not included in this omission pattern.
- **Supported alternatives:** A separate unsupplied dated subgroup plan may exist; alternatively the figure includes exploratory post hoc groups under a shared predefined title.
- **Exact human question:** Where were the unknown-diagnosis and hematologic-malignancy treatment-interaction analyses prespecified, or should their reported status differ from the predefined stratification analyses?

### F-ST1-001

**Observation:** Figure 3 hazard-ratio direction differs from the report contrast.

- **Exact locations and document roles:** REPORT main article p.4 treatment-effect method (HFNO versus standard oxygen); p.5 Table 2 primary and IMV rows; p.6 IMV narrative; p.7 Figure 3A and 3B, all 26 HR rows and the left/right favors labels.
- **Source links:** [REPORT main p.4](../../../../jama_azoulay_2018_oi_180109.pdf#page=4); [REPORT main p.5](../../../../jama_azoulay_2018_oi_180109.pdf#page=5); [REPORT main p.6](../../../../jama_azoulay_2018_oi_180109.pdf#page=6); [REPORT main p.7](../../../../jama_azoulay_2018_oi_180109.pdf#page=7).
- **Printed values/statements:** Table 2: mortality HR 0.98 (0.77–1.24), IMV cause-specific HR 0.85 (0.68–1.06). Figure 3 all-patient rows: mortality 1.02 (0.81–1.29), IMV 1.17 (0.94–1.46). Both figure panels label values below 1 'Favors High-Flow Nasal Oxygen Therapy' and above 1 'Favors Standard Oxygen Therapy'.
- **Rule and calculation:** For an event HR stated as HFNO versus standard oxygen, HR below 1 favors HFNO. Inverting the reported IMV HR gives 1/0.85=1.17647, and reversing its interval gives [1/1.06,1/0.68]=[0.94340,1.47059], close to the figure 1.17 [0.94,1.46] within display precision. Mortality reciprocal 1/0.98=1.02041 likewise matches the figure. This indicates a reversed contrast with the original favors labels. The point-estimate half-unit intervals for the two IMV readings, [0.845,0.855] and [1.165,1.175], have gap 0.310; relative gap 0.310/0.85=0.36471>0.05. Direction mismatch, rather than the small mortality reciprocal difference, is the finding. No subgroup HR is equated to its crude risk ratio.
- **Focus area:** B.
- **Proposed review domain:** statistical_results.
- **Proposed relationships:** S_W.
- **Qualifying route:** Route A, category 2.
- **Affected result or extracted value:** Figure 3 treatment direction and all-patient/subgroup HRs for death and IMV, especially IMV HR 1.17 versus 0.85.
- **Why context does not resolve it:** The reproduced reversal of the HR/reference-group reading is category 2; reconstructing the reciprocal does not remove the printed direction a reader could extract.
- **Alternatives and missing definition:** The figure may have fitted standard oxygen versus HFNO while retaining HFNO-versus-standard favors labels; alternatively the relative HR values or labels use an unreported contrast. Event-time differences do not explain reciprocal all-patient values paired with the same event counts. The missing definition is the figure numerator/reference group.
- **Exact human question:** What is the numerator/reference treatment for every Figure 3 HR, and which favors labels apply to that contrast?

### F-ST1-005

**Observation:** Planned longitudinal joint-model analyses are not identified.

- **Exact locations and document roles:** PLAN bundle p.55 lines 825–826; p.82 lines 1314–1315; p.105 lines 1745–1747. REPORT main article p.4 Statistical Analysis; pp.1,6 repeated oxygenation/comfort/dyspnea results; REPORT results supplement pp.4–5.
- **Source links:** [REPORT main p.1](../../../../jama_azoulay_2018_oi_180109.pdf#page=1); [REPORT main p.4](../../../../jama_azoulay_2018_oi_180109.pdf#page=4); [REPORT main p.6](../../../../jama_azoulay_2018_oi_180109.pdf#page=6); [PLAN bundle p.55](../../../../joi180109supp1_prod.pdf#page=55); [PLAN bundle p.82](../../../../joi180109supp1_prod.pdf#page=82); [PLAN bundle p.105](../../../../joi180109supp1_prod.pdf#page=105); [REPORT supplement 2 p.4](../../../../joi180109supp2_prod.pdf#page=4); [REPORT supplement 2 p.5](../../../../joi180109supp2_prod.pdf#page=5).
- **Printed values/statements:** PLAN: oxygenation, dyspnea and comfort analyzed with joint models accounting for right censoring. REPORT p.4 names Wilcoxon rank-sum for comfort/dyspnea; results report oxygenation difference 19.5 (4.4–34.6) and nonsignificant comfort/dyspnea over time. Figures provide no model/point/bar definition identifying a joint-model result.
- **Rule and calculation:** The joint-model commitment is explicit in the original SAP and final plan. The report names a different procedure for symptoms and never identifies the planned censoring-aware joint model or which reported longitudinal value it produced. This is not a proposed preferred model; it compares supplied descriptions. Rounding does not apply to the analysis mapping.
- **Focus area:** D.
- **Proposed review domain:** protocol_report.
- **Proposed relationships:** P_R.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** Abstract-reported/key secondary oxygenation, comfort and dyspnea longitudinal analyses.
- **Why context does not resolve it:** Category 5: planned key secondary joint-model analyses are replaced or not reported; the final plan retains them.
- **Alternatives and missing definition:** A joint model may have been fitted in addition to rank tests or used for a displayed mean contrast without being named. The supplied material does not define its longitudinal/survival components or identify its output.
- **Exact human question:** Were the planned joint models for oxygenation, comfort and dyspnea fitted, and which reported result corresponds to each model or to a stated replacement?

### F-ST1-006

**Observation:** Planned ICU length-of-stay survival analyses are not reported as specified.

- **Exact locations and document roles:** PLAN bundle p.54 lines 822–824; p.82 lines 1311–1313; p.105 lines 1742–1745. REPORT main article p.4 methods; p.5 Table 2 ICU stay; pp.1,6 ICU stay narrative.
- **Source links:** [REPORT main p.1](../../../../jama_azoulay_2018_oi_180109.pdf#page=1); [REPORT main p.4](../../../../jama_azoulay_2018_oi_180109.pdf#page=4); [REPORT main p.5](../../../../jama_azoulay_2018_oi_180109.pdf#page=5); [REPORT main p.6](../../../../jama_azoulay_2018_oi_180109.pdf#page=6); [PLAN bundle p.54](../../../../joi180109supp1_prod.pdf#page=54); [PLAN bundle p.82](../../../../joi180109supp1_prod.pdf#page=82); [PLAN bundle p.105](../../../../joi180109supp1_prod.pdf#page=105).
- **Printed values/statements:** PLAN: ICU stay overall and separately in survivors and deceased, using Kaplan–Meier and competing-risk estimators as printed. REPORT: Wilcoxon rank-sum for ICU stay; medians 8 versus 6 days, mean difference 0.6 (−1.0,2.2),P=.07. No separate survivor/decedent survival-estimator result is supplied.
- **Rule and calculation:** The named planned estimators/populations differ from the reported rank comparison and quantitative mean difference. The planned survivor/decedent analyses are not supplied. Ambiguous 'former/latter' estimator attribution is preserved; it does not remove the positive planned analyses. Display precision does not apply to this specification comparison.
- **Focus area:** D.
- **Proposed review domain:** protocol_report.
- **Proposed relationships:** P_R.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** The abstract-reported ICU length-of-stay analysis, overall and in planned survivor/decedent populations.
- **Why context does not resolve it:** Category 5: planned key secondary LOS analyses are replaced or not reported.
- **Alternatives and missing definition:** The rank test may have been an additional analysis or the plan may have been changed. No supplied result identifies the planned survival/competing-risk estimator or separate populations.
- **Exact human question:** Which reported ICU length-of-stay result corresponds to the planned overall and survivor/decedent survival analyses, or what analysis specification replaced them?

### F-ST1-008

**Observation:** Intubated mortality is reported as post hoc despite prospective secondary status.

- **Exact locations and document roles:** PLAN bundle p.6 lines 97–100; p.7 lines 142–146; p.38 secondary objectives; p.45 lines 675–676; p.47 lines 699–700. REPORT main article p.4 post hoc analysis description and p.6 Post Hoc Outcomes.
- **Source links:** [REPORT main p.4](../../../../jama_azoulay_2018_oi_180109.pdf#page=4); [REPORT main p.6](../../../../jama_azoulay_2018_oi_180109.pdf#page=6); [PLAN bundle p.6](../../../../joi180109supp1_prod.pdf#page=6); [PLAN bundle p.7](../../../../joi180109supp1_prod.pdf#page=7); [PLAN bundle p.38](../../../../joi180109supp1_prod.pdf#page=38); [PLAN bundle p.45](../../../../joi180109supp1_prod.pdf#page=45); [PLAN bundle p.47](../../../../joi180109supp1_prod.pdf#page=47).
- **Printed values/statements:** Initial PLAN lists mortality after HFNO failure/intubation as secondary and prospectively names intubated-in-either-arm day 28 mortality. REPORT calls subset analyses in intubated patients post hoc and reports 55.3% versus 52.3%,RD+3 (−8.5,14.5),P=.65 there.
- **Rule and calculation:** The same post-intubation mortality subset/result is explicitly prospective secondary in the supplied initial plan but retrospectively labeled post hoc in REPORT. The final plan has a shorter secondary list, and REPORT p.3 discloses different secondary endpoints after redesign; these are source-grounded alternatives, not grounds to discard a reproduced outcome-status change. Display precision does not apply.
- **Focus area:** D.
- **Proposed review domain:** protocol_report.
- **Proposed relationships:** P_R.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** The prespecification/outcome status of the reported intubated mortality contrast 55.3% versus 52.3%.
- **Why context does not resolve it:** Category 5 always registers a prespecified outcome whose status changes. The disclosed redesign is recorded as an alternative explanation.
- **Alternatives and missing definition:** The prospective analysis may have been removed with the grant-stage redesign and later reintroduced as post hoc, or only an additional intubated subset analysis may have been meant. The supplied report does not distinguish those analyses or date that status change.
- **Exact human question:** Was the reported intubated mortality contrast the prospectively listed secondary analysis, or was that analysis removed before the reported post hoc analysis, and where is the status change specified?

### F-ST1-011

**Observation:** The infection HR interval does not reproduce under the same-display interval diagnostic.

- **Exact locations and document roles:** REPORT main article p.5 Table 2 all three HR rows and footnote d; p.4 infection comparison method.
- **Source links:** [REPORT main p.4](../../../../jama_azoulay_2018_oi_180109.pdf#page=4); [REPORT main p.5](../../../../jama_azoulay_2018_oi_180109.pdf#page=5).
- **Printed values/statements:** Mortality:138/140 events,HR.98 (.77–1.24); IMV:150/170 events,HR.85 (.68–1.06); infection:39/41 events,HR 1.01 (.96–1.06), cause-specific HR per footnote. All 95% CIs.
- **Rule and calculation:** Diagnostic log-event-count interval H×exp(±1.95996×sqrt(1/e_H+1/e_C)) reproduces the mortality CI [0.77467,1.23975] and IMV CI [0.68244,1.05870] within printed half-unit intervals. Applied to the infection row it gives [0.65151,1.56574]. Allowing each count±0.5 and HR±0.005, lower endpoint range[0.64650,0.65653], upper[1.55374,1.57784]. Printed lower[0.955,0.965] has gap 0.29847/0.96=0.31091; printed upper[1.055,1.065] has gap 0.48874/1.06=0.46108. Both exceed 0.05. This is a diagnostic method supported by reproducing the other HR rows, not a claim that it is the exact fitted Cox covariance. No standard error or interval construction is supplied for the infection HR.
- **Focus area:** B, C.
- **Proposed review domain:** statistical_results.
- **Proposed relationships:** S_W.
- **Qualifying route:** Route A, category 4.
- **Affected result or extracted value:** The infection cause-specific HR95% CI0.96–1.06 and its precision for evidence extraction.
- **Why context does not resolve it:** Category 4: a printed interval does not reproduce under a method that reproduces the other rows of the same display. The missing model/variance/interval definition becomes the human question rather than making the observation conditional.
- **Alternatives and missing definition:** The infection HR interval may use a different analysis unit, event definition, variance or CI construction; the proportions chi-square P=.91 may belong to a separate comparison. These possibilities are not specified, and the diagnostic does not identify a final alternative interval.
- **Exact human question:** What event definition, analysis unit, model, variance estimator and confidence-interval construction produced the infection HR 1.01 (0.96–1.06), and why does its interval differ from the construction reproducing the other HR rows?

### F-ST1-014

**Observation:** Figure 3 describes diagnosis and malignancy subgroup analyses as predefined, but the supplied plans do not contain them.

- **Exact locations and document roles:** REPORT main article p.7 Figure 3 title and unknown-diagnosis/hematologic-malignancy rows in panels A/B; p.4 subgroup methods. PLAN bundle pp.45–46, lines 666–680, initial subgroup list; pp.98–99, lines 1600–1604, final strata; p.104, lines 1721–1723 and 1735–1736, planned subset interaction strategy.
- **Source links:** [REPORT main p.7](../../../../jama_azoulay_2018_oi_180109.pdf#page=7); [REPORT main p.4](../../../../jama_azoulay_2018_oi_180109.pdf#page=4); [PLAN p.45](../../../../joi180109supp1_prod.pdf#page=45); [PLAN p.46](../../../../joi180109supp1_prod.pdf#page=46); [PLAN p.98](../../../../joi180109supp1_prod.pdf#page=98); [PLAN p.99](../../../../joi180109supp1_prod.pdf#page=99); [PLAN p.104](../../../../joi180109supp1_prod.pdf#page=104).
- **Printed values/statements:** Figure 3 title says overall and in “Predefined Subgroups.” Unknown-diagnosis interactions are P=.12 for mortality and P=.9 for IMV. Hematologic-malignancy interactions are P=.5 for mortality and P=.01 for IMV; the IMV no-malignancy HR is 1.61 (1.16–2.23), and the malignancy HR is .89 (.65–1.22). Final PLAN names time since ICU admission, oxygen flow and shock strata; original PLAN adds oxygenation/organ-dysfunction and procedural/intubated/DNI subsets, but neither supplies unknown-diagnosis or hematologic-malignancy interaction analyses.
- **Rule and calculation:** Compare the report's positive predefined-analysis description with all supplied prospective subgroup specifications. The two diagnosis/disease subgroup analyses are absent from the complete supplied plan map. Eligibility definitions involving malignancy and historical associations involving unidentified ARF are not prospective treatment-interaction specifications. This is a prespecification mapping observation; display precision does not apply.
- **Focus area:** D.
- **Proposed review domain:** protocol_report.
- **Proposed relationships:** P_R.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** Prespecification status of the unknown-diagnosis and hematologic-malignancy treatment interactions, including the IMV malignancy interaction P=.01 and subgroup HRs.
- **Why context does not resolve it:** Category 5 applies to an analysis described as prespecified that the supplied plan does not contain. The exploratory multiple-testing caution does not establish whether these particular subgroup analyses were prospectively defined.
- **Alternatives and missing definition:** These subgroups may have been prospectively added in another analysis document, or the figure title may collectively describe a mixture of planned and exploratory subgroups. No supplied amendment or subgroup-specific status distinguishes those possibilities.
- **Exact human question:** Where were the unknown-diagnosis and hematologic-malignancy subgroup interaction analyses prospectively specified, or which Figure 3 subgroups should be read as exploratory additions?

