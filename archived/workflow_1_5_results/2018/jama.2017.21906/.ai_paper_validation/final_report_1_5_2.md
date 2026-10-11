# Quantitative Quality-Control Consistency Review: Huffman et al. Paper Package

## Pending Human Adjudication

Every candidate in this report is **Pending Human Adjudication**. This is a source-limited quantitative reporting quality-control review, not a correction, acceptance decision, exclusion decision, or broad clinical/methodological audit.

## Executive Quality-Control Summary

Complete fresh source coverage identified **6** distinct reporting-consistency candidates, C001-C006. The candidates concern repeated adjusted effects, a comparison-footnote label, prespecified-subgroup definitions, and a repeated composite definition. All six were mechanically rechecked at their exact supplied-source locations. No candidate is ranked, suppressed, or assigned a severity or final disposition.

## Package and Fresh-Processing Provenance

The direct-source package contains four supplied PDFs: [main article](<../jama_huffman_2018_oi_170166.pdf#page=1>), [protocol](<../joi170166supp1_prod.pdf#page=1>), [statistical analysis plan (SAP)](<../joi170166supp2_prod.pdf#page=1>), and [online supplement](<../joi170166supp3_prod.pdf#page=1>). Fresh native and layout text were produced for all sources. Result-relevant pages were rendered. DOC-004 pp. 3-16 had unusable native/layout text; consistent with the user direction, only the supplied page- and SHA-matched OCR was used as a fallback for those pages, with no new OCR. Direct PDFs remain the evidence authority.

## Scope, Complete Coverage, and Exclusions

All **80/80** direct PDF-page units were freshly required and mapped: DOC-001 12/12, DOC-002 32/32, DOC-003 9/9, and DOC-004 27/27. No prior audit findings or derivatives were used as evidence inputs. The review considered numeric, denominator/proportion/total, inferential-statistical, cross-document, effect-label/scale, and rate-versus-count relationships. It did not conduct a raw-data, clinical, misconduct, novelty, or broad study-design audit.

## Quantitative and Statistical Relationship Coverage

The numeric/reporting mapping and checks cover **53** relationships (N001-N037 and N300-N315). The inferential/statistical inventory covers **65/65** relationships (S001-S053 and S300-S311). Both independent statistical passes completed every statistical relationship: pass 1 (`/root/statistical_pass_1`, gpt-5.6-terra, high) and pass 2 (`/root/statistical_pass_2`, gpt-5.6-terra, high). Pass 2 added C006, which was then mechanically rechecked. No candidate is based on a coherent display-zero P value.

## Candidate Index

| ID | Category | Short description | Status |
|---|---|---|---|
| C001 | Statistical reporting inconsistency | In-hospital beta-blocker adjusted risk-difference CI upper endpoint differs between Table 2 and narrative. | Pending Human Adjudication |
| C002 | Cross-document numeric inconsistency | Discharge beta-blocker adjusted point estimates differ between Table 2 and narrative. | Pending Human Adjudication |
| C003 | Measure, label, or scale inconsistency | eTable 1 difference footnote names groups not displayed in the table. | Pending Human Adjudication |
| C004 | Cross-document numeric inconsistency | Reported prespecified age-subgroup boundaries differ from the supplied SAP. | Pending Human Adjudication |
| C005 | Measure, label, or scale inconsistency | Named optimal in-hospital medication composite has different component labels across final-result tables. | Pending Human Adjudication |
| C006 | Cross-document numeric inconsistency | Hospital-type subgroup is reported as prespecified but is absent from the supplied SAP subgroup list. | Pending Human Adjudication |

## Candidate Evidence Cards

## C001 — In-hospital beta-blocker adjusted-risk-difference CI endpoint differs between Table 2 and narrative

**Candidate statement:** The same named adjusted in-hospital beta-blocker result prints different upper risk-difference CI endpoints.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [Main article — PDF p. 6](<../jama_huffman_2018_oi_170166.pdf#page=6>), Table 2 `In-hospital β-blocker` row and adjacent Results narrative.

**Source evidence:** Table 2 prints adjusted risk difference 6.25% (95% CI, 4.10% to 8.40%) and OR 1.46 (1.29 to 1.65). The adjacent narrative prints 6.25% (4.10% to 8.10%) and OR 1.46 (1.29 to 1.65).

**Reported-versus-comparator:** Table upper endpoint 8.40% versus narrative upper endpoint 8.10%; the point estimate, lower endpoint, OR, and OR interval agree as printed.

**Reasoning procedure:** Directly observed are the two printed endpoints. Treating the occurrences as the same adjusted result is an inference supported by the same outcome, contrast, point estimate, lower endpoint, OR, and OR interval; no second analysis is identified.

**Calculation:** 8.40 - 8.10 = 0.30 percentage point.

**Alternative source-grounded interpretations:** One occurrence may be a transcription/production error, or the narrative may use an unlabelled distinct output. The supplied package does not establish either explanation or which endpoint is supported by final model output.

**Mechanical evidence recheck:** Both values and their exact locations were found; necessary printed inputs reproduce the mismatch. Unrounded marginal-effect output, execution records, and production files are absent.

**Quality-control relevance:** A same-result repetition should retain its displayed CI endpoint unless it identifies a distinct analysis.

**Potential downstream evidence impact:** If confirmed, a systematic-review or meta-analysis extractor could copy either 8.10% or 8.40% as the upper CI endpoint; no propagation or conclusion change is established.

**Human verification steps:** Retrieve the final adjusted in-hospital beta-blocker output and the table/narrative production records; determine which upper endpoint is supported and whether a distinct analysis existed.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Discharge beta-blocker adjusted point estimates differ between Table 2 and narrative

**Candidate statement:** Table 2 and the narrative print different adjusted discharge beta-blocker risk differences and ORs while printing identical intervals.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [Main article — PDF p. 6](<../jama_huffman_2018_oi_170166.pdf#page=6>), Table 2 `Discharge β-blocker` row; [Main article — PDF p. 7](<../jama_huffman_2018_oi_170166.pdf#page=7>), Results narrative.

**Source evidence:** Table 2 prints risk difference 6.69% (4.43% to 8.95%) and OR 1.48 (1.30 to 1.68). The narrative prints 6.63% with 4.43% to 8.95% and OR 1.47 with 1.30 to 1.68.

**Reported-versus-comparator:** Table 2 6.69%/1.48 versus narrative 6.63%/1.47, with both printed risk-difference and OR intervals identical.

**Reasoning procedure:** The estimate pairs and intervals are direct observations. Their identity as one result is inferred from the named discharge outcome, contrast, adjustment presentation, and identical intervals; no distinct model or population is named.

**Calculation:** 6.69 - 6.63 = 0.06 percentage point; 1.48 - 1.47 = 0.01.

**Alternative source-grounded interpretations:** A transcription/output-selection issue or an unlabelled distinct analytic run could explain the values. The package lacks unrounded output, code, and production history, so no cause is established.

**Mechanical evidence recheck:** Both page-specific source occurrences and all printed intervals were found. The mismatch is reproducible from the displayed values.

**Quality-control relevance:** A repeated adjusted outcome should preserve displayed point estimates at the stated precision unless a distinct analysis is labelled.

**Potential downstream evidence impact:** If confirmed, an extractor could select 6.69%/1.48 or 6.63%/1.47 for the same named result; no downstream propagation or conclusion change is shown.

**Human verification steps:** Compare final model output, eligible discharge population, and narrative/table production records to establish whether both locations derive from one adjusted analysis and which estimates it supports.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — eTable 1 difference footnote names groups not displayed in the table

**Candidate statement:** eTable 1 displays complete- and missing-follow-up groups, but its difference footnote defines an intervention-minus-control contrast.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [Online supplement — PDF p. 17](<../joi170166supp3_prod.pdf#page=17>), eTable 1 title, headers, values, and footnote a.

**Source evidence:** The columns are `Complete Follow Up` (n=21,079), `Missing Follow Up` (n=295), and `Difference (95% CI)`; footnote a states `Difference = intervention minus control.`

**Reported-versus-comparator:** The footnote names intervention/control, while the displayed comparison groups are complete/missing follow-up.

**Reasoning procedure:** Headers, footnote, and values are direct observations. Checked row arithmetic shows missing minus complete; a carried-over footnote is only a possible explanation.

**Calculation:** Age: 60.0 - 60.6 = -0.6; male percentage: 71.2 - 75.8 = -4.6; initial troponin: 4.6 - 1.3 = 3.3.

**Alternative source-grounded interpretations:** The footnote may have been carried over from eTable 2, while eTable 1 may intentionally use missing minus complete. The source does not define every CI contrast or table-production history.

**Mechanical evidence recheck:** The title, group sizes, footnote, and checked values were found on the cited page. The printed point differences reproduce the displayed follow-up-group direction.

**Quality-control relevance:** A difference label should name the displayed groups and comparator order.

**Potential downstream evidence impact:** If confirmed, a reviewer or data extractor could assign differences to the wrong comparator or reverse their direction; no actual extraction error or conclusion change is established.

**Human verification steps:** Obtain the eTable 1 shell/code and confirm the comparator order, sign convention, and CI calculation for every row.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Reported prespecified age-subgroup boundaries differ from the supplied SAP

**Candidate statement:** The article calls its Figure 3 age subgroups prespecified, but their numeric boundaries differ from the supplied SAP.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [SAP — PDF p. 7](<../joi170166supp2_prod.pdf#page=7>), section 7.5.2; [main article — PDF p. 3](<../jama_huffman_2018_oi_170166.pdf#page=3>), Statistical Analysis; [main article — PDF p. 9](<../jama_huffman_2018_oi_170166.pdf#page=9>), Figure 3 and adjacent Results narrative.

**Source evidence:** The SAP lists a priori age subgroups `<65 years` and `>65 years`. The article labels results prespecified and Figure 3 displays `<50`, `50-69`, and `≥70` years.

**Reported-versus-comparator:** Two SAP groups bounded at 65 versus three reported groups bounded at 50 and 70.

**Reasoning procedure:** The cut points and prespecified labels are direct observations. Whether an unsupplied amendment or broader prespecification exists is an inference, not evidence in this package.

**Calculation:** The number of groups changes from 2 to 3; neither Figure 3 boundary is 65 years.

**Alternative source-grounded interpretations:** A final/amended plan could have authorized the Figure 3 categories, or the article could refer to a broader prespecification record. No such record is supplied. The SAP's literal wording also leaves age 65 unspecified.

**Mechanical evidence recheck:** The SAP definition and article/Figure 3 labels and categories were found on all cited pages.

**Quality-control relevance:** Numeric subgroup definitions labelled prespecified should match the supplied prespecification or identify a documented redefinition.

**Potential downstream evidence impact:** If confirmed, an evidence reviewer could classify the displayed age-subgroup estimates or their prespecification status differently; no estimate is declared invalid and no conclusion change is established.

**Human verification steps:** Retrieve dated final/amended analysis-plan records and establish what age definition the article's prespecified label references.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — The named optimal in-hospital medication composite uses different component labels across final-result tables

**Candidate statement:** The same named optimal in-hospital medication composite is defined with `anticoagulant` in the article/eTable 5 and `heparin` in eTable 6.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [Main article — PDF p. 3](<../jama_huffman_2018_oi_170166.pdf#page=3>), Outcomes; [main article — PDF p. 7](<../jama_huffman_2018_oi_170166.pdf#page=7>), Table 3 footnote c; [online supplement — PDF p. 21](<../joi170166supp3_prod.pdf#page=21>), eTable 5 footnote c; [online supplement — PDF p. 22](<../joi170166supp3_prod.pdf#page=22>), eTable 6 footnote b.

**Source evidence:** Article/Table 3/eTable 5 list aspirin, an ADP-receptor antagonist, anticoagulant, and beta-blocker. eTable 6 uses the same composite name but lists heparin as the fourth component.

**Reported-versus-comparator:** Three components match; the fourth is `anticoagulant` versus `heparin`.

**Reasoning procedure:** The repeated composite name and component wording are direct observations. Whether heparin exhausts the operational anticoagulant category is unknown from supplied sources.

**Calculation:** Set comparison: aspirin, ADP-receptor antagonist, and beta-blocker are shared; the fourth printed label differs.

**Alternative source-grounded interpretations:** If heparin was the only qualifying anticoagulant in analyzed records, the labels may be extensionally equivalent. Medication coding, eligibility rules, and table-generation code are absent.

**Mechanical evidence recheck:** Every cited definition was found at its source location; the component-label difference is directly reproducible.

**Quality-control relevance:** A repeated named composite should retain its component definition or explicitly identify a different construct.

**Potential downstream evidence impact:** If confirmed, an extractor could encode the composite as broad anticoagulant use or heparin-only use; no difference in effect estimates, propagation, or conclusion change is established.

**Human verification steps:** Review medication coding, qualifying-anticoagulant rules, and the eTable 6 interaction-analysis definition to determine the implemented composite.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Hospital-type subgroup is reported as prespecified but is absent from the supplied SAP subgroup list

**Candidate statement:** The article calls the hospital-type Figure 3 subgroup prespecified, while the supplied SAP's a priori site-level subgroup list does not name hospital type.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [Main article — PDF p. 3](<../jama_huffman_2018_oi_170166.pdf#page=3>), Statistical Analysis; [main article — PDF p. 9](<../jama_huffman_2018_oi_170166.pdf#page=9>), Figure 3 and adjacent Results narrative; [SAP — PDF p. 7](<../joi170166supp2_prod.pdf#page=7>), section 7.5.2.

**Source evidence:** The article labels hospital type prespecified and Figure 3 prints government (9 hospitals), nonprofit (12), and private (42). The SAP lists hospital size and use of quality-improvement toolkit components as site-level a priori subgroups, not hospital type.

**Reported-versus-comparator:** Article/Figure 3 includes hospital type; the supplied SAP list includes toolkit-component use and does not name hospital type.

**Reasoning procedure:** The article label, three categories/counts, and SAP list are direct observations. A later amendment or separate plan is a possible but unsupplied explanation. The sources establish differing lists, not an intentional substitution.

**Calculation:** 9 + 12 + 42 = 63 hospitals. This confirms an implemented full hospital partition, not prespecification.

**Alternative source-grounded interpretations:** A separate or amended plan could have added hospital type and changed/omitted toolkit-component use before analysis. No such record is included.

**Mechanical evidence recheck:** The article/Figure 3 wording and categories and SAP site-level list were found at the exact cited pages.

**Quality-control relevance:** A final quantitative subgroup labelled prespecified should appear in the supplied prespecification or have a supplied documented basis.

**Potential downstream evidence impact:** If confirmed, an evidence reviewer could classify the hospital-type estimates or their prespecification status differently; no invalid estimate, propagation, or paper-level conclusion change is established.

**Human verification steps:** Retrieve dated amendment/separate prespecification records and determine whether hospital type was prespecified and why the SAP-listed toolkit-component-use subgroup is not displayed in Figure 3.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

Small preventable reporting defects can matter when systematic reviews, meta-analyses, guidelines, or structured data products copy an estimate, interval, subgroup definition, comparator direction, or composite definition. This package provides no evidence that any candidate propagated, changed a conclusion, or caused harm.

## Limitations and Missing Definitions

- No raw participant data, final model objects, production tables, covariance matrices, or response-level analysis outputs are supplied.
- The package lacks the variance, degrees-of-freedom, sidedness, multiplicity, and estimand inputs needed for unsupported inferential reconstruction.
- eTable 1 does not source-define its complete/missing-follow-up contrast order or CI procedure sufficiently to resolve the footnote.
- No final/amended prespecification record resolves the age-band or hospital-type list differences.
- The supplied documents do not establish whether heparin exhausts the broader anticoagulant component definition.
- For DOC-004 pp. 3-16, supplied source-matched OCR was fallback only; no new OCR was run, and direct PDFs remain authoritative.
- eFigures on DOC-004 pp. 24-27 lack exact point labels, so no unsupported plotted-value reconstruction was performed.

## Human Adjudication Checklist

For each candidate, retain the supplied PDFs and cited page locations; obtain the specific missing record named in the card; document the comparison of source output to printed locations; and complete the five `__` fields in that card. Do not infer a correction from this report alone.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Source integrity and reproducibility

| Direct source | Pages | SHA-256 |
|---|---:|---|
| `jama_huffman_2018_oi_170166.pdf` | 12 | `11311a6bb5c7a4be734ed60776b308f525ad101671ccc8d34bab18735aaca5f5` |
| `joi170166supp1_prod.pdf` | 32 | `0e13bdfc6e5e3c8b86e187f54f0a3d7d0217fc0614be9fbdbbb7839dbab9004a` |
| `joi170166supp2_prod.pdf` | 9 | `d49019c3cf6ee0766fb319f254f27f87751a73bfec66c34d38bae16a956bb1c6` |
| `joi170166supp3_prod.pdf` | 27 | `511f4a907e4c48d920f1c6b89d444fe76c7c91e11bbae84cdee834fa0393f3ec` |

### Agent execution

| Stage | Agent ID | Model | Reasoning effort |
|---|---|---|---|
| Coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high |
| Fresh source preprocessing | /root/fresh_source_preprocessor | gpt-5.6-terra | medium |
| Main quantitative mapping | /root/main_quantitative_mapper | gpt-5.6-terra | medium |
| Support quantitative mapping | /root/support_quantitative_mapper | gpt-5.6-terra | medium |
| Numeric consistency | /root/numeric_consistency_reviewer | gpt-5.6-terra | medium |
| Cross-source consistency | /root/cross_source_consistency_reviewer | gpt-5.6-terra | medium |
| Statistical pass 1 | /root/statistical_pass_1 | gpt-5.6-terra | high |
| Evidence recheck | /root/evidence_rechecker | gpt-5.6-sol | high |
| Statistical pass 2 | /root/statistical_pass_2 | gpt-5.6-terra | high |
| Evidence-quality audit | /root/quality_control_auditor | gpt-5.6-sol | high |
| Report generation | /root/report_generator | gpt-5.6-terra | medium |

### Performance

- **Target basis:** Four supplied PDFs totaling 80 pages, including a 12-page main article and three support documents; all 80 units require source-matched fresh mapping, with native/layout extraction expected to cover most pages and a supplied legacy OCR asset available only as a page-matched fallback for the image-heavy 27-page supplement. The relationship volume and two mandatory statistical passes make this moderately complex but smaller than the 102-page calibration package.
- **Total source units:** 80
- **Fresh-source units:** 80
- **Target elapsed minutes:** 30-45
- **Started UTC:** 2026-08-24T01:56:09Z
- **Finished UTC:** 2026-08-24T02:32:58Z
- **Observed elapsed minutes:** 36.8
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token accounting and cost

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Input tokens | Output tokens | Total tokens | Token-only API-equivalent estimate (USD) |
|---|---:|---:|---:|---:|
| gpt-5.6-sol | 0 | 0 | 0 | 0.000000 |
| gpt-5.6-terra | 0 | 0 | 0 | 0.000000 |

The runtime exposed no authoritative response-level token counts for any of the 11 manifested agents, including the coordinator. The ledger therefore uses explicit `UNAVAILABLE` records and does not estimate usage from text length. The displayed zeros are known recorded subtotals only; the complete package token count and cost remain unavailable. Amounts are token-only API-equivalent estimates under the pricing snapshot dated 2026-08-18, not invoices; cached-input/cache-write and reasoning counts are subsets and are not added again to total tokens. Per-agent detail is in `review_1_5_2/token_usage_summary.md`.
