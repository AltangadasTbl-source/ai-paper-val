# Statistical Consistency Checker Response

## Scope and method

- Audited the main-article evidence map, Supplement 3 result evidence map, normalized text, and retained page images for the main article and result-relevant supplement only.
- Checked point estimates against confidence intervals, confidence intervals against null values and P values, effect direction, repeated estimates/CIs/P values, narrative-table-figure correspondence, main-to-supplement correspondence, and subgroup labels.
- Did not use the protocol, SAP, web sources, or external knowledge. Source PDFs were not modified.
- CI symmetry and exact P-value reconstruction were not used because the report does not establish that all displayed intervals and P values came from a common Wald calculation.

## Candidate issues (2)

### SCC-01 - Blanket "no differences in quality of life" statement conflicts with a significant day-7 EuroQol contrast

- **Category:** Statistical reporting inconsistency
- **Locations:**
  - `jama_atherton_2025_oi_240145_1741627844.85412.pdf`, PDF p. 1 (printed p. 853), Abstract Results.
  - Same file, PDF p. 6 (printed p. 858), Secondary Outcomes.
  - `joi240145supp3_prod_1741627844.89412.pdf`, PDF p. 4, Supplementary eTable 3, "EQ5D-5L EuroQol score," Day 7 row.
- **Source statements and values:** The abstract says that, of 7 secondary outcomes, 6 "showed no significant difference," explicitly including quality of life. The Results text says, "There were no differences in quality of life between the 2 groups (eTables 2-4 in Supplement 3)." However, eTable 3 reports at day 7: iNPWT mean 0.44 (SD 0.32), surgeon's preference mean 0.49 (SD 0.30), adjusted mean difference **-0.057 (95% CI, -0.104 to -0.010), P=.02**. The table states that values greater than 0 favor iNPWT, so the displayed estimate favors the surgeon's-preference group; the CI excludes the null value 0 and the P value is below .05. The table also gives a treatment-by-time interaction **P=.10**.
- **Logical basis:** The unqualified narrative "no differences" does not correspond to the reported day-7 inferential result. The global treatment-by-time interaction is nonsignificant, so the intended inferential basis may have been the interaction rather than the pointwise contrast; the article does not make that distinction in the cited narrative.
- **Verification instruction:** Confirm whether the quality-of-life conclusion was intended to rely on the global interaction test or on the reported time-specific contrasts. Reconcile the sentence with the day-7 EuroQol estimate, CI, and P value, or explicitly label the day-7 contrast and the role of multiplicity/global interaction.

### SCC-02 - Figure 2 includes an incision-length subgroup not identified in the Methods subgroup list

- **Category:** Presentation inconsistency
- **Locations:**
  - `jama_atherton_2025_oi_240145_1741627844.85412.pdf`, PDF p. 4 (printed p. 856), Statistical Analysis, subgroup paragraph.
  - Same file, PDF p. 9 (printed p. 861), Figure 2, "Subgroup Analysis."
- **Source statements and values:** The Methods identifies prespecified primary-outcome subgroups as the minimization variables (operative contamination and stoma), operative procedure, skin preparation, BMI, country, wound-assessment method, and randomization before/on or after March 11, 2020. Figure 2 displays all of those and also displays **"Length of incision, cm"** with categories **<15** and **>=15**, event counts **21 vs 22** and **90 vs 81**, adjusted RRs **1.28 (95% CI, 0.76-2.16)** and **1.01 (0.79-1.29)**, and interaction **P=.42**.
- **Logical basis:** The additional figure subgroup has no corresponding label in the article's stated subgroup inventory. The report therefore does not let the reader determine from the audited main article whether incision length was prespecified or was an additional analysis. This is a reporting-label/scope mismatch, not a claim that the subgroup computation is wrong.
- **Verification instruction:** Confirm the intended status of the incision-length analysis from the reporting records. Add it to the Methods subgroup inventory if prespecified, or label it as additional/post hoc in Figure 2 or its caption if it was not.

## Uncertain leads (not asserted as findings)

### SCC-U01 - Wound-related readmission adjusted RD appears discordant with the adjusted RR and crude risks

