---
title: "2025 Paper Errors — JSON-Style Concise Catalog"
subtitle: "Location, problem, and expected state for every classified finding"
author: "Generated from the local AI paper-validation archive"
date: "2026-08-14"
lang: en-US
toc: true
toc-depth: 1
numbersections: true
---

# Summary

This catalog is generated directly from all **14 original `final_report.html` files**. It converts all **71 verified error records** into a fixed JSON-style structure: actual location(s), the observed problem, and the expected corrected state. The **8 uncertain candidates** are listed separately and are not treated as established errors.

| Error type | Verified | Uncertain |
|---|---|---|
| Presentation inconsistency | 35 | 2 |
| Statistical reporting inconsistency | 15 | 5 |
| Arithmetic inconsistency | 10 | 1 |
| Cross-document inconsistency | 10 | 0 |
| Participant-flow inconsistency | 1 | 0 |

When the reports do not identify which conflicting number is authoritative, the `expected` field says that the locations must be reconciled against source output instead of inventing a replacement value. Counts remain report-level instances because the two ImmunoSep packages contain overlapping findings.

# Representative issues for mentor review

This section was selected after reading the detailed Verified sections in all 14 original `final_report.html` files. It prioritizes direct reproducibility, interpretive consequence, clear source location, and independence from duplicate package records. Each original error category contributes up to 10 representative issues; categories with fewer than 10 verified records contribute all available records.

| Assessment | Meaning for final output |
|---|---|
| Tier A | Strong final result: directly reproducible and scientifically or interpretively meaningful. |
| Tier B | Valid final result: useful, but mainly a localized reporting or editorial problem. |
| Tier C | Supporting example: clear but low-impact, or best retained only after deduplication/context review. |

| Selected assessment | Count |
|---|---|
| Tier A | 32 |
| Tier B | 8 |
| Tier C | 1 |

The `mentor_note` field explains why the item is—or is not—worth emphasizing in the final communication. Overlapping ImmunoSep findings are explicitly marked for deduplication.

## Presentation inconsistency: representative set (10)

### typical_001 — jama.2025.4390 / C01

> {  
> **"rank_in_category"**: "1",  
> **"source_title"**: "Figure 3 rate headings conflict with the displayed all-patient values",  
> **"representative_pattern"**: "Unit/scale label failure",  
> **"problem"**: "Figure 3's two columns labeled `Rate per 100 patient-years` do not display the rates reported for the same all-patient outcome in Table 2. The mismatch spans the principal subgroup figure and can materially mislead rate interpretation.",  
> **"final_output_value"**: "Tier A — strong final result",  
> **"mentor_note"**: "The main subgroup figure labels an exposure-like quantity as an event rate, materially changing interpretation."  
> }

### typical_002 — jama.2025.7710 / C01

> {  
> **"rank_in_category"**: "2",  
> **"source_title"**: "Primary composite outcome analysis-unit labels conflict",  
> **"representative_pattern"**: "Primary analysis-unit ambiguity",  
> **"problem"**: "Identical primary neonatal-composite records are labeled infants, women, and patients. Since the article separately enumerates randomized women and infants and accounts for multiple births, the terminology could obscure whether the primary analysis concerns randomized women or infants.",  
> **"final_output_value"**: "Tier A — strong final result",  
> **"mentor_note"**: "Women, infants, and patients are used for the same primary records; the scientific analysis unit becomes unclear."  
> }

### typical_003 — jama.2025.250116 / C04

> {  
> **"rank_in_category"**: "3",  
> **"source_title"**: "eFigure 8 panel B duplicates eFigure 7 despite a different outcome",  
> **"representative_pattern"**: "Duplicated outcome panel",  
> **"problem"**: "eFigure 8 panel B duplicates the entire six-row panel B from eFigure 7 despite eFigure 8's different 28-day-mortality outcome and different panel-A event cells.",  
> **"final_output_value"**: "Tier A — strong final result after deduplication",  
> **"mentor_note"**: "An entire interaction panel is copied to a different outcome. Use this as the canonical ImmunoSep duplication record and deduplicate the overlapping 24175 finding."  
> }

### typical_004 — jama.2025.15185 / C08

> {  
> **"rank_in_category"**: "4",  
> **"source_title"**: "eTable 4 mislabels the mRS odds ratio as an FMA mean difference",  
> **"representative_pattern"**: "Effect-measure mislabeling",  
> **"problem"**: "eTable 4 places the modified Rankin Scale estimate under a column headed as a mean difference on FMA, while the main article identifies the same value as an adjusted odds ratio.",  
> **"final_output_value"**: "Tier A — strong final result",  
> **"mentor_note"**: "Calling an odds ratio an FMA mean difference changes the statistical meaning of the displayed effect."  
> }

### typical_005 — jama.2025.16450 / C-04

> {  
> **"rank_in_category"**: "5",  
> **"source_title"**: "eTable 4 incorrectly defines RR as risk difference",  
> **"representative_pattern"**: "Measure-definition error",  
> **"problem"**: "The eTable 4 abbreviation line incorrectly expands `RR` as “risk difference”; within the same table and the main article, `RR` is defined and used as “relative risk,” while `RD` denotes “risk difference.”",  
> **"final_output_value"**: "Tier B — valid final reporting result",  
> **"mentor_note"**: "RR is expanded as risk difference although the article uses RR for relative risk and RD for risk difference; the error is clear but localized."  
> }

### typical_006 — jama.2025.20765 / C06

> {  
> **"rank_in_category"**: "6",  
> **"source_title"**: "Adverse-event analysis population and missingness are not identified",  
> **"representative_pattern"**: "Missing denominator/missingness definition",  
> **"problem"**: "eTable 10 does not identify the adverse-event analysis population or missingness rules needed to interpret its represented denominators.",  
> **"final_output_value"**: "Tier B — valid interpretability result",  
> **"mentor_note"**: "The omission prevents readers from identifying the adverse-event analysis population, although it does not by itself prove a numerical value wrong."  
> }

### typical_007 — jama.2025.24175 / 5

> {  
> **"rank_in_category"**: "7",  
> **"source_title"**: "Table 2 reverses the displayed direction of the 28-day mortality difference",  
> **"representative_pattern"**: "Direction/sign presentation error",  
> **"problem"**: "Table 2 lists precision immunotherapy before placebo but prints a positive 6.1% 28-day mortality difference even though precision minus placebo is −6.1 percentage points; this matters because the difference column’s sign is opposite the displayed group ordering.",  
> **"final_output_value"**: "Tier A — strong final result",  
> **"mentor_note"**: "The mortality difference sign is the reverse of the displayed arm ordering and is directly recoverable from the printed risks."  
> }

### typical_008 — jama.2025.24175 / 6

> {  
> **"rank_in_category"**: "8",  
> **"source_title"**: "Abstract attaches patient-incidence percentage to an event count",  
> **"representative_pattern"**: "Event count versus patient incidence",  
> **"problem"**: "The abstract grammatically attaches 88.8% to 1069 serious adverse events, whereas the body and eTable 13 attach that percentage to 245 of 276 patients; this matters because event count and patient incidence are different quantities.",  
> **"final_output_value"**: "Tier A — strong final result",  
> **"mentor_note"**: "The abstract attaches a patient percentage to an event count, conflating two different safety quantities."  
> }

### typical_009 — jama.2025.9110 / C03

> {  
> **"rank_in_category"**: "9",  
> **"source_title"**: "Figure 1 uses patient-level randomization wording although ICUs were randomized",  
> **"representative_pattern"**: "Randomization-unit misstatement",  
> **"problem"**: "The four downstream patient boxes use patient-level randomization language inconsistent with the article’s explicit ICU/cluster randomization unit.",  
> **"final_output_value"**: "Tier A — strong final result",  
> **"mentor_note"**: "Patient-level randomization wording conflicts with the stated ICU/cluster randomization and can mislead interpretation of the design."  
> }

### typical_010 — jama.2025.11178 / C09

> {  
> **"rank_in_category"**: "10",  
> **"source_title"**: "eTable 9 calls explicitly unadjusted relative risks adjusted",  
> **"representative_pattern"**: "Adjusted/unadjusted label conflict",  
> **"problem"**: "The table title directly conflicts with both its surrounding description and its own footnote.",  
> **"final_output_value"**: "Tier A — strong final result",  
> **"mentor_note"**: "The table title says adjusted while the surrounding description and footnote explicitly say unadjusted."  
> }

## Statistical reporting inconsistency: representative set (10)

### typical_011 — jama.2025.11178 / C04

> {  
> **"rank_in_category"**: "1",  
> **"source_title"**: "Multiple invalid standardized mean difference displays in Table 3",  
> **"representative_pattern"**: "Structurally invalid effect/CI displays",  
> **"location_1"**: "main article PDF, Table 3, PDF pp. 10-11 / JAMA pp. 601-602; standardization definition in footnote d on PDF p. 11.",  
> **"reported_numbers"**: "Table 3 examples: −0.25 (95% CI, −0.24 to 0.01), −0.36 (−0.35 to −0.12), and −0.27 (−0.26 to −0.12). Across the table: 8 point-estimate/CI containment failures, 18 reversed-endpoint cells, and 4 sign conflicts.",  
> **"problem"**: "Table 3 contains multiple directly demonstrable invalid SMD displays: eight containment failures, 18 reversed endpoint displays, and four sign conflicts under the table's stated definition.",  
> **"final_output_value"**: "Tier A — strong final result",  
> **"mentor_note"**: "Multiple SMD cells fail point-estimate containment, endpoint ordering, or sign preservation under the table's own definition."  
> }

### typical_012 — jama.2025.250116 / C05

> {  
> **"rank_in_category"**: "2",  
> **"source_title"**: "Within-high-stratum treatment effects labeled and interpreted as interaction tests",  
> **"representative_pattern"**: "Interaction-effect misinterpretation",  
> **"location_1"**: "supplement 2 PDF, PDF/printed p. 51, eFigure 7, panel A event cells, panel B labels/estimates, and caption B.",  
> **"location_2"**: "supplement 2 PDF, PDF/printed p. 53, eFigure 9, panel A event cells, panel B labels/estimates, and caption B.",  
> **"location_3"**: "main article PDF, PDF p. 7, journal p. 781, and main article PDF, PDF p. 8, journal p. 782, “Post Hoc and Subgroup Analyses.”",  
> **"reported_numbers"**: "Printed high-stratum ORs reconstruct as APACHE II ≥25: (12×32)/(26×8)=1.846≈1.85; CCI ≥5: (20×69)/(34×7)=5.798≈5.79; SOFA ≥10: (25×57)/(42×11)=3.084≈3.08. SOFA <10 gives OR≈2.019; the high/low ratio is ≈1.53, not 3.08.",  
> **"problem"**: "In eFigures 7 and 9, multiple entries labeled as severity-by-treatment interaction results reproduce treatment ORs within the high-severity strata; the main text interprets selected entries as interaction tests. The finding remains independently supported after excluding eFigure 8.",  
> **"final_output_value"**: "Tier A — strong final result",  
> **"mentor_note"**: "Within-stratum treatment effects are labeled and interpreted as interaction tests, altering the scientific claim."  
> }

### typical_013 — jama.2025.250116 / C03

