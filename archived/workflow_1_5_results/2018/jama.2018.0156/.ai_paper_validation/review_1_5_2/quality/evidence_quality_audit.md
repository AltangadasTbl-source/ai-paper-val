# Evidence Quality Audit

## Audit scope and evidence boundary

This canonical audit uses only the current Workflow 1.5.2 artifacts and the three supplied source PDFs. It does not use `legacy_previous_run_20260824T015518Z/`, any previous candidate set, checker output, recheck, quality audit, final report, extracted text, or prior OCR as evidence or as a discovery boundary. No web source was used. The current run's freshly generated native text, layout text, rendered pages, and targeted CPU OCR for DOC-002 PDF pp. 52 and 103 were reviewed as transcription aids; the direct PDFs and fresh renderings remain the evidence authority. Prior OCR reuse is zero.

Discovery was relationship-complete rather than candidate-count-driven. No top-N rule, review queue, candidate cap, severity rank, or expected finding count controlled mapping, checking, registration, recheck, or this audit.

## Complete mechanical coverage audit

| Audit domain | Current scope | Audit result |
|---|---:|---|
| Direct sources | 3/3 | DOC-001 has 9 pages, DOC-002 has 134 pages, and DOC-003 has 3 pages. SHA-256 verification against `source_hashes_before.sha256` succeeds for all three sources. |
| Direct-source units | 146/146 | Every source row has `Reusable units = 0`, `Fresh-required units = Total units`, `Mapped units = Total units`, and `COMPLETE`: 9/9, 134/134, and 3/3. |
| Numeric relationships | 51/51 | The canonical inventory is gap-free from N001 through N051. `numeric_consistency.md` explicitly completes every relationship and emits three source-grounded signals without a count boundary. |
| Statistical relationships | 38/38 per pass | The canonical inventory is gap-free from S001 through S038. Both statistical passes contain one explicit completion row for every S ID. |
| Cross-source review | 89/89 | N001-N051 and S001-S038 are covered; five cross-source signals are reported, with matched populations, time points, contrasts, measures, versions, and limitations retained. |
| Stable candidates | 8/8 | The ledger set is exactly C001-C008. The eight IDs are preserved without deletion, merging, ranking, renumbering, suppression, severity, or scientific disposition. |
| Evidence recheck | 8/8 | The recheck set is exactly C001-C008. Every ID has its cited location, printed evidence, comparator, rule, reproduced calculation or logical comparison, available and missing inputs, alternative interpretation, inference boundary, human question, and `Pending Human Adjudication` status. |
| Statistical pass 2 | 38/38 plus 8/8 | Every S relationship and every rechecked stable ID was revisited. The genuinely new candidate count is 0. |
| Coverage manifest | 22/22 rows | Every row has exactly one undecorated relative artifact path. The 20 `COMPLETE` rows resolve; the quality row is `ASSIGNED` while this artifact is being written, and the report row is `PENDING`. |
| Agent execution manifest | 12/12 rows | The coordinator and all currently manifested agents appear once, with one ID, model, effort, start mode, and artifact. Every manifested artifact resolves. |
| Display-zero rule | 8/8 candidates compliant | No mapped relationship or candidate is based on `P = 0`, `p = 0.000`, or equivalent. The `P<.001` displays are inequalities, not display zero. No independent-contradiction field is required. |

The canonical relationship counts are 51 numeric and 38 statistical, not the stale counts in the superseded audit. The ledger, recheck, both statistical passes, numeric checker, and cross-source checker consistently use the current ID scopes.

## Coverage-manifest row and artifact-path audit

