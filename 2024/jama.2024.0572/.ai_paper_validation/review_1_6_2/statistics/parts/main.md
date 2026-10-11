# Statistical relationship inventory — main REPORT pass 1

Runtime agent: `/root/stat1_main`; model `gpt-6.1-sol`; effort `high`; fresh PASS 1 only. Assigned scope is DOC-001 main REPORT, physical PDF pp.1–14, including every printed inferential estimate, interval, interaction P, narrative test and statistical-method statement. Supporting REPORT rows and PLAN logic belong to other disjoint shards. Source: [main REPORT](../../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=1). Mapping input: extraction/main_quantitative_evidence.md M001–M120 and complete source-matched locator appendix. Direct Poppler pdftotext checks pp.1,6–10; reusable source-matched layout supplies remaining main methods. Reused p.6 image and fresh direct p.10 rendering visually confirmed the finding. All 14 main pages mapped; pp.13–14 contain no additional inferential analysis. Duplicate abstract/narrative/table appearances are matched within a record.

## Common source-defined analysis contracts

- **O (ordinal treatment):** 90-day mRS distribution, primary scores 5/6 merged; adjusted probabilistic index model (PIM), ties split equally; ITT allocated EVT vs MM, total336 (168/168). Figure1 adjusts age, NIHSS, time last-known-well to randomization, core volume; core omitted within core-volume strata. aGenOR>1 favors EVT. CI95%; all report hypothesis tests two-sided, significance P<.05, exploratory with no multiplicity adjustment. No row-effect P, test statistic, SE, covariance, or PIM test distribution is printed. Exact row-level P cannot be reconstructed without those definitions; containment/order/direction and the printed significance claims can be checked.
- **W (within-arm imaging):** as-treated EVT170/MM166 (2 crossovers), 90-day mRS; PIM aGenOR for ordinal distribution; modified Poisson regression with robust standard errors for binary outcomes. Table2 adjusts age, NIHSS, time; ASPECTS per1-point decrease, CTP/MRI core per10mL increase. Table3 additionally adjusts core and contrasts presence of mismatch with no-mismatch reference within each received-treatment arm. >1 means better ordinal outcome or greater binary-outcome risk/rate, respectively. CI95%, two-sided .05. Printed 'absolute risk reduction' expansion of aRR coexists with an explicit rate-ratio footnote and positive ratio scale; identity issue self-screened separately. No individual-effect P, SE or variance matrix supplied.
- **I (interaction):** treatment×characteristic term, categorical and continuous imaging examined separately where possible (p.4). Printed P values are heterogeneity tests, not row-effect P values. Exact fitted common versus arm-specific nuisance coefficients, contrast, degrees of freedom, covariance and test statistic are not supplied. A difference-of-independent-log-estimates diagnostic is not the stated interaction test and does not establish a contradiction by itself.
- **D (predictions):** g-computation full ordinal scale and bootstrapped confidence intervals, predicted margins/marginal probabilities. Curves are modeled, rather than raw proportions; no exact pointwise numerical table is printed. Full ordinal scale explicitly differs from primary merged5/6 analysis.

Every record below has explicit PASS_1_COMPLETE status. Checks that reconcile remain in these records; only apparent observations self-screened out are in the checker Excluded observations table. No evidence state or human disposition is assigned here.

## Figure 1 ordinal rows: all estimates, populations and matched occurrences

All rows use O; exact source [Figure1 p.6](../../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6). Each printed estimate lies within ordered positive endpoints and agrees with favors-EVT labeling; CI null-membership is shown. Mappings identify all duplicate locations. Medians/IQRs are descriptive, rather than intervals for the treatment effect.