> {  
> **"rank_in_category"**: "3",  
> **"source_title"**: "eFigure 9 APACHE point estimate outside its confidence interval",  
> **"representative_pattern"**: "Point estimate outside its CI",  
> **"location_1"**: "supplement 2 PDF, PDF/printed p. 53, eFigure 9, “90-Day Mortality According to Baseline Severity,” panel A APACHE II ≥25 row and panel B APACHE II ≥25 × Precision Immunotherapy row.",  
> **"reported_numbers"**: "eFigure 9B prints OR 0.11 (95% CI, 0.36–3.42), P=.86, with deaths 32/40 (placebo) and 31/38 (precision immunotherapy). The cells give OR≈1.107 and diagnostic 95% CI≈0.358–3.421.",  
> **"problem"**: "The published OR of 0.11 lies outside its own displayed 95% CI, while the displayed APACHE II ≥25 cells yield a diagnostic OR near 1.11 and an interval near 0.36-3.42.",  
> **"final_output_value"**: "Tier A — strong final result",  
> **"mentor_note"**: "The OR cannot lie below its own lower confidence limit; this later HTML record verifies an item that was uncertain in package 24175."  
> }

### typical_014 — jama.2025.15185 / C05

> {  
> **"rank_in_category"**: "4",  
> **"source_title"**: "Estimands 3 and 4 use a population label inconsistent with its definition",  
> **"representative_pattern"**: "Estimand population mismatch",  
> **"location_1"**: "supplement 3 PDF, PDF p. 12, eTable 2 population definitions, Full analysis set definition; supplement 3 PDF, PDF p. 13, eTable 2 results, Estimands 1, 3, and 4, Population, Intercurrent Events, and Number of participants columns; supplement 3 PDF, PDF p. 16, eTable 5, row “Participants died,” Overall/Placebo/Levodopa columns.",  
> **"reported_numbers"**: "Full analysis set: Estimand 1 N=582; Estimands 3–4 N=610; deaths=28 (17 placebo, 11 levodopa); 610−28=582. Printed effects: −0.98 (95% CI, −3.77 to 1.81) and win ratio 1.06 (0.86 to 1.26).",  
> **"problem"**: "eTable 2 labels Estimands 3 and 4 “Full analysis set,” although that set is defined as excluding deaths and both estimands report `N=610`, incorporating the 28 deaths.",  
> **"final_output_value"**: "Tier A — strong final result",  
> **"mentor_note"**: "The Full analysis set label conflicts with its death-exclusion definition and the displayed N."  
> }

### typical_015 — jama.2025.15185 / C06

> {  
> **"rank_in_category"**: "5",  
> **"source_title"**: "Estimand 11's written conjunction cannot produce its reported N",  
> **"representative_pattern"**: "Logical rule cannot produce reported N",  
> **"location_1"**: "supplement 3 PDF, PDF p. 14, eTable 3, Estimand 11, Intercurrent Events and Number of participants columns; supplement 3 PDF, PDF p. 13, eTable 2, Estimands 1, 6, and 7, Number of participants column. Comparator: main article PDF, PDF p. 4 (journal p. 1526), Statistical Analyses, post hoc estimand sentence.",  
> **"reported_numbers"**: "Base N=582; Estimand 6 N=496 (86 medication failures); Estimand 7 N=450 (132 rehabilitation failures); Estimand 11 N=395 (187 excluded). Under the printed AND rule, at most 86 can be excluded, so retained N must be ≥496, not 395.",  
> **"problem"**: "eTable 3 says Estimand 11 excludes participants meeting both low-rehabilitation and low-medication conditions, but excluding only that intersection cannot yield the reported `N=395`.",  
> **"final_output_value"**: "Tier A — strong final result",  
> **"mentor_note"**: "The written conjunction and the reported analysis population are mathematically incompatible."  
> }

### typical_016 — jama.2025.20765 / C08

> {  
> **"rank_in_category"**: "6",  
> **"source_title"**: "“Intention to treat” label is retained after deaths are excluded",  
> **"representative_pattern"**: "Incorrect ITT designation",  
> **"location_1"**: "main article PDF, PDF p. 3, journal p. 338, Statistical Analysis; main article PDF, PDF p. 4, journal p. 339, Figure 1; main article PDF, PDF p. 6, journal p. 341, Table 2. supplement 2 PDF, PDF p. 13 and supplement 2 PDF, PDF p. 14, eTable 9 and notes.",  
> **"reported_numbers"**: "Primary ITT denominators: 720 and 360; deaths: 25 and 27. eTable 9 uses 695 and 333, exactly 720−25 and 360−27; primary counts are 300/695=43.2% and 55/333=16.5%.",  
> **"problem"**: "eTable 9 labels a population from which precisely the reported deaths were removed as “intention to treat,” despite the main article presenting death exclusion as a distinct post hoc analysis.",  
> **"final_output_value"**: "Tier A — strong final result",  
> **"mentor_note"**: "A death-excluded post hoc population is labeled intention-to-treat, changing the meaning of the analysis set."  
> }

### typical_017 — jama.2025.19563 / C-04

> {  
> **"rank_in_category"**: "7",  
> **"source_title"**: "eTable 11 contains incompatible age and significance footnotes",  
> **"representative_pattern"**: "Conflicting inferential footnotes",  
> **"location_1"**: "supplement 2 PDF, PDF p. 53, eTable 11 and age row; and supplement 2 PDF, the same PDF, p. 54, footnotes 1-2.",  
> **"reported_numbers"**: "eTable 11 groups: N=151 vs N=149. Age is assigned P=.010 in footnote 1 and P=.014 in footnote 2; sex has P=.041, contradicting footnote 2's statement that all other P values exceed .05.",  
> **"problem"**: "eTable 11 assigns age two unexplained P values and includes an “all other” significance statement that conflicts with its reported significant sex result.",  
> **"final_output_value"**: "Tier B — valid final reporting result",  
> **"mentor_note"**: "Age receives two unexplained P values and the all-other statement conflicts with the reported sex significance."  
> }

### typical_018 — jama.2025.20765 / C04

> {  
> **"rank_in_category"**: "8",  
> **"source_title"**: "Main-text nausea and diarrhoea percentages do not reproduce from eTable 10",  
> **"representative_pattern"**: "Narrative/table percentage mismatch",  
> **"location_1"**: "main article PDF, PDF p. 5, journal p. 340, Adverse Events; supplement 2 PDF, PDF p. 15, eTable 10, Nausea and Diarrhoea blocks.",  
> **"reported_numbers"**: "Main text: nausea 23.0% vs 22.3%; diarrhea 7.5% vs 7.5%. eTable 10: nausea 161/699=23.0% vs 71/334=21.3%; diarrhea 51/699=7.3% vs 25/334=7.5%.",  
> **"problem"**: "The eTable 10 counts reproduce the main-text mHealth nausea and control diarrhoea percentages, but yield 21.3% rather than 22.3% for control nausea and 7.3% rather than 7.5% for mHealth diarrhoea.",  
> **"final_output_value"**: "Tier B — valid final numerical-reporting result",  
> **"mentor_note"**: "Two adverse-event percentages cannot be reproduced from the displayed table counts, but the absolute differences are small."  
> }

### typical_019 — jama.2025.9110 / C04

> {  
> **"rank_in_category"**: "9",  
> **"source_title"**: "Bayesian primary-outcome row labels median/IQR values as mean (SD)",  
> **"representative_pattern"**: "Summary-statistic/model mismatch",  
> **"location_1"**: "main article PDF, PDF p. 7, journal p. 325, Table 2, Primary outcome secondary analyses, Bayesian quantile mixed-model row; comparison in supplement 3 PDF, PDF p. 27, supplemental p. 27, eFigure 6.",  
> **"reported_numbers"**: "Bayesian row: 62.0 (0–77) vs 64.0 (0–77), median difference −1.50 (95% CrI, −3.86 to 0.90), but the row label says mean (SD). The adjacent row and eFigure 6 identify median (IQR)/median difference.",  
> **"problem"**: "`mean (SD)` is inconsistent with the displayed group summaries and the median-based Bayesian analysis; the completed record supports `median (IQR)` as the intended descriptive label.",  
> **"final_output_value"**: "Tier A — strong final result",  
> **"mentor_note"**: "A median/IQR Bayesian outcome is labeled mean (SD), misdescribing both the summaries and the model-based estimand."  
> }

### typical_020 — jama.2025.11178 / C05

> {  
> **"rank_in_category"**: "10",  
> **"source_title"**: "Results text and Table 3 report different 3-month SMDs",  
> **"representative_pattern"**: "Repeated effect estimate mismatch",  
> **"location_1"**: "main article PDF, Results—Secondary Outcomes, PDF p. 7 / JAMA p. 598, and Table 3, PDF p. 10 / JAMA p. 601.",  
> **"reported_numbers"**: "Results text gives 3-month pain-severity SMDs −0.26 and −0.36; Table 3 gives −0.25 and −0.34 for the same comparisons.",  
> **"problem"**: "The main article gives discordant published SMD point estimates for the same two effects.",  
> **"final_output_value"**: "Tier B — valid final reporting result",  
> **"mentor_note"**: "The text and table publish different SMDs for the same outcome, time point, and comparison; authoritative output is needed to choose the correction."  
> }

## Arithmetic inconsistency: representative set (10)

### typical_021 — jama.2025.4390 / C05

> {  
> **"rank_in_category"**: "1",  
> **"source_title"**: "British Columbia city counts exceed the province header by one",  
> **"representative_pattern"**: "Category-total reconstruction failure",  
> **"location_1"**: "supplement 3 PDF, PDF p. 22, eFigure 1, Location of Participating Practices, British Columbia column; comparison with supplement 3 PDF, the same file, PDF p. 27, eTable 1, recruitment footnote.",  
> **"reported_numbers"**: "British Columbia header=43; 14 city counts are 12, 1, 1, 1, 1, 1, 1, 1, 4, 12, 1, 3, 3, 2, summing to 44. Province headers 43+326+22+29+16=436, matching eTable 1's 436 providers.",  
> **"problem"**: "The British Columbia city-level counts sum to 44, not the displayed province total of 43.",  
> **"final_output_value"**: "Tier B — valid but low-impact final result",  
> **"mentor_note"**: "The city counts sum to 44 rather than the province total of 43; this is clear but localized."  
> }

### typical_022 — jama.2025.4390 / C07

> {  
> **"rank_in_category"**: "2",  
> **"source_title"**: "The bedtime calcium-channel-blocker percentage does not reproduce",  
> **"representative_pattern"**: "Percentage reconstruction failure",  
> **"location_1"**: "main article PDF, PDF p. 6, journal p. 2066, Table 1 continued, Calcium channel blocker; repeated in supplement 3 PDF, PDF p. 32, eTable 3, same row.",  
> **"reported_numbers"**: "Bedtime calcium-channel blocker: 479/1677=28.5629%→28.6%, but 28.2% is printed in main Table 1 and supplement eTable 3. Controls: 489/1680=29.1%; 968/3357=28.8%.",  
> **"problem"**: "Given the printed numerator and denominator, the bedtime percentage should arithmetically round to 28.6%; the displayed 28.2% is not reproducible and is repeated in two tables.",  
> **"final_output_value"**: "Tier A — strong final result",  
> **"mentor_note"**: "The printed percentage is nonreproducible and is propagated into two tables."  
> }

### typical_023 — jama.2025.9110 / C01

> {  
> **"rank_in_category"**: "3",  
> **"source_title"**: "Period 3 augmented-protein sex counts do not reconcile to the displayed denominator",  
> **"representative_pattern"**: "Subcategory counts below denominator",  
> **"location_1"**: "supplement 3 PDF, PDF p. 10, supplemental p. 10, eTable 4, “Period 3 – Augmented Protein” Sex rows; aggregate comparison in main article PDF, PDF p. 5, journal p. 323, Table 1, Sex rows.",  
> **"reported_numbers"**: "Period 3 augmented protein: n=551; male 359 (65.2%) + female 190 (34.5%)=549, leaving 2. Across periods: male 1069 vs Table 1's 1070; female 610 vs 611; combined 1679 vs 1681.",  
> **"problem"**: "The displayed Period 3 augmented-protein sex counts are two below the displayed period denominator and also leave one male and one female unreconciled against the aggregate Table 1 totals.",  
> **"final_output_value"**: "Tier B — valid final result",  
> **"mentor_note"**: "The sex counts leave two records unexplained and also fail the aggregate cross-check."  
> }

