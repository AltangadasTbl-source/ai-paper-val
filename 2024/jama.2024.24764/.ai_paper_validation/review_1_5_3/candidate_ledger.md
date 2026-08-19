# Stable Candidate Ledger

All eight records are **Pending Human Adjudication**. Stable IDs were assigned only after merging checker outputs; no two records compare the same printed values, comparator, and rule. No ID may be deleted, merged, or renumbered after this point.

## C001 — Smoking percentages use a different denominator from the printed smoking totals

- **Category:** Denominator, proportion, or total inconsistency
- **Checker provenance:** Numeric consistency review, NC-1
- **Exact source locations:** [DOC-001 PDF p. 5, Table 1](<../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=5>)
- **Printed evidence:** Group headers are 411 and 410; smoking `Total No.` values are 405 and 402. Counts 220/95/90 and 223/70/109 sum to 405 and 402, but the printed percentages 53.5/23.1/21.9 and 54.4/17.1/26.6 use denominators 411 and 410.
- **Rule and calculation:** A printed variable-specific total ordinarily identifies the denominator unless an alternative convention is stated. For example, 220/405=54.3%, whereas 220/411=53.5% as printed; all six printed percentages follow the group headers, not the row totals.
- **Supported alternative:** `Total No.` may identify nonmissing records while the table intentionally uses the randomized-group denominators, but this convention and the corresponding missingness are not stated on the page.
- **Exact human question:** What denominator was intended, and should the table explicitly explain the six and eight missing smoking values if percentages deliberately use 411 and 410?
- **Status:** Pending Human Adjudication

## C002 — Operating-surgeon level totals exceed participant denominators without a multi-response qualifier

- **Category:** Denominator, proportion, or total inconsistency
- **Checker provenance:** Numeric consistency review, NC-2
- **Exact source locations:** [DOC-001 PDF p. 7, Table 2](<../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=7>)
- **Printed evidence:** With group denominators 411 and 410, consultant/registrar/senior-house-officer counts are 319/123/4 and 318/110/1.
- **Rule and calculation:** The counts sum to 446 and 429, exceeding the participant denominators by 35 and 19; printed percentages sum to 108.5% and 104.6%.
- **Supported alternative:** More than one operating-surgeon level may have been recorded for one operation, making this an intended multi-response field, but the table is labelled `No. of participants (%)` and does not state non-mutual exclusivity.
- **Exact human question:** Were multiple operating-surgeon levels permitted per participant, and if so should the unit/footnote disclose that?
- **Status:** Pending Human Adjudication

## C003 — Fascia-closing surgeon level totals exceed participant denominators without a multi-response qualifier

- **Category:** Denominator, proportion, or total inconsistency
- **Checker provenance:** Numeric consistency review, NC-3
- **Exact source locations:** [DOC-001 PDF p. 7, Table 2 continuation](<../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=7>)
- **Printed evidence:** With group denominators 411 and 410, consultant/registrar/senior-house-officer fascia-closing counts are 201/218/26 and 193/225/15.
- **Rule and calculation:** The counts sum to 445 and 433, exceeding the participant denominators by 34 and 23; printed percentages sum to 108.2% and 105.7%.
- **Supported alternative:** Co-closure by more than one surgeon level could make the field non-mutually exclusive, but no such qualifier is printed.
- **Exact human question:** What is the analysis unit for the fascia-closing rows, and were multiple levels permitted per participant?
- **Status:** Pending Human Adjudication

## C004 — Skin-closing surgeon level totals exceed participant denominators without a multi-response qualifier

- **Category:** Denominator, proportion, or total inconsistency
- **Checker provenance:** Numeric consistency review, NC-4
- **Exact source locations:** [DOC-001 PDF p. 7, Table 2 continuation](<../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=7>)
- **Printed evidence:** With group denominators 411 and 410, consultant/registrar/senior-house-officer skin-closing counts are 115/214/96 and 102/241/73.
- **Rule and calculation:** The counts sum to 425 and 416, exceeding the participant denominators by 14 and 6; printed percentages sum to 103.5% and 101.5%.
- **Supported alternative:** More than one surgeon level may have participated in skin closure, but the table does not label this as a multi-response measure.
- **Exact human question:** Were multiple surgeon-level records allowed for one skin closure, and should the denominator or label be revised or qualified?
- **Status:** Pending Human Adjudication

## C005 — Control-arm mortality differs between participant flow and 30-day safety reporting

