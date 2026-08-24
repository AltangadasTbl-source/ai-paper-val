# Support numeric relationship inventory part

Provisional support numeric keys; all remain mapping records, not candidates. Locations use supplied PDF pages.

| Key | Exact locations | Relationship / values / match key |
|---|---|---|
| UN001 | DOC-002 pp. 10-11; DOC-003 pp. 2-3 | Sample-size chronology: 748 (374/group) from 30% vs 40%, RR .75, 80%, alpha .05, 5% dropout; revised first-618 observation, .20 control, 1912 plus 5%=2013; 90 centers x >=24. `sample_size_randomized` |
| UN002 | DOC-002 pp. 10, 29; DOC-005 pp. 18,22 | Eligibility: BMI >=35 kg/m2, ARISCAT >=26, surgery >=2 h; ARISCAT score components/coefficients/points and score threshold. `ARISCAT_eligibility` |
| UN003 | DOC-002 pp. 12-15; DOC-005 pp. 18-20,23 | Intervention contrast: PEEP 4 versus 12 cmH2O; tidal volume 7 mL/kg PBW/IBW; PBW sex formulas; FiO2 >=.4, SpO2 targets, 35-45-mmHg end-tidal CO2, recruitment/rescue numeric sequences. `assigned_peep` |
| UN004 | DOC-002 pp. 12,19-20,31-33; DOC-005 pp. 20-21 | Endpoint component and threshold definitions: 5-day PPC, oxygenation thresholds, BP/HR thresholds, VAS<3, transfusion/Hct/Hb criteria, PEPC criteria. `primary_PPC_definition` |
| UN005 | DOC-002 pp. 34; DOC-004 pp. 1-3 | Follow-up timepoints days 1-5/discharge/day 90 and final mITT/complete-case/subgroup definition. `analysis_population_time` |
| UN006 | DOC-005 p.24 | eTable3 all fluid counts, percentages, mean(SD) amounts and P values, high n989/low n987. `intraoperative_fluids` |
| UN007 | DOC-005 p.25 | eTable4 vasoactive drug use/counts/percentages, mg mean(SD), P values, high n989/low n987. `vasoactive_drugs` |
| UN008 | DOC-005 p.26 | eTable5 anesthetic, analgesic, paralytic, reversal count/percentage and P values, high n989/low n987. `anesthetic_agents` |
| UN009 | DOC-005 p.27 | eTable6 surgery priority, position, wound class count/percentages and intraabdominal pressure mmHg mean(SD), P values. `surgery_characteristics` |
| UN010 | DOC-005 p.28 | eTable7 VAS dyspnea/thoracic/abdominal rest/incident, cm mean(SD), daily N and P values days 1-5. `postoperative_pain_dyspnea` |
| UN011 | DOC-005 p.29 | Per-protocol high n917/low n912: all PPC-component counts, denominators, percentages, effect estimate, CI and P. `per_protocol_PPC` |
| UN012 | DOC-005 p.30 | mITT high n989/low n987: random effect, event count, common-effect, interaction, average-relative-effect sensitivity results. `primary_PPC_sensitivity` |
| UN013 | DOC-005 pp.31-37 | Figure quantity definitions: enrollment Z, tidal volume, PEEP, peak pressure, SpO2, driving pressure formula, FiO2; exact plotted coordinates unavailable. `ventilation_figure_series` |
| UN014 | DOC-005 p.38 | Time-to-PPC 21.3%/23.6%, follow-up 4(2-5), HR .88 (.73-1.06), P=.190, Schoenfeld .05. `time_to_PPC_5d` |
| UN015 | DOC-005 p.39 | Time-to-severe PPC 11.7%/13.6%, HR .85 (.66-1.09), P=.197, Schoenfeld .28. `time_to_severe_PPC_5d` |
| UN016 | DOC-005 p.40 | Time-to-PEPC 16.9%/15.2%, HR 1.12 (.89-1.39), P=.314, Schoenfeld .67. `time_to_PEPC_5d` |
| UN017 | DOC-005 p.41 | Caption/result pairing: text says extra-pulmonary complications; values/HR label says 5-d mortality, .5%/.3%, HR1.67(.40-6.97), P=.484, Schoenfeld .14. `time_to_mortality_5d` |
| UN018 | DOC-006 p.1 | Data/code availability administrative only; no numeric outcome data supplied. |

**Numeric-inventory count:** 18 provisional relationship records, including 12 observed-result numeric records (UN006-UN017), 5 definitions/design records, and 1 administrative no-result record. Complete detail is in `extraction/support_quantitative_evidence.md`.
