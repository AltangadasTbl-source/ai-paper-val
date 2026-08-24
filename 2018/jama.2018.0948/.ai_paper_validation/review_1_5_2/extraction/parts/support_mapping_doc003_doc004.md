# Fresh support quantitative evidence map: DOC-003 and DOC-004

## Scope, method, and mapper handles

This is a fresh, source-first map limited to `joi180015supp2_prod.pdf` (DOC-003, pp. 1-7) and `joi180015supp3_prod.pdf` (DOC-004, pp. 1-14). Native and layout text plus the newly rendered assigned pages were used; no legacy audit derivative, other mapper artifact, external source, or web material was used. PDF page numbers below are the printed PDF pages. `N-D3-*` and `N-D4-*` are mapper-local numeric/reporting handles; `S-D3-*` and `S-D4-*` are mapper-local statistical handles. They are not global IDs.

**Coverage result:** all 21 assigned PDF pages were read. DOC-003 has analysis specifications but no observed trial-result table. DOC-004 has two figures, definitions, three hospital-level table blocks, one ICU table, and one assumptions/calculation table. No candidate is registered by this mapper; possible leads are preserved without disposition at the end.

## DOC-003 — SAP / analysis plan (pp. 1-7)

### Outcome units, denominators, and primary models

| Local handle | Source evidence and reproducible relationship |
|---|---|
| N-D3-01 / S-D3-01 | **p. 1, lines 6-19:** Primary analysis is hospital-level; every hospital contributes baseline and intervention observations. A binary outcome is experienced at most once per patient (example: hospital mortality); its numerator is hospital-period events and denominator hospital-period discharges. A count outcome may be experienced more than once (example: clinical deterioration events); its numerator is hospital-period events and denominator hospital-period patient-days. GEE accounts for hospital clustering with exchangeable correlation. |
| S-D3-02 | **pp. 1-2:** Binary outcomes have two GEE binomial analyses using events `x` and discharges `n`: logit link (log odds) and identity link (probability). Predictors are intervention indicator and the hospital's baseline log odds or baseline probability, respectively. Printed group-level code is `geeglm(cbind(x,n-x) ~ Intervention + logitBaseline, id=Hospital, family=binomial, corstr="exchangeable")`; identity-link code uses `probBaseline` and `family=binomial(link=make.link("identity"))`. The separately displayed individual-level identity-link code is `geeglm(y ~ Intervention + probBaseline, id=Hospital, family=binomial(link=make.link("identity")), ...)`, where `y=1` for outcome and 0 otherwise. |
| N-D3-02 | **p. 2 code comments:** for a baseline logit, add 0.5 to the numerator and 1 to the denominator if `x=0`. This is a stated transformation for the baseline covariate, not a displayed event-rate result. |
| S-D3-03 | **pp. 2-3:** Count outcomes have two GEE Poisson analyses using events `x` and patient-days `time`: log link models log rate; identity link models rate. Both include patient-days. Log link uses log(patient-days) as offset; identity-link implementation uses re-arranged time-at-risk terms. Predictors are intervention and hospital baseline log rate or baseline rate. |
| N-D3-03 / S-D3-04 | **p. 3 code/comments:** `N` is post-randomization patient-days; `x` is post-randomization events; `logBaseline` is log baseline rate and adds 0.5 to the numerator when `x=0`; `Baseline` is baseline rate. Printed log-rate code reads `geeglm(x ~ offset(log(N)+Intervention + logBaseline, id=Hospital, family=poisson, data=EPOCH, corstr="exchangeable"))`. Printed identity-link setup is `Nlin=N/1000`, `GNlin=N*(d$Group=="BedsidePEWS")`, and `BNlin=N*Baseline`; its stated coefficients are usual-care intercept, rate difference, and increment per unit baseline rate. Printed identity-link model is `geeglm(x ~ Nlin+GNlin+BNlin-1, id=Hospital, family=poisson("identity"), data=EPOCH, corstr="exchangeable")`. `N/1000` establishes the displayed rate scale for that model. |
| S-D3-05 | **p. 4:** Patient-level continuous outcomes in Tables 2 and S4 use GEE Gaussian models. The stated structure is `geeglm(x ~ Intervention + x0, id=Hospital, data=EPOCH, corstr="exchangeable")`; `x0` is the hospital baseline mean for the patient outcome. The plan says large sample size and GEE robustness make mean comparisons largely unaffected by individual-level non-normality. |

