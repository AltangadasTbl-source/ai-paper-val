# 2024 retrospective document-role reclassification

All 91 full candidate cards from all 10 packages were read. The selected cards are from the current `final_report_1_5_3.md` files supplied in `input_2024.json`. This review reused existing detailed verification/checker records to classify the relationships they recorded; it did not perform a new scientific validation or adjudicate candidate validity. One JSON row per original key is in `coded_2024.json`, with concrete rationale, all substantive relationship tags, ambiguity, and exact deeper evidence paths. Source files were not changed.

## Mutually exclusive primary counts

| Primary relationship | Candidates | Of 91 |
|---|---:|---:|
| Report versus protocol/SAP, P_R | 11 | 12.1% |
| Within/between plan documents, P_P | 6 | 6.6% |
| Main versus non-plan supplement, S_C | 18 | 19.8% |
| Within one article/non-plan supplement, S_W | 56 | 61.5% |
| P_O / P_B / OTHER | 0 | 0.0% |
| Total | 91 | 100.0% |

There are 17 candidates involving plan documents (18.7% of all candidates), across 5/10 papers. Only 11 of them compare the reported article/results supplement to a plan, across 4/10 papers. The other 6 are plan-only. Thus 11/17 = 64.7% of plan-involved candidates are report-plan comparisons, and 6/17 = 35.3% are plan-only.

The report-to-plan or report-to-other-report cross-file union is 29 candidates. Under mutually exclusive primary precedence, 11/29 = 37.9% are assigned P_R and 18/29 = 62.1% are assigned S_C. Inclusive relationship tags are P_R 11, P_P 9, S_C 22, S_W 65. These totals overlap: four P_R candidates also have an S_C relationship, and three have a P_P relationship. A candidate can have multiple substantive relationships but still contributes one to the 91 denominator. In particular, the inclusive S_C share is 22/91 = 24.2%, while 74/91 = 81.3% have a submission-only primary assignment (S_C or S_W). Any submission-internal relationship, including mixed plan/report cards, occurs in 79/91 = 86.8%.

## Counts per paper

| Package | Total | P_R | P_P | S_C | S_W |
|---|---:|---:|---:|---:|---:|
| jama.2024.0318 | 6 | 0 | 0 | 2 | 4 |
| jama.2024.0572 | 2 | 0 | 0 | 1 | 1 |
| jama.2024.11057 | 3 | 1 | 0 | 0 | 2 |
| jama.2024.12829 | 17 | 1 | 2 | 1 | 13 |
| jama.2024.19585 | 3 | 0 | 0 | 1 | 2 |
| jama.2024.2302 | 5 | 4 | 1 | 0 | 0 |
| jama.2024.23898 | 7 | 5 | 0 | 0 | 2 |
| jama.2024.25786 | 8 | 0 | 0 | 3 | 5 |
| jama.2024.4183 | 24 | 0 | 3 | 5 | 16 |
| jama.2024.6063 | 16 | 0 | 0 | 5 | 11 |
| Total | 91 | 11 | 6 | 18 | 56 |

## Where the 11 report-plan candidates occur

| Package / ID | Target comparison | Qualification |
|---|---|---|
| 11057 C001 | Article 6 pre-quit message weeks versus protocol and results supplement 1 week | P_R + S_C. Protocol and article have contextual dates in 2021 and 2024; an intervention-version change is possible but not established. |
| 12829 C009 | Results study-design graphic 30 ± 3 days versus article/protocol 30 ± 7 days | P_R + S_C. No supplied distinction between operational contact and assessment window. |
| 2302 C001 | Main/SAP ≥1 SAE versus protocol/results eTable >1 | P_R + P_P + S_C. Identical reported counts do not establish implemented threshold. |
| 2302 C003 | Article common prior range 0.33–3.0 versus SAP outcome-class-specific ranges | P_R. Final model code/amendment missing. |
| 2302 C004 | Actual ≥28-week group versus SAP >28 wording | P_R + P_P. The SAP also uses ≥28; final gestational-age coding unknown. |
| 2302 C005 | Report/SAP SAE clock from randomization versus protocol from enrollment | P_R + P_P. The protocol itself mixes terms; operational simultaneity is unresolved. |
| 23898 C001 | Article 72 hours after surgery versus SAP 72 hours after operation start | P_R. Ambiguity in time-zero specificity, not a demonstrated different derivation. |
| 23898 C002 | Reported 24-hour opioids versus planned 72-hour opioids | P_R. A distinct final measure or changed window is possible. |
| 23898 C003 | Table 3 90-day readmission versus main Methods/protocol/SAP 30-day definition | P_R + S_W. Both report-plan endpoint mapping and internal Methods/table window differ. |
| 23898 C004 | Reported ERAS low <5/10 versus protocol example 0–30% / 30–60% / >60% bands | P_R. Protocol says “e.g.”; eFigure says categories were not predefined. Do not call this an undisclosed violation. |
| 23898 C007 | Article ERAS “high vs low” versus SAP/eFigure high/moderate/low | P_R + S_C. Shorthand or a separate extreme-group contrast remains possible. |

