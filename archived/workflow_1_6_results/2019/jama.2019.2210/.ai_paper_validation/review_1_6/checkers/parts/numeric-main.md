# Numeric consistency review — main shard

Runtime UUID: 01a12868-d20d-7603-b09d-5a1375e78ae9. Model/effort: gpt-6.1-sol/medium, fresh numeric-reviewer spawn, current authorized provider. Assigned scope: DOC-001 M001–M120, physical PDF pages 1–7, REPORT. N001–N120 contain all printed components and repetitions; 120 relationships checked, six distinct candidates emitted. M121–M134 and support documents are assigned to the independent numeric support shard. No stable candidate IDs or adjudications are assigned here.

Read completely: QUALITY_CONTROL_SCOPE.md, workflow_1_6/review_contract.md, extraction/main_quantitative_evidence.md. Scope is exact quantitative-reporting consistency; participant timing qualifies below because it conflicts with a reported IQR. All sources and reused derivatives preserved. Source-linked reusable native/layout locators for pp.1–7 inspected; reusable images pp.5,7 visually inspected; fresh direct-source Poppler pdftotext layout pp.2,4,5,7 stored in preprocessing/numeric-main-p2.txt, numeric-main-p4.txt, numeric-main-p5.txt and numeric-main-p7.txt. No OCR needed. No old candidate or report conclusions, external evidence, web or extra Python used.

## Completed checks and noncandidate relationships

Every N row in relationships/numeric_relationship_inventory.md records its printed inputs, location and applied check result. All arithmetic, count bounds, mutually exclusive category totals, percentage precision, missingness, measured versus randomized population identity, reference-group/direction, measures, units, rates versus risk/count distinctions, repeated values, interval containment and printed risk-array components were checked. Integer percentages use 0.5 percentage-point tolerance; one-decimal percentages use 0.05; exact count/identity comparisons have zero tolerance. The six candidates below are the complete emissions, with no count-based stopping.

All efficacy count percentages reconcile, as do death partitions. All subgroup and pooled risk arrays have correct baseline identity, nonnegative nonincreasing counts, nonnegative subgroup residuals and ordered corresponding endpoint populations. At-risk counts are not event counts. Five-year survival percentages are censoring-dependent estimates and need not equal crude fractions. Change ratios of paired participant values need not equal ratios of aggregate medians, so 87% versus (41−21)/21 is not a candidate. A mean age66 and median age66 can coexist; no age-summary mismatch inferred. BMI totals249/165 are below randomized251/166; missingness without a concrete percentage mismatch is not alone a candidate. Genotype percentages use measured category totals; applying randomized totals wholesale would manufacture discrepancies. Rounded category percentages need not sum to100%, as the source footnote states. No display-zero P value appears. Inferential interval/P-value calculations requiring unprinted model/test conventions are reserved to the independent statistical lane; CI order, containment and narrative direction were checked here.

## Candidate NM-01 — vitamin D middle-baseline percentage

Relationship: N051,N052,N053,N022. Proposed primary category: Denominator, proportion, or total inconsistency.

