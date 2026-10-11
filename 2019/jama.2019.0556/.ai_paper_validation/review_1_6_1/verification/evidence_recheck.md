# Workflow 1.6.1 Mechanical Evidence Recheck

All five stable candidates remain Pending Human Adjudication. This artifact records mechanical evidence facts and classification; it assigns no human disposition.

Fresh evidence_rechecker runtime ID: 01a128e9-9623-7823-b691-4b423018a8b4. Model: gpt-6.1-sol. Reasoning effort: high. Scope: C001, C002, C003, C004 and C005, including every location in the current ledger and independent screening working notes. Read QUALITY_CONTROL_SCOPE.md, review_contract.md, report_spec.md, the complete ledger and initial screening documents, and current source maps. No legacy candidate, disposition, report or external source was used.

## Direct-source method and provenance

Source content determines roles: DOC-001 jama_bot_2019_oi_190007.pdf is REPORT (main results article); DOC-002 joi190007supp1_prod.pdf is PLAN (prospective protocol); DOC-003 joi190007supp2_prod.pdf is PLAN (analysis plan); DOC-004 joi190007supp3_prod.pdf is REPORT (supplementary results and methods); DOC-005 joi190007supp4_prod.pdf is REPORT (published data-sharing statement). Physical supplement numbering is not a role rule. Every page number below is the physical supplied PDF page.

Independently regenerated full-document layout text directly from all five supplied PDFs using CPU-only Poppler pdftotext 26.01.0. Command pattern: `pdftotext -layout SOURCE.pdf .ai_paper_validation/review_1_6_1/preprocessing/recheck/NAME-layout.txt`. Outputs: preprocessing/recheck/main-layout.txt (DOC-001 pp.1–11); protocol-layout.txt (DOC-002 pp.1–60); sap-layout.txt (DOC-003 pp.1–5); results-layout.txt (DOC-004 pp.1–25); data-sharing-layout.txt (DOC-005 p.1). Form-feed boundaries provide physical-page locations. These are fresh source transcriptions, not scientific substitutes for the supplied PDFs.

Direct page rendering used Poppler pdftoppm 26.01.0: `pdftoppm -f N -l N -scale-to 1400 -singlefile -png SOURCE.pdf .ai_paper_validation/review_1_6_1/preprocessing/recheck/NAME-pN`; main p.8 used scale-to 1600. Independently rendered and visually inspected protocol-p16.png, protocol-p23.png, protocol-p28.png, protocol-p43.png, sap-p4.png, main-p8.png and results-p17.png. Native text was usable elsewhere; no targeted OCR, fallback, conversion or GPU was needed. No transcription or page correction affects an assigned ID. Sources and reusable artifacts were not modified. No derivative is claimed as final evidence authority.

## C001 — Planned and reported daily EPA+DHA dose

**Location found; source value/text matched; comparator matched:** Yes, for every listed occurrence. The exact source readings are:

