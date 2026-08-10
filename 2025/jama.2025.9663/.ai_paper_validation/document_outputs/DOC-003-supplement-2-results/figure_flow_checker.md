# Figure, table-presentation, and participant-flow check

**Scope:** DOC-003 result-relevant figures and tables on PDF pp. 8-27, compared with explicitly referenced main-text claims in DOC-001. DOC-002 was not audited by design.

## Candidates for verification

### FF-01 - Cross-document inconsistency

- **Exact locations:** `jama_martin_2025_oi_250042_1753377747.91025.pdf`, PDF p. 6, Results, "Primary and Secondary Outcomes"; `joi250042supp2_prod_1753377747.93025.pdf`, PDF pp. 11-12, eFigures 4-5.
- **Evidence:** The main article reports time to death as adjusted hazard ratio 1.01 (95% CI, 0.96-1.05) and cites "eFigure 4 in Supplement 2." eFigure 4 is an FiO2/SpO2 separation display. eFigure 5 is the Kaplan-Meier mortality plot and gives hazard ratio 1.01 (95% CI, 0.96-1.05; P=.82).
- **Logical basis:** The cited figure number points to a different result; the displayed mortality estimate is in eFigure 5.
- **Verification instruction:** Compare main-article PDF p. 6 with supplement PDF pp. 11-12 and confirm the intended reference.

### FF-02 - Presentation inconsistency

- **Exact location:** `joi250042supp2_prod_1753377747.93025.pdf`, PDF p. 22, eTable 6, rows "Patient median FiO2, %" and "Patient median FiO2 when receiving O2, %."
- **Evidence:** The two row labels specify percent, but displayed means are fractional FiO2 values: 0.32 versus 0.35 and 0.30 versus 0.35 for the overall rows; 0.36 versus 0.37 and 0.34 versus 0.37 for the oxygen-only rows. eTable 5 (PDF p. 21) labels the corresponding fractional values without a percent sign, and eTable 10 (PDF p. 27) also displays FiO2 as fractions.
- **Logical basis:** Values around 0.30-0.37 are presented as fractions elsewhere in the package, while the eTable 6 label assigns percent units.
- **Verification instruction:** Confirm whether the percent signs in the two eTable 6 FiO2 row labels should be removed or whether the displayed values should instead be expressed as percentages.

### FF-03 - Presentation inconsistency

- **Exact location:** `joi250042supp2_prod_1753377747.93025.pdf`, PDF p. 26, eTable 9, "Any serious adverse event" row.
- **Evidence:** Both cells under the labelled "Events, No." columns are blank, while the adjacent patient totals are 58 (0.7%) and 29 (0.4%). The enumerated rows contain 64 conservative events (56 specified + 8 other) and 37 usual events (35 specified + 2 other).
- **Logical basis:** Overall event-total cells are omitted under explicitly labelled event-count columns despite event counts being supplied for every listed category.
- **Verification instruction:** Confirm whether the blank overall-event cells were intentional; if the listed categories are exhaustive, verify whether total event counts should be displayed. Do not assume 64 and 37 are the intended printed totals without source-author confirmation.

### FF-04 - Presentation inconsistency

- **Exact location:** `joi250042supp2_prod_1753377747.93025.pdf`, PDF p. 27, eTable 10, "Year published" row, HOT-ICU column.
- **Evidence:** The displayed value is "202"; the six adjacent entries are four-digit years (2025, 2024, 2023, 2022, 2021, 2020).
- **Logical basis:** The three-digit year is visibly incomplete relative to the row format.
- **Verification instruction:** Confirm the intended four-digit year from the production source; this check does not infer the missing digit.

### FF-05 - Presentation inconsistency

- **Exact location:** `joi250042supp2_prod_1753377747.93025.pdf`, PDF p. 27, eTable 10, PILOT recruitment-date cell and table footnote area.
- **Evidence:** The PILOT recruitment date is printed as "07/2018 to 08/2021*" but no asterisked note appears beneath the table. The only defined table footnote is superscript "a" for achieved oxygenation.
- **Logical basis:** A visible annotation marker has no corresponding legend or note on the page.
- **Verification instruction:** Inspect the production source for the omitted asterisk definition or remove the marker if it was not intended.

## Checks without a candidate

- eFigures 1-4 show internally coherent axes, legends, treatment colors, and displayed enhanced-data denominators.
- eFigure 5's plotted mortality level and hazard-ratio annotation are compatible with the nearby mortality claims; no contradiction was inferred from its restricted risk set because the caption does not state that every linkage-consented participant was plotted.
- eFigure 6 group counts and death-score legend are consistent with the organ-support outcome display.
- eFigure 7 denominators account for the 40 missing primary outcomes across data-collection subgroups, and its displayed subgroup estimates match the nearby claims.
- eTable 1 totals 16,500 randomized participants across 97 recruiting hospitals, consistent with the main-article recruitment count.

