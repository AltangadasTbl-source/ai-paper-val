# Evidence Recheck — Stable Candidates C001-C013

Scope: mechanical recheck of every stable ID in `candidate_ledger.md` against the supplied direct-source PDF pages. Existing maps and extracted text were used only as locators. Values below were read from direct-source page renderings. Every candidate remains **Pending Human Adjudication**.

## C001 — Adjusted self-reported abstinence interval endpoint printed as 42

- **Location found:** DOC-001, `jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6`, Table 2, row “Continuous abstinence, self-reported only (ITT),” adjusted RR column.
- **Source text/value matched:** The rendered table prints adjusted RR `2.8 (1.9 to 42)` and ICC `0.19`.
- **Comparator matched:** The same row prints crude RR `2.7 (1.8 to 4.1)`; nearby adjusted intervals are `3.2 (2.2 to 5.2)`, `3.1 (2.1 to 5.2)`, `3.9 (2.4 to 6.9)`, `3.8 (2.3 to 7.7)`, and `2.7 (1.8 to 4.3)` or `2.7 (1.9 to 4.0)`.
- **Rule applicable:** An interval endpoint must be transcribed exactly and should be assessed for compatibility with its estimate, companion endpoint, and neighboring intervals; visual scale alone does not establish the intended value.
- **Calculation reproduced:** `42 / 2.8 = 15.0`; `1.9 / 2.8 = 0.6786`. The upper and lower multiplicative distances are markedly asymmetric, and ordinary rounding cannot transform `42` into `4.2`.
- **Necessary inputs/missing inputs:** The printed estimate and interval are available. The fitted coefficient, standard error, model output, and any profile-likelihood or transformation details needed to derive the endpoint are absent.
- **Source-grounded alternative:** The table footnote states that adjusted RR analyses used mixed-effects models accounting for clustering; a genuinely wide or asymmetric model interval remains possible from the supplied evidence.
- **Observation vs inference:** Direct observation: the table visibly prints `42`. Inference: a decimal-placement or transcription issue is plausible but is not established by the package.
- **Remaining human question:** Did the fitted adjusted model produce an upper endpoint of `42`, or was another endpoint intended?

## C002 — Discussion labels the all-cause death percentage as TB deaths

- **Location found:** DOC-001, `jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=8`, Discussion; DOC-001, `jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5`, Secondary Outcomes; DOC-001, `jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6`, Table 2; and DOC-003, `joi250093supp2_prod_1768590553.09463.pdf#page=6`, eTable 4.
- **Source text/value matched:** The Discussion says, “4.8% of the trial participants died of TB within 6 months.” Table 2 prints all-cause deaths `25/720 (3.5%)` and `27/360 (7.5%)`. eTable 4 prints total deaths `52` and “Death due to TB” `32 (61.5%)`.
- **Comparator matched:** The `4.8%` wording is compared with `52/1080` all-cause deaths and `32/1080` TB-cause deaths.
- **Rule applicable:** Cause-specific mortality and all-cause mortality require distinct numerators and labels over the same participant denominator.
- **Calculation reproduced:** `(25 + 27) / (720 + 360) × 100 = 52/1080 × 100 = 4.8148%`, which displays as `4.8%`; `32/1080 × 100 = 2.9630%`, which displays as `3.0%` to one decimal.
- **Necessary inputs/missing inputs:** Group denominators, all-cause death counts, total deaths, and TB-cause deaths are available. No separate supplied numerator/denominator produces `4.8%` TB-cause mortality.
- **Source-grounded alternative:** The phrase “died of TB” may have been used contextually for deaths occurring among participants receiving TB treatment, while eTable 4 is the package's explicit cause-of-death classification.
- **Observation vs inference:** Direct observation: the wording and all listed counts are printed. Inference: the Discussion may have attached a TB-cause label to the all-cause percentage.
- **Remaining human question:** Does `4.8%` refer to all-cause mortality, or is a separate TB-cause numerator or denominator intended?

## C003 — 178-message total conflicts with its printed frequency schedule

