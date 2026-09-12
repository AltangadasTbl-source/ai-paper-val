# 2019 retrospective document-role reclassification

Scope: all 71 current final-report candidate cards across 10 packages. Every complete candidate card was read; document inventories were consulted for all packages, followed by selected detailed mechanical rechecks, ledgers and cross-source checker records for ambiguous roles, comparator identity, amendments and overlapping candidates. This reuses the recorded validation evidence; it is not a new scientific audit and does not convert pending candidates into confirmed errors.

## Mutually exclusive primary counts

| Primary | Count | % of 71 |
|---|---:|---:|
| P_R | 8 | 11.27% |
| P_P | 10 | 14.08% |
| S_C | 13 | 18.31% |
| S_W | 40 | 56.34% |
| OTHER | 0 | 0.00% |

P_R means report versus protocol/SAP; P_P means plan-internal or plan-versus-plan; S_C means article versus non-plan supplement (or separate non-plan supplements); S_W means within one article or non-plan supplement. No P_O or P_B cases were identified in these cards.

- Any plan involvement: 18/71 = 25.35% across 9/10 packages.
- Report-versus-plan: 8/71 = 11.27%, across 6/10 packages.
- Submission-only: 53/71 = 74.65% (13 between report files, 40 within one report file).
- Among 21 report cross-file candidates (P_R + S_C), plan comparisons are 8/21 = 38.10%; submission main/supp comparisons are 13/21 = 61.90%. This denominator excludes all P_P candidates.
- Inclusive relation counts, which overlap: P_R 8; P_P 11; S_C 13; S_W 46. There are six S_C/S_W mixed cards and one P_R/P_P mixed card.

## Package counts

| Package | Total | P_R | P_P | S_C | S_W |
|---|---:|---:|---:|---:|---:|
| jama.2019.0556 | 9 | 1 | 3 | 1 | 4 |
| jama.2019.10517 | 3 | 0 | 1 | 1 | 1 |
| jama.2019.12618 | 8 | 2 | 1 | 1 | 4 |
| jama.2019.14231 | 11 | 1 | 0 | 1 | 9 |
| jama.2019.14630 | 9 | 0 | 0 | 4 | 5 |
| jama.2019.14901 | 6 | 1 | 1 | 1 | 3 |
| jama.2019.17380 | 7 | 1 | 0 | 3 | 3 |
| jama.2019.2210 | 9 | 2 | 2 | 1 | 4 |
| jama.2019.4755 | 5 | 0 | 1 | 0 | 4 |
| jama.2019.7505 | 4 | 0 | 1 | 0 | 3 |

## All report-versus-plan candidates

| Package / ID | Compared issue | Important qualification |
|---|---|---|
| 0556 C007 | Event-rate, per-group sample size and attrition planning assumptions | Different design stages or an amendment could explain the difference. |
| 12618 C003 | Block sizes {4,6} versus protocol {4,6,8} | Later SAP explicitly matches article {4,6}; original protocol may be superseded. |
| 12618 C004 | Six-month success omits protocol/manual no-injection-after-day-90 condition | Article may abbreviate an operational rule; no recalculated success count is possible. |
| 14231 C001 | Matching direction reversed between protocol and article | Protocol wording may be inverted rather than the realized analysis. |
| 14901 C002 | Reintubation pH cutoff <7.25 versus protocol <7.35 | Same decision role was checked in detail; a later refinement is possible. |
| 17380 C007 | Implemented 20 versus planned 10 imputations | Intentional analytic update or broader scope is possible. |
| 2210 C004 | De novo cancer tertiary versus safety hierarchy | Mixed P_R/P_P; change summary says separated from safety outcomes. |
| 2210 C008 | Randomization versus supplementation-start time labels | Wording-only: article explicitly equates these at the same visit. No actual date difference is claimed. |

## Original category does not identify document topology

The original Cross-document numeric inconsistency category has only 15 candidates. Reclassification: 5 P_R (33.33%), 7 S_C (46.67%), and 3 S_W (20.00%). The three S_W cases are 14630 C003 (two eTables in one supplement), 17380 C001 (main Figure 2 versus main Table 2), and 7505 C001 (main abstract versus main Table 3).

Reading all categories identifies three additional P_R cases (14901 C002; 2210 C004/C008) and six additional S_C cases (0556 C002; 10517 C002; 14231 C008; 17380 C005/C006; 2210 C006). All nine originally belonged to measure/label/scale inconsistency. Thus restricting analysis to the original cross-document category would miss 3/8 = 37.50% of the recorded report-versus-plan candidates and 6/13 = 46.15% of submission cross-file candidates.

## Comparator-role decisions

- 0556 C008 (DSM edition), 2210 C005 (high-vitamin-D operator), and 4755 C005 (SAP microgram prefix) are P_P only. Article statements corroborate an internal plan defect; their presence as citations does not make these P_R.
- 2210 C006 is S_C only. Protocol CDX2/rs11568820 establishes identity, but the substantive discrepancy is main Cdx2 versus results-supplement CDK2 labels.
- 14231 C002–C006 are S_W. Both incidences and ARDs are printed in main Table 2, and the supplement repeats agreeing incidence values. The cross-source checker calls source displays concordant; the final recheck retains the separate internal arithmetic/point-estimator concern. A no-lead conclusion about cross-file matching does not negate that final candidate.
- 14630 C001, 7505 C004, 4755 C004, 14901 C003/C004 and 2210 C001/C007 are S_W despite cross-file corroboration. Their targets are internal header/caption/arithmetic/denominator defects and the other report file agrees with the relevant comparator.
- 0556 C002, 10517 C002, 12618 C006 and 14231 C008 explicitly target both main/supplement identity and within-main definition/display differences; coded S_C with S_W relation.
- 17380 C005/C006 explicitly compare supplement Ns to exact randomized arm totals in the main article. Same-supplement eTable 6 also supplies arm/count compatibility: active measured N702/658 cannot fit reversed active randomized N609/653. Coded S_C with S_W, distinguishing expected randomized-versus-measured one-person availability differences.

