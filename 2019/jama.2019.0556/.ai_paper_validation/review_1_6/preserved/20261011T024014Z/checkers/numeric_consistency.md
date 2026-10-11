# Numeric consistency review

Fresh specialist: /root/numeric_checker, qc16_numeric_consistency_reviewer, gpt-6.1-sol/medium; inherited current provider. Inputs: complete M001–M120 main map, U001–U064 support map and disjoint PLAN/REPORT transcription parts, source inventory, scope, contract, settings and tooling record. No legacy candidates/reports, independent checker outputs, web, external literature, Python orchestration or GPU were used.

All 184 compound N relationships are complete: N001–N120 correspond to M001–M120; N121–N184 correspond to U001–U064. Each compound record includes every printed member and table subrow. All five sources/102 pages are accounted for, including explicit no-applicable pages. Numeric checks cover arithmetic, totals, subgroup sums, denominator, percentage, missingness, population, rounding, units, labels, scale, reference groups, rate/count and repeated values. Inferential compatibility receives independent S tracking. Parts: relationships/parts/numeric-main.md (120 records) and relationships/parts/numeric-support.md (64 records). Canonical complete merge: relationships/numeric_relationship_inventory.md.

Direct authority is the supplied PDFs. Source-linked native/layout transcriptions were read; reused main pp3,6,7 images were visually inspected. New numeric-main-p4-layout.txt was produced with direct Poppler pdftotext26.01.0, -f4 -l4 -layout. Counts use exact equality; percentages allow half the last printed digit; rounded values use propagated intervals. Population, model, imputation, time and measurement basis are matched before equality is asserted. Missing definitions remain named human questions. There are 15 distinct local NC candidates below (NC-01 through NC-12 and NC-14 through NC-16), without stable C IDs or AI adjudications. Display-zero P alone was excluded: U058.g is DISPLAY_ZERO_NOT_CANDIDATE.

## NC-01 — Sample-size total versus four cell counts

**Relationship / category:** N010/M010; Denominator, proportion, or total inconsistency.

