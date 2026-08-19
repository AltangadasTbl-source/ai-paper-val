# Numeric consistency review: N189--N282

## Scope, evidence, and checking rule

This shard covers exactly the 94 inventory relationships N189--N282.  I used the inventory as the scope crosswalk and the named extraction shards as locators, then rechecked the two proposed discrepancies against the direct supplied PDF.  The SAP records are prospective definitions, assumptions, and planning quantities rather than observed results; a planned value was not treated as inconsistent merely because the supplied package does not contain an observed matched result.  For displayed count/percentage cells, the rule was `100 x count / stated column N`, rounded to one decimal by ordinary half-up/nearest one-decimal display (tolerance 0.05 percentage points, subject to the displayed rounding convention).  For whole-percent enrollment values the tolerance is 0.5 percentage points.  For verbal approximations (`about`, `approximately`, `~`) I did not manufacture a numeric tolerance or candidate without a conflicting same-definition value.

Direct sources: `joi190092supp3_prod.pdf` (SAP; physical PDF pages cited below) and `joi190092supp1_prod.pdf` (Supplementary Results; physical PDF pages cited below).  The direct recheck used `pdftotext -layout` on Supplementary Results pp. 5, 14--15 and visual confirmation of p. 15.  Reusable evidence locators were `parts/support_sap_pp001_032.md`, `parts/support_sap_pp033_064.md`, `parts/support_sap_pp065_083.md`, and `parts/support_supp_results_pp001_016.md`.

## Complete relationship register

`PASS` means that the applicable source-grounded arithmetic, total/subgroup, denominator/percentage, population, measure/label/scale/unit, rate-versus-count, duplicate-value, and direct-source checks found no candidate draft. `NOT APPLICABLE` means the mapped relationship is a single planned definition/administrative convention with no displayed arithmetic or matched same-definition observed comparator in this assigned scope; this is not a scientific-coverage omission.

