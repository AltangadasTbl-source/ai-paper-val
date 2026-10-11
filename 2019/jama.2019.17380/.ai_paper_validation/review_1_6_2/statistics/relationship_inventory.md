# Statistical relationship inventory — Workflow 1.6.2

Pass 2 closure: fresh named statistical runtime /root/statistical_pass_2, gpt-6.1-sol/high, distinct from /root/statistical_pass_1. Every S001–S082 record is PASS_2_COMPLETE, retaining PASS_1_COMPLETE. Full independent per-relationship facts, all constituent-row checks, all 25 checker-exclusion audits and all 18 candidate/recheck implications are in [statistical_pass_2.md](../checkers/statistical_pass_2.md). New pass-2 findings: 0; additional pass-2 exclusions: 0. Exact reconstruction limits remain named rather than treated as omitted relationships.

Runtime agent: /root/statistical_pass_1; role qc162_statistical_consistency_reviewer; model gpt-6.1-sol; reasoning high; fresh mandatory pass 1. Stable mapper IDs are preserved: S001–S082, exactly 82 relationship groups; no extension IDs were needed. A grouped ID covers every constituent row, displayed interval, test, method and matching source statement rather than a sample. Direct sources: DOC-001 REPORT main article pp.1–11; DOC-002 PLAN protocol/addendum pp.1–33; DOC-003 REPORT results supplement pp.1–19; DOC-004 REPORT sharing statement p.1, with no inferential relationship. All source roles assigned by content.

Read completely QUALITY_CONTROL_SCOPE.md, workflow_1_6_2/review_contract.md and START_PROMPT.md. Source-matched maps are locators; supplied PDF pages and visual page renderings control. Historical extracts are not scientific conclusions. Normal diagnostics are explicitly diagnostic, not reconstructions of unstated Rubin degrees of freedom, covariance or Cox test identity. Noninferiority, equivalence and ancillary stopping rules are not supplied and are not inferred. No Python, external evidence or old conclusions used.

## Stable relationship evidence and pass status

