# Mechanical Evidence Recheck

This artifact mechanically rechecks every stable candidate ID in the supplied direct-source PDFs.
Fresh native layout extraction and, where needed, direct page rendering were used only to inspect the
cited PDF pages. Reusable artifacts served as locators, not evidentiary authority. These records do
not assign validity, severity, acceptance, rejection, exclusion, correction, or any other disposition.

## C001 — Balloon-angioplasty female percentage does not reconcile with count and denominator

- **Location found:** Yes — [DOC-001 Table 1, PDF p. 6](<../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=6>).
- **Source value/text matched:** The balloon-angioplasty column is headed `n = 249`; its sex rows print `Male 172 (69.1)` and `Female 77 (30.1)`.
- **Comparator matched:** The displayed arm denominator is 249, the two displayed sex counts are 172 and 77, and the male row provides a same-column percentage comparator.
- **Consistency rule applicable:** Yes. For a count-and-percentage row without a separate row denominator, the displayed percentage can be compared with count divided by the displayed column denominator under ordinary nearest-one-decimal rounding.
- **Calculation or logical comparison reproduced:** `172 + 77 = 249`; `77 / 249 x 100 = 30.923695%`, which rounds to `30.9%`, while `172 / 249 x 100 = 69.076305%`, which rounds to the printed `69.1%`. The printed sex percentages sum to `69.1% + 30.1% = 99.2%`.
- **Necessary inputs available:** The two counts, arm denominator, and printed percentages are available. No row-specific denominator or alternative percentage rule is printed.
- **Source-grounded alternative interpretation:** The coherent male calculation and the fact that the sex counts sum to 249 support the possibility that only the female percentage was transcribed incorrectly; a hidden female-row denominator or an error in another displayed input also remains possible because the source does not identify the production data.
- **Direct observation versus inferred explanation:** Direct observations are the printed values and reproduced arithmetic. Any transcription error, hidden denominator, or choice of which field should change is inferred.
- **Exact remaining human question:** Which intended source value governs the female row: count 77, arm denominator 249, or percentage 30.1%, and was any undisclosed row-specific denominator used?

## C002 — Balloon-angioplasty ischemic-stroke percentage is outside ordinary one-decimal rounding

