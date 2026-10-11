# Quantitative Quality-Control Consistency Review

## Pending Human Adjudication

Every observation in this report is **Pending Human Adjudication**. This is a quantitative reporting quality-control review, not a validity finding, correction, severity rating, or conclusion about the study.

## Executive Quality-Control Summary

Complete source coverage and two independent statistical passes registered **14** stable candidate records (C001-C014). Eight source comparisons were directly reproduced (C001, C006-C008, and C010-C013). Six retained IDs have direct-source repair or nonreproduction facts (C002-C005, C009, and C014); they are included for traceability and human review, not presented as reproduced paper inconsistencies. Small preventable reporting defects can matter if confirmed because values or labels may be copied during downstream evidence extraction; this report does not claim propagation, harm, or a changed conclusion.

## Package and Reused-Evidence Provenance

The package contains five direct PDFs: DOC-001 main article (12 pages), DOC-002 supplement 1/protocol and SAP material (72), DOC-003 supplement 2/results material (54), DOC-004 collaborator list (28), and DOC-005 data-sharing material (1): **167 source units** total. Their identities and SHA-256 values are recorded in [source inventory](<review_1_5_1/source_inventory.md>) and [source hashes](<review_1_5_1/source_hashes_before.sha256>).

Reusable source-linked assets covered DOC-001 pp. 1-12 and DOC-003 p. 1 plus pp. 6-53 (61 units). The remaining 106 units were freshly mapped from direct sources. OCR and native text were locators and transcription aids; direct PDFs were the authority for candidate recheck. See [reused-evidence inventory](<review_1_5_1/evidence_asset_inventory.md>) and [reused-asset hashes](<review_1_5_1/reused_artifact_hashes_before.sha256>).

## Scope, Complete Coverage, and Exclusions

All five direct-source rows are complete: 167/167 mapped units, with reusable plus fresh-required units partitioning each source. The full accounting is in [source coverage](<review_1_5_1/source_coverage.md>) and the unit/stage partition is in [coverage manifest](<review_1_5_1/coverage_manifest.md>). The review covered numeric, denominator, statistical, cross-document, measure/label/scale, and rate/count relationships. It did not perform a clinical, raw-data, misconduct, or external-literature audit.

Coherent finite-precision P-value displays were not candidates. In particular, `P<.001`, `P=<.001`, and `P<.0001` were recorded where relevant as noncandidate display conventions; no card is based on a display-zero P value.

## Quantitative and Statistical Relationship Coverage

The quantitative inventory contains N001-N125, and the inferential-statistical inventory contains S001-S051. Numeric and cross-source checks covered the complete mapped scope. Statistical pass 1 and independently staffed statistical pass 2 each completed S001-S051; pass 2 made no append proposal. See [numeric relationships](<review_1_5_1/relationships/numeric_relationship_inventory.md>), [statistical relationships](<review_1_5_1/statistics/relationship_inventory.md>), [numeric checks](<review_1_5_1/checkers/numeric_consistency.md>), [cross-source checks](<review_1_5_1/checkers/cross_source_consistency.md>), [statistical pass 1](<review_1_5_1/checkers/statistical_pass_1.md>), and [statistical pass 2](<review_1_5_1/checkers/statistical_pass_2.md>).

## Candidate Index

| ID | Category | Recheck state | Short description |
|---|---|---|---|
| C001 | Cross-document numeric inconsistency | Reproduced | Day-15 responder numerator differs across Table 2 and narrative. |
| C002 | Measure, label, or scale inconsistency | Original comparator not reproduced | Protocol/report dose directly agree at 100 micrograms. |
| C003 | Measure, label, or scale inconsistency | Original comparator not reproduced | Directly inspected responder cutoffs agree at 1.4 points. |
| C004 | Measure, label, or scale inconsistency | Original comparator not reproduced | Entry threshold is 5000; 8000 is a separate reversal rule. |
| C005 | Denominator, proportion, or total inconsistency | Original comparator not reproduced | Direct protocol value is 117 per arm, with rounding rule absent. |
| C006 | Cross-document numeric inconsistency | Reproduced, conditional | Narrative and flow death counts need time-window reconciliation. |
| C007 | Statistical reporting inconsistency | Reproduced | APACHE II P value is incompatible with displayed t-test inputs. |
| C008 | Denominator, proportion, or total inconsistency | Reproduced | Figure child counts exceed their parent by one. |
| C009 | Cross-document numeric inconsistency | Original comparator not reproduced | Repaired values are 24, 31, and 33 sites with undefined milestones. |
| C010 | Measure, label, or scale inconsistency | Reproduced | RR label conflicts with counts and identical nearby HR. |
| C011 | Statistical reporting inconsistency | Reproduced | SII OR does not reconcile with counts and interval scale. |
| C012 | Cross-document numeric inconsistency | Reproduced | Six interaction rows repeat under different outcome captions. |
| C013 | Statistical reporting inconsistency | Reproduced | Interaction estimate lies outside its printed interval. |
| C014 | Numeric or arithmetic inconsistency | Original comparator not reproduced | Alleged mortality pairs are absent; actual pairs reconcile. |

