# Canonical inferential-statistical relationship inventory

This inventory canonically assigns **38 individual statistical relationships**. Separate printed occurrences remain separate stable IDs where cross-location checking is possible. Every row is initialized for the two required independent statistical passes; no candidate determination is made here.

| Stable ID | Local ID; exact location | Printed statistical relationship; population/time/contrast/model | Match / cross-reference | Pass 1 | Pass 2 |
|---|---|---|---|---|---|
| S001 | MS001; DOC-001#page=1 abstract | ITT all-cancer difference1.69%,95%CI-.06 to3.46,P=.06;45/1156 vs64/1147. | `MAIN:ITT-all-cancer-count-proportion`; S014 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S002 | MS002; DOC-001#page=1 abstract | KM4y .042(.032-.056) versus.060(.048-.076),P=.06. | `MAIN:KM-all-cancer-4y`; S015 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S003 | MS003; DOC-001#page=1 abstract | Unadjusted Cox HR.70(.47-1.02), treatment/placebo. | `MAIN:Cox-all-cancer-unadjusted`; S016 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S004 | MS004; DOC-001#page=1 abstract conclusion | Narrative: no significantly lower4-y risk. | interpretation of S001-S003; S025 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S005 | MS005; DOC-001#page=3 | Power94.4/86.2/68.5% under stated1000/group annual-rate scenarios. | sample-size planning | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S006 | MS006; DOC-001#page=3 | Fisher/chi-square/Wilcoxon/pooled-t; two-sidedP<.05,SAS9.4 definitions. | test-rule definitions | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S007 | MS007; DOC-001#page=4 | Completion diff.012(-.013,.037); death diff.002(-.006,.037). | treatment/placebo flow | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S008 | MS008; DOC-001#page=5 Table2 | 12mo25OHD diff12.3(11.3-13.3),P<.001 ng/mL. | `MAIN:T2-25OHD-baseline-12mo` | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S009 | MS009; DOC-001#page=5 Table2 | 24mo25OHD diff12.6(11.6-13.6),P<.001. | `MAIN:T2-25OHD-24-48mo` | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S010 | MS010; DOC-001#page=5 Table2 | 36mo25OHD diff12.7(11.63-13.8),P<.001. | same Table2 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S011 | MS011; DOC-001#page=5 Table2 | 48mo25OHD diff11.6(10.6-12.7),P<.001. | same Table2 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S012 | MS012; DOC-001#page=5 Table2 | Mean visits2-9 diff12.0(11.1-12.9),P<.001; outside-D -128.1(-209.5,46.6),P=.002; outside-Ca -12(-46,22),P=.49; dietary D.4(-7.4,8.1),P=.93; dietary Ca8.1(-17.6,33.7),P=.54. | `MAIN:T2-*` | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S013 | MS013; DOC-001#page=6 Fig2 | All-cancer log-rank P=.06 after exclusion54/52,4y KM. | `MAIN:KM-all-cancer-4y`; S002/S015 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S014 | MS014; DOC-001#page=6 narrative | Repeat ITT difference1.69%(-.06,3.46),P=.06,45/1156 vs64/1147. | `MAIN:ITT-all-cancer-count-proportion`; S001 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S015 | MS015; DOC-001#page=6 narrative | Repeat KM .042(.032-.056)/.060(.048-.076),P=.06. | `MAIN:KM-all-cancer-4y`; S002/S013 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S016 | MS016; DOC-001#page=6 narrative | Repeat unadjusted Cox HR.70(.47-1.02), same events/exclusions/no covariate adjustment. | `MAIN:Cox-all-cancer-unadjusted`; S003 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S017 | MS017; DOC-001#page=6 | Breast difference.005(-.007,.016); log-rankP=.435; KM.018(.011-.028)/.023(.015-.034); HR.79(.43-1.43). | `MAIN:breast-cancer-4y` | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S018 | MS018; DOC-001#page=6 | Age HR1.05(1.02-1.08); treatment age-adjusted HR.70(.48-1.02); estrogen-adjusted HR.70(.47-1.02). | Cox primary analysis | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S019 | MS019; DOC-001#page=6 | Adherence differences -1.17(-3.88,1.55) and-1.7(-4.51,1.10). | includes discontinuers | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S020 | MS020; DOC-001#page=7 | Stopping diff.017(-.011,.044)/.005(-.028,.038); calculi.005(-.004,.015); high calcium.003(-.002,.010). | proportion contrasts | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S021 | MS021; DOC-001#page=7 | Years2-4 chi-square3.17%/4.86%,P=.046,diff1.7%(.1-3.4); log-rankP=.047; Cox HR.65(.42-.99); exclusions84/78. | `MAIN:posthoc-years2-4-count-proportion`; S034 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S022 | MS022; DOC-001#page=7 | 25OHD post hoc P=.03,coefficient-.017,HR.65(.44-.97)30-55 versus30ng/mL. | `MAIN:posthoc-25OHD-HR`; S036-S038 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S023 | MS023; DOC-001#page=8 | Prior-study RR/P values .40(.20-.82),P.01;.53(.27-1.03),P.06;.23(.09-.60),P.005;.59(.29-1.21),P.15. | comparative context, not current outcome | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S024 | MS024; DOC-001#page=8 | External RR2.53(1.49-4.32),RR1.11(.86-1.42),HR1.17(1.02-1.34). | comparative context | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S025 | MS025; DOC-001#page=9 | Repeat narrative nonsignificant4-y primary conclusion. | S004 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S026 | SS001; DOC-002#page=3 Table5 | Planned power grid by RR/base rate/n/attrition/hazard assumptions. | protocol planning only | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S027 | SS002; DOC-002#pages=3-4 Table6 | Pilot site RR/CI/P plus alpha=.10 planned power; retains site/pilot/first-year restriction. | protocol pilot only | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S028 | SS003; DOC-002#page=8 | Planned Cox one-unit log-HR coefficient,AFT,two-sidedP<.05 definition. | planned endpoint definition | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S029 | SS004; DOC-002#page=8 | Planned Cox/AFT/LIFETEST/logistic/person-time/GENMOD alternative estimands. | model-match prerequisite | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S030 | SS005; DOC-002#page=9 | Interim alpha′(0)=0,alpha′(.5)=.0025,alpha′(1)=.05. | planned interim only | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S031 | SS006; DOC-002#page=9 | Planned two-sided t of75 matched differences,null0,alpha.05; alternatives. | nested CC plan | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S032 | SS007; DOC-002#page=9 | Planned Fisher/Yates chi-square/PH and 25OHD quintile/trend analyses. | secondary endpoint plan | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S033 | SS008; DOC-002#page=10 | QC 95% CI upper error>.05% triggers re-entry. | data-QC rule | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S034 | SS009; DOC-003#page=2 eFig1 | Post-hoc invasive/in-situ years2-4 stratified log-rankP=.0469 after stated exclusion. | S021 comparable but precision/wording differs | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S035 | SS010; DOC-003#page=3 eFig2A | Age-only Cox martingale residual/loess diagnostic,range6-107ng/mL. | functional-form diagnostic | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S036 | SS011; DOC-003#page=4 eFig2B | Age-adjusted Cox/loess coefficient-.017,P=.03,HR.65(.44-.97),30-55 versus30ng/mL. | S022 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S037 | SS012; DOC-003#page=5 eFig2C | HR-scale transformation of S036 with95% bands,30ng/mL HR1. | S036 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S038 | SS013; DOC-003#page=6 | Time-varying two-interval25OHD Cox, age-adjusted residual/loess and exponentiated rescaling. | S035/S036 model definition | PASS_1_COMPLETE | PASS_2_COMPLETE |

## Coverage and retained matches

DOC-001 contributes S001-S025 (PDF pp.1,3-9; no inferential result on p2 or p10). DOC-002 contributes S026-S033 (pp.3-4 and8-10; planning definitions on remaining pages are numeric-only). DOC-003 contributes S034-S038 (pp.2-6; p1 index only). Exact/repeated result locations are cross-referenced rather than collapsed: S001/S014, S002/S013/S015, S003/S016, S004/S025, S021/S034, and S022/S036/S037/S038. No display-zero P value appears in any mapped source.
