# Statistical consistency review — pass 1

## Completion record

- **Runtime agent ID:** `/root/statistics_pass_1`
- **Configured role/model/effort:** fresh `statistics_pass_1`; `gpt-5.6-terra`; `high`.
- **Scope:** every package-wide inferential/statistical relationship and supplied inferential definition in `statistics/relationship_inventory.md`: S001-S036, covering DOC-001 pp. 1-11, DOC-002 pp. 1-103, DOC-003 pp. 1-26, and no-applicable inferential content in DOC-004 pp. 1-3 and DOC-005 p. 1.
- **Relationship count:** 36 package-wide S records, all explicitly `PASS_1_COMPLETE`.
- **Candidate-observation count:** 3 distinct observations, without `C` IDs; no count suppression.
- **Evidence boundary:** direct supplied PDFs are authoritative. Main/support mapping artifacts were locators and transcription aids. Candidate locations S018-A, S019-A, and S026-A were independently checked in the direct PDFs.

## Checks applied to the complete relationship set

| Check | S-record coverage | Result |
|---|---|---|
| Point-estimate containment and ordered endpoints | S003-S015, S016-S028 | All printed estimates lie inside correctly ordered reported CIs. |
| Sign/direction against event percentages, labels, and narrative | S003-S028 | Compatible except the independently reported percentage observations S018-A and S019-A; their OR direction is not at issue. |
| Effect measure, scale, and outcome-time labels | S001-S035 | ORs, mean differences, CIs, event counts/proportions, sensitivity scenarios, and rate-versus-person-time distinctions mapped. No rate/count label contradiction found in inferential output. |
| Cross-location repetition | S003-S005, S006-S010, S016-S021, S022-S028 | Main/supplement matched where population, time, contrast, and model permits. S018-A and S019-A are direct cross-location contradictions. The all-patient adjusted CIs 0.68-1.41 and 0.68-1.39 are not called a contradiction because eTable 7 does not supply sufficient adjusted-model definition. |
| Interval/P-value/test/statistic/SE compatibility | S003-S015, S022-S028 | Where two-sided 95%-CI and model definitions were supplied, diagnostic normal/log-scale checks agree with displayed P values to printed precision. IPW/GEE/row-level adjustment prevents treating diagnostics as reproductions. No SE or test statistic is printed for a direct SE/statistic check. |
| Interaction P values | S016-S021 | Recorded, not recalculated: interaction statistic, df, term definition, and covariance/variance detail are absent. |
| Planning, methods, populations, missingness, multiplicity, and monitoring definitions | S001-S002, S029-S035 | Mapped and version-matched without assuming observed-result equality. Missing definitions stated per record. |
| Display-zero P-value rule | S036 | No inferential P-value display zero appears. Zeros in supplied materials are counts, percentages, coding values, or non-P display values. No P-value display-zero candidate or tail-probability derivation made. |

## Candidate observations

### S018-A — eTable 7 AIS <3 liberal percentage

- **Direct evidence:** `joi240147supp2_prod_1738701765.29201.pdf#page=20` prints `48/473 (9.2)`; matched `jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=8` Figure 4 prints `48/473 (10.1)`.
- **Rule:** 48/473 x 100 = 10.15%, which rounds to 10.1% at one decimal, not 9.2%.
- **Candidate observation:** the printed percentage does not reconcile with its supplied numerator/denominator and differs from the matched main-figure occurrence.
- **Remaining human question:** confirm publication-level transcription/typesetting and authoritative percentage.

### S019-A — eTable 7 known-lung-disease liberal percentage

- **Direct evidence:** `joi240147supp2_prod_1738701765.29201.pdf#page=20` prints `14/69 (20.2)`; matched `jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=8` Figure 4 prints `14/69 (20.3)`.
- **Rule:** 14/69 x 100 = 20.289...%, which rounds to 20.3% at one decimal, not 20.2%.
- **Candidate observation:** the printed percentage does not reconcile with its supplied numerator/denominator and differs from the matched main-figure occurrence.
- **Remaining human question:** confirm publication-level transcription/typesetting and authoritative percentage.

### S026-A — eTable 11 missing-as-event primary count notation

- **Direct evidence:** `joi240147supp2_prod_1738701765.29201.pdf#page=25` visibly prints `135//750 (18.0)` in a `no./total no. (%)` table.
- **Rule:** 135/750 is compatible with 18.0%; the candidate is the independently observable doubled separator, not an arithmetic or P-value inference.
- **Candidate observation:** the count/denominator notation is malformed relative to the printed table convention and the paired `155/758` cell.
- **Remaining human question:** confirm whether the double separator is present in the publication version and requires clarification for data extraction.

## Missing definitions and diagnostic limits

- No model convention was inferred where the source omits it. In particular, no interaction P-value was reconstructed without the interaction-model term, statistic, df, covariance, and variance details.
- The reported outcome models include GEE/IPW and adjustment columns. CI/P diagnostics are explicitly diagnostic approximations under supplied two-sided 95%-CI definitions, not reconstructed analyses; no raw covariance, IP weights, or row-level model matrix was supplied.
- The source does not supply a row-specific BH threshold or adjusted P value for exploratory outcomes. Unadjusted P values are not converted into an adjusted significance claim.
- The final subgroup table labels a column “adjusted odds ratio” but does not state enough covariate detail to equate its overall adjusted CI (0.68-1.39) to eTable 4’s adjusted CI (0.68-1.41); no candidate is emitted for that difference.
- Direct visual inspection determined that an apparent duplicated eTable 11 respiratory row in native text is an extraction artifact: it appears once in the PDF.

## Per-relationship pass-1 completion index

+- S001: PASS_1_COMPLETE
- S002: PASS_1_COMPLETE
- S003: PASS_1_COMPLETE
- S004: PASS_1_COMPLETE
- S005: PASS_1_COMPLETE
- S006: PASS_1_COMPLETE
- S007: PASS_1_COMPLETE
- S008: PASS_1_COMPLETE
- S009: PASS_1_COMPLETE
- S010: PASS_1_COMPLETE
- S011: PASS_1_COMPLETE
- S012: PASS_1_COMPLETE
- S013: PASS_1_COMPLETE
- S014: PASS_1_COMPLETE
- S015: PASS_1_COMPLETE
- S016: PASS_1_COMPLETE
- S017: PASS_1_COMPLETE
- S018: PASS_1_COMPLETE
- S019: PASS_1_COMPLETE
- S020: PASS_1_COMPLETE
- S021: PASS_1_COMPLETE
- S022: PASS_1_COMPLETE
- S023: PASS_1_COMPLETE
- S024: PASS_1_COMPLETE
- S025: PASS_1_COMPLETE
- S026: PASS_1_COMPLETE
- S027: PASS_1_COMPLETE
- S028: PASS_1_COMPLETE
- S029: PASS_1_COMPLETE
- S030: PASS_1_COMPLETE
- S031: PASS_1_COMPLETE
- S032: PASS_1_COMPLETE
- S033: PASS_1_COMPLETE
- S034: PASS_1_COMPLETE
- S035: PASS_1_COMPLETE
- S036: PASS_1_COMPLETE

## Handoff

Pass 2 must revisit S001-S036 against the complete cross-lane candidate ledger and mechanical evidence-recheck record, append any genuinely new candidate observations through the coordinator, and update every S record to `PASS_2_COMPLETE`. This pass assigns no `C` ID, severity, validity, acceptance, rejection, correction, or adjudication.