### Sensitivity, subgroup, and ICU specifications

| Local handle | Source evidence and reproducible relationship |
|---|---|
| S-D3-06 | **pp. 4-5:** Sensitivity analyses for odds ratios, probabilities, and rate ratios: post-intervention-only GEE; post-only GLMER; GEE and GLMER with pre/post outcomes and time×intervention interaction; post-only GEE and GLMER adjusted for baseline; weighted linear logits/log-rates using weight `1/variance(logit)` or `1/variance(log-rate)` and baseline covariate; and quasi-binomial logistic or quasi-Poisson post models with baseline logit/log-rate. |
| S-D3-07 | **p. 5:** Probability/rate sensitivity analyses: post-only identity-link binomial/Poisson GEE; pre/post identity-link GEE with time×intervention; post-only identity-link GEE baseline-adjusted; weighted linear post-probability/rate model with inverse variance weight and baseline covariate; and quasi-binomial/Poisson identity-link post regression with baseline probability/rate. |
| N-D3-04 | **p. 5 shell table:** planned count/rate outcomes are resuscitation-team calls, stat calls, urgent ICU consultations, urgent ICU admissions (each baseline/post events over patient-days), unplanned ICU readmissions (events over ICU discharges), and unplanned hospital readmissions (events over hospital discharges); all are marked Poisson. This distinguishes rates/counts and their denominators. |
| S-D3-08 | **p. 6:** ECMO-service and MET-service subgroup analyses use the preceding methodology. Each estimates BedsidePEWS versus usual-care effect in service-present and service-absent hospital groups; a one-term treatment×subgroup interaction in one GEE assesses subgroup effect. |
| N-D3-05 / S-D3-09 | **p. 7:** ICU analysis is patient-level, with source data having one record per ICU admission. A patient may have multiple admissions; people admitted to the same ICU in both study periods are eliminated, and analysis has one record per patient. Per-patient variable definitions: total LOS=sum admission LOS; mean LOS=average admission LOS; PIM at admission=average PIM; PIM II predicted mortality (/1000 urgent ICU discharges)=average admission probability (inverse-logit PIM); ventilator-free days=first admission; technology days=sum mechanical-ventilation, nitric-oxide, ECMO, and dialysis days; technology use=any-day binary indicator for HFOV/ECMO/NO/dialysis/MV; 24-hour PELOD=average first-24-hour PELOD; PELOD ICU stay=average whole-admission PELOD. |

### DOC-003 checks and mapper-local lead

The plan supplies model families, links, units, baseline adjustments, and clustering but no estimate, interval, P value, or result count to reconcile. Definitions distinguish binary risk/probability, odds, counts, rates, and continuous means. **No candidate registered.**

**Lead L-D3-01 (no disposition):** p. 3's printed log-rate expression places `Intervention + logBaseline` inside `offset(log(N)+...)`, whereas surrounding prose says patient-days enter as the log-link offset and intervention/baseline are predictors. The expression also appears to have unmatched parentheses. Exact source comparison is the p. 3 prose/code, but the supplied source alone does not establish whether this is a transcription/layout code error or executable intended code. Preserve for coordinator/statistical review; do not treat as a candidate without the required reproducible reporting contradiction.

## DOC-004 — definitions and figures (pp. 1-8)

