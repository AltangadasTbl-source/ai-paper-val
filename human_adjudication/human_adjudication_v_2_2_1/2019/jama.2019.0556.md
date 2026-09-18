# jama.2019.0556

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2019 |
| Paper | jama.2019.0556 |
| Candidates | 9 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2019/jama.2019.0556/)

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

- [C001](#candidate-c001) — Table 2 footnote duplicates the supplements-without-therapy label (S_W)
- [C002](#candidate-c002) — Supplement-adherence cutoff changes from inclusive to strict wording (S_C)
- [C003](#candidate-c003) — eAppendix 8 footnote markers point to unrelated adherence rows (S_W)
- [C004](#candidate-c004) — eAppendix 10 prints a literal P value of zero (S_W)
- [C005](#candidate-c005) — Main-article sample-size total conflicts with four stated cell counts (S_W)
- [C006](#candidate-c006) — Protocol calls a 30% versus 15% contrast a 25% difference (P_P)
- [C007](#candidate-c007) — Protocol and publication state different sample-size assumptions (P_R)
- [C008](#candidate-c008) — Protocol uses incompatible DSM editions for the primary endpoint (P_P)
- [C009](#candidate-c009) — Analysis-plan significance threshold lacks a comparison operator (P_P)

## Candidate C001

**Table 2 footnote duplicates the supplements-without-therapy label**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.0556::C001 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-001 Table 2 — PDF p. 6; Figure 1 — PDF p. 3; Results — PDF p. 7.

### Candidate statement

> Table 2 footnote d assigns both event components to supplements without therapy, although the second component is elsewhere identified as supplements with therapy.

### AI rationale

> Main Table 2 calls both 32/256 and 22/256 supplements without therapy, whereas its other footnote and Results identify 22/256 as supplements with therapy. The conflicting arm labels are within the article.

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

> Footnote d prints 32/256 (12.5%) and 22/256 (8.6%) both as “supplements without therapy.” Footnote f and Results identify 22/256 (8.6%) as supplements with therapy.

#### Evidence 1: Reported-versus-comparator

> Repeated “without therapy” versus the Figure 1 allocation/Results and footnote-f “with therapy” label for 22/256.

#### Evidence 2: Calculation

> 32+22=54 events and 256+256=512; 22/256=8.59375%, rounded 8.6%. The other partition is 25+32=57 without therapy and 26+22=48 with therapy.

#### Evidence 3: Alternative source-grounded interpretations

> Counts, percentages, total, OR, CI, and P value reconcile; the problem may be confined to one footnote label.

### Source links

- sourceLinks 0: [DOC-001 Table 2 — PDF p. 6](../../../2019/jama.2019.0556/jama_bot_2019_oi_190007.pdf#page=6)
- sourceLinks 1: [Figure 1 — PDF p. 3](../../../2019/jama.2019.0556/jama_bot_2019_oi_190007.pdf#page=3)
- sourceLinks 2: [Results — PDF p. 7](../../../2019/jama.2019.0556/jama_bot_2019_oi_190007.pdf#page=7)
- evidencePaths 0: [2019/jama.2019.0556/.ai\_paper\_validation/review\_1\_4\_1/source\_inventory.md](../../../2019/jama.2019.0556/.ai_paper_validation/review_1_4_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.0556/.ai\_paper\_validation/review\_1\_4\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.0556/.ai_paper_validation/review_1_4_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2019/jama.2019.0556/.ai_paper_validation/final_report_1_4_1.md)

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
| key | 2019::jama.2019.0556::C001 |
| legacyRelationship |  |
| locations | DOC-001 Table 2 — PDF p. 6; Figure 1 — PDF p. 3; Results — PDF p. 7. |
| originalCrossDocument | 0 |
| package | jama.2019.0556 |
| planMechanism |  |
| primary | S\_W |
| rationale | Main Table 2 calls both 32/256 and 22/256 supplements without therapy, whereas its other footnote and Results identify 22/256 as supplements with therapy. The conflicting arm labels are within the article. |
| reportHref | ../../2019/jama.2019.0556/.ai\_paper\_validation/final\_report\_1\_4\_1.html |
| reportPath | 2019/jama.2019.0556/.ai\_paper\_validation/final\_report\_1\_4\_1.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | Table 2 footnote d assigns both event components to supplements without therapy, although the second component is elsewhere identified as supplements with therapy. |
| submissionInvolved | 1 |
| subtype | arm\_label |
| suggestedDomain | report\_internal\_inconsistency |
| title | Table 2 footnote duplicates the supplements-without-therapy label |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C002

**Supplement-adherence cutoff changes from inclusive to strict wording**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.0556::C002 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-001 Methods — PDF p. 4; Results — PDF p. 6; DOC-004 eAppendix 8 — PDF p. 16; eAppendix 12 — PDF p. 22.

### Candidate statement

> The predefined and supplement cutoff is \>=70%, whereas Results describes adherence as “more than 70%.”

### AI rationale

> The main Results strict \>70% adherence wording conflicts with both main Methods and the results supplement eAppendices 8/12 inclusive \>=70% definition. The explicitly matched main/supplement cutoff comparison is substantive; there is also a within-main wording mismatch. The word predefined does not establish a protocol/SAP comparator.

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

> Methods/eAppendices print \>=70%; Results says 77% had adherence “more than 70%.”

#### Evidence 1: Reported-versus-comparator

> Strict \>70% prose versus inclusive \>=70% operational/table wording.

#### Evidence 2: Calculation

> eAppendix 8 pill-weight multinutrient counts are 135+134+126+120=515; 515/666=77.3%, compatible with the rounded 77%. \>=70% includes exactly 70%; \>70% does not.

#### Evidence 3: Alternative source-grounded interpretations

> Results may use informal prose for the inclusive criterion and no participant may lie exactly at 70%.

### Source links

- sourceLinks 0: [DOC-001 Methods — PDF p. 4](../../../2019/jama.2019.0556/jama_bot_2019_oi_190007.pdf#page=4)
- sourceLinks 1: [Results — PDF p. 6](../../../2019/jama.2019.0556/jama_bot_2019_oi_190007.pdf#page=6)
- sourceLinks 2: [DOC-004 eAppendix 8 — PDF p. 16](../../../2019/jama.2019.0556/joi190007supp3_prod.pdf#page=16)
- sourceLinks 3: [eAppendix 12 — PDF p. 22](../../../2019/jama.2019.0556/joi190007supp3_prod.pdf#page=22)
- evidencePaths 0: [2019/jama.2019.0556/.ai\_paper\_validation/review\_1\_4\_1/source\_inventory.md](../../../2019/jama.2019.0556/.ai_paper_validation/review_1_4_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.0556/.ai\_paper\_validation/review\_1\_4\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.0556/.ai_paper_validation/review_1_4_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2019/jama.2019.0556/.ai_paper_validation/final_report_1_4_1.md)

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
| ambiguity | Mixed main-versus-results-supplement and within-main relation. Results may be informal prose and there may be no observations exactly at 70%. |
| broadPlanInvolved | 0 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 1 |
| id | C002 |
| key | 2019::jama.2019.0556::C002 |
| legacyRelationship |  |
| locations | DOC-001 Methods — PDF p. 4; Results — PDF p. 6; DOC-004 eAppendix 8 — PDF p. 16; eAppendix 12 — PDF p. 22. |
| originalCrossDocument | 0 |
| package | jama.2019.0556 |
| planMechanism |  |
| primary | S\_C |
| rationale | The main Results strict \>70% adherence wording conflicts with both main Methods and the results supplement eAppendices 8/12 inclusive \>=70% definition. The explicitly matched main/supplement cutoff comparison is substantive; there is also a within-main wording mismatch. The word predefined does not establish a protocol/SAP comparator. |
| reportHref | ../../2019/jama.2019.0556/.ai\_paper\_validation/final\_report\_1\_4\_1.html |
| reportPath | 2019/jama.2019.0556/.ai\_paper\_validation/final\_report\_1\_4\_1.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | The predefined and supplement cutoff is \>=70%, whereas Results describes adherence as “more than 70%.” |
| submissionInvolved | 1 |
| subtype | threshold\_operator |
| suggestedDomain | report\_internal\_inconsistency |
| title | Supplement-adherence cutoff changes from inclusive to strict wording |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C003

**eAppendix 8 footnote markers point to unrelated adherence rows**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.0556::C003 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-004 eAppendix 8 — PDF p. 16.

### Candidate statement

> Visible asterisks attach to four adherence rows but the corresponding note defines Morisky score; the Morisky row is unmarked and the kappa note has no visible double-marker target.

### AI rationale

> Results-supplement eAppendix 8 assigns asterisks on adherence rows to a Morisky note and leaves the kappa note without a double-marker target, all on one supplement page.

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

> Four \>=70% rows carry \*; the \* note defines average Morisky score. The Morisky row has no marker. The note gives kappas 0.73/0.70 but no row visibly carries .

#### Evidence 1: Reported-versus-comparator

> Marker placements versus the content and apparent targets of the two notes.

#### Evidence 2: Calculation

> Logical reproduction: four visible \* targets map to the sole Morisky note; zero visible targets map to the kappa note; no arithmetic applies.

#### Evidence 3: Alternative source-grounded interpretations

> Production may have shifted markers; the intended corrected arrangement cannot be determined from the PDF.

### Source links

- sourceLinks 0: [DOC-004 eAppendix 8 — PDF p. 16](../../../2019/jama.2019.0556/joi190007supp3_prod.pdf#page=16)
- evidencePaths 0: [2019/jama.2019.0556/.ai\_paper\_validation/review\_1\_4\_1/source\_inventory.md](../../../2019/jama.2019.0556/.ai_paper_validation/review_1_4_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.0556/.ai\_paper\_validation/review\_1\_4\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.0556/.ai_paper_validation/review_1_4_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2019/jama.2019.0556/.ai_paper_validation/final_report_1_4_1.md)

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
| key | 2019::jama.2019.0556::C003 |
| legacyRelationship |  |
| locations | DOC-004 eAppendix 8 — PDF p. 16. |
| originalCrossDocument | 0 |
| package | jama.2019.0556 |
| planMechanism |  |
| primary | S\_W |
| rationale | Results-supplement eAppendix 8 assigns asterisks on adherence rows to a Morisky note and leaves the kappa note without a double-marker target, all on one supplement page. |
| reportHref | ../../2019/jama.2019.0556/.ai\_paper\_validation/final\_report\_1\_4\_1.html |
| reportPath | 2019/jama.2019.0556/.ai\_paper\_validation/final\_report\_1\_4\_1.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | Visible asterisks attach to four adherence rows but the corresponding note defines Morisky score; the Morisky row is unmarked and the kappa note has no visible double-marker target. |
| submissionInvolved | 1 |
| subtype | footnote\_mapping |
| suggestedDomain | report\_internal\_inconsistency |
| title | eAppendix 8 footnote markers point to unrelated adherence rows |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C004

**eAppendix 10 prints a literal P value of zero**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.0556::C004 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-004 eAppendix 10B — PDF p. 19.

### Candidate statement

> The baseline GAD-7 row displays p=0 without threshold notation or a rounding convention.

### AI rationale

> The results supplement displays literal p=0 beside a nonzero coefficient and interval in its own eAppendix 10B. This is an internal statistical-display concern, with no competing protocol statement.

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

> The row prints B=0.464, 95% CI 0.409 to 0.52, and p=0.

#### Evidence 1: Reported-versus-comparator

> Literal zero P field versus the row’s positive coefficient/wholly positive interval; no independent exact P occurrence is supplied.

#### Evidence 2: Calculation

> Diagnostic only: SE approximately (0.520-0.409)/(2x1.96)=0.0283; z approximately 0.464/0.0283=16.4, consistent with a very small positive two-sided tail probability, not an exact recovered P value.

#### Evidence 3: Alternative source-grounded interpretations

> 0 may be fixed-precision software/export rendering of a very small positive P value.

### Source links

- sourceLinks 0: [DOC-004 eAppendix 10B — PDF p. 19](../../../2019/jama.2019.0556/joi190007supp3_prod.pdf#page=19)
- evidencePaths 0: [2019/jama.2019.0556/.ai\_paper\_validation/review\_1\_4\_1/source\_inventory.md](../../../2019/jama.2019.0556/.ai_paper_validation/review_1_4_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.0556/.ai\_paper\_validation/review\_1\_4\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.0556/.ai_paper_validation/review_1_4_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2019/jama.2019.0556/.ai_paper_validation/final_report_1_4_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Zero may be fixed-precision rendering of a small positive P value; exact inferential implementation and display convention are absent. |
| broadPlanInvolved | 0 |
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 0 |
| id | C004 |
| key | 2019::jama.2019.0556::C004 |
| legacyRelationship |  |
| locations | DOC-004 eAppendix 10B — PDF p. 19. |
| originalCrossDocument | 0 |
| package | jama.2019.0556 |
| planMechanism |  |
| primary | S\_W |
| rationale | The results supplement displays literal p=0 beside a nonzero coefficient and interval in its own eAppendix 10B. This is an internal statistical-display concern, with no competing protocol statement. |
| reportHref | ../../2019/jama.2019.0556/.ai\_paper\_validation/final\_report\_1\_4\_1.html |
| reportPath | 2019/jama.2019.0556/.ai\_paper\_validation/final\_report\_1\_4\_1.md |
| sourceId | C004 |
| sourceStatus | Pending Human Adjudication |
| statement | The baseline GAD-7 row displays p=0 without threshold notation or a rounding convention. |
| submissionInvolved | 1 |
| subtype | p\_value\_display |
| suggestedDomain | statistical\_results |
| title | eAppendix 10 prints a literal P value of zero |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C005

**Main-article sample-size total conflicts with four stated cell counts**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.0556::C005 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001 Sample Size — PDF p. 4.

### Candidate statement

> The article says 392 participants were needed while parenthetically stating 196 in each of four combinations.

### AI rationale

> The article calls 392 the required sample while saying 196 in each of four combinations (784). This is internal sample-size arithmetic, distinct from C007 comparing planning assumptions across documents.

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

> It prints “392 participants (196 in each of the 4 possible intervention combinations)” and then 22% attrition with 250 per intervention combination.

#### Evidence 1: Reported-versus-comparator

> Reported total 392 versus four stated cells of 196; later four cells of 250 provide an internal comparator.

#### Evidence 2: Calculation

> 4x196=784, not 392; 392/196=2. Conversely, 4x250=1000, consistent with the later per-combination statement.

#### Evidence 3: Alternative source-grounded interpretations

> 392 may be a marginal two-level factorial contrast (196+196), although the sentence says 196 in each of four combinations.

### Source links

- sourceLinks 0: [DOC-001 Sample Size — PDF p. 4](../../../2019/jama.2019.0556/jama_bot_2019_oi_190007.pdf#page=4)
- evidencePaths 0: [2019/jama.2019.0556/.ai\_paper\_validation/review\_1\_4\_1/source\_inventory.md](../../../2019/jama.2019.0556/.ai_paper_validation/review_1_4_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.0556/.ai\_paper\_validation/review\_1\_4\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.0556/.ai_paper_validation/review_1_4_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2019/jama.2019.0556/.ai_paper_validation/final_report_1_4_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | 392 could describe a marginal factorial quantity, but the sentence does not specify that unit. |
| broadPlanInvolved | 0 |
| category | Numeric or arithmetic inconsistency |
| currentReportCrossDocument | 0 |
| id | C005 |
| key | 2019::jama.2019.0556::C005 |
| legacyRelationship |  |
| locations | DOC-001 Sample Size — PDF p. 4. |
| originalCrossDocument | 0 |
| package | jama.2019.0556 |
| planMechanism |  |
| primary | S\_W |
| rationale | The article calls 392 the required sample while saying 196 in each of four combinations (784). This is internal sample-size arithmetic, distinct from C007 comparing planning assumptions across documents. |
| reportHref | ../../2019/jama.2019.0556/.ai\_paper\_validation/final\_report\_1\_4\_1.html |
| reportPath | 2019/jama.2019.0556/.ai\_paper\_validation/final\_report\_1\_4\_1.md |
| sourceId | C005 |
| sourceStatus | Pending Human Adjudication |
| statement | The article says 392 participants were needed while parenthetically stating 196 in each of four combinations. |
| submissionInvolved | 1 |
| subtype | sample\_size\_arithmetic |
| suggestedDomain | statistical\_results |
| title | Main-article sample-size total conflicts with four stated cell counts |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C006

**Protocol calls a 30% versus 15% contrast a 25% difference**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.0556::C006 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> DOC-002 Sample Size — PDF p. 16.

### Candidate statement

> The protocol’s stated 25% difference does not reconcile with its displayed 30% control and 15% intervention incidences under ordinary absolute or relative metrics.

### AI rationale

> One protocol paragraph calls 30% versus 15% incidence a 25% difference; the usual absolute and relative differences are 15 points and 50%. Both incompatible quantities are inside the protocol.

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

> The protocol prints “difference of 25%,” followed by 30% control and 15% intervention one-year incidence.

#### Evidence 1: Reported-versus-comparator

> 25% wording versus the two printed incidences.

#### Evidence 2: Calculation

> 30%-15%=15 percentage points; (30%-15%)/30%=50%; risk ratio=15%/30%=0.50. None equals 25%.

#### Evidence 3: Alternative source-grounded interpretations

> The 25% may refer to an unstated calculation parameter or drafting carryover.

### Source links

- sourceLinks 0: [DOC-002 Sample Size — PDF p. 16](../../../2019/jama.2019.0556/joi190007supp1_prod.pdf#page=16)
- evidencePaths 0: [2019/jama.2019.0556/.ai\_paper\_validation/review\_1\_4\_1/source\_inventory.md](../../../2019/jama.2019.0556/.ai_paper_validation/review_1_4_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.0556/.ai\_paper\_validation/review\_1\_4\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.0556/.ai_paper_validation/review_1_4_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2019/jama.2019.0556/.ai_paper_validation/final_report_1_4_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_P |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | The intended metric for 25% is not defined; C007 compares different documents and is not an exact duplicate. |
| broadPlanInvolved | 1 |
| category | Numeric or arithmetic inconsistency |
| currentReportCrossDocument | 0 |
| id | C006 |
| key | 2019::jama.2019.0556::C006 |
| legacyRelationship |  |
| locations | DOC-002 Sample Size — PDF p. 16. |
| originalCrossDocument | 0 |
| package | jama.2019.0556 |
| planMechanism |  |
| primary | P\_P |
| rationale | One protocol paragraph calls 30% versus 15% incidence a 25% difference; the usual absolute and relative differences are 15 points and 50%. Both incompatible quantities are inside the protocol. |
| reportHref | ../../2019/jama.2019.0556/.ai\_paper\_validation/final\_report\_1\_4\_1.html |
| reportPath | 2019/jama.2019.0556/.ai\_paper\_validation/final\_report\_1\_4\_1.md |
| sourceId | C006 |
| sourceStatus | Pending Human Adjudication |
| statement | The protocol’s stated 25% difference does not reconcile with its displayed 30% control and 15% intervention incidences under ordinary absolute or relative metrics. |
| submissionInvolved | 0 |
| subtype | planned\_effect\_arithmetic |
| suggestedDomain | plan\_material |
| title | Protocol calls a 30% versus 15% contrast a 25% difference |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C007

**Protocol and publication state different sample-size assumptions**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.0556::C007 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> DOC-001 Sample Size — PDF p. 4; DOC-002 Sample Size — PDF p. 16; DOC-002 continuation — PDF p. 17.

### Candidate statement

> Matched enrollment-planning passages report different active event rates, uninflated sample quantities, and attrition assumptions.

### AI rationale

> Article planning assumptions (active incidence 20%, 196 per combination, attrition 22%) differ from protocol assumptions (15%, 180 per group, dropout 20%), despite a shared 250-per-arm target. This is a direct report-versus-protocol comparison.

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

> Publication: 30% versus 20%, 33% reduction, 196 stated per combination, 22% attrition, 250 per combination. Protocol: 30% versus 15%, 180 per group, 20% dropout, 250 per arm.

#### Evidence 1: Reported-versus-comparator

> Same one-year factorial trial’s publication planning inputs versus protocol planning inputs.

#### Evidence 2: Calculation

> Protocol contrast: 15 percentage points/50% relative reduction. Publication: 10 points/33.3% relative reduction. Attrition differs by 2 points; both final targets imply 4x250=1000.

#### Evidence 3: Alternative source-grounded interpretations

> Protocol version 7 may reflect another planning stage or a legitimate amendment; the compared pages do not document the transition.

### Source links

- sourceLinks 0: [DOC-001 Sample Size — PDF p. 4](../../../2019/jama.2019.0556/jama_bot_2019_oi_190007.pdf#page=4)
- sourceLinks 1: [DOC-002 Sample Size — PDF p. 16](../../../2019/jama.2019.0556/joi190007supp1_prod.pdf#page=16)
- sourceLinks 2: [DOC-002 continuation — PDF p. 17](../../../2019/jama.2019.0556/joi190007supp1_prod.pdf#page=17)
- evidencePaths 0: [2019/jama.2019.0556/.ai\_paper\_validation/review\_1\_4\_1/source\_inventory.md](../../../2019/jama.2019.0556/.ai_paper_validation/review_1_4_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.0556/.ai\_paper\_validation/review\_1\_4\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.0556/.ai_paper_validation/review_1_4_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2019/jama.2019.0556/.ai_paper_validation/final_report_1_4_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Protocol version 7 is dated July 6, 2017; article refers to design-time assumptions. Different planning stages or an approved amendment remain possible. C005 and C006 are separate internal arithmetic defects. |
| broadPlanInvolved | 1 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C007 |
| key | 2019::jama.2019.0556::C007 |
| legacyRelationship |  |
| locations | DOC-001 Sample Size — PDF p. 4; DOC-002 Sample Size — PDF p. 16; DOC-002 continuation — PDF p. 17. |
| originalCrossDocument | 1 |
| package | jama.2019.0556 |
| planMechanism | analysis\_specification |
| primary | P\_R |
| rationale | Article planning assumptions (active incidence 20%, 196 per combination, attrition 22%) differ from protocol assumptions (15%, 180 per group, dropout 20%), despite a shared 250-per-arm target. This is a direct report-versus-protocol comparison. |
| reportHref | ../../2019/jama.2019.0556/.ai\_paper\_validation/final\_report\_1\_4\_1.html |
| reportPath | 2019/jama.2019.0556/.ai\_paper\_validation/final\_report\_1\_4\_1.md |
| sourceId | C007 |
| sourceStatus | Pending Human Adjudication |
| statement | Matched enrollment-planning passages report different active event rates, uninflated sample quantities, and attrition assumptions. |
| submissionInvolved | 0 |
| subtype | sample\_size\_assumptions |
| suggestedDomain | protocol\_report |
| title | Protocol and publication state different sample-size assumptions |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | retain |

## Candidate C008

**Protocol uses incompatible DSM editions for the primary endpoint**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.0556::C008 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> DOC-002 endpoint summary — PDF p. 8; DOC-002 Methods 8.1.1 — PDF p. 28; DOC-001 Primary Outcome — PDF p. 4.

### Candidate statement

> The protocol names DSM-IV and DSM-5 for the same MINI-assessed 12-month MDD endpoint and schedule.

### AI rationale

> Protocol p8 specifies DSM-IV and p28 DSM-5 for the same MINI-assessed MDD endpoint and schedule. The article repeats DSM-IV as corroboration of one internal protocol label; the candidate targets the protocol internal inconsistency, not a report-versus-plan deviation.

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

> Protocol p. 8 prints DSM-IV/MINI; p. 28 prints DSM-5/MINI V5.01, both with baseline, 3-, 6-, and 12-month assessment. The article identifies DSM-IV/MINI 5.0.

#### Evidence 1: Reported-versus-comparator

> DSM-IV endpoint label versus DSM-5 label for matching endpoint/schedule.

#### Evidence 2: Calculation

> Logical comparison only: DSM-IV and DSM-5 are distinct labels; no arithmetic applies.

#### Evidence 3: Alternative source-grounded interpretations

> An unrevised section may remain, or the label difference may not have altered the operational MINI assessment.

### Source links

- sourceLinks 0: [DOC-002 endpoint summary — PDF p. 8](../../../2019/jama.2019.0556/joi190007supp1_prod.pdf#page=8)
- sourceLinks 1: [DOC-002 Methods 8.1.1 — PDF p. 28](../../../2019/jama.2019.0556/joi190007supp1_prod.pdf#page=28)
- sourceLinks 2: [DOC-001 Primary Outcome — PDF p. 4](../../../2019/jama.2019.0556/jama_bot_2019_oi_190007.pdf#page=4)
- evidencePaths 0: [2019/jama.2019.0556/.ai\_paper\_validation/review\_1\_4\_1/source\_inventory.md](../../../2019/jama.2019.0556/.ai_paper_validation/review_1_4_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.0556/.ai\_paper\_validation/review\_1\_4\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.0556/.ai_paper_validation/review_1_4_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2019/jama.2019.0556/.ai_paper_validation/final_report_1_4_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_P |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | The edition-label difference may be drafting residue without an operational diagnostic change. |
| broadPlanInvolved | 1 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C008 |
| key | 2019::jama.2019.0556::C008 |
| legacyRelationship |  |
| locations | DOC-002 endpoint summary — PDF p. 8; DOC-002 Methods 8.1.1 — PDF p. 28; DOC-001 Primary Outcome — PDF p. 4. |
| originalCrossDocument | 0 |
| package | jama.2019.0556 |
| planMechanism |  |
| primary | P\_P |
| rationale | Protocol p8 specifies DSM-IV and p28 DSM-5 for the same MINI-assessed MDD endpoint and schedule. The article repeats DSM-IV as corroboration of one internal protocol label; the candidate targets the protocol internal inconsistency, not a report-versus-plan deviation. |
| reportHref | ../../2019/jama.2019.0556/.ai\_paper\_validation/final\_report\_1\_4\_1.html |
| reportPath | 2019/jama.2019.0556/.ai\_paper\_validation/final\_report\_1\_4\_1.md |
| sourceId | C008 |
| sourceStatus | Pending Human Adjudication |
| statement | The protocol names DSM-IV and DSM-5 for the same MINI-assessed 12-month MDD endpoint and schedule. |
| submissionInvolved | 0 |
| subtype | endpoint\_measure\_label |
| suggestedDomain | plan\_material |
| title | Protocol uses incompatible DSM editions for the primary endpoint |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C009

**Analysis-plan significance threshold lacks a comparison operator**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.0556::C009 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> DOC-003 statistical analysis plan — PDF p. 3; local interaction rule — PDF p. 5.

### Candidate statement

> The statistical analysis plan prints p 0.05 for the two-sided significance threshold without an operator.

### AI rationale

> The SAP global significance sentence prints p 0.05 without an operator, whereas a local rule in the same SAP prints p\<0.05. Both sides are plan text.

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

> The global sentence is the 2-sided significance threshold will be set at p 0.05. A p. 5 local modifier rule separately prints p\<0.05.

#### Evidence 1: Reported-versus-comparator

> Operator-free global threshold versus the locally explicit \< comparison.

#### Evidence 2: Calculation

> The p. 3 syntax cannot classify 0.049, 0.050, or 0.051. Under p. 5’s local p\<0.05, 0.049 meets that local rule; this comparator does not correct p. 3.

#### Evidence 3: Alternative source-grounded interpretations

> A less-than glyph may have been lost in production; it renders elsewhere in the same plan.

### Source links

- sourceLinks 0: [DOC-003 statistical analysis plan — PDF p. 3](../../../2019/jama.2019.0556/joi190007supp2_prod.pdf#page=3)
- sourceLinks 1: [local interaction rule — PDF p. 5](../../../2019/jama.2019.0556/joi190007supp2_prod.pdf#page=5)
- evidencePaths 0: [2019/jama.2019.0556/.ai\_paper\_validation/review\_1\_4\_1/source\_inventory.md](../../../2019/jama.2019.0556/.ai_paper_validation/review_1_4_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.0556/.ai\_paper\_validation/review\_1\_4\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.0556/.ai_paper_validation/review_1_4_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2019/jama.2019.0556/.ai_paper_validation/final_report_1_4_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_P |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | The local interaction rule does not establish the intended global equality boundary. |
| broadPlanInvolved | 1 |
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 0 |
| id | C009 |
| key | 2019::jama.2019.0556::C009 |
| legacyRelationship |  |
| locations | DOC-003 statistical analysis plan — PDF p. 3; local interaction rule — PDF p. 5. |
| originalCrossDocument | 0 |
| package | jama.2019.0556 |
| planMechanism |  |
| primary | P\_P |
| rationale | The SAP global significance sentence prints p 0.05 without an operator, whereas a local rule in the same SAP prints p\<0.05. Both sides are plan text. |
| reportHref | ../../2019/jama.2019.0556/.ai\_paper\_validation/final\_report\_1\_4\_1.html |
| reportPath | 2019/jama.2019.0556/.ai\_paper\_validation/final\_report\_1\_4\_1.md |
| sourceId | C009 |
| sourceStatus | Pending Human Adjudication |
| statement | The statistical analysis plan prints p 0.05 for the two-sided significance threshold without an operator. |
| submissionInvolved | 0 |
| subtype | threshold\_operator |
| suggestedDomain | plan\_material |
| title | Analysis-plan significance threshold lacks a comparison operator |
| year | 2019 |
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
