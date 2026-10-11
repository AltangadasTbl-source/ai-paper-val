# Statistical Relationship Inventory — Pass 1

## Scope and method

This inventory covers every inferential relationship mapped in the canonical main and support evidence maps: DOC-001 pp. 1-11, DOC-002 pp. 1-25, and DOC-003 pp. 1-167. Direct supplied-PDF text was used to confirm the main Table 2/Figures 1-3 and DOC-002 Tables S6-S11. No legacy candidate, verifier, quality, or report artifact was read.

`PASS_1_COMPLETE` means the listed point-estimate/interval containment, endpoint order, direction, measure/scale label, matched repetition, and any source-defined inferential compatibility checks were completed. It is not a validity decision or adjudication. `DIAGNOSTIC ONLY` marks an approximation or calculation that cannot replace the supplied analysis.

## Stable statistical relationships

| S ID | Source relationship and exact location | Pass-1 check outcome | Status |
|---|---|---|---|
| S001 | Main primary analysis definition: KM/log-rank, Cox HR/95% CI; DOC-001 p. 4 | Model, contrast, measure, CI level and unadjusted-centre label mapped; used as definition for matched primary result. | PASS_1_COMPLETE |
| S002 | Schoenfeld proportional-hazards test P=.12; DOC-001 p. 4 | Test and P printed; statistic/df not supplied, so no numerical reconstruction. | PASS_1_COMPLETE — MISSING_DEFINITION(statistic, df) |
| S003 | mRS generalized OR/Wilcoxon-Mann-Whitney and multiplicity definition; DOC-001 p. 4 | OR scale and favourable-direction convention agree with Table 2 footnote. Exact WMW statistic/variance not supplied. | PASS_1_COMPLETE — MISSING_DEFINITION(test statistic, variance) |
| S004 | Primary composite HR 0.32 (0.16-0.63), P<.001; DOC-001 pp. 1,5,8-10 | HR lies within ordered positive CI; HR<1 and narrative direction agree; abstract/table/figures/conclusion repeat compatibly. Log-rank P and Cox CI are distinct stated analyses, so no exact P-from-CI test. | PASS_1_COMPLETE |
| S005 | 30-d stroke/death HR 2.05 (0.62-6.81), P=.24; DOC-001 p. 8 | Containment/order/direction compatible. Diagnostic log-HR/CI approximation gives two-sided tail near .24; exact compatibility is not asserted because the row P test is not named. | PASS_1_COMPLETE — DIAGNOSTIC ONLY |
| S006 | Post-hoc qualifying-artery stroke HR 0.05 (0.01-0.39); DOC-001 p. 8 | Containment/order/direction and post-hoc label compatible; no row P supplied. | PASS_1_COMPLETE |
| S007 | Post-hoc revascularization HR 0.14 (0.04-0.47); DOC-001 p. 8 | Containment/order/direction and post-hoc label compatible; no row P supplied. | PASS_1_COMPLETE |
| S008 | 90-d target-territory stroke/death HR 0.72 (0.27-1.88), P=.49; DOC-001 p. 8 | Containment/order/direction compatible; exact P/CI compatibility unavailable because the row P test is not named. | PASS_1_COMPLETE — MISSING_DEFINITION(row P test) |
| S009 | 90-d outside-territory stroke P=.15, HR NA; DOC-001 p. 8 | NA HR agrees with a zero-event comparison; P test is unnamed. | PASS_1_COMPLETE — MISSING_DEFINITION(row P test) |
| S010 | 90-d mRS generalized OR 1.21 (1.03-1.38), P=.01; DOC-001 p. 8 | Ordered positive CI contains OR; >1 favourable BA direction agrees with footnote/narrative. Diagnostic log-OR/CI tail is near .01; test-specific compatibility not asserted. | PASS_1_COMPLETE — DIAGNOSTIC ONLY |
| S011 | 1-y target-territory stroke/death HR 0.35 (0.16-0.78), P=.01; DOC-001 p. 8 | Containment/order/direction compatible; row P test not named. | PASS_1_COMPLETE — MISSING_DEFINITION(row P test) |
| S012 | 1-y revascularization HR 0.16 (0.06-0.47), P<.001; DOC-001 p. 8 | Containment/order/direction compatible; row P test not named. | PASS_1_COMPLETE — MISSING_DEFINITION(row P test) |
| S013 | 1-y outside-territory stroke: incidence difference -0.4% (-2.4 to -1.7), HR 0.76 (0.17-3.40), P=.72; DOC-001 p. 8 | The displayed incidence difference is outside its displayed CI; see Proposal SP-01. HR/CI/P separately have compatible direction but row P test is unnamed. | PASS_1_COMPLETE — PROPOSAL SP-01 |
| S014 | 1-y mRS generalized OR 1.26 (1.06-1.45), P=.01; DOC-001 p. 8 | Ordered positive CI contains OR; >1 favourable BA convention agrees with footnote/narrative. Diagnostic log-OR/CI tail is near .01. | PASS_1_COMPLETE — DIAGNOSTIC ONLY |
| S015 | 1-y combined vascular events HR 0.38 (0.19-0.80), P=.01; DOC-001 p. 8 | Containment/order/direction compatible; row P test not named. | PASS_1_COMPLETE — MISSING_DEFINITION(row P test) |
| S016 | Narrative repetitions of secondary HR/OR results; DOC-001 p. 5 and p. 8 | All cited estimate/CI/P occurrences repeat Table 2 without a cross-location discrepancy. | PASS_1_COMPLETE |
| S017 | Centre-adjusted HR 0.32 (0.16-0.62), P=.001; interaction P=.10; removal-of-revascularization HR 0.39 (0.18-0.85), P=.01; DOC-001 p. 6 | Main text agrees with DOC-002 Tables S6, S7, and S10 for estimates/P values. Population headers in those tables are independently assessed in S033-S045. | PASS_1_COMPLETE |
| S018 | Disabling-stroke P=.02; DOC-001 p. 6 | Direction agrees with DOC-002 Table S11 counts and P. Chi-square label is supplied in support table; no conflict identified. | PASS_1_COMPLETE |
| S019 | Figure 2 overall primary HR 0.32 (0.16-0.63); DOC-001 p. 7 | Matches S004/S031 in estimate, CI, comparison, and direction. | PASS_1_COMPLETE |
| S020 | Figure 2 age subgroups and interaction P=.26; DOC-001 p. 7 | Each HR lies in ordered positive CI; group directions and interaction label are compatible. Interaction-model coefficients/df unavailable. | PASS_1_COMPLETE — MISSING_DEFINITION(interaction statistic, df) |
| S021 | Figure 2 sex subgroups and interaction P=.50; DOC-001 p. 7 | Containment/order/direction/label compatible; interaction statistic/df unavailable. | PASS_1_COMPLETE — MISSING_DEFINITION(interaction statistic, df) |
| S022 | Figure 2 hypertension subgroups and interaction P=.53; DOC-001 p. 7 | Containment/order/direction/label compatible; interaction statistic/df unavailable. | PASS_1_COMPLETE — MISSING_DEFINITION(interaction statistic, df) |
| S023 | Figure 2 diabetes subgroups and interaction P=.99; DOC-001 p. 7 | Containment/order/direction/label compatible; interaction statistic/df unavailable. | PASS_1_COMPLETE — MISSING_DEFINITION(interaction statistic, df) |
| S024 | Figure 2 smoking subgroups and interaction P=.46; DOC-001 p. 7 | Containment/order/direction/label compatible; interaction statistic/df unavailable. | PASS_1_COMPLETE — MISSING_DEFINITION(interaction statistic, df) |
| S025 | Figure 2 eGFR subgroups and interaction P=.95; DOC-001 p. 7 | Containment/order/direction/units compatible; interaction statistic/df unavailable. | PASS_1_COMPLETE — MISSING_DEFINITION(interaction statistic, df) |
| S026 | Figure 2 stenosis subgroups and interaction P=.74; DOC-001 p. 7 | Containment/order/direction/threshold label compatible; interaction statistic/df unavailable. | PASS_1_COMPLETE — MISSING_DEFINITION(interaction statistic, df) |
| S027 | Figure 2 BMI subgroups and interaction P=.17; DOC-001 p. 7 | Containment/order/direction compatible; figure combines BMI >=25, whereas the SAP has three planned BMI levels. This is a source-definition difference, not a matched-result contradiction because the final grouping/model is not supplied. | PASS_1_COMPLETE — MISSING_DEFINITION(final subgroup-model specification) |
| S028 | Figure 2 hypoperfusion subgroups and interaction P=.99; DOC-001 p. 7 | HR/CI compatible for “Yes”; NA HR is explained by zero AMM events for “No.” | PASS_1_COMPLETE |
| S029 | Figure 2 circulation subgroups and interaction P=.26; DOC-001 p. 7 | Containment/order/direction/label compatible; interaction statistic/df unavailable. | PASS_1_COMPLETE — MISSING_DEFINITION(interaction statistic, df) |
| S030 | Figure 2 TIA/stroke subgroups and interaction P=.67; DOC-001 p. 7 | Containment/order/direction/label compatible; interaction statistic/df unavailable. | PASS_1_COMPLETE — MISSING_DEFINITION(interaction statistic, df) |
| S031 | Figure 3 primary HR 0.32 (0.16-0.63), P<.001; DOC-001 p. 9 | Exact repetition of S004/S019, including direction. | PASS_1_COMPLETE |
| S032 | Figure 3 post-hoc landmark HRs 2.05 (0.62-6.81) and 0.10 (0.03-0.31); DOC-001 p. 9 | CIs ordered and contain estimates; early HR matches S005. Landmark selection/model details beyond crossing at 30 d are not supplied. | PASS_1_COMPLETE — MISSING_DEFINITION(landmark analysis specification) |
| S033 | DOC-002 Table S6 centre-adjusted primary HR 0.32 (0.16-0.62), P=.001; p. 19 | HR/CI/direction repeat S017. BA 9 (3.9) does not reconcile with stated n=249 (9/249=3.6% to one decimal); see SP-02. | PASS_1_COMPLETE — PROPOSAL SP-02 |
| S034 | DOC-002 Table S7 site interaction HRs and P=.10; p. 20 | Site HRs contain their CIs and interaction P matches S017. The printed group header totals 233/238 while site patient totals sum to 501; see SP-03. | PASS_1_COMPLETE — PROPOSAL SP-03 |
| S035 | DOC-002 Table S8 PPS primary HR 0.27 (0.13-0.56), P<.001; p. 21 | Ordered CI contains HR. PPS headers 249/252 conflict with the same table’s n(%) and Figure 1/Table S10 PPS denominators; see SP-04. | PASS_1_COMPLETE — PROPOSAL SP-04 |
| S036 | DOC-002 Table S8 PPS 30-d component HR 1.55 (0.44-5.49); p. 21 | CI contains HR; P not printed. Header/population inconsistency is SP-04. | PASS_1_COMPLETE — PROPOSAL SP-04 |
| S037 | DOC-002 Table S8 PPS qualifying-artery stroke HR 0.06 (0.01-0.41); p. 21 | CI contains HR; P not printed. Header/population inconsistency is SP-04. | PASS_1_COMPLETE — PROPOSAL SP-04 |
| S038 | DOC-002 Table S8 PPS revascularization HR 0.15 (0.04-0.50); p. 21 | CI contains HR; P not printed. Header/population inconsistency is SP-04. | PASS_1_COMPLETE — PROPOSAL SP-04 |
| S039 | DOC-002 Table S9 ATS primary HR 0.32 (0.16-0.64), P=.001; p. 22 | Ordered CI contains HR. ATS headers 249/252 conflict with Table S10 ATS denominators and the table’s n(%); see SP-05. | PASS_1_COMPLETE — PROPOSAL SP-05 |
| S040 | DOC-002 Table S9 ATS 30-d component HR 2.09 (0.63-6.92); p. 22 | CI contains HR; P not printed. Header/population inconsistency is SP-05. | PASS_1_COMPLETE — PROPOSAL SP-05 |
| S041 | DOC-002 Table S9 ATS qualifying-artery stroke HR 0.05 (0.01-0.39); p. 22 | CI contains HR; P not printed. Header/population inconsistency is SP-05. | PASS_1_COMPLETE — PROPOSAL SP-05 |
| S042 | DOC-002 Table S9 ATS revascularization HR 0.14 (0.04-0.47); p. 22 | CI contains HR; P not printed. Header/population inconsistency is SP-05. | PASS_1_COMPLETE — PROPOSAL SP-05 |
| S043 | DOC-002 Table S10 ITT post-hoc HR 0.39 (0.18-0.85), P=.01; p. 23 | CI contains HR; text S017 repeats it. | PASS_1_COMPLETE |
| S044 | DOC-002 Table S10 PPS post-hoc HR 0.32 (0.14-0.75), P=.01; p. 23 | CI contains HR; PPS N=233/238 agrees with Figure 1, and is the comparator for SP-04. | PASS_1_COMPLETE |
| S045 | DOC-002 Table S10 ATS post-hoc HR 0.40 (0.19-0.86), P=.02; p. 23 | CI contains HR; ATS N=247/254 is the comparator for SP-05. | PASS_1_COMPLETE |
| S046 | DOC-002 Table S11 overall SAE P=.84, chi-square; p. 24 | Counts/percentages and named test supplied; no incompatibility found. | PASS_1_COMPLETE |
| S047 | Table S11 nervous-system disorders P=.35, chi-square; p. 24 | Counts/percentages and named test supplied; no incompatibility found. | PASS_1_COMPLETE |
| S048 | Table S11 symptomatic ICH P=.37, Fisher exact; p. 24 | Counts/percentages and named test supplied; no incompatibility found. | PASS_1_COMPLETE |
| S049 | Table S11 asymptomatic ICH P=.12, Fisher exact; p. 24 | Counts/percentages and named test supplied; no incompatibility found. | PASS_1_COMPLETE |
| S050 | Table S11 any ICH P=.07, Fisher exact; p. 24 | Counts/percentages and named test supplied; no incompatibility found. | PASS_1_COMPLETE |
| S051 | Table S11 disabling stroke P=.02, chi-square; p. 24 | Counts/percentages and named test supplied; matches main narrative S018. | PASS_1_COMPLETE |
| S052 | Table S11 vascular/lymphatic disorder P=.62, Fisher exact; p. 24 | Counts/percentages and named test supplied; no incompatibility found. | PASS_1_COMPLETE |
| S053 | Table S11 metabolic/nutritional disease P=1.00, Fisher exact; p. 24 | Counts/percentages and named test supplied; no incompatibility found. | PASS_1_COMPLETE |
| S054 | Table S11 infection P=.50, Fisher exact; p. 24 | Counts/percentages and named test supplied; no incompatibility found. | PASS_1_COMPLETE |
| S055 | Table S11 operations P=.25, Fisher exact; p. 24 | Counts/percentages and named test supplied; no incompatibility found. | PASS_1_COMPLETE |
| S056 | Table S11 respiratory disorder P=1.00, Fisher exact; p. 24 | Counts/percentages and named test supplied; no incompatibility found. | PASS_1_COMPLETE |
| S057 | Table S11 gastrointestinal disorder P=1.00, Fisher exact; p. 24 | Counts/percentages and named test supplied; no incompatibility found. | PASS_1_COMPLETE |
| S058 | Table S11 injury/poisoning P=1.00, Fisher exact; p. 24 | Counts/percentages and named test supplied; no incompatibility found. | PASS_1_COMPLETE |
| S059 | Table S11 tumour/cyst/polyp P=.50, Fisher exact; p. 24 | Counts/percentages and named test supplied; no incompatibility found. | PASS_1_COMPLETE |
| S060 | Table S11 reproductive/breast disease P=.50, Fisher exact; p. 24 | Counts/percentages and named test supplied; no incompatibility found. | PASS_1_COMPLETE |
| S061 | DOC-003 protocol V2.0 sample-size/log-rank assumptions; pp. 11-12 | Planning values are versioned assumptions, not observed results. Exponential model and log-rank label supplied, but hazard/accrual/censoring definitions incomplete. | PASS_1_COMPLETE — MISSING_DEFINITION(hazard, accrual, censoring) |
| S062 | DOC-003 interim alpha plan alpha1=.0015, alpha2=.024; pp. 11-12 | Historical/protocol definition only; no result-level comparison made. | PASS_1_COMPLETE |
| S063 | DOC-003 protocol analysis framework: KM/log-rank/Cox HR, mRS ordinal OR; p. 40 | Compatible with main labels; plan supplies no realised test statistics. | PASS_1_COMPLETE — MISSING_DEFINITION(realised statistic, variance) |
| S064 | DOC-003 protocol 802-case sample-size plan; pp. 40-41 | Historical plan; printed 12.2% x (1-50%) = 6.1% is arithmetically compatible. No sample-size equation is supplied. | PASS_1_COMPLETE — MISSING_DEFINITION(sample-size equation) |
| S065 | DOC-003 protocol interim alpha plan; p. 41 | Historical plan; version change separately tracked. | PASS_1_COMPLETE |
| S066 | DOC-003 prespecified subgroup definitions; p. 41 | Main Figure 2 labels align except final BMI grouping/model is not given; no inferential contradiction established. | PASS_1_COMPLETE — MISSING_DEFINITION(final subgroup model) |
| S067 | DOC-003 revised planning: 7%/15%, 80%, one-sided alpha 2.5%, 512; p. 69 | Planning arithmetic 256+256=512 and 15%-7%=8 points holds. Derived 53.3% relative reduction is diagnostic only. | PASS_1_COMPLETE — DIAGNOSTIC ONLY |
| S068 | DOC-003 protocol V2.3 framework KM/log-rank/Cox and mRS ordinal OR; p. 102 | Matches main measure/scale labels; realised test details not supplied. | PASS_1_COMPLETE — MISSING_DEFINITION(realised statistic, variance) |
| S069 | DOC-003 protocol V2.3 sample-size plan 15%/7%, one-sided alpha 2.5%, N=512; p. 103 | Versioned planning relationship, internally arithmetically coherent. | PASS_1_COMPLETE |
| S070 | DOC-003 protocol V2.3 planned subgroup definitions; p. 103 | Matches Figure 2 key labels; final analysis grouping/model not supplied. | PASS_1_COMPLETE — MISSING_DEFINITION(final subgroup model) |
| S071 | DOC-003 SAP v1/v2 primary KM/log-rank/Cox HR framework; pp. 139,159 | Matches S001/S004 model and measure labels. CI/P exact compatibility not checked because log-rank P and Cox CI are distinct analyses. | PASS_1_COMPLETE |
| S072 | DOC-003 SAP secondary time-to-event Cox HR/95% CI plans; pp. 141,161 | Main secondary HR labels/time windows compatible where aligned; later 24/36-month endpoints are unreported main outcomes. | PASS_1_COMPLETE |
| S073 | DOC-003 SAP mRS ordinal-logistic/common-OR plan; pp. 141,161 | Compatible with main generalized-OR label/direction, except main reports an assumption-free WMW-derived generalized OR after proportional-odds failure. This is an explicitly reported analysis change, not a contradiction. | PASS_1_COMPLETE |
| S074 | DOC-003 SAP restenosis logistic-regression OR/95% CI plan; pp. 141,161 | Main reports a rate but no corresponding OR/CI; no matched inferential output to compare. | PASS_1_COMPLETE — MISSING_DEFINITION(reported model output) |
| S075 | DOC-003 SAP EQ-5D t-test/Wilcoxon plan; pp. 141,162 | Main has P=.40 but does not name which allowed test was used; no exact reconstruction. | PASS_1_COMPLETE — MISSING_DEFINITION(selected test, statistic) |
| S076 | DOC-003 SAP safety Fisher-exact comparison plan; pp. 142,162 | Table S11 reports row-level Fisher/chi-square labels; no discrepancy established. Event-versus-person comparison basis is unspecified in SAP. | PASS_1_COMPLETE — MISSING_DEFINITION(event/person basis) |
| S077 | DOC-003 SAP medication chi-square/Fisher plan; pp. 142,162-163 | No matched inferential medication output is supplied. | PASS_1_COMPLETE — MISSING_DEFINITION(observed output, selected test) |
| S078 | DOC-003 SAP v1 interim plan; p. 165 | Explicitly historical side of v1/v2 revision table. | PASS_1_COMPLETE |
| S079 | DOC-003 SAP v2 no-interim rule; p. 165 | Explicitly revised rule; differs from S078 by stated SAP version, so not a contradiction. | PASS_1_COMPLETE |
| S080 | DOC-003 SAP v1/v2 sample-size assumptions; pp. 165-166 | Versioned assumptions are internally labelled and explain 802 versus 512; no observed-result contradiction. | PASS_1_COMPLETE |

