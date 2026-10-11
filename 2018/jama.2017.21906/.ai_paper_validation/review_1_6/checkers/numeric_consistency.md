# Numeric consistency review

Scope: all100 global numeric groups in [inventory](../relationships/numeric_relationship_inventory.md), spanning all80 supplied physical pages and every mapped table/graph/definition group. All relevant count, percentage, sum, denominator, population, rounding, difference, unit, measure, reference-group, rate/count and repeated-value checks completed. Seventeen distinct local candidates follow; there is no count target. Stable C IDs, severity, evidence states and dispositions are not assigned here. Document roles are given for every compared location. Candidate provenance: fresh numeric_consistency_reviewer, current main/support maps and supplied-source/native/image checks. Statistical inference conventions remain the separate statistical lane.

Reusable images/text are locators; original PDF pages are final authority. Direct derivative engine: Poppler pdftotext25.03.0, commands `pdftotext -layout -f 6 -l 7 jama_huffman_2018_oi_170166.pdf preprocessing/numeric-main-p6-p7.txt` and `pdftotext -layout -f 17 -l 17 joi170166supp3_prod.pdf preprocessing/numeric-supp-p17.txt` with actual outputs under review_1_6/preprocessing. Figure1 and small sample demographics were additionally visually inspected in source-bound supplied/current page images. No web, new Python, clinical prescribing assessment or old candidate/report was used.

## NUM-01 — Inpatient beta-blocker interval repeated upper endpoint

