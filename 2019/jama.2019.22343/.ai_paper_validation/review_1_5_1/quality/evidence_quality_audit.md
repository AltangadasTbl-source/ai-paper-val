# Final Evidence-Quality Audit

## Audit scope and status

This audit reviewed the complete current-run coverage manifest, source-coverage ledger, direct-source and reused-asset inventories, quantitative evidence maps, canonical `N001` through `N034` and `S001` through `S071` relationship inventories, numeric and cross-source checker outputs, both statistical-pass artifacts, the six-ID candidate ledger, the mechanical direct-source evidence recheck, and the agent-execution manifest. It used only the three supplied PDFs and current-run artifacts. It did not use the web, an old candidate list, a ranked queue, or a count boundary as scientific input.

- **Direct-source coverage:** 75 of 75 PDF pages are mapped. The source rows reconcile as 40 reusable units plus 35 fresh-required units equaling 75 total units, with mapped units equal to total units for each of DOC-001, DOC-002, and DOC-003.
- **Relationship coverage:** 34 of 34 canonical numeric/reporting relationships and 71 of 71 canonical inferential-statistical relationships are present. Both statistical artifacts enumerate all 71 `S` IDs, and pass 2 records `PASS_2_COMPLETE` for every one.
- **Stable candidate identity:** the candidate ledger and mechanical recheck contain the identical set `C001`, `C002`, `C003`, `C004`, `C005`, and `C006`. This quality artifact returns that same set without deletion, merging, ranking, suppression, or renumbering.
- **Statistical-agent requirement:** `/root/statistical_pass_1` and `/root/statistical_pass_2` are distinct runtime IDs. Each is recorded as `gpt-5.6-terra`, reasoning effort `high`, start mode `FRESH_SPAWN`, with one distinct canonical artifact.
- **Coverage-manifest paths:** every current row contains exactly one undecorated relative artifact path. All paths for completed stages resolve. At the time of this audit, `evidence_quality` and `report_generation` remain marked `PLANNED`; the coordinator must mark the first complete after this artifact is accepted and mark the second complete only after the final Markdown report exists.
- **Source traceability:** every candidate PDF link resolves to one of the three direct source files, every cited page is within the source page count, and the cited content was found on the stated page. No false pagination was identified.
- **Integrity recheck:** all three direct-source hashes and all 89 reused-artifact hashes pass `sha256sum --check` against the before-work registers. No source or reused evidence asset changed.
- **Display-zero exclusion:** no stable candidate mentions `P = 0`, `p = 0.000`, or an equivalent P-value display zero. `S056` is a non-P incidence display and remains a checked non-candidate. The conditional independent-contradiction field is therefore not applicable to C001-C006.
- **Tone and categories:** all six stable records remain neutral quality-control candidates and **Pending Human Adjudication**. The stable-ledger categories conform to `QUALITY_CONTROL_SCOPE.md`. No paper-level conclusion change is established.

## Coordinator repair register and completion

The following supportable repairs were identified during audit. Items 1 through 7 were completed by the coordinator before report assembly; item 8 is a report-generation requirement. They do not alter the stable ID set or assign a scientific disposition.

1. Correct stale Figure 4 orientation wording in `extraction/main_quantitative_evidence.md`, `checkers/numeric_consistency.md`, `checkers/statistical_pass_1.md`, and `checkers/cross_source_consistency.md`. The direct figure has the negative side labeled “Favors NIPPV” and the positive side labeled “Favors No NIPPV.” Preserve the pass-2 correction and do not infer the unreported group-subtraction order.
2. In `verification/evidence_recheck.md`, replace the stale statement that the current ledger says positive values favor NIPPV. The current ledger already has the corrected orientation. Retain the direct-source observation and the missing-subtraction-order limitation.
3. Correct C004's numeric relationship provenance from `N028` to `N031`; `N028` concerns volume-assured BPAP versus BPAP-ST, while `N031` contains the 14-patient high-versus-low intensity CAT result.
4. Remove the unsupported C006 cross-reference to `N034`, which concerns use, adherence, and titration parameters. Retain `S058` and, if numeric/result-context cross-references are desired, use the actual displayed 3-through-18-study contexts: `N004`, `N006`, `N007`, `N009`, `N010`, and `N011`, with `S001`, `S003`, `S004`, and `S005` where applicable.
5. Correct canonical `S001` so it records 0.50 on Figure 1 and 0.51 in the abstract and narrative rather than describing pp. 1, 4, and 5 collectively as 0.51 and `DIRECT_MATCH`. Preserve the fact that pass 1 did not emit this observation and that the independent cross-source checker and pass 2 did capture it.
6. Harmonize the local CS-006 category with the stable category `Statistical reporting inconsistency`. The supportable issue is the nonidentical printed model-rule reporting for concrete syntheses, not a general measure-label concern and not a broad critique of model choice.
7. Reclassify local CS-007 in `checkers/cross_source_consistency.md` as a diagnostic-only observation rather than placing it under “Qualifying candidate observations.” The package lacks a source-supplied compatible effect-test and interval rule, so the approximate calculation for `S002` does not meet the stable-candidate threshold. Preserve it as a diagnostic and do not assign a C ID.
8. Build every final report card with all exact labels required by `report_spec.md`. The current candidate ledger is a registration artifact and lacks the exact final-card labels `Candidate statement`, `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, separate `Calculation`, `Alternative source-grounded interpretations`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields`. The report must populate those fields for every C ID and use `__` in every human-adjudication subfield.

