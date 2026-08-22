# Main-paper statistical relationship inventory

All IDs are provisional main-local IDs. This is a complete handoff list for both statistical passes; it records definitions and exact printed values without drawing conclusions.

| ID | Source and inferential relationship | Population/contrast/model; cross-document match key |
|---|---|---|
| MS001 | p1 Abstract all-cancer ITT difference 1.69%, 95% CI -0.06% to3.46%, P=.06. | 45/1156 vs64/1147; `MAIN:ITT-all-cancer-count-proportion`. |
| MS002 | p1 Abstract KM 4-y incidence 0.042 (0.032-0.056) vs0.060 (0.048-0.076), P=.06. | treatment vs placebo; `MAIN:KM-all-cancer-4y`. |
| MS003 | p1 Abstract unadjusted Cox HR0.70 (0.47-1.02). | treatment versus placebo; `MAIN:Cox-all-cancer-unadjusted`. |
| MS004 | p1 conclusion says no significantly lower 4-y cancer risk. | Narrative interpretation of MS001-MS003. |
| MS005 | p3 sample size power: 94.4%,86.2%,68.5% under three annual-rate scenarios 2/1%,1.5/.75%,1/.5%. | 1000/group, stated Fleiss equation 4.17. |
| MS006 | p3 methods tests: Fisher exact, chi-square independence, Wilcoxon rank-sum, pooled-variance t; two-sided P<.05, SAS9.4. | Defines compatible rules for mapped results where assigned. |
| MS007 | p4 completion difference .012 (-.013,.037); death difference .002 (-.006,.037). | treatment versus placebo. |
| MS008 | p5 Table2 12mo 25(OH)D difference 12.3 (11.3-13.3), P<.001. | ng/mL treatment-placebo; `MAIN:T2-25OHD-baseline-12mo`. |
| MS009 | p5 Table2 24mo difference12.6 (11.6-13.6), P<.001. | ng/mL. |
| MS010 | p5 Table2 36mo difference12.7 (11.63-13.8), P<.001. | ng/mL. |
| MS011 | p5 Table2 48mo difference11.6 (10.6-12.7), P<.001. | ng/mL. |
| MS012 | p5 Table2 mean visits2-9 difference12.0 (11.1-12.9), P<.001; outside D difference -128.1 (-209.5 to46.6), P=.002; outside calcium -12.0 (-46.0 to22.0), P=.49; dietary D .4 (-7.4 to8.1), P=.93; dietary calcium8.1 (-17.6-33.7),P=.54. | Units as Table2; treatment-placebo. |
| MS013 | p6 Figure2 log-rank P=.06. | all cancer, exclusion54/52, 4-y KM. |
| MS014 | p6 repeats ITT difference1.69% (-.06 to3.46),P=.06. | 45/1156 vs64/1147. |
| MS015 | p6 KM all cancer .042 (.032-.056) vs.060 (.048-.076),P=.06. | 4y, same events/exclusions. |
| MS016 | p6 unadjusted Cox all cancer HR .70 (.47-1.02). | same events/exclusions, no covariate adjustment. |
| MS017 | p6 breast difference .005 (-.007 to.016); log-rank P=.435; KM .018 (.011-.028) vs.023 (.015-.034); Cox HR.79 (.43-1.43). | 19 vs24 diagnoses; exclusion54/52. |
| MS018 | p6 age cancer association HR1.05 (1.02-1.08); age-adjusted treatment HR.70 (.48-1.02); estrogen agonist/antagonist adjusted treatment HR.70 (.47-1.02). | proportional hazards, cancer events and no-follow-up exclusions as primary KM. |
| MS019 | p6 adherence D/placebo mean difference -1.17 (-3.88 to1.55); calcium/placebo -1.7 (-4.51 to1.10). | percentage-point unit implied; includes discontinuers. |
| MS020 | p7 stopping D/placebo difference .017 (-.011 to.044); calcium/placebo .005 (-.028 to.038); renal-calculi .005 (-.004 to.015); high-calcium .003 (-.002 to.010). | treatment-placebo proportions. |
| MS021 | p7 post hoc years2-4: chi-square 3.17% vs4.86%, P=.046; difference1.7% (.1-3.4); log-rank P=.047; Cox HR.65 (.42-.99). | exclusions84/78, cancer34/52; `MAIN:posthoc-years2-4-count-proportion`. |
| MS022 | p7 post hoc achieved 25(OH)D: P=.03, coefficient -.017; HR.65 (.44-.97), for 30-55 ng/mL relative to 30 ng/mL baseline. | Cox covariates defined p3; `MAIN:posthoc-25OHD-HR`. |
| MS023 | p8 prior-trial comparative RRs/P: .40 (.20-.82),P=.01; .53(.27-1.03),P=.06; exclusion year1 .23(.09-.60),P=.005; .59(.29-1.21),P=.15. | Discussion quotation of prior study, not current-trial output. |
| MS024 | p8 external comparator effects: RR2.53(1.49-4.32); RR1.11(.86-1.42); HR1.17(1.02-1.34). | Discussion-supplied comparative context, not current-trial output. |
| MS025 | p9 repeats non-significant primary conclusion at4y. | Narrative match key `MAIN:conclusion-primary-result`. |

Every listed relationship requires explicit `PASS_1_COMPLETE` and `PASS_2_COMPLETE` treatment by the designated statistical reviewers. No display-zero P value was printed in this main paper.
