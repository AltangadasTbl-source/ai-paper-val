# AI Paper Validation Report — Human Adjudication

## Scope

Nine accepted evidence cards are presented below (maximum 10). Permission to perform this scoped validation was granted for this investigation. Source PDFs were read only and remain unchanged. This report is not a legal opinion.

## Scientific Issue Cards

### 1. Mortality-event-rate values differ between the article text and its cited eTable, which affects the numerical reporting of the primary shared-parameter model.

- **Category / severity:** Cross-document inconsistency / Major.
- **Evidence:** **Reported:** DOC-001, `jama_berry_2025_oi_240158_1742927563.7361.pdf`, PDF p. 4, *Results—Primary Efficacy Outcome*: “mortality event rate was **0.007 events per month** … shared placebo … and **0.006 events per month** … combined CNM-Au8 dosage groups.” **Comparator:** DOC-004, `joi240158supp3_prod_1742927563.7911.pdf`, PDF p. 15, eTable 2, *Mortality Event Rate (events per month)*: shared placebo median/mean **0.010 / 0.010 (0.0026)**; pooled CNM-Au8 **0.009 / 0.009 (0.0025)**.
- **Direct comparison:** Article 0.007 vs eTable 0.010 (shared placebo), difference **−0.003 events/month**; article 0.006 vs eTable 0.009 (CNM-Au8), difference **−0.003 events/month**. The article expressly cites eTable 2.
- **Calculation / rule:** For each group, reported article rate − eTable mean rate: 0.007−0.010=−0.003; 0.006−0.009=−0.003 events/month. A 0.001 display-rounding tolerance cannot reconcile either difference.
- **Bounded impact:** The mortality-rate sentence or eTable 2 value requires correction or confirmation; this card does not determine which source is authoritative.
- **Verification:** 1. Reproduce the model output used for the primary analysis. 2. Confirm the rounded posterior rate for each group. 3. Resolve the issue if the article and eTable are revised to the same defined estimate (median or mean) or if a stated estimand explains the difference.

### 2. The reported 95% credible-interval limits for ALSFRS-R slopes do not match the cited eTable, affecting precision reporting for the primary model.

- **Category / severity:** Cross-document inconsistency / Moderate.
- **Evidence:** **Reported:** DOC-001, `jama_berry_2025_oi_240158_1742927563.7361.pdf`, PDF p. 4, *Results—Primary Efficacy Outcome*: shared placebo −1.03 points/month “(95% CrI, **−1.176 to −0.892**)”; combined CNM-Au8 −1.00 points/month “(95% CrI, **−1.153 to −0.858**).” **Comparator:** DOC-004, `joi240158supp3_prod_1742927563.7911.pdf`, PDF p. 15, eTable 2, *ALSFRS-R Slopes (points per month)*: shared placebo **(−1.181, −0.894)**; pooled CNM-Au8 **(−1.143, −0.847)**.
- **Direct comparison:** Shared-placebo lower/upper limits differ by +0.005/+0.002 points/month; pooled-CNM-Au8 limits differ by −0.010/−0.011 points/month (article minus eTable).
- **Calculation / rule:** Article endpoint − eTable endpoint, as above. Three-decimal presentation means ordinary rounding tolerance is at most ±0.0005 points/month; each listed discrepancy exceeds that tolerance.
- **Bounded impact:** The reported CrI limits in the text or eTable need confirmation; the point estimates are not challenged by this card.
- **Verification:** 1. Inspect the model export and table-production code. 2. Identify the exact posterior quantiles and their rounding rule. 3. Resolve if both sources use the same quantiles/rounding, or correct the divergent limits.

### 3. The article labels 24-week SVC changes as “per month,” whereas the cited eTable labels them as 24-week change in percent predicted, making the reported unit/time basis unclear.