| S ID | Stratum; total n; EVT vs MM mRS median(IQR) | aGenOR(95% CI) | Additional same-analysis locations | Check record | Pass status |
|---|---|---|---|---|---|
| S001 | ASPECTS0–2;19;6(5–6) vs6(5–6) |1.52(0.94–2.46)|M055|Contains null1; no row P or significant claim|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S002 | ASPECTS3–5;277;4(3–6) vs5(4–6)|1.82(1.40–2.35)|p.4 narrative M020|Excludes1; narrative significantly better reconciles|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S003 | ASPECTS6–10;40;5(3–6) vs6(4–6)|1.55(0.81–2.98)|M057|Contains1; no row P or significant claim|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S004 | ASPECTS3;73;4(3–6) vs6(4–6)|1.71(1.04–2.81)|pp.1,4 abstract/narrative|Excludes1; improvement/significant narrative reconciles|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S005 | ASPECTS4;88;4(3–6) vs5(4–6)|2.01(1.19–3.40)|pp.1,4 abstract/narrative|Excludes1; improvement/significant narrative reconciles|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S006 | ASPECTS5;116;3(2–6) vs4(3–6)|1.85(1.22–2.79)|pp.1,4 abstract/narrative|Excludes1; improvement/significant narrative reconciles|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S007 | Core<70mL;156;3(2–6) vs4(3–6)|1.78(1.24–2.56)|pp.5–6 narrative M061|Excludes1; direction reconciles|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S008 | Core≥70mL;180;5(4–6) vs6(4–6)|1.63(1.23–2.16)|pp.1,5–6|Excludes1; matching estimate/direction reconciles|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S009 | Core<100mL;236;4(2–6) vs5(4–6)|1.91(1.44–2.55)|pp.5–6|Excludes1; direction reconciles|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S010 | Core≥100mL;100;6(4–6) vs6(5–6)|1.41(0.99–2.02)|pp.1,5–6,10 discussion;Figure2 p.7|Contains1; discussion identifies point-estimate benefit and uncertainty, without row significance claim|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S011 | Core<150mL;296;4(3–6) vs5(4–6)|1.82(1.42–2.34)|pp.5–6|Excludes1; direction reconciles|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S012 | Core≥150mL;40;6(4–6) vs6(5–6)|1.47(0.84–2.56)|pp.1,5–6,10–11 discussion|Contains1; discussion explicitly notes wide CI and point-estimate direction|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S013 | Mismatch≥1.2 AND≥10mL:no;29;4(4–6) vs5(4–6)|2.11(0.97–4.58)|pp.8,10–11|Contains1; few patients and uncertainty disclosed|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S014 | Mismatch≥1.2 AND≥10mL:yes;307;4(3–6) vs5(4–6)|1.75(1.38–2.24)|pp.8,10–11|Excludes1; treatment direction reconciles|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S015 | Mismatch≥1.8 AND≥15mL:no;120;5(4–6) vs6(4–6)|1.68(1.17–2.40)|pp.8,10–11|Excludes1; treatment direction reconciles|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S016 | Mismatch≥1.8 AND≥15mL:yes;216;4(2–6) vs5(4–6)|1.79(1.33–2.42)|pp.8,10–11|Excludes1; treatment direction reconciles|PASS_1_COMPLETE; PASS_2_COMPLETE|

## Figure 1 heterogeneity tests

All use I, ITT336, source Figure1 p.6 and methods p.4; no interaction estimate/interval/SE printed. Source narrative says no significant heterogeneity. All P>.05, so that stated decision reconciles; exact interaction statistics cannot be reconstructed from the separate within-stratum estimates without named missing definitions in I. These P values never substitute for individual-effect P values.

| S ID | Characteristic/test | Printed P | Matched locations | Check record | Pass status |
|---|---|---|---|---|---|
| S017 | ASPECTS0–2/3–5/6–10 |.80|p.6 Figure1, M055–57|Nonsignificant heterogeneity; no directly contradicted test statistic|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S018 | ASPECTS3/4/5 |.80|pp.4,6;S004–006|Nonsignificant heterogeneity agrees with narrative|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S019 | Core<70/≥70mL |.92|pp.5–6;S007–008|Nonsignificant heterogeneity agrees with narrative|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S020 | Core<100/≥100mL |.29|pp.5–6;S009–010|Nonsignificant heterogeneity agrees with narrative|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S021 | Core<150/≥150mL |.29|pp.5–6;S011–012|Nonsignificant heterogeneity agrees with narrative|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S022 | Mismatch≥1.2/≥10mL yes/no |.96|pp.1,6,8,10;S013–014|Nonsignificant heterogeneity agrees with narrative|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S023 | Mismatch≥1.8/≥15mL yes/no |.92|pp.1,6,8,10;S015–016|Nonsignificant heterogeneity agrees with narrative|PASS_1_COMPLETE; PASS_2_COMPLETE|

## Table 2 paired within-arm associations

Exact source [Table2 p.7](../../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=7), W, paired EVT170/MM166, time90d. Individual estimates have no effect P; interactions are separate S032–039. All estimates contained by ordered endpoints. Ordinal aGenOR null1 and binary aRR null1. Binary event denominators: independence34/170 vs12/166; ambulation66/170 vs30/166; dependence/death77/170 vs101/166. These are outcome counts, not crude imaging-association denominators. Exclusion: comparison against crude treatment risk ratio would compare a different estimand.

