# Final Evidence-Quality Audit

## Audit outcome

- **Coverage status:** Scientific coverage is complete. All 5 direct sources and all 88 PDF-page units are mapped: 12 reusable-backed units plus 76 fresh-required units equal 88 total units, and every direct-source row has mapped units equal to total units with `COMPLETE` status.
- **Relationship status:** All 62 stable numeric/reporting relationships, `N001` through `N062`, have numeric-check rows. All 23 stable inferential/statistical relationships, `S001` through `S023`, have distinct `PASS_1_COMPLETE` and `PASS_2_COMPLETE` rows.
- **Candidate status:** The ledger and evidence recheck contain the identical stable set `C001`, `C002`, `C003`, `C004`, and `C005`. This audit returns the same five IDs without deletion, merger, ranking, suppression, severity, or scientific disposition.
- **Discovery boundary:** The current artifacts expressly rebuild discovery from source-linked evidence maps and direct-source gap coverage. No top-N boundary, desired count, old candidate list, review queue, or early stop controlled the mapped source or relationship scope.
- **Statistical executions:** Statistical pass 1 used fresh runtime ID `/root/statistical_pass_1`; statistical pass 2 used different fresh runtime ID `/root/statistical_pass_2`. Both manifest rows record `gpt-5.6-terra`, `high`, `FRESH_SPAWN`, and one primary artifact path.
- **Integrity:** All 5 direct-source hashes and all 90 reused-artifact hashes reproduce their recorded baselines. No changed or missing hashed input was found.
- **Evidence locations and links:** Every recheck PDF link resolves inside the package and ends in a valid `#page=N` fragment. The cited pages are within the direct PDFs' page counts. Direct inspection supports DOC-004 PDF pp. 6-7 for C001-C004 and DOC-003 PDF pp. 6 and 8 plus DOC-001 PDF pp. 1 and 5 for C005. No false pagination was found.
- **Coverage-manifest paths:** Each of the 16 data rows contains one plain relative artifact path. Fourteen rows are currently `COMPLETE`; `evidence_quality` and `report_generation` remain `PENDING` pending coordinator updates and report assembly.
- **Report readiness:** The evidence base is sufficient for report generation after the coordinator applies the bounded repairs below. No scientific remapping, candidate deletion, or statistical rerun is indicated by this audit.

## Coordinator repairs required before report generation is complete

1. In `coverage_manifest.md`, replace the non-enumerated `evidence_quality` scope with explicit `C001, C002, C003, C004, C005`, and mark that row `COMPLETE` after this artifact is accepted. Replace the non-enumerated `report_generation` scope with the same explicit IDs before that stage is completed.
2. For C004, do not repeat the ledger's normalized shorthand `Cutoff [µg]` as an exact quotation. The direct rendering visibly shows `Cutoff` and the incomplete second-line string `[µg`; the closing bracket and `Hb/g` are not visibly rendered. The recheck already records this more exact observation. The final card should use that direct transcription and describe `Cutoff [µg Hb/g]` only as the matched comparator/intended complete form under human review.
3. Keep the C001-C003 calculated differences explicitly diagnostic. The package does not supply the exact unrounded analysis output or table-production convention. The final cards must not prescribe the calculated values as established corrections, even though the count-based calculations reproduce the detached PDF text magnitudes.
4. Distinguish the overlapping support-stage artifact roles in `coverage_manifest.md`: `support-001` is the canonical support relationship map, while `support-002` through `support-005` are fresh layout locator extractions, not additional scientific mapping assignments. This wording repair removes any implication that the same pages were assigned twice for scientific discovery.
5. Update the stale `run_state.md` current-stage sentence, which still says statistical pass 2 is in progress. After the report generator is spawned, add it exactly once to `agent_execution_manifest.md` and later to the token ledger as required by the accounting window.
6. Final report links must be relative to `.ai_paper_validation/`, not copied unchanged from the deeper recheck directory. Use `../joi190039supp3_prod.pdf#page=6`, `../joi190039supp3_prod.pdf#page=7`, `../joi190039supp2_prod.pdf#page=6`, `../joi190039supp2_prod.pdf#page=8`, `../jama_brenner_2019_oi_190039.pdf#page=1`, and `../jama_brenner_2019_oi_190039.pdf#page=5` as applicable.

## Candidate-card readiness rule

The ledger is not itself in final-card schema. For every candidate below, the report generator must render all exact report-spec labels. Fields not explicitly labelled in the ledger are: `Candidate statement`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Alternative source-grounded interpretations` in the required plural form, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields`. C004 and C005 also need `Source evidence` separated from the combined evidence-and-rule prose. The substantive source record is sufficient to populate these fields subject to the candidate-specific limitations below.

## C001 — Women’s quantitative 10.2 µg Hb/g PPV difference point estimate is absent

**Status:** Pending Human Adjudication.

