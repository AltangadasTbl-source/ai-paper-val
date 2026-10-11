# Numeric consistency review — count and denominator scope

Runtime task: /root/numeric_checker. Fresh numeric consistency specialist; gpt-6.1-sol, medium reasoning. Assigned scope: main mapping M001–M089 and support REPORT mappings R001–R013, R025. Estimate checker separately owns M090–M124 and R014–R024. Full scope and review contract read; all 117 assigned compound numeric relationships reviewed without a finding target. Every displayed count, denominator, percentage, category total and repeated flow count is retained in [numeric relationship inventory](../../relationships/numeric_relationship_inventory.md). All source locations in this artifact are REPORT by content.

Count arithmetic used exact printed integers, followed by conservative half-unit input intervals and each printed target's half-unit interval. An interval gap divided by the printed percentage must exceed 0.05 to qualify. Approximate graphical bar heights and model-based percentages are not treated as crude counts. No old candidate, report or checker conclusions, external sources or raw participant data were used.

## Findings

### F-NUM-001

**Title:** painTRAINER therapeutic-dose count and percentage do not reconcile.

**Relationships:** N024, N030. **Focus area:** A. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **Compared document roles:** REPORT main article Results paragraph versus REPORT main article allocation/flow. **Qualifying route:** Route A, category 3.

**Exact source locations:** [Main article physical PDF p4, Results, session completion paragraph](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); corroborating [physical PDF p5, Figure 1, painTRAINER randomized and session categories](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=5). The p4 paragraph states: “371 (43%) completed at least 6 sessions”; its immediate referent is those randomized to painTRAINER. Figure 1 prints painTRAINER randomized n776 and 371 completing 6–8 sessions, 156 completing 1–5 sessions, 249 completing 0 sessions. Their sum is 776.

**Printed inputs:** numerator371; randomized denominator776; displayed43%. The same paragraph prints527(68%) completing at least1 session. The health-coach counterparts are660(85%) and548(70%) with randomized n778.

**Rule and calculation:** percentage=100×count/randomized denominator. 100×371/776=47.809278%. With numerator [370.5,371.5] and denominator [775.5,776.5], the recomputed interval is [47.714102%,47.904578%]. Printed43% permits [42.5%,43.5%]. The interval gap is4.214102 percentage points; relative discrepancy=4.214102/43=0.0980024, exceeding0.05. The other three session-completion percentages reproduce under their stated randomized denominators. Figure 1's categories independently reproduce371 and776.

**Affected result or extracted value:** the fraction of randomized painTRAINER participants receiving the stated therapeutic dose of at least6 sessions; a data extractor could take43% or a value near47.8% from the accompanying count and randomized population.

**Why context does not resolve it:** this is a reproduced count/denominator/percentage discrepancy within one paragraph, an always-register category. The ability to calculate a percentage from the count does not remove the conflicting printed percentage.

**Alternatives and missing definition:**43% could refer to a different denominator or session-completion definition, but none is supplied in this paragraph. A denominator near863 would be needed for371/denominator to be43%; that exceeds the randomized painTRAINER population. The eight-session categories on p5 support the printed371 count without defining an alternative denominator.

**Exact human question:** Which numerator, denominator and percentage should be used for painTRAINER participants completing at least6 sessions, and what population or definition produced the printed43%?

**Direct-source confirmation:** fresh Poppler pdftotext26.01.0 layout extraction from supplied p4, CPU, confirms371(43%). Locator artifact: preprocessing/numeric_checker/main-p004.txt. No OCR normalization applied.

### F-NUM-002

**Title:** depression count and percentage in the all-observed workbook column do not reconcile.

**Relationships:** N112. **Focus area:** A. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **Compared document roles:** REPORT results workbook current-depression cell, column header and missing-count footnote within the same worksheet. **Qualifying route:** Route A, category 3.

**Exact source locations:** [Results workbook](../../../../joi250046supp5_prod_1755300121.16087.xlsx), worksheet **eTable 3**, E82, with row labelA82 “Current depression (PHQ-8 ≥10),c No. (%)”; E3 “(N=1568)”; E83 missing2; A110 states missing counts are excluded from the denominator of reported percentages. All-observed column labelE2; corresponding overall/other-pattern cellsB82:D82 and missingB83:D83 provide same-display comparators.

**Printed inputs:** E82=711(73.2); E3 N1568; E83 missing2. Thus the documented percentage denominator is1566. Overall B82=1116(47.9), missing B83=2 and N2331. Other-pattern C82=162(54.9), N295, missing0; D82=243(51.9), N468, missing0. Counts162+243+711=1116.