## C001 — BPAP mortality pooled confidence-interval lower endpoint differs across matched main-article displays

- **Evidence sufficiency:** The direct paper supplies the matched comparison, outcome, effect measure, confidence level, point estimate, upper endpoint, study count, and patient total. The abstract and results narrative print 0.51, while Figure 1 prints 0.50. This is sufficient to document a candidate consistency issue without deciding which endpoint is intended.
- **Exact-source traceability:** [DOC-001 PDF p. 1, abstract](../../../jama_wilson_2020_oi_190154.pdf#page=1), [DOC-001 PDF p. 4, Figure 1](../../../jama_wilson_2020_oi_190154.pdf#page=4), and [DOC-001 PDF p. 5, narrative](../../../jama_wilson_2020_oi_190154.pdf#page=5) resolve and contain the cited result. Pagination is truthful.
- **Rule reproducibility and arithmetic:** After matching BPAP versus no device, mortality, OR 0.66, upper endpoint 0.87, 13 studies, and 1423 patients, the displayed lower-endpoint difference is `0.51 - 0.50 = 0.01`. The mechanical recheck also reproduces `744 + 679 = 1423`.
- **Assumptions and alternatives:** The comparison does not assume access to the unrounded analysis. Different rounding or export behavior at an unprinted boundary remains a source-grounded alternative. The missing unrounded endpoint, standard error, model output, and display rule prevent selection of an intended value.
- **Duplicate and impact review:** C001 is not a duplicate of C002 or C004 because it concerns a different pooled result and comparator rule. No conclusion-impact claim is supported. If confirmed, a data extractor could copy different lower CI endpoints for the same mortality result; that is bounded downstream relevance, not evidence that propagation or conclusion change occurred.
- **Evidence-card fields still required:** At report assembly, add every exact report-card label listed in the coordinator repair register, including a separate calculation, mechanical-recheck summary, bounded downstream-impact field, verification steps, and blank human-adjudication fields.
- **Audit completion:** Complete for the assigned evidence-quality scope; **Pending Human Adjudication**.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — BPAP quality-of-life pooled confidence-interval upper endpoint differs across matched main-article displays

- **Evidence sufficiency:** The direct paper supplies a matched 9-study, 833-patient BPAP quality-of-life SMD of 0.16 with lower endpoint -0.06. Figure 4 prints upper endpoint 0.38, while the abstract and narrative print 0.39. This supports a source-grounded quality-control comparison without identifying the intended endpoint.
- **Exact-source traceability:** [DOC-001 PDF p. 1, abstract](../../../jama_wilson_2020_oi_190154.pdf#page=1) and [DOC-001 PDF p. 5, Figure 4 and narrative](../../../jama_wilson_2020_oi_190154.pdf#page=5) resolve and contain the cited values. Pagination is truthful.
- **Rule reproducibility and arithmetic:** Matching outcome, comparison, SMD, confidence level, lower endpoint, study count, and total permits the direct calculation `0.39 - 0.38 = 0.01`. The mechanical recheck reproduces `424 + 409 = 833`.
- **Assumptions and alternatives:** Independent rounding or export at a common unprinted boundary remains possible. The unrounded endpoint, standard error, final weights, analysis output, and display convention are absent; the record does not assume which display is correct.
- **Duplicate and impact review:** C002 and C003 share quality-of-life relationships but use different rules: C002 compares a printed interval endpoint, whereas C003 compares direction labels. They are not duplicates. If confirmed, an evidence extractor could copy either upper CI endpoint into an interval table; no paper-level conclusion impact is established.
- **Evidence-card fields still required:** At report assembly, add every exact report-card label listed in the coordinator repair register, including a separate calculation, mechanical-recheck summary, bounded downstream-impact field, verification steps, and blank human-adjudication fields.
- **Audit completion:** Complete for the assigned evidence-quality scope; **Pending Human Adjudication**.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Quality-of-life direction label conflicts with the stated standardized direction

- **Evidence sufficiency:** The methods directly state that quality-of-life measure directions were standardized and that higher scores represent better outcomes. Table 2 directly states that higher scores indicate worse quality of life. Supplement 2 directly documents mixed native instrument directions. These printed statements support a candidate about an unstated scale-context distinction. Figure 4 is relevant orientation context but does not, by itself, establish the subtraction order.
- **Exact-source traceability:** [DOC-001 PDF p. 3, synthesis methods](../../../jama_wilson_2020_oi_190154.pdf#page=3), [DOC-001 PDF p. 5, Figure 4](../../../jama_wilson_2020_oi_190154.pdf#page=5), [DOC-001 PDF p. 8, Table 2 footnote b](../../../jama_wilson_2020_oi_190154.pdf#page=8), and [DOC-003 PDF p. 15, instrument directions](../../../joi190154supp2_prod.pdf#page=15) resolve and contain the cited material. Pagination is truthful.
- **Rule reproducibility and corrected orientation:** The direct Figure 4 orientation is negative equals “Favors NIPPV” and positive equals “Favors No NIPPV.” The methods statement is higher standardized score equals better outcome; Table 2's unqualified footnote is higher score equals worse quality of life. These statements require an explicit distinction between standardized and native scales or another documented convention. Because the package does not state which group was subtracted from which, the audit does not infer that a positive SMD must favor NIPPV or no NIPPV.
- **Assumptions and alternatives:** Table 2's footnote may have been intended for one or more native instruments, and Figure 4 may use a control-minus-intervention orientation. The package lacks study-level sign transformations, extracted means, the group-subtraction definition, and a statement that the table reverted to native-scale polarity. These alternatives constrain the candidate wording but do not erase the directly printed opposite higher-score statements.
- **Prior wording repair:** The main evidence map, numeric checker, pass-1 checker, cross-source checker, and evidence recheck now use the corrected Figure 4 orientation and retain the missing-subtraction-order limitation.
- **Duplicate and impact review:** C003 is distinct from C002 because its rule concerns polarity and labeling rather than an interval endpoint. The candidate must not claim that the forest plot, SMD signs, or paper conclusions are wrong. If confirmed, a reviewer or extractor could reverse a quality-of-life direction or encode the Table 2 SMDs under the wrong scale convention; no actual downstream use is asserted.
- **Evidence-card fields still required:** At report assembly, add every exact report-card label listed in the coordinator repair register. The reasoning and calculation fields must state the corrected orientation and the missing subtraction order, and the bounded impact field must avoid claiming conclusion reversal.
- **Audit completion:** Complete for the assigned evidence-quality scope; **Pending Human Adjudication**.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — High-versus-low intensity CAT confidence interval differs between the main article and supplement

- **Evidence sufficiency:** The main article and eTable 10 identify the same one-RCT, 14-patient high-versus-low intensity CAT comparison and print WMD 2.30, but they print different confidence intervals. The direct printed comparison is adequate for a quality-control candidate without reconstructing the single-study variance.
- **Exact-source traceability:** [DOC-001 PDF p. 7, narrative](../../../jama_wilson_2020_oi_190154.pdf#page=7) and [DOC-003 PDF p. 43, eTable 10](../../../joi190154supp2_prod.pdf#page=43) resolve and contain the cited result. Pagination is truthful.
- **Rule reproducibility and arithmetic:** The lower endpoints differ by `-2.23 - (-2.35) = 0.12`; the upper endpoints differ by `6.95 - 6.83 = 0.12`. Both intervals are centered on 2.30: `(-2.23 + 6.83) / 2 = 2.30` and `(-2.35 + 6.95) / 2 = 2.30`. The half-widths are 4.53 and 4.65.
- **Assumptions and alternatives:** Different calculation or export versions remain possible. Group summaries, the exact standard error, CI construction, analysis output, and version history are absent, so neither interval is selected as intended.
- **Relationship repair and duplicate review:** The ledger now uses `N031`, the canonical numeric relationship for this result, rather than unrelated `N028`. C004 is distinct from C001 and C002 because it concerns a different comparison, source pair, and interval calculation. If confirmed, a data extractor could record different interval widths for the same 14-patient result; no conclusion change is established.
- **Evidence-card fields still required:** At report assembly, add every exact report-card label listed in the coordinator repair register, including the complete arithmetic above, mechanical recheck, bounded impact, verification steps, and blank human-adjudication fields.
- **Audit completion:** Complete for the assigned evidence-quality scope; **Pending Human Adjudication**.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Cheung 2010 participant total differs between matched baseline and effectiveness displays

- **Evidence sufficiency:** The supplement directly prints CPAP 24 and BPAP-ST 23 in the Cheung 2010 baseline row and directly prints 49 patients for the matched effectiveness comparison; the main article also prints 49. The study identity, intervention pair, and cited trial match. This supports a candidate about an undefined population distinction.
- **Exact-source traceability:** [DOC-003 PDF p. 19, eTable 6](../../../joi190154supp2_prod.pdf#page=19), [DOC-003 PDF p. 43, eTable 10](../../../joi190154supp2_prod.pdf#page=43), and [DOC-001 PDF p. 6, narrative](../../../jama_wilson_2020_oi_190154.pdf#page=6) resolve and contain the cited values. Pagination is truthful.
- **Rule reproducibility and arithmetic:** The baseline total is `24 + 23 = 47`; the difference from the effectiveness total is `49 - 47 = 2`. The recheck's percentage decomposition is properly labelled diagnostic rather than direct evidence because event numerators are not printed.
- **Assumptions and alternatives:** The 47 and 49 may represent baseline-characterized, randomized, treated, or outcome-analysis populations. The package does not define those populations for the two displays and does not print outcome numerators. The candidate does not assume that one total is erroneous.
- **Duplicate and impact review:** C005 uses a denominator/population identity rule and is not duplicated by an interval or model-rule candidate. If confirmed, an extractor could record either 47 or 49 as the trial total, potentially affecting denominator fields or sample-size metadata; the audit does not claim that such reuse occurred.
- **Evidence-card fields still required:** At report assembly, add every exact report-card label listed in the coordinator repair register, keep the percentage decomposition explicitly diagnostic, and include bounded impact, verification steps, and blank human-adjudication fields.
- **Audit completion:** Complete for the assigned evidence-quality scope; **Pending Human Adjudication**.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Final-report meta-analysis model rule differs from the protocol rule for syntheses with 3 through 18 studies

- **Evidence sufficiency:** The protocol directly states that eligible syntheses with no more than 18 studies use DerSimonian-Laird random effects with Knapp-Hartung variance adjustment. The final article directly describes DerSimonian-Laird random effects for syntheses with at least 3 studies and does not state that adjustment. Figures 1-4 directly show concrete syntheses with 3, 5, 6, 9, 13, and 15 studies. This supports a candidate about nonidentical printed reporting rules for displayed results.
- **Exact-source traceability:** [DOC-002 PDF p. 11, protocol Data Synthesis](../../../joi190154supp1_prod.pdf#page=11), [DOC-001 PDF p. 3, final Data Synthesis and Analysis](../../../jama_wilson_2020_oi_190154.pdf#page=3), [DOC-001 PDF p. 4, Figures 1 and 2](../../../jama_wilson_2020_oi_190154.pdf#page=4), and [DOC-001 PDF p. 5, Figures 3 and 4](../../../jama_wilson_2020_oi_190154.pdf#page=5) resolve and contain the cited rules and study counts. Pagination is truthful.
- **Rule reproducibility:** The protocol's meta-analysis threshold is more than two studies. Within that eligible domain, its “otherwise” branch assigns Knapp-Hartung-adjusted DerSimonian-Laird to `3 <= k <= 18`. The final article assigns its described DerSimonian-Laird random-effect method to `k >= 3` and omits whether Knapp-Hartung was retained. The overlap contains the displayed counts. This is a comparison of printed rule descriptions; it is not evidence that the actual analysis used one method or departed from the protocol.
- **Assumptions and alternatives:** The final article may use a higher-level description that silently includes the protocol adjustment, or the plan may have been amended. The package lacks analysis commands, per-synthesis output, degrees of freedom, critical-value and variance settings, or a dated amendment. Confidence intervals alone cannot resolve actual model use.
- **Relationship, category, duplicate, and impact review:** The ledger now removes unrelated `N034`, retains `S058`, and cross-links the concrete final-result contexts; CS-006 now uses `Statistical reporting inconsistency`. C006 is not a broad method critique and is not duplicated by the interval candidates. If confirmed, a reviewer could code the model or variance-adjustment rule differently or be unable to reproduce the reported interval method; no actual estimate change or paper-level conclusion change is established.
- **Evidence-card fields still required:** At report assembly, add every exact report-card label listed in the coordinator repair register. The candidate statement and reasoning must remain limited to the printed model-rule comparison, and the impact field must be bounded to method extraction or reproducibility.
- **Audit completion:** Complete for the assigned evidence-quality scope; **Pending Human Adjudication**.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Final audit conclusion

Complete source and relationship coverage is documented without a top-N boundary: all 75 direct-source pages, all 34 `N` relationships, and all 71 `S` relationships are represented; both distinct fresh Terra/high statistical passes cover the full statistical inventory; and all six stable IDs appear in the ledger, recheck, and this audit. The six IDs remain **Pending Human Adjudication**. Report assembly may proceed after the coordinator records the supportable repairs above, preserves all six IDs, supplies complete card fields with bounded language, and updates the remaining planned coverage rows.