| N ID | Direct source location and printed relationship checked | Applied check and reproducible result | Outcome |
|---|---|---|---|
| N189 | SAP p. 6, Phase I continuation, months 9/12 | Schedule/phase and removal rule are internally singular; no count/denominator comparator. | NOT APPLICABLE |
| N190 | SAP p. 7, 5-month success sustained >=28 days to month 6 | Time threshold and endpoint labels agree within the definition. | PASS |
| N191 | SAP p. 7, secondary outcome/time inventory | Endpoint names are distinct; no repeated-value or unit conflict is displayed. | PASS |
| N192 | SAP p. 7, 12-month steroid-discontinuation control | Measure is explicitly a probability, not a count/rate. | PASS |
| N193 | SAP p. 8, Aim 2 rescue success fraction at 6 months | Population (initial-treatment failures), time, and fraction label are aligned. | PASS |
| N194 | SAP p. 8, Aim 2 every-4-week follow-up to 6 months | Visit cadence and endpoint are a definition; no arithmetic comparator. | NOT APPLICABLE |
| N195 | SAP p. 8, four sites/two treatment arms | Site count and two-arm labels are distinct dimensions; no total is asserted. | PASS |
| N196 | SAP p. 9, blocks 4 with probability 2/3 and 6 with 1/3 | `2/3 + 1/3 = 1`; probabilities are complete and site-stratified. | PASS |
| N197 | SAP p. 10, five-character ID; sites 1--4; example 4J101 | ID specification is internally consistent: one digit + one letter + three digits = five. | PASS |
| N198 | SAP pp. 11--12, eye classes A--E | Five named categories agree with A--E enumeration. | PASS |
| N199 | SAP p. 12, patient randomization and 25 bilateral types | `5 x 5 = 25`; patient/eye units are expressly separated. | PASS |
| N200 | SAP p. 12, 5x5 eligibility table | Rule is at least one class-C eye; table and stated patient criterion agree. | PASS |
| N201 | SAP p. 12, month-6 eye-scoring table | Baseline E=NA and A--D rules are displayed as definitions, not totals. | PASS |
| N202 | SAP p. 13, both-eye patient success and visit schedule | Patient outcome is expressly distinguished from eye observations. | PASS |
| N203 | SAP p. 13, worst observed value for unavailable field | Missing-field handling and eye-level secondary population are explicit; no numeric contradiction. | PASS |
| N204 | SAP p. 14, unassessable/LOCF/failure rule at visits 6/12 | Baseline versus follow-up assessment rules use compatible time labels. | PASS |
| N205 | SAP pp. 14--15, principal-variable inventory | BSCVA is two observations/patient; other outcomes retain their stated patient/eye units. | PASS |
| N206 | SAP p. 15, location coding 0/1 and outcome window -2 to +4 weeks | Two codes and window endpoints are explicit; no unit/scale conflict. | PASS |
| N207 | SAP p. 16, `X1i=0/1`, `Yi=1/0`, missingness and AE discontinuation | Treatment, outcome, and missing/failure coding are differentiated, not conflated. | PASS |
| N208 | SAP pp. 16--17, mutually exclusive site indicators and site-1 baseline | Exactly one site indicator equals 1 per patient; stated reference is compatible. | PASS |
| N209 | SAP p. 17, anatomy subgroups and stratum RRs | Three-level enrollment and two-level history variables are separately named. | PASS |
| N210 | SAP pp. 18--20, secondary-outcome definitions | Each measure retains an outcome/time/unit label; no displayed duplicate expected to differ. | PASS |
| N211 | SAP p. 19, BSCVA eligible eyes, LOCF, logMAR 2.0 fallback | Eye-level population and 2.0 fallback are explicit; no incompatible denominator. | PASS |
| N212 | SAP p. 20, edema fraction and thickness adjusted for baseline | Fraction and micron thickness are separate measures; no rate/count conflation. | PASS |
| N213 | SAP p. 21, rescue success proportions with 95% CI | Contrast paths and success-proportion measure are separately stated. | PASS |
| N214 | SAP p. 22, planned diagnostic/sensitivity methods | Methods are alternatives, not repeated estimates. | NOT APPLICABLE |
| N215 | SAP pp. 22--23, total 216; 108/group; pc=.4; pi=.6; 20 points; 10% loss | `108 + 108 = 216`; `.6 - .4 = .20`; `(.6+.4)/2=.5`. Power is explicitly approximate/model-based. | PASS |
| N216 | SAP p. 23, 80%/90% power sensitivity table | In every row, printed Drug-B rate equals Drug-A rate plus printed effect after whole-percent rounding (e.g., 20+18=38; 60+19=79). | PASS |
| N217 | SAP p. 24, >80% power/25 points; 5% additional loss; ~78%/20 points | `10% + 5%` are sequential planned loss assumptions; values are labelled approximate. | PASS |
| N218 | SAP p. 24, 108/group; 10% loss; 2.47 months; median 3.5; alpha .05 | Time unit is months throughout; `lambda_C=log(2)/3.5` carries reciprocal-month scale. | PASS |
| N219 | SAP pp. 24--25, BSCVA SD 6.5; 108/group; 2.63 letters; QOL SD 8.4, r=.6, corrected SD 6.72 | `8.4 x sqrt(1-.6^2)=8.4 x .8=6.72`; BSCVA is letters and QOL points, not merged. | PASS |
| N220 | SAP p. 25, discontinuation 13/5% versus 4/5%; edema 19 vs 38%; thickness 65 microns | `19 x 2 = 38`; reason-specific discontinuation rates and micron thickness retain distinct labels. | PASS |
| N221 | SAP pp. 25--27, Aim-2 availability N0=108, r1=.9, r2=.95; 58.3/55.4 and 38.9/36.9 | Enrollment: `108*.9*(1-.4)=58.32` and `108*.9*(1-.6)=38.88`; completion times `.95` = `55.404`, `36.936`; displayed one-decimal values and floor text 58/38 reconcile. | PASS |
| N222 | SAP pp. 26--27, rescue power scenarios | Each row preserves its stated sample sizes, success paths, and approximate power; reversed .15/.42 row is a distinct contrast, not a duplicate. | PASS |
| N223 | SAP pp. 28--29, four missing-data analyses; 10 regression and 10 hot-deck imputations; visits 1:6 | Four methods and ten-replication counts are explicit; complete-case primary label is not a numerical contradiction. | PASS |
| N224 | SAP p. 29, ~three-fourths Aravind; alpha .05 | Approximate site share and alpha are different measures; no conflicting total. | PASS |
| N225 | SAP p. 30, 7--8/month for 2.5 years; 25% lower accrual; 3y3m; looks 1/3,2/3 | `2.5 years / .75 = 3.33 years` = 3 years 4 months approximately, compatible with the stated planning duration rounding. | PASS |
| N226 | SAP p. 30, analysis timing and R >=2.12 | Phase/time labels are distinct; version threshold is not a numeric result. | NOT APPLICABLE |
| N227 | SAP p. 31, analysis populations and per-protocol <50% receipt | Screening/safety/ITT/per-protocol populations are definitions; no reported count claimed. | PASS |
| N228 | SAP p. 31, deviation counts/percentages and discontinuation test | Count/percentage description is distinct from Fisher/chi-square test labels. | PASS |
| N229 | SAP p. 32, `NA`, coding, units | Missing-value label and examples retain unambiguous logMAR/thickness units. | PASS |
| N230 | SAP p. 32, monthly monitoring and final disposition frequencies | Frequency/count categories are planned outputs without displayed totals. | NOT APPLICABLE |
| N231 | SAP pp. 33--34, interim looks ~1/3 and ~2/3, subject 72 | Two looks and information fractions agree; "about" limits exact calendar arithmetic. | PASS |
| N232 | SAP pp. 35--36, pooled AE proportions versus recurrent-event rates | Directly distinguishes subject proportion from all/recurrent-event rate and randomized-arm exposure. | PASS |
| N233 | SAP p. 37, `NA` = not available | Missing-value label is singular and does not imply zero or a count. | PASS |
| N234 | SAP pp. 45--46, ITT 6-month success and Phase I months 6--12 | Population, endpoint, and phase/time labels are aligned. | PASS |
| N235 | SAP pp. 47--48, secondary endpoint inventory | Time-to-event, proportion, rate, scales, and discontinuation categories are distinct. | PASS |
| N236 | SAP p. 48, rescue failure/switch/4-week visits/6-month success | Failure population and rescue time origin are explicit. | PASS |
| N237 | SAP pp. 49--50, nine sites; blocks 4 at 2/3 and 6 at 1/3 | `2/3+1/3=1`; text correctly warns block distribution differs from person distribution. | PASS |
| N238 | SAP p. 50, site 1--9 plus checksum and 001 | One site digit + one letter + three digits = five characters. | PASS |
| N239 | SAP pp. 52--54, patient assignment/primary analysis; 5x5 tables | `5 x 5=25` table structure; patient and eye analysis units are explicitly separated. | PASS |
| N240 | SAP pp. 53--54, unavailable-field rule and schedules | Months 9/12 apply to Phase I; 6-month schedule applies to both phases as stated. | PASS |
| N241 | SAP pp. 54--55, baseline counts/percentages and outcome inventory | Two BSCVA observations/patient is marked eye-level; patient outcome counts are not conflated. | PASS |
| N242 | SAP p. 56, outcome windows -2 to +4 weeks | Same window width is used consistently for named 6- and 12-month endpoints. | PASS |
| N243 | SAP p. 56, 0/1 treatment and outcome coding | Reference/treatment and success/failure/missing coding are explicit and nonconflicting. | PASS |
| N244 | SAP pp. 57--58, anatomy/country/site coding | Two-level history, three-level enrollment, and country/site indicators retain distinct scales. | PASS |
| N245 | SAP pp. 58--60, endpoint definitions | Patient fraction, per-eye BSCVA, ordinal haze, and four-category discontinuation remain correctly labelled. | PASS |
| N246 | SAP p. 60, 10% non-inferiority margin and lower 95% CI wording | Direct observation: wording lacks contrast orientation; no matched reported value permits arithmetic contradiction. Human question only if used for a result: what signed contrast does the lower limit represent? | NOT APPLICABLE |
| N247 | SAP pp. 61--62, rescue proportions/95% CIs and LTFU sensitivity | Rescue paths and comparison population are distinguished. | PASS |
| N248 | SAP pp. 63--64, 2N formula; pc=.4, pi=.6, alpha=.05, 80%, 108/group/216 | Same reconciliation as N215: `2N=216`, `.6-.4=.2`, `pbar=.5`; 10% loss is a stated planning assumption. | PASS |
| N249 | SAP p. 64, sensitivity table and >80%/25-point subgroup plan | Each displayed Drug-B rate equals Drug-A plus effect at shown precision; subgroup statement is approximate. | PASS |
| N250 | SAP p. 65, additional 5% loss plus 10%; ~78% for 20% | Sequential loss periods and 12-month endpoint are explicit; approximate power needs no forced exact reconstruction. | PASS |
| N251 | SAP p. 65, 6-month censoring, median 3.5 months, 108/group, 2.47 months | All time quantities use months; treatment direction is declared in source. | PASS |
| N252 | SAP p. 65, BSCVA SD 6.5 letters and 2.63-letter difference | BSCVA retains its letters scale and direction; no QOL scale is combined with it. | PASS |
| N253 | SAP p. 65, QOL SD 8.4, r=.6, corrected SD 6.72, 2.57 points | `8.4 x sqrt(1-.6^2)=6.72`; QOL points and 0--100 scale are explicit. | PASS |
| N254 | SAP p. 65, discontinuation reason-specific rates 13/5 vs 4/5 | Tolerability and safety proportions are not added or mislabeled as a recurrent-event rate. | PASS |
| N255 | SAP p. 66, 61%; edema 38% and 19/38%; thickness 65/160/100 microns | `19 x 2=38`; proportion and micron measures are distinct. | PASS |
| N256 | SAP p. 66, rescue success probabilities/95% CI by failure reason | Probability, CI, initial drug, and reason stratum are all named. | PASS |
| N257 | SAP p. 66, availability formula N0=108, r1=.9, sj=.6/.4, r2=.95 | Formula has the correct complement `(1-sj)` for initial failure and labels group paths. | PASS |
| N258 | SAP p. 67, B/A 58.3/55.4 and A/B 38.9/36.9; floor 58/38 | `108*.9*.6=58.32`, then `*.95=55.404`; `108*.9*.4=38.88`, then `*.95=36.936`; one-decimal table and floor text reconcile. | PASS |
| N259 | SAP p. 67, p0=.15, p1=.42, power .87; 17-point ~80% statement | `.42-.15=.27`; separate 17-point statement is explicitly a different scenario, not a contradictory repeat. | PASS |
| N260 | SAP pp. 67--68, seven rescue-power sensitivity rows | Each row retains stated orientation; power is approximate/model-based and no two same-input rows disagree. | PASS |
| N261 | SAP p. 68, four missing-data analyses and complete-case primary | Endpoint is six-month success in each alternative; no denominator/count is printed. | PASS |
| N262 | SAP p. 68, 10 MI and 10 hot-deck replications; visit 1:6 | Replication counts and repeated-measure index are internally consistent. | PASS |
| N263 | SAP p. 70, injection 90 days after enrollment | 90-day sensitivity threshold and failure/success classification are explicit. | PASS |
| N264 | SAP p. 70, ~three-fourths; alpha .05; 7--8/month; 2.5y/3y3m; 1/3,2/3 looks | Mixed measures retain their units; calendar statement is approximate planning, not an exact total. | PASS |
| N265 | SAP p. 70, final-analysis timing and <50% per-protocol criterion | Populations, phases, and adherence threshold are stated without a reported count conflict. | PASS |
| N266 | SAP p. 71, counts/percentages and literal "2 N Fisher's exact test" | The text is a test-label wording, not a reported numerical result. No inferred correction/candidate was made. | NOT APPLICABLE |
| N267 | SAP p. 72, rectangular data/`NA`/units/monthly monitoring | Columns/rows and missing/unit conventions are not conflicting values. | PASS |
| N268 | SAP p. 73, DSMC 5--7 people, annual, 1/3/2/3, 6 months after 72nd | Ranges and approximate information fractions are labelled as such; no total/denominator mismatch. | PASS |
| N269 | SAP p. 74, t=1/3 -> 15; t=2/3 -> 30; gamma -5.623626; alpha .001/.0075 | With `alpha=.05`, `a*(t)=.05(1-exp(-gamma*t))/(1-exp(-gamma))` gives .000997 at 1/3 and .00750 at 2/3; matches stated approximate values. | PASS |
| N270 | SAP p. 75, SAE report within 24 hours; total/serious event outputs | Hours is a reporting deadline, while total/serious are count categories; no rate/count mix-up. | PASS |
| N271 | SAP p. 76, four pooled AE subject proportions and `NA` convention | Four categories are subject proportions, not recurrent-event rates; `NA` means unavailable. | PASS |
| N272 | SAP p. 79, randomization seed at least eight digits | Administrative threshold; no result count or comparator. | NOT APPLICABLE |
| N273 | SAP p. 80, revisions and nine recruiting sites | Nine-site statement is a revision definition; no matched observed total is in this relationship. | NOT APPLICABLE |
| N274 | SAP p. 81, REDCap dates 18/17 January 2017 | Chronology is internally ordered: 17 January precedes 18 January. | PASS |
| N275 | Supplementary Results p. 8, nine center counts totaling 216 and whole percentages | `65+36+35+34+21+11+9+3+2=216`; all nine `count/216` values round to printed whole percentages and sum to 100% after rounding. | PASS |
| N276 | Supplementary Results p. 10, eTable 4, N=107/108, 20 AE cells | Every printed cell satisfies `count/N x100` to one decimal (e.g., 9/107=8.4%, 19/108=17.6%); event rows are nonexclusive, so row sums are not expected. | PASS |
| N277 | Supplementary Results p. 11, eTable 5, N=107/108, 20 AE cells | All 20 count/percentage cells reconcile to one decimal; 5/107=4.7% and 5/108=4.6% correctly differ by denominator. | PASS |
| N278 | Supplementary Results p. 12, eTable 6, N=107/108, 52 AE cells | All 52 cells reconcile to one decimal; displayed 0 (0.0) cells are coherent count/percentage pairs. | PASS |
| N279 | Supplementary Results p. 14, eTable 8, N=62/56, 48 AE cells | All 48 cells reconcile to one decimal. A label comparison is separately recorded as Candidate Draft 2 below. | PASS except Candidate Draft 2 |
| N280 | Supplementary Results pp. 15--16, eTable 9, N=29/20, 46 AE cells | All cells except Mycophenolate serious-systemic diarrhea reconcile to one decimal; that direct-source mismatch is Candidate Draft 1 below. | Candidate Draft 1 |
| N281 | Supplementary Results p. 15, eTable 9 serious diarrhea, MMF N=20, `1 (3.4)` | Direct recheck: `1/20 x100=5.0%`, not 3.4%; see Candidate Draft 1. | Candidate Draft 1 |
| N282 | Supplementary Results pp. 5 and 14, eTable 1 definition versus eTable 8 serious-ocular row | Direct recheck: serious ocular hypertension requires surgery, while `>24 mm Hg` is non-serious; see Candidate Draft 2. | Candidate Draft 2 |

