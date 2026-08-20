# Final Evidence-Quality Audit

This audit covers the complete stable ledger, mechanical recheck, fresh source and evidence inventories, every coverage-manifest and source-coverage row, N001-N072, S001-S050, both statistical passes, the cross-source checker, and the agent-execution manifest. It used only the three supplied PDFs and current Workflow 1.5.2 artifacts. It did not use a legacy audit derivative or external material as evidence. Every candidate below remains **Pending Human Adjudication**.

## Audit-wide coverage and integrity

- **Direct sources:** DOC-001 has 8 PDF pages, DOC-002 has 16, and DOC-003 has 4. All three source-coverage rows have reusable units `0`, fresh-required units equal to total units, mapped units equal to total units, and status `COMPLETE` (28 of 28 total units).
- **Source integrity:** Fresh `sha256sum` checks during this audit reproduced all three hashes in `source_hashes_before.sha256`: DOC-001 `ef598eafd5458d572fad896a0decfd921e810989970a9b3cc9e51d779812937f`; DOC-002 `ad3a483ebb6fa19e67c030eb332b9a3df668a6fd8f5715ab09c02bad3008e2df`; DOC-003 `3b7a3ff0ee0fa03b443eb026c592f1da011aeeeea64cd4b19d20396cdd7e60e4`.
- **Fresh evidence boundary:** The inventories document new metadata, native text, layout text, and 14 targeted page renders. Native/layout text was usable for all 28 pages, so zero OCR units were needed. No Office, workbook, CSV, GPU, web, or old-audit evidence entered the chain. This audit found no contrary provenance in the fresh artifacts.
- **Coverage manifest:** All 12 required stage rows are present. Every row contains exactly one undecorated relative POSIX artifact path. Main and support mapping scopes cover DOC-001 pp. 1-8 and DOC-002 pp. 1-16 plus DOC-003 pp. 1-4, respectively. Candidate registration, recheck, quality, and report scopes each explicitly enumerate C001-C010. Both statistical scopes explicitly enumerate S001-S050. At the time of this stage audit, the upstream rows through statistical pass 2 were `COMPLETE`; the `evidence_quality` and `report_generation` rows remained `PENDING` because this artifact and the report had not yet been finalized. The coordinator must change each to `COMPLETE` only after its artifact is complete.
- **Relationship inventories:** N001-N072 are contiguous and each has an explicit numeric-check status. S001-S050 are contiguous; every relationship has `PASS_1_COMPLETE` and `PASS_2_COMPLETE` in the combined inventory and is now named literally in each corresponding pass artifact. The relationship scopes are complete and show no sampling, queue, top-N, or early-stopping boundary.
- **Completed repair:** The initial `checkers/statistical_pass_1.md` grouped 27 no-proposal relationships only under ranges, so their literal S IDs were absent from that artifact. The coordinator added an explicit complete S001-S050 scope. Recheck confirms all 50 exact IDs now occur in pass 1 and pass 2; scientific conclusions and candidate registration did not change.
- **Statistical execution:** The manifest records distinct fresh agents `/root/statistics_pass_1` and `/root/statistics_pass_2`, both `gpt-5.6-terra`, `high`, `FRESH_SPAWN`, with separate primary artifacts. The coordinator and every agent active through this audit appear exactly once. Any later report-generation or repair agent must be appended exactly once before accounting closes.
- **Candidate flow:** The ledger and mechanical recheck each contain C001-C010 once and in the same order; this audit does likewise. The eight numeric proposals, four pass-1 statistical proposals, and one cross-source proposal reconcile to 10 distinct stable candidates after genuine proposal overlap is removed: C001 recurs in all three lanes and C006 recurs in numeric and statistical lanes. The exact count of 10 is therefore provenance-reproducible and is not evidence of a count cap.
- **Display-zero exclusion:** No supplied result displays `P = 0`, `p = 0.000`, or an equivalent. No stable candidate is based on display-zero notation, finite precision, underflow, or nonzero-tail reasoning. The `P=0.03` text associated with C006 is a nonzero decimal and is not a display-zero case.
- **Human-adjudication fields:** The ledger and recheck contain no adjudication subfields, so there is no populated or nonblank human disposition in the audited candidate artifacts. The final report must give every C001-C010 card the five exact blank values `Validity: __`, `Importance: __`, `Action: __`, `Initials: __`, and `Notes: __` under the required bold labels.
- **Neutrality and downstream wording:** Categories use the exact scope vocabulary. No stable entry assigns severity, scientific disposition, correction, ranking, or conclusion change. The ledger makes no downstream-impact claim; the report generator must state only what a later evidence extractor or evidence product could copy if a candidate is human-confirmed, without claiming actual propagation or changed conclusions.

