# Mechanical evidence recheck: C039–C057

Assigned scope: C039, C040, C041, C042, C043, C044, C045, C046, C047, C048, C049, C050, C051, C052, C053, C054, C055, C056, C057. All 19 IDs were rechecked separately. Each remains Pending Human Adjudication. Evidence states describe the record, not an adjudication.

Authority and engines: direct supplied PDFs; fresh Poppler 26.01.0 `pdftotext -layout -f N -l N` derivatives `preprocessing/recheck_cross_stats_main_N.txt` for main pages 4,6,7,8; `recheck_cross_stats_results_N.txt` for results pages 5,6,11,12,14,15; `recheck_cross_stats_protocol_N.txt` for protocol pages 81,136; and `recheck_cross_stats_sap_N.txt` for SAP pages 16,17,18,26,27,31,46,57,58,60,61,67,68,71. Protocol pages 81 and 136 have unusable native text and were read visually from current-run source page rasters `protocol_middle_p81.png` and `plan_tail_protocol_136.png`. Source-linked current-run main page 8 raster `numeric_main_p008.png` was also read. Fresh direct Poppler `pdftoppm -r 100 -f N -l N -singlefile -png` source rasters `recheck_cross_stats_results_N.png` for pages 5,6,14,15 and `recheck_cross_stats_sap_N.png` for pages 16,17,58,61,67,68 were read visually. Mathematical signs in rasters govern over the text derivatives. All new derivatives are below review_1_6/preprocessing; no source or reused asset was modified. CPU-only R 4.5.2 reproduced C050/C052/C057 calculations using `preprocessing/recheck_cross_stats_calculations.R`, with results in `preprocessing/recheck_cross_stats_calculations.txt`; R was auxiliary arithmetic, not scientific orchestration.

Role assignments are content-based: main article and result eTables are REPORT; prospective protocol/manual and original/final SAP versions are PLAN. No plan that merely corroborates one side adds a discrepancy relationship.

## C039 — Six-month numbness/tingling counts and unresolved field identity