**Pass-1 inventory total:** 80 stable S IDs (S001-S080), all explicitly `PASS_1_COMPLETE`.

## Pass-2 completion register

The independent pass-2 reconciliation is recorded in `checkers/statistical_pass_2.md`. Each row below updates the corresponding stable S record with `PASS_2_COMPLETE`; no new candidate proposal or disposition is assigned by this register.

| S ID | Pass-2 status |
|---|---|
| S001 | PASS_2_COMPLETE |
| S002 | PASS_2_COMPLETE |
| S003 | PASS_2_COMPLETE |
| S004 | PASS_2_COMPLETE |
| S005 | PASS_2_COMPLETE |
| S006 | PASS_2_COMPLETE |
| S007 | PASS_2_COMPLETE |
| S008 | PASS_2_COMPLETE |
| S009 | PASS_2_COMPLETE |
| S010 | PASS_2_COMPLETE |
| S011 | PASS_2_COMPLETE |
| S012 | PASS_2_COMPLETE |
| S013 | PASS_2_COMPLETE |
| S014 | PASS_2_COMPLETE |
| S015 | PASS_2_COMPLETE |
| S016 | PASS_2_COMPLETE |
| S017 | PASS_2_COMPLETE |
| S018 | PASS_2_COMPLETE |
| S019 | PASS_2_COMPLETE |
| S020 | PASS_2_COMPLETE |
| S021 | PASS_2_COMPLETE |
| S022 | PASS_2_COMPLETE |
| S023 | PASS_2_COMPLETE |
| S024 | PASS_2_COMPLETE |
| S025 | PASS_2_COMPLETE |
| S026 | PASS_2_COMPLETE |
| S027 | PASS_2_COMPLETE |
| S028 | PASS_2_COMPLETE |
| S029 | PASS_2_COMPLETE |
| S030 | PASS_2_COMPLETE |
| S031 | PASS_2_COMPLETE |
| S032 | PASS_2_COMPLETE |
| S033 | PASS_2_COMPLETE |
| S034 | PASS_2_COMPLETE |
| S035 | PASS_2_COMPLETE |
| S036 | PASS_2_COMPLETE |
| S037 | PASS_2_COMPLETE |
| S038 | PASS_2_COMPLETE |
| S039 | PASS_2_COMPLETE |
| S040 | PASS_2_COMPLETE |
| S041 | PASS_2_COMPLETE |
| S042 | PASS_2_COMPLETE |
| S043 | PASS_2_COMPLETE |
| S044 | PASS_2_COMPLETE |
| S045 | PASS_2_COMPLETE |
| S046 | PASS_2_COMPLETE |
| S047 | PASS_2_COMPLETE |
| S048 | PASS_2_COMPLETE |
| S049 | PASS_2_COMPLETE |
| S050 | PASS_2_COMPLETE |
| S051 | PASS_2_COMPLETE |
| S052 | PASS_2_COMPLETE |
| S053 | PASS_2_COMPLETE |
| S054 | PASS_2_COMPLETE |
| S055 | PASS_2_COMPLETE |
| S056 | PASS_2_COMPLETE |
| S057 | PASS_2_COMPLETE |
| S058 | PASS_2_COMPLETE |
| S059 | PASS_2_COMPLETE |
| S060 | PASS_2_COMPLETE |
| S061 | PASS_2_COMPLETE |
| S062 | PASS_2_COMPLETE |
| S063 | PASS_2_COMPLETE |
| S064 | PASS_2_COMPLETE |
| S065 | PASS_2_COMPLETE |
| S066 | PASS_2_COMPLETE |
| S067 | PASS_2_COMPLETE |
| S068 | PASS_2_COMPLETE |
| S069 | PASS_2_COMPLETE |
| S070 | PASS_2_COMPLETE |
| S071 | PASS_2_COMPLETE |
| S072 | PASS_2_COMPLETE |
| S073 | PASS_2_COMPLETE |
| S074 | PASS_2_COMPLETE |
| S075 | PASS_2_COMPLETE |
| S076 | PASS_2_COMPLETE |
| S077 | PASS_2_COMPLETE |
| S078 | PASS_2_COMPLETE |
| S079 | PASS_2_COMPLETE |
| S080 | PASS_2_COMPLETE |