| S ID | Outcome; covariate scale; measure | EVT estimate(95%CI) | MM estimate(95%CI) | Check record and matched locations | Pass status |
|---|---|---|---|---|---|
| S024 | mRS distribution;ASPECTS per1-point decrease;aGenOR|0.91(0.82–1.00)|0.89(0.80–0.99)|EVT interval includes1 while p.6 narrative says significantly worse; F-ST1-001. Abstract p.1 repeats estimate without significance qualifier. MM CI excludes1; no conflicting MM claim.|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S025 | mRS distribution;core per10mL;aGenOR|0.92(0.89–0.95)|0.95(0.92–0.98)|Both below1; significantly worse EVT narrative pp.1,6 reconciles|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S026 | mRS0–2;ASPECTS per1-point decrease;aRR|0.94(0.81–1.09)|0.81(0.57–1.14)|Both include1; no individual significant claim|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S027 | mRS0–2;core per10mL;aRR|0.89(0.84–0.95)|0.91(0.80–1.03)|EVT excludes1; decreased significantly narrative p.6 reconciles; MM includes1|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S028 | mRS0–3;ASPECTS per1-point decrease;aRR|1.00(0.90–1.12)|0.92(0.72–1.19)|Both include1; no individual significant claim|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S029 | mRS0–3;core per10mL;aRR|0.91(0.87–0.95)|0.91(0.85–0.98)|Both exclude1; significant decrease EVT p.6 reconciles. Interaction .25 separately assessed S037.|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S030 | mRS5–6;ASPECTS per1-point decrease;aRR|1.04(0.93–1.15)|1.03(0.95–1.11)|Both include1; no individual significant claim|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S031 | mRS5–6;core per10mL;aRR|1.05(1.02–1.08)|1.03(1.01–1.05)|Both exceed1; EVT significantly increased adverse outcome p.6 reconciles|PASS_1_COMPLETE; PASS_2_COMPLETE|

## Table 2 interaction tests

Source Table2 p.7; I, as-treated336. All P>.05; no heterogeneity conclusion contradicts these printed decisions. A shared interaction-model coefficient need not equal an arm-specific coefficient when nuisance covariates are fitted differently. Covariance/test/contrast definitions absent; no method is inferred from convention. Diagnostic approximations do not supply a reported SE.

| S ID | Paired estimates record; interaction | P | Check record | Pass status |
|---|---|---|---|---|
| S032 | S024;ASPECTS×treatment for ordinal |.83|No printed interaction estimate/SE; decision nonsignificant|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S033 | S025;core×treatment for ordinal |.20|No printed interaction estimate/SE; decision nonsignificant|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S034 | S026;ASPECTS×treatment for mRS0–2|.41|No printed interaction estimate/SE; decision nonsignificant|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S035 | S027;core×treatment for mRS0–2|.58|No printed interaction estimate/SE; decision nonsignificant|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S036 | S028;ASPECTS×treatment for mRS0–3|.73|No printed interaction estimate/SE; decision nonsignificant|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S037 | S029;core×treatment for mRS0–3|.25|Same displayed arm aRR0.91 gives distinct-model diagnostic concern; exact interaction-to-arm-coefficient identity not specified. Conditional observation excluded; not an established interval-versus-own-test contradiction.|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S038 | S030;ASPECTS×treatment for mRS5–6|.86|No printed interaction estimate/SE; decision nonsignificant|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S039 | S031;core×treatment for mRS5–6|.37|No printed interaction estimate/SE; decision nonsignificant|PASS_1_COMPLETE; PASS_2_COMPLETE|

## Table 3 mismatch presence versus absence, all printed effect estimates

Exact source [Table3 p.9](../../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=9), W; within-arm as-treated. No-mismatch reference. DefinitionA is ratio≥1.2 ANDvolume≥10mL: EVT no8/yes162, MM no21/yes145. DefinitionB is ratio≥1.8 ANDvolume≥15mL: EVT no59/yes111, MM no61/yes105. All estimates contained by ordered intervals; all CIs include their null (ratio1/difference0). None has a printed individual P or a narrative significant within-arm association claim. aRD link/standardization method not defined in main text; do not equate it to a crude difference. Multiple estimates in a row refer to the same population/contrast and are tracked together without losing any printed value.

