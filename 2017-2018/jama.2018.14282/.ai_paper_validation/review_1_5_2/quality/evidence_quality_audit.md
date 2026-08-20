# Final Evidence-Quality Audit

## Audit status

This fresh Workflow 1.5.2 audit covers every stable candidate, every current coverage-manifest row, every source-coverage row, the complete numeric and statistical relationship inventories, both statistical passes, the candidate ledger, the mechanical evidence recheck, and every current agent-manifest row. The evidence set is **conditionally ready for report generation after the bounded coordinator actions below**. All 28 candidates remain **Pending Human Adjudication**. This artifact does not rank, suppress, merge, renumber, or adjudicate any candidate.

- **Stable candidate coverage:** 28/28 (`C001` through `C028`).
- **Numeric relationship coverage:** 54/54 (`N001` through `N054`) have explicit checker outcomes.
- **Statistical relationship coverage:** 38/38 (`S001` through `S038`) have explicit `PASS_1_COMPLETE` and `PASS_2_COMPLETE` outcomes.
- **Stable-ID equality at this stage:** candidate ledger = mechanical evidence recheck = this quality audit = `C001` through `C028`, with no extra or missing ID.
- **Source coverage:** 4/4 direct-source rows complete; 144 total units = 144 fresh-required units = 144 mapped units; reusable units are zero.
- **Source integrity:** the four current direct-source SHA-256 values exactly match `source_hashes_before.sha256`.
- **Evidence provenance:** the fresh inventory, evidence-asset inventory, run state, cross-source checker, and second statistical pass all state that legacy audit derivatives were not evidence inputs. No web evidence was used. All 40 candidate-ledger and 42 evidence-recheck PDF links resolve and end in `#page=N`; a separate 80-link relative-path defect in three mapping artifacts requires repair as stated below.
- **Discovery boundary:** the numeric checker covers every `N` record, both statistical passes cover every `S` record, cross-source review covers all 92 relationships, and merge accounting retains every distinct qualifying observation. No target, top-N rule, review queue, candidate cap, or early stopping boundary is present in the fresh discovery chain.
- **Display-zero exclusion:** no stable candidate is based on `P = 0`, `p = 0.000`, or equivalent. Both statistical passes record zero display-zero occurrences. No candidate card mentions a display-zero P value, so the conditional independent-contradiction field is not applicable to the present ledger.
- **Scientific boundary and tone:** all categories are permitted by `QUALITY_CONTROL_SCOPE.md`; descriptions are neutral quality-control observations; none asserts paper invalidity, severity, a scientific disposition, a required correction, or conclusion change.

## Bounded coordinator actions before final completion

1. Change the `evidence_quality` coverage row from `PENDING` to `COMPLETE` now that this canonical artifact exists. Do not alter its exact 28-ID scope or its single artifact path.
2. Generate the final Markdown report with all 28 cards, then change the `report_generation` row from `PENDING` to `COMPLETE`. At audit time the report artifact is not yet present, which is expected from stage order but prevents final validation now.
3. Add the fresh report-generation agent to `agent_execution_manifest.md` exactly once when spawned, and later include that agent in the token ledger. The current manifest is complete for the coordinator and the nine specialists used through this audit.
4. For `C023` and `C024`, use the repaired wording in the stable ledger, mechanical recheck, and statistical pass 2. Do not repeat the stronger stale wording in the earlier cross-source/pass-1 provenance that direct reciprocals of every already-rounded endpoint reproduce exactly.
5. For `C018`, preserve the source's introductory phrase `In the overall population`; frame the issue narrowly as denominator communication and possible arm-risk misreading, not as proof that the overall denominator is erroneous.
6. For `C025`, cite DOC-002 p.91 when using the published-protocol abstract's `778 patients overall` sentence because that sentence begins on p.90 and completes on p.91. DOC-002 p.103 independently contains the full `778 patients (389 in each group)` comparator.
7. Every final report card must contain all exact labels required by `report_spec.md`. The final report does not yet exist, so all final-card labels are currently pending for every ID. In particular, the ledger is not a substitute for the missing `Candidate statement`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Alternative source-grounded interpretations`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields` labels. Preserve the already available category, source-location, and source-evidence content.
8. In every final card, bound potential downstream impact to the exact value, label, interval, test name, or denominator that a data extractor or evidence synthesis could copy if the candidate is confirmed. Do not claim that propagation or a conclusion change occurred.
9. Use this exact blank template in every final card; no human-adjudication value is supplied by this audit:

   **Human adjudication fields:**
   - **Validity:** __
   - **Importance:** __
   - **Action:** __
   - **Initials:** __
   - **Notes:** __