## Candidate Evidence Cards

## C001 — Day-15 SOFA responder numerator differs between Table 2 and narrative

**Candidate statement:** Pending Human Adjudication. The matched day-15 responder occurrence prints 52/131 in Table 2 and 51/131 in the narrative.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [DOC-001 Table 2, PDF p. 6](<../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6>); [DOC-001 Results narrative, PDF p. 7](<../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=7>).

**Source evidence:** Table 2 prints precision immunotherapy 52/131 (39.7%) versus placebo 34/145 (23.4%); the narrative prints 51 of 131 (39.7%) versus 34 of 145 (23.4%) for the same endpoint.

**Reported-versus-comparator:** 52/131 versus 51/131, with the same displayed 39.7% and placebo comparator.

**Reasoning procedure:** Compare matched arm, endpoint, denominator, and percentage occurrences; allow only stated percentage rounding.

**Calculation:** 52/131 = 39.6947% (39.7% rounded); 51/131 = 38.9313% (38.9% rounded). Table-2 counts yield crude OR (52x111)/(79x34) = 2.15.

**Alternative source-grounded interpretations:** A table or narrative transcription error is possible; an undocumented analysis-set distinction is possible but both locations print denominator 131.

**Mechanical evidence recheck:** Reproduced: cited locations, printed values, comparator, and arithmetic were found. Participant-level listings and any undocumented analysis-set definition are unavailable.

**Quality-control relevance:** Binary-outcome counts and percentages are reusable extraction inputs.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy the wrong precision-arm responder count or percentage; no propagation is asserted.

**Human verification steps:** Check the original endpoint listing and determine whether 51 or 52 is authoritative, then harmonize matched outputs if needed.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Protocol and report IFN-gamma dose comparison

