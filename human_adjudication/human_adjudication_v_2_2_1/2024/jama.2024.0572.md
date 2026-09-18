# jama.2024.0572

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2024 |
| Paper | jama.2024.0572 |
| Candidates | 2 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2024/jama.2024.0572/)

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

- [C001](#candidate-c001) — ITT Figure 2 mRS distributions conflict with ITT eTable 2 threshold counts (S_C)
- [C002](#candidate-c002) — aRR is labeled as an absolute risk reduction but displayed and interpreted as a ratio (S_W)

## Candidate C001

**ITT Figure 2 mRS distributions conflict with ITT eTable 2 threshold counts**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.0572::C001 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> Main article Figure 2 — PDF p. 7; Supplement 5 eTable 2 — PDF p. 38; main Results population statement — PDF p. 4; and Supplement 5 eFigure 3 — PDF p. 8.

### Candidate statement

> The Figure 2 ITT 90-day mRS distributions and Supplement 5 eTable 2 ITT threshold counts do not reconcile under ordinary nearest-whole-percentage rounding, despite matching ITT labels and 168 participants per arm.

### AI rationale

> Main Figure2 ITT mRS distributions reconstruct different threshold counts from results-supplement eTable2 despite matched168-per-arm labels.

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

> Figure 2 is titled as an intention-to-treat 90-day mRS distribution. Its core-stratum denominators total EVT 117+51=168 and medical management (MM) 119+49=168. eTable 2 is also explicitly ITT with EVT N=168 and MM N=168, and prints mRS 0-2 as 34/168 and 12/168, mRS 0-3 as 65/168 and 31/168, and mRS 5-6 as 76/168 and 102/168, respectively.

#### Evidence 1: Reported-versus-comparator

> From Figure 2's printed percentages and denominators, the uniquely feasible mRS 0-6 counts are EVT \<100 mL \[2, 7, 21, 26, 17, 9, 35\], EVT \>=100 mL \[1, 3, 5, 10, 0, 5, 27\], MM \<100 mL \[0, 2, 9, 17, 27, 24, 40\], and MM \>=100 mL \[1, 0, 2, 8, 0, 8, 30\]. These yield Figure-derived EVT/MM mRS 0-2 counts of 39/14 and mRS 0-3 counts of 75/39, versus eTable 2 counts of 34/12 and 65/31. The mRS 5-6 counts reconcile at 76/102; reconstructed mRS-6 counts 62/70 also reconcile with eTable mortality.

#### Evidence 2: Calculation

> The Figure-derived minus eTable 2 differences are +5 EVT and +2 MM for mRS 0-2; +10 EVT and +8 MM for mRS 0-3; and 0/0 for mRS 5-6. The direct sources do not state the figure's unrounded values or percentage-production rule, so this is a reproducible diagnostic comparison, not an attribution of cause.

#### Evidence 3: Alternative source-grounded interpretations

> The displays may use different outcome derivations or versions despite identical ITT labels and arm totals; Figure 2 percentages, labels, or segment assignments may contain a production issue; eTable 2 may use an unstated outcome set; or an unstated non-nearest rounding, normalization, or weighting rule may invalidate the reconstruction.

### Source links

- sourceLinks 0: [Main article Figure 2 — PDF p. 7](../../../2024/jama.2024.0572/jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=7)
- sourceLinks 1: [Supplement 5 eTable 2 — PDF p. 38](../../../2024/jama.2024.0572/joi240006supp5_prod_1708623115.01733.pdf#page=38)
- sourceLinks 2: [main Results population statement — PDF p. 4](../../../2024/jama.2024.0572/jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4)
- sourceLinks 3: [Supplement 5 eFigure 3 — PDF p. 8](../../../2024/jama.2024.0572/joi240006supp5_prod_1708623115.01733.pdf#page=8)
- evidencePaths 0: [2024/jama.2024.0572/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.0572/.ai_paper_validation/review_1_5_3/source_inventory.md)
- evidencePaths 1: [2024/jama.2024.0572/.ai\_paper\_validation/review\_1\_5\_3/verification/evidence\_recheck.md](../../../2024/jama.2024.0572/.ai_paper_validation/review_1_5_3/verification/evidence_recheck.md)

[Original Markdown report](../../../2024/jama.2024.0572/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_C |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Requires ordinary nearest-whole rounding and identical outcome derivation. |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C001 |
| key | 2024::jama.2024.0572::C001 |
| legacyRelationship |  |
| locations | Main article Figure 2 — PDF p. 7; Supplement 5 eTable 2 — PDF p. 38; main Results population statement — PDF p. 4; and Supplement 5 eFigure 3 — PDF p. 8. |
| originalCrossDocument | 1 |
| package | jama.2024.0572 |
| planMechanism |  |
| primary | S\_C |
| rationale | Main Figure2 ITT mRS distributions reconstruct different threshold counts from results-supplement eTable2 despite matched168-per-arm labels. |
| reportHref | ../../2024/jama.2024.0572/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.0572/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | The Figure 2 ITT 90-day mRS distributions and Supplement 5 eTable 2 ITT threshold counts do not reconcile under ordinary nearest-whole-percentage rounding, despite matching ITT labels and 168 participants per arm. |
| submissionInvolved | 1 |
| subtype | distribution\_threshold\_counts |
| suggestedDomain | report\_internal\_inconsistency |
| title | ITT Figure 2 mRS distributions conflict with ITT eTable 2 threshold counts |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C002

**aRR is labeled as an absolute risk reduction but displayed and interpreted as a ratio**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.0572::C002 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> Main narrative — PDF p. 6; Main Table 2 — PDF p. 7; Main Table 3 — PDF p. 9; trial SAP — PDF p. 17; secondary-analysis SAP — PDF p. 4; and Supplement 5 eTable 7 — PDF p. 43.

### Candidate statement

> The main narrative and tables expand aRR as “absolute risk reduction,” while printed estimates, a greater-than-1 interpretation, separate aRD values, and supplied SAP statements indicate a ratio-scale measure.

### AI rationale

> Main narrative and tables expand aRR as absolute risk reduction while their own interpretation explicitly says rate ratio and uses null1, alongside separate additive aRD. SAP relative-risk methods and supplementary aRR/aRD rows corroborate this internal scale mismatch.

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

> The narrative and Tables 2-3 expand aRR as “absolute risk reduction.” Table 2 states that values greater than 1 indicate a higher rate ratio and prints values including 0.89 (0.84-0.95), 0.91 (0.87-0.95), and 1.05 (1.02-1.08). Table 3 separately labels aRD as adjusted risk difference and gives, for example, aRR 1.33 (0.52-3.44) alongside aRD 0.178 (-0.109 to 0.465). The SAPs specify modified-Poisson relative-risk analyses.

#### Evidence 1: Reported-versus-comparator

> An absolute risk reduction/risk difference is additive, expressed in risk units, and has a null value of 0. A risk or rate ratio is multiplicative, dimensionless, and has a null value of 1. The printed estimates, confidence intervals, and explicit greater-than-1 rate-ratio interpretation fit the latter scale; the repeated expansion “absolute risk reduction” does not reconcile with it.

#### Evidence 2: Calculation

> This is a logical scale comparison rather than a numerical reconstruction. A value 1.33 with a confidence interval 0.52-3.44 is ratio-scale and centered on a null of 1; the separately printed aRD 0.178 with an interval spanning 0 is additive-scale. The source's own rate-ratio sentence confirms the mismatch.

#### Evidence 3: Alternative source-grounded interpretations

> aRR may have been intended as adjusted risk ratio, while “absolute risk reduction” was a repeated abbreviation-key error. The tables' rate-ratio sentence may instead be unintended, or an unreported nonstandard term may have been used. The supplied package provides no definition that makes an absolute reduction compatible with the displayed ratio scale.

### Source links

- sourceLinks 0: [Main narrative — PDF p. 6](../../../2024/jama.2024.0572/jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6)
- sourceLinks 1: [Main Table 2 — PDF p. 7](../../../2024/jama.2024.0572/jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=7)
- sourceLinks 2: [Main Table 3 — PDF p. 9](../../../2024/jama.2024.0572/jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=9)
- sourceLinks 3: [trial SAP — PDF p. 17](../../../2024/jama.2024.0572/joi240006supp3_prod_1708623114.99733.pdf#page=17)
- sourceLinks 4: [secondary-analysis SAP — PDF p. 4](../../../2024/jama.2024.0572/joi240006supp4_prod_1708623115.00733.pdf#page=4)
- sourceLinks 5: [Supplement 5 eTable 7 — PDF p. 43](../../../2024/jama.2024.0572/joi240006supp5_prod_1708623115.01733.pdf#page=43)
- evidencePaths 0: [2024/jama.2024.0572/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.0572/.ai_paper_validation/review_1_5_3/source_inventory.md)
- evidencePaths 1: [2024/jama.2024.0572/.ai\_paper\_validation/review\_1\_5\_3/verification/evidence\_recheck.md](../../../2024/jama.2024.0572/.ai_paper_validation/review_1_5_3/verification/evidence_recheck.md)

[Original Markdown report](../../../2024/jama.2024.0572/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | SAP citation is supporting model context, not a demonstrated report-versus-plan analytical discrepancy. |
| broadPlanInvolved | 0 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C002 |
| key | 2024::jama.2024.0572::C002 |
| legacyRelationship |  |
| locations | Main narrative — PDF p. 6; Main Table 2 — PDF p. 7; Main Table 3 — PDF p. 9; trial SAP — PDF p. 17; secondary-analysis SAP — PDF p. 4; and Supplement 5 eTable 7 — PDF p. 43. |
| originalCrossDocument | 0 |
| package | jama.2024.0572 |
| planMechanism |  |
| primary | S\_W |
| rationale | Main narrative and tables expand aRR as absolute risk reduction while their own interpretation explicitly says rate ratio and uses null1, alongside separate additive aRD. SAP relative-risk methods and supplementary aRR/aRD rows corroborate this internal scale mismatch. |
| reportHref | ../../2024/jama.2024.0572/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.0572/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | The main narrative and tables expand aRR as “absolute risk reduction,” while printed estimates, a greater-than-1 interpretation, separate aRD values, and supplied SAP statements indicate a ratio-scale measure. |
| submissionInvolved | 1 |
| subtype | effect\_measure\_label |
| suggestedDomain | report\_internal\_inconsistency |
| title | aRR is labeled as an absolute risk reduction but displayed and interpreted as a ratio |
| year | 2024 |
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