10. Repair 80 mapping-artifact PDF links before report completion. In `extraction/support_quantitative_evidence.md`, 22 bare source-PDF targets require the package-root prefix `../../../`. In `relationships/parts/main_numeric.md`, 37 targets, and in `statistics/parts/main_statistical.md`, 21 targets, require `../../../../` rather than `../../../` from their respective `parts/` directories. Preserve every `#page=N` fragment and source filename. Re-run a relative-link existence check after the repair. This defect does not affect the correctly resolving ledger/recheck links or the source facts already rechecked.

## Source-coverage row audit

| Source ID | Row audit | Unit equality | Result |
|---|---|---|---|
| DOC-001 | `jama_azoulay_2018_oi_180109.pdf`, PDF pages 1-9 | total 9 = fresh-required 9 = mapped 9; reusable 0 | COMPLETE |
| DOC-002 | `joi180109supp1_prod.pdf`, PDF pages 1-129 | total 129 = fresh-required 129 = mapped 129; reusable 0 | COMPLETE |
| DOC-003 | `joi180109supp2_prod.pdf`, PDF pages 1-5 | total 5 = fresh-required 5 = mapped 5; reusable 0 | COMPLETE |
| DOC-004 | `joi180109supp3_prod.pdf`, PDF page 1 | total 1 = fresh-required 1 = mapped 1; reusable 0 | COMPLETE |

The source-row total is 144, exactly matching `run_state.md`. Every direct source has fresh native and layout text per stable page. Render/OCR decisions are recorded for all 144 pages; zero OCR pages is supported because native/layout text is usable for every result-relevant page. DOC-002 pp.78 and 129 are explicitly sparse non-result units.

## Coverage-manifest row audit

Each listed artifact cell contains one undecorated relative POSIX path. Every completed-row artifact resolves. The two pending-stage observations are the bounded coordinator actions already stated.

| Stage / shard | Exact-scope audit | One-path audit | Audit result |
|---|---|---|---|
| `source_inventory` / `inventory-001` | All 144 direct PDF pages enumerated | `source_inventory.md` resolves | COMPLETE |
| `evidence_assets` / `assets-001` | All four direct sources and 144 pages | `evidence_asset_inventory.md` resolves | COMPLETE |
| `evidence_assets` / `assets-002` | All 144 page-level decisions | `preprocessing/page_unit_register.md` resolves | COMPLETE |
| `main_evidence_mapping` / `main-001` | DOC-001 pp.1-9 | `extraction/main_quantitative_evidence.md` resolves | COMPLETE |
| `main_evidence_mapping` / `main-002` | DOC-001 numeric scope | `relationships/parts/main_numeric.md` resolves | COMPLETE |
| `main_evidence_mapping` / `main-003` | DOC-001 statistical scope | `statistics/parts/main_statistical.md` resolves | COMPLETE |
| `support_evidence_mapping` / `support-001` | DOC-002 pp.1-129, DOC-003 pp.1-5, DOC-004 p.1 | `extraction/support_quantitative_evidence.md` resolves | COMPLETE |
| `support_evidence_mapping` / `support-002` | All 135 support numeric pages | `relationships/parts/support_numeric.md` resolves | COMPLETE |
| `support_evidence_mapping` / `support-003` | All 135 support statistical pages | `statistics/parts/support_statistical.md` resolves | COMPLETE |
| `numeric_checks` / `numeric-001` | Every ID `N001` through `N054` is individually enumerated | `checkers/numeric_consistency.md` resolves | COMPLETE |
| `statistics_pass_1` / `statistics-001` | Every ID `S001` through `S038` is individually enumerated | `checkers/statistical_pass_1.md` resolves | COMPLETE |
| `cross_source_checks` / `cross-001` | All matched results across DOC-001 through DOC-004 | `checkers/cross_source_consistency.md` resolves | COMPLETE |
| `candidate_registration` / `candidates-001` | Every ID `C001` through `C028` is individually enumerated | `candidate_ledger.md` resolves | COMPLETE |
| `evidence_recheck` / `recheck-001` | Every ID `C001` through `C028` is individually enumerated | `verification/evidence_recheck.md` resolves | COMPLETE |
| `statistics_pass_2` / `statistics-002` | Every `S` ID, every `C` ID, and all recheck facts are enumerated | `checkers/statistical_pass_2.md` resolves | COMPLETE |
| `evidence_quality` / `quality-001` | Every `C` ID plus every coverage/source/agent row | `quality/evidence_quality_audit.md` now resolves | COMPLETE IN SUBSTANCE; coordinator must update row status |
| `report_generation` / `report-001` | Every `C` ID and all required metadata are enumerated | `../final_report_1_5_2.md` not yet present | PENDING BY STAGE; must become COMPLETE after report generation |

