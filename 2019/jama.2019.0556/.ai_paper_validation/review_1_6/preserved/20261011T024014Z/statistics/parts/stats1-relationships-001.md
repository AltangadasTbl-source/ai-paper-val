# Statistical relationship inventory part 1

Scope: S001–S117, 117 distinct inferential or definition relationships; runtime /root/statistics_pass1, gpt-6.1-sol/high, FRESH_SPAWN. Every row is PASS_1_COMPLETE. Source roles and physical PDF pages are explicit. NR means not reported, not zero. The model-definition profiles in the canonical inventory apply to every row naming that profile. Check K means ordered endpoints, estimate containment, direction, scale and labels checked; matched repetitions checked where present; no independent inconsistency found. Check Q means no numeric estimate/interval available; all supplied inferential statements, scope, label and repetitions checked. Exact CI/P/test compatibility is not asserted when the profile lacks a supplied compatible rule. Every row awaits the distinct pass-2 agent.

## Power, assumptions and missingness

| S ID | Mapping key | Exact source and role | Printed inferential relationship | Definition profile | Pass-1 checks and observations | Pass 1 | Pass 2 |
|---|---|---|---|---|---|---|---|
| S001 | M010 | REPORT jama_bot_2019_oi_190007.pdf p4 Sample Size | Active20%, control30%; relative33%, absolute10%; N392,196 in each4 combinations; two-sided alpha.05,power.90,attrition22%,250/combination; prior25–50% | POWER-R | Counts/scale checked; SC01 internal total wording; SC03 comparison with PLAN assumptions | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S002 | U009 | PLAN joi190007supp1_prod.pdf p16 section4.4,p17 continuation | Difference25%; control30%,active15%; additive-interaction180/group,two-sided alpha.05,power.90,dropout20%,250/arm | POWER-P | SC02 percentage meaning; SC03 planning-assumption match to S001; no invented power formula | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S003 | U010 | PLAN joi190007supp1_prod.pdf p17 section4.4 | Synergistic pure-treatment-group comparison power80%; IDS continuous power statement separately tracked S140 | POWER-P | Q; contrast differs from additive calculation; unreported effect/variance prevent reconstruction | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S004 | M012 | REPORT jama_bot_2019_oi_190007.pdf p4 Statistical Methods | Scaled Schoenfeld proportionality test P>.05; hazard assumption met | PH-TEST | Q; direction agrees with stated test; statistic/df/per-term/global identity NR | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S005 | M071 | REPORT jama_bot_2019_oi_190007.pdf p6 Follow-up Attrition | Primary missingness across4arms,T3 P=.47;194/1025 missing | MISSING | Q; no difference narrative compatible; test/df NR | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S006 | M071 | REPORT jama_bot_2019_oi_190007.pdf p6 Follow-up Attrition | Primary missingness across4arms,T6 P=.62;254/1025 missing | MISSING | Q; no difference narrative compatible; test/df NR | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S007 | M071 | REPORT jama_bot_2019_oi_190007.pdf p6 Follow-up Attrition | Primary missingness across4arms,T12 P=.91;246/1025 missing | MISSING | Q; no difference narrative compatible; test/df NR | PASS_1_COMPLETE | AWAITING_PASS_2 |

## Main primary and post hoc outcomes

