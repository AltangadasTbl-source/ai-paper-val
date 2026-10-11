# Candidate Ledger

All records below are **Pending Human Adjudication**. Stable IDs were assigned after merging only records that concerned the same printed values, comparator, and consistency rule. No display-zero-only candidates were registered.

## C001 — Figure 3 all-patient rate-column conflict with the matched primary-outcome rate

**Status:** Pending Human Adjudication

**Primary category:** Cross-document numeric inconsistency

**Checker provenance and relationship IDs:** Cross-source consistency checker, Proposal A; `N003`, `N030`, `S001`, `S005`, `S007`, `S010`, `S017`.

**Candidate statement:** The all-patient row in Figure 3 prints `71.0` for both treatment arms under columns labeled `Rate per 100 patient-years`, while the matched ITT primary-outcome result with the same arm-specific event counts is reported as 2.30 and 2.44 per 100 patient-years in Table 2 (and 2.3 and 2.4 in the abstract/narrative).

**Exact source locations:** [DOC-001 Figure 3 — PDF p. 9](<../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9>); [DOC-001 Table 2 — PDF p. 8](<../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=8>); [DOC-001 abstract — PDF p. 1](<../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=1>); [DOC-001 primary-outcome narrative — PDF p. 6](<../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=6>).

**Printed evidence and comparator:** Figure 3 identifies the composite primary outcome and prints all-patient event counts of 163 (bedtime) and 173 (morning), followed by 71.0 and 71.0 in its two columns headed `Rate per 100 patient-years`. Table 2 reports the same composite endpoint and arm event counts, with rates 2.30 and 2.44 per 100 patient-years. The abstract and narrative round these Table 2 rates to 2.3 and 2.4.

**Reproducible consistency rule and calculation:** The population (randomized ITT all patients), comparison (bedtime versus morning), outcome (composite primary outcome), and unit (rate per 100 patient-years) are printed as the same. Rounding can reconcile 2.30 with 2.3 and 2.44 with 2.4, but cannot reconcile 71.0 with either 2.30 or 2.44 under a shared rate unit. The direct printed all-patient event counts also match (163 and 173), so this is not explained by a different event count.

**Direct observation:** Figure 3 prints 71.0/71.0 under its rate columns; Table 2 prints 2.30/2.44 per 100 patient-years for the same all-patient composite result.

**Diagnostic inference:** The Figure 3 values or their column header may be a production/transcription error, or Figure 3 may use a different unprinted measure or denominator. The supplied sources do not establish which explanation is correct.

**Alternative source-grounded interpretations:** The figure may have retained a value from another scale, may have a mislabeled rate column, or may have been based on a differently defined rate calculation that is not described in its caption. The reported Table 2/narrative values could also be the intended all-patient rate display. None of these alternatives is resolved by the supplied package.

**Missing inputs:** Locked Figure 3 production dataset, person-time denominators used for its rate columns, and figure-generation specification.

**Exact human question:** What measure and denominator generated the Figure 3 all-patient values 71.0/71.0, and should the figure's values or its `Rate per 100 patient-years` header be corrected to match the matched primary-outcome analysis?

## C002 — Bedtime-diuretic six-month timing count triplets differ between eFigure 4 and eTable 6

**Status:** Pending Human Adjudication

**Primary category:** Cross-document numeric inconsistency

**Checker provenance and relationship IDs:** Cross-source consistency checker, Proposal B; `N025`, `N058`, `N064`, `N065`.

**Candidate statement:** DOC-004 eFigure 4 and eTable 6 print different medication-level timing counts for the same six-month bedtime-allocation diuretic total of 424.

