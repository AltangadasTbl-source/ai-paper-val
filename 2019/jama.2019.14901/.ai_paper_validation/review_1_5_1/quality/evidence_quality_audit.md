# Final Evidence-Quality Audit

**Review framing:** Pending Human Adjudication. This artifact is a neutral quantitative quality-control audit. It does not assign severity, scientific validity, acceptance, exclusion, or a correction. Every stable candidate remains available for human review.

## Audit scope and overall status

The audit covered the complete current source and evidence-asset inventories, every row of `source_coverage.md` and `coverage_manifest.md`, both quantitative relationship inventories, all numeric and cross-source checker output, all 39 records in each statistical pass, the complete stable candidate ledger, the complete mechanical evidence recheck, and the full agent execution manifest. It also re-opened the exact supplied-source PDF pages cited for C001-C006; derived text and images were used as locators and transcription aids, not as final authority.

- **Stable candidate set audited:** C001, C002, C003, C004, C005, C006 (6/6).
- **Candidate identity:** `candidate_ledger.md` and `verification/evidence_recheck.md` each contain exactly C001-C006 once. This audit returns exactly the same six current IDs. No stable ID was deleted, merged, ranked, suppressed, or renumbered.
- **Discovery boundary:** The durable artifacts state that old candidate, checker, verifier, critic, quality, and report records were not used as discovery inputs. Complete page mapping, N001-N059 checking, S001-S039 checking, and the absence of a stopping count support the conclusion that no top-N boundary or old candidate list controlled discovery.
- **Source integrity:** All four direct-source hashes reproduce the recorded pre-review hashes. All 59 reused-artifact hashes reproduce the recorded pre-review hashes.
- **Display-zero rule:** No stable candidate mentions `P = 0`, `p = 0.000`, or an equivalent display-zero P value. C005 compares `.10` and `.1057`, neither of which is a display zero. No independent-contradiction conditional field is therefore required for C001-C006.
- **Tone and disposition:** Candidate wording remains neutral and each candidate is framed as Pending Human Adjudication. No scientific disposition or severity has been assigned.

## Complete source and manifest coverage audit

| Source | Total units | Reusable units | Fresh-required units | Mapped units | Audit result |
|---|---:|---:|---:|---:|---|
| DOC-001 | 11 | 9 | 2 | 11 | Complete; 9 + 2 = 11 and 11 mapped. |
| DOC-002 | 48 | 0 | 48 | 48 | Complete; 0 + 48 = 48 and 48 mapped. |
| DOC-003 | 9 | 9 | 0 | 9 | Complete; 9 + 0 = 9 and 9 mapped. |
| DOC-004 | 1 | 0 | 1 | 1 | Complete; 0 + 1 = 1 and 1 mapped. |
| **Package** | **69** | **18** | **51** | **69** | **Complete scientific source coverage.** |

PDF metadata independently reproduces page counts of 11, 48, 9, and 1. The fresh files cover DOC-001 pp. 10-11, DOC-002 pp. 1-48, and DOC-004 p. 1, for 51 fresh-required units with no gap. Reusable and fresh-required units therefore partition every direct-source row, and mapped units close every row.

Every current coverage-manifest row contains one undecorated relative artifact path. Every artifact for a row marked `COMPLETE` exists. The candidate-stage scopes now explicitly enumerate C001-C006. The evidence recheck and evidence-quality artifacts exist, so the coordinator must change their manifest rows from `ASSIGNED` to `COMPLETE`. The report-generation row correctly enumerates C001-C006 and must remain `PENDING` until the report artifact exists. These are manifest-state updates, not scientific-coverage gaps.

The relationship inventories contain 23 main plus 36 support numeric/reporting relationships (N001-N059) and 23 main plus 16 support inferential relationships (S001-S039). The numeric checker has one explicit record for each of 59 N IDs. Statistical passes 1 and 2 each have one explicit completion record for each of 39 S IDs. The cross-source checker states full N001-N059 and S001-S039 coverage. No relationship was omitted because it produced no candidate.

## Statistical execution audit