- **Location found:** DOC-002, `joi250093supp1_prod_1768590553.08963.pdf#page=16`, lines 381-390.
- **Source text/value matched:** The page states that each intervention participant will receive `178 SMS messages` over `6 months`, with `4 to 5 messages per day` in the first two months, `2 to 3 messages per day` in the next two months, and `1 to 2 messages per week` in the last two months.
- **Comparator matched:** The printed total `178` is compared with the minimum number of sends implied by the three printed frequency periods.
- **Rule applicable:** A stated total exposure must be at least the sum of the minimum stated period-specific frequencies when the periods cover the same six months.
- **Calculation reproduced:** Using an intentionally conservative `28` days per month and `8` weeks for the final two months gives `2×28×4 + 2×28×2 + 8×1 = 344`, already `166` above `178`. Using `30` days per month and `8` weeks gives `368`.
- **Necessary inputs/missing inputs:** The total, durations, and frequency ranges are available. Exact calendar dates, whether “per day” excludes any days, and whether the frequencies refer to sends, unique templates, or another unit are not supplied.
- **Source-grounded alternative:** The same page says the program would undergo refinement after the pilot; the total and schedule could describe different plan states, but the passage does not label them that way.
- **Observation vs inference:** Direct observation: `178` and the three frequency periods appear in one passage. Inference: at least one total, unit, duration, or plan-state label may differ from what was intended.
- **Remaining human question:** What total number of messages and period-specific sending schedule were intended for this plan state?

## C004 — Repeated 2,384-participant plan names 44 and 48 facilities

- **Location found:** DOC-002, `joi250093supp1_prod_1768590553.08963.pdf#page=10`, lines 203-219, and `joi250093supp1_prod_1768590553.08963.pdf#page=26`, lines 702-717.
- **Source text/value matched:** Page 10 states `2,384` smokers with TB, approximately `50` recruits from `44 health facilities`; page 26 repeats `2,384`, approximately `50` recruits, but states `48 health clinics`. Both passages also print 10% missing primary-outcome data, 16 pilot participants, and the same Phase-3 and Phase-4 assumptions.
- **Comparator matched:** `44 health facilities` is compared with `48 health clinics` for the matched `2,384`-participant plan.
- **Rule applicable:** Repeated statements of the same sample-size plan should use the same cluster count unless a definition, subset, or version distinction is stated.
- **Calculation reproduced:** `2384/44 = 54.1818`; `2384/48 = 49.6667`. The second quotient directly supports “approximately 50”; the four-cluster difference is not a rounding difference.
- **Necessary inputs/missing inputs:** The repeated plan parameters and both counts are available. No definition distinguishing “health facilities” from “health clinics,” and no passage-specific amendment or effective-date label, is supplied.
- **Source-grounded alternative:** The two nouns could denote different operational sets or one passage could preserve an earlier plan, but the source gives no such distinction.
- **Observation vs inference:** Direct observation: matched passages print `44` and `48`. Inference: they may be unreconciled plan versions or differently defined site sets.
- **Remaining human question:** Which site count governed the `2,384`-participant plan, and what distinction, if any, separates the two terms?

## C005 — 134-message total conflicts with its printed frequency schedule

- **Location found:** The cited DOC-002 PDF page 51 contains the trial-flow diagram and does not contain this dose statement. The dose statement is on DOC-002, `joi250093supp1_prod_1768590553.08963.pdf#page=53`, lines 1521-1531.
- **Source text/value matched:** Page 53 states that each intervention participant will receive `134 SMS messages` over `6 months`, with `4 to 5 messages per day` in the first two months, `1 to 2 messages per day` in the next two months, and `1 message per week` in the last two months.
- **Comparator matched:** The printed total `134` is compared with the minimum implied by the three period-specific frequencies on the same page.
- **Rule applicable:** The total number received must be at least the sum of minimum scheduled sends over the same six-month period.
- **Calculation reproduced:** With conservative `28`-day months and `8` final-period weeks, the minimum is `2×28×4 + 2×28×1 + 8×1 = 288`, which is `154` above `134`; using `30`-day months gives `308`.
- **Necessary inputs/missing inputs:** Total, periods, and frequency ranges are printed. Exact dates and the intended meaning of a “message” as a unique template versus a repeated send are absent.
- **Source-grounded alternative:** DOC-002 page 80 gives a different `134`-message schedule—`3 to 4/day` for one month, `1/day` for one month, then `1/month` for four months—which can accommodate `134`; page 53 does not say its schedule belongs to a different plan state.
- **Observation vs inference:** Direct observation: page 53 prints the total and frequencies; page 51 does not. Inference: the page-53 schedule may be carryover wording from another regimen.
- **Remaining human question:** Which schedule accompanies the `134`-message total, and should page 53 be explicitly assigned to a different plan state if that was intended?