**Rule and calculation:** A110 requires100×711/(1568−2)=45.402299%. Allowing half-unit input intervals: count [710.5,711.5], N [1567.5,1568.5], missing [1.5,2.5], denominator [1565,1567]. Recomputed percentage interval [45.341417%,45.463259%]. Printed73.2% permits [73.15%,73.25%]. Interval gap=73.15−45.463259=27.686741 percentage points; relative discrepancy=27.686741/73.2=0.3782342, exceeding0.05. The three same-row comparator percentages reproduce from their stated denominators. Even using1568 without excluding missingness gives45.3444%, leaving the discrepancy.

**Affected result or extracted value:** baseline prevalence of current depression among participants with all primary-outcome follow-ups observed; a reader could extract73.2% or about45.4% from the accompanying count and denominator.

**Why context does not resolve it:** the count/denominator/percentage relationship within one worksheet qualifies under the always-register category, including descriptive baseline displays. Neighboring rows and the row count total support711 but do not identify which printed field should be used for extraction.

**Alternatives and missing definition:**73.2% could use an unprinted denominator near971, or711 could describe another population. Neither alternative is documented; the supplied E3/E83/A110 definition specifies1566. No provenance explanation or replacement value is inferred.

**Exact human question:** What count and denominator underlie the printed73.2% for current depression in the all-observed column, and which values should a reader use for this baseline result?

**Direct-source confirmation:** direct unzip of supplied workbook xl/worksheets/sheet1.xml and xl/sharedStrings.xml confirms E82 string711(73.2), E3 N1568, E83 numeric2 and A110 footnote; zero formulas. CPU ZIP/XML inspection is the authority, with the retained exact-cell extraction used only as a locator. Direct extracts are preserved in preprocessing/numeric_checker/sheet1.xml and sharedStrings.xml.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| Main p1/Table1 p6; workbook eTable 3 B11 and A113 | Main female count1712 versus workbook1713, with a self-reported/EHR fallback definition. Half-unit count intervals [1711.5,1712.5] and [1712.5,1713.5] meet; gap0. | ROUNDING_OR_DISPLAY_PRECISION |
| Main p7 secondary-outcomes narrative; Table3 p10 severity3-month SMD cells | Narrative−0.26/−0.36 versus table−0.25/−0.34. Half-unit gaps0 and.01 respectively; relative to narrative reference.36, .02778, below.05. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-005 p7 eTable1 observed-pattern rows; workbook eTable 3 D3 | Pattern188+283+1568=2039 versus any2036; interval gap1 relative1/2036=.000491. UC703/PT644/HC692 versus703/643/690 gives zero half-unit gaps. Weighted pattern5458 versus sum timepoint5449 gives interval gap4.5, relative.000826. Missing1-or2 workbook468 versus188+283=471 leaves gap1.5, relative1.5/468=.003205. All below.05. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-004 p6 fidelity review |1791+2350 completed sessions excludes training-period completed total, which is unprinted;193 is training sessions reviewed. Substituting193 as all training sessions would compare nonmatching totals. | CONDITIONAL_OR_UNREPORTED |
| DOC-004 p5; DOC-005 p13 modification narrative | Approximately140 versus454 enrolled at intervention change date is a peripheral administrative/enrollment comparison. Quantitative subset analysis populations and any planned decision-rule implications are separately assigned to cross-source and estimate checkers. | PERIPHERAL_COMPARISON |
| Workbook eTable 3 A103, A106 with B103:E103/B106:E106 | Threshold rows use mean(SD) wording while values visibly have counts and percentages; intended count/percentage reading is immediate and arithmetic reconciles. | TERMINOLOGY_OR_WORDING |

## Scope closure and limitations

117 complete compound relationships:89 main records,13 support families and15 workbook blocks, the latter preserving all525 nonempty cells. Two findings and six excluded-observation patterns. All count percentages within Table1 reconcile; flow recruitment, exclusions, allocation, sessions, terminal statuses, hospitalization/death group totals and all eTable1 displayed percentages were checked. The workbook category partitions, characteristic-missing denominators, category row sums and all count percentages were checked; only E82 exceeds the display-precision threshold. Mean(SD) cells are never tested as count percentages. Apparent graph shapes are not exact printed values.

No assigned scientific coverage gap. Raw-data reconstruction of continuous means/SDs and exact unnumbered histogram heights is unavailable from supplied displays; those absent inputs were not invented. Inferential conflicts, plan comparisons and adjusted-estimate transformations remain fully assigned to the other specialist lanes. Auxiliary arithmetic files contain calculations only; classification and inclusion reasoning above are agent-authored.
