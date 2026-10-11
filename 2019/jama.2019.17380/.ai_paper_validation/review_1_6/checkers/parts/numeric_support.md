# Supporting Numeric Consistency Checker

Assigned bounded shard: N201-N320 (120 relationships), DOC-002 PLAN pp.1-33; DOC-003 REPORT laboratory appendix pp.2-4 and all numeric fields of eTables1-9 pp.6-14. Complete relationship inventory: [numeric_support_inventory.md](../../relationships/parts/numeric_support_inventory.md). Exact reusable transcription locator: [support map](../../extraction/support_quantitative_evidence.md). Direct sources retain precedence. No candidate cap. Twelve distinct local candidate records follow; no stable C IDs or adjudications assigned.

The source document roles are by content: all historical figures inside the protocol are PLAN; laboratory methods and results eTables in the non-plan supplement are REPORT. Every discrepancy in this shard is internal to one document. Source-matched renders visually confirmed protocol pp.9,17,18,19,33 and results pp.7,12; fresh direct Poppler layout extraction confirmed protocol pp.15,21. Other mapped rows were checked from complete source-matched layout text. Missing exact denominators, model outputs and graph coordinates are named below and in the relationship inventory. No web or old review conclusions used.

## NUM-U01 — Inconsistent mass equivalence for the same vitamin D dose

