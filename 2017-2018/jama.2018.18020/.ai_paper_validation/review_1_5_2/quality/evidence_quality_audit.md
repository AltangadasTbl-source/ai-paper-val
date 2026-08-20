# Final Evidence-Quality and Completeness Audit

## Audit scope and outcome

This source-first audit covered every stable candidate in the current ledger (`C001` through `C014`), every corresponding mechanical recheck section, all four direct-source rows, all twelve coverage-manifest rows, the complete 57-record numeric inventory, both complete 56-record statistical passes, the 113-record cross-source scope, the checker union and duplicate merge, the source/evidence inventories, and all ten agent-execution rows present at the audit cutoff. The supplied PDFs were the evidentiary authority. Fresh native/layout text and current page renders were used as locators and for visual alignment; no old audit derivative or web source was used.

- **Stable candidate coverage:** 14/14 in the ledger and 14/14 in the mechanical recheck, with one section per ID and identical ID sets.
- **Candidate category coverage:** 14/14 use one category authorized by `QUALITY_CONTROL_SCOPE.md`: 2 denominator/proportion/total, 6 measure/label/scale, and 6 statistical-reporting candidates.
- **Numeric relationship coverage:** 57/57 (`N001`-`N035`, `N501`-`N522`).
- **Statistical relationship coverage:** 56/56 (`S001`-`S022`, `S501`-`S534`) in each of pass 1 and pass 2, with an explicit relationship-level completion row in both artifacts.
- **Cross-source coverage:** 113/113 mapped N and S relationships.
- **Checker union:** 21 provisional checker observations were losslessly registered as 14 distinct stable candidates after genuine duplicate consolidation. No assigned stable ID was deleted, merged after registration, ranked, or suppressed.
- **Source coverage:** 4/4 direct-source rows are `COMPLETE`; for every row, reusable units are 0 and fresh-required units and mapped units equal total units. Totals reconcile at 83/83 fresh-required and 83/83 mapped PDF pages.
- **Evidence assets:** Four metadata files, four native-text files, four layout-text files, and 83 page renders are present. Native/layout text was usable, so 0 OCR pages is a documented source-grounded decision.
- **Source integrity:** The four recomputed SHA-256 values match `source_hashes_before.sha256` exactly.
- **Coverage manifest at audit time:** 10/12 rows are `COMPLETE`. The `evidence_quality` and `report_generation` rows remain pre-completion placeholders and require the coordinator repairs listed below.
- **Agent execution at audit time:** 10/10 actual executions represented by one row each, including the coordinator and this quality auditor. Statistical pass 1 (`/root/statistics_pass_1`) and pass 2 (`/root/statistics_pass_2`) have distinct runtime IDs and are each recorded as fresh `gpt-5.6-terra`/`high` spawns with one durable artifact.
- **Discovery boundary:** The mapping/checker artifacts document complete assigned scopes, the ledger identifies itself as the complete uncapped checker union, and no top-N, queue, desired-count, or early-stopping boundary appears in the evidence chain.
- **Display-zero boundary:** No stable candidate mentions or depends on `P = 0`, `p = 0.000`, or an equivalent P-value display zero. S508's `0.00` is an effect estimate and S532's `0.00` is a simulation frequency; pass 2 appropriately records both as not display-zero-P candidates.
- **Neutrality:** Candidate wording is quality-control language, supplies alternative interpretations and exact human questions, and makes no severity, scientific disposition, correction, paper-invalidity, or demonstrated-conclusion-impact claim.

## Checker-union and duplicate-registration audit

The provisional-to-stable mapping is complete and reproducible:

