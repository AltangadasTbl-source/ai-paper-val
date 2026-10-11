# Complete inferential relationship inventory

Pass 1 owner/runtime: /root/statistics_pass_1; fresh gpt-6.1-sol/high. Scope is the entire inferential union of DOC-001 REPORT pp1–12, DOC-002 REPORT pp1–20 and DOC-003 PLAN pp1–7. Read QUALITY_CONTROL_SCOPE.md and review_contract.md completely and both fresh mapper maps. Stable records group the same outcome or variable across repeated times, locations or sensitivity datasets; every tuple is retained below, with no sampling. There are 100 S records. Pass 2 must update each record independently.

Direct confirmation: Poppler pdftotext 26.01.0, CPU, full layout extraction to preprocessing/stat1-main-layout.txt, preprocessing/stat1-supp-layout.txt and preprocessing/stat1-plan-layout.txt. Direct command pattern: pdftotext -layout SOURCE.pdf DESTINATION.txt. Exact source-page renders visually confirmed main Table2 and supplement pp8,12,18,20. Rendered images are reusable locators; supplied PDF links are authoritative. No new OCR, no fallback, no source edits, no external literature and no previous review conclusions.

Common checks performed on every tuple: interval endpoints ordered, estimate contained, contrast/null/scale identified, direction against graphic/narrative, confidence level and significance level matched, same-result copies matched, and applicable counts/method/plan dependencies checked. No numerical SE, covariance, model test statistic, pooling degrees of freedom or raw-data vectors are supplied. Numeric Wald reconstructions, where mentioned, are diagnostics only; unspecified test conventions were not promoted to a method. PH P tests and subgroup interaction P tests are explicitly distinct from treatment-effect P tests.

## Main outcomes: S001–S008

