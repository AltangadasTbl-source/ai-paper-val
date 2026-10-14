# Statistical pass 1

Runtime canonical ID: /root/statistics_1. Model gpt-6.1-sol; reasoning effort high; FRESH_SPAWN. Scope: all 107 inferential/statistical-design relationships S001–S107 across all 194 supplied PDF pages in six sources. Every relationship has PASS_1_COMPLETE in [inventory](../statistics/relationship_inventory.md). Complete QUALITY_CONTROL_SCOPE.md and review_contract.md were read. Current-run maps and source-linked evidence were used; legacy scientific conclusions and the web were not used. This checker assigns no candidate IDs or adjudications. Eight independently self-screened findings follow, with 15 excluded apparent observations. Findings need a fresh independent inclusion screen.

Source verification: main source-derived p1–7 native text and exact p6 render; SAP p4/7/8/9 source-linked images; active protocol PDF105/106/127–130 text; results supplement p4–6 fresh native extraction and source-linked p5/6/18 images. Exact source links below use physical PDF pages. Direct native text was produced with `.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py text joi250087supp3_prod_1766516490.97011.pdf --first 4 --last 6 .ai_paper_validation/review_1_6_2/preprocessing/statistics_1/supp3-p4-6-native.txt`; engine PyMuPDF1.26.4. No new rendering/OCR was required by this agent; source/reused artifacts preserved. Calculations use R4.5.2 diagnostics; code/results are recorded in the inventory and calculation record. No P/CI compatibility conclusion assumes an unstated sidedness/model/covariance.

### F-ST1-001 — Primary model adjustment factors are described differently

