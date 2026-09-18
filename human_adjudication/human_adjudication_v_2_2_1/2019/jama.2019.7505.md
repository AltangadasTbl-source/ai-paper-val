# jama.2019.7505

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2019 |
| Paper | jama.2019.7505 |
| Candidates | 4 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2019/jama.2019.7505/)

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

- [C001](#candidate-c001) — Hypoxemia confidence-interval endpoint sign differs between abstract and Table 3 (S_W)
- [C002](#candidate-c002) — DIC row finite risk ratio and narrow interval do not reconcile with zero comparator events (S_W)
- [C003](#candidate-c003) — Protocol analysis sentence combines odds-ratio and relative-risk labels (P_P)
- [C004](#candidate-c004) — eFigure 11 mortality values are described as extra-pulmonary complications (S_W)

## Candidate C001

**Hypoxemia confidence-interval endpoint sign differs between abstract and Table 3**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.7505::C001 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-001, jama\_bluth\_2019\_oi\_190055\_16092.pdf — PDF p. 1, abstract and PDF p. 9, Table 3.

### Candidate statement

> The abstract and Table 3 print opposite signs for the upper endpoint of the otherwise matched high-minus-low hypoxemia risk-difference confidence interval.

### AI rationale

> Main abstract hypoxemia risk-difference CI upper endpoint+6.1 conflicts with main Table3 -6.1 for the same counts, estimate and P. Both locations are in one article, despite original cross-document category.

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

> Both locations report intraoperative hypoxemia of 49/989 (5.0%) versus 134/987 (13.6%), a difference of -8.6 percentage points, and P \< .001. The abstract prints 95% CI -11.1 to +6.1; Table 3 prints -11.1 to -6.1 and RR 0.51 (0.40 to 0.65).

#### Evidence 1: Reported-versus-comparator

> Abstract upper endpoint +6.1 versus Table 3 upper endpoint -6.1 for the same matched result.

#### Evidence 2: Calculation

> 5.0 - 13.6 = -8.6 percentage points. The printed upper endpoint changes by 12.2 percentage points. A direct unpooled Wald calculation from the displayed counts is a diagnostic approximation of about -11.15 to -6.09 percentage points; it supports Table 3's displayed precision but does not determine which source should be corrected.

#### Evidence 3: Alternative source-grounded interpretations

> Either the abstract or Table 3 may contain the production error. A dropped abstract minus sign is plausible, but the package does not provide an authoritative analysis-output record or designate an authoritative display.

### Source links

- sourceLinks 0: [jama\_bluth\_2019\_oi\_190055\_16092.pdf — PDF p. 1, abstract](../../../2019/jama.2019.7505/jama_bluth_2019_oi_190055_16092.pdf#page=1)
- sourceLinks 1: [PDF p. 9, Table 3](../../../2019/jama.2019.7505/jama_bluth_2019_oi_190055_16092.pdf#page=9)
- evidencePaths 0: [2019/jama.2019.7505/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2019/jama.2019.7505/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2019/jama.2019.7505/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C001 |
| key | 2019::jama.2019.7505::C001 |
| legacyRelationship |  |
| locations | DOC-001, jama\_bluth\_2019\_oi\_190055\_16092.pdf — PDF p. 1, abstract and PDF p. 9, Table 3. |
| originalCrossDocument | 1 |
| package | jama.2019.7505 |
| planMechanism |  |
| primary | S\_W |
| rationale | Main abstract hypoxemia risk-difference CI upper endpoint+6.1 conflicts with main Table3 -6.1 for the same counts, estimate and P. Both locations are in one article, despite original cross-document category. |
| reportHref | ../../2019/jama.2019.7505/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2019/jama.2019.7505/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | The abstract and Table 3 print opposite signs for the upper endpoint of the otherwise matched high-minus-low hypoxemia risk-difference confidence interval. |
| submissionInvolved | 1 |
| subtype | ci\_sign |
| suggestedDomain | report\_internal\_inconsistency |
| title | Hypoxemia confidence-interval endpoint sign differs between abstract and Table 3 |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C002

**DIC row finite risk ratio and narrow interval do not reconcile with zero comparator events**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.7505::C002 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001, jama\_bluth\_2019\_oi\_190055\_16092.pdf — PDF p. 9, Table 3; PDF p. 10, continued Table 3 footnotes; and PDF p. 4, binary-outcome method.

### Candidate statement

> The Table 3 DIC row prints 1 versus 0 events but a finite RR 2.00 with a narrow interval excluding 1; the source does not supply the estimator needed to reconcile these values.

### AI rationale

> Main Table3 DIC row shows1 versus0 events alongside finite RR2.00 and narrow CI1.91–2.09/P\>.99; main methods lack the zero-cell rule needed to reconcile that display.

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

> The row prints disseminated intravascular coagulation as 1/989 (0.1%) versus 0/987, absolute difference 0.1 (95% CI -0.1 to 0.3), RR 2.00 (95% CI 1.91 to 2.09), and P \> .99. Table footnotes label the effect as a risk ratio and identify broad interval/test methods.

#### Evidence 1: Reported-versus-comparator

> A finite RR 2.00 with interval \[1.91, 2.09\] is displayed against a comparator risk of zero; the same row prints P \> .99.

#### Evidence 2: Calculation

> High risk = 1/989 = 0.0010111; low risk = 0/987 = 0. Thus (1/989)/(0/987) has a zero denominator and is not a finite direct RR. The printed interval excludes 1. No replacement RR, CI, or P value is calculated.

#### Evidence 3: Alternative source-grounded interpretations

> An unstated zero-cell correction, alternate estimator, cell alignment issue, or transcription error could explain part of the display. The supplied package does not identify a zero-cell rule, exact interval formula/software call, chi-square variant, or row-specific alternate population.

### Source links

- sourceLinks 0: [jama\_bluth\_2019\_oi\_190055\_16092.pdf — PDF p. 9, Table 3](../../../2019/jama.2019.7505/jama_bluth_2019_oi_190055_16092.pdf#page=9)
- sourceLinks 1: [PDF p. 10, continued Table 3 footnotes](../../../2019/jama.2019.7505/jama_bluth_2019_oi_190055_16092.pdf#page=10)
- sourceLinks 2: [PDF p. 4, binary-outcome method](../../../2019/jama.2019.7505/jama_bluth_2019_oi_190055_16092.pdf#page=4)
- evidencePaths 0: [2019/jama.2019.7505/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2019/jama.2019.7505/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2019/jama.2019.7505/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | An unstated zero-cell estimator, alternate method, or cell alignment may partly explain it; no replacement RR is asserted. |
| broadPlanInvolved | 0 |
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 0 |
| id | C002 |
| key | 2019::jama.2019.7505::C002 |
| legacyRelationship |  |
| locations | DOC-001, jama\_bluth\_2019\_oi\_190055\_16092.pdf — PDF p. 9, Table 3; PDF p. 10, continued Table 3 footnotes; and PDF p. 4, binary-outcome method. |
| originalCrossDocument | 0 |
| package | jama.2019.7505 |
| planMechanism |  |
| primary | S\_W |
| rationale | Main Table3 DIC row shows1 versus0 events alongside finite RR2.00 and narrow CI1.91–2.09/P\>.99; main methods lack the zero-cell rule needed to reconcile that display. |
| reportHref | ../../2019/jama.2019.7505/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2019/jama.2019.7505/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | The Table 3 DIC row prints 1 versus 0 events but a finite RR 2.00 with a narrow interval excluding 1; the source does not supply the estimator needed to reconcile these values. |
| submissionInvolved | 1 |
| subtype | statistical\_compatibility |
| suggestedDomain | statistical\_results |
| title | DIC row finite risk ratio and narrow interval do not reconcile with zero comparator events |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C003

**Protocol analysis sentence combines odds-ratio and relative-risk labels**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.7505::C003 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> DOC-002, joi190055supp1\_prod\_16092.pdf — physical PDF p. 23 (footer p. 22), section 8.2 Analysis; comparator definitions in DOC-004, joi190055supp3\_prod\_16092.pdf — PDF p. 2 and PDF p. 3.

### Candidate statement

> A protocol planned-analysis sentence joins “odds ratio” and “relative risks” without a separator, alternative-analysis definition, or conversion rule, while the final SAP specifies a primary risk ratio.

### AI rationale

> Protocol planned-analysis sentence combines odds ratio and relative risks without separation; final SAP separately specifies primary RR and exploratory OR. Both the indeterminate sentence and comparator are prospective planning documents, not reported results.

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

> DOC-002 states that “the odds ratio relative risks with corresponding 95% confidence levels interval” will be calculated using logistic regression. DOC-004 identifies the primary effect as a risk ratio and separately uses odds ratios for specified exploratory analyses.

#### Evidence 1: Reported-versus-comparator

> The uninterrupted compound protocol label “odds ratio relative risks” versus the final SAP's explicit primary-outcome risk-ratio label and distinct exploratory odds-ratio contexts.

#### Evidence 2: Calculation

> No arithmetic is needed. The reproducible comparison is the uninterrupted compound label against the SAP's measure-specific wording.

#### Evidence 3: Alternative source-grounded interpretations

> The phrase may be an editing artifact; the final SAP may supersede earlier wording by selecting risk ratio for the primary outcome; or distinct analyses may have been intended. The package does not resolve which explanation applies.

### Source links

- sourceLinks 0: [joi190055supp1\_prod\_16092.pdf — physical PDF p. 23 (footer p. 22), section 8.2 Analysis](../../../2019/jama.2019.7505/joi190055supp1_prod_16092.pdf#page=23)
- sourceLinks 1: [joi190055supp3\_prod\_16092.pdf — PDF p. 2](../../../2019/jama.2019.7505/joi190055supp3_prod_16092.pdf#page=2)
- sourceLinks 2: [PDF p. 3](../../../2019/jama.2019.7505/joi190055supp3_prod_16092.pdf#page=3)
- evidencePaths 0: [2019/jama.2019.7505/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2019/jama.2019.7505/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.7505/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2019/jama.2019.7505/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)

[Original Markdown report](../../../2019/jama.2019.7505/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_P |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Later SAP may legitimately supersede preliminary wording; the unresolved compound phrase is a planning-text issue. |
| broadPlanInvolved | 1 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C003 |
| key | 2019::jama.2019.7505::C003 |
| legacyRelationship |  |
| locations | DOC-002, joi190055supp1\_prod\_16092.pdf — physical PDF p. 23 (footer p. 22), section 8.2 Analysis; comparator definitions in DOC-004, joi190055supp3\_prod\_16092.pdf — PDF p. 2 and PDF p. 3. |
| originalCrossDocument | 0 |
| package | jama.2019.7505 |
| planMechanism |  |
| primary | P\_P |
| rationale | Protocol planned-analysis sentence combines odds ratio and relative risks without separation; final SAP separately specifies primary RR and exploratory OR. Both the indeterminate sentence and comparator are prospective planning documents, not reported results. |
| reportHref | ../../2019/jama.2019.7505/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2019/jama.2019.7505/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | A protocol planned-analysis sentence joins “odds ratio” and “relative risks” without a separator, alternative-analysis definition, or conversion rule, while the final SAP specifies a primary risk ratio. |
| submissionInvolved | 0 |
| subtype | effect\_measure\_label |
| suggestedDomain | plan\_material |
| title | Protocol analysis sentence combines odds-ratio and relative-risk labels |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C004

**eFigure 11 mortality values are described as extra-pulmonary complications**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.7505::C004 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-005, joi190055supp4\_prod\_16092.pdf — PDF p. 41, eFigure 11; comparator PDF p. 40, eFigure 10; and DOC-001, jama\_bluth\_2019\_oi\_190055\_16092.pdf — PDF p. 10, Table 3.

### Candidate statement

> eFigure 11's narrative calls its displayed mortality values postoperative extra-pulmonary complications, although its title, axis, effect label, and matching Table 3 values identify five-day mortality.

### AI rationale

> Results-supplement eFigure11 narrative calls its own mortality values extra-pulmonary complications despite mortality title/axis/effect label; neighboring eFigure10 provides a distinct complication rate. Main Table3 agrees with mortality and merely corroborates the internal caption defect.

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

> eFigure 11 is titled “Probability of death in the first 5 postoperative days,” labels the effect “hazard ratio for 5-day mortality,” and prints 0.5% versus 0.3%, HR 1.67 (0.40 to 6.97), P = .484. Its narrative calls those same values “the rate of postoperative extra-pulmonary complications.” eFigure 10 separately prints extra-pulmonary complications of 16.9% versus 15.2%, HR 1.12; Table 3 matches the eFigure 11 mortality values.

#### Evidence 1: Reported-versus-comparator

> The eFigure 11 narrative outcome noun conflicts with its mortality title, axis, effect label, and matched mortality values; eFigure 10 supplies the distinct extra-pulmonary-complication comparator.

#### Evidence 2: Calculation

> 5/989 = 0.5056% and 3/987 = 0.3040%, rounding to 0.5% and 0.3%. These mortality values are not rounding variants of the separately displayed 16.9% and 15.2% extra-pulmonary-complication values.

#### Evidence 3: Alternative source-grounded interpretations

> Carry-forward wording from neighboring eFigure 10 is plausible, or the sentence may refer to a neighboring figure, but neither explanation is stated in the supplied sources.

### Source links

- sourceLinks 0: [joi190055supp4\_prod\_16092.pdf — PDF p. 41, eFigure 11](../../../2019/jama.2019.7505/joi190055supp4_prod_16092.pdf#page=41)
- sourceLinks 1: [PDF p. 40, eFigure 10](../../../2019/jama.2019.7505/joi190055supp4_prod_16092.pdf#page=40)
- sourceLinks 2: [jama\_bluth\_2019\_oi\_190055\_16092.pdf — PDF p. 10, Table 3](../../../2019/jama.2019.7505/jama_bluth_2019_oi_190055_16092.pdf#page=10)
- evidencePaths 0: [2019/jama.2019.7505/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2019/jama.2019.7505/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.7505/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2019/jama.2019.7505/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)

[Original Markdown report](../../../2019/jama.2019.7505/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C004 |
| key | 2019::jama.2019.7505::C004 |
| legacyRelationship |  |
| locations | DOC-005, joi190055supp4\_prod\_16092.pdf — PDF p. 41, eFigure 11; comparator PDF p. 40, eFigure 10; and DOC-001, jama\_bluth\_2019\_oi\_190055\_16092.pdf — PDF p. 10, Table 3. |
| originalCrossDocument | 0 |
| package | jama.2019.7505 |
| planMechanism |  |
| primary | S\_W |
| rationale | Results-supplement eFigure11 narrative calls its own mortality values extra-pulmonary complications despite mortality title/axis/effect label; neighboring eFigure10 provides a distinct complication rate. Main Table3 agrees with mortality and merely corroborates the internal caption defect. |
| reportHref | ../../2019/jama.2019.7505/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2019/jama.2019.7505/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C004 |
| sourceStatus | Pending Human Adjudication |
| statement | eFigure 11's narrative calls its displayed mortality values postoperative extra-pulmonary complications, although its title, axis, effect label, and matching Table 3 values identify five-day mortality. |
| submissionInvolved | 1 |
| subtype | outcome\_label |
| suggestedDomain | report\_internal\_inconsistency |
| title | eFigure 11 mortality values are described as extra-pulmonary complications |
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
