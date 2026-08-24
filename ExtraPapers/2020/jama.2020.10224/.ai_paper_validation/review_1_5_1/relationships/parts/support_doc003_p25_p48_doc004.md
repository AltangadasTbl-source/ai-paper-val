# Numeric and statistical relationship inventory — DOC-003 pp. 25-48 and DOC-004 pp. 1-2

## Scope, source authority, and checking boundary

Assigned direct-source scope is DOC-003 `joi200066supp2_prod.pdf` PDF pp. 25-48 and DOC-004 `joi200066supp3_prod.pdf` PDF pp. 1-2. N IDs begin at N500 and S IDs at S500, as assigned. Locations are direct PDF pages. Native-layout text was used only for transcription; rendered direct PDF pages confirmed the tables and eFigure. These entries map relationships for later checking; no candidate IDs or adjudications are assigned here.

## Numeric/reporting relationships

| ID | Exact location | Relationship, values, labels, and rule/status |
|---|---|---|
| N500 | DOC-003 p.25 | Sensitivity narrative: censoring at CVD endpoint, total-depression HR 0.99 (0.88-1.10); CVD outcome associations HRs total 2.96 (2.05-4.27), incident 2.72 (1.76-4.21), recurrent 2.85 (1.46-5.55); time-updated CVD covariate, vitamin-D3 HR 0.97 (0.87-1.09); cancer HRs total 1.21 (0.89-1.65), incident 1.28 (0.91-1.81), recurrent 0.97 (0.48-1.97). All CIs contain their stated HRs. |
| N501 | DOC-003 p.26 | eTable 8 risk-set identity: total 18,353; incident 16,657; recurrent 1,696. Rule: 16,657 + 1,696 = 18,353 (PASS). Composite total depression and incident/recurrent definitions printed in footnotes. |
| N502 | DOC-003 p.27 | eTable 9 time-specific group Ns: vitamin D3 8,534/8,381/8,176/7,763/5,316 and average 9,181; placebo 8,486/8,344/8,112/7,603/5,231 and average 9,172. Rate-ratio label is explicitly defined as percent difference in PHQ-8 severity change. |
| N503 | DOC-003 pp.28-30 | eTable 10 censored-after-letter sensitivity: group Ns, adjusted baseline means, each annual adjusted change, vitamin-D3-minus-placebo differences and p values as fully transcribed in extraction artifact. P-interaction 0.63 is a 5-df treatment-by-time test; average years 1-5 difference 0.01 (-0.04,0.05), P=.71. Letter-related censoring definition is PHQ-8 >=10 in stated circumstances and all >=15; post-letter values censored. |
| N504 | DOC-003 pp.31-32 | eTable 11 omitting-year-5 sensitivity: group Ns, adjusted means/changes, contrasts and p values as transcribed. P-interaction .73; average years 1-4 difference 0.00 (-0.04,0.05), P=.83. |
| N505 | DOC-003 pp.33-35 | eTable 12 rate/count relationships by sex. Men: risk sets 8,642 + 688 = 9,330; cases 426 + 122 = 548. Women: 8,015 + 1,008 = 9,023; cases 494 + 192 = 686 (all PASS). Printed rate unit is cases per 1,000 p-y; person-time totals absent, so rate reproduction is not possible. Narrative rounds sex rates consistently to one decimal and reports women-versus-men HR 1.34 (1.19-1.50). |
| N506 | DOC-003 pp.36-37 | eTable 13 rate/count relationships by randomized group. Vitamin D3: risk sets 8,350 + 831 = 9,181; cases 459 + 150 = 609. Placebo: 8,307 + 865 = 9,172; cases 461 + 164 = 625 (all PASS). Rate unit is cases per 1,000 p-y; person-time totals absent. |
| N507 | DOC-003 pp.38-40 | eTable 14 categorical vitamin-D status sample identity: 10,089 sufficient + 1,328 low = 11,417, matching total sample with 25(OH)D (PASS). Low-vitamin-D threshold is <20 ng/mL; continuous exposure scale is per 10 ng/mL. HR results and overall PHQ-8-change mean differences have matching narrative restatement for the two HRs. |
| N508 | DOC-003 p.41 | eTable 15 descriptive PHQ-8 means (SDs) at baseline and years 1-5 in both randomized groups; all values and units are mapped in the extraction artifact. No denominators are supplied. |
| N509 | DOC-003 p.42 | eFigure eight item-level likelihood ratios, CIs, and p values; likelihood-ratio label, Vitamin-D3-versus-placebo direction, and average-over-follow-up definition are explicitly supplied. Values mapped in extraction artifact. |
| N510 | DOC-003 pp.43-47 | Protocol/context quantities: original/revised/final VITAL participant targets; age changes; approximately 70% CMS linkage; repeated-PHQ schedule; CTSC Ns, ICC, CI, and agreement percentage. These do not form a printed treatment-result contradiction within this assigned source scope. |
| N511 | DOC-003 p.48; DOC-004 pp.1-2 | No applicable result relationship: reference list and data-sharing administrative statement, respectively. DOC-004's 05-01-2021 availability date is administrative, not a clinical or statistical result. |