The 12618 bundle cover explicitly identifies original protocol, final protocol, and summary of changes; its original and final protocols are themselves written in Manual of Operations/Procedures format. The final v4.5 page 80 image directly confirms the primary-endpoint section and injection rule. C001/C003/C004 therefore retain their protocol role based on document function and full trial-design content, with plan_document_kind protocol_in_manual_of_operations_format. This is distinct from an independently supplied ancillary procedures manual.

## Plan-file topology

All P_P-relation cards have plan_topology. Ten are within_file, including mixed 2210 C004: 0556 C006/C008/C009; 10517 C003; 12618 C001; 14901 C006; 2210 C003/C004/C005; 4755 C005. Protocol and SAP sections in one bound PDF count as one file.

7505 C003 is both: the uninterrupted odds ratio relative risks phrase is internally indeterminate inside the protocol, and the candidate also compares it with a separate final SAP PDF. This is the sole 2019 P_P candidate with a substantive comparison between separate planning files. Therefore if all physically cross-file candidates are needed, add this one to P_R + S_C: 22, of which 9/22 = 40.91% involve planning documents (8 report–plan plus 1 plan–plan). Do not add every P_P to a physical cross-document denominator.

## Evidence state, sensitivity and duplicates

No 2019 final card explicitly reports that its recorded discrepancy was not reproduced on recheck; all 71 retain evidence_state recorded_candidate. This does not establish validity.

2210 C008 is an especially weak wording-only boundary case because the article explicitly states equivalent operational time origins. Excluding just that retained candidate gives total 70, P_R 7 (10.00%), P_P 10 (14.29%), S_C 13 (18.57%), S_W 40 (57.14%); among P_R + S_C, plan share is 7/20 = 35.00%. Any-plan share becomes 17/70 = 24.29%. It is not coded not_reproduced because the card reproduces the wording difference and explicitly avoids claiming a date difference.

No clearly identical underlying issue was marked duplicate_of. Related candidates remain distinct: 14630 C002/C003 share one red-wine cell, but one tests median/IQR ordering while the other compares both arms across tables; 14231 C002–C006 concern five different outcomes; 4755 C001–C003 concern distinct test/cutoff PPV cells; 0556 C005/C006/C007 concern two internal arithmetic mechanisms and a separate plan/report assumptions comparison. Shared production causes cannot be established from the records.

## Detailed evidence consulted

Final-report paths are retained in input_2019.json and implicitly support every coded row. Each row lists the additional files consulted. Distinct additional paths:

- `2019/jama.2019.0556/.ai_paper_validation/review_1_4_1/source_inventory.md`
- `2019/jama.2019.0556/.ai_paper_validation/review_1_4_1/verification/evidence_recheck.md`
- `2019/jama.2019.10517/.ai_paper_validation/review_1_5_1/source_inventory.md`
- `2019/jama.2019.10517/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md`
- `2019/jama.2019.12618/.ai_paper_validation/review_1_5_1/candidate_ledger.md`
- `2019/jama.2019.12618/.ai_paper_validation/review_1_5_1/parts/support_protocol_pp001_032.md`
- `2019/jama.2019.12618/.ai_paper_validation/review_1_5_1/parts/support_protocol_pp065_096.md`
- `2019/jama.2019.12618/.ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck_protocol_p080.png`
- `2019/jama.2019.12618/.ai_paper_validation/review_1_5_1/preprocessing/protocol_pp001_032_layout.txt`
- `2019/jama.2019.12618/.ai_paper_validation/review_1_5_1/preprocessing/protocol_pp065_096_layout.txt`
- `2019/jama.2019.12618/.ai_paper_validation/review_1_5_1/source_inventory.md`
- `2019/jama.2019.12618/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md`
- `2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/checkers/cross_source_consistency.md`
- `2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/source_inventory.md`
- `2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md`
- `2019/jama.2019.14630/.ai_paper_validation/review_1_5_1/candidate_ledger.md`
- `2019/jama.2019.14630/.ai_paper_validation/review_1_5_1/source_inventory.md`
- `2019/jama.2019.14630/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md`
- `2019/jama.2019.14901/.ai_paper_validation/review_1_5_1/source_inventory.md`
- `2019/jama.2019.14901/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md`
- `2019/jama.2019.17380/.ai_paper_validation/review_1_5_2/source_inventory.md`
- `2019/jama.2019.17380/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md`
- `2019/jama.2019.2210/.ai_paper_validation/review_1_5_1/candidate_ledger.md`
- `2019/jama.2019.2210/.ai_paper_validation/review_1_5_1/source_inventory.md`
- `2019/jama.2019.2210/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md`
- `2019/jama.2019.4755/.ai_paper_validation/review_1_5_1/source_inventory.md`
- `2019/jama.2019.4755/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md`
- `2019/jama.2019.7505/.ai_paper_validation/review_1_5_2/source_inventory.md`
- `2019/jama.2019.7505/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md`
