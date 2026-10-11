# Statistical pass 1

Runtime agent ID: root/statistics_pass_1 (canonical runtime name /root/statistics_pass_1). Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN. This agent performs pass 1 only; pass 2 requires a different runtime agent.

Scope: complete main REPORT PDF pp.1–9, PLAN protocol PDF pp.1–15, REPORT results-supplement PDF pp.1–16; all applicable estimate/test/method/design relationships reconstructed from both complete maps and exact direct sources. Canonical statistical inventory:118 relationships. Findings:5. Excluded observations:8. The counts describe coverage and judgments, without a finding target.

**Explicit completed scope:** S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, S113, S114, S115, S116, S117, S118.

Each enumerated S record is PASS_1_COMPLETE in statistics/relationship_inventory.md. All primary and repeated Table2/eTable5 estimates, both group intervals, all effect intervals/P values, all19 MI rows, all25 eTable4 nominal/adjusted tests, all36 eTable6 beta/SE/P triples and all5 omnibus tests, both Holm families, sample size, models, missingness, superiority, analysis-population rules, planned/report matching and stopping were checked. No NI/equivalence margin, numerical interim boundary, or actual benefit/futility stopping decision is supplied. No scientific source-coverage gap remains.

## Source and diagnostic authority

Direct-source pdftotext (Poppler26.01.0) reconfirmed main pp.2–4/8, protocol pp.5–6, and results supplement p.14. Reused source-matched rendered results-supplement p.14 was visually inspected to confirm 1.92(1.50,2.24), column identity and all six analysis rows. Images are CPU derivatives; no new derivative or OCR was produced by this agent. Source-linked complete maps provide other printed values, without reading prior findings/reports.

All ratios/intervals have estimates inside ordered endpoints and consistent positive abstinence direction; all displayed endpoint contrasts with P<.001 exclude their nulls. All36 eTable6 coefficient/P pairs reconcile under half-unit beta/SE rounding with two-sided normal-Wald diagnostics. For example Penn beta−.017/SE.027 gives diagnostic centralP.528937, but full rounded-input range[.509012,.548506] contains printed.519; no conflict is inferred from the central approximation. The omnibus categorical tests cannot be reconstructed from individual coefficients without covariance/df; they are separate tests and no contradiction follows from their component significance pattern.

The25-test moderator Holm family excludes individual categorical contrasts. Lowest nominal.010 has adjusted.250; racial-minority.024 gives.552, perceived-addiction.026 gives.572, motivation.033 gives.693, and remaining adjusted values cap at1.000. eTable4 similarly has25 families; <.001 and .001/.002 entries are evaluated over their printed ranges, not treated as exact. All nominal/adjusted entries are compatible with that construction and the narrative significant predictor list.

