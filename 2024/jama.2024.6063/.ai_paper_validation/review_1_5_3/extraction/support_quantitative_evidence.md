# Support Quantitative Evidence Map

## Scope and method

This map covers the complete assigned support union: `DOC-JAMA2024-6063-SUPP1-317ff46a` (the protocol, PDF pp. 1-15, all fresh direct-source extraction), `DOC-JAMA2024-6063-SUPP2-57681138` (the SAP excerpt, PDF p. 1, fresh direct-source extraction), and `DOC-JAMA2024-6063-SUPP3-67e172cd` (the results supplement, PDF pp. 1-15, reusable-backed native/layout text). The fresh page-level `pdftotext -layout` outputs and copies of the reusable source-matched page text are retained in `preprocessing/support_mapper_fresh/`. Direct-source visual confirmation was performed for the dense eTable 4 pages (SUPP3 pp. 5-7), eTable 5 (p. 8), and eTable 8 (p. 14); rendered confirmation files are in `preprocessing/support_mapper_fresh/rendered/`.

No OCR was needed: all assigned pages have legible native text, and the rendered checks agreed with the relevant table headers, columns, signs, intervals, and footnotes. This is an evidence map, not a candidate diagnosis. “Main-paper key” is a matching key for the later cross-source reviewer; it does not assert identity until population, time point, contrast, model, and precision are compared.

## Page-complete coverage register

| Source | Pages | Extraction status | Result-relevant content or explicit no-applicable record |
|---|---:|---|---|
| SUPP1 protocol | 1 | Fresh | Administrative title/version/investigator page; no trial result, table, formula, or result-relevant quantitative relationship. |
| SUPP1 protocol | 2 | Fresh | Planned 260-participant, 6-month trial; primary hypothesis: krill oil decreases 100-mm VAS pain by 10 mm more than placebo over 24 weeks; secondary hypothesis: 20% decrease in effusion size. Background figures only; no result applicable. |
| SUPP1 protocol | 3 | Fresh | Background Table 1 (structural-factor associations) and Figure 1 historical example: effusion-synovitis change over 2.6 years; no trial result applicable. |
| SUPP1 protocol | 4 | Fresh | Background prevalence: 67% of randomly selected participants aged >=50 had effusion-synovitis and 22% large effusions (score >=3); Figures 2-3 are unpublished background data; no current-trial result applicable. |
| SUPP1 protocol | 5 | Fresh | Background/pilot result: 90 participants aged 30-75; 300 mg krill oil for 30 days; WOMAC pain change -38.35 (SD 21.06) versus -0.6 (15.89), P=.01; CRP change -30.9% (1.0) versus +25.1% (1.05), P=.008. Historical external study, not a KARAOKE result. |
| SUPP1 protocol | 6 | Fresh | Planned trial aim/design, primary and 18 secondary outcomes; quantitative definitions mapped below. |
| SUPP1 protocol | 7 | Fresh | Planned sample/eligibility/randomization/intervention: 260 across five centres; age >40; VAS >40 mm; two capsules daily for 24 weeks; computer-generated, site-stratified adaptive allocation. |
| SUPP1 protocol | 8 | Fresh | Outcome measurement definitions, time points, units, scales, and formula for effusion change. |
| SUPP1 protocol | 9 | Fresh | Planned additional outcomes/measurement definitions, including strength and anthropometry time points. |
| SUPP1 protocol | 10 | Fresh | Planned safety: report incidence and number of regular AEs and SAEs by treatment and type; no statistical result. |
| SUPP1 protocol | 11 | Fresh | Table 2 schedule of assessments; planned time-point matrix, no result. |
| SUPP1 protocol | 12 | Fresh | Statistical definitions and sample-size/power calculations; mapped below. |
| SUPP1 protocol | 13-15 | Fresh | References only; no result-relevant quantitative relationship beyond citation metadata. |
| SUPP2 SAP excerpt | 1 | Fresh | Full planned analysis definition; mapped below. |
| SUPP3 results supplement | 1 | Reusable-backed | Contents/index page only; no independent result beyond locating eTables 1-8/eFigure. |
| SUPP3 results supplement | 2 | Reusable-backed | eTable 1 primary-outcome missingness sensitivity analysis. |
| SUPP3 results supplement | 3 | Reusable-backed | eTable 2 adherence/follow-up counts and percentages. |
| SUPP3 results supplement | 4 | Reusable-backed | eTable 3 Omega-3 Index descriptive statistics. |
| SUPP3 results supplement | 5-7 | Reusable-backed + direct visual table check | eTable 4 complete secondary-endpoint time-series table and footnotes. |
| SUPP3 results supplement | 8 | Reusable-backed + direct visual table check | eTable 5 WORMS effusion-score category counts/percentages. |
| SUPP3 results supplement | 9 | Reusable-backed | eTable 6 analgesic-use change counts. |
| SUPP3 results supplement | 10-13 | Reusable-backed | eTable 7 adverse-event count table, with no between-group risk analysis. |
| SUPP3 results supplement | 14 | Reusable-backed + direct visual table check | eTable 8 serious-adverse-event counts classified by severity/relationship, with no between-group risk analysis. |
| SUPP3 results supplement | 15 | Reusable-backed | eFigure is a 3-D illustrative rendering at baseline and 24 weeks; no numeric result. |

