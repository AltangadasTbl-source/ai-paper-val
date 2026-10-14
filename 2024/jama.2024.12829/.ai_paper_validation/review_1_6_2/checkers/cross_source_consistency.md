# Cross-source consistency review

Fresh mandatory cross-source stage: runtime 01a12bd6-75c0-7d23-80cf-cb43aa47bcbe, gpt-6.1-sol / medium. Complete scope: DOC-001 REPORT pp1–11, DOC-002 REPORT pp1–25, DOC-003 PLAN pp1–167; all 203 mapped pages. Checking began after the coordinator confirmed the canonical support map's lossless complete merge. QUALITY_CONTROL_SCOPE.md and the full 1.6.2 review contract were read before checking. No earlier checker, candidate, screening, disposition, classification or report was used; no external evidence was used.

The main map and all seven new support-map parts were read in bounded segments. Matched results were checked across the abstract, Key Points, narrative, tables, figures, captions and footnotes. No Office or CSV direct source is supplied. Original/final protocols and SAPs were kept distinct; amendment pages124–126 and165–166 disclose version changes. Source PDFs remain authoritative. Relevant current-source pages were reread with the supplied pdf_tools.py and pinned PyMuPDF1.26.4. DOC-002p13 was rendered with that helper, CPU,200dpi, to preprocessing/cross_checker/report-supp-p13.png and inspected visually. The current DOC-002p24 render preprocessing/stat1-supp-p24.png was inspected to resolve a derivative glyph discrepancy. No new OCR was needed; sources and reused assets were preserved.

## Completed comparisons

| Matched scope | Exact coverage | Comparison outcome |
|---|---|---|
| Primary result and components | Main pp1–5,7–9; supplement pp18–23. Match population, enrollment/procedural windows, artery territory, composite/components, adjustment, reference group, HR,CI,P and events. | Abstract,Key Points and main primary 11/249 versus34/252,HR0.32(0.16–0.63),P<.001 agree. Component overlap is explicitly allowed. Center-adjusted count is F-XS-003. |
| Primary subgroup list | Original protocolp41,finalp103,SAPpp140/160 versus mainpp4/5/7; all11 factors and every category/cutoff compared individually. | Age,sex,hypertension,diabetes,smoking,eGFR,stenosis,location,stroke/TIA agree. Planned hypoperfusion yes/no matches report CTP definition; SAP collateral-assessment wording does not negate that binary plan. BMI is F-XS-001. |
| Center analyses | SAPpp136/155–156; mainpp4/6; supplementpp19/20. Separate unadjusted primary,adjusted sensitivity and center interaction. | HR/CI/P copies agree. Prospective status is F-XS-002. Numerical population/header comparisons are independently covered by numeric checker. |
| Secondary and safety copies | Mainpp1/3/5–8; supplementpp13/17/18/23/24. Thirty-day stroke/death,90-day/1-year territory stroke/death,outside-territory stroke,mRS,revascularization,vascular composite,EQ-5D,restenosis,hemorrhage,complications and disabling stroke. | Matched result copies agree except registered primary-count/death comparisons. Planned common OR versus reported generalized OR is explicitly explained by assumption failure. Disabling-stroke threshold visually reads ≥2 in both sources. |
| Outcome definitions/statuses | Original protocolpp8/18–21,finalpp65–66/76/78–80; originalSAPpp130–131,finalpp148–150/160–161; reportpp1/3/8,supplementpp18–23. | Every original10/final19 secondary item matched by status,components and time. Added30-day and24-/36-month outcomes are disclosed amendments. Later outcomes explicitly not yet reported. Full primary includes postprocedure30-day window. Acute revascularization requires occlusion plus deficit/intervention; elective requires recurrent imaging-confirmed stroke or hard TIA>10min/new disabling symptoms. Criterion lists agree item by item. |
| Models/covariates/populations | Protocolpp40/102; SAPpp134–142/153–162; mainpp4–6/Figure1,supplementpp19–24. | Treated/as-randomized primary set,PP/ATS sensitivities,KM/log-rank/Cox,ordinal mRS plan,EQ-5D tests,multiplicity and sidedness individually compared. No contradictory covariate list printed. Plan permits finalizing serious PP violations at review. Withdrawal rules matched to complete follow-up apart from deaths; no unsupported population switch inferred. |
| Power/hypothesis/interim/stopping | Protocolpp11–12/40–41/69/76/103; SAPpp134/151/153/165–166; mainpp3–4. | 802→512,old12.2%-based50% reduction→15%/7%,80% power,10% dropout and removal of interim are disclosed changes. One-sided2.5% planning/two-sided.05 reporting have the same standard directional critical value. Safety review distinguished from interim efficacy analysis. |
| Eligibility/intervention/analysis-set criteria | All4 inclusion and24 original/25 final exclusion items: protocolpp9–11/21–23/66–69/81–83,amendments124–126. AMM/procedurepp25–30/85–91,SAPpp133/151–152,reportpp2–3/Figure1,supplementpp6/16–17/25. | Final35–80years,70–99% stenosis,arterial segments,stroke14–90days/TIA<90days,prior treatment,mRS<3,DAPT and supplying-artery rules matched to report summary. Full criteria available via protocol pointer; omissions alone do not establish changed eligibility. Aspirin100mg throughout,clopidogrel75mg90days,resistance substitutions,atorvastatin20–80mg1year,LDL/HbA1c targets,submaximal≤70%,success/rescue rules and follow-up continuation compared individually. |
| Remaining mapped pages | Front matter,contents,site/training/CEC/enrollment displays,risk targets,medications,devices,instruments,references. | Complete unit coverage via fresh maps. Administrative/per-time-point/baseline copies remain peripheral unless a qualifying result or analysis population changes. No external reference validation or methodological preference introduced. |

