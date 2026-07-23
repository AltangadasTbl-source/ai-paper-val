# Statistical consistency checker — DOC-001 and DOC-003

## Scope and method

- **Main article:** `jama_cinciripini_2024_oi_240036_1716416465.98349.pdf` (DOC-001), PDF pages 1–10.
- **Results supplement:** `joi240036supp2_prod_1716416466.01349.pdf` (DOC-003), PDF pages 4–35.
- **Inputs used:** the DOC-001 main-text evidence map, the DOC-003 result-relevant supplementary evidence map, page-linked native text, and the available linked page renders. DOC-002 was not opened; it remains **Not Audited by Design**.
- **Checks:** point estimate versus interval; interval/null versus reported posterior probability; direction/sign; repeated CrIs and posterior probabilities; denominators; treatment/status labels; main-versus-supplement repetitions; and internal statistical claims. The article reports CrIs/posterior probabilities rather than frequentist P values for the audited primary and secondary contrasts, so there were no repeated P values to check.
- **Disposition rule:** `Accepted local candidate` means the supplied files themselves verify a reporting inconsistency suitable for coordinator/evidence-verifier review. `Uncertain` means the printed values raise a question but model output or hidden precision is needed. `Rejected` means the contemplated check is not supported.

## Prioritized local candidate evaluations

### S01 — Effect direction reverses between the reported outcomes, prose, and supplemental row label

- **Disposition:** Accepted local candidate
- **Category:** Statistical reporting inconsistency
- **Locations and source values:**
  - DOC-001, PDF p. 5, “Smoking Cessation End of Phase 2”: among varenicline phase-1 nonabstainers, switching to CNRT is `0% (95% CrI, 0%–0%; 0/41)` and continuing varenicline is `3% (95% CrI, 1%–4%; 2/77)`. The next paragraph reports, “Relative to continuation on varenicline, switching to CNRT resulted in an absolute RD of −3% (95% CrI, −4% to −1%)” but then says there was `>99%` posterior probability “that continuing was worse than switching.”
  - DOC-001, PDF p. 7, Figure 3 repeats `0/41; 0% (0%–0%)` for switching and `2/77; 3% (1%–4%)` for continuing.
  - DOC-003, PDF p. 21, E-Table 4 labels the contrast `Varenicline-Non-Abst. -->CNRT (switch) vs. Varenicline-(stay)` but reports positive `ARD 3% (95% CrI 1%–4%)`.
- **Reasoning:** With the main-text stated orientation, switch minus continuation is `0% − 3% = −3%`; that direction makes switching worse, not continuing worse. E-Table 4 uses the same printed switch-versus-stay row order but gives the opposite sign, `+3%`. This is a direction/sign inconsistency and does not depend on CrI symmetry.
- **Verification instruction:** Check the source PDF at DOC-001 pp. 5 and 7 and DOC-003 p. 21; then confirm the intended contrast coding in the underlying output and correct either the prose direction, the E-Table 4 row order/sign, or both.

### S02 — Repeated primary-contrast CrIs disagree across abstract, main results, and E-Table 4

- **Disposition:** Accepted local candidate
- **Category:** Cross-document inconsistency
- **Locations and source values:**
  - **CNRT nonabstainers, switch versus continue:** DOC-001 PDF p. 1 Abstract gives `RD 6%; 95% CrI, 6%–11%` immediately after the 51-person switch result. DOC-001 p. 5 gives `RD 6% (95% CrI, 2%–11%)` for both switch and increase versus continuation. DOC-003 p. 21 E-Table 4 gives the switch contrast `6% (2%–10%)` and the increase contrast `6% (2%–11%)`.
  - **Varenicline nonabstainers, increase versus continue:** DOC-001 p. 5 gives `18% (13%–24%)`; DOC-003 p. 21 E-Table 4 gives `18% (13%–23%)`.
  - **Phase-1 abstainers, CNRT versus varenicline at week 12:** DOC-001 p. 7 gives `6% (−5%–16%)`; DOC-003 p. 21 E-Table 4 gives `6% (−4%–16%)`.
- **Reasoning:** These are repeated reports of the same week-12 contrasts, yet at least one printed credible limit changes for each. The check compares repeated values only; it makes no symmetry assumption.
- **Verification instruction:** Compare the exact posterior summaries used for the abstract, results text, and E-Table 4 and determine the single correct rounded CrI for each contrast.

### S03 — E-Table 2 power increases when the posterior-probability threshold becomes stricter

- **Disposition:** Accepted local candidate
- **Category:** Statistical reporting inconsistency
- **Locations and source values:**
  - DOC-003, PDF p. 8, eAppendix 3 states that each hypothesis was evaluated at posterior-probability thresholds `0.80, 0.85, 0.90, and 0.95` using `K=1000 simulations`.
  - DOC-003, PDF p. 18, E-Table 2, `Effect of Treatment Phase I Abstainers—VAR>CNRT at EOT`, reports power `0.948` at threshold `0.80`, `0.980` at `0.85`, `0.974` at `0.90`, and `0.963` at `0.95`.
