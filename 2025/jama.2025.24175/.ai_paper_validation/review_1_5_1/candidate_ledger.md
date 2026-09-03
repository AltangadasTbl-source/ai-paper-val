# Candidate Ledger

## Registration basis

This ledger registers distinct qualifying observations from the current workflow-1.5.1 numeric relationship inventory, inferential-statistical relationship inventory, and the completed numeric, statistical-pass-1, and cross-source checkers. Direct PDFs are the evidence authority; mapped evidence is retained as a locator and provenance record. Every entry is **Pending Human Adjudication**. No severity, validity judgment, correction, or disposition is assigned.

Candidates were merged before registration only where the proposals address the same printed values/statements, comparator, and consistency rule. In particular, the day-15 numerator observation, APACHE-II P-value observation, eFigure 8B duplication, eFigure 9B interval observation, and site-count observation each had corroborating proposals and are registered once. Versioning is retained as an alternative interpretation where supplied materials do not resolve it; it is not used to suppress an otherwise document-grounded observation.

## Stable candidate cards

## C001 — Day-15 SOFA responder numerator differs between Table 2 and narrative

- **Status:** Pending Human Adjudication.
- **Primary category:** Cross-document numeric inconsistency.
- **Relationship/checker provenance:** N031; S005; NC-1; P1-01; cross-source Proposal 1.
- **Exact source locations:** [DOC-001 Table 2, PDF p. 6](<../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6>) and [DOC-001 Results narrative, PDF p. 7](<../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=7>).
- **Printed inputs and comparator:** Table 2 prints precision immunotherapy `52/131 (39.7%)` versus placebo `34/145 (23.4%)` for the day-15 endpoint. The matched narrative prints precision immunotherapy `51 of 131 (39.7%)` versus placebo `34 of 145 (23.4%)`.
- **Direct observation:** The same named endpoint, all-randomized arm denominator, and placebo comparator have different printed precision-arm numerators.
- **Rule, calculation, and tolerance:** A matched count/denominator/percentage occurrence should reconcile exactly. `52/131×100=39.6947%`, which rounds to `39.7%`; `51/131×100=38.9313%`, which rounds to `38.9%`. For a one-decimal percentage, the `39.7%` interval is `[39.65%, 39.75%)`; 38.9313% is outside it. Table-2 counts also give crude OR `(52×111)/(79×34)=2.15` rounded, matching its printed OR 2.15.
- **Inference and supported alternatives:** At least one printed occurrence requires reconciliation. The narrative numerator may be a transcription error, Table 2 may contain the inaccurate count, or a missing analysis-set distinction may exist; the latter is not stated because both occurrences print denominator 131.
- **Quality-control relevance:** The count and percentage are reusable binary-outcome inputs.
- **Exact human question:** Which precision-immunotherapy numerator, 51 or 52, is authoritative for the all-randomized day-15 responder endpoint, and which matched text/table/effect outputs require harmonization?

## C002 — Protocol and report print different IFN-gamma doses for immunoparalysis

