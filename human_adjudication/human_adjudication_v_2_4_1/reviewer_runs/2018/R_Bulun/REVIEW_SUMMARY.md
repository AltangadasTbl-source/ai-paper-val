# v.2.4.1 independent primary review, 2018: reviewer R_Bulun

Reviewer R_Bulun reviewed all 115 candidates in the 2018 workbook (10 papers) against the original PDFs supplied for each paper. Independence: I did not open the other reviewer's output for 2018 or any other year, any other reviewer's working folder, any v.2.3.1 or earlier adjudication material, `meta_report/`, the paper packages in the repository (including their pipeline instruction and output files), or any `.ai_paper_validation/` folder. For each candidate I formed a judgment from the PDFs first and then read the candidate's card in `final_report_1_6_2.md`; where the card changed or extended my view, column R or the rationale says so.

## Files

- `human_adjudication_v_2_4_1_2018_R_Bulun_completed.xlsx`: completed workbook built from the R_B blank with `fill_review.py` (Setup!B2 = R_Bulun, role R_Bulun).
- `judgments.json`: one record per candidate with D, E, H to L, the column R note, the evidence inspected (files, pages, and whether pages were rendered or OCR'd) and the full rationale, including recomputations.
- `REVIEW_SUMMARY.md`: this file.

Recomputations were done in R (base `stats`: `chisq.test`, `fisher.test`, `wilcox.test`, `prop.trend.test`, Wald and Newcombe intervals, back-calculation of P values from printed intervals) and Python. Nothing in the review is stochastic, so no seed was required. Scripts are in my private working folder; every number cited in the workbook notes was computed or read directly from the source.

`recalc_check.py` on the completed workbook: all 115 rows `PRIMARY READY`; Checks: Candidates 115, Primary ready 115, Discuss 0, Unfinished 0, Workflow status `PRIMARY READY`.

## Counts

Disposition (D): retain 107, exclude 8, discuss 0.

| Review domain (E) | retain | exclude | discuss | total |
|---|---:|---:|---:|---:|
| statistical_results | 42 | 7 | 0 | 49 |
| report_internal_inconsistency | 4 | 0 | 0 | 4 |
| plan_material | 7 | 0 | 0 | 7 |
| protocol_report | 54 | 1 | 0 | 55 |
| Total | 107 | 8 | 0 | 115 |

E changed from the suggested domain: none. I considered a change for jama.2018.0156 C002 (protocol versus SAP endpoint families, arguably plan_material) but kept protocol_report because the candidate's comparison is plan against report, and I excluded it.

Exclusions:

- 2018::jama.2017.21906::C006. The wider LDL interval in eTable 1 is explained by LDL being measured in only 69% of participants (Table 1: 14 830 of 21 374); a pooled-SD interval with header n reproduces the five other rows, and the printed half-width implies about 193 participants with LDL in the missing-follow-up group (65%).
- 2018::jama.2018.0156::C002. The report labels airway difficulty and failure as secondary end points (as the protocols do) and analyzes them in the as-treated safety population (as the SAP does); the secondary-versus-safety labels coexist within the plan materials, so there is no plan-report conflict.
- 2018::jama.2018.0948::C008. A 95% CI excluding zero alongside a nonsignificant Holm-adjusted P is expected; the raw P implied by the interval (0.045) matches the printed .05.
- 2018::jama.2018.18020::C017. The interval implies P = 0.047, which rounds to the printed .05.
- 2018::jama.2018.6496::C009. Recomputed limits are -0.46, 0.44 and -0.43; integer rounding prints them as 0, and the unrounded intervals agree with P < .05.
- 2018::jama.2018.6496::C011. Both the Wald interval (17.1 to 102.9, truncated at 100) and the chi-square P (0.090) reproduce; they disagree because the stated methods are applied to an 8-patient subgroup with a 100% cell, not because of a reporting error.
- 2018::jama.2018.8802::C005. The interval implies P = 0.0016-0.0019; the printed 0.001 is consistent with truncation and the inferential readings agree.
- 2018::jama.2018.9128::C005. An unadjusted CI excluding 1 with a nonsignificant Benjamini-Hochberg-corrected P is expected; I reproduced all corrected P values.

## Outcome codes (retained rows)

statistical_results (42 retained):

| H \ I | substantive | minor_presentation | total |
|---|---:|---:|---:|
| confirmed_issue | 11 | 23 | 34 |
| probable_issue | 3 | 5 | 8 |

No retained row was coded `not_issue` or `indeterminate` on H. J (optional) was answered for all 42: direct 12, possible 11, unlikely 19.

Confirmed or probable and substantive (14):

- jama.2017.21906 C004 (two undefined adjusted contrasts for door-to-balloon time with discordant inference)
- jama.2018.0156 C005 (per-protocol CIs for survival and admission do not reproduce)
- jama.2018.14280 C001 (all 10 risk ratios and CIs reproduce as the transposed 2 x 2 ratio, not low vs intermediate tidal volume)
- jama.2018.14282 C012 (Figure 3 HRs are reciprocals of Table 2 while the favors headings are unchanged)
- jama.2018.14282 C013 (infection HR interval about nine times too narrow for 80 events)
- jama.2018.14282 C014 (pooled percentages for vasopressors and renal replacement therapy attributed to arms)
- jama.2018.17075 C008 (P = .09 for time-to-33C categories; Pearson and Fisher give 0.043-0.044) (probable)
- jama.2018.17075 C010 (RR, CI and P swapped between the two bleeding rows)
- jama.2018.18020 C001 (abstract 22% men; actual 73%)
- jama.2018.18020 C010 (SCN4A transient-paresis effect, interval and P mutually inconsistent; significant effect against mexiletine contradicts footnote d)
- jama.2018.18020 C011 (lower Table 2 header says placebo minus mexiletine; values are mexiletine minus placebo)
- jama.2018.18020 C015 (several effects do not equal the difference of period changes, including a sign reversal) (probable)
- jama.2018.18020 C016 (SCN4A fifth-handgrip interval crosses zero with P = .009)
- jama.2018.8802 C004 (in-hospital death interval crosses zero with P = .009; HR interval implausibly narrow)

K for report_internal_inconsistency (4): substantive_inconsistency 1 (jama.2018.14282 C001), minor_presentation 2, indeterminate 1. K for plan_material (7): minor_presentation 7.

L for retained protocol_report rows (54): substantive_difference 44, indeterminate 5, minor_presentation 3, left blank 2 (jama.2018.17075 C006 and jama.2018.6496 C006, both planned summary measures whose information is largely recoverable from reported data). Disclosed differences were retained with "disclosed" in column R, following the review decisions fixed before distribution.

## Discuss list

None. Candidates I considered for discuss and settled instead: jama.2018.0948 C001 (P belongs to a different model than the RD interval; retained as a probable, minor presentation issue), jama.2018.18020 C006 (whether the reported order/period terms are the planned interactions; retained with L indeterminate), jama.2018.6496 C005 (stopping rule; retained with L indeterminate), jama.2018.14280 C010 (vasopressor-day counting window; retained with K indeterminate), jama.2018.14282 C011 (outcome dropped between the superseded grant protocol and the final SAP; retained as a disclosed difference) and jama.2018.14282 C015 (unexplained subgroup denominators; retained as probable).

## Where I disagreed with or went beyond the AI card

- jama.2018.14280 C001: the card flagged only the ARDS and extrapulmonary-infection RRs and left the estimator open. Every printed RR and CI in Table 2 reproduces as P(low tidal volume | event) / P(low tidal volume | no event) with a log-Wald interval, i.e., the 2 x 2 table was transposed; the issue affects all 10 rows and the abstract.
- jama.2018.17075 C008: the card treated half-unit ranges of integer counts as reconciling P = .09. Counts are integers; the stated chi-square test gives P = 0.043, so the nonsignificance statement is not supported. Retained as probable and substantive.
- jama.2018.14282 C012: beyond the reciprocal HRs, raw counts confirm the direction error (IMV in non-hematologic patients 30.7% vs 44.9%, plotted under "favors standard").
- jama.2018.18020 C010: added that the period changes imply mexiletine worsened SCN4A transient paresis, contradicting Table 2 footnote d.
- jama.2018.8802 C004: added that the adjacent HR 0.96 (0.90-1.02) is implausibly precise for 34 deaths.
- jama.2018.14282 C013: added that the infection risk difference and P in the same row do not reproduce either.
- jama.2018.18020 C007: added that two patients counted as responders sit at a displayed 80%, which meets the protocol's "at least 80%" but not the supplement's ">80%".
- jama.2018.0156 C008: I initially misread the interval as excluding the point estimate; it does not, as the card notes. The interval is still wrong (mirrored relative to Wald and Newcombe).
- Exclusions where the card registered an issue: jama.2017.21906 C006, jama.2018.0948 C008, jama.2018.18020 C017, jama.2018.6496 C009 and C011, jama.2018.8802 C005, jama.2018.9128 C005 (reasons above), and jama.2018.0156 C002 (no plan-report conflict).

## Possible errors outside the candidate set (observed, not adjudicated)

- jama.2017.21906: in-hospital beta-blocker RD CI is 4.10-8.10 in the text and 4.10 to 8.40 in Table 2; discharge beta-blocker text gives 6.63 (4.43-8.95), OR 1.47 vs Table 2 6.69, OR 1.48; the eTable 1 footnote says "intervention minus control" for a missing-minus-complete comparison.
- jama.2018.0156: the final protocol defines technique failure as a composite including 28-day mortality, whereas the report's failure outcome is procedural failure only; the PP 28-day survival difference is printed 0.1 (computed 0.02); post hoc reclassification denominators sum to 2037, not 2040.
- jama.2018.0948: SCDE fluid threshold is >=60 mL/kg in the main text and >60 mL/kg in eTable 1; Table 3 places protocol-listed outcomes under a "Post hoc Outcomes" heading.
- jama.2018.14280: eTable 5 footnote reads "Data are mean ()"; subgroup mean differences on main p.6 are labelled IQR instead of 95% CI.
- jama.2018.14282: abstract respiratory-rate CI upper limit -0.2 vs -0.3 in the text.
- jama.2018.17075: eTable 12 multiple-imputation RR 1.00 (0.95 to 1.06) is implausibly narrow relative to its RD interval; the IMPACT-adjusted RR is labelled "unfavorable" in eTable 11 but "favorable" elsewhere; Table 1 Injury Severity Score for normothermia 20.0 (20.5-35.0) has the lower quartile above the median.
- jama.2018.18020: Table 1 SCN4A "Other" 5/11 printed as 46% (45.5%); the eTable 3 footnote describes patient 11's interval as (0;0) whereas the table prints (-12.24; 12.16).
- jama.2018.8802: Figure 1 says 3 hospitals declined and were replaced; the text says 3 hospitals had an "unexpected inability to conduct this trial".

## Template or source issues

- 2018::jama.2018.18020::C022 has no file or page in column C, as noted in the README; I located the rows from the card's source table and checked them on main p.7.
- jama.2018.9128 `joi180075supp1_prod.pdf`: the text layer silently drops numerals on some pages (e.g., p.36 "yielding [600] dyads per cohort", p.40 cohort and retention numbers) and p.67 has a character-shifted font ("VHYHQ" for "seven"). Values on those pages must be read from rendered images.
- jama.2018.14282 `joi180109supp1_prod.pdf`: the contents page lists pp.70-81 as the "final protocol", but those pages are the patient information and consent forms; the operative final specifications are in the published SAP (pp.84-127).
- jama.2018.0156 signed SAP (pp.126-134), jama.2018.17075 SAP update and correction (pp.183-187) and amendment pages (pp.140-162) are scanned without a usable text layer.
- jama.2018.6496: the supplied protocol p.21 leaves the interim-analysis sample size blank, while supplement 2 quotes the same section with "500".

## OCR and rendering use

- OCR (RapidOCR, 300 dpi): jama.2018.0156 supp1 pp.130, 131, 133 (scanned signed SAP; C002, C003, C007); jama.2018.17075 supp1 pp.152, 183, 184, 185, 187 (scanned amendment and SAP update; C011, C015). I checked the critical C007 line against a cropped render, which confirmed the missing minus sign.
- Rendered and viewed: jama.2017.21906 supp3 p.24 (eFigure 1A); jama.2018.14280 supp3 pp.5-9 (eTables 2, 4, 5); jama.2018.14282 main p.7 (Figure 3) and supp2 pp.2-4; jama.2018.17075 supp2 pp.5, 22 and supp1 p.192; jama.2018.18020 main pp.5, 7, 8 (Tables 1-2), supp2 p.5 (eTable 3), supp1 pp.39, 43 (protocol figures); jama.2018.6496 main pp.5-7 (Tables 1-3); jama.2018.8802 main p.5 (Figure 1); jama.2018.9128 supp1 pp.36, 40 (numerals missing from the text layer). Rendering was used wherever table alignment, signs, figure axes or flow-diagram labels mattered.

## Limitations

- Each candidate was judged by one reviewer from the supplied PDFs only; I did not consult registries, published SAPs cited but not supplied (e.g., the POLAR SAP in *Trials*), or trial authors, so several protocol_report judgments rest on the plan documents as supplied.
- Recomputations assume standard methods (Wald or log-Wald intervals, Pearson chi-square, normal or t back-calculation of P values). Where a paper used an unstated method, my confirmed/probable distinction reflects how strongly other rows of the same display identify the method.
- For protocol_report rows, L describes the difference only; it does not judge whether a change was justified, and disclosure was not treated as grounds for exclusion.
- Substantiveness (I) and downstream impact (J) are judgments about likely extraction use, not demonstrated effects on any synthesis.
- Observations outside the candidate set were noted while checking candidates and were not searched for systematically.