## C006 — TAM sampling header conflicts with contemporaneous narrative and equations

- **Location found:** The cited DOC-002 PDF page 53 contains intervention-dose text, not the TAM table. The TAM evidence is on DOC-002, `joi250093supp1_prod_1768590553.08963.pdf#page=55`, lines 1574-1600.
- **Source text/value matched:** The table row reads `TAM questionnaire (30% of participants in the mTB-Tobacco groups)`. The same page says `20%` of total patients in mTB-Tobacco groups will complete TAM and prints Phase-3 calculations `10 × 40 × 20% = 80` and `8 × 40 × 20% = 64`; Phase-4 cells print `11 × 45 = 495` and `7 × 45 = 315` without subsampling.
- **Comparator matched:** Header `30%` is compared with the `20%` Phase-3 narrative/equations and the all-participant Phase-4 equations.
- **Rule applicable:** A sampling label must match the denominator and phase-specific fraction used in its accompanying narrative and arithmetic.
- **Calculation reproduced:** Phase 3: `10×40×0.20 = 80` and `8×40×0.20 = 64`, totaling `144`, which is 20% of `720`. Phase 4: `11×45 = 495` and `7×45 = 315`, totaling all `810` mTB-Tobacco participants. Neither calculation applies 30%.
- **Necessary inputs/missing inputs:** Site counts, cluster sizes, phase allocations, and Phase-3 fraction are printed. No denominator or pooled rule for the header's `30%` is supplied.
- **Source-grounded alternative:** The `30%` header could refer to an earlier or pooled target, but no such target is defined on the page; the supplied version-change text on page 77 instead describes 20% in Phase 3 and all participants in Phase 4.
- **Observation vs inference:** Direct observation: `30%`, `20%`, and the phase-specific equations coexist. Inference: the header may be a stale generic label.
- **Remaining human question:** What population and phase does `30%` describe, if any, relative to the printed 20%/all-participant plan?

## C007 — Later 2,716-participant plan gives 48 clinics versus a 63-site diagram

- **Location found:** The high-level `2,716`/`63` statement is on DOC-002, `joi250093supp1_prod_1768590553.08963.pdf#page=48`, lines 1343-1359, not cited page 46. Diagram 1 is on `joi250093supp1_prod_1768590553.08963.pdf#page=51` and `joi250093supp1_prod_1768590553.08963.pdf#page=52`, not cited pages 49-50. The comparator is on `joi250093supp1_prod_1768590553.08963.pdf#page=62`, lines 1859-1863.
- **Source text/value matched:** Page 48 states `2,716`, approximately `43` recruits from `63 health facilities`; pages 51-52 show Phase 3 `27` sites and Phase 4 `36` sites, totaling `63`, and `1,096 + 1,620 = 2,716` including the pilot. Page 62 states `2,716`, approximately `50` recruits from `48 health clinics`.
- **Comparator matched:** The repeated total `2,716` is paired with `63/~43` in the plan/diagram and `48/~50` in the statistics section.
- **Rule applicable:** Matched occurrences of one recruitment plan require compatible cluster counts and implied average cluster sizes unless the source defines a subset or different site concept.
- **Calculation reproduced:** `27 + 36 = 63`; `1096 + 1620 = 2716`; `2716/63 = 43.1111`; `2716/48 = 56.5833`. The first quotient matches `~43`; the counts differ by 15 sites.
- **Necessary inputs/missing inputs:** Total participants, phase/site totals, and both high-level counts are available. No definition of a 48-clinic subset or bridge between 48 and 63 is supplied.
- **Source-grounded alternative:** The 48 clinics could be an unstated operational subset or a retained earlier-plan count, but neither interpretation is labelled in the direct source.
- **Observation vs inference:** Direct observation: the matched total is printed with two site counts. Inference: one statement may be an unreconciled plan-state or subset reference.
- **Remaining human question:** What exact clinic set does `48` denote, and how does it relate to the `63` sites in the matching `2,716` plan?

