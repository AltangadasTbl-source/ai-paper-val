# Table arithmetic and internal-consistency check — DOC-001 and DOC-003

## Scope and method

- **Checker:** table arithmetic and internal consistency.
- **Scientific scope inspected:** DOC-001 PDF pp. 1–10 and DOC-003 PDF pp. 4–35 only. DOC-002 was not opened or audited.
- **Materials:** page-linked native text, the result evidence maps, and targeted renders of DOC-001 p. 5 and DOC-003 pp. 15–16, 21, 32, and 35 to confirm table/figure column placement.
- **Scope boundary:** only result-relevant tables in the package manifest/evidence map were checked. Protocol/SAP/administrative material was excluded. No raw-data inference was made.

## Candidate issues for verification (priority order)

### TA-01 — Sex-row counts exceed each phase-1 table denominator

- **Category:** Arithmetic inconsistency
- **Location:** DOC-001, `jama_cinciripini_2024_oi_240036_1716416465.98349.pdf`, PDF p. 5 (journal p. 1726), **Table. Baseline Measures and Demographics**, *Sex* rows.
- **Source values:** both columns are headed `n = 245`. In each, Female is `105 (42.9)` and Male is `145 (57.1)`.
- **Calculation:** `105 + 145 = 250`, not 245; `145 / 245 = 59.2%`, not the printed 57.1%. Conversely, `57.1% × 245 ≈ 140`, and the result text on DOC-001 p. 4 reports 210 women among 490 participants, matching the displayed female total `105 + 105 = 210` but not the printed male total `145 + 145 = 290` (490 − 210 = 280).
- **Reasoning:** the two mutually exclusive sex counts cannot both be correct for either displayed N=245 arm.
- **Verification instruction:** check the source table typesetting/data table for the male numerator in both columns; retain the shown denominators and percentage labels when adjudicating.
- **Status:** Candidate — document-verifiable.

### TA-02 — Race/ethnicity categories exceed the displayed N in one phase-2 cell

- **Category:** Arithmetic inconsistency
- **Location:** DOC-003, `joi240036supp2_prod_1716416466.01349.pdf`, PDF p. 19, **E-Table 3**, *Race and ethnicity, n (%)*, `Varenicline` phase 1 → `Non-abstainer` → phase-2 `CNRT (N=41)` column.
- **Source values:** African American `12 (29.3)`, Asian `1 (2.4)`, Hispanic `3 (7.3)`, More than one race `1 (2.4)`, White non-Hispanic `24 (58.5)`, Other `4.9 (2)`.
- **Calculation:** counts (treating the visibly reversed final cell as 2) sum to `12 + 1 + 3 + 1 + 24 + 2 = 43`, versus header N=41. Percentages sum to `29.3 + 2.4 + 7.3 + 2.4 + 58.5 + 4.9 = 104.8%`. The displayed `4.9 (2)` is also reverse-ordered relative to the row label `n (%)` and all adjacent race cells.
- **Reasoning:** every other E-Table 3 race/ethnicity column reconciles to its stated N; this column does not, by two participants/4.8 percentage points.
- **Verification instruction:** reconcile this column against the underlying displayed category counts and confirm whether a count, denominator, or category assignment is misprinted; do not assume which individual cell should change.
- **Status:** Candidate — document-verifiable.

### TA-03 — Direction/sign in one E-Table 4 risk-difference contrast conflicts with its ordered comparison and outcome cells

- **Category:** Arithmetic inconsistency / Presentation inconsistency
- **Location:** DOC-003 PDF p. 21, **E-Table 4**, row `Varenicline-Non-Abst. -->CNRT (switch) vs. Varenicline-(stay)`; cross-check: DOC-001 PDF p. 7, Figure 3 and DOC-003 p. 21.
- **Source values:** E-Table 4 prints ARD `3%` (95% CrI `1%` to `4%`) and NNT `39` for the ordered `CNRT (switch) vs Varenicline (stay)` comparison. Figure 3 gives switch `0/41; 0%` and stay `2/77; 3%`; DOC-001 results text p. 5 reports a `−3%` RD for switching relative to continuation.
- **Calculation:** in the printed contrast order, `0% − 3% = −3%` (using the displayed point estimates; raw proportions are `0/41 − 2/77 = −2.60 percentage points`). Other E-Table 4 rows follow their printed first-minus-second direction (e.g., CNRT+ `14%` minus CNRT `8%` = `+6%`).
- **Reasoning:** the positive ARD/NNT is incompatible with the row’s stated contrast direction and the visible adjacent outcome values. The main article reports the negative sign, creating a within-package discrepancy.
- **Verification instruction:** verify whether the E-Table 4 row label/order, ARD sign/interval, and NNT direction were transposed; preserve the distinction between a sign correction and a change to the underlying event counts.
- **Status:** Candidate — document-verifiable.

