# Support Quantitative Evidence Map

## Scope and method

Direct-source mapping completed for DOC-002 PDF pp. 1-153, DOC-003 pp. 1-9, DOC-005 pp. 1-3, and DOC-006 p. 1 with fresh extraction. DOC-004 pp. 1-18 was mapped with the eligible native page text and rendered-page assets, with direct PDF visual confirmation for the figure pages. Direct PDFs remain the authority. DOC-003 is image-only; rendered-page inspection was required because `pdftotext` yielded no usable text.

Every assigned page was inspected. Administrative/no-result units are explicitly recorded below. This map reports observations and relationships, not candidate diagnoses.

## DOC-002 — protocol and amendment history (pp. 1-153)

### Complete page grouping

| PDF pages | Content | Result relevance |
|---|---|---|
| 1-47 | Protocol version 1.1 (04 December 2020), including cover/contents, objectives, design, procedures, analysis and references | Protocol definitions and planned analyses; no trial results |
| 48-93 | Protocol version 2.0 (31 May 2023) | Revised protocol definitions and planned analyses; no trial results |
| 94-139 | Protocol version 3.0 (26 June 2024) | Revised protocol definitions and planned analyses; no trial results |
| 140-153 | Summary-of-changes tables for versions 1.1→2.0 and 2.0→3.0 | Administrative/protocol-change evidence; no trial results |

The three protocol versions use the same core endpoint framework. Version 3.0 is the latest supplied protocol. Key changes in pp. 140-153 include the site count (13 to 14), recruitment duration, expected enrolment rate, eligibility wording, placebo description, and administrative safety procedures. These amendment records are not outcome-result tables.

### Result-relevant protocol definitions and planned quantities

| Provisional ID | Exact location | Direct-source observation / relationship |
|---|---|---|
| UN001 | `joi250087supp1_prod_1766516490.96011.pdf#page=14` (v1.1; corresponding definitions recur in v2/v3) | Primary outcome: time to successful ECMO weaning. Success requires survival without ECMO, another mechanical circulatory device, or heart transplantation for 30 days after ECMO removal; participants still on ECMO at day 30 are censored at day 30. |
| UN002 | DOC-002 p. 14; pp. 8, 37 | Primary analysis is a competing-risk analysis: successful weaning is the event of interest; death and weaning failure are competing events. Cumulative incidence is planned at days 15 and 30 with 95% CIs. |
| UN003 | DOC-002 p. 10; p. 37 | Planned enrolment is 206 participants, 103 per arm. Sample-size inputs: control cumulative incidence 50%, subdistribution HR 1.75, two-sided alpha 5%, power 80%, 101 successful-weaning events. |
| UN004 | DOC-002 p. 16 | Randomization is 1:1; minimization follows 20 initially balanced assignments, with assignment probability 0.8, stratified by primary cardiogenic-shock etiology and center. |
| UN005 | DOC-002 pp. 8, 14, 20, 37 | Secondary endpoints include D30/D60 mortality; ECMO duration/free days; ICU/hospital duration; MACE at D30/D60; hemodynamic and organ-failure measures; catecholamine and ventilation durations/free days; D30 LVEF; and drug adverse effects. Predefined etiologic subgroups are acute myocardial infarction, myocarditis, post-cardiac surgery, and post-cardiac arrest. |
| UN006 | DOC-002 p. 37 (fresh layout-extraction lines 1805-1935 are only a locator) | Planned descriptive measures: counts/percentages for qualitative variables; mean, SD, 95% CI, median, range, and IQR for quantitative variables; Kaplan-Meier for mortality through 60 days. |
| UN007 | DOC-002 p. 37 | Primary comparison: Fine-Gray model adjusted for prognostic factors, reporting subdistribution HR (sHR) with 95% CI; proportional-hazards assessment uses Schoenfeld residuals. A cause-specific Cox sensitivity analysis is planned. |
| UN008 | DOC-002 p. 37 | Planned secondary methods: chi-square/corrected chi-square/Fisher or logistic model for qualitative outcomes; t test or Mann-Whitney-Wilcoxon and linear regression for quantitative outcomes; log-rank/Cox for mortality. All comparisons have two-sided type-I error 5%. |
| UN009 | DOC-002 pp. 141-153 | Amendment history changes planned recruitment logistics (13→14 sites; inclusion period 24→24+12 and later 36+3 months; expected enrolment rate 0.7→0.4 per site/month) while retaining total planned sample size 206 in the displayed change table (p. 144). |

