# Inclusion, classification, and evidence-card quality audit

Pending Human Adjudication. This independently reasoned audit covers C001, C002, C003, C004, C005; all 13 checker findings and screening decisions; all 37 initial checker exclusions (13 numeric, 9 cross-source, 15 statistical); and all 37 corresponding pass-2 exclusion revisits. No finding count, earlier candidate selection, external literature, or other package controlled these decisions. Counts below describe completed work only. Source-unit, relationship-inventory, reuse, routing, and execution coverage are audited in the separate assigned coverage part and must be merged by the coordinator.

The five candidates satisfy the inclusion threshold: 5 CONFIRMED, 0 QUESTIONED. Two qualify through Route A category 5; three through Route B. No additional qualifying excluded or screened-out observation was identified. No new F-QA finding or screening reversal is required. Every stable ID is retained.

## Source authority and reproducibility

Read completely: AGENTS.md, QUALITY_CONTROL_SCOPE.md, PERFORMANCE_PROFILE.md, workflow_1_6_2/review_contract.md, workflow_1_6_2/report_spec.md, workflow_1_6_2/settings.toml, and tooling_record.md. Read the complete current ledger, screening decisions, and mechanical recheck; every initial checker finding/exclusion; and pass 2's candidate implications and every prior-exclusion revisit. Full relationship tables remain the assigned coverage auditor's scope. Current workflow artifacts are audit subjects, not legacy discovery inputs.

Fresh direct Poppler `pdftotext -layout` derivatives were written only under `preprocessing/quality_inclusion_audit/`: main.txt, plan.txt, supp2.txt, and supp3.txt, from the four exact supplied PDFs respectively. Engine: direct Poppler; compute device: CPU; no OCR, Office conversion, Python scientific review, or web was used. These are locators; supplied PDF pages and source-derived renders remain authority. Visually inspected current source-derived PLAN pp.10,12,14,15,16 and REPORT pp.3,4,5,7. Direct source text separately checked the full REPORT union, the eight randomized-group titles, recruitment/history comparisons, Table 5 on PLAN p.29, and the other exclusion anchors. Existing recheck page-inspection evidence supports the exhaustive REPORT absence test. Sources and reused assets were read only.

Source links in this unique part are relative to `quality/parts/`; when merging into `quality/evidence_quality_audit.md`, the coordinator must rebase `../../../../` to `../../../` without changing filenames or page anchors. PDF pagination means PDF file page, not journal page. Main PDF pp.3–9 correspond to journal pp.624–630; PLAN page numbers and file pages align at the cited locations. No Office pages were fabricated.

## C001 — Primary relapse score component differs from the plan

