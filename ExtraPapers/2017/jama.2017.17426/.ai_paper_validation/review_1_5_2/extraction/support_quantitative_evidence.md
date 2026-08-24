# Support quantitative evidence mapping

## Scope and method

Fresh support-source mapping only: `DOC-002 joi170130supp1_prod.pdf`, PDF pp. 1-69, and `DOC-003 joi170130supp2_prod.pdf`, PDF pp. 1-2. Native and layout text assets were read for all pages. Rendered pages were used for the protocol/SAP tables and the eTable; the rendered PNG (with the fresh targeted OCR only as navigation) was used for DOC-002 p. 66. The source PDFs and all older audit derivatives were not modified or used.

## Complete page coverage

| Source/pages | Content and quantitative relevance | Mapping result |
|---|---|---|
| DOC-002 pp. 1-6 | Supplement index; original protocol title, administration, contents, abbreviations | p. 1 identifies original/final protocol and original SAP; pp. 2-6 contain no observed trial results. |
| DOC-002 pp. 7-10 | Original protocol v1: target, allocation, outcomes, assessment schedule | Planned definitions and numeric design values mapped in UN001-UN006 and US001-US002. |
| DOC-002 pp. 11-16 | Original protocol administration, AE definitions, flowchart | p. 16 gives a planned care flow; no observed result. |
| DOC-002 pp. 17-24 | Participant information, consent, blank EQ-5D/VAS instruments | p. 23 uses 0-10 response anchors; p. 24 uses 0-100 VAS anchors and days 1-8; blank instruments, not results. |
| DOC-002 pp. 25-30 | Final protocol v4 front matter | Administrative/version material, no observed results. |
| DOC-002 pp. 31-35 | Final protocol v4 summary/design, eligibility, treatment, randomisation, endpoints, follow-up | Planned definitions and numerical design values mapped in UN007-UN014 and US003-US004. |
| DOC-002 pp. 36-46 | Final protocol sample-size calculation, administration/AE material, flowchart and blank questionnaires | p. 37 states a planned base of 62 per group at 80% power for 0.54 SD (approximately 5 days), with 20% loss adding 24 participants for target 146; p. 44 reiterates planned care flow; pp. 45-46 are blank 0-10 EQ-5D and 0-100 VAS instruments. No observed result. |
| DOC-002 pp. 47-51 | Protocol-change summary | Records design changes: regional minimisation added after 40% target recruited; probability changed from 0.5-0.7 to 0.8; missing-data/sample-size sections added. Mapped in UN015 and US005. |
| DOC-002 pp. 52-53 | Original SAP title/index | SAP v1 dated 2015-01-11; supplement states there were no subsequent SAP changes. No observed results. |
| DOC-002 pp. 54-61 | SAP design, endpoints and scale/measurement definitions | Planned definitions mapped in UN016-UN021 and US006-US010. |
| DOC-002 pp. 62-65 | SAP sample size and analysis rules | Planned pilot values/sample size and inferential methods mapped in UN022-UN024 and US011-US017. |
| DOC-002 p. 66 | SAP participant-flowchart template | Rendered flowchart contains only `X`/`Y` placeholders for screened, excluded, randomized, interventions, completed and analysed participants; no observed values. |
| DOC-002 pp. 67-68 | Suggested baseline and outcome table shells | Explicit `n=...` placeholders, no observed data; mapped as planned shells in UN025. |
| DOC-002 p. 69 | References | No result-relevant values. |
| DOC-003 p. 1 | Supplementary-online-content cover and eTable title | Identifies eTable as "Summary of Multiple Imputation by ITT Analysis." |
| DOC-003 p. 2 | eTable with imputed ITT VAS dyspnoea, VAS QoL and EQ5D estimates | Observed supplementary results, fully transcribed in UN026-UN028; inference/MI definition in US018. |

## Observed support results

Only DOC-003 p. 2 presents observed trial results. It reports estimates from 20 chained-equation multiply imputed data sets for the ITT analysis, with IPC (n=73), talc pleurodesis (n=71), estimated IPC-minus-talc difference, 95% CI, and P value.

## Cross-lane mapping repair: final-protocol sample-size relationship

