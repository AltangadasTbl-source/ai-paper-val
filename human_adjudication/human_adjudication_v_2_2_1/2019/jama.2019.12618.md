# jama.2019.12618

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2019 |
| Paper | jama.2019.12618 |
| Candidates | 8 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2019/jama.2019.12618/)

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

- [C001](#candidate-c001) — protocol timeline end date (P_P)
- [C002](#candidate-c002) — eligible failure total vs switching denominators (S_W)
- [C003](#candidate-c003) — allocation block sizes (P_R)
- [C004](#candidate-c004) — six-month success injection-after-90-days criterion (P_R)
- [C005](#candidate-c005) — missed-dose Welch P=.87 compatibility (S_W)
- [C006](#candidate-c006) — main Table 3 MMF n=109 header vs supplement N=108/percentages (S_C)
- [C007](#candidate-c007) — eTable 9 MMF serious diarrhea 1 (3.4) vs N=20 (S_W)
- [C008](#candidate-c008) — eTable 8 serious-ocular hypertension label vs eTable 1 surgery-required definition (S_W)

## Candidate C001

**protocol timeline end date**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.12618::C001 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> joi190092supp2\_prod.pdf — PDF p. 11, Table 1.

### Candidate statement

> Pending Human Adjudication: the printed protocol timeline has a maximum 12-month follow-up plus a one-month window ending before both the implied endpoint for the final enrollment month and the printed shorter follow-up endpoint.

### AI rationale

> A protocol timeline prints final enrollment May 2015, six-month follow-up December 2015, and maximum 12-month-plus-window follow-up July 2015. The ordering and implied June 2016 end conflict inside the protocol.

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

> Table 1 prints enrollment through May 2015, six-month follow-up through December 2015, and maximum 12-month follow-up plus a one-month visit window through July 2015.

#### Evidence 1: Reported-versus-comparator

> The July 2015 maximum-follow-up endpoint is compared with the May 2015 last enrollment month plus the printed duration, and independently with December 2015 for the shorter follow-up phase.

#### Evidence 2: Calculation

> May 2015 + 12 months + one-month window reaches approximately June 2016. July 2015 is also five months earlier than December 2015.

#### Evidence 3: Alternative source-grounded interpretations

> July 2015 may refer to an earlier cohort, a year digit may be typographical, or an unsupplied amendment may govern the schedule.

### Source links

- sourceLinks 0: [joi190092supp2\_prod.pdf — PDF p. 11, Table 1](../../../2019/jama.2019.12618/joi190092supp2_prod.pdf#page=11)
- evidencePaths 0: [2019/jama.2019.12618/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.12618/.ai_paper_validation/review_1_5_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.12618/.ai\_paper\_validation/review\_1\_5\_1/preprocessing/protocol\_pp001\_032\_layout.txt](../../../2019/jama.2019.12618/.ai_paper_validation/review_1_5_1/preprocessing/protocol_pp001_032_layout.txt)
- evidencePaths 2: [2019/jama.2019.12618/.ai\_paper\_validation/review\_1\_5\_1/parts/support\_protocol\_pp001\_032.md](../../../2019/jama.2019.12618/.ai_paper_validation/review_1_5_1/parts/support_protocol_pp001_032.md)

[Original Markdown report](../../../2019/jama.2019.12618/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_P |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Cohort applicability or an amendment could distinguish the July endpoint. Document role checked: the bundle cover explicitly identifies original protocol, final protocol, and changes; its protocols are written in MOP format and contain full trial design and endpoint definitions. |
| broadPlanInvolved | 1 |
| category | Numeric or arithmetic inconsistency |
| currentReportCrossDocument | 0 |
| id | C001 |
| key | 2019::jama.2019.12618::C001 |
| legacyRelationship |  |
| locations | joi190092supp2\_prod.pdf — PDF p. 11, Table 1. |
| originalCrossDocument | 0 |
| package | jama.2019.12618 |
| planMechanism |  |
| primary | P\_P |
| rationale | A protocol timeline prints final enrollment May 2015, six-month follow-up December 2015, and maximum 12-month-plus-window follow-up July 2015. The ordering and implied June 2016 end conflict inside the protocol. |
| reportHref | ../../2019/jama.2019.12618/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.12618/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | Pending Human Adjudication: the printed protocol timeline has a maximum 12-month follow-up plus a one-month window ending before both the implied endpoint for the final enrollment month and the printed shorter follow-up endpoint. |
| submissionInvolved | 0 |
| subtype | timeline\_arithmetic |
| suggestedDomain | plan\_material |
| title | protocol timeline end date |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C002

**eligible failure total vs switching denominators**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.12618::C002 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> jama\_rathinam\_2019\_oi\_190092.pdf — PDF p. 7; jama\_rathinam\_2019\_oi\_190092.pdf — PDF p. 6, Table 2; jama\_rathinam\_2019\_oi\_190092.pdf — PDF p. 3, Figure 1.

### Candidate statement

> Pending Human Adjudication: the arm-specific switching denominators total 74 while the prose reports 49 of 68 eligible failures, although the switching numerators and individual percentages reconcile.

### AI rationale

> Main Results calls 68 failures eligible while its switching fractions use 32+42=74; numerators sum correctly to 49. Article tables and flow provide the internal comparison.

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

> The prose gives 49 of 68 eligible patients, then 20/32 (62.5%) and 29/42 (69.0%). Table 2 gives 32 and 42 failures; Figure 1 gives 20 and 29 switches.

#### Evidence 1: Reported-versus-comparator

> The aggregate eligible denominator (68) is compared with the sum of the two printed arm denominators (32+42).

#### Evidence 2: Calculation

> 20+29=49; 32+42=74; 74−68=6. Individually, 20/32=62.5% and 29/42=69.05%, displayed as 69.0%.

#### Evidence 3: Alternative source-grounded interpretations

> The 32 and 42 may be all failures and 68 a narrower eligible subset; the original-arm allocation and reason for the six excluded failures are not supplied.

### Source links

- sourceLinks 0: [jama\_rathinam\_2019\_oi\_190092.pdf — PDF p. 7](../../../2019/jama.2019.12618/jama_rathinam_2019_oi_190092.pdf#page=7)
- sourceLinks 1: [jama\_rathinam\_2019\_oi\_190092.pdf — PDF p. 6, Table 2](../../../2019/jama.2019.12618/jama_rathinam_2019_oi_190092.pdf#page=6)
- sourceLinks 2: [jama\_rathinam\_2019\_oi\_190092.pdf — PDF p. 3, Figure 1](../../../2019/jama.2019.12618/jama_rathinam_2019_oi_190092.pdf#page=3)
- evidencePaths 0: [2019/jama.2019.12618/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.12618/.ai_paper_validation/review_1_5_1/source_inventory.md)

[Original Markdown report](../../../2019/jama.2019.12618/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | 68 could be a narrower eligible subset than all 74 failures, without supplied arm-specific exclusions. |
| broadPlanInvolved | 0 |
| category | Denominator, proportion, or total inconsistency |
| currentReportCrossDocument | 0 |
| id | C002 |
| key | 2019::jama.2019.12618::C002 |
| legacyRelationship |  |
| locations | jama\_rathinam\_2019\_oi\_190092.pdf — PDF p. 7; jama\_rathinam\_2019\_oi\_190092.pdf — PDF p. 6, Table 2; jama\_rathinam\_2019\_oi\_190092.pdf — PDF p. 3, Figure 1. |
| originalCrossDocument | 0 |
| package | jama.2019.12618 |
| planMechanism |  |
| primary | S\_W |
| rationale | Main Results calls 68 failures eligible while its switching fractions use 32+42=74; numerators sum correctly to 49. Article tables and flow provide the internal comparison. |
| reportHref | ../../2019/jama.2019.12618/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.12618/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | Pending Human Adjudication: the arm-specific switching denominators total 74 while the prose reports 49 of 68 eligible failures, although the switching numerators and individual percentages reconcile. |
| submissionInvolved | 1 |
| subtype | denominator\_definition |
| suggestedDomain | statistical\_results |
| title | eligible failure total vs switching denominators |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C003

**allocation block sizes**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.12618::C003 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> jama\_rathinam\_2019\_oi\_190092.pdf — PDF p. 2; joi190092supp2\_prod.pdf — PDF p. 13; joi190092supp3\_prod.pdf — PDF p. 9; joi190092supp3\_prod.pdf — PDF pp. 49–50 and p. 50.

### Candidate statement

> Pending Human Adjudication: matched trial allocation descriptions list different possible block-size sets.

### AI rationale

> Article block-size set {4,6} differs from the early protocol {4,6,8}. Later SAP 4/6 definitions support a possible version-specific explanation rather than an additional candidate discrepancy between plans.

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

> The article lists permutated block sizes 4 and 6. The protocol lists 4, 6, or 8 with equal probability. Later supplied SAP definitions specify 4 (probability 2/3) and 6 (probability 1/3).

#### Evidence 1: Reported-versus-comparator

> The article set {4,6} is compared with the protocol set {4,6,8}; the later SAP is alternative version-specific context rather than proof of the applied allocation list.

#### Evidence 2: Calculation

> {4,6} versus {4,6,8} has symmetric difference {8}.

#### Evidence 3: Alternative source-grounded interpretations

> A later amendment or implementation decision may have removed size 8, the article may describe realized rather than possible sizes, and the SAP's later 4/6 rule may govern the generated list.

### Source links

- sourceLinks 0: [jama\_rathinam\_2019\_oi\_190092.pdf — PDF p. 2](../../../2019/jama.2019.12618/jama_rathinam_2019_oi_190092.pdf#page=2)
- sourceLinks 1: [joi190092supp2\_prod.pdf — PDF p. 13](../../../2019/jama.2019.12618/joi190092supp2_prod.pdf#page=13)
- sourceLinks 2: [joi190092supp3\_prod.pdf — PDF p. 9](../../../2019/jama.2019.12618/joi190092supp3_prod.pdf#page=9)
- sourceLinks 3: [joi190092supp3\_prod.pdf — PDF pp. 49–50](../../../2019/jama.2019.12618/joi190092supp3_prod.pdf#page=49)
- sourceLinks 4: [p. 50](../../../2019/jama.2019.12618/joi190092supp3_prod.pdf#page=50)
- evidencePaths 0: [2019/jama.2019.12618/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.12618/.ai_paper_validation/review_1_5_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.12618/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.12618/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)
- evidencePaths 2: [2019/jama.2019.12618/.ai\_paper\_validation/review\_1\_5\_1/candidate\_ledger.md](../../../2019/jama.2019.12618/.ai_paper_validation/review_1_5_1/candidate_ledger.md)
- evidencePaths 3: [2019/jama.2019.12618/.ai\_paper\_validation/review\_1\_5\_1/preprocessing/protocol\_pp001\_032\_layout.txt](../../../2019/jama.2019.12618/.ai_paper_validation/review_1_5_1/preprocessing/protocol_pp001_032_layout.txt)
- evidencePaths 4: [2019/jama.2019.12618/.ai\_paper\_validation/review\_1\_5\_1/parts/support\_protocol\_pp001\_032.md](../../../2019/jama.2019.12618/.ai_paper_validation/review_1_5_1/parts/support_protocol_pp001_032.md)

[Original Markdown report](../../../2019/jama.2019.12618/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | The ledger explicitly records later SAP p9 and pp49–50 matching article sizes, with probabilities 2/3 and 1/3. This may be a legitimate supersession; it is not evidence of failed randomization. Document role checked: the bundle cover explicitly identifies original protocol, final protocol, and changes; its protocols are written in MOP format and contain full trial design and endpoint definitions. |
| broadPlanInvolved | 1 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C003 |
| key | 2019::jama.2019.12618::C003 |
| legacyRelationship |  |
| locations | jama\_rathinam\_2019\_oi\_190092.pdf — PDF p. 2; joi190092supp2\_prod.pdf — PDF p. 13; joi190092supp3\_prod.pdf — PDF p. 9; joi190092supp3\_prod.pdf — PDF pp. 49–50 and p. 50. |
| originalCrossDocument | 1 |
| package | jama.2019.12618 |
| planMechanism | analysis\_specification |
| primary | P\_R |
| rationale | Article block-size set {4,6} differs from the early protocol {4,6,8}. Later SAP 4/6 definitions support a possible version-specific explanation rather than an additional candidate discrepancy between plans. |
| reportHref | ../../2019/jama.2019.12618/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.12618/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | Pending Human Adjudication: matched trial allocation descriptions list different possible block-size sets. |
| submissionInvolved | 0 |
| subtype | randomization\_specification |
| suggestedDomain | protocol\_report |
| title | allocation block sizes |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | retain |

## Candidate C004

**six-month success injection-after-90-days criterion**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.12618::C004 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> jama\_rathinam\_2019\_oi\_190092.pdf — PDF p. 3; jama\_rathinam\_2019\_oi\_190092.pdf — PDF p. 6; joi190092supp2\_prod.pdf — PDF p. 80, §2.5.1; joi190092supp3\_prod.pdf — PDF p. 70.

### Candidate statement

> Pending Human Adjudication: the protocol manual includes a post-day-90 injection condition in six-month success, whereas the article's enumerated success definition omits it.

### AI rationale

> The supplied original/final protocol is authored as a Manual of Operations and Procedures. Its final v4.5 primary-endpoint definition requires no corticosteroid injection after day 90, while the article enumerated success definition omits that condition. This is a report-versus-protocol endpoint comparison, not merely a procedures annex assigned a plan role because of its filename.

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

> Protocol manual Version 4.5 requires no periocular or intravitreal corticosteroid injection after the first 90 days. The article's three-part success definition omits injection status, calls other injections protocol deviations, and reports four post-day-90 injections in each arm. The SAP sensitivity context on physical PDF p. 70 classifies an injection at 90 days using inflammation status at injection.

#### Evidence 1: Reported-versus-comparator

> The article's enumerated six-month success criteria are compared with the manual's explicit no-injection-after-90-days condition. The SAP text supplies context, not an established primary-analysis rule.

#### Evidence 2: Calculation

> The manual adds one explicit condition absent from the article's enumerated set. Eight reported cases are 4+4, but no revised 64/96 or 56/98 success count can be calculated.

#### Evidence 3: Alternative source-grounded interpretations

> The article may abbreviate an operational rule, protocol-deviation status may map to failure elsewhere, or an endpoint amendment may explain the difference. The SAP uses “90 days after enrollment”; a separate later deviation text uses \>90 days, so these are not silently normalized.

### Source links

- sourceLinks 0: [jama\_rathinam\_2019\_oi\_190092.pdf — PDF p. 3](../../../2019/jama.2019.12618/jama_rathinam_2019_oi_190092.pdf#page=3)
- sourceLinks 1: [jama\_rathinam\_2019\_oi\_190092.pdf — PDF p. 6](../../../2019/jama.2019.12618/jama_rathinam_2019_oi_190092.pdf#page=6)
- sourceLinks 2: [joi190092supp2\_prod.pdf — PDF p. 80, §2.5.1](../../../2019/jama.2019.12618/joi190092supp2_prod.pdf#page=80)
- sourceLinks 3: [joi190092supp3\_prod.pdf — PDF p. 70](../../../2019/jama.2019.12618/joi190092supp3_prod.pdf#page=70)
- evidencePaths 0: [2019/jama.2019.12618/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.12618/.ai_paper_validation/review_1_5_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.12618/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.12618/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)
- evidencePaths 2: [2019/jama.2019.12618/.ai\_paper\_validation/review\_1\_5\_1/candidate\_ledger.md](../../../2019/jama.2019.12618/.ai_paper_validation/review_1_5_1/candidate_ledger.md)
- evidencePaths 3: [2019/jama.2019.12618/.ai\_paper\_validation/review\_1\_5\_1/preprocessing/protocol\_pp001\_032\_layout.txt](../../../2019/jama.2019.12618/.ai_paper_validation/review_1_5_1/preprocessing/protocol_pp001_032_layout.txt)
- evidencePaths 4: [2019/jama.2019.12618/.ai\_paper\_validation/review\_1\_5\_1/parts/support\_protocol\_pp001\_032.md](../../../2019/jama.2019.12618/.ai_paper_validation/review_1_5_1/parts/support_protocol_pp001_032.md)
- evidencePaths 5: [2019/jama.2019.12618/.ai\_paper\_validation/review\_1\_5\_1/preprocessing/protocol\_pp065\_096\_layout.txt](../../../2019/jama.2019.12618/.ai_paper_validation/review_1_5_1/preprocessing/protocol_pp065_096_layout.txt)
- evidencePaths 6: [2019/jama.2019.12618/.ai\_paper\_validation/review\_1\_5\_1/parts/support\_protocol\_pp065\_096.md](../../../2019/jama.2019.12618/.ai_paper_validation/review_1_5_1/parts/support_protocol_pp065_096.md)
- evidencePaths 7: [2019/jama.2019.12618/.ai\_paper\_validation/review\_1\_5\_1/preprocessing/evidence\_recheck\_protocol\_p080.png](../../../2019/jama.2019.12618/.ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck_protocol_p080.png)

[Original Markdown report](../../../2019/jama.2019.12618/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Manual v4.5 may be abbreviated in the article or amended; eight reported injections cannot be translated into changed success counts. SAP sensitivity text is contextual, not a proven primary-rule discrepancy. Document role checked: the bundle cover explicitly identifies original protocol, final protocol, and changes; its protocols are written in MOP format and contain full trial design and endpoint definitions. |
| broadPlanInvolved | 1 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C004 |
| key | 2019::jama.2019.12618::C004 |
| legacyRelationship |  |
| locations | jama\_rathinam\_2019\_oi\_190092.pdf — PDF p. 3; jama\_rathinam\_2019\_oi\_190092.pdf — PDF p. 6; joi190092supp2\_prod.pdf — PDF p. 80, §2.5.1; joi190092supp3\_prod.pdf — PDF p. 70. |
| originalCrossDocument | 1 |
| package | jama.2019.12618 |
| planMechanism | endpoint\_definition\_window\_hierarchy |
| primary | P\_R |
| rationale | The supplied original/final protocol is authored as a Manual of Operations and Procedures. Its final v4.5 primary-endpoint definition requires no corticosteroid injection after day 90, while the article enumerated success definition omits that condition. This is a report-versus-protocol endpoint comparison, not merely a procedures annex assigned a plan role because of its filename. |
| reportHref | ../../2019/jama.2019.12618/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.12618/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C004 |
| sourceStatus | Pending Human Adjudication |
| statement | Pending Human Adjudication: the protocol manual includes a post-day-90 injection condition in six-month success, whereas the article's enumerated success definition omits it. |
| submissionInvolved | 0 |
| subtype | endpoint\_criterion\_omission |
| suggestedDomain | protocol\_report |
| title | six-month success injection-after-90-days criterion |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | retain |

## Candidate C005

**missed-dose Welch P=.87 compatibility**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.12618::C005 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> jama\_rathinam\_2019\_oi\_190092.pdf — PDF p. 4; jama\_rathinam\_2019\_oi\_190092.pdf — PDF p. 6, Table 2.

### Candidate statement

> Pending Human Adjudication: the reported P=.87 is not compatible with a conventional two-sided Welch calculation from the displayed missed-dose summaries and header sample sizes, subject to unreported analytic details.

### AI rationale

> Main Table 2 missed-dose means, SDs and header Ns plus main Welch-test method produce a diagnostic P around .0094, unlike printed .87. All discrepant inputs and claimed method are within the article.

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

> Table 2 prints MTX 4.6 (SD 1.0)% with n=96 and MMF 4.3 (SD 0.5)% with n=98, P=.87. Methods name a Welch t test for missed doses.

#### Evidence 1: Reported-versus-comparator

> The reported P=.87 is compared with a diagnostic conventional two-sample, two-sided Welch calculation using the displayed summaries and header n values.

#### Evidence 2: Calculation

> SE=sqrt(1.0²/96+0.5²/98)=0.113875753; difference =0.3; t=2.634450, approximately 139.06 Welch degrees of freedom; two-sided diagnostic P=0.009382747 (about .01), not .87.

#### Evidence 3: Alternative source-grounded interpretations

> Different analytic n, unrounded or transformed data, another summary definition, weighting, or a P value belonging to another comparison could explain the mismatch.

### Source links

- sourceLinks 0: [jama\_rathinam\_2019\_oi\_190092.pdf — PDF p. 4](../../../2019/jama.2019.12618/jama_rathinam_2019_oi_190092.pdf#page=4)
- sourceLinks 1: [jama\_rathinam\_2019\_oi\_190092.pdf — PDF p. 6, Table 2](../../../2019/jama.2019.12618/jama_rathinam_2019_oi_190092.pdf#page=6)
- evidencePaths 0: [2019/jama.2019.12618/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.12618/.ai_paper_validation/review_1_5_1/source_inventory.md)

[Original Markdown report](../../../2019/jama.2019.12618/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Row-specific N, SD meaning, transformation, or actual test output may differ from the reconstruction. |
| broadPlanInvolved | 0 |
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 0 |
| id | C005 |
| key | 2019::jama.2019.12618::C005 |
| legacyRelationship |  |
| locations | jama\_rathinam\_2019\_oi\_190092.pdf — PDF p. 4; jama\_rathinam\_2019\_oi\_190092.pdf — PDF p. 6, Table 2. |
| originalCrossDocument | 0 |
| package | jama.2019.12618 |
| planMechanism |  |
| primary | S\_W |
| rationale | Main Table 2 missed-dose means, SDs and header Ns plus main Welch-test method produce a diagnostic P around .0094, unlike printed .87. All discrepant inputs and claimed method are within the article. |
| reportHref | ../../2019/jama.2019.12618/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.12618/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C005 |
| sourceStatus | Pending Human Adjudication |
| statement | Pending Human Adjudication: the reported P=.87 is not compatible with a conventional two-sided Welch calculation from the displayed missed-dose summaries and header sample sizes, subject to unreported analytic details. |
| submissionInvolved | 1 |
| subtype | statistical\_compatibility |
| suggestedDomain | statistical\_results |
| title | missed-dose Welch P=.87 compatibility |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C006

**main Table 3 MMF n=109 header vs supplement N=108/percentages**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.12618::C006 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> jama\_rathinam\_2019\_oi\_190092.pdf — PDF p. 8, Table 3; joi190092supp1\_prod.pdf — PDF p. 10, eTable 4; joi190092supp1\_prod.pdf — PDF p. 11, eTable 5; joi190092supp1\_prod.pdf — PDF p. 12, eTable 6.

### Candidate statement

> Pending Human Adjudication: Main Table 3 uses an MMF header n=109 while its selected percentages reconcile to treated N=108, which matches Supplement 1 headers; the row-level denominator convention is implicit.

### AI rationale

> Main adverse-event Table 3 labels MMF n109 whereas results-supplement eTables4–6 label treated N108; main count/percent cells also imply 108. The target includes cross-file header discrepancy and a within-main header-versus-percentage check.

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

> Main Table 3 header is MMF n=109; it reports 19 (17.6) decreased/defective vision and 59 (54.6) fatigue, with a footnote that one assigned patient never received study drug. eTables 4–6 label treated MMF N=108. Only eTable 4 repeats the matched decreased/defective-vision cell 19 (17.6); the 59 (54.6) fatigue figure is an internal main-table denominator check, not an eTable 6 repeated cell.

#### Evidence 1: Reported-versus-comparator

> Main header n=109 and its count/percentage cells are compared with treated N=108 headers and the matched eTable 4 cell; the fatigue example is compared internally with its two possible denominators.

#### Evidence 2: Calculation

> 19/108=17.5926%→17.6%, versus 19/109=17.4312%→17.4%; 59/108=54.6296%→54.6%, versus 59/109=54.1284%→54.1%.

#### Evidence 3: Alternative source-grounded interpretations

> The header may intentionally report randomized N=109 while percentages use the 108 treated participants, signaled by the footnote but not stated as a row-level denominator convention.

### Source links

- sourceLinks 0: [jama\_rathinam\_2019\_oi\_190092.pdf — PDF p. 8, Table 3](../../../2019/jama.2019.12618/jama_rathinam_2019_oi_190092.pdf#page=8)
- sourceLinks 1: [joi190092supp1\_prod.pdf — PDF p. 10, eTable 4](../../../2019/jama.2019.12618/joi190092supp1_prod.pdf#page=10)
- sourceLinks 2: [joi190092supp1\_prod.pdf — PDF p. 11, eTable 5](../../../2019/jama.2019.12618/joi190092supp1_prod.pdf#page=11)
- sourceLinks 3: [joi190092supp1\_prod.pdf — PDF p. 12, eTable 6](../../../2019/jama.2019.12618/joi190092supp1_prod.pdf#page=12)
- evidencePaths 0: [2019/jama.2019.12618/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.12618/.ai_paper_validation/review_1_5_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.12618/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.12618/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2019/jama.2019.12618/.ai_paper_validation/final_report_1_5_1.md)

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
| ambiguity | The main footnote says one patient never received drug, so randomized header versus treated percentage convention may be intentional. Fatigue59(54.6) is internal only; eTable6 does not repeat it. |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C006 |
| key | 2019::jama.2019.12618::C006 |
| legacyRelationship |  |
| locations | jama\_rathinam\_2019\_oi\_190092.pdf — PDF p. 8, Table 3; joi190092supp1\_prod.pdf — PDF p. 10, eTable 4; joi190092supp1\_prod.pdf — PDF p. 11, eTable 5; joi190092supp1\_prod.pdf — PDF p. 12, eTable 6. |
| originalCrossDocument | 1 |
| package | jama.2019.12618 |
| planMechanism |  |
| primary | S\_C |
| rationale | Main adverse-event Table 3 labels MMF n109 whereas results-supplement eTables4–6 label treated N108; main count/percent cells also imply 108. The target includes cross-file header discrepancy and a within-main header-versus-percentage check. |
| reportHref | ../../2019/jama.2019.12618/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.12618/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C006 |
| sourceStatus | Pending Human Adjudication |
| statement | Pending Human Adjudication: Main Table 3 uses an MMF header n=109 while its selected percentages reconcile to treated N=108, which matches Supplement 1 headers; the row-level denominator convention is implicit. |
| submissionInvolved | 1 |
| subtype | denominator\_definition |
| suggestedDomain | report\_internal\_inconsistency |
| title | main Table 3 MMF n=109 header vs supplement N=108/percentages |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C007

**eTable 9 MMF serious diarrhea 1 (3.4) vs N=20**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.12618::C007 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> joi190092supp1\_prod.pdf — PDF p. 15, eTable 9, MMF N=20, Serious Systemic diarrhea row.

### Candidate statement

> Pending Human Adjudication: eTable 9 reports MMF N=20 and Serious Systemic diarrhea 1 (3.4), although the stated count-over-N rule yields 5.0% to one decimal.

### AI rationale

> One results-supplement eTable9 cell shows serious diarrhea1(3.4) in MMF N20; the same-table denominator gives5.0%. This is within one non-plan supplement.

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

> The table defines entries as patients reporting at least one event (%), labels MMF N=20, and prints 1 (3.4) for Serious Systemic diarrhea. Other N=20 count-one cells show 1 (5.0); N=29 MTX count-one cells show 1 (3.4).

#### Evidence 1: Reported-versus-comparator

> The displayed 3.4% is compared with the table's own N=20 denominator and count-over-denominator definition.

#### Evidence 2: Calculation

> 100×1/20=5.0%; 100×1/29=3.4483%, displayed as 3.4%.

#### Evidence 3: Alternative source-grounded interpretations

> The percentage may have been transposed from the N=29 column, the header/count may be wrong, or an unprinted subset near 29 may apply.

### Source links

- sourceLinks 0: [joi190092supp1\_prod.pdf — PDF p. 15, eTable 9](../../../2019/jama.2019.12618/joi190092supp1_prod.pdf#page=15)
- evidencePaths 0: [2019/jama.2019.12618/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.12618/.ai_paper_validation/review_1_5_1/source_inventory.md)

[Original Markdown report](../../../2019/jama.2019.12618/.ai_paper_validation/final_report_1_5_1.md)

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
| key | 2019::jama.2019.12618::C007 |
| legacyRelationship |  |
| locations | joi190092supp1\_prod.pdf — PDF p. 15, eTable 9, MMF N=20, Serious Systemic diarrhea row. |
| originalCrossDocument | 0 |
| package | jama.2019.12618 |
| planMechanism |  |
| primary | S\_W |
| rationale | One results-supplement eTable9 cell shows serious diarrhea1(3.4) in MMF N20; the same-table denominator gives5.0%. This is within one non-plan supplement. |
| reportHref | ../../2019/jama.2019.12618/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.12618/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C007 |
| sourceStatus | Pending Human Adjudication |
| statement | Pending Human Adjudication: eTable 9 reports MMF N=20 and Serious Systemic diarrhea 1 (3.4), although the stated count-over-N rule yields 5.0% to one decimal. |
| submissionInvolved | 1 |
| subtype | count\_percentage |
| suggestedDomain | statistical\_results |
| title | eTable 9 MMF serious diarrhea 1 (3.4) vs N=20 |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C008

**eTable 8 serious-ocular hypertension label vs eTable 1 surgery-required definition**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.12618::C008 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> joi190092supp1\_prod.pdf — PDF p. 5, eTable 1; joi190092supp1\_prod.pdf — PDF p. 14, eTable 8; joi190092supp1\_prod.pdf — PDF p. 15, eTable 9.

### Candidate statement

> Pending Human Adjudication: eTable 8 places “Ocular hypertension \>24mm Hg” in both non-serious and serious sections, whereas eTable 1 defines serious ocular hypertension as surgery required.

### AI rationale

> Results-supplement eTable8 serious ocular hypertension row uses \>24mmHg while eTable1 defines serious cases as surgery-required and eTable9 uses that label. All compared eTables belong to the same results supplement.

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

> eTable 1 classifies ocular hypertension at least 24 mm Hg as non-serious and surgery required (laser or incisional) as serious. eTable 8 repeats “Ocular hypertension \>24mm Hg” under both sections; the serious row is MTX 1 (1.6), MMF 0 (0.0). eTable 9 labels the serious row “Ocular hypertension, surgery required.”

#### Evidence 1: Reported-versus-comparator

> The eTable 8 serious-row label is compared with eTable 1's serious surgery-required criterion, eTable 8's own non-serious label, and eTable 9's surgery-required serious label.

#### Evidence 2: Calculation

> No percentage calculation applies. The serious eTable 8 row states a threshold-only criterion, while eTable 1 assigns threshold-only ocular hypertension to non-serious and surgery-required cases to serious; eTable 8 also uses \>24 where eTable 1 uses at least 24.

#### Evidence 3: Alternative source-grounded interpretations

> The serious event may have required surgery but have an abbreviated/copied label, or eTable 8 may use another unprinted definition. Its footnote points to eFigure 2, not eTable 1; no eFigure 2 content appears in the supplied supplement text.

### Source links

- sourceLinks 0: [joi190092supp1\_prod.pdf — PDF p. 5, eTable 1](../../../2019/jama.2019.12618/joi190092supp1_prod.pdf#page=5)
- sourceLinks 1: [joi190092supp1\_prod.pdf — PDF p. 14, eTable 8](../../../2019/jama.2019.12618/joi190092supp1_prod.pdf#page=14)
- sourceLinks 2: [joi190092supp1\_prod.pdf — PDF p. 15, eTable 9](../../../2019/jama.2019.12618/joi190092supp1_prod.pdf#page=15)
- evidencePaths 0: [2019/jama.2019.12618/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.12618/.ai_paper_validation/review_1_5_1/source_inventory.md)

[Original Markdown report](../../../2019/jama.2019.12618/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | A copied/abbreviated row label or an unprinted definition is possible; an unresolved eFigure2 footnote is not a second document. |
| broadPlanInvolved | 0 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C008 |
| key | 2019::jama.2019.12618::C008 |
| legacyRelationship |  |
| locations | joi190092supp1\_prod.pdf — PDF p. 5, eTable 1; joi190092supp1\_prod.pdf — PDF p. 14, eTable 8; joi190092supp1\_prod.pdf — PDF p. 15, eTable 9. |
| originalCrossDocument | 0 |
| package | jama.2019.12618 |
| planMechanism |  |
| primary | S\_W |
| rationale | Results-supplement eTable8 serious ocular hypertension row uses \>24mmHg while eTable1 defines serious cases as surgery-required and eTable9 uses that label. All compared eTables belong to the same results supplement. |
| reportHref | ../../2019/jama.2019.12618/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.12618/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C008 |
| sourceStatus | Pending Human Adjudication |
| statement | Pending Human Adjudication: eTable 8 places “Ocular hypertension \>24mm Hg” in both non-serious and serious sections, whereas eTable 1 defines serious ocular hypertension as surgery required. |
| submissionInvolved | 1 |
| subtype | outcome\_severity\_label |
| suggestedDomain | report\_internal\_inconsistency |
| title | eTable 8 serious-ocular hypertension label vs eTable 1 surgery-required definition |
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