**Candidate statement:** Pending Human Adjudication. Retained ID with a direct-source repair: the alleged 20-microgram protocol comparator was not reproduced.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [DOC-002 protocol, PDF p. 6](<../joi250116supp1_prod_1771885794.26255.pdf#page=6>); [DOC-001 regimen, PDF p. 2](<../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=2>).

**Source evidence:** Direct protocol rendering prints sc rhIFNgamma 100 micrograms once every other day; the report prints 100 micrograms every 48 hours for 15 days.

**Reported-versus-comparator:** Directly printed 100 micrograms versus 100 micrograms, not the prior 100-versus-20 comparison.

**Reasoning procedure:** Match intervention, route, frequency, and duration before comparing dose definitions.

**Calculation:** 100/100 = 1.

**Alternative source-grounded interpretations:** The 20-microgram locator transcription may reflect font encoding; an unsupplied approved protocol version remains unavailable.

**Mechanical evidence recheck:** Original comparator not reproduced. Both cited direct-source dose statements were found and agree; no supplied page printed 20 micrograms.

**Quality-control relevance:** Dose is a quantitative intervention-characterization field.

**Potential downstream evidence impact:** If confirmed as a workflow-record repair, it prevents copying an unsupported dose discrepancy; no downstream propagation is asserted.

**Human verification steps:** Check any approved protocol amendment outside the supplied package and repair the ledger/mapping if none states 20 micrograms.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Primary responder cutoff comparison

**Candidate statement:** Pending Human Adjudication. Retained ID with a direct-source repair: the alleged 1.5-point binary cutoff was not reproduced.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [DOC-002 protocol, PDF p. 7](<../joi250116supp1_prod_1771885794.26255.pdf#page=7>); [DOC-001 report, PDF p. 1](<../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=1>); [DOC-002 SAP, PDF p. 66](<../joi250116supp1_prod_1771885794.26255.pdf#page=66>).

**Source evidence:** Direct protocol, report, and SAP occurrences print a 1.4-point responder cutoff; SAP defines >1.4 as achievement.

**Reported-versus-comparator:** 1.4 versus 1.4 in matched supplied sources, not 1.5 versus 1.4.

**Reasoning procedure:** Trace the binary cutoff across matched endpoint definitions and distinguish it from a planning mean difference.

**Calculation:** 1.4 - 1.4 = 0.

**Alternative source-grounded interpretations:** The 1.5 value may be derivative-text recognition error; an unsupplied protocol version may differ.

**Mechanical evidence recheck:** Original comparator not reproduced. Locations were found and all directly inspected binary-cutoff occurrences agree at 1.4.

**Quality-control relevance:** The cutoff determines endpoint classification.

**Potential downstream evidence impact:** If confirmed as a workflow-record repair, it prevents copying an unsupported cutoff discrepancy; no propagation is asserted.

**Human verification steps:** Locate any approved unsupplied version and otherwise align source mapping to the printed 1.4-point cutoff.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Immunoparalysis entry-classification threshold comparison

**Candidate statement:** Pending Human Adjudication. Retained ID with a direct-source repair: entry sources agree at 5000, while 8000 belongs to a separately named reversal endpoint.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [DOC-002 protocol, PDF p. 9](<../joi250116supp1_prod_1771885794.26255.pdf#page=9>); [DOC-003 eMethods, PDF p. 13](<../joi250116supp2_prod_1771885794.27755.pdf#page=13>); [DOC-002 SAP reversal definition, PDF p. 69](<../joi250116supp1_prod_1771885794.26255.pdf#page=69>).

**Source evidence:** Entry classification is ferritin at or below 4420 ng/mL plus HLA-DR below 5000 molecules/monocyte. SAP p. 69 prints restoration above 8000 for day-15 reversal.

**Reported-versus-comparator:** Entry threshold 5000 versus separately defined reversal threshold 8000.

**Reasoning procedure:** Compare only matched definition names; do not treat entry and reversal thresholds as identical quantities.

**Calculation:** Matched entry sources agree at 5000; no 8000-versus-5000 entry comparison is present.

**Alternative source-grounded interpretations:** The prior record may have transferred the reversal value into entry classification; an unsupplied entry definition is unavailable.

**Mechanical evidence recheck:** Original comparator not reproduced. Direct entry-classification text and the distinct reversal definition were found.

**Quality-control relevance:** The threshold defines immune-state membership.

**Potential downstream evidence impact:** If confirmed as a workflow-record repair, it prevents copying an unsupported entry-threshold discrepancy; no propagation is asserted.

**Human verification steps:** Distinguish entry from reversal in source mapping and check whether an unsupplied approved entry definition uses 8000.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Protocol sample-size, dropout, and total-target arithmetic

**Candidate statement:** Pending Human Adjudication. Retained ID with repaired direct inputs: protocol prints 117 per arm, about 15% dropout, and total randomization 280.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [DOC-002 protocol, PDF p. 25](<../joi250116supp1_prod_1771885794.26255.pdf#page=25>) and [PDF p. 26](<../joi250116supp1_prod_1771885794.26255.pdf#page=26>).

**Source evidence:** The source does not print the prior 112-per-arm premise; it prints 117 patients per arm, about 15% dropout, and N=280.

**Reported-versus-comparator:** Required analyzable total 234 versus planned randomization 280 under an approximate attrition statement.

**Reasoning procedure:** Treat the calculation as a diagnostic and require a stated rounding/inflation rule before declaring an incompatibility.

**Calculation:** 2x117 = 234; 234/(1-.15) = 275.29 (conventionally at least 276); 1-234/280 = 16.43%.

**Alternative source-grounded interpretations:** Conservative rounding to 280, approximately 16.4% attrition, or unstated block/operational inflation could explain the residual.

**Mechanical evidence recheck:** Original comparator not reproduced. Direct 117-per-arm input was found; the source omits the convention taking approximately 276 to 280.

**Quality-control relevance:** Planning sample-size and attrition assumptions are commonly extracted.

**Potential downstream evidence impact:** If confirmed, it could affect extraction of planning assumptions and target sample size; no propagation is asserted.

**Human verification steps:** Retrieve the nQuery rounding, randomization-block, or other inflation rule and repair the 112-per-arm premise.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Historical-trial narrative and flow diagram death counts

**Candidate statement:** Pending Human Adjudication. The personalized-immunotherapy death count is 14 in the narrative and 11 in the flow figure, conditional on a matched time window.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [DOC-002 narrative, PDF p. 41](<../joi250116supp1_prod_1771885794.26255.pdf#page=41>); [DOC-002 Figure 1, PDF p. 50](<../joi250116supp1_prod_1771885794.26255.pdf#page=50>).

**Source evidence:** Narrative reports 18/21 (85.7%) placebo and 14/15 (93.3%) personalized-immunotherapy deaths at 28 days; Figure 1 reports early termination because of death n=18 and n=11.

**Reported-versus-comparator:** Personalized arm 14 versus 11; placebo count 18 agrees.

**Reasoning procedure:** Compare arm-specific death counts only if the flow's early-termination window matches narrative 28-day mortality.

**Calculation:** 14/15 = 93.3%; 11/15 = 73.3%; difference = 3 people.

**Alternative source-grounded interpretations:** Figure 1 may represent a shorter intervention-termination window; its time window is not stated.

**Mechanical evidence recheck:** Reproduced direct counts and arithmetic; the necessary flow-figure time-window definition is missing.

**Quality-control relevance:** Mortality counts and follow-up definitions are outcome inputs.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy a different historical-arm death count or time window; no propagation is asserted.

**Human verification steps:** Establish Figure 1's time window and reconcile counts only if it covers the same 28-day period.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — APACHE II Table 2 P value versus displayed t-test inputs

**Candidate statement:** Pending Human Adjudication. The printed P=.376 is not compatible with conventional two-group calculations from the displayed Student t-test inputs.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [DOC-002 Table 2, PDF p. 48](<../joi250116supp1_prod_1771885794.26255.pdf#page=48>).

**Source evidence:** Placebo n=21, 18.2 +/- 8.7; personalized immunotherapy n=15, 30.5 +/- 9.4; P=.376; footnote identifies Student t test.

**Reported-versus-comparator:** Printed P=.376 versus diagnostics from the displayed group summaries and named test.

**Reasoning procedure:** Apply pooled and Welch two-sample diagnostics to displayed means, SDs, and group sizes; do not infer a transformed or different analysis.

**Calculation:** Pooled SD about 9.00, SE about 3.04, t about 4.05 (34 df; two-sided P about .0003); Welch t about 3.99 (about 29 df; P about .0004).

**Alternative source-grounded interpretations:** P may be transposed, an input may be inaccurate, or an unreported transformed/different dataset analysis may have been used.

**Mechanical evidence recheck:** Reproduced the row, test label, and diagnostic. Raw observations and implementation details are unavailable.

**Quality-control relevance:** This is a reported baseline comparison.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy an incompatible baseline P value; no propagation is asserted.

**Human verification steps:** Compare original analysis output, group summaries, and test specification; do not select a corrected component from this report.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — Figure 1 septic-shock classification children exceed their parent total

**Candidate statement:** Pending Human Adjudication. Displayed child classifications sum to 178 under a parent total of 177.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [DOC-002 Figure 1, PDF p. 50](<../joi250116supp1_prod_1771885794.26255.pdf#page=50>).

**Source evidence:** Parent septic shock =177; children MALS 44 (24.8%), immunoparalysis 2 (1.1%), intermediate 132 (74.0%).

**Reported-versus-comparator:** Parent 177 versus displayed child total 178.

**Reasoning procedure:** Treat displayed flow branches as a parent partition unless overlap or a different denominator is stated.

**Calculation:** 44+2+132 = 178; percentages total 99.9% from rounding, but integer children exceed parent by one.

**Alternative source-grounded interpretations:** One count or parent total may be typographic, or an unstated overlap/unclassified case may exist.

**Mechanical evidence recheck:** Reproduced counts and arithmetic; no overlap or exception definition was printed.

**Quality-control relevance:** Classification totals determine denominators and proportions.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy an inconsistent classification total; no propagation is asserted.

**Human verification steps:** Check flow data and determine whether a count, parent total, overlap, or denominator label requires clarification.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C009 — ImmunoSep study-site totals across report, protocol, and SAP

**Candidate statement:** Pending Human Adjudication. Retained ID with repaired direct-source values: 24, 31, and 33 sites require milestone definitions.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [DOC-001 report, PDF p. 2](<../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=2>); [DOC-002 protocol, PDF p. 10](<../joi250116supp1_prod_1771885794.26255.pdf#page=10>); [DOC-002 SAP, PDF p. 65](<../joi250116supp1_prod_1771885794.26255.pdf#page=65>); [PDF p. 67](<../joi250116supp1_prod_1771885794.26255.pdf#page=67>).

**Source evidence:** Protocol and SAP design print 24 sites, SAP model text says 31 participated, and the report prints 33 sites.

**Reported-versus-comparator:** Repaired direct values 24, 31, and 33; prior 28 and report p.1 citation were not reproduced.

**Reasoning procedure:** Site totals need a stated planned, activated, participating, enrolling, or final milestone before identity comparison.

**Calculation:** The three integers cannot be reconciled by rounding; protocol and SAP design share 24.

**Alternative source-grounded interpretations:** They may describe different operational milestones, but chronology and definitions are absent.

**Mechanical evidence recheck:** Original comparator not reproduced. Direct values and locations were repaired; milestone identity remains unavailable.

**Quality-control relevance:** Site count is a trial-scale descriptor.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy the wrong site-count milestone; no propagation is asserted.

**Human verification steps:** Retrieve site chronology and define each count before identifying a final participating/enrolling total.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C010 — Figure 2C relative-risk label versus displayed association

**Candidate statement:** Pending Human Adjudication. Figure 2C labels 2.82 (1.58-5.14) as RR although displayed counts give a crude RR of 1.61 and the same value/CI appears as an HR in Figure 3.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [DOC-002 Figure 2C, PDF p. 51](<../joi250116supp1_prod_1771885794.26255.pdf#page=51>); [DOC-002 Figure 3, PDF p. 52](<../joi250116supp1_prod_1771885794.26255.pdf#page=52>).

**Source evidence:** Figure 2C shows 69/103 deaths versus 37/89 and labels RR_death 2.82 (1.58-5.14), P<.0001; Figure 3 prints HR 2.82 (1.58-5.14).

**Reported-versus-comparator:** RR label/value 2.82 versus crude RR 1.61 and identical nearby HR 2.82.

**Reasoning procedure:** Compute crude risk and odds ratios from displayed counts; compare measure labels without assuming an unreported model.

**Calculation:** (69/103)/(37/89) = 1.61; (69x52)/(34x37) = 2.85, compatible with 2.82.

**Alternative source-grounded interpretations:** The value may be HR, OR, another model output, or paired with count rows from a different analysis; source does not resolve it. P<.0001 is threshold notation and not this card's basis.

**Mechanical evidence recheck:** Reproduced counts, label, value/CI repetition, and diagnostics; model specification is missing.

**Quality-control relevance:** RR, OR, and HR are not interchangeable extraction measures.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy the wrong effect-measure label; no propagation is asserted.

**Human verification steps:** Identify the model producing 2.82 and correct or clarify the Figure 2C measure label/count relation.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C011 — eTable 10 SII day-15 OR versus counts, CI, and P value

**Candidate statement:** Pending Human Adjudication. Printed OR 1.194 does not reconcile with the count-derived crude OR and interval midpoint.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [DOC-003 eTable 10, PDF p. 22](<../joi250116supp2_prod_1771885794.27755.pdf#page=22>).

**Source evidence:** SII day-15 row prints 40/106 versus 29/122, OR 1.194 (1.09-3.45), P=.030.

**Reported-versus-comparator:** Printed 1.194 versus count-derived OR about 1.94 and CI log midpoint about 1.94.

**Reasoning procedure:** Use counts and CI midpoint as diagnostics; do not treat P=.030 as proof of an intended point estimate because test details are absent.

**Calculation:** (40x93)/(66x29) = 1.94; sqrt(1.09x3.45) about 1.94.

**Alternative source-grounded interpretations:** Decimal/transcription error or a differently defined analysis pairing may explain the row.

**Mechanical evidence recheck:** Reproduced direct row values and diagnostics; exact test/model details are unavailable.

**Quality-control relevance:** This is a stratum-specific effect estimate and interval.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy an inconsistent stratum-specific effect estimate; no propagation is asserted.

**Human verification steps:** Check original output and determine whether point estimate, counts, CI, or analysis definition requires repair.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C012 — eFigure 8B repeats eFigure 7B interaction results under a different outcome caption

**Candidate statement:** Pending Human Adjudication. Six OR/CI/P rows repeat exactly under primary-endpoint and 28-day-mortality captions.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [DOC-003 eFigure 7B, PDF p. 51](<../joi250116supp2_prod_1771885794.27755.pdf#page=51>); [DOC-003 eFigure 8B, PDF p. 52](<../joi250116supp2_prod_1771885794.27755.pdf#page=52>).

**Source evidence:** eFigure 7B prints APACHE 0.47 and interaction 1.85; CCI 0.22 and interaction 5.79; SOFA 0.56 and interaction 3.08, with their CIs/P values. eFigure 8B repeats all six rows exactly under a 28-day mortality caption; A panels have different event/total data.

**Reported-versus-comparator:** Complete six-row primary-endpoint output versus identical six-row 28-day-mortality output.

**Reasoning procedure:** Compare captions, all printed values, and A-panel data; exact repetition cannot be explained by rounding without an asserted shared output.

**Calculation:** Six point estimates, intervals, and P values are identical across the two panels.

**Alternative source-grounded interpretations:** A copied panel or incorrect caption is possible; source-production files are unavailable and no specific mechanism is established.

**Mechanical evidence recheck:** Reproduced all six direct comparisons and distinct outcome labels; no source statement explains a shared output.

**Quality-control relevance:** Subgroup interaction outputs are outcome-specific quantitative evidence.

**Potential downstream evidence impact:** If confirmed, a data extractor could assign a subgroup interaction to the wrong outcome; no propagation is asserted.

**Human verification steps:** Compare figure-production output and determine whether the interaction rows or caption/outcome label requires correction.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C013 — eFigure 9B APACHE interaction point estimate outside its CI

**Candidate statement:** Pending Human Adjudication. The printed OR 0.11 lies below its printed 95% CI lower endpoint 0.36.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [DOC-003 eFigure 9B, PDF p. 53](<../joi250116supp2_prod_1771885794.27755.pdf#page=53>).

**Source evidence:** APACHE II >=25 interaction row prints OR 0.11, 95% CI 0.36-3.42, P=.86.

**Reported-versus-comparator:** Point estimate 0.11 versus interval lower endpoint 0.36.

**Reasoning procedure:** Require a printed confidence interval on the same ratio scale to contain its point estimate.

**Calculation:** 0.11 < 0.36; rounding cannot span the difference.

**Alternative source-grounded interpretations:** A point estimate, endpoint, or row alignment may be wrong; source does not identify which component.

**Mechanical evidence recheck:** Reproduced the row and logical noncontainment; original model output is unavailable.

**Quality-control relevance:** Interaction estimates and intervals are quantitative subgroup outputs.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy an incompatible interaction estimate and interval; no propagation is asserted.

**Human verification steps:** Check original model output and establish which printed component matches it; do not infer a replacement value here.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C014 — Historical mortality-pair registration

**Candidate statement:** Pending Human Adjudication. Retained ID with direct-source repair: no supplied source prints the registered mortality count/percentage pairs.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [DOC-002 actual mortality sentence, PDF p. 41](<../joi250116supp1_prod_1771885794.26255.pdf#page=41>); [Discussion, PDF p. 42](<../joi250116supp1_prod_1771885794.26255.pdf#page=42>); [Table 2, PDF p. 48](<../joi250116supp1_prod_1771885794.26255.pdf#page=48>); [Figure 1, PDF p. 50](<../joi250116supp1_prod_1771885794.26255.pdf#page=50>).

**Source evidence:** Actual p.41 pairs are 18/21 (85.7%) and 14/15 (93.3%) and reconcile. The alleged p.42 pairs are absent; p.48 values 10 (47.6%) and 12 (80.0%) are unrelated rows.

**Reported-versus-comparator:** Unsupported assembled alleged pairs versus directly printed coherent p.41 mortality pairs.

**Reasoning procedure:** Apply count/percentage arithmetic only to a matched printed mortality statement; do not treat unrelated rows as a comparator.

**Calculation:** 18/21 = 85.7%; 14/15 = 93.3%.

**Alternative source-grounded interpretations:** The prior record may have combined a Figure 1 count with unrelated Table 2 values and a shifted page citation; an outside source is unavailable.

**Mechanical evidence recheck:** Original comparator not reproduced. Direct source confirms actual mortality pairs and absence of alleged pairs; C006 remains a separate narrative-versus-flow question.

**Quality-control relevance:** Arm-specific mortality pairs are reusable outcome data.

**Potential downstream evidence impact:** If confirmed as a workflow-record repair, it prevents reuse of an unsupported assembled pair; no propagation is asserted.

**Human verification steps:** Locate any original output actually containing the alleged pairs; otherwise repair this card's evidence record while preserving C006 separately.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If a candidate is confirmed, downstream users could copy a count, denominator, site descriptor, effect-measure label, interval, or outcome caption into evidence tables, systematic reviews, meta-analyses, or guideline evidence summaries. The package does not establish that any such copying occurred, that a conclusion changed, or that harm resulted.

## Limitations and Missing Definitions

DOC-002 embedded fonts made native/layout extraction unreliable, so rendered direct-page inspection was authoritative. No participant-level data, original model outputs, figure-production files, site chronology, randomization-block rule, complete amendment archive, or external source version was supplied. C006 lacks the flow time window; C009 lacks milestone definitions; C007 and C010-C013 lack source material identifying which printed component should change. The full record is in [limitations](<review_1_5_1/limitations.md>).

## Human Adjudication Checklist

1. Confirm each cited source location against the direct PDF.
2. Determine whether a missing definition, version, time window, or original output resolves the comparison.
3. Record validity, importance, action, initials, and notes in each card without assigning an AI disposition.
4. Keep C002-C005, C009, and C014 visibly marked as nonreproduced original comparators if their record is repaired.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

Source and reusable-artifact provenance are retained in the versioned hash ledgers cited above. The agent execution record is [agent execution manifest](<review_1_5_1/agent_execution_manifest.md>): coordinator gpt-5.6-sol/high; reuse, mapping, checking, registration, and report roles as documented; two distinct fresh gpt-5.6-terra/high statistical passes; and gpt-5.6-sol/high recheck and quality audit.

### Reproducibility Performance

- **Target basis:** Five supplied PDFs contain 167 pages; reusable page-level extraction appears available for the 12-page main article and much of one 54-page support document, while three support PDFs and uncovered pages require fresh native/layout mapping. The package exceeds the 102-page calibration package and includes a long SAP plus cross-document and table review, so a bounded 55-80 minute planning range is selected.
- **Total source units:** 167
- **Fresh-source units:** 106
- **Target elapsed minutes:** 55-80
- **Started UTC:** 2026-09-03T03:48:12Z
- **Finished UTC:** 2026-09-03T06:30:28Z
- **Observed elapsed minutes:** 162.3
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** 106 pages required fresh direct-source mapping; DOC-002 custom font encoding required direct high-resolution rendering; mechanical recheck identified six source-transcription/citation repair sets; canonical artifacts required synchronization after repair

### Token-Usage and Cost Metadata

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Known total tokens | Known token cost (USD) | Status |
|---|---:|---:|---|
| gpt-5.6-sol | 0 | 0.000000 | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| gpt-5.6-terra | 0 | 0.000000 | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |

All amounts are token-only API-equivalent estimates under the dated pricing snapshot, not invoices; cached/cache-write inputs and reasoning output are subsets and are not added again. Response-level runtime usage was unavailable for every manifested agent. See [token-usage summary](<review_1_5_1/token_usage_summary.md>) for versioned per-agent and per-model accounting detail.
