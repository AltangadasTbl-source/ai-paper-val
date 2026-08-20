# Main quantitative evidence map — DOC-001

## Scope and evidence basis

Complete mapping of `jama_lapergue_2017_oi_170084.pdf`, PDF pp. 1-10 (printed pp. 443-452). Evidence was read only from the direct PDF and fresh assets `preprocessing/native_text/DOC-001.txt`, `preprocessing/layout_text/DOC-001.txt`, and `preprocessing/layout_text/DOC-001-p1.txt` through `DOC-001-p10.txt`; page renders `preprocessing/rendered_pages/DOC-001-p1.png`, `-p4.png`, `-p5.png`, `-p6.png`, `-p7.png`, and `-p8.png` were used for visual table/figure context. All locations below use the direct-PDF convention `jama_lapergue_2017_oi_170084.pdf#page=N`.

Relationship key conventions: `MAIN-N` maps numeric, count, population, scale, time, and label relationships; `MAIN-S` maps stated inferential/model relationships. “Observed” is source transcription; “Derived” is a reproducible diagnostic and is not a candidate judgment.

## Page coverage

| PDF page | Coverage outcome |
|---:|---|
| 1 | Abstract: complete quantitative result and repeated trial definition mapped. |
| 2 | Background/trial design, eligibility, randomization definitions mapped; no standalone result display. |
| 3 | Outcome, scale, sample-size, and statistical definitions mapped; no observed outcome result display. |
| 4 | Participant flow, analysis populations, and baseline narrative mapped. |
| 5 | Every Table 1 baseline value, denominators, and footnotes mapped. |
| 6 | Every Table 2 primary/secondary efficacy value, estimate, CI, P value, and footnote mapped. |
| 7 | Every Figure 2 display count/axis/footnote and repeated efficacy, adverse-event, and clinical-outcome narrative mapped. |
| 8 | Every Table 3 adverse-event value and footnote, unplanned result, and discussion repetitions mapped. |
| 9 | Quantitative discussion repetitions/limitations mapped; no new result display. |
| 10 | References only; no applicable article-result quantitative relationship. |

## Trial, population, definitions, and repeated abstract/narrative results

| Key | Exact locations / fresh asset | Observed evidence | Derived relationship / cross-reference |
|---|---|---|---|
| MAIN-N001 | p1 Abstract; p4 Results; p7 Results | Randomized: contact aspiration 192; stent retriever 189; total 381. | 192 + 189 = 381. Same assigned-group totals recur in Tables 1-3 and Figure 2. |
| MAIN-N002 | p1 Abstract | Trial period October 2015-October 2016; 8 French comprehensive stroke centers; anterior-circulation large-vessel occlusion within 6 h. | Population/time setting identifier for comparisons. |
| MAIN-N003 | p1 Abstract; p3 Outcomes | Primary outcome: proportion with successful revascularization, mTICI 2b or 3, at end of all endovascular procedures. | Defines the primary result identity. |
| MAIN-N004 | p1 Abstract; p4 Results | Mean age 69.9 y; 174 women (45.7%); 363 completed trial (95.3%); median symptom-onset-to-puncture 227 min (IQR 180-280). | 174/381 = 45.7%; 363/381 = 95.3%. |
| MAIN-N005 | p1 Abstract; p6 Table 2; p6 narrative | Primary result: 164/192 (85.4%) vs 157/189 (83.1%); OR 1.20 (95% CI 0.68-2.10); P=.53; risk difference 2.4% (95% CI −5.4% to 9.7%). | Repeated abstract/Table 2/narrative matched for population, contrast, and displayed precision. Raw percentage difference 85.4167−83.0688=2.35%, compatible with 2.4%. |
| MAIN-N006 | p1 Abstract; p6/p7 | Clinical outcomes named: NIHSS change at 24 h, mRS distribution at 90 d, mortality at 90 d, procedure-related serious adverse events; abstract states no significant differences. | Outcome/time labels carried into detailed entries below. |
| MAIN-N007 | p2 Methods | Inclusion: adults, anterior circulation occlusion, within 6 h; eligible artery intracranial ICA, MCA M1/M2; prestroke mRS >3 excluded; IV thrombolysis permitted. | Population definition relevant to Table 1 and primary outcome. |
| MAIN-N008 | p2 Methods | Allocation 1:1, computer random numbers, blocks of 4, stratified by center and IV tPA. | Randomization strata matches Table 2 adjustment label. |
| MAIN-N009 | p3 Methods | At least 3 attempts with assigned technique before rescue; primary successful revascularization mTICI 2b/3 after all endovascular treatment. | Defines “first-line” versus “all procedures”. |
| MAIN-N010 | p3 Outcomes | Secondary technical endpoints: mTICI 2b/3, 2c/3, or 3 after first-line; mTICI 2c/3 or 3 after all procedures; puncture-to-successful-revascularization time. Clinical endpoints: 90-d mRS (5+6 combined), mRS≤2, NIHSS change at 24 h, 90-d death. | Endpoint definitions used in Table 2 / Figure 2. |
| MAIN-N011 | p3 Outcomes | Symptomatic intracranial hemorrhage at 24 h: any ICH plus NIHSS worsening ≥4 or death. | Definition used for Table 3 symptomatic ICH. |
| MAIN-S001 | p3 Statistical Analysis | Design: 90% power; two-sided α=.05; superiority; expected stent success 70%; assumed absolute increase 15%; assumed spontaneous revascularization/catheterization failure 15%; required 380 total /190 per group. | Stated design calculation only; no recalculation attempted because its full formula/assumptions are not supplied. |
| MAIN-S002 | p3-p4 Statistical Analysis | ITT assigned-group analysis; categorical frequencies/%; quantitative mean(SD) or median(IQR); Shapiro-Wilk normality assessment. | Analysis/model labels used to distinguish statistics. |
| MAIN-S003 | p3-p4 Statistical Analysis | Primary comparison: mixed logistic regression, IV thrombolysis fixed and center random effects; adjusted OR/95% CI; absolute/relative risk differences from marginal probabilities (Austin method). Two-sided tests; P<.05 significant; no multiplicity adjustment and secondary objectives exploratory. | Explains adjusted Table 2 effect estimates; raw arithmetic is not expected to equal adjusted RD/OR exactly. |
| MAIN-S004 | p4 Statistical Analysis | Core-lab missing/poor quality: 4 groin failures treated mTICI 0; 20 unavailable/poor-quality core images used site mTICI. Per-protocol requires ≥3 assigned-treatment attempts; subgroup factors IV tPA, occlusion site, clot burden (<6/≥6); unplanned clot length (<8/≥8). | Population/handling definitions for sensitivity/subgroup results. |

