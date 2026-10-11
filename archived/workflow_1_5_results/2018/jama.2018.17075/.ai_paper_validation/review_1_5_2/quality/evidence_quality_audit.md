# Workflow 1.5.2 Evidence-Quality Audit

## Audit scope and state

This is the mandatory pre-report evidence-quality gate for the fresh Workflow 1.5.2 run. It audits all 8 stable candidates, all 16 coverage-manifest rows, all 4 direct-source coverage rows, all 73 numeric relationships (`N001` through `N073`), all 32 statistical relationships (`S001` through `S032`), both statistical passes, the cross-source and numeric checker outputs, the stable ledger, and the mechanical evidence recheck. Every candidate remains **Pending Human Adjudication**. This audit assigns no scientific disposition, severity, ranking, acceptance, exclusion, or correction.

- **Stable candidate set audited:** C001; C002; C003; C004; C005; C006; C007; C008.
- **Canonical ID-set state at this gate:** the ledger, evidence recheck, and this quality artifact each contain exactly C001-C008. The report is intentionally not yet generated; its candidate-heading set must be checked after assembly.
- **Evidence boundary:** only the four supplied PDFs, fresh assets under `review_1_5_2/preprocessing/`, and current-run artifacts were used. The inventories and checker provenance consistently state that legacy audit derivatives and external sources were not used. No contrary evidence was found.
- **Discovery boundary:** the explicit 73/73 numeric, 32/32 statistical pass-1, 32/32 statistical pass-2, and 73+32 cross-source records demonstrate complete relationship processing. No top-N, count target, review queue, or early-stopping boundary appears in the discovery artifacts.
- **Display-zero boundary:** neither statistical pass found a `P=0`, `p=0.000`, or equivalent assigned relationship. The checked `<.0001` values are inequalities. No stable candidate is based on a display-zero P value, and no candidate card requires the conditional independent-contradiction field.

## Source and evidence coverage audit

| Source | PDF pages | Reusable | Fresh-required | Mapped | Audit result |
|---|---:|---:|---:|---:|---|
| DOC-001, `jama_cooper_2018_oi_180132.pdf` | 10 | 0 | 10 | 10 | Complete source-unit equality |
| DOC-002, `joi180132supp1_prod.pdf` | 194 | 0 | 194 | 194 | Complete source-unit equality |
| DOC-003, `joi180132supp2_prod.pdf` | 24 | 0 | 24 | 24 | Complete source-unit equality |
| DOC-004, `joi180132supp3_prod.pdf` | 1 | 0 | 1 | 1 | Complete source-unit equality |

The four page counts were independently confirmed with `pdfinfo`. The 229-page union was freshly extracted as native and layout text and rendered as 229 PNG page assets. Native/layout evidence was usable on all result-relevant pages, so the documented 0-page OCR decision is supportable. Current SHA-256 values exactly match `source_hashes_before.sha256` for all four sources.

The canonical numeric inventory contains exactly 73 table rows, one each for N001-N073. The numeric checker contains exactly 73 corresponding result rows and separately checks the numerical implications of all 32 S relationships. The statistical inventory contains exactly 32 rows, one each for S001-S032. Statistical pass 1 and pass 2 each contain exactly 32 table rows and mark every assigned S ID `PASS_1_COMPLETE` or `PASS_2_COMPLETE`. Cross-source review expressly covers N001-N073 and S001-S032. No relationship-unit omission or duplicate stable inventory row was found.

The support evidence-map transcription for SN032 was repaired during this audit: it now preserves the source's malformed `.95 (0.55-275 1.64) P=.84` string verbatim and labels `.55-1.64` as conjectural rather than extracted evidence.

## Coverage-manifest audit

The manifest has 16 data rows covering every required stage. Every row has exactly one undecorated POSIX-style relative artifact path; all 14 artifacts marked `COMPLETE` resolved at audit time. Candidate-registration, evidence-recheck, evidence-quality, statistical-pass-2 cross-lane, and report-generation scopes explicitly enumerate C001; C002; C003; C004; C005; C006; C007; C008. Both statistical-pass scopes explicitly enumerate S001-S032.

Two expected workflow transitions remain for the coordinator:

