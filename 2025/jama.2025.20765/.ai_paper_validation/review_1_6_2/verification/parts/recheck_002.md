# Evidence recheck: C008, C009, C010, C011, C012, C013

Pending Human Adjudication. Runtime ID: 01a12c63-aaf3-7ea2-b202-3ccc33a45f88. Exact-source page images were visually read; normalized text only located the report-wide gender search. Twenty-three unique pages were inspected, below the 32-image bound. Current-run renders were produced directly from supplied PDFs with bundled pdf_tools.py/PyMuPDF 1.26.4 on CPU: cross_main_{3,4,5,8}.png; st1-main-006.png; cross_plan_{28,48,62,63,66,77,83,84,91,92,93}.png; numeric_support_plan_p64.png; cross_supp_{6,12}.png; numeric_support_p013.png. Three additional CPU renders at 160 dpi are preprocessing/recheck002_main_001.png, recheck002_plan_099.png, and recheck002_supp_015.png. Existing text/OCR was not final authority. No new OCR was required; the recorded GPU_USER_REQUESTED device authorization remains applicable to OCR.

## C008 — CO<6 rows in primary-outcome blocks

Pending Human Adjudication.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, S_C, S_W

**Compared document roles:** PLAN DOC-002 p.84 primary definition vs REPORT DOC-001 p.6 and DOC-003 p.13 primary blocks; REPORT DOC-001 p.3 sensitivity statement

**Evidence state:** reproduced_after_transcription_correction

**Inclusion audit:** PENDING_AUDIT

**Finding IDs:** F-ST1-008

