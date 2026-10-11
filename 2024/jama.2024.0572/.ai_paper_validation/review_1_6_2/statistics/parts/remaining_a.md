# Statistical relationship inventory: remaining A, passes 1 and 2

Runtime ID: root/stat1_remaining_a. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN. Scope: DOC005 physical pages 1-7; DOC006 physical pages 1-12 and 20-32. DOC006 eFigures7-13, physical pages13-19, belong to independent forest shards. This shard reviewed 32 source pages, including 21 reusable page images, and creates 78 stable relationships S3001-S3078. Every relationship below is PASS_1_COMPLETE. No scientific coverage gap remains in the assigned units.

Read QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md completely. Mapping inputs: support_parts/results_a.md A001-A027 and A035-A041, and main_quantitative_evidence.md method/matched-result keys. Direct Poppler26.01.0 pdftotext, transient stdout, checked all DOC005 pages, DOC006pp4-12/20-32, and mainpp3,4,8,10,11. Reusable images DOC006pp5-12/20-32 were inspected visually; source-linked supplied PDF remains authority. No extraction files, sources, or reused assets were changed. Compute device: CPU. No web or unapproved Python used.

## Source and shared contracts

- [DOC005 analysis SAP](../../../../joi240006supp4_prod_1708623115.00733.pdf#page=1) is PLAN by prospective analysis content, including its disclosed post hoc appendix.
- [DOC006 results supplement](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=1) is REPORT. [Main article](../../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=1) is REPORT. All page numbers below are physical PDF pages; DOC006 printed folio equals physical page minus1.
- **P:** PLAN pp3-6 specifies all analyses as-treated, no imputation, exploratory/no multiplicity adjustment; ordinal PIM, mRS5/6 merged; binary modified Poisson with robust standard errors; adjust age, presentation NIHSS, LKW-to-randomization time and core; omit stratifier from adjustment; logistic regression permitted for calibrated binary probability plots. Composite=max(perfusion/diffusion core, CT hypodensity) is primary; perfusion/diffusion alone sensitivity. No sample-size inputs, noninferiority/equivalence margin, stopping threshold, or inferential SE/test statistic occurs in this analysis SAP.
- **R:** Main pp3-4 gives 90-day mRS outcome; ordinal PIM with ties split equally, 95%CI, two-sided P<.05, no multiplicity adjustment; modified Poisson robust binary models; allocated treatment for across-arm effects and received treatment for within-arm associations. Retained336=168/168 randomized or170/166 as-treated. Marginal probabilities and g-computation full ordinal scale with bootstrapped CI for generalized odds curves. Logistic versus Poisson choice for individual plotted binary panels, fitted coefficients, covariate reference distribution, covariance, and pointwise numeric coordinates are not printed. These are named reproduction limits, not independently conflicting values.
- **G:** REPORT eFigures14-17: A=mRS0-2, B=mRS0-3, C=mRS5-6, D=generalized odds of better mRS EVT versus MM. A/B/C arms: cyan EVT, salmon MM. Shading is95%CI; D black curve, dashed null1. Outcome90days. Three probability panels and one odds panel per figure. Exact curve coordinates are not printed; visual statements concern order/direction only, with any numerical reading explicitly diagnostic. Probability bands contain curves; odds endpoints are not numerically printed. No panel-specific P or SE supplied. Do not equate marginal risk differences with generalized odds or impose a single common binary model.
- **C:** REPORT eFigures18-19: EVT patients, independent ambulation mRS0-3, ages30-80 ticks with plotted extension above80; core settings70/100/150mL. Probability legend nine intervals (0.0,0.1] through(0.8,0.9]. No CI or exact fitted-point labels. Neither graph prints time-axis units. The associated main p10 age/time aRR/CI records are duplicates of main-shard relationships, not fresh tests here.
- **D:** REPORT eFigure20a-aa has27 descriptive strata and54 treatment bars,7 categories mRS0-6. Percentages are rounded integers; allocated arms sum168/168 for complementary strata. These are descriptions, with no additional test/P/CI. Displaying separate categories5/6 does not establish that modeled ordinal endpoints were unmerged.

## PLAN method and design relationships

| S ID | Source role/location; mapping | Printed definition, population, or rule | Pass-1 check and missing definition | Status |
|---|---|---|---|---|
| S3001 | PLAN DOC005p2;A001 | Version1.0.0 July7,2023, prespecified secondary SELECT2 analysis | Prospective identity read; no inference about trial publication chronology from supplied date alone | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3002 | PLAN p3;A002 | All SELECT2 enrolled patients for imaging-specific EVT treatment effect | REPORT exclusions explicitly identify16 excluded and336 retained; no hidden denominator assumed. Allocation contract examined S3006 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3003 | PLAN p3;A003 | Core-lab ASPECTS; RAPID rCBF<30%, ADC<620 X106mm/s2 as printed; manual hypodensity | ADC unit/exponent typography understood from imaging context/main definition; no changed numeric result established | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3004 | PLAN p3;A004 | Primary=max(CTP/MRI core,CT hypodensity); perfusion/diffusion-only sensitivity | Compare mainp4 composite called post hoc sensitivity; F-ST1-304. Definition reproducible; analysis hierarchy differs | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3005 | PLAN p3;A005 | Difference hypoperfused-core; ratio 'of ischemic core volume and critically hypoperfused tissue'; favorable1≥1.8 AND≥15mL;2≥1.2 AND≥10mL | No explicit division symbol giving reverse equation. Ratio ordering wording excluded; REPORT examples reproducibly use hypoperfused/core. Joint threshold definitions reconcile | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3006 | PLAN p3;A006 | Discordance core<70/ASPECTS≤5,core≥70/ASPECTS>5; concordance core≥70/ASPECTS≤5; all analyses as-treated; exploratory/no multiplicity | Imaging definitions reconcile. Across-arm analysis changed to allocated treatment per mainp4; F-ST1-303. No required multiplicity correction inferred | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3007 | PLAN p4;A007 | Linearity checks/transformation if substantial deviation; predictive margins; no imputation; mRS5/6 merged | Main outcomes confirms merge; no contradictory transformation or imputation statement. Actual fitted transformation/calibration not individually supplied | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3008 | PLAN p4;A008 | 90-day ordinal PIM; age,NIHSS,LKW-randomization,core; omit stratifier; merge5/6 | Main PIM and covariate specification coherent. Source does not establish that 'full ordinal scale' reverses explicit merged endpoint | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3009 | PLAN p4;A009 | mRS0-2 modified Poisson robust SE; same covariates; logistic fallback for marginal plots if better calibrated | Report binary model matches; logistic choice for each curve unreported, with no numerical contradiction | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3010 | PLAN pp4-5;A010 | mRS0-3 modified Poisson robust SE; same covariates/stratifier omission/logistic fallback | Method internally coherent; no independent SE or test supplied for prediction panels | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3011 | PLAN p5;A011 | EVT subgroup predicted mRS0-3 probability combining age and LKW-to-randomization | Complete REPORT counterpart lookup confirms no age×LKW-to-randomization ambulation surface; reported surfaces use reperfusion endpoints. F-ST1-306 independently applies RouteB; ambulation is not identified as key secondary | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3012 | PLAN p5;A012 | mRS5-6 modified Poisson robust SE/covariates/logistic fallback; descriptive bullet says independent ambulation | Endpoint title and model bullet consistently say5-6; descriptive-copy wording excluded. No contradictory printed estimate | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3013 | PLAN p5;A013 | sICH PHII/remote PH plus NIHSS rise≥4 at4-hour window; few events, count/proportion only,no testing/modeling | No sICH inferential display in assigned report pages; safety outcome cross-source scope delegated. No missing test invented | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3014 | PLAN p5;A014 | Core thresholds70,100,150; ASPECTS0-2/3-5/6-10; interaction | Report stratification matches; categorical interaction P belongs to forest/main shards, not repeated here | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3015 | PLAN p6;A015 | ASPECTS3/4/5 subgroups and treatment interactions | Matching main/forest outcome rows are indexed by ASPECTS rather than independent repeats of same model here | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3016 | PLAN p6;A016 | Mismatch profiles; additionally volume50/100mL strata; interaction; continuous EVT mismatch association | Complete REPORT counterpart lookup confirms no50/100mL mismatch outcome strata; continuous/profile analyses do not reproduce the planned categorical primary mRS comparisons. F-ST1-305 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3017 | PLAN p6;A017 | Concordant/discordant outcomes/treatment interactions | Definitions match main; detailed interaction rows belong to tables/main shards. No conflicting decision rule found in plan | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3018 | PLAN p7;A018 | Explicitly post hoc appendix: CT hypodensity third estimate; composite mismatch; overestimation; follow-up infarct; paired volumes | Disclosed extension; do not call every additional analysis prespecified. Composite itself identified as prespecified here, relevant F-ST1-304 | PASS_1_COMPLETE; PASS_2_COMPLETE |

## REPORT eMethods, illustrative definitions, populations, trend tests

| S ID | Source role/location; mapping | Printed values and analysis | Pass-1 record; duplicate occurrence/missing definition | Status |
|---|---|---|---|---|
| S3019 | REPORT DOC006p4;A019 | Models age,NIHSS,LKW-randomization and one imaging parameter; lower criteria/higher AUC better; BIC0-2 weak,2-6 positive,6-10 strong,>10 very strong | Direction of model-fit rule coherent; actual criteria/AUC cells checked by tables shard. No model-fit significance P inferred | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3020 | REPORT p5;A020 | rCBF core94mL,Tmax131mL,ratio1.4,difference37mL | 131/94=1.3936;131-94=37. Half-unit ratio range130.5/94.5 to131.5/93.5=1.3810-1.4064 overlaps1.35-1.45; difference36-38 overlaps36.5-37.5. Definitions match mainp3 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3021 | REPORT pp6-7;A021-A022 | Example rCBF13mL,Tmax39mL,mismatch26mL,ratio3.0; hypodensity5-12HU | 39/13=3;39-13=26; rounding ranges38.5/13.5 to39.5/12.5=2.8519-3.16 and25-27 overlap displayed intervals. Follow-up DWI has no fitted/test value | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3022 | REPORT p8;A023 |958-606=352;352-4=348;348-12=336; randomized168/168;received170/166 with2 MM crossovers | Population arithmetic reconciles and allocation/received labels distinguish estimands; same mainp4 population. No hidden test or population inserted | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3023 | REPORT p9;A024 | CT hypodensity larger19,44,59,68,76,76,76,86%; perfusion larger81,56,41,33,24,24,24,14% across0-24h bins | Narrative direction and first/last percentages reconcile with mainp4. 68+33=101 has rounding intervals summing100-102, includes100. Descriptive only; no independent trend test printed | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3024 | REPORT p10 eFigure5a;A025a | CTP1.2/10 no-mismatch4,10,13,10,7,4,4,14%; P for trend=.71 | Mainp8 duplicate .71/nonsignificant association. No CI/test statistic/bin denominator or trend algorithm supplied; cannot reconstruct exact P from percentages | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3025 | REPORT p10 eFigure5b;A025b | CTP1.8/15 no-mismatch62,42,47,32,30,26,4,29%; P<.001 | Mainp8/11 duplicate declining absence. Direction coherent, with nonmonotone bins allowed. No independent CI,denominators,test algorithm | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3026 | REPORT p11 eFigure5c;A026c | Composite1.2/10 no-mismatch8,18,27,24,26,22,20,29%; P=.27 | No interval or numeric trend coefficient contradicts P; bin percentages insufficient to reproduce test. Mainp8 describes no longer observing increasing mismatch | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3027 | REPORT p11 eFigure5d;A026d | Composite1.8/15 no-mismatch73,60,74,56,65,63,32,71%; P=.18 | No test/CI conflict; no bin denominators or algorithm. Nonsignificance cannot be deduced or refuted from unweighted bar slope | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3028 | REPORT p12 eFigure6a;A027a | CTP1.2/10 no-mismatch2,6,13,28%;mismatch98,94,87,73%;P<.001 | Increasing absence agrees caption/mainp8. 28+73=101 compatible rounding; bins0-49/50-99/100-149/≥150. No printed trend coefficient/CI or algorithm | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3029 | REPORT p12 eFigure6b;A027b | CTP1.8/15 no-mismatch4,29,68,83%;mismatch96,71,32,18%;P<.001 | Increasing absence agrees caption/mainp8. 83+18=101 compatible rounding; no assumption that categorical bars supply exact continuous test | PASS_1_COMPLETE; PASS_2_COMPLETE |

## REPORT prediction panels

All graph records use G or C and source-linked page/figure identities. Panel-wise model coefficients, exact pointwise coordinates, pointwise SE, and bootstrap replicates are absent; confidence shading is inspected for containment/order without inventing numeric limits. No unsupported interval-versus-P comparison is made.

| S ID | Source role/location; mapping | Printed axes/outcome/conditioning; population | Check record and duplicates | Status |
|---|---|---|---|---|
| S3030 | REPORT p20 eFigure14A;A035 | ASPECTS10,7.5,5,2.5,0; mRS0-2,y0,.2,.4,.6;composite adjusted;G | EVT slight rise/MM fall as ASPECTS decreases. No narrative significance tied to this individual curve | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3031 | REPORT p20 eFigure14B;A035 | Same ASPECTS; mRS0-3,y0,.2,.4,.6,.8;G | Both probabilities decline,EVT above MM;bands contain curves; mainp6 ASPECTS association at composite adjustment is distinct fitted summary | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3032 | REPORT p20 eFigure14C;A035 | Same ASPECTS; mRS5-6,y.25,.50,.75,1;G | Both probabilities rise,MM above EVT; adverse outcome direction coherent | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3033 | REPORT p20 eFigure14D;A035 | Generalized odds better mRS,y1,2,3;null1;G | Odds rise as ASPECTS decreases;caption explicitly explains favorable-ASPECTS eligibility. No individual contrast P printed | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3034 | REPORT p21 eFigure15A;A036 | Hypodensity0,100,200,300mL;mRS0-2,y0,.2,.4,.6;G | Both decline;EVT/MM curves cross at high volumes; no significance claim for crossing. Post hoc analysis disclosed in SAP | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3035 | REPORT p21 eFigure15B;A036 | Hypodensity same;mRS0-3,y0,.25,.50,.75;G | Both decline;band containment; no P or precise fitted point | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3036 | REPORT p21 eFigure15C;A036 | Hypodensity same;mRS5-6,y.25,.50,.75,1;G | Both rise with visible high-volume convergence/crossing;no outcome-label reversal | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3037 | REPORT p21 eFigure15D;A036 | Hypodensity same;generalized odds,y1,2,3,4,null1;G | Odds decline and reach below1 at high volumes;CI includes null there. No separate significant-benefit assertion tied to that point | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3038 | REPORT p22 eFigure16A;A037 | Composite0,100,200,300mL;mRS0-2,y0,.25,.50,.75;G | Both decline;probabilities stay0-1 and within bands. PLAN/REPORT hierarchy F-ST1-304 distinct from curve logic | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3039 | REPORT p22 eFigure16B;A037 | Composite same;mRS0-3,y0,.25,.50,.75;G | Both decline,EVT above MM; no printed panel P | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3040 | REPORT p22 eFigure16C;A037 | Composite same;mRS5-6,y.25,.50,.75,1;G | Both rise,MM above EVT;adverse direction coherent | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3041 | REPORT p22 eFigure16D;A037 | Composite same;odds,y1,2,3,4,5,null1;G | Declines toward1;CI encompasses1 at high volumes;no contradictory significance decision | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3042 | REPORT p23 eFigure17A;A038 | Mismatch-100,0,100,200,300,400mL;mRS0-2,y0,.2,.4,.6;G | Both curves decline;mainp8 says EVT increases. F-ST1-301; same direction pattern asS3043 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3043 | REPORT p23 eFigure17B;A038 | Same mismatch;mRS0-3,y0,.25,.50,.75;G | Both decline;mainp8 says EVT increases. Consolidated F-ST1-301,not separate issue | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3044 | REPORT p23 eFigure17C;A038 | Same mismatch;mRS5-6,y.25,.50,.75,1;G | Both rise. Negative x ticks reflect composite-minus-hypoperfusion possibility/model domain; not invented negative counts | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3045 | REPORT p23 eFigure17D;A038 | Mismatch0,100,200 ticks;odds1,1.5,2,2.5,null1;G | Slight decline;CI above1 across most range and approaches1 at high edge;no printed P or separate decision | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3046 | REPORT p24 eFigure18a;A039 | Core70mL;age30-80;CTP-to-reperfusion/end time100,200,300;C | Higher age/time lowers probability;CTP/MRI title versus composite prose F-ST1-302;mainp10 CTP/MRI corroborates title | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3047 | REPORT p24 eFigure18b;A039 | Core100mL;same age/time/probability legend;C | Same direction;probability lower than70 panel at common age/time;consolidated F-ST1-302 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3048 | REPORT p24 eFigure18c;A039 | Core150mL;same axes;C | Same direction;lower than100 panel;young/rapid-treatment sentence consistent with displayed bands;F-ST1-302 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3049 | REPORT p25 eFigure19a;A040 | Composite70mL;age30-80;LKW-to-reperfusion/end time0,500,1000,1500;C | Higher age/time lowers probability. Mainp10 calls same contours CTP/MRI,also F-ST1-302. No significant-time slope inferred from colors | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3050 | REPORT p25 eFigure19b;A040 | Composite100mL;same axes/legend;C | Same direction;common-coordinate probability below70 panel;F-ST1-302 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S3051 | REPORT p25 eFigure19c;A040 | Composite150mL;same axes/legend;C | Same direction;common-coordinate probability below100 panel;F-ST1-302 | PASS_1_COMPLETE; PASS_2_COMPLETE |

## REPORT descriptive distribution relationships relevant to ordinal method

Each record is D. Values preserve mRS0,1,2,3,4,5,6 order; zero-width categories use legend identity. All descriptive distributions were reviewed against their labels and ordinal modeling endpoint. No independent inferential test is printed. Detailed count/percentage consistency belongs to the numeric shard; no crude ratio is substituted for a PIM/modified-Poisson estimate.

| S ID | REPORT physical page/panel;A041 | Stratum; EVT n: percentages0-6; MM n: percentages0-6 | Method check | Status |
|---|---|---|---|---|
| S3052 |26/a|NCCT<70;68:3,6,16,25,10,9,31;64:0,2,5,14,19,22,39|D; descriptive7-category bars, no test|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S3053 |26/b|NCCT≥70;100:0,4,13,14,20,8,41;104:0,2,6,10,22,17,43|D; same|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S3054 |26/c|NCCT<100;103:2,8,18,22,14,9,27;104:0,3,5,12,23,21,37|D; same|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S3055 |26/d|NCCT≥100;65:0,0,8,12,20,8,52;64:0,0,6,11,17,16,50|D; same|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S3056 |27/e|NCCT<150;151:1,5,15,19,13,9,37;146:0,2,5,12,22,18,40|D; same|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S3057 |27/f|NCCT≥150;17:0,0,6,12,41,6,35;22:0,0,5,5,14,23,55|D; same|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S3058 |27/g|CTP/MRI<70;82:2,9,17,26,13,6,27;74:0,3,9,19,26,16,27|D; same|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S3059 |27/h|CTP/MRI≥70;86:0,1,12,12,19,10,47;94:0,1,2,5,17,21,53|D; same|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S3060 |28/i|CTP/MRI<150;147:1,5,16,20,15,8,35;149:0,2,6,13,21,19,38|D; same|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S3061 |28/j|CTP/MRI≥150;21:0,0,5,10,24,10,52;19:0,0,0,0,16,16,68|D; same|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S3062 |28/k|composite<70;42:5,10,19,29,5,5,29;38:0,3,8,21,24,18,26|D; same|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S3063 |28/l|composite≥70;126:0,3,13,15,20,10,40;130:0,2,5,8,20,19,46|D; same|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S3064 |29/m|composite<100;80:3,9,21,25,10,9,24;85:0,2,6,13,27,20,32|D; same|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S3065 |29/n|composite≥100;88:0,1,8,13,22,8,49;83:0,1,5,10,14,18,52|D; same|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S3066 |29/o|composite<150;135:1,6,16,20,13,9,35;138:0,2,6,13,22,19,38|D; same|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S3067 |29/p|composite≥150;33:0,0,6,12,30,6,45;30:0,0,3,3,13,20,60|D; same|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S3068 |30/q|ASPECTS0-2;11:0,0,0,0,18,27,55;8:0,0,0,0,0,38,63|D; no modeled improvement inferred from6-to5 bar difference|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S3069 |30/r|ASPECTS3-5;139:1,6,15,20,17,6,35;138:0,1,6,12,22,20,38|D; same|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S3070 |30/s|ASPECTS6-10;18:0,0,17,17,11,17,39;22:0,5,5,9,18,9,55|D; same|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S3071 |30/t|ASPECTS3;45:0,4,11,11,24,9,40;28:0,4,4,11,11,18,54|D; same|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S3072 |31/u|ASPECTS4;31:3,3,16,26,13,6,32;57:0,2,4,9,25,21,40|D; same|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S3073 |31/v|ASPECTS5;63:2,8,17,24,13,3,33;53:0,0,9,17,26,19,28|D; same|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S3074 |31/w|ASPECTS<6/CTP<70;76:3,9,16,26,13,7,26;63:0,2,10,19,25,17,27|D; same|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S3075 |32/x|ASPECTS≥6/CTP≥70;12:0,0,8,17,8,25,42;11:0,0,0,0,9,9,82|D; same|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S3076 |32/y|ASPECTS<6/CTP≥70;74:0,1,12,11,20,8,47;83:0,1,2,6,18,23,49|D; same|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S3077 |32/z|noCTP1.2/10mismatch;8:0,0,0,25,38,0,38;21:0,0,5,14,14,24,43|D; same|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S3078 |32/aa|CTP1.2/10mismatch;160:1,5,15,18,15,9,37;147:0,2,5,11,22,18,42|D; same|PASS_1_COMPLETE; PASS_2_COMPLETE|

## Coverage and limits

DOC005p1 and DOC006pp1-3 are title/contents with no independent inferential value. All other assigned content appears above. No sample-size calculation, superiority/noninferiority/equivalence margin, multiplicity adjustment threshold, interim threshold, or stopping statistic is stated within this shard; no such calculation is invented. Missing exact graph coefficients, binary plot-model identity, probability reference covariates, confidence bootstrap inputs, trend algorithm and bin denominators limit exact numerical reconstruction, while direction, labels, stated rules, model coherence and every displayed P were still checked. Complete REPORT counterpart lookup for S3011/S3016 was supplied in checkers/cross_source_parts/reports.md, Requested bounded REPORT-counterpart confirmation, and incorporated into independent planned-analysis reasoning. No coverage dependency remains open.

## Fresh independent pass-2 completion

Runtime ID: root/stat2_remaining_a; model gpt-6.1-sol; reasoning effort high; FRESH_SPAWN, distinct from pass1. All 78 retained S records were independently reread against exact supplied sources, the complete candidate ledger, every mechanical recheck and all 31 initial screening decisions/justifications. No pass-1 evidence record or stable ID was removed. Each original relationship row now explicitly carries both PASS_1_COMPLETE and PASS_2_COMPLETE. Zero new findings; all eight pass-1 apparent exclusions remain excluded under independently reapplied scope rules. No fresh derivative or source modification was needed; CPU direct Poppler26.01.0 and 21 source-linked reusable page images supplied complete assigned coverage. Exact per-ID reasoning follows, also preserved in checkers/statistical_parts/pass2_remaining_a.md.

| S ID | Independent pass-2 reasoning and source/recheck implication | Status |
|---|---|---|
| S3001 | Pp2 version/date and prespecified secondary-analysis identity confirmed; chronology alone supplies no competing result or inference. | PASS_2_COMPLETE |
| S3002 | Pp3 enrolled population versus R flow:16 exclusions are disclosed and 352−16=336; no undisclosed inference population manufactured. | PASS_2_COMPLETE |
| S3003 | Pp3 imaging thresholds/measurement identities match source; ADC exponent/unit typography remains recoverable from immediate imaging context, without changed extracted numeric threshold. | PASS_2_COMPLETE |
| S3004 | Pp3 composite-primary/perfusion-sensitivity hierarchy conflicts with reported status; retained C003, with explicit max definition and no presumed amendment. | PASS_2_COMPLETE |
| S3005 | Pp3 ratio wording has no explicit reverse division equation; R illustrative131/94=1.3936 establishes immediate meaning. Threshold1.8/15 and1.2/10 pairs match. | PASS_2_COMPLETE |
| S3006 | Pp3 discordance and exploratory/no-adjustment rules coherent; all-as-treated differs from reported across-arm allocation, retained C002. No preferred multiplicity choice imposed. | PASS_2_COMPLETE |
| S3007 | Pp4 transformations, no imputation and merged5/6 read directly; seven descriptive categories do not establish unmerged fitted ordinal comparisons. | PASS_2_COMPLETE |
| S3008 | Pp4 PIM endpoint/covariates/stratifier omission match main methods; allocation difference is C002 and no full-scale-versus-merged fitting contradiction is established by descriptive bars. | PASS_2_COMPLETE |
| S3009 | Pp4 modified-Poisson/robust-SE and permitted logistic calibration coherent; no fitted coefficient/SE identifies a contradictory probability panel. | PASS_2_COMPLETE |
| S3010 | Ppp4–5 ambulation endpoint/covariates/calibration fallback coherent; individual curve model is not supplied and no own effect test/interval is compared. | PASS_2_COMPLETE |
| S3011 | Pp5 age×LKW-to-randomization differs from reperfusion-based reported surfaces; retained C009 RouteB, without treating non-key ambulation absence as category5. | PASS_2_COMPLETE |
| S3012 | Pp5 heading and explicit model identify mRS5–6 despite descriptive-copy ambulation wording; no conflicting numeric endpoint attribution. | PASS_2_COMPLETE |
| S3013 | Pp5 four-hour sICH rule read directly; retained C015 P_P only after recheck, since parent PLAN24-hour definition conflicts but REPORT named criterion alone does not print a window. No missing safety test inferred. | PASS_2_COMPLETE |
| S3014 | Pp5 70/100/150 thresholds and0–2/3–5/6–10 ASPECTS groups match displays; interactions are checked in their independent effect shards. | PASS_2_COMPLETE |
| S3015 | Pp6 3/4/5 ASPECTS-specific analyses and interactions match their displayed stratification; no new primary rule or hierarchy change. | PASS_2_COMPLETE |
| S3016 | Pp6 categorical50/100mL mismatch analyses invoking primary mRS are distinct from profile/continuous results; complete counterpart handoff and recheck retain C016, while C007 addresses a separate direction statement. | PASS_2_COMPLETE |
| S3017 | Pp6 concordance/discordance definitions match R; C018 concerns printed profile count attribution rather than a new definition discrepancy. | PASS_2_COMPLETE |
| S3018 | Pp7 appendix expressly discloses additional post-hoc analyses and calls composite prespecified; retained C003. Other explicitly added analyses do not falsely acquire prespecified status. | PASS_2_COMPLETE |
| S3019 | Rp4 low information criterion/high AUC fit direction and BIC bands read directly; no unsupported P interpretation or inferential equivalence imposed on model-fit comparisons. | PASS_2_COMPLETE |
| S3020 | Rp5 131/94=1.3936 and131−94=37; input half-unit ranges ratio[1.3810,1.4064] and difference[36,38] overlap printed1.4/37 intervals. | PASS_2_COMPLETE |
| S3021 | Rpp6–7 example39/13=3,39−13=26; rounding ranges[2.8519,3.16]/[25,27] overlap displayed values; DWI continuation carries no independent test. | PASS_2_COMPLETE |
| S3022 | Rp8 flow958−606=352,352−4−12=336,168+168=336,170+166=336; twoMM→EVT crossovers distinguish populations. Allocation specification remains C002. | PASS_2_COMPLETE |
| S3023 | Rp9 rising hypodensity-larger proportions agree with caption/main direction;68+33=101 lies within joint[100,102] rounding interval. No inferential statistic printed. | PASS_2_COMPLETE |
| S3024 | Rp10 profile1.2/10 trendP=.71 matches main nonsignificant time result; no coefficient/CI/bin denominator or supported reproducing algorithm gives a competing test. | PASS_2_COMPLETE |
| S3025 | Rp10 profile1.8/15 P<.001 accompanies decreasing absence overall; nonmonotonic bins do not contradict a trend and no own interval is printed. | PASS_2_COMPLETE |
| S3026 | Rp11 composite1.2/10 P=.27 has no contradictory effect estimate/CI; unweighted bars cannot establish the actual source trend test. | PASS_2_COMPLETE |
| S3027 | Rp11 composite1.8/15 P=.18 has no matched inferential interval or statement claiming significance; denominators/algorithm remain exact named missing inputs. | PASS_2_COMPLETE |
| S3028 | Rp12 1.2/10 absence increases with core andP<.001;28+73=101 has rounding sum[100,102]. No source-supported second test. | PASS_2_COMPLETE |
| S3029 | Rp12 1.8/15 absence increases with core andP<.001;83+18=101 allows100 after rounding. Four core bins do not identify a continuous versus categorical testing convention. | PASS_2_COMPLETE |
| S3030 | Rp20A decreasing-ASPECTS horizontal orientation confirmed: EVT rises slightly/MM falls; probability bounds and curve-band containment reconcile, with no matched significant-effect claim. | PASS_2_COMPLETE |
| S3031 | Rp20B both ambulation curves decline as ASPECTS decreases, EVT aboveMM; visible confidence containment holds. A composite-adjusted plot is not equated to an unadjusted-for-core narrative model. | PASS_2_COMPLETE |
| S3032 | Rp20C adverse probabilities rise as ASPECTS decreases, MM aboveEVT; probability bounds/95% shading coherent. | PASS_2_COMPLETE |
| S3033 | Rp20D better-outcome odds rise as ASPECTS decreases; curve within shading and null1 shown. Caption provides eligibility context; no contradictory pointwise significance claim. | PASS_2_COMPLETE |
| S3034 | Rp21A independence curves fall with hypodensity; high-volume crossing has no significant-benefit assertion. Curves remain in shading. | PASS_2_COMPLETE |
| S3035 | Rp21B ambulation curves fall, with ordered probability axes and confidence shading; no pointwise numeric estimate/P supplied. | PASS_2_COMPLETE |
| S3036 | Rp21C adverse probabilities rise; high-volume convergence/crossing is consistent with probabilities and does not independently establish a test conflict. | PASS_2_COMPLETE |
| S3037 | Rp21D odds decline below1 at high volume while CI includes1; no matched claim of significant benefit at those coordinates. | PASS_2_COMPLETE |
| S3038 | Rp22A composite-core independence decreases in both arms and curves stay within95% bands. Analysis hierarchy remains C003, distinct from graph containment. | PASS_2_COMPLETE |
| S3039 | Rp22B ambulation decreases in both arms, with EVT aboveMM and contained bands; no individual P/SE printed. | PASS_2_COMPLETE |
| S3040 | Rp22C adverse probabilities increase, MM aboveEVT; no direction/reference reversal in this panel. | PASS_2_COMPLETE |
| S3041 | Rp22D odds approach1 at high composite core and shaded interval encompasses1; no separate significant-benefit conclusion is asserted there. | PASS_2_COMPLETE |
| S3042 | Rp23A cyan EVT independence decreases as labeled mismatch volume increases; directly reread main increasing statement conflicts, retained C007 category2. | PASS_2_COMPLETE |
| S3043 | Rp23B cyan EVT ambulation also decreases, retained same C007 pattern; binary profile associations are different contrasts. | PASS_2_COMPLETE |
| S3044 | Rp23C adverse probabilities rise in both arms; negative axis domain is not a printed negative participant count and composite differences/model plotting need not share perfusion-only geometry. | PASS_2_COMPLETE |
| S3045 | Rp23D odds decline slightly; shaded interval stays above1 over most plotted range and meets null near edge. No unsupported matched P or fixed inference reconstructed. | PASS_2_COMPLETE |
| S3046 | Rp24 core70 panel probability declines with age/acquisition-to-reperfusion; C008 retains title/prose core identity and C009 retains planned time difference. | PASS_2_COMPLETE |
| S3047 | Rp24 core100 panel is lower at common coordinates and declines with age/time; same C008/C009, not additional issues. | PASS_2_COMPLETE |
| S3048 | Rp24 core150 panel is lower again, with young/rapid-treatment narrative consistent with probability bands; same C008/C009 and no missing confidence interval turned into a finding. | PASS_2_COMPLETE |
| S3049 | Rp25 core70 uses LKW-to-reperfusion and composite title/prose; same C008 cross-document identity and C009 time specification. Visible slope alone does not imply significant time effect. | PASS_2_COMPLETE |
| S3050 | Rp25 core100 lower probability at common age/time, with small negative time slope; no inferred P conflict from contour colors. Same C008/C009. | PASS_2_COMPLETE |
| S3051 | Rp25 core150 lower probability again;9 legend probability bins ordered coherently, with no inferential CI printed. Same C008/C009. | PASS_2_COMPLETE |
| S3052 | Rp26a NCCT<70 n68/64 category order confirmed; descriptive totals permit100 after rounding; mRS5/6 split does not determine modeled treatment-success coding. | PASS_2_COMPLETE |
| S3053 | Rp26b NCCT≥70 n100/104 complements68/64 to168/168; category colors/percentages coherent, with no own test. | PASS_2_COMPLETE |
| S3054 | Rp26c NCCT<100 n103/104; score0–6 legend and favorable/adverse separation confirmed; rounded total permits100. | PASS_2_COMPLETE |
| S3055 | Rp26d NCCT≥100 n65/64 complements103/104 to168/168; zero-width favorable categories not shifted to adjacent colors. | PASS_2_COMPLETE |
| S3056 | Rp27e NCCT<150 n151/146 category sequence confirmed; seven percentages consistent with a rounded distribution, without inferential cells. | PASS_2_COMPLETE |
| S3057 | Rp27f NCCT≥150 n17/22 complements151/146; percent6/12/41/6/35 EVT and5/5/14/23/55 MM fit ordinary integer outcome proportions within precision. | PASS_2_COMPLETE |
| S3058 | Rp27g CTP<70 n82/74 category order confirmed, probability totals compatible with100; no adjusted effect is equated to crude cumulative categories. | PASS_2_COMPLETE |
| S3059 | Rp27h CTP≥70 n86/94 complements82/74; mRS0/1 tiny or zero-width cells read by legend, not by numeric token position. | PASS_2_COMPLETE |
| S3060 | Rp28i CTP<150 n147/149 categories confirmed; no exact secondary-test input from descriptive distributions. | PASS_2_COMPLETE |
| S3061 | Rp28j CTP≥150 n21/19 complements147/149; MM mRS0–3 all zero and16/16/68 adverse-side categories coherent. Finite adjusted tests reside in forest shard, not inferred here. | PASS_2_COMPLETE |
| S3062 | Rp28k composite<70 n42/38 favorable0–3 and adverse5–6 categories remain disjoint; rounding allows100. | PASS_2_COMPLETE |
| S3063 | Rp28l composite≥70 n126/130 complements42/38; category readout and labels coherent. Composite hierarchy remains separate C003. | PASS_2_COMPLETE |
| S3064 | Rp29m composite<100 n80/85 distributions confirmed with rounding-compatible total and explicit outcome legend. | PASS_2_COMPLETE |
| S3065 | Rp29n composite≥100 n88/83 complements80/85; no shifted zero cells, no printed inferential statistic. | PASS_2_COMPLETE |
| S3066 | Rp29o composite<150 n135/138 distributions confirmed; overlap with other thresholds is expected nested stratification, not independent extra patients. | PASS_2_COMPLETE |
| S3067 | Rp29p composite≥150 n33/30 complements135/138; separate5/6 bars do not establish that6→5 was modeled as a success. | PASS_2_COMPLETE |
| S3068 | Rp30q ASPECTS0–2 n11/8 both arms have zero favorable0–3 outcomes; this corroborates C004 finite-fit question but does not identify a fitting rule. 38+63=101 compatible with37.5/62.5 rounding. | PASS_2_COMPLETE |
| S3069 | Rp30r ASPECTS3–5 n139/138; favorable/adverse category sums coherent. With other ASPECTS groups gives168/168. | PASS_2_COMPLETE |
| S3070 | Rp30s ASPECTS6–10 n18/22; zero-width early EVT cells retained and17/17/11/17/39 visible categories read against legend. | PASS_2_COMPLETE |
| S3071 | Rp30t ASPECTS3 n45/28; separate score-specific rows are partitions of3–5, not new inferential tests. | PASS_2_COMPLETE |
| S3072 | Rp31u ASPECTS4 n31/57; category0/1 small percentages confirmed, distribution total within rounding. | PASS_2_COMPLETE |
| S3073 | Rp31v ASPECTS5 n63/53;45+31+63=139 EVT and28+57+53=138 MM; no population discrepancy. | PASS_2_COMPLETE |
| S3074 | Rp31w ASPECTS<6/CTP<70 n76/63 distributions confirmed; labels agree with planned discordant-profile1. | PASS_2_COMPLETE |
| S3075 | Rpp31–32x ASPECTS≥6/CTP≥70 n12/11:EVT8%mRS2+17%mRS3, MM no favorable cells; corroborates C018 opposite table attribution, with no new finding. | PASS_2_COMPLETE |
| S3076 | Rp32y ASPECTS<6/CTP≥70 n74/83;76+12+74=162 EVT and63+11+83=157 MM omit favorable-ASPECTS/small-core cells rather than imply complete partitions. No total168 requirement imposed on selected profiles. | PASS_2_COMPLETE |
| S3077 | Rp32z noCTP1.2/10 mismatch n8/21:EVT25/38/0/38 displayed tail sum101 compatible with2/3/0/3 events; no PIM reconstructed from the split tail. | PASS_2_COMPLETE |
| S3078 | Rp32aa CTP1.2/10 mismatch n160/147 complements8/21 to168/168; categorical distribution coherent within precision and no separate effect test claimed. | PASS_2_COMPLETE |

