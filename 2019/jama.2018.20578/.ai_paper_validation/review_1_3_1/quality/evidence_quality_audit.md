# Evidence Quality Audit

## Audit scope and completion

- Role: `qc13_quality_control_auditor`.
- Audited inputs: all current source and reused-evidence inventories, source coverage, coverage
  manifest, main and support extraction maps, `N001`-`N076`, `S001`-`S053`, all checker outputs,
  both statistical passes, the candidate ledger, and the mechanical evidence recheck.
- Stable candidate scope audited: `C001`, `C002`, `C003`, `C004`, `C005`, `C006`, `C007`, `C008`,
  `C009`, `C010`, `C011`, `C012`, `C013`, `C014`, `C015`, `C016`, `C017`, `C018`, `C019`,
  `C020`, `C021`, `C022`, `C023`, and `C024`.
- Candidate conservation: the ledger and recheck each contain all 24 IDs exactly once as level-2
  records. The checker-proposal merge history accounts for the complete proposal union. No stable ID
  is deleted, merged, renumbered, ranked, or suppressed by this audit.
- Source integrity at audit time: all 3 direct-source hashes and all 47 reused-artifact hashes match
  their recorded before-review values.
- Discovery coverage: all 76 numeric/reporting relationship vectors were checked; all 53 statistical
  relationships have explicit `PASS_1_COMPLETE` and `PASS_2_COMPLETE` records; all 30 registered
  cross-source match groups were examined. The records state and demonstrate continued review after
  findings, with no top-N, review-queue, or count-target boundary.
- Candidate status: every candidate remains **Pending Human Adjudication**. Audit language below is
  evidence-quality guidance and workflow repair guidance, not a scientific disposition.

## Coverage-manifest row audit

| Stage | Manifest scope audited | Coverage audit | Coordinator action |
|---|---|---|---|
| `source_inventory` | DOC-001 pp. 1-10; DOC-002 pp. 1-7; DOC-003 pp. 1-29 | Complete: 3 PDFs and 46/46 pages are registered; no Office or CSV source exists. | No scope repair. Preserve the two-DOI identity limitation in the final report. |
| `evidence_assets` | A001-A047 | Complete for reused assets: 47/47 are inventoried, fitness-labelled, and hash-stable. The inventory now separately records commands, versions, scopes, and outputs for run-local DOC-003 renders/OCR without adding them to the reused-before hash set. | No remaining support-render provenance repair. |
| `main_evidence_mapping` | DOC-001 pp. 1-10 and 73 provisional relationship keys | Complete: all pages, Tables 1-5, Figures 1-2, captions, footnotes, and result-relevant narrative are documented. | Record the exact command/tool version for the temporary direct p. 8 render if reproducibility metadata is intended to cover temporary confirmation work. |
| `support_evidence_mapping` | DOC-002 pp. 1-7; DOC-003 pp. 1-29 | Complete: protocol, eMethods, eTables 1-6, eFigures 1-4, and reference-only pages are explicitly accounted for. | No remaining scope or provenance repair. |
| `numeric_checks` | `N001`-`N076`, individually enumerated in the manifest | Complete: every relationship has a `COMPLETE` row and applicable arithmetic, denominator, label, duplicate, and forest checks. | No scope repair. Preserve unavailable raw/person-time/model inputs as limitations. |
| `statistics_pass_1` | `S001`-`S053`, individually enumerated | Complete: 53/53 have `PASS_1_COMPLETE`; all registered inferential vectors are covered. | No scope repair. |
| `cross_source_checks` | 30 match groups | Complete: 11 DOC-001 internal groups, 18 DOC-002/DOC-003 groups, and the package identity boundary are documented. | State prominently that DOC-001 is not the main article for DOC-002/DOC-003, so no clinical-result match across those identities is possible. |
| `candidate_registration` | `C001`-`C024`, individually enumerated | Complete: the stable ledger contains all 24 IDs and all checker provenance. | No ID-set repair. Apply category and wording repairs identified below without deleting an ID. |
| `evidence_recheck` | `C001`-`C024`, individually enumerated | Complete: all 24 locations and calculations are separately recorded, and all nested source links now resolve after the coordinator added the required `../`. | No remaining recheck-link repair. |
| `statistics_pass_2` | `S001`-`S053`, individually enumerated | Complete: 53/53 have `PASS_2_COMPLETE`; all 24 candidates were reconsidered; no new pass-2 proposal was emitted. | No scope repair. |
| `evidence_quality` | Placeholder text; manifest status `ASSIGNED` | This canonical audit now covers every coverage row and all 24 stable IDs. | Replace the placeholder with the explicit `C001`, `C002`, `C003`, `C004`, `C005`, `C006`, `C007`, `C008`, `C009`, `C010`, `C011`, `C012`, `C013`, `C014`, `C015`, `C016`, `C017`, `C018`, `C019`, `C020`, `C021`, `C022`, `C023`, `C024` scope and mark the row `COMPLETE`. |
| `report_generation` | Placeholder text; manifest status `ASSIGNED` | Not complete at audit time, as expected before report generation. | After generating both reports, enumerate all 24 IDs explicitly in this row and mark it `COMPLETE`; an ID range is not sufficient. |

