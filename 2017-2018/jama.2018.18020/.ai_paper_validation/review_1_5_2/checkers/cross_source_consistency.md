# Cross-Source and Repeated-Location Consistency Review

## Scope, evidence, and decision rule

This independent cross-source review covered every fresh mapped relationship: numeric/reporting `N001` through `N035` and `N501` through `N522` (57 records), and inferential/statistical `S001` through `S022` and `S501` through `S534` (56 records). It used only the current fresh evidence maps and their linked native/layout text and rendered pages for DOC-001 through DOC-004. No legacy audit output or external source was used.

Before comparison, each occurrence was matched on population, analysis set, time window, treatment contrast, outcome/scale, model, adjustment, reference direction, and displayed precision. Prospective DOC-002 protocol quantities and simulations were treated as plans/design operating characteristics, not as observed 2018 trial results. Bayesian credible-interval/posterior results were not compared as if they were frequentist estimates/P values. A coherent display-zero P value was not treated as a candidate; no such display-zero P-value-only observation was registered.

`CROSS` labels below are provisional checker identifiers only. They are not stable candidate IDs and every observation remains pending human adjudication.

## Complete matched-family coverage

| Matched family and exact relationship coverage | Comparison result |
|---|---|
| Participant flow, enrolled baseline population, dose/schedule, outcome scale/threshold, treatment sets, missing calls/assessments, individual responder counts, and Bayesian group results: N001, N002, N003, N004, N005, N006, N007, N008, N009, N010, N011, N012, N013, N030, N031, N032, N033, N034, N035; S001, S002, S003, S004, S005, S007, S008 | All matched counts, treatment-set identities, effect directions, values, intervals, and posterior probabilities reconcile at their stated analysis level, except the specific abstract sex-label observation CROSS-001 and the `CLNC1` label observation CROSS-002 below. The 3.06 Bayesian and 3.12 frequentist stiffness effects are different models/estimands and are not a conflict. |
| Baseline Table 1 and Table 2 rows, footnotes, scales, directions, subgroup rows, captions, and narrative repetitions: N014, N015, N016, N017, N018, N019, N020, N021, N022, N023, N024, N025, N026, N027, N028, N029; S006, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022 | Checked against the corresponding main-text statements and table/footnote definitions. Values, signs, reference directions, intervals, and P values match under the stated mixed-model or dependent-t-test context. No additional cross-source candidate. |
| Protocol design, schedule, endpoint definitions, planning/sample-size quantities, safety background, DSMB thresholds, and recruitment/model/interim definitions: N501, N502, N503, N504, N505, N506, N507, N508, N509, N510; S534 | All comparisons were context-qualified as prospective protocol versus published results where applicable. Planned n=30, 1-4 sets, the 0.75-point threshold, dose, and interim-rule definitions are not conflicts with the observed enrolled n=30/analyzed n=27 trial. Internal protocol component totals checked in scope reconcile. |
| Supplement baseline array, adverse-event table/figure, treatment-set figure, group posterior figure, individual/total Bayesian models, and simulation tables: N511, N512, N513, N514, N515, N516, N517, N518, N519, N520, N521, N522; S501, S502, S503, S504, S505, S506, S507, S508, S509, S510, S511, S512, S513, S514, S515, S516, S517, S518, S519, S520, S521, S522, S523, S524, S525, S526, S527, S528, S529, S530, S531, S532, S533 | Baseline n=30 versus interim-analysis n=27 is explained by the three recorded dropouts. eTable 4 count/percentage pairs use n=30 and agree with the abstract/main adverse-event figures; the patient-7 toxicodermia figure agrees with the serious-reaction row. eFigure 1, eTable 3, and the main article agree on four patients with two sets and 23 with one. eFigure 2 agrees with the main Bayesian probabilities. Individual eTable 3 entries match the stated threshold/action rules, including the explicit patient-11 prior explanation. Simulation counts/totals/power/bias reconcile. Three model-definition label discrepancies and their repeated locations are recorded as CROSS-003 through CROSS-005. DOC-004 has no quantitative result to match. |

## Provisional qualifying observations

### CROSS-001 — Abstract sex count is printed as a percentage rather than the matching count

