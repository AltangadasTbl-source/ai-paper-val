# Canonical numeric consistency review

Two disjoint fresh checker scopes are merged in full below.

# Numeric consistency checker — main and supplementary results pp.1–11

Fresh numeric reviewer runtime: 01a129ba-7aa6-77c0-9fab-ab97751545fe. Scope: DOC-001 physical pp.1–10; DOC-003 physical pp.1–11, R001–R017 and those page transcripts only; DOC-004 physical p.1 (no applicable outcome quantity). All three sources are REPORT by content. Reviewed QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md completely. Ownership limited to this checker part and relationships/parts/numeric_main.md. Sources and reusable assets preserved; no web or prior candidate/report conclusions used.

Completed all 97 stable numeric relationship bundles N001–N097 and every explicit component count/denominator/percentage, row/column/subgroup total, flow subtraction, matching abstract/primary value, descriptive statistic order and evident effect-measure identity in the assigned scope. Grouping in the inventory preserves every cell rather than limiting findings. Inferential intervals, tests and statistical methods have separate S-review coverage; the bleeding RR/CI/P pairing is explicitly referred for that coverage, not screened out by this numeric lane.

## Findings

### F-NUM-001

**Title:** Abstract and body give opposite signs for the primary favorable-outcome risk difference.

**Relationship IDs:** N010, supported by N009 and N011.

