---
title: "Reporting-Consistency Audit of 20 JAMA-Family Articles"
subtitle: "Synthesis and statistical analysis of retained Major and Minor findings"
date: "2026-07-23"

documentclass: article
fontsize: 10pt
geometry:
  - top=20mm
  - bottom=21mm
  - left=20mm
  - right=20mm
mainfont: "Noto Serif CJK SC"
sansfont: "Noto Sans CJK SC"
monofont: "Noto Sans Mono CJK SC"
colorlinks: true
linkcolor: "2B5D86"
urlcolor: "2B5D86"
toc: true
toc-depth: 2
numbersections: true
header-includes:
  - |
    \usepackage{booktabs}
    \usepackage{longtable}
    \usepackage{array}
    \usepackage{float}
---


# Executive summary

This report synthesizes the authoritative final Markdown report in each of 20 article
audit packages: 18 `final_report.md` files and two higher-priority
`human_adjudication_report.md` files. Only retained items in the final Scientific
Findings/Scientific Issues section were counted. Rejected, Uncertain, compliance-screen,
and candidate-stage items were excluded.

All 20 articles had at least one retained finding (100%; Wilson 95% CI
83.9%–100.0%). There were 111 findings: 22
Major (19.8%; Wilson 95% CI 13.5%–
28.2%) and 89 Minor (80.2%).
12/20 articles had at least one Major finding (60.0%;
Wilson 95% CI 38.7%–78.1%).

Presentation inconsistency was the most frequent formal category (49; 44.1%).
Cross-document inconsistency was less common (17) but 8/17 were Major (47.1%),
the highest Major density among the main categories. Multi-label artifact coding found
supplementary tables in the evidence chain of 69 findings across 18 articles, making
them the clearest concentration of risk. Flow diagrams were involved in 15 findings
across 10 articles, although only five findings were formally categorized as participant
flow inconsistency; the remainder concerned denominators, labels, or cross-document
alignment.

> Interpretation: “finding” means retained in the audit report and submitted for human
> adjudication. It does not necessarily mean author-confirmed error or completed correction.

# Data and methods

## Inclusion and source selection

- The 20 packages comprise 19 JAMA articles and one JAMA Surgery article; eight package
  IDs are from 2024 and 12 from 2025.
- A `human_adjudication_report.md` was preferred when present
  (`jama.2024.19585` and `jama.2024.4183`); otherwise `final_report.md` was used.
- Only final retained scientific findings were parsed. Rejected and Uncertain items
  were excluded from numerators.
- Each finding has one formal audit category, while artifact locations and text themes
  are multi-label.
- The complete 111-row ledger is `meta_report/audit_findings.csv`, including the source
  report path and normalized evidence text.

## Analysis

Counts, proportions, mean, median, quartiles, and range were calculated from the
finding-level ledger. Wilson 95% confidence intervals are reported for article-level
proportions. Text mining used a rule-based dictionary over each accepted finding's
title, locations, compared values, basis, and verification instructions. Thus an
artifact/theme count means involvement in the evidence chain, not necessarily the sole
root cause, and multi-label totals do not sum to 111.

Each audit could retain no more than 10 final findings; two articles reached that cap.
The total of 111 is therefore the count of prioritized final findings, not an
uncapped inventory of every detectable defect.

# Quantitative results

## Burden by article

The mean was 5.55 findings per article (SD
2.87); the median was 5.5,
IQR 3–8, range 1–10. The 2024 packages contributed 48 findings across eight articles
(mean 6.00; 10 Major), while the 2025 packages contributed 63 across 12 articles
(mean 5.25; 12 Major). This is descriptive only: the packages are not a random sample,
and year is confounded with package complexity and audit maturity.

![Major and Minor findings by article.](figures/article_findings.pdf){ width=92% }

| Article package | Major | Minor | Total |
| --- | ---: | ---: | ---: |
| jama.2024.11057 | 0 | 2 | 2 |
| jama.2024.12829 | 3 | 6 | 9 |
| jama.2024.19585 | 0 | 3 | 3 |
| jama.2024.2302 | 1 | 2 | 3 |
| jama.2024.240147 | 1 | 7 | 8 |
| jama.2024.24764 | 0 | 4 | 4 |
| jama.2024.4183 | 2 | 7 | 9 |
| jama.2024.6063 | 3 | 7 | 10 |
| jama.2025.11178 | 3 | 7 | 10 |
| jama.2025.15440 | 0 | 1 | 1 |
| jama.2025.16450 | 0 | 4 | 4 |
| jama.2025.19563 | 1 | 5 | 6 |
| jama.2025.20765 | 2 | 6 | 8 |
| jama.2025.250116 | 2 | 5 | 7 |
| jama.2025.4390 | 1 | 6 | 7 |
| jama.2025.7583 | 0 | 2 | 2 |
| jama.2025.7710 | 1 | 1 | 2 |
| jama.2025.9110 | 0 | 6 | 6 |
| jama.2025.9663 | 0 | 5 | 5 |
| jamasurg.2025.4929 | 2 | 3 | 5 |