### typical_024 — jama.2025.9110 / C02

> {  
> **"rank_in_category"**: "4",  
> **"source_title"**: "Protocol-deviation participant percentage matches the event count rather than the participant count",  
> **"representative_pattern"**: "Wrong numerator used for percentage",  
> **"location_1"**: "supplement 3 PDF, PDF p. 16, supplemental p. 16, eTable 8, “Total protocol deviations” in the Augmented Protein column.",  
> **"reported_numbers"**: "Augmented-protein denominator=1681; participants with ≥1 deviation=151 (printed 9.4%), events=158. 151/1681=8.9827%→9.0%; 158/1681=9.3992%→9.4%.",  
> **"problem"**: "The printed `9.4%` beside 151 participants is not the one-decimal percentage of 151/1681 and numerically equals the one-decimal percentage of 158/1681.",  
> **"final_output_value"**: "Tier A — strong final result",  
> **"mentor_note"**: "The percentage beside participant count 151 numerically matches 158 events, indicating a quantity-level mix-up."  
> }

### typical_025 — jama.2025.11178 / C03

> {  
> **"rank_in_category"**: "5",  
> **"source_title"**: "The current-depression percentage is incompatible with its count and denominator",  
> **"representative_pattern"**: "Gross count/percentage incompatibility",  
> **"location_1"**: "results workbook, sheet eTable 3, E3 and A82:E83; footnote a at A110.",  
> **"reported_numbers"**: "Workbook eTable 3: All Observed N=1568; current depression 711 (73.2%); missing=2. With missing excluded, 711/(1568−2)=45.402%→45.4%; 162+243+711=1116, matching the overall count.",  
> **"problem"**: "The error is localized to the percentage printed in E82. The directly recoverable display is `711 (45.4)`. The count 711 is internally supported; the supplied workbook does not establish where `73.2` originated.",  
> **"final_output_value"**: "Tier A — strong final result",  
> **"mentor_note"**: "The supported count gives 45.4%, not 73.2%; the corrected display is directly recoverable."  
> }

### typical_026 — jama.2025.15185 / C01

> {  
> **"rank_in_category"**: "6",  
> **"source_title"**: "eTable 6 overall adverse-event total is one event short",  
> **"representative_pattern"**: "Overall total one below every reconstruction",  
> **"location_1"**: "supplement 3 PDF, PDF p. 17, eTable 6, columns Overall, Placebo, and Levodopa, rows n, AE intensity, AE outcome, and Drug relation. Comparators: main article PDF, PDF p. 6 (journal p. 1528), Table 2, “Prespecified adverse events of interest”; and main article PDF, PDF p. 7 (journal p. 1529), Adverse Events continuation.",  
> **"reported_numbers"**: "Supplement overall=145, but arm totals 67+79=146; intensity 58+86+2=146; outcome 1+29+116=146; drug relation 2+66+23+2+39+14=146. Main article also reports 146.",  
> **"problem"**: "The results supplement reports 145 prespecified adverse events overall, although both arm totals and every displayed classification block sum to 146.",  
> **"final_output_value"**: "Tier A — strong final result",  
> **"mentor_note"**: "Arm totals and every classification block independently give 146 rather than the printed 145."  
> }

### typical_027 — jama.2025.19563 / C-01

> {  
> **"rank_in_category"**: "7",  
> **"source_title"**: "eTable 12 reports 10 of 59 as 19%",  
> **"representative_pattern"**: "Simple denominator-rule failure",  
> **"location_1"**: "supplement 2 PDF, PDF p. 55, eTable 12, second component-pattern row, Human-led DPP column.",  
> **"reported_numbers"**: "Human-led DPP N=59; cell 10 (19%). Direct calculation: 10/59=16.949%→17%; the adjacent row already prints 10 (17%), and all seven column counts sum to 59.",  
> **"problem"**: "The second-row Human-led DPP entry `10 (19%)` does not reconcile with its stated denominator; it rounds to 17% under the table’s denominator rule.",  
> **"final_output_value"**: "Tier A — strong final result",  
> **"mentor_note"**: "The displayed 10/59 is approximately 17%, not 19%, under the table's stated rule."  
> }

### typical_028 — jama.2025.20765 / C02

> {  
> **"rank_in_category"**: "8",  
> **"source_title"**: "Site 2008 death percentage is incompatible with its cluster denominator",  
> **"representative_pattern"**: "Cluster percentage denominator failure",  
> **"location_1"**: "supplement 2 PDF, PDF p. 9, eTable 6, Control/site 2008 row; supplement 2 PDF, PDF p. 8, eTable 5, Control/site 2008 row. Corroborating cluster size: main article PDF, PDF p. 5, journal p. 340, Table 1.",  
> **"reported_numbers"**: "Control site 2008: 5 deaths among 40 participants, printed as 5 (7.5%). 5/40=12.5%; 7.5% of 40 corresponds to 3 deaths. A neighboring 5-death site is printed as 12.5%.",  
> **"problem"**: "The displayed `5 (7.5)` is arithmetically inconsistent with the 40-person site denominator; the diagnostic percentage is 12.5%.",  
> **"final_output_value"**: "Tier A — strong final result",  
> **"mentor_note"**: "The printed 5/40 percentage should be 12.5%, not 7.5%."  
> }

### typical_029 — jama.2025.20765 / C03

> {  
> **"rank_in_category"**: "9",  
> **"source_title"**: "Death-cause percentages do not reproduce from the printed column totals",  
> **"representative_pattern"**: "Repeated cause-percentage error",  
> **"location_1"**: "supplement 2 PDF, PDF p. 6, eTable 4, “Causes of deaths among two study groups.”",  
> **"reported_numbers"**: "Usual-care total=27 deaths; Drug user=1 (7.4%) and Severe pneumonia=1 (7.4%). Each is 1/27=3.7037%→3.7%; 7.4% corresponds to 2/27. Printed usual-care percentages sum to 107.3%.",  
> **"problem"**: "eTable 4 contains arithmetic inconsistencies, most clearly the two usual-care `1 (7.4%)` cells, for which conventional one-decimal calculation gives 3.7% each.",  
> **"final_output_value"**: "Tier A — strong final result",  
> **"mentor_note"**: "Two 1/27 cells are reported as 7.4% although each should be 3.7%."  
> }

### typical_030 — jama.2025.250116 / C02

> {  
> **"rank_in_category"**: "10",  
> **"source_title"**: "Day-15 SII odds-ratio point estimate",  
> **"representative_pattern"**: "Odds-ratio transcription/reconstruction failure",  
> **"location_1"**: "supplement 2 PDF, PDF/printed p. 22, eTable 10, section “≥1.4-point decrease of mean SOFA of days 2 to 15 from baseline day 1,” SII row, the two treatment columns and OR unadjusted (95% CI) column.",  
> **"reported_numbers"**: "Responders: 40/106 (37.7%) vs 29/122 (23.8%); printed unadjusted OR 1.194 (95% CI, 1.09–3.45), P=.030. From nonresponders 66 and 93: OR=(40×93)/(66×29)=1.9436; diagnostic CI≈1.10–3.45.",  
> **"problem"**: "The displayed counts yield a diagnostic crude OR of approximately 1.94, whereas the table prints 1.194; the printed CI is approximately compatible with the former.",  
> **"final_output_value"**: "Tier A — strong final result after deduplication",  
> **"mentor_note"**: "The counts support an OR near 1.94 rather than 1.194. Deduplicate against the overlapping 24175 item 2."  
> }

## Cross-document inconsistency: representative set (10)

### typical_031 — jama.2025.9110 / C05

> {  
> **"rank_in_category"**: "1",  
> **"source_title"**: "Main-table ventilation summaries are labeled mean (SD) while the supplement identifies median (IQR) summaries",  
> **"representative_pattern"**: "Summary-statistic definition changes across documents",  
> **"location_1"**: "main article PDF, PDF p. 7, journal p. 325, Table 2, “Duration of invasive ventilation” row; supplement 3 PDF, PDF p. 18, supplemental p. 18, eTable 10 and footer; and supplement 3 PDF, PDF p. 4, supplemental p. 4, eMethods, “Duration of invasive ventilation”.",  
> **"reported_numbers"**: "Main Table 2 labels mean (SD) but prints 84.0 (35.0–178.9) vs 78.0 (33.2–161.0); model effect is mean difference 6.8 (95% CI, −3.0 to 16.5). Supplement eTable 10 defines the group summaries as median (IQR).",  
> **"problem"**: "The main article’s `mean (SD)` label conflicts with the displayed three-number group summaries and the supplement’s median (IQR) convention for the same outcome.",  
> **"final_output_value"**: "Tier A — strong final result",  
> **"mentor_note"**: "The main article says mean (SD) while the supplement identifies median (IQR) for the same ventilation summaries."  
> }

### typical_032 — jama.2025.9663 / C1

> {  
> **"rank_in_category"**: "2",  
> **"source_title"**: "Incorrect supplementary-figure citation for time to death",  
> **"representative_pattern"**: "Wrong supplementary-figure destination",  
> **"location_1"**: "main article PDF — PDF p. 6, journal p. 403, “Primary and Secondary Outcomes”; supplement 2 PDF — PDF p. 11, eFigure 4; and supplement 2 PDF — PDF p. 12, eFigure 5.",  
> **"reported_numbers"**: "Main text: time-to-death HR 1.01 (95% CI, 0.96–1.05), cited as eFigure 4. eFigure 4 is oxygenation (N=2489); eFigure 5 is mortality and prints HR 1.01 (0.96–1.05), P=.82.",  
> **"problem"**: "The main-text time-to-death statement points readers to eFigure 4, while the matching mortality result is in eFigure 5.",  
> **"final_output_value"**: "Tier C — supporting/editorial example",  
> **"mentor_note"**: "The error is unambiguous but only redirects readers from eFigure 4 to eFigure 5; scientific impact is limited."  
> }

### typical_033 — jama.2025.15185 / C02

> {  
> **"rank_in_category"**: "3",  
> **"source_title"**: "Supplementary stroke-type arm counts do not reconcile",  
> **"representative_pattern"**: "Arm counts conflict across documents",  
> **"location_1"**: "supplement 3 PDF, PDF p. 10, eTable 1, rows “Stroke ischemic – No. (%)” and “Stroke hemorrhagic – No. (%)”, columns Overall, Placebo, and Levodopa. Comparator: main article PDF, PDF p. 4 (journal p. 1526), Table 1, “Type of stroke,” rows Ischemic and Hemorrhagic, Levodopa and Placebo columns.",  
> **"reported_numbers"**: "Supplement Overall/placebo/levodopa: ischemic 519/259/263 and hemorrhagic 91/44/44. Main levodopa values are 260 and 47. Only 259+260=519 and 44+47=91; the supplement arm values miss each overall by 3.",  
> **"problem"**: "The supplement reports levodopa stroke-type counts of 263 ischemic and 44 hemorrhagic, whereas the main article reports 260 and 47; only the main-article arm values reproduce the supplement's Overall counts.",  
> **"final_output_value"**: "Tier A — strong final result",  
> **"mentor_note"**: "Only the main-article arm counts reproduce the supplement's overall totals, making the supplement internally and externally inconsistent."  
> }

