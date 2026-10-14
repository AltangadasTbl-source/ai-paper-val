# Review summary: v.2.4.1 independent primary review, 2018 (reviewer R_A)

Reviewer R_A, year 2018, 10 papers, 115 candidates. I reviewed every candidate myself, first against the original PDFs in the source mirror and then against the candidate's card in `final_report_1_6_2.md`. I did not open the other reviewer's folder or workbook, any other year's or role's folder under `reviewer_runs/`, `human_adjudication_v_2_3_1/`, `human_adjudication/previous/`, `meta_report/`, the paper packages under `/home/juliz/ai-paper-val/2018/`, any `.ai_paper_validation/` folder, or git history.

## Files

- `judgments.json`: one row per candidate with D, E, H to L, a short note (R), the evidence inspected and the full rationale, including recomputations.
- `human_adjudication_v_2_4_1_2018_R_A_completed.xlsx`: completed workbook built from the judgments with `fill_review.py`.
- `REVIEW_SUMMARY.md`: this file.

Validation: `fill_review.py --check` reported 115 of 115 keys judged and none missing. `recalc_check.py` reported column G as `PRIMARY READY` for all 115 rows and Checks `Workflow status` as `PRIMARY READY`, with 0 discuss rows and 0 unfinished rows.

## Counts

Disposition: 105 retain, 10 exclude, 0 discuss.

| Review domain (E) | Retain | Exclude | Discuss | Total |
|---|---:|---:|---:|---:|
| statistical_results | 42 | 7 | 0 | 49 |
| report_internal_inconsistency | 3 | 1 | 0 | 4 |
| plan_material | 7 | 0 | 0 | 7 |
| protocol_report | 53 | 2 | 0 | 55 |
| Total | 105 | 10 | 0 | 115 |

Changes to E from the AI suggestion: none. I checked the domain of each candidate against the documents actually compared, and every suggested domain fit.

Exclusions:

- 2018::jama.2017.21906::C006: The LDL interval in eTable 1 is wider than the header-N calculation because LDL was measured in only 14 830 of 21 374 patients. About 245 patients with missing follow-up and an LDL value reproduce the printed interval.
- 2018::jama.2018.0156::C002: The airway outcomes are secondary in the protocol and the article, and the article analyses them in the safety population, as the SAP specifies. Report and plan do not conflict.
- 2018::jama.2018.0948::C001: P=.03 belongs to the baseline-adjusted rate ratio. The disclosed fallback model without baseline adjustment produced the risk-difference interval.
- 2018::jama.2018.0948::C008: The respiratory-rate CI is not adjusted for multiplicity and the Holm P is; the unadjusted P (.045) agrees with the CI.
- 2018::jama.2018.14280::C010: Q3=4 days of vasopressor use is compatible with counting calendar days over the randomization day plus days 1 to 3, the frame the eTables use.
- 2018::jama.2018.14282::C011: Intubated-patient mortality was a secondary outcome only in the superseded grant protocol. Under the governing final plan the report's post hoc label is correct, and the report discloses the redesign.
- 2018::jama.2018.18020::C017: The CI implies P=.047, which rounds to .05, so CI and P agree.
- 2018::jama.2018.6496::C009: The three intervals reproduce (for example, -10.3 to -0.5); limits shown as 0 are whole-percent rounding.
- 2018::jama.2018.8802::C005: The CI implies P of .0016 to .0019. The printed .001 is consistent with truncation, and there is no inferential conflict.
- 2018::jama.2018.9128::C005: The CI is unadjusted and the corrected P is a Benjamini-Hochberg value; all corrected P values reproduce.

## Outcome codes (retained rows)

**statistical_results (42 retained).**

- H: 33 confirmed_issue, 7 probable_issue, 2 indeterminate, 0 not_issue.
- I: 15 substantive, 25 minor_presentation, 2 indeterminate.
- H by I: confirmed and substantive 13; confirmed and minor 19; confirmed and indeterminate 1; probable and substantive 2; probable and minor 5; indeterminate and minor 1; indeterminate and indeterminate 1.
- J (all 42 answered): 11 direct, 10 possible, 20 unlikely, 1 unknown.

