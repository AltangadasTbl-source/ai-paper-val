# Numeric Consistency Review

Status: COMPLETE. Scope: all 49 supplied PDF pages (main 11, protocol 25, support 13), all 182 canonical numeric/reporting relationships, every displayed table count/denominator/percentage and binary difference, participant flow, risk tables, rescue counts and effect-measure labels. The complete fresh main/support evidence maps were read. Counts were treated as exact patient counts; displayed integer percentages allow half-unit intervals. Every displayed numeric relationship is recorded in relationships/numeric_relationship_inventory.md, with two disjoint parts of 120 and 62 relationships. No old scientific findings or reports, external evidence, or raw-data assumptions were used.

Methods: direct Poppler pdftotext 25.03.0 layout reads of main pages 4–9 and source-linked reused page 5 image confirmed Table 1 positioning and footnote values. CPU; no saved derivative, new OCR or rendering. The complete support map includes source-linked image restorations for eTable/eFigure. All remaining counts were reviewed from complete source-matched mapping/transcriptions. Totals, disjoint partitions, endpoint-specific waveform availability and explicitly disclosed device substitution were distinguished. Binary contrast columns reproduce B minus T proportions within display precision. Hodges–Lehmann continuous contrasts are distinct from subtraction of group medians; Cox HRs are distinct from crude risks. Inferential interval/test and planned statistical design questions are independently assigned to the statistical and cross-source stages.

## Findings

### F-NUM-001

**Title:** Mixed denominator bases in four medical-indication percentage cells of Table 1.

**Numeric relationships:** N039, N040; context N034–N038, N041–N043.

