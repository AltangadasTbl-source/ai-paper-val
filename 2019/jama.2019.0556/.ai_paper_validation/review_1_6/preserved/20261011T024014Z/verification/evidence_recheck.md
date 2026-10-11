# Workflow 1.6 Direct-Source Evidence Recheck

Fresh specialist: `/root/evidence_rechecker`, `qc16_evidence_rechecker`, `gpt-6.1-sol`, reasoning effort `high`, current provider inherited. Assigned and completed IDs: C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017, C018, C019, C020. Every ID remains **Pending Human Adjudication**. This evidence record assigns no severity or final adjudication. Suggested review dispositions below are the mechanical prefill defined by the scope, not decisions.

## Authority and direct inspection

The current ledger and current numeric, cross-source and statistical-pass-1 provenance supplied the comparisons to recheck. QUALITY_CONTROL_SCOPE.md, review_contract.md and tooling_record.md supplied the rules. Supplied PDF physical pages are final authority; native/layout text was used only to locate content. All printed inputs below were visually inspected on source-linked images. Reused images were identity-matched through the current evidence inventory; no old scientific candidate/report artifacts were read. No web, external instrument facts, GPU, Python extraction or source modification was used.

Direct Poppler `pdftoppm` 26.01.0 produced 23 unique CPU-only derivatives at 100 dpi, with command pattern `pdftoppm -f N -l N -singlefile -r 100 -png SOURCE .ai_paper_validation/review_1_6/preprocessing/recheck-PREFIX-pN`. Every invocation selected exactly one physical source page; the batch comprised 23 pages, below 32. The source/derivative assignments are:

- `jama_bot_2019_oi_190007.pdf`: pp1,2 → `preprocessing/recheck-main-p1.png`, `preprocessing/recheck-main-p2.png`.
- `joi190007supp1_prod.pdf`: pp8,9,14,17,18,23,26,28,30,34,35,36,37,43 → `preprocessing/recheck-joi190007supp1-pN.png` for each listed N.
- `joi190007supp2_prod.pdf`: pp2,4 → `preprocessing/recheck-joi190007supp2-pN.png` for each listed N.
- `joi190007supp3_prod.pdf`: pp3,4,5,6,12 → `preprocessing/recheck-joi190007supp3-pN.png` for each listed N.

Also directly viewed: current-run `preprocessing/stats1-main-p4.png`, `preprocessing/stats1-s1-p16.png`; reused `../../document_outputs/DOC-001/rendered_pages/page_003.png`, `page_006.png`, `page_007.png`, `page_008.png`, and `../../document_outputs/DOC-004/rendered_pages/page_016.png`. These are visual derivatives of the supplied pages, not textual final authority. Relative PDF links in this artifact ascend three directories to the package root; page fragments are physical PDF pages. All needed candidate pages were available and readable; no derivative or scientific coverage gap arose.

## Proposed final classification table

Document roles were confirmed from content: observed trial article/results appendices are REPORT; prospective protocol, instrument schedule and analysis plan are PLAN. The table preserves every assigned ID. C009 and C018 receive `record_input_error` because their equality comparisons require unsupported alignment inputs. All other states are `recorded_candidate`; there are no `not_reproduced` or `repaired_residual` states. Primary categories and relationship codes remain as registered, with C009/C018 codes describing the registered comparisons while their applicability remains explicitly conditional.

| ID | Primary category | Relationship type | All relationships | Compared document roles | Review domain | Evidence state | Suggested review disposition |
|---|---|---|---|---|---|---|---|
| C001 | Denominator, proportion, or total inconsistency | S_W | S_W | REPORT main p4 total versus four cell counts | statistical_results | recorded_candidate | retain |
| C002 | Measure, label, or scale inconsistency | S_C | S_C, S_W | REPORT main p3 online BMI label versus REPORT supplement3 p3 online eligibility and main p2 eligibility | report_internal_inconsistency | recorded_candidate | retain |
| C003 | Measure, label, or scale inconsistency | S_W | S_W | REPORT main p6 footnote d versus main p6 footnote f and pp1/7 arm results | report_internal_inconsistency | recorded_candidate | retain |
| C004 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN protocol p16 target difference versus incidence assumptions | plan_material | recorded_candidate | retain |
| C005 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN protocol p9 blood summary versus pp36-37 detailed schedule | plan_material | recorded_candidate | retain |
| C006 | Cross-document numeric inconsistency | P_R | P_R | PLAN protocol p23 intended dose versus REPORT main p2 and supplement3 p4 dose | protocol_report | recorded_candidate | retain |
| C007 | Measure, label, or scale inconsistency | S_C | S_C, S_W | REPORT main p2 and supplement3 p4 declared ratio versus supplement3 p5 assay composition | report_internal_inconsistency | recorded_candidate | retain |
| C008 | Numeric or arithmetic inconsistency | S_W | S_W | REPORT supplement3 p6 food-group count versus its listed recommendations | statistical_results | recorded_candidate | retain |
| C009 | Denominator, proportion, or total inconsistency | S_C | S_C, S_W | REPORT supplement3 p12 blood count-percentage ranges versus REPORT main pp1/3 randomized total; alignment unestablished | statistical_results | record_input_error | discuss |
| C010 | Measure, label, or scale inconsistency | P_P | P_P | PLAN protocol p35 TFEQ-18 instrument label versus item count 21 | plan_material | recorded_candidate | retain |
| C011 | Cross-document numeric inconsistency | P_R | P_R | PLAN protocol p35 questionnaire item count versus REPORT supplement3 p12 questionnaire count | protocol_report | recorded_candidate | retain |
| C012 | Measure, label, or scale inconsistency | S_C | S_C, S_W | REPORT main p6 adherence prose versus main p4 and supplement3 pp12/16 threshold | report_internal_inconsistency | recorded_candidate | retain |
| C013 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN protocol p23 equivalent vitamin D upper limits versus comparative wording | plan_material | recorded_candidate | retain |
| C014 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN protocol p26 initial supply versus p30 initial supply | plan_material | recorded_candidate | retain |
| C015 | Denominator, proportion, or total inconsistency | S_W | S_W | REPORT supplement3 p12 blood-subset maximum versus p16 paired-change N | statistical_results | recorded_candidate | retain |
| C016 | Measure, label, or scale inconsistency | P_R | P_R, P_P | PLAN protocol p28 DSM label versus protocol pp8/34 and REPORT main p4 endpoint label | protocol_report | recorded_candidate | retain |
| C017 | Statistical reporting inconsistency | P_R | P_R, P_P | PLAN protocol pp9/28/43 IDS hierarchy versus protocol p14 and SAP p2 and REPORT main pp4/8 hierarchy | protocol_report | recorded_candidate | retain |
| C018 | Cross-document numeric inconsistency | P_R | P_R | PLAN protocol pp16-17 interaction-power inputs versus REPORT main p4 main-effect-power inputs; alignment unestablished | protocol_report | record_input_error | discuss |
| C019 | Statistical reporting inconsistency | P_R | P_R, P_P | PLAN SAP p4 and protocol p43 Cox-analysis status versus REPORT main pp4/6 post hoc HR label | protocol_report | recorded_candidate | retain |
| C020 | Measure, label, or scale inconsistency | S_W | S_W | REPORT supplement3 pp4/12 product-specific kappa assignments versus p16 footnote | report_internal_inconsistency | recorded_candidate | retain |
| C021 | Measure, label, or scale inconsistency | S_W | S_W | REPORT supplement3 p16 single-asterisk adherence rows versus same-page Morisky footnote and row | report_internal_inconsistency | recorded_candidate | retain |
| C022 | Measure, label, or scale inconsistency | P_P | P_P | PLAN protocol p26 upper product-label tablet dosage vs PLAN protocol p26 upper product-label capsule contents | plan_material | recorded_candidate | retain |

