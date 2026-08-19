# Mechanical Evidence Recheck

This artifact records a separate direct-source recheck for every stable candidate ID in the candidate ledger. Native layout extraction was used to locate text, and the source PDF pages themselves were inspected for layout-dependent claims. The observations below do not make a human adjudication.

## Coordinator repair notices

- **C001:** The direct source does contain a printed reconciliation mechanism on main-article PDF page 4: one person was randomized, did not complete baseline assessment or start treatment, and was replaced to maintain the sample size. The ledger phrase “without a printed reconciliation” does not match that page, although the printed totals and use of the word “randomized” remain as stated.
- **C007:** Protocol PDF page 15 is present but contains no BNP or NT-proBNP evidence. The relevant protocol pages are 14, 22, 41, and 54. Page 15 is an extraneous cited location for this candidate.
- **C012:** Direct visual inspection of SAP PDF page 38 shows that the one-row 24-hour ambulatory-heart-rate section has `24-hour` in the Time point column. It is not placed under `Baseline`. The ledger’s page-layout transcription should be repaired while retaining C012.

## C001 — Randomized total differs between the flow diagram and article population

- **Cited location found:** [Main article PDF page 1](../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=1), [page 3](../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=3), and [page 4](../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=4) were found. Page 3 was visually inspected because the claim depends on flow-diagram structure.
- **Source printed value/text matched:** Page 3 prints `551` assessed, `390` excluded, and `161 Randomized`; its two treatment boxes each print `80 Randomized` and `80 Received ≥1 dose of treatment`. Figure footnote b prints that one person withdrew after randomization before receiving therapy.
- **Comparator printed value/text matched:** Page 1 describes a trial “including 160 patients,” prints digoxin `n = 80` and bisoprolol `n = 80`, and begins Results with “Among 160 patients.” Page 4 prints, “There were 160 patients who completed randomization and received at least 1 dose of allocated treatment. Each group had 80 patients.”
- **Consistency rule applicable:** The arithmetic identity and repeated-population-label comparison are applicable. The stronger ledger characterization that the source supplies no reconciliation is not matched: page 4 explicitly says that one randomized participant did not complete baseline assessment or start treatment and that the trial steering committee replaced that participant to maintain the original sample size.
- **Calculation or logical comparison reproduced:** `551 - 390 = 161`; `80 + 80 = 160`; and `161 - 1 = 160`. The last identity accords with the printed early-withdrawal and replacement account, although the figure does not draw a separate allocation branch for that person.
- **Necessary inputs available and exact missing inputs:** The printed totals and the replacement explanation are available. The withdrawn participant’s allocated arm, whether the replacement is included in the figure’s `161 Randomized` node, and the intended technical distinction between “randomized,” “completed randomization,” “received treatment,” and “full analysis set” are not fully specified in the flow diagram.
- **Source-grounded alternative interpretation:** The sources support reading `161` as total initial allocation events including one pretreatment withdrawal, and `160` as the maintained treated/full-analysis cohort after replacement.
- **Direct observation:** The three totals, both arm counts, the withdrawal footnote, and the replacement sentence are printed directly in the source.
- **Inferred explanation:** Interpreting `161` as allocation events and `160` as the replacement-maintained cohort is a synthesis of those printed statements; the diagram does not itself label the two populations that way.
- **Exact remaining human question:** Is Figure 1 intended to distinguish 161 total allocation events from the replacement-maintained cohort of 160 treated participants, and should its branch structure or the abstract’s population wording explicitly name that distinction?

## C002 — Baseline digoxin NT-proBNP summaries differ between main Tables 1 and 3