### typical_034 — jama.2025.15185 / C03

> {  
> **"rank_in_category"**: "4",  
> **"source_title"**: "Onset-to-randomization timing differs by 4 to 5 median days",  
> **"representative_pattern"**: "Large timing discrepancy across documents",  
> **"location_1"**: "main article PDF, PDF p. 4 (journal p. 1526), Table 1 continuation, row “Time from stroke onset to randomization, median (IQR), d.” Comparator: supplement 3 PDF, PDF p. 11, eTable 1 continuation, row “Median time from stroke onset to randomization \[IQR\].” The supplement row does not itself print a day suffix; its values are compared to the main article's explicitly day-denominated row.",  
> **"reported_numbers"**: "Main article: levodopa 3.0 days (IQR 2.0–5.0), placebo 3.0 (2.0–5.0). Supplement: levodopa 7 (5–11), placebo 8 (5–10): median differences of 4 and 5 days.",  
> **"problem"**: "The main article reports a median of 3 days from stroke onset to randomization in each arm, while the identically described supplement row reports 7 days for levodopa and 8 days for placebo.",  
> **"final_output_value"**: "Tier A — strong final result",  
> **"mentor_note"**: "The same onset-to-randomization variable is reported as 3 days in the article and 7/8 days in the supplement."  
> }

### typical_035 — jama.2025.15185 / C04

> {  
> **"rank_in_category"**: "5",  
> **"source_title"**: "PRAI placebo numerator differs by one participant",  
> **"representative_pattern"**: "One-participant numerator mismatch",  
> **"location_1"**: "main article PDF, PDF p. 6 (journal p. 1528), Secondary Outcomes, patient-reported assessment of relevance of motor improvement sentence. Comparator: supplement 3 PDF, PDF p. 15, eTable 4, row “PRAI; no (relevant) improvement, 3 months, N. (%),” Placebo and Levodopa columns.",  
> **"reported_numbers"**: "Placebo response: main article 52/270=19.259%→19%; supplement 51/270=18.889%→18.89%. Difference: 1 participant, or 0.370 percentage points. Levodopa agrees at 51/276.",  
> **"problem"**: "The main article reports 52 of 270 placebo participants with no improvement or no relevant improvement, whereas eTable 4 reports 51 of 270.",  
> **"final_output_value"**: "Tier B — valid but low-impact final result",  
> **"mentor_note"**: "The same placebo response is 52/270 in the article and 51/270 in the supplement."  
> }

### typical_036 — jama.2025.19563 / C-06

> {  
> **"rank_in_category"**: "6",  
> **"source_title"**: "Figure 3B and eTable 14 use unreconciled HbA1c analysis-set sizes",  
> **"representative_pattern"**: "Unreconciled analysis-set sizes",  
> **"location_1"**: "main article PDF, PDF p. 8, journal p. 2086, Figure 3B, “Change in HbA1c at 12 mo.”",  
> **"location_2"**: "main article PDF, PDF p. 3, journal p. 2081, Outcomes section.",  
> **"location_3"**: "supplement 2 PDF, PDF p. 57, eTable 14, “Change in A1C (Baseline to 12 Months) (%).”",  
> **"reported_numbers"**: "Figure 3B axes extend to Human 149 and AI 151; visible nonzero bars are at least 117 and 121. eTable 14 HbA1c-change N=103 and N=106, respectively: at least 14 and 15 fewer; its other outcomes use N=149 and N=151.",  
> **"problem"**: "The figure demonstrably represents a larger HbA1c analysis set than eTable 14 reports for the co-cited HbA1c-change outcome, without a caption explanation reconciling the inclusion rule.",  
> **"final_output_value"**: "Tier A — strong final result",  
> **"mentor_note"**: "The figure and co-cited table use different HbA1c analysis populations without explaining the inclusion rule."  
> }

### typical_037 — jama.2025.19563 / C-07

> {  
> **"rank_in_category"**: "7",  
> **"source_title"**: "Supplement uses percent notation where the main article defines an absolute percentage-point HbA1c threshold",  
> **"representative_pattern"**: "Percent versus percentage-point definition",  
> **"location_1"**: "supplement 2 PDF, PDF p. 34, eFigure 3 row label and footnote 3.",  
> **"location_2"**: "main article PDF, PDF p. 3, journal p. 2081, Outcomes section.",  
> **"location_3"**: "main article PDF, PDF p. 7, journal p. 2085, Figure 2 row and footnote c.",  
> **"reported_numbers"**: "Same component counts in both displays: AI 35/130 and Human 35/130. Main article threshold: absolute HbA1c decrease ≥0.2 percentage points; supplement says 0.2%. Example: 0.2% relative to 6.0% is 0.012 percentage points, not 0.2.",  
> **"problem"**: "The main article and supplement label the same HbA1c component differently: absolute percentage points in the main article and percent notation in the supplement.",  
> **"final_output_value"**: "Tier A — strong final result",  
> **"mentor_note"**: "The supplement changes an absolute percentage-point threshold into percent notation, altering the clinical scale."  
> }

### typical_038 — jama.2025.19843 / V-02

> {  
> **"rank_in_category"**: "8",  
> **"source_title"**: "Day-30 MACE definition and placebo count cannot be reconciled",  
> **"representative_pattern"**: "Composite definition/count impossibility",  
> **"location_1"**: "Main-article composite definition: main article PDF — PDF p. 3, journal p. 62, Methods, “Outcomes,” right column, paragraph beginning “Predefined secondary outcomes included.”",  
> **"location_2"**: "Supplementary composite count: supplement 3 PDF — PDF p. 5, eTable 3, “Secondary End Points,” row “Major adverse cardiovascular events during first 30 days,” Placebo column, denominator in the column header.",  
> **"location_3"**: "Supplementary component count: supplement 3 PDF — PDF p. 5, eTable 3, row “Dialysis by day 30,” Placebo column.",  
> **"location_4"**: "Supplementary figure definition and event count: supplement 3 PDF — PDF p. 13, eFigure 4, title and D30 panel, cumulative number of events at day 30.",  
> **"reported_numbers"**: "Placebo N=104; day-30 MACE 36 (34.6%) and dialysis 38 (36.5%). MACE is 2 participants and 1.9 percentage points below a stated component. eFigure 4 repeats 36 but omits dialysis from its MACE definition.",  
> **"problem"**: "The main article defines dialysis as a day-30 major adverse cardiovascular event component, but the results supplement reports fewer placebo participants with day-30 MACE than with dialysis and repeats the MACE count in a figure whose definition omits dialysis; the definition, count, and display therefore cannot be jointly verified.",  
> **"final_output_value"**: "Tier A — highest-priority mentor result",  
> **"mentor_note"**: "MACE is reported smaller than dialysis even though dialysis is defined as a MACE component; the article and figure also disagree on the definition."  
> }

### typical_039 — jama.2025.20765 / C01

> {  
> **"rank_in_category"**: "9",  
> **"source_title"**: "Omitted mHealth cluster in the prior-quit-attempt table",  
> **"representative_pattern"**: "Omitted cluster changes analysis totals",  
> **"location_1"**: "supplement 2 PDF, PDF p. 4, eTable 2, both study-arm blocks; supplement 2 PDF, PDF p. 8, eTable 5, site 2012 row. main article PDF, PDF p. 5, journal p. 340, Table 1, cluster totals, participant totals, and “Attempted to quit in past” row.",  
> **"reported_numbers"**: "Main Table 1: 18 mHealth clusters×40=720 participants, prior quit attempts 178 (24.7%). eTable 2: 17 clusters, 680 participants, Yes=168 and No=512. Shortfalls: 1 cluster, 40 participants, 10 Yes, 30 No.",  
> **"problem"**: "eTable 2 omits one mHealth cluster relative to Table 1 and eTable 5, displaying 680 participants and 168 prior-attempt Yes responses rather than 720 and 178.",  
> **"final_output_value"**: "Tier A — strong final result",  
> **"mentor_note"**: "One mHealth cluster and 40 participants disappear from one table relative to two corroborating displays."  
> }

### typical_040 — jama.2025.20765 / C05

> {  
> **"rank_in_category"**: "10",  
> **"source_title"**: "The adverse-event direction statement is reversed for irritability and anxiety",  
> **"representative_pattern"**: "Reversed adverse-event direction statement",  
> **"location_1"**: "main article PDF, PDF p. 5, journal p. 340, Adverse Events; supplement 2 PDF, PDF p. 15, eTable 10, Dry mouth, Irritability, and Anxiety blocks.",  
> **"reported_numbers"**: "Any-grade occurrence: dry mouth 438/699=62.7% vs 186/334=55.7%; irritability 283/699=40.5% vs 145/334=43.4%; anxiety 233/699=33.3% vs 123/334=36.8%. Text says all three are more common in mHealth, but the latter two are lower.",  
> **"problem"**: "The main-text direction statement is inconsistent with any-grade irritability and anxiety occurrence, both of which are lower in mHealth; dry mouth alone has the stated direction.",  
> **"final_output_value"**: "Tier A — strong final result",  
> **"mentor_note"**: "The narrative direction for irritability and anxiety is opposite the tabled occurrence and therefore reverses the substantive safety statement."  
> }

## Participant-flow inconsistency: representative set (1)

### typical_041 — jama.2025.11178 / C01

> {  
> **"rank_in_category"**: "1",  
> **"source_title"**: "Follow-up-pattern counts do not reconcile",  
> **"representative_pattern"**: "Mutually exclusive flow categories do not partition N",  
> **"location_1"**: "supplement 4 PDF, PDF p. 7, eTable 1; corroboration in main article PDF, PDF p. 5, Figure 1, and results workbook, sheet eTable 3, B2:E3.",  
> **"reported_numbers"**: "Overall N=2331; pattern rows 295+188+283+1568=2334 (+3); nonzero rows 188+283+1568=2039 vs 2036 (+3). painTRAINER: 777 vs N=776 (+1); Health Coach: 780 vs N=778 (+2); usual care: 777=777.",  
> **"problem"**: "eTable 1 overcounts the mutually exclusive follow-up-pattern categories by 3, localized as +1 in painTRAINER and +2 in Health Coach. The error is within the one- and/or two-observed-follow-up cells; the supplied files do not identify the exact corrected allocation between those two rows.",  
> **"final_output_value"**: "Tier A — highest-priority mentor result",  
> **"mentor_note"**: "The follow-up-pattern categories overcount the analysis population by three and are localized to two treatment arms."  
> }

# Verified error records

## Presentation inconsistency (35)

### error_001 — jama.2025.11178 / C10

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 4 PDF, PDF p. 15 lead-in and PDF p. 17, eTable 11 title/header; analytic footnote continues on PDF p. 18.",  
> **"problem"**: "The supplement gives incompatible descriptions of the raw treatment-group summaries.",  
> **"expected"**: "Use the label, unit, summary statistic, or analysis description that matches the quantity actually displayed."  
> }

### error_002 — jama.2025.11178 / C06

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 4 PDF, PDF p. 9, eTable 4.",  
> **"problem"**: "The same complete coefficient row is printed twice.",  
> **"expected"**: "Remove the duplicate, or replace it with the intended row/panel from the authoritative source output."  
> }

### error_003 — jama.2025.11178 / C07

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 4 PDF, PDF p. 8, eTable 3, and PDF p. 9, eTable 4.",  
> **"problem"**: "The printed labels do not uniquely assign the education and site coefficients to design-matrix levels.",  
> **"expected"**: "Correct the affected display so its value and description agree with the authoritative analysis output."  
> }