## Formal error categories

| Audit category | Findings | Share of 111 | Major | Major within category | Articles |
| --- | ---: | ---: | ---: | ---: | ---: |
| Presentation inconsistency | 49 | 44.1% | 6 | 12.2% | 19 |
| Statistical reporting inconsistency | 24 | 21.6% | 5 | 20.8% | 13 |
| Cross-document inconsistency | 17 | 15.3% | 8 | 47.1% | 9 |
| Arithmetic inconsistency | 16 | 14.4% | 1 | 6.2% | 9 |
| Participant flow inconsistency | 5 | 4.5% | 2 | 40.0% | 4 |

![Formal audit category and severity.](figures/category_severity.pdf){ width=92% }

Severity structure matters more than frequency alone. Cross-document inconsistency
had 8 Major findings among 17, and participant-flow inconsistency had 2 among 5.
Presentation findings were far more numerous but only 6/49 were Major; arithmetic
inconsistency had only 1 Major among 16. High-frequency low-level defects therefore
clustered in presentation, whereas substantive conflict between the main article,
supplements, figures, or analysis populations was more likely to become Major.

![Error-category profile by article.](figures/category_heatmap.pdf){ width=96% }

# Common failure points

| Artifact/location (multi-label) | Finding mentions | Articles |
| --- | ---: | ---: |
| Supplementary table | 69 | 18 |
| Narrative/abstract | 28 | 15 |
| Other figure | 22 | 11 |
| Other main table | 21 | 9 |
| Flow diagram | 15 | 10 |
| Supplementary figure | 14 | 9 |
| Table 1/baseline | 9 | 9 |