The manifest says it was created before scientific extraction. Because the same file was updated after
later stages, its current modification time cannot independently establish its initial creation time;
the durable stage ordering statement is therefore accepted only as workflow provenance, not as a
scientific input.

## Cross-cutting repairs and report safeguards

1. The systematic source-link defect found in `verification/evidence_recheck.md` was repaired during
   this audit. All targets now use `../../../*.pdf#page=N`, and the three unique source targets resolve.
   Ledger source links also resolve.
2. Update the `evidence_quality` and, after report creation, `report_generation` manifest rows with all
   24 IDs explicitly enumerated and the appropriate completion status.
3. Reclassify C020 from `Cross-document numeric inconsistency` to `Numeric or arithmetic
   inconsistency`. Its two numeric comparators are eTable 4 and eFigure 4 within DOC-003; DOC-002
   supplies context but not the conflicting event totals.
4. Reconsider the primary category for C005 and C006. The source labels the cells as participant
   counts, and `3.0` and `2.0` are numerically integer-valued. `Rate-versus-count inconsistency`
   overstates the direct observation because no rate is printed. If the IDs are retained as required,
   `Measure, label, or scale inconsistency` better fits a representation-only formatting question.
   Final cards must not imply that `3.0` is arithmetically different from 3.
5. Exact commands, tool versions, page scopes, and output paths for run-local DOC-003 pp. 7-26 renders
   and pp. 22-26 targeted CPU OCR were added to `evidence_asset_inventory.md` during the audit. The
   main mapper's temporary 300-dpi DOC-001 p. 8 confirmation render is described in its extraction
   artifact but still lacks its exact command/tool-version record; add that provenance if temporary
   confirmation work is included in the run's reproducibility metadata.
6. Keep C014 conditional on the unstated NNH integer-rounding convention and estimand identity. The
   displayed pair is incompatible under ordinary nearest rounding and the usual common-estimand
   reciprocal reading, but `NNH 210` does not mathematically prove an exact unrounded ARD of
   `100/210` when the source omits its integer-display rule.
7. Preserve the visual-only limitation for C018: the graph has no numeric segment labels. The 9/4
   reading is reproducible from alignment and the 0%-100% axis, but exact plotted coordinates are not
   supplied.
8. Preserve C010 as an exact-duplicate quality-control signal, not proof that either row is wrong. A
   genuine coincidence remains source-grounded.
9. The final report must state that DOC-001 has DOI `10.1001/jama.2019.10517`, while DOC-002 and
   DOC-003 belong to DOI `10.1001/jama.2018.20578`. The package lacks the matching main article for
   the latter and lacks the supplement for the former, limiting package-level cross-document review.

## C001 — HbA1c narrative and table units