## Agent-execution and statistical-pass audit

The current manifest has ten distinct rows: the current coordinator and nine specialists through this quality audit. The coordinator occurs exactly once. Every current artifact path resolves after creation of this audit. Fresh preprocessing, main mapping, support mapping, numeric review, cross-source review, evidence recheck, and evidence-quality roles use the required model/effort combinations shown by the manifest.

| Stage | Agent-ID audit | Model / effort / start audit | Primary artifact audit |
|---|---|---|---|
| coordinator | `COORDINATOR-CURRENT-SESSION`, one row | `gpt-5.6-sol` / `high` / `CURRENT_SESSION` | `run_state.md` resolves |
| fresh_source_preprocessing | `/root/fresh_preprocessing`, one row | `gpt-5.6-terra` / `medium` / `FRESH_SPAWN` | `evidence_asset_inventory.md` resolves |
| main_quantitative_mapping | `/root/main_mapping`, one row | `gpt-5.6-terra` / `medium` / `FRESH_SPAWN` | `extraction/main_quantitative_evidence.md` resolves |
| support_quantitative_mapping | `/root/support_mapping`, one row | `gpt-5.6-terra` / `medium` / `FRESH_SPAWN` | `extraction/support_quantitative_evidence.md` resolves |
| numeric_checks | `/root/numeric_review`, one row | `gpt-5.6-terra` / `medium` / `FRESH_SPAWN` | `checkers/numeric_consistency.md` resolves |
| cross_source_checks | `/root/cross_source_review`, one row | `gpt-5.6-terra` / `medium` / `FRESH_SPAWN` | `checkers/cross_source_consistency.md` resolves |
| statistics_pass_1 | `/root/statistics_pass_1`, one row | `gpt-5.6-terra` / `high` / `FRESH_SPAWN` | `checkers/statistical_pass_1.md` resolves |
| evidence_recheck | `/root/evidence_recheck`, one row | `gpt-5.6-sol` / `high` / `FRESH_SPAWN` | `verification/evidence_recheck.md` resolves |
| statistics_pass_2 | `/root/statistics_pass_2`, one row | `gpt-5.6-terra` / `high` / `FRESH_SPAWN` | `checkers/statistical_pass_2.md` resolves |
| evidence_quality | `/root/quality_audit`, one row | `gpt-5.6-sol` / `high` / `FRESH_SPAWN` | `quality/evidence_quality_audit.md` resolves |

- Statistical pass 1: agent `/root/statistics_pass_1`; model `gpt-5.6-terra`; effort `high`; start mode `FRESH_SPAWN`; artifact `checkers/statistical_pass_1.md`; 38/38 `S` IDs complete.
- Statistical pass 2: agent `/root/statistics_pass_2`; model `gpt-5.6-terra`; effort `high`; start mode `FRESH_SPAWN`; artifact `checkers/statistical_pass_2.md`; 38/38 `S` IDs and 28/28 `C` IDs complete.
- The two statistical runtime IDs are non-placeholder, fresh, and distinct. Neither is a mapper reused through follow-up.
- The report generator does not yet appear because it has not yet run. The coordinator must append it exactly once and must not overwrite another agent row.

## Relationship and duplicate-accounting audit