- Statistical pass 1 is recorded as fresh agent `/root/statistics_pass_1`, model `gpt-5.6-terra`, effort `high`, start mode `FRESH_SPAWN`, with `checkers/statistical_pass_1.md` as its single primary manifest artifact.
- Statistical pass 2 is recorded as different fresh agent `/root/statistics_pass_2`, model `gpt-5.6-terra`, effort `high`, start mode `FRESH_SPAWN`, with `checkers/statistical_pass_2.md` as its single primary manifest artifact.
- The two runtime IDs are distinct and neither is a mapper or medium-effort agent. Both passes enumerate S001-S039 and mark all 39 relationships complete. Pass 2 reconsidered C001-C005 and the then-current cross-lane implications. C006 was appended by the later quality-audit repair, has only N027 provenance, and introduces no inferential relationship or change to S001-S039 coverage. The pass-2 artifact now records that bounded post-audit reconciliation and correctly distinguishes the original 5/5 execution scope from the final 6/6 ledger.
- The former pass-1 provenance typo is repaired: `STAT1-CAND-002` now cites `S019 / MAIN-S019 and S036 / SUPPORT-S013`, consistent with the stable ledger, recheck, and pass 2.
- Both passes expressly distinguish diagnostic calculations from reported analyses, refrain from inferring missing test conventions, and document that no literal display-zero P value occurs.

## Coordinator repair register

Closed during this audit:

1. The pass-1 C005 crosswalk now correctly uses S019/S036.
2. N027 was registered as C006 without altering earlier IDs, and C006 received a complete mechanical source recheck.
3. All candidate-stage manifest scopes now enumerate C001-C006.
4. The numeric checker now correctly states that 20/46 = 43.4783% rounds to 43% at whole-percent precision.
5. Statistical pass 2 now records the post-audit C006 reconciliation, its lack of an S relationship, and unchanged S001-S039 coverage.

Handoff-only manifest updates remain: change the `evidence_recheck` and `evidence_quality` rows from `ASSIGNED` to `COMPLETE`; keep report generation pending until its artifact exists. No scientific or evidence-card repair remains open in this audit.

## C001 — Day-7 respiratory-failure absolute difference differs across matched article locations