| Stable ID | Provisional provenance merged before stable registration |
|---|---|
| C001 | NUM001; CROSS-001 |
| C002 | NUM002 |
| C003 | NUM003; STAT1-001 |
| C004 | NUM004 |
| C005 | NUM005; CROSS-003; STAT1-006 |
| C006 | NUM006; CROSS-005; STAT1-007 |
| C007 | NUM007; CROSS-004 |
| C008 | CROSS-002 |
| C009 | STAT1-002 |
| C010 | STAT1-003 |
| C011 | STAT1-004 |
| C012 | STAT1-005 |
| C013 | STAT2-001 |
| C014 | STAT2-002 |

The merged records concern the same printed fields, comparator, and rule within each stable ID. The superficially related records that remain separate concern different parameters, cells, or rules: C005-C007 address three distinct Bayesian parameter-label relationships; C009-C012 address four distinct inferential rows; and C013-C014 address two distinct placebo-period estimate/interval cells. C003 concerns the shared treatment-effect column header and does not duplicate either C013 or C014.

## Coordinator repairs confirmed and remaining final-assembly controls

1. In `coverage_manifest.md`, enumerate `C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014` in each of the `evidence_quality` and `report_generation` exact scopes. Set the quality row to `COMPLETE` after this artifact is durable and the report row to `COMPLETE` only after the complete report exists. Retain exactly one plain relative artifact path per row.
2. **Confirmed repaired:** `evidence_asset_inventory.md` now labels extraction lengths as bytes and names the existing DOC-004 render exactly as `preprocessing/rendered_pages/DOC-004-1.png`.
3. **Confirmed repaired:** `extraction/main_quantitative_evidence.md` now places N026-N028 and S016-S020 result rows on DOC-001 PDF p. 7 and separately cites the relevant p. 8 footnotes. `checkers/numeric_consistency.md` now places N031's main-article adverse-events comparator on p. 8.
4. **Confirmed repaired:** `candidate_ledger.md` now uses separate exact page links for C005 and C008, adds DOC-001 p. 4 for the two-sided convention used by C009-C012, and adds p. 8 for the Table 2 footnote text used by C010-C011. The registered result cells remain correctly located: C009-C011 and C013-C014 on p. 7, and C012 on p. 8.
5. **Confirmed repaired:** `verification/evidence_recheck.md` now separates the dependent-t method on p. 3, two-sided convention on p. 4, and relevant p. 8 footnotes. Every current candidate/recheck PDF link ends in one truthful `#page=N` target.
6. At report assembly, provide every exact report-card field required by `report_spec.md` for every C ID. The ledger and recheck jointly supply the source evidence, comparator, reasoning, calculation or logical comparison, alternatives, mechanical facts, and exact human question, but they are not themselves the final-card template. Every final card must include bounded quality-control relevance and potential downstream evidence impact. No card may claim that propagation or a conclusion change occurred.
7. Every final-card human-adjudication subfield must use the exact blank placeholder `__`: `Validity`, `Importance`, `Action`, `Initials`, and `Notes`. No current ledger or recheck section contains a conflicting adjudication value. Because no card mentions a display-zero P value, the conditional independent-contradiction field is not required for the current stable set.
8. Append the report-generator execution to `agent_execution_manifest.md` when spawned, and include that agent plus every existing manifested execution in the final token ledger. Any later model repair similarly requires a manifest and token-ledger record.

## C001 — Abstract sex percentage conflicts with the enrolled sex count

- **Evidence and link audit:** DOC-001 physical pp. 1 and 4 resolve and print the matched enrolled-population statements: 30 enrolled with `22% men`, versus 22 men and 8 women.
- **Category and rule audit:** `Denominator, proportion, or total inconsistency` is the appropriate primary category. The identity is direct and reproducible: `22 + 8 = 30` and `22/30 = 73.33%`, not 22%.
- **Direct/inferred distinction:** The printed denominator, count, percentage, and sex-component total are direct. A lost count label, substituted percent sign, or alternate intended percentage is explicitly an inferred explanation.
- **Provenance and duplication:** NUM001 and CROSS-001 are genuine duplicates of the same enrolled-population field and were appropriately consolidated. No other C ID uses this comparator and rule.
- **Human question and report-card control:** The recheck names the authoritative enrollment data/proof as missing and asks whether the field should be `22 men`, approximately `73% men`, or another value. The final card should bound downstream relevance to possible extraction of the baseline sex count/percentage.