**Pass-2 inventory total:** 80 stable S IDs (S001-S080), all explicitly `PASS_2_COMPLETE`; no new statistical candidate proposal.

## Pass-1 candidate proposals (no C IDs)

### SP-01 — Table 2 incidence-difference estimate is not contained in its printed interval

- **Potential category:** Statistical reporting inconsistency.
- **Exact source:** DOC-001, `jama_sun_2024_oi_240088_1746815064.14747.pdf#page=8`, Table 2, “Any stroke outside the territory of the qualifying artery within 1 y after enrollment.”
- **Direct observation:** The table prints incidence difference **-0.4%** and **95% CI, -2.4% to -1.7%**.
- **Rule:** A reported point estimate must lie within its reported interval; -0.4 is greater than the printed upper endpoint -1.7.
- **Human question:** Does either the incidence-difference point estimate or one CI endpoint contain a transcription/production error? The source does not supply an alternative value.

### SP-02 — Centre-adjusted table’s BA n(%) does not reconcile with its displayed denominator

- **Potential category:** Denominator, proportion, or total inconsistency.
- **Exact source:** DOC-002, `joi240088supp1_prod_1746815064.21247.pdf#page=19`, Table S6.
- **Direct observation:** Header: BA group **n=249**. Primary row: **9 (3.9)**.
- **Rule:** With the displayed header denominator, 9/249 = **3.6%** to one decimal, not 3.9%. The 3.9% display instead accords with a denominator near 233, but the table supplies no such BA denominator.
- **Human question:** Which denominator/population was used for the centre-adjusted table’s displayed n(%)? No model-based explanation is inferred.

