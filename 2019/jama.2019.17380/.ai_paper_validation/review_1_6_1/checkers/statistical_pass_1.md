# Statistical consistency review — pass 1

Runtime task: /root/statistics_pass1. Fresh qc161_statistical_consistency_reviewer, gpt-6.1-sol/high, FRESH_SPAWN. The exact distinct runtime agent ID is supplied by the coordinator's spawn record and recorded in agent_execution_manifest.md; this agent is not reused for pass 2.

## Completed scope

All 64 supplied physical PDF pages are represented in the current complete main/support maps. Inferential scope covers REPORT main article pp. 1–11, PLAN protocol/addendum pp. 1–33, REPORT results supplement pp. 1–19; the REPORT data-sharing statement p. 1 has no applicable inferential relationship. Pass 1 establishes and checks 140 stable records, including all 42 complete outcome-table row families, all 52 graphical overall/subgroup rows with attached interaction tests, all 14 event/rate/RD/HR/P tuples, and all current-trial summary, method, power, analysis-population and decision rules. The canonical inventory is statistics/relationship_inventory.md. Table/forest grouping is transparent, complete and does not sample relationships.

Exact completed S scope: S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, S113, S114, S115, S116, S117, S118, S119, S120, S121, S122, S123, S124, S125, S126, S127, S128, S129, S130, S131, S132, S133, S134, S135, S136, S137, S138, S139, S140.

Every listed S ID is PASS_1_COMPLETE. Current source-linked map transcriptions, direct pdftotext -layout selected-page output and reusable source-page renders were used. Direct text reads included main pp. 3, 4, 6, 8, 9; supplement pp. 6, 9–15; protocol pp. 17–20, 23, 31–33. Visual confirmation included main pp. 8–9 and supplement pp. 18–19; protocol pp. 32–33 were inspected for the findings. All other source units are accounted for in complete mapper page records. No legacy candidate/checker/report conclusions or external sources were used. No derivative, source or reused asset was changed.

## Check results and rules

Every displayed current-trial point estimate lies inside its printed interval, and lower/upper endpoints are ordered. All six primary year-five intervention/change families and every sensitivity year-five contrast support the stated nonsignificant results. All primary eGFR graphical CIs cross zero; all secondary ACR graphical CIs cross one; every displayed subgroup interaction P exceeds .05. Individual subgroup point signs match the numerical arm changes and active-minus-placebo or active/placebo scales. Confidence intervals for the specified beneficial eGFR effect exclude 3.75 mL/min/1.73 m² because their upper limits are 2.5 and 2.6, consistent with the discussion. No noninferiority or equivalence inference was stated, and no such margin was invented.

The main report specifies a two-sided .05 treatment-by-year-five test, 95% intervals, random-intercept mixed models and Rubin combination. A normal diagnostic using a CI-derived SE gives approximately P=.27 for D and P=.29 for omega-3 when printed point estimates are treated as exact; half-unit display intervals allow reported P=.25/.27, and Rubin degrees of freedom/test implementation are not printed. This diagnostic is not substituted for the reported analysis. For Cox rows, the supplied source does not establish whether P comes from Wald, likelihood-ratio or score testing, the confidence procedure, event-timing/tie implementation or variance estimator. Null inclusion and direction were checked, but exact inversion under an assumed Wald test was not treated as a source-established rule. Counts divided by rates were not used to reconstruct unreported individual person-time.

The original ANCOVA power table has source-defined allocation, SD, baseline correlation and alpha inputs. A normal diagnostic residual SE is approximately .05745 for log ACR and .7964 for eGFR. Using the twelve displayed effects gives approximate ACR powers 80.8%, 90.0%, 95.6%, 98.4%, 99.5%, 99.9% and eGFR powers 70.9%, 78.9%, 85.4%, 90.4%, 94.4%, 97.0%, matching the printed rounded entries. Attrition and separate-treatment-combination power relationships are approximately compatible. The amended 2.3-difference power uses 2000 simulations and preliminary data not supplied in the addendum; exact reproduction cannot be undertaken without those variability/covariance and missingness inputs. Parent Haybittle-Peto guidance at z=3 corresponds to two-sided normal P≈.00270 and explicitly concerns parent cancer/CVD primary endpoints, rather than establishing an ancillary DKD interim test.

Three observations meet the self-screened inclusion threshold below. They concern planned-versus-reported statistical specification; they do not question the internal coherence of a stated reported method and do not recommend a preferred analysis.