- **Cited location found:** [Main article PDF page 5](../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=5), [page 6](../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=6), and [page 7](../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=7) were found; pages 5 and 7 contain the two table cells.
- **Source printed value/text matched:** Table 1 on page 5 prints baseline digoxin NT-proBNP `1095 (715-1527)` pg/mL under digoxin `n = 80`. The page 6 narrative repeats `1095 pg/mL (IQR, 715-1527 pg/mL)`.
- **Comparator printed value/text matched:** Table 3 on page 7 prints baseline digoxin NT-proBNP `1091 (710 to 1522)` pg/mL under digoxin `n = 80`.
- **Consistency rule applicable:** A repeated baseline summary for the same named analyte, arm, displayed denominator, unit, median, and IQR should agree at the same whole-number precision unless a different population, data version, or calculation convention is stated.
- **Calculation or logical comparison reproduced:** Median difference: `1095 - 1091 = 4` pg/mL. Lower IQR endpoint difference: `715 - 710 = 5` pg/mL. Upper endpoint difference: `1527 - 1522 = 5` pg/mL. One exact underlying whole-number summary cannot round to both displayed triples under one convention.
- **Necessary inputs available and exact missing inputs:** The matched labels, units, arm, `n = 80`, and all compared values are available. Participant-level values, the quartile convention, data-freeze/version history, and any hidden complete-case rule for the two tables are absent.
- **Source-grounded alternative interpretation:** Table 3 may reflect a later data freeze, a different quartile convention, or an unstated analytic handling rule despite displaying the same `n = 80`.
- **Direct observation:** The two different triples and the matching displayed denominators are printed directly.
- **Inferred explanation:** A revised data cut, subset, or quartile algorithm is not stated and is only a possible production explanation.
- **Exact remaining human question:** Do Tables 1 and 3 use the same 80 baseline digoxin measurements and the same median/IQR convention, and, if so, which printed triple is intended?

## C003 — Baseline digoxin 12-lead ECG heart-rate mean differs between main Table 1 and eTable 2