- **Location found:** Yes: REPORT [main p8 Table 3](../../../jama_rathinam_2019_oi_190092.pdf#page=8) and REPORT [results p12 eTable 6](../../../joi190092supp1_prod.pdf#page=12).
- **Source value/text matched:** Main nonserious systemic “Numbness or tingling” is MTX 25 (23.4%), MMF 18 (16.7%), under patients reporting at least one adverse event at six months.
- **Comparator matched:** eTable 6, “Six-Month Patient-Reported Other Systemic Adverse Events,” prints “Numbness/tingling” 13 (12.1%)/11 (10.2%), with N107/N108 and patients reporting at least one event.
- **Consistency rule applicable:** Same-variable, same-period, same-patient-stream counts should match; however, same-variable identity is not established by similar labels. The explicit “Other Systemic” title supports a distinct response stream as a possible interpretation.
- **Calculation/logical comparison reproduced:** Printed differences are 25−13=12 and 18−11=7. This is an observed count difference, but does not reproduce an unconditional same-variable inconsistency.
- **Necessary inputs available:** Counts, arms, six-month period and patient-level rather than event-level measure are available.
- **Exact missing inputs/definitions:** Field IDs, structured-versus-additional symptom provenance, aggregation and deduplication rules, and a crosswalk showing whether both rows represent the same safety variable.
- **Source-grounded alternative interpretation:** Main Table 3 may summarize the neurologic-function checklist item (eTable 1 p6 defines it as numbness or tingling), while eTable 6 explicitly summarizes patient-reported other systemic events. Different streams can yield different counts without numeric error.
- **Direct observation versus inferred explanation:** Counts and titles are observed; common-field identity and a specific data-collection mechanism are inferred and unconfirmed.
- **Exact remaining human question:** Do these rows share a field and aggregation rule, or do 25/18 and 13/11 summarize different questionnaire/event streams?
- **Classification:** Primary category Cross-document numeric inconsistency; primary S_C; all S_C; REPORT main p8 versus REPORT results p12. No role or relationship correction.
- **Evidence state:** `record_input_error`. Decisive fact: the registered comparison relies on unsupported field alignment; the package does not settle whether a residual same-variable mismatch exists. This does not erase the directly observed count difference.

## C040 — Mood counts and unresolved union membership

- **Location found:** Yes: REPORT [main p8 Table 3](../../../jama_rathinam_2019_oi_190092.pdf#page=8), REPORT [results p11 eTable 5](../../../joi190092supp1_prod.pdf#page=11).
- **Source value/text matched:** “Mood changes (self-reported, not requiring therapy)” 33 (30.8%)/26 (24.1%).
- **Comparator matched:** “Six-Month Patient-Reported Mood-Related Adverse Events,” “Any mood-related adverse event” 22 (20.6%)/19 (17.6%), N107/N108, counts of patients reporting at least one event.
- **Consistency rule applicable:** A subset cannot exceed its union, but the main checklist item must first be shown to belong to this specific appendix union. That inclusion is not printed.
- **Calculation/logical comparison reproduced:** 33>22 by 11 and 26>19 by 7. No overlapping subrow sum was used. A conditional set-containment problem exists if the main row belongs to the appendix union; unconditional membership is unestablished.
- **Necessary inputs available:** Arm, period, patient count, appendix union label and main nonserious mood label.
- **Exact missing inputs/definitions:** Questionnaire-field crosswalk, whether “Any” includes the structured mood-change item or only additional mood descriptions, and the union/deduplication algorithm.
- **Source-grounded alternative interpretation:** The appendix's detailed patient-reported symptom taxonomy may summarize a separate additional-response field, while main Table 3 uses the mood-change checklist category defined in eTable 1 p6.
- **Direct observation versus inferred explanation:** The two count pairs and labels are observed; subset membership and separate-stream mechanisms are inferences.
- **Exact remaining human question:** Does eTable 5 “Any” include the main structured mood item, and what fields and union rule produced 33/26 versus 22/19?
- **Classification:** Denominator, proportion, or total inconsistency; S_C; all S_C; REPORT main p8 versus REPORT results p11. No correction to category or relationships.
- **Evidence state:** `record_input_error`. Decisive fact: union membership required by the registered set rule is an unsupported alignment assumption and cannot be settled from supplied definitions.

## C041 — Creatinine lower-bound inequality

- **Location found:** Yes: REPORT [main p8](../../../jama_rathinam_2019_oi_190092.pdf#page=8), REPORT [results p5 eTable 1](../../../joi190092supp1_prod.pdf#page=5), PLAN [protocol p81 Table 3](../../../joi190092supp2_prod.pdf#page=81) and [p136 §6.1](../../../joi190092supp2_prod.pdf#page=136), with inequalities visually confirmed.
- **Source value/text matched:** Main nonserious creatinine “>1.5 to <2 mg/dL lasting <28 d,” counts 1/0.
- **Comparator matched:** Results definition and both plan locations use ≥1.5 to <2 mg/dL.
- **Consistency rule applicable:** Strict and inclusive inequalities classify exactly 1.5 differently; same numeric unit, adverse-event category and persistence condition are matched.
- **Calculation/logical comparison reproduced:** 1.5 satisfies x≥1.5 and does not satisfy x>1.5. The label mismatch is reproduced.
- **Necessary inputs available:** Printed lower/upper boundaries, mg/dL, <28-day rule and report counts.
- **Exact missing inputs/definitions:** Exact-boundary laboratory observations, implemented coding, and any later amended threshold; these are needed only to determine count consequences.
- **Source-grounded alternative interpretation:** Main row may abbreviate an inclusive implemented boundary, or an unprovided amended rule may exist.
- **Direct observation versus inferred explanation:** Inequalities differ directly; any changed count or production mechanism is not observed.
- **Exact remaining human question:** Was exactly 1.5 classified using the inclusive definition, and does the article label reflect the implemented rule?
- **Classification:** Measure, label, or scale inconsistency; P_R; all P_R, S_C. REPORT main differs from PLAN and REPORT results; the latter is a genuine report-report comparator.
- **Evidence state:** `recorded_candidate`, determined by the visually confirmed > versus ≥ boundary.

## C042 — Fever temperature cutpoint

- **Location found:** Yes: REPORT [main p8](../../../jama_rathinam_2019_oi_190092.pdf#page=8), REPORT [results p6 definition](../../../joi190092supp1_prod.pdf#page=6), [p14](../../../joi190092supp1_prod.pdf#page=14), [p15](../../../joi190092supp1_prod.pdf#page=15).
- **Source value/text matched:** Main “Fever <39°C for 12 h,” 11/18 patients.
- **Comparator matched:** p6 nonserious fever for 12 hours “>100.6 to 103°F/39.5°C”; serious ≥103°F/39.5°C. pp14–15 label fever <103 degrees for 12 hours; their six-to-twelve-month counts are not compared to six-month counts.
- **Consistency rule applicable:** Matched category definitions use different temperature boundaries even when periods of observed events differ.
- **Calculation/logical comparison reproduced:** (103−32)×5/9=39.4444°C; 39°C converts to 102.2°F. Thus the printed 39°C boundary differs from the appendix 103°F/39.5°C category definition.
- **Necessary inputs available:** Units, numeric thresholds, duration and category labels.
- **Exact missing inputs/definitions:** Whether main integer 39 was intended as a coarse abbreviation, actual coding boundary and any amended definition; observations near the boundary are needed for count impact.
- **Source-grounded alternative interpretation:** Main may coarsely shorten 39.5 to 39 or label a different threshold; neither is explicitly explained.
- **Direct observation versus inferred explanation:** Labels and conversion are direct/derived facts; individual reclassification is unobserved.
- **Exact remaining human question:** What temperature cutpoint and inequality generated the six-month 11/18 counts, and what was intended by “<39°C”?
- **Classification:** Measure, label, or scale inconsistency; S_C; all S_C; REPORT main versus REPORT results. The appendix's own ≤/strict boundary topic remains a separate candidate.
- **Evidence state:** `recorded_candidate`, determined by the different displayed category cutpoints.

## C043 — Hemoglobin boundary with corrected supplement transcription

- **Location found:** Yes: REPORT [main p8](../../../jama_rathinam_2019_oi_190092.pdf#page=8), REPORT [results p5](../../../joi190092supp1_prod.pdf#page=5), [p14](../../../joi190092supp1_prod.pdf#page=14), [p15](../../../joi190092supp1_prod.pdf#page=15), PLAN [protocol p81](../../../joi190092supp2_prod.pdf#page=81), all visually inspected.
- **Source value/text matched:** Main low hemoglobin >6.5 to <9 g/dL for <28 days, 2/3 patients; results pp14–15 also use >6.5.
- **Comparator matched:** Direct raster p5 eTable 1 reads **≥6.5 to <9**, not >6.5; its serious definition is <6.5 or persistent <9. PLAN p81 likewise reads ≥6.5 to <9 with serious <6.5. Fresh native extraction incorrectly loses the underline in ≥ and cannot govern transcription.
- **Consistency rule applicable:** Exactly 6.5 for less than 28 days belongs to the inclusive nonserious definition, but not the strict row labels.
- **Calculation/logical comparison reproduced:** x=6.5 satisfies ≥6.5 and fails >6.5. Main/plan mismatch remains; corrected p5 adds main-versus-supplement and supplement-internal definition-versus-later-label comparisons.
- **Necessary inputs available:** Boundary values, units, duration, direct images and main/later result labels.
- **Exact missing inputs/definitions:** Actual laboratory coding and exact-boundary observations; whether strict labels are shorthand or an amendment.
- **Source-grounded alternative interpretation:** Implemented categories may consistently use ≥6.5, with strict > retained only in result-row labels. No count change is inferable.
- **Direct observation versus inferred explanation:** The p5 ≥ symbol and main/later > symbols are observed; a label-production explanation remains inferred.
- **Exact remaining human question:** Was exactly 6.5 included in nonserious counts, and why do main/later rows differ from the inclusive definition?
- **Classification:** Measure, label, or scale inconsistency; P_R; **all P_R, S_C, S_W**. REPORT main and later supplement rows differ from PLAN p81; REPORT main p8 differs from REPORT results p5; within REPORT results p5 differs from pp14–15. Correction: p5 is inclusive and corroborates PLAN, but becomes a substantive comparator against the strict report labels. Primary precedence remains P_R.
- **Evidence state:** `recorded_candidate`. The original p5 transcription is disproven, but the registered main-versus-plan boundary mismatch remains directly reproduced; its exact-boundary question is unchanged rather than a new residual question.

## C044 — Leukocyte boundary reconciles after visual glyph correction

- **Location found:** Yes: REPORT [results p5](../../../joi190092supp1_prod.pdf#page=5), PLAN [protocol p81](../../../joi190092supp2_prod.pdf#page=81); REPORT [main p8](../../../jama_rathinam_2019_oi_190092.pdf#page=8) supplies the nonserious row only.
- **Source value/text matched:** Direct source raster eTable 1 serious acute leukocyte boundary reads **≤1,000/µL**, not the registered <1,000. Native text loses the underline. Nonserious is >1,000 and <2,500 lasting <28 days.
- **Comparator matched:** PLAN serious ≤1,000; nonserious >1,000 to <2,500. Persistent low counts are also described; the main nonserious row does not contradict this rule.
- **Consistency rule applicable:** Compare the actual strict/inclusive category boundaries at exactly 1,000.
- **Calculation/logical comparison reproduced:** At x=1,000 both REPORT and PLAN classify acute counts as serious; neither nonserious category includes x=1,000. Registered discrepancy is explicitly disproven.
- **Necessary inputs available:** Both exact source inequalities, same cells/µL units and duration conditions.
- **Exact missing inputs/definitions:** None needed to settle this registered printed-boundary comparison; patient-level laboratory values are unnecessary.
- **Source-grounded alternative interpretation:** The registered < arose from failed text extraction of ≤; the source itself reconciles.
- **Direct observation versus inferred explanation:** ≤ in both source images is observed. Extraction glyph loss is evidenced by the native derivative, without making an inference about author intent.
- **Exact remaining human question:** No boundary-consistency question remains for these compared locations; human review can inspect the ≤ glyph and retained record.
- **Classification:** Measure, label, or scale inconsistency; P_R; all P_R; REPORT results p5 versus PLAN p81. Relationship describes the registered comparison even though its evidence state changes; no extra relationship from the corroborating main nonserious row.
- **Evidence state:** `not_reproduced`, determined by direct source ≤1,000 matching PLAN ≤1,000 and disproving the registered < comparator.

## C045 — ALT/AST five-times-ULN boundary

- **Location found:** Yes: REPORT [main p8](../../../jama_rathinam_2019_oi_190092.pdf#page=8), [results p5](../../../joi190092supp1_prod.pdf#page=5), [p14](../../../joi190092supp1_prod.pdf#page=14); PLAN [protocol p81](../../../joi190092supp2_prod.pdf#page=81), [p136](../../../joi190092supp2_prod.pdf#page=136), visually inspected.
- **Source value/text matched:** Main and results define nonserious 2 to 5 times ULN for <28 days and serious >5 times ULN, or persistent 2 to 5. Main counts 14/8 nonserious and 3/2 serious; later supplement counts concern a different period.
- **Comparator matched:** PLAN nonserious 2 to <5 and serious ≥5, in both table and adverse-event prose. All relevant strict/inclusive symbols visually match this reading.
- **Consistency rule applicable:** If printed “2 to 5” includes its upper endpoint, exactly 5 for <28 days is nonserious under REPORT and serious under PLAN; REPORT serious >5 definitely excludes exactly 5.
- **Calculation/logical comparison reproduced:** x=5 satisfies PLAN ≥5 and fails REPORT >5. Persistence ≥28 days is a separate coherent route and does not resolve an acute exact-5 boundary.
- **Necessary inputs available:** ULN scale, numerical boundaries and persistence labels.
- **Exact missing inputs/definitions:** Implemented inclusivity of “2 to 5,” laboratory code, exact-boundary observations, and any rule amendment.
- **Source-grounded alternative interpretation:** Report labels may compress a half-open 2-to-<5 interval, with >5 serious itself an abbreviated ≥5 label; or a distinct implemented boundary was used.
- **Direct observation versus inferred explanation:** Printed ≥5 versus >5 is directly observed; proposed coding and count impacts are unobserved.
- **Exact remaining human question:** How was exactly 5×ULN classified before 28 days, and do the result-row boundaries describe that code?
- **Classification:** Measure, label, or scale inconsistency; P_R; all P_R. REPORT locations agree with one another on their printed boundaries; PLAN locations agree with one another, so neither S_C nor P_P is added.
- **Evidence state:** `recorded_candidate`, determined by directly different plan/report exact-5 serious boundaries.

## C046 — Per-protocol adherence definition

- **Location found:** Yes: REPORT [main p6 narrative](../../../jama_rathinam_2019_oi_190092.pdf#page=6), [p7 Figure 2 model 4 and footnote e](../../../jama_rathinam_2019_oi_190092.pdf#page=7), PLAN [original SAP p31](../../../joi190092supp3_prod.pdf#page=31), [final SAP p71 §4.1](../../../joi190092supp3_prod.pdf#page=71).
- **Source value/text matched:** Report “Per protocol” includes missed less than 20% of doses, n184, 61/90 versus 54/94, OR1.56 (0.84–2.96), P=.17.
- **Comparator matched:** Both SAP versions exclude major deviations or noncompliance defined as less than 50% of study drug received by self report or pill counts at study visits.
- **Consistency rule applicable:** Complementary missed/received percentages under the same expected-dose basis give distinct adherence cutoffs for this named numerical sensitivity result.
- **Calculation/logical comparison reproduced:** <20% missed implies >80% received; exclusion of <50% received permits ≥50% on that criterion. A participant receiving 70% passes the latter and fails the former. 90+94=184 matches the report population.
- **Necessary inputs available:** Labels, thresholds, n184 and its arm counts; the result concretely links the population mismatch to numbers.
- **Exact missing inputs/definitions:** Participant exclusions, equivalence of adherence denominators, major-deviation handling and whether model 4 implements SAP per-protocol or an additional sensitivity subset.
- **Source-grounded alternative interpretation:** A stricter adherent-subset sensitivity may intentionally be reported under a broad “per protocol” label.
- **Direct observation versus inferred explanation:** Cutoffs differ as printed; differences in which actual people were included and consequent estimates are not reconstructed.
- **Exact remaining human question:** Was n184 intended as the SAP per-protocol population or a separate >80%-received sensitivity population, and what participant inclusion rule was used?
- **Classification:** Analysis-unit or population inconsistency; P_R; all P_R; REPORT main versus PLAN SAP. Original/final SAP agree, so no P_P.
- **Evidence state:** `recorded_candidate`, determined by different explicit adherence rules attached to the named population/result.

## C047 — Report noninferiority interpretation versus plan criterion

- **Location found:** Yes: REPORT [main p4](../../../jama_rathinam_2019_oi_190092.pdf#page=4), PLAN [final SAP p61 item 16](../../../joi190092supp3_prod.pdf#page=61), plan clause visually confirmed.
- **Source value/text matched:** Main MTX−MMF risk difference 9.5%, CI −5.3% to 21.8%, and lower bound −5.3 excludes the prespecified 10% margin, giving evidence of MTX noninferiority.
- **Comparator matched:** SAP states MTX noninferior if the lower limit of the 95% CI for treatment success at six months is “less than 10%”; one-sided comparison and 10% margin are stated, but the exact signed contrast is not.
- **Consistency rule applicable:** For the REPORT MTX−MMF contrast and 10-point allowable loss, a lower bound above −10% excludes such loss; a lower bound <+10% is a different criterion. This compares formal rule wording, not merely whether the actual −5.3 satisfies both inequalities.
- **Calculation/logical comparison reproduced:** −5.3>−10; a hypothetical lower bound −50 would also satisfy the printed <+10 rule while permitting a loss beyond the margin. A reverse MMF−MTX contrast would require an upper loss bound rather than the written lower bound.
- **Necessary inputs available:** Report orientation, observed CI, plan margin, lower-bound name and less-than direction.
- **Exact missing inputs/definitions:** Signed NI estimand in the plan, intended endpoint/direction, original test specification and any amendment.
- **Source-grounded alternative interpretation:** A sign, inequality or bound-name transcription in the plan, or an unprovided amended decision rule, could explain the different formal wording.
- **Direct observation versus inferred explanation:** Both decision statements and observed interval are read directly; intended formal NI rule is not inferred as fact.
- **Exact remaining human question:** Which signed contrast, bound, inequality and margin sign were prespecified and used to interpret the −5.3% bound?
- **Classification:** Statistical reporting inconsistency; P_R; all P_R; REPORT main p4 versus PLAN final SAP p61. C051 uses a different plan-internal comparator and remains separate.
- **Evidence state:** `recorded_candidate`, determined by the directly different formal decision-rule wording, conditional on the explicitly missing plan estimand.

## C048 — Rescue-success OR model description

- **Location found:** Yes: REPORT [main p4 methods](../../../jama_rathinam_2019_oi_190092.pdf#page=4), [p6 Table 2 OR header/footnote b and switched row](../../../jama_rathinam_2019_oi_190092.pdf#page=6), [p7 narrative](../../../jama_rathinam_2019_oi_190092.pdf#page=7); PLAN [final SAP p61 Specific Aim 2](../../../joi190092supp3_prod.pdf#page=61).
- **Source value/text matched:** Report applies the same primary logistic model at 12 months; table OR footnote b specifies treatment fixed and study site random. Switched-drug success is 20/29 versus 7/20, OR4.17 (1.32–13.16), P=.02; p7 rounded OR4.2 is coherent.
- **Comparator matched:** Aim 2 primary rescue logistic predictors are treatment group and reason for failure of the first drug, lack of efficacy versus any other reason.
- **Consistency rule applicable:** Printed adjustment/model labels for the same rescue-success result can be compared; site and failure-reason adjustment are different described structures. Unknown realized design matrices cannot be equated or reconstructed from marginal counts.
- **Calculation/logical comparison reproduced:** The REPORT label omits the PLAN failure-reason predictor and describes site random effects. No adjusted OR was recomputed; equality or inequality of actual coefficients is not established.
- **Necessary inputs available:** Exact rescue outcome, new-treatment contrast, table result, report model label and plan predictors.
- **Exact missing inputs/definitions:** Actual rescue design matrix, included covariates, site-effect implementation, model output and any disclosed change applying to this result.
- **Source-grounded alternative interpretation:** Failure reason may have been included but omitted from the compressed label; report may give a supplementary or amended rescue model.
- **Direct observation versus inferred explanation:** The labels differ directly; omission from the actual fitted model and consequent OR change are not observed.
- **Exact remaining human question:** Did the model producing OR4.17 include failure reason, site random effects, both or another structure, and how does it relate to the planned Aim 2 primary analysis?
- **Classification:** Statistical reporting inconsistency; P_R; all P_R; REPORT main versus PLAN final SAP. No report-internal mismatch from the coherently rounded p7 result.
- **Evidence state:** `recorded_candidate`, determined by a reproduced model-description mismatch with actual fitted covariates explicitly unavailable.

## C049 — Dose-reduction Fisher versus logistic test label

- **Location found:** Yes: REPORT [main p4 methods](../../../jama_rathinam_2019_oi_190092.pdf#page=4), [p6 result](../../../jama_rathinam_2019_oi_190092.pdf#page=6), PLAN [final SAP p61 item 15](../../../joi190092supp3_prod.pdf#page=61).
- **Source value/text matched:** Report states dose reductions compared using Fisher exact test; 21 (19.6%) MTX versus 15 (13.8%) MMF, P=.27.
- **Comparator matched:** Plan states dose reduction compared by arm using logistic regression based on treatment and other covariates as needed.
- **Consistency rule applicable:** These are distinct explicitly named inferential procedures for the same dose-reduction arm comparison.
- **Calculation/logical comparison reproduced:** Fisher exact comparison is not the named logistic-regression coefficient inference. The plan's Fisher provision for major protocol deviations does not redefine its separate dose-reduction item.
- **Necessary inputs available:** Outcome, arm comparison, report result and both test labels.
- **Exact missing inputs/definitions:** Actual analysis call, amendment or supplementary-analysis designation, and whether logistic comparison was separately conducted.
- **Source-grounded alternative interpretation:** Report could intentionally describe an unadjusted supplementary Fisher comparison or an amended analysis.
- **Direct observation versus inferred explanation:** Test names differ directly; actual analysis amendment or omission of planned analysis is unproven.
- **Exact remaining human question:** What test generated P=.27, and was the logistic comparison replaced, separately performed or represented only by this supplementary result?
- **Classification:** Statistical reporting inconsistency; P_R; all P_R; REPORT main versus PLAN final SAP. C057 compares the numerical Fisher output/printing precision, a distinct comparator.
- **Evidence state:** `recorded_candidate`, determined by the two directly different test descriptions.

## C050 — Missed-dose mean/SD versus Welch P

- **Location found:** Yes: REPORT [main p4 methods](../../../jama_rathinam_2019_oi_190092.pdf#page=4), [p6 Table 2 and narrative](../../../jama_rathinam_2019_oi_190092.pdf#page=6).
- **Source value/text matched:** Table and narrative both label mean (SD) missed-dose percentages 4.6 (1.0) versus 4.3 (0.5), P=.87.
- **Comparator matched:** Methods say missed doses compared by Welch t test and significance assessed with two-sided P. Table patient headers n96/n98 are not an explicit adherence-test sample size.
- **Consistency rule applicable:** A participant-level two-sample Welch test of the same means and SDs must satisfy its mean/SD/sample-size identity; the conservative check only requires each sample size ≥2 for a sample SD.
- **Calculation/logical comparison reproduced:** Under nearest-tenth summary rounding, mean difference ≥0.20 and SDs ≤1.05 and ≤0.55. Consequently absolute t ≥0.20/sqrt((1.05²+0.55²)/2)=0.238619994509. Welch degrees of freedom ≥1 because its variance-component denominator cannot exceed the square of their sum. The conservative df1 two-sided P bound is 0.850878358724, reproduced by R `2*pt(-t_bound,df=1)`; .87 requires ≥.865 under nearest-hundredth P rounding. Thus these same participant-level summaries cannot yield the attached .87 under the declared Welch rule. No n96/n98 assumption was used.
- **Necessary inputs available:** Mean values, dispersion numbers explicitly labeled SD, Welch definition and attached P.
- **Exact missing inputs/definitions:** Exact adherence variable, sample sizes, whether dispersion is truly SD rather than SE, unrounded summaries, transformation and printing conventions.
- **Source-grounded alternative interpretation:** Dispersion could have been SE, or the test could concern raw counts/transformed observations while different summaries were printed. Different actual n alone cannot resolve the conservative same-summary bound.
- **Direct observation versus inferred explanation:** Means/SD labels/P/test are observed; the bound is a diagnostic derived from those labels. Any alternative variable or mistaken label is unconfirmed.
- **Exact remaining human question:** Which variable and analysis-set n entered the Welch test, are 1.0/0.5 SD or SE, and is P=.87 attached to those same summaries?
- **Classification:** Statistical reporting inconsistency; S_W; all S_W; REPORT main p4 versus REPORT main p6.
- **Evidence state:** `recorded_candidate`, determined by the reproduced conservative bound under the same-summary and stated-label interpretation; named missing definitions remain explicit.

## C051 — Plan-internal noninferiority decision rule

- **Location found:** Yes: PLAN [final SAP p61 item 16](../../../joi190092supp3_prod.pdf#page=61), [p46 comparative aim](../../../joi190092supp3_prod.pdf#page=46), [p57 coding](../../../joi190092supp3_prod.pdf#page=57).
- **Source value/text matched:** MTX noninferior if lower limit of 95% CI for six-month treatment success is less than 10%, with a 10% margin; direct raster confirms “less than.”
- **Comparator matched:** Plan aim compares success fraction MMF versus MTX; p57 codes MTX=0 and MMF=1, success=1, establishing a comparative rather than absolute-success objective, while item 16 does not explicitly define its contrast.
- **Consistency rule applicable:** A comparative allowable-loss NI criterion must restrict the appropriate confidence bound. Lower<+10 does not enforce a 10-point bound on loss of MTX success for the common contrasts implied by the plan.
- **Calculation/logical comparison reproduced:** For MTX−MMF, arbitrarily negative lower bounds satisfy lower<+10 despite permitting losses >10. For MMF−MTX loss, an upper bound is relevant. For MTX success alone, lower<10 does not establish comparative loss. These logical counterexamples reproduce the plan-internal rule question without report evidence.
- **Necessary inputs available:** Margin, group comparison, coding, confidence-bound endpoint and inequality.
- **Exact missing inputs/definitions:** NI estimand, sign, signed margin, intended bound endpoint and formal test.
- **Source-grounded alternative interpretation:** Clause may have a sign/direction/bound-name transcription defect or refer to an unprovided signed loss estimand.
- **Direct observation versus inferred explanation:** Printed wording/coding are observed; hypothetical counterexamples are diagnostic, not trial data; intended amended rule is unknown.
- **Exact remaining human question:** What contrast/quantity, signed boundary, confidence endpoint and inequality were intended for this exact plan criterion?
- **Classification:** Statistical reporting inconsistency; P_P; all P_P; PLAN final SAP p61 versus PLAN final SAP pp46/57. REPORT is context only here; C047 separately compares REPORT to PLAN.
- **Evidence state:** `recorded_candidate`, determined by the printed plan-internal comparative-rule question with its missing estimand stated.

## C052 — Detectable rescue difference 17 versus 25 points

- **Location found:** Yes: PLAN [original SAP p26 prose/formula](../../../joi190092supp3_prod.pdf#page=26), [p27 power table/summary](../../../joi190092supp3_prod.pdf#page=27), [final SAP p67](../../../joi190092supp3_prod.pdf#page=67), [p68](../../../joi190092supp3_prod.pdf#page=68); final formula and table read visually.
- **Source value/text matched:** Prose says approximately 80% power to detect a difference of 17% when MMF success is .42.
- **Comparator matched:** 80% row .42/.17, n1=58/n0=38; summary says difference 25%, success probability 42%, same sample counts and two-tailed alpha .05.
- **Consistency rule applicable:** Absolute difference in two probabilities is their subtraction, distinct from either lower success probability. The displayed normal-CDF power formula permits an auxiliary scenario check.
- **Calculation/logical comparison reproduced:** .42−.17=.25, or 25 points. R reproduces source-formula power 0.802453166564 for .42/.17; literal 17-point difference .42/.25 gives 0.428097397721 under the same formula/counts. This diagnostic does not repair sequence alignment, separately registered elsewhere.
- **Necessary inputs available:** Explicit success probabilities, scenario counts, formula, alpha and prose/summary comparison.
- **Exact missing inputs/definitions:** Whether “difference 17%” means the lower success probability or a distinct omitted scenario; author-intended scenario alignment.
- **Source-grounded alternative interpretation:** 17% may name the lower-group probability rather than the difference; an unprinted alternative scenario could explain the prose.
- **Direct observation versus inferred explanation:** 17%, 25%, .42/.17 and table labels are observed; the suggested prose intent is inference. Powers are source-formula diagnostics, not observed trial inference.
- **Exact remaining human question:** Does 17% denote lower success probability or an absolute detectable difference, and which scenario did the prose intend?
- **Classification:** Numeric or arithmetic inconsistency; P_P; all P_P; PLAN original/final SAP prose versus PLAN table/summary. Historical planning values remain PLAN.
- **Evidence state:** `recorded_candidate`, determined by reproduced .42−.17=.25 and the conflicting printed difference descriptions.

## C053 — Country-interaction coefficient absent from named equation

- **Location found:** Yes: PLAN [original SAP p16 Equation 1](../../../joi190092supp3_prod.pdf#page=16), [p17 first paragraph](../../../joi190092supp3_prod.pdf#page=17), both visually inspected.
- **Source value/text matched:** Equation 1 contains intercept, treatment b1 and site terms b2i/b3i/b4i; null b1=0 with one-df LRT. It has no country-by-treatment b12 term.
- **Comparator matched:** Next page explicitly calls Wald T-test of b12=0 “in Equation (1)” for treatment-country interaction. The visual source confirms b12, not b1.
- **Consistency rule applicable:** A test coefficient assigned to an identified displayed equation must exist in that equation or a supplied equivalent parameterization.
- **Calculation/logical comparison reproduced:** Comparing the displayed term list to b12 shows no b12 or interaction term. Exploratory model (d) has country interaction but is not labeled Equation 1.
- **Necessary inputs available:** Displayed model, coefficient list, test coefficient, named equation and model descriptions.
- **Exact missing inputs/definitions:** Equation/model actually intended for b12 and its coefficient mapping.
- **Source-grounded alternative interpretation:** The test may intend exploratory model (d), or an omitted interaction term/model reference.
- **Direct observation versus inferred explanation:** Absence of b12 from printed Equation 1 is observed; intended model substitution is inferred.
- **Exact remaining human question:** Which supplied model and coefficient define the country-interaction test called b12 in Equation 1?
- **Classification:** Statistical reporting inconsistency; P_P; all P_P; PLAN original SAP equation versus PLAN next-page test statement.
- **Evidence state:** `recorded_candidate`, determined by the directly reproduced equation/coefficient identity mismatch.

## C054 — Zero interaction null and stated difference

- **Location found:** Yes: PLAN [original SAP p17](../../../joi190092supp3_prod.pdf#page=17), [final SAP p58](../../../joi190092supp3_prod.pdf#page=58), exact formulas visually confirmed.
- **Source value/text matched:** Anatomical term β3X3 and interaction β13X1X3 are added; the hypothesis is β13=0.
- **Comparator matched:** Both passages immediately explain this as “i.e. that there is a difference in treatment efficacy between the anatomic locations, controlling for country.” X3 codes the two anatomical groups 0/1.
- **Consistency rule applicable:** In this supplied interaction parameterization, a zero interaction means no difference in the treatment log-odds coefficient between X3=0 and X3=1.
- **Calculation/logical comparison reproduced:** Treatment coefficient is β1 for X3=0 and β1+β13 for X3=1; their difference is β13, zero under the named null. The “i.e.” statement describes a nonzero alternative instead.
- **Necessary inputs available:** Coding, added terms, zero hypothesis and interpretation.
- **Exact missing inputs/definitions:** Intended null-versus-alternative meaning of the explanatory prose; no fitted interaction output needed.
- **Source-grounded alternative interpretation:** Prose may intend “test whether there is a difference” or describe the alternative rather than equate it to the null.
- **Direct observation versus inferred explanation:** Formula/null/words are observed; stated coefficient difference is algebra; intended prose meaning remains inferred.
- **Exact remaining human question:** Does the difference prose describe the alternative, and how should its explicit equivalence to β13=0 be read?
- **Classification:** Statistical reporting inconsistency; P_P; all P_P; all compared content is prospective SAP material in the same bound bundle.
- **Evidence state:** `recorded_candidate`, determined by the observed zero-null versus nonzero-difference interpretation and reproduced algebra.

## C055 — Final SAP Equation 1 model reference

- **Location found:** Yes: PLAN [final SAP p57 primary model](../../../joi190092supp3_prod.pdf#page=57), [p58 subgroup](../../../joi190092supp3_prod.pdf#page=58), [p60 Bayesian item](../../../joi190092supp3_prod.pdf#page=60), [p61 continuation](../../../joi190092supp3_prod.pdf#page=61), and PLAN [original SAP p16 Equation 1](../../../joi190092supp3_prod.pdf#page=16).
- **Source value/text matched:** Final primary analysis uses treatment predictor and study-site random intercept; no displayed numbered Equation 1 is supplied there. Final subgroup says begin with Equation (1); Bayesian continuation uses likelihood corresponding to Equation (1).
- **Comparator matched:** Printed numbered Equation 1 in the bound SAP's original version uses fixed site coefficients. The final primary paragraph and literal displayed referent differ in site structure.
- **Consistency rule applicable:** A model-reference label should identify the intended parameterization, or state a mapping when final and original specifications differ.
- **Calculation/logical comparison reproduced:** Original displayed fixed-site equation and final random-intercept primary paragraph are distinct specifications; final references do not supply a matching numbered formula or explicit mapping. No fitted analysis output is reconstructed.
- **Necessary inputs available:** Original equation and final primary/subgroup/Bayesian references.
- **Exact missing inputs/definitions:** Final numbered equation or explicit mapping; whether subgroup/Bayesian analyses deliberately retained fixed-site specifications.
- **Source-grounded alternative interpretation:** “Equation 1” may informally mean the final primary model despite a stale number, or explicitly mean a retained fixed-site model for these analyses.
- **Direct observation versus inferred explanation:** Reference and specifications are observed; intended old versus final referent is unresolved, and no claim about the actual report model follows.
- **Exact remaining human question:** Does final “Equation 1” mean the final random-intercept model, the original fixed-site equation or a separate retained model for subgroup/Bayesian work?
- **Classification:** Measure, label, or scale inconsistency; P_P; all P_P; PLAN final/original SAP model references. The fixed-to-random amendment by itself is not the discrepancy.
- **Evidence state:** `recorded_candidate`, determined by the unmatched final model reference, pending its explicitly missing mapping.

## C056 — Twelve-month same-Wald/model assertion

- **Location found:** Yes: PLAN [original SAP p16 primary](../../../joi190092supp3_prod.pdf#page=16), [p18 twelve-month item](../../../joi190092supp3_prod.pdf#page=18), [final SAP p57 primary](../../../joi190092supp3_prod.pdf#page=57), [p58 twelve-month item](../../../joi190092supp3_prod.pdf#page=58).
- **Source value/text matched:** Both primary sections use treatment coefficient zero and one-df likelihood-ratio test; final primary treatment/site-random model has no anatomical interaction.
- **Comparator matched:** Both twelve-month sections say the same statistical model “(and Wald procedure)” as primary, then state that treatment and treatment/anatomic-location interaction coefficients both equal zero.
- **Consistency rule applicable:** A “same” model/procedure statement should match the referenced test and contrast; distinct LRT/Wald labels and single-versus-joint coefficient nulls do not identify the same printed procedure/contrast without explanation.
- **Calculation/logical comparison reproduced:** Primary named procedure is LRT, not Wald; primary null is one treatment coefficient, while twelve-month joint null includes anatomical interaction absent from the printed final primary model. No assertion that realized LRT and Wald P values must differ is used.
- **Necessary inputs available:** Model/test definitions, one-df primary null and explicit twelve-month joint null.
- **Exact missing inputs/definitions:** Twelve-month model and contrast, any primary Wald definition, and intended meaning of “same.”
- **Source-grounded alternative interpretation:** Twelve-month analysis may deliberately use an expanded anatomical-interaction model and Wald test while retaining an older “same” clause. A model can permit both tests, but the text does not specify this mapping.
- **Direct observation versus inferred explanation:** Printed test names and nulls differ; intended expansion or realized test output is unknown.
- **Exact remaining human question:** Which model and joint contrast define the twelve-month test, and is its Wald procedure deliberately different from the primary one-df LRT?
- **Classification:** Statistical reporting inconsistency; P_P; all P_P; PLAN primary versus PLAN twelve-month statements within both SAP versions.
- **Evidence state:** `recorded_candidate`, determined by reproduced printed procedure/contrast identity mismatch.

## C057 — Dose-reduction Fisher output and P precision

- **Location found:** Yes: REPORT [main p4 Fisher/two-sided methods](../../../jama_rathinam_2019_oi_190092.pdf#page=4), [p6 dose-reduction result](../../../jama_rathinam_2019_oi_190092.pdf#page=6), with overall arm denominators 107/109 also in p4 results.
- **Source value/text matched:** 21 (19.6%) versus 15 (13.8%) dose reductions, P=.27; main methods Fisher exact and two-sided P; original software R3.51 is listed.
- **Comparator matched:** Standard probability-ordering two-sided Fisher for displayed 21/107 and 15/109 gives .276681552078. Direct counts imply 86/94 complements. R4.5.2 `fisher.test` reproduced that value; exposed-MMF108 sensitivity gives .278466774702.
- **Consistency rule applicable:** Under the standard R two-sided Fisher convention and nearest-hundredth rounding, .27668 displays .28, not .27. This is explicitly conditional on tail and printing conventions; source does not state a nearest-rounding promise.
- **Calculation/logical comparison reproduced:** R calculation of the exact displayed 2×2 table and the alternative 108 denominator both round to .28 at nearest hundredth. Printed .27 is compatible with truncation of .27668. This is a small precision question, not a significance or conclusion claim.
- **Necessary inputs available:** Reduction numerators, displayed arm denominators/proportions, test label and P.
- **Exact missing inputs/definitions:** Exact analysis 2×2 table, original R call/version behavior, conditional-tail convention and truncation/rounding rule.
- **Source-grounded alternative interpretation:** P may have been truncated to two decimals; different inclusion or tail convention may have generated the display. Source does not identify which.
- **Direct observation versus inferred explanation:** Counts/P/test label are observed; the standard-convention exact P is an auxiliary reconstruction; a particular formatting mistake is not established.
- **Exact remaining human question:** What exact table, Fisher-tail convention and printing rule produced P=.27 for 21 versus 15 dose reductions?
- **Classification:** Statistical reporting inconsistency; S_W; all S_W; REPORT main methods versus REPORT main result. C049 has PLAN logistic versus REPORT Fisher as its different comparator and remains separate.
- **Evidence state:** `recorded_candidate`, determined by reproduced conditional same-table Fisher/nearest-rounding mismatch, with the unprovided printing convention explicitly preserved.

## Classification field handoff

| ID | Primary category | Relationship type | All relationships | Compared document roles | Evidence state |
|---|---|---|---|---|---|
| C039 | Cross-document numeric inconsistency | S_C | S_C | REPORT main p8 versus REPORT results p12 | record_input_error |
| C040 | Denominator, proportion, or total inconsistency | S_C | S_C | REPORT main p8 versus REPORT results p11 | record_input_error |
| C041 | Measure, label, or scale inconsistency | P_R | P_R, S_C | REPORT main p8 versus REPORT results p5 and PLAN protocol pp81/136 | recorded_candidate |
| C042 | Measure, label, or scale inconsistency | S_C | S_C | REPORT main p8 versus REPORT results pp6/14/15 | recorded_candidate |
| C043 | Measure, label, or scale inconsistency | P_R | P_R, S_C, S_W | REPORT main p8 and REPORT results pp14/15 versus REPORT results p5 and PLAN protocol p81 | recorded_candidate |
| C044 | Measure, label, or scale inconsistency | P_R | P_R | REPORT results p5 versus PLAN protocol p81 | not_reproduced |
| C045 | Measure, label, or scale inconsistency | P_R | P_R | REPORT main p8 and REPORT results pp5/14 versus PLAN protocol pp81/136 | recorded_candidate |
| C046 | Analysis-unit or population inconsistency | P_R | P_R | REPORT main pp6/7 versus PLAN original/final SAP pp31/71 | recorded_candidate |
| C047 | Statistical reporting inconsistency | P_R | P_R | REPORT main p4 versus PLAN final SAP p61 | recorded_candidate |
| C048 | Statistical reporting inconsistency | P_R | P_R | REPORT main pp4/6/7 versus PLAN final SAP p61 | recorded_candidate |
| C049 | Statistical reporting inconsistency | P_R | P_R | REPORT main pp4/6 versus PLAN final SAP p61 | recorded_candidate |
| C050 | Statistical reporting inconsistency | S_W | S_W | REPORT main p4 versus REPORT main p6 | recorded_candidate |
| C051 | Statistical reporting inconsistency | P_P | P_P | PLAN final SAP p61 versus PLAN final SAP pp46/57 | recorded_candidate |
| C052 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN original/final SAP pp26/67 prose versus PLAN pp27/68 table/summary | recorded_candidate |
| C053 | Statistical reporting inconsistency | P_P | P_P | PLAN original SAP p16 equation versus PLAN p17 coefficient test | recorded_candidate |
| C054 | Statistical reporting inconsistency | P_P | P_P | PLAN original/final SAP pp17/58 null versus PLAN same passages interpretation | recorded_candidate |
| C055 | Measure, label, or scale inconsistency | P_P | P_P | PLAN final SAP pp57/58/60/61 references versus PLAN original SAP p16 equation | recorded_candidate |
| C056 | Statistical reporting inconsistency | P_P | P_P | PLAN original/final SAP pp16/57 primary test versus PLAN pp18/58 twelve-month test | recorded_candidate |
| C057 | Statistical reporting inconsistency | S_W | S_W | REPORT main p4 methods versus REPORT main p6 result | recorded_candidate |

Coverage result: 19 of 19 assigned IDs; 16 recorded_candidate, 2 record_input_error, 1 not_reproduced. No missing-tool limitation. Source native-text glyph failures are explicitly corrected at C043/C044; rasters close confirmation gaps. Remaining human inputs are individually named in every card, especially field alignment C039/C040, actual rescue design C048, NI estimand C047/C051, adherence-test variable/dispersion C050, and Fisher printing rule C057.
