# Statistical consistency checker — DOC-001-MAIN and DOC-006-RESULTS-SUPP

**Checker scope:** Document-grounded audit of statistical reporting relationships in
DOC-001-MAIN (`jama_sarraj_2024_oi_240006_1708623114.96234.pdf`) and
DOC-006-RESULTS-SUPP (`joi240006supp5_prod_1708623115.01733.pdf`) only.

**Evidence used:** The main-text evidence map, result-relevant supplementary evidence map,
page-linked native text, rendered result pages, and the two source PDFs. Protocol, SAP,
administrative files, and external sources were not used.

**Status:** Completed. Seven local candidates are returned: 3 directly verifiable discrepancies,
1 directly verifiable terminology error, 1 bounded narrative-versus-interaction candidate, and
2 CI/model-dependent candidates requiring unrounded or model-level confirmation. No point estimate
was found outside its own reported confidence interval.

## Candidate 1 — “Follow-up imaging” counts are actually baseline core-imaging counts

- **One-sentence issue statement:** The main Results section says follow-up imaging was MRI in
  8 patients and CT in 328, but those exact counts are the baseline modalities used to determine
  ischemic core, while the article and supplement identify 204 patients with MR-DWI follow-up.
- **Category / severity / local status:** Presentation inconsistency / Moderate /
  Directly verifiable candidate.
- **Reported item — exact location:** DOC-001-MAIN, PDF p. 4, Results, paragraph 2:
  “Follow-up imaging modality was MRI in 8 of 336 patients (2%) and CT in 328 of 336 patients
  (98%).”
- **Comparator 1 — exact location:** DOC-001-MAIN, PDF p. 5, Table 1, row
  “Imaging modality used to determine ischemic core volume at randomization”: CT perfusion
  165 EVT + 163 medical management; MR DWI 3 EVT + 5 medical management.
- **Comparator 2 — exact location:** DOC-001-MAIN, PDF p. 9, “Association of Follow-Up Infarct
  Volume and Infarct Growth With EVT Outcomes”: “In patients with MR diffusion follow-up
  (n = 204 [61%])…”
- **Comparator 3 — exact location:** DOC-006-RESULTS-SUPP, PDF p. 51, eTable 11,
  “patients with MR DWI follow-up”: MM N=101, mTICI 0-2a N=24, mTICI 2b-3 N=79.
- **Reproducible reasoning:** Baseline CT-perfusion count = 165 + 163 = 328; baseline MR-DWI
  count = 3 + 5 = 8. MR-DWI follow-up count = 101 + 24 + 79 = 204.
  Also, 8/336 = 2.38% (reported as 2%) whereas 204/336 = 60.71% (reported as 61%).
  Thus, the p. 4 sentence reproduces the baseline modality counts exactly but calls them
  follow-up modalities; it cannot also describe the reported 204-person MR-DWI follow-up cohort.
- **Bounded impact:** The sentence misidentifies the imaging time point and makes the follow-up
  modality denominator appear to be 8 rather than 204, which can mislead interpretation of the
  infarct-growth analysis population. It does not alter the numerical outcome estimates.
- **Human verification steps:**
  1. On DOC-001 PDF p. 4, confirm the printed phrase is “Follow-up imaging modality.”
  2. On DOC-001 PDF p. 5, add the two treatment-column modality counts and confirm 328 CT
     perfusion and 8 MR DWI at randomization.
  3. On DOC-001 PDF p. 9 and DOC-006 PDF p. 51, confirm the MR-DWI follow-up total is 204.
  4. The issue is confirmed if p. 4 says “follow-up” while its values match baseline Table 1
     and conflict with the 204-person follow-up cohort; it is resolved only if an erratum or
     source annotation establishes a different intended time point.

## Candidate 2 — Medical-management infarct-growth IQR differs between main text and cited eTable 11

- **One-sentence issue statement:** For the same MR-DWI follow-up medical-management group, the
  main article reports CTP/MRI-core infarct growth of 95 (IQR 56-125) mL, whereas cited eTable 11
  reports 95 (IQR 56-135) mL.
- **Category / severity / local status:** Cross-document inconsistency / Minor /
  Directly verifiable candidate.
