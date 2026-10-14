# Statistical consistency review — pass 1

Runtime ID: 01a12c43-fb96-7943-933b-ea7e7d98f89b; fresh gpt-6.1-sol/high. Scope: every inferential relationship in REPORT DOC-001 pp.1–9, REPORT DOC-003 pp.1–16, and PLAN DOC-002 pp.1–109. Complete new maps were read and supplied source-linked page images confirmed the observations below. Fresh source render st1-main-006.png uses bundled pdf_tools.py, PyMuPDF1.26.4,200dpi,CPU; no OCR or web used. Sources and legacy artifacts preserved.

All114 relationships received PASS_1_COMPLETE. S IDs: S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, S113, S114.

The complete relationship inventory records point estimates, every interval, counts, populations, contrasts, model labels, direction and limitations. All printed point estimates are within ordered intervals. Main superiority and death directions agree with null exclusion; TB success/default/failure intervals include their nulls. No printed standard error occurs. No displayed CI-versus-P significance conflict was found. Table2/eTables7–9 have no P values. eTable3 z/P pairs are compatible with two-sided normal diagnostics; test names, tie handling and analysis denominators are not inferred. Unmarked eTable10 rows reproduce Pearson statistics to display precision and align with their P values; marked exact rows retain their explicit alternative analysis, with exact-test variant unspecified. Figure2 all27 posterior and observed markers lie within their own graphical whiskers; numerical graph readings are approximate, and no Bayesian significance threshold is invented. Kaplan-Meier direction agrees with HR<1. Noninferiority/equivalence outcomes belong to a separate unreported Phase4; the stated8-point margin/effect-preservation arithmetic reconciles. No alpha-spending, model covariance, degrees of freedom, sidedness or missing estimand mapping is supplied from convention.

11 findings are emitted after self-screening, with14 excluded apparent observations. These are checker findings pending an independent inclusion screen; no candidate IDs or adjudications are assigned.

## Findings

### F-ST1-001 — Interval rows do not follow a reconstruction that fits other rows of their displays

