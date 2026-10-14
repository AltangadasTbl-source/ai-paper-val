# Cross-source consistency review

Runtime UUID: 01a12bc4-2f48-7c51-9f05-5bc5a8635034. Role: cross_source_consistency_reviewer; model gpt-6.1-sol; reasoning effort medium; fresh mandatory spawn.

## Scope and evidence

Completed cross-source and matched-location review of all four supplied sources: DOC-001 REPORT pp.1–10, DOC-002 PLAN pp.1–40, DOC-003 PLAN pp.1–31, DOC-004 REPORT pp.1–34, using the complete current main and support quantitative maps, including the complete support results transcription appendix. No earlier conclusions, candidate lists, checker results, screening records, classifications or reports were scientific inputs. No external evidence was used. No structured data source was supplied. Full QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read.

Population, time origin, contrast, effect measure, model, analysis set and displayed precision were matched before comparison. Main-map N/S keys and support-map P-/R- keys below are source-local relationship locators, not new canonical IDs. Seven secondary outcomes appearing numerically in the abstract are key secondary outcomes for this review. Destination is also prespecified secondary, with descriptive rather than comparative analysis. Planned parent-trial analyses are distinguished from the separate PRO-SCAN substudy and from historical background evidence.

SAP p.6 explicitly supersedes the previously published protocol and registration. Consequently changed earlier provisions alone are not treated as undisclosed active-SAP deviations. The ventilation change is separately emitted under route A category 5 because the active SAP planned Cox analysis for a key secondary outcome and the results supplement explicitly substitutes a tobit analysis without reporting the planned estimate. Its disclosure is recorded rather than suppressed.

Exact-source visually checked pages relevant to findings: main pp.2, 4, 7; SAP pp.9, 14, 16, 18; results pp.4, 7, 18. Reusable renderings remained unchanged. Exact native text supported additional main/report locators; reusable OCR was a locator for plan text. Any subsequently registered issue requires the independent exact-source recheck.

### Fresh derivatives and engine provenance

All three fresh images use bundled helper pdf_tools.py with the package-local pinned interpreter, PyMuPDF1.26.4, CPU, 200dpi. No fresh OCR was performed; the requested GPU was not needed for these renderings.

| Relative derivative path | Exact source/page | Exact command |
|---|---|---|
| preprocessing/cross_source/main-p2.png | DOC-001 PDF p.2 | .ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py render jama_summers_2025_oi_250040_1753124024.36498.pdf --page 2 .ai_paper_validation/review_1_6_2/preprocessing/cross_source/main-p2.png |
| preprocessing/cross_source/main-p4.png | DOC-001 PDF p.4 | .ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py render jama_summers_2025_oi_250040_1753124024.36498.pdf --page 4 .ai_paper_validation/review_1_6_2/preprocessing/cross_source/main-p4.png |
| preprocessing/cross_source/results-p4.png | DOC-004 PDF p.4 | .ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py render joi250040supp3_prod_1753124024.38098.pdf --page 4 .ai_paper_validation/review_1_6_2/preprocessing/cross_source/results-p4.png |

Source transcription clarification: SAP p.14 line319 prints ≥60 patients per cluster-period, not260. This was read from unchanged reusable image `.ai_paper_validation/review_1_5_1/preprocessing/sap_images/page-014.png`. The initial P-033/support OCR transcription is a derivative substitution, and main ≥60 reconciles. No supplied-source discrepancy results from that derivative.

## Complete relationship comparison coverage

Every row is CROSS_SOURCE_COMPLETE. Matched copies, descriptive subgroups, method descriptions, footnotes and graphical displays were included in the stated scope; administrative/reference pages introduce no additional current-trial matched numeric relationship. Numeric within-display calculations are covered by the separate numeric reviewer, while relevant aggregates and matched cross-location values are expressly checked here.

