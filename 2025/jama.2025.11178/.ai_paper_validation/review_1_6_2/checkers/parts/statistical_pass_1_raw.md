# Statistical pass 1 — raw-score REPORT shard

Agent runtime task: /root/statistics_pass_1_raw. Fixed model: gpt-6.1-sol; reasoning effort: high; FRESH_SPAWN. Exact assigned scope: DOC-005 eTable11 physical pp17–18, all21 outcome/time rows, all63 raw group summaries, all63 mean-difference/95%CI pairs, all21 omnibus P values and source headers/footnote. DOC-001 p11 Table3 h/i was inspected solely to establish the global-impression measurement definition. Complete relationship records: statistics/parts/relationship_inventory_raw.md, S401–S422, every relationship PASS_1_COMPLETE; pass2 pending. Finding count1; excluded-observation count3.

The complete QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read. The current routing preflight is PASS and tooling record establishes direct Poppler tools with CPU processing. Sources and reusable evidence were preserved; no old scientific selection record or web source was used. New direct layout text and CPU page renders at preprocessing/stat1_raw/ were visually inspected. The source images confirm the source's explicit distinction between median/quartile group columns and GEE mean-difference/CI columns.

## Checked results

Every one of the63 contrast estimates lies within its ordered interval. Every group median lies within its ordered printed quartiles. All21 linear-contrast transitivity comparisons reconcile after half-unit rounding (interval gap0). Every significant omnibus P is accompanied by at least one null-excluding contrast CI; physical3mo P=.212 and all three contrast intervals include0. An omnibus P and an individual contrast CI have different hypotheses, so they were not mechanically equated. Unreported test statistics, covariance, sidedness and degrees of freedom were not inferred. Rounded−0.0/0.0 interval endpoints do not establish an unprinted individual-contrast P value. There are no noninferiority/equivalence margins or interim/stopping conclusions in this table. Individual contrasts were not obtained by subtracting medians. No exact Wald-P diagnostic is presented as reproduction of a reported analysis.

### F-ST1-401

**Title:** Global-impression raw-score summaries do not consistently match the printed median quantity.

**Relationships:** S417, S418, S419, S420, S422. **Compared locations and document roles:** REPORT DOC-005 [eTable11, physical p17](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=17), title and “Raw Score Median (25%-tile, 75%tile)” header versus five cells listed below; REPORT DOC-001 [Table3 footnotes h/i, physical p11](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11), which defines both global-impression outcomes as one item with response categories1–7. REPORT DOC-005 [physical p18 footnote b](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=18) describes linear-GEE mean differences and CIs but does not redefine the group-summary columns.

**Printed values/statements:** The median header applies to every group summary, including Global Impression–Pain PT6mo2.8(2.7,2.9), PT12mo2.8(2.7,2.9), UC12mo2.2(2.1,2.3); Global Impression–General PT3mo2.7(2.6,2.7), UC6mo1.8(1.7,1.9). The main footnotes state one item, range1–7, with seven integer response categories from “much better” through “much worse.” Other cells include3mo HC2.0(1.0,3.0) for pain and2.0(1.0,2.0) for general, which are compatible with genuine medians/quartiles and prevent simply assuming a uniform mean/CI summary without clarification.

**Rule and calculation:** For raw single-item integer responses, an ordinary sample median is an integer (odd sample size) or the average of two integers (even size), hence belongs to {1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7}. The printed one-decimal median is allowed its ±0.05 interval. The permissible median values are exact values implied by the categorical source definition, rather than rounded input estimates. The nearest permissible value is used, making the test conservative.

| Exact eTable11 cell, REPORT p17 | Printed median | Allowed printed interval | Closest permissible median / exact interval | Remaining gap | Relative discrepancy |
|---|---:|---|---|---:|---:|
| Global pain6mo, PT column | 2.8 | [2.75,2.85] | 3.0 / [3.0,3.0] | 0.15 | 0.15/2.8=0.05357 |
| Global pain12mo, PT column | 2.8 | [2.75,2.85] | 3.0 / [3.0,3.0] | 0.15 | 0.05357 |
| Global pain12mo, UC column | 2.2 | [2.15,2.25] | 2.0 / [2.0,2.0] | 0.15 | 0.15/2.2=0.06818 |
| Global general3mo, PT column | 2.7 | [2.65,2.75] | 2.5 / [2.5,2.5] | 0.15 | 0.15/2.7=0.05556 |
| Global general6mo, UC column | 1.8 | [1.75,1.85] | 2.0 / [2.0,2.0] | 0.15 | 0.15/1.8=0.08333 |

