# Evidence-Quality Audit

## Audit scope and overall status

**Audit status: PASS WITH REQUIRED COORDINATOR REPAIRS.** This status concerns evidence-chain completeness and report readiness only. It is not a scientific disposition for any candidate. C001, C002, and C003 all remain **Pending Human Adjudication**.

The audit covered the complete direct-source inventory and source-coverage ledger; all coverage-manifest rows; the main and four support quantitative maps; the canonical N001-N089 and S001-S052 inventories; numeric, cross-source, and both statistical checker outputs; the candidate ledger; the mechanical evidence recheck; and the agent-execution manifest. Candidate facts were targeted-confirmed against the supplied PDFs. No legacy candidate set, old review queue, verifier disposition, quality artifact, or final report was used as a discovery source, and no web source was used.

### Coverage and execution findings

- Direct-source coverage closes: 5 supplied PDFs, 119/119 PDF-page units mapped. The 24 reusable units plus 95 fresh-required units equal 119, and each source row independently satisfies `reusable + fresh-required = total = mapped` with `COMPLETE` status.
- The page maps account for DOC-001 pp. 1-9, DOC-002 pp. 1-63, DOC-003 pp. 1-23, DOC-004 pp. 1-15, and DOC-005 pp. 1-9. No source-unit gap was found. The recorded limitation for image-only DOC-003 pp. 16-22 is a derivative-text limitation, not a scientific-coverage gap, because those pages were rendered and directly inspected.
- Every current coverage row contains one plain relative artifact path. All currently complete-stage paths resolve. The `evidence_quality` and `report_generation` rows are intentionally unfinished at this audit point and require the coordinator updates listed below.
- Numeric coverage is complete: 89/89 canonical N relationships have explicit checker rows. Statistical coverage is complete in the checker artifacts: S001-S052 each appears once with `PASS_1_COMPLETE` and once with `PASS_2_COMPLETE` (52/52 in each pass).
- Statistical pass 1 and pass 2 are distinct fresh executions: `/root/statistical_pass_1` and `/root/statistical_pass_2`, each recorded as `gpt-5.6-terra`, `high`, `FRESH_SPAWN`, with the required distinct artifact. The current agent manifest contains the coordinator and every agent manifested through this audit stage exactly once.
- Stable candidate identity closes across the current ledger and recheck: C001, C002, C003 in both, with no duplicate stable ID. This quality artifact returns the same complete set.
- Discovery was explicitly rebuilt from complete source-linked maps and complete N/S inventories. The checker scopes are uncapped (N001-N089 and S001-S052), and no top-N selection, legacy candidate list, round-number stopping rule, or deferred-by-cap path controlled discovery.
- All five direct-source hashes and all 92 reused-artifact hashes revalidated unchanged during this audit.
- No stable candidate is based on a display-zero P value. None of C001-C003 mentions `P = 0`, `p = 0.000`, or an equivalent display zero; therefore the conditional independent-contradiction field is not applicable.
- The three categories are exact categories allowed by `QUALITY_CONTROL_SCOPE.md`. Wording is neutral, separates direct observation from inference, and does not assign severity, validity, acceptance, rejection, exclusion, or a final correction.

### Required coordinator repairs before report completion

1. Amend `statistics/relationship_inventory.md` to record that all S001-S052 received both `PASS_1_COMPLETE` and `PASS_2_COMPLETE`. The two checker files already contain the complete per-ID records, but the canonical inventory currently lacks both completion markers required by the workflow validator.
2. In C002's ledger wording and final evidence card, retain `284 / 0.80 = 355` as the aggregate loss-fraction result, and add the balanced whole-arm result: `142 / 0.80 = 177.5`, so a 1:1 allocation requires 178 per arm and 356 total. Do not state or imply that 355 preserves equal whole-number arms.
3. After this artifact is complete, change the `evidence_quality` coverage row to `COMPLETE`. After report assembly, replace the report row's generic scope with the explicit set `C001, C002, C003`, change it to `COMPLETE`, and ensure its single artifact path resolves.
4. Add the report generator and any later repair agent exactly once to `agent_execution_manifest.md` and the token ledger. Do not alter the two distinct statistical execution rows.
5. In every final report card, include all required report-spec fields, use only source-resolving PDF links ending in `#page=N`, keep impact statements conditional and bounded, and use the exact five blank human-adjudication placeholders reproduced under each candidate below.

## C001 — Primary-endpoint midline-shift boundary differs across matched supplied sources

