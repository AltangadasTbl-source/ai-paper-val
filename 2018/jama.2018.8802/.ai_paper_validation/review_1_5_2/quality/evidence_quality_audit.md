# Final Evidence-Quality and Complete-Coverage Audit

This audit used only the three supplied direct PDFs, the fresh Workflow 1.5.2 evidence assets, and the current-run durable artifacts. No legacy audit derivative or web source was used. The audit does not assign an AI adjudication, scientific disposition, rank, or final source change. Every stable ID remains **Pending Human Adjudication**.

## Coverage and execution audit

- **Direct sources:** 3 PDFs, 44 PDF-page units. `source_coverage.md` has one row per direct source; every row records `Reusable units = 0`, `Fresh-required units = Total units`, `Mapped units = Total units`, and `Status = COMPLETE`. Totals are 44 total, 0 reusable, 44 fresh-required, and 44 mapped.
- **Source integrity:** Fresh recomputation during this audit reproduced every hash in `source_hashes_before.sha256`: DOC-001 `f921847452d4f5ab012a3eaaa58f25542a73c2f06a858974efc443be4af70fb9`; DOC-002 `5faf07d9e18fb1b9dcc415818622846fb502b410d67255be7ab28aca5e52d138`; DOC-003 `78ebed75675211c520c6eae88b8a1963c9b1f00dc66b2b6ff324d957a1e39645`.
- **Fresh evidence:** Native text and coordinate-layout evidence cover all 44 pages. Thirteen result-relevant pages have fresh full-page visual-confirmation rasters. Current evidence records state that no result-relevant page required OCR. The source inventory and lane records expressly exclude legacy audit derivatives.
- **Quantitative relationships:** 61 distinct `N` relationships are present in the canonical inventory, and all 61 have a row in `numeric_consistency.md`. The checker records 61/61 complete. The eight numeric discovery records were all carried into the stable ledger; the later source correction for NC004/C004 is preserved rather than suppressed.
- **Statistical relationships:** 67 distinct `S` relationships are present. Both `statistical_pass_1.md` and `statistical_pass_2.md` contain exactly 67 per-relationship rows, each respectively marked `PASS_1_COMPLETE` and `PASS_2_COMPLETE`. The canonical inventory records both pass statuses for all 67. Pass 2 reviewed the complete stable ledger and mechanical recheck and emitted no additional candidate.
- **Cross-source relationships:** The checker explicitly covers all N001-N061 and S001-S067 after population, time, contrast, model, scale, and precision matching. NC002 and XC001 were correctly merged before stable IDs because they compare the same LDL boundary statements under the same rule. The other provisional records concern distinct printed values, comparators, or rules and were not merged merely because they share a table or topic.
- **No count boundary:** Inventories and checkers document full relationship universes and complete status rows. Discovery was not stopped at, ranked by, or selected to a desired candidate count. The stable count of 11 follows the mapped lane union, not a top-N rule.
- **Stable-ID alignment at audit time:** `candidate_ledger.md` and `verification/evidence_recheck.md` each contain exactly C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, and C011. Statistical pass 2 reconciles the same 11 IDs. This audit contains the same 11 headings. The final report did not yet exist at this audit cutoff, so its ID set remains a required coordinator check after assembly.
- **Agent execution:** `agent_execution_manifest.md` records the coordinator once and every specialist manifested through this audit once. Statistical pass 1 is `/root/statistics_pass_1`, `gpt-5.6-terra`, high, `FRESH_SPAWN`; pass 2 is the distinct `/root/statistics_pass_2`, `gpt-5.6-terra`, high, `FRESH_SPAWN`. Each has one primary artifact and complete S001-S067 coverage. The report generator and any later repair agent must be added exactly once when spawned, and the eventual token ledger must use the identical complete agent set.
- **Coverage-manifest structure:** Every current row has exactly one undecorated relative artifact path. All current complete-stage artifacts exist. Candidate registration and recheck explicitly enumerate all 11 IDs; both statistical-pass rows explicitly enumerate all 67 S IDs. At audit time the evidence-quality row was `IN_PROGRESS` and the report row was `PENDING`; the coordinator must set them to `COMPLETE` only after this artifact and the complete report exist, and the report row must enumerate C001 through C011 rather than retain `Stable candidate set pending audited ledger`.
- **Display-zero rule:** No mapped source result uses `P = 0`, `p = 0.000`, or an equivalent display zero. No stable ID is based on display-zero formatting, so no conditional independent-contradiction field is applicable to the current 11 cards.