- **Category / severity:** Presentation inconsistency / Major.
- **Evidence:** **Reported:** DOC-001, `jama_berry_2025_oi_240158_1742927563.7361.pdf`, PDF p. 4, *Results—Secondary Efficacy Outcomes*: “mean change in SVC over 24 weeks was **−9.32 PPN per month** … vs **−8.53 PPN per month** (difference, **−0.78 PPN/month**).” **Comparator:** DOC-004, `joi240158supp3_prod_1742927563.7911.pdf`, PDF p. 16, eTable 3A, header *24-week Change Estimate*, row *SVC (% predicted)*: pooled −9.32 (1.36), shared placebo −8.53 (1.15), difference −0.78 (1.77), 95% CI −4.25 to 2.68.
- **Direct comparison:** The same values are presented as **PPN/month** in the article and as a **24-week change estimate for SVC (% predicted)** in the eTable.
- **Calculation / rule:** A 24-week change divided by approximately 5.52 months would be −1.69 and −1.55 percentage points/month, not −9.32 and −8.53. No rounding tolerance is relevant because the conflict is dimensional.
- **Bounded impact:** The text’s SVC unit/time label requires correction or confirmation; the numerical estimates and CI are not otherwise recalculated here.
- **Verification:** 1. Check the repeated-measures estimand and eTable 3A programming output. 2. Confirm whether −9.32/−8.53 are 24-week changes or monthly rates. 3. Resolve by aligning the article wording and table header with that estimand.

### 4. Serum-NfL changes and the between-group value differ between the article and eTable 3B, affecting the reported exploratory biomarker result.

- **Category / severity:** Cross-document inconsistency / Major.
- **Evidence:** **Reported:** DOC-001, `jama_berry_2025_oi_240158_1742927563.7361.pdf`, PDF p. 8, Figure 3B and *Biomarker Analyses*: regimen placebo **+30.8%** (43.1 to 56.5 pg/mL); CNM-Au8 **+0.4%** (60.6 to 60.8 pg/mL); difference **−23.2% geometric mean ratio** (95% CI −39.5% to −2.5%; P=.03). **Comparator:** DOC-004, `joi240158supp3_prod_1742927563.7911.pdf`, PDF p. 17, eTable 3B, ERO row *Serum NfL (% change)*: CNM-Au8 **0.4**, regimen placebo **26.8**, difference **−26.4**, 95% CI −50.3 to −2.6, P=.03; footnote: results were log-transformed and exponentiated back.
- **Direct comparison:** Placebo change is +30.8% vs +26.8% (**+4.0 percentage points**); reported between-group value is −23.2% vs −26.4% (**+3.2 percentage points**). CNM-Au8 +0.4% and P=.03 agree.
- **Calculation / rule:** From the article’s displayed concentrations, ((60.8/60.6)/(56.5/43.1)−1)×100 = **−23.5%**, consistent with the article’s −23.2% within rounding/model-based estimation. The eTable values identify a separately displayed −26.4%; the supplied evidence gives no stated reason for the discrepancy. Rounding tolerance: ±0.05 percentage point for one-decimal percentages.
- **Bounded impact:** The placebo change and/or reported serum-NfL comparison need confirmation across Figure 3/text and eTable 3B; this card does not determine the correct model output.
- **Verification:** 1. Verify the analysis population and log-scale back-transformation used for Figure 3B and eTable 3B. 2. Recalculate the published GMR from the model output. 3. Resolve by documenting distinct estimands or making the values/CI consistent.

### 5. **Uncertain** — Plasma-NfL confidence-interval limits differ slightly between Figure 3 and eTable 3B, but the supplied evidence does not establish whether this is more than display rounding.

- **Category / severity:** Cross-document inconsistency / Uncertain.
- **Missing evidence:** Unrounded model estimate/CI and the rounding convention for Figure 3 and eTable 3B.
- **Evidence:** **Reported:** DOC-001, `jama_berry_2025_oi_240158_1742927563.7361.pdf`, PDF p. 8, Figure 3A: difference **−9.5%** (95% CI **−17.8% to −0.5%**; P=.04). **Comparator:** DOC-004, `joi240158supp3_prod_1742927563.7911.pdf`, PDF p. 17, eTable 3B, ERO *Plasma NfL (% change)*: difference **−9.5**, 95% CI **−18.0, 0**, P=.04.
- **Direct comparison:** Point estimate and P value agree; lower/upper CI endpoints differ by **+0.2** and **−0.5 percentage points** respectively (figure minus eTable).
- **Calculation / rule:** −17.8−(−18.0)=+0.2; −0.5−0=−0.5 percentage points. One-decimal rounding normally allows ±0.05 percentage point per displayed endpoint, but the model scale/rounding and any figure-versus-table processing are unavailable.
- **Bounded impact:** Confirm the plasma-NfL CI display only; no conclusion about the underlying estimate is supported.
- **Verification:** 1. Obtain unrounded CI endpoints for both displays. 2. Apply each display’s documented rounding rule. 3. Resolve if the endpoints derive from the same CI after that rule; otherwise correct or explain the discrepant display.

