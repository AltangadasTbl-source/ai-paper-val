# Numeric Consistency Review

## Scope and checking rules

This review applies the numeric inventory N001-N042 to the complete mapped DOC-001/DOC-002/DOC-003 scope. It checks printed arithmetic, totals, subgroup sums, numerators, denominators, percentages, missingness/evaluated populations, population identity, rounding, labels/scales/units, rate-versus-count distinctions, and repeated values. A displayed percentage is treated as a one-decimal percentage with a rounding tolerance of plus or minus 0.05 percentage points unless the table prints a different precision. Design assumptions, protocol versions, and explicitly non-mutually-exclusive event rows are not treated as arithmetic contradictions merely because they differ or do not sum.

## Candidate proposals

### NP-01 — BA female percentage does not reconcile with the printed group denominator

- **Primary category:** Denominator, proportion, or total inconsistency.
- **Exact source locations:** DOC-001, `jama_sun_2024_oi_240088_1746815064.14747.pdf#page=6`, Table 1, Sex; direct PDF p. 6.
- **Printed inputs:** Balloon angioplasty group `n = 249`; male `172 (69.1)`; female `77 (30.1)`.
- **Direct observation:** The table prints both the group denominator and the female count/percentage. The two sex counts sum to 249.
- **Reproducible rule and calculation:** For a row marked `No. (%)`, percentage = 100 x count / printed group n. `100 x 77 / 249 = 30.9237%`, which rounds to `30.9%` at one decimal. Printed `30.1%` differs by `0.8237` percentage points from the unrounded value.
- **Tolerance:** Expected one-decimal interval for 30.9% is [30.85%, 30.95%); 30.1% is outside. The male calculation `172/249 = 69.0763% -> 69.1%` is coherent.
- **Inference and alternatives:** This is a direct count/denominator/percentage mismatch. A different unprinted female denominator, a transcription error in count, percentage, or header, or an unstated population restriction could explain it; none is printed in the table.
- **Quality-control relevance:** The baseline sex proportion is a common structured-data extraction field.
- **Exact human question:** Which printed item should be corrected or qualified: BA female count 77, BA group denominator 249, or BA female percentage 30.1%?

### NP-02 — BA ischemic-stroke percentage is outside ordinary one-decimal rounding from its printed numerator and denominator

- **Primary category:** Denominator, proportion, or total inconsistency.
- **Exact source locations:** DOC-001, `jama_sun_2024_oi_240088_1746815064.14747.pdf#page=6`, Table 1, Qualifying event; DOC-002, `joi240088supp1_prod_1746815064.21247.pdf#page=14`, Table S1, ischemic stroke.
- **Printed inputs:** Both locations print BA group `n=249` and ischemic stroke `215 (86.4)`; the main table also prints TIA `34 (13.7)`.
- **Direct observation:** The same count/percentage pairing is repeated in the main article and Supplement 1. `215 + 34 = 249`.
- **Reproducible rule and calculation:** `100 x 215 / 249 = 86.3454%`. At one decimal it rounds to `86.3%`; the displayed `86.4%` is `0.0546` percentage points above the unrounded value.
- **Tolerance:** A displayed 86.4% requires an unrounded value in [86.35%, 86.45%) under ordinary nearest one-decimal rounding. 86.3454% is outside by 0.0046 percentage points. The complement `34/249 = 13.6546% -> 13.7%` is coherent.
- **Inference and alternatives:** Direct observation establishes the repeated count/denominator/display relationship; the rounding diagnosis is inferred. A nonstandard rounding convention, a hidden denominator, or an error propagated across the two tables are alternatives.
- **Quality-control relevance:** The reported qualifying-event mix is repeated across paper and supplement and may be copied as a baseline composition.
- **Exact human question:** Was 86.4% produced under a documented rounding convention, or should the repeated BA ischemic-stroke percentage be 86.3% (or another printed input be changed)?

### NP-03 — Procedural table header labels 249 participants while its procedure rows use the 241 who underwent BA