The numeric inventory is contiguous from `N001` to `N054`, including explicit no-applicable records `N032` and `N054`. The numeric checker gives one explicit outcome for each record and emits `NC001` through `NC021`. The statistical inventory is contiguous from `S001` to `S038`, including no-applicable `S021`; pass 1 and pass 2 each give one explicit completion outcome for all 38 IDs. Cross-source review covers the union of all 92 relationships. Pass 2 revisits the complete ledger and emits zero new candidates.

Merge accounting is reproducible and does not suppress similar-but-distinct printed relationships: `NC001`-`NC021` map one-to-one to `C001`-`C021`; `XC001` and `SC002` map to `C017`; `XC002` and `SC007` map to `C022`; mortality and IMV portions of the reciprocal-orientation observation remain distinct as `C023` and `C024`; `XC005` and `SC001` map to `C025`; and `SC004`-`SC006` map to `C026`-`C028`. Complementary pairs `C001`/`C002` and `C020`/`C021` concern different printed count-percentage pairs and therefore are not genuine duplicates under the contract. No stable ID may be merged after registration.

## Candidate-by-candidate audit

For every section below, the final report card is not yet present; therefore all exact final-card labels identified in the report-card gate above remain pending. The source links in the ledger and recheck resolve, every PDF link ends in `#page=N`, and every section retains the exact blank human-adjudication template through the global requirement above.

## C001 — Standard-arm men percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Evidence audit:** DOC-001 p.4 prints standard-arm `n=388` and men `247 (63.6)`; `247/388×100=63.6598%`, nearest one-decimal `63.7%`. Source location and calculation reproduce.
- **Category/pagination/duplicate audit:** Permitted denominator/proportion category; PDF p.4 is correct; distinct from C002 because it concerns a different printed count-percentage pair.
- **Assumptions and limitations:** Nearest one-decimal rounding is diagnostic; the source does not supply its production rule. The complementary sex percentages total 100.0%, so an adjusted paired display is possible.
- **Report repair:** State the missing rounding rule, avoid prescribing a replacement, and bound downstream relevance to extraction of the printed male proportion.

## C002 — Standard-arm women percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Evidence audit:** DOC-001 p.4 prints women `141 (36.4)` under `n=388`; `141/388×100=36.3402%`, nearest one-decimal `36.3%`. Source and calculation reproduce.
- **Category/pagination/duplicate audit:** Permitted denominator/proportion category; p.4 is correct; different printed pair from C001.
- **Assumptions and limitations:** The paired sex percentages sum to 100.0%; forced-complement or adjusted rounding is source-grounded but undocumented.
- **Report repair:** Present the rounding rule as the human question and bound relevance to extraction of the printed female proportion.

## C003 — Standard-arm heart-failure percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Evidence audit:** DOC-001 p.4 prints `27 (6.9)` under `n=388`; `27/388×100=6.9588%`, nearest one-decimal `7.0%`.
- **Category/pagination/duplicate audit:** Permitted denominator/proportion category; p.4 is correct; no duplicate relationship.
- **Assumptions and limitations:** No row-specific nonmissing denominator or rounding rule is supplied.
- **Report repair:** Keep alternate-denominator and rounding explanations conditional; bound downstream relevance to the baseline heart-failure proportion.

## C004 — High-flow liver-disease percentage conflicts with displayed count

- **Status:** Pending Human Adjudication.
- **Evidence audit:** DOC-001 p.4 prints `45 (13.3)` under `n=388`; `45/388×100=11.5979%`, or `11.6%` to one decimal. The 1.7-point gap reproduces.
- **Category/pagination/duplicate audit:** Permitted denominator/proportion category; p.4 is correct; no duplicate.
- **Assumptions and limitations:** A row-specific denominator near 338, transcription, or placement issue is possible but not printed; do not select among them.
- **Report repair:** Ask which count, percentage, or denominator is intended; do not state a final correction or conclusion effect.

## C005 — Standard-arm kidney-disease percentage conflicts with displayed count

