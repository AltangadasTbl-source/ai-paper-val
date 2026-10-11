# Evidence Quality Audit

All stable candidates remain **Pending Human Adjudication**. This audit is a neutral quality-control review of evidence support, coverage closure, arithmetic, relationship identity, links, and report-card readiness. It does not assign severity, validity, acceptance, exclusion, correction, or a scientific disposition.

## Audit scope and coverage status

- **Stable candidate set audited:** C001, C002, C003, C004, C005, C006, C007, C008, and C009; 9 of 9 appear in both `candidate_ledger.md` and `verification/evidence_recheck.md`.
- **Direct-source closure:** Four PDF sources contain 96 page units. The source ledger partitions them into 49 reusable units and 47 fresh-required units, with 96 mapped units. Every direct-source row satisfies `reusable + fresh-required = total`, `mapped = total`, and `Status = COMPLETE`.
- **Relationship closure:** The canonical numeric inventory and checker each contain N001-N089, and both statistical passes contain an explicit record for every S001-S083. No assigned relationship is omitted from either statistical pass.
- **Statistical execution:** `/root/statistics_pass_1` and `/root/statistics_pass_2` are distinct manifested agent IDs. Each is recorded as a fresh spawn using `gpt-5.6-terra` with high reasoning effort, and each has one primary artifact. Both artifacts cover S001-S083.
- **Coverage manifest:** All 26 data rows contain exactly one plain relative artifact path. At the audit snapshot, the 24 pre-audit rows marked `COMPLETE` resolve to existing artifacts. The `evidence_quality` and `report_generation` rows remain `PLANNED`; after this artifact and the report exist, the coordinator must enumerate C001-C009 explicitly in each scope and change the applicable status to `COMPLETE`.
- **Discovery boundary:** The source inventory, reusable-asset inventory, page-disjoint mapping assignments, N001-N089 inventory, S001-S083 inventory, and uncapped ledger document fresh discovery from source-linked evidence. No reviewed artifact indicates that a top-N boundary, an old candidate list, a review queue, or an expected count controlled discovery. This is supported by the durable workflow records; exact wall-clock creation order beyond their own statements is not independently timestamped in the artifacts.
- **Display-zero exclusion:** Neither statistical pass found a `P = 0`, `p = 0.000`, or equivalent display zero. No C ID mentions or depends on one, so no conditional independent-contradiction field is applicable.
- **Integrity:** `sha256sum -c` succeeds for all four direct sources and all 289 listed reused artifacts against the before-review ledgers. No source or reused-asset change was detected during this audit.
- **Links and pagination:** Every candidate PDF target inspected resolves to an existing supplied PDF and ends in `#page=N`; the cited pages contain the stated evidence. No false page number was found. Where a ledger link label names a page range but anchors its first page, the mechanical recheck provides page-specific links; the final report should preserve separate links for noncontiguous or separately relied-on pages.

## Required coordinator repairs before report completion

1. Repair the BMI arithmetic in `extraction/main_quantitative_evidence.md` MN15, `relationships/numeric_relationship_inventory.md` N015, `checkers/numeric_consistency.md` N015, and `checkers/cross_source_consistency.md` CROSS-LEAD-003. The printed vitamin D BMI counts sum to `63 + 62 + 59 + 65 = 249`, not 251; the placebo counts sum to `36 + 43 + 45 + 41 = 165`, not 166. C007 and its mechanical recheck already use the correct arithmetic.
2. Repair the SNP denominator description in main extraction MN19 and canonical N019. It is incorrect to say that every genotype triplet except Cdx2 totals the arm header. The vitamin D/placebo totals are FokI `245/157`, BsmI `231/150`, Cdx2 `230/150`, ApaI `231/150`, TaqI `231/150`, DBP1 `231/148`, and DBP2 `231/150`. C001 and its recheck already preserve the correct totals.
3. Repair the N010 arithmetic explanation. `42/417 = 10.07%`, which rounds to 10.1%, not 10.3%. The printed 10.3% is reproducible as `(15 + 10 + 9 + 9)/417 = 43/417 = 10.31%` when the separately displayed lost vitamin D participant is included in the narrative's 15 nonmedical discontinuations, as the source explicitly states. This is a checker explanation repair, not an additional stable candidate.
4. In C008, preserve the article's direct statement that participants were randomized and started supplementation at the first outpatient visit and its parenthetical equation of time from randomization with time from starting medication. The unresolved item is the unavailable participant-level date identity and analysis variable, not evidence that the two dates actually differed. Do not claim that any estimate, risk set, or conclusion changed.
5. In the coverage manifest, replace the generic `evidence_quality` and `report_generation` scopes with the explicit list `C001, C002, C003, C004, C005, C006, C007, C008, C009`, then set each row to `COMPLETE` only after its artifact exists.
6. The current ledger is not yet assembled as final report cards. For every C ID, the final report must add the exact report-spec labels identified below and must use the exact five-field blank human-adjudication template. No downstream statement may assert propagation, harm, or a paper-level conclusion change.

