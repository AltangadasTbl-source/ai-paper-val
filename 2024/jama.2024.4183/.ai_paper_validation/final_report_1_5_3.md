# Quantitative Quality-Control Consistency Review — Workflow 1.5.3

## Pending Human Adjudication

Every observation below is **Pending Human Adjudication**. This is a quantitative reporting quality-control review, not a determination of validity, correction, or paper-level conclusion impact. Small preventable reporting defects can matter for downstream evidence extraction if confirmed; propagation, conclusion change, and serious harm are not claimed.

## Executive Quality-Control Summary

Complete uncapped review registered 24 stable candidate consistency issues (C001-C024). All 91 direct-source PDF pages were mapped. No candidate arises solely from a coherent display-zero P value.

## Package and Reused-Evidence Provenance

Direct sources were the 10-page main article, 45-page protocol, and 36-page results supplement. Source identities and SHA-256 values are recorded in [source inventory](review_1_5_3/source_inventory.md). Reused assets were inventoried but yielded zero reusable scientific-coverage units: DOC-001 and DOC-003 derivatives were stale after source-hash mismatch, and DOC-002 had no extraction. See [reused-evidence inventory](review_1_5_3/evidence_asset_inventory.md).

## Scope, Complete Coverage, and Exclusions

The review covered numeric, denominator, statistical, cross-document, measure/label, and rate/count consistency in supplied sources only. Source coverage is complete: 91 total units, 0 reusable units, 91 fresh-required units, and 91 mapped units ([coverage](review_1_5_3/source_coverage.md)). It excluded broad methodological, clinical, novelty, misconduct, and raw-data audits. There is no review queue, count cap, top-N subset, or deferred-by-cap section.

## Quantitative and Statistical Relationship Coverage

The numeric relationship inventory contains N001-N072; the statistical relationship inventory contains S001-S030. Independent numeric and cross-source checks were completed, and both statistical passes covered all 30 relationships. Details are retained in the [numeric inventory](review_1_5_3/relationships/numeric_relationship_inventory.md), [statistical inventory](review_1_5_3/statistics/relationship_inventory.md), [pass 1](review_1_5_3/checkers/statistical_pass_1.md), and [pass 2](review_1_5_3/checkers/statistical_pass_2.md).

## Candidate Index

| ID | Candidate consistency issue |
|---|---|
| C001 | Abstract phase-2 allocation percentages use incompatible denominators |
| C002 | Baseline sex counts do not close to printed arm denominators |
| C003 | Randomization total does not close to two displayed branches |
| C004 | Attendance status differs for continuation assignments |
| C005 | Conditional CNRT dose-increase CrI comparison differs |
| C006 | CNRT-switch primary CrI differs across occurrences |
| C007 | Varenicline-to-CNRT switch sign/reference differs |
| C008 | Increased-varenicline CrI upper endpoint differs |
| C009 | Phase-1 abstainer CrI lower endpoint differs |
| C010 | Protocol beta parameters do not reproduce paired probability |
| C011 | Protocol Aim-1 power rises at a stricter threshold |
| C012 | Protocol Table 3 comparator label is duplicated |
| C013 | One ETable 3 cell order differs from n (%) heading |
| C014 | EOT+30 CNRT-switch cell values do not reconcile as printed |
| C015 | EOT+30 increased-CNRT cell interval does not reconcile as printed |
| C016 | EOT+30 CNRT-switch ARD interval does not reconcile as printed |
| C017 | Repeated increased-varenicline intervals do not reconcile as printed |
| C018 | EOT+30 abstainer ARD differs between narrative and eTable |
| C019 | Six-month CNRT-switch cross-reference does not directly identify matched table |
| C020 | Six-month abstainer interval/direction do not reconcile as printed |
| C021 | Abstainer-summary cross-reference does not directly identify matched table |
| C022 | VAR-plus-versus-switch cross-reference does not directly identify matched table |
| C023 | Employment value order differs from declared n (%) |
| C024 | Employment totals do not close to two printed column Ns |

## Candidate Evidence Cards

## C001 — Abstract phase-2 allocation percentages mix incompatible denominators

**Candidate statement:** Abstract phase-2 allocation percentages mix incompatible denominators.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [Main article p. 1](<../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1>); [Main article p. 6](<../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=6>).

**Source evidence:** Among 191 CNRT nonabstainers the abstract prints 90 (47%), 50 (33%), and 51 (34%); among 157 varenicline nonabstainers it prints 39 (32%), 41 (34%), and 77 (49%). Figure 2 shows that 40 and 35 nonattenders were imputed into continuation.

**Reported-versus-comparator:** Printed evidence versus the matched source occurrence or stated consistency rule.

**Reasoning procedure:** The percentages in each sentence should use its introduced denominator or explicitly distinguish rerandomized from full analysis populations. They sum to 114% and 115%; continuation uses 191/157 while other arms use 151/122.

**Calculation:** Reproduce the stated arithmetic or direct printed comparison at displayed precision; see source evidence and consistency rule.

**Alternative source-grounded interpretations:** The supplied package does not state an authoritative correction; alternative production or version explanations require human review.

**Mechanical evidence recheck:** Exact cited values and locations were independently rechecked against supplied PDFs.

**Quality-control relevance:** The printed relationship requires human adjudication before use as a reconciled quantitative record.

**Potential downstream evidence impact:** If confirmed, a data extractor, systematic review, meta-analysis, or guideline could copy the affected value, interval, denominator, label, or cross-reference. Propagation and conclusion change are not claimed.

