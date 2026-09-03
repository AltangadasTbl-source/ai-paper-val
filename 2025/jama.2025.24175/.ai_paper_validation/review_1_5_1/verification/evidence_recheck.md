# Mechanical Evidence Recheck

## Scope and method

This recheck covers every registered stable ID, C001-C014. Every item remains **Pending Human Adjudication**. The supplied PDFs were treated as the authority. Current-workflow mappings and extracted text were used only as locators; cited result-bearing pages were then checked by direct PDF extraction or fresh CPU-only rendering. Page/value disagreements with the candidate ledger are recorded as repair facts and are not dispositions.

## C001 — Day-15 SOFA responder numerator differs between Table 2 and narrative

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes. DOC-001 Table 2 at [PDF p. 6](<../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6>) and the matched Results sentence at [PDF p. 7](<../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=7>) were found.
- **Source printed value/text matched:** Yes. Table 2 prints precision immunotherapy `52/131 (39.7%)` and placebo `34/145 (23.4%)` for the day-15 SOFA endpoint.
- **Comparator matched:** Yes. The narrative prints precision immunotherapy `51 of 131 (39.7%)` and placebo `34 of 145 (23.4%)` for the same endpoint.
- **Consistency rule applicable:** Yes. Matched count/denominator/percentage occurrences for the same arm, endpoint, and analysis population should reconcile exactly, subject only to percentage rounding.
- **Calculation or logical comparison reproduced:** `52/131×100=39.6947%`, which rounds to 39.7%; `51/131×100=38.9313%`, which rounds to 38.9%. The Table-2 crude OR is `(52×111)/(79×34)=2.15` rounded, matching the printed OR 2.15.
- **Necessary inputs available / exact missing inputs or definitions:** The two counts, denominators, percentage, endpoint, arms, and Table-2 OR are available. The participant-level endpoint listing and any undocumented population distinction are absent.
- **Source-grounded alternative interpretation:** One occurrence may contain a one-person transcription error, or an unstated analysis-set difference may exist; both occurrences nevertheless print denominator 131.
- **Direct observation versus inferred explanation:** Direct observation is `52/131` in Table 2 versus `51/131` in narrative with the same printed 39.7%. Any transcription mechanism or analysis-set explanation is inferred.
- **Exact remaining human question:** Which precision-immunotherapy numerator, 51 or 52, is authoritative for the all-randomized day-15 responder endpoint, and which matched text, table, percentage, and effect outputs require reconciliation?

## C002 — Protocol and report IFN-gamma dose comparison

- **Status:** Pending Human Adjudication.
- **Cited location found:** Partly. The cited DOC-002 [PDF p. 7](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=7>) exists but continues the regimen without printing a 20-µg dose. The dose itself is on DOC-002 [PDF p. 6](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=6>). DOC-001 prints the administered regimen across [PDF pp. 2-3](<../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=2>).
- **Source printed value/text matched:** No. Direct rendering of DOC-002 p. 6 prints `sc rhIFNγ 100 µg once every other day`, not 20 µg. This is a repair fact relative to the ledger.
- **Comparator matched:** Yes as to the report, but it does not conflict with the protocol. DOC-001 p. 3 prints `100 μg` subcutaneous recombinant human interferon gamma, with injections every 48 hours for 15 days stated on pp. 2-3.
- **Consistency rule applicable:** Yes. A matched intervention dose, route, frequency, and duration should agree or be expressly versioned.
- **Calculation or logical comparison reproduced:** The directly printed doses are `100 µg` and `100 µg`; their ratio is 1, not the ledger's fivefold `100/20` comparison.
- **Necessary inputs available / exact missing inputs or definitions:** Dose, route, frequency, duration, and the supplied protocol version label (`Version 1.0, 4 December 2020`) are available. No supplied page printing 20 µg was found; amendment history beyond the supplied document is absent.
- **Source-grounded alternative interpretation:** The 20-µg value appears consistent with a font-encoding/transcription error in the locator evidence rather than the rendered source. A different unsupplied protocol version remains possible but is not package evidence.
- **Direct observation versus inferred explanation:** Direct observation is agreement at 100 µg. The reason the ledger contains 20 µg is inferred.
- **Exact remaining human question:** Does any approved source version outside the supplied PDF actually specify 20 µg, or should the ledger/source mapping be repaired to the directly printed 100-µg protocol dose?

