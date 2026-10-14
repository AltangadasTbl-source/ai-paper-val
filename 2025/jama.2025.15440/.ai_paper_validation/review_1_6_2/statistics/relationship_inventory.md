# Statistical relationship inventory — Workflow 1.6.2

Pass-1 runtime agent: /root/statistics_pass1. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN. Pass 1 covered all 52 mapped inferential/design groups: S001–S028 and S101–S124. These are coverage groups, each retaining every component relationship; there is no finding quota. Pass-2 runtime agent: /root/statistics_pass2, a different fresh gpt-6.1-sol/high runtime with start mode FRESH_SPAWN. Pass 2 independently revisited every row and all component relationships using the complete current-run ledger, screening log, recheck, checker exclusions and exact supplied-source locations. Every row preserves PASS_1_COMPLETE and now records PASS_2_COMPLETE.

Read completely: QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md. Pass-1 scientific inputs: current complete main quantitative map; support map structured sections through its source-link/limits section; targeted SAP page appendices; main native pages 3 and 5; source-linked retained main figures on physical pages 6 and 7; result supplement figure on physical page 8; visually inspected protocol pages 20–22. No legacy scientific conclusions, candidates, checkers or reports were consulted. Pass2 additionally read all current-run checker outputs, the complete current ledger/screen/recheck and independently revisited every assigned source-linked relationship, as required by the two-pass contract.

## Source identity and checks