- **Cited location found:** [Main article PDF page 5](../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=5) and [Supplement 3 PDF page 14](../../../joi200126supp3_prod_1607962892.5372.pdf#page=14) were found. Supplement page 14 was visually inspected as a landscape table.
- **Source printed value/text matched:** Main Table 1 prints baseline digoxin 12-lead electrocardiogram heart rate `100.1 (16.8)` `/min` under `n = 80`.
- **Comparator printed value/text matched:** Supplement 3 eTable 2 prints `100.3 (16.8)` beats/min for baseline digoxin `n=80`. Main Table 3 on [page 7](../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=7) independently repeats `100.3 (16.8)` for baseline digoxin `n = 80`.
- **Consistency rule applicable:** The same baseline 12-lead ECG measure, arm, denominator, mean/SD form, and one-decimal precision should have one displayed mean.
- **Calculation or logical comparison reproduced:** `100.3 - 100.1 = 0.2` beats/min, while both SDs are `16.8`. A single exact mean cannot round to both `100.1` and `100.3` at one decimal.
- **Necessary inputs available and exact missing inputs:** The measure, time, arm, denominator, mean, SD, and units are available. Participant-level ECG values, inclusion flags, rounding code, and table-version history are missing.
- **Source-grounded alternative interpretation:** The agreement of eTable 2 with main Table 3 may indicate that Table 1 retained an earlier baseline-table value, or the tables may use an unstated processing distinction.
- **Direct observation:** The `100.1` and `100.3` values, equal SD, and equal displayed denominator are printed directly.
- **Inferred explanation:** A stale table value, data refresh, or processing distinction is not identified by the source.
- **Exact remaining human question:** Are these cells intended to summarize the same 80 baseline 12-lead ECG measurements, and which one-decimal mean corresponds to the intended dataset and processing rule?

## C004 — Baseline digoxin apical heart-rate mean differs between main Table 1 and eTable 2

- **Cited location found:** [Main article PDF page 5](../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=5) and [Supplement 3 PDF page 14](../../../joi200126supp3_prod_1607962892.5372.pdf#page=14) were found; the supplement table layout was visually inspected.
- **Source printed value/text matched:** Main Table 1 prints digoxin baseline “Apex beat over 30 s” as `98.2 (15.1)` `/min` under `n = 80`.
- **Comparator printed value/text matched:** eTable 2 prints “Apex beat; 30-second measurement” as `98.3 (15.1)` beats/min for baseline digoxin `n=80`.
- **Consistency rule applicable:** The matched 30-second apical measure, baseline time, arm, denominator, SD, and precision should have one displayed mean absent a stated population or processing difference.
- **Calculation or logical comparison reproduced:** `98.3 - 98.2 = 0.1` beats/min. One exact mean cannot round to both adjacent one-decimal values under the same rounding rule.
- **Necessary inputs available and exact missing inputs:** The compared cell labels, values, SD, arm, and denominator are available. Participant-level measurements, inclusion flags, rounding method, and table-version history are missing.
- **Source-grounded alternative interpretation:** An unlabelled processing or data-freeze difference could separate the two summaries even though the printed labels and `n = 80` match.
- **Direct observation:** The differing means and identical SDs are printed directly.
- **Inferred explanation:** Independent rounding inputs, a data refresh, or a hidden subset cannot be selected from the supplied text.
- **Exact remaining human question:** Are both cells derived from the same 80 baseline 30-second apical measurements, and which displayed mean is intended under the analysis dataset and rounding rule?

## C005 — Baseline digoxin radial-pulse SD differs between main Table 1 and eTable 2

- **Cited location found:** [Main article PDF page 5](../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=5) and [Supplement 3 PDF page 14](../../../joi200126supp3_prod_1607962892.5372.pdf#page=14) were found; the supplement table layout was visually inspected.
- **Source printed value/text matched:** Main Table 1 prints digoxin baseline “Radial pulse over 30 s” as `87.8 (12.1)` `/min` under `n = 80`.
- **Comparator printed value/text matched:** eTable 2 prints “Radial pulse; 30-second measurement” as `87.8 (12.0)` beats/min for baseline digoxin `n=80`.
- **Consistency rule applicable:** The same baseline radial-pulse measurements and displayed denominator should yield one one-decimal SD under one SD and rounding convention.
- **Calculation or logical comparison reproduced:** The means agree at `87.8`; the SD difference is `12.1 - 12.0 = 0.1` beats/min. One exact SD cannot round to both values under one rounding rule.
- **Necessary inputs available and exact missing inputs:** The matched labels, mean, arm, denominator, and two SDs are available. Participant-level values, sample-versus-population SD convention, inclusion flags, rounding code, and table-version history are missing.
- **Source-grounded alternative interpretation:** The tables may use different SD conventions, data versions, or an unlabelled handling difference while preserving the same displayed mean and `n = 80`.
- **Direct observation:** The same mean with two different one-decimal SDs is printed directly.
- **Inferred explanation:** The source does not identify whether an SD convention, refresh, or hidden data handling produced the difference.
- **Exact remaining human question:** Should both cells use the same participant set and SD convention, and, if so, is the intended radial-pulse SD `12.0` or `12.1` beats/min?

## C006 — Protocol assigns both PCS and physical-functioning labels to the primary endpoint

- **Cited location found:** Protocol [page 14](../../../joi200126supp1_prod_1607962892.5372.pdf#page=14), [page 21](../../../joi200126supp1_prod_1607962892.5372.pdf#page=21), [page 22](../../../joi200126supp1_prod_1607962892.5372.pdf#page=22), [page 54](../../../joi200126supp1_prod_1607962892.5372.pdf#page=54), and [page 56](../../../joi200126supp1_prod_1607962892.5372.pdf#page=56); SAP [page 18](../../../joi200126supp2_prod_1607962892.5372.pdf#page=18); and main article [page 1](../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=1) and [page 6](../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=6) were found.
- **Source printed value/text matched:** Protocol pages 14, 22, and 54 name the six-month primary outcome as the SF-36 physical component summary. SAP page 18 and main article page 1 also name six-month PCS; the article reports the PCS primary result.
- **Comparator printed value/text matched:** Protocol page 21 states both primary hypotheses in terms of the SF-36 physical functioning domain, and protocol page 56 calls the primary outcome analysis the continuous SF36 physical functioning domain score at six months. The article page 6 separately reports physical functioning among secondary SF-36 domains at 12 months.
- **Consistency rule applicable:** PCS and the physical functioning domain are separately named SF-36 measures in the supplied sources; one primary endpoint cannot be identified as both without an explicit equivalence or amendment.
- **Calculation or logical comparison reproduced:** This is a label-identity comparison rather than arithmetic: `PCS` is the SAP/article primary measure, whereas `physical functioning` is separately listed and reported as a domain. The two protocol passages therefore do not name the same printed measure.
- **Necessary inputs available and exact missing inputs:** Enough source text is available for the literal measure comparison. Missing are the protocol amendment history for these passages, the intended endpoint definition at the time each passage was drafted, and any document stating that one phrase was formally superseded.
- **Source-grounded alternative interpretation:** The two physical-functioning references may be drafting carryover, with PCS consistently intended in the trial summary, objectives, statistical considerations, SAP, and article.
- **Direct observation:** The competing labels and the separate article reporting of PCS and physical functioning are directly printed.
- **Inferred explanation:** Drafting carryover or supersession is not expressly stated in the supplied documents.
- **Exact remaining human question:** Was six-month PCS the intended primary endpoint throughout, and should protocol pages 21 and 56 be amended or annotated to distinguish physical functioning from PCS?

## C007 — Protocol outcome wording says BNP while assay and results say NT-proBNP

- **Cited location found:** Protocol [page 14](../../../joi200126supp1_prod_1607962892.5372.pdf#page=14), [page 15](../../../joi200126supp1_prod_1607962892.5372.pdf#page=15), [page 22](../../../joi200126supp1_prod_1607962892.5372.pdf#page=22), [page 41](../../../joi200126supp1_prod_1607962892.5372.pdf#page=41), and [page 54](../../../joi200126supp1_prod_1607962892.5372.pdf#page=54); SAP [page 40](../../../joi200126supp2_prod_1607962892.5372.pdf#page=40); and main article [page 7](../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=7) were found. Protocol page 15 contains no biomarker wording and is an extraneous location for this comparison.
- **Source printed value/text matched:** Protocol pages 14, 22, and 54 print “B-type natriuretic peptide (BNP)” in outcome lists. Protocol page 41 prints that “NT-pro B-type natriuretic peptide” will be analyzed with a specified assay.
- **Comparator printed value/text matched:** SAP page 40 heads the template “B-type natriuretic peptide (BNP) (NTproBNP)” and labels the row `NTproBNP (ng/L)`. Main Table 3 prints `NT-proBNP` in pg/mL.
- **Consistency rule applicable:** BNP and NT-proBNP are different analyte names. The package provides no statement defining them as interchangeable labels or a numeric conversion from one analyte to the other.
- **Calculation or logical comparison reproduced:** This is a measure-identity comparison: the outcome-list token is `BNP`, whereas the assay, SAP row, and reported result identify `NT-proBNP`. The pg/mL and ng/L notations for NT-proBNP are dimensionally equivalent and are not themselves the compared defect.
- **Necessary inputs available and exact missing inputs:** The competing analyte labels, assay text, SAP label, and result label are available. Missing are the intended analyte specification for the protocol outcome lists and any source-defined convention that uses “BNP” as a family shorthand for NT-proBNP.
- **Source-grounded alternative interpretation:** The protocol may use BNP informally as a biomarker-family shorthand while the assay and analysis consistently concern NT-proBNP.
- **Direct observation:** The outcome lists say BNP; the assay, SAP row, and result say NT-proBNP. Page 15 does not contain either relevant label.
- **Inferred explanation:** Informal shorthand or copied outcome wording is not declared in the protocol.
- **Exact remaining human question:** Was NT-proBNP the intended biomarker outcome throughout, should the protocol outcome lists be standardized to that analyte, and should page 15 be removed from this candidate’s evidence locations?

## C008 — SAP AFEQT template footnote calls the scale a visual-analogue score

- **Cited location found:** SAP [page 17](../../../joi200126supp2_prod_1607962892.5372.pdf#page=17), [page 19](../../../joi200126supp2_prod_1607962892.5372.pdf#page=19), and [page 36](../../../joi200126supp2_prod_1607962892.5372.pdf#page=36); main article [page 7](../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=7); and Supplement 3 [page 16](../../../joi200126supp3_prod_1607962892.5372.pdf#page=16) were found. SAP page 36 was visually inspected because the claim depends on which footnote is attached to which table.
- **Source printed value/text matched:** SAP page 17 names the AFEQT questionnaire overall score. Page 19 defines the AFEQT overall-score range as `0=complete disability to 100=no disability`. Page 36 heads the lower table “AFEQT overall score at 6 and 12 months” and marks its score with footnote `£`.
- **Comparator printed value/text matched:** The `£` footnote directly beneath the AFEQT table on page 36 prints, “The range for visual analogue score is from 0=worst score to 100=best score.” The upper table separately concerns the EQ-5D-5L visual analogue scale. Main Table 3 and Supplement 3 eTable 4 identify the reported measure as AFEQT overall score.
- **Consistency rule applicable:** Equal numeric ranges do not make AFEQT overall score and a visual analogue score the same measure; an AFEQT footnote should identify the AFEQT scale or otherwise state the intended relationship.
- **Calculation or logical comparison reproduced:** The page-36 footnote marker attaches the “visual analogue score” wording to the AFEQT table, while page 19 assigns a distinct AFEQT endpoint description to the same 0–100 range. The label identity does not reconcile.
- **Necessary inputs available and exact missing inputs:** The table association, footnote text, and intended AFEQT range description are available. No numerical input is missing. The SAP does not provide an edit history explaining the footnote.
- **Source-grounded alternative interpretation:** Because the immediately preceding page-36 table is the EQ-5D-5L visual analogue scale and uses closely related range wording, the AFEQT footnote may be copied template text.
- **Direct observation:** The AFEQT heading, footnote marker, visual-analogue wording, and separate EQ-5D VAS table are directly visible on page 36.
- **Inferred explanation:** Copy-forward from the preceding template is plausible but not stated.
- **Exact remaining human question:** Should the AFEQT footnote identify the AFEQT overall-score anchors rather than call it a visual analogue score?

## C009 — SAP reverses the favorable direction for E/e-prime

- **Cited location found:** SAP [page 20](../../../joi200126supp2_prod_1607962892.5372.pdf#page=20) and [page 37](../../../joi200126supp2_prod_1607962892.5372.pdf#page=37), and main article [page 7](../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=7), were found. SAP page 37 was visually inspected to associate the direction sentence with the E/e-prime table.
- **Source printed value/text matched:** SAP page 20 prints, “Lower values of E/e’ are considered better” and, with bisoprolol as reference, “lower values will indicate better outcome for Digoxin arm.”
- **Comparator printed value/text matched:** The E/e-prime template on SAP page 37 prints, “Higher values indicate better scores so a positive mean difference favours Digoxin arm.” Main Table 3 prints the digoxin-minus-bisoprolol adjusted difference as `−0.1 (−1.1 to 0.9)`.
- **Consistency rule applicable:** For one digoxin-minus-bisoprolol contrast on the same measure, lower/negative and higher/positive cannot both define the favorable direction.
- **Calculation or logical comparison reproduced:** Under the page-20 rule, a negative difference points in the lower-E/e-prime direction; under the page-37 sentence, a positive difference is favorable. These direction mappings are opposites. The reported interval crossing zero does not resolve the label contradiction.
- **Necessary inputs available and exact missing inputs:** The measure, reference group, both direction rules, and reported estimate are available. No numerical input is missing for the direction comparison. Missing is an explicit statement of which page-37 direction sentence was intended for E/e-prime.
- **Source-grounded alternative interpretation:** The page-37 sentence may be generic higher-is-better template text carried over from the preceding LVEF table.
- **Direct observation:** Both opposing direction statements and the reported adjusted difference are printed directly.
- **Inferred explanation:** Template carryover is suggested by page layout but is not declared.
- **Exact remaining human question:** Should the page-37 E/e-prime direction sentence say that lower values and a negative digoxin-minus-bisoprolol difference indicate the favorable direction?

## C010 — SAP NT-proBNP heading says six months but its table includes a 12-month row

- **Cited location found:** SAP [page 17](../../../joi200126supp2_prod_1607962892.5372.pdf#page=17), [page 21](../../../joi200126supp2_prod_1607962892.5372.pdf#page=21), and [page 40](../../../joi200126supp2_prod_1607962892.5372.pdf#page=40), and main article [page 7](../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=7), were found. SAP page 40 was visually inspected because the claim depends on table heading and row structure.
- **Source printed value/text matched:** SAP page 40 heads the table “Change in B-type natriuretic peptide (BNP) (NTproBNP) levels at 6 months.”
- **Comparator printed value/text matched:** The same table visibly contains Baseline, 6 months, and 12 months rows. SAP page 21 states that NT-proBNP is collected at baseline, 6 months, and 12 months and that separate analyses will be done at 6 and 12 months. Main Table 3 reports the 12-month NT-proBNP comparison.
- **Consistency rule applicable:** A title limited to “at 6 months” does not describe the table’s displayed 12-month analysis row.
- **Calculation or logical comparison reproduced:** The title names one follow-up (`6 months`), while the template includes two follow-ups (`6 months` and `12 months`). The set named by the title therefore omits one displayed follow-up.
- **Necessary inputs available and exact missing inputs:** The title, row labels, SAP analysis description, and reported 12-month result are available. No numerical input is missing. The intended final title and whether the template was revised are not provided.
- **Source-grounded alternative interpretation:** The table title may be an unrevised protocol-derived heading even though the finalized SAP analysis text and row structure include both follow-ups. The use of pg/mL in the article and ng/L in the SAP is a numerically equivalent unit notation for the same mass concentration and is not needed for this comparison.
- **Direct observation:** The six-month-only heading and 12-month row coexist on page 40; the other sources expressly include the 12-month analysis.
- **Inferred explanation:** An unrevised template heading is plausible but not stated.
- **Exact remaining human question:** Should the page-40 table heading name both 6- and 12-month NT-proBNP analyses, and is any explanatory standardization of the equivalent pg/mL and ng/L notation desired?

## C011 — SAP EHRA example uses an undefined class 3a

- **Cited location found:** [SAP PDF page 18](../../../joi200126supp2_prod_1607962892.5372.pdf#page=18) was found and contains both the defined class set and the example.
- **Source printed value/text matched:** Page 18 prints the categories as `1, 2a, 2b, 3, 4`, with category 1 best and category 4 worst.
- **Comparator printed value/text matched:** The next example prints, “if a patient had a baseline EHRA class of 3a and by 6 months they had an EHRA class of 2a.”
- **Consistency rule applicable:** An example value used for a variable should belong to the category set explicitly defined for that variable. `3a` is absent from the printed set.
- **Calculation or logical comparison reproduced:** Set-membership check: `3a ∉ {1, 2a, 2b, 3, 4}`. If `3a` is read as `3`, movement from `3` to `2a` crosses two ordered categories (`3 → 2b → 2a`), matching the surrounding two-class-improvement example.
- **Necessary inputs available and exact missing inputs:** The category set, ordering, and example are available. No numeric input is missing. The intended baseline token in the example is not expressly supplied elsewhere.
- **Source-grounded alternative interpretation:** `3a` may be a typographic substitution for the defined class `3`, which would make the example’s two-class movement coherent.
- **Direct observation:** The defined set omits `3a`, while the example uses it.
- **Inferred explanation:** Reading `3a` as a typo for `3` is consistent with the ordering but is not stated by the SAP.
- **Exact remaining human question:** Was the example intended to say baseline EHRA class `3`, and should `3a` be changed accordingly?

## C012 — SAP places the one-time ambulatory-HR result under a baseline heading

- **Cited location found:** SAP [page 20](../../../joi200126supp2_prod_1607962892.5372.pdf#page=20) and [page 38](../../../joi200126supp2_prod_1607962892.5372.pdf#page=38), and Supplement 3 [page 9](../../../joi200126supp3_prod_1607962892.5372.pdf#page=9), were found. SAP page 38 was visually inspected at full-page resolution.
- **Source printed value/text matched:** SAP page 20 states that 24-hour ambulatory heart rate is measured once and that no baseline score will be available for adjustment.
- **Comparator printed value/text matched:** The ledger’s stated comparator does not match the direct page layout. Page 38 places the ambulatory row in its own “24-hour ambulatory average Heart rate (bpm)” section and prints `24-hour` in the Time point column, not `Baseline`. Supplement 3 page 9 labels the reported 24-hour heart rate as measured at the end of uptitration.
- **Consistency rule applicable:** The general rule that a one-time nonbaseline measure should not be labeled baseline is applicable, but the page-38 premise needed to apply it is not present. A narrower time-label comparison remains possible because the template’s Time point cell says `24-hour` (measurement duration) rather than `end of uptitration` (visit timing).
- **Calculation or logical comparison reproduced:** Direct row-column tracing shows: outcome = `24-hour ambulatory Heart rate`; Time point = `24-hour`; statistic = `N`, `Mean [SD]`, `Min - Max`. The `Baseline` cell above belongs to the separate 12-lead ECG section.
- **Necessary inputs available and exact missing inputs:** The SAP timing statement, page-38 table structure, and results timing are available. The intended visit label for the template and whether `24-hour` was meant as duration rather than visit timing are not expressly explained.
- **Source-grounded alternative interpretation:** Page 38 may use `24-hour` to describe monitor duration in the Time point column while leaving the actual one-time visit unstated; Supplement 3 supplies that visit as end uptitration.
- **Direct observation:** Page 38 does not place the ambulatory row under `Baseline`; the row visibly says `24-hour`. Supplement 3 says end uptitration.
- **Inferred explanation:** Treating `24-hour` as measurement duration rather than visit timing is suggested by the measure name and results wording, but the template does not explain the column usage.
- **Exact remaining human question:** Should C012 be reframed around the template’s failure to name the end-uptitration visit, with `Baseline` removed from its statement, and should the Time point cell read `end uptitration` rather than `24-hour`?

## C013 — Results-supplement heart-rate table describes higher values as better quality of life

- **Cited location found:** [Supplement 3 PDF page 14](../../../joi200126supp3_prod_1607962892.5372.pdf#page=14) and main article [page 4](../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=4) and [page 6](../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=6) were found. Supplement page 14 was visually inspected to associate footnote a with eTable 2.
- **Source printed value/text matched:** Supplement 3 page 14 is eTable 2, “Resting and exertional heart rate,” and its rows and units are heart rate in beats/min.
- **Comparator printed value/text matched:** Footnote a states that differences are in reference to beta-blockers, “hence higher values represent better quality of life in the digoxin arm.” Main article page 4 discusses heart rate as a physiologic outcome, while page 6 separately reports quality-of-life measures. Supplement 3 eTable 4 on [page 16](../../../joi200126supp3_prod_1607962892.5372.pdf#page=16) uses the same clause for actual AFEQT quality-of-life scores.
- **Consistency rule applicable:** Beats/min is a heart-rate unit, not a patient-reported quality-of-life scale; no package source defines higher heart rate as better quality of life.
- **Calculation or logical comparison reproduced:** The table’s outcome label and units identify heart rate, whereas the footnote assigns a quality-of-life interpretation. The measure labels are not interchangeable. No arithmetic is required.
- **Necessary inputs available and exact missing inputs:** The table title, row labels, units, footnote, and a matching QoL-table footnote are available. No numeric input is missing. The intended heart-rate direction sentence for eTable 2 is absent.
- **Source-grounded alternative interpretation:** The quality-of-life clause may have been copied from eTable 4, where the same wording is attached to AFEQT scores; the first part of eTable 2 footnote a may only have intended to define the treatment contrast.
- **Direct observation:** A beats/min table directly carries the “better quality of life” clause, and the same clause appears on an actual QoL table.
- **Inferred explanation:** Copy-forward from the QoL table is plausible but is not stated.
- **Exact remaining human question:** Should the quality-of-life clause be removed from eTable 2 or replaced with a heart-rate-specific explanation of the adjusted contrast direction?

## C014 — Main Table 3 uses a universal higher-is-better footnote for lower-is-better measures

- **Cited location found:** Main article [page 6](../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=6) and [page 7](../../../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=7), and SAP [page 20](../../../joi200126supp2_prod_1607962892.5372.pdf#page=20), were found. Main page 7 was visually inspected to associate footnote b with the complete Table 3.
- **Source printed value/text matched:** Table 3 footnote b says bisoprolol is the reference group and, without a measure-specific qualifier, “Higher values indicate better response with digoxin therapy.” The table includes NYHA class score and E/e-prime, represented as the ratio of early mitral inflow to annular early diastolic velocity.
- **Comparator printed value/text matched:** Main page 6 states that digoxin was associated with significantly lower NYHA class. Table 3 prints the NYHA adjusted mean difference as `−0.6 (−0.8 to −0.4)` and the E/e-prime difference as `−0.1 (−1.1 to 0.9)`. SAP page 20 expressly says lower E/e-prime values indicate a better outcome for digoxin.
- **Consistency rule applicable:** One unqualified higher-is-better direction statement cannot correctly describe measures for which the supplied source defines lower values as favorable under the same digoxin-minus-bisoprolol contrast.
- **Calculation or logical comparison reproduced:** For NYHA, `1.5 - 2.0 = -0.5` from the displayed 12-month means, directionally consistent with the adjusted `−0.6` and the narrative’s “lower” wording. For E/e-prime, the printed adjusted difference is `−0.1`, and the SAP defines lower values as favorable. Both directions conflict with an unqualified positive/higher-is-better rule.
- **Necessary inputs available and exact missing inputs:** The reference group, table values, adjusted differences, NYHA narrative direction, and E/e-prime SAP direction are available. Missing is the intended scope of footnote b—whether it was meant only for applicable outcomes—and any measure-specific exception text.
- **Source-grounded alternative interpretation:** Footnote b may be generic contrast boilerplate intended for higher-is-better outcomes, while the authors relied on measure names, ordinal definitions, and narrative to convey exceptions.
- **Direct observation:** The unqualified footnote and the lower-direction examples coexist in the same table and cited sources.
- **Inferred explanation:** Restricting the footnote to only some rows is not stated and is an inferred editorial intention.
- **Exact remaining human question:** Should Table 3 limit the higher-is-better statement to applicable outcomes and explicitly state lower-is-better exceptions for NYHA class and E/e-prime?
