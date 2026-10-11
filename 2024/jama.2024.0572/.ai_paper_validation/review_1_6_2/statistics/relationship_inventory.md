# Statistical relationship inventory — main REPORT pass 1

Runtime agent: `/root/stat1_main`; model `gpt-6.1-sol`; effort `high`; fresh PASS 1 only. Assigned scope is DOC-001 main REPORT, physical PDF pp.1–14, including every printed inferential estimate, interval, interaction P, narrative test and statistical-method statement. Supporting REPORT rows and PLAN logic belong to other disjoint shards. Source: [main REPORT](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=1). Mapping input: extraction/main_quantitative_evidence.md M001–M120 and complete source-matched locator appendix. Direct Poppler pdftotext checks pp.1,6–10; reusable source-matched layout supplies remaining main methods. Reused p.6 image and fresh direct p.10 rendering visually confirmed the finding. All 14 main pages mapped; pp.13–14 contain no additional inferential analysis. Duplicate abstract/narrative/table appearances are matched within a record.

## Common source-defined analysis contracts

- **O (ordinal treatment):** 90-day mRS distribution, primary scores 5/6 merged; adjusted probabilistic index model (PIM), ties split equally; ITT allocated EVT vs MM, total336 (168/168). Figure1 adjusts age, NIHSS, time last-known-well to randomization, core volume; core omitted within core-volume strata. aGenOR>1 favors EVT. CI95%; all report hypothesis tests two-sided, significance P<.05, exploratory with no multiplicity adjustment. No row-effect P, test statistic, SE, covariance, or PIM test distribution is printed. Exact row-level P cannot be reconstructed without those definitions; containment/order/direction and the printed significance claims can be checked.
- **W (within-arm imaging):** as-treated EVT170/MM166 (2 crossovers), 90-day mRS; PIM aGenOR for ordinal distribution; modified Poisson regression with robust standard errors for binary outcomes. Table2 adjusts age, NIHSS, time; ASPECTS per1-point decrease, CTP/MRI core per10mL increase. Table3 additionally adjusts core and contrasts presence of mismatch with no-mismatch reference within each received-treatment arm. >1 means better ordinal outcome or greater binary-outcome risk/rate, respectively. CI95%, two-sided .05. Printed 'absolute risk reduction' expansion of aRR coexists with an explicit rate-ratio footnote and positive ratio scale; identity issue self-screened separately. No individual-effect P, SE or variance matrix supplied.
- **I (interaction):** treatment×characteristic term, categorical and continuous imaging examined separately where possible (p.4). Printed P values are heterogeneity tests, not row-effect P values. Exact fitted common versus arm-specific nuisance coefficients, contrast, degrees of freedom, covariance and test statistic are not supplied. A difference-of-independent-log-estimates diagnostic is not the stated interaction test and does not establish a contradiction by itself.
- **D (predictions):** g-computation full ordinal scale and bootstrapped confidence intervals, predicted margins/marginal probabilities. Curves are modeled, rather than raw proportions; no exact pointwise numerical table is printed. Full ordinal scale explicitly differs from primary merged5/6 analysis.

Every record below has explicit PASS_1_COMPLETE status. Checks that reconcile remain in these records; only apparent observations self-screened out are in the checker Excluded observations table. No evidence state or human disposition is assigned here.

## Figure 1 ordinal rows: all estimates, populations and matched occurrences

All rows use O; exact source [Figure1 p.6](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6). Each printed estimate lies within ordered positive endpoints and agrees with favors-EVT labeling; CI null-membership is shown. Mappings identify all duplicate locations. Medians/IQRs are descriptive, rather than intervals for the treatment effect.

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

Exact source [Table2 p.7](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=7), W, paired EVT170/MM166, time90d. Individual estimates have no effect P; interactions are separate S032–039. All estimates contained by ordered endpoints. Ordinal aGenOR null1 and binary aRR null1. Binary event denominators: independence34/170 vs12/166; ambulation66/170 vs30/166; dependence/death77/170 vs101/166. These are outcome counts, not crude imaging-association denominators. Exclusion: comparison against crude treatment risk ratio would compare a different estimand.

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

Exact source [Table3 p.9](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=9), W; within-arm as-treated. No-mismatch reference. DefinitionA is ratio≥1.2 ANDvolume≥10mL: EVT no8/yes162, MM no21/yes145. DefinitionB is ratio≥1.8 ANDvolume≥15mL: EVT no59/yes111, MM no61/yes105. All estimates contained by ordered intervals; all CIs include their null (ratio1/difference0). None has a printed individual P or a narrative significant within-arm association claim. aRD link/standardization method not defined in main text; do not equate it to a crude difference. Multiple estimates in a row refer to the same population/contrast and are tracked together without losing any printed value.

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

# Statistical relationship inventory part: forest A, passes 1 and 2

Runtime agent: /root/stat1_forest_a (manifest normalized identity root/stat1_forest_a). Model gpt-6.1-sol; effort high; fresh spawn. Exact assigned scope: DOC-006 physical PDF pp.13-15, eFigures7-9, mapper A028-A030. Context only: DOC-001 p4 statistical methods and DOC-005 pp4-6 secondary-analysis methods. No other forest or design relationship is independently rechecked here.

69 stable records: 48 outcome rows (45 printed finite RR/95%CI and3 asterisks), 18 printed treatment-interaction tests and3 unprinted interaction slots. Every record is PASS_1_COMPLETE and PASS_2_COMPLETE. Independent fresh pass-2 runtime root/stat2_forest_a (gpt-6.1-sol/high) reread every relationship using the complete ledger, screening handoff and mechanical recheck. Explicit per-S reasoning is in checkers/statistical_parts/pass2_forest_a.md; pass 2 adds zero findings and retains two excluded-observation patterns. IDs S1001-S1069. One finding F-ST1-101, two excluded-observation patterns. No finding count was targeted. Physical pages13/14/15 carry printed folios12/13/14.

## Sources, rules and precise limitations

