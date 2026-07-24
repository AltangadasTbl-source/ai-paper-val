# Statistical consistency checker response

## Scope

- Main article: `jama_sun_2024_oi_240088_1746815064.14747.pdf`
- Results supplement: `joi240088supp1_prod_1746815064.21247.pdf`, PDF pages 10–25 only
- Evidence used: the main-text evidence map, results-supplement evidence map, native page text, and retained page renders
- Protocol/SAP and supplement pages 3–9 were not used.
- Confidence-interval symmetry and other model-dependent properties were not treated as errors.

## Local candidate issues (10)

### 1. Incidence-difference estimate lies outside its reported 95% CI

- **Taxonomy:** Statistical reporting inconsistency
- **Location:** `jama_sun_2024_oi_240088_1746815064.14747.pdf`, PDF p.8 / print p.1066, Table 2, secondary outcome “Any stroke outside the territory of the qualifying artery within 1 y after enrollment.”
- **Source values:** Balloon angioplasty 3/249 (1.2%) vs aggressive medical management 4/252 (1.6%); incidence difference −0.4 percentage points; 95% CI, −2.4 to −1.7; HR 0.76 (95% CI, 0.17–3.40); P=.72.
- **Basis:** The raw percentage-point difference is `100 × (3/249 − 4/252) = −0.3825`, which rounds to the reported −0.4. A confidence interval for that point estimate must contain −0.4, but the displayed interval [−2.4, −1.7] does not.
- **Verification instruction:** Inspect the Table 2 row in the source render and recompute the incidence-difference CI using the article’s intended method; determine which displayed CI endpoint/sign is incorrect.

### 2. Table S6 mixes an ITT-sized header with a nonmatching balloon event count and percentage

- **Taxonomy:** Cross-document inconsistency
- **Locations:** `joi240088supp1_prod_1746815064.21247.pdf`, PDF p.19, Table S6; `jama_sun_2024_oi_240088_1746815064.14747.pdf`, PDF p.8 / print p.1066, Table 2, primary outcome.
- **Source values:** Table S6 labels the groups n=249 and n=252 but reports the primary outcome as 9 (3.9%) vs 34 (13.5%). Main Table 2 reports the same primary-outcome definition and denominators as 11 (4.4%) vs 34 (13.5%).
- **Basis:** `9/249 = 3.61%`, which rounds to 3.6%, not 3.9%. The displayed 3.9% instead matches `9/233 = 3.86%`, the per-protocol balloon denominator documented in Figure 1 and Table S10. Center adjustment can change an adjusted HR but does not explain a different displayed raw event count without a stated population restriction.
- **Verification instruction:** Confirm whether Table S6 was intended to show the ITT population (11/249) or PPS population (9/233), and check the analysis dataset behind the adjusted HR 0.32 (0.16–0.62).

### 3. Table S7 group headers conflict with the site rows and the analysis represented

- **Taxonomy:** Presentation inconsistency
- **Location:** `joi240088supp1_prod_1746815064.21247.pdf`, PDF p.20, Table S7.
- **Source values:** Headers say balloon N=233 and medical-management N=238. Site rows report Beijing Tiantan Hospital: 256 patients, 4 (2.9%) vs 19 (16.1%); other centers: 245 patients, 7 (6.3%) vs 15 (11.2%).
- **Basis:** The site totals are 256+245=501, not 471. The event totals are 11 vs 34, matching the ITT primary analysis. The only integer site denominators consistent with all four displayed one-decimal percentages and the two site totals are 138 vs 118 at Beijing Tiantan and 111 vs 134 at other centers; these sum to balloon 249 and medical management 252. Thus the row data reflect 249/252, not the displayed 233/238.
- **Verification instruction:** Reconstruct the site-by-treatment participant table and correct the group headers or, if PPS was intended, replace the site totals, event counts, percentages, HRs, and interaction analysis as applicable.

### 4. Table S8 labels per-protocol results with ITT denominators

- **Taxonomy:** Presentation inconsistency
- **Locations:** `joi240088supp1_prod_1746815064.21247.pdf`, PDF p.21, Table S8; PDF p.23, Table S10; main article PDF p.5 / print p.1063, Figure 1.
- **Source values:** Table S8 is titled “Study outcomes in the per-protocol population (PPS)” but its headers say n=249 and n=252. It reports 9 (3.9%) vs 33 (13.9%) for the primary outcome. Table S10 explicitly labels PPS N=233 and N=238; Figure 1 also shows 233 and 238 after per-protocol exclusions.
- **Basis:** The percentages use the PPS denominators: `9/233=3.86%→3.9%` and `33/238=13.87%→13.9%`. They do not use the headers: `9/249=3.6%` and `33/252=13.1%`.
- **Verification instruction:** Check the PPS analysis population and replace the Table S8 column headers with 233 and 238 if the displayed counts, percentages, and HRs are PPS results.

### 5. Table S9 labels as-treated results with ITT denominators

- **Taxonomy:** Presentation inconsistency
- **Locations:** `joi240088supp1_prod_1746815064.21247.pdf`, PDF p.22, Table S9; PDF p.23, Table S10.
- **Source values:** Table S9 is titled “Study outcomes in the as-treated population (ATS)” but its headers say n=249 and n=252. It reports 11 (4.5%) vs 34 (13.4%) for the primary outcome. Table S10 explicitly labels ATS N=247 and N=254.
- **Basis:** The percentages use the ATS denominators: `11/247=4.45%→4.5%` and `34/254=13.39%→13.4%`. With the displayed headers, they would be 4.4% and 13.5%.
- **Verification instruction:** Check treatment-received assignments and replace the Table S9 headers with 247 and 254 if the displayed results are the ATS analysis.

