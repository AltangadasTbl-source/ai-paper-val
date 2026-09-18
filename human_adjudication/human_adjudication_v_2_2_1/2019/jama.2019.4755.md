# jama.2019.4755

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2019 |
| Paper | jama.2019.4755 |
| Candidates | 5 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2019/jama.2019.4755/)

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

- [C001](#candidate-c001) — Women’s quantitative 10.2 µg Hb/g PPV difference point estimate is absent (S_W)
- [C002](#candidate-c002) — Women’s quantitative 17.0 µg Hb/g PPV difference point estimate is absent (S_W)
- [C003](#candidate-c003) — Women’s qualitative 10.2 µg Hb/g PPV difference point estimate is absent (S_W)
- [C004](#candidate-c004) — eTable 5 visible cutoff header truncates after \[µg (S_W)
- [C005](#candidate-c005) — One SAP occurrence omits the microgram prefix from the 10.2 cutoff (P_P)

## Candidate C001

**Women’s quantitative 10.2 µg Hb/g PPV difference point estimate is absent**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.4755::C001 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> joi190039supp3\_prod.pdf — PDF p. 7, DOC-004 eTable 5, Women/Quantitative/10.2, Difference in PPV; comparator joi190039supp3\_prod.pdf — PDF p. 6, DOC-004 eTable 4, same population, test, cutoff, day, and per-protocol analysis.

### Candidate statement

> In the Women/Quantitative/10.2 row of eTable 5, the Difference in PPV point-estimate position visibly contains only a hyphen although both arm PPVs and a negative confidence interval are printed.

### AI rationale

> Results-supplement eTable5 women quantitative10.2 PPV-difference cell visibly lacks numeric magnitude despite arm PPVs and a CI; matched eTable4 diagnostic counts are in the same supplement.

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

> Page 7 visibly prints aspirin PPV 15.9%, placebo PPV 34.1%, a lone hyphen in the point-estimate position, and 95% CI \[-34.7, -1.3\]. Page 6 prints TP/FP 11/58 for aspirin and 14/27 for placebo.

#### Evidence 1: Reported-versus-comparator

> The reported cell is - versus a numeric aspirin-minus-placebo PPV difference that is diagnostically supported by the matched counts and displayed arm PPVs; no numeric magnitude is visibly rendered in the cell.

#### Evidence 2: Calculation

> 11/(11+58) × 100 = 15.9420%; 14/(14+27) × 100 = 34.1463%; aspirin minus placebo = -18.2043 percentage points, rounding to -18.2. The displayed values also give 15.9 - 34.1 = -18.2.

#### Evidence 3: Alternative source-grounded interpretations

> A detached 18.2 PDF text fragment may indicate displaced, clipped, or suppressed table content, but the direct rendering does not visibly connect it to the cell. Alternatively, an undocumented hyphen-only convention may have been intended.

### Source links

- sourceLinks 0: [joi190039supp3\_prod.pdf — PDF p. 7](../../../2019/jama.2019.4755/joi190039supp3_prod.pdf#page=7)
- sourceLinks 1: [joi190039supp3\_prod.pdf — PDF p. 6](../../../2019/jama.2019.4755/joi190039supp3_prod.pdf#page=6)
- evidencePaths 0: [2019/jama.2019.4755/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.4755/.ai_paper_validation/review_1_5_1/source_inventory.md)

[Original Markdown report](../../../2019/jama.2019.4755/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Detached PDF numeric text may indicate clipping/displacement; a hyphen convention is not defined. Each candidate concerns a distinct test/cutoff row. |
| broadPlanInvolved | 0 |
| category | Numeric or arithmetic inconsistency |
| currentReportCrossDocument | 0 |
| id | C001 |
| key | 2019::jama.2019.4755::C001 |
| legacyRelationship |  |
| locations | joi190039supp3\_prod.pdf — PDF p. 7, DOC-004 eTable 5, Women/Quantitative/10.2, Difference in PPV; comparator joi190039supp3\_prod.pdf — PDF p. 6, DOC-004 eTable 4, same population, test, cutoff, day, and per-protocol analysis. |
| originalCrossDocument | 0 |
| package | jama.2019.4755 |
| planMechanism |  |
| primary | S\_W |
| rationale | Results-supplement eTable5 women quantitative10.2 PPV-difference cell visibly lacks numeric magnitude despite arm PPVs and a CI; matched eTable4 diagnostic counts are in the same supplement. |
| reportHref | ../../2019/jama.2019.4755/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.4755/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | In the Women/Quantitative/10.2 row of eTable 5, the Difference in PPV point-estimate position visibly contains only a hyphen although both arm PPVs and a negative confidence interval are printed. |
| submissionInvolved | 1 |
| subtype | missing\_point\_estimate |
| suggestedDomain | statistical\_results |
| title | Women’s quantitative 10.2 µg Hb/g PPV difference point estimate is absent |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C002

**Women’s quantitative 17.0 µg Hb/g PPV difference point estimate is absent**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.4755::C002 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> joi190039supp3\_prod.pdf — PDF p. 7, DOC-004 eTable 5, Women/Quantitative/17.0, Difference in PPV; comparator joi190039supp3\_prod.pdf — PDF p. 6, DOC-004 eTable 4, same population, test, cutoff, day, and per-protocol analysis.

### Candidate statement

> In the Women/Quantitative/17.0 row of eTable 5, the Difference in PPV point-estimate position visibly contains only a hyphen although both arm PPVs and a negative confidence interval are printed.

### AI rationale

> Results-supplement eTable5 women quantitative17.0 PPV-difference cell visibly lacks numeric magnitude despite arm PPVs and a CI; matched eTable4 diagnostic counts are in the same supplement.

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

> Page 7 visibly prints aspirin PPV 17.1%, placebo PPV 42.9%, a lone hyphen in the point-estimate position, and 95% CI \[-48.4, -0.7\]. Page 6 prints TP/FP 6/29 for aspirin and 9/12 for placebo.

#### Evidence 1: Reported-versus-comparator

> The reported cell is - versus a count-derived diagnostic difference that rounds to -25.7 percentage points; subtracting the independently rounded printed PPVs gives -25.8. Neither numeric value is visibly printed in the named cell.

#### Evidence 2: Calculation

> 6/(6+29) × 100 = 17.1429%; 9/(9+12) × 100 = 42.8571%; count-derived aspirin minus placebo = -25.7143, rounding to -25.7 percentage points. Displayed-value subtraction is 17.1 - 42.9 = -25.8; the 0.1-point difference is compatible with rounding paths.

#### Evidence 3: Alternative source-grounded interpretations

> A detached 25.7 PDF text fragment may indicate displaced, clipped, or suppressed content, but it is not visible in the cell. The intended display may have used unrounded proportions, or the hyphen may represent an undocumented convention.

### Source links

- sourceLinks 0: [joi190039supp3\_prod.pdf — PDF p. 7](../../../2019/jama.2019.4755/joi190039supp3_prod.pdf#page=7)
- sourceLinks 1: [joi190039supp3\_prod.pdf — PDF p. 6](../../../2019/jama.2019.4755/joi190039supp3_prod.pdf#page=6)
- evidencePaths 0: [2019/jama.2019.4755/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.4755/.ai_paper_validation/review_1_5_1/source_inventory.md)

[Original Markdown report](../../../2019/jama.2019.4755/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Detached PDF numeric text may indicate clipping/displacement; a hyphen convention is not defined. Each candidate concerns a distinct test/cutoff row. |
| broadPlanInvolved | 0 |
| category | Numeric or arithmetic inconsistency |
| currentReportCrossDocument | 0 |
| id | C002 |
| key | 2019::jama.2019.4755::C002 |
| legacyRelationship |  |
| locations | joi190039supp3\_prod.pdf — PDF p. 7, DOC-004 eTable 5, Women/Quantitative/17.0, Difference in PPV; comparator joi190039supp3\_prod.pdf — PDF p. 6, DOC-004 eTable 4, same population, test, cutoff, day, and per-protocol analysis. |
| originalCrossDocument | 0 |
| package | jama.2019.4755 |
| planMechanism |  |
| primary | S\_W |
| rationale | Results-supplement eTable5 women quantitative17.0 PPV-difference cell visibly lacks numeric magnitude despite arm PPVs and a CI; matched eTable4 diagnostic counts are in the same supplement. |
| reportHref | ../../2019/jama.2019.4755/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.4755/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | In the Women/Quantitative/17.0 row of eTable 5, the Difference in PPV point-estimate position visibly contains only a hyphen although both arm PPVs and a negative confidence interval are printed. |
| submissionInvolved | 1 |
| subtype | missing\_point\_estimate |
| suggestedDomain | statistical\_results |
| title | Women’s quantitative 17.0 µg Hb/g PPV difference point estimate is absent |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C003

**Women’s qualitative 10.2 µg Hb/g PPV difference point estimate is absent**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.4755::C003 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> joi190039supp3\_prod.pdf — PDF p. 7, DOC-004 eTable 5, Women/Qualitative/10.2, Difference in PPV; comparator joi190039supp3\_prod.pdf — PDF p. 6, DOC-004 eTable 4, same population, test, cutoff, day, and per-protocol analysis.

### Candidate statement

> In the Women/Qualitative/10.2 row of eTable 5, the Difference in PPV point-estimate position visibly contains only a hyphen although both arm PPVs and a negative confidence interval are printed.

### AI rationale

> Results-supplement eTable5 women qualitative10.2 PPV-difference cell visibly lacks numeric magnitude despite arm PPVs and a CI; matched eTable4 diagnostic counts are in the same supplement.

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

> Page 7 visibly prints aspirin PPV 9.7%, placebo PPV 31.2%, a lone hyphen in the point-estimate position, and 95% CI \[-38.9, -3.9\]. Page 6 prints TP/FP 6/56 for aspirin and 10/22 for placebo.

#### Evidence 1: Reported-versus-comparator

> The reported cell is - versus a count-derived diagnostic difference that rounds to -21.6 percentage points; displayed-value subtraction gives -21.5. No numeric magnitude is visibly printed in the cell.

#### Evidence 2: Calculation

> 6/(6+56) × 100 = 9.6774%; 10/(10+22) × 100 = 31.2500%; count-derived aspirin minus placebo = -21.5726, rounding to -21.6 percentage points. Displayed-value subtraction is 9.7 - 31.2 = -21.5; the difference is compatible with independent rounding.

#### Evidence 3: Alternative source-grounded interpretations

> A detached 21.6 PDF text fragment may reflect displacement, clipping, or suppression during production without establishing that mechanism. The hyphen could instead be an undocumented display convention.

### Source links

- sourceLinks 0: [joi190039supp3\_prod.pdf — PDF p. 7](../../../2019/jama.2019.4755/joi190039supp3_prod.pdf#page=7)
- sourceLinks 1: [joi190039supp3\_prod.pdf — PDF p. 6](../../../2019/jama.2019.4755/joi190039supp3_prod.pdf#page=6)
- evidencePaths 0: [2019/jama.2019.4755/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.4755/.ai_paper_validation/review_1_5_1/source_inventory.md)

[Original Markdown report](../../../2019/jama.2019.4755/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Detached PDF numeric text may indicate clipping/displacement; a hyphen convention is not defined. Each candidate concerns a distinct test/cutoff row. |
| broadPlanInvolved | 0 |
| category | Numeric or arithmetic inconsistency |
| currentReportCrossDocument | 0 |
| id | C003 |
| key | 2019::jama.2019.4755::C003 |
| legacyRelationship |  |
| locations | joi190039supp3\_prod.pdf — PDF p. 7, DOC-004 eTable 5, Women/Qualitative/10.2, Difference in PPV; comparator joi190039supp3\_prod.pdf — PDF p. 6, DOC-004 eTable 4, same population, test, cutoff, day, and per-protocol analysis. |
| originalCrossDocument | 0 |
| package | jama.2019.4755 |
| planMechanism |  |
| primary | S\_W |
| rationale | Results-supplement eTable5 women qualitative10.2 PPV-difference cell visibly lacks numeric magnitude despite arm PPVs and a CI; matched eTable4 diagnostic counts are in the same supplement. |
| reportHref | ../../2019/jama.2019.4755/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.4755/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | In the Women/Qualitative/10.2 row of eTable 5, the Difference in PPV point-estimate position visibly contains only a hyphen although both arm PPVs and a negative confidence interval are printed. |
| submissionInvolved | 1 |
| subtype | missing\_point\_estimate |
| suggestedDomain | statistical\_results |
| title | Women’s qualitative 10.2 µg Hb/g PPV difference point estimate is absent |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C004

**eTable 5 visible cutoff header truncates after \[µg**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.4755::C004 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> joi190039supp3\_prod.pdf — PDF p. 7, DOC-004 eTable 5 visible cutoff header; comparator joi190039supp3\_prod.pdf — PDF p. 6, DOC-004 eTable 4 header Cutoff \[µg Hb/g\]; additional matched main-table display jama\_brenner\_2019\_oi\_190039.pdf — PDF p. 5.

### Candidate statement

> eTable 5 visibly renders Cutoff and a second-line \[µg fragment, without visibly rendered Hb/g\], while matched cutoff displays use the full µg Hb/g scale.

### AI rationale

> Results-supplement eTable5 cutoff header truncates at\[µg while adjacent eTable4 in the same file prints fullµgHb/g. Main tables corroborate the unit; the target is an incomplete internal supplemental header.

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

> The direct rendering on page 7 visibly shows Cutoff and \[µg; neither Hb/g nor the closing bracket is visibly rendered. The same page applies cutoff values 10.2 and 17.0. Page 6 visibly renders Cutoff \[µg Hb/g\] for the corresponding day-2 per-protocol FIT context.

#### Evidence 1: Reported-versus-comparator

> The visible eTable 5 label ends at \[µg versus the matched eTable 4 and main-table concentration scale µg Hb/g. The incomplete string is the direct observation; the complete form is the comparator, not an asserted transcription of page 7.

#### Evidence 2: Calculation

> No arithmetic is applicable. The reproducible comparison is the visible incomplete mass-unit fragment \[µg against the matched mass-per-mass scale µg Hb/g.

#### Evidence 3: Alternative source-grounded interpretations

> A detached Hb/g\] PDF text fragment supports a possible layout or clipping explanation but is not visibly connected to the header. Readers may have been expected to carry the unit from adjacent tables, although the page gives no such instruction.

### Source links

- sourceLinks 0: [joi190039supp3\_prod.pdf — PDF p. 7](../../../2019/jama.2019.4755/joi190039supp3_prod.pdf#page=7)
- sourceLinks 1: [joi190039supp3\_prod.pdf — PDF p. 6](../../../2019/jama.2019.4755/joi190039supp3_prod.pdf#page=6)
- sourceLinks 2: [jama\_brenner\_2019\_oi\_190039.pdf — PDF p. 5](../../../2019/jama.2019.4755/jama_brenner_2019_oi_190039.pdf#page=5)
- evidencePaths 0: [2019/jama.2019.4755/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.4755/.ai_paper_validation/review_1_5_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.4755/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.4755/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2019/jama.2019.4755/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | A detached Hb/g\] text object supports possible clipping; no unit-inheritance rule is printed. |
| broadPlanInvolved | 0 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C004 |
| key | 2019::jama.2019.4755::C004 |
| legacyRelationship |  |
| locations | joi190039supp3\_prod.pdf — PDF p. 7, DOC-004 eTable 5 visible cutoff header; comparator joi190039supp3\_prod.pdf — PDF p. 6, DOC-004 eTable 4 header Cutoff \[µg Hb/g\]; additional matched main-table display jama\_brenner\_2019\_oi\_190039.pdf — PDF p. 5. |
| originalCrossDocument | 0 |
| package | jama.2019.4755 |
| planMechanism |  |
| primary | S\_W |
| rationale | Results-supplement eTable5 cutoff header truncates at\[µg while adjacent eTable4 in the same file prints fullµgHb/g. Main tables corroborate the unit; the target is an incomplete internal supplemental header. |
| reportHref | ../../2019/jama.2019.4755/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.4755/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C004 |
| sourceStatus | Pending Human Adjudication |
| statement | eTable 5 visibly renders Cutoff and a second-line \[µg fragment, without visibly rendered Hb/g\], while matched cutoff displays use the full µg Hb/g scale. |
| submissionInvolved | 1 |
| subtype | truncated\_unit |
| suggestedDomain | report\_internal\_inconsistency |
| title | eTable 5 visible cutoff header truncates after \[µg |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C005

**One SAP occurrence omits the microgram prefix from the 10.2 cutoff**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.4755::C005 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> joi190039supp2\_prod.pdf — PDF p. 6, DOC-003 §3.2; comparator joi190039supp2\_prod.pdf — PDF p. 8, DOC-003 §5.4; matched context jama\_brenner\_2019\_oi\_190039.pdf — PDF p. 1 and jama\_brenner\_2019\_oi\_190039.pdf — PDF p. 5.

### Candidate statement

> One SAP sentence prints 17 μg Hb/g feces and 10.2 Hb/g feces, while matched occurrences specify the lower cutoff as 10.2 μg Hb/g feces.

### AI rationale

> SAP section3.2 omitsµg locally from10.2Hb/g while section5.4 in the same SAP prints10.2µgHb/g. The main article supplies matched context only, so this is an internal-plan unit wording issue.

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

> DOC-003 p. 6 visibly prints 17 μg Hb/g feces and 10.2 Hb/g feces. DOC-003 p. 8 prints Manufacturer’s threshold (17 μg Hb/g feces) and threshold for positivity (10.2 μg Hb/g feces). The article supplies the same two FIT-cutoff context and complete unit headers.

#### Evidence 1: Reported-versus-comparator

> The lower cutoff is printed as 10.2 Hb/g feces on p. 6 versus 10.2 μg Hb/g feces on p. 8 for the same lower quantitative-FIT threshold.

#### Evidence 2: Calculation

> No arithmetic is required. The logical comparison checks whether the same 10.2 cutoff retains its μg numerator unit across the matched SAP occurrences.

#### Evidence 3: Alternative source-grounded interpretations

> The first μg may be intended to govern both coordinated thresholds grammatically. Because Hb/g feces is repeated after both numbers, that inheritance is not explicit; the package gives no editorial rule resolving it.

### Source links

- sourceLinks 0: [joi190039supp2\_prod.pdf — PDF p. 6](../../../2019/jama.2019.4755/joi190039supp2_prod.pdf#page=6)
- sourceLinks 1: [joi190039supp2\_prod.pdf — PDF p. 8](../../../2019/jama.2019.4755/joi190039supp2_prod.pdf#page=8)
- sourceLinks 2: [jama\_brenner\_2019\_oi\_190039.pdf — PDF p. 1](../../../2019/jama.2019.4755/jama_brenner_2019_oi_190039.pdf#page=1)
- sourceLinks 3: [jama\_brenner\_2019\_oi\_190039.pdf — PDF p. 5](../../../2019/jama.2019.4755/jama_brenner_2019_oi_190039.pdf#page=5)
- evidencePaths 0: [2019/jama.2019.4755/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.4755/.ai_paper_validation/review_1_5_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.4755/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.4755/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2019/jama.2019.4755/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_P |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | The firstµg in the coordinated sentence may grammatically apply to both thresholds; no inheritance convention is supplied. |
| broadPlanInvolved | 1 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C005 |
| key | 2019::jama.2019.4755::C005 |
| legacyRelationship |  |
| locations | joi190039supp2\_prod.pdf — PDF p. 6, DOC-003 §3.2; comparator joi190039supp2\_prod.pdf — PDF p. 8, DOC-003 §5.4; matched context jama\_brenner\_2019\_oi\_190039.pdf — PDF p. 1 and jama\_brenner\_2019\_oi\_190039.pdf — PDF p. 5. |
| originalCrossDocument | 0 |
| package | jama.2019.4755 |
| planMechanism |  |
| primary | P\_P |
| rationale | SAP section3.2 omitsµg locally from10.2Hb/g while section5.4 in the same SAP prints10.2µgHb/g. The main article supplies matched context only, so this is an internal-plan unit wording issue. |
| reportHref | ../../2019/jama.2019.4755/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.4755/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C005 |
| sourceStatus | Pending Human Adjudication |
| statement | One SAP sentence prints 17 μg Hb/g feces and 10.2 Hb/g feces, while matched occurrences specify the lower cutoff as 10.2 μg Hb/g feces. |
| submissionInvolved | 0 |
| subtype | unit\_omission |
| suggestedDomain | plan\_material |
| title | One SAP occurrence omits the microgram prefix from the 10.2 cutoff |
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