**Compared exact source locations and document roles:** REPORT DOC-001, [abstract Results, physical p.1](../../../jama_cooper_2018_oi_180132.pdf#page=1); REPORT DOC-001, [Primary Outcome paragraph, physical p.5](../../../jama_cooper_2018_oi_180132.pdf#page=5); REPORT DOC-001, [Table 2 primary favorable GOS-E row, physical p.7](../../../jama_cooper_2018_oi_180132.pdf#page=7). Printed pages 2211, 2215 and 2217. Source-native extraction and source-matched p.1/p.5 visual pages confirm the printed signs; no OCR normalization used.

**Printed inputs:** Abstract: favorable outcome H117 (48.8%) versus N111 (49.1%), risk difference **0.4%** (95% CI −9.4% to 8.7%), relative risk with hypothermia0.99 (0.82–1.19), P=.94. Body: same favorable counts and percentages, absolute risk difference **−0.4 percentage points** (−9.4 to 8.7), RR0.99 (0.82–1.19), P=.94. Table2: H117/240(48.8), N111/226(49.1), difference **−0.4** (−9.4 to8.7), RR0.99 (0.82–1.19), P=.94.

**Rule and reproduced calculation:** For H minus N, 100×(117/240−111/226)=−0.3650442478 percentage points, which rounds to−0.4. Permitting each count and denominator its half-unit interval gives the recomputed RD interval [−1.0049278342,+0.2746708328] percentage points. Abstract+0.4 has its half-unit interval [+0.35,+0.45], leaving a gap0.0753291672 and relative discrepancy0.0753291672/0.4=0.188322918>0.05. More directly, the two printed copies' half-unit intervals are [+0.35,+0.45] and [−0.45,−0.35], with gap0.70 percentage points and relative discrepancy0.70/0.40=1.75>0.05. Thus even the workflow's conservative precision rule does not reconcile the printed signs.

**Focus area:** B (estimate direction), with matching primary-result extraction.

**Proposed review domain:** statistical_results.

**Proposed relationship type / all relationships:** S_W / S_W. This is entirely within one REPORT document.

**Qualifying route:** Route A, category 2.

**Affected result or extracted value:** The signed absolute risk difference for favorable neurologic outcome (GOS-E5–8) at six months: the abstract's positive0.4 percentage points versus the body's/table's negative0.4 percentage points. The printed CI and P value imply no claimed statistical benefit; this issue concerns the signed point estimate taken into extraction.

**Why context does not resolve it:** Route A category2 covers a printed sign that changes effect direction even when the intended sign can be reconstructed from other numbers. A reader can extract the abstract's positive printed value. Counts, RR, the body and Table2 support the opposite sign, but do not remove the abstract's printed value.

**Source-grounded alternatives and missing definition:** The abstract might use N minus H while the body uses H minus N, or might intend an unsigned magnitude. Neither is stated. The unchanged asymmetric CI−9.4 to8.7 and explicitly H-referenced RR0.99 accompany the abstract point estimate, while a fully reversed contrast would also reverse those quantities. No production mechanism is inferred.

**Exact human question:** Which signed treatment contrast and risk-difference value should be extracted for the primary six-month favorable GOS-E outcome, and how should the abstract's+0.4% be read relative to the body/Table2's−0.4 percentage points?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| DOC-001 p.1 abstract Results versus p.5 Table1 sex | Abstract402 men(80.2%) among500; Table1 men207+194=401. Printed count-copy intervals[401.5,402.5] and[400.5,401.5] touch, gap0. Within abstract, 100×[401.5/500.5,402.5/499.5]=[80.219780,80.580581]% overlaps printed80.2 interval[80.15,80.25], gap0. The workflow precision rule screens the observation. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 p.5 Table1, normothermia Injury Severity Score | Median20.0 is below printed Q1=20.5 in IQR20.5–35.0. Medianinterval[19.95,20.05], Q1interval[20.45,20.55], gap0.40; relative discrepancy0.40/20.0=0.020≤0.05. This descriptive IQR is not an estimate confidence interval versus P value/test (Route A category1); the specified display rule screens this numerical ordering observation. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 p.4 Results target temperature versus same paragraph's27% never33°C | 71.5% reached33°C implies28.5% never under a common denominator, versus printed27%. Complement interval[28.45,28.55] and printed[26.5,27.5] yield gap0.95/27=0.035185≤0.05. eTable7 p.11 has primary-evaluable never65/240=27.083% and a different population from186/260 target attainment, supporting distinct denominators; numerical discrepancy does not meet precision threshold. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-003 p.8 eTable4, noradrenaline>15mcg/min days P value | Source-matched visual page prints P<.000; native locator wraps a trailing1 on the next row. Taken literally as display-zero small P, this is covered by the explicit display-zero P exclusion. No independent numeric-count contradiction found for this row. | ROUNDING_OR_DISPLAY_PRECISION |

## Completed reconciliation and handoff

Participant flow reconciles exactly:511−6−5=500; primary240+226=466; missing34=(16+4)+(13+1); mortality256+239=495 removes only consent withdrawal and lost follow-up; full protocol132+161=293. All baseline categorical denominators, mutually exclusive sex/CT/cause totals, explicit hypotension/hypoxia/ethanol denominators, and event percentages reconcile. Surgical and mass-lesion favorable subgroup numerators and denominators each partition the overall primary result. eTable7 sums to H240 and H117 favorable. eTable5 survivor proportions reconcile using186=240−54=117+69 and182=226−44=111+71. All97 inventory bundles are complete.

The Table2 bleeding point-RR comparison alone is within display precision: intracranial crudeRR1.172557 versus printed1.23 has rawrelative gapbelow5% and broader count-input overlap; extracranial crudeRR1.230769 versus printed1.17 is count-precision compatible. This does **not** screen out the distinct interval/P/method inconsistency: Table2's bleeding CI/P pairing and eTable6's P positions require the statistical/cross-source reviewers' independent checks. Those inferential relationships remain explicitly assigned and cannot be inferred as reconciled from this numeric check.

Counts:97 numeric bundles;1 finding;4 excluded observations. Limitations: figure-only quartiles/category shares are not printed as exact numbers; complete visual structures and contributor counts are retained without invented exact coordinates. No assigned scientific coverage gap. No candidate IDs, disposition or final correction assigned.
# Numeric consistency checker: supplementary results support shard

Fresh runtime: 01a129ba-a075-7e40-8815-b16cd5e4d1ad. Scope: DOC-003 physical pp.12–24, with DOC-001 physical pp.6–7 read only for matching non-ITT pneumonia claims. All locations are REPORT. Relationships N201–N262: 62 complete; findings: 1; excluded observations: 4. Read QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md completely. Discovery is independent of legacy candidates and reports. No sources or reused assets changed.

Direct review used pdftotext -layout stdout from the current PDF; visual flow and unusual-value confirmation used source-matched reusable rendered pages 12,16,17,18,20,22. CPU; no new rendering or OCR. The complete row values and arithmetic are in relationships/parts/numeric_support.md and the source-linked R018–R068 transcripts in extraction/support_results.md. Every baseline categorical row, event row, primary subgroup, sensitivity row and participant-flow component was reviewed. All flow figures reconcile, including crossovers and outcome availability. Every unadjusted displayed RR and the post hoc unadjusted OR has the stated identity within display precision. Inferential intervals, tests, adjusted model logic and plan matching remain separate assigned checker responsibilities; the exact unusual adjusted interval on physical p22 was communicated to the coordinator for statistical coverage.

## Findings

### F-NUM-101

**Title:** Count and percentage order does not reconcile in two as-treated normothermia CT categories.

**Relationships:** N224. Proposed relationship type: S_W; all relationships: S_W. **Focus area:** A, counts and denominators. **Proposed review domain:** statistical_results.

**Exact source locations and roles:** [REPORT, DOC-003 physical p18, eTable10, normothermia heading and CT Marshall classification rows V and VI](../../../joi180132supp2_prod.pdf#page=18). The column is headed “No. (%)”, normothermia “(n = 196)”. Evacuated mass lesion V is printed “34.7 (68)”; non-evacuated mass lesion VI is printed “1 (2)”. Other normothermia CT rows are “3 (1.5)”, “108 (55.1)”, “15 (7.7)”. Hypothermia cells use the heading's count-first order, including V “44 (33.1)” and VI “0 (0)”. Printed cells and heading were confirmed in the current PDF's native layout extraction and its source-matched page image.

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