## C002 — INQoL IQR endpoints exceed the stated 0-to-100 scale

- **Evidence and link audit:** DOC-001 physical p. 5 resolves to the Table 1 INQoL row and footnote f. The row prints upper IQR endpoints 110.3 and 120.0; the footnote prints a 0-to-100 scale.
- **Category and rule audit:** `Measure, label, or scale inconsistency` is appropriate. Under the printed bound, quantiles cannot exceed 100; the excesses of 10.3 and 20.0 points are reproduced exactly.
- **Direct/inferred distinction:** The endpoints and footnote are direct. An incomplete footnote, summed score, or alternate transform is explicitly an inferred source-grounded possibility, not an assumed correction.
- **Provenance and duplication:** NUM002 alone generated this relationship. It does not duplicate C003, which concerns treatment-effect direction, or any statistical candidate.
- **Human question and report-card control:** The recheck asks for the authoritative INQoL scoring range and algorithm. The final card should bound downstream relevance to possible copying of either the scale or the baseline distribution.

## C003 — Table 2 secondary-outcome contrast header is opposite to the displayed effect signs

- **Evidence and link audit:** DOC-001 physical p. 7 contains the `Treatment Effect (Placebo-Mexiletine)` header and repeated change-score rows; p. 8 contains the continuation and footnotes. All cited targets resolve.
- **Category and rule audit:** `Measure, label, or scale inconsistency` is appropriate. Exact rows reproduce mexiletine minus placebo: `-21.44 - (-7.22) = -14.22` and `-2.39 - 0.46 = -2.85`. The SF-36 rows independently preserve the same sign direction even where rounded marginal changes do not reproduce the paired estimate's magnitude.
- **Direct/inferred distinction:** Header, signs, period changes, and effect values are direct. A reversed header or undocumented favorable-direction convention is inferred and remains an exact human question.
- **Provenance and duplication:** NUM003 and STAT1-001 cover the same header/column rule and were correctly consolidated. C013-C014 concern different placebo-period interval cells, so retaining them separately is appropriate.
- **Human question and report-card control:** The recheck asks which contrast was actually computed and whether the header, signs, or a note should state it. The final card should limit downstream relevance to possible inversion during effect extraction or synthesis; it must not claim that such inversion has occurred.

## C004 — Placebo “Any” adverse-reaction percentage does not reconcile with the apparent denominator

- **Evidence and link audit:** DOC-003 physical p. 6 resolves to eTable 4 and DOC-001 physical p. 8 resolves to the `21 of 30 (70%)` adverse-event comparator. The preliminary p. 9 locator is no longer used by the ledger or recheck.
- **Category and rule audit:** `Denominator, proportion, or total inconsistency` is appropriate. Under the apparent common patient denominator and nearest-whole-percent convention, `2/30 = 6.67%`, ordinarily 7%, while neighboring 1-, 2-, 3-, 21-, and 27-count rows support the stated comparison.
- **Direct/inferred distinction:** `2 (6%)`, neighboring pairs, and `21 of 30` are direct. A denominator of 31 treatment-set exposures or truncation is inferred; the ledger and recheck do not present the apparent denominator as certain.
- **Provenance and duplication:** NUM004 is the sole provisional record. It is distinct from participant-flow and treatment-set totals because its exact comparator is the adverse-reaction count/percentage pair.
- **Human question and report-card control:** The exact denominator, analysis unit, handling of repeated sets/dropouts, and rounding rule remain missing. The final card must preserve this conditional basis and limit downstream relevance to possible adverse-event rate extraction.

## C005 — Bayesian parameter prose swaps `mu_mex[i]` and `mu_plac[i]` treatment labels

