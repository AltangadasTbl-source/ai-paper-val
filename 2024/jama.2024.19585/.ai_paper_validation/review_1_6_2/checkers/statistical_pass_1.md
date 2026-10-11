# Statistical consistency — pass 1

Fresh runtime agent: 01a129b6-3a3f-7742-b588-3b9736635a69; gpt-6.1-sol/high; FRESH_SPAWN. Scope: every constituent of S001–S040 and S101–S125, 65 relationship families. Read QUALITY_CONTROL_SCOPE.md and the review contract completely. The companion statistics/relationship_inventory.md records PASS_1_COMPLETE for each family and enumerates every constituent display. No previous findings, candidates, dispositions or reports were read; no external evidence used.

All findings remain for independent screening. No candidate IDs or human dispositions are assigned here. Seven findings, five excluded observations. Sources: DOC-001 main article REPORT, DOC-002 protocol/SAP PLAN, DOC-003 results supplement REPORT. Source hyperlinks below are relative to this checker directory.

Reuse: source-matched native/layout texts and rendered pages, plus both newly rebuilt semantic maps. Exact candidate locations were re-extracted directly with Poppler pdftotext 26.01.0; DOC-001 p9 and DOC-003 p14 source-page images were visually read. New direct derivatives: preprocessing/stat_pass1/doc001-p9-layout.txt, doc002-p36-37-layout.txt, doc003-p13-15-layout.txt, doc003-p18-19-layout.txt, doc003-p22-layout.txt. CPU; no OCR/fallback. Reuse is a locator/transcription aid; exact direct PDFs remain authoritative.

## Findings

### F-ST1-001

**Title:** Emergency-department rate-difference interval includes zero while its row has a significant adjusted test.

