# Statistical pass 2 — mandatory reviewer and shard A

**Status:** PASS_2_COMPLETE for every assigned S001–S040 record (40 relationships); **new distinct candidates: 0**. This is the mandatory pass-2 agent's disjoint shard A. Peer fresh pass-2 agents cover S041–S080 and S081–S120, and the coordinator merges the canonical inventory. This artifact makes no claim to independently revisit their records. Existing C001 is reconciled in S029 and S030 without duplicating it. All sixteen stable candidate IDs remain Pending Human Adjudication.

- **Runtime agent ID:** 01a12878-2f36-79f1-b1a9-e4f616338e59
- **Model:** gpt-6.1-sol
- **Reasoning effort:** high
- **Start mode:** FRESH_SPAWN
- **Distinct pass-1 runtime:** 01a12869-8c20-7fb1-b42a-ba626d66dcf5
- **Owned artifacts:** checkers/statistical_pass_2.md; statistics/parts/pass2_relationships_a.md
- **Provider:** current session provider; no provider selection or credential changes.
- **Complete decision inputs read:** candidate_ledger.md, verification/evidence_recheck.md, statistics/parts/shared_definitions.md, and assigned statistics/parts/pass2_relationships_a.md. Truncated displayed excerpts were completed with bounded consecutive reads. Normative QUALITY_CONTROL_SCOPE.md and workflow_1_6/review_contract.md were also read completely. No old candidates, reports or dispositions were used.

## Exact assigned scope and evidence authority

Assigned IDs are S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040.

S001–S018 cover all 18 sensitivity/specificity differences in main Table 2: All, Men, Women; quantitative 10.2, quantitative 17.0 and qualitative 10.2. S019–S036 cover all 18 PPV/NPV differences in main Table 3 with the same strata/tests and scheduled day-2 intention-to-screen population. S037–S040 cover eTable 3 All quantitative 10.2 and 17.0 sensitivity/specificity under at-least-one-positive results in up to three scheduled-day-2/3/4 samples. Each supplies point, interval, arm estimates and matched counts.

