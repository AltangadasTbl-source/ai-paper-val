# Numeric consistency checker: non-plan results supplement

Exact scope: DOC-002 joi190092supp1_prod.pdf PDF pp1-16, numeric relationships N100-N243 (NR001-NR144), and DOC-005 joi190092supp4_prod.pdf p1 administrative page. Two complete inventory parts contain95 and49 relationships. Main article and PLAN checks are assigned to other agents. No old candidates, review decisions or reports were read. No web used. All locations below are REPORT by content. No stable C IDs, judgments or dispositions assigned.

Method: source-linked reusable Poppler layout text plus current direct `pdftotext -layout` streams for pp3-12 and14-16; current Poppler26.01.0 renders of p10,p14,p15 visually inspected. Render command: `pdftoppm -f N -l N -scale-to 1600 -singlefile -png joi190092supp1_prod.pdf .ai_paper_validation/review_1_6/preprocessing/numeric_results_pN`. The three derivatives are numeric_results_p10.png, numeric_results_p14.png and numeric_results_p15.png under preprocessing. No OCR or Python extraction needed. Sources and reused assets unchanged.

## Complete checks

Every count/percentage cell in eTables2,4-6,8-9 was recalculated with its printed column N. Patient percentages are distinguished from event counts and person-time rates. The nine enrollment counts sum216; their whole-percent shares sum100 and individually reconcile within0.5 percentage points. All adverse-event counts lie within their column N. Any-event unions are at least the largest component count and at most the component sum; overlapping row counts are not added as mutually exclusive subgroups. Six-month exposure population107+108=215 plus one untreated randomized MMF participant is internally coherent. Continuing N62/56 and switching N29/20 are different populations/time windows; no baseline denominator substitution. Except the two cells below, all one-decimal shares reconcile within0.05 percentage points. Every eligibility, threshold/duration, serious-category, dose, unit and scale group was checked. Unreported CBC/creatinine units and thresholds at which no observed value is supplied do not alone establish numeric inconsistencies. Methotrexate BID on Day1 corresponds20mg or15mg per week; MMF BID on all7 days corresponds2g/day or1g/day. These are coherent reduced-dose patterns. Repeated values in distinct overlapping event rows do not establish copying. DOC-005 availability date is administrative and supplies no applicable outcome relationship.

Six distinct source-grounded observations follow; there is no finding-count target. The label comparisons are conditional on the printed eTable1 definitions being the applicable definitions for the reported eTables8/9. No changed event count is inferred.

## Observation A — Mycophenolate eye-floaters percentage