**Relationships:** S027, S036, S039, S117. **Locations/roles:** REPORT [DOC-001 p9, Table 3, emergency department row and footnote b](../../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=9); corroborating REPORT [DOC-003 p17, eTable 12 ED Poisson row](../../../joi240111supp2_prod_1733431204.76024.pdf#page=17). Primary relationship S_W; proposed domain statistical_results; focus B.

**Printed values:** absolute rate difference 3.38 per 100 patient-weeks, 95% CrI −0.57 to 7.94; adjusted RR 1.72, 95% CI 1.03 to 2.87; adjusted P=.04. REPORT p4 states two-sided tests and P<.05 significant; abstract/body call ED visits significantly greater.

**Rule/calculation:** −0.57<0<7.94, whereas .04<.05. RR interval excludes its null 1 and agrees with P; the absolute-difference interval includes its null zero and does not give the same inferential reading. This is a direct interval/test conflict, without assuming a Wald test, covariance, degrees of freedom or a prior. Printed rounding intervals for the CrI limits are [−.575,−.565] and [7.935,7.945]; zero remains inside. P rounding interval [.035,.045] remains below .05. Display-precision suppression does not apply to category 1; a numeric relative-discrepancy metric is not applicable to this logical conflict.

**Qualifying route:** Route A, category 1.

**Affected result or extracted value:** significance interpretation and extraction of the ED absolute rate difference versus the adjusted RR.

**Why context does not resolve it:** category 1 requires registration even when the interval and P originate in different analyses. Footnote b expressly distinguishes the models.

**Alternatives/missing definition:** The CrI is a Bayesian/marginalized absolute contrast from a mixed Poisson model containing treatment and site only; the frequentist adjusted RR/P include both stratification variables. Their different scales, covariate sets and inference explain how distinct analyses can differ. They are retained as alternatives rather than treated as a shared-model computational contradiction. The row does not specify a separate inferential decision for the CrI.

**Human question:** Which inference should accompany extraction of the ED absolute rate difference, and should the significant P be read solely as the separately adjusted RR test?

### F-ST1-002

**Title:** Significant symptom-specific intervention tests accompany intervals containing the null in two sparse symptomatic cohorts.

**Relationships:** S035, S116, S123. **Locations/roles:** REPORT [DOC-003 p14, eTable 10, symptom-specific intervention, SSPedi≥1, neuropathy and hunger rows](../../../joi240111supp2_prod_1733431204.76024.pdf#page=14), REPORT [p15 footnote b](../../../joi240111supp2_prod_1733431204.76024.pdf#page=15), REPORT [p22 eMethods](../../../joi240111supp2_prod_1733431204.76024.pdf#page=22). S_W; statistical_results; focus B.

**Printed values:** neuropathy 6/57 (10.5%) versus 0/70 (0%), OR 17.8 (95% CI .98–323.1), P=.007; hunger 6/111 (5.4%) versus 0/130 (0%), OR 16.08 (95% CI .9–288.74), P=.009. Both are in the SSPedi≥1 cohort. The report describes logistic-regression ORs and mixed/fixed logistic P values, with two-sided .05 significance.

**Rule/calculation:** .98<1<323.1 and .9<1<288.74, but .007<.05 and .009<.05. Even after half-unit rounding, neuropathy lower limit [.975,.985] stays below 1; hunger lower limit [.85,.95] stays below 1. P intervals [.0065,.0075] and [.0085,.0095] stay below .05. No distributional assumption is needed. Category 1 is independent of the relative-display-discrepancy rule; relative discrepancy is not applicable.

**Qualifying route:** Route A, category 1.

**Affected result or extracted value:** whether the neuropathy and hunger interventions are statistically distinguishable between groups among participants with any symptom, and the OR/interval/P combinations extracted.

**Why context does not resolve it:** a reproduced category-1 interval/test conflict remains; no row-specific alternative CI/test pairing is declared.

**Alternatives/missing definition:** Sparse cohorts have zero control events. A continuity-adjusted interval and an exact test can give different decisions, but the table calls P logistic-regression based and does not define the zero-event CI or row-specific test. This possible combination is an alternative, not an inferred analysis. Both occurrences are consolidated because the same sparse-event interval/test pattern recurs.

**Human question:** Which interval construction and significance test generated each of these two zero-control-event rows, and how should their differing null-value decisions be interpreted?

### F-ST1-003

**Title:** Sadness any-intervention interval excludes one at the printed P=.05 boundary.

**Relationships:** S035, S115, S037. **Locations/roles:** REPORT [DOC-003 p13 eTable 10, any intervention, all participants, sadness](../../../joi240111supp2_prod_1733431204.76024.pdf#page=13); REPORT [DOC-001 p4 significance rule](../../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=4) and [p5 narrative](../../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=5). Primary S_C; all relationships S_C, S_W; statistical_results; focus B.

**Printed values:** 52/220 (23.6%) versus 82/224 (36.6%); OR .51, 95% CI .26–.99, P=.05. Main narrative calls this significantly more common in usual care; general significance rule is P<.05.

**Rule/calculation:** .26≤.51≤.99<1, while the displayed equality .05 does not satisfy the strict printed P<.05 rule. Upper-limit rounding [.985,.995] remains below 1. P rounding [.045,.055] spans the decision threshold and can contain a value below .05; this is a source-grounded alternative. Under the normative category-1 exception it does not suppress the printed interval/P conflict. Relative discrepancy is not applicable to the strict-threshold comparison.

**Qualifying route:** Route A, category 1.

**Affected result or extracted value:** the sadness any-intervention OR/CI/P and the reported significance of its comparison.

**Why context does not resolve it:** category 1 requires independent screening of the printed combination; the possible intended significance does not replace the printed P.

**Alternatives/missing definition:** An unrounded P slightly below .05 or an intended inequality can agree with the CI and narrative. The report does not supply the unrounded value. This is separate from the much smaller P values in F-ST1-002 because its evident mechanism is a threshold display rather than the repeated sparse-event interval/test pattern.

**Human question:** What is the unrounded or intended P-value expression for the sadness any-intervention comparison?

### F-ST1-004

**Title:** Planned intervention risk-difference/exact-test analysis is replaced by reported logistic OR analysis.

**Relationships:** S035, S106, S115, S116, S123. **Locations/roles:** PLAN [DOC-002 p12 final protocol, secondary analysis 5](../../../joi240111supp1_prod_1733431204.57929.pdf#page=12), PLAN [p37 SAP secondary analysis 5](../../../joi240111supp1_prod_1733431204.57929.pdf#page=37); REPORT [DOC-001 p4 methods](../../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=4); REPORT [DOC-003 pp13–15 eTable 10](../../../joi240111supp2_prod_1733431204.76024.pdf#page=13), [p22 eMethods](../../../joi240111supp2_prod_1733431204.76024.pdf#page=22). Primary P_R; all relationships P_R; protocol_report; focus D.

**Printed statements:** Final protocol and SAP say all intervention treatment effects will be simple differences in proportions ignoring clustering, Fisher exact P values, and Newcombe 95% CIs. Report methods say mixed logistic adjusted for stratification, with treatment-only fixed logistic fallback; effects are ORs. Applies to both any and symptom-specific interventions, all 15 symptoms in each of three cohorts at the reported week-8 time point.

**Rule/comparison:** Difference in proportions with null zero and a Newcombe interval is a different estimand/model/test specification from logistic OR with null one, and including site clustering/strata differs from expressly ignoring clustering. Example: symptom-specific pain all participants is printed OR5.30 (2.50–11.24), P<.001; not the planned proportion-difference quantity. No crude-ratio comparison is used to judge an adjusted estimate. Display-precision arithmetic and relative discrepancy are not applicable to the method change.

**Qualifying route:** Route B.

**Affected result or extracted value:** every eTable 10 any/symptom-specific intervention effect and its correspondence to the analysis specification; particularly key symptom-specific intervention results highlighted in the abstract.

**Why context does not resolve it:** B1 in-focus analysis specification; B2 both final plan and report give explicit incompatible methods without a supplied explanatory amendment; B3 the effect scale and treatment of clustering change interpretation and extraction. The original protocol uses logistic analysis, but the supplied final protocol/SAP deliberately states the proportion-difference approach.

**Alternatives/missing definition:** A later analytical choice may have reinstated the original logistic approach; no supplied post-SAP statistical amendment explains it. The observational fact is the differing statements, not an inference about compliance.

**Human question:** Which specification was applied to the intervention comparisons, and where is the rationale or amendment connecting the final SAP proportion-difference/Fisher/Newcombe analysis to the reported logistic ORs?

### F-ST1-005

**Title:** The triggered planned ordinal sensitivity of the primary total score is not reported.

**Relationships:** S031, S032, S104, S118. **Locations/roles:** PLAN [DOC-002 p11 final protocol primary comparative analyses](../../../joi240111supp1_prod_1733431204.57929.pdf#page=11), PLAN [p36 SAP primary outcome](../../../joi240111supp1_prod_1733431204.57929.pdf#page=36); REPORT [DOC-003 p18 eFigure 1 primary sensitivities](../../../joi240111supp2_prod_1733431204.76024.pdf#page=18), REPORT [DOC-001 pp3–4 primary/sensitivity methods](../../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=4). P_R; protocol_report; focus D.

**Printed statements:** Plan says substantial residual non-normality triggers two sensitivities, one using normalizing transformations and another using an ordinal regression model. Report states residuals were clearly non-normal and right-skewed, reports square-root-transformed total score effect −.7 (−1.1 to −.3), P=.003, but no ordinal model result for the total SSPedi outcome in the complete supplied results.

**Rule/comparison:** The reported non-normality establishes the plan's trigger. The complete results inventory contains transformed total, chemotherapy-restricted, baseline-adjusted and missing-data sensitivities; individual-symptom ordinal models are different endpoints, not the planned total-score ordinal sensitivity. Neither the main article nor the 23-page results supplement reports that total-score analysis. Numeric display-precision and relative discrepancy are not applicable.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** sensitivity support for the primary week-8 total SSPedi result.

**Why context does not resolve it:** a planned primary analysis is absent after its explicitly supplied trigger is met; this is category 5.

**Alternatives/missing definition:** The analysis may have been conducted outside the supplied package, or the transformation may have been chosen as sufficient. Neither replaces the second analysis stated in the plan. No preferred analysis is proposed.

**Human question:** Was the planned ordinal-regression sensitivity for week-8 total SSPedi performed, and where is its result or the explanation for its replacement?

### F-ST1-006

**Title:** Finite between-group effects are printed for severe mouth sores when the intervention cohort contains no participant.

**Relationships:** S114, S115, S116, S123. **Locations/roles:** REPORT [DOC-003 p13 eTable 10 documentation, mouth sores, SSPedi≥3](../../../joi240111supp2_prod_1733431204.76024.pdf#page=13), REPORT [p14 any and symptom-specific interventions, mouth sores, SSPedi≥3](../../../joi240111supp2_prod_1733431204.76024.pdf#page=14); REPORT [p15 footnote b](../../../joi240111supp2_prod_1733431204.76024.pdf#page=15), REPORT [p22 eMethods](../../../joi240111supp2_prod_1733431204.76024.pdf#page=22). S_W; statistical_results; focus C.

**Printed values:** intervention0/0 versus control2/8 (25%) for documentation, OR2.6 (.04–170.4), P>.99; intervention0/0 versus control1/8 (12.5%) for both any and symptom-specific intervention, OR5.00 (.07–366.4), P>.99. All three are labeled comparisons between treatment groups.

**Rule/calculation:** A treatment-only logistic contrast cannot be identified from the observed cohort when treatment has only one observed level. A mixed model with treatment/strata does not create observations in the empty group either. Diagnostic only: adding .5 to all four contingency cells gives (.5×6.5)/(.5×2.5)=2.6 for documentation and (.5×7.5)/(.5×1.5)=5.0 for interventions, reproducing the printed point estimates, without proving that this was the authors' method. An undocumented continuity/pseudocount rule is distinct from fitting the stated ordinary logistic regression. Counts are exact discrete participant counts, not rounding inputs; arithmetic display gap between those diagnostic point values and printed values is zero. The finding is the absent identifiable observed contrast under the stated method, not a magnitude discrepancy.

**Qualifying route:** Route B.

**Affected result or extracted value:** severe-mouth-sore between-group ORs that a reader could extract as observed-cohort effects.

**Why context does not resolve it:** B1 source-grounded method logic; B2 no row-specific estimator/prior/pseudocount rule is stated and the empty group is explicit; B3 the finite reported contrast could be reused despite lacking an observed comparator. All three occurrences form one pattern.

**Alternatives/missing definition:** A continuity adjustment, penalized analysis or prior could generate finite numbers; source supplies none of these definitions. The diagnostic explains a possible calculation, not a reconstruction of a declared analysis and not a recommended change.

**Human question:** What estimator and added information produced the finite severe-mouth-sore contrasts when the intervention analysis denominator was zero, and how should these numbers be interpreted for extraction?

### F-ST1-007

**Title:** Planned week-4 individual-symptom inferential analyses are not supplied.

**Relationships:** S033, S039, S040, S102, S105, S121. **Locations/roles:** PLAN [DOC-002 p11 final protocol secondary analysis 1](../../../joi240111supp1_prod_1733431204.57929.pdf#page=11), PLAN [p36 SAP secondary outcomes 1](../../../joi240111supp1_prod_1733431204.57929.pdf#page=36); REPORT [DOC-001 p4 ordinal analysis and conclusions](../../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=4), REPORT [DOC-003 p12 eTable 9](../../../joi240111supp2_prod_1733431204.76024.pdf#page=12), REPORT [p20 eFigure 2](../../../joi240111supp2_prod_1733431204.76024.pdf#page=20). P_R; protocol_report; focus D.

**Printed statements:** Final protocol and SAP specify mixed proportional-odds models for individual SSPedi symptoms at weeks4 and8, ORs and95%CIs. Report analysis paragraph specifies week8; eTable9 gives week4 severe counts and other descriptive summaries, but no week4 ordinal effects/intervals. Table2 and eFigure2 supply week8 only. Individual-symptom improvement is a key secondary result in the abstract, including the 12/15 significance statement.

**Rule/comparison:** The complete result package supplies zero week4 inferential rows for these15 prespecified ordinal symptom outcomes. Severe score3/4 descriptive counts do not stand in for ORs over the0–4 ordinal endpoint. All15 missing week4 models are consolidated as one timepoint pattern. Display precision and relative discrepancy are not applicable to the missing planned analysis.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** temporal interpretation and extraction of the prespecified key individual-symptom outcomes, whose week8 result is highlighted in the abstract.

**Why context does not resolve it:** category5 planned key secondary analyses are not reported, even though the timepoint data were collected and descriptive results supplied. This is not a peripheral contributor-count comparison.

**Alternatives/missing definition:** Results may exist outside the supplied package, or week8 may have been selected for presentation; no supplied amendment narrows the planned two-timepoint inferential scope.

**Human question:** Where are the prespecified week4 individual-symptom ORs and intervals, or the explanation for reporting only week8 effects?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| DOC-001 Table2/eTable8; DOC-001 Table3 absolute contrasts | Crude severe-symptom odds or crude group-rate subtraction can differ from ordinal/model-based ORs and marginalized differences. The displayed model-based values are not asserted to be crude. | MODEL_VERSUS_CRUDE |
| DOC-002 pp11/36 compared with allocation pp8/23 and report/eTable6 | Analysis description says above/below average while actual stratification/allocation and coefficient labels say median; “stratification variables” identifies the recorded allocation factors, and no distinct recoding or changed printed result is supplied. Doubt about this wording alone does not establish a second analysis. | TERMINOLOGY_OR_WORDING |
| DOC-003 pp18–19 MICE versus DOC-002 p39 | Supplemental MI performed below the overall10% trigger, using an expanded predictor list. The report explicitly explains intervention10.4% as reason for extra sensitivity; absent group/strata/dataset-count details do not establish a contradictory implementation of a mandatory above-trigger analysis. | CONDITIONAL_OR_UNREPORTED |
| DOC-003 p17 eTable12 footnote | “Substantive conclusions were the same” despite ED Bayesian credible interval including1. The source reports similar directions/magnitudes,95.2% posterior RR>1, and no Bayesian significance decision rule; an asserted identical two-sided significance decision cannot be reproduced from this qualitative wording alone. | TERMINOLOGY_OR_WORDING |
| DOC-003 p19 eFigure1 and DOC-001 p4 | Robustness wording despite worst-case−2.0(−4.3,.3),P=.09. The displayed deliberately unrealistic sensitivity retains direction and openly shows lost significance; “robust” is not an explicit claim of significant benefit under that scenario. | CONTEXT_RESOLVES |

## Limits

No scientific-coverage gap. Exact model covariance/df/variance estimators, Bayesian priors and row-level fallback choices are not supplied for all displays, so exact joint CI/P reconstruction beyond stated null-decision checks is unavailable; no convention is silently assumed. The4000-trial power simulation is described but simulation data/code/seed are not supplied; the declared cluster total, missing-data inflation and monotone power table can be checked, while exact simulation percentages cannot independently be regenerated. Those missing definitions alone are not findings. S124/S125 lack participant-level age/sex/diagnosis datasets and named tests; diagnostic count checks cannot reproduce every P exactly. Noninferiority/equivalence/multiplicity margins and stopping rules are not stated, so no such rule is invented.

## Explicit completion index for mechanical validation

The original pass-1 scope used the ranges S001–S040 and S101–S125. The following index expands those ranges mechanically from the already completed canonical inventory; it does not add review work or change any finding, excluded observation or source fact. Each family's substantive pass-1 checks are recorded in statistics/relationship_inventory.md.

| Relationship ID | Existing pass-1 record |
|---|---|
| S001 | PASS_1_COMPLETE; canonical inventory family row |
| S002 | PASS_1_COMPLETE; canonical inventory family row |
| S003 | PASS_1_COMPLETE; canonical inventory family row |
| S004 | PASS_1_COMPLETE; canonical inventory family row |
| S005 | PASS_1_COMPLETE; canonical inventory family row |
| S006 | PASS_1_COMPLETE; canonical inventory family row |
| S007 | PASS_1_COMPLETE; canonical inventory family row |
| S008 | PASS_1_COMPLETE; canonical inventory family row |
| S009 | PASS_1_COMPLETE; canonical inventory family row |
| S010 | PASS_1_COMPLETE; canonical inventory family row |
| S011 | PASS_1_COMPLETE; canonical inventory family row |
| S012 | PASS_1_COMPLETE; canonical inventory family row |
| S013 | PASS_1_COMPLETE; canonical inventory family row |
| S014 | PASS_1_COMPLETE; canonical inventory family row |
| S015 | PASS_1_COMPLETE; canonical inventory family row |
| S016 | PASS_1_COMPLETE; canonical inventory family row |
| S017 | PASS_1_COMPLETE; canonical inventory family row |
| S018 | PASS_1_COMPLETE; canonical inventory family row |
| S019 | PASS_1_COMPLETE; canonical inventory family row |
| S020 | PASS_1_COMPLETE; canonical inventory family row |
| S021 | PASS_1_COMPLETE; canonical inventory family row |
| S022 | PASS_1_COMPLETE; canonical inventory family row |
| S023 | PASS_1_COMPLETE; canonical inventory family row |
| S024 | PASS_1_COMPLETE; canonical inventory family row |
| S025 | PASS_1_COMPLETE; canonical inventory family row |
| S026 | PASS_1_COMPLETE; canonical inventory family row |
| S027 | PASS_1_COMPLETE; canonical inventory family row |
| S028 | PASS_1_COMPLETE; canonical inventory family row |
| S029 | PASS_1_COMPLETE; canonical inventory family row |
| S030 | PASS_1_COMPLETE; canonical inventory family row |
| S031 | PASS_1_COMPLETE; canonical inventory family row |
| S032 | PASS_1_COMPLETE; canonical inventory family row |
| S033 | PASS_1_COMPLETE; canonical inventory family row |
| S034 | PASS_1_COMPLETE; canonical inventory family row |
| S035 | PASS_1_COMPLETE; canonical inventory family row |
| S036 | PASS_1_COMPLETE; canonical inventory family row |
| S037 | PASS_1_COMPLETE; canonical inventory family row |
| S038 | PASS_1_COMPLETE; canonical inventory family row |
| S039 | PASS_1_COMPLETE; canonical inventory family row |
| S040 | PASS_1_COMPLETE; canonical inventory family row |
| S101 | PASS_1_COMPLETE; canonical inventory family row |
| S102 | PASS_1_COMPLETE; canonical inventory family row |
| S103 | PASS_1_COMPLETE; canonical inventory family row |
| S104 | PASS_1_COMPLETE; canonical inventory family row |
| S105 | PASS_1_COMPLETE; canonical inventory family row |
| S106 | PASS_1_COMPLETE; canonical inventory family row |
| S107 | PASS_1_COMPLETE; canonical inventory family row |
| S108 | PASS_1_COMPLETE; canonical inventory family row |
| S109 | PASS_1_COMPLETE; canonical inventory family row |
| S110 | PASS_1_COMPLETE; canonical inventory family row |
| S111 | PASS_1_COMPLETE; canonical inventory family row |
| S112 | PASS_1_COMPLETE; canonical inventory family row |
| S113 | PASS_1_COMPLETE; canonical inventory family row |
| S114 | PASS_1_COMPLETE; canonical inventory family row |
| S115 | PASS_1_COMPLETE; canonical inventory family row |
| S116 | PASS_1_COMPLETE; canonical inventory family row |
| S117 | PASS_1_COMPLETE; canonical inventory family row |
| S118 | PASS_1_COMPLETE; canonical inventory family row |
| S119 | PASS_1_COMPLETE; canonical inventory family row |
| S120 | PASS_1_COMPLETE; canonical inventory family row |
| S121 | PASS_1_COMPLETE; canonical inventory family row |
| S122 | PASS_1_COMPLETE; canonical inventory family row |
| S123 | PASS_1_COMPLETE; canonical inventory family row |
| S124 | PASS_1_COMPLETE; canonical inventory family row |
| S125 | PASS_1_COMPLETE; canonical inventory family row |