[REPORT main Table2 p7](../../../jama_aminian_2019_oi_190103.pdf#page=7); [methods p4](../../../jama_aminian_2019_oi_190103.pdf#page=4); [six individual outcome plots p8](../../../jama_aminian_2019_oi_190103.pdf#page=8). All intervals 95%; KM incidence at8y surgery/control; ARD control minus surgery; fully adjusted Cox HR surgery/control with two-sided alpha .05. All Table1 covariates, MICE5 and Rubin pooling. Each row retains two incidence tuples, ARD tuple and HR/P tuple. Figures2–3 copy HR/P tuples exactly; abstract copies primary and death exactly; narrative direction lower surgery agrees. Printed counts are events over varying follow-up, not crude8y risk numerators.

| S ID | Outcome; risk set surgery/control | Surgery8y%(CI); control8y%(CI) | ARD%(CI); HR(CI); P | Pass1 result | Pass1 status | Pass2 status |
|---|---|---|---|---|---|---|
| S001 | Primary;2287/11435 | 30.8(27.6,34.0);47.7(46.1,49.2) | 16.9(13.1,20.4);.61(.55,.69);<.001 | All four contain/order/direction checks reconcile; ARD47.7−30.8=16.9; Figure2A/abstract/KeyPoints match; event counts385/3243 are separate follow-up counts | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S002 | Secondary;2287/11435 | 17.0(14.3,19.7);27.6(26.2,29.0) | 10.6(7.5,13.6);.62(.53,.72);<.001 | Four tuple checks reconcile; ARD27.6−17.0=10.6; Figure2B/narrative match; event counts194/1765 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S003 | Death;2287/11435 | 10.0(7.8,12.2);17.8(16.6,19.0) | 7.8(5.1,10.2);.59(.48,.72);<.001 | Four tuple checks reconcile; ARD17.8−10.0=7.8; Figure3A/abstract match; event counts112/1111 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S004 | Heart failure;2049/10093 | 6.8(4.9,8.6);18.9(17.6,20.2) | 12.9(10.4,15.1);.38(.30,.49);<.001 | All estimates contained; HR/P direction agrees; ARD arithmetic F-ST1-001 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S005 | Coronary artery disease;2050/10331 | 7.9(5.9,9.8);11.6(10.5,12.6) | 4.2(1.9,6.8);.69(.54,.87);.002 | All estimates contained; HR/P agree; ARD arithmetic F-ST1-001 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S006 | Cerebrovascular disease;2245/11077 | 4.1(2.7,5.5);5.6(4.9,6.3) | 1.8(−.03,3.4);.67(.48,.94);.02 | HR/P agree; ARD arithmetic F-ST1-001; ARD interval includes0 vs significant displayedP F-ST1-002, different-estimand alternative retained | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S007 | Nephropathy;1937/9190 | 6.1(4.4,7.8);16.3(15.0,17.6) | 11.1(8.8,13.6);.40(.31,.52);<.001 | All estimates contained; HR/P agree; ARD arithmetic F-ST1-001; additional renal exclusions recognized | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S008 | Atrial fibrillation;2135/10734 | 7.9(6.1,9.7);13.6(12.5,14.7) | 6.5(4.4,8.7);.78(.62,.97);.03 | All estimates contained; HR/P agree; ARD arithmetic F-ST1-001; PH rejection handled separately at S040 | PASS_1_COMPLETE | PASS_2_COMPLETE |

## Cause-specific rates: S009–S016

[REPORT eTable4 p6](../../../joi190103supp1_prod.pdf#page=6). Rate per100 patient-years; control−surgery difference with bootstrap95%CI1000 samples. Parentheses are mortality-plus-outcome composite rates. Each printed estimate is within its correctly ordered interval; all differences exclude0, direction higher controls. No paired P or exact person-time denominator is printed. No crude ratio substituted for Cox HR.

| S ID | Outcome | Surgery rate; control rate | Difference(CI) | Pass1 result | Pass1 status | Pass2 status |
|---|---|---|---|---|---|---|
| S009 | Primary | 4.51;7.45 | 2.94(2.42,3.48) | Subtraction agrees; methods defined | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S010 | Secondary | 2.11;3.64 | 1.53(1.18,1.87) | Subtraction agrees | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S011 | Death | 1.19;2.22 | 1.03(.76,1.29) | Subtraction agrees | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S012 | HF | .92(1.84);2.49(3.7) | 1.57(1.32,1.82) | Subtraction agrees; parentheses include death, not CI | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S013 | CAD | 1.03(1.98);1.55(3.36) | .52(.29,.77) | Subtraction agrees | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S014 | Cerebrovascular | .45(1.55);.73(2.74) | .28(.12,.43) | Subtraction agrees; rateCI excludes0, different estimand from S006 ARD | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S015 | Nephropathy | .89(1.77);2.07(3.47) | 1.18(.93,1.42) | Subtraction agrees | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S016 | AF | 1.14(2.16);1.77(3.42) | .63(.36,.88) | Subtraction agrees | PASS_1_COMPLETE | PASS_2_COMPLETE |

## Group-specific cumulative incidence: S017–S024

[REPORT eTable5 p7](../../../joi190103supp1_prod.pdf#page=7). Percent risk,95%CIs; times2/5/8y; each cell lists surgery then control. All48 tuples inspected individually for containment/order/[0,100] domain and increasing cumulative incidence. All8y copies match main Table2. No treatment P is supplied for these group-specific intervals; overlap of marginal intervals is not a treatment test.

| S ID | Outcome | Year2 surgery;control | Year5 surgery;control | Year8 surgery;control | Pass1 result | Pass1 status | Pass2 status |
|---|---|---|---|---|---|---|---|
| S017 | Primary | 7.6(6.4,8.8);12.2(11.5,12.8) | 17.7(15.6,19.7);30.4(29.4,31.5) | 30.8(27.6,34);47.7(46.1,49.2) | All6 tuples reconcile; controls higher | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S018 | Secondary | 3.3(2.5,4.1);5.5(5.1,6.0) | 8.8(7.2,10.4);15.5(14.7,16.4) | 17(14.3,19.7);27.6(26.2,29.0) | All6 reconcile | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S019 | Death | 1.8(1.2,2.4);3.2(2.8,3.5) | 4.9(3.7,6.1);10.1(9.4,10.8) | 10(7.8,12.2);17.8(16.6,19.0) | All6 reconcile | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S020 | HF | 1.5(1.0,2.1);4.2(3.8,4.6) | 3.8(2.6,4.9);10.4(9.7,11.2) | 6.8(4.9,8.6);18.9(17.6,20.2) | All6 reconcile | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S021 | CAD | 1.7(1.1,2.3);2.9(2.6,3.3) | 4.2(3.1,5.3);6.8(6.2,7.4) | 7.9(5.9,9.8);11.6(10.5,12.6) | All6 reconcile | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S022 | Cerebrovascular | .7(.3,1.1);1.3(1.1,1.5) | 2.2(1.4,3.0);3.1(2.7,3.5) | 4.1(2.7,5.5);5.6(4.9,6.3) | All6 reconcile | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S023 | Nephropathy | 1.4(.8,2.0);2.3(2.0,2.7) | 3.9(2.8,5.1);8.8(8.0,9.5) | 6.1(4.4,7.8);16.3(15.0,17.6) | All6 reconcile | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S024 | AF | 2.3(1.6,3.1);2.7(2.4,3.0) | 4.8(3.6,6.0);7.6(7.0,8.2) | 7.9(6.1,9.7);13.6(12.5,14.7) | All6 reconcile | PASS_1_COMPLETE | PASS_2_COMPLETE |

## Primary subgroup associations: S025–S032

[REPORT eFigure1 p8](../../../joi190103supp1_prod.pdf#page=8), matched main narrative p4. Adjusted Cox surgery/usual care, original covariate replaced by dichotomy plus treatment interaction. All16 printed subgroup95%CI tuples checked against plot positions, containment and risk-direction legend; all exclude1. All8 interaction P values exceed.05 and match no-heterogeneity narrative. Interaction P does not test each subgroup HR; covariance/interaction SE not supplied, so an independent-groups approximation is not a reproducing test.

| S ID | Variable | First level HR(CI) | Second level HR(CI) | InteractionP | Pass1 result | Pass1 status | Pass2 status |
|---|---|---|---|---|---|---|---|
| S025 | Sex | Male .58(.49,.69) | Female .64(.56,.74) | .35 | Both tuples and interaction conclusion agree | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S026 | Age | <54 .57(.47,.68) | ≥54 .57(.50,.66) | .93 | Both agree; printed point equality not inferred exact equality | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S027 | BMI | <40 .62(.49,.78) | ≥40 .61(.54,.69) | .90 | Both agree | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S028 | HbA1c | <7 .62(.52,.74) | ≥7 .60(.52,.70) | .80 | Both agree | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S029 | eGFR | <91 .61(.54,.70) | ≥91 .62(.51,.75) | .94 | Both agree | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S030 | Insulin | No .63(.55,.73) | Yes .59(.50,.70) | .53 | Both agree | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S031 | Sulfonylurea | No .63(.55,.72) | Yes .60(.49,.74) | .72 | Both agree | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S032 | Lipid lowering | No .61(.52,.73) | Yes .62(.53,.71) | .98 | Both agree | PASS_1_COMPLETE | PASS_2_COMPLETE |

## Cox treatment tests and proportional-hazards tests: S033–S040

[REPORT eTable6 p9](../../../joi190103supp1_prod.pdf#page=9). Treatment HR/CI/P copies S001–S008 exactly. PH P is weighted-residual treatment PH test, not a null-HR test. Each HR interval excludes1 and its treatment P<.05. Printed PH values match the main p6 statement that AF is the exception. No supplied exact test statistic/SE/df permits reproducing every Cox treatment P from rounded intervals, so no exact numerical test claimed. Log-scale diagnostics show no independent contradiction.

| S ID | Outcome | HR95%CI; treatmentP | PH P | Pass1 result | Pass1 status | Pass2 status |
|---|---|---|---|---|---|---|
| S033 | Primary | .61(.55,.69);<.001 | .89 | Treatment and PH implications agree | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S034 | Secondary | .62(.53,.72);<.001 | .76 | Agree | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S035 | Death | .59(.48,.72);<.001 | .63 | Agree | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S036 | HF | .38(.30,.49);<.001 | .65 | Agree | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S037 | CAD | .69(.54,.87);.002 | .24 | Agree | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S038 | Cerebrovascular | .67(.48,.94);.02 | .10 | Agree; separate ARD conflict tracked S006 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S039 | Nephropathy | .40(.31,.52);<.001 | .46 | Agree | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S040 | AF | .78(.62,.97);.03 | .04 | PH rejected at.05, explicitly disclosed; time-varying sensitivity reported; no internally contradicted PH assertion | PASS_1_COMPLETE | PASS_2_COMPLETE |

## Time-varying treatment associations: S041–S048

[REPORT eTable7 p10](../../../joi190103supp1_prod.pdf#page=10), exact repeated table and method [p19](../../../joi190103supp1_prod.pdf#page=19); PLAN p6 anticipates times2/5/8y. Restricted cubic spline of observed follow-up interacted with treatment in adjusted Cox. All24 HR/95%CI tuples and their repeated copies checked. No accompanying treatment P printed. Every estimate contained/order positive; null status listed. Time-varying and constant-HR analyses are separately identified, not assumed identical.

| S ID | Outcome | Year2 HR(CI) | Year5 HR(CI) | Year8 HR(CI) | Pass1 result | Pass1 status | Pass2 status |
|---|---|---|---|---|---|---|---|
| S041 | Primary | .57(.49,.65) | .78(.66,.93) | .79(.64,.97) | All3 exclude1 below; repeated copies exact | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S042 | Secondary | .51(.42,.63) | .82(.65,1.04) | .73(.56,.95) | Year5 includes1; others below; all3 reconcile | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S043 | Death | .43(.33,.57) | .69(.50,.95) | .80(.56,1.15) | Year8 includes1; others below | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S044 | HF | .31(.23,.41) | .40(.31,.53) | .52(.35,.79) | All3 below1 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S045 | CAD | .52(.38,.69) | 1.03(.71,1.51) | .99(.64,1.51) | Years5/8 include1; printed direction above1 at5y retained | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S046 | Cerebrovascular | .68(.45,1.04) | 1.29(.77,2.15) | .60(.28,1.25) | All3 include1; year5point above1 retained | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S047 | Nephropathy | .41(.30,.58) | .40(.26,.61) | .46(.30,.70) | All3 below1 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S048 | AF | .68(.52,.89) | .88(.62,1.25) | .65(.42,1.00) | Year2 below1;5 includes1;8 endpoint1.00; no source P or significance claim conflict | PASS_1_COMPLETE | PASS_2_COMPLETE |

## Longitudinal metabolic, nutritional and medication comparisons: S049–S061

[REPORT eTable8 p12](../../../joi190103supp1_prod.pdf#page=12); exact source image checked. Every52 estimate/98.8%CI/P tuple inspected, not selected. Time columns1/2/5/8y. Continuous spline×treatment comparisons; medication two-sample proportions tests. Null difference0; negative contrasts mean lower surgery vs nonsurgery.98.8% Bonferroni intervals correspond to alpha.012 (98.75% rounds98.8%, alpha.0125); comparisons of rawP to.05 are not forced to match these adjusted intervals. Stars appear on P<.001,.008,.007, and not.02,.19,.27; legend not supplied, pattern agrees with.0125. No estimate outside interval or reversed endpoint. No inferential significance conclusion is inferred from group-curve CI overlap.

| S ID | Variable/unit | Year1 estimate(CI);P | Year2 estimate(CI);P | Year5 estimate(CI);P | Year8 estimate(CI);P | Pass1 result | Pass1 status | Pass2 status |
|---|---|---|---|---|---|---|---|---|
| S049 | Weight lb | −56.6(−57.1,−56.1);<.001 | −73.7(−74.4,−73.0);<.001 | −45.2(−45.9,−44.6);<.001 | −44.8(−45.5,−44.1);<.001 | All4 significant and negative; kg conversion agrees within display precision | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S050 | Weight kg | −25.7(−25.9,−25.4);<.001 | −33.4(−33.7,−33.1);<.001 | −20.5(−20.8,−20.2);<.001 | −20.3(−20.6,−20.0);<.001 | All4 agree; mainp7 group reductions29.1(95%CI28.8,29.3)/8.7(8.6,8.9),difference20.3(20.1,20.6) all contained/ordered;95% differs from supplement98.8%; point rounding reconciles29.1−8.7 vs20.3 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S051 | HbA1c percentage points | −1.5(−1.6,−1.4);<.001 | −1.6(−1.7,−1.5);<.001 | −1.0(−1.1,−.9);<.001 | −1.1(−1.2,−1.0);<.001 | All4 agree; mainFigure4 difference magnitude1.1/P<.001 and curve directions match | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S052 | Protein g/dL | −.5(−.6,−.5);<.001 | −.5(−.5,−.5);<.001 | −.3(−.3,−.3);<.001 | −.3(−.3,−.3);<.001 | All4 below0; equal printed endpoints compatible with narrow rounded intervals; no supplied contradiction | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S053 | Albumin g/dL | −.3(−.3,−.3);<.001 | −.2(−.2,−.1);<.001 | −.1(−.1,−.1);<.001 | −.2(−.2,−.1);<.001 | All4 below0; mean changes differ from group-specific level curves, not equated | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S054 | Hemoglobin g/dL | −.6(−.6,−.5);<.001 | −.4(−.4,−.3);<.001 | −.1(−.2,0);<.001 | −.2(−.2,−.1);<.001 | Years1/2/8 agree; year5 printedCI includes0 whileP<.001 F-ST1-003; not screened as rounding | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S055 | VitaminD25 ug/L | 6.4(5.0,7.7);<.001 | 4.1(2.6,5.7);<.001 | −.9(−2.7,.9);.19 | −1.4(−4.4,1.7);.27 | Positive significant1/2; includes0 and nonsignificant5/8; all4 agree with98.8% rule | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S056 | Noninsulin medication percentage points | −50(−52.9,−47.1);<.001 | −51.5(−54.6,−48.3);<.001 | −47.4(−51.9,−42.9);<.001 | −37.9(−45.3,−30.6);<.001 | All4 agree; mainFigure5A8yP identical, surgery curve lower | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S057 | Insulin percentage points | −8.3(−11.1,−5.4);<.001 | −9.1(−12.3,−5.9);<.001 | −9.1(−13.7,−4.6);<.001 | −8.1(−15.5,−.7);.008 | All4 agree at98.8%; mainFigure5B8yP=.008 identical | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S058 | Renin–angiotensin inhibitor percentage points | −25(−28.1,−21.9);<.001 | −26.6(−30.1,−23.1);<.001 | −27.5(−32.3,−22.7);<.001 | −26.4(−34,−18.8);<.001 | All4 agree; mainFigure5C matches | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S059 | Other antihypertensive percentage points | −2.7(−5.6,.3);.02 | −3.4(−6.7,−.2);.007 | −7.7(−12.1,−3.2);<.001 | −10.6(−17.6,−3.7);<.001 | Year1 includes0 and.02>.012/.0125; year2 excludes0 and.007<.012; all4 reconcile; mainFigure5D8y matches | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S060 | Lipid-lowering percentage points | −16.7(−19.8,−13.5);<.001 | −21.1(−24.5,−17.6);<.001 | −26.4(−31.1,−21.7);<.001 | −28.3(−35.8,−20.8);<.001 | All4 agree; mainFigure5E matches | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S061 | Aspirin percentage points | −24.5(−27.1,−21.9);<.001 | −24.4(−27.4,−21.4);<.001 | −25.9(−30.2,−21.6);<.001 | −27(−34,−20);<.001 | All4 agree; mainFigure5F matches | PASS_1_COMPLETE | PASS_2_COMPLETE |

## Postoperative intervention risks: S062–S067

[REPORT eTable11 p15](../../../joi190103supp1_prod.pdf#page=15). Surgery-only KM cumulative incidence%,95%CI at1/2/5/8y; not crude proportions. All24 tuples inspected: point contained, endpoints ordered, percentages admissible, risk monotonically increasing. No P or treatment comparison supplied. Abdominal surgery excludes hernia repair/cholecystectomy; overlapping separate interventions are not summed. Early90d main percentages not matched as same-time copies.

| S ID | Intervention | Year1 | Year2 | Year5 | Year8 | Pass1 result | Pass1 status | Pass2 status |
|---|---|---|---|---|---|---|---|---|
| S062 | Parenteral nutrition | 1.5(1,2.1) | 1.8(1.2,2.4) | 2.1(1.5,2.8) | 2.9(1.9,3.9) | All4 reconcile | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S063 | Endoscopy | 23.9(22.1,25.7) | 30.1(28,32.1) | 44.2(41.6,46.8) | 52(48.7,55) | All4 reconcile | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S064 | Interventional radiology | 2.6(1.9,3.2) | 3.3(2.5,4.1) | 6.8(5.4,8.1) | 10.4(8.3,12.4) | All4 reconcile | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S065 | Abdominal surgery | 5.9(4.9,6.9) | 8.1(6.9,9.3) | 12.1(10.4,13.7) | 13.8(11.8,15.7) | All4 reconcile | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S066 | Hernia repair | 2.8(2.1,3.6) | 5.7(4.6,6.8) | 8.7(7.3,10.2) | 11.1(9.1,13) | All4 reconcile | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S067 | Cholecystectomy | 1.4(.9,1.9) | 3.5(2.6,4.3) | 6.5(5.2,7.8) | 9.7(7.7,11.7) | All4 reconcile | PASS_1_COMPLETE | PASS_2_COMPLETE |

## All120 graphical sensitivity comparisons: S068–S075

[REPORT eFigure4 p18](../../../joi190103supp1_prod.pdf#page=18) visually read in full, [p17 narrative](../../../joi190103supp1_prod.pdf#page=17). Adjusted Cox HR/95%CI, surgery/nonsurgery. Each row below explicitly retains all15 comparisons by iteration1,2,3,4,5 with each of three series: 1:1 circle,5:1 triangle,10:1 square (literal figure labels). Each point and both interval endpoints were inspected. All120 points lie below1 and inside their intervals; no endpoints reversed. Exact numbers are not printed and are not digitized; null-touch readings remain at graphical resolution. Code B=interval wholly below1; N=interval reaches/crosses1. These are graphical observations, not exact tests. No plotted numericalP supplied.

| S ID | Outcome | 1:1 iterations1,2,3,4,5 | 5:1 iterations1,2,3,4,5 | 10:1 iterations1,2,3,4,5 | Narrative significant datasets; pass1 result | Pass1 status | Pass2 status |
|---|---|---|---|---|---|---|---|
| S068 | Primary | B,B,B,B,B | B,B,B,B,B | B,B,B,B,B | 15; all15 inspected, agrees | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S069 | Secondary | B,B,B,B,B | B,B,B,B,B | B,B,B,B,B | 15; all15 inspected, agrees | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S070 | Death | B,B,B,B,B | B,B,B,B,B | B,B,B,B,B | 15; all15 inspected, agrees | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S071 | CAD | B,N,N,N,B | B,B,B,B,B | B,B,B,B,B | 12; all15 inspected, agrees | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S072 | Cerebrovascular | B,N,B,N,B | B,B,B,B,B | B,B,B,B,B | 13; all15 inspected, agrees | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S073 | HF | B,B,B,B,B | B,B,B,B,B | B,B,B,B,B | 15; all15 inspected, agrees | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S074 | Nephropathy | B,B,B,B,B | B,B,B,B,B | B,B,B,B,B | 15; all15 inspected, agrees | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S075 | AF | N,N,B,B,N | B,B,B,B,B | B,B,B,B,N | 11; all15 inspected, agrees | PASS_1_COMPLETE | PASS_2_COMPLETE |

## E-values and all40 known-factor associations: S076–S083

[REPORT eTable12 p20](../../../joi190103supp1_prod.pdf#page=20), [interpretation/method p19](../../../joi190103supp1_prod.pdf#page=19), HR source eTable6 p9. E-values on risk-ratio scale; HR-to-RR formula not printed. Empirical reproducing method within this display: E(h)=1/h+sqrt((1/h)(1/h−1)) for h<1; this is a diagnostic algebraic comparator supported by all7 nonprimary rows at both point and upper-limit inputs under half-unit rounding. It is not claimed to be the authors' universal intended transformation. Every40 factor HR/95%CI checked for point containment, endpoint order, contrast/direction, scale and source label. No factor P supplied; no same contrast inferred where row labels differ. Treatment Evalue point≥limit≥1 in all8. Smaller primary values do not reproduce this shared-display comparator, F-ST1-004. The primary p19 “5-component” phrase is considered separately as readily resolved wording, without changing any displayed HR assignment.

| S ID | Outcome; treatment HR/upper95%CI | Evalue point/limit | Current vsNever; Quit vsNever smoking HR(CI), unless labeled otherwise | Hypertension contrastHR(CI) | Dyslipidemia contrastHR(CI) | Insulin Yes/No HR(CI) | Pass1 result | Pass1 status | Pass2 status |
|---|---|---|---|---|---|---|---|---|---|
| S076 | Primary;.61/.69 | 2.15/1.92 | 1.25(1.13,1.39);1.13(1.05,1.21) | Yes/No1.05(.95,1.16) | No/Yes1.06(.98,1.16) | 1.33(1.23,1.43) | All5 HR tuples contain/order; Evalues F-ST1-004 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S077 | Secondary;.62/.72 | 2.62/2.11 | 1.37(1.19,1.58);1.14(1.03,1.26) | No/Yes1.04(.91,1.19) | No/Yes1.14(1.02,1.29) | 1.43(1.3,1.58) | All5 HR tuples reconcile; both Evalues overlap reproducing intervals | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S078 | Death;.59/.72 | 2.81/2.13 | 1.51(1.25,1.82);1.12(.98,1.27) | No/Yes1.14(.97,1.35) | No/Yes1.3(1.12,1.5) | 1.73(1.53,1.97) | All5 HR tuples and both Evalues reconcile | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S079 | HF;.38/.49 | 4.69/3.52 | 1.32(1.09,1.6);1.23(1.07,1.41) | Yes/No1.11(.93,1.33) | No/Yes1.27(1.09,1.48) | 1.47(1.29,1.67) | All5 HR tuples and both Evalues reconcile | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S080 | CAD;.69/.87 | 2.27/1.55 | 1.51(1.2,1.89);1.29(1.1,1.51) | No/Yes1.04(.83,1.29) | Yes/No1.16(.96,1.41) | 1.14(.97,1.34) | All5 HR tuples and both Evalues reconcile | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S081 | Cerebrovascular;.67/.94 | 2.35/1.31 | 1.33(.95,1.86);1.3(1.04,1.62) | Yes/No1.44(1.04,1.98) | No/Yes1.08(.83,1.4) | 1.17(.94,1.47) | All5 HR tuples and both Evalues reconcile | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S082 | Nephropathy;.40/.52 | 4.46/3.29 | Never/Current1.23(.96,1.58);Quit/Never1.03(.88,1.19) | Yes/No1.36(1.09,1.69) | No/Yes1.17(.97,1.4) | 1.29(1.11,1.5) | All5 HR tuples and both Evalues reconcile; smoking reference retained literally | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S083 | AF;.78/.97 | 1.9/1.21 | 1.07(.85,1.35);1.16(1,1.34) | Yes/No1.1(.9,1.35) | No/Yes1.27(1.07,1.51) | 1.06(.91,1.22) | All5 HR tuples and both Evalues reconcile; factorCI endpoint1 has no pairedP | PASS_1_COMPLETE | PASS_2_COMPLETE |

## Statistical-method and planned/report dependencies: S084–S100

Each row explicitly covers its entire named relationship, with document roles by content. These are source-grounded logical checks, not requests for a preferred analysis. A method detail missing by itself has no finding. Natural units include repeated measurements, matched cohort membership and outcome-specific risk sets; no randomized-treatment, noninferiority, equivalence, interim, power or stopping claim is supplied.

| S ID | Exact source relationships and printed definitions | Pass1 method/design result and absent definitions | Pass1 status | Pass2 status |
|---|---|---|---|---|
| S084 | REPORT [eFigure2p11](../../../joi190103supp1_prod.pdf#page=11), HbA1c/noninsulin×BMI<35/≥35 four curves each over0–4y; mainFigure4p9 weight%delta14.7(14.5,14.9),P<.001/HbA1cdelta1.1(1.0,1.2),P<.001 | All8 subgroup curves and both main trajectories/bands inspected; surgery generallylower; maindelta time8y and change not absolute level. No eFigure2 exact points/P/bandlevel; no quantitative conflict inferred from curves alone | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S085 | REPORT [eFigure3p16](../../../joi190103supp1_prod.pdf#page=16), protein/albumin/hemoglobin/vitaminD two level curves each through8y; S052–S055 change contrasts | All8 curves inspected; levels and differences in change explicitly distinguished; curve crossings are not a supplied contradiction of a change contrast. No exact curve numbers or curve-specificP | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S086 | REPORT [Table1pp5–6](../../../jama_aminian_2019_oi_190103.pdf#page=6), signed standardized differences vs footnote absolute-value definition | Sign convention is evident in surgery−control statement and bidirectional rows; no altered numerical effect/CI/test result; excluded wording observation. Baseline count/percentage arithmetic assigned numeric checker, not replaced by this method check | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S087 | PLAN [p3 matching](../../../joi190103supp2_prod.pdf#page=3) each nonsurgical to5surgical vs REPORT [p4](../../../jama_aminian_2019_oi_190103.pdf#page=4) each surgical to5nonsurgical,2287/11435; PLANp6 ratios1:1/1:5/1:10 | Explicit matching direction differs and could imply25-fold different surgery/control ratio; F-ST1-006. Ratio shorthand in PLANp6 gives alternative intended direction, not deletion | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S088 | PLAN [pp2–5](../../../joi190103supp2_prod.pdf#page=5) risk and cohort derivation vs REPORTpp2–3/Figure1/Table2 | Composite first incident eligible component, preexisting components omitted but individuals retained; individual prior condition excluded; renal additional eGFR/dialysis exclusions understood. Different control/surgery date/BMI rules stated, no critique of coherent choice. Base287438→matched13722 flow not a power calculation | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S089 | PLAN [p5](../../../joi190103supp2_prod.pdf#page=5) insurance/creatinine in variables “extracted…used for analysis,” [p6](../../../joi190103supp2_prod.pdf#page=6) all baseline variables vs REPORTp4 Table1 variables included/pp5–6 Table1 | Report does not say Table1 is an exclusive model list; insurance omission alone does not reproduce a changed model; excluded CONDITIONAL_OR_UNREPORTED. Creatinine is also linked to derived eGFR and no omitted adjustment is inferred | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S090 | PLAN [p6MI](../../../joi190103supp2_prod.pdf#page=6) and REPORT [p4MI](../../../jama_aminian_2019_oi_190103.pdf#page=4): MICE5, PMM/logistic/polytomous, Rubin estimate/contrastSE | Same descriptions reconcile. NumericSE/df/variance absent, no contradicted step; not infer Rubin df from convention | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S091 | REPORT [p4methods](../../../jama_aminian_2019_oi_190103.pdf#page=4)/Table2 bootstrap1000percentile95%; PLANp6rates/Cox vs eTables4–7 | HR and KMrisk estimands separately identified; all primary risk/HR direction agree. Five ARDpoint discrepancies and cerebrovascularCI/P tracked above. Exact bootstraps/person-times not supplied; no full-data reconstruction claimed | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S092 | REPORT [p4spline](../../../jama_aminian_2019_oi_190103.pdf#page=4), eTable8 four-knot spline×treatment vs [eTable9p13](../../../joi190103supp1_prod.pdf#page=13) observation/patient counts | Repeated observations explicitly distinguished from distinct patients; no printed assertion of independent observations or stated variance contradiction. Missing dependence/variance detail alone excluded; exact data/covariance absent. Weight/HbA1c/nutrition contributor tables fully considered | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S093 | REPORT mainp4/eTable8 two-sample proportions test; [Figure5p10](../../../jama_aminian_2019_oi_190103.pdf#page=10) Fisher exact8y; [eTable10p14](../../../joi190103supp1_prod.pdf#page=14) denominators0:2287/11433,1:1820/10309,2:1444/8762,5:784/4235,8:348/1219 | Fisher comparison fits general two-group proportions wording without specified competing formula; main and eTable8 exact8yP identical for all6 drugs. Time0control count11433 versus full11435 is peripheral precision-scale difference. No exact drug numerators/point proportions, so recomputation not possible | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S094 | PLAN [p6](../../../joi190103supp2_prod.pdf#page=6) secondary multiplicity adjustmentnotperformed/.05/95%; REPORTeTable8p12 Bonferroni98.8%, mainp4 exploratory secondary | Explicit adjustment addition F-ST1-005. Within-table consistency tested using98.8%, not95%; other-antihypertensiveyear1 .02 withCI crossing0 reconciles atadjustedlevel | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S095 | PLAN [p3](../../../joi190103supp2_prod.pdf#page=3) sensitivity baseline/effect/predictionaccuracy and [p6](../../../joi190103supp2_prod.pdf#page=6)15datasets/2,5,8y vs REPORTpp4,8–9/eFigures4/eTable7 | Matching/date-sensitivity HRs all15×8 supplied; timevarying all24 tuples supplied. Predictionaccuracy mentioned in general PLAN sampling motivation but not primary/keysecondary result or statistical decision rule; peripheral missing ancillary comparison excluded | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S096 | PLAN [p4](../../../joi190103supp2_prod.pdf#page=4) primary6,secondary3+[p5](../../../joi190103supp2_prod.pdf#page=5) individual6 vs REPORTabstractpp1–3/Discussionpp9–11 and [eTable1p2](../../../joi190103supp1_prod.pdf#page=2) operational criteria | All8 outcomes reported and named status/components match; time/risk-set definitions match. Operational AF ICD10i48.1 addition and coronary411.X/paired414.X primary-diagnosis restrictions are covered by fresh cross-source findings F-XS-002/F-XS-003; they can affect primary composite/component ascertainment, not inferred event-count changes. All7secondary results not a claim of familywise significance. Supplementp19“5-componentMACE” readilyidentified primary reference; wording excluded | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S097 | PLAN [amendmentp7](../../../joi190103supp2_prod.pdf#page=7) early<90d/lateinterventionproxy/4nutritionalvariables vs REPORTp7/eTables8,11/eFigure3 | Disclosed addition covers stated safety/nutritional endpoints; earlycounts and longer KMincidences differenttimes, no mismatch.90dwording not infer changed window | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S098 | PLAN [amendmentp7](../../../joi190103supp2_prod.pdf#page=7) Evalues for8HR/closestnulllimit vs REPORTpp9,19–20 | All8 supplied, upperCIclosernull since treatmentHR<1. Primary numeric transformation issue S076; formula/HRtoRR mapping absent but comparator supported bysame display. No isolated unreported formula candidate | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S099 | PLAN [p2objective](../../../joi190103supp2_prod.pdf#page=2), REPORT [p1design](../../../jama_aminian_2019_oi_190103.pdf#page=1)/Methods/Discussion | Retrospective matched cohort, no exposure randomization, no supplied power/sampletarget inputs, no NI/equivalence margin, no interim/stopping rule. These checks noapplicable rather than omitted; sample13722 is observed cohort and no stated calculation to reproduce | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S100 | REPORT [p4subgroup](../../../jama_aminian_2019_oi_190103.pdf#page=4) individualinteraction additions vs eFigure1p8 dichotomization/covariateremoval | Supplement details coherent with general mainmethod; no claim these subgroups are prespecified; no candidate for their absence from PLAN. All8interaction and16subgroup tuples trackedS025–S032; lackofcovariance prohibits exactinteractionP reproduction | PASS_1_COMPLETE | PASS_2_COMPLETE |

## Completion and limitations

100 records explicitly PASS_1_COMPLETE;0 omitted inferential units. All372 displayed numeric or graphical estimate/interval tuples in the core repeated displays were checked:32main,8rate-difference,48cumulativeincidence,16subgroup,8repeatedCox,24time-varying,52longitudinal,24intervention,120sensitivity,40known-factor; repeated24time-varying copies, repeatedmainfigure/abstract tuples and two mainFigure4tuples were also checked through their linked records. All16Evalues checked. The count describes comparisons, not independent analyses or findings. No shard exceeds120 natural Srecords.

Limitations: exact graphical sensitivity endpoints/P not printed; comparisons at plot resolution. Raw data, covariance matrices, imputation model internals/df, bootstrap samples, exact patient-times, medication numerators and exact curve coordinates absent. These constrain numeric reconstruction but leave no source-coverage gap. No unsupported preferred-method audit was performed. Findings6 and excluded observations7 are recorded in checkers/statistical_pass_1.md. Pass2 is reserved for a different fresh runtime.

## Completed second pass

Pass 2 owner/runtime: /root/statistics_pass_2; distinct fresh qc162_statistical_consistency_reviewer, gpt-6.1-sol/high. All100 S records above were independently revisited using the complete current candidate ledger, initial screening log, all eight mechanical recheck records, both evidence maps, direct source text and source-matched visual evidence. Every record now has PASS_2_COMPLETE. All372 core numeric/graphical tuples, their repeated copies, all16 E-values and all method/plan dependencies were covered. No printed S evidence or pass-1 assessment was replaced. Every one of the26 prior checker exclusion rows was reassessed against RouteA and the half-unit/.05 rule. New findings0; additional excluded observations0; historical exclusion rows reassessed26 (19 distinct observations after provenance consolidation). Exact individual pass-2 conclusions, retained candidate alternatives/classifications and reconstruction limits are in [checkers/statistical_pass_2.md](../checkers/statistical_pass_2.md). No omitted relationship or scientific-coverage gap remains.
