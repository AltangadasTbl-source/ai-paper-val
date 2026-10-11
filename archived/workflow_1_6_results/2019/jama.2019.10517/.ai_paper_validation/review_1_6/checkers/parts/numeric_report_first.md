# Numeric consistency checker — main article origins pages 1–6

Fresh runtime: `01a1286a-6645-7930-8d1b-45686ffab070`; model `gpt-6.1-sol`; reasoning effort `medium`.
Assigned scope: DOC-001 `jama_flint_2019_oi_190079.pdf` physical PDF pp.1–6 (journal622–627), abstract, definitions, Figure1, Tables1–2, initial results/statistical conventions. Counterpart report pages7/8 and DOC-003 p9 used only for relationships originating in pp1–6. Full current main map and relevant support definitions were read. Ninety-six local relationships RF001–RF096 are recorded in `relationships/parts/numeric_report_first.md`; all assigned quantitative records checked.

O=sertraline+olanzapine, n64; P=sertraline+placebo, n62. All main article locations are REPORT by their reporting content. Results eFigure8 is REPORT. The five candidate statements below have no assigned stable C ID, severity, validity, or disposition; all require human adjudication. Candidate identification is uncapped.

Evidence method: direct source `pdftotext -layout` (Poppler26.01.0), with targeted source pp3/4 and current source-matched rendered pp5/6 visual inspection. Reused assets and maps serve as locators. No source/reused asset changed; no old candidate or report conclusions used.

## RF-CAND-01 — Hyperlipidemia percentages conflict with table arm denominators