- **Status:** Pending Human Adjudication.
- **Evidence audit:** DOC-001 p.4 prints `69 (20.4)` under `n=388`; `69/388×100=17.7835%`, or `17.8%`. The 2.6-point gap reproduces.
- **Category/pagination/duplicate audit:** Permitted denominator/proportion category; p.4 is correct; no duplicate.
- **Assumptions and limitations:** A hidden denominator near 338 or transcription/placement issue is possible but unsupported as a chosen explanation.
- **Report repair:** Preserve the unresolved choice among count, percentage, and denominator; bound relevance to baseline kidney-disease extraction.

## C006 — Standard-arm nontransplant immunosuppression percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Evidence audit:** DOC-001 p.4 prints `98 (25.2)` under `n=388`; `98/388×100=25.2577%`, nearest one-decimal `25.3%`. The child counts `98+37=135` reconcile to their parent.
- **Category/pagination/duplicate audit:** Permitted denominator/proportion category; p.4 is correct; no duplicate.
- **Assumptions and limitations:** An undocumented adjustment across child percentages is possible; the count subtotal itself is coherent.
- **Report repair:** Separate the percentage-rounding observation from the correct count subtotal.

## C007 — High-flow at least 3-days-after-ICU-admission percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Evidence audit:** DOC-001 p.4 prints `20 (5.1)` under `n=388`; `20/388×100=5.1546%`, nearest one-decimal `5.2%`; timing counts sum to 388.
- **Category/pagination/duplicate audit:** Permitted denominator/proportion category; p.4 is correct; distinct from C008 because it is the high-flow arm's printed pair.
- **Assumptions and limitations:** A category-level adjustment is possible but undocumented.
- **Report repair:** Preserve the correct timing-count subtotal and frame only the displayed percentage rule as unresolved.

## C008 — Standard-arm at least 3-days-after-ICU-admission percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Evidence audit:** DOC-001 p.4 prints `20 (5.1)` under `n=388`; `20/388×100=5.1546%`, nearest one-decimal `5.2%`; timing counts sum to 388.
- **Category/pagination/duplicate audit:** Permitted denominator/proportion category; p.4 is correct; distinct from C007 because it is the standard arm's printed pair.
- **Assumptions and limitations:** A category-level adjustment is possible but undocumented.
- **Report repair:** Do not imply the count subtotal is wrong; ask for the percentage-production rule.

## C009 — Standard-arm vasopressor percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Evidence audit:** DOC-001 p.4 prints `39 (10.0)` under `n=388`; `39/388×100=10.0515%`, nearest one-decimal `10.1%`.
- **Category/pagination/duplicate audit:** Permitted denominator/proportion category; p.4 is correct; no duplicate.
- **Assumptions and limitations:** Truncation or a hidden denominator could explain the last-place difference, but neither is documented.
- **Report repair:** Keep the discrepancy small and conditional; bound relevance to extraction of the baseline vasopressor proportion.

## C010 — High-flow do-not-intubate percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Evidence audit:** DOC-001 p.4 prints `13 (3.3)` under `n=388`; `13/388×100=3.3505%`, nearest one-decimal `3.4%`.
- **Category/pagination/duplicate audit:** Permitted denominator/proportion category; p.4 is correct; no duplicate.
- **Assumptions and limitations:** Decimal truncation would reproduce 3.3%, but no uniform truncation policy is supplied.
- **Report repair:** State the production rule as missing and avoid asserting which displayed component changes.

## C011 — High-flow do-not-resuscitate percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Evidence audit:** DOC-001 p.4 prints `3 (0.7)` under `n=388`; `3/388×100=0.7732%`, nearest one-decimal `0.8%`.
- **Category/pagination/duplicate audit:** Permitted denominator/proportion category; p.4 is correct; no duplicate.
- **Assumptions and limitations:** Truncation is possible but unstated.
- **Report repair:** Frame as a small display-rule question and bound impact to copying the baseline percentage.

## C012 — Standard-arm do-not-resuscitate percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Evidence audit:** DOC-001 p.4 prints `1 (0.2)` under `n=388`; `1/388×100=0.2577%`, nearest one-decimal `0.3%`.
- **Category/pagination/duplicate audit:** Permitted denominator/proportion category; p.4 is correct; no duplicate.
- **Assumptions and limitations:** Truncation is possible but unstated.
- **Report repair:** Do not infer a changed count; keep the human question limited to denominator/rounding.

