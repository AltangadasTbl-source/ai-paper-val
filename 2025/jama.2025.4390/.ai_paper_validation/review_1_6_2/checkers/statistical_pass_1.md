# Statistical pass 1

Runtime ID: 01a12bc3-34f6-7a90-9ccf-69efae0c63b2. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN. Exact assigned scope: all 110 mapped relationships S001–S050, S100–S128, S200–S211, and S300–S318, including every constituent row of grouped relationships. This is the first statistical pass; pass 2 remains PENDING for a distinct fresh agent.

QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read completely. Inputs were the current main and complete support maps, the current 110-record inventory, current source PDFs and source-matched SAP renders. No historical scientific conclusions, candidate selections, or reports were used. No web evidence or preferred analysis was introduced. Observations below are independently self-screened findings awaiting the inclusion screener and human adjudication.

## Evidence authority and tooling

Current main source renders pp.3,4,7,8,9 and current results supplement renders pp.20,33,39,49 were visually read to confirm every cited printed statement and column placement. SAP p.3,4,6 source-matched renders and current protocol p.4 were visually read for compared specifications. The source-matched SAP images were assessed by the curator against the current direct-source identity. Additional current source confirmation renders are in preprocessing/stats1_confirmation/: main-3.png; protocol-4.png; supplement-20.png; supplement-33.png; supplement-39.png. Engine: package-local PyMuPDF 1.26.4 through the supplied pdf_tools.py render helper, 200 dpi, CPU. GPU OCR was authorized by the user, but no new OCR was necessary for these readable pages. Existing derivatives are locators; the visible supplied page is the authority. Highlighting visible in supplied files was not introduced by this checker and did not define discovery scope.

## Checks completed over the whole inventory

Every Table 2 outcome was checked separately, including both S030 endpoints: all printed HR/RR estimates are within ordered 95% intervals, and every displayed P value agrees with null inclusion at the stated two-sided .05 threshold. S026 has an upper bound printed 1.00 with P=.06; a displayed limit equal to the null is not an interval excluding it. No null-versus-P finding was reproduced. Effect direction agrees with the narrative, references and forest plots. Adjusted effects were not equated with crude risks or rates. No standard errors or test statistics are supplied for these Cox/Poisson results; log-normal/Wald calculations were diagnostics only, without assuming the covariance, variance estimator or test convention.

All 38 within-subgroup HR intervals in Figure 3 were separately checked for containment, order, direction and null inclusion. All 19 interaction P values were separately read. Interaction tests concern heterogeneity, whereas within-subgroup intervals concern treatment effects; these were never treated as the same null hypothesis. The caption specifies a primary-covariate Cox model with characteristic and treatment interaction. No covariance or relationship between the separate subgroup-fit estimates and the interaction-model coefficients is supplied. A difference-of-log-HR diagnostic does not reproduce the complete interaction column and therefore cannot replace its model. The prespecification and rate-display observations are recorded below.

All constituent inferential rows of S300–S307 were checked, not just representatives. Medians/IQRs alone do not reproduce continuous-variable tests. Categorical counts were checked with the same-display Pearson diagnostic, with degrees of freedom equal to nonempty categories minus one. This supports a reproducing-method comparison rather than an inference from customary practice. eTable4 reproducing categorical examples: age X²=30.217601, df4, P=.00000442; education 44.806702, df4, P<.001; ethnicity 18.854835, df7, P=.00865445; province 24.020802, df4, P<.001; health categories 26.035446, df5, P<.001; cognitive categories 23.724975, df3, P<.001; deprivation 5.952783, df5, P=.310840; BP-drug categories 5.395208, df3, P=.145042; non-BP categories 5.913123, df4, P=.205731; daily prescriptions 11.208242, df5, P=.047404; nonprescriptions 6.134502, df4, P=.189326; vitamins 12.693601, df4, P=.012874. The displayed copies reconcile under half-unit P intervals or the ≤.05 relative-gap rule, except chronotype below. Every binary count row was also evaluated, including rare dialysis, dementia with available-data denominators, medication classes, polypharmacy and resistant hypertension. No other over-tolerance same-display discrepancy was reproduced.

eTable5 reproducing categorical examples: age X²=2.832925, df4, P=.586163; chronotype 7.041402, df2, P=.029579; education 7.204558, df4, P=.125465; province .623897, df4, P=.960372; health categories 6.261731, df5, P=.281578; cognitive categories 2.631873, df2 after removing an empty category, P=.268223; deprivation 4.209400, df5, P=.519678; BP drugs 3.527480, df3, P=.317215; non-BP drugs 4.658519, df4, P=.324163; total prescriptions 1.392624, df5, P=.925118; nonprescriptions 2.354755, df2, P=.308086; vitamins 5.473681, df4, P=.242053. All binary rows were evaluated separately. The duplicated Other ethnicity counts make that displayed distribution unsuitable for reconstructing its ethnicity test; the printed-count issue is retained in the numeric lane rather than silently replacing cells. Diuretic versus combination P values are recorded below.

All 11 ABPM rows S308–S318 were checked. Each of five continuous estimates is contained in an ordered interval; zero exclusion agrees with P=.15,.72,<.001,.02,<.001 respectively, and direction agrees with bedtime-minus-morning means. SD-based independent-group standard-error diagnostics are approximately 1.6526,1.0894,1.9140,1.1422,.9610; these diagnose consistency without asserting an unstated test. All six binary rows reproduce the Pearson diagnostic within display precision: nondipping P=.00536569, appropriate dipping .162308, extreme dipping .0459775, awake BP control .120767, systolic control .125793, diastolic control .255975. P=.05 for extreme dipping is a rounded boundary, and no interval or significance claim contradicts it. Per-person dipping need not equal the dip of aggregate means.

