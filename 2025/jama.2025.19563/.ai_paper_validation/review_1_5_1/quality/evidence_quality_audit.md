# Final Evidence-Quality Audit — Workflow 1.5.1

## Audit scope and outcome

This audit covers the complete source and evidence-asset inventories, source coverage ledger, coverage manifest, canonical and shard-level quantitative extractions, numeric and statistical relationship inventories, numeric checker, cross-source checker, both statistical passes, stable candidate ledger, direct-source evidence recheck, and agent execution manifest. Direct supplied PDFs were used to resolve pagination and calculation questions. No web source, external literature, old candidate list, old review queue, or top-N boundary was used.

- **Audit status:** COMPLETE WITH REQUIRED REPORT-TIME REPAIRS.
- **Stable candidate IDs audited:** C001, C002, C003, C004, C005, C006, C007 (7/7).
- **Stable-ID preservation:** No stable ID was deleted, merged, renumbered, ranked, suppressed, or scientifically adjudicated.
- **Candidate status:** Every stable ID remains **Pending Human Adjudication**.
- **Display-zero control:** No mapped relationship or candidate displays `P = 0`, `p = 0.000`, or equivalent. No stable ID is based on display-zero notation.

## Complete-coverage controls

### Direct-source closure

| Source ID | Total units | Reusable units | Fresh-required units | Partition check | Mapped units | Closure |
|---|---:|---:|---:|---|---:|---|
| DOC-001 | 11 | 11 | 0 | 11 + 0 = 11 | 11 | COMPLETE |
| DOC-002 | 90 | 0 | 90 | 0 + 90 = 90 | 90 | COMPLETE |
| DOC-003 | 69 | 31 | 38 | 31 + 38 = 69 | 69 | COMPLETE |
| **Total** | **170** | **42** | **128** | **42 + 128 = 170** | **170** | **COMPLETE** |

All direct-source page counts were independently consistent with `pdfinfo`: 11, 90, and 69 pages. The six support-mapping shards and one main-mapping shard are disjoint and collectively cover all 170 pages. No-applicable pages are explicitly recorded in the mapper artifacts rather than omitted.

### Discovery-boundary control

The reusable-asset curator treated the old page/document maps only as provenance and locators. DOC-002 pp. 1-90 and DOC-003 pp. 1-33, 36-37, and 67-69 were assigned fresh direct-source mapping because reusable page-level extraction was absent. The current inventories contain N001-N117 and S001-S034, the numeric and cross-source checkers cover their full assigned scopes, and candidate discovery continued without a count target. Nothing in the current artifacts indicates that an old candidate set, review queue, ten-candidate boundary, or desired finding count controlled discovery.

### Coverage-manifest control

Every existing manifest row contains exactly one plain relative artifact path. All completed artifact targets resolve. At the time of this audit, only the expected downstream rows remained unfinished: `evidence_quality` and `report_generation`. The coordinator must update `evidence_quality` to `COMPLETE` with exact scope `C001; C002; C003; C004; C005; C006; C007` after accepting this artifact, and must complete `report_generation` after the full report is assembled.

### Relationship and statistical-pass closure

- Numeric inventory and numeric checker: 117/117 distinct IDs, N001-N117.
- Statistical inventory: 34/34 distinct IDs, S001-S034.
- Statistical pass 1: 34/34 S IDs have a relationship-level record under the `PASS_1_COMPLETE result` register.
- Statistical pass 2: 34/34 S IDs have a relationship-level record under the `PASS_2_COMPLETE result` register, and the canonical inventory also records 34/34 pass-2 states.
- Pass 1 runtime ID `/root/statistical_pass_1` and pass 2 runtime ID `/root/statistical_pass_2` are distinct fresh spawns, each recorded as `gpt-5.6-terra`, reasoning effort `high`, with a unique primary artifact.
- Candidate ledger and evidence recheck ID sets are identical: C001-C007.

One extraction/inventory transcription requires correction before report assembly: DOC-002 PDF p. 37 states that the sample-size criterion uses the upper limit of a **one-sided 95% confidence interval**. `parts/mapping/support_DOC002_p031-p060.md` under D2B-N006 and `statistics/relationship_inventory.md` under S009 incorrectly say “two-sided 95%.” Both statistical checker passes use the correct one-sided wording. The final report must use the direct-source wording, and the coordinator should repair the two canonical workflow records.

## Candidate-level audit

## C001 — Protocol and reported primary endpoint differ on the diabetes-range A1C failure condition

