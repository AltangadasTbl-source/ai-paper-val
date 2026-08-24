# Canonical Statistical Relationship Inventory

Complete fresh map: 58 relationships across DOC-001, DOC-002, and DOC-003. Disjoint stable ID blocks are S001-S031, S200-S215, and S400-S410; unused statistical IDs are intentionally unassigned. Every listed S ID requires both complete statistical passes.

**PASS_1_COMPLETE:** Every listed S relationship is explicitly complete in `checkers/statistical_pass_1.md`.

**PASS_2_COMPLETE:** Every listed S relationship is explicitly complete in `checkers/statistical_pass_2.md`.

# DOC-001 Statistical Relationship Inventory

All entries are source-extracted inferential relationships; no candidate conclusion is made here. `Loc` uses direct PDF page.

| ID | Statistical relationship | Loc |
|---|---|---|
| S001 | Design target: 80% power, alpha .05, 65% assumed mortality, 20-point ARR / 30.8% RR reduction at n=212; interim at 50% uses P<.001 and final two-sided P=.05. | p.3 |
| S002 | Primary mortality test: chi-square; 51/106 vs 34/103, RR 1.46 (95% CI 1.04-2.05), P=.03. | pp.1,5,7 |
| S003 | 28-day mortality: RR 1.48 (1.14-1.91), difference 21.6% (8.0%-35.3%), P=.002. | p.5 |
| S004 | SAPS-3 adjusted in-hospital mortality: RR 1.45 (1.04-2.02), P=.03. | p.5 |
| S005 | SAPS-3 adjusted 28-day mortality: RR 1.41 (1.08-1.84), P=.01. | p.5 |
| S006 | Time-to-event survival analysis is log-rank; Figure 2 P=.02. | pp.5-6 |
| S007 | Six-hour fluid: mean difference 1.2 L (1.0-1.5), P<.001; Table 2 agrees. | pp.1,4,6 |
| S008 | 24-hour fluid Table 2 P<.001. | p.6 |
| S009 | 72-hour fluid Table 2 P=.33. | p.6 |
| S010 | Dopamine first 6 h: 15 (14.2%) vs 2 (1.9%), Table P=.001; prose gives difference 12.3% (5.1%-19.4%), P<.001 (precision/display differs). | pp.1,4,6 |
| S011 | Dopamine during hospitalization Table 2 P=.004. | p.6 |
| S012 | Transfusion first 6 h Table 2 P=.48. | p.6 |
| S013 | Transfusion during hospitalization Table 2 P=.46. | p.6 |
| S014 | Time to antibiotics: 2.0 vs 1.5 h, P=.15. | pp.4,6 |
| S015 | SBP at 2 h Table 2 P=.09. | p.6 |
| S016 | DBP at 2 h Table 2 P=.99. | p.6 |
| S017 | SBP at 6 h Table 2 P=.95. | p.6 |
| S018 | DBP at 6 h Table 2 P=.82. | p.6 |
| S019 | Whole-blood lactate at 6 h Table 2 P=.25. | p.6 |
| S020 | Lactate change: mean difference 1.45 mmol/L (0.4-2.5), P=.02; Table 2 agrees. | pp.4,6 |
| S021 | Respiratory compromise: difference 13.5% (1.4%-25.7%), P=.03; Table 2 agrees. | pp.4,6 |
| S022 | Respiratory compromise resolved by 6 h Table 2 P=.02. | p.6 |
| S023 | Respiratory compromise persistent >6 h Table 2 P=.63. | p.6 |
| S024 | Hospital length of stay: 5 vs 7 days, P=.01. | p.5 |
| S025 | Subgroup HIV interaction P=.09; HIV-positive RR 1.57 (1.09-2.26), HIV-negative .75 (.23-2.44). | p.7 Fig 3 |
| S026 | Subgroup GCS interaction P=.01; RRs 1.92 (1.18-3.13), .97 (.46-2.07), .91 (.75-1.10). | p.7 Fig 3 |
| S027 | Subgroup hemoglobin interaction P=.99; RRs 1.37 (.82-2.29), 1.36 (.73-2.54). | p.7 Fig 3 |
| S028 | Subgroup SAPS-3 interaction P=.47; RRs 1.28 (.77-2.12), 1.65 (1.04-2.59). | p.7 Fig 3 |
| S029 | Subgroup lactate interaction P=.75; RRs 1.55 (.83-2.91), 1.38 (.91-2.08). | p.7 Fig 3 |
| S030 | Subgroup JVP interaction P=.29; RRs 1.75 (1.11-2.75), 1.22 (.73-2.01). | p.7 Fig 3 |
| S031 | Analysis methods link: parametric continuous t test; nonparametric Mann-Whitney; categorical chi-square; survival log-rank; subgroup interaction Mantel-Haenszel. | p.3 |

