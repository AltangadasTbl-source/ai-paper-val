# Cross-Source Consistency Check

## Scope, method, and coverage

This check used the current workflow-1.5.1 relationship inventories and their
source-linked mapping records only: all `N001-N125` numeric/reporting records
and all `S001-S051` inferential-statistical records.  The direct PDFs were the
authority; current native/layout/OCR/render derivatives were used only as
locators.  No previous candidate, checker, verifier, quality, or final-report
artifact was used as scientific input.

Matching required the same trial/population, analysis set, outcome, time
window, contrast, measure, model, reference group, and displayed precision.
Planned protocol/SAP statements were not numerically equated to observed trial
results unless the current materials supplied a matched identity.  The source
inventory contains no supplied workbook, CSV, or other structured dataset.

| Coverage lane | Relationships checked | Result |
|---|---:|---|
| Main article: abstract, narrative, Figure 1-2, Tables 1-3, captions and footnotes | N001-N042; S001-S012 | Complete; matched observed outcomes and definitions compared with supplement occurrences. |
| Protocol, version 7.0, and SAP definitions | N043-N101; S013-S036 | Complete; planned/administrative definitions compared only after version/context distinction. |
| Historical protocol results, tables, and figures | N061-N083; S018-S025 | Complete; identified as a distinct earlier 240-patient/36-randomized study, not the 276-patient current trial. |
| eMethods, eTables 1-15, eFigures 1-9 | N102-N125; S037-S051 | Complete; compared to matching main-paper outcomes, captions, and analysis populations. |
| DOC-004 collaborator roster and DOC-005 data-sharing statement | no applicable N/S IDs | Complete; no result-bearing matched comparator. |

The relationship inventory is complete at 125 numeric/reporting and 51
statistical records (176 total).  The candidate proposals below are uncapped
checker proposals only; they have no stable candidate ID and remain pending
human adjudication.

## Matched-result comparison record

| Matched relationship(s) | Locations compared | Result and rationale |
|---|---|---|
| Primary day-9 responder outcome: 46/131 vs 26/145; OR/risk difference | Main PDF pp. 1, 6-7; Supplement 2 p. 21-22 / eTables 9-10; N028, S001-S003, S037-S039 | PASS. Same randomized population, day-2-to-9 definition, contrast, and measure.  Abstract/Table 2 give OR 2.48 (1.42-4.32), P=.002; eTable 9 gives 2.48 (1.42-4.31), P=.001.  The small CI/P display difference accompanies a differently presented logistic table and does not by itself establish a contradiction. |
| Day-15 SOFA responder outcome | Main PDF pp. 6-7; Supplement 2 p. 22 / eTable 10; N031, S005, S040 | PROPOSAL 1 below.  Main Table 2 and its narrative name the same all-randomized, day-2-to-15 responder analysis but disagree on the precision-arm numerator.  eTable 10 is stratified and therefore not a substitute for either overall occurrence. |
| 28- and 90-day mortality | Main PDF pp. 6-7; Supplement 2 pp. 47-48 / eFigures 3-4; N029-N030, S003-S004, S042-S043 | PASS.  Main binary ORs/risk differences and supplement time-to-event HRs are different effect measures/models and are not expected to agree numerically.  Risk sets and event totals are compatible with the named randomized arms. |
| SIDF reversal | Main PDF pp. 6-7; Supplement 2 p. 50 / eFigure 6; N032, S006, S045 | PASS WITH PRECISION DIFFERENCE.  Counts and contrast are 46/59 vs 32/66.  Table 2 prints P=.001 and narrative/eFigure print P<.001.  A finite-precision value below .001 can round to .001, so this is not a qualifying difference. `DISPLAY_ZERO_NOT_CANDIDATE` is not applicable: no P=0 display is involved. |
| Day-15 infection disposition | Main PDF pp. 6-7; Supplement 2 p. 49 / eFigure 5; N033, S007, S044 | PASS.  Four category percentages and worse-outcome OR are the same randomized groups, time point, direction, and ordinal measure (main P=.02; eFigure P=.018 is compatible displayed precision). |
| Primary endpoint and 28-/90-day subgroup displays | Main PDF p. 8; Supplement 2 pp. 51-53 / eFigures 7-9; N022-N024, S010, S047-S051 | PROPOSALS 2 and 3 below.  Subgroup event/total rows were matched only to the stated outcome captions; eFigure 8B repeats eFigure 7B values despite a distinct mortality caption, and eFigure 9B contains a point estimate outside its printed CI. |
| Flow and safety totals | Main PDF pp. 3, 8; Supplement 2 pp. 6-8, 25-43; N003-N006, N036-N039, N102, N113-N114 | PASS.  Main 131+145=276 and safety 245/276 (88.8%) match appropriately corresponding supplement safety-set totals.  SOC rows count people whereas preferred-term rows can count events; no rate/count conflation was found. |
| Immune classification, treatment quantity, responder cutoff, and sample-size premise | Main PDF pp. 1-5; Protocol PDF pp. 6, 7, 9, 24-26; SAP PDF pp. 66-70; Supplement 2 pp. 3-4, 13, 50; N001-N002, N008, N043-N060, N084-N101, N103-N104, N122 | PASS AFTER DIRECT-SOURCE REPAIR.  Protocol p.6 and main report both print 100-µg rhIFN-gamma; direct protocol endpoint/power pages print the same 1.4-point cutoff as the report/SAP; and entry classification is ferritin at or below 4420 plus HLA-DR below 5000.  The 8000 value is a distinct day-15 reversal threshold, not an entry criterion.  The protocol sample-size premise is 117 analyzable patients per arm, about 15% dropout, and total 280; it is not a 112-per-arm premise. |
| Site counts | Main PDF p. 2 (33 sites); Protocol p. 10 (24 ImmunoSep sites); SAP pp. 65, 67 (24 and 31 sites); N002, N047, N084, N090 | PROPOSAL 4 below.  The directly reproduced site-count chain is 24 protocol / 24 SAP-design / 31 SAP participating / 33 final report.  The protocol p.9 mention of 14 sites concerns the different PROVIDE trial and is not a comparator. |
| Historical protocol's 240-person classification/36-randomized stage | Protocol PDF pp. 38-53; N061-N083, S018-S025 | NONCANDIDATE DISTINCT STUDY POPULATION.  Its 240 screened/classified and 36 randomized participants, figures, and outcomes are not the current 276-person trial. |
| Historical protocol trial mortality wording and flow | Protocol PDF p. 41 and Figure 1 p. 50; N066, N073, N078 | NONREPRODUCED MORTALITY-PAIRING CLAIM; SEPARATE FLOW COMPARATOR.  Direct p.41 narrative is coherent: 18/21=85.7% placebo and 14/15=93.3% personalized immunotherapy.  No p.42 mortality sentence pairing 11 with 47.6% or 15 with 80.0% was found.  Figure 1's personalized-arm early-termination death count of 11 is a separate, time-window-undefined comparator to the p.41 28-day count of 14. |