The 6 plan-only candidates are 12829 C010 (same V2.0 eligibility 21–90 versus 14–90 days), 12829 C013 (ambiguous repeated visit-number sentence inside a protocol bundle), 2302 C002 (planning medians 18/15 versus 8/5), and 4183 C010/C011/C012 (beta parameter identity, power monotonicity, and contrast label within protocol). **2302 C002 is explicitly corrected in the SAP**, which identifies 8/5 as intended and calls 18/15 incorrect; it is a disclosed plan correction, not a mismatch with observed data. The bundled protocol versions in 12829 C013 contain the same repeated sentence; these are not article-versus-protocol discrepancies.

## Why the original categories cannot answer the question directly

| Original category | P_R | P_P | S_C | S_W | Total |
|---|---:|---:|---:|---:|---:|
| Cross-document numeric inconsistency | 4 | 1 | 10 | 2 | 17 |
| Measure, label, or scale inconsistency | 6 | 3 | 4 | 13 | 26 |
| Statistical reporting inconsistency | 1 | 2 | 4 | 11 | 18 |
| Denominator, proportion, or total inconsistency | 0 | 0 | 0 | 25 | 25 |
| Analysis-unit or population inconsistency | 0 | 0 | 0 | 2 | 2 |
| Numeric or arithmetic inconsistency | 0 | 0 | 0 | 3 | 3 |
| Total | 11 | 6 | 18 | 56 | 91 |

Only 4/11 (36.4%) of the recoded report-plan candidates originally carried the cross-document label; 7/11 (63.6%) were hidden in measure/label or statistical categories. Conversely, two original cross-document candidates are internal to one PDF: 12829 C015 compares main narrative with main Figure 1, and 25786 C003 compares two eTables inside the same results supplement. An additional original cross-document candidate (2302 C002) compares only planning values.

## Corroboration and scope boundaries

- 0572 C002 is S_W: the main table itself calls aRR both “absolute risk reduction” and a ratio interpreted around 1. SAP modified-Poisson/relative-risk statements corroborate that scale reading; this is not counted as a separate plan deviation.
- 23898 C005 is S_W: 99% legend versus 95% caption within one eFigure. SAP 99% convention merely supports the legend. C006 is likewise S_W: day-5 P=.04/CI excluding zero versus no-significant-difference prose in the article; SAP supplies the nominal framework.
- 0318 C002 is S_W: year-12 heading versus year-7 footnotes within an eTable; the article pointer corroborates the heading. 0318 C004's supplemental GEE context does not even specify the disputed HbA1c operator.
- 11057 C002 compares the same eTable's IQR convention; main baseline Table 1 is a corroborative formatting comparator with different groupings. C003's IPWR/IPRW mismatch is demonstrated by the same supplement's explicit method definition and matched result; main methods corroborate the definition.
- 12829 C006 is S_W: Table S8 headers/percentages disagree with PPS totals in Table S10 of the same supplement; main Figure 1 corroborates those totals. “Per-protocol” is an analysis-set name and does not mean the comparator is a protocol document. C008 compares main eligibility and main baseline distribution; mentioning possible protocol deviations does not introduce a protocol-document comparison.
- 25786 C007 is S_W: within-group cell denominators accompany cross-group share percentages. Figure 1 agrees with the counts. The separate two-person total gap is explained by the table footnote and is not counted as another inconsistency.
- Cross-reference errors between the main article and a non-plan supplement (6063 C014/C015) are S_C; analogous cross-reference errors wholly inside a supplement (4183 C019/C021/C022) are S_W.
- 6063 C012/C013, 4183 C005/C006/C007, and 25786 C004/C005/C006 explicitly compare mismatched repeated report displays and also contain substantive within-file relationships, so both S_C and S_W are retained. C005 in 4183 is conditional on the scope of an abstract parenthetical; it is not an unconditionally established mismatch.