- **Reported item — exact location:** DOC-001-MAIN, PDF p. 9, “Association of Follow-Up Infarct
  Volume and Infarct Growth With EVT Outcomes”: medical management “median, 95
  [IQR, 56-125] mL,” explicitly citing eTable 11.
- **Comparator — exact location:** DOC-006-RESULTS-SUPP, PDF p. 51, eTable 11,
  row “Infarct growth from CTP/MRI core (ml), median (IQR),” MM N=101:
  “95 (56, 135)” mL.
- **Reproducible reasoning:** Main upper quartile = 125 mL; supplement upper quartile = 135 mL;
  difference = 135 − 125 = 10 mL. The median and lower quartile agree, and the main paragraph
  explicitly points to eTable 11, so this is not a comparison of unrelated outcomes.
- **Bounded impact:** Only the upper quartile of one descriptive infarct-growth distribution is
  affected; the median and the other two reperfusion-group summaries agree.
- **Human verification steps:**
  1. Confirm “56-125” in DOC-001 PDF p. 9.
  2. Confirm “56, 135” in DOC-006 PDF p. 51, eTable 11, MM column.
  3. Confirm both refer to infarct growth from baseline CTP/MRI core among MR-DWI follow-up
     patients.
  4. The issue is confirmed if the source PDFs retain the 10-mL upper-quartile difference.

## Candidate 3 — `aRR` is expanded as absolute risk reduction although the reported measure is a risk/rate ratio

- **One-sentence issue statement:** The article repeatedly expands `aRR` as “absolute risk
  reduction,” while its stated model, null value, table footnotes, and companion absolute-risk-
  difference measure show that `aRR` is an adjusted risk/rate ratio.
- **Category / severity / local status:** Presentation inconsistency / Minor /
  Directly verifiable candidate.
- **Method evidence — exact location:** DOC-001-MAIN, PDF p. 4, Statistical Analysis:
  secondary outcomes were evaluated with “modified Poisson regression models with robust
  standard errors.”
- **Mislabelled text — exact location:** DOC-001-MAIN, PDF p. 6, “Association of ASPECTS and CT
  Perfusion/MRI Core Volume With Clinical Outcomes in EVT-Treated Patients”:
  “Functional independence (absolute risk reduction [aRR], 0.89 [95% CI, 0.84-0.95]…).”
- **Mislabelled table definitions — exact locations:** DOC-001-MAIN, PDF p. 7, Table 2
  abbreviations; and PDF p. 9, Table 3 abbreviations: “aRR, absolute risk reduction.”
  Both tables' footnotes nevertheless say “aRR greater than 1 indicates higher rate ratio.”
  Table 3 separately labels `aRD` as “absolute risk difference.”
- **Reproducible reasoning:** A reported aRR of 0.89 with ratio-scale null 1 and modified
  Poisson estimation is a ratio measure; an absolute risk reduction/difference is additive and
  has null 0. Table 3 itself distinguishes `aRR` from `aRD`. The phrase “absolute risk reduction”
  is therefore incompatible with the displayed measure.
- **Bounded impact:** The numerical estimates and CIs need not be wrong, but the expansion can
  cause readers to interpret, for example, 0.89 as an absolute 0.89-unit reduction rather than a
  multiplicative ratio. The same footnote also ties `aRR > 1` to thrombectomy even in medical-care
  and within-arm predictor columns, making comparator direction less clear.
