# Numeric consistency checker: supplementary results support shard

Fresh runtime: 01a129ba-a075-7e40-8815-b16cd5e4d1ad. Scope: DOC-003 physical pp.12–24, with DOC-001 physical pp.6–7 read only for matching non-ITT pneumonia claims. All locations are REPORT. Relationships N201–N262: 62 complete; findings: 1; excluded observations: 4. Read QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md completely. Discovery is independent of legacy candidates and reports. No sources or reused assets changed.

Direct review used pdftotext -layout stdout from the current PDF; visual flow and unusual-value confirmation used source-matched reusable rendered pages 12,16,17,18,20,22. CPU; no new rendering or OCR. The complete row values and arithmetic are in relationships/parts/numeric_support.md and the source-linked R018–R068 transcripts in extraction/support_results.md. Every baseline categorical row, event row, primary subgroup, sensitivity row and participant-flow component was reviewed. All flow figures reconcile, including crossovers and outcome availability. Every unadjusted displayed RR and the post hoc unadjusted OR has the stated identity within display precision. Inferential intervals, tests, adjusted model logic and plan matching remain separate assigned checker responsibilities; the exact unusual adjusted interval on physical p22 was communicated to the coordinator for statistical coverage.

## Findings

### F-NUM-101

**Title:** Count and percentage order does not reconcile in two as-treated normothermia CT categories.

**Relationships:** N224. Proposed relationship type: S_W; all relationships: S_W. **Focus area:** A, counts and denominators. **Proposed review domain:** statistical_results.

**Exact source locations and roles:** [REPORT, DOC-003 physical p18, eTable10, normothermia heading and CT Marshall classification rows V and VI](../../../../joi180132supp2_prod.pdf#page=18). The column is headed “No. (%)”, normothermia “(n = 196)”. Evacuated mass lesion V is printed “34.7 (68)”; non-evacuated mass lesion VI is printed “1 (2)”. Other normothermia CT rows are “3 (1.5)”, “108 (55.1)”, “15 (7.7)”. Hypothermia cells use the heading's count-first order, including V “44 (33.1)” and VI “0 (0)”. Printed cells and heading were confirmed in the current PDF's native layout extraction and its source-matched page image.

**Printed inputs, rule and calculation:** Under the displayed count-first heading, the printed percentage must agree with 100×count/196, and the five mutually exclusive CT category counts must total196. Literal V reading yields100×34.7/196=17.7041%, versus printed68%; literal VI reading yields100×1/196=0.5102%, versus printed2%. Literal count sum is3+108+15+34.7+1=161.7 versus 196.

**Display precision:** For V, count34.7 gives[34.65,34.75], denominator196 gives[195.5,196.5], and printed percentage68 gives[67.5,68.5]. Recomputed percentage interval is[17.633588,17.774936]%. The interval gap is49.725064 percentage points; relative discrepancy49.725064/68=0.731251, above 0.05. For VI, count1 gives[0.5,1.5], denominator interval as above, printed percentage2 gives[1.5,2.5]. Recomputed percentage interval is[0.254453,0.767263]%; gap 0.732737 percentage points; relative discrepancy0.732737/2=0.366368, above 0.05. For the literal CT column total, the five count intervals sum to[159.65,163.75], which does not overlap196's[195.5,196.5]; gap31.75/196=0.161990, above 0.05. Integer counts are discrete in reality; allowing continuous half units here is conservative and still reproduces the discrepancy.

**Qualifying route:** Route A, category 3. The same transposed-order pattern affects both adjacent rows and is consolidated as one finding. The resulting literal magnitudes also meet category 2, but category 3 is the primary qualifying route.

**Affected result or extracted value:** The as-treated normothermia baseline numbers and proportions with evacuated and non-evacuated intracranial mass lesions. A literal extraction would take count34.7 and68% for V and count1 and2% for VI, whereas reversing each cell gives different counts and proportions.

**Why context does not resolve it:** Route A, category 3 always registers a reproduced count/denominator/percentage discrepancy, including in baseline displays. Immediate context suggests a reversed order, but reconstructing an intended reading does not remove the displayed numeric inconsistency. The column heading and neighboring rows retain count-first order.

**Alternatives and missing definition:** Reading the two cells as percentage(count), namely34.7%(68) and1%(2), would give100×68/196=34.6939% and100×2/196=1.0204%, and the resulting counts3+108+15+68+2=196 would reconcile. The source does not state a row-specific reversal of the column's presentation convention. This reconstruction is an alternative interpretation, not a proposed final correction. No external evidence is needed.

**Exact human question:** For the normothermia Marshall V and VI cells in eTable10, which participant counts and percentages should be extracted, and was a percentage-first order intended for those two cells despite the “No. (%)” heading?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-003 p21 eTable12 mostlikely H cell, N243 | Literal 133/260=51.1538% would ordinarily round to51.2 rather than printed 51.1. Allowing printed integer half units gives[50.8637,51.4451]%, overlapping printed 51.1 interval[51.05,51.15]; gap 0. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-003 pp14,19,22 adjusted rows, N207,N227,N247 | Severity-adjusted RR 1.04 and1.11 or time-adjusted OR 0.95 need not equal crude effects from event counts. Counts alone cannot establish an adjusted label/identity discrepancy; modeled estimates are explicitly identified. | MODEL_VERSUS_CRUDE |
| REPORT DOC-003 pp13–14 and18–19 mortality denominators, N208,N209,N228,N229 | Normothermia death denominators 160/195 are one below baseline 161/196. There is no printed claim of complete mortality ascertainment for every baseline participant; treating baseline totals as mandatory death denominators would require an unsupported completeness assumption. Each displayed count/denominator/percentage reconciles. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-003 p15 eFigure4 axis, N217 | Time-bin label37–41 is followed by43–48 among six-hour positions. The apparent axis-label slip changes no reported count, estimate, interval or effect direction and the timeline reading is evident. | NOTATION_OR_TYPOGRAPHY |

## Limitations and handoff

No assigned scientific unit omitted; physical p24 references have no applicable numeric relationship. Exact graph coordinates and participant-level covariates are not supplied; no values were manufactured. All 62 numeric relationships complete; F-NUM-101 ready for independent inclusion screening. Four excluded observations retain their single reason codes for statistical pass 2 and audit review. No C IDs, adjudications or proposed dispositions assigned.
