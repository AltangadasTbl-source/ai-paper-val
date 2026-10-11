# Quantitative Quality-Control Consistency Review — Workflow 1.6.2

**Pending Human Adjudication.** All eight candidates below are candidate reporting issues or inconsistencies. Evidence reproduction and inclusion audit are quality-control records, not human adjudications.

## Executive Quality-Control Summary

Complete review of the three supplied PDFs identified **8 stable candidates**, C001 through C008. Independent screening considered 16 checker findings: 14 INCLUDE records consolidated into eight distinct issues, and two SCREENED_OUT records. All eight candidates have reproduced evidence and CONFIRMED inclusion audits. Four concern statistical results, three concern plan–report comparisons, and one concerns plan material. No candidate concerns report-internal attribution of a number to a competing outcome or population.

The review covers counts and denominators, estimate and test logic, statistical method logic, and planned versus reported statistical design. All 146 physical source pages were mapped. Both independent statistical passes completed all 81 statistical relationships; numeric review completed 120 relationships and cross-source review completed 89 comparison groups. Potential implications concern the definition, population, percentage, interval, or decision boundary that an evidence extractor could record. The review does not establish actual changes to trial conclusions or downstream evidence.

## Package and Reused-Evidence Provenance

The package is the CAAM randomized-trial report comparing bag-mask ventilation (BMV) with endotracheal intubation (ETI; TI in plan material). Physical PDF page numbers are used throughout.

