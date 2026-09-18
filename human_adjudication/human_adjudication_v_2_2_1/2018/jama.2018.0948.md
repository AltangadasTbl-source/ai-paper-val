# jama.2018.0948

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2018 |
| Paper | jama.2018.0948 |
| Candidates | 7 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2018/jama.2018.0948/)

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

- [C001](#candidate-c001) — Inclusive versus exclusive fluid threshold in the SCD definition (P_R)
- [C002](#candidate-c002) — Mortality absolute-risk-reduction percent/unit conflict (P_P)
- [C003](#candidate-c003) — Cardiac-arrest events assigned incompatible resuscitation-scale categories (P_P)
- [C004](#candidate-c004) — Preventability threshold excludes and includes rating 4 (P_P)
- [C005](#candidate-c005) — The same SCDE reference count is labelled annual and two-year (P_P)
- [C006](#candidate-c006) — Stat-call absolute reduction does not reproduce from the printed inputs (P_P)
- [C007](#candidate-c007) — Urgent PICU admission rates do not match the printed counts and denominators at conventional rounding (P_P)

## Candidate C001

**Inclusive versus exclusive fluid threshold in the SCD definition**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.0948::C001 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> main article — PDF p. 4; Supplement 1 Table 5 — PDF p. 24; Supplement 3 eTable 1 — PDF p. 6.

### Candidate statement

> The same SCD fluid component is printed with inclusive and exclusive 60 mL/kg thresholds.

### AI rationale

> The main article uses fluid \>=60 mL/kg, while protocol Table 5 and the non-plan results-supplement eTable use \>60 for the same SCD component. The article is discrepant with both the plan and ordinary results supplement.

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

> The article says 60 mL/kg or greater within 12 hours; Supplement 1 and Supplement 3 say \>60 mL/kg for the matched component.

#### Evidence 1: Reported-versus-comparator

> x \>= 60 versus x \> 60 on the same unit and 12-hour window.

#### Evidence 2: Calculation

> At x = 60, x \>= 60 is true and x \> 60 is false; Table 5 also leaves 60 outside its printed \<60 and \>60 bands.

#### Evidence 3: Alternative source-grounded interpretations

> The article may paraphrase a strict operational rule, or the support sources may retain a strict sign while an inclusive rule was applied; supplied sources do not decide.

### Source links

- sourceLinks 0: [main article — PDF p. 4](../../../2018/jama.2018.0948/jama_parshuram_2018_oi_180015.pdf#page=4)
- sourceLinks 1: [Supplement 1 Table 5 — PDF p. 24](../../../2018/jama.2018.0948/joi180015supp1_prod.pdf#page=24)
- sourceLinks 2: [Supplement 3 eTable 1 — PDF p. 6](../../../2018/jama.2018.0948/joi180015supp3_prod.pdf#page=6)
- evidencePaths 0: [2018/jama.2018.0948/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.0948/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.0948/.ai\_paper\_validation/review\_1\_5\_2/candidate\_ledger.md](../../../2018/jama.2018.0948/.ai_paper_validation/review_1_5_2/candidate_ledger.md)

[Original Markdown report](../../../2018/jama.2018.0948/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |
| relations | 1 | S\_C |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Mixed reported-versus-plan and submitted cross-file definition discrepancy; operative rule and any exact-boundary cases are unknown. |
| broadPlanInvolved | 1 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 1 |
| id | C001 |
| key | 2018::jama.2018.0948::C001 |
| legacyRelationship |  |
| locations | main article — PDF p. 4; Supplement 1 Table 5 — PDF p. 24; Supplement 3 eTable 1 — PDF p. 6. |
| originalCrossDocument | 0 |
| package | jama.2018.0948 |
| planMechanism | endpoint\_definition\_window\_hierarchy |
| primary | P\_R |
| rationale | The main article uses fluid \>=60 mL/kg, while protocol Table 5 and the non-plan results-supplement eTable use \>60 for the same SCD component. The article is discrepant with both the plan and ordinary results supplement. |
| reportHref | ../../2018/jama.2018.0948/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.0948/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | The same SCD fluid component is printed with inclusive and exclusive 60 mL/kg thresholds. |
| submissionInvolved | 1 |
| subtype | outcome\_threshold\_boundary |
| suggestedDomain | protocol\_report |
| title | Inclusive versus exclusive fluid threshold in the SCD definition |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | retain |

## Candidate C002

**Mortality absolute-risk-reduction percent/unit conflict**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.0948::C002 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> Supplement 1 — PDF p. 1, p. 14, p. 29; main article — PDF p. 4.

### Candidate statement

> A matched mortality planning reduction is printed as 0.9% at one location but as 0.9 per 1,000/0.09% elsewhere.

### AI rationale

> The protocol appendix gives 0.9% for an approximately 18% reduction from 5.1 deaths/1000, whereas other passages in the same protocol give 0.9/1000 or 0.09%. The article repeats the coherent planning value and corroborates the internal plan unit-conversion defect; it is not counted as a separate plan-versus-report change.

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

> The matched 18% reduction from 5.1 deaths/1,000 is 0.9 per 1,000 and 0.09% at matched locations, while Supplement 1 p. 29 says 0.9%.

#### Evidence 1: Reported-versus-comparator

> 0.9% versus the corresponding 0.9 per 1,000 = 0.09%.

#### Evidence 2: Calculation

> 5.1 × 0.178 = 0.9078 per 1,000 = 0.09078%, conventionally 0.09%; 0.9% equals 9 per 1,000 and is tenfold larger.

#### Evidence 3: Alternative source-grounded interpretations

> P. 29 may have intended 0.09% or 0.9 per 1,000; the package does not establish editorial intent.

### Source links

- sourceLinks 0: [Supplement 1 — PDF p. 1](../../../2018/jama.2018.0948/joi180015supp1_prod.pdf#page=1)
- sourceLinks 1: [p. 14](../../../2018/jama.2018.0948/joi180015supp1_prod.pdf#page=14)
- sourceLinks 2: [p. 29](../../../2018/jama.2018.0948/joi180015supp1_prod.pdf#page=29)
- sourceLinks 3: [main article — PDF p. 4](../../../2018/jama.2018.0948/jama_parshuram_2018_oi_180015.pdf#page=4)
- evidencePaths 0: [2018/jama.2018.0948/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.0948/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.0948/.ai\_paper\_validation/review\_1\_5\_2/candidate\_ledger.md](../../../2018/jama.2018.0948/.ai_paper_validation/review_1_5_2/candidate_ledger.md)

[Original Markdown report](../../../2018/jama.2018.0948/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_P |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Boundary decision: P\_P only. Counting every transitive numerical disagreement would also involve the article, but the recorded issue is the internal planning percent/unit typo. |
| broadPlanInvolved | 1 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 0 |
| id | C002 |
| key | 2018::jama.2018.0948::C002 |
| legacyRelationship |  |
| locations | Supplement 1 — PDF p. 1, p. 14, p. 29; main article — PDF p. 4. |
| originalCrossDocument | 1 |
| package | jama.2018.0948 |
| planMechanism |  |
| primary | P\_P |
| rationale | The protocol appendix gives 0.9% for an approximately 18% reduction from 5.1 deaths/1000, whereas other passages in the same protocol give 0.9/1000 or 0.09%. The article repeats the coherent planning value and corroborates the internal plan unit-conversion defect; it is not counted as a separate plan-versus-report change. |
| reportHref | ../../2018/jama.2018.0948/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.0948/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | A matched mortality planning reduction is printed as 0.9% at one location but as 0.9 per 1,000/0.09% elsewhere. |
| submissionInvolved | 0 |
| subtype | planning\_unit\_conversion |
| suggestedDomain | plan\_material |
| title | Mortality absolute-risk-reduction percent/unit conflict |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C003

**Cardiac-arrest events assigned incompatible resuscitation-scale categories**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.0948::C003 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> Supplement 1 — PDF p. 11, Table 5 — PDF p. 24, Table 6 legend — PDF p. 27.

### Candidate statement

> Cardiac-arrest events are described as categories 6/7 but a Table 6 legend calls events including cardiac arrest 4/5.

### AI rationale

> Cardiac-arrest events are described as categories 6/7 but a Table 6 legend calls events including cardiac arrest 4/5. The focal discrepancy is internal to the protocol/SAP material, including plan-version passages in a bound bundle.

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

> P. 11 defines cardiac arrest without preceding DNR as 6 or 7; Table 5 maps CPR to 6 and death to 7; Table 6 names events including cardiac arrest as scale 4 or 5.

#### Evidence 1: Reported-versus-comparator

> {4,5} versus {6,7} under the named seven-category Children’s Resuscitation Intensity Scale.

#### Evidence 2: Calculation

> {4,5} ∩ {6,7} = ∅; the labels cannot reconcile under one unchanged scale.

#### Evidence 3: Alternative source-grounded interpretations

> P. 27 could refer to a different, undefined scale; a residual or transcription explanation is inferential.

### Source links

- sourceLinks 0: [Supplement 1 — PDF p. 11](../../../2018/jama.2018.0948/joi180015supp1_prod.pdf#page=11)
- sourceLinks 1: [Table 5 — PDF p. 24](../../../2018/jama.2018.0948/joi180015supp1_prod.pdf#page=24)
- sourceLinks 2: [Table 6 legend — PDF p. 27](../../../2018/jama.2018.0948/joi180015supp1_prod.pdf#page=27)
- evidencePaths 0: [2018/jama.2018.0948/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.0948/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.0948/.ai\_paper\_validation/review\_1\_5\_2/candidate\_ledger.md](../../../2018/jama.2018.0948/.ai_paper_validation/review_1_5_2/candidate_ledger.md)

[Original Markdown report](../../../2018/jama.2018.0948/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_P |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity |  |
| broadPlanInvolved | 1 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C003 |
| key | 2018::jama.2018.0948::C003 |
| legacyRelationship |  |
| locations | Supplement 1 — PDF p. 11, Table 5 — PDF p. 24, Table 6 legend — PDF p. 27. |
| originalCrossDocument | 0 |
| package | jama.2018.0948 |
| planMechanism |  |
| primary | P\_P |
| rationale | Cardiac-arrest events are described as categories 6/7 but a Table 6 legend calls events including cardiac arrest 4/5. The focal discrepancy is internal to the protocol/SAP material, including plan-version passages in a bound bundle. |
| reportHref | ../../2018/jama.2018.0948/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.0948/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | Cardiac-arrest events are described as categories 6/7 but a Table 6 legend calls events including cardiac arrest 4/5. |
| submissionInvolved | 0 |
| subtype | resuscitation\_category\_definition |
| suggestedDomain | plan\_material |
| title | Cardiac-arrest events assigned incompatible resuscitation-scale categories |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C004

**Preventability threshold excludes and includes rating 4**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.0948::C004 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> Supplement 1 — PDF p. 11, Table 7 — PDF p. 28; Supplement 3 eTable 1 — PDF p. 6; main article — PDF p. 7.

### Candidate statement

> The preventability definition says \>4 while nearby and cross-source descriptions include rating 4.

### AI rationale

> Protocol p11 says \>4 and immediately lists ratings 4, 5, 6; its own Table 7 says \>=4. The main article and results supplement corroborate the inclusive list. The focal operator/list contradiction is internal to the protocol.

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

> P. 11 prints \>4 but immediately includes ratings 4, 5, and 6; Table 7 says 4 or more, Supplement 3 says 4–6, and the article describes rating 4 as more than likely preventable.

#### Evidence 1: Reported-versus-comparator

> \>4 versus \>=4 on the stated six-point scale.

#### Evidence 2: Calculation

> 4 \> 4 is false, whereas 4 \>= 4 is true; the printed definitions classify rating 4 differently.

#### Evidence 3: Alternative source-grounded interpretations

> Table 7/final reporting may state the operative rule, or p. 11 may reflect a stricter intended threshold; sources do not decide.

### Source links

- sourceLinks 0: [Supplement 1 — PDF p. 11](../../../2018/jama.2018.0948/joi180015supp1_prod.pdf#page=11)
- sourceLinks 1: [Table 7 — PDF p. 28](../../../2018/jama.2018.0948/joi180015supp1_prod.pdf#page=28)
- sourceLinks 2: [Supplement 3 eTable 1 — PDF p. 6](../../../2018/jama.2018.0948/joi180015supp3_prod.pdf#page=6)
- sourceLinks 3: [main article — PDF p. 7](../../../2018/jama.2018.0948/jama_parshuram_2018_oi_180015.pdf#page=7)
- evidencePaths 0: [2018/jama.2018.0948/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.0948/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.0948/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2018.0948/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)
- evidencePaths 2: [2018/jama.2018.0948/.ai\_paper\_validation/review\_1\_5\_2/candidate\_ledger.md](../../../2018/jama.2018.0948/.ai_paper_validation/review_1_5_2/candidate_ledger.md)

[Original Markdown report](../../../2018/jama.2018.0948/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_P |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Boundary decision: P\_P only; final reporting corroborates the internally stated \>=4 rule. The actual rating-4 event classification is unknown. |
| broadPlanInvolved | 1 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C004 |
| key | 2018::jama.2018.0948::C004 |
| legacyRelationship |  |
| locations | Supplement 1 — PDF p. 11, Table 7 — PDF p. 28; Supplement 3 eTable 1 — PDF p. 6; main article — PDF p. 7. |
| originalCrossDocument | 0 |
| package | jama.2018.0948 |
| planMechanism |  |
| primary | P\_P |
| rationale | Protocol p11 says \>4 and immediately lists ratings 4, 5, 6; its own Table 7 says \>=4. The main article and results supplement corroborate the inclusive list. The focal operator/list contradiction is internal to the protocol. |
| reportHref | ../../2018/jama.2018.0948/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.0948/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C004 |
| sourceStatus | Pending Human Adjudication |
| statement | The preventability definition says \>4 while nearby and cross-source descriptions include rating 4. |
| submissionInvolved | 0 |
| subtype | preventability\_threshold |
| suggestedDomain | plan\_material |
| title | Preventability threshold excludes and includes rating 4 |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C005

**The same SCDE reference count is labelled annual and two-year**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.0948::C005 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> Supplement 1 — PDF p. 14 and PDF p. 30.

### Candidate statement

> The same 1,052 urgent ICU/PICU admission count is labelled annual and as a two-year total.

### AI rationale

> The same historical Ontario four-hospital 1052 urgent ICU/PICU admissions count is called annual in protocol power-assumption text and two-year in the historical reference-data appendix. The conflicting quantity is a prior-data observation period reused as a planning input, and therefore does not represent the current trial plan or report.

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

> P. 14 says 1,052 urgent ICU admissions per year; p. 30 says 1,052 urgent PICU admissions occurred in two years after 31 January 2007.

#### Evidence 1: Reported-versus-comparator

> One identical reference count with annual versus two-year period labels.

#### Evidence 2: Calculation

> If unannualized over two years, 1052 / 2 = 526 per year. Diagnostic reconstruction using printed assumptions is 1052 × .40 / (55,963 × 4) × 1,000 = 1.88, approximately 2 per 1,000; this does not establish an exact patient-day denominator.

#### Evidence 3: Alternative source-grounded interpretations

> P. 14 may annualize another dataset, or p. 30 may describe a broader window; no year-stratified data or exact patient-days are supplied.

### Source links

- sourceLinks 0: [Supplement 1 — PDF p. 14](../../../2018/jama.2018.0948/joi180015supp1_prod.pdf#page=14)
- sourceLinks 1: [PDF p. 30](../../../2018/jama.2018.0948/joi180015supp1_prod.pdf#page=30)
- evidencePaths 0: [2018/jama.2018.0948/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.0948/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.0948/.ai\_paper\_validation/review\_1\_5\_2/candidate\_ledger.md](../../../2018/jama.2018.0948/.ai_paper_validation/review_1_5_2/candidate_ledger.md)
- evidencePaths 2: [2018/jama.2018.0948/.ai\_paper\_validation/review\_1\_5\_2/preprocessing/native\_text/joi180015supp1\_prod.txt](../../../2018/jama.2018.0948/.ai_paper_validation/review_1_5_2/preprocessing/native_text/joi180015supp1_prod.txt)

[Original Markdown report](../../../2018/jama.2018.0948/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_P |
| legacyRelations | 0 | P\_B |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Historical evidence inside protocol. The p14 planning context uses this historical count, but the candidate does not independently challenge a prospective power calculation. Year-stratified data are absent. |
| broadPlanInvolved | 1 |
| category | Denominator, proportion, or total inconsistency |
| currentReportCrossDocument | 0 |
| id | C005 |
| key | 2018::jama.2018.0948::C005 |
| legacyRelationship | P\_B |
| locations | Supplement 1 — PDF p. 14 and PDF p. 30. |
| originalCrossDocument | 0 |
| package | jama.2018.0948 |
| planMechanism |  |
| primary | P\_P |
| rationale | The same historical Ontario four-hospital 1052 urgent ICU/PICU admissions count is called annual in protocol power-assumption text and two-year in the historical reference-data appendix. The conflicting quantity is a prior-data observation period reused as a planning input, and therefore does not represent the current trial plan or report. |
| reportHref | ../../2018/jama.2018.0948/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.0948/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C005 |
| sourceStatus | Pending Human Adjudication |
| statement | The same 1,052 urgent ICU/PICU admission count is labelled annual and as a two-year total. |
| submissionInvolved | 0 |
| subtype | planning\_reference\_period |
| suggestedDomain | plan\_material |
| title | The same SCDE reference count is labelled annual and two-year |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C006

**Stat-call absolute reduction does not reproduce from the printed inputs**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.0948::C006 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> Supplement 1 — PDF p. 30.

### Candidate statement

> The printed stat-call absolute reduction does not reproduce from the displayed baseline rate and relative reduction.

### AI rationale

> The printed stat-call absolute reduction does not reproduce from the displayed baseline rate and relative reduction. The focal discrepancy is internal to the protocol/SAP material, including plan-version passages in a bound bundle.

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

> The paragraph prints 8.13 calls/1,000 patient-days, maximum relative risk reduction 0.181, and a corresponding absolute reduction of 1.45 calls/1,000 patient-days.

#### Evidence 1: Reported-versus-comparator

> Printed 1.45 versus the product of printed inputs.

#### Evidence 2: Calculation

> 8.13 × .181 = 1.47153, conventionally 1.47. Display bounds 8.125 × .1805 = 1.4665625 through values below 8.135 × .1815 = 1.4765025 do not overlap the 1.445 to below 1.455 range displaying as 1.45.

#### Evidence 3: Alternative source-grounded interpretations

> More precise undisplayed inputs, a transcription step, or a nonstandard display method could explain the value; none is supplied.

### Source links

- sourceLinks 0: [Supplement 1 — PDF p. 30](../../../2018/jama.2018.0948/joi180015supp1_prod.pdf#page=30)
- evidencePaths 0: [2018/jama.2018.0948/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.0948/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.0948/.ai\_paper\_validation/review\_1\_5\_2/candidate\_ledger.md](../../../2018/jama.2018.0948/.ai_paper_validation/review_1_5_2/candidate_ledger.md)

[Original Markdown report](../../../2018/jama.2018.0948/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_P |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity |  |
| broadPlanInvolved | 1 |
| category | Numeric or arithmetic inconsistency |
| currentReportCrossDocument | 0 |
| id | C006 |
| key | 2018::jama.2018.0948::C006 |
| legacyRelationship |  |
| locations | Supplement 1 — PDF p. 30. |
| originalCrossDocument | 0 |
| package | jama.2018.0948 |
| planMechanism |  |
| primary | P\_P |
| rationale | The printed stat-call absolute reduction does not reproduce from the displayed baseline rate and relative reduction. The focal discrepancy is internal to the protocol/SAP material, including plan-version passages in a bound bundle. |
| reportHref | ../../2018/jama.2018.0948/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.0948/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C006 |
| sourceStatus | Pending Human Adjudication |
| statement | The printed stat-call absolute reduction does not reproduce from the displayed baseline rate and relative reduction. |
| submissionInvolved | 0 |
| subtype | planning\_product\_arithmetic |
| suggestedDomain | plan\_material |
| title | Stat-call absolute reduction does not reproduce from the printed inputs |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C007

**Urgent PICU admission rates do not match the printed counts and denominators at conventional rounding**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.0948::C007 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> Supplement 1 — PDF p. 30.

### Candidate statement

> Two printed urgent-PICU rates do not conventionally round from the displayed numerator and denominators.

### AI rationale

> The protocol Sample Size Appendix reproduces Ontario 2007-8 historical data attributed to the Kotsakis 2009 collaborative report: 1052 admissions, denominators 7300/55963, and rates 14.5%/18 per 1000. The rates do not round from those historical integers. In v.2.0.3 this is background material within consolidated P\_P, not current trial reported-versus-planned results.

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

> The four-hospital table prints 1,052 unplanned PICU admissions, 7,300 PICU discharges, 55,963 hospital discharges, 14.5%, and 18 per 1,000.

#### Evidence 1: Reported-versus-comparator

> Printed 14.5% and 18 per 1,000 versus rates calculated from the displayed integers.

#### Evidence 2: Calculation

> 1052/7300 × 100 = 14.4109589%, conventionally 14.4%; 1052/55963 × 1,000 = 18.7977778, conventionally 19. The printed denominators fall outside the respective nearest-rounding denominator ranges 7,231–7,280 and 56,865–60,114.

#### Evidence 3: Alternative source-grounded interpretations

> Undisplayed denominators, weighting, extraction history, or a display convention could explain one or both rates; truncation could explain 18 but not 14.5 from 14.4109589.

### Source links

- sourceLinks 0: [Supplement 1 — PDF p. 30](../../../2018/jama.2018.0948/joi180015supp1_prod.pdf#page=30)
- evidencePaths 0: [2018/jama.2018.0948/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.0948/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.0948/.ai\_paper\_validation/review\_1\_5\_2/candidate\_ledger.md](../../../2018/jama.2018.0948/.ai_paper_validation/review_1_5_2/candidate_ledger.md)
- evidencePaths 2: [2018/jama.2018.0948/.ai\_paper\_validation/review\_1\_5\_2/preprocessing/native\_text/joi180015supp1\_prod.txt](../../../2018/jama.2018.0948/.ai_paper_validation/review_1_5_2/preprocessing/native_text/joi180015supp1_prod.txt)

[Original Markdown report](../../../2018/jama.2018.0948/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_P |
| legacyRelations | 0 | P\_B |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Historical reference-table data can be planning inputs, but this candidate targets the pre-existing counts/rates themselves. The original external report was not obtained for new adjudication. |
| broadPlanInvolved | 1 |
| category | Denominator, proportion, or total inconsistency |
| currentReportCrossDocument | 0 |
| id | C007 |
| key | 2018::jama.2018.0948::C007 |
| legacyRelationship | P\_B |
| locations | Supplement 1 — PDF p. 30. |
| originalCrossDocument | 0 |
| package | jama.2018.0948 |
| planMechanism |  |
| primary | P\_P |
| rationale | The protocol Sample Size Appendix reproduces Ontario 2007-8 historical data attributed to the Kotsakis 2009 collaborative report: 1052 admissions, denominators 7300/55963, and rates 14.5%/18 per 1000. The rates do not round from those historical integers. In v.2.0.3 this is background material within consolidated P\_P, not current trial reported-versus-planned results. |
| reportHref | ../../2018/jama.2018.0948/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.0948/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C007 |
| sourceStatus | Pending Human Adjudication |
| statement | Two printed urgent-PICU rates do not conventionally round from the displayed numerator and denominators. |
| submissionInvolved | 0 |
| subtype | planning\_reference\_rates |
| suggestedDomain | plan\_material |
| title | Urgent PICU admission rates do not match the printed counts and denominators at conventional rounding |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
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
