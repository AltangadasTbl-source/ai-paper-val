# Main-paper numeric consistency review

Complete assigned scope: DOC-001 REPORT, N001–N079 and Table4 numeric portions S017–S032, all10 PDF pages reviewed through current source-linked map and direct source extractions/rendered displays. Authority: supplied PDF, not derivative conclusions. Full calculations and outcomes are in `relationships/parts/numeric_main.md`. No qualifying F-NUM finding was identified after complete assigned coverage. Relationship totals:79 stable N relationships,16 Table4 cross-references,0 findings,8 excluded observations. No candidate IDs or adjudications assigned.

## Findings

None in this bounded numeric shard. Participant-flow arithmetic, primary counts, all table percentages, safety fractions, Table5 absolute risk differences and effect identities were checked. The supplied adjusted Cox and mixed-model estimates are not crude count ratios or raw mean subtractions.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| DOC-001 REPORT PDF p.5 Table1 hyperlipidemia, N045 | O18/64=28.125% versus29.0%; P19/62=30.6452% versus29.7%. Half-unit input intervals yield[27.1318,29.1339]% and[29.6,31.7073]%, overlapping the printed intervals[28.95,29.05]% and[29.65,29.75]%. Gap0,relative discrepancy0 for both. Even fixed-integer percentage residuals divided by printed value are below.05. No row-specific denominator is imputed. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 REPORT PDF p.5 Table1 placebo living arrangements, N032–N034 | Printed49+10+1=60 versus column n62. Sum half-unit interval[58.5,61.5] and denominator interval[61.5,62.5] touch; gap0. With exact counts2/62=.03226 also below.05. Row percentages individually reconcile with62. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 REPORT PDF p.5 Table1 race, N023–N025 | Olanzapine printed84.4+9.4+6.3=100.1%; individually rounded categories reconcile with54+6+4=64. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 REPORT PDF p.6 Table2 DKEFS color row/footnotes, N057 | Superscript i points to Barnes scale while footnote h explicitly defines both DKEFS measures. Row name and footnote h identify the intended scaled score1–19; no printed value changes. | NOTATION_OR_TYPOGRAPHY |
| DOC-001 REPORT PDF pp.4,6 SAS/AIMS definitions, N017 | SAS0–40 versus explicitly head-dropping-excluded0–36 is different score totals; AIMS item-level0–5 versus overall severity0–4 is different scoring quantities. No matched quantity conflict established. | NOT_REPRODUCED |
| DOC-001 REPORT PDF p.4 UKU adverse-effect definition, N017 | Items stated0–3 and threshold says score3 or4, or2-point increase. Out-of-range4 is a redundant alternative beside attainable3; it does not change the immediately usable threshold or any printed adverse-effect percentage. | CONTEXT_RESOLVES |
| DOC-001 REPORT PDF pp.7–8 NNT, N069 | NNT2.8 attributed to HR; crude inverse RD from13/64 and34/62 is2.89635. Even before count-input rounding, gap from printed[2.75,2.85] is.04635/2.8=.01655≤.05. No stated time-specific survival calculation is contradicted by this difference. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 REPORT PDF pp.7–8 Table4, N075; S017–S032 | Several changes differ from subtraction of marginal baseline/termination means or medians. Footnote explicitly says difference may not equal subtraction because missing data; median of changes also need not equal difference of medians. Printed n permit different observation sets; equal marginal n do not establish paired identity. | CONTEXT_RESOLVES |

## Source evidence and limitations

Exact source authority for all apparent issues: `jama_flint_2019_oi_190079.pdf#page=4`, `#page=5`, `#page=6`, `#page=7`, `#page=8`. Supplied source role is REPORT at every compared location. Source-linked relative links from this shard directory: [Table1](../../../../jama_flint_2019_oi_190079.pdf#page=5), [Table2](../../../../jama_flint_2019_oi_190079.pdf#page=6), [NNT](../../../../jama_flint_2019_oi_190079.pdf#page=7), [Table4](../../../../jama_flint_2019_oi_190079.pdf#page=8), [Safety definitions](../../../../jama_flint_2019_oi_190079.pdf#page=4). Direct Poppler text and main-mapping CPU images confirmed the printed values; no OCR discrepancy was observed. Limits: paired individual data, exact underlying Cox/survival output and blank Table4 baseline n cells are absent. All assigned relationships are checked; there is no scientific coverage gap.
