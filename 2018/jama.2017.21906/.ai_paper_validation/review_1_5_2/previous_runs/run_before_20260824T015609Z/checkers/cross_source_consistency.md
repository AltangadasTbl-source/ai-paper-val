# Cross-Source Consistency Check

## Scope, method, and result

This check covers all 126 assigned canonical relationships: numeric/reporting IDs N001–N035 and N501–N528, and inferential/statistical IDs S001–S050 and S501–S513. It compared only matched results after checking population, time window, intervention/control contrast, analysis set, model, effect measure, scale, units, reference group, and printed precision. The direct sources were the main article, protocol, SAP, and online supplement. Existing current-run text/layout assets were used; no OCR was run and no prior audit derivative was used as evidence.

Five distinct candidate consistency issues are proposed below. All are **Pending Human Adjudication**; none is a correction, validity decision, or severity judgment.

## Explicit relationship coverage

### Numeric/reporting relationships

- **N001, N002, N003, N004, N005, N006, N007, N008, N009, N010, N011, N012, N013, N014, N015, N016, N017, N018, N019, N020, N021, N022, N023, N024, N025, N026, N027, N028, N029, N030, N031, N032, N033, N034, N035 — COMPLETE.** Compared matched abstract, results narrative, Tables 1–3, Figures 1–3, captions, and table footnotes. Counts, denominators, rounded percentages, outcome definitions, direction labels, and repeated main-paper values were concordant after distinction of crude versus model-derived measures, except the Table 2/narrative comparisons proposed below.

- **N501, N502, N503, N504, N505, N506, N507, N508, N509, N510, N511, N512, N513, N514, N515, N516, N517, N518, N519, N520, N521, N522, N523, N524, N525, N526, N527, N528 — COMPLETE.** Compared protocol/SAP planned quantities and definitions with the support tables and figures. Planned sample-size and interim values were not treated as reported outcomes. Support eTable 1’s group labels and footnote were checked separately (candidate proposal CP-03). The online-supplement graphical displays without exact printed point labels were checked for measure, direction, and scale only. The protocol/SAP versus published definitions and subgroup cut points are proposed below (CP-04 and CP-05).

### Inferential/statistical relationships

- **S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050 — COMPLETE.** Checked all main-paper estimates against their matched repeated displays and named model/scale conventions. Apparent differences between unadjusted proportions and model-derived marginal risk differences were not called discrepancies. Two same-result Table 2/narrative conflicts are proposed in CP-01 and CP-02. The published composite definition and age subgroup labels were compared to SAP definitions in CP-04 and CP-05.

- **S501, S502, S503, S504, S505, S506, S507, S508, S509, S510, S511, S512, S513 — COMPLETE.** Checked planned stepped-wedge/model/interim definitions and all supplied support inferential tables and figure conventions. No display-zero P value occurred. The eTable 1 contrast-footnote conflict is proposed in CP-03; planned-versus-published definitions are proposed in CP-04 and CP-05. No other matched support estimate, interval, OR direction, RD convention, population, or scale conflict was found.

## Candidate-proposal register

