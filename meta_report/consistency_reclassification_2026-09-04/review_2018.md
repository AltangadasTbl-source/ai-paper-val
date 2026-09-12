# 2018 retrospective document-role reclassification

All 119 complete candidate cards in the current final-report input were read across 10 packages. This is a reclassification of recorded candidates, not a new scientific validation or final error adjudication. All supplied candidate IDs are retained. Exact source statuses and original categories remain in input_2018.json and the root merged dataset. The output ledger is coded_2018.json; code_2018.py serializes manually assigned decisions rather than discovering or keyword-classifying candidates.

## Mutually exclusive primary counts

| Role | Candidates | Percent of 119 |
|---|---:|---:|
| P_R | 11 | 9.2% |
| P_O | 0 | 0.0% |
| P_P | 9 | 7.6% |
| P_B | 2 | 1.7% |
| S_C | 16 | 13.4% |
| S_W | 81 | 68.1% |
| OTHER | 0 | 0.0% |

P_R is reported article/results versus protocol/SAP. P_P is a planned-definition or plan-calculation discrepancy internal to supplied plan content. P_B is historical/background quantitative evidence reproduced within a protocol. S_C is main versus non-plan results supplement. S_W is within one main or non-plan supplement. P_O and OTHER have no 2018 candidates.

The 11 P_R candidates occur in 7/10 packages (70%). Their share is 11/119 = 9.2% of all recorded candidates. All protocol/SAP involvement, including 9 primary P_P and 2 P_B, is 22/119 = 18.5%, across 8/10 packages. Submission-only candidates are 97/119 = 81.5%: 16 cross-file and 81 within-file. Among submission-only candidates, 16/97 = 16.5% are cross-file and 81/97 = 83.5% within-file.

## Package reconciliation

| Package | Total | P_R | P_P | P_B | S_C | S_W |
|---|---:|---:|---:|---:|---:|---:|
| jama.2017.21906 | 6 | 2 | 0 | 0 | 1 | 3 |
| jama.2018.0156 | 8 | 2 | 0 | 0 | 1 | 5 |
| jama.2018.0948 | 7 | 1 | 4 | 2 | 0 | 0 |
| jama.2018.14280 | 23 | 1 | 0 | 0 | 1 | 21 |
| jama.2018.14282 | 28 | 0 | 3 | 0 | 1 | 24 |
| jama.2018.17075 | 8 | 0 | 0 | 0 | 2 | 6 |
| jama.2018.18020 | 14 | 0 | 0 | 0 | 0 | 14 |
| jama.2018.6496 | 4 | 2 | 0 | 0 | 0 | 2 |
| jama.2018.8802 | 8 | 1 | 0 | 0 | 1 | 6 |
| jama.2018.9128 | 13 | 2 | 2 | 0 | 9 | 0 |

## Inclusive relationships and overlap

| Relationship present | Candidates |
|---|---:|
| P_R | 11 |
| P_O | 0 |
| P_P | 11 |
| P_B | 2 |
| S_C | 18 |
| S_W | 94 |
| OTHER | 0 |

These inclusive counts overlap and must not be added as a candidate total. P_R and P_P overlap for jama.2018.9128 C011-C012. P_R and S_C overlap for jama.2018.0948 C001 and jama.2018.8802 C002. The latter also has S_W. Other S_C/S_W mixed cards are jama.2017.21906 C005, jama.2018.17075 C003-C004, and all nine BMI-count cards in jama.2018.9128. Every P_P relationship is within a single bound protocol/SAP PDF; no 2018 P_P relationship requires different physical plan files.

## Boundary decisions requiring detailed records