## Candidate Draft 1 — eTable 9 MMF serious-diarrhea percentage

- **Category:** Denominator, proportion, or total inconsistency.
- **Exact supplied-source locations:** `joi190092supp1_prod.pdf#page=15`, eTable 9, Mycophenolate Mofetil column header `(N=20)`, column subtitle `Number of Patients Reporting at Least One Event (%)`, Serious Systemic row `Diarrhea`.
- **Printed inputs:** the direct PDF prints `1 (3.4)` in that cell. The same table prints `1 (5.0)` for the MMF low-hemoglobin cell, and its methotrexate N=29 column prints 1 (3.4) in several cells; these are internal rounding comparators, not substitute denominators.
- **Rule, calculation, and tolerance:** expected percent is `100 x 1 / 20 = 5.0%` to one decimal. Under the stated one-decimal tolerance (0.05 percentage points), a printed 3.4% corresponds to a denominator about 29.4 and cannot be a rounded 1/20 percentage. The difference is 1.6 percentage points.
- **Direct observation versus inference:** Direct observation is the N=20 header and printed `1 (3.4)`. The inference is that the displayed percentage does not reconcile if the common column denominator applies. It does not establish the underlying event count, an alternative risk set, or a correction.
- **Source-grounded alternatives:** an unprinted event-specific denominator near 29, an erroneous header, a transposed/copy-forward percentage from the N=29 column, or a typesetting error could explain the mismatch. The table supplies no alternative denominator or exception note.
- **Quality-control relevance:** A count/percentage mismatch can be extracted incorrectly as a risk/proportion in downstream evidence tables; the scope of that risk is limited to the reported table cell.
- **Exact human question:** Does the MMF serious-diarrhea cell use an unprinted denominator or denominator definition, or should the printed percentage for 1 event in the N=20 column be 5.0%?

