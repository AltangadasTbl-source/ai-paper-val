# jama.2019.14630

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2019 |
| Paper | jama.2019.14630 |
| Candidates | 9 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2019/jama.2019.14630/)

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

- [C001](#candidate-c001) — eTable 2 assigns the N=3,311 column a second intervention-group label (S_W)
- [C002](#candidate-c002) — eTable 2 red-wine median lies above its printed upper quartile (S_W)
- [C003](#candidate-c003) — all-randomized red-wine baseline summaries differ between eTables 2 and 7 (S_W)
- [C004](#candidate-c004) — PDQS baseline mean differs between the principal and baseline-value-carried-forward tables (S_C)
- [C005](#candidate-c005) — intervention baseline energy SD differs between Table 3 and eTable 8 (S_C)
- [C006](#candidate-c006) — baseline body-weight summaries differ between Table 1 and eTable 9 (S_C)
- [C007](#candidate-c007) — baseline BMI means differ between Table 1 and eTable 9 (S_C)
- [C008](#candidate-c008) — Figure 4 threshold labels do not preserve the Methods boundary operators (S_W)
- [C009](#candidate-c009) — eTable 4 total-olive-oil baseline row conflicts with the table’s median/IQR convention (S_W)

## Candidate C001

**eTable 2 assigns the N=3,311 column a second intervention-group label**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.14630::C001 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> Supplement 3 eTable 2 opening header — PDF p. 3; Supplement 3 eTable 2 continuation — PDF p. 5; main article Table 2 — PDF p. 5.

### Candidate statement

> The eTable 2 opening header assigns Intervention group to both N=3,272 and N=3,311, whereas the continuation and main Table 2 identify N=3,311 as control.

### AI rationale

> Opening and continued pages of one results-supplement eTable2 label the same N3311 column intervention and control. Main Table2 only corroborates the continuation arm identity; the target is the internally inconsistent continued table.

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

> The opening page prints Intervention group over N=3,272 and again over N=3,311. The continued table and the main table pair N=3,311 with Control group.

#### Evidence 1: Reported-versus-comparator

> The same displayed N=3,311 column is labelled intervention on the opening page and control on the continuation and main table.

#### Evidence 2: Calculation

> This is a text-identity comparison: N=3,311 has two incompatible arm labels within a fixed two-arm display.

#### Evidence 3: Alternative source-grounded interpretations

> The opening heading may be a localized production error while the numerical column retains the control-group order. No supplied source documents a distinct N=3,311 intervention population.

### Source links

- sourceLinks 0: [Supplement 3 eTable 2 opening header — PDF p. 3](../../../2019/jama.2019.14630/joi190106supp3_prod_1635377898.49725.pdf#page=3)
- sourceLinks 1: [Supplement 3 eTable 2 continuation — PDF p. 5](../../../2019/jama.2019.14630/joi190106supp3_prod_1635377898.49725.pdf#page=5)
- sourceLinks 2: [main article Table 2 — PDF p. 5](../../../2019/jama.2019.14630/jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=5)
- evidencePaths 0: [2019/jama.2019.14630/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.14630/.ai_paper_validation/review_1_5_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.14630/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.14630/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2019/jama.2019.14630/.ai_paper_validation/final_report_1_5_1.md)

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
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C001 |
| key | 2019::jama.2019.14630::C001 |
| legacyRelationship |  |
| locations | Supplement 3 eTable 2 opening header — PDF p. 3; Supplement 3 eTable 2 continuation — PDF p. 5; main article Table 2 — PDF p. 5. |
| originalCrossDocument | 0 |
| package | jama.2019.14630 |
| planMechanism |  |
| primary | S\_W |
| rationale | Opening and continued pages of one results-supplement eTable2 label the same N3311 column intervention and control. Main Table2 only corroborates the continuation arm identity; the target is the internally inconsistent continued table. |
| reportHref | ../../2019/jama.2019.14630/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.14630/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | The eTable 2 opening header assigns Intervention group to both N=3,272 and N=3,311, whereas the continuation and main Table 2 identify N=3,311 as control. |
| submissionInvolved | 1 |
| subtype | arm\_label |
| suggestedDomain | report\_internal\_inconsistency |
| title | eTable 2 assigns the N=3,311 column a second intervention-group label |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C002

**eTable 2 red-wine median lies above its printed upper quartile**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.14630::C002 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> Supplement 3 eTable 2 red-wine row and footnote — PDF p. 7.

### Candidate statement

> The intervention baseline red-wine entry is printed as 33 (0, 29) g/week while the footnote defines baseline values as median (IQR).

### AI rationale

> Results-supplement eTable2 intervention red-wine median33 exceeds its own upper quartile29 under the local median(IQR) footnote.

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

> The printed intervention entry is 33 (0, 29) g/week, and the page states that baseline data are median (IQR).

#### Evidence 1: Reported-versus-comparator

> Median 33 is compared with the printed upper IQR endpoint 29.

#### Evidence 2: Calculation

> 0 ≤ 33 ≤ 29 is false; the median exceeds the printed upper endpoint by 33 − 29 = 4 g/week.

#### Evidence 3: Alternative source-grounded interpretations

> The median, an IQR endpoint, or row/column alignment may be a production error. The supplied PDFs do not identify the intended replacement.

### Source links

- sourceLinks 0: [Supplement 3 eTable 2 red-wine row and footnote — PDF p. 7](../../../2019/jama.2019.14630/joi190106supp3_prod_1635377898.49725.pdf#page=7)
- evidencePaths 0: [2019/jama.2019.14630/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.14630/.ai_paper_validation/review_1_5_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.14630/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.14630/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)
- evidencePaths 2: [2019/jama.2019.14630/.ai\_paper\_validation/review\_1\_5\_1/candidate\_ledger.md](../../../2019/jama.2019.14630/.ai_paper_validation/review_1_5_1/candidate_ledger.md)

[Original Markdown report](../../../2019/jama.2019.14630/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Overlaps the intervention cell in C003, but C003 additionally compares both arms across tables; same underlying production cause is not established. |
| broadPlanInvolved | 0 |
| category | Numeric or arithmetic inconsistency |
| currentReportCrossDocument | 0 |
| id | C002 |
| key | 2019::jama.2019.14630::C002 |
| legacyRelationship |  |
| locations | Supplement 3 eTable 2 red-wine row and footnote — PDF p. 7. |
| originalCrossDocument | 0 |
| package | jama.2019.14630 |
| planMechanism |  |
| primary | S\_W |
| rationale | Results-supplement eTable2 intervention red-wine median33 exceeds its own upper quartile29 under the local median(IQR) footnote. |
| reportHref | ../../2019/jama.2019.14630/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.14630/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | The intervention baseline red-wine entry is printed as 33 (0, 29) g/week while the footnote defines baseline values as median (IQR). |
| submissionInvolved | 1 |
| subtype | summary\_ordering |
| suggestedDomain | statistical\_results |
| title | eTable 2 red-wine median lies above its printed upper quartile |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C003

**all-randomized red-wine baseline summaries differ between eTables 2 and 7**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.14630::C003 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> Supplement 3 eTable 2 — PDF p. 7; Supplement 3 eTable 7 — PDF p. 19.

### Candidate statement

> ETable 2 prints red-wine baseline medians 33 and 4, whereas eTable 7 prints 0 and 0 for the same named arms, units, displayed arm Ns, and median/IQR convention.

### AI rationale

> eTables2 and7 in the same results supplement show all-randomized red-wine baseline medians33/4 versus0/0 with identical displayed arm Ns and IQRs. Different tables in one PDF do not make this cross-document.

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

> ETable 2 gives intervention/control 33 (0, 29) and 4 (0, 29) g/week. ETable 7 gives 0 (0, 29) in both arms. Each table displays N=3,272/N=3,311.

#### Evidence 1: Reported-versus-comparator

> Intervention is 33 versus 0 g/week and control is 4 versus 0 g/week; IQR endpoints match.

#### Evidence 2: Calculation

> The printed median differences are 33 − 0 = 33 and 4 − 0 = 4 g/week. Integer display precision does not reconcile either difference.

#### Evidence 3: Alternative source-grounded interpretations

> ETable 7 may use an unstated analysis-specific baseline subset or handling path despite the identical displayed arm Ns.

### Source links

- sourceLinks 0: [Supplement 3 eTable 2 — PDF p. 7](../../../2019/jama.2019.14630/joi190106supp3_prod_1635377898.49725.pdf#page=7)
- sourceLinks 1: [Supplement 3 eTable 7 — PDF p. 19](../../../2019/jama.2019.14630/joi190106supp3_prod_1635377898.49725.pdf#page=19)
- evidencePaths 0: [2019/jama.2019.14630/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.14630/.ai_paper_validation/review_1_5_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.14630/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.14630/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)
- evidencePaths 2: [2019/jama.2019.14630/.ai\_paper\_validation/review\_1\_5\_1/candidate\_ledger.md](../../../2019/jama.2019.14630/.ai_paper_validation/review_1_5_1/candidate_ledger.md)

[Original Markdown report](../../../2019/jama.2019.14630/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | An unstated analysis-specific baseline subset/handling path is possible. C002 tests ordering within one intervention cell, so these are related rather than exact duplicate candidates. |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 0 |
| id | C003 |
| key | 2019::jama.2019.14630::C003 |
| legacyRelationship |  |
| locations | Supplement 3 eTable 2 — PDF p. 7; Supplement 3 eTable 7 — PDF p. 19. |
| originalCrossDocument | 1 |
| package | jama.2019.14630 |
| planMechanism |  |
| primary | S\_W |
| rationale | eTables2 and7 in the same results supplement show all-randomized red-wine baseline medians33/4 versus0/0 with identical displayed arm Ns and IQRs. Different tables in one PDF do not make this cross-document. |
| reportHref | ../../2019/jama.2019.14630/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.14630/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | ETable 2 prints red-wine baseline medians 33 and 4, whereas eTable 7 prints 0 and 0 for the same named arms, units, displayed arm Ns, and median/IQR convention. |
| submissionInvolved | 1 |
| subtype | repeated\_baseline\_summary |
| suggestedDomain | report\_internal\_inconsistency |
| title | all-randomized red-wine baseline summaries differ between eTables 2 and 7 |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C004

**PDQS baseline mean differs between the principal and baseline-value-carried-forward tables**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.14630::C004 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> main article Table 2 — PDF p. 5; Supplement 3 eTable 6 — PDF p. 16.

### Candidate statement

> Main Table 2 prints baseline PDQS mean 21.1 in both arms, while eTable 6 prints 21.0 in both arms under the same displayed arm Ns and 0-42 scale.

### AI rationale

> Main Table2 baseline PDQS mean21.1 in each arm differs from results-supplement eTable6 mean21.0, under matched Ns and scale.

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

> Main Table 2 gives 21.1 (3.7) in both arms; eTable 6 gives 21.0 (3.7) in both arms with N=3,272/N=3,311.

#### Evidence 1: Reported-versus-comparator

> Each arm mean is 21.1 versus 21.0; the printed SDs and Ns match.

#### Evidence 2: Calculation

> 21.1 − 21.0 = 0.1 point in each arm; SD difference is 0.0.

#### Evidence 3: Alternative source-grounded interpretations

> An unstated analysis-specific baseline set, unreported unrounded values, or different rounding/truncation may account for the difference.

### Source links

- sourceLinks 0: [main article Table 2 — PDF p. 5](../../../2019/jama.2019.14630/jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=5)
- sourceLinks 1: [Supplement 3 eTable 6 — PDF p. 16](../../../2019/jama.2019.14630/joi190106supp3_prod_1635377898.49725.pdf#page=16)
- evidencePaths 0: [2019/jama.2019.14630/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.14630/.ai_paper_validation/review_1_5_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.14630/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.14630/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2019/jama.2019.14630/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_C |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Sensitivity-analysis baseline subset or rounding/truncation could differ despite shared displayed N. |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C004 |
| key | 2019::jama.2019.14630::C004 |
| legacyRelationship |  |
| locations | main article Table 2 — PDF p. 5; Supplement 3 eTable 6 — PDF p. 16. |
| originalCrossDocument | 1 |
| package | jama.2019.14630 |
| planMechanism |  |
| primary | S\_C |
| rationale | Main Table2 baseline PDQS mean21.1 in each arm differs from results-supplement eTable6 mean21.0, under matched Ns and scale. |
| reportHref | ../../2019/jama.2019.14630/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.14630/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C004 |
| sourceStatus | Pending Human Adjudication |
| statement | Main Table 2 prints baseline PDQS mean 21.1 in both arms, while eTable 6 prints 21.0 in both arms under the same displayed arm Ns and 0-42 scale. |
| submissionInvolved | 1 |
| subtype | repeated\_baseline\_summary |
| suggestedDomain | report\_internal\_inconsistency |
| title | PDQS baseline mean differs between the principal and baseline-value-carried-forward tables |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C005

**intervention baseline energy SD differs between Table 3 and eTable 8**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.14630::C005 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> main article Statistical Analysis — PDF p. 4; main article Table 3 — PDF p. 7; Supplement 3 eTable 8 — PDF p. 21.

### Candidate statement

> Intervention baseline energy is 2355 kcal/d in both displays, but its SD is 555 in Table 3 and 544 in eTable 8; the matched control entry agrees.

### AI rationale

> Main Table3 intervention baseline energySD555 differs from results-supplement eTable8 SD544 while means2355 and control summary agree.

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

> Table 3 gives intervention/control 2355 (555)/2369 (555) kcal/d. ETable 8 gives 2,355 (544)/2,369 (555) under the same displayed arm Ns. The main article states that follow-up, not baseline, values were imputed in the main analysis.

#### Evidence 1: Reported-versus-comparator

> Intervention SD is 555 versus 544; intervention mean and both control fields match.

#### Evidence 2: Calculation

> 555 − 544 = 11 kcal/d. Integer rounding of one common SD cannot produce both printed integers.

#### Evidence 3: Alternative source-grounded interpretations

> ETable 8 may use an unstated baseline set or separate extraction; one SD may instead be a production error.

### Source links

- sourceLinks 0: [main article Statistical Analysis — PDF p. 4](../../../2019/jama.2019.14630/jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4)
- sourceLinks 1: [main article Table 3 — PDF p. 7](../../../2019/jama.2019.14630/jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=7)
- sourceLinks 2: [Supplement 3 eTable 8 — PDF p. 21](../../../2019/jama.2019.14630/joi190106supp3_prod_1635377898.49725.pdf#page=21)
- evidencePaths 0: [2019/jama.2019.14630/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.14630/.ai_paper_validation/review_1_5_1/source_inventory.md)

[Original Markdown report](../../../2019/jama.2019.14630/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_C |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | The record states main imputation is follow-up only; an unreported baseline subset or separate extraction remains possible. |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C005 |
| key | 2019::jama.2019.14630::C005 |
| legacyRelationship |  |
| locations | main article Statistical Analysis — PDF p. 4; main article Table 3 — PDF p. 7; Supplement 3 eTable 8 — PDF p. 21. |
| originalCrossDocument | 1 |
| package | jama.2019.14630 |
| planMechanism |  |
| primary | S\_C |
| rationale | Main Table3 intervention baseline energySD555 differs from results-supplement eTable8 SD544 while means2355 and control summary agree. |
| reportHref | ../../2019/jama.2019.14630/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.14630/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C005 |
| sourceStatus | Pending Human Adjudication |
| statement | Intervention baseline energy is 2355 kcal/d in both displays, but its SD is 555 in Table 3 and 544 in eTable 8; the matched control entry agrees. |
| submissionInvolved | 1 |
| subtype | repeated\_baseline\_summary |
| suggestedDomain | report\_internal\_inconsistency |
| title | intervention baseline energy SD differs between Table 3 and eTable 8 |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C006

**baseline body-weight summaries differ between Table 1 and eTable 9**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.14630::C006 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> main article Table 1 — PDF p. 4; Supplement 3 eTable 9 — PDF p. 23.

### Candidate statement

> Table 1 and the all-randomized eTable 9 panel print different baseline weight means in both arms and a different intervention SD despite the same displayed arm Ns.

### AI rationale

> Main Table1 baseline weight86.7/86.4 differs from results-supplement eTable9 weight86.5/86.3 and interventionSD13.0/12.9 under shared displayed Ns.

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

> Table 1 prints 86.7 (13.0)/86.4 (13.0) kg. ETable 9 prints 86.5 (12.9)/86.3 (13.0) kg with N=3,272/N=3,311.

#### Evidence 1: Reported-versus-comparator

> Intervention mean differs by 0.2 kg and SD by 0.1 kg; control mean differs by 0.1 kg and control SD matches.

#### Evidence 2: Calculation

> 86.7 − 86.5 = 0.2, 13.0 − 12.9 = 0.1, 86.4 − 86.3 = 0.1, and 13.0 − 13.0 = 0.0 kg.

#### Evidence 3: Alternative source-grounded interpretations

> ETable 9 may use an outcome-specific baseline set or processing path while displaying the overall arm N.

### Source links

- sourceLinks 0: [main article Table 1 — PDF p. 4](../../../2019/jama.2019.14630/jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4)
- sourceLinks 1: [Supplement 3 eTable 9 — PDF p. 23](../../../2019/jama.2019.14630/joi190106supp3_prod_1635377898.49725.pdf#page=23)
- evidencePaths 0: [2019/jama.2019.14630/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.14630/.ai_paper_validation/review_1_5_1/source_inventory.md)

[Original Markdown report](../../../2019/jama.2019.14630/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_C |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Outcome-specific baseline records or processing may differ without being labelled. |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C006 |
| key | 2019::jama.2019.14630::C006 |
| legacyRelationship |  |
| locations | main article Table 1 — PDF p. 4; Supplement 3 eTable 9 — PDF p. 23. |
| originalCrossDocument | 1 |
| package | jama.2019.14630 |
| planMechanism |  |
| primary | S\_C |
| rationale | Main Table1 baseline weight86.7/86.4 differs from results-supplement eTable9 weight86.5/86.3 and interventionSD13.0/12.9 under shared displayed Ns. |
| reportHref | ../../2019/jama.2019.14630/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.14630/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C006 |
| sourceStatus | Pending Human Adjudication |
| statement | Table 1 and the all-randomized eTable 9 panel print different baseline weight means in both arms and a different intervention SD despite the same displayed arm Ns. |
| submissionInvolved | 1 |
| subtype | repeated\_baseline\_summary |
| suggestedDomain | report\_internal\_inconsistency |
| title | baseline body-weight summaries differ between Table 1 and eTable 9 |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C007

**baseline BMI means differ between Table 1 and eTable 9**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.14630::C007 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> main article Table 1 — PDF p. 4; Supplement 3 eTable 9 — PDF p. 23.

### Candidate statement

> Table 1 prints baseline BMI mean 32.5 in both arms, while the all-randomized eTable 9 panel prints 32.6 in both arms with the same displayed arm Ns and matching SDs.

### AI rationale

> Main Table1 baseline BMI32.5 differs from results-supplement eTable9 BMI32.6 in both arms, with matching SDs and displayed Ns.

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

> Table 1 prints 32.5 (3.4)/32.5 (3.5); eTable 9 prints 32.6 (3.4)/32.6 (3.5) kg/m² under N=3,272/N=3,311.

#### Evidence 1: Reported-versus-comparator

> Each arm mean differs by 0.1 kg/m²; the SDs match.

#### Evidence 2: Calculation

> 32.6 − 32.5 = 0.1 kg/m² in each arm; SD differences are zero.

#### Evidence 3: Alternative source-grounded interpretations

> Different participant records, individual-level derivation paths, or rounding conventions may have been used despite identical displayed group Ns.

### Source links

- sourceLinks 0: [main article Table 1 — PDF p. 4](../../../2019/jama.2019.14630/jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4)
- sourceLinks 1: [Supplement 3 eTable 9 — PDF p. 23](../../../2019/jama.2019.14630/joi190106supp3_prod_1635377898.49725.pdf#page=23)
- evidencePaths 0: [2019/jama.2019.14630/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.14630/.ai_paper_validation/review_1_5_1/source_inventory.md)

[Original Markdown report](../../../2019/jama.2019.14630/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_C |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | BMI derivation, records, or rounding may differ. Related weight candidate C006 concerns another statistic, not an exact duplicate. |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C007 |
| key | 2019::jama.2019.14630::C007 |
| legacyRelationship |  |
| locations | main article Table 1 — PDF p. 4; Supplement 3 eTable 9 — PDF p. 23. |
| originalCrossDocument | 1 |
| package | jama.2019.14630 |
| planMechanism |  |
| primary | S\_C |
| rationale | Main Table1 baseline BMI32.5 differs from results-supplement eTable9 BMI32.6 in both arms, with matching SDs and displayed Ns. |
| reportHref | ../../2019/jama.2019.14630/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.14630/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C007 |
| sourceStatus | Pending Human Adjudication |
| statement | Table 1 prints baseline BMI mean 32.5 in both arms, while the all-randomized eTable 9 panel prints 32.6 in both arms with the same displayed arm Ns and matching SDs. |
| submissionInvolved | 1 |
| subtype | repeated\_baseline\_summary |
| suggestedDomain | report\_internal\_inconsistency |
| title | baseline BMI means differ between Table 1 and eTable 9 |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C008

**Figure 4 threshold labels do not preserve the Methods boundary operators**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.14630::C008 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> main article Outcomes — PDF p. 4; main article Figure 4 — PDF p. 10.

### Candidate statement

> Methods defines clinically meaningful changes with inclusive at least boundaries, while Figure 4 prints strict greater-than signs for ten classifications and omits the diastolic operator.

### AI rationale

> Main Methods inclusive clinically meaningful thresholds differ from main Figure4 strict \> labels and an omitted diastolic operator. All compared descriptions are in the article.

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

> Methods uses at least for 5% weight/BMI/waist/lipid thresholds, 5 mm Hg systolic, 2.5 mm Hg diastolic, and 5% HDL; it specifies a 10% triglyceride reduction. Figure 4 prints \>5%, \>10%, and \>5 mm Hg; the diastolic label is Reduction 2.5 mm Hg without an operator.

#### Evidence 1: Reported-versus-comparator

> Inclusive ≥ x includes equality, strict \> x excludes it, and the diastolic figure label states neither operator.

#### Evidence 2: Calculation

> For the percentage and systolic classifications, ≥ x and \> x differ at exactly x. For diastolic blood pressure, ≥ 2.5 is compared with an operator-free 2.5 label.

#### Evidence 3: Alternative source-grounded interpretations

> Figure \> may be compact typography for the inclusive Methods rule, and the omitted diastolic operator may be typographic. Identical percentages could occur if no observation lay exactly at a boundary.

### Source links

- sourceLinks 0: [main article Outcomes — PDF p. 4](../../../2019/jama.2019.14630/jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4)
- sourceLinks 1: [main article Figure 4 — PDF p. 10](../../../2019/jama.2019.14630/jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=10)
- evidencePaths 0: [2019/jama.2019.14630/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.14630/.ai_paper_validation/review_1_5_1/source_inventory.md)

[Original Markdown report](../../../2019/jama.2019.14630/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Compact figure typography or no exact-boundary observations could leave the implemented classification unchanged. |
| broadPlanInvolved | 0 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C008 |
| key | 2019::jama.2019.14630::C008 |
| legacyRelationship |  |
| locations | main article Outcomes — PDF p. 4; main article Figure 4 — PDF p. 10. |
| originalCrossDocument | 0 |
| package | jama.2019.14630 |
| planMechanism |  |
| primary | S\_W |
| rationale | Main Methods inclusive clinically meaningful thresholds differ from main Figure4 strict \> labels and an omitted diastolic operator. All compared descriptions are in the article. |
| reportHref | ../../2019/jama.2019.14630/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.14630/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C008 |
| sourceStatus | Pending Human Adjudication |
| statement | Methods defines clinically meaningful changes with inclusive at least boundaries, while Figure 4 prints strict greater-than signs for ten classifications and omits the diastolic operator. |
| submissionInvolved | 1 |
| subtype | threshold\_operator |
| suggestedDomain | report\_internal\_inconsistency |
| title | Figure 4 threshold labels do not preserve the Methods boundary operators |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C009

**eTable 4 total-olive-oil baseline row conflicts with the table’s median/IQR convention**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.14630::C009 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> Supplement 3 eTable 4 row — PDF p. 10; Supplement 3 eTable 4 footnote — PDF p. 11; Supplement 3 eTable 2 comparator — PDF p. 3; Supplement 3 eTable 7 comparator — PDF p. 17.

### Candidate statement

> ETable 4 labels total-olive-oil baseline as mean (SD) but prints 350 (175, 350) while its footnote and parallel food tables define that form as median (IQR).

### AI rationale

> Results-supplement eTable4 labels350(175,350) mean(SD), whereas its own footnote and parallel tables in that same supplement define median(IQR).

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

> P. 10 prints Baseline, mean (SD) and 350 (175, 350) in both arms. P. 11 says baseline food data are median (IQR); eTables 2 and 7 label matching total-olive-oil triples median (IQR).

#### Evidence 1: Reported-versus-comparator

> The row label assigns mean/SD, while the table footnote and parallel displays assign median/Q1/Q3 to the same three-value form.

#### Evidence 2: Calculation

> Under median (IQR), the triple maps to median 350, Q1 175, and Q3 350. Under mean (SD), two parenthetical values are supplied where one SD would ordinarily be defined; the statistic types do not reconcile without an explicit exception.

#### Evidence 3: Alternative source-grounded interpretations

> A row-specific convention may exist but is not printed; otherwise the row label may be localized production text inconsistent with the footnote.

### Source links

- sourceLinks 0: [Supplement 3 eTable 4 row — PDF p. 10](../../../2019/jama.2019.14630/joi190106supp3_prod_1635377898.49725.pdf#page=10)
- sourceLinks 1: [Supplement 3 eTable 4 footnote — PDF p. 11](../../../2019/jama.2019.14630/joi190106supp3_prod_1635377898.49725.pdf#page=11)
- sourceLinks 2: [Supplement 3 eTable 2 comparator — PDF p. 3](../../../2019/jama.2019.14630/joi190106supp3_prod_1635377898.49725.pdf#page=3)
- sourceLinks 3: [Supplement 3 eTable 7 comparator — PDF p. 17](../../../2019/jama.2019.14630/joi190106supp3_prod_1635377898.49725.pdf#page=17)
- evidencePaths 0: [2019/jama.2019.14630/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.14630/.ai_paper_validation/review_1_5_1/source_inventory.md)

[Original Markdown report](../../../2019/jama.2019.14630/.ai_paper_validation/final_report_1_5_1.md)

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
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C009 |
| key | 2019::jama.2019.14630::C009 |
| legacyRelationship |  |
| locations | Supplement 3 eTable 4 row — PDF p. 10; Supplement 3 eTable 4 footnote — PDF p. 11; Supplement 3 eTable 2 comparator — PDF p. 3; Supplement 3 eTable 7 comparator — PDF p. 17. |
| originalCrossDocument | 0 |
| package | jama.2019.14630 |
| planMechanism |  |
| primary | S\_W |
| rationale | Results-supplement eTable4 labels350(175,350) mean(SD), whereas its own footnote and parallel tables in that same supplement define median(IQR). |
| reportHref | ../../2019/jama.2019.14630/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.14630/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C009 |
| sourceStatus | Pending Human Adjudication |
| statement | ETable 4 labels total-olive-oil baseline as mean (SD) but prints 350 (175, 350) while its footnote and parallel food tables define that form as median (IQR). |
| submissionInvolved | 1 |
| subtype | summary\_statistic\_label |
| suggestedDomain | report\_internal\_inconsistency |
| title | eTable 4 total-olive-oil baseline row conflicts with the table’s median/IQR convention |
| year | 2019 |
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
