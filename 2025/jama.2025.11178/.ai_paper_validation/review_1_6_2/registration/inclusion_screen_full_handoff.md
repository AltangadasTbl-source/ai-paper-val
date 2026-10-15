# Independent initial inclusion screen

Fresh screener: `/root/initial_screen`, gpt-6.1-sol/high. Scope: every finding in the current canonical numeric, cross-source and statistical-pass-1 artifacts: 5 + 8 + 13 = 26 findings. QUALITY_CONTROL_SCOPE.md and the full review contract were read. Every cited location was independently reread from 31 distinct current exact-source PDF renders and the supplied workbook XML/shared strings; checker transcription alone was never authority. No earlier scientific conclusions or web inputs were used. Sources and reused assets remain unchanged.

The coordinator assigned stable candidate IDs after these independent decisions, in substantive source order. Issue-group labels remain provenance labels; corroborating-only source definitions do not move an issue ahead of its conflicting report locations.

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-NUM-001 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C002 |
| F-NUM-002 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C017 |
| F-NUM-003 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C015 |
| F-NUM-004 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C003 |
| F-NUM-005 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C004 |
| F-XS-001 | cross_source_consistency_reviewer | initial | SCREENED_OUT | TERMINOLOGY_OR_WORDING | — |
| F-XS-002 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-XS-003 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C005 |
| F-XS-004 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C006 |
| F-XS-005 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C007 |
| F-XS-006 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C013 |
| F-XS-007 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C012 |
| F-XS-008 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C016 |
| F-ST1-001 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C009 |
| F-ST1-002 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C010 |
| F-ST1-003 | statistics_pass_1 | initial | SCREENED_OUT | CONTEXT_RESOLVES | — |
| F-ST1-004 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C003 |
| F-ST1-005 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C004 |
| F-ST1-006 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C008 |
| F-ST1-201 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C014 |
| F-ST1-202 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C014 |
| F-ST1-203 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C012 |
| F-ST1-204 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C013 |
| F-ST1-205 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C011 |
| F-ST1-206 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C004 |
| F-ST1-601 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C016 |

## One-sentence finding justifications

