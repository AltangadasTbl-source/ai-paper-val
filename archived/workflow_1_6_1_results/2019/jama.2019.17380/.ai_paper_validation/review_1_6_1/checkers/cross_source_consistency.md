# Cross-source consistency review

Scope: all matched result and planned-versus-reported relationships in DOC-001 PDF pages 1–11, DOC-002 PDF pages 1–33, DOC-003 PDF pages 1–19, and DOC-004 PDF page 1 (64 pages). DOC-001, DOC-003 and DOC-004 are REPORT; the entire DOC-002 bundle, including its implemented analytic addendum, is PLAN. No supplied structured data, workbook, CSV or Office source exists. The complete current main and support maps supplied the page accounting, relationship bundles, full table transcriptions and graphical transcriptions. Source-matched reusable Poppler text and page renders served only as evidence aids; direct selected-page `pdftotext -layout` and visual source-page renders confirmed the locations below. No old scientific conclusions or web evidence were used. No source or reusable asset was modified. No fresh persistent derivative was needed.

The implemented addendum (submitted March 2, 2015; implemented February 24, 2016) supersedes the original primary endpoint, follow-up schedule, primary model, missing-data approach and power assumptions. Comparisons below use that addendum wherever applicable. Findings are self-screened proposals for independent inclusion screening, with no candidate IDs or adjudications.

## Coverage and matched comparisons

| Relationship family | Compared scope | Result of cross-source check |
|---|---|---|
| Primary five-year eGFR results | Main abstract p1, Key Points p2, Results p4, Table2 p8, Figures3–4 pp8–9, discussion pp6–10 | Active changes −12.3 vitamin D/−12.2 omega-3, placebo −13.1, differences 0.9 with CIs −0.7 to2.5/−0.7 to2.6 and nonsignificance agree. Forest counts require the consolidated finding below. |
| Primary sensitivity analyses | Main pp3–4,6; supplement eTables4–5 pp9–10 | Complete-case N932 and displayed tuples reconcile with the flow; adherence analysis population definition differs from the implemented plan. Different sensitivity estimates are different analysis populations, not repeated primary estimates. |
| Secondary results and hierarchy | Main pp3–4,9, supplement eTables6–10 pp11–15 and eFigures2–3 pp18–19; plan pp17–20,32–33 | Composite HR0.92/1.11 and event total164 agree. eGFR threshold≥40%, composite kidney failure/death, five-year continuous ACR and geometric change direction match applicable plan context. ACR sensitivity population count needs review. Exploratory ≥30% variants are explicitly post hoc. |
| Participant flow, safety and adherence | Main pp1,4–6,10; supplement pp6–8,16 | Randomized1312, four arms370/333/289/320, follow-up blood1090, final blood934, final urine945, complete-case eGFR932, deaths80 and adverse-event examples agree. Questionnaire-response denominators explain per-time adherence percentages. |
| Primary model, covariates, analysis population and imputation | Plan addendum p32, main p3 and Table2 p8 | Random intercept, categorical0/2/5 time, treatment×time, five-year test and Rubin combination agree; primary analysis population and routine primary covariates differ. Ten versus20 imputations is separately excluded below. |
| Intervention interaction and multiplicity | Plan pp18,23,32–33; main pp3–4,8–9 | No detected interaction P=.42 supports pooled comparisons under addendum rule. Two-sided .05 per intervention agrees; secondary analyses explicitly exploratory. Parent-trial DSMB guidance is not interpreted as a DKD-specific stopping rule. No noninferiority/equivalence margin is stated or applicable. |
| Sample size and power | Original plan pp19–20, addendum p33, main pp2–3,6–7 | Addendum assumptions80% retention, simulation2000, power80%, detectable2.3 and two-sided .05 reconcile with reported target1320. Original N1500/90%/four-year assumptions are superseded. Absent preliminary variance inputs limit numerical reproduction. |
| Subgroups and other sensitivity specifications | Plan pp18–19,33; main pp3–4,8–9; supplement pp10,13–14,17–19 | ACR/eGFR/race/total25(OH)D and omega-3/CRP subgroups align. BMI and fish-intake additions are disclosed. Adherence threshold differs. Unreported bioavailable25(OH)D and exploratory biomarker model details are excluded rather than assumed to establish an undisclosed primary-result replacement. |
| Endpoints, dose and duration | Plan pp4,11–17,31–33; main pp1–3 | Amended five-year primary outcome reconciles; vitamin D2000IU/day and omega-3 totalEPA+DHA840mg/day agree. Original unit/ratio wording is contextually resolved. Formula identity cannot be established from the report's named equation alone. |
| Other units | Main p11; protocol background/administration/references pp1–10,21–30; supplement identity/laboratory/references pp1–5; data-sharing p1 | All units accounted for in current maps. Historical studies are not current trial results. Laboratory harmonization is disclosed in main/supplement context; data-sharing statement contains no independent result or analysis-plan comparator. |