## C003 — Primary responder cutoff comparison

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes, but the cited protocol value does not match the ledger. DOC-002 [PDF p. 7](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=7>) prints 1.4 points; direct checks of the protocol endpoint and power statements on [PDF pp. 24-26](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=24>) also print 1.4. DOC-001 [PDF pp. 1, 5, and 7](<../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=1>) and DOC-002 SAP [PDF pp. 66-67](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=66>) were located.
- **Source printed value/text matched:** No. The supplied protocol prints 1.4, not the ledger's 1.5. This is a repair fact.
- **Comparator matched:** Yes. The report and SAP print 1.4; SAP p. 67 defines more than 1.4 as achieving the endpoint and 1.4 or less as not achieving it.
- **Consistency rule applicable:** Yes. A responder cutoff should be traceable across sources, while a planning mean difference must not be conflated with a binary classification threshold.
- **Calculation or logical comparison reproduced:** All directly inspected supplied occurrences use 1.4; `1.4−1.4=0`. No 0.1-point discrepancy was reproduced.
- **Necessary inputs available / exact missing inputs or definitions:** Supplied protocol, SAP, and report definitions are available. No supplied occurrence of the claimed 1.5-point value was found; any earlier or later unsupplied version is missing.
- **Source-grounded alternative interpretation:** The 1.5 value may be a character-recognition error in font-encoded derivative text. An unsupplied protocol version could differ, but the package does not establish that.
- **Direct observation versus inferred explanation:** Direct observation is cross-source agreement at 1.4. Any explanation for the ledger's 1.5 is inferred.
- **Exact remaining human question:** Is there an approved version not supplied here that used 1.5 points, or should the ledger and affected mapping records be repaired to the supplied protocol's printed 1.4-point value?