- Relationship: N031/N060.
- Compared locations/roles: REPORT [main Table2 p6](../../../jama_huffman_2018_oi_170166.pdf#page=6), inpatient beta-blocker RD; REPORT same page narrative end, inpatient beta-blocker sentence.
- Printed inputs: table6.25% (95%CI4.10 to8.40); prose6.25% (95%CI4.10 to8.10), identical OR1.46 (1.29–1.65).
- Rule/calculation/tolerance: same intervention/control, outcome and cluster/time model, same two-decimal precision;8.40−8.10=.30pp, exceeding combined endpoint rounding .01pp.
- Direct observation: upper endpoints differ. Inference: transcription or separate analysis possible, not established.
- Alternatives: an undocumented different model could explain the difference; no model distinction is stated for this repeated sentence.
- Quality-control relevance: either upper limit could be copied into extracted process-effect records.
- Exact human question: Which upper confidence limit,8.40% or8.10%, belongs to this reported adjusted inpatient beta-blocker risk difference?

## NUM-02 — Discharge beta-blocker risk difference repeated point estimate

- Relationship: N044/N060.
- Compared locations/roles: REPORT [main Table2 p6](../../../jama_huffman_2018_oi_170166.pdf#page=6), discharge beta-blocker; REPORT [main p7](../../../jama_huffman_2018_oi_170166.pdf#page=7), discharge treatment prose.
- Printed inputs: tableRD6.69% (4.43–8.95); proseRD6.63% (4.43–8.95); table counts5808/8894 and6799/10178, same process in prose67%vs65%.
- Rule/calculation/tolerance: same adjusted outcome/contrast/model;6.69−6.63=.06pp >.01pp combined rounding.
- Direct observation: point estimates differ with identical CI. Inference: mechanism unknown.
- Alternatives: undocumented model/output revision; displayed crude proportions are not a reason to reconstruct adjusted RD.
- Quality-control relevance: inconsistent effect points can enter downstream extraction.
- Exact human question: Is the adjusted discharge beta-blocker risk difference6.69% or6.63%, and do the identical4.43%–8.95% limits belong to it?

## NUM-03 — Discharge beta-blocker odds ratio repeated point estimate

- Relationship: N044/N060.
- Compared locations/roles: REPORT [Table2 p6](../../../jama_huffman_2018_oi_170166.pdf#page=6); REPORT [discharge beta-blocker prose p7](../../../jama_huffman_2018_oi_170166.pdf#page=7).
- Printed inputs: tableOR1.48 (1.30–1.68); proseOR1.47 (1.30–1.68).
- Rule/calculation/tolerance: same adjusted outcome and same two-decimal precision should display the same rounded result. Difference.01 lies at the combined rounding boundary; half-open nearest-rounding bins[1.475,1.485) and[1.465,1.475) do not overlap under one consistent convention. This is a direct repeated-display discrepancy rather than proof of different unrounded estimates.
- Direct observation: printed points differ. Inference: separate rounding conventions or revision possible.
- Alternatives: tie handling applied differently at exactly1.475 or different analysis; source does not describe either.
- Quality-control relevance: exact OR extraction is ambiguous despite identical intervals.
- Exact human question: Which displayed adjusted odds ratio,1.48 or1.47, should be associated with this discharge beta-blocker result?

## NUM-04 — Door-to-balloon difference column percent versus time unit

- Relationship: N037.
- Compared locations/roles: REPORT [main Table2 p6](../../../jama_huffman_2018_oi_170166.pdf#page=6), door-to-balloon row label; REPORT same table Difference,% header and footnote b/c.
- Printed inputs: median(IQR),min;65(53–105),77(55–118); Difference,%6.18(−4.78 to17.14); beta13.00(3.64–22.36).
- Rule/calculation/tolerance: difference of marginal time measurements retains minutes unless a stated normalization/percent change is supplied. Dimensional comparison:min−min=min; the common header says%. No numerical tolerance applies to a unit label.
- Direct observation: time row shares percent difference header. Inference: the6.18 may be an intended relative change or a mislabeled native-unit difference; values alone do not determine which.
- Alternatives: percent transformation could be intended, but source footnote supplies no baseline denominator or formula for it; beta column has a separate coefficient and is not assumed identical to6.18.
- Quality-control relevance: extracted time effects need an unambiguous scale.
- Exact human question: Is6.18 a percentage change or a difference in minutes, and what calculation defines it?

## NUM-05 — Door-to-needle difference column percent versus time unit

- Relationship: N039.
- Compared locations/roles: REPORT [Table2 p6](../../../jama_huffman_2018_oi_170166.pdf#page=6), door-to-needle row; REPORT same table Difference,% header/footnotes.
- Printed inputs: median(IQR),min;44(30–67),45(27–75); Difference,% .40(−5.23 to6.03); beta5.00(−5.20 to15.20).
- Rule/calculation/tolerance: min−min=min unless normalized; no percent-change denominator/formula printed; categorical unit mismatch has no rounding tolerance.
- Direct observation: minutes row under percent difference heading. Inference: intended scale unresolved, and beta5.00 is not silently equated with.40.
- Alternatives: source may intend a separately normalized percentage; definition absent.
- Quality-control relevance: time-based effect magnitude and units cannot be copied safely without definition.
- Exact human question: Is.40 a percentage change or a difference in minutes, and how is this contrast calculated?

## NUM-06 — Table2 odds-ratio definition says difference in marginal effects

- Relationship: N048.
- Compared locations/roles: REPORT [main Table2 p6](../../../jama_huffman_2018_oi_170166.pdf#page=6), odds-ratio header/values; REPORT same page footnote b.
- Printed inputs: footnote 'Odds ratios and β-coefficients ... are calculated as the difference in marginal effects (intervention group minus control group)'; prehospital aspirin separate RD3.80% and OR1.40, inpatient beta-blocker RD6.25% and OR1.46.
- Rule/calculation/tolerance: subtraction of two probabilities is a risk difference bounded−1 to1; an odds ratio is a ratio, null1. Printed OR1.40 cannot be a raw probability difference; distinct risk-difference column values reinforce conflicting definitions. No label tolerance.
- Direct observation: footnote assigns subtraction rule to OR column. Inference: copied footnote may intend the RD column; production cause unknown.
- Alternatives: 'marginal effects' may have a different meaning but no definition of a ratio obtained by the stated intervention-minus-control subtraction is supplied. Native beta time differences can legitimately be subtraction and do not establish the OR rule.
- Quality-control relevance: readers may misidentify effect measure/model scale.
- Exact human question: Should the subtraction definition apply to risk differences rather than odds ratios, and what computation defines the OR column?

## NUM-07 — Table3 odds-ratio definition says difference in marginal effects

- Relationship: N059.
- Compared locations/roles: REPORT [main Table3 p7](../../../jama_huffman_2018_oi_170166.pdf#page=7), OR headers; REPORT same table footnote a.
- Printed inputs: 'Odds ratios ... are calculated as the difference in marginal effects (intervention group minus control group)'; MACE primaryRD−.09%,OR.98; optimal inpatient primaryRD6.00%,OR1.45.
- Rule/calculation/tolerance: probability subtraction and odds ratio have different definitions/nulls;1.45 exceeds upper bound1 for probability subtraction. Displayed RD−.0009 and OR.98 are distinct, so the footnote cannot consistently define both by the same subtraction. No unit-label rounding tolerance.
- Direct observation: definition conflicts with OR label/separate RD column. Inference: intended wording unknown.
- Alternatives: a specialized marginal-effect definition could be intended; it must be supplied, not invented. [REPORT eTable7 p23](../../../joi170166supp3_prod.pdf#page=23) separately defines OR as intervention/control effect and RD as marginal difference; it corroborates intended distinction and is not itself a discrepant comparator.
- Quality-control relevance: ambiguous effect measures can propagate to synthesis records.
- Exact human question: Does the subtraction definition in Table3 footnote a belong to the risk-difference columns, and how were the ORs computed?

## NUM-08 — Tobacco counseling described above95% despite94.7%

- Relationship: N058/N060.
- Compared locations/roles: REPORT [main p7 prose](../../../jama_huffman_2018_oi_170166.pdf#page=7), 'Rates of discharge second antiplatelet use and tobacco cessation counseling were high (>95%)'; REPORT same page Table3 tobacco cessation advice.
- Printed inputs: intervention2618(94.7%),control3526(96.0%).
- Rule/calculation/tolerance:94.7's one-decimal rounding interval[94.65,94.75) is entirely below95;95−94.7=.3pp. Thus both-group >95 description does not include the intervention counseling proportion.
- Direct observation: threshold and one reported proportion conflict. Inference: phrase may loosely generalize across the two treatments/groups.
- Alternatives: authors may mean some rates exceed95% or characterize the average; no such scope is specified. Adjusted OR does not turn the unadjusted intervention percentage into>95%.
- Quality-control relevance: numeric threshold summary can misstate uptake.
- Exact human question: Was>95% intended to describe each group's tobacco-counseling rate, or should the intervention94.7% be distinguished?

## NUM-09 — Toolkit ECG measure heading minutes versus percentage definition/display

- Relationship: N081.
- Compared locations/roles: PLAN [toolkit p9](../../../joi170166supp3_prod.pdf#page=9), measure18 heading; PLAN same page definition/percentile/monthly plots.
- Printed inputs: 'Door-to-1st ECG in minutes'; AMI patients with ECG within10minutes; percentile values99.8%,96.1%,92.0%,87.6%,71.5%; hospital scores87.6%,93.4%,94.7%,98.5%; percent axes.
- Rule/calculation/tolerance: time-to-ECG in minutes and proportion within a10-minute threshold are distinct measurements. All printed performance values are percentages, not minutes; no label tolerance.
- Direct observation: heading scale differs from defined/displayed scale. Inference: intended measure may be within-threshold proportion rather than continuous delay.
- Alternatives: short heading may name underlying timing field while the definition specifies performance proportion; human clarification still resolves reuse ambiguity. It is sample operational PLAN material, not a trial result.
- Quality-control relevance: audit metric extraction needs correct unit/type.
- Exact human question: Should measure18 be labeled percentage receiving ECG within10minutes, or are any displayed values intended to be minutes?

## NUM-10 — Toolkit three-month2014 scope versus four2011–2012 quarters

- Relationship: N081.
- Compared locations/roles: PLAN [toolkit p9](../../../joi170166supp3_prod.pdf#page=9), rolling-three-month heading; PLAN same page graph x-axis.
- Printed inputs: 'Rolling3Months (Oct2014–Dec2014)' versus2011Q3,2011Q4,2012Q1,2012Q2; four hospital-score labels87.6%,93.4%,94.7%,98.5%.
- Rule/calculation/tolerance: dates/period identities for the same graph should match. Oct–Dec2014 is three months in2014Q4; displayed four quarters run2011Q3–2012Q2 and do not intersect that period. No rounding tolerance.
- Direct observation: date scope/x-axis labels conflict. Inference: placeholder example-axis values probable but not established as correct.
- Alternatives: deliberately illustrative sample graphics from a different period, which should be identified as such; this is PLAN sample data and no trial chronology error is inferred.
- Quality-control relevance: operational audit periods could be misread when reused.
- Exact human question: Which time periods do the four plotted values represent, and is the Oct–Dec2014 rolling-three-month heading applicable to this graph?

## NUM-11 — Sample hospital gender percentages sum71%

- Relationship: N083.
- Compared locations/roles: PLAN [toolkit p10](../../../joi170166supp3_prod.pdf#page=10), Distribution of Gender male/female Hospital bars; PLAN same graph Percent of Admissions axis.
- Printed inputs: Hospital male43%,female28%, only two displayed gender categories.
- Rule/calculation/tolerance: if the displayed categories cover the admissions distribution,43+28=71%, leaving29pp; two integer percentages permit at most1pp sum-rounding error. Even maximum rounded underlying sum72% remains below100%.
- Direct observation: displayed sum71%. Inference: category coverage/denominator is unknown; no claim that all omitted admissions are assigned incorrectly.
- Alternatives: missing/unreported gender, omitted category or different bar denominators could explain deficit; none is labeled. Deliberately illustrative sample inputs may be incoherent by design but retain numeric ambiguity.
- Quality-control relevance: sample audit percentages need declared denominators/missingness.
- Exact human question: What accounts for the other29% of hospital admissions, and do male/female bars share the same denominator?

## NUM-12 — Sample all-hospital gender percentages sum85%

- Relationship: N083.
- Compared locations/roles: PLAN [toolkit p10](../../../joi170166supp3_prod.pdf#page=10), Distribution of Gender All bars; PLAN same graph Percent of Admissions axis.
- Printed inputs: All male56%,female29%, no further category shown.
- Rule/calculation/tolerance:56+29=85%, leaving15pp; maximum two-value integer rounding allowance1pp.
- Direct observation: displayed sum85%. Inference: omitted/missing category or denominator may explain it, not specified.
- Alternatives: different denominators or missing gender; illustrative example artifact. This is a separate population/printed pair from NUM-11 and not merged solely because the graph is shared.
- Quality-control relevance: comparator audit distribution cannot be interpreted as exhaustive without a definition.
- Exact human question: What accounts for the other15% of all-hospital admissions, and what denominator defines the two bars?

## NUM-13 — Prespecified age subgroup cutpoints differ from SAP

- Relationship: N062/N075.
- Compared locations/roles: PLAN [SAP p7 section7.5.2](../../../joi170166supp2_prod.pdf#page=7), a priori age '<65years and>65years'; REPORT [main p9 Figure3](../../../jama_huffman_2018_oi_170166.pdf#page=9), prespecified subgroup presentation, age<50,50–69,≥70; REPORT [main p3 subgroup methods](../../../jama_huffman_2018_oi_170166.pdf#page=3).
- Printed inputs: PLAN65cutpoint/two groups; REPORT50and70cutpoints/three groups, denominators2079/6606/2623 intervention and2045/5863/2158 control.
- Rule/calculation/tolerance: claimed prespecified age partition should match the supplied prespecification or name an amendment. Two65-based groups are not the reported three groups; e.g.age60 is PLAN<65 and REPORT50–69, age68 PLAN>65 same REPORT middle group. No numeric rounding tolerance.
- Direct observation: thresholds differ; all reported subgroup totals reconcile. Inference: updated prespecification may exist but is not supplied.
- Alternatives: undisclosed amendment or additional plan; no protocol-violation adjudication. The SAP also omits age65 boundary, but no participant count at65 is supplied, so that omission is not separately registered.
- Quality-control relevance: extracted subgroup estimates need accurate numerical partition/prespecification labels.
- Exact human question: Which prespecified plan or amendment supports the reported<50,50–69,≥70age partition rather than the supplied SAP65-year split?

## NUM-14 — SAP four crossover periods versus five-cohort schedule

- Relationship: N068.
- Compared locations/roles: PLAN [SAP p3 design/diagram](../../../joi170166supp2_prod.pdf#page=3); PLAN [SAP p4 randomization](../../../joi170166supp2_prod.pdf#page=4).
- Printed inputs: five steps/cohorts; interventions at4,8,12,16,20months; p4 'one cohort of hospitals ... in each of the four time periods'.
- Rule/calculation/tolerance: five distinct specified crossover dates imply five intervention crossover periods, not four; count5−4=1. Exact integers, zero tolerance.
- Direct observation: within-plan schedule counts conflict. Inference: four may refer only to periods after the first crossover, though sentence does not say that.
- Alternatives: initial crossover counted separately; prospective revisions. No realized participant-flow/design critique is inferred.
- Quality-control relevance: readers reconstructing the quantitative rollout need one period definition.
- Exact human question: Does 'four time periods' exclude the first crossover, or should it refer to all five scheduled intervention crossovers?

## NUM-15 — Five-percent dropout allowance gives less than15000 retained

- Relationship: N069.
- Compared locations/roles: PLAN [protocol p18 section8.2](../../../joi170166supp1_prod.pdf#page=18); PLAN [SAP p4 sample size](../../../joi170166supp2_prod.pdf#page=4). REPORT [main p3 sample-size paragraph](../../../jama_huffman_2018_oi_170166.pdf#page=3) repeats15750 and5% but does not create an independent discrepancy because it lacks15000 retention comparator.
- Printed inputs: anticipated15000 for stated power, increased15750 'to account for up to5%drop out between discharge and30-day follow-up'.
- Rule/calculation/tolerance: if15000 is required retained n, gross target must satisfy n×.95≥15000.15750×.95=14962.5;15000/.95=15789.4737, minimum integer15790. Printed15750=15000×1.05;37.5 expected retained shortfall. Exact target counts; integer retention may differ≤1, far below37.5.
- Direct observation: stated targets/inflation; inference:15000 assumed retained sample and5% assumed fraction of recruited participants. Full clustered-power formula absent.
- Alternatives: additive5% contingency convention or approximate planned target;15000 may itself be rounded or not retained requirement. No power failure or conclusion impact is asserted.
- Quality-control relevance: reproducible sample-size allowance arithmetic should distinguish additive padding from retention adjustment.
- Exact human question: Was15750 intended as approximate additive5%padding, or as the total needed to retain15000 after5%loss, and is15000 itself rounded?

## NUM-16 — Complete/missing follow-up table difference footnote names treatment arms

- Relationship: N090.
- Compared locations/roles: REPORT [supplement eTable1 p17](../../../joi170166supp3_prod.pdf#page=17), complete/missing column headers and row differences; REPORT same page footnote a.
- Printed inputs: Complete Follow Up n21079, Missing Follow Up n295; age60.6vs60.0,difference−.6; male75.8vs71.2,difference−4.6; footnote 'Difference=intervention minus control'.
- Rule/calculation/tolerance: displayed differences track missing−complete:60.0−60.6=−.6;71.2−75.8=−4.6pp. Neither column is labeled intervention or control. Reference-group identity has no rounding tolerance; values match missing−complete under normal display allowance.
- Direct observation: treatment-arm footnote inconsistent with actual column identities. Inference: copied contrast footnote likely, cause not known.
- Alternatives: unseen treatment-stratified contrast would not correspond to the displayed two follow-up populations; no such model is described.
- Quality-control relevance: column/reference identity can be mis-extracted despite coherent arithmetic.
- Exact human question: Should the eTable1 difference definition read missing-follow-up minus complete-follow-up rather than intervention minus control?

## NUM-17 — Flow lost-follow-up count275 versus incomplete outcome count295

- Relationship: N005.
- Compared locations/roles: REPORT [main Figure1 p4](../../../jama_huffman_2018_oi_170166.pdf#page=4), all20lost-follow-up boxes and caption; REPORT [main p6](../../../jama_huffman_2018_oi_170166.pdf#page=6),295incomplete outcomes=215not followed by enrolling site+80unreachable; REPORT [supplement eTable1 p17](../../../joi170166supp3_prod.pdf#page=17),missing follow-up n295. Supplement corroborates295; primary discrepancy is within main report.
- Printed inputs: control step0–4 lost42,45,54,27,2. Intervention cohort1steps1–5:2,6,0,3,10; cohort2steps2–5:18,4,6,8; cohort3steps3–5:10,8,7; cohort4steps4–5:7,7; cohort5step5:9. Caption includes those not reached after3attempts and those for whom site did not perform follow-up; lost participants included in analysis.
- Rule/calculation/tolerance: exhaustive disjoint cohort/step boxes cover the same analyzed21374participants. Control sum170; intervention sum105; total275. Narrative295−275=20. Integer tolerance0. Figure-derived completed count21374−275=21099, versus narrative/supplement21079. Percentage99%rounding hides the count difference and does not repair it.
- Direct observation: exact printed box sum differs from narrative/supplement; figure caption explicitly includes both named missing-follow-up mechanisms. Inference:20additional partially missing outcomes or a box transcription could explain it; no cause assigned.
- Alternatives: narrative 'incomplete outcome data' might encompass additional incomplete records outside Figure1lost category, but eTable1labels all295 'Missing Follow Up'; necessary distinction is not supplied. No lost patients are subtracted from analyzed totals; all enrollment/exclusion totals independently reconcile.
- Quality-control relevance: follow-up/missingness denominator extraction changes by20patients.
- Exact human question: Are Figure1's275lost-follow-up patients the same population as the295incomplete/missing-follow-up patients; if not, which20additional patients or missingness categories explain the difference?

## Completed checks without additional candidates and limitations

All27Table1 rows,21Table2 rows,10Table3 rows,14Figure3 subgroup rows,20flow boxes,all60Figure2cohort/step points and repeated denominator panels were covered. All7supplement result tables and every printed cell/footnote in their current annex were checked; all4results figures and14scanned toolkit pages remain source-linked and visually mapped. For eTable3/4, each categorical count/percentage and each step/arm/global sum reconciles; all continuous values/dispersion ordering and units were checked, with variable-specific missing n preventing exact pooled mean/SD proofs. Medians/SDs are never summed. Adjusted RD signs differing from crude rates are not arithmetic candidates. Process/medication denominators differ by eligibility/discharge/contraindication as explicitly stated; missing exact subset n alone is not a candidate.

Corrected current-map locator: DOC-004 p10 All age55–64source label is28%, not23%; the source-bound demographic crop shows28%. Age totals Hospital98%,All101% both fit seven integer categories'3.5pp rounding allowance, so no age-sum candidate. Unknown source category completeness is retained as an alternative for both gender candidates. Seven sample performance panels reuse same percentiles/scores; no supplied rule requires them to differ, so duplication alone is not a candidate. Their four plotted green points have only three explicit monthly numeric labels: do not misassign unlabeled fourth point to December or assert94.7versus98%contradiction. Clinical drug/dose correctness and external laboratory unit knowledge are outside supplied-source consistency scope.

No displayed-zero P candidate. No exact person-time denominator is printed; percent 'rates' consistently indicate proportions. Exact unlabeled plot rates/CI endpoints, complete per-variable n and undisclosed analysis revisions remain limitations, not scientific coverage gaps. All candidates are quality-control questions pending human adjudication; no claim that conclusions are wrong is made.
