# Statistical pass 1 — PLAN specifications and implementation

- Runtime agent ID: root/statistics_pass_1_plans.
- Model and effort: gpt-6.1-sol / high; FRESH_SPAWN, pass 1 only.
- Exact scope: DOC-002 protocol physical pages 1–77 and DOC-003 SAP physical pages 1–29. Matching REPORT methods and result labels were used to assess implementation of planned specifications. REPORT estimate/interval/test pairs are assigned to separate statistical shards.
- Relationship scope: S221–S288, 68 relationships. Every record is PASS_1_COMPLETE; pass 2 is pending.
- Findings: 3, F-ST1-221, F-ST1-222, F-ST1-223. Excluded apparent observations: 11. No finding count was targeted.

QUALITY_CONTROL_SCOPE.md and the complete review contract were read. The four fresh PLAN map parts, relevant raw source OCR, amendment histories and direct page images were consulted. Direct visual checks include protocol pages 56–57, SAP pages 19–21, results supplement pages 4/9 and main article page 4. Main and supplement method passages were matched to outcome, time, contrast and population before comparison. PLAN font-corrupted native text was not treated as scientific authority. New REPORT page renders used direct Poppler pdftoppm 26.01.0 at 140 dpi, CPU, saved to preprocessing/stat1_plans/report-p04.png, report-p09.png and main-p04.png. Pre-existing page images were preserved. No web, external reference, old checker conclusion or unpermitted Python was used.

## Findings

### F-ST1-221

**Title:** Age is called a prespecified base adjustment variable without being part of the supplied fixed primary model specification.

**Relationships:** S262. Proposed relationship type P_R; all relationships P_R. Focus area D. Proposed review domain protocol_report.

**Exact locations and document roles:**