- **Evidence and link audit:** DOC-003 p. 11 prints the eMethods 2 code and the relevant swapped mean-parameter dictionary rows; p. 13 prints the eMethods 3 code; p. 14 prints the eMethods 3 dictionary. The source comparison is exact and the repaired ledger gives each relevant physical page its own target.
- **Category and rule audit:** `Measure, label, or scale inconsistency` is appropriate. Both code blocks map `Stiff_Plac` to `mu_plac` and `Stiff_Mex` to `mu_mex`, while both dictionaries assign the opposite treatment meanings.
- **Direct/inferred distinction:** Code/data mappings and prose labels are direct. A prose-only transposition and unaffected execution are inferred; executed model files and outputs are not supplied.
- **Provenance and duplication:** NUM005, CROSS-003, and STAT1-006 are genuine duplicates of the same two-parameter treatment-label swap. C007 is separate because it concerns a variance parameter rather than these mean parameters.
- **Human question and report-card control:** The recheck asks which mapping appears in the authoritative executed files. Downstream relevance must be bounded to model interpretation or reproduction if the documentation is copied.

## C006 — `diff_CLCN1` is described as an SCN4A contrast

- **Evidence and link audit:** DOC-003 physical p. 13 prints `diff_CLCN1 <- mu.plac_CLCN1 - mu.mex_CLCN1`; p. 14 prints the SCN4A prose label. Both links resolve and pagination is exact.
- **Category and rule audit:** `Measure, label, or scale inconsistency` is appropriate. The parameter suffix and both code components identify CLCN1, while the dictionary names SCN4A; treatment/genotype identity is categorical.
- **Direct/inferred distinction:** The code and label are direct. A copy-forward documentation error with unaffected analysis is inferred and not presented as fact.
- **Provenance and duplication:** NUM006, CROSS-005, and STAT1-007 are the same `diff_CLCN1` relationship. C005 and C007 concern different parameter names and rules.
- **Human question and report-card control:** The recheck asks whether the row should identify CLCN1 and whether downstream output retained that mapping. The final card should bound relevance to subgroup-effect identification and reproduction.

## C007 — `sigma.mex` is described as placebo-period variability

- **Evidence and link audit:** DOC-003 pp. 11-12 and 13-14 resolve to both code/dictionary pairs. The source shows `tau.mex = 1/sigma.mex^2`, its use with `mu_mex`, and dictionaries that call `sigma.mex` placebo variability.
- **Category and rule audit:** `Measure, label, or scale inconsistency` is appropriate. The likelihood branch, suffix, and parallel `.plac` parameter provide a concrete categorical comparator.
- **Direct/inferred distinction:** Code associations and dictionary wording are direct. A repeated copy-forward documentation error and unaffected model run are inferred.
- **Provenance and duplication:** NUM007 and CROSS-004 are genuine duplicates. The record is not merged with C005 because the printed parameter, comparator, and potential extraction target differ.
- **Human question and report-card control:** The recheck asks which period `sigma.mex` represented in executed models. Downstream relevance must be limited to variance-component interpretation or model reproduction.

## C008 — Main text prints `CLNC1` for the matched `CLCN1` genotype subgroup

- **Evidence and link audit:** DOC-001 p. 4 prints `CLNC1` for the 3.84 result; DOC-001 pp. 5-6 and DOC-003 p. 4 print `CLCN1` for the matched n=16 subgroup and gene definition. All physical pages are correct and now have separate page targets.
- **Category and rule audit:** `Measure, label, or scale inconsistency` is appropriate because identical population, estimate, interval, n, and genotype context establish a concrete result-label mismatch.
- **Direct/inferred distinction:** The two strings and matched quantitative keys are direct. A local typographical transposition is inferred.
- **Provenance and duplication:** CROSS-002 alone generated this candidate. It is not a generic spelling issue; the numeric result and subgroup identity make it in-scope, and no other stable ID uses this label comparison.
- **Human question and report-card control:** The recheck asks whether the p. 4 sentence should read `CLCN1`. Downstream relevance should be bounded to subgroup-label extraction.