### error_004 — jama.2025.11178 / C08

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 4 PDF, PDF p. 14, eTable 8, first subset header.",  
> **"problem"**: "As printed, the header is incomplete or misleading about the meaning of the 149/153/152 values; they cannot be read as observed 3-month counts.",  
> **"expected"**: "Correct the affected display so its value and description agree with the authoritative analysis output."  
> }

### error_005 — jama.2025.11178 / C09

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 4 PDF, PDF p. 15, section heading/lead-in, eTable 9 title, and footnote b.",  
> **"problem"**: "The table title directly conflicts with both its surrounding description and its own footnote.",  
> **"expected"**: "Use the label, unit, summary statistic, or analysis description that matches the quantity actually displayed."  
> }

### error_006 — jama.2025.15185 / C10

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 3 PDF, PDF p. 26, eFigure 6, page heading and embedded caption beneath the spline plot. Comparators: supplement 3 PDF, PDF p. 23, eFigure 4, heading and forest plot; supplement 3 PDF, PDF p. 24…",  
> **"problem"**: "The supplement identifies the spline plot as eFigure 6, but its embedded caption calls it Figure 4, while eFigure 4 is a different forest plot.",  
> **"expected"**: "The conflicting locations should report the same value, direction, definition, or denominator; use authoritative source output when the correct version is not recoverable."  
> }

### error_007 — jama.2025.15185 / C07

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 3 PDF, PDF p. 27, eFigure 7, top color key and PH3 legend below the forest plot.",  
> **"problem"**: "eFigure 7's color key calls the PH3 series “moderate-severe impairment” and “very severe impairment,” while the PH3 legend defines the subgroups as severe (`≤35` points) and mild to moderate (`>35` points).",  
> **"expected"**: "Use the label, unit, summary statistic, or analysis description that matches the quantity actually displayed."  
> }

### error_008 — jama.2025.15185 / C08

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 3 PDF, PDF p. 15, eTable 4, effect-column header and row “mRS, 3 months, median \[IQR\].” Comparator: main article PDF, PDF p. 6 (journal p. 1528), Secondary Outcomes, ordinal logistic regression sentence.",  
> **"problem"**: "eTable 4 places the modified Rankin Scale estimate under a column headed as a mean difference on FMA, while the main article identifies the same value as an adjusted odds ratio.",  
> **"expected"**: "Use the label, unit, summary statistic, or analysis description that matches the quantity actually displayed."  
> }

### error_009 — jama.2025.16450 / C-01

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 4 PDF, PDF p. 2, eTable 1, four population headers, the block “GDB status (up to 120 days postnatal age), n (%),” and footnotes a–d.",  
> **"problem"**: "The displayed GDB-status percentages use undisclosed smaller denominators rather than the population sizes shown at the tops of the columns. The table therefore omits the applicable nonmissing denominators or a visible accounting for missing/unknown GDB status.",  
> **"expected"**: "Add the missing value, definition, or note; otherwise revise the title/marker so it does not promise information that is absent."  
> }

### error_010 — jama.2025.16450 / C-02

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 4 PDF, PDF p. 5, eTable 3, Budesonide + Surfactant header and the rows “Experienced Any AEs,” “Any of interest,” “Hyperglycemia,” and “Any fatal”; continued eTable 3 notes on PDF p. 6…",  
> **"problem"**: "Multiple Budesonide + Surfactant percentages in eTable 3 reproduce a denominator of 321 although the column is headed `n=322`, and the table gives no alternate denominator for those cells.",  
> **"expected"**: "Recalculate from the stated numerator and denominator, then replace the nonreproducible value while preserving the verified count/total."  
> }

### error_011 — jama.2025.16450 / C-03

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "main article PDF, PDF p. 6 / journal p. 1457, Table 1 continuation, “FIO2 at baseline” and “High FIO2 (≥0.5) at baseline,” plus footnote b; and PDF p. 9 / journal p. 1460, Figure 2, subgroup “Baseline FIO2…",  
> **"problem"**: "Table 1 and Figure 2 present Surfactant Alone baseline-FIO2 totals of 230 and 231, respectively, for the same pretreatment variable and threshold partition. No visible note explains the one-participant difference.",  
> **"expected"**: "The conflicting locations should report the same value, direction, definition, or denominator; use authoritative source output when the correct version is not recoverable."  
> }

### error_012 — jama.2025.16450 / C-04

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 4 PDF, PDF p. 7, eTable 4 estimate header and RR-labelled binary rows; PDF p. 8, abbreviation line and analysis note. Corroborating internal convention: main article PDF, PDF p. 8 / journal p. 1459…",  
> **"problem"**: "The eTable 4 abbreviation line incorrectly expands `RR` as “risk difference”; within the same table and the main article, `RR` is defined and used as “relative risk,” while `RD` denotes “risk difference.”",  
> **"expected"**: "Expand RR as relative risk; reserve RD for risk difference."  
> }

### error_013 — jama.2025.19563 / C-03

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "main article PDF, PDF p. 6, journal p. 2084, baseline Table footnote a.",  
> **"location_2"**: "supplement 2 PDF, PDF pp. 39-47, eTables 3-7 titles.",  
> **"problem"**: "All three main-table cross-reference numbers fail to match their stated descriptors. The described destinations appear to be eTables 3, 5, and 6.",  
> **"expected"**: "The citation should point to the supplement table or figure that actually contains the described result."  
> }

### error_014 — jama.2025.19563 / C-05

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "main article PDF, PDF p. 8, journal p. 2086, Figure 3 footnote a.",  
> **"location_2"**: "main article PDF, PDF p. 6, journal p. 2084, baseline Table, “BMI, median (IQR)” row.",  
> **"problem"**: "Figure 3 footnote a mislabels the displayed baseline BMI values as weight.",  
> **"expected"**: "Label the values as BMI (kg/m²), not weight."  
> }

### error_015 — jama.2025.20765 / C10

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 2 PDF, PDF p. 9, eTable 6; supplement 2 PDF, PDF p. 10 confirms that eTable 7 begins on the next page.",  
> **"problem"**: "The complete body of eTable 6 does not contain the unsuccessful tuberculosis-treatment outcome named in its title.",  
> **"expected"**: "Add the missing value, definition, or note; otherwise revise the title/marker so it does not promise information that is absent."  
> }

### error_016 — jama.2025.20765 / C06

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 2 PDF, PDF p. 15 and supplement 2 PDF, PDF p. 16, eTable 10, header, all symptom blocks, and sole footnote. Comparator populations: main article PDF, PDF p. 3, journal p. 338, Statistical Analysis…",  
> **"problem"**: "eTable 10 does not identify the adverse-event analysis population or missingness rules needed to interpret its represented denominators.",  
> **"expected"**: "Add the missing value, definition, or note; otherwise revise the title/marker so it does not promise information that is absent."  
> }

### error_017 — jama.2025.24175 / 1

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "Narrative: main article PDF, PDF p. 7, journal p. 781, Results—“Secondary End Points,” fourth endpoint: “(39.7%; 51 of 131)” for precision immunotherapy; placebo: “(23.4%; 34 of 145; P = .004).”",  
> **"location_2"**: "Table comparator: main article PDF, PDF p. 6, journal p. 780, Table 2, “Main secondary outcomes,” row “≥1.4-Point decrease of mean SOFA score d 2 to 15,” Precision immunotherapy column: 52/131 (39.7)…",  
> **"problem"**: "The day-15 SOFA narrative prints 51/131 with 39.7%, whereas the main table and subgroup counts support 52/131 (39.7%); this matters because the narrative numerator and its displayed percentage do not reconcile.",  
> **"expected"**: "The narrative should report 52/131 (39.7%) so its numerator agrees with the table, subgroup totals, and percentage."  
> }

### error_018 — jama.2025.24175 / 5

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "Direct source evidence. main article PDF, PDF p. 6, journal p. 780, Table 2, “Main secondary outcomes,” row “28-d Mortality”: Precision immunotherapy 57/131 (43.5); Placebo 72/145 (49.7); Difference 6.1 (−5.6 to 17.6)…",  
> **"problem"**: "Table 2 lists precision immunotherapy before placebo but prints a positive 6.1% 28-day mortality difference even though precision minus placebo is −6.1 percentage points; this matters because the difference column’s sign is opposite the displayed group ordering.",  
> **"expected"**: "Under the displayed precision-immunotherapy-minus-placebo ordering, the difference should be −6.1 percentage points."  
> }

### error_019 — jama.2025.24175 / 6

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "main article PDF, PDF p. 1, journal p. 775, Abstract—Results: “A total of 1069 serious treatment-emergent adverse events (88.8%) were reported.”",  
> **"location_2"**: "main article PDF, PDF p. 8, journal p. 782, Results—“Adverse Events”: “A total of 1069 serious treatment-emergent adverse events were reported in 245 patients (88.8%).”",  
> **"problem"**: "The abstract grammatically attaches 88.8% to 1069 serious adverse events, whereas the body and eTable 13 attach that percentage to 245 of 276 patients; this matters because event count and patient incidence are different quantities.",  
> **"expected"**: "State that 1069 events occurred in 245 of 276 patients (88.8%); attach 88.8% to patients, not to the event count."  
> }

### error_020 — jama.2025.250116 / C04

> {  
> **"severity"**: "Major",  
> **"location_1"**: "supplement 2 PDF, PDF p. 51, eFigure 7, panels A-B; and supplement 2 PDF, PDF p. 52, eFigure 8, panels A-B.",  
> **"problem"**: "eFigure 8 panel B duplicates the entire six-row panel B from eFigure 7 despite eFigure 8's different 28-day-mortality outcome and different panel-A event cells.",  
> **"expected"**: "Remove the duplicate, or replace it with the intended row/panel from the authoritative source output."  
> }

### error_021 — jama.2025.250116 / C06

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 2 PDF, PDF/printed p. 30, eTable 14, “Any AE; Classification by Maximum Severity, n (%)” section, Severe row, Standard care + rhIFNγ (N=106) column.",  
> **"problem"**: "The severe/rhIFNγ cell is missing an opening parenthesis; its displayed count and percentage reconcile arithmetically.",  
> **"expected"**: "Correct the affected display so its value and description agree with the authoritative analysis output."  
> }

### error_022 — jama.2025.250116 / C07

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 2 PDF, PDF/printed p. 30, eTable 14, “Any AE; Classification by Relationship to Study Drug, n (%)” section, Probably related row, Standard care + Anakinra (N=25) column.",  
> **"problem"**: "The probably-related MALS/anakinra cell contains a duplicated zero before the conventional `0 (0.0)` count-percentage expression.",  
> **"expected"**: "Remove the duplicate, or replace it with the intended row/panel from the authoritative source output."  
> }

### error_023 — jama.2025.4390 / C01

> {  
> **"severity"**: "Major",  
> **"location_1"**: "main article PDF, PDF p. 9, journal p. 2069, Figure 3, bedtime and morning columns headed Rate per 100 patient-years; comparison with main article PDF, the same file, PDF p. 8, journal p. 2068, Table 2…",  
> **"problem"**: "Figure 3's two columns labeled `Rate per 100 patient-years` do not display the rates reported for the same all-patient outcome in Table 2. The mismatch spans the principal subgroup figure and can materially mislead rate interpretation.",  
> **"expected"**: "The conflicting locations should report the same value, direction, definition, or denominator; use authoritative source output when the correct version is not recoverable."  
> }

