# Numeric consistency checker — main shard A

Scope: main-paper M001–M100 = N001–N100, all100 groups checked;100 explicit group outcomes in relationships/parts/numeric_main.md. Four distinct local candidate records follow. Stable C IDs, severity, validity and disposition are not assigned by this checker. All remain questions for human adjudication. Source role is REPORT for every compared location, established by the article's retrospective trial-result content. No PLAN location is part of these discrepancy comparisons.

Methods and evidence: complete main-map scope plus selective support context; fresh direct Poppler25.03.0 extraction from physicalPDFpp.5–7 and9; visual inspection of source-matched unchanged page rendersDOC-001-05/06/07 (legacy engineUNKNOWN). Locator derivatives assist transcription; direct supplied PDF establishes printed values. No old candidate sets, reports, web, Python helpers or scientific-input judgments used. Rounded whole percentages/differences allow ±0.5 percentage point (calculation precision0.001); integers allow zero count discrepancy. Group differences use unrounded proportions. Interval endpoint ordering is exact at printed precision. No statistical significance claim is derived from arithmetic alone.

## NUM-A01 — Respiratory medical-indication row uses a different percentage denominator

- Relationships: N044, corroborating N039/N040/N041/N042/N043.
- Primary category proposed: Denominator, proportion, or total inconsistency.
- Compared location1 and role: REPORT [main PDF p.5 Table1 column headers](../../../../jama_driver_2018_oi_180054.pdf#page=5), Bougie Group No.(%)(n=381), Endotracheal Tube+Stylet Group No.(%)(n=376).
- Compared location2 and role: REPORT [main PDF p.5 Table1 Asthma,COPD,heart failure,pneumonia row](../../../../jama_driver_2018_oi_180054.pdf#page=5),16(5) and23(7).
- Compared location3 and role: REPORT [main PDF p.5 Table1 Medical parent and sibling indication rows](../../../../jama_driver_2018_oi_180054.pdf#page=5),Medical318(83)/315(84);altered mental status185(49)/173(46);cardiac arrest32(8)/23(6);septic shock21(6)/27(7);seizure20(5)/28(7).
- Direct observation: the respiratory row displays5%/7%; headers give381/376; no fraction or footnote changes this row's percentage denominator. Sibling medical subrows predominantly match randomized header denominators.
- Rule and calculation:100×16/381=4.199%, nearest integer4%, not5%;100×23/376=6.117%, nearest integer6%, not7%. Deviations from printed values0.801/0.883 percentage points exceed ±0.5. By contrast100×16/318=5.031%→5 and100×23/315=7.302%→7. Sibling185/381=48.556%→49,173/376=46.011%→46 do not use medical denominators.
- Tolerance: exact numerator and header denominator, nearest-whole percentage ±0.5 percentage point;0.001 calculation tolerance.
- Inference: displayed respiratory percentages appear computed within medical-indication subsets; production mechanism is not established. This is an observable denominator/label mismatch under the printed header rule.
- Alternatives: a row-specific medical denominator may be intended; then its denominator must be explicitly distinguished from sibling rows. Numerators or percentages may instead contain transcription errors. Raw participant records are unavailable and are not inferred.
- Quality-control relevance: inconsistent denominator labels can be copied as arm-level baseline proportions in evidence extraction. No conclusion-impact assertion is made.
- Exact human question: Were16(5%) and23(7%) intended to describe proportions of all381/376 randomized patients or of318/315 medical-indication patients, and which printed row values or denominator label should be reconciled?

## NUM-A02 — Other medical-indication row changes its percentage denominator

- Relationships: N045, corroborating N039/N040 and traumaN046–N048. Distinct comparator and printed values fromNUM-A01; do not merge merely because both may share a denominator practice.
- Primary category proposed: Denominator, proportion, or total inconsistency.
- Compared location1 and role: REPORT [main PDF p.5 Table1 column headers](../../../../jama_driver_2018_oi_180054.pdf#page=5), n=381/n=376, No.(%).
- Compared location2 and role: REPORT [main PDF p.5 Table1 Medical—Other row](../../../../jama_driver_2018_oi_180054.pdf#page=5),44(14)/41(13).
- Compared location3 and role: REPORT [main PDF p.5 Table1 Medical parent and sibling rows](../../../../jama_driver_2018_oi_180054.pdf#page=5),318(83)/315(84),185(49)/173(46);Trauma—Other34(9)/38(10).
- Direct observation: row prints14%/13%; no explicit alternate denominator applies. All medical count subrows sum185+32+21+20+16+44=318 and173+23+27+28+23+41=315. Thus counts themselves reconcile; percentage labels are the issue.
- Rule and calculation:100×44/381=11.549%→12%, not14%;100×41/376=10.904%→11%, not13%. Printed-minus-derived2.451/2.096 percentage points exceed ±0.5. Medical denominators yield44/318=13.836%→14,41/315=13.016%→13. Sibling altered-mental and trauma-other percentages use randomized arm sizes. The medical subrow displayed percentages sum87%/86% versus parent83%/84%, consistent with mixed bases rather than a single rounding rule.
- Tolerance: zero count tolerance, nearest-whole percentage ±0.5 percentage point;0.001 arithmetic tolerance. Percentage-sum diagnostic is corroboration, not a separate candidate.
- Inference: medical-subset percentage denominators appear used for this row, despite common header/sibling convention; exact editorial origin unknown.
- Alternatives: intended row-specific denominator318/315; numerator transcription; percentage transcription. A deliberate subset-based display could be coherent if labelled.
- Quality-control relevance: arm-level baseline proportions versus within-indication proportions convey different quantities and may be extracted incorrectly downstream.
- Exact human question: Does Other under Medical mean44/381 and41/376 or44/318 and41/315, and how should the row and common header state that intended denominator consistently?

## NUM-A03 — Final-operator category counts exceed the bougie arm total

- Relationships: N076/N077/N078, with final-operator definitionN029.
- Primary category proposed: Denominator, proportion, or total inconsistency.
- Compared location1 and role: REPORT [main PDF p.6 Table2 column header and Operator rows](../../../../jama_driver_2018_oi_180054.pdf#page=6), bougie n=381;senior resident/fellowPGY≥3=318(83),junior residentPGY≤2=57(15),faculty=8(2). Comparator n=376 and334(89),37(10),5(1).
- Compared location2 and role: REPORT [main PDF p.6 Table2 footnotef](../../../../jama_driver_2018_oi_180054.pdf#page=6),“This lists the final intubating physician”;physician change8 times total,4/group.
- Direct observation: three final-operator count categories sum318+57+8=383 in an arm labelled381 patients; comparator334+37+5=376 reconciles.
- Rule and calculation: one final physician per patient classified as senior/fellow,junior,or faculty implies sum≤381 (and equals381 if all classified). Printed sum383 exceeds381 by2; combined operators759 exceeds trial757 by2. This is not caused by rounding of the83%/15%/2% values because the discrepant inputs are integers. Individual percentages and differences are coherent under381/376.
- Tolerance: exact integer totals, zero tolerance. Percent totals100% alone do not repair excess integer counts.
- Inference: at least two counted operator assignments overlap or some row/header input requires reconciliation under the stated final-physician definition. Exact cause unavailable.
- Alternatives: more than one operator was counted for some patients despite final-operator footnote; categories overlap under an unstated classification; one count is transcribed incorrectly. Four physician changes per group do not by themselves justify more than one final physician per patient.
- Quality-control relevance: operator-training distributions and denominators can be mis-extracted as patient-level covariates or subgroup descriptors. No effect estimate alteration is asserted.
- Exact human question: How do318 senior/fellow,57 junior,and8 faculty final-operator records reconcile to381 bougie-assigned patients, and does the final-physician footnote accurately define the counted unit?

## NUM-A04 — All-patient duration confidence interval endpoints appear in descending order

- Relationships: N097, source estimator definitionN010. SupplementU046 only corroborates ascending order and is not the discrepancy comparator for this local candidate.
- Primary category proposed: Statistical reporting inconsistency.
- Compared location1 and role: REPORT [main PDF p.7 Table3 All patients—First-attempt duration row](../../../../jama_driver_2018_oi_180054.pdf#page=7), bougie38(29 to51)s,tube36(25 to54)s,Difference(95%CI)1(4 to−1),P=.24,interactionNA.
- Compared location2 and role: REPORT [main PDF p.7 Table3 Difference(95%CI) header](../../../../jama_driver_2018_oi_180054.pdf#page=7), identifying 4 and −1 as interval endpoints; [p.4 Statistical Analysis](../../../../jama_driver_2018_oi_180054.pdf#page=4) defines the Hodges–Lehmann continuous between-group difference.
- Direct observation: source visually and direct PDF text prints1(4 to−1), exactly as mapped; this is not an OCR reordering. Other95%CI entries use ascending endpoints.
- Rule and calculation: a reported lower-to-upper confidence interval requireslower≤upper;4>−1, a5-second reversal. Under printed endpoint order,lower4 exceeds point estimate1 andupper−1 lies below it. Swapping endpoints would produce−1≤1≤4, but that diagnostic is not a prescribed correction.
- Tolerance: integer-second printed endpoints; order reversal5s exceeds any ±0.5s endpoint-rounding tolerance. Interpreting an unordered set{4,−1} could recover a range, but the publication's interval convention presents ordered endpoints.
- Inference: endpoint ordering appears inverted. The point estimate1s need not equal38−36=2s because Hodges–Lehmann estimates differ from subtracting displayed medians; that difference is not a candidate.
- Alternatives: descending notation intended despite common interval convention; endpoint transposition; other endpoint transcription. Raw timing data and model output are not supplied to select a correction.
- Quality-control relevance: an interval parsed as printed may fail structured extraction or be entered with reversed bounds in downstream evidence records.
- Exact human question: What are the intended lower and upper95% confidence limits for the all-patient1-second Hodges–Lehmann duration difference, and should the printed4 to−1 endpoint order be reconciled?

## Complete-scope limitations and no-candidate checks

The inventory explicitly coversN001–N100 without candidate-count stopping. No assigned relationship contains a display-zero P value requiring exclusion. Device-first, actual-device, randomized-group, difficult-feature and all-patient populations remain distinct. M020's31/444=7% pooled resistance retold as7% in the bougie group is an alignment ambiguity: an arm-specific numerator is not supplied, so31/381 is an unsupported reassignment; no distinct numeric candidate is emitted. M096's composite denominator366 and Table5hypoxemia denominator364 can differ if failed-attempt patients have a determinable composite outcome without a measured oxygen outcome; equal-denominator identity is not established. Position/video row subtotals are smaller than totals but exhaustiveness is not asserted. No raw event times, Office sheets, CSV records, or person-time denominators are supplied. These are reconstruction limits; all assigned units and relationships are checked.