- **Primary category:** Denominator, proportion, or total inconsistency.
- **Exact source locations:** DOC-002, `joi240088supp1_prod_1746815064.21247.pdf#page=17`, Table S4 and footnote a.
- **Printed inputs:** Header: `Balloon angioplasty group (n=249)`. Footnote: `241 of 249 patients underwent BA`. Procedure-time rows: `182 (75.5)`, `48 (19.9)`, `11 (4.6)`; residual-stenosis rows `214 (88.8)`, `19 (7.9)`, `8 (3.3)`; complications `42 (17.4)`.
- **Direct observation:** The procedure-category counts sum to 241 in each applicable set: `182+48+11=241` and `214+19+8=241`.
- **Reproducible rule and calculation:** `182/241=75.5%`, `214/241=88.8%`, and `42/241=17.4%`; those printed percentages use 241. They would instead be 73.1%, 85.9%, and 16.9% using the column-header 249.
- **Tolerance:** All cited rows reconcile to 241 at one decimal and not to 249; no rounding tolerance can reconcile 75.5% with 182/249.
- **Inference and alternatives:** Directly, the header and footnote name different population sizes; inferentially, the procedure rows appear to use the 241 treated patients. The table may intentionally retain a trial-arm header while the footnote is intended to define the analysis subset, but the applicable denominator is not repeated in the row/header label.
- **Quality-control relevance:** A reader can calculate procedural-complication and technical-success percentages with the wrong denominator.
- **Exact human question:** Should the Table S4 procedure-result column be explicitly labelled `n=241` (with a separate 249 randomized-arm context), or is another denominator intended for the displayed procedure percentages?

### NP-04 — Centre-adjusted primary BA percentage conflicts with the table header denominator

- **Primary category:** Denominator, proportion, or total inconsistency.
- **Exact source locations:** DOC-002, `joi240088supp1_prod_1746815064.21247.pdf#page=19`, Table S6.
- **Printed inputs:** BA header `n=249`, primary outcome `9 (3.9)`; AMM header `n=252`, primary outcome `34 (13.5)`.
- **Direct observation:** The table labels its cells `Data are n (%)` and prints BA n=249.
- **Reproducible rule and calculation:** `9/249 x 100 = 3.6145% -> 3.6%`, not 3.9%. `9/233 x 100 = 3.8627% -> 3.9%`; the latter is the BA per-protocol total shown elsewhere in the supplied supplement. AMM `34/252 = 13.4921% -> 13.5%` reconciles to its printed header.
- **Tolerance:** 3.9% at one decimal requires [3.85%, 3.95%); 9/249 is outside. 9/233 is inside.
- **Inference and alternatives:** The mismatch between BA header and BA percentage is direct. It is an inference, not an established correction, that 233 was used; a centre-adjustment-specific risk-set convention or an unprinted eligible subset could also be relevant.
- **Quality-control relevance:** The table reports a centre-adjusted primary analysis and is a likely source for extracting its event risk alongside the HR.
- **Exact human question:** What BA denominator produced `9 (3.9)` in Table S6, and should that denominator be printed instead of or in addition to `n=249`?

### NP-05 — Site-interaction table headers do not match the denominators implied by its displayed site percentages

- **Primary category:** Denominator, proportion, or total inconsistency.
- **Exact source locations:** DOC-002, `joi240088supp1_prod_1746815064.21247.pdf#page=20`, Table S7.
- **Printed inputs:** Headers state BA `N=233` and AMM `N=238`; site totals are Beijing Tiantan Hospital `256` and Other centers `245`. BA/AMM cells are `4 (2.9)` and `19 (16.1)` for Beijing, and `7 (6.3)` and `15 (11.2)` for other centers.
- **Direct observation:** The site totals add to 501. The four printed percentages cannot use the two column headers as their denominators.
- **Reproducible rule and calculation:** Header calculations are `4/233=1.7%`, `19/238=8.0%`, `7/233=3.0%`, and `15/238=6.3%`, not 2.9%, 16.1%, 6.3%, and 11.2%. The displayed values instead correspond (within one decimal) to site-by-arm denominators `4/138=2.9%`, `19/118=16.1%`, `7/111=6.3%`, `15/134=11.2%`; these inferred denominators sum to BA 249, AMM 252, and each site total 256/245.
- **Tolerance:** None of the first three cited percentages is reconcilable to its printed group header by one-decimal rounding. The inferred site-by-arm denominators are diagnostic, not printed labels.
- **Inference and alternatives:** Directly, table headers and cells conflict. The likely explanation is that the values use site-specific randomized/eligible arm totals while the headers erroneously show per-protocol totals; an unstated site-specific analytic population is another alternative.
- **Quality-control relevance:** The table supplies effect-modification context; denominators determine the subgroup event risks presented with the interaction result.
- **Exact human question:** What are the intended BA and AMM denominators within each site, and should Table S7 replace or supplement the printed `N=233`/`N=238` headers?