- jama.2018.0948 C001 compares main >=60 mL/kg with both protocol and results-supplement >60: P_R+S_C. C002 is a protocol-internal 0.9% versus 0.09%/0.9-per-1000 unit error, corroborated by the article; P_P only. C004 is protocol >4 immediately followed by an inclusive 4/5/6 list, corroborated by final reporting; P_P only.
- jama.2018.0948 C005 and C007 concern historical Ontario 2007-8 reference data (Kotsakis 2009) copied into the protocol Sample Size Appendix. C005 disputes annual versus two-year labels for the same historical 1052 count; C007 disputes historical rates from historical counts. Both are P_B. C006 instead tests the prospective power-planning reduction 8.13 x .181 versus 1.45 and remains P_P.
- jama.2018.0156 C003-C004 are within-main arithmetic/CI issues; the SAP supplies general conventions, not a discordant plan target. C007-C008 genuinely compare amended endpoint definitions with reported article descriptions. C008 is expressly conditional on undefined population/endpoint alignment.
- jama.2018.14280 C011 is main Methods HR wording versus main Table 2 RR labels, with SAP corroboration: S_W. C023 is a main-versus-SAP two-day enrollment-date mismatch: P_R, but it need not represent a prospective protocol violation; administrative closure may differ from last enrollment.
- jama.2018.14282 C025 is 779 versus 389+389 within the article, with protocol/SAP 778 as corroboration: S_W. C026-C028 are internal to the bound protocol/SAP, including a noninferiority sign, NIV/HFNO intervention label, and day-28/hospital-death endpoint label.
- jama.2018.18020 C005-C007 are Bayesian code/dictionary inconsistencies in the quantitative results supplement, not the separate trial protocol: S_W. C008 is a main CLNC1/CLCN1 typo with same-main comparator; the results-supplement gene definition is corroboration, so S_W. C004 is an internal adverse-event eTable denominator issue, conditional on 30 patients versus 31 treatment-set exposures.
- jama.2018.6496 C001 is main CI endpoint order; physician-clustered supplementary inference is explicitly different and not counted as a cross-file inconsistency. C002 is within-main linked outcome denominators 366/364; protocol definitions may explain that difference. C003-C004 genuinely compare planned cuff-inflation timing endpoints with reported blade-removal endpoints. The data form supports the reported operational definition and is not an additional P_O relationship.
- jama.2018.8802 C002 expressly targets formal planned eligibility versus reported LDL labels, with substantive ordinary-supplement definition/label inconsistency too: P_R+S_C+S_W. C007 is main 801 versus ordinary eAppendix 20x40=800; protocol 40-cluster context does not create another P_R.
- jama.2018.9128 C009-C010 are plan list/count contradictions, with final-report schedules as context: P_P. C011 compares original planned BMI percentile/BMI% with final SAP and reported raw BMI, also conflicting with the original raw formula: P_R+P_P. C012 compares 12x60, 7x45, and 6x30 control exposure across original/revised plans and article: P_R+P_P; amendment/component mapping remains unresolved.

## Evidence-state limitations and candidate granularity

No 2018 final card explicitly reports complete failure to reproduce its candidate discrepancy on recheck; 118 rows use evidence_state=recorded_candidate and one uses record_input_error as detailed below. However jama.2018.14282 C018 is expressly a communication-only concern: the paragraph says overall population and both percentages reproduce using 776. It must not be called a confirmed arithmetic inconsistency. C023-C024 in that package overstate exact reciprocity in earlier records; the final cards and recheck retain only near-reciprocal orientation under unknown reference definitions. These are not equivalent to a wholly un-reproduced record.

No clearly identical underlying candidate IDs were marked duplicate_of. Separate rows/arms/visits remain separate source candidates: jama.2018.14280 has ten distinct RR-versus-risk rows; jama.2018.14282 has many last-decimal count/percentage cells and complementary C020-C021; jama.2018.17075 C003-C004 may share a two-row transposition mechanism but target different bleeding outcomes; jama.2018.9128 has nine arm/visit BMI count mismatches. Therefore candidate proportions are sensitive to source workflow granularity and are not proportions of papers with independently proven errors.

