# Final Evidence-Quality Audit

## Audit scope and outcome

This audit used only the four supplied PDFs and the current fresh, manifested Workflow 1.5.2 artifacts. It covers every direct-source row, every coverage row, all 88 numeric/reporting relationships (`N001`-`N088`), all 45 inferential-statistical relationships (`S001`-`S045`), both statistical passes, all checker outputs in the fresh evidence chain, and every stable candidate (`C001`-`C007`). Every candidate remains **Pending Human Adjudication**. No scientific disposition, severity, ranking, acceptance, exclusion, or correction is assigned.

- Direct sources: 4 PDFs and 69 PDF-page units.
- Fresh-required units: 69/69; reusable units: 0/69; mapped units: 69/69.
- Numeric/reporting relationships: 88/88 completed without a count cap.
- Statistical relationships: 45/45 have one explicit `PASS_1_COMPLETE` record and one explicit `PASS_2_COMPLETE` record.
- Stable candidates: 7/7 returned in this canonical audit.
- Mechanical recheck: 7/7 stable IDs, with every current ledger locator resolving to the stated source page.

The audit identified two supportable omissions during its uncapped review of the checker calculations. They were appended without changing `C001`-`C005`: `C006` records the stat-call absolute-reduction arithmetic, and `C007` records the two urgent-PICU rate calculations. The coordinator repaired the ledger provenance, numeric checker, statistical passes, and mechanical recheck. No stable ID was deleted, merged, renumbered, ranked, or suppressed.

## Fresh-source, integrity, and legacy-exclusion audit

`source_coverage.md` contains exactly four direct-source rows: DOC-001 has 11 pages, DOC-002 has 37, DOC-003 has 7, and DOC-004 has 14. Each row has reusable units `0`, fresh-required units equal to total units, mapped units equal to total units, and `COMPLETE`. The row totals reconcile to 69. Fresh native and layout text exists for all 69 pages; 53 result-relevant pages were freshly rendered; native/layout text was usable, so no Tesseract OCR unit was needed. There are no direct Office, workbook, CSV, or other structured scientific sources.

The four current source hashes independently match `source_hashes_before.sha256`, `source_hashes_after.sha256`, and `source_inventory.md`. `pdfinfo` independently returns 11, 37, 7, and 14 pages. No source-integrity difference was found at this audit point.

The current canonical evidence chain expressly excludes legacy audit derivatives, web material, and external literature. The fresh coverage manifest and canonical relationship inventories point only to the fresh inventory, fresh evidence assets, current mapper parts, current checkers, ledger, recheck, and this audit. Unmanifested files left by the superseded tool-limited run were not evidence inputs. In particular, `preprocessing/tool_and_page_status.md`, `statistics/parts/main_statistical_relationships.md`, `statistics/parts/support_statistical_relationships.md`, and `checkers/candidate_parts/*.md` contain obsolete source-access statements or candidate-part records and are outside the current evidence chain. They remain preserved as required, but neither their zero-relationship conclusions nor their blocked-tool statements constrain this run.

## Coverage, relationship, and agent-execution audit

At the pre-finalization audit snapshot, `coverage_manifest.md` has 13 data rows and every required stage. Source and mapping assignments are disjoint and cover DOC-001 pp. 1-11, DOC-002 pp. 1-37, DOC-003 pp. 1-7, and DOC-004 pp. 1-14. Numeric scope explicitly enumerates `N001`-`N088`; each statistical-pass scope explicitly enumerates `S001`-`S045`; candidate registration and recheck enumerate the complete stable set. Every `Artifact` cell contains exactly one undecorated POSIX-style relative path. The coordinator must update the final `evidence_quality` and `report_generation` scopes to enumerate `C001, C002, C003, C004, C005, C006, C007` explicitly, rather than saying `Every stable C ID`, and mark each row `COMPLETE` only when its artifact is final.

The numeric checker now completes 88/88 records and contains five numeric-lane candidate records, including repaired N075/C007. Statistical pass 1 contains 45/45 explicit records and repaired S035/C006. Statistical pass 2 contains 45/45 explicit records, revisits the complete cross-lane ledger and the current 7/7 recheck, and reconciles C006 and C007 without creating a duplicate. Cross-source review covers all 88 `N` and all 45 `S` relationships after population, time, contrast, model, unit, scale, and precision matching. The stable ledger and recheck ID sets are identical to this audit's seven-ID set.

No discovery artifact applies a top-N rule, candidate target, desired count, review queue, or early-stopping boundary. The two candidates discovered during this final audit and appended after the initial five are affirmative evidence that discovery remained open through complete coverage.