- **Status:** Pending Human Adjudication.
- **Category audit:** `Cross-document numeric inconsistency` is supportable because the compared definitions govern a binary numeric endpoint classification. The card must not claim that any reported success count or noninferiority conclusion actually changed.
- **Evidence and location audit:** Protocol DOC-002 p. 15 prints `A or B or C`. Main DOC-001 p. 4 adds the below-6.5%-throughout condition. Supplement DOC-003 p. 30, not p. 56, explicitly states that diabetes-range participants were marked as endpoint failures regardless of body-weight and physical-activity improvements. DOC-003 p. 56 lists the 15 participant instances and thresholded A1C values. The ledger's location/evidence wording must be repaired to cite p. 30 for the global-failure rule and p. 56 only for the instance list.
- **Reproducible rule:** Protocol classification is `A or B or C`; reported classification is `(A or B or C) and D`, where `D` is absence of diabetes-range A1C during the defined visits. The 15 participants' component achievements are unavailable, so no affected-count calculation is supportable.
- **Observation/inference and alternative:** Printed definitions and the 15 instances are observations. A governing amendment, production history, and any change to 117 successes are unconfirmed alternatives or inferences. The dated final amendment/SAP and participant component statuses are missing.
- **Duplicate review:** Distinct from all other IDs; it concerns the endpoint rule, not A1C device availability or an inferential value.
- **Neutral and bounded report wording:** If confirmed, an evidence extractor could copy an incomplete endpoint definition or classification rule. Do not state that the paper's conclusion changed or that downstream propagation occurred.
- **Exact human question:** Was the global diabetes-range A1C failure rule prospectively adopted in a dated governing amendment or final analysis plan, and how many of the 15 listed participants otherwise met a success component?
- **Missing final-card fields in the ledger:** exact `Candidate statement`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields` labels must be supplied in the final report.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — 312 listed 12-month A1C measurements versus 313 participants with A1C available

- **Status:** Pending Human Adjudication.
- **Category audit:** `Denominator, proportion, or total inconsistency` matches the displayed count identity.
- **Evidence and location audit:** DOC-003 p. 8 prints follow-up method counts 282, 30, and 0. DOC-001 pp. 4-5 prints 313 complete outcomes and 26 plus 29 missed visits. DOC-003 pp. 48-50 prints 26 and 29 missing A1C values and states that completers had no missing A1C. The cited pagination is supportable.
- **Reproducible rule:** `282 + 30 + 0 = 312`; independently, `368 - (26 + 29) = 313`. The difference is one participant. The method rows' exhaustiveness is a necessary unresolved premise, not a direct observation.
- **Observation/inference and alternative:** Counts and missingness statements are observations. An unlisted method, including the Siemens DCA Vantage named in the source narrative, is a source-grounded alternative. Participant-level logs and an explicit exhaustiveness statement are absent.
- **Duplicate review:** Distinct from C001; this concerns A1C measurement-method accounting, not endpoint classification.
- **Neutral and bounded report wording:** If confirmed, an extractor could copy an incorrect A1C availability total or incomplete device-method breakdown. Do not imply that the outcome estimate changed.
- **Exact human question:** Which of the 313 participants with nonmissing 12-month A1C is absent from the 312 displayed method counts, and what method produced that result?
- **Missing final-card fields in the ledger:** exact `Candidate statement`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields` labels must be supplied in the final report.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Figure 3 labels BMI values in kg/m² as “weight”