**Exact source locations:** [DOC-004 eFigure 4 — PDF p. 26](<../../joi250019supp3_prod_1749674951.30054.pdf#page=26>); [DOC-004 eTable 6 — PDF p. 42](<../../joi250019supp3_prod_1749674951.30054.pdf#page=42>) (the table begins on PDF p. 41).

**Printed evidence and comparator:** eFigure 4 displays, for bedtime/PM diuretics, 278 as allocated, 138 off allocation, and 8 twice or more daily. eTable 6 reports the same bedtime diuretic total of 424 as 277/424 (65.3%) as allocated, 139/424 (32.8%) off allocation, and 8/424 (1.9%) twice or more daily.

**Reproducible consistency rule and calculation:** Both displays state the same allocation (bedtime), time point (six months), medication class (diuretic), and three timing categories, and both triplets total 424: 278+138+8=424 and 277+139+8=424. Nevertheless, the as-allocated and off-allocation cells differ by one. In addition, 277/424=65.33% and 139/424=32.78%, consistent with the eTable 6 displayed percentages at one decimal; 278/424=65.57%, which is not 65.3% at ordinary one-decimal rounding.

**Direct observation:** The direct-source figure and table give the exact differing triplets above, with the same total.

**Diagnostic inference:** One display may have been updated after the other, may use a distinct undisclosed coding cut, or may have a one-record category/transcription error. The supplied captions/notes do not state a different analysis set or definition that resolves the difference.

**Alternative source-grounded interpretations:** A diuretic medicine might have been recoded between figure and table production; one display could contain transposed allocation-category counts; or the visual figure may represent a pre-final extract. Both displayed triplets are arithmetically compatible with the printed total, so total arithmetic alone does not determine which is intended.

**Missing inputs:** Medication-level six-month timing records, analysis/extraction dates for eFigure 4 and eTable 6, and their figure/table generation code.

**Exact human question:** Which validated six-month medication-level extract is authoritative for bedtime diuretics, and should as-allocated/off-allocation be 278/138 or 277/139 of 424?

## C003 — eTable 5 `Other` ethnicity row duplicates White/Caucasian values and exceeds randomized `Other` totals

**Status:** Pending Human Adjudication

**Primary category:** Numeric or arithmetic inconsistency

**Checker provenance and relationship IDs:** Cross-source consistency checker, Proposal C; `N015`, `N061`, `N063`, `S034`.

**Candidate statement:** In DOC-004 eTable 5, the `Other` ethnicity row repeats the White/Caucasian values for participants unable to be followed through administrative data; those repeated counts also exceed the entire randomized baseline `Other` counts for each allocation arm in eTable 3.

**Exact source locations:** [DOC-004 eTable 5 — PDF p. 37](<../../joi250019supp3_prod_1749674951.30054.pdf#page=37>); [DOC-004 eTable 3 — PDF p. 29](<../../joi250019supp3_prod_1749674951.30054.pdf#page=29>).

**Printed evidence and comparator:** eTable 5 is headed morning allocation n=44 and bedtime allocation n=57. Its White/Caucasian row prints 40 (90.9%) and 53 (93.0%), and its later `Other` row prints exactly the same 40 (90.9%) and 53 (93.0%). eTable 3, for the randomized baseline arms, prints `Other` as 5/1680 (0.3%) morning and 9/1677 (0.5%) bedtime, while its White counts are 1587/1680 and 1565/1677.

**Reproducible consistency rule and calculation:** Under the table's displayed categorical ethnicity structure, `Other` cannot contain the same near-total count as White/Caucasian in the same n=44/n=57 cohort. Moreover, an unable-to-follow subgroup cannot contain more `Other` participants than its parent randomized allocation: 40>5 in morning and 53>9 in bedtime. This is not resolvable by rounding because the printed counts, not only percentages, conflict.

**Direct observation:** eTable 5 duplicates the White/Caucasian printed values in its `Other` row; eTable 3 prints the randomized-parent `Other` counts.

**Diagnostic inference:** The `Other` row values may be duplicated from White/Caucasian, a different row may be mislabeled or omitted, or a table-production error may have occurred. The package does not establish the intended replacement values.

**Alternative source-grounded interpretations:** A row label could have been misplaced, a value pair could have been copied during layout, or categories could conceivably have been differently coded. However, the source presents the rows as standard ethnicity categories and does not state that `Other` overlaps White/Caucasian; the parent-table counts independently remain incompatible.

**Missing inputs:** eTable 5 analysis export, the unable-to-follow cohort's baseline ethnicity coding, and the table layout/source file.

**Exact human question:** What are the validated morning and bedtime `Other` ethnicity counts for the n=44/n=57 unable-to-follow cohort, and does eTable 5 require correction of its duplicated row and any associated ethnicity comparison?

## Ledger summary

- **Stable candidate IDs:** C001, C002, C003.
- **Stable candidate count:** 3.
- **Status for every candidate:** Pending Human Adjudication.
- **Display-zero rule:** No display-zero-only candidates were registered.