### 6. Figure S5’s AMM category data use 249 patients despite the N=252 label

- **Taxonomy:** Presentation inconsistency
- **Location:** `joi240088supp1_prod_1746815064.21247.pdf`, PDF p.13, Figure S5, 1-year mRS distribution.
- **Source values:** The AMM bar is labelled N=252. Its mRS 0–6 category counts are 169, 58, 13, 3, 3, 1, and 2, with displayed percentages 67.9%, 23.3%, 5.2%, 1.2%, 1.2%, 0.4%, and 0.8%.
- **Basis:** Counts sum to 249, not 252. Every percentage is calculated using 249 (for example, 169/249=67.9% and 58/249=23.3%), whereas 169/252=67.1% and 58/252=23.0%. The figure gives no missing-data denominator.
- **Verification instruction:** Inspect the source-category dataset for the three unrepresented AMM participants and correct the group N, category counts/percentages, or add an explicit evaluated/missing denominator.

### 7. Lead-center count differs between the 501-patient main analysis and the site-interaction table

- **Taxonomy:** Cross-document inconsistency
- **Locations:** `jama_sun_2024_oi_240088_1746815064.14747.pdf`, PDF p.4 / print p.1062, Results—Patient Population; `joi240088supp1_prod_1746815064.21247.pdf`, PDF p.20, Table S7; supplement PDF p.12, Figure S3.
- **Source values:** The main Results state that 258/501 primary-analysis patients were from the lead center. Table S7 partitions the same 501 patients as 256 at Beijing Tiantan Hospital and 245 at other centers. Figure S3 separately shows 258 patients enrolled at Beijing Tiantan in the 512-patient recruitment display.
- **Basis:** `256+245=501`, so Table S7 assigns 256, not 258, of the analyzed patients to the lead center. The repeated value 258 in Figure S3 is attached to the pre-exclusion enrollment total of 512, suggesting the main narrative may have paired the recruitment count with the 501 denominator.
- **Verification instruction:** Trace the 11 postrandomization exclusions by site and confirm whether the lead-center numerator in the 501-patient analysis is 256 or 258.

### 8. Arterial perforation is reported as 0.4% in the main article but 0 in Table S4

- **Taxonomy:** Cross-document inconsistency
- **Locations:** `jama_sun_2024_oi_240088_1746815064.14747.pdf`, PDF p.7 / print p.1065, Results—Procedural Complications and Adverse Events; `joi240088supp1_prod_1746815064.21247.pdf`, PDF p.17, Table S4.
- **Source values:** Main narrative: arterial perforation 0.4% in the balloon group. Table S4: arterial perforation 0 (0.0%).
- **Basis:** The statements refer to the same listed balloon-angioplasty procedural-complication set and the main narrative cites Table S4, but one corresponds to one event and the other to zero.
- **Verification instruction:** Check the procedural-complication case list and adjudicated definition, then make the main narrative and Table S4 agree on the count and percentage.

### 9. Several baseline percentages do not match their displayed counts and denominators

- **Taxonomy:** Arithmetic inconsistency
- **Locations and source values:**
  - Main article PDF p.4 / print p.1062, Results—Patient Population: 343 (69.1%) male among 501.
  - Main article PDF p.6 / print p.1064, Table 1: balloon female 77 (30.1%) with group n=249; balloon 90%–99% stenosis 25 (10.4%) with group n=249.
  - Results supplement PDF p.14, Table S1: among 215 balloon patients with qualifying ischemic stroke, border-zone 84 (39.1%) and non-zone 131 (61.9%).
- **Basis:** `343/501=68.5%`, not 69.1%; `77/249=30.9%`, not 30.1%; `25/249=10.0%`, not 10.4%; and `131/215=60.9%`, not 61.9%. The Table S1 subcategories sum exactly to 215, confirming 215 as the local denominator.
- **Verification instruction:** Recalculate the published percentages from the displayed counts and applicable denominators, checking whether any count rather than percentage was intended to differ.

### 10. Table S11 P values marked as chi-square match Fisher exact calculations

- **Taxonomy:** Statistical reporting inconsistency
- **Location:** `joi240088supp1_prod_1746815064.21247.pdf`, PDF p.24, Table S11 and footnotes c/d.
- **Source values:** Rows marked footnote c (“Tested by Chi-square test”) include overall serious adverse events 12/249 vs 14/252, P=.84; nervous-system disorders 7/249 vs 12/252, P=.35; disabling stroke 6/249 vs 18/252, P=.02. Footnote d separately denotes Fisher’s exact test.
- **Basis:** For the first two decisive rows, ordinary Pearson chi-square calculations give P=.710 and P=.253; continuity-corrected chi-square gives P=.865 and P=.363. Two-sided Fisher exact calculations give P=.841 and P=.350, exactly matching the displayed .84 and .35. For disabling stroke, two-sided Fisher gives P=.0196 (display .02); Pearson gives .0131 and continuity-corrected chi-square gives .0231. Thus the c-labelled P values appear to have been generated by Fisher’s exact test or the method label is otherwise incomplete.
- **Verification instruction:** Re-run the three c-labelled 2×2 comparisons with the stated software/options and determine whether the P values or the c/d method markers should be corrected.

## Rejected/uncertain checks

- CI symmetry was not assessed because the reported Cox and generalized-odds models do not justify a symmetry assumption on the displayed scale.
- Subgroup HR/interaction-P recomputation was not attempted from aggregate events because time-to-event data and model covariance are unavailable.
- No issue was assigned merely because a CI crossed the null when no stratum-specific P value was reported.
- The Figure 3/Table 2 repeated HRs and P values, primary component counts, and Table S5 revascularization totals were internally concordant.

Source PDFs were not modified.
