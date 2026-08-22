# Cross-Source Consistency Check

## Scope and method

This check covers the complete current quantitative maps for DOC-001 through DOC-005: 125 numeric relationships and 90 inferential-statistical relationships (215 records). It compared every mapped repeated or definition-linked occurrence that could plausibly describe the same result, after matching the randomized/available-case population, time point, intervention contrast, model, measure, scale, unit, reference group, analysis set, and printed precision. Direct PDFs were the authority; current native/layout text was used only to locate the cited passages. No legacy candidate, checker, verifier, critic, or report material was read. DOC-005 is a data-sharing statement and contains no quantitative result to match.

The review checked the following complete evidence lanes.

| Lane | Matched scope completed | Result |
|---|---|---|
| Main article ↔ results supplement | Table 1/Table 2/Table 3/Figure 2 and narrative/abstract occurrences against eTables 1-5 and eFigures 2-5, including all mapped heart-rate, QoL, biomarker, echocardiography, EHRA, and safety relationships | Three baseline heart-rate cell differences and one direction-label issue are proposed below; remaining matched results reconcile at the stated precision or are different measures/times/models. |
| Main article ↔ protocol | Primary outcome, arm contrast, sample-size convention, analysis-set definitions, outcome schedule, biomarker naming, units, and rate/count definitions | Primary-endpoint and biomarker-label proposals are below; no unmatched realized count, rate, or effect estimate was found. |
| Main article/results supplement ↔ SAP | Primary/secondary outcome definitions, scales, covariates/reference, direction, model type, time point, and blank result templates | AFEQT, E/e', and NT-proBNP template-label proposals are below. Blank templates were not treated as observed result values. |
| Protocol ↔ SAP | Planned primary outcome, ITT/available-data rules, sample-size plan, adjustment factors, scale definitions, and safety-count conventions | The protocol's physical-functioning wording conflicts with the SAP's PCS wording; all other compared definitions either agree or differ only in planning detail without a conflicting displayed result. |

## Candidate proposals pending human adjudication

These are distinct source-grounded proposals, not stable candidate IDs and not adjudications.