| S ID | Definition;90d outcome | EVT effects(95%CI) | MM effects(95%CI) | Check record | Pass status |
|---|---|---|---|---|---|
| S040 | A;mRS distribution |aGenOR0.84(0.39–1.82)|aGenOR0.78(0.48–1.27)|Both include1; observed mRS medians4 vs4 and5 vs5 do not fix adjusted direction|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S041 | A;mRS0–2 |Not printed;0/8 vs34/162|aRR1.01(0.21–4.92);aRD−0.001(−0.138–0.136)|Ratio/difference have small opposite-signed point readings, but their mapping to common adjusted probabilities is unspecified; conditional observation excluded. Both include null.|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S042 | A;mRS0–3 |aRR1.04(0.26–4.21);aRD0.010(−0.344–0.364)|aRR0.49(0.22–1.05);aRD−0.139(−0.289–0.012)|Both RR/RD direction pairs agree; all include null|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S043 | A;mRS5–6 |aRR1.33(0.52–3.44);aRD0.178(−0.109–0.465)|aRR1.10(0.78–1.56);aRD0.075(−0.129–0.279)|RR/RD point directions agree; adjusted effects not equated to crude risk differences|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S044 | B;mRS distribution |aGenOR0.89(0.57–1.38)|aGenOR0.92(0.63–1.32)|Both include1; adjusted/model versus observed medians distinguished|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S045 | B;mRS0–2 |aRR1.20(0.44–3.28);aRD0.033(−0.124–0.191)|aRR1.09(0.26–4.57);aRD0.003(−0.097–0.103)|RR/RD direction agrees; all include null|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S046 | B;mRS0–3 |aRR1.03(0.56–1.88);aRD0.009(−0.164–0.181)|aRR0.87(0.39–1.92);aRD−0.032(−0.155–0.090)|RR/RD direction agrees; all include null|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S047 | B;mRS5–6 |aRR1.18(0.82–1.70);aRD0.092(−0.071–0.255)|aRR1.05(0.79–1.38);aRD0.037(−0.117–0.191)|RR/RD direction agrees; all include null; interaction separately S054|PASS_1_COMPLETE; PASS_2_COMPLETE|

## Table 3 interaction tests

I, as-treated336; exact Table3 p.9. P tests heterogeneity of mismatch association by treatment, not the null for any one aRR/aRD. All printed tests nonsignificant; effect P is blank for A independence (S041), so no unprinted interaction is invented.

| S ID | Paired effects; interaction | Printed P | Check record | Pass status |
|---|---|---|---|---|
| S048 | S040;A ordinal|.88|No interaction coefficient/variance supplied; nonsignificant decision|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S049 | S042;A ambulation|.47|No test specifies RR-scale versus RD-scale heterogeneity; no row-effect P conflict|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S050 | S043;A dependence/death|.65|No interaction coefficient/variance supplied; nonsignificant decision|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S051 | S044;B ordinal|.92|No interaction coefficient/variance supplied; nonsignificant decision|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S052 | S045;B independence|.75|No test specifies RR-scale versus RD-scale heterogeneity; nonsignificant decision|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S053 | S046;B ambulation|.60|No test specifies RR-scale versus RD-scale heterogeneity; nonsignificant decision|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S054 | S047;B dependence/death|>.99|An independent log-RR-difference diagnostic gives about .62, but interaction estimand/model mapping is not defined. Conditional observation excluded; no printed interaction interval exists to contradict.|PASS_1_COMPLETE; PASS_2_COMPLETE|

## Main narrative-only tests, predictions and method logic