DOC-006 is REPORT. Source links: [eFigure7](../../../joi240006supp5_prod_1708623115.01733.pdf#page=13), [eFigure8](../../../joi240006supp5_prod_1708623115.01733.pdf#page=14), [eFigure9](../../../joi240006supp5_prod_1708623115.01733.pdf#page=15). Every row is an EVT/MM between-randomized-treatment comparison at90days, using core-lab ASPECTS or CTP/MRI core/mismatch strata. Total subgroup n is not an arm denominator. Arm denominators in the table are source-matched from mapped distribution displays and reconcile with the printed counts/percentages; they are not additional inferential relationships.

Method R: REPORT [DOC-001 p4](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4) states secondary treatment effects within individual subgroups use modified Poisson regression with robust standard errors; treatment effects across imaging strata use randomized assignment. The forest prints relative risk and95%CI. PLAN [DOC-005 pp4-5](../../../joi240006supp4_prod_1708623115.00733.pdf#page=4) prescribes modified Poisson models with robust standard errors, prognostic adjustment age, presentation NIHSS, last-known-well to randomization and core volume, omitting the subgroup-defining prognostic covariate. The plan's logistic fallback is for marginal probability plots; it does not identify a replacement estimator for these forest RRs. Exact fitted binary covariate implementation, individual coefficient standard errors, robust covariance matrices and individual effect P values are not supplied on the forest pages. These omissions alone are not findings.

R-positive: RR>1 for mRS0-2/0-3 points to the printed rightward favors-EVT side. R-adverse: RR<1 for mRS5-6 points to the printed leftward favors-EVT side. The null is RR1; all45 finite CIs are correctly ordered and contain the point estimate. Counts/percentages reconcile within0.005 percentage-point rounding intervals. No adverse direction statement or inferential-decision claim contradicts the plotted reading. Printed CI limits at1.00 are retained, without imposing an unprinted effect-test decision.

Method I: REPORT DOC-001 p4 states treatment×characteristic interaction tests, separately by categorical imaging strata and continuous imaging where possible, two-sided tests, significance P<.05, exploratory with no multiplicity adjustment. PLAN [DOC-005 pp5-6](../../../joi240006supp4_prod_1708623115.00733.pdf#page=5) specifies these threshold/ASPECTS/mismatch interaction analyses. The forest labels the P column “Interaction p-value.” These are not individual treatment-effect P values. None of the18 printed interaction Ps is below.05. Exact interaction statistic, degrees of freedom, covariance, row-to-model fit mapping and, for the zero-event ASPECTS stratum, how estimability was handled are not supplied. No test equality is inferred from overlapping/nonoverlapping subgroup CIs; no test statistic or degrees of freedom is imputed. Missing slots are preserved as missing definitions, not synthesized tests. No subgroup-specific noninferiority/equivalence margin, interim/stopping decision or multiplicity-adjusted claim is printed; trial-design decisions are outside this disjoint shard.

Comparison against crude risks is diagnostic only and cannot reproduce adjusted RRs without individual covariates. No conventional variance formula is substituted for the stated robust model. Display precision is applied to arithmetic comparisons, but not to point-estimate containment or interval/test conflicts.

Provenance: mapper results_a.md as factual locator; reusable DOC-006 page_images/page-013.png, page-014.png and page-015.png inspected in full. For finding locations, exact supplied PDF pp13-14 were freshly rendered with Poppler26.01.0 pdftoppm, CPU, and visually read: command pattern pdftoppm -f N -l N -singlefile -scale-to 2200 -png joi240006supp5_prod_1708623115.01733.pdf .ai_paper_validation/review_1_6_2/preprocessing/stat1_forest_a/direct-pN. Derivatives direct-p13.png/direct-p14.png, engine Poppler26.01.0, CPU. Direct pdftotext -layout reads DOC-001 pp3-4 and DOC-005 pp3-6 to stdout; no text derivative created. Sources and all reusable assets preserved.

## Individual outcome relationships

Each finite record applies containment, endpoint-order, direction, source-matched count/denominator and method-attribution checks. “ordered/contained” does not imply that a model lacking its covariates or covariance was numerically reconstructed. Missing R means individual effect P/test statistic/standard error/robust covariance/fitted binary covariate implementation unavailable; missing Z adds the zero-event estimation and CI procedure; missing A means asterisk not accompanied by an estimate, uncertainty or estimation explanation. Reconciled records are not excluded observations.

| S ID | Mapping key and exact location | Roles | Matched result key | EVT count (%) / arm n | MM count (%) / arm n | Printed RR (95%CI) | Rule/result and named missing definitions | Pass 1 | Pass 2 |
|---|---|---|---|---|---|---|---|---|---|---|
| S1001 | A028.row1; DOC-006 p13/eFigure7 | REPORT; method context REPORT/PLAN | 90-day mRS0-2; ASPECTS 0-2; total n19; EVT/MM | 0 (0.00) / 11 | 0 (0.00) / 8 | 1.00 (0.37-2.72) | R-positive; ordered/contained; null included; F-ST1-101; zero-event model gap; missing R,Z | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1002 | A028.row2; DOC-006 p13/eFigure7 | REPORT; method context REPORT/PLAN | 90-day mRS0-2; ASPECTS 3-5; total n277; EVT/MM | 31 (22.30) / 139 | 10 (7.25) / 138 | 3.20 (1.67-6.14) | R-positive; ordered/contained; null excluded; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1003 | A028.row3; DOC-006 p13/eFigure7 | REPORT; method context REPORT/PLAN | 90-day mRS0-2; ASPECTS 6-10; total n40; EVT/MM | 3 (16.67) / 18 | 2 (9.09) / 22 | 3.22 (0.84-12.35) | R-positive; ordered/contained; null included; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1004 | A028.row4; DOC-006 p13/eFigure7 | REPORT; method context REPORT/PLAN | 90-day mRS0-2; ASPECTS 3; total n73; EVT/MM | 7 (15.56) / 45 | 2 (7.14) / 28 | 2.49 (0.60-10.23) | R-positive; ordered/contained; null included; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1005 | A028.row5; DOC-006 p13/eFigure7 | REPORT; method context REPORT/PLAN | 90-day mRS0-2; ASPECTS 4; total n88; EVT/MM | 7 (22.58) / 31 | 3 (5.26) / 57 | 3.52 (1.06-11.62) | R-positive; ordered/contained; null excluded; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1006 | A028.row6; DOC-006 p13/eFigure7 | REPORT; method context REPORT/PLAN | 90-day mRS0-2; ASPECTS 5; total n116; EVT/MM | 17 (26.98) / 63 | 5 (9.43) / 53 | 2.93 (1.20-7.17) | R-positive; ordered/contained; null excluded; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1007 | A028.row7; DOC-006 p13/eFigure7 | REPORT; method context REPORT/PLAN | 90-day mRS0-2; CTP/MRI core <70 mL; total n156; EVT/MM | 23 (28.05) / 82 | 9 (12.16) / 74 | 2.36 (1.20-4.61) | R-positive; ordered/contained; null excluded; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1008 | A028.row8; DOC-006 p13/eFigure7 | REPORT; method context REPORT/PLAN | 90-day mRS0-2; CTP/MRI core ≥70 mL; total n180; EVT/MM | 11 (12.79) / 86 | 3 (3.19) / 94 | 4.19 (1.27-13.89) | R-positive; ordered/contained; null excluded; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1009 | A028.row9; DOC-006 p13/eFigure7 | REPORT; method context REPORT/PLAN | 90-day mRS0-2; CTP/MRI core <100 mL; total n236; EVT/MM | 30 (25.64) / 117 | 11 (9.24) / 119 | 2.81 (1.53-5.17) | R-positive; ordered/contained; null excluded; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1010 | A028.row10; DOC-006 p13/eFigure7 | REPORT; method context REPORT/PLAN | 90-day mRS0-2; CTP/MRI core ≥100 mL; total n100; EVT/MM | 4 (7.84) / 51 | 1 (2.04) / 49 | 3.39 (0.52-22.13) | R-positive; ordered/contained; null included; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1011 | A028.row11; DOC-006 p13/eFigure7 | REPORT; method context REPORT/PLAN | 90-day mRS0-2; CTP/MRI core <150 mL; total n296; EVT/MM | 33 (22.45) / 147 | 12 (8.05) / 149 | 3.03 (1.68-5.47) | R-positive; ordered/contained; null excluded; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1012 | A028.row12; DOC-006 p13/eFigure7 | REPORT; method context REPORT/PLAN | 90-day mRS0-2; CTP/MRI core ≥150 mL; total n40; EVT/MM | 1 (4.76) / 21 | 0 (0.00) / 19 | * | R-positive; no finite effect printed; no containment/endpoint arithmetic available; missing A | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1013 | A028.row13; DOC-006 p13/eFigure7 | REPORT; method context REPORT/PLAN | 90-day mRS0-2; CTP/MRI mismatch ≥1.2 and ≥10 mL: No; total n29; EVT/MM | 0 (0.00) / 8 | 1 (4.76) / 21 | * | R-positive; no finite effect printed; no containment/endpoint arithmetic available; missing A | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1014 | A028.row14; DOC-006 p13/eFigure7 | REPORT; method context REPORT/PLAN | 90-day mRS0-2; CTP/MRI mismatch ≥1.2 and ≥10 mL: Yes; total n307; EVT/MM | 34 (21.25) / 160 | 11 (7.48) / 147 | 3.10 (1.68-5.70) | R-positive; ordered/contained; null excluded; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1015 | A028.row15; DOC-006 p13/eFigure7 | REPORT; method context REPORT/PLAN | 90-day mRS0-2; CTP/MRI mismatch ≥1.8 and ≥15 mL: No; total n120; EVT/MM | 6 (10.34) / 58 | 2 (3.23) / 62 | 3.54 (0.72-17.41) | R-positive; ordered/contained; null included; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1016 | A028.row16; DOC-006 p13/eFigure7 | REPORT; method context REPORT/PLAN | 90-day mRS0-2; CTP/MRI mismatch ≥1.8 and ≥15 mL: Yes; total n216; EVT/MM | 28 (25.45) / 110 | 10 (9.43) / 106 | 2.84 (1.50-5.38) | R-positive; ordered/contained; null excluded; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1017 | A029.row1; DOC-006 p14/eFigure8 | REPORT; method context REPORT/PLAN | 90-day mRS0-3; ASPECTS 0-2; total n19; EVT/MM | 0 (0.00) / 11 | 0 (0.00) / 8 | 1.00 (0.37-2.72) | R-positive; ordered/contained; null included; F-ST1-101; zero-event model gap; missing R,Z | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1018 | A029.row2; DOC-006 p14/eFigure8 | REPORT; method context REPORT/PLAN | 90-day mRS0-3; ASPECTS 3-5; total n277; EVT/MM | 59 (42.45) / 139 | 27 (19.57) / 138 | 2.22 (1.55-3.16) | R-positive; ordered/contained; null excluded; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1019 | A029.row3; DOC-006 p14/eFigure8 | REPORT; method context REPORT/PLAN | 90-day mRS0-3; ASPECTS 6-10; total n40; EVT/MM | 6 (33.33) / 18 | 4 (18.18) / 22 | 2.61 (1.00-6.84) | R-positive; ordered/contained; printed null boundary; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1020 | A029.row4; DOC-006 p14/eFigure8 | REPORT; method context REPORT/PLAN | 90-day mRS0-3; ASPECTS 3; total n73; EVT/MM | 12 (26.67) / 45 | 5 (17.86) / 28 | 1.75 (0.74-4.11) | R-positive; ordered/contained; null included; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1021 | A029.row5; DOC-006 p14/eFigure8 | REPORT; method context REPORT/PLAN | 90-day mRS0-3; ASPECTS 4; total n88; EVT/MM | 15 (48.39) / 31 | 8 (14.04) / 57 | 3.18 (1.61-6.28) | R-positive; ordered/contained; null excluded; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1022 | A029.row6; DOC-006 p14/eFigure8 | REPORT; method context REPORT/PLAN | 90-day mRS0-3; ASPECTS 5; total n116; EVT/MM | 32 (50.79) / 63 | 14 (26.42) / 53 | 1.97 (1.23-3.18) | R-positive; ordered/contained; null excluded; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1023 | A029.row7; DOC-006 p14/eFigure8 | REPORT; method context REPORT/PLAN | 90-day mRS0-3; CTP/MRI core <70 mL; total n156; EVT/MM | 44 (53.66) / 82 | 23 (31.08) / 74 | 1.79 (1.26-2.54) | R-positive; ordered/contained; null excluded; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1024 | A029.row8; DOC-006 p14/eFigure8 | REPORT; method context REPORT/PLAN | 90-day mRS0-3; CTP/MRI core ≥70 mL; total n180; EVT/MM | 21 (24.42) / 86 | 8 (8.51) / 94 | 3.10 (1.49-6.43) | R-positive; ordered/contained; null excluded; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1025 | A029.row9; DOC-006 p14/eFigure8 | REPORT; method context REPORT/PLAN | 90-day mRS0-3; CTP/MRI core <100 mL; total n236; EVT/MM | 56 (47.86) / 117 | 28 (23.53) / 119 | 2.10 (1.49-2.95) | R-positive; ordered/contained; null excluded; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1026 | A029.row10; DOC-006 p14/eFigure8 | REPORT; method context REPORT/PLAN | 90-day mRS0-3; CTP/MRI core ≥100 mL; total n100; EVT/MM | 9 (17.65) / 51 | 3 (6.12) / 49 | 3.16 (0.99-10.10) | R-positive; ordered/contained; null included; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1027 | A029.row11; DOC-006 p14/eFigure8 | REPORT; method context REPORT/PLAN | 90-day mRS0-3; CTP/MRI core <150 mL; total n296; EVT/MM | 62 (42.18) / 147 | 31 (20.81) / 149 | 2.17 (1.56-3.02) | R-positive; ordered/contained; null excluded; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1028 | A029.row12; DOC-006 p14/eFigure8 | REPORT; method context REPORT/PLAN | 90-day mRS0-3; CTP/MRI core ≥150 mL; total n40; EVT/MM | 3 (14.29) / 21 | 0 (0.00) / 19 | * | R-positive; no finite effect printed; no containment/endpoint arithmetic available; missing A | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1029 | A029.row13; DOC-006 p14/eFigure8 | REPORT; method context REPORT/PLAN | 90-day mRS0-3; CTP/MRI mismatch ≥1.2 and ≥10 mL: No; total n29; EVT/MM | 2 (25.00) / 8 | 4 (19.05) / 21 | 5.99 (0.76-47.33) | R-positive; ordered/contained; null included; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1030 | A029.row14; DOC-006 p14/eFigure8 | REPORT; method context REPORT/PLAN | 90-day mRS0-3; CTP/MRI mismatch ≥1.2 and ≥10 mL: Yes; total n307; EVT/MM | 63 (39.38) / 160 | 27 (18.37) / 147 | 2.32 (1.66-3.25) | R-positive; ordered/contained; null excluded; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1031 | A029.row15; DOC-006 p14/eFigure8 | REPORT; method context REPORT/PLAN | 90-day mRS0-3; CTP/MRI mismatch ≥1.8 and ≥15 mL: No; total n120; EVT/MM | 14 (24.14) / 58 | 6 (9.68) / 62 | 2.77 (1.17-6.53) | R-positive; ordered/contained; null excluded; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1032 | A029.row16; DOC-006 p14/eFigure8 | REPORT; method context REPORT/PLAN | 90-day mRS0-3; CTP/MRI mismatch ≥1.8 and ≥15 mL: Yes; total n216; EVT/MM | 51 (46.36) / 110 | 25 (23.58) / 106 | 2.08 (1.48-2.93) | R-positive; ordered/contained; null excluded; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1033 | A030.row1; DOC-006 p15/eFigure9 | REPORT; method context REPORT/PLAN | 90-day mRS5-6; ASPECTS 0-2; total n19; EVT/MM | 9 (81.82) / 11 | 8 (100.00) / 8 | 0.80 (0.60-1.07) | R-adverse; ordered/contained; null included; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1034 | A030.row2; DOC-006 p15/eFigure9 | REPORT; method context REPORT/PLAN | 90-day mRS5-6; ASPECTS 3-5; total n277; EVT/MM | 57 (41.01) / 139 | 80 (57.97) / 138 | 0.70 (0.56-0.88) | R-adverse; ordered/contained; null excluded; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1035 | A030.row3; DOC-006 p15/eFigure9 | REPORT; method context REPORT/PLAN | 90-day mRS5-6; ASPECTS 6-10; total n40; EVT/MM | 10 (55.56) / 18 | 14 (63.64) / 22 | 0.78 (0.46-1.33) | R-adverse; ordered/contained; null included; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1036 | A030.row4; DOC-006 p15/eFigure9 | REPORT; method context REPORT/PLAN | 90-day mRS5-6; ASPECTS 3; total n73; EVT/MM | 22 (48.89) / 45 | 20 (71.43) / 28 | 0.71 (0.49-1.04) | R-adverse; ordered/contained; null included; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1037 | A030.row5; DOC-006 p15/eFigure9 | REPORT; method context REPORT/PLAN | 90-day mRS5-6; ASPECTS 4; total n88; EVT/MM | 12 (38.71) / 31 | 35 (61.40) / 57 | 0.69 (0.45-1.07) | R-adverse; ordered/contained; null included; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1038 | A030.row6; DOC-006 p15/eFigure9 | REPORT; method context REPORT/PLAN | 90-day mRS5-6; ASPECTS 5; total n116; EVT/MM | 23 (36.51) / 63 | 25 (47.17) / 53 | 0.67 (0.45-1.01) | R-adverse; ordered/contained; null included; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1039 | A030.row7; DOC-006 p15/eFigure9 | REPORT; method context REPORT/PLAN | 90-day mRS5-6; CTP/MRI core <70 mL; total n156; EVT/MM | 27 (32.93) / 82 | 32 (43.24) / 74 | 0.75 (0.52-1.08) | R-adverse; ordered/contained; null included; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1040 | A030.row8; DOC-006 p15/eFigure9 | REPORT; method context REPORT/PLAN | 90-day mRS5-6; CTP/MRI core ≥70 mL; total n180; EVT/MM | 49 (56.98) / 86 | 70 (74.47) / 94 | 0.74 (0.61-0.91) | R-adverse; ordered/contained; null excluded; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1041 | A030.row9; DOC-006 p15/eFigure9 | REPORT; method context REPORT/PLAN | 90-day mRS5-6; CTP/MRI core <100 mL; total n236; EVT/MM | 44 (37.61) / 117 | 64 (53.78) / 119 | 0.66 (0.51-0.86) | R-adverse; ordered/contained; null excluded; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1042 | A030.row10; DOC-006 p15/eFigure9 | REPORT; method context REPORT/PLAN | 90-day mRS5-6; CTP/MRI core ≥100 mL; total n100; EVT/MM | 32 (62.75) / 51 | 38 (77.55) / 49 | 0.82 (0.65-1.04) | R-adverse; ordered/contained; null included; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1043 | A030.row11; DOC-006 p15/eFigure9 | REPORT; method context REPORT/PLAN | 90-day mRS5-6; CTP/MRI core <150 mL; total n296; EVT/MM | 63 (42.86) / 147 | 86 (57.72) / 149 | 0.69 (0.56-0.85) | R-adverse; ordered/contained; null excluded; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1044 | A030.row12; DOC-006 p15/eFigure9 | REPORT; method context REPORT/PLAN | 90-day mRS5-6; CTP/MRI core ≥150 mL; total n40; EVT/MM | 13 (61.90) / 21 | 16 (84.21) / 19 | 0.81 (0.56-1.19) | R-adverse; ordered/contained; null included; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1045 | A030.row13; DOC-006 p15/eFigure9 | REPORT; method context REPORT/PLAN | 90-day mRS5-6; CTP/MRI mismatch ≥1.2 and ≥10 mL: No; total n29; EVT/MM | 3 (37.50) / 8 | 14 (66.67) / 21 | 0.58 (0.26-1.31) | R-adverse; ordered/contained; null included; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1046 | A030.row14; DOC-006 p15/eFigure9 | REPORT; method context REPORT/PLAN | 90-day mRS5-6; CTP/MRI mismatch ≥1.2 and ≥10 mL: Yes; total n307; EVT/MM | 73 (45.62) / 160 | 88 (59.86) / 147 | 0.75 (0.62-0.91) | R-adverse; ordered/contained; null excluded; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1047 | A030.row15; DOC-006 p15/eFigure9 | REPORT; method context REPORT/PLAN | 90-day mRS5-6; CTP/MRI mismatch ≥1.8 and ≥15 mL: No; total n120; EVT/MM | 30 (51.72) / 58 | 44 (70.97) / 62 | 0.73 (0.55-0.95) | R-adverse; ordered/contained; null excluded; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1048 | A030.row16; DOC-006 p15/eFigure9 | REPORT; method context REPORT/PLAN | 90-day mRS5-6; CTP/MRI mismatch ≥1.8 and ≥15 mL: Yes; total n216; EVT/MM | 46 (41.82) / 110 | 58 (54.72) / 106 | 0.74 (0.58-0.95) | R-adverse; ordered/contained; null excluded; counts reconcile; missing R | PASS_1_COMPLETE | PASS_2_COMPLETE |

## Individual interaction-test relationships

Each record is separate from the row effects. Missing I means test statistic, degrees of freedom and fitted coefficient/covariance mapping absent; missing I0 adds unknown treatment interaction handling for the zero-event ASPECTS0-2 stratum; missing IM adds an unprinted test value and an unreported reason for omission. For core/mismatch binary groups, a two-subgroup interaction statistic is not reconstructed by assuming independence of fitted row effects. No finite interval for the heterogeneity contrast is printed.

| S ID | Mapping key and exact location | Roles | Matched result key | Printed interaction P | Stated rule / result | Named missing definitions | Pass 1 | Pass 2 |
|---|---|---|---|---|---|---|---|
| S1049 | A028.interaction1; DOC-006 p13/eFigure7 | REPORT; method context REPORT/PLAN | 90-day mRS0-2; treatment×ASPECTS 0-2/3-5/6-10 | .9055 | I; two-sided P>.05; no significant treatment heterogeneity supported by this printed test | I,I0 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1050 | A028.interaction2; DOC-006 p13/eFigure7 | REPORT; method context REPORT/PLAN | 90-day mRS0-2; treatment×ASPECTS 3/4/5 | .9543 | I; two-sided P>.05; no significant treatment heterogeneity supported by this printed test | I | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1051 | A028.interaction3; DOC-006 p13/eFigure7 | REPORT; method context REPORT/PLAN | 90-day mRS0-2; treatment×CTP/MRI core 70 mL | .4097 | I; two-sided P>.05; no significant treatment heterogeneity supported by this printed test | I | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1052 | A028.interaction4; DOC-006 p13/eFigure7 | REPORT; method context REPORT/PLAN | 90-day mRS0-2; treatment×CTP/MRI core 100 mL | .7338 | I; two-sided P>.05; no significant treatment heterogeneity supported by this printed test | I | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1053 | A028.interaction5; DOC-006 p13/eFigure7 | REPORT; method context REPORT/PLAN | 90-day mRS0-2; treatment×CTP/MRI core 150 mL | not displayed | I; no numeric test available | IM | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1054 | A028.interaction6; DOC-006 p13/eFigure7 | REPORT; method context REPORT/PLAN | 90-day mRS0-2; treatment×CTP/MRI mismatch ≥1.2 and ≥10 mL | not displayed | I; no numeric test available | IM | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1055 | A028.interaction7; DOC-006 p13/eFigure7 | REPORT; method context REPORT/PLAN | 90-day mRS0-2; treatment×CTP/MRI mismatch ≥1.8 and ≥15 mL | .8079 | I; two-sided P>.05; no significant treatment heterogeneity supported by this printed test | I | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1056 | A029.interaction1; DOC-006 p14/eFigure8 | REPORT; method context REPORT/PLAN | 90-day mRS0-3; treatment×ASPECTS 0-2/3-5/6-10 | .6788 | I; two-sided P>.05; no significant treatment heterogeneity supported by this printed test | I,I0 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1057 | A029.interaction2; DOC-006 p14/eFigure8 | REPORT; method context REPORT/PLAN | 90-day mRS0-3; treatment×ASPECTS 3/4/5 | .8927 | I; two-sided P>.05; no significant treatment heterogeneity supported by this printed test | I | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1058 | A029.interaction3; DOC-006 p14/eFigure8 | REPORT; method context REPORT/PLAN | 90-day mRS0-3; treatment×CTP/MRI core 70 mL | .2093 | I; two-sided P>.05; no significant treatment heterogeneity supported by this printed test | I | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1059 | A029.interaction4; DOC-006 p14/eFigure8 | REPORT; method context REPORT/PLAN | 90-day mRS0-3; treatment×CTP/MRI core 100 mL | .574 | I; two-sided P>.05; no significant treatment heterogeneity supported by this printed test | I | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1060 | A029.interaction5; DOC-006 p14/eFigure8 | REPORT; method context REPORT/PLAN | 90-day mRS0-3; treatment×CTP/MRI core 150 mL | not displayed | I; no numeric test available | IM | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1061 | A029.interaction6; DOC-006 p14/eFigure8 | REPORT; method context REPORT/PLAN | 90-day mRS0-3; treatment×CTP/MRI mismatch ≥1.2 and ≥10 mL | .4588 | I; two-sided P>.05; no significant treatment heterogeneity supported by this printed test | I | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1062 | A029.interaction7; DOC-006 p14/eFigure8 | REPORT; method context REPORT/PLAN | 90-day mRS0-3; treatment×CTP/MRI mismatch ≥1.8 and ≥15 mL | .5921 | I; two-sided P>.05; no significant treatment heterogeneity supported by this printed test | I | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1063 | A030.interaction1; DOC-006 p15/eFigure9 | REPORT; method context REPORT/PLAN | 90-day mRS5-6; treatment×ASPECTS 0-2/3-5/6-10 | .8204 | I; two-sided P>.05; no significant treatment heterogeneity supported by this printed test | I | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1064 | A030.interaction2; DOC-006 p15/eFigure9 | REPORT; method context REPORT/PLAN | 90-day mRS5-6; treatment×ASPECTS 3/4/5 | .7244 | I; two-sided P>.05; no significant treatment heterogeneity supported by this printed test | I | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1065 | A030.interaction3; DOC-006 p15/eFigure9 | REPORT; method context REPORT/PLAN | 90-day mRS5-6; treatment×CTP/MRI core 70 mL | .9344 | I; two-sided P>.05; no significant treatment heterogeneity supported by this printed test | I | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1066 | A030.interaction4; DOC-006 p15/eFigure9 | REPORT; method context REPORT/PLAN | 90-day mRS5-6; treatment×CTP/MRI core 100 mL | .2291 | I; two-sided P>.05; no significant treatment heterogeneity supported by this printed test | I | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1067 | A030.interaction5; DOC-006 p15/eFigure9 | REPORT; method context REPORT/PLAN | 90-day mRS5-6; treatment×CTP/MRI core 150 mL | .2056 | I; two-sided P>.05; no significant treatment heterogeneity supported by this printed test | I | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1068 | A030.interaction6; DOC-006 p15/eFigure9 | REPORT; method context REPORT/PLAN | 90-day mRS5-6; treatment×CTP/MRI mismatch ≥1.2 and ≥10 mL | .6255 | I; two-sided P>.05; no significant treatment heterogeneity supported by this printed test | I | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1069 | A030.interaction7; DOC-006 p15/eFigure9 | REPORT; method context REPORT/PLAN | 90-day mRS5-6; treatment×CTP/MRI mismatch ≥1.8 and ≥15 mL | .9485 | I; two-sided P>.05; no significant treatment heterogeneity supported by this printed test | I | PASS_1_COMPLETE | PASS_2_COMPLETE |

## Matched occurrences and cross-lane boundaries

A028-A030 and corresponding S IDs retain the exact binary thresholds; DOC-001 Figure1/SASPECTS narrative addresses ordinal mRS effects and is not a duplicate of these binary RRs or their interactions. DOC-001 p4's statement of similar results for binary outcomes is compatible with stronger-benefit central strata and nonsignificant heterogeneity; it does not claim every subgroup effect is significant. DOC-001 Table2 andTable3 are within-received-treatment imaging associations, with as-treated arm totals170/166, rather than these between-randomized-treatment stratum effects; they are not numerical duplicate occurrences. DOC-006 eFigure20 arm counts corroborate denominator identity but do not print duplicate modeled RRs. PLAN specifications corroborate the stated model only and do not create a PLAN/REPORT discrepancy for F-ST1-101. Cross-source design changes are assigned elsewhere.

Mechanical reproduction limits: individual covariates/covariance and interaction test statistics/degrees of freedom absent; three printed asterisks and three absent interaction P slots remain fully mapped. These are derivative/reproduction limits rather than scientific coverage gaps. Exact zero-event counts, finite RRs, finite intervals and within-subgroup model statement are available for F-ST1-101. No external evidence, old candidate/report decisions, or unapproved Python was used.


## Independent pass-2 completion

Fresh runtime root/stat2_forest_a, gpt-6.1-sol/high, revisited every S1001–S1069 record against the complete current ledger, screening decisions and source recheck. It directly inspected exact-source current-run renderings of DOC-006 pp.13–15 and DOC-001 p.7, and directly read DOC-001 p.4 and DOC-005 pp.4–6 with native Poppler26.01.0 extraction on CPU. No derivative was created and no supplied/reused artifact was changed. All 69 rows above carry both completion markers; every row has explicit independent reasoning in checkers/statistical_parts/pass2_forest_a.md. Existing C004 covers all-zero finite fits, C006 covers the ≥100mL matched mRS distribution/threshold discrepancies, and operative allocation/core-hierarchy issues remain C002/C003. Individual effect P values are not supplied; interaction Ps are separately labeled tests. No new qualifying observation was emitted. Precise absent model, covariance and missing-cell definitions remain documented. No severity, disposition or numeric replacement was assigned.
# Statistical pass 1 relationship inventory: forest B

Runtime agent identity: /root/stat1_forest_b. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN. Pass: 1. Exact assigned scope: DOC-006 physical PDF pp.16-19, eFigures10-13, mapper parents A031-A034. All 64 printed effect/CI rows and all32 distinct interaction tests are mapped below as 96 relationships S2001-S2096. There are no source-unit or relationship gaps. Other forests, continuous prediction graphs, design comparisons and main-paper results are assigned to other shards.

Sources were read from the supplied PDFs through direct Poppler pdftotext and the source-linked reusable page images page-016.png through page-019.png. Native text establishes captions; all four full forest images were visually inspected, including every numeric row, axis, direction annotation and interaction P. No source, reusable asset or other agent artifact was modified. CPU device and direct tools follow tooling_record.md. No new extraction or image derivative was produced. Scope and review contract were read completely.

## Shared definitions incorporated into every relationship record

Each record below includes these definitions by its M/P/D code. Document role of every plotted relationship is REPORT. Source links identify physical pages; printed folios are15-18. EVT denotes thrombectomy; MM medical management. Follow-up is90days. NCCT is CT hypodensity volume; largest is composite volume=max(CTP/MRI,CT hypodensity). Core thresholds are mL. Mismatch profile1 is ratio≥1.2 AND volume≥10mL; profile2 is ratio≥1.8 AND volume≥15mL;0=no,1=yes. Table printed component order is EVT;MM;effect(95%CI). Distribution rows use median[IQR]; binary rows use event count(percent). TotalN is the printed stratum total, not either arm denominator.

- **P1 population:** eligible analysis cohort of 336, retained after imaging/outcome exclusions; treatment-group effects compared by randomization assignment. [REPORT main article methods p4](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4) explicitly distinguishes these treatment effects from within-treatment as-treated associations. Arm sizes in the records are the integer arm sizes implied by the printed event counts/percentages and stratum total across these four displays; they are contextual denominator reconciliation, not newly supplied model inputs. The current-analysis PLAN says as-treated globally; that planned-versus-reported relationship is owned by the design shard, so it is cross-referenced rather than separately emitted here.
- **M1:** [REPORT main p3-4](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4) describes adjusted probabilistic index models for ordinal treatment effect, odds of a randomly chosen EVT patient having a better mRS outcome than a randomly chosen MM patient, ties split equally. mRS5/6 merged for distribution analysis. [PLAN DOC-005 p4](../../../joi240006supp4_prod_1708623115.00733.pdf#page=4) specifies age, presentation NIHSS, LKW-to-randomization and core volume, omitting the variable used for stratification. Core-stratified effects therefore omit core-volume adjustment. Actual forest columns print GenOR(95%CI); no individual row P, standard error, statistic or degrees of freedom are printed.
- **M2:** [REPORT main p4](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4) explicitly describes modified Poisson models with robust standard errors for secondary-outcome treatment effects. [PLAN DOC-005 pp4-5](../../../joi240006supp4_prod_1708623115.00733.pdf#page=4) specifies the same prognostic covariates/stratifier exclusion. Printed effect is relative risk EVT/MM, not an odds ratio, crude event ratio or within-arm covariate association. Logistic fallback is specified for probability plots, not these RR forests.
- **M3/M4:** interaction between randomized treatment and the characteristic/profile, accompanying M1/M2 outcome respectively. [REPORT main p4](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4) states subgroup and continuous interactions separately; [PLAN DOC-005 pp5-6](../../../joi240006supp4_prod_1708623115.00733.pdf#page=5) provides treatment×core/profile terms. Each printed P here belongs to a pair of strata; it is not the P for either row effect.
- **Decision rule:** main p4 states two-sided tests and significance P<.05, exploratory analyses without multiplicity adjustment. No noninferiority/equivalence margin, interim stopping assertion or multiplicity decision is attached to these four forests. The trial stopping relationship is outside this disjoint assignment.
- **D1 missing definitions:** exact fitted coefficients/covariate distributions, robust covariance matrix, estimation implementation and row-specific standard errors/test statistics/df are not supplied. For mismatch strata, the forest does not separately identify which imaging modality enters the core adjustment. These omissions alone contain no conflicting printed number. Exact adjusted effect/CI regeneration from descriptive counts is unavailable; crude substitution is prohibited.
- **D2 missing definitions:** interaction coefficient, its standard error/statistic/df, covariance with the subgroup effect estimates, and whether the fitted interaction used a common covariate slope or separately estimated slopes are not printed. No inference about these quantities from convention is used.
- **C1 checks:** ordered positive interval endpoints; printed point estimate contained; benefit direction for ordinal GenOR>1 or desirable binary RR>1; adverse binary RR<1 means less complete dependence/death with EVT. Row interval does not test interaction. Descriptive percentages reconcile using exact integer arm denominators; the effect is model-based.
- **C2 checks:** interaction P read in its printed group position; interpreted under the stated .05 rule; no comparison to individual row95%CI significance. Missing D2 quantities prevent an exact interaction P regeneration but do not themselves produce a finding.

## Effect and interval records

| S ID | Exact REPORT location and mapper key | Stratum; totalN; contextual EVT/MM N | Printed EVT;MM;effect(95%CI) | Outcome; model; population | Pass1 checks and finding cross-reference | Missing definitions | Status |
|---|---|---|---|---|---|---|---|
| S2001 | [DOC-006 p16,eFigure10,row1](../../../joi240006supp5_prod_1708623115.01733.pdf#page=16); A031 | NCCT<70; 132; 68/64 | 4[3-6];5[4-6];2.00(1.36-2.93) | mRS distribution; M1; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2002 | [DOC-006 p16,eFigure10,row2](../../../joi240006supp5_prod_1708623115.01733.pdf#page=16); A031 | NCCT≥70; 204; 100/104 | 4[3-6];5[4-6];1.53(1.15-2.04) | mRS distribution; M1; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2003 | [DOC-006 p16,eFigure10,row3](../../../joi240006supp5_prod_1708623115.01733.pdf#page=16); A031 | largest<70; 80; 42/38 | 3[2-6];4[3-6];1.88(1.11-3.16) | mRS distribution; M1; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2004 | [DOC-006 p16,eFigure10,row4](../../../joi240006supp5_prod_1708623115.01733.pdf#page=16); A031 | largest≥70; 256; 126/130 | 4[3-6];5[4-6];1.69(1.31-2.18) | mRS distribution; M1; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2005 | [DOC-006 p16,eFigure10,row5](../../../joi240006supp5_prod_1708623115.01733.pdf#page=16); A031 | NCCT<100; 207; 103/104 | 3[2-6];5[4-6];2.25(1.65-3.06) | mRS distribution; M1; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2006 | [DOC-006 p16,eFigure10,row6](../../../joi240006supp5_prod_1708623115.01733.pdf#page=16); A031 | NCCT≥100; 129; 65/64 | 6[4-6];6[4-6];1.25(.89-1.74) | mRS distribution; M1; P1 | C1: containment/order reconcile; CI contains null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2007 | [DOC-006 p16,eFigure10,row7](../../../joi240006supp5_prod_1708623115.01733.pdf#page=16); A031 | largest<100; 165; 80/85 | 3[2-5];5[4-6];2.33(1.62-3.34) | mRS distribution; M1; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2008 | [DOC-006 p16,eFigure10,row8](../../../joi240006supp5_prod_1708623115.01733.pdf#page=16); A031 | largest≥100; 171; 88/83 | 5[4-6];6[4-6];1.46(1.09-1.96) | mRS distribution; M1; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2009 | [DOC-006 p16,eFigure10,row9](../../../joi240006supp5_prod_1708623115.01733.pdf#page=16); A031 | NCCT<150; 297; 151/146 | 4[3-6];5[4-6];1.70(1.33-2.19) | mRS distribution; M1; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2010 | [DOC-006 p16,eFigure10,row10](../../../joi240006supp5_prod_1708623115.01733.pdf#page=16); A031 | NCCT≥150; 39; 17/22 | 4[4-6];6[5-6];2.21(1.16-4.19) | mRS distribution; M1; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2011 | [DOC-006 p16,eFigure10,row11](../../../joi240006supp5_prod_1708623115.01733.pdf#page=16); A031 | largest<150; 273; 135/138 | 4[3-6];5[4-6];1.80(1.39-2.35) | mRS distribution; M1; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2012 | [DOC-006 p16,eFigure10,row12](../../../joi240006supp5_prod_1708623115.01733.pdf#page=16); A031 | largest≥150; 63; 33/30 | 5[4-6];6[5-6];1.82(1.13-2.94) | mRS distribution; M1; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2013 | [DOC-006 p16,eFigure10,row13](../../../joi240006supp5_prod_1708623115.01733.pdf#page=16); A031 | largest profile ratio≥1.2/volume≥10:0; 74; 34/40 | 4[3-6];5[4-6];1.74(1.03-2.95) | mRS distribution; M1; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2014 | [DOC-006 p16,eFigure10,row14](../../../joi240006supp5_prod_1708623115.01733.pdf#page=16); A031 | largest profile ratio≥1.2/volume≥10:1; 262; 134/128 | 4[3-6];5[4-6];1.81(1.39-2.35) | mRS distribution; M1; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2015 | [DOC-006 p16,eFigure10,row15](../../../joi240006supp5_prod_1708623115.01733.pdf#page=16); A031 | largest profile ratio≥1.8/volume≥15:0; 211; 111/100 | 4[3-6];5[4-6];1.64(1.23-2.18) | mRS distribution; M1; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2016 | [DOC-006 p16,eFigure10,row16](../../../joi240006supp5_prod_1708623115.01733.pdf#page=16); A031 | largest profile ratio≥1.8/volume≥15:1; 125; 57/68 | 4[3-6];5[4-6];1.94(1.30-2.88) | mRS distribution; M1; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2017 | [DOC-006 p17,eFigure11,row1](../../../joi240006supp5_prod_1708623115.01733.pdf#page=17); A032 | NCCT<70; 132; 68/64 | 17(25.00);4(6.25);3.84(1.43-10.33) | mRS0-2; M2; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2018 | [DOC-006 p17,eFigure11,row2](../../../joi240006supp5_prod_1708623115.01733.pdf#page=17); A032 | NCCT≥70; 204; 100/104 | 17(17.00);8(7.69);2.40(1.13-5.09) | mRS0-2; M2; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2019 | [DOC-006 p17,eFigure11,row3](../../../joi240006supp5_prod_1708623115.01733.pdf#page=17); A032 | largest<70; 80; 42/38 | 14(33.33);4(10.53);3.04(1.16-7.97) | mRS0-2; M2; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2020 | [DOC-006 p17,eFigure11,row4](../../../joi240006supp5_prod_1708623115.01733.pdf#page=17); A032 | largest≥70; 256; 126/130 | 20(15.87);8(6.15);2.92(1.38-6.18) | mRS0-2; M2; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2021 | [DOC-006 p17,eFigure11,row5](../../../joi240006supp5_prod_1708623115.01733.pdf#page=17); A032 | NCCT<100; 207; 103/104 | 29(28.16);8(7.69);3.72(1.85-7.45) | mRS0-2; M2; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2022 | [DOC-006 p17,eFigure11,row6](../../../joi240006supp5_prod_1708623115.01733.pdf#page=17); A032 | NCCT≥100; 129; 65/64 | 5(7.69);4(6.25);1.44(.39-5.25) | mRS0-2; M2; P1 | C1: containment/order reconcile; CI contains null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2023 | [DOC-006 p17,eFigure11,row7](../../../joi240006supp5_prod_1708623115.01733.pdf#page=17); A032 | largest<100; 165; 80/85 | 26(32.50);7(8.24);3.80(1.83-7.88) | mRS0-2; M2; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2024 | [DOC-006 p17,eFigure11,row8](../../../joi240006supp5_prod_1708623115.01733.pdf#page=17); A032 | largest≥100; 171; 88/83 | 8(9.09);5(6.02);2.08(.70-6.18) | mRS0-2; M2; P1 | C1: containment/order reconcile; CI contains null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2025 | [DOC-006 p17,eFigure11,row9](../../../joi240006supp5_prod_1708623115.01733.pdf#page=17); A032 | NCCT<150; 297; 151/146 | 33(21.85);11(7.53);3.22(1.75-5.91) | mRS0-2; M2; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2026 | [DOC-006 p17,eFigure11,row10](../../../joi240006supp5_prod_1708623115.01733.pdf#page=17); A032 | NCCT≥150; 39; 17/22 | 1(5.88);1(4.55);.12(.01-1.05) | mRS0-2; M2; P1 | C1: containment/order reconcile; CI contains null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2027 | [DOC-006 p17,eFigure11,row11](../../../joi240006supp5_prod_1708623115.01733.pdf#page=17); A032 | largest<150; 273; 135/138 | 32(23.70);11(7.97);3.29(1.79-6.06) | mRS0-2; M2; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2028 | [DOC-006 p17,eFigure11,row12](../../../joi240006supp5_prod_1708623115.01733.pdf#page=17); A032 | largest≥150; 63; 33/30 | 2(6.06);1(3.33);1.58(.16-15.47) | mRS0-2; M2; P1 | C1: containment/order reconcile; CI contains null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2029 | [DOC-006 p17,eFigure11,row13](../../../joi240006supp5_prod_1708623115.01733.pdf#page=17); A032 | largest profile ratio≥1.2/volume≥10:0; 74; 34/40 | 5(14.71);3(7.50);1.62(.47-5.62) | mRS0-2; M2; P1 | C1: containment/order reconcile; CI contains null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2030 | [DOC-006 p17,eFigure11,row14](../../../joi240006supp5_prod_1708623115.01733.pdf#page=17); A032 | largest profile ratio≥1.2/volume≥10:1; 262; 134/128 | 29(21.64);9(7.03);3.36(1.72-6.56) | mRS0-2; M2; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2031 | [DOC-006 p17,eFigure11,row15](../../../joi240006supp5_prod_1708623115.01733.pdf#page=17); A032 | largest profile ratio≥1.8/volume≥15:0; 211; 111/100 | 21(18.92);8(8.00);2.53(1.26-5.10) | mRS0-2; M2; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2032 | [DOC-006 p17,eFigure11,row16](../../../joi240006supp5_prod_1708623115.01733.pdf#page=17); A032 | largest profile ratio≥1.8/volume≥15:1; 125; 57/68 | 13(22.81);4(5.88);3.84(1.39-10.58) | mRS0-2; M2; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2033 | [DOC-006 p18,eFigure12,row1](../../../joi240006supp5_prod_1708623115.01733.pdf#page=18); A033 | NCCT<70; 132; 68/64 | 34(50.00);13(20.31);2.38(1.50-3.79) | mRS0-3; M2; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2034 | [DOC-006 p18,eFigure12,row2](../../../joi240006supp5_prod_1708623115.01733.pdf#page=18); A033 | NCCT≥70; 204; 100/104 | 31(31.00);18(17.31);1.97(1.24-3.13) | mRS0-3; M2; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2035 | [DOC-006 p18,eFigure12,row3](../../../joi240006supp5_prod_1708623115.01733.pdf#page=18); A033 | largest<70; 80; 42/38 | 26(61.90);12(31.58);1.85(1.19-2.90) | mRS0-3; M2; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2036 | [DOC-006 p18,eFigure12,row4](../../../joi240006supp5_prod_1708623115.01733.pdf#page=18); A033 | largest≥70; 256; 126/130 | 39(30.95);19(14.62);2.34(1.50-3.67) | mRS0-3; M2; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2037 | [DOC-006 p18,eFigure12,row5](../../../joi240006supp5_prod_1708623115.01733.pdf#page=18); A033 | NCCT<100; 207; 103/104 | 52(50.49);20(19.23);2.67(1.84-3.89) | mRS0-3; M2; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2038 | [DOC-006 p18,eFigure12,row6](../../../joi240006supp5_prod_1708623115.01733.pdf#page=18); A033 | NCCT≥100; 129; 65/64 | 13(20.00);11(17.19);1.34(.66-2.71) | mRS0-3; M2; P1 | C1: containment/order reconcile; CI contains null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2039 | [DOC-006 p18,eFigure12,row7](../../../joi240006supp5_prod_1708623115.01733.pdf#page=18); A033 | largest<100; 165; 80/85 | 46(57.50);18(21.18);2.65(1.77-3.97) | mRS0-3; M2; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2040 | [DOC-006 p18,eFigure12,row8](../../../joi240006supp5_prod_1708623115.01733.pdf#page=18); A033 | largest≥100; 171; 88/83 | 19(21.59);13(15.66);1.64(.89-3.03) | mRS0-3; M2; P1 | C1: containment/order reconcile; CI contains null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2041 | [DOC-006 p18,eFigure12,row9](../../../joi240006supp5_prod_1708623115.01733.pdf#page=18); A033 | NCCT<150; 297; 151/146 | 62(41.06);29(19.86);2.24(1.60-3.13) | mRS0-3; M2; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2042 | [DOC-006 p18,eFigure12,row10](../../../joi240006supp5_prod_1708623115.01733.pdf#page=18); A033 | NCCT≥150; 39; 17/22 | 3(17.65);2(9.09);3.70(.90-15.24) | mRS0-3; M2; P1 | C1: containment/order reconcile; CI contains null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2043 | [DOC-006 p18,eFigure12,row11](../../../joi240006supp5_prod_1708623115.01733.pdf#page=18); A033 | largest<150; 273; 135/138 | 59(43.70);29(21.01);2.25(1.61-3.15) | mRS0-3; M2; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2044 | [DOC-006 p18,eFigure12,row12](../../../joi240006supp5_prod_1708623115.01733.pdf#page=18); A033 | largest≥150; 63; 33/30 | 6(18.18);2(6.67);3.50(1.12-10.92) | mRS0-3; M2; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2045 | [DOC-006 p18,eFigure12,row13](../../../joi240006supp5_prod_1708623115.01733.pdf#page=18); A033 | largest profile ratio≥1.2/volume≥10:0; 74; 34/40 | 13(38.24);7(17.50);2.11(.96-4.64) | mRS0-3; M2; P1 | C1: containment/order reconcile; CI contains null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2046 | [DOC-006 p18,eFigure12,row14](../../../joi240006supp5_prod_1708623115.01733.pdf#page=18); A033 | largest profile ratio≥1.2/volume≥10:1; 262; 134/128 | 52(38.81);24(18.75);2.26(1.59-3.21) | mRS0-3; M2; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2047 | [DOC-006 p18,eFigure12,row15](../../../joi240006supp5_prod_1708623115.01733.pdf#page=18); A033 | largest profile ratio≥1.8/volume≥15:0; 211; 111/100 | 39(35.14);18(18.00);1.99(1.28-3.10) | mRS0-3; M2; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2048 | [DOC-006 p18,eFigure12,row16](../../../joi240006supp5_prod_1708623115.01733.pdf#page=18); A033 | largest profile ratio≥1.8/volume≥15:1; 125; 57/68 | 26(45.61);13(19.12);2.46(1.53-3.93) | mRS0-3; M2; P1 | C1: containment/order reconcile; CI excludes null1; direction reconciles; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2049 | [DOC-006 p19,eFigure13,row1](../../../joi240006supp5_prod_1708623115.01733.pdf#page=19); A034 | NCCT<70; 132; 68/64 | 27(39.71);39(60.94);.68(.49-.95) | mRS5-6; M2; P1 | C1: containment/order reconcile; CI excludes null1; axis direction F-ST1-201; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2050 | [DOC-006 p19,eFigure13,row2](../../../joi240006supp5_prod_1708623115.01733.pdf#page=19); A034 | NCCT≥70; 204; 100/104 | 49(49.00);63(60.58);.77(.62-.97) | mRS5-6; M2; P1 | C1: containment/order reconcile; CI excludes null1; axis direction F-ST1-201; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2051 | [DOC-006 p19,eFigure13,row3](../../../joi240006supp5_prod_1708623115.01733.pdf#page=19); A034 | largest<70; 80; 42/38 | 14(33.33);17(44.74);.82(.49-1.37) | mRS5-6; M2; P1 | C1: containment/order reconcile; CI contains null1; axis direction F-ST1-201; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2052 | [DOC-006 p19,eFigure13,row4](../../../joi240006supp5_prod_1708623115.01733.pdf#page=19); A034 | largest≥70; 256; 126/130 | 62(49.21);85(65.38);.72(.60-.88) | mRS5-6; M2; P1 | C1: containment/order reconcile; CI excludes null1; axis direction F-ST1-201; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2053 | [DOC-006 p19,eFigure13,row5](../../../joi240006supp5_prod_1708623115.01733.pdf#page=19); A034 | NCCT<100; 207; 103/104 | 37(35.92);60(57.69);.61(.46-.81) | mRS5-6; M2; P1 | C1: containment/order reconcile; CI excludes null1; axis direction F-ST1-201; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2054 | [DOC-006 p19,eFigure13,row6](../../../joi240006supp5_prod_1708623115.01733.pdf#page=19); A034 | NCCT≥100; 129; 65/64 | 39(60.00);42(65.62);.87(.69-1.10) | mRS5-6; M2; P1 | C1: containment/order reconcile; CI contains null1; axis direction F-ST1-201; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2055 | [DOC-006 p19,eFigure13,row7](../../../joi240006supp5_prod_1708623115.01733.pdf#page=19); A034 | largest<100; 165; 80/85 | 26(32.50);44(51.76);.62(.44-.86) | mRS5-6; M2; P1 | C1: containment/order reconcile; CI excludes null1; axis direction F-ST1-201; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2056 | [DOC-006 p19,eFigure13,row8](../../../joi240006supp5_prod_1708623115.01733.pdf#page=19); A034 | largest≥100; 171; 88/83 | 50(56.82);58(69.88);.78(.64-.96) | mRS5-6; M2; P1 | C1: containment/order reconcile; CI excludes null1; axis direction F-ST1-201; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2057 | [DOC-006 p19,eFigure13,row9](../../../joi240006supp5_prod_1708623115.01733.pdf#page=19); A034 | NCCT<150; 297; 151/146 | 69(45.70);85(58.22);.76(.62-.93) | mRS5-6; M2; P1 | C1: containment/order reconcile; CI excludes null1; axis direction F-ST1-201; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2058 | [DOC-006 p19,eFigure13,row10](../../../joi240006supp5_prod_1708623115.01733.pdf#page=19); A034 | NCCT≥150; 39; 17/22 | 7(41.18);17(77.27);.55(.33-.94) | mRS5-6; M2; P1 | C1: containment/order reconcile; CI excludes null1; axis direction F-ST1-201; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2059 | [DOC-006 p19,eFigure13,row11](../../../joi240006supp5_prod_1708623115.01733.pdf#page=19); A034 | largest<150; 273; 135/138 | 59(43.70);78(56.52);.72(.58-.90) | mRS5-6; M2; P1 | C1: containment/order reconcile; CI excludes null1; axis direction F-ST1-201; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2060 | [DOC-006 p19,eFigure13,row12](../../../joi240006supp5_prod_1708623115.01733.pdf#page=19); A034 | largest≥150; 63; 33/30 | 17(51.52);24(80.00);.69(.48-.97) | mRS5-6; M2; P1 | C1: containment/order reconcile; CI excludes null1; axis direction F-ST1-201; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2061 | [DOC-006 p19,eFigure13,row13](../../../joi240006supp5_prod_1708623115.01733.pdf#page=19); A034 | largest profile ratio≥1.2/volume≥10:0; 74; 34/40 | 12(35.29);23(57.50);.67(.41-1.10) | mRS5-6; M2; P1 | C1: containment/order reconcile; CI contains null1; axis direction F-ST1-201; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2062 | [DOC-006 p19,eFigure13,row14](../../../joi240006supp5_prod_1708623115.01733.pdf#page=19); A034 | largest profile ratio≥1.2/volume≥10:1; 262; 134/128 | 64(47.76);79(61.72);.74(.61-.90) | mRS5-6; M2; P1 | C1: containment/order reconcile; CI excludes null1; axis direction F-ST1-201; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2063 | [DOC-006 p19,eFigure13,row15](../../../joi240006supp5_prod_1708623115.01733.pdf#page=19); A034 | largest profile ratio≥1.8/volume≥15:0; 211; 111/100 | 50(45.05);61(61.00);.76(.60-.95) | mRS5-6; M2; P1 | C1: containment/order reconcile; CI excludes null1; axis direction F-ST1-201; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2064 | [DOC-006 p19,eFigure13,row16](../../../joi240006supp5_prod_1708623115.01733.pdf#page=19); A034 | largest profile ratio≥1.8/volume≥15:1; 125; 57/68 | 26(45.61);41(60.29);.71(.53-.97) | mRS5-6; M2; P1 | C1: containment/order reconcile; CI excludes null1; axis direction F-ST1-201; no row-effect P printed | D1 | PASS_1_COMPLETE; PASS_2_COMPLETE |

## Interaction test records

| S ID | Exact REPORT location and mapper key | Characteristic/tested comparison | Printed interaction P | Outcome; model; population | Pass1 check | Missing definitions | Status |
|---|---|---|---|---|---|---|---|
| S2065 | [DOC-006 p16,eFigure10,interaction1](../../../joi240006supp5_prod_1708623115.01733.pdf#page=16); A031 | NCCT70; two subgroup levels | .2684 | mRS distribution; M3; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2066 | [DOC-006 p16,eFigure10,interaction2](../../../joi240006supp5_prod_1708623115.01733.pdf#page=16); A031 | largest70; two subgroup levels | .9413 | mRS distribution; M3; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2067 | [DOC-006 p16,eFigure10,interaction3](../../../joi240006supp5_prod_1708623115.01733.pdf#page=16); A031 | NCCT100; two subgroup levels | .0164 | mRS distribution; M3; P1 | C2; below .05; heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2068 | [DOC-006 p16,eFigure10,interaction4](../../../joi240006supp5_prod_1708623115.01733.pdf#page=16); A031 | largest100; two subgroup levels | .0707 | mRS distribution; M3; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2069 | [DOC-006 p16,eFigure10,interaction5](../../../joi240006supp5_prod_1708623115.01733.pdf#page=16); A031 | NCCT150; two subgroup levels | .8886 | mRS distribution; M3; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2070 | [DOC-006 p16,eFigure10,interaction6](../../../joi240006supp5_prod_1708623115.01733.pdf#page=16); A031 | largest150; two subgroup levels | .7243 | mRS distribution; M3; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2071 | [DOC-006 p16,eFigure10,interaction7](../../../joi240006supp5_prod_1708623115.01733.pdf#page=16); A031 | largest mismatch ratio≥1.2/volume≥10; two subgroup levels | .6791 | mRS distribution; M3; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2072 | [DOC-006 p16,eFigure10,interaction8](../../../joi240006supp5_prod_1708623115.01733.pdf#page=16); A031 | largest mismatch ratio≥1.8/volume≥15; two subgroup levels | .6165 | mRS distribution; M3; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2073 | [DOC-006 p17,eFigure11,interaction1](../../../joi240006supp5_prod_1708623115.01733.pdf#page=17); A032 | NCCT70; two subgroup levels | .4696 | mRS0-2; M4; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2074 | [DOC-006 p17,eFigure11,interaction2](../../../joi240006supp5_prod_1708623115.01733.pdf#page=17); A032 | largest70; two subgroup levels | .9978 | mRS0-2; M4; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2075 | [DOC-006 p17,eFigure11,interaction3](../../../joi240006supp5_prod_1708623115.01733.pdf#page=17); A032 | NCCT100; two subgroup levels | .1717 | mRS0-2; M4; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2076 | [DOC-006 p17,eFigure11,interaction4](../../../joi240006supp5_prod_1708623115.01733.pdf#page=17); A032 | largest100; two subgroup levels | .2581 | mRS0-2; M4; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2077 | [DOC-006 p17,eFigure11,interaction5](../../../joi240006supp5_prod_1708623115.01733.pdf#page=17); A032 | NCCT150; two subgroup levels | .336 | mRS0-2; M4; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2078 | [DOC-006 p17,eFigure11,interaction6](../../../joi240006supp5_prod_1708623115.01733.pdf#page=17); A032 | largest150; two subgroup levels | .5126 | mRS0-2; M4; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2079 | [DOC-006 p17,eFigure11,interaction7](../../../joi240006supp5_prod_1708623115.01733.pdf#page=17); A032 | largest mismatch ratio≥1.2/volume≥10; two subgroup levels | .3817 | mRS0-2; M4; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2080 | [DOC-006 p17,eFigure11,interaction8](../../../joi240006supp5_prod_1708623115.01733.pdf#page=17); A032 | largest mismatch ratio≥1.8/volume≥15; two subgroup levels | .5351 | mRS0-2; M4; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2081 | [DOC-006 p18,eFigure12,interaction1](../../../joi240006supp5_prod_1708623115.01733.pdf#page=18); A033 | NCCT70; two subgroup levels | .5583 | mRS0-3; M4; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2082 | [DOC-006 p18,eFigure12,interaction2](../../../joi240006supp5_prod_1708623115.01733.pdf#page=18); A033 | largest70; two subgroup levels | .4539 | mRS0-3; M4; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2083 | [DOC-006 p18,eFigure12,interaction3](../../../joi240006supp5_prod_1708623115.01733.pdf#page=18); A033 | NCCT100; two subgroup levels | .0762 | mRS0-3; M4; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2084 | [DOC-006 p18,eFigure12,interaction4](../../../joi240006supp5_prod_1708623115.01733.pdf#page=18); A033 | largest100; two subgroup levels | .1516 | mRS0-3; M4; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2085 | [DOC-006 p18,eFigure12,interaction5](../../../joi240006supp5_prod_1708623115.01733.pdf#page=18); A033 | NCCT150; two subgroup levels | .6936 | mRS0-3; M4; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2086 | [DOC-006 p18,eFigure12,interaction6](../../../joi240006supp5_prod_1708623115.01733.pdf#page=18); A033 | largest150; two subgroup levels | .9146 | mRS0-3; M4; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2087 | [DOC-006 p18,eFigure12,interaction7](../../../joi240006supp5_prod_1708623115.01733.pdf#page=18); A033 | largest mismatch ratio≥1.2/volume≥10; two subgroup levels | .7419 | mRS0-3; M4; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2088 | [DOC-006 p18,eFigure12,interaction8](../../../joi240006supp5_prod_1708623115.01733.pdf#page=18); A033 | largest mismatch ratio≥1.8/volume≥15; two subgroup levels | .5951 | mRS0-3; M4; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2089 | [DOC-006 p19,eFigure13,interaction1](../../../joi240006supp5_prod_1708623115.01733.pdf#page=19); A034 | NCCT70; two subgroup levels | .4646 | mRS5-6; M4; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2090 | [DOC-006 p19,eFigure13,interaction2](../../../joi240006supp5_prod_1708623115.01733.pdf#page=19); A034 | largest70; two subgroup levels | .7845 | mRS5-6; M4; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2091 | [DOC-006 p19,eFigure13,interaction3](../../../joi240006supp5_prod_1708623115.01733.pdf#page=19); A034 | NCCT100; two subgroup levels | .0664 | mRS5-6; M4; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2092 | [DOC-006 p19,eFigure13,interaction4](../../../joi240006supp5_prod_1708623115.01733.pdf#page=19); A034 | largest100; two subgroup levels | .2512 | mRS5-6; M4; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2093 | [DOC-006 p19,eFigure13,interaction5](../../../joi240006supp5_prod_1708623115.01733.pdf#page=19); A034 | NCCT150; two subgroup levels | .3272 | mRS5-6; M4; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2094 | [DOC-006 p19,eFigure13,interaction6](../../../joi240006supp5_prod_1708623115.01733.pdf#page=19); A034 | largest150; two subgroup levels | .9984 | mRS5-6; M4; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2095 | [DOC-006 p19,eFigure13,interaction7](../../../joi240006supp5_prod_1708623115.01733.pdf#page=19); A034 | largest mismatch ratio≥1.2/volume≥10; two subgroup levels | .7851 | mRS5-6; M4; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S2096 | [DOC-006 p19,eFigure13,interaction8](../../../joi240006supp5_prod_1708623115.01733.pdf#page=19); A034 | largest mismatch ratio≥1.8/volume≥15; two subgroup levels | .7981 | mRS5-6; M4; P1 | C2; above .05; no heterogeneity at stated level; not a row-effect P | D2 | PASS_1_COMPLETE; PASS_2_COMPLETE |

## Cross-references and completion

All effect estimates match their own printed columns and plotted direction of location relative to null1. All64 point estimates lie inside their ordered95%CI;51 intervals exclude null1 and13 include it. Every assigned interaction P has its own record;1 is below .05 and31 above .05. F-ST1-201 consolidates all16 eFigure13 reversed direction annotations and references S2049-S2064. No point-estimate/interval/P conflict is created by interpreting an interaction P as a treatment-effect P.

Main-paper ordinal/core/mismatch effects and adjacent forests A028-A030 have separate S IDs in other shards. Their common method and endpoint definitions are corroborating context here, not duplicate relationship registrations. eFigure20 exact arm counts/distributions (A041a-f,k-p and later composite mismatch panels) are numeric-shard relationships; denominators are shown here solely to identify each effect population. No unprinted event or pointwise fitted probability was reconstructed as a reported result. Any cross-source model/population or prespecification finding belongs to the separately assigned design/main shards.

As a descriptive diagnostic only, the geometric-center interval derived from endpoint half-unit intervals overlaps the half-unit interval of the printed point estimate for all 64 rows; each gap and relative discrepancy is zero. This does not infer an unstated CI construction method. The apparent geometric-center discrepancy for S2026 (.12 [.01-1.05]) is addressed in the checker exclusions. Interaction reconstruction from separate row CIs is diagnostic only and is addressed separately. These do not obscure the reproduced categorical direction conflict.


## Independent statistical pass 2 completion

Fresh runtime /root/stat2_forest_b, gpt-6.1-sol/high, revisited every S2001–S2096 after the complete ledger, screen and exact-source recheck existed. All96 original records above retain pass1 and explicitly record PASS_2_COMPLETE. Detailed per-S reasoning, full source rereading, all32 diagnostic interaction comparisons, and the independent three-row exclusion reconsideration are in [pass2 forest B](../checkers/statistical_parts/pass2_forest_b.md). No original source value or stable S ID changed; no new finding was reproduced. C017 covers all16 adverse-outcome direction labels. Missing fitted-model/covariance definitions remain precisely bounded; no scientific coverage gap remains.

# Statistical relationship inventory: remaining A, passes 1 and 2

Runtime ID: root/stat1_remaining_a. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN. Scope: DOC005 physical pages 1-7; DOC006 physical pages 1-12 and 20-32. DOC006 eFigures7-13, physical pages13-19, belong to independent forest shards. This shard reviewed 32 source pages, including 21 reusable page images, and creates 78 stable relationships S3001-S3078. Every relationship below is PASS_1_COMPLETE. No scientific coverage gap remains in the assigned units.

Read QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md completely. Mapping inputs: support_parts/results_a.md A001-A027 and A035-A041, and main_quantitative_evidence.md method/matched-result keys. Direct Poppler26.01.0 pdftotext, transient stdout, checked all DOC005 pages, DOC006pp4-12/20-32, and mainpp3,4,8,10,11. Reusable images DOC006pp5-12/20-32 were inspected visually; source-linked supplied PDF remains authority. No extraction files, sources, or reused assets were changed. Compute device: CPU. No web or unapproved Python used.

## Source and shared contracts

- [DOC005 analysis SAP](../../../joi240006supp4_prod_1708623115.00733.pdf#page=1) is PLAN by prospective analysis content, including its disclosed post hoc appendix.
- [DOC006 results supplement](../../../joi240006supp5_prod_1708623115.01733.pdf#page=1) is REPORT. [Main article](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=1) is REPORT. All page numbers below are physical PDF pages; DOC006 printed folio equals physical page minus1.
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

# Statistical relationship inventory — pass 1 and independent pass 2, tables A

Independent pass-2 runtime: root/stat2_tables_a; gpt-6.1-sol/high/FRESH_SPAWN. All 115 assigned records S4001–S4115 were reread against direct supplied PDF pp.39–44, complete current ledger C001–C018, complete source recheck, and all initial screening decisions/justifications. Each row below now contains a separate pass-2 check and both completion states. Pass-1 observations are retained as provenance; F-ST1-401 remains screened out and is not re-emitted. Source and current-inventory values matched for all 115 records; an apparent p.44 alignment concern was reread and not reproduced. New findings: 0. No source/reused asset modified.

Runtime agent: root/stat1_tables_a; fresh spawn; gpt-6.1-sol; high reasoning. Exact assigned scope: DOC-006 eTables 3–7, physical PDF pp. 39–44, mapping B006–B010. All these result locations are REPORT. Source: `joi240006supp5_prod_1708623115.01733.pdf`. Read all six source-page images and direct native layout text. Direct text engine: Poppler pdftotext 26.01.0, `pdftotext -layout -f 39 -l 44 "joi240006supp5_prod_1708623115.01733.pdf" -`; CPU. Reused images: `.ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-039.png` through `page-044.png`. No source or reused asset modified.

The inventory contains 115 relationships: 20 eTable 3 estimate-CIs; 22 eTable 4 estimate-CIs and two expressly non-estimable cells; 16 eTable 5 estimate-CIs and eight interaction tests; three eTable 6 complete outcome-specific model comparisons covering all 12 AIC/BIC rows, plus eight AUC-CIs; 28 eTable 7 estimate-CIs and eight last-column tests. Grouping complete four-model comparisons by outcome preserves all model values and their actual comparison relationship.

## Source-grounded method context and definitions

Read supplied REPORT main article physical pp. 3–4 and REPORT DOC-006 eMethods p. 4, together with PLAN analysis-specific SAP DOC-005 pp. 4–7, as method context only. Main article specifies adjusted probabilistic index models (PIM) for mRS, modified Poisson regression with robust standard errors for binary outcomes, treatment-by-imaging interaction tests, and similar models for within-treatment associations. Tests are two-sided, significance P < .05, intervals 95%, analyses exploratory without multiplicity adjustment. Imaging-stratified treatment comparisons are by randomized assignment; within-arm imaging associations are as treated. Missing values are not imputed. There is no superiority/noninferiority/equivalence margin, multiplicity rule or stopping decision made by these assigned tables.

For eTables 3–4, compare EVT with MM within imaging strata; GenOR >1 favors better mRS, RR >1 increases probability of the named binary outcome. The sensitivity covariate map follows main/SAP descriptions: age, presentation NIHSS, LKW-to-randomization time, and core volume when core is not the stratification variable. The table itself does not print sample sizes, coefficient covariance, degrees of freedom, numerical standard errors, or separate row effect P values. These are definition limits, not findings by themselves. eTable 3 uses site-investigator ASPECTS. eTable 4 excludes MRI; CTP core is rCBF <30%. Its <70/≥70, <100/≥100 and <150/≥150 cutoffs are separate nested sensitivity analyses, not six mutually exclusive strata.

For eTable 5, within-arm associations are per 10-mL increase in the named CT hypodensity/composite volume. Population as treated: EVT N=170, MM N=166. Age, NIHSS and timing covariates follow the primary within-arm models; precise additional-volume handling is not printed in the table. GenOR <1 means worse ordinal mRS with increasing volume; RR <1 means lower favorable-outcome probability and RR >1 higher mRS 5–6 probability. Interaction P values test heterogeneity between arms and are not P values for either arm-specific slope. Which combined interaction-model coefficients correspond to the separately displayed within-arm coefficients is not specified; do not assume their covariance or equality of nuisance adjustments.

For eTable 6, eMethods p.4 specifies models containing age, presentation NIHSS, LKW-to-randomization and one imaging parameter; the table explicitly specifies ordinal logistic regression for ordinal-mRS information criteria. Thus those criteria are not labeled PIM criteria. Lower AIC/BIC and higher AUC are better; BIC differences 0–2 weak, 2–6 positive, 6–10 strong, >10 very strong. Binary-regression family, exact likelihood implementation, parameter counts and AUC confidence procedure are not printed in this table/eMethods. No AUC-comparison P value is supplied.

For eTable 7, the title expressly defines within-received-treatment associations, as treated. The first numeric column corresponds to EVT N=170, second to MM N=166, established by arm-specific denominator sums and the matching main table layout. Contrast is mismatch versus no mismatch (reference), separately for composite-core mismatch thresholds ≥10mL/ratio≥1.2 and ≥15mL/ratio≥1.8. Footnote p.44 specifies age, NIHSS, LKW-to-randomization and CTP/MRI core adjustment. GenOR >1 means better mRS; RR >1 increases the named binary outcome; RD >0 increases its adjusted probability. Last-column headings are absent on these source pages, but main article/SAP interaction description and parallel table structure identify treatment-by-mismatch tests. Treat these as interaction tests, not individual RR/RD effect P values. The precise adjusted RD estimand, estimator and confidence procedure are not stated; the visible RR/RD null-inference difference at S4095/S4096 was recorded as pass-1 finding F-ST1-401 rather than attributed to the interaction P. Independent screening excluded that finding as CONDITIONAL_OR_UNREPORTED; pass 2 retains its provenance without re-emitting it.

Checks below: `C/O/D` means estimate containment, ordered endpoints and direction checked; `null in/out` describes the printed interval relative to its own null (1 for GenOR/RR, 0 for RD). Boundary 1.00 is preserved as printed and does not by itself establish a significance conflict. Wald log-symmetry and linear midpoint calculations are diagnostics only; no numerical effect P value is inferred as the reported P. All rows explicitly retain pass-1 completion; independent pass-2 checks and completion are now recorded by a different fresh runtime. Shared method/population definitions above apply to every row of the named table, with row-specific contrasts below.

## eTable 3 — REPORT physical p.39

[Exact source](../../../joi240006supp5_prod_1708623115.01733.pdf#page=39). Population: randomized sensitivity analysis with site-investigator ASPECTS; EVT versus MM; 90-day functional outcomes. No row effect P value supplied.

| S ID | ASPECTS stratum | Outcome and measure | Printed estimate (95% CI) | Pass-1 check | Pass-2 check | State |
|---|---|---|---|---|---|---|
| S4001 | 3–5 | mRS shift, aGenOR | 1.70 (1.33–2.17) | C/O/D; null out | Direct p.39 row matched; adjusted EVT/MM effect contains estimate and ordered limits; named outcome gives direction; no own-effect P/test. Site-investigator ASPECTS distinct from core-laboratory rows; C002/C003 analysis-specification context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4002 | 3–5 | mRS 0–2, aRR | 2.97 (1.60–5.49) | C/O/D; null out | Direct p.39 row matched; adjusted EVT/MM effect contains estimate and ordered limits; named outcome gives direction; no own-effect P/test. Site-investigator ASPECTS distinct from core-laboratory rows; C002/C003 analysis-specification context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4003 | 3–5 | mRS 0–3, aRR | 2.23 (1.56–3.16) | C/O/D; null out | Direct p.39 row matched; adjusted EVT/MM effect contains estimate and ordered limits; named outcome gives direction; no own-effect P/test. Site-investigator ASPECTS distinct from core-laboratory rows; C002/C003 analysis-specification context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4004 | 3–5 | mRS 5–6, aRR | 0.74 (0.61–0.91) | C/O/D; null out | Direct p.39 row matched; adjusted EVT/MM effect contains estimate and ordered limits; named outcome gives direction; no own-effect P/test. Site-investigator ASPECTS distinct from core-laboratory rows; C002/C003 analysis-specification context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4005 | 6–10 | mRS shift, aGenOR | 1.91 (1.04–3.54) | C/O/D; null out | Direct p.39 row matched; adjusted EVT/MM effect contains estimate and ordered limits; named outcome gives direction; no own-effect P/test. Site-investigator ASPECTS distinct from core-laboratory rows; C002/C003 analysis-specification context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4006 | 6–10 | mRS 0–2, aRR | 2.93 (0.42–20.47) | C/O/D; null in | Direct p.39 row matched; adjusted EVT/MM effect contains estimate and ordered limits; named outcome gives direction; no own-effect P/test. Site-investigator ASPECTS distinct from core-laboratory rows; C002/C003 analysis-specification context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4007 | 6–10 | mRS 0–3, aRR | 1.91 (0.75–4.90) | C/O/D; null in | Direct p.39 row matched; adjusted EVT/MM effect contains estimate and ordered limits; named outcome gives direction; no own-effect P/test. Site-investigator ASPECTS distinct from core-laboratory rows; C002/C003 analysis-specification context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4008 | 6–10 | mRS 5–6, aRR | 0.60 (0.35–1.02) | C/O/D; null in | Direct p.39 row matched; adjusted EVT/MM effect contains estimate and ordered limits; named outcome gives direction; no own-effect P/test. Site-investigator ASPECTS distinct from core-laboratory rows; C002/C003 analysis-specification context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4009 | 3 | mRS shift, aGenOR | 1.88 (1.27–2.78) | C/O/D; null out | Direct p.39 row matched; adjusted EVT/MM effect contains estimate and ordered limits; named outcome gives direction; no own-effect P/test. Site-investigator ASPECTS distinct from core-laboratory rows; C002/C003 analysis-specification context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4010 | 3 | mRS 0–2, aRR | 7.82 (1.14–53.56) | C/O/D; null out | Direct p.39 row matched; adjusted EVT/MM effect contains estimate and ordered limits; named outcome gives direction; no own-effect P/test. Site-investigator ASPECTS distinct from core-laboratory rows; C002/C003 analysis-specification context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4011 | 3 | mRS 0–3, aRR | 2.53 (1.00–6.36) | C/O/D; printed boundary 1.00 | Direct p.39 row matched; adjusted EVT/MM effect contains estimate and ordered limits; named outcome gives direction; no own-effect P/test. Site-investigator ASPECTS distinct from core-laboratory rows; C002/C003 analysis-specification context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4012 | 3 | mRS 5–6, aRR | 0.66 (0.49–0.88) | C/O/D; null out | Direct p.39 row matched; adjusted EVT/MM effect contains estimate and ordered limits; named outcome gives direction; no own-effect P/test. Site-investigator ASPECTS distinct from core-laboratory rows; C002/C003 analysis-specification context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4013 | 4 | mRS shift, aGenOR | 1.51 (0.92–2.48) | C/O/D; null in | Direct p.39 row matched; adjusted EVT/MM effect contains estimate and ordered limits; named outcome gives direction; no own-effect P/test. Site-investigator ASPECTS distinct from core-laboratory rows; C002/C003 analysis-specification context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4014 | 4 | mRS 0–2, aRR | 4.11 (1.40–12.09) | C/O/D; null out | Direct p.39 row matched; adjusted EVT/MM effect contains estimate and ordered limits; named outcome gives direction; no own-effect P/test. Site-investigator ASPECTS distinct from core-laboratory rows; C002/C003 analysis-specification context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4015 | 4 | mRS 0–3, aRR | 2.44 (1.39–4.29) | C/O/D; null out | Direct p.39 row matched; adjusted EVT/MM effect contains estimate and ordered limits; named outcome gives direction; no own-effect P/test. Site-investigator ASPECTS distinct from core-laboratory rows; C002/C003 analysis-specification context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4016 | 4 | mRS 5–6, aRR | 0.94 (0.62–1.44) | C/O/D; null in | Direct p.39 row matched; adjusted EVT/MM effect contains estimate and ordered limits; named outcome gives direction; no own-effect P/test. Site-investigator ASPECTS distinct from core-laboratory rows; C002/C003 analysis-specification context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4017 | 5 | mRS shift, aGenOR | 1.93 (1.25–2.98) | C/O/D; null out | Direct p.39 row matched; adjusted EVT/MM effect contains estimate and ordered limits; named outcome gives direction; no own-effect P/test. Site-investigator ASPECTS distinct from core-laboratory rows; C002/C003 analysis-specification context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4018 | 5 | mRS 0–2, aRR | 2.08 (1.02–4.22) | C/O/D; null out | Direct p.39 row matched; adjusted EVT/MM effect contains estimate and ordered limits; named outcome gives direction; no own-effect P/test. Site-investigator ASPECTS distinct from core-laboratory rows; C002/C003 analysis-specification context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4019 | 5 | mRS 0–3, aRR | 2.46 (1.56–3.90) | C/O/D; null out | Direct p.39 row matched; adjusted EVT/MM effect contains estimate and ordered limits; named outcome gives direction; no own-effect P/test. Site-investigator ASPECTS distinct from core-laboratory rows; C002/C003 analysis-specification context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4020 | 5 | mRS 5–6, aRR | 0.71 (0.50–1.01) | C/O/D; null in | Direct p.39 row matched; adjusted EVT/MM effect contains estimate and ordered limits; named outcome gives direction; no own-effect P/test. Site-investigator ASPECTS distinct from core-laboratory rows; C002/C003 analysis-specification context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |

## eTable 4 — REPORT physical p.40

[Exact source](../../../joi240006supp5_prod_1708623115.01733.pdf#page=40). Population: randomized CT-perfusion-only sensitivity analysis; EVT versus MM, within CTP rCBF <30% core strata; 90-day outcomes. N/A explicitly means could not be evaluated; missing event-level inputs do not permit reconstructing those unestimated cells.

| S ID | CTP core stratum | Outcome and measure | Printed estimate (95% CI) | Pass-1 check | Pass-2 check | State |
|---|---|---|---|---|---|---|
| S4021 | <70mL | mRS shift, aGenOR | 1.73 (1.20–2.48) | C/O/D; null out | Direct p.40 row matched; CTP-only sensitivity and nested cutoff recognized; containment/order/outcome direction reconcile. Own-effect P absent; printed null boundary alone is not C005 narrative significance. C002/C003 context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4022 | <70mL | mRS 0–2, aRR | 2.26 (1.15–4.43) | C/O/D; null out | Direct p.40 row matched; CTP-only sensitivity and nested cutoff recognized; containment/order/outcome direction reconcile. Own-effect P absent; printed null boundary alone is not C005 narrative significance. C002/C003 context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4023 | <70mL | mRS 0–3, aRR | 1.76 (1.24–2.50) | C/O/D; null out | Direct p.40 row matched; CTP-only sensitivity and nested cutoff recognized; containment/order/outcome direction reconcile. Own-effect P absent; printed null boundary alone is not C005 narrative significance. C002/C003 context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4024 | <70mL | mRS 5–6, aRR | 0.77 (0.53–1.11) | C/O/D; null in | Direct p.40 row matched; CTP-only sensitivity and nested cutoff recognized; containment/order/outcome direction reconcile. Own-effect P absent; printed null boundary alone is not C005 narrative significance. C002/C003 context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4025 | ≥70mL | mRS shift, aGenOR | 1.61 (1.21–2.15) | C/O/D; null out | Direct p.40 row matched; CTP-only sensitivity and nested cutoff recognized; containment/order/outcome direction reconcile. Own-effect P absent; printed null boundary alone is not C005 narrative significance. C002/C003 context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4026 | ≥70mL | mRS 0–2, aRR | 4.12 (1.25–13.63) | C/O/D; null out | Direct p.40 row matched; CTP-only sensitivity and nested cutoff recognized; containment/order/outcome direction reconcile. Own-effect P absent; printed null boundary alone is not C005 narrative significance. C002/C003 context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4027 | ≥70mL | mRS 0–3, aRR | 2.89 (1.39–6.02) | C/O/D; null out | Direct p.40 row matched; CTP-only sensitivity and nested cutoff recognized; containment/order/outcome direction reconcile. Own-effect P absent; printed null boundary alone is not C005 narrative significance. C002/C003 context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4028 | ≥70mL | mRS 5–6, aRR | 0.75 (0.61–0.92) | C/O/D; null out | Direct p.40 row matched; CTP-only sensitivity and nested cutoff recognized; containment/order/outcome direction reconcile. Own-effect P absent; printed null boundary alone is not C005 narrative significance. C002/C003 context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4029 | <100mL | mRS shift, aGenOR | 1.86 (1.40–2.49) | C/O/D; null out | Direct p.40 row matched; CTP-only sensitivity and nested cutoff recognized; containment/order/outcome direction reconcile. Own-effect P absent; printed null boundary alone is not C005 narrative significance. C002/C003 context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4030 | <100mL | mRS 0–2, aRR | 2.75 (1.49–5.07) | C/O/D; null out | Direct p.40 row matched; CTP-only sensitivity and nested cutoff recognized; containment/order/outcome direction reconcile. Own-effect P absent; printed null boundary alone is not C005 narrative significance. C002/C003 context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4031 | <100mL | mRS 0–3, aRR | 2.05 (1.45–2.89) | C/O/D; null out | Direct p.40 row matched; CTP-only sensitivity and nested cutoff recognized; containment/order/outcome direction reconcile. Own-effect P absent; printed null boundary alone is not C005 narrative significance. C002/C003 context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4032 | <100mL | mRS 5–6, aRR | 0.68 (0.52–0.88) | C/O/D; null out | Direct p.40 row matched; CTP-only sensitivity and nested cutoff recognized; containment/order/outcome direction reconcile. Own-effect P absent; printed null boundary alone is not C005 narrative significance. C002/C003 context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4033 | ≥100mL | mRS shift, aGenOR | 1.44 (1.00–2.06) | C/O/D; printed boundary 1.00 | Direct p.40 row matched; CTP-only sensitivity and nested cutoff recognized; containment/order/outcome direction reconcile. Own-effect P absent; printed null boundary alone is not C005 narrative significance. C002/C003 context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4034 | ≥100mL | mRS 0–2, aRR | 3.36 (0.52–21.64) | C/O/D; null in | Direct p.40 row matched; CTP-only sensitivity and nested cutoff recognized; containment/order/outcome direction reconcile. Own-effect P absent; printed null boundary alone is not C005 narrative significance. C002/C003 context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4035 | ≥100mL | mRS 0–3, aRR | 3.04 (0.95–9.73) | C/O/D; null in | Direct p.40 row matched; CTP-only sensitivity and nested cutoff recognized; containment/order/outcome direction reconcile. Own-effect P absent; printed null boundary alone is not C005 narrative significance. C002/C003 context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4036 | ≥100mL | mRS 5–6, aRR | 0.82 (0.64–1.04) | C/O/D; null in | Direct p.40 row matched; CTP-only sensitivity and nested cutoff recognized; containment/order/outcome direction reconcile. Own-effect P absent; printed null boundary alone is not C005 narrative significance. C002/C003 context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4037 | <150mL | mRS shift, aGenOR | 1.78 (1.39–2.30) | C/O/D; null out | Direct p.40 row matched; CTP-only sensitivity and nested cutoff recognized; containment/order/outcome direction reconcile. Own-effect P absent; printed null boundary alone is not C005 narrative significance. C002/C003 context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4038 | <150mL | mRS 0–2, aRR | 2.93 (1.62–5.30) | C/O/D; null out | Direct p.40 row matched; CTP-only sensitivity and nested cutoff recognized; containment/order/outcome direction reconcile. Own-effect P absent; printed null boundary alone is not C005 narrative significance. C002/C003 context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4039 | <150mL | mRS 0–3, aRR | 2.10 (1.51–2.92) | C/O/D; null out | Direct p.40 row matched; CTP-only sensitivity and nested cutoff recognized; containment/order/outcome direction reconcile. Own-effect P absent; printed null boundary alone is not C005 narrative significance. C002/C003 context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4040 | <150mL | mRS 5–6, aRR | 0.70 (0.56–0.87) | C/O/D; null out | Direct p.40 row matched; CTP-only sensitivity and nested cutoff recognized; containment/order/outcome direction reconcile. Own-effect P absent; printed null boundary alone is not C005 narrative significance. C002/C003 context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4041 | ≥150mL | mRS shift, aGenOR | 1.43 (0.80–2.54) | C/O/D; null in | Direct p.40 row matched; CTP-only sensitivity and nested cutoff recognized; containment/order/outcome direction reconcile. Own-effect P absent; printed null boundary alone is not C005 narrative significance. C002/C003 context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4042 | ≥150mL | mRS 0–2, aRR | N/A | Explicit non-estimable result; no numerical test supplied | Direct p.40 N/A and could-not-be-evaluated footnote matched; no finite numerical result asserted. MRI exclusion changes sensitivity population, so no equality to CTP/MRI primary rows assumed. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4043 | ≥150mL | mRS 0–3, aRR | N/A | Explicit non-estimable result; no numerical test supplied | Direct p.40 N/A and could-not-be-evaluated footnote matched; no finite numerical result asserted. MRI exclusion changes sensitivity population, so no equality to CTP/MRI primary rows assumed. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4044 | ≥150mL | mRS 5–6, aRR | 0.83 (0.56–1.23) | C/O/D; null in | Direct p.40 row matched; CTP-only sensitivity and nested cutoff recognized; containment/order/outcome direction reconcile. Own-effect P absent; printed null boundary alone is not C005 narrative significance. C002/C003 context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |

## eTable 5 — REPORT physical p.41

[Exact source](../../../joi240006supp5_prod_1708623115.01733.pdf#page=41). Within-arm as-treated population EVT 170/MM 166. Outcomes 90 days. Ordinal descriptions EVT median 4 (IQR3–6), MM5 (4–6); binary counts mRS0–2 34/170 (20.0%)/12/166 (7.2%); mRS0–3 66/170 (38.8%)/30/166 (18.1%); mRS5–6 77/170 (45.3%)/101/166 (60.8%). All percentages reconcile. No crude-count calculation recreates a per-10mL adjusted slope.

| S ID | Outcome; volume per10mL | Arm/test | Printed estimate (95% CI) or P | Pass-1 check | Pass-2 check | State |
|---|---|---|---|---|---|---|
| S4045 | mRS; CT hypodensity | EVT aGenOR | 0.95 (0.93–0.98) | C/O/D; null out | Direct p.41 within-arm adjusted per10mL effect matched; containment/order and adverse/favorable outcome direction reconcile. As-treated170/166 counts reconcile. No own-effect P; interaction P not its test. C005 boundary rule applies only if a corresponding significant test is asserted. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4046 | mRS; CT hypodensity | MM aGenOR | 0.98 (0.95–1.00) | C/O/D; printed boundary1.00 | Direct p.41 within-arm adjusted per10mL effect matched; containment/order and adverse/favorable outcome direction reconcile. As-treated170/166 counts reconcile. No own-effect P; interaction P not its test. C005 boundary rule applies only if a corresponding significant test is asserted. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4047 | mRS; CT hypodensity | Interaction | P=.14 | Heterogeneity nonsignificant; own-arm CI not its test | Direct p.41 interaction P matched and within[0,1]; contrasts heterogeneity, not either arm association. Independent-slope reconstruction is diagnostic and does not reproduce this combined-model display; coefficient/nuisance/covariance mapping absent; exclusion rechecked. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4048 | mRS; composite | EVT aGenOR | 0.92 (0.88–0.95) | C/O/D; null out | Direct p.41 within-arm adjusted per10mL effect matched; containment/order and adverse/favorable outcome direction reconcile. As-treated170/166 counts reconcile. No own-effect P; interaction P not its test. C005 boundary rule applies only if a corresponding significant test is asserted. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4049 | mRS; composite | MM aGenOR | 0.95 (0.92–0.98) | C/O/D; null out | Direct p.41 within-arm adjusted per10mL effect matched; containment/order and adverse/favorable outcome direction reconcile. As-treated170/166 counts reconcile. No own-effect P; interaction P not its test. C005 boundary rule applies only if a corresponding significant test is asserted. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4050 | mRS; composite | Interaction | P=.13 | Heterogeneity nonsignificant; own-arm CI not its test | Direct p.41 interaction P matched and within[0,1]; contrasts heterogeneity, not either arm association. Independent-slope reconstruction is diagnostic and does not reproduce this combined-model display; coefficient/nuisance/covariance mapping absent; exclusion rechecked. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4051 | mRS0–2; CT hypodensity | EVT aRR | 0.93 (0.89–0.98) | C/O/D; null out | Direct p.41 within-arm adjusted per10mL effect matched; containment/order and adverse/favorable outcome direction reconcile. As-treated170/166 counts reconcile. No own-effect P; interaction P not its test. C005 boundary rule applies only if a corresponding significant test is asserted. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4052 | mRS0–2; CT hypodensity | MM aRR | 0.97 (0.87–1.09) | C/O/D; null in | Direct p.41 within-arm adjusted per10mL effect matched; containment/order and adverse/favorable outcome direction reconcile. As-treated170/166 counts reconcile. No own-effect P; interaction P not its test. C005 boundary rule applies only if a corresponding significant test is asserted. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4053 | mRS0–2; CT hypodensity | Interaction | P=.53 | Heterogeneity nonsignificant; no coefficient/test mapping supplied | Direct p.41 interaction P matched and within[0,1]; contrasts heterogeneity, not either arm association. Independent-slope reconstruction is diagnostic and does not reproduce this combined-model display; coefficient/nuisance/covariance mapping absent; exclusion rechecked. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4054 | mRS0–2; composite | EVT aRR | 0.87 (0.82–0.93) | C/O/D; null out | Direct p.41 within-arm adjusted per10mL effect matched; containment/order and adverse/favorable outcome direction reconcile. As-treated170/166 counts reconcile. No own-effect P; interaction P not its test. C005 boundary rule applies only if a corresponding significant test is asserted. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4055 | mRS0–2; composite | MM aRR | 0.93 (0.83–1.05) | C/O/D; null in | Direct p.41 within-arm adjusted per10mL effect matched; containment/order and adverse/favorable outcome direction reconcile. As-treated170/166 counts reconcile. No own-effect P; interaction P not its test. C005 boundary rule applies only if a corresponding significant test is asserted. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4056 | mRS0–2; composite | Interaction | P=.82 | Independent-slope Wald diagnostic differs; combined-model mapping absent | Direct p.41 interaction P matched and within[0,1]; contrasts heterogeneity, not either arm association. Independent-slope reconstruction is diagnostic and does not reproduce this combined-model display; coefficient/nuisance/covariance mapping absent; exclusion rechecked. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4057 | mRS0–3; CT hypodensity | EVT aRR | 0.97 (0.91–1.03) | C/O/D; null in | Direct p.41 within-arm adjusted per10mL effect matched; containment/order and adverse/favorable outcome direction reconcile. As-treated170/166 counts reconcile. No own-effect P; interaction P not its test. C005 boundary rule applies only if a corresponding significant test is asserted. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4058 | mRS0–3; CT hypodensity | MM aRR | 0.97 (0.91–1.03) | C/O/D; null in | Direct p.41 within-arm adjusted per10mL effect matched; containment/order and adverse/favorable outcome direction reconcile. As-treated170/166 counts reconcile. No own-effect P; interaction P not its test. C005 boundary rule applies only if a corresponding significant test is asserted. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4059 | mRS0–3; CT hypodensity | Interaction | P=.32 | Identical displayed separate slopes; combined interaction mapping absent | Direct p.41 interaction P matched and within[0,1]; contrasts heterogeneity, not either arm association. Independent-slope reconstruction is diagnostic and does not reproduce this combined-model display; coefficient/nuisance/covariance mapping absent; exclusion rechecked. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4060 | mRS0–3; composite | EVT aRR | 0.91 (0.85–0.98) | C/O/D; null out | Direct p.41 within-arm adjusted per10mL effect matched; containment/order and adverse/favorable outcome direction reconcile. As-treated170/166 counts reconcile. No own-effect P; interaction P not its test. C005 boundary rule applies only if a corresponding significant test is asserted. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4061 | mRS0–3; composite | MM aRR | 0.91 (0.85–0.98) | C/O/D; null out | Direct p.41 within-arm adjusted per10mL effect matched; containment/order and adverse/favorable outcome direction reconcile. As-treated170/166 counts reconcile. No own-effect P; interaction P not its test. C005 boundary rule applies only if a corresponding significant test is asserted. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4062 | mRS0–3; composite | Interaction | P=.82 | Identical displayed separate slopes; combined interaction mapping absent | Direct p.41 interaction P matched and within[0,1]; contrasts heterogeneity, not either arm association. Independent-slope reconstruction is diagnostic and does not reproduce this combined-model display; coefficient/nuisance/covariance mapping absent; exclusion rechecked. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4063 | mRS5–6; CT hypodensity | EVT aRR | 1.04 (1.02–1.07) | C/O/D; null out | Direct p.41 within-arm adjusted per10mL effect matched; containment/order and adverse/favorable outcome direction reconcile. As-treated170/166 counts reconcile. No own-effect P; interaction P not its test. C005 boundary rule applies only if a corresponding significant test is asserted. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4064 | mRS5–6; CT hypodensity | MM aRR | 1.03 (1.01–1.05) | C/O/D; null out | Direct p.41 within-arm adjusted per10mL effect matched; containment/order and adverse/favorable outcome direction reconcile. As-treated170/166 counts reconcile. No own-effect P; interaction P not its test. C005 boundary rule applies only if a corresponding significant test is asserted. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4065 | mRS5–6; CT hypodensity | Interaction | P=.76 | Heterogeneity nonsignificant; own-arm CI not its test | Direct p.41 interaction P matched and within[0,1]; contrasts heterogeneity, not either arm association. Independent-slope reconstruction is diagnostic and does not reproduce this combined-model display; coefficient/nuisance/covariance mapping absent; exclusion rechecked. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4066 | mRS5–6; composite | EVT aRR | 1.03 (1.00–1.05) | C/O/D; printed boundary1.00 | Direct p.41 within-arm adjusted per10mL effect matched; containment/order and adverse/favorable outcome direction reconcile. As-treated170/166 counts reconcile. No own-effect P; interaction P not its test. C005 boundary rule applies only if a corresponding significant test is asserted. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4067 | mRS5–6; composite | MM aRR | 1.01 (1.00–1.03) | C/O/D; printed boundary1.00 | Direct p.41 within-arm adjusted per10mL effect matched; containment/order and adverse/favorable outcome direction reconcile. As-treated170/166 counts reconcile. No own-effect P; interaction P not its test. C005 boundary rule applies only if a corresponding significant test is asserted. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4068 | mRS5–6; composite | Interaction | P=.63 | Heterogeneity nonsignificant; own-arm CI not its test | Direct p.41 interaction P matched and within[0,1]; contrasts heterogeneity, not either arm association. Independent-slope reconstruction is diagnostic and does not reproduce this combined-model display; coefficient/nuisance/covariance mapping absent; exclusion rechecked. | PASS_1_COMPLETE; PASS_2_COMPLETE |

## eTable 6 — REPORT physical p.42

[Exact source](../../../joi240006supp5_prod_1708623115.01733.pdf#page=42). Model explanatory comparison, study population; no treatment contrast is claimed by these criteria. All four imaging models separately include age/NIHSS/timing. Sample count per model and fit outputs are not printed; no artificial treatment covariate is added. Each complete model comparison below preserves all four modality values in source order ASPECTS, CT hypodensity, CTP/MRI, composite.

| S ID | Outcome | All AIC values | All BIC values | Pass-1 check | Pass-2 check | State |
|---|---|---|---|---|---|---|
| S4069 | Ordinal mRS; ordinal logistic | 417.2590;412.6195;403.2944;398.6922 | 447.8850;443.2454;433.9203;429.3182 | Composite minimum both; BIC improvements18.5668,13.9272,4.6021: very strong,very strong,positive; all four AUC NA | Direct p.42 all four AIC/BIC pairs reread; composite minimizes both criteria; BIC differences reproduce supplied preference tiers. No treatment contrast/test inferred. Explicit ordinal-logistic criteria analysis is distinct from PIM; C003 prespecification context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4070 | mRS0–2 | 256.9212;252.1431;239.4032;236.5431 | 276.0068;271.2287;258.4887;255.6287 | Composite minimum both; BIC improvements20.3781,15.6000,2.8600: very strong,very strong,positive | Direct p.42 all four AIC/BIC pairs reread; composite minimizes both criteria; BIC differences reproduce supplied preference tiers. No treatment contrast/test inferred. Explicit ordinal-logistic criteria analysis is distinct from PIM; C003 prespecification context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4071 | mRS0–3 | 358.6683;352.1023;329.0319;324.2519 | 377.7538;371.1878;348.1174;343.3374 | Composite minimum both; BIC improvements34.4164,27.8504,4.7800: very strong,very strong,positive | Direct p.42 all four AIC/BIC pairs reread; composite minimizes both criteria; BIC differences reproduce supplied preference tiers. No treatment contrast/test inferred. Explicit ordinal-logistic criteria analysis is distinct from PIM; C003 prespecification context retained. | PASS_1_COMPLETE; PASS_2_COMPLETE |

| S ID | Outcome; modality | AUC (95% CI) | Pass-1 check | Pass-2 check | State |
|---|---|---|---|---|---|
| S4072 | mRS0–2; ASPECTS | .7106 (.6343–.7870) | C/O/D; within0–1; no comparative P | Direct p.42 AUC and endpoints matched; estimate contained, endpoints ordered within[0,1]; composite remains maximum for this outcome. No AUC-difference P/SE is printed; CI overlap is not a test of predictive differences. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4073 | mRS0–2; CT hypodensity | .7224 (.6481–.7968) | C/O/D; within0–1; no comparative P | Direct p.42 AUC and endpoints matched; estimate contained, endpoints ordered within[0,1]; composite remains maximum for this outcome. No AUC-difference P/SE is printed; CI overlap is not a test of predictive differences. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4074 | mRS0–2; CTP/MRI | .7716 (.7062–.8370) | C/O/D; within0–1; no comparative P | Direct p.42 AUC and endpoints matched; estimate contained, endpoints ordered within[0,1]; composite remains maximum for this outcome. No AUC-difference P/SE is printed; CI overlap is not a test of predictive differences. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4075 | mRS0–2; composite | .7783 (.7103–.8463) | C/O/D; maximum AUC; no significance of AUC difference claimed | Direct p.42 AUC and endpoints matched; estimate contained, endpoints ordered within[0,1]; composite remains maximum for this outcome. No AUC-difference P/SE is printed; CI overlap is not a test of predictive differences. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4076 | mRS0–3; ASPECTS | .7500 (.6937–.8062) | C/O/D; within0–1; no comparative P | Direct p.42 AUC and endpoints matched; estimate contained, endpoints ordered within[0,1]; composite remains maximum for this outcome. No AUC-difference P/SE is printed; CI overlap is not a test of predictive differences. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4077 | mRS0–3; CT hypodensity | .7522 (.6965–.8079) | C/O/D; within0–1; no comparative P | Direct p.42 AUC and endpoints matched; estimate contained, endpoints ordered within[0,1]; composite remains maximum for this outcome. No AUC-difference P/SE is printed; CI overlap is not a test of predictive differences. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4078 | mRS0–3; CTP/MRI | .7952 (.7454–.8450) | C/O/D; within0–1; no comparative P | Direct p.42 AUC and endpoints matched; estimate contained, endpoints ordered within[0,1]; composite remains maximum for this outcome. No AUC-difference P/SE is printed; CI overlap is not a test of predictive differences. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4079 | mRS0–3; composite | .7977 (.7472–.8482) | C/O/D; maximum AUC; no significance of AUC difference claimed | Direct p.42 AUC and endpoints matched; estimate contained, endpoints ordered within[0,1]; composite remains maximum for this outcome. No AUC-difference P/SE is printed; CI overlap is not a test of predictive differences. | PASS_1_COMPLETE; PASS_2_COMPLETE |

## eTable 7 — REPORT physical pp.43–44

[First definition](../../../joi240006supp5_prod_1708623115.01733.pdf#page=43), [second definition and adjustment footnote](../../../joi240006supp5_prod_1708623115.01733.pdf#page=44). Population as treated, within EVT/MM; 90-day outcomes, mismatch versus no mismatch. First threshold groups EVT34/136, MM40/126; second threshold EVT112/58, MM99/67. All denominators partition170/166 and all printed count percentages reconcile. Each row identifies its own scale/null; last-column tests remain distinct relationships.

| S ID | Definition; outcome | Arm/measure | Printed estimate (95% CI) or last-column value | Pass-1 check | Pass-2 check | State |
|---|---|---|---|---|---|---|
| S4080 | ≥10mL/≥1.2; mRS | EVT aGenOR | .77 (.50–1.17) | C/O/D; null in | Direct pp.43–44 adjusted mismatch/no-mismatch cell matched; estimate contained, limits ordered and own-scale direction coherent. Count partitions reconcile170/166; crude count contrast is not adjusted effect. Distinct composite profiles do not supply C01650/100mL analysis. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4081 | ≥10mL/≥1.2; mRS | MM aGenOR | .69 (.46–1.05) | C/O/D; null in | Direct pp.43–44 adjusted mismatch/no-mismatch cell matched; estimate contained, limits ordered and own-scale direction coherent. Count partitions reconcile170/166; crude count contrast is not adjusted effect. Distinct composite profiles do not supply C01650/100mL analysis. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4082 | ≥10mL/≥1.2; mRS | Last-column interaction | .73 | Distinct heterogeneity contrast; no row-effect P assumed | Direct pp.43–44 last-column value matched and within[0,1]; supplied methods identify heterogeneity contrast, not RR/RD effect P. Composite profile is not planned50/100mL categorical analysis in C016; no additional conflict. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4083 | ≥10mL/≥1.2; mRS0–2 | EVT aRR | 1.02 (.48–2.15) | C/O/D; null in | Direct pp.43–44 adjusted mismatch/no-mismatch cell matched; estimate contained, limits ordered and own-scale direction coherent. Count partitions reconcile170/166; crude count contrast is not adjusted effect. Distinct composite profiles do not supply C01650/100mL analysis. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4084 | ≥10mL/≥1.2; mRS0–2 | EVT aRD | −.000 (−.155–.154) | C/O/D; null in; printed zero preserved | Direct p.43 signed-zero RD and ordered null-containing interval confirmed;−.000 retains printed zero. RR1.02 and signed zero are not established fixed transformations; notation exclusion reread, no significance/direction claim at zero. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4085 | ≥10mL/≥1.2; mRS0–2 | MM aRR | .63 (.20–1.94) | C/O/D; null in | Direct pp.43–44 adjusted mismatch/no-mismatch cell matched; estimate contained, limits ordered and own-scale direction coherent. Count partitions reconcile170/166; crude count contrast is not adjusted effect. Distinct composite profiles do not supply C01650/100mL analysis. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4086 | ≥10mL/≥1.2; mRS0–2 | MM aRD | −.034 (−.123–.056) | C/O/D; null in | Direct pp.43–44 adjusted mismatch/no-mismatch cell matched; estimate contained, limits ordered and own-scale direction coherent. Count partitions reconcile170/166; crude count contrast is not adjusted effect. Distinct composite profiles do not supply C01650/100mL analysis. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4087 | ≥10mL/≥1.2; mRS0–2 | Last-column interaction | .47 | Distinct heterogeneity contrast; no row-effect P assumed | Direct pp.43–44 last-column value matched and within[0,1]; supplied methods identify heterogeneity contrast, not RR/RD effect P. Composite profile is not planned50/100mL categorical analysis in C016; no additional conflict. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4088 | ≥10mL/≥1.2; mRS0–3 | EVT aRR | .77 (.48–1.26) | C/O/D; null in | Direct pp.43–44 adjusted mismatch/no-mismatch cell matched; estimate contained, limits ordered and own-scale direction coherent. Count partitions reconcile170/166; crude count contrast is not adjusted effect. Distinct composite profiles do not supply C01650/100mL analysis. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4089 | ≥10mL/≥1.2; mRS0–3 | EVT aRD | −.097 (−.263–.070) | C/O/D; null in | Direct pp.43–44 adjusted mismatch/no-mismatch cell matched; estimate contained, limits ordered and own-scale direction coherent. Count partitions reconcile170/166; crude count contrast is not adjusted effect. Distinct composite profiles do not supply C01650/100mL analysis. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4090 | ≥10mL/≥1.2; mRS0–3 | MM aRR | .68 (.33–1.38) | C/O/D; null in | Direct pp.43–44 adjusted mismatch/no-mismatch cell matched; estimate contained, limits ordered and own-scale direction coherent. Count partitions reconcile170/166; crude count contrast is not adjusted effect. Distinct composite profiles do not supply C01650/100mL analysis. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4091 | ≥10mL/≥1.2; mRS0–3 | MM aRD | −.064 (−.184–.055) | C/O/D; null in | Direct pp.43–44 adjusted mismatch/no-mismatch cell matched; estimate contained, limits ordered and own-scale direction coherent. Count partitions reconcile170/166; crude count contrast is not adjusted effect. Distinct composite profiles do not supply C01650/100mL analysis. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4092 | ≥10mL/≥1.2; mRS0–3 | Last-column interaction | .79 | Distinct heterogeneity contrast; no row-effect P assumed | Direct pp.43–44 last-column value matched and within[0,1]; supplied methods identify heterogeneity contrast, not RR/RD effect P. Composite profile is not planned50/100mL categorical analysis in C016; no additional conflict. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4093 | ≥10mL/≥1.2; mRS5–6 | EVT aRR | 1.31 (.80–2.15) | C/O/D; null in | Direct pp.43–44 adjusted mismatch/no-mismatch cell matched; estimate contained, limits ordered and own-scale direction coherent. Count partitions reconcile170/166; crude count contrast is not adjusted effect. Distinct composite profiles do not supply C01650/100mL analysis. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4094 | ≥10mL/≥1.2; mRS5–6 | EVT aRD | .127 (−.039–.293) | C/O/D; null in | Direct pp.43–44 adjusted mismatch/no-mismatch cell matched; estimate contained, limits ordered and own-scale direction coherent. Count partitions reconcile170/166; crude count contrast is not adjusted effect. Distinct composite profiles do not supply C01650/100mL analysis. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4095 | ≥10mL/≥1.2; mRS5–6 | MM aRR | 1.29 (.93–1.79) | C/O/D; null in; paired inference F-ST1-401 | Direct p.43 printed RR/RD pair confirmed; ratio includes1 and RD excludes0. F-ST1-401 already screened CONDITIONAL_OR_UNREPORTED: distinct adjusted scales, no own-effect P/common confidence identity. No same-display reproducing method establishes routeA4; no re-emission. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4096 | ≥10mL/≥1.2; mRS5–6 | MM aRD | .168 (.011–.325) | C/O/D; null out; paired inference F-ST1-401 | Direct p.43 printed RR/RD pair confirmed; ratio includes1 and RD excludes0. F-ST1-401 already screened CONDITIONAL_OR_UNREPORTED: distinct adjusted scales, no own-effect P/common confidence identity. No same-display reproducing method establishes routeA4; no re-emission. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4097 | ≥10mL/≥1.2; mRS5–6 | Last-column interaction | .83 | Interaction is not S4096 effect P | Direct pp.43–44 last-column value matched and within[0,1]; supplied methods identify heterogeneity contrast, not RR/RD effect P. Composite profile is not planned50/100mL categorical analysis in C016; no additional conflict. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4098 | ≥15mL/≥1.8; mRS | EVT aGenOR | .76 (.50–1.18) | C/O/D; null in | Direct pp.43–44 adjusted mismatch/no-mismatch cell matched; estimate contained, limits ordered and own-scale direction coherent. Count partitions reconcile170/166; crude count contrast is not adjusted effect. Distinct composite profiles do not supply C01650/100mL analysis. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4099 | ≥15mL/≥1.8; mRS | MM aGenOR | .73 (.53–1.02) | C/O/D; null in | Direct pp.43–44 adjusted mismatch/no-mismatch cell matched; estimate contained, limits ordered and own-scale direction coherent. Count partitions reconcile170/166; crude count contrast is not adjusted effect. Distinct composite profiles do not supply C01650/100mL analysis. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4100 | ≥15mL/≥1.8; mRS | Last-column interaction | .88 | Distinct heterogeneity contrast; no row-effect P assumed | Direct pp.43–44 last-column value matched and within[0,1]; supplied methods identify heterogeneity contrast, not RR/RD effect P. Composite profile is not planned50/100mL categorical analysis in C016; no additional conflict. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4101 | ≥15mL/≥1.8; mRS0–2 | EVT aRR | .60 (.30–1.21) | C/O/D; null in | Direct pp.43–44 adjusted mismatch/no-mismatch cell matched; estimate contained, limits ordered and own-scale direction coherent. Count partitions reconcile170/166; crude count contrast is not adjusted effect. Distinct composite profiles do not supply C01650/100mL analysis. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4102 | ≥15mL/≥1.8; mRS0–2 | EVT aRD | −.099 (−.224–.027) | C/O/D; null in | Direct pp.43–44 adjusted mismatch/no-mismatch cell matched; estimate contained, limits ordered and own-scale direction coherent. Count partitions reconcile170/166; crude count contrast is not adjusted effect. Distinct composite profiles do not supply C01650/100mL analysis. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4103 | ≥15mL/≥1.8; mRS0–2 | MM aRR | .44 (.15–1.26) | C/O/D; null in | Direct pp.43–44 adjusted mismatch/no-mismatch cell matched; estimate contained, limits ordered and own-scale direction coherent. Count partitions reconcile170/166; crude count contrast is not adjusted effect. Distinct composite profiles do not supply C01650/100mL analysis. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4104 | ≥15mL/≥1.8; mRS0–2 | MM aRD | −.061 (−.144–.022) | C/O/D; null in | Direct p.44 cell matched in native extraction and exact-source rendering; estimate contained in ordered null-containing CI. Named adjusted scale and contrast preserved; no own-effect P/common confidence identity supplied. Apparent inventory/source alignment concern not reproduced. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4105 | ≥15mL/≥1.8; mRS0–2 | Last-column interaction | .76 | Distinct heterogeneity contrast; no row-effect P assumed | Direct pp.43–44 last-column value matched and within[0,1]; supplied methods identify heterogeneity contrast, not RR/RD effect P. Composite profile is not planned50/100mL categorical analysis in C016; no additional conflict. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4106 | ≥15mL/≥1.8; mRS0–3 | EVT aRR | .81 (.55–1.21) | C/O/D; null in | Direct p.44 cell matched in native extraction and exact-source rendering; estimate contained in ordered null-containing CI. Named adjusted scale and contrast preserved; no own-effect P/common confidence identity supplied. Apparent inventory/source alignment concern not reproduced. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4107 | ≥15mL/≥1.8; mRS0–3 | EVT aRD | −.076 (−.228–.075) | C/O/D; null in | Direct p.44 cell matched in native extraction and exact-source rendering; estimate contained in ordered null-containing CI. Named adjusted scale and contrast preserved; no own-effect P/common confidence identity supplied. Apparent inventory/source alignment concern not reproduced. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4108 | ≥15mL/≥1.8; mRS0–3 | MM aRR | .66 (.38–1.14) | C/O/D; null in | Direct p.44 cell matched in native extraction and exact-source rendering; estimate contained in ordered null-containing CI. Named adjusted scale and contrast preserved; no own-effect P/common confidence identity supplied. Apparent inventory/source alignment concern not reproduced. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4109 | ≥15mL/≥1.8; mRS0–3 | MM aRD | −.091 (−.202–.020) | C/O/D; null in | Direct p.44 cell matched in native extraction and exact-source rendering; estimate contained in ordered null-containing CI. Named adjusted scale and contrast preserved; no own-effect P/common confidence identity supplied. Apparent inventory/source alignment concern not reproduced. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4110 | ≥15mL/≥1.8; mRS0–3 | Last-column interaction | .68 | Distinct heterogeneity contrast; no row-effect P assumed | Direct pp.43–44 last-column value matched and within[0,1]; supplied methods identify heterogeneity contrast, not RR/RD effect P. Composite profile is not planned50/100mL categorical analysis in C016; no additional conflict. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4111 | ≥15mL/≥1.8; mRS5–6 | EVT aRR | 1.09 (.74–1.61) | C/O/D; null in | Direct p.44 cell matched in native extraction and exact-source rendering; estimate contained in ordered null-containing CI. Named adjusted scale and contrast preserved; no own-effect P/common confidence identity supplied. Apparent inventory/source alignment concern not reproduced. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4112 | ≥15mL/≥1.8; mRS5–6 | EVT aRD | .068 (−.088–.224) | C/O/D; null in | Direct p.44 cell matched in native extraction and exact-source rendering; estimate contained in ordered null-containing CI. Named adjusted scale and contrast preserved; no own-effect P/common confidence identity supplied. Apparent inventory/source alignment concern not reproduced. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4113 | ≥15mL/≥1.8; mRS5–6 | MM aRR | 1.21 (.94–1.56) | C/O/D; null in | Direct p.44 cell matched in native extraction and exact-source rendering; estimate contained in ordered null-containing CI. Named adjusted scale and contrast preserved; no own-effect P/common confidence identity supplied. Apparent inventory/source alignment concern not reproduced. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4114 | ≥15mL/≥1.8; mRS5–6 | MM aRD | .121 (−.017–.260) | C/O/D; null in | Direct p.44 cell matched in native extraction and exact-source rendering; estimate contained in ordered null-containing CI. Named adjusted scale and contrast preserved; no own-effect P/common confidence identity supplied. Apparent inventory/source alignment concern not reproduced. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S4115 | ≥15mL/≥1.8; mRS5–6 | Last-column interaction | .79 | Distinct heterogeneity contrast; no row-effect P assumed | Direct pp.43–44 last-column value matched and within[0,1]; supplied methods identify heterogeneity contrast, not RR/RD effect P. Composite profile is not planned50/100mL categorical analysis in C016; no additional conflict. | PASS_1_COMPLETE; PASS_2_COMPLETE |

## Coverage and definition limits

All 115 assigned relationships have PASS_1_COMPLETE. Every printed estimate-CI has its own S ID. Each distinct interaction/last-column test has its own S ID. All 12 criteria rows and four ordinal-AUC NAs are retained in three complete model-comparison records; both unestimated eTable4 binary cells remain explicit. No sampling, top-N selection or candidate-count target was applied.

No scientific coverage gap. Definition limits: no raw data, fit covariance, exact RD construction, row-effect P values or AUC-CI method; eTable7 lacks arm/last-column headings locally, with arm identity and interaction meaning recovered from supplied denominator/method context. These limits restrict reproduction of exact fitted coefficients/test statistics, not coverage. One finding is emitted for the printed paired-scale inference issue; apparent issues not meeting threshold appear once in the checker artifact's excluded-observations table.

## Independent pass-2 source comparison

Direct REPORT p.44 source reading and a current source-page rendering confirm the current source transcriptions for all second-profile rows. A provisional reviewer concern about p.44 cell alignment was compared mechanically with the saved inventory and not reproduced: each proposed before/current cell was identical. No inventory source-value correction was therefore required. This concern concerns the review transcription, not the supplied paper. None changes F-ST1-401 at S4095/S4096, any screened finding, or C001–C018 evidence/classification.

All 115 records have explicit PASS_1_COMPLETE and PASS_2_COMPLETE. Limits persist: no row-specific fit output, raw model rows, numerical SE/covariance, exact RD/interaction/AUC confidence construction. All supplied relationships were reviewed despite these definition limits. No assigned table states a superiority margin, noninferiority/equivalence claim, multiplicity/interim/stopping decision; none is inferred. C002/C003 governing-analysis questions, C016 different categorical primary specification, and C018 separate discordant-profile counts are reconciled as context rather than exported to unrelated rows.

Source reading: direct CPU Poppler26.01.0, `pdftotext -layout -f 39 -l 44 joi240006supp5_prod_1708623115.01733.pdf -`; method context main pp.3–4, results eMethods p.4, analysis SAP pp.4–7. One CPU direct source render was required for transcription confirmation: `pdftoppm -f 44 -l 44 -singlefile -r 120 -png joi240006supp5_prod_1708623115.01733.pdf .ai_paper_validation/review_1_6_2/preprocessing/stat2_tables_a/source-p44`; output preprocessing/stat2_tables_a/source-p44.png, engine Poppler26.01.0. No OCR/fallback invoked.
# Statistical relationship inventory — tables B, second-pass bounded shard

Mechanical source-linked split of first-pass statistics/parts/tables_b_plan.md. Scope: S5001–S5066, 66 inferential records, results eTables8–10/12. All first-pass evidence below is preserved unchanged. Fresh pass-2 agent adds its independent completion facts.

Fresh pass-2 runtime: root/stat2_tables_b; gpt-6.1-sol/high; FRESH_SPAWN. All 66 assigned records now have PASS_1_COMPLETE and PASS_2_COMPLETE. Exact source pp45–50/52, the complete current ledger, all screening decisions/justifications, and the complete source recheck were independently read. New findings: 0; C018 is reproduced and retained without re-emission. Checker details and exclusions: checkers/statistical_parts/pass2_tables_b.md. The original 120-record first-pass header below documents the parent artifact's historical scope; this current split contains only the 66 enumerated records.

# Statistical pass 1 inventory: tables B and plan methods

Fresh statistical shard: /root/stat1_tables_b_plan; model gpt-6.1-sol; reasoning high; FRESH_SPAWN. Scope: DOC-006 eTables8–13 physical pp45–53; DOC-003 entire protocol statistical-method and numerical decision-rule content; DOC-004 entire parent SAP statistical-method and numerical decision-rule content. Historical inferential statements are tracked as supplied PLAN facts, separately from SELECT2 outcomes. Main-report methods, DOC-005 and other result displays are separate assigned shards.

Read QUALITY_CONTROL_SCOPE.md and review_contract.md completely. Mapping aids: support_parts/results_b_admin.md, protocol.md and trial_sap_a.md/trial_sap_b.md. Final authority: direct Poppler layout extraction for DOC-003/006 and source-matched images for scanned DOC-004. Direct transient command pdftotext -layout -f N -l N source.pdf -. Visually read DOC-006 pp45–53; protocol pp13,80,81 and parent SAP pp10,11,12,16,40; existing mapper visual records cover other plan pages. No new derivative, Python, web or prior conclusions used. Reused sources/assets preserved. CPU inspection; engine/version for reused renders recorded in evidence_asset_inventory.md, unrecorded legacy engine versions remain limitations.

120 records: S5001–S5120. Every displayed estimate/CI pair and interaction test in eTables8–10 is independent:24+6+10+6+10+6; eTable12 adds4. Plan methods/rules37; historical inferential pairs/tests17. A Bayesian threshold vector is one complete decision rule, with every row calculated independently within that record.

Shared table definitions:95%CI; ordinal ratio null1, binary RR null1, RD null0. eTable8 is within each received-treatment arm, profile versus concordant reference: concordant ASPECTS<6/core≥70mL, D1 ASPECTS<6/core<70, D2 ASPECTS6–10/core≥70. N163EVT/N156MM. eTable9 is randomized EVT-versus-MM treatment effect within CTP/MRI profile, eTable10 within composite-core profile. Interaction always compares treatment-effect modification across profiles. No individual effect-test P is supplied in those tables. N/A cells have no numerical estimate/test to enumerate.

Numeric context for matching: eTable8 FI:EVT32/163,MM10/156; concordant10/75 vs3/82; D1 21/76 vs7/63; D2 1/12 vs0/11. Ambulation62/163vs27/156;concordant18/75vs8/82;D1 41/76vs19/63;D2 3/12vs0/11. mRS5–6 75/163vs97/156;concordant42/75vs59/82;D1 25/76vs28/63;D2 8/12vs10/11. eTable9 FI MM/EVT concordant3/83vs10/74;D1 7/63vs21/76;D2 1/11vs0/12(N/A). Ambulation8/83vs18/74;19/63vs41/76;3/11vs0/12(N/A). mRS5–6 60/83vs41/74;28/63vs25/76;10/11vs8/12. eTable10 FI8/118vs18/112;2/28vs13/38;2/12vs0/14(N/A);ambulation19/118vs35/112;8/28vs24/38;4/12vs0/14(N/A);mRS5–6 74/118vs53/112;14/28vs13/38;11/12vs9/14. Cross-table FI/ambulation cell attribution is preserved for numeric/cross-source review, without assuming same analysis set.

Descriptive-only inspection: eTable11 MRI-follow-up groupsN101MM/24mTICI0–2a/79mTICI2b–3, medians(IQR)CTP/MRI95(56,135)/125(76,179)/68(37,142); composite63(22,102)/91(71,142)/45(16,90);CT69(31,122)/107(87,152)/60(24,110). Each median lies within ordered IQR, no inferential CI/test. eTable13 core minus follow-up:162−143=19,140−90=50,93−11=82mL; each exceeds≥10mL threshold. 'Significant' there explicitly means volume threshold, not an unstated P test. These displays have no omitted inferential estimate/test.

### S5001 — eTable8 ordinal D1 EVT

- Location/role: [DOC-006 physical p45](../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 0.91 (0.50,1.65)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms OR0.91 inside[.50,1.65], including1; D1-versus-concordant within EVT differs from across-arm treatment effects. No own-effect P; C002 supplies the population context.

### S5002 — eTable8 ordinal D1 MM

- Location/role: [DOC-006 physical p45](../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 1.50 (0.94,2.40)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms OR1.50 inside[.94,2.40], including1; MM within-arm D1 contrast has no own-effect P. Interaction.20 tests effect modification rather than this coefficient.

### S5003 — eTable8 ordinal D2 EVT

- Location/role: [DOC-006 physical p45](../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 1.01 (0.53,1.92)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms OR1.01 inside[.53,1.92], including1. D2 EVT ordinal effect can coexist with sparse favorable binary counts; C018 identifies separately conflicting cross-table attribution.

### S5004 — eTable8 ordinal D2 MM

- Location/role: [DOC-006 physical p45](../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 0.65 (0.43,0.99)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms OR.65 inside[.43,.99], excluding1 toward worse D2 MM outcome. Interaction.26 is not its own-effect P; MM6(6,6) supplies descriptive context, not an effect CI.

### S5005 — eTable8 mRS0–2 D1 EVT RR

- Location/role: [DOC-006 physical p45](../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.51 (0.16,1.56)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms RR.51 inside[.16,1.56], including1. Adjusted profile effect need not equal crude(21/76)/(10/75)=2.072; no method reproducing these adjusted rows from crude counts is established.

### S5006 — eTable8 mRS0–2 D1 EVT RD

- Location/role: [DOC-006 physical p45](../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD −0.055 (−0.201,0.092)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms RD−.055 inside[−.201,.092], including0; its sign agrees with paired adjusted RR.51. Do not replace adjustment with observed28%−13%=15 percentage points.

### S5007 — eTable8 mRS0–2 D1 MM RR

- Location/role: [DOC-006 physical p45](../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 1.26 (0.17,9.43)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms RR1.26 inside[.17,9.43], including1; positive adjusted D1 MM direction agrees with paired RD+.040. No matched own-effect test printed.

### S5008 — eTable8 mRS0–2 D1 MM RD

- Location/role: [DOC-006 physical p45](../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD 0.040 (−0.059,0.138)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms RD+.040 inside[−.059,.138], including0; same direction as RR1.26. Exact confidence/test reconstruction needs the absent fit and variance output.

### S5009 — eTable8 mRS0–2 D2 EVT RR

- Location/role: [DOC-006 physical p45](../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.85 (0.12,5.79)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms RR.85 inside[.12,5.79], including1; paired RD+.010 points oppositely. No shared fitted-risk pair, standardization or RD derivation is supplied, so a common-risk identity is not assumed.

### S5010 — eTable8 mRS0–2 D2 EVT RD

- Location/role: [DOC-006 physical p45](../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD 0.010 (−0.395,0.415)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms RD+.010 inside[−.395,.415], including0; paired RR.85 reverses point direction. The observed count1/12 remains separate from an adjusted estimand; missing RR/RD mapping is recorded without a new finding.

### S5011 — eTable8 mRS0–3 D1 EVT RR

- Location/role: [DOC-006 physical p45](../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.86 (0.43,1.71)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms RR.86 inside[.43,1.71], including1; paired RD+.043 on p46 reverses point direction. A shared fitted-risk identity is absent and cannot be inferred from similar-model wording.

### S5012 — eTable8 mRS0–3 D1 EVT RD

- Location/role: [DOC-006 physical p46](../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD 0.043 (−0.125,0.211)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RD+.043 inside[−.125,.211], including0; opposite paired RR.86 direction is the same conditional mapping observation, consolidated in the pass-2 exclusion table.

### S5013 — eTable8 mRS0–3 D1 MM RR

- Location/role: [DOC-006 physical p45](../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 1.24 (0.38,4.07)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms RR1.24 inside[.38,4.07], including1; positive direction agrees with RD+.060. MM19/63 and8/82 are descriptive risks, not replacements for the adjusted estimate.

### S5014 — eTable8 mRS0–3 D1 MM RD

- Location/role: [DOC-006 physical p46](../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD 0.060 (−0.075,0.196)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RD+.060 inside[−.075,.196], including0, agreeing in direction with RR1.24. Interaction.72 is a distinct contrast; no interval/test conflict is reproduced.

### S5015 — eTable8 mRS0–3 D2 EVT RR

- Location/role: [DOC-006 physical p46](../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 1.19 (0.43,3.28)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RR1.19 inside[.43,3.28], including1; paired RD−.065 reverses point direction. Source supplies no common RR/RD risk pair or transformation, so conditional identity is not promoted.

### S5016 — eTable8 mRS0–3 D2 EVT RD

- Location/role: [DOC-006 physical p46](../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD −0.065 (−0.421,0.291)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RD−.065 inside[−.421,.291], including0. Paired RR1.19 has opposing direction; the same missing-model-mapping observation is consolidated once.

### S5017 — eTable8 mRS5–6 D1 EVT RR

- Location/role: [DOC-006 physical p46](../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.92 (0.57,1.48)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RR.92 inside[.57,1.48], including1; lower adjusted D1 EVT adverse risk agrees with RD−.077. The25/76 crude proportion does not identify the adjusted risk.

### S5018 — eTable8 mRS5–6 D1 EVT RD

- Location/role: [DOC-006 physical p46](../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD −0.077 (−0.244,0.091)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RD−.077 inside[−.244,.091], including0 and agreeing with RR.92 direction. Effect-adjustment and own-effect variance remain unavailable.

### S5019 — eTable8 mRS5–6 D1 MM RR

- Location/role: [DOC-006 physical p46](../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.69 (0.49,0.97)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RR.69 inside[.49,.97], excluding1; paired RD−.076 includes0. Distinct adjusted scales/confidence constructions do not supply a matched interval-versus-own-test conflict under the complete screening rationale.

### S5020 — eTable8 mRS5–6 D1 MM RD

- Location/role: [DOC-006 physical p46](../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD −0.076 (−0.248,0.096)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RD−.076 inside[−.248,.096], including0. Paired RR.69 is directionally concordant but has different null inclusion; no shared confidence transform or own-effect P establishes a contradiction.

### S5021 — eTable8 mRS5–6 D2 EVT RR

- Location/role: [DOC-006 physical p46](../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 1.08 (0.69,1.68)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RR1.08 inside[.69,1.68], including1; positive direction agrees with RD+.143. D2 EVT8/12 adverse and3/12 ambulation do not exceed12.

### S5022 — eTable8 mRS5–6 D2 EVT RD

- Location/role: [DOC-006 physical p46](../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD 0.143 (−0.212,0.498)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RD+.143 inside[−.212,.498], including0; agrees with RR1.08 direction. Exact regression reconstruction requires absent covariate rows/fitted probabilities.

### S5023 — eTable8 mRS5–6 D2 MM RR

- Location/role: [DOC-006 physical p46](../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 1.28 (1.01,1.63)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RR1.28 inside[1.01,1.63], excluding1 toward greater D2 MM adverse risk. Paired RD+.324 excludes0 consistently; interaction.02 is separately defined.

### S5024 — eTable8 mRS5–6 D2 MM RD

- Location/role: [DOC-006 physical p46](../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD 0.324 (0.165,0.483)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RD+.324 inside[.165,.483], excluding0 in the same direction as RR1.28. eTable8 MM10/11 adverse plus0/11 favorable reconciles internally; C018 concerns competing eTables9/10 copies.

### S5025 — eTable8 interaction ordinal D1

- Location/role: [DOC-006 physical p45](../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=.20
- Checks/calculation: Tests treatment×imaging-profile effect modification, rather than either individual within-arm estimate's null. The printed heading establishes distinct contrast; no interval supplied for the interaction.
- Definitions/limits: Interaction coefficient/covariance/test statistic not supplied; do not infer a Wald test from the arm-specific intervals.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 identifies P=.20 as D1 ordinal treatment interaction. It is not the test for OR.91 or1.50; absent interaction covariance/coefficient prevents exact P reconstruction.

### S5026 — eTable8 interaction ordinal D2

- Location/role: [DOC-006 physical p45](../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=.26
- Checks/calculation: Tests treatment×imaging-profile effect modification, rather than either individual within-arm estimate's null. The printed heading establishes distinct contrast; no interval supplied for the interaction.
- Definitions/limits: Interaction coefficient/covariance/test statistic not supplied; do not infer a Wald test from the arm-specific intervals.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 identifies P=.26 as D2 ordinal treatment interaction, not the test for MM OR.65 excluding1. No interaction interval is printed to form its own interval/test conflict.

### S5027 — eTable8 interaction mRS0–2 D1

- Location/role: [DOC-006 physical p45](../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=.78
- Checks/calculation: Tests treatment×imaging-profile effect modification, rather than either individual within-arm estimate's null. The printed heading establishes distinct contrast; no interval supplied for the interaction.
- Definitions/limits: Interaction coefficient/covariance/test statistic not supplied; do not infer a Wald test from the arm-specific intervals.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 identifies P=.78 as D1 functional-independence interaction, not an individual EVT/MM profile effect P. No test statistic or covariance supplies an exact numerical comparison.

### S5028 — eTable8 interaction mRS0–3 D1

- Location/role: [DOC-006 physical p45](../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=.72
- Checks/calculation: Tests treatment×imaging-profile effect modification, rather than either individual within-arm estimate's null. The printed heading establishes distinct contrast; no interval supplied for the interaction.
- Definitions/limits: Interaction coefficient/covariance/test statistic not supplied; do not infer a Wald test from the arm-specific intervals.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 identifies P=.72 as D1 ambulation interaction. The different point directions in RR/RD do not establish an interaction coefficient; no own interaction CI is supplied.

### S5029 — eTable8 interaction mRS5–6 D1

- Location/role: [DOC-006 physical p46](../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=.14
- Checks/calculation: Tests treatment×imaging-profile effect modification, rather than either individual within-arm estimate's null. The printed heading establishes distinct contrast; no interval supplied for the interaction.
- Definitions/limits: Interaction coefficient/covariance/test statistic not supplied; do not infer a Wald test from the arm-specific intervals.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 identifies P=.14 as D1 mRS5–6 interaction. An MM RR CI below1 beside.14 is a different contrast, so the apparent interval/P conflict is not reproduced.

### S5030 — eTable8 interaction mRS5–6 D2

- Location/role: [DOC-006 physical p46](../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=.02
- Checks/calculation: Tests treatment×imaging-profile effect modification, rather than either individual within-arm estimate's null. The printed heading establishes distinct contrast; no interval supplied for the interaction.
- Definitions/limits: Interaction coefficient/covariance/test statistic not supplied; do not infer a Wald test from the arm-specific intervals.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 identifies P=.02 as D2 mRS5–6 interaction. It is significant at the main stated.05 level but no own interaction CI/statistic permits further numerical compatibility reproduction.

### S5031 — eTable9 ordinal concordant

- Location/role: [DOC-006 physical p47](../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 1.60 (1.18,2.18)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 confirms OR1.60 inside[1.18,2.18], excluding1 toward better EVT ordinal outcome. Randomized within-profile comparison is distinct from eTable8 as-treated within-arm contrast, with C002 retained.

### S5032 — eTable9 ordinal D1

- Location/role: [DOC-006 physical p47](../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 1.87 (1.28,2.74)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 confirms OR1.87 inside[1.28,2.74], excluding1; P=.66 belongs to D1 interaction rather than this treatment contrast. Point containment/order and better-EVT direction reconcile.

### S5033 — eTable9 ordinal D2

- Location/role: [DOC-006 physical p47](../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 2.46 (1.14,5.32)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 confirms OR2.46 inside[1.14,5.32], excluding1. Better EVT ordinal outcome can involve shifts within poor categories despite printed zero favorable events; C018 retains the separate event-attribution issue.

### S5034 — eTable9 mRS0–2 concordant

- Location/role: [DOC-006 physical p47](../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 4.62 (1.27,16.71)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 confirms RR4.62 inside[1.27,16.71], excluding1 for EVT functional independence.10/74 versus3/83 is descriptive support; adjusted RR is not required to equal its crude ratio.

### S5035 — eTable9 mRS0–2 D1

- Location/role: [DOC-006 physical p47](../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 2.68 (1.25,5.76)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 confirms RR2.68 inside[1.25,5.76], excluding1 for D1 EVT functional independence; interaction.56 tests between-profile modification, not this effect.

### S5036 — eTable9 mRS0–3 concordant

- Location/role: [DOC-006 physical p47](../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 2.98 (1.44,6.17)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 confirms RR2.98 inside[1.44,6.17], excluding1 for concordant-profile EVT ambulation. No own-effect P or standard error is supplied; count-based crude replacement is unsupported.

### S5037 — eTable9 mRS0–3 D1

- Location/role: [DOC-006 physical p47](../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 1.90 (1.29,2.78)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 confirms RR1.90 inside[1.29,2.78], excluding1 for D1 EVT ambulation; interaction.38 is a separate contrast. Endpoint order and direction agree.

### S5038 — eTable9 mRS5–6 concordant

- Location/role: [DOC-006 physical p47](../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.76 (0.61,0.95)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 confirms RR.76 inside[.61,.95], excluding1 toward lower EVT adverse risk. C018's D2 mismatch does not justify a numerical replacement for this concordant adjusted estimate.

### S5039 — eTable9 mRS5–6 D1

- Location/role: [DOC-006 physical p48](../../../joi240006supp5_prod_1708623115.01733.pdf#page=48); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.72 (0.49,1.05)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p48 confirms RR.72 inside[.49,1.05], including1 for D1 adverse risk; interaction.83 is separately labeled. No same-effect statistical conclusion conflicts.

### S5040 — eTable9 mRS5–6 D2

- Location/role: [DOC-006 physical p48](../../../joi240006supp5_prod_1708623115.01733.pdf#page=48); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.59 (0.37,0.96)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p48 confirms RR.59 inside[.37,.96], excluding1 for D2 adverse risk; interaction.40 is not its own P. C018 recheck reproduces MM3+10>11 in this same profile but does not determine an amended fitted RR.

### S5041 — eTable9 interaction ordinal D1

- Location/role: [DOC-006 physical p47](../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.66
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 identifies ordinal D1 interaction P=.66. Across-arm OR intervals cannot reconstruct it without pooled-model covariance; no explicit interaction statistic is supplied.

### S5042 — eTable9 interaction ordinal D2

- Location/role: [DOC-006 physical p47](../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.18
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 identifies ordinal D2 interaction P=.18. The OR2.46 CI excluding1 tests a different effect, and C018 count issues do not supply an alternative interaction value.

### S5043 — eTable9 interaction mRS0–2 D1

- Location/role: [DOC-006 physical p47](../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.56
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 identifies independence D1 interaction P=.56. It is not the test for RR2.68; no matched interaction interval, covariance or statistic is available.

### S5044 — eTable9 interaction mRS0–3 D1

- Location/role: [DOC-006 physical p47](../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.38
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 identifies ambulation D1 interaction P=.38. It is not the test for RR1.90; no new interval/test conflict is reproduced.

### S5045 — eTable9 interaction mRS5–6 D1

- Location/role: [DOC-006 physical p48](../../../joi240006supp5_prod_1708623115.01733.pdf#page=48); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.83
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p48 identifies D1 adverse interaction P=.83; RR.72 is a within-D1 treatment effect. Both printed contrasts are distinct; covariance and exact test definition are absent.

### S5046 — eTable9 interaction mRS5–6 D2

- Location/role: [DOC-006 physical p48](../../../joi240006supp5_prod_1708623115.01733.pdf#page=48); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.40
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p48 identifies D2 adverse interaction P=.40, not the test for RR.59 whose CI excludes1. C018 is preserved without substituting count-derived interaction inference.

### S5047 — eTable10 ordinal concordant

- Location/role: [DOC-006 physical p49](../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 1.65 (1.26,2.16)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 confirms OR1.65 inside[1.26,2.16], excluding1 for concordant composite-profile EVT benefit. C003 addresses planned composite hierarchy; no additional estimate conflict is supplied.

### S5048 — eTable10 ordinal D1

- Location/role: [DOC-006 physical p49](../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 1.80 (1.00,3.22)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 confirms OR1.80 inside[1.00,3.22], containing printed null1. No own-effect P or significant narrative is paired with it, so this endpoint alone is not a category1 finding; interaction.61 is distinct.

### S5049 — eTable10 ordinal D2

- Location/role: [DOC-006 physical p49](../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 2.66 (1.34,5.28)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 confirms OR2.66 inside[1.34,5.28], excluding1. Composite D2 ordinal improvement remains possible within poor mRS categories; C018 concerns disjoint favorable/adverse counts, not this estimate's containment.

### S5050 — eTable10 mRS0–2 concordant

- Location/role: [DOC-006 physical p49](../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 2.88 (1.34,6.20)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 confirms RR2.88 inside[1.34,6.20], excluding1 for concordant composite-profile EVT independence; crude18/112 versus8/118 is not an adjusted-model reproduction.

### S5051 — eTable10 mRS0–2 D1

- Location/role: [DOC-006 physical p49](../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 3.71 (0.93,14.82)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 confirms RR3.71 inside[.93,14.82], including1 for composite D1 independence. No significant own-effect statement is printed, and interaction.71 is another contrast.

### S5052 — eTable10 mRS0–3 concordant

- Location/role: [DOC-006 physical p49](../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 2.21 (1.41,3.48)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 confirms RR2.21 inside[1.41,3.48], excluding1 for concordant composite-profile ambulation. C003 hierarchy provenance remains separate from the numerically coherent interval.

### S5053 — eTable10 mRS0–3 D1

- Location/role: [DOC-006 physical p49](../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 1.83 (1.04,3.22)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 confirms RR1.83 inside[1.04,3.22], excluding1 for composite D1 ambulation. P=.68 is the interaction and does not contradict this within-stratum interval.

### S5054 — eTable10 mRS5–6 concordant

- Location/role: [DOC-006 physical p49](../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.75 (0.60,0.92)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 confirms RR.75 inside[.60,.92], excluding1 toward lower concordant-profile EVT adverse risk. Count comparison is descriptive; no own-effect P, statistic or standard error printed.

### S5055 — eTable10 mRS5–6 D1

- Location/role: [DOC-006 physical p50](../../../joi240006supp5_prod_1708623115.01733.pdf#page=50); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.90 (0.52,1.56)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p50 confirms RR.90 inside[.52,1.56], including1 for composite D1 adverse risk. Interaction.92 is distinct; no matched test conflict.

### S5056 — eTable10 mRS5–6 D2

- Location/role: [DOC-006 physical p50](../../../joi240006supp5_prod_1708623115.01733.pdf#page=50); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.59 (0.39,0.88)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p50 confirms RR.59 inside[.39,.88], excluding1 for composite D2 adverse risk. Recheck C018 reproduces MM4+11>12 and2+11>12; this source count pattern is already screened and no fitted replacement is inferred.

### S5057 — eTable10 interaction ordinal D1

- Location/role: [DOC-006 physical p49](../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.61
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 identifies composite ordinal D1 interaction P=.61; CI1.00–3.22 is for the within-D1 effect. No own interaction interval/statistic exists.

### S5058 — eTable10 interaction ordinal D2

- Location/role: [DOC-006 physical p49](../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.13
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 identifies composite ordinal D2 interaction P=.13. CI1.34–5.28 is for the treatment effect, so the apparent interval/P mismatch uses different contrasts.

### S5059 — eTable10 interaction mRS0–2 D1

- Location/role: [DOC-006 physical p49](../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.71
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 identifies composite independence D1 interaction P=.71. The RR3.71 interval is not an interaction interval; supplied summary values cannot reconstruct pooled covariance.

### S5060 — eTable10 interaction mRS0–3 D1

- Location/role: [DOC-006 physical p49](../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.68
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 identifies composite ambulation D1 interaction P=.68, distinct from RR1.83 whose interval excludes1. No same-analysis interval/test conflict is reproduced.

### S5061 — eTable10 interaction mRS5–6 D1

- Location/role: [DOC-006 physical p50](../../../joi240006supp5_prod_1708623115.01733.pdf#page=50); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.92
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p50 identifies composite D1 adverse interaction P=.92. It is not the null test for RR.90; coefficient/covariance/test statistic remain absent.

### S5062 — eTable10 interaction mRS5–6 D2

- Location/role: [DOC-006 physical p50](../../../joi240006supp5_prod_1708623115.01733.pdf#page=50); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.38
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p50 identifies composite D2 adverse interaction P=.38, distinct from RR.59 whose interval excludes1. C018 counts remain registered without inventing their inferential effect.

### S5063 — eTable12 CTP/MRI growth by independence

- Location/role: [DOC-006 physical p52](../../../joi240006supp5_prod_1708623115.01733.pdf#page=52); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: mRS3–6 N290:102(61–167); mRS0–2 N46:45(32–88); P<.001
- Checks/calculation: Two disjoint outcome groups each sum to336. All medians lie inside ordered IQRs; IQR is not a treatment-effect CI, so no interval/P contradiction follows. Direction: greater growth with worse function.
- Definitions/limits: Rank-sum data/test statistic and exact tested statistic are absent on the table page; summary quantiles do not reproduce a rank-sum P. No unsupported normal approximation used.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p52 confirms290+46=336, medians102/45 inside ordered IQR61–167/32–88, and P<.001. The quantiles are IQRs, not effect CIs; ranks/statistic needed for exact P are absent.

### S5064 — eTable12 composite growth by independence

- Location/role: [DOC-006 physical p52](../../../joi240006supp5_prod_1708623115.01733.pdf#page=52); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: mRS3–6 N290:77(31–127); mRS0–2 N46:23.5(11–48); P<.001
- Checks/calculation: Two disjoint outcome groups each sum to336. All medians lie inside ordered IQRs; IQR is not a treatment-effect CI, so no interval/P contradiction follows. Direction: greater growth with worse function.
- Definitions/limits: Rank-sum data/test statistic and exact tested statistic are absent on the table page; summary quantiles do not reproduce a rank-sum P. No unsupported normal approximation used.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p52 confirms290+46=336, composite medians77/23.5 inside IQR31–127/11–48, P<.001. Direction agrees with greater growth in dependence; no CI/test pairing is supplied.

### S5065 — eTable12 CTP/MRI growth by ambulation

- Location/role: [DOC-006 physical p52](../../../joi240006supp5_prod_1708623115.01733.pdf#page=52); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: mRS4–6 N240:110.5(65.5–174.5); mRS0–3 N96:65.5(32.5–100.5); P<.001
- Checks/calculation: Two disjoint outcome groups each sum to336. All medians lie inside ordered IQRs; IQR is not a treatment-effect CI, so no interval/P contradiction follows. Direction: greater growth with worse function.
- Definitions/limits: Rank-sum data/test statistic and exact tested statistic are absent on the table page; summary quantiles do not reproduce a rank-sum P. No unsupported normal approximation used.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p52 confirms240+96=336, medians110.5/65.5 inside IQR65.5–174.5/32.5–100.5, P<.001. Overlap of IQRs does not contradict a between-group test.

### S5066 — eTable12 composite growth by ambulation

- Location/role: [DOC-006 physical p52](../../../joi240006supp5_prod_1708623115.01733.pdf#page=52); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: mRS4–6 N240:85.5(36–144); mRS0–3 N96:31.5(10–67); P<.001
- Checks/calculation: Two disjoint outcome groups each sum to336. All medians lie inside ordered IQRs; IQR is not a treatment-effect CI, so no interval/P contradiction follows. Direction: greater growth with worse function.
- Definitions/limits: Rank-sum data/test statistic and exact tested statistic are absent on the table page; summary quantiles do not reproduce a rank-sum P. No unsupported normal approximation used.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p52 confirms240+96=336, composite medians85.5/31.5 inside IQR36–144/10–67, P<.001. Full ranked data/test output is needed for numerical P reconstruction; no unsupported normal approximation is used.


# Statistical relationship inventory — plan methods, second-pass bounded shard

Mechanical source-linked split of first-pass statistics/parts/tables_b_plan.md. Scope: S5067–S5120, 54 inferential and statistical-design records. All first-pass evidence and complete Bayesian calculation facts below are preserved unchanged. Fresh pass-2 agent adds its independent completion facts.

# Statistical pass 1 inventory: tables B and plan methods

Fresh statistical shard: /root/stat1_tables_b_plan; model gpt-6.1-sol; reasoning high; FRESH_SPAWN. Scope: DOC-006 eTables8–13 physical pp45–53; DOC-003 entire protocol statistical-method and numerical decision-rule content; DOC-004 entire parent SAP statistical-method and numerical decision-rule content. Historical inferential statements are tracked as supplied PLAN facts, separately from SELECT2 outcomes. Main-report methods, DOC-005 and other result displays are separate assigned shards.

Read QUALITY_CONTROL_SCOPE.md and review_contract.md completely. Mapping aids: support_parts/results_b_admin.md, protocol.md and trial_sap_a.md/trial_sap_b.md. Final authority: direct Poppler layout extraction for DOC-003/006 and source-matched images for scanned DOC-004. Direct transient command pdftotext -layout -f N -l N source.pdf -. Visually read DOC-006 pp45–53; protocol pp13,80,81 and parent SAP pp10,11,12,16,40; existing mapper visual records cover other plan pages. No new derivative, Python, web or prior conclusions used. Reused sources/assets preserved. CPU inspection; engine/version for reused renders recorded in evidence_asset_inventory.md, unrecorded legacy engine versions remain limitations.

120 records: S5001–S5120. Every displayed estimate/CI pair and interaction test in eTables8–10 is independent:24+6+10+6+10+6; eTable12 adds4. Plan methods/rules37; historical inferential pairs/tests17. A Bayesian threshold vector is one complete decision rule, with every row calculated independently within that record.

Shared table definitions:95%CI; ordinal ratio null1, binary RR null1, RD null0. eTable8 is within each received-treatment arm, profile versus concordant reference: concordant ASPECTS<6/core≥70mL, D1 ASPECTS<6/core<70, D2 ASPECTS6–10/core≥70. N163EVT/N156MM. eTable9 is randomized EVT-versus-MM treatment effect within CTP/MRI profile, eTable10 within composite-core profile. Interaction always compares treatment-effect modification across profiles. No individual effect-test P is supplied in those tables. N/A cells have no numerical estimate/test to enumerate.

Numeric context for matching: eTable8 FI:EVT32/163,MM10/156; concordant10/75 vs3/82; D1 21/76 vs7/63; D2 1/12 vs0/11. Ambulation62/163vs27/156;concordant18/75vs8/82;D1 41/76vs19/63;D2 3/12vs0/11. mRS5–6 75/163vs97/156;concordant42/75vs59/82;D1 25/76vs28/63;D2 8/12vs10/11. eTable9 FI MM/EVT concordant3/83vs10/74;D1 7/63vs21/76;D2 1/11vs0/12(N/A). Ambulation8/83vs18/74;19/63vs41/76;3/11vs0/12(N/A). mRS5–6 60/83vs41/74;28/63vs25/76;10/11vs8/12. eTable10 FI8/118vs18/112;2/28vs13/38;2/12vs0/14(N/A);ambulation19/118vs35/112;8/28vs24/38;4/12vs0/14(N/A);mRS5–6 74/118vs53/112;14/28vs13/38;11/12vs9/14. Cross-table FI/ambulation cell attribution is preserved for numeric/cross-source review, without assuming same analysis set.

Descriptive-only inspection: eTable11 MRI-follow-up groupsN101MM/24mTICI0–2a/79mTICI2b–3, medians(IQR)CTP/MRI95(56,135)/125(76,179)/68(37,142); composite63(22,102)/91(71,142)/45(16,90);CT69(31,122)/107(87,152)/60(24,110). Each median lies within ordered IQR, no inferential CI/test. eTable13 core minus follow-up:162−143=19,140−90=50,93−11=82mL; each exceeds≥10mL threshold. 'Significant' there explicitly means volume threshold, not an unstated P test. These displays have no omitted inferential estimate/test.

### S5067 — Discordance superiority rule

- Location/role: [DOC-003 physical p22](../../../joi240006supp2_prod_1708623114.99233.pdf#page=22); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Prior EVT good-outcome rates 48% vs32%; planned15 percentage-point margin; logistic OR95%CI for discordant imaging comparison (p51); diagram p71.
- Checks/calculation: 48−32=16 percentage points. No executed margin decision supplied. p51 repeats same profile in two word orders, while p22, second p51 paragraph and diagram clearly identify two opposite profiles. Excluded wording observation.
- Definitions/limits: Margin-to-OR decision mapping lacks executed result; no generic preference asserted.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Direct protocol pp.22,51 confirm 16-point historical separation and prospective15-point margin; comparison profiles are immediately identifiable despite repeated wording. No executed OR-to-margin conclusion is supplied; exclusions remain wording/missing implementation, not a numerical superiority conclusion.

### S5068 — Functional-independence hierarchy

- Location/role: [DOC-003 physical p37](../../../joi240006supp2_prod_1708623114.99233.pdf#page=37); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: p8/p37: second primary=mRS0–2 at90days. p50: secondary endpoint=mRS0–2 at90days. DOC004p13/p17: secondary.
- Checks/calculation: Same outcome/time receives primary and secondary status inside one dated protocol. F-ST1-502; PLAN/PLAN, P_P.
- Definitions/limits: Status discrepancy directly affects planned hierarchy.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Exact protocol pp.37,50 and SAP pp.13,17 reproduce primary-versus-secondary status for the same90-day mRS0–2 endpoint. C010 and its Route A category5 provenance cover this pattern; PLAN-only P_P classification retained.

### S5069 — Protocol primary analysis

- Location/role: [DOC-003 physical p45](../../../joi240006supp2_prod_1708623114.99233.pdf#page=45); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: ITT90-day mRS; normal-approximation WMW/GLR; additional generalizedCMH stratified by randomization factors; age,NIHSS,time,core called continuous.
- Checks/calculation: Overall and adjusted rank-based comparisons are separately defined. Continuous stratification language lacks implementation but no numerical contradiction supplied.
- Definitions/limits: Stratum construction and tie/rank implementation missing; generic omission excluded.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Protocol p.45 names normal-WMW overall and additional generalized-CMH adjustment separately. Continuous-covariate language omits implementation but supplies no conflicting adjusted statistic. No test, strata or variance structure inferred.

### S5070 — Adaptive population partition

- Location/role: [DOC-003 physical p45](../../../joi240006supp2_prod_1708623114.99233.pdf#page=45); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: G1A/B: ASPECTS3–5/core<50; G2A/B: ASPECTS6–10/core≥50; G3A/B: ASPECTS3–5/core≥50. A0–12h/B12–24h. Five cumulative subgroups; DOC004p9 matches.
- Checks/calculation: Imaging definitions partition eligible population; five cumulative alternatives plus overall match J6. No observed boundary-time duplicate enrollment supplied.
- Definitions/limits: Unstated handling of exactly12hours does not establish numerical conflict.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Direct protocol p.45 and SAP p.9 confirm six disjoint imaging/time groups and five cumulative alternatives plus overall J=6. Exactly12h assignment is unreported without an observed duplicate count; no numeric population inconsistency.

### S5071 — Projected distributions and standardized effect

- Location/role: [DOC-003 physical p46](../../../joi240006supp2_prod_1708623114.99233.pdf#page=46); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: EVT mRS0–6:4,8,12,16,19,13,28%; MM:1,4,9,14,19,10,43%; effect.34; DOC004pp10–11 repeats.
- Checks/calculation: Both sums100%. Diagnostic half-tie WMW=.59375; sqrt(12)*(.59375−.5)=.324760. Difference from.34 less than5% before rounding; no finding.
- Definitions/limits: Standardized effect and tie-variance definition absent; diagnostic is not ASSISTant reproduction.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Both seven-cell projected distributions independently sum100%. Half-tie superiority=.59375 and untied normal standardization=.32475953 are diagnostic only; .34 versus that diagnostic differs4.48% and does not clear precision threshold.

### S5072 — Sample size and power

- Location/role: [DOC-003 physical p46](../../../joi240006supp2_prod_1708623114.99233.pdf#page=46); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: FixedN376=188/arm; power90%, alpha5% in protocol; DOC004p11 one-sided.025. Additional184 gives adaptive560; interim200/380; adaptive91%power/effect.34/one-sided.025.
- Checks/calculation: Arithmetic reproduces. Diagnostic N=4*(1.959964+1.281552)^2/.34^2=363.579. Effect[.335,.345],power[.895,.905],alpha[.0245,.0255] yields approximateN349–379, overlapping376±.5; exactWMW/simulation not reconstructed.
- Definitions/limits: Protocol fixed alpha sidedness absent; two-sided.05/one-sided.025 share critical z.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; 376=188+188 and376+184=560 reproduce;560−380=180. Diagnostic normal fixed N363.57865 is not ASSISTant/WMW reproduction; first-pass half-unit input bounds349–379 overlap printed376. One-sided.025 and unspecified protocol.05 do not establish calibration conflict.

### S5073 — First interim tree

- Location/role: [DOC-003 physical p47](../../../joi240006supp2_prod_1708623114.99233.pdf#page=47); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: N200 completed90-day. Overall neither→continue; efficacy→stop; futility→select/test subgroup. Selected neither→restrict; efficacy→stop; futility→stop. DOC004pp9–10 repeats.
- Checks/calculation: All branches defined; maximum560, with smaller available analyzedN after enrichment.
- Definitions/limits: No realized interim statistic or relaxed-bound formula supplied.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Direct protocol p.47/SAP p.9 specify every first-look overall/selected efficacy/futility/continue branch. Actual first200-patient continuation is disclosed atSAP p.12 without an observed statistic to reverse the decision.

### S5074 — Second interim tree

- Location/role: [DOC-003 physical p47](../../../joi240006supp2_prod_1708623114.99233.pdf#page=47); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: N380 completed90-day. Overall repeats first tree; selected neither→180 additional; efficacy→stop; futility→stop. DOC004p10 matches.
- Checks/calculation: 560−380=180; both accrual scenarios specified.
- Definitions/limits: No executed N380 decision supplied.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Second-look two-scenario tree matches protocol pp.47–48 and SAP p.10; additional180=560−380. No executed380-patient rule supplied; do not substitute300 review for this scheduled branch (C014).

### S5075 — Final tree

- Location/role: [DOC-003 physical p48](../../../joi240006supp2_prod_1708623114.99233.pdf#page=48); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Protocolp48 overall560: failure→select/test subgroup; previously selected→test selected. DOC004p10 tests overall or selected and otherwise declares not superior.
- Checks/calculation: Later SAP does not restate overall-failure rescue branch. Actual trial stopped at300 (p12). Apparent final-branch observation excluded because no executed result supplied.
- Definitions/limits: CONDITIONAL_OR_UNREPORTED; preserve both dated descriptions.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Direct protocol p.48 explicitly allows final subgroup selection/test after overall failure; SAP p.10 explicitly declares not superior on failed final efficacy test and p.40 states the overall final boundary. This is a printed planned primary decision-rule difference, not merely absent executed data: F-ST2-601; version/relevance ambiguity retained.

### S5076 — Adaptive simulation scenario 0

- Location/role: [DOC-003 physical p49](../../../joi240006supp2_prod_1708623114.99233.pdf#page=49); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: 0,0,0,0,0,0; mean0; adaptiveN426,power2.0%; fixed560,power2.5%; DOC004p11; weights.14,.06,.14,.06,.42,.18; 5000trials.
- Checks/calculation: Weighted mean0; null rates within2.5%; futility59.1%/N426 context coherent. Weights sum1; all expectedN≤560.
- Definitions/limits: Simulation code/seed not supplied. Normal calculations explicitly diagnostic.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Six zero effects yield weighted mean0; weights sum1; null2.0% adaptive/2.5% fixed and expected426≤560 reconcile. Simulation code/seed unavailable; observed trial statistics not substituted.

### S5077 — Adaptive simulation scenario 1

- Location/role: [DOC-003 physical p49](../../../joi240006supp2_prod_1708623114.99233.pdf#page=49); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: .32,.32,.32,.32,.32,.32; mean.32; adaptive376,86.0%; fixed560,95.8%; DOC004p11; weights.14,.06,.14,.06,.42,.18; 5000trials.
- Checks/calculation: Mean.32; diagnostic normal fixed power≈.958; printed copies match. Weights sum1; all expectedN≤560.
- Definitions/limits: Simulation code/seed not supplied. Normal calculations explicitly diagnostic.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Six.32 effects yield weighted.32; expected376≤560. Fixed95.8% versus adaptive86.0% with smaller expectedN is coherent; normal-power diagnostic about.958 only, not simulation-code reproduction.

### S5078 — Adaptive simulation scenario 2

- Location/role: [DOC-003 physical p49](../../../joi240006supp2_prod_1708623114.99233.pdf#page=49); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: .3,.3,.3,.3,.3,.3; mean.3; adaptive393,81.1%; fixed560,93.3%; DOC004p11; weights.14,.06,.14,.06,.42,.18; 5000trials.
- Checks/calculation: Mean.3; diagnostic normal power≈.944 differs<5% from.933, not an exact simulation calculation. Weights sum1; all expectedN≤560.
- Definitions/limits: Simulation code/seed not supplied. Normal calculations explicitly diagnostic.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Six.30 effects yield weighted.30; expected393≤560. Fixed93.3% versus adaptive81.1% is internally allowed; a normal diagnostic about.944 is within relative5%, without claiming exact simulation reproduction.

### S5079 — Adaptive simulation scenario 3

- Location/role: [DOC-003 physical p49](../../../joi240006supp2_prod_1708623114.99233.pdf#page=49); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: .4,.4,.4,.4,0,0; mean.16; adaptive500,74.1%; fixed560,45.7%; DOC004p11; weights.14,.06,.14,.06,.42,.18; 5000trials.
- Checks/calculation: Weighted mean.4*.4=.16. Weights sum1; all expectedN≤560.
- Definitions/limits: Simulation code/seed not supplied. Normal calculations explicitly diagnostic.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Weighted mean .4*(.14+.06+.14+.06)=.16; adaptiveN500≤560. Printed45.7% fixed/74.1% adaptive preserve distinct designs; no cross-design equivalence assumed.

### S5080 — Adaptive simulation scenario 4

- Location/role: [DOC-003 physical p49](../../../joi240006supp2_prod_1708623114.99233.pdf#page=49); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: .4,.4,.4,.4,−.1,−.1; mean.1; adaptive502,78.5%; fixed560:21.2%protocol/51.2%SAP; DOC004p11; weights.14,.06,.14,.06,.42,.18; 5000trials.
- Checks/calculation: Weighted mean.4*.4−.1*.6=.10. Same supplied input row; fixed powers differ beyond precision. F-ST1-503. Weights sum1; all expectedN≤560.
- Definitions/limits: Simulation code/seed not supplied. Normal calculations explicitly diagnostic.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Exact protocol p.49/SAP p.11 confirm scenario4fixed21.2%/51.2%, equal other displayed inputs. Complete screen records F-ST1-503 PERIPHERAL_COMPARISON; no duplicate finding. This alternative operating-characteristic output does not supply observed rejection or changed sample-size input.

### S5081 — Adaptive simulation scenario 5

- Location/role: [DOC-003 physical p49](../../../joi240006supp2_prod_1708623114.99233.pdf#page=49); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: .4,.4,.3,.3,0,−.1; mean.122; adaptive513,67.1%; fixed560,29.2%; DOC004p11; weights.14,.06,.14,.06,.42,.18; 5000trials.
- Checks/calculation: Weighted mean.4*.2+.3*.2−.1*.18=.122. Weights sum1; all expectedN≤560.
- Definitions/limits: Simulation code/seed not supplied. Normal calculations explicitly diagnostic.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Weighted mean .4*.20+.3*.20−.1*.18=.122; expected513≤560, fixed29.2%/adaptive67.1% distinct design outputs. No interval/test or count conflict.

### S5082 — Adaptive simulation scenario 6

- Location/role: [DOC-003 physical p49](../../../joi240006supp2_prod_1708623114.99233.pdf#page=49); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: .5,.5,0,0,0,0; mean.1; adaptive503,70.6%; fixed560,21.2%; DOC004p11; weights.14,.06,.14,.06,.42,.18; 5000trials.
- Checks/calculation: Weighted mean.5*.2=.10. Weights sum1; all expectedN≤560.
- Definitions/limits: Simulation code/seed not supplied. Normal calculations explicitly diagnostic.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Weighted mean .5*(.14+.06)=.10; expected503≤560. Fixed21.2% and adaptive70.6% are distinct algorithms, not paired estimates/tests.

### S5083 — Adaptive simulation scenario 7

- Location/role: [DOC-003 physical p49](../../../joi240006supp2_prod_1708623114.99233.pdf#page=49); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: .5,0,0,0,0,0; mean.07; adaptive503,60.5%; fixed560,12.8%; DOC004p11; weights.14,.06,.14,.06,.42,.18; 5000trials.
- Checks/calculation: Weighted mean.5*.14=.07. Weights sum1; all expectedN≤560.
- Definitions/limits: Simulation code/seed not supplied. Normal calculations explicitly diagnostic.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Weighted mean .5*.14=.07; expected503≤560. Fixed12.8% versus adaptive60.5% concerns concentrated alternative; coherent with separate designs, no reproducible conflict.

### S5084 — Minimization algorithm

- Location/role: [DOC-003 physical p78](../../../joi240006supp2_prod_1708623114.99233.pdf#page=78); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Gk=ΣwfIk; variance reduction2ΣwfNk/(K−1)+constant; choose minimum. Protocol weights4,4,3,3,2,blank,1,1 for age,NIHSS,clot,time,core,mismatch,hemisphere,center. SAPp37:3,4,3,3,4,2,2,1 plusASPECTS3; p79/SAPp38 T2probabilities.9/.5/.1.
- Checks/calculation: Probability.9 favors lower imbalance, tie.5 and opposite.1. Later SAP refines factors and weights. No realized allocation discrepancy. Blank weight alone excluded.
- Definitions/limits: No allocation/raw-data audit; later values retained by version.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Direct protocol pp.78–79/SAP pp.37–38 confirm minimum-imbalance assignment with probabilities.9/.5/.1; updates to factor weights are explicit in later plan. Blank protocol mismatch weight lacks executed allocation contradiction; no raw randomization audit.

### S5085 — Primary missing-outcome rules

- Location/role: [DOC-003 physical p52](../../../joi240006supp2_prod_1708623114.99233.pdf#page=52); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Protocol90±15day nominalvisit; retrieveclinic/phone60–120days then ordinal-logisticMI. SAPp16 MAR,30imputations,Rubin pooling/tipping point; ITT352p14.
- Checks/calculation: Broader retrieval window is explicit; later SAP adds MI detail. No executed conflicting imputation calculation.
- Definitions/limits: Exact predictor list absent, generic omission excluded.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Protocol p.52 defines broader60–120-day recovery before ordinal MI; SAP p.16 adds MAR,30imputations and Rubin pooling/tipping analysis. Parent352 ITT versus imaging336 is eligibility subset context, not same-population count conflict; no imputed patient output supplied.

### S5086 — Early-window safety

- Location/role: [DOC-003 physical p55](../../../joi240006supp2_prod_1708623114.99233.pdf#page=55); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Protocolpp55–56 MM mortality increase>20%vsEVT→hold enrollment pendingDSMB.
- Checks/calculation: Absolute/relative scale unspecified but no executed safety decision supplied.
- Definitions/limits: CONDITIONAL_OR_UNREPORTED for missing20%scale alone.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Direct pp.55–56 place hold on MMmortality increase>20% pending DSMB; absolute/relative scale absent. No observed triggering value/test conflicts; isolated missing scale remains conditional rather than an implemented stopping conclusion.

### S5087 — Bayesian sICH ≤100cc

- Location/role: [DOC-003 physical p58](../../../joi240006supp2_prod_1708623114.99233.pdf#page=58); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: N50,100,150,200,250; inclusive triggers24,44,63,82,101 throughN. PriorBeta(.35,.65); posterior Pr(p>.35)>.95; then Pr(EVT>MM+.10)>.95.
- Checks/calculation: PosteriorBeta(.35+s,.65+N−s). Exact incomplete-beta minima24,44,63,82,101; all reproduce.
- Definitions/limits: Step2 has no observed paired data; not assumed executed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Every ≤100cc sICH trigger independently recomputed using source Beta(.35,.65) posterior; minima24/44/63/82/101 atN50/100/150/200/250 all reproduce. Step2requires paired event data not supplied.

### S5088 — Bayesian sICH >100cc

- Location/role: [DOC-003 physical p59](../../../joi240006supp2_prod_1708623114.99233.pdf#page=59); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: N20,30,40,50,60,70,80,90,100; lower limits11,16,20,24,28,32,36,40,44. Beta(.35,.65);Pr(p>.35)>.95; thenEVT>MM+.10 probability>.95.
- Checks/calculation: Exact incomplete-beta minima11,16,20,24,28,32,36,40,44 reproduce.
- Definitions/limits: Numerical integration of stated beta posterior; no normal approximation.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Every >100cc sICH trigger independently recomputed:11/16/20/24/28/32/36/40/44 atN20–100; predecessor tails≤.95 and minima tails>.95. Exact source rows match.

### S5089 — Bayesian sICH extracranialICA

- Location/role: [DOC-003 physical p60](../../../joi240006supp2_prod_1708623114.99233.pdf#page=60); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: N20,30,40,50,60,70,80,90,100; lower limits11,16,20,24,28,32,36,40,44. Beta(.35,.65);Pr(p>.35)>.95; step2EVT>MM+.10 probability>.95.
- Checks/calculation: Same exact minima reproduce every printed row.
- Definitions/limits: Source-specific scope retained, not double counted as independent cause.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; ExtracranialICA sICH vector independently checked with same stated posterior and source pp.59–60; all nine minima match, with scope maintained separately. No executed event series.

### S5090 — Bayesian mortality ≤100cc

- Location/role: [DOC-003 physical p61](../../../joi240006supp2_prod_1708623114.99233.pdf#page=61); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: N50,100,150,200,250; lower limits26,49,71,92,113. Beta(.4,.6);Pr(p>.4)>.95; step2EVT>MM+.10 probability>.95.
- Checks/calculation: Exact minima26,49,71,92,113 reproduce.
- Definitions/limits: No executed step2 comparison supplied.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; ≤100cc mortality vector independently recomputed under Beta(.4,.6):26/49/71/92/113 atN50/100/150/200/250; every minimum and predecessor verifies the>.95 rule.

### S5091 — Bayesian mortality >100cc

- Location/role: [DOC-003 physical p62](../../../joi240006supp2_prod_1708623114.99233.pdf#page=62); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: N20,30,40,50,60,70,80,90,100; printed lower limits12,17,22,26,32,35,40,44,49. Beta(.4,.6);Pr(p>.4)>.95.
- Checks/calculation: Exact minima12,17,22,26,31,35,40,44,49. N60,s31 tail.9644096>.95;32vs31 differs3.125% and count half-unit intervals touch. Excluded display precision.
- Definitions/limits: Step2EVT>MM+.10 probability>.95; no executed data supplied.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; AtN60 the stated beta rule reaches>.95 with31events(tail.964409556), predecessor30=.938913247; source threshold32. Exact integer relative difference1/32=.03125≤.05 and half-unit intervals touch; display rule screens this apparent difference. Remaining eight rows reproduce.

### S5092 — Bayesian mortality extracranialICA

- Location/role: [DOC-003 physical p63](../../../joi240006supp2_prod_1708623114.99233.pdf#page=63); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: N20,30,40,50,60,70,80,90,100; printed lower limits12,17,22,26,32,35,40,44,49; Beta(.4,.6),Pr(p>.4)>.95.
- Checks/calculation: Same minima12,17,22,26,31,35,40,44,49; same N60 observation consolidated in excluded row, relative discrepancy≤5%.
- Definitions/limits: Step2 conditional comparison supplied without observed event data.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; ExtracranialICA mortality repeats the sameN60 threshold32/minimum31 pattern and is consolidated withS5091; all other eight rows reproduce. No interval-versus-ownP or same-display relative>.05 discrepancy; rounding exclusion retained.

### S5093 — Appendix direction and theta

- Location/role: [DOC-003 physical p81](../../../joi240006supp2_prod_1708623114.99233.pdf#page=81); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Y=MMmRS,X=EVTmRS;H0P(Y≤X)=.5;HAP(Y≤X)=.5+theta;theta=(z.975+z.9)/sqrt(3*560)=.0791. EfficacyZ≥2.604/final≥2.772;futilitytildeZ≤−1.897. DOC004pp39–40 repeats.
- Checks/calculation: Theta=.07908489 reproduces. Positive alternative favors lower MM score rather than EVT; F-ST1-504. Rank-sum orientation also needs clarification.
- Definitions/limits: Hypothesis orientation is explicit, independent of unknown ranking/tie convention; actual stoppingZ absent.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Exact protocol pp.80–81/SAP pp.39–40 confirm positiveP(MM≤EVT)=.5+.0791 despite lower-mRS benefit; C013 covers direction and missing coding/ranks/ties. Independenttheta=.0790848815 reproduces. No operational Z or alpha inferred.

### S5094 — SAP300 stopping review

- Location/role: [DOC-004 physical p12](../../../joi240006supp3_prod_1708623114.99733.pdf#page=12); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: DOC004p12 planned200/380, requested300 review, no alteration/additional interim analyses; apply prespecified boundaries to30090-day cases and stop for efficacy;family-wise.05.
- Checks/calculation: Boundary application at300 differs from stated200/380 schedule, while claiming no alteration. F-ST1-505 asks which calibrated rule applies.
- Definitions/limits: Review and stop explicitly disclosed; no broad critique; .05vsone-sided.025 alone excluded.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; SAP pp.9,11–12,40 directly retain200/380 schedule and describe300-outcome boundary rejection with no added analysis. C014 covers missing information-time/boundary mapping; count differences cannot be rounding, but no alpha-violation claim made.

### S5095 — SAP ordinal merge

- Location/role: [DOC-004 physical p14](../../../joi240006supp3_prod_1708623114.99733.pdf#page=14); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Primary mRS5/6 mergedp14/p16 to avoid6→5 counting as success; anticipated distributionp10 has sevenlevels.
- Checks/calculation: Analysis definition and planning distribution are separate objects; no contradictory executed calculation supplied.
- Definitions/limits: Tie handling not assumed beyond source merger.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; SAP pp.14–16 explicitly merges mRS5/6 for treatment-success analyses. Planningseven-level distribution and descriptive full-scale graphics are distinct quantities; no absent-rank reconstruction or raw data claim.

### S5096 — SAP WMW transformations

- Location/role: [DOC-004 physical p16](../../../joi240006supp3_prod_1708623114.99733.pdf#page=16); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: WMW superiority95%CI/P;ARD described as probability EVTbetter, formulaARD=2(WMW−.5);NNT=1/ARD;WMW generalized odds95%CI.
- Checks/calculation: Explicit transformation identifies net comparative quantity. Descriptive probability wording apparent issue excluded; no executedARD supplied.
- Definitions/limits: TERMINOLOGY_OR_WORDING; generalized-odds/tie/CI formula absent.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; DirectSAP p.16 suppliesARD=2(WMW−.5) andNNT=1/ARD, making net contrast explicit. Probability wording alone does not change a supplied executed ARD; no result or interval/P conflict established. Terminology exclusion retained.

### S5097 — SAP functional independence

- Location/role: [DOC-004 physical p17](../../../joi240006supp3_prod_1708623114.99733.pdf#page=17); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: 90-daymRS0–2; derive indicator from imputedmRS, Rubin pooling; modifiedPoissonRR95%CI/P.
- Checks/calculation: Model/output and imputation linkage coherent.
- Definitions/limits: No executed estimate/test here.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; DirectSAP p.17 defines90-daymRS0–2, derived binary indicators from MIordinal scores, Rubin pooling and modifiedPoissonRR95%CI/P; coherent planned linkage. Hierarchy discrepancy belongsC010; imaging-specific population discrepancy belongsC002.

### S5098 — SAP independent ambulation

- Location/role: [DOC-004 physical p17](../../../joi240006supp3_prod_1708623114.99733.pdf#page=17); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: 90-daymRS0–3; same MI/Rubin; modifiedPoissonRR95%CI/P.
- Checks/calculation: Model/output and population/threshold coherent.
- Definitions/limits: No executed estimate/test here.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; DirectSAP p.17 defines90-daymRS0–3 with sameMI/Rubin/modPoisson planned approach; threshold nested within ordinal outcome and not confused with independence. No executed number here.

### S5099 — SAP binary safety/early improvement

- Location/role: [DOC-004 physical p18](../../../joi240006supp3_prod_1708623114.99733.pdf#page=18); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: sICH24h, worsening≥4NIHSS24h, all-cause death90days, improvement≥8orNIHSS0–1 at24h. Binary logisticMI30, mortalityderivedmRS; modifiedPoissonRR95%CI/Ppp18–21.
- Checks/calculation: Common analysis rule checked separately against each endpoint definition and missingness link; all explicit. Missing early-improvement hypothesis predicate resolved by surrounding binary comparison.
- Definitions/limits: Covariate/pooled-test detail unreported; no numerical conflict.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; DirectSAP pp.18–21 separately verifies sICH/worsening24h,mortality90d and improvement≥8orNIHSS0–1; binarylogisticMI and modifiedPoissonRR output are distinct steps. C015 retains PLAN-only4h/24h comparison; no REPORTwindow fabricated.

### S5100 — SAP descriptive methods

- Location/role: [DOC-004 physical p19](../../../joi240006supp3_prod_1708623114.99733.pdf#page=19); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Complications cumulativecounts/proportions; reperfusionmTICI≥2bEVTonly; neither hypothesistest norimputation. Discharge sixcategory proportions/noimputationp20.
- Checks/calculation: Descriptive analysis intentionally distinguished from tested binary outcomes; unnamed discharge test has no executedP supplied.
- Definitions/limits: Generic absent discharge test excluded.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; DirectSAP pp.19–20 defines proceduralcomplications/reperfusion as descriptive with no hypothesis/imputation; discharge has hypothesis but no named test. No executed dischargeP establishes a missing-method contradiction.

### S5101 — SAP NeuroQoL

- Location/role: [DOC-004 physical p21](../../../joi240006supp3_prod_1708623114.99733.pdf#page=21); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: 90-dayquality-of-life distribution; median(IQR); median-regression difference95%CI/P; noimputation.
- Checks/calculation: Median contrast compatible with quantile-regression output.
- Definitions/limits: No executed estimate/CI here.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; DirectSAP p.21 names median-regression difference95%CI/P forNeuroQoL90d, median(IQR) description/noMI. This is an internally stated coherent model; no preferred quantile/rank method proposed.

### S5102 — SAP sensitivities/subgroups

- Location/role: [DOC-004 physical p23](../../../joi240006supp3_prod_1708623114.99733.pdf#page=23); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: As-treatedreceived treatment; per-protocol allcriteria/core-lab imaging/assignedtreatment. RepeatWMW. Subgroupsage70,NIHSS20,ICA/M1,time12/6h,core70/100/150,ASPECTS6–10/3–5/0–2,mismatch1.8/15and1.2/10,restrictedsets,hemisphere,US/nonUSpp21–23.
- Checks/calculation: Populations clearly separate; nested thresholds are distinct analyses. Secondary multiplicity not adjustedp14;95%CI. Illustrative forest entries1.00(.50,2.00) are placeholders.
- Definitions/limits: No comparison of illustrative values with trial estimates.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; SAP pp.21–23 defines all subgroup thresholds and distinctas-treated/per-protocol sensitivities. Illustrative1.00(.50,2.00) entries are templates, not zero-event reported RRs; no RouteA1 false pairing. Secondary multiplicity explicitly unadjusted.

### S5103 — SAP exploratory imaging

- Location/role: [DOC-004 physical p23](../../../joi240006supp3_prod_1708623114.99733.pdf#page=23); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Section12 exploratory/tertiary may defer; core/ASPECTS ceilings,joint modification,mismatch, compositeunion or larger when union infeasible, age/severity/time/hemisphere/transferetc.
- Checks/calculation: Context identifies same optional tertiary scope; no executed result here. DOC005 secondary-specific SAP separately assigned.
- Definitions/limits: No raw-data/model-preference audit.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; SAP pp.23–24 expressly permits tertiary analyses beyondprimarymanuscript; compositeunion with larger-volume fallback is specified. Later analysis-specific max-core hierarchy is coveredC003 in itsassignedlane; no generic omittedtertiary candidate.

### S5104 — Historical SELECT functional independence

- Location/role: [DOC-003 physical p13](../../../joi240006supp2_prod_1708623114.99233.pdf#page=13); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: EVT30%vsMM13%; adjustedOR2.92,95%CI1.00–7.91,P=.041
- Checks/calculation: Estimate contained, endpoints ordered; printedCIcontainsnull1 whileP<.05; F-ST1-501. No Wald method assumed.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.13 confirmshistoricalOR2.92CI1.00–7.91/P.041; estimatecontained,endpointsordered,butprintednullboundary/significantP remainsC011RouteA1. Hiddenprecision/CItestalternatives retained, no modelvariance inferred.

### S5105 — Historical SELECT ordinal effect

- Location/role: [DOC-003 physical p13](../../../joi240006supp2_prod_1708623114.99233.pdf#page=13); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: AdjustedOR2.01,95%CI1.00–4.03,P=.049
- Checks/calculation: Estimate contained, endpoints ordered; printedCIcontainsnull1 whileP<.05; F-ST1-501.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.13 confirmshistoricalOR2.01CI1.00–4.03/P.049 andsignificantshift; sameC011pattern. PLAN historicalclassificationambiguity explicit, not currenttrial effect.

### S5106 — Historical SELECT sICH

- Location/role: [DOC-003 physical p14](../../../joi240006supp2_prod_1708623114.99233.pdf#page=14); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: EVT7%vsMM13%,P=.26
- Checks/calculation: Nonsignificant conclusion agrees withP. No matched effectCI; exact test unstated.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.14 historical7%/13%,P.26 accompaniesnostatisticaldifference; direction/test conclusionreconcile. No matchedCI/testformula supplied for exactnumericP reproduction.

### S5107 — Historical SELECT mortality

- Location/role: [DOC-003 physical p14](../../../joi240006supp2_prod_1708623114.99233.pdf#page=14); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: EVT29%vsMM42%,P=.17
- Checks/calculation: Nonsignificant conclusion agrees withP. Exact test unstated.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.14 historical29%/42%,P.17 agreesnonsignificantmortalitystatement. Roundedpercentages and absentmodel/armNs cannot establish contradictory estimate.

### S5108 — Historical retrospective good outcome

- Location/role: [DOC-003 physical p14](../../../joi240006supp2_prod_1708623114.99233.pdf#page=14); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: ASPECTS<7:37%vs≥7:47%,P=.8
- Checks/calculation: Printed nonsignificant conclusion agrees withP; sample size/test absent; no assumed reproduction.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.14 historical37%/47%,P.8 agreesnonsignificantgood-outcomestatement; noCI/rawNs/test supplied, no imputed testmethod.

### S5109 — Historical retrospective sICH

- Location/role: [DOC-003 physical p14](../../../joi240006supp2_prod_1708623114.99233.pdf#page=14); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: 9%vs9%,P=1.0
- Checks/calculation: Identical rounded percentages and nonsignificantP; no contradiction.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.14 historical9%/9%,P1.0 agreesno sICHdifference. Equalroundedpercentages do not requireequal exactrisks; noconflict.

### S5110 — Historical retrospective mortality

- Location/role: [DOC-003 physical p14](../../../joi240006supp2_prod_1708623114.99233.pdf#page=14); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: 20%vs22%,P=.8
- Checks/calculation: Small displayed difference with nonsignificantP; no supplied contradictoryCI.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.14 historical20%/22%,P.8 agreesnomortalitydifference. No interval/test conflict or unique sourcedefinedreproduction.

### S5111 — Historical matched-cohort ordinal effect

- Location/role: [DOC-003 physical p14](../../../joi240006supp2_prod_1708623114.99233.pdf#page=14); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: OR2.56,95%CI2.50–8.47,P=.04
- Checks/calculation: Point contained; endpoints ordered; interval excludesnull1/P<.05 agree. Log-Wald symmetry diagnostic alone does not establish conflicting stated test.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.14 printsOR2.56(2.50–8.47),P.04; pointcontained, orderedlimits, null-exclusion/significanceagree. Log-Waldasymmetrydiagnostic lacks stated sharedCI algorithm; differenthistoricalstudies do not form a reproducing common-model display.

### S5112 — Historical matched-cohort independence

- Location/role: [DOC-003 physical p15](../../../joi240006supp2_prod_1708623114.99233.pdf#page=15); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: EVT25%vsMM0%,P=.04
- Checks/calculation: Reported significance matchesP; sample sizes/test absent; no CI supplied.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.15 historical25%/0%,P.04 agreesstatisticalindependenceclaim. MissingmatchedNs/model/CI prevent independentown-test numericreproduction; zero percentage not zeroP.

### S5113 — Historical matched-cohort infarct volume

- Location/role: [DOC-003 physical p15](../../../joi240006supp2_prod_1708623114.99233.pdf#page=15); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Mean(SD)EVT87(77)vsMM242(120)mL,P<.001
- Checks/calculation: Direction and significantP consistent; sample size missing, no fabricated t-test.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.15 infarctmean(SD)87(77)/242(120)mL,P<.001:lowerEVTvolumeandclaimed significanceagree. No armNs/statedtest for tdiagnostic orSE reconstruction.

### S5114 — Historical matched-cohort PH2

- Location/role: [DOC-003 physical p15](../../../joi240006supp2_prod_1708623114.99233.pdf#page=15); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: P>.99; stated no significant difference
- Checks/calculation: Conclusion/P agree; no point/interval supplied.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.15 PH2P>.99 agreesnostatisticaldifference; noestimateCI or Pzero slip. No additional inference supported.

### S5115 — Historical matched-cohort hemicraniectomy

- Location/role: [DOC-003 physical p15](../../../joi240006supp2_prod_1708623114.99233.pdf#page=15); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: P=.10; stated no significant difference
- Checks/calculation: Conclusion/P agree.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.15 hemicraniectomyP.10 agreesnostatisticaldifference; nointerval/point supplied. No unsupported allocation/test assumed.

### S5116 — Historical matched-cohort mortality

- Location/role: [DOC-003 physical p15](../../../joi240006supp2_prod_1708623114.99233.pdf#page=15); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: P=.75; stated no significant difference
- Checks/calculation: Conclusion/P agree.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.15 mortalityP.75 agreesnostatisticaldifference; absentcounts/test do not createcandidate.

### S5117 — Historical meta-analysis sICH

- Location/role: [DOC-003 physical p16](../../../joi240006supp2_prod_1708623114.99233.pdf#page=16); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: EVT0%vsMM12%,P=.24
- Checks/calculation: Stated no significant difference agrees; no sample/test inputs supplied.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.16 historicalmeta-analysis sICH0%/12%,P.24 agreesnonsignificant claim. No sampledenominators/model orCI to contradict ownP.

### S5118 — Historical SELECT early-window sICH

- Location/role: [DOC-003 physical p16](../../../joi240006supp2_prod_1708623114.99233.pdf#page=16); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: 8/173(5%)vs3/18(17%),P=.072; narrative safety outcomes significantly increased
- Checks/calculation: The sICH P=.072 is not significant at.05 while paragraph explicitly includes it among safety outcomes that significantly increased. Exact test unspecified; see F-ST1-506.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.16 confirms8/173=4.624%→5%,3/18=16.667%→17%,P.072 withcollectivesignificantstatement. C012 coversRouteA1, withhistoricalPLAN/collectivewordingambiguity; noadjusted/crude substitution.

### S5119 — Historical SELECT early-window worsening

- Location/role: [DOC-003 physical p16](../../../joi240006supp2_prod_1708623114.99233.pdf#page=16); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: 14/173(8%)vs5/18(28%),P=.023
- Checks/calculation: Direction and significance agree; percentages reconcile with integer rounding.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.16 confirms14/173=8.092%→8%,5/18=27.778%→28%,P.023:direction/significanceandcountpercentages agree. Qualitative doubledwording separatelyexcluded.

### S5120 — Historical SELECT early-window mortality

- Location/role: [DOC-003 physical p16](../../../joi240006supp2_prod_1708623114.99233.pdf#page=16); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: 15/173(9%)vs7/18(39%),P=.001
- Checks/calculation: Direction and significance agree; percentages reconcile with integer rounding.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.16 confirms15/173=8.671%→9%,7/18=38.889%→39%,P.001:direction/significanceandcountpercentages agree. No fabricatedSE/test calculation.

## Complete Bayesian calculation facts

Posterior given s events/N is Beta(a+s,b+N−s). Tail=1−I_t(a+s,b+N−s), evaluated with Lanczos log-gamma and a convergent incomplete-beta continued fraction in JavaScript. This is deterministic integration of source-specified priors and event counts. No Python, external package or normal approximation used. At each N the minimalinteger s is the first with tail>.95; every predecessor checked.

| Prior/threshold | N | Minimum s | Tail at s | Tail at s−1 |
|---|---:|---:|---:|---:|
| Beta(0.35,0.65);t=0.35 | 20 | 11 | 0.961767775 | 0.907160210 |
| Beta(0.35,0.65);t=0.35 | 30 | 16 | 0.977665716 | 0.949620772 |
| Beta(0.35,0.65);t=0.35 | 40 | 20 | 0.971728919 | 0.943879068 |
| Beta(0.35,0.65);t=0.35 | 50 | 24 | 0.968187856 | 0.941671152 |
| Beta(0.35,0.65);t=0.35 | 60 | 28 | 0.966289545 | 0.941479639 |
| Beta(0.35,0.65);t=0.35 | 70 | 32 | 0.965500009 | 0.942468950 |
| Beta(0.35,0.65);t=0.35 | 80 | 36 | 0.965458559 | 0.944154658 |
| Beta(0.35,0.65);t=0.35 | 90 | 40 | 0.965921547 | 0.946243703 |
| Beta(0.35,0.65);t=0.35 | 100 | 44 | 0.966722456 | 0.948552978 |
| Beta(0.35,0.65);t=0.35 | 150 | 63 | 0.960473449 | 0.943979008 |
| Beta(0.35,0.65);t=0.35 | 200 | 82 | 0.959361444 | 0.945000174 |
| Beta(0.35,0.65);t=0.35 | 250 | 101 | 0.960602998 | 0.948205346 |
| Beta(0.4,0.60);t=0.4 | 20 | 12 | 0.961099626 | 0.906027079 |
| Beta(0.4,0.60);t=0.4 | 30 | 17 | 0.964812378 | 0.925698692 |
| Beta(0.4,0.60);t=0.4 | 40 | 22 | 0.970415675 | 0.941869624 |
| Beta(0.4,0.60);t=0.4 | 50 | 26 | 0.954554044 | 0.920363713 |
| Beta(0.4,0.60);t=0.4 | 60 | 31 | 0.964409556 | 0.938913247 |
| Beta(0.4,0.60);t=0.4 | 70 | 35 | 0.952790714 | 0.924044283 |
| Beta(0.4,0.60);t=0.4 | 80 | 40 | 0.963305404 | 0.941342910 |
| Beta(0.4,0.60);t=0.4 | 90 | 44 | 0.954441732 | 0.930280177 |
| Beta(0.4,0.60);t=0.4 | 100 | 49 | 0.964452433 | 0.945653062 |
| Beta(0.4,0.60);t=0.4 | 150 | 71 | 0.964576872 | 0.949726349 |
| Beta(0.4,0.60);t=0.4 | 200 | 92 | 0.956349011 | 0.941476112 |
| Beta(0.4,0.60);t=0.4 | 250 | 113 | 0.951428952 | 0.937144130 |

No scientific scope gaps. Exact P/CI reproductions unavailable where named sidedness/test/variance/covariance or raw ranks are absent; these are recorded per relationship. Every assigned statistical statement was checked, with candidate inclusion independently pending screen.