## Qualifying candidate proposals

### Proposal 1 — Same day-15 endpoint has two precision-arm numerators

- **Category:** Cross-document numeric inconsistency.
- **Exact linked locations:** [main article — PDF p. 6](<../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6>), Table 2; [main article — PDF p. 7](<../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=7>), Results narrative.
- **Printed values:** Table 2 prints day-15 response as `52/131 (39.7%)` precision versus `34/145 (23.4%)` placebo.  The adjacent narrative prints `51/131 (39.7%)` versus `34/145 (23.4%)` for the same day-15 endpoint and P=.004.
- **Comparison logic:** Both occurrences name the all-randomized treatment groups, >=1.4-point decrease in mean SOFA through day 15, and the same placebo comparator.  At denominator 131, 52/131=39.7% to one decimal whereas 51/131=38.9%; therefore 51/131 cannot produce the printed 39.7%.
- **Supported alternatives:** The narrative numerator may be a transcription error, or Table 2 may contain an erroneous count.  The supplied overall eTable does not give a directly matched all-arm total and cannot resolve the source occurrence.
- **Human verification steps:** Inspect the production source/table data for the day-15 all-randomized responder indicator; establish whether the authoritative numerator is 51 or 52; reconcile the percentage, risk difference, OR, CI, and any analysis output to that numerator.

### Proposal 2 — eFigure 8B repeats primary-endpoint interaction results under a 28-day mortality caption

