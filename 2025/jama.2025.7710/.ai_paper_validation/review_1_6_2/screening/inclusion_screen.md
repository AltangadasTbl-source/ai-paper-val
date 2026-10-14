# Independent inclusion screen — initial stage

Runtime: `agent:/root/inclusion_initial`; fresh `qc162_inclusion_screener`, `gpt-6.1-sol`, high reasoning effort. Scope: all nine findings in the current-run canonical cross-source and statistical-pass-1 checker artifacts; the canonical numeric checker contains no finding IDs. The complete scope document, role contract and review-contract inclusion-screen section were read. Decisions use the supplied sources independently of checker judgments; no earlier review conclusions or external sources were consulted.

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-XS-001 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-XS-002 | cross_source_consistency_reviewer | initial | SCREENED_OUT | CONDITIONAL_OR_UNREPORTED | — |
| F-XS-003 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C002 |
| F-XS-004 | cross_source_consistency_reviewer | initial | SCREENED_OUT | NOT_REPRODUCED | — |
| F-XS-005 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C003 |
| F-ST1-001 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C002 |
| F-ST1-002 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-ST1-003 | statistics_pass_1 | initial | SCREENED_OUT | NOT_REPRODUCED | — |
| F-ST1-004 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C003 |

## One-sentence decision justifications

- **F-XS-001:** Include by **Route A, category 5**, because the SAP's separately specified prognostic-adjusted primary-outcome model has no identified result in the supplied reports despite the article stating that it was undertaken; consolidate with F-ST1-002 in group `prognostic_model`.
- **F-XS-002:** Screen out as `CONDITIONAL_OR_UNREPORTED` because the absent NNT is a derived summary of the already reported primary analysis, with no conflicting printed NNT, replaced outcome, or separately missing fitted analysis, and the supplied counts, risk difference, interval and RR leave the reported primary effect unambiguous.
- **F-XS-003:** Include by **Route A, category 5**, because the planned adjusted-P analysis for the ten key secondary components is replaced in the report by an explicit no-adjustment rule; consolidate with F-ST1-001 in group `component_multiplicity`.
- **F-XS-004:** Screen out as `NOT_REPRODUCED` because both plans explicitly say that the mortality boundary would be needed to justify recommending early stopping, while their separate composite-boundary paragraph specifies advice to the management committee and does not establish the independent stopping trigger asserted by the finding.
- **F-XS-005:** Include its prior-cesarean component by **Route B**, because any previous cesarean versus cesarean in the preceding pregnancy is an explicit subgroup-membership specification difference that can change the population attached to the primary-effect subgroup RRs and is not resolved by the immediate context; consolidate with F-ST1-004 in group `prior_cesarean_definition`, excluding the anomaly wording component as explained below.
- **F-ST1-001:** Include by **Route A, category 5**, because the ten-component key secondary multiplicity analysis required by both plans is absent under the article's explicit no-adjustment rule; consolidate with F-XS-003 in group `component_multiplicity`.
- **F-ST1-002:** Include by **Route A, category 5**, because the declared prognostic-adjusted primary analysis is distinct from the positively labeled cord-testing-indicator sensitivity models and has no supplied treatment-effect result; consolidate with F-XS-001 in group `prognostic_model`.
- **F-ST1-003:** Screen out as `NOT_REPRODUCED` because its proposed composite-versus-mortality stopping conflict does not remain after reading the plans' qualifying phrase that the mortality boundary would be needed to justify recommending early stopping.
- **F-ST1-004:** Include by **Route B**, because the protocol's any-prior-cesarean criterion differs from the reported preceding-pregnancy criterion in a prespecified subgroup analysis and can change the interpretation and extraction of RR 4.98 and RR 0.94 without an immediate source explanation of whether membership coincided; consolidate with F-XS-005 in group `prior_cesarean_definition`.

## Consolidated included issues and retained locations

Several INCLUDE rows retain distinct checker provenance but refer to one consolidated issue; the coordinator must assign the same stable ID to rows in each group. These group names are working references, not candidate IDs or adjudications.