The two-proportion sample-size approximation (diagnostic, not identified as the authors' engine) yields905.366 per arm at20%/15%,two-sidedalpha.05,power.80; stated900 is within the display-precision tolerance. Budget termination1503/1800=83.5% is disclosed. CTP paired/independent tests are not named, so diagnostic reconstructions do not establish an alternative authors' analysis.

## Findings

### F-ST1-001

**Title:** The 30-day IPRW odds-ratio upper interval does not reproduce the log-symmetric construction used by the other eTable5 odds-ratio rows.

**Locations and roles:** REPORT [results supplement PDFp.14,eTable5,30-dayppa IPRW odds-ratio cell](../../../joi240078supp2_prod_1739900423.24574.pdf#page=14), compared with REPORT same eTable5's other five odds-ratio cells; REPORT [PDFp.5,eAppendixC weighted logistic method](../../../joi240078supp2_prod_1739900423.24574.pdf#page=5). Relationship:S_W. Canonical relationship:S008, with S004,S005,S007,S041,S042 as same-display construction comparators.

**Printed values:** 30-day IPRW OR1.92(95%CI1.50–2.24),P<.001. Other OR cells:30-dayCCA1.98(1.55–2.52),30-dayMissing=Vaping1.57(1.26–1.95),repeatedCCA2.65(1.90–3.70),repeatedIPRW2.61(1.87–3.65),repeatedMissing=Vaping2.34(1.69–3.22).

**Rule and calculation:** A symmetric interval on the logistic coefficient/log-OR scale obeys U=OR²/L. This relation reproduces all five comparator cells after half-unit input/output rounding, including the other IPRW OR row. For1.92 and1.50, allowing OR[1.915,1.925] andL[1.495,1.505], the recomputed upper interval is[2.436694352,2.478678930]. PrintedU2.24 has interval[2.235,2.245]. Minimumgap.191694352; relative discrepancy.191694352/2.24=.085577836 (>0.05). Central diagnosticU2.4576. This calculation tests a method that reproduces other rows; it does not impose an unstated variance estimator or prescribe a replacement endpoint.

**Focus area:** B,C. **Proposed review domain:** statistical_results. **Qualifying route:** Route A, category 4.

**Affected result or extracted value:** The upper95%confidence limit for the weighted30-day abstinence odds ratio, which would be extracted as2.24.

**Why context does not resolve it:** RouteA category4 requires registration of a result not reproduced by the same-display construction. The source describes survey-weighted logistic regression but gives no distinct construction for this single interval.

**Alternatives and missing definitions:** An asymmetric interval procedure or a separately obtained endpoint could produce asymmetric limits; no such row-specific procedure is identified. The true weighted coefficient covariance/df and CI algorithm are unprinted. P<.001 is compatible with the positive OR and null-excluding interval, so this finding does not assert a significance reversal.

**Exact human question:** Which interval construction produced the30-dayIPRW odds-ratio interval1.50–2.24, and how does its upper limit relate to the construction used for the other odds-ratio rows?

### F-ST1-002

**Title:** The reported primary estimates cannot be assigned clearly to the protocol's baseline-adjusted analysis.

**Locations and roles:** PLAN [protocolPDFp.5,Data Analysis Plan/Primary Analysis](../../../joi240078supp1_prod_1739900423.22574.pdf#page=5); REPORT [articlePDFp.4,Statistical Methods](../../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=4), [articlePDFp.6,Table2](../../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=6), and [articlePDFp.1,abstract](../../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=1). Relationship:P_R; all relationships:P_R. Canonical:S003,S109.

**Printed statements/values:** Plan says all estimates will be adjusted for baseline confounders of the intervention-outcome relationship. Report specifies ordinary logistic regression in Rglm for primary analyses and prints primaryRR1.35(1.17–1.57),OR1.57(1.26–1.95), without naming primary baseline covariates, stating that none met a selection rule, or assigning the printed estimates to an adjusted versus treatment-only model.

**Rule and calculation:** A specified primary analysis requiring baseline adjustment needs an identifiable connection to the reported primary estimate. The stated adjustment step is absent from the report specification. Supporting arithmetic only: counts 287/759 and 208/744 give crude OR (287×536)/(472×208)=1.5669003, matching printed 1.57. This match is a diagnostic and does not establish that the actual model was unadjusted, nor is a model-versus-crude disagreement alleged. No numerical interval discrepancy is claimed; display precision is not applicable to the missing model attribution.

**Focus area:** C,D. **Proposed review domain:** protocol_report. **Qualifying route:** Route B.

**Affected result or extracted value:** The model/adjustment identity of the primary7-monthRR1.35 andOR1.57 for interpretation and synthesis.

**Why context does not resolve it:** B1 concerns planned primary-model specification; B2 neither main methods nor results supplement identifies the planned baseline adjustment for these estimates; B3 a reader cannot determine whether to extract these as adjusted or treatment-only primary estimates. The statement in the supplied plan is affirmative, rather than a general request for extra reporting.

**Alternatives and missing definitions:** The actual glm could include baseline covariates omitted from the report; no baseline variables may have met an unstated selection rule; or the planned analysis could have been updated. Protocol amendmentp.15 discloses assessment, capacity and fraud changes, without a primary-analysis-model amendment. Actual model formula, selected covariates/selection rule, and relation of Table2 estimates to that formula remain missing.

**Exact human question:** Which baseline covariates, if any, were included in the primary model producingRR1.35 andOR1.57, and how does that model correspond to the protocol's statement that all estimates are baseline adjusted?

### F-ST1-003

**Title:** The reported moderator testing family does not explain the planned outcome-association selection step.

**Locations and roles:** PLAN [protocolPDFp.5,Primary Analysis](../../../joi240078supp1_prod_1739900423.22574.pdf#page=5) and [p.6,opening continuation](../../../joi240078supp1_prod_1739900423.22574.pdf#page=6); REPORT [results supplementPDFp.6,eAppendixD](../../../joi240078supp2_prod_1739900423.24574.pdf#page=6), [p.15,eTable6](../../../joi240078supp2_prod_1739900423.24574.pdf#page=15), and [articlePDFp.5,Moderator Results](../../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=5). Relationship:P_R; all relationships:P_R. Canonical:S110,S014.

**Printed statements/values:** Plan describes selected potential moderators and states that for all moderators found associated with the primary outcome, treatment/moderator interactions will be examined after main effects. Report says all baseline characteristics inTable1 were examined one at a time; all25 variable-level interactions comprise the Holm family and none is significant after adjustment. ETable6 lowest nominalP.010 adjusts to.250.

**Rule and calculation:** The supplied plan contains an outcome-association selection step; the reported specification instead identifies an all-characteristic interaction family without reporting such a screening step, screening results, or their connection to the25-test correction family. This is an analysis-specification comparison, not a claim that Holm was computed inconsistently. The25-test Holm family itself reproduces. Numerical display precision is not applicable to the analysis-step discrepancy.

**Focus area:** C,D. **Proposed review domain:** protocol_report. **Qualifying route:** Route B.

**Affected result or extracted value:** The no-adjusted-significant-moderator conclusion and whether its25-test family corresponds to the planned selection procedure.

**Why context does not resolve it:** B1 concerns a planned interaction-analysis step; B2 the report does not say whether the outcome-association step was used, bypassed, or yielded all listed variables; B3 the test-family definition determines the interpretation of the adjusted moderation results.

**Alternatives and missing definitions:** All listed variables could have met the planned association criterion; the wording may permit additional exploratory moderators rather than a restrictive filter; or a fuller analysis-family specification may have superseded the supplied plan. These source-grounded interpretations require the criterion/results or updated specification to identify which applies.

**Exact human question:** Was the protocol's outcome-association selection step used for the reported moderator analyses, and what rule produced the25-variable Holm family?

### F-ST1-004

**Title:** Retention P values are reported beside all three randomized groups although waitlist is said to be excluded from significance tests.

**Locations and roles:** REPORT [articlePDFp.2,Participants](../../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=2); REPORT [articlePDFp.4,Results retention paragraph](../../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=4), corroborated by REPORT [p.6,flow figure](../../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=6). Relationship:S_W; all relationships:S_W. Canonical:S009,S010.

**Printed statements/values:** Waitlist group not included in sample-size calculations or tests of statistical significance. Retention paragraph presentsI609/759,C636/744,W152/178 at1month withP=.02 andI521/759,C543/744,W132/178 at7months withP=.11.

**Rule and calculation:** A test result must be attributable to its stated analysis population. These paragraphs present three-group comparisons while the exclusion statement says waitlist is not in significance tests. Diagnostic only: Pearson2×3 tests from the printed counts givechi-square8.108584,P=.0173478 (rounding.02), andchi-square4.327096,P=.1149167 (rounding.11). The method is not named, so diagnostics do not establish the actual test or choose a replacementP. Display precision does not resolve the population-description conflict; the diagnostics themselves are consistent with the printed P values.

**Focus area:** C. **Proposed review domain:** statistical_results. **Qualifying route:** Route B.

**Affected result or extracted value:** The1-month retentionP=.02 and7-month retentionP=.11, including which groups they compare.

**Why context does not resolve it:** B1 concerns statistical-test analysis population; B2 the all-three-group retention paragraph does not identify a narrower test contrast or exception to the waitlist exclusion; B3 a reader cannot assign the retained P values to anI:C comparison versus a three-arm omnibus comparison.

**Alternatives and missing definitions:** The exclusion statement may refer only to cessation-effect tests, with retention checks exempt; P values may reflect a different contrast or test. Exact test name and group contrast are missing.

**Exact human question:** Which groups and statistical tests generated the1- and7-month retention P values, and does the waitlist significance-test exclusion apply only to cessation outcomes?

### F-ST1-005

**Title:** The main report's pre-quit intervention duration differs from the supplied plan and report supplement.

**Locations and roles:** PLAN [protocolPDFp.2,intervention description](../../../joi240078supp1_prod_1739900423.22574.pdf#page=2); REPORT [articlePDFp.3,Vaping Cessation Intervention](../../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=3); REPORT [results supplementPDFp.2,eAppendixA](../../../joi240078supp2_prod_1739900423.24574.pdf#page=2). Relationship:P_R; all relationships:P_R,S_C. Canonical:S114.

**Printed values:** Protocol:messages for a week before and8weeks after a set quit date. Report supplement:1week preceding and8weeks afterward. Main report:6weeks before and8weeks after.

**Rule and calculation:** These descriptions apply to the same quit-date branch of the randomized intervention but specify different durations. Treating weeks as whole-unit displays gives6±.5 versus1±.5; minimumgap4weeks/reference1week=4 (>0.05). The total set-date message window is14weeks under the main description and9weeks under plan/supplement. No duration amendment is supplied on protocolp.15.

**Focus area:** D. **Proposed review domain:** protocol_report. **Qualifying route:** Route B.

**Affected result or extracted value:** The duration/exposure definition of the randomized program associated with primary7-monthRR1.35.

**Why context does not resolve it:** B1 intervention duration is expressly in cross-document scope; B2 both descriptions use the same set-quit-date branch and neither identifies an alternate phase; B3 intervention duration is a meaningful trial characteristic for result interpretation and intervention extraction. This is a printed duration difference, rather than a program-name difference.

**Alternatives and missing definitions:** A later program version could have expanded pre-quit exposure; main6weeks could refer to a different operational window, but none is identified. The actual delivered set-quit-date pre-period and any corresponding amendment remain unspecified.

**Exact human question:** Did participants who set a quit date receive1week or6weeks of pre-quit messages, and what source identifies the delivered duration and any change from the supplied protocol?

## Excluded observations

Only apparent issues self-screened out appear here. Reconciled routine checks remain in the S records.

| Location | Observation | Reason code |
|---|---|---|
| REPORT results supplementPDFpp.4/11,OR.miss−∞ | Odds-ratio endpoint is written−∞ although the limiting odds multiplier for all missing abstinent is0; immediate log-scale/limit context identifies intended all-abstinent endpoint, with no finite result ambiguity. | NOTATION_OR_TYPOGRAPHY |
| REPORT results supplementPDFp.11,FMI column | FMI is called a fraction while integer values2–23 omit apercent marker; scale context identifies2%–23%, with no change to effect estimates. | NOTATION_OR_TYPOGRAPHY |
| REPORT results supplement PDF p.11,+∞ versus REPORT article PDF pp.5/6 and supplement p.14 | MI limiting rates 37.98/28.06 versus count-based 37.8/28.0; printed interval gaps .125/.005 give relative discrepancies .00331/.000179, within .05. | ROUNDING_OR_DISPLAY_PRECISION |
| PLANprotocolPDFpp.3/6 versus REPORTarticlePDFp.8 | Planned mediator secondary aim is not analyzed in current article and explicitly declared outside manuscript scope; not designated primary or key-secondary endpoint, and no changed outcome status or prespecified report claim identified. | CONDITIONAL_OR_UNREPORTED |
| PLANprotocolPDFpp.5/6 versus REPORTarticlePDFpp.3/4 | Other quitting secondary measures7-dayppa/continuous/attempts/reduction/confidence are absent; report's repeated30-dayppa is not explicitly claimed prespecified and is not equated to continuous abstinence. Absence alone does not establish a changed primary/key-secondary outcome or status. | CONDITIONAL_OR_UNREPORTED |
| PLANprotocolPDFp.10 versus REPORTarticlePDFp.3 | FinalDSMB interim/monitoring rules not supplied; report budget stop does not assert crossing a statistical boundary. | CONDITIONAL_OR_UNREPORTED |
| REPORTarticlePDFpp.5–7,CTP longitudinal contrast | Exact paired CI/test engine not named; paired diagnostic from printed335discordances gives approximate13.66–20.40pp versus printed13.5–20.5pp, within precision and insufficient to identify actual engine. | CONDITIONAL_OR_UNREPORTED |
| PLANprotocolPDFp.6 versus REPORTsupplementPDFpp.4/11 | MI range expands1–5 to1/100–100 plus limits while retaining the planned1–5 values; expansion strengthens range exploration without replacing the stated primary missing=vaping analysis. | CONTEXT_RESOLVES |

## Limitations

No scientific source-unit coverage gap. Direct source inspection and source-linked maps cover all40PDFpages. Source does not supply individual data, IPRW weights, primary baseline covariate formula/selection, CI engines for all displays, response-comparison test names, omnibus covariance/df, or finalDSMB monitoring rules. Diagnostics are named and not presented as the authors' methods; such absent detail alone yields no finding. The log-symmetric OR observation relies on reproduction of other cells and records asymmetric-construction as a human-review alternative. Reused text/images and supplied sources were preserved unchanged.

