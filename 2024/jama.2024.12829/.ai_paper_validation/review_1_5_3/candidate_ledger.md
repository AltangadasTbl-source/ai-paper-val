# Stable Candidate Ledger

All candidates below remain **Pending Human Adjudication**. Genuine duplicates were merged only when
they concerned the same printed values, comparator, and consistency rule. No candidate was suppressed
by count, importance, or expected conclusion impact. No display-zero-only candidate was registered.

## C001 — Balloon-angioplasty female percentage does not reconcile with count and denominator

- **Category:** Denominator, proportion, or total inconsistency
- **Locations:** [DOC-001 Table 1, PDF p. 6](<../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=6>)
- **Evidence and rule:** BA `n=249`, male `172 (69.1)`, female `77 (30.1)`. Counts sum to 249, but `77/249 × 100 = 30.9237%`, which rounds to `30.9%`, not `30.1%`.
- **Direct observation versus inference:** The printed mismatch is direct; which field is wrong is unresolved.
- **Alternatives and human question:** A hidden denominator or transcription error could explain it. Which of count 77, denominator 249, or percentage 30.1% is intended?
- **Checker provenance:** NP-01; cross-source Proposal 1
- **Status:** Pending Human Adjudication

## C002 — Balloon-angioplasty ischemic-stroke percentage is outside ordinary one-decimal rounding