- **Audit result:** Evidence-supported candidate consistency issue; Pending Human Adjudication.
- **Category check:** `Measure, label, or scale inconsistency` is an allowed and appropriate primary category. The cross-document aspect is retained as provenance and does not create a duplicate candidate.
- **Evidence confirmation:** The main article prints “5 mm or greater” on [main article PDF p. 3](<../../../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=3>); the protocol prints `≥5 mm` on [protocol PDF p. 7](<../../../joi250033supp1_prod_1750956987.76581.pdf#page=7>) and [protocol PDF p. 16](<../../../joi250033supp1_prod_1750956987.76581.pdf#page=16>); the results supplement prints `≥5 mm` on [results supplement PDF p. 15](<../../../joi250033supp4_prod_1750956987.77981.pdf#page=15>); and the SAP prints `>5 mm` on [SAP PDF p. 3](<../../../joi250033supp5_prod_1750956987.78281.pdf#page=3>). All pagination and links were directly confirmed.
- **Reproducibility:** For shift `x`, `x ≥ 5` includes `x = 5`, while `x > 5` excludes it. The comparator, endpoint component, unit, six-month context, and trial identity match. No unsupported claim is made that an exactly 5-mm case existed or that the primary count changed.
- **Assumptions and alternatives:** The recheck correctly distinguishes the direct printed-operator difference from inferred explanations. A typographic or version-specific SAP expression and either possible operational rule remain bounded alternatives because the package supplies neither the adjudication programming rule nor participant-level measurements.
- **Duplicate/impact audit:** The numeric, cross-source, and statistical observations concern the same printed threshold, comparator, and identity rule and were properly merged before stable IDs. No other stable candidate duplicates C001. The conclusion impact is not overstated. If confirmed, the bounded downstream risk is that an evidence extractor could encode an inclusive or exclusive endpoint boundary depending on which supplied document is used; no propagation or conclusion change is asserted.
- **Final-card field audit:** The ledger and recheck supply the candidate statement, exact source locations, source evidence, comparator, reasoning rule, calculation, alternatives, mechanical recheck, quality-control relevance, and human question needed for report assembly. The final card must additionally state bounded downstream impact and concrete verification steps using the report specification's exact labels.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Printed sample-size attrition allowance does not reconcile with the printed target

- **Audit result:** Evidence-supported candidate consistency issue with one required arithmetic-presentation repair; Pending Human Adjudication.
- **Category check:** `Numeric or arithmetic inconsistency` is an allowed and appropriate primary category.
- **Evidence confirmation:** The protocol prints 142 required per group, 20% loss, and 342 total/171 per group on [protocol PDF p. 50](<../../../joi250033supp1_prod_1750956987.76581.pdf#page=50>). The SAP repeats the calculation across [SAP PDF p. 4](<../../../joi250033supp5_prod_1750956987.78281.pdf#page=4>) and [SAP PDF p. 5](<../../../joi250033supp5_prod_1750956987.78281.pdf#page=5>). The related main summary is on [main article PDF p. 3](<../../../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=3>). All pagination and links were directly confirmed.
- **Reproducibility:** The analyzable target is `142 * 2 = 284`. Under a true 20%-of-enrollment loss fraction, the aggregate minimum is `284 / 0.80 = 355`. Because the design is 1:1 with whole participants, the arm-level calculation is `142 / 0.80 = 177.5`, requiring 178 per arm and 356 total. The printed target instead gives `171 * 0.80 = 136.8` expected retained per arm. Adding 20% to the base gives `142 * 1.20 = 170.4`, which can round upward to 171 per arm. The current recheck contains this complete calculation; the shorter ledger statement must be conformed to it.
- **Assumptions and alternatives:** The candidate does not assume which convention was intended. The 20%-addition convention and an undocumented sequential-design or unrounded software result remain explicit alternatives. The missing attrition denominator, unrounded output, and calculation trace are correctly named.
- **Duplicate/impact audit:** Numeric and statistical observations concern the same printed inputs and arithmetic rule and were properly merged before stable IDs. C002 is distinct from the endpoint-definition and surgery-denominator candidates. No trial-outcome or conclusion impact is claimed. If confirmed, the bounded downstream risk is that a reviewer or data extractor could reconstruct a different planned enrollment or attrition convention; no realized analysis defect is asserted.
- **Required repair:** Final ledger/report language must show both 355 aggregate and 356 for balanced whole-number arms. This is a precision repair, not an adjudication or candidate suppression.
- **Final-card field audit:** The ledger and recheck provide the evidence, alternatives, missing definition, and human question. The final card must use the exact report-spec labels, include the balanced-arm repair, and bound downstream impact to sample-size-plan extraction.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Standard-care surgery-type counts exceed their shared printed denominator

- **Audit result:** Evidence-supported candidate consistency issue whose counting-rule premise remains explicitly conditional; Pending Human Adjudication.
- **Category check:** `Denominator, proportion, or total inconsistency` is an allowed and appropriate primary category.
- **Evidence confirmation:** Table 1 prints `146/163 (89.6%)` for burr-hole craniostomy and `18/163 (11.0%)` for trephine craniostomy in the standard-care column on [main article PDF p. 5](<../../../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=5>). The table header identifies `No./total No. (%)`, and footnote e describes the two procedure techniques. The page and link were directly confirmed.
- **Reproducibility:** `146 + 18 = 164`, one above the repeated denominator 163. Individually, `146 / 163 * 100 = 89.57...%` rounds to 89.6% and `18 / 163 * 100 = 11.04...%` rounds to 11.0%; the printed percentages sum to 100.6%. Rounding cannot remove the integer excess.
- **Assumptions and alternatives:** Mutual exclusivity is not treated as established. The source does not define whether bilateral procedures permit one participant to appear in both technique rows or whether the numerators count people versus procedures when techniques overlap. Participant overlap and a typographic count/denominator difference remain explicit source-grounded alternatives. The final card must say that the inconsistency requires clarification of the counting rule; it must not call the distribution impossible without that condition.
- **Duplicate/impact audit:** C003 concerns N021 only and is not duplicated by an S relationship or another stable candidate. It does not overstate impact on the primary outcome. If confirmed, the bounded downstream risk is that an extractor could treat 164 technique memberships as mutually exclusive participants under denominator 163; no actual reuse or conclusion change is asserted.
- **Final-card field audit:** The ledger and recheck supply the printed values, calculation, conditional applicability of the total rule, alternatives, and exact human question. The final card must preserve this conditional framing and include verification of participant-versus-procedure and overlap rules.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Limitations

The package does not supply participant-level imaging measurements, the adjudication implementation rule, participant-level procedure records, the sample-size software output, or the attrition denominator/convention. Exact model-variance inputs, imputation draws, and several planned-test implementation details are also unavailable, as recorded in the statistical passes. These limitations prevent scientific adjudication or exact reconstruction beyond the supplied relationships, but they do not leave a source-page, candidate-recheck, numeric-check, or statistical-pass coverage gap.