## Figure 1 flow and analysis populations

| Key | Exact locations / fresh asset | Observed evidence | Derived relationship / diagnostic |
|---|---|---|---|
| MAIN-N012 | p4 Figure 1; `layout_text/DOC-001-p4.txt` | 640 assessed; 259 excluded: 253 did not meet inclusion criteria and 6 enrolled in another trial. | 640−259=381 randomized. |
| MAIN-N013 | p4 Figure 1 | Did-not-meet-criteria components: posterior circulation 61; cervical carotid occlusion 113; onset-to-randomization >6 h 77; mRS >3 2. | 61+113+77+2=253. |
| MAIN-N014 | p4 Figure 1 | Contact: 192 randomized; 174 received assigned contact aspiration; 18 did not (15 spontaneous clot lysis, 3 groin access failure). Stent: 189 randomized; 170 received assigned stent; 19 did not (12 spontaneous lysis, 1 groin failure, 5 mistakenly contact aspiration/protocol violation, 1 extracranial stenting without stent). | Contact: 174+18=192; 15+3=18. Stent:170+19=189; 12+1+5+1=19. |
| MAIN-N015 | p4 Figure 1; p6 narrative/Table 2 footnote | Core-lab primary-endpoint data: 181 contact and 176 stent; not core-lab adjudicated: 11 (8 poor images, 3 groin failure) and 13 (12 poor images, 1 groin failure). | 181+11=192; 176+13=189; 181+176=357=93.7% of 381 (p6 narrative). |
| MAIN-N016 | p4 Figure 1; p7 Clinical Efficacy | 90-d status: contact 181 died/completed, 11 lost; stent 182 died/completed, 6 lost, 1 withdrew. | 181+11=192; 182+6+1=189; outcome assessment 181+182=363 (95.3%). |
| MAIN-N017 | p4 Results narrative | Mean baseline NIHSS 16.2 (SD 6.2); median onset-to-puncture 227 min (IQR 180-280); balance except age, admission systolic BP, prestroke mRS, occlusion site. | Matches overall values in abstract / group values in Table 1. |

## Table 1 baseline characteristics (all displayed values)