| S ID | Exact source (REPORT) and quantitative relationship | Source-defined model/population/test; missing definitions | Check record | Pass status |
|---|---|---|---|---|
| S055 | p.4 baseline modality-volume/timing comparison: larger hypodensity727(422–1004)min versus larger CTP/MRI372(251–664)min;P<.001 |336 retained; descriptive medians/IQRs; specific timing comparison test not named |Longer time direction and significant P reconcile; IQR is not a CI and cannot imply test result|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S056 | p.8 time versus mismatchA presence/absence:P=.71 trend |336;trend test unnamed;A≥1.2/≥10 |No association wording agrees with P>.05; no estimate/SE supplied|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S057 | p.8 time versus mismatchB absence:P<.001 trend |336;trend test unnamed;B≥1.8/≥15 |Decreased no-mismatch with time/significance agrees; exact trend slope/statistic unreported|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S058 | p.8 core versus mismatchA absence:P<.001 trend |336;trend test unnamed |Increasing no-mismatch with core/significance agrees; no contrary estimate|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S059 | p.8 core versus mismatchB absence:P<.001 trend |336;trend test unnamed |Increasing no-mismatch with core/significance agrees; no contrary estimate|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S060 | p.6 additional core-adjusted ASPECTS:aGenOR0.96(0.86–1.07) perpoint decrease |EVT as-treated;PIM;age/NIHSS/time/core;95%CI;no numeric effect P |Contained,ordered,includes1; narrative not significant reconciles. Different model from S024,not duplicate.|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S061 | p.10 age:aRR0.97(0.96–0.99) peryear;ambulation |Within EVT;modified Poisson similar-model framework;exact figure covariate combination deferred to support shard;no numeric P |Contained/ordered/below1; significantly decreased agrees|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S062 | p.10 CTP-acquisition→reperfusion/endprocedure:aRR0.97(0.93–1.00) per10min;ambulation |Within EVT;modified Poisson similar-model framework;95%CI,two-sided.05;exact numeric P/SE absent |Contained/ordered; printed includes1 while significantly decreased stated; F-ST1-001|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S063 | p.10 last-known-well→reperfusion/endprocedure:aRR1.00(0.99–1.00);ambulation |Within EVT;modified Poisson;unit not stated for this printed estimate;numericP/SE absent |Contains1 and estimate on endpoint; no significant association wording reconciles; no unit preference inferred|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S064 | p.9 follow-up infarct EVT170(123–268)mL vsMM168(110–253)mL,P=.43 |Posthoc;follow-up-imaging cohort;test unnamed;medians/IQRs |Not significant agrees with P; overlapping IQRs not a test; exact rank/distribution inputs absent|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S065 | p.9 follow-up MR diffusion n204:infarct growth68(37–142)mL successful reperfusion vs95(56–125)MM vs125(76–179)unsuccessful |Posthoc MRI-follow-up subset;reperfusion observational subdivisions;no growth effectCI orP in main |Numerical smaller wording agrees; does not manufacture significant test; supplement rows separately mapped|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S066 | p.8 Figure3A/B/C probability curves:mRS0–2/0–3 decline,mRS5–6 increases with core0–300mL |D;as-treated/received-treatment curves;95%CI shading;exact pointwise table absent |Probability scale0–1,curves inside bands,direction agrees with S027/S029/S031;no curve values invented|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S067 | p.8 Figure3D generalized odds improvement versus core0–250mL,reference1 |D;EVT-versus-MM full-ordinal g-computation,bootstrap95%CI |Point curve favorsEVT,wide upper-core CI; separate from PIM stratum estimates;fullscale explicitly stated,no missing-step contradiction|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S068 | pp.3–4 primary endpoint/model:90dmRS,5/6 merged,PIM/ties equally split |O;individual randomized trial with31 centers,1:1minimization;primary PIM distinguished from ordinal logistic model |Ordinal outcome and pair-probability generalized odds definition coherent; ties/merging supplied; no preference for another model|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S069 | pp.2–4 population/design/attrition:352randomized→336retained;12imaging+4lost;ITT168/168;as-treated170/166 |Allocated treatment for comparative strata;received treatment for withinarm association;missing not imputed;no powerinputs in main |16exclusions and2crossovers reconcile;ITT-versus-as-treated explicitly distinguishes estimands. Main does not supply sample-size calculation inputs; PLAN scope separately assigned.|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S070 | p.4 significance/multiplicity/stopping:two-sidedP<.05,noadjustment;first300completed90d review;352randomizedatstop;efficacyboundarycrossed |Exploratory present analysis distinct from maintrial stopping;numeric efficacyboundary not printed main |No numeric rule violation demonstrable from main; PLAN decision rules assigned separately. NoNI/equivalence claims/margins in main.|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S071 | pp.4,6,11 sensitivity/posthoc methods:siteASPECTS,MRIexcluded,composite/hypodensity,AIC/BIC/AUC,infarctgrowth;someposthoc,broadplanprespecified |Source states analyses/adjustment;individual summary metrics in support;no preferred model inferred |Descriptions differentiate supplied analyses rather than contradict a printed main result; PLAN-to-report status comparisons separately assigned|PASS_1_COMPLETE; PASS_2_COMPLETE|
| S072 | p.8 mismatch marginal probabilities increase forEVT/decreaseMM;discordance notassociatedwithheterogeneity |Withinarm predictedmargins versus ITT treatment interactions explicitly separate;exact slopes/interactionP absentmain |Narrative direction preserved without equating to Table3 categorical adjusted presence coefficients or crude proportions;support comparisons separately assigned|PASS_1_COMPLETE; PASS_2_COMPLETE|

## Pass-1 totals and limits

72 stable relationships S001–S072; 1 consolidated finding F-ST1-001; 6 excluded apparent observations. Every estimate/CI has containment/order checked and every significance/interaction statement has the appropriate null/test role distinguished. No printed SE or test statistic occurs in the main scientific results. Methods do not name all interaction contrasts, covariance estimators beyond robust Poisson standard errors, or trend tests; missing definitions limit exact reproduction, without creating a finding by absence alone. No independent sample-size reproduction can be made from the main report alone. This is completed main statistical coverage, not completed package-wide coverage; supporting results and plans are disjoint mandatory shards.

