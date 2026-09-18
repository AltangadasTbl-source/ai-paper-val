# jama.2019.2210

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2019 |
| Paper | jama.2019.2210 |
| Candidates | 9 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2019/jama.2019.2210/)

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

- [C001](#candidate-c001) — Table 1 SNP percentages use unlabelled, variable available-case denominators (S_W)
- [C002](#candidate-c002) — Figure 3 caption says panel-C risk numbers are absent although the panel prints them (S_W)
- [C003](#candidate-c003) — Final protocol gives different accrual stopping thresholds (P_P)
- [C004](#candidate-c004) — Final protocol assigns de novo cancer incompatible endpoint labels (P_R)
- [C005](#candidate-c005) — One final-protocol high-25(OH)D stratum label omits the boundary operator (P_P)
- [C006](#candidate-c006) — Supplement labels Cdx2 genotype panels as CDK2 (S_C)
- [C007](#candidate-c007) — Table 1 BMI categories use smaller, unlabelled denominators than the arm headers (S_W)
- [C008](#candidate-c008) — Report and protocol use different time-origin labels despite a same-visit equivalence statement (P_R)
- [C009](#candidate-c009) — Table 2 hazard-ratio direction footnote is opposite the displayed outcome direction (S_W)

## Candidate C001

**Table 1 SNP percentages use unlabelled, variable available-case denominators**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.2210::C001 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> main article — PDF p. 5; Supplement 2 — PDF p. 7, p. 13, and p. 27.

### Candidate statement

> Table 1 percentages use SNP-specific denominators smaller than the printed arm headers without an available-case or missingness label.

### AI rationale

> Main Table1 SNP category counts and percentages use variable available-case Ns smaller than its arm headers251/166. Results-supplement risk counts agree with genotype totals and corroborate internal denominator omission.

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

> Table 1 heads the arms vitamin D n=251 and placebo n=166; its Cdx2 counts are 89/103/38 and 49/77/24, while the footnote addresses only percentage rounding. Supplement figures repeat the genotype-specific time-zero counts.

#### Evidence 1: Reported-versus-comparator

> The arm headers are 251/166; Cdx2 triplets total 230/150, and other SNP totals vary from 230–245 and 148–157.

#### Evidence 2: Calculation

> Cdx2: 89+103+38=230, 49+77+24=150; 89/230=38.70%, 103/230=44.78%, and 38/230=16.52%, matching printed rounded percentages. The respective deficits from headers are 21 and 16.

#### Evidence 3: Alternative source-grounded interpretations

> SNP-specific assay availability could legitimately yield variable denominators, but neither the table nor its footnote states that explanation.

### Source links

- sourceLinks 0: [main article — PDF p. 5](../../../2019/jama.2019.2210/jama_urashima_2019_oi_190023.pdf#page=5)
- sourceLinks 1: [Supplement 2 — PDF p. 7](../../../2019/jama.2019.2210/joi190023supp2_prod.pdf#page=7)
- sourceLinks 2: [p. 13](../../../2019/jama.2019.2210/joi190023supp2_prod.pdf#page=13)
- sourceLinks 3: [p. 27](../../../2019/jama.2019.2210/joi190023supp2_prod.pdf#page=27)
- evidencePaths 0: [2019/jama.2019.2210/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.2210/.ai_paper_validation/review_1_5_1/source_inventory.md)

[Original Markdown report](../../../2019/jama.2019.2210/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Assay availability can legitimately create varying denominators; missingness labelling is the issue. |
| broadPlanInvolved | 0 |
| category | Denominator, proportion, or total inconsistency |
| currentReportCrossDocument | 0 |
| id | C001 |
| key | 2019::jama.2019.2210::C001 |
| legacyRelationship |  |
| locations | main article — PDF p. 5; Supplement 2 — PDF p. 7, p. 13, and p. 27. |
| originalCrossDocument | 0 |
| package | jama.2019.2210 |
| planMechanism |  |
| primary | S\_W |
| rationale | Main Table1 SNP category counts and percentages use variable available-case Ns smaller than its arm headers251/166. Results-supplement risk counts agree with genotype totals and corroborate internal denominator omission. |
| reportHref | ../../2019/jama.2019.2210/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.2210/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | Table 1 percentages use SNP-specific denominators smaller than the printed arm headers without an available-case or missingness label. |
| submissionInvolved | 1 |
| subtype | denominator\_definition |
| suggestedDomain | statistical\_results |
| title | Table 1 SNP percentages use unlabelled, variable available-case denominators |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C002

**Figure 3 caption says panel-C risk numbers are absent although the panel prints them**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.2210::C002 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> main article — PDF p. 7.

### Candidate statement

> Figure 3 panel C visibly prints risk rows while its caption says that panel-C numbers at risk are not given.

### AI rationale

> Main Figure3C visibly has14 at-risk entries while its own caption says panelC risk numbers are not given.

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

> Panel C prints placebo 90, 88, 70, 51, 34, 22, 11 and vitamin D 142, 139, 115, 88, 61, 41, 20 under No. at risk.

#### Evidence 1: Reported-versus-comparator

> The caption states, Numbers at risk for panel C are not given because of weighting.

#### Evidence 2: Calculation

> Seven placebo plus seven vitamin-D entries yield 14 displayed panel-C risk values, not zero.

#### Evidence 3: Alternative source-grounded interpretations

> The caption may mean weighted or effective numbers are unavailable while the panel shows raw counts; the source does not define that distinction.

### Source links

- sourceLinks 0: [main article — PDF p. 7](../../../2019/jama.2019.2210/jama_urashima_2019_oi_190023.pdf#page=7)
- evidencePaths 0: [2019/jama.2019.2210/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.2210/.ai_paper_validation/review_1_5_1/source_inventory.md)

[Original Markdown report](../../../2019/jama.2019.2210/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Caption could refer to weighted/effective counts while plotted entries are raw, but this distinction is unstated. |
| broadPlanInvolved | 0 |
| category | Numeric or arithmetic inconsistency |
| currentReportCrossDocument | 0 |
| id | C002 |
| key | 2019::jama.2019.2210::C002 |
| legacyRelationship |  |
| locations | main article — PDF p. 7. |
| originalCrossDocument | 0 |
| package | jama.2019.2210 |
| planMechanism |  |
| primary | S\_W |
| rationale | Main Figure3C visibly has14 at-risk entries while its own caption says panelC risk numbers are not given. |
| reportHref | ../../2019/jama.2019.2210/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.2210/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | Figure 3 panel C visibly prints risk rows while its caption says that panel-C numbers at risk are not given. |
| submissionInvolved | 1 |
| subtype | caption\_display |
| suggestedDomain | statistical\_results |
| title | Figure 3 caption says panel-C risk numbers are absent although the panel prints them |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C003

**Final protocol gives different accrual stopping thresholds**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.2210::C003 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> Supplement 1 — PDF p. 18 and Supplement 1 — PDF p. 31.

### Candidate statement

> Two final-protocol passages state different literal enrollment stopping thresholds.

### AI rationale

> Two passages in the final protocol say stop after400 enrollment versus when enrollment\>400; this compares threshold definitions inside one planning document.

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

> Page 18 says entry stops if randomized enrollment reaches \>400; it also gives 240+160=400 as the target allocation.

#### Evidence 1: Reported-versus-comparator

> Page 31 says, After enrolling 400 patients, enrollment will finish.

#### Evidence 2: Calculation

> 240+160=400; the smallest integer satisfying n\>400 is 401, whereas after enrolling 400 identifies 400.

#### Evidence 3: Alternative source-grounded interpretations

> Either statement could be shorthand for a near-400 operational target or a completed randomization block, but no cited passage says so.

### Source links

- sourceLinks 0: [Supplement 1 — PDF p. 18](../../../2019/jama.2019.2210/joi190023supp1_prod.pdf#page=18)
- sourceLinks 1: [Supplement 1 — PDF p. 31](../../../2019/jama.2019.2210/joi190023supp1_prod.pdf#page=31)
- evidencePaths 0: [2019/jama.2019.2210/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.2210/.ai_paper_validation/review_1_5_1/source_inventory.md)

[Original Markdown report](../../../2019/jama.2019.2210/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_P |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Near400 target or completed-block operational shorthand is possible. |
| broadPlanInvolved | 1 |
| category | Denominator, proportion, or total inconsistency |
| currentReportCrossDocument | 0 |
| id | C003 |
| key | 2019::jama.2019.2210::C003 |
| legacyRelationship |  |
| locations | Supplement 1 — PDF p. 18 and Supplement 1 — PDF p. 31. |
| originalCrossDocument | 0 |
| package | jama.2019.2210 |
| planMechanism |  |
| primary | P\_P |
| rationale | Two passages in the final protocol say stop after400 enrollment versus when enrollment\>400; this compares threshold definitions inside one planning document. |
| reportHref | ../../2019/jama.2019.2210/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.2210/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | Two final-protocol passages state different literal enrollment stopping thresholds. |
| submissionInvolved | 0 |
| subtype | enrollment\_threshold |
| suggestedDomain | plan\_material |
| title | Final protocol gives different accrual stopping thresholds |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C004

**Final protocol assigns de novo cancer incompatible endpoint labels**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.2210::C004 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> Supplement 1 — PDF p. 19, p. 25, p. 26, and p. 45; main article — PDF p. 8.

### Candidate statement

> The same de novo-cancer event is labelled not as an outcome, Tertiary outcome, and is reported in a safety-outcome table without a stated reconciliation.

### AI rationale

> The protocol synopsis calls de novo cancer not an outcome, while its body/change summary calls it tertiary and says it was separated from safety outcomes; the article reports it under Safety Outcomes. This genuinely combines internal-plan hierarchy mismatch and report-versus-plan classification.

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

> The synopsis says cancer appearing de novo will be an adverse event, not as an outcome; the final body lists it as a tertiary outcome, and the change summary says it was inserted as a tertiary outcome.

#### Evidence 1: Reported-versus-comparator

> The main article places Cancer de novo in Table 3, Safety Outcomes, including randomization-group counts 16/251 and 9/166.

#### Evidence 2: Calculation

> The logical comparison reproduces three labels: adverse event/not outcome; tertiary outcome; and Safety Outcomes. The reported counts establish that this is a quantitative reporting item.

#### Evidence 3: Alternative source-grounded interpretations

> Clinical monitoring could use an adverse-event role while the statistical hierarchy uses a tertiary-outcome role, but the supplied text does not define those roles separately.

### Source links

- sourceLinks 0: [Supplement 1 — PDF p. 19](../../../2019/jama.2019.2210/joi190023supp1_prod.pdf#page=19)
- sourceLinks 1: [p. 25](../../../2019/jama.2019.2210/joi190023supp1_prod.pdf#page=25)
- sourceLinks 2: [p. 26](../../../2019/jama.2019.2210/joi190023supp1_prod.pdf#page=26)
- sourceLinks 3: [p. 45](../../../2019/jama.2019.2210/joi190023supp1_prod.pdf#page=45)
- sourceLinks 4: [main article — PDF p. 8](../../../2019/jama.2019.2210/jama_urashima_2019_oi_190023.pdf#page=8)
- evidencePaths 0: [2019/jama.2019.2210/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.2210/.ai_paper_validation/review_1_5_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.2210/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.2210/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)
- evidencePaths 2: [2019/jama.2019.2210/.ai\_paper\_validation/review\_1\_5\_1/candidate\_ledger.md](../../../2019/jama.2019.2210/.ai_paper_validation/review_1_5_1/candidate_ledger.md)

[Original Markdown report](../../../2019/jama.2019.2210/.ai_paper_validation/final_report_1_5_1.md)

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
| ambiguity | The ledger merges an internal numeric lead and cross-source lead for the same event. Dual clinical safety and statistical tertiary roles may coexist, but the change summary explicitly says separated from safety outcomes. |
| broadPlanInvolved | 1 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 1 |
| id | C004 |
| key | 2019::jama.2019.2210::C004 |
| legacyRelationship |  |
| locations | Supplement 1 — PDF p. 19, p. 25, p. 26, and p. 45; main article — PDF p. 8. |
| originalCrossDocument | 0 |
| package | jama.2019.2210 |
| planMechanism | endpoint\_definition\_window\_hierarchy |
| primary | P\_R |
| rationale | The protocol synopsis calls de novo cancer not an outcome, while its body/change summary calls it tertiary and says it was separated from safety outcomes; the article reports it under Safety Outcomes. This genuinely combines internal-plan hierarchy mismatch and report-versus-plan classification. |
| reportHref | ../../2019/jama.2019.2210/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.2210/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C004 |
| sourceStatus | Pending Human Adjudication |
| statement | The same de novo-cancer event is labelled not as an outcome, Tertiary outcome, and is reported in a safety-outcome table without a stated reconciliation. |
| submissionInvolved | 0 |
| subtype | endpoint\_hierarchy |
| suggestedDomain | protocol\_report |
| title | Final protocol assigns de novo cancer incompatible endpoint labels |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | retain |

## Candidate C005

**One final-protocol high-25(OH)D stratum label omits the boundary operator**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.2210::C005 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> Supplement 1 — PDF p. 23 and p. 31; main article — PDF p. 3.

### Candidate statement

> One protocol page gives high 25(OH)D as (40 ng/mL) without an operator, unlike later explicit \>40 ng/mL definitions.

### AI rationale

> One final-protocol high25(OH)D label omits its operator at40 while a later section of the same protocol specifies\>40. The main article repeats\>40 as corroboration, not as a separate plan-report deviation.

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

> Page 23 defines low (\<20), middle (\>=20 to \<=40), and high (40 ng/mL).

#### Evidence 1: Reported-versus-comparator

> Page 31 and the article explicitly give high as \>40 ng/mL.

#### Evidence 2: Calculation

> At 40, 20\<=40\<=40 places the value in middle; 40 is not \>40. The page-23 text leaves whether high means =40, \>=40, or \>40 unspecified.

#### Evidence 3: Alternative source-grounded interpretations

> Page 23 may use 40 ng/mL as informal shorthand for the cutoff; the later sources make \>40 the likely intended explicit rule.

### Source links

- sourceLinks 0: [Supplement 1 — PDF p. 23](../../../2019/jama.2019.2210/joi190023supp1_prod.pdf#page=23)
- sourceLinks 1: [p. 31](../../../2019/jama.2019.2210/joi190023supp1_prod.pdf#page=31)
- sourceLinks 2: [main article — PDF p. 3](../../../2019/jama.2019.2210/jama_urashima_2019_oi_190023.pdf#page=3)
- evidencePaths 0: [2019/jama.2019.2210/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.2210/.ai_paper_validation/review_1_5_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.2210/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.2210/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2019/jama.2019.2210/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_P |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | 40ng/mL may be shorthand for the threshold; actual subgroup assignment is unavailable. |
| broadPlanInvolved | 1 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C005 |
| key | 2019::jama.2019.2210::C005 |
| legacyRelationship |  |
| locations | Supplement 1 — PDF p. 23 and p. 31; main article — PDF p. 3. |
| originalCrossDocument | 0 |
| package | jama.2019.2210 |
| planMechanism |  |
| primary | P\_P |
| rationale | One final-protocol high25(OH)D label omits its operator at40 while a later section of the same protocol specifies\>40. The main article repeats\>40 as corroboration, not as a separate plan-report deviation. |
| reportHref | ../../2019/jama.2019.2210/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.2210/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C005 |
| sourceStatus | Pending Human Adjudication |
| statement | One protocol page gives high 25(OH)D as (40 ng/mL) without an operator, unlike later explicit \>40 ng/mL definitions. |
| submissionInvolved | 0 |
| subtype | threshold\_operator |
| suggestedDomain | plan\_material |
| title | One final-protocol high-25(OH)D stratum label omits the boundary operator |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C006

**Supplement labels Cdx2 genotype panels as CDK2**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.2210::C006 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> main article — PDF p. 5; Supplement 1 — PDF p. 27; Supplement 2 — PDF p. 13, p. 14, and p. 15.

### Candidate statement

> Supplement 2 labels matched Cdx2 subgroup panels as CDK2 although the article and protocol identify Cdx2/CDX2 rs11568820.

### AI rationale

> Main Table1 Cdx2 genotype label and all six arm/genotype counts match results-supplement panels titled CDK2. The protocol CDX2 rs11568820 entry corroborates subgroup identity; the substantive target is the main/results-supplement locus label mismatch.

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

> Table 1 gives Cdx2 GG/GA/AA vitamin-D counts 89,103,38 and placebo counts 49,77,24; the protocol lists CDX2, rs11568820.

#### Evidence 1: Reported-versus-comparator

> Supplement panels are titled CDK2 GG, CDK2 GA, and CDK2 AA and show corresponding placebo/vitamin-D counts 49/89, 77/103, and 24/38.

#### Evidence 2: Calculation

> 49=49, 89=89, 77=77, 103=103, 24=24, and 38=38; labels differ at the third character after CD: X versus K.

#### Evidence 3: Alternative source-grounded interpretations

> Matching counts and absence of CDK2 from the protocol list support a possible typesetting substitution; a distinct analysis with coincident counts is not defined in the package.

### Source links

- sourceLinks 0: [main article — PDF p. 5](../../../2019/jama.2019.2210/jama_urashima_2019_oi_190023.pdf#page=5)
- sourceLinks 1: [Supplement 1 — PDF p. 27](../../../2019/jama.2019.2210/joi190023supp1_prod.pdf#page=27)
- sourceLinks 2: [Supplement 2 — PDF p. 13](../../../2019/jama.2019.2210/joi190023supp2_prod.pdf#page=13)
- sourceLinks 3: [p. 14](../../../2019/jama.2019.2210/joi190023supp2_prod.pdf#page=14)
- sourceLinks 4: [p. 15](../../../2019/jama.2019.2210/joi190023supp2_prod.pdf#page=15)
- evidencePaths 0: [2019/jama.2019.2210/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.2210/.ai_paper_validation/review_1_5_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.2210/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.2210/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2019/jama.2019.2210/.ai_paper_validation/final_report_1_5_1.md)

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
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 1 |
| id | C006 |
| key | 2019::jama.2019.2210::C006 |
| legacyRelationship |  |
| locations | main article — PDF p. 5; Supplement 1 — PDF p. 27; Supplement 2 — PDF p. 13, p. 14, and p. 15. |
| originalCrossDocument | 0 |
| package | jama.2019.2210 |
| planMechanism |  |
| primary | S\_C |
| rationale | Main Table1 Cdx2 genotype label and all six arm/genotype counts match results-supplement panels titled CDK2. The protocol CDX2 rs11568820 entry corroborates subgroup identity; the substantive target is the main/results-supplement locus label mismatch. |
| reportHref | ../../2019/jama.2019.2210/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.2210/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C006 |
| sourceStatus | Pending Human Adjudication |
| statement | Supplement 2 labels matched Cdx2 subgroup panels as CDK2 although the article and protocol identify Cdx2/CDX2 rs11568820. |
| submissionInvolved | 1 |
| subtype | genetic\_locus\_label |
| suggestedDomain | report\_internal\_inconsistency |
| title | Supplement labels Cdx2 genotype panels as CDK2 |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C007

**Table 1 BMI categories use smaller, unlabelled denominators than the arm headers**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.2210::C007 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> main article — PDF p. 5; Supplement 2 — PDF p. 32 and p. 33.

### Candidate statement

> Table 1 BMI quartiles and complementary supplement subgroups total fewer participants than the printed arm headers without a missingness or available-case label.

### AI rationale

> Main Table1 BMI quartiles total249/165, below its251/166 arm headers, and percentages use the smaller totals. Results supplement reproduces249/165 and corroborates the internal missing denominator statement.

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

> Under vitamin D n=251 and placebo n=166, Table 1 gives BMI quartile counts 63,62,59,65 and 36,43,45,41.

#### Evidence 1: Reported-versus-comparator

> Supplement 2 complementary BMI risks total vitamin D 208+41 and placebo 144+21.

#### Evidence 2: Calculation

> 63+62+59+65=249 and 36+43+45+41=165, deficits of 2 and 1; Supplement 2 repeats 208+41=249 and 144+21=165. Percentages also round from the smaller denominators.

#### Evidence 3: Alternative source-grounded interpretations

> BMI may be unavailable for exactly two vitamin-D and one placebo participant; a count transcription issue is another possibility. Neither explanation is stated.

### Source links

- sourceLinks 0: [main article — PDF p. 5](../../../2019/jama.2019.2210/jama_urashima_2019_oi_190023.pdf#page=5)
- sourceLinks 1: [Supplement 2 — PDF p. 32](../../../2019/jama.2019.2210/joi190023supp2_prod.pdf#page=32)
- sourceLinks 2: [p. 33](../../../2019/jama.2019.2210/joi190023supp2_prod.pdf#page=33)
- evidencePaths 0: [2019/jama.2019.2210/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.2210/.ai_paper_validation/review_1_5_1/source_inventory.md)

[Original Markdown report](../../../2019/jama.2019.2210/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | BMI availability may explain the2/1 deficits; it is not a disagreement between the main and supplemental totals. |
| broadPlanInvolved | 0 |
| category | Denominator, proportion, or total inconsistency |
| currentReportCrossDocument | 0 |
| id | C007 |
| key | 2019::jama.2019.2210::C007 |
| legacyRelationship |  |
| locations | main article — PDF p. 5; Supplement 2 — PDF p. 32 and p. 33. |
| originalCrossDocument | 0 |
| package | jama.2019.2210 |
| planMechanism |  |
| primary | S\_W |
| rationale | Main Table1 BMI quartiles total249/165, below its251/166 arm headers, and percentages use the smaller totals. Results supplement reproduces249/165 and corroborates the internal missing denominator statement. |
| reportHref | ../../2019/jama.2019.2210/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.2210/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C007 |
| sourceStatus | Pending Human Adjudication |
| statement | Table 1 BMI quartiles and complementary supplement subgroups total fewer participants than the printed arm headers without a missingness or available-case label. |
| submissionInvolved | 1 |
| subtype | denominator\_definition |
| suggestedDomain | statistical\_results |
| title | Table 1 BMI categories use smaller, unlabelled denominators than the arm headers |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C008

**Report and protocol use different time-origin labels despite a same-visit equivalence statement**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.2210::C008 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> main article — PDF p. 2 and p. 6; Supplement 1 — PDF p. 25 and p. 29; Supplement 2 — PDF p. 2 and p. 3.

### Candidate statement

> The report labels survival time from randomization while the final protocol labels it from starting supplementation; the article explicitly describes these as the same visit and treats them as equivalent, so no actual date difference is claimed.

### AI rationale

> Article/results-supplement survival axes say randomization while protocol says supplementation start. Retained as the recorded report-versus-plan time-origin wording candidate, although the article explicitly equates these dates at the same visit.

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

> The article defines RFS/OS from randomization, parenthetically as time from starting study medication, and plots years after randomization. It says participants were randomized and started supplementation at the first outpatient visit.

#### Evidence 1: Reported-versus-comparator

> The protocol defines RFS/OS and survival duration from starting supplementation or the supplement start day; Supplement 2 axes use randomization.

#### Evidence 2: Calculation

> No numeric estimate is recalculated. The wording comparison is randomization date versus supplement start day; participant-level date fields and survival-analysis code are not supplied to establish identity in every record.

#### Evidence 3: Alternative source-grounded interpretations

> The article itself supports different labels for the same operational date, rather than different numeric origins; universal participant-level identity remains unconfirmed.

### Source links

- sourceLinks 0: [main article — PDF p. 2](../../../2019/jama.2019.2210/jama_urashima_2019_oi_190023.pdf#page=2)
- sourceLinks 1: [p. 6](../../../2019/jama.2019.2210/jama_urashima_2019_oi_190023.pdf#page=6)
- sourceLinks 2: [Supplement 1 — PDF p. 25](../../../2019/jama.2019.2210/joi190023supp1_prod.pdf#page=25)
- sourceLinks 3: [p. 29](../../../2019/jama.2019.2210/joi190023supp1_prod.pdf#page=29)
- sourceLinks 4: [Supplement 2 — PDF p. 2](../../../2019/jama.2019.2210/joi190023supp2_prod.pdf#page=2)
- sourceLinks 5: [p. 3](../../../2019/jama.2019.2210/joi190023supp2_prod.pdf#page=3)
- evidencePaths 0: [2019/jama.2019.2210/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.2210/.ai_paper_validation/review_1_5_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.2210/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.2210/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)
- evidencePaths 2: [2019/jama.2019.2210/.ai\_paper\_validation/review\_1\_5\_1/candidate\_ledger.md](../../../2019/jama.2019.2210/.ai_paper_validation/review_1_5_1/candidate_ledger.md)

[Original Markdown report](../../../2019/jama.2019.2210/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 1 |
| ambiguity | Wording-only/equivalent: source directly states operational equivalence, so no actual time-origin discrepancy is established. Sensitivity excluding this candidate leaves7 report-versus-plan candidates out of70 total. |
| broadPlanInvolved | 1 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 1 |
| id | C008 |
| key | 2019::jama.2019.2210::C008 |
| legacyRelationship |  |
| locations | main article — PDF p. 2 and p. 6; Supplement 1 — PDF p. 25 and p. 29; Supplement 2 — PDF p. 2 and p. 3. |
| originalCrossDocument | 0 |
| package | jama.2019.2210 |
| planMechanism | endpoint\_definition\_window\_hierarchy |
| primary | P\_R |
| rationale | Article/results-supplement survival axes say randomization while protocol says supplementation start. Retained as the recorded report-versus-plan time-origin wording candidate, although the article explicitly equates these dates at the same visit. |
| reportHref | ../../2019/jama.2019.2210/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.2210/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C008 |
| sourceStatus | Pending Human Adjudication |
| statement | The report labels survival time from randomization while the final protocol labels it from starting supplementation; the article explicitly describes these as the same visit and treats them as equivalent, so no actual date difference is claimed. |
| submissionInvolved | 0 |
| subtype | time\_origin\_wording |
| suggestedDomain | protocol\_report |
| title | Report and protocol use different time-origin labels despite a same-visit equivalence statement |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | retain |

## Candidate C009

**Table 2 hazard-ratio direction footnote is opposite the displayed outcome direction**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.2210::C009 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> main article — PDF p. 4, p. 6, and p. 7.

### Candidate statement

> Table 2 says HR values greater than 1 indicate decreased outcome probability with vitamin D, whereas displayed outcome directions pair lower vitamin-D incidence with HRs below 1.

### AI rationale

> Main Table2 footnote says HR\>1 means reduced outcome with vitaminD, while main counts/curves and HRs below1 reflect lower vitaminD events. All compared direction descriptions are inside the article.

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

> Table 2 reports relapse HR 0.75 (0.48–1.17), cancer-specific-death HR 1.09 (0.58–2.01), noncancer-death HR 0.70 (0.29–1.73), and the footnote assigning decreased outcome probability to HR \>1.

#### Evidence 1: Reported-versus-comparator

> Page 4 gives vitamin D/placebo relapse 41/251 versus 36/166, cancer-specific death 27/251 versus 16/166, and noncancer death 10/251 versus 9/166; Figure 2C shows the vitamin-D relapse curve below placebo and prints HR 0.75.

#### Evidence 2: Calculation

> Diagnostic crude proportions are relapse 16.33% versus 21.69%, noncancer death 3.98% versus 5.42%, and cancer-specific death 10.76% versus 9.64%. Lower vitamin-D incidence corresponds to HRs below 1 for relapse and noncancer death; higher incidence corresponds to HR above 1 for cancer-specific death. These are diagnostics, not reproduced HR estimators.

#### Evidence 3: Alternative source-grounded interpretations

> A placebo-relative contrast could make the footnote coherent, but the plotted/narrated relapse direction and HR below 1 indicate the opposite orientation for displayed relapse results; a table-only reversed contrast is not stated.

### Source links

- sourceLinks 0: [main article — PDF p. 4](../../../2019/jama.2019.2210/jama_urashima_2019_oi_190023.pdf#page=4)
- sourceLinks 1: [p. 6](../../../2019/jama.2019.2210/jama_urashima_2019_oi_190023.pdf#page=6)
- sourceLinks 2: [p. 7](../../../2019/jama.2019.2210/jama_urashima_2019_oi_190023.pdf#page=7)
- evidencePaths 0: [2019/jama.2019.2210/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.2210/.ai_paper_validation/review_1_5_1/source_inventory.md)

[Original Markdown report](../../../2019/jama.2019.2210/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Exact event-time models are not reconstructed; no table-specific reversed contrast is stated. |
| broadPlanInvolved | 0 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C009 |
| key | 2019::jama.2019.2210::C009 |
| legacyRelationship |  |
| locations | main article — PDF p. 4, p. 6, and p. 7. |
| originalCrossDocument | 0 |
| package | jama.2019.2210 |
| planMechanism |  |
| primary | S\_W |
| rationale | Main Table2 footnote says HR\>1 means reduced outcome with vitaminD, while main counts/curves and HRs below1 reflect lower vitaminD events. All compared direction descriptions are inside the article. |
| reportHref | ../../2019/jama.2019.2210/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.2210/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C009 |
| sourceStatus | Pending Human Adjudication |
| statement | Table 2 says HR values greater than 1 indicate decreased outcome probability with vitamin D, whereas displayed outcome directions pair lower vitamin-D incidence with HRs below 1. |
| submissionInvolved | 1 |
| subtype | effect\_direction |
| suggestedDomain | report\_internal\_inconsistency |
| title | Table 2 hazard-ratio direction footnote is opposite the displayed outcome direction |
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
