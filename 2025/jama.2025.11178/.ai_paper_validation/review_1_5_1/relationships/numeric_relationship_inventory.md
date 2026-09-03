# Numeric relationship inventory

Stable IDs below cover every numeric, denominator, proportion, count, scale, label, formula, workbook-value, planned-definition, and no-applicable relationship in the canonical extraction. `Source record` is the lossless source transcription/provenance route in `support_quantitative_evidence.md` and the named shard. Records consolidate only same printed statements/values with the same meaning; planned and observed records remain distinct.

| ID | Relationship group / exact scope | Source record and linked statistical IDs |
|---|---|---|
| N001 | Main randomized population, allocation, dates and abstract baseline summary | Main N001; S002 |
| N002 | Main abstract primary adjusted percentages/RRs | Main N002; S002 |
| N003 | Eligibility, PEG and BPI scale/threshold definitions | Main N003/N005; protocol support-001 N001/N025/N026 |
| N004 | Main randomization/strata/block-size definition | Main N004; S001 |
| N005 | PROMIS and PGIC scale/direction/cut-point definitions | Main N006; DOC-005 R01-R06 |
| N006 | Main planned sample/power quantities | Main N007; S001 |
| N007 | Main screening/enrollment counts | Main N008/N011 |
| N008 | Main follow-up, adherence, sessions, withdrawals/deaths and analysis Ns | Main N009/N012/N013; DOC-005 R08/R12/R14 |
| N009 | Main baseline Table 1 demographics | Main N014 |
| N010 | Main baseline Table 1 race/residence/SDOH | Main N015 |
| N011 | Main baseline Table 1 pain/treatment/conditions | Main N016 |
| N012 | Main baseline Table 1 health/outcomes and denominator qualifiers | Main N017/N018 |
| N013 | Main safety/adverse-event counts | Main N019 |
| N014 | Main Figure 2 observed assessment Ns | Main N020; S002-S010 |
| N015 | Protocol version/history item-count, timing-window, site-encounter and surgery-exclusion definitions | support-001 N001-N007 |
| N016 | Protocol enrollment/randomization targets and three-arm/dose/assessment definitions | support-001 N008-N023 |
| N017 | Protocol outcome, population, subgroup, mediator and economic matching keys | support-001 N024-N036 |
| N018 | Protocol operational/interview sample quantities and delivery timing | support-002 N-SUP002-04/05 |
| N019 | Protocol MCID, secondary-outcome, economic endpoint/formula definitions | support-002 N-SUP002-01/02/03 |
| N020 | SAP document/amendment and planned target/arm/intervention population definitions | support-003 N-SAP-001 to N-SAP-006 |
| N021 | SAP subgroup cutpoints, economic/cost and safety definitions | support-004 SAP-D3-R01/R02/R10-R12 |
| N022 | TIDieR dose, training thresholds, outreach and fidelity quantities | support-004 TIDIER-D4-R01 to R05 |
| N023 | DOC-005 outcome scales, MCID and clinical cutpoints | support-004 RES-D5-R01 to R06 |
| N024 | DOC-005 observed missingness/observation-pattern denominators and follow-up totals | support-004 RES-D5-R08/R12/R14 |
| N025 | DOC-005 covariate-selection and model covariate sets | support-004 RES-D5-R10/R15 |
| N026 | DOC-005 imputation, weighted-estimator and weight-distribution quantitative inputs | support-004 RES-D5-R09/R11/R13/R16/R18 |
| N027 | DOC-005 complete-case/worst-best sensitivity denominators/percentages and subset denominators | support-004 RES-D5-R19 to R21; S057-S061 |
| N028 | DOC-005 eTable 9 binary n/N/% triplets and RR labels | support-005 PDF p15; S062-S070 |
| N029 | DOC-005 eTable 10 median/IQR and unadjusted difference values | support-005 PDF p16; S071-S085 |
| N030 | DOC-005 eTable 11 raw-score median/IQR and difference values | support-005 PDF pp17-18; S086-S106 |
| N031 | DOC-006 workbook title, column denominators, flags, P-value labels and notes | support-005 cells A1:J4, A110:J114 |
| N032 | DOC-006 worksheet clinical-site and demographic displayed counts/percentages | support-005 A4:J48 |
| N033 | DOC-006 worksheet clinical-characteristic displayed values and missing counts | support-005 A49:J94 |
| N034 | DOC-006 worksheet baseline primary/secondary displayed values and missing counts | support-005 A95:J109 |
| N035 | DOC-006 cached/displayed P values and no-formula status | support-005 H12:J108; linked S107-S109 |
| N036 | Direct-source no-applicable support units | support-001 through support-005 coverage/no-applicable tables |

## Coverage statement

N001-N036 is a sequential, complete numeric inventory for the complete direct-source union declared in `extraction/support_quantitative_evidence.md`. Within-group atomic values are intentionally retained in their lossless source component and exact PDF/cell provenance is never replaced by this grouping index. No candidate selection or diagnosis was performed.