## Findings

### F-XS-001

**Title:** Forest-plot participant counts do not align with their treatment columns across both interventions.

**Locations and roles:** REPORT [main Table1](../../../jama_de_boer_2019_oi_190122.pdf#page=5), [Figure1](../../../jama_de_boer_2019_oi_190122.pdf#page=6), [Table2 and Figure3](../../../jama_de_boer_2019_oi_190122.pdf#page=8), [Figure4](../../../jama_de_boer_2019_oi_190122.pdf#page=9); REPORT [supplement eFigure2](../../../joi190122supp2_prod.pdf#page=18), [eFigure3](../../../joi190122supp2_prod.pdf#page=19), [eTable6](../../../joi190122supp2_prod.pdf#page=11) and [assignment headings in eTable11](../../../joi190122supp2_prod.pdf#page=16).

**Printed values and comparison logic:** Figure1 and Table1 give four randomized arms370 D+omega,333 D+placebo,289 placebo+omega,320 double placebo. Thus activeD703/placeboD609 and activeomega659/placeboomega653. Figure3 instead prints overall Placebo703 and VitaminD609, alongside placebo mean change−13.1 and vitamin-D mean−12.3. Figure4 prints Placebo659 and Omega-3 Fatty Acids653, alongside placebo−13.1 and active−12.2. Those means match the Table2 treatment labels; the participant counts match the opposite assignments. The same overall N pattern occurs in supplementary ACR eFigures2–3, while eTable6 overall geometric changes3.02/2.97 (D placebo/active) and3.05/2.94 (omega placebo/active) match the forest means under their printed treatment headings.

All affected count rows are consolidated here: main Figure3 and supplement eFigure2, overall, White, Black, ACR<30/≥30, vitamin-D<20/20–<30/≥30, eGFR≥60/<60, BMI<25/25–<30/≥30, other-intervention placebo/active; main Figure4 and supplement eFigure3, overall, EPA/DHA≤2.2/>2.2, ACR<30/≥30, hsCRP≤0.2/>0.2, fish<1.5/≥1.5, other-intervention placebo/active. Equal count pairs do not themselves establish a difference but remain occurrences within the same column pattern. For example Table1 White counts240+211=451 activeD and199+207=406 placeboD appear as451 Placebo and406 VitaminD in Figure3; vitamin-D<20 counts62+48=110 activeD and41+44=85 placeboD similarly appear as110 Placebo and85 VitaminD. The last Figure3 rows print333/320 under omega-placebo and370/289 under omega-active, again activeD count first under the Placebo heading. Exact counts have no rounding allowance.

**Focus area:** A. **Proposed review domain:** statistical_results. **Proposed primary relationship:** S_C. **All relationships:** S_C, S_W.

**Affected result or extracted value:** Treatment-specific and subgroup-specific analysis counts accompanying the five-year eGFR and ACR effect estimates, including overall vitamin-D and omega-3 analysis populations.

**Why context does not resolve it:** Other locations establish randomized totals and corroborate overall treatment means, but the forest panels pair counts from one assignment with means under the other heading. A reader cannot establish solely from the panels whether every subgroup count, mean/SD, or column alignment follows the same assignment. Identifying a repeated transposition is an inferred explanation, not a source-supplied definition of the subgroup analysis population.

**Supported alternatives:** The counts may have been laid out in active-first order under placebo-first headings while means follow the headings; alternatively some broader subgroup alignment could differ. The source does not specify which component was transposed. No reversal of the primary effect estimates is inferred.

**Human verification steps:** Compare every count column with treatment-specific baseline subgroup totals and the analysis output for all four forest displays; establish the population associated with each mean/SD and plotted effect before extracting subgroup data.

### F-XS-002

**Title:** The implemented plan and report use different primary analysis populations.

**Locations and roles:** PLAN [addendum §15c](../../../joi190122supp1_prod.pdf#page=32) and [addendum implementation cover](../../../joi190122supp1_prod.pdf#page=31); REPORT [Data Analysis](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [retention and primary results](../../../jama_de_boer_2019_oi_190122.pdf#page=4), [Figure1](../../../jama_de_boer_2019_oi_190122.pdf#page=6), [Table2](../../../jama_de_boer_2019_oi_190122.pdf#page=8).

**Printed values and comparison logic:** Addendum §15c defines intent-to-treat inclusion as “all participants who return at least one follow-up biosample.” Report p3 says all randomized participants are analyzed “regardless of adherence or follow-up (full analytic population).” Figure1 confirms370+333+289+320=1312 included in the primary analysis, despite only303+280+242+265=1090 returning at least one follow-up blood sample. Report p4 gives1091 with at least one follow-up urine sample. Even the maximum blood/urine union allowed by these marginal counts is1312, so the actual union size is not supplied; the definitions nevertheless differ explicitly, and eGFR blood-specific retention leaves222 without a follow-up blood measurement. The finding rests on the conflicting inclusion rules and confirmed full randomized analysis, not on assuming blood/urine overlap or an exact plan-eligible union count.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship/all relationships:** P_R.

**Affected result or extracted value:** The population underlying both imputed five-year primary eGFR differences0.9 mL/min/1.73m² and their CIs, including the analysis-population size extracted as1312.

**Why context does not resolve it:** Both documents use intent-to-treat language, but one conditions inclusion on a postrandomization biosample while the report includes everyone irrespective of follow-up. The disclosed endpoint/time amendment does not disclose superseding §15c's biosample condition; the addendum itself is the implemented comparator. The report clearly identifies the actual analysis, but does not reconcile its population with the supplied implemented plan.

**Supported alternatives:** A later population amendment may have extended inclusion to all randomized participants; alternatively the published imputation analysis may be a change from the supplied addendum. A later amendment is not supplied. Exact overlap between blood and urine returners is unreported and not assumed.

**Human verification steps:** Establish the operational population prescribed by §15c, determine the eligible biosample union, and identify any later amendment covering participants with no follow-up outcomes.

### F-XS-003

**Title:** Routine primary-model covariates in the report are absent from the implemented primary hypothesis model.

**Locations and roles:** PLAN [addendum §15e Equation2](../../../joi190122supp1_prod.pdf#page=32); REPORT [Data Analysis](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [Table2 footnote a](../../../jama_de_boer_2019_oi_190122.pdf#page=8); REPORT [eTables4–5](../../../joi190122supp2_prod.pdf#page=9) and [adherent eGFR analysis](../../../joi190122supp2_prod.pdf#page=10) corroborate the reported adjustment.

**Printed values and comparison logic:** The addendum primary Equation2 includes intercept, treatment, categorical time, treatment×time, participant random effect and residual. Additional baseline-characteristic terms are described as sensitivity analyses conditional on imbalance. Report p3 instead includes linear age, sex, age×time and sex×time in the primary models; eGFR additionally includes baselineACR and ACR×time. Table2 states its primary estimates derive from adjustment for age, sex and baselineACR. These are explicitly routine primary terms rather than the addendum's conditional sensitivity additions. The same difference applies to both primary intervention contrasts.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship/all relationships:** P_R.

**Affected result or extracted value:** The model specification producing primary five-year eGFR differences0.9 (−0.7,2.5), P=.25 for vitamin D and0.9 (−0.7,2.6), P=.27 for omega-3.

**Why context does not resolve it:** The source supplies a concrete primary equation and separately assigns additional baseline adjustment to sensitivity analyses. The report supplies a concrete expanded primary model. No supplied addendum or immediate report context states that routine primary covariate adjustment replaced the printed primary hypothesis equation. Random-intercept and categorical-time agreement does not make the adjustment specifications equivalent.

**Supported alternatives:** The report may implement a later expanded primary specification, or may present a covariate-adjusted sensitivity specification as its primary analysis. The package does not identify an additional covariate amendment. No numerical effect of the added terms is assumed.

**Human verification steps:** Compare the implemented primary model formula and analysis code with Equation2; identify any prospective covariate amendment and establish whether the reported tuples were designated primary or sensitivity results.

### F-XS-004

**Title:** The reported adherent sensitivity population differs from the implemented plan's adherence restriction.

**Locations and roles:** PLAN [original exploratory restriction](../../../joi190122supp1_prod.pdf#page=19), [addendum §15g](../../../joi190122supp1_prod.pdf#page=33); REPORT [Covariates and Data Analysis](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [primary robustness narrative](../../../jama_de_boer_2019_oi_190122.pdf#page=4), [eTable1 definition](../../../joi190122supp2_prod.pdf#page=6), [eTable5 footnote](../../../joi190122supp2_prod.pdf#page=10) and [eTable8 footnote](../../../joi190122supp2_prod.pdf#page=13).

**Printed values and comparison logic:** Original plan≥80% adherence is retained and made explicit as “continuous adherence to ≥80%” in addendum §15g. Report defines high adherence as use at least two-thirds of the time, and eTables5/8 specify this self-report on at least4 of6 questionnaires at6months and years1–5, N1032 per intervention. These are different medication-use thresholds and different continuity requirements; ≥2/3 at4/6 assessments does not imply continuous≥80%. A hypothetical participant reporting70% at four assessments would meet the printed report rule but not the printed plan rule; this illustrates logical nonequivalence only, without asserting that such a participant exists in the trial.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship/all relationships:** P_R.

**Affected result or extracted value:** Primary eGFR adherence sensitivity differences vitaminD0.89 (−0.74,2.52), P=.28 and omega-3 0.42 (−1.22,2.06), P=.61, and the statement that null primary findings remain similar among consistently highly adherent participants. ACR adherence analyses use the same changed restriction.

**Why context does not resolve it:** Both source versions specify the restriction prospectively, and the reported footnotes specify the actual restriction. The numerically distinct thresholds and assessment requirements cannot be resolved as two names for the same population. No supplied amendment changes §15g's adherence criterion; consequently the reported robustness check cannot be identified as the planned ≥80% restriction.

**Supported alternatives:** A later amendment may have adopted the questionnaire-based two-thirds rule; alternatively the reported sensitivity analysis may replace the planned continuous≥80% analysis. The size and results of the latter population are not supplied and are not estimated.

**Human verification steps:** Confirm the operational adherence variable, locate any threshold amendment and compare which participants entered the planned and reported restrictions. Do not infer that the conclusions would differ.

### F-XS-005

**Title:** The ACR complete-case analysis has two incompatible reported sample-size constructions.

**Locations and roles:** REPORT [supplement eTable7 title, rows and footnote](../../../joi190122supp2_prod.pdf#page=12); REPORT [main retention narrative](../../../jama_de_boer_2019_oi_190122.pdf#page=4) provides additional context for final urine return.

**Printed values and comparison logic:** The table title specifies N944. Baseline and year5 rows total504+440=944 for vitaminD and477+467=944 for omega-3. Footnote states1311 baseline urine contributors,991 of these included at year5, and320 excluded for lacking year5 urine;1311−320=991. Thus two internally coherent constructions differ by47: table944 versus footnote991. The main narrative reports945 final urine samples, which is compatible with944 participants having both measurements but does not explain why the footnote explicitly assigns991 to this analysis. All counts are integers; rounding is not applicable.

**Focus area:** A. **Proposed review domain:** statistical_results. **Proposed relationship/all relationships:** S_W.

**Affected result or extracted value:** The complete-case analysis-population size attached to ACR sensitivity ratio1.03 (0.86,1.22), P=.77 for vitaminD and0.93 (0.78,1.11), P=.44 for omega-3.

**Why context does not resolve it:** The title and repeated rows support944, while the footnote explicitly says991 were included and supplies a mutually consistent exclusion count320. Determining which analysis generated the reported effect tuples requires choosing between these population descriptions; this is more than an isolated glyph or a peripheral per-time contributor difference.

**Supported alternatives:** The footnote may retain a different population description; alternatively additional eligibility exclusions could reduce991 to944 without being specified. The printed table does not identify such exclusions.

**Human verification steps:** Confirm the analytic membership and model N for eTable7, reconcile baseline1311, final945, footnote991 and excluded320, and identify any additional exclusions.

## Excluded observations

Each row records one consolidated observation and exactly one scope reason code. Reconciled matching results are documented in coverage above rather than assigned findings.

| Location | Observation | Reason code |
|---|---|---|
| PLAN pp17–20 vs addendum pp31–33; REPORT pp2–3 | Original ACR/four-year endpoint, ANCOVA/complete-case/composite definitions and N1500/90% power differ from five-year eGFR/LMM/imputation/N1320/80%; implemented addendum discloses the changes. | CONTEXT_RESOLVES |
| PLAN original pp4,11–15 vs addendum p32 | Original four-year biosample schedule versus addendum's reference to two-year antecedent schedule is version history, without a conflict in the implemented five-year result or decision rule. | PERIPHERAL_COMPARISON |
| PLAN pp19,33 | Original non-Caucasian directional hypothesis versus Caucasian in later addendum is an explicitly later plan version; reported two-sided subgroup analyses do not select either directional claim. | CONTEXT_RESOLVES |
| PLAN p32; REPORT p3 | Ten versus20 imputation datasets is a transparent change in repetition count; no source establishes that this difference changes a reported interpretation or extracted effect. Population change is separately raised above. | CONTEXT_RESOLVES |
| PLAN p32; REPORT p3 | Additional imputation predictors and detailed missingness mechanisms cannot be compared because the report does not supply the corresponding full chained-equation specification. | CONDITIONAL_OR_UNREPORTED |
| PLAN p32 Equation1 versus Equation2 | Interaction equation does not separately print a time-only term; its categorical-time model context and complete primary Equation2 make the intended time structure identifiable. No contradictory reported interaction-model output is supplied. | NOTATION_OR_TYPOGRAPHY |
| PLAN p33; REPORT pp3–4 and supplement p17 | Planned biomarker substitution in mixed models versus displayed marker correlations concerns exploratory association displays and does not establish a replacement of the primary or key secondary treatment result. | PERIPHERAL_COMPARISON |
| PLAN p33; REPORT pp3,8 | Bioavailable25(OH)D subgroup result is not printed; the source does not establish a measured biomarker or a different primary result from its omission. | CONDITIONAL_OR_UNREPORTED |
| REPORT p3; PLAN p33 | BMI and fish-intake subgroup additions are explicitly disclosed following parent-trial findings. | CONTEXT_RESOLVES |
| REPORT Figure2 p7 vs Table2 p8/eTable6 p11 | Omega-3 panels repeat vitamin-D per-time observation counts; matched analysis-population N and primary estimates remain specified elsewhere. These are individual time-point contributor displays. | PERIPHERAL_COMPARISON |
| REPORT eFigures2–3 pp18–19 versus eTable6 p11 | “Favors” arrows point toward higher active/placebo ACR ratio; explicit ratio labeling, numerical group changes and clinically interpretable lower albuminuria resolve the intended quantity immediately. No alternative numerical ratio is extracted from these arrows. | CONTEXT_RESOLVES |
| REPORT eFigures2–3 captions pp18–19 | Caption calls ratio a difference and says comparison to year5; plot explicitly labels ratio of change active/placebo with null1, making the measure and contrast apparent. | TERMINOLOGY_OR_WORDING |
| REPORT eFigure2 p18 versus eTable6 p11 | Overall .89 beneath interaction heading versus primary .90 cannot be equated with an established identical test/precision; both are clearly nonsignificant and values to extract are supplied in eTable6. | CONTEXT_RESOLVES |
| REPORT eFigure1 p17 axis versus caption/main pp3–4 | “DHA/EPA” shorthand versus omega-3 index/EPA+DHA wording occurs in an exploratory marker display and does not alter a primary or key secondary result. | PERIPHERAL_COMPARISON |
| REPORT Tables2/eTables4–9 | Differences between modeled changes and subtraction/ratios of observed means are model summaries with imputation and adjustment, not crude differences from identical observed contributors. | MODEL_VERSUS_CRUDE |
| REPORT p4 versus Table3 p9 | Rounded vitamin-D ACR HR1.34 (1.00,1.80), P=.05 versus nonsignificance narrative does not establish unrounded P<.05 or an interval excluding1 under display precision. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT Table1 p5 versus supplement eTables2–3 pp7–8 | Baseline descriptive medication counts differ between displays; they do not change the randomized analysis population, primary/key secondary effect or a decision rule. | PERIPHERAL_COMPARISON |
| PLAN pp4,12–14 versus REPORT p2 | Parent age/recruitment/stratification wording differs; administrative selection details do not identify a conflicting primary or key secondary result or analysis-population count. | PERIPHERAL_COMPARISON |
| PLAN p17 versus REPORT p3 | Original printed creatinine/cystatin-C eGFR equation versus report's named CKD-EPI estimator cannot establish formula nonequivalence without the report formula; no external reference was used. | CONDITIONAL_OR_UNREPORTED |
| PLAN pp15,21; REPORT p2 | Vitamin-D2000IU has differing microgram equivalents within plan text; randomized dose is consistently specified as2000IU, resolving which intervention was tested. | NOTATION_OR_TYPOGRAPHY |
| PLAN pp15–16; REPORT p2 | Planned EPA:DHA40:30 versus actual465+375mg preserves total840mg/day and identifies the reported composition; no competing dose of total omega-3 is established. | CONTEXT_RESOLVES |
| PLAN p23; REPORT p3 | Haybittle-Peto interim guidance explicitly concerns parent cancer/CVD endpoints; assuming DKD-specific interim adjustment would add an unsupported premise. | CONDITIONAL_OR_UNREPORTED |
| PLAN addendum p33; REPORT p3 | Full power reproduction requires unsupplied preliminary eGFR variability/correlation inputs referenced as D10/D12; a discrepancy cannot be inferred from absent inputs. | CONDITIONAL_OR_UNREPORTED |
| REPORT Table3 p9 and supplement eTable10 p15 | HRs versus crude event proportions or incidence-rate ratios compare different measures and follow-up; modeled HRs are explicitly Cox estimates. | MODEL_VERSUS_CRUDE |
| REPORT pp1,4,6 and eTable11 p16 | Repeated safety totals58 kidney stones and45 gastrointestinal bleeds reconcile with32+26 and28+17; no matching-result discrepancy remains. | NOT_REPRODUCED |
| REPORT Figure1 p6, narrative pp4,10 and eTable4 p9 | Final blood934 versus eGFR complete-case932 is resolved by missing baseline eGFR;71% final/83% at-least-one follow-up use stated denominators. | CONTEXT_RESOLVES |
| PLAN pp5–10,20–23,24–30; REPORT background/discussion/references | Historical study counts, rationale charts, safety background and administrative/reference details are not competing current trial result estimates. | OUT_OF_FOCUS |

## Limitations

Scientific cross-source coverage gaps: none. No raw dataset or structured result source is supplied. Forest effect estimates and CI endpoints are graphical without printed exact numbers; no exact values were invented from pixels. The full imputation predictor specification, blood/urine follow-up union, later amendments and preliminary power variance inputs are not supplied; observations requiring these were excluded or explicitly bounded. Five findings and27 excluded-observation rows were produced after full assigned coverage, without a target count.
