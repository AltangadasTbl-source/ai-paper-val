# Cross-source consistency review

Status: COMPLETE. Runtime ID: 01a129b9-0d28-70a3-a6a4-0dc8194fcb34. Assigned scope: all eligible matched REPORT results across the nine-page main article, five-page results supplement and one-page data-sharing statement; all prospective statistical design relationships in the 129-page PLAN bundle, including initial protocol, patient-information final-protocol section, original statistical strategy and published final plan. There are no supplied structured result files. Fourteen findings and thirteen excluded observations are recorded. No candidate IDs or human dispositions are assigned.

QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read completely. Current main and support maps were read for relationship discovery, with no earlier scientific conclusions consulted. Their complete historical/background and administrative records were inspected for matching eligibility; they do not become HIGH trial results. Exact source text was reread using available Poppler 25.03.0 pdftotext, native/layout modes, CPU, transient stdout. Relevant source locations include main pp.1–8, PLAN pp.6–7, 38, 40–42, 45–47, 53–55, 61, 82, 98–105. Preserved source-matched PNGs for main p.7 and results supplement p.3 were visually inspected. Sources and reusable assets were preserved. There was no rendering, OCR, network use, or new derivative.

## Comparison matrix

Each row is one bounded matched relationship group. There are 72 groups, including item-by-item eligibility, outcome, intervention, analysis-set and decision criteria. Main IDs refer to extraction/main_quantitative_evidence.md; support keys refer to extraction/support_quantitative_evidence.md. All PDF page numbers are physical pages. REPORT main is jama_azoulay_2018_oi_180109.pdf, REPORT supplement is joi180109supp2_prod.pdf, PLAN is joi180109supp1_prod.pdf. Exact linked locations for findings follow. Completed checks that reconcile are listed here, never in the excluded-observation table.