## Inferential-statistical relationships

| ID | Exact location | Definition and result inventory | Mapping status |
|---|---|---|---|
| S500 | DOC-003 p.25 | HR sensitivity results listed in N500. Compatibility is limited to point estimate within printed 95% CI; all listed HRs satisfy it. Exact models/sidedness/SEs are not supplied. | PASS_1_PENDING; PASS_2_PENDING |
| S501 | DOC-003 p.26 | Fine-Gray subdistribution-hazard models, death as competing event. Total HR 0.97 (0.87-1.09), P=.60; incident 0.99 (0.87-1.13), P=.87; recurrent .95 (.76-1.18), P=.62. Each CI includes 1 and each printed P exceeds .05; direction is coherent. | PASS_1_PENDING; PASS_2_PENDING |
| S502 | DOC-003 p.27 | Repeated-measures negative-binomial RR models; time indicator; age, sex, n-3 adjustment. Six RR/CI/P result triples: 1.00 (.95-1.05)/.92; 1.03 (.98-1.08)/.22; 1.02 (.96-1.07)/.57; 1.00 (.95-1.05)/.87; 1.03 (.97-1.09)/.30; 1.01 (.97-1.05)/.51. All CIs include 1 and Ps >.05. | PASS_1_PENDING; PASS_2_PENDING |
| S503 | DOC-003 pp.28-30 | General linear response-profile sensitivity with 5-df treatment-by-time interaction. Annual mean-difference CI/P pairs: -0.00 (-.06,.05)/.86; .02 (-.03,.08)/.42; .02 (-.04,.08)/.43; -.01 (-.07,.05)/.69; .03 (-.04,.10)/.39; average .01 (-.04,.05)/.71; interaction .63. All contrast CIs contain 0 and printed Ps >.05. | PASS_1_PENDING; PASS_2_PENDING |
| S504 | DOC-003 pp.31-32 | General linear response-profile sensitivity, omission of year 5. Annual mean-difference CI/P pairs: -.01 (-.06,.05)/.84; .03 (-.03,.08)/.36; .01 (-.05,.07)/.65; -.01 (-.07,.05)/.72; average .00 (-.04,.05)/.83; interaction .73. All contrast CIs contain 0 and printed Ps >.05. | PASS_1_PENDING; PASS_2_PENDING |
| S505 | DOC-003 p.35 | Women-versus-men total-depression HR 1.34 (1.19-1.50), primary results model. CI excludes 1 and point estimate lies inside CI; P value/model covariate details absent on this page. | PASS_1_PENDING; PASS_2_PENDING |
| S506 | DOC-003 pp.38-40 | Cox total-depression models: low vitamin D HR 1.08 (.87-1.35), P=.48; per 10 ng/mL HR 1.00 (.93-1.08), P=.94. General linear profile overall PHQ-8 change: low vitamin D difference -.04 (-.13,.06), P=.45; per 10 ng/mL .02 (-.01,.05), P=.14. All null CIs and Ps are coherent. | PASS_1_PENDING; PASS_2_PENDING |
| S507 | DOC-003 p.42 | Repeated-measures logistic item-level models, time indicator, age/sex/n-3 adjustment. Eight likelihood-ratio CI/P triples are in N509/extraction. Each CI contains 1 and each P is >.05; no incompatible display is observed. | PASS_1_PENDING; PASS_2_PENDING |
| S508 | DOC-003 pp.46-47 | CTSC concordance: ICC .63 (95% CI .59-.67), N=1,053; 86% eligibility agreement. The ICC is within its CI; percentage denominator is not printed, so it is not reproducible. | PASS_1_PENDING; PASS_2_PENDING |

## Matching main-paper keys for cross-source matching

These are result-identity keys derived from the assigned support source only. They identify the required match dimensions for a later main-paper comparison; they do not assert a comparison outside this disjoint assignment.

| Support relationships | Matching key |
|---|---|
| N500, S500-S501 | Vitamin D3 versus placebo; total, incident, or recurrent depression; hazard ratio; sensitivity/competing-risk specification; stated 95% CI and P value where printed. |
| N502-S504 | Vitamin D3 versus placebo; PHQ-8 change from baseline; specified year or average-years contrast; rate ratio or mean difference; stated model and sensitivity condition. |
| N505-S506 | Depression rates or risk by sex, randomized group, or baseline 25(OH)D; require exact population/exposure, time basis, rate unit or model, and covariate set. |
| N508-S507 | Vitamin D3 versus placebo; PHQ-8 score or item-level symptom; stated follow-up time/average; mean (SD) or likelihood ratio and CI/P. |
| N510-S508 | CTSC-only concordance/eligibility validation; distinguish CTSC N and PHQ-8/PHQ-9 or MINI comparator from the randomized treatment-effect population. |

## Mapping observation

No possible quantitative consistency candidate was observed within the assigned direct-source scope. No P value is printed as a display zero. Missing person-time denominators, exact model covariance/SEs, and an agreement denominator are recorded as limits on reproducing selected rates/tests, not as a candidate.