- **Category:** Denominator, proportion, or total inconsistency
- **Locations:** [DOC-001 Table 1, PDF p. 6](<../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=6>); [DOC-002 Table S1, PDF p. 14](<../../joi240088supp1_prod_1746815064.21247.pdf#page=14>)
- **Evidence and rule:** Both locations print BA `n=249` and ischemic stroke `215 (86.4)`. `215/249 × 100 = 86.3454%`, ordinarily `86.3%`; the complementary `34/249` prints coherently as 13.7%.
- **Direct observation versus inference:** Repetition is direct; the ordinary-rounding diagnosis assumes nearest one-decimal rounding.
- **Alternatives and human question:** Was a documented nonstandard convention used, or should the repeated percentage or another printed input change?
- **Checker provenance:** NP-02
- **Status:** Pending Human Adjudication

## C003 — Table S4 procedure rows use 241 while the column header states 249

- **Category:** Denominator, proportion, or total inconsistency
- **Locations:** [DOC-002 Table S4, PDF p. 17](<../../joi240088supp1_prod_1746815064.21247.pdf#page=17>)
- **Evidence and rule:** Header BA `n=249`; footnote says 241 of 249 underwent BA. Procedure rows sum to 241 and percentages such as `182 (75.5)`, `214 (88.8)`, and `42 (17.4)` use 241, not 249.
- **Direct observation versus inference:** Header, footnote, and arithmetic are direct; the intended display structure is unresolved.
- **Alternatives and human question:** Is 249 arm context with a footnoted 241 denominator sufficient, or should applicable rows/column be explicitly labelled `n=241`?
- **Checker provenance:** NP-03
- **Status:** Pending Human Adjudication

## C004 — Table S6 BA `9 (3.9)` conflicts with its displayed denominator 249

- **Category:** Denominator, proportion, or total inconsistency
- **Locations:** [DOC-002 Table S6, PDF p. 19](<../../joi240088supp1_prod_1746815064.21247.pdf#page=19>)
- **Evidence and rule:** BA header `n=249`, primary outcome `9 (3.9)`. `9/249=3.6145%`, ordinarily `3.6%`; `3.9%` is compatible with 9/233, a different supplied population size.
- **Direct observation versus inference:** The internal mismatch is direct; 233 as the production denominator is diagnostic inference.
- **Alternatives and human question:** What analysis-set denominator produced 3.9%, and should it be printed or should another value change?
- **Checker provenance:** NP-04; SP-02/S033
- **Status:** Pending Human Adjudication

## C005 — Table S7 group headers conflict with site totals and displayed site percentages

- **Category:** Denominator, proportion, or total inconsistency
- **Locations:** [DOC-002 Table S7, PDF p. 20](<../../joi240088supp1_prod_1746815064.21247.pdf#page=20>); [DOC-001 Figure 1, PDF p. 5](<../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5>); [DOC-002 Table S10, PDF p. 23](<../../joi240088supp1_prod_1746815064.21247.pdf#page=23>)
- **Evidence and rule:** Headers state BA/AMM `N=233/238` (471 total), while site totals are 256 and 245 (501 total). Percentages `4 (2.9)`, `19 (16.1)`, `7 (6.3)`, `15 (11.2)` imply site-by-arm denominators summing to 249/252, not 233/238.
- **Direct observation versus inference:** The 471-versus-501 and header-percentage conflicts are direct; inferred site denominators are diagnostic.
- **Alternatives and human question:** Which analysis set and site-by-arm denominators were intended, and should the headers or rows be relabelled?
- **Checker provenance:** NP-05; cross-source Proposal 4; SP-03/S034
- **Status:** Pending Human Adjudication

## C006 — Table S8 per-protocol percentages conflict with headers 249/252

- **Category:** Denominator, proportion, or total inconsistency
- **Locations:** [DOC-002 Table S8, PDF p. 21](<../../joi240088supp1_prod_1746815064.21247.pdf#page=21>); [DOC-001 Figure 1, PDF p. 5](<../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5>); [DOC-002 Table S10, PDF p. 23](<../../joi240088supp1_prod_1746815064.21247.pdf#page=23>)
- **Evidence and rule:** PPS table headers print 249/252, but `9 (3.9)` and `33 (13.9)` use supplied PPS denominators 233/238; multiple additional rows follow the same denominator pattern.
- **Direct observation versus inference:** The header-percentage mismatch and supplied 233/238 comparator are direct.
- **Alternatives and human question:** Are Table S8 headers copy-forward values, or does it use an outcome-specific PPS not identified in the source?
- **Checker provenance:** NP-06; cross-source Proposal 5; SP-04/S035-S038
- **Status:** Pending Human Adjudication

## C007 — Table S9 as-treated percentages conflict with headers 249/252

- **Category:** Denominator, proportion, or total inconsistency
- **Locations:** [DOC-002 Table S9, PDF p. 22](<../../joi240088supp1_prod_1746815064.21247.pdf#page=22>); [DOC-002 Table S10, PDF p. 23](<../../joi240088supp1_prod_1746815064.21247.pdf#page=23>)
- **Evidence and rule:** ATS headers print 249/252, but primary values `11 (4.5)` and `34 (13.4)` reconcile with Table S10 ATS denominators 247/254, not the displayed headers.
- **Direct observation versus inference:** The cross-table denominator/percentage mismatch is direct; the intended correction is unresolved.
- **Alternatives and human question:** Are the Table S9 headers copied from the primary analysis, or is a different outcome-specific ATS intended?
- **Checker provenance:** NP-07; cross-source Proposal 6; SP-05/S039-S042
- **Status:** Pending Human Adjudication

## C008 — Baseline stenosis categories include four values outside the stated 70%-99% eligibility range

- **Category:** Analysis-unit or population inconsistency
- **Locations:** [DOC-001 eligibility, PDF p. 2](<../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=2>); [DOC-001 Figure 1, PDF p. 5](<../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5>); [DOC-001 Table 1, PDF p. 6](<../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=6>)
- **Evidence and rule:** Eligibility states 70%-99%; Table 1 contains two AMM participants at 60%-69% and one participant per arm at 100%, four analysed participants outside that interval.
- **Direct observation versus inference:** The threshold/category conflict is direct; measurement timing or retained deviations could explain it.
- **Alternatives and human question:** Were these different-time measurements or protocol deviations, and should the population/table definition state that distinction?
- **Checker provenance:** NP-08
- **Status:** Pending Human Adjudication

## C009 — Thirty-day follow-up tolerance is ±3 days in the supplement but ±7 days elsewhere

- **Category:** Measure, label, or scale inconsistency
- **Locations:** [DOC-002 study-design graphic, PDF p. 6](<../../joi240088supp1_prod_1746815064.21247.pdf#page=6>); [DOC-001 schedule, PDF p. 3](<../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=3>); [DOC-003 schedule, PDF p. 15](<../../joi240088supp2_prod_1746815064.36071.pdf#page=15>)
- **Evidence and rule:** The matched 30-day visit is printed `30±3 days` in DOC-002 and `30±7 days` in DOC-001/DOC-003, a 6-day versus 14-day total window.
- **Direct observation versus inference:** The labels differ directly; whether the graphic describes a distinct convention is unresolved.
- **Alternatives and human question:** Is `±3` intentional for a distinct visit or should it match the main/protocol `±7` schedule?
- **Checker provenance:** NP-09
- **Status:** Pending Human Adjudication

## C010 — Protocol V2.0 gives 21-day and 14-day lower bounds for the same stroke criterion

- **Category:** Measure, label, or scale inconsistency
- **Locations:** [DOC-003 synopsis, PDF p. 7](<../../joi240088supp2_prod_1746815064.36071.pdf#page=7>); [DOC-003 body eligibility, PDF p. 21](<../../joi240088supp2_prod_1746815064.36071.pdf#page=21>)
- **Evidence and rule:** The same protocol version says ischemic stroke `21-90 days` in the synopsis and `14-90 days` in the body, a seven-day difference in the lower bound.
- **Direct observation versus inference:** Same-version threshold conflict is direct; the cause is unknown.
- **Alternatives and human question:** Which lower bound governed enrolment, and is one occurrence a synopsis/body or amendment error?
- **Checker provenance:** NP-10
- **Status:** Pending Human Adjudication

## C011 — BA 3-month aspirin percentage does not reconcile with count and displayed arm denominator

- **Category:** Denominator, proportion, or total inconsistency
- **Locations:** [DOC-002 Table S3, PDF p. 16](<../../joi240088supp1_prod_1746815064.21247.pdf#page=16>)
- **Evidence and rule:** BA `n=249`, aspirin `234 (93.9)`. `234/249=93.9759%`, ordinarily `94.0%`, and no row-specific evaluated denominator is printed.
- **Direct observation versus inference:** Count/header/percentage mismatch is direct under ordinary rounding.
- **Alternatives and human question:** What denominator and rounding rule produced 93.9%, and which displayed input should be corrected or qualified?
- **Checker provenance:** NP-11
- **Status:** Pending Human Adjudication

## C012 — Figure S1 repeats “2nd meeting” for three chronologically distinct meetings

- **Category:** Measure, label, or scale inconsistency
- **Locations:** [DOC-002 Figure S1, PDF p. 10](<../../joi240088supp1_prod_1746815064.21247.pdf#page=10>)
- **Evidence and rule:** Four dated streams are labelled `1st`, `2nd`, `2nd`, `2nd meeting` for 2021-05-30, 2021-11-20, 2022-09-07, and 2023-04-10.
- **Direct observation versus inference:** Repeated numeric identifiers are direct; a hidden cycle convention is possible but unprinted.
- **Alternatives and human question:** Should the later streams be third/fourth meetings, or is there an intended reason to reuse `2nd`?
- **Checker provenance:** NP-12
- **Status:** Pending Human Adjudication

## C013 — Recurring-visit sentence ambiguously repeats visit numbers 9 and 11

- **Category:** Measure, label, or scale inconsistency
- **Locations:** [DOC-003 Protocol V2.0 paragraph, PDF p. 35](<../../joi240088supp2_prod_1746815064.36071.pdf#page=35>); [DOC-003 Protocol V2.3 paragraph, PDF p. 96](<../../joi240088supp2_prod_1746815064.36071.pdf#page=96>); [DOC-003 schedule, PDF p. 15](<../../joi240088supp2_prod_1746815064.36071.pdf#page=15>)
- **Evidence and rule:** The identical sentence in V2.0 and V2.3 lists `visit 8, visit 9, visit 10, visit 11, visit 9, and visit 11`; the schedule identifies visits 8-11 as four recurring visits.
- **Direct observation versus inference:** Repeated labels are direct. It is not established that the sentence intends a six-visit sequence; the last two occurrences may identify a face-to-face subset of the preceding four.
- **Alternatives and human question:** Does the sentence list a sequence of six visits or four recurring visits followed by the visit 9/11 subset, and should punctuation or wording make that structure explicit?
- **Checker provenance:** NP-13
- **Status:** Pending Human Adjudication

## C014 — Table S9 BA `8 (3.3)` does not round from either supplied ATS or displayed denominator

- **Category:** Numeric or arithmetic inconsistency
- **Locations:** [DOC-002 Table S9, PDF p. 22](<../../joi240088supp1_prod_1746815064.21247.pdf#page=22>); [DOC-002 Table S10, PDF p. 23](<../../joi240088supp1_prod_1746815064.21247.pdf#page=23>)
- **Evidence and rule:** BA 30-day ATS outcome is `8 (3.3)`. `8/247=3.2389%` and `8/249=3.2129%`; both ordinarily round to `3.2%`, not `3.3%`.
- **Direct observation versus inference:** Printed values are direct; 247 is the source-grounded ATS comparator and ordinary rounding is assumed.
- **Alternatives and human question:** Was a hidden risk-set denominator or nonstandard convention used, and what generated `8 (3.3)`?
- **Checker provenance:** NP-14
- **Status:** Pending Human Adjudication

## C015 — Narrative assigns all 11 pre-analysis exclusions to consent withdrawal while Figure 1 assigns only 10

- **Category:** Cross-document numeric inconsistency
- **Locations:** [DOC-001 narrative, PDF p. 4](<../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=4>); [DOC-001 Figure 1, PDF p. 5](<../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5>)
- **Evidence and rule:** Narrative says 11 excluded due to consent withdrawal. Figure 1 shows 7 BA plus 3 AMM consent withdrawals and 1 AMM erroneous randomization assignment: 10 withdrawal + 1 other.
- **Direct observation versus inference:** The reason-category mismatch for the same 11 participants is direct.
- **Alternatives and human question:** Is the narrative umbrella shorthand, or did the erroneous-assignment participant also withdraw consent? Which classification is intended?
- **Checker provenance:** cross-source Proposal 2
- **Status:** Pending Human Adjudication

## C016 — Table S6 BA event count 9 conflicts with the matched primary-analysis count 11

- **Category:** Cross-document numeric inconsistency
- **Locations:** [DOC-001 primary narrative, PDF p. 5](<../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5>); [DOC-001 Table 2, PDF p. 8](<../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=8>); [DOC-002 Table S6, PDF p. 19](<../../joi240088supp1_prod_1746815064.21247.pdf#page=19>)
- **Evidence and rule:** Main primary result is BA `11 (4.4%)` of 249; centre-adjusted Table S6 prints the same endpoint/header but BA `9 (3.9)`. Model adjustment may change HR/CI/P, not the observed count for the same labelled population.
- **Direct observation versus inference:** Matched count conflict is direct; whether Table S6 actually uses an unlabelled alternative set is unresolved.
- **Alternatives and human question:** Does Table S6 use a different eligible/per-protocol set, or is its count, header, or endpoint label wrong?
- **Checker provenance:** cross-source Proposal 3
- **Status:** Pending Human Adjudication

## C017 — One-year incidence-difference point estimate lies outside its confidence interval

- **Category:** Statistical reporting inconsistency
- **Locations:** [DOC-001 Table 2, PDF p. 8](<../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=8>)
- **Evidence and rule:** For stroke outside the qualifying-artery territory within one year, Table 2 prints BA `3 (1.2%)`, AMM `4 (1.6%)`, incidence difference `−0.4% (95% CI, −2.4 to −1.7)`. The point estimate −0.4 is outside `[-2.4, -1.7]`; count-derived crude difference is about −0.38 percentage points.
- **Direct observation versus inference:** Non-containment is direct; the count-derived value is a diagnostic comparator.
- **Alternatives and human question:** Are one or both endpoints transcribed, or do point and interval refer to differently adjusted estimands not identified by the table?
- **Checker provenance:** cross-source Proposal 7; SP-01/S013
- **Status:** Pending Human Adjudication

## Registration record

- **Stable IDs:** C001 through C017 (17 total).
- **Duplicate merges:** NP-01/cross Proposal 1; NP-04/SP-02; NP-05/cross Proposal 4/SP-03; NP-06/cross Proposal 5/SP-04; NP-07/cross Proposal 6/SP-05; cross Proposal 7/SP-01.
- **Deliberately distinct observations:** C004 is Table S6's internal denominator-percentage conflict; C016 is the separate matched count conflict. C007 is the Table S9 population-header conflict; C014 is the separate rounding mismatch for `8 (3.3)` under either supplied denominator.
- **Adjudication:** Every ID remains Pending Human Adjudication; no severity, validity, acceptance, exclusion, or correction is assigned.