![Artifacts involved in each finding's evidence chain; labels are nonexclusive.](figures/artifact_involvement.pdf){ width=92% }

## Supplementary tables and Table 1

Supplementary tables were involved in 69/111 findings across 18/20 articles. Recurrent
patterns were header denominators that disagreed with cell percentages, mixtures of
ITT/PPS/safety populations, duplicated or shifted blocks, mislabeled effect measures
or models, and footnotes that contradicted the body. Table 1/baseline material was
involved in nine findings across nine articles, including nonconserving sex counts,
a one-person FIO2 discrepancy between Table 1 and Figure 2, a repeated calcium-channel
blocker percentage error, and different ethnicity-denominator conventions.

## Flow diagrams

Flow/CONSORT diagrams were involved in 15 findings across 10 articles, while only five
findings across four articles carried the formal participant-flow category. The
difference reflects presentation, population, and cross-document problems that surfaced
through a flow figure. High-yield checks are node conservation; explicit separation of
randomized, treated, followed, and analyzed populations; postrandomization withdrawal
branches; the unit of randomization; and agreement with prose and Table 2 analysis sets.

## Narrative, figures, footnotes, and cross-references

Narrative/abstract text was involved in 28 findings across 15 articles; other main
figures in 22 and other main tables in 21. Manual review confirmed at least five direct
cross-reference/location errors: `jama.2024.2302`, `jama.2024.6063`,
`jama.2025.19563`, `jama.2025.9110`, and `jama.2025.9663`. Dictionary coding also
flagged footnotes, titles, captions, and legends repeatedly, showing that semantic
labels require checks independent of the numerical cells.

# Statistical significance, confidence intervals, P values, and definitions

## Confidence intervals

Manual review identified seven findings centered on CI error or incompatibility:
`jama.2024.12829`, `jama.2024.4183`, two in `jama.2025.11178`,
`jama.2025.15440`, `jama.2025.250116`, and `jamasurg.2025.4929`.
Patterns included a point estimate outside its CI, reversed limits, different CIs for
the same comparison across abstract and body, and CI/P-value disagreement. The most
concentrated example was `jama.2025.11178`: seven rows had 95% CIs excluding zero
while their P values exceeded .05, plus a separate group of SMDs outside their CIs.

## P values and test methods

At least five findings made the P value or test method a central contradiction:
“Chi-square” rows that reproduced Fisher exact results (`jama.2024.12829`);
an unqualified no-difference narrative despite day-7 P=.02 and a CI excluding zero
(`jama.2024.24764`); grouped CI–P disagreement (`jama.2025.11178`);
two age P-value footnotes (`jama.2025.19563`); and identical binary counts with
different P values (`jama.2025.4390`). These should be separated into calculation
errors, method-label errors, and narrative failure to distinguish global interaction
from time-specific contrasts.

## Text and conceptual definitions

Recurring conceptual defects included an OR labeled “difference,” RR expanded as risk
difference, a univariate estimate described as multivariable, within-stratum treatment
ORs labeled interactions, median(IQR) labeled mean(SD), FiO2 fractions labeled
percentages, and one analysis unit called women, infants, and patients. These defects
may leave cell values unchanged while materially changing interpretation of the
estimand, population, or model.

| Dictionary theme (multi-label) | Finding hits | Articles |
| --- | ---: | ---: |
| Count/percentage arithmetic | 72 | 20 |
| Denominator/population | 54 | 19 |
| Footnote/title/caption/legend | 45 | 17 |
| P value/test labeling | 23 | 11 |
| Participant-flow wording | 21 | 13 |
| Summary-statistic/unit label | 20 | 13 |
| Duplicate/transposed content | 20 | 13 |
| Effect measure/model label | 20 | 12 |
| CI/point-estimate compatibility | 18 | 13 |
| Cross-reference/citation | 5 | 5 |
| Other wording/definition | 3 | 2 |

# The 22 Major findings

| Article | Finding | Category | Major finding synopsis |
| --- | --- | --- | --- |
| jama.2024.12829 | 1 | Statistical reporting inconsistency | Stroke incidence-difference CI excludes its point estimate |
| jama.2024.12829 | 2 | Cross-document inconsistency | Figure S5 conflicts with its denominator and Table S11 disabling-stroke counts |
| jama.2024.12829 | 3 | Cross-document inconsistency | Table S6 mixes ITT and PPS data |
| jama.2024.2302 | C1 | Presentation inconsistency | Abstract mislabels the 320 postwithdrawal cohort as repaired; actual repair total is 281 |
| jama.2024.240147 | F1 | Participant flow inconsistency | Randomized, intervention-stage, and analyzed populations are conflated |
| jama.2024.4183 | C04 | Cross-document inconsistency | CNRT+ lozenge dose conflicts as 2 mg versus 4 mg |
| jama.2024.4183 | C08 | Presentation inconsistency | Two supplemental estimates/intervals appear decimal-shifted |
| jama.2024.6063 | C04 | Arithmetic inconsistency | eTable 4 pain-change block duplicates an unrelated function row and conflicts with endpoints |
| jama.2024.6063 | C05 | Presentation inconsistency | Lower-leg-strength inference block exactly duplicates a back-pain row |
| jama.2024.6063 | C07 | Cross-document inconsistency | Main Table and eTable 7 adverse-event totals differ by five |
| jama.2025.11178 | 1 | Participant flow inconsistency | Follow-up-pattern cells exceed randomized and followed totals |
| jama.2025.11178 | 2 | Statistical reporting inconsistency | Seven 95% CIs exclude zero while paired P values exceed .05 |
| jama.2025.11178 | 4 | Statistical reporting inconsistency | Multiple SMDs fall outside CIs, have reversed endpoints, or opposite signs |
| jama.2025.19563 | C-06 | Cross-document inconsistency | Figure 3B uses a larger HbA1c analysis population than eTable 14 without explanation |
| jama.2025.20765 | F01 | Cross-document inconsistency | eTable 2 omits a 40-participant mHealth cluster |
| jama.2025.20765 | F02 | Cross-document inconsistency | Prose reverses the direction of irritability and anxiety events |
| jama.2025.250116 | C04 | Presentation inconsistency | eFigure 8 repeats eFigure 7 inference values despite different event cells |
| jama.2025.250116 | C05 | Statistical reporting inconsistency | High-stratum treatment ORs are labeled and interpreted as interactions |
| jama.2025.4390 | SCI-01 | Presentation inconsistency | Figure 3 rate columns contain person-time |
| jama.2025.7710 | 1 | Presentation inconsistency | Primary-outcome analysis unit conflicts among women, infants, and patients |
| jamasurg.2025.4929 | F-01 | Statistical reporting inconsistency | pN N3 row is internally incompatible across counts, percentage, OR, CI, and P value |
| jamasurg.2025.4929 | F-04 | Cross-document inconsistency | Main text presents a univariate approach estimate as multivariable |

# Article-by-article synthesis (Major and Minor)


## jama.2024.11057

**Major 0; Minor 2; total 2.**

Two Minor findings: eTable 4 labels mean(SD)-like values as median(IQR), and the eTable 5 responder-only title also covers randomized-denominator rows.


## jama.2024.12829

**Major 3; Minor 6; total 9.**

Three Major findings: a stroke-difference CI excludes its point estimate; Figure S5 conflicts on denominator/disabling stroke counts; and Table S6 mixes ITT and PPS data. Six Minor findings concern S7–S9 headers/denominators, center counts, a complication count, and test-method labeling.


## jama.2024.19585

**Major 0; Minor 3; total 3.**

Three Minor findings: eTable 10 labels an OR as a difference, Figure 2 does not state time-specific denominators, and the eFigure 3 legend fails to define displayed P values.


## jama.2024.2302

**Major 1; Minor 2; total 3.**

One Major finding: the abstract says 320 infants underwent repair, whereas the article and flow diagram total 281. Two Minor findings concern an omitted withdrawal branch and an enrollment cross-reference that should point only to eTable 1.


## jama.2024.240147

**Major 1; Minor 7; total 8.**

One Major finding: the abstract/Key Points call analyzed or intervention-stage populations randomized. Seven Minor findings include center percentages, 4/743 and 0/747 errors, an orphan footnote, cross-display percentages, and an undisclosed denominator.


## jama.2024.24764

**Major 0; Minor 4; total 4.**

Four Minor findings: undisclosed multiple responses, an omitted UK-only subgroup restriction, missing subgroup denominators, and a quality-of-life narrative inconsistent with the day-7 CI/P value.


## jama.2024.4183

**Major 2; Minor 7; total 9.**

Two Major findings: the CNRT+ lozenge dose conflicts across documents, and two supplemental values appear decimal-shifted. Seven Minor findings involve flow arithmetic/wording, sex counts, direction, power monotonicity, denominators, and adverse-event qualification.


## jama.2024.6063

**Major 3; Minor 7; total 10.**

Three Major findings: a copied/incorrect change block, an unrelated row duplicated wholesale, and conflicting adverse-event totals. Seven Minor findings concern estimate sign, percentages, arm reversals, adherence, wrong eTable citations, and layout.


## jama.2025.11178

**Major 3; Minor 7; total 10.**

Three Major findings: follow-up-pattern counts do not conserve N; seven CIs exclude zero while P>.05; and SMD estimates/CIs/signs are impossible. Seven Minor findings concern percentages, duplicate or missing labels, subgroup headers, adjustment status, and mean/median wording.


## jama.2025.15440

**Major 0; Minor 1; total 1.**

One Minor finding: the same stroke comparison has different 95% CIs in the abstract and the Results/Figure 4B.


## jama.2025.16450

**Major 0; Minor 4; total 4.**

Four Minor findings: undisclosed GDB denominators, a B+S header mismatch, a one-person FIO2 discrepancy between Table 1 and Figure 2, and RR expanded as risk difference.


## jama.2025.19563

**Major 1; Minor 5; total 6.**

One Major finding: Figure 3B visibly uses a larger HbA1c population than eTable 14 without explanation. Five Minor findings concern 10/59, three wrong eTable numbers, age-P-value footnotes, BMI called weight, and percent versus percentage points.


## jama.2025.20765

**Major 2; Minor 6; total 8.**

Two Major findings: a 40-person mHealth cluster is omitted and adverse-event direction is reversed in prose. Six Minor findings cover death/adverse-event percentages, an unidentified population, death-excluded ITT wording, and a title/body mismatch.


## jama.2025.250116

**Major 2; Minor 5; total 7.**

Two Major findings: eFigure 8 repeats eFigure 7 inference values, and high-stratum treatment ORs are labeled interactions. Five Minor findings concern a narrative count, OR decimal error, a point estimate outside its CI, and duplicated/missing table characters.


## jama.2025.4390

**Major 1; Minor 6; total 7.**

One Major finding: Figure 3 columns labeled rates per 100 patient-years contain about 71 hundreds of patient-years. Six Minor findings include a duplicated ethnicity row, adjusted/unadjusted CI labeling, identical counts with different P values, geography totals, adherence, and a repeated percentage error.


## jama.2025.7583

**Major 0; Minor 2; total 2.**

Two Minor findings: inclusion wording is applied to excluded patients, and the MAGIC-MT control event count is missing.


## jama.2025.7710

**Major 1; Minor 1; total 2.**

One Major finding: the same primary-outcome analysis unit is called women, infants, and patients. One Minor finding: prose and Table 1 use different placebo-ethnicity denominator conventions.


## jama.2025.9110

**Major 0; Minor 6; total 6.**

Six Minor findings: sex counts, a protocol-deviation percentage, patient-versus-ICU randomization wording, two mean(SD)/median(IQR) labels, and a Supplement 1/3 locator.


## jama.2025.9663

**Major 0; Minor 5; total 5.**

Five Minor findings: a wrong eFigure citation, mixed analytic subsets in a summary, a truncated year, FiO2 fractions labeled percentages, and an undefined asterisk.


## jamasurg.2025.4929

**Major 2; Minor 3; total 5.**

Two Major findings: the pN N3 regression row is internally impossible, and a univariate estimate is presented as multivariable. Three Minor findings concern the age row, five unreproducible ORs, and a CONSORT refusal label.


# Interpretation, limitations, and recommendations

1. **Audit supplementary tables first.** Apply column-level denominator inference,
   percentage recomputation, estimate/CI/P-value checks, and adjacent-row duplicate
   block detection.
2. **Use an explicit population-stage dictionary.** Randomized, treated, safety, ITT,
   complete-case, PPS, and death-excluded populations should never rely on context alone.
3. **Validate figures back against generation data.** Priorities are flow conservation,
   figure units and headers, eFigure copy/paste, and caption definitions.
4. **Automate cross-reference resolution.** Every eTable/eFigure/Supplement locator in
   the main article should map one-to-one to the actual title and file location.
5. **Make statistical consistency a release gate.** A point estimate must lie within
   its CI; two-sided P values, CIs, and null conclusions should align; identical 2×2
   cells under the same method cannot yield different P values; adjustment and model
   labels must agree with source output.

Limitations include the 10-finding cap, nonrandom package selection, heterogeneous
document volume/OCR/audit scope, use of the source audit taxonomy, and rule-based
multi-label text coding. Retained/accepted findings were submitted for or framed as
human adjudication and should not be read as completed author-confirmed errata.

# Reproducibility and provenance

- `meta_report/audit_findings.csv`: 111-row finding ledger.
- `meta_report/article_counts.csv`: Major/Minor counts by article.
- `meta_report/category_counts.csv`: category-by-severity counts.
- `meta_report/artifact_counts.csv`: multi-label artifact counts.
- `meta_report/mechanism_counts.csv`: multi-label text-theme counts.
- `meta_report/generate_report.py` and `meta_report/analysis.R`: reproducible scripts.

Authoritative source reports:

- `jama.2024.11057`: `jama.2024.11057/.ai_paper_validation/final_report.md`
- `jama.2024.12829`: `jama.2024.12829/.ai_paper_validation/final_report.md`
- `jama.2024.19585`: `jama.2024.19585/.ai_paper_validation/human_adjudication_report.md`
- `jama.2024.2302`: `jama.2024.2302/.ai_paper_validation/final_report.md`
- `jama.2024.240147`: `jama.2024.240147/.ai_paper_validation/final_report.md`
- `jama.2024.24764`: `jama.2024.24764/.ai_paper_validation/final_report.md`
- `jama.2024.4183`: `jama.2024.4183/.ai_paper_validation/human_adjudication_report.md`
- `jama.2024.6063`: `jama.2024.6063/.ai_paper_validation/final_report.md`
- `jama.2025.11178`: `jama.2025.11178/.ai_paper_validation/final_report.md`
- `jama.2025.15440`: `jama.2025.15440/.ai_paper_validation/final_report.md`
- `jama.2025.16450`: `jama.2025.16450/.ai_paper_validation/final_report.md`
- `jama.2025.19563`: `jama.2025.19563/.ai_paper_validation/final_report.md`
- `jama.2025.20765`: `jama.2025.20765/.ai_paper_validation/final_report.md`
- `jama.2025.250116`: `jama.2025.250116/.ai_paper_validation/final_report.md`
- `jama.2025.4390`: `jama.2025.4390/.ai_paper_validation/final_report.md`
- `jama.2025.7583`: `jama.2025.7583/.ai_paper_validation/final_report.md`
- `jama.2025.7710`: `jama.2025.7710/.ai_paper_validation/final_report.md`
- `jama.2025.9110`: `jama.2025.9110/.ai_paper_validation/final_report.md`
- `jama.2025.9663`: `jama.2025.9663/.ai_paper_validation/final_report.md`
- `jamasurg.2025.4929`: `jamasurg.2025.4929/.ai_paper_validation/final_report.md`