## C013 — Standard-arm unknown-goals percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Evidence audit:** DOC-001 p.4 prints `27 (6.9)` under `n=388`; `27/388×100=6.9588%`, nearest one-decimal `7.0%`; all five goal-of-care counts sum to 388.
- **Category/pagination/duplicate audit:** Permitted denominator/proportion category; p.4 is correct; no duplicate.
- **Assumptions and limitations:** An adjusted display across exhaustive categories is possible; the count distribution is complete.
- **Report repair:** Preserve the correct subtotal and limit the observation to percentage production.

## C014 — High-flow pre-randomization standard-oxygen percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Evidence audit:** DOC-001 p.4 prints `311 (80.1)` under `n=388`; `311/388×100=80.1546%`, nearest one-decimal `80.2%`.
- **Category/pagination/duplicate audit:** Permitted denominator/proportion category; p.4 is correct; no duplicate.
- **Assumptions and limitations:** A data-availability denominator is conceivable, but no missingness count or alternate denominator is printed.
- **Report repair:** Keep restricted-denominator reasoning explicitly conditional and bound relevance to baseline-treatment extraction.

## C015 — High-flow ICU-acquired-infection percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Evidence audit:** DOC-001 p.5 prints `39 (10.0)` under `n=388`; `39/388×100=10.0515%`, nearest one-decimal `10.1%`; the standard comparator `41/388=10.6%` reconciles.
- **Category/pagination/duplicate audit:** Permitted denominator/proportion category; p.5 is correct; distinct from C019 because this is the reported ICU-acquired-infection outcome, not six-hour invasive ventilation.
- **Assumptions and limitations:** An infection-at-risk denominator is possible but not supplied in Table 2.
- **Report repair:** Do not equate this with C019 solely because both print `39 (10.0)`; preserve the different outcome and source.

## C016 — Standard-arm hospital-mortality percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Evidence audit:** DOC-001 p.5 prints `162 (41.7)` under `n=388`; `162/388×100=41.7526%`, nearest one-decimal `41.8%`; no loss to follow-up is printed.
- **Category/pagination/duplicate audit:** Permitted denominator/proportion category; p.5 is correct; no duplicate.
- **Assumptions and limitations:** An alternate hospital-disposition denominator is not supplied.
- **Report repair:** Ask for the production denominator/rounding rule; do not infer an effect on the mortality comparison.

## C017 — Respiratory-rate confidence-interval endpoint differs between matched occurrences

- **Status:** Pending Human Adjudication.
- **Evidence audit:** DOC-001 p.1 and p.6 describe the same six-hour 25/min versus 26/min comparison and difference `-1.8`, but print upper 95% CI endpoints `-0.2` and `-0.3`; the difference is 0.1/min.
- **Category/pagination/duplicate audit:** Permitted cross-location numeric category; both pages are correct; numeric, cross-source, and statistical observations are genuine duplicates already merged into one stable ID.
- **Assumptions and limitations:** Unrounded endpoints, model identity, and display rule are absent. Separate hidden-precision calculations remain possible.
- **Report repair:** Do not claim the interval changes inference; ask which interval/model/rounding basis is authoritative.

## C018 — Arm-attributed support-needs percentages use the overall-trial denominator

- **Status:** Pending Human Adjudication.
- **Evidence audit:** DOC-001 p.6 prints 153 high-flow patients (19.7%) and 31 standard patients (4.0%). These percentages reproduce with 776 overall, while within-arm values are 39.4% and 8.0%.
- **Category/pagination/duplicate audit:** Permitted denominator/label observation; p.6 is correct; no duplicate.
- **Assumptions and limitations:** The paragraph expressly begins `In the overall population`, which supports intentional use of the overall denominator. The unresolved quality-control issue is whether the arm-attributed syntax can be misread as within-arm risk, not whether 776 is arithmetically wrong.
- **Report repair:** Include the introductory phrase and use neutral denominator-communication wording; do not present this as a demonstrated erroneous calculation.