- **Reasoning:** Within the stated set of simulations, the event “posterior probability exceeds 0.85” is a subset of “posterior probability exceeds 0.80,” so its detected proportion cannot be larger. The printed `0.980` at 0.85 exceeds `0.948` at 0.80, whereas the other rows are nonincreasing.
- **Verification instruction:** Recalculate the four proportions from the same 1000 simulation-level posterior probabilities and check whether `0.948` or `0.980` is a transcription error or whether different simulation sets were used and must be disclosed.

### S04 — Secondary-outcome prose contains decimal-shifted values and malformed CrIs that conflict with its linked figures/tables

- **Disposition:** Accepted local candidate
- **Category:** Presentation inconsistency
- **Locations and source values:**
  - DOC-003, PDF p. 10, detailed EOT+30 CNRT analysis prints switch `1.0% (7.0%–1.3%)`, CNRT+ `8.0% (5.0%–1.1%)`, and switch ARD `6.0% (3.0%–1.0%)`. The linked E-Figure 2 on p. 15 gives switch `10% (7%–13%)` and CNRT+ `8% (5%–11%)`; E-Table 9 on p. 33 gives switch ARD `6% (3%–10%)`.
  - DOC-003, pp. 10–11, varenicline+ is repeatedly printed as `8.0% (5.0%–1.1%)`; E-Figure 2 p. 15 and E-Tables 9–10 pp. 33–34 give `8% (5%–11%)`.
  - DOC-003, p. 11, the abstainer EOT+30 contrast is printed `ARD = 1.1% (−1.0%–22%)`; E-Table 11 p. 35 gives `11% (−1%–22%)`.
- **Reasoning:** As printed, several intervals are reverse ordered and do not contain their point estimates. The linked exhibits show a consistent missing-zero/decimal-shift pattern (`1.0` for `10`, `1.3` for `13`, `1.1` for `11`), verifying that these are presentation/transcription errors rather than interval-shape judgments.
- **Verification instruction:** Compare every numeric statement in the detailed secondary-outcome prose on pp. 10–12 with E-Figures 2–3 and E-Tables 9–11, then restore the intended decimal places and interval endpoints.

### S05 — The varenicline-continuation denominator is 42 in prose but 77 in both secondary-outcome figures

- **Disposition:** Accepted local candidate
- **Category:** Cross-document inconsistency
- **Locations and source values:**
  - DOC-001, PDF p. 7, secondary-outcome prose: varenicline+ `8%; n=39` benefited relative to continuation `0%; n=42`.
  - DOC-003, PDF pp. 9–10, secondary-outcome summary repeats continuation `0%; n=42`.
  - DOC-003, PDF p. 15, E-Figure 2 reports EOT+30 continuation `0/77; 0% (0%–0%)`; p. 16, E-Figure 3 reports 6-month continuation `0/77; 0% (0%–0%)`.
  - DOC-001, PDF p. 6, Figure 2 shows that the primary-analysis continuation path of 77 comprises 42 rerandomized participants plus 35 nonreturners assigned/imputed to continuation.
- **Reasoning:** The prose and figures attach different denominators to the same varenicline-continuation secondary-outcome cell. The zero estimate is unchanged, but the population label and denominator are not.
- **Verification instruction:** Confirm whether the 35 nonreturners were included as nonabstinent for secondary continuous-abstinence analyses. State `n=42` if the estimand uses only rerandomized continuers, or `N=77` if the figures’ intent-to-treat cell is correct, and harmonize all locations.

### S06 — Main-text adherence claim is lower than the active-varenicline value shown in E-Table 8

- **Disposition:** Accepted local candidate
- **Category:** Cross-document inconsistency
- **Locations and source values:**
  - DOC-001, PDF p. 7, “Visit and Medication Adherence”: mean prescribed dosage taken was `82% or higher for active varenicline`.
  - DOC-003, PDF p. 32, E-Table 8: the active (not asterisked as placebo) phase-1-varenicline/abstainer/phase-2-varenicline cell reports varenicline adherence `80% (SD 32)`. Other active varenicline phase-2 cells are 82%, 83%, and 87%.
- **Reasoning:** The table contains an active-varenicline mean of 80%, which is below the main text’s asserted minimum of 82%.
- **Verification instruction:** Confirm the active/placebo flags and intended cell inclusion, then revise the main-text minimum or the E-Table 8 value.

### S07 — E-Table 5’s claim that only nausea differed by more than 2 percentage points is contradicted by its displayed estimates

- **Disposition:** Accepted local candidate
- **Category:** Statistical reporting inconsistency
- **Locations and source values:**
  - DOC-003, PDF p. 22, E-Table 5 introduction: “There were no adverse events for which these differences exceeded 2%, except for nausea in VAR.”
  - Same table, pp. 22–24, contains multiple absolute estimate differences exceeding 2 points: pruritus `8.39` versus `5.55` (difference `2.84`); skin rash `6.36` versus `2.71` (`3.65`); constipation `2.30` versus `4.33` (`2.03`); appetite decreased `3.11` versus `5.14` (`2.03`); headache `5.14` versus `8.39` (`3.25`); concentration impairment `1.49` versus `3.93` (`2.44`).
  - DOC-001, PDF p. 7 uses a narrower statement—differences exceeding 2% **with nonoverlapping CrIs**, except nausea—which is not what the E-Table 5 introduction says.
