# Numeric consistency review

Runtime agent: 01a129b8-259b-7a33-80f7-0f3ece30aeba; fresh numeric_consistency_reviewer, gpt-6.1-sol/medium. Scope: complete main and support quantitative maps, DOC-001 REPORT pp1–9, DOC-002 PLAN pp1–134, DOC-003 REPORT pp1–3. The stable inventory contains N001–N120, with all main Table1–3 and supplementary eTable1–2 count rows, participant flow, analysis totals, group/subgroup sums and matched occurrences. Two findings qualify; nine apparent observations are excluded below. No candidate IDs or adjudications are assigned.

QUALITY_CONTROL_SCOPE.md and review_contract.md were read completely. Numeric reproduction uses half-unit display intervals and the strict relative-discrepancy threshold above0.05. Counts are discrete: [n−0.5,n+0.5] contains only integer n. No raw data, invented method, custom Python, web or old scientific conclusions were used. Inferential compatibility and sample-size-method reproduction belong to the independent statistical review; planned definitions and outcome/analysis reporting comparisons belong to cross-source review. All risk-difference labels were checked against percentage subtraction; none evidently represents a ratio. Primary center-adjusted estimates are not treated as crude count differences.

Direct-source confirmation: Poppler25.03.0 `pdftotext -layout -f 4 -l 6 jama_jabre_2018_oi_180004.pdf -` and `pdftotext -layout -f 2 -l 3 joi180004supp2_prod.pdf -`; source-matched reusable layout/OCR and fresh complete page mappings. Table2 was freshly rendered with direct CPU Poppler25.03.0 `pdftoppm -f 6 -l 6 -singlefile -scale-to 2000 -png jama_jabre_2018_oi_180004.pdf .ai_paper_validation/review_1_6_2/preprocessing/numeric/main-p006` and visually inspected. Derivative engine/device: Poppler25.03.0/CPU. No unreadable count display remains.

## Findings

### F-NUM-001

The per-protocol ETI ROSC count and displayed percentage do not reconcile.