**Inclusion audit: CONFIRMED.** The discrepancy is reproduced and qualifies through **Route A, category 5**: the printed primary composite score component changes from HAM-D ≥18 plus an additional 5-point increase relative to RCT entry in [PLAN p.12, lines 553–568](../../../joi190079supp1_prod.pdf#page=12) to HDRS ≥18 as a sufficient listed component in [REPORT p.4](../../../jama_flint_2019_oi_190079.pdf#page=4). The immediate source identifies the same 17-item scale. Its two names are not a discrepancy. No rounding comparison is applicable to the presence of the conjunction.

The diagnostic arithmetic reproduces: 18−15=3, below 5. This is a hypothetical illustration of the printed rules only. Other composite routes can still classify the hypothetical person, and no actual event is reassigned. The plan's preferred duration allows a safety exception. Psychiatric-hospitalization causes reconcile through [REPORT Table 3 p.7](../../../jama_flint_2019_oi_190079.pdf#page=7). The SADS qualification is operational context; no distinct unresolved psychosis criterion is inferred from the instrument wording.

Classification audit: PLAN prospective endpoint versus REPORT endpoint definition; primary relationship **P_R**; all relationships **P_R**; domain **protocol_report**; evidence state **reproduced**. No S_W is added for agreeing report copies, and no corroborating plan statement creates an additional relationship. P_R is the only conflict and therefore satisfies precedence. The ledger's compared roles and finding IDs F-XS-001, F-ST1-001 agree with the recheck and screening log.

Evidence-card audit: exact source/comparator, affected primary counts 13/64 and 34/62, HR 0.25 [0.13,0.48], rule, calculation, alternatives, context category, and remaining operational question are present. No transcription or pagination repair is needed. Carry forward the narrow additional-5-point statement, not the initial checker's broader hospitalization/psychosis summary. A source-grounded abbreviation or unprovided amendment remains possible. Bounded downstream impact: an extractor could copy the score-only primary-relapse definition; the supplied package does not establish that counts, HR, or the conclusion would change.

## C002 — Four prespecified key secondary counterparts are absent

**Inclusion audit: CONFIRMED.** Each member is reproduced and qualifies through **Route A, category 5**. [PLAN p.10, lines 473–488](../../../joi190079supp1_prod.pdf#page=10) specifies HOMA as the primary glycemic measure, separate BMI alternative modeling, and a secondary weight-change analysis accounting for depression-related weight loss. [PLAN p.16, lines 769–772](../../../joi190079supp1_prod.pdf#page=16) separately specifies an Intent-to-Attend treatment-effect comparison. The complete supplied 21-page REPORT union contains no counterpart for these four specified outcome/analysis results. The weight/metabolic outcomes are reported in [the abstract](../../../jama_flint_2019_oi_190079.pdf#page=1), and thus meet the scope's key-secondary definition. These Aim 2 counterparts are distinct from the expressly deferred age/genetic aims on [REPORT p.2](../../../jama_flint_2019_oi_190079.pdf#page=2).

Reported fasting glucose/HbA1c do not identify HOMA. Reported waist does not identify BMI. Descriptive premorbid weight and premorbid-reference adverse-event thresholds do not identify the specified longitudinal secondary weight-change result. Reported pattern-mixture investigation does not identify Intent-to-Attend comparison. [REPORT pp.4–5](../../../jama_flint_2019_oi_190079.pdf#page=4), [secondary results p.7](../../../jama_flint_2019_oi_190079.pdf#page=7), [Table 4 p.8](../../../jama_flint_2019_oi_190079.pdf#page=8), [the complete plot index](../../../joi190079supp2_prod.pdf#page=1), and the recheck's page-by-page 21-page record support the bounded absence comparison. No coefficient or HOMA formula is invented.

Classification audit: explicit PLAN specifications versus REPORT analysis/result record; primary relationship **P_R**; all relationships **P_R**; domain **protocol_report**; evidence state **reproduced**. The [PLAN p.14 exploratory paragraph](../../../joi190079supp1_prod.pdf#page=14) only corroborates insulin resistance's separate identity; it is not a P_P conflict and does not expand this candidate to exploratory nonreporting. The main and supplement agree on result scope and create no S_C conflict. Finding IDs F-XS-002, F-XS-004, F-ST1-002, F-ST1-006 all map to this same repeated absence-of-counterpart pattern. Precedence is satisfied.

Evidence-card audit: all four members, all locations, the full absence record, named affected weight/waist/metabolic results, alternatives and missing outputs are present. No required calculation is possible for absent results; the logical comparison is reproducible and display precision is inapplicable. No unmerged repeated member or unsupported nonperformance assertion was found. Final card must retain all four members and the complete source links, and state absence only from the supplied reporting record. Bounded downstream impact: an extractor could treat reported glucose/HbA1c and weight/metabolic results as a complete prespecified record without identifying the missing counterparts. Whether the analyses were performed elsewhere, deferred, amended, or unavailable is not established.

## C003 — Adverse-event baseline differs between plan and report

**Inclusion audit: CONFIRMED.** The printed eligibility/reference discrepancy is reproduced and meets **Route B**. **B1:** Focus D covers the planned-versus-reported safety event definition. [PLAN p.15, lines 705–717](../../../joi190079supp1_prod.pdf#page=15) explicitly restricts phase-specific adverse-event reporting to participants who did not meet criteria at acute-phase baseline. [REPORT p.4](../../../jama_flint_2019_oi_190079.pdf#page=4) explicitly uses RCT baseline for the UKU increase and for incident Barnes akathisia. **B2:** The epochs precede and follow acute/stabilization treatment; no immediate sentence reconciles their different eligibility/reference rules. **B3:** The specific extracted UKU incidences and incident-akathisia percentages in [REPORT p.7](../../../jama_flint_2019_oi_190079.pdf#page=7) have different possible event/population meanings under the printed rules.

The exact anchor is the PLAN's explicit acute-baseline eligibility exclusion. Its generic UKU phrase “from baseline” does not independently specify the increase-reference epoch. Preserve that distinction in the final card and ledger. The score-4 option alone is context-resolved and does not support this candidate. The reported 4.7%/4.8% akathisia and named UKU frequencies are affected results, not contradictory cross-arm copies. Without participant trajectories or operational denominators, no count reassignment or numeric discrepancy is calculated.

Classification audit: PLAN safety population/event definition versus REPORT safety population/event definition; primary relationship **P_R**; all relationships **P_R**; domain **protocol_report**; evidence state **reproduced**. Main phase descriptions corroborate distinct times and create no S_W. The single INCLUDE finding is F-XS-005. Precedence and content-based roles agree with recheck.

Evidence-card audit: matched statements, affected incidence results, applicable logic, missing trajectories, alternatives and remaining baseline question are present. No source transcription or pagination omission remains. The coordinator completed the wording refinement during this audit: the ledger now anchors the exact acute-baseline exclusion and expressly leaves the epoch of generic “from baseline” unassigned. Retain that boundary in the final card. An intentional randomized-phase emergent-event convention or unprovided amendment is possible. Bounded downstream impact: an extractor could attach the reported percentages to an acute-baseline incident-event population or to an RCT-baseline population; actual changed eligibility or counts are not demonstrated.

## C004 — Safety treatment classification differs from the plan

**Inclusion audit: CONFIRMED.** The printed group-definition question is reproduced and meets **Route B**. **B1:** Focus D includes analysis population/contrast specification. [PLAN p.14, lines 666–667](../../../joi190079supp1_prod.pdf#page=14) and [p.16, lines 766–769](../../../joi190079supp1_prod.pdf#page=16) specify medications-taken safety classification. The eight [REPORT supplement model plots, starting p.2](../../../joi190079supp2_prod.pdf#page=2), explicitly title model means as randomized groups. **B2:** No supplied coding rule maps those model-result labels to medication-taken classification. **B3:** The contrast represented by the eight named headline anthropometric/metabolic model effects could be extracted as assignment-based or exposure-based.

The reported inclusion of all randomized participants alone does not prove model group coding, and Table 4's descriptive n=64/n=62 does not prove it either. The candidate relies on the explicit randomized-group model titles compared with the prospective grouping rule. [Figure 1 p.3](../../../jama_flint_2019_oi_190079.pdf#page=3) confirms treatment departures: 59+5=64, 60+2=62, 3+2=5, 1+1=2. These identities reproduce exactly and are contextual evidence, not a count discrepancy. Do not assume all seven departures would be recoded, that they equal the seven primary-sensitivity exclusions, or that a fixed/time-varying exposure algorithm was applied.

Classification audit: PLAN safety-group rule versus REPORT model-result group definitions/presentation; primary relationship **P_R**; all relationships **P_R**; domain **protocol_report**; evidence state **reproduced**. Both plan passages agree. Main and supplement corroborate the report side; no P_P or S_C conflict is present. The INCLUDE finding is F-ST1-005. Precedence is satisfied. Operational coding, not document role, is the bounded classification ambiguity.

Evidence-card audit: all eight model plots and both prospective repetitions are retained, with treatment departures and affected estimates identified. No unsupported coefficient change is stated. Final card must identify source presentation as the observation and actual coding as the remaining question. All-randomized inclusion is supporting context only. Exposure coding with randomized presentation, exclusion of later observations, or intentional adoption of randomized assignment remain supplied-source-compatible alternatives. Bounded downstream impact: an extractor could label the eight effects as randomized-assignment contrasts without knowing how post-switch observations were handled. Numerical effect changes cannot be established from this package.

## C005 — Planned metabolic observation exclusion is placed in sensitivity analysis

**Inclusion audit: CONFIRMED.** The specification-role discrepancy is reproduced and meets **Route B**. **B1:** Focus D covers principal analysis observation selection and prespecification. [PLAN p.14, lines 673–679](../../../joi190079supp1_prod.pdf#page=14) places exclusion of pertinent later observations after hyperlipidemia-treatment starts/changes within H2 fitting. [REPORT p.5](../../../jama_flint_2019_oi_190079.pdf#page=5) describes statin/hypoglycemic exclusions as post hoc sensitivity. **B2:** The report does not identify whether post hoc describes the entire operation or only the hypoglycemic extension, nor which rule generated the principal estimates. **B3:** A reader could attribute the principal lipid effects to different observation-selection/prespecification rules.

[REPORT p.7](../../../jama_flint_2019_oi_190079.pdf#page=7) reports statin changes in 12 participants (6+6=12), hypoglycemic changes in three (2+1=3), and qualitative sensitivity similarity. These exact count identities reproduce. “All participants” does not mean all later observations: a participant can remain represented by earlier values. No principal-versus-sensitivity coefficient pair is supplied; no numerical difference or rounding calculation is possible. The planned hyperlipidemia rule is not expanded into an asserted planned hypoglycemic rule.

Classification audit: PLAN H2 observation-selection rule versus REPORT sensitivity specification/results; primary relationship **P_R**; all relationships **P_R**; domain **protocol_report**; evidence state **reproduced**. Agreeing abstract/body coefficients are affected results and add no S_W. F-XS-003 and F-ST1-004 are both INCLUDE and map to this candidate. Unlike C002, a counterpart operation is reported; the issue is its analysis role. Precedence is satisfied.

Evidence-card audit: source placements, named lipid effects, count context, alternatives, missing observation rule/output and the remaining question are present. The initial cross-source Route A designation is superseded by independently screened Route B and the ledger/recheck agree on Route B; source observations are preserved. Keep the alternative that the planned statin exclusion remained in the principal model and post hoc referred only to hypoglycemic expansion. Bounded downstream impact: an extractor could label the principal cholesterol/triglyceride estimates with an unresolved observation-selection or prespecification convention. No demonstrated coefficient or conclusion change is supported.

## Every screening decision audited

Each of the 13 finding IDs has exactly one screening-table row. All 10 INCLUDE rows map to the five ledger IDs; all ledger finding-ID fields include exactly their screened finding sets. The three SCREENED_OUT rows use one permissible reason code each and no candidate ID. No qualifying route A observation is screened out. Pass 2 emits no finding IDs, so there is no omitted pass-2 screening row. Its re-evaluations are audit coverage records rather than duplicate checker findings.

| Finding ID | Screening decision audit | Candidate / threshold reason |
|---|---|---|
| F-NUM-101 | SCREENED_OUT / PERIPHERAL_COMPARISON stands | Cross-location 82/site versus 98/site recruitment projections differ beyond precision, but the randomized target remains explicitly 176; no changed analysis-population count or power decision follows. This is neither a same-display count/denominator/percentage conflict nor an identified digit/sign slip changing a primary/key secondary reading. |
| F-NUM-102 | SCREENED_OUT / PERIPHERAL_COMPARISON stands | Historical 35% denominator wording is different, but the current power table explicitly chooses participant risks 35% and 15%. No current power input is left unidentified; historical counts needed for conversion are absent. |
| F-XS-001 | INCLUDE confirmed | C001; Route A category 5. |
| F-XS-002 | INCLUDE confirmed | C002 HOMA member; Route A category 5. |
| F-XS-003 | INCLUDE confirmed | C005; Route B, principal-versus-sensitivity specification role. |
| F-XS-004 | INCLUDE confirmed | C002 BMI/weight-loss/Intent-to-Attend members; Route A category 5. |
| F-XS-005 | INCLUDE confirmed | C003; Route B, explicit acute versus RCT baseline rules. |
| F-ST1-001 | INCLUDE confirmed | C001; Route A category 5, narrowed to the additional 5-point requirement. |
| F-ST1-002 | INCLUDE confirmed | C002 HOMA member; Route A category 5. |
| F-ST1-003 | SCREENED_OUT / PERIPHERAL_COMPARISON stands | H3 open-label age×weight is neither in the abstract nor designated key secondary; the article expressly excludes those additional aims. Route A category 5's primary/key-secondary nonreporting rule does not apply. |
| F-ST1-004 | INCLUDE confirmed | C005; Route B. |
| F-ST1-005 | INCLUDE confirmed | C004; Route B, model-result labels versus prospective medication grouping. |
| F-ST1-006 | INCLUDE confirmed | C002 repeated absent-counterpart members; Route A category 5. |

For F-NUM-101, intervals [81.5,82.5] and [97.5,98.5] leave gap 15; 15/98=0.153061. Four-site reconstruction [326,330] versus printed [391.5,392.5] leaves 61.5/392=0.156888. These are not screened as rounding. The PLAN separately predicts 60% remission and budgets conservatively for 50%; do not assume either is the unprinted explanation for 82. F-NUM-102's two displayed 35% intervals overlap; the different historical denominator reading is logical, not a computable numeric gap. No universal exclusion of plan discrepancies is used: each decision is bounded to the cited current input/result/decision-rule test.

## Every checker exclusion and pass-2 revisit audited

Row labels below identify table positions only and are not finding IDs. NUM 1–8 are main numeric exclusions; NUM 9–13 are support numeric exclusions. XS 1–9 and ST1 1–15 identify their respective tables. Every corresponding pass-2 revisit was checked; each addresses the same source observation and preserves a single stated reason code. No exclusion requires F-QA registration.

| Prior row | Independent threshold audit | Decision / one reason code |
|---|---|---|
| NUM 1 | Hyperlipidemia count/percentage intervals overlap; no category 3 discrepancy survives the exact scope precision rule. | Retain / ROUNDING_OR_DISPLAY_PRECISION |
| NUM 2 | Living-arrangement count sum and denominator intervals touch; exact 2/62 is also below .05. | Retain / ROUNDING_OR_DISPLAY_PRECISION |
| NUM 3 | Race percentages sum to 100.1 from independent rounding; interval sum includes 100 and exact counts sum to 64. | Retain / ROUNDING_OR_DISPLAY_PRECISION |
| NUM 4 | DKEFS row title and footnote h supply its intended scaled-score quantity; superscript mismatch changes no printed number. No route A numeric slip. | Retain / NOTATION_OR_TYPOGRAPHY |
| NUM 5 | Full SAS versus head-dropping-excluded SAS and AIMS item versus global score are distinct quantities; no matched source contradiction. | Retain / NOT_REPRODUCED |
| NUM 6 | UKU score-4 alternative is redundant beside attainable score 3; no changed printed event percentage or usable threshold is demonstrated. This does not resolve the separately included baseline candidate. | Retain / CONTEXT_RESOLVES |
| NUM 7 | NNT 2.8 versus crude inverse RD leaves at most .01655 relative fixed-count gap, and full input rounding intervals overlap. Model/crude distinction also remains. | Retain / ROUNDING_OR_DISPLAY_PRECISION |
| NUM 8 | Marginal summaries need not reconstruct paired changes; explicit missingness footnote and median nonadditivity resolve all 16 rows. No method reproduces neighboring rows while failing one. | Retain / CONTEXT_RESOLVES |
| NUM 9 | Prior-study longitudinal OR and last-assessment percentages differ in method/time; no source crude label. | Retain / MODEL_VERSUS_CRUDE |
| NUM 10 | Historical week-6 implied totals differ within .05; required interval calculation below independently reproduces. | Retain / ROUNDING_OR_DISPLAY_PRECISION |
| NUM 11 | General 5 mg minimum and EPSE-specific 10 mg reduction refer to separate permitted maneuvers. | Retain / CONTEXT_RESOLVES |
| NUM 12 | Standard 20 weeks and conditional 22-week extension are expressly different allowed pathways. | Retain / CONTEXT_RESOLVES |
| NUM 13 | Exact source inclusive eligibility glyphs agree with REPORT; greater-than locator text is derivative-only. | Retain / NOT_REPRODUCED |
| XS 1 | Same source-inclusive/locator-strict threshold observation as NUM 13; no printed-source conflict. | Retain / NOT_REPRODUCED |
| XS 2 | Additional H3/age/genetic aims are outside article Aims 1–2; not a hidden primary/key-secondary counterpart. | Retain / OUT_OF_FOCUS |
| XS 3 | Analytic section expressly conditions extra Cox covariates on imbalance and correlation; no source fact establishes those conditions triggered. | Retain / CONTEXT_RESOLVES |
| XS 4 | Omitted MMSE exception/extension permissions do not constitute a printed prohibition, applied conflict, or altered analysis count. | Retain / CONDITIONAL_OR_UNREPORTED |
| XS 5 | Disclosed post hoc Holm adjustment and exploratory interpretation retain secondary outcome labels; no outcome-status reassignment or unreconciled inferential decision is printed. | Retain / CONTEXT_RESOLVES |
| XS 6 | HbA1c percentage quantity is evident from table/plot and source values; mg/dL label changes no printed number or numeric conversion. | Retain / NOTATION_OR_TYPOGRAPHY |
| XS 7 | Raw marginal summaries and model least-square trajectories are different estimands, including nonlinear glucose trajectories. | Retain / MODEL_VERSUS_CRUDE |
| XS 8 | Same cross-location recruitment projection as screened F-NUM-101; >.05 gap does not turn it into same-display category 3. | Retain / PERIPHERAL_COMPARISON |
| XS 9 | One-minute orthostatic measurement versus within-three-minute definition does not establish an applied primary/key-secondary result or analysis-population change. | Retain / PERIPHERAL_COMPARISON |
| ST1 1 | Same evident HbA1c percentage unit as XS 6; no independent numeric slip. | Retain / NOTATION_OR_TYPOGRAPHY |
| ST1 2 | Same marginal-versus-paired change observation as NUM 8; explicit source footnote resolves it. | Retain / CONTEXT_RESOLVES |
| ST1 3 | HR-based NNT is not crude inverse RD; no >.05 discrepancy and no time-specific survival mapping supplied. | Retain / MODEL_VERSUS_CRUDE |
| ST1 4 | Adjusted Cox HR .25 and crude risk ratio .3704 measure different quantities; censoring/covariates are explicit. | Retain / MODEL_VERSUS_CRUDE |
| ST1 5 | Secondary intervals and adjusted P decisions agree. Unadjusted normal-CI approximations do not reproduce an exact adjusted test; no category 1 incompatibility is established. | Retain / CONDITIONAL_OR_UNREPORTED |
| ST1 6 | Ordinary Wald CI does not reproduce the other sparse-event rows, expressly exact; no P/null conflict and no qualifying same-display method reproduction. | Retain / CONDITIONAL_OR_UNREPORTED |
| ST1 7 | Unprinted event/censor generators and mixed covariance prevent exact simulation recreation; no stated reproducing method establishes a >.05 result discrepancy. | Retain / CONDITIONAL_OR_UNREPORTED |
| ST1 8 | Same explicitly conditional Cox-covariate criterion as XS 3; no trigger established. | Retain / CONTEXT_RESOLVES |
| ST1 9 | Same exact inclusive eligibility glyphs as NUM 13 and XS 1; no supplied-source mismatch. | Retain / NOT_REPRODUCED |
| ST1 10 | Exploratory age/genetic/PK results are expressly outside article scope; no key-secondary status change. | Retain / PERIPHERAL_COMPARISON |
| ST1 11 | Unspecified shading level/type and absent numeric coordinates do not reproduce a printed interval/test conflict. | Retain / CONDITIONAL_OR_UNREPORTED |
| ST1 12 | Poisson/SAS link and back-transformation are unprinted; no supported method reproduces another matching row. Curve diagnostics alone cannot establish raw-points versus link-scale identity. | Retain / CONDITIONAL_OR_UNREPORTED |
| ST1 13 | Benztropine use and triggered covariate comparison are unprinted; non-key EPSE implementation detail is not planned primary/key-secondary nonreporting. | Retain / CONDITIONAL_OR_UNREPORTED |
| ST1 14 | Unprinted descriptive dose changes supply no actual prohibited increase or fixed-dose result contradiction. | Retain / CONDITIONAL_OR_UNREPORTED |
| ST1 15 | Different PH diagnostic descriptions supply no contradictory statistic or reported assumption; missing diagnostic detail alone is insufficient. | Retain / CONDITIONAL_OR_UNREPORTED |

## Independent display-precision calculations

Every exclusion coded ROUNDING_OR_DISPLAY_PRECISION is covered below, including the identical pass-2 revisit. Category 1 interval-versus-P/test discrepancies never use this rule. None is present in these exclusions. No stable candidate rests on a very small P value displayed as zero.

| Exclusion | Recomputed interval and printed interval | Gap and relative discrepancy |
|---|---|---|
| NUM 1, olanzapine hyperlipidemia | 100×[17.5,18.5]/[63.5,64.5]=[27.131783,29.133858]%; printed 29.0 gives [28.95,29.05]%. | Overlap; gap 0; relative 0. |
| NUM 1, placebo hyperlipidemia | 100×[18.5,19.5]/[61.5,62.5]=[29.600000,31.707317]%; printed 29.7 gives [29.65,29.75]%. | Overlap; gap 0; relative 0. |
| NUM 2, living arrangements | [48.5,49.5]+[9.5,10.5]+[0.5,1.5]=[58.5,61.5]; printed 62 gives [61.5,62.5]. | Touch; gap 0; relative 0. Even exact-count difference 2/62=.032258≤.05. |
| NUM 3, race total | [84.35,84.45]+[9.35,9.45]+[6.25,6.35]=[99.95,100.25]%. | Contains exact 100%; gap 0; relative 0. Counts 54+6+4=64. |
| NUM 7, NNT | RD input intervals: [33.5/62.5−13.5/63.5,34.5/61.5−12.5/64.5]=[.323401575,.367177160]; inverse gives [2.723480947,3.092130892]. Printed 2.8 gives [2.75,2.85]. | Overlap; gap 0; relative 0. Fixed-count inverse RD=2.896350365 leaves (.046350365)/2.8=.016553702≤.05. |
| NUM 10, PLAN Table 5 week 6 | With exact printed group counts, race: 12×[.7495,.7505]+29×[.7585,.7595]+218×[.7475,.7485]=[193.9455,194.2045]. Ethnicity: 30×[.7995,.8005]+229×[.7375,.7385]=[192.8725,193.1315]. Count half-unit intervals widen these bounds. | Conservative gap .8140; relative .8140/194.075=.004194255≤.05. The one-person integer difference gives 1/194=.005154639≤.05. |

Arithmetic was independently recomputed using direct interval operations. The PLAN Table 5 denominators/percentages are printed on [PDF p.29](../../../joi190079supp1_prod.pdf#page=29); the main counts are on [Table 1 PDF p.5](../../../jama_flint_2019_oi_190079.pdf#page=5), and NNT/events on [PDF p.7](../../../jama_flint_2019_oi_190079.pdf#page=7). F-NUM-101 and XS 8 are >.05 comparisons screened for a separate scope reason, not rounding exclusions. No hidden >.05 rounding exclusion was identified.

## Repair register and final-card requirements

Only the coordinator owns the canonical ledger/screening/report. This part does not modify them. No stable ID is deleted, merged, ranked, or suppressed; the already consolidated repeated patterns retain every affected location.

| Repair / carry-forward | IDs / location | Concrete reason |
|---|---|---|
| Set Inclusion audit to CONFIRMED | C001, C002, C003, C004, C005 classification-table cells currently PENDING_AUDIT | This fresh source-based audit closes the provisional audit field; all five independently meet a qualifying route. |
| Completed by coordinator: use the explicit acute-baseline exclusion as the PLAN anchor | C003 ledger source reasoning; retain in final card | Generic PLAN “from baseline” does not name an epoch. The exact definite eligibility statement supports the candidate without that additional assumption; updated ledger was reread during this audit. |
| Retain narrowed endpoint basis | C001 final card | Hospitalization causes reconcile and psychosis wording is operational context; the independently reproduced extra 5-point condition is sufficient. |
| Completed by coordinator: identify randomized-group titles as direct evidence and actual coding as the question | C004 ledger source reasoning; retain in final card | All-randomized inclusion and descriptive n alone do not prove the design matrix or exposure coding; updated ledger was reread during this audit. |
| Completed by coordinator: retain all-participants/all-observations distinction and hypoglycemic-extension alternative | C005 ledger source reasoning; retain in final card | The supplied report does not establish inclusion of every later observation, and post hoc may refer only to expansion of the retained planned statin rule; updated ledger was reread during this audit. |
| Rebase source hyperlinks on merge | This part to canonical quality artifact | Part and canonical directory depths differ by one level; preserve truthful source file/page links. |
| Fill report-specific fields from existing supported material | All five final cards | Ledger is a registration record, not the final report-card format. Add the exact mandatory labels for mechanical recheck, reasoning, calculation, classification, source comparisons, and bounded downstream impact; do not invent new facts. |

No evidence-card source value, classification code, review domain, evidence state, source page, arithmetic, or finding provenance requires a factual change. All five recheck records separately contain every required mechanical field, including missing definitions and alternatives. The evidence states concern reproduced printed specifications or supplied-record absence, not demonstrated actual implementation or numerical impact.

Final report had not yet been assembled when this assigned audit part was completed. Therefore equality of actual final-card classification fields with the ledger is a completion dependency for the coordinator's assembly audit and validator, not a claim made here. Expected values for every ID are primary/all relationship P_R, domain protocol_report, evidence state reproduced, and Inclusion audit CONFIRMED; compared-role text and finding-ID sets must be copied exactly from the finalized ledger. All five must appear in the canonical quality artifact.

## Limitations and compact status

Inclusion/classification/screening/exclusion coverage: COMPLETE for this assigned shard. Covered stable IDs: C001, C002, C003, C004, C005. Inclusion counts: CONFIRMED 5; QUESTIONED 0. Screening: 13 decisions audited, 10 INCLUDE and 3 SCREENED_OUT; 0 reversals; 0 new findings. Exclusions: 37 initial rows and 37 pass-2 revisits audited. Recheck: every stable ID present, all reproduced. Neutral wording: no prohibited description was found in the examined ledger, screening log, recheck or checker artifacts; this part uses no such description and assigns no severity or scientific disposition.

Remaining evidence limitations are unavailable operational endpoint instructions/amendments, four missing counterpart outputs, participant trajectories and incidence denominators, safety group-coding matrices and exposure handling, and principal/sensitivity observation sets and coefficients. These bound the human questions; they do not create scientific source-unit gaps or authorize inferred conclusion changes. Final-report equality, full source/relationship/manifest coverage, final link resolution and unchanged integrity hashes are coordinator/coverage-audit completion checks.
# Coverage and execution audit part — Workflow 1.6.2

Fresh audit runtime: `root/quality_coverage_audit`, gpt-6.1-sol/high, FRESH_SPAWN. This disjoint part audits source coverage, quantitative maps, relationship coverage, reuse fitness and integrity, routing, tooling, and process records. Candidate inclusion, classification, evidence-card support, every screening decision and every checker excluded observation are assigned to `quality/parts/inclusion_classification_audit.md`; this part makes no candidate inclusion decision. The coordinator must merge both parts into `quality/evidence_quality_audit.md` without losing any stable ID.

## Coverage result

Scientific source and relationship coverage is complete. Recursive source enumeration finds exactly four supplied PDFs and no Office, workbook or CSV source. Direct `pdfinfo` independently confirms the page counts. Explicit page applicability ledgers cover every unit, including administrative and bibliography pages; these pages have a recorded applicability decision rather than an omitted mapping assignment.

| Source | Role by content | Total | Reusable | Fresh-required | Mapped | Audit result |
|---|---|---:|---:|---:|---:|---|
| DOC-001, jama_flint_2019_oi_190079.pdf | REPORT: trial article | 10 | 10 | 0 | 10 | Complete pp. 1–10 |
| DOC-002, joi190079supp1_prod.pdf | PLAN: protocol, analytic plan and pharmacotherapy appendix | 42 | 42 | 0 | 42 | Complete pp. 1–21 and disjoint pp. 22–42 |
| DOC-003, joi190079supp2_prod.pdf | REPORT: results supplement | 10 | 10 | 0 | 10 | Contents page and all nine plot pages |
| DOC-004, joi190079supp3_prod.pdf | REPORT: non-plan data-sharing statement | 1 | 1 | 0 | 1 | Administrative applicability recorded |
| Total | Four direct sources | 63 | 63 | 0 | 63 | All partitions and mapped totals close |

For each source, reusable plus fresh-required units equal total units, and mapped units equal total units. Zero fresh-required units reflects usable source-matched existing assets; every page nevertheless received fresh scientific relationship mapping. Sparse plot text is backed by complete source-matched images. Missing reusable page images elsewhere are derivative gaps closed by usable text and targeted exact-source renders, without a scientific gap.

Main mapping covers all five article tables, both figures, abstract, Key Points, narrative, captions and footnotes. The complete records retain all Table 4 arm rows, all four Table 5 contrasts, participant-flow arithmetic, risk-set sequences and outcome-specific units. Support mapping covers the complete plan schedule and footnotes, six survival-power rows, six repeated-measure-power rows, historical Table 5, the complete blinded-switch table, outcome hierarchy, analysis population, model/covariate and missingness specifications, all appendix pages, all nine result plots and the administrative data statement. Historical quantities and bibliography identifiers are identified by their actual content and are kept distinct from this trial's results.

## Relationship closure

| Relationship scope | Mapped records | Inventory records | Completion result |
|---|---:|---:|---|
| N001–N079, main article | 79 | 79 | Every ID has a numeric check record |
| N111–N132, plan core | 22 | 22 | Every ID has a numeric check record |
| N211–N236, plan appendix | 26 | 26 | Every ID has a numeric check record |
| All numeric relationships | 127 | 127 | Exact set agreement; no duplicate, missing or extra ID |
| S001–S039, main article | 39 | 39 | Both statistical passes complete |
| S040–S057, plan core | 18 | 18 | Both statistical passes complete |
| S058–S066, nine result plots | 9 | 9 | Both statistical passes complete |
| S081–S084, plan appendix | 4 | 4 | Both statistical passes complete |
| All statistical relationships | 70 | 70 | Exact set agreement; no duplicate, missing or extra ID |

Each statistical checker has exactly 70 per-ID completion rows. Their ID sets equal the inventory set, and every canonical inventory row records both `PASS_1_COMPLETE` and `PASS_2_COMPLETE`. The gaps between allocated ID blocks preserve disjoint mapper assignments and do not represent missing registered relationships. Table 4 numeric inputs are cross-referenced to S017–S032; all four Table 5 inferential contrasts are explicitly covered under S038 rather than omitted because they lack separate S IDs.

The cross-source comparison coverage includes population, phase, time, contrast, model, scale and precision matching; primary abstract/body/flow agreement; all eight metabolic model results and their supplementary plots; raw within-arm versus model-estimated distinctions; eligibility, relapse composite, intervention, covariates, power, missingness and planned analysis comparisons; and historical or administrative applicability. Both statistical passes cover the complete registered relationship set rather than only findings or stable candidates. Candidate-specific interpretations and excluded-observation decisions are audited in the other assigned part.

## Reuse, preservation and reproducibility

The asset inventory contains 194 distinct paths: 171 USABLE, 22 PARTIAL and one DUPLICATE. Every listed path occurs exactly once in `reused_artifact_hashes_before.sha256`, and every hashed reused path occurs in the inventory. USABLE assets independently span DOC-001 pp. 1–10, DOC-002 pp. 1–42, DOC-003 pp. 1–10 and DOC-004 p. 1. PARTIAL plot text is paired with USABLE images; the single duplicate does not inflate page coverage. No STALE or UNREADABLE asset is recorded. Potentially mixed legacy response wrappers are inventoried by path only and were not reused as scientific conclusions. Legacy scope restrictions do not control source coverage.

Local `sha256sum -c` checks reproduce all four direct-source hashes and all 194 reused-asset hashes without a mismatch. This is an audit-time preservation check; the coordinator must still produce final after-hash manifests at completion. New derivatives remain separate from reused assets. Engine provenance distinguishes historical PyMuPDF/OCR assets from current direct Poppler CPU derivatives. Unspecified historical image engines remain documented and do not replace supplied-source authority.

Mechanical inspection of 139 PDF evidence links in the canonical maps, numeric/statistical inventories and cross-source checker resolves each relative filename to one of the four supplied PDFs and confirms that every `#page=N` is within its actual page count. No Office source is assigned fictitious pagination. Numeric records supply count/denominator arithmetic and half-unit precision intervals; statistical diagnostics state their inputs and limits. Model-based estimates, marginal summaries, paired changes, survival curves and crude ratios retain their distinct quantities. Named unavailable inputs are not invented to claim exact test or model recreation.

## Execution and discovery controls

Routing preflight is PASS, with run model gpt-6.1-sol, source DEFAULT, coordinator/high, ordinary specialists/medium, statistical and screening/recheck/audit specialists/high, Coordinator inference PASS, INTERACTIVE_CLI and Provider CURRENT_SESSION. Direct inspection confirms the project coordinator pair and all ten named agent-preset pairs. No moving model alias or provider change is recorded.

The current execution manifest contains the coordinator exactly once and 13 distinct specialist runtime IDs, including every optional shard already invoked. All specialist rows record FRESH_SPAWN and the required model/effort class. Available collaboration-service records agree with the canonical task-name IDs for the current audit, statistical pass 2, screen and recheck agents. Earlier completed stages retain their recorded runtime provenance; the service exposes canonical task names rather than a separate UUID in this session.

Statistical pass 1 is `root/statistics_pass_one`; statistical pass 2 is `root/statistics_pass_two`. Both are distinct fresh gpt-6.1-sol/high agents and differ from `root/initial_inclusion_screen`, the fresh high-effort inclusion screener. Pass 2 was performed after the full ledger, screening and mechanical recheck existed. It records no new finding, so a pass-2 inclusion-screener stage is not applicable. Both audit shards are additional fresh high-effort agents. The report generator is a later dependent stage and must be added when it is spawned.

The scientific maps and inventories document complete discovery from supplied-source evidence and eligible locators, excluding old scientific conclusions. The pre-mapping manifest defines full source coverage; relationship inventories are exhaustive and disjoint. No discovery or screening count target, top-N selection, candidate cap, comparison with other papers or calibration to earlier candidate sets is evidenced. The 25–40 minute value in `run_state.md` is solely a package-specific elapsed-time planning range, with a bounded basis covering reuse, plots, plan/report matching and mandatory agent waves; it is not a finding target or early-stopping rule.

All 26 coverage rows have exactly one undecorated relative artifact path. The 22 completed upstream rows resolve to existing artifacts. Candidate registration and recheck enumerate C001, C002, C003, C004 and C005; both statistical passes enumerate all 70 S IDs. At this audit checkpoint, the two current audit rows are ASSIGNED, the canonical audit is PENDING_MERGE and report generation is PLANNED. These sequentially dependent rows must be closed by the coordinator after their artifacts exist; they are not source or relationship coverage gaps.

Tooling records CPU, all needed direct tools available, fallback NOT_NEEDED and removal NOT_CREATED. No fallback environment exists. Current artifacts document no new OCR or GPU processing. Historical GPU provenance is explicitly historical. No source or reused artifact was modified by this audit, and no web or external literature was used.

## Repairs and completion conditions

| Repair | Reason | Status |
|---|---|---|
| Support handoff statistical block changed from S031–S066 to S040–S066, retaining 27 records | The former text overlapped main IDs and disagreed with the complete final routed set | Coordinator repair confirmed in part and canonical map |
| Numeric support provenance now calls >2/>21 historical pre-correction map readings and identifies the current ≥2/≥21 annotation | Present-tense wording no longer matched the source-confirmed current map; literal extraction and reused assets remain preserved | Coordinator repair confirmed in canonical inventory and assigned support artifacts |
| Execution-manifest blank line removed before statistical pass 2 | All runtime rows must remain in one contiguous Markdown table | Coordinator repair confirmed |
| Appendix page-render filename aligned to p41.png | The new-derivative inventory named page41.png while the mapper and actual output name p41.png | Coordinator repair confirmed in the evidence-asset inventory |

No scientific source-unit or relationship repair is required. No candidate registration or screening repair originates from this coverage part. Final report assembly, report-card/ledger agreement, canonical audit merge, inclusion-audit values, timing finalization, after-hash manifests, standalone HTML and the final validator remain dependent completion checks. A report-generator runtime and its completed coverage row must be present before final completion. Update the two audit-part rows and canonical merge row only after their durable outputs are complete.

Reconstruction limits are supplied-source limits: exact plot coordinates and shaded-band definitions; paired participant data and some Table 4 baseline contributor cells; survival event/censor times and fitted-model outputs; mixed/Poisson covariance, degrees of freedom, link/back-transformation and exact contrasts; full simulation generators and replication counts; operational endpoint/treatment/observation coding; unreported analysis outputs and undisclosed amendments. These limits are bounded, named in the evidence artifacts and leave no source unit unreviewed. No severity or scientific disposition is assigned. All stable candidates remain Pending Human Adjudication.

Neutral-language scan of all current generated Markdown artifacts found none of the prohibited descriptive terms. Candidate-card inclusion, impact wording and repeated-pattern support remain covered by the independent inclusion/classification audit part and must be preserved in the canonical merge.
