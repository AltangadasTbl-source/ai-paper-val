# Evidence-Quality Audit — Workflow 1.5.1

## Audit scope and overall result

This audit covers the complete current-run source coverage and coverage manifests, canonical main and support quantitative extractions, numeric relationships N001-N088, statistical relationships S001-S041, numeric and cross-source checker outputs, both statistical passes, the stable candidate ledger, the mechanical evidence recheck, the limitations record, and the agent-execution manifest. Supplied package sources were the only scientific authority. No legacy candidate, queue, checker, quality, or report artifact and no external source was used.

- Direct-source coverage closes at 134/134 PDF pages: DOC-001 9/9, DOC-002 109/109, and DOC-003 16/16. For each source, reusable units plus fresh-required units equal total units and mapped units equal total units: `9+0=9`, `0+109=109`, and `14+2=16`.
- The disjoint mapping shards cover DOC-001 pp. 1-9, DOC-002 pp. 1-109, and DOC-003 pp. 1-16 without an unassigned page. Canonical extractions preserve page-by-page coverage, including pages with no applicable quantitative relationship.
- Numeric relationship coverage is 88/88, and the numeric checker returns one explicit row for every N001-N088 relationship.
- Statistical relationship coverage is 41/41 in each pass. The execution manifest records distinct fresh agents `/root/statistical_pass_1` and `/root/statistical_pass_2`, both `gpt-5.6-terra`, `high`, `FRESH_SPAWN`; both checker artifacts explicitly cover every S001-S041 relationship.
- Ledger and recheck ID sets are identical at 13/13 (`C001`-`C013`). This audit returns every one of those IDs below. Every stable ID remains **Pending Human Adjudication**.
- The coverage manifest has exactly one plain relative artifact path in every current row. Its completed source, mapping, checker, registration, recheck, and statistical scopes resolve to existing artifacts. The evidence-quality row becomes complete when this file is accepted; the report row remains planned.
- Discovery was not controlled by a top-N boundary or an old candidate list. The current-run maps cover every direct-source page, the checkers cover all 88 numeric and all 41 statistical relationships, and the current artifacts explicitly state that legacy candidate/checker/report records were not scientific inputs.
- No stable ID is based on `P=0`, `p=.000`, or equivalent. S014 is explicitly `DISPLAY_ZERO_NOT_CANDIDATE`; the `<.001` entries in S041/N088 are threshold displays. No candidate card requires the conditional display-zero field.

## Repairs required before report assembly

1. In `candidate_ledger.md`, correct the remaining stale prose locators: C007 `p.46` to `p.48`; C010 repeated `p.82` to `p.83`; and C013 `p.51` to `p.53`. The ledger's primary exact-location lines are already corrected, but the source-evidence sentences must match them.
2. In C003, replace the stated 28-day minimum `352` with `344`: `2×28×4 + 2×28×2 + 8×1 = 344`. The 30-day minimum `368` is correct.
3. Give C002 exactly one normative category, preferably `Cross-document numeric inconsistency`, and C013 exactly one normative category, `Cross-document numeric inconsistency`. Slash-joined categories do not satisfy the one-primary-category rule. Retain secondary aspects in the reasoning, not the category field.
4. For C001, do not state that `42` is statistically incompatible with RR `2.8`. It is unusual and differs markedly from adjacent intervals, but S006 confirms that the interval is ordered, contains the estimate, and lacks a matched same-result comparator or supplied model rule. Frame the card as a transcription/interval-field quality-control observation whose intended endpoint requires source-model confirmation.
5. For C010, preserve the printed approximation sign and the source-grounded `27×40=1080` alternative. State the observable issue as an undocumented transition between `704×1.50=1056` and the cluster-rounded recruitment target, plus the potentially unclear “effective sample size” label; do not call `≈1080` a strict equality failure.
6. For C011, make the calculation explicitly conditional on ordinary unit-spaced 1-to-5 coding. A “5-point scale” alone does not supply response anchors or weights. The source-grounded issue is that the stated five-domain, five-point description does not explain the printed 5-35 total range.
7. Retain C012's conditional denominator language. eTable 6 does not print its denominator; 40 is a matched same-site recruitment/ITT comparator from eTable 5, not a directly stated eTable 6 denominator. Do not prescribe `5 (12.5%)` or `3 (7.5%)` as a correction.
8. If checker artifacts are cited as provenance in the final report, use the mechanical recheck's corrected pages. Stale checker locators are: numeric NC005 p.51→p.53, NC006 p.53→p.55, NC007 p.46/pp.49-50→p.48/pp.51-52, NC010 p.82→pp.63 and 83, NC011 p.84→p.85; cross-source XC002 p.46/pp.49-50→p.48/pp.51-52, XC003 p.51→p.53, XC004 p.53→p.55, and XC008 p.84→p.85.
9. In `coverage_manifest.md`, enumerate `C001,C002,C003,C004,C005,C006,C007,C008,C009,C010,C011,C012,C013` in the report-generation scope rather than “Complete stable candidate set.” After acceptance of this audit and report assembly, change the evidence-quality and report-generation statuses to `COMPLETE` at their actual completion times.
10. In the final report, every PDF evidence link must use the complete filename and end in `#page=N`. Every candidate card must include the exact human-adjudication template shown at the end of this audit; each subfield value must be exactly `__`.

