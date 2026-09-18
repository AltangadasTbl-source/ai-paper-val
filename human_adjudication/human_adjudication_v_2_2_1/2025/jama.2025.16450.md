# jama.2025.16450

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2025 |
| Paper | jama.2025.16450 |
| Candidates | 10 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2025/jama.2025.16450/)

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

- [C001](#candidate-c001) — eTable 4 expands RR as risk difference although the table reports relative risk (S_W)
- [C002](#candidate-c002) — Registered eligibility-bound discrepancy is not reproduced on direct-source recheck (P_R)
- [C003](#candidate-c003) — Registered first-dose discrepancy is not reproduced on direct-source recheck (P_R)
- [C004](#candidate-c004) — Severe-NDI GMFCS cutoff differs between the manual and SAP (P_P)
- [C005](#candidate-c005) — Registered severe-NDI instrument-edition discrepancy is not reproduced on direct-source recheck (P_P)
- [C006](#candidate-c006) — Registered first-interim-alpha discrepancy is not reproduced on direct-source recheck (P_P)
- [C007](#candidate-c007) — Final primary-analysis alpha differs between the article and prospective documents (P_R)
- [C008](#candidate-c008) — Trial center count differs between final and prospective documents (P_R)
- [C009](#candidate-c009) — Table 3 RR label conflicts with a stated common-OR approximation (S_W)
- [C010](#candidate-c010) — eTable 3 relative-risk header conflicts with odds-ratio approximation footnote (S_W)

## Candidate C001

**eTable 4 expands RR as risk difference although the table reports relative risk**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.16450::C001 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-005 results supplement — PDF p. 7 (eTable 4 header and PDA row); results supplement — PDF p. 8 (abbreviations and binary-outcome model text).

### Candidate statement

> eTable 4 uses RR for ratio-scale relative-risk estimates but its abbreviation line expands RR as risk difference.

### AI rationale

> Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. The abbreviation says risk difference; the table header, model description, and estimates say or use relative risk.

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

> Page 7 prints Relative Risk (RR) or Mean Difference (MD) and PDA RR: 0.86 (0.75, 0.99); page 8 prints RR = risk difference while stating binary outcomes report relative risks.

#### Evidence 1: Reported-versus-comparator

> The abbreviation says risk difference; the table header, model description, and estimates say or use relative risk.

#### Evidence 2: Calculation

> From displayed PDA counts, (159/319)/(175/308) = 0.8772; 100 x (159/319 - 175/308) = -6.97 percentage points. The adjusted .86 is ratio-scale.

#### Evidence 3: Alternative source-grounded interpretations

> The p. 8 line may be an isolated copyediting or transcription error; the package does not establish cause.

### Source links

- sourceLinks 0: [results supplement — PDF p. 7](../../../2025/jama.2025.16450/joi250072supp4_prod_1761000786.6988.pdf#page=7)
- sourceLinks 1: [results supplement — PDF p. 8](../../../2025/jama.2025.16450/joi250072supp4_prod_1761000786.6988.pdf#page=8)
- evidencePaths 0: [2025/jama.2025.16450/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.16450/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2025.16450/.ai_paper_validation/final_report_1_5_1.md)

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
| key | 2025::jama.2025.16450::C001 |
| legacyRelationship |  |
| locations | DOC-005 results supplement — PDF p. 7 (eTable 4 header and PDA row); results supplement — PDF p. 8 (abbreviations and binary-outcome model text). |
| originalCrossDocument | 0 |
| package | jama.2025.16450 |
| planMechanism |  |
| primary | S\_W |
| rationale | Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. The abbreviation says risk difference; the table header, model description, and estimates say or use relative risk. |
| reportHref | ../../2025/jama.2025.16450/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.16450/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | eTable 4 uses RR for ratio-scale relative-risk estimates but its abbreviation line expands RR as risk difference. |
| submissionInvolved | 1 |
| subtype | eTable 4 expands RR as risk difference although the table reports relative risk |
| suggestedDomain | report\_internal\_inconsistency |
| title | eTable 4 expands RR as risk difference although the table reports relative risk |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C002

**Registered eligibility-bound discrepancy is not reproduced on direct-source recheck**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.16450::C002 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | exclude |

### Source location

> DOC-002 protocol — PDF p. 4; DOC-003 manual — PDF p. 7; DOC-004 SAP — PDF p. 8 and SAP — PDF p. 15; DOC-001 main article — PDF p. 2.

### Candidate statement

> The prior ledger recorded 27 6/7 weeks for DOC-002, but direct-source recheck shows 28 6/7; the original cross-document mismatch is not reproduced.

### AI rationale

> Target compares reported current-study content with supplied protocol/SAP specification. Earlier ledger transcription \`27 6/7\` versus direct-page \`28 6/7\` in DOC-002 and every comparator.

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

> The protocol directly prints 22 0/7 - 28 6/7 weeks gestation; the compared direct sources also print an upper bound of 28 weeks 6 days.

#### Evidence 1: Reported-versus-comparator

> Earlier ledger transcription 27 6/7 versus direct-page 28 6/7 in DOC-002 and every comparator.

#### Evidence 2: Calculation

> Pairwise upper-bound difference is 0 days, not 7 days.

#### Evidence 3: Alternative source-grounded interpretations

> The earlier extraction may have misread a custom-encoded 8 as 7; the mechanism is inferred, not established.

### Source links

- sourceLinks 0: [protocol — PDF p. 4](../../../2025/jama.2025.16450/joi250072supp1_prod_1761000786.68881.pdf#page=4)
- sourceLinks 1: [manual — PDF p. 7](../../../2025/jama.2025.16450/joi250072supp2_prod_1761000786.6938.pdf#page=7)
- sourceLinks 2: [SAP — PDF p. 8](../../../2025/jama.2025.16450/joi250072supp3_prod_1761000786.6988.pdf#page=8)
- sourceLinks 3: [SAP — PDF p. 15](../../../2025/jama.2025.16450/joi250072supp3_prod_1761000786.6988.pdf#page=15)
- sourceLinks 4: [main article — PDF p. 2](../../../2025/jama.2025.16450/jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=2)
- evidencePaths 0: [2025/jama.2025.16450/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.16450/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2025.16450/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Final direct-source recheck explicitly does not reproduce registered mismatch; relationship denotes original registration only.  |
| broadPlanInvolved | 1 |
| category | Analysis-unit or population inconsistency |
| currentReportCrossDocument | 1 |
| id | C002 |
| key | 2025::jama.2025.16450::C002 |
| legacyRelationship |  |
| locations | DOC-002 protocol — PDF p. 4; DOC-003 manual — PDF p. 7; DOC-004 SAP — PDF p. 8 and SAP — PDF p. 15; DOC-001 main article — PDF p. 2. |
| originalCrossDocument | 0 |
| package | jama.2025.16450 |
| planMechanism | population\_recruitment\_sites |
| primary | P\_R |
| rationale | Target compares reported current-study content with supplied protocol/SAP specification. Earlier ledger transcription \`27 6/7\` versus direct-page \`28 6/7\` in DOC-002 and every comparator. |
| reportHref | ../../2025/jama.2025.16450/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.16450/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | The prior ledger recorded 27 6/7 weeks for DOC-002, but direct-source recheck shows 28 6/7; the original cross-document mismatch is not reproduced. |
| submissionInvolved | 0 |
| subtype | Registered eligibility-bound discrepancy is not reproduced on direct-source recheck |
| suggestedDomain | protocol\_report |
| title | Registered eligibility-bound discrepancy is not reproduced on direct-source recheck |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | exclude |

## Candidate C003

**Registered first-dose discrepancy is not reproduced on direct-source recheck**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.16450::C003 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | exclude |

### Source location

> DOC-002 protocol — PDF p. 4; DOC-003 manual — PDF p. 7 and manual — PDF p. 12; DOC-004 SAP — PDF p. 8; DOC-001 main article — PDF p. 2; DOC-005 results supplement — PDF p. 4.

### Candidate statement

> The prior ledger assigned 1.25 mL/kg to the first dose in DOC-002, but direct-source recheck shows 2.5 mL/kg; the original mismatch is not reproduced.

### AI rationale

> Target compares reported current-study content with supplied protocol/SAP specification. Earlier first-dose transcription \`1.25 mL/kg\` versus direct-source first-dose \`2.5 mL/kg\`.

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

> All cited pages identify 2.5 mL/kg as dose 1; the manual and results supplement identify 1.25 mL/kg as dose 2.

#### Evidence 1: Reported-versus-comparator

> Earlier first-dose transcription 1.25 mL/kg versus direct-source first-dose 2.5 mL/kg.

#### Evidence 2: Calculation

> 2.5 / 2.5 = 1; difference 0 mL/kg for the compared first-dose values.

#### Evidence 3: Alternative source-grounded interpretations

> Earlier extraction may have transferred the second-dose value or misread the first-dose volume; cause is not documented.

### Source links

- sourceLinks 0: [protocol — PDF p. 4](../../../2025/jama.2025.16450/joi250072supp1_prod_1761000786.68881.pdf#page=4)
- sourceLinks 1: [manual — PDF p. 7](../../../2025/jama.2025.16450/joi250072supp2_prod_1761000786.6938.pdf#page=7)
- sourceLinks 2: [manual — PDF p. 12](../../../2025/jama.2025.16450/joi250072supp2_prod_1761000786.6938.pdf#page=12)
- sourceLinks 3: [SAP — PDF p. 8](../../../2025/jama.2025.16450/joi250072supp3_prod_1761000786.6988.pdf#page=8)
- sourceLinks 4: [main article — PDF p. 2](../../../2025/jama.2025.16450/jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=2)
- sourceLinks 5: [results supplement — PDF p. 4](../../../2025/jama.2025.16450/joi250072supp4_prod_1761000786.6988.pdf#page=4)
- evidencePaths 0: [2025/jama.2025.16450/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.16450/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2025.16450/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Final direct-source recheck explicitly does not reproduce registered mismatch; relationship denotes original registration only.  |
| broadPlanInvolved | 1 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C003 |
| key | 2025::jama.2025.16450::C003 |
| legacyRelationship |  |
| locations | DOC-002 protocol — PDF p. 4; DOC-003 manual — PDF p. 7 and manual — PDF p. 12; DOC-004 SAP — PDF p. 8; DOC-001 main article — PDF p. 2; DOC-005 results supplement — PDF p. 4. |
| originalCrossDocument | 1 |
| package | jama.2025.16450 |
| planMechanism | intervention\_delivery |
| primary | P\_R |
| rationale | Target compares reported current-study content with supplied protocol/SAP specification. Earlier first-dose transcription \`1.25 mL/kg\` versus direct-source first-dose \`2.5 mL/kg\`. |
| reportHref | ../../2025/jama.2025.16450/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.16450/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | The prior ledger assigned 1.25 mL/kg to the first dose in DOC-002, but direct-source recheck shows 2.5 mL/kg; the original mismatch is not reproduced. |
| submissionInvolved | 0 |
| subtype | Registered first-dose discrepancy is not reproduced on direct-source recheck |
| suggestedDomain | protocol\_report |
| title | Registered first-dose discrepancy is not reproduced on direct-source recheck |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | exclude |

## Candidate C004

**Severe-NDI GMFCS cutoff differs between the manual and SAP**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.16450::C004 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> DOC-003 manual — PDF p. 14 and manual — PDF p. 16; DOC-004 SAP — PDF p. 10 and SAP — PDF p. 33.

### Candidate statement

> The manual defines severe NDI using GMFCS levels 3-5, whereas the SAP uses 4-5.

### AI rationale

> Target compares protocol/SAP against a separate prospective operational manual, not a published-results report. Manual threshold \`{3,4,5}\` versus SAP threshold \`{4,5}\`.

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

> The manual prints 3-5; the SAP prints 4-5/level 4-5 for the severe-NDI component.

#### Evidence 1: Reported-versus-comparator

> Manual threshold {3,4,5} versus SAP threshold {4,5}.

#### Evidence 2: Calculation

> Exact set difference is {3}; the cutoff shifts by one GMFCS level.

#### Evidence 3: Alternative source-grounded interpretations

> A versioned definition change is possible, but no governing amendment or implemented follow-up algorithm is supplied.

### Source links

- sourceLinks 0: [manual — PDF p. 14](../../../2025/jama.2025.16450/joi250072supp2_prod_1761000786.6938.pdf#page=14)
- sourceLinks 1: [manual — PDF p. 16](../../../2025/jama.2025.16450/joi250072supp2_prod_1761000786.6938.pdf#page=16)
- sourceLinks 2: [SAP — PDF p. 10](../../../2025/jama.2025.16450/joi250072supp3_prod_1761000786.6988.pdf#page=10)
- sourceLinks 3: [SAP — PDF p. 33](../../../2025/jama.2025.16450/joi250072supp3_prod_1761000786.6988.pdf#page=33)
- evidencePaths 0: [2025/jama.2025.16450/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.16450/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2025.16450/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_P |
| legacyRelations | 0 | P\_O |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Manual of procedures is a distinct prospective operational document, not final results or protocol/SAP. Versioned definition change possible. |
| broadPlanInvolved | 1 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C004 |
| key | 2025::jama.2025.16450::C004 |
| legacyRelationship | P\_O |
| locations | DOC-003 manual — PDF p. 14 and manual — PDF p. 16; DOC-004 SAP — PDF p. 10 and SAP — PDF p. 33. |
| originalCrossDocument | 0 |
| package | jama.2025.16450 |
| planMechanism |  |
| primary | P\_P |
| rationale | Target compares protocol/SAP against a separate prospective operational manual, not a published-results report. Manual threshold \`{3,4,5}\` versus SAP threshold \`{4,5}\`. |
| reportHref | ../../2025/jama.2025.16450/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.16450/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C004 |
| sourceStatus | Pending Human Adjudication |
| statement | The manual defines severe NDI using GMFCS levels 3-5, whereas the SAP uses 4-5. |
| submissionInvolved | 0 |
| subtype | Severe-NDI GMFCS cutoff differs between the manual and SAP |
| suggestedDomain | plan\_material |
| title | Severe-NDI GMFCS cutoff differs between the manual and SAP |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C005

**Registered severe-NDI instrument-edition discrepancy is not reproduced on direct-source recheck**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.16450::C005 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | exclude |

### Source location

> DOC-003 manual — PDF p. 14 and manual — PDF p. 16; DOC-004 SAP — PDF p. 10, SAP — PDF p. 33, and SAP — PDF p. 34.

### Candidate statement

> The prior ledger reported Bayley-III versus BSID-IV, but direct-source recheck shows BSID-IV/fourth edition throughout; the original mismatch is not reproduced.

### AI rationale

> Target compares protocol/SAP against a separate prospective operational manual, not a published-results report. Earlier ledger Bayley-III transcription versus direct-source fourth-edition/BSID-IV wording.

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

> The cited passages print BSID-IV or 4th edition (BSID-IV) with cognitive score \<70; none prints Bayley-III.

#### Evidence 1: Reported-versus-comparator

> Earlier ledger Bayley-III transcription versus direct-source fourth-edition/BSID-IV wording.

#### Evidence 2: Calculation

> 4th edition and BSID-IV are the same edition; all cited passages retain \<70.

#### Evidence 3: Alternative source-grounded interpretations

> The prior extraction may have read IV as III or carried text from another template; cause is not established.

### Source links

- sourceLinks 0: [manual — PDF p. 14](../../../2025/jama.2025.16450/joi250072supp2_prod_1761000786.6938.pdf#page=14)
- sourceLinks 1: [manual — PDF p. 16](../../../2025/jama.2025.16450/joi250072supp2_prod_1761000786.6938.pdf#page=16)
- sourceLinks 2: [SAP — PDF p. 10](../../../2025/jama.2025.16450/joi250072supp3_prod_1761000786.6988.pdf#page=10)
- sourceLinks 3: [SAP — PDF p. 33](../../../2025/jama.2025.16450/joi250072supp3_prod_1761000786.6988.pdf#page=33)
- sourceLinks 4: [SAP — PDF p. 34](../../../2025/jama.2025.16450/joi250072supp3_prod_1761000786.6988.pdf#page=34)
- evidencePaths 0: [2025/jama.2025.16450/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.16450/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2025.16450/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_P |
| legacyRelations | 0 | P\_O |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Final direct-source recheck explicitly does not reproduce registered mismatch; relationship denotes original registration only.  |
| broadPlanInvolved | 1 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C005 |
| key | 2025::jama.2025.16450::C005 |
| legacyRelationship | P\_O |
| locations | DOC-003 manual — PDF p. 14 and manual — PDF p. 16; DOC-004 SAP — PDF p. 10, SAP — PDF p. 33, and SAP — PDF p. 34. |
| originalCrossDocument | 0 |
| package | jama.2025.16450 |
| planMechanism |  |
| primary | P\_P |
| rationale | Target compares protocol/SAP against a separate prospective operational manual, not a published-results report. Earlier ledger Bayley-III transcription versus direct-source fourth-edition/BSID-IV wording. |
| reportHref | ../../2025/jama.2025.16450/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.16450/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C005 |
| sourceStatus | Pending Human Adjudication |
| statement | The prior ledger reported Bayley-III versus BSID-IV, but direct-source recheck shows BSID-IV/fourth edition throughout; the original mismatch is not reproduced. |
| submissionInvolved | 0 |
| subtype | Registered severe-NDI instrument-edition discrepancy is not reproduced on direct-source recheck |
| suggestedDomain | plan\_material |
| title | Registered severe-NDI instrument-edition discrepancy is not reproduced on direct-source recheck |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | exclude |

## Candidate C006

**Registered first-interim-alpha discrepancy is not reproduced on direct-source recheck**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.16450::C006 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | exclude |

### Source location

> DOC-002 protocol — PDF p. 29; DOC-004 SAP — PDF p. 26.

### Candidate statement

> The prior ledger recorded protocol alpha 0.00015, but both direct pages print 0.000015; the original tenfold mismatch is not reproduced.

### AI rationale

> Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator. Earlier protocol transcription \`0.00015\` versus direct protocol and SAP \`0.000015\`.

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

> Both schedules print first-look alpha 0.000015, followed by .0030, .0183, and .0440.

#### Evidence 1: Reported-versus-comparator

> Earlier protocol transcription 0.00015 versus direct protocol and SAP 0.000015.

#### Evidence 2: Calculation

> 0.000015 / 0.000015 = 1; difference 0.

#### Evidence 3: Alternative source-grounded interpretations

> The earlier extraction may have dropped one zero in custom-encoded text; cause is inferred only.

### Source links

- sourceLinks 0: [protocol — PDF p. 29](../../../2025/jama.2025.16450/joi250072supp1_prod_1761000786.68881.pdf#page=29)
- sourceLinks 1: [SAP — PDF p. 26](../../../2025/jama.2025.16450/joi250072supp3_prod_1761000786.6988.pdf#page=26)
- evidencePaths 0: [2025/jama.2025.16450/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.16450/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2025.16450/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_P |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Final direct-source recheck explicitly does not reproduce registered mismatch; relationship denotes original registration only.  |
| broadPlanInvolved | 1 |
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 0 |
| id | C006 |
| key | 2025::jama.2025.16450::C006 |
| legacyRelationship |  |
| locations | DOC-002 protocol — PDF p. 29; DOC-004 SAP — PDF p. 26. |
| originalCrossDocument | 0 |
| package | jama.2025.16450 |
| planMechanism |  |
| primary | P\_P |
| rationale | Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator. Earlier protocol transcription \`0.00015\` versus direct protocol and SAP \`0.000015\`. |
| reportHref | ../../2025/jama.2025.16450/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.16450/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C006 |
| sourceStatus | Pending Human Adjudication |
| statement | The prior ledger recorded protocol alpha 0.00015, but both direct pages print 0.000015; the original tenfold mismatch is not reproduced. |
| submissionInvolved | 0 |
| subtype | Registered first-interim-alpha discrepancy is not reproduced on direct-source recheck |
| suggestedDomain | plan\_material |
| title | Registered first-interim-alpha discrepancy is not reproduced on direct-source recheck |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | exclude |

## Candidate C007

**Final primary-analysis alpha differs between the article and prospective documents**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.16450::C007 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> DOC-001 main article — PDF p. 3 and main article — PDF p. 7; DOC-002 protocol — PDF p. 29; DOC-004 SAP — PDF p. 26.

### Candidate statement

> The article reports primary-analysis alpha .049; the protocol and SAP list planned final alpha .0440.

### AI rationale

> Target compares reported current-study content with supplied protocol/SAP specification. Executed article alpha \`.049\` versus prospective planned final alpha \`.0440\`.

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

> Article text and Table 2 footnote state .049; the prospective schedules state .0440 for the planned final look.

#### Evidence 1: Reported-versus-comparator

> Executed article alpha .049 versus prospective planned final alpha .0440.

#### Evidence 2: Calculation

> .049 - .0440 = .0050; .049/.0440 = 1.1136.

#### Evidence 3: Alternative source-grounded interpretations

> A realized Lan-DeMets boundary, recovery of unspent alpha, different information timing, unperformed looks, or amendment could explain the values. Relevant execution output is absent.

### Source links

- sourceLinks 0: [main article — PDF p. 3](../../../2025/jama.2025.16450/jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=3)
- sourceLinks 1: [main article — PDF p. 7](../../../2025/jama.2025.16450/jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=7)
- sourceLinks 2: [protocol — PDF p. 29](../../../2025/jama.2025.16450/joi250072supp1_prod_1761000786.68881.pdf#page=29)
- sourceLinks 3: [SAP — PDF p. 26](../../../2025/jama.2025.16450/joi250072supp3_prod_1761000786.6988.pdf#page=26)
- evidencePaths 0: [2025/jama.2025.16450/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.16450/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2025.16450/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Planned versus realized alpha-spending boundaries need not be equal; missing execution output. |
| broadPlanInvolved | 1 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C007 |
| key | 2025::jama.2025.16450::C007 |
| legacyRelationship |  |
| locations | DOC-001 main article — PDF p. 3 and main article — PDF p. 7; DOC-002 protocol — PDF p. 29; DOC-004 SAP — PDF p. 26. |
| originalCrossDocument | 1 |
| package | jama.2025.16450 |
| planMechanism | analysis\_specification |
| primary | P\_R |
| rationale | Target compares reported current-study content with supplied protocol/SAP specification. Executed article alpha \`.049\` versus prospective planned final alpha \`.0440\`. |
| reportHref | ../../2025/jama.2025.16450/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.16450/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C007 |
| sourceStatus | Pending Human Adjudication |
| statement | The article reports primary-analysis alpha .049; the protocol and SAP list planned final alpha .0440. |
| submissionInvolved | 0 |
| subtype | Final primary-analysis alpha differs between the article and prospective documents |
| suggestedDomain | protocol\_report |
| title | Final primary-analysis alpha differs between the article and prospective documents |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | retain |

## Candidate C008

**Trial center count differs between final and prospective documents**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.16450::C008 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> DOC-001 main article — PDF p. 1; DOC-002 protocol — PDF p. 29; DOC-004 SAP — PDF p. 8.

### Candidate statement

> The article states 17 centers; the protocol and SAP state 15 centers in prospective context.

### AI rationale

> Target compares reported current-study content with supplied protocol/SAP specification. Completed-study count 17 versus planned count 15.

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

> DOC-001 reports 17 US centers; the prospective documents refer to 15 NRN centers/planned participation.

#### Evidence 1: Reported-versus-comparator

> Completed-study count 17 versus planned count 15.

#### Evidence 2: Calculation

> 17 - 15 = 2 centers.

#### Evidence 3: Alternative source-grounded interpretations

> Later site activation or a different center/hospital/pooling definition is plausible; activation/enrollment records are absent.

### Source links

- sourceLinks 0: [main article — PDF p. 1](../../../2025/jama.2025.16450/jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=1)
- sourceLinks 1: [protocol — PDF p. 29](../../../2025/jama.2025.16450/joi250072supp1_prod_1761000786.68881.pdf#page=29)
- sourceLinks 2: [SAP — PDF p. 8](../../../2025/jama.2025.16450/joi250072supp3_prod_1761000786.6988.pdf#page=8)
- evidencePaths 0: [2025/jama.2025.16450/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.16450/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2025.16450/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Planned 15 versus completed 17 centers may reflect activation/milestone differences. |
| broadPlanInvolved | 1 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C008 |
| key | 2025::jama.2025.16450::C008 |
| legacyRelationship |  |
| locations | DOC-001 main article — PDF p. 1; DOC-002 protocol — PDF p. 29; DOC-004 SAP — PDF p. 8. |
| originalCrossDocument | 1 |
| package | jama.2025.16450 |
| planMechanism | population\_recruitment\_sites |
| primary | P\_R |
| rationale | Target compares reported current-study content with supplied protocol/SAP specification. Completed-study count 17 versus planned count 15. |
| reportHref | ../../2025/jama.2025.16450/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.16450/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C008 |
| sourceStatus | Pending Human Adjudication |
| statement | The article states 17 centers; the protocol and SAP state 15 centers in prospective context. |
| submissionInvolved | 0 |
| subtype | Trial center count differs between final and prospective documents |
| suggestedDomain | protocol\_report |
| title | Trial center count differs between final and prospective documents |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | retain |

## Candidate C009

**Table 3 RR label conflicts with a stated common-OR approximation**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.16450::C009 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-001 main article — PDF p. 8 (Table 3 additional open-label surfactant row and footnote g).

### Candidate statement

> Table 3 labels an estimate RR while footnote g describes a common-OR approximation after robust-Poisson nonconvergence.

### AI rationale

> Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. RR row label versus common-OR approximation wording.

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

> The row prints RR: 0.69 (0.33 to 1.46) for 13/312 versus 18/299; footnote g names Mantel-Haenszel methods approximated by the common OR.

#### Evidence 1: Reported-versus-comparator

> RR row label versus common-OR approximation wording.

#### Evidence 2: Calculation

> Crude RR (13/312)/(18/299) = 0.6921; crude OR \[13 x 281\]/\[299 x 18\] = 0.6787.

#### Evidence 3: Alternative source-grounded interpretations

> The target estimand may be RR while a common OR was used as a sparse-event approximation. Stratum counts, weights, and model output are unavailable.

### Source links

- sourceLinks 0: [main article — PDF p. 8](../../../2025/jama.2025.16450/jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=8)
- evidencePaths 0: [2025/jama.2025.16450/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.16450/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2025.16450/.ai_paper_validation/final_report_1_5_1.md)

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
| key | 2025::jama.2025.16450::C009 |
| legacyRelationship |  |
| locations | DOC-001 main article — PDF p. 8 (Table 3 additional open-label surfactant row and footnote g). |
| originalCrossDocument | 0 |
| package | jama.2025.16450 |
| planMechanism |  |
| primary | S\_W |
| rationale | Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. RR row label versus common-OR approximation wording. |
| reportHref | ../../2025/jama.2025.16450/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.16450/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C009 |
| sourceStatus | Pending Human Adjudication |
| statement | Table 3 labels an estimate RR while footnote g describes a common-OR approximation after robust-Poisson nonconvergence. |
| submissionInvolved | 1 |
| subtype | Table 3 RR label conflicts with a stated common-OR approximation |
| suggestedDomain | report\_internal\_inconsistency |
| title | Table 3 RR label conflicts with a stated common-OR approximation |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C010

**eTable 3 relative-risk header conflicts with odds-ratio approximation footnote**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.16450::C010 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-005 results supplement — PDF p. 5 and results supplement — PDF p. 6 (eTable 3 header and footnote b).

### Candidate statement

> eTable 3's effect-estimate header says relative risk while footnote b identifies odds-ratio approximations for marked sparse rows.

### AI rationale

> Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. Table-level RR header versus odds-ratio approximation footnote for superscript-b rows.

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

> The header says Relative Risk (95% CI) or P-value; footnote b says marked low-prevalence rows use crude unadjusted odds ratios with exact 95% CIs as an approximation. Marked examples include .73, .65, and 2.64.

#### Evidence 1: Reported-versus-comparator

> Table-level RR header versus odds-ratio approximation footnote for superscript-b rows.

#### Evidence 2: Calculation

> (3 x 309)/(319 x 4) = 0.7265; (2 x 310)/(320 x 3) = 0.6458; (8 x 310)/(314 x 3) = 2.6327, close to .73, .65, and 2.64.

#### Evidence 3: Alternative source-grounded interpretations

> The header may name the target measure and the footnote the approximating estimator. Exact CI reproduction needs the specified exact-interval algorithm and row inputs.

### Source links

- sourceLinks 0: [results supplement — PDF p. 5](../../../2025/jama.2025.16450/joi250072supp4_prod_1761000786.6988.pdf#page=5)
- sourceLinks 1: [results supplement — PDF p. 6](../../../2025/jama.2025.16450/joi250072supp4_prod_1761000786.6988.pdf#page=6)
- evidencePaths 0: [2025/jama.2025.16450/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.16450/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2025.16450/.ai_paper_validation/final_report_1_5_1.md)

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
| id | C010 |
| key | 2025::jama.2025.16450::C010 |
| legacyRelationship |  |
| locations | DOC-005 results supplement — PDF p. 5 and results supplement — PDF p. 6 (eTable 3 header and footnote b). |
| originalCrossDocument | 0 |
| package | jama.2025.16450 |
| planMechanism |  |
| primary | S\_W |
| rationale | Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. Table-level RR header versus odds-ratio approximation footnote for superscript-b rows. |
| reportHref | ../../2025/jama.2025.16450/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.16450/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C010 |
| sourceStatus | Pending Human Adjudication |
| statement | eTable 3's effect-estimate header says relative risk while footnote b identifies odds-ratio approximations for marked sparse rows. |
| submissionInvolved | 1 |
| subtype | eTable 3 relative-risk header conflicts with odds-ratio approximation footnote |
| suggestedDomain | report\_internal\_inconsistency |
| title | eTable 3 relative-risk header conflicts with odds-ratio approximation footnote |
| year | 2025 |
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
