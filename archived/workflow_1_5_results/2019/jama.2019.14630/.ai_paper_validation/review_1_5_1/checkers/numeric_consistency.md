# Numeric consistency checks

## Scope, evidence, and checking rule

Checked the 269 canonical N relationships in relationships/numeric_relationship_inventory.md, covering MAIN-N001-MAIN-N100 and SUP-N001-SUP-N013. Direct evidence was the five supplied PDFs; reusable or fresh page-preserving text was used only as a locator/transcription aid. No legacy candidate, checker, verifier, critic, or report conclusion was used.

For displayed counts, sums must match exactly. For percentages, the value must lie within the ordinary rounding interval implied by displayed precision. For a median (IQR), the median must be within the displayed lower and upper quartiles: Q1 ≤ median ≤ Q3. For model-derived adjusted contrasts, raw subtraction of rounded group summaries is not an identity; the source labels the contrasts as mixed-effects model outputs. P values printed as <.001 were checked for display coherence only; none is a display-zero record.

## Completed check matrix

| Check family | Relationships | Result |
|---|---:|---|
| Enrollment, exclusions, sex, analysis and completer-flow arithmetic | N001-N007, N011-N014 | 14 coherent identities; no candidate |
| Percentage and rounding checks | N002-N003, N011-N014, N083-N093, N251-N257 | 26 applicable checked; all printed count-based percentages coherent; figure denominators unavailable where stated |
| Missingness/population labels | N007, N010, N033, N147-N150, N186-N189, N225-N246 | 35 checked; no concrete mismatch |
| Scores, units, scales, direction and reference labels | N008, N015-N018, N020-N035, N041-N097, N121-N124, N151-N250, N258-N269 | 192 checked; one candidate at N146 |
| Table row arithmetic, interval order and repeated-value review | N025-N032, N036-N093, N125-N246 | 150 checked; all CIs correctly ordered; no unqualified raw-difference test applied to model estimates |
| Rate/risk/proportion/count distinction | N098, N083-N093, N251-N257 | 20 checked; no confusion identified |
| Cross-location repetitions with a matched population/time/analysis | N001-N005, N021-N032, N036-N040, N080, N095-N097 | 25 checked; coherent |
| No-applicable current-result units | DOC-002 except embedded historical plan, DOC-003 except Table 2, DOC-004 p.8, DOC-005 p.1 | Complete; no candidate |

The check-family counts overlap because a relationship can receive several checks. All 269 canonical relationships received an explicit coherent, no-applicable, or candidate record.

## Preliminary candidate register

### QC-N001 — eTable 2 intervention red-wine baseline median lies outside its printed IQR

- **Canonical relationship:** N146 / SUP-N003, distinct from the completer and baseline-value-carried-forward red-wine rows.
- **Category for later human review:** Numeric or arithmetic inconsistency; denominator, proportion, or total inconsistency is not alleged.
- **Exact source location:** DOC-004, joi190106supp3_prod_1635377898.49725.pdf, PDF p.7, Supplemental eTable 2 (continued), row “Red wine (g/week), Baseline, median (IQR)”, multiple-imputation all-randomized participants, intervention group N=3,272.
- **Printed inputs:** Intervention baseline red wine is printed as “33 (0, 29)”; control is “4 (0, 29)”. The table footnote says baseline data are median (IQR). The same row prints 6-month intervention/control changes 1 (-1 to 3) and 2 (0 to 4), difference -1 (-4 to 1), P=.36; and 12-month changes 2 (0 to 4) and 3 (1 to 5), difference -1 (-4 to 1), P=.37.
- **Direct observation:** The source directly prints a baseline intervention median of 33 g/week and IQR endpoints 0 and 29 g/week.
- **Reproducible rule and calculation:** For a quantity reported as median (Q1, Q3), Q1 ≤ median ≤ Q3. Here Q1=0, median=33, Q3=29; 0 ≤ 33 is true, but 33 ≤ 29 is false. The median exceeds the printed upper quartile by 4 g/week.
- **Tolerance:** Exact ordering is required; no ordinary decimal rounding tolerance can make 33 ≤ 29. The displayed values are integers, and even a half-unit display tolerance leaves the minimum gap 3 g/week.
- **Inference, separated from observation:** This may be a transcription/typographic error in the displayed median or upper IQR endpoint. That explanation is an inference, not a source fact.
- **Source-grounded alternatives:** (1) The printed median 33 may be intended as 3 or another value within 0-29; (2) the printed upper IQR endpoint 29 may be intended as a value at least 33; (3) the source may use a nonstandard parenthetical quantity despite the table footnote explicitly calling baseline data median (IQR). No alternative is selected here.
- **Quality-control relevance:** A data extractor could copy a baseline red-wine median that is internally impossible under the table’s stated summary convention, contaminating a baseline-description or sensitivity-analysis comparison.
- **Exact human question:** Does the source PDF faithfully reflect the authors’ intended intervention-group baseline red-wine median and IQR in eTable 2, and if so, what are the correct printed values or summary convention?
- **Preliminary status:** Pending Human Adjudication. This is a provisional checker key only; no stable C ID, severity, validity, or disposition is assigned.

## Coherent special cases and exclusions

- N003: 6583/6874=95.77%, so printed 96% is ordinary whole-percent rounding.
- N005-N007: all exclusion and follow-up/completer arithmetic reconciles exactly.
- N011-N014: sex and education totals reconcile; education denominators are explicitly lower than group N.
- N098: the stated six-fold contact ratio is exact, 18/3=6.
- N025-N032 and N041-N079: contrasts are explicitly model-derived, so small differences from subtraction of rounded group summaries are not candidates without a supplied identity rule.
- N147-N150: differing score-table denominators are explicitly footnoted as a distinct marked er-MedDiet analysis, not an unqualified mismatch.
- N251-N257: absent readable intervention bar labels/denominators are an evidence limitation, not a numeric inconsistency.
- No P=0, p=0.000, or equivalent display-zero relationship was found in the numeric scope; therefore no DISPLAY_ZERO_NOT_CANDIDATE record was needed.

## Limitations

The graphics on DOC-004 pp.25-27 do not print every plotted coordinate, and eFigure 2 does not yield reliable intervention percentage labels from the supplied visual/text evidence. Those relationships were checked only for what is printed. No raw-data, methodology, or external-literature audit was performed.