## C001 — Adjusted self-reported abstinence interval endpoint printed as 42

- **Status:** Pending Human Adjudication.
- **Evidence and locator:** DOC-001 Table 2, `jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6`, directly prints adjusted RR `2.8 (1.9 to 42)` and same-row crude RR `2.7 (1.8 to 4.1)`.
- **Reproducibility:** `42/2.8=15.0` and `1.9/2.8=0.6786`; the printed endpoint and unusual asymmetry are reproducible observations. The interval remains ordered and contains 2.8.
- **Evidence-quality boundary:** The same-row crude interval and neighboring adjusted intervals are not a matched model-derived comparator. No coefficient, SE, covariance, or interval-construction output is supplied. Thus a decimal-placement explanation is inference only.
- **Required reporting repair:** Replace “incompatible” wording with a neutral statement that the printed endpoint is unusually large relative to its companion endpoint and adjacent intervals and requires confirmation against model output. Do not claim `4.2` is the correction.
- **Category and relevance:** `Numeric or arithmetic inconsistency` may be retained as the single category only if the card makes clear that the unresolved field is a transcription-quality observation, not a reconstructed statistical contradiction. Downstream impact is properly bounded to possible copying of the interval if confirmed.

## C002 — Discussion labels the all-cause death percentage as TB deaths

- **Status:** Pending Human Adjudication.
- **Evidence and locators:** DOC-001 pp. 5, 6, and 8 and DOC-003 p. 6. The discussion prints `4.8%` “died of TB”; the trial has `25+27=52` deaths among 1,080 participants, while TB is the classified cause for `32/52` deaths.
- **Reproducibility:** `52/1080×100=4.81%`, which rounds to 4.8%; `32/1080×100=2.96%`, which rounds to 3.0%.
- **Evidence-quality boundary:** The observation supports a cause-label mismatch. The possibility that “of TB” was contextual wording remains source-grounded and should stay in the card.
- **Required reporting repair:** Use exactly one category: `Cross-document numeric inconsistency`. Keep the all-cause versus TB-cause distinction in the evidence and reasoning.
- **Relevance:** The current conditional statement about a data extractor misclassifying the mortality outcome is bounded and does not assert paper-level conclusion change.

## C003 — 178-message total conflicts with its printed frequency schedule

