# Statistical consistency review — fresh pass 1

Runtime agent `/root/statistical_pass_1`; `gpt-6.1-sol` / `high`; `FRESH_SPAWN`. Exact scope: all 84 canonical statistical relationships S001–S084 in [relationship inventory](../statistics/relationship_inventory.md), covering all 170 mapped source pages (DOC-001 REPORT pp.1–11; DOC-002 PLAN pp.1–90; DOC-003 REPORT pp.1–69). The independent pass-2 agent must revisit the entire inventory after registration, screening and source recheck. No C IDs or human dispositions are assigned here.

The full scope and review contract were read. Checks include every printed estimate/interval/test row, containment, direction, null/margin, model and population matching, missing-data and clustering steps, randomization, sample-size inputs, multiplicity, interim/stopping rules, and original-versus-reported specifications. Each observation below was self-screened; the eleven findings require the fresh independent inclusion screen. An acknowledged amendment is preserved as an alternative, not a claim about its acceptability. Route A category 5 does not disappear merely because a primary-analysis or composite change is disclosed.

## Findings

### F-ST1-001 — MI-pooled proportions and the printed risk difference need an estimand/model mapping

- **Relationships:** S061. **Compared locations and roles:** REPORT [DOC-003 p.59, eTable16](../../../joi250084supp2_prod_1765403089.61751.pdf#page=59), three cells of its sole primary-outcome row. REPORT [p.30, eTable16 method](../../../joi250084supp2_prod_1765403089.61751.pdf#page=30) and PLAN [DOC-002 p.88, MICE method](../../../joi250084supp1_prod_1765403089.61351.pdf#page=88) corroborate pooling; the plan does not conflict with the report independently.
- **Printed values:** AI MI-pooled achievement32.2%, human31.9%; RD−1.1pp, one-sided95% lower endpoint−11.5pp. Twenty imputations; final proportions and between-group RDs combined using Rubin's rules. Report identifies binomial RD regression but gives no separate adjusted outcome-estimation model for this MI row.
- **Rule and calculation:** For the same imputation-specific arm risks, Qbar_RD=mean(p_AI−p_H)=mean(p_AI)−mean(p_H). Printed proportion intervals[32.15,32.25] and[31.85,31.95] give a pooled contrast[0.20,0.40]pp. PrintedRD interval[−1.15,−1.05] has gap1.25pp; relative discrepancy1.25/1.1=1.13636, above.05. This is a same-display pooling/contrast diagnostic, not a recomputed CI or a comparison of an explicitly adjusted estimate with crude counts.
- **Focus area:** B,C. **Proposed review domain:** `statistical_results`. **Relationship type:** `S_W`.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** The MI sensitivity primary-outcome point estimate and its direction; either the positive pooled-risk contrast or the negative printedRD could be extracted.
- **Why context does not resolve it:** Imputation predictors explain how missing outcomes were filled, but do not identify a distinct final regression contrast, standardization population or estimand capable of mapping the pooled risks to−1.1pp. The displayed values reverse the direction of the direct pooled contrast beyond precision.
- **Alternatives and missing definitions:** A separately adjusted/model-based RD could coexist with pooled marginal arm proportions; the missing final outcome model/estimand mapping must then be stated. A display transcription explanation is also possible. The printed lower endpoint remains above−15, so the reported NI conclusion is not independently contradicted by this arithmetic observation.
- **Human question:** Which final estimation model and estimand produced−1.1pp, and how does it relate to the32.2% and31.9% MI-pooled arm proportions?
- **Direct confirmation:** Fresh source render `preprocessing/st1-report-p59.png` and planp88 were visually inspected, PyMuPDF1.28.0/200dpi/CPU.

### F-ST1-002 — The printed physical-activity pipeline calculates an imputed vector but does not pass it into the outcome summaries

- **Relationships:** S013,S014,S039,S070. **Compared locations and roles:** REPORT [DOC-003 p.13, preprocessing and MVPA calculation](../../../joi250084supp2_prod_1765403089.61751.pdf#page=13), versus REPORT [p.15, first R loop](../../../joi250084supp2_prod_1765403089.61751.pdf#page=15) and [p.16, second R loop](../../../joi250084supp2_prod_1765403089.61751.pdf#page=16).
- **Printed statements:** Missing data within valid days are interpolated. Code sets `ac_imp <- impute_missing_data(ac_mid, wnw, valid.long)`, but each `activity_stats` call uses `ac, timestamp`; bout calls also use `ac`. `ac` was assigned the original `datai$vectormagnitude`, and no intervening printed assignment replaces it with `ac_imp`.
- **Rule and calculation:** A transformation computed into a new vector cannot enter the displayed data flow when subsequent summary calls consume the original vector and never consume the transformed output. Both loops show this same pattern; consolidate them into one method observation. This is a direct data-flow comparison; external package behavior is not assumed.
- **Focus area:** C. **Proposed review domain:** `statistical_results`. **Relationship type:** `S_W`.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Actigraphy-derived weekly MVPA, the>=4% weight-loss-plus150min/wk component (23/183 vs23/185), and continuous PA summaries210.5/174.4min/wk.
- **Why context does not resolve it:** The prose says interpolation contributes to preprocessing and labels this the calculation code, while the visible summary pipeline bypasses its output. The reader cannot tell which processing stream generated the published PA quantities.
- **Alternatives and missing definitions:** `activity_stats` might perform its own internal imputation, or the displayed script might be an abbreviated preprocessing illustration followed by unprinted processing. The supplied function implementation, actual production input vector and correspondence of the displayed script to analyzed data are missing. These alternatives are questions, not assertions that a preferred pipeline was required.
- **Human question:** Which vector and interpolation/nonwear processing were actually used to generate the published PA outcomes, and where does the printed `ac_imp` output enter that calculation?
- **Direct confirmation:** Fresh renders of reportpp.13,15,16 were visually inspected, PyMuPDF1.28.0/200dpi/CPU.

### F-ST1-003 — Available-period averaging and zero-filled missing periods leave the PA denominator unclear

- **Relationships:** S013,S015,S039,S070. **Compared locations and roles:** REPORT [DOC-003 p.13, Aggregation of MVPA Across Visits and Actigraphy Compliance](../../../joi250084supp2_prod_1765403089.61751.pdf#page=13), REPORT [p.30, eTable18a methods](../../../joi250084supp2_prod_1765403089.61751.pdf#page=30), and REPORT [p.49, eTable8b handling](../../../joi250084supp2_prod_1765403089.61751.pdf#page=49).
- **Printed statements:** Weekly MVPA from all valid wear periods is summed and divided by the number of available wear periods, maximum11 postbaseline. Elsewhere a month/week with inadequate/no valid data is assigned0minutes and treated as inactivity for the primary analysis.
- **Rule and calculation:** Excluding an unavailable period from the denominator differs from including its imputed0. A diagnostic illustration, not participant data: two scheduled periods with observed300 and one unavailable give300/1=300 under available-period averaging, versus(300+0)/2=150 under zero-filled scheduled-period averaging. With other inputs, the150 threshold can therefore be crossed differently. No amount of display rounding equates these distinct formulas.
- **Focus area:** C. **Proposed review domain:** `statistical_results`. **Relationship type:** `S_W`.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** The primary joint weight/PA component and reported mean weekly PA.
- **Why context does not resolve it:** “Valid” and “available” do not state whether zero-filled nonwear periods become eligible denominators. Both operations are described as the primary PA calculation, without the joining rule.
- **Alternatives and missing definitions:** Imputed0 periods may be counted as available, making the two descriptions compatible; alternatively available refers only to valid recorded periods. The analysis denominator after zero assignment is missing. No participant-level reclassification is asserted.
- **Human question:** After a missing/noncompliant period is assigned0, does that period enter the denominator for the PA average used in the primary endpoint and continuous PA display?
- **Direct confirmation:** Reportp13 freshly rendered/inspected; pp.30/49 source-linked full transcripts read, with direct-source recheck required for every location.

### F-ST1-004 — The primary PA component uses different printed averaging windows in the original plan and report

- **Relationships:** S001,S015,S039. **Compared locations and roles:** PLAN [DOC-002 p.15 §3.2](../../../joi250084supp1_prod_1765403089.61351.pdf#page=15), versus REPORT [DOC-003 p.13, aggregation](../../../joi250084supp2_prod_1765403089.61751.pdf#page=13). PLAN [pp.80–81, version1.4 amendment](../../../joi250084supp1_prod_1765403089.61351.pdf#page=80) is amendment context.
- **Printed statements:** Original>=4%loss+>=150min/wk branch averages months6–11. Report averages up to11 postbaseline monthly periods throughout12-month follow-up. Amendment states the primary PA measurement timeframe was clarified but does not print its replacement window.
- **Rule and calculation:** Months6–11 supply six monthly periods; all11 postbaseline months include earlier periods as well. The primary composite branch therefore has distinct printed time-window specifications; no numerical reclassification can be calculated without raw monthly PA.
- **Focus area:** D. **Proposed review domain:** `protocol_report`. **Relationship type:** `P_R`.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** Primary composite success and the23/183 versus23/185 joint component.
- **Why context does not resolve it:** This is a reproduced change in the primary composite specification, an always-register category. The amendment is an alternative explanation, but the replacement timeframe is not supplied explicitly.
- **Alternatives and missing definitions:** Reportp13 could describe the continuous PA summary while a separate months6–11 calculation generated the primary branch; or version1.4 could have changed both to all postbaseline periods. Exact endpoint-specific averaging window and amendment text are missing.
- **Human question:** Which months entered the primary PA component, and what final amended primary-endpoint specification established that window?
- **Direct confirmation:** Fresh planp15,amendmentpp.80–81 and reportp13 renders visually inspected.

### F-ST1-005 — Diabetes-range HbA1c became an additional primary-composite disqualifier

- **Relationships:** S001,S019,S037. **Compared locations and roles:** PLAN [DOC-002 p.15 §3.2](../../../joi250084supp1_prod_1765403089.61351.pdf#page=15), PLAN [p.86, incident-diabetes change row](../../../joi250084supp1_prod_1765403089.61351.pdf#page=86), versus REPORT [main p.3, Outcomes](../../../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=3) and REPORT [DOC-003 p.30, diabetes-range handling](../../../joi250084supp2_prod_1765403089.61751.pdf#page=30).
- **Printed statements:** Original composite is success if any listed weight/PA/A1c branch succeeds. Change disclosure says diabetes was not prespecified grounds for primary failure; implemented HbA1c>=6.5% at6/12months implies failure regardless of weight/PA improvement. Main requires HbA1c<6.5% throughout.
- **Rule and calculation:** Original A OR B OR C becomes (A OR B OR C) AND no diabetes-range HbA1c. These are different composite definitions; the package does not give cross-classified branch success among the15 diabetes-range participants to quantify the change.
- **Focus area:** D. **Proposed review domain:** `protocol_report`. **Relationship type:** `P_R`.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** Primary achievers58/183 and59/185 and associated NI result.
- **Why context does not resolve it:** A changed prespecified composite definition is always registered. The disclosure identifies the implemented rule; it does not remove the primary-definition comparison from the inclusion threshold.
- **Alternatives and missing definitions:** An accepted amendment may govern the final definition; timing/approval of this SAP-change table is not printed. This observation does not question its clinical rationale, continued participant follow-up, or a diagnosis requiring two confirmatory tests.
- **Human question:** What final prespecification/amendment governed this composite disqualifier, and which primary achievement values correspond to that definition?
- **Direct confirmation:** Fresh planpp.15/86 and mainp3 renders inspected; resultp30 full source-linked method transcript read.

### F-ST1-006 — The planned clustered logistic primary analysis was replaced by unadjusted binomial RD regression

- **Relationships:** S007,S037,S065,S066. **Compared locations and roles:** PLAN [DOC-002 p.37 §9.4.1](../../../joi250084supp1_prod_1765403089.61351.pdf#page=37), [p.38 §9.4.7](../../../joi250084supp1_prod_1765403089.61351.pdf#page=38), and [p.86 model change](../../../joi250084supp1_prod_1765403089.61351.pdf#page=86), versus REPORT [main p.4, Statistical Analysis](../../../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=4).
- **Printed statements:** Planned primary/secondary mixed-effects logistic models account for within-program-site clustering. Report primary uses binomial regression estimating RD; cluster-robust analyses are posthoc sensitivities. Change table explicitly describes unadjusted binomial regression replacing logistic primary analysis.
- **Rule and calculation:** The primary model family and incorporation of program-site clustering differ from the original specified primary analysis. Separate posthoc clustered SE sensitivities do not constitute a reported fit of the original mixed-effects logistic primary model.
- **Focus area:** D. **Proposed review domain:** `protocol_report`. **Relationship type:** `P_R`.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** PrimaryRD−0.2pp and its one-sided lower confidence endpoint−8.2pp.
- **Why context does not resolve it:** A planned primary analysis is replaced, an always-register category. The stated replacement and rationale are fully retained; no preferred model is proposed.
- **Alternatives and missing definitions:** A documented amendment may establish the binomial model as final; the original logistic model might have been fitted but not reported. Dates/approval and any original-model result are unavailable.
- **Human question:** What final primary-model specification governed the reportedRD, and is a result from the originally specified clustered logistic analysis available in the supplied package?
- **Direct confirmation:** Fresh planpp.37/38/86 and mainp4 renders inspected.

### F-ST1-007 — The original primary analysis exclusions were replaced by all-randomized failure imputation

- **Relationships:** S006,S037. **Compared locations and roles:** PLAN [DOC-002 p.37 §9.3](../../../joi250084supp1_prod_1765403089.61351.pdf#page=37) and [p.86 population change](../../../joi250084supp1_prod_1765403089.61351.pdf#page=86), versus REPORT [main p.4 primary methods/results](../../../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=4) and REPORT [DOC-003 p.27 primary cohort](../../../joi250084supp2_prod_1765403089.61751.pdf#page=27).
- **Printed statements:** Original effectiveness excludes withdrawals; change table additionally characterizes original exclusion of missing12-month outcomes. Report all368 randomized, including26/29 without twelve-month visits, with missing outcomes classified failure.
- **Rule and calculation:** Original exclusion versus inclusion-and-failure is a changed primary analysis population/missing-outcome rule. Report183+185=368 and observed157+156=313 with55 missing; the implemented denominators reconcile mechanically.
- **Focus area:** D. **Proposed review domain:** `protocol_report`. **Relationship type:** `P_R`.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** The primary denominators183/185, achievement rates31.7%/31.9%, and NI contrast.
- **Why context does not resolve it:** Replacement of a planned primary analysis is always registered, even with a disclosed conservative rationale. The counting operations differ.
- **Alternatives and missing definitions:** An amendment may govern all-randomized analysis; the exact original cohort cannot be reconstructed solely from visit completion because withdrawal and missingness are distinct. No alternate denominator is proposed as a correction.
- **Human question:** What final analysis-population amendment governed inclusion of missing/withdrawn participants, and how was it prespecified relative to the original exclusion rule?
- **Direct confirmation:** Fresh planpp.37/86 and mainp4 renders inspected; cohortp27 mapped source text read.

### F-ST1-008 — The planned primary physical-activity missing-data analysis was replaced by zero imputation

- **Relationships:** S015,S016,S037,S039. **Compared locations and roles:** PLAN [DOC-002 p.38 §9.4.2](../../../joi250084supp1_prod_1765403089.61351.pdf#page=38) and [p.86 missingness change](../../../joi250084supp1_prod_1765403089.61351.pdf#page=86), versus REPORT [DOC-003 p.13](../../../joi250084supp2_prod_1765403089.61751.pdf#page=13), [p.30 eTable18a methods](../../../joi250084supp2_prod_1765403089.61751.pdf#page=30), and [p.49 eTable8b](../../../joi250084supp2_prod_1765403089.61751.pdf#page=49).
- **Printed statements:** If PA missingness>5%, primary analysis based on multiple imputation and a100%-complete-PA sensitivity. Implemented primary PA gives0 to missing/noncompliant intervals; best-case nonwear/all-attain-PA are posthoc sensitivities. Change table expressly replaces the original MI rule with0minutes.
- **Rule and calculation:** Monthly displayed missingness rises above5% (e.g. month1 AI17/183=9.29%,human21/185=11.35%). Thus the supplied plan's trigger is relevant; final primary uses a different imputation rule, while MICE of missing twelve-month outcomes is a different sensitivity, not the original monthly-PA MI procedure.
- **Focus area:** D. **Proposed review domain:** `protocol_report`. **Relationship type:** `P_R`.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** Primary PA threshold/composite classification and primaryRD; individual reclassification counts unavailable.
- **Why context does not resolve it:** This is a reproduced replacement of a planned primary-analysis step. The rationale is disclosed and retained, not evaluated as a preferred choice.
- **Alternatives and missing definitions:** A revised SAP may govern zero imputation. No original PA-imputed analysis or complete-case100%-valid-PA result is identified. The precise amendment timing and changed denominator rule remain questions.
- **Human question:** What final amendment established primary zero imputation, and were the originally specified PA-imputed/100%-complete sensitivity analyses executed or reported?
- **Direct confirmation:** Fresh planpp.38/86 and reportp13 inspected; reportpp.30/49 complete mapped source transcripts read.

### F-ST1-009 — The planned primary-outcome program-completer analysis was replaced by a different restricted cohort

- **Relationships:** S008,S021,S057. **Compared locations and roles:** PLAN [DOC-002 p.37 §9.3](../../../joi250084supp1_prod_1765403089.61351.pdf#page=37), [pp.86–87 PP change](../../../joi250084supp1_prod_1765403089.61351.pdf#page=86), versus REPORT [main p.4 restricted analysis](../../../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=4), REPORT [DOC-003 p.27](../../../joi250084supp2_prod_1765403089.61751.pdf#page=27) and [p.58 eTable15](../../../joi250084supp2_prod_1765403089.61751.pdf#page=58).
- **Printed statements:** Original PP is program completers under CDC engagement standards. Implemented PP/restricted population has complete12-month study outcomes and no prohibited medication use,151/149, without the original program-completion requirement in its definition. The change is explicit.
- **Rule and calculation:** Program completers117/183 and93/185 are different from restricted151/149; complete outcomes without prohibited medication do not logically imply program completion. eTable15 therefore does not report the originally specified program-completer primary-outcome analysis.
- **Focus area:** D. **Proposed review domain:** `protocol_report`. **Relationship type:** `P_R`.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** Supportive primaryRD0.2pp(lower−8.9) for54/151vs53/149 and the interpretation of its population.
- **Why context does not resolve it:** The prespecified supportive analysis of the primary outcome is replaced. Acknowledged redefinition does not make the two cohorts equivalent.
- **Alternatives and missing definitions:** The restriction may be governed by a later amendment; Figure4 gives descriptive outcome counts among program completers, but does not give the planned program-completer NI estimate/interval. The report expressly avoids a causal-adherence interpretation; none is imposed here.
- **Human question:** What final specification governed the supportive primary analysis population, and where is the original program-completer primary-outcome contrast/interval reported, if executed?
- **Direct confirmation:** Fresh planpp.37/86–87 and mainp4 inspected; reportpp.27/58 mapped complete source text read.

### F-ST1-010 — The HbA1c branch of the prespecified primary composite was restricted to a baseline subset

- **Relationships:** S001,S018,S040,S060. **Compared locations and roles:** PLAN [DOC-002 p.15 §3.2](../../../joi250084supp1_prod_1765403089.61351.pdf#page=15), [pp.80–81 version1.4 amendment](../../../joi250084supp1_prod_1765403089.61351.pdf#page=81), versus REPORT [main p.3 Outcomes](../../../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=3) and [p.7 Figure2 HbA1c row/footnote](../../../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=7).
- **Printed statements:** Original primary>=0.2% HbA1c-reduction branch has no baseline-subset qualifier. Version1.4 (IRB03-28-2022) restricts it to baseline5.7–6.4% while broadening eligibility to other laboratory evidence of prediabetes. Report applies the branch only to130/130 participants instead of all183/185.
- **Rule and calculation:** An unconditional branch versus one defined only in a260-participant subset is a changed primary-composite specification; the58/59 composite achievers remain an all-randomized outcome. This is not a claim that subset denominators fail to reconcile.
- **Focus area:** D. **Proposed review domain:** `protocol_report`. **Relationship type:** `P_R`.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** HbA1c-component achievement35/130 in each arm and the all-randomized composite definition.
- **Why context does not resolve it:** A prespecified composite definition changes, an always-register category. The dated, explicitly disclosed amendment is preserved as the principal alternative explanation.
- **Alternatives and missing definitions:** The amendment may be the governing prospective specification for the expanded eligible population; original eligibility had already required prediabetes-rangeHbA1c, so some original participants may have unchanged practical eligibility for this branch. This limits the interpretation of the change but does not erase the printed specification comparison.
- **Human question:** Which final primary-composite amendment governs the HbA1c branch for the analyzed population, and how should that baseline-subset restriction be recorded with the extracted primary outcome?
- **Direct confirmation:** Fresh planpp.15/80–81 and mainp3 inspected; mainFigure2 complete source-matched map read.

### F-ST1-011 — The categorical-test P values in the baseline HbA1c subgroup display do not reproduce from the displayed counts

- **Relationships:** S028. **Compared locations and roles:** REPORT [DOC-003 p.44, eTable6 site and ethnicity rows](../../../joi250084supp2_prod_1765403089.61751.pdf#page=44), versus REPORT [p.45, footnote1](../../../joi250084supp2_prod_1765403089.61751.pdf#page=45). REPORT [p.29, eTable6 method index](../../../joi250084supp2_prod_1765403089.61751.pdf#page=29) points to the main baseline-table methods. PLAN [DOC-002 p.37 §9.4.1](../../../joi250084supp1_prod_1765403089.61351.pdf#page=37) specifies chi-square or Fisher exact tests for categorical baseline differences and provides method context, without an independent plan/report conflict.
- **Printed values:** A1c<5.7% groupN108 and5.7–6.4% groupN260. SiteJHU79/164 andReading29/96; footnote siteP=.024. Ethnicity notHispanic96/247,Hispanic10/10,declined0/2,unknown2/1; footnote ethnicityP=.018. Both printed P values indicate significance at.05.
- **Exact supplied-method chain:** Sourcep.28 eTable3 says baseline methods as mainTable1; p.29 eTable6 repeats that pointer. The explicitly named chi-square/Wilcoxon sentence spanningpp.28–29 belongs to eTable4, not eTable3, and is not silently reassigned to eTable6. The prospective general baseline methods on planp.37 nevertheless name chi-square or Fisher exact for categorical variables. Report materials do not give an adjusted model, changed population, or alternative site/ethnicity contrast for these table6 P values.
- **Rule and calculations:** For the displayed site2×2 counts, Pearson chi-square=sum[(O−E)^2/E]=3.450589,df1,P=.063229; two-sided Fisher probability-orderingP=.070263. For all four displayed ethnicity categories, Pearson chi-square7.265468,df3,P=.063901; exact Fisher–Freeman–Halton probability-ordering enumerationP=.055087. The latter enumerates the2×4 tables with fixed row totals343,20,2,3 and group total108, summing probabilities no greater than the observed-table probability. These results are nonsignificant, unlike both printed P values. Known ethnicity only (excluding declined/unknown) gives PearsonP=.035335/FisherP=.043870, still not the printed.018; collapsing declined/unknown into nonHispanic givesPearsonP=.037000. Site alone supplies the same conclusion under both named categorical-test choices, regardless of ethnicity missing-category handling.
- **Display precision:** Counts are exact integers. Printed siteP interval[.0235,.0245] versus Pearson.063229 gives gap.038729/.024=1.61371; Fisher gap.045763/.024=1.90679. Printed ethnicityP interval[.0175,.0185] versus full-category Pearson.063901 gives gap.045401/.018=2.52228; exact Fisher–Freeman–Halton gap.036587/.018=2.03261. These exceed.05. For the significance/test conflict, RouteA category1 independently prevents rounding-based exclusion.
- **Focus area:** B,C. **Proposed review domain:** `statistical_results`. **Relationship type:** `S_W`.
- **Qualifying route:** Route A, category 1.
- **Affected result or extracted value:** The reported site and ethnicity differences between baseline HbA1c subgroups and their extractedP values/significance readings.
- **Why context does not resolve it:** The printed categorical tests cannot belong to the displayed tables under either supplied general categorical-test choice; site significance reverses. Same-display counts, groups and footnote match. The broad parenthetical methods pointer does not state a different population/model for the P values.
- **Alternatives and missing definitions:** An undisclosed adjusted analysis, different population, differently coded contrast, or one-sided convention could have generated anotherP. No such mapping is supplied; no one-sided baseline test is inferred. Unknown/declined ethnicity handling is explicitly tested in several ways above. The independent screener should consider whether the plan-to-report baseline-method pointer establishes category1 or whether the missing analysis mapping instead supports RouteB; the finding preserves both facts and this ambiguity.
- **Human question:** Which population, coding and categorical test/model generated siteP=.024 and ethnicityP=.018, and how do they map to the displayed108/260 participant groups?
- **Direct confirmation:** Fresh reportpp.28,29,44,45 and planp.37 source renders visually inspected, PyMuPDF1.28.0/200dpi/CPU. This issue consolidates the two P values from the same baseline-subgroup display; no external documentation or participant data were used.

## Successful and bounded reproduction checks

The primary L−8.2 exceeds−15 and agrees with the NI conclusion. Restricted, age-adjusted, MAR/MNAR, nonwear and cluster primary sensitivities also print L>−15. No conclusion about formal subgroup/component NI was imposed on descriptive intervals. Every displayed one-sided endpoint is below its point, all signs match the AI−human contrast and forest labels, and median/IQR cells were not treated as confidence intervals.

Sample-size normal diagnostic gives137.39 participants/arm, ceiling138, total276;25%attrition gives368. Pearson count tests reproduce initiationP=.001, completionP=.008, incident diabetes-rangeP=.78, prohibited-medicationP=.793 and restricted-sexP=.041 at displayed precision. Normal/finite-sample variance diagnostics reproduce the unadjusted displays without assuming the final variance implementation. The classIII subgroup interval receives the explicit multi-method diagnostic in S056 and is not selected as an anomaly merely because an ordinary Wald calculation differs. Raw age/rank, imputation, cluster, function-body and individual PA data were not supplied, and no invented definitions were used to manufacture exact tests.

## Excluded observations

These are apparent issues decided not to emit, listed once with one scope reason each. Reconciled routine checks above are not added to this table.

| Location | Observation | Reason code |
|---|---|---|
| R p.35 classIII subgroup (S056) | Ordinary one-sided Wald lower−.332 differs from printed−.5, but the same-display finite-sample variance diagnostic yields−.5019 and resolves the apparent discrepancy; no supplied exact CI method contradicts that construction. | NOT_REPRODUCED |
| R p.34 age-adjusted four rows (S041–S044) | Adjusted RDs differ from crude count contrasts, including the positive raw joint-component contrast versus adjusted0.3; the age-adjusted model is explicit. | MODEL_VERSUS_CRUDE |
| R p.45 eTable6 blanket “other” baselineP>.05 (S028) | Literal inclusion of its A1c group-defining variable would conflict with the separated ranges, but the main immediately frames these comparisons as factors affecting weight/PA; no explicit testP for the defining variable is given. This is an ambiguous blanket phrase, not a reproduced A1c interval/test conflict. | TERMINOLOGY_OR_WORDING |
| R p.47 eTable7 (S029) | No significant baseline differences is followed by parentheticalp<.05; the parenthetical denotes the significance threshold and the intended claim is evident. | NOTATION_OR_TYPOGRAPHY |
| R pp.43,45,47,54 copied age footnote (S027–S030) | Arm-ageP=.014 remains in subgroup/restricted baseline footnotes; original arm contrast is distinguishable from each table's contrast, and continuous ranks are unavailable for a matched re-test. | PERIPHERAL_COMPARISON |
| P p.37§9.3 versus§9.2 (S002) | General two-sided significance wording coexists with the explicitly one-sided NI confidence rule; no reported borderline test/CI decision conflicts and intended NI sidedness is immediate. | CONTEXT_RESOLVES |
| P p.37§9.4.1 (S025) | Printed Wilcoxon signed-rank alongside unpairedt-test for independent baseline arms is a recognizable test-name slip; report materials use rank-sum where named, and no result is linked to an actual paired test. | TERMINOLOGY_OR_WORDING |
| P p.81 stratification amendment versus M p.2 (S005) | <6.0 versus<=6.0 symbol leaves6.0 unassigned in the amendment prose; neighboring original6.0/6.1 strata and main assignment make the intended boundary evident. No population/model count is contradicted. | NOTATION_OR_TYPOGRAPHY |
| P p.35 safety windows (S075) | Nonserious/serious versusGrades1–2/3–5 labels for7/30days differ, but no supplied filled result, primary/key-secondary value, analysis-population size or decision trigger is linked to different ascertainment. | PERIPHERAL_COMPARISON |
| P pp.33,38 versus R p.13 (S016) | 75%wear-time repeat rule versus>=5of7 valid days uses distinct validity constructs; no supplied record shows a result-changing contradictory classification. | CONDITIONAL_OR_UNREPORTED |
| P pp.15,38–39,86–87 versus M p.3/R p.57 (S076–S083) | Deferred ordinary secondary analyses and explicit continuous descriptive replacement are acknowledged; none is designated key secondary or reported in the abstract. No primary/key-secondary analysis absence is selected from these nonkey deferred outcomes. | CONTEXT_RESOLVES |
| R p.16 three identical bout calls (S014) | Threshold-labeled calls use identical arguments, but the external function body and any published bout result are absent; no affected printed bout quantity or primary unbouted-PA contradiction is established from that fact alone. | CONDITIONAL_OR_UNREPORTED |
| R p.52 eTable10b versus p.29 method index (S032) | Chi-square versus binary rank-sum test names coexist; the printedP=.793 reproduces the count contrast and no significance/extraction reading changes. | CONTEXT_RESOLVES |
| M p.4 versus P p.88 software (S036) | Stata17 general report versus Stata18 for the disclosed MICE step can identify different analysis-stage software, with no result-changing output conflict. | CONTEXT_RESOLVES |

## Completion

PASS_1_COMPLETE for S001–S084;11 findings;14 excluded observations. Every primary/secondary/sensitivity/adjusted/subgroup inferential display was covered, together with full plan design and analysis specifications. Exact missing definitions and data limitations are recorded in the inventory. Eighteen CPU source-confirmation renders were created and inspected with PyMuPDF1.28.0,200dpi; no new OCR. No scientific coverage gap and no candidate-count target. All sources/reusable assets preserved.

## Explicit pass-1 relationship records

Coordinator mechanical validation repair: the following 84 rows are copied verbatim from the pass-1 agent-authored [relationship inventory](../statistics/relationship_inventory.md). They make the individually completed records explicit in this checker artifact without changing any review result, finding or scope.

| ID | Locations and populations | Printed specifications, checks, and missing definitions | Pass 1 |
|---|---|---|---|
| S001 | M pp.1–4; P pp.6,15,80–81,86; R pp.7,29–30 | Primary 12-month success: >=5% weight loss OR >=4% loss plus >=150 min/wk PA OR >=0.2 pp HbA1c decrease; report also requires HbA1c<6.5% throughout. Original/amended composite tracked by S018/S019; PA window by S015. Components overlap. | PASS_1_COMPLETE |
| S002 | M pp.1,2,4,7; P pp.36–37 | NI null: human advantage>=15 pp; alternative smaller advantage. Reported AI−human lower confidence bound must be>=−15. Primary lower bound−8.2 meets the rule. Generic two-sided plan wording is assessed separately. | PASS_1_COMPLETE |
| S003 | M p.4; P p.37 | Historical difference46.7 pp(95%CI43.1–50.2),47% versus0.3%; 50% preservation≈23.35 pp, selected15 pp;15/46.7≈32.12%. Ordered bounds contain the point. Historical rationale does not estimate current composite effect. | PASS_1_COMPLETE |
| S004 | M p.4; P p.37 §9.2 | Expected50% success per arm; one-sided alpha.05,power.80,margin.15. Normal diagnostic n=2(.5)(.5)(1.644854+.841621)^2/.15^2=137.39 per arm, ceiling138; total276;276/.75=368,184 per arm. Exact power engine unprinted; totals reproduce. | PASS_1_COMPLETE |
| S005 | M p.2/Figure1; R p.19; P pp.28,81 | Individual1:1 blocked allocation; site and A1c strata; blocks2,4,8. Original5.7–6.0/6.1–6.4 strata broadened after eligibility amendment. Report<=6.0 versus6.1–6.4; amendment<6.0. No count/model consequence supplied; symbol observation screened. Not cluster randomization. | PASS_1_COMPLETE |
| S006 | M p.4; R pp.27,30,50; P pp.37,86 | Report includes all368 randomized,183/185; missing26/29 twelve-month visits classified failure. Original excludes withdrawals/lacking data; disclosed change includes all randomized.313 observed+55 missing=368. F-ST1-007. | PASS_1_COMPLETE |
| S007 | M p.4; P pp.37–38,86; R pp.28–30 | Original mixed-effects logistic primary/secondary models with program-site clustering; implemented unadjusted binomial primary RD; post hoc clustering sensitivities. Primary model replacement F-ST1-006. Exact link/covariates not invented; coherent implemented choice not challenged. | PASS_1_COMPLETE |
| S008 | M pp.4–5/Figure1; R pp.27,30,41,53–54,58; P pp.16,37,86–87 | Original PP=program completers; implemented complete12-month outcomes/no prohibited medications151/149. Observed157/156 minus6/7=151/149,total300. Definition change F-ST1-009. Supportive analysis expressly not a causal adherence estimand. | PASS_1_COMPLETE |
| S009 | M pp.4,7; R pp.28,34–35; P p.86 | All secondary analyses exploratory/descriptive without multiplicity adjustment; primary NI is the formal decision. No adjusted threshold inferred; component/subgroup confidence bounds not treated as confirmatory conclusions. | PASS_1_COMPLETE |
| S010 | P p.38 §9.4.4; M pp.4,6; R p.35 | Planned site sensitivities for all outcomes; reported primary site subgroup rows exist. No assertion that these fulfill prespecified site-adjusted models. Deferred nonkey analyses retained under S076; no unspecified model inferred. | PASS_1_COMPLETE |
| S011 | P p.38 §9.4.5/7; M p.4; R pp.28,34 | Planned supportive adjustment for baseline/study-period imbalances, including glucose-influencing medications/incident diabetes. Reported age-adjusted RD names age. No significant medication imbalance established; no additional covariate requirement inferred. | PASS_1_COMPLETE |
| S012 | P pp.35,40–42; R pp.63–68; M pp.6,9 | No planned efficacy interim analysis. Safety trigger five probably-related Grade3 AEs; observed related events0, so trigger not met. No statistical efficacy stopping decision. Safety windows assessed under S075. | PASS_1_COMPLETE |
| S013 | R pp.13,18; P pp.33,86; M p.3 | PA threshold3941 vector-counts/min,>=10h/day valid,90min zeros define nonwear; within-day interpolation and invalid-day0 rules. Compliance>=5 of7 days. Day/week/month units distinguished. Pipeline gap S014; averaging gap S015. | PASS_1_COMPLETE |
| S014 | R pp.13–17 | Code computes ac_imp but activity_stats/BoutsOfPA consume ac, with no visible interpolation output passed to summaries: F-ST1-002. Three bout calls have identical arguments under different labels; external function absent and no published bout result, so no separate bout finding. | PASS_1_COMPLETE |
| S015 | R pp.13,30,49; P pp.6,15,80–81,86 | Report sums valid wear periods and divides available periods(max11), while missing intervals are assigned0. Whether zero-filled intervals enter denominator is unclear: F-ST1-003. Original primary window months6–11 versus all11 postbaseline periods: F-ST1-004; timeframe amendment does not print replacement window. | PASS_1_COMPLETE |
| S016 | P pp.33,38–39,86; R pp.13,49 | Original repeat wear if below75% of seven-day period; report>=5 valid days. Original primary MI if>5% missing and100%-complete valid-PA sensitivity; report0 nonwear. Wear validity and dataset missingness differ. Replaced primary missingness analysis F-ST1-008. Raw wear streams absent. | PASS_1_COMPLETE |
| S017 | P pp.33,77–80; R pp.8–9; M p.3 | A1c device/QC/venous substitution procedures; change<=−.9 or>=+.8 triggers review. Report device counts334+33+1 baseline,282+30 follow-up. Devices changed through disclosed amendments. Raw paired assay readings absent; no external assay-validation claim checked. | PASS_1_COMPLETE |
| S018 | P pp.6,15,80–81; M pp.3,7; R pp.34,41,58 | Original A1c-change component general; amendment restricts baseline5.7–6.4; report130/130,restricted106/103. Disclosed primary-composite subset change F-ST1-010. Range wording is understood rather than two exact endpoint values. | PASS_1_COMPLETE |
| S019 | P pp.15,31,70,86; M pp.3–4; R pp.30,55–56 | Incident diabetes does not end follow-up but added HbA1c>=6.5 at6/12 months disqualifies composite regardless of other branches. Retention differs from outcome failure. Disclosed composite change F-ST1-005. | PASS_1_COMPLETE |
| S020 | M pp.3–4; P pp.7,13–16,38–40,87–90; R pp.28–31 | Outcome roles matched by content. Initiation and demographic/clinical subgroups called post hoc in report/nonprespecified in disclosure. Prespecified secondary outcomes remain secondary despite descriptive interpretation. Deferred analyses S076–S083. | PASS_1_COMPLETE |
| S021 | M pp.3–4,9; P pp.14–16; R p.30 | AI completion>=8 engagement weeks in months1–6 with>=9-month span; human>=8 sessions with>=9-month span. Planned human engagement denominators8/3/11 sessions; full app weeks; capped100%. Different effort/intensity acknowledged, not assumed equivalent. | PASS_1_COMPLETE |
| S022 | M pp.1,4–5,9; P p.89 | Initiation171/183 versus153/185;93.4%/82.7%,chi-squareP=.001. Pearson statistic10.0803,df1,P=.0014987 is within.001±.0005. Definitions app registration/use versus first session. | PASS_1_COMPLETE |
| S023 | M pp.4–5,9; P p.16 | Completion117/183 versus93/185;63.9%/50.3%,chi-squareP=.008. Pearson statistic7.0107,df1,P=.0081026 rounds.008. | PASS_1_COMPLETE |
| S024 | M pp.4–5; R p.56; P p.15 | Diabetes-range HbA1c8/183 versus7/185;4.4%/3.8%,chi-squareP=.78. Pearson statistic.081295,df1,P=.77555 rounds.78. Fifteen trajectories are participants rather than confirmed clinical diagnoses. | PASS_1_COMPLETE |
| S025 | M p.6 Table; R pp.39–40 | Randomized baseline: all rows covered by mainN026–N068 and R2-N04. AgeP=.01/.014 within display precision; other characteristicsP>.05. Age ranks unavailable; median/IQR cannot reproduce rank test. Main sex121/183 versus139/185 gives PearsonP>.05. | PASS_1_COMPLETE |
| S026 | R p.41 and eMethods pp.28–29 | Eligibility primary183/185 and restricted151/149; all three laboratory categories and glycemic summaries covered. Randomized3x2 Pearson statistic5.0090,df2,P=.08172 supports nonsignificant categorical claim. Continuous ranks absent. | PASS_1_COMPLETE |
| S027 | R pp.42–43 | Site baseline243/125; ageP=.017,race/marital/education/MVPAP<.001. All cells read; median/IQR not CI. Rank data unavailable for continuous tests. Categorical directions/totals coherent. Copied treatment-arm age footnote separated from site contrast. | PASS_1_COMPLETE |
| S028 | R pp.44–45; R method index pp.28–29; P p.37 §9.4.1 | A1c-status groups108/260; siteP=.024,ethnicityP=.018. Source method chain and exact categorical tests documented in F-ST1-011: site PearsonP=.063229/Fisher.070263; ethnicity full-category PearsonP=.063901/Fisher–Freeman–Halton.055087. Both printed significance readings differ. Blanket 'other' wording separately excluded. | PASS_1_COMPLETE |
| S029 | R pp.46–47 | Completers313/dropout55; no significant baseline differences with parentheticalp<.05; copied treatment-arm ageP=.014. Comparator populations distinguished. Age ranks unavailable. Marital3x2 Pearson statistic4.99647,P=.08223. Evident threshold notation screened. | PASS_1_COMPLETE |
| S030 | R pp.53–54 | Restricted151/149; ageP=.010,sexP=.041,othersP>.05. Sex96/151 versus111/149 Pearson statistic4.18134,P=.0408713 rounds.041. Copied age.014 separated from restricted contrast; continuous ranks absent. | PASS_1_COMPLETE |
| S031 | R pp.29,51; P p.89 | Visits6mo164/161 and12mo157/156; windows168–196/351–379; outside10/10 and7/12. Outside12mo means20.14±13.17 versus6.67±5.18,P=.016; supplied Wilcoxon rank-sum test rather than a test inferred from means. Individual ranks absent. | PASS_1_COMPLETE |
| S032 | R pp.29,52; M Figure1 | Prohibited medication6/183 versus7/185,P=.793; method index chi-square/table footnote rank-sum. Pearson statistic.0688724,P=.792986 supports value; binary tie-corrected rank test comparable. No result-changing conflict or preferred method. | PASS_1_COMPLETE |
| S033 | M p.6; R pp.39–54; P pp.54,86 | One missing diet item of8 imputed1 of0–2; score0–16. Three invalid baseline Actigraphy values imputed0. Raw monthly missing counts8/5 at baseline and17/21 through60/65 atmonth11 reflect different missingness definitions. No equality inferred between raw missing and no valid data after outreach. | PASS_1_COMPLETE |
| S034 | M pp.2–3; R pp.21–26; P pp.22–23 | Individual adaptive AI algorithm1.0; pooled pretraining and individual-only trial learning. No intervention-input imputation. Intervention input handling differs from outcome imputation; no model/causal claim inferred. | PASS_1_COMPLETE |
| S035 | M p.3; R p.38; P pp.26,65–66,84 | Human intervention12 months,16 weekly core sessions then maintenance; all reported synchronous distance learning. Plan permits both modes and discloses COVID video transition. Actual four programs63/60/3/59 versus planning five; cluster definitions use four. Administrative comparison has no result-changing implication. | PASS_1_COMPLETE |
| S036 | M p.4; P p.88 | Report R/Stata17; MICE disclosure Stata18. Different analysis-stage software versions possible, with no printed numerical conflict tied to version. No external documentation used. | PASS_1_COMPLETE |
| S037 | M pp.1,4,7 Figure2; R p.35overall;primary ITT12mo | 58/183;59/185 | −0.2;−8.2;NI holds | PASS_1_COMPLETE |
| S038 | M p.7 Figure2;>=5%weightlossITT | 31/183;37/185 | −3.1;−9.7;descriptive | PASS_1_COMPLETE |
| S039 | M p.7 Figure2;>=4%loss+PA150ITT | 23/183;23/185 | 0.1;−5.5;descriptive | PASS_1_COMPLETE |
| S040 | M p.7 Figure2;A1creductionITTbaseline5.7–6.4 | 35/130;35/130 | 0;−9.1;descriptive | PASS_1_COMPLETE |
| S041 | R pp.28,34 eFigure3;age-adjusted primary | 58/183;59/185 | −2.0;−9.8;NI holds | PASS_1_COMPLETE |
| S042 | R p.34;age-adjusted>=5%loss | 31/183;37/185 | −3.4;−9.8;descriptive | PASS_1_COMPLETE |
| S043 | R p.34;age-adjusted>=4%loss+PA150 | 23/183;23/185 | 0.3;−4.7;descriptive | PASS_1_COMPLETE |
| S044 | R p.34;age-adjustedA1creduction | 35/130;35/130 | −1.6;−10.7;descriptive | PASS_1_COMPLETE |
| S045 | R p.35 eFigure4;Baltimoreprimary subgroup | 36/120;43/123 | −5.0;−14.9;descriptive | PASS_1_COMPLETE |
| S046 | R p.35;Reading | 22/63;16/62 | 9.1;−4.4;descriptive | PASS_1_COMPLETE |
| S047 | R p.35;female | 36/121;42/139 | −0.5;−9.9;descriptive | PASS_1_COMPLETE |
| S048 | R p.35;male | 22/62;17/46 | −1.5;−16.9;descriptive | PASS_1_COMPLETE |
| S049 | R p.35;age<65 | 32/119;40/148 | −0.1;−9.1;descriptive | PASS_1_COMPLETE |
| S050 | R p.35;age>=65 | 26/64;19/37 | −10.7;−27.7;descriptive | PASS_1_COMPLETE |
| S051 | R p.35;A1c<6.0 | 37/123;38/135 | 1.9;−7.4;descriptive | PASS_1_COMPLETE |
| S052 | R p.35;A1c>=6.0 | 21/60;21/50 | −7.0;−22.4;descriptive | PASS_1_COMPLETE |
| S053 | R p.35;overweight | 17/55;13/47 | 3.2;−11.7;descriptive | PASS_1_COMPLETE |
| S054 | R p.35;classI obesity | 20/70;23/57 | −11.8;−25.7;descriptive | PASS_1_COMPLETE |
| S055 | R p.35;classII obesity | 11/33;16/47 | −0.7;−18.5;descriptive | PASS_1_COMPLETE |
| S056 | R p.35;classIII obesity | 10/25;7/34 | 19.4;−0.5;descriptive | PASS_1_COMPLETE |
| S057 | R p.58 eTable15;restricted primary | 54/151;53/149 | 0.2;−8.9;supportive NI | PASS_1_COMPLETE |
| S058 | R p.58;restricted>=5%loss | 28/151;33/149 | −3.6;−11.3;descriptive | PASS_1_COMPLETE |
| S059 | R p.58;restricted>=4%loss+PA150 | 22/151;22/149 | −0.2;−6.9;descriptive | PASS_1_COMPLETE |
| S060 | R p.58;restricted A1c reduction | 33/106;31/103 | 1.0;−9.5;descriptive | PASS_1_COMPLETE |
| S061 | R p.59 eTable16;P p.88;MI20 datasets,MAR | MIpooled32.2%;31.9% | −1.1;−11.5;NI holds;F-ST1-001 | PASS_1_COMPLETE |
| S062 | R p.60 eTable17;P p.88;MNARpatternmixture | 58/183;70/185 | −6.1;−14.3;NI holds | PASS_1_COMPLETE |
| S063 | R p.61 eTable18a;P pp.89–90;nonwear best case | 58/183;60/185 | −0.74;−8.8;NI holds | PASS_1_COMPLETE |
| S064 | R p.61 eTable18b;P p.90;all attain PA goal | 58/183;60/185 | −0.74;−8.8;NI holds | PASS_1_COMPLETE |
| S065 | R p.62 eTable19a;P pp.88–89;5 clusters | 58/183;59/185 | −0.20;−4.8;NI holds | PASS_1_COMPLETE |
| S066 | R p.62 eTable19b;P p.89;78site-month clusters | 58/183;59/185 | −0.20;−6.8;NI holds | PASS_1_COMPLETE |
| S067 | M p.8 Figure3; R p.57 eTable14; restricted percent weight change151/149:−1.03[−3.73,1.46] versus−1.43[−4.03,1.14] | Medians lie within ordered IQRs; noCI/P printed. Individual waterfall heights unprinted and not invented. | PASS_1_COMPLETE |
| S068 | R p.57; restricted kg weight change151/149:−1.00[−3.20,1.50] versus−1.30[−4.30,1.10] | Medians/IQRs contain points. Percent and absolute change are distinct units; no conversion of medians from aggregate weights. | PASS_1_COMPLETE |
| S069 | M p.8 Figure3; R p.57; restricted A1c106/103:0.0[−.2,.1] versus−.1[−.2,.1] | Baseline-prediabetes subset, median change, noformalP. Waterfall labels151/149 may include normoglycemic individuals; different display populations retained without invented participant-level comparisons. | PASS_1_COMPLETE |
| S070 | M p.8 Figure3; R p.57; restricted PA151/149:210.5[134.5,344] versus174.4[73.9,321.25]min/wk | Ordered IQRs contain medians; PA window S015 affects interpretation. IQRs are not used for CI/test calculations. | PASS_1_COMPLETE |
| S071 | M pp.5,7,9 Figure4; all randomized engagement/outcome matrices | AI failures9/42/74,successes3/12/43; human failures23/43/60,successes9/17/33. Engagement totals12/54/117=183 and32/60/93=185. Conditional success25/22/37 versus28/28/35%; success shares5/21/74 versus15/29/56 use appropriate column/row totals. No association test printed. | PASS_1_COMPLETE |
| S072 | R p.55 eTable12; M Figure2 | Seven combinationsABC/AB/AC/BC/A/B/C: AI5/14/6/1/6/3/23; human10/10/5/1/12/2/19; totals58/59. Denominators are achievers. Weight5% margins31/37,joint23/23,A1c35/35 matchFigure2; diabetes disqualifier retained. Printed human10(19%) AB handled by numeric lane. | PASS_1_COMPLETE |
| S073 | R pp.63–68 eTable20, all rows; M pp.6,9 | Participants>=1AE66/183 versus21/185; events100/25; grades13/42/43/2 versus5/11/8/1; related0 and unrelated100/25. All categories/conditions by grade covered in R2-N28–N31. No AE inference printed. Participants and events are different denominators. | PASS_1_COMPLETE |
| S074 | P pp.34–36,72,83; R pp.63–68 | Safety definitions and grades distinguished; seriousness is not identical to severity grade. No formal AE efficacy/stopping inference. New-problem/attribution questionnaire has no filled values. | PASS_1_COMPLETE |
| S075 | P p.35 §8.4.4/5; M pp.6,9; R pp.63–68 | Seven/thirty-day windows labeled nonserious/serious thenGrades1–2/3–5. No supplied result timing identifies an affected primary/key-secondary value,analysisN or trigger. Peripheral plan observation retained in excluded table. | PASS_1_COMPLETE |
| S076 | M p.3; P pp.13–16,38–40,87 | Complete deferred inventory: self-report composite; objective/self-report correlation; engagement/mediation; acceptability; well-being; response predictors; cost-effectiveness; other PA metrics;6mo outcomes. None designated key secondary in plan/abstract. Deferral explicit; no absence-only finding. | PASS_1_COMPLETE |
| S077 | P pp.15,38,86; M pp.3–4; R p.57 | Planned continuous linear/mixed-effects analyses changed to descriptive medians/IQRs withoutP; report matches disclosure. Ordinary secondary inferential choice explicit; not treated as primary or key-secondary inference. | PASS_1_COMPLETE |
| S078 | P pp.14–16,38,56,87,89; M pp.3–4 | Planned engagement mediation,within-arm response factors and NPART effect modification; clinical-demographic subgroups reported post hoc. No assertion these fulfill all planned interaction/mediation analyses. Individual covariates/ranks absent. | PASS_1_COMPLETE |
| S079 | P pp.60–64,38–39; M p.3 | Acceptability31 scored items/155×100,reverse15/17/30/31; features21 items/105×100,reverse13/14/20/21; WHO5sum0–25×4; NPS%promoters−%detractors. Planned item Spearman/chi-square,overall Pearson/t tests. No populated outcomes;20–100% and0–100 ranges coherent. | PASS_1_COMPLETE |
| S080 | P pp.14–15,33,79; M p.3; R p.13 | Planned PA self-report/objective validation correlation; survey timing amended from preceding week to after worn week. No reported estimate/CI/P or paired raw data; no preferred validation method. | PASS_1_COMPLETE |
| S081 | P pp.15,39,67; M p.3 | Planned12mo/lifetime health-system cost-effectiveness;3% discount; Markov normal glucose/IFG/IGT/diabetes/death; QALYtime×utility; ICERcostdifference/effectdifference; probabilistic/univariate sensitivities. No results; ordinary secondary, no absence-only finding. | PASS_1_COMPLETE |
| S082 | P pp.14–16; M pp.5,7,9 | Planned60% CDC benchmark among program completers distinct from randomized NI. Descriptive43/117≈37% versus33/93≈35% does not claim60% attained. Ordinary secondary benchmark analysis deferred rather than presumed performed. | PASS_1_COMPLETE |
| S083 | P pp.31,37,86; M Figure1 and p.4 | Original withdrawal replacement statement versus fixed368/finalITT. No supplied replacement/extra-randomized count. Final flow accounts for all368; no replacement cohort invented. | PASS_1_COMPLETE |
| S084 | P pp.9–10,28,76–80; M pp.3–4; R pp.20,29,51 | Outcome clock from randomization rather than first session. Actigraphy final345-day amendment;12mo365±14-day window; mean visit days366.78/367.42. No off-window participant-level endpoint reassignment inferred. Program and trial-completion clocks distinguished. | PASS_1_COMPLETE |
