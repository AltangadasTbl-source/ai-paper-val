# Canonical Inferential-Statistical Relationship Inventory

Stable `S` IDs cover every mapped inferential relationship. Related unclustered, clustered, protocol-planned, interim, and time-to-event records are retained as separate model/source relationships and explicitly cross-referenced. No relationship contains a displayed `P = 0` or equivalent; therefore no `DISPLAY_ZERO_NOT_CANDIDATE` classification is presently required.

| ID | Canonical statistical relationship | Exact source scope | Supplied compatibility context |
|---|---|---|---|
| S001 | Primary unclustered 96% vs 82%, difference 14% (8-20), P<.001 | DOC-001 pp. 1, 5, 7 | Difference in proportions; chi-square; two-sided alpha .05 |
| S002 | Overall unclustered 98% vs 87%, difference 11% (7-14), P<.001 | DOC-001 pp. 1, 5, 7 | Binary-outcome rule |
| S003 | No-difficult-airway 99% vs 92%, difference 8% (4-12), P<.001, interaction .36 | DOC-001 pp. 5, 7 | Binary outcome; subgroup interaction |
| S004 | Difficult-airway success without hypoxemia 82% vs 69%, difference 12% (3-21), P=.006, interaction .61 | DOC-001 p. 7 | Binary outcome |
| S005 | Difficult-airway duration 39 vs 40 s, difference -1 (-6 to 3), P=.50, interaction .17 | DOC-001 p. 7 | Hodges-Lehmann/continuous convention |
| S006 | All-patient success without hypoxemia 85% vs 77%, difference 8% (3-14), P=.003 | DOC-001 p. 7 | Binary outcome |
| S007 | All-patient duration 38 vs 36 s, printed difference `1 (4 to -1)`, P=.24 | DOC-001 p. 7 | Continuous outcome display |
| S008 | Blood/vomit subgroup 95% vs 82%, difference 13% (3-23), P=.01, interaction .31 | DOC-001 p. 7 | Unplanned subgroup |
| S009 | Cervical-immobilization subgroup 100% vs 78%, difference 22% (9-36), P=.001, interaction .25 | DOC-001 p. 7 | Unplanned subgroup |
| S010 | Obesity subgroup 96% vs 75%, difference 21% (10-33), P=.001, interaction .63 | DOC-001 p. 7 | Unplanned subgroup |
| S011 | C-MAC subgroup 98% vs 88%, difference 11% (7-14), P<.001, interaction .46 | DOC-001 p. 7 | Unplanned subgroup |
| S012 | Cormack-Lehane grade 1-4 estimates, CIs, P values, and interaction values | DOC-001 p. 7 | Unplanned subgroup; four level-specific rows |
| S013 | Actual-first-device result 98% vs 87%, difference 10% (7-14), P<.001 | DOC-001 p. 7 | Footnote-defined analysis population |
| S014 | Successful-first-attempt duration 38 vs 34 s, difference 4 (2-7), P<.001, interaction .03 | DOC-001 p. 7 | Post hoc subgroup |
| S015 | Difficult-airway time-to-success log-rank P=.02 and Cox HR 1.29 (1.04-1.60) | DOC-001 pp. 5, 8 | Unadjusted Cox; ETT reference; PH not upheld |
| S016 | All-patient time-to-success log-rank P=.12 and HR 1.12 (0.97-1.30) | DOC-001 p. 5; DOC-003 p. 4 | Unadjusted Cox; ETT reference; PH not upheld; supplement repeats HR/CI |
| S017 | All Table 2 process-measure differences, CIs, and P values | DOC-001 p. 6 | Stated binary/continuous methods and printed row labels |
| S018 | All Table 5 complication differences, CIs, and P values | DOC-001 p. 9 | Binary comparison context |
| S019 | Sample-size target 374, 80% power, 9-point difference, 95% vs 86%, two-sided alpha .05 | DOC-001 p. 3; DOC-002 p. 19 | Planning relationship; STATA command supplied in protocol |
| S020 | Interim futility analysis and absence of superiority alpha adjustment | DOC-001 p. 4; DOC-002 p. 21; DOC-003 p. 6 | Planned futility-only decision context |
| S021 | Exploratory interaction tests and no multiple-comparison correction | DOC-001 pp. 3-4 | Unplanned subgroup model label |
| S022 | Post hoc physician-clustering analysis reported as not materially changing results | DOC-001 pp. 3, 5; DOC-003 pp. 2-3 | Cluster-adjusted supplement is the comparator |
| S023 | Table 3/Figure 2 time definitions, HR direction, and ETT reference | DOC-001 pp. 7-8 | Scale/reference/model-label relationship |
| S024 | Remaining Table 5 P values including .99 and .08 | DOC-001 p. 9 | Binary comparison context; no display zero |
| S025 | Clustered primary difference 14% (7-21), P<.001, interaction .35 | DOC-003 p. 2 | Physician-cluster adjustment; compare S001/S022 |
| S026 | Clustered difficult-airway success without hypoxemia 12% (2-22), P=.015, interaction .61 | DOC-003 p. 2 | Physician-cluster adjustment; compare S004/S022 |
| S027 | Clustered difficult-airway duration -1 s (-6 to 3), P=.31, interaction .17 | DOC-003 p. 2 | Physician-cluster adjustment; compare S005/S022 |
| S028 | Clustered all-patient success 11% (6-15), P<.001 | DOC-003 pp. 2-3 | Physician-cluster adjustment; interaction not applicable; compare S002 |
| S029 | Clustered all-patient success without hypoxemia 8% (2-15), P=.02 | DOC-003 pp. 2-3 | Physician-cluster adjustment; compare S006 |
| S030 | Clustered all-patient duration 1 s (-1 to 4), P=.95 | DOC-003 pp. 2-3 | Physician-cluster adjustment; compare S007 |
| S031 | Cluster method: displayed treatment columns unchanged; difference/P/interaction recalculated; ICC <.001 (CI <.001-.03), upper bound used | DOC-003 p. 3 | Model-definition and label consistency |
| S032 | Supplement all-patient Kaplan-Meier HR 1.12 (0.97-1.30) with PH assumption not upheld | DOC-003 p. 4 | Exact HR/CI repetition included in S016; caption/model label check |
| S033 | Protocol formal-analysis plan: two-sided alpha .05 and planned summary/CI conventions | DOC-002 p. 19 | Planned method; compare reported methods |
| S034 | Protocol primary chi-square analysis in difficult-airway subset and secondary all-enrolled analysis | DOC-002 p. 20 | Planned population/test labels |
| S035 | Protocol sample-size command and assumptions | DOC-002 p. 19 | `sampsi 0.95 0.86, p(0.8)`; compare S019 |
| S036 | Protocol interim rule after 500, projection to 1000, equal allocation, +15-point capped assumption, futility stop if no difference | DOC-002 p. 21; DOC-003 p. 6 | Planned rule repeated in supplement; compare S020 |
| S037 | Interim observed n=507, 250/257 vs 213/250, and reported decision not to stop | DOC-003 p. 6 | Observed interim result under S036 rule |

Pass 1 and pass 2 must each explicitly cover `S001` through `S037`, including relationships that yield no candidate or cannot be mechanically reconciled because a named model definition is absent.

Final statistical coverage status: `PASS_1_COMPLETE` and `PASS_2_COMPLETE` for every relationship `S001` through `S037`, as documented in the two distinct checker artifacts.