- **Exact source locations and roles:** REPORT [main article physical p6, printed784, Table2, Per-Protocol Analysis header and Return of spontaneous circulation row](../../../jama_jabre_2018_oi_180004.pdf#page=6). The header prints ETI n=943; that same row prints ETI377(30.0), BMV342(34.4), BMV n=995, and difference−5.6(95%CI−9.9 to−1.3). REPORT [p4 Figure and Baseline Characteristics](../../../jama_jabre_2018_oi_180004.pdf#page=4) separately corroborates PP943 and995 but supplies no competing PP ROSC percentage.
- **Printed inputs:**377/943 and30.0%; comparator342/995(34.4%); difference−5.6 percentage points. Relationship N082.
- **Rule and calculation:** A table count divided by its stated group denominator must reproduce its percentage under the display-precision rule. Discrete half-unit intervals for377 and943 reduce to singletons. Recomputed interval=[39.9787911%,39.9787911%]. Printed30.0% has interval[29.95%,30.05%]. Gap=9.9287911 percentage points; relative discrepancy=9.9287911/30.0=0.3309597>0.05. The count-derived risk difference100(342/995−377/943)=−5.6069318 percentage points overlaps printed−5.6 interval[−5.65,−5.55]. The printed displayed percentages instead give34.4−30.0=+4.4 percentage points, the opposite direction to the difference column.
- **Focus area:** A, counts and denominators; B, displayed direction agreement.
- **Proposed review domain:** statistical_results. Relationship S_W; all relationships S_W. Both conflicting locations are within REPORT Table2.
- **Qualifying route:** Route A, category3. The displayed percentage also changes magnitude and apparent direction under category2; one finding covers the same row.
- **Affected result or extracted value:** The per-protocol ETI ROSC percentage and direction of the BMV versus ETI ROSC comparison.
- **Why context does not resolve it:** This is a reproduced within-display count/denominator/percentage discrepancy in an always-register category. The reader may extract the explicit30.0% even though the counts and difference support a different percentage.
- **Alternatives and missing definition:**30.0% may be a substituted percentage, or377 or943 may belong to another population. No alternative denominator/population is defined for this row. The difference column corroborates the count-derived direction but does not adjudicate which printed input should be retained.
- **Exact human question:** What are the intended ETI per-protocol ROSC event count, denominator and percentage in Table2, and which values should be used when extracting this result?

### F-NUM-002

The per-protocol day28 survival difference does not reproduce the count-based risk-difference calculation that reproduces the other binary-result rows.

- **Exact source locations and roles:** REPORT [main article physical p6, printed784, Table2 Per-Protocol Analysis header and Survival at28d row](../../../jama_jabre_2018_oi_180004.pdf#page=6); comparator rows in that same REPORT table are ITT Survival at28d, Survival to hospital admission and ROSC, and PP Survival to hospital admission and ROSC. REPORT [p4 Figure and baseline narrative](../../../jama_jabre_2018_oi_180004.pdf#page=4) corroborates995/943 analysis totals. There is no PLAN conflict in this finding.
- **Printed inputs:** PP BMV54(5.4%),n=995; ETI51(5.4%),n=943; proportion difference BMV(%)−ETI(%)0.1 percentage points,95%CI−10 to9.7,P=.99. Relationship N074. Interval/test reproduction is reserved for the statistical review.
- **Rule and calculation:** Subtract count-derived survival proportions, as supported by the column label and reproducing comparator rows. Half-unit intervals for integer counts54,995,51,943 intersect the integers at their respective singletons. Recomputed difference interval=[0.0188642044,0.0188642044] percentage points. Printed0.1 interval=[0.05,0.15]. Gap=0.0311357956; relative discrepancy=0.0311357956/0.1=0.311357956>0.05. Comparator count differences are ITT survival0.119013(printed0.1), ITT admission−3.7030(−3.7), ITT ROSC−4.6607(−4.7), PP admission−4.04067(−4.0), and PP ROSC−5.60693(−5.6); their printed display intervals overlap the recomputed quantities or their relative residual is≤0.05. The two PP survival percentages individually reconcile:5.42714% and5.40827% round to5.4%.
- **Focus area:** C, statistical method logic; A, count-derived result.
- **Proposed review domain:** statistical_results. Relationship S_W; all relationships S_W.
- **Qualifying route:** Route A, category4.
- **Affected result or extracted value:** The per-protocol day28 survival absolute risk difference0.1 percentage points.
- **Why context does not resolve it:** This is a reproduced printed-result discrepancy under the calculation that reproduces the other binary rows. The intended calculation or printed estimate remains the human question even though both groups display5.4%.
- **Alternatives and missing definition:** The difference may use a separately estimated population/model, or a different printed estimate may be intended. No adjusted/model-based label or row-specific difference definition appears in Table2. Subtracting rounded5.4% copies alone allows a broad interval, but the exact displayed counts and denominators identify the fractions and the evident calculation used by the surrounding rows.
- **Exact human question:** Which calculation and analysis population produced the per-protocol survival-at28days difference0.1 percentage points in Table2, and does it use the displayed54/995 and51/943 counts?

## Excluded observations

Only apparent issues decided not to emit appear here; routine reconciled checks remain in the relationship inventory.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 pp1,5 | Abstract665women versus Table1 ITT332+332=664, with randomized2043 versus ITT2040 populations. Even treating these as copies, discrete residual1/665=0.001504≤0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p6 Table2 PP CPC1 ETI |34/943=3.60551% versus3.5%,printed interval[3.45,3.55];gap0.05551/3.5=0.01586≤0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p6 Table2 PP admission BMV |289/995=29.045226% versus29.1%,interval[29.05,29.15];gap0.004774/29.1=0.000164≤0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p4 Figure PP |The BMV PP23exclusions reconcile with priorITT1018−995;ETI80 reconcile with randomized1023−943, rather than ITT1022−943=79. One-person residual relative to80 is0.0125≤0.05; reason sums cannot be treated as unique-patient counts because overlap is explicit. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p4 Figure rescue |55failure+100regurgitation=155 versus146rescue patients initially appears discrepant, but multiple reasons per patient are explicitly permitted. | NOT_REPRODUCED |
| REPORT DOC-001 p4;DOC-003 p3 crossover |Moving155fromITT1018/1022 yields863/1177 versus printed863/1174; denominator residual3/1174=0.00256≤0.05. Modified success total86 versus87 differs by1/87=0.01149≤0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p4 post-hoc pauses |Difference11is described in seconds although27and16are numbers of pauses. Immediate wording and subtraction identify the count comparison; no numeric input changes. | NOTATION_OR_TYPOGRAPHY |
| PLAN DOC-002 pp24,79 recruitment tables |5patients/month/centre×24months×20centres=2400versus target2000. These are approximate prospective recruitment-rate/calendar quantities; the statistical enrollment target is consistently2000. | PERIPHERAL_COMPARISON |
| REPORT DOC-001 p4 primary outcome |Hierarchical center-adjusted difference0.05% differs from crude44/1018−43/1022=0.11475%; it is explicitly a separate random-effect model. | MODEL_VERSUS_CRUDE |

## Limitations and completion

Numeric scientific coverage is complete:120 stable relationships,2 findings,9 excluded observations,0 unresolved source-reading gaps. No additional numeric shard is needed. Printed result counts are not a raw-data audit; overlapping PP exclusion reasons do not support unique-person reconstruction. The algorithm for inferential CIs and primary power simulations is not supplied sufficiently for this numeric lane to reproduce them; the statistical lane owns those methods. Historical rendering-engine provenance and absent direct OCR are recorded in tooling/assets; source-matched extraction and current direct PDF rendering cover this lane. Sources and reused assets were preserved.