## C001 — Planned total and factorial cell counts

**Location found:** Yes: [main p4, Sample Size](../../../jama_bot_2019_oi_190007.pdf#page=4), REPORT; [main p1, design](../../../jama_bot_2019_oi_190007.pdf#page=1), REPORT, corroborates 2×2 structure.

**Source value/text matched:** Yes: “392 participants (196 in each of the 4 possible intervention combinations)”; 250 per combination after 22% attrition. **Comparator matched:** Yes: four combinations and 196 in each occur in the same sentence.

**Consistency rule applicable:** Yes for the literal whole-trial total/per-cell identity; counts have zero rounding tolerance. **Calculation reproduced:** 4×196=784, which differs from 392 by 392. **Necessary inputs available:** All literal count inputs. **Exact missing inputs/definitions:** Whether 392 denotes one marginal condition rather than the whole trial, and which count unit 196 describes.

**Source-grounded alternative:** The sentence says power for the main effect of each intervention; 392 could be a two-cell marginal quantity. **Direct observation versus inferred explanation:** The printed total/cell wording and arithmetic are observed/reproduced; a marginal-count explanation is inferred, not established. **Exact human question:** What population unit does each of 392 and 196 count, and how should the four-combination parenthetical be understood?

**Classification confirmation:** S_W only, within the trial REPORT; PLAN factorial descriptions corroborate structure and add no P_R edge. Category/domain as table. **Classification ambiguity:** Count unit, not document role. **Evidence state:** `recorded_candidate`, determined by the directly printed nonreconciling literal identity; the named unit question remains. **Suggested review disposition:** `retain`. **Status:** Pending Human Adjudication.

## C002 — Online BMI lower threshold

**Location found:** Yes: [main p3 Figure 1](../../../jama_bot_2019_oi_190007.pdf#page=3), [main p2 eligibility](../../../jama_bot_2019_oi_190007.pdf#page=2), [supplement3 p3 eligibility](../../../joi190007supp3_prod.pdf#page=3); all REPORT.

**Source value/text matched:** Yes: 1451 online exclusions labelled BMI <15 or >40. **Comparator matched:** Yes: main inclusion 25–40; supplement explicitly states online inclusion 25–40; telephone flow lists 18 exclusions for BMI <25.

**Consistency rule applicable:** Yes as a mismatch between descriptions of the online lower eligibility threshold; correspondence to actual exclusions remains conditional. **Calculation reproduced:** 25−15=10 kg/m². **Necessary inputs available:** Thresholds, stage labels and linked count. **Exact missing inputs/definitions:** Actual online algorithm, stage-specific exceptions and BMI distribution for the 1451.

**Source-grounded alternative:** Telephone screening confirms eligibility after online screening, so deliberately broader prescreening could account for the figure. However supplement p3 explicitly calls 25–40 an online-screen inclusion criterion. **Direct observation versus inferred explanation:** Conflicting threshold labels are observed; a typo or staged algorithm is inferred. No participant misclassification is established. **Exact human question:** Which threshold produced the 1451 exclusions, and how does any intentional <15 prescreen reconcile with the stated online 25–40 inclusion rule?

**Classification confirmation:** S_C and S_W, primary S_C by precedence; protocol eligibility is only corroborative. **Classification ambiguity:** Screening-stage rules. **Evidence state:** `recorded_candidate`, determined by confirmed conflicting online labels pending that named definition. **Suggested review disposition:** `retain`. **Status:** Pending Human Adjudication.

## C003 — Duplicated therapy label for 22 cases

**Location found:** Yes: [main p6 Table 2 footnotes d/f](../../../jama_bot_2019_oi_190007.pdf#page=6), [main p1 abstract](../../../jama_bot_2019_oi_190007.pdf#page=1), [main p7 onset narrative](../../../jama_bot_2019_oi_190007.pdf#page=7); all REPORT.

**Source value/text matched:** Yes: footnote d assigns 32/256 (12.5%) and 22/256 (8.6%) both to supplements “without therapy.” **Comparator matched:** Yes: footnote f and abstract/narrative assign 22/256 to supplements with therapy and 32/256 to supplements alone.

**Consistency rule applicable:** Yes: matching arm/time/outcome labels for the same 22 events. **Calculation reproduced:** 32/256=12.5%; 22/256=8.59375% →8.6%; the percentages reconcile but therapy labels conflict. **Necessary inputs available:** Counts, denominators, labels and one-year event identity. **Exact missing inputs/definitions:** None for the observed wording conflict; author confirmation of intended footnote label remains.

**Source-grounded alternative:** Adjacent footnote f supplies a consistent distinct therapy-arm label; copied wording could explain d. **Direct observation versus inferred explanation:** Duplicate “without therapy” and comparator “with therapy” are observed; a copying mechanism is inferred. **Exact human question:** Which therapy label should accompany 22/256 in footnote d?

**Classification confirmation:** S_W only; all compared statements are inside one REPORT. **Classification ambiguity:** None in role/relationship. **Evidence state:** `recorded_candidate`, determined by direct duplicate arm-label mismatch. **Suggested review disposition:** `retain`. **Status:** Pending Human Adjudication.

## C004 — Plan percentage contrast definition

**Location found:** Yes: [protocol p16 §4.4](../../../joi190007supp1_prod.pdf#page=16), PLAN.

**Source value/text matched:** Yes: “difference of 25%” in cumulative incidence; control 30%, intervention 15%. **Comparator matched:** Yes: these quantities occur consecutively in the same calculation description, followed by additive-interaction power, 180/group, alpha .05 and power .90.

**Consistency rule applicable:** Yes conditionally to ordinary absolute or control-relative definitions; the intended contrast is not stated. **Calculation reproduced:** 30−15=15 percentage points; (30−15)/30=50% relative reduction. Neither equals 25%; ordinary displayed-percent rounding does not bridge the difference. **Necessary inputs available:** Three printed percentages. **Exact missing inputs/definitions:** Contrast, denominator and factorial risks defining 25%; full power formula not supplied and not reconstructed.

**Source-grounded alternative:** The paragraph discusses additive interaction, and p17 distinguishes synergistic pure-treatment-group comparisons. The 25% could refer to a different contrast. **Direct observation versus inferred explanation:** Printed quantities and ordinary contrast diagnostics are observed/reproduced; their intentional relationship is unresolved. **Exact human question:** What contrast and denominator define 25%, and how do they connect to control 30% and intervention 15%?

**Classification confirmation:** P_P only, inside one PLAN. **Classification ambiguity:** Power contrast, not document role. **Evidence state:** `recorded_candidate`, determined by the registered definition discrepancy remaining with its named missing contrast. **Suggested review disposition:** `retain`. **Status:** Pending Human Adjudication.

## C005 — Blood volume summary versus detailed schedule

**Location found:** Yes: [protocol p9 burden](../../../joi190007supp1_prod.pdf#page=9), [p36 Blood schedule](../../../joi190007supp1_prod.pdf#page=36), [p37 volume table/footnotes](../../../joi190007supp1_prod.pdf#page=37); all PLAN.

**Source value/text matched:** Yes: summary 3×6 mL and 2×8.5 mL at baseline/6/12 months. **Comparator matched:** Yes: detail lists 17,6,2,6,6 mL and prints 37 mL at each wave. The DNA 6 mL row carries the funding condition.

**Consistency rule applicable:** Yes for nominal totals at the matching waves. **Calculation reproduced:** 18+17=35; 17+6+2+6+6=37; difference 2 mL. Without conditional DNA, detail gives 31 mL, not 35. **Necessary inputs available:** Volumes, timing and funding footnote. **Exact missing inputs/definitions:** Summary scope, actual funded tube set and any amended collection schedule.

**Source-grounded alternative:** Omitting the 2 mL hematology tube produces the summary total; the source also identifies conditional DNA funding, although that alone does not produce 35. **Direct observation versus inferred explanation:** Totals/tubes/timing are observed; hematology omission or schedule change is inferred. Actual collection is unknown. **Exact human question:** Which tube set does the summary represent, and did the 2 mL hematology tube belong to baseline/6/12 collections?

**Classification confirmation:** P_P only. **Classification ambiguity:** Collection/funding scope. **Evidence state:** `recorded_candidate`, determined by confirmed nominal 35 versus 37 at the same scheduled waves. **Suggested review disposition:** `retain`. **Status:** Pending Human Adjudication.

## C006 — Intended and reported daily EPA+DHA dose

**Location found:** Yes: [protocol p23 Omega-3](../../../joi190007supp1_prod.pdf#page=23), [pp8](../../../joi190007supp1_prod.pdf#page=8)/[18](../../../joi190007supp1_prod.pdf#page=18) capsule composition, [p26 product label](../../../joi190007supp1_prod.pdf#page=26), all PLAN; [main p2 intervention](../../../jama_bot_2019_oi_190007.pdf#page=2) and [supplement3 p4 composition](../../../joi190007supp3_prod.pdf#page=4), REPORT.

**Source value/text matched:** Yes: p23 expressly says intended dose EPA+DHA=1.0 g/day. **Comparator matched:** Yes: both REPORT locations expressly describe 1412 mg EPA+DHA daily; pp8/18 say 1000 mg per capsule. Newly inspected protocol p26 label describes 1412 mg fish oil, at least 65% EPA and at least 10% DHA.

**Consistency rule applicable:** Yes to the two declared active daily masses, with a mass-basis question. **Calculation reproduced:** 1 g=1000 mg; 1412−1000=412 mg/day; 412/1000=41.2%. **Necessary inputs available:** Declared masses and daily dosing. **Exact missing inputs/definitions:** Delivered active-fatty-acid versus total fish-oil basis, final formulation/assay, and applicable amendment. Product tolerance is not assumed to apply to EPA+DHA.

**Source-grounded alternative:** The p26 label directly supplies a plausible total-fish-oil versus active-fatty-acid distinction: the same 1412 mg appears as fish oil in PLAN and EPA+DHA in REPORT. Minimum EPA/DHA percentages do not establish an exact active daily dose. **Direct observation versus inferred explanation:** Differing declared active doses and label basis are observed; a basis transcription or formulation change is inferred. **Exact human question:** Does 1412 mg denote fish oil or EPA+DHA in the administered product, and what final dose/amendment reconciles it with intended 1.0 g EPA+DHA?

**Classification confirmation:** P_R only for the registered dose discrepancy. Agreeing REPORT descriptions add no S_C; the p26 label is an alternative/basis locator, not an extra discrepancy edge with its minimum percentages. **Classification ambiguity:** Final mass basis and amendment. **Evidence state:** `recorded_candidate`, determined by confirmed differing active-dose declarations. **Suggested review disposition:** `retain`. **Status:** Pending Human Adjudication.

## C007 — Ratio declaration versus assay composition

**Location found:** Yes: [main p2](../../../jama_bot_2019_oi_190007.pdf#page=2), [supplement3 p4](../../../joi190007supp3_prod.pdf#page=4), [supplement3 p5 laboratory paragraph](../../../joi190007supp3_prod.pdf#page=5); all REPORT.

**Source value/text matched:** Yes: EPA:DHA ratio 3:1. **Comparator matched:** Yes: laboratory EPA mean 67.9 g/100 g FAME (SD .85), DHA 14.6 g/100 g FAME (SD 1.55), duplicate tests of six supplements; paragraph calls contents tested and confirmed.

**Consistency rule applicable:** Yes to a common-denominator ratio of displayed assay means; its equivalence to declared parent-fatty-acid mass ratio is conditional. **Calculation reproduced:** 67.9/14.6=4.650685; rounding inputs to nearest .1 yields approximately 4.6314–4.6701, excluding 3. This is ratio of means, not mean capsule ratio. **Necessary inputs available:** Nominal ratio, assay means/units and testing description. **Exact missing inputs/definitions:** Nominal versus assayed lot basis and FAME-to-parent-fatty-acid mass correspondence; individual capsule values and conversion factors are unavailable.

**Source-grounded alternative:** Declared formulation and assayed FAME may use different mass or lot bases. **Direct observation versus inferred explanation:** Shared FAME denominator and displayed ratio diagnostic are reproduced; their chemical/formulation reconciliation is not established. **Exact human question:** What basis defines 3:1, and how does that declaration relate to 67.9/14.6 on the assay's FAME basis?

**Classification confirmation:** S_C and S_W; main-to-assay and supplement-internal comparisons genuinely contrast nominal and laboratory values. PLAN minimum compositions are context only. **Classification ambiguity:** Mass/lot correspondence. **Evidence state:** `recorded_candidate`, determined by the registered ratio comparison remaining pending its named basis definition. **Suggested review disposition:** `retain`. **Status:** Pending Human Adjudication.

## C008 — Count of dietary recommendation groups

**Location found:** Yes: [supplement3 p6 dietary advice](../../../joi190007supp3_prod.pdf#page=6), REPORT.

**Source value/text matched:** Yes: “ten different food groups.” **Comparator matched:** Yes: vegetables, fruit, fish, meat, pulses or legumes, whole grains, low-fat dairy, olive oil, processed foods, soft drinks, alcoholic beverages appear in the ensuing list.

**Consistency rule applicable:** Yes under distinct-category counting; synonymous pulses/legumes count once. **Calculation reproduced:** Eleven listed recommendation categories versus ten stated; difference one. **Necessary inputs available:** Count word and full list. **Exact missing inputs/definitions:** Grouping rule, whether alcohol is outside the counted groups, or whether two listed categories form one group.

**Source-grounded alternative:** Alcohol might be advice outside the food-group count, or categories may be combined. Supplement p12's eleven-group score is a distinct scoring description and does not define the counseling taxonomy. **Direct observation versus inferred explanation:** Stated ten and eleven-category list are observed; grouping/exception explanation is inferred. **Exact human question:** Which listed categories form the ten groups, and is any listed recommendation intentionally outside that count?

**Classification confirmation:** S_W only. The score's eleven components supply context, not a second discrepancy relationship; no S_C or PLAN edge. **Classification ambiguity:** Grouping convention. **Evidence state:** `recorded_candidate`, determined by confirmed count/list tension with the named grouping definition missing. **Suggested review disposition:** `retain`. **Status:** Pending Human Adjudication.

## C009 — Blood count and percentage ranges

**Location found:** Yes: [supplement3 p12 blood paragraph](../../../joi190007supp3_prod.pdf#page=12), [main p1](../../../jama_bot_2019_oi_190007.pdf#page=1)/[p3](../../../jama_bot_2019_oi_190007.pdf#page=3) randomized total; all REPORT.

**Source value/text matched:** Yes: “At baseline and 12 months” subset “n=211 to 331, 22-32%” for serum selenium, folic acid and vitamin D. **Comparator matched:** Yes: 1025 randomized. The blood paragraph does not identify a denominator or pair each count endpoint to a percentage endpoint.

**Consistency rule applicable:** Only conditionally; the necessary common-denominator/endpoint alignment is unestablished. **Calculation reproduced:** Under D=1025, 211/D=20.585%→21% and 331/D=32.293%→32%. Under common integer D and paired endpoint rounding, 211→22% requires D=938–981; 331→32% requires D=1019–1050. No common D exists under that assumed pairing. **Necessary inputs available:** Printed ranges and whole-trial total. **Exact missing inputs/definitions:** Denominator by wave/analyte, endpoint pairing and definition of each percentage's eligible population.

**Source-grounded alternative:** The range covers baseline and 12 months plus three analytes; distinct wave/analyte denominators can generate different percentages, and count/percentage range endpoints need not be paired. **Direct observation versus inferred explanation:** The ranges and randomized total are observed; mapping 211 to 22% and all blood percentages to 1025 is an unsupported inference. **Exact human question:** Which wave/analyte numerator-denominator pairs generated the two ranges, and do their endpoints correspond?

**Classification confirmation:** The registered comparisons are S_C and S_W, primary S_C; role assignment is confirmed, but the presence of a substantive discrepancy is conditional on missing alignment. **Classification ambiguity:** Endpoint/population correspondence. **Evidence state:** `record_input_error`, determined by absent denominator/pairing inputs rather than a misread number. The diagnostic cannot establish the registered mismatch without them, nor can the package settle a residual discrepancy. **Suggested review disposition:** `discuss`. **Status:** Pending Human Adjudication.

## C010 — TFEQ label and item count

**Location found:** Yes: [protocol p35 questionnaire table](../../../joi190007supp1_prod.pdf#page=35), [p28 instrument designation](../../../joi190007supp1_prod.pdf#page=28), PLAN; [main p4 TFEQ-R18](../../../jama_bot_2019_oi_190007.pdf#page=4), REPORT, corroboration only.

**Source value/text matched:** Yes: TFEQ-18 row. **Comparator matched:** Yes: its “No items” cell is 21, correctly aligned to that row. Neighboring PHQ-9/9, IDS-SR30/30 and GAD-7/7 support the local suffix/count convention.

**Consistency rule applicable:** Conditional label/count diagnostic supported by neighboring rows; no external questionnaire definition is assumed. **Calculation reproduced:** 21−18=3. **Necessary inputs available:** Instrument label, row alignment, explicit item count and local convention. **Exact missing inputs/definitions:** Whether 18 is the scored-item count, whether three local items were added, and administered instrument version.

**Source-grounded alternative:** Eighteen scored items plus three supplementary questions, or a different version, could account for 21. **Direct observation versus inferred explanation:** Correct row label/count are observed; suffix-as-item-count and extension mechanism remain diagnostic explanations. **Exact human question:** Which instrument/version and administered-versus-scored item counts do TFEQ-18 and 21 describe?

**Classification confirmation:** P_P only. Main R18 corroborates one side and has no conflicting explicit administered count, so it does not create P_R. **Classification ambiguity:** Instrument naming convention/extension. **Evidence state:** `recorded_candidate`, determined by the registered PLAN table-label/item-count question remaining with its named definition. **Suggested review disposition:** `retain`. **Status:** Pending Human Adjudication.

## C011 — GA2LEN planned and reported item counts

**Location found:** Yes: [protocol p35 FFQ-GA2LEN row](../../../joi190007supp1_prod.pdf#page=35), PLAN; [supplement3 p12 dietary measures](../../../joi190007supp3_prod.pdf#page=12), REPORT.

**Source value/text matched:** Yes: FFQ-GA2LEN item count 264. **Comparator matched:** Yes: “250-item GA2LEN food frequency questionnaire”; eleven-group diet quality score 0–77.

**Consistency rule applicable:** Yes to the same named trial questionnaire count, pending version/count basis. **Calculation reproduced:** 264−250=14 items. **Necessary inputs available:** Questionnaire identity, explicit counts and trial context. **Exact missing inputs/definitions:** Food items versus all questions, local/site version, modifications and administered/scored subset.

**Source-grounded alternative:** Fourteen nonfood or local items, an adapted version or a revision could explain the count descriptions. **Direct observation versus inferred explanation:** Named instrument and two counts are observed; reason for differing count basis is inferred. No score arithmetic error is established. **Exact human question:** What item/version basis connects the planned 264-item instrument with the reported 250-item questionnaire?

**Classification confirmation:** P_R only; prospective instrument table versus retrospective trial measure description. **Classification ambiguity:** Version/count basis. **Evidence state:** `recorded_candidate`, determined by confirmed differing explicit counts for the named measure with a bounded version question. **Suggested review disposition:** `retain`. **Status:** Pending Human Adjudication.

## C012 — Adherence threshold inequality

**Location found:** Yes: [main p4 Other Measures](../../../jama_bot_2019_oi_190007.pdf#page=4), [main p6 adherence narrative](../../../jama_bot_2019_oi_190007.pdf#page=6), [supplement3 p12 definition](../../../joi190007supp3_prod.pdf#page=12), [p16 adherence rows](../../../joi190007supp3_prod.pdf#page=16), REPORT; [SAP p4](../../../joi190007supp2_prod.pdf#page=4), PLAN, corroboration only.

**Source value/text matched:** Yes: a priori ≥70% in main p4/supplement p12; table multinutrient pill-weight row ≥70%, N666, counts 135,134,126,120. **Comparator matched:** Yes: main p6 says 77% had “more than 70%” adherence. SAP “At least 70%” supports the inclusive side only.

**Consistency rule applicable:** Yes to inclusive versus strict threshold labels. **Calculation reproduced:** 135+134+126+120=515; 515/666=77.327%→77%. Exactly 70% satisfies ≥70% but fails >70%. **Necessary inputs available:** Threshold wording/counts/denominator. **Exact missing inputs/definitions:** Exact-boundary participants and implemented inequality; the p6 summary's precise product/aggregation provenance is not stated.

**Source-grounded alternative:** Informal “more than” wording or no boundary cases could preserve the same 77%; matching rounded summaries alone does not prove identical computation. **Direct observation versus inferred explanation:** Different inequality wording and arithmetic are observed; any participant inclusion/count impact is unestablished. **Exact human question:** Which inequality generated the reported adherence summary, and were any participants exactly at 70%?

**Classification confirmation:** S_C and S_W, primary S_C. SAP corroboration is not a P_R discrepancy. **Classification ambiguity:** Actual boundary implementation and summary mapping. **Evidence state:** `recorded_candidate`, determined by confirmed differing threshold labels, independent of an unclaimed count effect. **Suggested review disposition:** `retain`. **Status:** Pending Human Adjudication.

## C013 — Vitamin D upper-limit comparison

**Location found:** Yes: [protocol p23 Vitamin D paragraph](../../../joi190007supp1_prod.pdf#page=23), PLAN.

**Source value/text matched:** Yes: 20 μg or 800 IU; well below 4000 IU/day and “even more below” 100 μg/day. **Comparator matched:** Yes: both limits and the dose conversion occur in the same paragraph.

**Consistency rule applicable:** Yes if the comparative phrase states quantitative distance, using the supplied equivalence alone. **Calculation reproduced:** 800/20=40 IU/μg; 4000 IU=100 μg. The dose is 20% of either limit, 80% below either. **Necessary inputs available:** Supplied conversion and limits. **Exact missing inputs/definitions:** Whether comparative wording is quantitative or rhetorical, or whether a limit/unit was transcribed differently than intended.

**Source-grounded alternative:** The sentence names different authorities; “even more” might be rhetorical emphasis rather than a second larger numeric limit. **Direct observation versus inferred explanation:** Equal numeric limits are reproduced; rhetorical meaning is inferred and unresolved. No clinical safety judgment follows. **Exact human question:** Are the stated limits intended to be equal, and what quantitative meaning was intended by “even more below”?

**Classification confirmation:** P_P only. **Classification ambiguity:** Quantitative versus rhetorical comparison. **Evidence state:** `recorded_candidate`, determined by registered comparative wording remaining despite equal supplied-source converted limits. **Suggested review disposition:** `retain`. **Status:** Pending Human Adjudication.

## C014 — Baseline supplement supply duration

**Location found:** Yes: [protocol p26 §6.5](../../../joi190007supp1_prod.pdf#page=26), [protocol p30 baseline procedure](../../../joi190007supp1_prod.pdf#page=30); both PLAN.

**Source value/text matched:** Yes: 13-week supply at baseline and months 3,6,9. **Comparator matched:** Yes: after baseline randomization participants receive a “4 month supply”; follow-ups at months 3,6,12 are described.

**Consistency rule applicable:** Yes for baseline supply quantity under ordinary duration meanings. **Calculation reproduced:** 13 weeks=91 days; even four 28-day months=112 days, longer by at least 21 days. **Necessary inputs available:** Baseline identity and two durations. **Exact missing inputs/definitions:** Buffer/exception, operational month convention, actual dispensing count and amendment chronology.

**Source-grounded alternative:** Four months might include a baseline buffer before the month-3 resupply. **Direct observation versus inferred explanation:** Two baseline quantities are observed; buffer or altered procedure is inferred. **Exact human question:** Was the baseline package 13 weeks or four months, and was baseline an intentional exception to the regular supply schedule?

**Classification confirmation:** P_P only; both locations occur inside the same prospective PLAN, so category remains numeric/arithmetic. **Classification ambiguity:** Operational buffer/version. **Evidence state:** `recorded_candidate`, determined by directly differing baseline duration descriptions. **Suggested review disposition:** `retain`. **Status:** Pending Human Adjudication.

## C015 — Serum change count exceeds subset maximum

**Location found:** Yes: [supplement3 p12 blood subset](../../../joi190007supp3_prod.pdf#page=12), [p16 serum-change rows](../../../joi190007supp3_prod.pdf#page=16); both REPORT.

**Source value/text matched:** Yes: baseline/12-month blood subset n211–331 for selenium, folic acid and vitamin D. **Comparator matched:** Yes: T12−T0 changes for those same three analytes each have N335. EPA N334 is separate and unnecessary to this comparison.

**Consistency rule applicable:** Yes conditionally for observed paired changes from the same described subset: number of pairs cannot exceed either wave's count. **Calculation reproduced:** 335>331 by 4. **Necessary inputs available:** Explicit named analytes, timing and counts. **Exact missing inputs/definitions:** Per-wave measured counts, pairing/imputation rule, whether N335 includes different pooled participants, and scope of the n211–331 range.

**Source-grounded alternative:** A broader change-analysis sample, imputed measurements or range scope narrower than the change rows could explain 335. The main article's primary/secondary inferential imputation methods do not establish that this descriptive blood table is imputed. **Direct observation versus inferred explanation:** Count ordering and matched analyte/time labels are observed; raw paired-sample interpretation and any mechanism are conditional. **Exact human question:** What measurement/participant rule generates N335 changes, and how does that sample relate to the stated blood subset maximum331?

**Classification confirmation:** S_W only, inside one REPORT. **Classification ambiguity:** Pairing/population/imputation definition. **Evidence state:** `recorded_candidate`, determined by confirmed aligned analyte/time count tension remaining as registered pending its named sample definition. Unlike C009, no unspecified count/percentage endpoint pairing is introduced. **Suggested review disposition:** `retain`. **Status:** Pending Human Adjudication.

## C016 — MDD diagnostic version labels

**Location found:** Yes: [protocol p28 primary endpoint](../../../joi190007supp1_prod.pdf#page=28), [p8 main endpoint](../../../joi190007supp1_prod.pdf#page=8), [p34 MINI table](../../../joi190007supp1_prod.pdf#page=34), PLAN; [main p4 primary outcome](../../../jama_bot_2019_oi_190007.pdf#page=4), REPORT.

**Source value/text matched:** Yes: p28 says DSM-5 and MINI V5.0 with superscript citation 1. **Comparator matched:** Yes: p8/p34 say DSM-IV; main p4 says Diagnostic and Statistical Manual Fourth Edition and MINI5.0. The ledger's literal “MINI V5.01” conflates V5.0 with citation marker1; the DSM-5 versus DSM-IV comparison remains unchanged.

**Consistency rule applicable:** Yes to diagnostic criterion/version labels of the same 12-month MDD endpoint. **Logical comparison reproduced:** DSM-5 differs from DSM-IV; MINI version 5.0 does not itself conflict after separating the superscript. **Necessary inputs available:** Same endpoint, criterion labels, measure/time identity. **Exact missing inputs/definitions:** Approved final criteria/amendment and version actually used to define the 105 reported onsets.

**Source-grounded alternative:** A criterion-version wording defect or amendment could explain the different labels. **Direct observation versus inferred explanation:** DSM label mismatch is directly observed; actual differing diagnosis counts are not established. **Exact human question:** Which DSM criterion and MINI instrument version governed the approved endpoint and reported onsets, and how should the conflicting PLAN wording be interpreted?

**Classification confirmation:** P_R and P_P, primary P_R by precedence. Criterion mismatch is PLAN/REPORT and PLAN-internal. **Classification ambiguity:** Applicable final amendment, not roles. **Evidence state:** `recorded_candidate`, determined by the unchanged direct DSM-label contradiction. Separating the citation corrects ancillary transcription without creating a different residual question, so it does not require `repaired_residual`. **Suggested review disposition:** `retain`. **Status:** Pending Human Adjudication.

## C017 — IDS outcome-priority framing

**Location found:** Yes: [protocol p9 continuation](../../../joi190007supp1_prod.pdf#page=9), [p28 main parameters](../../../joi190007supp1_prod.pdf#page=28), [p43 primary analyses](../../../joi190007supp1_prod.pdf#page=43), [p14 secondary objective](../../../joi190007supp1_prod.pdf#page=14), [SAP p2 outcome hierarchy](../../../joi190007supp2_prod.pdf#page=2), PLAN; [main p4 secondary outcomes/statistical methods](../../../jama_bot_2019_oi_190007.pdf#page=4), [p8 Table3](../../../jama_bot_2019_oi_190007.pdf#page=8), REPORT.

**Source value/text matched:** Yes: IDS sits under p28 main endpoints and p43 Primary study parameters; p9 continues p8's main-parameter list and is not a secondary comparator. **Comparator matched:** Yes: p14 places depressive symptom scores among secondary outcomes; SAP explicitly labels IDS secondary; main describes IDS as secondary and secondary analyses as exploratory. Table3 IDS supplement effect .60 (.15–1.05), P.01 overall and .36 (−.19–.90), P.20 at12months are directly confirmed in the MAIN report, not a required supplement location.

**Consistency rule applicable:** Yes to the framing of the same IDS inferential outcome; formal meaning of “main” remains a named limitation, but p43 explicitly uses “Primary.” **Logical comparison reproduced:** PLAN main/primary versus PLAN and REPORT secondary. **Necessary inputs available:** IDS identity, hierarchy headers and reported statistics. **Exact missing inputs/definitions:** Final operative hierarchy, chronology and whether operational main parameters were intended as formal primary endpoints.

**Source-grounded alternative:** SAP may refine earlier hierarchy; p14's broad secondary objective may differ from operational parameter grouping. **Direct observation versus inferred explanation:** Conflicting hierarchy descriptions are observed; a disclosed amendment or informal operational use is not proven. **Exact human question:** Which final hierarchy governed these IDS statistics, and what do the protocol's main/primary labels mean relative to SAP/report secondary framing?

**Classification confirmation:** P_R and P_P, primary P_R. p9 is confirmed on the main-side only. The exact IDS numbers are located on main p8; this refines the ledger's generic “supplement” attribution without changing the registered hierarchy comparison. **Classification ambiguity:** Main-versus-formal-primary meaning and plan chronology. **Evidence state:** `recorded_candidate`, determined by confirmed hierarchy-label comparison with explicitly primary PLAN analysis text. **Suggested review disposition:** `retain`. **Status:** Pending Human Adjudication.

## C018 — Differently targeted power calculations

**Location found:** Yes: [protocol p16 calculation](../../../joi190007supp1_prod.pdf#page=16), [p17 continuation](../../../joi190007supp1_prod.pdf#page=17), PLAN; [main p4 sample size](../../../jama_bot_2019_oi_190007.pdf#page=4), REPORT.

**Source value/text matched:** Yes: PLAN control30%, intervention15%, 180/group, 20% dropout, .90 additive-interaction power; continuation describes 80% power for pure treatment groups if synergistic. **Comparator matched:** Yes: REPORT control30%, active20%, 196 in each printed combination,22% attrition,.90 power for each intervention's main effect; both state target250 per arm/combination.

**Consistency rule applicable:** No unconditional matched-power-input identity is established: the sources expressly target interaction versus main effects. **Calculation reproduced:** Numeric differences are 5 percentage points for active incidence,2 for attrition and16 for analyzable-group counts. These are descriptions of different calculations unless an operative-calculation alignment is supplied. **Necessary inputs available:** Printed inputs and, crucially, different contrast labels. **Exact missing inputs/definitions:** Same-governing-calculation identity, dated calculation/amendment sequence, factorial cell risk definitions and derivation connecting contrast-specific counts.

**Source-grounded alternative:** Interaction and main-effect calculations may legitimately use different risk assumptions or input summaries while producing the same recruitment target. This is supported by their explicit contrast descriptions, not merely conjectured. **Direct observation versus inferred explanation:** Input differences and contrast differences are observed; treating them as a contradiction in one matched calculation is an unsupported inference. **Exact human question:** Which dated calculation governed recruitment, and how do the distinct interaction and main-effect power scenarios map to that target?

**Classification confirmation:** The registered PLAN/REPORT comparison is P_R only, with its discrepancy applicability conditional; no PLAN-internal edge is added from the explicitly separate synergistic scenario. **Classification ambiguity:** Estimand and operative-calculation alignment. **Evidence state:** `record_input_error`, determined by the source-grounded break in assumed same-calculation alignment. The package cannot settle a residual mismatch; it does not prove the two inputs must reconcile. **Suggested review disposition:** `discuss`. **Status:** Pending Human Adjudication.

## C019 — Planned Cox analyses and post hoc label

**Location found:** Yes: [SAP p4 Secondary analysis](../../../joi190007supp2_prod.pdf#page=4), [protocol p43 Primary study parameters](../../../joi190007supp1_prod.pdf#page=43), PLAN; [main p4 statistical methods](../../../jama_bot_2019_oi_190007.pdf#page=4), [main p6 Table2](../../../jama_bot_2019_oi_190007.pdf#page=6), REPORT.

**Source value/text matched:** Yes: SAP explicitly proposes Cox regression for time to MDD with HR,95%CI,P values as secondary analysis; protocol specifies Cox time-to-event analysis under primary parameters. **Comparator matched:** Yes: main methods call Cox time-to-first-MDD analyses post hoc; Table2 header “Post Hoc Outcome: Time to MDD Onset” accompanies HR1.05(.86–1.27),.91(.75–1.10),interaction.91(.75–1.11).

**Consistency rule applicable:** Yes to generic planned-versus-post-hoc status labels for same time-to-MDD/Cox output; precise implementation and chronology remain conditional. **Logical comparison reproduced:** Planned secondary/primary Cox status differs from reported post hoc status; protocol/SAP also differ in primary/secondary framing. **Necessary inputs available:** Named outcome, Cox method, proposed/reported status and actual HR output. **Exact missing inputs/definitions:** Dated SAP approval/finalization, exact model/censoring/contrast configuration intended prospectively, and whether “post hoc” modifies outcome or a specific implementation.

**Source-grounded alternative:** The reported configuration may be a later variant of a general planned Cox analysis; SAP chronology could affect prespecification status. **Direct observation versus inferred explanation:** Generic method/status discrepancy is observed; exact prespecification identity is not adjudicated. **Exact human question:** Was this exact HR model/censoring configuration planned, and what specifically does the report's post hoc label modify?

**Classification confirmation:** P_R and P_P, primary P_R; both status comparisons are substantive, unlike a merely corroborating plan. **Classification ambiguity:** SAP chronology and exact implementation identity. **Evidence state:** `recorded_candidate`, determined by explicit generic Cox/status label comparison remaining with the named implementation question. **Suggested review disposition:** `retain`. **Status:** Pending Human Adjudication.

## C020 — Product identities assigned to kappas

**Location found:** Yes: [supplement3 p4 product definitions](../../../joi190007supp3_prod.pdf#page=4), [p12 adherence paragraph](../../../joi190007supp3_prod.pdf#page=12), [p16 table footnote](../../../joi190007supp3_prod.pdf#page=16); all REPORT.

**Source value/text matched:** Yes: product1 is omega-3 oil, product2 the selenium/folate/vitamin-D/calcium pill; p12 says kappas .73 and .70 for supplements1 and2 respectively. **Comparator matched:** Yes: p16 footnote says multinutrient=.73 and omega=.70 for pill-weight/self-report agreement, alongside distinct multinutrient and omega adherence rows.

**Consistency rule applicable:** Yes to identity of the same product-specific agreement statistics, pending any separately defined aggregate meaning. **Logical comparison reproduced:** Prose implies omega .73 and micronutrient pill .70; footnote assigns omega .70 and multinutrient .73. The omega assignment itself differs by .03; values are not altered by arithmetic.

**Necessary inputs available:** Explicit product numbering, respective mapping, footnote labels and agreement description. **Exact missing inputs/definitions:** Whether table multinutrient means product2 or a combined product measure, agreement populations/aggregation and which mapping is intended.

**Source-grounded alternative:** A combined multinutrient measure or different agreement aggregation could explain a difference; the shared omega identity and same agreement wording still require clarification. A swapped respective/footnote label is another inferred mechanism. **Direct observation versus inferred explanation:** Product/value mappings are observed; cause and corrected mapping are not established. **Exact human question:** Which kappa belongs to each product for the stated weight/self-report comparison, and do prose and footnote use the same population and aggregation?

**Classification confirmation:** S_W only. Product-definition p4 establishes identity inside the same REPORT; it does not create another discrepancy edge. **Classification ambiguity:** Multinutrient aggregation and matched denominators. **Evidence state:** `recorded_candidate`, determined by confirmed conflicting omega/product kappa labels. **Suggested review disposition:** `retain`. **Status:** Pending Human Adjudication.

## Completion and bounded limitations

All 20 assigned IDs received separate source/comparator/rule/input/alternative/question/state records and classifications. State counts: recorded_candidate 18; record_input_error 2 (C009, C018); not_reproduced 0; repaired_residual 0. Classification-code repairs: none against the current corrected ledger. Required transcription/location refinements: C016 MINI V5.0 plus citation 1 rather than literal V5.01; C017 IDS example statistics are directly on main p8 and protocol p9 corroborates main parameters only. C006's directly viewed protocol p26 fish-oil product label adds a source-grounded mass-basis alternative. These refinements leave their registered core comparisons unchanged.

Exact candidate pages were readable and fully inspected; no tooling or missing-source limitation arose. Missing raw participant boundary values, blood denominator/pairing definitions, questionnaire extensions, dose basis, final hierarchy/amendment chronology and exact prospective model configurations are bounded interpretive limitations recorded per ID. They do not establish paper-level conclusion impact. C009/C018 deliberately distinguish printed numeric differences from unsupported matching assumptions. Every stable ID is retained for human adjudication; no final correction or acceptance decision is proposed.
## C021 — Adherence-row asterisks point to a Morisky-score definition

- **Location found:** Yes. [Supplied results supplement, physical p16, eAppendix8](../../../joi190007supp3_prod.pdf#page=16), Adherence subsection, its four count/percentage adherence rows, following Morisky row, and single-asterisk footnote below the table. The printed page number is 15, so `#page=16` is the truthful PDF location.
- **Source value/text matched:** Yes, by direct visual reading of the page image. In the printed arm order (placebo without F-BA; placebo with F-BA; supplements without F-BA; supplements with F-BA), the rows are:
  - “Multinutrient adherence ≥70% from pill weight*”: N666; 135 (76.7%), 134 (78.8%), 126 (75.0%), 120 (78.9%).
  - “Multinutrient adherence ≥70% from self-report*”: N855; 164 (77.7%), 165 (74.3%), 155 (73.8%), 151 (71.2%).
  - “Omega adherence ≥70% from pill weight*”: N652; 133 (76.9%), 133 (81.1%), 126 (76.8%), 120 (79.5%).
  - “Omega adherence ≥70% from self-report *”: N855; 163 (77.3%), 164 (73.9%), 156 (74.3%), 152 (71.7%).
  Each label ends with one asterisk. Line wrapping does not change the row association.
- **Comparator matched:** Yes. The separately tabulated “Morisky score (average), median (IQR)” row has no asterisk; N856; 1 (0.50–1.50), 1 (0.50–1.75), 1 (0.50–1.50), 1 (0.50–1.75). The literal single-asterisk footnote is: “*average Morisky score over the four follow-up moments. Calculated when at least 1 follow-up value was available”. The following double-asterisk kappa footnote is a different marker/text association and is not the comparator for C021.
- **Consistency rule applicable:** Yes, as a printed measure/label association: a table-row asterisk refers to the footnote bearing the same marker. The four marked rows explicitly name ≥70% pill-weight or self-report adherence, while the matched footnote explicitly names average Morisky score, which has its own separately labeled, unmarked median/IQR row. No equality between the two measures, no required equality of their N values, and no inferential-statistical rule is assumed.
- **Calculation or logical comparison reproduced:** Yes. Visual marker count: four single-asterisk adherence rows versus zero single-asterisk markers on the Morisky row. Reading the corresponding single-asterisk footnote reproduces its reference to Morisky and to averaging across four follow-up moments with at least one available value. This reproduces the registered conditional footnote/measure association question. Arithmetic is unnecessary; N666/855/652/855 versus N856 provides separate-row context rather than a denominator contradiction.
- **Necessary inputs available:** Yes for the registered marker-association observation: row labels, marker locations, arm order, row N/cells, separate Morisky label and absence of a marker, and literal footnote text are all visible on one exact supplied page. Raw follow-up values are unnecessary for this observation.
- **Exact missing inputs or definitions:** The intended scope of the single asterisk; whether the Morisky-specific first sentence and availability/aggregation second sentence were intended to apply to different rows; and any explicit mapping from Morisky score to the four pill-weight/self-report adherence measures. The supplied page does not specify which aggregation/availability rule belongs to each marked percentage-adherence row. The absence of these definitions does not prevent observation of the printed association.
- **Source-grounded alternative interpretation:** The footnote's second sentence could be intended as a broader available-follow-up rule, even though its first sentence names Morisky specifically. A displaced marker or a footnote wording/association issue could also explain the table. These possibilities arise from the juxtaposition of the marked adherence rows, unmarked Morisky row and two-sentence footnote; the page does not establish which applies. No marker placement or final wording is prescribed.
- **Direct observation versus inferred explanation:** Direct observations are the four single asterisks, their row labels/cells, the unstarred Morisky row and its cells, and the Morisky-specific footnote. A misplaced marker, copied footnote, broader aggregation rule or production mechanism is only an inferred possible explanation. No wrong participant count, wrong analysis, score-percentage equivalence, conclusion impact or actual downstream consequence is inferred.
- **Exact remaining human question:** Which rows does the single-asterisk footnote describe, and what aggregation/availability rule applies to each of the four ≥70% adherence rows and to the Morisky score row?
- **Document roles confirmed:** Every compared location is `REPORT` by content: eAppendix8 presents observed adherence and other trial results with arm-specific N and descriptive summaries. Neither compared side is prospective PLAN content.
- **Relationship classification confirmed:** Primary relationship type `S_W`; all relationships `S_W`. The two discrepant printed associations are within the same results-supplement table/page. No cross-document discrepancy or PLAN comparator is involved; precedence does not change the result. Primary category `Measure, label, or scale inconsistency`; mechanically derived review domain `report_internal_inconsistency`. No classification repair is required.
- **Classification ambiguity:** Intended footnote scope and aggregation rule remain unresolved; document roles and within-document relationship are supported by the compared content.
- **Evidence state:** `recorded_candidate`. Determining recheck fact: the registered four marked adherence rows, unmarked Morisky row, and Morisky-specific single-asterisk footnote are all reproduced by source-page visual inspection. The question remains exactly as registered pending the named intended-scope definition; no transcription or alignment input was disproven.
- **Suggested review disposition:** `retain`, mechanically derived from `recorded_candidate`. This is a prefilled review field, not adjudication. **Status:** Pending Human Adjudication.
- **Distinctness:** C021 concerns single-asterisk measure/footnote association. C020 concerns product assignments of kappa values and a double-asterisk footnote. Their printed inputs, comparator and rule differ; no ID is merged or removed.

Scope complete: C021. Unresolved item: intended single-asterisk scope and per-measure aggregation/availability rule. Visual/source-location limitations: None. No additional source units or stable IDs were assigned to this extension.

## Final recheck completion after appended-ID review

Original mandatory rechecker covered C001-C020; fresh root/recheck_append_001 covered C021. The appended source part is preserved unchanged, and its candidate record is merged above with links adjusted for the canonical artifact directory. Final stable set:21 IDs. Final evidence states:19 recorded_candidate;2 record_input_error (C009,C018);0 not_reproduced;0 repaired_residual. The single final classification table contains all21 IDs in stable order. All remain Pending Human Adjudication.
## C022 — Multivitamin tablet label with capsule package contents

**Candidate:** The upper multivitamin example product label specifies a daily tablet but calls its package contents capsules.

**Status:** Pending Human Adjudication.

**Location found:** Yes. [Protocol physical PDF p26, upper multivitamin product label](../../../joi190007supp1_prod.pdf#page=26), above section 6.5. Its product/composition, dosage, and contents lines are separately legible within the same upper panel. The lower omega-3 label and surrounding section 6.5 are also visible on that exact page and were inspected for an alternative explanation.

**Source value/text matched:** Yes. In English translation, the upper label identifies multivitamins with calcium 100 mg, folic acid 400 micrograms, selenium 30 micrograms, and vitamin D3 20 micrograms, or a placebo tablet. Its next line states dosage of **1 tablet per day**, preferably before a meal. The numeral 1 and tablet unit are directly visible; there is no native-text or OCR substitution in this confirmation.

**Comparator matched:** Yes. The contents line of the **same upper label** states, in English translation, **Contents: 30 capsules**. The numeral 30 and capsule noun are directly visible. This is not a contents line imported from the lower panel: both panels independently display 30 capsules, while the lower panel's dosage is 1 capsule per day.

**Consistency rule applicable:** Yes. Within a single product label, the named dosage unit and named units in its package contents should describe the same dosage form unless a conversion, mixed package, or explicit alternative convention is supplied. This is a unit-label identity check, not a calculation of nutrient mass, adherence, duration, or treatment effect. The candidate concerns tablet versus capsule terminology; it does not allege that the printed count 30 is numerically incorrect.

**Calculation or logical comparison reproduced:** Yes. The upper panel's daily-dose unit is tablet, whereas its contents unit is capsule. The two different named dosage forms occur in adjacent lines for the same labeled product. The mismatch therefore reproduces directly without arithmetic or an inferred dispensing schedule. The lower omega-3 panel is internally capsule/capsule and provides context rather than a second discrepancy relationship.

**Necessary inputs available:** Yes for the printed unit-label comparison: panel identity, dose line, and contents line are all visible together on the supplied page. No quantitative input is missing for establishing that the two nouns differ.

**Exact missing inputs or definitions:** The supplied label does not define tablet and capsule as interchangeable terms, identify a mixed-form package, provide a conversion between the forms, or state the intended upper-label dosage-form noun. The referenced C1.2 document's official labels and manufacturing information are not supplied in this package. An authoritative final label or dispensing record establishing the actual dispensed upper product is also absent from this comparison. Those absent inputs limit explanation and adjudication, not transcription of the observed mismatch.

**Source-grounded alternative interpretation:** [Protocol physical p25, preparation and labelling section](../../../joi190007supp1_prod.pdf#page=25) explicitly describes the displayed labels as patient-information examples and refers to official labels on C1.2 pages 4–12 and manufacturing details on C1.2 pages 24–27. Thus the visible mismatch may be confined to an example rather than an actual final dispensing label. Section 6.5 on p26 uses the broader expressions multi-vitamin pills and capsules, and unused pills/capsules, in its shipping and accountability instructions. That generic wording may permit loose operational terminology; however, it does not explicitly equate tablet and capsule on the upper product label. The lower label has the same 30-capsule contents wording, making shared label-template wording a possible explanation. Neither the example status, broad accountability wording, nor similar lower panel establishes which upper-label noun was intended or what was actually dispensed.

**Direct observation versus inferred explanation:** Direct observation is the upper panel's tablet dosage and capsule contents terminology, together with the lower panel's consistent capsule terminology, the broad accountability prose, and p25's example-label framing. A copied template, informal synonym usage, a different actual dosage form, or a mixed package is an inferred explanation only. No production mechanism, clinical implication, or actual dispensing error is established by this observation.

**Exact remaining human question:** Does the upper multivitamin example label intentionally use capsule as an interchangeable term for tablet, or which dosage-form noun should describe its contents and daily dose? Was this wording confined to the patient-information example, or does an authoritative C1.2 final label or dispensing record establish the same wording and actual product form?

**Document-role confirmation:** The upper product/composition and dosage lines are PLAN, and the upper contents line is PLAN. By content, this is a prospective operational example product label embedded in a trial protocol, not a report of study results. The lower label, section 6.5, and p25's label-preparation explanation are also PLAN context. No REPORT location is part of this discrepancy.

**Relationship confirmation and precedence:** `P_P` confirmed. Both compared locations occur inside one PLAN label on one protocol page. All substantive discrepancy relationships are `P_P` only. The lower label and accountability prose support interpretation but introduce no additional discrepancy relationship. There is no `P_R`, `S_C`, or `S_W` comparison. No correction to the provisional category or relationship type is required.

**Classification ambiguity:** None for document role or relationship type. The unresolved issue is intended dosage-form terminology, not whether these source locations are PLAN content.

**Primary category:** Measure, label, or scale inconsistency.

**Relationship type:** P_P.

**All relationships:** P_P.

**Compared document roles:** PLAN protocol p26 upper product-label tablet dosage vs PLAN protocol p26 upper product-label capsule contents.

**Review domain:** plan_material.

**Evidence state:** recorded_candidate.

**Evidence-state determining fact:** Direct visual reading confirms that the same upper label gives a tablet daily dose and 30 capsule contents. The package does not supply a definition reconciling these dosage-form terms. The registered label mismatch remains as registered pending that named definition; no original input or alignment assumption is disproved.

**Suggested review disposition:** retain. This follows mechanically from `recorded_candidate` and is a prefilled human-review field, not an adjudication.

**Distinctness:** C006 compares fish-oil versus EPA+DHA mass descriptions across PLAN and REPORT content. C014 compares the separately printed 13-week and four-month supply durations. C022 instead compares two dosage-form nouns inside the same upper multivitamin label. Its values, comparator, and consistency rule are distinct from both IDs.

**Bounded downstream relevance:** An ambiguous dosage-form noun could be copied into intervention or packaging descriptions. The observation does not establish a changed dose, participant exposure, or paper-level conclusion effect.


## Final completion after visual-repair appended source recheck

All22 stable IDs now have complete direct-source records: original C001–C020 plus fresh C021 and C022 recheck parts. Final states:20 recorded_candidate and2 record_input_error (C009,C018);0 not_reproduced;0 repaired_residual. C022 is confirmed P_P/plan_material with retain mechanically derived. The22-row canonical classification table agrees with the ledger. All22 remain Pending Human Adjudication. Original20/21 completion sections above are chronological handoff records rather than current totals; this final22-ID completion supersedes their counts.
