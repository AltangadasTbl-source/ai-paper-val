# Canonical Statistical Relationship Inventory

This is the complete inferential-statistical union with continuous IDs. Each row retains the complete shard-local record as provenance, including exact source, population, time, contrast, model/test label, values, missing inputs, and check rule. These are mapped relationships, not candidates or adjudications.

| Global ID | Relationship, required matching controls | Exact provenance and later check rule | Pass status |
|---|---|---|---|
| S001 | Primary ITT NI: BMV-ETI .11%, one-sided 97.5% CI -1.64% to infinity, margin -1%, P=.11. | `main_statistical.md` MS001; DOC-001 pp.1/3-4; apply stated lower-limit rule and CI convention. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S002 | Hierarchical centre-random-effect primary model: .05%, one-sided 97.5% CI -1.70% to infinity. | MS002; DOC-001 p.4; retain endpoint, ITT, model, CI, and margin labels. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S003 | PP NI: 4.3%/4.2%, .08%, one-sided 97.5% CI -1.74% to infinity, P=.12. | MS003; DOC-001 p.4; apply PP-only NI rule. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S004 | ITT day-28 survival difference .1%, 95% CI -1.8 to 2.1, P=.90. | MS004; DOC-001 pp.1/4/6; check CI ordering, containment, population, and time. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S005 | ITT hospital-admission survival difference -3.7%, 95% CI -7.7 to .3, P=.07. | MS005; DOC-001 pp.1/4/6; check direction and matched narrative/table values. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S006 | ITT ROSC difference -4.7%, 95% CI -8.8 to -.5, P=.03. | MS006; DOC-001 pp.4/6; check population, direction, and containment. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S007 | ITT CPC-distribution P=.68. | MS007; DOC-001 p.6; P attaches to the distribution; primary success is CPC 1+2. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S008 | PP survival, admission, and ROSC estimates, CIs, and P values. | MS008; DOC-001 p.6; preserve PP population and each outcome-specific direction. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S009 | PP CPC-distribution P=.76. | MS009; DOC-001 p.6; verify distribution and population labels. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S010 | Airway-management difficulty difference 4.7%, 95% CI 1.5-7.9, P=.004. | MS010; DOC-001 pp.1/4/6; match safety denominator and direction. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S011 | Airway-management failure difference 4.6%, 95% CI 2.8-6.4, P<.001. | MS011; DOC-001 pp.1/4/6; threshold is not display zero. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S012 | Gastric-regurgitation difference 7.7%, 95% CI 4.9-10.4, P<.001. | MS012; DOC-001 pp.1/4/6; threshold is not display zero. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S013 | Table 3 P values use chi-square or Fisher exact tests. | MS013; DOC-001 p.6; do not infer the row-specific test. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S014 | Secondary rate and quantitative analysis family, two-sided .05, no multiplicity adjustment. | MS014; DOC-001 p.3; match outcome type and keep OR and difference CIs distinct. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S015 | Post-hoc CCF: BMV 86%, ETI 87%, difference -1%, CI -4% to 2%, P=.70. | MS015; DOC-001 p.4; check BMV-minus-ETI direction and containment. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S016 | Post-hoc pauses >2 seconds: 27 vs 16, difference 11 seconds, CI 7-15, P<.001. | MS016; DOC-001 p.4; check unit/measure label and interval containment. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S017 | NI design: 80% power, 956/group, 3%/2%, 1% margin; later interpretation. | MS017; DOC-001 pp.3/7-8; keep planned inputs distinct from observed results. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S018 | Protocol V1.3 NI contrast, 95% two-sided CI, and lower-limit >-0.01 rule. | `support_001_statistical.md` S1S001; DOC-002 pp.11/36-37. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S019 | Protocol V1.3 permits exact rather than asymptotic CI if necessary. | S1S002; DOC-002 pp.11/36; no method-specific result supplied. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S020 | Protocol V1.3 H0/H1 at the -0.01 boundary. | S1S003; DOC-002 p.36; retain printed inequality convention. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S021 | Difference test planned after demonstration of NI. | S1S004; DOC-002 p.36; alpha/test details absent. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S022 | Secondary rates use chi-square and 95% CIs for ORs and differences. | S1S005; DOC-002 pp.11/37; keep effect measures distinct. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S023 | Quantitative outcomes use t test or Mann-Whitney by distribution. | S1S006; DOC-002 pp.11/37; planned choice only. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S024 | Interim analyses at 50% and 75% for futility/sample-size recalculation. | S1S007; DOC-002 pp.11/36; stopping threshold absent. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S025 | Protocol sample-size assumptions: 3%/2%, 1% margin, 956/group, power .8, alpha .025, 2000, 5000 simulations. | S1S008; DOC-002 pp.11/37; planned inputs only. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S026 | NI main analyses use both ITT and PP populations. | S1S009; DOC-002 p.36; retain analysis-set definitions. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S027 | Safety/dichotomized endpoints use chi-square and 95% OR CI. | S1S010; DOC-002 p.37; planned rule only. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S028 | Prognostic factors use multivariable logistic regression. | S1S011; DOC-002 p.37; covariates/estimand absent. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S029 | Missing primary endpoint in ITT is no success; conditional sensitivity/multiple imputation. | S1S012; DOC-002 p.37; retain missing-data scope. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S030 | Randomization stratified by centre and blocked within centre. | S1S013; DOC-002 pp.17/37; block size absent. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S031 | Planned software SAS 9.2. | S1S014; DOC-002 p.37; software definition only. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S032 | Protocol V1.4 NI contrast/rule and exact-CI condition. | `support_002_statistical.md` S2S001; DOC-002 p.66; match ITT, contrast, margin, and confidence. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S033 | Protocol V1.4 H0/H1 and post-NI difference test. | S2S002; DOC-002 p.90; retain boundary and strictly-greater decision wording. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S034 | Repeated primary ITT 95% CI and lower-limit >-0.01 rule. | S2S003; DOC-002 p.91; match day-28 CPC<=2 endpoint. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S035 | Secondary rate criteria use chi-square and CIs for ORs/differences. | S2S004; DOC-002 p.66; effect measures distinct. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S036 | Repeated secondary chi-square and CI plan. | S2S005; DOC-002 p.91; endpoint-specific model absent. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S037 | Quantitative secondary criteria use t test or Mann-Whitney. | S2S006; DOC-002 pp.66/91; outcome-specific choice absent. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S038 | Interim analyses at 50% and 75% using ADDPLAN. | S2S007; DOC-002 pp.66/91; no alpha-spending boundary supplied. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S039 | Repeated sample-size design quantities and 5000 simulations. | S2S008; DOC-002 p.92; planned inputs only. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S040 | NI analyses use both ITT and PP. | S2S009; DOC-002 p.91; major-violation classification absent. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S041 | Safety analysis and exploratory logistic regression rules. | S2S010; DOC-002 p.92; covariates/model details absent. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S042 | ITT missing primary=no success; conditional sensitivity/multiple imputation. | S2S011; DOC-002 p.92; distinguish observed and imputed outcomes. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S043 | Randomization stratified by centre and blocked. | S2S012; DOC-002 pp.72/92; no block sizes supplied. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S044 | External background 40/120 vs 69/573, P<0.0001. | S2S013; DOC-002 p.67; non-CAAM and not display zero. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S045 | External background 2.9%/367837 vs 1.0%/41972. | S2S014; DOC-002 p.67; observational, non-CAAM result. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S046 | SAP trial design and H0/H1 at -0.01. | `support_003_statistical.md` S3S001; DOC-002 pp.119-121; native text controls over OCR errors. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S047 | SAP sample-size plan: 3%/2%, 1% margin, 956/group, .8 power, .025 alpha, 2000, 5000 simulations. | S3S002; DOC-002 p.120; planned relationship only. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S048 | SAP ITT/PP/AT and missing-data definitions. | S3S003; DOC-002 pp.121/123-124; match analysis set and missing rule. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S049 | SAP primary and secondary endpoint definitions. | S3S004; DOC-002 p.122; preserve outcome/time/scale. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S050 | SAP continuous/categorical summaries and one-decimal rounding rules. | S3S005; DOC-002 p.123; nonmissing denominator=100%. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S051 | SAP primary two-sided 95% CI NI rule for ITT/PP/AT. | S3S006; DOC-002 p.124; exact/asymptotic choice conditional. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S052 | SAP secondary/safety test families, alpha .05, and SAS 9.4. | S3S007; DOC-002 p.124; do not infer row-specific method. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S053 | eTable 1 centre contributions BMV N=1018 and ETI N=1022. | S3S008; DOC-003 p.2; arithmetic/rounding, no inferential statistic. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S054 | eTable 2 post-hoc exclusion result 43/971 vs 39/978, P=.63, difference .4, CI -2.2 to 1.3. | S3S009; DOC-003 p.3; row-specific test/CI method absent. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S055 | eTable 2 post-hoc reclassification result 41/863 vs 45/1174, P=.31, difference .9, CI -.9 to 2.7. | S3S010; DOC-003 p.3; row-specific test/CI method absent. | PASS_1_COMPLETE; PASS_2_COMPLETE |

## Cross-source statistical overlap map

S001-S003 must be compared to the matched protocol/SAP framework in S018-S031, S032-S045, and S046-S052 only after matching population, endpoint, time, contrast, CI sidedness, and model. The protocol repeats of the NI rule, sample-size basis, interim schedule, ITT/PP definition, and missing-data convention are genuine duplicates and are retained as cross-provenance rather than treated as independent trial results. S054-S055 match the SAP on primary endpoint and BMV-minus-TI direction, but their post-hoc denominators prohibit arithmetic substitution from S053 or main ITT totals.

## Explicit two-pass mapping status and limitations

**Total statistical relationships: 55 (S001-S055, no gaps).** Shard totals: main 17, support-001 14, support-002 14, support-003 10. Every canonical record carries `PASS_1_COMPLETE` and `PASS_2_COMPLETE`; unsupplied model/test details remain identified in the source mapping and pass artifacts. No source displays `P=0`/`p=0.000`; `P<.001` and `P<.0001` are thresholds, not display-zero records. DOC-002 p.134 is empty and provides no statistical relationship.