### NP-06 — Per-protocol outcome percentages use unlabelled 233/238 denominators rather than the printed 249/252 headers

- **Primary category:** Denominator, proportion, or total inconsistency.
- **Exact source locations:** DOC-002, `joi240088supp1_prod_1746815064.21247.pdf#page=21`, Table S8.
- **Printed inputs:** Table title `per-protocol population (PPS)`; headers BA `n=249`, AMM `n=252`. Rows include primary `9 (3.9)`/`33 (13.9)`, 30-day `6 (2.6)`/`4 (1.7)`, later stroke `1 (0.4)`/`18 (7.6)`, and revascularization `3 (1.3)`/`20 (8.4)`.
- **Direct observation:** Every displayed event percentage aligns with BA 233 and AMM 238, not the headers.
- **Reproducible rule and calculation:** Examples: `9/233=3.9%` and `33/238=13.9%`; `6/233=2.6%` and `4/238=1.7%`; `20/238=8.4%`. With printed headers, `9/249=3.6%`, `33/252=13.1%`, and `20/252=7.9%`.
- **Tolerance:** The discrepancies exceed one-decimal rounding tolerance. The 233/238 figures match the main flow's per-protocol totals, but this is comparator evidence rather than an unprinted table label.
- **Inference and alternatives:** The direct contradiction is headers versus percentages. A header transcription/production error is plausible; another possibility is that the title's PPS definition is not fully represented by the table header.
- **Quality-control relevance:** Per-protocol event risks, as well as the sensitivity estimate, could be extracted with the wrong denominators.
- **Exact human question:** Are the intended Table S8 headers BA `n=233` and AMM `n=238`, and if not, how were the printed PPS percentages calculated?

### NP-07 — As-treated outcome percentages use unlabelled 247/254 denominators rather than the printed 249/252 headers

- **Primary category:** Denominator, proportion, or total inconsistency.
- **Exact source locations:** DOC-002, `joi240088supp1_prod_1746815064.21247.pdf#page=22`, Table S9.
- **Printed inputs:** Table title `as-treated population (ATS)`; headers BA `n=249`, AMM `n=252`; primary `11 (4.5)`/`34 (13.4)`, 30-day `8 (3.3)`/`4 (1.6)`, later stroke `1 (0.4)`/`19 (7.5)`, revascularization `3 (1.2)`/`21 (8.3)`.
- **Direct observation:** The printed percentages do not reconcile to the headers but do reconcile to the as-treated denominators printed in Supplement 1 Table S10.
- **Reproducible rule and calculation:** `11/247=4.5%`, `34/254=13.4%`, `8/247=3.2%` (displayed 3.3% is at the one-decimal half-boundary under usual rounding), `19/254=7.5%`, and `21/254=8.3%`. With headers, `11/249=4.4%` and `34/252=13.5%`. The Table S10 comparison prints ATS `N=247` and `N=254`.
- **Tolerance:** The primary outcome and most component cells are not reconcilable to 249/252. The 8/247 cell has a separate borderline rounding issue but does not reconcile to the header either.
- **Inference and alternatives:** Directly, the header denominators and central event percentages conflict. The likely intended denominators are 247/254, but this remains an inference from another supplied table.
- **Quality-control relevance:** As-treated risks may be interpreted as randomized-arm risks if the headers remain unchanged.
- **Exact human question:** Should Table S9 identify ATS denominators as BA `n=247` and AMM `n=254`, and what rounding convention was used for `8 (3.3)`?

