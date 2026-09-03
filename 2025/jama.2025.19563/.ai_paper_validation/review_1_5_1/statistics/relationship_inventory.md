# Statistical Relationship Inventory — Canonical 1.5.1

## Scope, pass requirements, and identity rule

This inventory enumerates every 34 mapper-level inferential or formal statistical relationship. Every row requires PASS_1_COMPLETE and PASS_2_COMPLETE downstream. Exact source, printed values/statements, population, contrast, time point, model/test/interval, direction, scale, and prerequisites are retained through the provisional key in the current mapping part; unavailable inputs are stated rather than inferred.

| Stable ID | Provisional key | Exact source location | Relationship and checker-required fields |
|---|---|---|---|
| S001 | M-S001 | DOC-001 pp. 1,4 | Primary ITT binomial-regression RD; AI minus human; one-sided 95% lower bound; margin -15 pp; missing 12-month visits=failure. |
| S002 | M-S002 | DOC-001 p.4 | Sample-size assumptions: 15-point margin, 80% power, one-sided alpha .05, 276 analyzable and 368 target with 25% attrition. |
| S003 | M-S003 | DOC-001 p.4 | Statistical-analysis and five sensitivity families; component binomial models; chi-square families; descriptive secondary CIs/P values. |
| S004 | M-S004 | DOC-001 pp.1,4,7 | Primary RD -0.2 pp, one-sided lower bound -8.2, compared with -15 pp noninferiority margin. |
| S005 | M-S005 | DOC-001 p.7 | Component one-sided 95% CIs are descriptive; no multiplicity adjustment/formal hypothesis test. |
| S006 | M-S006 | DOC-001 p.4 | Chi-square comparisons: initiation P=.001 and completion P=.008. |
| S007 | M-S007 | DOC-001 p.4 | Incident A1C >=6.5% chi-square family and P=.78 narrative. |
| S008 | D2A-S001 | DOC-002 pp.6,15-16 | Planned binary primary endpoint/noninferiority objective; margin/test/CI/population absent in this slice. |
| S009 | D2B-S001 | DOC-002 pp.36-37 | Planned 15-pp noninferiority relation, 50% success, alpha/power/n/attrition, one-sided 95% CI criterion; formula convention absent. |
| S010 | D2B-S002 | DOC-002 pp.37-39 | Planned ITT/per-protocol populations; logistic/linear/mixed models and covariate sensitivities; no coefficients. |
| S011 | D2B-S003 | DOC-002 pp.38-39 | PA missingness >5% triggers MI; complete-case sensitivity needs 100% valid PA. |
| S012 | D2B-S004 | DOC-002 p.39 | Cost-effectiveness horizons, 3% discount, Markov/QALY/ICER and sensitivity; no observed economic result. |
| S013 | D3A-S001 | DOC-003 p.8 | Device-discordance threshold stated outside 95% CI; no statistic/P value. |
| S014 | D3A-S002 | DOC-003 p.28 | Age-adjusted RD, one-sided 95% CI, AI minus Human, randomized 12-month endpoints, -15 pp line. |
| S015 | D3A-S003 | DOC-003 p.28 | Exploratory subgroup RDs, one-sided 95% CIs, -15 pp line, no multiplicity adjustment. |
| S016 | D3A-S004 | DOC-003 p.29 | Chi-square proportions and Wilcoxon rank-sum continuous measures for eTable 4. |
| S017 | D3A-S005 | DOC-003 p.29 | Chi-square outside-window proportions and Wilcoxon days-outside-window comparison. |
| S018 | D3A-S006 | DOC-003 p.29 | Chi-square prohibited-medication-proportion comparison. |
| S019 | D3A-S007 | DOC-003 p.30 | Twenty MICE data sets combined under MAR with Rubin's rules. |
| S020 | D3B-S01 | DOC-003 p.34 | Age-adjusted primary/component RDs and one-sided CIs; randomized 12-month; AI minus Human; -15 pp. |
| S021 | D3B-S02 | DOC-003 p.35 | Exploratory subgroup primary RDs and one-sided CIs; unadjusted/no multiplicity; -15 pp. |
| S022 | D3B-S03 | DOC-003 pp.39-40 | Baseline-table age P=.014 and other-characteristics P>.05; summary-statistic conventions. |
| S023 | D3B-S04 | DOC-003 p.41 | Eligibility-table claim of no significant differences; test/statistic/exact P absent. |
| S024 | D3B-S05 | DOC-003 pp.42-43 | Site-table P values (age .017; race/marital/education/MVPA <.001) and repeated footnote. |
| S025 | D3B-S06 | DOC-003 pp.44-45 | Baseline-A1C subgroup site P=.024 and ethnicity P=.018; other P>.05. |
| S026 | D3B-S07 | DOC-003 pp.46-47 | Completer/dropout baseline-table significance wording and p<.05 statement. |
| S027 | D3B-S08 | DOC-003 p.51 | Attendance/outside-window comparisons; 12-month days P=.016, other P>.05; windows/denominators supplied. |
| S028 | D3B-S09 | DOC-003 p.52 | Medication proportions 6/183 vs 7/185, P=.793, table labels Wilcoxon Rank Sum Test. |
| S029 | D3B-S10 | DOC-003 pp.53-54 | Per-protocol baseline age P=.010, sex P=.041, other P>.05. |
| S030 | D3B-S11 | DOC-003 p.58 | Per-protocol binary RDs with one-sided bounds; population and component denominators supplied. |
| S031 | D3B-S12 | DOC-003 p.59 | MICE primary sensitivity: pooled percentages, RD and one-sided lower bound. |
| S032 | D3B-S13 | DOC-003 p.60 | Pattern-mixture sensitivity: arm values, RD/lower bound, stated noncompleter assumptions. |
| S033 | D3C-S01 | DOC-003 p.61 | Best-case/all-attainment sensitivity RDs with one-sided lower bounds and PA assumptions. |
| S034 | D3C-S02 | DOC-003 p.62 | Cluster-robust RDs/lower bounds under two stated cluster rules. |