## C008 — Phase-4 design-effect equality does not reproduce from printed inputs

- **Location found:** DOC-002, `joi250093supp1_prod_1768590553.08963.pdf#page=64`, lines 1923-1954.
- **Source text/value matched:** The page prints `N = 864 + (864 * 0.2) = 1036`, `Sample per cluster = 1036/36 = 29`, `DE = 1 + 0.02 (29-1) = 1.56`, and `ESS = effective sample size = 1036 * 1.56 = 1620 (45 subjects for each site)`; the diagram also prints 36 sites and 1,620 participants.
- **Comparator matched:** The stated product `1036 × 1.56 = 1620` is compared with literal multiplication and with the independent `36 × 45` recruitment total.
- **Rule applicable:** A displayed arithmetic equality should reproduce from its displayed operands; any ceiling or allocation rule should be stated separately from the literal product.
- **Calculation reproduced:** `864×1.2 = 1036.8`; `1036/36 = 28.7778`, displayed as 29; `1 + 0.02×(29−1) = 1.56`; `1036×1.56 = 1616.16`; `36×45 = 1620`.
- **Necessary inputs/missing inputs:** All displayed operands are present. The unrounded sample-size output and the sequence of integer, cluster-size, ceiling, or allocation rounding are not specified.
- **Source-grounded alternative:** `1,620` exactly represents a target of 45 participants at each of 36 sites, rather than the literal displayed `1036×1.56` product.
- **Observation vs inference:** Direct observation: the printed product and diagram total are `1,620`. Inference: site-level ceiling or allocation rounding may explain the four-person difference.
- **Remaining human question:** What explicit calculation and rounding sequence links the displayed operands to `1,620`?

## C009 — Phase-4 diagram is labelled Phase 3/Superiority

- **Location found:** DOC-002, `joi250093supp1_prod_1768590553.08963.pdf#page=64`, lines 1923-1954, Phase-4 section and diagram.
- **Source text/value matched:** The local heading reads `Phase 4`; the text specifies non-inferiority, A versus face-to-face B, `18 clusters in each`, and `36` total sites. The diagram box reads `Total clusters in Phase 3 (Superiority trial) = 36 sites` and `Patients to be recruited = 1620`.
- **Comparator matched:** The box's `Phase 3 (Superiority trial)` label is compared with the surrounding `Phase 4` non-inferiority section and its 36-site/1,620-person values.
- **Rule applicable:** A diagram's phase and inferential-objective labels must match the plan whose participant, cluster, and arm-allocation values it displays.
- **Calculation reproduced:** `18 + 18 = 36`; `36×45 = 1620`. On page 63 the Phase-3 diagram instead prints 27 sites and 1,080 participants.
- **Necessary inputs/missing inputs:** Phase headings, objectives, arm counts, site counts, and participant totals are available. No source definition assigns the 36-site/1,620 plan to Phase 3.
- **Source-grounded alternative:** None is supplied that makes 36 sites and 1,620 participants the local Phase-3 plan; a carried-over diagram label is a possible explanation only.
- **Observation vs inference:** Direct observation: the heading/context and diagram label differ categorically. Inference: the diagram label may have been carried over from the preceding phase's template.
- **Remaining human question:** What phase and inferential-objective label was intended for the 36-site/1,620-participant diagram?

## C010 — Phase-3 design-effect display gives unreproducible 1,080 effective sample size