An additional retrospective check found an input-label error in jama.2018.0156 C008: both the final card and mechanical recheck call 54/1022 ETI deaths, whereas the current-run main-article native text labels it day-28 survival (abstract and Table 2). Consequently the recorded 27-versus-21 mortality bound is not source-confirmed. P_R is retained for the stated amended-composite versus reported-failure-definition comparison; no new endpoint adjudication or numeric correction is imposed. The row carries evidence_state=record_input_error and validation_record_issue=survival_count_mislabeled_as_deaths, plus its exact native-text evidence path. Exact source-derivative wording: `global survival at day 28 (55/1018 [5.4%] in the BMV group vs 54/1022 [5.3%] in the ETI group)`. A stronger sensitivity excluding this single record gives P_R 10/118 = 8.5%, and package-level P_R remains 7/10 because C007 in the same package remains. This differs from an explicit final-card statement that the entire discrepancy failed recheck.

## Original-category migration

| Original category | Total | P_R | P_P | P_B | S_C | S_W |
|---|---:|---:|---:|---:|---:|---:|
| Cross-document numeric inconsistency | 19 | 4 | 1 | 0 | 11 | 3 |
| Denominator, proportion, or total inconsistency | 41 | 0 | 1 | 2 | 0 | 38 |
| Measure, label, or scale inconsistency | 26 | 7 | 4 | 0 | 2 | 13 |
| Numeric or arithmetic inconsistency | 7 | 0 | 2 | 0 | 0 | 5 |
| Statistical reporting inconsistency | 26 | 0 | 1 | 0 | 3 | 22 |

## Deeper evidence consulted

Every row cites its package source inventory; document roles were read for all ten packages. Candidate-specific deeper consultation is recorded in evidence_paths. Across this year, the consulted evidence paths are:

- `2018/jama.2017.21906/.ai_paper_validation/review_1_5_2/source_inventory.md`
- `2018/jama.2017.21906/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md`
- `2018/jama.2018.0156/.ai_paper_validation/review_1_5_2/source_inventory.md`
- `2018/jama.2018.0156/.ai_paper_validation/review_1_5_2/preprocessing/native_text/jama_jabre_2018_oi_180004.txt`
- `2018/jama.2018.0156/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md`
- `2018/jama.2018.0948/.ai_paper_validation/review_1_5_2/candidate_ledger.md`
- `2018/jama.2018.0948/.ai_paper_validation/review_1_5_2/preprocessing/native_text/joi180015supp1_prod.txt`
- `2018/jama.2018.0948/.ai_paper_validation/review_1_5_2/source_inventory.md`
- `2018/jama.2018.0948/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md`
- `2018/jama.2018.14280/.ai_paper_validation/review_1_5_2/source_inventory.md`
- `2018/jama.2018.14280/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md`
- `2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/candidate_ledger.md`
- `2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/source_inventory.md`
- `2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md`
- `2018/jama.2018.17075/.ai_paper_validation/review_1_5_2/source_inventory.md`
- `2018/jama.2018.17075/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md`
- `2018/jama.2018.18020/.ai_paper_validation/review_1_5_2/source_inventory.md`
- `2018/jama.2018.18020/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md`
- `2018/jama.2018.6496/.ai_paper_validation/review_1_5_2/source_inventory.md`
- `2018/jama.2018.6496/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md`
- `2018/jama.2018.8802/.ai_paper_validation/review_1_5_2/source_inventory.md`
- `2018/jama.2018.8802/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md`
- `2018/jama.2018.9128/.ai_paper_validation/review_1_5_2/source_inventory.md`
- `2018/jama.2018.9128/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md`

## Deterministic completeness checks

- 119 output rows, 119 distinct keys, and exact key equality with input_2018.json.
- Primary counts sum to 119; relation arrays begin with the primary role; every consulted evidence path exists.
- Zero source candidate IDs deleted, split, merged, or renumbered; zero source scientific package files modified.
- No web search or outside scientific source used. Historical source roles were inspected from current-run native extraction already provided in the packages.