## DOC-003 — Statistical Analysis Plan (pp. 1-9)

| Provisional ID | Exact location | Direct-source observation / relationship |
|---|---|---|
| UN010 | `joi250087supp2_prod_1766516490.96511.pdf#page=3` | Main endpoint is time to successful ECMO weaning within 30 days; successful weaning requires 30-day survival without ECMO/other mechanical support/transplant. |
| UN011 | DOC-003 p. 3 | Endpoint event-state definitions: successful weaning = event; unsuccessful weaning, death before day 30 without an attempt to wean, and new event at/after day 30 are competing events; absence of the listed events by day 30 is censored. |
| UN012 | DOC-003 p. 4 | Secondary endpoint definitions include D30/D60 mortality, ECMO support duration/free days, ICU/hospital duration, MACE, hemodynamic improvement, SOFA-defined organ failure (SOFA score ≥2 in at least one system), catecholamine and ventilation measures, RRT, LVEF, and safety. |
| UN013 | DOC-003 p. 5 | Sample-size specification matches UN003: control cumulative incidence 50%, competing risks, sHR 1.75, alpha 5%, power 80%, 101 events, total n=206 (103/group). Primary analysis population is intention-to-treat, with all randomized participants retained in assigned groups. |
| UN014 | DOC-003 p. 6 | Main analysis: CIF at days 15 and 30 with 95% CIs; Gray test; Fine-Gray model adjusted for primary etiology (acute MI, myocarditis, post-heart surgery, other); sHR with 95% CI; Schoenfeld assessment; cause-specific Cox sensitivity analysis with csHR. |
| UN015 | DOC-003 pp. 7-8 | Secondary analytic definitions: D30/D60 mortality uses Kaplan-Meier/log-rank/Cox; ECMO/free-day and several duration outcomes use Wilcoxon rank-sum with deaths imputed as zero failure-free days and adjusted general linear models; ICU/hospital stay uses RMST to day 60 and Cox; MACE uses Kaplan-Meier/log-rank/Cox. |
| UN016 | DOC-003 p. 8 | LVEF is compared using Global Net Benefit at D30: hierarchical death, transplant, then LVEF improvement >30%; net benefit is wins minus losses divided by total comparisons, with bootstrap 95% CI. Drug adverse reactions and adverse-event counts use Poisson regression adjusted for prognostic factors. |
| UN017 | DOC-003 p. 9 | All analyses are two-sided alpha 5%; primary-outcome missingness is censored without imputation; software is R 4.4.2. |

## DOC-004 — supplementary results (pp. 1-18)