Confirmed or probable issues judged substantive (15):

- jama.2017.21906::C004: Two different adjusted contrasts for door-to-balloon time, with no mapping between them; probable.
- jama.2018.0156::C005: Per-protocol CIs in Table 2 (survival -10 to 9.7).
- jama.2018.0156::C008: The eTable 2 CI belongs to the reversed contrast.
- jama.2018.14280::C001: All 10 risk ratios are the transposed (allocation-given-outcome) ratio.
- jama.2018.14282::C012: Figure 3 HRs are oriented standard vs high-flow under headings that read the other way, and the "All patients" rows are swapped.
- jama.2018.14282::C013: The infection HR CI is about ten times too narrow.
- jama.2018.14282::C014: Pooled percentages are attributed to arms.
- jama.2018.17075::C008: Under the stated test the eTable 7 P is .043, not .09; probable.
- jama.2018.17075::C010: RR, CI and P are swapped between the two bleeding rows.
- jama.2018.18020::C001: The abstract reports 22% men; the true figure is 73%.
- jama.2018.18020::C007: Only 2 of the 3 reported nonresponders met the Bayesian rule.
- jama.2018.18020::C010: The SCN4A transient-paresis CI has a spurious minus sign.
- jama.2018.18020::C011: The lower Table 2 header reverses the effect direction.
- jama.2018.18020::C016: The SCN4A fifth-handgrip CI has a dropped minus sign.
- jama.2018.8802::C004: The in-hospital death CI and P conflict.

**K (10 retained).**

- report_internal_inconsistency (3): 1 substantive_inconsistency (14282::C001) and 2 minor_presentation.
- plan_material (7): 1 substantive_inconsistency (18020::C020, DSMB trigger) and 6 minor_presentation.

**L (53 retained protocol_report).** 41 substantive_difference, 6 minor_presentation, 5 indeterminate, 1 version_timing; none left blank. Following the fixed review decision, I retained disclosed plan–report changes and wrote "disclosed" in column R, for example 21906::C001, 0948::C002/C006/C007, 14280::C005/C007 and 9128::C002.

## Discuss list

None. I considered the following for discuss and resolved them as stated:

- 18020::C015: Retained with H indeterminate. Whether the dependent t-test effects should equal the difference of period means depends on the paired-data sets, which are not reported.
- 6496::C005: Retained with L indeterminate. Enrollment lasted about one year, so the planned calendar rule and the reported accrual rule were probably met together.
- 8802::C004: Retained as confirmed. The row is internally contradictory whichever limit is wrong.
- 21906::C004: Retained as probable. A marginal-mean versus quantile explanation is possible but is not stated.

## Where I disagreed with or went beyond the AI card

- 14280::C001: The card raised the reverse-conditioned ratio only as a diagnostic. I recomputed all 10 rows; every printed RR and CI matches the transposed ratio within 0.01, so I treat the issue as confirmed.
- 14282::C012: I showed that every one of the 26 forest rows is oriented standard/high-flow. This reverses the reading of the only significant interaction (IMV, no hematologic malignancy).
- 0156::C008: I identified the eTable 2 CI as exactly the reversed contrast (-0.44, -2.22 to 1.34).
- 18020::C010 and C016: I showed that each CI is centred on its estimate once one sign is corrected. C010 also contradicts footnote d ("all significant findings favored mexiletine").
- 18020::C007: Patients 8 and 20 have a posterior of exactly 80%. They meet the protocol's "at least 80%" rule but not the report's ">80%" rule.
- 2017.21906::C006: The card treated the header Ns as reproduction inputs. Table 1 shows that LDL was missing for about 31% of patients, so I excluded the candidate.
- 17075::C008: The card did not test alternatives. I found that the stated chi-square test gives P=.043 and that no tested variant gives .09.
- 0156::C007: The card treats the sign difference as a boundary conflict. Because the signed copy's own H0 and decision rule use -0.01, I rated it minor.
- 14282::C011 and 9128::C002 are similar situations that I resolved differently. In 14282 the earlier version was a superseded grant protocol, so I excluded the candidate. In 9128 the original protocol governed the trial at its start, so I retained it.

