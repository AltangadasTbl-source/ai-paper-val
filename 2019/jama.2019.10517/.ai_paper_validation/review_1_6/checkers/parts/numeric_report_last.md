# Numeric consistency checker: late main report and complete results figures

Fresh runtime UUID: 01a1286a-814f-7b12-a00b-e90ab6064dbe. Model gpt-6.1-sol, medium. Origin scope DOC-001 pp7–10 and DOC-003 pp1–10; earlier main locations comparators only. Ownership restricted to this checker and relationships/parts/numeric_report_last.md. Complete assigned scope reviewed: 83 local quantitative relationships, 5 distinct local candidates, 14/14 pages, 9/9 support figures, no scientific coverage gap. All compared locations below are REPORT by content. No stable C IDs, adjudications, severity or dispositions are assigned.

Inputs were current full main/support maps and source-grounded model definitions, source-linked native assets, all nine reusable figure images, main Tables4/5 images, and direct Poppler source text for pp7–10 and methods comparator p5. Source files and all reused assets preserved. No old candidate/report conclusions, web, outside literature, Python extraction, OCR or GPU used. Native blanks in Table4 preserved. A complete row-by-row arithmetic/numeric inventory is in [the assigned relationship shard](../../relationships/parts/numeric_report_last.md). Source links resolve four directories above this checker.

## RL-CAND-01 — Placebo relapse hospitalization percentage does not round to the printed value

**Relationship:** RL009; comparator RL006. Primary category proposed: Denominator, proportion, or total inconsistency.