## C009 — SF-36 mental-component P value conflicts with the dependent-t 95% CI

- **Evidence and link audit:** DOC-001 p. 7 prints effect 6.78, 95% CI 1.64 to 11.92, and `P=.001`; p. 3 supplies the dependent-t method and p. 4 supplies the two-sided convention. The repaired ledger and recheck link all three physical pages separately.
- **Category and rule audit:** `Statistical reporting inconsistency` is appropriate. With the table-level N=27 assumption explicitly labeled as conditional, half-width 5.14, `SE about 2.50`, `t about 2.71`, and two-sided `P about .012` reproduce the diagnostic and do not reconcile with `.001`.
- **Direct/inferred distinction:** Printed result fields and method statements are direct. Treating table N=27 as 27 complete pairs and applying df=26 is inferred; the recheck names row-specific n, raw pairs, unrounded values, and exact implementation as missing.
- **Provenance and duplication:** STAT1-002 alone generated this row-specific result. It is distinct from C003's column-label rule and from every other inferential row.
- **Human question and report-card control:** The exact question asks which P value, interval, n, or procedure is authoritative. Any downstream statement must be limited to possible extraction of this result set if the mismatch is confirmed.

## C010 — SCN4A fifth handgrip-action-myotonia P value conflicts with its 95% CI

- **Evidence and link audit:** DOC-001 p. 7 prints effect -1.96, CI -3.41 to 0.51, and `P=.009`; p. 8 supplies the dependent-t subgroup footnote; pp. 3-4 supply method and sidedness. The repaired ledger and recheck link every physical page separately.
- **Category and rule audit:** `Statistical reporting inconsistency` is appropriate. The interval crosses zero, its midpoint is -1.45 rather than -1.96, and the conditional df=10 width diagnostic is near two-sided `.05`, not `.009`.
- **Direct/inferred distinction:** The off-center, zero-crossing interval and P value are direct. The df=10 diagnostic applies the printed subgroup n and test rule; raw pairs, complete-case n, unrounded output, and any alternate procedure are missing.
- **Provenance and duplication:** STAT1-003 alone generated this SCN4A fifth-attempt row. It is distinct from C013, which concerns the total-group first-attempt placebo-period interval.
- **Human question and report-card control:** The recheck asks for the exact paired sample, estimate, SE, endpoints, statistic, and P value. Downstream relevance should be limited to extraction of this subgroup inferential result.

## C011 — SCN4A fifth transient-paresis estimate, interval, and P value do not form a compatible dependent-t result

- **Evidence and link audit:** DOC-001 p. 7 prints 13.71, CI -1.96 to 25.47, and `P=.02`; p. 8 supplies the dependent-t subgroup footnote; pp. 3-4 supply method and sidedness. The repaired ledger, recheck, and fresh main evidence map now use the exact pages. The direct PDF confirms `.02`.
- **Category and rule audit:** `Statistical reporting inconsistency` is appropriate. The CI crosses zero, has midpoint 11.755 rather than 13.71, and under the stated conditional df=10 diagnostic gives a two-sided P near .05 rather than .02.
- **Direct/inferred distinction:** The repeated estimate/interval, off-center midpoint, zero crossing, and P value are direct. A missing sign, field transcription, different n, or alternate implementation is inferred.
- **Provenance and duplication:** STAT1-004 alone generated this exact row. It is distinct from C010 and C012 because the outcome, subgroup result, and printed fields differ.
- **Human question and report-card control:** The recheck asks for the authoritative lower endpoint, complete-pair n, SE/statistic, and P value. Downstream relevance should be limited to possible extraction of this subgroup inferential result.

## C012 — Myotonic-discharge P value conflicts with the dependent-t 95% CI