- **Category:** Denominator, proportion, or total inconsistency; Cross-document numeric inconsistency.
- **Exact linked locations:** [DOC-001 — PDF p. 1](../../../jama_stunnenberg_2018_oi_180136.pdf#page=1), Abstract Results: “Among 30 enrolled patients ... 22% men”; [DOC-001 — PDF p. 4](../../../jama_stunnenberg_2018_oi_180136.pdf#page=4), Baseline Data: “Twenty-two men and 8 women”; [DOC-001 — PDF p. 5](../../../jama_stunnenberg_2018_oi_180136.pdf#page=5), Table 1, CLCN1 men 13 (81%) and SCN4A men 7 (64%).
- **Printed values and comparison:** The abstract prints `22% men` for 30 enrolled patients. The main narrative prints `22 men and 8 women`; Table 1 prints 13+7=20 men among the 27 analyzed genotype-subgroup patients, a distinct analysis set and therefore not the comparator for the abstract.
- **Comparison logic:** For the same enrolled n=30 population, 22 men is 73.3%, whereas 22% corresponds to 6.6 persons and cannot be the count statement printed in the narrative. The enrolled-sex components in the narrative reconcile: 22+8=30.
- **Supported alternative interpretation:** The abstract may have intended `22 men`, with a percent sign introduced in error. It may instead have intended a percentage but the supplied package contains no enrolled-population male count consistent with 22%.
- **Human verification steps:** Check the publisher PDF/source typesetting for the abstract Results sentence and the author-approved enrollment dataset or proof. Confirm whether the intended field is `22 men` or a separately defined percentage.

### CROSS-002 — One main-text genotype label is printed as CLNC1 while the matched subgroup is CLCN1

- **Category:** Measure, label, or scale inconsistency.
- **Exact linked locations:** [DOC-001 — PDF p. 4](../../../jama_stunnenberg_2018_oi_180136.pdf#page=4), Primary Outcome: “3.84 ... for the `CLNC1` genotype subgroup (n = 16)”; [DOC-001 — PDF p. 5](../../../jama_stunnenberg_2018_oi_180136.pdf#page=5), Table 1 and Figure 2 labels: `CLCN1`; [DOC-001 — PDF p. 6](../../../jama_stunnenberg_2018_oi_180136.pdf#page=6), Figure 3 caption: `CLCN1`, n=16; [DOC-003 — PDF p. 4](../../../joi180136supp2_prod.pdf#page=4), eTable 2 footnote: `CLCN1` is the skeletal muscle chloride-channel gene.
- **Printed values and comparison:** The p.4 narrative attaches the 3.84 (95% CrI 2.52-5.16; n=16) subgroup result to `CLNC1`. The same n=16 subgroup and matching result displays use `CLCN1` elsewhere.
- **Comparison logic:** The identical population, estimate, interval, and n identify the same genotype subgroup; the character order in the p.4 label differs (`CLNC1` versus `CLCN1`).
- **Supported alternative interpretation:** This is likely a transposition in a single narrative label. The supplied package does not establish a distinct `CLNC1` subgroup.
- **Human verification steps:** Verify the p.4 result sentence against the Figure 2/3 source labels and the participant genotype table; confirm the intended gene symbol in the final published record.

### CROSS-003 — Bayesian hierarchical-model parameter definitions reverse placebo and mexiletine labels

- **Category:** Measure, label, or scale inconsistency.
- **Exact linked locations:** [DOC-003 — PDF p. 11](../../../joi180136supp2_prod.pdf#page=11), eMethods 2 code: `Stiff_Plac[i,t] ~ dnorm(mu_plac[i],...)`, `Stiff_Mex[i,t] ~ dnorm(mu_mex[i],...)`, and `diff_patient[i] <- mu_plac[i] - mu_mex[i]`; on the same page, parameter-definition text says `mu_mex[i]` is the placebo-treatment mean and `mu_plac[i]` is the mexiletine-treatment mean. [DOC-003 — PDF p. 14](../../../joi180136supp2_prod.pdf#page=14), eMethods 3 repeats the same code mapping and reversed explanatory labels.
- **Printed values and comparison:** In both models, the code binds placebo observations to `mu_plac[i]` and mexiletine observations to `mu_mex[i]`. The adjacent prose assigns the opposite treatment labels to those two parameter names.
- **Comparison logic:** Under the displayed likelihood equations, `mu_plac[i]` is the placebo mean and `mu_mex[i]` is the mexiletine mean. Reversing those labels changes the stated meaning of the individual-level quantities and conflicts with the displayed `placebo minus mexiletine` effect direction.
- **Supported alternative interpretation:** The code and the population-level `mu.plac`/`mu.mex` definitions are mutually consistent, so the explanatory rows may be swapped rather than the executed code being wrong. The supplied package does not expose an execution log to prove which text/code version was used in computation.
- **Human verification steps:** Compare the submitted WinBUGS files or archived analysis code with eMethods 2/3, confirm treatment-variable encoding, and determine whether the parameter-definition rows should be exchanged in both locations.

### CROSS-004 — `sigma.mex` is described as a placebo-period standard deviation in two Bayesian-method displays

- **Category:** Measure, label, or scale inconsistency.
- **Exact linked locations:** [DOC-003 — PDF p. 12](../../../joi180136supp2_prod.pdf#page=12), eMethods 2: `sigma.mex` is followed by “Standard deviation ... during placebo treatment”; [DOC-003 — PDF p. 11](../../../joi180136supp2_prod.pdf#page=11), code defines `tau.mex <- 1/(sigma.mex*sigma.mex)` next to the mexiletine population parameter `mu.mex`. [DOC-003 — PDF p. 14](../../../joi180136supp2_prod.pdf#page=14), eMethods 3 repeats the `sigma.mex`/“during placebo treatment” definition while the same display defines `mu.mex_SCN4A` and `mu.mex_CLCN1` as mexiletine-treatment means.
- **Printed values and comparison:** The two prose rows label `sigma.mex` as placebo-period variability; the code/paired population parameter labels use `.mex` for mexiletine.
- **Comparison logic:** The displayed parameter naming and its pairing with `tau.mex`/`mu.mex` support mexiletine-period variability, not placebo-period variability. The printed treatment-period label conflicts with that mapping.
- **Supported alternative interpretation:** The two variance parameters could have been intentionally constrained or otherwise relabeled in unseen analysis materials, but the displayed code has separate `sigma.plac` and `sigma.mex`; no stated equality justifies calling both placebo variability.
- **Human verification steps:** Inspect the analysis code and parameter-output dictionary; confirm the intended treatment-period description for `sigma.mex` in eMethods 2 and eMethods 3.

### CROSS-005 — `diff_CLCN1` is described using the SCN4A subgroup label

- **Category:** Measure, label, or scale inconsistency.
- **Exact linked locations:** [DOC-003 — PDF p. 13](../../../joi180136supp2_prod.pdf#page=13), eMethods 3 code: `diff_SCN4A <- mu.plac_SCN4A - mu.mex_SCN4A` and `diff_CLCN1 <- mu.plac_CLCN1 - mu.mex_CLCN1`; [DOC-003 — PDF p. 14](../../../joi180136supp2_prod.pdf#page=14), explanatory block: `diff_SCN4A` is defined for SCN4A, while the following `diff_CLCN1` row again prints “mu.plac – mu.mex for SCN4A patients.” The p.14 P2/P3 rows separately label CLCN1 probabilities as CLCN1.
- **Printed values and comparison:** The code identifies `diff_CLCN1` as the CLCN1 subgroup contrast. Its prose definition repeats the SCN4A label instead.
- **Comparison logic:** The symbol suffix and the code’s subgroup-specific components require the second contrast to be CLCN1. The repeated SCN4A wording cannot identify both distinct contrasts.
- **Supported alternative interpretation:** This may be a copy-forward labeling error in the `diff_CLCN1` explanatory row. The correct numerical estimates are not printed in that row, and the package alone does not show whether the documentation error affected an analysis export.
- **Human verification steps:** Reconcile the p.14 parameter dictionary against the WinBUGS code and reported CLCN1/SCN4A subgroup effects; confirm that the second explanatory row should say CLCN1.

## No-issue and exclusion record

- The apparent `N=30` baseline/eTable 4 denominator and `N=27` analyzed/interim denominator were not treated as a conflict because the package expressly identifies three dropouts and describes their inclusion/exclusion contexts.
- The 0.75 threshold appears in protocol, main article, and supplement with compatible IVR-point scale/direction after distinguishing prospective design values from observed posterior results.
- The frequentist 3.12-point result, Bayesian 3.06-point result, and prior-RCT 2.69-point result were not treated as disagreements because their analyses/trial contexts differ and are explicitly labeled.
- Patient 11's 38% posterior probability together with “Stopped” was not treated as a conflict: the eTable 3 footnote supplies the specific flat-prior/zero-observed-stiffness explanation, rather than applying the ordinary threshold mechanically.
- No coherent P=0/p=0.000 display was registered as a candidate.

## Limits

This review checks printed consistency and parameter/documentation labels, not raw-data validity or model execution. The supplied package contains no executable WinBUGS input/output files, analysis log, or participant-level treatment-period data; therefore the methods-label observations cannot establish whether any underlying computation was affected.

**Completion:** 15 matched families; 113/113 mapped relationships explicitly covered; 5 provisional qualifying observations; 0 display-zero-P-only candidates.
