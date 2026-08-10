# Evidence Verifier Response - Round 1

- Package: `jama.2025.4390`
- Verification scope: exactly the 7 coordinator-supplied candidates (`TAC-01`, `SCI-01`, `SCI-02`, `SCI-03`, `FFC-01`, `FFC-02`, `FFC-03`)
- Verification round: 1 of maximum 2
- Source standard: original supplied PDFs re-opened at every cited page; retained page renders visually inspected; no external sources used
- Outcome: **7 Verified; 0 Uncertain; 0 Rejected**
- Second verification round: **not required**

## Classification summary

| Candidate | Category | Classification |
|---|---|---|
| TAC-01 | Presentation inconsistency | **Verified** |
| SCI-01 | Presentation inconsistency | **Verified** |
| SCI-02 | Statistical reporting inconsistency | **Verified** |
| SCI-03 | Statistical reporting inconsistency | **Verified** |
| FFC-01 | Arithmetic inconsistency | **Verified** |
| FFC-02 | Presentation inconsistency | **Verified** |
| FFC-03 | Arithmetic inconsistency | **Verified** |

## Verified findings

### TAC-01 - Duplicated ethnicity row

- **Classification:** Verified.
- **Location:** `joi250019supp3_prod_1749674951.30054.pdf`, PDF p. 37, eTable 5, `Ethnicity - no. (%)`, `White/Caucasian` and `Other` rows.
- **Source values:** Morning allocation (n=44): `White/Caucasian 40 (90.9)` and `Other 40 (90.9)`. Bedtime allocation (n=57): `White/Caucasian 53 (93.0)` and `Other 53 (93.0)`.
- **Comparison evidence:** The corresponding full-cohort ethnicity breakdown in eTable 3, PDF p. 29, uses the same eight displayed categories as a partition: bedtime counts sum to 1677 and morning counts sum to 1680. No eTable 5 footnote authorizes overlapping ethnicity categories.
- **Calculation / logical basis:** On p. 37, the eight displayed ethnicity rows sum to `40+1+1+1+0+1+40+1 = 85` for morning and `53+1+1+1+1+0+53+1 = 111` for bedtime, or 193.2% and 194.7% of the stated group denominators. The `Other` cells exactly reproduce the `White/Caucasian` cells in both groups. This is a visible table-content duplication, even though the source export is needed to determine the intended `Other` values.
- **Human verification instruction:** Open supplement PDF p. 37, compare the `White/Caucasian` and `Other` cells, and check the eTable 5 source export for the intended `Other` counts or row placement.

### SCI-01 - Figure 3 rate columns contain person-time values

- **Classification:** Verified.
- **Location:** `jama_garrison_2025_oi_250019_1749674951.29054.pdf`, PDF p. 9 / printed p. 2069, Figure 3, both columns headed `Rate per 100 patient-years`; comparison: Table 2, PDF p. 8 / printed p. 2068, primary-outcome row.
- **Source values:** Figure 3 all-patients row gives bedtime `163` events and `71.0`, and morning `173` events and `71.0`, under the rate headings. Figure subgroup values partition the 71.0 values, for example bedtime sex rows `30.5+40.5=71.0` and age rows `14.9+56.1=71.0`. Table 2 gives the corresponding primary-outcome rates as bedtime `2.30` and morning `2.44` per 100 patient-years.
- **Calculation / logical basis:** The Table 2 event counts and rates imply about `163/2.30*100 = 7087.0` bedtime patient-years and `173/2.44*100 = 7090.2` morning patient-years, or about 70.9 hundreds of patient-years. Conversely, treating Figure 3's 71.0 as a rate would imply only 229.6 and 243.7 patient-years. Thus 71.0 behaves as person-time in hundreds of patient-years, not as an event rate per 100 patient-years. The Figure 3 column heading is inconsistent with its values.
- **Human verification instruction:** Compare Figure 3 p. 9 with Table 2 p. 8 and confirm in the figure-generation data that the 71.0 and subgroup values are patient-years divided by 100; correct either the heading or the displayed values.

### SCI-02 - Figure 3 footnote misstates the all-patients CI as unadjusted

- **Classification:** Verified.
- **Location:** `jama_garrison_2025_oi_250019_1749674951.29054.pdf`, PDF p. 9 / printed p. 2069, Figure 3 all-patients row and footnote; comparisons: Results text, PDF p. 6 / printed p. 2066, and Table 2, PDF p. 8 / printed p. 2068.
- **Source statements / values:** Figure 3 reports all patients `HR 0.96 (95% CI, 0.77-1.19)` and states `All confidence intervals are unadjusted.` Results text identifies `0.96 (95% CI, 0.77-1.19)` as the adjusted result and separately identifies the unadjusted result as `0.94 (95% CI, 0.76-1.17)`. Table 2 repeats the adjusted result `0.96 (95% CI, 0.77-1.19)`.
- **Calculation / logical basis:** The Figure 3 all-patients estimate and CI exactly match the adjusted primary analysis and differ from the separately reported unadjusted estimate and CI. Therefore, the universal footnote is false for the all-patients row as displayed.
- **Human verification instruction:** Compare the Figure 3 all-patients row and footnote on p. 9 with the adjusted and unadjusted results on pp. 6 and 8; determine whether the footnote should be limited to subgroup rows or the all-patients row should be changed.