# DOC-002 Protocol Statistical Relationship Inventory

These are mapped definitions/plans or preliminary statistical displays. They have not been adjudicated as candidates. Each needs both statistical passes after ledger assembly.

| ID | PDF location | Statistic or compatible relationship | Role and check prerequisites |
|---|---|---|---|
| S200 | p4 | Planned Mantel-Haenszel comparisons for primary/secondary analysis; adjusted mortality via multivariable logistic regression. | Plan only; final model/population definitions needed for compatibility checking. |
| S201 | p9 | Original SSSP preliminary 6-h fluid mean 2.7 vs 1.8 L, p<0.001. | Preliminary distinct study; no test statistic/variance/analysis denominator supplied here. |
| S202 | p9 | Original SSSP preliminary mortality 68.6% vs 64.1%. | Preliminary distinct study; component event counts/model are not supplied for the matched comparison. |
| S203 | p15 | Continuous variables: mean (SD), t test/ANOVA; categorical: proportions, chi-square/Fisher exact/Mantel-Haenszel. | Prespecified analysis families and display rules. |
| S204 | p15 | Adjusted hazard ratios use SAPS3 quartiles; time-to-event uses Kaplan-Meier, log-rank, Cox model; p<0.05 declared significant. | Prespecified effect measure and threshold. |
| S205 | p15 | Sample-size plan: 65% expected control mortality, two-sided alpha=0.05, 80% power, n=212 for 20-percentage-point absolute reduction, 1:1 allocation. | Planning calculation; later check needs stated allocation loss/rounding convention. |
| S206 | p16 | Five planned subgroups; subgroup p threshold <0.01 stated as 0.05/5. | Arithmetic relation 0.05/5=0.01; planning threshold reconciles. |
| S207 | p16 | As-treated >=3 vs <3 L first 6 h, multivariable logistic regression adjusted for SAPS3 and infection site. | Prespecified nonrandomized contrast; final adjustment/model details required. |
| S208 | p19 | Multivariable sensitivity analysis uses directly measured ranges for microcost variables and 95% CIs for all-patient variables; Tornado diagram planned. | Economic sensitivity plan, no result/interval provided. |
| S209 | p20 | Diagnostic sample-size precision plan: TBASS n=233 under parent n=342 and 68% HIV prevalence; TB prevalence 20%; sensitivity 70% +/-13%; specificity 95% +/-3%. | Planning figures; verifies 342 x 0.68=232.56, consistent with rounded expected 233. Exact CI method not named. |
| S210 | p21 | Diagnostic-score logistic regression removes highest p>0.05 iteratively; retains p<0.05; sensitivity/specificity, ROC/AUC; evaluate 4-variable combinations if >4 remain. | Prespecified selection/performance rule; no result. |
| S211 | p21 | Xpert sensitivity, specificity, AUC, and kappa; any-site culture is primary truth standard. | Prespecified diagnostic-statistical definitions. |
| S212 | p23 | Interim analysis at enrollment midpoint, stop possible if arm superior at p<0.001. | Prespecified stopping rule; interim test, alpha spending, and sidedness not supplied. |
| S213 | p6-8 | Background external figures include 46/91 (50.5%), 36/161 (22.3%), and quoted percentages/ranges. | Context values only; not compatible with SSSP-2 inferential checks. |
| S214 | p9/Table 2 | Original SSSP table reports counts/percents and preliminary p<0.001; total n=76, arm headers 36/44, while narrative gives 89 enrolled and primary data 74. | Preserve identities and denominators for numeric/cross-source review; no inferential reconstruction from this page alone. |
| S215 | p24 | Planned budget has dollar and Kwacha component totals; no inferential statistic. | Arithmetic only; totals reconcile exactly, therefore no statistical inference applies. |

# DOC-003 Statistical Relationship Inventory Part — Support Results

Assigned ID range: `S400`-`S410`. Source: `DOC-003`, `joi170091supp2_prod.pdf`, PDF pp. 5, 7, and 9. This is a complete mapping record, not a candidate assessment. Every relationship requires both statistical passes downstream.