## C019 — eTable high-flow invasive-MV percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Evidence audit:** DOC-003 p.2 prints high-flow `N=388` and invasive mechanical ventilation `39 (10.0)`; `39/388×100=10.0515%`, nearest one-decimal `10.1%`; `39+349=388`.
- **Category/pagination/duplicate audit:** Permitted denominator/proportion category; p.2 is correct; not a duplicate of C015 because outcome, time, and source display differ.
- **Assumptions and limitations:** A six-hour evaluable denominator or truncation is possible but not printed.
- **Report repair:** Keep the complementary count identity separate from the percentage-display question.

## C020 — eTable standard-arm invasive-MV percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Evidence audit:** DOC-003 p.2 prints `46 (11.8)` under `N=388`; `46/388×100=11.8557%`, nearest one-decimal `11.9%`; `46+342=388`.
- **Category/pagination/duplicate audit:** Permitted denominator/proportion category; p.2 is correct; distinct from C021 because it concerns the invasive-MV pair.
- **Assumptions and limitations:** The printed 11.8%/88.2% pair totals 100.0%, supporting a possible forced-complement display rule that is not documented.
- **Report repair:** Present complementary adjustment as an alternative, not a disposition.

## C021 — eTable standard-oxygen-only percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Evidence audit:** DOC-003 p.2 prints `342 (88.2)` under `N=388`; `342/388×100=88.1443%`, nearest one-decimal `88.1%`; `342+46=388`.
- **Category/pagination/duplicate audit:** Permitted denominator/proportion category; p.2 is correct; distinct from C020 because it concerns the standard-oxygen-only pair.
- **Assumptions and limitations:** 88.2% is exactly the complement of printed 11.8%, so the source may have forced complementary percentages.
- **Report repair:** Ask whether the value was independently calculated or set as the complement; do not merge with C020.

## C022 — IMV cumulative-incidence comparison has incompatible printed test labels

- **Status:** Pending Human Adjudication.
- **Evidence audit:** DOC-001 p.4 specifies competing-risk cumulative incidence and Gray testing; DOC-001 p.6 reports the linked IMV result; DOC-003 p.3 titles the matched cumulative-incidence figure and prints `P (log Rank test) = 0.17`. The named procedures differ even though the rounded P values match.
- **Category/pagination/duplicate audit:** Permitted statistical-reporting category; all three pages are correct; cross-source and statistical observations are genuine duplicates already merged.
- **Assumptions and limitations:** Test statistics, event/censoring data, and generating output are absent. Equal rounded P values do not establish identical procedures.
- **Report repair:** Ask which test generated each P=.17 and do not reconstruct significance or claim a conclusion effect.

## C023 — Figure 3A mortality HR has a near-reciprocal orientation relative to Table 2

- **Status:** Pending Human Adjudication.
- **Evidence audit:** DOC-001 p.5 prints mortality HR `0.98 (0.77-1.24)` and p.7 prints `1.02 (0.81-1.29)` for the same 138/388 versus 140/388 event counts under favor labels. `1/0.98=1.02` and `1/1.24=0.81`, but `1/0.77=1.30`, not the printed 1.29.
- **Category/pagination/duplicate audit:** Permitted measure/label/direction category; pp.5 and 7 are correct; distinct from C024 because it concerns mortality.
- **Assumptions and limitations:** Opposite orientation is compatible with hidden precision but exact reciprocal identity from all already-rounded endpoints is not established. Reference group and unrounded values are missing.
- **Report repair:** Use `near reciprocal` or `compatible with opposite orientation and hidden precision`; frame the unresolved issue around the absent reference definition and favor-axis alignment. Do not repeat the stale exact-reciprocal claim from earlier provisional outputs.

## C024 — Figure 3B IMV HR has a near-reciprocal orientation relative to Table 2

- **Status:** Pending Human Adjudication.
- **Evidence audit:** DOC-001 pp.5-6 print cause-specific HR `0.85 (0.68-1.06)` and p.7 prints `1.17 (0.94-1.46)` for the same 150/388 versus 170/388 counts. `1/1.06=0.94`, while `1/0.85=1.18` and `1/0.68=1.47`, not 1.17 and 1.46.
- **Category/pagination/duplicate audit:** Permitted measure/label/direction category; pp.5-7 are correct; distinct from C023 because it concerns IMV and a cause-specific HR.
- **Assumptions and limitations:** Hidden precision can support an opposite orientation, but the exact reciprocal cannot be derived from all rounded inputs. The figure-specific reference group and estimand definition are missing.
- **Report repair:** Retain the pass-2/recheck precision limitation and focus the card on reference definition and favor-label alignment.