## C001 — Table 1 SNP percentages use smaller, variable, unlabelled denominators

- **Status:** Pending Human Adjudication.
- **Evidence support and arithmetic:** Direct Table 1 values and the supplement's repeated time-zero genotype counts support the smaller, variable denominator observation. The recheck reproduces all seven SNP totals and the Cdx2 percentages. The phrase `available-case denominator` is a plausible interpretation, not a directly printed mechanism; the final candidate statement should say `smaller, variable, unlabelled denominators` and reserve assay availability or failed calls for alternatives.
- **Category audit:** `Denominator, proportion, or total inconsistency` follows `QUALITY_CONTROL_SCOPE.md`.
- **Assumptions and observation/inference separation:** Counts, arm headers, percentages, footnote text, and derived triplet totals are direct or reproducible. Failed assays, uncalled genotypes, and available-case processing are inferred and must remain conditional.
- **Duplicate-relationship audit:** C001 is not a duplicate of C006, which concerns the CDK2/CDX2 label, or C007, which concerns BMI denominators. Numeric and cross-source leads for the same SNP-denominator rule were appropriately combined before stable registration.
- **Pagination and links:** Main p. 5 and supplement pp. 7-27 are truthful. The final card should use page-specific anchors for representative or relied-on genotype panels rather than treating a single p. 7 anchor as navigation to every page.
- **Conclusion and downstream bounds:** Nothing supports a paper-level conclusion change. A bounded downstream statement may say that, if the issue is confirmed, an extractor could copy arm-header denominators for SNP proportions or subgroup sample sizes.
- **Missing exact final-card fields:** `Candidate statement`, `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Alternative source-grounded interpretations`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields`. The ledger and recheck contain facts for these fields but do not yet present them under the required labels.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Figure 3 caption says panel-C risk numbers are absent although the panel prints them

- **Status:** Pending Human Adjudication.
- **Evidence support and calculation:** Direct visual inspection confirms two seven-value panel-C rows and the caption statement that panel-C numbers are not given. The reproducible logical calculation is 14 displayed risk values versus a statement of none; no model inference is required.
- **Category audit:** `Numeric or arithmetic inconsistency` is an allowed category and is suitable for the direct display-versus-caption contradiction.
- **Assumptions and observation/inference separation:** The printed rows and caption are direct. A stale caption, misplaced rows, or raw-versus-weighted distinction is only an alternative explanation.
- **Duplicate-relationship audit:** NUM-LEAD-002 and CROSS-LEAD-001 concern the same panel, comparator, and presence rule and were appropriately combined. No other C ID duplicates that relationship.
- **Pagination and links:** DOC-001 p. 7 is exact and the visual evidence is present there.
- **Conclusion and downstream bounds:** No conclusion impact is established. A bounded downstream statement may identify possible copying or interpretation of the displayed panel-C risk-set values if they are confirmed as unintended or differently defined.
- **Missing exact final-card fields:** `Candidate statement`, `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Alternative source-grounded interpretations`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields`. The `Calculation` field should state the exact 7 + 7 presence comparison rather than inventing an inferential calculation.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Final protocol gives different accrual stopping thresholds

