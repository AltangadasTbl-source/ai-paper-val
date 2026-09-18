# jama.2024.27643

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2025 |
| Paper | jama.2024.27643 |
| Candidates | 8 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2025/jama.2024.27643/)

## Review setup

Edit the Markdown source. Empty cells mean unanswered. AI suggestions are reference only. All statuses and counts below are maintained manually.

| Field | Value |
| --- | --- |
| Stage | primary |
| Primary reviewer ID |  |
| Primary reviewer name |  |
| Checker ID |  |
| Checker name |  |
| Primary completed on |  |
| Primary backup or revision reference |  |
| Checker completed on |  |
| Paper status | not\_started |

Use `primary` or `checker` for Stage. Use `not_started`, `in_progress`, `primary_ready`, or `final_ready` for Paper status. Follow the [handoff instructions](../USAGE.md#handoff) before starting checking.

## Paper results

Leave final counts blank until every candidate is final. Zero means reviewed and none found. These are candidate counts, not independently deduplicated issue counts.

| Outcome | Final candidate count |
| --- | --- |
| primary\_temporal |  |
| secondary\_temporal |  |
| protocol\_descriptive |  |
| plan\_descriptive |  |
| not\_eligible |  |
| total\_final |  |

## Candidate index

- [C001](#candidate-c001) — Shared-placebo race missingness does not reconcile with the printed denominator (S_W)
- [C002](#candidate-c002) — SVC values have incompatible monthly-rate and 24-week-change labels (S_C)
- [C003](#candidate-c003) — Shared-placebo ALSFRS-R credible-interval endpoints differ for the cited primary model (S_C)
- [C004](#candidate-c004) — Pooled-active ALSFRS-R credible-interval endpoints differ for the cited primary model (S_C)
- [C005](#candidate-c005) — Bayesian mortality event rates differ between article text and cited eTable 2 (S_C)
- [C006](#candidate-c006) — Plasma NfL confidence intervals differ across Figure 3, narrative, and eTable 3B (S_C)
- [C007](#candidate-c007) — Serum NfL regimen-only values and contrast differ across displays (S_C)
- [C008](#candidate-c008) — Discussion total of 13 events conflicts with the 14 events displayed in Table 2 (S_W)

## Candidate C001

**Shared-placebo race missingness does not reconcile with the printed denominator**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2024.27643::C001 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> jama\_berry\_2025\_oi\_240158\_1742927563.7361.pdf — Table 1 and footnote b, PDF p. 6

### Candidate statement

> The displayed shared-placebo race accounting has a one-participant mismatch.

### AI rationale

> Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. The printed group total is 164 and the printed race denominator/category sum is 160, whereas the footnote reports 3 unknown or unreported participants.

### Human assessment

Fill Primary during initial review. At handoff, preserve Primary and copy its eight answers into Checker / final. Edit only Checker / final during checking. A blank final answer does not inherit a primary answer.

| Field | Primary | Checker / final |
| --- | --- | --- |
| Disposition |  |  |
| Review domain |  |  |
| Statistcal\_or\_numerical issue |  |  |
| Substantiveness |  |  |
| Downstream impact |  |  |
| Report-internal or planning-material inconsistency |  |  |
| Protocol interpretation |  |  |
| Notes (optional) |  |  |
| Complete | no | no |

| Checker record | Value |
| --- | --- |
| Checker result |  |
| Checker comment |  |
| Discussion resolution |  |
| Resolution note |  |
| Final outcome |  |

For `agree`, all eight effective final answers must equal Primary. Other checker results require a comment. `disagree`, `unable`, or a primary `discuss` require resolved discussion and a note naming participants and the conclusion. Leave Final outcome blank until final readiness.

### Evidence

#### Evidence 0: Source evidence

> Shared placebo is n=164; the race rows are Asian 2/160, Black or African American 6/160, White 151/160, and multiple races 1/160. Footnote b says race was unknown or unreported for 3 participants.

#### Evidence 1: Reported-versus-comparator

> The printed group total is 164 and the printed race denominator/category sum is 160, whereas the footnote reports 3 unknown or unreported participants.

#### Evidence 2: Calculation

> 2 + 6 + 151 + 1 = 160; 164 - 160 = 4; 4 - 3 = 1.

#### Evidence 3: Alternative source-grounded interpretations

> The denominator may be a complete-case subset excluding one additional status, or a numerator, denominator, or footnote may be printed incorrectly; the table gives no separate subset definition.

### Source links

- sourceLinks 0: [jama\_berry\_2025\_oi\_240158\_1742927563.7361.pdf — Table 1 and footnote b, PDF p. 6](../../../2025/jama.2024.27643/jama_berry_2025_oi_240158_1742927563.7361.pdf#page=6)

[Original Markdown report](../../../2025/jama.2024.27643/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity |  |
| broadPlanInvolved | 0 |
| category | Denominator, proportion, or total inconsistency |
| currentReportCrossDocument | 0 |
| id | C001 |
| key | 2025::jama.2024.27643::C001 |
| legacyRelationship |  |
| locations | jama\_berry\_2025\_oi\_240158\_1742927563.7361.pdf — Table 1 and footnote b, PDF p. 6 |
| originalCrossDocument | 0 |
| package | jama.2024.27643 |
| planMechanism |  |
| primary | S\_W |
| rationale | Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. The printed group total is 164 and the printed race denominator/category sum is 160, whereas the footnote reports 3 unknown or unreported participants. |
| reportHref | ../../2025/jama.2024.27643/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2025/jama.2024.27643/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | The displayed shared-placebo race accounting has a one-participant mismatch. |
| submissionInvolved | 1 |
| subtype | Shared-placebo race missingness does not reconcile with the printed denominator |
| suggestedDomain | statistical\_results |
| title | Shared-placebo race missingness does not reconcile with the printed denominator |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C002

**SVC values have incompatible monthly-rate and 24-week-change labels**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2024.27643::C002 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> jama\_berry\_2025\_oi\_240158\_1742927563.7361.pdf — Secondary Efficacy Outcomes, PDF p. 4; joi240158supp3\_prod\_1742927563.7911.pdf — eTable 3A, PDF p. 16

### Candidate statement

> Identical SVC values are labelled as monthly rates in the article and as 24-week change estimates in eTable 3A.

### AI rationale

> Target explicitly compares current main article and non-plan results supplement/workbook. A monthly rate is printed in the article; a cumulative 24-week change label is printed for the same values in the cited table.

### Human assessment

Fill Primary during initial review. At handoff, preserve Primary and copy its eight answers into Checker / final. Edit only Checker / final during checking. A blank final answer does not inherit a primary answer.

| Field | Primary | Checker / final |
| --- | --- | --- |
| Disposition |  |  |
| Review domain |  |  |
| Statistcal\_or\_numerical issue |  |  |
| Substantiveness |  |  |
| Downstream impact |  |  |
| Report-internal or planning-material inconsistency |  |  |
| Protocol interpretation |  |  |
| Notes (optional) |  |  |
| Complete | no | no |

| Checker record | Value |
| --- | --- |
| Checker result |  |
| Checker comment |  |
| Discussion resolution |  |
| Resolution note |  |
| Final outcome |  |

For `agree`, all eight effective final answers must equal Primary. Other checker results require a comment. `disagree`, `unable`, or a primary `discuss` require resolved discussion and a note naming participants and the conclusion. Leave Final outcome blank until final readiness.

### Evidence

#### Evidence 0: Source evidence

> The article calls -9.32, -8.53, and -0.78 PPN per month over 24 weeks. eTable 3A presents the same values under 24-week Change Estimate for SVC (% predicted).

#### Evidence 1: Reported-versus-comparator

> A monthly rate is printed in the article; a cumulative 24-week change label is printed for the same values in the cited table.

#### Evidence 2: Calculation

> The identical numeric triplet is -9.32, -8.53, and -0.78 in both locations; the printed labels describe different scales and the supplied sources give no conversion or estimand definition that reconciles them.

#### Evidence 3: Alternative source-grounded interpretations

> Per month may be an editorial unit label, or the eTable heading may omit a rate convention. The supplied package does not select either interpretation.

### Source links

- sourceLinks 0: [jama\_berry\_2025\_oi\_240158\_1742927563.7361.pdf — Secondary Efficacy Outcomes, PDF p. 4](../../../2025/jama.2024.27643/jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4)
- sourceLinks 1: [joi240158supp3\_prod\_1742927563.7911.pdf — eTable 3A, PDF p. 16](../../../2025/jama.2024.27643/joi240158supp3_prod_1742927563.7911.pdf#page=16)

[Original Markdown report](../../../2025/jama.2024.27643/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_C |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity |  |
| broadPlanInvolved | 0 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 1 |
| id | C002 |
| key | 2025::jama.2024.27643::C002 |
| legacyRelationship |  |
| locations | jama\_berry\_2025\_oi\_240158\_1742927563.7361.pdf — Secondary Efficacy Outcomes, PDF p. 4; joi240158supp3\_prod\_1742927563.7911.pdf — eTable 3A, PDF p. 16 |
| originalCrossDocument | 0 |
| package | jama.2024.27643 |
| planMechanism |  |
| primary | S\_C |
| rationale | Target explicitly compares current main article and non-plan results supplement/workbook. A monthly rate is printed in the article; a cumulative 24-week change label is printed for the same values in the cited table. |
| reportHref | ../../2025/jama.2024.27643/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2025/jama.2024.27643/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | Identical SVC values are labelled as monthly rates in the article and as 24-week change estimates in eTable 3A. |
| submissionInvolved | 1 |
| subtype | SVC values have incompatible monthly-rate and 24-week-change labels |
| suggestedDomain | report\_internal\_inconsistency |
| title | SVC values have incompatible monthly-rate and 24-week-change labels |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C003

**Shared-placebo ALSFRS-R credible-interval endpoints differ for the cited primary model**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2024.27643::C003 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> jama\_berry\_2025\_oi\_240158\_1742927563.7361.pdf — Primary Efficacy Outcome, PDF p. 4; joi240158supp3\_prod\_1742927563.7911.pdf — eTable 2, PDF p. 15

### Candidate statement

> The shared-placebo ALSFRS-R interval endpoints differ between the article and its cited eTable 2.

### AI rationale

> Target explicitly compares current main article and non-plan results supplement/workbook. Matched Bayesian shared-parameter-model, group, endpoint, and unit labels accompany different three-decimal interval endpoints.

### Human assessment

Fill Primary during initial review. At handoff, preserve Primary and copy its eight answers into Checker / final. Edit only Checker / final during checking. A blank final answer does not inherit a primary answer.

| Field | Primary | Checker / final |
| --- | --- | --- |
| Disposition |  |  |
| Review domain |  |  |
| Statistcal\_or\_numerical issue |  |  |
| Substantiveness |  |  |
| Downstream impact |  |  |
| Report-internal or planning-material inconsistency |  |  |
| Protocol interpretation |  |  |
| Notes (optional) |  |  |
| Complete | no | no |

| Checker record | Value |
| --- | --- |
| Checker result |  |
| Checker comment |  |
| Discussion resolution |  |
| Resolution note |  |
| Final outcome |  |

For `agree`, all eight effective final answers must equal Primary. Other checker results require a comment. `disagree`, `unable`, or a primary `discuss` require resolved discussion and a note naming participants and the conclusion. Leave Final outcome blank until final readiness.

### Evidence

#### Evidence 0: Source evidence

> The article gives shared-placebo slope -1.03 with 95% CrI -1.176 to -0.892; eTable 2 gives -1.03 with 95% CrI (-1.181, -0.894).

#### Evidence 1: Reported-versus-comparator

> Matched Bayesian shared-parameter-model, group, endpoint, and unit labels accompany different three-decimal interval endpoints.

#### Evidence 2: Calculation

> Lower endpoints differ by 0.005; upper endpoints differ by 0.002; the point estimate is -1.03 in both locations.

#### Evidence 3: Alternative source-grounded interpretations

> Different posterior runs, data locks, or production versions could exist, but neither source labels one.

### Source links

- sourceLinks 0: [jama\_berry\_2025\_oi\_240158\_1742927563.7361.pdf — Primary Efficacy Outcome, PDF p. 4](../../../2025/jama.2024.27643/jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4)
- sourceLinks 1: [joi240158supp3\_prod\_1742927563.7911.pdf — eTable 2, PDF p. 15](../../../2025/jama.2024.27643/joi240158supp3_prod_1742927563.7911.pdf#page=15)

[Original Markdown report](../../../2025/jama.2024.27643/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_C |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity |  |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C003 |
| key | 2025::jama.2024.27643::C003 |
| legacyRelationship |  |
| locations | jama\_berry\_2025\_oi\_240158\_1742927563.7361.pdf — Primary Efficacy Outcome, PDF p. 4; joi240158supp3\_prod\_1742927563.7911.pdf — eTable 2, PDF p. 15 |
| originalCrossDocument | 1 |
| package | jama.2024.27643 |
| planMechanism |  |
| primary | S\_C |
| rationale | Target explicitly compares current main article and non-plan results supplement/workbook. Matched Bayesian shared-parameter-model, group, endpoint, and unit labels accompany different three-decimal interval endpoints. |
| reportHref | ../../2025/jama.2024.27643/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2025/jama.2024.27643/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | The shared-placebo ALSFRS-R interval endpoints differ between the article and its cited eTable 2. |
| submissionInvolved | 1 |
| subtype | Shared-placebo ALSFRS-R credible-interval endpoints differ for the cited primary model |
| suggestedDomain | report\_internal\_inconsistency |
| title | Shared-placebo ALSFRS-R credible-interval endpoints differ for the cited primary model |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C004

**Pooled-active ALSFRS-R credible-interval endpoints differ for the cited primary model**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2024.27643::C004 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> jama\_berry\_2025\_oi\_240158\_1742927563.7361.pdf — Primary Efficacy Outcome, PDF p. 4; joi240158supp3\_prod\_1742927563.7911.pdf — eTable 2, PDF p. 15

### Candidate statement

> The pooled-active ALSFRS-R interval endpoints differ between the article and cited eTable 2.

### AI rationale

> Target explicitly compares current main article and non-plan results supplement/workbook. The point estimate and named model match, while both printed interval endpoints differ.

### Human assessment

Fill Primary during initial review. At handoff, preserve Primary and copy its eight answers into Checker / final. Edit only Checker / final during checking. A blank final answer does not inherit a primary answer.

| Field | Primary | Checker / final |
| --- | --- | --- |
| Disposition |  |  |
| Review domain |  |  |
| Statistcal\_or\_numerical issue |  |  |
| Substantiveness |  |  |
| Downstream impact |  |  |
| Report-internal or planning-material inconsistency |  |  |
| Protocol interpretation |  |  |
| Notes (optional) |  |  |
| Complete | no | no |

| Checker record | Value |
| --- | --- |
| Checker result |  |
| Checker comment |  |
| Discussion resolution |  |
| Resolution note |  |
| Final outcome |  |

For `agree`, all eight effective final answers must equal Primary. Other checker results require a comment. `disagree`, `unable`, or a primary `discuss` require resolved discussion and a note naming participants and the conclusion. Leave Final outcome blank until final readiness.

### Evidence

#### Evidence 0: Source evidence

> The article gives pooled-active slope -1.00 with 95% CrI -1.153 to -0.858; eTable 2 gives -1.00 with 95% CrI (-1.143, -0.847).

#### Evidence 1: Reported-versus-comparator

> The point estimate and named model match, while both printed interval endpoints differ.

#### Evidence 2: Calculation

> Lower endpoints differ by 0.010; upper endpoints differ by 0.011.

#### Evidence 3: Alternative source-grounded interpretations

> Separate posterior outputs or production versions may exist but are not identified on either supplied page.

### Source links

- sourceLinks 0: [jama\_berry\_2025\_oi\_240158\_1742927563.7361.pdf — Primary Efficacy Outcome, PDF p. 4](../../../2025/jama.2024.27643/jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4)
- sourceLinks 1: [joi240158supp3\_prod\_1742927563.7911.pdf — eTable 2, PDF p. 15](../../../2025/jama.2024.27643/joi240158supp3_prod_1742927563.7911.pdf#page=15)

[Original Markdown report](../../../2025/jama.2024.27643/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_C |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity |  |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C004 |
| key | 2025::jama.2024.27643::C004 |
| legacyRelationship |  |
| locations | jama\_berry\_2025\_oi\_240158\_1742927563.7361.pdf — Primary Efficacy Outcome, PDF p. 4; joi240158supp3\_prod\_1742927563.7911.pdf — eTable 2, PDF p. 15 |
| originalCrossDocument | 1 |
| package | jama.2024.27643 |
| planMechanism |  |
| primary | S\_C |
| rationale | Target explicitly compares current main article and non-plan results supplement/workbook. The point estimate and named model match, while both printed interval endpoints differ. |
| reportHref | ../../2025/jama.2024.27643/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2025/jama.2024.27643/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C004 |
| sourceStatus | Pending Human Adjudication |
| statement | The pooled-active ALSFRS-R interval endpoints differ between the article and cited eTable 2. |
| submissionInvolved | 1 |
| subtype | Pooled-active ALSFRS-R credible-interval endpoints differ for the cited primary model |
| suggestedDomain | report\_internal\_inconsistency |
| title | Pooled-active ALSFRS-R credible-interval endpoints differ for the cited primary model |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C005

**Bayesian mortality event rates differ between article text and cited eTable 2**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2024.27643::C005 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> jama\_berry\_2025\_oi\_240158\_1742927563.7361.pdf — Primary Efficacy Outcome, PDF p. 4; joi240158supp3\_prod\_1742927563.7911.pdf — eTable 2, PDF p. 15

### Candidate statement

> Article and eTable 2 event rates differ for the matched Bayesian shared-parameter-model components.

### AI rationale

> Target explicitly compares current main article and non-plan results supplement/workbook. Each matched group has a different three-decimal displayed mortality event rate.

### Human assessment

Fill Primary during initial review. At handoff, preserve Primary and copy its eight answers into Checker / final. Edit only Checker / final during checking. A blank final answer does not inherit a primary answer.

| Field | Primary | Checker / final |
| --- | --- | --- |
| Disposition |  |  |
| Review domain |  |  |
| Statistcal\_or\_numerical issue |  |  |
| Substantiveness |  |  |
| Downstream impact |  |  |
| Report-internal or planning-material inconsistency |  |  |
| Protocol interpretation |  |  |
| Notes (optional) |  |  |
| Complete | no | no |

| Checker record | Value |
| --- | --- |
| Checker result |  |
| Checker comment |  |
| Discussion resolution |  |
| Resolution note |  |
| Final outcome |  |

For `agree`, all eight effective final answers must equal Primary. Other checker results require a comment. `disagree`, `unable`, or a primary `discuss` require resolved discussion and a note naming participants and the conclusion. Leave Final outcome blank until final readiness.

### Evidence

#### Evidence 0: Source evidence

> The article gives shared placebo 0.007 and pooled active 0.006 events/month. eTable 2 gives 0.010 and 0.009 events/month for the same named model.

#### Evidence 1: Reported-versus-comparator

> Each matched group has a different three-decimal displayed mortality event rate.

#### Evidence 2: Calculation

> 0.010 - 0.007 = 0.003 events/month for shared placebo; 0.009 - 0.006 = 0.003 events/month for pooled active. Values differing by 0.003 cannot be the same value rounded to three decimals.

#### Evidence 3: Alternative source-grounded interpretations

> One display may use an unlabelled event definition, posterior summary, or model run.

### Source links

- sourceLinks 0: [jama\_berry\_2025\_oi\_240158\_1742927563.7361.pdf — Primary Efficacy Outcome, PDF p. 4](../../../2025/jama.2024.27643/jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4)
- sourceLinks 1: [joi240158supp3\_prod\_1742927563.7911.pdf — eTable 2, PDF p. 15](../../../2025/jama.2024.27643/joi240158supp3_prod_1742927563.7911.pdf#page=15)

[Original Markdown report](../../../2025/jama.2024.27643/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_C |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity |  |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C005 |
| key | 2025::jama.2024.27643::C005 |
| legacyRelationship |  |
| locations | jama\_berry\_2025\_oi\_240158\_1742927563.7361.pdf — Primary Efficacy Outcome, PDF p. 4; joi240158supp3\_prod\_1742927563.7911.pdf — eTable 2, PDF p. 15 |
| originalCrossDocument | 1 |
| package | jama.2024.27643 |
| planMechanism |  |
| primary | S\_C |
| rationale | Target explicitly compares current main article and non-plan results supplement/workbook. Each matched group has a different three-decimal displayed mortality event rate. |
| reportHref | ../../2025/jama.2024.27643/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2025/jama.2024.27643/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C005 |
| sourceStatus | Pending Human Adjudication |
| statement | Article and eTable 2 event rates differ for the matched Bayesian shared-parameter-model components. |
| submissionInvolved | 1 |
| subtype | Bayesian mortality event rates differ between article text and cited eTable 2 |
| suggestedDomain | report\_internal\_inconsistency |
| title | Bayesian mortality event rates differ between article text and cited eTable 2 |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C006

**Plasma NfL confidence intervals differ across Figure 3, narrative, and eTable 3B**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2024.27643::C006 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> jama\_berry\_2025\_oi\_240158\_1742927563.7361.pdf — Figure 3 and Biomarker Analyses, PDF p. 8; joi240158supp3\_prod\_1742927563.7911.pdf — eTable 3B, PDF p. 17

### Candidate statement

> The repeated plasma-NfL result has differing printed confidence-interval endpoints across three displays.

### AI rationale

> Target explicitly compares current main article and non-plan results supplement/workbook. The matched point estimate and P value are repeated with different printed interval endpoints.

### Human assessment

Fill Primary during initial review. At handoff, preserve Primary and copy its eight answers into Checker / final. Edit only Checker / final during checking. A blank final answer does not inherit a primary answer.

| Field | Primary | Checker / final |
| --- | --- | --- |
| Disposition |  |  |
| Review domain |  |  |
| Statistcal\_or\_numerical issue |  |  |
| Substantiveness |  |  |
| Downstream impact |  |  |
| Report-internal or planning-material inconsistency |  |  |
| Protocol interpretation |  |  |
| Notes (optional) |  |  |
| Complete | no | no |

| Checker record | Value |
| --- | --- |
| Checker result |  |
| Checker comment |  |
| Discussion resolution |  |
| Resolution note |  |
| Final outcome |  |

For `agree`, all eight effective final answers must equal Primary. Other checker results require a comment. `disagree`, `unable`, or a primary `discuss` require resolved discussion and a note naming participants and the conclusion. Leave Final outcome blank until final readiness.

### Evidence

#### Evidence 0: Source evidence

> Figure 3 gives -9.5% with CI -17.8% to -0.5%; nearby narrative gives -17.8% to -0.4%; eTable 3B gives -18.0% to 0. All print -9.5% and P=.04.

#### Evidence 1: Reported-versus-comparator

> The matched point estimate and P value are repeated with different printed interval endpoints.

#### Evidence 2: Calculation

> Figure and narrative upper endpoints differ by 0.1 percentage point. eTable 3B prints a distinct endpoint pair, -18.0% to 0; its unrounded upper endpoint and rounding rule are unavailable.

#### Evidence 3: Alternative source-grounded interpretations

> Independent rounding from unprinted higher precision or an unlabelled model/output version may explain the displays.

### Source links

- sourceLinks 0: [jama\_berry\_2025\_oi\_240158\_1742927563.7361.pdf — Figure 3 and Biomarker Analyses, PDF p. 8](../../../2025/jama.2024.27643/jama_berry_2025_oi_240158_1742927563.7361.pdf#page=8)
- sourceLinks 1: [joi240158supp3\_prod\_1742927563.7911.pdf — eTable 3B, PDF p. 17](../../../2025/jama.2024.27643/joi240158supp3_prod_1742927563.7911.pdf#page=17)

[Original Markdown report](../../../2025/jama.2024.27643/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_C |
| relations | 1 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Both article-internal Figure/narrative and article/results-supp interval differences are explicitly targeted. |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C006 |
| key | 2025::jama.2024.27643::C006 |
| legacyRelationship |  |
| locations | jama\_berry\_2025\_oi\_240158\_1742927563.7361.pdf — Figure 3 and Biomarker Analyses, PDF p. 8; joi240158supp3\_prod\_1742927563.7911.pdf — eTable 3B, PDF p. 17 |
| originalCrossDocument | 1 |
| package | jama.2024.27643 |
| planMechanism |  |
| primary | S\_C |
| rationale | Target explicitly compares current main article and non-plan results supplement/workbook. The matched point estimate and P value are repeated with different printed interval endpoints. |
| reportHref | ../../2025/jama.2024.27643/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2025/jama.2024.27643/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C006 |
| sourceStatus | Pending Human Adjudication |
| statement | The repeated plasma-NfL result has differing printed confidence-interval endpoints across three displays. |
| submissionInvolved | 1 |
| subtype | Plasma NfL confidence intervals differ across Figure 3, narrative, and eTable 3B |
| suggestedDomain | report\_internal\_inconsistency |
| title | Plasma NfL confidence intervals differ across Figure 3, narrative, and eTable 3B |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C007

**Serum NfL regimen-only values and contrast differ across displays**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2024.27643::C007 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> jama\_berry\_2025\_oi\_240158\_1742927563.7361.pdf — Figure 3 and Biomarker Analyses, PDF p. 8; joi240158supp3\_prod\_1742927563.7911.pdf — eTable 3B, PDF p. 17

### Candidate statement

> Matched article and eTable 3B serum-NfL displays report different placebo changes, contrasts, and interval endpoints.

### AI rationale

> Target explicitly compares current main article and non-plan results supplement/workbook. The active change and P value agree, but placebo changes differ by 4.0 percentage points, treatment contrasts differ by 3.2 points, and both interval endpoints differ.

### Human assessment

Fill Primary during initial review. At handoff, preserve Primary and copy its eight answers into Checker / final. Edit only Checker / final during checking. A blank final answer does not inherit a primary answer.

| Field | Primary | Checker / final |
| --- | --- | --- |
| Disposition |  |  |
| Review domain |  |  |
| Statistcal\_or\_numerical issue |  |  |
| Substantiveness |  |  |
| Downstream impact |  |  |
| Report-internal or planning-material inconsistency |  |  |
| Protocol interpretation |  |  |
| Notes (optional) |  |  |
| Complete | no | no |

| Checker record | Value |
| --- | --- |
| Checker result |  |
| Checker comment |  |
| Discussion resolution |  |
| Resolution note |  |
| Final outcome |  |

For `agree`, all eight effective final answers must equal Primary. Other checker results require a comment. `disagree`, `unable`, or a primary `discuss` require resolved discussion and a note naming participants and the conclusion. Leave Final outcome blank until final readiness.

### Evidence

#### Evidence 0: Source evidence

> Article: placebo +30.8%, active +0.4%, difference -23.2% (95% CI -39.5% to -2.5%; P=.03). eTable: placebo +26.8%, active +0.4%, difference -26.4% (95% CI -50.3% to -2.6%; P=.03).

#### Evidence 1: Reported-versus-comparator

> The active change and P value agree, but placebo changes differ by 4.0 percentage points, treatment contrasts differ by 3.2 points, and both interval endpoints differ.

#### Evidence 2: Calculation

> 30.8 - 26.8 = 4.0; \|-23.2 - (-26.4)\| = 3.2. The article's contrast is compatible with the displayed-value diagnostic \[(1.004 / 1.308) - 1\] x 100 = -23.24%, so this is not an internal crude-subtraction claim.

#### Evidence 3: Alternative source-grounded interpretations

> An unlabelled ERO model, population, plate rule, data cut, or fitted-contrast definition could differ between displays.

### Source links

- sourceLinks 0: [jama\_berry\_2025\_oi\_240158\_1742927563.7361.pdf — Figure 3 and Biomarker Analyses, PDF p. 8](../../../2025/jama.2024.27643/jama_berry_2025_oi_240158_1742927563.7361.pdf#page=8)
- sourceLinks 1: [joi240158supp3\_prod\_1742927563.7911.pdf — eTable 3B, PDF p. 17](../../../2025/jama.2024.27643/joi240158supp3_prod_1742927563.7911.pdf#page=17)

[Original Markdown report](../../../2025/jama.2024.27643/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_C |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity |  |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C007 |
| key | 2025::jama.2024.27643::C007 |
| legacyRelationship |  |
| locations | jama\_berry\_2025\_oi\_240158\_1742927563.7361.pdf — Figure 3 and Biomarker Analyses, PDF p. 8; joi240158supp3\_prod\_1742927563.7911.pdf — eTable 3B, PDF p. 17 |
| originalCrossDocument | 1 |
| package | jama.2024.27643 |
| planMechanism |  |
| primary | S\_C |
| rationale | Target explicitly compares current main article and non-plan results supplement/workbook. The active change and P value agree, but placebo changes differ by 4.0 percentage points, treatment contrasts differ by 3.2 points, and both interval endpoints differ. |
| reportHref | ../../2025/jama.2024.27643/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2025/jama.2024.27643/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C007 |
| sourceStatus | Pending Human Adjudication |
| statement | Matched article and eTable 3B serum-NfL displays report different placebo changes, contrasts, and interval endpoints. |
| submissionInvolved | 1 |
| subtype | Serum NfL regimen-only values and contrast differ across displays |
| suggestedDomain | report\_internal\_inconsistency |
| title | Serum NfL regimen-only values and contrast differ across displays |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C008

**Discussion total of 13 events conflicts with the 14 events displayed in Table 2**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2024.27643::C008 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> jama\_berry\_2025\_oi\_240158\_1742927563.7361.pdf — Table 2, PDF p. 7; jama\_berry\_2025\_oi\_240158\_1742927563.7361.pdf — Discussion, PDF p. 9

### Candidate statement

> The Discussion's 13-event total does not match the 14 events obtained from the cited Table 2 group numerators if the endpoint and cutoff are the same.

### AI rationale

> Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. Table 2's two printed numerators total 14, while the Discussion prints 13.

### Human assessment

Fill Primary during initial review. At handoff, preserve Primary and copy its eight answers into Checker / final. Edit only Checker / final during checking. A blank final answer does not inherit a primary answer.

| Field | Primary | Checker / final |
| --- | --- | --- |
| Disposition |  |  |
| Review domain |  |  |
| Statistcal\_or\_numerical issue |  |  |
| Substantiveness |  |  |
| Downstream impact |  |  |
| Report-internal or planning-material inconsistency |  |  |
| Protocol interpretation |  |  |
| Notes (optional) |  |  |
| Complete | no | no |

| Checker record | Value |
| --- | --- |
| Checker result |  |
| Checker comment |  |
| Discussion resolution |  |
| Resolution note |  |
| Final outcome |  |

For `agree`, all eight effective final answers must equal Primary. Other checker results require a comment. `disagree`, `unable`, or a primary `discuss` require resolved discussion and a note naming participants and the conclusion. Leave Final outcome blank until final readiness.

### Evidence

#### Evidence 0: Source evidence

> Table 2 reports 5/120 pooled-active and 9/162 shared-placebo death/PAV events. The Discussion reports 13 RCT-period events in those groups.

#### Evidence 1: Reported-versus-comparator

> Table 2's two printed numerators total 14, while the Discussion prints 13.

#### Evidence 2: Calculation

> 5 + 9 = 14, not 13.

#### Evidence 3: Alternative source-grounded interpretations

> The Discussion may use a narrower event definition, a different cutoff, or an unstated exclusion rather than Table 2's death-or-PAV endpoint.

### Source links

- sourceLinks 0: [jama\_berry\_2025\_oi\_240158\_1742927563.7361.pdf — Table 2, PDF p. 7](../../../2025/jama.2024.27643/jama_berry_2025_oi_240158_1742927563.7361.pdf#page=7)
- sourceLinks 1: [jama\_berry\_2025\_oi\_240158\_1742927563.7361.pdf — Discussion, PDF p. 9](../../../2025/jama.2024.27643/jama_berry_2025_oi_240158_1742927563.7361.pdf#page=9)

[Original Markdown report](../../../2025/jama.2024.27643/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity |  |
| broadPlanInvolved | 0 |
| category | Denominator, proportion, or total inconsistency |
| currentReportCrossDocument | 0 |
| id | C008 |
| key | 2025::jama.2024.27643::C008 |
| legacyRelationship |  |
| locations | jama\_berry\_2025\_oi\_240158\_1742927563.7361.pdf — Table 2, PDF p. 7; jama\_berry\_2025\_oi\_240158\_1742927563.7361.pdf — Discussion, PDF p. 9 |
| originalCrossDocument | 0 |
| package | jama.2024.27643 |
| planMechanism |  |
| primary | S\_W |
| rationale | Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. Table 2's two printed numerators total 14, while the Discussion prints 13. |
| reportHref | ../../2025/jama.2024.27643/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2025/jama.2024.27643/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C008 |
| sourceStatus | Pending Human Adjudication |
| statement | The Discussion's 13-event total does not match the 14 events obtained from the cited Table 2 group numerators if the endpoint and cutoff are the same. |
| submissionInvolved | 1 |
| subtype | Discussion total of 13 events conflicts with the 14 events displayed in Table 2 |
| suggestedDomain | statistical\_results |
| title | Discussion total of 13 events conflicts with the 14 events displayed in Table 2 |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Completion checklist

- [ ] Primary reviewer ID is recorded and every primary assessment is complete.
- [ ] Primary answers were preserved at handoff, with a backup or revision reference recorded.
- [ ] Checker is a different person, with a distinct reviewer ID.
- [ ] Every final assessment uses valid applicable codes and Complete is checker_done.
- [ ] Agreement matches Primary; all other checker results have comments.
- [ ] Required discussions are resolved and participants and conclusions are recorded.
- [ ] No final disposition remains discuss, and every Final outcome follows the codebook.
- [ ] Final counts reconcile to the candidate total and Paper status is final_ready.
