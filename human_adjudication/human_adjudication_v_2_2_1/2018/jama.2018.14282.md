# jama.2018.14282

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2018 |
| Paper | jama.2018.14282 |
| Candidates | 28 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2018/jama.2018.14282/)

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

- [C001](#candidate-c001) — Standard-arm men percentage does not reconcile (S_W)
- [C002](#candidate-c002) — Standard-arm women percentage does not reconcile (S_W)
- [C003](#candidate-c003) — Standard-arm heart-failure percentage does not reconcile (S_W)
- [C004](#candidate-c004) — High-flow liver-disease percentage conflicts with displayed count (S_W)
- [C005](#candidate-c005) — Standard-arm kidney-disease percentage conflicts with displayed count (S_W)
- [C006](#candidate-c006) — Standard-arm nontransplant immunosuppression percentage does not reconcile (S_W)
- [C007](#candidate-c007) — High-flow ≥3-days-after-ICU-admission percentage does not reconcile (S_W)
- [C008](#candidate-c008) — Standard-arm ≥3-days-after-ICU-admission percentage does not reconcile (S_W)
- [C009](#candidate-c009) — Standard-arm vasopressor percentage does not reconcile (S_W)
- [C010](#candidate-c010) — High-flow do-not-intubate percentage does not reconcile (S_W)
- [C011](#candidate-c011) — High-flow do-not-resuscitate percentage does not reconcile (S_W)
- [C012](#candidate-c012) — Standard-arm do-not-resuscitate percentage does not reconcile (S_W)
- [C013](#candidate-c013) — Standard-arm unknown-goals percentage does not reconcile (S_W)
- [C014](#candidate-c014) — High-flow pre-randomization standard-oxygen percentage does not reconcile (S_W)
- [C015](#candidate-c015) — High-flow ICU-acquired-infection percentage does not reconcile (S_W)
- [C016](#candidate-c016) — Standard-arm hospital-mortality percentage does not reconcile (S_W)
- [C017](#candidate-c017) — Respiratory-rate confidence-interval endpoint differs between matched occurrences (S_W)
- [C018](#candidate-c018) — Arm-attributed support-needs percentages use the overall-population denominator (S_W)
- [C019](#candidate-c019) — eTable high-flow invasive-MV percentage does not reconcile (S_W)
- [C020](#candidate-c020) — eTable standard-arm invasive-MV percentage does not reconcile (S_W)
- [C021](#candidate-c021) — eTable standard-oxygen-only percentage does not reconcile (S_W)
- [C022](#candidate-c022) — IMV cumulative-incidence comparison has incompatible printed test labels (S_C)
- [C023](#candidate-c023) — Figure 3A mortality HR has a near-reciprocal orientation relative to Table 2 (S_W)
- [C024](#candidate-c024) — Figure 3B IMV HR has a near-reciprocal orientation relative to Table 2 (S_W)
- [C025](#candidate-c025) — Revised-superiority sample-size total conflicts with equal arm counts (S_W)
- [C026](#candidate-c026) — Noninferiority bound/sign wording conflicts with its explanatory axis (P_P)
- [C027](#candidate-c027) — Primary-hypothesis intervention is labelled NIV while plans identify HFNO (P_P)
- [C028](#candidate-c028) — Planned primary outcome alternates between day-28 vital status and hospital death (P_P)

## Candidate C001

**Standard-arm men percentage does not reconcile**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14282::C001 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001 Table 1 — PDF p. 4

### Candidate statement

> The printed standard-arm men count and percentage do not reconcile under nearest one-decimal rounding.

### AI rationale

> The printed standard-arm men count and percentage do not reconcile under nearest one-decimal rounding. The focal mismatch is within the main article.

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

> Standard Oxygen Therapy n=388, men 247 (63.6).

#### Evidence 1: Reported-versus-comparator

> Reported 63.6% versus 63.7% from 247/388.

#### Evidence 2: Calculation

> 247/388×100=63.6598%; nearest one decimal=63.7%.

#### Evidence 3: Alternative source-grounded interpretations

> An unstated denominator or rounding convention could explain the display.

### Source links

- sourceLinks 0: [DOC-001 Table 1 — PDF p. 4](../../../2018/jama.2018.14282/jama_azoulay_2018_oi_180109.pdf#page=4)
- evidencePaths 0: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14282/.ai_paper_validation/final_report_1_5_2.md)

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
| key | 2018::jama.2018.14282::C001 |
| legacyRelationship |  |
| locations | DOC-001 Table 1 — PDF p. 4 |
| originalCrossDocument | 0 |
| package | jama.2018.14282 |
| planMechanism |  |
| primary | S\_W |
| rationale | The printed standard-arm men count and percentage do not reconcile under nearest one-decimal rounding. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | The printed standard-arm men count and percentage do not reconcile under nearest one-decimal rounding. |
| submissionInvolved | 1 |
| subtype | count\_percentage\_rounding |
| suggestedDomain | statistical\_results |
| title | Standard-arm men percentage does not reconcile |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C002

**Standard-arm women percentage does not reconcile**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14282::C002 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001 Table 1 — PDF p. 4

### Candidate statement

> The printed standard-arm women count and percentage do not reconcile under nearest one-decimal rounding.

### AI rationale

> The printed standard-arm women count and percentage do not reconcile under nearest one-decimal rounding. The focal mismatch is within the main article.

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

> Standard Oxygen Therapy n=388, women 141 (36.4).

#### Evidence 1: Reported-versus-comparator

> Reported 36.4% versus 36.3% from 141/388.

#### Evidence 2: Calculation

> 141/388×100=36.3402%; nearest one decimal=36.3%.

#### Evidence 3: Alternative source-grounded interpretations

> An unstated denominator or rounding convention could explain the display.

### Source links

- sourceLinks 0: [DOC-001 Table 1 — PDF p. 4](../../../2018/jama.2018.14282/jama_azoulay_2018_oi_180109.pdf#page=4)
- evidencePaths 0: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14282/.ai_paper_validation/final_report_1_5_2.md)

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
| key | 2018::jama.2018.14282::C002 |
| legacyRelationship |  |
| locations | DOC-001 Table 1 — PDF p. 4 |
| originalCrossDocument | 0 |
| package | jama.2018.14282 |
| planMechanism |  |
| primary | S\_W |
| rationale | The printed standard-arm women count and percentage do not reconcile under nearest one-decimal rounding. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | The printed standard-arm women count and percentage do not reconcile under nearest one-decimal rounding. |
| submissionInvolved | 1 |
| subtype | count\_percentage\_rounding |
| suggestedDomain | statistical\_results |
| title | Standard-arm women percentage does not reconcile |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C003

**Standard-arm heart-failure percentage does not reconcile**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14282::C003 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001 Table 1 — PDF p. 4

### Candidate statement

> The standard-arm heart-failure percentage does not reconcile under nearest one-decimal rounding.

### AI rationale

> The standard-arm heart-failure percentage does not reconcile under nearest one-decimal rounding. The focal mismatch is within the main article.

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

> Standard Oxygen Therapy n=388, heart failure 27 (6.9).

#### Evidence 1: Reported-versus-comparator

> Reported 6.9% versus 7.0% from 27/388.

#### Evidence 2: Calculation

> 27/388×100=6.9588%; nearest one decimal=7.0%.

#### Evidence 3: Alternative source-grounded interpretations

> A row-specific denominator or another rounding convention is not documented.

### Source links

- sourceLinks 0: [DOC-001 Table 1 — PDF p. 4](../../../2018/jama.2018.14282/jama_azoulay_2018_oi_180109.pdf#page=4)
- evidencePaths 0: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14282/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C003 |
| key | 2018::jama.2018.14282::C003 |
| legacyRelationship |  |
| locations | DOC-001 Table 1 — PDF p. 4 |
| originalCrossDocument | 0 |
| package | jama.2018.14282 |
| planMechanism |  |
| primary | S\_W |
| rationale | The standard-arm heart-failure percentage does not reconcile under nearest one-decimal rounding. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | The standard-arm heart-failure percentage does not reconcile under nearest one-decimal rounding. |
| submissionInvolved | 1 |
| subtype | count\_percentage\_rounding |
| suggestedDomain | statistical\_results |
| title | Standard-arm heart-failure percentage does not reconcile |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C004

**High-flow liver-disease percentage conflicts with displayed count**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14282::C004 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001 Table 1 — PDF p. 4

### Candidate statement

> The high-flow liver-disease count and percentage do not reconcile with the displayed arm denominator.

### AI rationale

> The high-flow liver-disease count and percentage do not reconcile with the displayed arm denominator. The focal mismatch is within the main article.

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

> High-Flow Oxygen Therapy n=388, liver disease 45 (13.3).

#### Evidence 1: Reported-versus-comparator

> Reported 13.3% versus 11.6% from 45/388.

#### Evidence 2: Calculation

> 45/388×100=11.5979%; nearest one decimal=11.6%.

#### Evidence 3: Alternative source-grounded interpretations

> A different population, transcription, or column-placement issue could explain the pair; none is identified in the source.

### Source links

- sourceLinks 0: [DOC-001 Table 1 — PDF p. 4](../../../2018/jama.2018.14282/jama_azoulay_2018_oi_180109.pdf#page=4)
- evidencePaths 0: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14282/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C004 |
| key | 2018::jama.2018.14282::C004 |
| legacyRelationship |  |
| locations | DOC-001 Table 1 — PDF p. 4 |
| originalCrossDocument | 0 |
| package | jama.2018.14282 |
| planMechanism |  |
| primary | S\_W |
| rationale | The high-flow liver-disease count and percentage do not reconcile with the displayed arm denominator. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C004 |
| sourceStatus | Pending Human Adjudication |
| statement | The high-flow liver-disease count and percentage do not reconcile with the displayed arm denominator. |
| submissionInvolved | 1 |
| subtype | count\_percentage\_rounding |
| suggestedDomain | statistical\_results |
| title | High-flow liver-disease percentage conflicts with displayed count |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C005

**Standard-arm kidney-disease percentage conflicts with displayed count**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14282::C005 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001 Table 1 — PDF p. 4

### Candidate statement

> The standard-arm kidney-disease count and percentage do not reconcile with the displayed arm denominator.

### AI rationale

> The standard-arm kidney-disease count and percentage do not reconcile with the displayed arm denominator. The focal mismatch is within the main article.

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

> Standard Oxygen Therapy n=388, kidney disease 69 (20.4).

#### Evidence 1: Reported-versus-comparator

> Reported 20.4% versus 17.8% from 69/388.

#### Evidence 2: Calculation

> 69/388×100=17.7835%; nearest one decimal=17.8%.

#### Evidence 3: Alternative source-grounded interpretations

> A different population, transcription, or column-placement issue is possible but not identified.

### Source links

- sourceLinks 0: [DOC-001 Table 1 — PDF p. 4](../../../2018/jama.2018.14282/jama_azoulay_2018_oi_180109.pdf#page=4)
- evidencePaths 0: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14282/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C005 |
| key | 2018::jama.2018.14282::C005 |
| legacyRelationship |  |
| locations | DOC-001 Table 1 — PDF p. 4 |
| originalCrossDocument | 0 |
| package | jama.2018.14282 |
| planMechanism |  |
| primary | S\_W |
| rationale | The standard-arm kidney-disease count and percentage do not reconcile with the displayed arm denominator. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C005 |
| sourceStatus | Pending Human Adjudication |
| statement | The standard-arm kidney-disease count and percentage do not reconcile with the displayed arm denominator. |
| submissionInvolved | 1 |
| subtype | count\_percentage\_rounding |
| suggestedDomain | statistical\_results |
| title | Standard-arm kidney-disease percentage conflicts with displayed count |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C006

**Standard-arm nontransplant immunosuppression percentage does not reconcile**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14282::C006 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001 Table 1 — PDF p. 4

### Candidate statement

> The standard-arm nontransplant immunosuppression percentage does not reconcile under nearest one-decimal rounding.

### AI rationale

> The standard-arm nontransplant immunosuppression percentage does not reconcile under nearest one-decimal rounding. The focal mismatch is within the main article.

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

> Non-transplant-related reasons, Standard Oxygen Therapy n=388, 98 (25.2).

#### Evidence 1: Reported-versus-comparator

> Reported 25.2% versus 25.3% from 98/388.

#### Evidence 2: Calculation

> 98/388×100=25.2577%; nearest one decimal=25.3%; child counts 98+37=135 reconcile to the parent.

#### Evidence 3: Alternative source-grounded interpretations

> An undocumented adjustment across child percentages is possible; the count subtotal is coherent.

### Source links

- sourceLinks 0: [DOC-001 Table 1 — PDF p. 4](../../../2018/jama.2018.14282/jama_azoulay_2018_oi_180109.pdf#page=4)
- evidencePaths 0: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14282/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C006 |
| key | 2018::jama.2018.14282::C006 |
| legacyRelationship |  |
| locations | DOC-001 Table 1 — PDF p. 4 |
| originalCrossDocument | 0 |
| package | jama.2018.14282 |
| planMechanism |  |
| primary | S\_W |
| rationale | The standard-arm nontransplant immunosuppression percentage does not reconcile under nearest one-decimal rounding. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C006 |
| sourceStatus | Pending Human Adjudication |
| statement | The standard-arm nontransplant immunosuppression percentage does not reconcile under nearest one-decimal rounding. |
| submissionInvolved | 1 |
| subtype | count\_percentage\_rounding |
| suggestedDomain | statistical\_results |
| title | Standard-arm nontransplant immunosuppression percentage does not reconcile |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C007

**High-flow ≥3-days-after-ICU-admission percentage does not reconcile**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14282::C007 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001 Table 1 — PDF p. 4

### Candidate statement

> The high-flow ≥3-days-after-admission percentage does not reconcile under nearest one-decimal rounding.

### AI rationale

> The high-flow ≥3-days-after-admission percentage does not reconcile under nearest one-decimal rounding. The focal mismatch is within the main article.

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

> High-flow arm n=388, randomization ≥3 days after, 20 (5.1).

#### Evidence 1: Reported-versus-comparator

> Reported 5.1% versus 5.2% from 20/388.

#### Evidence 2: Calculation

> 20/388×100=5.1546%; nearest one decimal=5.2%; timing counts sum to 388.

#### Evidence 3: Alternative source-grounded interpretations

> An undocumented category-level adjustment could explain the display.

### Source links

- sourceLinks 0: [DOC-001 Table 1 — PDF p. 4](../../../2018/jama.2018.14282/jama_azoulay_2018_oi_180109.pdf#page=4)
- evidencePaths 0: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14282/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C007 |
| key | 2018::jama.2018.14282::C007 |
| legacyRelationship |  |
| locations | DOC-001 Table 1 — PDF p. 4 |
| originalCrossDocument | 0 |
| package | jama.2018.14282 |
| planMechanism |  |
| primary | S\_W |
| rationale | The high-flow ≥3-days-after-admission percentage does not reconcile under nearest one-decimal rounding. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C007 |
| sourceStatus | Pending Human Adjudication |
| statement | The high-flow ≥3-days-after-admission percentage does not reconcile under nearest one-decimal rounding. |
| submissionInvolved | 1 |
| subtype | count\_percentage\_rounding |
| suggestedDomain | statistical\_results |
| title | High-flow ≥3-days-after-ICU-admission percentage does not reconcile |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C008

**Standard-arm ≥3-days-after-ICU-admission percentage does not reconcile**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14282::C008 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001 Table 1 — PDF p. 4

### Candidate statement

> The standard-arm ≥3-days-after-admission percentage does not reconcile under nearest one-decimal rounding.

### AI rationale

> The standard-arm ≥3-days-after-admission percentage does not reconcile under nearest one-decimal rounding. The focal mismatch is within the main article.

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

> Standard arm n=388, randomization ≥3 days after, 20 (5.1).

#### Evidence 1: Reported-versus-comparator

> Reported 5.1% versus 5.2% from 20/388.

#### Evidence 2: Calculation

> 20/388×100=5.1546%; nearest one decimal=5.2%; timing counts sum to 388.

#### Evidence 3: Alternative source-grounded interpretations

> An undocumented category-level adjustment could explain the display.

### Source links

- sourceLinks 0: [DOC-001 Table 1 — PDF p. 4](../../../2018/jama.2018.14282/jama_azoulay_2018_oi_180109.pdf#page=4)
- evidencePaths 0: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14282/.ai_paper_validation/final_report_1_5_2.md)

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
| key | 2018::jama.2018.14282::C008 |
| legacyRelationship |  |
| locations | DOC-001 Table 1 — PDF p. 4 |
| originalCrossDocument | 0 |
| package | jama.2018.14282 |
| planMechanism |  |
| primary | S\_W |
| rationale | The standard-arm ≥3-days-after-admission percentage does not reconcile under nearest one-decimal rounding. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C008 |
| sourceStatus | Pending Human Adjudication |
| statement | The standard-arm ≥3-days-after-admission percentage does not reconcile under nearest one-decimal rounding. |
| submissionInvolved | 1 |
| subtype | count\_percentage\_rounding |
| suggestedDomain | statistical\_results |
| title | Standard-arm ≥3-days-after-ICU-admission percentage does not reconcile |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C009

**Standard-arm vasopressor percentage does not reconcile**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14282::C009 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001 Table 1 — PDF p. 4

### Candidate statement

> The standard-arm vasopressor percentage does not reconcile under nearest one-decimal rounding.

### AI rationale

> The standard-arm vasopressor percentage does not reconcile under nearest one-decimal rounding. The focal mismatch is within the main article.

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

> Standard arm n=388, vasopressors 39 (10.0).

#### Evidence 1: Reported-versus-comparator

> Reported 10.0% versus 10.1% from 39/388.

#### Evidence 2: Calculation

> 39/388×100=10.0515%; nearest one decimal=10.1%.

#### Evidence 3: Alternative source-grounded interpretations

> Truncation or a hidden denominator could explain the last-place difference, but neither is documented.

### Source links

- sourceLinks 0: [DOC-001 Table 1 — PDF p. 4](../../../2018/jama.2018.14282/jama_azoulay_2018_oi_180109.pdf#page=4)
- evidencePaths 0: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14282/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C009 |
| key | 2018::jama.2018.14282::C009 |
| legacyRelationship |  |
| locations | DOC-001 Table 1 — PDF p. 4 |
| originalCrossDocument | 0 |
| package | jama.2018.14282 |
| planMechanism |  |
| primary | S\_W |
| rationale | The standard-arm vasopressor percentage does not reconcile under nearest one-decimal rounding. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C009 |
| sourceStatus | Pending Human Adjudication |
| statement | The standard-arm vasopressor percentage does not reconcile under nearest one-decimal rounding. |
| submissionInvolved | 1 |
| subtype | count\_percentage\_rounding |
| suggestedDomain | statistical\_results |
| title | Standard-arm vasopressor percentage does not reconcile |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C010

**High-flow do-not-intubate percentage does not reconcile**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14282::C010 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001 Table 1 — PDF p. 4

### Candidate statement

> The high-flow do-not-intubate percentage does not reconcile under nearest one-decimal rounding.

### AI rationale

> The high-flow do-not-intubate percentage does not reconcile under nearest one-decimal rounding. The focal mismatch is within the main article.

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

> High-flow arm n=388, do not intubate 13 (3.3).

#### Evidence 1: Reported-versus-comparator

> Reported 3.3% versus 3.4% from 13/388.

#### Evidence 2: Calculation

> 13/388×100=3.3505%; nearest one decimal=3.4%.

#### Evidence 3: Alternative source-grounded interpretations

> Decimal truncation could reproduce 3.3%, but no uniform truncation policy is supplied.

### Source links

- sourceLinks 0: [DOC-001 Table 1 — PDF p. 4](../../../2018/jama.2018.14282/jama_azoulay_2018_oi_180109.pdf#page=4)
- evidencePaths 0: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14282/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C010 |
| key | 2018::jama.2018.14282::C010 |
| legacyRelationship |  |
| locations | DOC-001 Table 1 — PDF p. 4 |
| originalCrossDocument | 0 |
| package | jama.2018.14282 |
| planMechanism |  |
| primary | S\_W |
| rationale | The high-flow do-not-intubate percentage does not reconcile under nearest one-decimal rounding. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C010 |
| sourceStatus | Pending Human Adjudication |
| statement | The high-flow do-not-intubate percentage does not reconcile under nearest one-decimal rounding. |
| submissionInvolved | 1 |
| subtype | count\_percentage\_rounding |
| suggestedDomain | statistical\_results |
| title | High-flow do-not-intubate percentage does not reconcile |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C011

**High-flow do-not-resuscitate percentage does not reconcile**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14282::C011 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001 Table 1 — PDF p. 4

### Candidate statement

> The high-flow do-not-resuscitate percentage does not reconcile under nearest one-decimal rounding.

### AI rationale

> The high-flow do-not-resuscitate percentage does not reconcile under nearest one-decimal rounding. The focal mismatch is within the main article.

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

> High-flow arm n=388, do not resuscitate 3 (0.7).

#### Evidence 1: Reported-versus-comparator

> Reported 0.7% versus 0.8% from 3/388.

#### Evidence 2: Calculation

> 3/388×100=0.7732%; nearest one decimal=0.8%.

#### Evidence 3: Alternative source-grounded interpretations

> Truncation is possible but unstated.

### Source links

- sourceLinks 0: [DOC-001 Table 1 — PDF p. 4](../../../2018/jama.2018.14282/jama_azoulay_2018_oi_180109.pdf#page=4)
- evidencePaths 0: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14282/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C011 |
| key | 2018::jama.2018.14282::C011 |
| legacyRelationship |  |
| locations | DOC-001 Table 1 — PDF p. 4 |
| originalCrossDocument | 0 |
| package | jama.2018.14282 |
| planMechanism |  |
| primary | S\_W |
| rationale | The high-flow do-not-resuscitate percentage does not reconcile under nearest one-decimal rounding. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C011 |
| sourceStatus | Pending Human Adjudication |
| statement | The high-flow do-not-resuscitate percentage does not reconcile under nearest one-decimal rounding. |
| submissionInvolved | 1 |
| subtype | count\_percentage\_rounding |
| suggestedDomain | statistical\_results |
| title | High-flow do-not-resuscitate percentage does not reconcile |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C012

**Standard-arm do-not-resuscitate percentage does not reconcile**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14282::C012 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001 Table 1 — PDF p. 4

### Candidate statement

> The standard-arm do-not-resuscitate percentage does not reconcile under nearest one-decimal rounding.

### AI rationale

> The standard-arm do-not-resuscitate percentage does not reconcile under nearest one-decimal rounding. The focal mismatch is within the main article.

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

> Standard arm n=388, do not resuscitate 1 (0.2).

#### Evidence 1: Reported-versus-comparator

> Reported 0.2% versus 0.3% from 1/388.

#### Evidence 2: Calculation

> 1/388×100=0.2577%; nearest one decimal=0.3%.

#### Evidence 3: Alternative source-grounded interpretations

> Truncation is possible but unstated.

### Source links

- sourceLinks 0: [DOC-001 Table 1 — PDF p. 4](../../../2018/jama.2018.14282/jama_azoulay_2018_oi_180109.pdf#page=4)
- evidencePaths 0: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14282/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C012 |
| key | 2018::jama.2018.14282::C012 |
| legacyRelationship |  |
| locations | DOC-001 Table 1 — PDF p. 4 |
| originalCrossDocument | 0 |
| package | jama.2018.14282 |
| planMechanism |  |
| primary | S\_W |
| rationale | The standard-arm do-not-resuscitate percentage does not reconcile under nearest one-decimal rounding. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C012 |
| sourceStatus | Pending Human Adjudication |
| statement | The standard-arm do-not-resuscitate percentage does not reconcile under nearest one-decimal rounding. |
| submissionInvolved | 1 |
| subtype | count\_percentage\_rounding |
| suggestedDomain | statistical\_results |
| title | Standard-arm do-not-resuscitate percentage does not reconcile |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C013

**Standard-arm unknown-goals percentage does not reconcile**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14282::C013 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001 Table 1 — PDF p. 4

### Candidate statement

> The standard-arm unknown-goals-of-care percentage does not reconcile under nearest one-decimal rounding.

### AI rationale

> The standard-arm unknown-goals-of-care percentage does not reconcile under nearest one-decimal rounding. The focal mismatch is within the main article.

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

> Standard arm n=388, unknown goals of care 27 (6.9).

#### Evidence 1: Reported-versus-comparator

> Reported 6.9% versus 7.0% from 27/388.

#### Evidence 2: Calculation

> 27/388×100=6.9588%; nearest one decimal=7.0%; all five goals-of-care counts sum to 388.

#### Evidence 3: Alternative source-grounded interpretations

> An adjusted display across exhaustive categories is possible; the count distribution is complete.

### Source links

- sourceLinks 0: [DOC-001 Table 1 — PDF p. 4](../../../2018/jama.2018.14282/jama_azoulay_2018_oi_180109.pdf#page=4)
- evidencePaths 0: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14282/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C013 |
| key | 2018::jama.2018.14282::C013 |
| legacyRelationship |  |
| locations | DOC-001 Table 1 — PDF p. 4 |
| originalCrossDocument | 0 |
| package | jama.2018.14282 |
| planMechanism |  |
| primary | S\_W |
| rationale | The standard-arm unknown-goals-of-care percentage does not reconcile under nearest one-decimal rounding. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C013 |
| sourceStatus | Pending Human Adjudication |
| statement | The standard-arm unknown-goals-of-care percentage does not reconcile under nearest one-decimal rounding. |
| submissionInvolved | 1 |
| subtype | count\_percentage\_rounding |
| suggestedDomain | statistical\_results |
| title | Standard-arm unknown-goals percentage does not reconcile |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C014

**High-flow pre-randomization standard-oxygen percentage does not reconcile**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14282::C014 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001 Table 1 — PDF p. 4

### Candidate statement

> The high-flow pre-randomization standard-oxygen percentage does not reconcile under nearest one-decimal rounding.

### AI rationale

> The high-flow pre-randomization standard-oxygen percentage does not reconcile under nearest one-decimal rounding. The focal mismatch is within the main article.

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

> High-flow arm n=388, received standard oxygen before randomization 311 (80.1).

#### Evidence 1: Reported-versus-comparator

> Reported 80.1% versus 80.2% from 311/388.

#### Evidence 2: Calculation

> 311/388×100=80.1546%; nearest one decimal=80.2%.

#### Evidence 3: Alternative source-grounded interpretations

> A data-availability denominator is conceivable, but no missingness count or alternate denominator is printed.

### Source links

- sourceLinks 0: [DOC-001 Table 1 — PDF p. 4](../../../2018/jama.2018.14282/jama_azoulay_2018_oi_180109.pdf#page=4)
- evidencePaths 0: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14282/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C014 |
| key | 2018::jama.2018.14282::C014 |
| legacyRelationship |  |
| locations | DOC-001 Table 1 — PDF p. 4 |
| originalCrossDocument | 0 |
| package | jama.2018.14282 |
| planMechanism |  |
| primary | S\_W |
| rationale | The high-flow pre-randomization standard-oxygen percentage does not reconcile under nearest one-decimal rounding. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C014 |
| sourceStatus | Pending Human Adjudication |
| statement | The high-flow pre-randomization standard-oxygen percentage does not reconcile under nearest one-decimal rounding. |
| submissionInvolved | 1 |
| subtype | count\_percentage\_rounding |
| suggestedDomain | statistical\_results |
| title | High-flow pre-randomization standard-oxygen percentage does not reconcile |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C015

**High-flow ICU-acquired-infection percentage does not reconcile**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14282::C015 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001 Table 2 — PDF p. 5

### Candidate statement

> The high-flow ICU-acquired-infection percentage does not reconcile under nearest one-decimal rounding.

### AI rationale

> The high-flow ICU-acquired-infection percentage does not reconcile under nearest one-decimal rounding. The focal mismatch is within the main article.

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

> High-flow arm n=388, ICU-acquired infection 39 (10.0).

#### Evidence 1: Reported-versus-comparator

> Reported 10.0% versus 10.1% from 39/388.

#### Evidence 2: Calculation

> 39/388×100=10.0515%; nearest one decimal=10.1%; standard comparator 41/388=10.6% reconciles.

#### Evidence 3: Alternative source-grounded interpretations

> An infection-at-risk denominator is possible but not supplied in Table 2.

### Source links

- sourceLinks 0: [DOC-001 Table 2 — PDF p. 5](../../../2018/jama.2018.14282/jama_azoulay_2018_oi_180109.pdf#page=5)
- evidencePaths 0: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14282/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C015 |
| key | 2018::jama.2018.14282::C015 |
| legacyRelationship |  |
| locations | DOC-001 Table 2 — PDF p. 5 |
| originalCrossDocument | 0 |
| package | jama.2018.14282 |
| planMechanism |  |
| primary | S\_W |
| rationale | The high-flow ICU-acquired-infection percentage does not reconcile under nearest one-decimal rounding. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C015 |
| sourceStatus | Pending Human Adjudication |
| statement | The high-flow ICU-acquired-infection percentage does not reconcile under nearest one-decimal rounding. |
| submissionInvolved | 1 |
| subtype | count\_percentage\_rounding |
| suggestedDomain | statistical\_results |
| title | High-flow ICU-acquired-infection percentage does not reconcile |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C016

**Standard-arm hospital-mortality percentage does not reconcile**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14282::C016 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001 Table 2 — PDF p. 5

### Candidate statement

> The standard-arm hospital-mortality percentage does not reconcile under nearest one-decimal rounding.

### AI rationale

> The standard-arm hospital-mortality percentage does not reconcile under nearest one-decimal rounding. The focal mismatch is within the main article.

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

> Standard arm n=388, hospital mortality 162 (41.7).

#### Evidence 1: Reported-versus-comparator

> Reported 41.7% versus 41.8% from 162/388.

#### Evidence 2: Calculation

> 162/388×100=41.7526%; nearest one decimal=41.8%.

#### Evidence 3: Alternative source-grounded interpretations

> An alternate hospital-disposition denominator is not supplied; no loss to follow-up is printed.

### Source links

- sourceLinks 0: [DOC-001 Table 2 — PDF p. 5](../../../2018/jama.2018.14282/jama_azoulay_2018_oi_180109.pdf#page=5)
- evidencePaths 0: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14282/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C016 |
| key | 2018::jama.2018.14282::C016 |
| legacyRelationship |  |
| locations | DOC-001 Table 2 — PDF p. 5 |
| originalCrossDocument | 0 |
| package | jama.2018.14282 |
| planMechanism |  |
| primary | S\_W |
| rationale | The standard-arm hospital-mortality percentage does not reconcile under nearest one-decimal rounding. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C016 |
| sourceStatus | Pending Human Adjudication |
| statement | The standard-arm hospital-mortality percentage does not reconcile under nearest one-decimal rounding. |
| submissionInvolved | 1 |
| subtype | count\_percentage\_rounding |
| suggestedDomain | statistical\_results |
| title | Standard-arm hospital-mortality percentage does not reconcile |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C017

**Respiratory-rate confidence-interval endpoint differs between matched occurrences**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14282::C017 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-001 abstract — PDF p. 1; DOC-001 results — PDF p. 6

### Candidate statement

> Matched abstract and results displays give different upper 95% confidence-interval endpoints for the same six-hour respiratory-rate comparison.

### AI rationale

> The abstract and Results of the same main PDF report upper CI endpoints -0.2 and -0.3/min for the matched six-hour respiratory-rate result. The original cross-document category is a within-main repetition discrepancy.

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

> Both occurrences report 25 versus 26/min, difference −1.8, and lower endpoint −3.2; the abstract upper endpoint is −0.2 and results upper endpoint is −0.3.

#### Evidence 1: Reported-versus-comparator

> Abstract 95% CI upper endpoint −0.2/min versus results −0.3/min.

#### Evidence 2: Calculation

> The printed endpoint difference is 0.1/min.

#### Evidence 3: Alternative source-grounded interpretations

> Separately rounded or calculated intervals are possible, but unrounded endpoints, model identity, and the display rule are not supplied.

### Source links

- sourceLinks 0: [DOC-001 abstract — PDF p. 1](../../../2018/jama.2018.14282/jama_azoulay_2018_oi_180109.pdf#page=1)
- sourceLinks 1: [DOC-001 results — PDF p. 6](../../../2018/jama.2018.14282/jama_azoulay_2018_oi_180109.pdf#page=6)
- evidencePaths 0: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/candidate\_ledger.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/candidate_ledger.md)

[Original Markdown report](../../../2018/jama.2018.14282/.ai_paper_validation/final_report_1_5_2.md)

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
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 0 |
| id | C017 |
| key | 2018::jama.2018.14282::C017 |
| legacyRelationship |  |
| locations | DOC-001 abstract — PDF p. 1; DOC-001 results — PDF p. 6 |
| originalCrossDocument | 1 |
| package | jama.2018.14282 |
| planMechanism |  |
| primary | S\_W |
| rationale | The abstract and Results of the same main PDF report upper CI endpoints -0.2 and -0.3/min for the matched six-hour respiratory-rate result. The original cross-document category is a within-main repetition discrepancy. |
| reportHref | ../../2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C017 |
| sourceStatus | Pending Human Adjudication |
| statement | Matched abstract and results displays give different upper 95% confidence-interval endpoints for the same six-hour respiratory-rate comparison. |
| submissionInvolved | 1 |
| subtype | repeated\_ci\_endpoint |
| suggestedDomain | report\_internal\_inconsistency |
| title | Respiratory-rate confidence-interval endpoint differs between matched occurrences |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C018

**Arm-attributed support-needs percentages use the overall-population denominator**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14282::C018 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001 post hoc outcomes — PDF p. 6

### Candidate statement

> Arm-attributed support-needs counts are paired with overall-population percentages, creating a denominator-communication question rather than a demonstrated arithmetic error.

### AI rationale

> The main paragraph explicitly begins In the overall population; 153/776=19.7% and 31/776=4.0% are correct, but the arm-attributed wording could be misread as within-arm risks. The retained candidate is within-main denominator communication, not an established numerical contradiction.

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

> The paragraph begins In the overall population and reports 153 patients (19.7%) randomized to high-flow and 31 patients (4.0%) randomized to standard oxygen.

#### Evidence 1: Reported-versus-comparator

> Reported 19.7% and 4.0% equal 153/776 and 31/776; within-arm values would be 39.4% and 8.0% using 388 per arm.

#### Evidence 2: Calculation

> 153/776=19.7%; 31/776=4.0%; 153/388=39.4%; 31/388=8.0%.

#### Evidence 3: Alternative source-grounded interpretations

> The introductory overall-population phrase supports intentional overall denominators; the remaining issue is possible within-arm-risk misreading.

### Source links

- sourceLinks 0: [DOC-001 post hoc outcomes — PDF p. 6](../../../2018/jama.2018.14282/jama_azoulay_2018_oi_180109.pdf#page=6)
- evidencePaths 0: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)
- evidencePaths 2: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/candidate\_ledger.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/candidate_ledger.md)

[Original Markdown report](../../../2018/jama.2018.14282/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Communication-only candidate: arithmetic reproduces under the printed overall-population context. It is not an explicit failed evidence recheck, so evidence\_state remains recorded\_candidate; do not describe it as a confirmed inconsistency. |
| broadPlanInvolved | 0 |
| category | Denominator, proportion, or total inconsistency |
| currentReportCrossDocument | 0 |
| id | C018 |
| key | 2018::jama.2018.14282::C018 |
| legacyRelationship |  |
| locations | DOC-001 post hoc outcomes — PDF p. 6 |
| originalCrossDocument | 0 |
| package | jama.2018.14282 |
| planMechanism |  |
| primary | S\_W |
| rationale | The main paragraph explicitly begins In the overall population; 153/776=19.7% and 31/776=4.0% are correct, but the arm-attributed wording could be misread as within-arm risks. The retained candidate is within-main denominator communication, not an established numerical contradiction. |
| reportHref | ../../2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C018 |
| sourceStatus | Pending Human Adjudication |
| statement | Arm-attributed support-needs counts are paired with overall-population percentages, creating a denominator-communication question rather than a demonstrated arithmetic error. |
| submissionInvolved | 1 |
| subtype | denominator\_communication |
| suggestedDomain | statistical\_results |
| title | Arm-attributed support-needs percentages use the overall-population denominator |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C019

**eTable high-flow invasive-MV percentage does not reconcile**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14282::C019 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-003 eTable — PDF p. 2

### Candidate statement

> The eTable high-flow invasive-mechanical-ventilation percentage does not reconcile under nearest one-decimal rounding.

### AI rationale

> The eTable high-flow invasive-mechanical-ventilation percentage does not reconcile under nearest one-decimal rounding. The focal mismatch is within one non-plan results supplement.

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

> High-flow N=388, invasive mechanical ventilation 39 (10.0).

#### Evidence 1: Reported-versus-comparator

> Reported 10.0% versus 10.1% from 39/388.

#### Evidence 2: Calculation

> 39/388×100=10.0515%; nearest one decimal=10.1%; 39+349=388.

#### Evidence 3: Alternative source-grounded interpretations

> A six-hour evaluable denominator or truncation is possible but not printed.

### Source links

- sourceLinks 0: [DOC-003 eTable — PDF p. 2](../../../2018/jama.2018.14282/joi180109supp2_prod.pdf#page=2)
- evidencePaths 0: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/candidate\_ledger.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/candidate_ledger.md)

[Original Markdown report](../../../2018/jama.2018.14282/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C019 |
| key | 2018::jama.2018.14282::C019 |
| legacyRelationship |  |
| locations | DOC-003 eTable — PDF p. 2 |
| originalCrossDocument | 0 |
| package | jama.2018.14282 |
| planMechanism |  |
| primary | S\_W |
| rationale | The eTable high-flow invasive-mechanical-ventilation percentage does not reconcile under nearest one-decimal rounding. The focal mismatch is within one non-plan results supplement. |
| reportHref | ../../2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C019 |
| sourceStatus | Pending Human Adjudication |
| statement | The eTable high-flow invasive-mechanical-ventilation percentage does not reconcile under nearest one-decimal rounding. |
| submissionInvolved | 1 |
| subtype | count\_percentage\_rounding |
| suggestedDomain | statistical\_results |
| title | eTable high-flow invasive-MV percentage does not reconcile |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C020

**eTable standard-arm invasive-MV percentage does not reconcile**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14282::C020 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-003 eTable — PDF p. 2

### Candidate statement

> The eTable standard-arm invasive-mechanical-ventilation percentage does not reconcile under nearest one-decimal rounding.

### AI rationale

> The eTable standard-arm invasive-mechanical-ventilation percentage does not reconcile under nearest one-decimal rounding. The focal mismatch is within one non-plan results supplement.

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

> Standard arm N=388, invasive mechanical ventilation 46 (11.8).

#### Evidence 1: Reported-versus-comparator

> Reported 11.8% versus 11.9% from 46/388.

#### Evidence 2: Calculation

> 46/388×100=11.8557%; nearest one decimal=11.9%; 46+342=388.

#### Evidence 3: Alternative source-grounded interpretations

> The 11.8%/88.2% pair totals 100.0%, supporting a possible forced-complement rule that is not documented.

### Source links

- sourceLinks 0: [DOC-003 eTable — PDF p. 2](../../../2018/jama.2018.14282/joi180109supp2_prod.pdf#page=2)
- evidencePaths 0: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/candidate\_ledger.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/candidate_ledger.md)

[Original Markdown report](../../../2018/jama.2018.14282/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Complementary to C021 and may share a forced-total percentage-production rule; separate printed count/percentage cell, so not marked an identical duplicate. |
| broadPlanInvolved | 0 |
| category | Denominator, proportion, or total inconsistency |
| currentReportCrossDocument | 0 |
| id | C020 |
| key | 2018::jama.2018.14282::C020 |
| legacyRelationship |  |
| locations | DOC-003 eTable — PDF p. 2 |
| originalCrossDocument | 0 |
| package | jama.2018.14282 |
| planMechanism |  |
| primary | S\_W |
| rationale | The eTable standard-arm invasive-mechanical-ventilation percentage does not reconcile under nearest one-decimal rounding. The focal mismatch is within one non-plan results supplement. |
| reportHref | ../../2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C020 |
| sourceStatus | Pending Human Adjudication |
| statement | The eTable standard-arm invasive-mechanical-ventilation percentage does not reconcile under nearest one-decimal rounding. |
| submissionInvolved | 1 |
| subtype | count\_percentage\_rounding |
| suggestedDomain | statistical\_results |
| title | eTable standard-arm invasive-MV percentage does not reconcile |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C021

**eTable standard-oxygen-only percentage does not reconcile**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14282::C021 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-003 eTable — PDF p. 2

### Candidate statement

> The eTable standard-oxygen-only percentage does not reconcile under nearest one-decimal rounding.

### AI rationale

> The eTable standard-oxygen-only percentage does not reconcile under nearest one-decimal rounding. The focal mismatch is within one non-plan results supplement.

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

> Standard arm N=388, standard oxygen only 342 (88.2).

#### Evidence 1: Reported-versus-comparator

> Reported 88.2% versus 88.1% from 342/388.

#### Evidence 2: Calculation

> 342/388×100=88.1443%; nearest one decimal=88.1%; 342+46=388.

#### Evidence 3: Alternative source-grounded interpretations

> 88.2% is exactly the complement of printed 11.8%, so a forced complementary display is possible but not confirmed.

### Source links

- sourceLinks 0: [DOC-003 eTable — PDF p. 2](../../../2018/jama.2018.14282/joi180109supp2_prod.pdf#page=2)
- evidencePaths 0: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/candidate\_ledger.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/candidate_ledger.md)

[Original Markdown report](../../../2018/jama.2018.14282/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Complementary to C020 and may share a forced-total percentage-production rule; separate printed count/percentage cell, so not marked an identical duplicate. |
| broadPlanInvolved | 0 |
| category | Denominator, proportion, or total inconsistency |
| currentReportCrossDocument | 0 |
| id | C021 |
| key | 2018::jama.2018.14282::C021 |
| legacyRelationship |  |
| locations | DOC-003 eTable — PDF p. 2 |
| originalCrossDocument | 0 |
| package | jama.2018.14282 |
| planMechanism |  |
| primary | S\_W |
| rationale | The eTable standard-oxygen-only percentage does not reconcile under nearest one-decimal rounding. The focal mismatch is within one non-plan results supplement. |
| reportHref | ../../2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C021 |
| sourceStatus | Pending Human Adjudication |
| statement | The eTable standard-oxygen-only percentage does not reconcile under nearest one-decimal rounding. |
| submissionInvolved | 1 |
| subtype | count\_percentage\_rounding |
| suggestedDomain | statistical\_results |
| title | eTable standard-oxygen-only percentage does not reconcile |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C022

**IMV cumulative-incidence comparison has incompatible printed test labels**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14282::C022 |
| Frozen relationship | S\_C |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001 methods — PDF p. 4; DOC-001 results — PDF p. 6; DOC-003 eFigure 1 — PDF p. 3

### Candidate statement

> A matched invasive-mechanical-ventilation cumulative-incidence comparison is described with Gray testing in the main article and a log-rank label in the linked eFigure.

### AI rationale

> A matched invasive-mechanical-ventilation cumulative-incidence comparison is described with Gray testing in the main article and a log-rank label in the linked eFigure. The focal comparison is the main article versus a non-plan results supplement.

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

> Methods specify death without IMV as a competing risk and Gray testing; the eFigure prints P (log Rank test) = 0.17, matching the main P=.17.

#### Evidence 1: Reported-versus-comparator

> Gray test/competing-risk description versus log Rank test label for a matched result.

#### Evidence 2: Calculation

> No reconstruction is used; Gray and log-rank are distinct named tests.

#### Evidence 3: Alternative source-grounded interpretations

> Separate tests could both round to .17; test statistics, event/censoring data, and generating output are absent.

### Source links

- sourceLinks 0: [DOC-001 methods — PDF p. 4](../../../2018/jama.2018.14282/jama_azoulay_2018_oi_180109.pdf#page=4)
- sourceLinks 1: [DOC-001 results — PDF p. 6](../../../2018/jama.2018.14282/jama_azoulay_2018_oi_180109.pdf#page=6)
- sourceLinks 2: [DOC-003 eFigure 1 — PDF p. 3](../../../2018/jama.2018.14282/joi180109supp2_prod.pdf#page=3)
- evidencePaths 0: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/candidate\_ledger.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/candidate_ledger.md)

[Original Markdown report](../../../2018/jama.2018.14282/.ai_paper_validation/final_report_1_5_2.md)

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
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 1 |
| id | C022 |
| key | 2018::jama.2018.14282::C022 |
| legacyRelationship |  |
| locations | DOC-001 methods — PDF p. 4; DOC-001 results — PDF p. 6; DOC-003 eFigure 1 — PDF p. 3 |
| originalCrossDocument | 0 |
| package | jama.2018.14282 |
| planMechanism |  |
| primary | S\_C |
| rationale | A matched invasive-mechanical-ventilation cumulative-incidence comparison is described with Gray testing in the main article and a log-rank label in the linked eFigure. The focal comparison is the main article versus a non-plan results supplement. |
| reportHref | ../../2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C022 |
| sourceStatus | Pending Human Adjudication |
| statement | A matched invasive-mechanical-ventilation cumulative-incidence comparison is described with Gray testing in the main article and a log-rank label in the linked eFigure. |
| submissionInvolved | 1 |
| subtype | test\_label |
| suggestedDomain | statistical\_results |
| title | IMV cumulative-incidence comparison has incompatible printed test labels |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C023

**Figure 3A mortality HR has a near-reciprocal orientation relative to Table 2**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14282::C023 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-001 Table 2 and narrative — PDF p. 5; DOC-001 Figure 3A — PDF p. 7

### Candidate statement

> Figure 3A mortality HRs are near reciprocals of the matched Table 2/narrative HRs under favor labels, but the figure reference group is not printed.

### AI rationale

> Figure 3A mortality HRs are near reciprocals of the matched Table 2/narrative HRs under favor labels, but the figure reference group is not printed. The focal mismatch is within the main article.

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

> Same 138/388 versus 140/388 day-28 deaths: Table/narrative HR 0.98 (0.77–1.24); Figure 3A HR 1.02 (0.81–1.29), with Favors High-Flow left and Favors Standard right.

#### Evidence 1: Reported-versus-comparator

> Table/narrative 0.98 (0.77–1.24) versus Figure 3A 1.02 (0.81–1.29).

#### Evidence 2: Calculation

> 1/0.98=1.020 and 1/1.24=0.806 reproduce 1.02 and 0.81; 1/0.77=1.299 rounds to 1.30, not 1.29.

#### Evidence 3: Alternative source-grounded interpretations

> Opposite orientation is compatible with hidden precision; exact reciprocal identity from all rounded values is not established, and reference group/unrounded values are absent.

### Source links

- sourceLinks 0: [DOC-001 Table 2 and narrative — PDF p. 5](../../../2018/jama.2018.14282/jama_azoulay_2018_oi_180109.pdf#page=5)
- sourceLinks 1: [DOC-001 Figure 3A — PDF p. 7](../../../2018/jama.2018.14282/jama_azoulay_2018_oi_180109.pdf#page=7)
- evidencePaths 0: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/candidate\_ledger.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/candidate_ledger.md)

[Original Markdown report](../../../2018/jama.2018.14282/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Figure reference group is not defined. Recheck rejects exact reciprocal agreement from all rounded values, while preserving near-reciprocal orientation compatible with hidden precision; this is not a wholly non-reproduced candidate. |
| broadPlanInvolved | 0 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C023 |
| key | 2018::jama.2018.14282::C023 |
| legacyRelationship |  |
| locations | DOC-001 Table 2 and narrative — PDF p. 5; DOC-001 Figure 3A — PDF p. 7 |
| originalCrossDocument | 0 |
| package | jama.2018.14282 |
| planMechanism |  |
| primary | S\_W |
| rationale | Figure 3A mortality HRs are near reciprocals of the matched Table 2/narrative HRs under favor labels, but the figure reference group is not printed. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C023 |
| sourceStatus | Pending Human Adjudication |
| statement | Figure 3A mortality HRs are near reciprocals of the matched Table 2/narrative HRs under favor labels, but the figure reference group is not printed. |
| submissionInvolved | 1 |
| subtype | hr\_orientation |
| suggestedDomain | report\_internal\_inconsistency |
| title | Figure 3A mortality HR has a near-reciprocal orientation relative to Table 2 |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C024

**Figure 3B IMV HR has a near-reciprocal orientation relative to Table 2**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14282::C024 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-001 Table 2 — PDF p. 5; DOC-001 narrative — PDF p. 6; DOC-001 Figure 3B — PDF p. 7

### Candidate statement

> Figure 3B IMV HRs are near reciprocals of the matched Table 2/narrative cause-specific HRs under favor labels, but figure reference/estimand definition is not printed.

### AI rationale

> Figure 3B IMV HRs are near reciprocals of the matched Table 2/narrative cause-specific HRs under favor labels, but figure reference/estimand definition is not printed. The focal mismatch is within the main article.

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

> Same 150/388 versus 170/388 IMV events: Table/narrative cause-specific HR 0.85 (0.68–1.06); Figure 3B HR 1.17 (0.94–1.46) under the same favor labels.

#### Evidence 1: Reported-versus-comparator

> Table/narrative 0.85 (0.68–1.06) versus Figure 3B 1.17 (0.94–1.46).

#### Evidence 2: Calculation

> 1/1.06=0.943 gives 0.94; 1/0.85=1.176 gives 1.18 and 1/0.68=1.471 gives 1.47, not 1.17 and 1.46.

#### Evidence 3: Alternative source-grounded interpretations

> Hidden precision can support opposite orientation, but exact reciprocity cannot be derived from all rounded inputs; figure-specific reference group and estimand are absent.

### Source links

- sourceLinks 0: [DOC-001 Table 2 — PDF p. 5](../../../2018/jama.2018.14282/jama_azoulay_2018_oi_180109.pdf#page=5)
- sourceLinks 1: [DOC-001 narrative — PDF p. 6](../../../2018/jama.2018.14282/jama_azoulay_2018_oi_180109.pdf#page=6)
- sourceLinks 2: [DOC-001 Figure 3B — PDF p. 7](../../../2018/jama.2018.14282/jama_azoulay_2018_oi_180109.pdf#page=7)
- evidencePaths 0: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/candidate\_ledger.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/candidate_ledger.md)

[Original Markdown report](../../../2018/jama.2018.14282/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Figure reference group is not defined. Recheck rejects exact reciprocal agreement from all rounded values, while preserving near-reciprocal orientation compatible with hidden precision; this is not a wholly non-reproduced candidate. |
| broadPlanInvolved | 0 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C024 |
| key | 2018::jama.2018.14282::C024 |
| legacyRelationship |  |
| locations | DOC-001 Table 2 — PDF p. 5; DOC-001 narrative — PDF p. 6; DOC-001 Figure 3B — PDF p. 7 |
| originalCrossDocument | 0 |
| package | jama.2018.14282 |
| planMechanism |  |
| primary | S\_W |
| rationale | Figure 3B IMV HRs are near reciprocals of the matched Table 2/narrative cause-specific HRs under favor labels, but figure reference/estimand definition is not printed. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C024 |
| sourceStatus | Pending Human Adjudication |
| statement | Figure 3B IMV HRs are near reciprocals of the matched Table 2/narrative cause-specific HRs under favor labels, but figure reference/estimand definition is not printed. |
| submissionInvolved | 1 |
| subtype | hr\_orientation |
| suggestedDomain | report\_internal\_inconsistency |
| title | Figure 3B IMV HR has a near-reciprocal orientation relative to Table 2 |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C025

**Revised-superiority sample-size total conflicts with equal arm counts**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14282::C025 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001 — PDF p. 3; DOC-002 completed published-protocol abstract sentence — PDF p. 91; DOC-002 statistical-plan comparator — PDF p. 103

### Candidate statement

> The main article's revised-superiority total of 779 conflicts with two stated 389-person groups and the matched protocol/SAP total of 778.

### AI rationale

> The main article states 779 patients with 389 in each of two arms, internally contradicting 389+389=778. The protocol/SAP 778 total corroborates that arithmetic; it is not counted as a separate implemented-versus-planned sample-size departure.

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

> DOC-001 prints 779 patients (389 in each group); DOC-002 prints 778 with 389 per group under matching revised-superiority assumptions. The abstract sentence begins on p.90 and completes with 778 patients overall on p.91.

#### Evidence 1: Reported-versus-comparator

> Main 779 total with 389 each versus protocol/SAP 778 total with 389 each.

#### Evidence 2: Calculation

> 389+389=778, not 779.

#### Evidence 3: Alternative source-grounded interpretations

> An earlier unequal or rounded target is possible but not supplied; version history is absent.

### Source links

- sourceLinks 0: [DOC-001 — PDF p. 3](../../../2018/jama.2018.14282/jama_azoulay_2018_oi_180109.pdf#page=3)
- sourceLinks 1: [DOC-002 completed published-protocol abstract sentence — PDF p. 91](../../../2018/jama.2018.14282/joi180109supp1_prod.pdf#page=91)
- sourceLinks 2: [DOC-002 statistical-plan comparator — PDF p. 103](../../../2018/jama.2018.14282/joi180109supp1_prod.pdf#page=103)
- evidencePaths 0: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)
- evidencePaths 2: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/candidate\_ledger.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/candidate_ledger.md)

[Original Markdown report](../../../2018/jama.2018.14282/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Boundary decision: S\_W only; the plan comparison supports the internal total error. An unreported earlier unequal target remains possible. |
| broadPlanInvolved | 0 |
| category | Numeric or arithmetic inconsistency |
| currentReportCrossDocument | 0 |
| id | C025 |
| key | 2018::jama.2018.14282::C025 |
| legacyRelationship |  |
| locations | DOC-001 — PDF p. 3; DOC-002 completed published-protocol abstract sentence — PDF p. 91; DOC-002 statistical-plan comparator — PDF p. 103 |
| originalCrossDocument | 0 |
| package | jama.2018.14282 |
| planMechanism |  |
| primary | S\_W |
| rationale | The main article states 779 patients with 389 in each of two arms, internally contradicting 389+389=778. The protocol/SAP 778 total corroborates that arithmetic; it is not counted as a separate implemented-versus-planned sample-size departure. |
| reportHref | ../../2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C025 |
| sourceStatus | Pending Human Adjudication |
| statement | The main article's revised-superiority total of 779 conflicts with two stated 389-person groups and the matched protocol/SAP total of 778. |
| submissionInvolved | 1 |
| subtype | sample\_size\_sum |
| suggestedDomain | statistical\_results |
| title | Revised-superiority sample-size total conflicts with equal arm counts |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C026

**Noninferiority bound/sign wording conflicts with its explanatory axis**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14282::C026 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> DOC-002 Figure 4 — PDF p. 40; DOC-002 — PDF p. 42

### Candidate statement

> Noninferiority wording uses a positive less than 9% lower-bound statement that is not reconciled with the negative-side margin on a new-treatment-minus-active-control axis.

### AI rationale

> Noninferiority wording uses a positive less than 9% lower-bound statement that is not reconciled with the negative-side margin on a new-treatment-minus-active-control axis. The focal discrepancy is internal to the protocol/SAP material, including plan-version passages in a bound bundle.

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

> Figure 4 axis is Difference in Efficacy (New Treatment Minus Active Control) with margin on the negative side; text says noninferiority occurs if lower 95% CI boundary is less than 9%.

#### Evidence 1: Reported-versus-comparator

> Positive less than 9% wording versus negative-side margin on the printed scale.

#### Evidence 2: Calculation

> No numerical reconstruction is used; the positive bound/inequality is not mapped to the plotted signed scale.

#### Evidence 3: Alternative source-grounded interpretations

> A missing minus sign, opposite risk scale, or inequality could explain it; signed estimand and prespecified rule are absent.

### Source links

- sourceLinks 0: [DOC-002 Figure 4 — PDF p. 40](../../../2018/jama.2018.14282/joi180109supp1_prod.pdf#page=40)
- sourceLinks 1: [DOC-002 — PDF p. 42](../../../2018/jama.2018.14282/joi180109supp1_prod.pdf#page=42)
- evidencePaths 0: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)
- evidencePaths 2: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/candidate\_ledger.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/candidate_ledger.md)

[Original Markdown report](../../../2018/jama.2018.14282/.ai_paper_validation/final_report_1_5_2.md)

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
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 0 |
| id | C026 |
| key | 2018::jama.2018.14282::C026 |
| legacyRelationship |  |
| locations | DOC-002 Figure 4 — PDF p. 40; DOC-002 — PDF p. 42 |
| originalCrossDocument | 0 |
| package | jama.2018.14282 |
| planMechanism |  |
| primary | P\_P |
| rationale | Noninferiority wording uses a positive less than 9% lower-bound statement that is not reconciled with the negative-side margin on a new-treatment-minus-active-control axis. The focal discrepancy is internal to the protocol/SAP material, including plan-version passages in a bound bundle. |
| reportHref | ../../2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C026 |
| sourceStatus | Pending Human Adjudication |
| statement | Noninferiority wording uses a positive less than 9% lower-bound statement that is not reconciled with the negative-side margin on a new-treatment-minus-active-control axis. |
| submissionInvolved | 0 |
| subtype | noninferiority\_margin\_sign |
| suggestedDomain | plan\_material |
| title | Noninferiority bound/sign wording conflicts with its explanatory axis |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C027

**Primary-hypothesis intervention is labelled NIV while plans identify HFNO**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14282::C027 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> DOC-002 — PDF p. 52; DOC-002 — PDF p. 104

### Candidate statement

> Primary-hypothesis sentences label the intervention NIV while adjacent and repeated plan wording identifies HFNO as the experimental intervention.

### AI rationale

> Primary-hypothesis sentences label the intervention NIV while adjacent and repeated plan wording identifies HFNO as the experimental intervention. The focal discrepancy is internal to the protocol/SAP material, including plan-version passages in a bound bundle.

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

> Primary-hypothesis sentences say noninferiority/superiority of NIV; adjacent and repeated plan wording identifies HFNO against standard oxygen.

#### Evidence 1: Reported-versus-comparator

> NIV primary-hypothesis label versus HFNO experimental-intervention definition.

#### Evidence 2: Calculation

> Not applicable; this is a source-text label comparison.

#### Evidence 3: Alternative source-grounded interpretations

> NIV may be a carried-forward label, but no cited passage defines it as equivalent to HFNO in the primary hypothesis.

### Source links

- sourceLinks 0: [DOC-002 — PDF p. 52](../../../2018/jama.2018.14282/joi180109supp1_prod.pdf#page=52)
- sourceLinks 1: [DOC-002 — PDF p. 104](../../../2018/jama.2018.14282/joi180109supp1_prod.pdf#page=104)
- evidencePaths 0: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)
- evidencePaths 2: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/candidate\_ledger.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/candidate_ledger.md)

[Original Markdown report](../../../2018/jama.2018.14282/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C027 |
| key | 2018::jama.2018.14282::C027 |
| legacyRelationship |  |
| locations | DOC-002 — PDF p. 52; DOC-002 — PDF p. 104 |
| originalCrossDocument | 0 |
| package | jama.2018.14282 |
| planMechanism |  |
| primary | P\_P |
| rationale | Primary-hypothesis sentences label the intervention NIV while adjacent and repeated plan wording identifies HFNO as the experimental intervention. The focal discrepancy is internal to the protocol/SAP material, including plan-version passages in a bound bundle. |
| reportHref | ../../2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C027 |
| sourceStatus | Pending Human Adjudication |
| statement | Primary-hypothesis sentences label the intervention NIV while adjacent and repeated plan wording identifies HFNO as the experimental intervention. |
| submissionInvolved | 0 |
| subtype | planned\_intervention\_label |
| suggestedDomain | plan\_material |
| title | Primary-hypothesis intervention is labelled NIV while plans identify HFNO |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C028

**Planned primary outcome alternates between day-28 vital status and hospital death**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14282::C028 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> DOC-002 — PDF p. 54; DOC-002 — PDF p. 82; DOC-002 — PDF p. 104

### Candidate statement

> Plan passages classify patients by day-28 vital status but then specify a relative risk of hospital death without explicitly equating the endpoints.

### AI rationale

> Plan passages classify patients by day-28 vital status but then specify a relative risk of hospital death without explicitly equating the endpoints. The focal discrepancy is internal to the protocol/SAP material, including plan-version passages in a bound bundle.

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

> Each plan occurrence says patients are followed to day 28 and classified alive/dead, then specifies a relative risk of hospital death.

#### Evidence 1: Reported-versus-comparator

> Day-28 all-cause vital-status endpoint versus hospital-death label.

#### Evidence 2: Calculation

> Not applicable; the endpoints/time horizons are distinct unless explicitly equated.

#### Evidence 3: Alternative source-grounded interpretations

> Hospital death may be shorthand for day-28 death during admission, but hospital-death definition, discharge handling, post-discharge deaths, and equivalence are not supplied.

### Source links

- sourceLinks 0: [DOC-002 — PDF p. 54](../../../2018/jama.2018.14282/joi180109supp1_prod.pdf#page=54)
- sourceLinks 1: [DOC-002 — PDF p. 82](../../../2018/jama.2018.14282/joi180109supp1_prod.pdf#page=82)
- sourceLinks 2: [DOC-002 — PDF p. 104](../../../2018/jama.2018.14282/joi180109supp1_prod.pdf#page=104)
- evidencePaths 0: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)
- evidencePaths 2: [2018/jama.2018.14282/.ai\_paper\_validation/review\_1\_5\_2/candidate\_ledger.md](../../../2018/jama.2018.14282/.ai_paper_validation/review_1_5_2/candidate_ledger.md)

[Original Markdown report](../../../2018/jama.2018.14282/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C028 |
| key | 2018::jama.2018.14282::C028 |
| legacyRelationship |  |
| locations | DOC-002 — PDF p. 54; DOC-002 — PDF p. 82; DOC-002 — PDF p. 104 |
| originalCrossDocument | 0 |
| package | jama.2018.14282 |
| planMechanism |  |
| primary | P\_P |
| rationale | Plan passages classify patients by day-28 vital status but then specify a relative risk of hospital death without explicitly equating the endpoints. The focal discrepancy is internal to the protocol/SAP material, including plan-version passages in a bound bundle. |
| reportHref | ../../2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14282/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C028 |
| sourceStatus | Pending Human Adjudication |
| statement | Plan passages classify patients by day-28 vital status but then specify a relative risk of hospital death without explicitly equating the endpoints. |
| submissionInvolved | 0 |
| subtype | planned\_endpoint\_horizon |
| suggestedDomain | plan\_material |
| title | Planned primary outcome alternates between day-28 vital status and hospital death |
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
