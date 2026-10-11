# Statistical Consistency Review — Pass 1

## Completion record

- **Runtime task ID:** `/root/statistical_pass_1`
- **Required role configuration:** fresh statistical specialist, `gpt-5.6-terra` / high effort.
- **Exact scope:** Stable inferential relationship inventory `S001`-`S020` (20 relationships): main mapper `S001`-`S013` and support mapper `S-SUP-001`-`S-SUP-007`, normalized to `S014`-`S020`.
- **Completion:** Every assigned relationship is marked `PASS_1_COMPLETE` in `statistics/relationship_inventory.md`.
- **Checks applied:** containment; endpoint ordering; sign/direction; effect-measure, reference-direction, and scale labels; matched repetitions; and source-compatible P/CI/model diagnostics only. Missing inferential inputs are named rather than inferred.
- **Candidate output:** Five pre-ID candidates (`P1-S-001` through `P1-S-005`); no stable candidate IDs created; no adjudication, severity, validity, or correction assigned.

## Candidate index

| Pre-ID | Relationship(s) | Candidate topic | Exact direct-source comparator |
|---|---|---|---|
| P1-S-001 | S014, S015 | Primary endpoint threshold is `≥1` versus `>1` SAE | PDF-001 p. 6; PDF-004 p. 5; corroborating PDF-002 p. 2 and PDF-003 p. 4 |
| P1-S-002 | S014 | Planned hospital-day medians 18/15 versus 8/5 | PDF-002 p. 3; PDF-003 pp. 3-4 |
| P1-S-003 | S005, S018 | Bayesian OR/RR prior ranges conflict | PDF-001 p. 4; PDF-003 p. 8 |
| P1-S-004 | S009, S011, S019 | GA boundary `≥28` versus `>28` | PDF-001 p. 8; PDF-003 pp. 3, 9 |
| P1-S-005 | S014 | Primary endpoint start is enrollment versus randomization | PDF-002 pp. 3, 11; PDF-003 p. 7; PDF-001 p. 6 |

Full direct-source evidence, consistency rules, direct-observation/diagnostic separation, and human questions are in the inventory’s `Pass-1 pre-ID candidate records` section.

## Relationship-by-relationship completion cross-reference

This table makes the exhaustive pass-1 scope explicit; detailed checks for each relationship are in
`statistics/relationship_inventory.md`.

| S ID | Pass-1 record |
|---|---|
| S001 | `PASS_1_COMPLETE` |
| S002 | `PASS_1_COMPLETE` |
| S003 | `PASS_1_COMPLETE` |
| S004 | `PASS_1_COMPLETE` |
| S005 | `PASS_1_COMPLETE` |
| S006 | `PASS_1_COMPLETE` |
| S007 | `PASS_1_COMPLETE` |
| S008 | `PASS_1_COMPLETE` |
| S009 | `PASS_1_COMPLETE` |
| S010 | `PASS_1_COMPLETE` |
| S011 | `PASS_1_COMPLETE` |
| S012 | `PASS_1_COMPLETE` |
| S013 | `PASS_1_COMPLETE` |
| S014 | `PASS_1_COMPLETE` |
| S015 | `PASS_1_COMPLETE` |
| S016 | `PASS_1_COMPLETE` |
| S017 | `PASS_1_COMPLETE` |
| S018 | `PASS_1_COMPLETE` |
| S019 | `PASS_1_COMPLETE` |
| S020 | `PASS_1_COMPLETE` |

## Non-candidate statistical checks

- Main Table 2/abstract Bayesian primary and hospital-day estimates are contained in ordered CrIs and use a consistent late-relative-to-early benefit direction.
- Figure 3’s overall Bayesian RD display (−0.08 [−0.17 to 0.002]) is compatible with Table 2’s percentage display (−7.9% [−16.9% to 0]) after finite-precision display; it is not a candidate.
- Main Bayesian and eTable frequentist primary/hospital-day results are explicitly distinct inferential frameworks and are not treated as conflicting solely because their estimates/intervals differ.
- Source-compatible diagnostic approximations for eTable RR/P pairs are approximately .015 (primary) and .37 (hospital days). Exact model coefficients, SEs, P-value tests, and rounding conventions are absent, so these diagnostics produce no candidate.
- No checked relationship contains a finite-precision P-value display zero.

## Limitations

- Exact SEs, test statistics, degrees of freedom, variance estimators, sidedness, and P-value rounding rules are not supplied for the eTable P values.
- Raw data and a final amendment-to-analysis mapping are absent; no unreported model or estimand mapping was inferred.
- All records remain pending human adjudication after later ledger registration and mechanical source recheck.
