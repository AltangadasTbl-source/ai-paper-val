# Mechanical evidence recheck — Workflow 1.6.2

Fresh evidence rechecker: `/root/evidence_recheck`, gpt-6.1-sol/high. Assigned stable scope: C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017. The complete scope, review contract, current ledger, initial screening record, inventory and tooling record were read. The included checker facts were read in their ledger provenance sections. Every affected source location below was independently read from its current direct-source page render or, for the workbook, directly from the supplied ZIP's worksheet and shared-string XML. Text/OCR conclusions were not final authority.

Source identity and roles, confirmed from the compared content:

| Source | Exact supplied source | Role | Reason |
|---|---|---|---|
| DOC-001 | [Main article](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=3) | REPORT | Published methods and trial results. |
| DOC-002 | [Protocol](../../../joi250046supp1_prod_1755300121.14087.pdf#page=43) | PLAN | Prospective intervention and analysis specifications. |
| DOC-003 | [SAP](../../../joi250046supp2_prod_1755300121.15087.pdf#page=19) | PLAN | Prospective analysis specification and dated amendments. |
| DOC-004 | [TIDieR intervention description](../../../joi250046supp3_prod_1755300121.15087.pdf#page=3) | REPORT | Published description of performed interventions, including received sessions; not a prospective manual. |
| DOC-005 | [Results and methods supplement](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4) | REPORT | Reported fitted models, supplementary results and retrospective analysis descriptions. |
| DOC-006 | [Supplied workbook](../../../joi250046supp5_prod_1755300121.16087.xlsx) | REPORT | Reported baseline and selection statistics; worksheet is exactly `eTable 3`. |

Visual confirmation covered DOC-001 physical PDF pages 3, 4, 5, 9, 10, 11; DOC-002 pages 43, 44, 56, 57; DOC-003 pages 4, 19, 20, 21; DOC-004 pages 3, 4; DOC-005 pages 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 17, 18: 28 distinct PDF pages. Existing current-run renders came from the recorded pinned PyMuPDF 1.26.4 fallback, CPU, under preprocessing/{numeric_review,initial_screen,protocol_b_restart,sap_restart,cross_source_review,stat1_reports,stat1_raw}. No new PDF/OCR derivative was necessary. Direct workbook commands were `unzip -p` on xl/workbook.xml, xl/worksheets/sheet1.xml and xl/sharedStrings.xml, with Perl used only to display exact targeted XML values. No recalculation, extra Python, web input, source modification or reused-artifact modification occurred.

For calculations, a displayed input receives its own half-unit interval. A recomputed output interval is compared with the displayed output's half-unit interval. Relative discrepancy is the nonoverlap gap divided by the absolute displayed output, or the reference copy for paired printed copies. Route A category 1 is exempt from rounding-based removal. Logical model/specification comparisons have no numerical precision interval. These evidence facts do not assign a disposition.

| ID | Review domain | Relationship type | All relationships | Evidence state | Classification recheck |
|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R | reproduced | Confirmed; agreeing main and TIDieR do not add S_C. |
| C002 | statistical_results | S_W | S_W | reproduced | Confirmed main internal arithmetic. |
| C003 | statistical_results | S_W | S_W | reproduced | Confirmed main internal method/contrast construction. |
| C004 | statistical_results | S_W | S_W | reproduced | Confirmed separate within-report patterns; no conflicting cross-document copy. |
| C005 | protocol_report | P_R | P_R, S_C, S_W | reproduced | Confirmed; report/plan, main/supplement and supplement-internal specification differences. |
| C006 | protocol_report | P_R | P_R | reproduced | Confirmed; secondary adjustment report/plan difference. |
| C007 | protocol_report | P_R | P_R, P_P | reproduced | Confirmed; retained primary-MAR wording differs from report and amended plan branch. |
| C008 | statistical_results | S_W | S_W | reproduced | Confirmed; matched main intervals, with interval-method ambiguity retained. |
| C009 | statistical_results | S_W | S_W | reproduced | Confirmed main point containment. |
| C010 | statistical_results | S_W | S_W | reproduced | Confirmed main repeated point containment. |
| C011 | statistical_results | S_W | S_W | reproduced | Confirmed supplement model attribution/adjustment difference. |
| C012 | statistical_results | S_W | S_W | reproduced | Confirmed supplement predictor membership; workbook corroboration only. |
| C013 | statistical_results | S_W | S_W | reproduced | Confirmed supplement model coding; workbook corroboration only. |
| C014 | statistical_results | S_W | S_W | reproduced | Confirmed supplement interval/P pattern; main alpha corroboration only. |
| C015 | statistical_results | S_W | S_W | reproduced | Confirmed supplement header nesting. |
| C016 | statistical_results | S_W | S_W | reproduced | Ledger confirmed; screen-group S_C characterization needs alignment to S_W because main scale definition is corroborating context. |
| C017 | statistical_results | S_W | S_W | reproduced | Confirmed workbook internal count/denominator arithmetic. |

## C001 — Planned versus reported online session duration

- **Location found:** Yes, all five locations: REPORT [main p.3, Health Coach Program and Online Program](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=3); PLAN [protocol p.43 §10.1.1](../../../joi250046supp1_prod_1755300121.14087.pdf#page=43) and [p.44 coach overview](../../../joi250046supp1_prod_1755300121.14087.pdf#page=44); REPORT [TIDieR p.3 Procedures](../../../joi250046supp3_prod_1755300121.15087.pdf#page=3) and [p.4 When and How Much](../../../joi250046supp3_prod_1755300121.15087.pdf#page=4).
- **Source text matched:** Main online session expectation is approximately 30–45 minutes; TIDieR prints 30–45 minutes each at both cited rows. Main/TIDieR coach expectation is 45–60 minutes. The main and TIDieR also identify eight sessions and intended completion over 12 weeks.
- **Comparator matched:** Protocol p.43 says each online session takes 45–60 minutes; p.44 coach sessions take 60 minutes. Both identify eight sessions and approximately weekly completion. The coach comparison overlaps and is context, not an additional duration discrepancy.
- **Consistency rule applicable:** Focus D, Route B, permitted randomized-intervention duration comparison. Matching range endpoints describe different extracted expected session doses.
- **Calculation reproduced, including precision:** Lower endpoints 45 versus 30 have intervals [44.5,45.5] and [29.5,30.5], gap 14, relative 14/45=.311111. Upper endpoints 60 versus 45 have [59.5,60.5] and [44.5,45.5], gap 14, relative 14/60=.233333. These calculations compare corresponding stated endpoints; they do not claim the two duration ranges have no overlap.
- **Necessary inputs available:** Session counts, stated duration ranges, intervention identity, self-pacing and pause/resume description. **Exact missing inputs/definitions:** Whether the ranges are planned content duration, anticipated self-paced completion time or observed completion time; any duration-specific amendment.
- **Source-grounded alternative interpretation:** The self-paced protocol permits stopping and resuming. A changed practical estimate or a planned-versus-observed duration convention may explain the shorter range without changed content.
- **Direct versus inferred:** Different printed range endpoints are directly observed. A revised treatment dose or content is an unestablished explanation.
- **Classification:** Roles above confirmed by content. Primary/all relationships P_R; domain protocol_report. Main and TIDieR agree, so there is no S_C relationship. No role ambiguity; expected-versus-delivered convention remains substantive ambiguity.
- **Evidence state:** reproduced. Determining fact: correctly read corresponding online endpoints remain separated above .05 after display precision.
- **Exact remaining human question:** Does 30–45 versus 45–60 minutes describe revised online session content/dose, actual completion time or different duration conventions, and which planned and delivered duration should be extracted?

## C002 — Therapeutic-dose adherence percentage

- **Location found:** Yes: REPORT [main p.4 Results adherence paragraph](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4) and [p.5 Figure 1 PT allocation/session counts](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=5).
- **Source text matched:** Of those randomized to painTRAINER, 371 (43%) completed at least six sessions; 527 (68%) completed at least one.
- **Comparator matched:** Figure 1: PT randomized 776; completed 6–8 sessions 371, 1–5 sessions 156, none 249. The category counts sum to 776, and 371+156=527.
- **Consistency rule applicable:** Focus A; Route A category 3, count/denominator/percentage reconciliation for the same adherence description.
- **Calculation reproduced, including precision:** 100×371/776=47.809278%. Half-unit inputs give [100×370.5/776.5,100×371.5/775.5]=[47.714102,47.904578]%. Printed 43% gives [42.5,43.5]%. Gap 4.214102 points; relative .098002. Initiator denominator 527 would give 70.398482%, not 43%.
- **Necessary inputs available:** Randomized denominator, exact dose-category numerator and repeated figure count. **Exact missing inputs/definitions:** Any other denominator or category underlying 43%.
- **Source-grounded alternative interpretation:** The percentage could refer to an unstated denominator or adherence category; the repeated numerator and explicitly randomized wording do not identify either.
- **Direct versus inferred:** The printed inputs and arithmetic discrepancy are direct. The source-production mechanism is unknown.
- **Classification:** Both locations REPORT in one article; primary/all relationships S_W; domain statistical_results. Confirmed; no classification ambiguity.
- **Evidence state:** reproduced. Determining fact: the directly confirmed numerator and randomized denominator give a percentage interval disjoint from 43% by relative gap .098002.
- **Exact remaining human question:** Which numerator, denominator and percentage represent randomized painTRAINER participants completing at least six sessions?

## C003 — SMD construction across Table 3

- **Location found:** Yes: REPORT [main p.4 SMD definition](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), [p.10 Table 3](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), and [p.11 continuation and footnote d](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11). All twenty registered outcome/time rows and all three point-contrast columns per row were read directly.
- **Source text matched:** The adjusted between-group mean difference is divided by the SD of change in the usual-care-plus group at the given outcome/time. Footnote d repeats the common UC denominator.
- **Comparator matched:** The complete printed SMD triples, and MD triples needed for the additional scaling/sign manifestations, appear below. Contrasts are PT−UC / HC−UC / HC−PT. PGIC rows are p.11; other rows p.10.
- **Consistency rule applicable:** Focus B/C, stated method construction; Route A category 4 for the consolidated pattern, with Route B for the additive component. For common adjusted means and one positive SD, b=a+c. This compares model contrasts with model contrasts, not adjusted results with crude group ratios.
- **Calculation reproduced, including precision:** Each printed two-decimal SMD has ±.005. Recomputed b=a+c has ±.010; displayed b has ±.005. Gap=max(0,|b−a−c|−.015). The table gives every additive manifestation, including its reference denominator |b|.

| Outcome/time | a: PT−UC | b: HC−UC | c: HC−PT | Recomputed b interval | Displayed b interval | Gap | Gap/absolute b |
|---|---:|---:|---:|---|---|---:|---:|
| Severity 3 months | −.25 | −.34 | −.13 | [−.390,−.370] | [−.345,−.335] | .025 | .073529 |
| Intensity 6 months | −.17 | −.27 | −.04 | [−.220,−.200] | [−.275,−.265] | .045 | .166667 |
| Intensity 12 months | −.16 | −.27 | −.03 | [−.200,−.180] | [−.275,−.265] | .065 | .240741 |
| Interference 3 months | −.25 | −.34 | −.13 | [−.390,−.370] | [−.345,−.335] | .025 | .073529 |
| Interference 6 months | −.27 | −.37 | −.14 | [−.420,−.400] | [−.375,−.365] | .025 | .067568 |
| Social 3 months | .12 | .01 | .20 | [.310,.330] | [.005,.015] | .295 | 29.500000 |
| Social 6 months | .18 | .06 | .26 | [.430,.450] | [.055,.065] | .365 | 6.083333 |
| Social 12 months | .19 | .07 | .27 | [.450,.470] | [.065,.075] | .375 | 5.357143 |
| Physical 3 months | .09 | −.02 | .16 | [.240,.260] | [−.025,−.015] | .255 | 12.750000 |
| Physical 6 months | .15 | .02 | .22 | [.360,.380] | [.015,.025] | .335 | 16.750000 |
| Physical 12 months | .20 | .07 | .27 | [.460,.480] | [.065,.075] | .385 | 5.500000 |
| PGIC pain 3 months | −.62 | −.62 | −.37 | [−1.000,−.980] | [−.625,−.615] | .355 | .572581 |
| PGIC pain 6 months | −.54 | −.55 | −.29 | [−.840,−.820] | [−.555,−.545] | .265 | .481818 |
| PGIC pain 12 months | −.55 | −.57 | −.29 | [−.850,−.830] | [−.575,−.565] | .255 | .447368 |
| PGIC general 3 months | −.66 | −.66 | −.40 | [−1.070,−1.050] | [−.665,−.655] | .385 | .583333 |
| PGIC general 6 months | −.46 | −.50 | −.24 | [−.710,−.690] | [−.505,−.495] | .185 | .370000 |
| PGIC general 12 months | −.53 | −.58 | −.28 | [−.820,−.800] | [−.585,−.575] | .215 | .370690 |

The remaining three registered rows have additive triples compatible with precision but fail MD/SMD scaling. With k=1/SD, k is constrained by |PT−UC SMD|/|PT−UC MD|. One-decimal MDs have ±.05; two-decimal SMDs have ±.005. The HC−PT MD is printed 0.0, giving [−.05,.05]. Its largest possible standardized magnitude is .05×(|a|+.005)/(|PT−UC MD|−.05).

| Outcome/time | Printed MD triple | Printed SMD triple | Recomputed HC−PT SMD interval | Displayed HC−PT interval | Gap | Relative gap |
|---|---|---|---|---|---:|---:|
| Severity 12 months | −.4 / −.4 / 0.0 | −.25 / −.36 / −.11 | [−.036429,.036429] | [−.115,−.105] | .068571 | .623377 |
| Intensity 3 months | −.3 / −.3 / −0.0 | −.21 / −.29 / −.08 | [−.043000,.043000] | [−.085,−.075] | .032000 | .400000 |
| Interference 12 months | −.5 / −.5 / 0.0 | −.26 / −.37 / −.12 | [−.029444,.029444] | [−.125,−.115] | .085556 | .712963 |

Additional sign manifestations within already-listed rows were confirmed: physical 3-month HC−UC MD .7 [ .65,.75 ] versus SMD −.02 [−.025,−.015]; physical 6-month HC−PT MD −.3 [−.35,−.25] versus SMD .22 [.215,.225]; physical 12-month HC−PT MD −.1 [−.15,−.05] versus SMD .27 [.265,.275]; PGIC pain 12-month HC−PT MD .1 [.05,.15] versus SMD −.29 [−.295,−.285]. A positive SD cannot reverse these signs. Additive manifestations in the table already independently satisfy the numeric precision threshold for these rows.

The same construction gives a precision-compatible reference at severity 6 months: MD −.4/−.5/−.1 and SMD −.26/−.36/−.12. From PT−UC, k∈[.255/.45,.265/.35]=[.566667,.757143]; predicted HC−UC SMD∈[−.416429,−.255], overlapping [−.365,−.355]; predicted HC−PT∈[−.113571,−.028333], gap to [−.125,−.115] .001429/.12=.011905. Its additive identity gap is .005: predicting HC−UC from the other two SMDs yields relative gap .005/.36=.013889; predicting HC−PT yields [−.110,−.090] against [−.125,−.115], relative gap .005/.12=.041667. Both remain within the .05 display-precision tolerance. This supports the same-display reproduction premise without supplying an absolute SD.

- **Necessary inputs available:** All point contrasts, their displayed precision, common-denominator definition and contrast headings. **Exact missing inputs/definitions:** Actual UC change SD by outcome/time; exact fitted contrasts; unrounded values; any distinct standardizers or separate-model assignments. These are needed for replacement values, not the reproduced identities.
- **Source-grounded alternative interpretation:** Contrast-specific standardizers, distinct model fits or a displaced outcome/contrast assignment could explain some SMDs, but differ from the printed common-denominator definition and require explicit mapping.
- **Direct versus inferred:** All printed point comparisons and algebraic failures under the stated definition are direct. A column displacement or production mechanism is unestablished. No covariance, degrees of freedom or pairwise test has been reconstructed.
- **Classification:** All compared content is REPORT within DOC-001; primary/all relationships S_W; domain statistical_results. Confirmed; no role ambiguity. One repeated construction pattern contains all twenty rows.
- **Evidence state:** reproduced. Determining fact: seventeen directly read triples exceed .05 after precision, and the other three fail the same MD/SMD scaling by relative gaps .623377, .400000 and .712963.
- **Exact remaining human question:** Which adjusted mean differences, positive usual-care change SDs and outcome/time/contrast assignments produced every registered SMD triple, and does the printed common-SD definition apply to all Table 3 rows?

## C004 — Reciprocal NNT point-reproduction pattern

- **Location found:** Yes: REPORT [main p.4 NNT definition](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); REPORT [main p.9 Table 2 severity 6-month HC/UC, interference 6-month HC/UC and footnote d](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9); REPORT [results p.14 eTable 8 reminder-letter 6-month PT/UC and footnote d](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14). All three affected rows were read.
- **Source values matched:** NNT points are 8, 7 and 8 respectively. **Comparator matched:** Corresponding adjusted percentages are 37.1/22.9, 40.9/24.3 and 35.6/21.3. Each local footnote defines one over the adjusted response-proportion difference.
- **Consistency rule applicable:** Focus C; Route A category 4. NNT=100/(percentage-point difference), with percentage inputs ±.05 and integer point ±.5. These are adjusted proportions, not crude counts.

| Exact affected row | Difference interval | Recomputed NNT interval | Printed NNT interval | Gap | Relative gap |
|---|---|---|---|---:|---:|
| Main severity 6-month HC/UC, 37.1−22.9 | [14.1,14.3] | [6.993007,7.092199] | [7.5,8.5] | .407801 | .050975 |
| Main interference 6-month HC/UC, 40.9−24.3 | [16.5,16.7] | [5.988024,6.060606] | [6.5,7.5] | .439394 | .062771 |
| Reminder-letter subset 6-month PT/UC, 35.6−21.3 | [14.2,14.4] | [6.944444,7.042254] | [7.5,8.5] | .457746 | .057218 |

- **Calculation reproduced:** The three reciprocal intervals above independently match the registered calculations. Same-display comparators also support the rule: main severity 12-month HC/UC 38.3−27.1 yields [8.849558,9.009009], overlapping printed 9 [8.5,9.5]; reminder-letter 3-month PT/UC 31.6−20.5 yields [8.928571,9.090909], overlapping printed 9 [8.5,9.5]. Main severity 3-month PT/UC 26.6−20.8 yields [16.949153,17.543860], overlapping printed 18 [17.5,18.5].
- **Necessary inputs available:** Adjusted rates, integer points, contrast matching and reciprocal definition. **Exact missing inputs/definitions:** Unrounded adjusted risk differences, integer reporting convention and any alternative point formula.
- **Source-grounded alternative interpretation:** Upward integer rounding could explain allthree points, including the supplementary row: the true reciprocal permitted by source half-unit percentage inputs can reach7.04225352, whose ceiling is8, while the printed-center reciprocal6.99300699 has ceiling7. An undisplayed modeled RD could differ from the displayed rate difference. The stated half-unit rule still leaves all three printed points above the threshold; no alternative formula is supplied.
- **Direct versus inferred:** Printed reciprocal nonreproduction is direct. Upward rounding or another RD is an explanation, not an observed implementation.
- **Classification:** Both main and supplement are REPORT. Each mismatch compares a row with its own local rate/NNT rule; the documents do not print conflicting copies of the same analysis. Primary/all relationships S_W; domain statistical_results. Confirmed; multiple report documents alone do not create S_C.
- **Evidence state:** reproduced. Determining fact: all three locally matched point calculations remain disjoint above relative .05.
- **Exact remaining human question:** Which unrounded adjusted risk differences and integer-reporting rule produced these three NNT points?

## C005 — Age as a prespecified base adjustment covariate

- **Location found:** Yes: PLAN [protocol p.56 §15.5](../../../joi250046supp1_prod_1755300121.14087.pdf#page=56); PLAN [SAP p.20 §§13–14](../../../joi250046supp2_prod_1755300121.15087.pdf#page=20); REPORT [main p.4 adjustment sentence](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); REPORT results [p.4 Adjustment](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4), [p.7 eTable 2 all-model variables](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7), [p.8 eTable 3 age](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8), [p.9 eTable 4 age](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9), [p.10 eTable 5 age](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10); REPORT [workbook](../../../joi250046supp5_prod_1755300121.16087.xlsx), `eTable 3` G2, A10, G10, directly decoded.
- **Source text matched:** Supplement p.4 first lists six planned factors, then describes a prespecified base set containing seven, including age. eTable 2 includes age ≥65 versus <65 in all models. Age coefficients are .19 (.12,.27), RR 1.15 (1,1.33) and OR .97 (.70,1.35). G2 shared string 138 reads Pre-specified Adjustment Variables; A10 string 4 reads Age in years; G10 string 146 is X.
- **Comparator matched:** Protocol/SAP primary lists and main list contain baseline severity, sex, site, residence, multisite pain and mental-health condition, without age. SAP §13 names age as a candidate baseline variable and subgroup factor; it does not make age a fixed factor in §14's primary list.
- **Consistency rule applicable:** Focus D, Route A category 5, reported prespecification versus supplied explicit plan specification; additionally the report descriptions differ.
- **Logical comparison reproduced, including precision:** Itemwise six-factor versus seven-factor sets differ exactly by age. Numeric coefficient equality is not the rule here. No arithmetic precision interval or relative discrepancy is applicable to membership/prespecification.
- **Necessary inputs available:** All cited lists, reported coefficients, workbook selection flag and prospective document identity. **Exact missing inputs/definitions:** A prospective statement establishing age as a fixed primary adjustment term; final main-model covariate vector and timing of age's addition.
- **Source-grounded alternative interpretation:** The generic baseline candidate list may have been intended to permit age selection; the base-set wording may use prespecified broadly; another amendment may have specified age. Its use is directly supported, its prespecification is unresolved.
- **Direct versus inferred:** List membership and fitted age terms are direct. Selection timing is not inferred from the age coefficients.
- **Classification:** All roles above confirmed. Primary P_R; all P_R, S_C, S_W; domain protocol_report. P_R contrasts prospective six-factor lists with reported age-as-base specification; S_C contrasts main six-factor list with supplement/workbook; S_W contrasts the two explicit supplement p.4 lists. Protocol and SAP agree, so P_P is absent. Highest-precedence P_R is retained.
- **Evidence state:** reproduced. Determining fact: source-confirmed report language and workbook flag call age prespecified/base despite its absence from the explicit supplied primary lists.
- **Exact remaining human question:** Which prospective specification made age a fixed primary covariate, and was age included in the main-result model as prespecified or subsequently added?

## C006 — Secondary-analysis adjustment specification

- **Location found:** Yes: PLAN [protocol p.57 §15.6](../../../joi250046supp1_prod_1755300121.14087.pdf#page=57); PLAN [SAP p.21 §15](../../../joi250046supp2_prod_1755300121.15087.pdf#page=21); REPORT [main p.4 secondary methods](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), [p.10 Table 3](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) and [p.11 continuation](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11).
- **Source text matched:** Report applies the same modeling structures as the primary analysis with added adjustment for the given baseline secondary outcome. The primary paragraph names multisite pain and mental-health condition as well as baseline severity and stratification factors.
- **Comparator matched:** Both plans say secondary analyses follow the same proposed approach as Aim 1; their explicit final secondary covariate sentence names baseline pain severity and all stratification variables, without the given baseline secondary-outcome value.
- **Consistency rule applicable:** Focus D, Route B, planned/reported adjustment of named secondary estimates. The outcome-specific baseline addition is the clearest explicit unmatched specification.
- **Logical comparison reproduced, including precision:** Baseline severity and strata match; the report expressly adds each baseline secondary outcome. Importing multisite/mental-health factors is plausible under both inheritance phrases and is retained as ambiguity, not treated as an established exclusion from the plans. No numerical rounding interval applies to covariate sets.
- **Necessary inputs available:** Both explicit secondary lists, inheritance language, main primary paragraph and secondary-result headings. **Exact missing inputs/definitions:** Planned and implemented per-outcome covariate vectors; how baseline adjustment applies to PGIC items that measure change; any prospective expansion statement.
- **Source-grounded alternative interpretation:** The general same-approach language might import primary factors and the explicit plan list might be a minimum. A separate outcome-specific baseline specification may have been intended.
- **Direct versus inferred:** The differently explicit lists are direct. The actual fitted inclusion/exclusion of each inherited covariate is not established by these lists alone.
- **Classification:** REPORT main compared with PLAN protocol/SAP; primary/all P_R; domain protocol_report. Confirmed. The plan comparators agree, so no P_P; table results instantiate the main method rather than creating S_W.
- **Evidence state:** reproduced. Determining fact: the report expressly specifies an additional given-baseline-secondary-outcome adjustment absent from both explicit plan lists.
- **Exact remaining human question:** What exact covariate set was planned and used for each secondary outcome, including its baseline value, multisite pain and mental-health condition, and where was any expansion documented?

## C007 — Primary versus sensitivity missing-data analysis roles

- **Location found:** Yes: PLAN [SAP p.19 §11](../../../joi250046supp2_prod_1755300121.15087.pdf#page=19), PLAN [p.4 July 17, 2024 amendment](../../../joi250046supp2_prod_1755300121.15087.pdf#page=4); REPORT [main p.4 missing-data paragraph](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); REPORT results [p.4 Missing Data](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4), [p.5 Non-Response Weighting](../../../joi250046supp4_prod_1755300121.15587.pdf#page=5), [p.9 eTable 4](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9), [p.11 sensitivity narrative and complete-case block](../../../joi250046supp4_prod_1755300121.15587.pdf#page=11). P.5 was read as disclosed-amendment context in addition to the registered comparisons.
- **Source text matched:** Report primary analysis uses MNAR pattern-mixture imputation among those with follow-up, nonresponse weighting for none and adjustment. Results p.4 says the >15% or differential-missingness criteria were met for this primary approach; p.5 says nonresponse weighting was formally incorporated into the SAP. eTable 4 labels the primary fit imputed and weighted; the follow-up/complete-case fit is described as sensitivity at p.11.
- **Comparator matched:** SAP p.19 retains the primary-follow-up/MAR sentence. Its next branch says missingness will be analyzed and sensitivity analyses conducted as required (>15% or differential); its first approach explicitly relaxes MAR using pattern-mixture imputation plus IPW, and its second approach is worst/best-case sensitivity. SAP p.4 explicitly adds IPW for no follow-up and calls pattern mixture the current approach, extending interpretation to all randomized. These amendment/branch facts are not omitted.
- **Logical comparison reproduced, including precision:** Primary-follow-up/MAR wording remains alongside amended pattern-mixture/IPW wording and differs from the reported primary MNAR designation. No numeric-copy comparison is made: main/eTable 4 primary 3-month RRs 1.28,1.54,1.20 differ from eTable 7 complete-case RRs 1.34 (1.12,1.61),1.48 (1.24,1.75),1.10 (.94,1.29) because these are expressly distinct analyses. Precision intervals are not applicable to their primary/sensitivity labels. The complete-case results are present; no absence is asserted.
- **Consistency rule applicable:** Focus D, Route B, primary-analysis role specification, with retained plan wording considered together with the disclosed amendment.
- **Necessary inputs available:** Final supplied SAP amendment, retained §11 language, report role labels, threshold and both reported analysis families. **Exact missing inputs/definitions:** A final approved hierarchy explicitly assigning primary versus sensitivity status and reconciling the retained MAR sentence with the amended first approach.
- **Source-grounded alternative interpretation:** The amendment and conditional first approach may authorize MNAR/IPW as primary, leaving earlier primary-MAR text retained; the report may implement that intended branch. This is substantive source support, not merely a hypothetical missing amendment. The residual question is role reconciliation, not whether IPW was disclosed.
- **Direct versus inferred:** Competing role/assumption statements are direct. A protocol violation, absence of the follow-up result, or lack of IPW authorization is not inferred.
- **Classification:** SAP amendment and §11 are PLAN; main/results are REPORT. Primary P_R; all P_R, P_P; domain protocol_report. P_R compares report primary/sensitivity assignment with retained PLAN primary-MAR wording; P_P records the prospective bundle's retained MAR versus current pattern-mixture/IPW specifications. Main/results agree and add no S_C. Highest precedence P_R applies. Classification ambiguity: a disclosed amendment may supersede retained wording; resolving that hierarchy could reconcile the plan/report role interpretation.
- **Evidence state:** reproduced. Determining fact: direct final-source reading confirms the competing unconditional primary-MAR sentence and reported primary MNAR assignment, while also confirming amendment support for the latter.
- **Exact remaining human question:** In the final approved SAP hierarchy, was primary status assigned to follow-up/MAR or weighted MNAR pattern-mixture estimation, and which clause or amendment reconciles the retained primary-MAR sentence and reported sensitivity label?


Audited qualifying-route refinement: Route B covers focusD, unresolved retained primary/MAR hierarchy versus reported primary MNAR/sensitivity designation, and the extractable primary-analysis specification. The follow-up analysis is reported as sensitivity; SAP4amendment and SAP19weightedfirstbranch remain alternatives. This refinement changes no ID, screeningdecision, evidence state, document roles or relationship codes.

## C008 — RR versus finite NNT null coverage

- **Location found:** Yes: REPORT [main p.9 Table 2 HC/PT columns and footnotes b,d,e](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9), all six registered contrast/time rows; REPORT [p.4 binary model and NNT method](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4).
- **Source values matched:** Each NNT interval is finite positive. **Comparator matched:** Each same-outcome/time/HC−PT RR interval contains 1. The exact pairs and reciprocal implications are reproduced below.
- **Consistency rule applicable:** Focus B, Route B, ambiguity about null coverage of matched adjusted-response contrasts under the printed NNT infinity rule. RR=1 and RD=0 express equality of the same responses. This is not an interval-versus-P assertion: no pairwise P is reconstructed from omnibus P.

| Outcome/time, HC−PT | RR (95% CI) | NNT (95% CI) | Reciprocal implied RD interval |
|---|---|---|---|
| Severity 6 months | 1.13 (.98,1.30) | 24 (12,186) | [1/186,1/12]=[.005376,.083333] |
| Severity 12 months | 1.07 (.96,1.19) | 41 (17,76) | [1/76,1/17]=[.013158,.058824] |
| Intensity 3 months | 1.11 (.93,1.33) | 37 (14,57) | [1/57,1/14]=[.017544,.071429] |
| Intensity 12 months | 1.05 (.92,1.20) | 63 (18,38) | [1/38,1/18]=[.026316,.055556] |
| Interference 6 months | 1.10 (.96,1.27) | 26 (11,67) | [1/67,1/11]=[.014925,.090909] |
| Interference 12 months | 1.07 (.97,1.18) | 39 (16,79) | [1/79,1/16]=[.012658,.062500] |

- **Calculation reproduced, including precision:** All six displayed RR intervals contain 1, while reciprocals of all finite positive NNT endpoints imply RD intervals strictly above zero. Main footnote e says an RD interval containing zero gives NNT limits reaching infinity and a negative NNH branch. Even with ±.5 on integer endpoints, all NNT endpoints remain positive finite; even with ±.005 on two-decimal RR endpoints, the listed RR lower/upper endpoints still straddle 1. The comparison is of null inclusion/interval interpretation, not a numeric-copy gap; no relative-discrepancy value is applicable to this logical observation. A common-confidence-set contradiction cannot be calculated because the RD interval construction is unspecified.
- **Necessary inputs available:** Exact matched contrasts, intervals, common binary-model description and local RD-to-NNT infinity rule. **Exact missing inputs/definitions:** RD interval endpoints before inversion; parameter-specific CI methods; joint response covariance and any distinct analyses underlying the RR/NNT columns.
- **Source-grounded alternative interpretation:** RR and RD confidence intervals can use different interval constructions and yield different finite-sample null coverage. That alternative is consistent with the source's separate parameter displays; no shared variance formula is assumed.
- **Direct versus inferred:** Different printed null readings and reciprocal implications are direct. Incompatibility under one exact common confidence construction is not established. The intensity 12-month point-containment rule is separately recorded in C009.
- **Classification:** All compared content is REPORT in DOC-001; primary/all S_W; domain statistical_results. Confirmed; interval-method ambiguity is substantive, not document-role ambiguity.
- **Evidence state:** reproduced. Determining fact: all six exact-source matched pairs retain their different displayed null coverage and the source does not identify the RD interval construction needed to interpret the finite NNT limits.
- **Exact remaining human question:** Which RD intervals and confidence construction produced these six NNT intervals, and how should their null coverage be interpreted alongside the same-contrast RR intervals?

## C009 — NNT point outside its confidence interval

- **Location found:** Yes: REPORT [main p.9 Table 2 pain intensity 12 months, HC/PT NNT column](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9).
- **Source value matched:** Point 63. **Comparator matched:** Printed 95% interval 18–38, in the same tuple.
- **Consistency rule applicable:** Focus B, Route A category 1, point containment.
- **Calculation reproduced, including precision:** 63>38. Point interval [62.5,63.5] is above the largest possible upper endpoint 38.5 by 24; diagnostic relative gap 24/63=.380952. Category 1 applies directly without rounding-based removal or a distributional assumption.
- **Necessary inputs available:** Same-row point, endpoints and 95% label. **Exact missing inputs/definitions:** Unrounded interval and its construction, or an explicit point/interval mapping that supplies the intended tuple. No missing input prevents the containment reading.
- **Source-grounded alternative interpretation:** A point or interval may belong to a different contrast/time, or a separate construction may have supplied the endpoints. No replacement is inferred from neighboring rows.
- **Direct versus inferred:** The outside point is direct. A production mechanism or replacement endpoint is unestablished.
- **Classification:** REPORT within main; primary/all S_W; domain statistical_results. Confirmed; no role ambiguity.
- **Evidence state:** reproduced. Determining fact: the source reads exactly 63 (18–38), and the point remains outside even after half-unit expansion.
- **Exact remaining human question:** What point estimate and 95% interval belong to the 12-month pain-intensity HC/PT NNT?

## C010 — SMD points outside printed confidence intervals

- **Location found:** Yes: REPORT [main p.10 Table 3](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) and [p.11 PGIC-pain continuation](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11). Every one of the fourteen registered tuples was read directly; all matched the ledger.
- **Source and comparator values matched:** Each point and both endpoints below are printed in the same SMD tuple; the headers say 95% CI. Physical-function endpoints are transcribed in printed order.
- **Consistency rule applicable:** Focus B, Route A category 1, point containment. Numerical sorting of physical endpoints does not remove containment failures.

| Page; outcome/time | Contrast | Source point (printed endpoints) | Direct comparison with nearest endpoint | Half-unit point/endpoint gap |
|---|---|---|---|---:|
| 10; severity 12 months | PT/UC | −.25 (−.24,.01) | −.25<−.24 | 0 |
| 10; severity 12 months | HC/UC | −.36 (−.35,−.12) | −.36<−.35 | 0 |
| 10; intensity 12 months | HC/UC | −.27 (−.26,−.12) | −.27<−.26 | 0 |
| 10; interference 12 months | PT/UC | −.26 (−.25,.01) | −.26<−.25 | 0 |
| 10; interference 12 months | HC/UC | −.37 (−.36,−.11) | −.37<−.36 | 0 |
| 10; physical 6 months | PT/UC | .15 (.09,−.06) | .15>.09 | .05 |
| 10; physical 6 months | HC/UC | .02 (−.03,−.18) | .02>−.03 | .04 |
| 10; physical 6 months | HC/PT | .22 (.16,.05) | .22>.16 | .05 |
| 10; physical 12 months | PT/UC | .20 (.18,−.03) | .20>.18 | .01 |
| 10; physical 12 months | HC/UC | .07 (.04,−.16) | .07>.04 | .02 |
| 10; physical 12 months | HC/PT | .27 (.25,.09) | .27>.25 | .01 |
| 11; PGIC pain 12 months | PT/UC | −.55 (−.50,.05) | −.55<−.50 | .04 |
| 11; PGIC pain 12 months | HC/UC | −.57 (−.54,−.08) | −.57<−.54 | .02 |
| 11; PGIC pain 12 months | HC/PT | −.29 (−.25,.14) | −.29<−.25 | .03 |

- **Calculation reproduced, including precision:** For each printed two-decimal point and endpoint, ±.005 expansion reduces its nearest-bound separation by .010. The final column records max(0,separation−.010), including five boundary-touching cases. Category 1 applies to the direct printed point-versus-interval reading and expressly exempts it from precision-based removal, so a zero expanded gap in those five cases does not erase the observed printed containment failure. No relative-gap threshold decides these tuples.
- **Necessary inputs available:** All fourteen points/endpoints, matched row/contrast and CI label. **Exact missing inputs/definitions:** Unrounded SMD tuples, exact SMD interval method and intended contrast/time mapping needed to identify replacement values. Those inputs are unnecessary for the printed containment check.
- **Source-grounded alternative interpretation:** Points or intervals may originate from distinct contrast/time assignments or another analysis. Endpoint order alone cannot explain the outside point, because it is outside the numerical minimum/maximum in every row.
- **Direct versus inferred:** All fourteen printed containment failures are direct. The cause, intended column mapping and replacement numbers are unestablished.
- **Classification:** REPORT within DOC-001; primary/all S_W; domain statistical_results. Confirmed. C003 compares point construction; this candidate compares point containment, a distinct rule.
- **Evidence state:** reproduced. Determining fact: all fourteen exact-source points lie outside both corresponding endpoints in numerical order.
- **Exact remaining human question:** Which SMD point and 95% interval belong together for each of these fourteen outcome/time/contrast tuples?

## C011 — Covariate set of restricted primary analyses

- **Location found:** Yes: REPORT results [p.4 Adjustment](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4), [p.7 eTable 2 final imputation/estimation set](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7), [p.13 Protocol Change Subset Analyses](../../../joi250046supp4_prod_1755300121.15587.pdf#page=13), [p.14 eTable 8 all three blocks and footnote b](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14). Fitted education/employment terms at [p.8](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8) and [p.9](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9) were also read as corroboration.
- **Source text matched:** P.13 identifies eTable 8 as results of the primary analysis restricted to subsets of the randomized population. Footnote b applies to every adjusted percentage/RR row and explicitly lists sex, age, site, rural/urban residence, multisite condition, mental-health diagnosis and baseline pain severity.
- **Comparator matched:** P.4 selection narrative and p.7 final list add education and unemployment to the primary imputation/estimation models; pp.8–9 contain both. These two selected terms are absent from eTable 8's explicit list.
- **Consistency rule applicable:** Focus C, Route B, identifying the model generating primary-outcome subset estimates. This is an explicit model-attribution comparison, not inference that unspecified imputation or weights were absent.
- **Logical comparison reproduced, including precision:** The seven-factor subset list versus seven base factors plus education/employment is a membership difference, with no numerical precision interval. All nine affected outcome/time rows below share the footnote and restricted-primary attribution; each row's percentages, three RR/NNT contrast columns were visually located. The RR triples identify every row precisely, rather than comparing different subsets numerically.

| eTable 8 block and time | PT/UC RR | HC/UC RR | HC/PT RR | Common model-description comparison |
|---|---:|---:|---:|---|
| Before enhancement, 3 months | .96 | 1.34 | 1.39 | Full primary model versus base-only footnote b |
| Before enhancement, 6 months | 1.31 | 1.29 | .98 | Same |
| Before enhancement, 12 months | 1.59 | 1.84 | 1.16 | Same |
| After enhancement, 3 months | 1.37 | 1.60 | 1.17 | Same |
| After enhancement, 6 months | 1.53 | 1.72 | 1.13 | Same |
| After enhancement, 12 months | 1.29 | 1.33 | 1.03 | Same |
| Reminder letters, 3 months | 1.54 | 1.67 | 1.08 | Same |
| Reminder letters, 6 months | 1.67 | 1.90 | 1.14 | Same |
| Reminder letters, 12 months | 1.46 | 1.49 | 1.02 | Same |

- **Necessary inputs available:** Full and subset covariate descriptions, model attribution and all affected rows. **Exact missing inputs/definitions:** Implemented covariate vector for each subset; whether additional predictors were reselected, dropped or only omitted from the footnote.
- **Source-grounded alternative interpretation:** A deliberately refitted base-only model or an abbreviated footnote could be coherent; the source does not identify which interpretation generated these results.
- **Direct versus inferred:** The different explicit lists and common attribution are direct. Actual education/employment omission from the fitted subset design matrix is not established by silence alone.
- **Classification:** All conflicting specifications are REPORT in DOC-005; primary/all S_W; domain statistical_results. Confirmed. The phrase Protocol Change names retrospective subgroup context, not a PLAN document role.
- **Evidence state:** reproduced. Determining fact: all nine row families share the restricted-primary attribution but a printed adjustment list omitting the two selected primary factors.
- **Exact remaining human question:** Which covariates entered each eTable 8 subset estimation model, and did primary analysis restricting to subsets use the full primary set or the base-only set printed in footnote b?

## C012 — Final response-weight model predictor membership

- **Location found:** Yes: REPORT results [p.4 Adjustment/selection](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4), [p.5 Non-Response Weighting](../../../joi250046supp4_prod_1755300121.15587.pdf#page=5), [p.7 eTable 2 final nonresponse predictors](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7), [p.10 eTable 5 full coefficient display](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10); corroborating REPORT [workbook](../../../joi250046supp5_prod_1755300121.16087.xlsx), `eTable 3` A18, H18, I18, J18.
- **Source values/text matched:** ETable 2 additional weighting list: PEG, PHQ-8, GAD-7, any negative SDOH and education (any college versus HS or less).
- **Comparator matched:** ETable 5 full fit includes PEG, PHQ-8, GAD-7, negative SDOH and Not employed, OR 1.49 (1.11,2.00), P=.008; it has no education row. The local note excludes healthcare-site information, not education. Direct XML: A18 is Not employed; H18 string 356 is <.001; I18 cached .0228; J18 cached .0591. Workbook H/I/J headings distinguish primary outcome/nonresponse/3-month missingness selection tests.
- **Consistency rule applicable:** Focus C, Route B, final primary weight-model membership.
- **Logical comparison reproduced, including precision:** Four additional predictors match; the final list names education while the displayed final fit names employment. No numeric-copy or coefficient-significance comparison is the rule; rounding intervals/relative discrepancy are inapplicable to predictor membership. The workbook tests corroborate possible employment selection and do not reconcile education's absence.
- **Necessary inputs available:** Complete final selected list, displayed coefficient fit, primary weight-model narrative and selection tests. **Exact missing inputs/definitions:** Implemented predictor vector and whether an education term was omitted from display, replaced or retained in the calculated weights.
- **Source-grounded alternative interpretation:** A prior selected-variable list may have persisted, the fitted display may omit education, or employment may have replaced it. The selection tests allow employment to qualify under the stated .10 criterion.
- **Direct versus inferred:** Different lists are direct; implemented substitution/omission cannot be inferred solely from coefficient absence.
- **Classification:** Conflicting locations are REPORT within DOC-005; workbook is REPORT corroboration only. Primary/all S_W; domain statistical_results. Confirmed; no S_C is added by corroborating selection tests.
- **Evidence state:** reproduced. Determining fact: exact-source final selection list and fitted coefficient display name different additional predictor membership.
- **Exact remaining human question:** Did the final nonresponse model include education, employment or both, and which predictor vector generated the primary-analysis weights?

## C013 — Education coding and coefficient attribution

- **Location found:** Yes: REPORT results [p.7 eTable 2 final primary predictor list](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7), [p.8 eTable 3 all three education rows](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8), [p.9 eTable 4 all three education rows](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9); corroborating REPORT [workbook](../../../joi250046supp5_prod_1755300121.16087.xlsx), `eTable 3` A12:A16.
- **Source text matched:** Selected education is any college versus HS degree or less, a binary grouping.
- **Comparator matched:** All six displayed coefficients and labels below were read directly. Workbook A12 is Education; A13 High school degree or less; A14 Associate's or Technical degree; A15 College degree; A16 Doctoral or Postgraduate degree. These are direct decoded shared strings 9,10,12,14,16.

| Source model and printed row | Effect | Printed 95% CI | P |
|---|---:|---|---:|
| eTable 3 first AA versus HS or less | −.02 | [−.11,.08] | .866 |
| eTable 3 second AA versus HS or less | .16 | [.07,.25] | .077 |
| eTable 3 graduate versus HS or less | .39 | [.29,.49] | <.001 |
| eTable 4 first AA versus HS or less | RR .97 | [.82,1.16] | .770 |
| eTable 4 second AA versus HS or less | RR 1.16 | [1,1.33] | .046 |
| eTable 4 graduate versus HS or less | RR 1.35 | [1.13,1.61] | <.001 |

- **Consistency rule applicable:** Focus C, Route B, primary-model design-matrix identity and coefficient attribution. Repeated AA wording alone is not the rule; binary specification versus three distinct model parameters is.
- **Logical comparison reproduced, including precision:** One binary variable relative to one reference group has one coefficient; both reported fits show three nonreference education coefficients. The repeated AA labels cannot map each to the distinct available categories with certainty. No numeric estimate equality is claimed and no rounding interval/relative gap applies to parameter-count/coding comparison.
- **Necessary inputs available:** Binary selected grouping, six coefficient tuples/reference labels and available workbook categories. **Exact missing inputs/definitions:** Final education design matrix in each fit, category-to-row correspondence and whether selection coding differed from final-fit coding.
- **Source-grounded alternative interpretation:** Binary education may have been used for selection while four-category education was used for final fitting; the list may summarize selection coding rather than implementation. The source does not state that distinction.
- **Direct versus inferred:** Binary phrase, three coefficients and duplicated labels are direct. Assigning the second AA row to college is an unestablished reconstruction and is not made.
- **Classification:** All conflicts REPORT within DOC-005; workbook REPORT corroboration only. Primary/all S_W; domain statistical_results. Confirmed; the concern is the statistical model, so report_internal_inconsistency is not selected.
- **Evidence state:** reproduced. Determining fact: both exact fitted displays have three education parameters despite the explicit binary final-list specification.
- **Exact remaining human question:** Was education binary or represented by three nonreference levels in each final imputation/estimation model, and which educational level does each printed coefficient represent?

## C014 — Coefficient CI versus P-value null-significance pattern

- **Location found:** Yes: REPORT results [p.8 eTable 3 seven registered rows](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8), [p.9 eTable 4 age and second AA rows](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9), [p.10 eTable 5 PEG row](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10). Method context was read at results [p.4](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4), [p.5](../../../joi250046supp4_prod_1755300121.15587.pdf#page=5), and REPORT [main p.4 two-sided alpha=.05](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4).
- **Source and comparator matched:** Every same-row estimate/95% CI and P below was directly read. All ten match the ledger.
- **Consistency rule applicable:** Focus B, Route A category 1, displayed interval-versus-P null/significance compatibility at 95%/.05. This rule does not require reconstructing an exact test statistic.

| Page/table; row | Source estimate (95% CI) | Comparator P | Null | Direct logical comparison |
|---|---|---:|---:|---|
| 8/eTable 3; Pattern 2 follow-ups | −.28 (−.47,−.08) | .150 | 0 | Upper endpoint <0; P>.05 |
| 8/eTable 3; Pattern 1 follow-up | −.20 (−.36,−.03) | .226 | 0 | Upper endpoint <0; P>.05 |
| 8/eTable 3; Pattern 2 × PT | −.30 (−.58,−.02) | .280 | 0 | Upper endpoint <0; P>.05 |
| 8/eTable 3; Pattern 2 × HC | −.47 (−.74,−.19) | .090 | 0 | Upper endpoint <0; P>.05 |
| 8/eTable 3; Site 3 | .19 (.08,.29) | .069 | 0 | Lower endpoint >0; P>.05 |
| 8/eTable 3; Site 4 | .15 (.05,.24) | .124 | 0 | Lower endpoint >0; P>.05 |
| 8/eTable 3; second AA row | .16 (.07,.25) | .077 | 0 | Lower endpoint >0; P>.05 |
| 9/eTable 4; Age ≥65 | RR 1.15 (1,1.33) | .046 | 1 | Printed interval contains 1; P<.05 |
| 9/eTable 4; second AA row | RR 1.16 (1,1.33) | .046 | 1 | Printed interval contains 1; P<.05 |
| 10/eTable 5; PEG | OR .96 (.92,1.00) | .037 | 1 | Printed interval contains 1; P<.05 |

- **Calculation reproduced, including precision:** For the seven linear rows, even ±.005 endpoint expansion excludes zero: closest bounds become −.075,−.025,−.015,−.185,.075,.045,.065; ±.0005 P intervals remain above .05. For the two RR rows, the endpoint is literally printed 1; for PEG, 1.00. Unrounded endpoints may lie just inside the null boundary, but the scope exempts category 1 from precision-based removal. The significant P intervals [.0455,.0465] and [.0365,.0375] remain below .05. No relative numeric-gap threshold is applied to any of the ten comparisons.
- **Necessary inputs available:** Coefficient identity, point and interval columns, 95% labels and source .05 level. **Exact missing inputs/definitions:** Unrounded null-adjacent endpoints; coefficient-test family, variance estimator for each column, reference distribution/degrees of freedom and any different analysis assignment. The source supplies robust GEE descriptions, but not the exact numeric ingredients needed to reproduce P values.
- **Source-grounded alternative interpretation:** Rounded null-adjacent endpoints may explain the three ratio rows. P values and intervals may use distinct variance/confidence constructions or correspond to different analyses. Those alternatives are retained; no normal-Wald standard errors, sidedness or df are invented.
- **Direct versus inferred:** The printed null/P comparisons are direct. A particular computation mechanism or replacement P/interval is unestablished.
- **Classification:** Conflicting values are REPORT within DOC-005. Main REPORT p.4 corroborates the test level and does not create S_C. Primary/all S_W; domain statistical_results. Confirmed; no role ambiguity.
- **Evidence state:** reproduced. Determining fact: all ten correctly read tuples show the registered displayed interval/P null-significance pattern under category 1, including the three explicitly retained null-adjacent endpoint cases.
- **Exact remaining human question:** Which analysis, variance and CI/test construction generated each of these ten rows; what are the three null-adjacent unrounded endpoints; and which interval/P pair should be extracted for every listed coefficient?

## C015 — Within-header three-month subset counts

- **Location found:** Yes: REPORT [results p.14 eTable 8 first subgroup header](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14); corroborating REPORT [p.7 eTable 1](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7), [p.13 subset definition](../../../joi250046supp4_prod_1755300121.15587.pdf#page=13), and the second/third headers on p.14.
- **Source values matched:** First header: randomized prior to 8/9/2021 N=454; PT=149, HC=153, UC=152 at 3 months.
- **Comparator matched:** Same header says 366 with at least one follow-up. Next block gives post-enhancement observed-at-three-month UC512/PT448/HC527; eTable 1 gives full observed-at-three-month UC621/PT542/HC635.
- **Consistency rule applicable:** Focus A, Route A category 3, nested contributors in the same header: observed-at-three-month contributors are within those with any follow-up.
- **Calculation reproduced, including precision:** 149+153+152=454>366. Sum interval [452.5,455.5] versus any-follow-up [365.5,366.5] leaves minimum excess 86; relative 86/366=.234973. Corroborating full minus post-enhancement arithmetic gives UC109/PT94/HC108, total311, conditional on disjoint observed-count populations. This subtraction is not a required replacement. The first sum exactly equals randomized N=454, which supports the alternative target-population interpretation.
- **Necessary inputs available:** All first-header counts/labels, any-follow-up total and neighboring contributor headers. **Exact missing inputs/definitions:** Whether first-header arm counts denote randomized population or observed three-month contributors; whether weighted representation explains the different count convention.
- **Source-grounded alternative interpretation:** The arm counts may be randomized target-population denominators, including those represented through weights, rather than observed contributors. The header's at-three-month phrase does not identify this departure from the other blocks.
- **Direct versus inferred:** The count sum, labels and within-header arithmetic are direct. Subtraction-derived alternative counts and weighting interpretation are conditional explanations, not replacements.
- **Classification:** REPORT internal to DOC-005; primary/all S_W; domain statistical_results. Confirmed; no plan relationship is created by retrospective protocol-change labels.
- **Evidence state:** reproduced. Determining fact: directly read at-three-month counts exceed the same header's any-follow-up count after precision, with the denominator convention unresolved.
- **Exact remaining human question:** Do PT149, HC153 and UC152 denote randomized arm sizes or observed three-month contributors, and which count convention applies to the first sensitivity-analysis subgroup?

## C016 — Raw-score summary statistic and bounds in eTable 11

- **Location found:** Yes: REPORT [results p.15 Additional Unadjusted Data and Analyses](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15), [p.17 eTable 11 title/header and all 21 rows](../../../joi250046supp4_prod_1755300121.15587.pdf#page=17), [p.18 note b](../../../joi250046supp4_prod_1755300121.15587.pdf#page=18); corroborating REPORT [main p.11 PGIC footnotes h/i](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11).
- **Source text matched:** Introduction says eTable 11 provides unadjusted mean secondary outcomes. Title says unadjusted median and interquartile ranges; raw-column header says Raw Score Median (25%-tile,75%tile). P.18 specifies unadjusted between-group MD/95% CI from linear GEE, without defining the raw-arm summaries.
- **Comparator matched:** All 21 rows' three raw-arm cells below were read directly, retaining printed bounds and mixed-width HC three-month PGIC cells. Main defines one item per PGIC pain/general outcome with response categories 1–7; it does not supply a conflicting mean/median definition.

| Outcome/time | PT raw cell | HC raw cell | UC raw cell |
|---|---|---|---|
| Severity 3 months | 5.1 (4.9,5.2) | 4.6 (4.4,4.7) | 4.6 (4.5,4.7) |
| Severity 6 months | 5.0 (4.8,5.1) | 4.4 (4.2,4.6) | 4.4 (4.2,4.5) |
| Severity 12 months | 4.8 (4.6,4.9) | 4.2 (4.1,4.4) | 4.3 (4.2,4.5) |
| Intensity 3 months | 4.9 (4.7,5.0) | 4.5 (4.3,4.6) | 4.5 (4.4,4.6) |
| Intensity 6 months | 4.8 (4.6,4.9) | 4.4 (4.2,4.5) | 4.4 (4.3,4.5) |
| Intensity 12 months | 4.6 (4.4,4.7) | 4.2 (4.1,4.4) | 4.3 (4.2,4.4) |
| Interference 3 months | 5.2 (5.0,5.3) | 4.6 (4.4,4.8) | 4.6 (4.5,4.7) |
| Interference 6 months | 5.1 (4.9,5.2) | 4.4 (4.2,4.6) | 4.4 (4.2,4.6) |
| Interference 12 months | 4.9 (4.7,5.1) | 4.2 (4.0,4.4) | 4.3 (4.2,4.5) |
| Social 3 months | 43.4 (42.8,44.0) | 44.6 (43.9,45.3) | 44.8 (44.4,45.2) |
| Social 6 months | 43.6 (42.9,44.2) | 45.4 (44.7,46.0) | 45.1 (44.7,45.4) |
| Social 12 months | 43.9 (43.3,44.6) | 45.8 (45.1,46.5) | 45.3 (44.8,45.8) |
| Physical 3 months | 37.7 (37.1,38.2) | 38.2 (37.7,38.8) | 38.2 (37.7,38.8) |
| Physical 6 months | 37.9 (37.3,38.4) | 38.9 (38.4,39.5) | 38.3 (37.8,38.8) |
| Physical 12 months | 37.9 (37.3,38.4) | 39.1 (38.5,39.7) | 38.8 (38.1,39.4) |
| PGIC pain 3 months | 2.9 (2.8,2.9) | 2.0 (1.0,3.0) | 1.9 (1.9,2.0) |
| PGIC pain 6 months | 2.8 (2.7,2.9) | 2.1 (2.0,2.2) | 2.1 (2.0,2.2) |
| PGIC pain 12 months | 2.8 (2.7,2.9) | 2.1 (2.0,2.2) | 2.2 (2.1,2.3) |
| PGIC general 3 months | 2.7 (2.6,2.7) | 2.0 (1.0,2.0) | 1.6 (1.5,1.6) |
| PGIC general 6 months | 2.5 (2.4,2.6) | 2.0 (1.9,2.1) | 1.8 (1.7,1.9) |
| PGIC general 12 months | 2.6 (2.4,2.7) | 1.9 (1.8,2.1) | 1.9 (1.7,2.0) |

- **Consistency rule applicable:** Focus C, Route B, extractable statistical summary identity and bounds. Mean and median/quartile labels name different statistical quantities. This affects all 21 raw-summary rows, regardless of the additional numerical diagnostic.
- **Logical/numerical comparison reproduced, including precision:** The mean narrative and median/quartile title/header do not establish the same summary. For an ordinary empirical median of one-item integer responses, the central value is on the integer/half-integer grid. Comparing a one-decimal printed center interval ±.05 with the nearest exact grid value gives the five above-threshold centers below. The grid constraint uses exact integer response categories, not rounded sample inputs.

| Exact PGIC cell | Printed-center interval | Nearest ordinary-median value | Gap | Relative gap |
|---|---|---:|---:|---:|
| Pain PT 6 months, 2.8 | [2.75,2.85] | 3 | .15 | .053571 |
| Pain PT 12 months, 2.8 | [2.75,2.85] | 3 | .15 | .053571 |
| Pain UC 12 months, 2.2 | [2.15,2.25] | 2 | .15 | .068182 |
| General PT 3 months, 2.7 | [2.65,2.75] | 2.5 | .15 | .055556 |
| General UC 6 months, 1.8 | [1.75,1.85] | 2 | .15 | .083333 |

The stated gap is the distance to the nearest grid value. Other fractional PGIC centers were checked: 2.9 gives .05/2.9=.017241; 2.6 gives .05/2.6=.019231; 2.1 gives .05/2.1=.023810; 1.9 gives .05/1.9=.026316; 1.6 gives .05/1.6=.031250; 2.0 and 2.5 have zero gap. These do not independently exceed .05. The numerical median diagnostic is restricted to its stated ordinary definition; the summary-label conflict does not assume that every possible interpolated/set-valued median excludes these values. No equality between raw medians and fitted MDs is assumed, and no arm permutation is inferred.

- **Necessary inputs available:** Narrative/title/header identities, all 63 raw cells, local MD-method note and one-item scale definition. **Exact missing inputs/definitions:** Raw central-statistic and bound method per arm/outcome/time; empirical/interpolated/weighted median definition; whether summary types are intentionally mixed; raw item responses/sample medians needed to reconstruct values.
- **Source-grounded alternative interpretation:** Most cells could be means with confidence intervals while the two wide HC three-month PGIC cells are medians/quartiles; an interpolated, set-valued or model-based summary could explain fractional centers. The local note defines between-group MDs only and does not resolve the raw-arm columns.
- **Direct versus inferred:** Conflicting summary labels and exact cell shapes are direct. Calling cells means, medians, confidence intervals or quartiles beyond the printed competing labels is an unestablished reconstruction. The ordinary-median grid result is an explicitly qualified calculation.
- **Classification:** Conflicting mean/median descriptions are REPORT within DOC-005. Main REPORT PGIC definition only establishes scale context, and does not conflict with the supplement's scale or summary definition. Primary/all S_W; domain statistical_results. Ledger classification is confirmed. The initial screen-group S_C/all S_C,S_W interpretation should be aligned because corroborating scale input alone is not a cross-report relationship. No role ambiguity; summary/median-method ambiguity remains.
- **Evidence state:** reproduced. Determining fact: exact-source narrative and table raw-summary labels remain different, all 21 affected rows are located, and five stated-definition median diagnostics exceed precision tolerance.
- **Exact remaining human question:** What central statistic and bound method were used for each raw-arm eTable 11 cell, especially the HC three-month PGIC cells; was any interpolation or mixed summary intentional; and which entries should be extracted as means/CI versus medians/quartiles?

## C017 — Workbook All Observed depression percentage

- **Location found:** Yes: supplied REPORT [workbook](../../../joi250046supp5_prod_1755300121.16087.xlsx), worksheet exactly `eTable 3`, E3, A82, E82, A83, E83, A110. Direct workbook.xml confirms worksheet name and worksheet relationship; direct sheet1.xml/sharedStrings.xml confirms all cells. B82/C82/D82 were also read as count-partition corroboration.
- **Source value matched:** E82 has shared-string index 290, decoded as 711 (73.2). A82 index 96 reads Current depression (PHQ-8 ≥10), No. (%).
- **Comparator matched:** E3 index144=(N=1568); A83 index109=Missing; E83 numeric2; A110 index355 says missing is reported as n but excluded from the denominator in the reported percentage. E2's All Observed group identity is consistent with the source group headings. B82=1116 (47.9), C82=162 (54.9), D82=243 (51.9) corroborate count alignment: 162+243+711=1116.
- **Consistency rule applicable:** Focus A, Route A category 3, same-workbook-display numerator/percentage/denominator reconciliation under the explicit missing-value footnote.
- **Calculation reproduced, including precision:** Nonmissing denominator 1568−2=1566; 100×711/1566=45.402299%. Half-unit N/missing inputs give denominator [1565,1567], numerator [710.5,711.5]. Recomputed percentage interval [100×710.5/1567,100×711.5/1565]=[45.341417,45.463259]%. Printed percentage [73.15,73.25]%. Gap 27.686741 points; relative 27.686741/73.2=.378234. A denominator approximately 711/.732=971.311475 would be required for the central printed percentage, rather than the stated nonmissing 1566.
- **Necessary inputs available:** Exact cached source cell text, group denominator, missing count, current-depression label and percentage rule. **Exact missing inputs/definitions:** Any restricted PHQ-8 assessment denominator supporting 73.2, or an alternate numerator definition for that cell.
- **Source-grounded alternative interpretation:** A restricted assessment population might produce another denominator, but no such denominator is stated in the cell/group/footnote. The source-production mechanism remains unknown.
- **Direct versus inferred:** Decoded cells and arithmetic are direct. Restricted denominator or substituted percentage is an unestablished explanation; no replacement is assigned.
- **Classification:** All compared content REPORT within one workbook; primary/all S_W; domain statistical_results. Confirmed; no role ambiguity. Exact actual source filename and worksheet cells resolve the locator; no current registered value/location required transcription repair.
- **Evidence state:** reproduced. Determining fact: direct source XML confirms 711 (73.2), N1568, missing2 and the nonmissing-denominator rule, leaving relative gap .378234.
- **Exact remaining human question:** What numerator and nonmissing denominator support the 73.2% printed in `eTable 3` E82?

## Recheck completion and unresolved inputs

All assigned IDs were covered separately: C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017. Evidence states: reproduced 17; reproduced_after_transcription_correction 0; not_reproduced 0. Repeated-pattern coverage includes all twenty C003 construction rows, all three C004 reciprocal-NNT rows, all six C008 matched interval pairs, all fourteen C010 containment tuples, all nine C011 subset rows, all six C013 education coefficient rows, all ten C014 interval/P tuples and all twenty-one C016 raw-summary rows.

The exact supplied-source locations were readable. No mechanical source-reading gap remains. Named unresolved evidence inputs remain: duration convention/amendment; adherence denominator; actual UC change SDs and unrounded contrast mapping; NNT integer and RD/CI construction; prospective age and secondary-adjustment specification; final primary/sensitivity hierarchy after disclosed amendment; subset/weight/education model vectors; unrounded coefficient endpoints and exact tests; subgroup count convention; and raw-summary/median/bounds definitions. Each is stated in the relevant card's human question. No covariance, coefficient-test distribution, degrees of freedom or replacement statistic has been inferred.

Classification values match the provisional ledger for every ID. One provenance-text alignment is needed: C016's initial screen-group S_C/all S_C,S_W description should follow the independently confirmed S_W/all S_W distinction, because main scale information is corroborating context. C007 retains both P_R and P_P and records the disclosed amendment as substantive alternative support. No assigned ID is deleted, and no disposition is assigned.


<!-- Fresh appended-candidate recheck -->

# Appended-candidate mechanical evidence recheck

Fresh runtime: /root/recheck_c018; model gpt-6.1-sol; reasoning effort high. Assigned stable ID: C018 only. The complete quantitative scope and review contract were read. Exact current-source render inspection, independently transcribed source tuples and separate JavaScript calculations were used; no web, legacy conclusions, source modification or new Python helper was used.

Source scope: DOC-005 physical PDF pages 15,17,18; DOC-001 physical PDF pages 4,11. Five distinct source pages visually inspected, below the 32-page shard bound. Existing current-run renders use pinned PyMuPDF1.26.4, CPU, as recorded in tooling_record.md. No new extraction/OCR/render derivative was required. Scientific text read remained below 200000 characters.

## C018 — Physical-function omnibus P values and contrast intervals
**Candidate statement:** The eTable 11 physical-function six- and twelve-month omnibus P values do not reconcile with their three mean-difference/95%CI tuples under the normal-CI/common-covariance/chi-square2 Wald reconstruction that is precision-feasible for the other 19 rows of that display.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eTable 11 omnibus P values versus REPORT results supplement eTable 11 mean-difference/95%CI contrasts and method context. Main article REPORT methods are corroboration only.

**Evidence state:** reproduced

**Finding IDs:** F-ST2-1001

**Qualifying route:** Route A, category 1

### Exact-source location and transcription facts

| Exact supplied-source location | Location found | Source value/text matched | Comparator matched | Content role |
|---|---|---|---|---|
| [Results supplement PDF p17, eTable 11 Physical Functioning 6 months](../../../joi250046supp4_prod_1755300121.15587.pdf#page=17) | Yes; every affected contrast and P cell visually read | PT−UC 1.1 (0.3,1.9); HC−UC 0.4 (−0.3,1.1); HC−PT −0.6 (−1.4,0.1) | Omnibus P=0.005 in the same six-month row | REPORT |
| [Results supplement PDF p17, eTable 11 Physical Functioning 12 months](../../../joi250046supp4_prod_1755300121.15587.pdf#page=17) | Yes; every affected contrast and P cell visually read | PT−UC 1.2 (0.4,2.0); HC−UC 0.9 (0.0,1.8); HC−PT −0.3 (−1.2,0.6) | Omnibus P=0.001 in the same twelve-month row | REPORT |
| [Results supplement PDF p17, all other 19 eTable 11 outcome/time rows](../../../joi250046supp4_prod_1755300121.15587.pdf#page=17) | Yes; all 57 corroborating mean-difference/CI tuples and 19 Ps visually read | Complete transcription appears below | All 19 feasible witnesses independently recalculated against their own exact printed tuples, not against the target rows | REPORT, same-display corroboration |
| [Results supplement PDF p18, eTable 11 note b](../../../joi250046supp4_prod_1755300121.15587.pdf#page=18) | Yes | Unadjusted between-group mean differences and 95% confidence intervals were calculated with a linear regression model fit using generalized estimating equations for each continuous outcome | Matches the inferential-column identity of eTable 11; no explicit normal critical value, covariance, omnibus distribution or df supplied | REPORT |
| [Results supplement PDF p15, Additional Unadjusted Data and Analyses](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15) | Yes | Tables 2 and 3 replicated with no adjustment, weighting or imputation; eTable 10 gives unadjusted mean change and eTable 11 gives unadjusted mean secondary outcomes | Supplies broad replicated-analysis context, not an explicit statement that every inferential implementation is identical | REPORT |
| [Main article PDF p11, Table 3 note c](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11) | Yes | Omnibus P value is the Wald test assessing any difference among the three groups; between-group comparisons follow omnibus P<.05 using the least significant difference approach | Corroborates a three-group Wald family for the main adjusted display; not an exact supplement df/covariance declaration | REPORT, corroboration only |
| [Main article PDF p4, Statistical Analysis](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4) | Yes | GEE with working-independence correlation and robust sandwich standard errors; linear GEE for continuous secondary outcomes; all tests two-sided with alpha=.05 | Corroborates the broad fitted family and confidence/testing context; exact eTable 11 inferential distributions remain absent | REPORT, corroboration only |

The rendered p17 heading is unadjusted between-group mean differences (95%CI), with PT vs UC, HC vs UC and HC vs PT columns and a separately named omnibus P column. No pairwise P value is printed. The comparison does not equate raw medians with fitted means, and does not equate a single pairwise null with the omnibus null.

### Independent source transcription, including every corroborating row

All entries below were reread visually from the exact supplied-source p17 render. The 19 remaining rows support a reproducible numerical family; only physical six/twelve months are affected locations of this candidate.

| Relationship | Outcome/time | PT−UC estimate (95%CI) | HC−UC estimate (95%CI) | HC−PT estimate (95%CI) | Omnibus P |
|---|---|---|---|---|---|
| S601 | Pain severity 3 months | -0.5 (-0.7, -0.3) | -0.5 (-0.7, -0.3) | 0 (-0.2, 0.2) | <.001 |
| S602 | Pain severity 6 months | -0.6 (-0.8, -0.3) | -0.6 (-0.8, -0.3) | 0 (-0.2, 0.2) | <.001 |
| S603 | Pain severity 12 months | -0.5 (-0.8, -0.3) | -0.4 (-0.6, -0.2) | 0.1 (-0.1, 0.3) | <.001 |
| S604 | Pain intensity 3 months | -0.4 (-0.6, -0.2) | -0.3 (-0.5, -0.1) | 0 (-0.2, 0.2) | <.001 |
| S605 | Pain intensity 6 months | -0.4 (-0.6, -0.2) | -0.4 (-0.6, -0.2) | 0 (-0.2, 0.2) | <.001 |
| S606 | Pain intensity 12 months | -0.3 (-0.6, -0.1) | -0.2 (-0.4, -0.1) | 0.1 (-0.1, 0.3) | <.001 |
| S607 | Pain-related interference 3 months | -0.6 (-0.8, -0.3) | -0.6 (-0.8, -0.4) | 0 (-0.2, 0.2) | <.001 |
| S608 | Pain-related interference 6 months | -0.7 (-0.9, -0.4) | -0.7 (-0.9, -0.4) | 0 (-0.3, 0.2) | <.001 |
| S609 | Pain-related interference 12 months | -0.6 (-0.9, -0.4) | -0.5 (-0.8, -0.3) | 0.1 (-0.1, 0.3) | <.001 |
| S610 | Social functioning 3 months | 1.2 (0.3, 2.1) | 1.4 (0.7, 2.2) | 0.2 (-0.5, 1) | 0.001 |
| S611 | Social functioning 6 months | 1.8 (0.9, 2.7) | 1.5 (0.8, 2.2) | -0.3 (-1, 0.4) | <.001 |
| S612 | Social functioning 12 months | 1.8 (0.9, 2.8) | 1.4 (0.5, 2.2) | -0.5 (-1.3, 0.3) | <.001 |
| S613 | Physical functioning 3 months | 0.6 (-0.2, 1.3) | 0.6 (-0.2, 1.3) | 0 (-0.8, 0.8) | 0.212 |
| S614 | Physical functioning 6 months | 1.1 (0.3, 1.9) | 0.4 (-0.3, 1.1) | -0.6 (-1.4, 0.1) | 0.005 |
| S615 | Physical functioning 12 months | 1.2 (0.4, 2) | 0.9 (0, 1.8) | -0.3 (-1.2, 0.6) | 0.001 |
| S616 | PGIC pain 3 months | -0.8 (-0.9, -0.6) | -0.9 (-1, -0.8) | -0.2 (-0.3, 0) | <.001 |
| S617 | PGIC pain 6 months | -0.7 (-0.8, -0.5) | -0.7 (-0.8, -0.5) | 0 (-0.2, 0.1) | <.001 |
| S618 | PGIC pain 12 months | -0.7 (-0.8, -0.5) | -0.6 (-0.7, -0.4) | 0.1 (-0.1, 0.2) | <.001 |
| S619 | PGIC general 3 months | -0.8 (-0.9, -0.6) | -1.1 (-1.2, -1) | -0.3 (-0.5, -0.2) | <.001 |
| S620 | PGIC general 6 months | -0.6 (-0.7, -0.4) | -0.8 (-0.9, -0.6) | -0.2 (-0.3, 0) | <.001 |
| S621 | PGIC general 12 months | -0.6 (-0.8, -0.4) | -0.7 (-0.8, -0.5) | -0.1 (-0.2, 0.1) | <.001 |

### Consistency rule and independently reproduced calculation

**Rule applicable:** Yes, as an explicitly labeled diagnostic reconstruction supported by the same display. Let a=PT−UC, b=HC−UC and c=HC−PT=b−a. Under symmetric normal95% intervals use z=1.959963984540054, interval halfwidths h_j, variances v_j=(h_j/z)^2 and covariance u=(v_a+v_b−v_c)/2. The two-dimensional joint Wald statistic is

Q=(v_b a²+v_a b²−2uab)/(v_a v_b−u²),

with diagnostic chi-square2 tail P=exp(−Q/2). This reconstructed covariance is algebra within the tested family; it is not a claim about the authors' actual fitted covariance.

For every witness below I checked additive contrast identity, positive determinant, each point and both symmetric endpoints against the corresponding source number ±.05, and the computed tail against numeric P±.0005 or printed <.001. Arithmetic tolerance 1e−12 only accommodates floating-point endpoints. All 19 pass. These witnesses prove feasibility for these rows under this diagnostic family, not the actual undisclosed fitted implementation.

| Relationship | Witness (a,b,c) | Witness halfwidths | Diagnostic Q | Diagnostic P | Largest point/endpoint gap | All witness constraints met |
|---|---|---|---:|---:|---:|---|
| S601 | (-0.549, -0.549, 0) | (0.199, 0.199, 0.15) | 34.077570344 | 3.9824434849e-8 | 0.050000 | Yes |
| S602 | (-0.6, -0.6, 0) | (0.25, 0.25, 0.15) | 24.315167920 | 0.0000052484174757 | 0.050000 | Yes |
| S603 | (-0.549, -0.449, 0.1) | (0.201, 0.199, 0.15) | 29.340551305 | 4.2538310425e-7 | 0.050000 | Yes |
| S604 | (-0.398, -0.349, 0.049) | (0.152, 0.199, 0.199) | 28.892830604 | 5.3211015956e-7 | 0.050000 | Yes |
| S605 | (-0.449, -0.449, 0) | (0.199, 0.199, 0.15) | 22.793793846 | 0.000011230279251 | 0.050000 | Yes |
| S606 | (-0.349, -0.249, 0.1) | (0.201, 0.101, 0.15) | 23.354754552 | 0.0000084835863752 | 0.050000 | Yes |
| S607 | (-0.6, -0.649, -0.049) | (0.25, 0.199, 0.199) | 41.641881462 | 9.0694370878e-10 | 0.050000 | Yes |
| S608 | (-0.7, -0.7, 0) | (0.25, 0.25, 0.25) | 40.156049539 | 1.9064465561e-9 | 0.050000 | Yes |
| S609 | (-0.649, -0.549, 0.1) | (0.201, 0.201, 0.15) | 41.341524438 | 1.0539063750e-9 | 0.050000 | Yes |
| S610 | (1.151, 1.4, 0.249) | (0.899, 0.75, 0.701) | 13.411989543 | 0.0012235549409 | 0.050000 | Yes |
| S611 | (1.751, 1.451, -0.3) | (0.899, 0.699, 0.65) | 18.441295422 | 0.000098974559956 | 0.050000 | Yes |
| S612 | (1.802, 1.351, -0.451) | (0.948, 0.801, 0.799) | 15.726369532 | 0.00038464690825 | 0.050000 | Yes |
| S613 | (0.551, 0.552, 0.001) | (0.701, 0.798, 0.849) | 3.101587512 | 0.21207956755 | 0.050000 | Yes |
| S616 | (-0.798, -0.949, -0.151) | (0.148, 0.099, 0.101) | 375.441268582 | 2.9782722021e-82 | 0.050000 | Yes |
| S617 | (-0.7, -0.7, 0) | (0.15, 0.15, 0.15) | 111.544582053 | 6.0034619739e-25 | 0.050000 | Yes |
| S618 | (-0.7, -0.6, 0.1) | (0.15, 0.15, 0.15) | 97.886061801 | 5.5502398618e-22 | 0.050000 | Yes |
| S619 | (-0.8, -1.149, -0.349) | (0.15, 0.099, 0.101) | 611.340829900 | 1.7742936821e-133 | 0.050000 | Yes |
| S620 | (-0.6, -0.8, -0.2) | (0.15, 0.15, 0.15) | 118.373842178 | 1.9744528631e-26 | 0.050000 | Yes |
| S621 | (-0.649, -0.7, -0.051) | (0.199, 0.15, 0.101) | 93.615347054 | 4.6955414279e-21 | 0.050000 | Yes |

In particular social three months produces .001223554941 within [.0005,.0015], physical three months .21207956755 within [.2115,.2125], and all other 17 witnesses produce P<.001. The witnesses match source printed values and demonstrate same-display numerical support; no witness is offered as an author estimate.

### Exhaustive conservative display-precision check for both affected rows

Each displayed target point and CI endpoint receives ±.05. Numeric omnibus P receives ±.0005. Full feasible point/endpoint coupling is conservatively relaxed when forming the following bounding domains.

For physical six months: a∈[1.05,1.15], b∈[.35,.45], c=b−a∈[−.65,−.55] yields the point triangle (1.05,.40), (1.05,.45), (1.10,.45). Endpoint rounding permits the enlarged halfwidth boxes [.75,.85], [.65,.75], [.70,.80]. I separately evaluated all 24 point/variance-vertex combinations. Minimum covariance determinant 0.01195380636846352; maximum Q=8.556087823817016 at a=1.10,b=.45,h=(.75,.75,.70). Thus diagnostic P≥0.013869766053172373.

For physical twelve months: deliberately retain the larger point rectangle a∈[1.15,1.25], b∈[.85,.95], dropping the c constraint, and enlarged halfwidth boxes [.75,.85], [.85,.95], [.85,.95]. I separately evaluated all 32 point/variance-vertex combinations. Minimum covariance determinant 0.02217991416023505; maximum Q=12.281125558721055 at a=1.25,b=.95,h=(.75,.85,.95). Thus diagnostic P≥0.0021537112129520757.

The proof is not a grid search: Q=d′V⁻¹d is convex in d for fixed positive-definite V and convex in positive-definite V for fixed d; V is affine in the three contrast variances. All variance-box vertices are positive definite, hence so is their convex hull. Successive convexity therefore bounds Q by its point/variance-vertex maximum. Dropping point/endpoint halfwidth coupling, and the twelve-month c constraint, enlarges the feasible domains and preserves the bounds. Every actually precision-feasible tuple lies inside these conservative domains.

| Affected result | Conservative recomputed diagnostic P interval | Printed P half-unit interval | Minimum separating gap | Gap / absolute printed P |
|---|---|---|---:|---:|
| Physical functioning 6 months | [.013869766053172373,1] | [.0045,.0055] | .008369766053172373 | 1.6739532106344746 |
| Physical functioning 12 months | [.0021537112129520757,1] | [.0005,.0015] | .0006537112129520757 | .6537112129520757 |

**Calculation reproduced:** Yes, independently in JavaScript V8. Both outer diagnostic P intervals remain separated from the printed intervals even after conservative allowance for all displayed input precision. Route A category1 is independently exempt from rounding-based removal. The intervals' upper endpoints of 1 are deliberately loose logical bounds, not attainable maxima or fitted-P estimates. No replacement P is proposed. Both printed omnibus Ps and at least one contrast interval in each affected row indicate a result below .05; this candidate makes no claim of a .05-level conclusion reversal.

### Available inputs, exact missing definitions and alternatives

**Necessary inputs available:** Every printed target estimate, both interval limits, row/time and contrast identity, confidence level95%, corresponding numeric omnibus P, all19 same-display comparators, linear-GEE interval definition and broad replicated Wald-test context. These are sufficient to reproduce the diagnostic comparison and precision bounds.

**Necessary inputs unavailable for identification of the actual fitted analysis:** Unrounded estimates/interval endpoints; actual contrast covariance matrix; actual confidence critical value/reference distribution; omnibus reference distribution and degrees of freedom; explicit mapping of each omnibus P and contrast interval to the same covariance, fitted analysis and estimand; per-outcome/time sample size and missingness denominators; participant-level observations. The normal z and chi-square2 reference distribution are diagnostic choices, not reported facts.

**Source-grounded alternative interpretation:** eTable 11 note b identifies GEE intervals without explicitly naming their reference distribution, and the p15 replication statement may preserve broad structure rather than identical inferential details. An outcome/time-specific confidence distribution, a different omnibus reference distribution or df, separate covariance estimators, separate fitted analyses or another estimand/time-specific omnibus comparison could reconcile actual values. The table does not establish which of these applies. Missing definitions remain the human question rather than an inferred production mechanism.

**Direct observation versus inferred explanation:** Direct: the exact physical6/12 printed tuples, the two Ps and the stated model context. Reproduced mathematical observation: these tuples cannot yield those Ps within the independently supported normal-CI/common-covariance/chi-square2 reconstruction after half-unit rounding. Inferred only: that the authors used that exact reconstruction, that any particular production mechanism caused the discrepancy, or that one printed number should replace another. None of those inferences is asserted.

### Classification and determining evidence fact

**Document roles confirmed:** All compared numeric columns belong to REPORT results material, by content. Main article methods are REPORT corroboration. No PLAN content is compared.

**Relationship and precedence confirmed:** Primary S_W; all relationships S_W. The quantitative comparison is internal to one REPORT supplement. Main REPORT context only corroborates the tested family; it does not conflict with a numeric counterpart and adds no S_C relationship. No P_R or P_P relationship applies. No classification correction is required.

**Review domain confirmed:** statistical_results because the candidate concerns estimate/interval/test and method logic, rather than a conflicting assignment of a number to an outcome or analysis set.

**Classification ambiguity:** Exact supplement inferential mappings remain absent. This is an ambiguity of mathematical reconciliation, not of REPORT/PLAN content or relationship precedence.

**Evidence-state determining fact:** reproduced. All cited numbers and locations match the exact source, all19 comparator witnesses are precision-feasible when independently recalculated, and both affected tuples remain outside the diagnostic P half-unit intervals under exhaustive conservative bounds. No source transcription correction was needed. This evidence-record state does not identify the actual author implementation or adjudicate the candidate.

**Exact remaining human question:** Which fitted analysis, contrast covariance, confidence critical value/reference distribution and omnibus reference distribution/degrees of freedom produced the eTable11 physical-function six-/twelve-month P=.005/.001 and three MD95%CIs; do these columns refer to the same outcome, time, covariance and estimand; and which reported values should be extracted if their inferential constructions differ?

Completion: C018 separately rechecked; both affected rows and all19 corroborating rows covered; five distinct supplied-source pages visually inspected; one evidence state reproduced; zero source-reading gaps. Exact inferential definitions and fitted inputs named above remain unresolved. Every supplied source and previously written artifact was preserved.

