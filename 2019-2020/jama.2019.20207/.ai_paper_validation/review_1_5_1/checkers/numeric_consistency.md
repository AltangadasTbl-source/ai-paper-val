# Numeric Consistency Review

## Scope and method

This checker reviewed every canonical numeric relationship, N001 through N031, against the supplied direct PDFs and the complete main and support evidence maps. It applied applicable count, total, percentage, denominator, missingness, population, unit, label, scale, reference-group, rate-versus-count, duplicate-value, and cross-location arithmetic checks. Percentages printed to one decimal were assessed with a conventional display tolerance of plus or minus 0.05 percentage points when both numerator and denominator were explicit. Two-decimal displayed differences were assessed with plus or minus 0.015 in the stated unit when subtraction of rounded inputs was meaningful. Model-derived Kaplan-Meier estimates and mixed-model contrasts were not treated as raw ratios or simple arithmetic identities.

Direct observations and derived diagnostics are separated below. Candidate proposals are pending human adjudication and have no stable candidate identifiers.

## Relationship records

### N001 — Trial population and allocation

**Checker outcome: CONSISTENT.** Direct inputs: DOC-001, [PDF p. 1](<../../../jama_parsons_2020_oi_190140.pdf#page=1>) and [PDF p. 4](<../../../jama_parsons_2020_oi_190140.pdf#page=4>) print 478 randomized, 237 intervention, 241 control, 226 and 217 in the primary set, 443 total, and 91 sites. Calculations: 237 + 241 = 478; 226 + 217 = 443. The figure also gives 478 minus 35 exclusions = 443. Exact-count tolerance is zero. The same allocation and 443-primary-set values recur in DOC-002 [PDF p. 40](<../../../joi190140supp1_prod.pdf#page=40>) as planned design context and DOC-003 [PDF p. 3](<../../../joi190140supp2_prod.pdf#page=3>) as planned population context; those sources are not substituted for observed results. No candidate proposal.

### N002 — Main baseline age and PSA

**Checker outcome: CONSISTENT.** DOC-001 [PDF p. 1](<../../../jama_parsons_2020_oi_190140.pdf#page=1>) prints mean (SD) age 64 (7) years and PSA 4.9 (2.1) ng/mL among 478 randomized participants. DOC-001 [PDF p. 5](<../../../jama_parsons_2020_oi_190140.pdf#page=5>) repeats the pooled narrative values. These are rounded pooled descriptives, not quantities recoverable from the arm-specific Table 1 means without arm weights and complete individual data. No arithmetic identity or competing printed value requires a candidate.

### N003 — Eligibility thresholds

**Checker outcome: CANDIDATE PROPOSAL NP-01.**

- **Exact source locations and printed inputs:** DOC-001 [PDF p. 2](<../../../jama_parsons_2020_oi_190140.pdf#page=2>) defines the grade-group eligibility split as grade group 1 for men younger than 70 years and grade group 2 or less for men aged 70 years or older. DOC-002 [PDF p. 2](<../../../joi190140supp1_prod.pdf#page=2>) reports Update 10’s age-stratification change to 70 years or younger versus older than 70 years; DOC-002 [PDF pp. 15-16](<../../../joi190140supp1_prod.pdf#page=15>) and DOC-003 [PDF pp. 1-2](<../../../joi190140supp2_prod.pdf#page=1>) use the latter boundary for the corresponding Gleason eligibility definition.
- **Rule and calculation:** An exact-age-70 participant belongs to the older group under the main article’s “younger than 70” versus “70 years or older” rule, but belongs to the younger group under the support documents’ “70 years or younger” versus “older than 70” rule. The boundary-set comparison is {age <70}/{age >=70} versus {age <=70}/{age >70}; their only nonmatching value is age 70. This is a direct definition comparison, with zero tolerance.
- **Direct observation versus inference:** The incompatible printed boundary symbols/phrases are direct observations. The possibility that an age-70 participant could meet different eligibility pathology criteria is an inference from those definitions, not an assertion about an enrolled participant.
- **Alternative source-grounded interpretations:** The protocol/SAP may preserve an earlier or administrative version while the article reports the rule actually used; the Update 10 notation may have a document-version purpose. The supplied sources do not identify which age-70 rule governed all final eligibility determinations.
- **Quality-control relevance:** A data extractor could apply the wrong eligibility threshold at the age-70 boundary when reconstructing the analyzed population.
- **Exact human question:** Which age-boundary rule and corresponding pathology eligibility rule governed participants who were exactly 70 years old in the final trial analysis, and should the source documents be aligned or version-qualified?

### N004 — Randomization strata

**Checker outcome: CANDIDATE PROPOSAL NP-02.**

- **Exact source locations and printed inputs:** DOC-001 [PDF p. 2](<../../../jama_parsons_2020_oi_190140.pdf#page=2>) states randomization stratification by age “<70” versus “>=70” years. DOC-002 [PDF p. 2](<../../../joi190140supp1_prod.pdf#page=2>) states that Update 10 changed the age stratum to “<=70” versus “>70”; DOC-002 [PDF pp. 5 and 18](<../../../joi190140supp1_prod.pdf#page=5>) and DOC-003 [PDF pp. 1-2](<../../../joi190140supp2_prod.pdf#page=1>) retain the latter convention.
- **Rule and calculation:** The two printed partitions assign age 70 to different randomization strata: <70/>=70 assigns it to the second stratum, whereas <=70/>70 assigns it to the first. Boundary comparison has zero tolerance.
- **Direct observation versus inference:** The two boundary definitions are direct observations. Any effect on adjusted or stratified analysis is an inference and is not asserted.
- **Alternative source-grounded interpretations:** The protocol update may record a historical amendment and the main article may correctly state the implemented final allocation convention. No supplied source explicitly reconciles the final randomization implementation for age 70.
- **Quality-control relevance:** The stated stratification-factor label can be copied into trial metadata or used to reproduce an adjusted analysis.
- **Exact human question:** Was the final randomization age stratum <70/>=70 or <=70/>70, and which document should carry a version clarification for exactly 70-year-old participants?

### N005 — Intervention and assessment dose

**Checker outcome: CONSISTENT.** DOC-001 [PDF p. 3](<../../../jama_parsons_2020_oi_190140.pdf#page=3>) gives four phases with 6 + 4 + 4 + 8 calls; calculation 22 calls, exact-count tolerance zero. The 24-month duration, 22 calls, and baseline/12-/24-month dietary schedule are corroborated by DOC-002 [PDF pp. 26-30](<../../../joi190140supp1_prod.pdf#page=26>) and [PDF pp. 50-52](<../../../joi190140supp1_prod.pdf#page=50>). The plasma schedule is baseline and 12 months in the article, while the support documents separately describe various specimen schedules; these are not the same measure and create no numeric conflict.

### N006 — Composite progression definition

**Checker outcome: CANDIDATE PROPOSAL NP-03.**

**Later source recheck/pass-2 qualification:** This precursor proposal is retained as checker provenance, but the direct recheck found that the article, protocol p. 31, and SAP p. 2 endpoint definitions all use `<70`/`>=70`. The `<=70`/`>70` text is an eligibility rule on SAP p. 1, not the cited endpoint comparator. Stable C003 therefore uses the narrowed version-confirmation framing and records that the opposite endpoint-boundary comparison was not reproduced.

- **Exact source locations and printed inputs:** DOC-001 [PDF p. 3](<../../../jama_parsons_2020_oi_190140.pdf#page=3>) uses pathology progression thresholds of ISUP grade group >1 for those younger than 70 and >2 for those aged 70 or older. DOC-002 [PDF p. 31](<../../../joi190140supp1_prod.pdf#page=31>) and DOC-003 [PDF pp. 1-2](<../../../joi190140supp2_prod.pdf#page=1>) use the age boundary 70 years or younger versus older than 70 for their repeat-biopsy Gleason thresholds. All sources use PSA >=10 ng/mL and PSADT <3 years, so those components match.
- **Rule and calculation:** The age partitions <70/>=70 and <=70/>70 differ only at age 70. Thus the pathology component labels a 70-year-old in different threshold groups across matched progression definitions. Definition-comparison tolerance is zero.
- **Direct observation versus inference:** The divergent printed boundary is direct. The possibility of different progression classification at age 70 is derived; no individual-level outcome is supplied.
- **Alternative source-grounded interpretations:** The support documents may report a prior protocol rule, and the article may report the final operational definition. The source package does not explicitly state which definition was applied to age-70 participants in the analyzed endpoint.
- **Quality-control relevance:** This affects the reproducible label of a component of the composite endpoint, not an unqualified claim about the study result.
- **Exact human question:** Which age-specific pathology progression threshold was applied for participants exactly 70 years old in the final endpoint, and should the cross-document endpoint definitions be reconciled or version-labeled?

### N007 — PSADT computation

**Checker outcome: CONSISTENT.** DOC-001 [PDF p. 3](<../../../jama_parsons_2020_oi_190140.pdf#page=3>), DOC-002 [PDF p. 41](<../../../joi190140supp1_prod.pdf#page=41>), and DOC-003 [PDF p. 2](<../../../joi190140supp2_prod.pdf#page=2>) each specify log(2) divided by a least-squares slope of log PSA with at least three measures. Slight wording differences about the initial month-6 window versus later available values are complementary operational detail; no incompatible printed formula, unit, or time origin was found.

### N008 — Planned primary design

**Checker outcome: OBSERVATION.** DOC-001 [PDF p. 3](<../../../jama_parsons_2020_oi_190140.pdf#page=3>), DOC-002 [PDF p. 40](<../../../joi190140supp1_prod.pdf#page=40>), and DOC-003 [PDF p. 3](<../../../joi190140supp2_prod.pdf#page=3>) print planned 418 eligible participants, 57 events, at least 80% power, 20% versus 10% progression, 10% dropout, and target enrollment 464. The protocol allocation is 232 + 232 = 464, exact. The stated 18%-control-rate recalculation to 466 eligible in DOC-002 [PDF p. 42](<../../../joi190140supp1_prod.pdf#page=42>) is approximately 11.5% above 418 and is described as “about 11%”; this falls within the source’s explicitly approximate wording. HR 2.118 and HR 0.472 are approximate reciprocals after reversed reference-arm orientation (1 / 2.118 = 0.4721). No candidate proposal.

### N009 — Figure 1 flow

**Checker outcome: CONSISTENT.** Direct Figure 1 inputs in DOC-001 [PDF p. 4](<../../../jama_parsons_2020_oi_190140.pdf#page=4>) reconcile exactly: 602 - 124 = 478; 237 + 241 = 478; 237 - 11 = 226; 241 - 24 = 217; 226 + 217 = 443; and 11 + 24 = 35. Arm exclusion details also reconcile: 9 + 2 = 11 and 19 + 5 = 24. Exact-count tolerance is zero. No candidate proposal.

### N010 — Per-protocol completion

**Checker outcome: CANDIDATE PROPOSAL NP-04.**

- **Exact source locations and printed inputs:** DOC-001 [PDF p. 5](<../../../jama_parsons_2020_oi_190140.pdf#page=5>) states, “Of these 443 participants,” 183 intervention participants (81.7%) and 171 control participants (79.5%) met per-protocol criteria. The same page and Figure 1 on [PDF p. 4](<../../../jama_parsons_2020_oi_190140.pdf#page=4>) give the immediately relevant primary-set denominators: 226 intervention and 217 control.
- **Rule and calculation:** If “of these 443” means the displayed primary analysis arm denominators, 183 / 226 x 100 = 80.97%, which rounds to 81.0%, not 81.7%; 171 / 217 x 100 = 78.80%, which rounds to 78.8%, not 79.5%. Differences are 0.73 and 0.70 percentage points, exceeding the plus or minus 0.05 percentage-point one-decimal display tolerance. The count identities 226 - 43 = 183 and 217 - 46 = 171 are independently reproduced from the same page’s listed noncompletion reasons.
- **Direct observation versus inference:** Counts, printed percentages, and primary-set denominators are direct. The conclusion that the percentages were intended to use 226/217 is an inference from “of these 443”; no unreported percentage denominator is assumed.
- **Alternative source-grounded interpretations:** The percentages may use undisclosed denominators of 224 and 215, respectively, or the phrase “of these 443” may be imprecise while a different per-protocol evaluable population was used. The package does not state such denominators.
- **Quality-control relevance:** Completion percentages can be abstracted as adherence/fidelity outcomes and require a stated denominator to be reproducible.
- **Exact human question:** What denominators produced the printed 81.7% and 79.5% per-protocol completion percentages, and should the sentence identify those denominators or correct the percentages relative to 226 and 217?

### N011 — Table 1 baseline demographics

**Checker outcome: CANDIDATE PROPOSAL NP-05.**

- **Exact source locations and printed inputs:** DOC-001 Table 1, [PDF p. 5](<../../../jama_parsons_2020_oi_190140.pdf#page=5>), explicitly prints serum PSA denominators of intervention n=224 and control n=217. Under that heading, the only displayed categories are 0-2.5 ng/mL (25 and 30) and >2.5-5 ng/mL (99 and 98).
- **Rule and calculation:** The displayed PSA category counts total 25 + 99 = 124 intervention and 30 + 98 = 128 control, whereas their printed PSA denominators are 224 and 217. The residuals are 100 and 89 participants. Exact-count tolerance is zero. Unlike the race, region, and tumor-stage rows on the same table, no “other” or “remainder” PSA category is displayed or footnoted.
- **Direct observation versus inference:** The denominator, category labels, and counts are direct observations. The inference that higher PSA categories were omitted rather than intentionally excluded from a partial table is not established by the source.
- **Alternative source-grounded interpretations:** The table may intentionally display only PSA categories below or equal to 5 ng/mL, with all remaining values in an unprinted >5-to-<10 range consistent with eligibility. The supplied Table 1 does not label the PSA display as partial or provide that remainder category.
- **Quality-control relevance:** A baseline-characteristics extractor may regard the displayed categories as exhaustive because they sit under a stated n, producing a materially incomplete PSA distribution.
- **Exact human question:** Are the two printed PSA categories intentionally a partial distribution, and if so, should Table 1 identify the omitted PSA category or state that the rows do not exhaust n=224 and n=217?

The remaining Table 1 checks are consistent: race categories sum to 226 intervention and 216 control; region categories sum to 226 and 217; tumor-stage categories sum to 225 and 217. Their percentages agree with printed denominators within the one-decimal tolerance. Variable-specific denominators must not be homogenized to 226/217.

### N012 — Completion, censoring, biopsy, and narrative descriptors

**Checker outcome: CONSISTENT.** DOC-001 [PDF p. 5](<../../../jama_parsons_2020_oi_190140.pdf#page=5>) gives noncompletion reasons totaling 36 + 4 + 1 + 2 = 43 intervention and 34 + 4 + 3 + 5 = 46 control; subtraction from the displayed primary-set arms gives 183 and 171, respectively. Death counts 1 + 3 = 4 and elective-treatment withdrawals without progression 3 + 2 = 5 match their displayed totals. The 24-month biopsy percentages are reported without raw counts and therefore were not forced into a raw-count identity. The percentage-denominator inconsistency in the completion sentence is recorded once in N010, not duplicated here.

### N013 — Main composite events and 24-month progression-free percentages

**Checker outcome: CONSISTENT.** DOC-001 [PDF pp. 1 and 5](<../../../jama_parsons_2020_oi_190140.pdf#page=1>) prints 245 events, comprising 124 intervention and 121 control; 124 + 121 = 245 exactly. The 24-month 43.5% versus 41.4% Kaplan-Meier progression-free estimates have printed difference 2.1 percentage points; 43.5 - 41.4 = 2.1 within displayed precision. They are time-to-event estimates with censoring, not complements of 124/226 or 121/217; no rate-versus-count error is inferred. The 49 biopsy-only events also reconcile as 28 + 21 = 49.

### N014 — Active treatment

**Checker outcome: CONSISTENT.** DOC-001 [PDF p. 5](<../../../jama_parsons_2020_oi_190140.pdf#page=5>) prints total active treatment 6/226 (2.7%) intervention and 4/217 (1.8%) control. Calculations yield 2.65% and 1.84%, rounding to 2.7% and 1.8% within the one-decimal tolerance. The eight withdrawals and two additional post-protocol intervention treatments are correctly distinguished from the five elective-treatment withdrawals without clinical progression in the primary-outcome censoring description.

### N015 — Diet and plasma-carotenoid narrative changes

**Checker outcome: OBSERVATION.** The 12- and 24-month dietary values in DOC-001 [PDF pp. 5-6](<../../../jama_parsons_2020_oi_190140.pdf#page=5>) agree with the matched Table 2 values on [PDF p. 7](<../../../jama_parsons_2020_oi_190140.pdf#page=7>) at printed precision, including total vegetables and total carotenoids. Dietary counts at 12 and 24 months are not denominators for Kaplan-Meier progression estimates or plasma-carotenoid samples. The one narrative label/unit mismatch is recorded once in N017.

### N016 — Figure 2 risk sets and follow-up

**Checker outcome: CONSISTENT.** DOC-001 [PDF p. 6](<../../../jama_parsons_2020_oi_190140.pdf#page=6>) starts Figure 2A risk sets at 226 and 217 and Figure 2B at the same primary-set counts. Later risk sets decline over time and do not increase within an arm. These are numbers at risk, not event counts or a fixed common denominator; no subgroup-sum rule applies. The median follow-up values and IQR endpoints are correctly ordered.

### N017 — Main Table 2 labels, units, and rows

**Checker outcome: CANDIDATE PROPOSAL NP-06.**

- **Exact source locations and printed inputs:** In the correlative-outcomes narrative on DOC-001 [PDF p. 5](<../../../jama_parsons_2020_oi_190140.pdf#page=5>), the article says “cruciferous servings” and immediately prints mean changes 43.10 g/d versus 6.44 g/d. The matched Table 2 on DOC-001 [PDF p. 7](<../../../jama_parsons_2020_oi_190140.pdf#page=7>) labels those exact values as “Cruciferous, g/d.” A separate Table 2 row, “Cruciferous, servings/d,” contains different values (0.71 versus 0.12 at 12 months).
- **Rule and calculation:** A noun phrase identifying a serving-based measure should not label values printed in grams/day when a distinct servings/day row is present. The exact values 43.10 and 6.44 source-match the grams/day row, not the servings/day row. This is a direct measure-label comparison with zero tolerance; no arithmetic reconstruction is needed.
- **Direct observation versus inference:** The narrative wording, units, values, and the two table rows are direct. The explanation that the word “servings” is a copy-editing error is an inference.
- **Alternative source-grounded interpretations:** The narrative may use “cruciferous servings” colloquially while the adjacent g/d units deliberately identify the actual measure; no result value differs across locations.
- **Quality-control relevance:** A data extractor may enter a grams/day contrast as servings/day, creating an incorrect scale and unit in a secondary outcome record.
- **Exact human question:** Should the narrative phrase “cruciferous servings” be changed or qualified to “cruciferous vegetables” or another grams/day label so it matches the displayed g/d values and the Table 2 measure?

### N018 — Supplement-only vegetable juice and eFigure

**Checker outcome: CONSISTENT.** DOC-004 [PDF p. 2](<../../../joi190140supp3_prod.pdf#page=2>) gives vegetable-juice values only in the supplement; there is no falsely matched main-table row. The eFigure on [PDF p. 3](<../../../joi190140supp3_prod.pdf#page=3>) is graphical and prints axes but not summary statistics, so it cannot be used for numeric total or duplicate-value arithmetic. Shared eTable and Table 2 values match at printed precision; its N columns identify time-specific displayed sample counts, not a common all-outcome denominator.

### N019 — Main conclusion

**Checker outcome: CONSISTENT.** DOC-001 [PDF pp. 1, 6, and 8](<../../../jama_parsons_2020_oi_190140.pdf#page=1>) consistently states no significant reduction in clinical progression and notes possible underpowering. This agrees with the printed primary unadjusted HR 0.96 with 95% CI 0.75 to 1.24 and P=.76. No numeric or direction contradiction is present.

### N020 — MEAL pilot allocation and vegetable table

**Checker outcome: CANDIDATE PROPOSAL NP-07.**

- **Exact source locations and printed inputs:** DOC-002 [PDF p. 12](<../../../joi190140supp1_prod.pdf#page=12>) describes a randomized controlled MEAL pilot “of 74 men” with two intervention participants randomized for every one comparison participant. The same page’s Table 1 headers print Intervention n=45 and Control n=23.
- **Rule and calculation:** The table header counts sum to 45 + 23 = 68, six fewer than the narrative pilot total of 74. A 2:1 allocation description also does not itself explain a 45:23 analyzed split. Exact-count tolerance is zero.
- **Direct observation versus inference:** The total 74, allocation wording, and table n values are direct. An inference that six participants were excluded or lacked diet data is not supported by a stated table footnote or denominator description.
- **Alternative source-grounded interpretations:** Table 1 may intentionally represent a six-month dietary-recall subset or complete cases, while the narrative refers to all randomized pilot participants. The supplied page does not state this population distinction.
- **Quality-control relevance:** The denominator determines interpretation of feasibility dietary changes and the quoted pilot allocation.
- **Exact human question:** Do Table 1’s n=45 and n=23 represent an evaluable subset of the 74 randomized pilot participants, and if so, what happened to the other six and where is that denominator definition stated?

### N021 — Pilot nonvegetable and carotenoid changes

**Checker outcome: OBSERVATION.** DOC-002 [PDF p. 13](<../../../joi190140supp1_prod.pdf#page=13>) prints percentages calculated from underlying data while baseline and six-month means are rounded. For example, recalculations from displayed two-decimal means may differ slightly from printed percent change. With no unrounded inputs or matched contradictory value, these are rounding-sensitive observations, not candidate proposals. Units are explicitly mmol/L in Table 2 and are not confused with the main article’s dietary micrograms/day outcomes.

### N022 — Pilot subgroup, satisfaction, and planned enrollment

**Checker outcome: CONSISTENT.** DOC-002 [PDF pp. 13-14](<../../../joi190140supp1_prod.pdf#page=13>) prints AS subgroup 53% and satisfaction n=33 with rating-5 counts 31, 30, 32, 29, 26, 25, and 24; each count is no greater than 33. Planned enrollment race counts 3 + 9 + 1 + 54 + 397 + 0 = 464, while 447 non-Hispanic plus 17 Hispanic = 464. Exact-count tolerance is zero. No candidate proposal.

### N023 — Protocol outcome and assessment schedule

**Checker outcome: CONSISTENT.** DOC-002 [PDF pp. 15 and 20-25](<../../../joi190140supp1_prod.pdf#page=15>) supplies planned operational schedules and endpoint definitions. PSA every three months and 24-month follow-up match the main article’s reported methods. Biopsy exemption after definitive treatment describes a denominator condition rather than an inconsistent biopsy count. No candidate proposal.

### N024 — Biospecimens and tissue substudy

**Checker outcome: CONSISTENT.** DOC-002 [PDF pp. 21-24 and 35-38](<../../../joi190140supp1_prod.pdf#page=21>) specifies 1 x 10-mL specimen volumes and assay quantities. The tissue power input n=334 is the displayed rounded product of 418 x 0.80 = 334.4; rounding to a whole-participant planning number is appropriate. Sample types, volumes, and timepoints are distinct from plasma-outcome analytic counts, so no inappropriate denominator equality is assumed.

### N025 — QOL instruments and scales

**Checker outcome: CONSISTENT.** DOC-002 [PDF pp. 25 and 29-34](<../../../joi190140supp1_prod.pdf#page=25>) and DOC-003 [PDF pp. 6-10](<../../../joi190140supp2_prod.pdf#page=6>) give instrument item counts, ranges, timepoints, transforms, and higher-is-favorable direction. The SAP’s stated transformation to 0-100 distinguishes transformed summary scores from native item scales. No duplicate scale or inverse-direction inconsistency was identified in the supplied quantitative results.

### N026 — Correlative genetic and tissue predictors

**Checker outcome: CONSISTENT.** DOC-002 [PDF pp. 35-40](<../../../joi190140supp1_prod.pdf#page=35>) reports planned correlative endpoints and power inputs, not observed result estimates. The n=334 calculation is addressed in N024. No observed rate, risk, count, or effect label is incorrectly conflated with these planned biomarker quantities.

### N027 — Interim and recalculation quantities

**Checker outcome: OBSERVATION.** DOC-002 [PDF p. 42](<../../../joi190140supp1_prod.pdf#page=42>) specifies a first superiority interim at 80 progressions or 2-year completion and a recalculation at 400 enrolled. The protocol’s 18% example specifies 466 eligible participants, “about 11%” over 418: (466 - 418) / 418 x 100 = 11.48%, consistent with the qualified wording. Its HR=0.472 is compatible with the inverse of the p.40 HR=2.118 under reversed reference-arm orientation. The separate one-sided superiority/futility decision rules are planned definitions; no raw total or probability identity establishes a candidate.

### N028 — Consent schedule and optional samples

**Checker outcome: CONSISTENT.** DOC-002 [PDF pp. 50-57](<../../../joi190140supp1_prod.pdf#page=50>) describes consent and optional-substudy volumes/timing. “About 464” in consent is compatible with the protocol target of 464, and the 22 calls over two years match the main intervention schedule. Teaspoon volumes apply to a separate optional study and are not a contradictory measure of the 10-mL protocol specimens.

### N029 — SAP population and pathology rule

**Checker outcome: OBSERVATION.** DOC-003 [PDF pp. 3-5 and 9](<../../../joi190140supp2_prod.pdf#page=3>) distinguishes ITT from modified ITT and records final use of local pathology after central follow-up discrepancies. The observed primary set 443 equals the article’s 226 + 217 and is compatible with excluding 35 participants after randomization. The exact-age-70 endpoint-boundary comparison is proposed once in N006; it is not duplicated here. No additional population total mismatch was found.

### N030 — SAP alpha, multiplicity, missing-data, and transformations

**Checker outcome: CONSISTENT.** DOC-003 [PDF pp. 7-10](<../../../joi190140supp2_prod.pdf#page=7>) describes planned alpha, multiplicity, missing-data, and transformation rules. These are not competing observed estimates. No P=0 display occurs in the supplied scope, and no rate/count, unit, or scale contradiction is created by the stated rules.

### N031 — No-applicable support units

**Checker outcome: CONSISTENT.** DOC-002 PDF pages 1, 3-4, 6, 19, 43-49, 53-56, and 58-60; DOC-003 [PDF p. 11](<../../../joi190140supp2_prod.pdf#page=11>); DOC-004 [PDF p. 1](<../../../joi190140supp3_prod.pdf#page=1>); and DOC-005 [PDF p. 1](<../../../joi190140supp4_prod.pdf#page=1>) contain only administrative, cover, consent-administrative, or references material beyond separately mapped schedules/definitions. No result-relevant quantitative relationship or duplicate result was found there.

## Candidate-proposal count and limitations

Seven distinct candidate proposals were emitted: NP-01 through NP-07. They concern three exact-age-70 definition mismatches, one per-protocol percentage-denominator mismatch, one incomplete displayed PSA distribution, one narrative unit/measure-label mismatch, and one pilot total-versus-table-denominator mismatch. No stable candidate identifier has been assigned.

Limitations: protocol and SAP documents may preserve versioned planned definitions rather than final implemented ones; the package does not provide individual-level data, unrounded pilot means, or an explicit denominator for the pilot dietary table or the per-protocol percentages. These limitations are included in the relevant human questions and do not erase the printed comparisons.