- **Category if confirmed:** Statistical reporting inconsistency
- **Location:** `jama_atherton_2025_oi_240145_1741627844.85412.pdf`, PDF p. 8 (printed p. 860), Table 3, "Hospital readmission for wound-related complications."
- **Values:** **11/399 (3%) vs 11/398 (3%)**; adjusted **RD 0.010 (95% CI, -0.014 to 0.034)**; adjusted **RR 1.02 (95% CI, 0.45-2.31), P=.96**. The crude RD is `11/399 - 11/398 = -0.000069`, and at an approximately 2.8% reference risk an RR of 1.02 corresponds to an RD near 0.0006, not 0.010.
- **Why uncertain:** The Methods states that RD and RR came from separate adjusted mixed-effects binomial models using identity and log links. Without fitted model outputs or underlying covariates, exact agreement between the two adjusted scales is not a document-valid requirement.
- **Verification instruction:** Check the analysis output or typesetting source to determine whether **0.010** is the intended adjusted RD or a decimal-place transcription error (for example, **0.001**).

### SCC-U02 - Figure 1 reports one more control-group death than the 30-day mortality result

- **Category if confirmed:** Cross-document inconsistency or Participant flow inconsistency
- **Locations:** Main article PDF p. 3 (printed p. 855), Figure 1 footnote b; PDF p. 6 (printed p. 858), Safety Outcomes; PDF p. 8 (printed p. 860), Table 3.
- **Values:** Figure 1 footnote b says **25 deaths** were reported: **10 iNPWT and 15 surgeon's preference**. The Safety Outcomes text and Table 3 report mortality **within 30 days** as **10/411 and 14/410**.
- **Why uncertain:** Figure 1 says "total deaths reported" without an explicit time window, whereas the text/table result is explicitly restricted to 30 days. One later control-group death could explain the difference.
- **Verification instruction:** Confirm the time window for the 15 control-group deaths in Figure 1. If all occurred within 30 days, reconcile Figure 1 with the 14-death result; otherwise add the time distinction.

## Rejected checks

- **Point estimate inside CI:** All audited estimates lie within their displayed CIs.
- **CI-null-P-value direction:** Every audited CI excluding its null has a reported P value below .05 (day-7 pain and day-7 EuroQol), and every audited CI including its null has a reported P value at or above .05. No threshold contradiction was found.
- **Repeated primary estimates:** Primary RR **1.03 (0.83-1.28), P=.78** agrees across the abstract, Results text, Table 3, Figure 2 (estimate/CI), and Supplement 3 eFigure 3 (estimate/CI). Per-protocol RR **1.00 (0.80-1.25), P=.98** in the main text agrees with eFigure 3's estimate/CI.
- **Repeated secondary estimates:** Main Table 3 and Supplement 3 eTable 2 agree after rounding for SF-12 day-30 PCS (**-0.86 [-2.83 to 1.11], P=.39**) and MCS (**-1.90 [-4.28 to 0.47], P=.12**). LOS, pain, wound-complication, and readmission estimates repeated in the main narrative also agree with Table 3.
- **Effect direction:** Table 3, Figure 2, and Supplement 3 eFigure 3 consistently label RR <1 as favoring iNPWT. Displayed forest-plot points and CIs correspond to their printed values. Supplement 3 eTables 2-4 consistently define positive mean differences as favoring iNPWT; displayed estimate signs are compatible with that convention.
- **Supplementary SSI reconstruction:** Supplement 3 eTable 6 reconstructs the main primary-event numerators: iNPWT **109 + 0 + 3 = 112** and control **107 + 1 + 0 = 108**.
- **Subgroup results:** All Figure 2 interaction P values are above .05 and therefore correspond to the narrative that there was no evidence of treatment-effect heterogeneity. Missing subgroup classifications prevent event-count sums from always reaching 112/108 but do not create a stated denominator contradiction.

## Result

- **Document-verifiable candidate count:** 2
- **Uncertain, model/time-window-dependent leads:** 2
- **No additional statistical reporting candidates identified.**