- **Status:** Pending Human Adjudication.
- **Evidence and locator:** DOC-002 `joi250093supp1_prod_1768590553.08963.pdf#page=16` prints 178 SMS over six months, with two months at 4-5/day, two months at 2-3/day, and two months at 1-2/week.
- **Reproducibility:** A conservative minimum is `2×28×4 + 2×28×2 + 8×1 = 344`, which is 166 above 178. With 30-day months it is 368.
- **Evidence-quality boundary:** Whether “message” means a send, a unique template, or another unit is not defined; exact dates and any excluded days are absent. These limits do not reconcile the stated same-passage total and minimum schedule as written.
- **Required reporting repair:** Correct the ledger's 28-day arithmetic from 352 to 344 and retain the missing-unit/version explanation as inference.
- **Duplicate review:** This is a within-passage schedule-versus-total relationship. C013 is a different cross-location version/dose relationship; the two are not genuine duplicates.

## C004 — Repeated 2,384-participant plan names 44 and 48 facilities

- **Status:** Pending Human Adjudication.
- **Evidence and locators:** DOC-002 pp. 10 and 26 repeat the 2,384-participant plan and its surrounding assumptions while printing 44 facilities and 48 clinics, respectively.
- **Reproducibility:** `2384/44=54.18`; `2384/48=49.67`. The four-site difference is not display rounding, and only the second quotient closely reproduces “approximately 50.”
- **Evidence-quality boundary:** Facility/clinic definitions and amendment chronology are absent. An unlabelled site-type or version distinction remains possible.
- **Required reporting repair:** None beyond preserving direct-observation/inference separation and using the corrected full PDF links.
- **Duplicate review:** C007 concerns a distinct 2,716-participant plan and a different 48-versus-63 relationship.

## C005 — 134-message total conflicts with its printed frequency schedule

- **Status:** Pending Human Adjudication.
- **Evidence and locator:** The statement is on DOC-002 `joi250093supp1_prod_1768590553.08963.pdf#page=53`, not p. 51. It prints 134 SMS over six months with two months at 4-5/day, two months at 1-2/day, and two months at 1/week.
- **Reproducibility:** `2×28×4 + 2×28×1 + 8×1 = 288`, already 154 above 134; the 30-day calculation gives 308.
- **Evidence-quality boundary:** Unique-template versus send units and plan version are not defined. Page 80 supplies a different 134-message schedule that can accommodate the total but does not label page 53 as another plan state.
- **Required reporting repair:** Use p. 53 consistently and do not carry forward NC005's stale p. 51 locator.
- **Duplicate review:** This within-passage arithmetic relationship is distinct from C003's 178-message passage and C013's cross-location total/version relationship.

## C006 — TAM sampling header conflicts with contemporaneous narrative and equations

- **Status:** Pending Human Adjudication.
- **Evidence and locator:** DOC-002 `joi250093supp1_prod_1768590553.08963.pdf#page=55` prints a 30% header, a 20% Phase-3 narrative, `10×40×20%=80`, `8×40×20%=64`, and all-participant Phase-4 calculations `11×45=495` and `7×45=315`.
- **Reproducibility:** `80+64=144`, or 20% of 720; `495+315=810`, or all Phase-4 intervention participants. Neither is the unqualified 30% header.
- **Evidence-quality boundary:** A separate pooled or earlier 30% target is possible but not defined in the supplied page.
- **Required reporting repair:** Use p. 55 consistently and retain `Measure, label, or scale inconsistency` as the single category.
- **Relevance:** The downstream statement should remain conditional and limited to extraction of the TAM sampling denominator.

## C007 — Later 2,716-participant plan gives 48 clinics versus a 63-site diagram

- **Status:** Pending Human Adjudication.
- **Evidence and locators:** DOC-002 p. 48 prints 2,716 participants, approximately 43 recruits, and 63 facilities; pp. 51-52 show 27+36=63 sites and 1,096+1,620=2,716; p. 62 prints 2,716, approximately 50, and 48 clinics.
- **Reproducibility:** `2716/63=43.11`, while `2716/48=56.58`; the site counts differ by 15.
- **Evidence-quality boundary:** A distinct 48-clinic subset or an earlier unlabelled plan is possible but not supplied.
- **Required reporting repair:** Change the ledger source-evidence sentence from p. 46 to p. 48. Do not use the stale checker pages 46 and 49-50; use p. 48 and pp. 51-52.
- **Duplicate review:** This relationship is distinct from C004 because the total, site counts, and plan state differ.

