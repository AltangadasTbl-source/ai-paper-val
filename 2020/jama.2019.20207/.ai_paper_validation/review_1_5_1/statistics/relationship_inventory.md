# Canonical Statistical Relationship Inventory

Stable IDs retain all provisional source provenance. They are statistical/reporting relationships only; no candidate ID or adjudication is assigned.

| Stable ID | Relationship | Locations and provisional provenance | Linked numeric ID |
|---|---|---|---|
| S001 | Observed main TTP Cox/log-rank framework and composite primary result: HR .96 (.75-1.24), P=.76; adjusted .97 (.76-1.25), P=.84; 24-month KM percentages/difference. | DOC-001 pp.1,5-6 M-S001,M-S002,M-S006,M-S009 | N013 |
| S002 | Main biopsy-only sensitivity: HR 1.40 (.79-2.46), P=.24; Figure-2 panel-B log-rank P=.24. | DOC-001 pp.5-6 M-S006,M-S009 | N013 |
| S003 | Main/SAP/protocol initial sample-size design: two-sided alpha .05, N=418, >=80% power, 20%/10%, 57 events, HR 2.1/2.118, target 464. | DOC-001 p.3 M-S003; DOC-002 p.40 P2-S004; DOC-003 p.3 P3-S002 | N008 |
| S004 | Main analysis populations/models: KM/log-rank/Cox, 3-stratum adjustment, ITT support, proportional-hazards check, shared frailty and biopsy-only sensitivity. | DOC-001 pp.3-4 M-S004; DOC-003 pp.3-6 P3-S003-P3-S006 | N029 |
| S005 | Main repeated diet/carotenoid linear mixed-model definition, categorical time/group interaction, contrasts, likelihood-ratio/Wald, missing-at-random, two-sided P<=.05. | DOC-001 pp.4,7 M-S005,M-S011-M-S015; DOC-004 p.2 P3-S015 | N017 |
| S006 | Main active-treatment comparisons: Fisher exact P=.75; time-to-treatment HR 1.38 (.39-4.90), P=.61. | DOC-001 p.5 M-S007 | N014 |
| S007 | Main plasma-carotenoid mixed-model contrast: difference .10 (.02-.18) log-umol/L, P=.01. | DOC-001 p.6 M-S010 | N015 |
| S008 | MEAL pilot Table-1/2 footnote significance definitions, total carotenoid P=.02, and other stated P<.05 changes. | DOC-002 pp.12-13 P1-S002-P1-S005 | N020,N021 |
| S009 | Protocol/SAP PSADT derivation and progression analysis: log(2)/LS slope log PSA, log-rank/Cox, censoring, eligible/ITT sensitivity. | DOC-002 pp.28,41 P1-S006,P2-S005-P2-S008; DOC-003 pp.1-6 P3-S001,P3-S004-P3-S007 | N006,N007,N029 |
| S010 | Protocol primary/secondary planned endpoints and assessment timepoint definitions. | DOC-002 pp.15,25,29 P1-S007,P1-S008 | N023 |
| S011 | Protocol correlative biomarker planned models: Cox PFS, allocation/interaction, lasso score; carotenoid t-test/regression/Cox plans. | DOC-002 pp.38-41 P2-S002,P2-S003,P2-S011,P2-S014 | N024,N026 |
| S012 | Protocol planned QOL/diet longitudinal models: t test/linear regression, GEE, t tests at 12/24, Bang-Jung-George adjustment. | DOC-002 pp.34,41 P2-S001,P2-S009,P2-S010 | N025 |
| S013 | Interim superiority/futility plan: .0025 interim/.025 final one-sided alpha; 4-5 interims; P>=.5 or statistic <0 futility. | DOC-002 p.42 P2-S012 | N027 |
| S014 | Adaptive sample-size calculation: if control PGR<20%, HR .472, two-sided .05/80%; 18% example 466 eligible. | DOC-002 p.42 P2-S013 | N027 |
| S015 | SAP QOL Wilcoxon plans by instrument/timepoint, two-sided 5%, no multiplicity; interactions 15%, missing-data rule. | DOC-003 pp.7-8 P3-S008-P3-S013 | N025,N030 |
| S016 | SAP instrument scales/direction and DOC-004 eFigure descriptive plotting definition. | DOC-003 p.10 P3-S014; DOC-004 p.3 P3-S016 | N018,N025 |
| S017 | DOC-004 eTable P-value semantics: `*` within group follow-up vs baseline; `†` intervention-change vs control-change; mixed-model analysis. | DOC-004 p.2 P3-S015 | N017 |

## Cross-source/definition observations for later statistical passes

1. The protocol’s HR 2.118 and recalculation HR .472 are reciprocal under reversed arm orientation; preserve reference groups.
2. Interim P=.5/sign wording is not the .0025 rejection boundary and needs definition-aware review, not arithmetic comparison alone.
3. Planned SAP/protocol quantities are not observed estimates. Main Kaplan-Meier percentages, Cox HRs, and log-rank P values must remain distinct.
4. No source has a display-zero P value; `DISPLAY_ZERO_NOT_CANDIDATE` is therefore not applicable.

## Statistical pass completion matrix

| Relationship | Pass 1 | Pass 2 |
|---|---|---|
| S001 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S002 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S003 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S004 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S005 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S006 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S007 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S008 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S009 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S010 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S011 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S012 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S013 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S014 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S015 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S016 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S017 | PASS_1_COMPLETE | PASS_2_COMPLETE |
