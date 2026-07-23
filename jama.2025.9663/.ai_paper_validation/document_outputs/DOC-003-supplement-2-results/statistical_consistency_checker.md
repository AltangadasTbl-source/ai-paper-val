# Statistical Consistency Checker

## Candidate SC-01

- **Taxonomy:** Cross-document inconsistency
- **Locations and source values:**
  - `jama_martin_2025_oi_250042_1753377747.91025.pdf`, PDF p. 6, Results, "Primary and Secondary Outcomes": time to death is reported as adjusted hazard ratio 1.01 (95% CI, 0.96-1.05) and attributed to "eFigure 4 in Supplement 2."
  - `joi250042supp2_prod_1753377747.93025.pdf`, PDF p. 11, eFigure 4: the figure is "Separation in FIO2 and SpO2 when receiving oxygen over time and by site participant sequence"; it does not display time to death.
  - Same supplement, PDF p. 12, eFigure 5: Kaplan-Meier plot of cumulative all-cause mortality to 1 year; hazard ratio 1.01 (95% CI, 0.96-1.05; P=.82).
- **Logical basis:** The estimate and CI in the main article repeat the time-to-death values in eFigure 5, not eFigure 4. The supplement figure number cited for this result is therefore inconsistent across documents.
- **Verification step:** Open main-article PDF p. 6 and supplement PDF pp. 11-12; confirm that the time-to-death citation should identify eFigure 5.

## Candidate SC-02

- **Taxonomy:** Presentation inconsistency
- **Locations and source values:**
  - `jama_martin_2025_oi_250042_1753377747.91025.pdf`, PDF p. 6, Results, "Oxygen Exposure": mean (SD) of patient median SpO2 is 93.3% (2.8%) conservative versus 95.1% (2.4%) usual.
  - `joi250042supp2_prod_1753377747.93025.pdf`, PDF p. 21, eTable 5, "Patient median SpO2, %, Mean (SD) [No.]": 93.3 (2.8) [1248] versus 95.1 (2.4) [1230], difference -1.8 percentage points (95% CI, -2.0 to -1.6).
  - Same supplement, PDF p. 27, eTable 10, UK-ROX "Achieved oxygenation": lower-group SpO2 93.3%, higher-group SpO2 95.2%, difference (high-low) 2%.
  - eTable 5 separately reports "Patient median SpO2 when receiving O2" as 93.3% (3.0%) [1225] versus 95.2% (2.6%) [1228]. By contrast, eTable 10's PaO2 values (71.5 and 79.5 mm Hg) and FIO2 values (0.31 and 0.35) match eTable 5's overall patient-median rows, not its "when receiving O2" rows (PaO2 73.8 and 81.4; FIO2 0.35 and 0.37).
- **Logical basis:** eTable 10 changes the usual-group SpO2 from the overall value 95.1% to the "when receiving O2" value 95.2% without labelling that switch, while its PaO2 and FIO2 entries use the overall measures. The generic "Achieved oxygenation" label therefore does not identify a statistically consistent source measure across metrics.
- **Verification step:** Compare supplement eTable 10's UK-ROX column with both corresponding rows for each metric in eTable 5 and the main-text Oxygen Exposure paragraph; determine whether higher-group SpO2 should be 95.1% or whether eTable 10 should explicitly specify that SpO2 alone is restricted to periods receiving oxygen.