| Source | Content role | Physical pages | SHA-256 |
|---|---|---:|---|
| [jama_jabre_2018_oi_180004.pdf](<../jama_jabre_2018_oi_180004.pdf#page=1>) | REPORT: main completed-trial article | 9 | `114e922542bbb1f8369ca9b5c19be65d93856e16cf4ff295c483439e4e208839` |
| [joi180004supp1_prod.pdf](<../joi180004supp1_prod.pdf#page=1>) | PLAN: original/final protocols, amendments and native/signed SAP copies | 134 | `70106d31b08e3a9d7eaac8a0e035bbf8d92a43b51f2483b634d7349b0c5f6913` |
| [joi180004supp2_prod.pdf](<../joi180004supp2_prod.pdf#page=1>) | REPORT: non-plan results supplement | 3 | `937e18794fc87074907b1e9ab792f9a35d2f2d895d586dd27e7cbf44d5ed8d46` |

The [source inventory](review_1_6_2/source_inventory.md), [evidence-asset inventory](review_1_6_2/evidence_asset_inventory.md) and [reused-artifact hash inventory](review_1_6_2/reused_artifact_hashes_before.sha256) document 128 reused text, OCR, image and extraction-provenance artifacts. These assets supported fresh discovery and mapping; earlier scientific selections and conclusions were not inputs. All six legacy Poppler native/layout files were byte-matched to current direct extraction. The plan OCR metadata matches the supplied plan's source hash. Alternate PyMuPDF text records engine 1.28.0; no new invocation was made.

Historical OCR records rapidocr_onnxruntime/rapidocr-cuda on an NVIDIA GeForce RTX 5070 Laptop GPU for 11 plan pages. This run reused those assets and used CPU processing only. Some historical rendering-engine details and secondary OCR-engine details are unavailable; source page identity and direct visual confirmation govern candidate evidence.

## Scope, Complete Coverage, and Exclusions

| Source | Total units | Reusable-backed units | Fresh-required derivative units | Mapped units | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 main article | 9 | 9 | 0 | 9 | COMPLETE |
| DOC-002 plan bundle | 134 | 134 | 0 | 134 | COMPLETE |
| DOC-003 results supplement | 3 | 3 | 0 | 3 | COMPLETE |
| Total | 146 | 146 | 0 | 146 | COMPLETE |

Zero fresh-required derivative units does not mean zero fresh scientific review. Every page received fresh mapping, including covers, forms, references, amendments and pages without applicable quantitative content. Main mapping covers pages 1–9. Disjoint support parts cover plan pages 1–63, 64–107, and 108–134 plus results-supplement pages 1–3; their canonical merge retained all content. The [source coverage ledger](review_1_6_2/source_coverage.md) and [coverage manifest](review_1_6_2/coverage_manifest.md) record these assignments.

Plan pages 108–109 and 126–134 lack native text; page 134 lacks OCR. Source-matched supplied OCR and readable images cover the scans, and the page-134 image was visually mapped as header/footer with an otherwise blank body. Embedded IDS displays on plan pages 52 and 103 received fresh CPU image confirmation. No scientific source-unit gap remains. No direct Office, workbook or CSV source is supplied.

Excluded scope includes broad methodology, clinical or study-design critique, preferred analyses, raw-data auditing, and external literature. Within the quantitative scope, the review applies the display-precision rule, retains distinct analysis populations and models, and screens out peripheral comparisons or context-resolved wording when no always-register category applies.

## Quantitative and Statistical Relationship Coverage

The complete [main quantitative map](review_1_6_2/extraction/main_quantitative_evidence.md) and [support quantitative map](review_1_6_2/extraction/support_quantitative_evidence.md) reconstruct result-relevant displays before candidate selection. Review matched quantities by outcome, population, time point, contrast, reference group and model.

| Review scope | Completed relationships or groups | Durable record |
|---|---:|---|
| Numeric counts, denominators, totals and effect-measure identity | 120 | [Numeric relationship inventory](review_1_6_2/relationships/numeric_relationship_inventory.md) |
| Cross-source and cross-location comparisons | 89 | [Cross-source checker](review_1_6_2/checkers/cross_source_consistency.md) |
| Statistical pass 1 | 81 of 81 | [Pass 1](review_1_6_2/checkers/statistical_pass_1.md) |
| Statistical pass 2 | 81 of 81 | [Pass 2](review_1_6_2/checkers/statistical_pass_2.md) |

Every statistical inventory row records PASS_1_COMPLETE and PASS_2_COMPLETE in the [statistical relationship inventory](review_1_6_2/statistics/relationship_inventory.md). The two high-effort passes used distinct fresh runtime agents. They addressed counts, containment and interval order, estimate/interval/test compatibility, noninferiority and other decision rules, method logic, matching copies, effect-measure identity, and plan–report design comparisons. A named missing input limits mechanical reconstruction without leaving its relationship unreviewed.

Pass 2 reread all 45 initial checker excluded observations: nine numeric, 17 cross-source and 19 statistical-pass-1 rows. It generated zero new findings and zero new excluded observations. The independently audited accounting is precision 11, not reproduced 2, notation 4, peripheral 10, model versus crude 2, context resolves 3, wording 6, conditional/unreported 6, and duplicate of included 1. The last row is planned OR-interval presentation already covered by C003; it is not an additional finding in the inclusion log. Quality audit reviewed all exclusions and all screening decisions in both directions and identified no additional distinct issue.

## Inclusion Screening Summary

A candidate requires reproduction plus either an always-register Route A category or all three Route B conditions: in focus, unresolved by immediate context, and bearing on interpretation or extraction. Printed numeric comparisons allow every input and output its half-unit display interval; interval overlap or a relative interval gap at most 0.05 is screened out. Interval-versus-P/test conflicts are always-register comparisons and are not screened as precision differences.

Counts below reconcile exactly to the single table in the [inclusion screening log](review_1_6_2/screening/inclusion_screen.md). They count findings, not checker excluded observations.

| Decision | Reason code | Count |
|---|---|---:|
| INCLUDE | MEETS_THRESHOLD | 14 |
| SCREENED_OUT | NOT_REPRODUCED | 1 |
| SCREENED_OUT | ROUNDING_OR_DISPLAY_PRECISION | 1 |
| SCREENED_OUT | NOTATION_OR_TYPOGRAPHY | 0 |
| SCREENED_OUT | TERMINOLOGY_OR_WORDING | 0 |
| SCREENED_OUT | MODEL_VERSUS_CRUDE | 0 |
| SCREENED_OUT | CONTEXT_RESOLVES | 0 |
| SCREENED_OUT | CONDITIONAL_OR_UNREPORTED | 0 |
| SCREENED_OUT | PERIPHERAL_COMPARISON | 0 |
| SCREENED_OUT | OUT_OF_FOCUS | 0 |
| SCREENED_OUT | DUPLICATE_OF_INCLUDED | 0 |
| Total screened findings | All decisions | 16 |

The included records consolidate into eight issues while preserving every included finding ID. The screened PP survival point difference has overlapping full half-unit intervals. The screened composite comparison matched distinct procedural and death-containing outcomes rather than a reproduced change in a common outcome. Neither has a candidate card. Pass 2 and audit required no additional screening rows.

## Review-Domain Summary

| Review domain | Definition | Candidates |
|---|---|---:|
| statistical_results | Counts, estimates, intervals, tests or statistical method logic in REPORT material | 4 |
| report_internal_inconsistency | REPORT locations conflict about which outcome, population, time point or comparison a number describes | 0 |
| protocol_report | REPORT differs from PLAN in statistical design or analysis | 3 |
| plan_material | PLAN internally differs in a statistical design element used by reported analysis | 1 |
| Total | One domain per candidate | 8 |

| Primary relationship type | Meaning | Candidates |
|---|---|---:|
| P_R | PLAN–REPORT comparison | 3 |
| P_P | PLAN-only comparison | 1 |
| S_C | Between different REPORT documents | 0 |
| S_W | Within one REPORT document | 4 |
| Total | Primary types | 8 |

C002 also contains P_P; P_R takes precedence. Across all relationships, P_R occurs in three candidates, P_P in two, S_W in four and S_C in zero; these memberships overlap and sum to nine. Corroborating documents do not introduce conflicting relationships.

| Evidence state | Candidates |
|---|---:|
| reproduced | 8 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| Total | 8 |

Inclusion audit counts are CONFIRMED 8 and QUESTIONED 0. These counts are inclusion records, not adjudications.

## Candidate Index

| Stable ID | Candidate reporting issue | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|---|
| [C001](#C001) | Primary favorable-survival definition | protocol_report | P_R | reproduced | CONFIRMED |
| [C002](#C002) | Airway endpoint status | protocol_report | P_R | reproduced | CONFIRMED |
| [C003](#C003) | Specified analysis populations and interval presentations | protocol_report | P_R | reproduced | CONFIRMED |
| [C004](#C004) | Numerical ordering of noninferiority bound | statistical_results | S_W | reproduced | CONFIRMED |
| [C005](#C005) | Table 2 per-protocol confidence intervals | statistical_results | S_W | reproduced | CONFIRMED |
| [C006](#C006) | Per-protocol ROSC count and percentage | statistical_results | S_W | reproduced | CONFIRMED |
| [C007](#C007) | Native/signed SAP alternative boundary | plan_material | P_P | reproduced | CONFIRMED |
| [C008](#C008) | Post-hoc exclusion confidence interval | statistical_results | S_W | reproduced | CONFIRMED |

## Candidate Evidence Cards

<a id="C001"></a>
## C001 — Primary favorable-survival definition

Pending Human Adjudication.

**Candidate statement:** The amended primary favorable-survival definition allows unchanged pre-existing neurological disability, whereas the article's explicit success rule counts CPC categories 1–2.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN, REPORT

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-001, F-ST1-006

**Qualifying route:** Route B

**Classification rationale:** The conflict is between an amended PLAN endpoint predicate and the completed REPORT coding statement. Earlier plan wording corroborates the absolute CPC rule and a disclosed chronology; it does not add an unexplained plan-internal comparison.

**Classification ambiguity:** Disclosed endpoint chronology and retained older SAP wording do not identify how the amended exception was applied to the reported primary indicator.

**Exact source locations:** PLAN [joi180004supp1_prod.pdf — p. 71 §4.1.1](<../joi180004supp1_prod.pdf#page=71>) and [p. 110 amendment comparison](<../joi180004supp1_prod.pdf#page=110>); REPORT [jama_jabre_2018_oi_180004.pdf — p. 1 Main Outcomes and Measures](<../jama_jabre_2018_oi_180004.pdf#page=1>), [p. 3 Outcomes](<../jama_jabre_2018_oi_180004.pdf#page=3>), [p. 4 Primary Outcome](<../jama_jabre_2018_oi_180004.pdf#page=4>) and [p. 6 Table 2 footnote b and ITT CPC rows](<../jama_jabre_2018_oi_180004.pdf#page=6>). Corroborating older PLAN definitions: [p. 15 §4.1.1](<../joi180004supp1_prod.pdf#page=15>), [p. 122 §6.1](<../joi180004supp1_prod.pdf#page=122>) and [p. 131 signed §6.1](<../joi180004supp1_prod.pdf#page=131>).

**Source evidence:** The final protocol adds favorable survival with the same neurological disability as before randomization. The amendment discloses this addition. The article defines success as CPC 1 or 2 and reports primary ITT successes 44/1018 and 43/1022; its CPC rows are 35 and 9 versus 37 and 6.

**Reported-versus-comparator:** REPORT success is absolute CPC≤2; amended PLAN success can also include unchanged baseline CPC>2. Original protocol and both SAP copies retain the absolute rule.

**Reasoning procedure:** Compare the success predicates, then reconcile the article's displayed CPC categories with its numerator. Separate the observable definition difference from any participant-level impact.

**Calculation:** 35+9=44 and 37+6=43. Full half-unit sums [43,45] and [42,44] overlap printed numerator ranges [43.5,44.5] and [42.5,43.5]; arithmetic discrepancy is zero. Categorical predicates are not reconciled through rounding. No numerical impact can be calculated without baseline-to-day-28 CPC linkage and exception coding.

**Affected result or extracted value:** The primary favorable-neurological-survival definition attached to 44/1018 and 43/1022.

**Why context does not resolve it:** Route B applies: this is the primary endpoint definition, and the report's CPC coding does not establish whether the amended unchanged-disability exception was used. An extractor cannot identify the exact implemented predicate from that coding statement alone.

**Alternative source-grounded interpretations:** No survivor may have qualified for the exception; it may have been applied without changing the displayed totals; or the older absolute definition may have been used. The disclosed amendment explains chronology without resolving implementation.

**Mechanical evidence recheck:** Every cited location and source/comparator statement was found and matched. The logical rule and count checks reproduced; content roles and classification were confirmed without transcription adjustment. Missing inputs are participant-linked baseline/day-28 CPC, eligible survivor counts and the implemented coding instruction. The reproduced fact is a definition discrepancy, not an observed numerator change or production mechanism.

**Potential downstream evidence impact:** If confirmed, an extractor could attach CPC≤2 alone to the prespecified primary outcome and omit the baseline-relative exception. No participant reclassification, numerator change or conclusion change is established.

<a id="C002"></a>
## C002 — Airway endpoint status across protocol, SAP and report

Pending Human Adjudication.

**Candidate statement:** Matched airway outcomes are assigned to protocol/report secondary endpoint lists and to the SAP's separately specified safety endpoint family. Concurrent secondary and safety designations remain a substantive source-grounded interpretation.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN, REPORT

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-002, F-ST1-007

**Qualifying route:** Route A, category 5

**Classification rationale:** Protocol–SAP assignments provide P_P and SAP–report assignments provide P_R. P_R takes precedence. All protocols and SAP copies are PLAN; article endpoint lists and safety results are REPORT.

**Classification ambiguity:** The sources may use concurrent secondary/safety umbrella designations rather than replace formal endpoint hierarchy. The SAP nevertheless separates efficacy and safety families and their analysis populations.

**Exact source locations:** PLAN original secondary lists in [joi180004supp1_prod.pdf — p. 9 Summary](<../joi180004supp1_prod.pdf#page=9>), [p. 10 continuation](<../joi180004supp1_prod.pdf#page=10>), [p. 16 §4.1.2](<../joi180004supp1_prod.pdf#page=16>); final lists [p. 64 Summary](<../joi180004supp1_prod.pdf#page=64>), [p. 65 continuation](<../joi180004supp1_prod.pdf#page=65>), [p. 71 §4.1.2](<../joi180004supp1_prod.pdf#page=71>); SAP families [p. 122 §§6.1–6.2](<../joi180004supp1_prod.pdf#page=122>) and [p. 131 signed §§6.1–6.2](<../joi180004supp1_prod.pdf#page=131>). Concurrent safety-analysis context: [p. 37 §11.5](<../joi180004supp1_prod.pdf#page=37>) and [p. 92 §11.5](<../joi180004supp1_prod.pdf#page=92>). REPORT [jama_jabre_2018_oi_180004.pdf — p. 1 Main Outcomes and Measures](<../jama_jabre_2018_oi_180004.pdf#page=1>), [p. 3 Outcomes](<../jama_jabre_2018_oi_180004.pdf#page=3>), [p. 4 Adverse Events Analysis](<../jama_jabre_2018_oi_180004.pdf#page=4>) and [p. 6 Table 3 Safety Population](<../jama_jabre_2018_oi_180004.pdf#page=6>).

**Source evidence:** Protocols place airway difficulty/complications in secondary lists. SAP copies place VAS/Han and airway failure/complications in Safety Endpoints, separate from secondary efficacy admission survival, day-28 survival, ROSC and IDS. The report calls difficulty/failure secondary and also presents safety analyses.

**Reported-versus-comparator:** Matched measures include VAS/Han BMV difficulty; TI failure, esophageal/mainstem intubation, vomiting, pulmonary aspiration, dental trauma and extubation; and BMV gastric regurgitation. SAP BMV failure and gastric inflation are retained as family context without inventing a corresponding protocol entry for gastric inflation. IDS remains secondary efficacy and is not a shifted-status measure. The abstract-reported difficulty, failure and regurgitation results are affected.

**Reasoning procedure:** Match individual endpoints across explicit lists and analysis families, retaining all repeated locations. Distinguish formal family assignments from an ordinary descriptive heading and retain concurrent labels as an alternative.

**Calculation:** Logical endpoint-family comparison; numerical display precision does not apply to status categories. No event count, effect size or numerical hierarchy impact is inferred. Formal concurrent-status mapping and the governing ITT/PP/AT family are not uniquely supplied.

**Affected result or extracted value:** Prespecified status and analysis-family assignment of abstract-reported airway difficulty, failure and regurgitation, with the matched complications forming the repeated pattern.

**Why context does not resolve it:** Route A, category 5 concerns planned versus reported outcome status. Concurrent labels provide an alternative interpretation but do not establish that the SAP's separately specified efficacy/safety assignments are formally identical.

**Alternative source-grounded interpretations:** Secondary may be an umbrella under which safety endpoints coexist. Both protocol safety sections and article secondary/safety usage support this possibility. The supplied separation of SAP efficacy and safety families, with differing analysis populations, leaves the formal crosswalk unspecified.

**Mechanical evidence recheck:** Every cited assignment and repeated family location was found and matched. Logical comparison reproduced and classification confirmed, including P_R precedence over P_P. No numerical inputs are needed. Missing is the formal concurrent-status crosswalk and the analysis-family mapping governing published airway results. Direct observation is the differing allocations; a substantive hierarchy replacement is not established.

**Potential downstream evidence impact:** If confirmed, an extractor could assign a single prespecified efficacy or safety status, and associated analysis population, to a result with unresolved concurrent designations. No change to the event estimates or downstream conclusions is demonstrated.

<a id="C003"></a>
## C003 — Specified analysis populations and interval presentations

Pending Human Adjudication.

**Candidate statement:** Explicitly specified primary/key-secondary population analyses and interval presentations have no identified matching display in the complete supplied reporting package.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN, REPORT

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-003, F-ST1-008

**Qualifying route:** Route A, category 5

**Classification rationale:** SAP/protocol analysis and presentation requirements are PLAN; completed article and post-hoc supplement are REPORT. Both reporting documents contribute the searched scope, without conflicting copies that would create S_C.

**Classification ambiguity:** The SAP contains prospective and retrospective language, limiting chronology interpretation. The post-hoc reclassification could have been intended as a population counterpart, but an explicit AT crosswalk or replacement amendment is absent.

**Exact source locations:** PLAN [joi180004supp1_prod.pdf — p. 121 §5.3](<../joi180004supp1_prod.pdf#page=121>), [p. 130 signed §5.3](<../joi180004supp1_prod.pdf#page=130>), [p. 124 §§8.2.1, 8.2.3, 8.2.4](<../joi180004supp1_prod.pdf#page=124>) and [p. 133 signed corresponding sections](<../joi180004supp1_prod.pdf#page=133>). Corroborating OR-presentation specifications: [p. 37 §§11.4.2–11.5](<../joi180004supp1_prod.pdf#page=37>), [p. 91 §11.4.2](<../joi180004supp1_prod.pdf#page=91>), [p. 92 §11.5](<../joi180004supp1_prod.pdf#page=92>). REPORT [jama_jabre_2018_oi_180004.pdf — p. 1 abstract](<../jama_jabre_2018_oi_180004.pdf#page=1>), [p. 3 Statistical Analysis](<../jama_jabre_2018_oi_180004.pdf#page=3>), [p. 4 Results](<../jama_jabre_2018_oi_180004.pdf#page=4>), [p. 6 Tables 2–3 and post-hoc continuation](<../jama_jabre_2018_oi_180004.pdf#page=6>), and [joi180004supp2_prod.pdf — p. 3 eTable 2](<../joi180004supp2_prod.pdf#page=3>). Complete search scope: main physical pages 1–9 and results-supplement pages 1–3.

**Source evidence:** The SAP defines AT by technique actually received and specifies primary CI/NI analysis in ITT/PP/AT, secondary analysis also in PP/AT, safety analysis in ITT/AT, secondary OR/difference intervals and safety OR intervals. The supplied report displays primary ITT/PP NI, secondary ITT/PP and actual-treatment safety. It states that OR intervals were calculated but does not display the specified trial OR intervals.

**Reported-versus-comparator:** No matching full AT primary NI, AT admission/day-28 survival, randomized ITT difficulty/failure/regurgitation, or corresponding trial OR interval presentation is identified. eTable 2 supplies one-way BMV→ETI reclassification under an ITT heading, not an identified full AT mapping and AT NI test. The article's actual-treatment safety population supplies the AT safety counterpart, not the additional ITT safety display.

**Reasoning procedure:** Match each specified primary or abstract-reported secondary analysis to the complete supplied report scope by endpoint, population, contrast and inferential purpose. Keep actual-treatment safety and reclassification distinct from an assumed full AT efficacy analysis.

**Calculation:** eTable 2 reclassification prints 41/863 versus 45/1174 with a conventional two-sided interval and zero-difference P value. Those values alone do not identify a full AT NI analysis. Rounding cannot supply an absent population mapping or planned presentation; this is a logical reporting comparison, not a numeric residual.

**Affected result or extracted value:** Primary NI population coverage, abstract-reported admission/day-28 survival and airway-event population coverage, and planned OR estimates/intervals.

**Why context does not resolve it:** Route A, category 5 covers planned primary/key-secondary analyses not reported. Calculation language is not presentation of an estimate/interval, and the post-hoc row lacks the specified population and NI crosswalk.

**Alternative source-grounded interpretations:** The post-hoc row may have been intended as an AT primary counterpart; an unsupplied amendment may explain changed reporting; the promised results may exist outside this package. These possibilities do not provide a supplied matching result.

**Mechanical evidence recheck:** Requirements, report counterparts and every cited location were found and matched; complete main/results reporting scope was checked. Reproduced evidence is absence of identified matching displays in supplied material, not proof that an analysis was never conducted. Missing are full AT mapping, additional population/OR outputs and an explicit replacement amendment. Roles and P_R classification were confirmed without transcription adjustment.

**Potential downstream evidence impact:** If confirmed, an extractor could miss a planned population-specific result or infer that a post-hoc row supplies the complete AT analysis. No unperformed analysis, selective intention or actual conclusion change is established.

<a id="C004"></a>
## C004 — Numerical ordering of the noninferiority confidence bound

Pending Human Adjudication.

**Candidate statement:** The primary-outcome paragraph describes the −1.64% lower bound as greater than the −1% NI threshold, reversing their numerical ordering while also concluding that NI was not demonstrated.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-004, F-ST1-001

**Qualifying route:** Route A, category 2

**Classification rationale:** The conflicting rule and numerical-order statement are within the same REPORT article. Other conclusions corroborate one side and add no relationship.

**Classification ambiguity:** None

**Exact source locations:** REPORT [jama_jabre_2018_oi_180004.pdf — p. 3 Statistical Analysis](<../jama_jabre_2018_oi_180004.pdf#page=3>) and [p. 4 Primary Outcome](<../jama_jabre_2018_oi_180004.pdf#page=4>). Corroborating no-NI statements: [p. 1 abstract](<../jama_jabre_2018_oi_180004.pdf#page=1>), [p. 2 Key Points](<../jama_jabre_2018_oi_180004.pdf#page=2>), [p. 7 Discussion](<../jama_jabre_2018_oi_180004.pdf#page=7>) and [p. 8 Conclusions](<../jama_jabre_2018_oi_180004.pdf#page=8>).

**Source evidence:** Methods accept NI when the lower CI bound exceeds −1%. Results print −1.64%, describe it as greater than the threshold, and state that NI was not demonstrated. Other report locations retain the inconclusive NI result.

**Reported-versus-comparator:** Printed greater-than reading versus −1.64<−1. The numerical bound and no-NI conclusion agree under the stated rule.

**Reasoning procedure:** Compare the already printed lower bound with the declared design margin; no CI algorithm or test reconstruction is needed. Check whether full display allowance can reverse their order.

**Calculation:** Literal separation is 0.64 percentage points. Lower-bound interval [−1.645,−1.635]% is wholly below exact −1%. Even allowing the broader margin display interval [−1.5,−0.5]% leaves a 0.135-point gap and relative discrepancy 0.135/1=0.135>0.05. Against the exact margin the minimum separation is 0.635 points.

**Affected result or extracted value:** The bound-versus-margin explanation of the primary ITT NI result.

**Why context does not resolve it:** Route A, category 2 retains a numerical-direction statement that reverses printed values. The inferable intended wording does not remove that printed reading.

**Alternative source-grounded interpretations:** The greater-than phrase may express a different intended comparison. The immediate no-NI conclusion and other report copies support the below-margin reading; no competing actual NI result is supplied.

**Mechanical evidence recheck:** All cited locations and printed values were found and matched. Ordering and display-precision calculation reproduced; no numerical input is missing. The intended ordering phrase remains unspecified. Direct observation is the incompatible ordering, while its production mechanism or replacement wording is not observed. Classification was confirmed without adjustment.

**Potential downstream evidence impact:** If confirmed, an extractor could copy the reversed bound/threshold explanation. The article's overall no-NI conclusion is supported by its printed bound and is not shown to change.

<a id="C005"></a>
## C005 — Table 2 per-protocol confidence intervals

Pending Human Adjudication.

**Candidate statement:** Two PP binary-outcome intervals do not reproduce under an independent-proportion normal/Wald 95% interval calculation that reproduces the other binary rows in the same display, beyond full display-precision allowance.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-002

**Qualifying route:** Route A, category 4

**Classification rationale:** Affected results, printed inputs and same-display comparators all belong to main REPORT Table 2. There is no conflicting PLAN or second REPORT copy.

**Classification ambiguity:** None

**Exact source locations:** REPORT [jama_jabre_2018_oi_180004.pdf — p. 6 Table 2, PP survival at 28 days and survival to hospital admission](<../jama_jabre_2018_oi_180004.pdf#page=6>), including same-table ITT survival, ITT admission, ITT ROSC and PP ROSC comparators and footnote a; [p. 3 Statistical Analysis](<../jama_jabre_2018_oi_180004.pdf#page=3>) supplies secondary difference/OR interval language without a row-specific CI algorithm.

**Source evidence:** PP denominators are 995 and 943. Survival counts are 54 and 51, difference 0.1, CI [−10,9.7], P=.99. Admission counts are 289 and 312, difference −4.0, CI [−7.6,0.6], P=.055. Footnote a identifies chi-square/Fisher tests for P values, not the interval algorithm.

**Reported-versus-comparator:** The reproducing calculation gives PP survival [−1.997461,2.035189] and PP admission [−8.160786,0.079446]. In the same table it reproduces ITT survival [−1.832853,2.070839], ITT admission [−7.703934,0.297908], ITT ROSC [−8.834359,−0.487092], and PP ROSC [−9.906235,−1.307629] at printed precision.

**Reasoning procedure:** With p=a/n and q=b/m, calculate d=100(p−q), standard error s=100√[p(1−p)/n+q(1−q)/m], and d±1.95996398454s. This is an independent reproducing-method comparison; it does not establish that the authors used Wald intervals. Permit all counts/denominators ±0.5 and printed limits their own half-unit intervals. Conservative separate difference/variance extrema enlarge the possible endpoint ranges; tighter joint arithmetic cannot close retained gaps.

**Calculation:**

| Affected limit | Recomputed range | Printed range | Gap | Relative gap |
|---|---|---|---:|---:|
| PP survival lower −10 | [−2.116389,−1.878497] | [−10.5,−9.5] | 7.383611 | 0.738361 |
| PP survival upper 9.7 | [1.916219,2.154111] | [9.65,9.75] | 7.495889 | 0.772772 |
| PP admission upper 0.6 | [−0.059492,0.218370] | [0.55,0.65] | 0.331630 | 0.552717 |

PP admission lower alone has range [−8.299719,−8.021857] versus [−7.65,−7.55], residual 0.371857/7.6=0.048929≤0.05, so it is not an independent qualifying discrepancy. PP survival point-difference range [−0.090007,0.127730] overlaps printed [0.05,0.15]; its gap is zero. Both affected printed intervals contain zero consistently with their nonsignificant P values; no interval-versus-P conflict is asserted.

**Affected result or extracted value:** PP 28-day survival and hospital-admission risk-difference confidence limits in Table 2.

**Why context does not resolve it:** Route A, category 4 applies because the same-display reproducing method leaves relative gaps above 0.05. Its uncertainty is the unprinted interval method or input mapping, not absence of an observable comparison.

**Alternative source-grounded interpretations:** A distinct row-specific method, another input population, or an alternative intended limit reading could explain the display. The methods do not uniquely establish the actual algorithm. The two PP rows form one same-display pattern; no shared cause with C008 is established.

**Mechanical evidence recheck:** Both affected rows, all four same-display comparators and method context were directly matched. Independent full half-unit arithmetic reproduced the stated gaps and precision exceptions. All numeric inputs for this comparison are available; actual CI algorithm, per-row method/population changes and source calculation output are absent. Direct observation is lack of reproduction under a comparator-supported method, not an assigned replacement interval. Classification was confirmed without adjustment.

**Potential downstream evidence impact:** If confirmed, an extractor could copy the printed PP confidence limits for synthesis or precision assessment. The review does not establish which replacement limits are intended or any actual downstream change.

<a id="C006"></a>
## C006 — Per-protocol ROSC count and percentage

Pending Human Adjudication.

**Candidate statement:** The PP ETI ROSC count 377, denominator 943 and printed 30.0% do not reconcile within Table 2; the printed percentages also reverse the count-derived direction.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-001, F-ST1-003

**Qualifying route:** Route A, category 3

**Classification rationale:** The inconsistency is within a single REPORT table. Same-article population statements corroborate denominators without adding another relationship.

**Classification ambiguity:** None

**Exact source locations:** REPORT [jama_jabre_2018_oi_180004.pdf — p. 6 Table 2 PP header and Return of spontaneous circulation row](<../jama_jabre_2018_oi_180004.pdf#page=6>); corroborating [p. 4 Figure and Baseline Characteristics paragraph](<../jama_jabre_2018_oi_180004.pdf#page=4>).

**Source evidence:** BMV 342 (34.4%) under n=995; ETI 377 (30.0%) under n=943; BMV−ETI difference −5.6, CI [−9.9,−1.3], P=.01. Figure and population paragraph give the same PP denominators.

**Reported-versus-comparator:** 100×377/943=39.9787911%, versus displayed 30.0%. Count-derived difference is −5.6069318 points, agreeing with −5.6; displayed percentages give 34.4−30.0=+4.4 points.

**Reasoning procedure:** Divide each event count by its printed column denominator and compare its full half-unit range with the percentage range. Compare count-derived and percentage-derived direction without assigning an intended correction.

**Calculation:** ETI inputs [376.5,377.5] and [942.5,943.5] give percentage [39.9046105,40.0530504]%; printed [29.95,30.05]% leaves gap 9.8546105 and relative gap 0.3284870>0.05. BMV range [34.3043697,34.4394168]% overlaps [34.35,34.45]%. Count-derived difference [−5.7486807,−5.4651937] overlaps [−5.65,−5.55]; printed-percentage difference [4.30,4.50] remains positive.

**Affected result or extracted value:** ETI PP ROSC percentage and the apparent direction of the BMV–ETI comparison.

**Why context does not resolve it:** Route A, category 3 retains a within-display count/denominator/percentage discrepancy above 0.05. The associated reversed direction also falls under category 2; corroborating arithmetic does not authorize selecting a replacement field.

**Alternative source-grounded interpretations:** The percentage may refer to another intended population or a substituted reading; the count or denominator might instead be an intended different field. No alternative denominator is supplied for this row.

**Mechanical evidence recheck:** The visible numerator, denominator, percentage, difference and corroborating populations were found and matched. Full interval arithmetic reproduced the mismatch and direction comparison. No arithmetic input is missing; intended row fields or another population and source output remain unspecified. Direct observation is the unreconciled display; a production mechanism and correction are not observed. Classification was confirmed without adjustment.

**Potential downstream evidence impact:** If confirmed, an extractor could copy 30.0% or use displayed percentages to infer a positive BMV–ETI contrast. The card does not assign a replacement value or claim that such extraction occurred.

<a id="C007"></a>
## C007 — Alternative boundary in native and signed SAP copies

Pending Human Adjudication.

**Candidate statement:** The signed SAP H1 line prints a positive +0.01 BMV−TI boundary, whereas the matching native SAP H1 and operational NI rules use −0.01.

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-005, F-ST1-005

**Qualifying route:** Route A, category 2

**Classification rationale:** Both SAP copies and corroborating protocol decision rules are PLAN within one bound plan bundle. The article's margin merely corroborates one side; no P_R conflict is added.

**Classification ambiguity:** The controlling-copy or chronology instruction is unspecified; content roles are clear.

**Exact source locations:** PLAN [joi180004supp1_prod.pdf — p. 121 §4.1 native SAP H1](<../joi180004supp1_prod.pdf#page=121>) and [p. 130 §4.1 signed SAP H1](<../joi180004supp1_prod.pdf#page=130>). Corroborating operational rules [p. 124 §8.2.1](<../joi180004supp1_prod.pdf#page=124>) and [p. 133 signed §8.2.1](<../joi180004supp1_prod.pdf#page=133>); original/final hypotheses [p. 36 §11.2 continuation](<../joi180004supp1_prod.pdf#page=36>) and [p. 90 §11.2](<../joi180004supp1_prod.pdf#page=90>).

**Source evidence:** Native H1 is BMV−TI≥−0.01; the signed image visibly prints BMV−TI≥0.01 without a minus mark. Both H0 lines use ≤−0.01. Both SAP copies have version 1/date 18 February 2015; both operational sections require a lower bound higher than −0.01.

**Reported-versus-comparator:** Signed positive alternative boundary versus native negative boundary and matching negative operational rules. This changes a numerical design reading, rather than an equality convention.

**Reasoning procedure:** Read the signed source image for the sign, align the identical H1 contrast and version/date, and compare with explicit operational rules. Do not infer which boundary was implemented.

**Calculation:** Literal design constants differ by 0.02, or two percentage points. Even treating them as rounded gives [−0.015,−0.005] and [0.005,0.015], gap 0.010 and relative discrepancy 0.010/0.01=1.00>0.05.

**Affected result or extracted value:** The signed primary NI alternative-hypothesis boundary.

**Why context does not resolve it:** Route A, category 2 applies to a sign difference changing a printed numerical decision boundary beyond display precision. Corroborating negative rules do not suppress the signed positive reading.

**Alternative source-grounded interpretations:** A missing sign in the signed line, or a different intended rule not propagated to operational sections, may explain the comparison. Neither establishes which copy controls.

**Mechanical evidence recheck:** All cited lines were found and matched; direct signed-image reading determined +0.01 independently of OCR. Logical comparison and interval gap reproduced. No numeric input is missing; an explicit controlling-copy instruction or amendment is missing. Direct observation is the sign difference, not evidence that the positive rule was applied. PLAN roles and P_P classification were confirmed without adjustment.

**Potential downstream evidence impact:** If confirmed, an extractor could record +0.01 as the planned alternative boundary from the signed copy. The review does not establish implementation of that positive boundary or a change in the published NI conclusion.

<a id="C008"></a>
## C008 — Post-hoc exclusion confidence interval

Pending Human Adjudication.

**Candidate statement:** The eTable 2 ECMO/donation-exclusion interval does not reproduce under an independent-proportion normal/Wald 95% method that reproduces its companion row, beyond full display-precision allowance.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-004

**Qualifying route:** Route A, category 4

**Classification rationale:** Both numerical rows are within the same non-plan REPORT supplement. Article post-hoc descriptions corroborate scope without a conflicting copy and add no S_C relationship.

**Classification ambiguity:** None

**Exact source locations:** REPORT [joi180004supp2_prod.pdf — p. 3 eTable 2 ECMO/donation-exclusion row, companion reclassification row and test footnote](<../joi180004supp2_prod.pdf#page=3>). Corroborating REPORT post-hoc scope: [jama_jabre_2018_oi_180004.pdf — p. 3 methods](<../jama_jabre_2018_oi_180004.pdf#page=3>), [p. 4 continuation](<../jama_jabre_2018_oi_180004.pdf#page=4>) and [p. 6 results pointers](<../jama_jabre_2018_oi_180004.pdf#page=6>).

**Source evidence:** Exclusion row: 43/971 versus 39/978, difference 0.4, CI [−2.2,1.3], P=.63. Companion row: 41/863 versus 45/1174, difference 0.9, CI [−0.9,2.7], P=.31. The footnote identifies chi-square/Fisher P tests without a CI algorithm.

**Reported-versus-comparator:** Independent-proportion 95% calculation gives exclusion CI [−1.342071,2.223459]; companion CI [−0.876733,2.712373] reproduces its printed endpoints.

**Reasoning procedure:** Independently apply d=100(a/n−b/m), s=100√[p(1−p)/n+q(1−q)/m] and d±1.95996398454s within this display. Allow every count/denominator ±0.5 and printed limits ±0.05, using conservative difference/variance bounds as in C005. This does not establish that the authors used Wald intervals or that either CI shares the P-test formula.

**Calculation:** Exclusion lower range [−1.460262,−1.223817] versus printed [−2.25,−2.15] leaves gap 0.689738 and relative gap 0.313517. Upper range [2.105207,2.341652] versus [1.25,1.35] leaves gap 0.755207 and relative gap 0.580928. Companion lower [−0.992603,−0.760774] and upper [2.596445,2.828275] overlap printed ranges [−0.95,−0.85] and [2.65,2.75]. Exclusion difference range [0.333758,0.547632] overlaps [0.35,0.45]. Printed intervals contain their point estimates and zero, consistent with nonsignificant P values; there is no CI/P significance conflict.

**Affected result or extracted value:** Confidence limits for the post-hoc favorable-survival difference after ECMO/donation exclusions.

**Why context does not resolve it:** Route A, category 4 applies because a companion-row reproducing method leaves relative confidence-limit gaps above 0.05. The unspecified actual interval method does not erase the reproduced comparison.

**Alternative source-grounded interpretations:** A distinct unprinted exclusion-row method, input population, or intended limit reading could explain the interval. The companion row supports the reproducing comparison without proving the actual selected algorithm. No common production cause with C005 is established.

**Mechanical evidence recheck:** Both source rows, footnote and all corroborating locations were found and matched. Independent interval arithmetic reproduced both endpoint gaps and companion agreement. Counts, contrast and confidence level are available; actual algorithm, per-row population/method switch and source output are missing. Direct observation is the interval-method mismatch, not an assigned replacement interval or mechanism. Classification was confirmed without adjustment.

**Potential downstream evidence impact:** If confirmed, an extractor could copy the printed post-hoc confidence limits for uncertainty assessment or synthesis. No downstream use, replacement limits or actual conclusion change is established.

## Downstream Evidence-Chain Considerations

Evidence extraction can carry an endpoint definition, analysis population, outcome status, percentage, confidence interval or decision boundary into a structured review record. A confirmed candidate could therefore affect which field is copied or how a comparison is described. Population and contrast metadata should accompany extracted estimates so that distinct ITT, PP, AT, safety and post-hoc results remain identifiable. These observations describe potential relevance only; no propagation into a review, guideline or clinical decision is documented in the supplied package.

## Limitations and Missing Definitions

All source units and assigned relationships are complete. Remaining limitations concern supplied analytic definitions and inputs, rather than unread source pages. C001 lacks participant-linked baseline/day-28 CPC and implemented exception coding. C002 lacks the formal concurrent-versus-changed endpoint-family crosswalk. C003 lacks full AT mapping, promised additional displays and an identified replacement amendment. C004 lacks an explicit intended ordering phrase. C005/C008 lack actual interval algorithms, per-row input/method mappings and calculation outputs. C006 lacks intended field/population mapping for the unreconciled ROSC row. C007 lacks the controlling-copy instruction for the signed/native boundary.

Other completed statistical checks are limited by the unspecified primary NI test formula and 5000-simulation implementation/seed; per-row chi-square/Fisher selection; continuous-outcome dispersion, covariance and exact mean/median-to-test mapping; and numerical futility/recalculation or large-PP/ITT imputation triggers. These missing details alone are not candidates. Model details are not inferred from convention, and crude ratios are not substituted for labeled modeled estimates.

No raw participant data, unsupplied result outputs or external literature were used. Source-matched derivatives are locators and transcription aids; supplied PDF content is authoritative. Historical rendering and secondary OCR provenance are partly incomplete. Local OCR and Office conversion executables are absent, but reusable scan images/OCR and direct CPU Poppler rendering closed all coverage. The full durable limitations record is [limitations.md](review_1_6_2/limitations.md).

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

The [routing preflight](review_1_6_2/routing_preflight.md) records PASS, exact default run model gpt-6.1-sol, CURRENT_SESSION provider, INTERACTIVE_CLI mode and all ten named presets checked against their fixed role matrix. All specialists were fresh distinct spawns. Ordinary specialists used medium effort; statistical, screening, recheck and audit specialists used high effort. The [tooling record](review_1_6_2/tooling_record.md) records CPU, direct Poppler 25.03.0, Pandoc 3.1.11.1 and no fallback environment created. This report stage performs no rendering or new OCR.

Final post-assembly SHA-256 recomputation matches the before-hash records for all three direct sources and all 128 reused artifacts. Before-hash records: [sources](review_1_6_2/source_hashes_before.sha256) and [reused assets](review_1_6_2/reused_artifact_hashes_before.sha256); after-hash records: [sources](review_1_6_2/source_hashes_after.sha256) and [reused assets](review_1_6_2/reused_artifact_hashes_after.sha256). The standalone HTML is rendered by the bundled profile-specific renderer, and final mechanical checks are recorded in [review_validation.json](review_1_6_2/review_validation.json). Scientific evidence and classifications are documented by the [candidate ledger](review_1_6_2/candidate_ledger.md), [mechanical recheck](review_1_6_2/verification/evidence_recheck.md), and [quality audit](review_1_6_2/quality/evidence_quality_audit.md).

### Agent execution

The following is the complete actual 14-agent execution record at report assembly, copied from the [execution manifest](review_1_6_2/agent_execution_manifest.md). Primary artifact paths are relative to review_1_6_2/.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a129ae-36a4-7dd1-b706-3785463a1417 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a129af-e908-7e73-af17-8c17952112f3 | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a129b2-4e97-7b71-ba67-2a7339b3fab3 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a129b2-7db6-7d30-acec-7d2915ec00eb | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_shard_2 | 01a129b2-a1ff-7160-83f9-947c4281ad93 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_002.md |
| support_quantitative_mapper_shard_3 | 01a129b2-cf6b-7012-a167-043a1a698676 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_003.md |
| numeric_consistency_reviewer | 01a129b8-259b-7a33-80f7-0f3ece30aeba | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | 01a129b8-5c9e-7c92-9c17-7a7021494f5f | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a129b8-92ad-7b63-b00a-a605a8e9f04a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | 01a129c7-b779-7032-a642-4c771d89b0b0 | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | 01a129cf-84b6-7100-8632-d270ac1d0646 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a129d5-f792-7cd0-8513-81fd560836b5 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | 01a129dd-b1a8-71d3-9890-7d865e112daf | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | 01a129e5-087a-7262-8048-feac507631de | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

### Reproducibility performance

- **Target basis:** Three supplied PDFs comprise 146 pages, all backed by usable reusable text, OCR, or images. The 134-page plan bundle contains multiple protocol versions, amendments, forms, and scanned SAP pages. Main mapping and three disjoint support shards precede independent numeric, cross-source, and two statistical passes, screening, recheck, audit, and report waves. Native extraction and CPU visual inspection suffice; no new OCR or Office conversion is expected.
- **Total source units:** 146
- **Fresh-source units:** 0
- **Target elapsed minutes:** 45-65
- **Started UTC:** 2026-10-11T06:38:44Z
- **Finished UTC:** 2026-10-11T07:44:10Z
- **Observed elapsed minutes:** 65.43
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Sequential fresh-agent screening, direct-source recheck, second statistical pass, audit and complete eight-card report assembly, followed by final provenance-metadata integration; all 81 statistical relationships and 45 excluded observations received complete records.

Performance fields exactly mirror finalized run_state.md. The initial Markdown assembly was recorded at 07:43:14 UTC (64.50 minutes); this final metadata integration extends the review window to the finish time above. Local HTML rendering, fallback cleanup and mechanical validation follow the finalized review record.