| Group | Matched keys and exact roles/locations | Comparison and completed outcome |
|---|---|---|
| XS01 | N001, N008, N009; REPORT main pp.1, 3, 5; R4-02 REPORT supplement p.2 | 778 randomized, 389 per arm; two consent withdrawals; 776 analyzed, 388 per arm. Consistent once randomized versus analyzed populations are matched. Abstract intervention wording is handled in exclusions. |
| XS02 | S012, S013; REPORT main pp.1, 2, 5, 8 | Day-28 all-cause mortality risks 35.6%/36.1%, RD −0.5 (−7.3, 6.3), HR .98 (.77, 1.24), P .94 and nonsignificant conclusion match. |
| XS03 | S014, S015; REPORT main pp.1, 5, 6; R4-03 REPORT supplement p.3 | Day-28 IMV counts 150/170, risks 38.7%/43.8%, RD−5.1 (−12.3, 2.0) and direction match; figure terminal geometry agrees approximately. Test attribution: F-XS-003. |
| XS04 | S016; REPORT main pp.1, 5, 6 | Infection risks 10.0%/10.6%, RD−.6 (−4.6, 4.1), nonsignificance repeated consistently. Analysis-plan comparison separately XS54. |
| XS05 | S019, S020; REPORT main pp.1, 5, 6 | ICU stay medians 8/6, effect .6 (−1, 2.2); hospital stay24/27, effect−2 (−7.3, 3.3) match. Median summaries and mean differences are distinct quantities. |
| XS06 | S021, S022; REPORT main pp.1, 6; R4-02 REPORT supplement p.2 | Six-hour respiratory medians 25/26 and mean difference−1.8 match. Upper CI−.2 versus−.3 overlaps at half-unit boundaries; excluded as precision. |
| XS07 | S023, N010; REPORT main pp.1, 3, 6; R4-02, R4-05 REPORT supplement pp.2, 4 | PaO2/FiO2 medians 150/119 at six hours and mean effect19.5 (4.4, 34.6) repeat; abstract attribution to three days after intubation conflicts with randomization-based series: F-XS-001. |
| XS08 | S024; REPORT main pp.1, 6; R4-06, R4-07 REPORT supplement p.5 | Comfort/dyspnea nonsignificance has no conflicting exact numeric counterpart; graphical uncertainty unspecified, no fabricated test. Planned model and measures separately XS55, XS60. |
| XS09 | S029, S013; REPORT main pp.5, 6 | Cox-associated P .94 and explicitly log-rank P .85 are different named tests; apparent matched-P observation excluded. |
| XS10 | S015, S031–S056; REPORT main pp.5–7 | All-patient and subgroup forest direction/reference compared; recurring reference ambiguity and inverse IMV HR: F-XS-002. |
| XS11 | N004, S009, S031, S032, S044, S045; REPORT main pp.2, 4, 5, 7 | ICU-time stratification ≤2/≥3 differs from forest0–1/≥2; subgroup total321/330 agrees with days 0+1 Table 1; F-XS-013. |
| XS12 | S009, S033, S034, S039–S042, S046, S047, S052–S055; REPORT main pp.4, 5, 7; S-P 2-010, P4-06 PLAN pp.45, 98–99 | Figure title says predefined; supplied plans contain oxygenation in initial protocol, but no diagnosis or hematologic-malignancy subgroups: F-XS-014. |
| XS13 | N005, N056; REPORT main pp.2, 3, 5; R4-02 REPORT supplement p.2 | Initiation50 L/min; 6-hour50[50–60]; discomfort substitution exceptions distinguish received treatment versus allocation. No matched conflict. |
| XS14 | N044, N045; REPORT main pp.1, 4, 5; R4-04, R4-05 REPORT supplement p.4 | Baseline medians 33/32 and136/128 versus approximate graph means34/32.9 and143/126 are unmatched summary types; excluded. |
| XS15 | N058, R4-03; REPORT main p.6 and REPORT supplement p.3 | Mortality and IMV risk tables have different event/removal rules; not copies of the same population at risk. No matched conflict asserted. |
| XS16 | N003; P4-05; REPORT main p.2; PLAN p.98 | Adult age≥18 criterion matches item by item. |
| XS17 | N003; P4-05; REPORT main p.2; PLAN p.98 | Immunosuppressive drugs criterion matches. |
| XS18 | N003; P4-05; REPORT main p.2; PLAN p.98 | Steroid duration>3 months or dose>.5mg/kg/day matches. |
| XS19 | N003; P4-05; REPORT main p.2; PLAN p.98 | Solid-organ transplant criterion matches. |
| XS20 | N003; P4-05; REPORT main p.2; PLAN p.98 | Solid-tumor cancer care versus chemotherapy in last5 years: wording observation excluded. |
| XS21 | N003; P4-05; REPORT main p.2; PLAN p.98 | Hematologic malignancy criterion matches; report elaboration does not change printed result attribution. |
| XS22 | N003; P4-05; REPORT main p.2; PLAN p.98 | Primary immune deficiency matches final plan; report AIDS exclusion versus initial HIV inclusion resolved by explicitly revised population/version. |
| XS23 | N003; S314, P4-05; REPORT main pp.1, 2; PLAN pp.90, 98 | ICU ARF admission and oxygen≥6 L/min match; report operational PaO2/SpO2/distress list adds definition to ARF. No source conflict in final eligibility. |
| XS24 | N003; P4-05, S305; REPORT main p.2; PLAN pp.74, 79, 98 | Patient/proxy informed consent and later refusal/withdrawal exclusion match. Emergency consent timing not a contradictory analysis rule. |
| XS25 | N003; P4-05; REPORT main p.2; PLAN p.98 | Moribund/imminent-death exclusion matches. |
| XS26 | N003; P4-05; REPORT main p.2; PLAN p.98 | Refusal exclusion matches. |
| XS27 | N003; P4-05; REPORT main p.2; PLAN p.98 | PaCO2≥50/formal NIV indication exclusion matches. |
| XS28 | N003; P4-05; REPORT main p.2; PLAN p.98 | Isolated cardiogenic edema exclusion matches; plan allowance for mixed etiologies does not conflict with word isolated. |
| XS29 | N003; P4-05; REPORT main p.2; PLAN p.98 | Pregnancy/breastfeeding exclusion matches. |
| XS30 | N003; P4-05; REPORT main p.2; PLAN p.98 | Cannula-precluding anatomy exclusion matches. |
| XS31 | N003; P4-05; REPORT main p.2; PLAN p.98 | No French insurance coverage exclusion matches. |
| XS32 | N003; S314, P4-05; REPORT main p.2; PLAN pp.90, 98 | Recent surgery days 1–6 exclusion matches. |
| XS33 | N005; P4-03; REPORT main pp.2, 3; PLAN p.100 | HFNO initial50 L/min and FiO2 100% match. |
| XS34 | N005; P4-03; REPORT main pp.2, 3; PLAN p.100 | Minimum50 L/min first3 days, up to60, targetSpO2≥95% and FiO2 taper match; initial40 L/min version superseded. |
| XS35 | N005; P4-03; REPORT main p.3; PLAN pp.96, 100 | Use during laryngoscopy/immediately after extubation matches. Other procedure detail absent without conflict. |
| XS36 | N005, N056; P4-03; REPORT main pp.3, 5; PLAN p.100 | Flow reduction for discomfort and temporary Venturi substitution match. Plan's isolated standard-oxygen sentence is excluded as wording resolved by paragraph. |
| XS37 | N006; P4-03; REPORT main p.3; PLAN p.100 | Stop criterion distress improvement matches. |
| XS38 | N006; P4-03; REPORT main p.3; PLAN p.100 | Stop criterion PaO2/FiO2>300 matches. |
| XS39 | N006; P4-03; REPORT main p.3; PLAN p.100 | Stop criterionSpO2≥95% on<6 L/min matches final; initial<2 replaced. No maximum-duration conflict. |
| XS40 | N006; P4-07; REPORT main p.3; PLAN p.99 | Standard devices and SpO2 target match. |
| XS41 | N006, N056; P4-07; REPORT main pp.3, 5; PLAN p.99 | No-control-HFNO rule versus rescue in DNI patients, 30 crossovers: F-XS-011. |
| XS42 | N006; P4-03, P4-07; REPORT main p.3; PLAN pp.99, 100 | NIV only hypercapnia/edema while indicated matches. |
| XS43 | N006; P4-07; REPORT main p.3; PLAN p.99 | ICU dischargeSpO2≥95% on<6 L/min matches final rule. |
| XS44 | N004; P4-06; REPORT main p.2; PLAN pp.98, 99 | ICU timeD0–2/≥3 and catecholamines stratification match; exact9 L/min boundary changes: F-XS-012. |
| XS45 | N004; P4-06, P1-S001, S-P 2-012; REPORT main p.2; PLAN pp.6, 50, 99 | Individual1:1 allocation, blocks and centralized concealment match. Isolated center-unit phrase excluded as wording. |
| XS46 | S001; P1-S001, S301, P4-02; REPORT main p.3; PLAN pp.6, 71, 97 | Initial noninferiority9% versus final superiority explicitly disclosed before grant/IRB; final hypothesis matches. |
| XS47 | N010, S004; P1-S004, S-P 2-001, P4-02, P4-11; REPORT main p.3; PLAN pp.6, 7, 46, 97, 102 | Primary all-cause mortality28 days after randomization matches final; early admission-origin versus randomization discrepancy resolved for reported endpoint by final version. |
| XS48 | S002; P1-S006, S317, P4-13; REPORT main pp.3, 7; PLAN pp.6, 91, 103 | Final assumptions30%/20%, alpha 5%, power 90%, 389 each match; total779 versus778 excluded as precision. Initial26%/9%/80%/816 pertains disclosed earlier design. |
| XS49 | S003; S-P 2-018, S-P 2-031, P4-10, P4-14, P4-22; REPORT main pp.3, 5; PLAN pp.53, 61, 102, 103, 107 | Final one interim100 deaths, .001 threshold, Bayesian uniform prior and continuation match. Initial no-interim/scheduled-safety-interim texts excluded as superseded. |
| XS50 | S010, S011; S-P 2-015, P4-14, P4-15; REPORT main pp.4, 5, 8; PLAN pp.52, 103, 104 | Two-sided secondary P, final .05 and no numeric secondary multiplicity correction conflict. Exploratory status comparison separately XS61. |
| XS51 | S004, N008, N009; S-P 2-005, S-P 2-019, S305, P4-05, P4-15; REPORT main pp.3, 5; PLAN pp.42, 53, 74, 79, 98, 104 | Full randomized set, allocated arm and consent-withdrawal exception match. No exclusion for missing data conflicts with the plan. |
| XS52 | S004; S-P 2-020, S-P 2-021, P4-16; REPORT main p.3; PLAN pp.53, 54, 104 | Primary loss anticipated absent, no actual follow-up loss; conditional time-to-event missingness and multiple imputation lack trigger/outcomes, excluded omission only. |
| XS53 | S005, S013; S-P 2-022, S307, P4-17; REPORT main pp.3, 5, 8; PLAN pp.54, 82, 104 | Primary RR plan versus HR report: F-XS-004. Planned adjusted and PP primary analyses absent: F-XS-005. |
| XS54 | S006, S007, S015, S016; S-P 2-024, S309, S310, P4-18; REPORT main pp.3–6; PLAN pp.54, 82, 105 | IMV Gray/Cox matches in broad model but live discharge omitted from competing events; infection χ2 versus planned Gray/competing-risk model: F-XS-006 includes both endpoint specification changes. |
| XS55 | S008, S023, S024; S-P 2-026, S312, P4-20; REPORT main pp.4, 6; REPORT supplement pp.4, 5; PLAN pp.55, 82, 105 | Joint censoring-aware longitudinal analysis absent; reported Wilcoxon symptom tests: F-XS-007. |
| XS56 | S008, S019; S-P 2-025, S311, P4-19; REPORT main pp.4–6; PLAN pp.54, 82, 105 | Planned ICU-stay KM/competing-risk and separate survivor/decedent analyses versus Wilcoxon aggregate: F-XS-008. |
| XS57 | S009; S-P 2-023, S308, P4-17; REPORT main pp.4, 7; PLAN pp.54, 82, 104 | Gail–Simon interaction statistic matches; conditional significant-interaction subset follow-up not assumed absent when no significant primary interaction. |
| XS58 | S014, S015; S-P 2-003, P4-12; REPORT main pp.1, 3, 5, 6; PLAN pp.38, 46, 103 | Intubation day 28 status and IMV definition match final; day 3 initial secondary removed within disclosed endpoint revision. |
| XS59 | S019, S024; S-P 2-003, P4-12; REPORT main pp.1, 3, 5, 6; PLAN pp.38, 46, 103 | ComfortVAS, respiratory rate, ICU stay and infection endpoint names match final. |
| XS60 | S023, S024; S-P 2-003, P4-12; REPORT main pp.1, 3, 6; REPORT supplement pp.2, 4, 5; PLAN pp.38, 46, 103 | LowestSpO2 and Borg dyspnea prespecified in retained abstract-reported oxygenation/dyspnea outcomes, absent results: F-XS-009. |
| XS61 | S010, S026; S-P 2-003, S-P 2-010, P4-12; REPORT main pp.4, 6, 8; PLAN pp.38, 45–47, 103 | Secondary analyses called exploratory as inferential caution, excluded as wording; initial secondary intubated mortality called post hoc: F-XS-010. |
| XS62 | S017, S018, S020; P4-08; REPORT main pp.1, 3, 5, 6; PLAN p.101 | Hospital stay appears in planned collection, so abstract report does not establish an unplanned endpoint. ICU/hospital mortality status not labeled prespecified by article; no unsupported claim inferred. |
| XS63 | S-P 2-003, S-P 2-010, S309 versus P4-12, P4-18; PLAN pp.38, 45–47, 82, 103, 105; REPORT main pp.3, 4, 6 | Pulmonary-infiltrate clearance, oxygen/ventilation-free survival, reintubation, peri-intubationSpO2, DNI-specific outcomes and satisfaction are removed from final named endpoint list; not abstract/key-secondary and revision disclosed. No unreported-key-secondary assertion. |
| XS64 | S-P 2-002, S-P 2-004; PLAN pp.40–42; S001 REPORT main p.3 | Initial lower-bound decision wording conflicts with illustrative geometry, but abandoned noninferiority rule does not govern reported superiority. Excluded as context. |
| XS65 | S-P 2-015, P4-15; PLAN pp.52, 104 | NIV primary-hypothesis name versus HFNO everywhere else; excluded as immediately resolvable terminology, no number attribution changes. |
| XS66 | P1-N001; PLAN p.1 versus initial/final design sections; REPORT main p.3 | No-amendment cover versus differently named initial/final plans does not override explicit report chronology; no statistical amendment timing inferred. |
| XS67 | N002; N-P 2-001, N-P 2-002, S314, P4-04, P4-22; REPORT main pp.1, 2; PLAN pp.33–37, 90, 97, 107 | Site/recruitment differences are administrative; consolidated peripheral exclusion. |
| XS68 | N012–N053; P1-N003, P4-24; REPORT main p.4; PLAN pp.10, 122–123 | Generic measurement/device definitions do not reproduce baseline values. No baseline-table counterpart supplied; within-table arithmetic belongs numeric checker. |
| XS69 | P1-N008–P1-N017, N303–N309, P4-01, P4-27; PLAN pp.20–31, 93–95, 127–128 | Historical studies remain distinct from HIGH. Copies/rounding of historical rationale not result/design-relevant cross-source findings; clipped final historical table limitation retained. |
| XS70 | R4-02–R4-07; REPORT supplement pp.2–5 | Exact eTable quantities and graphical mean-like points/undefined bars matched only by time/outcome; no conditional inference that bars are95%CI . |
| XS71 | S313, P4-12, S011; PLAN pp.83, 103; REPORT main p.5 | SAS plusR plan versus reportedR3.1.0 has no changed numeric analysis demonstrated; no finding. |
| XS72 | R4-08; REPORT data-sharing statement p.1 | No numeric result, prospective analysis specification or matching statistical design element. COMPLETE_NO_APPLICABLE_COMPARISON. |