### NP-08 — Reported baseline stenosis categories include values outside the stated eligibility range

- **Primary category:** Analysis-unit or population inconsistency.
- **Exact source locations:** DOC-001, `jama_sun_2024_oi_240088_1746815064.14747.pdf#page=2`, eligibility; `jama_sun_2024_oi_240088_1746815064.14747.pdf#page=6`, Table 1, Stenosis of symptomatic artery; `jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5`, Figure 1, exclusions for angiographic stenosis <70% and target-artery occlusion.
- **Printed inputs:** Eligibility is 70%-99% atherosclerotic stenosis. Table 1 (BA n=249; AMM n=252) reports 60%-69%: BA 0, AMM 2 (0.8); 100%: BA 1 (0.4), AMM 1 (0.4). Figure 1 reports screening exclusions for angiographic stenosis <70% and target-artery occlusion.
- **Direct observation:** Four analysed-table participants are placed in categories outside the stated 70%-99% range: two below 70% and two at 100%.
- **Reproducible rule and calculation:** `0+2+1+1=4` participants outside the stated interval. `2/501=0.4%` and `2/501=0.4%` for the two outside-range categories, using the Table 1 group totals.
- **Tolerance:** Not a rounding check; 60%-69% and 100% are categorically outside a closed 70%-99% eligibility interval.
- **Inference and alternatives:** Direct observation is the threshold/category conflict. Different imaging time points, a post-enrollment central measurement, protocol deviations retained in the analysis, or a table-label issue could reconcile it, but the cited locations do not state such an explanation.
- **Quality-control relevance:** This affects the identity of the analysed stenosis population and the interpretation of the baseline distribution.
- **Exact human question:** Why does the analysed baseline table include two <70% and two 100% stenosis categories despite the stated 70%-99% eligibility and the flow exclusions; were they measured at a different time point or retained protocol deviations?

### NP-09 — Supplementary trial graphic gives a different 30-day follow-up tolerance from the main/protocol schedule

- **Primary category:** Measure, label, or scale inconsistency.
- **Exact source locations:** DOC-002, `joi240088supp1_prod_1746815064.21247.pdf#page=6`, study-design graphic; DOC-001, `jama_sun_2024_oi_240088_1746815064.14747.pdf#page=3`, follow-up schedule; DOC-003, `joi240088supp2_prod_1746815064.36071.pdf#page=15`, schedule of assessments.
- **Printed inputs:** DOC-002 prints `30±3 days`; DOC-001 and DOC-003 print `30±7 days`. The subsequent 90-day, 6-month, and 1-year labels are otherwise aligned in the mapped schedules.
- **Direct observation:** The three supplied sources use different numerical tolerance values for the nominal 30-day visit.
- **Reproducible rule and calculation:** Identity rule for a matched visit label: source A tolerance must equal source B tolerance unless a distinct visit/procedure is identified. `+/-3 days != +/-7 days`; the allowed window widths are 6 versus 14 days.
- **Tolerance:** None; these are exact printed schedule labels, not rounded measurements.
- **Inference and alternatives:** It is direct that the numeric labels differ. The graphic may intentionally describe a different clinical follow-up schedule, may be simplified, or may contain a production error; the graphic does not supply a distinction.
- **Quality-control relevance:** Follow-up windows define timepoint alignment for outcome collection and can be copied into protocol or trial-characteristic extraction.
- **Exact human question:** Does the supplementary `30±3 days` label identify a distinct visit convention, or should it match the `30±7 days` schedule in the main article and protocol?

### NP-10 — Original protocol synopsis and body disagree on the lower stroke-eligibility bound