Source for entries MAIN-N018–MAIN-N031: p5 Table 1 and its footnotes; fresh `layout_text/DOC-001-p5.txt` and render `rendered_pages/DOC-001-p5.png`. Each pair is contact aspiration (n=192) / stent retriever (n=189).

| Key | Observed values | Derived diagnostic / definition |
|---|---|---|
| MAIN-N018 | Age mean(SD), y: 71.7(13.8) / 68.1(14.6); men:103/192(53.7) /104/189(55.0). | Percentages reconcile (rounded). |
| MAIN-N019 | Hypertension 118/186(63.4)/111/187(59.4); diabetes 36/185(19.5)/40/188(21.3); hypercholesterolemia 65/184(35.3)/66/187(35.3); smoking 31/158(19.6)/31/163(19.0). | Numerator/denominator percentages reconcile (rounded); varying denominators are observed missingness, not pooled totals. |
| MAIN-N020 | Coronary disease 30/183(16.4)/33/186(17.7); prior stroke/TIA 36/186(19.4)/29/188(15.4); prior antithrombotic 91/185(49.2)/91/187(48.7); antiplatelet 58/185(31.4)/60/187(32.1); anticoagulant 37/185(20.0)/35/187(18.7). | Percentages reconcile; antiplatelet/anticoagulant are not specified as mutually exclusive. |
| MAIN-N021 | Systolic BP mean(SD) mm Hg:150(24)/145(26); NIHSS mean(SD):16.3(5.9)/16.1(6.5). | NIHSS range footnote: 0=no deficit to 42=most severe; 3 missing, 1 contact. |
| MAIN-N022 | Prestroke mRS 0:158/190(83.2)/159/189(84.1); 1:17/190(8.9)/16/189(8.5); 2:5/190(2.6)/11/189(5.8); 3:8/190(4.2)/3/189(1.6); >3:2/190(1.0)/0. | Contact counts 158+17+5+8+2=190; stent 159+16+11+3=189. mRS scale 0 symptom-free to 6 dead. |
| MAIN-N023 | ASPECTS median(IQR):7(6-9)/7(5-9). | Scale 0-10, higher=fewer early ischemic changes; 5 missing, 1 contact. |
| MAIN-N024 | Occlusion M1:100/174(57.5)/104/176(59.1); M2:48/174(27.6)/31/176(17.6); intracranial ICA:22/174(12.6)/33/176(18.7); tandem:4/174(2.3)/8/176(4.6). | Each group sum:174 and176. Footnote says unavailable for spontaneous lysis n=27 or groin failure n=4, so 381−31=350; displayed denominators sum 350. |
| MAIN-N025 | Clot burden median(IQR):7(5-8)/6(3-8); clot length mm:13.0(9.0-19.0)/11.5(8.0-18.0). | Clot-burden scale 0-10 and lower=higher burden; 254 assessed (129 contact); clot length 293 assessed (147 contact), consistent with group totals by subtraction. |
| MAIN-N026 | Arterial occlusion lesion score 0:153/177(86.4)/160/175(91.4); 1:1/177(0.6)/2/175(1.1); 2:13/177(7.3)/8/175(4.6); 3:10/177(5.7)/5/175(2.9). | Each category sum=177 /175; scale 0=no revascularization, 3=complete. |
| MAIN-N027 | Favorable collaterals:37/146(25.3)/37/138(26.8). | Collateral scale 0-4; favorable=3-4. Percentages reconcile. |
| MAIN-N028 | Suspected cause: large-artery atherosclerosis13/192(6.8)/17/189(9.0); cardioembolic88/192(45.8)/75/189(39.7); other/unknown91/192(47.4)/97/189(51.3). | Counts sum to randomized denominators in each group; rounded percentages total 100.0. |
| MAIN-N029 | Direct comprehensive-center admission70/192(36.5)/68/189(36.0); IV rtPA126/192(65.6)/124/189(65.6); general anesthesia21/191(11.0)/25/188(13.3). | Percentages reconcile; footnote k says 3 missing, 1 contact (denominators total379). |
| MAIN-N030 | Onset-to-groin puncture min median(IQR):217(166-279)/235(186-283); onset-to-imaging109(82-146)/116(85-150); imaging-to-randomization86(43-132)/82(40-135); randomization-to-puncture11(5-25)/13(5-23). | Time units explicitly minutes. |
| MAIN-N031 | Table 1 footnotes: 13 unspecified missing (6 contact); table-specific missingness and denominator definitions as recorded in MAIN-N021–N030. | No internal arithmetic contradiction identified in mapped Table 1 totals under stated missingness. |