## C025 — Revised-superiority sample-size total conflicts with equal arm counts

- **Status:** Pending Human Adjudication.
- **Evidence audit:** DOC-001 p.3 prints `779 patients (389 in each group)`; `389+389=778`. DOC-002 p.103 prints `778 patients (389 in each group)` under the same revised-superiority assumptions. The published-protocol abstract's matching sentence begins on p.90 and completes with `778 patients overall` on p.91.
- **Category/pagination/duplicate audit:** Permitted numeric/arithmetic category; DOC-001 p.3 and DOC-002 p.103 are exact. A report relying on the abstract comparator must cite p.91 rather than p.90 alone. Cross-source and statistical observations are genuine duplicates already merged.
- **Assumptions and limitations:** Version history or an unequal allocation is not supplied; do not infer the intended number.
- **Report repair:** Include DOC-002 p.91 or use the complete p.103 comparator, and ask whether 778 or 779 was intended.

## C026 — Noninferiority bound/sign wording conflicts with its explanatory axis

- **Status:** Pending Human Adjudication.
- **Evidence audit:** DOC-002 p.40 labels a new-treatment-minus-active-control efficacy axis with the margin on the negative side; p.42 says noninferiority occurs if the lower 95% CI boundary is `less than 9%`. The positive value/inequality is not mapped to the plotted scale.
- **Category/pagination/duplicate audit:** Permitted statistical-reporting category; pp.40 and 42 are correct; no duplicate stable ID.
- **Assumptions and limitations:** The signed estimand, whether efficacy or mortality risk, and the prespecified inequality are missing. Minus-sign omission, reverse scale, or translation are alternatives only.
- **Report repair:** Do not state a corrected inequality; ask for the exact signed effect measure and rule.

## C027 — Primary-hypothesis intervention is labelled NIV while plans identify HFNO

- **Status:** Pending Human Adjudication.
- **Evidence audit:** DOC-002 p.52 and p.104 use `NIV` in the primary-hypothesis sentence while adjacent text and the supplied plans identify HFNO as the experimental intervention. The label comparison reproduces.
- **Category/pagination/duplicate audit:** Permitted measure/label category; both pages are correct; the repeated initial/published occurrences are the same carried-forward wording relationship and are appropriately one stable ID.
- **Assumptions and limitations:** No passage equates NIV with HFNO in the primary hypothesis. Template carryover is possible but not established.
- **Report repair:** Ask whether NIV intentionally denotes HFNO; do not prescribe a replacement.

## C028 — Planned primary outcome alternates between day-28 vital status and hospital death

- **Status:** Pending Human Adjudication.
- **Evidence audit:** DOC-002 pp.54, 82, and 104 each classify patients alive/dead at day 28 and then specify a relative risk of `hospital death`. The within-passage label switch reproduces three times.
- **Category/pagination/duplicate audit:** Permitted measure/label category; all pages are correct; repeated occurrences represent the same relationship and are appropriately one stable ID.
- **Assumptions and limitations:** Hospital-death definition, discharge handling, post-discharge deaths, and equivalence to day-28 mortality are absent. Shorthand is possible but unsupported as a resolution.
- **Report repair:** Ask for the exact estimand/time horizon; do not claim that event counts or conclusions changed.

## Final report-readiness conclusion

The fresh evidence chain is complete through quality audit: 144/144 source units, 54/54 numeric relationships, 38/38 relationships in each statistical pass, and 28/28 stable candidates in ledger, recheck, and audit. Candidate arithmetic/logical comparisons and all ledger/recheck links are reproducible. Before report completion, the coordinator must repair the 80 mapping-artifact relative links described above. The only substantive candidate-content repairs required for report generation are the C018 contextual phrase, the C023-C024 reciprocal-precision limitation, and complete C025 pagination when the protocol abstract is cited. All other card work is required formatting, bounded relevance wording, blank human-adjudication placeholders, report/manifest completion, token accounting, final hashes, rendering, and mechanical validation. No scientific limitation identified here authorizes deletion, merging, ranking, suppression, or disposition of any stable ID.