### SP-03 — Site-interaction table presents incompatible analysis-population totals

- **Potential category:** Analysis-unit or population inconsistency.
- **Exact source:** DOC-002, `joi240088supp1_prod_1746815064.21247.pdf#page=20`, Table S7; comparator DOC-001 p. 5 Figure 1 and DOC-002 p. 23 Table S10.
- **Direct observation:** Table S7 headers identify BA **N=233** and AMM **N=238** (total 471), while its site “No. of patients” values are **256** and **245** (total 501). Figure 1 identifies 501 as the primary-analysis total and 233/238 as the per-protocol total.
- **Rule:** Within a table labelled as an analysis of the stated groups, the displayed population total must be identifiable and consistent with its header or explicitly distinguished.
- **Human question:** Are the site counts/percentages based on the 501 primary-analysis participants while the header is PPS, or is another population intended? The source does not name a distinct population for those columns.

### SP-04 — Per-protocol Table S8 headers conflict with its percentages and the supplied PPS denominators

- **Potential category:** Denominator, proportion, or total inconsistency.
- **Exact source:** DOC-002, `joi240088supp1_prod_1746815064.21247.pdf#page=21`, Table S8; comparators DOC-001 p. 5 Figure 1 and DOC-002 p. 23 Table S10.
- **Direct observation:** Table S8 is labelled “per-protocol population (PPS)” but headers say BA **n=249**, AMM **n=252**. Its primary counts **9 (3.9)** and **33 (13.9)** instead equal 9/233 and 33/238 to one decimal. Figure 1 and Table S10 explicitly give PPS **233/238**.
- **Rule:** A labelled population’s headers, its n(%), and an exact supplied population comparator should identify the same denominator unless a distinction is stated.
- **Human question:** Were Table S8’s headers intended to be 233/238, or does the table use another stated PPS definition? No correction is assigned.