## Statistical coverage controls

- Population is randomized/ITT unless per-protocol, subgroup, completer/dropout, or plan scope is stated.
- RDs are percentage points and generally AI/dDPP minus human/hDPP; one-sided entries contain a lower bound, not a reconstructed two-sided interval.
- Protocol plans are distinct from reported results; later comparisons must match definition, population, time, and model.
- No display-zero P value is mapped.
- No candidate conclusion, severity, validity, or adjudication occurs in this inventory.

## Pass-2 completion register

This canonical inventory update records the independent pass-2 completion state. The detailed direct-source rationale, missing-definition notes, and stable-candidate cross-references are in `checkers/statistical_pass_2.md`; these labels do not adjudicate any candidate.

| Stable ID | Pass-2 state | Result / cross-lane context |
|---|---|---|
| S001 | PASS_2_COMPLETE | NO_NEW_CANDIDATE; C001 context |
| S002 | PASS_2_COMPLETE | NO_NEW_CANDIDATE |
| S003 | PASS_2_COMPLETE | NO_NEW_CANDIDATE |
| S004 | PASS_2_COMPLETE | NO_NEW_CANDIDATE |
| S005 | PASS_2_COMPLETE | NO_NEW_CANDIDATE |
| S006 | PASS_2_COMPLETE | NO_NEW_CANDIDATE |
| S007 | PASS_2_COMPLETE | NO_NEW_CANDIDATE |
| S008 | PASS_2_COMPLETE | NO_NEW_CANDIDATE_MISSING_DEFINITION; C001 context |
| S009 | PASS_2_COMPLETE | NO_NEW_CANDIDATE_MISSING_DEFINITION; C001 context |
| S010 | PASS_2_COMPLETE | NO_NEW_CANDIDATE_MISSING_DEFINITION; C001 context |
| S011 | PASS_2_COMPLETE | NO_NEW_CANDIDATE |
| S012 | PASS_2_COMPLETE | NO_NEW_CANDIDATE_MISSING_DEFINITION |
| S013 | PASS_2_COMPLETE | NO_NEW_CANDIDATE_MISSING_DEFINITION |
| S014 | PASS_2_COMPLETE | NO_NEW_CANDIDATE |
| S015 | PASS_2_COMPLETE | NO_NEW_CANDIDATE |
| S016 | PASS_2_COMPLETE | NO_NEW_CANDIDATE |
| S017 | PASS_2_COMPLETE | NO_NEW_CANDIDATE |
| S018 | PASS_2_COMPLETE | NO_NEW_CANDIDATE; C006 context |
| S019 | PASS_2_COMPLETE | NO_NEW_CANDIDATE; C007 context |
| S020 | PASS_2_COMPLETE | NO_NEW_CANDIDATE |
| S021 | PASS_2_COMPLETE | NO_NEW_CANDIDATE |
| S022 | PASS_2_COMPLETE | NO_NEW_CANDIDATE; C004 context |
| S023 | PASS_2_COMPLETE | NO_NEW_CANDIDATE_MISSING_DEFINITION |
| S024 | PASS_2_COMPLETE | NO_NEW_CANDIDATE; C004 context |
| S025 | PASS_2_COMPLETE | NO_NEW_CANDIDATE; C004 context |
| S026 | PASS_2_COMPLETE | NO_NEW_CANDIDATE; C004 and C005 context |
| S027 | PASS_2_COMPLETE | NO_NEW_CANDIDATE |
| S028 | PASS_2_COMPLETE | NO_NEW_CANDIDATE; C006 context |
| S029 | PASS_2_COMPLETE | NO_NEW_CANDIDATE |
| S030 | PASS_2_COMPLETE | NO_NEW_CANDIDATE |
| S031 | PASS_2_COMPLETE | NO_NEW_CANDIDATE; C007 context |
| S032 | PASS_2_COMPLETE | NO_NEW_CANDIDATE |
| S033 | PASS_2_COMPLETE | NO_NEW_CANDIDATE |
| S034 | PASS_2_COMPLETE | NO_NEW_CANDIDATE |
