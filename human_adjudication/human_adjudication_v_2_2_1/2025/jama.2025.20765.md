# jama.2025.20765

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2025 |
| Paper | jama.2025.20765 |
| Candidates | 13 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2025/jama.2025.20765/)

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

- [C001](#candidate-c001) — Adjusted self-reported abstinence interval endpoint printed as 42 (S_W)
- [C002](#candidate-c002) — Discussion labels the all-cause death percentage as TB deaths (S_C)
- [C003](#candidate-c003) — 178-message total conflicts with its printed frequency schedule (P_P)
- [C004](#candidate-c004) — Repeated 2,384-participant plan names 44 and 48 facilities (P_P)
- [C005](#candidate-c005) — 134-message total conflicts with its printed frequency schedule (P_P)
- [C006](#candidate-c006) — TAM sampling header conflicts with contemporaneous narrative and equations (P_P)
- [C007](#candidate-c007) — Later 2,716-participant plan gives 48 clinics versus a 63-site diagram (P_P)
- [C008](#candidate-c008) — Phase-4 design-effect equality does not reproduce from printed inputs (P_P)
- [C009](#candidate-c009) — Phase-4 diagram is labelled Phase 3/Superiority (P_P)
- [C010](#candidate-c010) — Phase-3 design-effect display gives undocumented 1,080 effective sample size (P_P)
- [C011](#candidate-c011) — MPSS score range conflicts with stated item scale (P_P)
- [C012](#candidate-c012) — Site 2008 death count and percentage lack a compatible supplied denominator (S_W)
- [C013](#candidate-c013) — Protocol message dose changes from 178 to 134 without supplied reconciliation (P_R)

## Candidate C001

**Adjusted self-reported abstinence interval endpoint printed as 42**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.20765::C001 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001 main article — PDF p. 6, Table 2, continuous abstinence, self-reported only (ITT), adjusted RR.

### Candidate statement

> The printed adjusted self-reported abstinence RR interval has upper endpoint 42, an unusual interval field requiring confirmation against the fitted model output.

### AI rationale

> Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. Printed upper endpoint \`42\` versus the same-row estimate and companion interval context.

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

> Adjusted RR is printed as 2.8 (1.9 to 42); the same row's crude RR is 2.7 (1.8 to 4.1).

#### Evidence 1: Reported-versus-comparator

> Printed upper endpoint 42 versus the same-row estimate and companion interval context.

#### Evidence 2: Calculation

> 42/2.8=15.0; 1.9/2.8=0.6786. Ordinary rounding cannot convert 42 to 4.2.

#### Evidence 3: Alternative source-grounded interpretations

> A genuinely wide asymmetric interval remains possible under the stated mixed-effects model; the package lacks coefficient, SE, and model-output details.

### Source links

- sourceLinks 0: [main article — PDF p. 6](../../../2025/jama.2025.20765/jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6)

[Original Markdown report](../../../2025/jama.2025.20765/.ai_paper_validation/final_report_1_5_1.md)

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
| category | Numeric or arithmetic inconsistency |
| currentReportCrossDocument | 0 |
| id | C001 |
| key | 2025::jama.2025.20765::C001 |
| legacyRelationship |  |
| locations | DOC-001 main article — PDF p. 6, Table 2, continuous abstinence, self-reported only (ITT), adjusted RR. |
| originalCrossDocument | 0 |
| package | jama.2025.20765 |
| planMechanism |  |
| primary | S\_W |
| rationale | Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. Printed upper endpoint \`42\` versus the same-row estimate and companion interval context. |
| reportHref | ../../2025/jama.2025.20765/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.20765/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | The printed adjusted self-reported abstinence RR interval has upper endpoint 42, an unusual interval field requiring confirmation against the fitted model output. |
| submissionInvolved | 1 |
| subtype | Adjusted self-reported abstinence interval endpoint printed as 42 |
| suggestedDomain | statistical\_results |
| title | Adjusted self-reported abstinence interval endpoint printed as 42 |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C002

**Discussion labels the all-cause death percentage as TB deaths**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.20765::C002 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-001 main article — PDF p. 8, Discussion; PDF p. 5 and PDF p. 6, Results/Table 2; DOC-003 Supplement 2 — PDF p. 6, eTable 4.

### Candidate statement

> The discussion's 4.8% phrase “died of TB” matches the all-cause death total rather than the supplied TB-cause count.

### AI rationale

> Target explicitly compares current main article and non-plan results supplement/workbook. 4.8% labelled TB deaths versus 52/1080 all-cause deaths and 32/1080 TB-cause deaths.

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

> The discussion says 4.8% died of TB; Table 2 gives 25/720 and 27/360 deaths, and eTable 4 classifies 32/52 deaths as TB cause.

#### Evidence 1: Reported-versus-comparator

> 4.8% labelled TB deaths versus 52/1080 all-cause deaths and 32/1080 TB-cause deaths.

#### Evidence 2: Calculation

> 52/1080×100=4.81% (4.8%); 32/1080×100=2.96% (3.0%).

#### Evidence 3: Alternative source-grounded interpretations

> “Died of TB” could be loose contextual wording; eTable 4 is the explicit cause classification and no alternate TB-death denominator is supplied.

### Source links

- sourceLinks 0: [main article — PDF p. 8](../../../2025/jama.2025.20765/jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=8)
- sourceLinks 1: [PDF p. 5](../../../2025/jama.2025.20765/jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5)
- sourceLinks 2: [PDF p. 6](../../../2025/jama.2025.20765/jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6)
- sourceLinks 3: [Supplement 2 — PDF p. 6](../../../2025/jama.2025.20765/joi250093supp2_prod_1768590553.09463.pdf#page=6)

[Original Markdown report](../../../2025/jama.2025.20765/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_C |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | All-cause main total corroborates cause-label issue, while explicitly disaggregated TB deaths come from results supplement. |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C002 |
| key | 2025::jama.2025.20765::C002 |
| legacyRelationship |  |
| locations | DOC-001 main article — PDF p. 8, Discussion; PDF p. 5 and PDF p. 6, Results/Table 2; DOC-003 Supplement 2 — PDF p. 6, eTable 4. |
| originalCrossDocument | 1 |
| package | jama.2025.20765 |
| planMechanism |  |
| primary | S\_C |
| rationale | Target explicitly compares current main article and non-plan results supplement/workbook. 4.8% labelled TB deaths versus 52/1080 all-cause deaths and 32/1080 TB-cause deaths. |
| reportHref | ../../2025/jama.2025.20765/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.20765/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | The discussion's 4.8% phrase “died of TB” matches the all-cause death total rather than the supplied TB-cause count. |
| submissionInvolved | 1 |
| subtype | Discussion labels the all-cause death percentage as TB deaths |
| suggestedDomain | report\_internal\_inconsistency |
| title | Discussion labels the all-cause death percentage as TB deaths |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C003

**178-message total conflicts with its printed frequency schedule**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.20765::C003 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> DOC-002 Supplement 1 — PDF p. 16.

### Candidate statement

> A six-month plan states 178 SMS but its own minimum printed schedule exceeds that total.

### AI rationale

> Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator. Printed total 178 versus the schedule's conservative minimum.

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

> 178 SMS over six months; first two months 4-5/day, next two 2-3/day, final two 1-2/week.

#### Evidence 1: Reported-versus-comparator

> Printed total 178 versus the schedule's conservative minimum.

#### Evidence 2: Calculation

> 2×28×4 + 2×28×2 + 8×1=344, 166 above 178; at 30-day months, 368.

#### Evidence 3: Alternative source-grounded interpretations

> “Message” may mean a send, template, or another undefined unit; frequency, duration, or total may be from unlabelled plan states.

### Source links

- sourceLinks 0: [Supplement 1 — PDF p. 16](../../../2025/jama.2025.20765/joi250093supp1_prod_1768590553.08963.pdf#page=16)

[Original Markdown report](../../../2025/jama.2025.20765/.ai_paper_validation/final_report_1_5_1.md)

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
| id | C003 |
| key | 2025::jama.2025.20765::C003 |
| legacyRelationship |  |
| locations | DOC-002 Supplement 1 — PDF p. 16. |
| originalCrossDocument | 0 |
| package | jama.2025.20765 |
| planMechanism |  |
| primary | P\_P |
| rationale | Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator. Printed total 178 versus the schedule's conservative minimum. |
| reportHref | ../../2025/jama.2025.20765/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.20765/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | A six-month plan states 178 SMS but its own minimum printed schedule exceeds that total. |
| submissionInvolved | 0 |
| subtype | 178-message total conflicts with its printed frequency schedule |
| suggestedDomain | plan\_material |
| title | 178-message total conflicts with its printed frequency schedule |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C004

**Repeated 2,384-participant plan names 44 and 48 facilities**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.20765::C004 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> DOC-002 Supplement 1 — PDF p. 10 and PDF p. 26.

### Candidate statement

> Matched repeated plan text gives 44 facilities in one location and 48 clinics in another.

### AI rationale

> Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator. 44 versus 48 sites for the same printed plan.

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

> Both locations describe the 2,384-participant plan, approximately 50 recruits, 10% missing primary outcome, 16 pilot participants, and matching Phase-3/4 allocation assumptions, but list 44 and 48 sites.

#### Evidence 1: Reported-versus-comparator

> 44 versus 48 sites for the same printed plan.

#### Evidence 2: Calculation

> 2384/44=54.18; 2384/48=49.67; the latter aligns with approximately 50.

#### Evidence 3: Alternative source-grounded interpretations

> Facility/clinic definitions or amendment chronology may differ but are not supplied.

### Source links

- sourceLinks 0: [Supplement 1 — PDF p. 10](../../../2025/jama.2025.20765/joi250093supp1_prod_1768590553.08963.pdf#page=10)
- sourceLinks 1: [PDF p. 26](../../../2025/jama.2025.20765/joi250093supp1_prod_1768590553.08963.pdf#page=26)

[Original Markdown report](../../../2025/jama.2025.20765/.ai_paper_validation/final_report_1_5_1.md)

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
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 0 |
| id | C004 |
| key | 2025::jama.2025.20765::C004 |
| legacyRelationship |  |
| locations | DOC-002 Supplement 1 — PDF p. 10 and PDF p. 26. |
| originalCrossDocument | 1 |
| package | jama.2025.20765 |
| planMechanism |  |
| primary | P\_P |
| rationale | Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator. 44 versus 48 sites for the same printed plan. |
| reportHref | ../../2025/jama.2025.20765/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.20765/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C004 |
| sourceStatus | Pending Human Adjudication |
| statement | Matched repeated plan text gives 44 facilities in one location and 48 clinics in another. |
| submissionInvolved | 0 |
| subtype | Repeated 2,384-participant plan names 44 and 48 facilities |
| suggestedDomain | plan\_material |
| title | Repeated 2,384-participant plan names 44 and 48 facilities |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C005

**134-message total conflicts with its printed frequency schedule**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.20765::C005 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> DOC-002 Supplement 1 — PDF p. 53.

### Candidate statement

> A 134-message six-month statement conflicts with the minimum implied by its printed schedule.

### AI rationale

> Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator. Printed total 134 versus schedule minimum.

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

> 134 SMS over six months; first two months 4-5/day, next two 1-2/day, final two 1/week.

#### Evidence 1: Reported-versus-comparator

> Printed total 134 versus schedule minimum.

#### Evidence 2: Calculation

> 2×28×4 + 2×28×1 + 8×1=288, 154 above 134; the 30-day calculation is 308.

#### Evidence 3: Alternative source-grounded interpretations

> Unique-template versus send units or an unlabelled version may explain the text; p. 80 has a different 134-message schedule but does not label p. 53 as a separate plan state.

### Source links

- sourceLinks 0: [Supplement 1 — PDF p. 53](../../../2025/jama.2025.20765/joi250093supp1_prod_1768590553.08963.pdf#page=53)

[Original Markdown report](../../../2025/jama.2025.20765/.ai_paper_validation/final_report_1_5_1.md)

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
| id | C005 |
| key | 2025::jama.2025.20765::C005 |
| legacyRelationship |  |
| locations | DOC-002 Supplement 1 — PDF p. 53. |
| originalCrossDocument | 0 |
| package | jama.2025.20765 |
| planMechanism |  |
| primary | P\_P |
| rationale | Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator. Printed total 134 versus schedule minimum. |
| reportHref | ../../2025/jama.2025.20765/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.20765/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C005 |
| sourceStatus | Pending Human Adjudication |
| statement | A 134-message six-month statement conflicts with the minimum implied by its printed schedule. |
| submissionInvolved | 0 |
| subtype | 134-message total conflicts with its printed frequency schedule |
| suggestedDomain | plan\_material |
| title | 134-message total conflicts with its printed frequency schedule |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C006

**TAM sampling header conflicts with contemporaneous narrative and equations**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.20765::C006 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> DOC-002 Supplement 1 — PDF p. 55.

### Candidate statement

> A TAM sampling header says 30%, while contemporaneous phase-specific narrative and equations show 20% Phase 3 and all Phase 4 participants.

### AI rationale

> Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator. 30% header versus 20%/100% phase-specific calculation.

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

> Header 30%; narrative 20% in Phase 3 and all in Phase 4; equations 10×40×20%=80, 8×40×20%=64, 11×45=495, and 7×45=315.

#### Evidence 1: Reported-versus-comparator

> 30% header versus 20%/100% phase-specific calculation.

#### Evidence 2: Calculation

> 80+64=144=20% of 720 Phase-3 A participants; 495+315=810=100% of Phase-4 A participants.

#### Evidence 3: Alternative source-grounded interpretations

> 30% could refer to an unstated pooled or earlier target.

### Source links

- sourceLinks 0: [Supplement 1 — PDF p. 55](../../../2025/jama.2025.20765/joi250093supp1_prod_1768590553.08963.pdf#page=55)
- evidencePaths 0: [2025/jama.2025.20765/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.20765/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2025.20765/.ai_paper_validation/final_report_1_5_1.md)

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
| id | C006 |
| key | 2025::jama.2025.20765::C006 |
| legacyRelationship |  |
| locations | DOC-002 Supplement 1 — PDF p. 55. |
| originalCrossDocument | 0 |
| package | jama.2025.20765 |
| planMechanism |  |
| primary | P\_P |
| rationale | Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator. 30% header versus 20%/100% phase-specific calculation. |
| reportHref | ../../2025/jama.2025.20765/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.20765/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C006 |
| sourceStatus | Pending Human Adjudication |
| statement | A TAM sampling header says 30%, while contemporaneous phase-specific narrative and equations show 20% Phase 3 and all Phase 4 participants. |
| submissionInvolved | 0 |
| subtype | TAM sampling header conflicts with contemporaneous narrative and equations |
| suggestedDomain | plan\_material |
| title | TAM sampling header conflicts with contemporaneous narrative and equations |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C007

**Later 2,716-participant plan gives 48 clinics versus a 63-site diagram**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.20765::C007 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> DOC-002 Supplement 1 — PDF p. 48, PDF p. 51, PDF p. 52, and PDF p. 62.

### Candidate statement

> A later 2,716-participant plan presents 48 clinics and approximately 50 recruits per clinic, while related text and diagram present 63 sites and approximately 43 per site.

### AI rationale

> Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator. Same plan total with 48/~50 versus 63/~43.

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

> p. 48 and the pp. 51-52 diagram give 2,716 participants, 63 sites (27+36), and approximately 43/site; p. 62 gives 2,716, approximately 50 from 48 clinics.

#### Evidence 1: Reported-versus-comparator

> Same plan total with 48/~50 versus 63/~43.

#### Evidence 2: Calculation

> 2716/63=43.11; 2716/48=56.58; site counts differ by 15.

#### Evidence 3: Alternative source-grounded interpretations

> The 48 clinics may be an unstated subset or earlier plan.

### Source links

- sourceLinks 0: [Supplement 1 — PDF p. 48](../../../2025/jama.2025.20765/joi250093supp1_prod_1768590553.08963.pdf#page=48)
- sourceLinks 1: [PDF p. 51](../../../2025/jama.2025.20765/joi250093supp1_prod_1768590553.08963.pdf#page=51)
- sourceLinks 2: [PDF p. 52](../../../2025/jama.2025.20765/joi250093supp1_prod_1768590553.08963.pdf#page=52)
- sourceLinks 3: [PDF p. 62](../../../2025/jama.2025.20765/joi250093supp1_prod_1768590553.08963.pdf#page=62)

[Original Markdown report](../../../2025/jama.2025.20765/.ai_paper_validation/final_report_1_5_1.md)

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
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 0 |
| id | C007 |
| key | 2025::jama.2025.20765::C007 |
| legacyRelationship |  |
| locations | DOC-002 Supplement 1 — PDF p. 48, PDF p. 51, PDF p. 52, and PDF p. 62. |
| originalCrossDocument | 1 |
| package | jama.2025.20765 |
| planMechanism |  |
| primary | P\_P |
| rationale | Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator. Same plan total with 48/~50 versus 63/~43. |
| reportHref | ../../2025/jama.2025.20765/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.20765/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C007 |
| sourceStatus | Pending Human Adjudication |
| statement | A later 2,716-participant plan presents 48 clinics and approximately 50 recruits per clinic, while related text and diagram present 63 sites and approximately 43 per site. |
| submissionInvolved | 0 |
| subtype | Later 2,716-participant plan gives 48 clinics versus a 63-site diagram |
| suggestedDomain | plan\_material |
| title | Later 2,716-participant plan gives 48 clinics versus a 63-site diagram |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C008

**Phase-4 design-effect equality does not reproduce from printed inputs**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.20765::C008 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> DOC-002 Supplement 1 — PDF p. 64.

### Candidate statement

> A Phase-4 display equates 1,036 multiplied by 1.56 to 1,620, although the exact product differs.

### AI rationale

> Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator. Displayed \`1036×1.56=1620\` versus exact product and the separate site-target total.

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

> 864+(864×0.2)=1036; 1036/36=29; DE=1+0.02(29-1)=1.56; ESS=1036×1.56=1620; diagram 36×45=1620.

#### Evidence 1: Reported-versus-comparator

> Displayed 1036×1.56=1620 versus exact product and the separate site-target total.

#### Evidence 2: Calculation

> 864×1.2=1036.8; 1036×1.56=1616.16; 36×45=1620.

#### Evidence 3: Alternative source-grounded interpretations

> A cluster-level ceiling/allocation step can explain 1,620 but is not stated.

### Source links

- sourceLinks 0: [Supplement 1 — PDF p. 64](../../../2025/jama.2025.20765/joi250093supp1_prod_1768590553.08963.pdf#page=64)

[Original Markdown report](../../../2025/jama.2025.20765/.ai_paper_validation/final_report_1_5_1.md)

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
| id | C008 |
| key | 2025::jama.2025.20765::C008 |
| legacyRelationship |  |
| locations | DOC-002 Supplement 1 — PDF p. 64. |
| originalCrossDocument | 0 |
| package | jama.2025.20765 |
| planMechanism |  |
| primary | P\_P |
| rationale | Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator. Displayed \`1036×1.56=1620\` versus exact product and the separate site-target total. |
| reportHref | ../../2025/jama.2025.20765/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.20765/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C008 |
| sourceStatus | Pending Human Adjudication |
| statement | A Phase-4 display equates 1,036 multiplied by 1.56 to 1,620, although the exact product differs. |
| submissionInvolved | 0 |
| subtype | Phase-4 design-effect equality does not reproduce from printed inputs |
| suggestedDomain | plan\_material |
| title | Phase-4 design-effect equality does not reproduce from printed inputs |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C009

**Phase-4 diagram is labelled Phase 3/Superiority**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.20765::C009 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> DOC-002 Supplement 1 — PDF p. 64.

### Candidate statement

> A diagram within a Phase-4 noninferiority section is labelled “Phase 3 (Superiority trial).”

### AI rationale

> Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator. Phase-3/Superiority label versus local Phase-4/noninferiority plan.

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

> Local text says Phase 4, noninferiority, A vs B, 36 sites, 1,620 participants; diagram says “Total clusters in Phase 3 (Superiority trial) = 36 sites.”

#### Evidence 1: Reported-versus-comparator

> Phase-3/Superiority label versus local Phase-4/noninferiority plan.

#### Evidence 2: Calculation

> 18+18=36; 36×45=1620; the separate Phase-3 plan uses 27 sites and 1,080 participants.

#### Evidence 3: Alternative source-grounded interpretations

> A carry-over caption is plausible but not established by the supplied record.

### Source links

- sourceLinks 0: [Supplement 1 — PDF p. 64](../../../2025/jama.2025.20765/joi250093supp1_prod_1768590553.08963.pdf#page=64)

[Original Markdown report](../../../2025/jama.2025.20765/.ai_paper_validation/final_report_1_5_1.md)

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
| id | C009 |
| key | 2025::jama.2025.20765::C009 |
| legacyRelationship |  |
| locations | DOC-002 Supplement 1 — PDF p. 64. |
| originalCrossDocument | 0 |
| package | jama.2025.20765 |
| planMechanism |  |
| primary | P\_P |
| rationale | Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator. Phase-3/Superiority label versus local Phase-4/noninferiority plan. |
| reportHref | ../../2025/jama.2025.20765/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.20765/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C009 |
| sourceStatus | Pending Human Adjudication |
| statement | A diagram within a Phase-4 noninferiority section is labelled “Phase 3 (Superiority trial).” |
| submissionInvolved | 0 |
| subtype | Phase-4 diagram is labelled Phase 3/Superiority |
| suggestedDomain | plan\_material |
| title | Phase-4 diagram is labelled Phase 3/Superiority |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C010

**Phase-3 design-effect display gives undocumented 1,080 effective sample size**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.20765::C010 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> DOC-002 Supplement 1 — PDF p. 63 and PDF p. 83.

### Candidate statement

> A Phase-3 display reports 704×1.50≈1080 and calls it effective sample size without documenting the cluster-rounding/allocation transition or terminology.

### AI rationale

> Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator. \`704×1.50≈1080\` and “effective sample size” versus exact multiplication and the independent \`27×40=1080\` cluster allocation.

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

> p. 63 gives N=587+(587×0.2)=704, 27 sites, 704/27=26, DE=1+0.02(26−1)=1.50, and ESS=704×1.50≈1080 (40/site); p. 83 repeats 704, 26, DE 1.50, and 1080/40/site.

#### Evidence 1: Reported-versus-comparator

> 704×1.50≈1080 and “effective sample size” versus exact multiplication and the independent 27×40=1080 cluster allocation.

#### Evidence 2: Calculation

> 704×1.50=1056; 1080/704=1.5341; 27×40=1080.

#### Evidence 3: Alternative source-grounded interpretations

> The 1,056 design-effect-inflated target may have been rounded upward to 40 per site; that is plausible but unstated, and 1,080 is not asserted impossible.

### Source links

- sourceLinks 0: [Supplement 1 — PDF p. 63](../../../2025/jama.2025.20765/joi250093supp1_prod_1768590553.08963.pdf#page=63)
- sourceLinks 1: [PDF p. 83](../../../2025/jama.2025.20765/joi250093supp1_prod_1768590553.08963.pdf#page=83)

[Original Markdown report](../../../2025/jama.2025.20765/.ai_paper_validation/final_report_1_5_1.md)

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
| id | C010 |
| key | 2025::jama.2025.20765::C010 |
| legacyRelationship |  |
| locations | DOC-002 Supplement 1 — PDF p. 63 and PDF p. 83. |
| originalCrossDocument | 0 |
| package | jama.2025.20765 |
| planMechanism |  |
| primary | P\_P |
| rationale | Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator. \`704×1.50≈1080\` and “effective sample size” versus exact multiplication and the independent \`27×40=1080\` cluster allocation. |
| reportHref | ../../2025/jama.2025.20765/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.20765/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C010 |
| sourceStatus | Pending Human Adjudication |
| statement | A Phase-3 display reports 704×1.50≈1080 and calls it effective sample size without documenting the cluster-rounding/allocation transition or terminology. |
| submissionInvolved | 0 |
| subtype | Phase-3 design-effect display gives undocumented 1,080 effective sample size |
| suggestedDomain | plan\_material |
| title | Phase-3 design-effect display gives undocumented 1,080 effective sample size |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C011

**MPSS score range conflicts with stated item scale**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.20765::C011 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> DOC-002 Supplement 1 — PDF p. 85.

### Candidate statement

> The MPSS description names five 5-point domains but gives a summed 5-35 range without explaining the scoring rule.

### AI rationale

> Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator. Printed 5-35 range versus the stated five-domain 5-point description.

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

> MPSS has five domains rated on a 5-point scale and summed 5-35.

#### Evidence 1: Reported-versus-comparator

> Printed 5-35 range versus the stated five-domain 5-point description.

#### Evidence 2: Calculation

> Under ordinary 1-to-5 coding, five items span 5×1=5 to 5×5=25, not 35.

#### Evidence 3: Alternative source-grounded interpretations

> Additional items, non-unit coding, weights, anchors, or transformation could yield 35; none is supplied.

### Source links

- sourceLinks 0: [Supplement 1 — PDF p. 85](../../../2025/jama.2025.20765/joi250093supp1_prod_1768590553.08963.pdf#page=85)

[Original Markdown report](../../../2025/jama.2025.20765/.ai_paper_validation/final_report_1_5_1.md)

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
| id | C011 |
| key | 2025::jama.2025.20765::C011 |
| legacyRelationship |  |
| locations | DOC-002 Supplement 1 — PDF p. 85. |
| originalCrossDocument | 0 |
| package | jama.2025.20765 |
| planMechanism |  |
| primary | P\_P |
| rationale | Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator. Printed 5-35 range versus the stated five-domain 5-point description. |
| reportHref | ../../2025/jama.2025.20765/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.20765/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C011 |
| sourceStatus | Pending Human Adjudication |
| statement | The MPSS description names five 5-point domains but gives a summed 5-35 range without explaining the scoring rule. |
| submissionInvolved | 0 |
| subtype | MPSS score range conflicts with stated item scale |
| suggestedDomain | plan\_material |
| title | MPSS score range conflicts with stated item scale |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C012

**Site 2008 death count and percentage lack a compatible supplied denominator**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.20765::C012 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-003 Supplement 2 — PDF p. 8, eTable 5; PDF p. 9, eTable 6.

### Candidate statement

> Site 2008 is reported as 5 deaths (7.5%) without a denominator compatible with the supplied same-site recruitment/ITT total.

### AI rationale

> Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. 5 deaths (7.5%) versus matched same-site 40-person recruitment/ITT denominator.

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

> eTable 5 gives site 2008 recruitment/ITT denominator 40; eTable 6 gives 5 (7.5%) deaths without printing a denominator.

#### Evidence 1: Reported-versus-comparator

> 5 deaths (7.5%) versus matched same-site 40-person recruitment/ITT denominator.

#### Evidence 2: Calculation

> If denominator is 40, 5/40×100=12.5%; 5/0.075=66.67, and no 66-67 site population is supplied.

#### Evidence 3: Alternative source-grounded interpretations

> A distinct unprinted death denominator may exist.

### Source links

- sourceLinks 0: [Supplement 2 — PDF p. 8](../../../2025/jama.2025.20765/joi250093supp2_prod_1768590553.09463.pdf#page=8)
- sourceLinks 1: [PDF p. 9](../../../2025/jama.2025.20765/joi250093supp2_prod_1768590553.09463.pdf#page=9)

[Original Markdown report](../../../2025/jama.2025.20765/.ai_paper_validation/final_report_1_5_1.md)

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
| category | Rate-versus-count inconsistency |
| currentReportCrossDocument | 0 |
| id | C012 |
| key | 2025::jama.2025.20765::C012 |
| legacyRelationship |  |
| locations | DOC-003 Supplement 2 — PDF p. 8, eTable 5; PDF p. 9, eTable 6. |
| originalCrossDocument | 0 |
| package | jama.2025.20765 |
| planMechanism |  |
| primary | S\_W |
| rationale | Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. 5 deaths (7.5%) versus matched same-site 40-person recruitment/ITT denominator. |
| reportHref | ../../2025/jama.2025.20765/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.20765/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C012 |
| sourceStatus | Pending Human Adjudication |
| statement | Site 2008 is reported as 5 deaths (7.5%) without a denominator compatible with the supplied same-site recruitment/ITT total. |
| submissionInvolved | 1 |
| subtype | Site 2008 death count and percentage lack a compatible supplied denominator |
| suggestedDomain | statistical\_results |
| title | Site 2008 death count and percentage lack a compatible supplied denominator |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C013

**Protocol message dose changes from 178 to 134 without supplied reconciliation**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.20765::C013 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> DOC-002 Supplement 1 — PDF p. 16, PDF p. 53, PDF p. 80, and PDF p. 101 through PDF p. 109; DOC-001 main article — PDF p. 3.

### Candidate statement

> Protocol and main-article materials give 178 and 134 messages for the six-month mTB-Tobacco participant dose without an explicit crosswalk or supersession statement.

### AI rationale

> Target compares reported current-study content with supplied protocol/SAP specification. 178 versus 134 for matched six-month intervention dose.

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

> p. 16 says 178 SMS; pp. 53 and 80 say 134 with differing schedules; pp. 101-109 show a 1-134 log; main p. 3 reports 134 unique messages as 100+30+4.

#### Evidence 1: Reported-versus-comparator

> 178 versus 134 for matched six-month intervention dose.

#### Evidence 2: Calculation

> 178−134=44; 100+30+4=134; the log begins at 1 and ends at 134.

#### Evidence 3: Alternative source-grounded interpretations

> A formal amendment is plausible, but supplied material does not explicitly link the 178-message passage to the later 134-message regimen or establish what participants received.

### Source links

- sourceLinks 0: [Supplement 1 — PDF p. 16](../../../2025/jama.2025.20765/joi250093supp1_prod_1768590553.08963.pdf#page=16)
- sourceLinks 1: [PDF p. 53](../../../2025/jama.2025.20765/joi250093supp1_prod_1768590553.08963.pdf#page=53)
- sourceLinks 2: [PDF p. 80](../../../2025/jama.2025.20765/joi250093supp1_prod_1768590553.08963.pdf#page=80)
- sourceLinks 3: [PDF p. 101](../../../2025/jama.2025.20765/joi250093supp1_prod_1768590553.08963.pdf#page=101)
- sourceLinks 4: [PDF p. 109](../../../2025/jama.2025.20765/joi250093supp1_prod_1768590553.08963.pdf#page=109)
- sourceLinks 5: [main article — PDF p. 3](../../../2025/jama.2025.20765/jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3)
- evidencePaths 0: [2025/jama.2025.20765/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.20765/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2025.20765/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |
| relations | 1 | P\_P |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Explicit old-plan versus later-plan and reported 178/134 message total difference. Distinct from schedule arithmetic C003/C005; chronology unresolved. |
| broadPlanInvolved | 1 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C013 |
| key | 2025::jama.2025.20765::C013 |
| legacyRelationship |  |
| locations | DOC-002 Supplement 1 — PDF p. 16, PDF p. 53, PDF p. 80, and PDF p. 101 through PDF p. 109; DOC-001 main article — PDF p. 3. |
| originalCrossDocument | 1 |
| package | jama.2025.20765 |
| planMechanism | intervention\_delivery |
| primary | P\_R |
| rationale | Target compares reported current-study content with supplied protocol/SAP specification. 178 versus 134 for matched six-month intervention dose. |
| reportHref | ../../2025/jama.2025.20765/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.20765/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C013 |
| sourceStatus | Pending Human Adjudication |
| statement | Protocol and main-article materials give 178 and 134 messages for the six-month mTB-Tobacco participant dose without an explicit crosswalk or supersession statement. |
| submissionInvolved | 0 |
| subtype | Protocol message dose changes from 178 to 134 without supplied reconciliation |
| suggestedDomain | protocol\_report |
| title | Protocol message dose changes from 178 to 134 without supplied reconciliation |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
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