## Artifact repairs required before final validation

1. All 15 source-PDF links in `checkers/cross_source_consistency.md` currently use `../../` from the `checkers/` directory and resolve incorrectly under `.ai_paper_validation/`. Change those targets to `../../../<source.pdf>#page=N`. The candidate-ledger and evidence-recheck links resolve to existing PDFs and their cited page numbers are within the inventoried page counts.
2. `extraction/support_quantitative_evidence.md` UN029 and the provisional NC004 record in `checkers/numeric_consistency.md` retain the pre-raster transcription `9.6`. The exact source, candidate ledger, mechanical recheck, and statistical pass 2 establish `9.66`. The final report must use `9.66` and identify the earlier value as a corrected discovery transcription, not as printed source evidence.
3. The candidate-ledger C011 link labelled `PDF pp. 14-15` targets only `#page=14`. The final report must use separate links for DOC-002 PDF p. 14 and PDF p. 15, as the mechanical recheck does.
4. Mapper-time limitations saying current inventories or source images were unavailable are historical handoff limitations. The final report must use the later complete evidence-asset inventory and recheck facts: 44/44 mapped pages and 13 fresh visual-confirmation rasters.
5. No final candidate cards existed at this audit cutoff. Every final card must contain all exact labels required by `report_spec.md`, including candidate statement, reported-versus-comparator, reasoning procedure, calculation, alternatives, mechanical recheck, quality-control relevance, bounded potential downstream evidence impact, human verification steps, and the exact blank adjudication template below. No subfield may contain an AI-supplied value.

```markdown
**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __
```

## C001 — Table 1 CAD/previous-MI percentage and displayed count