## Table 2 efficacy outcomes (all displayed values)

Source for entries MAIN-N032–MAIN-N047 and MAIN-S005–MAIN-S012: p6 Table 2 and footnotes; fresh `layout_text/DOC-001-p6.txt` and render `rendered_pages/DOC-001-p6.png`. All ORs/RDs are adjusted for center and IV thrombolysis unless stated; therefore derived raw percentage differences are checks of displayed proportions, not substitutes for adjusted effects.

| Key | Observed values: contact / stent; effect (95% CI); P | Derived diagnostic / repeated occurrence |
|---|---|---|
| MAIN-N032 / MAIN-S005 | Primary ITT core-lab mTICI2b/3:164/192(85.4)/157/189(83.1); RD2.4(−5.4 to9.7); OR1.20(0.68-2.10); .53. | Same result MAIN-N005; 164/192 and157/189 reconcile; OR CI contains1. |
| MAIN-N033 / MAIN-S006 | Per-protocol mTICI2b/3:140/153(91.5)/140/165(84.9); RD6.8(−0.6 to14.11); OR1.91(0.93-3.91); .08. | Percentages reconcile; CI contains null for RD/OR. Endpoint population differs from ITT. |
| MAIN-N034 / MAIN-S007 | Study-site mTICI2b/3:163/192(84.9)/163/189(86.2); RD−1.4(−8.3 to5.5); OR0.90(0.50-1.59); .71. | Unplanned sensitivity; percentages reconcile; CI contains null. |
| MAIN-N035 / MAIN-S008 | All-procedure mTICI3:72/192(37.5)/73/189(38.6); RD−1.1(−11.0 to9.0); OR0.95(0.62-1.45); .82. | Percentages reconcile; CI contains null. |
| MAIN-N036 / MAIN-S009 | All-procedure mTICI2c/3:108/192(56.3)/107/189(56.6); RD0.4(−10.9 to9.7); OR0.99(0.65-1.48); .84. | Percentages reconcile; CI contains null. |
| MAIN-N037 / MAIN-S010 | First-line mTICI2b/3:121/192(63.0)/128/189(67.7); RD−4.7(−13.8 to4.4); OR0.81(0.53-1.24); .34. | Percentages reconcile; CI contains null. |
| MAIN-N038 / MAIN-S011 | First-line mTICI3:55/192(28.7)/67/189(35.5); RD−6.8(−16.2 to2.5); OR0.73(0.54-1.13); .16. | Percentages reconcile; CI contains null. |
| MAIN-N039 / MAIN-S012 | First-line mTICI2c/3:83/192(43.2)/94/189(49.7); RD−6.5(−16.4 to3.3); OR0.77(0.51-1.16); .21. | Percentages reconcile; CI contains null. |
| MAIN-N040 / MAIN-S013 | Rescue treatment:63/192(32.8)/45/189(23.8); RD9.0(−0.9 to18.1); OR1.57(0.99-2.47); .05. | Percentages reconcile; reported CI includes null. |
| MAIN-N041 / MAIN-S014 | NIHSS 24-h mean change(95%CI):−4.8(−6.1 to−3.6)/−5.2(−6.5 to−3.9); mean difference0.38(−1.42 to2.18); P=.68. | 23 missing (12 contact); mean change and mean difference adjusted for baseline NIHSS; interval contains0. |
| MAIN-N042 / MAIN-S015 | Functional independence at3mo mRS≤2:82/181(45.3)/91/182(50.0); RD−4.6(−14.7 to6.1); OR0.83(0.54-1.26); .38. | Percentages reconcile and denominators = complete/death follow-up groups; CI contains null. |
| MAIN-N043 / MAIN-S016 | 3-mo mRS median(IQR):3.0(1.0-5.0)/2.5(1.0-5.0); common OR improvement 1 point=0.76(0.53-1.10); .15. | mRS ordinal shift scale; CI contains1. |
| MAIN-N044 | p6 Table 2 footnotes | mTICI categories: 0 no perfusion;1 penetration/no perfusion;2a distal filling<50%;2b substantial filling≥50%;2c near complete;3 complete. Core lab absent11 contact/13 stent due groin failure or unavailable/poor images. | Outcome-scale labels and missingness required for Table/Figure matching. |
| MAIN-N045 | p6 narrative | Core lab assessed357/381(93.7%), 181 contact/176 stent; balloon-guide catheter used in92% of stent group; primary outcome repeated exactly. | 181+176=357; source gives no numerator for 92%, so no count derivation. |
| MAIN-N046 / MAIN-S017 | p7 narrative | Rescue used63/192(32.8)/45/189(23.8), OR1.57(0.99-2.47), P=.05; among119 first-line failures (68/51), rescue57(83.8%)/42(82.4%), OR1.21(0.43-3.38), P=.72. | 68+51=119; 57/68=83.8%,42/51=82.4%; CIs contain1. |
| MAIN-N047 / MAIN-S018 | p7 narrative | Attempts median(IQR; range):2(1-4;0-11)/2(1-3;0-15), P=.84; among primary-outcome patients puncture-to-revascularization min:38(24-60)/45(31-60), P=.10. | Different denominators not printed for time subset; no ungrounded reconstruction. |