## C001 — Spontaneous-delivery hazard ratio conflicts across narrative and Figure 2B

- **Audit outcome:** Evidence-sufficient quality-control candidate; **Pending Human Adjudication**.
- **Category and locations:** `Cross-document numeric inconsistency` is appropriate for the matched narrative/figure mismatch. The supplied [DOC-001 p. 5 narrative](../../../jama_saccone_2017_oi_170144.pdf#page=5) prints HR `0.36` with 95% CI `0.54-0.87`; [DOC-001 p. 6, Figure 2B](../../../jama_saccone_2017_oi_170144.pdf#page=6), labeled “Spontaneous delivery only,” prints HR `0.68` with the identical CI `0.54-0.87`. Page identities and printed values were directly rechecked.
- **Comparator, rule, and calculation:** Both occurrences identify the spontaneous-delivery Cox/Kaplan-Meier context and share the same CI. A matched result should reproduce its point estimate, and an HR must lie within its ordered interval. `0.36 != 0.68`; `0.36 < 0.54`; `0.54 <= 0.68 <= 0.87`.
- **Direct versus inferred:** The two HRs, common interval, labels, and containment failure are direct. A transcription error, model swap, or unreported specification difference is only an inferred production explanation. Figure 2A's any-delivery HR `0.70 (0.55-0.88)` is a source-grounded alternative analysis but does not reconcile the two spontaneous-delivery occurrences.
- **Completeness and duplication audit:** The ledger and recheck provide the required evidence, comparator, calculation, missing inputs, alternative interpretation, and exact human question. The cross-location identity and the narrative HR/CI containment observations are coupled around the same printed narrative result and were consistently registered as one candidate across all proposal lanes; no second stable ID duplicates C001. No replacement HR or CI is asserted.
- **Human question and reporting boundary:** The remaining question correctly asks which HR/CI pair belongs to the intended spontaneous-delivery analysis through 34 weeks. A final card must add the required verification, bounded downstream-copying statement, and five exact `__` adjudication placeholders; it must not claim that either value is the correction.

## C002 — SPTB under 32 weeks difference does not round from printed counts

- **Audit outcome:** Evidence-sufficient quality-control candidate; **Pending Human Adjudication**.
- **Category and location:** `Numeric or arithmetic inconsistency` is appropriate. [DOC-001 p. 5, Table 2](../../../jama_saccone_2017_oi_170144.pdf#page=5) prints pessary `10/150 (6.7%)`, control `14/150 (9.3%)`, and difference `-2.6%`. The page, row, arm headers, values, and comparator were directly rechecked.
- **Comparator, rule, and calculation:** From the exact printed fractions, `100*(10/150 - 14/150) = -2.666666...`, which rounds to `-2.7%` at one decimal; the printed `-2.6%` instead equals `6.7 - 9.3`. The discrepancy exceeds the half-unit rounding tolerance by about `0.0167` percentage points.
- **Direct versus inferred:** The row values are direct. It is inferred, not established, that displayed rounded percentages were used as computational inputs. That source-grounded convention exactly reproduces `-2.6%` and is therefore a material alternative, while production code and any alternative denominator are absent.
- **Completeness and duplication audit:** The ledger/recheck include the necessary fields and do not overstate the arithmetic diagnostic. No other stable ID uses this row and exact-fraction rounding rule. The human question appropriately asks which convention generated the point estimate.
- **Reporting boundary:** A final card must describe only the potential copying of the absolute difference if human-confirmed, include all required card fields and five exact `__` placeholders, and avoid prescribing `-2.7%` as a correction.

## C003 — Operative-vaginal-delivery difference does not round from printed counts

- **Audit outcome:** Evidence-sufficient quality-control candidate; **Pending Human Adjudication**.
- **Category and location:** `Numeric or arithmetic inconsistency` is appropriate. [DOC-001 p. 5, Table 2](../../../jama_saccone_2017_oi_170144.pdf#page=5) prints pessary `5/150 (3.3%)`, control `10/150 (6.7%)`, and difference `-3.4%`.
- **Comparator, rule, and calculation:** `100*(5/150 - 10/150) = -3.333333...`, which rounds to `-3.3%`; subtraction of displayed percentages gives `3.3 - 6.7 = -3.4%`.
- **Direct versus inferred:** Counts, denominators, percentages, and difference are direct. Rounded-display subtraction is a source-grounded alternative that reproduces the print; the actual production convention is missing and must not be inferred.
- **Completeness and duplication audit:** C003 and C010 concern the same row but are not duplicates: C003 compares the printed difference with exact-fraction rounding, whereas C010 compares that printed point with its interval. The ledger and recheck preserve both comparator/rule paths without asserting a corrected value.
- **Human question and reporting boundary:** The exact human question about the intended denominator/rounding convention is supported. The final card must add bounded reuse relevance and five exact `__` placeholders, without merging C003 into C010 or claiming impact on conclusions.

## C004 — Chorioamnionitis difference does not round from printed counts

- **Audit outcome:** Evidence-sufficient quality-control candidate; **Pending Human Adjudication**.
- **Category and location:** `Numeric or arithmetic inconsistency` is appropriate. [DOC-001 p. 5, Table 2](../../../jama_saccone_2017_oi_170144.pdf#page=5) prints pessary `5/150 (3.3%)`, control `7/150 (4.7%)`, and difference `-1.4%`.
- **Comparator, rule, and calculation:** `100*(5/150 - 7/150) = -1.333333...`, which rounds to `-1.3%`; displayed-percentage subtraction gives `3.3 - 4.7 = -1.4%`.
- **Direct versus inferred:** The printed row is direct. Use of rounded percentages or an unreported denominator/calculation is an unresolved explanation. The first alternative exactly reproduces the display and is correctly retained rather than suppressed.
- **Completeness and duplication audit:** All threshold fields are present in ledger/recheck; no other C ID addresses this exact row and rounding rule. The candidate remains neutral and does not assert which display is correct.
- **Human question and reporting boundary:** The question distinguishing exact-fraction from intended alternative convention is exact and answerable from production records. The final card must use a bounded copying-risk statement and five exact `__` placeholders.

## C005 — Perinatal-death difference does not round from printed counts

- **Audit outcome:** Evidence-sufficient quality-control candidate; **Pending Human Adjudication**.
- **Category and location:** `Numeric or arithmetic inconsistency` is appropriate. [DOC-001 p. 5, Table 2](../../../jama_saccone_2017_oi_170144.pdf#page=5) prints pessary `2/150 (1.3%)`, control `4/150 (2.7%)`, and difference `-1.4%`.
- **Comparator, rule, and calculation:** `100*(2/150 - 4/150) = -1.333333...`, which rounds to `-1.3%`; `1.3 - 2.7 = -1.4%` reproduces the printed display from rounded percentages.
- **Direct versus inferred:** The row and arm sizes are direct; its production convention is not. No source supports replacing the printed value, and the ledger/recheck correctly frame the alternative as unresolved.
- **Completeness and duplication audit:** The evidence, calculation, alternative, and human question are complete for candidate threshold purposes. No duplicate stable relationship was found.
- **Reporting boundary:** The final card must preserve the exact convention question, add bounded evidence-extraction relevance and five exact `__` placeholders, and avoid asserting a correction or conclusion effect.

## C006 — Birth weight under 2500 g difference lies outside its printed CI

- **Audit outcome:** Evidence-sufficient quality-control candidate; **Pending Human Adjudication**.
- **Category and location:** `Statistical reporting inconsistency` is appropriate. [DOC-003 p. 3, eTable 2](../../../joi170144supp2_prod.pdf#page=3) prints pessary `28/150 (18.7%)`, control `45/150 (30.0%)`, difference `-11.3%` with 95% CI `-1.1 to +21.2`, RR `0.62 (0.41-0.94)`, and `P=0.03`. The page and dense-table alignment were directly checked.
- **Comparator, rule, and calculation:** A point must lie within its own same-scale ordered CI. `100*(28/150 - 45/150) = -11.333333...`, consistent with `-11.3%`; however, `-11.3 < -1.1`, so it is outside `[-1.1, 21.2]`.
- **Direct versus inferred:** Non-containment and the negative count/RR direction are direct. A reverse-contrast interval is a source-grounded possible explanation because `+11.3` lies within the printed interval, but the table does not label opposite contrast directions. Endpoint/sign transcription is also possible; neither explanation supplies a replacement CI.
- **Completeness and duplication audit:** Numeric P-N06 and statistical P04 are genuine duplicates of this same point/interval/rule and were correctly registered once. Required ledger/recheck facts are complete. `P=0.03` is not a display zero and is corroborating context only, not the candidate basis.
- **Human question and reporting boundary:** The question asks for the signed CI produced for the pessary-minus-control difference. The final card must include bounded extraction relevance and five exact `__` placeholders, with no reconstructed bootstrap interval or impact claim.

## C007 — Respiratory-distress-syndrome difference does not round from printed counts

- **Audit outcome:** Evidence-sufficient quality-control candidate; **Pending Human Adjudication**.
- **Category and location:** `Numeric or arithmetic inconsistency` is appropriate. [DOC-003 p. 3, eTable 2](../../../joi170144supp2_prod.pdf#page=3) prints pessary `14/150 (9.3%)`, control `31/150 (20.7%)`, and difference `-11.4%`.
- **Comparator, rule, and calculation:** `100*(14/150 - 31/150) = -11.333333...`, which rounds to `-11.3%`; displayed-percentage subtraction yields `9.3 - 20.7 = -11.4%`.
- **Direct versus inferred:** All compared values are direct. Rounded-display subtraction is a reproducible alternative; the production code and explicit convention are absent. The coherent inferential display does not resolve the last-digit arithmetic convention.
- **Completeness and duplication audit:** Ledger and recheck supply all threshold facts and the exact human question. No other stable ID uses this row and arithmetic rule.
- **Reporting boundary:** The final card must retain the conditional wording, add only bounded copying relevance, use five exact `__` placeholders, and not prescribe a replacement value.

## C008 — Cervical-length subgroup difference is on the opposite side of the rounding boundary

- **Audit outcome:** Evidence-sufficient quality-control candidate; **Pending Human Adjudication**.
- **Category and location:** `Numeric or arithmetic inconsistency` is appropriate. [DOC-003 p. 4, eTable 3](../../../joi170144supp2_prod.pdf#page=4) prints TVU CL `<=10 mm`: pessary `3/56 (5.4%)`, control `10/42 (23.8%)`, and difference `-18.4%`.
- **Comparator, rule, and calculation:** `100*(3/56 - 10/42) = -18.452380...`; nearest one-decimal rounding is `-18.5%`. Displayed-percentage subtraction gives `5.4 - 23.8 = -18.4%`. The exact result is about `0.00238` percentage points beyond the `-18.45` midpoint toward `-18.5`.
- **Direct versus inferred:** The fractions and table display are direct. The chosen production/rounding convention is absent. The very small boundary distance is explicitly disclosed, and rounded-display subtraction is a material source-grounded alternative.
- **Completeness and duplication audit:** The candidate is not an unsupported precision complaint: exact integer fractions and denominators are printed. Ledger and recheck include the boundary calculation, limitations, and human question. No duplicate stable rule was found.
- **Reporting boundary:** The final card must make the near-boundary nature prominent, preserve conditional language, add bounded reuse relevance, and use five exact `__` placeholders without asserting a correction.

## C009 — Cesarean-delivery difference lies outside its printed CI

- **Audit outcome:** Evidence-sufficient quality-control candidate; **Pending Human Adjudication**.
- **Category and location:** `Statistical reporting inconsistency` is appropriate. [DOC-001 p. 5, Table 2](../../../jama_saccone_2017_oi_170144.pdf#page=5) prints pessary `45/150 (30.0%)`, control `57/150 (38.0%)`, difference `-8.0%` with 95% CI `-3.2 to 19.0`, RR `0.79 (0.57-1.09)`, and `P=.18`.
- **Comparator, rule, and calculation:** A point must lie in its same-scale ordered interval. `30.0 - 38.0 = -8.0`, while `-8.0 < -3.2`, so the point is outside `[-3.2, 19.0]`.
- **Direct versus inferred:** The point, interval, and count direction are direct. A reverse-contrast CI is a possible source-grounded explanation because `+8.0` is contained, but the common table column does not label mixed directions. A sign/endpoint production error is also possible; no corrected interval is supplied.
- **Completeness and duplication audit:** Statistical P02 maps uniquely to C009. The card facts are complete for candidate threshold purposes, and no duplicate stable relationship was found.
- **Human question and reporting boundary:** The exact remaining question asks which signed bootstrap CI belongs to the pessary-minus-control estimate. The final card must add bounded reuse relevance and five exact `__` placeholders without asserting reverse contrast as fact.

## C010 — Operative-vaginal-delivery difference lies outside its printed CI

- **Audit outcome:** Evidence-sufficient quality-control candidate; **Pending Human Adjudication**.
- **Category and location:** `Statistical reporting inconsistency` is appropriate. [DOC-001 p. 5, Table 2](../../../jama_saccone_2017_oi_170144.pdf#page=5) prints pessary `5/150 (3.3%)`, control `10/150 (6.7%)`, difference `-3.4%` with 95% CI `-2.1 to 9.1`, RR `0.50 (0.18-1.43)`, and `P=.29`.
- **Comparator, rule, and calculation:** `-3.4 < -2.1`, so the printed point is outside `[-2.1, 9.1]`. The displayed percentages independently reproduce the point direction; `+3.4` would lie within the interval.
- **Direct versus inferred:** Non-containment is direct. Reverse-contrast CI generation or endpoint/sign transcription is possible but unsupported as the actual mechanism. No replacement interval is inferred.
- **Completeness and duplication audit:** C010 remains distinct from C003 because it uses point/CI containment rather than exact-fraction rounding. Statistical P03 maps uniquely to C010. Ledger/recheck evidence and the human question are complete.
- **Reporting boundary:** The final card must preserve both stable IDs, add bounded evidence-reuse relevance and five exact `__` placeholders, and avoid assigning a corrected CI, severity, or conclusion impact.

## Final audit conclusion

- **Covered stable IDs:** C001, C002, C003, C004, C005, C006, C007, C008, C009, C010 (10 of 10).
- **Relationship coverage:** N001-N072 (72 of 72), statistical pass 1 S001-S050 (50 of 50), and statistical pass 2 S001-S050 (50 of 50).
- **Coverage rows:** 3 of 3 direct-source rows fully mapped; 12 of 12 required manifest stages present with one artifact path per row. Evidence-quality and report-generation status transitions remain coordinator actions after their artifacts are complete.
- **Stable-ID equality at this stage:** Ledger = recheck = quality audit = `{C001, C002, C003, C004, C005, C006, C007, C008, C009, C010}`. The final report must reproduce the identical ordered set.
- **Supportable omissions or new candidates:** None after the completed explicit-pass-1-ID repair. No stable ID was deleted, merged, renumbered, ranked, suppressed, or adjudicated.
- **Limitations:** Authoritative Cox output is absent for C001; point-difference production/rounding rules are absent for C002-C005, C007, and C008; bootstrap draws and authoritative signed risk-difference CI outputs are absent for C006, C009, and C010. These limitations prevent selection of a correction but do not erase the direct printed comparisons.
- **Result:** Complete evidence-quality coverage with all candidates retained as **Pending Human Adjudication**. Final report assembly, exact blank adjudication fields, later-agent manifest/token accounting, status updates, source-hash recomputation, HTML rendering, and mechanical validation remain downstream coordinator responsibilities.