## Candidate Draft 2 — eTable 8 serious-ocular hypertension label

- **Category:** Measure, label, or scale inconsistency.
- **Exact supplied-source locations:** `joi190092supp1_prod.pdf#page=5`, eTable 1, Ocular Hypertension row; and `joi190092supp1_prod.pdf#page=14`, eTable 8, Serious Ocular row `Ocular hypertension >24mm Hg` (methotrexate `1 (1.6)`, mycophenolate `0 (0.0)`).
- **Printed inputs:** eTable 1 defines non-serious ocular hypertension as `>= 24 mm Hg` and serious ocular hypertension as `Surgery required (laser or incisional)`. eTable 8 places `Ocular hypertension >24mm Hg` under `Serious Ocular`. Its footnote points to “eFigure 2,” not eTable 1; eTable 1 is a separate supplied comparator.
- **Rule and tolerance:** The eTable 8 severity label should meet the eTable 1 serious criterion when the footnote adopts that definition. A pressure threshold alone matches the non-serious criterion; the distinction is categorical, so no numeric rounding tolerance applies.
- **Direct observation versus inference:** Direct observations are the two printed definitions/labels and eTable 8 placement. The inference is that the serious-section row label lacks the surgery-required condition and therefore does not reconcile with the referenced criterion. This does not establish whether the event was surgery-required.
- **Source-grounded alternatives:** The eTable 8 row may abbreviate a surgery-required event, the eTable 1 definition may have been revised for the continuing-after-success cohort, or the row may carry the non-serious pressure label in error. No cohort-specific definition appears; p. 14 footnote a points to “eFigure 2,” whose content is not present in the supplied supplement text.
- **Quality-control relevance:** Severity labels define which events populate serious-AE counts/proportions. A label/definition mismatch can alter how a reader classifies the displayed event, without establishing any clinical or trial-conclusion consequence.
- **Exact human question:** Was the eTable 8 serious-ocular event surgery-required and incompletely labelled, did this cohort use a different seriousness definition, or was `Ocular hypertension >24mm Hg` placed under the wrong severity heading?

## Limitations

The SAP relationships are planning/design records, so the supplied SAP pages generally contain no observed numerical result from which to compute a new cross-document inconsistency.  Model-based power statements are marked approximate and were only checked for displayed input identity, arithmetic that the source itself makes reproducible, units, and measure labels; no unreported variance, sidedness, or implementation detail was assumed.  Supplementary Results eTables contain no workbook, raw data, person-time, CIs, estimates, or cell-specific alternate denominators beyond those printed.
