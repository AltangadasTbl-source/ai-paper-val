# Evidence Recheck

This mechanical recheck covers every stable candidate ID in `candidate_ledger.md`: C001, C002, and C003. Each cited location was re-opened in the current supplied PDF. Native/layout text was extracted directly from the current PDF pages, and the table or figure pages containing the candidate values were freshly rendered from those PDFs for visual confirmation. Reusable or earlier extracted artifacts were not treated as evidentiary authority. Every candidate remains **Pending Human Adjudication**.

## C001 — Figure 3 all-patient rate-column conflict with the matched primary-outcome rate

**Status:** Pending Human Adjudication

**Cited location found:** Yes. The all-patient row and its headers are present in [DOC-001 Figure 3 — PDF p. 9](<../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9>). The matched primary-outcome row is present in [DOC-001 Table 2 — PDF p. 8](<../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=8>). The rounded result is also present in the [DOC-001 abstract — PDF p. 1](<../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=1>) and [DOC-001 primary-outcome narrative — PDF p. 6](<../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=6>).

**Source printed value/text matched:** Yes. Figure 3 is titled as a subgroup analysis of the composite primary outcome of all-cause death or hospitalization/emergency department visit for stroke, acute coronary syndrome, or heart failure. Its all-patient row prints bedtime `163` events and `71.0`, and morning `173` events and `71.0`. In both arms, the second number is under a column headed `Rate per 100 patient-years`. The row also prints hazard ratio `0.96 (0.77-1.19)`.

**Comparator matched:** Yes. Table 2's primary-outcome row describes the same composite, prints bedtime `163` and morning `173`, and prints rates per 100 patient-years of `2.30` and `2.44`, respectively, with hazard ratio `0.96 (0.77-1.19)` and `P = .70`. The abstract and primary-outcome narrative print the rounded rates `2.3` and `2.4` per 100 patient-years and the same adjusted hazard ratio and confidence interval. The repeated endpoint, arm order, event counts, effect estimate, and rate-unit wording establish a matched comparison.

**Consistency rule applicable:** For the same outcome, allocation arms, population, and explicitly named unit, repeated rate values should agree subject to the stated precision, or the source should identify a different measure or denominator. Ordinary rounding can reconcile `2.30` with `2.3` and `2.44` with `2.4`; it cannot reconcile values near `2.3` and `2.4` with `71.0` when all are read as rates per 100 patient-years.

**Calculation or logical comparison reproduced:** Yes. The direct value comparison is bedtime `71.0` versus `2.30` and morning `71.0` versus `2.44`, under identically worded rate columns. The event-count comparison is exact: `163 = 163` and `173 = 173`. A source-grounded diagnostic calculation also shows why `71.0` could be an exposure quantity rather than a rate: if `71.0` denotes hundreds of patient-years, then `163 / 7100 x 100 = 2.2958`, which rounds to `2.30`, and `173 / 7100 x 100 = 2.4366`, which rounds to `2.44`. Figure 3's complementary subgroup cells also add to `71.0` within each arm, for example bedtime male plus female is `30.5 + 40.5 = 71.0` and morning male plus female is `30.4 + 40.6 = 71.0`. Those calculations do not alter the directly printed Figure 3 header.

**Necessary inputs available:** The supplied paper provides enough information to reproduce the printed cross-location conflict: the exact endpoint wording, population context, arm order, event counts, rate headings, displayed rates, and repeated hazard ratio are all available. It also provides enough displayed precision to test ordinary rounding.

**Exact missing inputs or definitions:** The supplied package does not provide the locked Figure 3 production dataset, exact unrounded arm-specific patient-time denominators, a definition of what the `71.0` fields were intended to measure, the figure-generation specification, or the final figure source/layout file. These are required to determine whether the values, header, or both differ from the intended analysis output.

**Source-grounded alternative interpretation:** The `71.0` values may be total follow-up exposure expressed in hundreds of patient-years, because treating each as `7100` patient-years reproduces the Table 2 rates at the printed precision and because complementary subgroup values add to `71.0`. Alternatively, the fields may represent another unprinted exposure scale. The PDF does not label either interpretation.

**Direct observation versus inferred explanation:** Directly observed: Figure 3 prints `71.0/71.0` under `Rate per 100 patient-years`, whereas Table 2 prints `2.30/2.44` for the matched primary-outcome event counts and the narrative reports `2.3/2.4`. Inferred only: `71.0` may be exposure in hundreds of patient-years, or a figure-column label/value may have entered production incorrectly. The supplied source does not identify the production mechanism.

