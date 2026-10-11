# Quantitative Quality-Control Consistency Review — Workflow 1.5.3

> ## Pending Human Adjudication
>
> Every observation in this report is a source-grounded quantitative reporting quality-control candidate. None is a final correction or conclusion about the paper’s findings.

## Executive Quality-Control Summary

Complete review of the supplied package identified **17 stable candidate consistency issues** (C001-C017). The review is framed as quantitative reporting quality control: small preventable defects can matter for downstream evidence extraction, but this report does not claim that any defect propagated, changed a conclusion, or caused serious harm. No review queue, top-N subset, or deferred-by-cap section was used. No coherent display-zero P value was registered as a candidate.

## Package and Reused-Evidence Provenance

The package contains three supplied PDFs: [main article](<../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=1>), [results supplement](<../joi240088supp1_prod_1746815064.21247.pdf#page=1>), and [protocol/SAP supplement](<../joi240088supp2_prod_1746815064.36071.pdf#page=1>). Existing native/layout text and rendered pages were reused as locators where fit for purpose; exact candidate statements were mechanically checked against the supplied PDFs. The evidence-asset inventory records 61 hashed reusable artifacts; source and reuse integrity are recorded in the versioned review artifacts.

## Scope, Complete Coverage, and Exclusions

| Source | Units | Reusable | Fresh required | Mapped | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 main article | 11 pages | 11 | 0 | 11 | COMPLETE |
| DOC-002 results supplement | 25 pages | 18 | 7 | 25 | COMPLETE |
| DOC-003 protocol/SAP supplement | 167 pages | 0 | 167 | 167 | COMPLETE |
| **Total** | **203** | **29** | **174** | **203** | **COMPLETE** |

The review covered numeric, denominator, statistical, cross-document, measure/label, and rate/count relationships. It excluded broad methodological, clinical, novelty, misconduct, and raw-data auditing. A P value displayed as zero alone would not qualify; none occurred in this scope.

## Quantitative and Statistical Relationship Coverage

Numeric/reporting relationships N001-N042 were reviewed. Statistical pass 1 and independent statistical pass 2 each covered S001-S080. Pass 2 revisited the complete candidate ledger and mechanical rechecks, found no new candidate, and retained existing links C004-C007, C016, and C017 where applicable. Missing model/test definitions were retained as limitations rather than inferred.

## Candidate Index

| ID | Candidate |
|---|---|
| C001 | BA female percentage and displayed denominator |
| C002 | BA ischemic-stroke percentage rounding |
| C003 | Table S4 procedure denominator labeling |
| C004 | Table S6 `9 (3.9)` and displayed denominator |
| C005 | Table S7 headers, site totals, and site percentages |
| C006 | Table S8 PPS headers and percentages |
| C007 | Table S9 ATS headers and percentages |
| C008 | Eligibility threshold and baseline stenosis categories |
| C009 | Thirty-day follow-up tolerance |
| C010 | Protocol V2.0 stroke lower bound |
| C011 | Three-month aspirin percentage |
| C012 | Figure S1 meeting ordinals |
| C013 | Recurring-visit subset-versus-sequence ambiguity |
| C014 | Table S9 `8 (3.3)` rounding |
| C015 | Pre-analysis exclusion reason classification |
| C016 | Table S6 versus main primary-event count |
| C017 | Incidence difference and confidence interval |

## Candidate Evidence Cards

## C001 — Balloon-angioplasty female percentage does not reconcile with count and denominator

**Candidate statement:** The BA female percentage is inconsistent with the printed count and displayed arm denominator under ordinary nearest-one-decimal rounding.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [DOC-001 Table 1, PDF p. 6](<../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=6>)

**Source evidence:** BA `n=249`; male `172 (69.1)` and female `77 (30.1)`.

**Reported-versus-comparator:** Reported female `30.1%` versus `77/249`.

**Reasoning procedure:** Apply the displayed arm denominator and ordinary nearest-one-decimal rounding; the sex counts also provide an internal total check.

**Calculation:** `172+77=249`; `77/249×100=30.9237%`, ordinarily `30.9%`; printed sex percentages total `99.2%`.

**Alternative source-grounded interpretations:** A hidden row denominator, transcription difference, or another displayed input could explain the observation; the source does not identify the production field that should govern.

**Mechanical evidence recheck:** Location, values, comparator, and calculation were reproduced directly from the PDF; no row-specific denominator or display rule is printed.

**Quality-control relevance:** This is a baseline count/percentage reconciliation check.

**Potential downstream evidence impact:** If confirmed, an extractor could copy the BA female baseline proportion incorrectly; no propagation or conclusion change is asserted.

**Human verification steps:** Confirm the source dataset, the intended female percentage, denominator, and rounding rule.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Balloon-angioplasty ischemic-stroke percentage is outside ordinary one-decimal rounding

**Candidate statement:** The repeated BA ischemic-stroke percentage is conditionally inconsistent with ordinary nearest-one-decimal rounding.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [DOC-001 Table 1, PDF p. 6](<../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=6>); [DOC-002 Table S1, PDF p. 14](<../joi240088supp1_prod_1746815064.21247.pdf#page=14>)

**Source evidence:** Both tables print BA `n=249` and ischemic stroke `215 (86.4)`; the complement is `34 (13.7)`.

**Reported-versus-comparator:** Reported `86.4%` versus `215/249`.

**Reasoning procedure:** Reproduce count/denominator rounding and compare the complementary row.

**Calculation:** `215/249×100=86.3454%`, ordinarily `86.3%`; `34/249×100=13.6546%`, ordinarily `13.7%`; counts sum to 249.

**Alternative source-grounded interpretations:** An unstated rounding convention could produce the repeated presentation; the difference is near the ordinary rounding boundary and should not be called definitively erroneous.

**Mechanical evidence recheck:** Both printed repetitions, the complement, and calculations were reproduced; no alternative convention is stated.

**Quality-control relevance:** This checks a repeated baseline event-composition percentage.

**Potential downstream evidence impact:** If confirmed, a baseline qualifying-event composition value could be copied differently by extractors; no further effect is assumed.

**Human verification steps:** Confirm the display convention and intended percentage in both source tables.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Table S4 procedure rows use 241 while the column header states 249

**Candidate statement:** Table S4 raises a denominator-label clarity question because procedure rows use the footnoted 241 participants while the column header states 249.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [DOC-002 Table S4, PDF p. 17](<../joi240088supp1_prod_1746815064.21247.pdf#page=17>)

**Source evidence:** The BA header is `n=249`; footnote a states that 241 of 249 underwent BA. Procedure rows include `182 (75.5)`, `214 (88.8)`, and `42 (17.4)`.

**Reported-versus-comparator:** Header `249` versus the linked footnoted procedure-applicable denominator `241`.

**Reasoning procedure:** Test the displayed procedure counts and percentages against the footnoted denominator, while treating the footnote as a possible resolving definition.

**Calculation:** `182+48+11=241`; `182/241=75.5%`, `214/241=88.8%`, and `42/241=17.4%` at one decimal.

**Alternative source-grounded interpretations:** The header may provide randomized-arm context and the footnote may sufficiently define the 241 denominator for procedure rows. The observation is not established incorrect arithmetic.

**Mechanical evidence recheck:** Header, footnote, rows, sums, and percentages were reproduced. Applicability is conditional because the footnote may fully resolve the presentation.

**Quality-control relevance:** Clear denominator labeling helps distinguish randomized-arm and procedure-applicable rates.

**Potential downstream evidence impact:** If confirmed as unclear, an extractor could use 249 rather than 241 for procedure rates; no downstream use is assumed.

**Human verification steps:** Determine whether footnote a is intended to govern every applicable procedure row and whether the current labeling is sufficiently explicit.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Table S6 BA `9 (3.9)` conflicts with its displayed denominator 249

**Candidate statement:** The Table S6 BA percentage does not reconcile with its displayed `n=249` under ordinary rounding.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [DOC-002 Table S6, PDF p. 19](<../joi240088supp1_prod_1746815064.21247.pdf#page=19>)

**Source evidence:** BA header `n=249`; primary-outcome cell `9 (3.9)`.

**Reported-versus-comparator:** Reported `3.9%` versus `9/249`.

**Reasoning procedure:** Apply the displayed header denominator; distinguish this internal percentage check from C016's separate cross-document count comparison.

**Calculation:** `9/249×100=3.6145%`, ordinarily `3.6%`. Diagnostically, `9/233×100=3.8627%`, ordinarily `3.9%`.

**Alternative source-grounded interpretations:** The 233 comparison is a diagnostic inference from a separately supplied PPS total, not a Table S6 label. An unlabelled analysis set or display rule remains possible.

**Mechanical evidence recheck:** The table cell, header, and arithmetic were reproduced; no Table S6 denominator for 3.9% is supplied.

**Quality-control relevance:** This checks the stated centre-adjusted analysis population and risk presentation.

**Potential downstream evidence impact:** If confirmed, a reviewer could extract an incorrect centre-adjusted population or risk; no conclusion change is asserted.

**Human verification steps:** Identify the Table S6 analysis denominator and intended percentage display rule.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Table S7 group headers conflict with site totals and displayed site percentages

**Candidate statement:** Table S7's group headers, site totals, and displayed site percentages do not all describe one disclosed population.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [DOC-002 Table S7, PDF p. 20](<../joi240088supp1_prod_1746815064.21247.pdf#page=20>); [DOC-001 Figure 1, PDF p. 5](<../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5>); [DOC-002 Table S10, PDF p. 23](<../joi240088supp1_prod_1746815064.21247.pdf#page=23>)

**Source evidence:** Headers are BA/AMM `233/238`; site totals are 256 and 245; cells include `4 (2.9)`, `19 (16.1)`, `7 (6.3)`, and `15 (11.2)`.

**Reported-versus-comparator:** Header total `471` versus site total `501`, with cell percentages inconsistent with the headers.

**Reasoning procedure:** Compare totals and assess each displayed percentage against disclosed and diagnostic denominators.

**Calculation:** `233+238=471`; `256+245=501`. Rounded cells are diagnostically compatible with site-by-arm denominators summing to `249/252`, not printed as such.

**Alternative source-grounded interpretations:** Derived site-by-arm denominators are diagnostic only. A different disclosed analysis population could explain the table if identified.

**Mechanical evidence recheck:** Headers, site totals, cells, and source comparators were reproduced; no single disclosed denominator resolves all elements.

**Quality-control relevance:** Site-level denominators affect interpretation of subgroup and interaction tables.

**Potential downstream evidence impact:** If confirmed, site risk or interaction-table extraction could use mismatched populations; no downstream outcome is asserted.

**Human verification steps:** Confirm the intended analysis set and site-by-arm denominators, then verify the headers and percentage bases.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Table S8 per-protocol percentages conflict with headers 249/252

**Candidate statement:** Table S8 is labelled PPS but its printed headers conflict with the denominators that reproduce its percentages.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [DOC-002 Table S8, PDF p. 21](<../joi240088supp1_prod_1746815064.21247.pdf#page=21>); [DOC-001 Figure 1, PDF p. 5](<../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5>); [DOC-002 Table S10, PDF p. 23](<../joi240088supp1_prod_1746815064.21247.pdf#page=23>)

**Source evidence:** PPS headers print `249/252`; rows include `9 (3.9)`, `33 (13.9)`, `6 (2.6)`, and `20 (8.4)`.

**Reported-versus-comparator:** Displayed `249/252` headers versus supplied PPS denominators `233/238`.

**Reasoning procedure:** Reproduce representative PPS cell percentages using the separately supplied PPS totals.

**Calculation:** `9/233=3.9%`, `33/238=13.9%`, `6/233=2.6%`, and `20/238=8.4%` at one decimal.

**Alternative source-grounded interpretations:** A copy-forward header is only an inferred mechanism. An outcome-specific PPS could exist but is not identified.

**Mechanical evidence recheck:** The cells, headers, and PPS comparators were reproduced; effect-estimate intervals were separately coherent.

**Quality-control relevance:** Per-protocol denominators are needed to interpret sensitivity results accurately.

**Potential downstream evidence impact:** If confirmed, PPS denominator and risk extraction could be inconsistent; no harm or conclusion change is assumed.

**Human verification steps:** Confirm the PPS definition and whether Table S8 headers should identify `233/238` or another stated set.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Table S9 as-treated percentages conflict with headers 249/252

**Candidate statement:** Table S9 is labelled ATS but its printed headers conflict with the denominators that reproduce its primary percentages.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [DOC-002 Table S9, PDF p. 22](<../joi240088supp1_prod_1746815064.21247.pdf#page=22>); [DOC-002 Table S10, PDF p. 23](<../joi240088supp1_prod_1746815064.21247.pdf#page=23>)

**Source evidence:** ATS headers print `249/252`; primary values include `11 (4.5)` and `34 (13.4)`.

**Reported-versus-comparator:** Displayed headers `249/252` versus supplied ATS denominators `247/254`.

**Reasoning procedure:** Reproduce representative percentages using the supplied ATS totals and retain C014 as a separate cell-level rounding observation.

**Calculation:** `11/247=4.5%` and `34/254=13.4%` at one decimal.

**Alternative source-grounded interpretations:** Copied primary headers are not directly observed; a different ATS definition remains possible if documented.

**Mechanical evidence recheck:** The headers, cells, and ATS comparator were reproduced. C014 remains distinct because it tests `8 (3.3)` under both supplied denominators.

**Quality-control relevance:** Accurate ATS population labels are needed for sensitivity-analysis interpretation.

**Potential downstream evidence impact:** If confirmed, ATS population and risk values could be extracted with the wrong denominator; no other impact is claimed.

**Human verification steps:** Confirm the ATS set and intended Table S9 headers before extracting its risks.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — Baseline stenosis categories include values outside the stated 70%-99% eligibility range

**Candidate statement:** A cross-location threshold/category mismatch is present between the stated eligibility interval and four Table 1 baseline categories; measurement identity is unresolved.

**Category:** Analysis-unit or population inconsistency

**Exact source locations:** [DOC-001 eligibility, PDF p. 2](<../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=2>); [DOC-001 Figure 1, PDF p. 5](<../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5>); [DOC-001 Table 1, PDF p. 6](<../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=6>)

**Source evidence:** Eligibility is `70%-99%`; Table 1 includes AMM `2` at `60%-69%` and one participant in each arm at `100%`.

**Reported-versus-comparator:** Eligibility interval `70%-99%` versus displayed analysed baseline categories outside that interval.

**Reasoning procedure:** Compare the printed threshold to the table categories only conditionally on the same measurement time, reader, angiogram, and qualifying-artery definition.

**Calculation:** `2+1+1=4` displayed participants are outside the inclusive `70%-99%` interval.

**Alternative source-grounded interpretations:** Eligibility and table measurements may be from different times/readers or angiograms; retained protocol deviations are also possible. The sources do not establish identity conditions.

**Mechanical evidence recheck:** Threshold, categories, counts, and flow context were reproduced; measurement identity conditions are missing.

**Quality-control relevance:** The observation concerns the clarity of analysed baseline stenosis and eligibility definitions, not a determination that participants were ineligible.

**Potential downstream evidence impact:** If confirmed, extractors could conflate baseline stenosis distribution with the eligibility definition; no validity or conclusion claim is made.

**Human verification steps:** Establish the measurement timing, reader/method, qualifying artery, and handling of any retained deviations.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C009 — Thirty-day follow-up tolerance is plus or minus 3 days in the supplement but plus or minus 7 days elsewhere

**Candidate statement:** The matched 30-day follow-up is labelled `±3` days in one supplied location and `±7` days in two others.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [DOC-002 study-design graphic, PDF p. 6](<../joi240088supp1_prod_1746815064.21247.pdf#page=6>); [DOC-001 schedule, PDF p. 3](<../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=3>); [DOC-003 schedule, PDF p. 15](<../joi240088supp2_prod_1746815064.36071.pdf#page=15>)

**Source evidence:** DOC-002 prints `30±3d`; DOC-001 and DOC-003 print `30±7 days`/`30d±7d`.

**Reported-versus-comparator:** `±3` versus `±7` for the matched nominal 30-day visit.

**Reasoning procedure:** Compare visit labels across the graphic, article, and protocol, absent a stated distinct operational window.

**Calculation:** `30±3` spans days 27-33 (numerical endpoint-to-endpoint width 6); `30±7` spans days 23-37 (width 14); half-widths differ by 4 days.

**Alternative source-grounded interpretations:** The graphic may depict a tighter operational contact window while the article/protocol allow a wider assessment window, but no source defines that distinction.

**Mechanical evidence recheck:** All three labels and their visit context were reproduced; no separate-window note was found.

**Quality-control relevance:** Follow-up-window labels support consistent protocol and outcome-time extraction.

**Potential downstream evidence impact:** If confirmed, an extractor or implementer could select a different 30-day tolerance; no downstream effect is asserted.

**Human verification steps:** Determine whether the two tolerances are distinct documented windows or which label governs the clinical visit.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C010 — Protocol V2.0 gives 21-day and 14-day lower bounds for the same stroke criterion

**Candidate statement:** Protocol V2.0 prints two different lower bounds for the matched ischemic-stroke eligibility criterion.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [DOC-003 synopsis, PDF p. 7](<../joi240088supp2_prod_1746815064.36071.pdf#page=7>); [DOC-003 body eligibility, PDF p. 21](<../joi240088supp2_prod_1746815064.36071.pdf#page=21>)

**Source evidence:** The synopsis prints `21-90 days`; the body prints `14-90 days`.

**Reported-versus-comparator:** Same-version lower bound `21` versus `14` days.

**Reasoning procedure:** Match protocol version, criterion, and upper bound before comparing lower bounds.

**Calculation:** Lower bounds differ by `21-14=7` days.

**Alternative source-grounded interpretations:** A stale synopsis, unmarked amendment, or other production difference could explain the mismatch; the governing criterion is not established.

**Mechanical evidence recheck:** Both occurrences were found and matched to Protocol V2.0; cause is not supplied.

**Quality-control relevance:** Eligibility-window labels require a single interpretable definition.

**Potential downstream evidence impact:** If confirmed, protocol eligibility-window extraction could differ by seven days; no enrolment or conclusion effect is asserted.

**Human verification steps:** Identify which V2.0 occurrence governed enrolment and whether one needs an amendment or clarification.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C011 — BA 3-month aspirin percentage does not reconcile with count and displayed arm denominator

**Candidate statement:** The BA three-month aspirin percentage is inconsistent with the displayed arm denominator under ordinary nearest-one-decimal rounding.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [DOC-002 Table S3, PDF p. 16](<../joi240088supp1_prod_1746815064.21247.pdf#page=16>)

**Source evidence:** BA header `n=249`; three-month aspirin `234 (93.9)`.

**Reported-versus-comparator:** Reported `93.9%` versus `234/249`.

**Reasoning procedure:** Apply the only printed BA denominator, while retaining missingness and display-rule uncertainty.

**Calculation:** `234/249×100=93.9759%`, ordinarily `94.0%`; truncation would display `93.9%`.

**Alternative source-grounded interpretations:** Truncation, weighting, an undisclosed evaluated denominator, or missingness handling could explain the presentation. No alternative integer denominator no larger than 249 is identified as the answer.

**Mechanical evidence recheck:** Cell, header, and arithmetic were reproduced; actual three-month denominator and display rule are absent.

**Quality-control relevance:** This checks follow-up medication-use percentage reporting.

**Potential downstream evidence impact:** If confirmed, medication-use extraction may copy a different percentage; no clinical or conclusion implication is claimed.

**Human verification steps:** Confirm the evaluated denominator, missingness handling, and display rule for the three-month cell.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C012 — Figure S1 repeats “2nd meeting” for three chronologically distinct meetings

**Candidate statement:** Figure S1 repeats the ordinal `2nd meeting` for three different dates within the displayed review process.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [DOC-002 Figure S1, PDF p. 10](<../joi240088supp1_prod_1746815064.21247.pdf#page=10>)

**Source evidence:** The figure labels `1st` (2021/05/30), then `2nd` (2021/11/20, 2022/09/07, and 2023/04/10).

**Reported-versus-comparator:** Four chronologically distinct dated boxes versus two unique ordinal labels.

**Reasoning procedure:** Test ordinal uniqueness only if the labels represent one chronological meeting sequence.

**Calculation:** Four dated boxes contain only two unique ordinals; `2nd meeting` appears three times.

**Alternative source-grounded interpretations:** An unprinted review-cycle convention could use `2nd` repeatedly. The figure does not label such a cycle; its case-count arithmetic separately reconciles.

**Mechanical evidence recheck:** The direct rendered PDF page confirmed all labels and dates.

**Quality-control relevance:** Timeline labels should permit unambiguous interpretation of the review process.

**Potential downstream evidence impact:** If confirmed, chronology of CEC meetings could be extracted ambiguously; endpoint counts are not challenged.

**Human verification steps:** Confirm whether ordinals denote one chronology or repeated review cycles, and clarify the figure accordingly.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C013 — Recurring-visit sentence ambiguously repeats visit numbers 9 and 11

**Candidate statement:** The identical recurring-visit sentence is ambiguous between a four-visit sequence with a face-to-face subset and a six-token sequence because it repeats visits 9 and 11.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [DOC-003 Protocol V2.0 paragraph, PDF p. 35](<../joi240088supp2_prod_1746815064.36071.pdf#page=35>); [DOC-003 Protocol V2.3 paragraph, PDF p. 96](<../joi240088supp2_prod_1746815064.36071.pdf#page=96>); [DOC-003 schedule, PDF p. 15](<../joi240088supp2_prod_1746815064.36071.pdf#page=15>)

**Source evidence:** V2.0 p. 35 and V2.3 p. 96 each print `visit 8, visit 9, visit 10, visit 11, visit 9, and visit 11 require patients to undergo face-to-face follow-up`; the schedule identifies visits 8-11 as four recurring visits.

**Reported-versus-comparator:** Six visit tokens `8,9,10,11,9,11` versus the four-visit schedule `8-11`.

**Reasoning procedure:** Compare the sentence with the schedule, preserving the distinction that p. 35 is Protocol V2.0 and p. 96 is final Protocol V2.3.

**Calculation:** Six tokens contain four unique identifiers; 9 and 11 each occur twice.

**Alternative source-grounded interpretations:** The sentence plausibly lists visits 8-11 and then names visits 9 and 11 as the face-to-face subset, with missing clarifying syntax. A six-visit sequence is not established.

**Mechanical evidence recheck:** Both versioned occurrences, the schedule, and the version identities were reproduced directly.

**Quality-control relevance:** Clarifying subset-versus-sequence syntax supports accurate longitudinal visit labeling.

**Potential downstream evidence impact:** If confirmed, longitudinal follow-up schedules could be extracted ambiguously; no protocol-compliance or outcome effect is claimed.

**Human verification steps:** Confirm whether visits 9 and 11 are the face-to-face subset of visits 8-11, then clarify the syntax in both versioned occurrences if needed.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C014 — Table S9 BA `8 (3.3)` does not round from either supplied ATS or displayed denominator

**Candidate statement:** The Table S9 BA `8 (3.3)` cell does not round to 3.3% from either the displayed or supplied ATS denominator.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [DOC-002 Table S9, PDF p. 22](<../joi240088supp1_prod_1746815064.21247.pdf#page=22>); [DOC-002 Table S10, PDF p. 23](<../joi240088supp1_prod_1746815064.21247.pdf#page=23>)

**Source evidence:** Table S9 prints BA `8 (3.3)` and header `249`; Table S10 supplies ATS `N=247`.

**Reported-versus-comparator:** Reported `3.3%` versus both `8/249` and `8/247`.

**Reasoning procedure:** Apply ordinary nearest-one-decimal rounding to both supplied denominators; this is distinct from C007's header/population issue.

**Calculation:** `8/249×100=3.2129%` and `8/247×100=3.2389%`; both ordinarily round to `3.2%`.

**Alternative source-grounded interpretations:** An unprinted outcome-specific risk set or nonstandard display rule could explain `3.3%`; neither is supplied.

**Mechanical evidence recheck:** Both table locations, values, and calculations were reproduced.

**Quality-control relevance:** This is a separate early ATS event-risk arithmetic check.

**Potential downstream evidence impact:** If confirmed, an extractor could copy the early ATS risk inaccurately; no broader effect is asserted.

**Human verification steps:** Identify the cell's intended denominator and percentage convention.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C015 — Narrative assigns all 11 pre-analysis exclusions to consent withdrawal while Figure 1 assigns only 10

**Candidate statement:** The narrative and Figure 1 reconcile to the same total removals but assign different reason categories to the 11 pre-analysis exclusions.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [DOC-001 narrative, PDF p. 4](<../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=4>); [DOC-001 Figure 1, PDF p. 5](<../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5>)

**Source evidence:** Narrative: 11 excluded due to consent withdrawal. Figure: BA 7 plus AMM 3 consent withdrawals, plus 1 erroneous randomization assignment.

**Reported-versus-comparator:** Narrative reason category for `11` versus Figure reason categories totaling `10+1`.

**Reasoning procedure:** Match the randomized-to-analysed flow and compare reason-category assignments without disputing the total.

**Calculation:** `7+3=10` consent withdrawals; `10+1=11` total removals; the 501-person analysed total reconciles.

**Alternative source-grounded interpretations:** The narrative may use umbrella shorthand, or the erroneously assigned participant may also have withdrawn consent; Figure 1 presents a separate reason.

**Mechanical evidence recheck:** Both locations, totals, and reason counts were reproduced; individual-level dual classification is not supplied.

**Quality-control relevance:** Participant-flow reason categories should be consistently extractable.

**Potential downstream evidence impact:** If confirmed, a flow-data extractor could classify exclusions differently; the analysed total is not challenged.

**Human verification steps:** Establish whether the erroneous-assignment participant also withdrew consent and clarify the narrative/category distinction.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C016 — Table S6 BA event count 9 conflicts with the matched primary-analysis count 11

**Candidate statement:** Table S6 prints a BA count of 9 for a matched primary endpoint and `n=249` header where the main narrative and Table 2 print 11; this is distinct from C004.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [DOC-001 primary narrative, PDF p. 5](<../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5>); [DOC-001 Table 2, PDF p. 8](<../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=8>); [DOC-002 Table S6, PDF p. 19](<../joi240088supp1_prod_1746815064.21247.pdf#page=19>)

**Source evidence:** Main result: BA `11 (4.4)` and AMM `34 (13.5)` under `249/252`. Centre-adjusted Table S6 has the matched composite wording and headers but prints BA `9 (3.9)` and AMM `34 (13.5)`.

**Reported-versus-comparator:** Table S6 BA count `9` versus matched main BA count `11`.

**Reasoning procedure:** Match endpoint wording and population headers; distinguish model-adjusted effect estimates from observed counts.

**Calculation:** `11-9=2`; AMM remains `34`. Table S10's related no-revascularization composite has BA 9, but Table S6 retains revascularization in its label.

**Alternative source-grounded interpretations:** An unlabelled alternative set or carryover of the Table S10 no-revascularization count could explain the entry. Centre adjustment alone does not explain two fewer observed events.

**Mechanical evidence recheck:** Matched labels, headers, counts, and the Table S10 context were reproduced. Event list, alternate-set definition, and Table S6 denominator remain unavailable.

**Quality-control relevance:** This checks whether a centre-adjusted sensitivity table has an interpretable event count for the matched endpoint.

**Potential downstream evidence impact:** If confirmed, an extractor could record the centre-adjusted sensitivity event count inconsistently; no paper-level conclusion impact is asserted.

**Human verification steps:** Confirm the Table S6 population and endpoint definition, the BA event list, and whether the count should be 9 or 11.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C017 — One-year incidence-difference point estimate lies outside its confidence interval

**Candidate statement:** The printed one-year incidence-difference point estimate is not contained in its paired printed confidence interval.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [DOC-001 Table 2, PDF p. 8](<../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=8>)

**Source evidence:** For stroke outside the qualifying-artery territory within one year: BA `3 (1.2)`, AMM `4 (1.6)`, incidence difference `−0.4% (95% CI, −2.4 to −1.7)`.

**Reported-versus-comparator:** Point estimate `−0.4%` versus interval `[−2.4%, −1.7%]`.

**Reasoning procedure:** Test containment of a point estimate in its paired conventional confidence interval; treat the count-derived difference only as a diagnostic comparator.

**Calculation:** `−0.4` is outside `[−2.4,−1.7]`; `(3/249−4/252)×100=−0.3825` percentage points, which rounds to `−0.4%`.

**Alternative source-grounded interpretations:** A confidence-limit sign/value may be transcribed, or point and interval may use undisclosed different estimands/methods. The exact CI method is not supplied.

**Mechanical evidence recheck:** Row, point, interval, counts, denominators, and non-containment were reproduced. The interval construction and estimand mapping remain missing.

**Quality-control relevance:** Point/interval pairing is central to reliable statistical-result extraction.

**Potential downstream evidence impact:** If confirmed, a meta-analysis or evidence table could copy an incompatible incidence difference and interval; no actual propagation or conclusion change is claimed.

**Human verification steps:** Verify intended confidence limits, CI construction, and whether the point estimate and interval use the same estimand.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If confirmed, these candidate consistency issues could affect extraction of baseline composition, procedure and analysis-set denominators, follow-up windows, protocol eligibility labels, participant-flow reasons, sensitivity results, or statistical intervals. They are presented as bounded risks to evidence reuse only. The supplied sources do not establish propagation, patient harm, or a changed paper-level conclusion.

## Limitations and Missing Definitions

See the complete versioned limitations record: [limitations.md](<review_1_5_3/limitations.md>). In brief, unresolved denominator/display conventions, measurement identities, analysis-set/endpoint definitions, and statistical-model/test details prevent a final correction determination.

## Human Adjudication Checklist

1. Confirm that each cited source location and comparator refer to the same population, time point, endpoint, and analysis set.
2. Check production data, table shells, statistical output, protocol versions, and amendment history where applicable.
3. Record the decision only in each card’s five placeholder fields.
4. If a change is warranted, specify the authoritative source, correction, and affected cross-document occurrences.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

- **Routing preflight:** PASS; coordinator inference PASS; execution mode INTERACTIVE_CLI.
- **Source integrity:** 3 direct-source hashes and 61 reused-artifact hashes were recorded before review; the quality audit recorded a passing 64-path hash check.
- **Coverage:** 203 total source units; 174 fresh-source units; all 203 units mapped.
- **Candidate-set consistency:** C001-C017 are identical across ledger, recheck, audit, and this report.

### Agent execution

| Stage | Agent ID | Model | Effort |
|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high |
| reuse asset curator | /root/reuse_asset_curator | gpt-5.6-terra | medium |
| main mapper | /root/main_mapper | gpt-5.6-terra | medium |
| support mapper DOC-002 | /root/support_mapper_doc002 | gpt-5.6-terra | medium |
| support mapper DOC-003 pp. 1-32 | /root/support_mapper_001_032 | gpt-5.6-terra | medium |
| support mapper DOC-003 pp. 33-64 | /root/support_mapper_033_064 | gpt-5.6-terra | medium |
| support mapper DOC-003 pp. 65-96 | /root/support_mapper_065_096 | gpt-5.6-terra | medium |
| support mapper DOC-003 pp. 97-128 | /root/support_mapper_097_128 | gpt-5.6-terra | medium |
| support mapper DOC-003 pp. 129-160 | /root/support_mapper_129_160 | gpt-5.6-terra | medium |
| support mapper DOC-003 pp. 161-167 | /root/support_mapper_161_167 | gpt-5.6-terra | medium |
| support mapper merge | /root/support_mapper_merge | gpt-5.6-terra | medium |
| numeric reviewer | /root/numeric_reviewer | gpt-5.6-terra | medium |
| cross-source reviewer | /root/cross_source_reviewer | gpt-5.6-terra | medium |
| statistical pass 1 | /root/statistics_pass_1 | gpt-5.6-terra | high |
| evidence rechecker | /root/evidence_rechecker | gpt-5.6-sol | high |
| statistical pass 2 | /root/statistics_pass_2 | gpt-5.6-terra | high |
| quality auditor | /root/quality_auditor | gpt-5.6-sol | high |
| report generator | /root/report_generator | gpt-5.6-terra | medium |

### Performance

- **Target basis:** Three supplied PDFs contain 203 page units: an 11-page article fully covered by usable native text and targeted renders, a 25-page results supplement with 18 reusable pages and 7 uncovered pages, and a 167-page protocol/SAP with no reusable scientific extraction. The 174 fresh-required pages, the large protocol/SAP direct-mapping burden, visual-table confirmation, cross-document matching, and required independent reviewer stages justify this bounded target.
- **Total source units:** 203
- **Fresh-source units:** 174
- **Target elapsed minutes:** 65-90
- **Started UTC:** 2026-08-19T04:36:45Z
- **Finished UTC:** 2026-08-19T05:10:07Z
- **Observed elapsed minutes:** 33.37
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token accounting and cost

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Input tokens | Output tokens | Total tokens | Known token cost (USD) |
|---|---:|---:|---:|---:|
| gpt-5.6-sol | 0 | 0 | 0 | 0.000000 |
| gpt-5.6-terra | 0 | 0 | 0 | 0.000000 |

The coordinator will replace these markers after Markdown assembly from authoritative response-level runtime/API usage, then link the versioned [per-agent token summary](<review_1_5_3/token_usage_summary.md>). Cached input and cache-write counts are input subsets, and reasoning counts are output subsets; they are not added again to total tokens. Any available amount uses the bundled dated fixed-model rates and is a token-only estimate, not an invoice.