**Exact locations and document roles:** REPORT [DOC-001 PDF p.6](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6), Table2, adjusted CO<10 complete-case/PP row; crude and adjusted CO<6 complete-case/PP row; adjusted continuous self-report row. REPORT [DOC-003 PDF p.12](../../../joi250093supp2_prod_1768590553.09463.pdf#page=12), eTable8, All; age≥40; primary education; secondary or above; active employment; dependent/retired; smoking duration<24; reading SMS No. REPORT [DOC-003 PDF p.13](../../../joi250093supp2_prod_1768590553.09463.pdf#page=13), eTable9, CO<10 crude and adjusted columns; population/adjustment definitions REPORT [DOC-003 PDF p.14](../../../joi250093supp2_prod_1768590553.09463.pdf#page=14).

**Printed values:** All affected point/lower/upper triples are recorded in the calculation table below. Each is labeled RR and95%CI. Table2 prints adjusted self-report upper limit42, which was independently confirmed in the exact PDF render; it is preserved literally.

**Rule and calculation:** Test the same log-symmetric interval reconstruction on each display: U*=E²/L, equivalent to a point at the geometric midpoint of the limits. This is a reproducing-method check, not a claim that the authors necessarily used a Wald interval. For displayed half-units hE,hL,hU, reconstructed U* range=[(E−hE)²/(L+hL),(E+hE)²/(L−hL)], printed U range=[U−hU,U+hU]; discrepancy is their nonnegative separation, divided by|U|. Allowing exactly the displayed precisions, the following rows exceed.05. Counts/populations are not substituted for modeled estimates.

| Display/row/column | Printed E;L;U | Reconstructed U* rounding range | Interval gap | Relative discrepancy |
|---|---|---|---:|---:|
| Table2 CO10 PP adjusted | 3.1;2.1;5.2 | [4.326744,4.840244] | 0.309756 | 0.059568 |
| Table2 CO6 PP crude | 3.6;2.14;6.87 | [5.875291,6.240047] | 0.624953 | 0.090968 |
| Table2 CO6 PP adjusted | 3.8;2.3;7.7 | [5.984043,6.587778] | 1.062222 | 0.137951 |
| Table2 self-report adjusted | 2.8;1.9;42 | [3.878205,4.390541] | 37.109459 | 0.883559 |
| eTable8 All | 2.890;1.983;4.709 | [4.209332,4.214371] | 0.494129 | 0.104933 |
| eTable8 Age≥40 | 2.953;2.048;5.092 | [4.255434,4.260397] | 0.831103 | 0.163217 |
| eTable8 Primary | 2.638;1.849;4.07 | [3.761236,3.766125] | 0.298875 | 0.073434 |
| eTable8 Secondary | 2.719;1.348;4.83 | [5.480343,5.488445] | 0.645343 | 0.133611 |
| eTable8 Active | 2.989;1.933;4.885 | [4.619153,4.624637] | 0.259863 | 0.053196 |
| eTable8 Dependent | 2.587;1.329;3.986 | [5.031954,5.039636] | 1.045454 | 0.262281 |
| eTable8 Smoke<24 | 3.511;1.884;7.127 | [6.539459,6.546659] | 0.579841 | 0.081358 |
| eTable8 Reading SMS No | 2.198;1.288;3.299 | [3.747774,3.754099] | 0.448274 | 0.135882 |
| eTable9 CO<10 crude | 2.9;1.8;6.4 | [4.390541,4.972857] | 1.377143 | 0.215179 |
| eTable9 CO<10 adjusted | 3.1;1.9;6.5 | [4.770513,5.363514] | 1.086486 | 0.167152 |

Reproducing rows in Table2 include continuous-self-report crude2.7[1.8,4.1], point-week9 crude2.6[1.8,3.9], adjusted2.7[1.8,4.3], point-month6 crude2.7[2.0,3.8],adjusted2.7[1.9,4.0], and TB-success crude1.2[.9,1.6],adjusted1.2[.9,1.5]; their reconstructed/printed rounding ranges overlap. Other Table2 rows screened by the.05 rule are separately recorded once below. In eTable8, age<40 has reconstruction[4.846799,4.853725], printedU[4.8565,4.8575], relative gap.000571; smoking≥24 has[3.857124,3.862770], printedU[3.9105,3.9115], relative gap.012204; no formal education and reading Yes also pass the display rule. In eTable9, CO<6 crude3.6[2.4,5.4] and adjusted3.8[2.4,6.2], point-week9 crude2.5[1.7,3.6] and adjusted2.6[1.7,3.8], point-month6 crude2.58[1.8,3.6] and adjusted2.7[1.8,4.0], and success1.1[.7,1.6]/1.1[.7,1.5] all have overlapping ranges. This establishes within-display reproduction without presuming a universal interval procedure.

**Focus area:** B,C.
**Proposed review domain:** statistical_results.
**Proposed relationships:** S_W; separate occurrences within each REPORT document, with one consolidated interval-construction pattern. No matching result is asserted to conflict across documents.
**Qualifying route:** Route A, category 4.
**Affected result or extracted value:** The14 listed95%CI upper endpoints, including42, and the corresponding primary/sensitivity/subgroup uncertainty.
**Why context does not resolve it:** RouteA category 4 requires registration when a method reproduces other display rows yet does not reproduce these printed rows beyond precision; an unstated construction does not remove the observation.
**Alternatives and missing definition:** Profile likelihood, bootstrap, transformed marginal-risk or other nonsymmetric CIs may explain some or all rows. Different procedures by row are possible. The source does not give row-specific interval construction or covariance/SE. This calculation is a diagnostic reconstruction, not proof of a misplaced decimal or a prescribed correction.
**Exact human question:** Which estimate/interval construction produced each listed row, and are all listed printed limits, including42, the intended values for that construction?
**Relationships:** S002,S004,S005,S054,S056,S058,S059,S060,S061,S062,S065,S066.

### F-ST1-002 — Reported relative risks lack a derivation from the stated logistic model

**Exact locations and document roles:** REPORT [DOC-001 PDF p.3](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3), Statistical Analysis; REPORT [DOC-001 PDF p.6](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6), Table2 RR headers and notea; corresponding REPORT [DOC-003 PDF p.11](../../../joi250093supp2_prod_1768590553.09463.pdf#page=11) eTable7 and [DOC-003 PDF p.13](../../../joi250093supp2_prod_1768590553.09463.pdf#page=13)–[DOC-003 PDF p.14](../../../joi250093supp2_prod_1768590553.09463.pdf#page=14) eTable9 useRR labels.
**Printed values:** Mixed-effects logistic regression for categorical outcomes, intervention fixed effect/cluster random effect; primary crudeRR3.0[2.0,4.9],adjustedRR3.2[2.2,5.2]; other abstinence RRs and covariateRRs as mapped.
**Rule and calculation:** A logistic model specifies logit(p)=η; exponentiating a treatment coefficient gives an odds ratio. A risk ratio requires an additional defined prediction/conversion step or a different link. The report calls these results RR without stating that step. No comparison with a crude count ratio is used, and no claim that an OR was actually reported is made. Display precision is not applicable to the logical missing step.
**Focus area:** C.
**Proposed review domain:** statistical_results.
**Proposed relationships:** S_W. The main report's method and its Table2 measure are the conflicting pair; supplemental RR displays extend the affected-results scope without adding a separate cross-document conflict.
**Qualifying route:** Route B.
**Affected result or extracted value:** PrimaryRR3.0/3.2 and95%CIs, and other displayed RRs used in extraction.
**Why context does not resolve it:** Logistic regression can yield multiple risk-based quantities through additional operations; neither the main method nor table notes identify the operation, marginal/conditional estimand, or reference-risk mapping that produced these printed RRs.
**Alternatives and missing definition:** Predictions standardized over patients/sites could produceRRs; a fitted log-link model could have been used; the logistic sentence could apply to a distinct analysis. The derivation, averaging distribution and actual model linked to each RR are missing. No preferred method is proposed.
**Exact human question:** What transformation, prediction/standardization rule or fitted link produced the printed RRs and their95%CIs from the stated mixed-effects logistic analysis?
**Relationships:** S087,S001–S008,S046–S072.

### F-ST1-003 — Primary model differs between protocol, SAP and report

**Exact locations and document roles:** PLAN [DOC-002 PDF p.66](../../../joi250093supp1_prod_1768590553.08963.pdf#page=66), lines2011–2016, section28.2.2; corroborating earlier PLAN [DOC-002 PDF p.28](../../../joi250093supp1_prod_1768590553.08963.pdf#page=28), lines759–764. PLAN [DOC-002 PDF p.91](../../../joi250093supp1_prod_1768590553.08963.pdf#page=91), lines2886–2889. REPORT [DOC-001 PDF p.3](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3), Statistical Analysis.
**Printed statements:** Latest protocol specifies generalized linear mixed model with log link and Poisson distribution, cluster random intercept and crude/adjustedRRs; SAP specifies mixed-effects logistic regression with site random effect andRR; report states mixed-effects logistic regression for categorical outcomes.
**Rule and calculation:** Log(P)=η and logit(P)=η are distinct primary model specifications. Protocol and SAP explicitly name different model families/links for the primary categorical outcome. Report matches the logistic side. Display precision is not applicable.
**Focus area:** D,C.
**Proposed review domain:** protocol_report.
**Proposed relationships:** P_R,P_P; primaryP_R. The protocol conflicts with the reported primary model and with the SAP; SAP corroborates the reported family.
**Qualifying route:** Route B.
**Affected result or extracted value:** Primary adjusted/crudeRRs and their interpretation as planned versus reported estimates.
**Why context does not resolve it:** The supplied change statement [DOC-002 PDF p.77](../../../joi250093supp1_prod_1768590553.08963.pdf#page=77) documents outcome/sample-size/intervention changes but does not map this primary-model replacement or give a protocol/SAP hierarchy.
**Alternatives and missing definition:** A disclosed amendment not in the bundle or SAP supersession may explain the family change; a separate Poisson analysis may exist. No such mapping is supplied.
**Exact human question:** Which primary model specification governed the reported analysis, and where is the Poisson-to-logistic change or the distinct-analysis mapping documented?
**Relationship:** S088.

### F-ST1-004 — Primary missing-outcome handling differs across protocol and SAP/report

**Exact locations and document roles:** PLAN [DOC-002 PDF p.66](../../../joi250093supp1_prod_1768590553.08963.pdf#page=66), lines2012–2016 and earlier PLAN [DOC-002 PDF p.28](../../../joi250093supp1_prod_1768590553.08963.pdf#page=28), lines759–764; PLAN [DOC-002 PDF p.91](../../../joi250093supp1_prod_1768590553.08963.pdf#page=91), lines2890–2892; REPORT [DOC-001 PDF p.3](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3), missing-primary paragraph; REPORT [DOC-001 PDF p.4](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4), Figure1 attrition.
**Printed statements/values:** Protocol primary missing-at-random architecture; SAP dropout/incomplete data treated as continuing smokers; report missing primary outcomes treated negative/not abstinent. Missing primary outcomes53/720 and42/360, total95.
**Rule and calculation:** Treating all95 missing primary results as nonabstinent defines an observed composite classification; an outcome model under missing-at-random is a distinct stated primary missing-data architecture. Neither source specifies how both are combined in the same primary analysis. This is a logical specification comparison, not a numerical estimate of bias; display precision not applicable.
**Focus area:** D,C.
**Proposed review domain:** protocol_report.
**Proposed relationships:** P_R,P_P; primaryP_R.
**Qualifying route:** Route B.
**Affected result or extracted value:** PrimaryITT300/720 versus55/360 and the corresponding RR/CI.
**Why context does not resolve it:** The SAP/report give a definite negative classification, while the protocol explicitly namesMAR for the primary analysis. Complete-case sensitivity is separately stated and does not identify a primaryMAR analysis or its replacement.
**Alternatives and missing definition:** MAR may refer to a distinct missing covariate/economic model, or a later analysis amendment may supersede it. The protocol paragraph does not make that restriction, and the change statement supplies no mapping.
**Exact human question:** Did the primary analysis use the plannedMAR architecture, negative classification of missing abstinence outcomes, or both in separately identified analyses, and what amendment or mapping explains the difference?
**Relationship:** S089.

### F-ST1-005 — Planned tobacco-form adjustment is absent from the reported adjusted analysis

**Exact locations and document roles:** PLAN [DOC-002 PDF p.92](../../../joi250093supp1_prod_1768590553.08963.pdf#page=92), lines2919–2926, fully adjusted sensitivity; REPORT [DOC-001 PDF p.3](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3), fixed-effects and post-hoc covariate statements; REPORT [DOC-001 PDF p.6](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6), Table2 notea; REPORT [DOC-003 PDF p.14](../../../joi250093supp2_prod_1768590553.09463.pdf#page=14), eTable9 notee.
**Printed statements/values:** SAP fully adjusted models include sociodemographic variables alongside tobacco-use form and other baseline characteristics. Report/table notes list age,sex,education,occupation,smoking duration, selected post hoc; primary adjustedRR3.2[2.2,5.2]. Tobacco-use form does not appear in that finite list.
**Rule and calculation:** Compare the explicitly planned adjustment element against the finite reported adjustment list. The tobacco-form-adjusted primary sensitivity analysis specified inSAP is absent; this is an analysis specification comparison, not a preferred covariate recommendation. Display precision not applicable.
**Focus area:** D.
**Proposed review domain:** protocol_report.
**Proposed relationships:** P_R.
**Qualifying route:** Route A, category 5.
**Affected result or extracted value:** Primary adjustedRR3.2[2.2,5.2] and excluding-deaths adjustedRR3.1[1.9,6.5].
**Why context does not resolve it:** RouteA category 5 covers a planned primary analysis not reported; post-hoc selection does not itself identify the planned fully adjusted model or its replacement.
**Alternatives and missing definition:** The planned model may have been attempted with a dropped variable or reported elsewhere; tobacco-form levels may have been collapsed. No reason or mapping is supplied.
**Exact human question:** Was the prespecified tobacco-form-adjusted primary sensitivity model fitted, and where are its results or the documented change to the reported covariate list?
**Relationship:** S090.

### F-ST1-006 — Prespecified gender subgroup analysis of the primary outcome is not reported

**Exact locations and document roles:** PLAN [DOC-002 PDF p.93](../../../joi250093supp1_prod_1768590553.08963.pdf#page=93), lines2940–2952, especially2942, and PLAN [DOC-002 PDF p.99](../../../joi250093supp1_prod_1768590553.08963.pdf#page=99) subgroup template; REPORT [DOC-001 PDF p.3](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3), prespecified subgroup list; REPORT [DOC-003 PDF p.12](../../../joi250093supp2_prod_1768590553.09463.pdf#page=12), complete eTable8.
**Printed statements/values:** SAP primary sensitivity subgroups include gender male/female, each with a mixed-effects model, RR and95%CI, and disclosure of missingCIs. Report list/eTable8 contain age,education,occupation,smoking duration and readingSMS, without gender rows. Main baseline includes698/720 and345/360 males.
**Rule and calculation:** Exhaustively match every planned primary subgroup to the complete report displays. Gender has no matched primary result or stated nonestimability. Display precision not applicable.
**Focus area:** D.
**Proposed review domain:** protocol_report.
**Proposed relationships:** P_R.
**Qualifying route:** Route A, category 5.
**Affected result or extracted value:** Planned sex-specific primaryRRs/CIs and the reported claim of subgroup consistency.
**Why context does not resolve it:** RouteA category 5 covers an omitted planned primary analysis. Small female numbers could explain nonestimation, but theSAP explicitly anticipates disclosure of missingCIs; the report supplies neither estimate nor such disclosure.
**Alternatives and missing definition:** Estimation may have been infeasible or a later amendment may have removed the subgroup. Those explanations are not stated.
**Exact human question:** Where are the prespecified male/female primary-outcome subgroup results, or the disclosed reason that these estimates/CIs could not be produced or were removed?
**Relationship:** S097.

### F-ST1-007 — Randomization description omits a planned minimization factor

**Exact locations and document roles:** PLAN [DOC-002 PDF p.51](../../../joi250093supp1_prod_1768590553.08963.pdf#page=51), lines1445–1453, and earlier PLAN [DOC-002 PDF p.13](../../../joi250093supp1_prod_1768590553.08963.pdf#page=13), lines304–312; REPORT [DOC-001 PDF p.2](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=2), Procedures.
**Printed statements:** PLAN allocation uses minimization to balance average number ofTB patients seen per month and country. REPORT allocation is country-stratified computer-generated lists for27 clinics in2:1 ratio; the clinic-volume minimization factor is not identified.
**Rule and calculation:** Compare the explicitly planned statistical allocation rule with the reported allocation description for the same Phase3 population. Country matching explains one factor but does not identify the second. Display precision not applicable.
**Focus area:** D.
**Proposed review domain:** protocol_report.
**Proposed relationships:** P_R.
**Qualifying route:** Route B.
**Affected result or extracted value:** Statistical design underlying the primary randomized comparison and its27-clinic population.
**Why context does not resolve it:** Country stratification and minimization including clinic volume can coexist, but the reader cannot tell whether the planned volume rule was used, removed or encompassed in an unstated implementation.
**Alternatives and missing definition:** A shortened description may omit an implemented minimization procedure. The source does not say the factor was abandoned; that is not inferred.
**Exact human question:** Was clinic monthlyTB volume used in the planned minimization procedure, and how does that procedure map to the reported country-stratified randomization?
**Relationship:** S085.

### F-ST1-008 — CO<6 sensitivity is labeled as a primary outcome in a results display

**Exact locations and document roles:** REPORT [DOC-003 PDF p.13](../../../joi250093supp2_prod_1768590553.09463.pdf#page=13), eTable9 Primary outcomes block, CO<6 row; REPORT [DOC-001 PDF p.3](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3), primary definition and posthoc sensitivity; REPORT [DOC-001 PDF p.6](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6), primary/sensitivity rows; PLAN [DOC-002 PDF p.84](../../../joi250093supp1_prod_1768590553.08963.pdf#page=84), lines2653–2669.
**Printed statements/values:** PLAN primary verificationCO<10ppm. Main report callsCO<6ppm a posthoc sensitivity. eTable9 placesCO<6 beneath Primary outcomes, with264/695 versus38/333,RR3.6[2.4,5.4],adjusted3.8[2.4,6.2].
**Rule and calculation:** Compare explicit outcome status for the sameCO<6 analysis. A posthoc threshold sensitivity is printed as a primary outcome in this display; precision not applicable to status.
**Focus area:** D,B.
**Proposed review domain:** protocol_report.
**Proposed relationships:** P_R,S_C; primaryP_R because the report's primary label differs from the plan-defined primary threshold.
**Qualifying route:** Route A, category 5.
**Affected result or extracted value:** Status and extraction ofCO<6RR3.6/3.8 as primary rather than sensitivity.
**Why context does not resolve it:** RouteA category 5 always registers changes in planned outcome status; the same appendix title's posthoc label is an alternative interpretation, not a removal of the printed primary block.
**Alternatives and missing definition:** Primary outcomes may mean a block of analyses of the primary abstinence construct including sensitivity thresholds. The source does not explicitly distinguish that display convention from endpoint status.
**Exact human question:** Does theCO<6 row retain posthoc sensitivity status, and what outcome status should accompany its estimates in extraction from the Primary outcomes block?
**Relationship:** S113.

### F-ST1-009 — Latest protocol retains different Phase3 cluster allocations in its power specifications

**Exact locations and document roles:** PLAN [DOC-002 PDF p.48](../../../joi250093supp1_prod_1768590553.08963.pdf#page=48), lines1347–1350; PLAN [DOC-002 PDF p.63](../../../joi250093supp1_prod_1768590553.08963.pdf#page=63), lines1886–1907; PLAN [DOC-002 PDF p.65](../../../joi250093supp1_prod_1768590553.08963.pdf#page=65), lines1958–1961; amendment context PLAN [DOC-002 PDF p.77](../../../joi250093supp1_prod_1768590553.08963.pdf#page=77). REPORT enrollment [DOC-001 PDF p.4](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4) corroborates27clinics,18/9 but is not a conflicting comparator.
**Printed values:** Latest overview/detailed Phase3A18/C9,total27,90%power at5%,probabilities18%/8%. Later same latest protocol text statesA16/C8,total24 with same power/level/probabilities.
**Rule and calculation:** Matching Phase3 specification within the same latest protocol yields18 versus16 interventionclusters and27 versus24 total. Half-unit ranges[17.5,18.5] versus[15.5,16.5] have gap1,relative1/16=.0625; totalranges[26.5,27.5] versus[23.5,24.5] gap2,relative2/24=.083333. Control9 versus8 alone touches after half-unit rounding and is not the reproducing basis.
**Focus area:** D,C.
**Proposed review domain:** plan_material.
**Proposed relationships:** P_P.
**Qualifying route:** Route B.
**Affected result or extracted value:** Planned Phase3 population/cluster allocation and power underlying the1080-participant reported trial.
**Why context does not resolve it:** The change note confirms24→27 but the latest text retains both without marking one obsolete; this is a statistical power/allocation input rather than a peripheral site-count copy.
**Alternatives and missing definition:** The16/8paragraph may be unrevised earlier-version text; that production explanation is not a replacement for a source statement identifying which power calculation applies.
**Exact human question:** Which Phase3 cluster allocation and corresponding power calculation governs the latest protocol, and should the16/8 specification be read as historical?
**Relationship:** S103.

### F-ST1-010 — Latest protocol uses both10% and20% primary-outcome attrition assumptions

**Exact locations and document roles:** PLAN [DOC-002 PDF p.48](../../../joi250093supp1_prod_1768590553.08963.pdf#page=48), lines1344–1346; PLAN [DOC-002 PDF p.62](../../../joi250093supp1_prod_1768590553.08963.pdf#page=62), lines1860–1864; PLAN [DOC-002 PDF p.63](../../../joi250093supp1_prod_1768590553.08963.pdf#page=63), lines1894–1898; PLAN [DOC-002 PDF p.83](../../../joi250093supp1_prod_1768590553.08963.pdf#page=83), lines2624–2638; REPORT [DOC-001 PDF p.3](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3)20% corroborates detailed calculation only.
**Printed values:** Latest overview/statistics introduction assumes10% withoutprimary outcome. Latest detailed Phase3 calculation andSAP use20%,587+(587×.2)=704,then1080; report says anticipated20%.
**Rule and calculation:** These are assumptions for the same latest planned primary-outcome sample. Printedpercentage rounding ranges[9.5,10.5] and[19.5,20.5] have gap9percentagepoints; relative9/10=.9>.05. The observation is not about replacing the expressly given additive-inflation formula.
**Focus area:** D,C.
**Proposed review domain:** plan_material.
**Proposed relationships:** P_P.
**Qualifying route:** Route B.
**Affected result or extracted value:** Phase3 sample-size and power assumptions supporting1080participants.
**Why context does not resolve it:** Same latest plan material prints both assumptions; no separate cause/type of missingness is given to map10% and20% to different calculations.
**Alternatives and missing definition:** The introduction may retain an earlier allowance; the detailed calculation may supersede it, but no explicit reconciliation appears.
**Exact human question:** Which primary-outcome attrition assumption governs the latest Phase3 calculation, and how do its10% and20% statements relate?
**Relationship:** S104.

### F-ST1-011 — Latest protocol and SAP retain different treatment-failure windows

**Exact locations and document roles:** PLAN [DOC-002 PDF p.47](../../../joi250093supp1_prod_1768590553.08963.pdf#page=47), lines1319–1320; PLAN [DOC-002 PDF p.77](../../../joi250093supp1_prod_1768590553.08963.pdf#page=77)explicit5→6change; PLAN [DOC-002 PDF p.85](../../../joi250093supp1_prod_1768590553.08963.pdf#page=85), lines2685–2686. REPORT [DOC-001 PDF p.6](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6)failure counts are the affected result, not a statement of a conflicting threshold.
**Printed statements/values:** Latest protocol initially smear-positive and remains smear-positive atmonth6or later. Change note explicitly replacesmonth5withmonth6. SAP retainsmonth5or later. Reportfailure1/720versus2/360.
**Rule and calculation:** Month5 andmonth6 imply different eligibility windows for classifying failure; half-unit monthranges[4.5,5.5] and[5.5,6.5] touch, but the relevant comparison is the exact named endpoint time window, not a rounded measurement. No numerical failure-count difference is inferred.
**Focus area:** D.
**Proposed review domain:** plan_material.
**Proposed relationships:** P_P.
**Qualifying route:** Route B.
**Affected result or extracted value:** Definition attached to failure1/720 and2/360,and the cure/completed/failure classification used forTB outcomes.
**Why context does not resolve it:** The explicit amendment identifies a change, while theSAP keeps the earlier definition; no statement says which definition produced the reported failure counts. This is a changed outcome definition, not merely a pointer.
**Alternatives and missing definition:** SAP may retain the earlier threshold despite the protocol amendment, or programme-register classifications may follow one definition; no mapping is supplied.
**Exact human question:** Were the reported treatment-failure counts classified usingmonth5or later ormonth6or later, and how does theSAP definition map to the explicit protocol amendment?
**Relationship:** S109.

## Excluded observations

Only apparent issues not emitted are listed. Relationships that reconcile without an apparent issue are recorded in the inventory, not counted here. Every row has exactly one reason code.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 p6 Table2; DOC-003 pp11–14 eTables7–9 | Model-based RRs differ from count-based risk ratios. Mixed-effects/adjusted estimates are not crude participant-level ratios even when a column saysCrude; no source states the displayed modelRR equals the simple ratio. | MODEL_VERSUS_CRUDE |
| PLAN DOC-002 pp63–64; REPORT DOC-001 p3 | Initial n587 and n864 do not equal one normal-approximation calculation from displayed power/rates. The precise initial sample-size test, continuity adjustment/equation and software are not supplied; diagnostic≈540/969 is not a reproducing source method and does not establish a contradiction. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002 pp63–64 attrition calculations | Additive20% allowance versus dividing by.8 would produce≈734 rather than704 and1080 rather than1036. Even the point-level gap relative to704/1036 isabout4.2–4.3%; allowing input/output half-units makes the relative discrepancy no larger. The explicit additive rule itself reproduces. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN DOC-002 pp63–64,83; REPORT DOC-001 p3 | 704×1.50=1056 versus≈1080;1036×1.56=1616.16 versus1620;1.50versus1.56 Phase4DE. For704±.5 and1.50±.005 product[1051.7325,1060.2725],printed1080±.5 gap19.2275/1080=.0178; Phase4gap<.003; DEgap(.050)/1.50=.0333. Rounded cluster capacities and display rule screen the apparent arithmetic differences. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p6 Table2 and DOC-003 p12 eTable8 | Other log-symmetric reconstruction departures do not cross.05: Table2 primaryITT crude.01622,adjusted.04562;CO10PPcrude.03983;CO6ITTadjusted.03053. eTable8 age<40 .000571,no formal .043561,smoking≥24 .012204,readingYes .017970. These are excluded once; rows above.05 are all retained inF-ST1-001. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 pp6,8 | Narrative observedICC.19 versus primaryITTtable.18. Printed ranges[.185,.195] and[.175,.185] touch,gap0;complete-caseICC.19 also supplies context. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 pp3,6 | PP label versus complete-case description. The methods define omission of missingprimary outcomes and Table2 denominators667/318 exactly implement it; terminology does not obscure which numbers apply. | TERMINOLOGY_OR_WORDING |
| REPORT DOC-001 p5;DOC-003 p11 eTable7 | Narrative says shorter smoking duration and higher education modified theprimary outcome, whereas table supplies prognostic covariateRRs rather than interactions. Immediate outcome-predictor context allows the wording, and no specific interaction statistic is claimed. | TERMINOLOGY_OR_WORDING |
| REPORT DOC-001 pp3,7 Figure2 | Bayesian prior,MCMC and exact numerical CrI endpoints are not supplied. No printed probability/statement conflicts with a stated prior or method; graphical values remain approximate. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002 pp85–86,91–92,97;allREPORT results | Additional planned non-key secondary EQ5D,clinicalTB score,sputum conversion,relapse,MPSS/SUTS and anyAE/SAE analyses are not displayed. These are not designatedkey secondary or primaryanalyses and no status-changing replacement is stated; omission alone is peripheral under the tiered scope. The planned genderprimary subgroup is separately emitted. | PERIPHERAL_COMPARISON |
| PLAN DOC-002 pp64–65,83 | Phase4 cluster allocations18/18 versus20/20 concern the separately unreported noninferiority phase; no reportedPhase3 decision or population depends on those counts. Phase3allocation discrepancy is separately emitted. | PERIPHERAL_COMPARISON |
| REPORT DOC-003 pp15–16 eTable10 | Pearson diagnostics give drymouth31.842versus31.2;headache2.787versus2.7;insomnia6.991versus6.9. Even treating integer counts as exact,printedhalf-units yield maximum relativegaps.01898,.01386,.00590,all≤.05. Exact-marked rows retain their distinct test and are not judged by an assumeddf. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN DOC-002 p84;REPORT DOC-001 p3 | Planned urine-striplevel<3 versus report negativecassette naming does not supply a numerical contradictory threshold or observedclassification. Missing assaymapping alone is not a result conflict. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002 pp8,47,84;REPORT DOC-001 p3 | CO<10 verification andCO>10 supersession sentences leave an unstated operational sentence for exact10. No observedexact10 result or claimed classification conflicts; the<10 endpoint itself is definite. | CONDITIONAL_OR_UNREPORTED |

## Limitations and durable handoff

All114 S relationships were completed; zero assigned scientific relationships or source units were omitted. Full mapping is provided by the canonicalmain/support evidence maps. NativePLANtext is garbled, so readable source-linked rendered pages and fresh direct rendering where needed supplied text; no source-derived finding is based solely on an OCR discrepancy. Exact graph endpoint numbers, rawdata, participant death times, model covariance/standard errors and row-specific CI constructions are absent from the supplied package. These limits do not suppress reproduced RouteA4 rows. Findings use no external literature, diagnostic approximations are explicitly labeled, and no preferred analysis or correction is proposed.

Artifacts: statistics/relationship_inventory.md;checkers/statistical_pass_1.md;preprocessing/st1-main-006.png. Runtime/model/effort supplied to coordinator; the later statistical pass must use a different fresh runtimeID.