- **Location found:** DOC-002, `joi250093supp1_prod_1768590553.08963.pdf#page=63`, lines 1884-1920. The repeated prose is on `joi250093supp1_prod_1768590553.08963.pdf#page=83`, lines 2623-2638, not cited page 82.
- **Source text/value matched:** Page 63 prints `N = 587 + (587 * 0.2) = 704`, `704/27 = 26`, `DE = 1 + 0.02 (26-1) = 1.50`, and `ESS = effective sample size = 704 * 1.50 ≈ 1080 (40 subjects for each site)`. Page 83 repeats 704, about 26 per cluster, ICC 0.02, design effect 1.50, and effective sample size around 1,080 or 40 per site.
- **Comparator matched:** The displayed `704×1.50≈1080` relationship is compared with literal multiplication and with the site-allocation total `27×40=1080`.
- **Rule applicable:** A displayed product should reproduce from its operands, and a cluster-rounded recruitment target should be distinguished from a quantity labelled “effective sample size.”
- **Calculation reproduced:** `587×1.2 = 704.4`; `704/27 = 26.0741`; `1 + 0.02×(26−1) = 1.50`; `704×1.50 = 1056`; `1080/704 = 1.5341`; `27×40 = 1080`.
- **Necessary inputs/missing inputs:** Displayed base sample, attrition, cluster count, ICC, design-effect formula, and final site target are available. The unrounded base calculation and the cluster-level ceiling/allocation convention are absent.
- **Source-grounded alternative:** A 1,056 inflated requirement could have been raised to 40 participants in each of 27 sites, producing 1,080; the source does not state that intermediate convention and instead prints the approximate product.
- **Observation vs inference:** Direct observation: both pages associate 704 and design effect 1.50 with about 1,080. Inference: cluster-level upward allocation may explain the difference and the terminology may be imprecise.
- **Remaining human question:** Was `1,080` a cluster-rounded recruitment target after obtaining `1,056`, and what quantity is intended by “effective sample size” here?

## C011 — MPSS score range conflicts with stated item scale

- **Location found:** The cited DOC-002 PDF page 84 contains primary/secondary outcome text and not the MPSS definition. The definition is on DOC-002, `joi250093supp1_prod_1768590553.08963.pdf#page=85`, lines 2703-2709.
- **Source text/value matched:** The page states that participants rate five domains on a `5-point scale`—depression, irritability, restlessness, hunger, and poor concentration—and that “These items” are summed for an overall score ranging from `5 to 35`.
- **Comparator matched:** Five listed domains on a five-point scale are compared with the stated summed range `5-35`.
- **Rule applicable:** A summed scale range must be compatible with its stated number of summed items, response-point count, and scoring anchors.
- **Calculation reproduced:** Under the ordinary 1-to-5 coding implied by a minimum total of 5, five items produce minimum `5×1 = 5` and maximum `5×5 = 25`, not 35. A maximum of 35 would require seven maximum points per item or additional/weighted items.
- **Necessary inputs/missing inputs:** Five named domains, five-point description, and stated total range are available. Item anchors, numeric coding, weights, subitems, and any transformation are absent.
- **Source-grounded alternative:** The source could be omitting additional items or a weighting/transformation rule, but it supplies no such rule and refers to the five listed domains as “These items.”
- **Observation vs inference:** Direct observation: the page prints five domains, five-point scale, and range 5-35. Inference: an item-count, response-scale, or total-range definition may be omitted or mismatched.
- **Remaining human question:** What complete MPSS item coding or transformation yields the stated `5-35` range?

## C012 — Site 2008 death count and percentage lack a compatible supplied denominator