- **Category:** Cross-document numeric inconsistency.
- **Exact linked locations:** [Supplement 2 — PDF p. 51](<../../../joi250116supp2_prod_1771885794.27755.pdf#page=51>), eFigure 7B (primary-endpoint interaction table); [Supplement 2 — PDF p. 52](<../../../joi250116supp2_prod_1771885794.27755.pdf#page=52>), eFigure 8B (captioned 28-day mortality interaction table).
- **Printed values:** eFigure 7B prints APACHE `0.47 (0.30-1.62), P=.70`, interaction `1.85 (0.66-5.19), P=.24`; CCI `0.22 (0.09-0.53), P=.001`, interaction `5.79 (2.34-15.05), P<.0001`; SOFA `0.56 (0.27-1.19), P=.13`, interaction `3.08 (1.37-6.96), P=.007`.  eFigure 8B prints the same six rows and values while its caption identifies 28-day mortality.
- **Comparison logic:** The captions specify distinct outcomes with distinct event/total rows on their respective A panels.  Exact duplication of the complete interaction table, including estimates, CIs, and P values, across those outcomes is inconsistent with the displayed outcome identity.
- **Supported alternatives:** The eFigure 8B table may have been copied from eFigure 7B, or its caption could be mislabeled.  The supplied figure does not identify which element is authoritative.
- **Human verification steps:** Re-run or recover the 28-day mortality subgroup interaction model; compare it to the eFigure 8B source table and caption; correct the outcome label or all six displayed rows as supported by the verified output.

### Proposal 3 — eFigure 9B APACHE interaction estimate is outside its own interval

- **Category:** Statistical reporting inconsistency.
- **Exact linked location:** [Supplement 2 — PDF p. 53](<../../../joi250116supp2_prod_1771885794.27755.pdf#page=53>), eFigure 9B, 90-day mortality interaction/model table.
- **Printed values:** APACHE interaction prints OR `0.11`, 95% CI `0.36-3.42`, P=.86.
- **Comparison logic:** For an odds ratio and its 95% CI presented on the same scale, the point estimate must lie within the interval.  `0.11 < 0.36`, so the printed estimate is not contained in the printed CI.
- **Supported alternatives:** The point estimate may be `1.11` rather than `0.11`, an interval endpoint may be wrong, or the row may be misaligned.  The source alone cannot determine the correct value.
- **Human verification steps:** Inspect the analysis output and original figure table for the APACHE interaction row; confirm the effect-measure scale and all three printed quantities before replacing any component.

### Proposal 4 — SAP contains incompatible site counts for the described phase-2 trial

- **Category:** Cross-document numeric inconsistency.
- **Exact linked locations:** [Protocol — PDF p. 10](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=10>), 24 ImmunoSep sites; [Protocol/SAP — PDF p. 65](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=65>), SAP design statement; [Protocol/SAP — PDF p. 67](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=67>), logistic-model site statement; comparator [main article — PDF p. 2](<../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=2>), 33-site final study description.
- **Printed values:** Protocol p.10 and SAP p.65 each say total `24 study sites`; SAP p.67 says `31 study sites participated`; main article p.2 describes `33 sites in 6 countries`.
- **Comparison logic:** The two SAP statements each describe the phase-2 ImmunoSep trial and provide different site totals.  They cannot both be the same site-count quantity without a specified distinction.
- **Supported alternatives:** Counts may refer to a protocol planning stage, participating/randomizing sites, or final activated sites.  The materials do not define those distinctions beside either SAP number.
- **Human verification steps:** Examine the SAP version history, site-activation log, and model site variable; label each number explicitly as planned, activated, participating, randomized, or final-report site count, or correct an unsupported number.

## Nonreproduced proposal withdrawn after direct-source repair

The earlier checker proposal alleging a historical-protocol mortality pairing of
`11/21 (47.6%)` and `15/15 (80.0%)` is **NONREPRODUCED AND WITHDRAWN AS A
PROPOSAL**.  Direct-source recheck found no such mortality statement on
[Protocol PDF p. 42](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=42>).
The directly printed p.41 mortality sentence is coherent: placebo `18/21
(85.7%)` and personalized immunotherapy `14/15 (93.3%)`.  Table 2 p.48
contains unrelated `10 (47.6%)` and `12 (80.0%)` treatment rows; it is not a
mortality comparator.  The distinct Figure-1 p.50 `n=11` early-termination
death count remains a separate flow-versus-28-day-mortality comparison with an
undefined figure time window; it is not restated here as the withdrawn pairing.

## Noncandidate observations and limitations

- `P=.001` versus `P<.001` for SIDF reversal is compatible with rounding/threshold display and is not a candidate.  No P=0 or p=0.000 display was registered as a candidate.
- The direct-source repair establishes agreement at 100 µg for rhIFN-gamma, 1.4 points for the responder cutoff, and 5000 for the entry HLA-DR threshold.  The separately labelled 8000 threshold is for day-15 reversal.  Protocol planning states 117 analyzable participants per arm, approximately 15% dropout, and total N=280; the unelaborated rounding/inflation from 276 to 280 is not a reproduced contradiction.
- Main-effect binary ORs and survival HRs, and all-arm results versus stratified/sensitivity results, were not compared as though they were the same measure or population.
- DOC-002 has font-encoded text; its mapped values were directly rendered-page confirmed by the mapping lane.  This checker relied on those current source-linked records and did not treat OCR as final authority.

## Completion counts

- Numeric/reporting relationships reviewed: 125/125.
- Inferential-statistical relationships reviewed for cross-location matching: 51/51.
- Distinct qualifying candidate proposals: 4.
- Noncandidate precision/definition differences and one withdrawn nonreproduced proposal recorded: 4 lanes.
- Limitation: no participant-level dataset or underlying analysis output was supplied, so the checker cannot resolve which of the competing printed alternatives is correct.