## Negated old discrepancy and duplicate review

19585 C001 explicitly states the old 71-versus-58 arithmetic mismatch is not carried forward. The verifier finds 7+4+2=13 nested under a parent, and top-level reasons sum to 58. This row retains primary S_W to identify the historical relationship but has `evidence_state = not_reproduced`. Excluding that explicitly negated case gives 90 records: P_R 11 (12.2%), P_P 6 (6.7%), S_C 18 (20.0%), S_W 55 (61.1%). Plan involvement is then 17/90 (18.9%). No other 2024 card explicitly negates the targeted relationship after recheck. This sensitivity exclusion is evidence bookkeeping, not final human validity adjudication.

No clearly identical duplicate candidate IDs were found. Related but distinct pairs/sets remain separate: 12829 C004/C016 (percentage identity versus cross-file event count), C007/C014 (ATS headers versus a cell that still fails under ATS denominator); 6063 C002/C016 (supplement denominator versus main adherence percentage); 4183 C005/C006 (different rescue contrasts, with C005 scope ambiguity), C014/C016 (arm response versus between-arm ARD), C015/C017 (different treatment arms), and C023/C024 (value order versus missing counts). The six 6063 C003–C008 candidates concern six different percentage cells. Such granularity affects the result count; 91 candidate records should not be read as 91 independent underlying production events.

## Detailed records consulted

All ten package source inventories were read. Targeted verifier sections and checker records below were consulted beyond every complete final-report card. Per-candidate paths appear in the JSON.

- `2024/jama.2024.0318/.ai_paper_validation/review_1_5_3/source_inventory.md`
- `2024/jama.2024.0318/.ai_paper_validation/review_1_5_3/verification/evidence_recheck.md`
- `2024/jama.2024.0572/.ai_paper_validation/review_1_5_3/source_inventory.md`
- `2024/jama.2024.0572/.ai_paper_validation/review_1_5_3/verification/evidence_recheck.md`
- `2024/jama.2024.11057/.ai_paper_validation/review_1_5_3/source_inventory.md`
- `2024/jama.2024.11057/.ai_paper_validation/review_1_5_3/verification/evidence_recheck.md`
- `2024/jama.2024.11057/.ai_paper_validation/review_1_5_3/verification/evidence_recheck_C003.md`
- `2024/jama.2024.12829/.ai_paper_validation/review_1_5_3/source_inventory.md`
- `2024/jama.2024.12829/.ai_paper_validation/review_1_5_3/verification/evidence_recheck.md`
- `2024/jama.2024.19585/.ai_paper_validation/review_1_5_3/source_inventory.md`
- `2024/jama.2024.19585/.ai_paper_validation/review_1_5_3/verification/evidence_recheck.md`
- `2024/jama.2024.2302/.ai_paper_validation/review_1_5_3/source_inventory.md`
- `2024/jama.2024.2302/.ai_paper_validation/review_1_5_3/verification/evidence_recheck.md`
- `2024/jama.2024.23898/.ai_paper_validation/review_1_5_3/checkers/cross_source_consistency.md`
- `2024/jama.2024.23898/.ai_paper_validation/review_1_5_3/checkers/statistical_pass_2.md`
- `2024/jama.2024.23898/.ai_paper_validation/review_1_5_3/source_inventory.md`
- `2024/jama.2024.25786/.ai_paper_validation/review_1_5_3/source_inventory.md`
- `2024/jama.2024.25786/.ai_paper_validation/review_1_5_3/verification/evidence_recheck.md`
- `2024/jama.2024.4183/.ai_paper_validation/review_1_5_3/source_inventory.md`
- `2024/jama.2024.4183/.ai_paper_validation/review_1_5_3/verification/evidence_recheck.md`
- `2024/jama.2024.6063/.ai_paper_validation/review_1_5_3/source_inventory.md`
- `2024/jama.2024.6063/.ai_paper_validation/review_1_5_3/verification/evidence_recheck.md`

## Plan-document topology

Within one bound plan file: 12829 C010/C013, 2302 C004, 4183 C010/C011/C012. Between distinct protocol and SAP files: 2302 C001. Both within protocol and between protocol/SAP: 2302 C002/C005. The two historical protocol versions for 12829 C013 are inside one physical PDF. `plan_topology` is recorded for all nine rows carrying P_P.