| S ID | Mapping key | Exact source and role | Estimate, 95% CI, P | Profile | Checks and repetitions | Pass 1 | Pass 2 |
|---|---|---|---|---|---|---|---|
| S008 | M075,M085 | REPORT jama_bot_2019_oi_190007.pdf p6 Table2,p7 Onset,p1 abstract | Supplements OR1.06,[.87,1.29],P.57;N512/513,54/51 events | LOGIT-MI | K; p1,p6,p7 estimates/CI identical;p6/p7 P identical; unit-change/contrast definition limitation only | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S009 | M077,M085 | REPORT jama_bot_2019_oi_190007.pdf p6 Table2,p7 Onset,p1 abstract | F-BA OR.93,[.76,1.13],P.47;N512/513,48/57 events | LOGIT-MI | K; all repeats agree; shared effectcode contrast definition limitation only | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S010 | M078,M085 | REPORT jama_bot_2019_oi_190007.pdf p6 Table2,p7 Onset,p1 abstract | Supplements×F-BA OR.93,[.76,1.14],P.48 | LOGIT-MI | K; repeats identical; p1 says combination and explicitly P for interaction; interpretation limited to interaction | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S011 | M080,M085 | REPORT jama_bot_2019_oi_190007.pdf p6 Table2,p7 Onset | Supplements HR1.05,[.86,1.27],P.65;4488/4656 person-months | COX-MI | K; repetitions match; effectcode contrast definition limitation only; SC06 planned-secondary/post-hoc label | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S012 | M082,M085 | REPORT jama_bot_2019_oi_190007.pdf p6 Table2,p7 Onset | F-BA HR.91,[.75,1.10],P.32;4641/4503 person-months | COX-MI | K; repetitions match; shared effectcode definition limitation only; SC06 shared analysis label | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S013 | M083,M085 | REPORT jama_bot_2019_oi_190007.pdf p6 Table2,p7 Onset | Supplements×F-BA HR.91,[.75,1.11],P.36 | COX-MI | K; repetitions match; interaction kept distinct from joint intervention effect | PASS_1_COMPLETE | AWAITING_PASS_2 |

## Main secondary effects: each outcome/time/contrast separately

Narrative comparisons below use the explicit Table3 footnote d factor2. Rounding compatibility is assessed by allowing each rounded coefficient/endpoint its printed last-digit half-unit. Thus .33 may represent .325 and .12 may represent .124; their doubled displays .65 and .25 are compatible. No hidden exact values are assumed.

| S ID | Mapping key | REPORT exact location: jama_bot_2019_oi_190007.pdf | Coefficient,95% CI,P and matched adjusted mean difference | Profile | Checks | Pass 1 | Pass 2 |
|---|---|---|---|---|---|---|---|
| S014 | M092.overall,M105 | p8 Table3 PHQ supplements overall;p8 text | B.33,[.12,.53],P.002; text MD.65,[.25,1.06],P.002 | GEE-MI | K; factor2 matches after independent display rounding | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S015 | M092.T12,M108 | p8 Table3 PHQ supplements T12;p8 text | B.28,[.05,.50],P.02; text MD.56,[.11,1.01],P.02 | ROBUST-MI | K; factor2 matches after independent display rounding | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S016 | M093.overall | p8 Table3 PHQ F-BA overall | B−.13,[−.33,.07],P.19 | GEE-MI | K; negative symptom coefficient compatible with nonsignificance | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S017 | M093.T12 | p8 Table3 PHQ F-BA T12 | B−.17,[−.39,.06],P.14 | ROBUST-MI | K; narrative no other significant therapy effect agrees | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S018 | M094.overall,M106 | p8 Table3 IDS supplements overall;p8 text | B.60,[.15,1.05],P.01; text MD1.20,[.29,2.10],P.01 | GEE-MI | K; factor2 compatible with rounding; symptom increase direction | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S019 | M094.T12 | p8 Table3 IDS supplements T12 | B.36,[−.19,.90],P.20 | ROBUST-MI | K; overall significance does not imply T12 significance | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S020 | M095.overall | p8 Table3 IDS F-BA overall | B−.23,[−.67,.22],P.32 | GEE-MI | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S021 | M095.T12 | p8 Table3 IDS F-BA T12 | B−.28,[−.83,.27],P.31 | ROBUST-MI | K; Cohen D S033 belongs separate unadjusted baseline/T12 definition | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S022 | M096.overall,M107 | p8 Table3 GAD supplements overall;p8 text | B.25,[.08,.42],P.004; text MD.50,[.16,.84],P.004 | GEE-MI | K; exact displayed factor2 agreement | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S023 | M096.T12 | p8 Table3 GAD supplements T12 | B.14,[−.04,.33],P.13 | ROBUST-MI | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S024 | M097.overall | p8 Table3 GAD F-BA overall | B−.16,[−.32,.01],P.06 | GEE-MI | K; near-null nonsignificance retained | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S025 | M097.T12,M104 | p8 Table3 GAD F-BA T12;p8 text;p9 discussion | B−.24,[−.42,−.06],P.01; text MD−.48,[−.84,−.12],P.01 | ROBUST-MI | K; exact factor2 agreement, lower anxiety narrative and figure direction coherent | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S026 | M098.overall | p8 Table3 utility supplements overall | B−.006,[−.012,.000],P.052 | GEE-MI | K; rounded upper.000 may be slightly positive; no forced exact-zero boundary contradiction | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S027 | M098.T12 | p8 Table3 utility supplements T12 | B−.002,[−.008,.005],P.61 | ROBUST-MI | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S028 | M099.overall | p8 Table3 utility F-BA overall | B.002,[−.003,.008],P.44 | GEE-MI | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S029 | M099.T12 | p8 Table3 utility F-BA T12 | B.004,[−.002,.009],P.23 | ROBUST-MI | K | PASS_1_COMPLETE | AWAITING_PASS_2 |