Fresh derivative provenance: `pdftoppm -f 10 -l 10 -singlefile -scale-to 2000 -png jama_sarraj_2024_oi_240006_1708623114.96234.pdf .ai_paper_validation/review_1_6_2/preprocessing/stat1_main/page-10`; Poppler26.01.0,CPU; output preprocessing/stat1_main/page-10.png. Direct source authority confirmed the significant imaging-time phrase and printed upperCI1.00. Reused p.6 image supplies exact ASPECTS wording. No Python, OCR, network or old candidate/report inputs used.

## Independent pass 2 — root/stat2_main

Fresh gpt-6.1-sol/high statistical reviewer independently completed every S001–S072 after reading the full18-ID ledger, independent recheck and all31 screening decisions. Pass1 content is preserved. The per-record status above now records both passes; this appended table documents independent pass2 reasoning. Complete 75-row excluded-observation reconsideration and empirical diagnostic checks are in checkers/statistical_parts/pass2_main.md. No new main-shard finding ID; qualifying final-decision-rule reconsideration is referred to the plan-method shard F-ST2-601 for independent screening.

| S ID | Pass 2 status | Independent pass 2 reasoning |
|---|---|---|
| S001 | PASS_2_COMPLETE | ASPECTS0–2 ordinal1.52(.94–2.46) contained and positive;null1 included, no own effectP/significance. Binary all-zeroC004 is a distinct measure. |
| S002 | PASS_2_COMPLETE | ASPECTS3–5 ordinal1.82(1.40–2.35) contains point/excludes1;matching significant narrative and277partition reconcile. |
| S003 | PASS_2_COMPLETE | ASPECTS6–10 ordinal1.55(.81–2.98) ordered/includes1; no unsupported subgroup-significance claim. |
| S004 | PASS_2_COMPLETE | ASPECTS3 ordinal1.71(1.04–2.81) matches abstract andbody; excludes1, n73 consistent. |
| S005 | PASS_2_COMPLETE | ASPECTS4 ordinal2.01(1.19–3.40) matches abstract andbody; excludes1, n88 consistent. |
| S006 | PASS_2_COMPLETE | ASPECTS5 ordinal1.85(1.22–2.79) matches abstract andbody; excludes1, n116 consistent. |
| S007 | PASS_2_COMPLETE | Core<70 ordinal1.78(1.24–2.56),n156;estimate/CI/direction agree. Coredefinition/statusC003 separately retained. |
| S008 | PASS_2_COMPLETE | Core≥70 ordinal1.63(1.23–2.16),n180;abstract/body direction agree, ordered. |
| S009 | PASS_2_COMPLETE | Core<100 ordinal1.91(1.44–2.55),n236;estimate contained and favorsEVT. |
| S010 | PASS_2_COMPLETE | Core≥100 ordinal1.41(.99–2.02) contains1;discussion emphasizes pointdirection/uncertainty. DistributionC006 retained rather than treated as sameeffectCI. |
| S011 | PASS_2_COMPLETE | Core<150 ordinal1.82(1.42–2.34),n296;contained/order/direction reconcile. |
| S012 | PASS_2_COMPLETE | Core≥150 ordinal1.47(.84–2.56),n40;wideCI explicitly acknowledged; pointbenefit does not claim significance. |
| S013 | PASS_2_COMPLETE | NoA mismatchordinal2.11(.97–4.58),n29;includes1, uncertainty acknowledged. C016 is different planned50/100mL stratification. |
| S014 | PASS_2_COMPLETE | YesA mismatchordinal1.75(1.38–2.24),n307;ordered/excludes1.29+307=336. |
| S015 | PASS_2_COMPLETE | NoB mismatchordinal1.68(1.17–2.40),n120;ordered/excludes1; no equating binary crudeassociation. |
| S016 | PASS_2_COMPLETE | YesB mismatchordinal1.79(1.33–2.42),n216;ordered/excludes1;120+216=336. |
| S017 | PASS_2_COMPLETE | ASPECTS category interaction.80>.05;no individualeffectP substituted;modelcontrast/covariance missing. |
| S018 | PASS_2_COMPLETE | ASPECTS3/4/5 interaction.80>.05 matches narrative;three-category test not inferred from pairwiseCIs. |
| S019 | PASS_2_COMPLETE | Core70 interaction.92>.05 matches noheterogeneity;its own interaction estimate/SE absent. |
| S020 | PASS_2_COMPLETE | Core100 interaction.29>.05 agrees with noheterogeneity despite differing point estimates. |
| S021 | PASS_2_COMPLETE | Core150 interaction.29>.05 agrees with noheterogeneity;wide stratumCI not an interactionvariance. |
| S022 | PASS_2_COMPLETE | MismatchA interaction.96>.05 agrees with noheterogeneity;no-mismatchCI includes1 without conflict. |
| S023 | PASS_2_COMPLETE | MismatchB interaction.92>.05 agrees with noheterogeneity;bothstratum treatmenteffects significant can coexist. |
| S024 | PASS_2_COMPLETE | EVTASPECTS.91(.82–1.00) versus significant narrative remains C005;MM.89(.80–.99) has compatible nullreading. |
| S025 | PASS_2_COMPLETE | CoreordinalEVT.92(.89–.95)/MM.95(.92–.98) both below1;reported EVT significant worsening agrees. |
| S026 | PASS_2_COMPLETE | ASPECTSindependence.94(.81–1.09)/.81(.57–1.14) include1; no own significant narrative. Crude treatmentRR would differ in estimand. |
| S027 | PASS_2_COMPLETE | Coreindependence.89(.84–.95)/.91(.80–1.03):EVT significant decline agrees, MM no significance manufactured. |
| S028 | PASS_2_COMPLETE | ASPECTSambulation1.00(.90–1.12)/.92(.72–1.19) include1;no own significantclaim. |
| S029 | PASS_2_COMPLETE | Coreambulationboth.91 withCI.87–.95/.85–.98:bothwithinarm negative associations agree;interaction.25 separately boundeddiagnostic. |
| S030 | PASS_2_COMPLETE | ASPECTSadverse1.04(.93–1.15)/1.03(.95–1.11) include1;not interpreted as favorable outcomes. |
| S031 | PASS_2_COMPLETE | Coreadverse1.05(1.02–1.08)/1.03(1.01–1.05) >1;mainincreased adverse narrative agrees. |
| S032 | PASS_2_COMPLETE | OrdinalASPECTS interaction.83 not theP forEVT.91;C005 retains narrative interval conflict without misusing thisP. |
| S033 | PASS_2_COMPLETE | Ordinalcore interaction.20>.05;diagnostic differenceP.166 not source-stated test; no contradictory interactionCI printed. |
| S034 | PASS_2_COMPLETE | IndependenceASPECTSinteraction.41>.05;independentslope diagnostic.439 cannot identify actualmodel. |
| S035 | PASS_2_COMPLETE | Independencecoreinteraction.58>.05;independentslope diagnostic.757 does not reproduce samefit. |
| S036 | PASS_2_COMPLETE | AmbulationASPECTSinteraction.73>.05;diagnostic.551 differs butcommon-nuisance mapping unstated. |
| S037 | PASS_2_COMPLETE | Ambulationcoreinteraction.25:diagnosticP≈1,precisionlowerbound≈.777;fullsame-display reconstruction fails otherrows so conditional observation retained. |
| S038 | PASS_2_COMPLETE | AdverseASPECTSinteraction.86>.05;diagnostic.886 close numerically butdoesnotcalibrate a generalinteractionmethod. |
| S039 | PASS_2_COMPLETE | Adversecoreinteraction.37>.05;diagnostic.275 further demonstrates lack ofreproducing independent-slope procedure. |
| S040 | PASS_2_COMPLETE | AordinalEVT.84(.39–1.82)/MM.78(.48–1.27) contained/order/bothnull;categorical association distinctfromcontinuousC007. |
| S041 | PASS_2_COMPLETE | AindependenceEVT0/8 hasblank effect;MMRR1.01(.21–4.92),RD−.001(−.138,.136) bothnull;sharedRR/RD risk mappingnotdefined. |
| S042 | PASS_2_COMPLETE | AambulationRR/RD signsagree ineacharm,allCIscontainnull;no ownP. Doesnotreconstruct adjusted slopes fromcounts. |
| S043 | PASS_2_COMPLETE | AadverseRR1.33/1.10 andRD.178/.075 signsagree;ordered intervals containnull. |
| S044 | PASS_2_COMPLETE | Bordinal.89(.57–1.38)/.92(.63–1.32) containnull;observedmedians not a modelcoefficient identity. |
| S045 | PASS_2_COMPLETE | BindependenceRR1.20/1.09,RD.033/.003 signsagree;allnull-containing andpoint-contained. |
| S046 | PASS_2_COMPLETE | BambulationRR1.03/.87,RD.009/−.032 signsagree;CIsordered andnull-containing. |
| S047 | PASS_2_COMPLETE | BadverseRR1.18/1.05,RD.092/.037 signsagree;allCIsnull-containing. LastP>.99 concernsanothercontrast. |
| S048 | PASS_2_COMPLETE | Aordinalinteraction.88>.05;diagnostic.873 near butdoesnotvalidate binaryPoisson interactions. |
| S049 | PASS_2_COMPLETE | Aambulationinteraction.47>.05;RRdiagnostic.356, RDcontrast unspecified;no same-effect testCI conflict. |
| S050 | PASS_2_COMPLETE | Aadverseinteraction.65>.05;RRdiagnostic.712, common coefficient/covariance missing. |
| S051 | PASS_2_COMPLETE | Bordinalinteraction.92>.05;PIM diagnostic.910 near, separatefrombinarymodels. |
| S052 | PASS_2_COMPLETE | Bindependenceinteraction.75>.05;RRdiagnostic.914 doesnotreproduce sourceinteraction. |
| S053 | PASS_2_COMPLETE | Bambulationinteraction.60>.05;RRdiagnostic.741 doesnotreproduce sourceinteraction. |
| S054 | PASS_2_COMPLETE | Badverseinteraction>.99 versusdiagnostic.618;no printed interactionCI andno binarysame-display method reconstruction. Retain conditional exclusion. |
| S055 | PASS_2_COMPLETE | Timingcomparison727 versus372 min,P<.001 hascoherentdirection;IQRsnotCI,exact ranks/testunnamed. |
| S056 | PASS_2_COMPLETE | MismatchA time trend.71 supports nonsignificant association;coefficient/test/binN missing without printedcontradiction. |
| S057 | PASS_2_COMPLETE | MismatchB time trend<.001 matches decreasing absencewithtime;no fittedslopeSE assumed. |
| S058 | PASS_2_COMPLETE | MismatchA core trend<.001 matches increasingabsencewithcore;barpercentagesnot precise trendtestinputs. |
| S059 | PASS_2_COMPLETE | MismatchB core trend<.001 matches increasingabsencewithcore;rounding101% doesnot changeinferentialrole. |
| S060 | PASS_2_COMPLETE | Core-adjustedASPECTS.96(.86–1.07) contained/null-inclusive andnot significant asstated;fullyplannedadjustment counterpartpresent. |
| S061 | PASS_2_COMPLETE | AgeRR.97(.96–.99) peryear below1 supports significantambulationdecrease;coreidentityC008 andpredictorC009 retained. |
| S062 | PASS_2_COMPLETE | Imaging-timeRR.97(.93–1.00) significantdecline remains C005 category1;unroundedupperlimit/testmapping not invented. |
| S063 | PASS_2_COMPLETE | LKW→reperfusionRR1.00(.99–1.00) atnullsupports no significantassociation;C009 distinguishes plannedrandomizationtime. |
| S064 | PASS_2_COMPLETE | InfarctmediancomparisonP.43 nonsignificant coherent;IQR170(123–268) versus168(110–253) not inferentialCIs. |
| S065 | PASS_2_COMPLETE | MRgrowthmedians68/95/125 numericalordering coherent;C001 retains analysispopulation8/204 discrepancy;IQRcopiesperipheral nottreatmentCIs. |
| S066 | PASS_2_COMPLETE | Figure3A/Bprobabilitiesdescendwithcore,Cascends;centralcurvesinsidebands. Distinctpredictor frommismatchC007. |
| S067 | PASS_2_COMPLETE | Figure3D fullordinalg-computation pointcurvefavorsEVT,upper-coreCIwide;source explicitly fullscale so separatefromprimarymergedPIM. |
| S068 | PASS_2_COMPLETE | PrimaryPIMties/merged5–6 sourcecoherent;C002 allocation andC003 definitionstatus retained. No alternativeanalysis recommended. |
| S069 | PASS_2_COMPLETE | 352−12−4=336;168/168→170/166via2crossovers;missingnotimputedgoverningimagingSAP. C002 populationrulecomparison retained. |
| S070 | PASS_2_COMPLETE | Two-sided.05/exploratorynomultiplicityexplicit;noNI/equivalencemargin.300stopreport corroboratesC014 butdoesnot supplyobservedZ/boundarymapping. |
| S071 | PASS_2_COMPLETE | Reportedposthoccomposite sensitivitycontrastsplannedprimary/prespecified=C003;core-adjustedASPECTS supplied;modelcomparisons namedseparately. |
| S072 | PASS_2_COMPLETE | ContinuousEVT mismatchprobabilitynarrativeincreases butsourceeFigure17curvesdecrease=C007. Categoricalpresence/crudeoutcomes do notresolve thatdirection. |