- **Presence and source audit:** Present in the ledger and recheck. Direct inspection confirms
  `-0.0002 mg/dL` on [DOC-001 p. 1](../../../jama_flint_2019_oi_190079.pdf#page=1) and
  [p. 7](../../../jama_flint_2019_oi_190079.pdf#page=7), while Table 4 prints `HbA1c, %` on
  [p. 8](../../../jama_flint_2019_oi_190079.pdf#page=8).
- **Calculation and category audit:** The unit identity rule is applicable and the `Measure, label, or
  scale inconsistency` category fits. No conversion between concentration and percent is supplied.
- **Assumption, wording, and downstream audit:** The ledger correctly separates the printed labels
  from the inferred adjacent-row copy mechanism and bounds risk to unit-bearing evidence extraction.
- **Repair guidance:** No candidate-specific content repair beyond the global recheck-link correction.
  The report should retain the missing coefficient-scale definition and the exact human question.
- **Status:** Pending Human Adjudication.

## C002 — UKU score range and operational rule

- **Presence and source audit:** Present in both ID sets. [DOC-001 p. 4](../../../jama_flint_2019_oi_190079.pdf#page=4)
  directly prints a 0-3 item range and a `3 or 4` operational condition.
- **Calculation and category audit:** `4 > 3` reproduces exactly; the current measure/scale category
  fits. A special code or alternate instrument version is not supplied.
- **Assumption, wording, and downstream audit:** The record appropriately treats recoding or
  transcription as alternatives and limits relevance to literal rule implementation.
- **Repair guidance:** No candidate-specific repair; retain the coding-definition limitation.
- **Status:** Pending Human Adjudication.

## C003 — Placebo living-arrangement total

- **Presence and source audit:** Present in both ID sets. [DOC-001 p. 5](../../../jama_flint_2019_oi_190079.pdf#page=5)
  prints the `n=62` header and counts 49, 10, and 1 with no row-specific denominator.
- **Calculation and category audit:** `49+10+1=60` and `79.0+16.1+1.6=96.7%`; the denominator/total
  category fits. The gap exceeds ordinary one-decimal rounding accumulation.
- **Assumption, wording, and downstream audit:** The record correctly says the categories appear
  exhaustive and treats two missing observations as an inference rather than a fact.
- **Repair guidance:** No candidate-specific repair; final wording must preserve the possible
  respondent-denominator alternative.
- **Status:** Pending Human Adjudication.

## C004 — Hyperlipidemia percentages and arm denominators

- **Presence and source audit:** Present in both ID sets. Counts, percentages, and 64/62 arm headers
  are confirmed on [DOC-001 p. 5](../../../jama_flint_2019_oi_190079.pdf#page=5).
- **Calculation and category audit:** Own-arm calculations give 28.1% and 30.6%; opposite-arm
  calculations give the printed 29.0% and 29.7%. The denominator/proportion category fits.
- **Assumption, wording, and downstream audit:** Denominator transposition remains diagnostic only;
  unprinted row denominators are named as an alternative, with the placebo-size constraint retained.
- **Repair guidance:** No candidate-specific repair beyond source-link correction in the recheck.
- **Status:** Pending Human Adjudication.

## C005 — Barnes count representation

- **Presence and source audit:** Present in both ID sets. [DOC-001 p. 6](../../../jama_flint_2019_oi_190079.pdf#page=6)
  prints `3.0 (4.7)` and `2.0 (3.2)` under a `No. (%) of Participants` heading.
- **Calculation and category audit:** The percentages reproduce from counts 3 and 2. Because
  `3.0=3` and `2.0=2`, there is no direct count-versus-rate mismatch and no arithmetic defect.
- **Assumption, wording, and downstream audit:** The ledger properly calls the concern representation
  only, but the current `Rate-versus-count inconsistency` category is not well matched to the source.
- **Repair guidance:** Use a representation-focused `Measure, label, or scale inconsistency` category
  or explain the category choice explicitly; do not say a decimal-valued integer is not a count.
- **Status:** Pending Human Adjudication.

## C006 — AIMS count representation

- **Presence and source audit:** Present in both ID sets. [DOC-001 p. 6](../../../jama_flint_2019_oi_190079.pdf#page=6)
  prints `2.0 (3.1)` and `2.0 (3.2)` under the participant-count heading.
- **Calculation and category audit:** `2/64` and `2/62` reproduce the percentages. Decimal notation
  does not change the integer value, and no rate is mislabeled.
- **Assumption, wording, and downstream audit:** The row is appropriately framed as possible table
  formatting, but the current primary category overstates a rate/count distinction.
- **Repair guidance:** Apply the same representation-focused category and wording repair as C005.
- **Status:** Pending Human Adjudication.

## C007 — Relapse-hospitalization percentage boundary

- **Presence and source audit:** Present in both ID sets. [DOC-001 p. 8](../../../jama_flint_2019_oi_190079.pdf#page=8)
  prints `11 (32.3%) of 34`.
- **Calculation and category audit:** `100*11/34=32.352941...%`, ordinarily 32.4% at one decimal. The
  exact value is only 0.00294 percentage point beyond the upper display boundary for 32.3%.
- **Assumption, wording, and downstream audit:** The denominator/proportion category fits; truncation
  is explicitly retained as an alternative and conclusion impact is not overstated.
- **Repair guidance:** Final reporting must preserve the very small boundary magnitude and avoid
  presenting the issue as more than a display-convention question without further evidence.
- **Status:** Pending Human Adjudication.

## C008 — Total-cholesterol unadjusted difference

- **Presence and source audit:** Present in both ID sets. The complete row is confirmed on
  [DOC-001 p. 9](../../../jama_flint_2019_oi_190079.pdf#page=9).
- **Calculation and category audit:** `100*(9/64-6/62)=4.3850806`, ordinarily 4.4 rather than 4.3;
  the numeric/arithmetic category fits the explicitly unadjusted column.
- **Assumption, wording, and downstream audit:** An unprinted denominator or display rule remains an
  alternative; the downstream statement is bounded to extraction of this row.
- **Repair guidance:** No candidate-specific repair.
- **Status:** Pending Human Adjudication.

## C009 — LDL unadjusted difference

- **Presence and source audit:** Present in both ID sets. The separate LDL row is confirmed on
  [DOC-001 p. 9](../../../jama_flint_2019_oi_190079.pdf#page=9).
- **Calculation and category audit:** The same exact count calculation yields 4.3850806, ordinarily
  4.4; this remains a distinct printed outcome and numeric relationship.
- **Assumption, wording, and downstream audit:** A shared production mechanism with C008 is clearly
  labelled as inference, not a reason to merge the two stable IDs.
- **Repair guidance:** No candidate-specific repair.
- **Status:** Pending Human Adjudication.

## C010 — Exact duplicate incident-high vectors

- **Presence and source audit:** Present in both ID sets. [DOC-001 p. 9](../../../jama_flint_2019_oi_190079.pdf#page=9)
  directly shows different thresholds and identical counts, percentages, difference, and interval.
- **Calculation and category audit:** Field-by-field equality is reproducible. The numeric category is
  usable as a duplicate-value check under the contract, but equality alone is not an error.
- **Assumption, wording, and downstream audit:** The current record correctly avoids a probability
  claim and retains genuine coincidence as a source-grounded alternative.
- **Repair guidance:** Keep the final card explicitly as a candidate transcription-control signal;
  do not call it a duplicated-row error without source-data confirmation.
- **Status:** Pending Human Adjudication.

## C011 — ARD subtraction order and sign

- **Presence and source audit:** Present in both ID sets. The literal subtraction wording is confirmed
  on [DOC-002 p. 6](../../../joi180151supp1_prod.pdf#page=6) and the negative-favors-aspirin rule is
  confirmed there and on [DOC-003 p. 4](../../../joi180151supp2_prod.pdf#page=4).
- **Calculation and category audit:** For `RR<1`, `R0-RR*R0>0`, whereas the stated interpretation
  requires `RR*R0-R0<0`. The measure/direction category fits.
- **Assumption, wording, and downstream audit:** The grammatical-referent alternative is preserved;
  the record does not claim that final ARDs were computed with the prose order.
- **Repair guidance:** No candidate-specific repair.
- **Status:** Pending Human Adjudication.

## C012 — Incident-cancer model-selection rule

- **Presence and source audit:** Present in both ID sets. The rule on
  [DOC-003 p. 4](../../../joi180151supp2_prod.pdf#page=4) and row on
  [p. 5](../../../joi180151supp2_prod.pdf#page=5) are confirmed.
- **Calculation and category audit:** DIC difference `0.87<3`; printed I2 is exactly 25, which does
  not meet the printed strict `>25%` condition. The statistical category fits.
- **Assumption, wording, and downstream audit:** Unrounded I2 and an intended inclusive threshold are
  correctly retained as alternatives; the model choice or outcome direction is not adjudicated.
- **Repair guidance:** No candidate-specific repair.
- **Status:** Pending Human Adjudication.

## C013 — Missing ARD display scale

- **Presence and source audit:** Present in both ID sets. The methods on
  [DOC-002 p. 6](../../../joi180151supp1_prod.pdf#page=6) and
  [DOC-003 p. 4](../../../joi180151supp2_prod.pdf#page=4), and the table on
  [DOC-003 p. 15](../../../joi180151supp2_prod.pdf#page=15), do not state the ARD display unit.
- **Calculation and category audit:** Reciprocal magnitudes distinguish a proportion from percentage
  points by a factor of 100; the measure/scale category fits.
- **Assumption, wording, and downstream audit:** Percentage points are correctly presented as an
  inference from NNT/NNH magnitude, not a supplied label. The downstream scale risk is bounded.
- **Repair guidance:** No candidate-specific repair; the final card must not silently assign the unit.
- **Status:** Pending Human Adjudication.

## C014 — All-patient major-bleeding ARD and NNH

- **Presence and source audit:** Present in both ID sets. The method is confirmed on
  [DOC-003 p. 4](../../../joi180151supp2_prod.pdf#page=4), and the `0.47`/`210` pair is confirmed on
  [DOC-003 p. 15](../../../joi180151supp2_prod.pdf#page=15).
- **Calculation and category audit:** `100/0.47=212.77`. Under nearest two-decimal ARD display and an
  ordinary common-estimand reciprocal convention, the pair does not share a common hidden value.
- **Assumption, wording, and downstream audit:** The source omits the unrounded ARD, NNH integer rule,
  and proof that both fields use the same estimand. Those missing inputs materially constrain the
  strength of the diagnostic.
- **Repair guidance:** Replace any unconditional statement that `NNH 210` *implies exactly*
  `ARD=100/210` with the conditional compatibility test and explicitly retain an unstated integer
  convention or separate estimand as alternatives.
- **Status:** Pending Human Adjudication.

## C015 — High-risk major-bleeding ARD and NNH

- **Presence and source audit:** Present in both ID sets. The `0.64`/`152` pair is confirmed on
  [DOC-003 p. 15](../../../joi180151supp2_prod.pdf#page=15), with the method on
  [p. 4](../../../joi180151supp2_prod.pdf#page=4).
- **Calculation and category audit:** `100/0.64=156.25`; `100/152=0.65789`, outside the 0.64
  nearest-display interval. The numeric category fits.
- **Assumption, wording, and downstream audit:** The missing unrounded estimate, estimand identity,
  and integer rule are named. The larger gap remains under ordinary nearby integer conventions.
- **Repair guidance:** No additional content repair; preserve the conditional same-estimand premise.
- **Status:** Pending Human Adjudication.

## C016 — Diabetes major-bleeding ARD and NNH

- **Presence and source audit:** Present in both ID sets. The `0.80`/`121` pair is confirmed on
  [DOC-003 p. 15](../../../joi180151supp2_prod.pdf#page=15), with the method on
  [p. 4](../../../joi180151supp2_prod.pdf#page=4).
- **Calculation and category audit:** `100/0.80=125`; `100/121=0.82645`, outside the 0.80
  nearest-display interval. The numeric category fits.
- **Assumption, wording, and downstream audit:** A separately modeled NNH or unstated convention is
  preserved; conclusion impact is not claimed.
- **Repair guidance:** No additional content repair; preserve the same-estimand premise.
- **Status:** Pending Human Adjudication.

## C017 — Low/high-risk versus all-participant stroke events

- **Presence and source audit:** Present in both ID sets. All counts and denominators are confirmed on
  [DOC-003 p. 16](../../../joi180151supp2_prod.pdf#page=16).
- **Calculation and category audit:** Denominators partition exactly, while events give 1133 versus
  1116 and 1168 versus 1136. The denominator/total category fits.
- **Assumption, wording, and downstream audit:** Exhaustive event partitioning is conditional on the
  same outcome availability and analysis set; the record explicitly retains an unreported exception.
- **Repair guidance:** No candidate-specific repair; do not imply participant-level subgroup data are
  supplied.
- **Status:** Pending Human Adjudication.

## C018 — Detection-bias table and graph

- **Presence and source audit:** Present in both ID sets. The 13 table classifications are on
  [DOC-003 pp. 10-14](../../../joi180151supp2_prod.pdf#page=10); the rendered graph on
  [p. 20](../../../joi180151supp2_prod.pdf#page=20) visibly aligns detection with the 9/4 bars.
- **Calculation and category audit:** Table proportions are 61.54%/38.46%; the plotted boundary is
  approximately 69.23%/30.77%. The denominator/proportion category fits.
- **Assumption, wording, and downstream audit:** Exact 9/4 assignment from the unlabeled boundary is
  inference, explicitly acknowledged. The table classifications and graph geometry are direct.
- **Repair guidance:** Preserve `approximately` and the absence of numeric plot labels in the report.
- **Status:** Pending Human Adjudication.

## C019 — Egger coefficient, SE, and t

- **Presence and source audit:** Present in both ID sets. The complete vector is confirmed on
  [DOC-003 p. 21](../../../joi180151supp2_prod.pdf#page=21).
- **Calculation and category audit:** `-0.47/0.77=-0.61039`; ordinary two-decimal input intervals give
  magnitude 0.600-0.621, excluding a t displayed as 0.59. The statistical category fits.
- **Assumption, wording, and downstream audit:** The coefficient/SE t identity depends on the exact
  Egger implementation and field meanings, which are not supplied. The alternative is appropriately
  named, and no funnel-plot conclusion is asserted.
- **Repair guidance:** No content repair beyond retaining the implementation limitation.
- **Status:** Pending Human Adjudication.

## C020 — Twelve-study total-stroke event totals

- **Presence and source audit:** Present in both ID sets. eTable 4 on
  [DOC-003 p. 16](../../../joi180151supp2_prod.pdf#page=16) and the forest plot on
  [p. 24](../../../joi180151supp2_prod.pdf#page=24) supply the numeric comparators; the protocol on
  [DOC-002 p. 7](../../../joi180151supp1_prod.pdf#page=7) supplies exclusion context.
- **Calculation and category audit:** Removing ASCEND reproduces denominators but yields forest events
  1118/1134 versus table events 1116/1136. The mismatch is within DOC-003, so the current
  `Cross-document numeric inconsistency` category is not truthful to the comparator locations.
- **Assumption, wording, and downstream audit:** Separate event curation or analysis versions remain
  source-grounded alternatives; the record does not claim a changed pooled conclusion.
- **Repair guidance:** Change the primary category to `Numeric or arithmetic inconsistency` while
  retaining DOC-002 as definition/context provenance.
- **Status:** Pending Human Adjudication.

## C021 — NNT with a displayed null-reaching ARD interval

- **Presence and source audit:** Present in both ID sets. The NNT rule on
  [DOC-003 p. 4](../../../joi180151supp2_prod.pdf#page=4) and `-0.27 (-0.49 to 0.00)` with NNT 366 on
  [p. 15](../../../joi180151supp2_prod.pdf#page=15) are confirmed.
- **Calculation and category audit:** The printed 95% CI includes 0.00 while the display rule is
  significance-conditioned; the statistical category fits at displayed precision.
- **Assumption, wording, and downstream audit:** A slightly negative unrounded endpoint could explain
  both facts and is prominently retained. The record does not assign significance from rounded data.
- **Repair guidance:** No candidate-specific repair; keep the unrounded-endpoint question central.
- **Status:** Pending Human Adjudication.

## C022 — Diabetes total-stroke CI/CrI terminology

- **Presence and source audit:** Present in both ID sets. [DOC-003 p. 16](../../../joi180151supp2_prod.pdf#page=16)
  labels the HR column `95% CrI` and the attached 1.004 footnote `confidence interval`.
- **Calculation and category audit:** The same endpoint receives distinct interval-type labels; the
  measure/label category fits. The 1.004 footnote resolves rounding, not terminology.
- **Assumption, wording, and downstream audit:** Informal use of “confidence” and a header error are
  both retained; no interval framework is assigned by the audit.
- **Repair guidance:** No candidate-specific repair.
- **Status:** Pending Human Adjudication.

## C023 — Sensitivity-analysis CI/CrI terminology

- **Presence and source audit:** Present in both ID sets. [DOC-003 p. 18](../../../joi180151supp2_prod.pdf#page=18)
  labels results `95% CrI` and the attached 0.9989 footnote `confidence interval`.
- **Calculation and category audit:** The terminology comparison is direct and the measure/label
  category fits. The unrounded endpoint resolves the null boundary only.
- **Assumption, wording, and downstream audit:** The record preserves both informal-wording and wrong-
  header alternatives and does not infer the analysis type.
- **Repair guidance:** No candidate-specific repair.
- **Status:** Pending Human Adjudication.

## C024 — ASCEND ischemic-only row in total-stroke forest plot

- **Presence and source audit:** Present in both ID sets. The outcome definition is on
  [DOC-003 p. 9](../../../joi180151supp2_prod.pdf#page=9), the 12-study table on
  [p. 16](../../../joi180151supp2_prod.pdf#page=16), both forest panels on
  [p. 24](../../../joi180151supp2_prod.pdf#page=24), and protocol context on
  [DOC-002 p. 7](../../../joi180151supp1_prod.pdf#page=7).
- **Calculation and category audit:** The identical ASCEND 240/7740 versus 263/7740 row appears in
  both panels, and adding its denominators converts the 12-study totals to the 13-study forest totals.
  The measure/label category fits this outcome-classification question.
- **Assumption, wording, and downstream audit:** An intentionally broader frequentist available-event
  convention remains a source-grounded but unstated alternative. C024 is distinct from C020's
  non-ASCEND arm-count mismatch.
- **Repair guidance:** No candidate-specific category repair; preserve the exact definition exception
  question and bounded downstream outcome-classification risk.
- **Status:** Pending Human Adjudication.

## Audit limitations

- No raw participant data, table-production files, unrounded ARDs, NNT/NNH integer convention,
  unrounded I2, MCMC output, trial-level person-time mapping, or Egger model output is supplied.
- The eFigure 2 segment has no numeric label; C018 necessarily combines exact table counts with a
  reproducible visual-axis comparison.
- Direct-source table and forest values were checked against supplied PDFs, but the audit did not fit
  replacement statistical models or treat diagnostic calculations as the reported analysis.
- The supplied package joins direct sources from two different article identities and does not include
  the corresponding main/supplement pair for either identity; cross-identity scientific comparisons
  were correctly not manufactured.

## Audit completion statement

All 12 required coverage stages and all 24 stable candidate IDs have been audited. The candidate,
recheck, statistical-pass, and quality ID sets are conserved at this stage. Recheck-link and support-
render/OCR provenance repairs were completed during the audit. Remaining coordinator work is limited
to manifest enumeration/status updates, optional exact provenance for the main mapper's temporary
p. 8 render, the C005/C006 category/framing issue, the C020 category, and the C014 reciprocal wording
safeguard. Every stable candidate remains **Pending Human Adjudication**.