- **Status:** Pending Human Adjudication.
- **Category audit:** `Measure, label, or scale inconsistency` matches the label/unit identity.
- **Evidence and location audit:** DOC-001 p. 8 Figure 3 prints “weight” with kg/m² and both arm triplets; DOC-001 p. 6 prints the identical triplets in the BMI row. DOC-003 p. 53 supplies supporting BMI-unit usage. Pagination and values reproduce.
- **Reproducible rule:** The six arm-specific median/IQR values match exactly; kg/m² is the printed BMI unit, while weight alone is a mass quantity. No rounding assumption is needed.
- **Observation/inference and alternative:** Words, units, values, arm labels, and time point are observations. A carried-over figure label or shorthand is an inferred production explanation. No literal weight-in-kilograms comparator is supplied.
- **Duplicate review:** Distinct label/unit relationship; no overlap with the other stable IDs' comparators or rules.
- **Neutral and bounded report wording:** If confirmed, a figure-data extractor could misrecord BMI as body weight or assign the wrong unit. Do not infer any change to a treatment effect.
- **Exact human question:** Was Figure 3 footnote a intended to identify baseline BMI, or is another weight measure and unit intended?
- **Missing final-card fields in the ledger:** exact `Candidate statement`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields` labels must be supplied in the final report.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — eTables 5-7 repeat an age P-value statement beneath different comparison tables

- **Status:** Pending Human Adjudication.
- **Category audit:** `Cross-document numeric inconsistency` is supportable as a cross-location P-value/comparator-label issue. The final card should emphasize scope ambiguity rather than assume an unstated comparator.
- **Evidence and location audit:** DOC-003 pp. 39-40, 42-43, 44-45, and 46-47 repeat `p = 0.014`. eTables 5-7 display site, baseline-A1C, and completion-status contrasts. eTable 5 separately reports site-age `p = 0.017`. The ledger title and cross-source checker overstate that p=.014 is definitively the treatment-group result and that eTable 3 itself displays treatment arms; eTable 3 has an overall randomized-cohort column. The main DOC-001 p. 6 arm comparison prints `P = .01`, which is compatible at coarser precision and supports, but does not prove, the treatment-arm interpretation. The final card must frame the issue as unresolved comparator scope.
- **Reproducible rule:** A P value is identified by population, outcome, and contrast. The same unlabeled statement occurs beneath tables whose displayed contrasts differ. Summary values do not permit recreation of all rank-based P values.
- **Observation/inference and alternative:** Repeated text, table titles/columns, and site-age p=.017 are observations. Treatment-arm attribution and copied-footnote history are inferences. An intentionally global note is a source-grounded alternative.
- **Duplicate review:** Distinct from C005. C004 concerns the comparator/scope of the repeated p=.014 note; C005 concerns the reversed inequality in a different eTable 7 footnote.
- **Neutral and bounded report wording:** If confirmed, an extractor could attach p=.014 to the wrong table contrast. Do not claim that any recalculated P value differs because individual-level ages and test outputs are absent.
- **Exact human question:** At each eTables 5-7 occurrence, which population and contrast does `p = 0.014` describe, and what comparator label was intended?
- **Missing final-card fields in the ledger:** exact `Candidate statement`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields` labels must be supplied in the final report.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — eTable 7 pairs “no statistically significant” with p<0.05

- **Status:** Pending Human Adjudication.
- **Category audit:** `Statistical reporting inconsistency` matches the sentence/inequality contradiction.
- **Evidence and location audit:** DOC-003 p. 47 contains both the no-significance sentence with `p<0.05` and the neighboring statement using `p=.014` for a difference and `p>0.05` for similarity. Pagination is exact.
- **Reproducible rule:** The page's own convention makes `0.014 < 0.05` correspond to a difference and `p>0.05` to similarity; the no-significance sentence paired with `p<0.05` reverses that relationship. No unreported characteristic-specific P value is inferred.
- **Observation/inference and alternative:** The sentence and symbols are observations. Sign error, omitted qualifier, or copied note are inferred alternatives. Completion-status analysis outputs are missing.
- **Duplicate review:** Not a duplicate of C004 because it uses a different printed statement and a different consistency rule.
- **Neutral and bounded report wording:** If confirmed, an extractor could reverse the table's significance summary or inequality. Do not infer which characteristics differed.
- **Exact human question:** What were the completion-status comparison results, and what inequality and scope were intended in footnote 1?
- **Missing final-card fields in the ledger:** exact `Candidate statement`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields` labels must be supplied in the final report.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — eTable 10b labels one comparison as both chi-squared and Wilcoxon rank-sum

- **Status:** Pending Human Adjudication.
- **Category audit:** `Statistical reporting inconsistency` matches the conflicting named-test labels.
- **Evidence and location audit:** DOC-003 p. 29 specifies chi-squared for the prohibited-medication proportion comparison; p. 52 prints 6/183, 7/185, `P = 0.793`, and a Wilcoxon rank-sum footnote. Pagination and values reproduce.
- **Reproducible rule:** The same binary arm comparison carries two named test labels. The proportions reproduce: `6/183 = 3.28%` and `7/185 = 3.78%`. A pooled uncorrected two-proportion/Pearson diagnostic is approximately compatible with .793, but cannot identify the generating software procedure and must remain diagnostic only.
- **Observation/inference and alternative:** Counts, denominators, P value, and labels are observations. The actual procedure, options, and any copied-footnote history are inferences. A binary rank-based implementation can be numerically close and is not excluded by the displayed P value alone.
- **Duplicate review:** Distinct from C005 and C007; the rule is named-test identity, not inequality direction or arm-percentage/RD arithmetic.
- **Neutral and bounded report wording:** If confirmed, an extractor could record the wrong statistical test for P=.793. Do not claim that the P value itself is wrong.
- **Exact human question:** Which named software procedure and options generated `P = 0.793`, and which printed test label describes it?
- **Missing final-card fields in the ledger:** exact `Candidate statement`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields` labels must be supplied in the final report.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — MICE pooled percentages and printed risk difference have incompatible signs