## Figure 2 distributions and display-label diagnostic

| Key | Exact locations / fresh asset | Observed evidence | Derived diagnostic |
|---|---|---|---|
| MAIN-N048 | p7 Figure2A; `layout_text/DOC-001-p7.txt`; render p7 | All-procedure stacked display, contact: 8,2,18,92,72 for mTICI 0,1,2a,2b,3; stent:5,5,22,84,73. Axis label “Patients, %”; group labels n=192/189. | Contact segments sum192; stent segments sum189. mTICI2b+3=164 and157, exactly Table2 primary counts. |
| MAIN-N049 | p7 Figure2B | First-line stacked display, contact:26,6,39,66,55; stent:20,9,32,61,67, for mTICI0,1,2a,2b,3; axis “Patients, %”; group n=192/189. | Sums192 and189; mTICI2b+3=121 and128, exactly Table2. |
| MAIN-N050 | p7 Figure2 footnotes | mTICI simplified labels:0 no revascularization,1 minimal,2 partial (2a<50%,2b≥50%),3 complete. Core-lab assessment; 4 groin failures treated mTICI0; no core read replaced by study-site result n=20 all-procedure/n=22 first-line. | Supports Figure/Table comparison; all-procedure 20 matches p4 missing core lab image count. |
| MAIN-N051 | p7 Figure2A-B | Numbers printed within stacked bars are whole numbers that sum to group n, while horizontal axis is labelled “Patients, %.” | **Candidate signal (not a candidate ID):** label/count ambiguity. The bar geometry/axis uses percentages but internal labels behave as counts (e.g., Figure2A contact 8+2+18+92+72=192). Human review should determine whether the figures intentionally combine percentage scale with unlabelled counts or whether a count/percent label was omitted/misapplied. |

## Clinical efficacy, adverse events, Table 3, and discussion repetitions

