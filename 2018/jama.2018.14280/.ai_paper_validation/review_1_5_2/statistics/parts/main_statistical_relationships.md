# Main inferential-statistical relationship inventory — DOC-001

Provisional `MS` IDs are mapper-local. “Pass-ready” records include every main-paper displayed statistical comparison and its supplied analysis rule. They are not candidate determinations.

| ID | Result and exact printed statistic | Comparator/rule supplied by source | Locations | Cross-source key |
|---|---|---|---|---|
| MS001 | VFD day 28: MD −0.27, 95% CI −1.74 to1.19, P=.71; n=475/480 | t test, 95% superiority CI; abstract/table/narrative repeat | pp.1,5-6 | OUT:VFD28 |
| MS002 | VFD stratification-variable sensitivity analysis P=.72 | GLMM with hospital and intubation location random effects; narrative says consistent | p.6 | OUT:VFD28-sensitivity |
| MS003 | Days ventilation in survivors: MD −0.56, CI −1.61 to0.49, no P shown | Table 2 contrast; analysis definition not separately stated for this row | p.6 | OUT:vent-days-survivors |
| MS004 | ICU stay Table 2: MD 0.39, CI −1.09 to1.89, P=.58 | inverse-Gaussian GLM per table footnote | pp.1,6 | OUT:ICU-stay-table |
| MS005 | ICU-stay Figure 2: HR 0.94, CI 0.80-1.09, P=.41; Schoenfeld P=.21 | Cox proportional hazards/Kaplan-Meier; table and curve estimands differ | pp.6-7 | OUT:ICU-stay-curve |
| MS006 | Hospital stay Table 2: MD −0.60, CI −3.52 to2.31, P=.68 | inverse-Gaussian GLM per table footnote | pp.1,6 | OUT:hospital-stay-table |
| MS007 | Hospital-stay Figure 2: HR 1.02, CI 0.87-1.19, P=.83; Schoenfeld P=.82 | Cox proportional hazards/Kaplan-Meier; table and curve estimands differ | pp.6-7 | OUT:hospital-stay-curve |
| MS008 | ICU mortality: RR 1.11, CI 0.96-1.27, P=.15 | Table footnote labels ICU mortality RR despite methods narrative saying mortality rates reported as HR/Cox; binary-outcome rule is Wald LR CI + chi-square P | p.6 | OUT:mortality-ICU |
| MS009 | Hospital mortality: RR 1.06, CI 0.93-1.22, P=.35 | Same Table 2/footnote binary rule | p.6 | OUT:mortality-hospital |
| MS010 | 28-day mortality: HR 1.12, CI 0.90-1.40, P=.30 | Cox proportional hazard, abstract/table repeat | pp.1,6 | OUT:mortality-28 |
| MS011 | 90-day mortality: HR 1.07, CI 0.87-1.31, P=.54 | Cox; abstract/table/Fig2B repeat; Figure Schoenfeld P=.13 | pp.1,6-7 | OUT:mortality-90 |
| MS012 | ARDS: RR 0.86, CI 0.59-1.24, P=.38 | Wald LR CI plus chi-square P; abstract/table repeat | pp.1,6 | OUT:ARDS |
| MS013 | Pneumonia: RR 1.07, CI 0.78-1.47, P=.67 | Wald LR CI plus chi-square P; abstract/table repeat | pp.1,6 | OUT:pneumonia |
| MS014 | Pneumothorax: RR 1.16, CI 0.73-1.84, P=.55 | Wald LR CI plus chi-square P; abstract/table repeat | pp.1,6 | OUT:pneumothorax |
| MS015 | Atelectasis: RR 1.00, CI 0.81-1.23, P=.94 | Wald LR CI plus chi-square P; abstract/table repeat | pp.1,6 | OUT:atelectasis |
| MS016 | Extrapulmonary infection: RR 0.84, CI 0.60-1.18, P=.28 | Wald LR CI plus chi-square P | p.6 | OUT:infection |
| MS017 | Extrapulmonary sepsis: RR 0.87, CI 0.56-1.33, P=.50 | Wald LR CI plus chi-square P | p.6 | OUT:sepsis |
| MS018 | Delirium: RR 1.15, CI 0.99-1.34, P=.06 | Wald LR CI plus chi-square P | p.6 | OUT:delirium |
| MS019 | Need tracheostomy: RR 1.03, CI 0.84-1.26, P=.78 | Wald LR CI plus chi-square P | p.6 | OUT:tracheostomy |
| MS020 | Figure 2A free-from-invasive-ventilation HR 0.99, CI 0.86-1.14, P=.92; Schoenfeld P=.68 | Cox/Kaplan-Meier curve; endpoint distinct from VFD t-test | p.7 | FIG:VFD-curve |
| MS021 | Location subgroup: MD −2.50 (IQR −4.63 to−0.36) inside vs 1.45 (IQR −0.52 to3.43) outside; interaction P=.01 | Prespecified exploratory subgroup GLM with Gaussian distribution; intervals printed as IQR | p.6 | OUT:subgroup-intubation-location |
| MS022 | Analysis methods: mixed-effect longitudinal models for tidal-volume-over-time with hospital/patient random intercepts; time continuous | Detailed numerical estimates are in DOC-004 eTables/eFigures, not this paper | p.4 | MODEL:ventilator-time-series |
| MS023 | All primary/secondary significance P values stated two-sided, alpha .05, no multiple-comparison adjustment; secondary/exploratory | global interpretation rule | p.4 | P:two-sided |