- **Source-grounded facts:** [DOC-001 PDF p. 6](<../../../jama_wang_2018_oi_180070.pdf#page=6>) visibly prints `311 (13.05)` in the intervention column, whose patient total is 2400. `311 / 2400 x 100 = 12.9583...%`, giving 13.0% at one decimal or 12.96% at two decimals, not 13.05%.
- **Category and scope:** `Numeric or arithmetic inconsistency` is within scope. The observable mismatch is conditional on 2400 being the row denominator; the recheck correctly names the missing row-specific denominator or missingness count rather than assuming none exists.
- **Assumption and arithmetic audit:** Arithmetic is correct. An unprinted denominator near 2383-2384 is only a diagnostic possibility and must not be stated as the actual denominator. No duplicate candidate uses the same cell and rule.
- **Card and link audit:** The cited page resolves and pagination is truthful. The final card must explicitly separate the printed quantities from the possible hidden-denominator explanation and include the exact human question from the recheck.
- **Bounded relevance and impact wording:** If confirmed, a data extractor could copy a baseline CAD/previous-MI prevalence that does not reproduce from the displayed count and group total. Do not claim an effect on randomization, adjusted outcomes, or paper conclusions from supplied evidence.
- **Required status:** Pending Human Adjudication.

## C002 — LDL eligibility boundary and complete eligibility routes

- **Source-grounded facts:** [DOC-001 PDF p. 3](<../../../jama_wang_2018_oi_180070.pdf#page=3>) and [p. 7](<../../../jama_wang_2018_oi_180070.pdf#page=7>) use `more than 100`/`>100 mg/dL`; [DOC-002 PDF p. 14](<../../../joi180070supp1_prod.pdf#page=14>), [p. 15](<../../../joi180070supp1_prod.pdf#page=15>), and [DOC-003 PDF p. 3](<../../../joi180070supp2_prod.pdf#page=3>) use `>=100 mg/dL` and give additional routes. At LDL exactly 100, the predicates differ.
- **Category and scope:** `Measure, label, or scale inconsistency` is the correct primary category because the displayed eligibility label can change the denominator at the boundary. NC002 and XC001 were a genuine pre-ID duplicate and were correctly registered once as C002.
- **Assumption and calculation audit:** The logical boundary comparison is correct. The package does not establish that anyone had LDL exactly 100, which rule was executable, or that the short article label omitted rather than incorporated other routes. Those remain human questions; the card must not claim a demonstrated patient-count change.
- **Card and link audit:** All cited pages resolve. The final card must state both the inequality difference and the additional prior-treatment/undocumented-LDL wording, and distinguish the printed label conflict from any inferred denominator consequence.
- **Bounded relevance and impact wording:** If confirmed, an extractor could apply a different lipid-lowering eligibility definition or denominator. Do not claim that a reported effect estimate changes without analysis data.
- **Required status:** Pending Human Adjudication.

## C003 — Baseline per-cluster statement and total baseline patients

- **Source-grounded facts:** [DOC-003 PDF p. 2](<../../../joi180070supp2_prod.pdf#page=2>) prints `20 patients per cluster`; [DOC-001 PDF p. 3](<../../../jama_wang_2018_oi_180070.pdf#page=3>) identifies 40 hospitals, and [p. 6](<../../../jama_wang_2018_oi_180070.pdf#page=6>) reports 40 baseline hospitals and 801 baseline patients. Under an exact equal-count reading, `20 x 40 = 800`, one below 801.
- **Category and scope:** `Denominator, proportion, or total inconsistency` is within scope because an exact reading yields a concrete total mismatch.
- **Assumption and arithmetic audit:** Arithmetic is correct. The ledger title's word `Exact` is stronger than the source establishes: the sentence does not say `exactly`, and 20 may be a target or typical inclusion count. The final candidate statement must use the conditional rule and name cluster-specific counts and target-versus-achieved wording as missing inputs.
- **Card and link audit:** All cited pages resolve and page identities are truthful. C003 is not a duplicate of sample-size relationships S001/S028 because it concerns the separate baseline survey and its 801 total.
- **Bounded relevance and impact wording:** If confirmed, an extractor could copy mutually unreconciled baseline sampling counts. Do not infer an effect on the randomized 4800-patient analysis.
- **Required status:** Pending Human Adjudication.

## C004 — Corrected rtPA source transcription and reproducible percentage

- **Source-grounded facts:** [DOC-003 PDF p. 8](<../../../joi180070supp2_prod.pdf#page=8>) visibly prints `23/238 (9.66)`, not `9.6`; the paired cell prints `46/254 (18.11)`. `23 / 238 x 100 = 9.663865...%` rounds to 9.66%, and `46 / 254 x 100 = 18.110236...%` rounds to 18.11%.
- **Category and scope:** The stable category remains recorded as `Denominator, proportion, or total inconsistency`, but the original arithmetic premise is not supported by the direct source after recheck. Stable-ID preservation does not authorize repeating `9.6` as the printed value.
- **Assumption and arithmetic audit:** The corrected arithmetic is reproducible. Row-specific two-decimal precision is visibly present in both rtPA cells; whether that formatting was intentional is not stated. No new statistical conflict follows for S058. C004 is distinct from C005-C008 because it concerns a different cell, and its corrected source fact must remain separately documented.
- **Card and link audit:** The cited page resolves and the recheck correction is complete. The final candidate statement, reported-versus-comparator, calculation, mechanical-recheck, and relevance fields must lead with the corrected `9.66` fact. It must not present a source percentage mismatch.
- **Bounded relevance and impact wording:** The concrete quality-control value is preventing an erroneous `9.6` transcription or false arithmetic flag from entering later extraction. The supplied printed fraction and percentage themselves reproduce at two decimals; do not imply a source defect or paper-level effect from this ID.
- **Required status:** Pending Human Adjudication; ask only whether the visible two-decimal row precision was intended.

## C005 — Sensitivity discharge-antithrombotics fraction and percentage

- **Source-grounded facts:** [DOC-003 PDF p. 8](<../../../joi180070supp2_prod.pdf#page=8>) prints `2141/2400 (89.3)`. `2141 / 2400 x 100 = 89.2083...%`, which rounds to 89.2% at one decimal.
- **Category and scope:** `Denominator, proportion, or total inconsistency` is correct. The printed same-cell fraction supplies the comparator.
- **Assumption and arithmetic audit:** Arithmetic is correct. A hidden denominator, another analysis version, or alternate convention is possible but not supplied and must remain an alternative, not a claimed cause. C005 is not duplicative of the neighboring eTable 4 cells because each has different printed inputs and its own reproducible calculation.
- **Card and link audit:** The link and page are truthful. The final card must retain the exact printed fraction, show nearest-rounding calculation, state missing alternate denominator/convention, and ask which displayed value was intended.
- **Bounded relevance and impact wording:** If confirmed, an extractor could copy an adherence proportion that does not reproduce from the same-cell fraction. Do not extrapolate to the adjusted effect or study conclusions.
- **Required status:** Pending Human Adjudication.

## C006 — Sensitivity AF-anticoagulation fraction and percentage

- **Source-grounded facts:** [DOC-003 PDF p. 8](<../../../joi180070supp2_prod.pdf#page=8>) prints `39/174 (22.5)`. `39 / 174 x 100 = 22.4138...%`, which rounds to 22.4% at one decimal.
- **Category and scope:** `Denominator, proportion, or total inconsistency` is correct.
- **Assumption and arithmetic audit:** Arithmetic is correct. No alternate eligible denominator or non-nearest convention is supplied. Possible hidden inputs or production history must be labelled as inferred explanations. This is a separate row-level relationship, not a duplicate of C005, C007, or C008.
- **Card and link audit:** The link resolves to the exact source page. The final card must name all three printed values and retain the recheck's exact question about the intended numerator, eligible denominator, and percentage.
- **Bounded relevance and impact wording:** If confirmed, a data extractor could copy a control-group adherence percentage that does not reproduce from 39/174. Do not assert a change to the corresponding adjusted inference.
- **Required status:** Pending Human Adjudication.

## C007 — Sensitivity lipid-lowering fraction and percentage

- **Source-grounded facts:** [DOC-003 PDF p. 8](<../../../joi180070supp2_prod.pdf#page=8>) prints `1439/1586 (90.8)`. `1439 / 1586 x 100 = 90.7314...%`, which rounds to 90.7% at one decimal.
- **Category and scope:** `Denominator, proportion, or total inconsistency` is correct for this cell. C002 separately concerns the eligibility label; it is not a duplicate because it uses different source statements and a boundary-identity rule.
- **Assumption and arithmetic audit:** Arithmetic is correct. The package does not show whether a different denominator or eligibility implementation produced 90.8; neither may be asserted as the cause.
- **Card and link audit:** The source link and page are truthful. The final card must cross-reference C002 only to distinguish the issues, not merge them, and must retain the cell-specific human question.
- **Bounded relevance and impact wording:** If confirmed, an extractor could copy a sensitivity-analysis percentage that does not reproduce from its displayed fraction. Do not claim that the threshold wording explains the arithmetic without source evidence.
- **Required status:** Pending Human Adjudication.

## C008 — Sensitivity antidiabetic-medication fraction and percentage

- **Source-grounded facts:** [DOC-003 PDF p. 8](<../../../joi180070supp2_prod.pdf#page=8>) prints `557/688 (81.1)`. `557 / 688 x 100 = 80.9593...%`, which rounds to 81.0% at one decimal.
- **Category and scope:** `Denominator, proportion, or total inconsistency` is correct.
- **Assumption and arithmetic audit:** Arithmetic is correct. A hidden denominator or earlier table version is not supplied and must remain an explicitly inferred possibility. This relationship is not a duplicate of the other eTable 4 row calculations.
- **Card and link audit:** The page link resolves. The final card must show the direct observation separately from production-mechanism speculation and ask which value and rounding rule were intended.
- **Bounded relevance and impact wording:** If confirmed, an extractor could copy a percentage that does not reproduce from the printed numerator and denominator. Do not claim an effect on the separately reported adjusted difference or ORPA.
- **Required status:** Pending Human Adjudication.

## C009 — In-hospital-death absolute-difference interval and P value

- **Source-grounded facts:** [DOC-001 PDF p. 8](<../../../jama_wang_2018_oi_180070.pdf#page=8>) prints absolute difference `-0.7` with 95% CI `-1.1 to +0.2` and adjacent `P=.009`. The separately headed HR block is `0.96 (0.90 to 1.02), P=.14`. The article states two-sided testing.
- **Category and scope:** `Statistical reporting inconsistency` is correct. The candidate is based on the independent same-block CI/null and P-threshold contradiction, not a display-zero P value.
- **Assumption and arithmetic audit:** The direct logical comparison is reproducible: the CI contains 0 while `.009 < .05`. The midpoint/half-width/normal calculation is diagnostic only. The exact estimator, variance, degrees of freedom, CI construction, and statement that the CI and P invert the same test are missing, so the card must not prescribe a replacement P value or CI.
- **Card and link audit:** The page and column identities are visually confirmed and truthful. The final card must distinguish the absolute-difference P from the HR P=.14, name the missing construction details, and preserve the exact human question. There is no duplicate stable statistical candidate.
- **Bounded relevance and impact wording:** If confirmed, an extractor could code the same absolute-difference result differently from the CI and the P value. Do not claim that a conclusion changed or that either printed element is definitively wrong.
- **Required status:** Pending Human Adjudication.

## C010 — Composite descriptions, analysis units, and displayed estimands

- **Source-grounded facts:** [DOC-001 PDF p. 3](<../../../jama_wang_2018_oi_180070.pdf#page=3>) defines and averages patient ratios; [p. 4](<../../../jama_wang_2018_oi_180070.pdf#page=4>) and [DOC-002 pp. 18](<../../../joi180070supp1_prod.pdf#page=18>)-[19](<../../../joi180070supp1_prod.pdf#page=19>) describe eligible care opportunities as binary observations and a population-average OR; [DOC-003 PDF p. 2](<../../../joi180070supp2_prod.pdf#page=2>) gives a pooled performed/possible-interventions baseline definition. DOC-001 p. 7 separately labels mean (SD), adjusted absolute difference, and ORPA.
- **Category and scope:** `Analysis-unit or population inconsistency` is permissible here only because the different printed unit descriptions create a concrete unresolved mapping to the displayed composite percentage, adjusted difference, and ORPA. General concerns about GEE or trial design are out of scope.
- **Assumption and calculation audit:** `mean_i(performed_i/eligible_i)` and `sum_i(performed_i)/sum_i(eligible_i)` are generally nonidentical when eligible counts vary. However, the source may intentionally use patient-level descriptive means and opportunity-level inferential modeling. The card must not call the separately labelled mean and ORPA mutually contradictory; it must frame the unresolved fact as which unit and estimator generated each displayed column, especially the adjusted absolute difference.
- **Card and link audit:** Add DOC-001 p. 4 to the final exact locations; the shorter ledger location list omits this relevant analysis description, while the recheck includes it. All links above resolve. C010 is distinct from C002 because it concerns aggregation/analysis unit rather than eligibility boundary.
- **Bounded relevance and impact wording:** If confirmed, an extractor could mislabel a composite estimate's weighting or analysis unit. Do not claim numeric change without patient-level eligible-opportunity data.
- **Required status:** Pending Human Adjudication.

## C011 — DVT-prophylaxis timing labels

- **Source-grounded facts:** [DOC-002 PDF p. 13](<../../../joi180070supp1_prod.pdf#page=13>) says `within 48 hours of admission`; [p. 14](<../../../joi180070supp1_prod.pdf#page=14>) and [p. 15](<../../../joi180070supp1_prod.pdf#page=15>) continue the detailed `by end of hospital day two` definition; [DOC-003 PDF p. 3](<../../../joi180070supp2_prod.pdf#page=3>) and [DOC-001 PDF p. 7](<../../../jama_wang_2018_oi_180070.pdf#page=7>) use hospital day 2 for the reported measure.
- **Category and scope:** `Measure, label, or scale inconsistency` is correct because the timing label defines eligibility/adherence for the displayed 178/645 and 66/592 values.
- **Assumption and calculation audit:** An elapsed 48-hour boundary and a calendar end-of-day-2 boundary can differ for a late-day admission. The package does not define `hospital day`, timestamp inclusion, or its executable rule. The card must present the calendar-day example as conditional logic, not as the trial's proven implementation.
- **Card and link audit:** The final card must use separate DOC-002 p. 14 and p. 15 links rather than the ledger's single `pp. 14-15` link targeting page 14. C011 is distinct from the DVT effect relationships because it concerns the measure's timing definition, not a new estimate/interval/P conflict.
- **Bounded relevance and impact wording:** If confirmed, an extractor or guideline reviewer could copy a different DVT timing definition for the reported adherence measure. Do not claim that any patient was reclassified or that the effect estimate changes without timestamp data.
- **Required status:** Pending Human Adjudication.

## Completion status and limitations

- **Audit scope completed:** 3/3 source rows; 20/20 current coverage rows; 61/61 N relationships; 67/67 pass-1 S relationships; 67/67 pass-2 S relationships; 10/10 currently manifested execution rows including the coordinator; and 11/11 stable candidate IDs.
- **Repairs handed to coordinator:** cross-source link depth; final use of the corrected C004 source transcription; C011 split pagination; C010 addition of DOC-001 p. 4; complete report-card fields, bounded impact wording, and exact `__` adjudication placeholders; final coverage, manifest, token-ledger, hash-after, report, and validator synchronization.
- **Evidence limitations:** The supplied package lacks raw patient-level or cluster-level data, row-specific missingness/hidden denominators, an executable LDL rule, a hospital-day timestamp definition, a complete composite-estimator mapping, and the exact CI/P construction details needed to resolve C001-C003 and C005-C011 beyond the stated source comparisons. C004's exact printed fraction and percentage are available and mathematically reproducible.
- **Canonical ID result:** C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, and C011 are all present once and remain **Pending Human Adjudication**.