Sample-size inputs were tested separately: a two-sided equal-allocation proportional-hazards event diagnostic gives 4(1.959964+.841621)²/log(.75)²=379.3517 events, reconciling with 379 under printed inputs/display precision; 379×1.07=405.53 reconciles with 406. No equation is supplied, so this is a diagnostic, not identification of the original engine. Recruitment-letter 6400 packages is a separate administrative randomization, and its 8% baseline/2-percentage-point detectable difference/80% power/.05 inputs give approximately 6400 under a two-group proportion diagnostic; it is not the main event requirement. The protocol's 37% effect/200-event interim statement is also consistent with a diagnostic expected standardized effect of about 3.27 versus the .001 two-sided boundary about 3.29, giving approximately 50% power. No noninferiority or equivalence margin is stated. The primary superiority result is nonsignificant as reported. Benefit ≤.001 and harm ≤.05 stopping thresholds are stated; no individual interim estimates/tests are supplied, so actual threshold crossing cannot be reconstructed. The funding stop and event-target change are disclosed; no preferred stopping rule is inferred.

All plan-method, outcome, missingness, ascertainment and censoring relationships were compared with the matched main/supplement context. Outcome-source flags were distinguished from adjudicated endpoints; events and components were not assumed mutually exclusive. Province-specific dementia sensitivity is disclosed and is not a candidate merely because provinces differ. The final supplied SAP supersedes original model and ABPM-size specifications where an evolution is documented. Specific remaining reproduced observations follow.

## Findings

### F-ST1-001 — eTable4 chronotype test does not reproduce under the method supported by its other rows

