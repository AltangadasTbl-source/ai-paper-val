# Independent evidence quality-control audit — Workflow 1.6.2

Fresh mandatory auditor runtime: root/quality_auditor; model gpt-6.1-sol; reasoning effort high. All candidates remain Pending Human Adjudication. This audit preserves C001, C002, C003, C004 and C005 and every included provenance finding. It does not assign a scientific disposition.

The complete scope, review contract and tooling record were read. Inputs are the current-run source/evidence inventories, complete page maps and relationship inventories, numeric/cross-source/statistical checker artifacts and bounded assessment parts, independent screening log, candidate ledger, mechanical recheck, source coverage and execution manifest. No historical candidate selection, classification, screening decision or final report was consulted. The supplied sources and all reusable assets are preserved. There is no count target or comparison with another paper or earlier run.

## C001 — Missing stratification-only primary-outcome analysis

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN final protocol vs REPORT main article

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-001, F-ST1-002

The exact final protocol [PDF p70, §4.2.2](../../../joi250042supp1_prod_1753377747.92525.pdf#page=70), independently read as a complete source-linked image in this audit, retains both a stratification-only analysis and a fully adjusted primary-outcome analysis. The original protocol p30 is a repeated occurrence, not the sole basis. The main [p3 methods](../../../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=3) and [p8 Table 2 and footnotes](../../../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=8) identify additional baseline adjustment in both available-case and imputed columns. The recheck also confirms main p6's separately labeled unadjusted RD. Neither an unadjusted contrast nor a change in missing-data handling supplies the site/diagnosis-only adjusted estimate. Complete maps cover both supplied REPORT documents, with no matching companion estimate.

Reproduced and qualifying by **Route A, category 5**: a retained planned analysis of the primary outcome is not reported in the supplied results. Category 5 does not require an inferred effect-size change. The named affected extraction is the planned companion 90-day mortality contrast; no missing estimate is invented. The later SAP's detailed fully adjusted model is a source-grounded possible supersession, explicitly retained as an alternative; an explicit cancellation is absent. This ambiguity is appropriate for human review and does not remove the category-5 observation. Display precision is inapplicable to adjustment-set membership or the absence of a specified analysis.

Roles, P_R, protocol_report and reproduced agree between ledger table/card and recheck. The SAP merely supports the implemented fully adjusted model; no separate P_P relationship is asserted here. Card evidence fields, bounded absence scope, alternative interpretation and human question are present. No calculation, pagination or impact repair is needed.

## C002 — Retained protocol stay test versus SAP/report stay method

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN final protocol vs PLAN final SAP and REPORT main article

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-004, F-ST1-004

The final protocol [pp70–71](../../../joi250042supp1_prod_1753377747.92525.pdf#page=70) retains Wilcoxon rank-sum comparisons stratified by survival. The exact p70 image was independently read in this audit; the full continuation, original repetition and both SAP statements were mechanically source-confirmed in the recheck. Final SAP [p128](../../../joi250042supp1_prod_1753377747.92525.pdf#page=128) and REPORT [main p3](../../../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=3) instead identify Fine–Gray competing-risk regression, consistent with Table 2's ICU sHR 1.00 (0.96–1.04), P=.97, and hospital sHR 0.98 (0.94–1.02), P=.27. Those printed intervals and P values themselves reconcile.

Reproduced and qualifying by **Route B**. B1: explicit planned-versus-reported model/test specification is focus D. B2: the final protocol and final SAP retain distinct procedures without an explicit replacement/addition statement; immediate context does not settle the status of the protocol test. B3: the issue changes the prospective analysis specification attached to the named ICU/hospital contrasts and whether the reported sHRs replace a retained comparison. The implemented report method is clear; the card does not suggest that the sHR was computed by a Wilcoxon test. A later detailed SAP intentionally superseding protocol shorthand is a plausible, bounded alternative, not an established fact in these sources.

The final protocol versus REPORT comparison supplies P_R; final protocol versus final SAP supplies P_P; SAP/report agreement adds no relationship. P_R precedence and protocol_report are consistent. The final versions, original repeated locations, missing counterpart scope, alternatives and human question are retained. No unsupported method-suitability judgment, test-significance conflict or numerical downstream effect is claimed. No card repair is needed.

## C003 — SAP all-outcome MICE versus reported predictors and stay censoring

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, S_C

**Compared document roles:** PLAN final SAP vs REPORT main article and REPORT results supplement

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-003, F-ST1-003

The complete final SAP [p132, §7](../../../joi250042supp1_prod_1753377747.92525.pdf#page=132), REPORT [main p3 imputation paragraph](../../../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=3), [main p8 Table 2](../../../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=8), and [results p24 eTable 7](../../../joi250042supp2_prod_1753377747.93025.pdf#page=24) were independently read as source-linked full-page images. The SAP explicitly includes all adjusted baseline variables and all outcome variables in each MICE model; the supplemental auxiliary column lists selected outcome variables or None. Its footnote separately lists baseline variables and treatment assignment. Missing duration rows instead specify Censoring, auxiliaries N/A. Main Table 2 explicitly excepts stay durations from multiple imputation. Main p3 says at least the primary outcome supports imputation of secondary outcomes, while the one-year supplemental row lists auxiliary variables None.

Reproduced and qualifying by **Route B**. B1: explicit imputation predictor membership and imputation-versus-censoring specifications are focus D. B2: neither the general all-outcome specification nor the selected/None lists and duration exception explicitly explains their relationship. Baseline variables alone do not supply an omitted outcome variable. B3: the unresolved specification attaches to named imputed mortality/organ-support effects, including one-year RD 3.3 (−0.7–7.3), and the ICU/hospital sHR analyses. It concerns reproducible analysis definitions; no numerical effect of using another predictor set or procedure is inferred.

The auxiliary column might list only additions to an unprinted predictor mechanism; main p3 might describe incorporation across the imputation exercise rather than in every model. Both alternatives remain explicit in the ledger and recheck. They limit the strength of the companion S_C reading, but do not resolve the explicit P_R specification difference. Retain P_R, S_C with that ambiguity; P_R precedence selects protocol_report. This is one missing-data specification pattern covering all affected outcome rows, including the narrower duration manifestation of F-XS-003. It is distinct from C004's conflicting operational censoring time.

The p132 source prints five datasets with 1000 bootstrap replications as a computational alternative. The prior current-run locator value 100 was corrected before registration; it is not a source issue and does not require the evidence state reproduced_after_transcription_correction. The current card and recheck contain 1000. No card/classification repair is needed. Final reporting must preserve the nonuniversal-main-sentence alternative and avoid asserting a known effect-size change or known implemented predictor matrix.

## C004 — Hospital missing-duration censoring at one hour versus one day

**Review domain:** statistical_results

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT main article vs REPORT results supplement

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-002, F-ST1-001

The exact REPORT [main p8 footnote b](../../../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=8) specifies 1 hour for missing discharge times for both ICU and acute-hospital duration. The REPORT [results p24 footnote e](../../../joi250042supp2_prod_1753377747.93025.pdf#page=24) specifies 1 hour for ICU but 1 day for hospital duration and lists 1677 (10.2%) missing hospital durations. Both complete images were independently read in this audit. The conflict concerns the same hospital-duration analysis, not the two different endpoints.

Reproduced and qualifying by **Route B**. B1: conflicting explicit censoring times are statistical method logic within C. B2: endpoint attribution and identical displayed sHRs do not identify which hospital cutoff generated the analysis. B3: the named hospital sHR 0.98 (0.94–1.02), P=.27, has an unresolved missing-data censoring definition for extraction/reproduction. One day equals 24 hours; exact operational gap is 23 hours. Conservative half-unit display intervals [0.5,1.5] hours versus [0.5,1.5] days=[12,36] hours give minimum gap 10.5 hours, divided by the main printed 1 hour=10.5, greater than .05. The arithmetic reproduces; the card distinguishes operational cutoffs from this precision sensitivity.

Both conflicting documents are REPORT by content; S_C and statistical_results follow. The SAP/MICE comparison is contained in C003 and is not an extra P_R relationship in this card. A generalized main footnote or a supplemental implementation distinction are alternatives, without any claimed change in sHR magnitude or significance. Exact timestamps/code remain unavailable. No card repair is needed.

## C005 — Pilot adherence numerator and progression direction

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN original SAP vs PLAN final SAP and PLAN final protocol

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-001

The original SAP [p95 Table 1/footnote](../../../joi250042supp1_prod_1753377747.92525.pdf#page=95), its patient-level adherence definition [p98](../../../joi250042supp1_prod_1753377747.92525.pdf#page=98), and repeated final SAP [p118](../../../joi250042supp1_prod_1753377747.92525.pdf#page=118) were independently read as complete images. Both table footnotes use conservative-group patients with one or more adjudicated deviations under the high-is-Green adherence row. Original p98 explicitly defines adherence as no deviation. The recheck also confirms final protocol p69's adherence definition and the funder/TSC-qualified prospective decision consequences at pp70/96/119.

Reproduced and qualifying by **Route B**. B1: a planned decision rule and quantity-changing event membership are within D/C. B2: the progression footnote explicitly ties the deviation numerator to the percentage in the threshold table; it cannot be resolved solely by knowing that adherence usually means compliance. B3: a data extractor applying the printed prospective progression rule obtains complementary numerator definitions and potentially different traffic-light classifications. For the matched conservative population, d=the fraction with at least one adjudicated deviation and a=the fraction with none, hence a=1−d. Green d≥.75 implies a≤.25, rather than adherence Green a≥.75; Red d<.50 implies a>.50. Illustrative a=.80/d=.20 is Green using adherence but Red using the footnote numerator. This is algebra, not an observed pilot decision.

Display precision cannot reconcile complementary event membership. The recheck's optional boundary sensitivity gives [74.5%,75.5%] versus [24.5%,25.5%], gap49 percentage points/75≈.653>.05; it is clearly illustrative and does not claim the exact decision thresholds were measured/rounded. Equality conventions at 75% are a separate excluded observation. PLAN-versus-PLAN content supplies P_P/plan_material. Final protocol corroborates the no-deviation side; no REPORT relationship is added. All repeated occurrences are retained in one candidate. Actual pilot fraction, color and decision remain unknown; no actual reversal is asserted. No card repair is needed.

## Initial screening audit

All nine defined checker findings have exactly one initial decision in the single screening table, each INCLUDE/MEETS_THRESHOLD. Each maps to the appropriate stable ID; all included provenance IDs occur in the ledger classification table/card and the evidence recheck. Parallel checker observations share a stable ID rather than creating repeated candidates. There are no SCREENED_OUT finding decisions to overturn. This does not exempt the 26 checker exclusions, independently audited below.

| Finding ID | Candidate ID | Audit of initial decision |
|---|---|---|
| F-NUM-001 | C005 | Retain INCLUDE: reproduced complementary pilot numerator, Route B. |
| F-XS-001 | C001 | Retain INCLUDE: retained primary companion analysis absent from supplied reports, Route A category 5. |
| F-XS-002 | C004 | Retain INCLUDE: printed hospital cutoff conflict beyond precision, Route B. |
| F-XS-003 | C003 | Retain INCLUDE: duration-handling manifestation of the broader explicit missing-data specification pattern, Route B. |
| F-XS-004 | C002 | Retain INCLUDE: retained prospective stay-test difference, Route B. |
| F-ST1-001 | C004 | Retain INCLUDE: independent provenance for the same hospital cutoff issue. |
| F-ST1-002 | C001 | Retain INCLUDE: independent provenance for the same Route A category-5 omission. |
| F-ST1-003 | C003 | Retain INCLUDE: all-outcome versus selected/None predictors and stay exception, one pattern. |
| F-ST1-004 | C002 | Retain INCLUDE: independent provenance for the same retained stay-test specification difference. |

## Independent audit of checker exclusions

The original numeric, cross-source and pass-1 Excluded observations tables were read, alongside pass 2's independent 26-row assessment. Each original row is retained below exactly once by within-table ordinal. No exclusion relies on a very small P displayed as zero. No reproduced interval-versus-P/test conflict is screened out as precision, wording, peripheral or conditional. Pass 2 raised no additional excluded observation or finding; its empty new-observation table is appropriate.

| Checker row | Source observation | Independent inclusion/precision audit | Retained reason code |
|---|---|---|---|
| NUM-1 | Results p24 organ-support-free missing 1639 vs main p8 16434−7327−7444=1663 | Half-unit recomputed missing interval [1661.5,1664.5] versus printed [1638.5,1639.5]; gap22/1639=.0134228≤.05. This fails numerical reproduction under the prescribed rule; no route A category-1 conflict. Counts were independently confirmed on both source images. | ROUNDING_OR_DISPLAY_PRECISION |
| NUM-2 | Results p24 ethnicity missing 1630 vs main p5 available 7340+7465 | Recomputed 1629; half-unit input interval [1627.5,1630.5] overlaps printed [1629.5,1630.5]. Gap0. No reproduced route A count issue. | ROUNDING_OR_DISPLAY_PRECISION |
| NUM-3 | Main p6 526/1252 displayed42.1% | Recomputed interval 100×[525.5/1252.5,526.5/1251.5]=[41.9561,42.0695]% overlaps [42.05,42.15]%; gap0. Distinct from C005's prospective event membership. | ROUNDING_OR_DISPLAY_PRECISION |
| NUM-4 | Results pp21–23 rounded exposure means/differences | 62.6−27.2 recomputed [35.30,35.50] overlaps displayed35.5 interval [35.45,35.55]. 37.3−26.0 recomputed [11.20,11.40] overlaps displayed11.4 [11.35,11.45]. Remaining apparent0.1 differences have the same half-unit overlap. No route A category-4 discrepancy beyond.05. | ROUNDING_OR_DISPLAY_PRECISION |
| NUM-5 | Results p22 FiO2 percentage label over fractional cells | Fractional values and adjacent definitions resolve units immediately; no printed digit, numerical sign or outcome reference is changed. Category2 is not reproduced. | NOTATION_OR_TYPOGRAPHY |
| NUM-6 | Results p27 usual SpO2 95.2 vs p21 overall95.1 | Descriptive exposure copy is peripheral to primary/key outcomes, and conditional-on-oxygen95.2 is separately identified. Half-unit intervals also touch at95.15; no reproduced numerical difference. | PERIPHERAL_COMPARISON |
| NUM-7 | PLAN sample15444, loss6%, target16500 | Allowing6% to mean [.055,.065] gives inflation approximately [16342.3,16518.2], overlapping recruitment16500±.5. The diagnostic power result15442.18 likewise reconciles rounded inputs. No sample-size logical conflict is reproduced. | ROUNDING_OR_DISPLAY_PRECISION |
| NUM-8 | PLAN100site target vs REPORT97sites achieved | Planned and achieved administrative quantities differ; no primary population size or decision-rule change is shown. Not an inconsistent count within one display. | PERIPHERAL_COMPARISON |
| NUM-9 | Results p1 contents vs eTables1–4 captions | Actual displays identify quantities; the pointer difference does not reassign a printed result's endpoint/population/time. | PERIPHERAL_COMPARISON |
| XS-1 | Usual SpO2 95.1 vs95.2 in results cross-trial table | Copy intervals [95.05,95.15] and [95.15,95.25] touch; gap0, relative0. No numerical reproduction, regardless of peripheral status. | ROUNDING_OR_DISPLAY_PRECISION |
| XS-2 | Mainp6 eFigure4 pointer vs actual eFigure5; contents shifts | The actual survival caption and HR1.01(.96,1.05) identify the same result. No quantity/outcome attribution changes. | PERIPHERAL_COMPARISON |
| XS-3 | Original oxygen target/alarms vs final/report target/alarms | Explicit v1.2 amendment supplies the active counterpart. Final reported target matches it; no reproduced active planned-versus-reported intervention change. | NOT_REPRODUCED |
| XS-4 | Organ-support outcome absent originally but reportedsecondary | Final plan explicitly adds it as SECONDARY and reported components/status match. The amendment resolves active comparison, including route A category5. | NOT_REPRODUCED |
| XS-5 | Prespecified exploratory forest HTE result not supplied | Status is exploratory and report explicitly defers separate output. No primary/key-secondary omission or changed status is established. Category5 is not applicable to this omission. | CONDITIONAL_OR_UNREPORTED |
| XS-6 | Clinical paper lacks economic/EQ5D results | Mainp3 expressly defers integrated health economics; SAP places HRQoL there. No changed endpoint status or mislabeled clinical effect is shown. | CONTEXT_RESOLVES |
| XS-7 | Shared exact75%/3% pilot boundaries | Explicit Green≥ fixes equality immediately. No observed pilot color conflict; complementary event numerator is independently retained as C005. | CONTEXT_RESOLVES |
| XS-8 | Global exploratory statement vs first-ten signal/P.03 | Immediate results context explicitly names weak first-ten harm; its interaction P and row effects are distinct. Neither printed direction nor interval/test significance conflicts. | CONTEXT_RESOLVES |
| XS-9 | Mainp8 says ranked by days with support; headingfree days | Ranking direction is unspecified, while complete composite definition identifies the outcome. No printed effect or score is demonstrably assigned a reversed quantity from this wording alone. No route A sign/reference reversal is reproduced. | TERMINOLOGY_OR_WORDING |
| ST1-1 | Adjusted RD/OR vs crude counts | Source states multilevel adjustment/marginal standardization. Crude substitution is not the supplied estimator, and no method reproduces the other modeled rows while failing one beyond.05. | MODEL_VERSUS_CRUDE |
| ST1-2 | One-year RD3.3(−.7,7.3),P=.34 vs symmetric Wald diagnostic | Point lies within interval and interval contains0 with nonsignificantP. Exact paired MI/bootstrap test/variance/df is absent. A normal approximation alone does not establish that the printed P cannot belong to the stated analysis; no reproduced category1 conflict. | CONDITIONAL_OR_UNREPORTED |
| ST1-3 | Omnibus interaction P paired to subgroup rowCI | Printed hypotheses differ. Matching source attribution eliminates the apparent conflict; category1 is not reproduced. | NOT_REPRODUCED |
| ST1-4 | Cox analysis with342 unknown exact death times | Caption expressly states interval/left censoring. Exact estimator details are absent without a conflicting printed implementation; assumed conventional partial likelihood is not source evidence. | CONDITIONAL_OR_UNREPORTED |
| ST1-5 | Re-enrollment permitted after90days vs report model | Permission does not establish actual repeated contributions or a contrary variance statement. No observed data-structure conflict is reproduced. | CONDITIONAL_OR_UNREPORTED |
| ST1-6 | Original vs final/report oxygen targets | Explicit amendment resolves active specification. No undisclosed current intervention difference or category5 status change is shown. | CONTEXT_RESOLVES |
| ST1-7 | Original SAPp107 extreme-case sensitivity absentfinal | Original and final complete missingness sections and p136 changes were independently read as images in this audit. Final section replaces/expands the original, without retaining its extreme-case promise. Unlike C001, no corresponding requirement remains in the final supplied specification. No retained planned primary analysis omission is established. | CONTEXT_RESOLVES |
| ST1-8 | Planned any-SAE Fisher test lacks printedP | Source labels safety separately; this is a non-key safety analysis omission without a printed test/interval contradiction or status change. Category5's omission category is primary/key-secondary. | CONDITIONAL_OR_UNREPORTED |

All26/26 excluded rows remain below the inclusion threshold. No audit screening row, new F-QA finding or appended candidate is required. Six precision-coded rows were individually checked against the .05 rule; no category1 conflict was treated as precision. Retained reason totals: precision6, peripheral4, notation1, not-reproduced3, conditional5, context5, terminology1, model-versus-crude1. These are observation-screening counts, not candidate dispositions.

## Source and quantitative coverage audit

| Direct source | Role by content | Total | Reusable | Fresh-required | Mapped | Audit |
|---|---|---:|---:|---:|---:|---|
| DOC-001 main article | REPORT | 11 | 11 | 0 | 11 | 11+0=11; page map contains each physical page once. |
| DOC-002 bound protocol/SAP | PLAN | 136 | 32 | 104 | 136 | 32+104=136; disjoint page maps contain every page1–136 exactly once. |
| DOC-003 results supplement | REPORT | 29 | 29 | 0 | 29 | 29+0=29; page map contains each physical page once. |
| Total | Three direct PDFs | 176 | 72 | 104 | 176 | Scientific source-unit closure complete. |

Reusable plan pages29–56,100,120,121,126 are32 unique units. Their complement1–28,57–99,101–119,122–125,127–136 is104 units. The partition is complete and disjoint; unusable encoded native text is not counted as usable coverage. Current fresh raster/OCR inventories account for all104 new CPU rasters and136 GPU OCR aids. Complete visual mapping resolves OCR omissions. Reuse accelerates extraction, not discovery: all source-unit relationships were mapped anew by fresh agents. The evidence curator excludes all six mixed legacy extractor maps in full, preventing candidate-section leakage into scientific scope; 201 raw/metadata aids are selected from483 eligible artifacts. No old candidate list or requested candidate count appears as a controlling input.

Numeric inventory contains233 distinct N IDs: main87, support39, further-plan107. All233 appear exactly once in the bounded numeric completion records; no missing, extra or repeated assessment ID was found. Grouped support relationships retain all97 site rows and222 explicit count/denominator/percentage cells, all constituent exposure rows, and safety/continuous-outcome quantities. Page maps identify contents, references and administrative pages explicitly rather than omitting them.

Statistical inventory contains195 distinct S IDs: main40, support/opening-plan37, further-plan118. The full77/118 assessment parts for each statistical pass were read. Every195 ID has exactly one per-pass completion row; there are no missing, extra or repeated per-pass IDs. The canonical inventory jointly records PASS_1_COMPLETE and PASS_2_COMPLETE for195/195 rows. The canonical pass-2 registry and exact manifest S scopes cover the same set. Checks retain both available/imputed clinical columns, every11 confirmatory subgroup row, every13 posthoc row and all exposure-difference intervals; interaction P values are matched to their own hypotheses. Exact unprinted tests are named limitations, not invented calculations.

The three sources and all201 selected reused hashes were checked with sha256sum -c during this audit: every entry matched. The coordinator must still produce the final after-hash records at closure. No source/reused asset changed during this audit.

## Coverage-manifest audit

All39 existing rows were inspected. Each Artifact cell contains exactly one plain relative path, without prose, comma, semicolon, Markdown decoration or unresolved glob. Every preceding-stage artifact exists; the audit-stable path was the only expected not-yet-written artifact when checked and now exists. Source reading shards are disjoint: main11; results29; opening plan28; plan-b28; plan-c32; plan-d32; plan-e16. The support aggregate is an explicitly lossless aggregate of its six source parts, not a second independent source assignment. Relationship blocks are disjoint; canonical aggregate/part rows are separate artifacts documenting the same completed union, not extra source units.

| Existing stage and shard rows | Audit of complete assigned scope/artifact |
|---|---|
| source_inventory: inventory | ThreePDF sources,176 units, content roles and exact hashes documented. |
| evidence_assets: reused; fresh-ocr | Every selected aid and every current136-page OCR/raster unit has provenance/fitness or fresh derivative record. |
| main_evidence_mapping: main; main-numeric; main-statistical | Main11-page map and disjoint87N/40S records are complete. |
| support_evidence_mapping: support; support-results-part; support-plan-a-part; support-numeric; support-statistical | Aggregate plus bounded29/28-page parts retain complete tables/footnotes and39N/37S IDs. |
| support_evidence_mapping: plan-b; plan-b-numeric; plan-b-statistical | Pages29–56 complete;15N/17S. |
| support_evidence_mapping: plan-c; plan-c-numeric; plan-c-statistical | Pages57–88 complete;30N/23S. |
| support_evidence_mapping: plan-d; plan-d-numeric; plan-d-statistical | Pages89–120 complete;34N/31S. |
| support_evidence_mapping: plan-e; plan-e-numeric; plan-e-statistical | Pages121–136 complete;28N/47S. |
| numeric_checks: numeric-all; numeric-main; numeric-support; numeric-plan |233/233N IDs assessed once in bounded parts; canonical findings/exclusions complete. |
| cross_source_checks: cross-all |24 matched counterpart families cover all3 sources with endpoint/model/population matching and amendments. |
| statistics_pass_1: stat1-all; stat1-report-part; stat1-plan-part | Explicit scopes enumerate all195S IDs;77/118 parts and canonical artifact complete. |
| inclusion_screening: initial-nine; initial-groups | Nine findings independently decided; consolidated groups retain every source occurrence/provenance. |
| candidate_registration: initial-stable | Exact C001,C002,C003,C004,C005 set and allnine INCLUDED findings retained. |
| evidence_recheck: initial-recheck | Exact C001,C002,C003,C004,C005 set; each affected location source-confirmed, classification/evidence state explicit. |
| statistics_pass_2: stat2-all; stat2-report; stat2-plan | Explicit scopes enumerate all195S IDs; all195 independently completed after ledger/screen/recheck. |
| evidence_quality: audit-stable | Exact C001,C002,C003,C004,C005 set, nine decisions,26 exclusions, all39 existing rows and classifications audited here. |

The auditor's row is appropriately PLANNED while this artifact is being assembled. The coordinator must mark it COMPLETE after handoff and add the next mandatory report_generation rows, explicitly enumerating allfive IDs with one artifact path each. Expected future report sequencing is not a scientific source gap.

## Runtime routing and freshness audit

Execution manifest contains15 distinct actual runtime IDs at this stage, including the current coordinator exactly once. All rows specify gpt-6.1-sol; coordinator/high, ordinary curator/mappers/numeric/cross medium, statistical/screen/recheck/audit high match the fixed contract. All mandatory specialists are FRESH_SPAWN with distinct canonical runtime identifiers. Optional plan shards extend mapping at medium and do not replace another mandatory stage.

| Required independent runtime | Manifest evidence | Audit |
|---|---|---|
| Statistical pass1 | root/statistical_pass_1; gpt-6.1-sol/high; FRESH_SPAWN | Distinct mandatory first-pass runtime;195 complete. |
| Initial inclusion screener | root/initial_screener; gpt-6.1-sol/high; FRESH_SPAWN | Independent of both checker/mapping and recheck stages; nine source-grounded decisions. |
| Evidence rechecker | root/evidence_rechecker; gpt-6.1-sol/high; FRESH_SPAWN | Fresh exact-source stage after stable registration; allfive reproduced. |
| Statistical pass2 | root/statistical_pass_2; gpt-6.1-sol/high; FRESH_SPAWN | Distinct from pass1 and every other stage; ledger/screen/recheck explicitly assessed;195 complete. |
| Quality auditor | root/quality_auditor; gpt-6.1-sol/high; FRESH_SPAWN | Independent current audit runtime, all stable IDs returned. |

Statistical pass1 was continued within its original stage to finalize durable output, as documented by the coordinator; it was not reused/promoted for a different mandatory stage. No pass2 findings exist, so a pass2 inclusion screener is not applicable. The mandatory report generator is the next fresh gpt-6.1-sol/medium runtime and must be added exactly once when spawned. Routing preflight already records PASS and verified fixed pairs; provider remains the current session.

## Card completeness, neutrality and repair record

Stable registration order reproduces the main p3 Statistical Analysis reading sequence: primary covariate/model specification (C001), outcome model sentence naming Fine–Gray stay regression (C002), then the MICE auxiliary paragraph (C003). C004 follows at main p8's hospital-duration footnote; C005 is the remaining PLAN-only decision rule. The order is source-grounded and requires no stable-ID renumbering.

Every ledger C card contains printed statements, complete source locations and roles, applicable comparison/calculation, named affected extraction, route/B criteria, source-grounded alternatives, bounded missing inputs/human question and neutral pending-human status. Recheck supplies direct observation versus inferred explanation separately. The classification table and ledger card fields agree with recheck; precedence and corroboration are appropriately distinguished. Repeated findings are consolidated without suppressing a stable ID. The nine initial findings remain provenance of five distinct issues; C002 method identity, C003 missing-data strategy and C004 hospital cutoff are different rules and are not an unmerged repetition.

A mechanical check of all644 local Markdown links across current evidence/mapping/checker/screen/ledger/recheck artifacts found no absent target or out-of-range physical PDF anchor. Candidate/recheck links use the correct directory-relative source paths; PLANp70 is physical page70 even though its printed footer is29. The exact source images independently inspected here agree with those page assignments.

Vocabulary review found no prohibited evaluative description of a candidate, value or authors' work. Existing occurrences are the established terms standard error and congenital anomaly/birth defect in source-preserving extraction; these retain their statistical/clinical meaning. No candidate depends on a display-zero P. No severity, acceptance, preferred analysis or paper-level disposition is assigned. Impact is limited to the named analysis specification or planned decision rule; no actual effect alteration, actual pilot reversal or broad conclusion impact is claimed.

| Repair or completion action | Reason | Responsibility/status |
|---|---|---|
| Replace the five Pending inclusion-audit values in ledger table and cards with CONFIRMED | This independent audit confirms each reproduced issue by its recorded route. | Coordinator after this handoff; no scientific classification change. |
| Carry identical domain/type/allrelationships/roles/state/audit/finding fields into every report card | The report is assembled after audit; it must repeat the finalized ledger classification exactly. | Mandatory fresh report generator and coordinator final comparison. |
| Preserve C003's alternative/nonuniversal auxiliary-sentence interpretation | Evidence supports the printed specification difference without establishing executed predictor matrices. | Final reporting requirement; current ledger/recheck already explicit. |
| Complete audit/report coverage rows and append actual report-generator runtime | Current audit and next-stage reporting are sequential work. | Coordinator closure. |
| Final after-hashes, finish/performance fields, HTML rendering, fallback removal and validator PASS | These occur after Markdown assembly under the prescribed sequence. | Coordinator closure; no current scientific-coverage limitation. |

No source-evidence, arithmetic, location, screening or classification repair is requested. No F-QA finding or new stable ID is raised. Ledger/recheck/audit sets are exactly C001,C002,C003,C004,C005. At this pre-report audit stage no current final report exists to compare; ledger/report identity is an explicit final coordinator check, not an unsupported assertion made here.

## Bounded limitations and completion

Scientific assigned coverage is complete:176/176 source pages;233/233N IDs;195/195S IDs in each of two fresh independent statistical passes; nine/nine finding decisions;26/26 checker exclusions; five/five stable IDs. Inclusion-audit counts: CONFIRMED5, QUESTIONED0. New findings0; screening reversals0; classification changes0; evidence states reproduced5.

Bounded evidence limitations are unprovided implemented analysis code/predictor matrices, unrounded test/variance/df/bootstrap details, exact unknown-death-time estimator, actual repeat-enrollment contributions, hospital censoring timestamps, exact graphic ordinates and actual pilot fraction/color/decision record. Derivative limitations are incomplete legacy engine metadata and OCR omissions, resolved for scientific coverage by complete source-image mapping and direct recheck. None authorizes omitting a unit or inventing an effect. Every candidate remains Pending Human Adjudication.