- **Status:** Pending Human Adjudication.
- **Evidence support and arithmetic:** Final-protocol pp. 18 and 31 directly print `>400` and stopping after 400. The smallest integer satisfying `n > 400` is 401, while `240 + 160 = 400`. The source supports the literal threshold comparison.
- **Category audit:** `Denominator, proportion, or total inconsistency` is within scope because the issue is a concrete integer enrollment threshold.
- **Assumptions and observation/inference separation:** The two rules and integer comparison are direct/reproducible. Target-versus-cap wording, block completion, and operational implementation are unresolved alternatives. The main article's statement that entry exceeded 400 because the stopping rule was not met is useful source context and should be included as an alternative, without converting it into proof of which protocol sentence governed.
- **Duplicate-relationship audit:** This is distinct from the planned-versus-observed enrollment difference and from statistical interim-boundary S017; no separate C ID registers those nonidentical relationships.
- **Pagination and links:** DOC-002 pp. 18 and 31 are exact. The final card should link both pages separately.
- **Conclusion and downstream bounds:** No efficacy or safety conclusion impact is supported. A bounded downstream statement may concern extraction of the planned enrollment rule as target, cap, or stopping trigger.
- **Missing exact final-card fields:** `Candidate statement`, `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Alternative source-grounded interpretations`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields`.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Final protocol and report use multiple unqualified labels for de novo cancer

- **Status:** Pending Human Adjudication.
- **Evidence support and logical comparison:** The synopsis says adverse event and `not as an outcome`; the final body and change summary say tertiary outcome and separated from safety outcomes; the report presents counts in its adverse-event/safety table. These labels and counts are directly printed.
- **Category audit:** `Measure, label, or scale inconsistency` follows the normative category list.
- **Assumptions and observation/inference separation:** The label variation is direct. A dual clinical-ascertainment and statistical-hierarchy role is a source-grounded possible reconciliation but is not defined. To avoid overstatement, the final candidate statement should use `multiple unqualified labels` rather than claim that the categories cannot coexist under any definition.
- **Duplicate-relationship audit:** NUM-LEAD-004 and CROSS-LEAD-006 share the same event, label comparator, and rule and were appropriately combined. This is distinct from all numeric denominator candidates.
- **Pagination and links:** DOC-002 pp. 19, 25, 26, and 45 and DOC-001 p. 8 are truthful. The final report should give separate anchors for the separately relied-on pages.
- **Conclusion and downstream bounds:** No trial conclusion effect is established. A bounded downstream statement may say an extractor could classify the same counts as safety/adverse-event data or as a tertiary outcome if the hierarchy remains unclear.
- **Missing exact final-card fields:** `Candidate statement`, `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Alternative source-grounded interpretations`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields`. The `Calculation` field may state that no arithmetic is needed and enumerate the three directly compared labels.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — One final-protocol high-25(OH)D stratum label omits the boundary operator