## Protocol and SAP definitions (administrative content opened across all assigned units)

### Planned design, estimands, measures, and formulae

| Local key | Exact source location | Extracted relationship/definition | Main-paper key for matching |
|---|---|---|---|
| N-SUP-001 | [SUPP1 p. 2](<../../../joi240048supp1_prod_1727199125.7845.pdf#page=2>), p. 6 | Planned double-blind placebo-controlled 6-month trial; target N=260. Primary endpoint is change in 100-mm VAS knee pain over 24 weeks; planned contrast is krill oil versus identical placebo. | PRIMARY-VAS-24WK-ITT |
| N-SUP-002 | [SUPP1 p. 2](<../../../joi240048supp1_prod_1727199125.7845.pdf#page=2>) | Planned primary hypothesis: 10-mm greater VAS pain decrease with krill oil than placebo over 24 weeks. Secondary hypothesis: 20% reduction in effusion size over 24 weeks. These are targets, not reported results. | PRIMARY-VAS-24WK-ITT; EFFUSION-24WK |
| N-SUP-003 | [SUPP1 p. 6](<../../../joi240048supp1_prod_1727199125.7845.pdf#page=6>) | Predeclared secondary domains: maximal area/volume and ordinal effusion, BML area, ultrasound, serial VAS and WOMAC pain, hand/back pain, function, OMERACT-OARSI response, hsCRP/lipids/glucose, strength, analgesic use, AQoL, PPT, AEs, costs. Listed assessment times include 4, 8, 12, 16, 20, and/or 24 weeks as domain-specific. | SECONDARY-TIME-SERIES; SAFETY |
| N-SUP-004 | [SUPP1 p. 7](<../../../joi240048supp1_prod_1727199125.7845.pdf#page=7>) | Eligibility uses age >40 years, knee VAS >40 mm, MRI effusion-synovitis, and clinical ACR knee-OA criteria. Treatment is two active/placebo capsules daily for 24 weeks; allocation is computer-generated by site using adaptive allocation. | POPULATION; RANDOMIZATION; TREATMENT-24WK |
| N-SUP-005 | [SUPP1 p. 8](<../../../joi240048supp1_prod_1727199125.7845.pdf#page=8>) | MRI effusion: four ROI (suprapatellar pouch, central portion, posterior femoral recess, subpopliteal recess) summed per slice; greatest four-ROI sum in mm² is maximal effusion. Volume sums slices over whole joint. **Formula:** change in effusion-synovitis area/volume = follow-up maximal value - baseline value. ICC for maximal-area method 0.81; ordinal method kappa 0.63-0.75. | EFFUSION-24WK; EFFUSION-DEFINITION |
| N-SUP-006 | [SUPP1 p. 8](<../../../joi240048supp1_prod_1727199125.7845.pdf#page=8>) | X-ray OARSI JSN/osteophyte scale 0-3; reported protocol repeatability ICC 0.98 (JSN) and 0.99 (osteophytes). MRI BML maximum area is mm²; observer blinded; protocol repeatability ICC 0.97. | BASELINE-STRUCTURE; BML-24WK |
| N-SUP-007 | [SUPP1 p. 9](<../../../joi240048supp1_prod_1727199125.7845.pdf#page=9>) | Strength by bilateral dynamometry at weeks 0, 12, 24; protocol Cronbach alpha 0.91. Blood markers sampled screening, 12, 24 weeks; weight/height at 0, 12, 24 weeks. | STRENGTH-12/24WK; METABOLIC-12/24WK |
| N-SUP-008 | [SUPP1 p. 10](<../../../joi240048supp1_prod_1727199125.7845.pdf#page=10>) | Planned harms reporting: incidence and number of regular AEs by treatment group/type; incidence and number of SAEs including cancer, unplanned hospital admissions, and joint replacement. | AE; SAE |
| N-SUP-009 | [SUPP1 p. 11](<../../../joi240048supp1_prod_1727199125.7845.pdf#page=11>) | Assessment table: VAS at screening, 0, 4, 8, 12, 16, 20, 24 weeks; WOMAC/ICOAP/global at 0,4,8,12,16,20,24; MRI screening and 24; bloods screening,12,24; AE safety at 12,24; strength/PPT at 0,12,24. | TIMEPOINTS; PRIMARY-VAS-24WK; SECONDARY-TIME-SERIES |
| S-SUP-001 | [SUPP1 p. 12](<../../../joi240048supp1_prod_1727199125.7845.pdf#page=12>); [SUPP2 p. 1](<../../../joi240048supp2_prod_1727199125.8245.pdf#page=1>) | SAP/protocol: linear regression compares change in pain, maximal effusion size, and function between groups; univariate and multivariable modelling if baseline groups not well matched; intention-to-treat for all outcomes. Per-protocol analysis: >=80% capsules. Two-tailed significance P<.05. Missing data: propensity weighting “as appropriate.” SAP p. 1 is explicitly an excerpt from protocol V2 dated 02 Feb 2016. | ANALYSIS-MODEL; PRIMARY-VAS-24WK-ITT; EFFUSION-24WK; FUNCTION-24WK; PP-80PCT |
| S-SUP-002 | [SUPP1 p. 12](<../../../joi240048supp1_prod_1727199125.7845.pdf#page=12>) | Pain power basis: placebo VAS reduction -15.5 +/-25.5 mm over 12 weeks, assumed 10-mm difference, 90% power, alpha=.05 => N=234; 10% loss adjustment => N=260, 130/arm. Effusion basis: 96% power for 20% difference, mean 2.24 cm² and SD change 1.35. Pilot WOMAC basis: 20% relative difference, 90% power, alpha=.05 => total N=54 over 4 weeks. | SAMPLE-SIZE; PRIMARY-VAS-24WK; EFFUSION-24WK |

## Results supplement: tables, labels, values, and statistical relationships

### eTable 1: primary-outcome sensitivity analysis

Source: [SUPP3 p. 2](<../../../joi240048supp3_prod_1727199125.83025.pdf#page=2>). Outcome label is knee VAS at 24 weeks; each change is mean (95% CI), and the table labels the final field as an absolute between-group difference with P value but does not define the signed operand order.

| Analysis | Krill-oil change (95% CI) | Placebo change (95% CI) | Difference (95% CI) | P | Main-paper key |
|---|---|---|---|---:|---|
| Original data | -19.93 (-24.67 to -15.20) | -20.21 (-24.87 to -15.54) | -0.27 (-6.92 to 6.38) | .94 | PRIMARY-VAS-24WK-ITT |
| + age | -19.95 (-24.68 to -15.21) | -20.21 (-24.88 to -15.55) | -0.26 (-6.91 to 6.38) | .94 | PRIMARY-VAS-24WK-AGE-SENSITIVITY |
| Multiple imputation | -19.94 (-24.56 to -15.32) | -20.29 (-24.9 to -15.68) | -0.35 (-6.79 to 6.09) | .92 | PRIMARY-VAS-24WK-MI-SENSITIVITY |

### eTables 2-3: adherence and biomarker descriptive values

| Local key | Source location | Extracted relationship | Main-paper key |
|---|---|---|---|
| N-SUP-010 | [SUPP3 p. 3](<../../../joi240048supp3_prod_1727199125.83025.pdf#page=3>) | eTable 2 arms: krill N=130/placebo N=132. Follow-up days, mean (SD): 190 (44.5)/184 (34.5). Follow-up >24 weeks: 55 (42.3%)/46 (34.8%). >=80% adherence: 0-12 wk, 91 (100%)/89 (100%); 12-24 wk, 82 (96.5%)/82 (90.1%); overall, 82 (98.8%)/81 (96.4%). Overall row denominator is N=167. Footnote says adherence is only among available pill-count data and trial completers (N=165 [75%]), creating a named denominator-definition requirement for later reconciliation. | ADHERENCE; PP-80PCT |
| N-SUP-011 | [SUPP3 p. 4](<../../../joi240048supp3_prod_1727199125.83025.pdf#page=4>) | eTable 3 Omega-3 Index (%). Krill: baseline N=116, 6.5 (1.61); 12 wk N=100, 7.8 (1.51), change 1.25 (1.42), change-N=98; 24 wk N=96, 8.0 (1.65), change 1.47 (1.50), change-N=94. Placebo: baseline N=111, 6.5 (1.53); 12 wk N=93, 6.5 (1.28), change .10 (1.17), change-N=92; 24 wk N=91, 6.6 (1.30), change .14 (1.31), change-N=90. | OMEGA3-INDEX-12/24WK |

### eTable 4: complete secondary-endpoint time-series table

Source: [SUPP3 pp. 5-7](<../../../joi240048supp3_prod_1727199125.83025.pdf#page=5>) (continues [p. 6](<../../../joi240048supp3_prod_1727199125.83025.pdf#page=6>) and [p. 7](<../../../joi240048supp3_prod_1727199125.83025.pdf#page=7>)). The complete printed cells (each arm’s N, final mean/median, baseline, and change with intervals) are preserved in `preprocessing/support_mapper_fresh/supp3-p05-reused-layout.txt` and `supp3-p06-reused-layout.txt`; the direct visual render verifies the column alignment. The compact matrix below records every printed between-group relationship and P value, which are the cross-source/checker comparators.

| Endpoint and time (weeks) | Between-group difference/measure (95% CI) | P | Main-paper key |
|---|---|---:|---|
| Knee pain VAS: 4, 8, 12, 16, 20, 24 | -0.4 (-4.9 to 4.1); -0.8 (-5.6 to 4.0); -0.1 (-5.2 to 5.1); 0.3 (-5.3 to 5.9); -0.5 (-6.7 to 5.6); -0.3 (-6.9 to 6.4) | .85; .75; .98; .91; .87; .94 | VAS-4/8/12/16/20/24WK |
| WOMAC total pain: 4, 8, 12, 16, 20, 24 | -5 (-23 to 13); -3 (-22 to 16); -3 (-24 to 18); -1 (-24 to 22); 5 (-21 to 30); 3 (-24 to 31) | .59; .77; .76; .92; .72; .81 | WOMAC-TOTAL-4/8/12/16/20/24WK |
| WOMAC weight-bearing pain: 4, 8, 12, 16, 20, 24 | 3 (-10 to 16); 1 (-12 to 14); 0.0 (-13 to 13); 0.0 (-14 to 13); 4 (-10 to 17); 3 (-10 to 16) | .66; .88; .99; .97; .60; .70 | WOMAC-WB-4/8/12/16/20/24WK |
| WOMAC non-weight-bearing pain: 4, 8, 12, 16, 20, 24 | -5 (-13 to 3); -3 (-12 to 6); -2 (-11 to 7); 0 (-10 to 10); 1 (-10 to 12); 2 (-10 to 14) | .25; .52; .64; .94; .82; .70 | WOMAC-NWB-4/8/12/16/20/24WK |
| WOMAC function: 4, 8, 12, 16, 20, 24 | -19 (-73 to 35); -4 (-62 to 53); 10 (-52 to 72); 22 (-47 to 90); 33 (-43 to 109); 51 (-31 to 133) | .48; .88; .75; .53; .39; .22 | WOMAC-FUNCTION-4/8/12/16/20/24WK |
| Hand-pain VAS: 4, 8, 12, 16, 20, 24 | -1.6 (-6.1 to 2.9); 3.8 (-0.9 to 8.6); -0.1 (-5.0 to 4.9); 0.4 (-4.9 to 5.7); 1.7 (-4.1 to 7.5); 1.3 (-4.8 to 7.3) | .49; .12; .98; .89; .57; .69 | HAND-VAS-4/8/12/16/20/24WK |
| Back-pain VAS: 4, 8, 12, 16, 20, 24 | -1.4 (-5.9 to 3.0); 3.9 (-0.9 to 8.6); 4.1 (-0.8 to 9.1); 4.3 (-0.9 to 9.6); -0.3 (-6.0 to 5.3); -1.3 (-7.9 to 5.2) | .53; .11; .10; .11; .91; .69 | BACK-VAS-4/8/12/16/20/24WK |
| Lower-leg strength, Newtons: 12, 24 | -1.4 (-5.9 to 3.0); -2.2 (-7.9 to 3.4) | .53; .44 | STRENGTH-12/24WK |
| AQoL-6D: 12, 24 | -0.0003 (-0.02 to 0.02); -0.01 (-0.04 to 0.01) | .98; .38 | AQOL-12/24WK |
| OMERACT-OARSI responder: 4, 8, 12, 16, 20, 24 | RR 0.85 (0.50 to 1.46); 0.87 (0.57 to 1.32); 0.98 (0.69 to 1.39); 0.94 (0.66 to 1.33); 1.06 (0.77 to 1.48); 1.14 (0.84 to 1.55) | .57; .51; .90; .72; .71; .39 | OMERACT-OARSI-4/8/12/16/20/24WK |
| hsCRP: 12, 24 | 0.07 (-1.19 to 1.33); 0.64 (-0.56 to 1.84) | .92; .30 | HSCRP-12/24WK |
| Triglycerides: 12, 24 | 0.24 (0.07 to 0.42); 0.15 (-0.04 to 0.33) | .01; .11 | TRIGLYCERIDES-12/24WK |
| HDL cholesterol: 12, 24 | -0.01 (-0.07 to 0.05); -0.03 (-0.09 to 0.03) | .76; .32 | HDL-12/24WK |
| LDL cholesterol: 12, 24 | -0.14 (-0.29 to 0.005); 0.01 (-0.14 to 0.17) | .06; .90 | LDL-12/24WK |
| Fasting glucose: 12, 24 | 0.07 (-1.19 to 1.33); 0.04 (-0.23 to 0.30) | .92; .79 | GLUCOSE-12/24WK |

eTable 4 definitions: VAS 0-100 (higher=worse); WOMAC total pain 0-500, weight-bearing 0-300, non-weight-bearing 0-200, physical function 0-1700 (all higher=worse); hand/back VAS 0-100 (higher=worse); strength 0-250 Newtons (higher=greater force); AQoL-6D -0.04 to 1.0 (1=full health, 0=death-equivalent, -0.04=worse than death). Values are mean (SD) with 95% CIs except effusion-synovitis volume and hsCRP (median [IQR]); table says no missing values were imputed. It says age was the only variable associated with missingness and age sensitivity showed no significant difference (eTable 1). Analyses are baseline-adjusted when Table 1 difference P<=.1, named as hsCRP, back pain, WOMAC total pain, and weight-bearing pain. OMERACT-OARSI responder is either >=50% improvement plus absolute change >=20 points in VAS pain or WOMAC function, or >=20% improvement plus >=10 mm absolute change in at least two of three categories; RR (95% CI) is derived from log-binomial regression and responder index is calculated at final follow-up as a baseline-change measure.

### eTables 5-8 and eFigure

| Local key | Source location | Extracted relationship/definition | Main-paper key |
|---|---|---|---|
| N-SUP-012 | [SUPP3 p. 8](<../../../joi240048supp3_prod_1727199125.83025.pdf#page=8>) | eTable 5, WORMS effusion score at 24 weeks. Krill/placebo: smaller by 2 units 2 (1.9%)/2 (1.9%); smaller by 1, 10 (12%)/16 (12%); no change, 80 (72%)/75 (72%); larger by 1, 12 (12%)/13 (12%); larger by 2, 3 (2.8%)/3 (2.8%); total 107 (100%)/109 (100%). | WORMS-EFFUSION-24WK |
| N-SUP-013 | [SUPP3 p. 9](<../../../joi240048supp3_prod_1727199125.83025.pdf#page=9>) | eTable 6 analgesic-use change versus previous visit: week 4 and 8 all “--”; week 12 krill increase/decrease 1/1, placebo 3/--; week 16 all “--”; week 20 krill blank/-- and placebo --/--; week 24 krill blank/-- and placebo 1/--. Dashes/blanks are printed exactly and need a source-definition check before any arithmetic interpretation. | ANALGESIC-USE |
| N-SUP-014 | [SUPP3 pp. 10-13](<../../../joi240048supp3_prod_1727199125.83025.pdf#page=10>) | eTable 7 is a complete event-level count table for krill N=130 and placebo N=132, continuing across pp. 10-13. All printed event labels/count cells are retained in `supp3-p10` through `supp3-p13` reusable-layout derivatives. It reports counts, not person counts, and states that statistical analysis of between-group risk differences was not undertaken because AE numbers were low. | AE |
| N-SUP-015 | [SUPP3 p. 14](<../../../joi240048supp3_prod_1727199125.83025.pdf#page=14>) | eTable 8 is a serious-AE count table for placebo N=132 and krill N=130 cross-classified by unknown/mild/moderate/severe and relationship (NA, unlikely, possible, probable). The complete 13 printed SAE rows are retained in `supp3-p14-reused-layout.txt`; footnote: unknown severity/relationship not recorded. It defines mild/moderate/severe and states no between-group risk-difference analysis due to low AE numbers. | SAE |
| N-SUP-016 | [SUPP3 p. 15](<../../../joi240048supp3_prod_1727199125.83025.pdf#page=15>) | eFigure: three-dimensional rendering of effusion-synovitis for one participant at baseline and 24 weeks. It has no numeric scale, estimate, table value, or inferential result. | EFFUSION-ILLUSTRATION |

## Mapping summary and limitations

- Direct-source units mapped: SUPP1 15/15 fresh pages; SUPP2 1/1 fresh page; SUPP3 15/15 reusable-backed pages. Total assigned and mapped: 31/31 pages.
- Result-relevant table/figure units mapped: protocol Table 1/Figures 1-4 and Table 2; results eTables 1-8 and eFigure. The protocol background tables/figures are explicitly differentiated from KARAOKE results.
- Proposed support numeric/reporting keys: N-SUP-001 through N-SUP-016. Proposed statistical keys: S-SUP-001 through S-SUP-002 plus every eTable 1 and eTable 4 estimate/CI/P relationship; downstream inventory construction should assign package-wide `N###`/`S###` IDs without losing these locations.
- No workbook, CSV, DOC/DOCX, or formula/cached-workbook content exists in this assigned support scope.
- No scientific-coverage gap remains. One source-definition limitation is explicit: eTable 2’s denominators (especially overall adherence) and eTable 6’s blanks/dashes must be interpreted only with an available source definition; this map does not infer missing values or diagnose a candidate.
