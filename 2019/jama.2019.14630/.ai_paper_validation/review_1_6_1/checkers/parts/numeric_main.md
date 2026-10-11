# Numeric consistency review: main and plan population shard

Status: COMPLETE. Exact assigned scope: DOC-001 main-paper flow, analysis populations, all Table 1 baseline cells, all Table 2 and Table 3 score/nutrient rows, Figures 1–4, matched abstract and narrative occurrences, and effect-measure identity; additionally DOC-002 protocol and DOC-003 SAP participant-flow and analysis-population arithmetic. All 106 canonical relationships N001–N106 were checked. Supplementary result-table numerical checks and inferential sample-size reproduction are disjoint assignments.

Source roles: DOC-001 REPORT, DOC-002 PLAN, DOC-003 PLAN, determined from content. Source-linked fresh maps and current supplied PDFs were used. No old candidate conclusions or external evidence were used. No source or reused asset was modified.

The inclusion threshold was independently applied to every observation. Each displayed value retains its half-unit rounding interval. Different instruments and populations were matched before comparing their counts; mixed-model estimates were not required to equal crude differences. Repeated observations from one pattern are consolidated. Finding count: 1. Excluded-observation count: 16.

## Findings

### F-NUM-001

The abstract describes the main-analysis population as having completed 12-month follow-up without distinguishing that population from participants with observed follow-up information.

**Exact source locations and document roles:**

- REPORT DOC-001 [PDF p. 1, abstract Results](../../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=1): “Among 6874 randomized participants” and “6583 (96%) completed the 12-month follow-up and were included in the main analysis.”
- REPORT DOC-001 [PDF p. 3, Figure 1, main-analysis boxes and 12-month information/sensitivity boxes](../../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=3): 3272 intervention and 3311 control included in main analyses; 439 and 368 without available nutritional information at 12 months; 2833 and 2943 in the 12-month sensitivity analyses.
- REPORT DOC-001 [PDF p. 4, Statistical Analysis and Results](../../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4): principal analyses include randomized participants with baseline nutritional data regardless of incomplete information at follow-up; 53 baseline questionnaire exclusions and 238 energy exclusions; 6583 analyzed with multiple imputation.
- REPORT DOC-001 [PDF p. 5, Table 2 header and footnote a](../../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=5): main denominators 3272 and 3311; 517 er-MedDiet values imputed at 12 months, and 807 MDS/MEDAS/PDQS values imputed at 12 months.

**Printed inputs:** 6874 randomized; 6583 stated completers and main-analysis participants; 3272 and 3311 main-analysis arm totals; 53 and 238 baseline exclusions; 439 and 368 missing nutritional-information counts; 2833 and 2943 nutritional completers; 517 missing primary-score values filled by imputation.

**Rule and calculation:** A baseline-eligible analysis count including imputed follow-up information is distinct from an observed follow-up outcome count. The number 6583 is exactly reconstructed by 6874 − 53 − 238 = 6583 and 3272 + 3311 = 6583. Nutritional completeness gives 2833 + 2943 = 5776, equivalently 6583 − 439 − 368 = 5776. For the primary er-MedDiet score, the reported 517 imputed values imply 6583 − 517 = 6066 non-imputed values at 12 months. With randomized denominator 6874, these three quantities are 95.7667%, 84.0268%, and 88.2456%, respectively. They describe distinct populations. No claim is made that absence of nutritional information establishes absence from the follow-up visit.

**Display-precision check:** The 96% itself reconciles with 6583/6874 because 95.7667% lies inside the whole-percentage interval 95.5–96.5%. The observation concerns the completion attribution, not that rounded percentage. Even allowing half-unit intervals around each integer tally, the primary non-imputed count lies between 6065 and 6067 and nutritional completeness between 5775 and 5777; neither overlaps the displayed 6583 interval 6582.5–6583.5.

**Focus area:** A, counts and denominators.

**Proposed review domain:** statistical_results.

**Proposed relationship type:** S_W. All compared locations are within REPORT DOC-001.