| Row scope | Artifact path | Status/path audit |
|---|---|---|
| Source inventory | `source_inventory.md` | COMPLETE; one path; resolves. |
| Evidence assets | `evidence_asset_inventory.md` | COMPLETE; one path; resolves. |
| Main evidence map, DOC-001 pp. 1-9 | `extraction/main_quantitative_evidence.md` | COMPLETE; one path; resolves. |
| Main numeric part | `relationships/parts/main_numeric_relationships.md` | COMPLETE; one path; resolves. |
| Main statistical part | `statistics/parts/main_statistical_relationships.md` | COMPLETE; one path; resolves. |
| Canonical N001-N051 inventory | `relationships/numeric_relationship_inventory.md` | COMPLETE; one path; resolves. |
| Canonical S001-S038 inventory | `statistics/relationship_inventory.md` | COMPLETE; one path; resolves. |
| Support A evidence, DOC-002 pp. 1-67 | `extraction/parts/support_a_quantitative_evidence.md` | COMPLETE; one path; resolves. |
| Support A numeric part | `relationships/parts/support_a_numeric_relationships.md` | COMPLETE; one path; resolves. |
| Support A statistical part | `statistics/parts/support_a_statistical_relationships.md` | COMPLETE; one path; resolves. |
| Support B evidence, DOC-002 pp. 68-134 and DOC-003 pp. 1-3 | `extraction/parts/support_b_quantitative_evidence.md` | COMPLETE; one path; resolves. |
| Support B numeric part | `relationships/parts/support_b_numeric_relationships.md` | COMPLETE; one path; resolves. |
| Support B statistical part | `statistics/parts/support_b_statistical_relationships.md` | COMPLETE; one path; resolves. |
| Canonical support evidence | `extraction/support_quantitative_evidence.md` | COMPLETE; one path; resolves. |
| Numeric checks, N001-N051 | `checkers/numeric_consistency.md` | COMPLETE; one path; resolves. |
| Statistical pass 1, S001-S038 | `checkers/statistical_pass_1.md` | COMPLETE; one path; resolves. |
| Cross-source checks, N001-N051 and S001-S038 | `checkers/cross_source_consistency.md` | COMPLETE; one path; resolves. |
| Candidate registration, C001-C008 | `candidate_ledger.md` | COMPLETE; one path; resolves. |
| Evidence recheck, C001-C008 | `verification/evidence_recheck.md` | COMPLETE; one path; resolves. |
| Statistical pass 2, S001-S038 plus C001-C008 and recheck facts | `checkers/statistical_pass_2.md` | COMPLETE; one path; resolves. |
| Evidence quality, all current scopes | `quality/evidence_quality_audit.md` | ASSIGNED during write; one path; resolves. Change to COMPLETE after this artifact is durable. |
| Report generation, C001-C008 | `../final_report_1_5_2.md` | PENDING. The existing file is a stale four-candidate derivative and must be overwritten, not used as evidence. |

The source-page shards are disjoint and exhaustive: DOC-001 pp. 1-9, DOC-002 pp. 1-67, DOC-002 pp. 68-134, and DOC-003 pp. 1-3. Canonical union rows are separately identified and do not create double assignment of source units. Blank DOC-002 pp. 108-109 and 126-134 remain counted and mapped as direct-source pages.

## Statistical-agent execution audit

Statistical pass 1 is recorded as `/root/statistics_pass_1`, `gpt-5.6-terra`, `high`, `FRESH_SPAWN`, with artifact `checkers/statistical_pass_1.md`. Statistical pass 2 is recorded as `/root/statistics_pass_2`, `gpt-5.6-terra`, `high`, `FRESH_SPAWN`, with artifact `checkers/statistical_pass_2.md`. The runtime IDs are distinct, both agents are fresh spawns, and each artifact covers S001-S038. Pass 2 also covers the complete C001-C008 ledger and recheck facts. No mapper agent was reused for either statistical pass.

The execution manifest currently contains 12 unique rows, including the coordinator, the original quality auditor, and this repair specialist. Each row has exactly one artifact path. Token-ledger inclusion and final report-generator registration remain later closeout duties after the accounting window is finalized.

## C001 — Noninferiority narrative reverses the displayed bound direction