- **Category:** Cross-document numeric inconsistency
- **Checker provenance:** Cross-source consistency review
- **Exact source locations:** [DOC-001 PDF p. 3, Figure 1 footnote](<../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=3>); [DOC-001 PDF p. 8, Table 3](<../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=8>); [DOC-001 PDF p. 6, safety narrative](<../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=6>)
- **Printed evidence:** Figure 1 says 25 deaths were reported, 10 iNPWT and 15 control. Table 3 and the narrative report mortality within 30 days as 10/411 and 14/410, totaling 24.
- **Rule and calculation:** The intervention count agrees, but the control count differs by one and totals are 25 versus 24.
- **Supported alternative:** Figure 1 may include one control-arm death outside the 30-day Table 3 window; Figure 1 does not state its mortality window.
- **Exact human question:** Does the Figure 1 total include a post-day-30 death, and should its time window be stated or the counts reconciled?
- **Status:** Pending Human Adjudication

## C006 — Longitudinal quality-of-life covariance specification differs between SAP and final article

- **Category:** Statistical reporting inconsistency
- **Checker provenance:** Statistical pass 1, SP1-CAND-001 / S026
- **Exact source locations:** [DOC-002 PDF p. 26, SAP](<../../joi240145supp1_prod_1741627844.87412.pdf#page=26>); [DOC-001 PDF p. 4, Statistical Analysis](<../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=4>)
- **Printed evidence:** The SAP specifies an unstructured covariance structure and robust sandwich standard errors for the SF-12/EQ-5D longitudinal models; the final article specifies an independent covariance structure for the same outcome-model family.
- **Rule and calculation:** `Unstructured` and `independent` are distinct named covariance specifications. No arithmetic calculation is applicable.
- **Supported alternative:** A documented amendment, model diagnostic, convergence issue, or condensed reporting may explain the change, but none is supplied and the results supplement does not identify covariance or variance estimation.
- **Exact human question:** Which covariance and variance-estimation specification generated the published estimates and P values, and was the departure from the SAP documented?
- **Status:** Pending Human Adjudication

## C007 — Length-of-stay effect measure and model differ between SAP/protocol and final article

- **Category:** Measure, label, or scale inconsistency
- **Checker provenance:** Statistical pass 1, SP1-CAND-002 / S007
- **Exact source locations:** [DOC-002 PDF p. 25, SAP](<../../joi240145supp1_prod_1741627844.87412.pdf#page=25>); [DOC-004 PDF p. 39, protocol](<../../joi240145supp4_prod_1741627844.90412.pdf#page=39>); [DOC-001 PDF p. 4, Statistical Analysis](<../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=4>); [DOC-001 PDF p. 8, Table 3](<../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=8>)
- **Printed evidence:** SAP/protocol specify an adjusted mean difference from mixed-effects linear regression, or an unadjusted median difference if skewed. The final article states log transformation and reports adjusted ratios of geometric means (0.91 and 0.96).
- **Rule and calculation:** Mean difference, median difference, and ratio of geometric means are different effect measures/scales for the same endpoint. The printed final ratios are internally coherent with the final log-transformed model.
- **Supported alternative:** A prespecified or documented model-selection amendment could explain the change, but no rationale or amendment is supplied.
- **Exact human question:** Was the log-transformed ratio-of-geometric-means analysis a documented change, and which effect measure was intended for extraction and interpretation?
- **Status:** Pending Human Adjudication

## C008 — Australia-inclusive length-of-stay result differs from the stated UK-only analysis population

- **Category:** Analysis-unit or population inconsistency
- **Checker provenance:** Statistical pass 2, SP2-CAND-001 / S008
- **Exact source locations:** [DOC-002 PDF p. 18, SAP endpoint definition](<../../joi240145supp1_prod_1741627844.87412.pdf#page=18>); [DOC-002 PDF p. 25, SAP analysis population](<../../joi240145supp1_prod_1741627844.87412.pdf#page=25>); [DOC-004 PDF p. 24, protocol](<../../joi240145supp4_prod_1741627844.90412.pdf#page=24>); [DOC-001 PDF p. 1, abstract](<../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=1>); [DOC-001 PDF p. 8, Table 3](<../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=8>)
- **Printed evidence:** SAP/protocol specify that length of stay will be analysed/reported for UK patients only and that Australian-randomized participants are excluded from that endpoint analysis. The final article reports the UK-only result and also an Australia-inclusive ratio of geometric means of 0.96 (95% CI 0.88-1.06), P=.21.
- **Rule and calculation:** The analysis population is part of the identity of a reported result. The Australia-inclusive estimate uses a different population from the specified UK-only endpoint analysis. This is distinct from C007, which concerns the effect measure and model.
- **Supported alternative:** The all-country analysis may be an additional prespecified or documented analysis while the UK-only result remains the designated endpoint analysis, but the supplied package contains no amendment or rationale.
- **Exact human question:** Was the Australia-inclusive LOS analysis prespecified or documented, and how should its relationship to the UK-only endpoint be labelled for extraction and interpretation?
- **Status:** Pending Human Adjudication