- **Human verification steps:**
  1. Confirm the modified Poisson method on DOC-001 PDF p. 4.
  2. Confirm the “absolute risk reduction” expansion on pp. 6, 7, and 9.
  3. Confirm the same table footnotes call the values “rate ratio” and that Table 3 reports
     `aRD` separately.
  4. The issue is confirmed if all wording remains as printed; it is resolved by defining
     `aRR` as adjusted risk ratio (or the authors' intended ratio term).

## Candidate 4 — Printed ASPECTS CI reaches the null despite a claim of statistical significance

- **One-sentence issue statement:** The main text calls the within-EVT association per 1-point
  ASPECTS decrease statistically significant even though its printed 95% CI is 0.82-1.00 and
  therefore reaches the ratio null of 1.00.
- **Category / severity / local status:** Statistical reporting inconsistency / Minor /
  **Uncertain because of rounding; requires unrounded CI or P value.**
- **Reported item — exact location:** DOC-001-MAIN, PDF p. 6, “Association of ASPECTS and CT
  Perfusion/MRI Core Volume With Clinical Outcomes in EVT-Treated Patients”:
  “decreasing ASPECTS score was associated with significantly worse clinical outcomes within
  EVT-treated patients (aGenOR, 0.91 [95% CI, 0.82-1.00] per 1-point ASPECTS score decrease).”
  The same estimate is in PDF p. 7, Table 2, EVT column.
- **Decision rule — exact location:** DOC-001-MAIN, PDF p. 4, Statistical Analysis:
  “All hypotheses were evaluated using 2-sided tests. P < .05 was considered statistically
  significant.”
- **Reproducible reasoning:** The aGenOR null is 1.00. The printed interval [0.82, 1.00]
  contains/reaches 1.00, while “significantly” implies exclusion of the null under the article's
  two-sided 0.05 rule. However, an unrounded upper bound slightly below 1 could round to 1.00,
  so the package does not establish whether the inference or only the rounded display is wrong.
- **Bounded impact:** The uncertainty concerns the significance adjective for one within-EVT
  ASPECTS association; the point estimate still indicates the reported direction.
- **Human verification steps:**
  1. Confirm the significance wording and 0.91 (0.82-1.00) on DOC-001 PDF p. 6.
  2. Confirm the two-sided P<.05 rule on p. 4.
  3. Obtain the unrounded CI or corresponding P value.
  4. Confirm inconsistency if the unrounded CI includes 1 or P≥.05; resolve it as rounding if
     the unrounded upper limit is <1 and P<.05.

## Candidate 5 — Printed imaging-to-reperfusion CI reaches the null despite a claim of statistical significance

- **One-sentence issue statement:** The main text says independent ambulation decreased
  significantly per 10-minute imaging-to-reperfusion/end-procedure delay, but the printed aRR
  95% CI is 0.93-1.00 and reaches the ratio null.
- **Category / severity / local status:** Statistical reporting inconsistency / Minor /
  **Uncertain because of rounding; requires unrounded CI or P value.**
- **Reported item — exact location:** DOC-001-MAIN, PDF p. 10, “Association of Age and Time With
  Functional Outcome After EVT”: “time from CT perfusion acquisition to reperfusion or end of
  the procedure (aRR, 0.97 [95% CI, 0.93-1.00] per 10-minute increment), the predicted
  probability of achieving independent ambulation significantly decreased.”
- **Decision rule — exact location:** DOC-001-MAIN, PDF p. 4, Statistical Analysis:
  2-sided tests and P<.05 threshold.
- **Reproducible reasoning:** The ratio null is 1.00, and the printed interval [0.93, 1.00]
  reaches it. As in Candidate 4, rounding could conceal an upper bound slightly below 1.
- **Bounded impact:** The issue is limited to the statistical-significance characterization of
  the imaging-to-procedure-time association; it does not change the displayed direction.
- **Human verification steps:**
  1. Confirm the quoted claim and CI on DOC-001 PDF p. 10.
  2. Obtain the unrounded CI or P value for the imaging-to-reperfusion/end-procedure coefficient.
  3. Confirm inconsistency if the unrounded CI includes 1 or P≥.05; resolve it as rounding if
     the unrounded upper limit is <1 and P<.05.

## Candidate 6 — “No effect modification” narrative is not true for the reported NCCT 100-mL analysis

- **One-sentence issue statement:** The main article broadly states that there was no evidence of
  EVT treatment-effect modification by imaging modality, but supplementary eFigure 10 reports
  interaction P=.0164 for the noncontrast-CT hypodensity 100-mL split.
- **Category / severity / local status:** Cross-document inconsistency / Minor /
  Bounded candidate; the intended scope of “either imaging modality” should be confirmed.
- **Narrative evidence — exact location:** DOC-001-MAIN, PDF p. 11, Discussion:
  “While no evidence of EVT treatment effect modification was observed based on either imaging
  modality…” DOC-001 PDF p. 6 also says “Similar results were also observed using composite core
  and CT hypodensity volumes (post hoc) (eFigures 10-13 in Supplement 5).”
- **Comparator — exact location:** DOC-006-RESULTS-SUPP, PDF p. 16, eFigure 10, NCCT
  hypodensity-volume 100-mL rows: <100 mL, n=207, GenOR 2.25 (95% CI 1.65-3.06);
  ≥100 mL, n=129, GenOR 1.25 (95% CI 0.89-1.74); interaction P=.0164.
- **Decision rule — exact location:** DOC-001-MAIN, PDF p. 4: P<.05 was considered statistically
  significant.
- **Reproducible reasoning:** .0164 < .05, so the supplement's reported interaction test is
  evidence of effect modification for this one post hoc NCCT hypodensity threshold. All cited
  values are printed outputs; no CI-symmetry assumption is used.
- **Bounded impact:** The exception is confined to the post hoc NCCT hypodensity <100 versus
  ≥100 mL ordinal-mRS analysis. It does not establish effect modification for CTP/MRI core,
  composite core, other thresholds, or secondary outcomes.
- **Human verification steps:**
  1. Confirm the main Discussion wording on DOC-001 PDF p. 11.
  2. Confirm the NCCT labels, two GenORs, and interaction P=.0164 in DOC-006 PDF p. 16.
  3. Determine whether “either imaging modality” was intended to include the reported
     NCCT-hypodensity sensitivity analyses.
  4. Confirm the issue if the narrative was intended as a summary of all reported imaging
     analyses; resolve it by explicitly limiting the narrative to prespecified ASPECTS and
     CTP/MRI-core analyses.

## Candidate 7 — A relative risk is displayed for a subgroup with zero events in both arms without an explained estimand

- **One-sentence issue statement:** Supplementary eFigure 7 reports RR 1.00 (95% CI 0.37-2.72)
  for ASPECTS 0-2 even though the displayed functional-independence event counts are zero in both
  arms, and the package does not explain how that zero-event subgroup estimate was obtained.
- **Category / severity / local status:** Statistical reporting inconsistency / Minor /
  **Uncertain; model code or a zero-cell rule is necessary.**
- **Reported item — exact location:** DOC-006-RESULTS-SUPP, PDF p. 13, eFigure 7, ASPECTS 0-2
  (n=19): thrombectomy 0 (0.00%), medical management 0 (0.00%), “Relative Risk (95% CI)”
  1.00 (0.37-2.72).
- **Method evidence — exact location:** DOC-001-MAIN, PDF p. 4, Statistical Analysis states that
  secondary treatment effects within subgroups used modified Poisson regression with robust
  standard errors. eFigure 7 does not label the displayed RR as adjusted or state a zero-cell or
  continuity rule.
- **Reproducible reasoning:** From the displayed subgroup counts, crude risk in each arm is
  0/denominator; their ratio is (0/denominator)/(0/denominator) = 0/0, which is undefined.
  A model-based marginal RR may differ from the crude ratio, but its covariate specification and
  zero-event handling are not reported beside the estimate and cannot be reproduced from the
  article package.
- **Bounded impact:** This affects only the eFigure 7 functional-independence estimate for the
  19-patient ASPECTS 0-2 subgroup; the figure's observed event counts remain zero in both arms.
- **Human verification steps:**
  1. Confirm both zero counts and RR 1.00 (0.37-2.72) in DOC-006 PDF p. 13.
  2. Inspect the analysis output/code for the subgroup-specific modified Poisson model,
     covariate adjustment, and any continuity or penalization rule.
  3. Reproduce the point estimate and CI from that stated procedure.
  4. Confirm a reporting problem if the RR cannot be reproduced or is merely a placeholder;
     resolve the candidate if a prespecified estimable model-based RR and its calculation are
     documented.

## Checks completed without a reportable inconsistency

- Every transcribed point estimate was within its own reported CI.
- Ratio CIs that clearly excluded 1 were directionally coherent with claims of significance;
  CIs that clearly included 1 were not otherwise called significant, apart from the two
  boundary-at-1.00 candidates above.
- Main Figure 1 estimates and interaction P values matched their repetitions in the abstract and
  Results text.
- Main mismatch counts, trend P values, and treatment-effect estimates matched the result-relevant
  supplementary figures/tables where the same analysis and analysis set were identifiable.
- The differing follow-up-infarct-volume IQRs in main p. 9 and supplementary eTable 2 were not
  promoted as a candidate because eTable 2 is explicitly intention-to-treat while the main
  post hoc paragraph does not state an analysis set; the necessary same-estimand link is absent.
- CI symmetry was not used as an error test.

