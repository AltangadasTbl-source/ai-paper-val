# Statistical pass 1: methods and support shard

Runtime: 01a12959-b34f-7793-ae97-9dece6336e61; gpt-6.1-sol/high; fresh spawn. Exact scope S102–S123 and S301–S388: 110 records. New complete source maps: extraction/main_part_4_methods_definitions.md and extraction/support_quantitative_evidence.md with its plan, tables and figures parts. Source roles are REPORT DOC-001/DOC-005, PLAN DOC-002/DOC-003/DOC-004. DOC-006 has no statistical record. Exact table tuples remain in those maps and per-page transcripts.

All numeric annotations on result figures DOC-005 pp. 31–42 were visually read, including all twelve component and four global forest rows. Page 31 supplies boundaries, not actual interim results. Pages 32–37 supply group means/95% CI graphically, not precise unlabeled endpoints, and their P values are time-by-group interactions. Pages 38–41 supply every HR/CI/P, Schoenfeld P, incidence, observation time and risk-table annotation. All those distinctions were maintained. Existing CPU-rendered images have an unrecorded historical engine. Fresh direct-source layout extractions by Poppler 26.01.0 confirmed DOC-005 pp. 20, 21, 29, 30, 42, DOC-004 pp. 1–3, DOC-002 pp. 11, 22, 23 in preprocessing/statistics_pass_1/. Commands are pdftotext -layout -f N -l N SOURCE OUTPUT; source identity is the package inventory identity. No OCR or new rendering was needed.

The calculations in the findings are arithmetic or labelled diagnostics, not preferred analyses. No convention supplies missing sidedness, test type, covariance, degree of freedom, GEE variance estimator, subgroup model link or estimand mapping. No noninferiority/equivalence analysis or margin is specified. Group-sequential boundaries, Bonferroni confidence level, exploratory secondary interpretation and unadjusted Cox designation for five-day mortality are checked under the supplied rules.