**Compared locations and roles:** [DOC-001 p8, opening tolerability continuation, REPORT](../../../../jama_flint_2019_oi_190079.pdf#page=8); [DOC-001 p7 Table3 psychiatric hospitalization, REPORT](../../../../jama_flint_2019_oi_190079.pdf#page=7). The discrepancy is within the main REPORT document; the Table3 count corroborates numerator11.

**Printed inputs:** p8: “11 (32.3%) of 34 in the placebo group required psychiatric hospitalization because of the relapse.” Table3 placebo hospitalization11. Adjacent olanzapine statement6(46.2%) of13.

**Rule and calculation:** A printed one-decimal percent for11/34 under nearest rounding equals100×11/34=32.352941176%, hence32.4%. A32.3% display under nearest rounding represents[32.25%,32.35%); the exact count ratio lies0.002941 percentage point above its upper rounding boundary. Equivalently the displayed deviation is0.052941 percentage point, exceeding half-unit tolerance0.05. Adjacent6/13=46.153846% correctly yields46.2%.

**Direct observation versus inference:** Source text and rendered p8 directly print11,34,32.3%; only division and nearest-rounding inference are derived. No participant-level reconstruction is required.

**Alternatives:** Truncating rather than rounding11/34 yields32.3%, but neighboring6/13 and other article percentages use nearest rounding; a deliberate alternate display convention must be clarified. An unprinted differing numerator/denominator cannot be substituted for the sentence's explicit11 of34.

**Quality-control relevance:** A small participant-proportion mismatch can be copied into adverse-event or hospitalization extraction. No paper-conclusion effect is asserted.

**Exact human question:** Was32.3% obtained by a documented truncation convention, or should the displayed percentage for the explicit11/34 hospitalization count be reconciled with ordinary one-decimal rounding?

## RL-CAND-02 — Total cholesterol unadjusted absolute risk difference does not reconcile with its arm counts

**Relationship:** RL054 (Table5 total difference; coordinator may rebase local relationship numbering from inventory). Primary category proposed: Denominator, proportion, or total inconsistency.

**Compared locations and roles:** [DOC-001 p9 Table5, total cholesterol row and O64/P62 column headers, REPORT](../../../../jama_flint_2019_oi_190079.pdf#page=9). All three cells and headers belong to one REPORT document.

**Printed inputs:** O9(14.1%), n64; P6(9.7%), n62; “Absolute Unadjusted Difference Between Groups, % (95% CI)”4.3(−8 to17.2). Threshold above both baseline and240mg/dL.

**Rule and calculation:** Signed O-minus-P unadjusted risk difference in percentage points=100×(9/64−6/62)=14.0625−9.677419355=4.385080645. Nearest0.1 gives4.4;4.3±0.05 spans[4.25,4.35], excluding4.385080645. The discrepancy from display4.3 is0.085080645 percentage point. Even subtraction of the printed arm percentages yields14.1−9.7=4.4. No hypothesis-test reconstruction or CI-symmetry assumption is needed. Printed arm percentages themselves round correctly.

**Direct observation versus inference:** Values/headers are directly printed and visually inspected; difference calculation is derived from explicit arm counts and denominators.

**Alternatives:** A different complete-case denominator or model-derived estimate could change the difference, but no differing denominator is named and the column explicitly says unadjusted. A truncation convention would produce4.3 but is not stated and differs from nearest rounding of arm proportions. ExactCI footnote b is attached only to triglyceride/glucose, so no unsupported method for this CI is assumed.

**Quality-control relevance:** This independently labeled metabolic incidence difference may be reused as a risk difference in a downstream evidence table. The issue is the small point-estimate arithmetic mismatch, not inferred clinical impact.

**Exact human question:** Which denominators and rounding rule generated the total-cholesterol difference4.3 percentage points, and do they agree with the table's explicit9/64 and6/62 counts and “unadjusted” label?

## RL-CAND-03 — LDL unadjusted absolute risk difference does not reconcile with its arm counts

**Relationship:** RL055 (Table5 LDL difference; coordinator may rebase local relationship numbering from inventory). Primary category proposed: Denominator, proportion, or total inconsistency.

**Compared locations and roles:** [DOC-001 p9 Table5, LDL row and O64/P62 column headers, REPORT](../../../../jama_flint_2019_oi_190079.pdf#page=9). Same REPORT document; this is a separately labeled LDL result.

**Printed inputs:** O9(14.1%), n64; P6(9.7%), n62; absolute unadjusted difference4.3(−8 to17.2); LDL qualifying value above both baseline and160mg/dL.

**Rule and calculation:** 100×(9/64−6/62)=4.385080645 percentage points, nearest0.1=4.4, outside the4.3±0.05 rounding interval. Displayed percentages14.1−9.7=4.4. Exact counts have zero input tolerance. CI contains the estimate and zero; no unsupported exact/normal convention is inferred.

**Direct observation versus inference:** Explicit LDL cells and denominators directly observed; arithmetic derived. The identical total-cholesterol row is a separate reported outcome, not evidence that the outcomes' participant identities are equal.

**Alternatives:** Different unprinted denominator or truncation rule could explain production, but neither is identified in the table. Identical counts across LDL/total cholesterol are plausible and are not themselves treated as duplicate-data evidence.

**Quality-control relevance:** LDL incidence is separately extractable and can transmit its own point-estimate discrepancy. Shared printed arithmetic with total cholesterol does not collapse the different outcome/comparator relationship.

**Exact human question:** Which denominators and rounding rule generated the LDL difference4.3 percentage points, and do they agree with the LDL row's9/64 and6/62 counts and the unadjusted-difference label?

## RL-CAND-04 — HbA1c trajectory coefficient is labeled mg/dL while the reported outcome uses percent

**Relationship:** RL028; DOC-003 eFigure8, Table4 HbA1c rows as comparators. Primary category proposed: Measure, label, or scale inconsistency.

**Compared locations and roles:** [DOC-001 p7 Secondary Outcomes, HbA1c coefficient, REPORT](../../../../jama_flint_2019_oi_190079.pdf#page=7); [DOC-001 p8 Table4 HbA1c row, REPORT](../../../../jama_flint_2019_oi_190079.pdf#page=8); [DOC-003 p9 eFigure8 axis, REPORT](../../../../joi190079supp2_prod.pdf#page=9); [DOC-001 p1 abstract repeated HbA1c result, REPORT](../../../../jama_flint_2019_oi_190079.pdf#page=1), comparator only. Within-main unit mismatch and main-versus-results-supplement unit mismatch are substantive comparisons.

**Printed inputs:** Main p7 daily treatment×linear-time coefficient for HbA1c:−0.0002mg/dL,95%CI−0.0021 to0.0016,adjustedP=.99; abstract repeats the same mg/dL labels. Table4 outcome “HbA1c, %,” baseline means5.9 in each arm, termination5.7 O/5.9 P. Supplement axis “HbA1c (%)”, ticks5.6/5.8/6.0/6.2, Day axis.

**Rule and calculation:** A linear coefficient for an outcome measured in percent has percentage-point/day scale unless a transformation/conversion is supplied; mg/dL denotes a different measurement unit. Numerically the plotted approximate slope contrast[(5.71−5.90)−(5.76−5.89)]/252≈−0.000238 percentage point/day, compatible with coefficient−0.0002 at its coarse precision. This graphic is corroborative only; the exact printed dimensional disagreement requires no extraction of coordinates. Unit-label tolerance is zero. Plot readings are approximate±0.015 percentage point per endpoint.

**Direct observation versus inference:** mg/dL in narrative and% in Table4/figure are exact labels. Inferred dimensional rule and graphical slope illustrate rather than replace the printed comparison. Estimate/CI order is coherent and not a separate candidate.

**Alternatives:** A model using a separately converted concentration outcome could justify mg/dL, but the supplied report does not identify such a conversion and the stated trajectory figure uses%. An intended use of “percent” for the daily effect is a possible explanation, not a prescribed correction.

**Quality-control relevance:** Unit confusion affects effect extraction and interpretation of the very small trajectory coefficient; no claim about a statistically significant glycemic effect is made.

**Exact human question:** Was the HbA1c mixed model fit on the percentage scale shown in Table4/eFigure8, or on a documented concentration scale; what unit should accompany the displayed daily coefficient and interval?

## RL-CAND-05 — Simpson–Angus weekly effect labeled score points matches the plotted log-scale contrast more closely

**Relationship:** RL034; DOC-003 eFigure9. Primary category proposed: Measure, label, or scale inconsistency.

**Compared locations and roles:** [DOC-001 p7 Extrapyramidal Measures, REPORT](../../../../jama_flint_2019_oi_190079.pdf#page=7); [DOC-001 p4 Statistical Analysis, Poisson mixed model, REPORT](../../../../jama_flint_2019_oi_190079.pdf#page=4), continuing on [p5](../../../../jama_flint_2019_oi_190079.pdf#page=5), model-definition comparator; [DOC-003 p10 eFigure9 title and Week/SAS Total Score axes, REPORT](../../../../joi190079supp2_prod.pdf#page=10). Within-main coefficient/model interpretation question and main-to-results-figure scale comparison; all REPORT.

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


Coordinator post-recheck/audit clarification for RL-CAND-05 (stable C009): the original conditional lane observation is preserved for provenance. Fresh exact-source recheck supersedes its numerical interpretation with record_input_error/discuss because the additive plotted secant and model coefficient lack an established scale/estimand alignment. The primary/all relationship is S_C; the main model definition begins p4 and continuesp5 and is supporting context, without an independent S_W discrepancy. Every stable ID remains Pending Human Adjudication.