**Affected result or extracted value:** The observed 12-month completion count and percentage for the primary dietary-adherence analysis, and whether 6583 can be extracted as complete observed follow-up rather than as the multiple-imputation analysis population.

**Why context does not resolve it:** The abstract uses one number for completion and analysis without stating that completion means attendance rather than observed dietary information. The body clearly identifies the analysis population but retains different observed-information counts for the primary questionnaire and food-frequency-based measures. It does not identify a visit-attendance count that independently supports 6583 as completed follow-up. A reader can identify the analyzed denominator but cannot choose an observed primary follow-up completion count from the abstract's statement alone.

**Alternative source-grounded interpretations:** The intended 6583 may denote only baseline-eligible participants retained in the imputed main analysis. Alternatively, all 6583 may have attended some 12-month follow-up while dietary measurements remained incomplete; the package does not give a count or definition establishing that attendance interpretation. Primary-score availability and nutritional-information completeness must remain separate and do not themselves establish withdrawal or loss to clinical follow-up.

**Exact human question:** Does “6583 (96%) completed the 12-month follow-up” refer to visit attendance or to inclusion in the multiple-imputation analysis, and what count and denominator should be extracted for observed 12-month primary er-MedDiet follow-up completeness?

**Direct-source confirmation:** The abstract and Figure 1 were visually inspected in fresh Poppler pdftoppm 26.01.0 renders; Table 1/methods and Table 2 were visually inspected in source-linked retained renders. Fresh direct Poppler pdftotext 26.01.0 layouts of pp. 1–4 and p. 5 confirm the quoted values. Derivatives: preprocessing/numeric-main-p001.png, preprocessing/numeric-main-p003.png, preprocessing/numeric-main-p001-004.txt, preprocessing/numeric-main-p005.txt. Rendered derivatives serve as direct-source visual confirmation, not independent document comparators.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 p. 1 abstract Results; p. 4 Results/Table 1 | The abstract places 3406 men and 52% after 6874 randomized. 3406/6874 is 49.55%, while 3406/6583 is 51.74%. The exact main-table counts 1702 + 1704 = 3406 and main-population total identify the baseline demographic population immediately; this does not change the primary analysis denominator. | CONTEXT_RESOLVES |
| REPORT DOC-001 p. 4 Table 1, intervention university and control secondary education | 703/3240 = 21.6975% versus printed 21%, and 902/3285 = 27.4581% versus printed 28%. These do not reconcile under ordinary whole-percent intervals, including half-unit count sensitivity. All category counts sum exactly to explicitly supplied education denominators, so the full cells resolve demographic extraction immediately. Both instances are one education-percentage observation. | CONTEXT_RESOLVES |
| REPORT DOC-001 p. 4 Results; p. 3 Figure 1; pp. 5 and 8 footnotes | 807/6583 × 100 = 12.25885%, outside the printed 12.2% interval 12.15–12.25; even minimum half-unit ratio is 12.25032%. Exact 807 numerator, 6583 denominator and 439 + 368 missing counts resolve extraction immediately. | CONTEXT_RESOLVES |
| REPORT DOC-001 p. 5 Table 2, 12-month PDQS; p. 6 matching narrative | Displayed 6.9 − 4.4 = 2.5 versus contrast 2.4: the independent difference interval 2.40–2.60 overlaps the contrast interval 2.35–2.45. Follow-up and baseline displays also permit a common underlying difference. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 pp. 7–8 Table 3, SFA both times, MUFA:SFA at 6 months, PUFA at 12 months, fiber at 6 months, cholesterol at 6 months | Last-digit differences in displayed group-change subtraction versus contrasts are compatible with independent half-unit input intervals. Examples: −1.0 − (−0.6) permits −0.50 to −0.30, intersecting displayed −0.5; 40 − 16 permits 23–25, intersecting displayed 23 at 22.5–23.5. All 26 nutrient-change rows were checked. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p. 6 relative primary-score increase | 4.7/8.5 × 100 = 55.29% versus printed 55%; the input interval yields 54.386–56.213%, intersecting the printed 54.5–55.5% interval. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p. 5 Table 2 and pp. 7–8 Table 3, mixed-model contrast columns | A mixed-model contrast cannot be rejected solely because a crude subtraction of printed means differs; the footnotes explicitly identify modeled contrasts. No independent quantity-label contradiction was found. | MODEL_VERSUS_CRUDE |
| REPORT DOC-001 p. 7 Table 3 baseline macronutrient and alcohol rows | A required sum of exactly 100% is not established: alcohol is a median whereas the other printed components are means, and the table does not state an exhaustive individual energy-accounting identity for those printed summaries. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-001 p. 7 Table 3, MUFA:SFA baseline/change | A mean individual ratio or its mean change need not equal a ratio of group mean MUFA and SFA. Individual nutrient pairs needed for an unconditional equality are not supplied. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-001 p. 10 Figure 4 all 11 percentage pairs | Exact event numerators and contributing denominators are not printed; inversion from a displayed proportion/CI would depend on unreported test/interval and available-case assumptions. No exact count or effect-measure identity discrepancy can be reproduced from those summaries alone. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-001 p. 10 Figure 4 all 11 axes/caption | Axis text appends “95% CI,” but the caption immediately defines medians, IQR boxes and 1.5-IQR whiskers. Distribution quantity is identifiable directly from the caption and familiar boxplot marks. | CONTEXT_RESOLVES |
| REPORT DOC-001 p. 4 meaningful-change definitions; p. 10 Figure 4 labels | “At least 5%” in methods versus “>5%” figure labels, and omitted comparison wording on the diastolic threshold, do not supply counts of exact-boundary observations or a result-changing difference. The common clinical thresholds are identifiable in context. | TERMINOLOGY_OR_WORDING |
| REPORT DOC-001 p. 3 Figure 1; PLAN DOC-003 p. 15 Figure 2 | Main 2803 exclusions are summarized as not meeting inclusion criteria, while SAP screening partitions 2271 refusals and 532 criterion exclusions. Total 2803 and randomized 6874 agree exactly; the shorthand exclusion-reason difference does not alter an analysis population or primary dietary result. | PERIPHERAL_COMPARISON |
| PLAN DOC-002 pp. 14,18,54; PLAN DOC-003 pp. 6–7,14–15 | Planned 6000 and approximate center recruitment goals differ from achieved 6874; prospective goals and achieved participants are different quantities. Original 20 centers versus later 23 centers is disclosed administrative context. | PERIPHERAL_COMPARISON |
| PLAN DOC-002 p. 18; PLAN DOC-003 pp. 14–15 | Planned diabetes quota 25%, SAP 27% wording, and screening 27.2% describe quota/descriptive material and do not change the interim dietary analysis-set count or a supplied statistical decision rule. | PERIPHERAL_COMPARISON |
| REPORT DOC-001 pp. 5–10 table headings and PLAN DOC-003 p. 15 randomization labels | “All randomized included participants,” “all randomized participants” with explicit 3272/3311 headers, and household participants “randomized by couples” are understood through adjacent totals and household context; counts refer to participants, not numbers of couples. | TERMINOLOGY_OR_WORDING |

## Scope completion and limitations

All main numeric relationships and assigned plan flow/population arithmetic were reviewed, including each of the 8 score follow-up rows, 26 nutrient-change rows, 13 nutrient baselines, every Table 1 cell, all 11 Figure 4 proportion pairs, four Figure 2 distributions and all 22 Figure 3 panels. Main flow sums and all SAP flow row/column sums reconcile. No displayed current-trial OR/RR/HR, incidence/person-time denominator, or numerical histogram-bin count is supplied. References and administrative quantities on DOC-001 pp. 12–14 have no additional current-trial numeric relationship.

Limitations are bounded to missing printed graphical values, Figure 4 numerator/denominator details, and distinction between attendance and outcome completeness. All relevant source units remain mapped; none was omitted. Inferential compatibility, statistical model logic and sample-size reproduction are handled in the statistical lane. Source and reused assets remain preserved.