DOC-001 is REPORT: [main article](../../../jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=1), 9 physical pages. DOC-002 is PLAN: [protocol](../../../joi250068supp1_prod_1760999665.28862.pdf#page=1), 26 pages. DOC-003 is PLAN: [SAP](../../../joi250068supp2_prod_1760999665.29862.pdf#page=1), 24 pages. DOC-004 is REPORT: [result supplement](../../../joi250068supp3_prod_1760999665.30362.pdf#page=1), 11 pages. Locations below use physical PDF pages. The complete maps cover all 70 pages, including material with no applicable inferential content.

All printed estimates/intervals were checked for containment, endpoint order, direction and null exclusion; matching P values were checked at the stated 95% confidence/.05 significance levels without applying the rounding screen to any interval–test conflict. Heterogeneity P values compare subgroup effects, not a subgroup effect against its own null. No superiority conclusion beyond the stated primary test, noninferiority/equivalence margin, formal multiplicity adjustment, efficacy/safety interim decision, or stopping boundary is supplied. Sample-size extension used blinded-to-total-AF information and is distinct from an efficacy interim test. Statistical methods were compared only with supplied descriptions; absent implementation inputs were named, not supplied by convention.

Diagnostic reconstructions below do not substitute for reported analyses. For counts-based primary/sensitivity displays, log-ratio Wald intervals and unpooled Wald difference intervals reproduce every row; Pearson chi-square reproduces reported overall P values. This is a demonstrated same-display reconstruction, not an inferred universal model. Counts are exact integers; percentage/estimate display intervals use half the last printed unit.

## Complete pass records

| S ID | Exact source scope and role | Relationship and pass-1 facts | Pass 1 | Pass 2 |
|---|---|---|---|---|
| S001 | DOC-001 p3 REPORT; S113, S117, S118 PLAN comparators | Initial 2500/extended 5000; 4.4% versus 1.75%; ratio approximately 2.5; >90% at two-sided .01, including ratio 2. Protocol table powers 96%–100% at 5000 support whole-trial claim; age80/sex .05 powers 89%–99% support approximately90% language. Under75 .01 cell separately tracked S118/F-ST1-001; it is not the main stated age80 power claim. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S002 | DOC-001 p3 REPORT; S101, S102, S105, S108 PLAN | Individual ITT chi-square proportions, age/sex heterogeneity; matching sensitivity/OAC proportions. Baseline adjustment not claimed. Exact event counts and populations match defined analyses; no paired or cluster unit is claimed. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S003 | DOC-001 pp1,2,4 REPORT | Primary172/2520 versus 136/2520; RR1.26(1.02–1.57), P=.03. Recomputed RR1.264706, CI1.016965–1.572798, Pearson P=.034260. Contains estimate, excludes1, P significant; primary-success statement follows .05 rule. Abstract/Key Points/body match. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S004 | DOC-001 pp4,6 REPORT | Proportions6.83%(5.84–7.81),5.40%(4.51–6.28); RD1.43%(0.11–2.75). Unpooled Wald RD1.428571%, CI0.106555–2.750588%; each individual-proportion Wald CI rounds as printed. Overall RR/test as S003. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S005 | DOC-001 p6 REPORT | Age<80:94/1715 versus 74/1744, RD1.24%(-.20–2.67), RR1.29(.96–1.74). Recomputed RD1.237930%, CI-.195730–2.671590; RR1.291750, CI.959623–1.738827. Null included in both; no local P printed. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S006 | DOC-001 p6 REPORT | Age≥80:78/805 versus 62/776, RD1.70%(-1.10–4.50), RR1.21(.88–1.67). Recomputed RD1.699750%, CI-1.095771–4.495271; RR1.212743, CI.881893–1.667714. Null included; no local P. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S007 | DOC-001 p6 REPORT | Female76/1180 versus 46/1180, RD2.54%(.76–4.33), RR1.65(1.16–2.36). Recomputed RD2.542373%, CI.758750–4.325996; RR1.652174, CI1.155991–2.361332. Both exclude null with increased detection direction; no local P. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S008 | DOC-001 p6 REPORT | Male96/1340 versus 90/1340, RD.45%(-1.48–2.37), RR1.07(.81–1.41). Recomputed RD.447761%, CI-1.476499–2.372021; RR1.066667, CI.808248–1.407709. Both include null; no local P. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S009 | DOC-001 pp4,6 REPORT | Age heterogeneity P=.78; sex P=.06. Diagnostic independent log-RR contrasts give .776472/.057911, matching rounded P. These compare subgroup effects, so female null-excluding CI and sex heterogeneity .06 do not conflict. No-significant-heterogeneity narrative follows stated rule; consistency does not claim identical effects. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S010 | DOC-001 p3 REPORT | Log-rank O−E and variance V, RR expression exp(O−E÷V). O−E is explicitly named a single quantity; missing visual parentheses do not identify a different computed value. O−E,V, log-rank statistic and CI algorithm are absent, preventing exact reconstruction. No method-dependent numeric conflict established. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S011 | DOC-001 pp5,6 REPORT | AF time-to-event RR1.29(1.03–1.61), log-rank P=.03. Estimate contained; limits ordered; excludes1/P<.05 and earlier/more detection direction agree. Diagnostic log-CI SE≈.114 yields P≈.025–.03 after display rounding. O−E,V unavailable. Distinct censored rate comparison from S003 crude proportion. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S012 | DOC-001 p3 REPORT; S103, S104, S107 PLAN | Permutation compares mean AF days in all randomized; noAF=0; endpoint earliest2.5y/death/withdrawal; imputation for primary-care loss stated. SAP allowed later imputation definition; report supplies it. Replication count, permutation distribution and CI algorithm absent. No contradictory step established. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S013 | DOC-001 p5 REPORT | Mean AF days41(37–45),21(17–25), difference20(13–28), P<.001. Each estimate contained/ordered; displayed mean difference20 reconciles; positive difference CI excludes0 with P<.001. Ordinary independent Wald propagation is not a supplied CI method, so cannot adjudicate interval-width differences from summaries alone. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S014 | DOC-001 p5 REPORT; DOC-004 p10 REPORT | Median report-to-GP AF14days(9–26), 83/89 ever recorded/78within3months. Median contained and delay direction coherent; single-group KM eFigure3 supplies descriptive context, not a printed comparison P. Event times and quantile CI construction absent. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S015 | DOC-001 p5 REPORT | OAC364/2520 versus 322/2520, RR1.13(.98–1.30), P=.08. Recomputed RR1.130435, CI.983334–1.299540, Pearson P=.084478. Null included/P≥.05; direction increased OAC agrees. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S016 | DOC-001 pp5,7 REPORT | OAC time-to-event RR1.15(.99–1.34), log-rank P=.07. Estimate contained/ordered; includes1/P≥.05; curves favor earlier/more OAC patch. Diagnostic log-CI P≈.07; O−E,V unavailable. Distinct from S015 proportion; month-of-randomization excluded explicitly. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S017 | DOC-001 pp1,3,5 REPORT | OAC means1.63(1.50–1.76)/1.14(1.01–1.26)months, difference.50(.24–.75), P<.001. All estimates contained; null exclusion/P agree. Difference from rounded means lies .480–.500, overlapping printed .495–.505. Abstract/body match. Permutation/CI details absent, not assumed independent-Wald. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S018 | DOC-001 p7 REPORT | Cardiovascular death32/2520 versus 43/2520; rateRR.74(.47–1.17). Estimate contained/ordered, null included and fewer-patch direction matches graph. No P or O−E/V supplied; no crude-RR substitution. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S019 | DOC-001 p7 REPORT | Noncardiovascular death71 versus 83, rateRR.85(.62–1.17). Containment/order/null/direction reconcile; no P or O−E/V. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S020 | DOC-001 pp5,7 REPORT | Anydeath103 versus 126, rateRR.82(.63–1.06). 32+71=103 and43+83=126. Containment/order/null/direction reconcile; no P. Source-specific deaths distinct from primary-care flow deaths98/118. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S021 | DOC-001 p7 REPORT | Presumed ischemic stroke60 versus 58, rateRR1.03(.72–1.48). Ordered/contained/null included; direction agrees. Unspecified stroke included in definition; no P, O−E/V or mutually exclusive participant categorization stated. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S022 | DOC-001 p7 REPORT | Hemorrhagic stroke12 versus 6, rateRR1.94(.77–4.90). Ordered/contained/null included; rightward direction agrees. Model-based time-to-event RR not replaced with crude2; no P. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S023 | DOC-001 p1 REPORT; S024 REPORT comparator | Abstract any-stroke69 versus 64, rateRR1.08(.76–1.53). Estimate contained/null included. Matched body CI.77–1.51 differences remain below scope 5% threshold after rounding intervals; no significance reversal. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S024 | DOC-001 pp5,7 REPORT | Any-stroke69 versus 64, rateRR1.08(.77–1.51). Ordered/contained/null included, no P. Report explicitly exploratory/not powered/no trend; estimates and favorable-direction axis agree. Separate stroke categories need not partition individuals. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S025 | DOC-001 pp2–3 REPORT; S101–S112,S115 PLAN | Primary2.5y GP AF, age80/sex secondary proportion, both-care sensitivity, exploratory timeAF/AF days/OAC and long-term clinical results. Primary/key secondary definitions, ITT, randomization/intervention match. Five-year AF-days remains a later outcome, not replaced by2.5y exploratory endpoint. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S026 | DOC-001 p3 REPORT; DOC-003 pp12–14,19–20 PLAN | Proportion noAF beforeloss grouped noAF; primary-care timeAF censors death/withdrawal/GP loss/2.5y. OAC/death do not censor GP loss because national data. AF-days continues afterknownAF with death/withdrawal limits. At-risk counts are monotone and valid, not equated to raw proportions. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S027 | DOC-001 p3,pp6–7 REPORT; S114 PLAN | Primary significance two-sided .05; noformal multiple-testing adjustment; secondary/sensitivity/exploratory interpretation qualified. PrimaryP=.03 satisfies decision rule. Design power at.01 is not stated as final testing alpha. No noninferiority/equivalence/interim boundary applies. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S028 | DOC-001 p3 REPORT; DOC-003 p23 PLAN | SAS9.4/R4.5.0/RStudio2025.05 build496; SAP4.2.2/2024.12 build563 orlater. Later software fits stated allowance; no numeric discrepancy derived from version. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S101 | DOC-002 pp4,9,11,15 PLAN; DOC-003 pp5,8,13,18 PLAN; S002–S004 REPORT | Primary GP AF presence to2.5y, all randomized ITT, no censoring/chi-square/ratio 95%CI. PrerandomAF counts only if later record. Matches report populations/counts/method. No adjusted-effect versus crude contradiction. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S102 | DOC-002 pp4,10–11,15 PLAN; DOC-003 pp8–9,18 PLAN; S005–S009 REPORT | Prespecified age80/sex chi-square subgroup effects and heterogeneity match report. Diagram age-only shorthand resolved by same-plan narrative specifying sex; no conflicting extracted number or outcome status. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S103 | DOC-002 pp4,10–11,15 PLAN; DOC-003 pp5,7–9,14,18 PLAN | Five-year secondary mean dayswithAF overall/age80/sex; noAF=0; earliestdeath/withdrawal/5y; permutation empirical P=(1+s)/(n+1). Formula allows nonzero empiricalP; no numerical s,n supplied. Report at2.5y does not supply five-year result and explicitly distinguishes shorter exploratory window. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S104 | DOC-003 pp10–14,16–18 PLAN | Separate GP/national follow-up, day913/1826, loss and withdrawal, AF-days imputation later. Definitions agree with report source-specific follow-up and missingness. Future specification not proof of contradictory imputation; report gives actual rule. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S105 | DOC-003 p18 PLAN; DOC-004 p8 REPORT | Both-care AF sensitivity primary/subgroups is supplied as all five eFigure1 rows. Endpoint differs intentionally from GP-only result; method/population/timepoint match planned sensitivity. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S106 | DOC-003 p19 PLAN; S010–S011,S026 REPORT | TimeAF2.5/5y GP-firstAF, censored GP loss/death/withdrawal/day913/1826, log-rank/cumulative curve/median amongdiagnosed. Report2.5y matches; conditionalmedians103/530days not all-randomized mean. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S107 | DOC-003 p19 PLAN; S012–S013 REPORT | 2.5y AF-days expressly exploratory, using shorter version of 5y secondary permutation method. Status/model align; no change from5y secondary to2.5y primary asserted. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S108 | DOC-003 pp13,19 PLAN; S015 REPORT | OAC postrandom proportions/chi-square; randomization-monthbaseline; exclude rivaroxaban2.5mgBID from clinicalOAC. Report dispensing/calendar method coherent; underlying drug-code extraction not supplied. Missing coding detail alone not finding. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S109 | DOC-003 pp13–14,19 PLAN; S017 REPORT | Mean distinctcalendar exposure months, permutation, death/withdrawal censoring; separate derivationdocument not supplied. Report means/difference/test coherent, exact individual-month reproduction unavailable. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S110 | DOC-003 p20 PLAN; S016 REPORT | OAC cumulative first-postrandommonth, death/withdrawal censoring, log-rank to30/60months. Report30months test/curve matches, not GP-loss censored. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S111 | DOC-002 p16 PLAN; DOC-003 pp20–21 PLAN | Nonrandomized diagnosis route/OAC groups and GP-reportdate rules; report supplies reportdelay, not full OAC comparison. Missing exploratory nonrandomized OAC output is outside primary/key-secondary omitted-analysis category. No prespecified claim for unsupplied number. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S112 | DOC-002 p16 PLAN; DOC-003 pp11–12,20 PLAN; S018–S024,S027 REPORT | Future exploratoryclinical event counts/nohypothesistesting; report exploratory log-rank rateRR/CIs without death/strokeP or significance claim. CI/effect calculation does not by itself demonstrate a hypothesis test was performed. Details may be later specified; no reproduced decision-rule conflict. No formalDMC/interimassessment matches no reported interim efficacy decision. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S113 | DOC-002 pp13–15,19–22 PLAN; DOC-003 pp21–22 PLAN; S001 REPORT | Annual.7%usualcare→1.75%2.5y; patch3.75% and active4.4%; initial2500, extended5000 based on1250blinded-to-totalAF; approximately3000/.05 and4100/.01 for ratio 2 matches table2939/4088. Wholetrialpower and age80/sex.05 narrative reconcile. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S114 | DOC-003 pp22–23 PLAN; S002,S027,S028 REPORT | Noapriori baselineadjustment; conditionalif imbalance, minimization expectedbalance. Report unadjusted proportions do not contradict conditionalclause. Two-sided.05/noformal multiplicity/95%CIs and later software agree. Unreported imbalance trigger not presumed activated. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S115 | DOC-002 pp10–13 PLAN; DOC-003 pp6–10,12 PLAN; DOC-004 p2 REPORT | Individual1:1centralminimization, age/sex/residualscore, single14daypatch versususualcare, all randomized ITT, careindependent. All report inferential denominators5040/2520 each match unit/population; no clustering adjustment claim. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S116 | DOC-002 pp19–20 PLAN Tables1–2 | All9 sample-size rows and annual projection checked. Firstyearactive3.96=2+(.49+.42+.35+.28+.21)+.21; subsequentcumulative3.96,.28,.35,.42,.49 increments yield4.24,4.59,5.01,5.50. Continuous-time parameter values unavailable; no forced linear reconstruction. Continuity-corrected sample-size diagnostics track all 9 rows within <.5%; complete table below. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S117 | DOC-002 p21 PLAN Table 3 | All5 rows,10sample-size outputs and25power cells checked. Patch×1.177 andactive/ratio reproduce rounded rates; fulltrial5000 two-sided.01 powers>90% consistent with narrative. Diagnostic reconstructed sizes/powers below; small remaining differences below5% display threshold. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S118 | DOC-002 p22 PLAN Table 4 | All6 rows,12sample-size outputs and24power cells checked. Population fractions andsubgroup rather than totaln applied. One cell: age <75,total trial 5000,.01 printed 34% versus reproducing-method28.585%/roundingenvelope27.355–29.840%: F-ST1-001. Everyother23power cell below5% displaythreshold; complete diagnostics below. Female3.09% read visually, not altered. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S119 | DOC-004 pp5–6 REPORT eTable 2 | Every31printed P comparisons checked, including20binaryrows, five categorical overalltests, three ordinal trends and three continuous summaries. Chi-square exact count outputs below; all match displayprecision. Diagnosticrankscore trends match. Age meanT has roundedsummaryuncertainty; BMI mean supports<.001. Mann–Whitney scoremedian cannot reproduce without individual distribution; no conflicting printed statistic. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S120 | DOC-004 p8 REPORT | Overallboth-care251/2520 versus 207/2520, RD1.75%(.16–3.33), RR1.21(1.02–1.45), P=.03. RecomputedRD1.746032%, CI.159707–3.332357; RR1.212560, CI1.017345–1.445235, PearsonP=.031061. Null exclusion/P agree; direction matches. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S121 | DOC-004 p8 REPORT | <80:142/1715 versus 110/1744, RD1.97%(.24–3.71), RR1.31(1.03–1.67); ≥80:109/805 versus 97/776,RD1.04%(-2.28–4.36),RR1.08(.84–1.40); heterogeneityP=.28. Bothrows reproduced below; estimatecontainment/order and matchingnulls hold. Diagnosticlog-RR heterogeneityP=.282179. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S122 | DOC-004 p8 REPORT | Female105/1180 versus 70/1180,RD2.97%(.86–5.08),RR1.50(1.12–2.01); male146/1340 versus 137/1340,RD.67%(-1.66–3.00),RR1.07(.85–1.33); heterogeneityP=.07. Bothrows reproduced below; matchingnulls hold. Diagnosticlog-RR heterogeneityP=.066769. FemaleCIexcluding1 does not conflict with heterogeneityP. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S123 | DOC-004 p10 REPORT; DOC-003 p17 PLAN | Single-group89patchAF reportdelayKM, sevenprior-GPAF events immediatelyafterday0; riskcounts89,34,18,10,8,7,6 monotone and ≤89. No P/CIinfigure;14daymedianCIfrommain containsestimate. Comparisonstatistic not invented; source event timing convention explicit. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S124 | DOC-004 pp2,7,9,11 REPORT; DOC-003 pp6,17 PLAN | PatchAF≥30s, AF/flutter populations89/102, algorithm/technicianreview, thresholds andburden/duration/heart-rate units match planneddefinitions. NoP/CIinhistograms. AFonlygroupedepisode9/29/20/42% andAF/AFL10/26/18/46% sum100 separately; differentpopulation not conflictingresult. | PASS_1_COMPLETE | PASS_2_COMPLETE |

## Reproducing calculations

Let p1=a/n1, p0=c/n0. RR=p1/p0; log-RR variance=1/a−1/n1+1/c−1/n0. Its Wald95%CI is RR×exp(±1.959963985×sqrt(variance)). Difference95%CI is (p1−p0)±1.959963985×sqrt[p1(1−p1)/n1+p0(1−p0)/n0]. Pearson1df P uses pooled p=(a+c)/(n1+n0). These calculations reproduce all displayed primary and sensitivity count-based rows; they are not applied to log-rank estimates.

| S ID | Recomputed RR95%CI | Recomputed RD95%CI, percentage points | Overall printed P check |
|---|---|---|---|
| S003,S004 | 1.264706(1.016965–1.572798) | 1.428571(.106555–2.750588) | .034260→.03 |
| S005 | 1.291750(.959623–1.738827) | 1.237930(-.195730–2.671590) | No printed localP |
| S006 | 1.212743(.881893–1.667714) | 1.699750(-1.095771–4.495271) | No printed localP |
| S007 | 1.652174(1.155991–2.361332) | 2.542373(.758750–4.325996) | No printed localP |
| S008 | 1.066667(.808248–1.407709) | .447761(-1.476499–2.372021) | No printed localP |
| S015 | 1.130435(.983334–1.299540) | 1.666667(-.226157–3.559491), not printed | .084478→.08 |
| S120 | 1.212560(1.017345–1.445235) | 1.746032(.159707–3.332357) | .031061→.03 |
| S121,<80 | 1.312738(1.032782–1.668581) | 1.972544(.239703–3.705385) | No printed localP |
| S121,≥80 | 1.083230(.839251–1.398135) | 1.040373(-2.276401–4.357146) | No printed localP |
| S122,female | 1.500000(1.120751–2.007582) | 2.966102(.855248–5.076955) | No printed localP |
| S122,male | 1.065693(.854816–1.328592) | .671642(-1.655255–2.998539) | No printed localP |

No route A category 1 conflict was identified in any printed estimate/interval/test combination, including the permutation results. Exact permutation P reproduction requires individual outcomes, imputed outcomes, replication count and permutation distribution; exact quantile/mean CI reproduction requires its specified construction. Absence of those inputs is a reproduction limitation, not an omitted check or a stand-alone finding.

### S119: every supplementary P

Two-by-two rows contrast characteristic present/absent across2126withECG/394withoutECG. Missing ethnicity/BMI excluded exactly as footnotes specify. Overall ethnicity compares white1738/307 with othernonmissing39/11.

| Comparison | Printed P | Recomputed Pearson P or diagnostic fact |
|---|---|---|
| Age categories | .75 | .751174 |
| Age ordinal trend | .62 | .620450, diagnostic rank scores1,2,3 |
| Age mean | .50 | Rounded means77.6/77.8 andSD5.9/6.1 admit .50 under two-sampleT; means' half-unit intervals allow difference .10–.30, not a fixed .20 |
| Sex | .47 | .474390 |
| White versus othernonmissing | .17 | .173665 |
| BMI categories | .07 | .073284 |
| BMI ordinal trend | .03 | .027446, diagnostic rank scores1,2,3 |
| BMI mean | <.001 | Difference1.3, unequal-variance diagnostic SE≈.3845 gives absoluteT≈3.381; pooleddiagnostic SE≈.3357 givesT≈3.873; both support <.001 with roundedinputs |
| Score categories | <.001 | .00008698 |
| Score ordinal trend | <.001 | .00002166, diagnostic rank scores1,2,3,4 |
| Score median | <.001 | Mann–Whitney requires individual ranks; medians/IQR alone do not reproduce P |
| Hypertension | .32 | .319503 |
| Diabetes | .02 | .017437 |
| Stroke/TIA | .05 | .048661, rounds.05; noCIprinted to contradict this roundedP |
| CKD | .61 | .610505 |
| Thromboembolism | .03 | .025351 |
| Myocardial infarction | .87 | .867106 |
| Heartfailure | .006 | .005879 |
| Peripheral artery disease | .04 | .038071 |
| Statin | .54 | .544574 |
| RAASinhibition | .36 | .362340 |
| PPI/H2 | .81 | .807741 |
| Calciumchannelblocker | .07 | .072018 |
| Diuretic | .30 | .299333 |
| Aspirin/dipyridamole | .23 | .232373 |
| Betablocker | .39 | .387631 |
| P2Y12inhibition | .33 | .329296 |
| OAC | .03 | .034084 |
| DirectOAC | .08 | .080915 |
| VKA | .31 | .314063 |
| Insulin | .22 | .219808 |

The exact equal/unequal-variance T implementation and ordinal scores are not stated; continuous/ordinal reconstructions are diagnostics and are not a basis for a finding. Correct denominators for BMI means are nonmissing data, ECG1527/noECG283, not all 2126/394; the diagnostic standard errors above use those nonmissing counts. Supplied rounded BMI inputs support both tests' <.001 conclusion.

### S116–S118: complete power/sample-size diagnostics

Let A=sqrt[2pbar(1−pbar)], B=sqrt[p0(1−p0)+p1(1−p1)], d=p1−p0>0, pbar=(p0+p1)/2, zα=Φ⁻¹(1−α/2), z90=Φ⁻¹(.90). Uncorrected per-arm n0=(zαA+z90B)²/d². Continuity-corrected total nCC=(n0/2)[1+sqrt(1+4/(n0d))]². For total trial T and subgroup fraction f, per-arm m=Tf/2. Reconstructed power100×{Φ[(sqrt(m)d−zαA−1/sqrt(m))/B]+Φ[(-sqrt(m)d−zαA−1/sqrt(m))/B]}. Second term is the other rejection tail. Normal approximation is explicitly diagnostic; exact software is unreported. ProtocolTable 2 specifies continuity-corrected sample size, and same-display Table 4 printed outputs empirically support this reconstruction except the noted cell. It is not claimed that every package analysis uses these formulas.

| S116 comparisonyear | Printed n | Diagnostic nCC |
|---|---:|---:|
| 1 | 1019 | 1014.820 |
| 1.5 | 1261 | 1257.022 |
| 2 | 1565 | 1561.567 |
| 2.5 | 1914 | 1916.466 |
| 3 | 2348 | 2345.419 |
| 3.5 | 2825 | 2822.334 |
| 4 | 3406 | 3403.622 |
| 4.5 | 4004 | 4018.772 |
| 5 | 4711 | 4709.286 |

| S117 row | Printed n .05/.01 | Diagnostic n .05/.01 | Printed powers:2500.05,4000.05,4000.01,5000.05,5000.01 | Diagnostic powers sameorder |
|---|---|---|---|---|
| Original | 1914/2649 | 1916.466/2654.293 | 96,100,99,100,99 | 96.234,99.764,98.637,99.968,99.740 |
| Ratio2.5 | 1941/2687 | 1950.239/2701.640 | 96,100,99,100,100 | 95.938,99.729,98.475,99.961,99.697 |
| Interimratio2.5 | 1773/2454 | 1772.606/2455.383 | 97,100,99,100,100 | 97.359,99.875,99.192,99.986,99.871 |
| Ratio2 | 2939/4088 | 2954.068/4110.445 | 84,97,89,99,96 | 84.244,96.741,89.008,98.964,95.507 |
| Interimratio2 | 2684/3732 | 2680.638/3729.679 | 88,98,92,99,97 | 87.760,97.944,92.296,99.437,97.239 |

| S118 subgroup | Printed n .05/.01 | Diagnostic n .05/.01 | Printed powers:4000.05,4000.01,5000.05,5000.01 | Diagnostic powers sameorder |
|---|---|---|---|---|
| Age<80 | 2642/3658 | 2644.027/3662.921 | 89,73,95,85 | 88.978,72.846,94.860,84.477 |
| Age≥80 | 1135/1571 | 1129.398/1564.024 | 96,87,99,95 | 95.858,86.767,98.604,94.288 |
| Age<75 | 2924/4048 | 2905.288/4024.585 | 41,20,52,34 | 41.851,20.531,52.055,28.585 |
| Age≥75 | 1563/2164 | 1565.495/2168.427 | 100,98,100,100 | 99.557,97.723,99.926,99.480 |
| Male | 1458/2018 | 1457.054/2018.125 | 98,92,99,98 | 97.938,92.261,99.444,97.260 |
| Female | 2367/3276 | 2373.467/3288.083 | 80,60,89,75 | 80.517,59.595,89.005,72.889 |

All power inputs are displayed percentages converted to proportions. Complete half-unit interval envelope for the flagged cell: p0∈[.01175,.01185],p1∈[.02955,.02965],f∈[.245,.255],T=5000 gives 27.354722–29.840489%. This conservatively lets rates and fraction vary independently; enforcing ratio 2.5/patch×1.177 cannot enlarge it. Printed34% interval[33.5,34.5] is disjoint; intervalgap3.659511 percentagepoints/34=.107633. No other Table 4 cell has a relative discrepancy above.05 after its own half-unit interval. Sample-size outputs at all stated alphas also stay within threshold. Calculations used JavaScript arithmetic with Φ evaluated to better than approximately10⁻⁶ absolute precision; scientific Python was not used.

## Handoff and limitations

Pass-2 completion:52/52 groups revisited;0 new findings;24/24 original checker exclusion rows individually reconsidered;0 new excluded observations. The complete explicit per-S pass-2 facts and per-exclusion source reasoning are in [statistical_pass_2.md](../checkers/statistical_pass_2.md). Independent arithmetic is retained in [stat2-independent-computations.json](../preprocessing/stat2-independent-computations.json). All pass-1 component transcriptions and calculations below/above are preserved, rather than silently normalized.

For S118/C001, the fresh mechanical recheck and independent pass-2 full interval propagation supersede the narrower pass-1 endpoint envelope as the completion-stage conservative enclosure:27.225013–29.972805% after an outward .00002 percentage-point numerical guard; printed34% permits[33.5,34.5]%; relative minimum gap.103741>.05. This corroborates the pass-1 observation and introduces no source-transcription correction. The recheck's PLAN/PLAN, P_P, plan_material and reproduced classification agrees with source content. The original F-ST1-001 INCLUDE/C001 and F-XS-001 SCREENED_OUT records were revisited and not re-emitted; no new independent Route A or Route B issue was reproduced. Exact implementation/individual-data limitations remain named in the pass-2 artifact and do not constitute uncovered S groups.

Pass1 result:52 groups complete,1 finding(F-ST1-001),9 excluded apparent-observation rows in checkers/statistical_pass_1.md. All source units are represented by the fresh maps; no scientific coverage gap remains. Remaining mechanical limitations: unreported individual outcomes/permutation settings/CI constructions, log-rank O−E/V, full event timings/covariance and separate outcome-derivation/economic plans; no exact histogram coordinates are supplied. These limitations do not screen a reproduced interval–P conflict, count mismatch or reproducing-method discrepancy. Report and plan roles were assigned from content. Every candidate remains for independent screening and human adjudication; pass1 assigns no candidate IDs.

