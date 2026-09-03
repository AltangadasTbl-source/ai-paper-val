# Support Relationship Inventory — Provisional IDs

All IDs are provisional mapper IDs for coordinator normalization. They are not candidates or adjudications. Each listed relationship has a direct-source location in `extraction/support_quantitative_evidence.md`.

## Numeric/reporting relationships

| ID | Source pages | Relationship |
|---|---|---|
| UN001-UN004 | DOC-002 pp.20-22 | Protocol AF-projection, whole-trial and subgroup sample-size/power tables. |
| UN005-UN010 | DOC-003 pp.7-22 | SAP outcome/population/follow-up/patch and anticoagulation definitions, planned denominators, and sample-size assumptions. |
| UN011 | DOC-004 p.2 | Patch duration, >=30-second AF definition, urgent-report thresholds. |
| UN012-UN013 | DOC-004 p.4 | Patch adherence/usage and short-wear reason denominators. |
| UN014-UN017 | DOC-004 pp.5-6 | Patch-data availability baseline counts, percentages, and medication/diagnosis breakdowns. |
| UN018-UN019 | DOC-004 p.7 | Patch-detected condition counts and two denominator-specific proportions. |
| UN020-UN021 | DOC-004 p.8 | Sensitivity AF counts/proportions, differences, ratios, CIs and subgroup heterogeneity. |
| UN022 | DOC-004 p.9 | AF histogram scales and grouped-duration percentages. |
| UN023 | DOC-004 p.10 | Time-to-primary-care-AF risk set and immediate-event definition. |
| UN024 | DOC-004 p.11 | AF/AFL histogram scales and grouped-duration percentages. |

## Inferential/statistical relationships

| ID | Exact source pages | Definition / planned or displayed inferential relationship |
|---|---|---|
| US001 | DOC-003 pp.7-9,18 | Primary ITT screen-versus-usual-care 2.5-year primary-care AF proportion; chi-square, arm proportions, ratio of proportions and 95% CI. |
| US002 | DOC-003 pp.9,18 | Primary-outcome age (<80/>=80) and sex subgroup chi-square comparisons with heterogeneity testing. |
| US003 | DOC-003 pp.8-9,14,18 | Five-year mean time-with-known-AF estimand; permutation comparison; no-AF contributes zero; empirical p=(1+s)/(n+1), with s simulations at least as extreme and n total simulations. |
| US004 | DOC-003 p.18 | Sensitivity primary/secondary analyses using AF from primary or secondary care. |
| US005 | DOC-003 p.19 | 2.5- and 5-year time-to-first-AF curves, log-rank testing, and censoring at death/withdrawal/primary-care loss/day 913 or 1826. |
| US006 | DOC-003 pp.19-20 | Oral-anticoagulant record proportions (chi-square), months/exposure mean (permutation), and time-to-record (log-rank) to 30/60 months. |
| US007 | DOC-003 pp.21-22 | Planning: 1.75% versus 4.4%, ratio about 2.5; power statements; two-sided alpha <.05; no formal multiplicity adjustment; primary/secondary 95% CIs. |
| US008 | DOC-004 pp.5-6 | eTable 2 association tests: categorical chi-square; ordinal Mantel-Haenszel trend; two-sample t test for normal continuous and Mann-Whitney U for nonnormal continuous variables; missing excluded. |
| US009 | DOC-004 p.8 | Sensitivity overall AF ratio 1.21 (95% CI 1.02-1.45), p=.03, and unadjusted-for-multiplicity subgroup CIs. |
| US010 | DOC-004 p.8 | Sensitivity subgroup effect-modification/heterogeneity: age p=.28 and sex p=.07. |
| US011 | DOC-004 p.10 | Kaplan-Meier time from urgent patch report to first primary-care AF record among patch-detected AF, including seven immediate events. |

## Explicit mapping completion records

- DOC-002 pp.1-26: `MAPPED_PROTOCOL_ALL_PAGES`; no observed results display; planning tables and protocol definitions mapped.
- DOC-003 pp.1-24: `MAPPED_SAP_ALL_PAGES`; no observed results display; every result-relevant analysis definition, estimator, censoring rule, testing rule, and planning quantity mapped.
- DOC-004 pp.1-11: `MAPPED_RESULTS_SUPPLEMENT_ALL_PAGES`; pp.2-3 directly extracted fresh and all displayed results, definitions, tables, figures, captions, and footnotes mapped.