## C004 — Immunoparalysis entry-classification threshold comparison

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes. DOC-002 protocol [PDF pp. 8-9](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=8>), with the entry criterion printed on p. 9, DOC-001 [PDF pp. 1-2](<../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=1>), DOC-003 eMethods/eTable 4 [PDF p. 13](<../../../joi250116supp2_prod_1771885794.27755.pdf#page=13>), and DOC-002 SAP reversal definition [PDF p. 69](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=69>) were found.
- **Source printed value/text matched:** No. Direct protocol rendering prints ferritin at or below 4420 ng/mL plus HLA-DR below `5000` molecules/monocyte for entry classification, not below 8000. Protocol p. 13 independently repeats below 5000. This is a repair fact.
- **Comparator matched:** The report and eMethods also print below 5000 for entry. SAP p. 69 separately prints restoration above 8000 with ferritin below 4420 for day-15 reversal.
- **Consistency rule applicable:** Yes. Entry and reversal thresholds must be distinguished; only matched definitions should be compared as identities.
- **Calculation or logical comparison reproduced:** Entry sources agree at 5000. The 8000 value applies to the separately named reversal endpoint, so it is not a conflicting entry threshold.
- **Necessary inputs available / exact missing inputs or definitions:** Entry and reversal labels, biomarker context, and thresholds are available. No supplied source prints an 8000 entry threshold.
- **Source-grounded alternative interpretation:** The ledger likely carried the SAP reversal threshold into the protocol entry rule, possibly compounded by font-encoded extraction. No direct-source basis for that transfer was found.
- **Direct observation versus inferred explanation:** Direct observation is entry agreement at 5000 and a distinct reversal rule at 8000. The production mechanism of the ledger mismatch is inferred.
- **Exact remaining human question:** Should the candidate and mapping be repaired to distinguish the directly printed 5000 entry criterion from the 8000 day-15 reversal criterion, or is there an unsupplied approved entry definition using 8000?

## C005 — Protocol sample-size, dropout, and total-target arithmetic

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes. DOC-002 protocol [PDF pp. 25-26](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=25>) contains the power statement, with the per-arm number and total on p. 26.
- **Source printed value/text matched:** No as to the ledger's per-arm value. The source prints `117 patients ... per trial arm`, about 15% dropout, and total randomization of 280; it does not print 112 per arm. This is a repair fact.
- **Comparator matched:** The about-15% dropout and total 280 are matched; 117 per arm is the direct comparator to 280.
- **Consistency rule applicable:** Yes. A required analyzable total and an attrition allowance should reconcile under the stated or documented rounding/inflation convention.
- **Calculation or logical comparison reproduced:** `2×117=234`; `234/(1−0.15)=275.29`, conventionally at least 276. A target of 280 leaves 238 after exactly 15% attrition, or 119 per arm, and `1−234/280=16.43%`. Thus the ledger's 16-person/20%-attrition calculation from 112 per arm is not reproducible; the direct-source residual is four participants beyond 276 and may fit conservative rounding of “about 15%.”
- **Necessary inputs available / exact missing inputs or definitions:** Printed per-arm requirement, power, alpha, anticipated difference, dropout description, and target are available. The nQuery rounding rule, any block-size/site inflation, and any explicit conservatism leading from 276 to 280 are absent.
- **Source-grounded alternative interpretation:** Rounding a planning target to 280 or allowing approximately 16.4% attrition is consistent with the wording “about 15%”; an additional unstated allocation or operational constraint is also possible.
- **Direct observation versus inferred explanation:** Direct observation is 117 per arm, about 15%, and 280. Any rationale for selecting 280 rather than 276 is inferred.
- **Exact remaining human question:** What rounding, randomization-block, or additional inflation convention produced N=280 from 117 per arm and about 15% dropout, and should the ledger's 112-per-arm premise be repaired?

## C006 — Historical-trial narrative and flow diagram death counts

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes. DOC-002 historical-trial narrative [PDF p. 41](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=41>) and Figure 1 [PDF p. 50](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=50>) were found.
- **Source printed value/text matched:** Yes. The narrative prints 18 placebo deaths among 21 with 28-day mortality 85.7%, and 14 personalized-immunotherapy deaths among 15 with 28-day mortality 93.3%.
- **Comparator matched:** Yes. Figure 1 prints early termination because of death `n=18` for placebo and `n=11` for personalized immunotherapy.
- **Consistency rule applicable:** Yes, conditional on matching time windows. Arm-specific death counts should agree when the figure's early-termination count covers the same follow-up as 28-day mortality.
- **Calculation or logical comparison reproduced:** `18/21=85.7%`; `14/15=93.3%`; `11/15=73.3%`. Placebo agrees across locations; personalized immunotherapy differs by three deaths.
- **Necessary inputs available / exact missing inputs or definitions:** Arm denominators, narrative 28-day label, and figure early-termination counts are available. The figure does not define the time window or whether deaths after intervention termination but before day 28 are excluded from its early-termination box.
- **Source-grounded alternative interpretation:** Figure 1 may count deaths that terminated intervention during a shorter treatment window, while the narrative counts all deaths by day 28.
- **Direct observation versus inferred explanation:** Direct observation is 14 versus 11 for the personalized arm and agreement at 18 for placebo. A shorter figure time window or a typographic error is inferred.
- **Exact remaining human question:** Does Figure 1's personalized-arm `n=11` count only deaths causing treatment termination before a specified day, or should it reconcile to the narrative's 14 deaths by day 28?

## C007 — APACHE II Table 2 P value versus displayed t-test inputs

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes. DOC-002 Table 2 [PDF p. 48](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=48>) was directly rendered.
- **Source printed value/text matched:** Yes. The table prints placebo `n=21`, APACHE II `18.2 ± 8.7`; personalized immunotherapy `n=15`, `30.5 ± 9.4`; and `P=.376`.
- **Comparator matched:** Yes. The table footnote marks the row with an asterisk and defines the asterisk as comparison by Student's t-test.
- **Consistency rule applicable:** Yes. With group sizes, means, SDs, and a named two-group Student t-test, a diagnostic t statistic can be reproduced from the printed inputs.
- **Calculation or logical comparison reproduced:** Pooled SD is about 9.00; pooled-test SE is about 3.04; `t≈(30.5−18.2)/3.04≈4.05` with 34 df, giving a two-sided P value near .0003. Welch gives `t≈3.99` and a P value near .0004. Neither is compatible with .376 at the printed precision.
- **Necessary inputs available / exact missing inputs or definitions:** The displayed inputs and Student-test label are available. Raw observations, any transformation, and confirmation of equal-variance versus Welch implementation are absent, but either conventional calculation is far from .376.
- **Source-grounded alternative interpretation:** A mean, SD, group column, P value, or test label may be transposed or may come from a different unlabelled analysis.
- **Direct observation versus inferred explanation:** Direct observation is the printed row and footnote. The cause of the mismatch is inferred; the recomputation is a diagnostic based on the displayed summary statistics.
- **Exact remaining human question:** Which APACHE-II input, P value, or test label is authoritative in the original Table-2 analysis output?

## C008 — Figure 1 septic-shock child counts exceed parent total

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes. DOC-002 Figure 1 [PDF p. 50](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=50>) was directly rendered.
- **Source printed value/text matched:** Yes. The parent box prints `Septic shock = 177`.
- **Comparator matched:** Yes. Its displayed classifications print MALS `44 (24.8%)`, immunoparalysis `2 (1.1%)`, and intermediate status `132 (74.0%)`.
- **Consistency rule applicable:** Yes. The three displayed immune-state classifications appear as child branches of the septic-shock parent and should partition it unless overlap or a different denominator is stated.
- **Calculation or logical comparison reproduced:** `44+2+132=178`, which is one more than 177. Printed percentages sum to 99.9%, but rounding percentages cannot explain an integer child total above the parent.
- **Necessary inputs available / exact missing inputs or definitions:** Parent and child counts and labels are available. An overlap rule, alternate denominator, or exception note is absent.
- **Source-grounded alternative interpretation:** One count may be typographic, or a person may have been double-classified under an unstated rule; the diagram elsewhere describes three immune states without marking overlap.
- **Direct observation versus inferred explanation:** Direct observation is the 177 parent and child sum 178. Any typographic or overlap mechanism is inferred.
- **Exact remaining human question:** Which displayed parent or child count is authoritative, and was any overlap or denominator exception intended?

## C009 — Study-site totals across report, protocol, and SAP

- **Status:** Pending Human Adjudication.
- **Cited location found:** Partly, with page/value repairs. DOC-001 prints 33 sites on [PDF p. 2](<../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=2>), not p. 1. DOC-002 protocol prints 24 ImmunoSep sites on [PDF p. 10](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=10>), while p. 9 discusses 14 sites for the different PROVIDE trial. DOC-002 SAP prints 24 sites on [PDF p. 65](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=65>) and 31 participating sites on [PDF p. 67](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=67>).
- **Source printed value/text matched:** No as written in the ledger. The direct protocol value is 24, not 28; the report's 33-site statement is on p. 2, not p. 1. These are repair facts.
- **Comparator matched:** Yes after repair. The directly printed ImmunoSep values are 24 in protocol, 24 in SAP design, 31 participating in SAP model text, and 33 in the final report.
- **Consistency rule applicable:** Yes. Site counts must agree only after qualifying planned, approved, activated, participating, enrolling, and final-report definitions.
- **Calculation or logical comparison reproduced:** The distinct directly printed counts are 24, 31, and 33; no rounding rule reconciles them. The protocol and SAP-design 24 agree with each other.
- **Necessary inputs available / exact missing inputs or definitions:** Values and nearby wording are available. A site-level chronology identifying approved, activated, enrolled, contributed data, and final listed sites is absent.
- **Source-grounded alternative interpretation:** The 24 may be planned sites, 31 may be sites participating when the SAP model was written, and 33 may be the final report's study-site count. These milestones are plausible but not explicitly cross-walked.
- **Direct observation versus inferred explanation:** Direct observation is 24 versus 31 versus 33 and the incorrect ledger locations/value. Any milestone explanation is inferred.
- **Exact remaining human question:** What operational milestone does each of 24, 31, and 33 denote, which is the final participating/enrolling-site total, and should the ledger's 28-site value and page citations be repaired?

## C010 — Figure 2C relative-risk label versus displayed association

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes. DOC-002 Figure 2C [PDF p. 51](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=51>) and Figure 3 [PDF p. 52](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=52>) were directly rendered.
- **Source printed value/text matched:** Yes. Figure 2C prints 69 deaths and 34 survivors for the below-5000 group (`n=103`), 37 deaths and 52 survivors for the at-least-5000 group (`n=89`), and `RR` 2.82 (1.58-5.14), `P<.0001`.
- **Comparator matched:** Yes. Figure 3 prints univariate Cox HR 2.82 (1.58-5.14) for immunoparalysis versus intermediate status.
- **Consistency rule applicable:** Yes. A risk ratio derived from displayed risks should be on the risk-ratio scale; RR, OR, and HR labels are not interchangeable.
- **Calculation or logical comparison reproduced:** Crude RR is `(69/103)/(37/89)=1.61`; crude OR is `(69×52)/(34×37)=2.85`. The printed 2.82 (1.58-5.14) exactly matches the Figure-3 HR and is close to the crude OR, not the count-derived RR.
- **Necessary inputs available / exact missing inputs or definitions:** Counts, totals, printed label/value/CI, and matched Cox output are available. The exact model used for Figure 2C and whether its printed line was intended as crude RR, OR, or copied HR are not stated.
- **Source-grounded alternative interpretation:** Figure 2C may contain an RR label error, or its estimate may intentionally come from a model different from the displayed 2×2 counts but lacks the necessary model label.
- **Direct observation versus inferred explanation:** Direct observation is the RR label, counts, and exact repetition of the Figure-3 HR/CI. Mislabeling or copying is inferred.
- **Exact remaining human question:** What effect measure generated Figure 2C's 2.82 (1.58-5.14), and should it be labelled HR, OR, or another explicitly defined model estimate rather than RR?

## C011 — eTable 10 SII day-15 OR versus counts, CI, and P value

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes. DOC-003 eTable 10 [PDF p. 22](<../../../joi250116supp2_prod_1771885794.27755.pdf#page=22>) was directly extracted and rendered.
- **Source printed value/text matched:** Yes. The SII day-15 row prints `40/106 (37.7%)` versus `29/122 (23.8%)` and unadjusted OR `1.194`.
- **Comparator matched:** Yes. The same row prints 95% CI `1.09 to 3.45` and `P=.030`.
- **Consistency rule applicable:** Yes. An unadjusted OR should reconcile with its displayed 2×2 counts, and its ratio-scale CI should be centered near the point estimate on the log scale, subject to method-specific asymmetry.
- **Calculation or logical comparison reproduced:** The crude OR is `(40×93)/(66×29)=1.9436`. The geometric midpoint of the CI is `sqrt(1.09×3.45)=1.939`. Both are on a 1.94 scale, not 1.194. Exact P-value reconstruction is not asserted because the test method for this row is not printed.
- **Necessary inputs available / exact missing inputs or definitions:** Counts, totals, OR, CI, and P value are available. The CI/test method and any continuity or exact-test convention are absent.
- **Source-grounded alternative interpretation:** The point estimate may contain an extra `1` or misplaced decimal, or the estimate may have been paired with counts/CI/P from another analysis.
- **Direct observation versus inferred explanation:** Direct observation is the printed row. A transcription error is inferred; the crude OR and log-CI midpoint are reproduced diagnostics.
- **Exact remaining human question:** Is `1.194` the intended unadjusted OR, or should the original analysis output show an approximately 1.94 estimate matching the counts and CI?

## C012 — eFigure 8B repeats eFigure 7B under a different outcome caption

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes. DOC-003 eFigure 7B [PDF p. 51](<../../../joi250116supp2_prod_1771885794.27755.pdf#page=51>) and eFigure 8B [PDF p. 52](<../../../joi250116supp2_prod_1771885794.27755.pdf#page=52>) were directly rendered.
- **Source printed value/text matched:** Yes. eFigure 7B is labelled as primary-endpoint interaction tests and prints the six OR/CI/P rows beginning `0.47 (0.30-1.62), .70` and `1.85 (0.66-5.19), .24`, followed by the CCI and SOFA rows.
- **Comparator matched:** Yes. eFigure 8B is labelled as 28-day-mortality interaction tests and repeats all six rows exactly: 0.47, 1.85, 0.22, 5.79, 0.56, and 3.08 with identical CIs and P values.
- **Consistency rule applicable:** Yes. Distinct outcome captions should have their corresponding interaction output, or an intentional shared output must be explicitly identified.
- **Calculation or logical comparison reproduced:** Row-by-row visual comparison found exact equality of all six point estimates, all six CIs, and all six P values, while the A panels contain different endpoint-specific counts.
- **Necessary inputs available / exact missing inputs or definitions:** Both complete panels, captions, and A-panel counts are available. The original interaction-model outputs and figure-production history are absent.
- **Source-grounded alternative interpretation:** eFigure 8B may be a copy of eFigure 7B, or the eFigure 8 caption/outcome label may be incorrect. Exact equality by chance is not impossible, but the package provides no statement supporting it.
- **Direct observation versus inferred explanation:** Direct observation is complete six-row duplication under different outcome labels. Copying or caption error is inferred.
- **Exact remaining human question:** Does eFigure 8B require the actual 28-day-mortality interaction output, or is its 28-day caption/outcome designation incorrect?

## C013 — eFigure 9B APACHE interaction estimate outside its CI

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes. DOC-003 eFigure 9B [PDF p. 53](<../../../joi250116supp2_prod_1771885794.27755.pdf#page=53>) was directly rendered.
- **Source printed value/text matched:** Yes. The APACHE II at-least-25 by precision-immunotherapy interaction row prints OR `0.11`.
- **Comparator matched:** Yes. The same row prints 95% CI `0.36-3.42` and `P=.86`.
- **Consistency rule applicable:** Yes. A confidence interval for a ratio-scale point estimate must contain that point estimate when the estimate and interval refer to the same model parameter.
- **Calculation or logical comparison reproduced:** `0.11 < 0.36`, so the point estimate lies below the printed lower endpoint; display rounding cannot close a gap of 0.25.
- **Necessary inputs available / exact missing inputs or definitions:** Point estimate, CI, P value, row label, and OR scale are available. The original model coefficient, SE, and table-generation output are absent.
- **Source-grounded alternative interpretation:** The point estimate may have been intended as 1.11, an interval endpoint may be wrong, or values may be row-misaligned.
- **Direct observation versus inferred explanation:** Direct observation is noncontainment of 0.11 by 0.36-3.42. Each proposed production error is inferred.
- **Exact remaining human question:** Which APACHE interaction component—the point estimate, interval endpoint(s), or row alignment—matches the original model output?

## C014 — Historical-trial death count/percentage pairing

- **Status:** Pending Human Adjudication.
- **Cited location found:** Partly, but the claimed mortality sentence was not found. DOC-002 [PDF p. 42](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=42>) is Discussion text and does not print the ledger's count/percentage pairs. The actual historical-trial mortality sentence is on [PDF p. 41](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=41>); Table 2 is on [PDF p. 48](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=48>); Figure 1 is on [PDF p. 50](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=50>).
- **Source printed value/text matched:** No. The direct mortality narrative prints 18 placebo deaths with 85.7% and 14 personalized-immunotherapy deaths with 93.3%, not 11 with 47.6% and 15 with 80.0%. This is a repair fact.
- **Comparator matched:** No as a matched mortality comparator. Table 2 supplies denominators 21 and 15 but does not print death counts; it contains unrelated values such as 10 (47.6%) for community-acquired pneumonia, 12 (80.0%) for carbapenems, and 18 (85.7%) for guideline-concordant antimicrobials. Figure 1 prints early-termination death counts 18 and 11, addressed separately in C006.
- **Consistency rule applicable:** Yes in principle: each mortality count/percentage must reconcile with its arm denominator. It cannot be applied to the ledger's alleged pairs because those pairs are not printed together as mortality data in the cited source.
- **Calculation or logical comparison reproduced:** The actual mortality sentence is coherent: `18/21=85.7%` and `14/15=93.3%`. The ledger calculations `11/21=52.4%`, `10/21=47.6%`, `15/15=100%`, and `12/15=80%` are arithmetically correct diagnostics but do not reproduce a directly printed mortality pairing.
- **Necessary inputs available / exact missing inputs or definitions:** Actual narrative counts, percentages, and arm sizes are available. No directly printed source sentence pairing 11 deaths with 47.6% or 15 deaths with 80.0% was found; provenance for those assembled pairs is missing.
- **Source-grounded alternative interpretation:** The candidate appears to combine Figure-1 death count 11 with unrelated Table-2 percentages/counts and a page-shifted narrative citation. The distinct 14-versus-11 death-count question remains recorded under C006.
- **Direct observation versus inferred explanation:** Direct observation is a coherent p. 41 mortality sentence and the absence of the alleged p. 42 statement. Cross-row/figure assembly as the cause is inferred.
- **Exact remaining human question:** Is there any supplied or original analysis output that actually reports the ledger's mortality pairs, or should C014's evidence statement be repaired while preserving the separately observed C006 narrative-versus-flow count difference?

## Completion summary

- Stable IDs rechecked: C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014 (14/14).
- Direct-source comparisons reproduced without a ledger value/location repair: C001, C006, C007, C008, C010, C011, C012, C013.
- Ledger/source repair facts recorded: C002, C003, C004, C005, C009, C014.
- No stable ID was deleted, renumbered, merged, suppressed, or adjudicated.
- General limitation: No participant-level data, original statistical output, protocol amendment archive beyond the supplied PDFs, or site-activation chronology was supplied. Those absences are retained as exact human questions rather than resolved by inference.