## Findings

### F-XS-001

The abstract assigns oxygenation to a post-intubation period while the reported matching result belongs to the randomization-based oxygenation series.

- **Locations and roles:** REPORT [main p.1, Main Outcomes and Results](../../../jama_azoulay_2018_oi_180109.pdf#page=1); REPORT [main p.6, Secondary Outcomes](../../../jama_azoulay_2018_oi_180109.pdf#page=6); REPORT [supplement p.2, eTable](../../../joi180109supp2_prod.pdf#page=2) and [p.4, eFigure 2B](../../../joi180109supp2_prod.pdf#page=4). Mapper keys N010, S023, R4-02, R4-05.
- **Printed statements and values:** Abstract secondary outcome is PaO2/FiO2 over three days after intubation; its150 versus119 and difference 19.5 (95%CI 4.4–34.6) reappear in narrative describing higher oxygenation until day 4. The eTable explicitly reports150[104–230] versus119[86–165] six hours after randomization; eFigure 2 uses randomization, H6, days 1–7.
- **Comparison logic:** Match150/119 and19.5 interval across abstract/narrative; then compare outcome time origin and population. Post-intubation subset/time is not interchangeable with the randomized oxygenation series. No arithmetic discrepancy is alleged: matching printed numeric intervals overlap, discrepancy0; display precision cannot convert the two time/population definitions.
- **Focus area:** B/C. **Proposed review domain:** report_internal_inconsistency. **Relationship type:** S_C. **All relationships:** S_C, S_W.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Population and measurement window for the PaO2/FiO2 treatment effect19.5 (4.4–34.6).
- **Why context does not resolve it:** Both post-intubation oxygenation and early randomized oxygenation are plausible outcomes, and the abstract explicitly assigns a different time origin rather than using an abbreviated endpoint name.
- **Supported alternatives:** The abstract may intend three days after randomization; a separate intubated-subset result may be intended, but none of the supplied displays identifies19.5 as that result.
- **Exact human question:** Does the oxygenation effect19.5 (95%CI 4.4–34.6) apply to measurements after randomization or after intubation, and to which patients and measurement window?

### F-XS-002

The forest plots use effect directions that do not reconcile with the corresponding overall IMV HR and their favors labels.

- **Locations and roles:** REPORT [main p.5, Table 2 IMV](../../../jama_azoulay_2018_oi_180109.pdf#page=5); REPORT [main p.6, Secondary Outcomes](../../../jama_azoulay_2018_oi_180109.pdf#page=6); REPORT [main p.7, Figure 3A and3B, all13 rows of each panel, headings/axes/caption](../../../jama_azoulay_2018_oi_180109.pdf#page=7). Keys S015, S031–S057.
- **Printed values:** Table 2/narrative IMV 150/388 versus170/388, HR .85(.68, 1.06). Figure 3B repeats150/388 versus170/388 but HR 1.17(.94, 1.46); its left side favors HFNO and right side favors standard. Figure 3A all-patient HR 1.02(.81, 1.29) versus Table 2 mortality.98(.77, 1.24). Affected Figure 3 rows in both panels are ICU-time0–1/≥2, PaO2/FiO2<200/≥200, flow≤9/>9, catecholaminesNo/Yes, unknown diagnosisNo/Yes, hematologic malignancyNo/Yes, and all patients.
- **Calculation and precision:** IMV copied-HR intervals [.845, .855] and[1.165, 1.175] have gap .310; relative discrepancy.310/.85=.3647. Reciprocating the Table 2 HR interval yields point[1.1696, 1.1834], lower-limit range approximately[.9390, .9479], upper-limit range[1.4599, 1.4815], consistent with the forest's printed reciprocal reading. This is a reference-direction diagnostic, not a crude-risk replacement of Cox. The mortality .98/1.02 numerical copy alone falls below5% and is not independently registered; it supports the recurring reference pattern. Subgroup curves/raw times are unavailable, so no subgroup Cox recomputation is asserted.
- **Focus area:** B. **Proposed review domain:** statistical_results. **Relationship type:** S_W. **All relationships:** S_W.
- **Qualifying route:** Route A, category2.
- **Affected result or extracted value:** Direction/reference of all Figure 3 mortality and IMV forest estimates, especially overall IMV 1.17(.94, 1.46) versus.85(.68, 1.06).
- **Why context does not resolve it:** Category2 applies to the reproduced overall IMV reversal. The printed favors labels invite the opposite interpretation from a reciprocal contrast; they do not identify a reference change.
- **Supported alternatives:** Figure 3 may use standard/HFNO while Table 2 uses HFNO/standard; in that case its favors headings require clarification. A different model is possible but not described as a different overall comparison.
- **Exact human question:** Which treatment is the numerator/reference in each Figure 3 panel, and should the figure's HRs and favors headings be interpreted with the same contrast as Table 2?

### F-XS-003

The matching IMV cumulative-incidence result is attributed to Gray testing in the article and log-rank testing in the supplement.

- **Locations and roles:** REPORT [main p.3, competing-risk definition](../../../jama_azoulay_2018_oi_180109.pdf#page=3); REPORT [main p.4, methods continuation](../../../jama_azoulay_2018_oi_180109.pdf#page=4); REPORT [main p.5, Table 2 IMV P=.17](../../../jama_azoulay_2018_oi_180109.pdf#page=5) and [p.6, IMV result and supplement pointer](../../../jama_azoulay_2018_oi_180109.pdf#page=6); REPORT [supplement p.3, eFigure 1](../../../joi180109supp2_prod.pdf#page=3). Keys S006, S015, R4-03.
- **Printed statements:** Article cumulative incidence with death withoutIMV as competing risk, compared by Gray test; matching IMV P=.17. eFigure 1 labels cumulative incidence of mechanical ventilation and P(log Rank test)=.17.
- **Comparison logic:** Same randomized population, time since randomization, day 28 IMV and P .17, but different named inferential procedures. Numeric copies overlap[.165, .175], discrepancy0; this is method attribution, not a numeric-copy difference .
- **Focus area:** C. **Proposed review domain:** statistical_results. **Relationship type:** S_C. **All relationships:** S_C.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Test identity for the reported day 28 cumulative-IMV P=.17.
- **Why context does not resolve it:** Gray and log-rank tests target differently handled event processes; neither the figure nor its article pointer says separate tests produced the coincident printed P .
- **Supported alternatives:** The graph may show an additional log-rank comparison; alternatively its test label may denote the article's Gray comparison. The supplied material does not distinguish these possibilities.
- **Exact human question:** Is eFigure 1 P=.17 from the Gray test or a separate log-rank test, and how were competing events handled for that plotted comparison?

### F-XS-004

The primary effect measure changes from planned risk ratio to reported hazard ratio.

- **Locations and roles:** PLAN [p.54, lines 808–812](../../../joi180109supp1_prod.pdf#page=54), [p.82, lines 1297–1300](../../../joi180109supp1_prod.pdf#page=82), [p.104, lines 1730–1734](../../../joi180109supp1_prod.pdf#page=104); REPORT [main p.3, primary methods](../../../jama_azoulay_2018_oi_180109.pdf#page=3), [p.5, Table 2](../../../jama_azoulay_2018_oi_180109.pdf#page=5). Keys S-P 2-022, S307, P4-17, S005, S013.
- **Printed specifications:** Plan binary alive/dead at day 28, relative risk of hospital death experimental/control with95%CI . Article Kaplan–Meier, absolute RD and univariable CoxHR.98(.77, 1.24); Table 2 uses RR for ICU/hospital mortality but HR for primary day 28 mortality.
- **Comparison logic:** Same primary treatment comparison and day 28 endpoint; RR and HR are different estimands. No numerical conflict is claimed between a hazard ratio and a crude risk ratio. Numeric precision is not applicable to a categorical effect-measure change.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Primary day 28 mortality effect-measure identity and planned versus reported estimand.
- **Why context does not resolve it:** The final published plan retains RR while the report specifies CoxHR; the disclosed noninferiority-to-superiority revision does not explain this final-plan measure change.
- **Supported alternatives:** CoxHR may replace the planned RR; alternatively a planned RR analysis may have been performed but not supplied. Hospital-death wording may refer to day 28 death, which does not equate RR with HR .
- **Exact human question:** Was the prespecified primary day 28 risk-ratio analysis replaced by the Cox hazard-ratio analysis, and where is the applicable analysis-plan change or the planned RR result documented?

### F-XS-005

Prespecified adjusted and per-protocol primary analyses are not reported in the supplied results.

- **Locations and roles:** PLAN [p.53, lines 786–787](../../../joi180109supp1_prod.pdf#page=53), [p.54, lines 808–812](../../../joi180109supp1_prod.pdf#page=54), [p.82, lines 1297–1300](../../../joi180109supp1_prod.pdf#page=82), [p.104, lines 1723, 1734](../../../joi180109supp1_prod.pdf#page=104); REPORT [main p.3, univariable primary analysis](../../../jama_azoulay_2018_oi_180109.pdf#page=3), [p.5, Table 2](../../../jama_azoulay_2018_oi_180109.pdf#page=5), [p.8, unadjusted-treatment-effect limitation](../../../jama_azoulay_2018_oi_180109.pdf#page=8); REPORT results supplement pp.1–5 contains no PP or adjusted-primary display. Keys S-P 2-017, S-P 2-022, S307, P4-15, P4-17, S005, S010.
- **Printed specifications:** Final plan explicitly says per-protocol analysis will be performed and analyses adjusted for potential confounders will be performed. Article reports allocation-based388-per-arm univariableCox and states effects were not adjusted for stratification factors. Its post hoc site frailty model is a different specified analysis.
- **Comparison logic:** Complete report search across article/supplement finds no PP primary population/result and no planned adjusted-primary result. This is a planned primary analysis omission, not merely an unreported model detail. Missing PP membership rules and covariate names are acknowledged; numeric rounding is not applicable.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route A, category5.
- **Affected result or extracted value:** Primary mortality sensitivity to adherence-based population and prespecified confounder adjustment.
- **Why context does not resolve it:** Category5 applies; an unadjustedITT result and post hoc site model do not supply the planned PP and confounder-adjusted analyses.
- **Supported alternatives:** These analyses may exist outside the supplied report; PP may coincide with another set, but substantial reported treatment crossovers mean equality cannot simply be assumed. The final plan may retain superseded requirements without a disclosed corresponding amendment.
- **Exact human question:** Were the final-plan per-protocol and confounder-adjusted primary analyses performed, and what are their populations, covariates and results, or the documented reason for their replacement?

### F-XS-006

The reported ICU-acquired-event analyses differ from the planned competing-risk specification.

- **Locations and roles:** PLAN [p.54, lines 816–821](../../../joi180109supp1_prod.pdf#page=54), [p.82, lines 1305–1310](../../../joi180109supp1_prod.pdf#page=82), [p.105, lines 1738–1742](../../../joi180109supp1_prod.pdf#page=105); REPORT [main p.3, IMV competing risk](../../../jama_azoulay_2018_oi_180109.pdf#page=3), [p.4, infection/IMV methods](../../../jama_azoulay_2018_oi_180109.pdf#page=4), [p.5, Table 2 infection footnoted cause-specificHR](../../../jama_azoulay_2018_oi_180109.pdf#page=5), [p.6, secondary outcomes](../../../jama_azoulay_2018_oi_180109.pdf#page=6). Keys S-P 2-024, S309, S310, P4-18, S006, S007, S015, S016.
- **Printed specifications/values:** Plan both intubation/infection cumulative incidence with death or liveICU discharge competing, Gray tests and adjusted cause-specificCox. Report intubation death-withoutIMV competition and univariableCox; infection proportions compared byχ2; infection39/388 versus41/388, HR 1.01(.96, 1.06), P .91, footnoted cause-specificHR.
- **Comparison logic:** Named shared key-secondary endpoints have changed test/model/event specifications. LiveICU discharge is absent from article's explicit IMV competing-event definition; infectionχ2 is not plannedGray. No inference from crude counts is substituted for model estimates. Precision not applicable to these analysis-rule differences.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** IMV/infection cumulative-incidence estimands, competing events, infectionP.91 and effectHR1.01.
- **Why context does not resolve it:** The report explicitly identifies different methods while neither article nor results supplement explains replacement of the final-plan competing-risk strategy.
- **Supported alternatives:** The article may omit live-discharge competition from a fuller implemented model; infectionHR may arise from an additionalCox analysis whileχ2 suppliesP.91. Both require identification of the actual analysis rather than inferred conventions.
- **Exact human question:** Which competing events, adjustment and tests generated the reported IMV and infection results, and how do they relate to the final-plan Gray/cause-specificCox specification with death and live discharge competing?

### F-XS-007

The planned longitudinal joint analyses are not supplied alongside the reported symptom and oxygenation results.

- **Locations and roles:** PLAN [p.55, lines 825–826](../../../joi180109supp1_prod.pdf#page=55), [p.82, lines 1314–1315](../../../joi180109supp1_prod.pdf#page=82), [p.105, lines 1745–1747](../../../joi180109supp1_prod.pdf#page=105); REPORT [main p.4, Wilcoxon methods](../../../jama_azoulay_2018_oi_180109.pdf#page=4), [p.6, oxygenation/comfort/dyspnea results](../../../jama_azoulay_2018_oi_180109.pdf#page=6); REPORT [supplement p.4, eFigure 2](../../../joi180109supp2_prod.pdf#page=4) and [p.5, eFigure 3](../../../joi180109supp2_prod.pdf#page=5). Keys S-P 2-026, S312, P4-20, S008, S023, S024, R4-05, R4-06, R4-07.
- **Printed specifications:** Plan longitudinal oxygenation, dyspnea and comfort joint models accounting for right censoring. Article Wilcoxon rank-sum for symptom scores, nonsignificance at each time and oxygenation advantage untilday4; supplement displays repeated observations without joint-model results.
- **Comparison logic:** All three are abstract-reported key secondary outcomes. Complete supplied reports contain no named joint-model result. Wilcoxon symptom tests and time-specific graphs do not reproduce the planned longitudinal censoring-aware analysis. No graph-bar confidence convention is assumed. Precision not applicable.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route A, category5.
- **Affected result or extracted value:** Interpretation of oxygenation benefit and null comfort/dyspnea effects as prespecified longitudinal analyses versus time-specific comparisons.
- **Why context does not resolve it:** Category5 applies to the absent planned key-secondary joint analyses.
- **Supported alternatives:** Joint models may underlie an unlabelled oxygenation comparison; alternatively they were replaced by available-case/time-specific tests. Neither model components nor joint estimates are supplied.
- **Exact human question:** Were the prespecified joint longitudinal models for oxygenation, dyspnea and comfort fitted, and where are their estimates or the documented replacement analysis?

### F-XS-008

The planned ICU-stay survival and survivor/decedent analyses are not reported.

- **Locations and roles:** PLAN [p.54, lines 822–824](../../../joi180109supp1_prod.pdf#page=54), [p.82, lines 1311–1313](../../../joi180109supp1_prod.pdf#page=82), [p.105, lines 1742–1745](../../../joi180109supp1_prod.pdf#page=105); REPORT [main p.4, Wilcoxon ICU-stay method](../../../jama_azoulay_2018_oi_180109.pdf#page=4), [p.5, Table 2](../../../jama_azoulay_2018_oi_180109.pdf#page=5), [p.6, secondary outcomes](../../../jama_azoulay_2018_oi_180109.pdf#page=6). Keys S-P 2-025, S311, P4-19, S008, S019.
- **Printed specifications/values:** Plan ICU stay overall and separately in survivors/deceased, using Kaplan–Meier and competing-risk estimators. Report Wilcoxon, aggregate medians 8(4–14)/6(4–13), mean difference .6(−1, 2.2), P .07; Table 2 says stay effect could not be expressed byHR.
- **Comparison logic:** ICU stay is abstract-reported key secondary. No supplied survivor/decedent results or planned survival/competing-risk ICU-stay estimates accompany the aggregate Wilcoxon result. Absence is anchored to explicit planned analyses; precision not applicable.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route A, category5.
- **Affected result or extracted value:** ICU-stay effect and its handling of mortality-associated stay distributions.
- **Why context does not resolve it:** Category5 applies; a pooled stay summary does not supply the planned subgroup/estimator results.
- **Supported alternatives:** Planned separate/survival analyses may be available elsewhere or replaced; the plan's former/latter wording leaves estimator allocation unclear, but the entire specified strategy is absent rather than clarified by report.
- **Exact human question:** Were the planned overall and survivor/decedent ICU-stay analyses with Kaplan–Meier/competing-risk estimators performed, and where are their results or documented replacement?

### F-XS-009

Retained key-secondary outcome definitions contain prespecified measures absent from the supplied results.

- **Locations and roles:** PLAN [p.38, lines 548–550](../../../joi180109supp1_prod.pdf#page=38), [p.46, lines 688–691](../../../joi180109supp1_prod.pdf#page=46), [p.103, lines 1694–1697](../../../joi180109supp1_prod.pdf#page=103); REPORT [main p.1, abstract](../../../jama_azoulay_2018_oi_180109.pdf#page=1), [p.3, endpoint definitions](../../../jama_azoulay_2018_oi_180109.pdf#page=3) and [p.6, dyspnea/oxygenation results](../../../jama_azoulay_2018_oi_180109.pdf#page=6); REPORT [supplement p.2, eTable](../../../joi180109supp2_prod.pdf#page=2), [p.4, eFigure 2B](../../../joi180109supp2_prod.pdf#page=4), [p.5, eFigure 3B](../../../joi180109supp2_prod.pdf#page=5). Keys S-P 2-003, P4-12, S023, S024, R4-02, R4-05, R4-07.
- **Printed specifications:** Final plan dyspneaVAS andBorg; oxygenation lowestSpO2 andPaO2/FiO2 days 1–3. Report dyspnea0–10VAS and oxygenationPaO2/FiO2; no Borg or lowestSpO2 outcome result appears in full supplied results.
- **Comparison logic:** Both dyspnea/oxygenation appear in abstract and retain secondary status; these are missing prespecified measurement analyses within retained key-secondary outcomes, not peripheral deleted early endpoints. Precision not applicable; no SpO2 values reconstructed from PaO2/FiO2 .
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route A, category5.
- **Affected result or extracted value:** Whether null dyspnea and improved oxygenation conclusions cover the prespecified Borg and lowestSpO2 measures.
- **Why context does not resolve it:** Category5 applies to planned key-secondary measure analyses absent from report; the two scales/oxygen measures are not synonymous.
- **Supported alternatives:** OnlyVAS andPaO2/FiO2 may have been analyzed/reported; Borg/SpO2 may exist elsewhere or have been dropped. The disclosed earlier endpoint revisions do not explain their continued presence in final plan.
- **Exact human question:** What are the prespecified Borg dyspnea and lowestSpO2 oxygenation results, or where was their removal from the final-plan key-secondary outcome analyses documented?

### F-XS-010

The initially prespecified intubated-mortality analysis receives post hoc status in the report.

- **Locations and roles:** PLAN [p.38, secondary objectives including post-intubation mortality](../../../joi180109supp1_prod.pdf#page=38), [p.45, lines 675–676](../../../joi180109supp1_prod.pdf#page=45), [p.47, line 699](../../../joi180109supp1_prod.pdf#page=47), [p.103, secondary list](../../../joi180109supp1_prod.pdf#page=103); REPORT [main p.4, secondary exploratory and intubated-subset post hoc methods](../../../jama_azoulay_2018_oi_180109.pdf#page=4), [p.6, Post Hoc Outcomes](../../../jama_azoulay_2018_oi_180109.pdf#page=6), [p.8, secondary exploratory statement](../../../jama_azoulay_2018_oi_180109.pdf#page=8). Keys S-P 2-003, S-P 2-010, P4-12, S010, S026.
- **Printed specifications/values:** Initial plan explicitly prespecifies intubated-patient day 28 mortality and labels mortality after HFNO versus control secondary. Report calls intubated-subset analyses post hoc, displaying55.3%/52.3%, RD 3(−8.5, 14.5), P .65. The final plan omits this endpoint from its seven named secondary outcomes.
- **Comparison logic:** Compare analysis/outcome status item by item. Intubated mortality occurs prospectively in initial plan despite report post hoc classification. This is status, not a numeric discrepancy; rounding not applicable. The separate multiplicity-related exploratory wording is excluded below because endpoints remain explicitly secondary in the report.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route A, category5.
- **Affected result or extracted value:** Prespecification/status of intubated mortality55.3% versus52.3%, RD 3(−8.5, 14.5), P .65.
- **Why context does not resolve it:** Category5 applies to outcome/analysis status changes. The report discloses different initial secondary endpoints and explains exploratory interpretation, but those disclosures do not supply the status correspondence for each analysis.
- **Supported alternatives:** Intubated mortality may have been removed before final plan and reintroduced post hoc. The report discloses earlier secondary endpoint revisions, but does not identify the status history of this matching analysis.
- **Exact human question:** Was the initially prespecified secondary intubated-mortality analysis removed before being reintroduced as the reported post hoc analysis, and where is that status change documented?

### F-XS-011

The final plan prohibits control-group HFNO while the report permits rescue HFNO for DNI patients.

- **Locations and roles:** PLAN [p.99, line 1621](../../../joi180109supp1_prod.pdf#page=99); REPORT [main p.3, control intervention](../../../jama_azoulay_2018_oi_180109.pdf#page=3), [p.5, Interventions](../../../jama_azoulay_2018_oi_180109.pdf#page=5). Keys P4-07, N006, N056.
- **Printed statements/values:** Final plan HFNO will not be used in control. Report HFNO could be used only for DNI patients after standard failure; 30(7.7%) controls switched, 14(46.7%) died.
- **Comparison logic:** Compare allowable randomized intervention strategy, not adherence alone. The report expressly authorizes a subgroup exception absent from final-plan rule. Counts are not divergent copies; rounding not applicable to prohibition versus allowance.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Treatment-policy interpretation of primary mortality and IMV under standard oxygen with authorized rescueHFNO.
- **Why context does not resolve it:** The report explains why rescue was used but does not reconcile permission with the categorical final-plan prohibition.
- **Supported alternatives:** An ethical rescue amendment or undocumented permitted exception may govern these patients; alternatively this was treatment crossover underITT rather than a prespecified allowance.
- **Exact human question:** Was DNI rescueHFNO a prespecified/amended control-strategy exception, and where is its authorization relative to the final-plan prohibition documented?

### F-XS-012

Patients at exactly9 L/min belong to different oxygen-flow strata in plan and report.

- **Locations and roles:** PLAN [p.99, line 1602](../../../joi180109supp1_prod.pdf#page=99); REPORT [main p.2, Randomization](../../../jama_azoulay_2018_oi_180109.pdf#page=2), [p.7, Figure 3A/B oxygen-flow rows](../../../jama_azoulay_2018_oi_180109.pdf#page=7). Keys P4-06, N004, S035, S036, S048, S049.
- **Printed specifications:** Final plan<9 versus≥9 L/min; report>9 versus≤9 L/min. Figure repeats≤9/>9 with populations 348/347 versus40/41.
- **Comparison logic:** Truth-table comparison at exactly9 yields plan high/report low; all other flow values agree. Exact threshold membership is a logical criterion rather than a rounded copy of an estimate; half-unit percentage arithmetic is inapplicable.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Prespecified allocation strata and primary/IMV oxygen-flow subgroup membership and interactionP.39/.65.
- **Why context does not resolve it:** Equality membership cannot be inferred consistently from two explicit opposing inequalities; 9 L/min is a feasible clinical setting.
- **Supported alternatives:** Report reflects actual randomization lists and final-plan inequality differs; alternatively subgroup analysis used a revised boundary. Counts at exactly9 are not supplied.
- **Exact human question:** Were patients receiving exactly9 L/min randomized/analyzed in the lower or higher oxygen-flow stratum, and which plan/report boundary governs Figure 3?

### F-XS-013

The ICU-time forest subgroups differ from the reported stratification groups that the methods say define the subgroups.

- **Locations and roles:** REPORT [main p.2, Randomization](../../../jama_azoulay_2018_oi_180109.pdf#page=2), [p.4, subgroup methods and Table 1 randomization timing](../../../jama_azoulay_2018_oi_180109.pdf#page=4), [p.5, three predefined subgroups claim](../../../jama_azoulay_2018_oi_180109.pdf#page=5), [p.7, Figure 3A/B ICU-time rows](../../../jama_azoulay_2018_oi_180109.pdf#page=7). PLAN [p.98, lines 1600–1601](../../../joi180109supp1_prod.pdf#page=98) and [p.99, line 1602](../../../joi180109supp1_prod.pdf#page=99) corroborate reported allocation boundary only. Keys N004, N031–N034, S009, S031, S032, S044, S045, P4-06.
- **Printed specifications/counts:** Randomization≤2 versus≥3 days; methods subgroup effects defined by stratification variables. Figure 0–1 versus≥2 days, 321/330 and67/58 patients. Table 1 days 0, 1, 2, ≥3:H244, 77, 47, 20; C251, 79, 38, 20.
- **Calculation:** Figure low subgroup321=244+77 and330=251+79; high67=47+20 and58=38+20. Reported allocation low would368=244+77+47 and368=251+79+38; high20/20. Integer counts are exact membership counts; the discrepancy in low-H population47/368=.1277 and low-C38/368=.1033 exceeds5% even if conventional half-unit intervals are allowed: recomputed three-input totals[366.5, 369.5], figure low-H[320.5, 321.5] and low-C[329.5, 330.5], gaps45 and36, relative discrepancies45/368=.1223 and36/368=.0978. Thus this is actual regrouping, not only a heading abbreviation.
- **Focus area:** A/C. **Proposed review domain:** report_internal_inconsistency. **Relationship type:** S_W. **All relationships:** S_W. The PLAN is corroboration, not a conflict location.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Population/time definition of ICU-time primary-mortality andIMV subgroup effects and interactionsP.15/.17.
- **Why context does not resolve it:** Table 1 supports the figure grouping, but the methods explicitly tie analyses to different stratification groups; no regrouping rule is given.
- **Supported alternatives:** Figure intentionally uses an analysis-specific0–1/≥2 boundary; methods may describe only variables and omit changed category thresholds. These alternatives require clarification of which subgroup analysis was prespecified.
- **Exact human question:** Why does Figure 3 use0–1/≥2 days rather than the≤2/≥3day randomization strata, and which grouping was prespecified for the reported interactions?

### F-XS-014

Two subgroup analyses described as predefined are not contained in the supplied prospective plans.

- **Locations and roles:** REPORT [main p.7, Figure 3 title and unknown-diagnosis/hematologic-malignancy rows inA/B](../../../jama_azoulay_2018_oi_180109.pdf#page=7); REPORT [main p.4, subgroup methods](../../../jama_azoulay_2018_oi_180109.pdf#page=4); PLAN [p.45, complete subgroup list](../../../joi180109supp1_prod.pdf#page=45), [p.53, interaction statement](../../../joi180109supp1_prod.pdf#page=53), [p.82, interaction strategy](../../../joi180109supp1_prod.pdf#page=82), [p.98, final stratification list start](../../../joi180109supp1_prod.pdf#page=98), [p.99, final list continuation](../../../joi180109supp1_prod.pdf#page=99), [p.104, subsets-defined-above statement](../../../joi180109supp1_prod.pdf#page=104). Keys S009, S039–S042, S052–S055, S-P 2-010, S-P 2-016, S308, P4-06, P4-15, P4-17.
- **Printed statements:** Figure 3 calls its mortality/IMV groups predefined and includes unknown diagnosisNo/Yes and hematologic malignancyNo/Yes; the latterIMV interactionP=.01 and effects1.61(1.16, 2.23)/.89(.65, 1.22). Initial complete subgroup list includes oxygenation, other organ failure, peri-intubation, postextubation, intubated andDNI. Final list specifiesICUtime, oxygenflow, shock; final analysis refers to subsets defined above. No plan text prespecifies diagnosis or hematologic-malignancy interactions.
- **Comparison logic:** Search/match complete supplied plan inventory and source-linked subgroup paragraphs; compare explicit predefinition claim to absence from all supplied prospective subgroup lists. A broad intention to analyze intubation predictors is not a prespecified named treatment interaction. Precision not applicable to prespecification status.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route A, category5.
- **Affected result or extracted value:** Prespecification of unknown-diagnosis and hematologic-malignancy mortality/IMV subgroups, especially hematologic-malignancyIMV interactionP=.01.
- **Why context does not resolve it:** Category5 applies to analyses described as prespecified without supplied plan support. Initial PaO2/FiO2 subgroup support was found and is not included in this omission pattern.
- **Supported alternatives:** A separate unsupplied dated subgroup plan may exist; alternatively the figure includes exploratory post hoc groups under a shared predefined title.
- **Exact human question:** Where were the unknown-diagnosis and hematologic-malignancy treatment-interaction analyses prespecified, or should their reported status differ from the predefined stratification analyses?

## Excluded observations

Only apparent issues decided against emission are listed. Reconciled checks remain in the matrix. One reason code per row; repeated structures are consolidated.

| Location | Observation | Reason code |
|---|---|---|
| REPORT main pp.1, 6 respiratory CI | Upper CI−.2 versus−.3: half-unit intervals[−.25, −.15] and[−.35, −.25] touch; gap 0, relative discrepancy0. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p.3; PLAN pp.91, 103 sample target | Report 779 total versus389 each/plan778: printed half-unit copy intervals[778.5, 779.5] and[777.5, 778.5] touch, gap 0. Exact allocation differs by1/778=.00129 even without rounding. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main pp.5, 6 mortality P | P .94 primary Cox-associated result versus explicitly log-rank P .85 figure is a different named test; not a reproduced same-test copy conflict. | NOT_REPRODUCED |
| REPORT main pp.1, 3, 5 allocation | Abstract 388 per randomized intervention group versus actual389 randomized/388 analyzed is immediately explained by the same abstract's778 randomized and776 completed and explicit consent withdrawals; no result extraction denominator remains ambiguous. | CONTEXT_RESOLVES |
| REPORT main p.4 baseline; REPORT supplement p.4 graphs | Medians 33/32, 136/128 versus graph approximate34/32.9, 143/126 do not establish copies of the same summary statistic; point/bar statistic is unspecified. | CONDITIONAL_OR_UNREPORTED |
| PLAN pp.6, 42–45 versus pp.98–100; REPORT main pp.2, 3 | Initial HIV-inclusive population, lower-dose/weaning criteria, NI design/sample inputs and endpoints versus revised final version: report explicitly discloses initial design/secondary changes; final matching rules govern reported trial. | CONTEXT_RESOLVES |
| PLAN pp.6, 7, 40–42, 53, 61 versus pp.97, 102–104; REPORT main p.3 | Initial admission-based versus randomization-based day 28 origin, NI lower-bound wording and no-interim versus scheduled safety interim are supplanted by explicit final randomization-based superiority/one-interim rules; no conflicting operative reported decision rule remains. | CONTEXT_RESOLVES |
| PLAN pp.50, 99 center-unit phrase; pp.52, 104 NIV hypothesis phrase; p.100 standard-oxygen sentence | Isolated center/NIV/standard-oxygen wording resolves from individual randomization, HFNO-versus oxygen objective and continuous-HFNO/temporary Venturi paragraph. No printed number or effect attribution depends on those phrases. | TERMINOLOGY_OR_WORDING |
| PLAN p.98 cancer-care criterion versus REPORT main p.2 chemotherapy criterion | Cancer-care versus chemotherapy descriptive wording with same 5-year window; no supplied quantitative evidence establishes a changed included population. Doubt about clinical wording is excluded. | TERMINOLOGY_OR_WORDING |
| PLAN p.103 secondary list; REPORT main pp.3, 4, 8 | Secondary analyses considered exploratory because of multiple testing is an inferential caution; the same report continues to label the endpoints secondary. It does not reproduce a change in endpoint status. | TERMINOLOGY_OR_WORDING |
| PLAN pp.53–54, 104; REPORT main p.3 | Conditional missing-outcome handling and predictor multiple imputation have no demonstrated triggered missingness or conflicting implemented imputation statement; article says no losses and no exclusions for missingness. | CONDITIONAL_OR_UNREPORTED |
| PLAN pp.1, 33–37, 70–81, 90–91, 97, 107; REPORT main pp.1, 2 | Site counts, recruitment calendars, cover no-amendment nomenclature, consent participation duration and administrative version metadata do not alter primary/key-secondary result, analysis-population size or operative decision rule. | PERIPHERAL_COMPARISON |
| PLAN pp.20–31, 93–95, 122–128; REPORT supplement pp.4–5 | Historical rationale copies/clipped historical results and per-time contributor/observation count comparisons are peripheral; no matched HIGH key-result or analysis-set size change established. | PERIPHERAL_COMPARISON |

## Limitations and completion

All 72 bounded relationship groups are complete. Supplied result figures do not define point/bar summary statistics or print exact plotted effects; geometric readings were not promoted to exact values. Raw event times and named covariate/PP-membership definitions are not supplied, so subgroup Cox models and unreported planned analyses cannot be independently reconstructed; findings identify the exact missing definition rather than assume one. The final historical table's clipped right edge limits historical-rationale transcription only. There is no scientific comparison coverage gap, structured-data omission, tooling gap, or source modification. Fourteen findings are prepared for independent inclusion screening; thirteen apparent observations are excluded once.