## Findings

### F-XS-001

**Reporting issue:** BMI subgroup categories differ from the supplied prespecification although all reported forest-plot analyses are called prespecified.

**Compared locations and roles:** REPORT [mainp4 statistical analysis](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=4), [mainp5 subgroup narrative](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5), [mainp7 Figure2 BMI](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=7); PLAN [original protocolp41](../../../joi240088supp2_prod_1746815064.36071.pdf#page=41), [final protocolp103 line1779](../../../joi240088supp2_prod_1746815064.36071.pdf#page=103), [original SAPp140 line2357](../../../joi240088supp2_prod_1746815064.36071.pdf#page=140), [final SAPp160 line2768](../../../joi240088supp2_prod_1746815064.36071.pdf#page=160).

**Printed statements:** Mainp4 says all subgroup analyses in the forest plot were prespecified; p5 repeats prespecified baseline factors. All four PLAN occurrences specify BMI<25,25–30,≥30kg/m². Figure2 reports only <25 versus≥25: HR0.17(0.05–0.57) and0.48(0.21–1.11),interactionP=.17; ≥25 has BA8/139 andAMM17/142.

**Comparison logic:** Match primary composite,1-year follow-up,primary population and BMI factor. Three planned categories become two reported categories, combining the two strata above25. The final SAP retains all three and no supplied amendment changes this partition. This changes the subgroup contrast/model partition rather than its name. Display precision is not applicable to a categorical specification.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R. **All relationships:** P_R.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Prespecification and analysis identity of BMI effect modification, especially HR0.48 and interactionP=.17 for BMI≥25.

**Why context does not resolve it:** Category5 covers an analysis called prespecified whose exact reported partition is absent from supplied plans; the planned three-category primary-outcome subgroup analysis is not displayed. A prespecified factor does not by itself specify the merged contrast.

**Supported alternatives:** A separate unsupplied amendment may authorize merging; the factor may have been prespecified while regrouping was later chosen. No reason for merging is inferred.

**Human question:** Which prespecification authorizes BMI<25 versus≥25, and was the planned three-category BMI interaction analyzed or replaced?

### F-XS-002

**Reporting issue:** Center-effect adjustment is called post hoc although both supplied SAP versions specify a primary-outcome center-adjusted sensitivity analysis.

**Compared locations and roles:** PLAN [original SAPp136 §9.1 lines2263–2267](../../../joi240088supp2_prod_1746815064.36071.pdf#page=136), [final SAPp155](../../../joi240088supp2_prod_1746815064.36071.pdf#page=155) and [p156 §9.1 lines2667–2674](../../../joi240088supp2_prod_1746815064.36071.pdf#page=156); REPORT [mainp4 post hoc list](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=4), [mainp6 adjusted result](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=6), [supplementp19 TableS6 title/footnote](../../../joi240088supp1_prod_1746815064.21247.pdf#page=19).

**Printed statements:** Both SAPs specify no center adjustment for main analysis,center-adjusted sensitivity,small centers pooled with larger centers,and Cox treatmentHR adjusted for center. Mainp4 lists center-effect adjustment results for the primary endpoint among post hoc analyses; mainp6 reports HR0.32(0.16–0.62),P=.001. S6 is titled post hoc center-effect adjustment and describes BeijingTiantan versus other centers.

**Comparison logic:** Match primary composite,1-year follow-up,Cox treatmentHR and center covariate. The general center-adjusted sensitivity is explicitly planned; the report characterizes adjustment results as post hoc. A later binary grouping choice is distinguishable from an unplanned center-adjustment analysis. No HR/CI/P difference is alleged; display precision is not applicable.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R. **All relationships:** P_R.

**Qualifying route:** Route B.

**Affected result or extracted value:** Planned versus exploratory interpretation of center-adjusted primary HR0.32(0.16–0.62),P=.001.

**Why context does not resolve it:** Original SAP already contains the sensitivity analysis. The broad post hoc label does not distinguish later choice of binary grouping from later choice of the analysis itself. This concerns the primary sensitivity's analysis specification/prospective status, rather than group names, and affects its interpretation as support for the primary result.

**Supported alternatives:** General center adjustment was planned but binary grouping was post hoc; another planned implementation exists but is not reported; the label refers only to a narrower implementation. The source does not distinguish these alternatives.

**Human question:** Does post hoc refer only to grouping Tiantan versus other centers, and how does S6 relate to the center-adjusted primary sensitivity in both SAPs?

### F-XS-003

**Reporting issue:** The center-adjusted primary table prints a different balloon-group primary event count from the main table under the same declared population.

**Compared locations and roles:** REPORT [mainp8 Table2 primary](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=8),corroborated by [mainp7 Figure2 overall](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=7); REPORT [supplementp19 TableS6 primary/footnote](../../../joi240088supp1_prod_1746815064.21247.pdf#page=19). [Supplementp21 TableS8](../../../joi240088supp1_prod_1746815064.21247.pdf#page=21) is an alternative-population locator,not another contradiction.

**Printed values:** Main primary BA11(4.4),n249; AMM34(13.5),n252. S6 BA9(3.9),n249; AMM34(13.5),n252; HR0.32(0.16–0.62),P=.001. Footnote describes group/center adjustment without another population or composite. PPS TableS8 also has BA9(3.9),but expressly names PPS.

**Comparison logic and precision:** Full primary composite and declared n249 are matched. Count intervals[10.5,11.5] versus[8.5,9.5] leave gap1; relative discrepancy1/11=.090909>.05. Percentage intervals[4.35,4.45] versus[3.85,3.95] leave gap.40 percentage points; relative discrepancy.40/4.4=.090909>.05. Covariate adjustment changes modeled HR,not by itself the observed event count in the same declared population. This is not a modeled-versus-crude estimate comparison.

**Focus area:** A. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_C. **All relationships:** S_C.

**Qualifying route:** Route B.

**Affected result or extracted value:** Balloon-group primary events/risk in the adjusted sensitivity,9(3.9) versus11(4.4),and which population produced adjustedHR0.32.

**Why context does not resolve it:** Both displays declare249/252 and the full primary definition. No event exclusions are disclosed in S6. S8's9(3.9) suggests an alternative population but does not identify S6's actual population.

**Supported alternatives:** An undisclosed restricted/complete-case population; a count/percentage shared with PPS; or another unreported count definition. These are alternatives,not inferred production mechanisms.

**Human question:** Which participants and observed primary event count underpin S6,and why does BA9(3.9) differ from11(4.4) under the same declared n249?

### F-XS-004

**Reporting issue:** The one-year mRS distribution assigns a different death percentage to AMM from the main one-year death statement.

**Compared locations and roles:** REPORT [mainp8 Table2 footnoteg](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=8), [mainp7 death narrative](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=7); REPORT [supplementp13 FigureS5 AMMscore6](../../../joi240088supp1_prod_1746815064.21247.pdf#page=13). PLAN [final protocolp115 mRS definition](../../../joi240088supp2_prod_1746815064.36071.pdf#page=115) corroborates score6=death; it does not create a PLAN relationship.

**Printed values:** Main footnoteg says AMM death within1year0.4%(1/252); narrative identifies one AMM death beyond30days due to a motor vehicle crash. FigureS5 is captioned1year,declares AMMN252,and score6 reads0.8%(N=2). mRS6 is death. BA1(0.4) agrees across locations.

**Comparison logic and precision:** Match AMM,all-cause death,1year and declared n252. Main.4% interval[.35,.45] versusfigure.8% interval[.75,.85] leaves gap.30 percentage points; relative discrepancy.30/.4=.75>.05. Integer count intervals[.5,1.5] and[1.5,2.5] touch; the percentage comparison independently reproduces the discrepancy. No different regression method is assumed.

**Focus area:** A. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_C. **All relationships:** S_C.

**Qualifying route:** Route B.

**Affected result or extracted value:** AMM one-year all-cause death proportion and the death category in the mRS distribution,.4% versus.8%.

**Why context does not resolve it:** Figure labels the same time/group n252 without another death definition,analysis set or window. Main explicitly says all-cause death,so exclusion of a nonvascular cause cannot reconcile it.

**Supported alternatives:** An undisclosed window/analysis set,or figure category values requiring clarification. The figure's separate count/percentage arithmetic is handled by numeric review; no replacement value is assigned here.

**Human question:** Why does S5 show AMM mRS6(death).8%(N2) at1year when Table2 gives.4%(1/252),and which death category belongs to the one-year mRS analysis?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| Mainp3/supplementp24 S11b | Text derivative showed >2 for disabling stroke; current source render prints ≥2,matching main. A derivative glyph is not a reporting finding. | NOT_REPRODUCED |
| Protocol/SAP amendmentspp124–126/165–166;mainpp3–4 | 802/interim versus512/no interim,21→14-day stroke eligibility,and added outcomes differ by version; disclosed amendments explain report's final design. | CONTEXT_RESOLVES |
| Final protocolp103/SAPp153/mainp3 | One-sided.025 planning versus two-sided.05 reporting share the standard directional critical value; final SAP also specifies two-sided.05 reporting. | CONTEXT_RESOLVES |
| Original protocolp11 versusp41/SAPp134 | Planning6.25% versus6.1%: intervals[6.245,6.255] and[6.05,6.15],gap.095/6.1=.015574≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| Original protocolp11 versusp41 | Synopsis90% confidence is not explicitly identified as80% power's counterpart; treating confidence as power assumes an unstated meaning. | TERMINOLOGY_OR_WORDING |
| Original protocolp41/SAPp134/synopsisp11 | Historical SAMMPRIS experimental-arm12.2% is an input; it does not itself assign12.2% to BASIS balloon arm. | CONTEXT_RESOLVES |
| Protocolpp65/77/89,SAPp152,mainp3,supplementp25 | Synopsis BP130–140/90–100 versus detailed≤140/90(nonDM),≤130/80(DM),main abbreviated≤140/90. No qualifying primary result,population size or statistical decision changes are established. | PERIPHERAL_COMPARISON |
| Protocolp81/mainp5 Figure1 | Planned lesion≤10mm versus actual excluded subjects described as>15mm does not establish a changed threshold or retained10–15mm subjects. | CONDITIONAL_OR_UNREPORTED |
| Final SAPp161/mainp5/supplementp17 | Planned comparative restenosis OR not displayed; report gives BA15.7%. Outcome is not key secondary under supplied definition,no conflicting comparative OR claim; omission alone does not qualify. | CONDITIONAL_OR_UNREPORTED |
| Mainp4/protocolp102/SAPp161 | Ordinal logistic common OR replaced with generalized OR after explicitly reported assumption failure; report does not attribute generalized OR to planned model. | CONTEXT_RESOLVES |
| Mainp8 abbreviated primary label/fullp3/SAPp148/supplementpp19–22 | Postangioplasty window omitted in short row label but explicit full definition supplies it; no displayed result attributed to another composite. | TERMINOLOGY_OR_WORDING |
| Mainpp2/4/final SAPpp153–154/158 | Eligible/ITT/FAS/mITT names while protocol violations retained in primary but excluded in PPS do not establish different numeric primary sets; flow gives501. | TERMINOLOGY_OR_WORDING |
| Mainp6/supplementp14 baseline | Baseline copy differences are peripheral; within-display arithmetic independently covered by numeric review. | PERIPHERAL_COMPARISON |
| Mainp3/supplementpp6/9 | Diagram30±3days versus30±7days and completion calendars differ without an established qualifying result,population size or decision-rule change. | PERIPHERAL_COMPARISON |
| Original protocolp21/p22 | Original inclusion14–90days and exclusion<21days differ; disclosedV2.1/final criteria use14days. No final analysis-set decision or qualifying result discrepancy established from this superseded criterion copy. | PERIPHERAL_COMPARISON |

## Completion and limitations

Four findings;15 excluded observations. All203 mapped pages and all matched result/design families covered without finding caps; no scientific coverage gap. Numeric checker independently covers S7/S8 sensitivity-header pattern(F-NUM-003) and S6 count discrepancy(F-NUM-002),which may be merged with F-XS-003 by the independent inclusion screen. FigureS5 death percentage remains a separate matched-result observation from within-figure denominator arithmetic. Direct rendering confirms S11b≥2 despite extracted>2. No candidate IDs,dispositions,preferred analysis or final corrections assigned. No raw data or unprinted model details assumed.