### SP-05 — As-treated Table S9 headers conflict with its percentages and the supplied ATS denominators

- **Potential category:** Denominator, proportion, or total inconsistency.
- **Exact source:** DOC-002, `joi240088supp1_prod_1746815064.21247.pdf#page=22`, Table S9; comparator DOC-002 p. 23 Table S10.
- **Direct observation:** Table S9 is labelled “as-treated population (ATS)” with headers BA **n=249**, AMM **n=252**. Its primary counts **11 (4.5)** and **34 (13.4)** correspond to 11/247 and 34/254 to one decimal, and Table S10 expressly labels ATS **N=247/N=254**.
- **Rule:** A labelled population’s headers, its n(%), and an exact supplied ATS comparator should identify the same denominator unless a distinction is stated.
- **Human question:** Were Table S9’s headers intended to be 247/254, or is another ATS definition used? No correction is assigned.

## Limitations and exclusions

- The supplied sources do not give raw data, Cox-model coefficients/SEs, covariance matrices, degrees of freedom, exact interaction statistics, or the selected row-level P test for most Table 2 outcomes. No sidedness, variance estimator, model, estimand mapping, or multiplicity rule was inferred from convention.
- The log-scale P approximations in S005, S010, and S014 are labelled diagnostics only. They do not replace a source-defined test and do not establish a candidate.
- No `P = 0`, `p = 0.000`, or equivalent display-zero result occurs in the mapped inferential output; therefore the pass-1 display-zero count is 0. Had one been coherent, it would have been recorded as `DISPLAY_ZERO_NOT_CANDIDATE`, not proposed as a candidate.
- Versioned protocol/SAP differences (including the 802-to-512 and interim-analysis revisions) were preserved as versioned planning changes, not treated as result contradictions.