The five remaining gaps exceed0.05 relative discrepancy. This is a reproduced incompatibility of numeric group-summary values with their declared quantity, consolidated as one summary-definition pattern. No conclusion is drawn about the actual unprinted medians or about a mean-minus-median equality.

**Focus area:** C (effect/summary-measure identity and analysis-to-number mapping), with B numeric interpretation. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_C (all relationships S_C): the scale definition and reported median quantity occur in different REPORT documents. If the rechecker treats the main definition solely as corroboration of the meaning of the scale, S_W is a source-grounded alternative classification for the internal eTable11 header/cell conflict.

**Qualifying route:** Route B. B1: the conflict concerns a reported statistical summary quantity. B2: the source does not explain whether fractional single-item values are raw medians, fitted/averaged scores, or a mixture of summaries. B3: the distinction affects extracting a median/IQR versus a mean/CI and using the printed global-impression group values in evidence synthesis.

**Affected result or extracted value:** The five named global-impression group summaries, their summary statistic, and whether the parentheses denote quartiles as printed. This finding does not itself establish a change in any omnibus or pairwise inferential conclusion.

**Why context does not resolve it:** Some3mo HC cells have integer medians with broad quartiles, while other cells have fractional centers incompatible with ordinary raw medians beyond the scope's display tolerance. The GEE footnote explicitly describes the between-group means and their CIs; it does not label the raw group cells as means or explain a mixed summary. A reader cannot choose the intended extraction quantity from the stated table definition alone.

**Source-grounded alternatives and missing definition:** The linear-GEE analysis makes fitted means a possible interpretation of some fractional centers, but the source labels those group cells medians and the footnote only defines between-group estimates. The table could use different group summaries in different cells, or a transformed/interpolated/nonordinary median of another quantity, but such a procedure is not supplied. The required definition is the exact statistic producing each raw-score group center and its two accompanying limits, and whether any noninteger preprocessed responses entered this single-item summary. No replacement values or preferred method are proposed.

**Exact human question:** What summary statistic and accompanying limits were used for the five named global-impression group cells in eTable11, and how do those definitions reconcile the fractional printed values with the stated raw-score median of a single1–7 response item?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| DOC-005 REPORT eTable11 p17, all21 rows and p18 method | The displayed group-median differences often have a different direction/magnitude from GEE mean contrasts, suggesting a possible group-column pattern. Raw medians need not equal fitted means; no source establishes their equality, so a column permutation cannot be reproduced from subtracting these medians. | CONDITIONAL_OR_UNREPORTED |
| DOC-005 REPORT eTable11 pp17–18 | Exact omnibus-P and CI-width reproduction would require covariance/variance/test implementation not supplied for this table. Missing inputs alone provide no conflicting printed numerical statement. | CONDITIONAL_OR_UNREPORTED |
| DOC-005 REPORT eTable11 p17, remaining fractional global-impression medians2.9,2.1,1.9,1.6,2.6 | Distances to the nearest permissible ordinary median after ±0.05 display allowance are at most0.05 relative discrepancy; these individual cells do not independently reproduce the numeric threshold used for F-ST1-401. Integer2.0 and half-integer2.5 centers reconcile and are not excluded observations. | ROUNDING_OR_DISPLAY_PRECISION |

## Limitations

All assigned source cells and footnotes were inspected. The source does not supply individual records, group arithmetic means for this table, a fitted covariance matrix, per-row analysis counts or test statistics; no convention was substituted for these missing inputs. The finding concerns the printed summary quantity and named numeric cells, not a raw-data audit. Independent inclusion screening and exact-source mechanical recheck remain the coordinator's next stages.