- **Status:** Pending Human Adjudication.
- **Category audit:** `Statistical reporting inconsistency` matches the displayed estimate/arithmetic relationship.
- **Relationship-provenance audit:** Add numeric relationship N110 to the final card alongside S019 and S031. N110 is the canonical numeric record for the same eTable 16 printed percentages and risk difference; omitting it would lose cross-lane relationship provenance even though the numeric checker itself did not promote a provisional candidate.
- **Evidence and location audit:** DOC-003 p. 30 supplies MICE/Rubin context; p. 59 prints AI 32.2%, human 31.9%, and AI-minus-human RD -1.1 pp with lower bound -11.5. Pagination and column order reproduce.
- **Reproducible rule:** Direct subtraction is `32.2 - 31.9 = +0.3` pp, whereas the table prints -1.1 pp. If values rounded conventionally to one decimal, the underlying displayed-value difference is approximately **+0.2 to +0.4 pp**, not the `+0.1 to +0.5` range stated in the pass-1 candidate text and ledger. The report must use the corrected bound. The confidence bound is not reproducible from displayed marginals alone.
- **Observation/inference and alternative:** Percentages, RD, lower bound, MICE method, and column order are observations. An adjusted/standardized estimand, separate pooling scale, contrast reversal, and production error are alternatives or inferences. Full per-imputation outputs, model, coding, covariance, and pooling calculations are absent.
- **Duplicate review:** Distinct from C006; it concerns estimate sign/arithmetic, not a test label.
- **Neutral and bounded report wording:** If confirmed, an extractor could copy a risk difference whose sign does not match the displayed arm percentages or could copy the wrong arm percentages. Do not claim that the confidence bound, noninferiority result, or paper conclusion is wrong.
- **Exact human question:** What estimand, contrast order, model, and pooling calculation produced -1.1 pp, and is it intended to be directly comparable with 32.2% and 31.9%?
- **Missing final-card fields in the ledger:** exact `Candidate statement`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields` labels must be supplied in the final report.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Required report-time repairs and controls

1. Repair C001 pagination and evidence wording: cite DOC-003 p. 30 for the global failure clause and p. 56 for the 15-instance table.
2. Frame C004 as an unresolved P-value comparator/scope label. Do not state as direct fact that eTable 3 displays treatment arms or that p=.014 is definitively the treatment-arm result.
3. Correct C007's one-decimal rounding interval to approximately +0.2 to +0.4 percentage points and add N110 to its relationship provenance alongside S019 and S031.
4. Use “one-sided 95% confidence interval” for DOC-002 p. 37 and repair the contrary “two-sided” text in D2B-N006 and S009 before relying on those records in the report.
5. Populate every final evidence card with all exact report-spec labels. Preserve a separate observation, comparator, rule, calculation, source-grounded alternative, bounded relevance statement, bounded downstream statement, and human verification procedure.
6. For every final card, use exactly the five human-adjudication subfields shown in this audit and retain `__` for every blank. Do not add validity, importance, action, initials, or notes content.
7. Preserve all seven IDs and the exact status `Pending Human Adjudication`. Do not use severity terms or scientific disposition labels.
8. Update the `evidence_quality` coverage-manifest row to exact scope `C001; C002; C003; C004; C005; C006; C007`, artifact `quality/evidence_quality_audit.md`, status `COMPLETE`. Complete the analogous report row only after all seven cards are assembled.

## Residual audit limitations

The package lacks the protocol/SAP amendment history and participant-level component outcomes needed to resolve C001; participant-level A1C/device logs needed to resolve C002; source-production files for the figure/table labels and footnotes in C003-C006; and full imputation/model/pooling output needed to resolve C007. Several planned statistical relationships lack formula, variance, covariance, degrees-of-freedom, sidedness, or model-output details; those quantities were not reconstructed. DOC-002's glyph-encoded native text required direct CPU-rendered page review. These are resolution or derivative limitations, not source-coverage gaps.

`EVIDENCE_QUALITY_AUDIT_COMPLETE`