| S ID | Explicit statistical/method check and outcome | Pass 1 |
|---|---|---|
| S102 | Individual site-stratified 1:1 randomization coherent; PLAN block 6 vs REPORT blocks 4/6/8 is excluded as outside stated result/design focus. | PASS_1_COMPLETE |
| S103 | Original 40% vs 30%, two-sided .05/80% gives normal-approximation diagnostic about 356/group; 748 target consistent with printed 356 and 5% at display precision. | PASS_1_COMPLETE |
| S104 | Blinded pooled-rate re-estimation disclosed; 1912/.95=2012.63, target 2013 agrees. East group-sequential size cannot be independently regenerated without complete software specification. | PASS_1_COMPLETE |
| S105 | Final .044 agrees with Z 2.012; interim .006/.015/.044 and nonbinding futility rules agree with PLAN. Actual interim test values unreported; continuation alone is no conflict. | PASS_1_COMPLETE |
| S106 | Complete-case/modified ITT definition and flow exclusion explain analyzed 1976 after 8 losses; terminology ITT vs modified ITT excluded. No missing-data sensitivity trigger (>1%) reached by 8/1984. | PASS_1_COMPLETE |
| S107 | PP exclusions and sums reconcile 989−72=917 and 987−75=912; missing ventilation and specified PEEP exclusions sum. | PASS_1_COMPLETE |
| S108 | Primary binary model/test declarations match SAP; effect-orientation pattern F-ST1-004. Two-sided .044 consistently distinct from .05 secondary. | PASS_1_COMPLETE |
| S109 | KM/Cox primary HR matches eFigure 8; SAP log-rank test not explicitly named in report but .190 could be its P; absence alone excluded, not asserted replaced. | PASS_1_COMPLETE |
| S110 | Site-random GLMM sensitivity matches eTable 9. Planned severity-weighted primary GEE has no identified reported result; F-ST1-008. | PASS_1_COMPLETE |
| S111 | Binary outcome interval/P method declarations match Table 3; interval conflicts tracked independently F-ST1-005/F-ST1-007; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S112 | Hospital-free t-test/mean difference matches Table 3 note; no null/test conflict. Planned additional GAM confirmation unreported but not primary/key secondary; excluded. | PASS_1_COMPLETE |
| S113 | Five-day unadjusted Cox matches main note and eFigure 11 HR/CI/P, not substituted for in-hospital endpoint. | PASS_1_COMPLETE |
| S114 | Exploratory secondary analyses/no general adjustment consistent; Bonferroni component sensitivity is a distinct analysis. Primary .044 exception clear. | PASS_1_COMPLETE |
| S115 | All five subgroup dichotomies and interaction specification match SAP and Figure 2; no within-stratum P inferred from interaction. | PASS_1_COMPLETE |
| S116 | Complete-case statement coherent; rescue/vasoactive designated post hoc in all main occurrences; R version change alone excluded. | PASS_1_COMPLETE |
| S117 | Twelve-component first-five-day union matches SAP/PLAN; component sums not required to equal composite incidence. | PASS_1_COMPLETE |
| S118 | Nine reported prespecified secondary outcomes match updated SAP grouping; supplement includes post hoc five-day mortality under a broader secondary heading, excluded as wording rather than an explicit prespecification claim. Historical protocol supersession checked separately. | PASS_1_COMPLETE |
| S119 | Main duration/baseline-sensitive hypoxemia/hypotension definitions do not identify a single counting rule; F-ST1-010. Bradycardia definitions agree. | PASS_1_COMPLETE |
| S120 | Respiratory severity thresholds checked; mild ≤2 L in main vs =2 L supplement is compressed wording adjacent to moderate >2 L; excluded, no additional numeric effect asserted. | PASS_1_COMPLETE |
| S121 | GI severity subset 49/46 of 65/56 events is compatible with incomplete classification; conditional missing detail alone excluded. Stages/overall test coherent. | PASS_1_COMPLETE |
| S122 | Kidney risk/injury/failure/loss definitions and row counts reconcile; no stage-specific P inferred. | PASS_1_COMPLETE |
| S123 | PP primary CI/P, site-adjusted and alternate displayed models all support nonsignificance; clinical weighting lacks identified result F-ST1-008. Subgroup interaction claim matches .08. | PASS_1_COMPLETE |
| S301 | Original PLAN power inputs match report; diagnostic n≈356/group and target 748 within display rule. | PASS_1_COMPLETE |
| S302 | Revised inputs .20/.15, .05/80%, max1912 and dropout-inflated2013 internally coherent; full East reproduction unavailable, not a conflicting printed number. | PASS_1_COMPLETE |
| S303 | Allocation website/site balance and block6 compared with main site strata and blocks4/6/8; administrative block/stratum wording alone excluded. | PASS_1_COMPLETE |
| S304 | PLAN five-day collapsed 12-component primary matches main/SAP; union definition coherent. | PASS_1_COMPLETE |
| S305 | Original secondary lists and statuses compared with updated SAP and reports; disclosed updated SAP supersedes earlier list, not independent drift finding. | PASS_1_COMPLETE |
| S306 | Information fractions ×1912 give956/1434/1912; cumulative alpha/beta monotone to .05/.20; crossing sums .801/.200 within precision; Z-to-two-sided P companions reconcile. | PASS_1_COMPLETE |
| S307 | Older logistic/OR/RR hybrid wording compared with explicit updated SAP; no coherent choice challenged. No effect inferred from term alone. | PASS_1_COMPLETE |
| S308 | Older confirmatory-primary/exploratory-other designation matches updated main; updated SAP supplies modified ITT and R in place of earlier SPSS. | PASS_1_COMPLETE |
| S309 | Version-history deletion/reintroduction of interim analysis explicitly disclosed; old threshold not treated as current stopping rule. | PASS_1_COMPLETE |
| S310 | Updated SAP primary and seven grouped prespecified secondary items match nine main outcomes; broad report-supplement secondary wording does not assert five-day prespecification. | PASS_1_COMPLETE |
| S311 | Complete-case/trigger>1%/modified ITT coherent with 8 losses and final1976; absent imputation under <1% not a conflict. | PASS_1_COMPLETE |
| S312 | Distribution assessment, two-sided levels, no general adjustment and selected ventilation times coherent with reports; no normality result invented. | PASS_1_COMPLETE |
| S313 | Primary RR/Wald/chi-square and .044 match main; log-rank may supply unnamed eFigure 8 P, absent named test alone excluded. | PASS_1_COMPLETE |
| S314 | Secondary RR and hospital-free t match main; additional zero-inflated-beta mean-ratio result not identified, outside primary/key omission threshold and excluded. | PASS_1_COMPLETE |
| S315 | Five subgroup boundaries/interactions match all Figure 2 rows; not interpreted as ten main-effect tests. | PASS_1_COMPLETE |
| S316 | GLMM site random and component count/proportional odds with Mann–Whitney correspond exactly to eTable 9 footnotes. | PASS_1_COMPLETE |
| S317 | 1−.05/12=.995833..., printed99.58% agrees; component forest all intervals ordered/containing; common/distinct GEE specifications map to eTable 9. | PASS_1_COMPLETE |
| S318 | Treatment-by-component P .11 has identified reported result; clinical severity-weight GEE lacks identified counterpart; F-ST1-008. | PASS_1_COMPLETE |
| S319 | All ARISCAT operational OR/CI/coefficients and rounded coefficient×10 scores checked; estimates contained, limits ordered and score arithmetic coherent; historical model not trial treatment estimate. | PASS_1_COMPLETE |
| S320 | All fluid count/percent/volume/SD/P tuples checked; no CI conflicts; rounded means and unspecified distribution/sample detail prevent unsupported exact-test inference. Main median vs supplement overall mean not conflicting estimands. | PASS_1_COMPLETE |
| S321 | All six drug/count/dose tuples checked; need-for-vasoactive counts/P match main; dopamine sparse-count P raises diagnostic question but exact test unidentified, excluded. | PASS_1_COMPLETE |
| S322 | All 29 agent rows checked; counts within precision, overlapping drug classes not summed as partition; sparse-cell P differences cannot establish test without definition. | PASS_1_COMPLETE |
| S323 | All surgical-priority/position/wound partitions checked; small total differences reflect available observations, percentages within precision. Global P not interpreted per category; pressure no interval conflict. | PASS_1_COMPLETE |
| S324 | Dyspnea day1: equal rounded means, P .53; no CI, no contradiction under mean precision or a named test. | PASS_1_COMPLETE |
| S325 | Dyspnea day2: rounded mean ranges can yield small nonsignificant contrast/P .57; no exact test inferred. | PASS_1_COMPLETE |
| S326 | Dyspnea day3: rounded mean ranges can reconcile P .68; no CI. | PASS_1_COMPLETE |
| S327 | Dyspnea day4: equal rounded means and P .79 compatible; no CI. | PASS_1_COMPLETE |
| S328 | Dyspnea day5: equal rounded means and P .78 compatible; no CI. | PASS_1_COMPLETE |
| S329 | Thoracic day1: rounded mean ranges can reconcile P .52; no CI. | PASS_1_COMPLETE |
| S330 | Thoracic day2: SD3.9 retained, not normalized; P .34 does not establish numeric contradiction with rounded means. | PASS_1_COMPLETE |
| S331 | Thoracic day3: rounded equal means/P .94 compatible; no CI. | PASS_1_COMPLETE |
| S332 | Thoracic day4: rounded mean ranges include a difference yielding P .20; no test assumed. | PASS_1_COMPLETE |
| S333 | Thoracic day5: equal rounded means/P .16 can reconcile through precision; no CI. | PASS_1_COMPLETE |
| S334 | Abdominal rest day1: printed mean intervals allow .10 difference and nonsignificant P .10; no CI. | PASS_1_COMPLETE |
| S335 | Abdominal rest day2: equal rounded means/P .31 compatible; no CI. | PASS_1_COMPLETE |
| S336 | Abdominal rest day3: equal rounded means/P .94 compatible; no CI. | PASS_1_COMPLETE |
| S337 | Abdominal rest day4: equal rounded means/P .75 compatible; no CI. | PASS_1_COMPLETE |
| S338 | Abdominal rest day5: equal rounded means/P .83 compatible; no CI. | PASS_1_COMPLETE |
| S339 | Abdominal incident day1: equal rounded means/P .52 compatible; no CI. | PASS_1_COMPLETE |
| S340 | Abdominal incident day2: rounded mean ranges permit small contrast/P .51; no CI. | PASS_1_COMPLETE |
| S341 | Abdominal incident day3: equal rounded means/P .55 compatible; no CI. | PASS_1_COMPLETE |
| S342 | Abdominal incident day4: rounded mean ranges permit small contrast/P .69; no CI. | PASS_1_COMPLETE |
| S343 | Abdominal incident day5: equal rounded means/P .58 compatible; no CI. | PASS_1_COMPLETE |
| S344 | PP primary: counts/percentages and ordered containing null CI/P .17 agree; effect-orientation pattern F-ST1-004. | PASS_1_COMPLETE |
| S345 | PP mild: ordered containing null CI/P .15 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S346 | PP moderate: ordered containing null CI/P .15 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S347 | PP severe: ordered containing null CI/P .18 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S348 | PP ARDS: ordered containing null CI/P .62 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S349 | PP bronchospasm: ordered containing null CI/P .84 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S350 | PP infiltrates: equal counts, ordered null CI/P .99 agree; near-one estimate within display precision. | PASS_1_COMPLETE |
| S351 | PP infection: ordered containing null CI/P .83 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S352 | PP aspiration: ordered containing null CI/P1.00 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S353 | PP pleural: CI excludes one and P .01 agrees; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S354 | PP atelectasis: containing null CI/P .18 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S355 | PP cardiopulmonary edema: CI1.02–1.82 excludes one with P .09; F-ST1-007; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S356 | PP pneumothorax: ordered containing null CI/P .62 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S357 | Site-random OR.86(.68–1.08), P.19: ordered containing null CI/test agree; not compared with crude RR. | PASS_1_COMPLETE |
| S358 | Count OR.88(.72–1.09), P.25: ordered containing null CI/test agree despite expressly different OR and Wilcoxon analyses; mean count distinct from incidence. | PASS_1_COMPLETE |
| S359 | Common-effect GEE OR.93(.80–1.08), P.37: ordered containing null CI/test agree; no covariance inferred. | PASS_1_COMPLETE |
| S360 | Treatment-component interaction P .11: defined heterogeneity test, no estimate/CI given; no other row P substituted. | PASS_1_COMPLETE |
| S361 | Average-effect OR.99(.94–1.05), P.98: ordered containing null CI/test significance agree; log-Wald diagnostic differs but test/CI transform not specified, excluded. | PASS_1_COMPLETE |
| S362 | Sequential figure directions/boundaries/enrollment match PLAN; drawing is design boundary not observed Z, so continuation not inferred from it. | PASS_1_COMPLETE |
| S363 | Tidal graph: all five means inside their graphical CIs; unit/legend coherent; .081 is time×group, not main table within-time .007/.008. | PASS_1_COMPLETE |
| S364 | PEEP graph: all five means contained, high above low, P <.001 interaction distinct from high-low comparisons; no precise endpoint invented. | PASS_1_COMPLETE |
| S365 | Peak graph: all five means contained, high above low, interaction P <.001 and main direction agree. | PASS_1_COMPLETE |
| S366 | SpO2 graph: all five means contained, high above low, interaction P <.001; table/graphic direction agrees. | PASS_1_COMPLETE |
| S367 | Driving graph: all five means contained, high below low, interaction P <.001; pressure-minus-PEEP definition coherent. | PASS_1_COMPLETE |
| S368 | FIO2 graph: all five means contained, high lower after initial time, interaction P <.001; percent vs main fraction scale resolves immediately. | PASS_1_COMPLETE |
| S369 | Primary time-to-event HR.88(.73–1.06), P.190: containing null CI and direction agree; all annotations match caption; Schoenfeld .05 no reported contradictory decision. | PASS_1_COMPLETE |
| S370 | Severe time-to-event HR.85(.66–1.09), P.197: containing null CI and direction agree; Schoenfeld .28; duplicate primary risk table apparent issue excluded as peripheral. | PASS_1_COMPLETE |
| S371 | Extrapulmonary HR1.12(.89–1.39), P.314: containing null CI and direction agree; Schoenfeld .67; caption/annotation consistent. | PASS_1_COMPLETE |
| S372 | Five-day HR1.67(.40–6.97), P.484: containing null CI and direction agree; Schoenfeld .14; caption's extraneous outcome phrase resolves from title, scale and parenthesis and is excluded. | PASS_1_COMPLETE |
| S373 | Mild forest RR.92[.76,1.12]: containing ordered99.58% CI; no printed P; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S374 | Moderate forest RR.83[.59,1.17]: containing ordered99.58% CI; no P inferred; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S375 | Severe forest RR.91[.61,1.34]: containing ordered99.58% CI; effect pattern F-ST1-004; small .90/.91 copy gap within precision. | PASS_1_COMPLETE |
| S376 | Aspiration RR1.33[.41,4.30]: containing ordered99.58% CI/arrows coherent; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S377 | Bronchospasm RR1.09[.62,1.91]: containing ordered99.58% CI; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S378 | ARDS RR1.50[.65,3.44]: containing ordered99.58% CI; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S379 | Infection RR1.00[.52,1.90]: containing ordered99.58% CI; .99/1.00 display difference within precision. | PASS_1_COMPLETE |
| S380 | Atelectasis RR.88[.64,1.23]: containing ordered99.58% CI; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S381 | Edema RR1.31[.87,1.98]: containing ordered99.58% CI; different multiplicity level not compared with95% PP conflict; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S382 | Pleural RR1.36[1.05,1.76]: containing ordered99.58% CI excludes one; no multiplicity-adjusted P printed; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S383 | Pneumothorax RR.50[.04,5.96]: containing ordered99.58% CI/arrows coherent; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S384 | Infiltrates RR.87[.49,1.55]: containing ordered99.58% CI; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S385 | Collapsed .93[.83,1.04] called OR while main same tuple called RR; quantity-label conflict F-ST1-009. Containment/order coherent. | PASS_1_COMPLETE |
| S386 | Count .88[.72,1.09]: OR label agrees with eTable 9, ordered containing null95% CI. | PASS_1_COMPLETE |
| S387 | Common GEE .93[.80,1.08]: OR label and tuple match eTable 9; containing null95% CI. | PASS_1_COMPLETE |
| S388 | Average GEE .99[.94,1.05]: OR label and tuple match eTable 9; containing null95% CI; diagnostic limitation tracked at S361. | PASS_1_COMPLETE |
