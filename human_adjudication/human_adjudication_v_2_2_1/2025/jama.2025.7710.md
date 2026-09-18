# jama.2025.7710

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2025 |
| Paper | jama.2025.7710 |
| Candidates | 4 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2025/jama.2025.7710/)

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

- [C001](#candidate-c001) — Conflicting economic price-year labels within the protocol (P_P)
- [C002](#candidate-c002) — Primary-composite counting rationale does not reconcile with the displayed endpoint list (P_P)
- [C003](#candidate-c003) — Economic comparator label conflicts with the detailed trial comparison (P_P)
- [C004](#candidate-c004) — Reported no-adjustment statement conflicts with the supplied multiplicity plan (P_R)

## Candidate C001

**Conflicting economic price-year labels within the protocol**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.7710::C001 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> joi250034supp1\_prod\_1750956984.09018.pdf — PDF p. 16, section 7.2.3; joi250034supp1\_prod\_1750956984.09018.pdf — PDF p. 17, section 8.2.

### Candidate statement

> Two linked protocol descriptions of the economic-analysis framework state different monetary price years.

### AI rationale

> Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator. Reported: 2024/25 dollars (p. 16). Comparator: 2023/24 dollars (p. 17).

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

> Section 7.2.3 states that all costs will be presented in 2024/25 dollars, with no discounting, for a payer-perspective one-year cost-utility analysis and five-year budget-impact analysis. Section 8.2 describes the same perspective, horizons, and no-discounting statement but says all costs will be presented in 2023/24 dollars.

#### Evidence 1: Reported-versus-comparator

> Reported: 2024/25 dollars (p. 16). Comparator: 2023/24 dollars (p. 17).

#### Evidence 2: Calculation

> 2024/25 is not equal to 2023/24; no rounding or transformation is involved.

#### Evidence 3: Alternative source-grounded interpretations

> One section may retain wording from an intended price-year update, or the sections may have meant different explicitly converted analyses. The supplied protocol neither identifies a superseded section nor distinguishes separate price-year conventions.

### Source links

- sourceLinks 0: [joi250034supp1\_prod\_1750956984.09018.pdf — PDF p. 16, section 7.2.3](../../../2025/jama.2025.7710/joi250034supp1_prod_1750956984.09018.pdf#page=16)
- sourceLinks 1: [joi250034supp1\_prod\_1750956984.09018.pdf — PDF p. 17, section 8.2](../../../2025/jama.2025.7710/joi250034supp1_prod_1750956984.09018.pdf#page=17)

[Original Markdown report](../../../2025/jama.2025.7710/.ai_paper_validation/final_report_1_5_1.md)

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
| id | C001 |
| key | 2025::jama.2025.7710::C001 |
| legacyRelationship |  |
| locations | joi250034supp1\_prod\_1750956984.09018.pdf — PDF p. 16, section 7.2.3; joi250034supp1\_prod\_1750956984.09018.pdf — PDF p. 17, section 8.2. |
| originalCrossDocument | 0 |
| package | jama.2025.7710 |
| planMechanism |  |
| primary | P\_P |
| rationale | Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator. Reported: 2024/25 dollars (p. 16). Comparator: 2023/24 dollars (p. 17). |
| reportHref | ../../2025/jama.2025.7710/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.7710/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | Two linked protocol descriptions of the economic-analysis framework state different monetary price years. |
| submissionInvolved | 0 |
| subtype | Conflicting economic price-year labels within the protocol |
| suggestedDomain | plan\_material |
| title | Conflicting economic price-year labels within the protocol |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C002

**Primary-composite counting rationale does not reconcile with the displayed endpoint list**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.7710::C002 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> joi250034supp1\_prod\_1750956984.09018.pdf — PDF p. 15, section 7.1; joi250034supp1\_prod\_1750956984.09018.pdf — PDF p. 16, section 7.2.1.

### Candidate statement

> The protocol displays ten separate endpoint bullets but explains a total of ten by saying two listed outcomes each contain two individual components.

### AI rationale

> Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator. Reported list: ten displayed bullets. Comparator rationale: a total of ten attributed to expanding outcomes (i) and (viii).

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

> Page 15 displays ten separate primary-composite endpoint bullets. Page 16 states, “There are ten items because outcomes (i) and (viii) each contain two individual components.” Section 7.1.1 groups intrapartum stillbirth with 28-day neonatal death, while 7.1.2 separately defines 28-day neonatal mortality; the eighth bullet names Special Care or Intensive Care within one neonatal-unit-admission endpoint.

#### Evidence 1: Reported-versus-comparator

> Reported list: ten displayed bullets. Comparator rationale: a total of ten attributed to expanding outcomes (i) and (viii).

#### Evidence 2: Calculation

> Displayed count = 10. Under the conditional reading that two already displayed items are each expanded from one to two components, 10 + 1 + 1 = 12. An 8 + 1 + 1 = 10 reconciliation would require an authoritative eight-group starting list, which is not displayed at the cited locations.

#### Evidence 3: Alternative source-grounded interpretations

> The 7.1.1 heading and Special Care/Intensive Care wording could reflect an older or unstated eight-group structure. That structure is not the displayed ten-bullet list, and the supplied materials do not provide a definitive numbered taxonomy.

### Source links

- sourceLinks 0: [joi250034supp1\_prod\_1750956984.09018.pdf — PDF p. 15, section 7.1](../../../2025/jama.2025.7710/joi250034supp1_prod_1750956984.09018.pdf#page=15)
- sourceLinks 1: [joi250034supp1\_prod\_1750956984.09018.pdf — PDF p. 16, section 7.2.1](../../../2025/jama.2025.7710/joi250034supp1_prod_1750956984.09018.pdf#page=16)

[Original Markdown report](../../../2025/jama.2025.7710/.ai_paper_validation/final_report_1_5_1.md)

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
| id | C002 |
| key | 2025::jama.2025.7710::C002 |
| legacyRelationship |  |
| locations | joi250034supp1\_prod\_1750956984.09018.pdf — PDF p. 15, section 7.1; joi250034supp1\_prod\_1750956984.09018.pdf — PDF p. 16, section 7.2.1. |
| originalCrossDocument | 0 |
| package | jama.2025.7710 |
| planMechanism |  |
| primary | P\_P |
| rationale | Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator. Reported list: ten displayed bullets. Comparator rationale: a total of ten attributed to expanding outcomes (i) and (viii). |
| reportHref | ../../2025/jama.2025.7710/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.7710/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | The protocol displays ten separate endpoint bullets but explains a total of ten by saying two listed outcomes each contain two individual components. |
| submissionInvolved | 0 |
| subtype | Primary-composite counting rationale does not reconcile with the displayed endpoint list |
| suggestedDomain | plan\_material |
| title | Primary-composite counting rationale does not reconcile with the displayed endpoint list |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C003

**Economic comparator label conflicts with the detailed trial comparison**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.7710::C003 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> joi250034supp1\_prod\_1750956984.09018.pdf — PDF p. 5, synopsis and schema; joi250034supp1\_prod\_1750956984.09018.pdf — PDF p. 16, section 7.2.3; joi250034supp1\_prod\_1750956984.09018.pdf — PDF p. 17, section 8.2.

### Candidate statement

> A protocol economic-analysis label uses CS vs standard care, while the detailed economic comparison and trial synopsis identify sildenafil citrate (SC) versus placebo/standard care.

### AI rationale

> Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator. Reported economic label: \`CS vs standard care\`. Comparator description: \`SC\` versus placebo/standard care.

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

> Page 16 describes cost effectiveness and budget impact of CS vs standard care. Page 17 specifies treatment with SC versus placebo (standard of care). The synopsis defines SC as sildenafil citrate, CS as caesarean section, the study treatment as 50 mg SC, and the control as matching placebo.

#### Evidence 1: Reported-versus-comparator

> Reported economic label: CS vs standard care. Comparator description: SC versus placebo/standard care.

#### Evidence 2: Calculation

> Supplied mappings are SC = sildenafil citrate, CS = caesarean section, and control = matching placebo. Thus CS does not denote the same supplied intervention label as SC.

#### Evidence 3: Alternative source-grounded interpretations

> CS may be a transposition of SC, a locally intended abbreviation not defined at the cited location, or an insufficiently explained comparison. No completed economic analysis is supplied.

### Source links

- sourceLinks 0: [joi250034supp1\_prod\_1750956984.09018.pdf — PDF p. 5, synopsis and schema](../../../2025/jama.2025.7710/joi250034supp1_prod_1750956984.09018.pdf#page=5)
- sourceLinks 1: [joi250034supp1\_prod\_1750956984.09018.pdf — PDF p. 16, section 7.2.3](../../../2025/jama.2025.7710/joi250034supp1_prod_1750956984.09018.pdf#page=16)
- sourceLinks 2: [joi250034supp1\_prod\_1750956984.09018.pdf — PDF p. 17, section 8.2](../../../2025/jama.2025.7710/joi250034supp1_prod_1750956984.09018.pdf#page=17)

[Original Markdown report](../../../2025/jama.2025.7710/.ai_paper_validation/final_report_1_5_1.md)

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
| key | 2025::jama.2025.7710::C003 |
| legacyRelationship |  |
| locations | joi250034supp1\_prod\_1750956984.09018.pdf — PDF p. 5, synopsis and schema; joi250034supp1\_prod\_1750956984.09018.pdf — PDF p. 16, section 7.2.3; joi250034supp1\_prod\_1750956984.09018.pdf — PDF p. 17, section 8.2. |
| originalCrossDocument | 0 |
| package | jama.2025.7710 |
| planMechanism |  |
| primary | P\_P |
| rationale | Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator. Reported economic label: \`CS vs standard care\`. Comparator description: \`SC\` versus placebo/standard care. |
| reportHref | ../../2025/jama.2025.7710/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.7710/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | A protocol economic-analysis label uses CS vs standard care, while the detailed economic comparison and trial synopsis identify sildenafil citrate (SC) versus placebo/standard care. |
| submissionInvolved | 0 |
| subtype | Economic comparator label conflicts with the detailed trial comparison |
| suggestedDomain | plan\_material |
| title | Economic comparator label conflicts with the detailed trial comparison |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C004

**Reported no-adjustment statement conflicts with the supplied multiplicity plan**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.7710::C004 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> jama\_kumar\_2025\_oi\_250034\_1750956984.08518.pdf — PDF p. 4, Statistical Analysis; jama\_kumar\_2025\_oi\_250034\_1750956984.08518.pdf — PDF p. 7, Table 3; joi250034supp1\_prod\_1750956984.09018.pdf — PDF p. 20, section 13.2; joi250034supp2\_prod\_1750956984.11521.pdf — PDF p. 12, section 3.2; joi250034supp2\_prod\_1750956984.11521.pdf — PDF p. 25, proposed Table 11.

### Candidate statement

> The article reports no adjustment for multiple testing, while the supplied protocol and draft SAP plan Benjamini-Hochberg adjusted P values for the ten component comparisons.

### AI rationale

> Target compares reported current-study content with supplied protocol/SAP specification. Reported multiplicity treatment: no adjustment. Comparator planned treatment: adjusted P values for ten component comparisons.

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

> The article states, “There was no adjustment for multiple testing,” and its Table 3 displays ten component rows with one P-value column. The protocol and draft SAP state that adjusted P values for ten component comparisons will be derived using the Benjamin-Hochberg procedure; the SAP shell includes separate P-value and adjusted-P-value columns. The SAP identifies itself as Draft Version 1.2 on p. 1.

#### Evidence 1: Reported-versus-comparator

> Reported multiplicity treatment: no adjustment. Comparator planned treatment: adjusted P values for ten component comparisons.

#### Evidence 2: Calculation

> Article: adjustment applied = no. Protocol/draft SAP: adjusted P values for 10 component comparisons = planned; the SAP Table 11 shell allocates an adjusted-P-value column. These descriptions cannot both be the implemented treatment for the same comparisons without a superseding plan decision or a narrower scope for the article statement.

#### Evidence 3: Alternative source-grounded interpretations

> A final approved SAP, amendment, or documented pre-unblinding decision may have superseded the supplied draft plan. The article notes an interpretive approach to interrelated secondary outcomes, but does not state that the planned adjustment was superseded. Raw P values are not thereby arithmetically invalid.

### Source links

- sourceLinks 0: [jama\_kumar\_2025\_oi\_250034\_1750956984.08518.pdf — PDF p. 4, Statistical Analysis](../../../2025/jama.2025.7710/jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=4)
- sourceLinks 1: [jama\_kumar\_2025\_oi\_250034\_1750956984.08518.pdf — PDF p. 7, Table 3](../../../2025/jama.2025.7710/jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=7)
- sourceLinks 2: [joi250034supp1\_prod\_1750956984.09018.pdf — PDF p. 20, section 13.2](../../../2025/jama.2025.7710/joi250034supp1_prod_1750956984.09018.pdf#page=20)
- sourceLinks 3: [joi250034supp2\_prod\_1750956984.11521.pdf — PDF p. 12, section 3.2](../../../2025/jama.2025.7710/joi250034supp2_prod_1750956984.11521.pdf#page=12)
- sourceLinks 4: [joi250034supp2\_prod\_1750956984.11521.pdf — PDF p. 25, proposed Table 11](../../../2025/jama.2025.7710/joi250034supp2_prod_1750956984.11521.pdf#page=25)
- evidencePaths 0: [2025/jama.2025.7710/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.7710/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2025.7710/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | SAP expressly Draft v1.2; final approved plan/amendment missing. No-adjustment versus planned BH remains candidate governance question. |
| broadPlanInvolved | 1 |
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 1 |
| id | C004 |
| key | 2025::jama.2025.7710::C004 |
| legacyRelationship |  |
| locations | jama\_kumar\_2025\_oi\_250034\_1750956984.08518.pdf — PDF p. 4, Statistical Analysis; jama\_kumar\_2025\_oi\_250034\_1750956984.08518.pdf — PDF p. 7, Table 3; joi250034supp1\_prod\_1750956984.09018.pdf — PDF p. 20, section 13.2; joi250034supp2\_prod\_1750956984.11521.pdf — PDF p. 12, section 3.2; joi250034supp2\_prod\_1750956984.11521.pdf — PDF p. 25, proposed Table 11. |
| originalCrossDocument | 0 |
| package | jama.2025.7710 |
| planMechanism | analysis\_specification |
| primary | P\_R |
| rationale | Target compares reported current-study content with supplied protocol/SAP specification. Reported multiplicity treatment: no adjustment. Comparator planned treatment: adjusted P values for ten component comparisons. |
| reportHref | ../../2025/jama.2025.7710/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.7710/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C004 |
| sourceStatus | Pending Human Adjudication |
| statement | The article reports no adjustment for multiple testing, while the supplied protocol and draft SAP plan Benjamini-Hochberg adjusted P values for the ten component comparisons. |
| submissionInvolved | 0 |
| subtype | Reported no-adjustment statement conflicts with the supplied multiplicity plan |
| suggestedDomain | protocol\_report |
| title | Reported no-adjustment statement conflicts with the supplied multiplicity plan |
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