- Relationships: N152/NR053.
- Compared locations and roles: REPORT [DOC-002 p10 eTable4 eye floaters MMF cell](../../../joi190092supp1_prod.pdf#page=10); REPORT same-page MMF header N=108 and footnote108 exposed participants.
- Printed inputs:5(4.7), N108. Direct render confirms4.7, so this is not an extraction artifact.
- Rule/calculation/tolerance:100×5/108=4.6296296%, nearest one decimal4.6%; 4.7−4.6296296=0.0703704 percentage points exceeds0.05 rounding tolerance. MTX5/107=4.6728972→4.7 is coherent but does not supply the MMF denominator.
- Direct observation: printed numerator, percentage and column denominator do not reconcile under ordinary one-decimal rounding. Inference: a copied percentage or different row denominator is possible, not established.
- Alternatives: an unreported row-specific denominator107 would yield4.7; the table explicitly supplies108, and no row-specific missingness is disclosed. Count, percentage or header could be the input needing clarification.
- Quality-control relevance: an extracted patient proportion may differ from the printed population definition; bounded downstream transcription risk only.
- Exact human question: Is the MMF eye-floaters row calculated from108 exposed patients, or was a different row denominator used; which printed input explains5(4.7)?

## Observation B — Mycophenolate serious-diarrhea percentage after switch

- Relationships: N240/NR141.
- Compared locations and roles: REPORT [DOC-002 p15 eTable9 Serious Systemic, Diarrhea MMF cell](../../../joi190092supp1_prod.pdf#page=15); REPORT same-page MMF header N=20.
- Printed inputs:1(3.4), N20; directly confirmed in current source image.
- Rule/calculation/tolerance:100×1/20=5.0%; printed3.4 differs by1.6 percentage points, exceeding0.05. The neighboring MTX denominator29 would give100/29=3.4482759→3.4, but does not apply to the MMF column.
- Direct observation: numerator/percentage/header mismatch. Inference: use of the other column denominator is a plausible mechanism only.
- Alternatives: row-specific denominator29, a different numerator, or misplaced column label would require clarification; no row-specific population is stated.
- Quality-control relevance: affects extraction of a serious-event patient proportion in the switch population; no conclusion impact inferred.
- Exact human question: What numerator and denominator generated the MMF serious-diarrhea1(3.4) cell under N20?

## Observation C — Ocular hypertension threshold inclusion differs

- Relationships: N118/NR019, N197/NR098, N219/NR120.
- Compared locations and roles: REPORT [DOC-002 p5 eTable1 nonserious ocular hypertension](../../../joi190092supp1_prod.pdf#page=5), versus REPORT [p14 eTable8 nonserious ocular row](../../../joi190092supp1_prod.pdf#page=14) and REPORT [p15 eTable9 nonserious ocular row](../../../joi190092supp1_prod.pdf#page=15).
- Printed inputs: definition≥24mmHg; result rows>24mmHg. p14 reports3(4.8)/1(1.8) under N62/56; p15 reports2(6.9)/3(15.0) under N29/20.
- Rule/calculation/tolerance: threshold labels for the same named event should agree; x=24 satisfies x≥24 but not x>24. Logical comparison has zero numeric tolerance. The associated percentages reconcile; the issue concerns the event definition.
- Direct observation: inclusive and strict threshold symbols differ. Inference: whether any participant at exactly24 was classified differently is unknown.
- Alternatives: the > labels may be shorthand for≥; an explicitly changed criterion may have been applied. No such distinction is disclosed within these report tables. No count correction is asserted.
- Quality-control relevance: prevents incompatible extraction of the event threshold supporting patient counts.
- Exact human question: Did eTables8/9 count ocular hypertension at≥24 or strictly>24mmHg, and how should their labels align with eTable1?

## Observation D — Serious ocular hypertension result label uses pressure criterion

- Relationships: N118/NR019, N199/NR100 (N223/NR124 provides corroboration only).
- Compared locations and roles: REPORT [DOC-002 p5 eTable1 serious ocular hypertension](../../../joi190092supp1_prod.pdf#page=5), versus REPORT [p14 eTable8 Serious Ocular row](../../../joi190092supp1_prod.pdf#page=14).
- Printed inputs: serious definition Surgery required(laser or incisional); p14 serious row Ocular hypertension>24mmHg with MTX1(1.6), MMF0(0.0), N62/56. p15 serious row explicitly says surgery required and corroborates the definition.
- Rule/calculation/tolerance: a counted serious event should retain its defining severity criterion. Pressure>24 is the same description printed in the nonserious row on p14 and does not express surgery required. Percentages1/62×100=1.6129→1.6 and0/56=0 are coherent; exact category-label comparison has no arithmetic tolerance.
- Direct observation: reported serious-row label omits/replaces the supplied surgery criterion and duplicates the pressure description of the nonserious row. Inference: underlying patient may have required surgery; source does not show individual event details.
- Alternatives: abbreviated label under a Serious Ocular heading may imply surgery without restating it; alternatively a different seriousness rule was used. This is a conditional label-consistency question, not evidence that the patient was misclassified.
- Quality-control relevance: reader may treat a pressure-only threshold as the definition of the reported serious count.
- Exact human question: Does the p14 serious ocular-hypertension count represent surgery-required cases, and is>24mmHg an abbreviated or different serious-event criterion?

## Observation E — Serious cataract count versus not-applicable definition

- Relationships: N132/NR033, N224/NR125.
- Compared locations and roles: REPORT [DOC-002 p5 eTable1 Cataract serious column](../../../joi190092supp1_prod.pdf#page=5), versus REPORT [p15 eTable9 Serious Ocular Cataract surgery](../../../joi190092supp1_prod.pdf#page=15); REPORT [p7 generic hospitalization/intervention serious definitions](../../../joi190092supp1_prod.pdf#page=7) supplies a potential alternative.
- Printed inputs: p5 nonserious Visually significant cataract/cataract surgery indicated, serious Not applicable(n/a). p15 serious cataract surgery MTX1(3.4), MMF0(0.0), N29/20.
- Rule/calculation/tolerance: a category marked n/a in the stated event definitions conflicts with a nonzero result explicitly under that serious category unless a separate criterion applies. 100×1/29=3.4482759→3.4 is arithmetically coherent. Category comparison exact, no rounding tolerance.
- Direct observation: a nonzero serious cataract result appears despite serious cataractn/a. Inference: the event may have met a generic hospitalization or intervention criterion; participant detail not provided.
- Alternatives: surgery was separately serious due to hospitalization/preventing permanent impairment, distinguishing actual surgery from merely indicated surgery. The generic p7 rules make this possible, but the table does not explain which applies to this count.
- Quality-control relevance: consistent serious/nonserious labeling matters for safety-count extraction; no clinical judgment is made.
- Exact human question: Which stated serious-event criterion supports the one cataract-surgery patient in eTable9 despite eTable1 marking serious cataractn/a?

## Observation F — Fever upper endpoint differs between definitions and result labels

- Relationships: N130/NR031, N213/NR114, N237/NR138.
- Compared locations and roles: REPORT [DOC-002 p6 eTable1 Fever for12hours](../../../joi190092supp1_prod.pdf#page=6), versus REPORT [p14 eTable8 Non-Serious Systemic fever](../../../joi190092supp1_prod.pdf#page=14) and REPORT [p15 eTable9 same row](../../../joi190092supp1_prod.pdf#page=15).
- Printed inputs: p6 nonserious>100.6 to103°F/39.5°C, serious≥103°F/39.5°C; p14/p15 nonserious Fever<103degrees for12hours. Result counts p14 MTX3(4.8), MMF3(5.4); p15 MTX4(13.8), MMF1(5.0).
- Rule/calculation/tolerance: the upper endpoint described as to103 differs from explicitly<103 if to includes the endpoint; exactly103 also meets the printed serious≥103 criterion. Exact logical endpoint comparison, zero tolerance. All row percentages reconcile. Conversion103°F→39.444°C is compatible with approximate temperature-threshold display; no conversion candidate emitted.
- Direct observation: the printed upper-bound descriptions differ. Inference: inclusive interpretation of to103 creates a boundary overlap; no measured participant temperature at103 is supplied.
- Alternatives: to103 may mean up to but excluding103, making the results labels clarify rather than change the definition. This ambiguity must be preserved; no observed-event reclassification is inferred.
- Quality-control relevance: the quantitative fever endpoint defining reported patient counts is not consistently explicit.
- Exact human question: Does the nonserious fever definition exclude exactly103°F, as eTables8/9 state, and is to103 in eTable1 intended as an exclusive upper endpoint?

## Handoff and limitations

Inventories: relationships/numeric_results_part1.md (95 complete N rows) and relationships/numeric_results_part2.md (49 complete N rows). Checker scope144 relationships, six emitted observations. No extraction or scientific-coverage gap. Conditional label observations identify missing event-specific explanations rather than asserting changed counts. Footnotes referring to nonexistent eFigure2 are locator defects without an independent numeric inconsistency and are not emitted. Statistical interaction P values are delegated to the statistical checker. No source-preservation limitation.