- **Card-field audit:** The ledger and recheck contain the required category, exact locations, printed evidence, comparator/rule, calculation, alternative/limitation, provenance, human question, and exact status. The final report card has not yet been regenerated.
- **Evidence and pagination:** DOC-001 PDF pp. 3 and 4 exist within the nine-page source. The recheck links resolve and use PDF page anchors.
- **Calculation audit:** `-1.64% < -1.00%`, with a `-0.64` percentage-point difference from the threshold. The printed noninferiority conclusion follows the displayed values; only the narrative word `greater` conflicts.
- **Assumption audit:** No unreported model or P-value reconstruction is needed. Treating the word as an editorial error or choosing replacement wording would be an inference and is appropriately left to human adjudication.
- **Duplicate and impact audit:** This is the single proposition from S002/SP1-01. It does not duplicate any other C ID. Current wording does not claim that the paper conclusion changed or that downstream propagation occurred.
- **Repair status:** No remaining candidate-artifact repair identified.

## C002 — Centre-5 pause contrast mixes a count outcome with seconds

- **Card-field audit:** The ledger and recheck contain the required fields and preserve the summary-type and unit uncertainty. The final report card remains to be regenerated.
- **Evidence and pagination:** DOC-001 PDF p. 4 exists; the supporting Methods wording on p. 3 also resolves in the recheck.
- **Calculation audit:** `27 - 16 = 11`. Under the repeated `number of pauses` wording, the quantity is a count; the 2-second value defines the qualifying-event threshold.
- **Assumption audit:** The source does not establish whether 27 and 16 are totals, means, medians, or time summaries, or identify the CI method. The card does not choose whether the count wording or seconds label was intended.
- **Duplicate and impact audit:** N026, S018, NUM-CAND-003, and SP1-05 are the same relationship signal and were correctly merged into one stable ID. No downstream propagation or conclusion effect is asserted.
- **Repair status:** No remaining candidate-artifact repair identified.

## C003 — PP day-28 survival point difference does not round from the printed inputs

- **Card-field audit:** The ledger and recheck contain the required fields and explicitly condition the check on the printed counts and denominators defining the displayed estimator. The final report card remains to be regenerated.
- **Evidence and pagination:** DOC-001 PDF p. 6 and DOC-002 PDF p. 123 exist within their respective 9- and 134-page sources; recheck links resolve.
- **Calculation audit:** `100 x (54/995 - 51/943) = 0.018864` percentage points, which ordinarily rounds to `0.0` at one decimal, not the printed `0.1`. The arithmetic is current and reproducible.
- **Assumption audit:** The exact point-estimation procedure, any adjustment or weighting, retained internal rates, row-specific denominator, and explicit rounding rule for the difference column are not supplied. The candidate remains conditional and does not assign `0.0` as a correction.
- **Duplicate and impact audit:** This is distinct from C004: C003 concerns the point display and rounding; C004 concerns interval scale/precision. Repeated N016/S010/numeric/pass-1 signals were correctly merged into C003.
- **Repair status:** No remaining candidate-artifact repair identified.

## C004 — PP day-28 survival confidence interval has an unresolved scale/precision inconsistency

- **Card-field audit:** The ledger and recheck contain the required fields, identify the diagnostic calculation as nonreplacement reasoning, and retain the missing row-level method. The final report card remains to be regenerated.
- **Evidence and pagination:** DOC-001 PDF pp. 3 and 6 and DOC-002 PDF p. 124 exist; visual confirmation that the lower endpoint is printed as `-10`, not `-1.0`, is recorded in the recheck.
- **Calculation audit:** From the printed rates, the diagnostic unpooled-binomial SE is exactly `1.028756` percentage points at the reported precision used in the artifacts. With point difference `0.018864`, the ordinary Wald diagnostic interval is `-1.997498 to 2.035226` percentage points. These values are arithmetically correct and are not proposed endpoints.
- **Assumption audit:** The exact CI formula, software options, variance estimator, correction, adjustment, retained row data, and production precision are unavailable. The same-row `P=.99` is context only and does not independently determine or contradict the printed CI.
- **Duplicate and impact audit:** C004 is distinct from C003 by comparator and rule. N020/S010/XSC-02/SP1-03 were correctly merged into this one interval proposition. No paper-level conclusion change is claimed.
- **Repair status:** The previously identified SE and interval arithmetic defect is repaired in the current ledger and recheck; no remaining candidate-artifact repair identified.

