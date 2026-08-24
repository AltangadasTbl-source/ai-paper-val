# Final Evidence-Quality Audit

This audit covers every fresh canonical source, evidence, extraction, relationship, checker, registration, and recheck artifact available before report generation. The stable set is C001, C002, C003, C004, C005, C006, C007, C008, and C009. All nine remain **Pending Human Adjudication**. This artifact records quality-control facts and coordinator repairs; it does not make a scientific disposition, assign importance, or prescribe a correction.

## Coverage and execution audit

- **Fresh-source boundary:** The three direct PDFs are the only evidence sources. The fresh inventory, preprocessing record, quantitative maps, and checker provenance state that no pre-existing audit derivative or external source was used. No canonical source citation points to an old audit output. Direct `sha256sum -c` verification against `source_hashes_before.sha256` returned `OK` for all three PDFs.
- **Direct-source coverage:** DOC-001 is 8 total, 0 reusable, 8 fresh-required, and 8 mapped PDF pages; DOC-002 is 29 total, 0 reusable, 29 fresh-required, and 29 mapped pages; DOC-003 is 10 total, 0 reusable, 10 fresh-required, and 10 mapped pages. Every row is `COMPLETE`. The package totals are 47 total, 0 reusable, 47 fresh-required, and 47 mapped units. Thus fresh-required units and mapped units equal total units for every direct source and for the package.
- **Evidence assets and pagination:** Fresh native and layout text cover all 47 pages. Forty-three result-relevant pages were freshly rendered; DOC-002 pp. 26-29 were freshly extracted and classified as reference-list continuation. Native/layout text was usable, so no OCR was required. Direct-PDF checks confirmed every candidate location: DOC-001 pp. 3-7, DOC-002 pp. 7 and 9, and DOC-003 p. 5. The recheck links resolve from its directory and end in the cited `#page=N`; no false candidate pagination was identified.
- **Complete relationship coverage:** The canonical numeric inventory contains 133 unique relationships: N001-N047, N200-N231, and N600-N653. The canonical numeric checker contains the identical 133-ID set. The canonical statistical inventory contains 58 unique relationships: S001-S031, S200-S215, and S400-S410. Each statistical pass contains the identical 58-ID set and an explicit completion record for every S ID. No top-N rule, target count, candidate cap, review queue, or early-stopping boundary controlled discovery.
- **Statistical execution provenance:** `agent_execution_manifest.md` records distinct fresh agents `/root/statistics_pass_1` and `/root/statistics_pass_2`, both `gpt-5.6-terra`, reasoning effort `high`, start mode `FRESH_SPAWN`, with one primary artifact each. Their IDs are distinct, and both passes cover all 58 S relationships. The manifest has 12 unique current execution rows including the coordinator and this quality auditor. A report-generator row will be required when that agent is spawned.
- **S407 boundary:** S407 directly prints HR 1.69, 95% CI 1.14-2.51, and P=.001. The Wald/log-HR calculation in NUM-B-001 and CROSS-002 is diagnostic only. The supplied package does not identify a common P test and CI construction, sidedness, coefficient precision, standard error, or variance estimator. Passes 1 and 2 therefore correctly keep S407 outside the stable C set. The report must not promote the provisional checker wording to a candidate.
- **Display-zero boundary:** No supplied inferential result displays `P = 0`, `P = 0.000`, or an equivalent P-value display zero. The two statistical passes record `DISPLAY_ZERO_NOT_CANDIDATE` count 0. Event cells such as `0 (0.0%)` are counts and percentages, not P values. No stable C ID has a display-zero P value as its basis, so the conditional independent-contradiction report field is not applicable to C001-C009.
- **Stable-ID equality:** The ledger and evidence recheck each contain exactly C001-C009 once. This audit contains the same nine IDs once. The report-ready set is therefore nine IDs, but the pending `report_generation` manifest row does not yet enumerate them and the final report does not yet exist.
- **Coverage-manifest path audit:** All 22 data rows contain exactly one undecorated relative artifact path. Every artifact for a row marked `COMPLETE` exists. This audit creates the listed evidence-quality artifact. The report artifact is appropriately absent while its row remains `PENDING`.
- **Coordinator repairs required:** In `coverage_manifest.md`, replace the generic `evidence_quality` exact scope with `C001, C002, C003, C004, C005, C006, C007, C008, C009` and mark the row `COMPLETE`. Replace the generic `report_generation` exact scope with the same explicit list, then mark it `COMPLETE` only after the report exists. Preserve the historical checker outputs, but treat NUM-B-001/CROSS-002 solely as the S407 diagnostic described above. Apply the C002 and C006 wording repairs specified below before report assembly.
- **Final-card assembly rule:** The ledger is a registration artifact, not the final-card schema. For every C ID, the report generator must create all exact report-spec labels: `Candidate statement`, `Category`, `Exact source locations`, `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Alternative source-grounded interpretations`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields`. The underlying ledger and recheck supply the evidence for these fields, but the exact final-card labels and stepwise human instructions are not yet assembled. Every card's adjudication block must be exactly:

```markdown
**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __
```

No current ledger or recheck section contains a human-adjudication subfield with a nonblank value; report generation remains responsible for inserting the exact `__` placeholders.

## C001 — Discontinuation-reason counts do not exhaust the stated 65 recipients stopping before 4 L

- **Status and source truth:** Pending Human Adjudication. DOC-001 p. 4 directly prints the 65-person group and reason counts 32, 9, 5, and 4. The cited page is correct.
- **Arithmetic and rule:** `32 + 9 + 5 + 4 = 50`, leaving `65 - 50 = 15`; the displayed percentages sum to 47.2%, consistent with 50 of 106. The complete-partition rule is conditional because the source does not say whether reasons are exhaustive or mutually exclusive.
- **Missing card fields and assumptions:** Assemble every exact final-card label listed in the coverage audit. The material needed for the evidence and recheck fields is present. The missing definitions are exhaustiveness, overlap, and any reason assignment for the residual 15; an omitted category or overlap is an explanation, not a direct observation.
- **Duplicate, impact, and wording audit:** No other stable ID applies the same printed values and partition rule. The current text does not claim paper-level conclusion change. Downstream wording must remain limited to the reason counts or intervention-process table that an extractor could copy if the issue is confirmed.
- **Coordinator repair:** No candidate-specific arithmetic or pagination repair is needed. Preserve the conditional wording and do not present the 15 as a proven omitted category.

## C002 — Usual-care fluid-bolus percentage does not reconcile with its printed count and arm denominator

- **Status and source truth:** Pending Human Adjudication. DOC-001 p. 4 directly prints 50 patients (48.3%); Figure 1 on p. 4 and Table 2 on p. 6 directly print the usual-care analysis denominator 103. Both cited pages are correct.
- **Arithmetic and rule:** `50 / 103 x 100 = 48.543689%`, ordinarily 48.5%, not 48.3%. The denominator assignment remains conditional because the process sentence does not print its denominator. Importantly, `50 / 104 x 100 = 48.076923%`, ordinarily 48.1%; an integer denominator of 104 does not reproduce 48.3%.
- **Missing card fields and assumptions:** Assemble every exact final-card label listed above. The missing inputs are the process-measure denominator, available-case definition, and rounding rule. Treat 103 as the adjacent displayed comparator, not as an expressly printed denominator for the sentence.
- **Duplicate, impact, and wording audit:** This is distinct from C005 because it concerns the usual-care bolus numerator/percentage, not 28-day follow-up completeness. No conclusion-impact claim appears. Bound downstream wording to possible copying of the bolus count, percent, or denominator.
- **Coordinator repair:** Replace the ledger alternative `50/0.483≈104` as a potentially explanatory available-case denominator. State instead that the exact back-calculation is nonintegral and neither 103 nor 104 produces 48.3% under ordinary nearest-tenth rounding; retain an unspecified denominator or calculation rule as the unresolved possibility.

## C003 — Usual-care lactate-change IQR differs between narrative and Table 2 and is nonascending in the narrative

- **Status and source truth:** Pending Human Adjudication. DOC-001 p. 4 directly prints median -0.5 with IQR 2.2 to 1.1; Table 2 on p. 6 directly prints -0.5 (-2.2 to 1.1). The pagination and matched baseline-to-6-hour label are correct.
- **Arithmetic and rule:** The p. 4 lower endpoint exceeds its upper endpoint because `2.2 > 1.1`, and the lower endpoint differs in sign across the two displays. No arithmetic defect was found in the candidate record.
- **Missing card fields and assumptions:** Assemble every exact final-card label listed above. Raw observations and the intended lower endpoint are missing. A dropped minus sign is plausible but inferred; a different unlabelled subset is also only an alternative and has no printed support.
- **Duplicate, impact, and wording audit:** C003 is the sole stable ID for this sign/order relationship; S020 is a related statistical relationship, not a duplicate candidate. The statement that the lower-tail direction differs is bounded to the display. Do not claim an outcome or paper-level conclusion change.
- **Coordinator repair:** No candidate-specific evidence repair is required; the report must present `-2.2` as the comparator, not as an established correction.

## C004 — Respiratory-compromise oxygen-saturation threshold is labelled inconsistently

- **Status and source truth:** Pending Human Adjudication. DOC-001 p. 3 prints `>=3%`, p. 4 prints `3% or greater`, and Table 2 on p. 6 prints `>=3%` while footnote b prints `more than 3%`. All cited locations are correct.
- **Arithmetic and rule:** The threshold sets differ only at exactly 3 percentage points: `>=3%` includes the boundary and `>3%` excludes it. The logical comparison is reproducible.
- **Missing card fields and assumptions:** Assemble every exact final-card label listed above. The operational coding rule and participant-level saturation changes are missing. Whether any count changes at the boundary is unknown and must remain an inference.
- **Duplicate, impact, and wording audit:** S021-S023 are affected relationships but not duplicate stable candidates. The current record does not overstate conclusion impact. Bound downstream wording to the threshold definition or respiratory-compromise count a reviewer might extract or attempt to reproduce.
- **Coordinator repair:** No source or calculation repair is needed. Keep the count impact explicitly unknown.

## C005 — Figure 2's 94.2% vital-status percentage does not reconcile with the displayed modified-ITT/28-day counts

- **Status and source truth:** Pending Human Adjudication. Figure 2 on DOC-001 p. 6 directly prints only `194 patients (94.2%)`; its caption does not print a denominator. Figure 1 on p. 4 prints 106 and 103 in the primary analysis, 9 and 6 lost after discharge, and 97 and 97 in the 28-day analysis. Both pages are correct.
- **Arithmetic and rule:** `106 + 103 = 209`, `9 + 6 = 15`, `97 + 97 = 194`, and `209 - 15 = 194`. Against the displayed cohort, `194 / 209 x 100 = 92.822967%`, ordinarily 92.8%. `194 / 206 x 100 = 94.174757%`, ordinarily 94.2%, but 206 is only a back-calculated, inferred denominator and is not printed anywhere for the caption.
- **Missing card fields and assumptions:** Assemble every exact final-card label listed above. The caption's denominator and any population rule that could define 206 are missing. Neither a 206-person eligible subset nor a three-person exclusion is a direct source fact.
- **Duplicate, impact, and wording audit:** C005 is distinct from C007: it addresses the percentage with known vital status, whereas C007 addresses an arm-specific mortality percentage. S003, S006, and S410 are cross-references, not duplicate candidates. No paper-level conclusion effect is supported. Bound downstream wording to follow-up-completeness extraction.
- **Coordinator repair:** In the report, state first that the caption supplies no denominator. Label 209 as derived from displayed arm counts and 206 solely as the denominator implied by ordinary one-decimal back-calculation. Do not state or imply that the source reports 206 or documents three excluded participants.

## C006 — Protocol Table 2 column headers and row percentages use incompatible denominators

- **Status and source truth:** Pending Human Adjudication. DOC-002 p. 9 directly prints Total n=76, SSSP n=36, Control n=44 and the cited count/whole-percent cells. The page is correct.
- **Arithmetic and rule:** `36 + 44 = 80`, not 76. Using 44 gives 70.5%, 61.4%, 31.8%, 29.5%, 29.5%, and 38.6% for the cited control counts, not the printed values. Using 40 gives 77.5%, 67.5%, 35.0%, 32.5%, 32.5%, and 42.5%, each within 0.5 point of its display and also gives `36 + 40 = 76`. However, no single ordinary half-up or half-even tie rule maps every .5 value to the mix of printed 78, 68, 33, 33, and 42. Thus 40 is diagnostic, not an established common denominator/rounding solution.
- **Missing card fields and assumptions:** Assemble every exact final-card label listed above. The intended table population, row-specific denominators, and rounding convention are missing. A control denominator of 40 and a mixed-version production explanation are inferred.
- **Duplicate, impact, and wording audit:** The numeric, statistical-pass-1, and cross-source provisional records concern the same headers, cells, and denominator rule and were correctly consolidated as C006 before stable IDs. No later stable candidate duplicates it. The current impact is bounded to reuse of the preliminary baseline table and does not assert a final-trial conclusion effect.
- **Coordinator repair:** Replace any statement that denominator 40 simply reproduces all percentages “after rounding” with the precise ±0.5-point diagnostic and the unresolved tie-rule limitation. Preserve the exact 76-versus-80 header contradiction as the direct core.

## C007 — Printed 28-day usual-care mortality percentage does not round from the displayed follow-up and total-death counts

- **Status and source truth:** Pending Human Adjudication. DOC-001 pp. 4-5 directly print 97 participants per arm and mortality percentages 67.0% and 45.3%; DOC-003 p. 5 directly prints 109 deaths among 194 with 28-day follow-up. The pagination is correct.
- **Arithmetic and rule:** Under ordinary nearest-tenth rounding, 67.0% of 97 uniquely implies 65 deaths; `109 - 65 = 44`, and `44 / 97 x 100 = 45.360825%`, ordinarily 45.4%, not 45.3%. The 65 and 44 arm counts are derived rather than printed.
- **Missing card fields and assumptions:** Assemble every exact final-card label listed above. Missing are direct arm death counts, an explicit identity statement tying the DOC-003 total to the same arm analysis, and the source's rounding/truncation rule. The candidate must remain conditional on those definitions.
- **Duplicate, impact, and wording audit:** C007 is not a duplicate of C005 because its comparator, rule, and reported quantity differ. S003/S410 provide relationship context. Do not claim that the small display difference changes the secondary-outcome conclusion; bound downstream wording to the arm mortality percentage or derived count an extractor could record.
- **Coordinator repair:** No arithmetic repair is needed. Keep 65 and 44 explicitly labelled as derived under ordinary rounding and state truncation as an unresolved alternative.

## C008 — HIV-negative subgroup risk ratio does not reconcile with its printed deaths and denominators

- **Status and source truth:** Pending Human Adjudication. DOC-001 p. 7 directly prints 9/9 subgroup denominators, deaths 3 (33.3%) and 5 (55.6%), and RR 0.75 (95% CI 0.23-2.44). The cited page and row are correct.
- **Arithmetic and rule:** The crude displayed-count ratio is `(3 / 9) / (5 / 9) = 0.60`, not 0.75. The component percentages reconcile, and 0.75 lies within the ordered printed CI. The discrepancy is point estimate versus crude displayed counts, not interval order or direction.
- **Missing card fields and assumptions:** Assemble every exact final-card label listed above. The exact row estimator, adjustment/weighting, analysis population identity, CI construction, and test definition are missing. Applying the crude rule is conditional because the figure does not state whether the row RR is non-crude.
- **Duplicate, impact, and wording audit:** Numeric and statistical pass-1 records used the same row and rule and were correctly consolidated as C008 before stable IDs. No other stable ID duplicates it. Bound downstream wording to the subgroup RR/counts that could be extracted; do not assert a subgroup or paper-level conclusion change.
- **Coordinator repair:** No source or arithmetic repair is required. Ensure the report does not describe 0.60 as the intended corrected RR.

## C009 — Protocol background culture-yield percentage does not round from its printed count and denominator

- **Status and source truth:** Pending Human Adjudication. DOC-002 p. 7 directly prints 36 (22.3%) of 161 septic patients after excluding probable contaminants. The cited page is correct.
- **Arithmetic and rule:** `36 / 161 x 100 = 22.360248%`, ordinarily 22.4% to one decimal, not 22.3%. The difference depends on the unreported rounding convention; truncation would explain the display.
- **Missing card fields and assumptions:** Assemble every exact final-card label listed above. The rounding convention and any alternative denominator are missing. Truncation, transcription, or a different denominator are alternatives rather than direct facts.
- **Duplicate, impact, and wording audit:** S213 is a context relationship, not a duplicate candidate. C009 is distinct from the trial-result candidates because it concerns a protocol background value. No conclusion-impact claim is supported. Bound downstream wording to the culture-yield count/percentage a data extractor could copy.
- **Coordinator repair:** No arithmetic or pagination repair is needed. Preserve the background/context label and the conditional rounding language.

## Limitations and coordinator handoff

The supplied package has no raw observations, analysis code, directly printed arm death counts for 28-day mortality, row-specific model coefficients or standard errors, Cox P-test/CI construction definitions, or universal rounding convention. These omissions limit mechanism identification but do not justify removing or combining any stable ID. The final report must return all nine IDs, preserve the candidate-specific inference boundaries above, use neutral quality-control language, avoid paper-level conclusion claims, and keep every adjudication subfield exactly `__`.
