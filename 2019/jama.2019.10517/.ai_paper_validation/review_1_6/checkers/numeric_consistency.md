# Complete Numeric Consistency Review

Merged complete four-shard numeric review: 400 checked relationships, no candidate-count cap. Original specialist cards retain their local candidate labels and runtime provenance. Genuine duplicate candidates are merged only by the coordinator before stable C IDs.

# Numeric consistency checker — main article origins pages 1–6

Fresh runtime: `01a1286a-6645-7930-8d1b-45686ffab070`; model `gpt-6.1-sol`; reasoning effort `medium`.
Assigned scope: DOC-001 `jama_flint_2019_oi_190079.pdf` physical PDF pp.1–6 (journal622–627), abstract, definitions, Figure1, Tables1–2, initial results/statistical conventions. Counterpart report pages7/8 and DOC-003 p9 used only for relationships originating in pp1–6. Full current main map and relevant support definitions were read. Ninety-six local relationships RF001–RF096 are recorded in `relationships/parts/numeric_report_first.md`; all assigned quantitative records checked.

O=sertraline+olanzapine, n64; P=sertraline+placebo, n62. All main article locations are REPORT by their reporting content. Results eFigure8 is REPORT. The five candidate statements below have no assigned stable C ID, severity, validity, or disposition; all require human adjudication. Candidate identification is uncapped.

Evidence method: direct source `pdftotext -layout` (Poppler26.01.0), with targeted source pp3/4 and current source-matched rendered pp5/6 visual inspection. Reused assets and maps serve as locators. No source/reused asset changed; no old candidate or report conclusions used.

## RF-CAND-01 — Hyperlipidemia percentages conflict with table arm denominators