| ID | Exact mapped source location | Printed relationship / all constituent scope | Pass 1 | Pass 2 |
|---|---|---|---|---|
| S001 | p1 abstract;pp2/4matching;Table2p8 |D change−12.3CI−13.4,−11.2;placebo−13.1CI−14.2,−11.9;difference.9CI−.7,2.5;nonsignificant5y | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S002 | p1 abstract;pp2/4matching;Table2p8 |Ochange−12.2CI−13.3,−11.1;placebo−13.1CI−14.2,−12.0;difference.9CI−.7,2.6;nonsignificant5y | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S003 | p2 outcomes |Primary changealbuminuria changedtoeGFRin2016;5yextension disclosed;not slope coefficient | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S004 | p3 sample size |1320→80%power for≥2.3difference;α.05two-sided;80%followups;preliminarychange distributions in plan;clinicalsurrogate≥.75/year≥3.75/5y | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S005 | p3 continuous model/test |Randomintercept;3categoricaltimes;treatment×time;age/sex+timeinteraction;baselineACR+timeinteractiononlyeGFR;year5interactionP;2tailedP<.05;secondaryexploratory | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S006 | p3 missingness/populations |Allrandomized;MI20,Rubin;completecasebaseline+year5;highadherence;ACRexcludeUTIsymptoms | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S007 | p3 subgroup plan/method |D race/25OHD/ACR/eGFRprespecified;BMIadded;Oomegain­dex/CRPprespecified;fishadded;subgroupmain/time/threewayinteraction;Waldthreewaytest | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S008 | p3 categorical method |CoxPH;Schoenfeldresidualtest;R3.6.0 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S009 | p4 biomarkers |Year2 D25OHD41.4SD11.0vs29.8SD11.1ng/mL,P<.001;Oindex3.6SD1.0%vs2.3SD.8%,P<.001 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S010 | p4 overall change |Fullanalytic−12.7CI−13.6,−11.7;932baseline/year5eGFR−12.4CI−13.3,−11.4 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S011 | p4 interaction/sensitivity |D×OP.42;primarysensitivitiescompletecase/highadherence similar;no subgroupheterogeneity;year2biomarkerchange notsignificantlycorrelatedwith5yeGFRchange | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S012 | p4 secondary narrative |3prespecifiednone significant;compositeHRD.92CI.68,1.25;O1.11CI.81,1.50;40%declinenotsignificant;ACRnotreatmentdifference;subgroup/sensitivitysimilar | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S013 | p4 posthoc narrative |40%decline/kidneyfailureand30%declinecomposites notprespecified;notsignificant;matchesdefinitionp3 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S014 | p6 PH/discussion |NostatisticallysignificantPHviolations anysecondary;nosignificantprimary/sensitivity/secondarydifference;5ychange akin eGFRslope | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S015 | p7 discussion |95%CIsexcluded3.75differenceover5y;insufficientcompositeevents;HRsclose1;secondarynullsupportsprimary;albuminuriaapproximately3fold | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S016 | Table2p8 Dbaseline |Active n701,eGFR86.3CI84.6–88.0;placebo607,85.3CI83.7–87.0;fourmissingbaseline | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S017 | Table2 Dyear2 |Active531,80.6CI78.8–82.4;change−5.2CI−6.2,−4.2;placebo459,79.3CI77.3–81.2;change−6.1CI−7.1,−5.1;difference.9CI−.6,2.5;noPprinted | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S018 | Table2 Dyear5 |Active496,74.3CI72.3–76.2;change−12.3CI−13.4,−11.2;placebo438,72.5CI70.6–74.5;change−13.1CI−14.2,−11.9;difference.9CI−.7,2.5;P.25 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S019 | Table2 Obaseline/year2 |Baselineactive657,85.7CI84.1–87.3;placebo651,86.0CI84.2–87.8. Year2active499,79.4CI77.6–81.2;change−5.7CI−6.8,−4.7;placebo491,80.6CI78.6–82.5;change−5.5CI−6.5,−4.6;difference−.3CI−1.8,1.3;noPprinted | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S020 | Table2 Oyear5/footnotes |Active472,73.7CI71.8–75.6;change−12.2CI−13.3,−11.1;placebo462,73.2CI71.1–75.3;change−13.1CI−14.2,−12.0;difference.9CI−.7,2.6;P.27. Modeledage/sex/baselineACRadjustedMI;changesMIallparticipants;positivehigher/slowerdecline;Ptest5ychange | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S021 | Figure3p8 overall |Printedplacebo703,−13.1SD14.4;D609,−12.3SD14.8;adjustedforestpositivemarker,intervalspans0 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S022 | Figure3 white |Placebo451,−12.1SD13.7;D406,−11.7SD13.5;forestpositive,intervalspans0;raceinteractionP.58sharedblack | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S023 | Figure3 black |Placebo148,−15.9SD16.0;D130,−14.7SD17.1;forestpositive,intervalspans0;P.58 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S024 | Figure3 ACR<30 |Placebo635,−12.4SD14.2;D559,−11.8SD14.4;forestpositive,intervalspans0;ACRinteractionP.36 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S025 | Figure3 ACR≥30 |Placebo67,−20.4SD15.0;D50,−17.3SD17.4;forestpositive,intervalspans0;P.36 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S026 | Figure3 25OHD<20 |Placebo110,−14.6SD13.9;D85,−12.2SD17.1;forestpositive,intervalspans0;25OHDinteractionP.15 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S027 | Figure3 25OHD20–<30 |Placebo230,−14.7SD15.2;D203,−12.4SD14.0;forestpositive,intervalspans0;P.15 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S028 | Figure3 25OHD≥30 |Placebo332,−11.5SD13.9;D297,−12.3SD14.6;forestnegative,intervalspans0;P.15 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S029 | Figure3 eGFR≥60/<60 |≥60:placebo612,−14.1SD14.4;D531,−13.7SD14.5;positiveforest. <60:placebo89,−5.8SD12.4;D76,−3.0SD13.6;positiveforest. Bothintervalsspannull;interactionP.18 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S030 | Figure3 BMI<25/25–<30 |<25:placebo87,−12.9SD13.2;D87,−10.5SD11.7;25–<30:placebo228,−12.3SD14.1;D205,−12.2SD14.4;bothforestpositive,span0;BMIinteractionP.79 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S031 | Figure3 BMI≥30 |Placebo364,−13.7SD15.0;D294,−12.8SD15.7;forestpositive,span0;P.79. Source lacks closingparenthesisafter15.0;valuepreserved | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S032 | Figure3 Oassignment/plotcaption |Oplacebo:printedplacebo333,−13.2SD14.9;D320,−13.0SD14.7;Oactive:printedplacebo370,−12.9SD13.9;D289,−11.7SD14.9;bothpositiveforest,span0;P.42. Plotaxis−4,−2,0,2,4,6,8,10;active−placebo95%CI;adjustedage/sex/baselineACR;baseline→year5 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S033 | Figure4p9 overall |Printedplacebo659,−13.1SD14.8;O653,−12.2SD14.5;positiveforest,intervalspans0 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S034 | Figure4 EPA/DHA≤2.2% |Placebo332,−13.3SD15.0;O347,−12.5SD14.6;positiveforest,span0;omegaindexinteractionP.72 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S035 | Figure4 EPA/DHA>2.2% |Placebo308,−12.9SD14.6;O292,−11.9SD14.4;positiveforest,span0;P.72 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S036 | Figure4 ACR<30 |Placebo596,−12.6SD14.8;O598,−11.5SD13.8;positiveforest,span0;ACRinteractionP.70 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S037 | Figure4 ACR≥30 |Placebo62,−18.1SD14.2;O55,−19.1SD18.3;markerat/near0,intervalspans0;P.70 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S038 | Figure4 hsCRP≤.2mg/dL |Placebo334,−12.9SD14.3;O335,−11.5SD13.4;positiveforest,span0;CRPinteractionP.73 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S039 | Figure4 hsCRP>.2mg/dL |Placebo323,−13.3SD15.3;O316,−13.0SD15.5;positiveforest,span0;P.73 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S040 | Figure4 fish<1.5servings/week |Placebo354,−13.4SD15.3;O329,−11.8SD14.7;positiveforest,span0;fishinteractionP.51 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S041 | Figure4 fish≥1.5servings/week |Placebo295,−12.9SD14.3;O310,−12.7SD14.3;positiveforest,span0;P.51 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S042 | Figure4 Dassignment/plotcaption |Dplacebo:printedplacebo289,−13.2SD14.9;O320,−12.9SD13.9;Dactive:printedplacebo370,−13.0SD14.7;O333,−11.7SD14.9;bothpositiveforest,span0;P.42. Axis−6,−4,−2,0,2,4,6;active−placebo95%CI;age/sex/baselineACRadjustment;baseline→year5 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S043 | Table3p9 Dcomposite |Eventsactive85/placebo79;ratesper100person-years2.5CI2.0–3.0/2.7CI2.1–3.3;rate difference−.2CI−1.0,.6;HR.92CI.68–1.25;P.61 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S044 | Table3 D40%decline |Events42/38;rates1.6CI1.1–2.1/1.7CI1.2–2.1;difference−.1CI−.7,.6;HR.97CI.63–1.51;P.90 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S045 | Table3 DACRdoubling+≥30 |Events111/74;rates4.4CI3.6–5.2/3.3CI2.5–4.0;difference1.1CI.0,2.2;HR1.34CI1.00–1.80;P.05 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S046 | Table3 Ocomposite |Events86/78;rates2.7CI2.2–3.3/2.5CI1.9–3.0;difference.3CI−.5,1.1;HR1.11CI.81–1.50;P.52 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S047 | Table3 O40%decline |Events40/40;rates1.6CI1.1–2.1/1.6CI1.2–2.1;difference.0CI−.7,.7;HR.99CI.64–1.54;P.97 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S048 | Table3 OACRdoubling+≥30 |Events96/89;rates4.0CI3.2–4.8/3.7CI3.0–4.5;difference.3CI−.8,1.4;HR1.08CI.81–1.44;P.60 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S049 | Table3 labels/footnotes |Prespecifiedsecondary:composite,40%decline,ACRchange;ACRanalyzedtime-doubling≥30here/continuous eTable6;CoxHR;omit4baselineeGFR/1baselineACRmissing;PnullHR1;person-time denominatorsnotprinted | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S050 | pp9–10 subgroup/conclusion |FavoredDpointestimatesCKD/lowD/normalBMI;CIsnullcrossing;interactionnotsignificant;hypothesisgenerating. Modestmeasurements limit slopes/time-to-event;eventsinsufficient;subgroupnotpowered;missingnessMI+completecase;no5ydifference | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S051 | [protocol pp12–14](../../../joi190122supp1_prod.pdf#page=12) | Parent inclusion: men ≥60, women ≥65; high school education or higher; nonstudy vitamin D ≤800 IU/d, calcium ≤1200 mg/d; forego fish oil; placebo-run-in adherence >67%; ancillary self-reported physician diabetes and return both baseline blood/urine. Parent exclusions: known CVD (MI, stroke, TIA, angina, CABG, PCI), cancer except nonmelanoma skin cancer, kidney stones, kidney failure/dialysis, hypercalcemia, hypo/hyperparathyroidism, cirrhosis, granulomatous disease, fish allergy, serious illness precluding participation. Ancillary exclusions: diabetes only in pregnancy; diagnosis before 30 and initially insulin-treated; known kidney disease cause other than diabetes; kidney transplant. p14 enrollment algorithm explicitly says a known cause other than “diabetes of hypertension”; preserve this printed wording as a location detail. Key: report eligibility/analysis population. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S052 | [p14](../../../joi190122supp1_prod.pdf#page=14) | Individual participant 2×2 factorial; computer random numbers stratified in 5-year age groups, blocks of 8, two participants in each of four combinations. First 1500 eligible parent participants enrolled; run-in 3–6 months (p13). Key: report randomization/strata. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S053 | [pp15–16](../../../joi190122supp1_prod.pdf#page=15) | Cholecalciferol 2000 IU daily, printed as 40 µg; one pill/d, matching placebo, anticipated 25(OH)D increment ≈16 ng/mL; discontinue on kidney stones/hypercalcemia. Fish oil 1000-mg capsule containing 840 mg EPA+DHA/d, EPA:DHA 40:30, contains no vitamin D. Baseline and year-4 first-morning urine/blood/questionnaires; parent baseline blood separate consent. p21 repeats 2000 IU (40 µg), and cites UL as 50 µg or 2000 IU, allowed external supplements ≤800 IU, total ≤2800 IU. Key: report dose and follow-up; N101 preserves units. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S054 | [p17](../../../joi190122supp1_prod.pdf#page=17) | Original primary: change in urine ACR baseline to year4, continuous, percent change (ACR4−ACR0)/ACR0, log-normalization rationale. Key: amended primary status; reported ACR status. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S055 | [p17](../../../joi190122supp1_prod.pdf#page=17) | eGFR secondary; text says “secondary dichotomous outcome” then “analyzed as a continuous variable”; absolute eGFR4−eGFR0, no transformation. Equation eGFR=177.6×SCr^(−0.65)×CysC^(−0.57)×age^(−0.20)×(0.82 if female)×(1.11 if black); SCr mg/dL, CysC mg/L; cited measured-GFR variation explained 89%. Key: report primary eGFR, estimating equation. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S056 | [p17](../../../joi190122supp1_prod.pdf#page=17) | Original additional secondary composite: albuminuria progression (100% increase and year4 ACR ≥30 mg/g), rapid eGFR loss (≥12 mL/min over four years), ESRD (maintenance dialysis/transplant verified records), and/or death. Composite defined as proportion; threshold rationale 3 mL/min/year. Key: amended composite and report status/components. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S057 | [pp17–18](../../../joi190122supp1_prod.pdf#page=18) | Original interaction for each primary and secondary outcome: additive contrast both-active versus double-placebo compared with sum of each singly-active contrast; multiplicative interaction by ANCOVA logACR4=β0+β1logACR0+β2D+β3ω+β4(D+ω)+ε, where final term is indicator of both active, β4 P<.05. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S058 | [p18](../../../joi190122supp1_prod.pdf#page=18) | If either-scale interaction for an outcome, all its analyses compare three active combinations individually with double-placebo; otherwise marginal factorial comparisons each agent versus its placebo. Key: report interaction P and factorial contrasts. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S059 | [p18](../../../joi190122supp1_prod.pdf#page=18) | Original primary ANCOVA logACR4=β0+β1logACR0+β2D+ε; exp(β2)−1 interpreted relative difference in percent change, 95% CI/P. Parallel ω analysis. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S060 | [p18](../../../joi190122supp1_prod.pdf#page=18) | Original eGFR ANCOVA eGFR4=β0+β1eGFR0+β2D+ε; β2 active-minus-placebo difference; parallel ω analysis; substitute rank-sum if distributions indicate; composite chi-square proportions. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S061 | [p18](../../../joi190122supp1_prod.pdf#page=18) | Alpha .05 without multiple-comparison correction. Original ITT continuous analysis includes only participants with baseline AND year4 measurement, regardless of medication adherence (complete case). Key: later imputation and reported all-randomized population. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S062 | [p18](../../../joi190122supp1_prod.pdf#page=18) | Imbalanced baseline characteristics added as secondary ANCOVA covariates; medication/HbA1c/CRP differences explored for mediation by adding covariates and changes toward/away from null treatment coefficient. No fixed age/sex/ACR adjustment specified here. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S063 | [pp18–19](../../../joi190122supp1_prod.pdf#page=19) | Vitamin D prespecified subgroups: baseline plasma 25(OH)D, ACR, eGFR, race/ethnicity; benefit expected in low 25(OH)D, ACR≥30 or eGFR<60, non-Caucasian. Omega-3 subgroups baseline EPA+DHA and CRP, greater benefit with low EPA+DHA/high CRP. Treatment×subgroup ANCOVA interactions. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S064 | [p19](../../../joi190122supp1_prod.pdf#page=19) | Original exploratory adherence ≥80% medications; biomarker concentration changes replace assignment in ANCOVA to associate with ACR/eGFR changes; explicitly cautious postrandomization interpretation. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S065 | [p19](../../../joi190122supp1_prod.pdf#page=19) | Power inputs: independent equal allocation; logACR follow-up mean3.085 SD1.59 correlation baseline .78 (MESA); eGFR mean70 SD25 correlation .834 (CHS); 20% loss; ANCOVA significance .05, target1500, follow-up1200. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S066 | [pp19–20](../../../joi190122supp1_prod.pdf#page=19) | 90% power at observed ACR difference17%, eGFR2.6. Table2 labeled “co-primary”: ACR15/17/19/21/23/25% -> power81/90/96/98/>99/>99%; eGFR2.0/2.2/2.4/2.6/2.8/3.0 ->71/79/85/90/94/97%. All differences four-year total, not yearly. With80% adherence,17% and2.6 correspond to21% and3.2 among adherent. Loss10%/N1350 =>93% power; loss30%/N1050 =>86%. Interaction requiring combination comparison =>80% atACR20%,eGFR3.2. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S067 | [p20](../../../joi190122supp1_prod.pdf#page=20) | Secondary-composite power: ACR progression and rapid eGFR loss incidence ≈17% each, ESRD<1%, death≈4.6%, expected joint20–30%;80% power RR .69–.76 or lower;90% RR .65–.73 or lower. Figure11 plots power versus relative risk with four fixed cumulative-incidence curves (30%,25%,20%,15%); no exact extra estimates are printed in the text, curve positions are not numerical observations. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S068 | [p23](../../../joi190122supp1_prod.pdf#page=23) | Parent DSMB annual unblinded endpoint/adverse-effect review, Haybittle–Peto z3 (P=.0027), final close nominal significance; guideline decisions examine totality, primary parent cancer/CVD endpoints. Scope distinction: no separately stated ancillary interim decision. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S069 | [pp31–32](../../../joi190122supp1_prod.pdf#page=31) | Analytic-plan addendum submitted NIH renewal03/02/2015, implemented02/24/2016. p32 says extension “from2 to5years” and eGFR baseline→year5 supplants two-year albuminuria/eGFR changes as primary. Key: disclosed amendments and primary status/timing. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S070 | [p32](../../../joi190122supp1_prod.pdf#page=32) | Amended primary eGFR5−eGFR0. Secondary ACR baseline→years2 and5; time to rapid eGFR loss (≥40% baseline to year2 or5); time to composite rapid eGFR loss, ESRD (records-confirmed maintenance dialysis/transplant), or death. Key: report secondary/exploratory outcomes. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S071 | [p32](../../../joi190122supp1_prod.pdf#page=32) | Amended ITT expressly all participants returning ≥1 follow-up biosample regardless adherence/postrandomization features; multiple imputation for missing year5 eGFR by chained equations, baseline data/year2 eGFR/ACR,10 datasets,Rubin combination. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S072 | [p32](../../../joi190122supp1_prod.pdf#page=32) | Amended interaction LMM: eGFRij=β0+β1Di+β2ωi+β3Diωi+β4Di tij+β5ωi tij+β6Diωi tij+ai+εij; j=0,2,5; categorical time, patient random effect;β6 P<.05 interaction. If interaction three active combinations vs double-placebo; otherwise marginal comparisons. Preserve printed equation; no added time-main-effect term. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S073 | [p32](../../../joi190122supp1_prod.pdf#page=32) | Primary random-intercept LMM eGFRij=β0+β1Di+β2tij+β3Di tij+ai+εij;β3 treatment difference in change,95%CI/P; description atyears2/5 but inference year5 only; corresponding ω and log-ACR models. Key: reported repeated-measures model/categorical time. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S074 | [pp32–33](../../../joi190122supp1_prod.pdf#page=33) | Sensitivity terms for baseline imbalance; follow-up medication,HbA1c,CRP,IL6 covariates explored as mediators/attenuators; secondary categorical outcomes discrete Cox proportional hazards. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S075 | [p33](../../../joi190122supp1_prod.pdf#page=33) | Amended vitamin D subgroups total AND bioavailable baseline25(OH)D,ACR,eGFR,race/ethnicity; hypothesized greater low25(OH)D,DKD(ACR≥30 or eGFR<60),Caucasian. Omega-3 baseline EPA+DHA,hsCRP;lowEPA+DHA/highhsCRP; treatment×subgroup LMM. Key: report prespecified subgroup list and thresholds. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S076 | [p33](../../../joi190122supp1_prod.pdf#page=33) | Amended exploratory adherent subset continuous adherence≥80%; biomarker change replaces randomized assignment in LMM for ACR/eGFR; postrandomization interpretation caution. Key: report≥two-thirds adherence in four/six questionnaires and complete biomarker correlations. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S077 | [p33](../../../joi190122supp1_prod.pdf#page=33) | Amended simulation2000replications, independent/equal allocation,1058(80%)≥1follow-up blood sample,no interaction,eGFR variation from preliminary cohort;80%power two-sidedα=.05 for2.3mL/min/1.73m² year5difference. Figure7 smooth power curve with x ticks0,1,2,3mL/min/1.73m² and y .2,.4,.6,.8,1; no additional pointwise values printed; no secondary power because incidence hard to predict. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S078 | [supplement pp2–4](../../../joi190122supp2_prod.pdf#page=2) | Laboratory calibration relation N102 below; match report eGFR cystatinC definition and assay QC. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S079 | [supplement p6](../../../joi190122supp2_prod.pdf#page=6) | Adherence at individual time ≥two-thirds; throughyear2≥2/3 questionnaires; throughyear5≥4/6; questionnaire-response denominator, not all randomized. N103 all counts. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S080 | [supplement pp9–14](../../../joi190122supp2_prod.pdf#page=9) | All six continuous tables retain full rows in appendix. eGFR adjusted LMM age,sex,baselineACR; ACR adjusted LMM age,sex; missing data multiple imputation; change summarized over all participants with imputation. Between-group effect model-based active-minus-placebo for eGFR, active/placebo ratio of geometric change for ACR. P tests year5 change only. eTable4 complete-case blood population; eTable5 adherent; eTable6 all; eTable7 paired urine; eTable8 adherent; eTable9 excludes UTI-symptom visits. Matching key primary eGFR versus secondary ACR and sensitivity population. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S081 | [supplement p15](../../../joi190122supp2_prod.pdf#page=15) | eTable10 explicitly all analyses not prespecified/post-hoc; CoxHR active/placebo,P nullHR1; excludes4missingbaselineeGFR,1missingbaselineACR. N112 retains event/rate/difference/CI/P triples. Matching key report categorical outcomes/status and definitions. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S082 | [supplement pp17–19](../../../joi190122supp2_prod.pdf#page=17) | Biomarker correlations use only all-data participants, biomarker baseline→year2 versus eGFRbaseline→year5. ACR subgroup figures age/sex-adjusted, ratio active/placebo95%CI as plotted, counts/geometricSD; caption calls estimates difference. Numeric intervals are graphical only, not printed numeric endpoints; axis/logscale details below. Matching keys subgroup effects, interaction, exposure change correlations. | PASS_1_COMPLETE | PASS_2_COMPLETE |

## Per-relationship pass-1 facts

### S001

**Pass 1:** PASS_1_COMPLETE. Primary vitamin D estimates, CIs and nonsignificance agree across abstract, Key Points, narrative and Table 2. Every estimate is contained in its ordered CI; active-minus-placebo direction is positive.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S002

**Pass 1:** PASS_1_COMPLETE. Primary omega-3 estimates, CIs and nonsignificance agree across matched locations. Difference 0.9 (−0.7, 2.6) includes zero and has the reported positive direction.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S003

**Pass 1:** PASS_1_COMPLETE. Original ACR primary versus amended/reported eGFR primary is F-ST1-008 under route A, category 5. The supplied 2016 amendment is a documented alternative, not an exclusion ground.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S004

**Pass 1:** PASS_1_COMPLETE. 1320 × 80% = 1056 versus plan 1058 is within display precision. Final simulation lacks the preliminary variance/covariance inputs needed for exact power reproduction; no substitute variance is assumed.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S005

**Pass 1:** PASS_1_COMPLETE. Repeated observations, random intercept, categorical time and year-5 interaction test are coherent. Fixed primary covariates differ from amended Equation 2: F-ST1-003. Two-sided alpha .05 and exploratory secondary interpretation agree.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S006

**Pass 1:** PASS_1_COMPLETE. All randomized participants and 20 imputations differ from the amended follow-up-conditioned population and 10 imputations: F-ST1-001/002. Complete-case sensitivity is a distinct population. Adherence comparison is F-ST1-004.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S007

**Pass 1:** PASS_1_COMPLETE. Subgroup P values test heterogeneity, rather than individual subgroup effects. Bioavailable 25(OH)D analysis is absent: F-ST1-005. BMI and fish-intake additions are disclosed.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S008

**Pass 1:** PASS_1_COMPLETE. Cox PH and Schoenfeld checks match the stated time-to-event design. Risk sets, event times, tie method and exact test type are unavailable; no printed HR/CI/P conflict is established.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S009

**Pass 1:** PASS_1_COMPLETE. Biomarker differences 11.6 ng/mL and 1.3 percentage points have the expected active-exposure direction and stated P<.001. Test identity and exact sample counts are absent; SDs alone do not reproduce the tests.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S010

**Pass 1:** PASS_1_COMPLETE. Full-imputed −12.7 and paired-participant −12.4 changes describe different populations. Both CIs are ordered and contain their estimates, so they are not competing estimates for one matched analysis.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S011

**Pass 1:** PASS_1_COMPLETE. Treatment interaction P=.42 supports marginal factorial comparisons under the stated rule. Sensitivity estimates and all subgroup interaction tests reconcile; biomarker correlations are checked separately.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S012

**Pass 1:** PASS_1_COMPLETE. Composite HRs include one and support nonsignificance. Other secondary triples reconcile. Standalone categorical ACR prespecification is F-ST1-006.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S013

**Pass 1:** PASS_1_COMPLETE. Report explicitly labels the additional composites post hoc, matching eTable 10. All eight inferential triples include the null and have P>.05.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S014

**Pass 1:** PASS_1_COMPLETE. No printed Schoenfeld statistic conflicts with the PH narrative. Discussion nonsignificance agrees with results. “Akin to slope” is a contextual analogy to five-year change.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S015

**Pass 1:** PASS_1_COMPLETE. Primary upper CI limits 2.5 and 2.6 exclude the stated 3.75 five-year improvement threshold; .75 × 5 = 3.75. No noninferiority or equivalence conclusion is claimed.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S016

**Pass 1:** PASS_1_COMPLETE. Baseline counts 701+607=1308 reconcile with four missing of 1312. Both mean CIs contain their estimates and have ordered endpoints.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S017

**Pass 1:** PASS_1_COMPLETE. Every vitamin D year-2 mean, change and contrast CI is ordered and contains its estimate. Positive contrast direction agrees with the arm changes. No year-2 P is printed, as inference is reserved for year 5.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S018

**Pass 1:** PASS_1_COMPLETE. Vitamin D year-5 contrast 0.9 (−0.7, 2.5), P=.25 agrees on significance. Normal diagnostic P=.270 reconciles after half-unit rounding; no Rubin degrees of freedom are inferred.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S019

**Pass 1:** PASS_1_COMPLETE. Every omega-3 baseline/year-2 CI contains its estimate. Negative year-2 adjusted contrast agrees with greater active-arm decline. Rounded arm changes are not substituted for a modeled contrast.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S020

**Pass 1:** PASS_1_COMPLETE. Omega-3 year-5 contrast 0.9 (−0.7, 2.6), P=.27 agrees on significance. Normal diagnostic P=.285 reconciles after rounding. Footnote distinguishes imputed summaries from adjusted contrasts.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S021

**Pass 1:** PASS_1_COMPLETE. Figure 3 overall forest estimate is positive and its CI spans zero, matching Table 2. The printed group-count assignment discrepancy belongs to the numeric lane; SDs do not reconstruct the adjusted effect.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S022

**Pass 1:** PASS_1_COMPLETE. White subgroup marker is contained and its interval spans zero. Race P=.58 is a shared interaction test, not a test of the white subgroup effect.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S023

**Pass 1:** PASS_1_COMPLETE. Black subgroup marker is contained and its interval spans zero. Race P=.58 agrees with nonsignificant heterogeneity; the adjusted forest estimate remains separate from the crude mean difference.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S024

**Pass 1:** PASS_1_COMPLETE. ACR<30 subgroup forest is positive with a CI spanning zero. P=.36 tests heterogeneity across ACR strata, rather than this stratum's null effect.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S025

**Pass 1:** PASS_1_COMPLETE. ACR≥30 subgroup marker is contained and its CI spans zero. Shared P=.36 is nonsignificant heterogeneity; no numeric CI is fabricated from counts and SDs.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S026

**Pass 1:** PASS_1_COMPLETE. Low 25(OH)D subgroup forest is positive and spans zero. P=.15 is the categorical interaction test, not this subgroup's effect test.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S027

**Pass 1:** PASS_1_COMPLETE. Middle 25(OH)D subgroup marker is contained and its interval spans zero; shared interaction P=.15 agrees with the narrative.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S028

**Pass 1:** PASS_1_COMPLETE. High 25(OH)D subgroup forest is negative and spans zero, consistent with printed changes −12.3 versus −11.5. Interaction P=.15 remains a different null.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S029

**Pass 1:** PASS_1_COMPLETE. Both eGFR strata have positive markers contained in CIs spanning zero. Interaction P=.18 agrees with the hypothesis-generating narrative.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S030

**Pass 1:** PASS_1_COMPLETE. Both lower BMI strata have positive markers and CIs spanning zero. Global BMI interaction P=.79 supplies no significant heterogeneity.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S031

**Pass 1:** PASS_1_COMPLETE. BMI≥30 forest is positive and spans zero; P=.79 is global heterogeneity. Missing parenthesis after SD 15.0 changes no numeric reading and is excluded.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S032

**Pass 1:** PASS_1_COMPLETE. Both omega-assignment strata have positive markers and CIs spanning zero. P=.42 agrees with the primary treatment-interaction rule. Numeric lane covers crossed-cell count headers.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S033

**Pass 1:** PASS_1_COMPLETE. Figure 4 overall forest is positive and spans zero, matching the primary omega result. Count/header assignment is independently checked by the numeric lane.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S034

**Pass 1:** PASS_1_COMPLETE. Low EPA/DHA forest is positive and spans zero. P=.72 tests interaction across strata and is not an individual subgroup P value.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S035

**Pass 1:** PASS_1_COMPLETE. High EPA/DHA forest is positive and spans zero; shared P=.72 agrees with nonsignificant heterogeneity. Crude means/SDs do not recreate the adjusted interval.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S036

**Pass 1:** PASS_1_COMPLETE. ACR<30 omega subgroup forest is positive and spans zero. P=.70 is the shared ACR interaction test.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S037

**Pass 1:** PASS_1_COMPLETE. ACR≥30 omega subgroup forest is near zero and its CI spans zero. A negative crude mean difference need not equal the adjusted marker. P=.70 tests interaction.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S038

**Pass 1:** PASS_1_COMPLETE. Low hsCRP subgroup forest is positive and spans zero. P=.73 tests heterogeneity, with no significant subgroup-effect claim.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S039

**Pass 1:** PASS_1_COMPLETE. High hsCRP subgroup forest is positive and spans zero; direction agrees with the printed changes and interaction P=.73.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S040

**Pass 1:** PASS_1_COMPLETE. Lower fish-intake forest is positive and spans zero. Interaction P=.51 is nonsignificant; this exploratory subgroup addition is disclosed.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S041

**Pass 1:** PASS_1_COMPLETE. Higher fish-intake forest is positive and spans zero. Shared P=.51 agrees with the stated lack of heterogeneity.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S042

**Pass 1:** PASS_1_COMPLETE. Both vitamin D assignment strata have positive markers and CIs spanning zero. P=.42 agrees with the main interaction result; adjusted contrasts are not replaced by crude differences.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S043

**Pass 1:** PASS_1_COMPLETE. Vitamin D composite HR .92 (.68, 1.25), P=.61 has containment, ordered endpoints and consistent null inclusion. Rate estimates and differences lie within their CIs.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S044

**Pass 1:** PASS_1_COMPLETE. Vitamin D ≥40% decline HR .97 (.63, 1.51), P=.90 reconciles. Rate difference −.1 (−.7, .6) includes zero. Person-time denominators are absent.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S045

**Pass 1:** PASS_1_COMPLETE. Vitamin D ACR HR 1.34 (1.00, 1.80), P=.05 is at the printed boundary; neither interval excludes the null nor printed P is<.05. Endpoint prespecification is F-ST1-006.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S046

**Pass 1:** PASS_1_COMPLETE. Omega composite HR 1.11 (.81, 1.50), P=.52 reconciles. Rate difference .3 (−.5, 1.1) includes zero. Cox HR and rounded incidence rates are separate quantities.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S047

**Pass 1:** PASS_1_COMPLETE. Omega ≥40% decline HR .99 (.64, 1.54), P=.97 reconciles. Equal event counts do not require HR exactly one, because event timing and risk sets matter.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S048

**Pass 1:** PASS_1_COMPLETE. Omega ACR HR 1.08 (.81, 1.44), P=.60 and rate difference .3 (−.8, 1.4) reconcile. Standalone outcome status is F-ST1-006.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S049

**Pass 1:** PASS_1_COMPLETE. Tests explicitly use null HR=1. Baseline exclusions of four/one match measurable outcomes. Standalone time-to-ACR-doubling is called prespecified but absent from the amended endpoint list: F-ST1-006.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S050

**Pass 1:** PASS_1_COMPLETE. Discussion identifies favorable subgroup point estimates but null-crossing CIs and nonsignificant interaction, explicitly as hypothesis-generating. Primary five-year nonsignificance agrees.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S051

**Pass 1:** PASS_1_COMPLETE. Eligibility and analysis-population implications were inspected. Age and insulin-exclusion comparisons are assigned to the cross-source design lane; no unstated eligibility model is inferred.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S052

**Pass 1:** PASS_1_COMPLETE. Individual factorial randomization in blocks of eight matches the report. Age-only versus age/sex/race strata is assigned to the cross-source design lane; there is no cluster or paired-test mismatch.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S053

**Pass 1:** PASS_1_COMPLETE. D 2000 IU and EPA+DHA 840 mg within a 1000-mg capsule match total dose quantities. Component-ratio deviations are within precision. IU/µg pairing is assigned to the numeric lane.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S054

**Pass 1:** PASS_1_COMPLETE. Original ACR primary becomes secondary in the amended/report hierarchy: F-ST1-008. The amendment is documented. Current log-LMM ratio representation is coherent.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S055

**Pass 1:** PASS_1_COMPLETE. Original eGFR secondary becomes primary: F-ST1-008. The estimating-equation comparison is assigned to the cross-source lane. “Dichotomous” beside explicit continuous equations does not establish a binary model.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S056

**Pass 1:** PASS_1_COMPLETE. Original composite includes ACR progression and absolute ≥12 loss; amended/report composite removes ACR and uses relative ≥40% loss: F-ST1-009. The documented amendment remains an alternative.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S057

**Pass 1:** PASS_1_COMPLETE. Original additive/multiplicative interaction is superseded by the final LMM interaction specification. Original joint-treatment binary indicator is coherent and is not treated as an arithmetic sum.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S058

**Pass 1:** PASS_1_COMPLETE. Treatment interaction P=.42>.05 supports marginal contrasts under the amended conditional rule. No significant printed interaction requires the unreported combination comparisons.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S059

**Pass 1:** PASS_1_COMPLETE. Original ANCOVA exp(β)−1 and current LMM exp(β) are different representations; the amendment authorizes log-LMM. Wording alone does not establish a conflicting extracted effect measure.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S060

**Pass 1:** PASS_1_COMPLETE. Original ANCOVA/chi-square is explicitly replaced by final LMM/discrete Cox. Both are stated choices; no preferred model or unreported rank-sum substitution is assumed.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S061

**Pass 1:** PASS_1_COMPLETE. Original complete-case ITT is superseded by the amended plan. Current follow-up-conditioned versus all-randomized difference is F-ST1-001; imputation count is F-ST1-002. Nominal alpha/exploratory interpretation agree.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S062

**Pass 1:** PASS_1_COMPLETE. Original optional covariates are secondary; final model retains conditional sensitivity terms rather than fixed primary adjustment. This primary term-set comparison is F-ST1-003. Conditional mediation alone does not imply an omitted mandatory analysis.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S063

**Pass 1:** PASS_1_COMPLETE. Original subgroup definitions match reported total 25(OH)D, ACR, eGFR, race, omega index and CRP. Final bioavailable subgroup is absent: F-ST1-005. Individual intervals are not interaction tests.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S064

**Pass 1:** PASS_1_COMPLETE. Original adherence threshold ≥80% is reiterated in the final plan and differs from the report: F-ST1-004. Printed biomarker correlations alone do not identify a replacement regression method.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S065

**Pass 1:** PASS_1_COMPLETE. Original ANCOVA power diagnostics use only supplied SDs, baseline correlations and 1200 follow-up participants. Exact amended preliminary variance is not substituted from historical cohorts.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S066

**Pass 1:** PASS_1_COMPLETE. Every original power row reproduces within display precision. Attrition/adherence and combination comparisons reconcile. Original/final outcome hierarchy is F-ST1-008; old table wording does not create ambiguity in the current decision rule.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S067

**Pass 1:** PASS_1_COMPLETE. Joint incidence is not reconstructed by summing overlapping components. Diagnostic two-proportion tests support the stated original RR ranges. Graph-only power curves do not supply exact additional observations.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S068

**Pass 1:** PASS_1_COMPLETE. Parent DSMB z=3 gives two-sided normal P=.00270, matching .0027. This is a parent cancer/CVD rule, not an inferred ancillary interim rule; no reported kidney stopping decision conflicts.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S069

**Pass 1:** PASS_1_COMPLETE. Implemented 2016 amendment matches report disclosure. Hierarchy/composite revisions are F-ST1-008/009. Older two-/four-year history does not change the current five-year decision rule.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S070

**Pass 1:** PASS_1_COMPLETE. Amended eGFR primary and continuous ACR/≥40% loss/composite definitions match final report, with original revisions F-ST1-008/009. Standalone categorical ACR prespecification is F-ST1-006.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S071

**Pass 1:** PASS_1_COMPLETE. Amended follow-up-conditioned population and M=10 differ from reported all randomized and M=20: F-ST1-001/002. Chained-equation predictors are not fully detailed in the report but no predictor conflict is established.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S072

**Pass 1:** PASS_1_COMPLETE. Printed interaction model and P=.42 decision were inspected. Adding a time-main term would infer an unrestricted model not independently required by supplied text; the apparent omission is excluded without proposing a preferred model.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S073

**Pass 1:** PASS_1_COMPLETE. Final random intercept, categorical treatment/time interaction and year-5 inference match the report, except fixed primary covariates: F-ST1-003. No continuous numeric slope is assumed from categorical-time notation.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S074

**Pass 1:** PASS_1_COMPLETE. “Discrete Cox” versus “Cox” alone does not establish a changed tie/risk-set method. Conditional mediator exploration does not require output in the absence of its condition. Fixed primary adjustment is F-ST1-003.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S075

**Pass 1:** PASS_1_COMPLETE. Planned bioavailable 25(OH)D primary subgroup is not reported: F-ST1-005. Race-hypothesis wording changes in a supplied update while tests remain two-sided and reported groups remain matched.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S076

**Pass 1:** PASS_1_COMPLETE. Adherence threshold/continuity differs: F-ST1-004. Planned biomarker-replacement LMM versus printed r alone cannot establish replacement because no regression method/coefficient is named.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S077

**Pass 1:** PASS_1_COMPLETE. Final 2000-replication simulation, equal allocation, 1058 participants and 2.3/80% result agree with the report at precision. Preliminary variance/covariances are absent, preventing exact simulation reconstruction.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S078

**Pass 1:** PASS_1_COMPLETE. Post-shift standard calibration and pre-shift harmonization are sequential coherent operations. 5.96 versus 5.961 is display precision. Correlation .999 and identity plot agree; QC sample data are unavailable for exact SEs.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S079

**Pass 1:** PASS_1_COMPLETE. Response denominators and longitudinal adherence N=1032 are distinct. Two-thirds on two/three or four/six questionnaires is explicitly defined. Planned ≥80% comparison is F-ST1-004.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S080

**Pass 1:** PASS_1_COMPLETE. All 36 continuous-table time rows, arm mean/change intervals, 24 nonbaseline contrast intervals and 12 printed year-5 P values were checked. Containment/order/null decisions reconcile. eTable 7 population/exclusion inconsistency is assigned to the numeric lane.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S081

**Pass 1:** PASS_1_COMPLETE. All eight post hoc outcome rows, counts, rates/CIs, differences/CIs, HR/CIs and P values were checked. Every interval contains its estimate and all HR intervals include one with P>.05. Rate-SE diagnostics reproduce displayed precision.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

### S082

**Pass 1:** PASS_1_COMPLETE. Both biomarker panels and all 26 ACR forest rows were checked. All graphical intervals contain markers and span one; interaction P values are nonsignificant. Reversed favor-direction arrows are F-ST1-007. Count-column comparisons belong to the numeric lane.

**Pass 2:** PASS_2_COMPLETE. The complete independent pass-2 facts for this S ID, including grouped constituent rows, screening and mechanical-recheck implications, are recorded in [statistical_pass_2.md](../checkers/statistical_pass_2.md).

## Limits of exact reconstruction

Exact adjusted/MI coefficients cannot be regenerated without raw longitudinal data, covariance matrices, imputation details and pooling degrees of freedom. Cox HRs/P values cannot be regenerated without risk sets, event times and specified test type. Final simulation lacks preliminary variance/covariance inputs. Graphical forest estimates/endpoints are not numerically printed and remain visual containment/null/direction observations. These are reconstruction limits; no statistical relationship was omitted.

## New auxiliary derivatives

Direct Poppler pdftotext -layout 26.01.0, CPU: preprocessing/statistical_pass_1/plan17-23.txt (DOC-002 pp17–23); preprocessing/statistical_pass_1/plan31-33.txt (DOC-002 pp31–33); preprocessing/statistical_pass_1/supp2-4.txt (DOC-003 pp2–4). These exact supplied-PDF derivatives support locators; no OCR/rendering/conversion or fallback environment created. Existing canonical renderings used as visual evidence, without modification.

Exact producing commands, run from package root:

- pdftotext -layout -f 17 -l 23 joi190122supp1_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/statistical_pass_1/plan17-23.txt
- pdftotext -layout -f 31 -l 33 joi190122supp1_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/statistical_pass_1/plan31-33.txt
- pdftotext -layout -f 2 -l 4 joi190122supp2_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/statistical_pass_1/supp2-4.txt

## Literal route-A endpoint-revision registration

S003, S054, S055, S066, S069 and S070 additionally map to F-ST1-008 (outcome hierarchy revision). S056, S069 and S070 additionally map to F-ST1-009 (composite definition revision). Their contextual disclosure and source-supported amendment remain alternatives rather than exclusion grounds under routeA category5. Both latest-plan/report definitions reconcile, while original-plan/report and plan-version definitions differ. Every affected S record remains PASS_1_COMPLETE.

