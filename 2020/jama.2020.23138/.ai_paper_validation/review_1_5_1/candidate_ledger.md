# Stable Candidate Ledger

All candidates remain **Pending Human Adjudication**. Stable IDs were assigned only after merging records that concerned the same printed values or statements, comparator, and consistency rule. No candidate was ranked, suppressed, or selected by count.

## C001 — Randomized total differs between the flow diagram and article population

- **Category:** Denominator, proportion, or total inconsistency
- **Exact source locations:** `jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=1`, `#page=3`, and `#page=4`.
- **Printed evidence:** Figure 1 prints 551 assessed, 390 excluded, and 161 randomized; the abstract and Results describe 160 randomized and the two arms contain 80 participants each. Figure 1 notes one participant withdrew after randomization before therapy.
- **Consistency rule:** 551 - 390 = 161, whereas 80 + 80 = 160. Page 4 supplies a replacement mechanism, but the diagram and article population wording do not consistently label initial allocation events versus the replacement-maintained treated/full-analysis cohort.
- **Source-grounded alternative:** Page 4 supports that one randomized participant did not complete baseline assessment or start treatment and was replaced, so 161 may count initial allocation events while 160 describes the maintained treated/full-analysis cohort.
- **Checker provenance:** Numeric consistency Proposal 1; mapper relationships N001 and N002.
- **Human question:** Should the abstract/flow explicitly distinguish 161 initial allocation events from the replacement-maintained cohort of 160 treated/analyzed participants?

## C002 — Baseline digoxin NT-proBNP summaries differ between main Tables 1 and 3

- **Category:** Numeric or arithmetic inconsistency
- **Exact source locations:** `jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=5`, `#page=6`, and `#page=7`.
- **Printed evidence:** Table 1 and narrative print 1095 (IQR 715-1527) pg/mL; Table 3 prints 1091 (710-1522) for the same baseline digoxin measure and displayed n=80.
- **Consistency rule:** The median differs by 4 pg/mL and each IQR endpoint by 5 pg/mL, beyond whole-number rounding of one common summary.
- **Source-grounded alternative:** Table 3 may use an unstated analytic subset or revised data cut.
- **Checker provenance:** Numeric consistency Proposal 2; mapper relationships N011 and N022.
- **Human question:** What denominator or data version accounts for the Table 3 values, or which repeated summary should be corrected?

## C003 — Baseline digoxin 12-lead ECG heart-rate mean differs between main Table 1 and eTable 2

- **Category:** Cross-document numeric inconsistency
- **Exact source locations:** `jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=5`; `joi200126supp3_prod_1607962892.5372.pdf#page=14`.
- **Printed evidence:** Main Table 1 prints 100.1 (16.8) /min; eTable 2 prints 100.3 (16.8) beats/min, both for baseline digoxin n=80.
- **Consistency rule:** The one-decimal means differ by 0.2 beats/min for an otherwise matched measure, arm, time, denominator, and SD.
- **Source-grounded alternative:** Separate table freezes, processing definitions, or an unlabelled subset could explain the values.
- **Checker provenance:** Numeric consistency Proposal 3; cross-source Proposal 1; relationships N012 and N3010.
- **Human question:** Are both cells intended to summarize the same 80 baseline ECG measurements, and if so which mean is correct?

## C004 — Baseline digoxin apical heart-rate mean differs between main Table 1 and eTable 2

- **Category:** Cross-document numeric inconsistency
- **Exact source locations:** `jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=5`; `joi200126supp3_prod_1607962892.5372.pdf#page=14`.
- **Printed evidence:** Main Table 1 prints 98.2 (15.1) /min; eTable 2 prints 98.3 (15.1) beats/min, with baseline digoxin n=80 in both.
- **Consistency rule:** The means differ by 0.1 at the same one-decimal precision while SD, arm, time, and denominator match.
- **Source-grounded alternative:** Independent rounding inputs or an unlabelled measurement/subset distinction may exist.
- **Checker provenance:** Numeric consistency Proposal 5; cross-source Proposal 2; relationships N012 and N3011.
- **Human question:** Are these the same 30-second apical assessment, and which displayed mean is intended?

## C005 — Baseline digoxin radial-pulse SD differs between main Table 1 and eTable 2