- Relationship: RF072 (Table1 Hyperlipidemia).
- Compared locations and roles: REPORT DOC-001 Table1 p5 column headers O n64/P n62 versus REPORT same Table1 hyperlipidemia row O18(29.0)/P19(29.7). Evidence: [main article PDF p5](../../../jama_flint_2019_oi_190079.pdf#page=5).
- Printed inputs: `Sertraline + Olanzapine (n = 64)`, `Sertraline + Placebo (n = 62)`, `Hyperlipidemia 18 (29.0) 19 (29.7)`. No row-specific n or footnote denominator appears. Direct native extraction and the rendered source-matched table agree.
- Rule/calculation: count divided by column n times100. O100×18/64=28.125%, which rounds28.1%; P100×19/62=30.64516%, which rounds30.6%. Printed29.0/29.7 lie outside ±0.05 percentage-point display tolerance. Conversely100×18/62=29.03226%→29.0 and100×19/64=29.6875%→29.7.
- Direct observation: printed percentages do not reconcile with printed column denominators. Inference: opposite-arm denominators reproduce both percentages; this is a diagnostic, not proof of the production mechanism.
- Alternatives: a row-specific reduced O denominator62 could explain29.0, but the P percentage requires approximately64, exceeding its assigned group62; ordinary missingness in P cannot explain it. Counts, percentages, or arm assignment could be mistranscribed. No alternative denominator is supplied.
- Quality-control relevance: baseline comorbidity prevalence may be copied with incorrect group labels or denominators in evidence extraction. No consequence for trial conclusions is inferred.
- Exact human question: Are the hyperlipidemia counts18/19, percentages29.0/29.7, or arm placement incorrect, and what source denominator was actually used for each cell?
- Classification input: discrepancy solely within main REPORT; no PLAN or separate REPORT comparator needed.

## RF-CAND-02 — Placebo living-arrangement categories account for60 of62 participants

- Relationship: RF078.
- Compared locations and roles: REPORT DOC-001 Table1 p5 P header n62 and living-arrangement rows with others49(79.0), alone10(16.1), senior residence1(1.6). REPORT same table O header64 and analogous46/17/1 are an internal corroborating control. Evidence: [main article PDF p5](../../../jama_flint_2019_oi_190079.pdf#page=5).
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
- Compared locations and roles: REPORT DOC-001 Table2 p6 DKEFS color word interference condition3 final weighted scaled-score row with superscripti versus REPORT footnotei defining Barnes global clinical assessment0–5; REPORT footnoteh defines both DKEFS tasks as scaled1–19. Evidence: [main article PDF p6](../../../jama_flint_2019_oi_190079.pdf#page=6).
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
- Compared locations and roles: REPORT DOC-001 p4 Other Measures of Tolerability, UKU range definition versus REPORT same paragraph operational adverse-effect rule. Evidence: [main article PDF p4](../../../jama_flint_2019_oi_190079.pdf#page=4).
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
- Compared locations and roles: REPORT DOC-001 p1 abstract daily HbA1c result (also same unit repeated p7) versus REPORT DOC-001 p8 Table4 HbA1c,% and REPORT DOC-003 `joi190079supp2_prod.pdf` p9 eFigure8 HbA1c(%) by Day. Evidence: [main article PDF p1](../../../jama_flint_2019_oi_190079.pdf#page=1), [main article PDF p7](../../../jama_flint_2019_oi_190079.pdf#page=7), [main article PDF p8](../../../jama_flint_2019_oi_190079.pdf#page=8), [results supplement PDF p9](../../../joi190079supp2_prod.pdf#page=9).
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



# Numeric consistency checker: late main report and complete results figures

Fresh runtime UUID: 01a1286a-814f-7b12-a00b-e90ab6064dbe. Model gpt-6.1-sol, medium. Origin scope DOC-001 pp7–10 and DOC-003 pp1–10; earlier main locations comparators only. Ownership restricted to this checker and relationships/parts/numeric_report_last.md. Complete assigned scope reviewed: 83 local quantitative relationships, 5 distinct local candidates, 14/14 pages, 9/9 support figures, no scientific coverage gap. All compared locations below are REPORT by content. No stable C IDs, adjudications, severity or dispositions are assigned.

Inputs were current full main/support maps and source-grounded model definitions, source-linked native assets, all nine reusable figure images, main Tables4/5 images, and direct Poppler source text for pp7–10 and methods comparator p5. Source files and all reused assets preserved. No old candidate/report conclusions, web, outside literature, Python extraction, OCR or GPU used. Native blanks in Table4 preserved. A complete row-by-row arithmetic/numeric inventory is in [the assigned relationship shard](../relationships/parts/numeric_report_last.md). Source links resolve three directories above this merged checker; shard links resolve four levels above their own parts directory.

## RL-CAND-01 — Placebo relapse hospitalization percentage does not round to the printed value

**Relationship:** RL009; comparator RL006. Primary category proposed: Denominator, proportion, or total inconsistency.

**Compared locations and roles:** [DOC-001 p8, opening tolerability continuation, REPORT](../../../jama_flint_2019_oi_190079.pdf#page=8); [DOC-001 p7 Table3 psychiatric hospitalization, REPORT](../../../jama_flint_2019_oi_190079.pdf#page=7). The discrepancy is within the main REPORT document; the Table3 count corroborates numerator11.

**Printed inputs:** p8: “11 (32.3%) of 34 in the placebo group required psychiatric hospitalization because of the relapse.” Table3 placebo hospitalization11. Adjacent olanzapine statement6(46.2%) of13.

**Rule and calculation:** A printed one-decimal percent for11/34 under nearest rounding equals100×11/34=32.352941176%, hence32.4%. A32.3% display under nearest rounding represents[32.25%,32.35%); the exact count ratio lies0.002941 percentage point above its upper rounding boundary. Equivalently the displayed deviation is0.052941 percentage point, exceeding half-unit tolerance0.05. Adjacent6/13=46.153846% correctly yields46.2%.

**Direct observation versus inference:** Source text and rendered p8 directly print11,34,32.3%; only division and nearest-rounding inference are derived. No participant-level reconstruction is required.

**Alternatives:** Truncating rather than rounding11/34 yields32.3%, but neighboring6/13 and other article percentages use nearest rounding; a deliberate alternate display convention must be clarified. An unprinted differing numerator/denominator cannot be substituted for the sentence's explicit11 of34.

**Quality-control relevance:** A small participant-proportion mismatch can be copied into adverse-event or hospitalization extraction. No paper-conclusion effect is asserted.

**Exact human question:** Was32.3% obtained by a documented truncation convention, or should the displayed percentage for the explicit11/34 hospitalization count be reconciled with ordinary one-decimal rounding?

## RL-CAND-02 — Total cholesterol unadjusted absolute risk difference does not reconcile with its arm counts

**Relationship:** RL054 (Table5 total difference; coordinator may rebase local relationship numbering from inventory). Primary category proposed: Denominator, proportion, or total inconsistency.

**Compared locations and roles:** [DOC-001 p9 Table5, total cholesterol row and O64/P62 column headers, REPORT](../../../jama_flint_2019_oi_190079.pdf#page=9). All three cells and headers belong to one REPORT document.

**Printed inputs:** O9(14.1%), n64; P6(9.7%), n62; “Absolute Unadjusted Difference Between Groups, % (95% CI)”4.3(−8 to17.2). Threshold above both baseline and240mg/dL.

**Rule and calculation:** Signed O-minus-P unadjusted risk difference in percentage points=100×(9/64−6/62)=14.0625−9.677419355=4.385080645. Nearest0.1 gives4.4;4.3±0.05 spans[4.25,4.35], excluding4.385080645. The discrepancy from display4.3 is0.085080645 percentage point. Even subtraction of the printed arm percentages yields14.1−9.7=4.4. No hypothesis-test reconstruction or CI-symmetry assumption is needed. Printed arm percentages themselves round correctly.

**Direct observation versus inference:** Values/headers are directly printed and visually inspected; difference calculation is derived from explicit arm counts and denominators.

**Alternatives:** A different complete-case denominator or model-derived estimate could change the difference, but no differing denominator is named and the column explicitly says unadjusted. A truncation convention would produce4.3 but is not stated and differs from nearest rounding of arm proportions. ExactCI footnote b is attached only to triglyceride/glucose, so no unsupported method for this CI is assumed.

**Quality-control relevance:** This independently labeled metabolic incidence difference may be reused as a risk difference in a downstream evidence table. The issue is the small point-estimate arithmetic mismatch, not inferred clinical impact.

**Exact human question:** Which denominators and rounding rule generated the total-cholesterol difference4.3 percentage points, and do they agree with the table's explicit9/64 and6/62 counts and “unadjusted” label?

## RL-CAND-03 — LDL unadjusted absolute risk difference does not reconcile with its arm counts

**Relationship:** RL055 (Table5 LDL difference; coordinator may rebase local relationship numbering from inventory). Primary category proposed: Denominator, proportion, or total inconsistency.

**Compared locations and roles:** [DOC-001 p9 Table5, LDL row and O64/P62 column headers, REPORT](../../../jama_flint_2019_oi_190079.pdf#page=9). Same REPORT document; this is a separately labeled LDL result.

**Printed inputs:** O9(14.1%), n64; P6(9.7%), n62; absolute unadjusted difference4.3(−8 to17.2); LDL qualifying value above both baseline and160mg/dL.

**Rule and calculation:** 100×(9/64−6/62)=4.385080645 percentage points, nearest0.1=4.4, outside the4.3±0.05 rounding interval. Displayed percentages14.1−9.7=4.4. Exact counts have zero input tolerance. CI contains the estimate and zero; no unsupported exact/normal convention is inferred.

**Direct observation versus inference:** Explicit LDL cells and denominators directly observed; arithmetic derived. The identical total-cholesterol row is a separate reported outcome, not evidence that the outcomes' participant identities are equal.

**Alternatives:** Different unprinted denominator or truncation rule could explain production, but neither is identified in the table. Identical counts across LDL/total cholesterol are plausible and are not themselves treated as duplicate-data evidence.

**Quality-control relevance:** LDL incidence is separately extractable and can transmit its own point-estimate discrepancy. Shared printed arithmetic with total cholesterol does not collapse the different outcome/comparator relationship.

**Exact human question:** Which denominators and rounding rule generated the LDL difference4.3 percentage points, and do they agree with the LDL row's9/64 and6/62 counts and the unadjusted-difference label?

## RL-CAND-04 — HbA1c trajectory coefficient is labeled mg/dL while the reported outcome uses percent

**Relationship:** RL028; DOC-003 eFigure8, Table4 HbA1c rows as comparators. Primary category proposed: Measure, label, or scale inconsistency.

**Compared locations and roles:** [DOC-001 p7 Secondary Outcomes, HbA1c coefficient, REPORT](../../../jama_flint_2019_oi_190079.pdf#page=7); [DOC-001 p8 Table4 HbA1c row, REPORT](../../../jama_flint_2019_oi_190079.pdf#page=8); [DOC-003 p9 eFigure8 axis, REPORT](../../../joi190079supp2_prod.pdf#page=9); [DOC-001 p1 abstract repeated HbA1c result, REPORT](../../../jama_flint_2019_oi_190079.pdf#page=1), comparator only. Within-main unit mismatch and main-versus-results-supplement unit mismatch are substantive comparisons.

**Printed inputs:** Main p7 daily treatment×linear-time coefficient for HbA1c:−0.0002mg/dL,95%CI−0.0021 to0.0016,adjustedP=.99; abstract repeats the same mg/dL labels. Table4 outcome “HbA1c, %,” baseline means5.9 in each arm, termination5.7 O/5.9 P. Supplement axis “HbA1c (%)”, ticks5.6/5.8/6.0/6.2, Day axis.

**Rule and calculation:** A linear coefficient for an outcome measured in percent has percentage-point/day scale unless a transformation/conversion is supplied; mg/dL denotes a different measurement unit. Numerically the plotted approximate slope contrast[(5.71−5.90)−(5.76−5.89)]/252≈−0.000238 percentage point/day, compatible with coefficient−0.0002 at its coarse precision. This graphic is corroborative only; the exact printed dimensional disagreement requires no extraction of coordinates. Unit-label tolerance is zero. Plot readings are approximate±0.015 percentage point per endpoint.

**Direct observation versus inference:** mg/dL in narrative and% in Table4/figure are exact labels. Inferred dimensional rule and graphical slope illustrate rather than replace the printed comparison. Estimate/CI order is coherent and not a separate candidate.

**Alternatives:** A model using a separately converted concentration outcome could justify mg/dL, but the supplied report does not identify such a conversion and the stated trajectory figure uses%. An intended use of “percent” for the daily effect is a possible explanation, not a prescribed correction.

**Quality-control relevance:** Unit confusion affects effect extraction and interpretation of the very small trajectory coefficient; no claim about a statistically significant glycemic effect is made.

**Exact human question:** Was the HbA1c mixed model fit on the percentage scale shown in Table4/eFigure8, or on a documented concentration scale; what unit should accompany the displayed daily coefficient and interval?

## RL-CAND-05 — Simpson–Angus weekly effect labeled score points matches the plotted log-scale contrast more closely

**Relationship:** RL034; DOC-003 eFigure9. Primary category proposed: Measure, label, or scale inconsistency.

**Compared locations and roles:** [DOC-001 p7 Extrapyramidal Measures, REPORT](../../../jama_flint_2019_oi_190079.pdf#page=7); [DOC-001 p4 Statistical Analysis, Poisson mixed model, REPORT](../../../jama_flint_2019_oi_190079.pdf#page=4), continuing on [p5](../../../jama_flint_2019_oi_190079.pdf#page=5), model-definition comparator; [DOC-003 p10 eFigure9 title and Week/SAS Total Score axes, REPORT](../../../joi190079supp2_prod.pdf#page=10). Within-main coefficient/model interpretation question and main-to-results-figure scale comparison; all REPORT.

**Printed inputs:** “Weekly changes in Simpson-Angus Scale total score ... (0.022 points [95% CI,0.009–0.036], adjustedP=.009).” Methods specify a Poisson mixed model with overdispersion, random intercept, site/time/treatment/interaction. eFigure9 displays mixed-model least-square means of total score, x weeks0–36; O approximately.56 at0 and.73 at36; P approximately.685 at0 and.40 at36. No numerical plot-coordinate table or link/back-transformation formula is supplied.

**Rule and reproducible diagnostic:** If0.022 is a constant difference of weekly changes in raw score points for these plotted means, its full36-week contrast of changes would be0.792points. The graph instead gives(.73−.56)−(.40−.685)=.455points, hence.455/36=.0126389 points/week. With±.02 score uncertainty for each of four endpoints, the diagnostic contrast range is.375–.535, or.0104167–.0148611 points/week, disjoint from nearest-rounding interval.0215–.0225. This check does not compare0.022 with its CI—the interval describes uncertainty in a fitted parameter rather than graph-reading precision. A natural-log trajectory contrast calculated as[ln(.73/.56)−ln(.40/.685)]/36≈.02231/week is numerically close to printed.022. The ln calculation is expressly a diagnostic; the package specifies Poisson but does not explicitly state the link.

**Direct observation versus inference:** Printed0.022“points,” Poisson model wording, score/time axes are direct. All curve values, raw slope and logarithmic interpretation are inferred approximations. The figure lines are gently exponential; no exact curve points or constant raw-slope model is asserted.

**Alternatives:** Poisson coefficient with a log link may explain the numeric agreement if the unit is an unback-transformed interaction rather than raw points. A particular marginal derivative or other back-transformed effect at a chosen time/population could also yield a raw-score value. Those definitions are absent; the specific production mechanism is not inferred as fact. The concrete question is the scale of the displayed effect in relation to the named model and plotted outcome, not a complaint solely about an unreported link.

**Quality-control relevance:** Extracting0.022 as a raw weekly score difference could overstate a36-week score contrast relative to the accompanying graph. This concerns measure labeling and downstream numeric reuse, not efficacy or the tolerability conclusion.

**Exact human question:** Is0.022 the treatment×week coefficient on a Poisson link scale or a back-transformed difference in total-score points, and what time/reference population or transformation makes the “points” label agree with eFigure9?

## Complete noncandidate checks and limitations

All83 relationship rows are complete. Table3 event counts intentionally overlap: O15/P44 events versus13/34 relapsers are allowed by footnote. Survival risk sets fall monotonically and reconcile to43/24 completed-remission persons; Kaplan–Meier curves are not equated to uncensored risks. P≤12-week majority-relapse prose is compatible with risk-set loss even after all4 other exits are removed. Observation median19.5 is compatible with half followed≤20weeks. “45% ... did not relapse” equals28/62=45.16% at whole-percent precision, not an inferred Kaplan–Meier estimate.

All Table4 arm-specific sample counts, mean/SD or median/IQR inputs and intervals are retained, including native blanks. Every displayed estimate is inside ordered CI. Termination minus marginal baseline means is not forced to equal paired differences because footnote explicitly permits missing-data effects; median differences are not generally differences of medians. Mixed-model LS means are not raw baseline/termination means. All Table5 arm percentages reconcile; triglyceride3.0 and glucose−.2 differences reconcile; identical total/LDL counts do not themselves imply an error. ExactCI b applies only to triglyceride/glucose, and asymmetry is not treated as an arithmetic defect.

Tolerability percentages admit coherent integer counts under randomized denominators, but unprinted counts are not asserted. Pooled UKU incidence >5% is coherent for all five listed effects, even where one arm's percentage is≤5%. Falls20/64 and11/62 and SAEs12/64 and12/62 round correctly; ≥1 events denotes persons rather than event totals. One fatal SAE is distinct from all-cause hospitalization/relapse event totals. Statin6+6=12 and hypoglycemic2+1=3 sensitivity totals reconcile.

Cox estimates are positive, ordered/contained and correctly labeled by reference group. All eight metabolic coefficients agree with repeated abstract values and directions; Holm-adjusted P values cannot be compared directly with unadjusted interval-derived nominal P values. Pattern-mixture triglyceride curves lack subgroup weighting; no invented aggregate is constructed. Weight, cholesterol and glucose contain quadratic time and cannot be checked by extrapolating linear coefficients over252days. Waist/LDL/HDL/HbA1c graphical linear slope checks broadly agree numerically, subject to plot precision. Anthropometric/metabolic Day252=36weeks; last tick250 is not a shorter study.

NNT2.8 repeats consistently in pp7–8 and is explicitly described as HR-based. A crude-risk reciprocal yields2.896350364964, but the source does not state that crude risks were its computation, and HR plus unprinted baseline survival could generate a different survival-based NNT. That diagnostic is not emitted as a candidate without a concrete source-grounded identical-estimand contradiction. All nine eFigure panel titles/units/legends/axis ticks are covered; cover and administrative/reference page have no additional current-trial result. No display-zero P appears.

Limitations: graphical coordinates approximate; confidence level of DOC-003 shaded bands unspecified; exact subgroup weights, Poisson link/back-transformation, NNT survival computation and Table4 paired subsets unavailable. None prevents page or numeric-relationship coverage. Every candidate remains a quality-control question for human review.



# Numeric consistency checker: protocol pages 1–21

Runtime UUID: 01a1286a-9bc9-7b92-a717-2777aa292dbf. Fresh numeric-review specialist; gpt-6.1-sol/medium. Exact disjoint origin scope: DOC-002 physical pages 1–21. Complete inventory: relationships/parts/numeric_plan_first.md, 105 provisional PF relationships. Every assigned source page was reviewed, including administrative/no-applicable content, Figures1–2, and Tables1–4. All compared source locations below are PLAN, including the protocol's historical STOP-PD summaries. Sources and pre-existing assets were preserved. The supplied scope and review contract govern this numeric review; no external scientific claims or broad methodology audit were performed.

Three distinct document-grounded candidate observations are emitted without stable C IDs, severity, validity, acceptance, or disposition. Human adjudication remains pending. The complete quantitative inventory also records no-candidate checks, population/model distinctions, and bounded diagnostic limitations.

## PF-CAND-01 — Conflicting prospective per-site recruitment totals

**Relationship:** PF099. **Primary category proposed:** Numeric or arithmetic inconsistency.

**Compared locations and content roles:**

- [DOC-002 p21, Section4.2.1, lines995–997](../../../joi190079supp1_prod.pdf#page=21), PLAN: “four research sites, with each site recruiting 82 patients 18 years or older” with psychotic depression.
- [DOC-002 p17, Table4 first row, line842](../../../joi190079supp1_prod.pdf#page=17), PLAN: all four sites; “Each site will recruit 98 acutely ill participants and randomize 44 remitted participants.”
- [DOC-002 p7, Section3.9.1 general overview and Figure1](../../../joi190079supp1_prod.pdf#page=7), PLAN: 392 acute participants across4sites; stabilization196; randomized176. This corroborates the p17 acute target and supplies the common phase identity.

**Printed inputs:** four sites;82 per site;98 per site;392 acute overall. The target176 randomized is not substituted for the acute target.

**Rule and calculation:** Equal per-site contributions to the same proposed acute recruitment target should sum to the stated overall total. Four×98=392; four×82=328;392−328=64 participants;98−82=16 participants per site. Counts are exact; no rounding tolerance can account for16 per site.

**Direct observation versus inference:** The82 and98 targets and four-site identity are directly printed. The totals328 and difference64 are arithmetic deductions. The source p21 rendering was visually inspected and confirms82. The protocol map/direct table locator identifies98 in Table4; mechanical source-page recheck remains the next workflow stage.

**Alternatives and unresolved definition:**82 could be a historical target retained in one paragraph, a superseded version, or an intended subgroup rather than the complete acute population. No amendment label or subgroup qualifier in the cited passages establishes such a distinction. This observation concerns two prospective statements inside one PLAN, rather than any difference between planned enrollment and observed recruitment.

**Quality-control relevance:** The conflicting target can produce different extracted planned sample sizes or recruitment denominators in a protocol summary. It does not establish a problem with observed trial results.

**Exact human question:** Does “82 patients” in Section4.2.1 describe the same full acute recruitment population as98 per site in Table4 and392 overall in Section3.9.1, or is a supplied amendment or explicit population distinction intended to reconcile these targets?

## PF-CAND-02 — The MMSE≥24 threshold is attached to different entry phases

**Relationship:** PF034, corroborated by PF058. **Primary category proposed:** Measure, label, or scale inconsistency.

**Compared locations and content roles:**

- [DOC-002 p9, heading at line438](../../../joi190079supp1_prod.pdf#page=9), PLAN: “MMSE Score ≥24 to Enter the Stabilization Phase.”
- [DOC-002 p9, paragraph lines439–444](../../../joi190079supp1_prod.pdf#page=9), continuing line445 on [p10](../../../joi190079supp1_prod.pdf#page=10), PLAN: participants with MMSE<24 “at the end of the stabilization phase” are excluded from “participation in the RCT,” with specified exceptions; historical1/37 have<24 after stabilization.
- [DOC-002 p7, general overview and lines322–325](../../../joi190079supp1_prod.pdf#page=7), PLAN: MMSE≥24 at the end of stabilization qualifies entry to the36-week RCT; below24 may receive Steering Committee exception.
- [DOC-002 p11, Table1 footnoteH, lines508–509](../../../joi190079supp1_prod.pdf#page=11), PLAN, corroboration: MMSE assessed at the end of Stabilization; IQCODE is the baseline cognitive screen. This footnote independently helps locate the threshold's operational timing.

**Printed inputs:** Numeric threshold24; preceding stabilization8weeks; “enter Stabilization” versus “at end of Stabilization”/“enter RCT.” Conditional below24 exceptions are explicitly retained.

**Rule and calculation:** The same eligibility threshold must carry a consistent phase/time label. Entry into stabilization precedes its end and subsequent RCT entry by the standard8-week stabilization interval. This is a categorical timing identity check, not a claim that scores themselves differ; no arithmetic rounding applies.

**Direct observation versus inference:** Heading and paragraph are directly printed in the same page. The mismatch is between the threshold's printed entry-phase labels. The approximately8-week separation follows the printed standard phase duration; the two-week optional extension does not remove the different entry phases.

**Alternatives and unresolved definition:** The heading could be shorthand or a retained earlier-phase label; two separate eligibility gates could theoretically exist. The cited operational paragraph and scheduled MMSE timing identify the gate at stabilization end/RCT entry and do not establish a separate≥24 stabilization-entry gate. The case-by-case exception changes qualification for low scores, not the phase label.

**Quality-control relevance:** Extracting the heading alone could assign the numeric eligibility cutoff to an earlier population/time point. No methodological or clinical judgement follows from the label conflict.

**Exact human question:** Is the≥24 MMSE gate intended for entry into Stabilization, for entry into the RCT at Stabilization end, or for both; which supplied operational passage reconciles the heading with its paragraph and scheduled assessment time?

## PF-CAND-03 — The same historical35% is framed with two different denominators

**Relationship:** PF008. **Primary category proposed:** Denominator, proportion, or total inconsistency.

**Compared locations and content roles:**

- [DOC-002 p4, Section3.4, lines175–177](../../../joi190079supp1_prod.pdf#page=4), PLAN: in the Aronson chart review, “approximately35% of relapses occurred following the discontinuation of antipsychotic medication” while antidepressant continued.
- [DOC-002 p15, H1 power assumptions, lines728–732](../../../joi190079supp1_prod.pdf#page=15), PLAN: assumed15% relapse with continued sertraline+olanzapine and35% in sertraline+placebo; “A35% relapse following olanzapine discontinuation is the same as the rate reported by Aronson et al.32 in a naturalistic study of antipsychotic discontinuation in PD.”

**Printed inputs:** Approximately35% of relapses attributed to discontinuation in one passage;35% participant relapse risk after discontinuation in the other; same named historical chart review/reference32. The planned35% versus15% absolute20-point contrast is internally arithmetically coherent and is not this candidate.

**Rule and calculation:** Let R be all relapses, D the relapses following antipsychotic discontinuation, and E the persons at risk after discontinuation. Page4 describes D/R≈.35; the page15 participant relapse assumption and historical equivalence describe D/E≈.35. These are different conditional proportions unless the denominator populations coincide or the historical account supplies a further risk estimate. Equal printed percentages do not establish equal measures. No R,D,E counts are supplied, so actual participant risk cannot be recomputed; this is a printed denominator/identity contradiction pending clarification, not a reconstructed historical estimate.

**Tolerance:** The approximation “approximately” allows coarser percentage rounding but cannot reconcile different denominator definitions. No precision-based candidate is asserted.

**Direct observation versus inference:** The denominator wording “of relapses” and the later participant relapse-rate framing are direct observations. D/R versus D/E is a diagnostic symbolic transcription of those words. Whether the historical study actually supplies both quantities is unknown from the supplied package and cannot be settled using external literature under this review.

**Alternatives and unresolved definition:** Page4 may have inadvertently condensed a participant-risk denominator; page15 may cite a separate result from the same study; or the populations may coincide under an unprinted historical definition. These possibilities do not make the two printed summaries interchangeable and are the named missing definition.

**Quality-control relevance:** An extractor could carry the same35% forward as either the fraction of observed relapses associated with discontinuation or the risk among discontinuers. The observation does not establish that the chosen power assumption or trial conclusion is wrong.

**Exact human question:** In the supplied protocol's account of Aronson et al., does35% mean discontinuation-associated relapses divided by all relapses, or relapsing participants divided by all discontinuing participants; is a second distinct35% estimate or an explicit common denominator intended to support the claimed identity?

## Bounded non-candidate and diagnostic records

- Conservative flow: p8 explicitly distinguishes expected60% acute response from a50% scenario used to protect the randomized target.392×.5×.9=176.4 supports176;392×.6×.9=211.68 is a different scenario and is not registered as a contradiction.
- Recruitment-rate rounding:392/(4×38)=2.578947 rounds2.6 per site per month. Reconstructing395.2 from the rounded rate is not a candidate.
- Risk differences/NNT: Historical last-visit41.9%−23.9%=18.0points yields5.6; completer66.7%−49.2%=17.5points yields5.7. Planned35%−15%=20points yields5. Different populations are retained.
- Schedule: Source rendering corrected the mapper's metabolic visit labels to RCT8,16,24,32,36, all five observations. Original map8,12,20,28,36 was a derivative alignment error; no scientific candidate is generated from it. The inventory uses the corrected source schedule. Weight15RCTvisits and6open-label maximum scheduled columns reconcile with H2/H3 text. Every Table2/Table3 row was checked for power range, direction of change with contrast/attrition/effect/observation count, and the prose's matching power scenario. Missing simulation-generation details preclude exact power replication.
- Eligibility inequality: Direct p21 image confirms DAS≥2 and HAM-D≥21. Native/layout losses of equality strokes do not establish a source inconsistency.
- Orthostasis: The measurement after1minute standing is within the adverse-event criterion's3-minute window; no timing candidate is established by those values alone.
- Dose/time: Minimum10weeks beforeRCT in p13 is a loose lower bound compatible with standard12–20week course; no candidate is based on the arithmetic fact12≥10. Comparator p41 explicitly says minimum10/maximum20; coordinator notified that p7's authorized two-week stabilization extension can yield a22-week course with12-week acute duration. Plan-last owns the p41 comparison and any resulting candidate; this shard does not duplicate it.
- Covariate thresholds r≥.30 versus r>.30 appear in general/specific rules, but no printed r=.30 result is affected. No purely hypothetical boundary candidate is emitted.
- Metabolic exclusion “<5% (i.e.<10)” with176 participants is a loose bound: exact<5% means≤8, which is necessarily<10; it is not a claim that9/176<5%.
- Historical younger glucose t211 next to younger n117 is flagged as a statistical locator, not emitted here under an assumed one-sample test. The supplied passage does not identify the t model/population. Historical age-specific weight dispersion and adjusted F similarly cannot be forced into an unstated simple independent-means rule. Specialist statistical passes receive the exact source location.
- Historical means in p6 and12-week-completer means in p16 have different population definitions and do not establish duplicate-value inconsistency. The p16 standardization is diagnostically coherent:5.9/sqrt((16.5²+11.3²)/2)≈.417→.42.
- Estimated3relapses/site/year is an operational frequency: expected176×(.15+.35)/2=44relapses over approximately4×47/12=15.67site-years gives2.81≈3. It is not participant relapse risk.
- Informal historical “rates” in p4 are explicitly percentages over follow-up, without a competing person-time definition; no mere vocabulary candidate is emitted.

## Completion and limitations

Scope completed: DOC-002 pages1–21,21/21pages,105quantitative relationship records,3distinct candidate observations. No assigned scientific-coverage gaps. Sources and reused assets unchanged. All candidate compared locations are PLAN; the candidate relationships are wholly within plan material. Source locations and exact human questions are complete. No candidate count target or early stopping applied. Underlying historical denominators, historical model identities, and simulation inputs are not supplied; these are bounded reproducibility limitations, not omitted source units. Final source-page recheck and coordinator classification are subsequent required stages.


# Numeric consistency checker: plan-last shard

Runtime UUID: 01a1286a-b71f-73c2-90f9-22d2fd35e362; fresh gpt-6.1-sol/medium numeric reviewer. Exact origins: DOC-002 physical pp22–42 and DOC-004 p1. Complete relationship artifact: relationships/parts/numeric_plan_last.md,116 local PL relationships. This checker emits two distinct local candidates, without stable C IDs, adjudications, severity or dispositions. Every source location in either candidate is PLAN by content; historical data inside a protocol retain PLAN role. All22 assigned source pages covered. Historical STOP-PD populations are not current STOP-PD II trial populations.

Evidence inputs are the current mapper artifacts and source-linked reusable native/layout texts only. QUALITY_CONTROL_SCOPE.md and workflow_1_6/review_contract.md were read completely. No old candidate, verifier, critic or final report conclusions were read. No external evidence, unbundled Python or GPU was used. Direct Poppler rendering resolves table alignment and confirms Table5 transcription; direct source remains final authority at mandatory recheck.

## PL-CAND-01: historical Week6 completion total differs between race and ethnicity partitions

Relationship keys: PL038,PL073,PL075,PL077,PL079,PL081,PL087,PL088. Category cue: denominator/proportion/total consistency. Every compared location is the same historical Table5 in [DOC-002 p29](../../../joi190079supp1_prod.pdf#page=29), PLAN. The title reads “Percentage of Participants Completing the 12-Week STOP-PD Study by Ethnicity and Race.” Denominator header is “Number of Randomized Participants”; outcome header is “% Completers (Week6).” These are historical background results inside the protocol, not reported results for the current continuation RCT.

Printed inputs:

| Compared location and role | Randomized n | Week6 printed % | Compatible integer completers k | Exact100k/n |
|---|---:|---:|---:|---:|
| DOC-002 p29 Table5 Asian; PLAN |12|75.0|9|75.000000%|
| DOC-002 p29 Table5 Black or African American; PLAN |29|75.9|22|75.862069%|
| DOC-002 p29 Table5 White; PLAN |218|74.8|163|74.770642%|
| DOC-002 p29 Table5 Hispanic or Latino; PLAN |30|80.0|24|80.000000%|
| DOC-002 p29 Table5 Not Hispanic or Latino; PLAN |229|73.8|169|73.799127%|

Reproducible rule: under the printed row-specific randomized denominators, each one-decimal completion percentage p corresponds to integer k satisfying p−0.05≤100k/n<p+0.05 percentage points. Every row permits exactly one k: the feasible count interval has width0.001n≤0.229, so no second integer is possible. No half-rounding boundary is encountered. Both population partitions have total259:12+29+218=259 and30+229=259. If both describe the same259 participants at the same Week6 endpoint, their total number completing must agree. Race gives9+22+163=194; ethnicity gives24+169=193. Difference=1 completer, or100/259=0.386100 percentage points in the aggregate. Rounding each cell to its displayed precision cannot remove the mismatch.

Direct observation: printed denominators, percentages, common column labels and two complete denominator sums are confirmed visually on the supplied PDF p29. Derived diagnostic: the unique integer numerators and the194 versus193 totals. No completion numerator is printed in the table, and no particular row is identified as the source of the difference.

Necessary inputs available: displayed counts, percentages, common time, denominator labels and historical population identity. Missing inputs: raw historical completer counts, any row-specific alternative denominators, whether the race categories are mutually exclusive, and any undisclosed completion-classification difference across the two axes. Three race rows exactly total259 and prose racial percentages exactly total100.0%, strongly supporting an exhaustive partition; the two complementary ethnicity labels also total259.

Alternatives: undisclosed missingness/alternative outcome denominators could decouple printed randomized n from percentage denominators; overlapping race records plus unlisted persons could coincidentally sum259; axes might use distinct completion classifications. None is stated in Table5. A table transcription or rounding-method issue is possible but cannot be assigned to a cell from the supplied package. Adjacent Week12 diagnostic reconciles:6+15+121=16+126=142, and all individual Week12 cells round correctly. “Highly comparable” retention prose has no numerical comparability threshold and is not separately treated as a candidate.

Quality-control relevance: the table supports historical recruitment/retention background. Reusing it as an aggregate completion count could yield194 or193 for the same stated Week6 population. The observation does not establish a change to the current trial's conclusions.

Exact human question: Do the race and ethnicity rows partition the same259 randomized STOP-PD participants and use the printed randomized denominators for Week6 completion percentages? If so, which historical Week6 percentage/count requires reconciliation; if not, what denominator or completion-definition difference explains194 versus193 implied completers?

## PL-CAND-02: printed pre-RCT sertraline exposure range versus phase durations and permitted extension

Relationship keys: PL066,PL114; compared plan counterparts at p10–11,p25,p40 and corroborating p13. Category cue: numeric/arithmetic consistency in time labels. All locations are PLAN within the same protocol bundle.

Printed origin: [DOC-002 p41](../../../joi190079supp1_prod.pdf#page=41), lines2069–2070, A3.1 Sertraline states participants will have been taking sertraline for a “minimum of10weeks and a maximum of20weeks before entering the RCT.” Sertraline is open-label through acute/stabilization; p39 lines1979–1986 describes acute sertraline starting50mg/day and titration.

Printed counterparts: [DOC-002 p10](../../../joi190079supp1_prod.pdf#page=10), Table1 acute-phase header states “4–12wks in duration”; [p11](../../../joi190079supp1_prod.pdf#page=11), footnoteA/line491 explicitly states acute duration “between4and12weeks”; footnoteD/lines500–501 says end acute occurs between4and12weeks after starting study medications. [p25](../../../joi190079supp1_prod.pdf#page=25), lines1244–1248, and [p40](../../../joi190079supp1_prod.pdf#page=40), lines2043–2044, specify8-week stabilization before RCT. [p13](../../../joi190079supp1_prod.pdf#page=13) prospective RCT dosing repeats minimum10weeks sertraline; this repeated lower bound may be the same candidate emitted by the first-plan shard and must be merged before stable C assignment if rule/comparator match.

Additional printed counterpart: [DOC-002 p7](../../../joi190079supp1_prod.pdf#page=7), lines326–332, permits participants who achieved near-remission at acute end and have HAM-D >15 without psychosis at stabilization Week8 to have two additional weekly stabilization visits. These determine whether two consecutive weeks of partial-remission criteria are met before RCT entry; steering-committee agreement is required. The same page explicitly describes stabilization as continuation of open-label sertraline and olanzapine; p40 A2 likewise retains both drugs during stabilization. No medication discontinuation or exposure-clock suspension is stated for those additional stabilization visits.

Rule/calculation: sequential acute duration 4–12 weeks after initiating medication plus ordinary 8-week stabilization yields 12–20 weeks. The conditional two additional weekly visits after Week8 permit stabilization through Weeks9 and10; a participant entering stabilization after the allowed 12-week acute phase and successfully completing the extension has 12+8+2=22 weeks before RCT entry. Thus the printed maximum 20 agrees with the ordinary schedule but lacks the explicit permitted two-week exception. Printed minimum 10 is two weeks below the ordinary summed lower endpoint 12, although it could be a conservative inequality. These are whole-week prospective duration labels; arithmetic tolerance is 0 weeks, with no numerical rounding convention printed.

Direct observation: the p41 10–20 range, 4–12/8 component durations, explicit additional weekly stabilization visits, and continuation of sertraline through stabilization. Direct visual source confirmation covers p10/11 component labels. Derived comparison: ordinary summed 12–20 range and conditionally permitted 22-week exposure. No individual is claimed to have used the extension; the comparison concerns stated prospective limits. This is a plan-internal duration-label question, not an actual achieved exposure discrepancy or a broad participant-flow/design criticism.

Necessary inputs available: sequential phase definitions, dose-continuation statements, component duration labels, printed exposure range and extension rule. Missing input: whether the p41 maximum describes only the ordinary course and intentionally excludes extended stabilization; whether a rapid-response exception permits entering stabilization after 2 rather than 4 acute weeks; whether its duration clock differs from the acute-phase clock. p39 permits already prescribed sertraline/olanzapine to continue; prior exposure may lengthen medication exposure but does not by itself explain an ordinary course shorter than 4+8 measured from study initiation.

Alternatives: p41 may summarize ordinary exposure rather than all authorized exceptions; an explicit qualification for extended stabilization would then reconcile its maximum. Table1 may present a usual rather than absolute minimum despite footnote wording; two-week early transition may be intended by remission criteria requiring two consecutive assessments. A conservative minimum would allow actual duration ≥12 to satisfy ≥10. Those alternatives weaken the lower-endpoint observation but do not themselves reconcile maximum 20 with the permitted continuously treated 22-week path. No claim of actual excess exposure is made.

Quality-control relevance: a reader extracting the permitted pre-randomization treatment timeline obtains a maximum 20 from p41 but a conditional maximum 22 from the component rules and extension. The ordinary minimum is also labeled differently. This may affect protocol timeline extraction without establishing any actual participant exposure or trial conclusion was different.

Exact human question: Does the printed 10–20-week pre-RCT sertraline exposure range describe only the ordinary schedule and exclude the explicitly authorized two-week stabilization extension, which permits 12+8+2=22 weeks on continuous sertraline? If so, where is that qualification stated; and is the 10-week minimum a conservative bound or a permitted two-week acute course despite Table1's 4-week minimum?

## Completed noncandidate checks and source corrections

All116 relationships have explicit completed checks in the inventory. Table5 has all10individual percentages checked; racial/hispanic composition percentages reproduce at one decimal; two denominator totals agree259; Week12 total142reconciles; Week6 mismatch retained above. Historical5/259benztropine rounds to1.9%; “no more than7of259” is an upper-bound fraction, not an exact diabetes count. All20switch A/B pairs preserve starting4/3/2/1pills and nominal20/15/10/5mg, respectively; continued-arm active dose is constant and placebo-arm active dose nonincreasing. Identical Week3/Week4table rows are an explicit schedule.1-pill participants retain open-label drug through Week4and switch thereafter; a uniform25%weekly taper is not printed, and no independent four-week-boundary contradiction is established.

General olanzapine minimum5mg and indication-specific EPSE10mg minimum are distinguished rather than equated. Prospective recruitment/demographic targets do not require equality with current trial outcomes. Race/ethnicity census axes overlap. Historical reliability ICC ranges lie within[0,1], ordered, and are annual estimate ranges rather than confidence intervals. Background absolute risk/proportion and projected event frequency retain their populations and time horizons; no supplied person-time allows converting them into incidence rates.

Direct source correction: the current first-support mapping transcribed Table1metabolic-lab RCT marks as8,12,20,28,36. Visual comparison of physical pp10header and11marks establishes8,16,24,32,36. The corrected marks support an8-week cadence with a termination measurement at36; source-text derivatives were not edited. This derivative alignment error is not a paper candidate. p27“week4acute and thereafter every8weeks” is a broad cadence with phase-end/termination assessments; variable acute end prevents establishing one absolute timing contradiction absent an override definition.

DOC-004p1 contains administrative data-sharing availability/access conditions and no quantitative origin. Curator classifiesPLAN; mapper classifiesREPORT. Prospective operational content supportsPLAN; whether publication administrative disclosure isREPORTis a bounded role question. No numeric candidate is emitted solely from that classification difference.

## Direct derivative provenance and handoff

Direct tool recorded available: Poppler pdftoppm26.01.0; CPU PNG rendering only. Commands:

```bash
pdftoppm -f 29 -l 29 -singlefile -scale-to 1800 -png joi190079supp1_prod.pdf .ai_paper_validation/review_1_6/preprocessing/numeric-plan-last-p29
pdftoppm -f 11 -l 11 -singlefile -scale-to 1800 -png joi190079supp1_prod.pdf .ai_paper_validation/review_1_6/preprocessing/numeric-plan-last-p11
pdftoppm -f 10 -l 10 -singlefile -scale-to 1800 -png joi190079supp1_prod.pdf .ai_paper_validation/review_1_6/preprocessing/numeric-plan-last-p10
```

Outputs are matching.pngfiles, visually inspected using view_image. Rendered outputs are fresh derivatives under the authorized tree; no supplied/reused artifact modified. Exact candidate source PDF locations end in#page=N. Current candidate cards distinguish source-printed inputs from inferred integer numerators and summed timing.

Completion:22/22origin pages and116/116local relationships checked;2candidate records, including possible cross-shard duplicate of minimum-exposure relation. No scientific coverage gap. Underlying historical raw completer counts and explicit minimum-exposure exception are not supplied; these are candidate-specific missing definitions, not omitted units. Statistical P/CI/test reconstructions are not possible from these pages; no display-zeroPoccurs. Office/workbook/CSV sources do not exist here. Return artifacts: checkers/parts/numeric_plan_last.md and relationships/parts/numeric_plan_last.md.



Coordinator derivative-only arithmetic repair after statistical pass2: the crude reciprocal risk difference is 1/(34/62−13/64)=2.896350364964; an approximate2.894 in the original current-run diagnostic has been corrected in its shard and this merged artifact. This is not a source discrepancy because the printed2.8 is expressly HR-based and a matching computation is not supplied. Pass2 retains the original diagnostic text as provenance.

Coordinator derivative-only audit repair: N203/PF024 now quotes the source's unspecified unequal-variances test and labels ordinary Welch calculations as conditional. With the stated hypothetical SD/n inputs, SE102.369578, t.9944361 and df100.3006 replace imprecise derivative calculations. The estimator and effective subset remain unknown, so no source candidate follows. Statistical pass1's hypothetical SAS log diagnostic now rounds to.0223/week from.022307279. No source, candidate ID, classification or evidence state changed.

Coordinator post-recheck/audit clarification for RL-CAND-05 (stable C009): original conditional lane observation is provenance, superseded by the direct recheck determining record_input_error/discuss because additive plot secant/model coefficient scale and estimand alignment is unestablished. Primary/all relationship S_C; model p4 continuingp5 is supporting context and does not add S_W. PF-CAND-02's MMSE paragraph continuation on physicalp10 is now linked. Five shortened cross-reference endpoints in the merged N inventory were mechanically expanded to their correct stable aliases using numeric_id_map.tsv. No candidate/evidence state changed.