- **Relationships:** S300. **Locations / roles:** REPORT [results supplement p.33, eTable4 chronotype and other categorical rows](../../../joi250019supp3_prod_1749674951.30054.pdf#page=33); REPORT [p.34, deprivation and categorical outcomes](../../../joi250019supp3_prod_1749674951.30054.pdf#page=34); REPORT [p.35, medication-number categories](../../../joi250019supp3_prod_1749674951.30054.pdf#page=35).
- **Printed values:** Completed/death n=2726: early bird1388, night owl818, neither520; withdrew/lost n=631:352,154,125. Printed P=.09. All three category totals reconcile with the stated column denominators.
- **Rule and calculation:** Pearson X²=Σ(O−E)²/E with E from observed margins gives X²=8.038700681, df=2, P=exp(−X²/2)=.017964632. This same-display method reproduces age, education, province, deprivation, medication-count and other categorical tests as documented above. With each displayed integer cell conservatively varied by ±.5, the corner envelope is P=.0152689–.0210417; count discreteness restricts admissible counts further. The printed P half-unit interval is [.085,.095]. Its gap from the conservative recomputed envelope is at least .0639583; relative discrepancy .0639583/.09=.71065>.05. The numerical method comparison is a diagnostic reproducing-method test, not an assertion of the original test engine.
- **Focus area:** B/C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W; **All relationships:** S_W.
- **Qualifying route:** Route A, category 4.
- **Affected result or extracted value:** Chronotype association with withdrawal/loss and the P value extracted from eTable4; the printed .09 and reproducing .018 have different .05 readings.
- **Why context does not resolve it:** Route A category4 applies to a printed result not reproduced by a method that reproduces other rows of the same display. The source provides neither an alternative chronotype test nor an adjusted model producing .09.
- **Alternatives / missing definition:** A different chronotype-only test, adjusted model, differently coded categories or analysis subset could produce a different P, but none is defined in the supplied display. This possibility remains a human question.
- **Exact human question:** Which test, category coding and analysis population produced chronotype P=.09, given that the printed 2×3 counts give P≈.018 under the method supported by other categorical rows?

### F-ST1-002 — Identical eTable5 medication-count comparisons carry nonreconciling P values

- **Relationships:** S306. **Locations / roles:** REPORT [results supplement p.39, eTable5 diuretic and combination BP medication](../../../joi250019supp3_prod_1749674951.30054.pdf#page=39), with n44/n57 in REPORT [eTable5 p.37](../../../joi250019supp3_prod_1749674951.30054.pdf#page=37).
- **Printed values:** Both rows are morning9(20.5%)/44 and bedtime16(28.1%)/57; diuretic P=.34 and combination P=.38.
- **Rule and calculation:** Identical 2×2 tables are [[9,35],[16,41]]. The same-display Pearson method gives X²=.773226937, df1, P=.379220624, reproducing the combination .38 and the other binary rows. Two printed copies for the same count-based comparison have P half-unit intervals [.335,.345] and [.375,.385]; gap .030, relative to reference .38 is .078947>.05 (relative to .34 is .088235). Counts are individually discrete participants; the only admissible integer in every count's half-unit interval is its printed count. If a different method or unprinted subset was used, that is an alternative, not a disclosed resolution.
- **Focus area:** B/C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W; **All relationships:** S_W.
- **Qualifying route:** Route A, category 4.
- **Affected result or extracted value:** The diuretic-comparison P value in the follow-up-unavailable sensitivity display.
- **Why context does not resolve it:** Route A category4 applies; both categorical rows and denominators are visibly identical, but a row-specific test/model is not identified.
- **Alternatives / missing definition:** Row-specific tests, covariate adjustment or underlying subsets might distinguish the analyses, but the display and supplied methods give no such mapping. No choice of preferred test is proposed.
- **Exact human question:** Why do identical diuretic and combination-medication 2×2 comparisons have P=.34 and P=.38, and which analysis produced the diuretic value?

### F-ST1-003 — Main and supplementary missing-value methods differ for adjusted analyses

- **Relationships:** S006,S209. **Locations / roles:** REPORT [main p.4, Statistical Analysis](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=4); REPORT [results supplement p.20, missing data](../../../joi250019supp3_prod_1749674951.30054.pdf#page=20).
- **Printed statements:** Main: other analyses include individuals with available data and “We did not impute missing values.” Supplement: categorical covariates replaced by modal observations and continuous covariates by means; no outcome data imputed.
- **Rule and comparison:** Modal/mean replacement of an unavailable covariate is an imputation/replacement step in the adjusted-analysis input. A blanket statement of no missing-value imputation and an explicit covariate replacement step describe different handling unless the main statement is restricted to outcomes. This is a logical comparison; display precision is not applicable.
- **Focus area:** C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_C; **All relationships:** S_C.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Input population and missing-covariate handling for adjusted primary HR.96(.77–1.19) and secondary models.
- **Why context does not resolve it:** The main statement does not specify an outcome-only restriction, and its available-data statement could imply exclusion whereas the supplement specifies replacement. Which adjusted-analysis inputs were used remains relevant to extracting the method and analysis population.
- **Alternatives / missing definition:** Main no-imputation may be shorthand for outcomes, in which case the supplement provides the intended distinction; the number of replaced covariates and participants is not stated. The observation does not claim a numerical HR change.
- **Exact human question:** Does the main no-imputation statement apply only to outcomes, and were missing baseline covariates replaced by modes/means in the reported adjusted analyses?

### F-ST1-004 — Six medication subgroups are called prespecified without a supplied plan counterpart

- **Relationships:** S044,S045,S046,S047,S048,S049,S128. **Locations / roles:** REPORT [main p.9, Figure3 six medication-use axes and caption](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9); PLAN [SAP p.6, Subgroup Analyses](../../../joi250019supp2_prod_1749674951.30054.pdf#page=6). The complete protocol/amendment map was checked for a corresponding treatment-effect subgroup specification.
- **Printed statements/values:** Figure3 caption calls the subgroup analyses prespecified; ACE inhibitor, ARB, beta-blocker, CCB, diuretic and combination-pill axes carry interaction P=.05,.44,.54,.66,.43,.72 respectively and all 12 subgroup estimates. SAP lists exactly13 axes: age, sex, frailty, polypharmacy, health, resistant hypertension, HF, diabetes, CAD, stroke/TIA, sleep apnea, CKD and sedentary status. Medication-class timing adherence and external-validity comparisons in the protocol are different analyses.
- **Rule and comparison:** Each of six medication-use treatment-effect subgroup axes lacks a counterpart in the supplied primary-outcome subgroup list. The repeated prespecification pattern is one finding, not six. No arithmetic/display-precision issue applies.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R; **All relationships:** P_R.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** Prespecification status of all six medication-class subgroup treatment effects and their interaction P values, including ACE interaction P=.05.
- **Why context does not resolve it:** Route A category5 applies to analyses called prespecified without a supplied plan counterpart; the adherence/external-validity descriptions do not specify these composite-endpoint treatment interactions.
- **Alternatives / missing definition:** An unavailable later amendment or detailed publication could contain them; such material is not supplied and cannot be assumed. The medication comparisons may be exploratory despite the shared caption.
- **Exact human question:** Which supplied prospective specification supports calling the six medication-use primary-outcome subgroup analyses prespecified, or which axes does that caption intend to identify as prespecified?

### F-ST1-005 — Planned within-arm withdrawal sensitivity comparison is replaced by different displayed contrasts

- **Relationships:** S128,S300,S301,S302,S303,S304,S305,S306,S307. **Locations / roles:** PLAN [SAP p.6, Sensitivity Analyses](../../../joi250019supp2_prod_1749674951.30054.pdf#page=6); REPORT [results supplement eTable4 p.33](../../../joi250019supp3_prod_1749674951.30054.pdf#page=33), [p.34](../../../joi250019supp3_prod_1749674951.30054.pdf#page=34), [p.35](../../../joi250019supp3_prod_1749674951.30054.pdf#page=35), [p.36](../../../joi250019supp3_prod_1749674951.30054.pdf#page=36); REPORT [eTable5 p.37](../../../joi250019supp3_prod_1749674951.30054.pdf#page=37), [p.38](../../../joi250019supp3_prod_1749674951.30054.pdf#page=38), [p.39](../../../joi250019supp3_prod_1749674951.30054.pdf#page=39), [p.40](../../../joi250019supp3_prod_1749674951.30054.pdf#page=40).
- **Printed statements/values:** SAP: according to treatment group, present baseline characteristics of those censored because of withdrawal/loss and compare with those not censored this way using Fisher exact. eTable4 compares pooled completed/death2726 with all interview withdrawals/losses631. eTable5 compares morning44 with bedtime57 among those unavailable for both interviews and administrative follow-up. These are different populations/contrasts; 631 includes530 retained in administrative tracking, and only101 are unavailable for all follow-up.
- **Rule and comparison:** Neither displayed comparison is the treatment-arm-specific censored-versus-not-censored comparison specified for the primary survival analysis. Complete supplied report mapping finds no separate table with that contrast. Pearson diagnostics reproduce displayed categorical rows but do not identify the plan's Fisher comparison. This finding concerns the contrast and analysis-population mapping, not a preference for Fisher over another method. No numerical rounding can equate the four required within-arm comparison cells to the displayed two contrasts.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R; **All relationships:** P_R.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** Prespecified sensitivity analysis addressing withdrawal-related composition of the primary survival-analysis population.
- **Why context does not resolve it:** Route A category5 applies to the planned primary-analysis sensitivity comparison not displayed; neither pooled interview retention nor cross-arm comparison confined to the unavailable subset supplies the planned within-arm comparator.
- **Alternatives / missing definition:** The phrase “according to treatment group” could have been intended less specifically, or a separate analysis may exist outside the supplied package. The report's alternative displays can be useful while still being different contrasts. No preferred analysis or clinical criticism is proposed.
- **Exact human question:** Where is the SAP's arm-specific censored-versus-not-censored baseline comparison, or how were eTables4/5 intended to implement that specified contrast and population?

### F-ST1-006 — Withdrawal censoring dates differ between the supplied SAP and report

- **Relationships:** S006,S126. **Locations / roles:** PLAN [SAP p.3, Withdrawal](../../../joi250019supp2_prod_1749674951.30054.pdf#page=3); REPORT [main p.4, censoring method](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=4), including Figure1 withdrawal rows.
- **Printed statements/values:** SAP: withdrawal retaining administrative consent follows claims; participants not agreeing to continuing claims are censored on withdrawal date. Main: participants lost to follow-up are censored on last telephone/email contact, and administratively trackable active-follow-up dropouts on latest healthcare contact. Figure1 shows withdrawal53 bedtime/42 morning without electronic follow-up and loss4/2 without electronic follow-up.
- **Rule and comparison:** The report states a last-successful-contact rule for follow-up loss but supplies no withdrawal-date exception for the95 withdrawals without electronic follow-up, whereas the SAP explicitly prespecifies that exception. Withdrawal date and last successful contact need not coincide. A primary time-to-event censoring specification cannot be matched for those participants from the supplied descriptions alone. No display-precision calculation applies.
- **Focus area:** D/C. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R; **All relationships:** P_R.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Censoring rule and person-time in the primary adjusted survival result for withdrawals without administrative follow-up.
- **Why context does not resolve it:** The main method discusses follow-up loss and dropout without identifying whether the plan's withdrawal-date exception was applied. Two source-defined dates are possible for a specific primary-analysis subgroup.
- **Alternatives / missing definition:** Withdrawal may have occurred at the last successful contact, or “lost to follow-up” may be used narrowly and the planned withdrawal rule applied without repeating it. The source does not supply the dates, so no numerical HR change is claimed.
- **Exact human question:** For the95 participants withdrawing without administrative follow-up, was censoring at withdrawal date as specified in the SAP or at last successful telephone/email contact, and do those dates coincide?

### F-ST1-007 — Reported blocked/province-stratified allocation differs from the supplied protocol specification

- **Relationships:** S107,S006,S009. **Locations / roles:** PLAN [original protocol p.4, Allocation](../../../joi250019supp1_prod_1749674951.29554.pdf#page=4); REPORT [main p.3, Intervention](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=3); REPORT [main p.7, primary covariates](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=7). All supplied amendment units were reviewed for the corresponding change.
- **Printed statements:** Protocol simple randomization with no stratification or blocking; main permuted blocks of random sizes10/12 stratified by province. Province also enters the stated adjusted primary model.
- **Rule and comparison:** Simple unblocked/unstratified allocation and permuted blocked/province-stratified allocation are different statistical-design specifications. No supplied amendment identifies that change. This is the design-to-analysis specification comparison, not a broad preference for an allocation scheme. No rounding rule applies.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R; **All relationships:** P_R.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Recorded randomized-design specification and province adjustment context of the primary treatment estimate.
- **Why context does not resolve it:** The original protocol is explicitly versioned, making a later amendment plausible, but none of the supplied amendment statements specifies this changed allocation procedure. A data extractor cannot map the final procedure to a supplied prospective design record.
- **Alternatives / missing definition:** A later operational change or unavailable published protocol may explain the report. The reported procedure and province-adjusted Cox model can be internally coherent; no critique of that stated choice is made.
- **Exact human question:** Which supplied amendment establishes blocked, province-stratified randomization, and how does it relate to the supplied original no-block/no-stratification specification?

### F-ST1-008 — Primary Figure3 event-rate column does not reconcile with the matched primary rate

- **Relationships:** S016 and S031–S049; numeric cross-reference N016. **Locations / roles:** REPORT [main p.9, Figure3 all-patients and all subgroup rate columns](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9); REPORT [main p.8, Table2 primary row](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=8); REPORT [main p.1, abstract primary rates](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=1).
- **Printed values:** Same primary events163/173 and adjusted HR.96(.77–1.19). Figure3 labels both rate columns “Rate per100 patient-years” and prints71.0 for each all-patients row. Table2 prints2.30/2.44; abstract2.3/2.4. Figure3 subgroup entries partition approximately71.0 in each arm rather than displaying the arm/subgroup event-rate pattern: male/female30.5+40.5 and30.4+40.6; age14.9+56.1 and14.5+56.5; frailty12.4+58.6 and12.7+58.3; polypharmacy23.0+48.0 and22.4+48.6; health28.5+42.5 and25.1+45.9; resistant HTN7.7+63.3 and7.0+64.0; HF1.1+69.8 and1.1+69.9; diabetes12.5+58.5 and12.5+58.5; CAD7.0+63.9 and7.3+63.7; stroke/TIA4.6+66.4 and4.8+66.2; apnea16.0+55.0 and14.4+56.6; CKD4.8+66.2 and4.8+66.2; sedentary17.7+53.2 and18.3+52.7; ACE24.4+46.6 and25.8+45.2; ARB22.8+48.2 and19.7+51.3; beta11.6+59.4 and10.9+60.1; CCB19.2+51.7 and19.8+51.2; diuretic18.6+52.4 and19.6+51.4; combination14.1+56.9 and13.4+57.6. This repeated column pattern is one observation.
- **Rule and calculation:** Matched same-unit primary rate copies: Figure interval[70.95,71.05]; Table2 bedtime[2.295,2.305] and morning[2.435,2.445]. Gaps68.645 and68.505; relative to reference2.30/2.44 are29.8457 and28.0758, both>.05. The count163 and rate2.30 imply about7086.96 patient-years, while interpreting71.0 literally implies229.58; count173 with2.44 implies7090.16 versus243.66. Person-time calculations are diagnostics because total person-time is not printed. They illustrate the quantity changed by the column, not an inferred replacement value.
- **Focus area:** A/B/C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W; **All relationships:** S_W.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Primary and all subgroup rate-per100-patient-years values extracted from Figure3.
- **Why context does not resolve it:** The comparison matches outcome, randomized arms, events and primary HR, yet the labeled rate differs far beyond display precision. The actual quantity encoded by the full Figure3 rate column is not specified.
- **Alternatives / missing definition:** The columns may represent scaled person-time or another quantity while carrying a rate label. Their near-additive partitions suggest a common total, but the source supplies no scale or person-time definition supporting a relabeling. No final correction is proposed.
- **Exact human question:** What quantity and scaling do the71.0 totals and subgroup rate-column values represent, and how should they be matched to the primary rates2.30/2.44 per100 patient-years?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| Main p.9 Figure3, all19 interaction axes | Diagnostic differences between independent subgroup log-HR ratios and printed interaction P values require unsupported covariance/model equivalence; the diagnostic does not reproduce the entire column. The caption defines a separate adjusted interaction model. | CONDITIONAL_OR_UNREPORTED |
| Main p.7 EQ-5D and SAP p.5–6 exploratory model | The crude rounded-mean difference−.6 differs from reported−.75, but the SAP specifies a multiple-linear-regression estimate; no unadjusted label is supplied. | MODEL_VERSUS_CRUDE |
| Results supplement p.49 sleep-time DBP and main p.7 | Rounded means62.9 and65.5 subtract to−2.6 whereas reported difference is−2.7. Input half-unit subtraction range[−2.70,−2.50] overlaps printed[−2.75,−2.65]; gap0. | ROUNDING_OR_DISPLAY_PRECISION |
| Main p.3 and protocol p.3 | 7% event-target inflation is not equal to projected5% attrition, but these are stated as distinct inputs and 379×1.07 reproduces406; the text does not claim a5% mechanical uplift. | CONTEXT_RESOLVES |
| Main p.3/6 interim versus original protocol p.4 | Original200-event interim and later155-event review follow a disclosed primary target reduction406→255; exact interim date/event counts can lag a target. No unprinted threshold crossing is inferred. | CONTEXT_RESOLVES |
| Main p.7 primary covariates versus original protocol p.4 | Original binary age/frailty/cognition model differs from the final reported model, but the later supplied SAP specifies the matching final ordered model. Comparing the original version alone would omit the source's prospective version context. | CONTEXT_RESOLVES |
| Main p.7/results supplement p.18 and protocol p.4/10 | Original100-per-arm ABPM sample differs from151/arm, but the supplied February2018 amendment explicitly specifies151/arm. | CONTEXT_RESOLVES |
| Main p.7/10 primary confidence-bound wording | Discussion excludedHR≤.76 versus adjusted lower bound.77 is also consistent with the expressly reported unadjusted lower bound.76; their half-unit copies touch and the relative difference is within tolerance. | ROUNDING_OR_DISPLAY_PRECISION |
| Results supplement p.6/8 dementia ascertainment | Manitoba medication-dispensation ascertainment differs from other provinces, but this is explicitly described and does not conflict with a stated common operational ascertainment rule. | CONTEXT_RESOLVES |
| Main Table2 HR/RR versus crude count/rate ratios | Adjusted Cox/Poisson estimates, including dementia and syncope, need not equal crude arm count or rate ratios. The supplied SAP provides covariate adjustment rather than a crude-effect label. | MODEL_VERSUS_CRUDE |

Exactly10 excluded observations. Reconciled containment, endpoint ordering, matching results and P checks are recorded as checks, not inflated into excluded-observation entries. Eight findings emitted; none receives a C ID here. All findings remain Pending Human Adjudication if independently included.

## Limitations and handoff

No assigned relationship or constituent inferential row was omitted. No new S ID was necessary. Missing source definitions limit exact mechanical reconstruction of Cox/Poisson tests, interaction covariance, continuous median tests, individual interim decisions and the ABPM test engine; those absences alone are not findings. Source-matched SAP render engine/version is historically unrecorded. Complete model selection and display checks are documented above; every canonical S row now explicitly records PASS_1_COMPLETE, with pass2 PENDING. Independent inclusion screening is required for all eight findings.

## Pass-1 relationship-by-relationship outcomes

Every S record remains stable. Checks here are source-grounded; absence of printed inputs is named without adopting a convention. No new S relationship was uncovered. Finding IDs do not imply independent screening inclusion or human adjudication.

| S ID | Pass 1 check and result | Pass 1 | Pass 2 |
|---|---|---|---|
| S001 | Primary CI ordered/contains estimate/includes1 with P.70; direction and all matched copies reconcile. | PASS_1_COMPLETE | PENDING |
| S002 | Key Points match primary HR/rates; no independent test supplied. | PASS_1_COMPLETE | PENDING |
| S003 | All endpoint/time/status definitions compared with current SAP and disclosed amendments; supplementary grouping does not redefine test measures. | PASS_1_COMPLETE | PENDING |
| S004 | Event diagnostic379.3517 and379×1.07=405.53 reproduce379/406; no calculation engine asserted. | PASS_1_COMPLETE | PENDING |
| S005 | Actual interim155 and funding stop distinguished from original200/406 and disclosed255 target; no interim statistics available to test crossing. | PASS_1_COMPLETE | PENDING |
| S006 | ITT/available-data/model/two-sided.05/censoring compared; F-ST1-003 imputation and F-ST1-006 withdrawal censoring; final allocation context F-ST1-007. | PASS_1_COMPLETE | PENDING |
| S007 | Adjusted/unadjusted primary CI containment/order/direction and narrative P.70 reconcile. | PASS_1_COMPLETE | PENDING |
| S008 | Both sensitivity HR CIs contain estimate and1, adjusted P.50 nonsignificant; exclusions clearly post hoc, not a prespecification finding. | PASS_1_COMPLETE | PENDING |
| S009 | All primary covariates match later SAP, not merely original protocol; province links F-ST1-007; figure CI/direction/risk counts reconcile. | PASS_1_COMPLETE | PENDING |
| S010 | Daytime systolic mean/P matched to S308; full supplementary CI includes0. | PASS_1_COMPLETE | PENDING |
| S011 | Daytime diastolic mean/P matched to S309; full supplementary CI includes0. | PASS_1_COMPLETE | PENDING |
| S012 | Overnight systolic difference/CI excludes0 and P<.001; means/direction match S310. | PASS_1_COMPLETE | PENDING |
| S013 | Overnight diastolic CI excludes0 with P.02; mean-difference half-unit intervals overlap; match S311. | PASS_1_COMPLETE | PENDING |
| S014 | Daytime BP control percentages/P match S316; denominator151/arm and Pearson diagnostic reconcile. | PASS_1_COMPLETE | PENDING |
| S015 | EQ-5D difference CI ordered/contains−.75/includes0 with P.12; crude means not substituted for planned linear model. | PASS_1_COMPLETE | PENDING |
| S016 | Primary counts/effect CI/P reconcile with abstract/narrative/Figure2; Figure3 same-unit rate conflict F-ST1-008. | PASS_1_COMPLETE | PENDING |
| S017 | Death HR.90 within.67–1.22, includes1 with P.50; direction/adjustment coherent. | PASS_1_COMPLETE | PENDING |
| S018 | Stroke HR.86 within.52–1.44, includes1 with P.57; adjusted estimate not crude ratio. | PASS_1_COMPLETE | PENDING |
| S019 | MI/ACS HR1.25 within.82–1.91, includes1 with P.30; direction matches higher crude bedtime rate. | PASS_1_COMPLETE | PENDING |
| S020 | HF HR.72 within.45–1.15, includes1 with P.17; direction matches report. | PASS_1_COMPLETE | PENDING |
| S021 | All-cause hospital/ED HR.93 within.85–1.02, includes1 with P.10; first-event times distinguished from composite. | PASS_1_COMPLETE | PENDING |
| S022 | Nonvertebral fracture HR.92 within.74–1.14, includes1 with P.44; disclosed prospective addition retained. | PASS_1_COMPLETE | PENDING |
| S023 | Hip fracture HR.65 within.37–1.15, includes1 with P.14; separately defined safety event. | PASS_1_COMPLETE | PENDING |
| S024 | Falls RR.96 within.86–1.07, includes1 with P.47; interview-percent mean is not a Poisson crude-risk denominator. | PASS_1_COMPLETE | PENDING |
| S025 | Syncope RR1.28 within.93–1.75, includes1 with P.12; rounded equal symptom means do not specify adjusted RR. | PASS_1_COMPLETE | PENDING |
| S026 | Lightheadedness RR.95 within.90–1.00; printed upper1.00 includes null and P.06 does not conflict. | PASS_1_COMPLETE | PENDING |
| S027 | Glaucoma HR1.13 within.73–1.74, includes1 with P.58; adjudicated diagnoses distinguished from administrative flags. | PASS_1_COMPLETE | PENDING |
| S028 | Vision RR1.02 within.89–1.17, includes1 with P.74; repeated worsening rule matches final SAP. | PASS_1_COMPLETE | PENDING |
| S029 | Cognitive RR.98 within.85–1.13, includes1 with P.82;18-month denominator separately supplied, Poisson plan matched. | PASS_1_COMPLETE | PENDING |
| S030 | Dementia RR1.12 within.83–1.51,P.48 and nursing HR1.38 within.83–2.27,P.21 separately checked; both include1. | PASS_1_COMPLETE | PENDING |
| S031 | Sex both HR/CIs ordered/contain estimates/include1; forest directions match; interaction.10 is separate model/null. Rate pattern F-ST1-008. | PASS_1_COMPLETE | PENDING |
| S032 | Age both HR/CIs ordered/contain/include1; interaction.87 separate; SAP threshold75 matched; rate pattern F-ST1-008. | PASS_1_COMPLETE | PENDING |
| S033 | Frailty both HR/CIs ordered/contain/include1; interaction.22 separate; threshold3 matched; rate pattern F-ST1-008. | PASS_1_COMPLETE | PENDING |
| S034 | Polypharmacy both HR/CIs ordered/contain/include1; interaction.49 separate; threshold5 daily prescriptions matched; rate pattern F-ST1-008. | PASS_1_COMPLETE | PENDING |
| S035 | Health both HR/CIs ordered/contain/include1; interaction.14 separate; threshold75 matched; rate pattern F-ST1-008. | PASS_1_COMPLETE | PENDING |
| S036 | Resistant HTN both HR/CIs ordered/contain/include1; interaction.07 separate; ≥3BP-drug threshold matched; rate pattern F-ST1-008. | PASS_1_COMPLETE | PENDING |
| S037 | HF both HR/CIs ordered/contain/include1; interaction.16 separate; low CI extends plotting scale with arrow; rate pattern F-ST1-008. | PASS_1_COMPLETE | PENDING |
| S038 | Diabetes both HR/CIs ordered/contain/include1; interaction.05 is a distinct rounded heterogeneity test, no within-group significance claim; F-ST1-008. | PASS_1_COMPLETE | PENDING |
| S039 | CAD both HR/CIs ordered/contain/include1; interaction.93 separate; covariance/model mapping absent; rate pattern F-ST1-008. | PASS_1_COMPLETE | PENDING |
| S040 | Stroke/TIA both HR/CIs ordered/contain/include1; interaction.57 separate; combined characteristic matched; rate pattern F-ST1-008. | PASS_1_COMPLETE | PENDING |
| S041 | Apnea both HR/CIs ordered/contain/include1; interaction.54 separate; rate pattern F-ST1-008. | PASS_1_COMPLETE | PENDING |
| S042 | CKD both HR/CIs ordered/contain/include1; interaction.97 separate; unsupported difference-of-log-HR diagnostic excluded; rate pattern F-ST1-008. | PASS_1_COMPLETE | PENDING |
| S043 | Sedentary both HR/CIs ordered/contain/include1; interaction.69 separate; zero exercise threshold matched; rate pattern F-ST1-008. | PASS_1_COMPLETE | PENDING |
| S044 | ACE both HR/CIs ordered/contain/include1; interaction.05 separate; prespecification F-ST1-004 and rate F-ST1-008. | PASS_1_COMPLETE | PENDING |
| S045 | ARB both HR/CIs ordered/contain/include1; interaction.44 separate; prespecification F-ST1-004 and rate F-ST1-008. | PASS_1_COMPLETE | PENDING |
| S046 | Beta-blocker both HR/CIs ordered/contain/include1; interaction.54 separate; prespecification F-ST1-004 and rate F-ST1-008. | PASS_1_COMPLETE | PENDING |
| S047 | CCB both HR/CIs ordered/contain/include1; interaction.66 separate; prespecification F-ST1-004 and rate F-ST1-008. | PASS_1_COMPLETE | PENDING |
| S048 | Diuretic both HR/CIs ordered/contain/include1; interaction.43 separate; prespecification F-ST1-004 and rate F-ST1-008. | PASS_1_COMPLETE | PENDING |
| S049 | Combination both HR/CIs ordered/contain/include1; interaction.72 separate; prespecification F-ST1-004 and rate F-ST1-008. | PASS_1_COMPLETE | PENDING |
| S050 | Exclusion of25% reduction matches primary lower CI>.75; .76 wording matches unadjusted bound and display precision. | PASS_1_COMPLETE | PENDING |
| S100 | Protocol/SAP version order and final attestation considered; missing unavailable publication not assumed to fill a specification. | PASS_1_COMPLETE | PENDING |
| S101 | PROBE/individual eligibility and report population definitions matched; no paired/cluster method conflict. | PASS_1_COMPLETE | PENDING |
| S102 | First composite and components match current report; all-cause death retained, not substituted by cardiovascular death. | PASS_1_COMPLETE | PENDING |
| S103 | Primary event requirement379 reproduces under diagnostic stated survival inputs; same as S004. | PASS_1_COMPLETE | PENDING |
| S104 | 7% inflation379→406 reconciles; projected5% loss is distinct assumption; funding/target change disclosed. | PASS_1_COMPLETE | PENDING |
| S105 | Historical projected2.9%/2.0% distinguish component-count avoidance and assumed effect from actual trial rates; no primary numerical contradiction. | PASS_1_COMPLETE | PENDING |
| S106 | Original outcome classes compared to later supplied SAP and blinded additions; do not turn coherent version evolution into a plan-internal conflict. | PASS_1_COMPLETE | PENDING |
| S107 | Original unblocked/unstratified allocation versus reported block/province strata F-ST1-007; no corresponding supplied amendment located. | PASS_1_COMPLETE | PENDING |
| S108 | Benefit≤.001/harm≤.05 boundaries match report; original200 interim contextualized by disclosed target change. | PASS_1_COMPLETE | PENDING |
| S109 | Original ABPM100/arm updated explicitly to151/arm by2018 amendment; no unsupported size conflict. | PASS_1_COMPLETE | PENDING |
| S110 | Diuretic tolerance adaption is distinct from primary efficacy stop; timing/threshold statement lacks a printed contrary estimate. | PASS_1_COMPLETE | PENDING |
| S111 | Original binary-covariate Cox specification superseded by later SAP matching report; no method preference. | PASS_1_COMPLETE | PENDING |
| S112 | Event-driven projections distinguish assumptions from final enrollment;37%/200-event interim power≈50% diagnostic reconciles. | PASS_1_COMPLETE | PENDING |
| S113 | Claims/telephone supplements matched to outcome-source and censoring definitions; flags distinguished from adjudication. | PASS_1_COMPLETE | PENDING |
| S114 | External-validity comparator and primary treatment subgroups are separate purposes; does not establish six medication treatment interactions. | PASS_1_COMPLETE | PENDING |
| S115 | Recruitment/geographic/sample projections are amended assumptions, not reported primary randomized analysis totals. | PASS_1_COMPLETE | PENDING |
| S116 | Tiered claims follow-up and151/arm amendment matched; voluntary sampling evolution disclosed. | PASS_1_COMPLETE | PENDING |
| S117 | Self-change delivery amendment preserves complex-patient clinical guidance; no statistical paired/cluster/unit conflict. | PASS_1_COMPLETE | PENDING |
| S118 | Recruitment-letter 8%/2points/.05/80% inputs give approximately6400 total in two-group diagnostic; administrative substudy separate. | PASS_1_COMPLETE | PENDING |
| S119 | External-validity comparator cohorts and70000 aggregate population do not define primary randomized analysis or subgroup tests. | PASS_1_COMPLETE | PENDING |
| S120 | Self/claims reconciliation and physician adjudication matched; no event double-count assumption adopted. | PASS_1_COMPLETE | PENDING |
| S121 | One-year extension/end2023 and final funding stop have supplied version context; no stopping-boundary crossing value supplied. | PASS_1_COMPLETE | PENDING |
| S122 |3357 primary/302ABPM and event-days definitions match; future workbook is not supplied data. | PASS_1_COMPLETE | PENDING |
| S123 | All six secondary headings/models/ordered covariates individually matched to current effects; Cox versus Poisson distinguished. | PASS_1_COMPLETE | PENDING |
| S124 | All supplementary safety definitions/models matched; symptom recurrent interview-percent summaries not crude binary proportions. | PASS_1_COMPLETE | PENDING |
| S125 | Costs are not supplied primary/key-secondary estimates; exploratory EQ-5D linear model explains crude-mean diagnostic;302ABPM process population matched. | PASS_1_COMPLETE | PENDING |
| S126 | Claims/no-claims censoring/withdrawal exception compared; F-ST1-006; optional analysis-specific imputation/exclusion not falsely treated as mandatory outcome imputation. | PASS_1_COMPLETE | PENDING |
| S127 | Ordered maximum covariate rule checked:336 events permits primary21 covariate variables including4 province dummies; reduced subgroup/outcome models explicitly described. | PASS_1_COMPLETE | PENDING |
| S128 | All13 planned axes matched; six medication axes F-ST1-004; planned arm-specific sensitivity comparison F-ST1-005. | PASS_1_COMPLETE | PENDING |
| S200 | Every province endpoint-code group read; flags/adjudication distinguished; dementia sensitivity differences explicitly disclosed. | PASS_1_COMPLETE | PENDING |
| S201 | All province medical-service cutoffs/inputs checked against last-contact method; do not compare database cutoffs with nominal overall trial end as event denominators. | PASS_1_COMPLETE | PENDING |
| S202 | Three blinded voting adjudicators and source corroboration rules match report; overlapping reports not additive participants. | PASS_1_COMPLETE | PENDING |
| S203 | First accepted occurrence/date assignment/one-hospitalization attribution rules read; composite components can overlap across different hospitalizations. | PASS_1_COMPLETE | PENDING |
| S204 | All ACS/HF/stroke exclusions/24-hour/imaging/admission/ED rules read; operational rules not substituted for reported inferential model. | PASS_1_COMPLETE | PENDING |
| S205 | Every secondary/safety adjudication rule read and matched; nursing facility control/traumatic fractures/acute admissions distinguished. | PASS_1_COMPLETE | PENDING |
| S206 |151/arm ABPM volunteers, minimum readings/replacement flow, intended6months versus actual9.6months disclosed; no paired within-person arm comparison. | PASS_1_COMPLETE | PENDING |
| S207 | Contact-attempt criteria govern interview loss, distinct from loss of all follow-up; primary censoring compared via S006/S126. | PASS_1_COMPLETE | PENDING |
| S208 | Full18 covariate concepts expand to21 variables with province4 as SAP; reduced models explicitly importance-ordered. | PASS_1_COMPLETE | PENDING |
| S209 | Covariate mean/mode replacement versus main blanket no-imputation F-ST1-003; no outcome imputation agrees with SAP optional exclusion. | PASS_1_COMPLETE | PENDING |
| S210 | Kolmogorov-type PH diagnostic/1000 simulations/allocation versus covariate distinction read; no printed contrary PH test or preferred method. | PASS_1_COMPLETE | PENDING |
| S211 | All disclosed blinded endpoint changes read; final SAP definitions corroborate report rather than treating historical versions as simultaneous statements. | PASS_1_COMPLETE | PENDING |
| S300 | All8 tests and every category checked; same-display reproducing Pearson method chronotype F-ST1-001; pooled-versus-planned contrast F-ST1-005. | PASS_1_COMPLETE | PENDING |
| S301 | Every continuous/categorical/binary test checked, available dementia denominator derived from stated province exclusions; no other over-tolerance test discrepancy; F-ST1-005. | PASS_1_COMPLETE | PENDING |
| S302 | Every category/binary P checked; Pearson BP.1450,total.0474,vitamin.01287 round/reconcile; sparse dialysis.9450 matches.95; F-ST1-005. | PASS_1_COMPLETE | PENDING |
| S303 | All medication/polypharmacy/resistant-HTN tests checked; Pearson.6593,.1929,.6020,.9503,.2345,.03998 reproduce; F-ST1-005. | PASS_1_COMPLETE | PENDING |
| S304 | All tests/category counts checked; Pearson categorical age.5862,chronotype.02958,education.1255,province.9604 match; ethnicity duplicated-count issue retained numeric lane; F-ST1-005. | PASS_1_COMPLETE | PENDING |
| S305 | Every test separately checked; categorical health/SBT/deprivation and all binary rows reproduce within tolerance; continuous medians cannot identify tests; F-ST1-005. | PASS_1_COMPLETE | PENDING |
| S306 | Every medication-number/class test checked; same-display categorical/other binary rows reproduce; diuretic/combination F-ST1-002 and comparison F-ST1-005. | PASS_1_COMPLETE | PENDING |
| S307 | Polypharmacy Pearson.750997 and resistantHTN.710534 match.75/.71; F-ST1-005 contrast. | PASS_1_COMPLETE | PENDING |
| S308 | Awake SBP−2.4 within−5.7,.9; zero inclusion matches.15; SD/N diagnostic compatible; no test engine inferred. | PASS_1_COMPLETE | PENDING |
| S309 | Awake DBP−.4 within−2.5,1.8; zero inclusion matches.72; SD/N diagnostic compatible. | PASS_1_COMPLETE | PENDING |
| S310 | Sleep SBP−7.4 within−11.2,−3.7; zero excluded with<.001; direction and matched main copy reconcile. | PASS_1_COMPLETE | PENDING |
| S311 | Sleep DBP−2.7 within−4.9,−.4; zero excluded with.02; displayed means allow difference through rounding. | PASS_1_COMPLETE | PENDING |
| S312 | Dip3.8 within1.9,5.7; zero excluded with<.001; individual dipping statistic not recomputed from aggregate BP means. | PASS_1_COMPLETE | PENDING |
| S313 | Nondipping54/151 versus78/151 percentages reconcile; Pearson P.005366 matches.005. | PASS_1_COMPLETE | PENDING |
| S314 | Appropriate dipping70/151 versus58/151 percentages reconcile; Pearson.162308 matches.16. | PASS_1_COMPLETE | PENDING |
| S315 | Extreme dipping27/151 versus15/151 percentages reconcile; Pearson.045978 rounds.05; no contrary interval/conclusion printed. | PASS_1_COMPLETE | PENDING |
| S316 | Awake BP62/151 versus49/151 percentages reconcile; Pearson.120767 matches.12; main copy matches. | PASS_1_COMPLETE | PENDING |
| S317 | Awake SBP66/151 versus53/151 percentages reconcile; Pearson.125793 matches.13. | PASS_1_COMPLETE | PENDING |
| S318 | Awake DBP111/151 versus102/151 percentages reconcile; Pearson.255975 versus printed.25 has half-unit gap.000975/ .25=.00390≤.05. | PASS_1_COMPLETE | PENDING |