- **Location found:** DOC-003, `joi250093supp2_prod_1768590553.09463.pdf#page=8`, eTable 5, site 2008 row; and `joi250093supp2_prod_1768590553.09463.pdf#page=9`, eTable 6, site 2008 row.
- **Source text/value matched:** eTable 5 prints site 2008 recruitment `40/484 (8.2%)`, self-reported quitters `15/35 (42.9%)`, verified quitters `12/35 (34.3%)`, and ITT quitters `12/40 (30%)`. eTable 6 prints deaths `5 (7.5)` for site 2008 but provides no denominator column.
- **Comparator matched:** The death count/percentage pair `5 (7.5%)` is compared with the matched site's supplied randomized/ITT participant count of 40.
- **Rule applicable:** A count and percentage require a denominator that reproduces the displayed percentage after stated rounding; a denominator from another table is conditional unless explicitly linked.
- **Calculation reproduced:** With denominator 40, `5/40×100 = 12.5%`, not 7.5%. Conversely, `5/0.075 = 66.6667`; an integer denominator of 67 would give `7.46%`, but no 67-person site population is supplied.
- **Necessary inputs/missing inputs:** Site ID, death count, displayed percent, recruitment/ITT denominator, and complete-case abstinence denominator are available. eTable 6's intended death denominator and any separate at-risk population are absent.
- **Source-grounded alternative:** eTable 6 may use a distinct unprinted site-specific denominator; however, no such denominator is present in the supplied tables.
- **Observation vs inference:** Direct observation: eTable 6 prints `5 (7.5)` and omits a denominator. Inference: using 40 is a cross-table denominator match and remains conditional.
- **Remaining human question:** What denominator generated `7.5%` for five deaths at site 2008?

## C013 — Protocol message dose changes from 178 to 134 without supplied reconciliation

- **Location found:** DOC-002, `joi250093supp1_prod_1768590553.08963.pdf#page=16`, lines 381-390 (`178` regimen); DOC-002, `joi250093supp1_prod_1768590553.08963.pdf#page=53`, lines 1521-1531 (`134` with a two/two/two-month schedule; not cited page 51); DOC-002, `joi250093supp1_prod_1768590553.08963.pdf#page=80`, lines 2526-2536 (`134` with a one/one/four-month schedule); DOC-002, `joi250093supp1_prod_1768590553.08963.pdf#page=101` through `joi250093supp1_prod_1768590553.08963.pdf#page=109`, SMS log numbered 1-134; and DOC-001, `jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3`, intervention description. DOC-001 page 1 describes delivery timing but does not print the total `134`.
- **Source text/value matched:** Page 16 prints `178 SMS messages` over six months. Pages 53 and 80 print `134 SMS messages` over six months but with different within-period schedules. The SMS log begins at message 1 on page 101 and ends at message 134 on page 109. DOC-001 page 3 prints `134 unique text messages`: 100 in month 1, 30 in month 2, and 4 monthly messages over months 3-6.
- **Comparator matched:** The matched mTB-Tobacco participant dose total `178` is compared with the repeated `134` total and the complete 1-134 message log.
- **Rule applicable:** Intervention dose comparisons require a plan/version identity; a changed total should be explicitly tied to a superseding regimen or distinctly labelled population.
- **Calculation reproduced:** `178−134 = 44`. The article's component count reconciles: `100 + 30 + 4 = 134`. The log's first and last identifiers establish a consecutively labelled 1-134 set, subject to the visible page sequence.
- **Necessary inputs/missing inputs:** Both totals, their schedules, the article components, and the 1-134 log are available. A dated amendment or explicit crosswalk stating that the 178-message text was superseded by the 134-message regimen is absent; page 77's v4-to-v6 change list does not mention message dose.
- **Source-grounded alternative:** Both protocol passages describe a post-pilot refinement process, so an intervention revision is plausible; the package does not explicitly connect that process to the 178-to-134 change.
- **Observation vs inference:** Direct observation: the package prints both totals and later provides a 1-134 log. Inference: `178` may represent an obsolete or earlier regimen rather than the delivered trial intervention.
- **Remaining human question:** Was the `178`-message regimen formally superseded by the `134`-message regimen, and what version/effective-date label should distinguish them?

## Recheck summary

- Stable IDs covered: 13 (`C001`-`C013`).
- Source-value/comparator checks completed: 13.
- Stable-ID status: all remain **Pending Human Adjudication**.
- Locator discrepancies observed mechanically: five IDs (`C005`, `C006`, `C007`, `C010`, `C011`); exact direct-source pages are recorded above.
- Remaining limitations: model output is absent for C001; schedule-unit/version definitions are absent for C003, C005, and C013; site/plan definitions are absent for C004 and C007; calculation-rounding conventions are absent for C008 and C010; full MPSS scoring rules are absent for C011; and the eTable 6 death denominator is absent for C012.