### Proposal 1 — Baseline 12-lead ECG heart-rate mean differs between main Table 1 and eTable 2

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** [DOC-001 Table 1, PDF p. 5](<../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=5>); [DOC-004 eTable 2, PDF p. 14](<../../../joi200126supp3_prod_1607962892.5372.pdf#page=14>).
- **Printed values:** For the digoxin arm at baseline, n=80, both locations label the measure as 12-lead ECG heart rate in beats/min and print SD 16.8. Table 1 prints **100.1 (16.8)**; eTable 2 prints **100.3 (16.8)**. The bisoprolol value is 99.2 (19.2) in both locations.
- **Comparison logic:** Population, baseline time point, arm, instrument, unit, and one-decimal display precision match. A 0.2 difference remains after matching these fields; it is not explained by the stated display precision.
- **Supported alternatives:** One location may derive from a differently rounded underlying value or from a separately frozen extract, despite the identical n and SD. The supplied sources do not state such a distinction.
- **Human verification steps:** Inspect the Table 1 and eTable 2 production data or source table; confirm whether 100.1 or 100.3 is the intended baseline digoxin ECG mean and whether the two displays intentionally use different rounding inputs.

### Proposal 2 — Baseline apical heart-rate mean differs between main Table 1 and eTable 2

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** [DOC-001 Table 1, PDF p. 5](<../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=5>); [DOC-004 eTable 2, PDF p. 14](<../../../joi200126supp3_prod_1607962892.5372.pdf#page=14>).
- **Printed values:** For the digoxin arm at baseline, n=80, the 30-second apex-beat measure has SD 15.1 in both locations. Table 1 prints **98.2 (15.1) /min**; eTable 2 prints **98.3 (15.1) beats/min**. The bisoprolol value is 99.0 (16.8) in both locations.
- **Comparison logic:** The population, time, treatment arm, measurement method, unit, and displayed precision match. The one-decimal mean differs by 0.1.
- **Supported alternatives:** The same underlying value may have been rounded differently in independently prepared tables; no differing analysis set or measurement time is printed.
- **Human verification steps:** Compare the baseline apical-pulse source records or table-generation outputs and establish which one-decimal mean is intended.

### Proposal 3 — Baseline radial-pulse SD differs between main Table 1 and eTable 2

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** [DOC-001 Table 1, PDF p. 5](<../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=5>); [DOC-004 eTable 2, PDF p. 14](<../../../joi200126supp3_prod_1607962892.5372.pdf#page=14>).
- **Printed values:** For the digoxin arm at baseline, n=80, 30-second radial pulse, Table 1 prints **87.8 (12.1) /min** and eTable 2 prints **87.8 (12.0) beats/min**. The bisoprolol value is 86.9 (10.3) in both.
- **Comparison logic:** The matched mean and all defining fields agree, but the SD differs at the displayed one-decimal precision. The source gives no different subset, calculation method, or time for either baseline cell.
- **Supported alternatives:** Different rounding or a late table refresh could account for the 0.1 SD difference; neither explanation is documented in the supplied PDFs.
- **Human verification steps:** Recalculate or inspect the baseline radial-pulse SD for the 80 digoxin participants, and confirm the intended displayed SD.

### Proposal 4 — The protocol labels the primary endpoint as physical functioning where the SAP and reported trial result identify PCS

- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** [DOC-002 protocol, PDF p. 21](<../../../joi200126supp1_prod_1607962892.5372.pdf#page=21>) and [PDF p. 56](<../../../joi200126supp1_prod_1607962892.5372.pdf#page=56>); [DOC-003 SAP, PDF p. 18](<../../../joi200126supp2_prod_1607962892.5372.pdf#page=18>); [DOC-001 main article, PDF p. 3](<../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=3>) and [PDF p. 6](<../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=6>); [DOC-004 eFigure 4 glossary, PDF p. 11](<../../../joi200126supp3_prod_1607962892.5372.pdf#page=11>).
- **Printed values and labels:** The protocol calls the primary quality-of-life measure the SF-36 **physical component summary** on pp. 14, 22, and 54, but calls it the **physical functioning domain** in its p. 21 hypothesis and p. 56 primary-analysis section. The SAP specifies the **PCS score**. The reported primary result is PCS: 31.9 (11.7) versus 29.7 (11.4), adjusted difference 1.4 (95% CI, -1.1 to 3.8), P=.28. Physical functioning is a separate reported domain (at 12 months, 31.5 [14.1] versus 27.5 [13.0], adjusted difference 2.8 [0 to 5.7], P=.05).
- **Comparison logic:** PCS and physical functioning are separately named SF-36 measures and have different printed values. They therefore cannot be treated as interchangeable descriptions of one primary endpoint.
- **Supported alternatives:** The two protocol instances may be drafting carryover errors while the governing SAP and final report consistently use PCS. The documents do not explicitly declare a protocol amendment or label correction.
- **Human verification steps:** Review the approved protocol version history and statistical-analysis authorization; determine whether p. 21/p. 56 were intended to say PCS and whether a correction or explanatory note is needed.

### Proposal 5 — Protocol outcome wording uses BNP while its assay and the reported result use NT-proBNP

- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** [DOC-002 protocol, PDF p. 14](<../../../joi200126supp1_prod_1607962892.5372.pdf#page=14>), [PDF p. 22](<../../../joi200126supp1_prod_1607962892.5372.pdf#page=22>), and [PDF p. 41](<../../../joi200126supp1_prod_1607962892.5372.pdf#page=41>); [DOC-003 SAP, PDF p. 40](<../../../joi200126supp2_prod_1607962892.5372.pdf#page=40>); [DOC-001 Table 3, PDF p. 7](<../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=7>).
- **Printed values and labels:** Protocol outcome lists say “change in B-type natriuretic peptide (BNP),” whereas the protocol assay page names **NT-pro B-type natriuretic peptide**. The SAP template says “BNP (NTproBNP).” The reported Table 3 measure is **NT-proBNP**, with 12-month medians 960 (626-1531) versus 1250 (847-1890) pg/mL and geometric-mean ratio 0.77 (0.64-0.92), P=.005.
- **Comparison logic:** BNP and NT-proBNP are distinct analyte labels. The reported numerical result is explicitly NT-proBNP, so the generic BNP outcome label does not preserve the reported measure identity.
- **Supported alternatives:** “BNP” may have been used informally as a family-level shorthand rather than as the assayed analyte; the protocol's assay specification supports that interpretation but does not state it.
- **Human verification steps:** Verify the laboratory analyte and approved outcome terminology; confirm whether every outcome-list occurrence of “BNP” was intended as shorthand for NT-proBNP.

### Proposal 6 — SAP AFEQT template labels its range as a visual-analogue score

- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** [DOC-003 SAP Appendix D6, PDF p. 36](<../../../joi200126supp2_prod_1607962892.5372.pdf#page=36>); [DOC-001 main article, PDF p. 3](<../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=3>) and [PDF p. 7](<../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=7>); [DOC-004 eFigure 4 glossary, PDF p. 11](<../../../joi200126supp3_prod_1607962892.5372.pdf#page=11>) and [eTable 4, PDF p. 16](<../../../joi200126supp3_prod_1607962892.5372.pdf#page=16>).
- **Printed values and labels:** The SAP template heading is “AFEQT overall score at 6 and 12 months,” but its £ footnote says “The range for **visual analogue score** is from 0=worst score to 100=best score.” The main article distinguishes EQ-5D visual analog scale from AFEQT, and the results supplement defines AFEQT as the Atrial Fibrillation Effect on QualiTy-of-life overall score. Reported AFEQT overall at 12 months is 75.6 (17.1) versus 68.1 (16.1), adjusted difference 4.1 (-0.5 to 8.7), P=.08.
- **Comparison logic:** Both measures use a 0-100 scale, but their names and instruments differ. A shared range does not make an AFEQT score a visual-analogue score.
- **Supported alternatives:** The SAP footnote may be a copied range statement that is numerically correct but attached to the wrong instrument.
- **Human verification steps:** Inspect the SAP template source and confirm that the £ footnote should name AFEQT, not the EQ-5D VAS.

### Proposal 7 — SAP E/e' template says higher values and a positive difference favour digoxin although the SAP defines lower E/e' as better

- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** [DOC-003 SAP, PDF p. 20](<../../../joi200126supp2_prod_1607962892.5372.pdf#page=20>) and [Appendix D6, PDF p. 37](<../../../joi200126supp2_prod_1607962892.5372.pdf#page=37>); [DOC-001 Table 3, PDF p. 7](<../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=7>).
- **Printed values and labels:** SAP p. 20 states that “Lower values of E/e' are considered better.” Its E/e' result template on p. 37 states, “Higher values indicate better scores so a positive mean difference favours Digoxin arm.” The reported 12-month E/e' values are 10.8 (5.1) versus 10.8 (5.5), adjusted digoxin-minus-bisoprolol difference **-0.1** (-1.1 to 0.9), P=.81.
- **Comparison logic:** Population, time, contrast, adjusted mean-difference scale, and reference group are the same. For a measure explicitly defined as better when lower, the template's higher/positive-favours wording reverses the stated direction.
- **Supported alternatives:** The p. 37 sentence may be generic boilerplate intended for adjacent higher-is-better outcomes rather than an interpretation of E/e'. It is nevertheless printed directly below the E/e' template without an exception.
- **Human verification steps:** Confirm the intended E/e' direction in the SAP and determine whether the p. 37 boilerplate should be removed or replaced with lower/negative-favours wording.

### Proposal 8 — Main Table 3 gives a universal higher-value direction statement that conflicts with the lower-is-better E/e' and NYHA measures it contains

- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** [DOC-001 Table 3 and footnotes, PDF p. 7](<../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=7>); [DOC-001 results narrative, PDF p. 6](<../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=6>); [DOC-003 SAP E/e' definition, PDF p. 20](<../../../joi200126supp2_prod_1607962892.5372.pdf#page=20>).
- **Printed values and labels:** Table 3 footnote b says that, with bisoprolol as reference, “Higher values indicate better response with digoxin therapy.” The same table includes E/e' (10.8 [5.1] versus 10.8 [5.5], adjusted difference -0.1 [-1.1 to 0.9]) and NYHA score (1.5 [.6] versus 2.0 [.6], adjusted difference -0.6 [-0.8 to -0.4]). The narrative describes the lower NYHA class as better; the SAP defines lower E/e' as better.
- **Comparison logic:** The footnote is presented as the adjustment/direction statement for the table's adjusted models. A higher-is-better direction cannot apply to these two lower-is-better measures without an explicit exception.
- **Supported alternatives:** The sentence may mean only that a positive contrast generally favours digoxin for applicable outcomes, rather than that a higher raw value is clinically better. Its unqualified placement and the two contrary measures leave this unclear.
- **Human verification steps:** Review the intended scope of Table 3 footnote b; specify measure-specific direction for E/e' and NYHA, or explicitly limit the generic statement to higher-is-better outcomes.

### Proposal 9 — eTable 2 heart-rate footnote describes higher heart-rate values as better quality of life

- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** [DOC-004 eTable 2 footnote a, PDF p. 14](<../../../joi200126supp3_prod_1607962892.5372.pdf#page=14>); [DOC-002 protocol heart-rate target, PDF p. 32](<../../../joi200126supp1_prod_1607962892.5372.pdf#page=32>); [DOC-001 main article, PDF p. 4](<../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=4>).
- **Printed values and labels:** eTable 2 reports heart rate in beats/min, then footnote a says that because differences reference beta-blockers, “higher values represent better quality of life in the digoxin arm.” The protocol specifies a resting-heart-rate aim of **<=100 beats/min**. The main article reports the post-uptitration 24-hour heart-rate adjusted difference as 4.3/min (0.7 to 7.9), P=.02, but does not describe a higher rate as a quality-of-life measure.
- **Comparison logic:** The eTable's population, time points, and contrast are heart-rate measurements, not a quality-of-life scale. Its direction statement attaches a QoL interpretation to a beats/min outcome and does not match the protocol's lower threshold target.
- **Supported alternatives:** This may be a copied adjustment footnote from the QoL eTables, with “better quality of life” not intended to interpret the heart-rate effects. The source does not label it as a copy or exception.
- **Human verification steps:** Confirm whether eTable 2 should omit the QoL wording and, if directionality is intended, state an outcome-appropriate heart-rate interpretation.

### Proposal 10 — SAP NT-proBNP template heading says “at 6 months” while its rows include baseline, 6 months, and 12 months

- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** [DOC-003 SAP Appendix D6, PDF p. 40](<../../../joi200126supp2_prod_1607962892.5372.pdf#page=40>); [DOC-003 SAP outcome definition, PDF p. 21](<../../../joi200126supp2_prod_1607962892.5372.pdf#page=21>); [DOC-001 Table 3, PDF p. 7](<../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=7>).
- **Printed values and labels:** The p. 40 heading is “Change in B-type natriuretic peptide (BNP) (NTproBNP) levels **at 6 months**.” Its blank table prints baseline, 6-month, and 12-month rows. SAP p. 21 specifies NT-proBNP analysis at baseline, 6, and 12 months; Table 3 reports the 12-month value 960 versus 1250 pg/mL and ratio 0.77 (0.64 to 0.92), P=.005.
- **Comparison logic:** The table layout and the SAP's own outcome definition include a 12-month result, while the heading restricts the outcome to 6 months. This is a time-label inconsistency, not a comparison of the blank template cells with observed values.
- **Supported alternatives:** “At 6 months” may be an unrevised template title retained after the 12-month row was added.
- **Human verification steps:** Consult the SAP amendment/template history and confirm whether the heading should read “at 6 and 12 months” (with baseline descriptive rows) or whether the 12-month row was unintended.

## Matched occurrences not proposed as candidates

- The main abstract, narrative, Table 2, Table 3, Editor's Note, and results-supplement eTables agree for the normalized six-month PCS result, resting 6- and 12-month ECG heart-rate effects, EHRA binary and ordinal results, 12-month NT-proBNP ratio, QoL effects, walk ratio, LVEF/diastolic effects, and safety event/patient distinctions, except where proposals above identify a separately printed label or baseline cell.
- The 24-hour heart-rate values in DOC-004 (79+/-11 versus 74+/-11, P=.020) and DOC-001 (adjusted difference 4.3/min, 0.7-7.9, P=.02) were not called discrepant: they concern the same end-of-uptitration measure but use unadjusted arm summaries versus an adjusted contrast, and their printed precision differs.
- Figure 4 P values .013, .049, and .038 in DOC-004 round to the corresponding eTable values .01, .05, and .04; no cross-source conflict remains at the table's two-decimal precision.
- Unnormalized six-month PCS values in the Key Points/Table 2 and normalized PCS values in the abstract/Table 2 are different defined scales, not conflicting estimates.
- Protocol/SAP ITT wording and the main article's full analysis set do not produce a displayed denominator conflict: the final trial cohort has 160 randomized participants with at least one dose after replacement of the pre-treatment withdrawal.
- Protocol/SAP `pg/mL` versus `ng/L` labels for NT-proBNP are numerically equivalent units (1 pg/mL = 1 ng/L). The SAP's unit variation is retained as a documentation limitation, but it is not a numeric conflict without a value that fails conversion.
- SAP blank cells, dashes, and P-value placeholders were not treated as results; they cannot conflict with an observed result solely by lacking a populated value.
- No coherent P=0 or p=0.000 display occurred in this assigned scope.

## Counts and limitations

- **Mapped relationship records reviewed:** 215 (125 numeric; 90 inferential-statistical).
- **Distinct qualifying candidate proposals:** 10.
- **Non-candidate matched/definition checks documented:** 8 grouped check classes above, covering all remaining credible repeated-result and definition-linked occurrences in the mapped lanes.
- **Limitations:** Direct sources provide no underlying dataset, table-generation scripts, protocol amendment log, or production-history explanation for the three small baseline heart-rate differences. Template-only proposals concern printed labels/directions, not unfilled numerical cells. No external sources or legacy AI conclusions were used.