- **Category audit:** `Numeric or arithmetic inconsistency` is an exact permitted category and fits the observable missing numeric content in a named difference column.
- **Evidence and pagination audit:** DOC-004 PDF p. 7 visibly contains aspirin PPV 15.9%, placebo PPV 34.1%, a lone hyphen in the PPV-difference point-estimate position, and 95% CI -34.7 to -1.3. DOC-004 PDF p. 6 contains the matched TP/FP counts 11/58 and 14/27. Population, test, cutoff, treatment order, day, and per-protocol set match. The cited pages and links are accurate.
- **Arithmetic audit:** `11 / (11 + 58) = 0.15942028986`; `14 / (14 + 27) = 0.34146341463`; their aspirin-minus-placebo difference is `-18.204312478` percentage points and rounds to `-18.2`. The displayed-PPV subtraction `15.9 - 34.1` also gives `-18.2`. No arithmetic defect was found.
- **Assumption audit:** The visible omission is directly supported. The intended point estimate, exact unrounded analysis output, and cause of the detached `18.2` text object are not established. Any clipping, displacement, or undocumented-dash explanation must remain conditional.
- **Duplicate audit:** C001 is not a duplicate of C002 or C003 because it concerns a different cutoff/test row and different printed values. It is distinct from C004's header-unit relationship.
- **Conclusion and downstream boundary:** The source supports a table-cell completeness observation, not a claim about the paper's primary conclusion. If human review confirms the issue, a data extractor, systematic review, or meta-analysis could copy an incomplete PPV comparison or reconstruct it inconsistently; propagation or conclusion change is not established.
- **Missing final-card content:** Add all common missing labels listed above. State the exact absent-versus-calculated comparison, reproduce the calculation, incorporate the recheck facts, give page-opening verification steps, and keep the downstream statement conditional and bounded.
- **Display-zero P-value rule:** This candidate has no display-zero P-value content or basis; no conditional independent-contradiction field is required.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Women’s quantitative 17.0 µg Hb/g PPV difference point estimate is absent

**Status:** Pending Human Adjudication.

- **Category audit:** `Numeric or arithmetic inconsistency` is an exact permitted category and fits the missing numeric point-estimate display.
- **Evidence and pagination audit:** DOC-004 PDF p. 7 visibly contains aspirin PPV 17.1%, placebo PPV 42.9%, a lone hyphen in the PPV-difference position, and 95% CI -48.4 to -0.7. DOC-004 PDF p. 6 contains matched TP/FP counts 6/29 and 9/12. The identity fields and cited pages match.
- **Arithmetic audit:** `6 / 35 = 0.17142857143`; `9 / 21 = 0.42857142857`; the count-derived aspirin-minus-placebo difference is `-25.714285714` percentage points and rounds to `-25.7`. Subtracting displayed rounded PPVs gives `17.1 - 42.9 = -25.8`; the 0.1-point difference is an expected rounding-path difference. No arithmetic defect was found.
- **Assumption audit:** The visible omission is supported, but the exact intended estimate and rounding source are not supplied. The detached `25.7` text object supports a production explanation only conditionally and is not authority to prescribe a correction.
- **Duplicate audit:** C002 is a separate 17.0 quantitative row, not the same printed value/comparator/rule instance as C001 or C003. It is not duplicative of the C004 header issue.
- **Conclusion and downstream boundary:** This is a tabular PPV-extraction issue. If confirmed, a downstream extractor could record a missing value or choose different reconstructed rounding; the package does not establish propagation or any effect on the paper's primary conclusion.
- **Missing final-card content:** Add all common missing labels, distinguish `-25.7` count-derived from `-25.8` displayed-value subtraction, name the absent exact unrounded output, and provide bounded verification and downstream wording.
- **Display-zero P-value rule:** This candidate does not mention or depend on a display-zero P value; no conditional independent-contradiction field is required.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Women’s qualitative 10.2 µg Hb/g PPV difference point estimate is absent

**Status:** Pending Human Adjudication.

- **Category audit:** `Numeric or arithmetic inconsistency` is an exact permitted category and fits the incomplete comparative-result cell.
- **Evidence and pagination audit:** DOC-004 PDF p. 7 visibly contains aspirin PPV 9.7%, placebo PPV 31.2%, a lone hyphen in the PPV-difference position, and 95% CI -38.9 to -3.9. DOC-004 PDF p. 6 contains matched TP/FP counts 6/56 and 10/22. The population, qualitative test, cutoff, analysis set, and page citations match.
- **Arithmetic audit:** `6 / 62 = 0.09677419355`; `10 / 32 = 0.3125`; the count-derived difference is `-21.572580645` percentage points and rounds to `-21.6`. Subtraction of displayed PPVs gives `9.7 - 31.2 = -21.5`, a rounding-path difference. No arithmetic defect was found.
- **Assumption audit:** The missing visible magnitude is supported. The exact analysis output, rounding basis, and cause of the detached `21.6` object are not supplied; production-loss language must remain an alternative rather than a conclusion.
- **Duplicate audit:** C003 is the qualitative-test row and has its own values and comparator. It is distinct from both quantitative-row candidates and from C004's common header issue.
- **Conclusion and downstream boundary:** If confirmed, an extractor could copy an incomplete qualitative-test PPV difference or reconstruct it using a different rounding path. No conclusion impact or actual downstream propagation is shown.
- **Missing final-card content:** Add all common missing labels, present both diagnostic rounding paths, preserve the missing-input limitation, and state verification and potential reuse implications conditionally.
- **Display-zero P-value rule:** This candidate has no display-zero P-value basis and needs no independent-contradiction field.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — eTable 5 cutoff header omits the Hb/g concentration denominator