- **Status:** Pending Human Adjudication.
- **Primary category:** Measure, label, or scale inconsistency.
- **Relationship/checker provenance:** N002, N044; NC-2.
- **Exact source locations:** [DOC-002 protocol v1.0, PDF p. 6](<../../joi250116supp1_prod_1771885794.26255.pdf#page=6>) (dose; p. 7 continues the regimen) and [DOC-001 intervention description, PDF pp. 2-3](<../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=2>).
- **Printed inputs and comparator:** Direct rendering of the protocol prints `sc rhIFNγ 100 µg once every other day`; the report prints `100 μg` subcutaneous recombinant human interferon gamma every 48 hours for 15 days.
- **Direct observation:** **NOT REPRODUCED in the supplied direct PDF.** The directly printed matched doses are both 100 µg; the prior ledger transcription of 20 µg is not present on the supplied protocol page.
- **Rule, calculation, and tolerance:** After matching intervention, route, frequency, and duration, one administered-dose definition should agree or be expressly versioned. The direct comparison is `100/100=1`, not the prior fivefold `100/20` comparison.
- **Inference and supported alternatives:** The 20-µg value may be a font-encoding/transcription error in locator evidence. A different, unsupplied approved protocol version remains possible but is not package evidence.
- **Quality-control relevance:** Dose is an intervention-defining quantitative field for trial characterization and downstream extraction.
- **Exact human question:** Does any approved source version outside the supplied PDF specify 20 µg, or should the ledger and source mapping be repaired to the directly printed 100-µg protocol dose?

## C003 — Primary responder cutoff is printed as 1.5 points in protocol and 1.4 points in report/SAP

- **Status:** Pending Human Adjudication.
- **Primary category:** Measure, label, or scale inconsistency.
- **Relationship/checker provenance:** N025, N045, N086, N089; NC-3.
- **Exact source locations:** [DOC-002 protocol v1.0, PDF p. 7](<../../joi250116supp1_prod_1771885794.26255.pdf#page=7>) and [pp. 24-26](<../../joi250116supp1_prod_1771885794.26255.pdf#page=24>); [DOC-001, PDF pp. 1, 5, and 7](<../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=1>); [DOC-002 SAP, PDF pp. 66-67](<../../joi250116supp1_prod_1771885794.26255.pdf#page=66>).
- **Printed inputs and comparator:** The directly inspected protocol, report, and SAP each print a `1.4`-point responder cutoff; SAP p. 67 defines `>1.4` as achievement and `≤1.4` as nonachievement.
- **Direct observation:** **NOT REPRODUCED in the supplied direct PDF.** No supplied protocol occurrence of the prior ledger's 1.5-point binary-responder cutoff was found.
- **Rule, calculation, and tolerance:** A binary responder cutoff should be traceable across sources and not conflated with a planning mean difference. The direct matched cutoff comparison is `1.4−1.4=0`.
- **Inference and supported alternatives:** The 1.5 value may be a character-recognition error in font-encoded derivative text. An unsupplied protocol version could differ, but the supplied package does not establish it.
- **Quality-control relevance:** The cutoff determines endpoint classification and the outcome extracted from the trial.
- **Exact human question:** Is there an approved version not supplied here that used 1.5 points, or should the ledger and affected mapping records be repaired to the supplied protocol's printed 1.4-point cutoff?

## C004 — Immunoparalysis entry-classification threshold differs between protocol and report/eMethods

- **Status:** Pending Human Adjudication.
- **Primary category:** Measure, label, or scale inconsistency.
- **Relationship/checker provenance:** N001, N046, N095, N105; NC-4.
- **Exact source locations:** [DOC-002 protocol v1.0, PDF p. 9](<../../joi250116supp1_prod_1771885794.26255.pdf#page=9>) (also repeated on p. 13); [DOC-001, PDF pp. 1-2](<../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=1>); [DOC-003 eMethods/eTable 4, PDF p. 13](<../../joi250116supp2_prod_1771885794.27755.pdf#page=13>); comparator [DOC-002 SAP reversal definition, PDF p. 69](<../../joi250116supp1_prod_1771885794.26255.pdf#page=69>).
- **Printed inputs and comparator:** The protocol, report, and eMethods print entry classification as ferritin at or below 4420 ng/mL plus HLA-DR below `5000` molecules/monocyte. SAP p. 69 separately prints restoration above `8000` with ferritin below 4420 for day-15 reversal.
- **Direct observation:** **NOT REPRODUCED in the supplied direct PDF.** Direct entry-classification sources agree at 5000; 8000 is printed for the separately named reversal endpoint, not for entry classification.
- **Rule, calculation, and tolerance:** Entry and reversal thresholds must be distinguished, and only matched definitions should be compared as identities. The supplied entry sources have no 8000-versus-5000 discrepancy.
- **Inference and supported alternatives:** The prior ledger comparison may have carried the SAP reversal threshold into the protocol entry rule, possibly compounded by font-encoded extraction. No direct source supports that transfer; an unsupplied approved entry definition remains possible.
- **Quality-control relevance:** The classifier changes immune-state membership and treatment allocation.
- **Exact human question:** Should the candidate and mapping be repaired to distinguish the directly printed 5000 entry criterion from the 8000 day-15 reversal criterion, or is there an unsupplied approved entry definition using 8000?

## C005 — Protocol sample-size, dropout, and total-target values do not reconcile

- **Status:** Pending Human Adjudication.
- **Primary category:** Denominator, proportion, or total inconsistency.
- **Relationship/checker provenance:** N057; NC-5.
- **Exact source location:** [DOC-002 protocol v1.0, PDF pp. 25-26](<../../joi250116supp1_prod_1771885794.26255.pdf#page=25>) (per-arm number and total on p. 26).
- **Printed inputs and comparator:** The directly printed statement is `117 patients ... per trial arm`, `about 15%` dropout, and total randomization `280`; it does not print 112 per arm.
- **Direct observation:** **NOT REPRODUCED as originally transcribed.** The ledger's 112-per-arm premise is absent from the supplied direct PDF.
- **Rule, calculation, and tolerance:** `2×117=234`; with exact 15% attrition, `234/(1−0.15)=275.29`, conventionally at least 276. N=280 leaves 238 after exactly 15% attrition (119 per arm), and `1−234/280=16.43%`. The prior 16-person/20%-attrition calculation is not reproducible; the four-participant difference beyond 276 may fit conservative rounding of “about 15%.”
- **Inference and supported alternatives:** Rounding the target to 280, allowing approximately 16.4% attrition, or applying an unstated randomization-block/operational inflation could explain the direct values.
- **Quality-control relevance:** Planning sample size and attrition assumptions are routinely extracted and compared across trial records.
- **Exact human question:** What rounding, randomization-block, or additional inflation convention produced N=280 from 117 per arm and about 15% dropout, and should the ledger's 112-per-arm premise be repaired?

## C006 — Historical-trial narrative and flow diagram give different personalized-immunotherapy death counts

- **Status:** Pending Human Adjudication.
- **Primary category:** Cross-document numeric inconsistency.
- **Relationship/checker provenance:** N066, N078; NC-6.
- **Exact source locations:** [DOC-002 historical-trial narrative, PDF p. 41](<../../joi250116supp1_prod_1771885794.26255.pdf#page=41>) and [DOC-002 Figure 1, PDF p. 50](<../../joi250116supp1_prod_1771885794.26255.pdf#page=50>).
- **Printed inputs and comparator:** The narrative gives placebo `18/21 (85.7%)` deaths and personalized immunotherapy `14/15 (93.3%)` deaths. Figure 1 gives early termination because of death `n=18` and `n=11`, respectively, for the displayed randomized arms.
- **Direct observation:** The placebo count agrees across the locations; the personalized-immunotherapy count is 14 in the narrative and 11 in the figure.
- **Rule, calculation, and tolerance:** Matched arm-specific death counts should agree, unless a different follow-up window is explicitly stated. `14/15=93.3%` whereas `11/15=73.3%`; the three-person difference is not rounding.
- **Inference and supported alternatives:** The figure may use a shorter early-termination window, or the figure/narrative count may be erroneous. The Figure 1 label does not itself state a 28-day window.
- **Quality-control relevance:** Arm-specific mortality counts and follow-up definitions are direct outcome inputs.
- **Exact human question:** Does Figure 1's `n=11` use a different time window from the narrative's 28-day mortality, or should the count/label in one occurrence be corrected?

## C007 — APACHE II Table 2 P value is incompatible with the displayed t-test inputs

- **Status:** Pending Human Adjudication.
- **Primary category:** Statistical reporting inconsistency.
- **Relationship/checker provenance:** N074; S019; NC-7; P1-02.
- **Exact source location:** [DOC-002 Table 2, PDF p. 48](<../../joi250116supp1_prod_1771885794.26255.pdf#page=48>).
- **Printed inputs and comparator:** Placebo `n=21`, APACHE II `18.2 ± 8.7`; personalized immunotherapy `n=15`, `30.5 ± 9.4`; printed `P=.376`, with a footnote identifying Student's t-test.
- **Direct observation:** The group sizes, means, SDs, P value, and named t-test are printed in the same table row/footnote.
- **Rule, calculation, and tolerance:** A two-sample diagnostic using the displayed values gives pooled SD about 9.00, SE about 3.04, `t≈4.05` (34 df; two-sided `P≈.0003`). Welch gives `t≈3.99` (about 29 df; `P≈.0004`). One-decimal rounding of the printed means/SDs cannot yield `.376`.
- **Inference and supported alternatives:** The P value may be transposed, a displayed input may be inaccurate, or an unreported transformed/different dataset analysis may have been used; the latter conflicts with the printed Student-t-test row label.
- **Quality-control relevance:** The baseline comparison is a reported balance result available for downstream extraction.
- **Exact human question:** Which APACHE-II P value, group input, or test is correct for this Table-2 comparison, and was `.376` transposed or generated from a different analysis?

## C008 — Figure 1 septic-shock classification children exceed their parent total

- **Status:** Pending Human Adjudication.
- **Primary category:** Denominator, proportion, or total inconsistency.
- **Relationship/checker provenance:** N078; NC-8.
- **Exact source location:** [DOC-002 Figure 1, PDF p. 50](<../../joi250116supp1_prod_1771885794.26255.pdf#page=50>).
- **Printed inputs and comparator:** The parent box says `Septic shock = 177`; its displayed child classifications are MALS `44 (24.8%)`, immunoparalysis `2 (1.1%)`, and intermediate `132 (74.0%)`.
- **Direct observation:** The figure presents three child classifications under the septic-shock parent without an overlap or fourth-category label.
- **Rule, calculation, and tolerance:** Mutually displayed flow branches should partition their parent. `44+2+132=178`, one above 177. Percentages total 99.9% due to rounding, but integer child counts cannot exceed the printed parent total.
- **Inference and supported alternatives:** One child count or the parent count may be typographic, or an unstated overlap/unclassified participant may exist. The diagram does not identify such an exception.
- **Quality-control relevance:** Classification denominators determine reported group sizes and proportions.
- **Exact human question:** Which Figure-1 count is intended—parent 177 or one of the three child counts—and was an overlap or unclassified participant omitted from the labelling?

## C009 — Four incompatible study-site totals are printed for the named ImmunoSep trial

- **Status:** Pending Human Adjudication.
- **Primary category:** Cross-document numeric inconsistency.
- **Relationship/checker provenance:** N002, N047, N084, N090; NC-9; cross-source Proposal 4.
- **Exact source locations:** [DOC-001, PDF p. 2](<../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=2>); [DOC-002 protocol v1.0, PDF p. 10](<../../joi250116supp1_prod_1771885794.26255.pdf#page=10>) (p. 9 concerns 14 sites for the distinct PROVIDE trial); [DOC-002 SAP design, PDF p. 65](<../../joi250116supp1_prod_1771885794.26255.pdf#page=65>); and [DOC-002 SAP logistic-model statement, PDF p. 67](<../../joi250116supp1_prod_1771885794.26255.pdf#page=67>).
- **Printed inputs and comparator:** The report prints `33 sites`; the direct protocol and SAP-design statements each print `24` ImmunoSep sites; SAP p. 67 says `31 study sites participated`.
- **Direct observation:** **NOT REPRODUCED as originally transcribed.** The ledger's protocol value 28 and its p. 1 report citation are incorrect. The distinct directly printed ImmunoSep values are 24, 31, and 33.
- **Rule, calculation, and tolerance:** A site-count quantity must match or be explicitly qualified as planned, activated, recruiting, participating, randomizing, or final. 24, 31, and 33 cannot be reconciled by rounding; the protocol and SAP-design 24 agree.
- **Inference and supported alternatives:** The counts may denote planned sites, participating sites when the SAP model was written, and final-report sites. That milestone mapping is plausible but not explicitly supplied.
- **Quality-control relevance:** Site total is a trial-scale descriptor commonly used in study characterization and cross-document verification.
- **Exact human question:** What operational milestone does each of 24, 31, and 33 denote, which is the final participating/enrolling-site total, and should the ledger's 28-site value and page citations be repaired?

## C010 — Figure 2C labels an HR/OR-sized association as a relative risk

- **Status:** Pending Human Adjudication.
- **Primary category:** Measure, label, or scale inconsistency.
- **Relationship/checker provenance:** S023; P1-03.
- **Exact source locations:** [DOC-002 Figure 2C, PDF p. 51](<../../joi250116supp1_prod_1771885794.26255.pdf#page=51>) and comparator [DOC-002 Figure 3, PDF p. 52](<../../joi250116supp1_prod_1771885794.26255.pdf#page=52>).
- **Printed inputs and comparator:** Figure 2C shows 69 deaths/34 survivors (`n=103`) versus 37 deaths/52 survivors (`n=89`) and labels `RR_death 2.82 (1.58-5.14), P<.0001`. Figure 3 prints HR `2.82 (1.58-5.14)` for immunoparalysis.
- **Direct observation:** Figure 2C carries an RR label on a value/CI that exactly repeat Figure 3's HR.
- **Rule, calculation, and tolerance:** The displayed counts give crude risk ratio `(69/103)/(37/89)=1.61`; they give crude odds ratio `(69×52)/(34×37)=2.85`, compatible with 2.82. No rounding can make the count-derived RR 2.82. Measure labels must identify the displayed quantity/scale correctly.
- **Inference and supported alternatives:** The Figure 2C association may be mislabelled HR or OR, or its count rows and printed estimate may represent different stated analyses. The source does not resolve which.
- **Quality-control relevance:** RR, OR, and HR are not interchangeable for evidence extraction or synthesis.
- **Exact human question:** Should Figure 2C label the reported association HR/OR rather than RR, or do its displayed count rows and 2.82 value correspond to different analyses that need explicit labelling?

## C011 — eTable 10 SII day-15 OR is inconsistent with its counts, CI, and P value

- **Status:** Pending Human Adjudication.
- **Primary category:** Statistical reporting inconsistency.
- **Relationship/checker provenance:** S040; P1-04.
- **Exact source location:** [DOC-003 eTable 10, PDF p. 22](<../../joi250116supp2_prod_1771885794.27755.pdf#page=22>).
- **Printed inputs and comparator:** For the SII day-15 response row, the table prints `40/106` versus `29/122`, OR `1.194 (1.09-3.45)`, `P=.030`.
- **Direct observation:** The counts, point estimate, CI, and P value are printed in the same result row.
- **Rule, calculation, and tolerance:** The crude OR from counts is `(40×93)/(66×29)=1.94`. The log-scale midpoint of CI 1.09-3.45 is approximately 1.94; `P=.030` is compatible with the 1.94 scale, not 1.194. Although 1.194 falls inside the interval, the counts and CI provide independent incompatible comparators; normal display rounding cannot explain the discrepancy.
- **Inference and supported alternatives:** `1.194` may be a decimal/transcription error (for example, 1.94), or the counts/CI/P may belong to a differently defined analysis. The printed row does not state such a distinction.
- **Quality-control relevance:** This is a stratum-specific effect estimate used in quantitative extraction.
- **Exact human question:** Is `1.194` a transcription/decimal error, or do the counts, CI, and P value belong to a different explicitly defined analysis?

## C012 — eFigure 8B repeats eFigure 7B interaction results under a different outcome caption

- **Status:** Pending Human Adjudication.
- **Primary category:** Cross-document numeric inconsistency.
- **Relationship/checker provenance:** S047, S049; P1-05; cross-source Proposal 2.
- **Exact source locations:** [DOC-003 eFigure 7B, PDF p. 51](<../../joi250116supp2_prod_1771885794.27755.pdf#page=51>) and [DOC-003 eFigure 8B, PDF p. 52](<../../joi250116supp2_prod_1771885794.27755.pdf#page=52>).
- **Printed inputs and comparator:** eFigure 7B is captioned primary endpoint and prints APACHE `0.47 (0.30-1.62), P=.70`, interaction `1.85 (0.66-5.19), P=.24`; CCI `0.22 (0.09-0.53), P=.001`, interaction `5.79 (2.34-15.05), P<.0001`; SOFA `0.56 (0.27-1.19), P=.13`, interaction `3.08 (1.37-6.96), P=.007`. eFigure 8B, captioned 28-day mortality, repeats all six rows exactly.
- **Direct observation:** The complete estimates, CIs, and P values are duplicated under captions naming different outcomes; their A panels display different event/total data.
- **Rule, calculation, and tolerance:** Interaction outputs for differently captioned outcomes must be identified as the same output if intentional. Exact repetition of six complete rows across distinct outcome captions cannot be resolved by numeric rounding, and no source statement asserts an identity.
- **Inference and supported alternatives:** eFigure 8B may have copied eFigure 7B, or its caption/outcome label may be wrong. The supplied figure cannot identify which component is authoritative.
- **Quality-control relevance:** Misassigned subgroup-interaction outputs can be propagated into outcome-specific evidence extraction.
- **Exact human question:** Does eFigure 8B require its own 28-day-mortality interaction output, or is its caption/outcome label incorrect?

## C013 — eFigure 9B APACHE interaction point estimate lies outside its stated CI

- **Status:** Pending Human Adjudication.
- **Primary category:** Statistical reporting inconsistency.
- **Relationship/checker provenance:** S051; P1-06; cross-source Proposal 3.
- **Exact source location:** [DOC-003 eFigure 9B, PDF p. 53](<../../joi250116supp2_prod_1771885794.27755.pdf#page=53>).
- **Printed inputs and comparator:** The APACHE II ≥25 interaction row prints OR `0.11`, 95% CI `0.36-3.42`, `P=.86`.
- **Direct observation:** The point estimate and confidence-interval endpoints are printed together on the stated OR scale.
- **Rule, calculation, and tolerance:** A confidence interval on the same ratio scale must contain its stated point estimate. `0.11 < 0.36`; therefore the point estimate is outside the printed interval. This is not a rounding-tolerance issue.
- **Inference and supported alternatives:** The estimate may be 1.11 rather than 0.11, an endpoint may be wrong, or the row may be misaligned. The source alone does not select the correction.
- **Quality-control relevance:** The interaction effect and CI are quantitative outputs used to interpret subgroup evidence.
- **Exact human question:** Which APACHE interaction component—the point estimate, CI endpoint(s), or row alignment—is correct in the original analysis output?

## C014 — Historical-trial death counts do not reconcile with the stated arm percentages

- **Status:** Pending Human Adjudication.
- **Primary category:** Numeric or arithmetic inconsistency.
- **Relationship/checker provenance:** N066, N073, N078; cross-source Proposal 5.
- **Exact source locations:** The cited [DOC-002 PDF p. 42](<../../joi250116supp1_prod_1771885794.26255.pdf#page=42>) is Discussion text and does not contain the alleged mortality pairs. The direct mortality sentence is on [PDF p. 41](<../../joi250116supp1_prod_1771885794.26255.pdf#page=41>); [Table 2 is p. 48](<../../joi250116supp1_prod_1771885794.26255.pdf#page=48>) and [Figure 1 is p. 50](<../../joi250116supp1_prod_1771885794.26255.pdf#page=50>).
- **Printed inputs and comparator:** Direct p. 41 prints placebo `18/21 (85.7%)` and personalized immunotherapy `14/15 (93.3%)`. Table 2 provides denominators 21 and 15 but no mortality count/percentage pair; its `10 (47.6%)` and `12 (80.0%)` values are unrelated baseline-treatment rows. Figure 1's 18 and 11 early-termination counts are separately addressed in C006.
- **Direct observation:** **NOT REPRODUCED in the supplied direct PDF.** The alleged p. 42 mortality pairs `11/21 (47.6%)` and `15/15 (80.0%)` are not printed as a matched mortality statement; the actual p. 41 mortality pairs reconcile.
- **Rule, calculation, and tolerance:** A mortality count/percentage must reconcile with its arm denominator, but that rule cannot be applied to the prior ledger's assembled, unsupported pairs. The directly printed pairs are coherent: `18/21=85.7%` and `14/15=93.3%`.
- **Inference and supported alternatives:** The prior ledger may have combined Figure-1's death count 11 with unrelated Table-2 values and a page-shifted narrative citation. A source outside the supplied package could contain the alleged pairs, but it is not available here.
- **Quality-control relevance:** Arm-specific mortality count/percentage pairs are reusable outcome data.
- **Exact human question:** Is there any supplied or original analysis output that actually reports the ledger's alleged mortality pairs, or should C014's evidence statement be repaired while preserving C006's separate narrative-versus-flow count question?

## Proposal-to-ledger merge crosswalk

| Stable ID | Merged checker proposal(s) | Registration result |
|---|---|---|
| C001 | NC-1; P1-01; cross-source Proposal 1 | Same Table-2/narrative numerator comparator and reconciliation rule; merged. |
| C002 | NC-2 | Retained stable ID; direct-source recheck did not reproduce the 20-µg comparator. |
| C003 | NC-3 | Retained stable ID; direct-source recheck did not reproduce a 1.5-point binary-responder cutoff. |
| C004 | NC-4 | Retained stable ID; direct-source recheck found 5000 for entry and 8000 only for reversal. |
| C005 | NC-5 | Retained stable ID; direct-source recheck corrected 112 to 117 per arm. |
| C006 | NC-6 | Distinct p.41 narrative/Figure-1 death-count comparator. |
| C007 | NC-7; P1-02 | Same APACHE-II t-test/P-value comparator and diagnostic rule; merged. |
| C008 | NC-8 | Distinct Figure-1 subgroup-sum rule. |
| C009 | NC-9; cross-source Proposal 4 | Merged site-count question retained; direct-source recheck corrected 28 to 24 and the report citation to p. 2. |
| C010 | P1-03 | Distinct measure-label/count-derived-risk comparison. |
| C011 | P1-04 | Distinct SII OR/count-CI-P compatibility rule. |
| C012 | P1-05; cross-source Proposal 2 | Same eFigure-7B/eFigure-8B repeated-output comparator; merged. |
| C013 | P1-06; cross-source Proposal 3 | Same point-estimate/CI containment rule; merged. |
| C014 | cross-source Proposal 5 | Retained stable ID; alleged p. 42 mortality pairing was not reproduced and remains distinct from C006's direct 14-versus-11 comparator. |

## Registration summary

- Stable candidate IDs registered: C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014.
- Distinct candidates: 14.
- Display-zero-only observations registered: 0.
- Limitation: No participant-level dataset, analysis output, protocol amendment history, site-activation documentation, or unsupplied source version was available to resolve the remaining direct observations or source-mapping repair questions. All entries remain Pending Human Adjudication.
