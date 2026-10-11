# Candidate ledger

All entries are **Pending Human Adjudication**. Stable IDs preserve distinct printed values, comparators, and consistency rules; no severity, validity, disposition, or correction is assigned.

## Merge crosswalk

| Provisional checker record | Retained ledger entry | Basis |
|---|---|---|
| Statistical P1-027; cross-source observation C | C036 | Same narrative value, Table 3 value, PT-versus-UC comparator, 3-month pain-severity SMD, and matched-result rule. |
| Statistical P1-028; cross-source observation D | C037 | Same narrative value, Table 3 value, HC-versus-UC comparator, 3-month pain-severity SMD, and matched-result rule. |

## C001 — Conditional Figure 1 further-ineligibility component subtotal gap

**Status:** Pending Human Adjudication  
**Category:** Numeric or arithmetic inconsistency  
**Checker provenance:** numeric CANDIDATE_NUM-01.  
**Exact source locations:** [main article — PDF p. 5](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=5), Figure 1, “4481 Ineligible.”  
**Printed values:** Further-reason subtotal `1243`; listed counts `411, 273, 189, 121, 95, 34`.  
**Comparison/rule/calculation:** If the displayed six reasons exhaust the “one or more of” subtotal, their sum must be at least its union: `411+273+189+121+95+34=1123`, 120 below 1243.  
**Direct observation vs diagnostic reasoning:** Printed counts and gap are direct; exhaustiveness of the listed reasons is the diagnostic assumption.  
**Source-grounded alternatives:** One or more further reasons may be omitted, or a count/subtotal may be wrong; overlap cannot make a component sum below the union.  
**Missing definition/human question:** Does the figure intend the six reasons to exhaust 1243, and which value should reconcile?  
**Bounded downstream relevance:** A screening-reason denominator could be copied into trial-flow extraction.

## C002 — Overall eTable 1 follow-up-pattern partition