## Standardized descriptors and qualitative inference

| S ID | Mapping key | Exact location and role | Printed value or inferential statement | Profile | Checks | Pass 1 | Pass 2 |
|---|---|---|---|---|---|---|---|
| S030 | M092.D,M103 | REPORT main p8 Table3 PHQ supplements | Cohen D.10, no CI/P for D | COHEN | Positive sign agrees with poorer supplement PHQ change; no exact imputed group summaries supplied | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S031 | M093.D,M103 | REPORT main p8 Table3 PHQ F-BA | Cohen D−.02, no CI/P for D | COHEN | Direction coherent; adjusted B and baseline/T12 descriptor are different estimands | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S032 | M094.D,M103 | REPORT main p8 Table3 IDS supplements | Cohen D.05, no CI/P for D | COHEN | Positive sign agrees; exact imputed inputs NR | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S033 | M095.D,M103 | REPORT main p8 Table3 IDS F-BA | Cohen D.006, no CI/P for D | COHEN | Small positive D versus negative adjusted B is not a contradiction: unadjusted change and adjusted ANCOVA differ; inputs NR | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S034 | M096.D,M103 | REPORT main p8 Table3 GAD supplements | Cohen D.10, no CI/P for D | COHEN | Direction coherent; inputs NR | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S035 | M097.D,M103 | REPORT main p8 Table3 GAD F-BA | Cohen D−.07, no CI/P for D | COHEN | Direction coherent; inputs NR | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S036 | M098.D,M103 | REPORT main p8 Table3 utility supplements | Cohen D−.07, no CI/P for D | COHEN | Direction coherent; higher utility is better, unlike symptom scales | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S037 | M099.D,M103 | REPORT main p8 Table3 utility F-BA | Cohen D.08, no CI/P for D | COHEN | Direction coherent; no equality with adjusted B asserted | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S038 | M091 | REPORT main p7 secondary interaction prose,p8 Table3 footnote a | PHQ supplements×F-BA no significant interaction; P belongs aggregate range.41–.98, row-specific P NR | INTERACTION-MI | Q; main interactions omitted; nonimputed interactions S098/S099 are distinct variant | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S039 | M091 | REPORT main p7,p8 Table3 footnote a | IDS supplements×F-BA no significant interaction; P aggregate.41–.98,row-specific NR | INTERACTION-MI | Q; no inferred row-specific P | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S040 | M091 | REPORT main p7,p8 Table3 footnote a | GAD supplements×F-BA no significant interaction; P aggregate.41–.98,row-specific NR | INTERACTION-MI | Q | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S041 | M091 | REPORT main p7,p8 Table3 footnote a | Utility supplements×F-BA no significant interaction; P aggregate.41–.98,row-specific NR | INTERACTION-MI | Q | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S042 | U057.narrative | REPORT joi190007supp3_prod.pdf p18 moderation opening | MDD history×supplements: primary outcome not moderated; coefficient/CI/P NR | HISTORY-MOD | Q; statement not confused with main history covariate coefficient | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S043 | U057.narrative | REPORT supplement3 p18 | MDD history×F-BA: primary outcome not moderated; coefficient/CI/P NR | HISTORY-MOD | Q | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S044 | U057.narrative | REPORT supplement3 p18 | MDD history×supplements: PHQ secondary not moderated; coefficient/CI/P/time-specific NR | HISTORY-MOD | Q | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S045 | U057.narrative | REPORT supplement3 p18 | MDD history×F-BA: PHQ secondary not moderated; coefficient/CI/P/time-specific NR | HISTORY-MOD | Q | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S046 | U057.narrative | REPORT supplement3 p18 | MDD history×supplements: IDS secondary not moderated; coefficient/CI/P/time-specific NR | HISTORY-MOD | Q | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S047 | U057.narrative | REPORT supplement3 p18 | MDD history×F-BA: IDS secondary not moderated; coefficient/CI/P/time-specific NR | HISTORY-MOD | Q | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S048 | U057.narrative | REPORT supplement3 p18 | MDD history×supplements: GAD secondary not moderated; coefficient/CI/P/time-specific NR | HISTORY-MOD | Q | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S049 | U057.narrative | REPORT supplement3 p18 | MDD history×F-BA: GAD secondary not moderated; coefficient/CI/P/time-specific NR | HISTORY-MOD | Q | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S050 | U057.narrative | REPORT supplement3 p18 | MDD history×supplements: utility secondary not moderated; coefficient/CI/P/time-specific NR | HISTORY-MOD | Q | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S051 | U057.narrative | REPORT supplement3 p18 | MDD history×F-BA: utility secondary not moderated; coefficient/CI/P/time-specific NR | HISTORY-MOD | Q; no result assumed for unprinted separate time-to-onset moderation | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S052 | M116,U064 | REPORT main p8 concealment;REPORT joi190007supp3_prod.pdf p23 eAppendix13 | P<.001; n759; believed supplements percentages8.2,10.4,25.5,43.7 across four arms,three answers | CONCEAL | Q; matched P/percentages agree; exact test and tested grouping NR; no assumed chi-square df | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S053 | U051,U055 footnote | REPORT joi190007supp3_prod.pdf p12 compliance,p16 footnote | Kappa.73: p12 supplement1,p16 multinutrient | KAPPA | Definition-label comparison SC07; estimate in admissible range; no CI/SE | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S054 | U051,U055 footnote | REPORT joi190007supp3_prod.pdf p12 compliance,p16 footnote | Kappa.70: p12 supplement2,p16 omega | KAPPA | Definition-label comparison SC07; estimate in admissible range; no CI/SE | PASS_1_COMPLETE | AWAITING_PASS_2 |