**Human verification steps:** Which denominator is intended for each parenthetical allocation percentage?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Main baseline sex counts exceed both printed arm denominators

**Candidate statement:** Main baseline sex counts exceed both printed arm denominators.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [Main article p. 5](<../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=5>), baseline Table.

**Source evidence:** Each arm is `n=245`, but each prints female 105 (42.9) and male 145 (57.1).

**Reported-versus-comparator:** Printed evidence versus the matched source occurrence or stated consistency rule.

**Reasoning procedure:** Mutually exclusive counts must sum to the column total: 105+145=250, not 245; 145/245=59.2%, not 57.1%.

**Calculation:** Reproduce the stated arithmetic or direct printed comparison at displayed precision; see source evidence and consistency rule.

**Alternative source-grounded interpretations:** The supplied package does not state an authoritative correction; alternative production or version explanations require human review.

**Mechanical evidence recheck:** Exact cited values and locations were independently rechecked against supplied PDFs.

**Quality-control relevance:** The printed relationship requires human adjudication before use as a reconciled quantitative record.

**Potential downstream evidence impact:** If confirmed, a data extractor, systematic review, meta-analysis, or guideline could copy the affected value, interval, denominator, label, or cross-reference. Propagation and conclusion change are not claimed.

**Human verification steps:** Is the male count intended to be 140, or is another table element incorrect?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Displayed randomization total does not equal its two initial branches

**Candidate statement:** Displayed randomization total does not equal its two initial branches.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [Main article p. 4](<../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=4>); [Main article p. 6](<../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=6>).

**Source evidence:** Results/Figure 2 state 491 randomized, followed by branches of 245 CNRT and 245 varenicline; the abstract/analysis population is 490 and one participant was excluded later.

**Reported-versus-comparator:** Printed evidence versus the matched source occurrence or stated consistency rule.

**Reasoning procedure:** The two displayed initial branches sum to 490, not 491. A later exclusion explains an analysis total but does not close the displayed initial branch identity.

**Calculation:** Reproduce the stated arithmetic or direct printed comparison at displayed precision; see source evidence and consistency rule.

**Alternative source-grounded interpretations:** The supplied package does not state an authoritative correction; alternative production or version explanations require human review.

**Mechanical evidence recheck:** Exact cited values and locations were independently rechecked against supplied PDFs.

**Quality-control relevance:** The printed relationship requires human adjudication before use as a reconciled quantitative record.

**Potential downstream evidence impact:** If confirmed, a data extractor, systematic review, meta-analysis, or guideline could copy the affected value, interval, denominator, label, or cross-reference. Propagation and conclusion change are not claimed.

**Human verification steps:** What initial allocation includes the 491st randomized participant?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Results reverses attendance status for continuation assignments

**Candidate statement:** Results reverses attendance status for continuation assignments.

**Category:** Analysis-unit or population inconsistency

**Exact source locations:** [Main article p. 1](<../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1>); [Main article p. 4](<../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=4>); [Main article p. 6](<../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=6>).

**Source evidence:** Results says the 40 CNRT and 35 varenicline participants `who did attend rerandomization` were assigned to continuation; abstract and Figure 2 say they did not return/attend.

**Reported-versus-comparator:** Printed evidence versus the matched source occurrence or stated consistency rule.

**Reasoning procedure:** The same 75-person analysis-set pathway cannot simultaneously be attendees and nonattendees.

**Calculation:** Reproduce the stated arithmetic or direct printed comparison at displayed precision; see source evidence and consistency rule.

**Alternative source-grounded interpretations:** The supplied package does not state an authoritative correction; alternative production or version explanations require human review.

**Mechanical evidence recheck:** Exact cited values and locations were independently rechecked against supplied PDFs.

**Quality-control relevance:** The printed relationship requires human adjudication before use as a reconciled quantitative record.

**Potential downstream evidence impact:** If confirmed, a data extractor, systematic review, meta-analysis, or guideline could copy the affected value, interval, denominator, label, or cross-reference. Propagation and conclusion change are not claimed.

**Human verification steps:** Was `not` omitted from the Results sentence?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — CNRT dose-increase primary CrI differs between abstract and matched results