### error_024 — jama.2025.4390 / C02

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 3 PDF, PDF p. 37, eTable 5, Ethnicity – no. (%), White/Caucasian and Other rows; comparison with supplement 3 PDF, the same file, PDF p. 29, eTable 3, ethnicity rows.",  
> **"problem"**: "eTable 5 displays the White/Caucasian values a second time under the distinct label `Other`, creating an internally non-reconciling ethnicity block.",  
> **"expected"**: "Remove the duplicate, or replace it with the intended row/panel from the authoritative source output."  
> }

### error_025 — jama.2025.4390 / C06

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 3 PDF, PDF p. 26, eFigure 4, bedtime/PM Diuretic bar; comparison with supplement 3 PDF, the same file, PDF p. 42, eTable 6, bedtime Diuretic rows…",  
> **"problem"**: "eFigure 4 and eTable 6 disagree by one bedtime diuretic medication between `as allocated` and `off allocation` while preserving the same total.",  
> **"expected"**: "The conflicting locations should report the same value, direction, definition, or denominator; use authoritative source output when the correct version is not recoverable."  
> }

### error_026 — jama.2025.7583 / C02

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "main article PDF, PDF p. 4, journal p. 130, Figure 1 footnote a.",  
> **"location_2"**: "supplement 4 PDF, PDF p. 8, eFigure 1 title and Excluded (n=317) box.",  
> **"problem"**: "The main Figure 1 cross-reference and supplementary eFigure 1 title apply an inclusion label to a displayed exclusion/non-inclusion list.",  
> **"expected"**: "Correct the affected display so its value and description agree with the authoritative analysis output."  
> }

### error_027 — jama.2025.7583 / C04

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 4 PDF, PDF p. 14, eTable 4, MAGIC-MT row, Primary outcome column.",  
> **"problem"**: "The MAGIC-MT primary-outcome summary omits the usual-care event numerator while presenting the corresponding 9.9% and while adjacent trial rows report counts for both arms. The comparative sentence is incomplete and cannot be count-verified from the supplied table.",  
> **"expected"**: "Add the missing value, definition, or note; otherwise revise the title/marker so it does not promise information that is absent."  
> }

### error_028 — jama.2025.7710 / C01

> {  
> **"severity"**: "Major",  
> **"location_1"**: "main article PDF, PDF p. 1/JAMA p. 149, Abstract Results; main article PDF, PDF p. 4/JAMA p. 152, Results and Figure 1; main article PDF, PDF p. 6/JAMA p. 154, “Primary and Secondary Outcomes”; main article PDF, PDF p…",  
> **"problem"**: "Identical primary neonatal-composite records are labeled infants, women, and patients. Since the article separately enumerates randomized women and infants and accounts for multiple births, the terminology could obscure whether the primary analysis concerns randomized women or infants.",  
> **"expected"**: "Use the label, unit, summary statistic, or analysis description that matches the quantity actually displayed."  
> }

### error_029 — jama.2025.7710 / C02

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "main article PDF, PDF p. 4/JAMA p. 152, Results, “Participants and Adherence,” ethnicity paragraph; and main article PDF, PDF p. 5/JAMA p. 153, Table 1, placebo Ethnicity heading and rows.",  
> **"problem"**: "Adjacent reporting uses nonmissing observations in Table 1 and the full randomized placebo cohort in the prose without explaining the switch, producing different percentages for identical counts.",  
> **"expected"**: "Recalculate from the stated numerator and denominator, then replace the nonreproducible value while preserving the verified count/total."  
> }

### error_030 — jama.2025.9110 / C03

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "main article PDF, PDF p. 3, journal p. 321, Figure 1; comparison statements in main article PDF, PDF p. 2, journal p. 320, Design/Trial Procedures and main article PDF, PDF p. 8, journal p. 326, Limitations.",  
> **"problem"**: "The four downstream patient boxes use patient-level randomization language inconsistent with the article’s explicit ICU/cluster randomization unit.",  
> **"expected"**: "Use the label, unit, summary statistic, or analysis description that matches the quantity actually displayed."  
> }

### error_031 — jama.2025.9110 / C07

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "main article PDF, PDF p. 7, journal p. 325, Table 2 footnote f; comparison in main article PDF, PDF p. 4, journal p. 322, Primary Outcome and supplement 3 PDF, PDF p. 27, supplemental p. 27, eFigure 6.",  
> **"problem"**: "Table 2 footnote f gives the wrong supplement number for eFigure 6; the figure is located in Supplement 3.",  
> **"expected"**: "The citation should point to the supplement table or figure that actually contains the described result."  
> }

### error_032 — jama.2025.9663 / C2

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 2 PDF — PDF p. 21, eTable 5, patient-median and “when receiving O2” rows; supplement 2 PDF — PDF p. 27, eTable 10, UK-ROX “Achieved oxygenation”; and main article PDF — PDF p. 6, journal p. 403…",  
> **"problem"**: "Under its generic “Achieved oxygenation” presentation, eTable 10 uses the oxygen-only source row for SpO2 and the patient-median source rows for PaO2 and FiO2 without identifying that metric-specific definition change.",  
> **"expected"**: "Correct the affected display so its value and description agree with the authoritative analysis output."  
> }

### error_033 — jama.2025.9663 / C4

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 2 PDF — PDF p. 27, eTable 10, “Year published”, HOT-ICU column.",  
> **"problem"**: "The displayed HOT-ICU publication year is incomplete relative to the label and the format used throughout the row.",  
> **"expected"**: "Correct the affected display so its value and description agree with the authoritative analysis output."  
> }

### error_034 — jama.2025.9663 / C5

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 2 PDF — PDF p. 22, eTable 6, rows “Patient median FiO2, %” and “Patient median FiO2 when receiving O2, %”; comparison with supplement 2 PDF — PDF p. 21, eTable 5 and supplement 2 PDF — PDF p. 27, eTable 10.",  
> **"problem"**: "eTable 6 labels fractional-scale FiO2 values as percentages, contrary to the scale and terminology used for the same measure elsewhere in the package.",  
> **"expected"**: "Either label the displayed values as fractions or multiply them by 100 before labeling them as percentages."  
> }

### error_035 — jama.2025.9663 / C6

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 2 PDF — PDF p. 27, eTable 10, “Recruitment dates”, PILOT column and complete footnote area.",  
> **"problem"**: "The PILOT recruitment-date asterisk has no corresponding note or legend in eTable 10.",  
> **"expected"**: "Add the missing value, definition, or note; otherwise revise the title/marker so it does not promise information that is absent."  
> }

## Statistical reporting inconsistency (15)

### error_036 — jama.2025.11178 / C04

> {  
> **"severity"**: "Major",  
> **"location_1"**: "main article PDF, Table 3, PDF pp. 10-11 / JAMA pp. 601-602; standardization definition in footnote d on PDF p. 11.",  
> **"problem"**: "Table 3 contains multiple directly demonstrable invalid SMD displays: eight containment failures, 18 reversed endpoint displays, and four sign conflicts under the table's stated definition.",  
> **"expected"**: "The reported value and label should match the stated estimand, analysis population, effect measure, and model output."  
> }

### error_037 — jama.2025.11178 / C05

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "main article PDF, Results—Secondary Outcomes, PDF p. 7 / JAMA p. 598, and Table 3, PDF p. 10 / JAMA p. 601.",  
> **"problem"**: "The main article gives discordant published SMD point estimates for the same two effects.",  
> **"expected"**: "Regenerate a matched point estimate and confidence interval; the point estimate must lie within its own interval and the endpoints must be ordered correctly."  
> }

### error_038 — jama.2025.15185 / C05

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 3 PDF, PDF p. 12, eTable 2 population definitions, Full analysis set definition; supplement 3 PDF, PDF p. 13, eTable 2 results, Estimands 1, 3, and 4, Population, Intercurrent Events…",  
> **"problem"**: "eTable 2 labels Estimands 3 and 4 “Full analysis set,” although that set is defined as excluding deaths and both estimands report `N=610`, incorporating the 28 deaths.",  
> **"expected"**: "Use a population label consistent with whether deaths are included; do not call an N that includes deaths the defined Full analysis set."  
> }

### error_039 — jama.2025.15185 / C06

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 3 PDF, PDF p. 14, eTable 3, Estimand 11, Intercurrent Events and Number of participants columns; supplement 3 PDF, PDF p. 13, eTable 2, Estimands 1, 6, and 7, Number of participants column…",  
> **"problem"**: "eTable 3 says Estimand 11 excludes participants meeting both low-rehabilitation and low-medication conditions, but excluding only that intersection cannot yield the reported `N=395`.",  
> **"expected"**: "The reported value and label should match the stated estimand, analysis population, effect measure, and model output."  
> }

### error_040 — jama.2025.15440 / C-01

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "main article PDF, PDF p. 1, journal p. 1349, structured abstract, Results, final sentence.",  
> **"location_2"**: "main article PDF, Same file, PDF p. 5, journal p. 1353, Results, final paragraph.",  
> **"problem"**: "The structured abstract reports **0.76-1.53**, whereas the Results text and Figure 4B report **0.77-1.51** for the same printed any-stroke comparison. This is the critic-retained Minor statistical reporting inconsistency.",  
> **"expected"**: "Regenerate a matched point estimate and confidence interval; the point estimate must lie within its own interval and the endpoints must be ordered correctly."  
> }

### error_041 — jama.2025.19563 / C-04

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 2 PDF, PDF p. 53, eTable 11 and age row; and supplement 2 PDF, the same PDF, p. 54, footnotes 1-2.",  
> **"problem"**: "eTable 11 assigns age two unexplained P values and includes an “all other” significance statement that conflicts with its reported significant sex result.",  
> **"expected"**: "The reported value and label should match the stated estimand, analysis population, effect measure, and model output."  
> }

### error_042 — jama.2025.20765 / C04

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "main article PDF, PDF p. 5, journal p. 340, Adverse Events; supplement 2 PDF, PDF p. 15, eTable 10, Nausea and Diarrhoea blocks.",  
> **"problem"**: "The eTable 10 counts reproduce the main-text mHealth nausea and control diarrhoea percentages, but yield 21.3% rather than 22.3% for control nausea and 7.3% rather than 7.5% for mHealth diarrhoea.",  
> **"expected"**: "Recalculate from the stated numerator and denominator, then replace the nonreproducible value while preserving the verified count/total."  
> }

### error_043 — jama.2025.20765 / C08

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "main article PDF, PDF p. 3, journal p. 338, Statistical Analysis; main article PDF, PDF p. 4, journal p. 339, Figure 1; main article PDF, PDF p. 6, journal p. 341, Table 2. supplement 2 PDF, PDF p…",  
> **"problem"**: "eTable 9 labels a population from which precisely the reported deaths were removed as “intention to treat,” despite the main article presenting death exclusion as a distinct post hoc analysis.",  
> **"expected"**: "Label the result as the post hoc death-excluded analysis, not intention-to-treat."  
> }

### error_044 — jama.2025.24175 / 2

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "Direct source evidence. supplement 2 PDF, PDF p. 22 (printed page 22), eTable 10, row “Sepsis-induced immunoparalysis” under “≥1.4-point decrease of mean SOFA of days 2 to 15”: Precision immunotherapy 40/106 (37.7)…",  
> **"problem"**: "In the day-15 sepsis-induced-immunoparalysis row, eTable 10 prints an unadjusted OR of 1.194, but the four printed counts yield a cross-product OR of about 1.94; this matters because the point estimate cannot be reproduced by ordinary rounding.",  
> **"expected"**: "The reported value and label should match the stated estimand, analysis population, effect measure, and model output."  
> }

### error_045 — jama.2025.24175 / 4

