# Final Evidence-Quality Audit

## Overall audit completion record

- **Audit scope:** Complete fresh Workflow 1.5.2 source/evidence audit through stable candidate registration, mechanical evidence recheck, and statistical pass 2.
- **Audited direct sources:** 6 supplied PDFs, 100 physical PDF-page units.
- **Audited relationship units:** 69 numeric/reporting relationships (`N001`–`N049`, `N200`–`N219`) and 53 inferential-statistical relationships (`S001`–`S038`, `S200`–`S214`).
- **Audited stable candidate set:** `C001`, `C002`, `C003`, `C004`.
- **Disposition:** Every stable candidate remains **Pending Human Adjudication**.
- **Evidence-quality completion:** COMPLETE for the full assigned source, relationship, checker, candidate, recheck, and execution-manifest scope.
- **Unresolved evidence-quality defects:** None in the audited completed stages after the coordinator repairs recorded below.
- **Downstream completion gates:** The coordinator must mark the `evidence_quality` coverage row `COMPLETE` with the exact scope `C001, C002, C003, C004`; after report assembly, the report-generation row must do the same, the report-generator agent must be added to the execution manifest, and the final report/HTML/validator checks must be completed. These are later workflow stages, not unresolved candidate-evidence defects.

## Evidence boundary and fresh-source audit

The evidence chain is source-first. `source_inventory.md`, `evidence_asset_inventory.md`, both mapper artifacts, every checker, both statistical passes, the candidate ledger, and the recheck consistently identify the six supplied PDFs and fresh assets below `review_1_5_2/preprocessing/` as their evidence basis. No evidence citation, relationship scope, duplicate key, or candidate provenance points to a previous audit derivative. References to the preserved prior run only document its exclusion; they do not supply a fact or discovery boundary. No web or external-literature evidence was used.

The source inventory contains one row for each supplied PDF. Independent `pdfinfo` checks confirm page counts of 14, 36, 3, 3, 43, and 1, totaling 100. Fresh SHA-256 recomputation exactly matches every line of `source_hashes_before.sha256`:

| Source ID | Total units | Reusable units | Fresh-required units | Mapped units | Status | Hash audit |
|---|---:|---:|---:|---:|---|---|
| DOC-001 | 14 | 0 | 14 | 14 | COMPLETE | Unchanged |
| DOC-002 | 36 | 0 | 36 | 36 | COMPLETE | Unchanged |
| DOC-003 | 3 | 0 | 3 | 3 | COMPLETE | Unchanged |
| DOC-004 | 3 | 0 | 3 | 3 | COMPLETE | Unchanged |
| DOC-005 | 43 | 0 | 43 | 43 | COMPLETE | Unchanged |
| DOC-006 | 1 | 0 | 1 | 1 | COMPLETE | Unchanged |
| **Total** | **100** | **0** | **100** | **100** | **COMPLETE** | **6/6 unchanged** |

Native and layout text exist for every direct source. Sixty-seven result-relevant pages were freshly rendered. Native/layout text was usable for every relevant page, so zero OCR units were required. Main pages 13–14 and the documented non-rendered support pages were still mapped as source units and were classified as non-result-bearing or covered through usable native/layout text; rendering was not treated as the unit-coverage denominator.

## Coverage-manifest audit

The manifest contains the required stages and assigns every source/evidence scope to one plain relative artifact path per row. All listed completed-stage artifacts exist. Main mapping covers DOC-001 pp. 1–14; support mapping covers DOC-002 pp. 1–36, DOC-003 pp. 1–3, DOC-004 pp. 1–3, DOC-005 pp. 1–43, and DOC-006 p. 1. The source-unit union is all 100 PDF pages.

Candidate registration and evidence recheck each enumerate exactly `C001, C002, C003, C004`. Both statistical scopes enumerate every one of the 53 S IDs without a range-only shortcut. The `evidence_quality` row was necessarily pending while this artifact was being written, and the `report_generation` row is a later-stage handoff; the coordinator was notified that both rows must enumerate `C001, C002, C003, C004` and become `COMPLETE` at their respective completion points.

## Quantitative and checker coverage audit