**Location found; source and comparator matched:** All four cited locations were found. [DOC-002 p.84](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=84>), lines2654–2660, defines the primary endpoint as six-month continuous abstinence verified by CO<10 ppm. [DOC-001 p.3](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) explicitly identifies CO<6 ppm as a post hoc sensitivity of the primary outcome. [DOC-001 p.6](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>), Table2, places both CO<6 rows in the Primary outcome block: ITT 264/720 versus38/360, RR3.7 [2.4,5.8]; PP264/667 versus39/318, RR3.6 [2.14,6.87]. [DOC-003 p.13](<../../../../joi250093supp2_prod_1768590553.09463.pdf#page=13>), eTable9, is explicitly titled Post-hoc sensitivity analysis (intention to treat) after excluding deaths, but its Primary outcomes block also contains CO<6:264/695 versus38/333, crudeRR3.6 [2.4,5.4], adjustedRR3.8 [2.4,6.2]. Every affected CO<6 row at the cited displays was confirmed.

**Rule and logical comparison reproduced:** A planned primary threshold and an explicitly post hoc sensitivity threshold receive the same printed primary-block status in the two displays. No numeric rounding or half-unit comparison applies to this categorical status observation. This record confirms the printed grouping; it does not infer that investigators actually promoted the sensitivity to a prespecified primary endpoint.

**Necessary inputs available; missing definitions:** Threshold definitions, table titles, and block headings are available. The missing input is the intended status convention of the primary blocks: formal endpoint hierarchy versus grouping all analyses of the primary construct.

**Alternative interpretation; direct versus inferred:** The explicit post-hoc eTable9 title and main sensitivity sentence support grouping by primary construct. A changed outcome hierarchy is an inferred interpretation, not directly observed. The direct observation is the competing primary-block and sensitivity descriptions relevant to status extraction.

**Classification rationale:** PLAN and REPORT status descriptions give P_R; main narrative versus results supplement gives S_C; main narrative versus its own Table2 gives S_W. P_R takes precedence. The registration described main p.6 as a sensitivity-definition location; visual reading instead shows a primary block, so that location description is corrected and S_W added. Printed values themselves are unchanged. This transcription/context correction determines reproduced_after_transcription_correction.

**Classification ambiguity:** The primary-construct grouping convention may reconcile the hierarchy; no supplied statement defines that convention. This evidence fact remains distinct from inclusion adjudication.

**Exact remaining human question:** Do all three CO<6 rows retain post hoc sensitivity status despite placement in primary blocks, and what outcome-status metadata should accompany their estimates?

## C009 — Missing-outcome architecture

Pending Human Adjudication.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN DOC-002 protocol pp.28,66 vs PLAN DOC-002 SAP p.91 and REPORT DOC-001 pp.3,4

**Evidence state:** reproduced

**Inclusion audit:** PENDING_AUDIT

**Finding IDs:** F-XS-002, F-ST1-004

**Location found; source and comparator matched:** [DOC-002 p.28](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=28>), lines759–764, and [p.66](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=66>), lines2011–2016, separately headed Statistical analysis, both state that outcomes will primarily be analyzed in a missing-at-random architecture. Both follow economic complete-case/imputation paragraphs but say Outcomes without an economic restriction. [SAP p.91](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=91>), lines2890–2892, explicitly identifies primary ITT and regards dropout/incomplete data as continuing smokers. [DOC-001 p.3](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) treats missing primary outcomes as negative/not abstinent and separately discards missing outcomes for complete-case analysis. [DOC-001 p.4](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4>), Figure1, confirms missing53 and42, including deaths25 and27, and primary analysis totals720 and360.

**Rule and comparison reproduced:** Both protocol occurrences name MAR, whereas SAP/report explicitly assign all missing primary outcomes smoking status. The supplied passages do not map these to one combined primary analysis or restrict MAR to another outcome. Deterministic classification and MAR may coexist in different analyses, but that mapping is missing. Arithmetic53+42=95 and720+360=1080 reconciles; no count discrepancy is asserted. Half-unit/display precision does not apply to the missingness-architecture contrast.

**Necessary inputs available; missing definitions:** Printed handling statements and retained denominators are available; outcome-specific MAR applicability, the imputation model/variables, and an explicit replacement/amendment hierarchy are absent.

**Alternative interpretation; direct versus inferred:** Economic context could limit MAR to costs/QALYs, or SAP could replace the broader protocol. The separately headed Outcomes statement is directly observed; applicability to the reported primary ITT beyond its broad wording, and replacement chronology, are inferred possibilities. No bias or alternative efficacy estimate is inferred.

**Classification rationale:** All protocol/SAP passages are prospective PLAN; article methods/flow are REPORT. Protocol–report yields P_R; protocol–SAP yields P_P. Precedence/domain are confirmed without correction.

**Classification ambiguity:** Adjacent economic material is a material contextual alternative but does not expressly delimit the separately headed paragraph.

**Exact remaining human question:** Which outcomes/analyses use MAR, and how do those analyses relate to the smoking-status imputation for the primary ITT?

## C010 — Gender-specific primary analyses

Pending Human Adjudication.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 SAP pp.92,93,99 vs REPORT DOC-001 pp.3,5 and DOC-003 p.12

**Evidence state:** reproduced

**Inclusion audit:** PENDING_AUDIT

**Finding IDs:** F-XS-004, F-ST1-006

**Location found; source and comparator matched:** [SAP p.92](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=92>), lines2936–2939, specifies subgroup sensitivity analyses of primary treatment-effect stability. [p.93](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=93>), lines2940–2952, includes gender male/female, separate mixed-effects subgroup models, RR/95%CI, and disclosure of missing CIs. [p.99](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=99>) contains blank Gender Male/Female table-shell rows. [DOC-001 p.3](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) lists prespecified age, education, employment, and smoking-duration subgroups; [p.5](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5>) narrative adds reading SMS but reports no gender effect; its baseline table shows male698/720 and345/360, female22 and15. The complete [DOC-003 p.12](<../../../../joi250093supp2_prod_1768590553.09463.pdf#page=12>), eTable8, contains All, Age, Education, Occupation, Smoking Duration, Reading SMS, and no gender rows.

**Rule and comparison reproduced:** The prespecified primary-effect gender analysis has no result or missing-CI disclosure at its matched complete report displays. Source-text searches across main/report supplement locate gender only as baseline/context, not treatment-effect results. The blank shell is a prospective PLAN, not a report with absent cell values. Categorical planned-versus-reported analysis matching, Route A category5, applies; half-unit arithmetic does not address absent analyses.

**Necessary inputs available; missing definitions:** Plan models and complete reported subgroup categories are available. Male/female RR/CI outputs, sex-specific abstinence counts/model estimability, and a reason for omission/removal are absent.

**Alternative interpretation; direct versus inferred:** Sparse female enrollment is directly reported; inability to estimate gender-specific models, completed-but-omitted analysis, or an amendment are possible explanations, not observed facts. The SAP explicitly anticipates missing-CI disclosure.

**Classification rationale:** Prospective SAP versus report subgroup methods/results gives P_R/protocol_report. Main and supplement lists agree in lacking gender; they do not create S_C. No correction.

**Classification ambiguity:** Absence is bounded to the complete supplied report package, not proof that the analysis was never performed.

**Exact remaining human question:** Where are the planned male/female primary RR/CI results, or the disclosed explanation for nonestimation, omission, or removal?

## C011 — Ten versus twenty percent attrition inputs

Pending Human Adjudication.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN DOC-002 protocol pp.48,62 vs PLAN DOC-002 pp.63,64,83 and REPORT DOC-001 p.3; PLAN DOC-002 p.77 amendment context

**Evidence state:** reproduced

**Inclusion audit:** PENDING_AUDIT

**Finding IDs:** F-XS-010, F-ST1-010

**Location found; source and comparator matched:** [DOC-002 p.48](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=48>), lines1344–1347, combined study total2716 assumes10% do not provide primary data. [p.62](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=62>), lines1861–1863, repeats2716 and10%. [p.63](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=63>), lines1894–1898, Phase3 assumes20% and prints587+(587×0.2)=704. [p.64](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=64>), lines1936–1938, Phase4 likewise uses20%,864+(864×0.2)=1036. [SAP p.83](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=83>), lines2624–2638, combined overview and Phase3 both use20%; Phase3 proceeds to1080. [DOC-001 p.3](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) also says anticipated20% attrition in the1080-participant calculation. [DOC-002 p.77](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=77>), lines2416–2424, discloses sample-size revisions from888 to1080 for Phase3 and1480 to1620 for Phase4, without explicitly reconciling attrition percentages.

**Rule and calculation reproduced:** Same primary-data attrition input is10% in combined-plan overview/introduction and20% in both phase calculations, SAP overview, and report. Printed integer-percent intervals[9.5,10.5] and[19.5,20.5] have gap9 percentage points; relative discrepancy9/10=0.90>0.05. The registered additive inflation convention is stated and is not independently challenged.

**Necessary inputs available; missing definitions:** Percentages, phase labels, additive formula and amendment summary are available. A dated applicable-input hierarchy or explanation distinguishing combined-study missingness from phase-specific attrition is absent.

**Alternative interpretation; direct versus inferred:** Ten percent could be a retained overview input or a combined-study assumption different from phase attrition. Printed10/20 passages are direct observations; obsolescence or differing definitions are inferred explanations. Phase4 is context supporting the combined-study comparison, not a reported efficacy result.

**Classification rationale:** Conflicting protocol–SAP/detail assumptions give P_P;10% protocol versus20% report gives P_R, which takes precedence. All supplied specifications are PLAN by prospective content; article sample-size explanation is REPORT. No substantive classification correction.

**Classification ambiguity:** The10% wording covers the combined study, while the report concerns Phase3; both phase calculations and SAP combined overview use20%, so no supplied phase distinction expressly reconciles the input.

**Exact remaining human question:** Which attrition assumption governed Phase3, and does the combined-study10% statement denote a distinct definition or a superseded input?

## C012 — Cause attribution of the 4.8% mortality value

Pending Human Adjudication.

**Review domain:** report_internal_inconsistency

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Compared document roles:** REPORT DOC-001 p.8 discussion vs REPORT DOC-001 pp.1,4,5,6 and DOC-003 p.6

**Evidence state:** reproduced

**Inclusion audit:** PENDING_AUDIT

**Finding IDs:** F-NUM-001, F-XS-012

**Location found; source and comparator matched:** [DOC-001 p.8](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=8>) explicitly attributes4.8% within six months to deaths of TB. [p.5](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5>) specifies TB as61.5% [32/52] of deaths. [DOC-003 p.6](<../../../../joi250093supp2_prod_1768590553.09463.pdf#page=6>), eTable4, confirms52 total,25/27 by arm,32 TB deaths,16/16 by arm, and20 deaths across other causes. [DOC-001 p.1](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=1>) confirms1080 randomized; [p.4](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4>) Figure1 confirms720/360, deaths25/27; [p.6](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>) Table2 Death confirms25/720 and27/360. Every cited supporting location was visually matched.

**Rule and calculation reproduced:** TB-specific risk32/1080×100=2.962963%; all-cause52/1080×100=4.814815%. Applying the mandated half-unit intervals conservatively even to exact integer counts gives TB range100×[31.5/1080.5,32.5/1079.5]=[2.915317,3.010653]%. Printed4.8 gives[4.75,4.85]%; gap1.739347 and relative gap0.362364>0.05. All-cause range[4.766312,4.863363]% overlaps printed4.8. Thus the same printed percentage reconciles with total deaths but not the labeled cause-specific numerator.

**Necessary inputs available; missing definitions:** Counts, enrollment, time horizon and cause table are available. No alternate TB-attributable cause definition, denominator, or adjudication mapping yielding4.8% is supplied.

**Alternative interpretation; direct versus inferred:** The sentence may mean all-cause mortality among people with TB; that interpretation matches52/1080. The cause-specific words,32 TB deaths and52 total deaths are direct observations. Intended all-cause wording or an alternate cause population is inferred.

**Classification rationale:** Main discussion versus main cause result gives S_W; discussion versus supplementary cause table gives S_C. Both are REPORT by result content; S_C takes precedence. Domain reflects outcome attribution, rather than a separate count discrepancy. No correction.

**Classification ambiguity:** Generic denominator/death counts corroborate the arithmetic; no PLAN relationship is introduced.

**Exact remaining human question:** Is4.8% all-cause mortality among trial participants with TB or TB-attributed mortality, and which numerator/denominator defines the latter?

## C013 — Any-irritability and any-anxiety directions

Pending Human Adjudication.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-001 p.5 prevalence pairs vs same-paragraph direction; REPORT DOC-003 p.15 corroborates and supplies severity alternative

**Evidence state:** reproduced

**Inclusion audit:** PENDING_AUDIT

**Finding IDs:** F-NUM-002, F-XS-013

**Location found; source and comparator matched:** [DOC-001 p.5](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5>), Adverse Events, fixes mHealth/usual-care order, prints irritability40.5%/43.4% and anxiety33.3%/36.8%, then says dry mouth, irritability and anxiety were more common in mHealth. [DOC-003 p.15](<../../../../joi250093supp2_prod_1768590553.09463.pdf#page=15>), eTable10, confirms irritability None59.5%/56.6% and anxiety None66.7%/63.2%, whose complements match those any-symptom frequencies. Moderate/severe percentages are irritability11.2+4.3=15.5% versus7.2+1.2=8.4%; anxiety6.9+2.4=9.3% versus3.6+0.3=3.9%. Both repeated affected symptoms were confirmed.

**Rule and calculation reproduced:** Any-symptom mHealth-minus-control differences are−2.9 and−3.5 percentage points. Half-unit ranges are[−3.00,−2.80] and[−3.60,−3.40], strictly lower in mHealth; relative interval gaps2.80/43.4=0.064516 and3.40/36.8=0.092391 both exceed0.05. Printed direction reverses the matched any-symptom reading, Route A category2. Dry mouth62.7%/55.7% agrees and is contextual, not an additional occurrence.

**Necessary inputs available; missing definitions:** Arm order, any-symptom percentages, and severity rows are available. The missing definition is whether more common switches from any symptom to moderate/severe burden.

**Alternative interpretation; direct versus inferred:** Moderate/severe frequencies are directly higher in mHealth in eTable10 and provide a source-grounded alternative. A switch to that severity quantity in the main sentence is inferred because it is not stated.

**Classification rationale:** The conflicting values/direction occur inside one REPORT paragraph, yielding S_W/statistical_results. Supplementary rows corroborate the prevalence and support the severity alternative; they do not conflict with main prevalences and therefore add no S_C. No correction.

**Classification ambiguity:** Prevalence and severity are separate quantities; their intended linkage is not specified.

**Exact remaining human question:** Does more common mean any irritability/anxiety or moderate/severe symptoms, and which quantity and direction should be extracted?
