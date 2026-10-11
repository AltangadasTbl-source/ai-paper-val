# Numeric consistency checker — main and supplementary results pp.1–11

Fresh numeric reviewer runtime: 01a129ba-7aa6-77c0-9fab-ab97751545fe. Scope: DOC-001 physical pp.1–10; DOC-003 physical pp.1–11, R001–R017 and those page transcripts only; DOC-004 physical p.1 (no applicable outcome quantity). All three sources are REPORT by content. Reviewed QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md completely. Ownership limited to this checker part and relationships/parts/numeric_main.md. Sources and reusable assets preserved; no web or prior candidate/report conclusions used.

Completed all 97 stable numeric relationship bundles N001–N097 and every explicit component count/denominator/percentage, row/column/subgroup total, flow subtraction, matching abstract/primary value, descriptive statistic order and evident effect-measure identity in the assigned scope. Grouping in the inventory preserves every cell rather than limiting findings. Inferential intervals, tests and statistical methods have separate S-review coverage; the bleeding RR/CI/P pairing is explicitly referred for that coverage, not screened out by this numeric lane.

## Findings

### F-NUM-001

**Title:** Abstract and body give opposite signs for the primary favorable-outcome risk difference.

**Relationship IDs:** N010, supported by N009 and N011.

**Compared exact source locations and document roles:** REPORT DOC-001, [abstract Results, physical p.1](../../../../jama_cooper_2018_oi_180132.pdf#page=1); REPORT DOC-001, [Primary Outcome paragraph, physical p.5](../../../../jama_cooper_2018_oi_180132.pdf#page=5); REPORT DOC-001, [Table 2 primary favorable GOS-E row, physical p.7](../../../../jama_cooper_2018_oi_180132.pdf#page=7). Printed pages 2211, 2215 and 2217. Source-native extraction and source-matched p.1/p.5 visual pages confirm the printed signs; no OCR normalization used.

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