## C005 — PP ROSC ETI percentage conflicts with its count, denominator, and signed difference

- **Card-field audit:** The ledger and recheck contain the required fields and do not assign an intended correction. The final report card remains to be regenerated.
- **Evidence and pagination:** DOC-001 PDF p. 6 exists and the Table 2 location resolves.
- **Calculation audit:** `100 x 377/943 = 39.978791%`, which rounds to `40.0%`, not `30.0%`. `100 x (342/995 - 377/943) = -5.606932` percentage points, matching the displayed `-5.6`; the printed percentages instead imply `+4.4`.
- **Assumption audit:** No alternate denominator, adjusted rate, or retained internal value is supplied. `40.0%` remains a count-derived comparison, not an adjudicated correction.
- **Duplicate and impact audit:** N019, S013, NUM-CAND-001, XSC-01, and SP1-04 are the same row-level proposition and were correctly merged. No unbounded downstream or conclusion-impact claim appears.
- **Repair status:** No remaining candidate-artifact repair identified.

## C006 — Main article and eTable report different contributing-centre counts

- **Card-field audit:** The ledger and recheck contain the required fields and explicitly retain the counting-unit limitation. The final report card remains to be regenerated.
- **Evidence and pagination:** DOC-001 PDF p. 2 and DOC-003 PDF p. 2 exist. The eTable has 21 distinct contributing investigator-centre rows; their arm totals reproduce 1018 and 1022.
- **Calculation audit:** The main article's country counts give `15 + 5 = 20`, while the eTable contains 21 contributing rows. No row is empty across both arms.
- **Assumption audit:** Equality of `EMS center` and `investigator centre` counting units is not established because no crosswalk is supplied. The candidate is correctly framed as a mapping question, not proof that either count is wrong.
- **Duplicate and impact audit:** N044/XSC-03 form one cross-document proposition. It is not duplicated elsewhere and does not assert a changed result or observed reuse.
- **Repair status:** No remaining candidate-artifact repair identified.

## C007 — Published primary-endpoint description omits the amended baseline-disability qualification

- **Card-field audit:** The ledger and recheck contain the required fields and distinguish the printed definition difference from any effect on participant classification. The final report card remains to be regenerated.
- **Evidence and pagination:** DOC-001 PDF pp. 1 and 3, DOC-001 Table 2 on p. 6, and DOC-002 PDF p. 110 exist; all recheck links resolve.
- **Logical-rule audit:** The amended definition can classify a survivor who retains worse baseline disability as favourable even though a literal CPC-1-or-2-only description would not. This is a definitional comparison; aggregate sources do not permit participant-level recalculation.
- **Assumption audit:** The final coding algorithm, paired baseline/day-28 disability, operational definition of `same degree`, and number of affected participants are unavailable. The card does not assume that any reported count changed.
- **Duplicate and impact audit:** N041/N051/S037/XSC-04 form one endpoint-description proposition. C007 is distinct from C008, which concerns a separate technique-failure endpoint and population.
- **Repair status:** No remaining candidate-artifact repair identified.

## C008 — Protocol composite technique-failure definition cannot reconcile with the article's smaller ETI failure count if they are the same endpoint

