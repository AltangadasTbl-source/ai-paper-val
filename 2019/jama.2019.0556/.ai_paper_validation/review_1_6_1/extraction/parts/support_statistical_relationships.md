# Support statistical relationship inventory

Every row is a source-grounded relationship for both statistical passes. Source locations are physical PDF pages. Main matching keys are descriptive, without a finding judgment. Exact cell transcriptions for multicolumn regressions follow the inventory.

| ID | Source locations and roles | Outcome / relationship / complete specification | Main matching key |
|---|---|---|---|
| S050 | DOC-002 PLAN pp.8,9,28,33,34 | Summary MDD12month cumulative incidence DSM-IV MINI baseline,3,6,12; methods p.28 DSM-5 MINI V5.01 same times; screening/schedule pp.33-34 DSM-IV MINI V5; IDS depressive severity baseline,3,6,12 listed main endpoint. | Primary endpoint; IDS hierarchy |
| S051 | DOC-002 PLAN pp.16-17 | Powered to detect difference25% in cumulative DSM-IV incidence across1year; expected30%control(placebo/noFBC),15%intervention; additive-interaction interest;180/group,2-sidedα.05,power.90;20%dropout,250/arm; synergistic pure-treatment comparison power80%; continuous IDS power larger. | Sample size/power |
| S052 | DOC-002 PLAN pp.15,29 | Individual2×2factorial central online blockrandomization stratified by center and historyMDD; pill allocation participant/researcher blinded; four arms250. | Randomization design |
| S053 | DOC-002 PLAN pp.39,43 | All four centers pooled; primary ITT; supplementary perprotocol; withdrawn intervention participants encouraged measurements. Baseline four-arm tests chi-square,t,AN(C)OVA. | Analysis populations |
| S054 | DOC-002 PLAN p.43 | Primary incidence time-to-event Kaplan-Meier/logrank/Cox;2-way/4-way separate+combined effects; adjust country and depression history. | Primary model; time-to-event |
| S055 | DOC-002 PLAN p.43 | Mixed regression baseline,3,6,12 tests main effects+interaction on onsetMDD and IDS severity; repeated measurements and country clustering. | Primary/IDS longitudinal analysis |
| S056 | DOC-002 PLAN p.43 | Secondary foodintake,BMI/weight,activity,sedentary,PHQ,anxiety,bodyimage,eating domains,qualitylife mixed models interventions+interaction; country clustering. | Secondary models/covariates |
| S057 | DOC-002 PLAN pp.43-44 | Four-step mediation regression/bootstrapping indirect effects; blood subgroup linearregression nutritional-status change vs onsetMDD/depressive-change adjusted intervention. | Additional analyses |
| S058 | DOC-002 PLAN p.44 | Effectmodifiers country,sex,education,income,baselineBMI,age; interaction in Cox for MDD and mixed regression depressive severity. | Prespecified subgroups |
| S059 | DOC-002 PLAN pp.14,28,29,35,36 | Depression/secondary outcomes24month longterm, questionnaire online; no evaluation questions; LIDAS episodes since12month. | Time windows |
| S060 | DOC-002 PLAN pp.40-42,49 | Safety suspension if disadvantages greater than foreseen; DSMB notapplicable; no numerical interim efficacy or multiplicity stopping rule specified in these pages. Endstudy lastpatient lastvisit. | Interim/stopping |
| S061 | DOC-003 PLAN p.2 | Primary cumulative MDD yes1 if positive T3,T6,orT12; no0 if negative allthree; MINI5.0plus MDD section. | Primary endpoint definition |
| S062 | DOC-003 PLAN p.2 | Secondary PHQ9 and IDS30 T3,T6,T12; otherGAD7,EQ5D5L. | Endpoint hierarchy |
| S063 | DOC-003 PLAN pp.2-3 | All analyses adjust historyMDD baseline yes/no and centerAMS/LEI/EXE/MAL; primary noother covariates bydefault; secondary may add. Secondary corresponding baseline depression score to increaseprecision. | Covariates |
| S064 | DOC-003 PLAN p.3 | Primary logistic regression interventions effectcoded,main+interaction,OR95%CI/P; secondary mixedmodels orGEE B95%CI/P; T12continuous standardized mean differences95%CI/P. | Planned primary/secondary measures |
| S065 | DOC-003 PLAN p.3 | SAS/R,alltests2-sided significance .05 (printed p0.05). No explicit multiplicity adjustment stated. | Testing threshold |
| S066 | DOC-003 PLAN p.4 | PrimaryITT; secondaryCACE preserving randomization. Goodcompliance≥70%supplements12months weightedjars else mean selfreportT3/T6/T9/T12; FBA≥8/21sessions12months. | CACE population/compliance |
| S067 | DOC-003 PLAN p.4 | MDD logistic multiplicative A×B interaction; sensitivity biological additive relative-risk interactionRERI; RERI>0;linear oddsratio model likelihood95%CI;joint lowest-assumed-risk stratum reference. | Interaction specification |
| S068 | DOC-003 PLAN p.4 | Secondary time-to-onsetMDD Cox HR95%CI/P. | Cox priority |
| S069 | DOC-003 PLAN pp.4-5 | ModifierhistoryMDD/center; others separatepaper; logisticA×MDDhistory/B×MDDhistory plusA,B,history,center; interactionP<.05;stratifiedtable or narrative. | Prespecified modifiers |
| S070 | DOC-003 PLAN p.5 | Missingness frequency/nature; FIML orMI appropriate;100MI primaryoutcome datasets underMAR; Rubin pooling;sensitivity assumptions. | Missing data |
| S071 | DOC-003 PLAN p.5 | Outliers inspect/correct if possible; sensitivitywith/without otheroutliers;logtransform for nonnormal assumptionviolations. | Distribution sensitivity |
| S072 | DOC-004 REPORT pp.14-15 | CACE randomization instrument inSEM; latentcompliers/nevercompliers,similarproportion byallocation,exclusionrestriction; estimate ratiooriginalinterventioneffect/proportioncompliers; fullsample. | CACE method |
| S073 | DOC-004 REPORT p.18 tableA | PHQ12month moderation FBA×baselinePHQ−.064(−.118,−.01),P.020;supplement×baselinePHQ.032(−.023,.086),P.259; full modelcells below. Narrative higherbaselinePHQ favorsFBA. | PHQ baseline moderation |
| S074 | DOC-004 REPORT p.19 tableB | Anxiety overall moderation supplement×baselineGAD.062(.009,.115),P.022;FBA×baselineGAD−.016(−.068,.036),P.554; full modelcells below. NarrativehigherbaselineGAD supplementhigherfollowupanxiety. | GAD moderation |
| S075 | DOC-004 REPORT p.20 tableC1 | Utility12month FBA×UK.017(.001,.033),P.041,NLreference;Spain.016(−.001,.032)P.066;Germany.006(−.01,.022)P.452; all supplement/siteinteractioncells below. | Site moderation |
| S076 | DOC-004 REPORT p.20 UKsubgroup | Utility12monthUK FBA.013(.001,.024),P.033; completeadjustmentcells below. | UK utility subgroup |
| S077 | DOC-004 REPORT p.20 NLsubgroup | Utility12monthNL FBA−.007(−.019,.005),P.267; completeadjustmentcells below. | NL utility subgroup |
| S078 | DOC-004 REPORT p.21 | NoMI PHQ supplement overallB.30(.11,.49)P.002;T12B.28(SE.11)P.013. | Complete-case PHQ supplement |
| S079 | DOC-004 REPORT p.21 | NoMI PHQ FBA overall−.14(−.34,.05)P.14;T12−.22(SE.11)P.052. | Complete-case PHQ FBA |
| S080 | DOC-004 REPORT p.21 | NoMI PHQ interaction overall−.01(−.20,.18)P.94;T12.02(SE.11)P.84. | Complete-case PHQ interaction |
| S081 | DOC-004 REPORT p.21 | NoMI IDS supplement overall.55(.11,.99)P.01;T12.28(SE.28)P.30. | Complete-case IDS supplement |
| S082 | DOC-004 REPORT p.21 | NoMI IDS FBA overall−.26(−.70,.18)P.25;T12−.36(SE.28)P.20. | Complete-case IDS FBA |
| S083 | DOC-004 REPORT p.21 | NoMI IDS interaction overall−.01(−.45,.43)P.96;T12.12(SE.28)P.66. | Complete-case IDS interaction |
| S084 | DOC-004 REPORT p.21 | NoMI GAD supplement overall.24(.08,.40)P.004;T12.17(SE.09)P.07. | Complete-case GAD supplement |
| S085 | DOC-004 REPORT p.21 | NoMI GAD FBA overall−.16(−.32,.00)P.06;T12−.26(SE.09)P.005. | Complete-case GAD FBA |
| S086 | DOC-004 REPORT p.21 | NoMI GAD interaction overall.04(−.13,.20)P.66;T12.03(SE.09)P.74. | Complete-case GAD interaction |
| S087 | DOC-004 REPORT p.21 | NoMI utilitysupplement overall−.006(−.011,.000)P.055;T12−.001(SE.003)P.66. | Complete-case utility supplement |
| S088 | DOC-004 REPORT p.21 | NoMI utilityFBA overall.002(−.004,.007)P.51;T12.004(SE.003)P.23. | Complete-case utility FBA |
| S089 | DOC-004 REPORT p.21 | NoMI utilityinteraction overall−.002(−.008,.003)P.42;T12.001(SE.003)P.65. All S078-S089:bothinterventions+interaction together,site/historyMDD/correspondingbaselineoutcome, effectcoding−1,+1;overallGEE, T12robustlinearregression;Bunstandardized. | Complete-case models |
| S090 | DOC-004 REPORT p.22 | MI CACE MDDonset: FBAOR.78(.64,.95)*;supplementOR.84(.67,1.07). LogisticMDD atanyfollowup,site/historyMDDadjusted;effectcoding−1,+1. | CACE primaryMDD |
| S091 | DOC-004 REPORT p.22 | MI CACE PHQ:T12FBA B−.22(−.59,.15);supplement.43(.08,.77)*;ANCOVAcorrespondingbaseline/site/historyadjusted. | CACE PHQ |
| S092 | DOC-004 REPORT p.22 | MI CACE IDS:T12FBA−.42(−1.24,.40);supplement.47(−.33,1.27);sameANCOVA. | CACE IDS |
| S093 | DOC-004 REPORT p.22 | MI CACE GAD:T12FBA−.31(−.60,−.02)*;supplement.18(−.11,.47);sameANCOVA. FootnotesFBA8/21,omega≥70%,*P<.05/**P<.01. | CACE GAD |
| S094 | DOC-004 REPORT p.23 | Blinding four-arm threecategory distribution n759,P<.001; exactcellcountsN121. Testtype notnamed onpage. | Concealment test |

## All moderation model cells

Each numeric tuple is B; lower95%CI; upper95%CI; P. Ref and blank CI/P cells are preserved. These adjustment coefficients belong to the S073-S077 model relationships, rather than new independent results.

### S073 — DOC-004 physical p.18, table A

| Covariate | B | Lower | Upper | P |
|---|---:|---:|---:|---:|
| Supplements | 0.046 | -0.399 | 0.490 | 0.841 |
| F-BA | 0.288 | -0.155 | 0.731 | 0.203 |
| Netherlands | ref | | | |
| Spain | -0.480 | -1.161 | 0.202 | 0.168 |
| United Kingdom | 0.275 | -0.373 | 0.923 | 0.405 |
| Germany | 0.233 | -0.396 | 0.862 | 0.468 |
| History of depression | -0.536 | -1.036 | -0.036 | 0.036 |
| Baseline PHQ-9 | 0.322 | 0.265 | 0.379 | <0.001 |
| F-BA: baseline PHQ-9 | -0.064 | -0.118 | -0.01 | 0.020 |
| Supplements: baseline PHQ-9 | 0.032 | -0.023 | 0.086 | 0.259 |

### S074 — DOC-004 physical p.19, table B

| Covariate | B | Lower | Upper | P |
|---|---:|---:|---:|---:|
| Supplements | -0.107 | -0.384 | 0.17 | 0.45 |
| F-BA | -0.054 | -0.329 | 0.221 | 0.703 |
| Netherlands | ref | | | |
| Spain | 0.107 | -0.424 | 0.520 | 0.694 |
| United Kingdom | 0.117 | -0.371 | 0.638 | 0.637 |
| Germany | 0.058 | -0.401 | 0.606 | 0.804 |
| History of depression | -0.317 | -0.698 | 0.063 | 0.102 |
| Baseline GAD-7 | 0.464 | 0.409 | 0.52 | 0 |
| F-BA × baseline GAD-7 | -0.016 | -0.068 | 0.036 | 0.554 |
| Supplements × baseline GAD-7 | 0.062 | 0.009 | 0.115 | 0.022 |

### S075 — DOC-004 physical p.20, table C1

| Covariate | B | Lower | Upper | P |
|---|---:|---:|---:|---:|
| Supplements | 0.000 | -0.012 | 0.012 | 0.952 |
| F-BA | -0.006 | -0.018 | 0.006 | 0.313 |
| Netherlands | ref | | | |
| Spain | 0.005 | -0.012 | 0.022 | 0.548 |
| United Kingdom | -0.014 | -0.031 | 0.003 | 0.097 |
| Germany | 0.011 | -0.006 | 0.027 | 0.198 |
| History of depression | 0.009 | -0.003 | 0.022 | 0.148 |
| Baseline health utility | 0.498 | 0.438 | 0.558 | <0.001 |
| F-BA × Netherlands | ref | | | |
| F-BA × Spain | 0.016 | -0.001 | 0.032 | 0.066 |
| F-BA × United Kingdom | 0.017 | 0.001 | 0.033 | 0.041 |
| F-BA × Germany | 0.006 | -0.01 | 0.022 | 0.452 |
| Supplements: Netherlands | ref | | | |
| Supplements × Spain | -0.006 | -0.023 | 0.011 | 0.499 |
| Supplements × United Kingdom | -0.001 | -0.018 | 0.016 | 0.907 |
| Supplements × Germany | 0.002 | -0.014 | 0.017 | 0.850 |

### S076 and S077 — DOC-004 physical p.20, two printed C2 subgroup tables

| Subgroup / covariate | B | Lower | Upper | P |
|---|---:|---:|---:|---:|
| UK Supplements | 0.000 | -0.012 | 0.011 | 0.944 |
| UK F-BA | 0.013 | 0.001 | 0.024 | 0.033 |
| UK History of depression | 0.007 | -0.016 | 0.03 | 0.559 |
| UK Baseline health utility | 0.738 | 0.62 | 0.856 | <0.001 |
| Netherlands Supplements | 0.000 | -0.012 | 0.012 | 0.935 |
| Netherlands F-BA | -0.007 | -0.019 | 0.005 | 0.267 |
| Netherlands History of depression | -0.005 | -0.031 | 0.021 | 0.697 |
| Netherlands Baseline health utility | 0.509 | 0.400 | 0.619 | <0.001 |

Narrative DOC-004 p.18 says no reported primary/secondary intervention effects moderated by historyMDD. No unprinted history interaction values are inferred. Report tables A/B/C do not independently name confidence-interval computation or covariance method; p.21 and22 model footnotes are scoped to their own tables. Displayed zeroP in tableB is preserved literally as display precision.
