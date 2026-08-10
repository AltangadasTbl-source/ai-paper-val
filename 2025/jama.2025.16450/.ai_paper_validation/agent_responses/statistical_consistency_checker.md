# Statistical Consistency Checker Response

- Agent: `statistical_consistency_checker`
- Documents audited: `JAMA2025-16450-MAIN` and `JAMA2025-16450-SUPP04-RESULTS`
- Sources used: retained main-text evidence map, results-supplement evidence map, page-linked normalized text, and retained/rendered table and figure images.
- Excluded by design: protocol, Manual of Operations, SAP, administrative material, and external sources.
- Candidate limit: 2 local candidates retained.

## Retained candidates

### SC-01 - Baseline FIO2 subgroup denominator differs between Table 1 and Figure 2

- **Category:** Presentation inconsistency
- **Confidence:** High
- **Document and locations:** `jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf`
  - PDF p.6 / printed p.1457, Table 1, rows "FIO2 at baseline" and "High FIO2 (>=0.5) at baseline."
  - PDF p.9 / printed p.1460, Figure 2, subgroup "Baseline FIO2," plus footnote c.
- **Source values/statements:**
  - Table 1 reports baseline FIO2 for budesonide + surfactant as `n=228`, with `86/228` at FIO2 >=0.5; therefore the complementary FIO2 <0.50 denominator is `228 - 86 = 142`.
  - Table 1 reports baseline FIO2 for surfactant alone as `n=230`, with `81/230` at FIO2 >=0.5; therefore the complementary FIO2 <0.50 denominator is `230 - 81 = 149`.
  - Figure 2 reports budesonide + surfactant denominators of `142` for FIO2 <0.50 and `86` for FIO2 >=0.50, matching Table 1 (`142 + 86 = 228`).
  - Figure 2 reports surfactant-alone denominators of `150` for FIO2 <0.50 and `81` for FIO2 >=0.50, totaling `231`, one more than Table 1's `n=230`.
  - Figure 2 footnote c states that the FIO2 subgroups exclude 182 participants from the ITT population. With the reported ITT population of 641, that implies `641 - 182 = 459`, equal to Figure 2's `228 + 231`, while Table 1 supplies `228 + 230 = 458` baseline FIO2 observations.
- **Logical basis:** The same baseline FIO2 variable, thresholds, ITT framing, and "last known" pretreatment measurement are presented with discordant surfactant-alone denominators. The discrepancy is localized to one participant in the FIO2 <0.50 subgroup; the article does not explain a different data source or eligibility rule for Figure 2.
- **Verification instruction:** Visually compare Table 1 on PDF p.6 with the FIO2 rows and footnote c of Figure 2 on PDF p.9, then verify against the subgroup-analysis input which surfactant-alone denominator is correct (`149`/total `230` or `150`/total `231`).

### SC-02 - eTable 4 defines "RR" as risk difference although the table reports relative risks

- **Category:** Presentation inconsistency
- **Confidence:** High
- **Document and locations:** `joi250072supp4_prod_1761000786.6988.pdf`
  - PDF p.7, eTable 4 header and binary-outcome estimate labels.
  - PDF p.8, eTable 4 abbreviation line and methods note.
  - Corroborating internal convention: main article PDF p.8 / printed p.1459, Table 3, which separately labels `RD` as risk difference and `RR` as relative risk.
- **Source values/statements:**
  - eTable 4's estimate column is headed "Relative Risk (RR) or Mean Difference (MD) (95% CI)," and binary rows are labeled `RR`, for example PDA `RR: 0.86 (0.75, 0.99)`.
  - The eTable 4 note states, "Binary outcomes report relative risks, estimated by robust Poisson regression, unless otherwise noted."
  - The abbreviation line on PDF p.8 instead states, "RR = risk difference."
- **Logical basis:** "RR = risk difference" conflicts with the table header, row labels, model description, and the article's separate use of `RD` for risk difference. The displayed numerical measures in eTable 4 are intended as relative risks, so the abbreviation expands RR incorrectly.
- **Verification instruction:** Inspect the eTable 4 header on PDF p.7 and the abbreviation/methods lines on PDF p.8; correct the expansion to "RR = relative risk" if confirmed.

## Rejected or uncertain checks

### R-01 - ITT-excluding-untreated population size 635 versus Table 2 analyzed denominator 634

- **Disposition:** Rejected
- **Locations:** Main article PDF p.7 / printed p.1458, sensitivity-analysis text and Table 2; results supplement PDF p.2, eTable 1.
- **Reasoning:** The text defines an ITT-excluding-untreated population of `n=635`. Table 2 reports `218/319` and `215/315`, totaling 634 participants with observed primary endpoints. eTable 1 explicitly reports primary-endpoint completion as `634/635` and one early end. The population size and analyzed nonmissing denominator therefore describe different, consistently documented quantities.

### R-02 - Main-article and supplement death counts differ

- **Disposition:** Rejected
- **Locations:** Main article PDF p.7 / printed p.1458, Table 2; results supplement PDF p.15, eTable 8.
- **Reasoning:** Table 2 reports ITT/as-randomized death before 36 weeks PMA (`49/321` vs `42/318`), whereas eTable 8 reports the safety/as-treated population (`48/321` vs `41/313`). eTable 1 defines the treatment-assignment basis for each population. The differing counts are population-dependent and are not a document-grounded contradiction.

### U-01 - Adjusted direction for the "Other" race subgroup differs from the crude proportions

- **Disposition:** Uncertain; not retained as an issue
- **Location:** Main article PDF p.9 / printed p.1460, Figure 2.
- **Values:** `7/21 (33.3%)` versus `4/17 (23.5%)` gives a crude risk ratio of approximately `1.42`, while Figure 2 reports adjusted RR `0.93 (0.33-2.66)`.
- **Reasoning:** Figure 2 states that the estimate comes from robust Poisson regression adjusted for gestational-age stratum and pooled center. An adjusted estimate can reverse the crude direction, especially in a small subgroup. Without the model strata/output, this model-dependent property is not verifiable as an error.

### R-03 - "No difference" statements, confidence intervals, and subgroup P values

- **Disposition:** Rejected
- **Locations:** Main article PDF pp.1-2 and 6-9 / printed pp.1452-1453 and 1457-1460; supplement PDF pp.5-8, eTables 3-4.
- **Reasoning:** Reported point estimates lie within their printed confidence intervals. Primary, component, secondary, SAE, and subgroup estimates described as showing no difference have intervals containing the appropriate null (0 for differences; 1 for ratios). Figure 2 interaction P values (`.72`, `.35`, `.45`, `.28`, `.33`) are all above `.05` and agree with the statement that no significant treatment-by-subgroup differences were observed. The adverse-event burden P values (`.004` for AE burden and `.42` for SAE burden) agree with the displayed between-group direction/equality at the available precision. No CI-versus-P-value contradiction was located.

## Cross-source checks with no retained issue

- The primary adjusted RR `1.00 (0.90-1.11)` is repeated consistently in the abstract, Key Points, Results text, and Table 2.
- Death `1.13 (0.78-1.64)` and physiologic BPD `0.99 (0.87-1.12)` are repeated consistently in the abstract, Results text, and Table 2.
- Any adverse event `1.16 (1.05-1.28)`, hyperglycemia `1.33 (1.17-1.51)`, and PDA `0.86 (0.75-0.99)` agree between the main text and Supplement 4.
- The signed mean differences and risk differences in main Table 3 agree with the displayed treatment-group direction; no confidence-interval symmetry assumption was used.