- **Relationships:** S065, S068, S069.
- **Exact locations and roles:** REPORT [main p2, Randomization](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=2); REPORT [main p3, Statistical Analysis](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=3); REPORT [main p6, Table2 footnote c](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=6). PLAN [SAP p6, Analysis](../../../joi250087supp2_prod_1766516490.96511.pdf#page=6) corroborates the table's etiology specification.
- **Printed statements/values:** Randomization minimization factors are primary shock etiology **and center**. Main Statistical Analysis says the primary analysis was adjusted on “minimization stratification factors.” Table2 footnote c says Fine–Gray adjusted for cardiogenic shock etiology; SAP names etiology (acute MI, myocarditis, post-heart surgery, other). The primary sHR is1.02,95%CI.74–1.39.
- **Rule and calculation:** The reported set of minimization factors is {etiology,center}; the named model covariate set is {etiology}. The difference is center. This is a logical model-definition comparison; numeric display rounding does not apply.
- **Focus area:** C. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W. The SAP corroborates one side and does not itself add P_R.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** The adjustment specification attached to the primary Fine–Gray sHR1.02(.74–1.39).
- **Why context does not resolve it:** The footnote identifies one covariate, while the main analysis sentence refers to both named minimization factors; the reader cannot tell whether center was included in the fitted primary model.
- **Alternatives/missing definition:** The main sentence may intend etiology alone, or the footnote/SAP wording may omit a center term used in the reported analysis. Neither fitted model formula nor a center term definition is supplied.
- **Exact human question:** “Was center included in the Fine–Gray model producing sHR1.02(95%CI0.74–1.39), and which printed adjustment description applies to that estimate?”

### F-ST1-002 — Planned hierarchical LV-function analysis is replaced by an LVEF median contrast

- **Relationships:** S023, S078.
- **Exact locations and roles:** PLAN [SAP p8, Left Ventricular Function](../../../joi250087supp2_prod_1766516490.96511.pdf#page=8); REPORT [supplement p5, eTable3 LVEF row](../../../joi250087supp3_prod_1766516490.97011.pdf#page=5) and REPORT [p6, footnotes a/b](../../../joi250087supp3_prod_1766516490.97011.pdf#page=6). Original/final PLAN protocol endpoint lists repeat LV function: PDF8/14/15,53/59/60,99/105/106 (complete occurrence keys in S078).
- **Printed statements/values:** SAP specifies Global Net Benefit at D30 using hierarchical death, heart transplantation, and LV improvement defined LVEF>30%, each experimental patient compared with each control patient;95%CI bootstrap. Report prints LVEF45(IQR30–50),n100 vs40(IQR25–50), median difference 5(95%CI−0 to10). For decedents, last available predeath LVEF replaces the D30 value.
- **Rule and calculation:** A hierarchy ranking death before transplantation before LVEF is an outcome composite; it is not a difference in marginal LVEF medians. Planned comparisons101×104=10504 before missing-data handling; the report instead summarizes100/104 LVEF measurements. No Global Net Benefit estimate or CI was found in the complete report union. Numeric rounding cannot reconcile these estimands.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R.
- **Qualifying route:** Route A, category5.
- **Affected result or extracted value:** The D30 LV-function treatment effect: median LVEF difference 5 percentage points versus the planned death/transplant/LVEF hierarchical net benefit.
- **Why context does not resolve it:** Route A category5 covers a changed prespecified outcome composite. The reported substitution of predeath LVEF does not disclose how it relates to the planned hierarchy.
- **Alternatives/missing definition:** An unprovided later amendment may replace the hierarchy; the median contrast might supplement an unreported net-benefit analysis. The supplied report contains no amendment or hierarchy result.
- **Exact human question:** “Which analysis represents the planned D30 LV-function endpoint: the SAP's death/transplant/LVEF Global Net Benefit or the reported median LVEF contrast, and where is any analysis amendment or hierarchical result documented?”

### F-ST1-003 — Dialysis is included in some MACE definitions and omitted from others

- **Relationships:** S024, S028, S030, S033, S043, S044, S077.
- **Exact locations and roles:** PLAN [protocol p8](../../../joi250087supp1_prod_1766516490.96011.pdf#page=8), p14/15, p53/59/60, p99/[p105](../../../joi250087supp1_prod_1766516490.96011.pdf#page=105)/[p106](../../../joi250087supp1_prod_1766516490.96011.pdf#page=106) endpoint lists; PLAN [SAP p4](../../../joi250087supp2_prod_1766516490.96511.pdf#page=4) and [p7 MACE](../../../joi250087supp2_prod_1766516490.96511.pdf#page=7); REPORT [main p3, Outcomes](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=3); REPORT [supplement p1 contents](../../../joi250087supp3_prod_1766516490.97011.pdf#page=1), [p5/6 eTable3](../../../joi250087supp3_prod_1766516490.97011.pdf#page=5) and [p13 eFigure4 caption](../../../joi250087supp3_prod_1766516490.97011.pdf#page=13).
- **Printed statements/values:** All protocol versions and main Outcomes include death, transplant, permanentLVAD, stroke, **dialysis**, HF rehospitalization. SAP and eFigure4 caption include the other five components, without dialysis. eTable3 prints D30 MACE35/101 vs36/104; D60 36/101 vs39/104, and dialysisD30 29/101 vs38/104. D60 dialysis is dash/dash.
- **Rule and calculation:** The component sets differ by dialysis. Composite counts cannot be reconstructed by adding component counts because overlap is unknown; no such sum is assumed. The change affects which participants enter the first-event analysis and its logrank P.87/.94, irrespective of numeric rounding.
- **Focus area:** D (with report result-definition implications). **Proposed review domain:** protocol_report. **Proposed relationship:** P_R; **All relationships:** P_R,P_P,S_C. PLAN version repetition is one pattern, not separate findings.
- **Qualifying route:** Route A, category5.
- **Affected result or extracted value:** D30/D60 MACE patient counts35/36 and36/39, RRs1.00/.95, and logrank comparisons.87/.94.
- **Why context does not resolve it:** Route A category5 covers changed composite definitions. The main report restates the six-component definition while the SAP/caption use five; neither identifies the membership rule used for the actual counts/curves.
- **Alternatives/missing definition:** Dialysis may have been removed by an unprovided amendment, or reported separately while retained in the composite. The source gives no participant-level overlap or explicit composite membership coding.
- **Exact human question:** “Did dialysis count as a MACE component in the reported D30/D60 counts and curves, and which supplied definition or documented amendment governs those results?”

### F-ST1-004 — Organ-failure cutoff differs between SAP and report

- **Relationships:** S014, S015, S057, S075.
- **Exact locations and roles:** PLAN [SAP p4, Organ Failure](../../../joi250087supp2_prod_1766516490.96511.pdf#page=4) and [p7, Organ Failure](../../../joi250087supp2_prod_1766516490.96511.pdf#page=7); REPORT [main p3, predefined secondary outcomes](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=3); REPORT [supplement p5, first two eTable3 rows](../../../joi250087supp3_prod_1766516490.97011.pdf#page=5).
- **Printed statements/values:** SAP defines failure as SOFA score>2 in at least one of six organ systems. Main defines days alive without organ failure as each component score0–1. Report organ-failure-free medians12(IQR0–21) vs14(IQR0–23), difference−2(−10 to4); failure-day medians9(6–17) vs12(6–18), difference−3(−5 to2).
- **Rule and calculation:** For integer SOFA components, absence of any score>2 admits score 2 as failure-free; requiring every score0–1 excludes score 2. A day with one component2 and all others0/1 is classified differently. This exact cutoff comparison is not rounding.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** D30 organ-failure-free medians12/14 and difference−2, and failure-day medians9/12 and difference−3.
- **Why context does not resolve it:** Both are explicit numerical thresholds for the same endpoint; no revised cutoff or coding statement determines which generated the printed day counts.
- **Alternatives/missing definition:** The SAP may intend≥2, or reportfree may intend≤2; the report and plan supply no amendment or participant-day coding. No preferred threshold is proposed.
- **Exact human question:** “Were days with a SOFA component score 2 counted as organ-failure-free or as organ failure in the reported D30 summaries, and which definition produced those numbers?”

### F-ST1-005 — Planned primary post-cardiac-arrest subgroup is absent from the reported predefined subgroup analyses

- **Relationships:** S036–S040, S082.
- **Exact locations and roles:** PLAN protocol PDF8/14/15,53/59/60,99/[105](../../../joi250087supp1_prod_1766516490.96011.pdf#page=105)/[106](../../../joi250087supp1_prod_1766516490.96011.pdf#page=106), every subgroup endpoint list; REPORT [main p4, Statistical Analysis](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=4); REPORT [main p7, Figure3/caption](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=7); REPORT [supplement p9 eTable6](../../../joi250087supp3_prod_1766516490.97011.pdf#page=9) and [p18 eFigure9](../../../joi250087supp3_prod_1766516490.97011.pdf#page=18). PLAN SAP pp1–9 contains no subgroup prescription.
- **Printed statements/values:** Protocol calls primary and secondary analyses predefined in MI, myocarditis, post-cardiac-surgery and **post-cardiac-arrest** patients. Main says predefined minimization-factor subgroups and reports MI,myocarditis,postcardiotomy,**other**; eTable6 places cardiac-arrest-beforeECMO5/21 levosimendan and1/21 placebo inside other. Other sHR1.61(.78–3.33), not an arrest-specific estimate.
- **Rule and calculation:** The planned fourth subgroup and reported fourth subgroup are different sets: 6 arrest patients are a subset of42 other patients. No arrest-specific primary result was found in the complete report scope. This is primary-analysis prespecification/report matching, not a demand for additional exploratory analysis.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R.
- **Qualifying route:** Route A, category5.
- **Affected result or extracted value:** Which primary successful-weaning subgroup analysis is prespecified, and whether the other-group sHR1.61 can be extracted for post-cardiac-arrest patients.
- **Why context does not resolve it:** Route A category5 covers a planned primary analysis not reported. Presence of arrest patients in other does not provide the planned arrest-subgroup comparison.
- **Alternatives/missing definition:** A prespecified amendment may replace arrest with the minimization other category; none supplied changes the subgroup list. The SAP's silence does not explicitly amend it.
- **Exact human question:** “Was the protocol's primary post-cardiac-arrest subgroup analysis replaced by the other-etiology subgroup, and where is the amendment or the separately planned primary subgroup result?”

### F-ST1-006 — Etiology-adjusted analyses for key secondary outcomes are planned but not reported

- **Relationships:** S004–S009, S073, S074, S087.
- **Exact locations and roles:** PLAN [SAP p7, Mortality/ECMO/ICU and Hospital](../../../joi250087supp2_prod_1766516490.96511.pdf#page=7); PLAN [protocol p35/37](../../../joi250087supp1_prod_1766516490.96011.pdf#page=35),p81–84,[p127–130](../../../joi250087supp1_prod_1766516490.96011.pdf#page=129) general adjusted/unadjusted analyses; REPORT [main p1 abstract](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=1), [p4 methods/results](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=4), [p6 Table2](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=6); REPORT [supplement p11 mortality](../../../joi250087supp3_prod_1766516490.97011.pdf#page=11) and [p16 stays](../../../joi250087supp3_prod_1766516490.97011.pdf#page=16). Complete REPORT supplements/eTables were searched through the lossless map.
- **Printed statements/values:** SAP specifies etiology-adjusted Cox for mortality and ICU/hospital duration, and etiology-adjusted general linear model for ECMO duration/free days. These outcomes appear in the abstract, making them key secondary under the scope. Report prints mortality RR1.11(.70–1.75), ECMO medians5/6, ICU RMST18/19, hospitalRMST28/35, bootstrap differences and unadjusted rank/logrank comparisons. No secondary Cox HR or etiology-adjusted general-linear contrast is identified.
- **Rule and calculation:** Named planned models are compared with the complete reported result union. BinaryRR is not a CoxHR; difference of unadjusted medians/RMST is not identified as an etiology-adjusted model coefficient. The missing outputs form one repeated planned-adjusted-analysis reporting pattern. This is not a preference for adjusted analyses; the supplied SAP explicitly prescribes them.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R.
- **Qualifying route:** Route A, category5.
- **Affected result or extracted value:** The planned adjusted mortality, ECMO duration/free-day and ICU/hospital treatment effects for key secondary endpoints.
- **Why context does not resolve it:** Route A category5 covers a planned key secondary analysis not reported. Primary model etiology adjustment does not establish adjustment of these secondary summaries.
- **Alternatives/missing definition:** These adjusted models may have been performed but omitted, or removed by a later unsupplied analysis amendment. A table footnote referring to primary etiology adjustment does not label these secondary effects.
- **Exact human question:** “Where are the SAP-prespecified etiology-adjusted Cox results for mortality and ICU/hospital duration and general-linear results for ECMO duration/free days, or the documented amendment removing those key secondary analyses?”

### F-ST1-007 — Kidney-replacement duration population or coding is unclear relative to the dialysis count

- **Relationships:** S021, S022, S028, S080.
- **Exact locations and roles:** REPORT [supplement p5 eTable3, KRT-duration and dialysis rows](../../../joi250087supp3_prod_1766516490.97011.pdf#page=5); REPORT [p6, footnotes a/b](../../../joi250087supp3_prod_1766516490.97011.pdf#page=6); PLAN [SAP p4 RRT endpoint](../../../joi250087supp2_prod_1766516490.96511.pdf#page=4) and [p8 RRT method](../../../joi250087supp2_prod_1766516490.96511.pdf#page=8).
- **Printed statements/values:** Table arm headersN101/N104. KRT duration byD30 median30(IQR0–30)/30(IQR8–30); difference0(−5 to1). Alive/KRT-free days0(IQR0–2)/0(IQR0–5). The same table lists dialysis byD30 in29/101(28.7%) and38/104(36.5%). Footnote defines continuous rows as median/IQR and identifies missing-observation n when present; no recipient subset or special duration code is printed for KRT.
- **Rule and calculation:** Under the printed full-arm population and ordinary duration-of-treatment interpretation, a30-day median requires at least51/101 and52/104 positive-duration patients; dialysis counts29/38 are below half. This diagnoses a population/coding conflict, while explicitly not treating an unstated zero-assignment or identity of incident dialysis and any KRT as established. If recipients alone were summarized, their n must be named to identify the extracted distribution. Numeric rounding does not change the half-population implication: a printed30 median spans29.5–30.5days, entirely positive.
- **Focus area:** C. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W. SAP corroborates the intended duration endpoint rather than adding a PLAN conflict.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** KRT duration median30days in each arm, its IQR/difference, and the population to which that duration applies.
- **Why context does not resolve it:** Neither a recipient-only n nor coding for patients without KRT, decedents or ongoing treatment identifies how the printed30-day medians arise alongside dialysis incidence below50%. A reader cannot identify the duration distribution being extracted.
- **Alternatives/missing definition:** The row may summarize recipients only, use a transformed/free-day duration code, or distinguish incident dialysis from all KRT. Those possibilities require the unprinted analysis population/coding definition; they are not proposed replacements.
- **Exact human question:** “Which patients and duration-coding rules produced the KRT medians of30days, and how do those populations relate to the29/101 and38/104 patients with dialysis byD30 in the same table?”

### F-ST1-008 — Planned day-60 ECMO-free and ventilator-free outcomes are absent from the reported window-specific results

- **Relationships:** S006, S073, S079.
- **Exact locations and roles:** PLAN protocol PDF8/14/15,53/59/60,99/[105](../../../joi250087supp1_prod_1766516490.96011.pdf#page=105)/[106](../../../joi250087supp1_prod_1766516490.96011.pdf#page=106); PLAN [SAP p4](../../../joi250087supp2_prod_1766516490.96511.pdf#page=4), [p7 ECMO](../../../joi250087supp2_prod_1766516490.96511.pdf#page=7), [p8 Mechanical Ventilation](../../../joi250087supp2_prod_1766516490.96511.pdf#page=8); REPORT [main p1 abstract](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=1), [p3 outcomes](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=3), [p6 Table2 ECMO-free](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=6), REPORT [supplement p5 eTable3 MV-free](../../../joi250087supp3_prod_1766516490.97011.pdf#page=5). Full report tables/figures contain noD60free-day counterpart.
- **Printed statements/values:** Protocol and SAP specify ECMO-free and MV-free outcomes through bothD30 andD60. Main Outcomes repeats both windows; abstract names these outcomes as secondary. Table2 reports ECMO-free **byD30**24(IQR0–26)vs23(12–26), difference1(−1 to4); eTable3 reports MV-free **byD30**6(3–11)vs6(3–13), difference−0(−3 to2). NoD60free-day estimate or analysis is supplied.
- **Rule and calculation:** D30 andD60 outcomes have different observation windows. A D30 result cannot serve as a D60 result. This is a complete-source absence comparison for planned key secondary outcomes (named in the abstract), not a per-timepoint descriptive count comparison. No numerical rounding operation supplies the missing window.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R.
- **Qualifying route:** Route A, category5.
- **Affected result or extracted value:** Prespecified D60 ECMO-free and ventilator-free treatment effects, which are absent despite D30 reports and stated D60 follow-up.
- **Why context does not resolve it:** Route A category5 covers planned key secondary analyses not reported. The plan/report outcome definitions explicitly name both windows and no replacement/omission explanation is provided.
- **Alternatives/missing definition:** D60 outcomes may have been analyzed but omitted or removed by an unsupplied amendment. A generic ECMO-duration row without a window does not report a D60 free-day measure.
- **Exact human question:** “Where are the prespecified D60 ECMO-free and ventilator-free outcome analyses, or the documented amendment explaining their omission from the reported window-specific results?”

## Excluded observations

Only apparent issues considered and not emitted appear here; routine reconciliations remain in the S inventory. One reason code per row. These exclusions require independent pass-2/audit review, especially any printed-number or planned/report element. There is no observation-count target.

| Location | Observation | Reason code |
|---|---|---|
| E01: PLAN SAP p8 RRT paragraph | Death rule repeats 'ventilatory-free days' inside the RRT section; intended RRT-free measure is evident from its heading and same paragraph. No printed number changes. | NOTATION_OR_TYPOGRAPHY |
| E02: REPORT main p1/4 mortality D60 and supplement p11 | Main P.78 differs from explicitly logrank P.56; main categorical-method option allows chi-square and source counts reproduce Yates P .7765 as a diagnostic. Both are nonsignificant; these are binary-count and survival-time tests, not attributed to one named test. | CONTEXT_RESOLVES |
| E03: REPORT main p6 arrhythmia RD/RR intervals | RD95%CI.4–18.1 excludes 0 while RR95%CI.97–4.37 includes 1. No P/test is printed, absolute CI is explicitly bootstrap, and the source does not identify these as the same inferential procedure. Diagnostic log-RR interval reproduces the relative column. This is not an interval-versus-P or stated-test conflict. | CONTEXT_RESOLVES |
| E04: REPORT supplement p5 MV-duration row | Medians 21 vs22 and difference−0 appear different. Half-unit input intervals[20.5, 21.5]/[21.5, 22.5] imply difference[−2, 0], overlapping printed 0 interval[−.5, .5]; gap0. | ROUNDING_OR_DISPLAY_PRECISION |
| E05: REPORT main p7 etiology interaction P.74 | Independent subgroup log-Wald heterogeneity approximation could differ, but joint fitted interaction model/covariance/statistic/df are not supplied. No equality of that approximation to the stated interaction test is established by other rows. | CONDITIONAL_OR_UNREPORTED |
| E06: REPORT supplement p18 eFigure9 myocarditis/post-surgery traces | Truncated/crossing cumulative-incidence curves do not by themselves reverse the time-weighted sHR or equal D30 success risks. No exact end-of-window coordinates/test can be extracted from these traces. | CONDITIONAL_OR_UNREPORTED |
| E07: REPORT main p6 Figure2 risk/event arrays | Physical-risk plus cumulative-events complement checks assume an unprinted risk-row/event-row definition. Fine–Gray augmented risk can retain competing-event participants; the source does not establish those arrays as complementary populations. Exact printed counts remain in S055 for numeric/pass2 review. | CONDITIONAL_OR_UNREPORTED |
| E08: PLAN protocol p37/84/130, SAP p5; REPORT main p3 | 101 events/206 subjects lacks a printed full sample-size equation. Diagnostic event count 100.2508 rounds 101 and target CIF.702698 rounds 70%; a naive 101/.50=202 versus 206 has half-unit interval [199.0099,205.0505] (101 events ±.5 and control 50% ±.5 percentage points), printed 206 interval [205.5,206.5], gap .4495/206=.002182≤.05, and assumes control incidence for the pooled event rate. | ROUNDING_OR_DISPLAY_PRECISION |
| E09: REPORT supplement p5 D7 cardiovascular-free outcome versus PLAN lists | The specific D7 SOFA component contrast is not named in plan, but the report does not call that row prespecified and broad organ function follow-up is supplied. An unprinted prespecification detail alone does not establish status/composite change. | CONDITIONAL_OR_UNREPORTED |
| E10: REPORT table footnotes withhold secondary P while narrative/plots print P | Footnote says P values are not reported in the secondary table; it does not state every report location withholds all secondary P. No formal multiplicity family or adjusted alpha claim is supplied. | CONTEXT_RESOLVES |
| E11: PLAN SAP p3 and protocol versions' calendar/site projections | SAP 24-month recruitment versus active protocol 39-month recruitment and 13/14 planned versus 11 reported sites are administrative comparisons; planned 206 power input unchanged and amendments disclosed. | PERIPHERAL_COMPARISON |
| E12: PLAN SAP cover 11/04/2025 and changes-before-unblinding rule | A final SAP date after follow-up does not establish unblinding date or committee validation; no supplied statement places analysis changes after unblinding. | CONDITIONAL_OR_UNREPORTED |
| E13: REPORT main p8 sample limitation | Assumed 50% failure versus actual 32% is complement of 50% planned/68.3% observed success; no formal post hoc power number claimed. 'Underpowered' wording alone does not supply a reproducible contradictory statistical result. | TERMINOLOGY_OR_WORDING |
| E14: PLAN protocol p13/58/104 historical Affronti | Weaning 83.3% vs27.3% with P.498 looks numerically striking, but historical sample sizes, test, paired structure and intervals absent; no supported method reproduces surrounding display rows because no common display test is specified. | CONDITIONAL_OR_UNREPORTED |
| E15: PLAN protocol p13/58/104 historical Distelmaier | 'Lower survival' alongside HR<1 lacks historical modeled event definition; significance CI/P pairs reconcile. Wording alone cannot establish reversed quantitative event direction. | TERMINOLOGY_OR_WORDING |

## Closure and limitations

Pass 1 complete: 107 relationships; 8 findings; 15 excluded apparent observations; 0 scientific coverage gaps. Definitions limiting mechanical checking: raw ranks/event times, numerical test statistics/SE, bootstrap algorithm, RR interval algorithm, subgroup interaction model/covariance, Figure 2 risk/event-row mapping, full sample-size equation, KRT duration population/coding. The named gaps do not authorize candidate omission in an always-register category. No severity, validity or correction is assigned. All findings remain for independent inclusion screen and human question preparation.

Calculation artifacts: [R diagnostics](../preprocessing/statistics_1/calculations.R) and [complete recorded output](../preprocessing/statistics_1/calculation_record.txt), engine R4.5.2. Full display-precision propagation for the naive sample-size diagnostic includes 50% ±0.5 percentage points. The SAE multiplicity check gives140/139 events, distinct from59/61 patients with at least one SAE.

## Explicit pass-1 completion records mirrored from the agent-authored inventory

The coordinator mechanically mirrors the first reviewer's complete per-relationship assessment and PASS_1_COMPLETE status from its separately authored inventory, so this checker also enumerates every relationship. No scientific decision or candidate is added. Six diagnostic transcription decimals and the key-SAE wording retain the transparent second-pass corrections recorded in the inventory and pass-2 artifact; printed source values remain unchanged.

| S ID | Agent-authored pass-1 assessment | Status |
|---|---|---|
| S001 | Contained/ordered; all null included, P>.05; repeated values match. Diagnostic log-Wald P.902 is not Gray P.92 and does not establish a conflict. | PASS_1_COMPLETE |
| S002 | Contained/ordered; negative RD and sHR<1 agree; CI/test nonsignificant. Diagnostic Wald P.328. Numerical test type for competitor P not separately named. | PASS_1_COMPLETE |
| S003 | Contained/ordered; positive RD and sHR>1 agree; diagnostic Wald P.469; no significance conflict. | PASS_1_COMPLETE |
| S004 | Contained/ordered; RR count calculation1.164; diagnostic log-RR CI[.713, 1.899]; all nonsignificant. Survival P need not equal binary-count test. | PASS_1_COMPLETE |
| S005 | Contained/ordered; diagnostic RR1.1089 CI[.7013, 1.7535]; Yates chi-square P .7765 rounds.78. Different survival/count tests give different P; no significance conflict. Exclusion E02. | PASS_1_COMPLETE |
| S006 | Contained/ordered; 24-23=1. Difference/CI bootstrap; no P printed. Planned D60 counterpart tracked S073. | PASS_1_COMPLETE |
| S007 | Contained/ordered; difference-1; CI includes0 and P>.05 agree; raw ranks not supplied. | PASS_1_COMPLETE |
| S008 | Contained/ordered; 17.5 rounds18, not a numeric conflict; RMST/bootstrap CI and logrank are distinct functional analyses. | PASS_1_COMPLETE |
| S009 | Contained/ordered; -7 matches displayed RMSTs; longer placebo stay agrees; no P printed; no multiplicity-adjusted superiority assertion inferred. | PASS_1_COMPLETE |
| S010 | Ordered/contained; diagnostic RR2.0594 CI[.9710, 4.3678] reproduces; RD-bootstrap versus RR intervals straddle different nulls. No same-test duality stated. Exclusion E03. | PASS_1_COMPLETE |
| S011 | Ordered/contained; diagnostic log-Wald SE.173696/P.4210; null included, P nonsignificant. | PASS_1_COMPLETE |
| S012 | Ordered/contained; diagnostic SE.350865/P.7881. | PASS_1_COMPLETE |
| S013 | Ordered/contained; diagnostic SE.398981/P.2582. | PASS_1_COMPLETE |
| S014 | Ordered/contained; difference-2; threshold mapping S075. | PASS_1_COMPLETE |
| S015 | Ordered/contained; difference-3; exposure/free days need not add30 under death 0/ICU discharge. | PASS_1_COMPLETE |
| S016 | Ordered/contained; death 0 free days; no P. | PASS_1_COMPLETE |
| S017 | Ordered/contained; difference-1; recipient-specific individual-drug durations p8 are different populations/quantities. | PASS_1_COMPLETE |
| S018 | Ordered/contained; degenerate bootstrap median CI can occur with point-mass zero; endpoint plan mapping S084. | PASS_1_COMPLETE |
| S019 | Ordered/contained; signed zero is same numeric0; death 0 free days planned. | PASS_1_COMPLETE |
| S020 | Ordered/contained; half-unit inputs imply difference[-2, 0], overlapping printed0[-.5, .5], gap0. Exclusion E04. | PASS_1_COMPLETE |
| S021 | Ordered/contained difference; duration population/coding does not explain median30 at dialysis incidence<50%. F-ST1-007; do not assume all nonusers were coded0 as an established source fact. | PASS_1_COMPLETE |
| S022 | Ordered/contained; degenerate median bootstrap CI possible. Duration/free mapping kept separate S021. | PASS_1_COMPLETE |
| S023 | Ordered/contained, difference 5; planned GNB/death-transplant-LVEF composite mapping F-ST1-002. | PASS_1_COMPLETE |
| S024 | Ordered/contained; crude RR1.0011; absolute crude .0381 pp rounds0.0; composite S077. | PASS_1_COMPLETE |
| S025 | Ordered/contained; source expressly withholds RR at zero events; no P printed. | PASS_1_COMPLETE |
| S026 | Ordered/contained; crude RD.1142/RR1.0297 match; no P. | PASS_1_COMPLETE |
| S027 | Ordered/contained; repeated exact results, crude RD1.1615/RR1.2013 match. | PASS_1_COMPLETE |
| S028 | Ordered/contained; crude RD-7.82559025/RR.7858 match; S021 duration comparison and S077 composite implication. | PASS_1_COMPLETE |
| S029 | Ordered/contained; repeated exact results; zero-event RR rule applies. | PASS_1_COMPLETE |
| S030 | Ordered/contained; crude RD-1.8564/RR.9505 match; no P in table; logrank S044. | PASS_1_COMPLETE |
| S031 | Ordered/contained; same events as D30; no invented RR/P. | PASS_1_COMPLETE |
| S032 | Ordered/contained; crude RD-.8473/RR.8238 match. | PASS_1_COMPLETE |
| S033 | No invented count; absent descriptive D60 row not itself primary/key-secondary missing-analysis finding; composite S077. | PASS_1_COMPLETE |
| S034 | Model identity and all row CIs checked; no numerical algorithm/replications supplied; no formal secondary adjusted alpha supplied. | PASS_1_COMPLETE |
| S035 | Distinct estimands kept separate, no t-test from printed RMST SD inferred; adjustment wording S069. | PASS_1_COMPLETE |
| S036 | Ordered/contained; main direction favors placebo agrees sHR; eFigure9 crossing curves cannot alone determine constant sHR direction. E06. | PASS_1_COMPLETE |
| S037 | Ordered/contained; faster placebo curve direction generally agrees; crude risk is not sHR. | PASS_1_COMPLETE |
| S038 | Ordered/contained; higher levo effect favorable; eFigure9 truncated trace not a printed D30 probability. | PASS_1_COMPLETE |
| S039 | Ordered/contained; favorable levo label agrees; includes5 levo/1placebo post-arrest in eTable6. | PASS_1_COMPLETE |
| S040 | Overall matches S001; interaction model, statistic, df and covariance not supplied. Individual subgroup CIs cannot reproduce stated interaction; E05. | PASS_1_COMPLETE |
| S041 | Arrays retained exactly in support map; 30-day totals match S004; event timing between ticks unavailable, so P not recomputed from coarse arrays. | PASS_1_COMPLETE |
| S042 | Totals match S005; coarse arrays insufficient for exact logrank. | PASS_1_COMPLETE |
| S043 | No significant MACE claim conflicts; shaded CIs no numeric bounds. Component sums need not equal patients with first event. | PASS_1_COMPLETE |
| S044 | Same nonsignificant conclusion as RD/RR; composite differs between protocol/report narrative and SAP/caption, S077. | PASS_1_COMPLETE |
| S045 | Crude RD-.23800457 rounds-.2; SAE multiplicity S060 not same estimand. | PASS_1_COMPLETE |
| S046 | Crude RD9.49162224; noCI/P. | PASS_1_COMPLETE |
| S047 | Crude RD6.76884996; noCI/P. | PASS_1_COMPLETE |
| S048 | Crude RD2.3610; noCI/P. | PASS_1_COMPLETE |
| S049 | Crude RD2.99885758; noCI/P. | PASS_1_COMPLETE |
| S050 | Both event counts0, difference0; no inferential test invented. | PASS_1_COMPLETE |
| S051 | Repeated S010, all occurrence locations preserved. | PASS_1_COMPLETE |
| S052 | Crude RD2.99885758; distinct subset from S051. | PASS_1_COMPLETE |
| S053 | Crude RD-.9330; noCI/P. | PASS_1_COMPLETE |
| S054 | Crude RD8.0350; temporary/definitive differs from definitive flow11/3. | PASS_1_COMPLETE |
| S055 | Exact rows retained; event/risk-row definitions not supplied beyond labels. Fine–Gray augmented risk differs from physical risk. Do not require complements without definition. E07; exact counts remain available to numeric checker and pass2. | PASS_1_COMPLETE |
| S056 | Component sums15/21 match failure; total101/104; classification accords SAP removal-date event coding, not subsequent-component dates. | PASS_1_COMPLETE |
| S057 | All bars inspected by mapper; no exact graph coordinates invented; threshold association S075. | PASS_1_COMPLETE |
| S058 | Descriptive plot replaces hemodynamic-improvement analysis explicitly in SAP; missing arm error-bar definition alone not finding. | PASS_1_COMPLETE |
| S059 | Matches S008/009 under display precision; histograms not exact event-time/risk data. | PASS_1_COMPLETE |
| S060 | Patient totals101/104; ≥1 totals59/61 match S045; weighted event counts140/139 differ from patient incidence by definition. Planned Poisson S081. | PASS_1_COMPLETE |
| S061 | Medians within ordered quartiles; sparse epinephrine curve interpolation not daily observed exposure. No inferential P/model printed. | PASS_1_COMPLETE |
| S062 | Recipient durations differ from all-patient catecholamine duration; ordered quartiles; no additional effect/P. | PASS_1_COMPLETE |
| S063 | No inferential baseline test implied; SAP summary definitions match mean/SD ormedian/IQR selection; counts separately tracked by numeric lane. | PASS_1_COMPLETE |
| S064 | Dose statement comparison retained for numeric/XS review; intervention regimen matches active amended protocol; no dose-effect hypothesis invented. | PASS_1_COMPLETE |
| S065 | Stated individual design coherent with models; no noninferiority/equivalence margin or conclusion supplied anywhere. | PASS_1_COMPLETE |
| S066 | Endpoint/date/backdated qualification matches; clinically retrospective qualification internally stated, not preferred-method critique. | PASS_1_COMPLETE |
| S067 | Event coding is explicitly source-grounded and coherent; no generic independent-risk versus subdistribution-risk inference. | PASS_1_COMPLETE |
| S068 | SAP/report agree on named models; protocol general Fine–Gray comparison refined in SAP. Primary unadjusted Gray and adjusted sHR are different analyses. | PASS_1_COMPLETE |
| S069 | F-ST1-001: center-adjustment description does not specify actual primary model. | PASS_1_COMPLETE |
| S070 | No stated diagnostic outcome contradicts model; missing printed check result alone not finding. | PASS_1_COMPLETE |
| S071 | Diagnostic event equation 100.2508→101; CIF conversion.702698→70%; exact total 206 reproduction lacks printed equation/censoring inputs. No substantive >5% discrepancy shown; E08. | PASS_1_COMPLETE |
| S072 | Population definitions agree; 205 analysed (101/104) includes censored, not complete-case denominator. Noninformative censoring specified, not empirically audited. | PASS_1_COMPLETE |
| S073 | F-ST1-006 tracks missing planned adjusted model; D60-specific estimates absent; F-ST1-008 tracks D60 key secondary reporting. | PASS_1_COMPLETE |
| S074 | RMST design accounts right-censoring coherently; F-ST1-006 planned adjusted models not located. | PASS_1_COMPLETE |
| S075 | F-ST1-004 definition difference at score 2; same nonfailure complement differs by one ordered category. | PASS_1_COMPLETE |
| S076 | Report median outcomes; missing adjustment results for non-key secondary alone not raised; dose/recipient quantities separate S061/062. | PASS_1_COMPLETE |
| S077 | F-ST1-003 consolidated P_R/P_P/S_C pattern; dialysis component 29/38 at D30 could affect membership. | PASS_1_COMPLETE |
| S078 | F-ST1-002: composite planned analysis replaced in report; no GNB number supplied. | PASS_1_COMPLETE |
| S079 | F-ST1-008 absent D60 key secondary analysis; half-unit difference S020 screened; no raw data to infer swapped labels. | PASS_1_COMPLETE |
| S080 | E01 obvious duplicated term in RRT paragraph; F-ST1-007 separate source-grounded duration/population question. | PASS_1_COMPLETE |
| S081 | Stated plan coherent with recurrent counts; report has descriptive tables/plots, no identified adjusted Poisson output. Serious adverse events are abstract-named key secondary outcomes; their missing planned adjusted Poisson result is already included in C007, not a new finding. | PASS_1_COMPLETE |
| S082 | F-ST1-005: primary post-arrest subgroup not separately reported, other includes 5/1 post-arrest; source contains planned list, not a raw data exploratory demand. | PASS_1_COMPLETE |
| S083 | Disclosed revised endpoint agrees; not a missing planned-analysis finding. Protocol general SBP/DBP/HR stabilization descriptive differences not quantified as key secondary. | PASS_1_COMPLETE |
| S084 | Broad organ-failure measurement contains component data; report does not explicitly call this specific D7 analysis prespecified. Missing definition/status claim alone E09, not category 5. | PASS_1_COMPLETE |
| S085 | No hierarchy, family adjustment, interim spending or significance boundary supplied; omission of P in the table does not state all report locations withhold P. E10. | PASS_1_COMPLETE |
| S086 | Active amendment explicitly deletes monthly text; no formal interim/stopping decision reported; missing numeric boundary is not a finding. | PASS_1_COMPLETE |
| S087 | F-ST1-006: key secondary adjusted analyses not located; alternative post-SAP amendment not supplied. | PASS_1_COMPLETE |
| S088 | Missing secondary imputation algorithm alone no finding; LVEF substitution is concrete planned/report contrast S078. | PASS_1_COMPLETE |
| S089 | Active regimen agrees; no intervention duration/statistical hypothesis mismatch. | PASS_1_COMPLETE |
| S090 | Deleted/inserted text separated; disclosed amendment context resolves phase placebo/infusion wording. | PASS_1_COMPLETE |
| S091 | Target analysis population mapping covered; abbreviated main list versus complete supplement not incompatible. | PASS_1_COMPLETE |
| S092 | Same protocolized criteria in both arms; no reported different threshold that would change the primary event. | PASS_1_COMPLETE |
| S093 | Stopping drug does not remove ITT; definitive 11/3 versus suspected AE any cessation 12/4: different definition. | PASS_1_COMPLETE |
| S094 | Calendar/site differences peripheral; power input 206 unchanged; disclosed amendments supply active chronology. E11. | PASS_1_COMPLETE |
| S095 | Unblinding date not supplied; date alone cannot establish violation; E12. | PASS_1_COMPLETE |
| S096 | Complement of assumed 50% success is 50% nonsuccess; reported 68.3% success complement 31.7% rounds 32; wording does not define a formal post hoc power calculation. E13. | PASS_1_COMPLETE |
| S097 | sHR95%CI.74–1.39/P.92 supports no demonstrated superiority; no equivalence/null-proof assertion or margin inferred. | PASS_1_COMPLETE |
| S098 | Contained/ordered, CI includes 1/P>.05; model/test details absent, no binary-HR comparison. | PASS_1_COMPLETE |
| S099 | No CI/test/arm n supplied to reproduce P; no significance claim conflicts. | PASS_1_COMPLETE |
| S100 | No mathematical test input; historical design details are not LEVOECMO prespecification. | PASS_1_COMPLETE |
| S101 | Ordered/contained and null included/P nonsignificant; no stated futility rule permits checking the historical stop boundary. | PASS_1_COMPLETE |
| S102 | No CI, n, paired test or unpaired test definition supplied; large percentage contrast alone cannot establish a P conflict. E14. | PASS_1_COMPLETE |
| S103 | Direction matches narrative; test missing, no contradictory CI. | PASS_1_COMPLETE |
| S104 | Each point contained/ordered/null excluded with P<.05; narrative 'lower survival' with HR<1 lacks named modeled historical event; wording E15. | PASS_1_COMPLETE |
| S105 | Ordered/contained; both CIs exclude 1/P<.05; diagnostic log-Wald P.026 matches second. No external verification. | PASS_1_COMPLETE |
| S106 | Ordered/contained; favors lower death; diagnostic log-Wald P.0043; coherent. | PASS_1_COMPLETE |
| S107 | Explicit no-applicable-inferential-unit closure; all pages mapped, no scientific coverage gap. | PASS_1_COMPLETE |
