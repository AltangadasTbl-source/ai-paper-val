# Numeric Consistency Review

Runtime: /root/numeric_checker. Model: gpt-6.1-sol. Reasoning effort: medium. Start mode: FRESH_SPAWN. Scope: all39 supplied PDF pages (main12 REPORT;results supplement20 REPORT;protocol7 PLAN), all116 main mapper records and every support map key. Completed63 stable grouped N relationships,48 baseline categorical/missing rows with142 count/percentage pairs,all24 eTable3 pairs,all8 event-rate differences,all8 Table2 risk differences,all8 five-time risk sets,all30 observation/patient rows,and all10 medication denominators. The full numeric inventory is [numeric_relationship_inventory.md](../relationships/numeric_relationship_inventory.md).

Read QUALITY_CONTROL_SCOPE.md and workflow1.6.2 review contract completely. Source PDFs remain the authority. Main Table2 finding was confirmed against direct PDFp7 Poppler26.01.0 layout extraction and visually against the corresponding source render. CPU;no OCR,fallback,web,or old scientific conclusions used. No source or reused asset changed. One consolidated finding;four excluded observations. Statistical test compatibility has a separate complete fresh review stage and is not replaced by these numeric arithmetic checks.

## Findings

### F-NUM-001

**Title:** Five Table2 individual-outcome absolute risk differences do not reproduce from the displayed8-year risks.