## C008 — Phase-4 design-effect equality does not reproduce from printed inputs

- **Status:** Pending Human Adjudication.
- **Evidence and locator:** DOC-002 `joi250093supp1_prod_1768590553.08963.pdf#page=64` prints `1036×1.56=1620` and a 36-site, 45-per-site diagram total of 1,620.
- **Reproducibility:** `864×1.2=1036.8`; `1036/36=28.7778`; `1+0.02×(29−1)=1.56`; `1036×1.56=1616.16`; `36×45=1620`.
- **Evidence-quality boundary:** The direct issue is the displayed equality. A cluster-level ceiling/allocation step can explain the four-person difference, but the source does not state that step.
- **Required reporting repair:** Preserve the cluster-target alternative and avoid implying that 1,620 is impossible; it is exactly reproducible as `36×45`.
- **Duplicate review:** C010 is the analogous Phase-3 relationship but has different operands, an approximation sign, and an additional terminology issue, so it is not the same printed relationship.

## C009 — Phase-4 diagram is labelled Phase 3/Superiority

- **Status:** Pending Human Adjudication.
- **Evidence and locator:** DOC-002 p. 64 places a diagram labelled `Phase 3 (Superiority trial)` inside a Phase-4 non-inferiority section; the diagram's 36 sites and 1,620 participants match the local Phase-4 plan.
- **Reproducibility:** `18+18=36` and `36×45=1620`; the separate Phase-3 plan uses 27 sites and 1,080 participants.
- **Evidence-quality boundary:** The categorical label conflict is directly observed. “Carry-over caption” is a plausible explanation, not an established production history.
- **Required reporting repair:** None beyond neutral wording and the exact p. 64 source link.
- **Relevance:** The conditional downstream statement is bounded to possible phase/objective misclassification.

## C010 — Phase-3 design-effect display gives unreproducible 1,080 effective sample size

- **Status:** Pending Human Adjudication.
- **Evidence and locators:** DOC-002 p. 63 prints `704×1.50≈1080` and 27 sites at 40 participants per site. The repeated summary is on p. 83, not p. 82.
- **Reproducibility:** `704×1.50=1056`; `1080/704=1.5341`; `27×40=1080`.
- **Evidence-quality boundary:** Because the source uses `≈` and independently supplies a cluster allocation that yields 1,080, the observation is not a strict false equality. The missing step is the rule that raises the design-effect-inflated target to 40 per site; the meaning of “effective sample size” is also not defined.
- **Required reporting repair:** Change the residual ledger reference p.82 to p.83. Phrase the candidate around the undocumented rounding/allocation transition and terminology, while preserving the source-grounded explanation that 1,080 is a cluster-rounded recruitment target.
- **Category and duplicate review:** `Statistical reporting inconsistency` is an appropriate single category. It remains distinct from C008's Phase-4 exact equality.

## C011 — MPSS score range conflicts with stated item scale

- **Status:** Pending Human Adjudication.
- **Evidence and locator:** The MPSS definition is on DOC-002 `joi250093supp1_prod_1768590553.08963.pdf#page=85`, not p. 84. It lists five domains, a 5-point scale, and a summed range of 5-35.
- **Reproducibility:** Under ordinary unit-spaced 1-to-5 coding, five items span `5×1=5` to `5×5=25`, not 35.
- **Evidence-quality boundary:** The source does not print response anchors, coding values, weights, subitems, or a transformation. Therefore the 5-25 calculation must remain conditional; the directly observed issue is that the stated description does not explain the printed range.
- **Required reporting repair:** Use p. 85 consistently and avoid asserting that every possible five-point coding must have a maximum of 25.
- **Relevance:** Potential downstream impact is properly bounded to coding/extraction of the scale range if the description is confirmed incomplete or mismatched.

## C012 — Site 2008 death count and percentage lack a compatible supplied denominator

