# Quantitative Quality-Control Consistency Review: Barkin et al. Paper Package

## Pending Human Adjudication

**All 13 candidate consistency issues in this report are Pending Human Adjudication.** This source-first quality-control review records reproducible printed mismatches for human review. It does not assign severity, validity, acceptance, exclusion, a final correction, or a conclusion about the paper.

## Executive Quality-Control Summary

Complete fresh processing of the three supplied PDFs identified 13 distinct source-grounded quantitative reporting candidates: nine arm-by-visit observed-BMI count mismatches, two assessment-schedule count/list mismatches, one outcome-scale label mismatch, and one control-exposure description mismatch. The candidate set is `C001` through `C013`; it has no queue, ranking, cap, or deferred subset. No candidate was created from a display-zero P value.

The review is a quantitative reporting quality-control exercise. Small preventable defects can matter if a later evidence extractor copies a count, schedule, scale, or exposure description. This report does not assert that any defect propagated, altered an effect estimate, changed a conclusion, or caused harm.

## Package and Fresh-Processing Provenance

Only the direct supplied sources and newly created Workflow 1.5.2 evidence assets were used. Existing audit derivatives were not evidence inputs or discovery boundaries.

| Source ID | Direct source | Role | Units | SHA-256 |
|---|---|---|---:|---|
| DOC-001 | [jama_barkin_2018_oi_180075.pdf](<../jama_barkin_2018_oi_180075.pdf#page=1>) | Main article | 11 PDF pages | `231de40e6ac86c81413c11d958fc410e49450ece9b6ddb0c22e2042d2c162e36` |
| DOC-002 | [joi180075supp1_prod.pdf](<../joi180075supp1_prod.pdf#page=1>) | Protocol and statistical analysis plan supplement | 113 PDF pages | `b67c573979a4264284b87711cc2dd9ff7a74c2d709e1b045993f54624a4c6196` |
| DOC-003 | [joi180075supp2_prod.pdf](<../joi180075supp2_prod.pdf#page=1>) | Results supplement | 8 PDF pages | `5417d3ddc9769fa45832d8495fb337bcbeb2396276f08c79c81efa7626556a9a` |

Fresh native and layout PDF text were prepared for every direct source. Result-relevant pages were rendered; targeted CPU OCR was used only where the native text was inadequate for the relevant content. Fresh assets and methods are inventoried in [evidence_asset_inventory.md](<review_1_5_2/evidence_asset_inventory.md>).

## Scope, Complete Coverage, and Exclusions

| Source ID | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 | 11 | 0 | 11 | 11 | COMPLETE |
| DOC-002 | 113 | 0 | 113 | 113 | COMPLETE |
| DOC-003 | 8 | 0 | 8 | 8 | COMPLETE |
| **Total** | **132** | **0** | **132** | **132** | **COMPLETE** |

Coverage includes all result-relevant main-article and support contents, not only primary outcomes or significant results. The complete stage assignment and artifact paths are in [coverage_manifest.md](<review_1_5_2/coverage_manifest.md>). Exclusions were limited to unsupported reconstruction: no raw participant data, unprinted eFigure coordinates, or unprinted model parameters were inferred. Coherent finite-precision P-value displays were not treated as candidates.

## Quantitative and Statistical Relationship Coverage

The numeric/reporting inventory covered all 64 relationships: `N001`, `N002`, `N003`, `N004`, `N005`, `N006`, `N007`, `N008`, `N009`, `N010`, `N011`, `N012`, `N013`, `N014`, `N015`, `N016`, `N017`, `N018`, `N019`, `N020`, `N021`, `N022`, `N023`, `N024`, `N025`, `N026`, `N027`, `N028`, `N029`, `N030`, `N031`, `N032`, `N033`, `N034`, `N035`, `N036`, `N037`, `N038`, `N039`, `N040`, `N041`, `N042`, `N043`, `N044`, `N045`, `N046`, `N047`, `N048`, `N049`, `N050`, `N051`, `N052`, `N053`, `N054`, `N055`, `N056`, `N057`, `N058`, `N059`, `N060`, `N061`, `N062`, `N063`, and `N064` ([inventory](<review_1_5_2/relationships/numeric_relationship_inventory.md>)).

The inferential/statistical inventory covered all 71 relationships: `S001`, `S002`, `S003`, `S004`, `S005`, `S006`, `S007`, `S008`, `S009`, `S010`, `S011`, `S012`, `S013`, `S014`, `S015`, `S016`, `S017`, `S018`, `S019`, `S020`, `S021`, `S022`, `S023`, `S024`, `S025`, `S026`, `S027`, `S028`, `S029`, `S030`, `S031`, `S032`, `S033`, `S034`, `S035`, `S036`, `S037`, `S038`, `S039`, `S040`, `S041`, `S042`, `S043`, `S044`, `S045`, `S046`, `S047`, `S048`, `S049`, `S050`, `S051`, `S052`, `S053`, `S054`, `S055`, `S056`, `S057`, `S058`, `S059`, `S060`, `S061`, `S062`, `S063`, `S064`, `S065`, `S066`, `S067`, `S068`, `S069`, `S070`, and `S071` ([inventory](<review_1_5_2/statistics/relationship_inventory.md>)).

Numeric and cross-source checks completed all applicable relationships. Independent statistical pass 1 recorded `PASS_1_COMPLETE` for all 71 S relationships; independent statistical pass 2 recorded `PASS_2_COMPLETE` for all 71 S relationships and reconciled every stable candidate and recheck fact. The pass artifacts are [pass 1](<review_1_5_2/checkers/statistical_pass_1.md>) and [pass 2](<review_1_5_2/checkers/statistical_pass_2.md>).

## Candidate Index

| ID | Candidate statement | Category |
|---|---|---|
| [C001](#c001--intervention-3-month-bmi-observation-count-differs-across-result-displays) | Intervention 3-month BMI-observation count differs across result displays | Cross-document numeric inconsistency |
| [C002](#c002--control-3-month-bmi-observation-count-differs-across-result-displays) | Control 3-month BMI-observation count differs across result displays | Cross-document numeric inconsistency |
| [C003](#c003--intervention-9-month-bmi-observation-count-differs-across-result-displays) | Intervention 9-month BMI-observation count differs across result displays | Cross-document numeric inconsistency |
| [C004](#c004--intervention-12-month-bmi-observation-count-differs-across-result-displays) | Intervention 12-month BMI-observation count differs across result displays | Cross-document numeric inconsistency |
| [C005](#c005--control-12-month-bmi-observation-count-differs-across-result-displays) | Control 12-month BMI-observation count differs across result displays | Cross-document numeric inconsistency |
| [C006](#c006--intervention-24-month-bmi-observation-count-differs-across-result-displays) | Intervention 24-month BMI-observation count differs across result displays | Cross-document numeric inconsistency |
| [C007](#c007--control-24-month-bmi-observation-count-differs-across-result-displays) | Control 24-month BMI-observation count differs across result displays | Cross-document numeric inconsistency |
| [C008](#c008--intervention-36-month-bmi-observation-count-differs-across-result-displays) | Intervention 36-month BMI-observation count differs across result displays | Cross-document numeric inconsistency |
| [C009](#c009--final-sap-says-six-assessment-points-but-enumerates-five) | Final SAP says six assessment points but enumerates five | Numeric or arithmetic inconsistency |
| [C010](#c010--revised-protocol-gives-six-points-but-lists-seven-including-48-months) | Revised protocol gives six points but lists seven including 48 months | Denominator, proportion, or total inconsistency |
| [C011](#c011--original-protocol-labels-primary-outcome-as-bmi-percentilebmi-while-results-use-bmi-kgm) | Original protocol labels primary outcome as BMI percentile/BMI% while results use BMI kg/m² | Measure, label, or scale inconsistency |
| [C012](#c012--control-condition-session-count-and-duration-differ-across-protocol-versions-and-article) | Control-condition session count and duration differ across protocol versions and article | Cross-document numeric inconsistency |
| [C013](#c013--control-9-month-bmi-observation-count-differs-across-result-displays) | Control 9-month BMI-observation count differs across result displays | Cross-document numeric inconsistency |

## Candidate Evidence Cards

## C001 — Intervention 3-month BMI-observation count differs across result displays

**Status:** Pending Human Adjudication

**Candidate statement:** The intervention 3-month BMI count is 288 in the flow diagram and 279 in both the observed-BMI figure and eTable.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [DOC-001 Figure 1 — PDF p. 3](<../jama_barkin_2018_oi_180075.pdf#page=3>); [DOC-001 Figure 2 — PDF p. 7](<../jama_barkin_2018_oi_180075.pdf#page=7>); [DOC-003 eTable 1 — PDF p. 2](<../joi180075supp2_prod.pdf#page=2>).

**Source evidence:** Figure 1 prints `288 BMI measured at 3 mo` for intervention and defines the retained count as children for whom BMI was collected. Figure 2 and eTable 1 each print intervention `279` at 3 months.

**Reported-versus-comparator:** 288 versus 279 for intervention, 3 months; Figure 2 and eTable 1 agree with each other.

**Reasoning procedure:** Compare same arm, visit, and labeled observed/collected BMI quantity; an explicit differing subset is needed to reconcile unequal integer counts.

**Calculation:** `288 - 279 = 9`.

**Alternative source-grounded interpretations:** Figure 1 may count all collected measurements while Figure 2/eTable 1 may use a cleaned descriptive subset; no supplied caption or method defines that distinction.

**Mechanical evidence recheck:** All three cited locations were found; their printed values and labels matched; the integer comparison was reproduced. Missing inputs are record-level inclusion flags, validity/cleaning criteria, and exclusion reasons. Direct observation is the 288/279 mismatch; cleaning is an inferred explanation.

**Quality-control relevance:** A source-defined distinction is needed for readers to reconcile two printed intervention 3-month BMI denominators.

**Potential downstream evidence impact:** If confirmed, an extractor could copy an inconsistent intervention 3-month observed-BMI denominator into a systematic review, meta-analysis, guideline evidence table, or other evidence product.

**Human verification steps:** Reconcile participant-level 3-month intervention BMI records and identify any post-collection rule separating the flow count from Figure 2/eTable 1.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Control 3-month BMI-observation count differs across result displays

**Status:** Pending Human Adjudication

**Candidate statement:** The control 3-month BMI count is 277 in the flow diagram and 271 in both the observed-BMI figure and eTable.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [DOC-001 Figure 1 — PDF p. 3](<../jama_barkin_2018_oi_180075.pdf#page=3>); [DOC-001 Figure 2 — PDF p. 7](<../jama_barkin_2018_oi_180075.pdf#page=7>); [DOC-003 eTable 1 — PDF p. 2](<../joi180075supp2_prod.pdf#page=2>).

**Source evidence:** Figure 1 prints `277 BMI measured at 3 mo` for control; Figure 2 and eTable 1 each print control `271` at 3 months.

**Reported-versus-comparator:** 277 versus 271 for control, 3 months.

**Reasoning procedure:** Same arm, visit, and observed/collected BMI count should agree unless a distinct subset is expressly defined.

**Calculation:** `277 - 271 = 6`.

**Alternative source-grounded interpretations:** Figure 2/eTable 1 may be a cleaned descriptive subset, but the supplied package does not define a cleaning or inclusion rule.

**Mechanical evidence recheck:** The locations, values, and comparison rule were reproduced. Missing inputs are record-level inclusion flags, post-collection criteria, and exclusion reasons; any cleaning explanation remains inferred.

**Quality-control relevance:** The control 3-month denominator is not reconciled across displayed results.

**Potential downstream evidence impact:** If confirmed, a later extractor could copy an inconsistent control 3-month observed-BMI denominator.

**Human verification steps:** Reconcile the six records between collection and descriptive-display denominators and document the governing eligibility rule.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Intervention 9-month BMI-observation count differs across result displays

**Status:** Pending Human Adjudication

**Candidate statement:** The intervention 9-month BMI count is 282 in the flow diagram and 280 in both the observed-BMI figure and eTable.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [DOC-001 Figure 1 — PDF p. 3](<../jama_barkin_2018_oi_180075.pdf#page=3>); [DOC-001 Figure 2 — PDF p. 7](<../jama_barkin_2018_oi_180075.pdf#page=7>); [DOC-003 eTable 1 — PDF p. 2](<../joi180075supp2_prod.pdf#page=2>).

**Source evidence:** Figure 1 prints intervention `282 BMI measured at 9 mo`; Figure 2 and eTable 1 each print 280.

**Reported-versus-comparator:** 282 versus 280 for intervention, 9 months.

**Reasoning procedure:** Compare the repeated same-arm, same-visit observed-BMI count under zero integer tolerance.

**Calculation:** `282 - 280 = 2`.

**Alternative source-grounded interpretations:** A post-collection analytic or descriptive subset could explain the difference, but the package supplies no definition.

**Mechanical evidence recheck:** Cited pages, printed values, and calculation were reproduced. Record identities and inclusion rules are unavailable; subset exclusion is inference, not direct observation.

**Quality-control relevance:** The printed intervention 9-month denominator needs a source-defined reconciliation.

**Potential downstream evidence impact:** If confirmed, the intervention 9-month denominator could be copied inconsistently into later evidence extraction.

**Human verification steps:** Reconcile the two intervention records and the relation of Figure 1 collection counts to Figure 2/eTable denominators.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Intervention 12-month BMI-observation count differs across result displays

**Status:** Pending Human Adjudication

**Candidate statement:** The intervention 12-month BMI count is 275 in the flow diagram and 274 in both the observed-BMI figure and eTable.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [DOC-001 Figure 1 — PDF p. 3](<../jama_barkin_2018_oi_180075.pdf#page=3>); [DOC-001 Figure 2 — PDF p. 7](<../jama_barkin_2018_oi_180075.pdf#page=7>); [DOC-003 eTable 1 — PDF p. 2](<../joi180075supp2_prod.pdf#page=2>).

**Source evidence:** Figure 1 prints intervention `275 BMI measured at 12 mo`; Figure 2 and eTable 1 each print 274.

**Reported-versus-comparator:** 275 versus 274 for intervention, 12 months.

**Reasoning procedure:** Same arm, time point, and observed/collected measure require the same integer unless different subsets are defined.

**Calculation:** `275 - 274 = 1`.

**Alternative source-grounded interpretations:** One record may have been excluded from a descriptive subset, but no supplied rule establishes that.

**Mechanical evidence recheck:** Locations, values, and arithmetic were reproduced. The record identity and any cleaning rule are missing; exclusion is only a possible explanation.

**Quality-control relevance:** The intervention 12-month observed-BMI denominator is not fully defined across displays.

**Potential downstream evidence impact:** If confirmed, an evidence product could copy the wrong intervention 12-month denominator.

**Human verification steps:** Identify the one-record difference and document any display-specific inclusion rule.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Control 12-month BMI-observation count differs across result displays

**Status:** Pending Human Adjudication

**Candidate statement:** The control 12-month BMI count is 276 in the flow diagram and 275 in both the observed-BMI figure and eTable.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [DOC-001 Figure 1 — PDF p. 3](<../jama_barkin_2018_oi_180075.pdf#page=3>); [DOC-001 Figure 2 — PDF p. 7](<../jama_barkin_2018_oi_180075.pdf#page=7>); [DOC-003 eTable 1 — PDF p. 2](<../joi180075supp2_prod.pdf#page=2>).

**Source evidence:** Figure 1 prints control `276 BMI measured at 12 mo`; Figure 2 and eTable 1 each print 275.

**Reported-versus-comparator:** 276 versus 275 for control, 12 months.

**Reasoning procedure:** Apply the same-arm, same-visit integer-count identity rule.

**Calculation:** `276 - 275 = 1`.

**Alternative source-grounded interpretations:** A cleaned descriptive subset is possible but is not defined by the supplied materials.

**Mechanical evidence recheck:** All cited printed values and the arithmetic comparison were confirmed. Record-level disposition and subset definition are unavailable.

**Quality-control relevance:** The control 12-month denominator is inconsistently displayed without an explanation.

**Potential downstream evidence impact:** If confirmed, a reviewer could extract an inconsistent control 12-month denominator.

**Human verification steps:** Reconcile the one record and obtain the collection-to-display inclusion definition.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Intervention 24-month BMI-observation count differs across result displays

**Status:** Pending Human Adjudication

**Candidate statement:** The intervention 24-month BMI count is 280 in the flow diagram and 278 in both the observed-BMI figure and eTable.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [DOC-001 Figure 1 — PDF p. 3](<../jama_barkin_2018_oi_180075.pdf#page=3>); [DOC-001 Figure 2 — PDF p. 7](<../jama_barkin_2018_oi_180075.pdf#page=7>); [DOC-003 eTable 1 — PDF p. 2](<../joi180075supp2_prod.pdf#page=2>).

**Source evidence:** Figure 1 prints intervention `280 BMI measured at 24 mo`; Figure 2 and eTable 1 each print 278.

**Reported-versus-comparator:** 280 versus 278 for intervention, 24 months.

**Reasoning procedure:** Compare the repeated same-arm, same-time observed-BMI count; no tolerance applies to the displayed integers.

**Calculation:** `280 - 278 = 2`.

**Alternative source-grounded interpretations:** A post-collection descriptive-display subset could account for the difference, but the package does not state one.

**Mechanical evidence recheck:** Cited locations, printed counts, and calculation matched. Participant-level disposition and display-inclusion criteria are absent; no exclusion is asserted.

**Quality-control relevance:** The intervention 24-month denominator requires clarification for consistent quantitative reporting.

**Potential downstream evidence impact:** If confirmed, an evidence extractor could copy an inconsistent intervention 24-month denominator.

**Human verification steps:** Reconcile the two records and provide the rule distinguishing collection and descriptive display.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Control 24-month BMI-observation count differs across result displays

**Status:** Pending Human Adjudication

**Candidate statement:** The control 24-month BMI count is 267 in the flow diagram and 266 in both the observed-BMI figure and eTable.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [DOC-001 Figure 1 — PDF p. 3](<../jama_barkin_2018_oi_180075.pdf#page=3>); [DOC-001 Figure 2 — PDF p. 7](<../jama_barkin_2018_oi_180075.pdf#page=7>); [DOC-003 eTable 1 — PDF p. 2](<../joi180075supp2_prod.pdf#page=2>).

**Source evidence:** Figure 1 prints control `267 BMI measured at 24 mo`; Figure 2 and eTable 1 each print 266.

**Reported-versus-comparator:** 267 versus 266 for control, 24 months.

**Reasoning procedure:** Apply the repeated count-identity rule to the same arm, visit, and BMI measure.

**Calculation:** `267 - 266 = 1`.

**Alternative source-grounded interpretations:** A cleaning or descriptive-subset distinction is possible but unreported.

**Mechanical evidence recheck:** Printed values, locations, and calculation were reproduced. The individual record and the applicable inclusion rule are missing.

**Quality-control relevance:** The control 24-month observed-BMI denominator is not reconciled in the displays.

**Potential downstream evidence impact:** If confirmed, a later evidence product could copy an inconsistent control 24-month denominator.

**Human verification steps:** Reconcile the one record and document the count definition in each result display.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — Intervention 36-month BMI-observation count differs across result displays

**Status:** Pending Human Adjudication

**Candidate statement:** The intervention 36-month count is 278 retained/BMI collected in the flow diagram and 276 in both the observed-BMI figure and eTable.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [DOC-001 Figure 1 — PDF p. 3](<../jama_barkin_2018_oi_180075.pdf#page=3>); [DOC-001 Figure 2 — PDF p. 7](<../jama_barkin_2018_oi_180075.pdf#page=7>); [DOC-003 eTable 1 — PDF p. 2](<../joi180075supp2_prod.pdf#page=2>).

**Source evidence:** Figure 1 prints intervention `278 Retained at 36 mo`; its caption defines retained as BMI collected. Figure 2 and eTable 1 each print 276.

**Reported-versus-comparator:** 278 versus 276 for intervention, 36 months.

**Reasoning procedure:** Use the Figure 1 caption's BMI-collected definition and compare with the same-arm observed-BMI result displays.

**Calculation:** `278 - 276 = 2`.

**Alternative source-grounded interpretations:** `Retained` may have been used more broadly despite the caption, or a post-collection subset may have been used; neither is defined.

**Mechanical evidence recheck:** Locations, counts, caption, and arithmetic were confirmed. The meaning of retained and any record-level exclusion rule remain missing; alternatives are inference only.

**Quality-control relevance:** The 36-month intervention denominator needs a stated reconciliation between retention/collection and observed-BMI displays.

**Potential downstream evidence impact:** If confirmed, extraction of the intervention 36-month observed or retained denominator could be inconsistent.

**Human verification steps:** Determine whether retained is broader than the caption's BMI-collected definition and reconcile the two records.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C009 — Final SAP says six assessment points but enumerates five

**Status:** Pending Human Adjudication

**Candidate statement:** The final SAP states six time points but its parenthetical schedule lists only baseline, 3, 9, 12, and 36 months.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [DOC-002 final SAP — PDF p. 110](<../joi180075supp1_prod.pdf#page=110>); [DOC-002 protocol schedule — PDF p. 15](<../joi180075supp1_prod.pdf#page=15>); [DOC-001 Methods — PDF p. 4](<../jama_barkin_2018_oi_180075.pdf#page=4>); [DOC-003 eTable 1 — PDF p. 2](<../joi180075supp2_prod.pdf#page=2>).

**Source evidence:** The SAP says `6 time points` while enumerating five occasions. Other supplied schedules/results include 24 months; the SAP also describes six repeated measurements on p. 112.

**Reported-versus-comparator:** Stated total of six versus five listed occasions; matching sources show the otherwise omitted 24-month occasion.

**Reasoning procedure:** Count the explicitly enumerated distinct occasions and compare that count with the stated total, without inferring unprinted model data.

**Calculation:** `count(baseline, 3, 9, 12, 36) = 5`; including 24 months yields 6.

**Alternative source-grounded interpretations:** The final-SAP prose may have an editorial omission, and the model may still have used 24-month data; the package does not provide the archived analysis input schedule.

**Mechanical evidence recheck:** The p. 110 sentence, p. 112 six-measurement statement, and matching 24-month locations were found. The five-item list and count rule are direct; identification of 24 months as the intended omission is source-supported inference.

**Quality-control relevance:** A stated assessment schedule should enumerate the same number of occasions it claims.

**Potential downstream evidence impact:** If confirmed, a review or guideline evidence table could copy an incomplete planned measurement schedule or model-timepoint description.

**Human verification steps:** Inspect the final archived SAP and model input schedule to determine whether 24 months was intended in the parenthetical list and primary model.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C010 — Revised protocol gives six points but lists seven including 48 months

**Status:** Pending Human Adjudication

**Candidate statement:** The revised protocol calls the schedule six points/T1-T6 while listing seven occasions, including 48 months.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [DOC-002 revised protocol — PDF p. 64](<../joi180075supp1_prod.pdf#page=64>); [DOC-001 Methods — PDF p. 4](<../jama_barkin_2018_oi_180075.pdf#page=4>); [DOC-003 eTable 1 — PDF p. 2](<../joi180075supp2_prod.pdf#page=2>).

**Source evidence:** The revised protocol states `6-points in time (T1-T6)` and lists baseline, 3, 9, 12, 24, 36, and 48 months; it also says six collection points. The article and eTable report through 36 months.

**Reported-versus-comparator:** Six claimed points versus seven listed occasions; baseline-to-36-month reported schedule has six occasions.

**Reasoning procedure:** Count the distinct occasions in the revised-protocol sentence and compare its stated total with the matched reported schedule.

**Calculation:** `count(baseline, 3, 9, 12, 24, 36, 48) = 7`, not 6.

**Alternative source-grounded interpretations:** The 48-month visit may have been a separate approved extension outside T1-T6; amendment chronology and the intended distinction are not supplied.

**Mechanical evidence recheck:** The internal six-versus-seven wording and matched article/eTable schedule were found and reproduced. The missing input is dated amendment/version documentation; lack of a published 48-month result is not treated as proof of error.

**Quality-control relevance:** The revised protocol's total/list statement cannot be read as a single unambiguous assessment schedule.

**Potential downstream evidence impact:** If confirmed, protocol schedule abstraction in systematic reviews, meta-analyses, or guideline evidence tables could be inconsistent.

**Human verification steps:** Review amendment dates and define whether 48 months was separate from the core T1-T6 assessment schedule.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C011 — Original protocol labels primary outcome as BMI percentile/BMI% while results use BMI kg/m²

**Status:** Pending Human Adjudication

**Candidate statement:** The original protocol labels the primary outcome BMI Percentile/BMI%, whereas the final SAP, article, and eTable report raw BMI in kg/m².

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [DOC-002 original protocol — PDF p. 16](<../joi180075supp1_prod.pdf#page=16>); [DOC-002 final SAP — PDF p. 110](<../joi180075supp1_prod.pdf#page=110>); [DOC-001 Outcomes — PDF p. 3](<../jama_barkin_2018_oi_180075.pdf#page=3>); [DOC-003 eTable 1 — PDF p. 2](<../joi180075supp2_prod.pdf#page=2>).

**Source evidence:** The original protocol uses `child's BMI Percentile` and `BMI%` while displaying a weight(kg)/height(m²) formula. The final sources analyze/report raw BMI in kg/m², including values such as 17.8.

**Reported-versus-comparator:** BMI percentile/BMI% label versus raw-BMI kg/m² formula, analysis label, and reported values.

**Reasoning procedure:** Compare the printed measure labels and scales; percentile/BMI% and raw BMI kg/m² are distinct scales unless an authoritative definition or amendment equates them.

**Calculation:** No arithmetic reconstruction is applicable; this is a categorical scale comparison.

**Alternative source-grounded interpretations:** `BMI%` may be erroneous shorthand for raw BMI, or a protocol amendment may have changed the primary outcome scale; neither explanation is resolved in the supplied package.

**Mechanical evidence recheck:** The original label/formula and final raw-BMI locations were found. The difference in labels/scales is direct; an analysis-variable change or typographical explanation is inferred and needs source documentation.

**Quality-control relevance:** The outcome scale needs an authoritative definition so planned and reported outcome descriptions can be reconciled.

**Potential downstream evidence impact:** If confirmed, an evidence extractor could misclassify the prespecified or reported primary outcome scale.

**Human verification steps:** Review the approved protocol/amendment trail and primary-model analysis variable or codebook.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C012 — Control-condition session count and duration differ across protocol versions and article

**Status:** Pending Human Adjudication

**Candidate statement:** The supplied original protocol, revised protocol, and article describe control exposure as 12×60, 7×45, and 6×30 minutes, respectively, without a supplied component mapping.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [DOC-002 original protocol — PDF p. 14](<../joi180075supp1_prod.pdf#page=14>); [DOC-002 revised protocol — PDF p. 64](<../joi180075supp1_prod.pdf#page=64>); [DOC-001 abstract — PDF p. 1](<../jama_barkin_2018_oi_180075.pdf#page=1>); [DOC-001 Methods — PDF p. 3](<../jama_barkin_2018_oi_180075.pdf#page=3>).

**Source evidence:** Original protocol: 12 quarterly 60-minute control sessions. Revised protocol: seven 45-minute school-readiness/success programs. Article: six 30-minute group activities.

**Reported-versus-comparator:** `12 × 60` versus `7 × 45` versus `6 × 30` minutes for descriptions of the control school-readiness exposure.

**Reasoning procedure:** Compare count and duration descriptions across protocol versions and the article; they cannot all describe one identical schedule absent a stated distinction among planned, ancillary, and delivered components.

**Calculation:** `12 × 60 = 720` minutes; `7 × 45 = 315` minutes; `6 × 30 = 180` minutes.

**Alternative source-grounded interpretations:** The versions may describe changed plans, ancillary components, or actual delivery. Session logs and a chronology/mapping of newsletters, field trips, baseline sessions, and activities are not supplied.

**Mechanical evidence recheck:** Each cited page and count/duration was found; arithmetic was reproduced. The unresolved human question is whether the descriptions refer to the same component or different planned/delivered components.

**Quality-control relevance:** A clear control-exposure mapping is needed to reconcile quantitative trial descriptions.

**Potential downstream evidence impact:** If confirmed, systematic reviews, meta-analyses, guidelines, or other extractors could copy inconsistent control-exposure intensity or duration.

**Human verification steps:** Review protocol chronology, amendment records, intervention logs, and component definitions to map planned and delivered control exposure.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C013 — Control 9-month BMI-observation count differs across result displays

**Status:** Pending Human Adjudication

**Candidate statement:** The control 9-month BMI count is 282 in the flow diagram and 280 in both the observed-BMI figure and eTable.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [DOC-001 Figure 1 — PDF p. 3](<../jama_barkin_2018_oi_180075.pdf#page=3>); [DOC-001 Figure 2 — PDF p. 7](<../jama_barkin_2018_oi_180075.pdf#page=7>); [DOC-003 eTable 1 — PDF p. 2](<../joi180075supp2_prod.pdf#page=2>).

**Source evidence:** Figure 1 prints control `282 BMI measured at 9 mo`; Figure 2 and eTable 1 each print 280.

**Reported-versus-comparator:** 282 versus 280 for control, 9 months.

**Reasoning procedure:** Compare same arm, visit, and observed/collected BMI quantity under the integer-count identity rule.

**Calculation:** `282 - 280 = 2`.

**Alternative source-grounded interpretations:** An unreported post-collection analytic or descriptive subset could explain the difference, but the supplied sources do not define it.

**Mechanical evidence recheck:** Cited values, pages, and arithmetic were reproduced. Participant-level record reconciliation and inclusion criteria are unavailable; exclusion remains an inferred explanation.

**Quality-control relevance:** The control 9-month observed-BMI denominator requires a defined reconciliation across results displays.

**Potential downstream evidence impact:** If confirmed, a later evidence extractor could copy an inconsistent control 9-month denominator.

**Human verification steps:** Reconcile the two records and document how Figure 1 collection counts relate to Figure 2/eTable denominators.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If confirmed, the candidates identify fields that later evidence users could copy: observed-BMI denominators by arm and visit, planned assessment schedules, outcome scale, and control-exposure intensity. Such fields can be carried into study-characteristic tables, data extraction forms, and evidence syntheses. The supplied package does not establish any actual downstream propagation, effect-estimate change, paper-level conclusion change, or harm.

## Limitations and Missing Definitions

The supplied package does not include participant-level denominator reconciliation, record-level BMI validity/cleaning and exclusion rules, full model matrices/covariance and degrees-of-freedom details, all moderator centering/coding rules, observed outputs for planned robustness analyses, or numerical coordinates for supplementary figures. DOC-002 pp. 108 and 111 have imperfect equation-glyph OCR; DOC-003 figure OCR is incomplete, so the rendered source pages were used for visual inspection. Multiple protocol versions do not always distinguish planned from delivered components. These limitations prevent unsupported reconstruction but do not remove the directly printed mismatches retained for human adjudication.

## Human Adjudication Checklist

1. Confirm the cited source page, printed values, and comparator for each stable C ID.
2. Obtain record-level or archived analysis documentation for the nine BMI-count differences.
3. Verify the final SAP schedule and protocol-version/amendment chronology.
4. Verify the authoritative primary-outcome scale and control-exposure component mapping.
5. Complete the blank adjudication fields in each card; retain the original evidence and any adjudication rationale.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

The pre-processing source hashes above match the fresh source-integrity audit. The direct-source inventory, coverage manifest, relationship inventories, candidate ledger, evidence recheck, and quality audit are versioned under [review_1_5_2](<review_1_5_2/>). The stable candidate ID set is identical across the ledger, recheck, quality audit, and this report: C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013.

### Agent execution

The execution manifest records the coordinator plus fresh preprocessing, main/support mapping, inventory, numeric, cross-source, two independent statistical-pass, evidence-recheck, quality-audit, and report-generation agents. Pass 1 and pass 2 were distinct fresh `gpt-5.6-terra` high-reasoning executions. See [agent_execution_manifest.md](<review_1_5_2/agent_execution_manifest.md>) for the complete agent/model/effort/start-mode list.

### Final performance and token metadata

- **Target basis:** Three supplied digital PDFs totaling 132 pages require fresh native and layout extraction. The package combines an 11-page main report, a 113-page protocol/SAP supplement with extensive definitions and planned analyses, and an 8-page results supplement; native text is expected to be usable, but complete cross-document mapping and two statistical passes create substantial relationship volume. No Office conversion or broad OCR burden is presently expected.
- **Total source units:** 132
- **Fresh-source units:** 132
- **Target elapsed minutes:** 55-80
- **Started UTC:** 2026-08-20T18:02:54Z
- **Finished UTC:** 2026-08-20T18:42:55Z
- **Observed elapsed minutes:** 40.0
- **Target status:** MET_TARGET
- **Exceedance causes:** None

Authoritative response-level token counts were not exposed by the coordinator or specialist runtimes. Accordingly, every manifested agent has an `UNAVAILABLE` ledger row; no token count or cost was approximated from text length.

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Agents | Exact records | Totals-only records | Unavailable records | Known total tokens | Known cost USD | Complete estimated cost USD | Status |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| gpt-5.6-sol | 3 | 0 | 0 | 3 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| gpt-5.6-terra | 10 | 0 | 0 | 10 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |

The accounting uses the 2026-08-18 pricing snapshot. These amounts are token-only API-equivalent estimates, not invoices; non-token tools, containers, storage, subscriptions, taxes, and other vendor charges are excluded.

Per-agent token detail is recorded in the versioned [token_usage_summary.md](<review_1_5_2/token_usage_summary.md>) after the accounting window closes. Token amounts, when finalized, are token-only API-equivalent estimates under the dated pricing snapshot and are not invoices.