**Status:** Pending Human Adjudication  
**Category:** Denominator, proportion, or total inconsistency  
**Checker provenance:** numeric CANDIDATE_NUM-02.  
**Exact source locations:** [results supplement — PDF p. 7](../../joi250046supp4_prod_1755300121.15587.pdf#page=7), eTable 1, Overall column.  
**Printed values:** At least one follow-up `2036`; one/two/three observed follow-ups `188/283/1568`.  
**Comparison/rule/calculation:** Mutually exclusive follow-up patterns should partition the total: `188+283+1568=2039`, not 2036 (difference 3; integer tolerance 0).  
**Direct observation vs diagnostic reasoning:** Values and labels are direct; partition identity follows their one/two/three labels.  
**Source-grounded alternatives:** A pattern row, total, or source-data definition differs; no alternate denominator is printed.  
**Missing definition/human question:** Which printed Overall value defines the intended partition?  
**Bounded downstream relevance:** Follow-up-pattern totals may be reused for missing-data assessment.

## C003 — painTRAINER eTable 1 follow-up-pattern partition

**Status:** Pending Human Adjudication  
**Category:** Denominator, proportion, or total inconsistency  
**Checker provenance:** numeric CANDIDATE_NUM-03.  
**Exact source locations:** [results supplement — PDF p. 7](../../joi250046supp4_prod_1755300121.15587.pdf#page=7), eTable 1, painTRAINER column.  
**Printed values:** At least one follow-up `643`; one/two/three `77/103/464`.  
**Comparison/rule/calculation:** `77+103+464=644`, one above 643 (integer tolerance 0).  
**Direct observation vs diagnostic reasoning:** Values are direct; partition rule follows row labels.  
**Source-grounded alternatives:** One pattern count or arm total may be discrepant; no alternate denominator is printed.  
**Missing definition/human question:** Is 643 or the 644 pattern sum authoritative?  
**Bounded downstream relevance:** Arm-level follow-up distribution may be copied into missingness analyses.

## C004 — Health Coach eTable 1 follow-up-pattern partition

**Status:** Pending Human Adjudication  
**Category:** Denominator, proportion, or total inconsistency  
**Checker provenance:** numeric CANDIDATE_NUM-04.  
**Exact source locations:** [results supplement — PDF p. 7](../../joi250046supp4_prod_1755300121.15587.pdf#page=7), eTable 1, Health Coach column.  
**Printed values:** At least one follow-up `690`; one/two/three `47/81/564`.  
**Comparison/rule/calculation:** `47+81+564=692`, two above 690 (integer tolerance 0).  
**Direct observation vs diagnostic reasoning:** Values are direct; partition rule follows row labels.  
**Source-grounded alternatives:** A pattern count or arm total may be discrepant; no alternative denominator is shown.  
**Missing definition/human question:** Is 690 or the 692 pattern sum authoritative?  
**Bounded downstream relevance:** Differential-follow-up quantities may be reused in evidence extraction.

## C005 — Workbook current-depression percentage incompatible with its count

**Status:** Pending Human Adjudication  
**Category:** Denominator, proportion, or total inconsistency  
**Checker provenance:** numeric CANDIDATE_NUM-05.  
**Exact source locations:** [workbook](../../joi250046supp5_prod_1755300121.16087.xlsx), `eTable 3` A82:E83 and E2:E3.  
**Printed values:** All Observed N `1568`, missing `2`, current depression `711 (73.2)`.  
**Comparison/rule/calculation:** Missing-excluded denominator is `1566`; `711/1566=45.4%`, not 73.2% (and `711/1568=45.3%`).  
**Direct observation vs diagnostic reasoning:** Cells are direct; percentage calculation is deterministic.  
**Source-grounded alternatives:** The count may be right with a mistyped percentage, or percentage/denominator may belong elsewhere; `162+243+711=1116` supports the count.  
**Missing definition/human question:** Should E82 be `711 (45.4%)`, or does a different unprinted denominator apply?  
**Bounded downstream relevance:** This baseline prevalence/predictor could be copied in missingness reporting.

## C006 — Workbook social-role cutoff labeled as mean (SD)

**Status:** Pending Human Adjudication  
**Category:** Measure, label, or scale inconsistency  
**Checker provenance:** numeric CANDIDATE_NUM-06.  
**Exact source locations:** [workbook](../../joi250046supp5_prod_1755300121.16087.xlsx), `eTable 3` A103:E104.  
**Printed values:** Label `PROMIS Social role functioning <=40, mean (sd)`; values `818 (35.7)|113 (38.8)|180 (38.7)|525 (34.2)`.  
**Comparison/rule/calculation:** Entries are count/percentages: `525/(1568-31)=34.2%`; they are not mean/SD values.  
**Direct observation vs diagnostic reasoning:** Label/cells are direct; N(%) interpretation follows calculation and table convention.  
**Source-grounded alternatives:** `mean (sd)` may be a template carryover; intended label may be `N (%)`.  
**Missing definition/human question:** Should the cutoff row be relabeled `N (%)`?  
**Bounded downstream relevance:** Incorrect scale labeling can lead to incorrect categorical-measure extraction.

## C007 — Workbook physical-function cutoff labeled as mean (SD)

**Status:** Pending Human Adjudication  
**Category:** Measure, label, or scale inconsistency  
**Checker provenance:** numeric CANDIDATE_NUM-07.  
**Exact source locations:** [workbook](../../joi250046supp5_prod_1755300121.16087.xlsx), `eTable 3` A106:E107.  
**Printed values:** Label `PROMIS Physical functioning <=40, mean (sd)`; values `1709 (74.1)|209 (72.6)|357 (76.8)|1143 (73.6)`.  
**Comparison/rule/calculation:** `1143/(1568-14)=73.6%`; displayed cells are N(%), not mean(SD).  
**Direct observation vs diagnostic reasoning:** Label/cells are direct; interpretation follows reproduced proportion.  
**Source-grounded alternatives:** Formatting/template carryover may explain the label.  
**Missing definition/human question:** Should the cutoff row be relabeled `N (%)`?  
**Bounded downstream relevance:** A functional-limitation measure could be categorized incorrectly downstream.

## C008 — Pain-severity 12-month painTRAINER SMD outside printed CI

**Status:** Pending Human Adjudication  
**Category:** Statistical reporting inconsistency  
**Checker provenance:** statistical P1-001 (S013).  
**Exact source locations:** [main article — PDF p. 10](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, pain severity 12 months, painTRAINER vs usual care plus SMD.  
**Printed values:** `-0.25 (-0.24 to 0.01)`.  
**Comparison/rule/calculation:** Point estimate must lie within its interval; `-0.25 < -0.24`.  
**Direct observation vs diagnostic reasoning:** Printed estimate/CI and containment failure are direct mechanical facts.  
**Source-grounded alternatives:** Estimate or CI endpoint may be transcribed incorrectly.  
**Missing definition/human question:** What estimate and CI does the analysis output support?  
**Bounded downstream relevance:** An SMD/CI may be extracted for synthesis.

## C009 — Pain-severity 12-month Health Coach SMD outside printed CI

**Status:** Pending Human Adjudication  
**Category:** Statistical reporting inconsistency  
**Checker provenance:** statistical P1-002 (S013).  
**Exact source locations:** [main article — PDF p. 10](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, pain severity 12 months, Health Coach vs usual care plus SMD.  
**Printed values:** `-0.36 (-0.35 to -0.12)`.  
**Comparison/rule/calculation:** `-0.36 < -0.35`, so estimate is outside CI.  
**Direct observation vs diagnostic reasoning:** Direct printed containment check.  
**Source-grounded alternatives:** Point estimate or CI endpoint may be erroneous.  
**Missing definition/human question:** What matched CI is intended?  
**Bounded downstream relevance:** An SMD/CI may be copied into evidence synthesis.

## C010 — Pain-intensity 12-month Health Coach SMD outside printed CI

**Status:** Pending Human Adjudication  
**Category:** Statistical reporting inconsistency  
**Checker provenance:** statistical P1-003 (S016).  
**Exact source locations:** [main article — PDF p. 10](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, pain intensity 12 months, Health Coach vs usual care plus SMD.  
**Printed values:** `-0.27 (-0.26 to -0.12)`.  
**Comparison/rule/calculation:** `-0.27 < -0.26`, outside CI.  
**Direct observation vs diagnostic reasoning:** Direct printed containment check.  
**Source-grounded alternatives:** Estimate or CI endpoint may differ from intended output.  
**Missing definition/human question:** What matched CI is intended?  
**Bounded downstream relevance:** An SMD/CI may be copied into evidence synthesis.

## C011 — Pain-interference 12-month painTRAINER SMD outside printed CI

**Status:** Pending Human Adjudication  
**Category:** Statistical reporting inconsistency  
**Checker provenance:** statistical P1-004 (S019).  
**Exact source locations:** [main article — PDF p. 10](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, interference 12 months, painTRAINER vs usual care plus SMD.  
**Printed values:** `-0.26 (-0.25 to 0.01)`.  
**Comparison/rule/calculation:** `-0.26 < -0.25`, outside CI.  
**Direct observation vs diagnostic reasoning:** Direct printed containment check.  
**Source-grounded alternatives:** Estimate or endpoint may be incorrect.  
**Missing definition/human question:** What matched CI is intended?  
**Bounded downstream relevance:** An SMD/CI may be copied into evidence synthesis.

## C012 — Pain-interference 12-month Health Coach SMD outside printed CI

**Status:** Pending Human Adjudication  
**Category:** Statistical reporting inconsistency  
**Checker provenance:** statistical P1-005 (S019).  
**Exact source locations:** [main article — PDF p. 10](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, interference 12 months, Health Coach vs usual care plus SMD.  
**Printed values:** `-0.37 (-0.36 to -0.11)`.  
**Comparison/rule/calculation:** `-0.37 < -0.36`, outside CI.  
**Direct observation vs diagnostic reasoning:** Direct printed containment check.  
**Source-grounded alternatives:** Estimate or endpoint may be incorrect.  
**Missing definition/human question:** What matched CI is intended?  
**Bounded downstream relevance:** An SMD/CI may be copied into evidence synthesis.

## C013 — Social-role 3-month painTRAINER SMD endpoints reversed

**Status:** Pending Human Adjudication  
**Category:** Statistical reporting inconsistency  
**Checker provenance:** statistical P1-006 (S020).  
**Exact source locations:** [main article — PDF p. 10](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, social role, 3 months, painTRAINER vs usual care plus SMD.  
**Printed values:** `0.12 (0.23 to 0.11)`.  
**Comparison/rule/calculation:** Interval endpoints must be low-to-high; `0.23 > 0.11`.  
**Direct observation vs diagnostic reasoning:** Values/order failure are direct.  
**Source-grounded alternatives:** Signs, endpoint order, or transcription may be wrong.  
**Missing definition/human question:** What ordered CI is intended?  
**Bounded downstream relevance:** An SMD interval could be copied into synthesis.

## C014 — Social-role 3-month Health Coach SMD endpoints reversed

**Status:** Pending Human Adjudication  
**Category:** Statistical reporting inconsistency  
**Checker provenance:** statistical P1-007 (S020).  
**Exact source locations:** [main article — PDF p. 10](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, social role, 3 months, Health Coach vs usual care plus SMD.  
**Printed values:** `0.01 (0.12 to -0.00)`.  
**Comparison/rule/calculation:** `0.12 > -0.00`; endpoints are reversed.  
**Direct observation vs diagnostic reasoning:** Direct printed ordering check.  
**Source-grounded alternatives:** Signs/order may be erroneous.  
**Missing definition/human question:** What ordered CI is intended?  
**Bounded downstream relevance:** An SMD interval could be copied into synthesis.

## C015 — Social-role 3-month Health Coach versus painTRAINER SMD endpoints reversed

**Status:** Pending Human Adjudication  
**Category:** Statistical reporting inconsistency  
**Checker provenance:** statistical P1-008 (S020).  
**Exact source locations:** [main article — PDF p. 10](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, social role, 3 months, Health Coach vs painTRAINER SMD.  
**Printed values:** `0.20 (0.29 to 0.19)`.  
**Comparison/rule/calculation:** `0.29 > 0.19`; endpoints are reversed.  
**Direct observation vs diagnostic reasoning:** Direct ordering check.  
**Source-grounded alternatives:** Endpoint order/signs may be incorrect.  
**Missing definition/human question:** What ordered CI is intended?  
**Bounded downstream relevance:** An SMD interval could be copied into synthesis.

## C016 — Social-role 6-month painTRAINER SMD endpoints reversed

**Status:** Pending Human Adjudication  
**Category:** Statistical reporting inconsistency  
**Checker provenance:** statistical P1-009 (S021).  
**Exact source locations:** [main article — PDF p. 10](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, social role, 6 months, painTRAINER vs usual care plus SMD.  
**Printed values:** `0.18 (0.23 to 0.05)`.  
**Comparison/rule/calculation:** `0.23 > 0.05`; endpoints are reversed.  
**Direct observation vs diagnostic reasoning:** Direct ordering check.  
**Source-grounded alternatives:** Endpoint order/signs may be incorrect.  
**Missing definition/human question:** What ordered CI is intended?  
**Bounded downstream relevance:** An SMD interval could be copied into synthesis.

## C017 — Social-role 6-month Health Coach SMD endpoints reversed

**Status:** Pending Human Adjudication  
**Category:** Statistical reporting inconsistency  
**Checker provenance:** statistical P1-010 (S021).  
**Exact source locations:** [main article — PDF p. 10](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, social role, 6 months, Health Coach vs usual care plus SMD.  
**Printed values:** `0.06 (0.11 to -0.06)`.  
**Comparison/rule/calculation:** `0.11 > -0.06`; endpoints are reversed.  
**Direct observation vs diagnostic reasoning:** Direct ordering check.  
**Source-grounded alternatives:** Endpoint order/signs may be incorrect.  
**Missing definition/human question:** What ordered CI is intended?  
**Bounded downstream relevance:** An SMD interval could be copied into synthesis.

## C018 — Social-role 6-month Health Coach versus painTRAINER SMD endpoints reversed

**Status:** Pending Human Adjudication  
**Category:** Statistical reporting inconsistency  
**Checker provenance:** statistical P1-011 (S021).  
**Exact source locations:** [main article — PDF p. 10](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, social role, 6 months, Health Coach vs painTRAINER SMD.  
**Printed values:** `0.26 (0.30 to 0.15)`.  
**Comparison/rule/calculation:** `0.30 > 0.15`; endpoints are reversed.  
**Direct observation vs diagnostic reasoning:** Direct ordering check.  
**Source-grounded alternatives:** Endpoint order/signs may be incorrect.  
**Missing definition/human question:** What ordered CI is intended?  
**Bounded downstream relevance:** An SMD interval could be copied into synthesis.

## C019 — Social-role 12-month painTRAINER SMD endpoints reversed

**Status:** Pending Human Adjudication  
**Category:** Statistical reporting inconsistency  
**Checker provenance:** statistical P1-012 (S022).  
**Exact source locations:** [main article — PDF p. 10](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, social role, 12 months, painTRAINER vs usual care plus SMD.  
**Printed values:** `0.19 (0.21 to 0.01)`.  
**Comparison/rule/calculation:** `0.21 > 0.01`; endpoints are reversed.  
**Direct observation vs diagnostic reasoning:** Direct ordering check.  
**Source-grounded alternatives:** Endpoint order/signs may be incorrect.  
**Missing definition/human question:** What ordered CI is intended?  
**Bounded downstream relevance:** An SMD interval could be copied into synthesis.

## C020 — Social-role 12-month Health Coach SMD endpoints reversed

**Status:** Pending Human Adjudication  
**Category:** Statistical reporting inconsistency  
**Checker provenance:** statistical P1-013 (S022).  
**Exact source locations:** [main article — PDF p. 10](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, social role, 12 months, Health Coach vs usual care plus SMD.  
**Printed values:** `0.07 (0.09 to -0.10)`.  
**Comparison/rule/calculation:** `0.09 > -0.10`; endpoints are reversed.  
**Direct observation vs diagnostic reasoning:** Direct ordering check.  
**Source-grounded alternatives:** Endpoint order/signs may be incorrect.  
**Missing definition/human question:** What ordered CI is intended?  
**Bounded downstream relevance:** An SMD interval could be copied into synthesis.

## C021 — Social-role 12-month Health Coach versus painTRAINER SMD endpoints reversed

**Status:** Pending Human Adjudication  
**Category:** Statistical reporting inconsistency  
**Checker provenance:** statistical P1-014 (S022).  
**Exact source locations:** [main article — PDF p. 10](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, social role, 12 months, Health Coach vs painTRAINER SMD.  
**Printed values:** `0.27 (0.28 to 0.12)`.  
**Comparison/rule/calculation:** `0.28 > 0.12`; endpoints are reversed.  
**Direct observation vs diagnostic reasoning:** Direct ordering check.  
**Source-grounded alternatives:** Endpoint order/signs may be incorrect.  
**Missing definition/human question:** What ordered CI is intended?  
**Bounded downstream relevance:** An SMD interval could be copied into synthesis.

## C022 — Physical-function 3-month painTRAINER SMD endpoints reversed

**Status:** Pending Human Adjudication  
**Category:** Statistical reporting inconsistency  
**Checker provenance:** statistical P1-015 (S023).  
**Exact source locations:** [main article — PDF p. 10](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, physical function, 3 months, painTRAINER vs usual care plus SMD.  
**Printed values:** `0.09 (0.16 to 0.07)`.  
**Comparison/rule/calculation:** `0.16 > 0.07`; endpoints are reversed.  
**Direct observation vs diagnostic reasoning:** Direct ordering check.  
**Source-grounded alternatives:** Endpoint order/signs may be incorrect.  
**Missing definition/human question:** What ordered CI is intended?  
**Bounded downstream relevance:** An SMD interval could be copied into synthesis.

## C023 — Physical-function 3-month Health Coach SMD endpoints reversed

**Status:** Pending Human Adjudication  
**Category:** Statistical reporting inconsistency  
**Checker provenance:** statistical P1-016 (S023).  
**Exact source locations:** [main article — PDF p. 10](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, physical function, 3 months, Health Coach vs usual care plus SMD.  
**Printed values:** `-0.02 (0.05 to -0.04)`.  
**Comparison/rule/calculation:** `0.05 > -0.04`; endpoints are reversed.  
**Direct observation vs diagnostic reasoning:** Direct ordering check.  
**Source-grounded alternatives:** Endpoint order/signs may be incorrect.  
**Missing definition/human question:** What ordered CI is intended?  
**Bounded downstream relevance:** An SMD interval could be copied into synthesis.

## C024 — Physical-function 3-month Health Coach versus painTRAINER SMD endpoints reversed

**Status:** Pending Human Adjudication  
**Category:** Statistical reporting inconsistency  
**Checker provenance:** statistical P1-017 (S023).  
**Exact source locations:** [main article — PDF p. 10](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, physical function, 3 months, Health Coach vs painTRAINER SMD.  
**Printed values:** `0.16 (0.22 to 0.15)`.  
**Comparison/rule/calculation:** `0.22 > 0.15`; endpoints are reversed.  
**Direct observation vs diagnostic reasoning:** Direct ordering check.  
**Source-grounded alternatives:** Endpoint order/signs may be incorrect.  
**Missing definition/human question:** What ordered CI is intended?  
**Bounded downstream relevance:** An SMD interval could be copied into synthesis.

## C025 — Physical-function 6-month painTRAINER SMD endpoints reversed and exclude estimate

**Status:** Pending Human Adjudication  
**Category:** Statistical reporting inconsistency  
**Checker provenance:** statistical P1-018 (S024).  
**Exact source locations:** [main article — PDF p. 10](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, physical function, 6 months, painTRAINER vs usual care plus SMD.  
**Printed values:** `0.15 (0.09 to -0.06)`.  
**Comparison/rule/calculation:** `0.09 > -0.06`; sorting endpoints still gives `[-0.06,0.09]`, which excludes 0.15.  
**Direct observation vs diagnostic reasoning:** Printed values and ordering/containment checks are direct.  
**Source-grounded alternatives:** Signs/order or estimate/CI may be incorrect.  
**Missing definition/human question:** What estimate and ordered CI are intended?  
**Bounded downstream relevance:** An SMD/CI could be copied into synthesis.

## C026 — Physical-function 6-month Health Coach SMD endpoints reversed

**Status:** Pending Human Adjudication  
**Category:** Statistical reporting inconsistency  
**Checker provenance:** statistical P1-019 (S024).  
**Exact source locations:** [main article — PDF p. 10](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, physical function, 6 months, Health Coach vs usual care plus SMD.  
**Printed values:** `0.02 (0.03 to -0.18)`.  
**Comparison/rule/calculation:** `0.03 > -0.18`; endpoints are reversed.  
**Direct observation vs diagnostic reasoning:** Direct ordering check.  
**Source-grounded alternatives:** Signs/order may be incorrect.  
**Missing definition/human question:** What ordered CI is intended?  
**Bounded downstream relevance:** An SMD interval could be copied into synthesis.

## C027 — Physical-function 6-month Health Coach versus painTRAINER SMD endpoints reversed and exclude estimate

**Status:** Pending Human Adjudication  
**Category:** Statistical reporting inconsistency  
**Checker provenance:** statistical P1-020 (S024).  
**Exact source locations:** [main article — PDF p. 10](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, physical function, 6 months, Health Coach vs painTRAINER SMD.  
**Printed values:** `0.22 (0.16 to 0.05)`.  
**Comparison/rule/calculation:** `0.16 > 0.05`; sorted interval `[0.05,0.16]` excludes 0.22.  
**Direct observation vs diagnostic reasoning:** Direct printed checks.  
**Source-grounded alternatives:** Endpoint order/signs or estimate/CI may be wrong.  
**Missing definition/human question:** What estimate and ordered CI are intended?  
**Bounded downstream relevance:** An SMD/CI could be copied into synthesis.

## C028 — Physical-function 12-month painTRAINER SMD endpoints reversed and exclude estimate

**Status:** Pending Human Adjudication  
**Category:** Statistical reporting inconsistency  
**Checker provenance:** statistical P1-021 (S025).  
**Exact source locations:** [main article — PDF p. 10](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, physical function, 12 months, painTRAINER vs usual care plus SMD.  
**Printed values:** `0.20 (0.18 to -0.03)`.  
**Comparison/rule/calculation:** `0.18 > -0.03`; sorted interval `[-0.03,0.18]` excludes 0.20.  
**Direct observation vs diagnostic reasoning:** Direct printed checks.  
**Source-grounded alternatives:** Endpoint order/signs or estimate/CI may be wrong.  
**Missing definition/human question:** What estimate and ordered CI are intended?  
**Bounded downstream relevance:** An SMD/CI could be copied into synthesis.

## C029 — Physical-function 12-month Health Coach SMD endpoints reversed and exclude estimate

**Status:** Pending Human Adjudication  
**Category:** Statistical reporting inconsistency  
**Checker provenance:** statistical P1-022 (S025).  
**Exact source locations:** [main article — PDF p. 10](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, physical function, 12 months, Health Coach vs usual care plus SMD.  
**Printed values:** `0.07 (0.04 to -0.16)`.  
**Comparison/rule/calculation:** `0.04 > -0.16`; sorted interval `[-0.16,0.04]` excludes 0.07.  
**Direct observation vs diagnostic reasoning:** Direct printed checks.  
**Source-grounded alternatives:** Endpoint order/signs or estimate/CI may be wrong.  
**Missing definition/human question:** What estimate and ordered CI are intended?  
**Bounded downstream relevance:** An SMD/CI could be copied into synthesis.

## C030 — Physical-function 12-month Health Coach versus painTRAINER SMD endpoints reversed and exclude estimate

**Status:** Pending Human Adjudication  
**Category:** Statistical reporting inconsistency  
**Checker provenance:** statistical P1-023 (S025).  
**Exact source locations:** [main article — PDF p. 10](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, physical function, 12 months, Health Coach vs painTRAINER SMD.  
**Printed values:** `0.27 (0.25 to 0.09)`.  
**Comparison/rule/calculation:** `0.25 > 0.09`; sorted interval `[0.09,0.25]` excludes 0.27.  
**Direct observation vs diagnostic reasoning:** Direct printed checks.  
**Source-grounded alternatives:** Endpoint order/signs or estimate/CI may be wrong.  
**Missing definition/human question:** What estimate and ordered CI are intended?  
**Bounded downstream relevance:** An SMD/CI could be copied into synthesis.

## C031 — PGIC-pain 12-month painTRAINER SMD outside printed CI

**Status:** Pending Human Adjudication  
**Category:** Statistical reporting inconsistency  
**Checker provenance:** statistical P1-024 (S028).  
**Exact source locations:** [main article — PDF p. 11](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11), Table 3, PGIC-pain, 12 months, painTRAINER vs usual care plus SMD.  
**Printed values:** `-0.55 (-0.50 to 0.05)`.  
**Comparison/rule/calculation:** `-0.55 < -0.50`, outside CI.  
**Direct observation vs diagnostic reasoning:** Direct containment check.  
**Source-grounded alternatives:** Estimate or endpoint may be incorrect.  
**Missing definition/human question:** What matched CI is intended?  
**Bounded downstream relevance:** An SMD/CI could be copied into synthesis.

## C032 — PGIC-pain 12-month Health Coach SMD outside printed CI

**Status:** Pending Human Adjudication  
**Category:** Statistical reporting inconsistency  
**Checker provenance:** statistical P1-025 (S028).  
**Exact source locations:** [main article — PDF p. 11](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11), Table 3, PGIC-pain, 12 months, Health Coach vs usual care plus SMD.  
**Printed values:** `-0.57 (-0.54 to -0.08)`.  
**Comparison/rule/calculation:** `-0.57 < -0.54`, outside CI.  
**Direct observation vs diagnostic reasoning:** Direct containment check.  
**Source-grounded alternatives:** Estimate or endpoint may be incorrect.  
**Missing definition/human question:** What matched CI is intended?  
**Bounded downstream relevance:** An SMD/CI could be copied into synthesis.

## C033 — PGIC-pain 12-month Health Coach versus painTRAINER SMD outside printed CI

**Status:** Pending Human Adjudication  
**Category:** Statistical reporting inconsistency  
**Checker provenance:** statistical P1-026 (S028).  
**Exact source locations:** [main article — PDF p. 11](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11), Table 3, PGIC-pain, 12 months, Health Coach vs painTRAINER SMD.  
**Printed values:** `-0.29 (-0.25 to 0.14)`.  
**Comparison/rule/calculation:** `-0.29 < -0.25`, outside CI.  
**Direct observation vs diagnostic reasoning:** Direct containment check.  
**Source-grounded alternatives:** Estimate or endpoint may be incorrect.  
**Missing definition/human question:** What matched CI is intended?  
**Bounded downstream relevance:** An SMD/CI could be copied into synthesis.

## C034 — Female total differs across sources if the printed derivations are intended to match

**Status:** Pending Human Adjudication  
**Category:** Cross-document numeric inconsistency  
**Checker provenance:** cross-source observation A.  
**Exact source locations:** [main article — PDF p. 1](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=1), Abstract; [main article — PDF p. 6](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=6), Table 1; [workbook](../../joi250046supp5_prod_1755300121.16087.xlsx), `eTable 3` A11:B11.  
**Printed values:** Abstract `1712 [74%] women`; Table 1 female counts `571/776`, `572/778`, `569/777`; workbook Overall `1713 (73.5)`.  
**Comparison/rule/calculation:** If Table 1 and the workbook intend the same sex variable for the same N=2331 cohort, their counts should agree: `571+572+569=1712`, not workbook 1713. `1712/2331=73.444873...%`, which rounds to 73.4% at one decimal; `1713/2331=73.487773...%`, which rounds to 73.5%.  
**Direct observation vs diagnostic reasoning:** Counts, cohort labels, and percentages are direct; treating the variables as equivalent is conditional because their printed derivation notes differ.  
**Source-grounded alternatives:** Table 1 uses self-reported sex with EHR fallback, while workbook row 11 is footnoted as EHR-derived; these may intentionally be different variables. A data-version update may also exist but is not stated.  
**Missing definition/human question:** Are these sources intended to report the same sex derivation, and, if so, which female count is authoritative?  
**Bounded downstream relevance:** A demographic count may be copied into study-characteristic extraction.

## C035 — Narrative current-depression percentage differs from Table 1/workbook record

**Status:** Pending Human Adjudication  
**Category:** Cross-document numeric inconsistency  
**Checker provenance:** cross-source observation B.  
**Exact source locations:** [main article — PDF p. 4](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), Results; [main article — PDF p. 6](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=6), Table 1; [workbook](../../joi250046supp5_prod_1755300121.16087.xlsx), `eTable 3` A82:B82.  
**Printed values:** Narrative `47.8%`; Table 1 `373/775`, `373/777`, `370/777`; workbook `1116 (47.9)`.  
**Comparison/rule/calculation:** Same PHQ-8 >=10 baseline definition; `1116/(775+777+777)=1116/2329=47.9176%`, or 47.9% to one decimal, not 47.8%.  
**Direct observation vs diagnostic reasoning:** Printed values are direct; arithmetic is deterministic.  
**Source-grounded alternatives:** Narrative may use an unprinted denominator or earlier data snapshot.  
**Missing definition/human question:** What numerator/denominator generated the narrative value?  
**Bounded downstream relevance:** Baseline depression prevalence may be copied into evidence tables.

## C036 — painTRAINER 3-month pain-severity SMD differs between narrative and Table 3

**Status:** Pending Human Adjudication  
**Category:** Cross-document numeric inconsistency  
**Checker provenance:** statistical P1-027; cross-source observation C.  
**Exact source locations:** [main article — PDF p. 7](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=7), Secondary Outcomes; [main article — PDF p. 10](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3.  
**Printed values:** Narrative SMD `-0.26`; Table 3 painTRAINER vs usual care plus SMD `-0.25 (-0.28 to -0.02)`.  
**Comparison/rule/calculation:** Same adjusted outcome/time/contrast/effect measure, explicitly cross-referenced; `-0.26 != -0.25`, displayed difference 0.01.  
**Direct observation vs diagnostic reasoning:** Direct matched-value comparison.  
**Source-grounded alternatives:** Differently rounded source outputs are possible but not stated.  
**Missing definition/human question:** Which 3-month SMD is authoritative?  
**Bounded downstream relevance:** A standardized effect may be copied into meta-analysis extraction.

## C037 — Health Coach 3-month pain-severity SMD differs between narrative and Table 3

**Status:** Pending Human Adjudication  
**Category:** Cross-document numeric inconsistency  
**Checker provenance:** statistical P1-028; cross-source observation D.  
**Exact source locations:** [main article — PDF p. 7](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=7), Secondary Outcomes; [main article — PDF p. 10](../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3.  
**Printed values:** Narrative SMD `-0.36`; Table 3 Health Coach vs usual care plus SMD `-0.34 (-0.36 to -0.13)`.  
**Comparison/rule/calculation:** Same adjusted outcome/time/contrast/effect measure; `-0.36 != -0.34`, displayed difference 0.02.  
**Direct observation vs diagnostic reasoning:** Direct matched-value comparison.  
**Source-grounded alternatives:** Differently rounded source outputs are possible but not stated.  
**Missing definition/human question:** Which 3-month SMD is authoritative?  
**Bounded downstream relevance:** A standardized effect may be copied into meta-analysis extraction.

## Ledger limitations

- Source package lacks unrounded model output/covariance; candidates use only printed mechanical comparisons.
- No display-zero-only finding received an ID.
- C005 and C035 concern different printed values, comparators, and rules and were intentionally not merged.