`agent_execution_manifest.md` contains the coordinator exactly once and every current specialist exactly once at this snapshot, with one primary artifact per row. The required statistical reviewers are distinct non-placeholder fresh agents: `/root/statistics_pass_1` and `/root/statistics_pass_2`, both `gpt-5.6-terra`, `high`, and `FRESH_SPAWN`. Neither is a mapper or a Terra/medium execution. This final audit is separately manifested as `/root/quality_audit`, `gpt-5.6-sol`, `high`, `FRESH_SPAWN`. Any later report-generation or repair agent must be appended exactly once to both the execution manifest and token ledger.

## Candidate-card and adjudication-field requirements

The fresh final report is not yet assembled at this audit snapshot. Therefore every stable ID still needs a final report card containing every exact label required by `report_spec.md`: `Candidate statement`, `Category`, `Exact source locations`, `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Alternative source-grounded interpretations`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields`. Each source-PDF link must end in `#page=N`; from `.ai_paper_validation/final_report_1_5_2.md`, each supplied-source target must use `../FILENAME.pdf#page=N`.

The ledger and recheck do not instantiate human-adjudication subfields and contain no nonblank adjudication value. Every final card must use exactly this blank template:

```markdown
**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __
```

None of the seven candidates is based on `P = 0`, `p = 0.000`, or equivalent finite-precision display zero. The only relevant small-P notation is `<.0001`, which the statistical records correctly treat as threshold notation and not a candidate basis. No candidate needs the conditional `Independent contradiction beyond P=0 display` field.

## C001 — Inclusive versus exclusive fluid threshold in the SCD definition

