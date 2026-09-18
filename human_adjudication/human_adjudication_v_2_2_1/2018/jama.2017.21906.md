# jama.2017.21906

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2018 |
| Paper | jama.2017.21906 |
| Candidates | 6 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2018/jama.2017.21906/)

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

- [C001](#candidate-c001) — In-hospital beta-blocker adjusted-risk-difference CI endpoint differs between Table 2 and narrative (S_W)
- [C002](#candidate-c002) — Discharge beta-blocker adjusted point estimates differ between Table 2 and narrative (S_W)
- [C003](#candidate-c003) — eTable 1 difference footnote names groups not displayed in the table (S_W)
- [C004](#candidate-c004) — Reported prespecified age-subgroup boundaries differ from the supplied SAP (P_R)
- [C005](#candidate-c005) — The named optimal in-hospital medication composite uses different component labels across final-result tables (S_C)
- [C006](#candidate-c006) — Hospital-type subgroup is reported as prespecified but is absent from the supplied SAP subgroup list (P_R)

## Candidate C001

**In-hospital beta-blocker adjusted-risk-difference CI endpoint differs between Table 2 and narrative**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2017.21906::C001 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> Main article — PDF p. 6, Table 2 In-hospital β-blocker row and adjacent Results narrative.

### Candidate statement

> The same named adjusted in-hospital beta-blocker result prints different upper risk-difference CI endpoints.

### AI rationale

> The same named adjusted in-hospital beta-blocker result prints different upper risk-difference CI endpoints. The focal mismatch is within the main article.

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

> Table 2 prints adjusted risk difference 6.25% (95% CI, 4.10% to 8.40%) and OR 1.46 (1.29 to 1.65). The adjacent narrative prints 6.25% (4.10% to 8.10%) and OR 1.46 (1.29 to 1.65).

#### Evidence 1: Reported-versus-comparator

> Table upper endpoint 8.40% versus narrative upper endpoint 8.10%; the point estimate, lower endpoint, OR, and OR interval agree as printed.

#### Evidence 2: Calculation

> 8.40 - 8.10 = 0.30 percentage point.

#### Evidence 3: Alternative source-grounded interpretations

> One occurrence may be a transcription/production error, or the narrative may use an unlabelled distinct output. The supplied package does not establish either explanation or which endpoint is supported by final model output.

### Source links

- sourceLinks 0: [Main article — PDF p. 6](../../../2018/jama.2017.21906/jama_huffman_2018_oi_170166.pdf#page=6)
- evidencePaths 0: [2018/jama.2017.21906/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2017.21906/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2017.21906/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2017.21906/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)

[Original Markdown report](../../../2018/jama.2017.21906/.ai_paper_validation/final_report_1_5_2.md)

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
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 0 |
| id | C001 |
| key | 2018::jama.2017.21906::C001 |
| legacyRelationship |  |
| locations | Main article — PDF p. 6, Table 2 In-hospital β-blocker row and adjacent Results narrative. |
| originalCrossDocument | 0 |
| package | jama.2017.21906 |
| planMechanism |  |
| primary | S\_W |
| rationale | The same named adjusted in-hospital beta-blocker result prints different upper risk-difference CI endpoints. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2017.21906/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2017.21906/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | The same named adjusted in-hospital beta-blocker result prints different upper risk-difference CI endpoints. |
| submissionInvolved | 1 |
| subtype | repeated\_ci\_endpoint |
| suggestedDomain | statistical\_results |
| title | In-hospital beta-blocker adjusted-risk-difference CI endpoint differs between Table 2 and narrative |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C002

**Discharge beta-blocker adjusted point estimates differ between Table 2 and narrative**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2017.21906::C002 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> Main article — PDF p. 6, Table 2 Discharge β-blocker row; Main article — PDF p. 7, Results narrative.

### Candidate statement

> Table 2 and the narrative print different adjusted discharge beta-blocker risk differences and ORs while printing identical intervals.

### AI rationale

> Table 2 and Results narrative in the same main PDF report discharge beta-blocker RD 6.69 versus 6.63 and OR 1.48 versus 1.47 with identical intervals. Despite its original cross-document category, both discrepant occurrences are within the main article.

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

> Table 2 prints risk difference 6.69% (4.43% to 8.95%) and OR 1.48 (1.30 to 1.68). The narrative prints 6.63% with 4.43% to 8.95% and OR 1.47 with 1.30 to 1.68.

#### Evidence 1: Reported-versus-comparator

> Table 2 6.69%/1.48 versus narrative 6.63%/1.47, with both printed risk-difference and OR intervals identical.

#### Evidence 2: Calculation

> 6.69 - 6.63 = 0.06 percentage point; 1.48 - 1.47 = 0.01.

#### Evidence 3: Alternative source-grounded interpretations

> A transcription/output-selection issue or an unlabelled distinct analytic run could explain the values. The package lacks unrounded output, code, and production history, so no cause is established.

### Source links

- sourceLinks 0: [Main article — PDF p. 6](../../../2018/jama.2017.21906/jama_huffman_2018_oi_170166.pdf#page=6)
- sourceLinks 1: [Main article — PDF p. 7](../../../2018/jama.2017.21906/jama_huffman_2018_oi_170166.pdf#page=7)
- evidencePaths 0: [2018/jama.2017.21906/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2017.21906/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2017.21906/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2017.21906/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)

[Original Markdown report](../../../2018/jama.2017.21906/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C002 |
| key | 2018::jama.2017.21906::C002 |
| legacyRelationship |  |
| locations | Main article — PDF p. 6, Table 2 Discharge β-blocker row; Main article — PDF p. 7, Results narrative. |
| originalCrossDocument | 1 |
| package | jama.2017.21906 |
| planMechanism |  |
| primary | S\_W |
| rationale | Table 2 and Results narrative in the same main PDF report discharge beta-blocker RD 6.69 versus 6.63 and OR 1.48 versus 1.47 with identical intervals. Despite its original cross-document category, both discrepant occurrences are within the main article. |
| reportHref | ../../2018/jama.2017.21906/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2017.21906/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | Table 2 and the narrative print different adjusted discharge beta-blocker risk differences and ORs while printing identical intervals. |
| submissionInvolved | 1 |
| subtype | repeated\_effect\_estimate |
| suggestedDomain | report\_internal\_inconsistency |
| title | Discharge beta-blocker adjusted point estimates differ between Table 2 and narrative |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C003

**eTable 1 difference footnote names groups not displayed in the table**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2017.21906::C003 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> Online supplement — PDF p. 17, eTable 1 title, headers, values, and footnote a.

### Candidate statement

> eTable 1 displays complete- and missing-follow-up groups, but its difference footnote defines an intervention-minus-control contrast.

### AI rationale

> eTable 1 displays complete- and missing-follow-up groups, but its difference footnote defines an intervention-minus-control contrast. The focal mismatch is within one non-plan results supplement.

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

> The columns are Complete Follow Up (n=21,079), Missing Follow Up (n=295), and Difference (95% CI); footnote a states Difference = intervention minus control.

#### Evidence 1: Reported-versus-comparator

> The footnote names intervention/control, while the displayed comparison groups are complete/missing follow-up.

#### Evidence 2: Calculation

> Age: 60.0 - 60.6 = -0.6; male percentage: 71.2 - 75.8 = -4.6; initial troponin: 4.6 - 1.3 = 3.3.

#### Evidence 3: Alternative source-grounded interpretations

> The footnote may have been carried over from eTable 2, while eTable 1 may intentionally use missing minus complete. The source does not define every CI contrast or table-production history.

### Source links

- sourceLinks 0: [Online supplement — PDF p. 17](../../../2018/jama.2017.21906/joi170166supp3_prod.pdf#page=17)
- evidencePaths 0: [2018/jama.2017.21906/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2017.21906/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2017.21906/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2017.21906/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)

[Original Markdown report](../../../2018/jama.2017.21906/.ai_paper_validation/final_report_1_5_2.md)

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
| key | 2018::jama.2017.21906::C003 |
| legacyRelationship |  |
| locations | Online supplement — PDF p. 17, eTable 1 title, headers, values, and footnote a. |
| originalCrossDocument | 0 |
| package | jama.2017.21906 |
| planMechanism |  |
| primary | S\_W |
| rationale | eTable 1 displays complete- and missing-follow-up groups, but its difference footnote defines an intervention-minus-control contrast. The focal mismatch is within one non-plan results supplement. |
| reportHref | ../../2018/jama.2017.21906/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2017.21906/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | eTable 1 displays complete- and missing-follow-up groups, but its difference footnote defines an intervention-minus-control contrast. |
| submissionInvolved | 1 |
| subtype | comparator\_label |
| suggestedDomain | report\_internal\_inconsistency |
| title | eTable 1 difference footnote names groups not displayed in the table |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C004

**Reported prespecified age-subgroup boundaries differ from the supplied SAP**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2017.21906::C004 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> SAP — PDF p. 7, section 7.5.2; main article — PDF p. 3, Statistical Analysis; main article — PDF p. 9, Figure 3 and adjacent Results narrative.

### Candidate statement

> The article calls its Figure 3 age subgroups prespecified, but their numeric boundaries differ from the supplied SAP.

### AI rationale

> The main article calls age strata \<50, 50-69, and \>=70 prespecified, whereas the supplied SAP specifies two groups split at 65; this is a reported-versus-prespecified subgroup definition discrepancy.

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

> The SAP lists a priori age subgroups \<65 years and \>65 years. The article labels results prespecified and Figure 3 displays \<50, 50-69, and ≥70 years.

#### Evidence 1: Reported-versus-comparator

> Two SAP groups bounded at 65 versus three reported groups bounded at 50 and 70.

#### Evidence 2: Calculation

> The number of groups changes from 2 to 3; neither Figure 3 boundary is 65 years.

#### Evidence 3: Alternative source-grounded interpretations

> A final/amended plan could have authorized the Figure 3 categories, or the article could refer to a broader prespecification record. No such record is supplied. The SAP's literal wording also leaves age 65 unspecified.

### Source links

- sourceLinks 0: [SAP — PDF p. 7](../../../2018/jama.2017.21906/joi170166supp2_prod.pdf#page=7)
- sourceLinks 1: [main article — PDF p. 3](../../../2018/jama.2017.21906/jama_huffman_2018_oi_170166.pdf#page=3)
- sourceLinks 2: [main article — PDF p. 9](../../../2018/jama.2017.21906/jama_huffman_2018_oi_170166.pdf#page=9)
- evidencePaths 0: [2018/jama.2017.21906/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2017.21906/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2017.21906/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2017.21906/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)

[Original Markdown report](../../../2018/jama.2017.21906/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | A later or separate prespecification could authorize the published cutpoints; no such dated record is supplied. The SAP age-65 gap is contextual, not a separate counted relationship. |
| broadPlanInvolved | 1 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C004 |
| key | 2018::jama.2017.21906::C004 |
| legacyRelationship |  |
| locations | SAP — PDF p. 7, section 7.5.2; main article — PDF p. 3, Statistical Analysis; main article — PDF p. 9, Figure 3 and adjacent Results narrative. |
| originalCrossDocument | 1 |
| package | jama.2017.21906 |
| planMechanism | analysis\_specification |
| primary | P\_R |
| rationale | The main article calls age strata \<50, 50-69, and \>=70 prespecified, whereas the supplied SAP specifies two groups split at 65; this is a reported-versus-prespecified subgroup definition discrepancy. |
| reportHref | ../../2018/jama.2017.21906/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2017.21906/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C004 |
| sourceStatus | Pending Human Adjudication |
| statement | The article calls its Figure 3 age subgroups prespecified, but their numeric boundaries differ from the supplied SAP. |
| submissionInvolved | 0 |
| subtype | subgroup\_cutpoint\_prespecification |
| suggestedDomain | protocol\_report |
| title | Reported prespecified age-subgroup boundaries differ from the supplied SAP |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | retain |

## Candidate C005

**The named optimal in-hospital medication composite uses different component labels across final-result tables**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2017.21906::C005 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> Main article — PDF p. 3, Outcomes; main article — PDF p. 7, Table 3 footnote c; online supplement — PDF p. 21, eTable 5 footnote c; online supplement — PDF p. 22, eTable 6 footnote b.

### Candidate statement

> The same named optimal in-hospital medication composite is defined with anticoagulant in the article/eTable 5 and heparin in eTable 6.

### AI rationale

> The main article and results-supplement eTable 5 define the medication composite using anticoagulant; eTable 6 in the same results supplement says heparin. The cross-file component mismatch and the eTable 5/eTable 6 within-file mismatch are both substantive.

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

> Article/Table 3/eTable 5 list aspirin, an ADP-receptor antagonist, anticoagulant, and beta-blocker. eTable 6 uses the same composite name but lists heparin as the fourth component.

#### Evidence 1: Reported-versus-comparator

> Three components match; the fourth is anticoagulant versus heparin.

#### Evidence 2: Calculation

> Set comparison: aspirin, ADP-receptor antagonist, and beta-blocker are shared; the fourth printed label differs.

#### Evidence 3: Alternative source-grounded interpretations

> If heparin was the only qualifying anticoagulant in analyzed records, the labels may be extensionally equivalent. Medication coding, eligibility rules, and table-generation code are absent.

### Source links

- sourceLinks 0: [Main article — PDF p. 3](../../../2018/jama.2017.21906/jama_huffman_2018_oi_170166.pdf#page=3)
- sourceLinks 1: [main article — PDF p. 7](../../../2018/jama.2017.21906/jama_huffman_2018_oi_170166.pdf#page=7)
- sourceLinks 2: [online supplement — PDF p. 21](../../../2018/jama.2017.21906/joi170166supp3_prod.pdf#page=21)
- sourceLinks 3: [online supplement — PDF p. 22](../../../2018/jama.2017.21906/joi170166supp3_prod.pdf#page=22)
- evidencePaths 0: [2018/jama.2017.21906/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2017.21906/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2017.21906/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2017.21906/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)

[Original Markdown report](../../../2018/jama.2017.21906/.ai_paper_validation/final_report_1_5_2.md)

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
| ambiguity | Mixed cross-file and within-supplement relationship. Heparin may exhaust the operative anticoagulant class; operational equivalence is unknown. |
| broadPlanInvolved | 0 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 1 |
| id | C005 |
| key | 2018::jama.2017.21906::C005 |
| legacyRelationship |  |
| locations | Main article — PDF p. 3, Outcomes; main article — PDF p. 7, Table 3 footnote c; online supplement — PDF p. 21, eTable 5 footnote c; online supplement — PDF p. 22, eTable 6 footnote b. |
| originalCrossDocument | 0 |
| package | jama.2017.21906 |
| planMechanism |  |
| primary | S\_C |
| rationale | The main article and results-supplement eTable 5 define the medication composite using anticoagulant; eTable 6 in the same results supplement says heparin. The cross-file component mismatch and the eTable 5/eTable 6 within-file mismatch are both substantive. |
| reportHref | ../../2018/jama.2017.21906/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2017.21906/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C005 |
| sourceStatus | Pending Human Adjudication |
| statement | The same named optimal in-hospital medication composite is defined with anticoagulant in the article/eTable 5 and heparin in eTable 6. |
| submissionInvolved | 1 |
| subtype | composite\_component\_definition |
| suggestedDomain | report\_internal\_inconsistency |
| title | The named optimal in-hospital medication composite uses different component labels across final-result tables |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C006

**Hospital-type subgroup is reported as prespecified but is absent from the supplied SAP subgroup list**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2017.21906::C006 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> Main article — PDF p. 3, Statistical Analysis; main article — PDF p. 9, Figure 3 and adjacent Results narrative; SAP — PDF p. 7, section 7.5.2.

### Candidate statement

> The article calls the hospital-type Figure 3 subgroup prespecified, while the supplied SAP's a priori site-level subgroup list does not name hospital type.

### AI rationale

> Hospital type (government/nonprofit/private) is presented as prespecified in the main Figure 3 but absent from the supplied SAP site-level subgroup list. This compares reported prespecification with the plan, not main versus ordinary supplementary results.

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

> The article labels hospital type prespecified and Figure 3 prints government (9 hospitals), nonprofit (12), and private (42). The SAP lists hospital size and use of quality-improvement toolkit components as site-level a priori subgroups, not hospital type.

#### Evidence 1: Reported-versus-comparator

> Article/Figure 3 includes hospital type; the supplied SAP list includes toolkit-component use and does not name hospital type.

#### Evidence 2: Calculation

> 9 + 12 + 42 = 63 hospitals. This confirms an implemented full hospital partition, not prespecification.

#### Evidence 3: Alternative source-grounded interpretations

> A separate or amended plan could have added hospital type and changed/omitted toolkit-component use before analysis. No such record is included.

### Source links

- sourceLinks 0: [Main article — PDF p. 3](../../../2018/jama.2017.21906/jama_huffman_2018_oi_170166.pdf#page=3)
- sourceLinks 1: [main article — PDF p. 9](../../../2018/jama.2017.21906/jama_huffman_2018_oi_170166.pdf#page=9)
- sourceLinks 2: [SAP — PDF p. 7](../../../2018/jama.2017.21906/joi170166supp2_prod.pdf#page=7)
- evidencePaths 0: [2018/jama.2017.21906/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2017.21906/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2017.21906/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | An amended or separate plan may account for hospital type; the record establishes differing lists rather than intentional substitution. |
| broadPlanInvolved | 1 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C006 |
| key | 2018::jama.2017.21906::C006 |
| legacyRelationship |  |
| locations | Main article — PDF p. 3, Statistical Analysis; main article — PDF p. 9, Figure 3 and adjacent Results narrative; SAP — PDF p. 7, section 7.5.2. |
| originalCrossDocument | 1 |
| package | jama.2017.21906 |
| planMechanism | analysis\_specification |
| primary | P\_R |
| rationale | Hospital type (government/nonprofit/private) is presented as prespecified in the main Figure 3 but absent from the supplied SAP site-level subgroup list. This compares reported prespecification with the plan, not main versus ordinary supplementary results. |
| reportHref | ../../2018/jama.2017.21906/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2017.21906/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C006 |
| sourceStatus | Pending Human Adjudication |
| statement | The article calls the hospital-type Figure 3 subgroup prespecified, while the supplied SAP's a priori site-level subgroup list does not name hospital type. |
| submissionInvolved | 0 |
| subtype | subgroup\_prespecification |
| suggestedDomain | protocol\_report |
| title | Hospital-type subgroup is reported as prespecified but is absent from the supplied SAP subgroup list |
| year | 2018 |
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