| Relationship locators | Exact compared source locations and roles | Explicit comparison and result |
|---|---|---|
| N001, S001 | REPORT main pp.1, 2, 4, 5, 7 | Abstract/Key Points/narrative/Table 2: 3397, primary medians62/64, difference−1.97, 95% CI−7.24/3.30, P.46 agree. Male1070+1087=2157; 64% agrees with combined total. Overall age61(48–71) not reconstructed from subgroup quantiles. |
| N002, P-001, P-025, R-009, R-023 | REPORT main pp.1–3; REPORT results pp.9, 23; PLAN protocol pp.7, 11–13; PLAN SAP pp.4, 8 | Eight ICUs/four per sequence/four alternating3-month periods agree. Sequence1353+2044=3397 and treatment1681+1716=3397. Staggered start is distinct from treatment sequence. Phrase double crossover does not change explicit four-period diagram. |
| N003, P-007, R-003 | REPORT main pp.1, 2; REPORT results p.3; PLAN protocol p.13; PLAN SAP p.10 |100g/L vs63g/L agree; 1.26 vs1.25kcal/mL approximate isocaloric wording resolves .8% difference. Assigned concentration is distinct from patient-delivered g/kg/day. |
| N003, P-008, P-025 | REPORT main p.2; PLAN protocol p.14; PLAN SAP p.8 | Assigned formula retained across crossover/readmission while indicated, capped90days/ICU discharge/death. Short observed exposure87/84h is not a changed assigned duration. |
| N004, P-005, P-029, R-007 | REPORT main pp.2, 3; REPORT results p.7; PLAN protocol pp.11–12; PLAN SAP p.9 | Itemwise age≥16, first EN during index/later ICU stay, contraindication, prior participation agree; 12-hour equality boundary differs in main narrative: F-XS-005. |
| N005, N006, N007, N008, N009, P-026, R-009, R-010, R-018 | REPORT main pp.3, 4; REPORT results pp.9, 10, 18; PLAN SAP p.4 | Figure branch counts650+1031=1681 and703+1013=1716; 3411−14=3397; period480+298+551+352=1681 and335+530+368+483=1716. SAP3412 vsreport3411 pre-retention enrolments below display discrepancy threshold, excluded. |
| N010, P-003, P-030, R-008 | REPORT main pp.1, 3, 7; REPORT results p.8; PLAN protocol p.10; PLAN SAP pp.10–11 | Primary definition90 minus index-hospital/readmission days, death≤90assigned0; readmission midnight criterion; day90 and EN origin agree. No composite-component/status change in active SAP. |
| N012, S002, N030 | REPORT main pp.4, 7 |497/475 described alive with zero hospital-free days does not reconcile with all-patient means47.5/48.9 and survivors1221/1269 under0–90 support: F-XS-001. |
| N011, N024, P-036, R-013 | REPORT main pp.4, 5; REPORT results p.13; PLAN SAP p.15 | Feeding87(36–187)/84(34–182)h and696(408–951)/676(405–957)mL/d reconcile with more precise supplement87(36.4–187)/84(34–182.4), 696(408–950.8)/676.2(405–956.7); time19.0(9.2–37.7)/19.3(9.5–39.8)identical. |
| N013, N014, N015, N016, N017, N018, N019, N020, R-010, R-011, R-012 | REPORT main Table1p.5; REPORT results eTable 4pp.10–12 | Baseline period-to-arm copies are descriptive/peripheral; no primary outcome discrepancy registered from baseline copies. Period sex countsum1069vs1070 and551period total vs549sex sum below5% precision rule. Diagnosis APACHEII/IIIj label resolves field-specific category wording. Baseline category definitions and analysis total matching checked. |
| N021, S013, S014, P-042, R-011, R-028, R-029, R-030 | REPORT main pp.5, 8; REPORT results pp.11, 28–30; PLAN SAP p.19 | Ventilation1385/1355 and complements296/361 agree; all medians/IQRs, 2.7(−5.24, 10.64), −3.44(−9.64, 2.76)agree. Main interaction.02 vssupp.023 rounds; ICEMANverylow credibility agrees with narrative. |
| N022, R-011 | REPORT main p.5; REPORT results p.11 | Vasopressor period sums926/921 agree. Peripheral baseline copy comparison; not new outcome result. |
| N023, S015, S016, P-017, P-042, R-011, R-028, R-031, R-032 | REPORT main pp.4, 5, 8; REPORT results pp.11, 28, 31–32; PLAN protocol p.21; PLAN SAP p.19 | Baseline KRT122/119, complements1559/1597, median differences0(−4.32, 4.32)/−13.19(−50, 23.62), interaction<.001 agree. Timing before EN distinct from post-EN secondaryKRT. EFFORT-induced addition disclosed consistently; moderatecredibility matches. |
| N025, R-019 | REPORT main pp.5, 8; REPORT results p.19 | Exact urea day1 medians7.3/7.5 and day10 13.0/10.6 withIQRs agree; mean wording in discussion alone is readily resolved by explicit median reporting and does not identify a separate numeric mean. Excluded wording observation. |
| N026, R-020, R-021, P-013 | REPORT main p.5; REPORT results pp.4, 5, 20, 21; PLAN protocol pp.19–20 | AE3+1=4, SAE1+1=2 andperiod counts agree; AE windows48h after EN cessation, SAE90days, relatedness restrictions agree. AE/SAE displays may overlap; not mutually exclusive outcome categories. |
| N027, N028, P-036, R-013, R-023 | REPORT main p.6; REPORT results pp.13, 23; PLAN SAP p.15 | Days1–5, 10, 20, 30, protein/calorie units, all contributor counts andmedian/IQR plot definitions match. Protein higher/calories similar narrative agrees with supplement exact medians; unlabelled plots not assigned invented exact values. |
| R-014, R-015, R-024, R-025 | REPORT results pp.14, 15, 24, 25; REPORT main p.4 | IBW/ABW definitions and all-feeding versus excluding-enrolment-day analysis sets distinguished.103=49+54removed from1681/1716gives1632/1662. Contributor counts are per-observation populations, notITT sizes; weight missingness is not primary outcome missingness. |
| N029, S006, P-031, P-039, R-008, R-018 | REPORT main pp.1, 3, 5, 7; REPORT results pp.8, 18; PLAN SAP pp.11, 17 | Survivor endpoint only alive90; 72(57–80)/72(59–80), difference.01(−1.94, 1.96)P.995 agree across matched report locations. Planned quantile model agrees. Period medians cannot be averaged to obtain pooledmedian. |
| N030, S007, P-031, P-040, R-008, R-018 | REPORT main pp.1, 3, 5, 7; REPORT results pp.6, 8, 18; PLAN SAP pp.11, 17–18 |1221/1269 survivors reproduce period323+229+408+261 and258+383+270+358.72.6/74.0, RR.99(.95, 1.03)agree; GEElog/exchangeable/ICU/Fay–Graubard context matches planned model. SecondaryP.47 differs output principle: F-XS-004. |
| N031, S008, P-031, P-041, P-046, R-004, R-006, R-008, R-018 | REPORT main pp.1, 3, 5, 7; REPORT results pp.4, 6, 8, 18; PLAN SAP pp.12, 18, 28 | Key secondary ventilator effect6.8(−3.0, 16.5)h agrees among abstract/narrative/Table 2; active SAPCox liberation HR replaced by disclosedtobit mean difference: F-XS-003. Mean(SD)group label ambiguous: F-XS-002. Total hours include pre-EN and reintubation, not merely post-EN days. |
| N032, S009, P-031, P-041, R-008, R-018 | REPORT main pp.1, 3, 5, 7; REPORT results pp.6, 8, 18; PLAN SAP pp.12, 18 | HR.93(.88, 1.00), time-to-liveICUdischarge, competingdeath, cumulativeincidence median6.6/6.2 agree across main. Supplement period5.1/5.8, etc are ordinary descriptive medians, not pooled cumulativeincidence medians; no conflicting sameestimand reconstructed. P.04presentation: F-XS-004. |
| N033, S010, P-031, P-041, R-008, R-018 | REPORT main pp.1, 3, 5, 7; REPORT results pp.6, 8, 18; PLAN SAP pp.12, 18 | HR.96(.90, 1.02), time-to-livehospitaldischarge, cumulativeincidence median21.4/21.1agree across main. Supplement period raw medians not competingrisk pooled quantiles. Indexhospital stays vsreadmissions distinguished. P.15presentation: F-XS-004. |
| N034, S011, P-031, P-040, R-008, R-018 | REPORT main pp.1, 3, 5, 7; REPORT results pp.6, 8, 18; PLAN SAP pp.12, 17–18 | Tracheostomy134/121 equals period27+29+35+43/36+24+38+23; 8.0/7.1, RR1.15(.66, 2.01)agree. Planned GEE consistent with report. P.57presentation: F-XS-004. |
| N035, S012, P-031, P-040, R-008, R-018 | REPORT main pp.1, 3, 5, 7; REPORT results pp.6, 8, 18; PLAN SAP pp.12, 17–18 | Post-ENnewKRT122/127 equals33+22+38+29/26+35+33+33; 7.3/7.4, RR.97(.81, 1.16)agree; not compared to baseline122/119 as identical outcome. P.69presentation: F-XS-004. |
| N036, P-031, P-042, R-008, R-018 | REPORT main pp.1, 3, 7; REPORT results pp.8, 18; PLAN SAP pp.12, 13, 19 | Hospitaldestination seven main categories include378/380deaths; ICUdestination supplement categories have different time/location, not matched as same endpoint. Planned destination descriptive status agrees; no inferentialtest invented. |
| N037, R-018, R-022 | REPORT main pp.5, 7; REPORT results pp.18, 22 | Hospitalreadmission161/172=47+12+76+26/29+50+26+67; also1681−1520/1716−1544. TotalICU+hospitalreadmissions244/250andindexICUreadmission89/86are distinctdefinitions; no crosslabel substitution. |
| S001, S023, P-015, P-037, P-046, R-005 | REPORT main pp.4, 5, 7; REPORT results p.5; PLAN protocol pp.20–21; PLAN SAP pp.16, 28 | Mainq=.5, treatment/period/delayed start, ICUrandomnormal, blockbootstrap95%CI match.1000replications supply additional implementation detail; no unreported preferred method assumed. Difference in medians is adjusted and need not equal crude−2. |
| S002, S025, P-039, R-005 | REPORT main pp.4, 7; REPORT results p.5; PLAN SAP p.17 | Planned additional linear mixed analysis reported47.5(34.0)/48.9(33.5), adjusted−1.26(−3.59, 1.06). Same primary distribution used; meandifference not presumed crude−1.4. |
| S003, P-038, R-005, R-006, R-027 | REPORT main p.7; REPORT results pp.5, 6, 27; PLAN SAP pp.16, 28 | Bayesian−1.50(−3.86, .90)andquantile estimand match eFigure6; posteriorbenefit.109 distinct fromP.109. Priors defaults and separately described intercept do not establish a reproduced flat-versusStudent-t fixed-slope conflict. Groupmeanlabel: F-XS-002. |
| N038, S004, S005, P-006, P-043, P-046, R-005, R-012, R-016 | REPORT main pp.4, 7; REPORT results pp.5, 12, 16; PLAN protocol p.12; PLAN SAP pp.19, 29 | Active SAP known nontrial andpalliative/organ donation exclusions match report.234=144+90 and27=17+10; periodpalliative/donation totals17/10agree. Older transfer/>12hsensitivity wording superseded. Planned imputation not needed with completeprimary. |
| N039, S017, S018, P-042, R-028 | REPORT main p.8; REPORT results p.28; PLAN SAP p.19 | Agecutpoint70and allcounts/medians/IQR/differences agree: −3(−8.48, 2.49), .85(−8.98, 10.68); interaction.11/.106displayrounds. |
| N040, S019, S020, P-042, R-028 | REPORT main p.8; REPORT results p.28; PLAN SAP p.19 | BMIcutpoint35andcounts1066/1074, 222/206 agree; −3.46(−12.44, 5.53), 7.23(−3.56, 18.02)agree; interaction.47/.468rounds. MissingBMIparticipants not included in printedsubgroups. |
| S021, S022, P-014, P-033 | REPORT main pp.3, 4, 8; PLAN protocol p.20; PLAN SAP pp.13–14 | Original1-day80/90%andposttrial2-day>80%rationales distinguished; CV.5, baseICC.02 agree. SAP≥60confirmed visually, notOCR260. Protocolsix-clusterpreliminary wording superseded bySAPeight-cluster specification. BroaderSAPcorrelationrange andnarrowermainplausiblerange not necessarily conflicting parameter statements. |
| S024, P-034 | REPORT main pp.4, 7; PLAN SAP pp.14–15 | Two-sided95%and.05 align; secondaryCI-onlyprinciple versussevenprintedsecondaryPvalues: F-XS-004. No claimed primary multiplicity/interim adjustment or NI/equivalence margin exists. |
| S026, P-017, P-042, P-046, R-006, R-028, R-029, R-031 | REPORT main pp.4, 5, 8; REPORT results pp.6, 28–32; PLAN protocol p.21; PLAN SAP pp.19, 29 | Threeinitialsubgroups plusdisclosedrenaladdition align. Allfour likelihoodratio interactiontests match plannedmodel; within-stratumCI null andglobalinteractionP are differenthypotheses, notmatched as conflictingtest. |
| S027, P-004, P-031, R-008, R-019 | REPORT main pp.1, 3, 7; REPORT results pp.8, 19; PLAN protocol pp.10–11, 17; PLAN SAP pp.11–13 | ActiveSAPoutcome list/status matches report eightsecondarydefinitions; protocolhealtheconomics omitted under explicitSAPsupersession. Biochemistry tertiary inreport; collectiondays1/5/10versusprotocol1–5/10doesnot changeprimary/keysecondary analysis. |
| S028, P-012, P-013 | REPORT main pp.3, 4; REPORT results pp.4–5; PLAN protocol pp.18–20 | No efficacyinterim inplan/report agrees. Protocol3-monthlyDSMCreview vsreportsingle midwayreviewis safety-monitoringcadence; no numericalstatistical stoppingboundaryspecified or changeddecision demonstrated. Excludedperipheralobservation. |
| S031, P-044, R-005 | REPORT main pp.4, 9; REPORT results p.5; PLAN SAP pp.19–21 | Primaryfullyobserved⇒worst/bestimputationand>5%MItrigger inactive; completecasesecondary specified and reported. Missingweight/BMI counts not primary outcome missingness. No planned primary/keysecondary analysis omitted exceptventilation replacement. |
| P-035, N003 | PLAN SAP pp.8, 15; REPORT main pp.2, 4 | SAPindexICUadmissionassignment andreportoriginalallocation retention considered with ENenrolment procedure; no source prints patientreassignments or opposing fittedanalysissets. A crossover-between-admission-andEN discrepancy would depend on unreported participant timing; excludedconditionalobservation. |
| P-010, P-011, P-032, P-045 | PLAN protocol pp.16–18, 30; PLAN SAP pp.13, 21; REPORT main pp.2, 4; REPORT results p.3 | ActiveSAP day1ENcommencement matchesreportnutritionpartialcalendar-daydefinition. OlderprotocolICU day1/calendar wording not used to redefine active primaryendpoint. Recruitmentcalendar, site/pointer variations peripheral. |
| P-020, P-021, P-022, P-023, P-024 | PLAN protocol pp.35–40; REPORT main pp.1–10; REPORT results pp.1–34 | PRO-SCAN separateco-primaryCTCSA/lowCSA/day90response aims; baseline72hbeforeICU/48hafterEN, followup≥5d, thresholds170/110cm², >7dexposure, exploratorymodels andCTforecasts checkeditemwise. No PRO-SCAN results or claims supplied inparentreport, so its standaloneanalyses not treated as unreported parentprimary/keysecondaryresults. |
| P-002, P-009, P-018, P-019, P-028, R-033, R-034 | PLAN background/admin/referencepages; REPORT main p.10/results pp.33–34 | Priortrials, recommendations, bibliographiccounts, consentworkload andtimelineforecasts inspected; not matched tocurrent trialresults. No additional suppliedstructureddata/relevantnumericcomparison remains. |