- **Evidence and link audit:** DOC-001 p. 8 prints effect 0.67, CI 0.23 to 1.11, and `P<.001`; p. 3 supplies the dependent-t method and p. 4 the two-sided convention. The repaired ledger and recheck link all three physical pages separately.
- **Category and rule audit:** `Statistical reporting inconsistency` is appropriate. Under the explicitly conditional table-level N=27 assignment, half-width 0.44 yields `SE about 0.214`, `t about 3.13`, and two-sided `P about .004`, not below .001.
- **Direct/inferred distinction:** Period means, effect, CI, P threshold, and methods are direct. The df=26 calculation assumes 27 complete pairs; row-specific n, paired-difference SD, and exact output are missing.
- **Provenance and duplication:** STAT1-005 alone generated this result. It is distinct from C009-C011 and is the only current candidate result cell on the Table 2 continuation page.
- **Human question and report-card control:** The recheck asks for row-specific n, paired-difference SD/SE, statistic, CI method, and exact P value. Downstream relevance should be limited to extraction of this inferential result.

## C013 — First handgrip placebo-period interval is reversed and excludes its estimate

- **Evidence and link audit:** DOC-001 physical p. 7 resolves to the first-attempt handgrip placebo-period cell and prints `0.46 (-0.30 to -1.23)`.
- **Category and rule audit:** `Statistical reporting inconsistency` is appropriate. `-0.30 > -1.23`, and reordering the endpoints still leaves 0.46 outside. The same-row identity `-2.39 - 0.46 = -2.85` supports the printed point estimate under the table's observed sign direction.
- **Direct/inferred distinction:** Endpoint order, estimate containment, and row arithmetic are direct. A missing positive sign or other interval transcription is inferred.
- **Provenance and duplication:** STAT2-001 is a genuinely new pass-2 observation. It is not C003's treatment-effect header rule or C010's subgroup fifth-attempt effect/CI/P rule.
- **Human question and report-card control:** The recheck asks for the authoritative placebo estimate, endpoints, SE, and paired n. Downstream relevance should be limited to extraction of this placebo-period summary.

## C014 — Mean Timed Up&Go placebo-period estimate lies outside its interval

- **Evidence and link audit:** DOC-001 physical p. 7 resolves to the mean Timed Up&Go placebo-period cell and prints `0.07 (-0.67 to 0.01)`.
- **Category and rule audit:** `Statistical reporting inconsistency` is appropriate. The ordered interval's upper endpoint is 0.01, so the estimate exceeds it by 0.06. Same-row arithmetic `-1.05 - 0.07 = -1.12` supports the printed estimate under the observed table direction.
- **Direct/inferred distinction:** Estimate, endpoints, containment failure, and row arithmetic are direct. A missing endpoint digit, estimate sign, or other field transcription is inferred.
- **Provenance and duplication:** STAT2-002 is a genuinely new pass-2 observation and is distinct from C013 by outcome and cell.
- **Human question and report-card control:** The recheck asks for the authoritative estimate, endpoints, SE, and paired n. Downstream relevance should be limited to extraction of this placebo-period summary.

## Audit limitations

- The package does not include raw paired observations, row-specific complete-case counts, unrounded inferential output, executed Bayesian model files/logs, an explicit eTable 4 denominator/rounding rule, or the authoritative INQoL scoring worksheet. The candidate artifacts name these missing inputs and do not infer them as facts.
- Artifact declarations and path inspection show a fresh derivative chain with no legacy-audit evidence citation. This audit cannot independently inspect unrecorded reasoning outside the durable artifacts; it therefore confirms nonuse of old derivatives from the reproducible evidence chain and explicit provenance statements.
- The final report, human-adjudication templates, token ledger, post-run source-hash file, HTML, and validator result did not yet exist at this audit cutoff. Their completion remains a coordinator responsibility and must incorporate the repairs above.

**Canonical quality-audit coverage:** C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014.