- **F-NUM-001:** Include through **Route A, category 3**, because the stated randomized denominator 776 and count 371 give a percentage interval [47.714102,47.904578] separated from printed 43% [42.5,43.5] by 4.214102 points, relative discrepancy .098002.
- **F-NUM-002:** Include through **Route A, category 3**, because workbook E82's 711 (73.2) conflicts with E3's N=1568, E83's two missing and A110's nonmissing-denominator rule, with recomputed [45.341417%,45.463259%] and relative gap .378234.
- **F-NUM-003:** Include through **Route A, category 3**, because the first eTable 8 header's at-three-month arm counts sum to [452.5,455.5], exceeding its [365.5,366.5] any-follow-up count by at least 86, relative gap .234973.
- **F-NUM-004:** Include through **Route B**, because the explicitly shared usual-care SD requires pairwise SMD additivity, 17 displayed triples remain separated above .05 after precision, and the intended standardized contrasts cannot be identified from the table for extraction.
- **F-NUM-005:** Include through **Route A, category 4**, because the stated reciprocal method reproduces other NNT rows but the three specified printed points remain separated from their recomputed intervals by relative gaps .050975, .062771 and .057218.
- **F-XS-001:** Screen out as **TERMINOLOGY_OR_WORDING**, because the main article's clinical diagnosis description and the plans' repeated-code EHR ascertainment describe the same malignancy exclusion at different levels of operational detail, without establishing that different participants entered the reported analysis.
- **F-XS-002:** Include through **Route B**, because the online session-duration endpoints differ by 14 minutes after half-unit precision, relative gaps .311 and .233, and the supplied sources do not identify whether the extracted primary intervention duration was revised or merely estimated differently.
- **F-XS-003:** Include through **Route A, category 5**, because age is labeled part of the prespecified base analysis in the report and workbook but is absent from the plans' explicit primary adjustment set.
- **F-XS-004:** Include through **Route B**, because the reported secondary models add the outcome-specific baseline value and import primary-model factors beyond the plans' explicit list, leaving the planned versus implemented adjustment of the key secondary estimates unresolved.
- **F-XS-005:** Include through **Route A, category 5**, because the SAP retains a primary follow-up/MAR specification while the report assigns primary status to weighted MNAR estimation and sensitivity status to the follow-up analysis, with the disclosed IPW amendment retained as an alternative explanation.
- **F-XS-006:** Include through **Route B**, because a stated binary education adjustment and three displayed education coefficients describe different primary-model coding and the repeated AA labels prevent definite coefficient attribution.
- **F-XS-007:** Include through **Route B**, because the stated final weight-model list names education while the fitted coefficient table substitutes employment, leaving the covariate set that generated primary response weights unresolved.
- **F-XS-008:** Include through **Route B**, because eTable 11's median/quartile labels conflict with its mean description and five PGIC centers beyond display tolerance for ordinary medians of the stated single-item scale, so an extractor cannot identify the summary and bounds to take.
- **F-ST1-001:** Include through **Route A, category 1**, because the main Table 2 intensity 12-month HC/PT NNT point 63 lies outside its printed 18–38 interval.
- **F-ST1-002:** Include through **Route A, category 1**, because the fourteen source-confirmed SMD points lie outside their printed intervals, including six physical-function points outside even the numerically sorted endpoints.
- **F-ST1-003:** Screen out as **CONTEXT_RESOLVES**, because descending endpoints identify the same numerical interval by their minimum and maximum without changing an extractable endpoint value, while separate point-containment and SMD-construction issues remain included.
- **F-ST1-004:** Include through **Route A, category 4**, because the common-SD construction reproduces the severity six-month row but fails twenty other rows by additivity, MD/SMD scaling or sign, extending included IG03 beyond F-NUM-004's seventeen triples.
- **F-ST1-005:** Screen out as **DUPLICATE_OF_INCLUDED**, because both main-table reciprocal-NNT occurrences are already retained by F-NUM-005 in IG04.
- **F-ST1-006:** Include through **Route B**, because six matched HC/PT response contrasts have null-containing RR intervals and finite positive NNT intervals, and the source's infinity rule does not establish how the different extracted null readings reconcile.
- **F-ST1-201:** Include through **Route A, category 1**, because seven imputation-model 95% intervals exclude zero while their P values exceed .05, independent of an unreported coefficient-test convention.
- **F-ST1-202:** Include through **Route A, category 1**, because three ratio intervals include a printed endpoint of 1 while their P values are below .05, and this route expressly forbids rounding-based removal.
- **F-ST1-203:** Screen out as **DUPLICATE_OF_INCLUDED**, because the education-versus-employment weight-model discrepancy and all its method locations are already retained by F-XS-007 in IG13.
- **F-ST1-204:** Screen out as **DUPLICATE_OF_INCLUDED**, because the binary-versus-multilevel education coding and repeated-label pattern is retained by F-XS-006 in IG14 with every coefficient and workbook location.
- **F-ST1-205:** Include through **Route B**, because the restricted-primary-analysis narrative and base-only covariate footnote do not identify whether education and employment entered the models generating eTable 8's primary-outcome subset estimates.
- **F-ST1-206:** Screen out as **DUPLICATE_OF_INCLUDED**, because the reminder-letter six-month PT/UC NNT point and its percentage inputs are already retained by F-NUM-005 in IG04.
- **F-ST1-601:** Screen out as **DUPLICATE_OF_INCLUDED**, because its five precision-qualified PGIC raw centers and summary-definition conflict are retained by F-XS-008 in IG11, including the p.18 method note.

## Consolidated issue groups for coordinator registration

### IG01 — Planned versus reported online session duration