- **Primary category:** Measure, label, or scale inconsistency.
- **Exact source locations:** DOC-003, `joi240088supp2_prod_1746815064.36071.pdf#page=7`, V2.0 synopsis; `joi240088supp2_prod_1746815064.36071.pdf#page=21`, V2.0 body eligibility.
- **Printed inputs:** The synopsis says ischemic stroke `21-90 days` before enrollment. The body eligibility text says ischemic stroke `14-90 days` before enrollment.
- **Direct observation:** Both numbers occur within the supplied original Protocol V2.0.
- **Reproducible rule and calculation:** A same-version inclusion criterion should specify one lower bound unless the source identifies separate populations. `21 days - 14 days = 7 days`; the two eligibility intervals are not identical.
- **Tolerance:** None; the values are exact threshold labels.
- **Inference and alternatives:** Directly, the threshold differs. A synopsis typo, later body amendment not reflected in the synopsis, translation issue, or distinct unlabelled eligibility stratum are alternatives; none is explained at these locations.
- **Quality-control relevance:** The lower bound changes the defined recruitable stroke population.
- **Exact human question:** Which lower bound governed Protocol V2.0 enrolment—14 or 21 days after ischemic stroke—and should the other occurrence be corrected or version-qualified?

### NP-11 — BA 3-month aspirin percentage does not reconcile with the stated trial-arm denominator

- **Primary category:** Denominator, proportion, or total inconsistency.
- **Exact source locations:** DOC-002, `joi240088supp1_prod_1746815064.21247.pdf#page=16`, Table S3.
- **Printed inputs:** BA group `n=249`; receiving aspirin at 3 months `234 (93.9)`.
- **Direct observation:** Table S3 identifies values as `n (%)` and gives no row-specific evaluated denominator.
- **Reproducible rule and calculation:** `100 x 234 / 249 = 93.9759%`, which rounds to `94.0%` at one decimal. Printed 93.9% differs by 0.0759 percentage points from the unrounded value.
- **Tolerance:** A one-decimal 93.9% requires [93.85%, 93.95%); 93.9759% is outside. The calculation assumes the only printed denominator, 249.
- **Inference and alternatives:** The printed count/denominator/percentage mismatch is direct under the column label. A row-specific 249-plus/missingness convention cannot yield a denominator larger than the trial arm without a stated reason; a hidden 250 denominator or an incorrect header/count/percentage are alternatives.
- **Quality-control relevance:** Medication adherence/use proportions are commonly extracted as follow-up treatment exposure.
- **Exact human question:** What denominator was used for BA aspirin use at 3 months, and should `234 (93.9)` or the column denominator be corrected/qualified?

### NP-12 — Figure S1 repeats “2nd meeting” for three separate dated adjudication streams

- **Primary category:** Measure, label, or scale inconsistency.
- **Exact source locations:** DOC-002, `joi240088supp1_prod_1746815064.21247.pdf#page=10`, Figure S1 direct-render labels.
- **Printed inputs:** The four streams are labelled `1st meeting` (2021/05/30), `2nd meeting` (2021/11/20), `2nd meeting` (2022/09/07), and `2nd meeting` (2023/04/10), with reported cases 19, 27, 26, and 15 respectively.
- **Direct observation:** Three chronologically distinct dates and count streams use the same ordinal label.
- **Reproducible rule and calculation:** For a sequential meeting-number label, four distinct chronological meetings require four distinct ordinals unless the figure states that an ordinal is reused. Dates are strictly ordered and the labels contain one `1st` and three `2nd` instances.
- **Tolerance:** Not applicable; ordinal labels are exact text/numeric identifiers.
- **Inference and alternatives:** Directly, the repetition exists. The later labels may intentionally mean a second meeting of a different unprinted cycle, or they may be production errors; the figure does not define an alternate cycle.
- **Quality-control relevance:** The figure's counts reconcile arithmetically, but duplicated meeting identifiers make the event-adjudication timeline ambiguous.
- **Exact human question:** Are the 2022/09/07 and 2023/04/10 streams intended to be the third and fourth CEC meetings, or is there an unprinted reason for repeating `2nd meeting`?

### NP-13 — Recurring-visit sentence ambiguously repeats visit numbers 9 and 11