### 6. Death counts for the regimen-specific placebo group are reported as 1, 3, and 2 across the narrative, participant-flow figure, and safety eTable.

- **Category / severity:** Participant flow inconsistency / Major.
- **Evidence:** **Reported narrative:** DOC-001, `jama_berry_2025_oi_240158_1742927563.7361.pdf`, PDF p. 4, *Results—Trial Participants*: “One participant in the regimen placebo group died during participation in the RCT portion.” **Flow comparator:** DOC-001, same file, PDF p. 5, Figure 1, regimen-specific placebo (n=41) follow-up branch: “**3 Died**.” **Safety comparator:** DOC-004, `joi240158supp3_prod_1742927563.7911.pdf`, PDF p. 21, eTable 5, row *Deaths*, regimen-specific placebo: **2 (4.9%), 2**.
- **Direct comparison:** For the same regimen-specific placebo group, counts are **1 vs 3 vs 2**; figure minus narrative = +2, eTable minus narrative = +1, figure minus eTable = +1 death.
- **Calculation / rule:** Direct count subtraction above; no rounding tolerance applies to whole-person death counts. The supplied excerpts do not state a common time window/definition that reconciles all three counts.
- **Bounded impact:** The regimen-specific placebo death count and its flow/safety presentation need confirmation; this card does not infer a total mortality count beyond the three reports.
- **Verification:** 1. Check participant-level death dates and each display’s population/time window. 2. Confirm the intended count for RCT participation, Figure 1 discontinuation, and TEAE safety reporting. 3. Resolve with harmonized labels/counts or explicit definitions that reconcile them.

### 7. **Uncertain** — The article says no serious adverse events were related to trial drug, while eTable 5 reports treatment-related serious TEAEs; differing terminology/populations are not resolved in the supplied evidence.

- **Category / severity:** Cross-document inconsistency / Uncertain.
- **Missing evidence:** Definitions/mapping of “SAE” versus “treatment-related serious TEAE,” and confirmation of the analysis population/time window.
- **Evidence:** **Reported:** DOC-001, `jama_berry_2025_oi_240158_1742927563.7361.pdf`, PDF p. 8, *Safety and Tolerability*: “**No SAEs** … were considered related to the trial drug.” **Comparator:** DOC-004, `joi240158supp3_prod_1742927563.7911.pdf`, PDF p. 21, eTable 5, row *Treatment-Related Serious TEAE*: shared placebo **2 (1.2%), 3 events**; regimen-specific placebo **1 (2.4%), 2 events**; pooled CNM-Au8 **0 (0.0%), 0**.
- **Direct comparison:** Text reports zero related SAEs; eTable reports related serious TEAEs in placebo columns (2 participants/3 events shared placebo and 1 participant/2 events regimen-specific placebo). The death clause in the same sentence is not part of this card.
- **Calculation / rule:** Zero versus nonzero counts: 0→2 participants (+2) and 0→1 participant (+1). No rounding tolerance applies; semantic equivalence cannot be established from the supplied evidence.
- **Bounded impact:** Confirm the relationship between the narrative SAE claim and eTable 5’s treatment-related serious-TEAE row; no conclusion that either is erroneous is supported.
- **Verification:** 1. Review the protocol/SAP definitions and AE coding for SAE and serious TEAE. 2. Match the eTable events to the narrative population and causality assessment. 3. Resolve by confirming non-equivalence or correcting/explaining the narrative/table.

### 8. The serum-NfL sensitivity eFigure mixes serum and plasma timing/specimen wording and presents one percentage change without a percent sign, reducing clarity of the result display.

