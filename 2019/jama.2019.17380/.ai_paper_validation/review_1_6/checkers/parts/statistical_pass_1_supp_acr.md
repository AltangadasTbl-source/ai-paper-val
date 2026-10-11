# Statistical Pass 1: Supplement ACR Checker Part

- Agent: /root/stats_pass1_supp_acr, fresh gpt-6.1-sol/high; runtime ID tracked by coordinator.
- Exact scope: DOC-003 REPORT, joi190122supp2_prod.pdf pp. 11–14, eTables 6, 7, 8, and 9; all 96 estimate/95% CI fields plus 8 year-5 P values paired to contrasts.
- Inventory: statistics/parts/pass1_supp_acr_inventory.md; S401–S496, each PASS_1_COMPLETE.
- Independent emitted candidates: 1 (STAT-UA01); no stable C ID assigned by this checker.
- Limitations: exact table-specific marginal/change CI estimators, contrast test statistic, SE, reference distribution, df, covariance, variance estimator and MI pooling output unavailable. No source-coverage gap.
- Provenance: direct Poppler 26.01.0 pdftotext -layout -f 11 -l 14 joi190122supp2_prod.pdf -; source-matched current maps; visual source-matched reusable p12 render. No old candidates or report conclusions read, no web, no OCR required.

## Scope accounting

| Table and page | Relationships | Marginal GM/95% CI | Within-assignment ratio/95% CI | Active/placebo ratio/95% CI | Paired P | Completed |
|---|---|---:|---:|---:|---:|---|
| eTable6 p11 | S401–S424 | 12 | 8 | 4 | 2 | PASS_1_COMPLETE |
| eTable7 p12 | S425–S448 | 12 | 8 | 4 | 2 | PASS_1_COMPLETE |
| eTable8 p13 | S449–S472 | 12 | 8 | 4 | 2 | PASS_1_COMPLETE |
| eTable9 p14 | S473–S496 | 12 | 8 | 4 | 2 | PASS_1_COMPLETE |
| Total | 96 independent fields | 48 | 32 | 16 | 8 | PASS_1_COMPLETE |

Individual records, values, fields, row N, role, model and footnote definitions are retained in the inventory. A year-5 P remains integral to its D record. Baseline reference constants are recorded as 1.0 (Ref.) and do not inflate the interval count.

## Completed statistical checks and absence of other candidates

Every one of 96 points is contained in its positive, correctly ordered printed 95% CI. GM values use mg albumin/g creatinine; CA/CP/D use dimensionless ratios. Within-assignment change refers to baseline with reference1, and D compares active change against corresponding placebo change with null1. All 32 nonbaseline within-assignment ratios and lower endpoints exceed1; larger follow-up ACR geometric means are directionally compatible with increase. No negative-ratio or swapped-endpoint contradiction occurs.

All 16 active/placebo CIs include1 at printed precision. Eight year-5 P values (.90,.64,.77,.44,.87,.94,.90,.80 in table/intervention order) exceed.05. The interval/P observation is a qualitative diagnostic only: printed same-contrast 95% CI and P do not furnish the full inferential definition required to calculate exact P from the interval. No CI/P candidate is emitted on an assumed normal distribution, assumed df, assumed covariance, or assumed MI pooling rule. The two rounded1.00 year-2 lower endpoints receive no significance interpretation and have no printed P.

All label, reference, direction, duplicate-value and matched-repeat checks in the inventory are complete. Distinct sensitivity populations remain distinct; repeated rounded estimates do not by themselves establish duplication. Mixed-model adjusted contrast estimates are not required to equal divisions of separately imputed unadjusted summaries. Generic units boilerplate mentioning SD does not supersede explicit95% CI headers. No display-zero P occurs; the display-zero exclusion was applied.

## STAT-UA01 — ACR complete-case population count differs between title/arm totals and inclusion footnote