Finding: **F-XS-002**. Earliest substantive compared location: DOC-001 p.3. Compared roles: REPORT main p.3; PLAN protocol pp.43–44; REPORT TIDieR pp.3–4. Proposed domain **protocol_report**, primary/all relationships **P_R**; main and TIDieR agree and merely corroborate the reported side.

Locations: [main p.3, Health Coach and Online Program](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=3); [protocol p.43, §10.1.1](../../../joi250046supp1_prod_1755300121.14087.pdf#page=43); [protocol p.44, coach overview](../../../joi250046supp1_prod_1755300121.14087.pdf#page=44); [TIDieR p.3, Procedures](../../../joi250046supp3_prod_1755300121.15087.pdf#page=3); [TIDieR p.4, When and How Much](../../../joi250046supp3_prod_1755300121.15087.pdf#page=4). Retain planned PT45–60 versus reported PT30–45 minutes, eight sessions/12 weeks in both; coach60 versus45–60 minutes overlaps and is context, not a separate numeric discrepancy. **Route B**: a permitted intervention-duration comparison, with unresolved convention and a different extractable treatment duration; self-pacing or a revised duration estimate remains an alternative, rather than an inferred intervention revision.

### IG02 — Therapeutic-dose adherence percentage

Finding: **F-NUM-001**. Earliest location: DOC-001 p.4. REPORT versus REPORT within main; domain **statistical_results**, primary/all relationships **S_W**. Locations: [main p.4, Results adherence paragraph](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4) and [p.5, Figure 1 PT allocation/session counts](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=5). **Route A, category 3**: retain 371 (43%) of randomized776 and the complete precision calculation above; Figure 1 corroborates 371 for6–8 sessions. No stated alternative denominator supports43%.

### IG03 — SMD construction across Table 3

Included findings: **F-NUM-004, F-ST1-004**. Earliest location: DOC-001 p.4 SMD definition. REPORT versus REPORT within main; domain **statistical_results**, primary/all relationships **S_W**. Locations: [main p.4, SMD method](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), [p.10, all severity/intensity/interference/social/physical MD and SMD columns](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), [p.11, both PGIC blocks and footnote d](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11).

Retain all three contrasts for the following20 outcome/time rows: severity3/12 months; intensity3/6/12; interference3/6/12; social3/6/12; physical3/6/12; PGIC-pain3/6/12; PGIC-general3/6/12. Seventeen rows have the additive-triple discrepancy in F-NUM-004, and the other three are severity12, intensity3 and interference12, where MD/SMD scaling gives HC/PT intervals [−.036429,.036429], [−.043,.043], [−.029444,.029444], versus printed −.11,−.08,−.12, remaining relative gaps .623377,.400,.712963. Retain physical3 HC/UC and physical6/12 HC/PT and PGIC-pain12 HC/PT sign comparisons as additional manifestations within those rows. **Route B** qualifies the numeric-checker pattern; **Route A, category 4** additionally qualifies the expanded method-reproduction pattern because the common-SD definition does reproduce severity6 within the required precision. Do not split additive, scale and sign manifestations of this same standardized-contrast construction. Actual UC-change SDs and fitted code are absent; different standardizers or contrast assignments remain questions, not assumptions.

### IG04 — Reciprocal NNT point-reproduction pattern

Included finding: **F-NUM-005**; duplicates **F-ST1-005, F-ST1-206**. Earliest location: DOC-001 p.4 NNT method. Compared roles REPORT main and REPORT results supplement, with separate internal percentage/NNT comparisons; domain **statistical_results**, primary/all relationships **S_W** (the sources do not print conflicting copies of the same analysis).

Locations: [main p.4, NNT definition](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); [main p.9, Table 2 severity6 HC/UC, interference6 HC/UC and footnote d](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9); [supplement p.14, eTable 8 Reminder Letters Added6 months PT/UC and footnote d](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14). **Route A, category 4**: adjusted percentages37.1/22.9 with NNT8,40.9/24.3 with NNT7,35.6/21.3 with NNT8 yield the three disjoint recomputed/printed intervals in the finding justification. The reciprocal calculation reproduces the other display rows within scope tolerance. Upward integer reporting is an alternative, particularly for main rows, but cannot remove the reproduced route-A observations under the prescribed half-unit rule.

### IG05 — Age as a prespecified base adjustment covariate

Finding: **F-XS-003**. Earliest location: DOC-001 p.4 adjustment list. Compared roles REPORT main/results/workbook versus PLAN protocol/SAP; domain **protocol_report**, primary relationship **P_R**, all relationships **P_R, S_C, S_W**.

Locations: [main p.4, Statistical Analysis covariates](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); [protocol p.56, §15.5](../../../joi250046supp1_prod_1755300121.14087.pdf#page=56); [SAP p.20, §§13–14](../../../joi250046supp2_prod_1755300121.15087.pdf#page=20); [results p.4, Adjustment](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4); [p.7 eTable 2 all-model variables](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7); [p.8 eTable 3 age](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8); [p.9 eTable 4 age](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9); [p.10 eTable 5 age](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10); [workbook eTable 3, G2, A10 and G10](../../../joi250046supp5_prod_1755300121.16087.xlsx). **Route A, category 5**: retain the six-factor explicit plan/main specification versus the report's seven-factor prespecified base set and workbook age flag. SAP§13 names age as a potential baseline variable, not fixed primary adjustment; a missing additional prospective specification remains an alternative.

### IG06 — Secondary-analysis adjustment specification

Finding: **F-XS-004**. Earliest location: DOC-001 p.4 secondary model paragraph. REPORT versus PLAN; domain **protocol_report**, primary/all relationships **P_R**. Locations: [main p.4](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); [main p.10 Table 3](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10); [main p.11 Table 3 continuation](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11); [protocol p.57, §15.6](../../../joi250046supp1_prod_1755300121.14087.pdf#page=57); [SAP p.21, §15](../../../joi250046supp2_prod_1755300121.15087.pdf#page=21). **Route B**: preserve the plan's baseline severity/all-strata list and its “same proposed approach” phrase, versus reported primary structure plus each secondary baseline value; the latter prevents reducing the finding to a wording variation because the model producing named intensity/interference/functioning estimates remains differently specified. The inheritance phrase may authorize some common primary factors, so outcome-specific baseline adjustment is the clearest unmatched element.

### IG07 — Primary versus sensitivity missing-data analysis roles

Finding: **F-XS-005**. Earliest location: DOC-001 p.4 missing-data methods. REPORT versus PLAN, plus retained plan-internal primary/MAR versus amended pattern-mixture/IPW wording; domain **protocol_report**, primary relationship **P_R**, all relationships **P_R, P_P**.

Locations: [main p.4](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); [SAP p.4, July2024 IPW amendment](../../../joi250046supp2_prod_1755300121.15087.pdf#page=4); [SAP p.19, §11](../../../joi250046supp2_prod_1755300121.15087.pdf#page=19); [results p.4 Missing Data](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4); [p.9 eTable 4](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9); [p.11 eTable 7 sensitivity introduction/complete-case block](../../../joi250046supp4_prod_1755300121.15587.pdf#page=11). **Route A, category 5**: retain the different primary/follow-up/MAR and primary/weighted-MNAR labels, rather than treating different estimates as matching numeric copies. The final amendment explicitly supports adding IPW and the threshold paragraph permits a pattern-mixture first approach; these are substantive alternatives that may explain the reported implementation, but do not erase the retained unconditional primary-MAR wording and report's primary/sensitivity assignment. Do not claim that the follow-up result is absent: the corresponding complete-case estimates are supplied in eTable7.

### IG08 — RR versus finite NNT null coverage

Finding: **F-ST1-006**. Earliest substantive result: DOC-001 p.9; p.4 is method context. REPORT versus REPORT within main; domain **statistical_results**, primary/all relationships **S_W**. Locations: [main p.4, binary model/NNT definition](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), [main p.9, Table 2 HC/PT severity6/12, intensity3/12, interference6/12 and footnotes b,d,e](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9). **Route B**: retain the six exact RR/NNT pairs and reciprocal implied RD intervals from the finding; RR=1 and RD=0 express the same response-equality null, but interval constructions may differ. This is a direct ambiguity about displayed null coverage and benefit-interval extraction, not a reconstructed pairwise P value or an assumed exact common-covariance contradiction. Missing RD interval construction and differing parameter-specific intervals remain explicit alternatives.

### IG09 — NNT point outside its confidence interval

Finding: **F-ST1-001**. Earliest location: DOC-001 p.9, Table 2 intensity12 HC/PT. REPORT internal; domain **statistical_results**, primary/all relationships **S_W**. [Exact source p.9](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9): **63 (18–38)**. **Route A, category 1**: point containment fails without an inferential-method assumption; this separate rule is not merged with IG08's null-coverage question.

### IG10 — SMD points outside printed confidence intervals

Finding: **F-ST1-002**. Earliest location: DOC-001 p.10. REPORT internal; domain **statistical_results**, primary/all relationships **S_W**. Locations: [main p.10 Table 3](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) and [p.11 PGIC-pain continuation](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11). **Route A, category 1**: preserve all fourteen tuples: severity12 PT/UC−.25(−.24,.01),HC/UC−.36(−.35,−.12); intensity12 HC/UC−.27(−.26,−.12); interference12 PT/UC−.26(−.25,.01),HC/UC−.37(−.36,−.11); physical6 PT/UC.15(.09,−.06),HC/UC.02(−.03,−.18),HC/PT.22(.16,.05); physical12 PT/UC.20(.18,−.03),HC/UC.07(.04,−.16),HC/PT.27(.25,.09); PGIC-pain12 PT/UC−.55(−.50,.05),HC/UC−.57(−.54,−.08),HC/PT−.29(−.25,.14). Sorting endpoint order does not remove any of these containment failures. This is distinct from IG03's point-construction rule; F-ST1-003's order-only observation is screened separately.

### IG11 — Raw-score summary statistic and bounds in eTable 11

Included finding: **F-XS-008**; duplicate **F-ST1-601**. Earliest substantive label conflict: DOC-005 p.15; DOC-001 p.11 provides the exact PGIC score definition needed for the numerical check. REPORT results supplement internal comparison; domain **statistical_results**, primary/all relationships **S_W**. The main PGIC scale definition corroborates the numerical premise and does not create S_C. This classification alignment follows the independent mechanical recheck; the inclusion decision is unchanged.

Locations: [main p.11, Table 3 PGIC footnotes h/i](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11); [results p.15, Additional Unadjusted Data and Analyses](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15); [p.17, eTable 11 title/header and all21 rows](../../../joi250046supp4_prod_1755300121.15587.pdf#page=17); [p.18 note b](../../../joi250046supp4_prod_1755300121.15587.pdf#page=18). **Route B**: preserve the mean-versus-median/quartile source descriptions and all raw-column locations, including the mixed-width HC3-month PGIC entries. The precision-qualified numerical subset is PGIC-pain PT6=2.8,PT12=2.8,UC12=2.2; PGIC-general PT3=2.7,UC6=1.8; each printed half-unit interval is separated from its nearest ordinary empirical single-item median by .15, relative gaps .053571,.053571,.068182,.055556,.083333. Other fractional centers, such as2.9 or2.6, have relative gaps≤.05 and are not separate numerical discrepancies. A set-valued or interpolated median definition remains an alternative; the independent inclusion rests on the unresolved extractable summary identity, not on asserting that every mathematical definition of a median excludes these values. No equality between raw medians and model mean differences or arm-column permutation is assumed.

### IG12 — Covariate set of restricted primary analyses

Finding: **F-ST1-205**. Earliest substantive comparator: DOC-005 p.4 primary adjustment description. REPORT internal; domain **statistical_results**, primary/all relationships **S_W**. Locations: [results p.4, Adjustment](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4); [p.7 eTable 2 final imputation/estimation variables](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7); [p.13 Protocol Change Subset Analyses](../../../joi250046supp4_prod_1755300121.15587.pdf#page=13); [p.14 eTable 8 footnote b and all three subset blocks](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14). **Route B**: education/employment are selected for primary estimation but absent from the explicit subset adjustment list despite the “primary analysis restricting to subsets” attribution. Preserve every3/6/12-month row in pre-enhancement, post-enhancement and reminder-letter blocks, especially the3-month primary-outcome estimates. An abbreviated footnote or a deliberately refitted base-only model is possible but not identified; do not infer missing weighting/imputation merely from silence.

### IG13 — Final response-weight model predictor membership

Included finding: **F-XS-007**; duplicate **F-ST1-203**. Earliest location: DOC-005 p.4 selection narrative; p.5 specifies weighting. REPORT internal; domain **statistical_results**, primary/all relationships **S_W**. Locations: [results p.4, Adjustment/selection](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4); [p.5, Non-Response Weighting](../../../joi250046supp4_prod_1755300121.15587.pdf#page=5); [p.7 eTable 2 final weight-model list](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7); [p.10 eTable 5 complete coefficient display](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10); corroborating [workbook eTable 3 A18,H18:J18](../../../joi250046supp5_prod_1755300121.16087.xlsx). **Route B**: retain listed education versus fitted employment OR1.49(1.11,2.00),P=.008; workbook employment selection Ps<.001,.0228,.0591 corroborate possible inclusion without resolving the final education omission. This is a primary-analysis model-membership question, not peripheral coefficient copying.

### IG14 — Education coding and coefficient attribution

Included finding: **F-XS-006**; duplicate **F-ST1-204**. Earliest location: DOC-005 p.7 eTable 2 final variable list. REPORT internal; domain **statistical_results**, primary/all relationships **S_W**. Locations: [results p.7 eTable 2 education selection](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7); [p.8 eTable 3 all three education rows](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8); [p.9 eTable 4 all three education rows](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9); corroborating [workbook eTable 3 A12:A16](../../../joi250046supp5_prod_1755300121.16087.xlsx). **Route B**: retain binary “any college vs HS degree or less” versus three model coefficients, both repeated AA labels and their distinct numeric estimates/intervals/Ps, and available distinct workbook categories. The repeated label alone might be wording, but the binary-versus-three-parameter model conflict prevents immediate identification of the adjustment generating the primary result and coefficient extraction.

### IG15 — Coefficient CI versus P-value null-significance pattern

Included findings: **F-ST1-201, F-ST1-202**, consolidated as one repeated coefficient interval/test compatibility issue with all10 rows. Earliest substantive location: DOC-005 p.8. REPORT internal; domain **statistical_results**, primary/all relationships **S_W**. Locations: [results p.8 eTable 3 seven rows](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8); [p.9 eTable 4 Age≥65 and second AA rows](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9); [p.10 eTable 5 PEG row](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10). Context: [results p.4 imputation description](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4), [p.5 model methods](../../../joi250046supp4_prod_1755300121.15587.pdf#page=5), [main p.4 two-sidedα=.05](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); the main source only corroborates the test level and does not create S_C.

**Route A, category 1**: retain eTable3 Pattern2−.28(−.47,−.08),P=.150; Pattern1−.20(−.36,−.03),P=.226; Pattern2/PT−.30(−.58,−.02),P=.280; Pattern2/HC−.47(−.74,−.19),P=.090; Site3 .19(.08,.29),P=.069; Site4 .15(.05,.24),P=.124; second AA .16(.07,.25),P=.077; eTable4 Age RR1.15(1,1.33),P=.046 and second AA RR1.16(1,1.33),P=.046; eTable5 PEG OR.96(.92,1.00),P=.037. Unrounded null-adjacent endpoints may explain the latter three, but the scope expressly exempts all these interval-versus-P comparisons from display-precision removal. Different test/interval constructions remain alternatives, with no inferred Wald standard errors, reference distributions or replacement numbers.

### IG16 — Within-header three-month subset counts

Finding: **F-NUM-003**. Earliest conflicting display: DOC-005 p.14 first eTable 8 population header. REPORT internal; domain **statistical_results**, primary/all relationships **S_W**. [Results p.14 first header](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14): randomized454;366 with any follow-up;PT149,HC153,UC152 at3months. Corroboration: [p.7 eTable 1 full follow-up counts](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7); [p.13 subgroup definition](../../../joi250046supp4_prod_1755300121.15587.pdf#page=13); samep.14 next header. **Route A, category 3**: the within-header nesting discrepancy exceeds display tolerance; randomized target-population counts are a possible interpretation, but do not identify why this block uses the same “at3months” description as observed contributors in the other blocks. Retain subtraction-based UC109/PT94/HC108 only as corroborating arithmetic, not as a required replacement.

### IG17 — Workbook All Observed depression percentage

Finding: **F-NUM-002**. Earliest workbook location: DOC-006 eTable 3 E3, then E82/E83/A110. REPORT internal; domain **statistical_results**, primary/all relationships **S_W**. [Supplied workbook eTable 3, E3,A82,E82,A83,E83,A110](../../../joi250046supp5_prod_1755300121.16087.xlsx). **Route A, category 3**: retain all exact cells, decoded source shared-string values and nonmissing-denominator calculation in the justification. The count711 and N1568−missing2 imply a percentage near45.4 rather than printed73.2; no restricted assessment denominator is stated. Checker links containing inserted spaces in the source filename were locator slips; the supplied workbook and exact XML cells above were used for this decision.

## Source confirmation and limitations

Source roles by content: DOC-001 main, DOC-004 intervention results description, DOC-005 results/method supplement and DOC-006 workbook are REPORT; DOC-002 protocol and DOC-003 SAP are PLAN. Every finding's quoted values and comparison locations were checked against the supplied source renders or direct worksheet/shared-string XML, including all fourteen containment tuples, all twenty SMD-construction rows and all ten interval/P rows. The precision calculations use half-unit bounds and the fixed relative-gap rule; interval-versus-test/point-containment comparisons are never rounded away. No scientific source-reading gap remains in this assigned scope.

Durable engine/source notes: `preprocessing/initial_screen/engine_record.md`; freshly generated mainp5/mainp9 derivatives use pinned PyMuPDF1.26.4,200dpi,CPU; other exact-source pages are current-run renders independently visually reread, not reused checker conclusions. Workbook XML copies came from direct `unzip -p`; no spreadsheet recalculation or new Python helper was used.

Named evidence limits: no participant-level records, exact UC change SDs, complete covariance/test degrees of freedom, unrounded coefficient endpoints, RD/NNT interval construction, or additional prospective amendment is supplied; the PGIC median calculation uses the ordinary empirical median and retains alternative interpolation as a question. These limits are recorded in the relevant included group and do not replace observable source comparisons. No severity, validity or human disposition is assigned.

Counts: **26 findings;19 INCLUDE rows consolidated into17 included issues;7 SCREENED_OUT rows**: DUPLICATE_OF_INCLUDED5, TERMINOLOGY_OR_WORDING1, CONTEXT_RESOLVES1; all other permitted screened-out reason codes0. Every finding has exactly one initial decision.


Mechanical classification alignment: C016/IG11 is S_W, with the main PGIC score definition used only as corroboration. All26 independent initial decisions remain unchanged.