- **Category:** Cross-document numeric inconsistency
- **Exact source locations:** `jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=5`; `joi200126supp3_prod_1607962892.5372.pdf#page=14`.
- **Printed evidence:** Main Table 1 prints 87.8 (12.1) /min; eTable 2 prints 87.8 (12.0) beats/min for baseline digoxin n=80.
- **Consistency rule:** The one-decimal SD differs by 0.1 for an otherwise matched cell.
- **Source-grounded alternative:** A table refresh, independent computation, or unstated subset may explain the difference.
- **Checker provenance:** Numeric consistency Proposal 4; cross-source Proposal 3; relationships N012 and N3012.
- **Human question:** Should the radial-pulse SD be 12.0 or 12.1, or do the tables use different calculations?

## C006 — Protocol assigns both PCS and physical-functioning labels to the primary endpoint

- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** `joi200126supp1_prod_1607962892.5372.pdf#page=14`, `#page=21`, `#page=22`, `#page=54`, and `#page=56`; `joi200126supp2_prod_1607962892.5372.pdf#page=18`; `jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=1` and `#page=6`.
- **Printed evidence:** Protocol pp.14/22/54 name the six-month SF-36 physical component summary, while pp.21/56 call the primary measure the physical-functioning domain. The SAP and reported primary result use PCS; physical functioning is separately reported.
- **Consistency rule:** PCS and physical functioning are distinct SF-36 measures and cannot both identify one primary endpoint without explanation.
- **Source-grounded alternative:** The physical-functioning wording may be drafting carryover while PCS was the intended endpoint.
- **Checker provenance:** Numeric Proposal 6; cross-source Proposal 4; statistical pass 1 P1-PROP-01; N1002, S1001, and S1005.
- **Human question:** Was PCS intended throughout, and should the two physical-functioning references be corrected or reconciled?

## C007 — Protocol outcome wording says BNP while assay and results say NT-proBNP

- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** `joi200126supp1_prod_1607962892.5372.pdf#page=14`, `#page=22`, `#page=41`, and `#page=54`; `joi200126supp2_prod_1607962892.5372.pdf#page=40`; `jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=7`.
- **Printed evidence:** Protocol outcome lists call the biomarker BNP, its assay section identifies NT-proBNP, the SAP says BNP (NTproBNP), and the reported result is NT-proBNP.
- **Consistency rule:** BNP and NT-proBNP are distinct analyte labels; the supplied sources give no numerical conversion making the names interchangeable.
- **Source-grounded alternative:** BNP may be used informally as a peptide-family shorthand.
- **Checker provenance:** Numeric Proposal 7; cross-source Proposal 5; N1005 and N1016.
- **Human question:** Was NT-proBNP the intended outcome throughout, and should the outcome-list terminology be standardized?

## C008 — SAP AFEQT template footnote calls the scale a visual-analogue score

- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** `joi200126supp2_prod_1607962892.5372.pdf#page=17`, `#page=19`, and `#page=36`; `jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=7`; `joi200126supp3_prod_1607962892.5372.pdf#page=16`.
- **Printed evidence:** The SAP defines and heads the table as AFEQT overall score, but its p.36 footnote calls the 0-100 range a visual analogue score; EQ-5D VAS is a separate instrument.
- **Consistency rule:** A shared 0-100 range does not make AFEQT and a visual-analogue score the same measure.
- **Source-grounded alternative:** The footnote may be copied from the preceding EQ-5D VAS template.
- **Checker provenance:** Numeric Proposal 8; cross-source Proposal 6; statistical pass 1 P1-PROP-02; N2013 and S2009.
- **Human question:** Should the footnote identify AFEQT rather than a visual-analogue score?

## C009 — SAP reverses the favorable direction for E/e-prime

- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** `joi200126supp2_prod_1607962892.5372.pdf#page=20` and `#page=37`; `jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=7`.
- **Printed evidence:** SAP p.20 says lower E/e-prime is better; the p.37 template says higher values and a positive difference favor digoxin. The reported adjusted difference is -0.1 (-1.1 to 0.9).
- **Consistency rule:** For the same digoxin-minus-bisoprolol contrast, lower/negative and higher/positive cannot both define the favorable direction.
- **Source-grounded alternative:** The p.37 sentence may be generic higher-is-better boilerplate.
- **Checker provenance:** Numeric Proposal 9; cross-source Proposal 7; statistical pass 1 P1-PROP-03; N2021, S2011, and S017.
- **Human question:** Should the p.37 direction statement specify lower/negative values as favorable for E/e-prime?