1. After this file is written, change the `evidence_quality` row from `IN_PROGRESS` to `COMPLETE`.
2. After the Markdown report is assembled and checked, change `report_generation` from `PLANNED` to `COMPLETE`. At this audit gate the report artifact does not yet exist, as required by the workflow sequence.

No source, relationship, or candidate scope may be shortened during those transitions.

## Agent-execution and statistical-pass audit

The execution manifest contains 10 unique current agent rows, including the coordinator exactly once and this auditor. Statistical pass 1 is `/root/statistics_pass_1`; statistical pass 2 is `/root/statistics_pass_2`. They are distinct fresh runtime IDs, each recorded as `gpt-5.6-terra`, reasoning effort `high`, start mode `FRESH_SPAWN`, and each has one primary artifact. Pass 2 explicitly integrates all 8 ledger candidates and the complete evidence recheck, and emits no new candidate.

The manifest is complete for agents that have executed through this gate. The coordinator must add the future report-generator agent exactly once after it is spawned, and any later repair agent exactly once if an additional model call occurs. Those agents must also appear in the token ledger before final validation.

## Candidate-card field gate

For every C ID below, the ledger plus recheck supply a candidate statement, one allowed primary category, exact source locations, source evidence, reported-versus-comparator facts, a reproducible reasoning procedure/calculation or logical parse, source-grounded alternatives, a mechanical recheck, direct-versus-inferred separation, and an exact human question. The report generator must add the report-only fields for quality-control relevance, bounded potential downstream evidence impact, and human verification steps without claiming that propagation or conclusion change occurred.

Every final-report card must use the exact adjudication template below; every subfield must retain the exact blank placeholder `__`:

```markdown
**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __
```

Because the report is downstream of this gate, final-card label presence, final placeholder preservation, and report/ledger/recheck/quality heading-set identity require a post-assembly mechanical check.

## C001 — Normothermia Injury Severity Score median is below its printed IQR lower endpoint

