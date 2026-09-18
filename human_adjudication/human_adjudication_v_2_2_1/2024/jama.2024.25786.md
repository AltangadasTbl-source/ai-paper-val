# jama.2024.25786

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2024 |
| Paper | jama.2024.25786 |
| Candidates | 8 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2024/jama.2024.25786/)

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

- [C001](#candidate-c001) — Liberal walk-in transport percentage does not reconcile with 4/743 (S_W)
- [C002](#candidate-c002) — Liberal vascular-surgery percentage is nonzero with a printed zero numerator (S_W)
- [C003](#candidate-c003) — Matched all-patient adjusted confidence-interval upper limit differs between eTables 4 and 7 (S_W)
- [C004](#candidate-c004) — AIS less-than-3 subgroup percentage conflicts with its count and matched Figure 4 (S_C)
- [C005](#candidate-c005) — Known-lung-disease subgroup percentage conflicts with its count and matched Figure 4 (S_C)
- [C006](#candidate-c006) — Postrandomization-exclusion total and group counts do not reconcile across eTable 10 and Figure 1 (S_C)
- [C007](#candidate-c007) — Secondary-exclusion cells pair within-group denominators with cross-group partition percentages (S_W)
- [C008](#candidate-c008) — Missing-as-event primary count uses a doubled numerator/denominator separator (S_W)

## Candidate C001

**Liberal walk-in transport percentage does not reconcile with 4/743**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.25786::C001 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> Supplement 2, eTable 2, PDF p. 15, liberal oxygen group, walk-in transport row.

### Candidate statement

> The liberal-group walk-in transport cell does not reconcile under its printed count/total/percentage format.

### AI rationale

> Results-supplement eTable2 pairs4/743 with5.3%, whereas the printed fraction gives0.5%.

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

> The direct PDF prints 4/743 (5.3) under no./total no. (%). Reported-versus-comparator: Reported 5.3% versus the percentage derived from the paired printed numerator and denominator. Reasoning procedure: Apply 100 × numerator / denominator and round to the table’s one-decimal precision. Calculation: 100 × 4 / 743 = 0.538358...%, which rounds to 0.5%, not 5.3%. Alternative source-grounded interpretations: The count, denominator, or percentage may be mistranscribed; adjacent cells use denominator 743 and no footnote supplies an alternative. Mechanical evidence recheck: Direct layout extraction and rendered-page inspection confirmed 4/743 (5.3) and the count/total/percentage label. Quality-control relevance: The printed fields form an internally reproducible percentage mismatch; the authoritative field is not identifiable from the package. Potential downstream evidence impact: If confirmed, a baseline-characteristics extractor could copy 5.3% or a count-derived percentage without knowing which is authoritative; no propagation or conclusion change is asserted. Human verification steps: Verify the underlying transport record or table output and identify the authoritative numerator, denominator, and percentage. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

#### Evidence 1: Reported-versus-comparator

> Reported 5.3% versus the percentage derived from the paired printed numerator and denominator. Reasoning procedure: Apply 100 × numerator / denominator and round to the table’s one-decimal precision. Calculation: 100 × 4 / 743 = 0.538358...%, which rounds to 0.5%, not 5.3%. Alternative source-grounded interpretations: The count, denominator, or percentage may be mistranscribed; adjacent cells use denominator 743 and no footnote supplies an alternative. Mechanical evidence recheck: Direct layout extraction and rendered-page inspection confirmed 4/743 (5.3) and the count/total/percentage label. Quality-control relevance: The printed fields form an internally reproducible percentage mismatch; the authoritative field is not identifiable from the package. Potential downstream evidence impact: If confirmed, a baseline-characteristics extractor could copy 5.3% or a count-derived percentage without knowing which is authoritative; no propagation or conclusion change is asserted. Human verification steps: Verify the underlying transport record or table output and identify the authoritative numerator, denominator, and percentage. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

#### Evidence 2: Calculation

> 100 × 4 / 743 = 0.538358...%, which rounds to 0.5%, not 5.3%. Alternative source-grounded interpretations: The count, denominator, or percentage may be mistranscribed; adjacent cells use denominator 743 and no footnote supplies an alternative. Mechanical evidence recheck: Direct layout extraction and rendered-page inspection confirmed 4/743 (5.3) and the count/total/percentage label. Quality-control relevance: The printed fields form an internally reproducible percentage mismatch; the authoritative field is not identifiable from the package. Potential downstream evidence impact: If confirmed, a baseline-characteristics extractor could copy 5.3% or a count-derived percentage without knowing which is authoritative; no propagation or conclusion change is asserted. Human verification steps: Verify the underlying transport record or table output and identify the authoritative numerator, denominator, and percentage. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

#### Evidence 3: Alternative source-grounded interpretations

> The count, denominator, or percentage may be mistranscribed; adjacent cells use denominator 743 and no footnote supplies an alternative. Mechanical evidence recheck: Direct layout extraction and rendered-page inspection confirmed 4/743 (5.3) and the count/total/percentage label. Quality-control relevance: The printed fields form an internally reproducible percentage mismatch; the authoritative field is not identifiable from the package. Potential downstream evidence impact: If confirmed, a baseline-characteristics extractor could copy 5.3% or a count-derived percentage without knowing which is authoritative; no propagation or conclusion change is asserted. Human verification steps: Verify the underlying transport record or table output and identify the authoritative numerator, denominator, and percentage. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

### Source links

- sourceLinks 0: [Supplement 2, eTable 2, PDF p. 15](../../../2024/jama.2024.25786/joi240147supp2_prod_1738701765.29201.pdf#page=15)
- evidencePaths 0: [2024/jama.2024.25786/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.25786/.ai_paper_validation/review_1_5_3/source_inventory.md)

[Original Markdown report](../../../2024/jama.2024.25786/.ai_paper_validation/final_report_1_5_3.md)

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
| key | 2024::jama.2024.25786::C001 |
| legacyRelationship |  |
| locations | Supplement 2, eTable 2, PDF p. 15, liberal oxygen group, walk-in transport row. |
| originalCrossDocument | 0 |
| package | jama.2024.25786 |
| planMechanism |  |
| primary | S\_W |
| rationale | Results-supplement eTable2 pairs4/743 with5.3%, whereas the printed fraction gives0.5%. |
| reportHref | ../../2024/jama.2024.25786/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.25786/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | The liberal-group walk-in transport cell does not reconcile under its printed count/total/percentage format. |
| submissionInvolved | 1 |
| subtype | count\_percentage |
| suggestedDomain | statistical\_results |
| title | Liberal walk-in transport percentage does not reconcile with 4/743 |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C002

**Liberal vascular-surgery percentage is nonzero with a printed zero numerator**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.25786::C002 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> Supplement 2, eTable 2, PDF p. 15, liberal oxygen group, vascular surgery row.

### Candidate statement

> The liberal vascular-surgery cell pairs a zero numerator with a nonzero percentage.

### AI rationale

> Results-supplement eTable2 pairs0/747 with1.1%, inconsistent with its own count/total format.

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

> The direct PDF prints 0/747 (1.1) under no./total no. (%). Reported-versus-comparator: Reported 1.1% versus the percentage implied by numerator 0 and denominator 747. Reasoning procedure: Apply the displayed count/total/percentage identity. Calculation: 100 × 0 / 747 = 0.0%, not 1.1%. Alternative source-grounded interpretations: A typographic zero, carried-over percentage, or unprinted qualifier is possible; no footnote provides another rule. Mechanical evidence recheck: Direct layout extraction and rendered-page inspection confirmed the printed cell and format label. Quality-control relevance: The count and percentage cannot both represent the stated quantity under the printed format. Potential downstream evidence impact: If confirmed, an extractor could copy an unresolved rare baseline frequency into a descriptive table; no propagation or conclusion change is asserted. Human verification steps: Check the source surgery records or table-production output and identify the authoritative numerator and percentage. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

#### Evidence 1: Reported-versus-comparator

> Reported 1.1% versus the percentage implied by numerator 0 and denominator 747. Reasoning procedure: Apply the displayed count/total/percentage identity. Calculation: 100 × 0 / 747 = 0.0%, not 1.1%. Alternative source-grounded interpretations: A typographic zero, carried-over percentage, or unprinted qualifier is possible; no footnote provides another rule. Mechanical evidence recheck: Direct layout extraction and rendered-page inspection confirmed the printed cell and format label. Quality-control relevance: The count and percentage cannot both represent the stated quantity under the printed format. Potential downstream evidence impact: If confirmed, an extractor could copy an unresolved rare baseline frequency into a descriptive table; no propagation or conclusion change is asserted. Human verification steps: Check the source surgery records or table-production output and identify the authoritative numerator and percentage. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

#### Evidence 2: Calculation

> 100 × 0 / 747 = 0.0%, not 1.1%. Alternative source-grounded interpretations: A typographic zero, carried-over percentage, or unprinted qualifier is possible; no footnote provides another rule. Mechanical evidence recheck: Direct layout extraction and rendered-page inspection confirmed the printed cell and format label. Quality-control relevance: The count and percentage cannot both represent the stated quantity under the printed format. Potential downstream evidence impact: If confirmed, an extractor could copy an unresolved rare baseline frequency into a descriptive table; no propagation or conclusion change is asserted. Human verification steps: Check the source surgery records or table-production output and identify the authoritative numerator and percentage. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

#### Evidence 3: Alternative source-grounded interpretations

> A typographic zero, carried-over percentage, or unprinted qualifier is possible; no footnote provides another rule. Mechanical evidence recheck: Direct layout extraction and rendered-page inspection confirmed the printed cell and format label. Quality-control relevance: The count and percentage cannot both represent the stated quantity under the printed format. Potential downstream evidence impact: If confirmed, an extractor could copy an unresolved rare baseline frequency into a descriptive table; no propagation or conclusion change is asserted. Human verification steps: Check the source surgery records or table-production output and identify the authoritative numerator and percentage. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

### Source links

- sourceLinks 0: [Supplement 2, eTable 2, PDF p. 15](../../../2024/jama.2024.25786/joi240147supp2_prod_1738701765.29201.pdf#page=15)
- evidencePaths 0: [2024/jama.2024.25786/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.25786/.ai_paper_validation/review_1_5_3/source_inventory.md)

[Original Markdown report](../../../2024/jama.2024.25786/.ai_paper_validation/final_report_1_5_3.md)

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
| id | C002 |
| key | 2024::jama.2024.25786::C002 |
| legacyRelationship |  |
| locations | Supplement 2, eTable 2, PDF p. 15, liberal oxygen group, vascular surgery row. |
| originalCrossDocument | 0 |
| package | jama.2024.25786 |
| planMechanism |  |
| primary | S\_W |
| rationale | Results-supplement eTable2 pairs0/747 with1.1%, inconsistent with its own count/total format. |
| reportHref | ../../2024/jama.2024.25786/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.25786/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | The liberal vascular-surgery cell pairs a zero numerator with a nonzero percentage. |
| submissionInvolved | 1 |
| subtype | count\_percentage |
| suggestedDomain | statistical\_results |
| title | Liberal vascular-surgery percentage is nonzero with a printed zero numerator |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C003

**Matched all-patient adjusted confidence-interval upper limit differs between eTables 4 and 7**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.25786::C003 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> Supplement 2, eTable 4, PDF p. 17, further-adjusted primary outcome; Supplement 2, eTable 7, PDF p. 20, all-patient adjusted odds ratio; relevant methods Main article, PDF p. 5.

### Candidate statement

> Two apparently matched all-patient adjusted results show different displayed upper confidence limits without a table-specific model distinction.

### AI rationale

> Matched eTables4 and7 within the same results supplement print upper95% limits1.41 and1.39 forOR0.98. Main methods only provide model context.

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

> eTable 4 prints 0.98 (0.68 to 1.41) and eTable 7 prints 0.98 (0.68 to 1.39) for the same displayed counts, outcome, contrast, effect label, point estimate, and lower endpoint. Reported-versus-comparator: Upper limit 1.41 versus upper limit 1.39 at the same displayed precision. Reasoning procedure: Compare the matched printed result fields; the relationship is conditional because the two tables do not explicitly bind their adjusted columns to one identical table-specific model. Calculation: 1.41 − 1.39 = 0.02 displayed upper-limit difference. Alternative source-grounded interpretations: The models may differ but be insufficiently labelled; if the models are identical, one endpoint is inconsistent. Unrounded intervals and fitted-model details are not supplied. Mechanical evidence recheck: Direct extraction and page inspection confirmed both intervals, matched event counts, and the absence of a table-specific model formula resolving the comparison. Quality-control relevance: A repeated adjusted result needs either matching displayed endpoints or enough model labelling to prevent a false same-result comparison. Potential downstream evidence impact: If confirmed, an adjusted-effect extractor could copy either upper confidence limit into a precision field; no propagation or conclusion change is asserted. Human verification steps: Determine whether the fitted models and data handling are identical; if so, verify the authoritative unrounded and displayed upper interval. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

#### Evidence 1: Reported-versus-comparator

> Upper limit 1.41 versus upper limit 1.39 at the same displayed precision. Reasoning procedure: Compare the matched printed result fields; the relationship is conditional because the two tables do not explicitly bind their adjusted columns to one identical table-specific model. Calculation: 1.41 − 1.39 = 0.02 displayed upper-limit difference. Alternative source-grounded interpretations: The models may differ but be insufficiently labelled; if the models are identical, one endpoint is inconsistent. Unrounded intervals and fitted-model details are not supplied. Mechanical evidence recheck: Direct extraction and page inspection confirmed both intervals, matched event counts, and the absence of a table-specific model formula resolving the comparison. Quality-control relevance: A repeated adjusted result needs either matching displayed endpoints or enough model labelling to prevent a false same-result comparison. Potential downstream evidence impact: If confirmed, an adjusted-effect extractor could copy either upper confidence limit into a precision field; no propagation or conclusion change is asserted. Human verification steps: Determine whether the fitted models and data handling are identical; if so, verify the authoritative unrounded and displayed upper interval. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

#### Evidence 2: Calculation

> 1.41 − 1.39 = 0.02 displayed upper-limit difference. Alternative source-grounded interpretations: The models may differ but be insufficiently labelled; if the models are identical, one endpoint is inconsistent. Unrounded intervals and fitted-model details are not supplied. Mechanical evidence recheck: Direct extraction and page inspection confirmed both intervals, matched event counts, and the absence of a table-specific model formula resolving the comparison. Quality-control relevance: A repeated adjusted result needs either matching displayed endpoints or enough model labelling to prevent a false same-result comparison. Potential downstream evidence impact: If confirmed, an adjusted-effect extractor could copy either upper confidence limit into a precision field; no propagation or conclusion change is asserted. Human verification steps: Determine whether the fitted models and data handling are identical; if so, verify the authoritative unrounded and displayed upper interval. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

#### Evidence 3: Alternative source-grounded interpretations

> The models may differ but be insufficiently labelled; if the models are identical, one endpoint is inconsistent. Unrounded intervals and fitted-model details are not supplied. Mechanical evidence recheck: Direct extraction and page inspection confirmed both intervals, matched event counts, and the absence of a table-specific model formula resolving the comparison. Quality-control relevance: A repeated adjusted result needs either matching displayed endpoints or enough model labelling to prevent a false same-result comparison. Potential downstream evidence impact: If confirmed, an adjusted-effect extractor could copy either upper confidence limit into a precision field; no propagation or conclusion change is asserted. Human verification steps: Determine whether the fitted models and data handling are identical; if so, verify the authoritative unrounded and displayed upper interval. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

### Source links

- sourceLinks 0: [Supplement 2, eTable 4, PDF p. 17](../../../2024/jama.2024.25786/joi240147supp2_prod_1738701765.29201.pdf#page=17)
- sourceLinks 1: [Supplement 2, eTable 7, PDF p. 20](../../../2024/jama.2024.25786/joi240147supp2_prod_1738701765.29201.pdf#page=20)
- sourceLinks 2: [Main article, PDF p. 5](../../../2024/jama.2024.25786/jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=5)
- evidencePaths 0: [2024/jama.2024.25786/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.25786/.ai_paper_validation/review_1_5_3/source_inventory.md)
- evidencePaths 1: [2024/jama.2024.25786/.ai\_paper\_validation/review\_1\_5\_3/verification/evidence\_recheck.md](../../../2024/jama.2024.25786/.ai_paper_validation/review_1_5_3/verification/evidence_recheck.md)

[Original Markdown report](../../../2024/jama.2024.25786/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Original cross-document category is within one non-plan PDF; precise model identity remains conditional. |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 0 |
| id | C003 |
| key | 2024::jama.2024.25786::C003 |
| legacyRelationship |  |
| locations | Supplement 2, eTable 4, PDF p. 17, further-adjusted primary outcome; Supplement 2, eTable 7, PDF p. 20, all-patient adjusted odds ratio; relevant methods Main article, PDF p. 5. |
| originalCrossDocument | 1 |
| package | jama.2024.25786 |
| planMechanism |  |
| primary | S\_W |
| rationale | Matched eTables4 and7 within the same results supplement print upper95% limits1.41 and1.39 forOR0.98. Main methods only provide model context. |
| reportHref | ../../2024/jama.2024.25786/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.25786/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | Two apparently matched all-patient adjusted results show different displayed upper confidence limits without a table-specific model distinction. |
| submissionInvolved | 1 |
| subtype | interval\_repeat |
| suggestedDomain | report\_internal\_inconsistency |
| title | Matched all-patient adjusted confidence-interval upper limit differs between eTables 4 and 7 |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C004

**AIS less-than-3 subgroup percentage conflicts with its count and matched Figure 4**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.25786::C004 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> Main article, Figure 4, PDF p. 8, AIS score less than 3; Supplement 2, eTable 7, PDF p. 20, AIS less than 3.

### Candidate statement

> The eTable 7 liberal AIS-less-than-3 percentage conflicts with its printed count/denominator and the matched Figure 4 display.

### AI rationale

> Main Figure4 gives48/473(10.1) while results eTable7 gives48/473(9.2), also inconsistent with its own fraction.

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

> Figure 4 prints liberal 48/473 (10.1); eTable 7 prints liberal 48/473 (9.2). Reported-versus-comparator: eTable 7 9.2% versus Figure 4 10.1% and the percentage derived from the shared 48/473. Reasoning procedure: Match subgroup, group, numerator, denominator, and outcome, then apply ordinary one-decimal percentage rounding. Calculation: 100 × 48 / 473 = 10.147991...%, which rounds to 10.1%, not 9.2%. Alternative source-grounded interpretations: eTable 7 may contain a transcription error or use an undisclosed denominator inconsistent with its printed 473. Mechanical evidence recheck: Direct page inspection confirmed both printed strings and the shared numerator/denominator. Quality-control relevance: The same displayed subgroup count and denominator support incompatible percentages across supplied locations. Potential downstream evidence impact: If confirmed, a subgroup extractor could copy 9.2% rather than the count-derived and matched 10.1%; no propagation or conclusion change is asserted. Human verification steps: Verify the subgroup source data, intended denominator, and authoritative displayed percentage. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

#### Evidence 1: Reported-versus-comparator

> eTable 7 9.2% versus Figure 4 10.1% and the percentage derived from the shared 48/473. Reasoning procedure: Match subgroup, group, numerator, denominator, and outcome, then apply ordinary one-decimal percentage rounding. Calculation: 100 × 48 / 473 = 10.147991...%, which rounds to 10.1%, not 9.2%. Alternative source-grounded interpretations: eTable 7 may contain a transcription error or use an undisclosed denominator inconsistent with its printed 473. Mechanical evidence recheck: Direct page inspection confirmed both printed strings and the shared numerator/denominator. Quality-control relevance: The same displayed subgroup count and denominator support incompatible percentages across supplied locations. Potential downstream evidence impact: If confirmed, a subgroup extractor could copy 9.2% rather than the count-derived and matched 10.1%; no propagation or conclusion change is asserted. Human verification steps: Verify the subgroup source data, intended denominator, and authoritative displayed percentage. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

#### Evidence 2: Calculation

> 100 × 48 / 473 = 10.147991...%, which rounds to 10.1%, not 9.2%. Alternative source-grounded interpretations: eTable 7 may contain a transcription error or use an undisclosed denominator inconsistent with its printed 473. Mechanical evidence recheck: Direct page inspection confirmed both printed strings and the shared numerator/denominator. Quality-control relevance: The same displayed subgroup count and denominator support incompatible percentages across supplied locations. Potential downstream evidence impact: If confirmed, a subgroup extractor could copy 9.2% rather than the count-derived and matched 10.1%; no propagation or conclusion change is asserted. Human verification steps: Verify the subgroup source data, intended denominator, and authoritative displayed percentage. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

#### Evidence 3: Alternative source-grounded interpretations

> eTable 7 may contain a transcription error or use an undisclosed denominator inconsistent with its printed 473. Mechanical evidence recheck: Direct page inspection confirmed both printed strings and the shared numerator/denominator. Quality-control relevance: The same displayed subgroup count and denominator support incompatible percentages across supplied locations. Potential downstream evidence impact: If confirmed, a subgroup extractor could copy 9.2% rather than the count-derived and matched 10.1%; no propagation or conclusion change is asserted. Human verification steps: Verify the subgroup source data, intended denominator, and authoritative displayed percentage. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

### Source links

- sourceLinks 0: [Main article, Figure 4, PDF p. 8](../../../2024/jama.2024.25786/jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=8)
- sourceLinks 1: [Supplement 2, eTable 7, PDF p. 20](../../../2024/jama.2024.25786/joi240147supp2_prod_1738701765.29201.pdf#page=20)
- evidencePaths 0: [2024/jama.2024.25786/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.25786/.ai_paper_validation/review_1_5_3/source_inventory.md)
- evidencePaths 1: [2024/jama.2024.25786/.ai\_paper\_validation/review\_1\_5\_3/verification/evidence\_recheck.md](../../../2024/jama.2024.25786/.ai_paper_validation/review_1_5_3/verification/evidence_recheck.md)

[Original Markdown report](../../../2024/jama.2024.25786/.ai_paper_validation/final_report_1_5_3.md)

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
| ambiguity | Mixed cross-file repeated percentage and within-table arithmetic relationship. |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C004 |
| key | 2024::jama.2024.25786::C004 |
| legacyRelationship |  |
| locations | Main article, Figure 4, PDF p. 8, AIS score less than 3; Supplement 2, eTable 7, PDF p. 20, AIS less than 3. |
| originalCrossDocument | 1 |
| package | jama.2024.25786 |
| planMechanism |  |
| primary | S\_C |
| rationale | Main Figure4 gives48/473(10.1) while results eTable7 gives48/473(9.2), also inconsistent with its own fraction. |
| reportHref | ../../2024/jama.2024.25786/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.25786/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C004 |
| sourceStatus | Pending Human Adjudication |
| statement | The eTable 7 liberal AIS-less-than-3 percentage conflicts with its printed count/denominator and the matched Figure 4 display. |
| submissionInvolved | 1 |
| subtype | percentage\_repeat |
| suggestedDomain | report\_internal\_inconsistency |
| title | AIS less-than-3 subgroup percentage conflicts with its count and matched Figure 4 |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C005

**Known-lung-disease subgroup percentage conflicts with its count and matched Figure 4**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.25786::C005 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> Main article, Figure 4, PDF p. 8, known lung disease, yes; Supplement 2, eTable 7, PDF p. 20, known lung disease, yes.

### Candidate statement

> The eTable 7 liberal known-lung-disease percentage differs from the matched Figure 4 percentage despite the same printed count and denominator.

### AI rationale

> Main Figure4 gives14/69(20.3) while results eTable7 gives14/69(20.2); the latter differs from ordinary nearest rounding.

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

> Figure 4 prints liberal 14/69 (20.3); eTable 7 prints liberal 14/69 (20.2). Reported-versus-comparator: eTable 7 20.2% versus Figure 4 20.3% and ordinary nearest rounding of 14/69. Reasoning procedure: Match the subgroup and printed count/denominator, then calculate the one-decimal percentage while retaining an unspecified rounding convention as an alternative. Calculation: 100 × 14 / 69 = 20.289855...%, which is 20.3% under ordinary nearest rounding. Alternative source-grounded interpretations: An unreported truncation or production-time rounding convention, or a transcription difference, may explain the discrepancy; the package does not state a publication-wide rounding rule. Mechanical evidence recheck: Direct page inspection confirmed both values and the shared 14/69. Quality-control relevance: Matched one-decimal subgroup displays are inconsistent unless a different rounding rule is established. Potential downstream evidence impact: If confirmed, a subgroup extractor could copy either one-decimal percentage without a stated convention; no propagation or conclusion change is asserted. Human verification steps: Verify the intended rounding convention and authoritative subgroup percentage. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

#### Evidence 1: Reported-versus-comparator

> eTable 7 20.2% versus Figure 4 20.3% and ordinary nearest rounding of 14/69. Reasoning procedure: Match the subgroup and printed count/denominator, then calculate the one-decimal percentage while retaining an unspecified rounding convention as an alternative. Calculation: 100 × 14 / 69 = 20.289855...%, which is 20.3% under ordinary nearest rounding. Alternative source-grounded interpretations: An unreported truncation or production-time rounding convention, or a transcription difference, may explain the discrepancy; the package does not state a publication-wide rounding rule. Mechanical evidence recheck: Direct page inspection confirmed both values and the shared 14/69. Quality-control relevance: Matched one-decimal subgroup displays are inconsistent unless a different rounding rule is established. Potential downstream evidence impact: If confirmed, a subgroup extractor could copy either one-decimal percentage without a stated convention; no propagation or conclusion change is asserted. Human verification steps: Verify the intended rounding convention and authoritative subgroup percentage. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

#### Evidence 2: Calculation

> 100 × 14 / 69 = 20.289855...%, which is 20.3% under ordinary nearest rounding. Alternative source-grounded interpretations: An unreported truncation or production-time rounding convention, or a transcription difference, may explain the discrepancy; the package does not state a publication-wide rounding rule. Mechanical evidence recheck: Direct page inspection confirmed both values and the shared 14/69. Quality-control relevance: Matched one-decimal subgroup displays are inconsistent unless a different rounding rule is established. Potential downstream evidence impact: If confirmed, a subgroup extractor could copy either one-decimal percentage without a stated convention; no propagation or conclusion change is asserted. Human verification steps: Verify the intended rounding convention and authoritative subgroup percentage. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

#### Evidence 3: Alternative source-grounded interpretations

> An unreported truncation or production-time rounding convention, or a transcription difference, may explain the discrepancy; the package does not state a publication-wide rounding rule. Mechanical evidence recheck: Direct page inspection confirmed both values and the shared 14/69. Quality-control relevance: Matched one-decimal subgroup displays are inconsistent unless a different rounding rule is established. Potential downstream evidence impact: If confirmed, a subgroup extractor could copy either one-decimal percentage without a stated convention; no propagation or conclusion change is asserted. Human verification steps: Verify the intended rounding convention and authoritative subgroup percentage. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

### Source links

- sourceLinks 0: [Main article, Figure 4, PDF p. 8](../../../2024/jama.2024.25786/jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=8)
- sourceLinks 1: [Supplement 2, eTable 7, PDF p. 20](../../../2024/jama.2024.25786/joi240147supp2_prod_1738701765.29201.pdf#page=20)
- evidencePaths 0: [2024/jama.2024.25786/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.25786/.ai_paper_validation/review_1_5_3/source_inventory.md)
- evidencePaths 1: [2024/jama.2024.25786/.ai\_paper\_validation/review\_1\_5\_3/verification/evidence\_recheck.md](../../../2024/jama.2024.25786/.ai_paper_validation/review_1_5_3/verification/evidence_recheck.md)

[Original Markdown report](../../../2024/jama.2024.25786/.ai_paper_validation/final_report_1_5_3.md)

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
| ambiguity | Mixed cross-file and internal arithmetic; unspecified truncation could explain20.2. |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C005 |
| key | 2024::jama.2024.25786::C005 |
| legacyRelationship |  |
| locations | Main article, Figure 4, PDF p. 8, known lung disease, yes; Supplement 2, eTable 7, PDF p. 20, known lung disease, yes. |
| originalCrossDocument | 1 |
| package | jama.2024.25786 |
| planMechanism |  |
| primary | S\_C |
| rationale | Main Figure4 gives14/69(20.3) while results eTable7 gives14/69(20.2); the latter differs from ordinary nearest rounding. |
| reportHref | ../../2024/jama.2024.25786/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.25786/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C005 |
| sourceStatus | Pending Human Adjudication |
| statement | The eTable 7 liberal known-lung-disease percentage differs from the matched Figure 4 percentage despite the same printed count and denominator. |
| submissionInvolved | 1 |
| subtype | rounding\_repeat |
| suggestedDomain | report\_internal\_inconsistency |
| title | Known-lung-disease subgroup percentage conflicts with its count and matched Figure 4 |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C006

**Postrandomization-exclusion total and group counts do not reconcile across eTable 10 and Figure 1**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.25786::C006 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> Supplement 2, eTable 10, PDF p. 24, exclusion after randomization; Main article, Figure 1, PDF p. 3, excluded after randomization.

### Candidate statement

> eTable 10’s postrandomization-exclusion total and group counts do not reconcile with each other or with Figure 1 without an explained population restriction.

### AI rationale

> Results eTable10 gives55+67=122 against its ownN130, while main Figure1 gives59+71=130.

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

> eTable 10 states N=130 and prints restrictive 55/750 (45) and liberal 67/758 (55); Figure 1 prints 59 restrictive and 71 liberal exclusions, totaling 130. Reported-versus-comparator: eTable group total 122 versus its stated 130 and Figure 1’s 130, with each Figure 1 group count four higher. Reasoning procedure: Sum the displayed eTable group counts and compare them with the eTable total and matched Figure 1 branches. Calculation: 55 + 67 = 122; 130 − 122 = 8; 59 + 71 = 130; each figure count exceeds its table count by 4. Alternative source-grounded interpretations: eTable 10 may intentionally omit four Swiss-law consent-withdrawal cases per group, but neither its row label nor footnote defines that restriction. Mechanical evidence recheck: Direct page inspection confirmed the eTable values, Figure 1 values, and the absence of an eTable explanation for the eight-person difference. Quality-control relevance: Participant-flow totals and group counts should state any population restriction needed to reconcile linked displays. Potential downstream evidence impact: If confirmed, an evidence extractor could copy inconsistent flow totals or group exclusions; no effect-estimate impact, propagation, or conclusion change is asserted. Human verification steps: Determine whether the eight omissions are intentional; if so, label the population and reconcile total, denominators, and footnote. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

#### Evidence 1: Reported-versus-comparator

> eTable group total 122 versus its stated 130 and Figure 1’s 130, with each Figure 1 group count four higher. Reasoning procedure: Sum the displayed eTable group counts and compare them with the eTable total and matched Figure 1 branches. Calculation: 55 + 67 = 122; 130 − 122 = 8; 59 + 71 = 130; each figure count exceeds its table count by 4. Alternative source-grounded interpretations: eTable 10 may intentionally omit four Swiss-law consent-withdrawal cases per group, but neither its row label nor footnote defines that restriction. Mechanical evidence recheck: Direct page inspection confirmed the eTable values, Figure 1 values, and the absence of an eTable explanation for the eight-person difference. Quality-control relevance: Participant-flow totals and group counts should state any population restriction needed to reconcile linked displays. Potential downstream evidence impact: If confirmed, an evidence extractor could copy inconsistent flow totals or group exclusions; no effect-estimate impact, propagation, or conclusion change is asserted. Human verification steps: Determine whether the eight omissions are intentional; if so, label the population and reconcile total, denominators, and footnote. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

#### Evidence 2: Calculation

> 55 + 67 = 122; 130 − 122 = 8; 59 + 71 = 130; each figure count exceeds its table count by 4. Alternative source-grounded interpretations: eTable 10 may intentionally omit four Swiss-law consent-withdrawal cases per group, but neither its row label nor footnote defines that restriction. Mechanical evidence recheck: Direct page inspection confirmed the eTable values, Figure 1 values, and the absence of an eTable explanation for the eight-person difference. Quality-control relevance: Participant-flow totals and group counts should state any population restriction needed to reconcile linked displays. Potential downstream evidence impact: If confirmed, an evidence extractor could copy inconsistent flow totals or group exclusions; no effect-estimate impact, propagation, or conclusion change is asserted. Human verification steps: Determine whether the eight omissions are intentional; if so, label the population and reconcile total, denominators, and footnote. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

#### Evidence 3: Alternative source-grounded interpretations

> eTable 10 may intentionally omit four Swiss-law consent-withdrawal cases per group, but neither its row label nor footnote defines that restriction. Mechanical evidence recheck: Direct page inspection confirmed the eTable values, Figure 1 values, and the absence of an eTable explanation for the eight-person difference. Quality-control relevance: Participant-flow totals and group counts should state any population restriction needed to reconcile linked displays. Potential downstream evidence impact: If confirmed, an evidence extractor could copy inconsistent flow totals or group exclusions; no effect-estimate impact, propagation, or conclusion change is asserted. Human verification steps: Determine whether the eight omissions are intentional; if so, label the population and reconcile total, denominators, and footnote. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

### Source links

- sourceLinks 0: [Supplement 2, eTable 10, PDF p. 24](../../../2024/jama.2024.25786/joi240147supp2_prod_1738701765.29201.pdf#page=24)
- sourceLinks 1: [Main article, Figure 1, PDF p. 3](../../../2024/jama.2024.25786/jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=3)
- evidencePaths 0: [2024/jama.2024.25786/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.25786/.ai_paper_validation/review_1_5_3/source_inventory.md)
- evidencePaths 1: [2024/jama.2024.25786/.ai\_paper\_validation/review\_1\_5\_3/verification/evidence\_recheck.md](../../../2024/jama.2024.25786/.ai_paper_validation/review_1_5_3/verification/evidence_recheck.md)

[Original Markdown report](../../../2024/jama.2024.25786/.ai_paper_validation/final_report_1_5_3.md)

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
| ambiguity | Mixed cross-file counts and within-table total; four Swiss-law consent omissions per arm offer a plausible but unlabelled restriction. |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C006 |
| key | 2024::jama.2024.25786::C006 |
| legacyRelationship |  |
| locations | Supplement 2, eTable 10, PDF p. 24, exclusion after randomization; Main article, Figure 1, PDF p. 3, excluded after randomization. |
| originalCrossDocument | 1 |
| package | jama.2024.25786 |
| planMechanism |  |
| primary | S\_C |
| rationale | Results eTable10 gives55+67=122 against its ownN130, while main Figure1 gives59+71=130. |
| reportHref | ../../2024/jama.2024.25786/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.25786/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C006 |
| sourceStatus | Pending Human Adjudication |
| statement | eTable 10’s postrandomization-exclusion total and group counts do not reconcile with each other or with Figure 1 without an explained population restriction. |
| submissionInvolved | 1 |
| subtype | flow\_total |
| suggestedDomain | report\_internal\_inconsistency |
| title | Postrandomization-exclusion total and group counts do not reconcile across eTable 10 and Figure 1 |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C007

**Secondary-exclusion cells pair within-group denominators with cross-group partition percentages**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.25786::C007 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> Supplement 2, eTable 10, PDF p. 24, secondary exclusion; count comparator Main article, Figure 1, PDF p. 3.

### Candidate statement

> eTable 10 pairs within-group denominators with percentages that instead partition the classified cross-group total.

### AI rationale

> Results eTable10 pairs174/750 and165/758 with51%/49%, which instead partition339 cross-arm exclusions. Main Figure1 agrees with the counts.

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

> eTable 10 states N=341 and prints restrictive 174/750 (51) and liberal 165/758 (49); its footnote notes two missing randomized-oxygen assignments. Figure 1 matches counts 174 and 165. Reported-versus-comparator: Printed 51% and 49% versus 23.2% and 21.8% from the printed cell denominators; the printed percentages instead reproduce from the 339 classified exclusions. Reasoning procedure: Calculate percentages using each printed cell denominator and compare them with the cross-group classified-total partition. Calculation: 174/750 = 23.2%; 165/758 = 21.8%; 174 + 165 = 339; 174/339 = 51.3%; 165/339 = 48.7%; 341 − 339 = 2. Alternative source-grounded interpretations: The intended estimand may be within-group exclusion incidence or allocation distribution among classified exclusions; the table does not choose one consistently or explain how to present the two unassigned patients. Mechanical evidence recheck: Direct page inspection confirmed the values, footnote, and Figure 1 count comparator. Quality-control relevance: The display combines incompatible denominator concepts in a count/total/percentage cell. Potential downstream evidence impact: If confirmed, an extractor could copy 51%/49% as within-group rates or 23.2%/21.8% as allocation shares; no propagation or conclusion change is asserted. Human verification steps: Establish the intended estimand, use one denominator consistently, and describe the two missing assignments. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

#### Evidence 1: Reported-versus-comparator

> Printed 51% and 49% versus 23.2% and 21.8% from the printed cell denominators; the printed percentages instead reproduce from the 339 classified exclusions. Reasoning procedure: Calculate percentages using each printed cell denominator and compare them with the cross-group classified-total partition. Calculation: 174/750 = 23.2%; 165/758 = 21.8%; 174 + 165 = 339; 174/339 = 51.3%; 165/339 = 48.7%; 341 − 339 = 2. Alternative source-grounded interpretations: The intended estimand may be within-group exclusion incidence or allocation distribution among classified exclusions; the table does not choose one consistently or explain how to present the two unassigned patients. Mechanical evidence recheck: Direct page inspection confirmed the values, footnote, and Figure 1 count comparator. Quality-control relevance: The display combines incompatible denominator concepts in a count/total/percentage cell. Potential downstream evidence impact: If confirmed, an extractor could copy 51%/49% as within-group rates or 23.2%/21.8% as allocation shares; no propagation or conclusion change is asserted. Human verification steps: Establish the intended estimand, use one denominator consistently, and describe the two missing assignments. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

#### Evidence 2: Calculation

> 174/750 = 23.2%; 165/758 = 21.8%; 174 + 165 = 339; 174/339 = 51.3%; 165/339 = 48.7%; 341 − 339 = 2. Alternative source-grounded interpretations: The intended estimand may be within-group exclusion incidence or allocation distribution among classified exclusions; the table does not choose one consistently or explain how to present the two unassigned patients. Mechanical evidence recheck: Direct page inspection confirmed the values, footnote, and Figure 1 count comparator. Quality-control relevance: The display combines incompatible denominator concepts in a count/total/percentage cell. Potential downstream evidence impact: If confirmed, an extractor could copy 51%/49% as within-group rates or 23.2%/21.8% as allocation shares; no propagation or conclusion change is asserted. Human verification steps: Establish the intended estimand, use one denominator consistently, and describe the two missing assignments. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

#### Evidence 3: Alternative source-grounded interpretations

> The intended estimand may be within-group exclusion incidence or allocation distribution among classified exclusions; the table does not choose one consistently or explain how to present the two unassigned patients. Mechanical evidence recheck: Direct page inspection confirmed the values, footnote, and Figure 1 count comparator. Quality-control relevance: The display combines incompatible denominator concepts in a count/total/percentage cell. Potential downstream evidence impact: If confirmed, an extractor could copy 51%/49% as within-group rates or 23.2%/21.8% as allocation shares; no propagation or conclusion change is asserted. Human verification steps: Establish the intended estimand, use one denominator consistently, and describe the two missing assignments. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

### Source links

- sourceLinks 0: [Supplement 2, eTable 10, PDF p. 24](../../../2024/jama.2024.25786/joi240147supp2_prod_1738701765.29201.pdf#page=24)
- sourceLinks 1: [Main article, Figure 1, PDF p. 3](../../../2024/jama.2024.25786/jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=3)
- evidencePaths 0: [2024/jama.2024.25786/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.25786/.ai_paper_validation/review_1_5_3/source_inventory.md)
- evidencePaths 1: [2024/jama.2024.25786/.ai\_paper\_validation/review\_1\_5\_3/verification/evidence\_recheck.md](../../../2024/jama.2024.25786/.ai_paper_validation/review_1_5_3/verification/evidence_recheck.md)

[Original Markdown report](../../../2024/jama.2024.25786/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Main is corroborative; the two unassigned cases are already explained by a footnote, so that two-person gap is not another discrepancy. |
| broadPlanInvolved | 0 |
| category | Denominator, proportion, or total inconsistency |
| currentReportCrossDocument | 0 |
| id | C007 |
| key | 2024::jama.2024.25786::C007 |
| legacyRelationship |  |
| locations | Supplement 2, eTable 10, PDF p. 24, secondary exclusion; count comparator Main article, Figure 1, PDF p. 3. |
| originalCrossDocument | 0 |
| package | jama.2024.25786 |
| planMechanism |  |
| primary | S\_W |
| rationale | Results eTable10 pairs174/750 and165/758 with51%/49%, which instead partition339 cross-arm exclusions. Main Figure1 agrees with the counts. |
| reportHref | ../../2024/jama.2024.25786/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.25786/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C007 |
| sourceStatus | Pending Human Adjudication |
| statement | eTable 10 pairs within-group denominators with percentages that instead partition the classified cross-group total. |
| submissionInvolved | 1 |
| subtype | denominator\_estimand |
| suggestedDomain | statistical\_results |
| title | Secondary-exclusion cells pair within-group denominators with cross-group partition percentages |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C008

**Missing-as-event primary count uses a doubled numerator/denominator separator**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.25786::C008 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> Supplement 2, eTable 11, PDF p. 25, primary outcome with missing counted as event.

### Candidate statement

> The restrictive missing-as-event primary-outcome count has a doubled numerator/denominator separator despite otherwise reconciling numerically.

### AI rationale

> Results eTable11 prints135//750 with a doubled separator despite its own single-slash count convention; numerical18.0% reconciles.

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

> The direct PDF visibly prints restrictive 135//750 (18.0) under no./total no. (%); the paired liberal cell is 155/758 (20.4). Reported-versus-comparator: Doubled // separator versus the table’s single-slash count/denominator notation and paired cell. Reasoning procedure: Confirm the glyph string directly and compare it with the table convention; separately confirm that the numeric percentage reconciles. Calculation: 100 × 135 / 750 = 18.0%; the numeric relation reconciles, while the doubled separator does not match the notation. Alternative source-grounded interpretations: The doubled slash may be a typographic, encoding, or production artifact; the package does not identify its source stage or intended correction. Mechanical evidence recheck: Direct rendering, high-resolution crop, raw-text and bounding-box extraction, and targeted CPU OCR all retained both slash glyphs. Quality-control relevance: A malformed count separator can impair manual or machine extraction even when its arithmetic is coherent. Potential downstream evidence impact: If confirmed, a manual or machine extractor could retain the malformed separator when copying the display verbatim; no propagation or conclusion change is asserted. Human verification steps: Confirm the authoritative publication string and determine whether clarification of the notation is needed. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

#### Evidence 1: Reported-versus-comparator

> Doubled // separator versus the table’s single-slash count/denominator notation and paired cell. Reasoning procedure: Confirm the glyph string directly and compare it with the table convention; separately confirm that the numeric percentage reconciles. Calculation: 100 × 135 / 750 = 18.0%; the numeric relation reconciles, while the doubled separator does not match the notation. Alternative source-grounded interpretations: The doubled slash may be a typographic, encoding, or production artifact; the package does not identify its source stage or intended correction. Mechanical evidence recheck: Direct rendering, high-resolution crop, raw-text and bounding-box extraction, and targeted CPU OCR all retained both slash glyphs. Quality-control relevance: A malformed count separator can impair manual or machine extraction even when its arithmetic is coherent. Potential downstream evidence impact: If confirmed, a manual or machine extractor could retain the malformed separator when copying the display verbatim; no propagation or conclusion change is asserted. Human verification steps: Confirm the authoritative publication string and determine whether clarification of the notation is needed. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

#### Evidence 2: Calculation

> 100 × 135 / 750 = 18.0%; the numeric relation reconciles, while the doubled separator does not match the notation. Alternative source-grounded interpretations: The doubled slash may be a typographic, encoding, or production artifact; the package does not identify its source stage or intended correction. Mechanical evidence recheck: Direct rendering, high-resolution crop, raw-text and bounding-box extraction, and targeted CPU OCR all retained both slash glyphs. Quality-control relevance: A malformed count separator can impair manual or machine extraction even when its arithmetic is coherent. Potential downstream evidence impact: If confirmed, a manual or machine extractor could retain the malformed separator when copying the display verbatim; no propagation or conclusion change is asserted. Human verification steps: Confirm the authoritative publication string and determine whether clarification of the notation is needed. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

#### Evidence 3: Alternative source-grounded interpretations

> The doubled slash may be a typographic, encoding, or production artifact; the package does not identify its source stage or intended correction. Mechanical evidence recheck: Direct rendering, high-resolution crop, raw-text and bounding-box extraction, and targeted CPU OCR all retained both slash glyphs. Quality-control relevance: A malformed count separator can impair manual or machine extraction even when its arithmetic is coherent. Potential downstream evidence impact: If confirmed, a manual or machine extractor could retain the malformed separator when copying the display verbatim; no propagation or conclusion change is asserted. Human verification steps: Confirm the authoritative publication string and determine whether clarification of the notation is needed. Human adjudication fields: - Validity: \_\_ - Importance: \_\_ - Action: \_\_ - Initials: \_\_ - Notes: \_\_

### Source links

- sourceLinks 0: [Supplement 2, eTable 11, PDF p. 25](../../../2024/jama.2024.25786/joi240147supp2_prod_1738701765.29201.pdf#page=25)
- evidencePaths 0: [2024/jama.2024.25786/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.25786/.ai_paper_validation/review_1_5_3/source_inventory.md)

[Original Markdown report](../../../2024/jama.2024.25786/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Notation defect remains observed even though arithmetic reconciles; not a negated candidate. |
| broadPlanInvolved | 0 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C008 |
| key | 2024::jama.2024.25786::C008 |
| legacyRelationship |  |
| locations | Supplement 2, eTable 11, PDF p. 25, primary outcome with missing counted as event. |
| originalCrossDocument | 0 |
| package | jama.2024.25786 |
| planMechanism |  |
| primary | S\_W |
| rationale | Results eTable11 prints135//750 with a doubled separator despite its own single-slash count convention; numerical18.0% reconciles. |
| reportHref | ../../2024/jama.2024.25786/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.25786/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C008 |
| sourceStatus | Pending Human Adjudication |
| statement | The restrictive missing-as-event primary-outcome count has a doubled numerator/denominator separator despite otherwise reconciling numerically. |
| submissionInvolved | 1 |
| subtype | count\_notation |
| suggestedDomain | report\_internal\_inconsistency |
| title | Missing-as-event primary count uses a doubled numerator/denominator separator |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
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