## C010 — SAP NT-proBNP heading says six months but its table includes a 12-month row

- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** `joi200126supp2_prod_1607962892.5372.pdf#page=17`, `#page=21`, and `#page=40`; `jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=7`.
- **Printed evidence:** The p.40 blank table is headed NT-proBNP “at 6 months” but contains baseline, 6-month, and 12-month rows; p.21 specifies analyses at both follow-ups and the article reports both. The SAP also alternates pg/mL and numerically equivalent ng/L labels.
- **Consistency rule:** A heading limited to six months does not cover its displayed 12-month row. The equivalent unit notation is contextual and is not the independent candidate rule.
- **Source-grounded alternative:** The title may be an unrevised template heading.
- **Checker provenance:** Numeric Proposal 10; cross-source Proposal 10; statistical pass 1 P1-PROP-04; N2015, N2027, and S2015.
- **Human question:** Should the table heading name both 6 and 12 months, and should equivalent units be standardized or explained?

## C011 — SAP EHRA example uses an undefined class 3a

- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** `joi200126supp2_prod_1607962892.5372.pdf#page=18`.
- **Printed evidence:** The SAP defines modified EHRA classes 1, 2a, 2b, 3, and 4, then illustrates two-class improvement with “3a” to 2a.
- **Consistency rule:** 3a is not a member of the explicitly defined category set.
- **Source-grounded alternative:** “3a” may be a typographic error for class 3.
- **Checker provenance:** Numeric Proposal 11; statistical pass 1 P1-PROP-05; N2017 and S2014.
- **Human question:** Was class 3 intended in the example?

## C012 — SAP ambulatory-HR template uses monitor duration where the visit time point is expected

- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** `joi200126supp2_prod_1607962892.5372.pdf#page=20` and `#page=38`; `joi200126supp3_prod_1607962892.5372.pdf#page=9`.
- **Printed evidence:** SAP p.20 says 24-hour ambulatory heart rate is measured once and has no baseline score. Direct visual recheck shows that the p.38 Time point cell says `24-hour`, which describes monitor duration rather than the visit; the results supplement labels the measurement end uptitration. The nearby `Baseline` cell belongs to the separate 12-lead ECG section.
- **Consistency rule:** A table column headed Time point should identify the measurement visit; `24-hour` identifies duration and does not match the reported end-uptitration visit.
- **Source-grounded alternative:** The template may intentionally repeat monitor duration in the Time point column while leaving visit timing implicit.
- **Checker provenance:** Numeric Proposal 12; N2022 and S2012.
- **Human question:** Should the Time point cell identify end uptitration rather than repeat the 24-hour monitor duration?

## C013 — Results-supplement heart-rate table describes higher values as better quality of life

- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** `joi200126supp3_prod_1607962892.5372.pdf#page=14`; `jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=4` and `#page=6`.
- **Printed evidence:** eTable 2 contains beats/min outcomes, but footnote a says higher values represent better quality of life in the digoxin arm.
- **Consistency rule:** Heart rate in beats/min is not a QoL scale, and no supplied rule equates higher heart rate with better QoL.
- **Source-grounded alternative:** The clause may be copied from QoL eTables 3-4 and may only have intended to name contrast direction.
- **Checker provenance:** Numeric Proposal 13; cross-source Proposal 9; statistical pass 1 P1-PROP-06; N3010-N3015 and S3016.
- **Human question:** Should the QoL clause be removed or replaced with a heart-rate-specific direction statement?

## C014 — Main Table 3 uses a universal higher-is-better footnote for lower-is-better measures

- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** `jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=6` and `#page=7`; `joi200126supp2_prod_1607962892.5372.pdf#page=20`.
- **Printed evidence:** Table 3 footnote b says higher values indicate better response with digoxin, but the table includes NYHA score and E/e-prime, for which supplied text defines lower values as better. Their printed differences are -0.6 and -0.1, respectively.
- **Consistency rule:** An unqualified higher-is-better direction cannot apply simultaneously to lower-is-better measures in the same table.
- **Source-grounded alternative:** The sentence may have been intended only for applicable higher-is-better outcomes or as a generic contrast statement.
- **Checker provenance:** Cross-source Proposal 8; relationships S015, S017, and N026.
- **Human question:** Should Table 3 give measure-specific direction exceptions or limit the higher-is-better statement?
