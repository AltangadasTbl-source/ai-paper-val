# Final Evidence-Quality Audit

## Audit scope and outcome

This audit covers all four direct sources, all 64 source pages, all 19 rows currently present in `coverage_manifest.md`, all four rows in `source_coverage.md`, canonical relationships `N001` through `N062` and `S001` through `S039`, both statistical passes, every checker output, stable candidates `C001` through `C007`, the complete mechanical recheck, and every current row in `agent_execution_manifest.md`.

**Coverage status:** COMPLETE for the evidence-quality scope. Four direct PDFs contain 64 pages; every source row has `Reusable units = 0`, `Fresh-required units = Total units`, `Mapped units = Total units`, and `Status = COMPLETE`. The canonical inventories contain 62 distinct N relationships and 39 distinct S relationships. Numeric checking covers all 62 N IDs; both statistical passes contain one explicit completion record for each of the 39 S IDs; cross-source checking covers all 101 relationships; the candidate ledger, evidence recheck, statistical pass 2 reconciliation, and this audit all cover C001, C002, C003, C004, C005, C006, and C007.

All seven stable candidates remain **Pending Human Adjudication**. This audit assigns no validity, importance, action, severity, acceptance, rejection, or scientific disposition. No stable ID is deleted, merged, ranked, renumbered, or suppressed.

## Source, evidence, and coverage controls

- The direct-source hashes recomputed during this audit match `source_hashes_before.sha256` for DOC-001 through DOC-004. The supplied PDFs are unchanged.
- Fresh `pdfinfo`, native-text, layout-text, and page-render assets are present for every direct source. All 64 pages have fresh native and layout extraction. Forty-four result-relevant pages were rendered; the remaining 20 protocol pages have usable fresh text and no result display requiring visual confirmation. No page met the targeted OCR criterion.
- Current evidence artifacts cite only DOC-001 through DOC-004 and derivatives below `review_1_5_2/preprocessing/`. No current evidence, checker, ledger, or recheck artifact cites the retained prior-audit directory. Direct PDF spot checks independently reproduced every candidate value and page used below. This supports the recorded statement that old audit derivatives were not used as evidence.
- The source and extraction maps explicitly cover DOC-001 pp. 1-11, DOC-002 pp. 1-33, DOC-003 pp. 1-19, and DOC-004 p. 1. Pages without a result display are still mapped with their content classification; they were not silently omitted.
- Every coverage-manifest row contains one plain relative artifact path. All required workflow stages are represented. Seventeen current rows are `COMPLETE`; `evidence_quality` is correctly `IN_PROGRESS` until the coordinator incorporates this artifact, and `report_generation` is `PENDING`. The coordinator must change those lifecycle rows only after the corresponding artifacts are complete.
- Candidate-stage scopes enumerate all seven IDs without a range. Statistical-pass scopes enumerate all 39 S IDs without a range. The manifest therefore documents complete unions rather than sampled shards.
- The relationship and checker artifacts state full-scope processing, and no top-N, target count, review queue, or early-stop boundary appears in the current review artifacts. Seven candidates are the result of complete mapped coverage, not a discovery limit.
- `agent_execution_manifest.md` contains the coordinator and every current specialist exactly once. Statistical pass 1 is `/root/statistical_pass_1`, and statistical pass 2 is `/root/statistical_pass_2`; these are distinct non-placeholder runtime IDs. Both are recorded as fresh spawns using `gpt-5.6-terra` at `high` reasoning effort and point to distinct canonical pass artifacts. The two pass files each cover S001-S039, and pass 2 additionally covers the complete C001-C007 ledger and recheck.
- No `P = 0`, `p = 0.000`, or equivalent display zero occurs in the mapped S inventory. No stable candidate is based on display-zero notation, finite precision, underflow, or mathematical nonzero-tail reasoning. The printed `P < .001` records are ordinary inequality displays and are not candidate bases.
- All existing candidate-ledger and recheck PDF links resolve to the supplied PDFs and use valid `#page=N` destinations. One provenance-link omission for C005 and C006 is identified below for coordinator repair.
- The current ledger and recheck do not contain human-adjudication subfields, so there is no nonblank adjudication value in them. The pending final report must include all five required subfields for every C ID and set each value to the exact placeholder `__`.

## C001 — Figure 2 omega-3 eGFR contributor counts conflict with Table 2