- **State and category:** Pending Human Adjudication; `Numeric or arithmetic inconsistency`, an allowed primary category.
- **Evidence and pagination:** [DOC-001 PDF p. 5, Table 1](../../../jama_cooper_2018_oi_180132.pdf#page=5) prints the normothermia Injury Severity Score as median `20.0` with IQR `20.5-35.0`. Page 5 exists within the 10-page source, and the link target resolves.
- **Reproducibility:** the labelled lower quartile exceeds the labelled median: `20.5 - 20.0 = 0.5`. Under the supplied median/IQR definition, `Q1 <= median <= Q3` is applicable. Participant-level values are not required to identify the printed ordering but would be required to reconstruct intended replacement values.
- **Assumption and duplicate audit:** possible digit error, rounding source, or nonstandard convention is correctly separated as inference. This is not duplicated by any other C ID.
- **Card and impact audit:** ledger and recheck fields are supportable. The numeric-checker relevance wording was repaired during this audit to a conditional, bounded later-extraction risk. The final card must not claim a changed baseline comparison or downstream use.

## C002 — Primary risk difference has opposite signs in matched main-article locations

- **State and category:** Pending Human Adjudication; `Cross-document numeric inconsistency`, whose scope expressly includes matched abstract, narrative, and table occurrences.
- **Evidence and pagination:** [DOC-001 PDF p. 1 abstract](../../../jama_cooper_2018_oi_180132.pdf#page=1), [p. 5 Results](../../../jama_cooper_2018_oi_180132.pdf#page=5), and [p. 7 Table 2](../../../jama_cooper_2018_oi_180132.pdf#page=7) exist and resolve. The abstract prints `+0.4%` while Results/Table 2 print `-0.4`, with the same counts and CI.
- **Reproducibility:** `(117/240 - 111/226) x 100 = -0.365044` percentage points, which rounds to `-0.4`. A reversed contrast could produce a positive point estimate, but its CI orientation would also need definition; the unchanged abstract CI does not fully reconcile that alternative.
- **Assumption and duplicate audit:** missing-minus-sign and reversed/absolute-contrast explanations remain explicitly inferential. No other C ID concerns this result/sign rule.
- **Card and impact audit:** all source-grounded inputs are present. The final card should bound reuse risk to an abstract-level extractor copying the printed sign if the candidate is confirmed, without asserting effect-direction or conclusion change.

## C003 — Intracranial-bleeding effect and P-value reporting conflicts with matched evidence

- **State and category:** Pending Human Adjudication; `Statistical reporting inconsistency`.
- **Evidence and pagination:** [DOC-001 PDF p. 7, Table 2](../../../jama_cooper_2018_oi_180132.pdf#page=7) and [DOC-003 PDF p. 10, eTable 6](../../../joi180132supp2_prod.pdf#page=10) exist and resolve. Both print `47/260` versus `37/240`; the main table prints RR `1.23 (0.43-3.5), P=.70`, while eTable 6 prints `P=.43`.
- **Reproducibility:** `(47/260)/(37/240) = 1.172557`, rounding to `1.17`, not `1.23`. The direct same-row P-value disagreement requires no reconstructed test. The diagnostic log-scale interval/P calculation is labelled as diagnostic and does not replace the reported analysis.
- **Assumption and duplicate audit:** possible row transposition is correctly inferential. C003 and C004 must remain separate because they concern different named outcomes, printed rows, count pairs, and row-specific assignments, even though one production event may explain both.
- **Card and impact audit:** no missing evidence-card input or unsupported conclusion claim was found. Downstream wording must remain conditional and limited to a reviewer or extractor assigning the wrong RR/CI/P to this named outcome if confirmed.

## C004 — Extracranial-bleeding effect and P-value reporting conflicts with matched evidence

- **State and category:** Pending Human Adjudication; `Statistical reporting inconsistency`.
- **Evidence and pagination:** [DOC-001 PDF p. 7, Table 2](../../../jama_cooper_2018_oi_180132.pdf#page=7) and [DOC-003 PDF p. 10, eTable 6](../../../joi180132supp2_prod.pdf#page=10) exist and resolve. Both print `8/260` versus `6/240`; the main table prints RR `1.17 (0.79-1.74), P=.43`, while eTable 6 prints `P=.70`.
- **Reproducibility:** `(8/260)/(6/240) = 1.230769`, rounding to `1.23`, not `1.17`. The cross-source P disagreement is direct; the count-based CI/P results are appropriately diagnostic.
- **Assumption and duplicate audit:** possible row transposition is not asserted as a correction. This ID is not mergeable with C003 after stable assignment and also concerns a distinct printed relationship under the pre-ID duplicate rule.
- **Card and impact audit:** no missing evidence-card input or unbounded conclusion claim was found. The final card must describe only conditional misassignment of this named outcome's RR/CI/P in later extraction.

## C005 — As-treated evacuated-mass-lesion cell reverses count and percentage order

- **State and category:** Pending Human Adjudication; `Measure, label, or scale inconsistency`.
- **Evidence and pagination:** [DOC-003 PDF p. 18, eTable 10](../../../joi180132supp2_prod.pdf#page=18) exists and resolves. Under `No. (%)` and normothermia `n=196`, the cell prints `34.7 (68)`.
- **Reproducibility:** `68/196 x 100 = 34.693878%`, rounding to `34.7%`; the first displayed token is noninteger in a count position. The coherent reverse reading is diagnostic, not a prescribed correction.
- **Assumption and duplicate audit:** a row-specific percentage-first convention is not supported by the header or surrounding cells. C005 is distinct from C006 because it audits a different row and token pair.
- **Card and impact audit:** the numeric-checker relevance wording was repaired during this audit to a conditional mechanical-extraction risk. The final card must not claim actual extraction, propagation, or magnitude of downstream harm.

## C006 — As-treated non-evacuated-mass-lesion cell reverses count and percentage order

- **State and category:** Pending Human Adjudication; `Measure, label, or scale inconsistency`.
- **Evidence and pagination:** [DOC-003 PDF p. 18, eTable 10](../../../joi180132supp2_prod.pdf#page=18) exists and resolves. Under `No. (%)` and normothermia `n=196`, the cell prints `1 (2)`.
- **Reproducibility:** literal count-first reading gives `1/196 x 100 = 0.510204%`, not `2%`; reversing the tokens gives `2/196 x 100 = 1.020408%`, rounding to `1%`. Together with the other four CT counts, `3+108+15+68+2=196`.
- **Assumption and duplicate audit:** a denominator of 50 is only a hypothetical reconciliation and is correctly identified as unsupported by the displayed `n=196` and absent row-specific denominator. C006 remains distinct from C005 because it is a separate row, pair, percentage check, and total contribution.
- **Card and impact audit:** no missing evidence-card input was found. The final card should identify only the conditional risk of copying `1` as the count and `2%` as the percentage if confirmed.

## C007 — Adjusted odds-ratio confidence-interval string is malformed

- **State and category:** Pending Human Adjudication; `Statistical reporting inconsistency`.
- **Evidence and pagination:** [DOC-003 PDF p. 22, post-hoc Results](../../../joi180132supp2_prod.pdf#page=22) exists and resolves. Native text, layout text, and the rendered page all show `0.95 (0.55-275 1.64) P = .84`.
- **Reproducibility:** the parenthesis contains three numeric tokens and no source-defined delimiter or role for `275`, so it cannot be parsed as exactly two unambiguous ordered CI endpoints. The possible `0.55-1.64` reading is explicitly conjectural because coefficient, SE/covariance, and model output are not supplied.
- **Assumption and duplicate audit:** no unsupported deletion of `275` or reconstruction of endpoints is made. This is a distinct malformed-string relationship, not duplicated by another C ID.
- **Card and impact audit:** the upstream SN032 transcription defect was repaired during this audit and now preserves the source string. The final card must limit downstream risk to possible ambiguous CI extraction if confirmed and must not supply a final interval.

## C008 — Abstract male count conflicts with its percentage and Table 1 total

- **State and category:** Pending Human Adjudication; `Denominator, proportion, or total inconsistency`.
- **Evidence and pagination:** [DOC-001 PDF p. 1 abstract](../../../jama_cooper_2018_oi_180132.pdf#page=1) and [p. 5 Table 1](../../../jama_cooper_2018_oi_180132.pdf#page=5) exist and resolve. The abstract prints 500 participants, `402 men (80.2%)`; Table 1 prints `207+194=401` men among `260+240=500` participants.
- **Reproducibility:** `402/500 x 100 = 80.4%`, while `401/500 x 100 = 80.2%`; Table 1 sex counts close as `207+194+53+46=500`.
- **Assumption and duplicate audit:** a different denominator is only hypothetical and is not supplied. A typographical count explanation is not asserted as a correction. No other C ID addresses this cohort-characteristic identity.
- **Card and impact audit:** numeric-checker wording was repaired during this audit to a conditional abstract-only extraction risk. The final card must not claim actual propagation or a paper-level conclusion change.

## Repairs completed and remaining completion gates

Completed through the coordinator during this audit:

- SN032 now transcribes the malformed adjusted-OR interval exactly and separates conjecture from source evidence.
- Numeric-checker relevance statements associated with C001, C005, and C008 now use conditional, bounded extraction/reuse wording.
- The report-generation coverage scope now explicitly enumerates C001-C008.

No candidate was deleted, merged, renumbered, ranked, or suppressed. No new candidate was added. No arithmetic, pagination, source-link, category, candidate-provenance, or stable-ID defect remains in the ledger/recheck after those repairs.

Remaining workflow gates are procedural and downstream of this audit: mark the evidence-quality coverage row complete; generate the full report with all eight cards and exact blank adjudication placeholders; add the report generator and any later repair agents to the execution manifest and token ledger; check identical C-ID heading sets across ledger, recheck, quality audit, and report; verify every report evidence link; then finalize timing/token accounting, render HTML, recompute hashes, and run the validator.

## Limitations

The supplied package lacks participant-level data, unrounded summaries, complete model coefficients/SEs/covariances, some exact test variants, and embedded text for externally referenced SAP/update/correction material. These absences prevent reconstruction of intended replacement values or exact model output but do not prevent the printed-value comparisons above. The final Markdown report and standalone HTML did not yet exist at this required pre-report audit stage, so their card-label, placeholder, link, heading-set, and rendering checks remain mandatory after assembly.
