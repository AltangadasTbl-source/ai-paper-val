# Final Evidence-Quality Audit

All 12 immutable stable candidate IDs remain **Pending Human Adjudication**. This audit reviewed the complete source and coverage ledgers, main/support extraction maps and relationship parts, numeric and statistical inventories, numeric and cross-source checker outputs, both independent statistical passes, the candidate ledger, the mechanical evidence recheck, source and reused-artifact hash baselines, and the agent execution manifest. It did not use a legacy candidate list or any external source.

## Coverage, execution, and integrity audit

- **Direct-source closure:** Seven supplied PDFs contain 159 stable PDF-page units. Every source row is `COMPLETE`; each row satisfies reusable units plus fresh-required units equals total units and mapped units equals total units. Package totals reproduce as `28 + 131 = 159`, with `159/159` mapped.
- **Page-count reproduction:** Direct `pdfinfo` checks reproduced DOC-001 through DOC-007 page counts as 10, 94, 18, 27, 8, 1, and 1, respectively.
- **No ranked-count boundary:** The main and support maps explicitly cover every page, including no-applicable-result pages. The numeric inventory covers N001-N033; the statistical inventory covers S001-S021; the checker artifacts process those complete sets. The artifacts state that no legacy candidate set was used, and no review queue, candidate limit, early stop, or ranked-ten selection appears in the discovery chain.
- **Coverage-manifest structure:** Every row contains one plain relative POSIX artifact path. Required pre-report stages are present. Numeric rows enumerate all 33 N IDs; both statistical-pass scopes enumerate all 21 S IDs; candidate registration and evidence recheck enumerate C001-C012 individually. The later coordinator confirmation of C010 has its own row and unique artifact path.
- **Relationship completion:** N001-N033 are mapped and checked. S001-S021 each have explicit `PASS_1_COMPLETE` and `PASS_2_COMPLETE` records. Statistical pass 2 reviewed all 12 registered C IDs and all recheck facts and added no candidate.
- **Statistical execution:** `root/statistical_pass_1` and `root/statistical_pass_2` are distinct normalized runtime agent IDs. Both are recorded as fresh `gpt-5.6-terra` agents at high reasoning effort with separate primary artifacts. The manifest also records the coordinator and every specialist used through this audit exactly once.
- **Stable-ID closure:** Candidate ledger, evidence recheck, and this quality audit contain the identical intended set C001-C012. No ID was deleted, merged, suppressed, ranked, renumbered, or scientifically adjudicated after registration.
- **Source integrity:** Recalculation with both baseline checksum files returned `OK` for all 7 direct sources and all 88 reused artifacts. No source or reused artifact changed.
- **Link and pagination check:** Every evidence-recheck PDF link resolves from its artifact location to an existing supplied PDF and ends in `#page=N`. Cited pages are within the reproduced document page counts. The C010 run-local visual-confirmation artifact exists at `preprocessing/coordinator_confirmations/doc004-p23.png`; its manifest row contains only that path.
- **Display-zero exclusion:** No candidate is based on, or mentions, `P = 0`, `p = 0.000`, or an equivalent display zero. Both statistical passes explicitly report zero display-zero records. No conditional independent-contradiction field is therefore required for C001-C012.
- **Categories and tone:** Every ledger record uses exactly one category allowed by `QUALITY_CONTROL_SCOPE.md`. Wording remains neutral and separates observed printed mismatches from inferred explanations. None of the records claims that the paper-level conclusion is wrong.

## Report-card completion control