Compared locations and document roles: REPORT [main article p.5 Table1 baseline25(OH)D rows](../../../../jama_urashima_2019_oi_190023.pdf#page=5), with REPORT [p.4 baseline subgroup totals](../../../../jama_urashima_2019_oi_190023.pdf#page=4) and REPORT [p.6 missing baseline statement](../../../../jama_urashima_2019_oi_190023.pdf#page=6). The discrepancy is internal to one REPORT.

Printed inputs: vitamin D low102(41), middle142(58), high4(1.6); randomized D251. Placebo71(44),90(56),1(0.6); total randomized417; seven missing baseline levels; pooled measured groups173,232,5.

Reproducible rule/calculation: mutually exclusive low/middle/high measured categories total102+142+4=248. 100×142/248=57.2580645%, differing from58% by0.7419355 percentage point, beyond integer-rounding tolerance0.5. Randomized denominator251 yields56.5737%, also not58%. All displayed category counts total410 and seven missing reconcile417. This registers the individual142(58) cell, not the rounded percentage-column sum.

Direct observation: source prints142(58) and exhaustive category counts. Derived inference: 248 is the category-based measured denominator, not an explicitly printed arm-specific denominator. No claim is made about cause. Alternatives: a different percentage-specific denominator, a count transcription, or a nonstandard rounding rule might explain the cell; excluding high produces244 and58.1967% for middle, but would yield41.8033% for low rather than printed41%, so it does not give one coherent denominator for the low/middle pair.

Quality-control relevance: the inconsistent count/percentage can be propagated when extracting baseline subgroup composition. Exact human question: What denominator and rounding rule were used for the vitamin D middle25(OH)D cell, and should its count or displayed percentage be reconciled with the complete baseline category totals?

## Candidate NM-02 — placebo ApaI GT percentage

Relationship: N064,N065,N066. Proposed primary category: Denominator, proportion, or total inconsistency.

Compared locations and document roles: REPORT [main article p.5 Table1 continued, ApaI GG/GT/TT placebo cells and rounding footnote](../../../../jama_urashima_2019_oi_190023.pdf#page=5). All compared content is REPORT in the same document.

Printed inputs: placebo ApaI GG69(46), GT61(40), TT20(13); header placebo n166. Vitamin D corresponding counts96,104,31 are not substituted for placebo.

Reproducible rule/calculation: 69+61+20=150 measured genotype counts;100×61/150=40.6666667%, differing from40% by0.6666667 percentage point, beyond0.5 tolerance. The other placebo cells69/150=46.0% and20/150=13.3333% reconcile46 and13. Randomized166 gives36.7470%, not40%. A percentage total99% alone would be allowed; this observation concerns the individual61(40) pair.

Direct observation: all counts/percentages printed as above, confirmed by direct layout text and visual locator. Derived inference:150 is the measured-category denominator. Alternatives: genotype-specific percentage denominators, truncation rather than nearest rounding, or a count/percentage transcription. Uniform truncation does not explain all genotype percentages, but rounding details are not assumed conclusively.

Quality-control relevance: a mislabeled genotype frequency could enter subgroup summaries or systematic evidence extraction. Exact human question: Does placebo ApaI GT use the common measured denominator150, and what source count, denominator or rounding rule accounts for the printed40%?

## Candidate NM-03 — Table2 hazard-ratio direction footnote

Relationship: N104 with N086,N094,N009. Proposed primary category: Measure, label, or scale inconsistency.

Compared locations and document roles: REPORT [main article p.7 Table2 footnotea and relapse row](../../../../jama_urashima_2019_oi_190023.pdf#page=7); REPORT [p.6 competing-risk result narrative](../../../../jama_urashima_2019_oi_190023.pdf#page=6); REPORT [p.3 statistical model and treatment description](../../../../jama_urashima_2019_oi_190023.pdf#page=3). All are one REPORT.

Printed inputs: Table2 footnote says “Hazard ratio (HR) values greater than 1 indicate that vitamin D supplementation was associated with a decreased probability of the outcome.” Relapse rows include total subdistributionHR0.75(0.48–1.17) and middle0.44(0.21–0.89). P.6 says middle cumulative incidence is significantly lower in vitamin D than placebo with0.44. Main results consistently describe vitamin D compared with placebo.

Reproducible rule/calculation: for the stated vitamin-D-versus-placebo event-hazard contrast, ratio above1 is larger vitamin D event hazard and ratio below1 is smaller. The source itself pairs0.44<1 with lower outcome incidence, while the universal footnote pairs>1 with decreased probability. Ratio direction is an exact label/contrast comparison with zero numerical tolerance; probability and hazard are not equated numerically.

Direct observation: conflicting sign wording and printed effect/narrative. Derived inference: applying the article's treatment contrast to the universal footnote. Alternatives: the footnote might intend an inverse reference contrast or a complementary favorable endpoint, but neither is named and the table endpoints are relapse and death.

Quality-control relevance: the direction label could reverse interpretation during evidence reuse even though results narratives give the intended direction. Exact human question: What treatment reference group and outcome direction does footnotea intend, and how should the greater-than1 statement be reconciled with the reported lower relapse incidence atHR0.44?

## Candidate NM-04 — Figure3C risk-table presence versus caption

Relationship: N114,N116. Proposed primary category: Numeric or arithmetic inconsistency.

Compared locations and document roles: REPORT [main article p.7 Figure3 panelC and its caption](../../../../jama_urashima_2019_oi_190023.pdf#page=7); same REPORT.

Printed inputs: panelC “Death, baseline25(OH)D level20–40ng/mL” has “No. at risk” placebo90,88,70,51,34,22,11 and vitaminD142,139,115,88,61,41,20 at years0–6. Caption says “Numbers at risk for panel C are not given because of weighting.”

Reproducible rule/calculation: caption claims an absent table while directly displayed panelC has two rows of seven numeric risk counts. Presence/identity comparison uses zero tolerance; no values are digitized from curves or converted from weights.

Direct observation: labeled panelC contains the printed risk rows, and caption states none given. No unreported weighting method is inferred. Alternatives: the caption could name the wrong panel, or rows may be unweighted counts while a distinct weighted risk quantity was intended; the caption does not distinguish those quantities.

Quality-control relevance: a reader extracting cohort risk counts or interpreting weighted displays faces conflicting guidance about the displayed numbers. Exact human question: Does the caption refer to this panelC and these risk rows, and are the displayed counts the intended numbers at risk or a different unweighted quantity?

## Candidate NM-05 — pooled stageII narrative percentage

Relationship: N020,N046 with N045,N047. Proposed primary category: Denominator, proportion, or total inconsistency.

Compared locations and document roles: REPORT [main article p.4 Study Population stage distribution and n417](../../../../jama_urashima_2019_oi_190023.pdf#page=4); REPORT [p.5 Table1 cancer-stage counts](../../../../jama_urashima_2019_oi_190023.pdf#page=5). Same REPORT.

Printed inputs: body states “Disease stages were I, II, and III in44%,26%, and30% of patients, respectively.” Table1 stageII vitaminD63 and placebo48; stageI115/67, stageIII73/51, arm totals251/166.

Reproducible rule/calculation: all stage counts sum251+166=417. Pooled stageII63+48=111;100×111/417=26.6187050%. Difference from26% is0.6187050 percentage point, beyond integer rounding tolerance0.5. StagesI182/417=43.6451% andIII124/417=29.7362% round44 and30. An unweighted average of arm percentages(25+29)/2=27% also does not yield26%.

Direct observation: printed stage counts and pooled percentage. Derived inference: the statement's denominator is all417 described in the same population paragraph, supported by exhaustive stage table sums. Alternatives: a different stage definition or population, a count transcription, or truncation for this percentage. Uniform truncation would not reproduce44%/30% for the other stages.

Quality-control relevance: pooled stage mix can be copied into baseline comparability or evidence tables. Exact human question: Are the narrative stageII percentage and Table1 stageII counts based on the same417 participants, and what denominator or rounding rule reconciles26% with111 participants?

## Candidate NM-06 — postoperative randomization window versus reported IQR

Relationship: N003,N019. Proposed primary category: Numeric or arithmetic inconsistency.

Compared locations and document roles: REPORT [main article p.2 Trial Design statement](../../../../jama_urashima_2019_oi_190023.pdf#page=2); REPORT [p.4 Study Population postoperative randomization timing](../../../../jama_urashima_2019_oi_190023.pdf#page=4). Same REPORT. This is a concrete timing-summary inconsistency rather than a general participant-flow/design criticism.

Printed inputs: p.2 says “in this study, patients who did not meet exclusion criteria were randomized and started supplementation at the first outpatient visit between2 and4 weeks after operation.” P.4 says participants randomized and started medication at median23.5(IQR13–44)days after operation.

Reproducible rule/calculation:2–4weeks=14–28days. If the p.2 statement is the realized inclusion window, every observed timing, hence its lower/upper quartile, must be within[14,28]. Printed quartiles13 and44 lie outside: lower1day earlier, upper16days later. Even interpreting integer IQR bounds with±0.5day display tolerance does not put44 inside28. Week wording may be approximate; this is preserved as the human question.

Direct observation: fixed-seeming trial timing statement and actual IQR. Derived inference: converting weeks using7days/week and applying the bounded-observation property of quantiles. Alternatives: p.2 may summarize intended/usual scheduling rather than a strict observed window; allowed clinical deviations could explain timings without contradicting the actual IQR. No adherence, eligibility or protocol-violation judgment is made.

Quality-control relevance: timing windows and timing dispersion can be reused in trial summaries and population comparisons; the apparent realized-window statement can misdescribe the reported distribution. Exact human question: Does “between2 and4weeks” describe a strict realized randomization range or intended/usual scheduling, and what wording or numeric definition reconciles it with IQR13–44days?

## Limitations and completion

No missing scientific unit within assigned M001–M120. Denominators for some measured subsets, exact change-ratio summary definition and full statistical covariance/test conventions are not printed in assigned pages; absent definitions alone generated no candidate. All six candidates retain source-grounded alternatives and exact unresolved questions. Fresh complete direct-source recheck is mandatory before coordinator classification/report assembly. Candidate count6; relationship count120. All remain Pending Human Adjudication.