**Compared locations and document roles:** REPORT [main article PDF p.5, Table 1 headers and Indication for intubation → Medical subrows](../../../jama_driver_2018_oi_180054.pdf#page=5), both columns. Bougie header n=381; tube + stylet header n=376. Affected rows: “Asthma, COPD, heart failure, pneumonia,” 16 (5) and 23 (7); medical “Other,” 44 (14) and 41 (13). Same table gives parent medical counts 318 and 315. Neighboring medical subrows use arm-wide percentages, e.g. altered mental status 185 (49),173 (46).

**Printed inputs, rule and calculation:** With the arm denominators specified in the column headers, each patient count has a singleton input interval. Integer printed percentage p has interval [p−0.5,p+0.5]. The gap is the distance between the recomputed singleton and that interval, divided by absolute p.

| Cell | Exact count/base | Recomputed percentage interval | Printed percentage interval | Gap, percentage points | Relative discrepancy |
|---|---|---|---|---|---|
| Bougie respiratory/cardiac grouped indication | 16/381 | [4.19948,4.19948] | [4.5,5.5] | 0.30052 | 0.06010 |
| Tube respiratory/cardiac grouped indication | 23/376 | [6.11702,6.11702] | [6.5,7.5] | 0.38298 | 0.05471 |
| Bougie medical Other | 44/381 | [11.54856,11.54856] | [13.5,14.5] | 1.95144 | 0.13939 |
| Tube medical Other | 41/376 | [10.90426,10.90426] | [12.5,13.5] | 1.59574 | 0.12275 |

All four remaining relative gaps exceed 0.05. The counts themselves sum correctly to the parent medical totals: bougie185+32+21+20+16+44=318; tube173+23+27+28+23+41=315. Using these parent totals instead reproduces the four affected percentages:16/318=5.031%,23/315=7.302%,44/318=13.836%,41/315=13.016%. That alternative is not a uniform reading of the subrows:185/318=58.176% and173/315=54.921%, unlike printed49%/46%. Thus one denominator change appears in a repeated pattern, consolidated into one finding.

**Focus area:** A (counts and denominators).

**Proposed review domain:** statistical_results. **Proposed relationship type:** S_W; all relationships S_W.

**Qualifying route:** Route A, category 3.

**Affected result or extracted value:** Four baseline medical-indication percentages, and whether they describe all randomized participants or only those with a medical indication.

**Why context does not resolve it:** This is a reproduced count/denominator/percentage mismatch within one display, an always-register category. Indentation suggests medical membership but cannot explain why only two of six equally nested medical rows use the parent denominator. The apparent intended calculation does not remove a printed percentage from extraction scope.

**Alternatives and missing definition:** The four percentages may intentionally be conditional on medical indication, whereas preceding subrows are marginal arm percentages. No row-level definition or footnote states such a switch. Another possible explanation is a different denominator not supplied. Those are interpretations, not observed production facts.

**Exact human question:** What denominator applies to each medical-indication subrow of Table 1, particularly the four affected percentage cells, and are these percentages intended to use one common base?

### F-NUM-002

**Title:** Table 1 initial oxygen-saturation denominators and missingness footnote do not reconcile.

**Numeric relationships:** N032,N033,N056; context N001,N054,N055.

**Compared locations and document roles:** REPORT [main article PDF p.5, Table 1 oxygen saturation <90% and <80% rows, column headers and footnote b](../../../jama_driver_2018_oi_180054.pdf#page=5). Headers give381 bougie and376 tube participants. Both threshold rows explicitly give denominators352 and344. Footnote b gives43 patients without initial oxygen saturation,19 bougie and24 tube, respectively. The same footnote defines initial vital signs as after enrollment and before intubation and cites waveform unreliability/nonconnection as reasons for unavailable measurements.

**Printed inputs, rule and calculation:** Exact integer patient-count inputs have singleton intervals. If the threshold denominators are the participants with initial saturation available, the missing counts implied by the table are381−352=29 bougie and376−344=32 tube, total61. The footnote instead gives19+24=43. Recomputed total missingness interval[61,61], printed total interval[43,43], gap18 patients, relative discrepancy18/43=0.41860. Groupwise gaps10/19=0.52632 and8/24=0.33333 also exceed0.05. Although differences expressed relative to the large observed-data denominators are small, the compared quantities here are the expressly printed numbers of participants missing the same initial measurement. Saturation event percentages themselves reproduce their printed denominators and are not independently discrepant.

**Focus area:** A (counts and denominators).

**Proposed review domain:** statistical_results. **Proposed relationship type:** S_W; all relationships S_W.

**Qualifying route:** Route A, category 3.

**Affected result or extracted value:** The number of participants contributing initial oxygen-saturation data, and the corresponding initial saturation missing counts19/24 or29/32 (total43 or61).

**Why context does not resolve it:** Count and data-denominator descriptions for the same baseline measurement coexist in one table. The table does not distinguish a separate eligibility criterion for threshold calculations from availability of initial saturation. This is an always-register count discrepancy within one display.

**Alternatives and missing definition:** The saturation median/IQR may have more observed measurements than the threshold rows, or additional threshold-specific exclusions may exist; neither distinction is supplied. The threshold denominators equal group sizes minus the footnote's missing heart-rate counts29/32, which corroborates a possible count-label alignment issue but does not establish its origin or a final correction.

**Exact human question:** Do352/344 describe all participants with initial oxygen saturation available, and, if so, how do they reconcile with footnote b's43 missing initial saturation values (19/24); alternatively, what additional criterion distinguishes the threshold-row population?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| Main PDF p.6 Table2 Operator, footnote f; N063,N103–N105 | Bougie final-operator counts318+57+8=383 versus header381. Exact remaining relative discrepancy2/381=.00525 is at most0.05; tube sum376 reconciles. | ROUNDING_OR_DISPLAY_PRECISION |
| Main PDF p.6 Table2 video-screen rows; N109–N111 | Numerators218+78+75=371 against377 and182+90+98=370 against372. Relative gaps6/377=.01592 and2/372=.00538 are at most0.05; prospective form also supplies an N/A option. | ROUNDING_OR_DISPLAY_PRECISION |
| Main PDF p.5 Table1 heart-rate bougie SD; N029 | Parenthesis after108 (25 is absent; the number25 and its SD interpretation remain clear. | NOTATION_OR_TYPOGRAPHY |
| Main PDF p.7 Table3 all-patient duration; N124 | Group medians38 and36 differ by2 whereas printed Hodges–Lehmann contrast is1; these are distinct quantities under the stated estimator. The separately printed reversed CI endpoints4 to−1 are preserved for statistical review and are not excluded here. | MODEL_VERSUS_CRUDE |

## Scope closure

182/182 N relationships COMPLETE; all49 supplied pages covered;2 findings and4 excluded apparent observations. Checks that reconcile are recorded in the relationship inventory rather than the exclusion table. No scientific coverage limitation. Supplied data lack patient-level records and separate randomized-arm impingement counts; those absence-only details were not converted into findings. Every inferential row remains available to both statistical passes; this lane does not adjudicate registered candidates.