## Moderation Table A: PHQ at 12 months

All following locations are REPORT joi190007supp3_prod.pdf p18 Table A, B unstandardized, 95% CI/P, MOD-A profile. Netherlands reference has no inferential estimate and is retained in the profile, not an invented S row.

| S ID | Map | Predictor | B | 95% CI | P | Checks | Pass 1 | Pass 2 |
|---|---|---|---:|---|---|---|---|---|
| S055 | U057.a | Supplements | .046 | [−.399,.490] | .841 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S056 | U057.b | F-BA | .288 | [−.155,.731] | .203 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S057 | U057.c | Spain | −.480 | [−1.161,.202] | .168 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S058 | U057.d | UK | .275 | [−.373,.923] | .405 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S059 | U057.e | Germany | .233 | [−.396,.862] | .468 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S060 | U057.f | MDD history | −.536 | [−1.036,−.036] | .036 | K; main history covariate is not intervention×history | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S061 | U057.g | Baseline PHQ | .322 | [.265,.379] | <.001 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S062 | U057.h,M111 | F-BA×baseline PHQ | −.064 | [−.118,−.01] | .020 | K; p18 and main p8/p9 larger reduction at higher PHQ direction match | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S063 | U057.i | Supplements×baseline PHQ | .032 | [−.023,.086] | .259 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |

## Moderation Table B: overall follow-up anxiety

All locations REPORT joi190007supp3_prod.pdf p19 Table B; MOD-B profile, B unstandardized, 95% CI/P; Netherlands reference. Intervals for site terms need not be forced symmetric without an explicit interval engine.

| S ID | Map | Predictor | B | 95% CI | P | Checks | Pass 1 | Pass 2 |
|---|---|---|---:|---|---|---|---|---|
| S064 | U058.a | Supplements | −.107 | [−.384,.17] | .45 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S065 | U058.b | F-BA | −.054 | [−.329,.221] | .703 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S066 | U058.c | Spain | .107 | [−.424,.520] | .694 | K; asymmetric about B, method NR; no symmetry-only candidate | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S067 | U058.d | UK | .117 | [−.371,.638] | .637 | K; asymmetric about B, method NR | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S068 | U058.e | Germany | .058 | [−.401,.606] | .804 | K; asymmetric about B, method NR | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S069 | U058.f | MDD history | −.317 | [−.698,.063] | .102 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S070 | U058.g | Baseline GAD | .464 | [.409,.52] | 0 | K; DISPLAY_ZERO_NOT_CANDIDATE; independent contradiction absent | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S071 | U058.h | F-BA×baseline GAD | −.016 | [−.068,.036] | .554 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S072 | U058.i,M111 | Supplements×baseline GAD | .062 | [.009,.115] | .022 | K; p18 and main p8 higher anxiety at higher baseline direction agree | PASS_1_COMPLETE | AWAITING_PASS_2 |

## Utility moderation: all-site C1 and separate UK/NL C2 tables

All locations REPORT joi190007supp3_prod.pdf p20, B unstandardized,95% CI/P. MOD-C profile; C1 Netherlands reference for site/interactions. Both subgroup headings printed C2; numbering does not alter quantitative identities. Rounded B.000 does not establish an exact zero coefficient.

| S ID | Map | Table/population and predictor | B | 95% CI | P | Checks | Pass 1 | Pass 2 |
|---|---|---|---:|---|---|---|---|---|
| S073 | U059.a | C1 supplements | .000 | [−.012,.012] | .952 | K; rounding compatible | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S074 | U059.b | C1 F-BA | −.006 | [−.018,.006] | .313 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S075 | U059.c | C1 Spain | .005 | [−.012,.022] | .548 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S076 | U059.d | C1 UK | −.014 | [−.031,.003] | .097 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S077 | U059.e | C1 Germany | .011 | [−.006,.027] | .198 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S078 | U059.f | C1 MDD history | .009 | [−.003,.022] | .148 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S079 | U059.g | C1 baseline utility | .498 | [.438,.558] | <.001 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S080 | U059.h | C1 F-BA×Spain | .016 | [−.001,.032] | .066 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S081 | U059.i,M111 | C1 F-BA×UK | .017 | [.001,.033] | .041 | K; UK>NL narrative p18/main p8 matches | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S082 | U059.j | C1 F-BA×Germany | .006 | [−.01,.022] | .452 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S083 | U059.k | C1 supplements×Spain | −.006 | [−.023,.011] | .499 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S084 | U059.l | C1 supplements×UK | −.001 | [−.018,.016] | .907 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S085 | U059.m | C1 supplements×Germany | .002 | [−.014,.017] | .850 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S086 | U060.a | C2 UK supplements | .000 | [−.012,.011] | .944 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S087 | U060.b | C2 UK F-BA | .013 | [.001,.024] | .033 | K; UK benefit direction agrees with C1 comparison | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S088 | U060.c | C2 UK MDD history | .007 | [−.016,.03] | .559 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S089 | U060.d | C2 UK baseline utility | .738 | [.62,.856] | <.001 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S090 | U061.a | C2 NL supplements | .000 | [−.012,.012] | .935 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S091 | U061.b | C2 NL F-BA | −.007 | [−.019,.005] | .267 | K; distinct subgroup model, not exact C1 conditional coefficient identity | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S092 | U061.c | C2 NL MDD history | −.005 | [−.031,.021] | .697 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S093 | U061.d | C2 NL baseline utility | .509 | [.400,.619] | <.001 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |

## Nonimputed sensitivity: every overall and T12 result

All locations REPORT joi190007supp3_prod.pdf p21 eAppendix11. Profile GEE-OBS overall, ROBUST-OBS T12. Effectcoded−1,+1; intervention and interaction included together; site/history/baseline adjusted. Main Table3 excludes interaction and imputes; numeric equality is not expected. Overall shows B95%CI; T12 shows B(SE), not a CI. No guessed variance or degrees of freedom.

| S ID | Map | Outcome/contrast/time | B | CI or SE exactly as labeled | P | Checks | Pass 1 | Pass 2 |
|---|---|---|---:|---|---|---|---|---|
| S094 | U062.a.overall | PHQ supplements overall | .30 | CI[.11,.49] | .002 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S095 | U062.a.T12 | PHQ supplements T12 | .28 | SE.11 | .013 | SE positive; no CI supplied; rounded ratio compatible diagnostically, no exact rule supplied | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S096 | U062.b.overall | PHQ F-BA overall | −.14 | CI[−.34,.05] | .14 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S097 | U062.b.T12 | PHQ F-BA T12 | −.22 | SE.11 | .052 | SE positive; near-threshold result not forced to P<.05 from rounded2.0 ratio | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S098 | U062.c.overall | PHQ interaction overall | −.01 | CI[−.20,.18] | .94 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S099 | U062.c.T12 | PHQ interaction T12 | .02 | SE.11 | .84 | SE positive; low ratio coherent qualitatively | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S100 | U062.d.overall | IDS supplements overall | .55 | CI[.11,.99] | .01 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S101 | U062.d.T12 | IDS supplements T12 | .28 | SE.28 | .30 | SE positive; .275–.285 rounding of numerator/denominator admits ratio1.036 and diagnostic Pabout.30 | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S102 | U062.e.overall | IDS F-BA overall | −.26 | CI[−.70,.18] | .25 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S103 | U062.e.T12 | IDS F-BA T12 | −.36 | SE.28 | .20 | SE positive; no exact inferential rule | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S104 | U062.f.overall | IDS interaction overall | −.01 | CI[−.45,.43] | .96 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S105 | U062.f.T12 | IDS interaction T12 | .12 | SE.28 | .66 | SE positive; no exact inferential rule | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S106 | U062.g.overall | GAD supplements overall | .24 | CI[.08,.40] | .004 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S107 | U062.g.T12 | GAD supplements T12 | .17 | SE.09 | .07 | SE positive; no exact inferential rule | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S108 | U062.h.overall | GAD F-BA overall | −.16 | CI[−.32,.00] | .06 | K; rounded upper.00 can be positive; no boundary-only candidate | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S109 | U062.h.T12 | GAD F-BA T12 | −.26 | SE.09 | .005 | SE positive; lower anxiety direction matches main sensitivity interpretation | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S110 | U062.i.overall | GAD interaction overall | .04 | CI[−.13,.20] | .66 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S111 | U062.i.T12 | GAD interaction T12 | .03 | SE.09 | .74 | SE positive; no exact inferential rule | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S112 | U062.j.overall | Utility supplements overall | −.006 | CI[−.011,.000] | .055 | K; precision permits null within unrounded interval | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S113 | U062.j.T12 | Utility supplements T12 | −.001 | SE.003 | .66 | SE positive; coarse ratio precision retained | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S114 | U062.k.overall | Utility F-BA overall | .002 | CI[−.004,.007] | .51 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S115 | U062.k.T12 | Utility F-BA T12 | .004 | SE.003 | .23 | SE positive; coarse ratio precision retained | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S116 | U062.l.overall | Utility interaction overall | −.002 | CI[−.008,.003] | .42 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S117 | U062.l.T12 | Utility interaction T12 | .001 | SE.003 | .65 | SE positive; coarse ratio precision retained | PASS_1_COMPLETE | AWAITING_PASS_2 |