- **Coverage and provenance:** Complete. Candidate provenance joins N018, N021, S001, and S002 with NUM-OBS-001, XSC-001, and the eGFR part of STAT-P1-OBS-001. The merge is appropriate because these records compare the same six printed arm/time counts under the same eGFR identity rule.
- **Exact evidence and pagination:** Reproduced at [DOC-001 Figure 2, PDF p. 7](<../../../jama_de_boer_2019_oi_190122.pdf#page=7>) and [DOC-001 Table 2, PDF p. 8](<../../../jama_de_boer_2019_oi_190122.pdf#page=8>). Figure 2 panel B prints placebo `607/459/438` and omega-3 `701/531/496`; Table 2 prints placebo `651/491/462` and active `657/499/472` at baseline/year 2/year 5.
- **Calculation:** Figure minus table is `-44/-32/-24` for placebo and `+44/+32/+24` for active. Both locations total `1308/990/934`, isolating the observation to the arm split. Panel B exactly repeats panel A's vitamin-D counts.
- **Category and framing:** `Cross-document numeric inconsistency` is a valid single primary category. The direct observation is the six-cell mismatch and exact duplicated sequence. A copied annotation or unstated figure-specific arm subset is an inferred alternative, not a source-established cause.
- **Alternatives and human question:** Both are present and bounded. The question asks which arm-specific counts and population definition were intended.
- **Duplicate and impact control:** C001 is not a duplicate of C002 because it concerns eGFR, different printed counts, Table 2, and a distinct same-outcome identity. No paper-conclusion impact is established. Any downstream statement must be limited to possible copying of the displayed eGFR contributor counts if human review confirms the observation.
- **Candidate repair needed:** None in the canonical ledger or recheck.

## C002 — Figure 2 omega-3 urine-ACR contributor counts conflict with eTable 6

- **Coverage and provenance:** Complete. N022, N050, N051, S029, and S030 are connected to NUM-OBS-002, XSC-002, and the urine-ACR portion of STAT-P1-OBS-001. The merged lane records concern the same six ACR contributor counts and the same comparator.
- **Exact evidence and pagination:** Reproduced at [DOC-001 Figure 2, PDF p. 7](<../../../jama_de_boer_2019_oi_190122.pdf#page=7>) and [DOC-003 eTable 6, PDF p. 11](<../../../joi190122supp2_prod.pdf#page=11>). Figure panel D prints placebo `609/463/440` and omega-3 `702/529/505`; eTable 6 prints placebo `653/490/467` and active `658/502/478`.
- **Calculation:** Figure minus table is `-44/-27/-27` for placebo and `+44/+27/+27` for active. Both sources total `1311/992/945`. Panel D exactly repeats the panel-C vitamin-D split.
- **Category and framing:** `Cross-document numeric inconsistency` is valid. The direct observation, inferred production explanations, missing figure-specific rule, and source-grounded alternatives are separated correctly.
- **Alternatives and human question:** Complete. The source does not identify a different plotting population; it also does not prove a copying mechanism.
- **Duplicate and impact control:** C002 is distinct from C001 because the outcome, six values, and comparator source differ. Any downstream statement must be limited to potential reuse of the displayed ACR contributor counts if confirmed.
- **Candidate repair needed:** None in the canonical ledger or recheck.

## C003 — Figure 3 assigns vitamin-D arm sizes to the opposite column labels

- **Coverage and provenance:** Complete. N001, N017, N030, N032, and S013 support the count-column identity check. XSC-003 and STAT-P1-OBS-002 are genuine duplicate lane observations of the same Figure 3 count mapping.
- **Exact evidence and pagination:** Reproduced at [DOC-001 abstract, PDF p. 1](<../../../jama_de_boer_2019_oi_190122.pdf#page=1>) and [DOC-001 Table 2 and Figure 3, PDF p. 8](<../../../jama_de_boer_2019_oi_190122.pdf#page=8>). Active vitamin D is `370+333=703`; vitamin-D placebo is `289+320=609`. Figure 3 prints `703` under Placebo and `609` under Vitamin D, with the nested factorial counts following the same opposite-arm mapping.
- **Category and framing:** `Measure, label, or scale inconsistency` is valid for a count-to-treatment-label conflict. The canonical ledger, recheck, and pass 2 correctly restrict the observation to participant-count columns. The overall changes `-13.1` under placebo and `-12.3` under vitamin D remain aligned with the treatment headings and Table 2; the source does not support reversal of mean changes or forest estimates.
- **Alternatives and human question:** Complete and appropriately conditional. Figure-production metadata and an independent cell-level mapping for all subgroup estimates are unavailable.
- **Duplicate and impact control:** C003 is distinct from C005 because it concerns eGFR Figure 3 rather than urine-ACR eFigure 2. No conclusion impact is established; bounded reuse risk concerns subgroup participant-count extraction only.
- **Candidate repair needed:** None in the canonical ledger or recheck. Earlier cross-source wording requires the systematic count-only repair listed in the coordinator section.

## C004 — Figure 4 assigns omega-3 arm sizes to the opposite column labels

- **Coverage and provenance:** Complete. N001, N018, N031, N032, and S014 support the count mapping; XSC-004 and STAT-P1-OBS-003 are duplicate lane observations correctly merged before stable IDs.
- **Exact evidence and pagination:** Reproduced at [DOC-001 abstract, PDF p. 1](<../../../jama_de_boer_2019_oi_190122.pdf#page=1>), [DOC-001 Table 2, PDF p. 8](<../../../jama_de_boer_2019_oi_190122.pdf#page=8>), and [DOC-001 Figure 4, PDF p. 9](<../../../jama_de_boer_2019_oi_190122.pdf#page=9>). Active omega-3 is `370+289=659`; omega-3 placebo is `333+320=653`. Figure 4 places those Ns under the opposite treatment headings, including the nested factorial rows.
- **Category and framing:** `Measure, label, or scale inconsistency` is valid. The canonical ledger/recheck/pass 2 correctly limit the observation to participant counts. The overall changes `-13.1` under placebo and `-12.2` under omega-3 agree with the treatment headings and Table 2 at printed precision.
- **Alternatives and human question:** Complete. The source does not establish which production element caused the N-column exchange or whether any subgroup estimate needs remapping.
- **Duplicate and impact control:** C004 is distinct from C006 because the outcome and display are different. No paper-level conclusion effect is established. Bounded reuse risk concerns the Figure 4 subgroup counts.
- **Candidate repair needed:** None in the canonical ledger or recheck. Earlier cross-source wording requires count-only narrowing.

## C005 — eFigure 2 places vitamin-D participant counts under the opposite headings

- **Coverage and provenance:** Complete. N050, N059, S029, and S037 support the comparison; NUM-OBS-003, XSC-005, and STAT-P1-OBS-004 are overlapping observations of the same eFigure 2 participant-count mapping.
- **Exact evidence and pagination:** Reproduced at [DOC-003 eTable 6, PDF p. 11](<../../../joi190122supp2_prod.pdf#page=11>) and [DOC-003 eFigure 2, PDF p. 18](<../../../joi190122supp2_prod.pdf#page=18>). The allocation identity used by the calculation is printed at [DOC-001 abstract, PDF p. 1](<../../../jama_de_boer_2019_oi_190122.pdf#page=1>). Active vitamin D totals `370+333=703`; placebo totals `289+320=609`. eFigure 2 prints N=703 under Placebo and N=609 under Active intervention, and its nested N values preserve that opposite mapping.
- **Value-versus-count boundary:** The overall change values do not reverse with the Ns. eFigure 2 prints `3.02` under Placebo and `2.97` under Active intervention; eTable 6 identifies placebo `3.02` and active `2.97`. The reproducible issue is therefore participant-count identity only. The randomized-versus-measured difference `703` versus `702` does not explain the opposite N mapping.
- **Category and framing:** `Measure, label, or scale inconsistency` is valid when explicitly confined to displayed participant counts. The canonical ledger, recheck, and pass 2 apply that boundary correctly.
- **Alternatives and human question:** Complete. The source supports possible N-column transposition but does not establish that headings, change values, or forest estimates should be reversed.
- **Duplicate and impact control:** C005 is not a duplicate of C003 because it concerns a distinct outcome, source display, values, and ratio-scale context. No conclusion impact is established. Any downstream statement must concern possible extraction of eFigure 2 subgroup Ns only.
- **Coordinator repair applied:** DOC-001 abstract p. 1 was added to the ledger's exact source locations, and earlier lane wording was narrowed to the participant-count-only observation.

## C006 — eFigure 3 places omega-3 participant counts under the opposite headings

- **Coverage and provenance:** Complete. N051, N060, S030, and S038 support the comparison; NUM-OBS-004, XSC-006, and STAT-P1-OBS-005 are genuine duplicates of the same eFigure 3 count relationship.
- **Exact evidence and pagination:** Reproduced at [DOC-003 eTable 6, PDF p. 11](<../../../joi190122supp2_prod.pdf#page=11>) and [DOC-003 eFigure 3, PDF p. 19](<../../../joi190122supp2_prod.pdf#page=19>). The allocation identity is printed at [DOC-001 abstract, PDF p. 1](<../../../jama_de_boer_2019_oi_190122.pdf#page=1>). Active omega-3 totals `370+289=659`; placebo totals `333+320=653`. eFigure 3 places N=659 under Placebo and N=653 under Active intervention, including the nested count mapping.
- **Value-versus-count boundary:** eFigure 3's `3.05` under Placebo and `2.94` under Active intervention agree with eTable 6's placebo and active change ratios. Only the participant counts map to the opposite assignments. The `659` versus measured-baseline `658` difference does not resolve the exchange.
- **Category and framing:** `Measure, label, or scale inconsistency` is valid under count-only framing. The canonical ledger, recheck, and pass 2 are appropriately narrow.
- **Alternatives and human question:** Complete. The source does not show that the change values, ratio direction, or forest estimates are reversed.
- **Duplicate and impact control:** C006 is distinct from C004 because the source display, outcome, values, and effect scale differ. No conclusion impact is established; bounded reuse risk concerns eFigure 3 subgroup Ns only.
- **Coordinator repair applied:** DOC-001 abstract p. 1 was added to the ledger's exact locations, and earlier lane descriptions were narrowed to participant counts.

## C007 — Imputation count differs between the analytic-plan addendum and article methods

- **Coverage and provenance:** Complete. N035, N041, S016, and S023 support STAT-P1-OBS-006. This relationship is distinct from all count/label candidates.
- **Exact evidence and pagination:** Reproduced at [DOC-002 Section 15c, PDF p. 32](<../../../joi190122supp1_prod.pdf#page=32>) and [DOC-001 Methods, PDF p. 3](<../../../jama_de_boer_2019_oi_190122.pdf#page=3>). The addendum states `10 imputation datasets`; the article states implemented multiple imputation `M = 20`. Both name Rubin-rule combination. The direct arithmetic is `20-10=10`, and 20 is twice 10.
- **Category and framing:** `Cross-document numeric inconsistency` is acceptable only as a neutral plan-versus-implemented-method difference. The source does not establish an analysis error or a disclosure obligation. The article's broader imputation description, a possible later amendment, and an intentional increase are all retained as source-grounded alternatives.
- **Direct versus inferred:** The two printed counts and document roles are direct. Intent, governance by this exact plan version, rationale, and need for clarification are unresolved rather than inferred as facts.
- **Alternatives and human question:** Complete. The remaining question asks whether the change was intentional and documented in a later governing record.
- **Duplicate and impact control:** No duplicate relationship exists. No outcome-estimate or conclusion effect is established. Any downstream statement must be limited to possible extraction of a planned-versus-implemented analytic-method count if confirmed relevant by human review.
- **Coordinator repair applied:** STAT-P1-OBS-006 now cites DOC-002 PDF p. 32, matching the canonical ledger, recheck, and pass 2.

## Coordinator repair disposition

Four supportable evidence-record repair groups were identified and completed by the coordinator. None changed the stable ID set.

1. **COMPLETED:** `checkers/numeric_consistency.md` now records 35 S relationships with applicable displayed numeric implications and separately identifies S021-S023 and S039 as reviewed prospective definitions.
2. **COMPLETED:** `checkers/statistical_pass_1.md` now cites DOC-002 PDF p. 32 for STAT-P1-OBS-006.
3. **COMPLETED:** XSC-003-XSC-006, NUM-OBS-003/004, STAT-P1-OBS-004/005, N059/N060, and support-map wording now confine C003-C006 to participant-count columns; treatment-aligned means, changes, and forest directions are not claimed inconsistent.
4. **COMPLETED:** C005 and C006 in `candidate_ledger.md` now include DOC-001 abstract PDF p. 1 as provenance for randomized factorial totals.

Following these completed repairs, the coordinator must generate the full report for C001-C007 and then mark `report_generation` complete. Every final report card must contain all required fields. Its human-adjudication block must use exactly:

```markdown
**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __
```

No candidate card may claim that propagation or a conclusion change occurred. Potential downstream wording must identify only the exact count, label, or imputation-method value that an evidence extractor could copy if the candidate is confirmed.

## Limitations

The package supplies no participant-level data, figure-production files, unrounded model outputs, complete person-time denominators, or later change-control record for the imputation plan. These missing materials prevent determination of production mechanism, correction, or scientific consequence. They do not prevent reproduction of the seven printed comparisons. This audit is a source-grounded quality-control review and leaves every candidate for human adjudication.
