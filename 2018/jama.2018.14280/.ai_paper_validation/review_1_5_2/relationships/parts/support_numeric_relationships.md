# Support Numeric Relationship Inventory (Provisional IDs)

Provisional IDs `UN001` onward are support numeric/reporting relationships; coordinator assigns canonical N IDs. All source locations are direct PDF pages and fresh layout evidence paths are given where a dense grid is the complete transcription.

| ID | Source / exact scope | Relationship, rule, and matched key |
|---|---|---|
| UN001 | DOC-002 pp.17-19; DOC-003 pp.10-11 | Planned total 952 = 476 per arm after 20% expansion; before expansion 397 per arm. Rule: planned total is sum of arm targets. Key `sample_size_952`. |
| UN002 | DOC-002 pp.20-23; DOC-003 pp.7-8 | Randomized low 4-6 and higher/intermediate 8-10 mL/kg PBW; male/female PBW formulas; protocol thresholds/timepoints. Rule: label/arm/scale identity. Key `ventilator_settings_days0_3`. |
| UN003 | DOC-002 pp.26-30; DOC-003 pp.8-9 | Primary VFD day-28 population/time definition and secondary outcome schedule/units. Rule: same primary endpoint requires same 28-day/alive/24-consecutive-hour definition. Key `VFD_day28_all_randomized`. |
| UN004 | DOC-002 p.48 | ARDS and scale definitions: PaO2/FiO2 bands and PEEP requirement; APACHE/SAPS/MRC ranges. Rule: threshold and unit identity. Key `ARDS_definition`. |
| UN005 | DOC-004 p.5/eTable1 | All-mode ventilatory rows (N, VT, RR, MV, plateau, PEEP, driving pressure, FiO2, PaO2/FiO2, PaCO2, pHa, pHa<7.25, acidosis) at four timepoints. Rule: printed numerator/denominator percent and median/IQR ordering. Key `ventilator_settings_days0_3`. |
| UN006 | DOC-004 p.6/eTable2; fresh layout text p.6 | Mode-stratified VT/RR/MV/pressure/PEEP/driving-or-PS at four timepoints for VC, PS, Other. Rule: mode-cell sums can be compared to eTable1 only after matching timepoint and measure; exact printed `8 (5-1)` retained. Key `ventilator_settings_mode_strata`. |
| UN007 | DOC-004 p.7/eTable3; fresh layout text p.7 | Mode-stratified FiO2, PaO2/FiO2, PaCO2, pH, pH<7.25, acidosis at four timepoints for VC, PS, Other. Rule: count percentage uses its stated ABG denominator; `---` is an uncomputed P cell, not display-zero P. Key `ABG_mode_strata`. |
| UN008 | DOC-004 p.8/eTable4 | Co-intervention rows: treatment N 477/484; stated count/total % and median(IQR) values, including fluid/blood product denominators 454/464. Rule: percent should reconcile with printed numerator/denominator under rounding. Key `eTable4_cointerventions`. |
| UN009 | DOC-004 p.9/eTable5 | Subgroup VFD means±SD, low-minus-intermediate mean difference/95% CI, and subgroup interaction P. Rule: point estimate direction must match displayed group means subject to rounding. Key `subgroup_VFD`. |
| UN010 | DOC-004 p.10/eFigure1 | Cumulative percent free from ventilation by VFD 0-28, low/intermediate curves. Rule: graphical arm/axis identity. Key `VFD_day28_all_randomized`. |
| UN011 | DOC-004 pp.11-13/eFigures2-4 | VT distributions in VC and PS; PS-level distribution in PS. Rule: graphical distributions contain no printed numeric result to reconcile. Key `ventilator_settings_days0_3`. |
| UN012 | DOC-005 p.1 | Data availability “No”; no result-relevant numeric relationship. Rule: documented no-applicable scope. |