> {  
> **"severity"**: "Major",  
> **"location_1"**: "supplement 2 PDF, PDF p. 51 (printed page 51), eFigure 7B, caption “Attainment of the Primary Endpoint According to Baseline Severity,” panel B “Interaction tests … for the primary endpoint”: 0.47 (0.30-1.62), P=.70; 1…",  
> **"location_2"**: "supplement 2 PDF, PDF p. 52 (printed page 52), eFigure 8, caption “28-Day Mortality According to Baseline Severity,” panel B: the same six displayed triplets at the same labels: 0.47 (0.30-1.62), .70; 1.85 (0.66-5.19)…",  
> **"problem"**: "eFigure 8B, labelled as 28-day-mortality interactions, repeats all six OR/CI/P triplets printed for eFigure 7B, which is labelled as primary-endpoint interactions; this matters because the displayed mortality subgroup/interaction statistics are not reliable as shown.",  
> **"expected"**: "Remove the duplicate, or replace it with the intended row/panel from the authoritative source output."  
> }

### error_046 — jama.2025.250116 / C01

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "main article PDF, PDF p. 6, journal p. 780, Table 2, “Main secondary outcomes,” row “≥1.4-Point decrease of mean SOFA score d 2 to 15,” Precision immunotherapy column.",  
> **"location_2"**: "main article PDF, PDF p. 7, journal p. 781, Results, “Secondary End Points,” fourth endpoint.",  
> **"problem"**: "The main narrative's `51 of 131 (39.7%)` conflicts with Table 2's `52/131 (39.7%)`; eTable 10's mutually classified strata sum to 52/131.",  
> **"expected"**: "The reported value and label should match the stated estimand, analysis population, effect measure, and model output."  
> }

### error_047 — jama.2025.250116 / C03

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 2 PDF, PDF/printed p. 53, eFigure 9, “90-Day Mortality According to Baseline Severity,” panel A APACHE II ≥25 row and panel B APACHE II ≥25 × Precision Immunotherapy row.",  
> **"problem"**: "The published OR of 0.11 lies outside its own displayed 95% CI, while the displayed APACHE II ≥25 cells yield a diagnostic OR near 1.11 and an interval near 0.36-3.42.",  
> **"expected"**: "Regenerate a matched point estimate and confidence interval; the point estimate must lie within its own interval and the endpoints must be ordered correctly."  
> }

### error_048 — jama.2025.250116 / C05

> {  
> **"severity"**: "Major",  
> **"location_1"**: "supplement 2 PDF, PDF/printed p. 51, eFigure 7, panel A event cells, panel B labels/estimates, and caption B.",  
> **"location_2"**: "supplement 2 PDF, PDF/printed p. 53, eFigure 9, panel A event cells, panel B labels/estimates, and caption B.",  
> **"problem"**: "In eFigures 7 and 9, multiple entries labeled as severity-by-treatment interaction results reproduce treatment ORs within the high-severity strata; the main text interprets selected entries as interaction tests. The finding remains independently supported after excluding eFigure 8.",  
> **"expected"**: "The reported value and label should match the stated estimand, analysis population, effect measure, and model output."  
> }

### error_049 — jama.2025.4390 / C03

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "main article PDF, PDF p. 9, journal p. 2069, Figure 3 all-patients row and footnote; comparison with main article PDF, the same file, PDF p. 6, journal p. 2066, Results, Primary Outcome, and main article PDF, PDF p. 8…",  
> **"problem"**: "Figure 3's universal unadjusted-CI footnote is false for the displayed all-patients row.",  
> **"expected"**: "Use the label, unit, summary statistic, or analysis description that matches the quantity actually displayed."  
> }

### error_050 — jama.2025.9110 / C04

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "main article PDF, PDF p. 7, journal p. 325, Table 2, Primary outcome secondary analyses, Bayesian quantile mixed-model row; comparison in supplement 3 PDF, PDF p. 27, supplemental p. 27, eFigure 6.",  
> **"problem"**: "`mean (SD)` is inconsistent with the displayed group summaries and the median-based Bayesian analysis; the completed record supports `median (IQR)` as the intended descriptive label.",  
> **"expected"**: "Use median (IQR) for the three-number summaries and median-based analysis; do not label them mean (SD)."  
> }

## Arithmetic inconsistency (10)

### error_051 — jama.2025.11178 / C03

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "results workbook, sheet eTable 3, E3 and A82:E83; footnote a at A110.",  
> **"problem"**: "The error is localized to the percentage printed in E82. The directly recoverable display is `711 (45.4)`. The count 711 is internally supported; the supplied workbook does not establish where `73.2` originated.",  
> **"expected"**: "Use the recoverable value stated in the finding: `711 (45.4)`."  
> }

### error_052 — jama.2025.15185 / C01

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 3 PDF, PDF p. 17, eTable 6, columns Overall, Placebo, and Levodopa, rows n, AE intensity, AE outcome, and Drug relation. Comparators: main article PDF, PDF p. 6 (journal p. 1528), Table 2…",  
> **"problem"**: "The results supplement reports 145 prespecified adverse events overall, although both arm totals and every displayed classification block sum to 146.",  
> **"expected"**: "Recalculate from the stated numerator and denominator, then replace the nonreproducible value while preserving the verified count/total."  
> }

### error_053 — jama.2025.19563 / C-01

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 2 PDF, PDF p. 55, eTable 12, second component-pattern row, Human-led DPP column.",  
> **"problem"**: "The second-row Human-led DPP entry `10 (19%)` does not reconcile with its stated denominator; it rounds to 17% under the table’s denominator rule.",  
> **"expected"**: "Recalculate from the stated numerator and denominator, then replace the nonreproducible value while preserving the verified count/total."  
> }

### error_054 — jama.2025.20765 / C02

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 2 PDF, PDF p. 9, eTable 6, Control/site 2008 row; supplement 2 PDF, PDF p. 8, eTable 5, Control/site 2008 row. Corroborating cluster size: main article PDF, PDF p. 5, journal p. 340, Table 1.",  
> **"problem"**: "The displayed `5 (7.5)` is arithmetically inconsistent with the 40-person site denominator; the diagnostic percentage is 12.5%.",  
> **"expected"**: "Report 5/40 as 12.5%, not 7.5%."  
> }

### error_055 — jama.2025.20765 / C03

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 2 PDF, PDF p. 6, eTable 4, “Causes of deaths among two study groups.”",  
> **"problem"**: "eTable 4 contains arithmetic inconsistencies, most clearly the two usual-care `1 (7.4%)` cells, for which conventional one-decimal calculation gives 3.7% each.",  
> **"expected"**: "Report each 1/27 cell as 3.7%, not 7.4%."  
> }

### error_056 — jama.2025.250116 / C02

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 2 PDF, PDF/printed p. 22, eTable 10, section “≥1.4-point decrease of mean SOFA of days 2 to 15 from baseline day 1,” SII row, the two treatment columns and OR unadjusted (95% CI) column.",  
> **"problem"**: "The displayed counts yield a diagnostic crude OR of approximately 1.94, whereas the table prints 1.194; the printed CI is approximately compatible with the former.",  
> **"expected"**: "The displayed counts support a crude OR near 1.94; verify the source model and replace the printed 1.194 if it is a transcription error."  
> }

### error_057 — jama.2025.4390 / C05

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 3 PDF, PDF p. 22, eFigure 1, Location of Participating Practices, British Columbia column; comparison with supplement 3 PDF, the same file, PDF p. 27, eTable 1, recruitment footnote.",  
> **"problem"**: "The British Columbia city-level counts sum to 44, not the displayed province total of 43.",  
> **"expected"**: "Recalculate from the stated numerator and denominator, then replace the nonreproducible value while preserving the verified count/total."  
> }

### error_058 — jama.2025.4390 / C07

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "main article PDF, PDF p. 6, journal p. 2066, Table 1 continued, Calcium channel blocker; repeated in supplement 3 PDF, PDF p. 32, eTable 3, same row.",  
> **"problem"**: "Given the printed numerator and denominator, the bedtime percentage should arithmetically round to 28.6%; the displayed 28.2% is not reproducible and is repeated in two tables.",  
> **"expected"**: "Use the recoverable value stated in the finding: 28.6%."  
> }

### error_059 — jama.2025.9110 / C01

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 3 PDF, PDF p. 10, supplemental p. 10, eTable 4, “Period 3 – Augmented Protein” Sex rows; aggregate comparison in main article PDF, PDF p. 5, journal p. 323, Table 1, Sex rows.",  
> **"problem"**: "The displayed Period 3 augmented-protein sex counts are two below the displayed period denominator and also leave one male and one female unreconciled against the aggregate Table 1 totals.",  
> **"expected"**: "Recalculate from the stated numerator and denominator, then replace the nonreproducible value while preserving the verified count/total."  
> }

### error_060 — jama.2025.9110 / C02

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 3 PDF, PDF p. 16, supplemental p. 16, eTable 8, “Total protocol deviations” in the Augmented Protein column.",  
> **"problem"**: "The printed `9.4%` beside 151 participants is not the one-decimal percentage of 151/1681 and numerically equals the one-decimal percentage of 158/1681.",  
> **"expected"**: "Report 151/1681 as 9.0%; 9.4% corresponds to 158/1681 events, not 151 participants."  
> }

## Cross-document inconsistency (10)

### error_061 — jama.2025.15185 / C02

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 3 PDF, PDF p. 10, eTable 1, rows “Stroke ischemic – No. (%)” and “Stroke hemorrhagic – No. (%)”, columns Overall, Placebo, and Levodopa. Comparator: main article PDF, PDF p. 4 (journal p. 1526), Table 1…",  
> **"problem"**: "The supplement reports levodopa stroke-type counts of 263 ischemic and 44 hemorrhagic, whereas the main article reports 260 and 47; only the main-article arm values reproduce the supplement's Overall counts.",  
> **"expected"**: "Recalculate from the stated numerator and denominator, then replace the nonreproducible value while preserving the verified count/total."  
> }

### error_062 — jama.2025.15185 / C03

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "main article PDF, PDF p. 4 (journal p. 1526), Table 1 continuation, row “Time from stroke onset to randomization, median (IQR), d.” Comparator: supplement 3 PDF, PDF p. 11, eTable 1 continuation…",  
> **"problem"**: "The main article reports a median of 3 days from stroke onset to randomization in each arm, while the identically described supplement row reports 7 days for levodopa and 8 days for placebo.",  
> **"expected"**: "Use one authoritative value or definition consistently in the main article, supplement, table, figure, and narrative."  
> }

### error_063 — jama.2025.15185 / C04

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "main article PDF, PDF p. 6 (journal p. 1528), Secondary Outcomes, patient-reported assessment of relevance of motor improvement sentence. Comparator: supplement 3 PDF, PDF p. 15, eTable 4, row “PRAI…",  
> **"problem"**: "The main article reports 52 of 270 placebo participants with no improvement or no relevant improvement, whereas eTable 4 reports 51 of 270.",  
> **"expected"**: "Use one authoritative value or definition consistently in the main article, supplement, table, figure, and narrative."  
> }

### error_064 — jama.2025.19563 / C-06

> {  
> **"severity"**: "Major",  
> **"location_1"**: "main article PDF, PDF p. 8, journal p. 2086, Figure 3B, “Change in HbA1c at 12 mo.”",  
> **"location_2"**: "main article PDF, PDF p. 3, journal p. 2081, Outcomes section.",  
> **"problem"**: "The figure demonstrably represents a larger HbA1c analysis set than eTable 14 reports for the co-cited HbA1c-change outcome, without a caption explanation reconciling the inclusion rule.",  
> **"expected"**: "Use one authoritative value or definition consistently in the main article, supplement, table, figure, and narrative."  
> }