| Key | Exact locations / fresh asset | Observed evidence | Derived diagnostic / cross-reference |
|---|---|---|---|
| MAIN-N052 / MAIN-S019 | p7 Clinical Efficacy; p6 Table2 | NIHSS change −4.8(−6.1 to−3.6) vs−5.2(−6.5 to−3.9); difference0.38(−1.42 to2.18), P=.68. 363/381(95.3%) mRS assessed; mRS≤2 45.3% vs50.0%, OR0.83(0.54-1.26), P=.38, RD−4.6%(−14.7 to6.1); shift OR0.76(0.53-1.10),P=.15. | Repeats Table2 values at same stated precision; no mismatch. |
| MAIN-N053 | p7 Adverse Events | 3-mo death70/363(19.3%); ICH24h87/188(46.3%) contact and85/188(46.2%) stent; symptomatic ICH10/188(5.3%) and12/188(6.5%); procedure-related adverse events31/192(16.2%) and30/189(15.9%). | 35+35 Table3 deaths=70; 70/363=19.3%. Stent ICH and symptomatic-ICH percentages do not reproduce from the printed /188 fractions: 45.2% and 6.4% at one decimal, respectively. |
| MAIN-N054 | p7 Adverse Events; p8 Table3 | Most frequent events pooled: subarachnoid hemorrhage n=26, vasospasm17, embolization new territory12, perforation8, dissection7. New ischemic stroke different territory10/188(5.3%) vs16/188(8.5%). | Pooled totals equal Table3 pairs:13+13=26;5+12=17;7+5=12;5+3=8;5+2=7. |
| MAIN-N055 | p8 Table3; fresh `layout_text/DOC-001-p8.txt`, render p8 | Death35/181(19.3)/35/182(19.2); ICH24h87/188(46.3)/85/188(46.2); hemorrhagic infarction58/188(30.9)/49/188(26.6); type1 23/188(12.2)/24/188(13.0); type2 35/188(18.6)/25/188(13.6). | Death total=70; hemorrhagic-infarction components sum 58/49. In the stent column, the four displayed percentages for ICH, hemorrhagic infarction, type 1, and type 2 do not reproduce from the printed /188 fractions. |
| MAIN-N056 | p8 Table3 | Parenchymal hematoma24/188(12.8)/33/188(17.4); type1 17/188(9.0)/19/188(10.3); type2 7/188(3.7)/14/188(7.6); intraventricular hemorrhage6/188(3.2)/2/184(1.1); remote ICH1/188(0.5)/1/184(0.5). | Parenchymal components sum24/33. In the stent column, parenchymal total, type 1, and type 2 percentages do not reproduce from the printed /188 fractions. The explicit /184 intraventricular and remote rows reconcile. |
| MAIN-N057 | p8 Table3 | Symptomatic ICH10/188(5.3)/12/188(6.5); procedure related events31/192(16.2)/30/189(15.9); embolization7/192(3.7)/5/189(2.7); perforation5/192(2.6)/3/189(1.6); dissection5/192(2.6)/2/189(1.1); vasospasm5/192(2.6)/12/189(6.4); SAH13/188(6.9)/13/188(7.1); new ischemic stroke10/188(5.3)/16/188(8.5). | Stent symptomatic ICH and subarachnoid hemorrhage percentages do not reproduce from their printed /188 fractions. The other listed fractions reconcile. Procedure-event components need not sum to patient totals because patients may have multiple event types. |
| MAIN-N058 | p8 Table3 footnotes | Core-lab assessment; multiple events of one type counted once. Definitions: HI1 isolated petechiae/no mass effect; HI2 confluent petechiae/no mass effect; PH1 <30% infarcted area/mild effect; PH2 >30%/significant effect. | Definitions and counting rule prevent improper component-total comparison. |
| MAIN-N059 / MAIN-S020 | p8 Unplanned analyses | No heterogeneity by clot length; no group difference with local mTICI sensitivity. Clot-contact-to-revascularization median13 min(IQR6-38) vs22(10-38), P=.03, exploratory/not prespecified. | Explicit exploratory/model qualification; no effect estimate supplied. |
| MAIN-N060 | p8 Discussion | 381 participants, 8 centers; first-line contact aspiration not superior. 90% received allocated treatment; 2 combined technique instances contact and8 stent during rescue. | 174+? allocation: p4 flow supports treatment crossovers; “90%” is rounded narrative. |
| MAIN-N061 | p8-p9 Discussion | Primary measure is difference in revascularization after all procedures; successful revascularization specifically mTICI2b/3. Discussion states no group differences in mTICI3 or new-territory embolization; hypothesis expected15% increase; trial not designed equivalence/noninferiority; secondary/adverse outcomes no significant group differences. | Qualitative repetitions align with Table2/3 directions; no numerical contradiction observed. |
| MAIN-N062 | p9 Discussion | Retrospective comparison values: symptomatic hemorrhage2.9% contact/5.4% stent; other retrospective embolization2%; this study embolization different territory3.7% contact vs prior reports6%/5.7%. | External-study contextual figures are not matched trial outcomes; in-study 3.7% matches Table3 7/192. |
| MAIN-N063 | p9 Limitations/conclusion | Superiority design targeted15% primary difference; not powered for a smaller difference or subgroup analyses; conclusion: no higher successful revascularization rate. | Qualitative conclusion matches primary effect whose CI crosses null. |

## Candidate-signal register (provisional only; no C IDs or judgments)

| Signal | Linked key | Observation and reproducible rule |
|---|---|---|
| SIG-MAIN-001 | MAIN-N051 | Figure 2 bars are explicitly scaled “Patients, %,” but their embedded integers sum exactly to each group sample size and reproduce Table 2 counts. This is a possible count-versus-percentage display-label ambiguity. Exact source location: `jama_lapergue_2017_oi_170084.pdf#page=7`. |

## Completion summary

Mapped relationship keys: 63 numeric/reporting (`MAIN-N001`–`MAIN-N063`) and 20 inferential/statistical (`MAIN-S001`–`MAIN-S020`). Candidate signals: 1. Page 10 has no applicable article-result relationship; all other pages were mapped as above. Limitations: exact line coordinates are unavailable from the PDF assets; page, table/figure, row, footnote, and repeated narrative location are recorded. No legacy audit derivatives or external sources were used.