- `relationships/numeric_relationship_inventory.md` contains exactly 69 unique IDs: `N001`–`N049` and `N200`–`N219`.
- `checkers/numeric_consistency.md` contains exactly the same 69 IDs and an explicit `COMPLETE` record for every ID.
- Numeric checks cover arithmetic, denominators/percentages, category partitions, units/scales, rate/count distinctions, analysis-population distinctions, repeated locations, and version-matched support definitions. Nonexclusive or conditionally denominated rows were not forced into false totals.
- `statistics/relationship_inventory.md` contains exactly 53 unique S IDs. Every S ID has a relationship-level `PASS_1_COMPLETE` record and a relationship-level `PASS_2_COMPLETE` record.
- `checkers/statistical_pass_1.md` and `checkers/statistical_pass_2.md` each explicitly name all 53 S IDs. Pass 2 revisits all four stable candidates and the complete mechanical recheck.
- `checkers/cross_source_consistency.md` covers the complete union of 69 N and 53 S relationships after matching population, time point, contrast, model/effect measure, scale, and precision.

Two correctable statistical-coverage defects were identified during this audit and repaired by the coordinator: the pass-1 checker initially lacked an explicit line for each S ID, and the canonical statistical inventory initially lacked relationship-level pass-2 markers. Recheck after repair confirms 53/53 explicit pass-1 checker records and 53/53 explicit pass-2 inventory records.

No minimum, maximum, desired count, top-N route, review queue, or cap-controlled deferral appears in the discovery chain. Pre-ID proposals were reconciled by exact duplicate key, comparator, and rule: P-N004/P1/CS-01 became C001; P-N040/P2 became C002; P3 became C003; and P-N218/P5/CS-03 became C004. The ARISCAT extraction proposal was source-visually resolved as superscript citation 18 followed by the threshold 26 and therefore did not establish a numeric contradiction. The eTable 8 proposal identified a missing effect-measure definition without a contradictory printed label and is retained as a limitation. These are threshold decisions before stable-ID assignment, not deletion, ranking, or suppression of a stable ID.

No literal `P = 0`, `p = 0.000`, or equivalent display-zero result underlies any stable candidate. No candidate card requires the conditional `Independent contradiction beyond P=0 display` field.

## Stable-ID, card-readiness, and link audit

The ledger and mechanical recheck ID sets are identical and ordered `C001`, `C002`, `C003`, `C004`; this audit returns the same set. Each ledger record provides the category, exact locations, printed evidence and comparator, reproducible rule/calculation, direct-observation/inference separation, source-grounded alternatives, and exact remaining human question. Each recheck independently records all mechanical-recheck fields required by the contract.

The final report cards do not yet exist at this stage. The ledger is not required to use the final-report label template, but the report generator must populate every exact report-card label from these audited facts. In particular, it must not omit quality-control relevance, bounded downstream impact, human verification steps, the mechanical-recheck summary, or the exact five-line human-adjudication template reproduced under every candidate below. From a report located directly in `.ai_paper_validation/`, source links must use `../SOURCE.pdf#page=N`; the quality-artifact links below correctly use `../../../SOURCE.pdf#page=N`. Every audited PDF link resolves and every fragment is within the verified source page count.

## Agent-execution audit

The manifest contains the coordinator once and one row for each agent used through this audit, with a single primary artifact path per row. Every listed completed artifact exists; this audit file satisfies the quality-auditor row. The statistical agents are fresh and distinct:

| Stage | Runtime agent ID | Model | Effort | Start mode | Primary artifact | Audit |
|---|---|---|---|---|---|---|
| statistics_pass_1 | `/root/statistics_pass_1` | `gpt-5.6-terra` | `high` | `FRESH_SPAWN` | `checkers/statistical_pass_1.md` | 53/53 complete |
| statistics_pass_2 | `/root/statistics_pass_2` | `gpt-5.6-terra` | `high` | `FRESH_SPAWN` | `checkers/statistical_pass_2.md` | 53/53 complete |

The two runtime IDs differ. No medium-effort mapper/checker was relabeled or reused as either high-effort statistical pass. The report generator has not yet run and must be added exactly once when spawned; token accounting must later contain the identical final agent set.

## C001 — Hypoxemia confidence-interval endpoint sign differs between abstract and Table 3