## Findings

### F-XS-001 — Zero-outcome counts are described as living patients despite incompatible all-patient means

**Locations and roles:** REPORT [main p.4, Primary Outcome paragraph](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=4), REPORT [main p.7 Table 2, linear primary summaries and alive-day90 row](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7). REPORT [main p.3 endpoint death-zero rule](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=3) and REPORT [results p.8 eTable 2](../../../joi250040supp3_prod_1753124024.38098.pdf#page=8) supply endpoint support0–90.

**Printed statements:**497(29.6%) augmented and475(27.7%)usual “had zero days free of the index hospital and were alive at day90.” Table 2 prints all-patient means47.5(34.0) and48.9(33.5), and alive90counts1221/1681 and1269/1716.

**Comparison logic/calculation:** If497 and475 are living zero-day patients, no more than1221−497=724 and1269−475=794 patients can have a positive outcome. With all outcomes≤90 and deaths assigned0, mean≤724×90/1681=38.76 and794×90/1716=41.64days, respectively, rather than47.5/48.9. Allowing each displayed count a half-unit interval, most permissive bounds are90×725/1680.5=38.82773 and90×795/1715.5=41.70796. Printed mean intervals[47.45, 47.55] and[48.85, 48.95] remain separated by≥8.62227 and7.14204days; relative discrepancies against47.5/48.9 are≥.18152/.14605, above.05. Count/percentage pairs themselves round consistently; the conflict is outcome-population attribution.

**Focus area:** A, C. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W. **Qualifying route:** Route B.

**Affected result or extracted value:** Number/proportion of day90 survivors with zero hospital-free days and distribution/mean of the primary composite outcome.

**Why context does not resolve it:** The narrative explicitly restricts the counts to patients alive90; reading that restriction literally is mathematically incompatible with separately printed all-patient means. This is more than alternative names for the endpoint: it changes which individuals a numerical count includes.

**Supported alternatives/missing definition:**497/475 may instead count all zero-valued composite outcomes including deaths; that alternative is compatible with the outcome definition but is not established as the printed living-patient count. No corrected count is assigned.

**Human question:** Do497/475 include participants who died before90, and what counts should be extracted for alive90 patients with zero hospital-free days?

### F-XS-002 — Mean/SD labels do not identify the quantities represented by primary Bayesian and ventilation group summaries

**Locations and roles:** REPORT [main p.7 Table 2 Bayesian row, linear row, primary quantile row, ventilation row](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7); REPORT [main p.4 primary medians](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=4); REPORT [results p.18 eTable 10 ventilation and descriptive median/IQR footnote](../../../joi250040supp3_prod_1753124024.38098.pdf#page=18).

**Printed statements/values:** Bayesian quantile row is labeled mean (SD) and prints62.0(0to77), 64.0(0to77), identical to primary median (IQR)row. The same endpoint/all ITT linear row explicitly prints mean (SD)47.5(34.0), 48.9(33.5). Ventilation row is labeled mean (SD), h and prints84.0(35.0to178.9), 78.0(33.2to161.0), a pair of parenthetic limits rather than one SD. Supplement period-stratified ventilation summaries are explicitly median (IQR).

**Comparison logic/calculation:** Different outcome models may change treatment estimates, but do not change an unqualified descriptive sample mean for the same complete population. Under printed mean labels, the Bayesian62.0 versuslinear47.5half-unit intervals[61.95, 62.05]/[47.45, 47.55] have gap14.40, relative.30316; 64.0vs48.9intervals[63.95, 64.05]/[48.85, 48.95] have gap15.00, relative.30675. The first pair exactly matches printed medians, while the ventilation parenthetic ranges do not state a single dispersion quantity. No numerical mean or SD is reconstructed from subgroup medians.

**Focus area:** C. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W. All relationships: S_W. The supplement corroborates the median/IQR interpretation without providing an exact pooled duplicate; it does not add a separate relationship. **Qualifying route:** Route B.

**Affected result or extracted value:** Group means/SDs versus medians/quartiles for primary and ventilation outcomes; these quantities support different evidence extraction.

**Why context does not resolve it:** The table offers numerically different values explicitly called means for the identical primary endpoint/population, and does not specify what the two ventilation parentheses represent. A suspected labeling explanation does not establish what group summaries a data extractor should enter.

**Supported alternatives/missing definition:** The Bayesian descriptive cells may repeat sample medians/IQRs while the posterior treatment coefficient is a separate model summary. Ventilation descriptive cells may be median/IQR despite the tobit mean treatment contrast. These possibilities are not assigned as corrections; the repeated pattern is consolidated into one finding.

**Human question:** Which descriptive statistic and dispersion/quantile definition applies to each of the Bayesian-primary and ventilation group cells?

### F-XS-003 — Planned key-secondary ventilation Cox analysis is replaced by a tobit mean contrast

**Locations and roles:** PLAN [SAP p.18 lines416–431](../../../joi250040supp2_prod_1753124024.37799.pdf#page=18), PLAN [SAP p.28 Table1](../../../joi250040supp2_prod_1753124024.37799.pdf#page=28); REPORT [results p.4 Duration of invasive ventilation](../../../joi250040supp3_prod_1753124024.38098.pdf#page=4), REPORT [results p.6 observed-outcome margins method](../../../joi250040supp3_prod_1753124024.38098.pdf#page=6), REPORT [main p.1 abstract ventilation effect](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=1), REPORT [main p.7 Table 2](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7). PLAN protocolp.21corroboratesSAPCoxspecification; REPORT mainp.4states all analyses accordance with SAP.

**Printed statements/values:** SAP specifies time to liberation from invasive ventilation, Cox adjustedperiod/delayed start, ICUstratification/robustSE, cause-specificHR, deaths censored, 48-hourpalliativeextubationrule. Results explicitly says duration considered lower-bounded continuous“rather than as a time-to-event outcome as stated in the published statistical analysis plan”; tobit mixed model and observed-outcome margins produce mean difference6.8(95% CI−3.0to16.5)h, P.17. No planned ventilation cause-specificHR is reported anywhere in the supplied report.

**Comparison logic:** Same key-secondary outcome is reported with different estimand/model/death handling than active SAP; planned cause-specificHR is absent. Cox HR and tobit mean difference are distinct quantities, not rounded versions. Numerical display-precision comparison is not applicable to this categorical model/estimand substitution.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R. **Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Key-secondary invasive-ventilation effect6.8h and its relationship to the prespecified cause-specificHR/competingdeath analysis.

**Why context does not resolve it:** Route A category5requires registration of the unreported/replaced planned key-secondary analysis even when the change is disclosed. The supplement disclosure is retained as a supported explanation and does not make the two analyses identical.

**Supported alternatives/missing definition:** Authors may have intentionally revised this analysis after SAP; the results supplement establishes disclosure but supplies no ventilationHR from the planned model. No preference for either analysis is expressed.

**Human question:** Was the SAP ventilation analysis formally replaced, and is its planned cause-specificHR available or intentionally unreported?

### F-XS-004 — Seven secondary-outcome P values are presented despite the SAP CI-only principle

**Locations and roles:** PLAN [SAP p.14 lines330–333](../../../joi250040supp2_prod_1753124024.37799.pdf#page=14); REPORT [main p.7 Table 2 seven inferential secondary rows](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7); REPORT [main p.4 statistical threshold and SAP-concordance statement](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=4); REPORT [main p.5 secondary-results narrative](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=5).

**Printed statements/values:** SAP says secondary outcomes will have effect sizes and two-sided95%CIs“only, ”because trial not powered for secondary outcomes and no planned multiplicity adjustment. Table 2 prints P.995survivordays, .47alive90, .17ventilation, .04ICUduration, .15hospitalduration, .57tracheostomy, .69newKRT. Main gives two-sidedP<.05significance threshold and says all analyses accordance with SAP.

**Comparison logic:** Active SAP explicitly limits secondary inference presentation to estimates/intervals; report adds hypothesis-test P values for allseven matched secondary outcomes, includingICUduration.04. Primary-outcome secondary analyses and subgroup interaction P values are not part of this pattern because SAP separately permits them. Numerical rounding is not applicable to the planned presentation rule.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R. **Qualifying route:** Route B.

**Affected result or extracted value:** Interpretation of seven secondary tests, particularlyICUdischargeHR.93(.88, 1.00), P.04, in relation to aCI-only, no-multiplicity-adjustment prespecified inference principle.

**Why context does not resolve it:** The active plan says“only”and explains its statistical rationale; the report applies a general.05threshold and supplies tests without stating whether the secondary rule was amended. The reader cannot determine from immediate context whether secondary P values are intended for that threshold or only descriptive perspective.

**Supported alternatives/missing definition:** The P values may be supplementary/exploratory presentation intended without confirmatory interpretation; an amendment may permit them. Neither is expressly linked to the SAP CI-only restriction in supplied report text.

**Human question:** Was the secondary CI-only presentation rule amended, and what inferential status applies to the seven secondary P values?

### F-XS-005 — The nontrial-feeding exclusion boundary is inclusive in narrative and strict in the active plan

**Locations and roles:** REPORT [main p.2 eligibility paragraph](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=2), REPORT [main p.3 Figure 1 exclusion labels](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=3), REPORT [results p.7 eTable 1 criterion2](../../../joi250040supp3_prod_1753124024.38098.pdf#page=7); PLAN [SAP p.9 criterion2](../../../joi250040supp2_prod_1753124024.37799.pdf#page=9), PLAN [protocol p.12 eligibility table](../../../joi250040supp1_prod_1753124024.37199.pdf#page=12).

**Printed statements:** Main narrative excludes“12 or more hours”of nontrialEN, i.e.≥12h. Main flowchart labels>12h; active SAP andreport eTable 1say“greater than12hours, ”i.e.>12h. Earlierprotocolcriterionagrees with strictboundary.

**Comparison logic:** Itemwise criteria compare the same pre-enrolment nontrial nutrition duration and analysis-population selection. At exactly12h the inclusive rule excludes and the strict rule permits, so the criterion sets differ. This is an inequality-domain difference, not a difference in rounded printed measured values; half-unit discrepancy intervals are not applicable to the logical boundary.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R; all relationships: P_R, S_C, S_W. **Qualifying route:** Route B.

**Affected result or extracted value:** Eligibility/analysis-population definition underlying3397primary analysis participants and pre-enrolment nontrial-feeding exclusions.

**Why context does not resolve it:** The explicit inclusive and strict criteria assign opposite eligibility at the boundary; the supplied report does not state which rule was implemented. The discrepancy changes a defined selection rule rather than simply renaming the population. No actual participant count at exactly12h is alleged.

**Supported alternatives/missing definition:** Narrative may use a less precise paraphrase of the fully enumerated criteria; alternatively an inclusive implemented rule may differ from the table/SAP. No event-level durations establish which was applied. Boundary applicability is a limitation to interpreting magnitude, not to reproducing the printed criterion difference.

**Human question:** Was exactly12h nontrialEN eligible or excluded, and which criterion defines the reported primary population?

## Excluded observations

One code is assigned to each apparent issue; routine reconciled checks remain in the coverage table. No excluded row belongs to a reproduced routeAalways-registercategory.

| Location | Observation | Reason code |
|---|---|---|
| PLAN SAP p.14line319 vsREPORT mainp.4 | ReusableOCR260suggested power-inputdifference; exact imageprints≥60andmain≥60agrees. | NOT_REPRODUCED |
| PLAN SAP p.4 vsREPORT mainp.4 |3412versus3411enrolled; halfunitintervalgap0(includingtouchat3411.5), relative0; different linkage-stage context also possible. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT mainp.8 vsREPORT resultsp.28–29 | InteractionP.02/.023, .11/.106, .47/.468; printed halfunitintervalsoverlap ineachpair. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT mainp.4 vsREPORT resultsp.13 | Roundedfeedingduration/volume differ from supplement precision; allhalfunitintervalsoverlap. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT mainTable1p.5 vsREPORT resultseTable4pp.10–12 | Baselinecopies/sexperiodsum1069versus1070 andAPACHEII/IIIcategorylabels do not establishprimary/keysecondarymatchedresultdifference; countgaprelativebelow.05. | PERIPHERAL_COMPARISON |
| REPORT mainp.8 vsREPORT resultsp.19 | Discussionmeanurea wording vsnumericalmedian/IQR; immediate numericdisplay identifies summarystatistic, withno second conflictingprinted mean. | TERMINOLOGY_OR_WORDING |
| PLAN SAP p.16 vsREPORT resultsp.6 | Flatfixedregressioncoefficientprior versusseparateStudent-tinterceptdescription; defaultpriorsandseparateparameterlabels do not reproduce a supplied-source slopepriorconflict. | NOT_REPRODUCED |
| PLAN protocolp.20 vsPLAN SAPpp.6, 13–14 | Earlier six-cluster calculation versusSAPeight; active SAPexplicitly supersedesearlier analysis plan andmatchesreported originaleightclusters. | CONTEXT_RESOLVES |
| PLAN protocolpp.10–11 vsPLAN SAPpp.6, 11–13/REPORT outcome lists | Earlierhealtheconomicsecondary outcome absent in laterSAP/report; explicitSAPsupersession establishes a disclosed replacement of activeoutcomelist. | CONTEXT_RESOLVES |
| PLAN protocolp.12 vsPLAN SAP p.19/REPORT mainp.7 | Oldertransfer/>12h sensitivity vsactiveknown nontrialexclusionandpalliative/organ-donation sensitivity; explicitSAPsupersession resolves activeanalysislist. | CONTEXT_RESOLVES |
| PLAN protocolp.18 vsREPORT mainp.3 | Three-monthlyDSMC safety-review cadence vsone reviewaftertwoperiods; no numericalefficacy/harmstoppingrulecontradiction or alteredprimarydecision demonstrated. | PERIPHERAL_COMPARISON |
| PLAN SAPpp.8, 15 vsREPORT mainp.2 | Admission-periodvsENenrolmentassignment would changeanalysis only ifparticipant timing crossedperiodbeforefirstEN; no opposingimplementedpatientassignment orprimarycount supplied. | CONDITIONAL_OR_UNREPORTED |
| PLAN protocolpp.17–18 vsREPORT resultsp.5 | Biochemicalcollection1–5/10vs1/5/10andday-originphrasing doesnot changeprimary/keysecondarydefinition; tertiarybiochemistry collectiondetail. | PERIPHERAL_COMPARISON |
| PLAN protocolp.30 vsPLAN SAP p.21/REPORT mainp.4 | Recruitmenttimelineforecast/calendar differences administrative; notprimaryendpoint timewindow ordecisionrule. | PERIPHERAL_COMPARISON |
| REPORT mainp.7footnotef vsREPORT resultsp.27 | Bayesianfigurepointer namesSupplement1ratherthanresultsSupplement3; exact numericalfigure/Table 2agree. | PERIPHERAL_COMPARISON |
| REPORT mainp.7 vsREPORT resultsp.18 | PooledICU/hospitalcompetingriskquantiles versusperioddescriptivemedians; differentestimands/aggregation, notmatchingcopies. | NOT_REPRODUCED |
| REPORT mainp.7 vsREPORT resultsp.22 | Hospitalreadmission161/172versustotalICU+hospital244/250; differentoutcomedefinitions explicitsource labels. | NOT_REPRODUCED |

## Completion and limitations

Five findings; 17 excluded observations; explicit complete coverage rows. All 115 source pages represented by complete current maps, and all applicable matched-result and active-plan relationships checked without sampling. No source, reused asset or other agent artifact changed. New derivatives are limited to three CPU source-page renders as recorded. Reusable engine versions unknown; graphical box and histogram heights lack exact printed values; no raw participant data supplied; eligibility boundary implementation and prior parameterization require human clarification if retained. These are evidence or interpretation limits, not scientific source-coverage gaps. Every finding remains a proposed reporting issue for independent screening and subsequent human adjudication; no C IDs or AI dispositions assigned.