- **Status:** Pending Human Adjudication.
- **Evidence support and logical comparison:** Protocol p. 23 prints high `(40 ng/mL)` after a middle category that includes 40; p. 31 and the article print high `>40 ng/mL`. The boundary-membership comparison is reproducible and does not depend on an observed participant at exactly 40.
- **Category audit:** `Measure, label, or scale inconsistency` is the applicable normative category.
- **Assumptions and observation/inference separation:** The absent operator and explicit comparators are direct. A typesetting omission or shorthand is inferred and must remain an alternative.
- **Duplicate-relationship audit:** NUM-LEAD-005, CROSS-LEAD-004, and STAT1-LEAD-001 use the same cutoff label and rule and were appropriately combined before C005. No other C ID duplicates it.
- **Pagination and links:** DOC-002 pp. 23 and 31 and DOC-001 p. 3 are exact; use separate page anchors in the final card.
- **Conclusion and downstream bounds:** No result or conclusion change is established, and no boundary participant is identified. A bounded downstream statement may concern copying an incomplete subgroup definition or assigning 40 ng/mL inconsistently.
- **Missing exact final-card fields:** `Candidate statement`, `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Alternative source-grounded interpretations`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields`. The `Calculation` field should explain membership of 40 under `20 <= x <= 40` and `x > 40` without asserting an observed reclassification.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Supplement labels Cdx2 genotype panels as CDK2

- **Status:** Pending Human Adjudication.
- **Evidence support and identity rule:** The protocol prints `CDX2, rs11568820`, Table 1 prints `Cdx2`, and supplement panels print `CDK2`. All six arm-by-genotype baseline counts match exactly, supporting the matched-result identity while leaving the intended locus for human confirmation.
- **Category audit:** `Measure, label, or scale inconsistency` is the applicable normative category.
- **Assumptions and observation/inference separation:** Labels and count identity are direct. A typesetting substitution or a coincident distinct-locus analysis is inferred; underlying genotype data and code are unavailable.
- **Duplicate-relationship audit:** This is distinct from C001 because C006 tests the locus label while C001 tests denominators. The cross-source lead was registered once.
- **Pagination and links:** DOC-001 p. 5, DOC-002 p. 27, and DOC-003 pp. 13-15 are exact. Use distinct anchors for all three supplement panels in the final card.
- **Conclusion and downstream bounds:** No treatment conclusion impact is supported. A bounded downstream statement may identify copying the wrong locus name or assigning subgroup HRs to a different genetic marker if the label is confirmed incorrect.
- **Missing exact final-card fields:** `Candidate statement`, `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Alternative source-grounded interpretations`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields`.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Table 1 BMI categories use smaller, unlabelled denominators than the arm headers

- **Status:** Pending Human Adjudication.
- **Evidence support and arithmetic:** Direct Table 1 values give vitamin D `63 + 62 + 59 + 65 = 249` and placebo `36 + 43 + 45 + 41 = 165`. Supplementary complementary BMI groups independently give `208 + 41 = 249` and `144 + 21 = 165`. Relative to 251/166, the deficits are 2 and 1. The ledger and recheck are correct.
- **Category audit:** `Denominator, proportion, or total inconsistency` follows the normative category list.
- **Assumptions and observation/inference separation:** Counts, sums, deficits, and repeated subgroup totals are direct/reproducible. Missing BMI or exclusion is inferred and no source states the mechanism.
- **Duplicate-relationship audit:** C007 is not a duplicate of C001 because it concerns a different variable, denominator set, comparator, and missingness question. The cross-source lead is one relationship, not separate vitamin D and placebo candidates.
- **Pagination and links:** DOC-001 p. 5 and DOC-003 pp. 32-33 are exact; separate anchors should be retained.
- **Conclusion and downstream bounds:** No efficacy conclusion impact is supported. A bounded downstream statement may say that an extractor could use 251/166 rather than the implied 249/165 when deriving BMI proportions or subgroup sample sizes.
- **Unsupported upstream statements requiring repair:** Main extraction MN15, canonical N015, numeric checker N015, and CROSS-LEAD-003 contain conflicting incorrect arithmetic as listed in the coordinator repairs. The final card must use the ledger/recheck arithmetic only after those artifacts are repaired.
- **Missing exact final-card fields:** `Candidate statement`, `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Alternative source-grounded interpretations`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields`.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — Report and final protocol use different labels for the survival time origin

- **Status:** Pending Human Adjudication.
- **Evidence support and limitation:** The article and axes print randomization; the protocol prints supplementation start. The article also directly says participants were randomized and started supplementation at the first outpatient visit and defines time from randomization parenthetically as time from starting study medication. Therefore, the supported observation is a label difference with an unavailable participant-level date/analysis-variable check, not a demonstrated difference in actual time zero.
- **Category audit:** `Measure, label, or scale inconsistency` remains within scope only when framed as this concrete definition-label comparison and unresolved implementation question.
- **Assumptions and observation/inference separation:** The two labels and article's equivalence statements are direct. Universal date equality, any delay, the analysis variable, and any effect on estimates are inferred or unavailable.
- **Duplicate-relationship audit:** The mapped RFS/OS relationships share this definition question and are appropriately represented by one stable ID. It is distinct from C003's enrollment threshold.
- **Pagination and links:** DOC-001 pp. 2 and 6, DOC-002 pp. 25 and 29, and DOC-003 pp. 2-3 are exact. Use separate anchors for every relied-on page in the final card.
- **Conclusion and downstream bounds:** Do not state that risk sets, HRs, follow-up, or conclusions changed. A bounded downstream statement may say that an extractor could record different time-origin labels unless the operational equivalence and analysis variable are clarified.
- **Required wording repair:** Replace any unqualified statement that the documents used different actual time origins with the precise statement that they use different labels while the article explicitly treats the events as contemporaneous. Preserve the exact unresolved human question about stored dates and analysis code.
- **Missing exact final-card fields:** `Candidate statement`, `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Alternative source-grounded interpretations`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields`. The `Calculation` field should state that no numeric estimate can be recalculated and identify the missing participant-level dates and code.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C009 — Table 2 hazard-ratio direction footnote is opposite the displayed outcome direction