- **Status:** Pending Human Adjudication.
- **Category audit:** `Cross-document numeric inconsistency`, an exact allowed category.
- **Exact evidence audit:** [DOC-001 PDF p. 1 abstract](../../../jama_bluth_2019_oi_190055_16092.pdf#page=1) prints high versus low hypoxemia 5.0% versus 13.6%, difference −8.6%, 95% CI −11.1% to +6.1%, and `P < .001`. [DOC-001 PDF p. 9 Table 3](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) prints 49/989 (5.0%) versus 134/987 (13.6%), difference −8.6 with 95% CI −11.1 to −6.1, RR 0.51 (0.40 to 0.65), and `P < .001`. Fresh visual inspection confirms both endpoint signs and physical PDF pages.
- **Arithmetic audit:** `49/989 = 4.9545%`; `134/987 = 13.5765%`; high minus low is `−8.6220` percentage points and rounds to −8.6. The two printed upper endpoints differ by 12.2 percentage points. A diagnostic unpooled Wald interval from displayed counts is approximately −11.15 to −6.09, but that approximation is not treated as the authoritative analysis output.
- **Rule and assumption audit:** The population, outcome, treatment order, point estimate, confidence level, precision, and P value match across locations, so the endpoint-sign identity rule is applicable. The candidate does not assume which location is correct; authoritative output and exact interval implementation remain unavailable.
- **Pagination/link audit:** PDF pp. 1 and 9 are truthful physical pages, exist within the 14-page source, and both links resolve.
- **Duplicate audit:** N004/S002 proposals sharing the same values, comparator, and endpoint-sign rule were genuinely merged before C001 assignment. No other stable candidate duplicates this relationship.
- **Impact-language audit:** The bounded supported statement is that an abstract-focused extractor could copy an interval crossing zero while a table-focused extractor could copy an interval wholly below zero if the mismatch is confirmed. No propagation or conclusion change is claimed.
- **Final-card field audit:** The ledger and recheck support every required final-card field. Report wording must retain the direct sign mismatch, label the Wald calculation diagnostic, state the exact remaining human question, and avoid naming a corrected endpoint.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — DIC row finite risk ratio and narrow interval do not reconcile with zero comparator events

- **Status:** Pending Human Adjudication.
- **Category audit:** `Statistical reporting inconsistency`, an exact allowed category.
- **Exact evidence audit:** [DOC-001 PDF p. 9 Table 3](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) prints DIC as 1/989 (0.1%) versus 0/987, difference 0.1 (95% CI −0.1 to 0.3), RR 2.00 (1.91 to 2.09), and `P > .99`. The continued [Table 3 footnotes on PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) identify risk ratios, a Wald likelihood-ratio approximation for RR intervals, and chi-square P values; [PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4) gives the matching broad binary-outcome method.
- **Arithmetic audit:** High risk is `1/989 = 0.0010111`; low risk is `0/987 = 0`. Their ordinary uncorrected ratio has a zero denominator and cannot directly equal the finite printed RR 2.00. The printed RR interval excludes 1. No replacement RR, CI, or P value is calculated.
- **Rule and assumption audit:** The source does not supply a zero-cell correction, alternate estimator, exact interval formula/software call, chi-square variant, row-specific analysis population, or authoritative output. Therefore the candidate is supportably centered on the displayed counts versus finite RR/CI reconciliation. Any interval/P-value comparison must remain conditional because the source names different broad procedures and does not supply their implementations.
- **Pagination/link audit:** PDF pp. 4, 9, and 10 are truthful physical pages, exist within the 14-page source, and all links resolve.
- **Duplicate audit:** N040/S027 proposals with the same DIC row, comparator, and zero-denominator rule were genuinely merged before C002 assignment. C002 is distinct from the cross-location and label candidates.
- **Impact-language audit:** The bounded supported statement is that an extractor could copy a precise finite RR/CI without the undisclosed rule needed to reconcile it with 1 versus 0 events if the candidate is confirmed. No downstream propagation or paper-level conclusion change is claimed.
- **Final-card field audit:** The report must explicitly name the missing zero-cell/estimator definitions, distinguish the directly printed row from possible explanations, and must not prescribe a replacement or treat the P value as display-zero notation.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Protocol analysis sentence combines odds-ratio and relative-risk labels

- **Status:** Pending Human Adjudication.
- **Category audit:** `Measure, label, or scale inconsistency`, an exact allowed category.
- **Exact evidence audit:** [DOC-002 physical PDF p. 23, footer p. 22](../../../joi190055supp1_prod_16092.pdf#page=23) visibly prints the uninterrupted phrase `the odds ratio relative risks ... will be calculated using logistic regression analysis`. [DOC-004 PDF p. 2](../../../joi190055supp3_prod_16092.pdf#page=2) explicitly names the primary effect as a risk ratio, while [DOC-004 PDF p. 3](../../../joi190055supp3_prod_16092.pdf#page=3) separately names odds ratios for exploratory analyses.
- **Logical audit:** No arithmetic is required. Odds ratio and risk ratio are distinct supplied-document measure labels; the protocol sentence provides no separator, alternative-analysis definition, or conversion rule that makes the compound phrase unique.
- **Rule and assumption audit:** The audit does not infer the intended link, estimand, conversion, or punctuation from the phrase `logistic regression`. The later final SAP may supersede the earlier protocol wording, but supersession does not identify what the archived compound phrase intended.
- **Pagination/link audit:** The corrected locator is physical PDF p. 23, not physical p. 22; footer p. 22 is stated only as the internal footer. Comparator pages 2 and 3 are truthful physical pages. All links resolve within their respective page counts.
- **Duplicate audit:** Only the S202/P3 relationship supports C003. It is not merged with eTable 8's missing label because the printed statements, comparator, and rule differ.
- **Impact-language audit:** The bounded supported statement is that a protocol extractor could code the planned effect measure ambiguously if the compound label is confirmed. No claim is made that the final analysis used the wrong estimand or that conclusions changed.
- **Final-card field audit:** The report must retain both source-grounded alternatives—editing residue or later supersession—while asking whether the protocol intended an odds ratio, a risk ratio, or distinct analyses.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — eFigure 11 mortality values are described as extra-pulmonary complications

- **Status:** Pending Human Adjudication.
- **Category audit:** `Measure, label, or scale inconsistency`, an exact allowed category.
- **Exact evidence audit:** [DOC-005 PDF p. 41 eFigure 11](../../../joi190055supp4_prod_16092.pdf#page=41) is titled `Probability of death in the first 5 postoperative days`, labels the y-axis `5-Day Mortality`, and prints 0.5% versus 0.3%, HR 1.67 (0.40 to 6.97), and `P = 0.484`, while its narrative calls those values postoperative extra-pulmonary complications. [DOC-005 PDF p. 40 eFigure 10](../../../joi190055supp4_prod_16092.pdf#page=40) separately reports extra-pulmonary complications as 16.9% versus 15.2%, HR 1.12 (0.89 to 1.39). [DOC-001 PDF p. 10 Table 3](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) reports 5-day mortality as 5/989 (0.5%) versus 3/987 (0.3%), HR 1.67 (0.40 to 6.97), and `P = .48`.
- **Arithmetic audit:** `5/989 = 0.5056%` and `3/987 = 0.3040%`, rounding to 0.5% and 0.3%. These are not rounding variants of 16.9% and 15.2%; the eFigure 11 HR/CI also matches the mortality row, not eFigure 10.
- **Rule and assumption audit:** The directly observed issue is the outcome noun conflict. Carry-forward wording from adjacent eFigure 10 is plausible but is not established as the production mechanism or final correction.
- **Pagination/link audit:** Physical PDF pp. 40 and 41 and main PDF p. 10 are truthful, within verified page counts, and all links resolve.
- **Duplicate audit:** N218/S214 proposals sharing the same eFigure 11 values, comparator, and label-identity rule were genuinely merged before C004 assignment. The record is distinct from C003 because it concerns a different source statement and outcome-label rule.
- **Impact-language audit:** The bounded supported statement is that an extractor could misclassify a 5-day mortality effect as an extra-pulmonary-complication effect if the label mismatch is confirmed. No propagation, harm, or conclusion change is claimed.
- **Final-card field audit:** The report must separate the directly conflicting noun from the inferred carry-forward explanation and ask which outcome name the authoritative figure source intended.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Final limitations and report-generation handoff

- The supplied package has no raw data, analysis code, unrounded result output, publisher production source, or authorial clarification. Those absences limit adjudication but do not prevent the four direct consistency observations from being reproduced.
- Several Table 2/support-table P values, group-sequential calculations, and survival diagnostics lack enough supplied definitions for strict reconstruction; both statistical passes correctly retain them as definition-bounded rather than importing conventions.
- The DIC row lacks its zero-cell estimator and exact inferential implementations; no replacement is proposed.
- The final Markdown report had not yet been assembled when this stage began, so report-card label completeness, report-relative link syntax, exact blank human fields, HTML rendering, token metadata, and final validator status remain downstream mechanical checks. This audit supplies exact card-ready facts and exact blank templates for all four IDs; the report generator and validator must preserve them.

**Audit covered IDs:** `C001`, `C002`, `C003`, `C004`  
**Candidate count returned:** 4  
**Correctable defects found during audit:** 2 statistical coverage-record defects, both repaired and mechanically rechecked  
**Remaining candidate-evidence defects:** 0  
**Primary artifact:** `quality/evidence_quality_audit.md`