| ID | Exact location | Result / statistic | Population, contrast, model, and direction definition | Checkable supplied inputs / limitations |
|---|---|---|---|---|
| S400 | p. 9, eTable 4 row 1 | Unadjusted logistic primary analysis: OR 1.88, 95% CI 1.07-3.30, P=0.03. | n=209; in-hospital mortality; sepsis protocol versus usual care; received interventions and followed. OR>1 means higher death odds in protocol group. | OR, CI, P, n, contrast, and direction supplied. Test sidedness, SE, and exact coefficient absent. |
| S401 | p. 9, eTable 4 row 2 | Unadjusted logistic worst-case as-randomized: OR 1.75, 95% CI 1.00-3.04, P=0.047. | n=212; in-hospital mortality, protocol versus usual care; assumes 1 post-randomization-excluded protocol patient lived and 2 excluded usual-care patients died. | OR, CI, P, n, contrast, and explicit imputation supplied. Test sidedness/SE absent. |
| S402 | p. 9, eTable 4 row 3 | Adjusted logistic: OR 1.93, 95% CI 1.09-3.43, P=0.03. | n=209; in-hospital mortality, protocol versus usual care; adjusted for baseline SAPS-3 and lactate as continuous variables. | OR, CI, P, n, adjustment and direction supplied. Coefficients/SE/sidedness absent. |
| S403 | p. 9, eTable 4 row 4 | Unadjusted as-treated logistic: OR 1.45, 95% CI 0.83-2.54, P=0.20. | n=209; in-hospital mortality for >=3 L versus <3 L IV fluid in the six hours after ED registration. OR>1 direction is defined only in text as protocol-versus-usual-care; its applicability to this as-treated contrast should be interpreted from the stated >=3-L first comparator. | OR, CI, P, n, exposure threshold/time anchor supplied. Test sidedness/SE absent. |
| S404 | p. 9, eTable 4 row 5 | Adjusted as-treated logistic: OR 1.41, 95% CI 0.80-2.49, P=0.24. | n=209; same >=3 L versus <3 L contrast; adjusted for continuous SAPS-3 and suspected infection site. | OR, CI, P, n, contrast/time anchor and adjustments supplied. Test sidedness/SE absent. |
| S405 | p. 9, eTable 4 row 6 | Unadjusted Cox proportional hazards: HR 1.65, 95% CI 1.12-2.44, P=0.01. | n=209; survival, protocol versus usual care. HR>1 means shorter survival in protocol group. | HR, CI, P, n, contrast and direction supplied. Follow-up/censoring details, sidedness, and SE absent. |
| S406 | p. 9, eTable 4 row 7 | Adjusted Cox: HR 1.68, 95% CI 1.14-2.49, P=0.009. | n=209; survival, protocol versus usual care; baseline SAPS-3 continuous. HR>1 direction as supplied. | HR, CI, P, n, contrast/adjustment/direction supplied. Follow-up/censoring, sidedness, and SE absent. |
| S407 | p. 9, eTable 4 row 8 | Adjusted Cox: HR 1.69, 95% CI 1.14-2.51, P=0.001. | n=209; survival, protocol versus usual care; baseline SAPS-3 categorized by quartile. HR>1 direction as supplied. | HR, CI, P, n, contrast/adjustment/direction supplied. Follow-up/censoring, sidedness, and SE absent. |
| S408 | p. 7, eTable 2 footnote | Antimicrobials added/changed: 46/103 (44.7%) usual care versus 46/106 (43.4%) protocol; P>0.85. | Between-group comparison after admission and before discharge. | Counts, denominators, percentages, and threshold P supplied; named test and exact P absent. |
| S409 | p. 7, eTable 2 footnote | Antimicrobial change after culture-result availability: 0/103 (0.0%) versus 1/106 (0.9%); P>0.99. | Between-group comparison. | Counts, denominators, percentages, and threshold P supplied; named test and exact P absent. |
| S410 | p. 5, eMethods D | Model-development definition: 85/209 in-hospital deaths and 109/194 28-day deaths; prespecified covariates group assignment and SAPS-3; no interaction, no data reduction; SAPS-3 continuous or quartiles in sensitivity analysis; same covariates for 28-day mortality. | Defines analytic outcome populations and adjustment structure for matching results. | No coefficients, SEs, model diagnostics, or independent-validation statistics are supplied. |

## Statistical-definition links and review cautions

* eTable 4 labels OR models as logistic in-hospital-mortality analyses and HR models as Cox survival analyses; effect measures must not be cross-compared without their model/outcome labels.
* The source supplies 95% CIs but not the confidence level in eMethods; the eTable header calls them "95% CI." It supplies P values but not test sidedness or model standard errors. Any interval/P reconciliation must be explicitly diagnostic and retain those limitations.
* No `P = 0`, `P = 0.000`, or equivalent display-zero result occurs in this assigned source scope; `DISPLAY_ZERO_NOT_CANDIDATE` is not applicable.
* Matching keys to main-paper results: intervention-received/followed n=209, as-randomized n=212, 28-day-follow-up n=194; protocol vs usual-care contrast; as-treated >=3-L vs <3-L contrast; in-hospital mortality versus survival; SAPS-3 continuous versus quartile adjustment.