- **Status:** Pending Human Adjudication
- **Candidate statement:** The abstract and Results narrative print a day-7 respiratory-failure absolute difference of -8.7 percentage points, while Table 2 prints -8.5 for the otherwise matched result.
- **Category:** Numeric or arithmetic inconsistency
- **Exact source locations:** [main article — PDF p. 1](<../../../jama_thille_2019_oi_190108.pdf#page=1>), abstract Results; [main article — PDF p. 6](<../../../jama_thille_2019_oi_190108.pdf#page=6>), Secondary Outcomes; [main article — PDF p. 8](<../../../jama_thille_2019_oi_190108.pdf#page=8>), Table 2.
- **Source evidence:** PDF pp. 1 and 6 directly print 21% versus 29%, difference -8.7% (95% CI -15.2% to -1.8%; P=.01). PDF p. 8 directly prints 88/302 versus 70/339, difference -8.5% with the same interval and P value.
- **Reported-versus-comparator:** Reported prose value -8.7 percentage points versus Table 2 and displayed-count value -8.5 percentage points.
- **Reasoning procedure:** Match population, endpoint, day, treatment direction, interval, and P value; then compare the printed point estimates and reproduce the unadjusted difference from the displayed counts.
- **Calculation:** `(70 / 339 - 88 / 302) x 100 = -8.490105296`, which rounds to -8.5 percentage points at one decimal. The two printed point estimates differ by 0.2 percentage points.
- **Alternative source-grounded interpretations:** The prose may reflect an unprinted analysis output or editing stage, while Table 2 may reflect the displayed counts. No cited location labels a distinct population, endpoint, model, or denominator for -8.7.
- **Mechanical evidence recheck:** All three cited locations were found by direct visual inspection; both printed values, the shared interval/P value, and the count-derived calculation were reproduced. The unavailable input is the analysis output or rule that produced -8.7.
- **Quality-control relevance:** The evidence supports a bounded request to reconcile one matched point estimate. It does not establish which value is authoritatively intended or that the paper-level conclusion changes.
- **Potential downstream evidence impact:** If confirmed, a data extractor or meta-analytic reviewer could copy either -8.7 or -8.5 for the same day-7 result. No actual propagation or conclusion change is established by the package.
- **Human verification steps:** Compare the authorial analysis output and amendment/edit history for the result; identify the intended denominator and calculation; then reconcile the matched abstract, narrative, and table presentation.
- **Evidence-card field audit:** The ledger contains the core observation, category, locations, calculation rule, alternatives, and human question but does not carry all final-card labels. The explicit mechanical-recheck, quality relevance, downstream-impact, verification-step, and adjudication fields are supplied here for report generation.
- **Unsupported-assumption audit:** Treating -8.5 as count-compatible is supportable diagnostic reasoning. Treating it as the final intended estimate, or attributing -8.7 to a specific production error, would be unsupported and is not done.
- **Pagination and link audit:** All citations identify actual PDF pages within the 11-page source, and every PDF link ends in the correct `#page=N` fragment.
- **Duplicate-relationship audit:** NUM-CAND-001, CROSS-CAND-001, and STAT1-CAND-001 compare the same values under the same rule and were correctly registered once as C001.
- **Conclusion-impact audit:** No paper-level conclusion impact is claimed or source-established.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Reintubation respiratory-acidosis cutoff differs between article and protocol

- **Status:** Pending Human Adjudication
- **Candidate statement:** The article and supplied protocol print different pH cutoffs for the respiratory-acidosis component of the reintubation respiratory-failure criterion.
- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** [main article — PDF p. 4](<../../../jama_thille_2019_oi_190108.pdf#page=4>), Outcomes; [protocol — PDF p. 30](<../../../joi190108supp1_prod.pdf#page=30>) and [protocol — PDF p. 31](<../../../joi190108supp1_prod.pdf#page=31>), section 5.4 continuation.
- **Source evidence:** The article directly prints pH below 7.25 with PaCO2 above 45 mm Hg. Protocol section 5.4 directly prints pH below 7.35 with PaCO2 above 45 mm Hg for the same reintubation-rule component.
- **Reported-versus-comparator:** Article cutoff `<7.25` versus protocol cutoff `<7.35`, with the same PaCO2 condition and criterion role.
- **Reasoning procedure:** Match the decision context, at-least-two-criteria structure, physiological component, unit, and PaCO2 threshold, then compare the pH thresholds.
- **Calculation:** `7.35 - 7.25 = 0.10` pH units.
- **Alternative source-grounded interpretations:** The article may reflect a later approved amendment or an implementation-specific refinement. The package contains protocol version 4 but no amendment history, final case-report definition, or operational event-adjudication rule that resolves the difference.
- **Mechanical evidence recheck:** The article location and the protocol continuation across pp. 30-31 were visually found. The criterion role and both threshold pairs were matched. Missing inputs are the final amendment history and operative ascertainment definition.
- **Quality-control relevance:** The evidence supports a bounded question about which printed threshold governed event ascertainment. It does not show that any participant classification or reported event count changed.
- **Potential downstream evidence impact:** If confirmed, a protocol reviewer or outcome-definition extractor could record different reintubation criteria from the two sources. The package does not demonstrate altered trial results or downstream propagation.
- **Human verification steps:** Retrieve the final approved protocol/amendments and operative case-report or adjudication instructions; determine the effective threshold and date; then reconcile the source descriptions if necessary.
- **Evidence-card field audit:** The ledger supplies the core comparison, locations, rule, alternatives, and human question. This audit supplies explicit mechanical-recheck, quality relevance, bounded downstream-impact, verification-step, and blank adjudication fields needed by the final card.
- **Unsupported-assumption audit:** A later amendment is possible but not observed. The audit does not assume that the protocol version was the final operative definition or that the threshold difference altered the results.
- **Pagination and link audit:** PDF p. 30 truthfully begins section 5.4 and PDF p. 31 truthfully contains the continued pH criterion. No false single-page attribution is used.
- **Duplicate-relationship audit:** CROSS-CAND-002 and STAT1-CAND-003 concern the same matched cutoff discrepancy and were correctly registered once as C002.
- **Conclusion-impact audit:** No paper-level conclusion impact is claimed or source-established.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Hypercapnic ineffective-cough percentages conflict with printed fractions

- **Status:** Pending Human Adjudication
- **Candidate statement:** In the hypercapnic eTable 2 ineffective-cough row, each printed percentage conflicts with its adjacent printed numerator and denominator.
- **Category:** Denominator, proportion, or total inconsistency
- **Exact source locations:** [results supplement — PDF p. 4](<../../../joi190108supp2_prod.pdf#page=4>), eTable 2; [main article — PDF p. 6](<../../../jama_thille_2019_oi_190108.pdf#page=6>), Table 1 aggregate row.
- **Source evidence:** eTable 2 directly prints `14/45 (69)` and `16/59 (73)` under `Ineffective cough, No./total No. (%)`. The same eTable prints nonhypercapnic `51/239 (21)` and `70/263 (27)`; Table 1 prints aggregate `65/284 (23)` and `86/322 (27)`.
- **Reported-versus-comparator:** Printed 69% versus 14/45 = 31.1%; printed 73% versus 16/59 = 27.1%.
- **Reasoning procedure:** Apply the row's own numerator/denominator/percentage identity, then test the source-grounded complementary proportions and stratum-to-aggregate sums.
- **Calculation:** `14/45 x 100 = 31.1111%` and `16/59 x 100 = 27.1186%`. Their complements are `31/45 = 68.8889%` and `43/59 = 72.8814%`, reproducing 69% and 73%. The strata reconcile: `51+14=65`, `239+45=284`, `70+16=86`, and `263+59=322`.
- **Alternative source-grounded interpretations:** The percentages may describe effective rather than ineffective cough, or the numerators, percentages, or row label may contain a transcription/coding mismatch. The source does not name an inverse measure.
- **Mechanical evidence recheck:** The row and aggregate comparator were found by direct visual inspection. Both fraction-percentage conflicts, both complements, and all four aggregate identities were reproduced. The missing input is the intended cough-status coding definition.
- **Quality-control relevance:** The evidence supports reconciliation of two baseline-characteristic cells and their label. It does not establish an outcome-analysis defect or a paper-level conclusion change.
- **Potential downstream evidence impact:** If confirmed, a baseline-characteristic extractor could copy 69% or 73% as ineffective-cough prevalence despite the adjacent fractions. The package does not show that this has occurred.
- **Human verification steps:** Check the source data dictionary and table-production code; determine whether the numerator, percentage, or label expresses the intended category; then reconcile both cells and the aggregate representation.
- **Evidence-card field audit:** The ledger supplies the printed values, arithmetic, alternatives, and human question. This audit supplies explicit mechanical-recheck, quality relevance, bounded downstream-impact, verification-step, and blank adjudication fields for the final report.
- **Unsupported-assumption audit:** Complement coding is a reproducible numerical pattern, not an established explanation. The audit does not infer which component is wrong.
- **Pagination and link audit:** Both direct-source citations point to actual pages and use truthful page fragments.
- **Duplicate-relationship audit:** C003 and C004 share relationship N050 and a similar complement pattern, but they concern different labelled rows and different printed cell pairs. They are not duplicates and must remain separate stable IDs.
- **Conclusion-impact audit:** No paper-level conclusion impact is claimed or source-established.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Hypercapnic abundant-secretion percentages conflict with printed fractions

- **Status:** Pending Human Adjudication
- **Candidate statement:** In the hypercapnic eTable 2 abundant-secretions row, each printed percentage conflicts with its adjacent printed numerator and denominator.
- **Category:** Denominator, proportion, or total inconsistency
- **Exact source locations:** [results supplement — PDF p. 4](<../../../joi190108supp2_prod.pdf#page=4>), eTable 2; [main article — PDF p. 6](<../../../jama_thille_2019_oi_190108.pdf#page=6>), Table 1 aggregate row.
- **Source evidence:** eTable 2 directly prints `20/46 (57)` and `23/61 (62)` under `Abundant secretions, No./total No. (%)`. The same eTable prints nonhypercapnic `101/242 (42)` and `91/265 (34)`; Table 1 prints aggregate `121/288 (42)` and `114/326 (35)`.
- **Reported-versus-comparator:** Printed 57% versus 20/46 = 43.5%; printed 62% versus 23/61 = 37.7%.
- **Reasoning procedure:** Apply the row's numerator/denominator/percentage identity, then check complementary proportions and stratum-to-aggregate sums.
- **Calculation:** `20/46 x 100 = 43.4783%`, which rounds to 43% at whole-percent precision, and `23/61 x 100 = 37.7049%`, which rounds to 38%. Their complements are `26/46 = 56.5217%` and `38/61 = 62.2951%`, reproducing 57% and 62%. The strata reconcile: `101+20=121`, `242+46=288`, `91+23=114`, and `265+61=326`.
- **Alternative source-grounded interpretations:** The percentages may describe absence rather than presence of abundant secretions, or the numerators, percentages, or row label may contain a transcription/coding mismatch. The source does not label an inverse measure.
- **Mechanical evidence recheck:** The row and aggregate comparator were found by direct visual inspection. Both fraction-percentage conflicts, both complements, and all aggregate identities were reproduced. The missing input is the intended secretion-status coding definition.
- **Quality-control relevance:** The evidence supports reconciliation of two baseline-characteristic cells and their label. It does not establish an outcome-analysis defect or a paper-level conclusion change.
- **Potential downstream evidence impact:** If confirmed, a baseline-characteristic extractor could copy 57% or 62% as abundant-secretions prevalence despite the adjacent fractions. The package does not show that this has occurred.
- **Human verification steps:** Check the source data dictionary and table-production code; determine whether the numerator, percentage, or label expresses the intended category; then reconcile both cells and the aggregate representation.
- **Evidence-card field audit:** The ledger supplies the printed values, arithmetic, alternatives, and human question. This audit supplies explicit mechanical-recheck, quality relevance, bounded downstream-impact, verification-step, and blank adjudication fields for the final report.
- **Unsupported-assumption audit:** Complement coding is a numerical inference, not a demonstrated cause. The audit does not infer which component is wrong.
- **Pagination and link audit:** Both direct-source citations point to actual pages and use truthful page fragments.
- **Duplicate-relationship audit:** C004 is distinct from C003 because it concerns the abundant-secretions row and different printed fractions/percentages. Similarity of the apparent mechanism is not a basis for merging stable IDs.
- **Conclusion-impact audit:** No paper-level conclusion impact is claimed or source-established.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Matched nonhypercapnic day-7 reintubation P values differ across article and supplement

- **Status:** Pending Human Adjudication
- **Candidate statement:** The article and eTable 4 print different P values for a matched nonhypercapnic day-7 reintubation result.
- **Category:** Cross-document numeric inconsistency
- **Exact source locations:** [main article — PDF p. 7](<../../../jama_thille_2019_oi_190108.pdf#page=7>), subgroup Results; [results supplement — PDF p. 7](<../../../joi190108supp2_prod.pdf#page=7>), eTable 4.
- **Source evidence:** The article directly prints 13% versus 18%, difference -5.0% (95% CI -11.2% to 1.1%), P=.10. eTable 4 directly prints 35/276 versus 45/254, the same displayed difference and interval, and P=.1057.
- **Reported-versus-comparator:** Main-text P=.10 versus supplement P=.1057 for matching population, endpoint, counts-derived percentages, contrast, difference, and confidence interval.
- **Reasoning procedure:** Match all result descriptors and printed effect components before comparing the attached P values. Use count-based test reconstruction only as a diagnostic because the exact subgroup test and display rule are not fully supplied.
- **Calculation:** `45/254 x 100 = 17.7165%`; `35/276 x 100 = 12.6812%`; the intervention-minus-control difference is -5.0354 percentage points, reproducing -5.0. At ordinary two-decimal rounding, .1057 becomes .11, not .10. The recheck's uncorrected Pearson diagnostic reproduces approximately .1057, but it does not establish the analysis used at both locations.
- **Alternative source-grounded interpretations:** The locations may use different test variants, separately generated outputs, or an unstated truncation/display convention. The package does not identify which explanation applies.
- **Mechanical evidence recheck:** Both cited pages were directly inspected and the matched result descriptors, two P values, and count-derived effect were reproduced. Missing inputs are the exact subgroup test setting, correction choice, analysis output, and editorial display rule.
- **Quality-control relevance:** The evidence supports a bounded request to reconcile or explain two printed P values. Both printed values remain above .05, and the package does not establish a different scientific conclusion.
- **Potential downstream evidence impact:** If confirmed, a data extractor could copy either `.10` or `.1057` for the same result. No actual propagation or effect on a pooled estimate, guideline, or conclusion is established.
- **Human verification steps:** Compare the exact subgroup-analysis output and table/narrative formatting rules; identify the test and precision convention used at each location; then reconcile or explicitly distinguish the displays.
- **Evidence-card field audit:** The ledger supplies the core match, discrepancy, alternatives, and human question. This audit supplies explicit mechanical-recheck, quality relevance, bounded downstream-impact, verification-step, and blank adjudication fields for the final report.
- **Unsupported-assumption audit:** Ordinary rounding and the Pearson calculation are diagnostics only. The audit does not assume truncation was forbidden, that both locations used the same test, or that .1057 is the uniquely correct P value.
- **Pagination and link audit:** Both PDF citations identify actual page 7 in their respective sources and end in truthful page fragments.
- **Duplicate-relationship audit:** S019 is the main-article relationship and S036 is the support relationship. Figure 3's P=.11 is a separately labelled log-rank result and is not merged into C005 as a duplicate fixed-time P value.
- **Conclusion-impact audit:** No paper-level conclusion impact is claimed or source-established.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Protocol total-duration breakdown does not arithmetically reach the printed total

- **Status:** Pending Human Adjudication
- **Candidate statement:** Protocol section 5.6 prints a total duration of 51 months but names only 36 study months plus 12 analysis months in the same breakdown sentence.
- **Category:** Numeric or arithmetic inconsistency
- **Exact source locations:** [protocol — PDF p. 11](<../../../joi190108supp1_prod.pdf#page=11>), synopsis study duration; [protocol — PDF p. 32](<../../../joi190108supp1_prod.pdf#page=32>), section 5.6.
- **Source evidence:** PDF p. 11 directly prints 36 months of inclusion, 3 months of participation for each patient, and 51 months total comprising 39 study months plus 12 analysis months. PDF p. 32 directly prints 3 months of participation, 36 months of recruitment, and then 51 months total “with 36 months for the study and 12 months for analysis.”
- **Reported-versus-comparator:** Page-32 named breakdown `36 + 12 = 48` months versus its printed 51-month total; page-11 reconciled breakdown `39 + 12 = 51`, with `36 + 3 = 39` as source context.
- **Reasoning procedure:** Treat the components explicitly named as a total-duration breakdown as additive, reproduce both page decompositions, and keep the adjacent three-month participation period as a possible source-grounded explanation rather than silently adding it to a sentence that omits it.
- **Calculation:** Page 11: `36 + 3 = 39` and `39 + 12 = 51`. Page 32's total sentence: `36 + 12 = 48`, three months below 51. Adding the separately stated participation period gives `36 + 3 + 12 = 51`, but page 32 does not state the sequential relationship in its total sentence.
- **Alternative source-grounded interpretations:** The p. 32 phrase “36 months for the study” may be shorthand for recruitment plus the final participant's three-month follow-up. Page 11 supports that intended schedule, but the p. 32 breakdown remains incomplete when read literally.
- **Mechanical evidence recheck:** Both cited pages were found and directly inspected. Every duration, both decompositions, the three-month difference, and the possible final-participant-follow-up interpretation were reproduced. Missing definitions are whether analysis overlaps follow-up and whether the final participation period is explicitly included after recruitment.
- **Quality-control relevance:** The evidence supports a bounded request to clarify one protocol timeline sentence. It does not establish an inconsistency in participant outcomes, effect estimates, or the article's scientific conclusion.
- **Potential downstream evidence impact:** If confirmed, a protocol timeline extractor could record 48 or 51 months, or misunderstand the recruitment/follow-up boundary. The package does not show actual propagation or a change to trial results.
- **Human verification steps:** Confirm the intended study timeline and whether the final participant's three-month follow-up follows recruitment; then state either 39 study months plus 12 analysis months or an explicit 36 + 3 + 12 decomposition on p. 32.
- **Evidence-card field audit:** The appended ledger entry supplies the core observation, locations, arithmetic, alternative, and human question. The complete recheck and this audit supply explicit quality relevance, bounded downstream impact, verification steps, and blank adjudication fields for the final report.
- **Unsupported-assumption audit:** The arithmetic mismatch is direct. Treating the adjacent three-month period as sequential and nonoverlapping is a plausible inference supported by p. 11, not an observed timing rule on p. 32.
- **Pagination and link audit:** Both citations identify actual protocol PDF pages. Internal footer numbering does not replace the truthful PDF page references.
- **Duplicate-relationship audit:** C006 concerns N027 and a protocol-duration breakdown. It does not duplicate any threshold, outcome, proportion, or P-value candidate.
- **Conclusion-impact audit:** No paper-level conclusion impact is claimed or source-established.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Bounded audit conclusion

The stable set C001-C006 has exact supplied-source support, reproducible comparisons, separated observation and inference, bounded human questions, truthful PDF pagination, and no display-zero-only basis. The six IDs are distinct after appropriate pre-ID merging, and no current stable ID should be removed or merged. The evidence audit is complete; the coordinator only needs to record the two completed stage statuses and ensure that later report generation returns the identical six-ID set.