The ledger is a registration artifact rather than the final report, so its compact records do not yet use every exact final-card label. For each C001-C012, the report generator must carry forward the source substance documented below and include the exact labels `Candidate statement`, `Category`, `Exact source locations`, `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Alternative source-grounded interpretations`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields`. The downstream field must name only what a data extractor, systematic review, meta-analysis, or guideline could copy if the candidate is confirmed; it must not claim that propagation or conclusion change occurred.

Every final candidate card must end with exactly:

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C001 — Baseline index-stroke type counts differ across baseline tables

- **Status/category:** Pending Human Adjudication; `Cross-document numeric inconsistency` is in scope.
- **Evidence and reproducibility:** DOC-001 p.4 and DOC-004 pp.10-11 are found and correctly paginated. Main levodopa counts reproduce as `260 + 47 = 307`; supplement counts reproduce as `263 + 44 = 307`. The exact same-arm categories differ by `+3/-3` while the placebo values agree.
- **Support audit:** Printed values, comparator, identity rule, direct-versus-inferred distinction, missing recoding/data-version definition, alternative interpretation, and exact human question are complete in the ledger/recheck. No unsupported arithmetic or false pagination remains.
- **Duplicate/impact audit:** This relationship is not duplicated by another C ID. The report may state only that confirmed stroke-type counts could be copied incorrectly into trial-characteristic or subgroup extraction; no conclusion impact is established.
- **Final-card fields:** All exact report-card labels and the five `__` adjudication placeholders remain to be added during report assembly.

## C002 — Baseline NIHSS statistic and label do not reconcile across tables

- **Status/category:** Pending Human Adjudication; `Measure, label, or scale inconsistency` is in scope.
- **Evidence and reproducibility:** DOC-001 pp.4-5 and DOC-004 p.11 are found and correctly paginated. Main median/IQR values have two interval endpoints, whereas the supplement's row labelled median/IQR prints decimal central values with one parenthesized value. The forms cannot be equated without a missing statistic definition.
- **Support audit:** The recheck appropriately treats mean (SD) as an inference, not a fact. The missing meaning of `8.2 (3.9)` and the exact human question are stated. No arithmetic selection of a preferred summary is made.
- **Duplicate/impact audit:** C002 is distinct from C003 because the printed variable and rule differ. A confirmed label/value mismatch could affect baseline-severity extraction; no paper-conclusion impact is established.
- **Final-card fields:** All exact report-card labels and the five `__` adjudication placeholders remain to be added during report assembly.

## C003 — Time from stroke onset to randomization differs across baseline tables

- **Status/category:** Pending Human Adjudication; `Cross-document numeric inconsistency` is in scope, conditional on the shared unit.
- **Evidence and reproducibility:** DOC-001 p.4 and DOC-004 p.11 are found and correctly paginated. The supplement row prints `7/8/7` but does not visibly print a unit. Under confirmation of the main table's day unit, the arm medians differ by 4 and 5 days and cannot be explained by rounding.
- **Support audit:** The repaired ledger, numeric checker, cross-source checker, and recheck now distinguish the observed same-name values from the inferred common-day unit. Missing unit, time origin, derivation, population, and data-version definitions are named. No unsupported unconditional day claim remains.
- **Duplicate/impact audit:** C003 is distinct from C001/C002 by variable and rule. If confirmed under the same unit, the timing values could affect trial-timing extraction; no treatment-effect or conclusion impact is established.
- **Final-card fields:** The final card must preserve the conditional unit wording, all exact labels, and the five `__` adjudication placeholders.

## C004 — Estimand 4 confidence-interval upper endpoint differs within eTable 2

- **Status/category:** Pending Human Adjudication; `Statistical reporting inconsistency` is in scope.
- **Evidence and reproducibility:** DOC-004 pp.12-13 are found and correctly paginated. The point estimate and lower endpoint agree, while the upper endpoints reproduce as `1.25` and `1.26`, a displayed difference of `0.01`.
- **Support audit:** The source does not supply an unrounded endpoint or separate analysis rule, so rounding/transcription is correctly retained as an unresolved alternative. The record does not infer an exact replacement value.
- **Duplicate/impact audit:** C004 is distinct from C011 and C012: it compares CI endpoints, whereas those IDs compare measure labels. A confirmed endpoint mismatch could be copied into effect-precision extraction; no conclusion change is claimed.
- **Final-card fields:** All exact report-card labels and the five `__` adjudication placeholders remain to be added during report assembly.

## C005 — Levodopa PROMIS-29 descriptive mean differs between main text and eTable 4

- **Status/category:** Pending Human Adjudication; `Cross-document numeric inconsistency` is in scope.
- **Evidence and reproducibility:** DOC-001 p.6 and DOC-004 p.15 are found and correctly paginated. `64.74` rounds to 65, not 66, and `64.74 - 65.11 = -0.37`; the table is internally aligned with its printed effect while the main levodopa descriptive mean does not follow ordinary whole-number rounding.
- **Support audit:** The record distinguishes descriptive from adjusted quantities and names scoring, analysis-set, and unrounded-value definitions that are unavailable. It does not assume a mechanism or select an authoritative mean.
- **Duplicate/impact audit:** C005 is distinct from C006 by PROMIS instrument and from C007 by endpoint/statistic. A confirmed descriptive-mean mismatch could affect secondary-outcome extraction; no paper-conclusion impact is established.
- **Final-card fields:** All exact report-card labels and the five `__` adjudication placeholders remain to be added during report assembly.

## C006 — PROMIS-10 descriptive means differ between main text and eTable 4

- **Status/category:** Pending Human Adjudication; `Cross-document numeric inconsistency` is in scope.
- **Evidence and reproducibility:** DOC-001 p.6 and DOC-004 p.15 are found and correctly paginated. Both detailed means round to 30, not 28. The raw difference `30.04 - 29.87 = 0.17` is not incorrectly forced to equal the adjusted estimate `0.18`.
- **Support audit:** Missing scoring/version, analysis-population, and unrounded narrative inputs are named. The source-grounded alternative is stated without assuming it occurred.
- **Duplicate/impact audit:** C006 is a separate endpoint from C005 and C007. Confirmed values could affect PROMIS-10 descriptive extraction; no conclusion impact is established.
- **Final-card fields:** All exact report-card labels and the five `__` adjudication placeholders remain to be added during report assembly.

## C007 — Placebo five-week FMA standard deviation differs from eTable 4

- **Status/category:** Pending Human Adjudication; `Cross-document numeric inconsistency` is in scope.
- **Evidence and reproducibility:** DOC-001 p.6 and DOC-004 p.15 are found and correctly paginated. The corrected numeric checker and recheck reproduce that `25.20` rounds to 25, not the main-text 26; the placebo mean and both levodopa values otherwise follow ordinary rounding.
- **Support audit:** A prior N014 rounding error was repaired by the coordinator. The final checker, ledger, and recheck no longer contain that arithmetic defect. Missing unrounded data, population, imputation, and rounding convention remain explicit human questions.
- **Duplicate/impact audit:** C007 is not duplicated by the PROMIS candidates because it concerns the five-week FMA placebo SD. A confirmed SD mismatch could affect descriptive-variance extraction; no treatment-effect or conclusion impact is established.
- **Final-card fields:** All exact report-card labels and the five `__` adjudication placeholders remain to be added during report assembly.

## C008 — Placebo PRAI no-improvement numerator differs between main text and eTable 4

- **Status/category:** Pending Human Adjudication; `Cross-document numeric inconsistency` is in scope.
- **Evidence and reproducibility:** DOC-001 p.6 and DOC-004 p.15 are found and correctly paginated. `51/270 = 18.888...%`, matching 18.89%, while `52/270 = 19.259...%`, compatible with whole-percent 19%; percentages can each fit their own numerator, but the same-denominator numerator differs by one.
- **Support audit:** The record correctly names a possible response-category difference without asserting it. Numerators, denominator, category wording, and remaining record-level definition are complete.
- **Duplicate/impact audit:** C008 is distinct from the continuous-outcome records C005-C007. A confirmed numerator discrepancy could affect binary-outcome extraction; no downstream propagation or conclusion change is claimed.
- **Final-card fields:** All exact report-card labels and the five `__` adjudication placeholders remain to be added during report assembly.

## C009 — eTable 6 overall adverse-event total is one below arms and category sums

- **Status/category:** Pending Human Adjudication; `Denominator, proportion, or total inconsistency` is in scope.
- **Evidence and reproducibility:** DOC-001 pp.6-7 and DOC-004 p.17 are found and correctly paginated. Arms reproduce as `67 + 79 = 146`; intensity as `58 + 86 + 2 = 146`; outcome as `1 + 29 + 116 = 146`; drug relation as `2 + 66 + 23 + 2 + 39 + 14 = 146`. Each conflicts with the printed overall 145.
- **Support audit:** The event-count unit is correctly distinguished from participant counts. No exclusion or duplicate-event rule is supplied, and the record asks for one rather than assuming a typographical correction.
- **Duplicate/impact audit:** C009 is the only stable ID for this same printed overall/event-set rule; numeric and cross-source proposals were genuinely merged before IDs. A confirmed total mismatch could affect safety-event extraction; no safety conclusion change is established.
- **Final-card fields:** All exact report-card labels and the five `__` adjudication placeholders remain to be added during report assembly.

## C010 — eFigure 4 switches from FMA to FMMA in its axis abbreviation

- **Status/category:** Pending Human Adjudication; `Measure, label, or scale inconsistency` is retained as a neutral local-abbreviation consistency question.
- **Evidence and reproducibility:** DOC-004 p.23 is found and correctly paginated. Direct 240-dpi source rendering visibly confirms the title `FMA Total Score` and axis `Adjusted Mean Difference (FMMA points)`. DOC-003 p.2 also directly defines `Fugl-Meyer Motor Assessment (FMMA)`.
- **Support audit:** The coordinator repaired the earlier unsupported “undefined abbreviation/typo” framing. The final record now treats the SAP definition as direct source-grounded evidence that FMMA may be an intentional synonym; only the within-figure switch and lack of a local explanation are observed. No claim that the numeric plot is wrong is supported.
- **Duplicate/impact audit:** C010 is distinct from C011/C012 because it concerns the outcome abbreviation rather than Estimand 4's effect-measure label. If confirmed as a presentation issue, an extractor could copy inconsistent outcome terminology; no numeric or conclusion impact is established.
- **Final-card fields:** The final card must include DOC-003 p.2 in the exact source locations/alternative interpretation, avoid asserting an undefined measure or typographical error as fact, and include all exact labels and five `__` placeholders.

## C011 — Estimand 4 win ratio appears under an FMA mean-difference column heading

- **Status/category:** Pending Human Adjudication; `Measure, label, or scale inconsistency` is in scope.
- **Evidence and reproducibility:** DOC-004 p.13 is found and correctly paginated. The spanning column heading identifies a mean difference on FMA, while the Estimand 4 row identifies a win ratio with 95% CI. These are not the same measure/scale under any definition supplied on the page.
- **Support audit:** The row-specific label potentially overriding a general heading is correctly recorded as an alternative, not a resolution. The missing header exception/footnote and exact human question are present.
- **Duplicate/impact audit:** C011 is distinct from C012 because its comparator is the table heading, and from C004 because it does not concern an endpoint value. A confirmed heading-scope issue could cause an extractor to assign the wrong effect measure; no conclusion impact is established.
- **Final-card fields:** All exact report-card labels and the five `__` adjudication placeholders remain to be added during report assembly.

## C012 — Estimand 4 is called an odds ratio in prose and a win ratio in the table

- **Status/category:** Pending Human Adjudication; `Measure, label, or scale inconsistency` is in scope.
- **Evidence and reproducibility:** DOC-004 pp.12-13 are found and correctly paginated. The same named Estimand 4 value `1.06` is labelled `odds ratio` in prose and `win ratio` in the row. No supplied model identity equates the two terms.
- **Support audit:** A possible modelling relationship is explicitly treated as unresolved because the required definition is missing. The record does not select one measure name or infer interchangeability.
- **Duplicate/impact audit:** C012 is distinct from C011 by comparator and from C004 by rule. A confirmed measure-label mismatch could cause an effect estimate to be extracted under the wrong measure; no conclusion change or actual propagation is claimed.
- **Final-card fields:** All exact report-card labels and the five `__` adjudication placeholders remain to be added during report assembly.

## Audit completion and limitations

- **Coverage status:** Complete for 7/7 direct sources, 159/159 source units, N001-N033, S001-S021 in both passes, and C001-C012 in ledger/recheck/quality artifacts.
- **Repairs confirmed:** C003 now conditions its day calculation on the supplement's omitted unit; N014/C007 now use the correct `25.20` to 25 rounding; C010 has direct visual confirmation and incorporates the SAP's explicit FMMA definition without asserting an undefined abbreviation or typographical error.
- **Remaining source limitations:** C003 still requires human confirmation of the supplement row's unit/time origin. C002 requires the statistic represented by the supplement NIHSS values. C004 requires unrounded analysis output. C005-C008 require the named score/population/record definitions. C009 requires an event-counting rule if 145 is intentional. C011-C012 require the intended header scope and effect-measure definition. These are adjudication questions, not scientific dispositions.
- **Report-stage condition:** At the time of this audit, `evidence_quality` and `report_generation` are the only manifest stages awaiting coordinator completion. The report generator must return all 12 cards, apply the exact labels and five `__` placeholders above to every card, preserve neutral wording and bounded downstream impact, and add no severity or scientific disposition.

**Canonical audit artifact:** `quality/evidence_quality_audit.md`