**Status:** Pending Human Adjudication.

- **Category audit:** `Measure, label, or scale inconsistency` is an exact permitted category and fits the matched cutoff-unit display.
- **Evidence and pagination audit:** DOC-004 PDF p. 7 visibly renders `Cutoff` and `[µg` but not `Hb/g]`; DOC-004 PDF p. 6 and DOC-001 PDF p. 5 visibly render the matched cutoff unit as `µg Hb/g`. The same 10.2 and 17.0 cutoffs, tests, day, and per-protocol context align across eTables 4 and 5. Pagination and links are accurate.
- **Calculation audit:** No arithmetic is applicable. The reproducible rule is dimensional label identity: `µg` alone is a mass unit, while `µg Hb/g` is a mass-per-mass cutoff scale. Outcome-column changes do not change the FIT cutoff scale.
- **Assumption and transcription audit:** The ledger's `Cutoff [µg]` shorthand adds a closing bracket that is not visibly rendered and must not be presented as an exact quotation. The detached `Hb/g]` PDF text object makes clipping or displacement plausible but does not establish the production mechanism or intended approved header. An inheritance convention is not printed.
- **Duplicate audit:** C004 concerns one shared eTable 5 header, not the three row-specific missing PPV point estimates. It is also distinct from C005, which concerns a different SAP sentence and a missing numerator prefix in one repeated cutoff expression.
- **Conclusion and downstream boundary:** If confirmed, an extractor could record the cutoff as a mass-only quantity or omit its denominator when transcribing PPV/NPV results. The package does not show that a different analytical scale was used or that a scientific conclusion changes.
- **Missing final-card content:** In addition to the common missing labels, separate `Source evidence` from `Reasoning procedure`, set `Calculation` to a reproducible label comparison with no arithmetic, quote the visible incomplete header exactly, and keep the production explanation conditional.
- **Display-zero P-value rule:** This candidate does not mention or rely on any P value.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — One SAP occurrence omits the microgram prefix from the 10.2 cutoff

**Status:** Pending Human Adjudication.

- **Category audit:** `Measure, label, or scale inconsistency` is an exact permitted category and fits the repeated cutoff-unit expression.
- **Evidence and pagination audit:** DOC-003 PDF p. 6 visibly prints `17 μg Hb/g feces and 10.2 Hb/g feces`; DOC-003 PDF p. 8 prints `10.2 μg Hb/g feces`. DOC-001 PDF pp. 1 and 5 give the matching 10.2 and 17 cutoff context and complete table unit. The cited locations, pages, and links are accurate.
- **Calculation audit:** No arithmetic is applicable. The reproducible comparison matches the same lower FOBGold cutoff across source occurrences and checks whether its numerator unit remains `μg`.
- **Assumption audit:** It is not established whether the first `μg` was intended grammatically to govern both coordinated thresholds. The final card must not assert that the analyzed scale changed or prescribe wording; it must preserve the explicit inheritance question.
- **Duplicate audit:** C005 concerns a SAP sentence on a different source page and a different printed unit construction from C004's incomplete eTable header. Similar unit subject matter does not make the relationships duplicates.
- **Conclusion and downstream boundary:** If confirmed, a data extractor could copy the lower cutoff without its microgram prefix or interpret the repeated unit inconsistently. The supplied evidence does not establish a changed analysis value, result, or paper-level conclusion.
- **Missing final-card content:** Add all common missing labels, split source observation from the unit-identity rule, state that no arithmetic is needed, provide direct page-comparison steps, and retain the grammatical-inheritance alternative.
- **Display-zero P-value rule:** This candidate has no P-value display-zero content or basis.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Limitations and handoff

- Exact unrounded PPV-difference analysis output, table-production source files, and an explicit unit-inheritance convention are not supplied. These limitations define the remaining human questions; they do not create a scientific-coverage gap.
- Final Markdown/HTML reports, report-generator execution, token-usage accounting, finalized timing fields, after-run hash reporting, and validator output are downstream stages and were not yet available for this evidence-quality audit.
- The final report must return C001-C005 in ledger order, use all required card labels, keep all five human-adjudication subfields exactly `__`, and preserve neutral quality-control wording.
