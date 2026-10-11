# Stable Candidate Ledger

All eight distinct pre-ledger observations from the complete numeric, cross-source, and statistical-pass-1 lanes are registered below. Duplicates were merged only when they concern the same printed values/statements, comparator, and consistency rule. IDs are stable and every candidate remains **Pending Human Adjudication**.

## C001 — Intraoperative adverse-event threshold definitions differ within the main article

- **Candidate statement:** The methods and Table 3 footnotes print different operational criteria for the same named intraoperative hypoxemia and hypotension outcomes.
- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** [DOC-001 PDF p. 3](../../jama_bluth_2019_oi_190055_16092.pdf#page=3); [DOC-001 PDF p. 10](../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- **Printed evidence:** P. 3 defines hypoxemia as SpO2 at or below 92% for more than 1 minute and hypotension as systolic pressure below 90 mm Hg for more than 2 minutes. P. 10 adds baseline-dependent alternative criteria (greater than 5% SpO2 decline when already below 92%; greater than 10-mm-Hg systolic decline when already below 90) while omitting the durations.
- **Consistency rule:** The same named reported outcome should have one operational threshold or an explicit statement distinguishing a short definition from a complete/superseding definition.
- **Direct observation and diagnostic reasoning:** The threshold sets are textually nonidentical; no model or raw-data inference is used. The alternative criteria could change the reported numerators.
- **Alternative source-grounded interpretation:** P. 3 may be intentionally abbreviated and p. 10 may be the complete definition, or the footnote may describe a rescue convention. The package does not say which.
- **Remaining human question:** Which threshold set generated the reported Table 3 counts, and should the other location be reconciled or identified as abbreviated?
- **Provenance:** Numeric checker PROV-N006-01; canonical relationship N006.
- **Status:** Pending Human Adjudication

## C002 — White-blood-cell magnitude and unit are on incompatible printed scales

- **Candidate statement:** Table 1 pairs white-blood-cell values in the thousands with a `×10^9/L` unit.
- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** [DOC-001 PDF p. 6](../../jama_bluth_2019_oi_190055_16092.pdf#page=6); [DOC-005 PDF p. 20](../../joi190055supp4_prod_16092.pdf#page=20).
- **Printed evidence:** DOC-001 prints `White blood cells, ×10^9/L` with 8224 (2346) and 8347 (2758). DOC-005 defines leukocyte thresholds as below 4000 or above 12000 cells/mm3.
- **Consistency rule:** A laboratory magnitude and unit must use the same scale.
- **Calculation:** `8224 cells/mm3 = 8.224 ×10^9/L`; conversely, `8224 ×10^9/L = 8,224,000 cells/mm3`. Rounding cannot bridge the factor-of-1000 scale difference.
- **Alternative source-grounded interpretation:** The intended unit may be cells/mm3, or the intended displayed values under `×10^9/L` may be approximately 8.224 and 8.347.
- **Remaining human question:** Should the unit be changed, or should the values be rescaled?
- **Provenance:** Numeric checker PROV-N015-01; canonical relationship N015.
- **Status:** Pending Human Adjudication

## C003 — Per-protocol effect estimates are generically labeled and do not reproduce as crude ratios

- **Candidate statement:** Supplement eTable 8 labels its column only `Effect Estimate 95% CI`, and several estimates do not reproduce as crude risk ratios or odds ratios from the displayed exact counts and denominators.
- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** [DOC-005 PDF p. 29](../../joi190055supp4_prod_16092.pdf#page=29); [DOC-001 PDF p. 9](../../jama_bluth_2019_oi_190055_16092.pdf#page=9); [DOC-001 PDF p. 10](../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- **Printed evidence:** PPC is 186/917 versus 209/912 with effect 0.92; pleural effusion is 38/917 versus 18/912 with effect 1.37; cardiopulmonary edema is 15/917 versus 7/912 with effect 1.36. The analogous main table labels its effect column `Risk Ratio`.
- **Consistency rule:** A reported effect estimate needs an identifiable measure/reference/model, particularly when it does not equal an obvious ratio of the displayed exact inputs.
- **Calculation:** Diagnostic crude high/low risk ratios from the exact printed counts are 0.885100, 2.099600, and 2.131173; crude odds ratios are 0.855864, 2.147137, and 2.149984. None matches 0.92, 1.37, or 1.36 at displayed precision. These diagnostics do not assert an error in an unidentified adjusted model.
- **Alternative source-grounded interpretation:** The estimates may be adjusted or model-based and therefore valid, but the table does not identify their estimand, direction, model, or adjustment set.
- **Remaining human question:** What effect measure and model produced eTable 8, and should the table/footnote name it?
- **Provenance:** Numeric checker PROV-N048-01; canonical relationship N048/S025. Statistical pass 1 retained the issue as definition-limited rather than independently registering it.
- **Status:** Pending Human Adjudication

## C004 — eFigure 11 body text assigns mortality statistics to extra-pulmonary complications

- **Candidate statement:** The eFigure 11 title and numerical result identify 5-day mortality, while its body sentence labels the rate as postoperative extra-pulmonary complications.
- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** [DOC-005 PDF p. 41](../../joi190055supp4_prod_16092.pdf#page=41); [DOC-005 PDF p. 40](../../joi190055supp4_prod_16092.pdf#page=40); [DOC-001 PDF p. 10](../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- **Printed evidence:** EFigure 11 is titled probability of death and prints 0.5% versus 0.3%, HR 1.67 (0.40-6.97), P=.484 for 5-day mortality, but its body sentence names extra-pulmonary complications. DOC-001 prints matching mortality values; eFigure 10 separately prints PEPC 16.9% versus 15.2%, HR 1.12 (0.89-1.39), P=.314.
- **Consistency rule:** A figure's body outcome label must agree with its title, measure label, and matched numerical result.
- **Direct observation and diagnostic reasoning:** Mortality and PEPC are distinct named outcomes with distinct supplied statistics; no tolerance or model assumption is needed.
- **Alternative source-grounded interpretation:** The PEPC phrase may be copied from eFigure 10 while the mortality title/statistics are intended; plotted curves could not be visually inspected in the current environment.
- **Remaining human question:** Is the eFigure 11 body label a production carryover, and does the plotted curve also represent mortality?
- **Provenance:** Numeric PROV-N054-01, cross-source XS-003, and statistical pass-1 P1-STAT-004 merged; canonical N054/S031.
- **Status:** Pending Human Adjudication

## C005 — Abstract hypoxemia confidence interval loses the negative sign on its upper endpoint

- **Candidate statement:** The abstract and Table 3 print opposite signs for the upper endpoint of the same hypoxemia difference confidence interval.
- **Category:** Cross-document numeric inconsistency
- **Exact source locations:** [DOC-001 PDF p. 1](../../jama_bluth_2019_oi_190055_16092.pdf#page=1); [DOC-001 PDF p. 9](../../jama_bluth_2019_oi_190055_16092.pdf#page=9).
- **Printed evidence:** The abstract prints 5.0% versus 13.6%, a high-minus-low difference of -8.6%, 95% CI -11.1% to 6.1%, and P<.001. Table 3 supplies the matched exact fractions 49/989 and 134/987, the same rounded percentages and difference, and 95% CI -11.1% to -6.1%.
- **Consistency rule:** Repeated displays of the same population, outcome, contrast, estimate, and interval should agree; endpoint sign is not a rounding difference.
- **Calculation:** `5.0% - 13.6% = -8.6%`. The table's wholly negative interval contains the estimate and is directionally compatible with P<.001; the abstract's positive upper endpoint crosses zero.
- **Alternative source-grounded interpretation:** The abstract may have lost a typographic minus sign, or the table may be the intended source; the package supplies no correction record.
- **Remaining human question:** Which upper endpoint is intended in the abstract and final production record?
- **Provenance:** Cross-source XS-001; relationships N033/S011.
- **Status:** Pending Human Adjudication

## C006 — Matched synthetic-colloid-use rows print different P values

- **Candidate statement:** The main and supplement repeat the same binary synthetic-colloid-use result but print P=.09 and P=.10.
- **Category:** Cross-document numeric inconsistency
- **Exact source locations:** [DOC-001 PDF p. 8](../../jama_bluth_2019_oi_190055_16092.pdf#page=8); [DOC-005 PDF p. 24](../../joi190055supp4_prod_16092.pdf#page=24).
- **Printed evidence:** Both report 74/989 (7.5%) versus 56/987 (5.7%). DOC-001 Table 2 prints difference 1.8% (95% CI -0.3 to 4.0), P=.09; DOC-005 eTable 3 prints P=.10.
- **Consistency rule:** A matched population/contrast/binary result printed to the same P-value precision should agree unless different tests are identified.
- **Calculation:** Direct comparison `.09 ≠ .10`; no tail probability was reconstructed.
- **Alternative source-grounded interpretation:** Different undocumented tests or rounding pipelines may have been used; otherwise one display may be a transcription difference.
- **Remaining human question:** Were different tests intended, and which displayed P value follows the prespecified analysis?
- **Provenance:** Cross-source XS-002 and statistical pass-1 P1-STAT-003 merged; relationships N026/N043/S020.
- **Status:** Pending Human Adjudication

## C007 — Neuromuscular-monitoring percentages do not match their printed fractions

- **Candidate statement:** Table 2's monitoring percentages do not reconcile with the printed numerators and denominators.
- **Category:** Denominator, proportion, or total inconsistency
- **Exact source locations:** [DOC-001 PDF p. 8](../../jama_bluth_2019_oi_190055_16092.pdf#page=8).
- **Printed evidence:** Monitoring is printed as 632/982 (64.9%) versus 651/984 (67.7%), with difference -1.8% (-6.0 to 2.4), P=.40.
- **Consistency rule:** Each `No./total No. (%)` percentage should equal its printed fraction to one-decimal rounding.
- **Calculation:** `632/982×100=64.36%` (64.4%), not 64.9%; `651/984×100=66.16%` (66.2%), not 67.7%. The count-derived difference is -1.80 points, while printed percentages differ by -2.8 points.
- **Alternative source-grounded interpretation:** One or more printed count, denominator, or percentage values may be transcribed incorrectly; the difference appears count-derived.
- **Remaining human question:** Which fields are authoritative, and should counts, denominators, percentages, and difference be reconciled?
- **Provenance:** Statistical pass-1 P1-STAT-001; relationships N025/S006.
- **Status:** Pending Human Adjudication

## C008 — Neuromuscular-reversal percentages do not match their printed fractions

- **Candidate statement:** Table 2's reversal percentages do not reconcile with the printed numerators and denominators.
- **Category:** Denominator, proportion, or total inconsistency
- **Exact source locations:** [DOC-001 PDF p. 8](../../jama_bluth_2019_oi_190055_16092.pdf#page=8).
- **Printed evidence:** Reversal is printed as 724/982 (74.3%) versus 723/984 (75.2%), with difference 0.2% (-3.6 to 4.1), P=.90.
- **Consistency rule:** Each `No./total No. (%)` percentage should equal its printed fraction to one-decimal rounding.
- **Calculation:** `724/982×100=73.7271%` (73.7%), not 74.3%; `723/984×100=73.4756%` (73.5%), not 75.2%. The exact fraction-derived difference is +0.2515 points, which ordinarily rounds to +0.3 rather than the printed +0.2; the printed percentages imply -0.9 points.
- **Alternative source-grounded interpretation:** One or more printed count, denominator, percentage, or difference values may be transcribed differently from the analysis output; alternatively, the difference may be model-based or use unprinted inputs.
- **Remaining human question:** Which fields are authoritative, and should counts, denominators, percentages, and difference be reconciled?
- **Provenance:** Statistical pass-1 P1-STAT-002; relationships N025/S006.
- **Status:** Pending Human Adjudication

## Registration completeness

**Stable candidate count:** 8. Stable IDs: C001, C002, C003, C004, C005, C006, C007, C008. No candidate was registered solely from a display-zero P value.