- **Location found:** Yes — [DOC-001 Table 1, PDF p. 6](<../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=6>) and [DOC-002 Table S1, PDF p. 14](<../../../joi240088supp1_prod_1746815064.21247.pdf#page=14>).
- **Source value/text matched:** Both tables print balloon-angioplasty `n = 249` and ischemic stroke `215 (86.4)`.
- **Comparator matched:** DOC-001 prints the complementary qualifying-event row `Transient ischemic attack 34 (13.7)`, and `215 + 34 = 249`.
- **Consistency rule applicable:** Yes, under ordinary nearest-one-decimal rounding of count divided by the displayed denominator. The source does not state a different convention.
- **Calculation or logical comparison reproduced:** `215 / 249 x 100 = 86.345382%`, which ordinarily rounds to `86.3%`, not `86.4%`; `34 / 249 x 100 = 13.654618%`, which rounds to the printed `13.7%`. The same `215 (86.4)` is repeated in the supplement.
- **Necessary inputs available:** Counts, denominator, complementary category, and repeated printed percentage are available. The exact rounding convention and any hidden analysis denominator are not supplied.
- **Source-grounded alternative interpretation:** The repeated value could reflect a shared upstream tabulation convention or copied value rather than two independent calculations; an unprinted weighted or non-integer denominator could also generate a different percentage, but neither table identifies one.
- **Direct observation versus inferred explanation:** Repetition and arithmetic are direct. A nonstandard convention, weighting, or shared transcription mechanism is inferred.
- **Exact remaining human question:** What denominator and rounding convention generated 86.4%, and should the count, denominator, or repeated percentage be treated as the intended value?

## C003 — Table S4 procedure rows use 241 while the column header states 249

- **Location found:** Yes — [DOC-002 Table S4, PDF p. 17](<../../../joi240088supp1_prod_1746815064.21247.pdf#page=17>).
- **Source value/text matched:** The column is headed `Balloon angioplasty group (n=249)` with superscript `a`; footnote `a` states that 241 of 249 patients underwent balloon angioplasty and explains the eight who did not.
- **Comparator matched:** Procedure rows include balloon-angioplasty times `182 (75.5)`, `48 (19.9)`, and `11 (4.6)`; residual-stenosis rows `214 (88.8)`, `19 (7.9)`, and `8 (3.3)`; and intraprocedural complications `42 (17.4)`.
- **Consistency rule applicable:** Conditionally. A column header ordinarily supplies the denominator, but a linked footnote may supersede it for procedure-applicable rows. The mechanical question is whether the footnote clearly governs those rows.
- **Calculation or logical comparison reproduced:** `182 + 48 + 11 = 241`; `214 + 19 + 8 = 241`; and the eTICI category counts sum to 241. Also, `182/241 = 75.518672%` to `75.5%`, `214/241 = 88.796680%` to `88.8%`, and `42/241 = 17.427386%` to `17.4%`. These percentages do not use 249.
- **Necessary inputs available:** The arm size, underwent-procedure count, exclusions, row counts, and percentages are available. The table does not explicitly state, row by row, whether every procedure and complication percentage uses 241; the restenosis rows separately identify 153 imaged patients.
- **Source-grounded alternative interpretation:** The header can be read as overall randomized-arm context and superscript `a` as the applicable denominator definition for procedure rows; under that reading, the 241-based percentages are explained by the printed footnote even though the header remains 249.
- **Direct observation versus inferred explanation:** The header, footnote, sums, and percentages are direct. Whether the footnote provides sufficient denominator labeling for every applicable row is interpretive.
- **Exact remaining human question:** Is superscript `a` intended to define 241 as the denominator for all procedure-applicable count-and-percentage rows, and is the current header-plus-footnote presentation the intended denominator labeling?

## C004 — Table S6 BA `9 (3.9)` conflicts with its displayed denominator 249

- **Location found:** Yes — [DOC-002 Table S6, PDF p. 19](<../../../joi240088supp1_prod_1746815064.21247.pdf#page=19>).
- **Source value/text matched:** Table S6 is headed balloon angioplasty `n=249` and prints the primary outcome as `9 (3.9)`.
- **Comparator matched:** The displayed denominator is 249. A separate supplied population size of 233 is printed for the per-protocol balloon-angioplasty population in [DOC-001 Figure 1, PDF p. 5](<../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5>) and [DOC-002 Table S10, PDF p. 23](<../../../joi240088supp1_prod_1746815064.21247.pdf#page=23>), but Table S6 does not label itself per-protocol.
- **Consistency rule applicable:** Yes. A count-and-percentage entry can be checked against its displayed column denominator absent a printed alternative denominator.
- **Calculation or logical comparison reproduced:** `9/249 x 100 = 3.614458%`, which rounds to `3.6%`; `9/233 x 100 = 3.862661%`, which rounds to the printed `3.9%`.
- **Necessary inputs available:** The internal count, percentage, and header denominator are available. The denominator actually used to calculate 3.9% and the analysis population for the count are not stated in Table S6.
- **Source-grounded alternative interpretation:** The percentage may have been calculated with the supplied per-protocol denominator 233 even though the table displays 249, or a different unlabelled analysis set may have been used. Table S6's footnote describes adjustment for groups and centers but does not define a changed population denominator.
- **Direct observation versus inferred explanation:** The `9 (3.9)`, header 249, and calculations are direct. Use of 233 or another hidden population is inferred.
- **Exact remaining human question:** Which analysis-set denominator produced 3.9%, and do Table S6's count, percentage, endpoint, and `n=249` header all refer to the same population?

## C005 — Table S7 group headers conflict with site totals and displayed site percentages

- **Location found:** Yes — [DOC-002 Table S7, PDF p. 20](<../../../joi240088supp1_prod_1746815064.21247.pdf#page=20>), [DOC-001 Figure 1, PDF p. 5](<../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5>), and [DOC-002 Table S10, PDF p. 23](<../../../joi240088supp1_prod_1746815064.21247.pdf#page=23>).
- **Source value/text matched:** Table S7 heads the BA and AMM columns `N=233` and `N=238`, gives site totals 256 and 245, and prints Beijing `4 (2.9)` and `19 (16.1)` plus other centers `7 (6.3)` and `15 (11.2)`.
- **Comparator matched:** The site totals sum to 501. Figure 1 and Table S10 print primary/intention-to-treat group sizes 249 and 252, also totaling 501; their per-protocol sizes are 233 and 238, totaling 471.
- **Consistency rule applicable:** Yes. The table's site totals, column population labels, and within-site percentages must identify one coherent population or disclose distinct denominators.
- **Calculation or logical comparison reproduced:** Header total `233+238=471`, whereas site total `256+245=501`. Using headers directly gives `4/233=1.7%`, `19/238=8.0%`, `7/233=3.0%`, and `15/238=6.3%`, not three of the four printed percentages. Integer site-by-arm denominators consistent with the printed percentages and site totals are 138/118 for Beijing and 111/134 for other centers: `4/138=2.9%`, `19/118=16.1%`, `7/111=6.3%`, and `15/134=11.2%`; these inferred column sums are `138+111=249` and `118+134=252`.
- **Necessary inputs available:** All displayed headers, site totals, cell counts, cell percentages, and the supplied 249/252 and 233/238 population totals are available. Exact site-by-arm denominators and Table S7's analysis-population label are not printed.
- **Source-grounded alternative interpretation:** The percentages and site totals can be read as intention-to-treat site strata using 249/252 overall, while the 233/238 headers may be contextual per-protocol totals or copied labels. That reading reconciles the cells but is not stated by Table S7.
- **Direct observation versus inferred explanation:** The headers, totals, and percentages are direct. The four site-by-arm denominators are arithmetically inferred from the rounded percentages and row/column totals; a copy-forward mechanism is inferred.
- **Exact remaining human question:** Which population does Table S7 analyze, what are the exact site-by-arm denominators, and why do its headers show 233/238 when its totals and percentages align with 249/252?

## C006 — Table S8 per-protocol percentages conflict with headers 249/252

- **Location found:** Yes — [DOC-002 Table S8, PDF p. 21](<../../../joi240088supp1_prod_1746815064.21247.pdf#page=21>), [DOC-001 Figure 1, PDF p. 5](<../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5>), and [DOC-002 Table S10, PDF p. 23](<../../../joi240088supp1_prod_1746815064.21247.pdf#page=23>).
- **Source value/text matched:** Table S8 is titled as the per-protocol population but heads its columns `n=249` and `n=252`; it prints primary `9 (3.9)` and `33 (13.9)` and component rows `6 (2.6)/4 (1.7)`, `1 (0.4)/18 (7.6)`, and `3 (1.3)/20 (8.4)`.
- **Comparator matched:** Figure 1 and Table S10 identify per-protocol denominators as BA 233 and AMM 238; 249/252 are the primary/intention-to-treat denominators.
- **Consistency rule applicable:** Yes. A table explicitly titled per-protocol should use or disclose denominators consistent with that population, and its count percentages can be checked against the supplied PPS sizes.
- **Calculation or logical comparison reproduced:** With 233/238, the displayed rows reproduce as `9/233=3.9%`, `33/238=13.9%`, `6/233=2.6%`, `4/238=1.7%`, `1/233=0.4%`, `18/238=7.6%`, `3/233=1.3%`, and `20/238=8.4%`, after one-decimal rounding. The printed 249/252 headers do not generate the primary percentages.
- **Necessary inputs available:** The table title, headers, counts, percentages, and externally supplied PPS denominators are available. No Table S8 footnote redefines the headers or identifies an outcome-specific PPS.
- **Source-grounded alternative interpretation:** The 249/252 headers may show randomized-arm context while all percentages use actual PPS denominators 233/238; alternatively the headers may be copy-forward labels from the primary table. The source does not select between those readings.
- **Direct observation versus inferred explanation:** Title, headers, external PPS sizes, and arithmetic are direct. Copy-forward or contextual-header explanations are inferred.
- **Exact remaining human question:** Are 233/238 the intended denominators for every Table S8 row, and are the displayed 249/252 headers contextual labels or unintended values?

## C007 — Table S9 as-treated percentages conflict with headers 249/252

- **Location found:** Yes — [DOC-002 Table S9, PDF p. 22](<../../../joi240088supp1_prod_1746815064.21247.pdf#page=22>) and [DOC-002 Table S10, PDF p. 23](<../../../joi240088supp1_prod_1746815064.21247.pdf#page=23>).
- **Source value/text matched:** Table S9 is titled as-treated but heads its columns `n=249` and `n=252`; its primary row is `11 (4.5)` and `34 (13.4)`, followed by `8 (3.3)/4 (1.6)`, `1 (0.4)/19 (7.5)`, and `3 (1.2)/21 (8.3)`.
- **Comparator matched:** Table S10 supplies as-treated denominators BA 247 and AMM 254; its intention-to-treat denominators are 249 and 252.
- **Consistency rule applicable:** Yes. The as-treated label, displayed headers, supplied ATS denominators, counts, and percentages should refer to a coherent population or disclose distinct risk sets.
- **Calculation or logical comparison reproduced:** Using 247/254 gives `11/247=4.5%`, `34/254=13.4%`, `4/254=1.6%`, `1/247=0.4%`, `19/254=7.5%`, `3/247=1.2%`, and `21/254=8.3%` after one-decimal rounding. Thus most rows align with 247/254 rather than 249/252. The separate `8 (3.3)` arithmetic is recorded under C014.
- **Necessary inputs available:** Table title, headers, counts, percentages, and supplied ATS denominators are available. Table S9 provides no footnote defining the population denominators or outcome-specific risk sets.
- **Source-grounded alternative interpretation:** The headers may show original randomized group sizes while ATS percentages use the reassigned 247/254 populations, or the headers may be copied from the primary table. Either reading requires a population-label explanation absent from Table S9.
- **Direct observation versus inferred explanation:** The labels, values, and calculations are direct. Header provenance and any copy-forward mechanism are inferred.
- **Exact remaining human question:** Are 247/254 the intended Table S9 denominators, and if so, what is the intended meaning of the printed 249/252 headers?

## C008 — Baseline stenosis categories include four values outside the stated 70%-99% eligibility range

- **Location found:** Yes — [DOC-001 eligibility text, PDF p. 2](<../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=2>), [DOC-001 Figure 1, PDF p. 5](<../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5>), and [DOC-001 Table 1, PDF p. 6](<../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=6>).
- **Source value/text matched:** Eligibility requires severe atherosclerotic stenosis `70%-99% according to the Warfarin Aspirin Symptomatic Intracranial Disease method`. Table 1 prints symptomatic-artery stenosis `60%-69%`: BA 0 and AMM 2; and `100%`: BA 1 and AMM 1.
- **Comparator matched:** Figure 1 shows 73 screened patients excluded for angiography with stenosis below 70%, then primary-analysis groups of 249 and 252. Table 1's four out-of-range participants are within those displayed primary groups.
- **Consistency rule applicable:** Yes, if the eligibility and baseline table use the same stenosis measurement, time point, method, and qualifying-artery definition. The source does not explicitly establish all four identity conditions.
- **Calculation or logical comparison reproduced:** Two AMM participants are below 70%, and one participant in each arm is at 100%; `2+1+1=4` displayed participants lie outside the inclusive 70%-99% interval.
- **Necessary inputs available:** Eligibility bounds, table categories/counts, arm sizes, and screening-flow statement are available. Missing definitions are the Table 1 measurement time, assessor/core-lab status, whether the eligibility value came from a different angiogram or reader, and whether retained deviations were allowed.
- **Source-grounded alternative interpretation:** Screening/site measurements may have satisfied 70%-99% while later baseline or core-laboratory reassessment moved four values outside the range; retained protocol deviations are another possibility. The article does not tie Table 1's values to the exact eligibility assessment.
- **Direct observation versus inferred explanation:** Thresholds and four table counts are direct. Measurement drift, reader differences, or protocol deviations are inferred.
- **Exact remaining human question:** Were the four Table 1 values measured at a different time or by a different reader from the eligibility assessment, or were they retained eligibility deviations, and how should that distinction be labeled?

## C009 — Thirty-day follow-up tolerance is +/-3 days in the supplement but +/-7 days elsewhere

- **Location found:** Yes — [DOC-002 study-design graphic, PDF p. 6](<../../../joi240088supp1_prod_1746815064.21247.pdf#page=6>), [DOC-001 follow-up schedule, PDF p. 3](<../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=3>), and [DOC-003 protocol schedule, PDF p. 15](<../../../joi240088supp2_prod_1746815064.36071.pdf#page=15>).
- **Source value/text matched:** The DOC-002 graphic labels clinical follow-up `30+/-3d`; DOC-001 states participants were followed at `30 +/- 7 days`; DOC-003 Visit 4 is `30d +/- 7d`.
- **Comparator matched:** All three locations describe the matched 30-day post-enrollment clinical visit/schedule; the 90-day, 6-month, and 1-year tolerances otherwise align between the graphic and schedules.
- **Consistency rule applicable:** Yes. A matched visit window should have the same tolerance unless the source labels distinct operational and protocol windows.
- **Calculation or logical comparison reproduced:** `30 +/- 3` spans days 27-33, a six-day endpoint-to-endpoint width; `30 +/- 7` spans days 23-37, a 14-day width. The tolerances differ by four days on each side.
- **Necessary inputs available:** Visit target, tolerances, and schedule context are available. No source note defines `+/-3` as a separate visit, analytic window, or operational subset.
- **Source-grounded alternative interpretation:** The study-design graphic could depict a tighter intended clinical-contact window while the article/protocol allow a wider assessment window, but the graphic calls it clinical follow-up and does not state such a distinction.
- **Direct observation versus inferred explanation:** The three labels and window arithmetic are direct. A distinct operational convention or graphic transcription error is inferred.
- **Exact remaining human question:** Was the 30-day clinical follow-up intended to use +/-3 or +/-7 days, or do the two tolerances describe distinct, undocumented windows?

## C010 — Protocol V2.0 gives 21-day and 14-day lower bounds for the same stroke criterion

- **Location found:** Yes — [DOC-003 synopsis, PDF p. 7](<../../../joi240088supp2_prod_1746815064.36071.pdf#page=7>) and [DOC-003 body eligibility, PDF p. 21](<../../../joi240088supp2_prod_1746815064.36071.pdf#page=21>). [DOC-003 PDF p. 3](<../../../joi240088supp2_prod_1746815064.36071.pdf#page=3>) identifies this section as Protocol Version 2.0 dated June 25, 2018.
- **Source value/text matched:** The synopsis says eligible patients had ischemic stroke `21 to 90 days` before enrollment; body inclusion criterion 2 says ischemic stroke `[14-90 days]` before enrollment. Both pair the interval with TIA under 90 days and 70%-99% stenosis.
- **Comparator matched:** The two statements occur in the synopsis and detailed inclusion criteria of the same original protocol version and describe patient eligibility.
- **Consistency rule applicable:** Yes. The lower bound for the same eligibility interval should agree within one protocol version unless the synopsis and body explicitly define different populations or stages.
- **Calculation or logical comparison reproduced:** Lower bounds 21 and 14 differ by seven days; the corresponding intervals are 21-90 days and 14-90 days.
- **Necessary inputs available:** Protocol identity, version/date, criterion wording, and both bounds are available. No hierarchy clause, amendment note within V2.0, or distinction between screening and enrollment criteria is supplied at these locations.
- **Source-grounded alternative interpretation:** The detailed body may govern over a stale synopsis, or one interval may reflect an unmarked amendment incorporated inconsistently. Both are production explanations; the source does not state which text controlled enrollment.
- **Direct observation versus inferred explanation:** Same-version wording and the seven-day difference are direct. Stale-summary or amendment explanations are inferred.
- **Exact remaining human question:** Which V2.0 lower bound governed enrollment, 14 or 21 days, and is either occurrence an unmarked synopsis/body amendment artifact?

## C011 — BA 3-month aspirin percentage does not reconcile with count and displayed arm denominator

- **Location found:** Yes — [DOC-002 Table S3, PDF p. 16](<../../../joi240088supp1_prod_1746815064.21247.pdf#page=16>).
- **Source value/text matched:** The BA group header is `n=249`; the 3-month aspirin cell is `234 (93.9)`.
- **Comparator matched:** The displayed arm denominator 249 is the only printed BA denominator for the baseline, 3-month, and 1-year columns; no evaluated-at-3-month denominator is shown.
- **Consistency rule applicable:** Yes, under ordinary nearest-one-decimal rounding, absent a printed row/time-specific denominator or a stated truncation rule.
- **Calculation or logical comparison reproduced:** `234/249 x 100 = 93.975904%`, which rounds to `94.0%`, not `93.9%`. Truncating rather than rounding at one decimal would display 93.9%.
- **Necessary inputs available:** Count, header denominator, time point, and printed percentage are available. Missing inputs are the actual 3-month evaluated denominator, handling of missing follow-up, and percentage display rule.
- **Source-grounded alternative interpretation:** The table may use truncation rather than nearest rounding, or an undisclosed time-specific denominator or weighting scheme. Neither is identified in Table S3.
- **Direct observation versus inferred explanation:** The printed cell and arithmetic are direct. Truncation, hidden denominator, or weighting is inferred.
- **Exact remaining human question:** What 3-month denominator and display rule generated 93.9%, and are all BA aspirin cells intended to use the header denominator 249?

## C012 — Figure S1 repeats “2nd meeting” for three chronologically distinct meetings

- **Location found:** Yes — [DOC-002 Figure S1, PDF p. 10](<../../../joi240088supp1_prod_1746815064.21247.pdf#page=10>); the labels were confirmed from the rendered direct PDF page.
- **Source value/text matched:** The four branches print `1st meeting 2021/05/30`, `2nd meeting 2021/11/20`, `2nd meeting 2022/09/07`, and `2nd meeting 2023/04/10`.
- **Comparator matched:** The dates are chronologically distinct and all four boxes descend from the same statement about confirming endpoint events at each review meeting.
- **Consistency rule applicable:** Yes, if `1st` and `2nd` are ordinal identifiers in one meeting sequence. A repeated phase/cycle label would require a different stated rule.
- **Calculation or logical comparison reproduced:** There are four dated meeting boxes but only two unique ordinal labels; `2nd meeting` is printed three times for dates spanning November 2021 through April 2023.
- **Necessary inputs available:** Ordinal labels, dates, and common process context are available. The intended meaning of the ordinal, any review-cycle reset, and intended third/fourth identifiers are not defined.
- **Source-grounded alternative interpretation:** Because all boxes are CEC review streams from one common node, `2nd meeting` could denote multiple sessions within a second review cycle rather than chronological meeting number; the figure provides no cycle label or legend supporting that convention.
- **Direct observation versus inferred explanation:** Repeated labels and dates are direct. Sequential third/fourth labels or a hidden cycle convention are inferred.
- **Exact remaining human question:** Are the 2022 and 2023 boxes intended to be third and fourth meetings, or does `2nd meeting` name a repeated review cycle that should be explicitly defined?

## C013 — Recurring visit list duplicates visit numbers 9 and 11

- **Location found:** Yes — the cited text is present at [DOC-003 PDF p. 35](<../../../joi240088supp2_prod_1746815064.36071.pdf#page=35>). That page belongs to original Protocol V2.0, not the final-protocol section. The identical sentence is also present in final Protocol V2.3 at [DOC-003 PDF p. 96](<../../../joi240088supp2_prod_1746815064.36071.pdf#page=96>).
- **Source value/text matched:** Both pages print: `Follow-up every 6 months (visit 8, visit 9, visit 10, visit 11, visit 9, and visit 11 require patients to undergo face-to-face follow-up).`
- **Comparator matched:** The original protocol schedule at [DOC-003 PDF p. 15](<../../../joi240088supp2_prod_1746815064.36071.pdf#page=15>) labels follow-up from one to three years as `Visit 8,9,10,11` at six-month intervals.
- **Consistency rule applicable:** Yes. Ordered visit identifiers should be distinct when they denote successive visits; repeated identifiers can be coherent only if the sentence is instead enumerating a subset or visit type and states that syntax clearly.
- **Calculation or logical comparison reproduced:** Six visit tokens are printed: 8, 9, 10, 11, 9, 11. There are four unique identifiers; 9 and 11 each occur twice. The schedule comparator contains only visits 8 through 11.
- **Necessary inputs available:** Exact sentence, recurrence interval, schedule identifiers, and protocol-section identities are available. Missing information is whether the last `visit 9, and visit 11` is meant as a face-to-face subset of visits 8-11 or whether six successive visits were intended.
- **Source-grounded alternative interpretation:** The sentence may intend to enumerate visits 8-11 and then specify visits 9 and 11 as the face-to-face subset, with missing punctuation or linking words; alternatively a six-visit sequence may have intended different fifth and sixth identifiers. The four-visit schedule supports the subset reading but does not resolve the grammar.
- **Direct observation versus inferred explanation:** The duplicate list, schedule, and the fact that p. 35 is V2.0 while p. 96 is V2.3 are direct. Any intended subset, punctuation issue, or replacement identifiers are inferred.
- **Exact remaining human question:** Does the sentence mean that visits 9 and 11 are the face-to-face subset within visits 8-11, or was a six-visit sequence intended; and should the candidate's source descriptor refer to p. 96 when calling the text final-protocol material?

## C014 — Table S9 BA `8 (3.3)` does not round from either supplied ATS or displayed denominator

- **Location found:** Yes — [DOC-002 Table S9, PDF p. 22](<../../../joi240088supp1_prod_1746815064.21247.pdf#page=22>) and [DOC-002 Table S10, PDF p. 23](<../../../joi240088supp1_prod_1746815064.21247.pdf#page=23>).
- **Source value/text matched:** Table S9 prints BA `8 (3.3)` for any stroke or all-cause death within 30 days and displays BA header `n=249`.
- **Comparator matched:** Table S10 supplies BA as-treated `N=247`; the Table S9 displayed denominator is 249. No separate 30-day risk-set denominator is printed.
- **Consistency rule applicable:** Yes, under ordinary nearest-one-decimal rounding against either supplied plausible denominator.
- **Calculation or logical comparison reproduced:** `8/247 x 100 = 3.238866%` and `8/249 x 100 = 3.212851%`; both round to `3.2%`, not `3.3%`.
- **Necessary inputs available:** Count, printed percentage, Table S9 header, and supplied ATS denominator are available. The outcome-specific denominator and any nonstandard percentage rule are absent.
- **Source-grounded alternative interpretation:** A smaller undisclosed 30-day risk set could yield 3.3%, or the percentage could follow a nonstandard upward display rule. Table S9 does not identify either condition.
- **Direct observation versus inferred explanation:** The values and both calculations are direct. A hidden risk set, nonstandard rule, or transcription mechanism is inferred.
- **Exact remaining human question:** What denominator and percentage rule generated `8 (3.3)`, and does this cell use the same 247-person ATS population as the other BA rows?

## C015 — Narrative assigns all 11 pre-analysis exclusions to consent withdrawal while Figure 1 assigns only 10

- **Location found:** Yes — [DOC-001 patient-population narrative, PDF p. 4](<../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=4>) and [DOC-001 Figure 1, PDF p. 5](<../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5>).
- **Source value/text matched:** The narrative states, `Eleven patients were excluded due to consent withdrawal`, producing 501 primary-analysis patients from 512 randomized.
- **Comparator matched:** Figure 1 prints seven BA consent withdrawals, three AMM consent withdrawals, and one AMM participant `Not successfully recruited but assigned a randomization number in error`, followed by primary-analysis groups 249 and 252.
- **Consistency rule applicable:** Yes. Matched exclusions from the same 512 randomized to the same 501 analyzed should have coherent reason-category counts across narrative and flowchart.
- **Calculation or logical comparison reproduced:** Figure consent withdrawals total `7+3=10`; including the separate erroneous-randomization category gives `7+3+1=11`. Both locations reconcile numerically to 501 analyzed, but they do not assign the same reason to all 11.
- **Necessary inputs available:** Randomized total, analyzed totals, arm-specific exclusion counts, and printed reasons are available. The individual-level relationship between the erroneous randomization and consent withdrawal is not stated.
- **Source-grounded alternative interpretation:** The narrative may use `consent withdrawal` as umbrella shorthand for all pre-analysis removals, or the erroneously assigned participant may also have lacked/withdrawn consent. Figure 1 presents that participant as a separate reason.
- **Direct observation versus inferred explanation:** The 10-versus-11 reason classification is direct. Umbrella shorthand or dual classification is inferred.
- **Exact remaining human question:** Did the erroneously assigned participant also withdraw consent, or should the narrative distinguish 10 consent withdrawals from one erroneous randomization assignment?

## C016 — Table S6 BA event count 9 conflicts with the matched primary-analysis count 11

- **Location found:** Yes — [DOC-001 primary-outcome narrative, PDF p. 5](<../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5>), [DOC-001 Table 2, PDF p. 8](<../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=8>), and [DOC-002 Table S6, PDF p. 19](<../../../joi240088supp1_prod_1746815064.21247.pdf#page=19>).
- **Source value/text matched:** The main narrative reports primary rates 4.4% versus 13.5%; Table 2 prints BA `11 (4.4)` and AMM `34 (13.5)` under n=249/252. Table S6, under the same n=249/252 headers and the same printed composite endpoint, gives BA `9 (3.9)` and AMM `34 (13.5)`.
- **Comparator matched:** The endpoint wording includes stroke/death within 30 days plus qualifying-artery ischemic stroke or revascularization beyond 30 days through one year in both Table 2 and Table S6. Table S6 is labeled a post hoc center-effect adjustment.
- **Consistency rule applicable:** Yes. Model adjustment can change an effect estimate, interval, or P value, but the observed event count for the same endpoint and labeled population should remain fixed unless the analysis set or outcome definition changes and is disclosed.
- **Calculation or logical comparison reproduced:** BA counts differ by `11-9=2`; AMM remains 34. The source separately shows a related composite excluding revascularization as BA 9 in Table S10, but Table S6 explicitly retains revascularization in its endpoint label. Also, as recorded for C004, `9/249=3.6%`, not Table S6's 3.9%.
- **Necessary inputs available:** Both endpoint labels, population headers, counts, percentages, and adjustment footnote are available. Missing inputs are a Table S6 event list, any alternate analysis-set definition, and the denominator used for 3.9%.
- **Source-grounded alternative interpretation:** Table S6 may use an unlabelled alternate set, or its BA count may derive from the related Table S10 composite that excludes revascularization while the label was retained. The adjustment footnote itself does not explain removal of two observed BA events.
- **Direct observation versus inferred explanation:** Matched labels, headers, and 11-versus-9 counts are direct. Alternate-set or cross-table carryover explanations are inferred.
- **Exact remaining human question:** Does Table S6 intentionally use a different population or composite definition, and if so where is it defined; otherwise, which event count and denominator generated its BA entry?

## C017 — One-year incidence-difference point estimate lies outside its confidence interval

- **Location found:** Yes — [DOC-001 Table 2, PDF p. 8](<../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=8>).
- **Source value/text matched:** For any stroke outside the qualifying-artery territory within one year, Table 2 prints BA `3 (1.2)`, AMM `4 (1.6)`, incidence difference `-0.4`, and `95% CI, -2.4 to -1.7`.
- **Comparator matched:** The point estimate and interval appear in the same incidence-difference column and row. The group counts, denominators 249/252, and percentages provide a crude-direction comparator.
- **Consistency rule applicable:** Yes for a point estimate and its paired conventional 95% confidence interval, subject to the source using the same estimand and method. The table does not state a distinct estimator for the interval.
- **Calculation or logical comparison reproduced:** `-0.4` is greater than both interval endpoints and is not contained in `[-2.4,-1.7]`. The crude count-derived difference is `(3/249 - 4/252) x 100 = -0.382482` percentage points, which rounds to `-0.4`; the displayed group percentages also give `1.2-1.6=-0.4`.
- **Necessary inputs available:** Printed point estimate, confidence limits, counts, group denominators, and group percentages are available. The exact confidence-interval construction and whether the point and interval use different adjusted estimands are not defined for this row.
- **Source-grounded alternative interpretation:** One confidence-limit sign or value may be transcribed, or the interval and point estimate may have been produced from different undisclosed estimands or methods. The table pairs them without such a distinction.
- **Direct observation versus inferred explanation:** Non-containment and the crude comparator are direct calculations from printed values. Transcription, sign error, or different-estimand explanations are inferred.
- **Exact remaining human question:** What are the intended lower and upper confidence limits for the `-0.4%` incidence difference, and were the point estimate and interval calculated for the same estimand and analysis method?

## Recheck scope summary

- **Stable IDs covered:** C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, and C017.
- **Count covered:** 17 of 17 assigned stable IDs.
- **Outstanding evidence definitions:** Row- or population-specific denominators for C001, C002, C004-C007, C011, and C014; measurement timing/reader and deviation handling for C008; visit-window semantics for C009; governing eligibility bound for C010; ordinal/visit-label semantics for C012-C013; exclusion reason classification for C015; Table S6 population/endpoint definition for C016; and incidence-difference CI construction for C017.