Fresh cross-source review identified a result-relevant planned relationship on DOC-002 p. 37 that the initial mapper summary omitted. The final protocol prints 62 participants per group for 80% power at a two-sided 5% level to detect 0.54 SD (described as approximately 5 days from an 18-day post-pleurodesis stay), then a 20% loss allowance adding 24 participants for a target of 146. This is mapped with the SAP/main relationship that instead prints 65 per group and a 12% loss allowance for the same target. The repair uses the same fresh DOC-002 assets and preserves complete page coverage.

| Measure/time | IPC estimate (95% CI) | Talc estimate (95% CI) | IPC minus talc (95% CI); P |
|---|---:|---:|---:|
| VAS dyspnoea baseline | 49.8 (37.1, 62.5) | 51.9 (39.0, 64.7) | -2.06 (-10.30, 6.17); .62 |
| VAS dyspnoea day 1 | 65.5 (52.6, 78.4) | 71.7 (58.7, 84.7) | -6.19 (-15.04, 2.66); .17 |
| VAS dyspnoea 30 d | 70.3 (57.4, 83.2) | 71.4 (58.4, 84.4) | -1.11 (-9.64, 7.42); .80 |
| VAS dyspnoea 6 mo | 72.1 (59.0, 85.3) | 71.3 (57.5, 85.1) | 0.84 (-8.95, 10.65); .87 |
| VAS dyspnoea 12 mo | 70.4 (56.6, 84.3) | 59.8 (45.4, 74.4) | 10.52 (-1.36, 22.41); .08 |
| VAS QoL baseline | 52.3 (43.2, 61.3) | 56.7 (47.5, 65.9) | -4.41 (-12.54, 3.72); .29 |
| VAS QoL day 2 | 60.8 (51.7, 69.9) | 59.6 (50.1, 69.1) | 1.20 (-7.13, 9.53); .78 |
| VAS QoL 30 d | 62.0 (52.8, 71.2) | 66.2 (56.6, 75.9) | -4.27 (-12.93, 4.38); .33 |
| VAS QoL 6 mo | 67.5 (57.8, 77.3) | 65.3 (54.9, 75.8) | 2.12 (-7.94, 12.28); .67 |
| VAS QoL 12 mo | 59.1 (48.1, 70.2) | 57.7 (45.6, 69.8) | 1.43 (-11.46, 14.32); .83 |
| EQ5D baseline | 31.2 (26.9, 35.6) | 32.5 (28.1, 36.8) | -1.23 (-4.67, 2.21); .48 |
| EQ5D day 8 | 33.5 (28.9, 38.1) | 35.5 (30.9, 40.0) | -1.97 (-5.84, 1.90); .32 |
| EQ5D 30 d | 35.4 (31.0, 39.9) | 34.2 (29.6, 38.8) | 1.26 (-2.68, 5.20); .53 |
| EQ5D 6 mo | 34.3 (29.6, 38.9) | 32.7 (27.8, 37.7) | 1.53 (-2.94, 5.99); .50 |
| EQ5D 12 mo | 31.5 (26.5, 36.5) | 32.3 (27.0, 37.7) | -0.82 (-6.25, 4.61); .77 |

## Matched main-paper keys (fresh DOC-001 assets)

The main paper reports the complete-case/primary ITT Table 2 rather than the eTable's multiple-imputation sensitivity values: p. 6 has IPC n=73 and talc n=71; VAS and EQ5D table cells are estimated means with 95% CIs and P values. Its footnote says its displayed difference convention is a difference in estimated means, but the signs correspond to talc-minus-IPC (for example, baseline dyspnoea 52.2 minus 50.0 = 2.2, printed 2.27), whereas DOC-003 is explicitly IPC-minus-talc (51.9 minus 49.8 = 2.1, printed -2.06). Thus the directions must not be compared without reversing one convention and recognizing the MI sensitivity population/estimation procedure.

DOC-001 pp. 1, 3, and 6 match the final SAP definitions: randomized 146; primary-analysis IPC/talc denominators 73/71; primary total hospital days from procedure to death or 12 months, including hospice and midnight-crossing admissions; secondary breathlessness/QoL measures; and planned/used ITT analysis. DOC-001 p. 3 describes multiple-imputation sensitivity analysis when VAS/EQ5D data are missing.

## Interpretation limits

The protocols and SAP are prospective planning records, including historical protocol versions and blank output shells; they are not evidence that a planned value was observed. No candidate or adjudication conclusion is made here. Numerical background claims and external-reference statistics were recorded only where they define a design or scale; they were not treated as trial results.