**Candidate statement:** CNRT dose-increase primary CrI differs between abstract and matched results.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [Main article p. 1](<../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1>); [Main article p. 5](<../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=5>); [Supplement 2 p. 21](<../joi240036supp2_prod_1716416466.01349.pdf#page=21>).

**Source evidence:** After listing both CNRT rescue arms, the abstract's singular following statement gives RD 6%, 95% CrI 6%-11%; Results and eTable 4 explicitly give 6%, 2%-11% for increased CNRT versus continuation.

**Reported-versus-comparator:** Printed evidence versus the matched source occurrence or stated consistency rule.

**Reasoning procedure:** If the abstract parenthetical applies to both rescue arms, matched population, time, contrast, measure, and interval level should reproduce the same endpoints absent a stated alternate analysis. Its grammatical scope is not explicit.

**Calculation:** Reproduce the stated arithmetic or direct printed comparison at displayed precision; see source evidence and consistency rule.

**Alternative source-grounded interpretations:** The abstract parenthetical may apply only to switching; this card remains conditional on grammatical scope.

**Mechanical evidence recheck:** Exact cited values and locations were independently rechecked against supplied PDFs.

**Quality-control relevance:** The printed relationship requires human adjudication before use as a reconciled quantitative record.

**Potential downstream evidence impact:** If confirmed, a data extractor, systematic review, meta-analysis, or guideline could copy the affected value, interval, denominator, label, or cross-reference. Propagation and conclusion change are not claimed.

**Human verification steps:** Does the abstract interval apply only to switching or to both rescue arms, and if it applies to increased CNRT, is the intended lower endpoint 6% or 2%?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — CNRT switch primary CrI differs across abstract, Results, and eTable

**Candidate statement:** CNRT switch primary CrI differs across abstract, Results, and eTable.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [Main article p. 1](<../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1>); [Main article p. 5](<../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=5>); [Supplement 2 p. 21](<../joi240036supp2_prod_1716416466.01349.pdf#page=21>).

**Source evidence:** Switch-to-varenicline versus continuation is RD 6% with CrI 6%-11%, 2%-11%, and 2%-10% at the three locations.

**Reported-versus-comparator:** Printed evidence versus the matched source occurrence or stated consistency rule.

**Reasoning procedure:** One matched contrast should retain one displayed 95% CrI absent a named estimator/version distinction.

**Calculation:** Reproduce the stated arithmetic or direct printed comparison at displayed precision; see source evidence and consistency rule.

**Alternative source-grounded interpretations:** The supplied package does not state an authoritative correction; alternative production or version explanations require human review.

**Mechanical evidence recheck:** Exact cited values and locations were independently rechecked against supplied PDFs.

**Quality-control relevance:** The printed relationship requires human adjudication before use as a reconciled quantitative record.

**Potential downstream evidence impact:** If confirmed, a data extractor, systematic review, meta-analysis, or guideline could copy the affected value, interval, denominator, label, or cross-reference. Propagation and conclusion change are not claimed.

**Human verification steps:** Which interval belongs to the final switch contrast?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Varenicline-to-CNRT switch contrast has inconsistent sign and reference

**Candidate statement:** Varenicline-to-CNRT switch contrast has inconsistent sign and reference.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [Main article p. 1](<../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1>); [Main article p. 5](<../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=5>); [Main article p. 7](<../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=7>); [Supplement 2 p. 21](<../joi240036supp2_prod_1716416466.01349.pdf#page=21>).

**Source evidence:** Main text prints switch relative to continuation RD -3% (-4% to -1%) but says continuation was worse; eTable 4 labels switch versus stay and prints +3% (1%-4%); displayed cells are 0% switch and 3% stay.

**Reported-versus-comparator:** Printed evidence versus the matched source occurrence or stated consistency rule.

**Reasoning procedure:** Contrast label, sign, interval, raw direction, and narrative interpretation must use the same reference orientation.

**Calculation:** Reproduce the stated arithmetic or direct printed comparison at displayed precision; see source evidence and consistency rule.

**Alternative source-grounded interpretations:** The supplied package does not state an authoritative correction; alternative production or version explanations require human review.

**Mechanical evidence recheck:** Exact cited values and locations were independently rechecked against supplied PDFs.

**Quality-control relevance:** The printed relationship requires human adjudication before use as a reconciled quantitative record.

**Potential downstream evidence impact:** If confirmed, a data extractor, systematic review, meta-analysis, or guideline could copy the affected value, interval, denominator, label, or cross-reference. Propagation and conclusion change are not claimed.

**Human verification steps:** Which signed contrast and reference orientation are intended?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — Increased-varenicline primary CrI upper endpoint differs

**Candidate statement:** Increased-varenicline primary CrI upper endpoint differs.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [Main article p. 1](<../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1>); [Main article p. 5](<../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=5>); [Supplement 2 p. 21](<../joi240036supp2_prod_1716416466.01349.pdf#page=21>).

**Source evidence:** Main abstract/results print RD 18% (13%-24%); eTable 4 prints 18% (13%-23%).

**Reported-versus-comparator:** Printed evidence versus the matched source occurrence or stated consistency rule.

**Reasoning procedure:** A matched primary contrast should reproduce the same interval endpoint at the stated precision.

**Calculation:** Reproduce the stated arithmetic or direct printed comparison at displayed precision; see source evidence and consistency rule.

**Alternative source-grounded interpretations:** The supplied package does not state an authoritative correction; alternative production or version explanations require human review.

**Mechanical evidence recheck:** Exact cited values and locations were independently rechecked against supplied PDFs.

**Quality-control relevance:** The printed relationship requires human adjudication before use as a reconciled quantitative record.

**Potential downstream evidence impact:** If confirmed, a data extractor, systematic review, meta-analysis, or guideline could copy the affected value, interval, denominator, label, or cross-reference. Propagation and conclusion change are not claimed.

**Human verification steps:** Is the final upper endpoint 24% or 23%?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C009 — Phase-1 abstainer primary CrI lower endpoint differs

**Candidate statement:** Phase-1 abstainer primary CrI lower endpoint differs.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [Main article p. 7](<../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=7>); [Supplement 2 p. 21](<../joi240036supp2_prod_1716416466.01349.pdf#page=21>).

**Source evidence:** Main Results gives CNRT-versus-varenicline RD 6% (-5% to 16%); eTable 4 gives 6% (-4% to 16%).

**Reported-versus-comparator:** Printed evidence versus the matched source occurrence or stated consistency rule.

**Reasoning procedure:** A matched comparison should retain the same interval endpoints absent a stated analysis distinction.

**Calculation:** Reproduce the stated arithmetic or direct printed comparison at displayed precision; see source evidence and consistency rule.

**Alternative source-grounded interpretations:** The supplied package does not state an authoritative correction; alternative production or version explanations require human review.

**Mechanical evidence recheck:** Exact cited values and locations were independently rechecked against supplied PDFs.

**Quality-control relevance:** The printed relationship requires human adjudication before use as a reconciled quantitative record.

**Potential downstream evidence impact:** If confirmed, a data extractor, systematic review, meta-analysis, or guideline could copy the affected value, interval, denominator, label, or cross-reference. Propagation and conclusion change are not claimed.

**Human verification steps:** Is the final lower endpoint -5% or -4%?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C010 — Protocol beta parameters do not reproduce the paired varenicline response probability

**Candidate statement:** Protocol beta parameters do not reproduce the paired varenicline response probability.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [Protocol p. 32](<../joi240036supp1_prod_1716416466.00349.pdf#page=32>), Figure 2.

**Source evidence:** Varenicline week-6 response is paired as 0.50 (0.40-0.60) with Beta(785,869).

**Reported-versus-comparator:** Printed evidence versus the matched source occurrence or stated consistency rule.

**Reasoning procedure:** The beta mean from the printed parameters is 785/(785+869)=0.4746, not 0.50; the interval also is not reproduced by those concentrated parameters under the recorded diagnostic.

**Calculation:** Reproduce the stated arithmetic or direct printed comparison at displayed precision; see source evidence and consistency rule.

**Alternative source-grounded interpretations:** The beta parameters may represent a different quantity; the interval-to-beta linkage is not defined.

**Mechanical evidence recheck:** Exact cited values and locations were independently rechecked against supplied PDFs.

**Quality-control relevance:** The printed relationship requires human adjudication before use as a reconciled quantitative record.

**Potential downstream evidence impact:** If confirmed, a data extractor, systematic review, meta-analysis, or guideline could copy the affected value, interval, denominator, label, or cross-reference. Propagation and conclusion change are not claimed.

**Human verification steps:** Do the beta parameters represent a different quantity, or is one printed input incorrect?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C011 — Protocol Aim-1 power increases at a stricter nested threshold

**Candidate statement:** Protocol Aim-1 power increases at a stricter nested threshold.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [Protocol p. 34](<../joi240036supp1_prod_1716416466.00349.pdf#page=34>), Table 3.

**Source evidence:** Aim-1 detection power is 0.948, 0.980, 0.974, and 0.963 at posterior thresholds 0.80, 0.85, 0.90, and 0.95.

**Reported-versus-comparator:** Printed evidence versus the matched source occurrence or stated consistency rule.

**Reasoning procedure:** On one simulation set, detections satisfying a stricter threshold are a subset of those satisfying a looser threshold; 0.980 exceeds 0.948 by 0.032.

**Calculation:** Reproduce the stated arithmetic or direct printed comparison at displayed precision; see source evidence and consistency rule.

**Alternative source-grounded interpretations:** Simulation realizations or detection definitions may differ; common use is not explicitly stated.

**Mechanical evidence recheck:** Exact cited values and locations were independently rechecked against supplied PDFs.

**Quality-control relevance:** The printed relationship requires human adjudication before use as a reconciled quantitative record.

**Potential downstream evidence impact:** If confirmed, a data extractor, systematic review, meta-analysis, or guideline could copy the affected value, interval, denominator, label, or cross-reference. Propagation and conclusion change are not claimed.

**Human verification steps:** Are the first two power values or their threshold labels transposed, or is a nonnested definition missing?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C012 — Protocol Table 3 duplicates an Aim-2 comparator label

**Candidate statement:** Protocol Table 3 duplicates an Aim-2 comparator label.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [Protocol p. 29](<../joi240036supp1_prod_1716416466.00349.pdf#page=29>); [Protocol p. 33](<../joi240036supp1_prod_1716416466.00349.pdf#page=33>); [Protocol p. 34](<../joi240036supp1_prod_1716416466.00349.pdf#page=34>).

**Source evidence:** Table 3 labels the first and third Aim-2 effects `VAR vs. NPL`; the third estimate 0.195 equals 0.399-0.204, matching VAR versus NPL+, while 0.370 equals VAR versus NPL.

**Reported-versus-comparator:** Printed evidence versus the matched source occurrence or stated consistency rule.

**Reasoning procedure:** A comparator label must identify the displayed effect and stated contrast formula.

**Calculation:** Reproduce the stated arithmetic or direct printed comparison at displayed precision; see source evidence and consistency rule.

**Alternative source-grounded interpretations:** The supplied package does not state an authoritative correction; alternative production or version explanations require human review.

**Mechanical evidence recheck:** Exact cited values and locations were independently rechecked against supplied PDFs.

**Quality-control relevance:** The printed relationship requires human adjudication before use as a reconciled quantitative record.

**Potential downstream evidence impact:** If confirmed, a data extractor, systematic review, meta-analysis, or guideline could copy the affected value, interval, denominator, label, or cross-reference. Propagation and conclusion change are not claimed.

**Human verification steps:** Should the third label read `VAR vs. NPL+`?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C013 — ETable 3 reverses count and percentage in one n (%) cell

**Candidate statement:** ETable 3 reverses count and percentage in one n (%) cell.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [Supplement 2 p. 19](<../joi240036supp2_prod_1716416466.01349.pdf#page=19>), ETable 3.

**Source evidence:** Under `n (%)`, race/ethnicity `Other` for the N=41 VAR-nonabstainer-to-CNRT column is `4.9 (2)`.

**Reported-versus-comparator:** Printed evidence versus the matched source occurrence or stated consistency rule.

**Reasoning procedure:** Counts must be integers and 2/41=4.878%, so the values fit only as `2 (4.9)`.

**Calculation:** Reproduce the stated arithmetic or direct printed comparison at displayed precision; see source evidence and consistency rule.

**Alternative source-grounded interpretations:** The supplied package does not state an authoritative correction; alternative production or version explanations require human review.

**Mechanical evidence recheck:** Exact cited values and locations were independently rechecked against supplied PDFs.

**Quality-control relevance:** The printed relationship requires human adjudication before use as a reconciled quantitative record.

**Potential downstream evidence impact:** If confirmed, a data extractor, systematic review, meta-analysis, or guideline could copy the affected value, interval, denominator, label, or cross-reference. Propagation and conclusion change are not claimed.

**Human verification steps:** Should the cell be reordered to `2 (4.9)`?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C014 — EOT+30 CNRT-switch cell estimate and CrI do not reconcile with matched figure as printed

**Candidate statement:** EOT+30 CNRT-switch cell estimate and CrI do not reconcile with matched figure as printed.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [Supplement 2 p. 10](<../joi240036supp2_prod_1716416466.01349.pdf#page=10>); [Supplement 2 p. 15](<../joi240036supp2_prod_1716416466.01349.pdf#page=15>).

**Source evidence:** Narrative prints 1.0% (7.0%-1.3%); matched eFigure 2 prints 5/51, 10% (7%-13%).

**Reported-versus-comparator:** Printed evidence versus the matched source occurrence or stated consistency rule.

**Reasoning procedure:** The narrative interval is reversed/non-containing, its estimate differs from the matched cell, and 5/51 rounds to 10%.

**Calculation:** Reproduce the stated arithmetic or direct printed comparison at displayed precision; see source evidence and consistency rule.

**Alternative source-grounded interpretations:** The supplied package does not state an authoritative correction; alternative production or version explanations require human review.

**Mechanical evidence recheck:** Exact cited values and locations were independently rechecked against supplied PDFs.

**Quality-control relevance:** The printed relationship requires human adjudication before use as a reconciled quantitative record.

**Potential downstream evidence impact:** If confirmed, a data extractor, systematic review, meta-analysis, or guideline could copy the affected value, interval, denominator, label, or cross-reference. Propagation and conclusion change are not claimed.

**Human verification steps:** Is the narrative intended to read 10% (7%-13%)?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C015 — EOT+30 increased-CNRT cell CrI upper endpoint does not reconcile with matched figure as printed

**Candidate statement:** EOT+30 increased-CNRT cell CrI upper endpoint does not reconcile with matched figure as printed.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [Supplement 2 p. 10](<../joi240036supp2_prod_1716416466.01349.pdf#page=10>); [Supplement 2 p. 15](<../joi240036supp2_prod_1716416466.01349.pdf#page=15>).

**Source evidence:** Narrative prints 8.0% (5.0%-1.1%); eFigure 2 prints 4/50, 8% (5%-11%).

**Reported-versus-comparator:** Printed evidence versus the matched source occurrence or stated consistency rule.

**Reasoning procedure:** The narrative interval is reversed and excludes its estimate; the matched cell has ordered endpoints.

**Calculation:** Reproduce the stated arithmetic or direct printed comparison at displayed precision; see source evidence and consistency rule.

**Alternative source-grounded interpretations:** The supplied package does not state an authoritative correction; alternative production or version explanations require human review.

**Mechanical evidence recheck:** Exact cited values and locations were independently rechecked against supplied PDFs.

**Quality-control relevance:** The printed relationship requires human adjudication before use as a reconciled quantitative record.

**Potential downstream evidence impact:** If confirmed, a data extractor, systematic review, meta-analysis, or guideline could copy the affected value, interval, denominator, label, or cross-reference. Propagation and conclusion change are not claimed.

**Human verification steps:** Is `1.1%` a decimal-placement error for `11%`?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C016 — EOT+30 CNRT-switch ARD CrI upper endpoint does not reconcile with matched table as printed

**Candidate statement:** EOT+30 CNRT-switch ARD CrI upper endpoint does not reconcile with matched table as printed.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [Supplement 2 p. 10](<../joi240036supp2_prod_1716416466.01349.pdf#page=10>); [Supplement 2 p. 33](<../joi240036supp2_prod_1716416466.01349.pdf#page=33>).

**Source evidence:** Narrative prints switch-versus-continuation ARD 6.0% (3.0%-1.0%); eTable 9 prints 6% (3%-10%).

**Reported-versus-comparator:** Printed evidence versus the matched source occurrence or stated consistency rule.

**Reasoning procedure:** The narrative effect interval is reversed/non-containing and differs from the matched contrast.

**Calculation:** Reproduce the stated arithmetic or direct printed comparison at displayed precision; see source evidence and consistency rule.

**Alternative source-grounded interpretations:** The supplied package does not state an authoritative correction; alternative production or version explanations require human review.

**Mechanical evidence recheck:** Exact cited values and locations were independently rechecked against supplied PDFs.

**Quality-control relevance:** The printed relationship requires human adjudication before use as a reconciled quantitative record.

**Potential downstream evidence impact:** If confirmed, a data extractor, systematic review, meta-analysis, or guideline could copy the affected value, interval, denominator, label, or cross-reference. Propagation and conclusion change are not claimed.

**Human verification steps:** Is the intended upper endpoint 10%?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C017 — EOT+30 increased-varenicline narrative has repeated intervals that do not reconcile as printed

**Candidate statement:** EOT+30 increased-varenicline narrative has repeated intervals that do not reconcile as printed.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [Supplement 2 p. 10](<../joi240036supp2_prod_1716416466.01349.pdf#page=10>); [Supplement 2 p. 11](<../joi240036supp2_prod_1716416466.01349.pdf#page=11>); [Supplement 2 p. 15](<../joi240036supp2_prod_1716416466.01349.pdf#page=15>); [Supplement 2 p. 33](<../joi240036supp2_prod_1716416466.01349.pdf#page=33>); [Supplement 2 p. 34](<../joi240036supp2_prod_1716416466.01349.pdf#page=34>).

**Source evidence:** Narrative repeats 8.0% (5.0%-1.1%) for the cell and two ARDs; eFigure 2 and eTables 9-10 print 8% (5%-11%).

**Reported-versus-comparator:** Printed evidence versus the matched source occurrence or stated consistency rule.

**Reasoning procedure:** Each repeated narrative interval is reversed/non-containing and differs from its matched figure/table occurrence.

**Calculation:** Reproduce the stated arithmetic or direct printed comparison at displayed precision; see source evidence and consistency rule.

**Alternative source-grounded interpretations:** The supplied package does not state an authoritative correction; alternative production or version explanations require human review.

**Mechanical evidence recheck:** Exact cited values and locations were independently rechecked against supplied PDFs.

**Quality-control relevance:** The printed relationship requires human adjudication before use as a reconciled quantitative record.

**Potential downstream evidence impact:** If confirmed, a data extractor, systematic review, meta-analysis, or guideline could copy the affected value, interval, denominator, label, or cross-reference. Propagation and conclusion change are not claimed.

**Human verification steps:** Should all repeated `1.1%` upper endpoints be `11%`?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C018 — EOT+30 abstainer ARD is 1.1% in narrative but 11% in eTable

**Candidate statement:** EOT+30 abstainer ARD is 1.1% in narrative but 11% in eTable.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [Supplement 2 p. 11](<../joi240036supp2_prod_1716416466.01349.pdf#page=11>); [Supplement 2 p. 15](<../joi240036supp2_prod_1716416466.01349.pdf#page=15>); [Supplement 2 p. 35](<../joi240036supp2_prod_1716416466.01349.pdf#page=35>).

**Source evidence:** Narrative gives ARD 1.1% (-1.0%-22%), while eTable 11 gives 11% (-1%-22%); cell probabilities are 67% versus 56% and probability is 97%.

**Reported-versus-comparator:** Printed evidence versus the matched source occurrence or stated consistency rule.

**Reasoning procedure:** The matched contrast and displayed cell difference support an 11-point, not 1.1-point, value at the displayed precision.

**Calculation:** Reproduce the stated arithmetic or direct printed comparison at displayed precision; see source evidence and consistency rule.

**Alternative source-grounded interpretations:** The supplied package does not state an authoritative correction; alternative production or version explanations require human review.

**Mechanical evidence recheck:** Exact cited values and locations were independently rechecked against supplied PDFs.

**Quality-control relevance:** The printed relationship requires human adjudication before use as a reconciled quantitative record.

**Potential downstream evidence impact:** If confirmed, a data extractor, systematic review, meta-analysis, or guideline could copy the affected value, interval, denominator, label, or cross-reference. Propagation and conclusion change are not claimed.

**Human verification steps:** Is the narrative decimal point unintended?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C019 — Six-month CNRT-switch cross-reference does not directly identify the matched table

**Candidate statement:** The six-month CNRT-switch cross-reference does not directly identify the matched outcome table.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [Supplement 2 p. 11](<../joi240036supp2_prod_1716416466.01349.pdf#page=11>); [Supplement 2 p. 31](<../joi240036supp2_prod_1716416466.01349.pdf#page=31>); [Supplement 2 p. 33](<../joi240036supp2_prod_1716416466.01349.pdf#page=33>).

**Source evidence:** Narrative assigns ARD 1.0% (-2.0%-3.0%), probability 66%, to ETable 7; ETable 7 is compliance, while ETable 9 contains the exact outcome contrast.

**Reported-versus-comparator:** Printed evidence versus the matched source occurrence or stated consistency rule.

**Reasoning procedure:** A quantitative cross-reference should identify the table containing the stated measure and value.

**Calculation:** Reproduce the stated arithmetic or direct printed comparison at displayed precision; see source evidence and consistency rule.

**Alternative source-grounded interpretations:** The supplied package does not state an authoritative correction; alternative production or version explanations require human review.

**Mechanical evidence recheck:** Exact cited values and locations were independently rechecked against supplied PDFs.

**Quality-control relevance:** The printed relationship requires human adjudication before use as a reconciled quantitative record.

**Potential downstream evidence impact:** If confirmed, a data extractor, systematic review, meta-analysis, or guideline could copy the affected value, interval, denominator, label, or cross-reference. Propagation and conclusion change are not claimed.

**Human verification steps:** Should the cross-reference be ETable 9?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C020 — Six-month abstainer narrative interval and direction do not reconcile with matched sources

**Candidate statement:** Six-month abstainer narrative interval and direction do not reconcile with matched sources.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [Supplement 2 p. 12](<../joi240036supp2_prod_1716416466.01349.pdf#page=12>); [Supplement 2 p. 16](<../joi240036supp2_prod_1716416466.01349.pdf#page=16>); [Supplement 2 p. 35](<../joi240036supp2_prod_1716416466.01349.pdf#page=35>).

**Source evidence:** Narrative gives CNRT 39%, VAR 40%, posterior probability 55%, ARD +1.0% (-1.3% to -1.1%), and a varenicline benefit; eTable 11 headed CNRT vs VAR gives +1% (-11% to 12%), probability 56%.

**Reported-versus-comparator:** Printed evidence versus the matched source occurrence or stated consistency rule.

**Reasoning procedure:** The narrative estimate is outside its interval; interval scale, probability, sign/reference label, and stated direction do not all align with the matched table/figure.

**Calculation:** Reproduce the stated arithmetic or direct printed comparison at displayed precision; see source evidence and consistency rule.

**Alternative source-grounded interpretations:** The supplied package does not state an authoritative correction; alternative production or version explanations require human review.

**Mechanical evidence recheck:** Exact cited values and locations were independently rechecked against supplied PDFs.

**Quality-control relevance:** The printed relationship requires human adjudication before use as a reconciled quantitative record.

**Potential downstream evidence impact:** If confirmed, a data extractor, systematic review, meta-analysis, or guideline could copy the affected value, interval, denominator, label, or cross-reference. Propagation and conclusion change are not claimed.

**Human verification steps:** What signed contrast, reference group, interval, and posterior probability are intended?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C021 — Phase-1-abstainer summary cross-reference does not directly identify the matched table

**Candidate statement:** The phase-1-abstainer summary cross-reference does not directly identify the matched table.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [Supplement 2 p. 10](<../joi240036supp2_prod_1716416466.01349.pdf#page=10>); [Supplement 2 p. 34](<../joi240036supp2_prod_1716416466.01349.pdf#page=34>); [Supplement 2 p. 35](<../joi240036supp2_prod_1716416466.01349.pdf#page=35>).

**Source evidence:** The phase-1-abstainer EOT+30 and six-month summary cites ETable 10; ETable 10 reports increase-versus-switch comparisons among nonabstainers, while ETable 11 reports the phase-1-abstainer CNRT-versus-VAR results.

**Reported-versus-comparator:** Printed evidence versus the matched source occurrence or stated consistency rule.

**Reasoning procedure:** A quantitative cross-reference should identify the table containing the stated population and comparison.

**Calculation:** Reproduce the stated arithmetic or direct printed comparison at displayed precision; see source evidence and consistency rule.

**Alternative source-grounded interpretations:** The supplied package does not state an authoritative correction; alternative production or version explanations require human review.

**Mechanical evidence recheck:** Exact cited values and locations were independently rechecked against supplied PDFs.

**Quality-control relevance:** The printed relationship requires human adjudication before use as a reconciled quantitative record.

**Potential downstream evidence impact:** If confirmed, a data extractor, systematic review, meta-analysis, or guideline could copy the affected value, interval, denominator, label, or cross-reference. Propagation and conclusion change are not claimed.

**Human verification steps:** Should the summary cite ETable 11 rather than ETable 10?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C022 — Six-month VAR-plus-versus-switch cross-reference does not directly identify the matched table

**Candidate statement:** The VAR-plus-versus-switch cross-reference does not directly identify the matched direct-contrast table.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [Supplement 2 p. 12](<../joi240036supp2_prod_1716416466.01349.pdf#page=12>); [Supplement 2 p. 33](<../joi240036supp2_prod_1716416466.01349.pdf#page=33>); [Supplement 2 p. 34](<../joi240036supp2_prod_1716416466.01349.pdf#page=34>).

**Source evidence:** The narrative cites ETable 9 for both VAR+ versus continuation and VAR+ versus CNRT switch; ETable 9 contains continuation-reference comparisons, while ETable 10 contains the switch-reference comparison 2% (1%-5%), greater than 99%.

**Reported-versus-comparator:** Printed evidence versus the matched source occurrence or stated consistency rule.

**Reasoning procedure:** A quantitative cross-reference should identify the table defining and reporting the stated comparator.

**Calculation:** Reproduce the stated arithmetic or direct printed comparison at displayed precision; see source evidence and consistency rule.

**Alternative source-grounded interpretations:** The supplied package does not state an authoritative correction; alternative production or version explanations require human review.

**Mechanical evidence recheck:** Exact cited values and locations were independently rechecked against supplied PDFs.

**Quality-control relevance:** The printed relationship requires human adjudication before use as a reconciled quantitative record.

**Potential downstream evidence impact:** If confirmed, a data extractor, systematic review, meta-analysis, or guideline could copy the affected value, interval, denominator, label, or cross-reference. Propagation and conclusion change are not claimed.

**Human verification steps:** Should the switch-reference clause cite ETable 10 rather than ETable 9?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C023 — ETable 3 employment value order differs from declared n (%)

**Candidate statement:** ETable 3 employment value order differs from the declared n (%) heading.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [Supplement 2 p. 19](<../joi240036supp2_prod_1716416466.01349.pdf#page=19>), ETable 3.

**Source evidence:** The section heading is `Employment, n (%)`, but every populated Employed and Unemployed cell prints percentage first and count in parentheses, including `72.2 (39)` and `27.8 (15)` under N=54 and `74.5 (38)` and `25.5 (13)` under N=51.

**Reported-versus-comparator:** Printed evidence versus the matched source occurrence or stated consistency rule.

**Reasoning procedure:** Under `n (%)`, the first value should be an integer count and the parenthetical value a percentage; the printed values reconcile only as percentage(count).

**Calculation:** Reproduce the stated arithmetic or direct printed comparison at displayed precision; see source evidence and consistency rule.

**Alternative source-grounded interpretations:** The supplied package does not state an authoritative correction; alternative production or version explanations require human review.

**Mechanical evidence recheck:** Exact cited values and locations were independently rechecked against supplied PDFs.

**Quality-control relevance:** The printed relationship requires human adjudication before use as a reconciled quantitative record.

**Potential downstream evidence impact:** If confirmed, a data extractor, systematic review, meta-analysis, or guideline could copy the affected value, interval, denominator, label, or cross-reference. Propagation and conclusion change are not claimed.

**Human verification steps:** Should the heading be `Employment, % (n)`, or should all employment cells be reordered to n (%)?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C024 — ETable 3 employment totals do not close to two printed column Ns

**Candidate statement:** ETable 3 employment totals do not close to two printed column Ns.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [Supplement 2 p. 19](<../joi240036supp2_prod_1716416466.01349.pdf#page=19>), ETable 3.

**Source evidence:** In the CNRT+ N=50 column, Employment counts are 40 and 9 (percentages 80 and 18); in the VAR+ N=39 column they are 27 and 11 (69.2 and 28.2). No employment missingness category or footnote is printed.

**Reported-versus-comparator:** Printed evidence versus the matched source occurrence or stated consistency rule.

**Reasoning procedure:** Displayed exhaustive Employed/Unemployed categories should sum to the column N or identify missingness. The totals are 49/50 and 38/39; percentages sum to 98% and 97.4%.

**Calculation:** Reproduce the stated arithmetic or direct printed comparison at displayed precision; see source evidence and consistency rule.

**Alternative source-grounded interpretations:** The supplied package does not state an authoritative correction; alternative production or version explanations require human review.

**Mechanical evidence recheck:** Exact cited values and locations were independently rechecked against supplied PDFs.

**Quality-control relevance:** The printed relationship requires human adjudication before use as a reconciled quantitative record.

**Potential downstream evidence impact:** If confirmed, a data extractor, systematic review, meta-analysis, or guideline could copy the affected value, interval, denominator, label, or cross-reference. Propagation and conclusion change are not claimed.

**Human verification steps:** Are the two shortfalls missing employment values, and what denominator should govern the displayed percentages?

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If confirmed, these observations could affect extraction of denominators, counts, percentages, interval endpoints, signed references, planning parameters, comparator labels, secondary-outcome values, or table navigation. This report does not assert that any such information has propagated, changed conclusions, or caused harm.

## Limitations and Missing Definitions

See the durable [limitations record](review_1_5_3/limitations.md). In brief, no raw data, posterior draws, table-generation files, simulation code, version crosswalk, or history was supplied. C005 remains conditional on abstract grammatical scope; C010 has no defined interval-to-beta linkage; and C011 has no stated common-simulation definition.

## Human Adjudication Checklist

For every stable ID, compare the cited source pages, verify the stated arithmetic or matching rule, decide the intended source interpretation, record validity/importance/action/initials/notes in the card, and retain any authoritative correction separately from this review.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

- **Routing preflight:** PASS ([record](review_1_5_3/routing_preflight.md)).
- **Direct sources:** 3 PDFs; 91 PDF-page units; all 91 mapped.
- **Source integrity:** Source and reused-artifact hashes were recorded before review; the quality audit reports all 3 direct sources and 79 reused artifacts matched those records.
- **Coverage manifest:** [coverage_manifest.md](review_1_5_3/coverage_manifest.md).
- **Evidence recheck:** All C001-C024 were independently rechecked ([record](review_1_5_3/verification/evidence_recheck.md)).

### Agent execution

The execution manifest records the coordinator and every specialist, model, reasoning effort, fresh-start mode, and durable artifact: [agent_execution_manifest.md](review_1_5_3/agent_execution_manifest.md). Both statistical passes were separate fresh gpt-5.6-terra/high agents.

### Reproducibility performance

- **Target basis:** Three current-source PDFs contain 91 total page units; all 91 require fresh direct-source mapping because DOC-001 and DOC-003 derivatives are source-hash stale and DOC-002 has no extraction. The scope includes one main article, a 45-page protocol, and a 36-page results supplement, requiring two mapping lanes, complete direct extraction, visual/table confirmation where needed, and subsequent numeric, cross-source, two-pass statistical, recheck, audit, and report stages. This has fewer total units but 10 more fresh-required units than the 102-unit/81-fresh calibration package, so a bounded 55-75 minute target was selected.
- **Total source units:** 91
- **Fresh-source units:** 91
- **Target elapsed minutes:** 55-75
- **Started UTC:** 2026-08-19T04:32:23Z
- **Finished UTC:** 2026-08-19T05:11:57Z
- **Observed elapsed minutes:** 39.6
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token accounting and cost

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Input tokens | Output tokens | Total tokens | Known token cost (USD) |
|---|---:|---:|---:|---:|
| gpt-5.6-sol | 0 | 0 | 0 | 0.000000 |
| gpt-5.6-terra | 0 | 0 | 0 | 0.000000 |

Authoritative runtime token counts were unavailable for the coordinator and all 15 specialist agents, so the total-token count and complete price remain explicitly incomplete; zero is only the known recorded subtotal, not an estimate of actual usage. Per-agent detail is in [token_usage_summary.md](review_1_5_3/token_usage_summary.md). Cached input and cache-write counts are input subsets; reasoning is an output subset; none is added again to total tokens. Any available amount uses the bundled pricing snapshot dated 2026-08-18 and is a token-only estimate, not an invoice.