- **Status:** Pending Human Adjudication.
- **Evidence and locators:** DOC-003 p. 9 eTable 6 prints site 2008 deaths `5 (7.5)` without a denominator; DOC-003 p. 8 eTable 5 prints a same-site recruitment/ITT denominator of 40.
- **Reproducibility:** Conditional on denominator 40, `5/40×100=12.5%`; conversely, `5/0.075=66.6667`, and no 66-67-person site population is supplied.
- **Evidence-quality boundary:** The denominator of 40 is a cross-table matched comparator, not an eTable 6 observation. The intended death denominator remains absent.
- **Required reporting repair:** Keep every calculation conditional and ask for the denominator. Do not name a replacement count, percentage, or denominator as the correction.
- **Category and relevance:** `Rate-versus-count inconsistency` is a permissible single category. The downstream statement is bounded to possible copying of a cluster count/proportion pair.

## C013 — Protocol message dose changes from 178 to 134 without supplied reconciliation

- **Status:** Pending Human Adjudication.
- **Evidence and locators:** DOC-002 p. 16 prints 178 messages; p. 53 and p. 80 print 134 with different schedules; pp. 101-109 contain a 1-134 log; DOC-001 p. 3 prints 134 unique messages as `100+30+4`.
- **Reproducibility:** `178−134=44` and `100+30+4=134`. The visible log begins at 1 and ends at 134.
- **Evidence-quality boundary:** An intervention amendment is plausible, but the supplied version-change material does not explicitly link or supersede the 178-message passage. The record must not assert which regimen participants actually received.
- **Required reporting repair:** Change the ledger source-evidence sentence from p. 51 to p. 53. Use exactly one category, `Cross-document numeric inconsistency`; discuss schedule/version labels in the reasoning.
- **Duplicate review:** C013 compares dose totals and version identity across locations. C003 and C005 test arithmetic within individual schedule passages, so all three remain separate stable relationships.

## ID, wording, and report-field controls

- Covered stable IDs: `C001,C002,C003,C004,C005,C006,C007,C008,C009,C010,C011,C012,C013`.
- No stable ID is deleted, merged, ranked, suppressed, renumbered, assigned severity, or given a scientific disposition. All remain **Pending Human Adjudication**.
- Direct observation and inference are separable for every ID after the repairs above. C001, C010, C011, and C012 especially require the stated evidentiary qualifications.
- Candidate relevance statements must remain conditional and limited to a value, label, denominator, interval, regimen, phase, or scale that a data extractor, review, meta-analysis, or protocol synthesis could copy if the candidate is confirmed. No card should state that downstream propagation or a paper-level conclusion change occurred.
- Every final-report card must use exactly this blank template:

```markdown
**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __
```

## Remaining limitations

The package lacks model output for C001; explicit message-unit and amendment crosswalks for C003, C005, and C013; facility/clinic definitions and plan chronology for C004 and C007; design-effect rounding/allocation conventions for C008 and C010; complete MPSS anchors and scoring rules for C011; and the eTable 6 death denominator for C012. DOC-002's native text layer is substitution-garbled, but all 109 pages were freshly rendered and visually mapped, so this is a derivative-quality limitation rather than an open scientific-coverage unit. Figure-only Bayesian values have no exact printed numeric endpoints and were appropriately not reconstructed.

## Audit counts

- Direct sources: 3/3 complete.
- Direct-source units: 134/134 mapped.
- Numeric relationships: 88/88 checked.
- Statistical relationships: 41/41 in pass 1 and 41/41 in pass 2.
- Stable candidates: 13/13 audited and returned.
- Candidate IDs requiring locator prose repair: 3 in the ledger (C007, C010, C013); five recheck-corrected ID families have stale locators in checker provenance (C005, C006, C007, C010, C011), with additional stale cross-source references for C013.
- Arithmetic text repairs: 1 (C003).
- Single-category repairs: 2 (C002, C013).
- Display-zero-only stable candidates: 0.