### CP-01 — In-hospital beta-blocker adjusted-risk-difference upper CI differs between the table and narrative

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** [Main article, Table 2 — PDF p. 6](../../../jama_huffman_2018_oi_170166.pdf#page=6); [main article, Results narrative — PDF p. 7](../../../jama_huffman_2018_oi_170166.pdf#page=7).
- **Matched result:** In-hospital beta-blocker use among eligible participants without contraindications; intervention versus control; mixed-effects logistic model accounting for hospital clustering and temporal trends; adjusted risk difference in percentage points.
- **Printed values:** Table 2: `6.25% (95% CI, 4.10% to 8.40%)`, OR `1.46 (1.29-1.65)`. Narrative: `6.25% (95% CI, 4.10% to 8.10%)`, OR `1.46 (1.29-1.65)`.
- **Comparison logic:** The population, contrast, estimate, lower CI endpoint, OR, and OR CI are the same, but the risk-difference upper endpoint is printed as `8.40%` in the table and `8.10%` in the narrative. This is not explained by rounding because both locations print hundredths.
- **Supported alternatives:** One occurrence could be a transcription or typesetting error; supplied sources do not identify which endpoint is authoritative.
- **Human verification steps:** Locate the model output or locked analysis table for this row; confirm the upper endpoint and harmonize the table/narrative display if required.

### CP-02 — Discharge beta-blocker adjusted result differs between Table 2 and the narrative

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** [Main article, Table 2 — PDF p. 6](../../../jama_huffman_2018_oi_170166.pdf#page=6); [main article, Results narrative — PDF p. 7](../../../jama_huffman_2018_oi_170166.pdf#page=7).
- **Matched result:** Discharge beta-blocker use among discharged eligible participants; intervention versus control; mixed-effects logistic model accounting for hospital clustering and temporal trends.
- **Printed values:** Table 2: adjusted risk difference `6.69% (95% CI, 4.43% to 8.95%)`, OR `1.48 (1.30-1.68)`. Narrative: adjusted risk difference `6.63% (95% CI, 4.43% to 8.95%)`, OR `1.47 (1.30-1.68)`.
- **Comparison logic:** The displayed analysis context and CI endpoints match, while the narrative changes both the point risk difference (`6.69` versus `6.63`) and OR (`1.48` versus `1.47`). Both are printed to two decimals, so the mismatch is not resolved by the stated display precision.
- **Supported alternatives:** The narrative may be copied from a nearby analysis run while Table 2 may reflect a different run; the supplied package does not establish which printed point estimates are intended.
- **Human verification steps:** Reproduce this row from the finalized analysis output using the Table 2 eligibility definition; compare the stored point estimates before deciding whether either printed location needs amendment.

### CP-03 — eTable 1 labels its complete-versus-missing comparison as an intervention-versus-control difference

- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** [Online supplement 3, eTable 1 — PDF p. 17](../../../joi170166supp3_prod.pdf#page=17); [main article, missing-follow-up narrative referring to eTable 1 — PDF p. 6](../../../jama_huffman_2018_oi_170166.pdf#page=6).
- **Matched result:** eTable 1 columns are explicitly `Complete Follow Up n=21,079` and `Missing Follow Up n=295`; the main narrative describes these same groups as included participants and participants missing follow-up.
- **Printed values:** The eTable footnote says `Difference = intervention minus control`. However, its tobacco values are `30.8%` (complete) and `42.4%` (missing), with a printed difference `11.6%`; this equals missing minus complete, not intervention minus control. The age values `60.6` (complete) and `60.0` (missing), with `-0.6`, likewise match missing minus complete.
- **Comparison logic:** The table’s population columns are follow-up-completion groups, not randomized intervention/control groups. The printed differences numerically follow the table’s column groups, while the footnote assigns a different contrast. This produces a direct label/contrast conflict.
- **Supported alternatives:** The footnote may have been inadvertently carried over from eTable 2, which genuinely uses intervention minus control; alternatively the eTable title or column labels would need source confirmation. The values themselves do not indicate an intervention/control comparison.
- **Human verification steps:** Check the eTable production file and analysis code to identify the intended contrast label; verify whether every displayed eTable 1 difference is missing minus complete before updating any label.

### CP-04 — Published “optimal in-hospital medication” outcome excludes statin, unlike the SAP’s named composite

- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** [SAP, secondary endpoint definition — PDF p. 5](../../../joi170166supp2_prod.pdf#page=5); [main article, secondary-outcome definition — PDF p. 3](../../../jama_huffman_2018_oi_170166.pdf#page=3); [main article, Table 3 footnote — PDF p. 7](../../../jama_huffman_2018_oi_170166.pdf#page=7).
- **Matched result:** The named secondary outcome `optimal in-hospital medication use`.
- **Printed values/statements:** The SAP defines it as aspirin, ADP-receptor antagonist, heparin, **statin**, and beta blocker. The article defines it as aspirin, ADP-receptor antagonist, anticoagulant, and beta blocker and states that in-hospital statin use was predefined but data were not collected. Table 3 uses that latter four-component definition for the reported `31.7%` control and `35.8%` intervention outcome.
- **Comparison logic:** The supplied SAP and article use the same outcome name for different printed component sets: statin is included in the SAP and omitted from the reported composite. The article directly defines its four-component measure and explains that predefined statin data were not collected; the package supplies no amendment or change-control record linking the two definitions.
- **Supported alternatives:** This may be a transparent post-plan operational deviation rather than a numerical transcription issue, because the article states that in-hospital statin data were not collected. The supplied package contains no amendment or finalized analysis-plan documentation that resolves whether the unchanged label was intended.
- **Human verification steps:** Review the finalized protocol/SAP amendment history and data-collection specification to establish whether and when the component set was formally changed.

### CP-05 — Published figure calls its age strata prespecified, but they differ from the SAP’s stated age strata

- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** [SAP, §7.5.2 subgroup analyses — PDF p. 7](../../../joi170166supp2_prod.pdf#page=7); [main article, Figure 3 — PDF p. 9](../../../jama_huffman_2018_oi_170166.pdf#page=9); [main article, Results narrative — PDF p. 9](../../../jama_huffman_2018_oi_170166.pdf#page=9).
- **Matched result:** Age subgroup analysis of 30-day MACE.
- **Printed values/statements:** The SAP specifies age `<65 years and >65 years` for an a priori participant-level subgroup. Figure 3 is titled as analysis by `Prespecified Subgroups` but reports age `<50`, `50-69`, and `≥70` years; the Results narrative calls these prespecified subgroups.
- **Comparison logic:** The analysis sets and age cut points do not match: the SAP describes a two-category 65-year split, while the published figure reports three categories with 50 and 70 cut points. The paper’s “prespecified” label therefore does not match the supplied SAP wording without an unprovided amendment or revised plan.
- **Supported alternatives:** A subsequent prespecified amendment or a separate analysis plan may have changed the cut points; the SAP itself also uses `>65`, which may be an imprecise rendering for `≥65`. Neither possibility explains the displayed 50/70 categories from supplied evidence alone.
- **Human verification steps:** Check dated SAP versions, statistical-analysis archive, and figure-programming specification to establish whether the 50/70 strata were prespecified and whether the figure/narrative should identify the analysis as modified or exploratory.

## Limitations

This was a consistency check, not a raw-data, clinical, or general methodological audit. Model-derived marginal differences were not recomputed from crude displayed percentages, and graphical points without exact printed labels were not treated as numeric comparators. The provided sources contain no analysis-output archive or amendment record, so the authoritative value/definition for each proposal requires human source verification.

## Compact completion record

- **Assigned relationships checked:** 126 of 126.
- **Candidate proposals:** 5 distinct proposals (CP-01 through CP-05), all Pending Human Adjudication.
- **Display-zero P-value records:** None applicable; no candidate was proposed on that basis.
- **Artifact:** `.ai_paper_validation/review_1_5_2/checkers/cross_source_consistency.md`.