**Exact remaining human question:** What measure and denominator generated Figure 3's all-patient `71.0/71.0` fields, and should the human-approved publication action concern the displayed values, the `Rate per 100 patient-years` header, or both?

## C002 — Bedtime-diuretic six-month timing count triplets differ between eFigure 4 and eTable 6

**Status:** Pending Human Adjudication

**Cited location found:** Yes. The plotted medication counts are present in [DOC-004 eFigure 4 — PDF p. 26](<../../../joi250019supp3_prod_1749674951.30054.pdf#page=26>). The matched diuretic table rows are present in [DOC-004 eTable 6 — PDF p. 42](<../../../joi250019supp3_prod_1749674951.30054.pdf#page=42>); eTable 6 begins on [DOC-004 PDF p. 41](<../../../joi250019supp3_prod_1749674951.30054.pdf#page=41>).

**Source printed value/text matched:** Yes. eFigure 4 is titled `Adherence to allocation time at 6-months, by medication class`; its caption identifies `PM` as the bedtime group. The PM diuretic stack prints `278` as allocated, `138` off allocation, and `8` twice or more daily. The legend identifies those three categories.

**Comparator matched:** Yes. eTable 6 is titled `Medication use at 6-months`. Under bedtime `Diuretic`, it prints total `424`, with `277/424 (65.3)` as allocated, `139/424 (32.8)` off allocation, and `8/424 (1.9)` twice or more daily. Thus the time point, bedtime allocation, medication class, three timing categories, and total medication count match the figure context.

**Consistency rule applicable:** When a figure and table identify the same allocation arm, six-month time point, medication class, mutually exhaustive displayed timing categories, and medication total, their category counts should agree unless a distinct analysis set, coding rule, or data version is disclosed. Neither cited page discloses such a distinction for bedtime diuretics.

**Calculation or logical comparison reproduced:** Yes. Both triplets total the same `424`: `278 + 138 + 8 = 424` in eFigure 4 and `277 + 139 + 8 = 424` in eTable 6. The as-allocated count differs by one (`278` versus `277`), and the off-allocation count differs by one in the opposite direction (`138` versus `139`); the twice-or-more-daily count agrees (`8 = 8`). The eTable 6 percentages reproduce from its counts: `277/424 x 100 = 65.3302%`, `139/424 x 100 = 32.7830%`, and `8/424 x 100 = 1.8868%`, which round to `65.3%`, `32.8%`, and `1.9%`. Applying the same calculation to the figure counts gives `65.6%`, `32.5%`, and `1.9%` at one decimal, so the table percentages specifically support its `277/139/8` triplet rather than the plotted `278/138/8` triplet.

**Necessary inputs available:** The current PDF supplies the figure title/caption, arm key, legend categories, all three plotted PM diuretic counts, the table title, the bedtime diuretic total, and all table counts and percentages. These are sufficient to reproduce the one-medication category disagreement.

**Exact missing inputs or definitions:** The package does not provide the medication-level six-month timing records, a record identifier for the one medication classified differently, figure and table analysis-extraction dates, versioned coding rules, figure/table generation code, or a data-freeze record. Those inputs are needed to identify the intended category assignment.

**Source-grounded alternative interpretation:** One medication may have been reclassified between `as allocated` and `off allocation` after one display was generated; the figure and table may reflect different undisclosed data cuts; or one display may contain a transcription/layout change. Each interpretation preserves the shared total of `424`, but no cited source selects among them.

**Direct observation versus inferred explanation:** Directly observed: eFigure 4 prints `278/138/8`, eTable 6 prints `277/139/8`, and both triplets sum to `424`. Inferred only: a one-record recoding, asynchronous data cut, or production transcription may explain the difference. No generation history is supplied.

**Exact remaining human question:** Which locked six-month medication-level extract and category coding are authoritative for bedtime diuretics, and are the intended as-allocated/off-allocation counts `278/138` or `277/139` out of `424`?

## C003 — eTable 5 `Other` ethnicity row duplicates White/Caucasian values and exceeds randomized `Other` totals

**Status:** Pending Human Adjudication

**Cited location found:** Yes. The unable-to-follow cohort and its ethnicity rows are present in [DOC-004 eTable 5 — PDF p. 37](<../../../joi250019supp3_prod_1749674951.30054.pdf#page=37>). The randomized-arm ethnicity rows are present in [DOC-004 eTable 3 — PDF p. 29](<../../../joi250019supp3_prod_1749674951.30054.pdf#page=29>).

**Source printed value/text matched:** Yes. eTable 5 is headed as baseline characteristics for participants who did not complete follow-up and could not be followed using administrative data, stratified by morning allocation `n=44` and bedtime allocation `n=57`. Its `White/Caucasian` row prints morning `40 (90.9)` and bedtime `53 (93.0)`. Its separate `Other` row prints the identical values, morning `40 (90.9)` and bedtime `53 (93.0)`.

**Comparator matched:** Yes. eTable 3 is the expanded baseline table for the parent randomized arms, with bedtime `N=1677` and morning `N=1680`. Its `Other` ethnicity row prints bedtime `9 (0.5)` and morning `5 (0.3)`. Its `White` row prints bedtime `1565 (93.3)` and morning `1587 (94.5)`. The common baseline ethnicity label and allocation arms provide the comparator; eTable 5's stated unable-to-follow cohort is a subset of those randomized arms.

**Consistency rule applicable:** Under a common categorical definition, a subgroup count for a category cannot exceed the count for that category in its parent allocation arm. A separately printed category row also should not duplicate another category's count and percentage in both arms without an explicit overlapping-category or recoding definition. Neither cited table states that `Other` overlaps `White/Caucasian` or that `Other` was redefined in eTable 5.

**Calculation or logical comparison reproduced:** Yes. The eTable 5 percentages are arithmetically consistent with the duplicated counts: `40/44 x 100 = 90.9091%`, which rounds to `90.9%`, and `53/57 x 100 = 92.9825%`, which rounds to `93.0%`. The subset-to-parent comparisons are nevertheless impossible under the same `Other` definition: morning `40 > 5` by `35`, and bedtime `53 > 9` by `44`. The eTable 3 ethnicity counts also sum to each randomized-arm total: bedtime `1565 + 42 + 29 + 17 + 7 + 5 + 9 + 3 = 1677`; morning `1587 + 34 + 22 + 20 + 7 + 4 + 5 + 1 = 1680`. This supports interpreting its printed categories as a complete arm-level allocation of ethnicity entries rather than a smaller denominator that could contain additional unshown `Other` participants.

**Necessary inputs available:** The current PDF provides the subgroup definitions and denominators, allocation labels, duplicated eTable 5 rows, parent randomized-arm denominators, exact parent `Other` and `White` counts, and all needed displayed percentages. Those inputs are sufficient to reproduce the duplication and the parent-subset conflict under the same category label.

**Exact missing inputs or definitions:** The package does not provide the eTable 5 analysis export, participant-level baseline ethnicity records for the `n=44/n=57` cohort, a data dictionary proving identical category coding across eTables 3 and 5, the row-specific analysis behind the printed ethnicity `p-value`, or the table source/layout file. Those inputs are needed to recover the intended `Other` row and determine whether any label, value, or associated analysis changed.

**Source-grounded alternative interpretation:** The eTable 5 `Other` row may contain values copied from the adjacent `White/Caucasian` row; a row label may be misplaced; or eTable 5 may use an undisclosed recoding or overlapping-category definition. The duplicated values are plausible as White/Caucasian subgroup values because they are within the parent White counts, but that observation does not establish what the intended `Other` values are. No cited source documents a category redefinition.

**Direct observation versus inferred explanation:** Directly observed: eTable 5 prints the same `40 (90.9)` and `53 (93.0)` in both `White/Caucasian` and `Other`, while eTable 3 prints only `5` morning and `9` bedtime participants as `Other` in the full randomized arms. Inferred only: copying, row misalignment, recoding, or another production mechanism may explain the display. The intended replacement values cannot be inferred from the PDFs.

**Exact remaining human question:** What are the source-dataset morning and bedtime `Other` ethnicity counts for the `n=44/n=57` unable-to-follow cohort, was `Other` defined identically across eTables 3 and 5, and what human-approved publication action follows for the duplicated row and its associated ethnicity comparison?

## Recheck scope summary

- Stable IDs covered: C001, C002, C003 (`3/3`).
- Current direct-source locations found: all cited locations.
- Remaining limitations: the PDFs establish each printed comparison but do not supply the production datasets, exact unrounded person-time, version histories, generation code, or participant/medication-level records needed to identify intended replacement content.
- Status of every ID: Pending Human Adjudication.