- **Status:** Pending Human Adjudication.
- **Evidence support and diagnostic arithmetic:** Table 2 directly says HR values greater than 1 indicate decreased outcome probability with vitamin D. Figure 2C and the narrative pair lower vitamin D relapse incidence with subdistribution HRs below 1. Direct counts also give relapse `41/251 = 16.33%` versus `36/166 = 21.69%`, noncancer death `10/251 = 3.98%` versus `9/166 = 5.42%`, and cancer-specific death `27/251 = 10.76%` versus `16/166 = 9.64%`, with printed HR directions opposite the footnote. These crude proportions are diagnostics, not reconstructions of time-to-event models.
- **Category audit:** `Measure, label, or scale inconsistency` is the applicable normative category.
- **Assumptions and observation/inference separation:** Footnote, counts, curves, narrative direction, and HRs are direct. A table-only reversed contrast or production error is inferred. Event times, censoring, model code, and explicit per-row reference orientation are unavailable.
- **Duplicate-relationship audit:** S009-S012 share one table-wide footnote-direction rule and are appropriately represented by one stable ID, not separate candidates by row. Statistical pass 2 independently revisited the relationship and did not add a duplicate.
- **Pagination and links:** DOC-001 pp. 4, 6, and 7 are exact. Use three separate anchors in the final card.
- **Conclusion and downstream bounds:** No treatment conclusion change is established. A bounded downstream statement may identify copying the HR direction or treatment-reference interpretation incorrectly if the footnote is confirmed reversed.
- **Missing exact final-card fields:** `Candidate statement`, `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Alternative source-grounded interpretations`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields`. The calculation must retain the diagnostic qualifier and must not claim to reproduce the HRs.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Limitations and final handoff

- Individual-level data, event and censoring times, genotype assay-call logs, figure-production files, analysis code, and participant-level randomization/first-dose dates are not supplied. Those gaps limit mechanism and implementation checks but do not leave a direct-source page unmapped.
- Exact statistical P-value reconstruction is unavailable where the package omits the matched test statistic, sidedness, variance estimator, degrees of freedom, covariance, confidence-interval construction, adjustment, or reference orientation. Both passes appropriately restrict those relationships to containment, endpoint order, null/P-threshold, label, and repeated-result checks.
- The planned Freedman/log-rank sample-size output is source-printed and arithmetically coherent in N and allocation, but exact software reconstruction is not established from a retained command execution artifact. It is not used as the sole basis of a C ID.
- The stable ID set for the ledger, recheck, this quality artifact, and the intended report is exactly C001-C009. No stable ID is deleted, merged, renumbered, ranked, or suppressed by this audit.
- Report generation, final manifest status changes, after-review hash ledgers, token accounting, HTML rendering, and final validation occur after this audit and remain coordinator responsibilities.