Every scoped source result location is REPORT by content. Main methods, narrative, Table 2 and Table 3 are in [main article](../../../jama_brenner_2019_oi_190039.pdf#page=5); the combined-sample table is in the non-plan [results supplement](../../../joi190039supp3_prod.pdf#page=5). [SAP analysis amendments](../../../joi190039supp2_prod.pdf#page=9) are PLAN and identify the disclosed primary intention-to-screen set and missing-day handling. No comparison is classified P_R solely because the plan is consulted for definitions.

Direct source page inspection and supplied-source recheck are authoritative. The existing fresh recheck-main-p5.png was visually inspected during this pass, confirming every Table 2/Table 3 value and the blank men's third Table 3 Test cell. Direct pdftotext -layout (available Poppler, CPU) was used read-only to inspect main physical pages 1, 3–4; results physical page 5; and SAP physical page 9. No new derivative file was created and no source or reused asset was changed. The complete fresh mechanical recheck supplies page-authoritative facts for all C001–C016 comparisons.

## Check families and bounded interpretations

1. **Arithmetic and denominator identity.** Each count-derived arm estimate and raw aspirin-minus-placebo contrast was recomputed using the source-defined diagnostic proportion. Every displayed arm value and difference differs by at most 0.05 percentage points from the matched count result. Contrast computation uses counts rather than subtraction of previously rounded percentages. Counts are people classified by a test, and the appropriate conditional denominators differ among sensitivity, specificity, PPV and NPV. No common total is substituted into these distinct conditional probabilities.
2. **Containment, endpoint ordering and direction.** All forty lower endpoints are below their upper endpoints; each printed point lies inside its interval. Every sign agrees with raw counts and the source's aspirin-minus-placebo comparison. Negative specificity differences agree with the narrative's lower-specificity wording; positive sensitivity statements do not imply a positive interval lower bound.
3. **Effect measure, scale, reference group and rate/count.** Percent arm estimates and percentage-point contrasts describe unadjusted diagnostic proportions. No OR, RR, HR, standardized difference, person-time rate, probability of any adverse event or number of samples is substituted. The common percent notation for a difference is interpreted in the clearly stated percentage-point context rather than creating an unsupported relative-change candidate.
4. **P/test/statistic/SE compatibility.** S001–S006 provide P values in the main text; their null-inclusion and narrative interpretations agree qualitatively at the source's two-sided .05 level. D2 does not establish the actual difference-P formula, null variance, continuity correction, statistic or SE. Exact CI/P inversion is unavailable, even though D4 supplies a diagnostic Agresti–Caffo calculation. S007–S040 have no result-specific P/statistic/SE; no such number is manufactured. Degrees of freedom, covariance, variance estimator, multiplicity and estimand bridges are never inferred from convention.
5. **Repetitions, duplicates, population and cross-source identity.** Main abstract and narrative quantitative primary results match the Table 2 numbers. Men's narrative ranges repeat the appropriate endpoints rather than defining a pooled result. Main PPV/NPV values reconcile with Table 2 counts. ITS, PP and multi-day aggregation are distinct populations/time definitions, so their numerical differences are not treated as disagreement. Shared cutoff numbers do not establish test identity; the blank men's Table 3 cell remains explicitly unresolved C001.
6. **Figure, totals and missingness implications.** The main flow figure's 1075 aspirin and 1059 placebo analysis counts are upper cohort counts, whereas Table 2 quantitative valid scheduled-day-2 totals are 1030 and 1012, and qualitative totals are 974 and 969. These are explicitly described valid-test subsets in main p.3, not missing participants requiring a common denominator. Quantitative Table 2 TP/FN/TN/FP sums across Men and Women equal their All cells at each cutoff; the same is true for qualitative counts. Multi-day All quantitative totals are 1059 and 1042, comprising disease-conditioned denominators 113/107 and nondisease denominators 946/935; each is within its arm analysis cohort. They need not equal the single-day denominators 112/102 and 918/910.
7. **Observation versus diagnostic.** Printed values, visible cells and statements are observations. Raw-count arithmetic and D4 endpoints are calculations, and D4 reconstruction remains labelled diagnostic rather than a replacement reported analysis. The intended qualitative identity in S029/S030 is inferred from matched counts, not printed into the blank source cell.
8. **Display zero.** No displayed P=0 is present in these assigned results. Coherent finite-precision P zeros would be recorded DISPLAY_ZERO_NOT_CANDIDATE without tiny-tail reconstruction or a replacement threshold. The full recheck/shared definitions confirm eTable 6 SD zeros are parameter values, while actual P values are .16–.50; those out-of-shard facts neither justify a P-zero candidate nor change these comparisons.

## Complete forty-relationship pass-2 register

The numerator/denominator and interval inputs are source-backed. Computed differences below are diagnostic arithmetic on matched counts; source printed point estimates follow the arrow. All rows have zero new distinct candidate outcomes. P values are qualitative compatibility locators, not a claim of exact CI/P test inversion.

| S ID | Measure | Aspirin versus placebo numerator/denominator | Raw difference → printed point (percentage points) | Source 95% interval and direct checks | Reported P | Recheck/candidate implication | Pass 2 |
|---|---|---|---|---|---|---|---|
| S001 | Sensitivity | 45/112 vs 31/102 | 9.786415 → 9.8 | [-3.1, 22.2] ordered; point contained | .14 | No new candidate | PASS_2_COMPLETE |
| S002 | Specificity | 755/918 vs 807/910 | -6.437310 → -6.4 | [-9.6, -3.2] ordered; point contained | <.001 | No new candidate | PASS_2_COMPLETE |
| S003 | Sensitivity | 32/112 vs 23/102 | 6.022409 → 6 | [-5.7, 17.5] ordered; point contained | .32 | No new candidate | PASS_2_COMPLETE |
| S004 | Specificity | 842/918 vs 863/910 | -3.114032 → -3.1 | [-5.4, -0.8] ordered; point contained | .008 | No new candidate | PASS_2_COMPLETE |
| S005 | Sensitivity | 35/101 vs 22/100 | 12.653465 → 12.7 | [0.1, 24.7] ordered; point contained | .048 | No new candidate | PASS_2_COMPLETE |
| S006 | Specificity | 732/873 vs 798/869 | -7.980892 → -8 | [-11, -4.9] ordered; point contained | <.001 | No new candidate | PASS_2_COMPLETE |
| S007 | Sensitivity | 33/77 vs 15/54 | 15.079365 → 15.1 | [-1.6, 30.6] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S008 | Specificity | 360/450 vs 387/455 | -5.054945 → -5.1 | [-10, -0.1] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S009 | Sensitivity | 25/77 vs 13/54 | 8.393458 → 8.4 | [-7.5, 23.3] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S010 | Specificity | 408/450 vs 424/455 | -2.520147 → -2.5 | [-6.1, 1.1] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S011 | Sensitivity | 28/71 vs 12/55 | 17.618438 → 17.6 | [1.3, 32.6] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S012 | Specificity | 354/428 vs 400/448 | -6.575434 → -6.6 | [-11.2, -2] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S013 | Sensitivity | 12/35 vs 16/48 | 0.952381 → 1 | [-19.1, 21.4] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S014 | Specificity | 395/468 vs 420/455 | -7.905983 → -7.9 | [-12, -3.8] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S015 | Sensitivity | 7/35 vs 10/48 | -0.833333 → -0.8 | [-17.9, 17.2] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S016 | Specificity | 434/468 vs 439/455 | -3.748474 → -3.7 | [-6.7, -0.8] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S017 | Sensitivity | 7/30 vs 10/45 | 1.111111 → 1.1 | [-17.7, 20.9] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S018 | Specificity | 378/445 vs 398/421 | -9.592997 → -9.6 | [-13.5, -5.5] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S019 | PPV | 45/208 vs 31/134 | -1.499713 → -1.5 | [-10.7, 7.4] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S020 | NPV | 755/822 vs 807/878 | -0.064291 → -0.1 | [-2.7, 2.5] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S021 | PPV | 32/108 vs 23/70 | -3.227513 → -3.2 | [-17.2, 10.5] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S022 | NPV | 842/922 vs 863/942 | -0.290378 → -0.3 | [-2.8, 2.3] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S023 | PPV | 35/176 vs 22/93 | -3.769550 → -3.8 | [-14.4, 6.5] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S024 | NPV | 732/798 vs 798/876 | 0.633433 → 0.6 | [-2.1, 3.3] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S025 | PPV | 33/123 vs 15/83 | 8.756979 → 8.8 | [-3, 19.8] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S026 | NPV | 360/404 vs 387/426 | -1.736160 → -1.7 | [-5.9, 2.4] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S027 | PPV | 25/67 vs 13/44 | 7.767978 → 7.8 | [-10.3, 24.8] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S028 | NPV | 408/460 vs 424/465 | -2.487144 → -2.5 | [-6.4, 1.4] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S029 | PPV | 28/102 vs 12/60 | 7.450980 → 7.5 | [-6.4, 20.2] ordered; point contained | Not printed | C001, no new candidate | PASS_2_COMPLETE |
| S030 | NPV | 354/397 vs 400/443 | -1.124688 → -1.1 | [-5.3, 3] ordered; point contained | Not printed | C001, no new candidate | PASS_2_COMPLETE |
| S031 | PPV | 12/85 vs 16/51 | -17.254902 → -17.3 | [-31.8, -2.5] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S032 | NPV | 395/418 vs 420/452 | 1.577254 → 1.6 | [-1.7, 4.8] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S033 | PPV | 7/41 vs 10/26 | -21.388368 → -21.4 | [-42.2, 0.8] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S034 | NPV | 434/462 vs 439/477 | 1.905851 → 1.9 | [-1.4, 5.2] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S035 | PPV | 7/74 vs 10/33 | -20.843571 → -20.8 | [-37.8, -4] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S036 | NPV | 378/401 vs 398/433 | 2.347480 → 2.3 | [-1.1, 5.8] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S037 | Sensitivity | 63/113 vs 49/107 | 9.957820 → 10 | [-3.3, 22.8] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S038 | Specificity | 685/946 vs 774/935 | -10.370601 → -10.4 | [-14.1, -6.6] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S039 | Sensitivity | 44/113 vs 35/107 | 6.227773 → 6.2 | [-6.4, 18.7] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |
| S040 | Specificity | 816/946 vs 852/935 | -4.865067 → -4.9 | [-7.7, -2] ordered; point contained | Not printed | No new candidate | PASS_2_COMPLETE |

## Complete cross-lane ledger and recheck reconciliation

Every registered ID was read, retained and considered for implications in the assigned statistical scope. No missing plan definition is transformed into a new inferential candidate and no existing ID is removed because recheck narrowed its claim.

| Existing ID | Source roles and registered relationship | Pass-2 implication for S001–S040 |
|---|---|---|
| C001 | REPORT main Table 3 vs REPORT main Table 2; S_W | Directly affects S029 and S030. Fresh source confirms one blank Test cell; matched qualitative counts reproduce both measures and intervals. One existing label candidate remains, with no duplicate or arithmetic candidate. |
| C002 | REPORT eTable 5 vs REPORT eTable 4; S_W | Visible cutoff unit ends at [µg in the PP predictive-value table; main Table 3's complete unit is corroboration. It does not change main numeric inputs or constitute a new cross-document conflict. |
| C003 | REPORT women's PP quantitative 10.2 eTable 5 vs eTable 4; S_W | The visible point magnitude is absent; count-derived -18.20431248 is diagnostic. S031 is ITS, with -17.25490196 and an intact visible point; different population numbers are not conflicting repetitions. |
| C004 | REPORT women's PP quantitative 17.0 eTable 5 vs eTable 4; S_W | Minus-only visible PP point and diagnostic -25.71428571 are distinct from intact ITS S033 -21.38836773. No duplication or implied equality across PP/ITS. |
| C005 | REPORT women's PP qualitative 10.2 eTable 5 vs eTable 4; S_W | Minus-only PP point with diagnostic -21.57258065 is distinct from intact ITS S035 -20.84357084. Placebo 31.25% rounding tie does not independently establish an arithmetic contradiction. |
| C006 | PLAN SAP p.6 paired thresholds; P_P | The p.6 standalone 10.2 Hb/g omits µg relative to its paired 17 expression. p.8's qualitative FD threshold is corroborating unit context only, not the same quantitative primary-result endpoint. Main table complete units and numeric cutoffs remain coherent. |
| C007 | PLAN duration field and dated schedule; P_P | Missing total-duration endpoints are retained as a bounded calendar question. A planned schedule is not an observed follow-up equality comparator for these inferential results. |
| C008 | PLAN three working days and attached 72 hours; P_P | The undefined working calendar concerns an operational assessor deadline; it does not redefine scheduled or actual stool-sampling days or any test denominator. |
| C009 | PLAN general blood-tube range and serum-specific volume; P_P | Optional serum 8.5 mL versus general 9–10 mL concerns blood sampling, not stool test positivity, disease ascertainment or an assigned interval denominator. |
| C010 | PLAN pharmacovigilance component and subtotal; P_P | Decimal interpretation of 1.704 reconciles rounded subtotal while thousands interpretation differs. Both branches remain explicit; neither supplies a disease/test count or model definition. |
| C011 | PLAN optional blood procurement; P_P; record_input_error | Recheck removes unsupported randomization-N purchasing alignment. Do not propagate the hypothetical 2400-person difference into any inferential population concern. |
| C012 | PLAN insurance rate formula and attached total; P_P | 23.50×2400=56400 versus 67116, with diagnostic exact ratio 1.19, is a plan arithmetic question. No unprinted insurance modifier is used to reinterpret statistical estimates. |
| C013 | PLAN top-level budget totals and overall amount; P_P | 507605 versus 505570 differs by 2035 using displayed category totals; no implication for forty diagnostic inferential rows or trial participant totals. |
| C014 | PLAN printing line and attached footnote; P_P | 3000 versus 3500 concerns printing scope/version. It does not supply conflicting trial test statistics. |
| C015 | PLAN meeting cost bundle; P_P; record_input_error | Printed 480+500=980 reconciles. Fourfold repetition of one bundle is unsupported, and no inferential mismatch is propagated from it. |
| C016 | PLAN center and practice payment components; P_P; record_input_error | Printed 30×2000=60000 reconciles; identity with the 75-EUR incentive is unestablished. Do not equate payment populations with diagnostic denominators. |

## Exact remaining definitions and outcomes

Source-defined diagnostic proportion, population, cutoff, direction and 95% interval level suffice for all direct arithmetic/order/containment checks. The actual difference-P computation, statistic, SE, null variance/continuity rule and full method identity are not supplied for exact inferential inversion. Intended men's third Table 3 Test identity or omitted-label convention remains the explicit human question in C001. No additional scientific coverage gap exists within the assigned forty relationships.

The overall predictive-value statement is explicitly pooled: all six Table 3 All-population intervals span zero. S031 and S035's negative women's intervals do not make that pooled statement contradictory; subgroup results are not interchangeable with overall results. The quantitative-primary conclusion also does not conflict with qualitative secondary sensitivity S005, or men's qualitative S011, because the test and population differ. Non-significant sex interaction does not imply that every within-sex interval must include zero.

For S037/S039, multi-day sensitivity increases in both arms and aspirin-minus-placebo sensitivity changes little relative to the single-day result, consistent with the main p.4 statement. For S038/S040, multi-day specificity decreases in both arms, also matching the narrative. At-least-one-positive aggregation is per participant rather than an unreported independence assumption or threefold sample count. No same-estimand covariance or multi-day variance is invented.

**New candidate emission:** None after all forty assigned relationships, complete current ledger and all fresh recheck facts were revisited. This explicit zero outcome is not a stopping/count criterion. The assigned part contains full row-specific reasoning and PASS_2_COMPLETE for every S ID, including no-new-candidate rows. Coordinator canonical merge and the peer disjoint shards remain required for full S001–S120 completion.