### SCI-03 - Identical binary comparisons have different P values

- **Classification:** Verified.
- **Location:** `joi250019supp3_prod_1749674951.30054.pdf`, PDF p. 39, eTable 5, `Type of BP-lowering med - no. (%)`, `Diuretic` and `Combination BP med` rows. Group denominators are stated in the eTable 5 header on PDF p. 37.
- **Source values:** Morning allocation n=44 and bedtime allocation n=57. `Diuretic` reports `9 (20.5)` versus `16 (28.1)`, `P=0.34`. `Combination BP med` reports the identical `9 (20.5)` versus `16 (28.1)`, `P=0.38`.
- **Calculation / logical basis:** The displayed 2-by-2 comparison is identical for both rows: morning 9 yes/35 no and bedtime 16 yes/41 no. Applying the same unadjusted binary-group comparison to identical cells must return the same P value. The table gives different P values and states no different denominator, adjustment, or row-specific procedure. At least one displayed P value or count is inconsistent with the table's presented comparison.
- **Human verification instruction:** Re-run or inspect the source output for both eTable 5 binary comparisons using n=44 and n=57; identify whether a count or one of the two P values needs correction.

### FFC-01 - British Columbia city counts exceed the province header

- **Classification:** Verified.
- **Location:** `joi250019supp3_prod_1749674951.30054.pdf`, PDF p. 22, eFigure 1, `Location of Participating Practices`, British Columbia column; comparison: eTable 1, PDF p. 27.
- **Source values:** British Columbia header `43`. Listed city counts: Chilliwack 12; Comox 1; Courtenay 1; Cranbrook 1; Duncan 1; Fort St. John 1; Langley 1; Nanaimo 1; New Westminster 4; Port Coquitlam 12; Powell River 1; Richmond 3; Smithers 3; Vancouver 2. Other province headers are Alberta 326, Saskatchewan 22, Manitoba 29, and Ontario 16. eTable 1 states that 436 PCPs mailed recruitment information.
- **Calculation / logical basis:** British Columbia city counts sum to `12+1+1+1+1+1+1+1+4+12+1+3+3+2 = 44`, not 43. The five province headers sum to `43+326+22+29+16 = 436`, matching eTable 1, whereas the city listings sum one higher because the British Columbia column is internally off by one.
- **Human verification instruction:** Recount the British Columbia city entries on p. 22 and compare them with the province header; inspect the figure source data to identify whether the header or a city count is wrong.

### FFC-02 - Bedtime diuretic adherence differs between figure and table

- **Classification:** Verified.
- **Location:** `joi250019supp3_prod_1749674951.30054.pdf`, PDF p. 26, eFigure 4, bedtime/PM `Diuretic` bar; comparison: eTable 6, PDF p. 42, bedtime `Diuretic` rows.
- **Source values:** eFigure 4 shows `278` as allocated, `138` off allocation, and `8` twice or more daily. eTable 6 reports bedtime diuretic n=424 as `277/424` as allocated, `139/424` off allocation, and `8/424` twice or more daily.
- **Calculation / logical basis:** Both displays use the same total and the same mutually exclusive categories. Figure total: `278+138+8 = 424`. Table total: `277+139+8 = 424`. One medication is assigned differently between the first two categories.
- **Human verification instruction:** Compare the bedtime/PM diuretic bar on p. 26 with the bedtime diuretic rows on p. 42 and check the 6-month medication-timing source export to determine which display is correct.

### FFC-03 - Calcium-channel-blocker percentage is arithmetically wrong in two tables

- **Classification:** Verified.
- **Location:** `jama_garrison_2025_oi_250019_1749674951.29054.pdf`, PDF p. 6 / printed p. 2066, Table 1 continued, `Calcium channel blocker`; repeated in `joi250019supp3_prod_1749674951.30054.pdf`, PDF p. 32, eTable 3, same row.
- **Source values:** Bedtime denominator n=1677 and `479 (28.2)` in both tables. The same rows report morning `489/1680 (29.1)` and overall `968/3357 (28.8)`.
- **Calculation / logical basis:** `479/1677*100 = 28.5629%`, which rounds to **28.6%** at one decimal, not 28.2%. The comparison cells reconcile: `489/1680*100 = 29.1071%` -> 29.1%, and `968/3357*100 = 28.8353%` -> 28.8%.
- **Human verification instruction:** Inspect the repeated cell in main Table 1 p. 6 and supplement eTable 3 p. 32, verify the intended numerator and denominator in the source table, and correct the repeated percentage or source count.

## Round disposition

All seven candidates meet the package evidence standard in round 1: exact page/table/figure location, source and comparison values, and a reproducible arithmetic or logical basis are present. No candidate is being advanced to a second verification round.