- **Evidence and locator audit:** The main article prints `60 mL/kg or greater` on [`jama_parshuram_2018_oi_180015.pdf#page=4`](../../../jama_parshuram_2018_oi_180015.pdf#page=4); protocol Table 5 prints `>60ml/kg` on [`joi180015supp1_prod.pdf#page=24`](../../../joi180015supp1_prod.pdf#page=24); Supplement 3 eTable 1 prints `>60 ml/kg` on [`joi180015supp3_prod.pdf#page=6`](../../../joi180015supp3_prod.pdf#page=6). PDF page 6 is the correct Supplement 3 locator. The current ledger and recheck use it; no false pagination remains.
- **Rule and reproducibility:** At exactly `x = 60`, `x >= 60` is true and `x > 60` is false. This is a direct measure-definition boundary difference, and the assigned category `Measure, label, or scale inconsistency` follows `QUALITY_CONTROL_SCOPE.md`.
- **Assumptions and missing inputs:** Event-level exposures, rounding instructions for accumulated fluid, and the operational adjudication rule are absent. The card must not state that any patient's classification or any reported event count changed. Any typographic-error explanation remains inferential.
- **Duplicate and impact audit:** The numeric, cross-source, and statistical records compare the same operators, sources, and rule and were properly merged into one stable ID. C001 is distinct from all other candidates. A bounded downstream statement may say that a data extractor could copy different boundary definitions if the issue is confirmed; it must not claim propagation or conclusion change.
- **Card-field audit:** All common final-card fields listed above still need to be instantiated for C001. The calculation should include the `x = 60` truth-value comparison, the recheck should preserve missing boundary-case data, and every adjudication subfield must be `__`.
- **State:** Pending Human Adjudication.

## C002 — Mortality absolute-risk-reduction percent/unit conflict

- **Evidence and locator audit:** The matched planning statements resolve to [`joi180015supp1_prod.pdf#page=1`](../../../joi180015supp1_prod.pdf#page=1), [`joi180015supp1_prod.pdf#page=14`](../../../joi180015supp1_prod.pdf#page=14), [`joi180015supp1_prod.pdf#page=29`](../../../joi180015supp1_prod.pdf#page=29), and [`jama_parshuram_2018_oi_180015.pdf#page=4`](../../../jama_parshuram_2018_oi_180015.pdf#page=4). All current pagination is correct.
- **Rule and reproducibility:** `5.1 x 0.178 = 0.9078` per 1,000, equivalent to `0.09078%`. Thus `0.9 per 1,000` and `0.09%` agree to displayed precision, whereas `0.9%` equals 9 per 1,000 and is tenfold above 0.09%. The category `Cross-document numeric inconsistency` is allowed and source-grounded.
- **Assumptions and missing inputs:** The package does not identify the intended editorial replacement on page 29. The card may describe a possible percent-sign or decimal transcription mechanism only as an inference; it must not prescribe a final correction or infer a changed power calculation.
- **Duplicate and impact audit:** NC-01, CS-02, and P1-01 concern the same baseline, relative reduction, absolute reduction, and scale conversion and were properly merged. A bounded downstream statement may identify the planning absolute reduction that an extractor could copy; it must not claim actual reuse or a conclusion effect.
- **Card-field audit:** All common final-card fields still need to be instantiated for C002. The calculation must show both per-1,000 and percent conversion, the alternatives must retain `0.09%` versus `0.9 per 1,000`, and every adjudication subfield must be `__`.
- **State:** Pending Human Adjudication.

## C003 — Cardiac-arrest events assigned incompatible resuscitation-scale categories

- **Evidence and locator audit:** The source passages resolve to [`joi180015supp1_prod.pdf#page=11`](../../../joi180015supp1_prod.pdf#page=11), [`joi180015supp1_prod.pdf#page=24`](../../../joi180015supp1_prod.pdf#page=24), and [`joi180015supp1_prod.pdf#page=27`](../../../joi180015supp1_prod.pdf#page=27). Page 11 says cardiac arrest is rated 6 or 7; Table 5 assigns CPR/death to 6/7; the Table 6 legend says events including cardiac arrest have `scale rating 4 or 5`.
- **Rule and reproducibility:** `{4,5}` and `{6,7}` do not overlap. The comparison is reproducible if page 27 refers to the seven-category Children's Resuscitation Intensity Scale. Page 27 does not name the scale, so the final card must retain the conditional comparator and the possibility of an undefined second scale. `Measure, label, or scale inconsistency` is the appropriate category.
- **Assumptions and missing inputs:** A Table-6-specific scale definition, operational abstraction manual, and version history are absent. The report must not assume that page 27 necessarily names the Children's scale or that event selection changed.
- **Duplicate and impact audit:** C003 concerns a seven-category resuscitation-intensity label; C004 concerns a separate six-point preventability threshold. They are not duplicates. A bounded downstream statement may identify the category codes that could be copied if C003 is confirmed, without asserting altered results.
- **Card-field audit:** All common final-card fields still need to be instantiated for C003. The reasoning must state the conditional same-scale rule and missing alternative scale definition; every adjudication subfield must be `__`.
- **State:** Pending Human Adjudication.

## C004 — Preventability threshold excludes and includes rating 4

- **Evidence and locator audit:** The threshold statements resolve to [`joi180015supp1_prod.pdf#page=11`](../../../joi180015supp1_prod.pdf#page=11), [`joi180015supp1_prod.pdf#page=28`](../../../joi180015supp1_prod.pdf#page=28), [`joi180015supp3_prod.pdf#page=6`](../../../joi180015supp3_prod.pdf#page=6), and [`jama_parshuram_2018_oi_180015.pdf#page=7`](../../../jama_parshuram_2018_oi_180015.pdf#page=7). PDF page 6 is the correct Supplement 3 locator. No false pagination remains in the current ledger or recheck.
- **Rule and reproducibility:** On the stated six-point scale, `>4` selects ratings 5 and 6, while `4 or more` and the explicit 4-6 list include rating 4. Evaluating rating 4 reproduces the contradiction. The category `Measure, label, or scale inconsistency` follows the scope.
- **Assumptions and missing inputs:** Operational adjudication instructions and rating-level event data are absent. The card must not assume that the strict sign is typographical or that reported potentially preventable-arrest counts changed.
- **Duplicate and impact audit:** The p.11 text, Table 7, final article, and Supplement 3 compare the same threshold and were properly merged. C004 is distinct from C003's different scale and comparator. A bounded downstream statement may identify the threshold a reviewer could extract, without asserting propagation.
- **Card-field audit:** All common final-card fields still need to be instantiated for C004. The calculation should show `4 > 4` is false and `4 >= 4` is true; every adjudication subfield must be `__`.
- **State:** Pending Human Adjudication.

## C005 — The same SCDE reference count is labelled annual and two-year

- **Evidence and locator audit:** Both matched passages resolve to [`joi180015supp1_prod.pdf#page=14`](../../../joi180015supp1_prod.pdf#page=14) and [`joi180015supp1_prod.pdf#page=30`](../../../joi180015supp1_prod.pdf#page=30). Page 14 attaches `/ year` to 1,052 urgent ICU admissions; page 30 describes the same four-hospital count as a two-year total.
- **Rule and reproducibility:** If 1,052 is an unannualized two-year count, its simple annual average is `1052 / 2 = 526`. Using page-30 values diagnostically, `1052 x 0.40 = 420.8`, `55,963 x 4 = 223,852`, and `420.8 / 223,852 x 1,000 = 1.88`, approximately the printed 2 per 1,000. This supports the period/denominator question but does not establish an exact cohort patient-day denominator. `Denominator, proportion, or total inconsistency` is within scope.
- **Assumptions and missing inputs:** Year-stratified counts and the exact four-hospital patient-day denominator are absent. The four-day stay is a printed planning assumption and must not be presented as observed cohort patient-time. Neither period label should be declared the correction.
- **Duplicate and impact audit:** C005 concerns the time basis of the 1,052 count. C007 uses the same page-30 numerator but different denominators and a different rate-rounding rule, so it is not a duplicate. A bounded downstream statement may identify the period/rate input an extractor could copy if confirmed.
- **Card-field audit:** All common final-card fields still need to be instantiated for C005. The calculation must label the 1.88-per-1,000 reconstruction as diagnostic and approximate; every adjudication subfield must be `__`.
- **State:** Pending Human Adjudication.

## C006 — Stat-call absolute reduction does not reproduce from the printed inputs

- **Evidence and locator audit:** The complete matched statement is on [`joi180015supp1_prod.pdf#page=30`](../../../joi180015supp1_prod.pdf#page=30). The corrected primary provenance is S035 only; unrelated N075 is not assigned to C006.
- **Rule and reproducibility:** The printed baseline rate 8.13 per 1,000 multiplied by the printed relative reduction 0.181 is `1.47153` per 1,000, conventionally `1.47`, not the printed `1.45`. Nearest-display bounds reproduce as `8.125 x 0.1805 = 1.4665625` through values below `8.135 x 0.1815 = 1.4765025`; that interval does not overlap the `1.445` to below `1.455` interval that would display as 1.45. `Numeric or arithmetic inconsistency` is the appropriate category.
- **Assumptions and missing inputs:** Unrounded power-calculation inputs and output are absent. A different hidden input, transcription step, or nonstandard display method is only an alternative explanation. The report must not prescribe which printed number should change or claim an effect on trial results.
- **Duplicate and impact audit:** C006 concerns the stat-call baseline and relative-reduction product. It is distinct from C002's mortality unit conversion and from C007's urgent-PICU rates. A bounded downstream statement may identify the planned stat-call absolute reduction that could be extracted if C006 is confirmed.
- **Card-field audit:** All common final-card fields still need to be instantiated for C006. The calculation and rounding-bound intervals should be retained, and every adjudication subfield must be `__`.
- **State:** Pending Human Adjudication.

## C007 — Urgent PICU admission rates do not match the printed counts and denominators at conventional rounding

- **Evidence and locator audit:** The table and its explanatory paragraph are on [`joi180015supp1_prod.pdf#page=30`](../../../joi180015supp1_prod.pdf#page=30). The corrected primary provenance is N075 only; S033 is not assigned to C007.
- **Rule and reproducibility:** `1052 / 7300 x 100 = 14.4109589%`, conventionally 14.4% to one decimal rather than 14.5%. `1052 / 55963 x 1,000 = 18.7977778`, conventionally 19 to a whole number rather than 18. The first display would require a denominator from 7,231 through 7,280 under nearest one-decimal rounding; the second would require a denominator from 56,865 through 60,114 under nearest whole-number rounding. The printed denominators are outside those respective ranges. `Denominator, proportion, or total inconsistency` follows the scope.
- **Assumptions and missing inputs:** Alternative source denominators, a weighted rate, a data-extract history, and the display convention are absent. Truncation could explain 18 but would not explain 14.5 from 14.4109589, so no single documented rule reconciles both. The final report must frame conventional rounding as the stated diagnostic rule and preserve the human question.
- **Duplicate and impact audit:** C007 differs from C005 because it compares printed numerator/denominator rate identities, not the annual-versus-two-year period label. It differs from C006 because it concerns another quantity and rule. A bounded downstream statement may identify the two displayed urgent-PICU rates that could be copied if C007 is confirmed; it must not assert downstream propagation.
- **Card-field audit:** All common final-card fields still need to be instantiated for C007. The report should reproduce both calculations, name the missing rounding convention, and set every adjudication subfield to `__`.
- **State:** Pending Human Adjudication.

## Coordinator finalization requirements

1. Update the `evidence_quality` and `report_generation` coverage scopes to enumerate `C001, C002, C003, C004, C005, C006, C007`, then mark each complete only after its current artifact is final.
2. Generate every final report card with the exact required labels, page-addressable links, bounded impact language, and five exact `__` adjudication placeholders. The final report, ledger, recheck, and quality-audit heading sets must all equal `C001`-`C007`.
3. Preserve the explicit exclusion of unmanifested legacy, tool-limited derivatives from the fresh evidence chain. Do not cite their blocked-source or empty-inventory statements.
4. Finalize `run_state.md`, append every later manifested response to the authoritative token ledger, recompute token summaries, recompute source hashes, render the standalone HTML, and repair validation defects until the versioned validator reports `PASS`.

## Audit limitations

The supplied package has no event-level dataset, fitted-model covariance output, adjudication manual, document-version history, exact four-hospital patient-day denominator, original power-calculation output, or documented rounding convention for the page-30 table. These absences limit resolution of the seven human questions and any assessment of numeric consequence. They do not prevent reproduction of the printed comparisons recorded here. The audit confirms reporting-consistency candidates only and makes no claim about paper-level conclusions or actual downstream use.