- **Category / severity:** Presentation inconsistency / Moderate.
- **Evidence:** DOC-004, `joi240158supp3_prod_1742927563.7911.pdf`, PDF p. 25, *eFigure. Serum Neurofilament Sensitivity Analysis*: “NfL tested in **serum samples** longitudinally at Baseline, Week 4 (**plasma only**), Week 8 (**serum only**), Week 16, and Week 24”; “NfL values **<4pg/mL**”; “placebo group (**+11.6**) and … CNM-Au8 treatment group (**+0.8%**).”
- **Direct comparison:** The title/specimen statement says serum, while the timepoint parentheticals include “plasma only”; +11.6 has no displayed “%” whereas +0.8 includes it. “<4pg/mL” lacks spacing between value and unit.
- **Calculation / rule:** No numeric transformation is required. Consistent specimen labeling requires each included timepoint to match the stated serum analysis; consistent percentage presentation requires the % unit on both changes. Rounding tolerance is not applicable.
- **Bounded impact:** The eFigure caption/prose needs clarification or correction of specimen/timepoint and unit presentation; this card does not alter the sensitivity-analysis estimate.
- **Verification:** 1. Check the plotted data and analysis dataset for specimen at each visit. 2. Confirm whether Week 4 belongs in a serum-only sensitivity analysis. 3. Correct the caption/units or state why the wording is intentional.

### 9. Table 1 race counts total 160 for a shared-placebo group of 164, but the footnote says race was unknown or unreported for 3 participants, leaving one participant unaccounted for.

- **Category / severity:** Arithmetic inconsistency / Moderate.
- **Evidence:** DOC-001, `jama_berry_2025_oi_240158_1742927563.7361.pdf`, PDF p. 6, Table 1, *Shared (n=164)*, Race rows: Asian **2/160 (1.2%)**; Black or African American **6/160 (3.8%)**; White **151/160 (94.4%)**; Multiple races **1/160 (0.6%)**. Table 1 footnote b: “Race was unknown or unreported for **3 participants** ….”
- **Direct comparison:** Race-row numerator total is 2+6+151+1=**160**. With n=164 and 3 unknown/unreported, expected classified-race denominator is 164−3=**161**; reported denominator is 160, a deficit of **1 participant**.
- **Calculation / rule:** 2+6+151+1=160; 164−3=161; 161−160=1 participant. Percentages sum to 100.0% on the printed denominator 160 (1.2+3.8+94.4+0.6=100.0), so percentage rounding does not resolve the count/footnote discrepancy.
- **Bounded impact:** The shared-placebo race denominator or footnote requires correction/confirmation; this card is limited to the Table 1 race presentation.
- **Verification:** 1. Check the baseline demographic dataset for the shared-placebo group’s race field. 2. Confirm the number unknown/unreported and the denominator used for percentages. 3. Resolve by correcting the rows or footnote so the denominator and missing count reconcile with n=164.

## AI Training Restriction Summary

This is a separate document-level compliance screen, not a scientific issue list, and is not a legal opinion.

| Document ID | Filename | Status | Exact evidence location | Human Compliance Review |
|---|---|---|---|---|
| DOC-001 | `jama_berry_2025_oi_240158_1742927563.7361.pdf` | Explicit AI Training Restriction | PDF p. 1, bottom copyright footer (identical pp. 2–12): “All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Yes |
| DOC-002 | `joi240158supp1_prod_1742927563.7611.pdf` | Conditional / Permission Required | PDF p. 8, protocol signature page: “I will not disclose such information to others without authorization”; p. 69, §12.6.1: third-party disclosure prohibited; p. 70, §12.7.2: sharing governed by legal agreements. | Yes |
| DOC-003 | `joi240158supp2_prod_1742927563.7711.pdf` | No AI Training Restriction Located in Provided Materials | Rights-focused review of PDF pp. 1, 62, 63, and 130, searchable text layer, and embedded metadata located no responsive AI-training/right statement. | No |
| DOC-004 | `joi240158supp3_prod_1742927563.7911.pdf` | Explicit AI Training Restriction | PDF p. 1 footer (confirmed pp. 2, 24–26): “All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Yes |
| DOC-005 | `joi240158supp4_prod_1742927563.8061.pdf` | No AI Training Restriction Located in Provided Materials | Rights-focused review of PDF pp. 1 and 6, all-page keyword screen, and embedded metadata located no responsive AI-training/right statement. | No |
| DOC-006 | `joi240158supp5_prod_1742927563.8111.pdf` | No AI Training Restriction Located in Provided Materials | PDF p. 1, *Additional Information*, and embedded metadata: data/report-sharing and code-access statements do not address AI training; no responsive rights statement located. | No |

“No AI Training Restriction Located” does not infer permission from silence.