**Exact compared locations and document roles:** REPORT main article [PDFp7,Table2](../../../jama_aminian_2019_oi_190103.pdf#page=7),heart failure,coronary artery disease,cerebrovascular disease,nephropathy,and atrial fibrillation rows:Metabolic Surgery and Nonsurgical Control cumulative-incidence columns versus Absolute8-Year Risk Difference column and footnotea. REPORT main article [PDFp4,Statistical Analysis](../../../jama_aminian_2019_oi_190103.pdf#page=4) specifies Kaplan–Meier cumulative incidence and bootstrapped8-year absolute risk differences. REPORT results supplement [PDFp7,eTable5](../../../joi190103supp1_prod.pdf#page=7) corroborates the five displayed group risks;it is corroboration,not a separate conflicting source relationship.

**Focus area:** B (estimate logic),with arithmetic difference identity under C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **All relationships:** S_W.

**Qualifying route:** Route A, category4.

**Printed inputs,rule and calculation:** Footnotea defines the difference as nonsurgical control−metabolic surgery. The same difference method reproduces the primary47.7−30.8=16.9,secondary27.6−17.0=10.6,and mortality17.8−10.0=7.8 rows. All inputs and differences below print one decimal;allow each risk ±0.05 percentage points and each printed difference ±0.05. Each difference interval is [control−surgery−0.10,control−surgery+0.10]. All units are percentage points.

| Outcome | Surgery risk | Control risk | Printed ARD(95%CI) | Control−surgery | Recomputed interval | Printed ARD interval | Remaining gap | Relative discrepancy |
|---|---:|---:|---|---:|---|---|---:|---:|
| Heart failure |6.8|18.9|12.9(10.4–15.1)|12.1|[12.00,12.20]|[12.85,12.95]|0.65|0.0503876|
| Coronary artery disease |7.9|11.6|4.2(1.9–6.8)|3.7|[3.60,3.80]|[4.15,4.25]|0.35|0.0833333|
| Cerebrovascular disease |4.1|5.6|1.8(−0.03 to3.4)|1.5|[1.40,1.60]|[1.75,1.85]|0.15|0.0833333|
| Nephropathy |6.1|16.3|11.1(8.8–13.6)|10.2|[10.10,10.30]|[11.05,11.15]|0.75|0.0675676|
| Atrial fibrillation |7.9|13.6|6.5(4.4–8.7)|5.7|[5.60,5.80]|[6.45,6.55]|0.65|0.1000000|

The relative discrepancy divides the remaining gap by the absolute printed ARD. Every value exceeds0.05;heart failure remains just above the threshold after the complete half-unit calculation. The displayed method that reproduces three other rows does not reproduce these five rows. Consolidate these repeated failures of the same explicitly defined difference column as one reporting issue.

**Affected result or extracted value:** The8-year absolute reduction in each of the five individual outcomes;a data extractor could use12.9,4.2,1.8,11.1,and6.5 percentage points or the displayed group-risk differences12.1,3.7,1.5,10.2,and5.7. The reported ARD interval limits are retained as printed and cannot be reconstructed from marginal group confidence limits.

**Why context does not resolve it:** This is route A category4:a printed result does not reproduce under the difference method that reproduces other rows of the same display. Footnotea supplies orientation and bootstrap CI construction,but supplies no alternate point-estimate definition for these five rows. The supplied description does not identify which extraction value applies. The known point estimates and labelled risk differences are compared,not adjusted Cox HRs against crude ratios.

**Source-grounded alternatives and missing definition:** Bootstrap resampling is stated for95%CIs;an unstated bootstrap mean,alternate risk-set standardization,or another point-estimate construction might explain the difference column,but the source does not state such a distinction. Individual baseline-history exclusions exist,but both group risks and their difference occupy the same individual-outcome rows. The observed discrepancy does not establish its production mechanism. No preferred analysis or numerical correction is proposed.

**Exact human question:** What point-estimate definition produced the five individual-outcome absolute8-year risk differences,and which group risks and analysis populations should be used to interpret or extract them?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT [main p5, Table1, unmatched men](../../../jama_aminian_2019_oi_190103.pdf#page=5) | 18895/39267 produces48.1193% versus48.2%. Half-unit input and output intervals leave a relative gap0.0005981≤0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT [results supplementp5,eTable3,biguanides surgery](../../../joi190103supp1_prod.pdf#page=5) |1530/2287 produces66.8999% versus67.9%. Half-unit input interval[66.863388,66.936366]%,printed interval[67.85,67.95]%;gap0.913634/67.9=0.0134556≤0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT [mainp6,Table1 footnoteb](../../../jama_aminian_2019_oi_190103.pdf#page=6) versus signed difference columns [p5](../../../jama_aminian_2019_oi_190103.pdf#page=5) andp6 | Footnote says absolute value,while columns retain signed surgery−control differences. The displayed sign convention is evident from paired rows (women/men;Ohio/Florida),without changing a clinical estimate or a count extraction. | TERMINOLOGY_OR_WORDING |
| REPORT [supplementp14,eTable10,year0controls](../../../joi190103supp1_prod.pdf#page=14) versus main [p1 cohort](../../../jama_aminian_2019_oi_190103.pdf#page=1) |11433 medication denominator versus11435 full matched controls;copy half-unit intervals[11432.5,11433.5] and[11434.5,11435.5] leavegap1/11435=0.00008745≤0.05. | ROUNDING_OR_DISPLAY_PRECISION |

## Reconciled checks and bounded limitations

Participant flow subtraction/addition and1:5 matched totals reconcile. Exclusion reasons overlap explicitly. All Table1 category totals and count/percentage pairs,including baseline and missing-data rows,meet display precision. eTable3 has no qualifying within-display count discrepancy after the stated threshold. All eTable4 cause-specific rate differences reproduce;rates are not cumulative proportions. Figure risk sets decrease over time and begin at Table2 denominators. Nephropathy extra baseline exclusions are supplied in PLANp5. Thirty eTable9 observation/patient tuples respect repeated-measure and group-size constraints. Ten medication denominators decrease. Postoperative counts and percentages reconcile. Longitudinal pounds/kilograms and their intervals reconcile conversion precision;20.3kg versus29.1−8.7kg permits overlapping display intervals. No raw participant data,bootstrap draws,group-specific spline inputs,or numeric sensitivity plot point labels are supplied;these bounded absent inputs do not leave any assigned count/display unchecked. Every registered finding has source-confirmed arithmetic rather than inferred raw-data behavior.

## Numeric derivative record

Direct engine:pdftotext Poppler26.01.0;deviceCPU. Commands:`pdftotext -layout -f7 -l7 jama_aminian_2019_oi_190103.pdf` to preprocessing/numeric-main-p007.txt;`pdftotext -layout -f5 -l6 jama_aminian_2019_oi_190103.pdf` to preprocessing/numeric-main-p005-006.txt;`pdftotext -layout -f5 -l7 joi190103supp1_prod.pdf` to preprocessing/numeric-support-p005-007.txt. Actual commands use separated option values as recorded in the session. Source-matched reusable p7 image confirmed all5 affected rows visually. No fresh rendering or OCR derivative produced.