## Findings

### F-ST1-001

**Title:** Amended-plan biosample-defined inclusion and reported all-randomized primary population differ.

**Exact locations and roles:** PLAN [joi190122supp1_prod.pdf, physical p. 32, §15c](../../../joi190122supp1_prod.pdf#page=32), read with PLAN [p. 31 addendum provenance](../../../joi190122supp1_prod.pdf#page=31); REPORT [jama_de_boer_2019_oi_190122.pdf, physical p. 3, Data Analysis](../../../jama_de_boer_2019_oi_190122.pdf#page=3); REPORT [p. 6, Figure 1 primary-analysis and follow-up boxes](../../../jama_de_boer_2019_oi_190122.pdf#page=6); REPORT [p. 4, primary results and biosample retention](../../../jama_de_boer_2019_oi_190122.pdf#page=4). The bound addendum remains PLAN.

**Printed values/statements:** §15c defines intent-to-treat inclusion as all participants who return at least one follow-up biosample, irrespective of adherence or later characteristics. The report instead says all participants were analyzed according to randomized group regardless of adherence or follow-up, using multiple imputation. Figure 1 includes 370, 333, 289 and 320 participants in primary analyses; the same four groups have 303, 280, 242 and 265 returning any follow-up blood sample. Narrative follow-up urine return is 1091.

**Rule and calculation:** Compare the operational inclusion criterion of the latest supplied plan with that used for the reported primary result, rather than equating the two uses of the intent-to-treat label. Primary-analysis boxes sum to 1312; follow-up blood boxes sum to 1090, leaving 222 primary participants without follow-up blood. The report expressly admits participants regardless of follow-up, while the amended plan names follow-up biosample return in its definition. The blood and urine overlap is unreported; 1090 is not asserted to be the exact planned any-biosample population, and no actual planned union size is invented. This is a discrepancy in inclusion specification, with its numerical effect unresolved.

**Focus area:** D, analysis population and handling of missing data. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R. **Statistical relationships:** S119, S120; primary contrasts S003 and S006.

**Affected result or extracted value:** Primary five-year eGFR differences 0.9 (95% CI −0.7 to 2.5) for vitamin D and 0.9 (−0.7 to 2.6) for omega-3, and their analysis-population/missing-data classification in evidence extraction.

**Why context does not resolve it:** The original plan was explicitly amended, so the current comparison uses §15c, not the superseded complete-case plan. Both current descriptions are clear individually, but the source package does not disclose how the follow-up-return condition was removed or how participants with no follow-up biosample entered the primary imputation population. Shared intent-to-treat terminology does not reconcile these operational definitions.

**Alternatives and missing definitions:** A later unsupplied amendment may have expanded inclusion; the §15c wording may have been intended as a minimum inclusion commitment rather than an exclusion condition; or blood and urine return could have produced a larger union than either marginal count. Exact overlap and later amendments are absent. None permits asserting a particular unreported planned N or a particular change to the estimated treatment effects.

**Exact human question:** How should the reported all-randomized primary population be classified against the supplied amended-plan follow-up-biosample inclusion definition, and what amendment or operational definition connects them?

### F-ST1-002

**Title:** Reported primary adjustment terms differ from the amended primary model and conditional sensitivity covariates.

**Exact locations and roles:** PLAN [joi190122supp1_prod.pdf, physical p. 32, §15e Equation 2 and sensitivity paragraph](../../../joi190122supp1_prod.pdf#page=32); PLAN [p. 33, continuation](../../../joi190122supp1_prod.pdf#page=33); REPORT [jama_de_boer_2019_oi_190122.pdf, physical p. 3, Data Analysis](../../../jama_de_boer_2019_oi_190122.pdf#page=3); REPORT [p. 8, Table 2 footnote a](../../../jama_de_boer_2019_oi_190122.pdf#page=8). Supporting REPORT model footnotes occur in [joi190122supp2_prod.pdf pp. 9–10, eTables 4–5](../../../joi190122supp2_prod.pdf#page=9) and [p. 10](../../../joi190122supp2_prod.pdf#page=10).

**Printed values/statements:** Amended Equation 2 contains intercept, vitamin D assignment, categorical time, treatment-by-time, participant random intercept and residual. Corresponding omega-3/log ACR equations are specified. Additional baseline characteristics are assigned to sensitivity analyses if baseline groups are imbalanced. The report's primary model contains age, sex and their time interactions; eGFR also contains baseline urine ACR and its time interaction. Table 2 says the primary difference is derived from an age-, sex- and baseline-ACR-adjusted mixed model.

**Rule and calculation:** Compare the latest plan's specified primary fixed-effect terms and conditional sensitivity rule with the fixed-effect terms used for the reported primary contrast. The report adds three named baseline covariate groups and their time interactions to the primary eGFR model, rather than identifying them as the planned conditional sensitivity analyses. No arithmetic is needed, and no claim is made that either model is internally incoherent.

**Focus area:** D, primary analysis model and covariates. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R. **Statistical relationships:** S121, S122; primary contrasts S003 and S006.

**Affected result or extracted value:** The adjusted primary five-year intervention effects, their confidence intervals/P values, and the planned-versus-reported primary-model specification extracted for synthesis.

**Why context does not resolve it:** The report clearly identifies its adjusted model, but the dated supplied addendum identifies a different primary equation and assigns additional baseline adjustments to a conditional sensitivity step. The package does not state that these added terms became the primary specification through another amendment or that Table 2 is the conditional sensitivity model. An evidence extractor cannot silently classify the reported adjusted primary model as the exact supplied planned equation.

**Alternatives and missing definitions:** A later unsupplied analysis specification could authorize these fixed terms; the printed plan equation could have been shorthand with covariates omitted; or the primary table could implement the plan's sensitivity adjustment after a documented imbalance. That supporting specification or trigger is absent. The observation concerns specification correspondence, not a preferred covariate strategy or an unreported magnitude of estimate change.

**Exact human question:** Which supplied or later analysis specification connects the amended primary Equation 2 and conditional baseline-adjustment rule to the age-, sex- and baseline-ACR-adjusted primary model reported in Table 2?

### F-ST1-003

**Title:** Primary-outcome adherence sensitivity uses a different threshold and continuity definition from the amended plan.

**Exact locations and roles:** PLAN [joi190122supp1_prod.pdf, physical p. 33, §15g](../../../joi190122supp1_prod.pdf#page=33), corroborated by PLAN [p. 19, §VI.g](../../../joi190122supp1_prod.pdf#page=19); REPORT [jama_de_boer_2019_oi_190122.pdf, physical p. 3, Covariates and Data Analysis](../../../jama_de_boer_2019_oi_190122.pdf#page=3); REPORT [p. 4, primary sensitivity statement](../../../jama_de_boer_2019_oi_190122.pdf#page=4); REPORT [joi190122supp2_prod.pdf, physical p. 10, eTable 5 definition and results](../../../joi190122supp2_prod.pdf#page=10); REPORT [p. 6, eTable 1 footnote](../../../joi190122supp2_prod.pdf#page=6). The same definition also affects secondary ACR sensitivity in REPORT [p. 13, eTable 8](../../../joi190122supp2_prod.pdf#page=13).

**Printed values/statements:** The addendum specifies continuous adherence to at least 80% of medications. The report defines high adherence as at least two-thirds use; eTable 5 requires this on at least four questionnaires among six assessments at 6 months and years 1–5, yielding N=1032 per intervention. Its five-year eGFR contrasts are vitamin D 0.89 (95% CI −0.74 to 2.52), P=.28; omega-3 0.42 (−1.22 to 2.06), P=.61. eTable 8 repeats the population definition for ACR.

**Rule and calculation:** Compare the planned and reported membership predicates, retaining both pill-use threshold and continuity requirement. Two-thirds is approximately 66.7%, 13.3 percentage points below 80%; four of six qualifying assessments allow two nonqualifying or unavailable assessments, whereas continuous ≥80% is the plan's requirement. These are distinct predicates, not display precision or two names for the same population. One repeated definition pattern covers both interventions and both eTables.

**Focus area:** D, prespecified primary-outcome sensitivity population and analysis definition. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R. **Statistical relationships:** S127; eGFR families S013–S018 and ACR families S031–S036.

**Affected result or extracted value:** The eTable 5 adherence-restricted five-year eGFR effect estimates and the narrative inference that the primary null results persist among consistently highly adherent participants; secondarily the eTable 8 ACR sensitivity population.

**Why context does not resolve it:** The threshold and assessment count are explicit, but no supplied amendment maps continuous ≥80% to ≥2/3 at four of six assessments. Labeling both populations adherent does not make membership equivalent. An extractor must retain the reported weaker threshold and assessment rule rather than describe these estimates as the supplied planned continuous-80% sensitivity.

**Alternatives and missing definitions:** The available adherence questionnaire categories may have led to a revised operational definition, or a later amendment may have adopted the reported rule. The package does not provide that linkage or the N satisfying continuous ≥80%; no alternative effect estimate or preferred definition is proposed.

**Exact human question:** What documented operational change connects the planned continuous ≥80% adherence analysis to the reported ≥2/3-at-four-of-six subset, and how should these sensitivity estimates be labeled in review?

## Excluded observations

Each observation below has exactly one scope reason code and no finding ID. A repeated display/model pattern is listed once.

| Location | Observation | Reason code |
|---|---|---|
| Main PDF p. 8 Table 2; supplement pp. 9–10 eTables 4–5 | Rounded arm changes sometimes subtract to .8 while a modeled contrast prints .9/.89, or subtract to −.2 while −.3 is printed. Half-unit rounding intervals overlap the contrast interval; the quantities are also modeled. | ROUNDING_OR_DISPLAY_PRECISION |
| Main PDF p. 8 Table 2 | Normal diagnostics from rounded primary estimates/intervals need not exactly reproduce .25/.27; source-defined Rubin degrees of freedom and full test implementation are absent, and display ranges permit these values. | ROUNDING_OR_DISPLAY_PRECISION |
| Main PDF p. 9 Table 3, D ACR doubling | P=.05 and HR lower CI=1.00 are compatible with the narrative nonsignificance under a strict P<.05 rule; unrounded values can include 1 with P at or above .05. | ROUNDING_OR_DISPLAY_PRECISION |
| Main p. 9 Table 3; supplement p. 15 eTable 10 | Incidence-rate differences such as 2.7−2.5 versus .3, 3.4−4.2 versus −.7, and 3.3−3.9 versus −.5 reconcile with half-unit rounding ranges. | ROUNDING_OR_DISPLAY_PRECISION |
| Supplement pp. 11–14 eTables 6–9 | Ratios of rounded marginal changes do not invariably equal adjusted ratio contrasts, and subtracting observed geometric means does not reproduce modeled longitudinal effects. | MODEL_VERSUS_CRUDE |
| Main pp. 8–9 Figures 3–4; supplement pp. 18–19 eFigures 2–3 | Computing subgroup SEs/tests from printed N/SD or crude ratios would substitute an unadjusted calculation for an imputed adjusted longitudinal model. Count-column attribution is separately available to numeric/cross-source reviewers; no reconstructed crude P is a statistical finding. | MODEL_VERSUS_CRUDE |
| Main p. 9 Table 3; supplement p. 15 eTable 10 | Cox HRs differ from event-count risks or incidence-rate ratios; source labels HRs as model estimates. | MODEL_VERSUS_CRUDE |
| Main p. 9 Table 3; supplement p. 15 eTable 10 | Exact CI/P inversion assuming a Wald test, variance estimator or tie method is conditional on details the package does not establish. | CONDITIONAL_OR_UNREPORTED |
| Supplement pp. 18–19 eFigures 2–3 | Favor arrows are opposite to lower-ACR benefit, but the explicit active/placebo ratio, arm changes and endpoint context make the intended numerical effect direction immediately identifiable. | CONTEXT_RESOLVES |
| Supplement pp. 18–19 eFigures 2–3 | Overall treatment P is placed in an interaction column, and captions say active assignment compared to year 5; overall result and active/placebo contrast identify the intended reading. | CONTEXT_RESOLVES |
| Supplement p. 17 eFigure 1 | Omega axis DHA/EPA differs from the caption's omega-3 index, but the caption and main p. 3 definition identify EPA plus DHA as percentage of total fatty acids. | TERMINOLOGY_OR_WORDING |
| Supplement p. 17 eFigure 1; main p. 4 | N, precise correlation estimator, test and CI are unreported, so a contradiction in the weak-correlation nonsignificance statement cannot be established. | CONDITIONAL_OR_UNREPORTED |
| Plan p. 33 §15g; supplement p. 17 | Graphical r summaries alone do not demonstrate that planned biomarker-substitution mixed models were not run or were replaced. | CONDITIONAL_OR_UNREPORTED |
| Plan p. 33 §15f; main p. 3 and Figures 3–4 | A bioavailable-vitamin-D subgroup result is not displayed, but no conflicting existing result or replaced primary estimate is established solely by that absence. | CONDITIONAL_OR_UNREPORTED |
| Plan p. 32 §15c; main p. 3 | Ten planned versus twenty reported imputations is a computational difference without an independently demonstrated change to an extracted result or decision rule. | CONTEXT_RESOLVES |
| Main p. 3; supplement pp. 9 and 12 eTables 4 and 7 | Baseline/year 5 complete-case populations can retain missing year 2 outcomes or covariates, so an MI footnote does not by itself conflict with endpoint-complete restriction. | CONTEXT_RESOLVES |
| Plan p. 32 interaction Equation 1 versus primary Equation 2 | Omission of the time-only term in the interaction equation is identifiable from categorical-time text and the neighboring equation; no conflicting applied interaction result is established. | NOTATION_OR_TYPOGRAPHY |
| Plan p. 19 Table 2 and outcome section p. 17 | Original co-primary power-table heading versus explicit primary ACR/secondary eGFR sections is resolved by the named outcome section and the later primary-endpoint amendment. | CONTEXT_RESOLVES |
| Plan pp. 17–18 | Secondary dichotomous eGFR wording is immediately followed by its explicit continuous definition; log-ACR contrast percent-change terminology does not supply a second competing estimate. | TERMINOLOGY_OR_WORDING |
| Plan pp. 17 and 32; main p. 2 | Original four-year and addendum intermediate two-year follow-up histories are superseded by the clearly disclosed baseline-to-five-year current endpoint. | CONTEXT_RESOLVES |
| Plan p. 33 power; main p. 3 | 1058 is approximately 80% of the 1320 target; 1320×.8=1056 is a small approximation difference, not a demonstrated changed power decision. | ROUNDING_OR_DISPLAY_PRECISION |
| Plan p. 33 power Figure 7; main p. 3 | Exact 2.3-difference simulation power cannot be reconstructed without referenced preliminary variance/covariance and missingness inputs. Missing inputs alone do not show incompatible power. | CONDITIONAL_OR_UNREPORTED |
| Plan p. 23 | Parent interim rule does not establish ancillary DKD interim testing, and no supplied DKD interim/stopping result contradicts a stated DKD rule. | CONDITIONAL_OR_UNREPORTED |
| Plan p. 33 discrete Cox; main p. 3 Cox description | Discrete Cox versus Cox wording alone does not prove a different model; event timing and tie details are not supplied. | TERMINOLOGY_OR_WORDING |
| Main p. 3 and p. 6 PH statement | Unreported test statistics/individual P values do not contradict the statement that no significant PH violations were observed. | CONDITIONAL_OR_UNREPORTED |
| Plan p. 17; main p. 3 | The current CKD-EPI formula is referred to but not printed; a source-only algebraic discrepancy with the original equation cannot be inferred from citation labels. | CONDITIONAL_OR_UNREPORTED |
| Main p. 3; plan p. 32 | Missing full imputation predictor/covariance definitions do not independently establish incompatible analyses or estimates. | CONDITIONAL_OR_UNREPORTED |
| Plan p. 14; main p. 2 | Different randomization stratification detail is not shown to change a primary/key-secondary result or planned decision rule. | PERIPHERAL_COMPARISON |
| Main p. 3; plan p. 32 | Planned kidney-failure record confirmation versus report questionnaire ascertainment does not establish that confirmation was omitted. | CONDITIONAL_OR_UNREPORTED |
| Main p. 8 Figure 3 BMI≥30 | A missing closing parenthesis has an immediately evident intended reading. | NOTATION_OR_TYPOGRAPHY |

## Limitations and handoff

No scientific coverage gap remains in pass 1. Exact graphical subgroup adjusted estimates/CI endpoints are not numerically printed; every interval and point was inspected visually without inventing exact values. Exact simulation power, Cox test subtype/variance estimator, individual person-time, complete imputer definitions, unrounded outputs and correlation N/test cannot be reconstructed from the package. Missing blood/urine overlap prevents assigning a fabricated exact planned population size. Three findings require a fresh independent inclusion screen before any candidate ID is assigned. Every stable candidate and all screening/recheck facts must then be considered by a distinct fresh statistical pass-2 agent, which must revisit all 140 S records. Findings=3; excluded observations=30; relationships=140; pass=PASS_1_COMPLETE.