### TA-04 — E-Table 8 footnote denominator conflicts with the header it annotates

- **Category:** Arithmetic inconsistency / Presentation inconsistency
- **Location:** DOC-003 PDF p. 32, **E-Table 8**, phase-1 CNRT/non-abstinent, phase-2 `CNRT (N=50)^b` header and footnote `b=2/51`.
- **Source values:** the header bearing superscript b says `CNRT (N=50)^b`; the only b footnote says `medication data was incomplete or missing for b=2/51`.
- **Calculation:** the annotated header denominator is 50, whereas the footnote denominator is 51; `2/51` cannot describe missing data within an N=50 column.
- **Reasoning:** the printed pointer/denominator relationship is internally impossible. The table’s adjacent CNRT-phase-1 non-abstainer switch column is `VAR 2mg (N=51)` without a footnote marker, so a misplaced marker is one possible explanation, but the correction is not inferred.
- **Verification instruction:** verify the intended recipient of footnote b and its denominator against the phase-2 compliance source table; do not recalculate compliance means from unavailable person-level data.
- **Status:** Candidate — document-verifiable.

### TA-05 — Six-month abstainer ARD sign conflicts with its labeled direction and displayed probabilities

- **Category:** Arithmetic inconsistency / Presentation inconsistency
- **Location:** DOC-003 PDF p. 35, **E-Table 11**, *6-months, Continuous Abstinence* (`ARD For CNRT vs. VAR`); cross-check DOC-003 PDF p. 16, **E-Figure 3**.
- **Source values:** E-Table 11 prints `1% (−11%–12%)` for CNRT vs VAR. E-Figure 3 displays CNRT `21/54; 39%` and varenicline `35/88; 40%`.
- **Calculation:** in the table’s stated CNRT-versus-VAR direction, displayed probabilities give `39% − 40% = −1 percentage point`; raw proportions give `(21/54 − 35/88) × 100 = −0.88 percentage points`. E-Table 11 instead prints `+1%`. The supplement prose on p. 12 describes the small direction as benefit for varenicline continuation.
- **Reasoning:** the printed positive ARD is directionally inconsistent with both the labeled comparison and the table-linked displayed outcome values. The confidence interval crosses zero, so this is a sign/presentation issue, not a claim of a meaningful treatment difference.
- **Verification instruction:** verify the signed six-month CNRT-minus-VAR point estimate in the analysis output; retain the interval/probability unless independently shown to be affected.
- **Status:** Candidate — document-verifiable.

## Rejected / not advanced after local checks

| Check | Location | Calculation / reason for rejection |
|---|---|---|
| E-Table 4 NNT values other than TA-03 | DOC-003 p. 21 | Apparent differences between reciprocal calculations using rounded ARDs and printed NNTs are compatible with unrounded model estimates: e.g., 6% can yield NNT 16 or 17; no document-verifiable discrepancy identified. |
| E-Table 8 pathway header totals vs full primary-analysis totals | DOC-003 p. 32 vs DOC-001 p. 6 | Headers sum to 205 for initial CNRT and 210 for initial varenicline, short of 245 by 40 and 35. Those exact shortfalls are the non-rerandomized nonabstainers assigned to continuation for primary analysis; a compliance-table omission is not independently documented as erroneous. |
| E-Tables 9–10 secondary-outcome ARDs | DOC-003 pp. 33–34 vs E-Figures 2–3, pp. 15–16 | Differences and directions reconcile at displayed precision: EOT+30 CNRT+ vs switch `8%−10%=−2%`; VAR+ vs CNRT `8%−0%=8%`; six-month values `6%−4%=2%` and `2%−0%=2%`. Small deviations in switch-vs-continuation values are model/rounding-compatible. |
| Main Table race, employment, and income totals excluding sex counts | DOC-001 p. 5 | Each displayed category set totals N=245 per arm; no additional arithmetic candidate. |
| E-Table 3 employment value order | DOC-003 p. 19 | Cells use percentage followed by count (e.g., `72.2 (39)`) despite a `n (%)` convention elsewhere. Counts/percentages reconcile, but this is a table-wide formatting convention and is not advanced separately beyond TA-02’s locally reversed race cell. |

## Completion/status update

- DOC-001 table arithmetic check completed for the selected result-relevant table(s).
- DOC-003 table arithmetic check completed for result-relevant E-Tables 1–12; E-Figures 2–3 were used only as table-linked outcome anchors for direction/denominator checks.
- Five document-verifiable candidates are advanced; no raw-data claims or protocol/SAP comparisons were made. Source PDFs unchanged.