| Provisional ID | Exact location | Direct-source observation / relationship |
|---|---|---|
| UN018 | `joi250087supp3_prod_1766516490.97011.pdf#page=3`, eTable 1 | Consent groups reconcile: emergency-consent denominators 69+77=146 and close-relative/surrogate denominators 32+27=59; 146+59=205, with category counts summing to each denominator. |
| US001 | DOC-004 p. 4, eTable 2 | Cause-specific Cox (adjusted for cardiogenic-shock etiology): successful weaning csHR 1.15 (95% CI 0.82-1.62), P=.42; weaning failure 0.91 (0.46-1.82), P=.79; death before weaning 1.57 (0.72-3.44), P=.26. |
| UN019 | DOC-004 pp. 5-6, eTable 3 | Secondary endpoint table uses medians (IQR) or n (%); absolute differences are median or percentage-point differences with bootstrap 95% CIs; binary relative effects are RRs. RR/CI are intentionally not estimated if either group has zero events; no secondary-outcome P values are reported because of multiple-testing concerns. |
| UN020 | DOC-004 p. 5, eTable 3 | At D30: organ-failure-free days 12 (0-21) vs 14 (0-23), difference -2 (-10 to 4); organ-failure days 9 (6-17) vs 12 (6-18), -3 (-5 to 2); catecholamine-free days 18 (0-23) vs 18 (5-25), 0 (-4 to 6); catecholamine duration 9 (5-13) vs 10 (5-16), -1 (-4 to 2), Levosimendan vs Placebo. |
| UN021 | DOC-004 pp. 5-6, eTable 3 | MACE D30: 35/101 (34.7%) vs 36/104 (34.6%), RD 0.0 (-12.6 to 13.6), RR 1.00 (0.69-1.46). MACE D60: 36/101 (35.6%) vs 39/104 (37.5%), RD -1.9 (-15.4 to 11.7), RR 0.95 (0.66-1.36). Components and denominators are printed on pp. 5-6. |
| UN022 | DOC-004 p. 7, eTable 4; p. 15, eFigure 6 | Daily dobutamine, epinephrine, and norepinephrine median/IQR doses from randomization through day 7 are tabulated. The figure is a graphical rendering of these drug-dose trajectories; table values are the exact numerical source. |
| UN023 | DOC-004 p. 8, eTable 5 | Exposure/duration data: dobutamine 93/101 (92.1%) vs 96/104 (92.3%), 6 [4-10] vs 7 [4.75-13]; epinephrine 8/101 (7.9%) vs 5/104 (4.8%), 1 [1-1] vs 1 [1-2]; norepinephrine 93/101 (92.1%) vs 98/104 (94.2%), 7 [4-11] vs 5 [3-12]; other vasoactive drugs 14/101 (13.9%) vs 12/104 (11.5%), 2.5 [1.25-3] vs 2 [1-3.25]. |
| UN024 | DOC-004 p. 9, eTable 6 | “Other” cardiogenic-shock causes use n=21 in each arm, with six listed categories; counts per arm sum to 21 and each percentage corresponds to its printed numerator/21 denominator, subject to one-decimal rounding. |
| UN025 | DOC-004 p. 10, eFigure 1 | Trajectory categories sum to randomized totals: Levosimendan 69 successful (68.3%), 11 unsuccessful/death (10.9%), 4 transplant (4.0%), 15 LVAD (14.9%), 2 censored (2.0%) =101; Placebo 71 (68.3%), 12 (11.5%), 5 (4.8%), 4 (3.8%), 12 death-before-weaning (11.5%), 0 censored =104. |
| US002 | DOC-004 p. 11, eFigure 2 | D30 mortality log-rank P=.47 and D60 mortality log-rank P=.56. Exact plotted cumulative-event counts at D30 are Placebo 23 and Levosimendan 26; at D60, Placebo 26 and Levosimendan 28. |
| UN026 | DOC-004 p. 13, eFigure 4 | MACE figure displays D30 and D60 cumulative-event counts and log-rank P=.87 and P=.94, respectively. Its D30 terminal counts (Placebo 36; Levosimendan 35) and D60 terminal counts (Placebo 39; Levosimendan 36) match eTable 3. |
| UN027 | DOC-004 p. 14, eFigure 5 | Mean blood-pressure trajectory is displayed in mm Hg at days 1,5,10,15,20,25,30; total plotted n values are 203,191,139,102,61,44,38. The blue dashed reference is 60 mm Hg. Exact plotted means are graphical rather than printed as a table. |
| UN028 | DOC-004 p. 16, eFigure 7 | Restricted mean stay durations to D60 are labelled hospital: Levosimendan 28 days, Placebo 35 days; ICU: Levosimendan 17.5 days, Placebo 19 days. |
| UN029 | DOC-004 p. 17, eFigure 8 | Serious-adverse-event-count distributions reconcile to allocated group sizes: Levosimendan frequencies 42,22,19,8,2,4,2,2 across 0,1,2,3,4,5,6,8 events total 101; Placebo 43,31,13,4,6,3,1,2,1 across 0,1,2,3,4,5,6,8,9 total 104. |
| US003 | DOC-004 p. 18, eFigure 9 | Subgroup Fine-Gray sHRs (Levosimendan vs Placebo as shown by legend): acute MI 0.73 (95% CI 0.37-1.40); myocarditis 2.16 (0.97-4.80); post-heart surgery 0.73 (0.46-1.15); others 1.61 (0.78-3.33). |

## DOC-005 and DOC-006 — no result-relevant quantitative evidence

DOC-005 pp. 1-3 is a nonauthor-collaborator roster. It has no study results, tables, figures, endpoint definitions, or statistical results; all three pages are mapped as not applicable for quantitative-result extraction. DOC-006 p. 1 is a data-sharing statement: data available “No” and ClinicalTrials.gov identifier NCT04728932 are administrative metadata, not a quantitative study result. No workbook/CSV/Office source was supplied, so no formula-versus-cached-value distinction applies.