- **Card-field audit:** The ledger and recheck contain the required fields, including the explicit conditional population-alignment limitation. The final report card remains to be regenerated.
- **Evidence and pagination:** DOC-002 PDF p. 110 and DOC-001 PDF pp. 1, 4, and 6 exist; all recheck links resolve.
- **Calculation audit:** The current conservative conditional calculation is `54 - 24 - 3 = 27`, and `27 > 21`. It allows all 24 participants outside the 999-person ETI-side safety display and all 3 further denominator omissions from 999 to 996 to be deaths before comparing with the displayed failure count.
- **Assumption audit:** Exact alignment among ETI randomization, actual treatment, the 996-person Table 3 row, deaths, regurgitation, and procedural failure is not mechanically established. The article may use a narrower procedural endpoint or a different final population. The candidate appropriately states the relationship conditionally and does not treat 27 as an observed count.
- **Duplicate and impact audit:** N012/N022/N051/S015/S037/XSC-05 form one conditional definition/population proposition. It is distinct from C007 and makes no unbounded downstream-impact or paper-conclusion claim.
- **Repair status:** The previous unqualified population-alignment defect is repaired. No remaining candidate-artifact repair identified.

## Card-set, category, tone, and placeholder audit

The ledger and recheck ID sets are identical at C001-C008. The categories are exact allowed categories from `QUALITY_CONTROL_SCOPE.md`: C001 and C004 are `Statistical reporting inconsistency`; C002, C007, and C008 are `Measure, label, or scale inconsistency`; C003 is `Numeric or arithmetic inconsistency`; C005 is `Denominator, proportion, or total inconsistency`; and C006 is `Cross-document numeric inconsistency`. All wording remains neutral quality control, every status is exactly `Pending Human Adjudication`, and no severity, validity, acceptance, rejection, exclusion, or final correction is assigned.

The current canonical report-generation row is still `PENDING`. The pre-existing Markdown/HTML report pair contains only a stale C001-C004 set and is not a current-run evidence artifact. It must be overwritten with exactly C001-C008. For each of the eight new report cards, all report-spec fields must be present and the human-adjudication template must be exactly:

```markdown
**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __
```

No current candidate mentions a display-zero P value. Therefore the conditional `Independent contradiction beyond P=0 display` report field is not applicable.

## Remaining closeout repairs

1. After this artifact is durable, change the `evidence_quality` coverage row from `ASSIGNED` to `COMPLETE`.
2. Overwrite the stale four-candidate Markdown and HTML reports with the current C001-C008 report. Then change the report-generation coverage row from `PENDING` to `COMPLETE`.
3. Confirm the final report ID set is C001-C008 and every candidate has all required report fields and the five exact `__` adjudication placeholders.
4. Add the report generator and any later repair agents to the execution manifest exactly once, include every manifested agent in the token ledger, finalize the accounting window, rerender HTML once, and run the final validator.

No additional candidate-artifact arithmetic, pagination, duplicate, category, display-zero, unsupported-assumption, or tone repair remains in the current ledger or recheck. New candidate count from this audit: **0**.

## Audit totals and limitations

- Stable IDs audited and returned: **8/8** (C001-C008).
- Source rows audited: **3/3**, **146/146** units fresh-required and mapped.
- Numeric relationships audited through the completed lanes: **51/51**.
- Statistical relationships audited through both fresh passes: **38/38 in pass 1** and **38/38 in pass 2**.
- Coverage rows audited: **22/22**, each with one plain artifact path.
- Manifest rows audited: **12/12** currently recorded.
- Stable IDs absent from recheck: **0**.
- Stable IDs based only on display-zero P values: **0**.
- False candidate pagination or broken recheck evidence links found: **0**.
- Candidate-specific remaining repairs: **0**.
- New candidate propositions: **0**.

The supplied aggregate evidence cannot identify intended corrections, all row-level estimators or CI methods, participant-level classifications, the centre crosswalk, or the exact Table 3 failure population. Those limitations preserve the need for human adjudication; they do not justify removing or scientifically disposing of any stable ID.
