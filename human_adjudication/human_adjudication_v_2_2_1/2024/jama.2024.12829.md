# jama.2024.12829

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2024 |
| Paper | jama.2024.12829 |
| Candidates | 17 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2024/jama.2024.12829/)

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

- [C001](#candidate-c001) — Balloon-angioplasty female percentage does not reconcile with count and denominator (S_W)
- [C002](#candidate-c002) — Balloon-angioplasty ischemic-stroke percentage is outside ordinary one-decimal rounding (S_W)
- [C003](#candidate-c003) — Table S4 procedure rows use 241 while the column header states 249 (S_W)
- [C004](#candidate-c004) — Table S6 BA 9 (3.9) conflicts with its displayed denominator 249 (S_W)
- [C005](#candidate-c005) — Table S7 group headers conflict with site totals and displayed site percentages (S_W)
- [C006](#candidate-c006) — Table S8 per-protocol percentages conflict with headers 249/252 (S_W)
- [C007](#candidate-c007) — Table S9 as-treated percentages conflict with headers 249/252 (S_W)
- [C008](#candidate-c008) — Baseline stenosis categories include values outside the stated 70%-99% eligibility range (S_W)
- [C009](#candidate-c009) — Thirty-day follow-up tolerance is plus or minus 3 days in the supplement but plus or minus 7 days elsewhere (P_R)
- [C010](#candidate-c010) — Protocol V2.0 gives 21-day and 14-day lower bounds for the same stroke criterion (P_P)
- [C011](#candidate-c011) — BA 3-month aspirin percentage does not reconcile with count and displayed arm denominator (S_W)
- [C012](#candidate-c012) — Figure S1 repeats “2nd meeting” for three chronologically distinct meetings (S_W)
- [C013](#candidate-c013) — Recurring-visit sentence ambiguously repeats visit numbers 9 and 11 (P_P)
- [C014](#candidate-c014) — Table S9 BA 8 (3.3) does not round from either supplied ATS or displayed denominator (S_W)
- [C015](#candidate-c015) — Narrative assigns all 11 pre-analysis exclusions to consent withdrawal while Figure 1 assigns only 10 (S_W)
- [C016](#candidate-c016) — Table S6 BA event count 9 conflicts with the matched primary-analysis count 11 (S_C)
- [C017](#candidate-c017) — One-year incidence-difference point estimate lies outside its confidence interval (S_W)

## Candidate C001

**Balloon-angioplasty female percentage does not reconcile with count and denominator**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.12829::C001 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001 Table 1, PDF p. 6

### Candidate statement

> The BA female percentage is inconsistent with the printed count and displayed arm denominator under ordinary nearest-one-decimal rounding.

### AI rationale

> Main Table1 gives77 females of249 as30.1% instead of the count-derived30.9%.

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

> BA n=249; male 172 (69.1) and female 77 (30.1).

#### Evidence 1: Reported-versus-comparator

> Reported female 30.1% versus 77/249.

#### Evidence 2: Calculation

> 172+77=249; 77/249×100=30.9237%, ordinarily 30.9%; printed sex percentages total 99.2%.

#### Evidence 3: Alternative source-grounded interpretations

> A hidden row denominator, transcription difference, or another displayed input could explain the observation; the source does not identify the production field that should govern.

### Source links

- sourceLinks 0: [DOC-001 Table 1, PDF p. 6](../../../2024/jama.2024.12829/jama_sun_2024_oi_240088_1746815064.14747.pdf#page=6)
- evidencePaths 0: [2024/jama.2024.12829/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.12829/.ai_paper_validation/review_1_5_3/source_inventory.md)

[Original Markdown report](../../../2024/jama.2024.12829/.ai_paper_validation/final_report_1_5_3.md)

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
| key | 2024::jama.2024.12829::C001 |
| legacyRelationship |  |
| locations | DOC-001 Table 1, PDF p. 6 |
| originalCrossDocument | 0 |
| package | jama.2024.12829 |
| planMechanism |  |
| primary | S\_W |
| rationale | Main Table1 gives77 females of249 as30.1% instead of the count-derived30.9%. |
| reportHref | ../../2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | The BA female percentage is inconsistent with the printed count and displayed arm denominator under ordinary nearest-one-decimal rounding. |
| submissionInvolved | 1 |
| subtype | count\_percentage |
| suggestedDomain | statistical\_results |
| title | Balloon-angioplasty female percentage does not reconcile with count and denominator |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C002

**Balloon-angioplasty ischemic-stroke percentage is outside ordinary one-decimal rounding**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.12829::C002 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001 Table 1, PDF p. 6; DOC-002 Table S1, PDF p. 14

### Candidate statement

> The repeated BA ischemic-stroke percentage is conditionally inconsistent with ordinary nearest-one-decimal rounding.

### AI rationale

> Main Table1 and results-supplement TableS1 identically repeat215/249 as86.4%; their agreement is not a cross-file inconsistency. Each is an internal rounding candidate.

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

> Both tables print BA n=249 and ischemic stroke 215 (86.4); the complement is 34 (13.7).

#### Evidence 1: Reported-versus-comparator

> Reported 86.4% versus 215/249.

#### Evidence 2: Calculation

> 215/249×100=86.3454%, ordinarily 86.3%; 34/249×100=13.6546%, ordinarily 13.7%; counts sum to 249.

#### Evidence 3: Alternative source-grounded interpretations

> An unstated rounding convention could produce the repeated presentation; the difference is near the ordinary rounding boundary and should not be called definitively erroneous.

### Source links

- sourceLinks 0: [DOC-001 Table 1, PDF p. 6](../../../2024/jama.2024.12829/jama_sun_2024_oi_240088_1746815064.14747.pdf#page=6)
- sourceLinks 1: [DOC-002 Table S1, PDF p. 14](../../../2024/jama.2024.12829/joi240088supp1_prod_1746815064.21247.pdf#page=14)
- evidencePaths 0: [2024/jama.2024.12829/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.12829/.ai_paper_validation/review_1_5_3/source_inventory.md)

[Original Markdown report](../../../2024/jama.2024.12829/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | 86.3% follows ordinary nearest rounding; an unspecified display convention may explain the difference. |
| broadPlanInvolved | 0 |
| category | Denominator, proportion, or total inconsistency |
| currentReportCrossDocument | 0 |
| id | C002 |
| key | 2024::jama.2024.12829::C002 |
| legacyRelationship |  |
| locations | DOC-001 Table 1, PDF p. 6; DOC-002 Table S1, PDF p. 14 |
| originalCrossDocument | 0 |
| package | jama.2024.12829 |
| planMechanism |  |
| primary | S\_W |
| rationale | Main Table1 and results-supplement TableS1 identically repeat215/249 as86.4%; their agreement is not a cross-file inconsistency. Each is an internal rounding candidate. |
| reportHref | ../../2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | The repeated BA ischemic-stroke percentage is conditionally inconsistent with ordinary nearest-one-decimal rounding. |
| submissionInvolved | 1 |
| subtype | rounding |
| suggestedDomain | statistical\_results |
| title | Balloon-angioplasty ischemic-stroke percentage is outside ordinary one-decimal rounding |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C003

**Table S4 procedure rows use 241 while the column header states 249**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.12829::C003 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-002 Table S4, PDF p. 17

### Candidate statement

> Table S4 raises a denominator-label clarity question because procedure rows use the footnoted 241 participants while the column header states 249.

### AI rationale

> Results-supplement TableS4 header249 differs from footnoted procedure-applicable241, which reproduces the percentages.

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

> The BA header is n=249; footnote a states that 241 of 249 underwent BA. Procedure rows include 182 (75.5), 214 (88.8), and 42 (17.4).

#### Evidence 1: Reported-versus-comparator

> Header 249 versus the linked footnoted procedure-applicable denominator 241.

#### Evidence 2: Calculation

> 182+48+11=241; 182/241=75.5%, 214/241=88.8%, and 42/241=17.4% at one decimal.

#### Evidence 3: Alternative source-grounded interpretations

> The header may provide randomized-arm context and the footnote may sufficiently define the 241 denominator for procedure rows. The observation is not established incorrect arithmetic.

### Source links

- sourceLinks 0: [DOC-002 Table S4, PDF p. 17](../../../2024/jama.2024.12829/joi240088supp1_prod_1746815064.21247.pdf#page=17)
- evidencePaths 0: [2024/jama.2024.12829/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.12829/.ai_paper_validation/review_1_5_3/source_inventory.md)

[Original Markdown report](../../../2024/jama.2024.12829/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | The explicit241 footnote may fully resolve the header context; retained candidate is not established bad arithmetic. |
| broadPlanInvolved | 0 |
| category | Denominator, proportion, or total inconsistency |
| currentReportCrossDocument | 0 |
| id | C003 |
| key | 2024::jama.2024.12829::C003 |
| legacyRelationship |  |
| locations | DOC-002 Table S4, PDF p. 17 |
| originalCrossDocument | 0 |
| package | jama.2024.12829 |
| planMechanism |  |
| primary | S\_W |
| rationale | Results-supplement TableS4 header249 differs from footnoted procedure-applicable241, which reproduces the percentages. |
| reportHref | ../../2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | Table S4 raises a denominator-label clarity question because procedure rows use the footnoted 241 participants while the column header states 249. |
| submissionInvolved | 1 |
| subtype | denominator\_header |
| suggestedDomain | statistical\_results |
| title | Table S4 procedure rows use 241 while the column header states 249 |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C004

**Table S6 BA 9 (3.9) conflicts with its displayed denominator 249**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.12829::C004 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-002 Table S6, PDF p. 19

### Candidate statement

> The Table S6 BA percentage does not reconcile with its displayed n=249 under ordinary rounding.

### AI rationale

> Results-supplement TableS6 gives9(3.9) under249;9/249 rounds3.6%. This percentage/header issue is separate from C016's9-versus11 event-count comparison.

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

> BA header n=249; primary-outcome cell 9 (3.9).

#### Evidence 1: Reported-versus-comparator

> Reported 3.9% versus 9/249.

#### Evidence 2: Calculation

> 9/249×100=3.6145%, ordinarily 3.6%. Diagnostically, 9/233×100=3.8627%, ordinarily 3.9%.

#### Evidence 3: Alternative source-grounded interpretations

> The 233 comparison is a diagnostic inference from a separately supplied PPS total, not a Table S6 label. An unlabelled analysis set or display rule remains possible.

### Source links

- sourceLinks 0: [DOC-002 Table S6, PDF p. 19](../../../2024/jama.2024.12829/joi240088supp1_prod_1746815064.21247.pdf#page=19)
- evidencePaths 0: [2024/jama.2024.12829/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.12829/.ai_paper_validation/review_1_5_3/source_inventory.md)

[Original Markdown report](../../../2024/jama.2024.12829/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Unlabelled PPS denominator233 could explain3.9%; it is diagnostic only. |
| broadPlanInvolved | 0 |
| category | Denominator, proportion, or total inconsistency |
| currentReportCrossDocument | 0 |
| id | C004 |
| key | 2024::jama.2024.12829::C004 |
| legacyRelationship |  |
| locations | DOC-002 Table S6, PDF p. 19 |
| originalCrossDocument | 0 |
| package | jama.2024.12829 |
| planMechanism |  |
| primary | S\_W |
| rationale | Results-supplement TableS6 gives9(3.9) under249;9/249 rounds3.6%. This percentage/header issue is separate from C016's9-versus11 event-count comparison. |
| reportHref | ../../2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C004 |
| sourceStatus | Pending Human Adjudication |
| statement | The Table S6 BA percentage does not reconcile with its displayed n=249 under ordinary rounding. |
| submissionInvolved | 1 |
| subtype | count\_percentage |
| suggestedDomain | statistical\_results |
| title | Table S6 BA 9 (3.9) conflicts with its displayed denominator 249 |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C005

**Table S7 group headers conflict with site totals and displayed site percentages**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.12829::C005 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-002 Table S7, PDF p. 20; DOC-001 Figure 1, PDF p. 5; DOC-002 Table S10, PDF p. 23

### Candidate statement

> Table S7's group headers, site totals, and displayed site percentages do not all describe one disclosed population.

### AI rationale

> Within results-supplement TableS7, headers233/238 total471 while site totals sum501 and cell percentages imply other denominators. Main Figure1 provides contextual population totals.

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

> Headers are BA/AMM 233/238; site totals are 256 and 245; cells include 4 (2.9), 19 (16.1), 7 (6.3), and 15 (11.2).

#### Evidence 1: Reported-versus-comparator

> Header total 471 versus site total 501, with cell percentages inconsistent with the headers.

#### Evidence 2: Calculation

> 233+238=471; 256+245=501. Rounded cells are diagnostically compatible with site-by-arm denominators summing to 249/252, not printed as such.

#### Evidence 3: Alternative source-grounded interpretations

> Derived site-by-arm denominators are diagnostic only. A different disclosed analysis population could explain the table if identified.

### Source links

- sourceLinks 0: [DOC-002 Table S7, PDF p. 20](../../../2024/jama.2024.12829/joi240088supp1_prod_1746815064.21247.pdf#page=20)
- sourceLinks 1: [DOC-001 Figure 1, PDF p. 5](../../../2024/jama.2024.12829/jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5)
- sourceLinks 2: [DOC-002 Table S10, PDF p. 23](../../../2024/jama.2024.12829/joi240088supp1_prod_1746815064.21247.pdf#page=23)
- evidencePaths 0: [2024/jama.2024.12829/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.12829/.ai_paper_validation/review_1_5_3/source_inventory.md)

[Original Markdown report](../../../2024/jama.2024.12829/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Main flow context is corroborative; no specific contradictory main result is the target. |
| broadPlanInvolved | 0 |
| category | Denominator, proportion, or total inconsistency |
| currentReportCrossDocument | 0 |
| id | C005 |
| key | 2024::jama.2024.12829::C005 |
| legacyRelationship |  |
| locations | DOC-002 Table S7, PDF p. 20; DOC-001 Figure 1, PDF p. 5; DOC-002 Table S10, PDF p. 23 |
| originalCrossDocument | 0 |
| package | jama.2024.12829 |
| planMechanism |  |
| primary | S\_W |
| rationale | Within results-supplement TableS7, headers233/238 total471 while site totals sum501 and cell percentages imply other denominators. Main Figure1 provides contextual population totals. |
| reportHref | ../../2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C005 |
| sourceStatus | Pending Human Adjudication |
| statement | Table S7's group headers, site totals, and displayed site percentages do not all describe one disclosed population. |
| submissionInvolved | 1 |
| subtype | denominator\_population |
| suggestedDomain | statistical\_results |
| title | Table S7 group headers conflict with site totals and displayed site percentages |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C006

**Table S8 per-protocol percentages conflict with headers 249/252**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.12829::C006 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-002 Table S8, PDF p. 21; DOC-001 Figure 1, PDF p. 5; DOC-002 Table S10, PDF p. 23

### Candidate statement

> Table S8 is labelled PPS but its printed headers conflict with the denominators that reproduce its percentages.

### AI rationale

> Results-supplement TableS8 is labelled PPS but headers249/252 conflict with its percentages and same-supplement TableS10 PPS totals233/238. Main Figure1 corroborates those PPS totals.

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

> PPS headers print 249/252; rows include 9 (3.9), 33 (13.9), 6 (2.6), and 20 (8.4).

#### Evidence 1: Reported-versus-comparator

> Displayed 249/252 headers versus supplied PPS denominators 233/238.

#### Evidence 2: Calculation

> 9/233=3.9%, 33/238=13.9%, 6/233=2.6%, and 20/238=8.4% at one decimal.

#### Evidence 3: Alternative source-grounded interpretations

> A copy-forward header is only an inferred mechanism. An outcome-specific PPS could exist but is not identified.

### Source links

- sourceLinks 0: [DOC-002 Table S8, PDF p. 21](../../../2024/jama.2024.12829/joi240088supp1_prod_1746815064.21247.pdf#page=21)
- sourceLinks 1: [DOC-001 Figure 1, PDF p. 5](../../../2024/jama.2024.12829/jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5)
- sourceLinks 2: [DOC-002 Table S10, PDF p. 23](../../../2024/jama.2024.12829/joi240088supp1_prod_1746815064.21247.pdf#page=23)
- evidencePaths 0: [2024/jama.2024.12829/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.12829/.ai_paper_validation/review_1_5_3/source_inventory.md)
- evidencePaths 1: [2024/jama.2024.12829/.ai\_paper\_validation/review\_1\_5\_3/verification/evidence\_recheck.md](../../../2024/jama.2024.12829/.ai_paper_validation/review_1_5_3/verification/evidence_recheck.md)

[Original Markdown report](../../../2024/jama.2024.12829/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Per-protocol denotes an analysis set, not a protocol document; main population totals corroborate the internal supplement mismatch. |
| broadPlanInvolved | 0 |
| category | Denominator, proportion, or total inconsistency |
| currentReportCrossDocument | 0 |
| id | C006 |
| key | 2024::jama.2024.12829::C006 |
| legacyRelationship |  |
| locations | DOC-002 Table S8, PDF p. 21; DOC-001 Figure 1, PDF p. 5; DOC-002 Table S10, PDF p. 23 |
| originalCrossDocument | 0 |
| package | jama.2024.12829 |
| planMechanism |  |
| primary | S\_W |
| rationale | Results-supplement TableS8 is labelled PPS but headers249/252 conflict with its percentages and same-supplement TableS10 PPS totals233/238. Main Figure1 corroborates those PPS totals. |
| reportHref | ../../2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C006 |
| sourceStatus | Pending Human Adjudication |
| statement | Table S8 is labelled PPS but its printed headers conflict with the denominators that reproduce its percentages. |
| submissionInvolved | 1 |
| subtype | denominator\_population |
| suggestedDomain | statistical\_results |
| title | Table S8 per-protocol percentages conflict with headers 249/252 |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C007

**Table S9 as-treated percentages conflict with headers 249/252**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.12829::C007 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-002 Table S9, PDF p. 22; DOC-002 Table S10, PDF p. 23

### Candidate statement

> Table S9 is labelled ATS but its printed headers conflict with the denominators that reproduce its primary percentages.

### AI rationale

> ATS TableS9 headers249/252 conflict with percentages reproduced by same-supplement TableS10 ATS totals247/254.

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

> ATS headers print 249/252; primary values include 11 (4.5) and 34 (13.4).

#### Evidence 1: Reported-versus-comparator

> Displayed headers 249/252 versus supplied ATS denominators 247/254.

#### Evidence 2: Calculation

> 11/247=4.5% and 34/254=13.4% at one decimal.

#### Evidence 3: Alternative source-grounded interpretations

> Copied primary headers are not directly observed; a different ATS definition remains possible if documented.

### Source links

- sourceLinks 0: [DOC-002 Table S9, PDF p. 22](../../../2024/jama.2024.12829/joi240088supp1_prod_1746815064.21247.pdf#page=22)
- sourceLinks 1: [DOC-002 Table S10, PDF p. 23](../../../2024/jama.2024.12829/joi240088supp1_prod_1746815064.21247.pdf#page=23)
- evidencePaths 0: [2024/jama.2024.12829/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.12829/.ai_paper_validation/review_1_5_3/source_inventory.md)

[Original Markdown report](../../../2024/jama.2024.12829/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Separate from C014's cell percentage, which fails even under the ATS denominator. |
| broadPlanInvolved | 0 |
| category | Denominator, proportion, or total inconsistency |
| currentReportCrossDocument | 0 |
| id | C007 |
| key | 2024::jama.2024.12829::C007 |
| legacyRelationship |  |
| locations | DOC-002 Table S9, PDF p. 22; DOC-002 Table S10, PDF p. 23 |
| originalCrossDocument | 0 |
| package | jama.2024.12829 |
| planMechanism |  |
| primary | S\_W |
| rationale | ATS TableS9 headers249/252 conflict with percentages reproduced by same-supplement TableS10 ATS totals247/254. |
| reportHref | ../../2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C007 |
| sourceStatus | Pending Human Adjudication |
| statement | Table S9 is labelled ATS but its printed headers conflict with the denominators that reproduce its primary percentages. |
| submissionInvolved | 1 |
| subtype | denominator\_population |
| suggestedDomain | statistical\_results |
| title | Table S9 as-treated percentages conflict with headers 249/252 |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C008

**Baseline stenosis categories include values outside the stated 70%-99% eligibility range**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.12829::C008 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001 eligibility, PDF p. 2; DOC-001 Figure 1, PDF p. 5; DOC-001 Table 1, PDF p. 6

### Candidate statement

> A cross-location threshold/category mismatch is present between the stated eligibility interval and four Table 1 baseline categories; measurement identity is unresolved.

### AI rationale

> Main eligibility text specifies70%-99% stenosis while its Table1 includes four participants in60%-69% or100% categories.

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

> Eligibility is 70%-99%; Table 1 includes AMM 2 at 60%-69% and one participant in each arm at 100%.

#### Evidence 1: Reported-versus-comparator

> Eligibility interval 70%-99% versus displayed analysed baseline categories outside that interval.

#### Evidence 2: Calculation

> 2+1+1=4 displayed participants are outside the inclusive 70%-99% interval.

#### Evidence 3: Alternative source-grounded interpretations

> Eligibility and table measurements may be from different times/readers or angiograms; retained protocol deviations are also possible. The sources do not establish identity conditions.

### Source links

- sourceLinks 0: [DOC-001 eligibility, PDF p. 2](../../../2024/jama.2024.12829/jama_sun_2024_oi_240088_1746815064.14747.pdf#page=2)
- sourceLinks 1: [DOC-001 Figure 1, PDF p. 5](../../../2024/jama.2024.12829/jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5)
- sourceLinks 2: [DOC-001 Table 1, PDF p. 6](../../../2024/jama.2024.12829/jama_sun_2024_oi_240088_1746815064.14747.pdf#page=6)
- evidencePaths 0: [2024/jama.2024.12829/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.12829/.ai_paper_validation/review_1_5_3/source_inventory.md)

[Original Markdown report](../../../2024/jama.2024.12829/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Measurement time/reader identity is unresolved; mention of possible protocol deviations does not make this a protocol-document comparison. |
| broadPlanInvolved | 0 |
| category | Analysis-unit or population inconsistency |
| currentReportCrossDocument | 0 |
| id | C008 |
| key | 2024::jama.2024.12829::C008 |
| legacyRelationship |  |
| locations | DOC-001 eligibility, PDF p. 2; DOC-001 Figure 1, PDF p. 5; DOC-001 Table 1, PDF p. 6 |
| originalCrossDocument | 0 |
| package | jama.2024.12829 |
| planMechanism |  |
| primary | S\_W |
| rationale | Main eligibility text specifies70%-99% stenosis while its Table1 includes four participants in60%-69% or100% categories. |
| reportHref | ../../2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C008 |
| sourceStatus | Pending Human Adjudication |
| statement | A cross-location threshold/category mismatch is present between the stated eligibility interval and four Table 1 baseline categories; measurement identity is unresolved. |
| submissionInvolved | 1 |
| subtype | eligibility\_distribution |
| suggestedDomain | statistical\_results |
| title | Baseline stenosis categories include values outside the stated 70%-99% eligibility range |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C009

**Thirty-day follow-up tolerance is plus or minus 3 days in the supplement but plus or minus 7 days elsewhere**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.12829::C009 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> DOC-002 study-design graphic, PDF p. 6; DOC-001 schedule, PDF p. 3; DOC-003 schedule, PDF p. 15

### Candidate statement

> The matched 30-day follow-up is labelled ±3 days in one supplied location and ±7 days in two others.

### AI rationale

> Non-plan study-design graphic says30±3days, whereas main schedule and supplied protocol schedule say30±7days for the matched visit.

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

> DOC-002 prints 30±3d; DOC-001 and DOC-003 print 30±7 days/30d±7d.

#### Evidence 1: Reported-versus-comparator

> ±3 versus ±7 for the matched nominal 30-day visit.

#### Evidence 2: Calculation

> 30±3 spans days 27-33 (numerical endpoint-to-endpoint width 6); 30±7 spans days 23-37 (width 14); half-widths differ by 4 days.

#### Evidence 3: Alternative source-grounded interpretations

> The graphic may depict a tighter operational contact window while the article/protocol allow a wider assessment window, but no source defines that distinction.

### Source links

- sourceLinks 0: [DOC-002 study-design graphic, PDF p. 6](../../../2024/jama.2024.12829/joi240088supp1_prod_1746815064.21247.pdf#page=6)
- sourceLinks 1: [DOC-001 schedule, PDF p. 3](../../../2024/jama.2024.12829/jama_sun_2024_oi_240088_1746815064.14747.pdf#page=3)
- sourceLinks 2: [DOC-003 schedule, PDF p. 15](../../../2024/jama.2024.12829/joi240088supp2_prod_1746815064.36071.pdf#page=15)
- evidencePaths 0: [2024/jama.2024.12829/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.12829/.ai_paper_validation/review_1_5_3/source_inventory.md)
- evidencePaths 1: [2024/jama.2024.12829/.ai\_paper\_validation/review\_1\_5\_3/verification/evidence\_recheck.md](../../../2024/jama.2024.12829/.ai_paper_validation/review_1_5_3/verification/evidence_recheck.md)

[Original Markdown report](../../../2024/jama.2024.12829/.ai_paper_validation/final_report_1_5_3.md)

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
| ambiguity | Mixed results-supplement versus plan and main-versus-supplement discrepancy; a tighter operational contact window is possible but undefined. |
| broadPlanInvolved | 1 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 1 |
| id | C009 |
| key | 2024::jama.2024.12829::C009 |
| legacyRelationship |  |
| locations | DOC-002 study-design graphic, PDF p. 6; DOC-001 schedule, PDF p. 3; DOC-003 schedule, PDF p. 15 |
| originalCrossDocument | 0 |
| package | jama.2024.12829 |
| planMechanism | endpoint\_definition\_window\_hierarchy |
| primary | P\_R |
| rationale | Non-plan study-design graphic says30±3days, whereas main schedule and supplied protocol schedule say30±7days for the matched visit. |
| reportHref | ../../2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C009 |
| sourceStatus | Pending Human Adjudication |
| statement | The matched 30-day follow-up is labelled ±3 days in one supplied location and ±7 days in two others. |
| submissionInvolved | 1 |
| subtype | visit\_window |
| suggestedDomain | protocol\_report |
| title | Thirty-day follow-up tolerance is plus or minus 3 days in the supplement but plus or minus 7 days elsewhere |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | retain |

## Candidate C010

**Protocol V2.0 gives 21-day and 14-day lower bounds for the same stroke criterion**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.12829::C010 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> DOC-003 synopsis, PDF p. 7; DOC-003 body eligibility, PDF p. 21

### Candidate statement

> Protocol V2.0 prints two different lower bounds for the matched ischemic-stroke eligibility criterion.

### AI rationale

> Within ProtocolV2.0, synopsis says ischemic stroke21-90days and body criterion says14-90days.

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

> The synopsis prints 21-90 days; the body prints 14-90 days.

#### Evidence 1: Reported-versus-comparator

> Same-version lower bound 21 versus 14 days.

#### Evidence 2: Calculation

> Lower bounds differ by 21-14=7 days.

#### Evidence 3: Alternative source-grounded interpretations

> A stale synopsis, unmarked amendment, or other production difference could explain the mismatch; the governing criterion is not established.

### Source links

- sourceLinks 0: [DOC-003 synopsis, PDF p. 7](../../../2024/jama.2024.12829/joi240088supp2_prod_1746815064.36071.pdf#page=7)
- sourceLinks 1: [DOC-003 body eligibility, PDF p. 21](../../../2024/jama.2024.12829/joi240088supp2_prod_1746815064.36071.pdf#page=21)
- evidencePaths 0: [2024/jama.2024.12829/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.12829/.ai_paper_validation/review_1_5_3/source_inventory.md)
- evidencePaths 1: [2024/jama.2024.12829/.ai\_paper\_validation/review\_1\_5\_3/verification/evidence\_recheck.md](../../../2024/jama.2024.12829/.ai_paper_validation/review_1_5_3/verification/evidence_recheck.md)

[Original Markdown report](../../../2024/jama.2024.12829/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_P |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Same-version discrepancy; possible stale synopsis or unmarked amendment, not report-versus-plan. |
| broadPlanInvolved | 1 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C010 |
| key | 2024::jama.2024.12829::C010 |
| legacyRelationship |  |
| locations | DOC-003 synopsis, PDF p. 7; DOC-003 body eligibility, PDF p. 21 |
| originalCrossDocument | 0 |
| package | jama.2024.12829 |
| planMechanism |  |
| primary | P\_P |
| rationale | Within ProtocolV2.0, synopsis says ischemic stroke21-90days and body criterion says14-90days. |
| reportHref | ../../2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C010 |
| sourceStatus | Pending Human Adjudication |
| statement | Protocol V2.0 prints two different lower bounds for the matched ischemic-stroke eligibility criterion. |
| submissionInvolved | 0 |
| subtype | eligibility\_window |
| suggestedDomain | plan\_material |
| title | Protocol V2.0 gives 21-day and 14-day lower bounds for the same stroke criterion |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C011

**BA 3-month aspirin percentage does not reconcile with count and displayed arm denominator**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.12829::C011 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-002 Table S3, PDF p. 16

### Candidate statement

> The BA three-month aspirin percentage is inconsistent with the displayed arm denominator under ordinary nearest-one-decimal rounding.

### AI rationale

> Results-supplement TableS3 gives234/249 as93.9% while ordinary nearest rounding gives94.0%.

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

> BA header n=249; three-month aspirin 234 (93.9).

#### Evidence 1: Reported-versus-comparator

> Reported 93.9% versus 234/249.

#### Evidence 2: Calculation

> 234/249×100=93.9759%, ordinarily 94.0%; truncation would display 93.9%.

#### Evidence 3: Alternative source-grounded interpretations

> Truncation, weighting, an undisclosed evaluated denominator, or missingness handling could explain the presentation. No alternative integer denominator no larger than 249 is identified as the answer.

### Source links

- sourceLinks 0: [DOC-002 Table S3, PDF p. 16](../../../2024/jama.2024.12829/joi240088supp1_prod_1746815064.21247.pdf#page=16)
- evidencePaths 0: [2024/jama.2024.12829/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.12829/.ai_paper_validation/review_1_5_3/source_inventory.md)

[Original Markdown report](../../../2024/jama.2024.12829/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Truncation could explain the display; evaluated denominator is not supplied. |
| broadPlanInvolved | 0 |
| category | Denominator, proportion, or total inconsistency |
| currentReportCrossDocument | 0 |
| id | C011 |
| key | 2024::jama.2024.12829::C011 |
| legacyRelationship |  |
| locations | DOC-002 Table S3, PDF p. 16 |
| originalCrossDocument | 0 |
| package | jama.2024.12829 |
| planMechanism |  |
| primary | S\_W |
| rationale | Results-supplement TableS3 gives234/249 as93.9% while ordinary nearest rounding gives94.0%. |
| reportHref | ../../2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C011 |
| sourceStatus | Pending Human Adjudication |
| statement | The BA three-month aspirin percentage is inconsistent with the displayed arm denominator under ordinary nearest-one-decimal rounding. |
| submissionInvolved | 1 |
| subtype | rounding |
| suggestedDomain | statistical\_results |
| title | BA 3-month aspirin percentage does not reconcile with count and displayed arm denominator |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C012

**Figure S1 repeats “2nd meeting” for three chronologically distinct meetings**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.12829::C012 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-002 Figure S1, PDF p. 10

### Candidate statement

> Figure S1 repeats the ordinal 2nd meeting for three different dates within the displayed review process.

### AI rationale

> Non-plan FigureS1 repeats2nd meeting for three distinct dates within its own chronology.

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

> The figure labels 1st (2021/05/30), then 2nd (2021/11/20, 2022/09/07, and 2023/04/10).

#### Evidence 1: Reported-versus-comparator

> Four chronologically distinct dated boxes versus two unique ordinal labels.

#### Evidence 2: Calculation

> Four dated boxes contain only two unique ordinals; 2nd meeting appears three times.

#### Evidence 3: Alternative source-grounded interpretations

> An unprinted review-cycle convention could use 2nd repeatedly. The figure does not label such a cycle; its case-count arithmetic separately reconciles.

### Source links

- sourceLinks 0: [DOC-002 Figure S1, PDF p. 10](../../../2024/jama.2024.12829/joi240088supp1_prod_1746815064.21247.pdf#page=10)
- evidencePaths 0: [2024/jama.2024.12829/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.12829/.ai_paper_validation/review_1_5_3/source_inventory.md)

[Original Markdown report](../../../2024/jama.2024.12829/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | A repeated review-cycle convention is possible but unstated. |
| broadPlanInvolved | 0 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C012 |
| key | 2024::jama.2024.12829::C012 |
| legacyRelationship |  |
| locations | DOC-002 Figure S1, PDF p. 10 |
| originalCrossDocument | 0 |
| package | jama.2024.12829 |
| planMechanism |  |
| primary | S\_W |
| rationale | Non-plan FigureS1 repeats2nd meeting for three distinct dates within its own chronology. |
| reportHref | ../../2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C012 |
| sourceStatus | Pending Human Adjudication |
| statement | Figure S1 repeats the ordinal 2nd meeting for three different dates within the displayed review process. |
| submissionInvolved | 1 |
| subtype | timeline\_ordinal |
| suggestedDomain | report\_internal\_inconsistency |
| title | Figure S1 repeats “2nd meeting” for three chronologically distinct meetings |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C013

**Recurring-visit sentence ambiguously repeats visit numbers 9 and 11**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.12829::C013 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> DOC-003 Protocol V2.0 paragraph, PDF p. 35; DOC-003 Protocol V2.3 paragraph, PDF p. 96; DOC-003 schedule, PDF p. 15

### Candidate statement

> The identical recurring-visit sentence is ambiguous between a four-visit sequence with a face-to-face subset and a six-token sequence because it repeats visits 9 and 11.

### AI rationale

> The same protocol bundle repeats visit9 and11 in a six-token sentence in bothV2.0 andV2.3, against its four-visit8-11 schedule.

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

> V2.0 p. 35 and V2.3 p. 96 each print visit 8, visit 9, visit 10, visit 11, visit 9, and visit 11 require patients to undergo face-to-face follow-up; the schedule identifies visits 8-11 as four recurring visits.

#### Evidence 1: Reported-versus-comparator

> Six visit tokens 8,9,10,11,9,11 versus the four-visit schedule 8-11.

#### Evidence 2: Calculation

> Six tokens contain four unique identifiers; 9 and 11 each occur twice.

#### Evidence 3: Alternative source-grounded interpretations

> The sentence plausibly lists visits 8-11 and then names visits 9 and 11 as the face-to-face subset, with missing clarifying syntax. A six-visit sequence is not established.

### Source links

- sourceLinks 0: [DOC-003 Protocol V2.0 paragraph, PDF p. 35](../../../2024/jama.2024.12829/joi240088supp2_prod_1746815064.36071.pdf#page=35)
- sourceLinks 1: [DOC-003 Protocol V2.3 paragraph, PDF p. 96](../../../2024/jama.2024.12829/joi240088supp2_prod_1746815064.36071.pdf#page=96)
- sourceLinks 2: [DOC-003 schedule, PDF p. 15](../../../2024/jama.2024.12829/joi240088supp2_prod_1746815064.36071.pdf#page=15)
- evidencePaths 0: [2024/jama.2024.12829/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.12829/.ai_paper_validation/review_1_5_3/source_inventory.md)
- evidencePaths 1: [2024/jama.2024.12829/.ai\_paper\_validation/review\_1\_5\_3/verification/evidence\_recheck.md](../../../2024/jama.2024.12829/.ai_paper_validation/review_1_5_3/verification/evidence_recheck.md)

[Original Markdown report](../../../2024/jama.2024.12829/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_P |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | The sentence may specify face-to-face subset9/11 rather than six successive visits; two versioned repetitions remain one retained candidate. |
| broadPlanInvolved | 1 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C013 |
| key | 2024::jama.2024.12829::C013 |
| legacyRelationship |  |
| locations | DOC-003 Protocol V2.0 paragraph, PDF p. 35; DOC-003 Protocol V2.3 paragraph, PDF p. 96; DOC-003 schedule, PDF p. 15 |
| originalCrossDocument | 0 |
| package | jama.2024.12829 |
| planMechanism |  |
| primary | P\_P |
| rationale | The same protocol bundle repeats visit9 and11 in a six-token sentence in bothV2.0 andV2.3, against its four-visit8-11 schedule. |
| reportHref | ../../2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C013 |
| sourceStatus | Pending Human Adjudication |
| statement | The identical recurring-visit sentence is ambiguous between a four-visit sequence with a face-to-face subset and a six-token sequence because it repeats visits 9 and 11. |
| submissionInvolved | 0 |
| subtype | visit\_sequence |
| suggestedDomain | plan\_material |
| title | Recurring-visit sentence ambiguously repeats visit numbers 9 and 11 |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C014

**Table S9 BA 8 (3.3) does not round from either supplied ATS or displayed denominator**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.12829::C014 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-002 Table S9, PDF p. 22; DOC-002 Table S10, PDF p. 23

### Candidate statement

> The Table S9 BA 8 (3.3) cell does not round to 3.3% from either the displayed or supplied ATS denominator.

### AI rationale

> Results-supplement TableS9 gives8(3.3), but both displayed249 and same-supplement ATS247 denominators produce3.2%.

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

> Table S9 prints BA 8 (3.3) and header 249; Table S10 supplies ATS N=247.

#### Evidence 1: Reported-versus-comparator

> Reported 3.3% versus both 8/249 and 8/247.

#### Evidence 2: Calculation

> 8/249×100=3.2129% and 8/247×100=3.2389%; both ordinarily round to 3.2%.

#### Evidence 3: Alternative source-grounded interpretations

> An unprinted outcome-specific risk set or nonstandard display rule could explain 3.3%; neither is supplied.

### Source links

- sourceLinks 0: [DOC-002 Table S9, PDF p. 22](../../../2024/jama.2024.12829/joi240088supp1_prod_1746815064.21247.pdf#page=22)
- sourceLinks 1: [DOC-002 Table S10, PDF p. 23](../../../2024/jama.2024.12829/joi240088supp1_prod_1746815064.21247.pdf#page=23)
- evidencePaths 0: [2024/jama.2024.12829/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.12829/.ai_paper_validation/review_1_5_3/source_inventory.md)

[Original Markdown report](../../../2024/jama.2024.12829/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Distinct from C007: changing the ATS header alone does not resolve this cell. |
| broadPlanInvolved | 0 |
| category | Numeric or arithmetic inconsistency |
| currentReportCrossDocument | 0 |
| id | C014 |
| key | 2024::jama.2024.12829::C014 |
| legacyRelationship |  |
| locations | DOC-002 Table S9, PDF p. 22; DOC-002 Table S10, PDF p. 23 |
| originalCrossDocument | 0 |
| package | jama.2024.12829 |
| planMechanism |  |
| primary | S\_W |
| rationale | Results-supplement TableS9 gives8(3.3), but both displayed249 and same-supplement ATS247 denominators produce3.2%. |
| reportHref | ../../2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C014 |
| sourceStatus | Pending Human Adjudication |
| statement | The Table S9 BA 8 (3.3) cell does not round to 3.3% from either the displayed or supplied ATS denominator. |
| submissionInvolved | 1 |
| subtype | rounding |
| suggestedDomain | statistical\_results |
| title | Table S9 BA 8 (3.3) does not round from either supplied ATS or displayed denominator |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C015

**Narrative assigns all 11 pre-analysis exclusions to consent withdrawal while Figure 1 assigns only 10**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.12829::C015 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-001 narrative, PDF p. 4; DOC-001 Figure 1, PDF p. 5

### Candidate statement

> The narrative and Figure 1 reconcile to the same total removals but assign different reason categories to the 11 pre-analysis exclusions.

### AI rationale

> Main narrative attributes all11 exclusions to consent withdrawal; its Figure1 assigns10 to withdrawal and1 to erroneous randomization.

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

> Narrative: 11 excluded due to consent withdrawal. Figure: BA 7 plus AMM 3 consent withdrawals, plus 1 erroneous randomization assignment.

#### Evidence 1: Reported-versus-comparator

> Narrative reason category for 11 versus Figure reason categories totaling 10+1.

#### Evidence 2: Calculation

> 7+3=10 consent withdrawals; 10+1=11 total removals; the 501-person analysed total reconciles.

#### Evidence 3: Alternative source-grounded interpretations

> The narrative may use umbrella shorthand, or the erroneously assigned participant may also have withdrawn consent; Figure 1 presents a separate reason.

### Source links

- sourceLinks 0: [DOC-001 narrative, PDF p. 4](../../../2024/jama.2024.12829/jama_sun_2024_oi_240088_1746815064.14747.pdf#page=4)
- sourceLinks 1: [DOC-001 Figure 1, PDF p. 5](../../../2024/jama.2024.12829/jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5)
- evidencePaths 0: [2024/jama.2024.12829/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.12829/.ai_paper_validation/review_1_5_3/source_inventory.md)

[Original Markdown report](../../../2024/jama.2024.12829/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Original cross-document category actually describes two locations in one article; dual reason coding remains possible. |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 0 |
| id | C015 |
| key | 2024::jama.2024.12829::C015 |
| legacyRelationship |  |
| locations | DOC-001 narrative, PDF p. 4; DOC-001 Figure 1, PDF p. 5 |
| originalCrossDocument | 1 |
| package | jama.2024.12829 |
| planMechanism |  |
| primary | S\_W |
| rationale | Main narrative attributes all11 exclusions to consent withdrawal; its Figure1 assigns10 to withdrawal and1 to erroneous randomization. |
| reportHref | ../../2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C015 |
| sourceStatus | Pending Human Adjudication |
| statement | The narrative and Figure 1 reconcile to the same total removals but assign different reason categories to the 11 pre-analysis exclusions. |
| submissionInvolved | 1 |
| subtype | flow\_reason\_category |
| suggestedDomain | report\_internal\_inconsistency |
| title | Narrative assigns all 11 pre-analysis exclusions to consent withdrawal while Figure 1 assigns only 10 |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C016

**Table S6 BA event count 9 conflicts with the matched primary-analysis count 11**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.12829::C016 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-001 primary narrative, PDF p. 5; DOC-001 Table 2, PDF p. 8; DOC-002 Table S6, PDF p. 19

### Candidate statement

> Table S6 prints a BA count of 9 for a matched primary endpoint and n=249 header where the main narrative and Table 2 print 11; this is distinct from C004.

### AI rationale

> Main primary endpoint narrative/Table2 giveBA11 events, whereas matched non-plan TableS6 prints9 under the same249 header and endpoint wording.

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

> Main result: BA 11 (4.4) and AMM 34 (13.5) under 249/252. Centre-adjusted Table S6 has the matched composite wording and headers but prints BA 9 (3.9) and AMM 34 (13.5).

#### Evidence 1: Reported-versus-comparator

> Table S6 BA count 9 versus matched main BA count 11.

#### Evidence 2: Calculation

> 11-9=2; AMM remains 34. Table S10's related no-revascularization composite has BA 9, but Table S6 retains revascularization in its label.

#### Evidence 3: Alternative source-grounded interpretations

> An unlabelled alternative set or carryover of the Table S10 no-revascularization count could explain the entry. Centre adjustment alone does not explain two fewer observed events.

### Source links

- sourceLinks 0: [DOC-001 primary narrative, PDF p. 5](../../../2024/jama.2024.12829/jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5)
- sourceLinks 1: [DOC-001 Table 2, PDF p. 8](../../../2024/jama.2024.12829/jama_sun_2024_oi_240088_1746815064.14747.pdf#page=8)
- sourceLinks 2: [DOC-002 Table S6, PDF p. 19](../../../2024/jama.2024.12829/joi240088supp1_prod_1746815064.21247.pdf#page=19)
- evidencePaths 0: [2024/jama.2024.12829/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.12829/.ai_paper_validation/review_1_5_3/source_inventory.md)

[Original Markdown report](../../../2024/jama.2024.12829/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_C |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Different from C004's arithmetic defect; unknown endpoint/population mapping could explain the count difference. |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C016 |
| key | 2024::jama.2024.12829::C016 |
| legacyRelationship |  |
| locations | DOC-001 primary narrative, PDF p. 5; DOC-001 Table 2, PDF p. 8; DOC-002 Table S6, PDF p. 19 |
| originalCrossDocument | 1 |
| package | jama.2024.12829 |
| planMechanism |  |
| primary | S\_C |
| rationale | Main primary endpoint narrative/Table2 giveBA11 events, whereas matched non-plan TableS6 prints9 under the same249 header and endpoint wording. |
| reportHref | ../../2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C016 |
| sourceStatus | Pending Human Adjudication |
| statement | Table S6 prints a BA count of 9 for a matched primary endpoint and n=249 header where the main narrative and Table 2 print 11; this is distinct from C004. |
| submissionInvolved | 1 |
| subtype | event\_count\_repeat |
| suggestedDomain | report\_internal\_inconsistency |
| title | Table S6 BA event count 9 conflicts with the matched primary-analysis count 11 |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C017

**One-year incidence-difference point estimate lies outside its confidence interval**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.12829::C017 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001 Table 2, PDF p. 8

### Candidate statement

> The printed one-year incidence-difference point estimate is not contained in its paired printed confidence interval.

### AI rationale

> Main Table2 incidence difference-0.4 lies outside its printed95%CI\[-2.4,-1.7\].

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

> For stroke outside the qualifying-artery territory within one year: BA 3 (1.2), AMM 4 (1.6), incidence difference −0.4% (95% CI, −2.4 to −1.7).

#### Evidence 1: Reported-versus-comparator

> Point estimate −0.4% versus interval \[−2.4%, −1.7%\].

#### Evidence 2: Calculation

> −0.4 is outside \[−2.4,−1.7\]; (3/249−4/252)×100=−0.3825 percentage points, which rounds to −0.4%.

#### Evidence 3: Alternative source-grounded interpretations

> A confidence-limit sign/value may be transcribed, or point and interval may use undisclosed different estimands/methods. The exact CI method is not supplied.

### Source links

- sourceLinks 0: [DOC-001 Table 2, PDF p. 8](../../../2024/jama.2024.12829/jama_sun_2024_oi_240088_1746815064.14747.pdf#page=8)
- evidencePaths 0: [2024/jama.2024.12829/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.12829/.ai_paper_validation/review_1_5_3/source_inventory.md)

[Original Markdown report](../../../2024/jama.2024.12829/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | The interval construction or a mismatched estimand is not supplied. |
| broadPlanInvolved | 0 |
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 0 |
| id | C017 |
| key | 2024::jama.2024.12829::C017 |
| legacyRelationship |  |
| locations | DOC-001 Table 2, PDF p. 8 |
| originalCrossDocument | 0 |
| package | jama.2024.12829 |
| planMechanism |  |
| primary | S\_W |
| rationale | Main Table2 incidence difference-0.4 lies outside its printed95%CI\[-2.4,-1.7\]. |
| reportHref | ../../2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.12829/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C017 |
| sourceStatus | Pending Human Adjudication |
| statement | The printed one-year incidence-difference point estimate is not contained in its paired printed confidence interval. |
| submissionInvolved | 1 |
| subtype | point\_interval\_containment |
| suggestedDomain | statistical\_results |
| title | One-year incidence-difference point estimate lies outside its confidence interval |
| year | 2024 |
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