## Possible errors outside the candidate set (observed, not adjudicated)

- jama.2017.21906:
  - The p.6-7 text disagrees with Table 2: in-hospital β-blocker CI 4.10%-8.10% vs 4.10 to 8.40; discharge β-blocker RD 6.63 vs 6.69 and OR 1.47 vs 1.48.
  - The eTable 1 footnote reads "intervention minus control", but the columns are complete vs missing follow-up.
  - The eTable 6 footnote says "heparin" where the other tables say "anticoagulant".
- jama.2018.0156: In the eTable 2 reclassification row the ETI n is 1174, but 1022+155=1177. The main text p.6 calls the reclassification an "exclusion".
- jama.2018.14280: Main text p.6 labels the subgroup 95% CIs as "IQR".
- jama.2018.14282:
  - ICU and hospital mortality P values (.64, .77) do not match chi-square tests of the counts (.94, .88).
  - The abstract respiratory-rate CI upper limit is -0.2; the text gives -0.3.
- jama.2018.17075: The eTable 10 cell "1 (2)" is inconsistent with n=196 (0.5%).
- jama.2018.18020: Footnote d of Table 2 conflicts with the significant SCN4A transient-paresis effect that favors placebo.
- jama.2018.8802:
  - The in-hospital death HR 0.96 (0.90-1.02) is implausibly narrow for 34 events.
  - Results p.4 says three hospitals were replaced for "unexpected inability to conduct this trial"; Figure 1 says "declined to participate".

## Template or source issues

- 18020::C022: Column C has no file or page, a known limitation. I used the row list in the card's evidence table.
- The guide (Section 2.1) gives report paths under `.ai_paper_validation/`. In the source mirror the reports are at the paper-folder root; I used those.
- Several plan pages are scanned without a text layer:
  - 0156 supp1: 11 pages, including the signed SAP pp.126-134.
  - 17075 supp1: 27 pages, including the SAP update pp.183-187 and the 2010 amendment p.152, which is rotated.
  - 14282 supp1: 2 pages.
- 9128 supp1 p.67 has a font-shifted text layer (for example, "VHYHQ" for "seven"); the content is readable once decoded.
- 17075: The published SAP (Trials 2018) appears only as a citation (supp1 p.181) and is not supplied, which limited the check for C015.

## OCR and rendering use

- OCR (RapidOCR, 250-300 dpi):
  - 0156 supp1 pp.130, 131, 133 (signed SAP, scanned). I viewed a crop of p.130 to confirm the H1 "≥0.01" sign.
  - 17075 supp1 pp.152, 183, 184, 185, 187 (scanned amendment and SAP update). OCR of p.152 was garbled by the page rotation, so I read the rendered image.
- Rendering (fitz, 110-200 dpi) where layout or a single printed character mattered:
  - 21906 supp3 p.24 (eFigure 1A).
  - 14280 supp3 pp.6, 9 (eTable 2 PEEP cell; eTable 5 row alignment).
  - 17075 supp2 pp.5, 22 (KM window; "275" token) and supp1 pp.152, 191, 192 (rotated amendment; DSMB charts).
  - 18020 main pp.7-8 (Table 2 signs and CIs) and supp1 pp.39, 43 (DSMB and interim flowcharts).
  - 8802 main p.5 (Figure 1).
- All other pages were read from the PDF text layer and checked against neighbouring values.

## Limitations

- This is a single reviewer's reading. L and I involve judgment, and I did not calibrate them against anyone.
- Recomputations used Wald, chi-square, Fisher or t approximations where the authors' exact method was unstated or model-based (GEE, mixed models, Hodges-Lehmann). For adjusted estimates they are indicative only.
- I located "not reported" findings by text search and page reading of the supplied report documents. I OCR'd only the scanned plan pages relevant to each candidate, not every scanned page, so plan content on other scanned pages could have been missed.
- I did not look for amendments, registry entries or companion publications outside the supplied materials.
- I consulted cards only after forming an initial judgment. Where a card supplied a computation (for example, the 18020::C022 row list), I recomputed it rather than adopting it.
