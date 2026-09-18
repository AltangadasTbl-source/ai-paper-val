# jama.2018.18020

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2018 |
| Paper | jama.2018.18020 |
| Candidates | 14 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2018/jama.2018.18020/)

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

- [C001](#candidate-c001) — Abstract sex percentage conflicts with the enrolled sex count (S_W)
- [C002](#candidate-c002) — INQoL IQR endpoints exceed the stated 0-to-100 scale (S_W)
- [C003](#candidate-c003) — Table 2 secondary-outcome contrast header is opposite to the displayed effect signs (S_W)
- [C004](#candidate-c004) — Placebo “Any” adverse-reaction percentage does not reconcile with the apparent denominator (S_W)
- [C005](#candidate-c005) — Bayesian parameter prose swaps mu\_mex\[i\] and mu\_plac\[i\] treatment labels (S_W)
- [C006](#candidate-c006) — diff\_CLCN1 is described as an SCN4A contrast (S_W)
- [C007](#candidate-c007) — sigma.mex is described as placebo-period variability (S_W)
- [C008](#candidate-c008) — Main text prints CLNC1 for the matched CLCN1 genotype subgroup (S_W)
- [C009](#candidate-c009) — SF-36 mental-component P value conflicts with the dependent-t 95% CI (S_W)
- [C010](#candidate-c010) — SCN4A fifth handgrip-action-myotonia P value conflicts with its 95% CI (S_W)
- [C011](#candidate-c011) — SCN4A fifth transient-paresis estimate, interval, and P value do not form a compatible dependent-t result (S_W)
- [C012](#candidate-c012) — Myotonic-discharge P value conflicts with the dependent-t 95% CI (S_W)
- [C013](#candidate-c013) — First handgrip placebo-period interval is reversed and excludes its estimate (S_W)
- [C014](#candidate-c014) — Mean Timed Up&Go placebo-period estimate lies outside its interval (S_W)

## Candidate C001

**Abstract sex percentage conflicts with the enrolled sex count**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.18020::C001 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 1, Abstract Results; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 4, Baseline Data.

### Candidate statement

> The abstract's 22% men is incompatible with its enrolled total and the later count of 22 men and 8 women.

### AI rationale

> The abstract's 22% men is incompatible with its enrolled total and the later count of 22 men and 8 women. The focal mismatch is within the main article.

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

> The abstract prints 30 enrolled patients and 22% men; Baseline Data prints 22 men and 8 women.

#### Evidence 1: Reported-versus-comparator

> Reported 22% men versus comparator 22/30 men.

#### Evidence 2: Calculation

> 22 + 8 = 30; 22/30 × 100 = 73.33%; 22% × 30 = 6.6, not 22 patients.

#### Evidence 3: Alternative source-grounded interpretations

> The abstract may have intended 22 men or approximately 73% men; enrollment-level data and proof history are unavailable.

### Source links

- sourceLinks 0: [jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 1](../../../2018/jama.2018.18020/jama_stunnenberg_2018_oi_180136.pdf#page=1)
- sourceLinks 1: [jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 4](../../../2018/jama.2018.18020/jama_stunnenberg_2018_oi_180136.pdf#page=4)
- evidencePaths 0: [2018/jama.2018.18020/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.18020/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.18020/.ai_paper_validation/final_report_1_5_2.md)

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
| key | 2018::jama.2018.18020::C001 |
| legacyRelationship |  |
| locations | jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 1, Abstract Results; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 4, Baseline Data. |
| originalCrossDocument | 0 |
| package | jama.2018.18020 |
| planMechanism |  |
| primary | S\_W |
| rationale | The abstract's 22% men is incompatible with its enrolled total and the later count of 22 men and 8 women. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.18020/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.18020/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | The abstract's 22% men is incompatible with its enrolled total and the later count of 22 men and 8 women. |
| submissionInvolved | 1 |
| subtype | sex\_count\_vs\_percentage |
| suggestedDomain | statistical\_results |
| title | Abstract sex percentage conflicts with the enrolled sex count |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C002

**INQoL IQR endpoints exceed the stated 0-to-100 scale**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.18020::C002 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 5, Table 1 and footnote f; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 8, Table 2 footnote g.

### Candidate statement

> Table 1 reports INQoL upper IQR endpoints above the table's stated maximum of 100.

### AI rationale

> Table 1 reports INQoL upper IQR endpoints above the table's stated maximum of 100. The focal mismatch is within the main article.

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

> CLCN1 is 84.0 (74.5-110.3) and SCN4A is 98.0 (56.0-120.0) while the footnote states Scale, 0 to 100.

#### Evidence 1: Reported-versus-comparator

> Reported upper endpoints 110.3 and 120.0 versus stated upper scale bound 100.

#### Evidence 2: Calculation

> 110.3 - 100 = 10.3 and 120.0 - 100 = 20.0; a bounded score's quantile cannot exceed its bound.

#### Evidence 3: Alternative source-grounded interpretations

> The footnote may be incomplete or the displayed values may use an undocumented summed/transformed scale.

### Source links

- sourceLinks 0: [jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 5](../../../2018/jama.2018.18020/jama_stunnenberg_2018_oi_180136.pdf#page=5)
- sourceLinks 1: [jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 8](../../../2018/jama.2018.18020/jama_stunnenberg_2018_oi_180136.pdf#page=8)
- evidencePaths 0: [2018/jama.2018.18020/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.18020/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.18020/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C002 |
| key | 2018::jama.2018.18020::C002 |
| legacyRelationship |  |
| locations | jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 5, Table 1 and footnote f; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 8, Table 2 footnote g. |
| originalCrossDocument | 0 |
| package | jama.2018.18020 |
| planMechanism |  |
| primary | S\_W |
| rationale | Table 1 reports INQoL upper IQR endpoints above the table's stated maximum of 100. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.18020/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.18020/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | Table 1 reports INQoL upper IQR endpoints above the table's stated maximum of 100. |
| submissionInvolved | 1 |
| subtype | score\_scale\_bound |
| suggestedDomain | report\_internal\_inconsistency |
| title | INQoL IQR endpoints exceed the stated 0-to-100 scale |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C003

**Table 2 secondary-outcome contrast header is opposite to the displayed effect signs**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.18020::C003 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 7, Table 2 header and change-score rows; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 8, Table 2 footnotes.

### Candidate statement

> The Table 2 header states placebo minus mexiletine, whereas repeated displayed change rows follow mexiletine minus placebo.

### AI rationale

> The Table 2 header states placebo minus mexiletine, whereas repeated displayed change rows follow mexiletine minus placebo. The focal mismatch is within the main article.

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

> The header says Treatment Effect (Placebo-Mexiletine); effects include -14.22 and -2.85 under rows whose period changes are -7.22/-21.44 and 0.46/-2.39.

#### Evidence 1: Reported-versus-comparator

> Printed placebo-minus-mexiletine header versus row arithmetic consistent with mexiletine-minus-placebo.

#### Evidence 2: Calculation

> -21.44 - (-7.22) = -14.22; -2.39 - 0.46 = -2.85; reversing the subtraction reverses both signs.

#### Evidence 3: Alternative source-grounded interpretations

> The header may be reversed, or an undocumented favorable-direction convention may be applied; unrounded paired data are absent.

### Source links

- sourceLinks 0: [jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 7](../../../2018/jama.2018.18020/jama_stunnenberg_2018_oi_180136.pdf#page=7)
- sourceLinks 1: [jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 8](../../../2018/jama.2018.18020/jama_stunnenberg_2018_oi_180136.pdf#page=8)
- evidencePaths 0: [2018/jama.2018.18020/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.18020/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.18020/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C003 |
| key | 2018::jama.2018.18020::C003 |
| legacyRelationship |  |
| locations | jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 7, Table 2 header and change-score rows; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 8, Table 2 footnotes. |
| originalCrossDocument | 0 |
| package | jama.2018.18020 |
| planMechanism |  |
| primary | S\_W |
| rationale | The Table 2 header states placebo minus mexiletine, whereas repeated displayed change rows follow mexiletine minus placebo. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.18020/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.18020/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | The Table 2 header states placebo minus mexiletine, whereas repeated displayed change rows follow mexiletine minus placebo. |
| submissionInvolved | 1 |
| subtype | contrast\_direction |
| suggestedDomain | report\_internal\_inconsistency |
| title | Table 2 secondary-outcome contrast header is opposite to the displayed effect signs |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C004

**Placebo “Any” adverse-reaction percentage does not reconcile with the apparent denominator**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.18020::C004 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> joi180136supp2\_prod.pdf — PDF p. 6, eTable 4; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 8, Adverse Events.

### Candidate statement

> eTable 4's placebo Any 2 (6%) is not compatible with the apparent 30-patient denominator and neighboring nearest-whole-percent displays.

### AI rationale

> Results-supplement eTable 4 prints placebo Any 2 (6%) against neighboring count-2 values of 7% and other pairs implying 30 participants. The main 21/30 statement supports that apparent denominator; the focal discrepancy is an internal eTable denominator/display issue, not a conflicting matched main result.

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

> eTable 4 prints placebo Any 2 (6%), mexiletine Any 27 (90%), and count-2 rows displayed as 7%; main text prints 21 of 30 patients (70%).

#### Evidence 1: Reported-versus-comparator

> Reported 2 (6%) versus the apparent 30-patient denominator and surrounding count/percentage convention.

#### Evidence 2: Calculation

> 2/30 × 100 = 6.67%, ordinarily 7%; a denominator of 31 gives 6.45%, which can round to 6%.

#### Evidence 3: Alternative source-grounded interpretations

> The row may use 31 treatment-set exposures or truncation; eTable 4 does not print a denominator, unit, or rounding rule.

### Source links

- sourceLinks 0: [joi180136supp2\_prod.pdf — PDF p. 6](../../../2018/jama.2018.18020/joi180136supp2_prod.pdf#page=6)
- sourceLinks 1: [jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 8](../../../2018/jama.2018.18020/jama_stunnenberg_2018_oi_180136.pdf#page=8)
- evidencePaths 0: [2018/jama.2018.18020/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.18020/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.18020/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2018.18020/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)

[Original Markdown report](../../../2018/jama.2018.18020/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Conditional denominator: 31 treatment-set exposures, mentioned in the main article, could produce 6%; the table supplies neither analysis unit nor denominator. |
| broadPlanInvolved | 0 |
| category | Denominator, proportion, or total inconsistency |
| currentReportCrossDocument | 0 |
| id | C004 |
| key | 2018::jama.2018.18020::C004 |
| legacyRelationship |  |
| locations | joi180136supp2\_prod.pdf — PDF p. 6, eTable 4; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 8, Adverse Events. |
| originalCrossDocument | 0 |
| package | jama.2018.18020 |
| planMechanism |  |
| primary | S\_W |
| rationale | Results-supplement eTable 4 prints placebo Any 2 (6%) against neighboring count-2 values of 7% and other pairs implying 30 participants. The main 21/30 statement supports that apparent denominator; the focal discrepancy is an internal eTable denominator/display issue, not a conflicting matched main result. |
| reportHref | ../../2018/jama.2018.18020/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.18020/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C004 |
| sourceStatus | Pending Human Adjudication |
| statement | eTable 4's placebo Any 2 (6%) is not compatible with the apparent 30-patient denominator and neighboring nearest-whole-percent displays. |
| submissionInvolved | 1 |
| subtype | adverse\_event\_denominator |
| suggestedDomain | statistical\_results |
| title | Placebo “Any” adverse-reaction percentage does not reconcile with the apparent denominator |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C005

**Bayesian parameter prose swaps mu\_mex\[i\] and mu\_plac\[i\] treatment labels**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.18020::C005 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> joi180136supp2\_prod.pdf — PDF p. 11, eMethods 2 code/dictionary; joi180136supp2\_prod.pdf — PDF p. 13, eMethods 3 code; joi180136supp2\_prod.pdf — PDF p. 14, eMethods 3 dictionary.

### Candidate statement

> The displayed Bayesian-code mappings and adjacent prose assign opposite treatment meanings to mu\_mex\[i\] and mu\_plac\[i\].

### AI rationale

> The displayed Bayesian-code mappings and adjacent prose assign opposite treatment meanings to mu\_mex\[i\] and mu\_plac\[i\]. The focal mismatch is within one non-plan results supplement.

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

> Code maps Stiff\_Plac to mu\_plac and Stiff\_Mex to mu\_mex; dictionaries describe mu\_mex\[i\] as placebo and mu\_plac\[i\] as mexiletine.

#### Evidence 1: Reported-versus-comparator

> Prose treatment labels versus likelihood/data-to-parameter mappings and named population parameters.

#### Evidence 2: Calculation

> Stiff\_Plac -\> mu\_plac and Stiff\_Mex -\> mu\_mex; diff\_patient \<- mu\_plac\[i\] - mu\_mex\[i\] follows that code mapping.

#### Evidence 3: Alternative source-grounded interpretations

> Two prose rows may be transposed while executed code/output remained correct; executed files and logs are not supplied.

### Source links

- sourceLinks 0: [joi180136supp2\_prod.pdf — PDF p. 11](../../../2018/jama.2018.18020/joi180136supp2_prod.pdf#page=11)
- sourceLinks 1: [joi180136supp2\_prod.pdf — PDF p. 13](../../../2018/jama.2018.18020/joi180136supp2_prod.pdf#page=13)
- sourceLinks 2: [joi180136supp2\_prod.pdf — PDF p. 14](../../../2018/jama.2018.18020/joi180136supp2_prod.pdf#page=14)
- evidencePaths 0: [2018/jama.2018.18020/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.18020/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.18020/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2018.18020/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)

[Original Markdown report](../../../2018/jama.2018.18020/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C005 |
| key | 2018::jama.2018.18020::C005 |
| legacyRelationship |  |
| locations | joi180136supp2\_prod.pdf — PDF p. 11, eMethods 2 code/dictionary; joi180136supp2\_prod.pdf — PDF p. 13, eMethods 3 code; joi180136supp2\_prod.pdf — PDF p. 14, eMethods 3 dictionary. |
| originalCrossDocument | 0 |
| package | jama.2018.18020 |
| planMechanism |  |
| primary | S\_W |
| rationale | The displayed Bayesian-code mappings and adjacent prose assign opposite treatment meanings to mu\_mex\[i\] and mu\_plac\[i\]. The focal mismatch is within one non-plan results supplement. |
| reportHref | ../../2018/jama.2018.18020/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.18020/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C005 |
| sourceStatus | Pending Human Adjudication |
| statement | The displayed Bayesian-code mappings and adjacent prose assign opposite treatment meanings to mu\_mex\[i\] and mu\_plac\[i\]. |
| submissionInvolved | 1 |
| subtype | parameter\_treatment\_label |
| suggestedDomain | report\_internal\_inconsistency |
| title | Bayesian parameter prose swaps mu\_mex\[i\] and mu\_plac\[i\] treatment labels |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C006

**diff\_CLCN1 is described as an SCN4A contrast**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.18020::C006 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> joi180136supp2\_prod.pdf — PDF p. 13, eMethods 3 code; joi180136supp2\_prod.pdf — PDF p. 14, parameter dictionary.

### Candidate statement

> The dictionary describes diff\_CLCN1 as SCN4A although its displayed code components are CLCN1.

### AI rationale

> The dictionary describes diff\_CLCN1 as SCN4A although its displayed code components are CLCN1. The focal mismatch is within one non-plan results supplement.

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

> Code defines diff\_CLCN1 \<- mu.plac\_CLCN1 - mu.mex\_CLCN1; the dictionary says mu.plac-mu.mex for SCN4A patients.

#### Evidence 1: Reported-versus-comparator

> SCN4A prose description versus the CLCN1 parameter suffix and both CLCN1 code components.

#### Evidence 2: Calculation

> Substituting the displayed components produces the CLCN1 placebo-minus-mexiletine contrast, not an SCN4A contrast.

#### Evidence 3: Alternative source-grounded interpretations

> The row may be a copy-forward of the preceding SCN4A description; executed output is unavailable.

### Source links

- sourceLinks 0: [joi180136supp2\_prod.pdf — PDF p. 13](../../../2018/jama.2018.18020/joi180136supp2_prod.pdf#page=13)
- sourceLinks 1: [joi180136supp2\_prod.pdf — PDF p. 14](../../../2018/jama.2018.18020/joi180136supp2_prod.pdf#page=14)
- evidencePaths 0: [2018/jama.2018.18020/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.18020/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.18020/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2018.18020/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)

[Original Markdown report](../../../2018/jama.2018.18020/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C006 |
| key | 2018::jama.2018.18020::C006 |
| legacyRelationship |  |
| locations | joi180136supp2\_prod.pdf — PDF p. 13, eMethods 3 code; joi180136supp2\_prod.pdf — PDF p. 14, parameter dictionary. |
| originalCrossDocument | 0 |
| package | jama.2018.18020 |
| planMechanism |  |
| primary | S\_W |
| rationale | The dictionary describes diff\_CLCN1 as SCN4A although its displayed code components are CLCN1. The focal mismatch is within one non-plan results supplement. |
| reportHref | ../../2018/jama.2018.18020/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.18020/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C006 |
| sourceStatus | Pending Human Adjudication |
| statement | The dictionary describes diff\_CLCN1 as SCN4A although its displayed code components are CLCN1. |
| submissionInvolved | 1 |
| subtype | parameter\_genotype\_label |
| suggestedDomain | report\_internal\_inconsistency |
| title | diff\_CLCN1 is described as an SCN4A contrast |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C007

**sigma.mex is described as placebo-period variability**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.18020::C007 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> joi180136supp2\_prod.pdf — PDF p. 11, eMethods 2 code; joi180136supp2\_prod.pdf — PDF p. 12, eMethods 2 dictionary; joi180136supp2\_prod.pdf — PDF p. 13, eMethods 3 code; joi180136supp2\_prod.pdf — PDF p. 14, eMethods 3 dictionary.

### Candidate statement

> Both parameter dictionaries describe sigma.mex as placebo variability despite the displayed mexiletine model branch.

### AI rationale

> Both parameter dictionaries describe sigma.mex as placebo variability despite the displayed mexiletine model branch. The focal mismatch is within one non-plan results supplement.

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

> tau.mex \<- 1/(sigma.mex\*sigma.mex) is used with mu\_mex and Stiff\_Mex, while prose calls sigma.mex placebo-period variability.

#### Evidence 1: Reported-versus-comparator

> Placebo wording versus .mex likelihood branch, mean parameter, and parallel .plac parameter.

#### Evidence 2: Calculation

> tau.mex = 1/sigma.mex^2 supplies precision for mu\_mex, which is used for Stiff\_Mex.

#### Evidence 3: Alternative source-grounded interpretations

> The wording may be repeated copy-forward text while code remains correct; executed models/logs are not supplied.

### Source links

- sourceLinks 0: [joi180136supp2\_prod.pdf — PDF p. 11](../../../2018/jama.2018.18020/joi180136supp2_prod.pdf#page=11)
- sourceLinks 1: [joi180136supp2\_prod.pdf — PDF p. 12](../../../2018/jama.2018.18020/joi180136supp2_prod.pdf#page=12)
- sourceLinks 2: [joi180136supp2\_prod.pdf — PDF p. 13](../../../2018/jama.2018.18020/joi180136supp2_prod.pdf#page=13)
- sourceLinks 3: [joi180136supp2\_prod.pdf — PDF p. 14](../../../2018/jama.2018.18020/joi180136supp2_prod.pdf#page=14)
- evidencePaths 0: [2018/jama.2018.18020/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.18020/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.18020/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2018.18020/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)

[Original Markdown report](../../../2018/jama.2018.18020/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C007 |
| key | 2018::jama.2018.18020::C007 |
| legacyRelationship |  |
| locations | joi180136supp2\_prod.pdf — PDF p. 11, eMethods 2 code; joi180136supp2\_prod.pdf — PDF p. 12, eMethods 2 dictionary; joi180136supp2\_prod.pdf — PDF p. 13, eMethods 3 code; joi180136supp2\_prod.pdf — PDF p. 14, eMethods 3 dictionary. |
| originalCrossDocument | 0 |
| package | jama.2018.18020 |
| planMechanism |  |
| primary | S\_W |
| rationale | Both parameter dictionaries describe sigma.mex as placebo variability despite the displayed mexiletine model branch. The focal mismatch is within one non-plan results supplement. |
| reportHref | ../../2018/jama.2018.18020/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.18020/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C007 |
| sourceStatus | Pending Human Adjudication |
| statement | Both parameter dictionaries describe sigma.mex as placebo variability despite the displayed mexiletine model branch. |
| submissionInvolved | 1 |
| subtype | variance\_treatment\_label |
| suggestedDomain | report\_internal\_inconsistency |
| title | sigma.mex is described as placebo-period variability |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C008

**Main text prints CLNC1 for the matched CLCN1 genotype subgroup**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.18020::C008 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 4, Primary Outcome; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 5, Table 1/Figure 2; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 6, Figure 3; joi180136supp2\_prod.pdf — PDF p. 4, eTable 2 footnote.

### Candidate statement

> A main-text subgroup result is labeled CLNC1 while matched displays and the supplement identify CLCN1.

### AI rationale

> The main narrative attaches CLNC1 to the n=16 subgroup, while the same page gene definition and main figures use CLCN1. The results-supplement footnote corroborates the gene name, so the focal typo is within the main article.

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

> Page 4 assigns 3.84 (95% CrI 2.52-5.16; n=16) to CLNC1; matched displays and gene definition use CLCN1.

#### Evidence 1: Reported-versus-comparator

> CLNC1 in narrative versus CLCN1 in matched subgroup displays with identical estimate, interval, and n.

#### Evidence 2: Calculation

> The numeric keys 3.84, 2.52-5.16, and n=16 identify one subgroup; only the gene-symbol character order differs.

#### Evidence 3: Alternative source-grounded interpretations

> This may be a local typographical transposition; supplied evidence does not establish an effect on analysis.

### Source links

- sourceLinks 0: [jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 4](../../../2018/jama.2018.18020/jama_stunnenberg_2018_oi_180136.pdf#page=4)
- sourceLinks 1: [jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 5](../../../2018/jama.2018.18020/jama_stunnenberg_2018_oi_180136.pdf#page=5)
- sourceLinks 2: [jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 6](../../../2018/jama.2018.18020/jama_stunnenberg_2018_oi_180136.pdf#page=6)
- sourceLinks 3: [joi180136supp2\_prod.pdf — PDF p. 4](../../../2018/jama.2018.18020/joi180136supp2_prod.pdf#page=4)
- evidencePaths 0: [2018/jama.2018.18020/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.18020/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.18020/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2018.18020/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)

[Original Markdown report](../../../2018/jama.2018.18020/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Boundary decision: S\_W only; the supplementary gene definition is corroborating context rather than a separate mismatched reported result. |
| broadPlanInvolved | 0 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C008 |
| key | 2018::jama.2018.18020::C008 |
| legacyRelationship |  |
| locations | jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 4, Primary Outcome; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 5, Table 1/Figure 2; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 6, Figure 3; joi180136supp2\_prod.pdf — PDF p. 4, eTable 2 footnote. |
| originalCrossDocument | 0 |
| package | jama.2018.18020 |
| planMechanism |  |
| primary | S\_W |
| rationale | The main narrative attaches CLNC1 to the n=16 subgroup, while the same page gene definition and main figures use CLCN1. The results-supplement footnote corroborates the gene name, so the focal typo is within the main article. |
| reportHref | ../../2018/jama.2018.18020/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.18020/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C008 |
| sourceStatus | Pending Human Adjudication |
| statement | A main-text subgroup result is labeled CLNC1 while matched displays and the supplement identify CLCN1. |
| submissionInvolved | 1 |
| subtype | genotype\_symbol\_typo |
| suggestedDomain | report\_internal\_inconsistency |
| title | Main text prints CLNC1 for the matched CLCN1 genotype subgroup |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C009

**SF-36 mental-component P value conflicts with the dependent-t 95% CI**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.18020::C009 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 7, Table 2; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 3, dependent-t method; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 4, two-sided P-value convention.

### Candidate statement

> The SF-36 mental-component effect, CI, P value, and printed dependent-t context do not reconcile under the table-level N=27 assumption.

### AI rationale

> The SF-36 mental-component effect, CI, P value, and printed dependent-t context do not reconcile under the table-level N=27 assumption. The focal mismatch is within the main article.

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

> The row reports effect 6.78, 95% CI 1.64 to 11.92, and P=.001; Table 2 states N=27 and dependent t tests for non-IVR secondary outcomes.

#### Evidence 1: Reported-versus-comparator

> Reported .001 versus CI-derived two-sided diagnostic under df=26.

#### Evidence 2: Calculation

> Half-width 5.14 gives SE about 5.14/2.056 = 2.50; t ≈ 6.78/2.50 = 2.71; two-sided P is about .012, not .001.

#### Evidence 3: Alternative source-grounded interpretations

> Row-specific paired n, CI construction, or inferential procedure could differ but are not supplied.

### Source links

- sourceLinks 0: [jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 7](../../../2018/jama.2018.18020/jama_stunnenberg_2018_oi_180136.pdf#page=7)
- sourceLinks 1: [jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 3](../../../2018/jama.2018.18020/jama_stunnenberg_2018_oi_180136.pdf#page=3)
- sourceLinks 2: [jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 4](../../../2018/jama.2018.18020/jama_stunnenberg_2018_oi_180136.pdf#page=4)
- evidencePaths 0: [2018/jama.2018.18020/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.18020/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.18020/.ai_paper_validation/final_report_1_5_2.md)

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
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 0 |
| id | C009 |
| key | 2018::jama.2018.18020::C009 |
| legacyRelationship |  |
| locations | jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 7, Table 2; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 3, dependent-t method; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 4, two-sided P-value convention. |
| originalCrossDocument | 0 |
| package | jama.2018.18020 |
| planMechanism |  |
| primary | S\_W |
| rationale | The SF-36 mental-component effect, CI, P value, and printed dependent-t context do not reconcile under the table-level N=27 assumption. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.18020/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.18020/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C009 |
| sourceStatus | Pending Human Adjudication |
| statement | The SF-36 mental-component effect, CI, P value, and printed dependent-t context do not reconcile under the table-level N=27 assumption. |
| submissionInvolved | 1 |
| subtype | ci\_p\_compatibility |
| suggestedDomain | statistical\_results |
| title | SF-36 mental-component P value conflicts with the dependent-t 95% CI |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C010

**SCN4A fifth handgrip-action-myotonia P value conflicts with its 95% CI**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.18020::C010 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 7, Table 2 row; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 8, Table 2 footnotes; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 3, method; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 4, sidedness.

### Candidate statement

> The SCN4A fifth handgrip effect, zero-crossing CI, and P=.009 do not reconcile under the printed subgroup dependent-t context.

### AI rationale

> The SCN4A fifth handgrip effect, zero-crossing CI, and P=.009 do not reconcile under the printed subgroup dependent-t context. The focal mismatch is within the main article.

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

> The row prints -1.96, 95% CI -3.41 to 0.51, P=.009; subgroup n=11 and dependent t test are stated.

#### Evidence 1: Reported-versus-comparator

> Reported .009 versus a CI that crosses zero and the conditional df=10 diagnostic.

#### Evidence 2: Calculation

> CI half-width 1.96 with df=10 gives SE about 1.96/2.228 = 0.88; \|t\| ≈ 1.96/0.88 = 2.23, two-sided P about .05.

#### Evidence 3: Alternative source-grounded interpretations

> A P value, endpoint, subgroup n, or CI/test definition may differ from the table-level rule.

### Source links

- sourceLinks 0: [jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 7](../../../2018/jama.2018.18020/jama_stunnenberg_2018_oi_180136.pdf#page=7)
- sourceLinks 1: [jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 8](../../../2018/jama.2018.18020/jama_stunnenberg_2018_oi_180136.pdf#page=8)
- sourceLinks 2: [jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 3](../../../2018/jama.2018.18020/jama_stunnenberg_2018_oi_180136.pdf#page=3)
- sourceLinks 3: [jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 4](../../../2018/jama.2018.18020/jama_stunnenberg_2018_oi_180136.pdf#page=4)
- evidencePaths 0: [2018/jama.2018.18020/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.18020/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.18020/.ai_paper_validation/final_report_1_5_2.md)

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
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 0 |
| id | C010 |
| key | 2018::jama.2018.18020::C010 |
| legacyRelationship |  |
| locations | jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 7, Table 2 row; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 8, Table 2 footnotes; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 3, method; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 4, sidedness. |
| originalCrossDocument | 0 |
| package | jama.2018.18020 |
| planMechanism |  |
| primary | S\_W |
| rationale | The SCN4A fifth handgrip effect, zero-crossing CI, and P=.009 do not reconcile under the printed subgroup dependent-t context. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.18020/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.18020/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C010 |
| sourceStatus | Pending Human Adjudication |
| statement | The SCN4A fifth handgrip effect, zero-crossing CI, and P=.009 do not reconcile under the printed subgroup dependent-t context. |
| submissionInvolved | 1 |
| subtype | ci\_p\_compatibility |
| suggestedDomain | statistical\_results |
| title | SCN4A fifth handgrip-action-myotonia P value conflicts with its 95% CI |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C011

**SCN4A fifth transient-paresis estimate, interval, and P value do not form a compatible dependent-t result**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.18020::C011 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 7, Table 2 row; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 6, narrative repetition; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 8, footnotes; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 3, method; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 4, sidedness.

### Candidate statement

> The SCN4A fifth transient-paresis estimate, interval, and P value are mutually incompatible under the printed dependent-t context.

### AI rationale

> The SCN4A fifth transient-paresis estimate, interval, and P value are mutually incompatible under the printed dependent-t context. The focal mismatch is within the main article.

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

> The row prints 13.71, 95% CI -1.96 to 25.47, and P=.02; subgroup n=11 and dependent t test are stated.

#### Evidence 1: Reported-versus-comparator

> Reported estimate/CI/P versus interval midpoint, zero crossing, and conditional df=10 diagnostic.

#### Evidence 2: Calculation

> Midpoint is (-1.96 + 25.47)/2 = 11.755, not 13.71; CI crosses zero; half-width 13.715 gives a two-sided diagnostic near .05, not .02.

#### Evidence 3: Alternative source-grounded interpretations

> A lower-endpoint sign/transcription, P value, n, or procedure may be different; raw output is absent.

### Source links

- sourceLinks 0: [jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 7](../../../2018/jama.2018.18020/jama_stunnenberg_2018_oi_180136.pdf#page=7)
- sourceLinks 1: [jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 6](../../../2018/jama.2018.18020/jama_stunnenberg_2018_oi_180136.pdf#page=6)
- sourceLinks 2: [jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 8](../../../2018/jama.2018.18020/jama_stunnenberg_2018_oi_180136.pdf#page=8)
- sourceLinks 3: [jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 3](../../../2018/jama.2018.18020/jama_stunnenberg_2018_oi_180136.pdf#page=3)
- sourceLinks 4: [jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 4](../../../2018/jama.2018.18020/jama_stunnenberg_2018_oi_180136.pdf#page=4)
- evidencePaths 0: [2018/jama.2018.18020/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.18020/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.18020/.ai_paper_validation/final_report_1_5_2.md)

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
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 0 |
| id | C011 |
| key | 2018::jama.2018.18020::C011 |
| legacyRelationship |  |
| locations | jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 7, Table 2 row; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 6, narrative repetition; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 8, footnotes; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 3, method; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 4, sidedness. |
| originalCrossDocument | 0 |
| package | jama.2018.18020 |
| planMechanism |  |
| primary | S\_W |
| rationale | The SCN4A fifth transient-paresis estimate, interval, and P value are mutually incompatible under the printed dependent-t context. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.18020/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.18020/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C011 |
| sourceStatus | Pending Human Adjudication |
| statement | The SCN4A fifth transient-paresis estimate, interval, and P value are mutually incompatible under the printed dependent-t context. |
| submissionInvolved | 1 |
| subtype | estimate\_ci\_p\_compatibility |
| suggestedDomain | statistical\_results |
| title | SCN4A fifth transient-paresis estimate, interval, and P value do not form a compatible dependent-t result |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C012

**Myotonic-discharge P value conflicts with the dependent-t 95% CI**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.18020::C012 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 8, Table 2 continuation and footnotes; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 3, dependent-t method; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 4, two-sided convention.

### Candidate statement

> The myotonic-discharge effect, CI, and P\<.001 do not reconcile under the printed N=27 dependent-t context.

### AI rationale

> The myotonic-discharge effect, CI, and P\<.001 do not reconcile under the printed N=27 dependent-t context. The focal mismatch is within the main article.

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

> The row reports effect 0.67, 95% CI 0.23 to 1.11, and P\<.001; Table 2 states N=27 and dependent t tests for non-IVR outcomes.

#### Evidence 1: Reported-versus-comparator

> Reported P\<.001 versus a CI-derived two-sided diagnostic under df=26.

#### Evidence 2: Calculation

> Half-width .44 gives SE about .44/2.056 = .214; t ≈ .67/.214 = 3.13; two-sided P about .004, not below .001.

#### Evidence 3: Alternative source-grounded interpretations

> Row-specific n, paired-difference variability, or exact CI/P calculation may differ but are not printed.

### Source links

- sourceLinks 0: [jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 8](../../../2018/jama.2018.18020/jama_stunnenberg_2018_oi_180136.pdf#page=8)
- sourceLinks 1: [jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 3](../../../2018/jama.2018.18020/jama_stunnenberg_2018_oi_180136.pdf#page=3)
- sourceLinks 2: [jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 4](../../../2018/jama.2018.18020/jama_stunnenberg_2018_oi_180136.pdf#page=4)
- evidencePaths 0: [2018/jama.2018.18020/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.18020/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.18020/.ai_paper_validation/final_report_1_5_2.md)

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
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 0 |
| id | C012 |
| key | 2018::jama.2018.18020::C012 |
| legacyRelationship |  |
| locations | jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 8, Table 2 continuation and footnotes; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 3, dependent-t method; jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 4, two-sided convention. |
| originalCrossDocument | 0 |
| package | jama.2018.18020 |
| planMechanism |  |
| primary | S\_W |
| rationale | The myotonic-discharge effect, CI, and P\<.001 do not reconcile under the printed N=27 dependent-t context. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.18020/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.18020/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C012 |
| sourceStatus | Pending Human Adjudication |
| statement | The myotonic-discharge effect, CI, and P\<.001 do not reconcile under the printed N=27 dependent-t context. |
| submissionInvolved | 1 |
| subtype | ci\_p\_compatibility |
| suggestedDomain | statistical\_results |
| title | Myotonic-discharge P value conflicts with the dependent-t 95% CI |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C013

**First handgrip placebo-period interval is reversed and excludes its estimate**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.18020::C013 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 7, Table 2 first-attempt handgrip action-myotonia placebo-period change.

### Candidate statement

> The first-attempt handgrip placebo-period cell prints an interval in reverse order that also excludes its printed point estimate.

### AI rationale

> The first-attempt handgrip placebo-period cell prints an interval in reverse order that also excludes its printed point estimate. The focal mismatch is within the main article.

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

> The cell prints 0.46 (-0.30 to -1.23).

#### Evidence 1: Reported-versus-comparator

> Printed estimate 0.46 versus printed endpoints -0.30 and -1.23.

#### Evidence 2: Calculation

> -0.30 \> -1.23; even when ordered as -1.23 to -0.30, 0.46 is outside. The same row gives -2.39 - 0.46 = -2.85 for the observed treatment-effect direction.

#### Evidence 3: Alternative source-grounded interpretations

> Endpoints may be transposed, or an endpoint sign/value or point estimate may be misprinted.

### Source links

- sourceLinks 0: [jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 7](../../../2018/jama.2018.18020/jama_stunnenberg_2018_oi_180136.pdf#page=7)
- evidencePaths 0: [2018/jama.2018.18020/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.18020/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.18020/.ai_paper_validation/final_report_1_5_2.md)

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
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 0 |
| id | C013 |
| key | 2018::jama.2018.18020::C013 |
| legacyRelationship |  |
| locations | jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 7, Table 2 first-attempt handgrip action-myotonia placebo-period change. |
| originalCrossDocument | 0 |
| package | jama.2018.18020 |
| planMechanism |  |
| primary | S\_W |
| rationale | The first-attempt handgrip placebo-period cell prints an interval in reverse order that also excludes its printed point estimate. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.18020/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.18020/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C013 |
| sourceStatus | Pending Human Adjudication |
| statement | The first-attempt handgrip placebo-period cell prints an interval in reverse order that also excludes its printed point estimate. |
| submissionInvolved | 1 |
| subtype | interval\_order\_and\_containment |
| suggestedDomain | statistical\_results |
| title | First handgrip placebo-period interval is reversed and excludes its estimate |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C014

**Mean Timed Up&Go placebo-period estimate lies outside its interval**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.18020::C014 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 7, Table 2 mean Timed Up&Go placebo-period change.

### Candidate statement

> The mean Timed Up&Go placebo-period estimate exceeds the upper endpoint of its printed interval.

### AI rationale

> The mean Timed Up&Go placebo-period estimate exceeds the upper endpoint of its printed interval. The focal mismatch is within the main article.

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

> The cell prints 0.07 (-0.67 to 0.01).

#### Evidence 1: Reported-versus-comparator

> Printed estimate 0.07 versus ordered interval -0.67 to 0.01.

#### Evidence 2: Calculation

> 0.07 \> 0.01; the estimate exceeds the printed upper endpoint by 0.06. Same-row arithmetic gives -1.05 - 0.07 = -1.12 under the observed table direction.

#### Evidence 3: Alternative source-grounded interpretations

> An endpoint digit, estimate sign/value, or other table field may be transcribed incorrectly.

### Source links

- sourceLinks 0: [jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 7](../../../2018/jama.2018.18020/jama_stunnenberg_2018_oi_180136.pdf#page=7)
- evidencePaths 0: [2018/jama.2018.18020/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.18020/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.18020/.ai_paper_validation/final_report_1_5_2.md)

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
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 0 |
| id | C014 |
| key | 2018::jama.2018.18020::C014 |
| legacyRelationship |  |
| locations | jama\_stunnenberg\_2018\_oi\_180136.pdf — PDF p. 7, Table 2 mean Timed Up&Go placebo-period change. |
| originalCrossDocument | 0 |
| package | jama.2018.18020 |
| planMechanism |  |
| primary | S\_W |
| rationale | The mean Timed Up&Go placebo-period estimate exceeds the upper endpoint of its printed interval. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.18020/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.18020/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C014 |
| sourceStatus | Pending Human Adjudication |
| statement | The mean Timed Up&Go placebo-period estimate exceeds the upper endpoint of its printed interval. |
| submissionInvolved | 1 |
| subtype | estimate\_interval\_containment |
| suggestedDomain | statistical\_results |
| title | Mean Timed Up&Go placebo-period estimate lies outside its interval |
| year | 2018 |
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