**Candidate statement:** eTable7 labels the baseline/year-5 available-measurement ACR analysis N=944 and prints active/placebo arm counts summing to944 for both assignments at baseline and year5. Its footnote says991 participants donated both urine samples and “were included in this analysis.” These reported inclusion totals differ by47.

**Suggested primary category for registration:** Denominator, proportion, or total inconsistency.

**Compared document roles and exact locations:**

1. REPORT DOC-003 results supplement [PDF p12](../../../../joi190122supp2_prod.pdf#page=12), eTable7 title: “Among Participants With Available Baseline and Year 5 Measurements (N = 944*)”.
2. REPORT DOC-003 same [PDF p12](../../../../joi190122supp2_prod.pdf#page=12), eTable7 Vitamin D baseline and year5 N columns:504 active,440 placebo; omega-3 baseline and year5 N columns:477 active,467 placebo.
3. REPORT DOC-003 same [PDF p12](../../../../joi190122supp2_prod.pdf#page=12), eTable7 footnote*:1,312 enrolled;1,311 donated baseline urine;991 also donated year5 urine “and were included in this analysis”;320 baseline-only participants excluded;1 without baseline urine excluded.

**Relationship role rationale:** all discrepancy endpoints lie within one non-plan results supplement, so S_W. No PLAN comparator is implicated. Classification ambiguity: donation versus analyzable measurement may be different populations, but the footnote expressly calls991 included in this analysis.

**Relationships affected:** population key P7 and all eTable7 field records S425–S448. No estimate/CI containment contradiction is alleged.

**Printed rule and reproducible calculation:** active and corresponding placebo assignment arms partition a factorial-assignment comparison;504+440=944 and477+467=944. The footnote's own arithmetic is coherent:1,311−320=991;1,312−320−1=991. But991−944=47. A complete-case analysis described by a single N cannot simultaneously have included totals944 and991 without a supplied distinction.

**Tolerance:** integer count identities; rounding tolerance0 participants. This is not an interval- or P-value approximation.

**Direct observation versus inference:** the title944, four arm totals944 and explicit footnote991 are direct printed observations confirmed by current direct PDF text and the source-matched rendered p12 page. The numerical difference47 is exact arithmetic. A copied footnote or an extra47-person assay/missing-measurement exclusion is a possible explanation, not a supplied fact.

**Source-grounded alternatives and missing definitions:** the table could include only participants with analyzable ACR values, while991 donated urine; donor status and available measured ACR need not be identical. The source provides no47-person attrition bridge and says991 were included, leaving the label conflict. The MI footnotes might use a larger inferential population than displayed complete-case N, but no such distinct991-person modeling population is identified in the title or footnote. No participant-level assay-validity record or model N is supplied.

**Exact human question:** Which population and exclusion rule generated eTable7's geometric means, change ratios, CIs and P values:944 with analyzable baseline/year5 ACR,991 donors, or different descriptive/model populations? What supplied record accounts for47 people between donation and reported available measurements?

**Human verification steps:** open source PDF p12; read title and all four baseline/year5 assignment totals; read footnote* and its exclusions; identify any stated distinction between donated urine and analyzable paired ACR or between descriptive and MI model N. Recompute both independent sums and footnote remainder. Preserve the candidate pending that definition.

**Quality-control relevance:** the printed population attached to an ACR complete-case sensitivity result is inconsistent. If confirmed, a downstream extractor could copy the wrong analysis sample size or available-case definition. This does not establish that the estimates or the paper conclusion are wrong.

**Status:** Pending Human Adjudication. No severity, validity, acceptance, or correction assigned.

## Handoff

Complete assigned scope: all96 ACR estimate/95% CI fields, all8 paired P values, all baseline reference constants, model/scale/population footnotes and within-scope repetitions. One candidate, STAT-UA01. Coordinator may merge this with a genuine numeric-lane duplicate before C IDs. Fresh pass2 must revisit every S record using complete cross-lane ledger and recheck; this pass1 agent must not serve as pass2.