- **Primary category:** Measure, label, or scale inconsistency.
- **Exact source locations:** DOC-003, `joi240088supp2_prod_1746815064.36071.pdf#page=35`, Protocol V2.0 recurring-visit paragraph; identical text at `joi240088supp2_prod_1746815064.36071.pdf#page=96`, Protocol V2.3; schedule comparator at PDF p. 15.
- **Printed inputs:** The post-year-one recurring list is `visit 8, visit 9, visit 10, visit 11, visit 9, and visit 11`.
- **Direct observation:** The sentence repeats two ordinal visit identifiers in both protocol versions; the schedule identifies visits 8-11 as the four recurring visits.
- **Reproducible rule and calculation:** The text contains six occurrences but four unique labels {8, 9, 10, 11}. This is ambiguous between a six-item sequence and a four-visit list followed by a face-to-face subset (visits 9 and 11).
- **Tolerance:** Not applicable; these are exact ordinal schedule labels.
- **Inference and alternatives:** The repeated labels may be deliberate subset references whose syntax is unclear, or they may be typographic errors. The sentence does not resolve the structure.
- **Quality-control relevance:** Visit labels anchor longitudinal measurement, visit attendance, and late follow-up event timing.
- **Exact human question:** Does the sentence list six sequential visits or four recurring visits followed by the visit 9/11 face-to-face subset, and should punctuation or wording clarify it?

### NP-14 — As-treated 30-day BA percentage has a second, borderline rounding ambiguity after its header mismatch

- **Primary category:** Numeric or arithmetic inconsistency.
- **Exact source locations:** DOC-002, `joi240088supp1_prod_1746815064.21247.pdf#page=22`, Table S9; comparator denominator DOC-002, `joi240088supp1_prod_1746815064.21247.pdf#page=23`, Table S10 ATS row.
- **Printed inputs:** Table S9 reports BA 30-day stroke/death `8 (3.3)`; Table S10 identifies ATS BA `N=247`.
- **Direct observation:** The table's printed header is n=249 (already addressed in NP-07), while the related ATS table prints N=247.
- **Reproducible rule and calculation:** With the likely ATS denominator, `100 x 8 / 247 = 3.2389%`, which ordinarily rounds to `3.2%`, not `3.3%`. With the Table S9 header, `8/249=3.2129% -> 3.2%`. Thus neither printed denominator yields 3.3% under ordinary nearest one-decimal rounding.
- **Tolerance:** A displayed 3.3% requires [3.25%, 3.35%); both 3.2389% and 3.2129% are outside. This is a distinct rounding issue from the population-header issue in NP-07.
- **Inference and alternatives:** Direct observation is the count and displayed percentage; the 247 denominator is a source-grounded comparator. A nonstandard rounding convention or an unprinted risk-set denominator can explain the display.
- **Quality-control relevance:** It affects the reported early event risk in the as-treated sensitivity analysis.
- **Exact human question:** What numerator/denominator and rounding rule generated BA `8 (3.3)` for the Table S9 30-day as-treated outcome?

## Checks that did not yield a candidate proposal

- Screening, allocation, and centre-enrolment totals reconcile where the source gives mutually exclusive components.
- Table 2 primary and secondary count/percentage relationships reconcile within printed precision; component counts were not added to composite counts because the table expressly reports multiple events per participant.
- Figure S4/S5 mRS category counts sum to their displayed BA and AMM denominators at both time points.
- Table S5 revascularization row and column totals reconcile; Table S12 percentages use their immediately preceding evaluated counts.
- Procedure-component counts were not required to sum to the number of participants with any complication because the source does not state that a participant can have only one complication.
- Protocol/SAP historical versus revised sample-size values were treated as versioned planning assumptions, not contradictory observed trial totals.
- No candidate was created solely from a display-zero P value; none was present in this numeric scope.

## Counts and limitations

- **N relationships checked:** 42.
- **Distinct candidate proposals:** 14.
- **Direct-PDF confirmation performed for every proposal:** yes.
- **Limitations:** There are no participant-level data, risk-set logs, or table-production specifications. Where a denominator is inferred from another supplied table, it is explicitly marked as inference and the human question asks for the authorial definition rather than asserting a correction. Inferential-statistical compatibility, including HR/CI/P-value relationships, is outside this numeric stage.