**Compared locations and document roles:** [main p4 Sample Size](../../../jama_bot_2019_oi_190007.pdf#page=4), REPORT, total and parenthetical cell count in the same paragraph; [main p1 factorial design](../../../jama_bot_2019_oi_190007.pdf#page=1), REPORT, four combinations.

**Printed inputs:** “392 participants (196 in each of the 4 possible intervention combinations)”; 20% versus30% incidence, 33% relative reduction, 22% attrition and250 per combination.

**Rule, calculation and tolerance:** Four cells of196 imply4×196=784, not392; discrepancy392 participants, exact count tolerance0. The incidence contrast itself reconciles:10/30=33.33%. No unprovided power formula is reconstructed.

**Direct observation versus inference / alternatives:** The total/cell wording conflicts arithmetically.392 might instead mean one two-cell marginal condition, or196 might describe one of two main-effect groups. That aggregation is unprovided; neither interpretation is imposed.

**Quality-control relevance:** Planning totals can be copied with incompatible per-cell counts; conclusion impact is not asserted.

**Exact human question:** Does392 denote one marginal intervention condition, the entire pre-attrition sample, or something else, and how does “196 in each of the4 possible intervention combinations” correspond to it?

## NC-02 — BMI label on1451 online exclusions

**Relationship / category:** N002/N018/N021; Measure, label, or scale inconsistency.

**Compared locations and document roles:** [main p3 Figure1 online and telephone exclusion rows](../../../jama_bot_2019_oi_190007.pdf#page=3), REPORT; [main p2 Eligibility](../../../jama_bot_2019_oi_190007.pdf#page=2), REPORT. Results-supplement p3 corroborates25–40 only.

**Printed inputs:** “1451 BMI<15 or>40”; inclusion BMI25–40; telephone18 BMI<25.

**Rule, calculation and tolerance:** Lower thresholds15 and25 differ by10kg/m². A diagnostic BMI20 fails25–40 but not the printed online rule. Label tolerance0; this illustrative value is not participant data.

**Direct observation versus inference / alternatives:**15 was visually read. No actual BMI distribution or misclassified count is supplied. A wider online prescreen followed by stricter telephone screening, or a label defect, could explain the difference; the stage-specific rule is missing.

**Quality-control relevance:** The criterion attached to1451 exclusions affects quantitative flow extraction without establishing ineligible enrollment.

**Exact human question:** Were the1451 exclusions based onBMI<15, or should the label use25; if15 was intentional, what stage-specific rule reconciles it with later BMI25–40 eligibility?

## NC-03 —22 events assigned the wrong therapy label in Table2 footnote d

**Relationship / category:** N075/M075 and Table2 footnotes; Measure, label, or scale inconsistency.

**Compared locations and document roles:** [main p6 Table2 footnotes d/f](../../../jama_bot_2019_oi_190007.pdf#page=6), REPORT; [main p7 onset narrative](../../../jama_bot_2019_oi_190007.pdf#page=7), REPORT.

**Printed inputs:** Footnote d assigns32/256(12.5%) and22/256(8.6%) both to supplements without therapy. Footnote f and p7 assign22 to supplements with therapy.

**Rule, calculation and tolerance:** The same arm/time/outcome cannot have32 and22 as separate component counts.32/256=12.5%,22/256=8.59375%→8.6%; percentages reconcile, but the22-event arm label conflicts. Label tolerance0.

**Direct observation versus inference / alternatives:** Both “without therapy” phrases were visually read. A copy defect is plausible, but no correction is imposed; no alternate population/time is stated.

**Quality-control relevance:**22 events can be assigned to a different arm during extraction despite the correct54-event margin.

**Exact human question:** Which therapy arm should carry22/256(8.6%) in Table2 footnote d, and how should its component labels be reconciled?

## NC-04 — PLAN25% contrast versus30% and15% incidences

**Relationship / category:** N129/U009; Numeric or arithmetic inconsistency.

**Compared locations and document roles:** [protocol p16 §4.4 first sentence and following risks](../../../joi190007supp1_prod.pdf#page=16), both PLAN.

**Printed inputs:** Powered to detect a25% difference; expected control30%, intervention15%;180/group, α=.05, power.90.

**Rule, calculation and tolerance:**30−15=15 percentage points; control-relative reduction15/30=50%, not25%. Half-integer percentage rounding gives14–16pp and approximately47.46–52.46% relative reduction, still excluding25%.

**Direct observation versus inference / alternatives:** All three quantities are printed. Ordinary absolute/control-relative definitions are diagnostics.25% might describe a different factorial/main-effect/additive-interaction contrast; its denominator is unprovided. Power is not independently recreated.

**Quality-control relevance:** Plan effect-size assumptions may be extracted inconsistently; this does not adjudicate study power.

**Exact human question:** Which contrast and denominator define25%, and how does it relate to the adjacent30% control and15% intervention cumulative incidences?

## NC-05 — PLAN blood summary35ml versus detail37ml

**Relationship / category:** N122/N148/N149; Numeric or arithmetic inconsistency.

**Compared locations and document roles:** [protocol p9 burden paragraph](../../../joi190007supp1_prod.pdf#page=9), PLAN; [p36 Blood rows](../../../joi190007supp1_prod.pdf#page=36), PLAN; [p37 volume table](../../../joi190007supp1_prod.pdf#page=37), PLAN.

**Printed inputs:** Summary3×6ml+2×8.5ml at baseline/6/12 months; detail2×8.5ml serum,6ml trace elements,2ml hematology,6ml plasma,6ml DNA;37ml total at each wave.

**Rule, calculation and tolerance:** Summary18+17=35ml; detail17+6+2+6+6=37ml; discrepancy2ml. Detail total itself is exact. Nominal tube-volume tolerance0; small decimal rounding cannot bridge2ml.

**Direct observation versus inference / alternatives:** The amounts are printed. The2ml hematology tube is a possible omitted component, not an assertion about actual draws. Conditional DNA collection would remove6ml, yielding31ml rather than35ml; another amended schedule remains possible.

**Quality-control relevance:** Nominal specimen volumes may be copied inconsistently into operational summaries.

**Exact human question:** Should the summary include the2ml hematology tube, or was a distinct35ml schedule intended; which schedule applies to baseline/6/12 collections?

## NC-06 — Planned1000mg/day EPA+DHA versus reported1412mg/day

**Relationship / category:** N003/N121/N131/N133/N136/N165; Cross-document numeric inconsistency.

**Compared locations and document roles:** [protocol p23 dose](../../../joi190007supp1_prod.pdf#page=23), PLAN; [p18 capsule definition](../../../joi190007supp1_prod.pdf#page=18), PLAN; [main p2 intervention](../../../jama_bot_2019_oi_190007.pdf#page=2), REPORT; [results supplement p4 composition](../../../joi190007supp3_prod.pdf#page=4), REPORT. Protocol p20 tolerance is PLAN contextual support.

**Printed inputs:** IntendedEPA+DHA=1.0g/day;1000mg capsule,3:1 ratio, daily capsule; reported1412mg EPA+DHA/day,3:1. Product acceptable deviation90–125%.

**Rule, calculation and tolerance:**1g=1000mg; difference412mg/day,41.2%. If nominal tolerance applies, allowed900–1250mg, with1412 exceeding1250 by162mg. Display rounding cannot bridge412mg.

**Direct observation versus inference / alternatives:** The declared daily masses differ. Applying product tolerance to totalEPA+DHA is conditional on an unprovided analyte basis. Amendment, changed formulation, nominal versus actual mass or capsule/fish-oil versus active-fatty-acid basis could explain it; p23 explicitly calls1g EPA+DHA.

**Quality-control relevance:** Dose extraction can differ between plan and report without proving a protocol violation or safety concern.

**Exact human question:** How does intended1.0g/day EPA+DHA relate to reported1412mg/day; was a formulation/amendment or different mass basis used, and does90–125% tolerance apply?

## NC-07 — Declared EPA:DHA3:1 versus laboratory composition

**Relationship / category:** N003/N165/N166; Measure, label, or scale inconsistency.

**Compared locations and document roles:** [results supplement p4 ratio](../../../joi190007supp3_prod.pdf#page=4), REPORT; [p5 assays](../../../joi190007supp3_prod.pdf#page=5), REPORT. Main p2 corroborates3:1 only.

**Printed inputs:** EPA+DHA1412mg,3:1 ratio; laboratory EPA67.9g/100gFAME(SD.85),DHA14.6g/100gFAME(SD1.55), six active supplements tested in duplicate.

**Rule, calculation and tolerance:** Common laboratory denominator permits ratio-of-means67.9/14.6=4.650685. Half.1 rounding gives[4.6314,4.6701], excluding3. This is not the mean per-capsule ratio or reconstructed daily mass; SD is assay variation, not mean rounding tolerance.

**Direct observation versus inference / alternatives:** Ratio declaration and assay means are printed. Equating methyl-ester composition with delivered fatty-acid mass is conditional. Nominal/assayed formulation, batches or unprovided conversion factors could explain it; total fat mass and chemical conversions are not invented.

**Quality-control relevance:** Ratio and laboratory composition may yield different intervention descriptions.

**Exact human question:** On what formulation/mass basis is3:1 defined, and how does it reconcile67.9 and14.6g/100gFAME?

## NC-08 — Ten food groups versus eleven listed categories

**Relationship / category:** N167/U047; Numeric or arithmetic inconsistency.

**Compared locations and document roles:** [results supplement p6 dietary advice count/list](../../../joi190007supp3_prod.pdf#page=6), REPORT. [p12 eleven-group score](../../../joi190007supp3_prod.pdf#page=12), REPORT, corroborates a possible convention but is not the required comparator.

**Printed inputs:** “Ten different food groups”: vegetables,fruit,fish,meat,pulses/legumes,whole grains,low-fat dairy,olive oil,processed foods,soft drinks,alcoholic beverages.

**Rule, calculation and tolerance:** Eleven distinct listed categories, counting synonymous pulses/legumes once, versus ten; count tolerance0.

**Direct observation versus inference / alternatives:** Count word and list are printed. Some categories may be combined, or alcohol may lie outside the counted groups. No grouping is supplied; counseling taxonomy is not assumed identical to scoring taxonomy.

**Quality-control relevance:** Dietary intervention components may be summarized as ten or eleven.

**Exact human question:** Which listed items form the ten groups, or should the count be eleven; is any recommendation intentionally outside the count?

## NC-09 — Blood subset211–331 paired with22–32%

**Relationship / category:** N171/U051; Denominator, proportion, or total inconsistency.

**Compared locations and document roles:** [results supplement p12 subset range](../../../joi190007supp3_prod.pdf#page=12), REPORT; [main p1 total1025](../../../jama_bot_2019_oi_190007.pdf#page=1), REPORT, possible whole-trial denominator.

**Printed inputs:** Baseline/12-month subset “n=211 to331,22-32%”; trial1025.

**Rule, calculation and tolerance:**211/1025=20.585%→21%;331/1025=32.293%→32%. Under any common integer denominatorD, rounded22% for211 requiresD938–981; rounded32% for331 requiresD1019–1050. These intervals do not overlap. Integer percentages allow±.5pp; counts exact.

**Direct observation versus inference / alternatives:** Paired ranges are printed; pairing range endpoints and a common denominator are diagnostic assumptions. Separate wave/analyte populations or nonpaired range endpoints could explain the percentages; the denominator definition is missing.

**Quality-control relevance:** Blood measurement coverage can be extracted as22% when211 is about21% of the randomized sample.

**Exact human question:** Which denominators and wave/analyte pairings yield211–331 as22–32%, and do percentage endpoints refer to the same participant base?

## NC-10 — TFEQ-18 labeled21 items in PLAN

**Relationship / category:** N147/U027; Measure, label, or scale inconsistency.

**Compared locations and document roles:** [protocol p35 instrument row and item count](../../../joi190007supp1_prod.pdf#page=35), PLAN; [p28 TFEQ-18 designation](../../../joi190007supp1_prod.pdf#page=28), PLAN. Main p4 R18 label is corroboration only.

**Printed inputs:** TFEQ-18, No.items21; earlier TFEQ-18 designation.

**Rule, calculation and tolerance:** Under the apparent item-count suffix convention,18 differs21 by3. Neighboring PHQ-9/9,IDS-SR30/30,GAD-7/7 support this diagnostic convention; no external instrument knowledge is used. Label/count tolerance0.

**Direct observation versus inference / alternatives:**18 and21 are printed; treating suffix18 as item count is conditional. Three local questions, a21-item variant or a table defect could explain it; no extension is stated.

**Quality-control relevance:** Instrument version/length can be extracted differently without proving the scored outcomes wrong.

**Exact human question:** Was an18-item TFEQ plus three additional questions used, a21-item version, or another instrument, and how should its label and21-item count be reconciled?

## NC-11 — GA2LEN264 PLAN items versus250 REPORT items

**Relationship / category:** N147/N171; Cross-document numeric inconsistency.

**Compared locations and document roles:** [protocol p35 FFQ-GA2LEN row](../../../joi190007supp1_prod.pdf#page=35), PLAN; [results supplement p12 questionnaire description](../../../joi190007supp3_prod.pdf#page=12), REPORT.

**Printed inputs:** FFQ-GA2LEN No.items264;250-item GA2LEN food frequency questionnaire.

**Rule, calculation and tolerance:** Same named trial measure,264−250=14 items; count tolerance0.

**Direct observation versus inference / alternatives:** Counts/name are printed; alignment assumes the same FFQ version. Extra nonfood items, site/language variants, a revision or a250-food-item subset could explain the difference; item-count basis is unprovided.

**Quality-control relevance:** Questionnaire length/version may be transcribed inconsistently; dietary scores are not declared incorrect.

**Exact human question:** How do264 planned GA2LEN items relate to the250-item report; were14 omitted, classified differently or changed by site/version?

## NC-12 — Strict greater-than versus at-least70% adherence

**Relationship / category:** N009/N072/N162/N171/N175; Measure, label, or scale inconsistency.

**Compared locations and document roles:** [main p4 adherence definition](../../../jama_bot_2019_oi_190007.pdf#page=4), REPORT; [main p6 adherence narrative](../../../jama_bot_2019_oi_190007.pdf#page=6), REPORT; [results supplement p16 weight adherence row](../../../joi190007supp3_prod.pdf#page=16), REPORT. SAP p4 corroborates≥70% only.

**Printed inputs:** A-priori≥70%; narrative77% adherent “more than70%”; table≥70%, counts135+134+126+120=515,N666.

**Rule, calculation and tolerance:**≥70% includes exactly70%,>70% excludes it.515/666=77.327%→77%, attaching the same summary to differently strict threshold wording. Threshold tolerance0; summary rounding±.5pp.

**Direct observation versus inference / alternatives:** Inequalities/counts are printed. No participant exactly at70% is asserted. Informal shorthand, an altered criterion or no observations at the boundary could preserve counts while leaving a label question.

**Quality-control relevance:** Inclusion at70% may be reproduced differently from copied definitions.

**Exact human question:** Was515/666 computed using≥70% or strictly>70%, and which inequality should the p6 narrative use?

## Checked noncandidate — CACE formula diagnostic (local NC-13 withdrawn before stable registration)

**Diagnostic relationships:** N014/N112/N174/N183. Status: CHECKED_NONCANDIDATE_LIMITATION. The supplied formula does not identify the binary-outcome original estimate or scale; matching pooled main ITT logOR to the latent-class CACE quantity is unsupported. No independently printed contradictory label or sign for the same matched estimate exists. This diagnostic is not emitted as a candidate; its question is a limitation, not a proposed adjudication.

**Compared locations and document roles:** [results supplement p15 CACE formula](../../../joi190007supp3_prod.pdf#page=15), REPORT; [main p6 supplement ITT OR](../../../jama_bot_2019_oi_190007.pdf#page=6), REPORT; [results supplement p22 CACE OR](../../../joi190007supp3_prod.pdf#page=22), REPORT; [p16 compliance percentages](../../../joi190007supp3_prod.pdf#page=16), REPORT, contextual positive fractions.

**Printed inputs:** CACE estimate is original intervention estimate divided by treated-arm compliance; ITT supplementOR1.06(.87–1.29),CACEOR.84(.67–1.07); both interventions effect-coded−1,+1. Active-arm omega weight adherence76.8%/79.5%, self-report74.3%/71.7%.

**Rule, calculation and tolerance:** If original effect is a log-odds coefficient andp>0, division byp preserves sign. log1.06=.05827>0;log.84=−.17435<0. Rounded intervals[1.055,1.065) and[.835,.845) remain opposite sides of1. Illustrativep=.77 yields exp(log1.06/.77)=1.0786, not.84. LiteralOR/p is not assumed.

**Direct observation versus inference / alternatives:** Formula and ORs are printed; application on log-odds scale is explicitly conditional. Latent-class/structural-equation estimation may differ from literal pooled-ITT rescaling, or reference/outcome coding and imputation could differ. Exact original estimate, scale and compliance fraction are missing. Overlapping CIs do not settle a formula identity.

**Quality-control relevance:** A generic formula can be applied to these ORs on an unspecified scale; no causal/efficacy judgment is made.

**Exact human question:** On what scale, original estimate and compliance fraction does the formula apply to binary MDD, and how does it yield supplementOR.84 from ITTOR1.06 with the stated coding?

## NC-14 — Equal vitaminD upper limits described as unequally distant

**Relationship / category:** N136/U016; Numeric or arithmetic inconsistency.

**Compared locations and document roles:** [protocol p23 vitaminD dose/conversion and upper-limit prose](../../../joi190007supp1_prod.pdf#page=23), PLAN throughout.

**Printed inputs:**20μg=800IU; dose “well below”4000IU/day and “even more below”100μg/day.

**Rule, calculation and tolerance:** The supplied conversion is40IU/μg, so4000IU=100μg.20μg is20% of either limit,80% below both. Equal converted absolute distances also exclude “even more.” Nominal in-source conversion is exact for this diagnostic; no external standard is introduced.

**Direct observation versus inference / alternatives:** Values and comparative wording are printed; equality is derived in-source. The phrase might be rhetorical, or one limit/unit might be transcribed incorrectly; the package cannot select an explanation.

**Quality-control relevance:** Plan unit comparisons can suggest two different upper limits without implying the dose exceeds either.

**Exact human question:** Are4000IU/day and100μg/day the same intended limit under the stated conversion, and what quantitative comparison was intended by “even more below”?

## NC-15 — Initial PLAN supply13weeks versus4months

**Relationship / category:** N139/N142; Numeric or arithmetic inconsistency.

**Compared locations and document roles:** [protocol p26 Drug accountability](../../../joi190007supp1_prod.pdf#page=26), PLAN; [p30 baseline procedures](../../../joi190007supp1_prod.pdf#page=30), PLAN.

**Printed inputs:**13-week supply at baseline and months3,6,9; baseline package “a4month supply.”

**Rule, calculation and tolerance:**13weeks=91days; ordinary four calendar months approximately120–123days, difference29–32days. Even four28-day units=112days,21days more. Exact month convention is unspecified; ordinary rounding cannot make13weeks four months.

**Direct observation versus inference / alternatives:** Both baseline package durations are printed, referring to the same daily supplement schedule. A baseline buffer, earlier version or special overage could explain it, but no exception is stated. Actual ingestion/overdosing is not inferred.

**Quality-control relevance:** Operational supply quantity can be extracted differently from two plan paragraphs.

**Exact human question:** Did the baseline package contain13weeks or4months of daily pills/capsules, and was an explicit baseline buffer intended beyond the13-week rule?

## NC-16 — Paired nutrient-changeN335 versus blood upper331

**Relationship / category:** N171/N175,U051/U055.o/U055.p/U055.q; Denominator, proportion, or total inconsistency.

**Compared locations and document roles:** [results supplement p12 specimen subset](../../../joi190007supp3_prod.pdf#page=12), REPORT; [p16 nutrient-change N rows](../../../joi190007supp3_prod.pdf#page=16), REPORT.

**Printed inputs:** Baseline/12-month serum subset211–331 for selenium,folate,vitaminD;T12−T0 change N335 for all three. EPA334 is another analyte, not required for this comparison.

**Rule, calculation and tolerance:** Observed paired changes cannot exceed either wave's available sample.335>331 by4; exact count tolerance0. The pairing/subset alignment is conditional; table N is printed, not reconstructed.

**Direct observation versus inference / alternatives:** Counts/time labels are printed; paired-intersection bound is derived. Imputed change values, pooled sites, different analyte/wave coverage or a transcription difference could explain it. The table does not explicitly identify that base or imputation rule; raw specimen data are unavailable.

**Quality-control relevance:** Biomarker analyticN may be copied as335 despite a stated blood-sampling maximum331.

**Exact human question:** Which participants and measurement/imputation rule produceN335 for paired selenium/folate/vitaminD changes, and how does that population relate to the stated211–331 blood subset?

## Complete noncandidate checks and limitations

The N inventory records each completion calculation. Flow exclusions, per-arm attrition reasons, baseline count/percentage pairs, sex/country/education totals, event margins, person-month margins, person-time rates, questionnaire missingness, hospital/death totals and concealment count/percentage cells reconcile.239 endpoint-censored dropouts versus246 missing month12 MINI is reconciled by the explicit Table2 definition; planned1000 versus observed1025 is not itself a discrepancy. Different imputed/nonimputed/model/time results are not forced equal. CohenD and adjustedB may differ because their calculations differ. Identical rounded alcohol/utility summaries and near-zero coefficients alone are not contradictions. Table3 doubling versus narrative differences reconcile with propagated rounding.

Unprinted adherence denominators were uniquely inferable from displayed count/percentage pairs and sum to their printed totals, but remain derived. Graphs lack exact labeled means/whiskers; only printed axes, sample sizes, legends and direct visual direction were used. Unpublished manufacturingC1.2, participant data, exact CACE compliance fractions and complete model outputs are unavailable. These constrain diagnosis rather than source coverage. External recheck and human adjudication are coordinator stages; this checker assigns no evidence states or dispositions.