| Exact supplied-source location | Role by content | Directly matched value or text | Function in comparison |
|---|---|---|---|
| [DOC-002 protocol p.1](../../../joi190007supp1_prod.pdf#page=1), cover | PLAN | Version 7, July 11, 2017, protocol with final amendments; initial main-protocol approval dated July 8, 2015 | Version context; no formulation-change mapping |
| [DOC-002 protocol p.8](../../../joi190007supp1_prod.pdf#page=8), Summary Intervention | PLAN | One capsule and one pill; omega-3 1000 mg per capsule, EPA/DHA ratio 3:1, EPA above 700 mg and DHA above 100 mg | Planned repeated dose occurrence |
| [DOC-002 protocol p.18](../../../joi190007supp1_prod.pdf#page=18), §5.1 | PLAN | Two pills daily for one year; omega-3 1000 mg per capsule, EPA/DHA 3:1 | Planned repeated dose/duration occurrence |
| [DOC-002 protocol p.20](../../../joi190007supp1_prod.pdf#page=20), investigational-product composition box | PLAN | Acceptable deviation 90%–125%; detailed compositions referenced to C1.2 | Tolerance context; C1.2 is referenced rather than a separately supplied direct source |
| [DOC-002 protocol p.23](../../../joi190007supp1_prod.pdf#page=23), Omega-3 PUFA fish oils | PLAN | Intended dose explicitly defined as EPA+DHA = 1.0 g per day | Decisive mass definition; visually confirmed |
| [DOC-001 main p.1](../../../jama_bot_2019_oi_190007.pdf#page=1), Interventions | REPORT | Daily supplement includes 1412-mg omega-3 fatty acids for one year | Reported repeated dose occurrence |
| [DOC-001 main p.2](../../../jama_bot_2019_oi_190007.pdf#page=2), Multinutrient Supplements | REPORT | 1412 mg eicosapentaenoic and docosahexaenoic omega-3 PUFAs, ratio 3:1, with other nutrients in two pills daily for one year | Reported explicit EPA+DHA comparator |
| [DOC-004 results p.4](../../../joi190007supp3_prod.pdf#page=4), eAppendix 2 | REPORT | Two pills daily for one year; 1412 mg EPA and DHA, ratio 3:1, in one capsule plus a vitamin/mineral pill | Independent REPORT repetition agrees with main |
| [DOC-004 results p.5](../../../joi190007supp3_prod.pdf#page=5), composition testing | REPORT | EPA 67.9 g/100 g FAME (SD 0.85), DHA 14.6 g/100 g FAME (SD 1.55), selenium average 30 micrograms (SD 0.4) | Composition-test context, not a daily EPA+DHA mass comparator |

**Consistency rule applicable:** Focus D explicitly includes randomized intervention dose. Compare the same defined daily EPA+DHA mass and one-year supplement regimen. The explicit p.23 EPA+DHA definition prevents treating the whole conflict as total-oil versus active-fatty-acid terminology.

**Calculation and display-precision interval check:** 1.0 g/day converts to 1000 mg/day; 1412 − 1000 = 412 mg/day, or 41.2% relative to the planned nominal dose. Applying the printed 125% tolerance to nominal 1000 mg gives 1250 mg, 162 mg below 1412 mg. Even allowing the coarser 1.0-g display its half-unit interval [0.95,1.05) g, or [950,1050) mg, and allowing the integer 125% upper tolerance the generous half-unit ceiling 125.5%, the upper product is below 1050 × 1.255 = 1317.75 mg. This remains below the reported interval [1411.5,1412.5) mg. Thus display precision cannot reconcile the defined daily masses. This interval check is deliberately conservative; it does not reconstruct dose from FAME composition.

**Necessary inputs available:** Units, daily frequency, EPA+DHA definition and duration are supplied; these suffice for the direct comparison. **Exact missing inputs or definitions:** The referenced C1.2 composition document is not separately supplied; no explicit formulation-amendment history maps 1.0 g/day to 1.412 g/day; p.20 does not fully define which composition component receives the tolerance. The mismatch survives even the interpretation that this tolerance applies to EPA+DHA. Capsule oil mass, methylation conversion factors and batch-specific content needed for laboratory dose reconstruction are absent; that reconstruction is not undertaken.

**Source-grounded alternative interpretation:** A revised delivered formulation could coexist with preliminary intended-dose wording retained in the protocol, or the referenced requirements could contain a later formulation. The main and results supplement agree on the delivered dose, so extracting their reported 1412 mg is straightforward; its reconciliation with the supplied planned dose is not documented.

**Direct observation versus inferred explanation:** The defined 1.0-g intended and 1412-mg reported doses, duration and tolerance are directly observed. A formulation revision or retained earlier text is a possible explanation, not a demonstrated event.

**Affected result or extracted value:** EPA+DHA dose attached to the randomized multinutrient primary MDD comparison, whose reported OR is 1.06 (95% CI 0.87–1.29). No numerical change to this OR is asserted.

**Classification confirmation:** Every protocol location is PLAN; main and supplementary results are REPORT. Primary relationship P_R; all relationships P_R; review domain protocol_report. Main and supplementary REPORT doses agree, giving no S_C relationship; tolerance and version context do not create a separate P_P conflict. No correction to provisional classification. **Classification ambiguity:** Formulation amendment chronology and detailed tolerance definition are absent.

**Evidence state:** reproduced. **Determining recheck fact:** Directly read EPA+DHA 1.0 g/day and reported EPA+DHA 1412 mg/day remain separated after a conservative display-precision and tolerance check.

**Exact remaining human question:** What supplied or additional documented formulation specification or amendment reconciles the protocol's intended EPA+DHA 1.0 g/day with the reported 1.412 g/day regimen?

## C002 — Primary MDD model priority and Cox prespecification

**Location found; source value/text matched; comparator matched:** Yes, for every occurrence. Exact readings:

| Exact supplied-source location | Role by content | Directly matched statement/result |
|---|---|---|
| [DOC-002 protocol p.43](../../../joi190007supp1_prod.pdf#page=43), §10.1 Primary study parameter(s) | PLAN | Kaplan–Meier/log-rank/Cox for MDD time-to-event, two-way and four-way intervention analyses; additionally mixed regression for MDD onset and IDS, with strata adjustments and repeated-measure/country handling |
| [DOC-003 SAP p.3](../../../joi190007supp2_prod.pdf#page=3), Fourth analysis | PLAN | Logistic regression for primary new MDD; effect-coded interventions, main effects and interaction, ORs and 95% CIs |
| [DOC-003 SAP p.4](../../../joi190007supp2_prod.pdf#page=4), Secondary analysis | PLAN | Definite commitment to Cox time-to-onset analysis as secondary, with HRs, CIs and P values; visually confirmed |
| [DOC-001 main p.1](../../../jama_bot_2019_oi_190007.pdf#page=1), Main Outcome and Measures/Results | REPORT | Primary cumulative one-year MDD analyzed with logistic regression; supplement/therapy/interaction ORs 1.06/0.93/0.93 |
| [DOC-001 main p.2](../../../jama_bot_2019_oi_190007.pdf#page=2), Study Design | REPORT | Explicitly identifies supplied protocol and SAP; reports primary/secondary mental-health outcomes up to 12 months |
| [DOC-001 main p.4](../../../jama_bot_2019_oi_190007.pdf#page=4), Outcomes and Statistical Methods | REPORT | Logistic primary analysis; time to MDD included for post hoc analysis; Cox modeling explicitly post hoc; onset/censoring at 3,6,12 months and proportional-hazard check described |
| [DOC-001 main p.6](../../../jama_bot_2019_oi_190007.pdf#page=6), Table 2 | REPORT | Primary logistic ORs 1.06 (0.87–1.29), 0.93 (0.76–1.13), 0.93 (0.76–1.14); table's Post Hoc Outcome is time to MDD onset, HRs 1.05 (0.86–1.27), 0.91 (0.75–1.10), 0.91 (0.75–1.11) |
| [DOC-001 main p.7](../../../jama_bot_2019_oi_190007.pdf#page=7), Onset of MDD narrative | REPORT | Repeats logistic ORs and Cox HRs with matching intervals and P values (.57/.47/.48 and .65/.32/.36) |

**Consistency rule applicable:** Focus D covers primary-analysis models and prespecified primary/key-outcome analysis priority. Compare prospective status and hierarchy of matched primary-MDD and time-to-MDD analyses, not equality of OR and HR estimands.

**Calculation or logical comparison and display-precision interval check:** Protocol §10.1 assigns time-to-event/Cox and additional mixed regression to primary-study-parameter analysis; SAP assigns cumulative-MDD logistic as primary and Cox as secondary; report adopts the logistic primary model and labels the Cox result post hoc. The protocol/SAP priority differs, and the explicit SAP secondary Cox commitment remains unreconciled with the report's post hoc designation even if SAP supersedes protocol. The ORs and HRs are consistently attributed to their stated models. Half-unit intervals (±0.005 for two-decimal estimates/CI limits/P values) permit agreement of repeated reported numbers; they cannot change the textual planned-secondary/post-hoc distinction. No crude/model equality or OR/HR equality is applied.

**Necessary inputs available:** The named models, outcome, prospective plan wording, report status labels, covariates, coding and result labels suffice for a status comparison. **Exact missing inputs or definitions:** SAP operative date/version and protocol-to-SAP amendment mapping; whether the phrase post hoc refers to a particular Cox implementation beyond the SAP's time-to-onset provision; any document identifying a prospectively approved replacement of the protocol hierarchy. Participant-level data and full Cox implementation are not needed for this comparison and are not supplied for numerical model reconstruction.

**Source-grounded alternative interpretation:** SAP could prospectively refine or supersede protocol. Post hoc could describe a narrower late Cox implementation rather than the broad secondary time-to-onset estimand. Neither supplied status wording states that distinction; SAP agreement with primary logistic alone does not reconcile its explicit Cox provision.

**Direct observation versus inferred explanation:** Printed model choices and primary/secondary/post-hoc labels are directly observed. Supersession, implementation change or timing of analytical decisions are possible explanations, not source-established events.

**Affected result or extracted value:** Prospective hierarchy of primary ORs 1.06/0.93/0.93 and especially planned-supporting versus post-hoc status of Cox HRs 1.05/0.91/0.91. The method producing each printed number is clear; no arithmetic inconsistency of the effect estimates is asserted.

**Classification confirmation:** Protocol and SAP are PLAN; main article is REPORT. Protocol/SAP hierarchy conflict is P_P; protocol/report priority and SAP/report Cox status are P_R. Primary P_R by precedence over P_P; all relationships P_R, P_P; review domain protocol_report. No S_W relationship because report model/result attribution agrees internally. No correction to provisional classification. **Classification ambiguity:** Operative SAP timing and narrower meaning of post hoc are absent.

**Evidence state:** reproduced. **Determining recheck fact:** The exact SAP sentence prospectively specifies secondary Cox, while the report explicitly calls the corresponding time-to-MDD analysis post hoc, independently of protocol/logistic refinement.

**Exact remaining human question:** Which model hierarchy operated prospectively, and what exact decision, version or implementation distinction reconciles the planned secondary Cox time-to-onset analysis with its reported post hoc status?

## C003 — Planned additive-interaction sensitivity not reported

**Location found; source value/text matched; comparator matched:** Yes. Every positive comparator and the bounded absence scope were checked:

| Exact supplied-source location | Role by content | Directly matched statement/result |
|---|---|---|
| [DOC-003 SAP p.4](../../../joi190007supp2_prod.pdf#page=4), Interaction of the intervention strategies for our primary outcome | PLAN | Multiplicative logistic interaction; additionally definite sensitivity commitment to additive interaction via RERI from a linear odds-ratio model and likelihood-based 95% CI, with lowest-assumed-risk joint reference recoding |
| [DOC-001 main p.1](../../../jama_bot_2019_oi_190007.pdf#page=1), combination Results | REPORT | Combination OR 0.93 (0.76–1.14), P for interaction .48, no additive-scale estimate |
| [DOC-001 main p.4](../../../jama_bot_2019_oi_190007.pdf#page=4), Statistical Methods | REPORT | Effect-coded logistic/Cox methods; GEE without imputation sensitivity; CACE; no RERI/additive sensitivity specification |
| [DOC-001 main p.6](../../../jama_bot_2019_oi_190007.pdf#page=6), Table 2 | REPORT | Logistic interaction OR 0.93 (0.76–1.14), P=.48; Cox interaction HR 0.91 (0.75–1.11), P=.36 |
| [DOC-001 main p.7](../../../jama_bot_2019_oi_190007.pdf#page=7), Onset of MDD | REPORT | Repeats multiplicative logistic and Cox interaction results |
| [DOC-001 main p.8](../../../jama_bot_2019_oi_190007.pdf#page=8), Effect Modification and Sensitivity Analyses | REPORT | Symptom/utility sensitivity without imputation; CACE including primary MDD OR 0.78 (0.64–0.95) for therapy; no additive interaction estimate or reconciliation |
| [DOC-004 results p.21](../../../joi190007supp3_prod.pdf#page=21), eAppendix 11 | REPORT | No-imputation PHQ/IDS/GAD/utility coefficients, including interaction terms; secondary outcomes and different estimands |
| [DOC-004 results p.22](../../../joi190007supp3_prod.pdf#page=22), eAppendix 12 | REPORT | CACE MDD ORs 0.78 (0.64–0.95) and 0.84 (0.67–1.07), plus secondary estimates; no RERI/additive result |

**Bounded full REPORT absence scope:** Fresh full-document layout extraction and searches for RERI, additive/additivity, biological interaction, linear odds, likelihood-based, interaction and sensitivity covered DOC-001 pp.1–11, DOC-004 pp.1–25 and DOC-005 p.1. Positive matches were read in context, all REPORT page contents were cross-checked against complete current maps, and the image-only trajectory figure on DOC-004 p.17 was independently rendered/read: it shows PHQ, IDS, GAD and utility distributions, not additive MDD interaction. The full results supplement contains recruitment/intervention methods, MCID/compliance, CACE description, adherence/adverse events/nutrient changes, secondary trajectories/moderation, no-imputation secondary results, CACE results, concealment and references. DOC-005 [p.1](../../../joi190007supp4_prod.pdf#page=1) provides access conditions and no additional supplied results. No RERI, additive estimate/CI or replacement/deferment explanation was located anywhere within this supplied REPORT union. This is a bounded package reporting absence; it is not a claim that an analysis was unperformed.

**Consistency rule applicable:** Focus D expressly covers a prespecified primary-outcome analysis not reported, including sensitivity specification. SAP's biological rationale is speculative, but its following promise to study additive interaction is definite and not conditioned on significant multiplicative interaction. A logistic product-term OR or a Cox product-term HR does not identify the planned additive-departure estimate.

**Calculation or logical comparison and display-precision interval check:** Source comparison reproduces an explicit planned RERI/CI against a report union containing only other named interaction/sensitivity estimands. No missing RERI is reconstructed from counts: such a calculation would not reproduce the specified model, recoding, covariates and likelihood CI. Printed multiplicative estimates/intervals repeat within half-unit display intervals; no numerical discrepancy in those repeated values forms this candidate. Display rounding cannot supply an absent distinct estimand or an explanation of its reporting status.

**Necessary inputs available:** Exact unconditional primary-MDD additive sensitivity commitment and complete supplied REPORT coverage suffice for the reporting comparison. **Exact missing inputs or definitions:** RERI estimate, likelihood-based 95% CI, actual joint-reference recoding, and any documented replacement, deferral or omission decision. Full fitted model parameters/covariance and individual data for independent reproduction are absent. Actual analysis execution remains unknown.

**Source-grounded alternative interpretation:** The additive analysis might have been conducted but not included in these supplied results, or prospectively replaced/deferred. Other reported sensitivities answer different questions; none is labeled as replacing this one.

**Direct observation versus inferred explanation:** The SAP commitment, named multiplicative results, other sensitivity outputs and bounded absence are observations. Nonexecution, replacement, deferral and any change in substantive conclusion are not established.

**Affected result or extracted value:** Completeness and additive-scale interpretation of the primary MDD combined-intervention evidence; the promised RERI estimate/CI is unavailable to extract. No conclusion reversal is claimed.

**Classification confirmation:** SAP is PLAN; main/results supplement/data-sharing material are REPORT. Primary P_R; all relationships P_R; domain protocol_report. REPORTs jointly establish coverage rather than conflicting with one another, so no S_C/S_W relationship. No correction to provisional classification. **Classification ambiguity:** Whether the analysis was actually performed is outside supplied evidence.

**Evidence state:** reproduced. **Determining recheck fact:** The unconditional SAP primary-outcome RERI/CI commitment is present; no corresponding result or reconciliation is present in the complete supplied REPORT union.

**Exact remaining human question:** Where is the planned primary-MDD additive-interaction RERI and likelihood-based 95% CI, or the documented explanation reconciling that commitment with the supplied reported interaction evidence?

## C004 — IDS endpoint hierarchy across protocol, SAP and report

**Audit contextual supplementation:** The subsequent fresh quality auditor independently reread [DOC-002 protocol p.14, Secondary Objective](../../../joi190007supp1_prod.pdf#page=14). That paragraph includes depressive symptom scores among secondary outcomes, without naming IDS specifically. This is additional context for the same reproduced placement comparison, rather than a new candidate or a rechecker inference. The auditor recorded QUESTIONED inclusion because broad protocol headings do not establish a formal co-primary/key hierarchy. The evidence state and classifications below remain reproduced, protocol_report, P_R with P_P; the initial recheck's direct facts are preserved.

**Location found; source value/text matched; comparator matched:** Yes, for all affected locations:

| Exact supplied-source location | Role by content | Directly matched statement/result |
|---|---|---|
| [DOC-002 protocol p.9](../../../joi190007supp1_prod.pdf#page=9), continuation of Main study parameters/endpoints from p.8 | PLAN | IDS depressive symptomatology at baseline,3,6,12 months listed under main-endpoint summary |
| [DOC-002 protocol p.28](../../../joi190007supp1_prod.pdf#page=28), §§8.1.1/8.1.2 | PLAN | IDS is included in Main study parameter/endpoint with MDD; separate Secondary study parameters/endpoints lists other measures |
| [DOC-002 protocol p.43](../../../joi190007supp1_prod.pdf#page=43), §§10.1/10.2 | PLAN | IDS severity mixed-regression analysis belongs to Primary study parameter(s); PHQ-9 and other outcomes belong to distinct Secondary study parameter(s) |
| [DOC-003 SAP p.2](../../../joi190007supp2_prod.pdf#page=2), Outcomes | PLAN | Cumulative MDD primary; PHQ-9 and IDS30-SR at T3,T6,T12 explicitly secondary |
| [DOC-001 main p.4](../../../jama_bot_2019_oi_190007.pdf#page=4), Secondary Outcomes/Statistical Methods | REPORT | IDS30-SR depression severity is secondary; secondary analyses should be interpreted as exploratory because of multiple comparisons |
| [DOC-001 main p.8](../../../jama_bot_2019_oi_190007.pdf#page=8), Table 3/IDS narrative | REPORT | Secondary-outcome IDS supplement overall coefficient 0.60 (0.15–1.05), P=.01; footnote doubles coefficient/CI for adjusted mean difference; narrative 1.20 (0.29–2.10), P=.01 |

**Consistency rule applicable:** Focus D includes endpoint hierarchy. The same IDS symptom severity and repeated follow-up window are matched. Protocol's main-endpoint list and distinct primary-analysis subsection support a hierarchy comparison; no formal co-primary decision rule or required multiplicity adjustment is inferred.

**Calculation or logical comparison and display-precision interval check:** The direct hierarchy contrast is protocol main/primary-study-parameter placement versus SAP/report secondary placement and report exploratory interpretation. It is textual and not resolved by decimal precision. The apparent 0.60-versus-1.20 numeric contrast reconciles by the explicit effect-coding factor 2: coefficient interval [0.595,0.605) doubles to [1.19,1.21), overlapping narrative mean-difference interval [1.195,1.205). Lower CI 0.15 permits [0.145,0.155), doubled [0.29,0.31), overlapping printed 0.29's interval [0.285,0.295); upper 1.05 permits [1.045,1.055), doubled [2.09,2.11), overlapping 2.10's interval [2.095,2.105). Thus numeric estimates and limits can agree under stated coding and display precision; that contrast is not the registered issue.

**Necessary inputs available:** Endpoint identity, follow-up windows, headings/list membership, analysis placement and reported interpretation suffice for the hierarchy comparison. **Exact missing inputs or definitions:** An operational definition distinguishing protocol main/primary study parameters from formally co-primary/key endpoints; operative SAP timing and hierarchy-amendment mapping; any formal co-primary success or multiplicity rule. Those definitions cannot be inferred from mere list membership.

**Source-grounded alternative interpretation:** The protocol could use main/primary study parameters broadly rather than designate formal co-primary endpoints; SAP might prospectively refine or reclassify the outcome. IDS's placement in both main-endpoint and primary-analysis sections, while PHQ-9 appears separately in the secondary analysis section, prevents identifying that intended reconciliation from an isolated synonym alone.

**Direct observation versus inferred explanation:** Headings, IDS membership, secondary/exploratory report language and reported coefficient are observations. Formal co-primary status, prospective reclassification and multiplicity consequences remain unestablished explanations or questions.

**Affected result or extracted value:** Prospective hierarchy attached to IDS supplement overall coefficient 0.60 (0.15–1.05), P=.01, equivalent within coding/precision to adjusted mean difference 1.20 (0.29–2.10). No numeric effect discrepancy is asserted.

**Classification confirmation:** Protocol/SAP are PLAN; article is REPORT. Protocol/SAP hierarchy contrast is P_P; protocol/report hierarchy contrast is P_R. Primary P_R by precedence, all relationships P_R, P_P, domain protocol_report. SAP/report agreement creates no extra relationship. No correction to provisional classification. **Classification ambiguity:** Formal co-primary designation and prospective amendment chronology are not established.

**Evidence state:** reproduced. **Determining recheck fact:** IDS is directly printed under both protocol main-endpoint and primary-analysis headings, while SAP/report explicitly classify the same measure secondary; the printed effect magnitudes reconcile and are not the basis.

**Exact remaining human question:** What operative prospective IDS hierarchy and definition of main/primary study parameter reconcile its protocol placement with SAP/report secondary and exploratory status, without presuming a formal co-primary rule that the supplied package does not state?

## C005 — Primary MDD power assumptions and contrasts

**Location found; source value/text matched; comparator matched:** Yes, including both continuation and contextual report occurrences:

| Exact supplied-source location | Role by content | Directly matched statement/result |
|---|---|---|
| [DOC-002 protocol p.1](../../../joi190007supp1_prod.pdf#page=1), cover | PLAN | Version 7 with final amendments; no calculation-amendment mapping |
| [DOC-002 protocol p.16](../../../joi190007supp1_prod.pdf#page=16), §4.4 | PLAN | Expected control (placebo/no FBC) 30%, intervention 15%; additive-interaction interest; 180/group, two-sided alpha .05, power .90; dropout 20%, 250/intervention arm |
| [DOC-002 protocol p.17](../../../joi190007supp1_prod.pdf#page=17), continuation | PLAN | 250 sufficient; greater IDS power; if synergistic rather than additive, pure treatment groups compared with 80% power |
| [DOC-001 main p.4](../../../jama_bot_2019_oi_190007.pdf#page=4), Sample Size | REPORT | Sample size based on primary outcome/factorial design; 33% relative reduction, active 20% versus control 30%; 392 participants with 196 in each of four combinations; main effects, alpha .05, power .90; attrition 22%, 250/combination; absolute difference 10% |
| [DOC-001 main p.9](../../../jama_bot_2019_oi_190007.pdf#page=9), Discussion and Limitations | REPORT | MDD onset lower than expected and statistical power reduced; attrition about a quarter |

**Consistency rule applicable:** Focus D includes sample-size/power assumptions and prospective versus reported primary-design specifications. The protocol explicitly names an additive-interaction interest and conditional synergistic pure-group contrast; the article explicitly names intervention main effects. These contrasts are preserved separately. A single identical marginal population or common sample-size algorithm is not assumed.

**Calculation or logical comparison and display-precision interval check:** The stated active-incidence inputs differ by 20 − 15 = 5 percentage points; nominal differences from 30% control are 15 and 10 percentage points respectively. Dropout inputs differ by 22 − 20 = 2 percentage points. Integer-percent half-unit intervals for active incidence [14.5,15.5)% versus [19.5,20.5)% do not overlap; dropout intervals [19.5,20.5)% versus [21.5,22.5)% do not overlap. Report's (30−20)/30 = 1/3 relative reduction reconciles with displayed 33%, and the absolute difference is 10 percentage points. Report's 196/392 wording is context-resolved through factorial cell versus marginal intervention allocations and is not a basis for this candidate. Protocol introductory 25% wording is also not used. No claim that 180 or 196 fails an exact power algorithm is made. Different contrast calculations need not yield equal sample sizes. Their common approximately 250-per-cell recruitment target does not itself map the two stated assumption sets and objectives to the operative design basis.

**Necessary inputs available:** Printed expected risks, attrition inputs, alpha/power and named contrasts suffice to compare the specifications. **Exact missing inputs or definitions:** A calculation or amendment mapping stating how the protocol's interaction-oriented assumptions and the article's main-effect assumptions jointly governed or revised recruitment; exact interaction alternative, group comparison and calculation algorithm; any explicit designation of one calculation as supplementary rather than operative. Individual data and full design calculation are not supplied for exact achieved-power reproduction.

**Source-grounded alternative interpretation:** The protocol may describe an interaction-oriented calculation and article a separate main-effect calculation; both could coexist and support the same target. Alternatively, assumptions could have been prospectively revised while the protocol retained earlier wording. The contrast difference explains why their arithmetic need not coincide but does not establish the operative mapping. This is the strongest alternative and remains a live human question, not evidence of an arithmetic failure.

**Direct observation versus inferred explanation:** The distinct input sets, contrasts, sample targets and lower-than-expected-onset discussion are directly observed. Assumption revision, supplementary calculation or their joint role in recruitment is not established. No change in the primary null result or achieved power is calculated.

**Affected result or extracted value:** Extraction of primary-design incidence/effect/attrition assumptions and powering contrast accompanying the reported primary MDD result; interpretation of which prospective basis underlies its power discussion.

**Classification confirmation:** Protocol is PLAN and main is REPORT. Primary P_R, all relationships P_R, domain protocol_report. SAP provides no separate powering comparator, so it contributes neither P_P nor a corroboration relationship. No correction to provisional classification. **Classification ambiguity:** Explicitly distinct contrasts may coexist; their operational mapping and revision chronology are absent. Do not identify the two active-rate assumptions as demonstrably identical marginal contrasts.

**Evidence state:** reproduced. **Determining recheck fact:** The printed primary-design risk/attrition specifications differ beyond precision, and their distinct declared objectives are not mapped to one another in the supplied design account. This state records the reproduced specification difference; it does not establish that the two calculations could not coexist.

**Exact remaining human question:** How do the protocol's 30%/15%,20%-dropout interaction-oriented specification and the report's 30%/20%,22%-attrition main-effect specification jointly define or revise the operative primary-design power basis for the shared recruitment target?

## Final recheck classification and scope reconciliation

| ID | Compared document roles | Relationship type | All relationships | Review domain | Evidence state | Classification change |
|---|---|---|---|---|---|---|
| C001 | PLAN protocol pp.8,18,20,23 vs REPORT main pp.1,2 and results pp.4,5 | P_R | P_R | protocol_report | reproduced | None |
| C002 | PLAN protocol p.43 vs PLAN SAP pp.3,4 and REPORT main pp.1,2,4,6,7 | P_R | P_R, P_P | protocol_report | reproduced | None |
| C003 | PLAN SAP p.4 vs REPORT main pp.1,4,6,7,8 and results pp.21,22; full REPORT union main pp.1–11/results pp.1–25/data-sharing p.1 | P_R | P_R | protocol_report | reproduced | None |
| C004 | PLAN protocol pp.9,28,43 vs PLAN SAP p.2 and REPORT main pp.4,8 | P_R | P_R, P_P | protocol_report | reproduced | None |
| C005 | PLAN protocol pp.16,17 vs REPORT main pp.4,9 | P_R | P_R | protocol_report | reproduced | None |

Covered IDs: C001–C005, five of five. Every cited affected location is found and matched. Evidence states: reproduced 5; reproduced_after_transcription_correction 0; not_reproduced 0. Classification changes: 0. Direct-source extraction and visual confirmation introduced no candidate-affecting transcription/location change. Inclusion threshold remains subject to independent audit, particularly the bounded hierarchy and contrast alternatives in C004/C005; this recheck does not adjudicate those alternatives. All IDs remain Pending Human Adjudication.

Unresolved source-grounded items: referenced formulation requirements/amendment history; SAP operative chronology; exact scope of the post hoc Cox designation; actual additive-analysis execution and missing reported RERI/CI; formal IDS hierarchy definitions; mapping of distinct power contrasts/input sets. No technical tooling gap, unresolved cited location or unmapped REPORT absence-scope unit limits this recheck. No extra candidate was introduced and no stable ID was deleted or suppressed.