- Relationship: RF072 (Table1 Hyperlipidemia).
- Compared locations and roles: REPORT DOC-001 Table1 p5 column headers O n64/P n62 versus REPORT same Table1 hyperlipidemia row O18(29.0)/P19(29.7). Evidence: [main article PDF p5](../../../../jama_flint_2019_oi_190079.pdf#page=5).
- Printed inputs: `Sertraline + Olanzapine (n = 64)`, `Sertraline + Placebo (n = 62)`, `Hyperlipidemia 18 (29.0) 19 (29.7)`. No row-specific n or footnote denominator appears. Direct native extraction and the rendered source-matched table agree.
- Rule/calculation: count divided by column n times100. O100×18/64=28.125%, which rounds28.1%; P100×19/62=30.64516%, which rounds30.6%. Printed29.0/29.7 lie outside ±0.05 percentage-point display tolerance. Conversely100×18/62=29.03226%→29.0 and100×19/64=29.6875%→29.7.
- Direct observation: printed percentages do not reconcile with printed column denominators. Inference: opposite-arm denominators reproduce both percentages; this is a diagnostic, not proof of the production mechanism.
- Alternatives: a row-specific reduced O denominator62 could explain29.0, but the P percentage requires approximately64, exceeding its assigned group62; ordinary missingness in P cannot explain it. Counts, percentages, or arm assignment could be mistranscribed. No alternative denominator is supplied.
- Quality-control relevance: baseline comorbidity prevalence may be copied with incorrect group labels or denominators in evidence extraction. No consequence for trial conclusions is inferred.
- Exact human question: Are the hyperlipidemia counts18/19, percentages29.0/29.7, or arm placement incorrect, and what source denominator was actually used for each cell?
- Classification input: discrepancy solely within main REPORT; no PLAN or separate REPORT comparator needed.

## RF-CAND-02 — Placebo living-arrangement categories account for60 of62 participants

- Relationship: RF078.
- Compared locations and roles: REPORT DOC-001 Table1 p5 P header n62 and living-arrangement rows with others49(79.0), alone10(16.1), senior residence1(1.6). REPORT same table O header64 and analogous46/17/1 are an internal corroborating control. Evidence: [main article PDF p5](../../../../jama_flint_2019_oi_190079.pdf#page=5).
- Printed inputs: above three named categories; no unknown/missing category or restricted denominator printed for living arrangements.
- Rule/calculation: if the displayed partition represents the whole column population, sum categories must equal n. P49+10+1=60;62−60=2 unaccounted participants.79.0+16.1+1.6=96.7%; integer deficit2/62×100=3.22581%. O46+17+1=64. Each separate printed P percentage correctly uses n62.
- Tolerance: integer sums exact; rounding three one-decimal percentages can explain at most0.15 percentage points of deviation, not3.3 points.
- Direct observation: the listed P counts total60 versus header62. Conditional inference: the category block is incomplete unless two participants had unprinted missing/other status; the package does not explicitly declare exhaustive living arrangements.
- Alternatives: two participants may have missing or unlisted living-arrangement data; categories may not have been intended as exhaustive. If n60 complete cases were intended, printed percentages use62 instead, so the denominator convention still needs disclosure. A row count could be a transcription error.
- Quality-control relevance: readers can mistake60 accounted participants for a complete62-person category distribution; missingness versus an omitted category changes extractable baseline counts.
- Exact human question: What are the living-arrangement or missing-data statuses of the two placebo participants absent from the three displayed categories, and is62 the intended denominator for these percentages?
- Classification input: one REPORT table-internal total/missingness relationship, conditional on the unprinted category definition.

## RF-CAND-03 — DKEFS color-word row points to a Barnes akathisia footnote

- Relationship: RF087.
- Compared locations and roles: REPORT DOC-001 Table2 p6 DKEFS color word interference condition3 final weighted scaled-score row with superscripti versus REPORT footnotei defining Barnes global clinical assessment0–5; REPORT footnoteh defines both DKEFS tasks as scaled1–19. Evidence: [main article PDF p6](../../../../jama_flint_2019_oi_190079.pdf#page=6).
- Printed inputs: DKEFS row O8.6(2.9),n60;P7.6(2.8),n58; row superscripti. Footnotei: Barnes global0–5,higher worse,0 absent. Footnoteh: trail making and color word interference,scaled1–19,higher better,10 normative mean. Barnes row has no superscripti in the source-matched image.
- Rule/calculation: row footnote must identify that row's measure/scale. Applying footnotei literally gives a bounded0–5 measure yet row means8.6 and7.6 exceed5 by3.6/2.6, and the scale direction/construct differ. Footnoteh instead explicitly describes the reported cognitive measure and permits those means.
- Tolerance: exact label/footnote identity; even one-decimal rounding ±0.05 leaves both means>5.
- Direct observation: superscripti is attached to the DKEFS color-word row but texti names Barnes akathisia. Inference: misplaced marker or omitted sharedh is a plausible production explanation, not an assigned correction.
- Alternatives: footnoteh may have been intended to cover both DKEFS rows implicitly, whilei was displaced from Barnes; data values may all be correct. This resolves quantitative interpretation only after recognizing the marker mismatch.
- Quality-control relevance: a reader following the printed marker could apply the wrong range and direction to cognitive scores or misidentify them as extrapyramidal adverse effects.
- Exact human question: Which footnote marker belongs on the DKEFS color-word row, and should footnotei instead identify the Barnes akathisia row?
- Classification input: REPORT internal measure/scale-label discrepancy.

## RF-CAND-04 — UKU adverse-effect rule includes score4 outside stated0–3 item range

- Relationship: RF041.
- Compared locations and roles: REPORT DOC-001 p4 Other Measures of Tolerability, UKU range definition versus REPORT same paragraph operational adverse-effect rule. Evidence: [main article PDF p4](../../../../jama_flint_2019_oi_190079.pdf#page=4).
- Printed inputs: UKU “score range,0-3 on each of48items”; except weight gain/loss, adverse effect present if “a2-point increase from RCT baseline or a score of3or4 and an increase from baseline.”
- Rule/calculation: under stated integer range S={0,1,2,3}, the score4 branch cannot occur;4>max(S)=3 by1 scale point. Range and rule concern the same UKU items and paragraph.
- Tolerance: exact integer threshold/range; rounding does not apply.
- Direct observation: stated operational threshold contains an out-of-range value. Inference: the rule or range may have a reporting error, or the item scores were recoded, but no recoding is disclosed in this report.
- Alternatives: inclusion of4 may be harmless redundant wording in an “or” rule since3 remains attainable; a1–4 recoding could produce4 but would contradict the printed0–3 range without explanation. PLAN UKU threshold is not a conflicting origin in this numeric shard and is not used to upgrade classification.
- Quality-control relevance: adverse-event prevalence definitions are part of downstream extractable outcomes; replicating the threshold requires an unambiguous score system. No change to counts or conclusions is asserted.
- Exact human question: Was UKU actually scored0–3, was any item recoded to include4, and what precise threshold generated the reported adverse-effect frequencies?
- Classification input: REPORT internal scale/operational-threshold discrepancy.

## RF-CAND-05 — Abstract labels HbA1c daily coefficient mg/dL while outcome is reported as percent

- Relationship: RF018.
- Compared locations and roles: REPORT DOC-001 p1 abstract daily HbA1c result (also same unit repeated p7) versus REPORT DOC-001 p8 Table4 HbA1c,% and REPORT DOC-003 `joi190079supp2_prod.pdf` p9 eFigure8 HbA1c(%) by Day. Evidence: [main article PDF p1](../../../../jama_flint_2019_oi_190079.pdf#page=1), [main article PDF p7](../../../../jama_flint_2019_oi_190079.pdf#page=7), [main article PDF p8](../../../../jama_flint_2019_oi_190079.pdf#page=8), [results supplement PDF p9](../../../../joi190079supp2_prod.pdf#page=9).
- Printed inputs: daily coefficient−0.0002mg/dL,95%CI−0.0021 to0.0016 in abstract; p7 repeatsmg/dL. Table4 HbA1c,% baseline means5.9/5.9 and termination5.7/5.9; eFigure8 labels HbA1c(%) versusDay. Direct source eFigure8 native text explicitly prints(%).
- Rule/calculation: a time slope for a response measured in percent has units percentage points/day, unless a response conversion is stated. The printed mass concentrationmg/dL and response% are different dimensions; no supplied conversion is given. Do not multiply coefficient by252 and compare raw group changes because quadratic time and differing follow-up are present.
- Tolerance: exact dimensional identity; coefficient rounding cannot change a unit.
- Direct observation: main result unitmg/dL differs from percent in main descriptive table and corresponding model figure. Inference: copied metabolic concentration unit is a plausible explanation, not a determined correction.
- Alternatives: a separate concentration-transformed HbA1c analysis could be intended, but the report gives no transformation and the matched mixed-model figure is in%. Raw descriptive changes and model slopes are different estimands; that distinction does not itself explain different response dimensions.
- Quality-control relevance: data extraction can preserve an incorrect unit for an HbA1c treatment×time coefficient or combine it with incompatible outcomes.
- Exact human question: What response unit was used for the HbA1c mixed model, and should the reported daily coefficient/interval carry percentage points per day or another explicitly defined unit?
- Classification input: main REPORT internal unit mismatch plus main REPORT versus separate results REPORT unit mismatch; both substantive comparisons preserved for coordinator classification.

## Complete no-candidate checks and limitations

All96 relationships and their printed inputs/calculations/tolerances/outcomes appear in the paired inventory. Figure1 every upstream transition, reason sum, allocation receipt and randomized endpoint disposition reconciles. Abstract114 completion equals67 remission/near-remission endpoints plus47 relapse endpoints and also126−12 discontinuations; no flow discrepancy is emitted. Table1 every percentage other than hyperlipidemia reconciles with64/62; age/sex/race/marital/site partitions reconcile. Exact .05 rounding ties explain56.2 for36/64 and other half-decimal choices; sums100.1 from rounding are not findings. Restricted sample sizes are preserved. Table2 count-format decimals are still counts under No.(%), and their percentages reconcile. AIMS individual-item range and separate global-summary range do not establish an identical scale item from supplied evidence; no candidate is created solely by that alignment assumption. Simpson-Angus0–40 versus0–36 explicitly changes included item set. Target dosage versus observed IQR is not an arithmetic conflict. Planned128 versus observed126 is not misreported enrollment. No personal event counts, person-time, missing raw data, or statistical conventions are invented.

Limitations: row-specific hyperlipidemia denominators, living-arrangement missingness categories, and HbA1c conversion/scoring definitions are not printed. Inferential calculations and PLAN-origin comparisons are assigned to other current reviewers. All first-six-page quantitative relationships were inspected; no scientific-coverage gaps remain within this scope. No DISPLAY_ZERO_NOT_CANDIDATE occurrence is present here. Sources and reuse assets are unchanged.