### error_065 — jama.2025.19563 / C-07

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "supplement 2 PDF, PDF p. 34, eFigure 3 row label and footnote 3.",  
> **"location_2"**: "main article PDF, PDF p. 3, journal p. 2081, Outcomes section.",  
> **"problem"**: "The main article and supplement label the same HbA1c component differently: absolute percentage points in the main article and percent notation in the supplement.",  
> **"expected"**: "Use the main article's absolute percentage-point definition in the supplement; do not express it as a relative percent change."  
> }

### error_066 — jama.2025.19843 / V-02

> {  
> **"severity"**: "Major (critic-retained; verifier had recorded Moderate)",  
> **"location_1"**: "Main-article composite definition: main article PDF — PDF p. 3, journal p. 62, Methods, “Outcomes,” right column, paragraph beginning “Predefined secondary outcomes included.”",  
> **"location_2"**: "Supplementary composite count: supplement 3 PDF — PDF p. 5, eTable 3, “Secondary End Points,” row “Major adverse cardiovascular events during first 30 days,” Placebo column, denominator in the column header.",  
> **"problem"**: "The main article defines dialysis as a day-30 major adverse cardiovascular event component, but the results supplement reports fewer placebo participants with day-30 MACE than with dialysis and repeats the MACE count in a figure whose definition omits dialysis; the definition, count, and display therefore cannot be jointly verified.",  
> **"expected"**: "Use one authoritative value or definition consistently in the main article, supplement, table, figure, and narrative."  
> }

### error_067 — jama.2025.20765 / C01

> {  
> **"severity"**: "Major",  
> **"location_1"**: "supplement 2 PDF, PDF p. 4, eTable 2, both study-arm blocks; supplement 2 PDF, PDF p. 8, eTable 5, site 2012 row. main article PDF, PDF p. 5, journal p. 340, Table 1, cluster totals, participant totals…",  
> **"problem"**: "eTable 2 omits one mHealth cluster relative to Table 1 and eTable 5, displaying 680 participants and 168 prior-attempt Yes responses rather than 720 and 178.",  
> **"expected"**: "Add the missing value, definition, or note; otherwise revise the title/marker so it does not promise information that is absent."  
> }

### error_068 — jama.2025.20765 / C05

> {  
> **"severity"**: "Major",  
> **"location_1"**: "main article PDF, PDF p. 5, journal p. 340, Adverse Events; supplement 2 PDF, PDF p. 15, eTable 10, Dry mouth, Irritability, and Anxiety blocks.",  
> **"problem"**: "The main-text direction statement is inconsistent with any-grade irritability and anxiety occurrence, both of which are lower in mHealth; dry mouth alone has the stated direction.",  
> **"expected"**: "Use one authoritative value or definition consistently in the main article, supplement, table, figure, and narrative."  
> }

### error_069 — jama.2025.9110 / C05

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "main article PDF, PDF p. 7, journal p. 325, Table 2, “Duration of invasive ventilation” row; supplement 3 PDF, PDF p. 18, supplemental p. 18, eTable 10 and footer; and supplement 3 PDF, PDF p. 4, supplemental p. 4…",  
> **"problem"**: "The main article’s `mean (SD)` label conflicts with the displayed three-number group summaries and the supplement’s median (IQR) convention for the same outcome.",  
> **"expected"**: "Use median (IQR) for the three-number summaries and median-based analysis; do not label them mean (SD)."  
> }

### error_070 — jama.2025.9663 / C1

> {  
> **"severity"**: "Minor",  
> **"location_1"**: "main article PDF — PDF p. 6, journal p. 403, “Primary and Secondary Outcomes”; supplement 2 PDF — PDF p. 11, eFigure 4; and supplement 2 PDF — PDF p. 12, eFigure 5.",  
> **"problem"**: "The main-text time-to-death statement points readers to eFigure 4, while the matching mortality result is in eFigure 5.",  
> **"expected"**: "The citation should point to the supplement table or figure that actually contains the described result."  
> }

## Participant-flow inconsistency (1)

### error_071 — jama.2025.11178 / C01

> {  
> **"severity"**: "Major",  
> **"location_1"**: "supplement 4 PDF, PDF p. 7, eTable 1; corroboration in main article PDF, PDF p. 5, Figure 1, and results workbook, sheet eTable 3, B2:E3.",  
> **"problem"**: "eTable 1 overcounts the mutually exclusive follow-up-pattern categories by 3, localized as +1 in painTRAINER and +2 in Health Coach. The error is within the one- and/or two-observed-follow-up cells; the supplied files do not identify the exact corrected allocation between those two rows.",  
> **"expected"**: "Recalculate from the stated numerator and denominator, then replace the nonreproducible value while preserving the verified count/total."  
> }

# Uncertain records

These records identify a plausible problem, but the supplied package does not establish which element is wrong or what corrected value should replace it.

### concern_001 — jama.2025.19563 / C-02

> {  
> **"severity"**: "Not assigned",  
> **"status"**: "uncertain",  
> **"location_1"**: "supplement 2 PDF, PDF p. 59, eTable 16.",  
> **"location_2"**: "supplement 2 PDF, PDF p. 30, multiple-imputation description.",  
> **"problem"**: "The direct subtraction differs from the reported risk difference, but the package does not demonstrate that direct subtraction is the estimand the table intends to report. The locked disposition remains Uncertain.",  
> **"expected"**: "Do not amend the publication yet; first obtain the missing definition, unrounded result, or model/source output identified by the validation report."  
> }

### concern_002 — jama.2025.19843 / V-01

> {  
> **"severity"**: "Not assigned in the authoritative verifier record",  
> **"status"**: "uncertain",  
> **"location_1"**: "main article PDF — PDF p. 6, journal p. 65:",  
> **"problem"**: "Figure 2 displays “at risk” and “with event” values whose simple sums exceed the randomized group totals at days 5, 10, and 15, but the supplied figure does not define the event row or risk-set convention well enough to establish that the two displayed rows are mutually exclusive participant counts.",  
> **"expected"**: "Do not amend the publication yet; first obtain the missing definition, unrounded result, or model/source output identified by the validation report."  
> }

### concern_003 — jama.2025.9663 / C3

> {  
> **"severity"**: "Uncertain",  
> **"status"**: "uncertain",  
> **"location_1"**: "supplement 2 PDF — PDF p. 26, eTable 9, “Any serious adverse event”, under both “Events, No.” columns.",  
> **"problem"**: "The blank overall event-count cells and the diagnostic sums of 64 and 37 are document-grounded; whether totals were intended in those cells is not established.",  
> **"expected"**: "Do not amend the publication yet; first obtain the missing definition, unrounded result, or model/source output identified by the validation report."  
> }

### concern_004 — jama.2025.11178 / C02

> {  
> **"severity"**: "Major if confirmed",  
> **"status"**: "uncertain",  
> **"location_1"**: "supplement 4 PDF, PDF p. 8, eTable 3; imputation-model description on PDF pp. 4-5.",  
> **"problem"**: "The seven printed triples are highly suspicious under ordinary row-level two-sided inference, but the package does not define enough of the P-value procedure to prove the contradiction solely from the published files.",  
> **"expected"**: "Do not amend the publication yet; first obtain the missing definition, unrounded result, or model/source output identified by the validation report."  
> }

### concern_005 — jama.2025.20765 / C07

> {  
> **"severity"**: "Not assigned",  
> **"status"**: "uncertain",  
> **"location_1"**: "main article PDF, PDF p. 3, journal p. 338, Statistical Analysis; main article PDF, PDF p. 4, journal p. 339, Figure 1; main article PDF, PDF p. 6, journal p. 341, Table 2 and abbreviation note.",  
> **"problem"**: "The PP denominators exactly reproduce the described complete-case population, but the package does not resolve whether the PP label is erroneous.",  
> **"expected"**: "Do not amend the publication yet; first obtain the missing definition, unrounded result, or model/source output identified by the validation report."  
> }

### concern_006 — jama.2025.24175 / 3

> {  
> **"severity"**: "Potential severity not separately assigned in surviving record",  
> **"status"**: "uncertain",  
> **"location_1"**: "Direct source evidence. supplement 2 PDF, PDF p. 53 (printed page 53), eFigure 9B, row “APACHE II ≥25 × Precision Immunotherapy,” OR column 0.11, 95% CIs column 0.36-3.42, P-value column .86…",  
> **"problem"**: "eFigure 9B prints an OR of 0.11 with a 95% CI of 0.36-3.42 for the APACHE II ≥25 interaction, placing the stated OR below its stated lower bound; this matters because the matched interaction magnitude cannot be interpreted reliably as printed.",  
> **"expected"**: "Do not amend the publication yet; first obtain the missing definition, unrounded result, or model/source output identified by the validation report."  
> }

### concern_007 — jama.2025.4390 / C04

> {  
> **"severity"**: "Potential Minor",  
> **"status"**: "uncertain",  
> **"location_1"**: "supplement 3 PDF, PDF p. 39, eTable 5, Type of BP-lowering med – no. (%), Diuretic and Combination BP med; allocation denominators are in the eTable 5 header on supplement 3 PDF, PDF p. 37…",  
> **"problem"**: "The table visibly presents identical marginal comparisons with different P values, which warrants source-output review.",  
> **"expected"**: "Do not amend the publication yet; first obtain the missing definition, unrounded result, or model/source output identified by the validation report."  
> }

### concern_008 — jama.2025.9110 / C06

> {  
> **"severity"**: "Uncertain",  
> **"status"**: "uncertain",  
> **"location_1"**: "main article PDF, PDF p. 8, journal p. 326, Discussion; main article PDF, PDF p. 5, journal p. 323, Biochemical Outcomes; and supplement 3 PDF, PDF p. 19, supplemental p. 19, eTable 11, Blood urea, Day 10.",  
> **"problem"**: "The package directly supports a terminology difference between the Discussion’s `mean` wording and the only displayed day-10 summaries, which are medians (IQR).",  
> **"expected"**: "Do not amend the publication yet; first obtain the missing definition, unrounded result, or model/source output identified by the validation report."  
> }

# Source report index

- **jama.2025.4390:** [final_report.html](jama.2025.4390/.ai_paper_validation/final_report.html)
- **jama.2025.7583:** [final_report.html](jama.2025.7583/.ai_paper_validation/final_report.html)
- **jama.2025.7710:** [final_report.html](jama.2025.7710/.ai_paper_validation/final_report.html)
- **jama.2025.9110:** [final_report.html](jama.2025.9110/.ai_paper_validation/final_report.html)
- **jama.2025.9663:** [final_report.html](jama.2025.9663/.ai_paper_validation/final_report.html)
- **jama.2025.11178:** [final_report.html](jama.2025.11178/.ai_paper_validation/final_report.html)
- **jama.2025.15185:** [final_report.html](jama.2025.15185/.ai_paper_validation/final_report.html)
- **jama.2025.15440:** [final_report.html](jama.2025.15440/.ai_paper_validation/final_report.html)
- **jama.2025.16450:** [final_report.html](jama.2025.16450/.ai_paper_validation/final_report.html)
- **jama.2025.19563:** [final_report.html](jama.2025.19563/.ai_paper_validation/final_report.html)
- **jama.2025.19843:** [final_report.html](jama.2025.19843/.ai_paper_validation/final_report.html)
- **jama.2025.20765:** [final_report.html](jama.2025.20765/.ai_paper_validation/final_report.html)
- **jama.2025.24175:** [final_report.html](jama.2025.24175/.ai_paper_validation/final_report.html)
- **jama.2025.250116:** [final_report.html](jama.2025.250116/.ai_paper_validation/final_report.html)