- Relationship: N212. Primary category: Measure, label, or scale inconsistency.
- Compared locations and roles: PLAN [DOC-002 p15 V.e.1](../../../../joi190122supp1_prod.pdf#page=15), study pill “2000 IU (40 µg)”; PLAN [DOC-002 p21 VII.a](../../../../joi190122supp1_prod.pdf#page=21), study “2000 IU (40 µg)” and UL “50 µg, or 2000 IU”.
- Printed inputs: 2000 IU corresponds to 40 µg in two study-dose locations but to 50 µg in the same safety section's UL equivalence.
- Rule/calculation: identical vitamin D3 IU values should have a single mass equivalent. Source-implied factors are 2000/40=50 IU/µg versus 2000/50=40 IU/µg. Mass equivalents differ by 10 µg, or 25% relative to 40 µg. No external conversion rule imported.
- Tolerance: exact same 2000-IU identity; ordinary integer rounding cannot explain a 10-µg difference.
- Direct observation: the two incompatible equivalences are printed. Diagnostic inference: at least one dose/mass pair may be a transcription problem; the package does not identify which.
- Alternatives/missing definition: different institutional limits could differ, but do not give the same chemical IU value a different mass equivalent. The intended institutional limit and intended mass for the study dose require confirmation.
- QC relevance: conflicting unit equivalents can be copied into dose extraction or plan summaries. No outcome or clinical-safety conclusion is inferred.
- Exact human question: What are the intended IU and µg values for the study dose and each printed UL, and why is 2000 IU paired with both 40 and 50 µg?

## NUM-U02 — Selected dose described as lower than an equal printed UL

- Relationship: N213. Primary category: Numeric or arithmetic inconsistency.
- Compared locations and roles: PLAN [DOC-002 p21 VII.a, first and second dose paragraphs](../../../../joi190122supp1_prod.pdf#page=21): “2000 IU” selected dose; “selected dose is lower than” the UL “50 µg, or 2000 IU”.
- Rule/calculation: compare printed IU values using the paragraph's strict inequality. 2000−2000=0, so selected dose is equal to the stated IU UL, rather than lower.
- Tolerance: exact equal integer values; no arithmetic rounding is needed.
- Direct observation: dose, UL and “lower than” comparison are printed in one section. This inequality candidate is independent of NUM-U01's mass-equivalence issue.
- Alternatives/missing definition: the comparison could have been intended in the mass units (40<50) rather than using the stated IU equivalent, or one UL value might be intended differently. This cannot be selected without human clarification.
- QC relevance: the plan's quantitative dose-to-limit interpretation is internally inconsistent as written; no assessment of actual contemporary intake limits is made.
- Exact human question: Is “lower than” intended to compare 40 with 50 µg, or should the dose/UL in IU or the comparison wording be different?

## NUM-U03 — Percent-change label applied to a fractional-change formula

- Relationship: N218. Primary category: Measure, label, or scale inconsistency.
- Compared locations and roles: PLAN [DOC-002 p17 VI.b](../../../../joi190122supp1_prod.pdf#page=17), “Percent change” and formula [(ACR4−ACR0)/ACR0]; PLAN same page VI.c, albuminuria progression “100% increase”.
- Rule/calculation: the displayed quotient is fractional change; percentage change is 100 times that quotient. For the source's own 100%-increase condition ACR4=2×ACR0, the displayed formula returns 1, while a percent-number display would return 100.
- Tolerance: factor100 scale identity; no measured ACR values or sampling assumptions required.
- Direct observation: “Percent change” is attached to a quotient without ×100. Diagnostic: implementation might still scale for a percentage display; no implementation output is supplied.
- Alternatives/missing definition: storing a fraction and formatting as percent is conventional and would reconcile the label operationally. No percent-formatting convention or downstream display rule is stated here.
- QC relevance: distinguishes fractional and percent-number quantities when reproducing plan formulas; does not establish an error in the trial result analysis.
- Exact human question: Was the quotient intended as fractional change formatted as a percentage, or was a ×100 operation omitted from the displayed formula?

## NUM-U04 — Same eGFR change called dichotomous and continuous

- Relationship: N219. Primary category: Measure, label, or scale inconsistency.
- Compared locations and roles: PLAN [DOC-002 p17 VI.c first sentence and later formula](../../../../joi190122supp1_prod.pdf#page=17), “secondary dichotomous outcome” for eGFR change, “analyzed as a continuous variable”, and [eGFR4−eGFR0]; PLAN [p18 VI.e Equation4](../../../../joi190122supp1_prod.pdf#page=18), continuous eGFR ANCOVA.
- Rule/calculation: an unrestricted numerical difference on the stated eGFR scale is continuous; a dichotomous outcome requires a two-category/threshold definition. The first sentence labels the same quantity both ways.
- Tolerance: categorical identity rule, not rounding.
- Direct observation: the contrary labels appear in the same sentence; the change formula and analysis reinforce the continuous side.
- Alternatives/missing definition: “dichotomous” may refer to the additional composite later in VI.c, but the first sentence explicitly attaches it to eGFR change. No threshold for that first outcome is printed.
- QC relevance: a quantitative outcome-scale label can affect data extraction and interpretation of the planned model; no broad design judgment made.
- Exact human question: Should the eGFR difference in the first sentence be labelled continuous, or was a separate dichotomous eGFR outcome intended there?

## NUM-U05 — Same eGFR threshold uses different surface-area normalization

- Relationship: N220. Primary category: Measure, label, or scale inconsistency.
- Compared locations and roles: PLAN [DOC-002 p5 I.a.1](../../../../joi190122supp1_prod.pdf#page=5), abnormal eGFR <60 mL/min/1.73 m²; PLAN [p19 VI.f](../../../../joi190122supp1_prod.pdf#page=19), subgroup <60 mL/min/m²; PLAN [p33 15f](../../../../joi190122supp1_prod.pdf#page=33), same <60 mL/min/m², while its power caption and narrative use mL/min/1.73 m².
- Printed inputs/rule: same numeric <60 threshold is given per1.73 m² and per1 m². Expressing 60 mL/min per1.73 m² per1 m² gives 60/1.73≈34.68; 60 per1 m² corresponds to 103.8 per1.73 m².
- Tolerance: displayed normalization factor1.73 is explicit; integer threshold rounding cannot make 60 and34.68 equal.
- Direct observation: missing1.73 normalization in both subgroup definitions. Diagnostic inference: typographic shorthand is plausible; no participant reclassification is inferred.
- Alternatives/missing definition: authors may intend the normalized eGFR convention throughout and use abbreviated unit notation. Actual subgroup coding is not supplied.
- QC relevance: a numeric threshold/unit can be extracted literally and misapplied in a reproduced subgroup definition.
- Exact human question: Do both <60 subgroup definitions mean mL/min/1.73 m², and which normalized threshold was used in subgroup coding?

## NUM-U06 — Historical diabetes-trial figure sample counts do not sum to narrative total

- Relationship: N209. Primary category: Denominator, proportion, or total inconsistency.
- Compared locations and roles: PLAN [DOC-002 p9 I.c.5](../../../../joi190122supp1_prod.pdf#page=9), seven diabetes trials “222 participants”; PLAN same page Figure7, study-name parenthetical counts15,17,18,24,21,22,12 for seven diabetes studies.
- Rule/calculation: if the parenthetical counts describe the participants in those seven trial rows, sum=15+17+18+24+21+22+12=129, differing from222 by93.
- Tolerance: integer counts exact.
- Direct observation: seven figure rows and narrative count are printed together and reference the same diabetes meta-analysis. Conditional diagnostic: parenthetical numbers lack an explicit denominator definition; the sum mismatch is conditional on their being total trial participants.
- Alternatives/missing definition: figure counts might be one arm, complete cases, matched pairs or another analysis subset while222 is randomized total; the supplied figure does not say. No external source is fetched to decide.
- QC relevance: historical sample-size extraction inside plan material may silently conflate randomized and analytic N.
- Exact human question: What does each parenthetical figure count represent, and how do those seven counts relate to the stated222 diabetes participants?

## NUM-U07 — Exponentiated ANCOVA coefficient labelled relative difference in percent change

- Relationship: N221. Primary category: Measure, label, or scale inconsistency.
- Compared locations and roles: PLAN [DOC-002 p18 VI.e Equation3 and its interpretation](../../../../joi190122supp1_prod.pdf#page=18): log(ACR4)=β0+β1log(ACR0)+β2(vitaminD)+e; [exp(β2)−1] “relative difference in percent change”; PLAN [p17 VI.b](../../../../joi190122supp1_prod.pdf#page=17), percent-change definition.
- Rule/calculation: at a common baseline, the displayed model gives exp(β2)=adjusted follow-up ACR active/placebo ratio. Subtracting1 gives a relative follow-up-level difference, not generally a relative difference of baseline percent changes. Algebraic diagnostic only: placebo follow-up2B and active3B implies exp(β2)−1=3/2−1=.5, while fractional changes are1 and2 and their relative difference is2/1−1=1. These are illustrative inputs, not trial data.
- Tolerance: symbolic identity; no observed effect or model fit asserted.
- Direct observation: model and interpretation label are printed. Diagnostic inference: “percent change” may be loose terminology for relative follow-up change conditional on baseline.
- Alternatives/missing definition: if the intended change measure is a fold-change ratio rather than (follow-up−baseline)/baseline, the relative effect is coherent but the percent-change description needs clarification.
- QC relevance: the planned estimand can be extracted as either relative change of level or relative difference of percent changes, which have different algebraic meaning.
- Exact human question: Does exp(β2)−1 describe the baseline-adjusted relative follow-up ACR difference, or a relative contrast of percent changes as defined on p17?

## NUM-U08 — Stated intake multiplier differs from total intake after adding the supplement

- Relationship: N216. Primary category: Numeric or arithmetic inconsistency.
- Compared locations and roles: PLAN [DOC-002 p16 V.e.2 intake paragraph](../../../../joi190122supp1_prod.pdf#page=16), average EPA+DHA100-200 mg/day, proposed840 mg/day intervention, “increase ... intake by a factor of4 to8”.
- Rule/calculation: if intervention adds to unchanged dietary intake, total/baseline=(100+840)/100=9.4 at100 mg/day and (200+840)/200=5.2 at200 mg/day. Dose/baseline alone is840/200=4.2 to840/100=8.4, roughly the stated4-8.
- Tolerance: stated ranges are broad; no explicit approximation tolerance is supplied. This is a conditional added-versus-total multiplier discrepancy, not a precision complaint about4.2 rounding to4.
- Direct observation: all three inputs and “increase intake” wording are printed. Diagnostic inference: the authors may have meant supplemental dose as a multiple of baseline intake.
- Alternatives/missing definition: total dietary intake might change after assignment, or “by a factor” may refer loosely to added amount rather than final amount. No dietary-replacement assumption is stated.
- QC relevance: percentage or fold-intake descriptions may be reproduced incorrectly from the plan.
- Exact human question: Is4-8 the supplement-to-baseline ratio or the total post-supplement-to-baseline ratio, and was unchanged baseline dietary intake assumed?

## NUM-U09 — Intake-ratio calculation does not uniformly reach the claimed target range

- Relationship: N217. Primary category: Numeric or arithmetic inconsistency.
- Compared locations and roles: PLAN [DOC-002 p16 V.e.2](../../../../joi190122supp1_prod.pdf#page=16), Western omega3:omega6 ratio1:10 to1:20; hypothesized optimal1:1 or1:2; stated omega3 increase factor4-8; unchanged omega6 “would thus ... achiev[e]” optimal ratio.
- Rule/calculation: applying the stated factor to the stated initial ratio while holding omega6 fixed yields extremes4/20=.2 (1:5) and8/10=.8 (1:1.25). The claimed target corresponds to ratios.5-1, so the source's own lower extreme remains below that range. Even total-intake factor5.2 at1:20 gives.26 (1:3.846).
- Tolerance: arithmetic on broad source ranges; not a measured dietary estimate.
- Direct observation: the inference “would ... achieve” and input ranges are printed. Conditional diagnostic: EPA+DHA intake and total omega3 intake are not explicitly equated.
- Alternatives/missing definition: particular typical intakes may reach the target; non-EPA/DHA omega3 can change the multiplier; the paragraph could intend a directional move toward the target rather than assurance throughout the stated range.
- QC relevance: a quantitative ratio claim can be over-read when translating supplemental dose into a dietary intake ratio.
- Exact human question: Which baseline omega3 and omega6 intakes support the claimed achieved ratio, and is “achieving” intended for the full printed intake range or only a specified typical case?

## NUM-U10 — Vitamin D active SGLT2 year5 percentage lacks a common column denominator

- Relationship: N271. Primary category: Denominator, proportion, or total inconsistency.
- Compared locations and roles: REPORT [DOC-003 p7 eTable2, VitaminD active, year5 SGLT2](../../../../joi190122supp2_prod.pdf#page=7),25(6%); REPORT same table year5 biguanides325(66%) and footnote percentages among nonmissing responses, total916.
- Rule/calculation: integer percentages rounded to nearest percent imply |100n/d−p|≤.5. The biguanide cell implies d between32500/66.5≈488.72 and32500/65.5≈496.18, hence integers489-496. SGLT2 implies d between2500/6.5≈384.62 and2500/5.5≈454.55, hence385-454. There is no overlap. Across all other medication rows/tables, active D year5 feasible denominator490-493, which gives25/d≈5.071-5.102%, rounding5%.
- Tolerance: ±.5 percentage point; exact numerators. Denominator not inferred from703 baseline N.
- Direct observation: both count/percent pairs are printed. Diagnostic: a common assignment/time nonmissing-response denominator cannot reproduce both.
- Alternatives/missing definition: medication-specific SGLT2 missingness could yield a different denominator; exact arm- and item-specific denominators are absent. A reversed denominator or transcribed percentage is only a possible mechanism.
- QC relevance: dose-assignment medication prevalences can be extracted with an inconsistent denominator interpretation.
- Exact human question: What nonmissing denominator was used for25 SGLT2 users in the active vitaminD year5 cell, and is it intended to share the denominator used for other year5 medication cells?

## NUM-U11 — Vitamin D placebo SGLT2 year5 percentage lacks a common column denominator

- Relationship: N271. Primary category: Denominator, proportion, or total inconsistency.
- Compared locations and roles: REPORT [DOC-003 p7 eTable2, VitaminD placebo, year5 SGLT2](../../../../joi190122supp2_prod.pdf#page=7),21(4%); REPORT same table year5 biguanides313(74%) and nonmissing-response footnote total916.
- Rule/calculation: biguanides imply d in(31300/74.5,31300/73.5]≈(420.13,425.85], integers421-425. SGLT2 implies d in(2100/4.5,2100/3.5]≈(466.67,600], integers467-600. No overlap. Joint other-row feasible D placebo denominator422-425 gives21/d≈4.941-4.976%, rounding5%.
- Tolerance: ±.5 percentage point; exact numerators.
- Direct observation: distinct placebo cell has a separate mismatch from NUM-U10; shared row/cause does not merge them.
- Alternatives/missing definition: medication-specific SGLT2 responses might differ, but explaining21(4%) requires at least467 respondents whereas the biguanide denominator is at most425. Unreported item-specific denominators remain the relevant alternative.
- QC relevance: same bounded prevalence-extraction consequence as NUM-U10, with a distinct comparator and cell.
- Exact human question: What nonmissing denominator was used for21 SGLT2 users in the placebo vitaminD year5 cell, and should this percentage reconcile to the other year5 medication denominator?

## NUM-U12 — Paired urine analysis total944 conflicts with footnote included991

- Relationship: N319. Primary category: Denominator, proportion, or total inconsistency.
- Compared locations and roles: REPORT [DOC-003 p12 eTable7 title and baseline/year5 N cells](../../../../joi190122supp2_prod.pdf#page=12), analysis N944, VitaminD504+440 and omega3477+467; REPORT same page asterisk footnote,1312 enrolled,1311 baseline urine,991 baseline-and-year5 included,320 baseline-only and1 without baseline excluded.
- Rule/calculation: both arm partitions504+440=944 and477+467=944 agree with the title. Footnote arithmetic1311−320=991 and1312−320−1=991 gives a different included total. Difference991−944=47. If944 is the intended paired analytic N and1 baseline missing, implied baseline-only exclusion is1311−944=367, rather than320.
- Tolerance: exact integer identities, no rounding.
- Direct observation: title, N cells, included and excluded footnote counts contradict within the same table. Diagnostic: sample donation versus assay eligibility might distinguish991 from944, but the footnote explicitly says991 “were included in this analysis”.
- Alternatives/missing definition:47 paired sample donors might have unusable urine ACR assays or another exclusion omitted from the footnote; collection and analysable measurement are not synonymous. Package does not give a bridge explaining47.
- QC relevance: paired-analysis denominator and missingness can be extracted incorrectly; no effect-estimate distortion or conclusion impact is established.
- Exact human question: Were944 or991 participants included in eTable7, and what explains the47-participant difference and the associated320-versus367 exclusion count?

## Completed checks yielding no additional candidate

All120 relationships in the inventory are COMPLETE. All16 eTable1 count sums reconcile; respondent-specific percentage denominators are jointly feasible at displayed precision. All25 eTable2 and21 eTable3 observed numeric rows have exact two-factorial count partitions and coherent overall percentages, with only the two distinct SGLT2 percentage cells flagged above. Every ACE/ARB union has nonnegative implied overlap and valid bounds; medication classes are nonexclusive.

All24 intervention/time rows of eTables4-9 were checked for N bounds, within-arm signs, difference/ratio reference, units, active-to-placebo contrast orientation and descriptive arithmetic. The tables distinguish model-adjusted contrasts and MI changes from observed available-case marginal means: nonidentical raw arithmetic is recorded as diagnostic in the inventory, rather than assumed evidence of an error. eTable4 paired total and exclusions reconcile; eTable5 and8 measured N remain at or below intervention-specific adherence cohorts; eTable6 parallel visit totals match; eTable9 excluded-UTI counts match between assignment partitions. The footnote phrase “Mean and SD values” accompanies columns explicitly identified as95% CI and ratios: it does not override those explicit column labels or establish that a displayed CI is an SD, so no standalone candidate is emitted.

No candidate is generated solely for absent raw source data, exact graphical coordinates, individual medication response denominators, or a display-zero P value. Power-table monotonicity, original cohort loss arithmetic, simple treatment allocation and stated dose-plus-nonstudy limit arithmetic reconcile. Historical observations are not equated across distinct cohorts, observation periods or markers.

## Limitations and reserved remainder

Exact arm/item nonmissing denominators are not printed for follow-up medication percentages; raw imputation/model output and exact graph coordinates are not supplied. Those are calculation limits, with full printed scope checked. No assigned scientific coverage gap remains.

Coordinator's explicit boundary reserves DOC-003 eTable10 p15, eTable11 p16, eFigures1-3 pp17-19 and DOC-004 p1 to a fresh extension reviewer. This shard does not claim those numeric checks complete. Candidate count:12 local records NUM-U01 through NUM-U12; relationship count120 N201-N320.