- **Reasoning:** Direct subtraction of E-Table 5’s own point estimates contradicts the table’s unqualified “exceeded 2%” claim. Several listed CrIs overlap, suggesting the supplement may have omitted the main article’s additional nonoverlap condition.
- **Verification instruction:** Recompute all phase-1 adverse-event estimate differences and clarify whether the intended statement was “>2 percentage points and nonoverlapping CrIs”; harmonize the table introduction with the main article.

### S08 — Repeated posterior probabilities differ between supplement prose and tables

- **Disposition:** Accepted local candidate
- **Category:** Statistical reporting inconsistency
- **Locations and source values:**
  - DOC-003, PDF p. 11, six-month CNRT+ versus varenicline switch: posterior probability `88%`; E-Table 10 p. 34 reports `89%` for the same `ARD 2% (−1%–6%)`.
  - DOC-003, PDF p. 12, six-month abstainer comparison: posterior probability `55%`; E-Table 11 p. 35 reports `56%`.
- **Reasoning:** Each pair repeats the same contrast and time point to a whole percentage point but gives two different rounded probabilities.
- **Verification instruction:** Retrieve the unrounded posterior probabilities and apply one stated rounding rule consistently in prose and tables.

### S09 — Abstract allocation percentages silently use different denominators within each nonabstainer cohort

- **Disposition:** Accepted local candidate
- **Category:** Presentation inconsistency
- **Locations and source values:**
  - DOC-001, PDF p. 1 Abstract Results: among `191` CNRT nonabstainers, `151` were rerandomized and 40 nonreturners were assigned to continuation; the outcome sentence gives continue `90 (47%)`, increase `50 (33%)`, and switch `51 (34%)`.
  - The same abstract states `157` varenicline nonabstainers, `122` rerandomized and 35 nonreturners assigned to continuation; the outcome sentence gives increase `39 (32%)`, switch `41 (34%)`, and continue `77 (49%)`.
- **Reasoning:** The displayed calculations use two denominators without labeling the change: CNRT `90/191=47%`, but `50/151=33%` and `51/151=34%`; varenicline `77/157=49%`, but `39/122=32%` and `41/122=34%`. Read as percentages of each stated nonabstainer cohort, the percentages do not partition the cohort and sum above 100%.
- **Verification instruction:** Label the rerandomized denominator for switch/increase percentages or express all three phase-2 path percentages using the same denominator.

### S10 — Six-month abstainer ARD sign may conflict with the printed group estimates and contrast label

- **Disposition:** Uncertain
- **Category:** Statistical reporting inconsistency
- **Locations and source values:**
  - DOC-003, PDF p. 16, E-Figure 3: CNRT abstainers continuing CNRT `39% (30%–48%)`; varenicline abstainers continuing varenicline `40% (33%–47%)`.
  - DOC-003, PDF p. 35, E-Table 11 header `ARD For CNRT vs. VAR` gives `+1% (−11%–12%)`.
  - DOC-003, PDF p. 12 says the same contrast is a small benefit of varenicline continuation and reports `ARD = 1.0%` with decimal-shifted limits.
- **Reasoning:** The displayed group estimates and prose direction suggest VAR minus CNRT is positive (or CNRT minus VAR is negative), whereas the table labels CNRT versus VAR and prints positive `1%`. However, the contrast is model-based and the displayed cell estimates are rounded; the unrounded joint posterior is unavailable, so the sign cannot be conclusively reconstructed from the package artifacts.
- **Verification instruction:** Inspect the unrounded posterior draws and the E-Table 11 contrast code to confirm whether the header, sign, or prose direction should change.

## Rejected/non-finding checks

- **CrI symmetry:** Rejected as an audit basis. The outcome analyses are Bayesian logistic/IPW models; the reported method does not imply symmetric probability-scale CrIs. No candidate above relies on symmetry.
- **CrI/null versus posterior probability:** No additional contradiction verified. Examples such as `3% (0%–6%)` with a 96% directional posterior probability and `11% (−1%–22%)` with 97% are compatible with central interval quantiles plus whole-percent rounding.
- **Point estimate inside its interval:** All exhibit-level estimates checked were inside their reported intervals. The exceptions are the malformed detailed-prose values in S04, which are independently verified as decimal transcription errors by their linked figures/tables.
- **Subgroup labels:** No demographic subgroup/interaction result was reported in the audited main text. Treatment-path/status labels were checked; the consequential direction/label questions are captured in S01 and S10.

## Checker conclusion

Nine local candidates are accepted for coordinator prioritization and one is uncertain. The strongest candidates are S01, S03, S04, and S02. No source PDF was modified, no external source was used, and DOC-002 was not opened.