- PLAN [protocol physical page 56, section 15.5](../../../../joi250046supp1_prod_1755300121.14087.pdf#page=56): primary-model adjustment paragraph.
- PLAN [SAP physical page 20, section 14.0](../../../../joi250046supp2_prod_1755300121.15087.pdf#page=20): primary-model adjustment paragraph, with section 13.0 on the same page as contextual alternative.
- PLAN [SAP physical pages 2–4, amendment history](../../../../joi250046supp2_prod_1755300121.15087.pdf#page=2): no recorded addition of age as a fixed primary-adjustment variable; age subgroup analysis is expressly added on page 2.
- REPORT [results supplement physical page 4, Adjustment paragraph](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=4): list immediately after “base set of pre-specified adjustment variables.”
- REPORT [results supplement physical page 5, Non-Response Weighting paragraph](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=5): prespecified prediction-variable list also includes age.
- REPORT [results supplement physical pages 8–10, eTables 3–5](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=8): fitted imputation, estimation and weight models print an age term, establishing application to the reported primary analysis.

**Printed statements compared:** Both operative PLAN primary paragraphs specify baseline pain severity, sex, clinical site, rural/medically underserved residency, multisite pain and co-occurring mental health condition. The REPORT's base prespecified list adds “age” to those six covariate concepts. SAP section 13.0 lists age among demographic/descriptive candidate variables and age ≥65 among moderators, but does not specify age as a fixed primary adjustment covariate. Its dated age amendment adds subgroup analyses rather than primary fixed adjustment.

**Rule and reproduced comparison:** An analysis described as prespecified must appear in the supplied plan at the corresponding analysis role. Set comparison of the enumerated fixed primary covariates leaves REPORT age without a corresponding fixed-primary PLAN term. This is a textual specification comparison; display rounding and numerical recomputation are not applicable. The age term is present in all three fitted primary-analysis model summaries, so the observation concerns an implemented specification rather than an unused variable. Directly inspected eTable 4 prints the indicator “Age >=65 (vs. <65),” RR 1.15, 95% CI 1–1.33, P .046; those inferential values are tracked by the separately assigned REPORT statistical shard, while this finding concerns the adjustment's prespecification status.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** The reported primary 3-month adjusted pain-severity response, RR and interval, and their imputation/weighting specification; interpretation of age adjustment as prespecified rather than added.

**Why context does not resolve it:** This is the always-register category for an analysis described as prespecified that the supplied plan does not contain in the claimed role. The general candidate-variable paragraph and moderator listing do not specify which demographic candidates must enter the fixed primary model.

**Source-grounded alternatives and missing definition:** The authors may have regarded the broad section 13.0 candidate list as authorization for age adjustment, or a separately documented fixed-model revision may exist outside this supplied package. The REPORT may have added age as a chosen adjustment variable while retaining the label prespecified. No direction or magnitude of its impact is inferred.

**Exact human question:** Which supplied prospective specification makes age a fixed base adjustment variable for the primary imputation, estimation and nonresponse-weight models, and how should its prespecification status be read alongside the enumerated protocol/SAP primary covariates?

### F-ST1-222

**Title:** The SAP's primary MAR description and the report's primary MNAR analysis have different stated roles.

**Relationships:** S264–S266. Proposed relationship type P_R; all relationships P_R. Focus area D. Proposed review domain protocol_report.

**Exact locations and document roles:**

- PLAN [SAP physical page 19, section 11.0 Missing Data](../../../../joi250046supp2_prod_1755300121.15087.pdf#page=19): first primary-analysis sentences and sensitivity-trigger paragraph.
- PLAN [SAP physical page 4, 07/17/24 IPW amendment](../../../../joi250046supp2_prod_1755300121.15087.pdf#page=4): missing-all weighting amendment, preserving the all-randomized interpretation.
- REPORT [main article physical page 4, Statistical Analysis](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4): primary missingness addressed by nonignorable pattern-mixture imputation and missing-all IPW.
- REPORT [results supplement physical page 4, first Missing Data paragraph](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=4): claims the SAP prespecified criteria for the primary analysis to use an MNAR imputation approach with weighting and regression adjustment.
- REPORT [results supplement physical page 11, eTable 7](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=11): complete-case approach is reported as a sensitivity analysis rather than the principal result.

**Printed statements compared:** The SAP says that for primary analyses patients with follow-up will be analyzed and missing data assumed MAR given baseline covariate adjustment. It then calls for sensitivity analyses when >15% are missing the 3-month outcome or arm missingness differs, and describes pattern-mixture imputation plus missing-all IPW as its first approach and worst/best case as its second approach. The REPORT says the >15%/differential criteria prespecified an MNAR primary analysis, and implements pattern-mixture/IPW as primary. The REPORT prints 77.1% 3-month completeness overall, 79.9% UC, 69.8% painTRAINER and 81.6% health coach.

**Rule and reproduced comparison:** Keep method identity separate from its planned primary/sensitivity role. Pattern-mixture and IPW are indeed in the SAP; this finding concerns the explicitly stated primary MAR role versus the implemented primary MNAR role and the REPORT's claim of a prespecified switch. The supplied SAP does not expressly say that meeting the trigger replaces the primary MAR analysis with the MNAR approach. Arithmetic confirms the trigger was met: 100−77.1=22.9% missing at 3 months, exceeding 15%; arm completeness also differs. There is no rounding-sensitive numeric inconsistency: the logical discrepancy is the analysis role. Recomputed numeric interval for overall missingness is [22.85%,22.95%] from completeness 77.1±0.05%, entirely above the displayed 15±0.5% threshold.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** The principal adjusted 3-month MCID response/RR and intervals, and whether they represent the planned primary MAR analysis or a promoted missing-data sensitivity approach.

**Why context does not resolve it:** This is the always-register category for a planned primary analysis that is replaced, and for a claimed prespecified analysis role absent from the explicit supplied specification. The SAP's first-approach language supplies a possible interpretation of the switch, but does not explicitly reconcile its earlier primary-MAR sentences.

**Source-grounded alternatives and missing definition:** The first approach after the trigger may have been intended as the conditional primary analysis, with worst/best case alone designated sensitivity; the prose can support that interpretation. Alternatively, both approaches may have been planned sensitivities while the REPORT selected MNAR as primary. The July2024 amendment authorizes weighting for an all-randomized estimand but does not separately state a replacement of the primary MAR role. No judgment about a preferred missing-data method is made.

**Exact human question:** Did the >15%/differential-missingness trigger prospectively replace the SAP's stated MAR primary analysis with the MNAR pattern-mixture/IPW analysis, and where does the supplied plan explicitly define that primary-versus-sensitivity role?

### F-ST1-223

**Title:** Reported baseline adjustment for key secondary outcomes includes the outcome's own baseline, beyond the operative secondary plan paragraph.

**Relationships:** S267–S268. Proposed relationship type P_R; all relationships P_R. Focus area D. Proposed review domain protocol_report.

**Exact locations and document roles:**

- PLAN [protocol physical page 57, section 15.6](../../../../joi250046supp1_prod_1755300121.14087.pdf#page=57): final secondary-model paragraph.
- PLAN [SAP physical page 21, section 15.0](../../../../joi250046supp2_prod_1755300121.15087.pdf#page=21): final secondary-model paragraph.
- REPORT [main article physical page 4, Statistical Analysis](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4): secondary models use the same modeling structures “with added adjustment for the given baseline secondary outcome.”
- REPORT [main article physical page 9, Table 2](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9): adjusted intensity/interference MCID results; [physical pages 10–11, Table 3](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10): adjusted continuous severity, intensity, interference and functioning results.

**Printed statements compared:** The operative protocol and SAP secondary paragraphs specify baseline levels of pain severity and all stratification variables as covariates. They prescribe continuous linear and binary/count Poisson GEE with arm×time terms. The main REPORT states that the secondary analysis uses the same primary-model structures with additional adjustment for the given baseline secondary outcome. For intensity, interference, social function and physical function, that own-baseline measure is a distinct covariate from the specified composite baseline pain severity.

**Rule and reproduced comparison:** Match each secondary measure before comparing model covariates. Composite baseline severity is not identical to baseline intensity, baseline interference or baseline PROMIS function. The reported explicit addition is absent from the operative secondary specification; the supplied amendment histories do not record adding own-baseline secondary adjustment. This is a textual specification comparison with no numerical rounding interval or relative discrepancy applicable. Continuous overall severity is not counted as a distinct discrepancy because its own baseline equals the plan's baseline pain-severity measure. Global impression is not included in the affected list because no baseline PGIC collection is planned.

**Qualifying route:** Route B.

**Affected result or extracted value:** The adjusted secondary intensity/interference MCID RRs and the adjusted between-group continuous intensity, interference, social-function and physical-function differences and intervals in Tables 2–3; these outcomes also appear in the abstract and therefore are key secondary under this workflow.

**Why context does not resolve it:** The plan and report identify different covariate sets for the same outcome/time contrasts. The phrase “same proposed approach as Aim 1” establishes shared modeling structure, but does not specify the additional own-baseline covariate later described in the REPORT. Which planned covariate set produced the tabulated results matters for analysis extraction.

**Source-grounded alternatives and missing definition:** The plan's listed covariates may have been intended as a minimum rather than an exhaustive list, or own-baseline secondary adjustment may have been understood as part of that shared approach. A separate prespecified expansion is not supplied. The REPORT explicitly discloses its adjustment, so this finding does not assert that the fitted result is unidentified or that a different analysis should have been used.

**Exact human question:** Were the distinct baseline intensity, interference and PROMIS function covariates prospectively included in the secondary models, and how should the explicit REPORT addition be reconciled with the protocol/SAP secondary covariate paragraph?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| PLAN protocol pp22–23; SAP p11; explicit secondary analysis protocol p57/SAP p21 | Intensity/interference MCID measured-by cells omit 3 months while time-frame cells and explicit analysis specify 3 months; immediate analysis text supplies intended collection/analysis time. | CONTEXT_RESOLVES |
| PLAN protocol p22; SAP p11 | Interference MCID description repeats the word intensity, but the row names interference and the 7-item interference subscale; the intended endpoint is immediate. | TERMINOLOGY_OR_WORDING |
| PLAN protocol p25 versus pp57–58; SAP pp14,22 | Moderator overview says 6 months while operative interaction paragraph says primary comparison 3 months; no reported moderator result depends on either in this efficacy package. | PERIPHERAL_COMPARISON |
| PLAN protocol p27/SAP p15 versus protocol p58/SAP pp22–23 | Perceived support is measured at notification rather than baseline while mediation prose describes baseline-to3-month change; mediation results are absent and this is outside primary analysis used by this report. | PERIPHERAL_COMPARISON |
| PLAN SAP p23 | Mediation Step3a prose adjusts baseline confounders but printed assignment formula omits them; no reported mediation result uses this model. | PERIPHERAL_COMPARISON |
| PLAN protocol p5 versus p32; SAP pp3,17; REPORT main p2 | Historical KP encounter-separation amendment30 days versus operative>60 days; report follows operative>60 days and supplied evidence does not establish a changed analysis-population size or primary decision rule. | PERIPHERAL_COMPARISON |
| PLAN SAP p4; REPORT results supplement pp4,6 | Amendment rationale missing-all12.1% versus reported12.7%; the rationale is a historical missingness summary, not a conflicting primary result or analyzed population count. | PERIPHERAL_COMPARISON |
| PLAN protocol/SAP power tables pp55/16 | “Relative change” might be read as percentage increase, but table explicitly defines it as %Intervention/%UC;150%,206.7%,184.7%,172% reconcile as ratios. | TERMINOLOGY_OR_WORDING |
| PLAN primary sample-size passages; REPORT main p4 | Simple two-arm independent-proportion normal approximation need not give exactly621/arm, but reported power uses10000modified-Poisson simulations with LSD gate. Exact simulated power event/third-arm configuration are absent; no source-supported reproducing calculation is available. | CONDITIONAL_OR_UNREPORTED |
| PLAN SAP pp18,21; REPORT main p5 | Broad all-randomized wording versus exclusion of two UC EHR-ineligible participants: SAP separately qualifies eligible subjects, and the report flow explicitly locates the exclusions. This reading is immediately resolved by population qualification. | CONTEXT_RESOLVES |
| PLAN SAP pp19–20; REPORT results supplement pp4–7 | Additional predictor-selection thresholdP<.10 and exact imputation/weight covariates are detailed in REPORT but not fully in SAP. These additional variables are expressly described as selected rather than all prespecified; absent detail alone is not a finding. This does not subsume the age-prespecification issue. | CONDITIONAL_OR_UNREPORTED |

## Coverage, reconciled checks and limitations

Every assigned inferential relationship is recorded in statistics/parts/relationship_inventory_plans.md. Reconciled checks include primary endpoint status, 11-item composite, 30% threshold and 3-month time; 6/12-month secondary times; all abstract secondary outcomes and their planned status; allocation and strata; modified-Poisson RR family/link and GEE variance rationale; power input arithmetic and retention; hierarchy and LSD omnibus gate; explicit missing-data trigger and IPW amendment; worst/best-case sensitivity; after 8/9/2021 onboarding sensitivity; as-treated conditional rule; adherence 75%=6/8; planned safety descriptives/no formal testing; and no formal efficacy/futility interim analysis. No numerical interval/test conflict is printed in this PLAN scope. The planned mediation/economic specifications were completely inventoried, but absent result implementations were not invented. No broad study-design, clinical or preferred-analysis review was performed.

All106 assigned PLAN physical pages are covered by fresh source maps and this complete planned relationship inventory. Bibliography and administrative units do not add original inferential results. Exact power simulation details are absent, so no unsupported sample-size contradiction is claimed. No scientific coverage gap. Findings concern supplied textual analysis specifications, with source-grounded alternatives for independent screening and human adjudication.