| Local handle | Source evidence and quantitative meaning |
|---|---|
| N-D4-01 | **p. 2 Figure S1; p. 3 caption:** all-cause hospital mortality is deaths per 1,000 hospital discharges, baseline on x-axis and post-randomization on y-axis. Each circle is a hospital; circle size is post-period discharges. A-J are BedsidePEWS (A, C, H extended run-in) and K-U usual care. Identity line means equal period rates. Fitted intervention and usual-care lines are visually coincident; caption states this is consistent with no significant primary-analysis difference and baseline-adjusted absolute difference `0.01 per 1,000 patient discharges` (the caption's wording says patient discharges while the figure title says hospital discharges). |
| N-D4-02 | **pp. 4-5 Figure S2:** weekly per-hospital random sample of five ward inpatients admitted at least 24 hours; seven reviewed observation types (heart rate, respiratory rate, systolic BP, saturation, respiratory effort, capillary refill, oxygen therapy). The most recent same-time set is scored 0-7; `0` can occur when only temperature is documented and `7` when all BedsidePEWS types are used. Post-period sample `5,420 = 2,588` BedsidePEWS + `2,832` usual-care patients. Histogram is relative-frequency distribution; caption reports proportion with >=5 types significantly greater in BedsidePEWS, but supplies no numeric test statistic/P value. |
| N-D4-03 | **pp. 6-8 eTable 1:** definitions: hospital mortality includes eligible-inpatient deaths including DNR; mortality-without-DNR excludes documented DNR at death. Significant clinical deterioration/late ICU admission is composite of specified ventilation, fluid/inotrope/vasopressor, CPR/ECMO, or qualifying death components; cardiac arrest is a non-DNR low/absent-output event requiring/meeting the specified chest-compression/death criteria and is a subset of the deterioration event; potentially preventable arrest is blinded two-reviewer rating 4-6. Urgent ICU admission is departure <6 h after initiation; unplanned ICU/hospital readmission is before midnight of second full calendar day (before third midnight). |
| N-D4-04 | **pp. 7-8 eTable 1:** ventilator-free days are alive/non-invasive-MV days in the 28 days from ICU admission, first ICU admission per period. Documentation frequency is 24-h frequency of the seven score observations in five randomly selected eligible patients/week/hospital. ICU LOS and technology day definitions use whole/part study or calendar days as printed; PELOD ranges 0-71, higher=worse dysfunction. PIM-2 uses first 12 h of urgent ICU data, higher=worse death probability; minimum `-8.4137` = `0.02%`, illustrative PIM `+9.7778` with PaO2 `40` and BE `-35` = `99.9%`. |

## DOC-004 — eTable 2 mortality matrix (pp. 9-10)

**N-D4-05.** Columns are baseline/post/total discharges, then mortality and mortality-without-DNR as `n (per 10^3 discharges)`. Exact hospital rows, `baseline,post,total | mortality B,P | no-DNR B,P`:

```text
BedsidePEWS: A 467,837,1304 | 0(0),0(0) | 0(0),0(0)
B 677,1643,2320 | 0(0),2(1.22) | 0(0),0(0)
C 663,1250,1913 | 4(6.03),1(0.80) | 2(3.02),1(0.80)
D 1256,2915,4171 | 4(3.18),2(0.69) | 2(1.59),0(0)
E 2131,4287,6418 | 6(2.82),9(2.10) | 5(2.35),6(1.40)
F 4143,8049,12192 | 3(0.72),3(0.37) | 1(0.24),1(0.12)
G 3689,7037,10726 | 9(2.44),18(2.56) | 3(0.81),3(0.43)
H 2022,4034,6056 | 5(2.47),21(5.21) | 0(0),13(3.22)
I 6698,11370,18068 | 8(1.19),22(1.93) | 8(1.19),14(1.23)
J 4918,8751,13669 | 13(2.64),19(2.17) | 5(1.02),4(0.46)
All 26664,50173,76837 | 52(1.95),97(1.93) | 26(0.98),42(0.84)
Usual care: K 3472,7285,10757 | 4(1.15),6(0.82) | 1(0.29),1(0.14)
L 2526,5642,8168 | 0(0),5(0.89) | 0(0),2(0.35)
M 1978,3811,5789 | 0(0),12(3.15) | 0(0),2(0.52)
N 1762,3672,5434 | 2(1.14),2(0.54) | 1(0.57),0(0)
O 2232,4638,6870 | 2(0.90),5(1.08) | 0(0),1(0.22)
P 2819,5471,8290 | 4(1.42),17(3.11) | 1(0.35),7(1.28)
Q 3497,6440,9937 | 6(1.72),9(1.40) | 1(0.29),4(0.62)
R 3545,7327,10872 | 6(1.69),7(0.96) | 1(0.28),2(0.27)
S 3266,5886,9152 | 3(0.92),9(1.53) | 0(0),6(1.02)
T 13308,26956,40264 | 11(0.83),21(0.78) | 7(0.53),8(0.30)
U 8313,17238,25551 | 23(2.77),54(3.13) | 4(0.48),14(0.81)
All 46718,94366,141084 | 61(1.31),147(1.56) | 16(0.34),47(0.50)
```

Checks: each displayed hospital total equals baseline+post; group totals equal their hospital-row sums; displayed rates equal `1,000*n/period discharges` to shown rounding (e.g., BedsidePEWS post mortality `97/50,173*1,000=1.933`, usual-care post `147/94,366*1,000=1.558`). No-DNR counts do not exceed all mortality. Footnote specifies discharges are rate denominators; A-J and K-U group/rank labels identify cross-table linkage to eTable 3 and Figure S1.

## DOC-004 — eTable 3 event-rate matrix (p. 11)

**N-D4-06.** Columns are baseline/post patient-days and, for each outcome, `n (per 10^3 patient-days)` in baseline/post. Exact values are retained in the direct table; compact row map below is `hospital: Bdays,Pdays | SCDE B,P | arrest B,P | preventable arrest B,P`.

```text
A:1133,2270|0(0),0(0)|0(0),0(0)|0(0),0(0)       B:1876,5135|1(.53),0(0)|0,0|0,0
C:5283,10443|4(.76),8(.77)|2(.38),1(.10)|2(.38),1(.10)
D:4965,9555|11(2.22),11(1.15)|1(.20),2(.21)|1(.20),2(.21)
E:8662,17779|9(1.04),15(.84)|0,1(.06)|0,1(.06) F:10392,23522|5(.48),7(.30)|2(.19),3(.13)|1(.10),2(.09)
G:17238,34438|19(1.10),23(.67)|5(.29),9(.26)|4(.23),8(.23)
H:23244,47145|13(.56),21(.45)|2(.09),3(.06)|1(.04),2(.04)
I:30571,56231|10(.33),23(.41)|2(.07),5(.09)|1(.03),3(.05)
J:26336,45341|8(.30),19(.42)|1(.04),3(.07)|1(.04),2(.04)
Bedside All:129700,251859|80(.62),127(.50)|15(.12),27(.11)|11(.08),21(.08)
K:10164,22431|5(.49),8(.36)|1(.10),0|1(.10),0 L:6655,13034|13(1.95),27(2.07)|1(.15),0|0,0
M:8941,16388|4(.45),18(1.10)|0,3(.18)|0,3(.18) N:8917,16888|1(.11),1(.06)|1(.11),0|1(.11),0
O:11705,22810|6(.51),13(.57)|1(.09),2(.09)|1(.09),1(.04) P:12126,22113|3(.25),5(.23)|2(.16),2(.09)|2(.16),2(.09)
Q:13335,25093|11(.82),10(.40)|2(.15),4(.16)|1(.07),4(.16) R:16077,33678|9(.56),17(.50)|2(.12),4(.12)|2(.12),4(.12)
S:14304,24762|1(.07),5(.20)|0,0|0,0 T:28698,49117|41(1.43),62(1.26)|2(.07),5(.10)|1(.03),4(.08)
U:31575,61270|50(1.58),93(1.52)|6(.19),12(.20)|3(.10),11(.18)
Usual All:162497,307584|144(.89),259(.84)|18(.11),32(.10)|12(.07),29(.09)
```

Checks: group patient-day totals equal row sums; all printed rates are compatible with `1,000*n/patient-days` to precision (e.g., `127/251,859*1,000=.504`, `259/307,584*1,000=.842`). Preventable-arrest counts never exceed cardiac-arrest counts. Footnote defines patient-days as denominators and identifies A-U linkage. `80ß(0.62)` is a text-extraction glyph; rendered source displays the count as 80.

## DOC-004 — eTable 4 ICU resource utilization (pp. 12-13)

**N-D4-07 / S-D4-01.** Columns are BedsidePEWS baseline/post (`393`,`686` urgent ICU admissions) and usual-care baseline/post (`531`,`967`), followed by adjusted difference (95% CI) and P value. Exact rows, in that order:

```text
Mortality: 31(7.9%),42(6.1%),28(5.3%),67(6.9%) | -1.55 (-4.90,1.80), P=.36
PIM-2 predicted mortality: 21(5.4%),38(5.5%),25(4.8%),44(4.6%) | .69 (-.54,1.92), P=.27
PIM-2 mean(SD): -4(1.6),-3.9(1.5),-3.9(1.4),-3.9(1.3) | .13 (-.11,.37), P=.29
ICU total LOS mean(SD): 8.6(14.6),9.4(14.2),9.4(14.5),9(15) | 1.28 (-.97,3.53), P=.27
ICU total LOS median(IQR): 4(2,8),4(2,9),5(2,9.5),4(2,9) | no comparison
ICU mean LOS mean(SD): 7.4(12.3),7.8(11.2),8(12.4),7.4(12) | 1.04 (-.91,2.99), P=.29
ICU mean LOS median(IQR): 4(2-8),4(2-8),4(2-8),4(2-8) | no comparison
Ventilator-free days mean(SD): 23.7(8.0),23.9(7.8),24.3(7.0),24(7.6) | .26 (-1.04,1.57), P=.69
Ventilator-free days median(IQR): 28(23,28),28(24,28),28(24,28),28(24,28) | no comparison
MV days mean(SD): 3.9(10.6),4.1(10.1),4(10.3),3.7(10.3) | .69 (-.99,2.36), P=.42
MV use:164(41.7%),287(41.8%),220(41.4%),400(41.4%) | -.93 (-7.46,5.61), P=.78
HFOV use:23(5.9%),25(3.6%),15(2.8%),30(3.1%) | -1.17 (-2.52,.19), P=.09
Nitric oxide:19(4.8%),27(3.9%),20(3.8%),29(3.0%) | -.38 (-1.91,1.15), P=.63
ECMO:10(2.5%),9(1.3%),6(1.1%),17(1.8%) | -1.03 (-2.45,.38), P=.15
Dialysis:9(2.3%),27(3.9%),12(2.3%),27(2.8%) | .96 (-1.25,3.17), P=.40
ICU technology days mean(SD):4.6(12.2),5.1(13.9),4.5(11.4),4.1(11.3) |1.13(-.99,3.25),P=.30
ICU technology days median(IQR):0(0-5),0(0-4),0(0-4),0(0-4) | no comparison
PELOD ICU mean(SD):9.3(9.4),9.6(9),10.2(9.9),10(9.4) |-.12(-1.62,1.37),P=.87
PELOD 24h mean(SD):6.7(7.7),6.6(7.4),6.9(7.5),7(7.6) |-.29(-1.06,.49),P=.47
```

`S-D4-01` applies to every listed estimate/CI/P relation. Population is patient-level urgent ICU admission; 55 patients (3.2%) with admissions in both periods were removed. Binary percentages use admitted-patient denominators. Total and mean LOS account for multiple admissions; PIM-2 and PELOD use per-patient means across stays; ventilator-free days use first admission. All comparisons adjust for hospital-specific baseline and use GEE for hospital clustering. Continuous measures use linear-model mean differences and 95% CIs; binary measures use identity-link binomial risk differences and 95% CIs. PIM predicted counts are sum inverse-logits `1/(1+exp(-PIM))`, rounded to nearest integer. DNR-before-urgent-ICU deaths: 8, 4 per group. PIM/PELOD scales and bounds are as in N-D4-04.

Reproducible checks: shown percentages reconcile to displayed N and period denominators within rounding (e.g., 42/686=6.12%; 67/967=6.93%); all CIs contain their point estimates and have ordered endpoints; the sign/direction labels are compatible with signed adjusted differences, but the model-adjusted differences are not expected to equal raw difference-in-changes. The stated compatible models make the displayed two-sided P values directionally compatible with CIs crossing 0. No display-zero P value occurs.

## DOC-004 — eTable 5 sample assumptions/post-trial calculations (p. 14)

**N-D4-08.** Anticipated vs actual: hospitals `20, 21`; ward beds `2,397, 2,085`; patient discharges `99,389, 144,539`; patient-days `397,556, 559,443`; inter-cluster CV k `.15, .43`; between-cluster SD sigma-c `.00076, .00071`; mortality per 1,000 discharges `5.1,1.7`; deaths `507,244`; SCDE per 1,000 patient-days `2.0,.69`; SCDE events `795,386`. Post-hoc recalculated Bayesian k is `.43 (95% CI .17-.77)`.

Checks: actual discharges `50,173+94,366=144,539`; actual deaths `97+147=244`; actual patient-days `251,859+307,584=559,443`; actual SCDE `127+259=386` (all cross-reference eTables 2-3). Anticipated deaths `99,389*5.1/1,000=506.9`, rounds to 507; anticipated SCDE `397,556*2.0/1,000=795.112`, rounds to 795. Actual mortality `244/144,539*1,000=1.688`, prints 1.7; actual SCDE `386/559,443*1,000=.690`, prints .69. These reconcile at stated precision.

## Completion and no-candidate statement

All DOC-003 pp. 1-7 and DOC-004 pp. 1-14 result-relevant specifications, definitions, figures, tables, counts, denominators, percentages/rates, estimates, intervals, P values, scale/unit/time/population/contrast/reference information have been mapped. Matrix rows retain exact printed evidence, including zeros. No source-grounded inconsistency satisfying the candidate threshold was identified in this assigned support scope. L-D3-01 is retained solely as a lead for subsequent independent review.