### Group `prognostic_model` — F-XS-001 and F-ST1-002

**Qualifying route:** Route A, category 5. **Focus:** C, D. **Proposed domain:** `protocol_report`. **Proposed relationship:** `P_R`; all relationships `P_R`.

**PLAN locations:** [protocol p.20 §13.2](../../../joi250034supp1_prod_1750956984.09018.pdf#page=20); [SAP p.12 §3.2, lines 399–401](../../../joi250034supp2_prod_1750956984.11521.pdf#page=12); [SAP p.13 §3.9, lines 442–450](../../../joi250034supp2_prod_1750956984.11521.pdf#page=13); [SAP p.26 Table 12](../../../joi250034supp2_prod_1750956984.11521.pdf#page=26).

**REPORT locations:** [main p.3 Statistical Analysis](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=3); [main p.6 primary-result sensitivity paragraph](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=6); [main p.7 Table 3](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=7); [main p.8 Figure 2 and Table 4](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=8); [results supplement p.2 eTable 1, especially fifth/sixth rows and footnotes](../../../joi250034supp3_prod_1750956984.12018.pdf#page=2).

**Independent comparison:** SAP §3.9 specifies small-for-gestational-age status, preeclampsia, previous-pregnancy delivery method and postnatal fetal anomaly, with multiple birth added if a GEE cannot be fitted; Table 12 separately lays out the multivariable model and robust-Poisson footnote. Main p.3 states that secondary primary-outcome analysis with prognostic adjustment using robust modified Poisson regression “was undertaken.” The RR 1.02 (0.75–1.37) belongs to the main primary GEE result; RR 0.98 (0.73–1.31) and RR 0.97 (0.73–1.30) are explicitly labeled as cord-testing-indicator GLM sensitivities in eTable 1. The remaining supplied report displays contain site, subgroup, tertiary and safety results, with no separately identified prognostic-adjusted primary treatment RR/CI. The missing result is the planned fitted primary-outcome analysis, rather than an inference that its covariates were omitted from some unidentified fit.

**Affected result:** The prognostic-adjusted primary-composite treatment RR and confidence interval. **Bounded alternatives:** Result omitted after fitting, result under an undisclosed mapping, or an amended specification; no alternative is selected. The protocol's conditional baseline-imbalance language is retained as context, while the unconditional SAP specification and article undertaking statement establish the observation. Comparisons among existing REPORT numerical values are not alleged to conflict, so no `S_C` or `S_W` relationship is added.

### Group `component_multiplicity` — F-XS-003 and F-ST1-001

**Qualifying route:** Route A, category 5. **Focus:** D. **Proposed domain:** `protocol_report`. **Proposed relationship:** `P_R`; all relationships `P_R`.

**PLAN locations:** [protocol p.20 §13.2](../../../joi250034supp1_prod_1750956984.09018.pdf#page=20), continuing onto [protocol p.21](../../../joi250034supp1_prod_1750956984.09018.pdf#page=21); [SAP p.12 §3.2, lines 404–408](../../../joi250034supp2_prod_1750956984.11521.pdf#page=12); [SAP p.25 Table 11 adjusted-P column](../../../joi250034supp2_prod_1750956984.11521.pdf#page=25).

**REPORT locations:** [main p.3 Statistical Analysis interpretation paragraph](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=3); [main p.4 Statistical Analysis no-adjustment statement](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=4); [main p.7 Table 3](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=7).

**Independent comparison:** Both plans identify the ten individual composite components as key secondary and require adjusted P values for that family using the named procedure; SAP Table 11 has an adjusted-P column. Main p.4 states “There was no adjustment for multiple testing.” Table 3 supplies a single component P column: NA, NA, .48, .12, .96, .61, .39, .35, .34, .29. Cautious interpretation of related outcomes does not identify the planned adjusted analysis or its outputs. The observation concerns the planned-versus-reported analysis rule, independently of the procedure-name spelling or whether the reported interpretation would change after adjustment.

**Affected result:** The multiplicity-adjusted inference for all ten key secondary component results. **Bounded alternatives:** Adjustment omitted from the report, planned adjustment replaced, or a different scope intended by the no-adjustment sentence; the sources do not select one.

### Group `prior_cesarean_definition` — F-XS-005 retained component and F-ST1-004

**Qualifying route:** Route B. **Focus:** D. **Proposed domain:** `protocol_report`. **Proposed relationship:** `P_R`; all relationships `P_R`.

**PLAN comparator:** [protocol p.17 §8, subgroup 4](../../../joi250034supp1_prod_1750956984.09018.pdf#page=17). **REPORT locations:** [main p.4 prespecified-subgroup paragraph](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=4); [main p.8 Figure 2, preceding-pregnancy cesarean family](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=8). **Corroborating PLAN locations retained:** [SAP p.14 §3.11, lines 477–480](../../../joi250034supp2_prod_1750956984.11521.pdf#page=14); [SAP p.29 Table 15](../../../joi250034supp2_prod_1750956984.11521.pdf#page=29).

**Independent comparison:** The protocol specifies “one or more previous CS”; the article and Figure 2 specify cesarean delivery in the preceding pregnancy, matching the SAP's previous-pregnancy/preceding-pregnancy criterion. These are explicitly different history windows: a cesarean followed by a vaginal delivery can meet the first criterion and not the second. No such participant is asserted to have occurred. B1 is satisfied because the comparison concerns a prespecified primary-effect subgroup specification, an eligible plan/report comparison rather than a peripheral descriptive copy; B2 is satisfied because the sources do not identify this specific definition change or show that the two criteria coincide; B3 is satisfied because the extracted primary subgroup population attached to yes 4/57 versus 1/71, RR 4.98 (0.57–43.35), and no 79/1568 versus 83/1554, RR 0.94 (0.70–1.27), can differ under the two rules.

**Bounded alternatives:** The SAP prospectively revised the protocol criterion, the label summarizes a broader implemented criterion, or both criteria selected identical participants. SAP corroboration does not create an additional plan-internal relationship in this bounded issue. The possible prospective revision remains a classification ambiguity for later recheck, rather than a selected explanation.

**F-XS-005 component narrowing:** The same cited locations also show protocol “major fetal anomaly in this pregnancy” versus report/SAP “postnatal diagnosis of fetal anomaly,” with Figure 2 yes 7/19 versus 4/22, RR 2.03 (0.70–5.87), and no 76/1606 versus 80/1603, RR 0.95 (0.70–1.29). That component is excluded as `TERMINOLOGY_OR_WORDING`: the sources do not explicitly state that minor anomalies were included or that the cohort differs, and prenatal-versus-postnatal wording can describe ascertainment of the same anomaly in the current pregnancy. With no contrary coding or case detail, the difference remains ambiguous wording under the instructed wording-doubt rule. The finding row remains INCLUDE solely for the prior-cesarean component; retain the anomaly locations and this exclusion note as provenance without adding the anomaly subgroup to the included issue's affected results.

## Screened-out findings: source qualifications

### F-XS-002 — planned NNT output

The NNT commitment is present in [PLAN protocol p.20 §13.2](../../../joi250034supp1_prod_1750956984.09018.pdf#page=20), [PLAN SAP p.12 §3.2](../../../joi250034supp2_prod_1750956984.11521.pdf#page=12), [PLAN SAP p.13 §3.6](../../../joi250034supp2_prod_1750956984.11521.pdf#page=13), and [PLAN SAP p.25 Table 11](../../../joi250034supp2_prod_1750956984.11521.pdf#page=25). No NNT output is supplied in [REPORT main p.1 abstract](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=1), [p.6 primary results](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=6), [p.7 Table 3](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=7), [p.8 Figure 2](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=8), or [results supplement p.2](../../../joi250034supp3_prod_1750956984.12018.pdf#page=2); the rest of the supplied report pages contain no current-trial NNT output either.

The absence is reproduced, but neither the source nor the finding establishes a conflicting NNT value, a change in primary-outcome status/definition, a claim that the NNT was not calculated, or a separate missing fitted analysis. The primary analysis and its absolute-effect summary are supplied: 83/1625 versus 84/1625, absolute difference −0.1 percentage points (−1.6 to 1.5), RR 1.02 (0.75–1.37), P=.91. Route A category 5 does not turn every absent transformation of a reported analysis into a separate missing analysis. Route B does not identify ambiguity in the reported primary result or a competing value to extract; this remains an unreported derived display detail. No NNT or preferred reporting convention is proposed.

### F-XS-004 and F-ST1-003 — interim advice versus stopping recommendation

Exact locations: [PLAN protocol p.21 §13.3](../../../joi250034supp1_prod_1750956984.09018.pdf#page=21); [PLAN SAP p.10 §2.9, timing](../../../joi250034supp2_prod_1750956984.11521.pdf#page=10); [PLAN SAP p.11, lines 360–367](../../../joi250034supp2_prod_1750956984.11521.pdf#page=11); [REPORT main p.3 interim paragraph](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=3).

Both plans say that the committee will advise the TMC about convincing primary-composite benefit/harm using P<.001, then separately describe the mortality P<.0027 boundary with the qualification “which would be needed to justify recommending early stopping.” Main p.3 says that early-stop recommendation required a perinatal-mortality difference at P<.003. Thus the sources themselves distinguish composite advice from the specified mortality condition for an early-stop recommendation; the findings' asserted independent composite stopping permission is not established by the cited comparison. The protocol's general statement that the TMC can consider continuation, modification or stopping based on advice or other information does not negate its explicit mortality qualification. Main does not assert that composite monitoring was absent or that the planned composite analysis was replaced, so its shortened description does not independently establish an omitted applicable primary analysis under Route A category 5.

**Display precision:** For the mortality thresholds, .0027 permits [.00265,.00275] and .003 permits [.0025,.0035]; their gap is 0 and relative discrepancy is 0. No interval-versus-test conflict is alleged. The two finding rows use `NOT_REPRODUCED` for the proposed logical conflict, rather than a second rounding reason code.

## Source inspection and completion

All cited pages were reread through fresh supplied-PDF extraction using the recorded package-local `pdf_tools.py` fallback, PyMuPDF 1.26.4, sorted reading order, CPU. New derivatives are solely in `../preprocessing/inclusion_initial/`: `main.txt` (main pp.1–11), `protocol17-21.txt`, `sap10-14.txt`, `sap25-29.txt`, and `results.txt` (results supplement pp.1–6). Fresh 200-dpi CPU renders visually inspected were `main3.png`, `main7.png`, `main8.png`, `protocol17.png`, `protocol21.png`, `sap11.png`, `sap25.png`, `sap26.png`, and `results2.png`; page identity and the decisive text/table associations matched extraction. No OCR was needed. Sources and existing derivatives were preserved.

The included comparisons concern categorical model/output/specification associations, so a recomputed numeric interval and relative discrepancy are not applicable; their existing numerical values are locators and affected-result identifiers, without an asserted arithmetic conflict. The one numerical threshold comparison is explicitly reconciled above. No scientific inspection gap remains for this assigned screen. Actual model outputs, subgroup coding and a specific amendment mapping remain unavailable where named; these are bounded interpretation alternatives, not assumed facts.

**Counts:** 9 findings screened; 6 INCLUDE rows consolidated into 3 included issues; 3 SCREENED_OUT rows: `NOT_REPRODUCED` 2 and `CONDITIONAL_OR_UNREPORTED` 1; all other screened-out row reason counts 0. The excluded anomaly component of F-XS-005 is separately recorded within that included finding and does not constitute an additional finding row. Coordinator assigned C001 to prognostic_model, C002 to component_multiplicity, and C003 to prior_cesarean_definition after this independent screen.
