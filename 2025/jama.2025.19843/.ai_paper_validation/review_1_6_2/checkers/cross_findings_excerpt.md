# Complete current cross-source finding and excluded-observation excerpt

## Findings


### F-XS-001

**Observation:** The primary analysis covariate description does not reconcile with the primary-result footnote.

**Exact locations and roles:** REPORT [main p.2, Randomization](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=2) identifies center and primary cardiogenic-shock etiology as minimization factors. REPORT [main p.3, Statistical Analysis](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=3) states that the primary analysis was adjusted on “minimization stratification factors.” REPORT [main p.6, Table 2 footnote d](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=6) describes Fine–Gray adjustment for cardiogenic-shock etiology. PLAN [SAP p.6, Analysis](../../../joi250087supp2_prod_1766516490.96511.pdf#page=6) also names etiology alone and corroborates the latter description; it is not itself a conflicting specification.

**Printed values/statements:** Primary successful-weaning sHR 1.02 (95% CI 0.74–1.39), P=.92. The report gives both an adjustment description referring to the minimization factors (center and etiology) and a specific footnote naming etiology.

**Comparison logic:** A reader taking the p.3 description together with the defined minimization factors reads a center-and-etiology model; the footnote explicitly names only etiology. Neither location explains whether center was included or whether the general phrase was intended to mean etiology alone. This is a model-specification comparison, not a numerical rounding comparison; no recomputed numeric interval or relative discrepancy applies.

**Focus area:** C. **Proposed review domain:** statistical_results. **Proposed primary relationship:** S_W. **All relationships:** S_W.

**Qualifying route:** Route B.

**Affected result or extracted value:** The adjusted primary sHR 1.02 (0.74–1.39), and the covariate set accompanying its extraction.

**Why context does not resolve it:** The report defines two minimization factors, while the exact result footnote names one. The supplied text does not say that center is implicit in that footnote or identify which covariate set produced the displayed sHR.

**Supported alternatives and missing definition:** The fitted model may include etiology alone, as the SAP and footnote state; it may include center as well, as the general report wording suggests. The fitted primary model formula is missing from these conflicting descriptions. The plan corroboration does not turn this report-internal finding into P_R.

**Exact human question:** Did the Fine–Gray model producing sHR 1.02 (95% CI 0.74–1.39) adjust for cardiogenic-shock etiology alone or for both etiology and center, and which report description specifies that fitted model?

### F-XS-002

**Observation:** Dialysis is included in some MACE definitions and absent from others.

**Exact locations and roles:** PLAN protocol [p.8](../../../joi250087supp1_prod_1766516490.96011.pdf#page=8), [p.14](../../../joi250087supp1_prod_1766516490.96011.pdf#page=14), [p.15](../../../joi250087supp1_prod_1766516490.96011.pdf#page=15), [p.53](../../../joi250087supp1_prod_1766516490.96011.pdf#page=53), [p.59](../../../joi250087supp1_prod_1766516490.96011.pdf#page=59), [p.60](../../../joi250087supp1_prod_1766516490.96011.pdf#page=60), [p.99](../../../joi250087supp1_prod_1766516490.96011.pdf#page=99), [p.105](../../../joi250087supp1_prod_1766516490.96011.pdf#page=105), and [p.106](../../../joi250087supp1_prod_1766516490.96011.pdf#page=106) list death, cardiac transplant, permanent LVAD escalation, stroke, dialysis, and heart-failure rehospitalization. REPORT [main p.3, Outcomes](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=3) likewise includes dialysis. PLAN [SAP p.4, Secondary endpoints](../../../joi250087supp2_prod_1766516490.96511.pdf#page=4) and [p.7, MACE analysis](../../../joi250087supp2_prod_1766516490.96511.pdf#page=7) list the other five components without dialysis. REPORT [supplement p.1, eFigure 4 contents title](../../../joi250087supp3_prod_1766516490.97011.pdf#page=1) and [p.13, eFigure 4 title](../../../joi250087supp3_prod_1766516490.97011.pdf#page=13) also specify the five-component composite. REPORT [eTable 3 p.5](../../../joi250087supp3_prod_1766516490.97011.pdf#page=5) and [p.6](../../../joi250087supp3_prod_1766516490.97011.pdf#page=6) place dialysis among the displayed component rows.

**Printed values/statements:** Day-30 MACE 35/101 (34.7%) versus36/104 (34.6%), RD0.0 (−12.6 to13.6), RR1.00 (0.69–1.46). Day-60 MACE36/101 (35.6%) versus39/104 (37.5%), RD−1.9 (−15.4 to11.7), RR0.95 (0.66–1.36). Dialysis by day30 is29/101 versus38/104; day60 dialysis entries are dashes. eFigure4 repeats MACE counts35/36 and36/39, with log-rank P=.87/.94.

**Comparison logic:** Item-by-item comparison reconciles death, transplant, LVAD, stroke and rehospitalization, and does not reconcile dialysis inclusion. Thus the same printed MACE counts have two possible composite definitions. Component counts cannot reconstruct the union because participant overlap is not supplied. This is an explicit endpoint-component comparison; numeric half-unit intervals and relative discrepancy are not applicable.

**Focus area:** D, with report attribution implications. **Proposed review domain:** protocol_report. **Proposed primary relationship:** P_R. **All relationships:** P_R, P_P, S_C.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** The D30/D60 MACE risks, risk differences, RRs and time-to-first-MACE curves.

**Why context does not resolve it:** Route A category5 applies to a prespecified composite definition change. The protocol and main narrative specify dialysis, while the SAP and figure specify its absence. Separate dialysis rows do not identify whether dialysis entered the composite union.

**Supported alternatives and missing definition:** The reported union may be the final-SAP five-component endpoint; the main definition and component rows may describe the original six-component endpoint; or different MACE displays may use different unions. No disclosed dialysis-component amendment or participant-level event flags are supplied.

**Exact human question:** Did dialysis contribute to the MACE counts and curves at D30 and D60, and which of the supplied five- or six-component definitions applies to each reported MACE result?

### F-XS-003

**Observation:** The organ-failure-free-day threshold differs between the SAP and report.

**Exact locations and roles:** PLAN [SAP p.4, Organ Failure](../../../joi250087supp2_prod_1766516490.96511.pdf#page=4), and [p.7, Organ Failure analysis](../../../joi250087supp2_prod_1766516490.96511.pdf#page=7): organ failure is SOFA score >2 in at least one of six organ systems. REPORT [main p.3, predefined secondary outcomes](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=3): days alive without organ failure use SOFA score0–1 for each component. REPORT [supplement p.5, eTable3 first two rows](../../../joi250087supp3_prod_1766516490.97011.pdf#page=5) provides organ-failure-free days and days with organ failure; [p.12, eFigure3](../../../joi250087supp3_prod_1766516490.97011.pdf#page=12) displays component-score categories0,1,2,3–4.

**Printed values/statements:** D30 organ-failure-free days12 (IQR0–21) versus14 (0–23), median difference−2 (95% CI−10 to4); days with organ failure9 (6–17) versus12 (6–18), difference−3 (−5 to2). SAP uses >2 in at least one component; report uses0–1 in every component.

**Comparison logic:** For a living patient with a component score exactly2 and all other components≤2, the SAP failure definition is false; the report criterion for being free of failure is also false. These definitions assign that day differently. SOFA component scores are integer thresholds, not rounded estimates. Numeric rounding intervals and relative discrepancy do not apply to this classification-rule comparison.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed primary relationship:** P_R. **All relationships:** P_R.

**Qualifying route:** Route B.

**Affected result or extracted value:** The eTable3 organ-failure-free-day medians12/14 and organ-failure-duration medians9/12, and the corresponding between-arm differences.

**Why context does not resolve it:** The SAP twice prints >2 and the report specifically prints0–1; score2 is separately represented in eFigure3. The field terminology alone does not tell a reader which threshold was used in the outcome calculation.

**Supported alternatives and missing definition:** The calculation may use failure≥2 (free0–1), or failure>2 (free0–2). The event-day classification used for the displayed durations is not specified consistently.

**Exact human question:** Were organ-failure-free days computed using all six SOFA components≤1 or≤2, and which threshold generated the organ-failure duration and free-day results in eTable3?

### F-XS-004

**Observation:** The supplied planned LV-function comparison is a hierarchical death/transplant/LVEF composite, while the reported comparison is a median LVEF analysis with pre-death measurements.

**Exact locations and roles:** PLAN [SAP p.8, Left Ventricular Function](../../../joi250087supp2_prod_1766516490.96511.pdf#page=8); REPORT [main p.3, predefined secondary outcomes](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=3); REPORT [supplement p.5, eTable3 LVEF row](../../../joi250087supp3_prod_1766516490.97011.pdf#page=5), and [p.6, footnotes a/b](../../../joi250087supp3_prod_1766516490.97011.pdf#page=6). No other supplied REPORT page contains a Global Net Benefit estimate or its interval.

**Printed values/statements:** The SAP specifies Global Net Benefit at day30, comparing every experimental patient with every control patient in the order: (1)death; (2)heart transplantation; (3)LV improvement defined as LVEF>30%, with wins/losses/ties and bootstrap95% CI. The report gives LVEF45 (IQR30–50), n=100, versus40 (25–50), median difference5 (95% CI−0 to10). Its footnote uses the day30 LVEF for living patients and the last available pre-death LVEF for patients dying before day30.

**Comparison logic:** A median difference of5 LVEF percentage points is not a net-benefit estimate from the planned three-level ordering. Replacing the death-first ranking with a measured LVEF before death changes the planned composite and death handling. All three hierarchy levels were compared item by item. This is an endpoint/analysis-definition comparison, not a numeric calculation; no rounding interval or relative discrepancy applies.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed primary relationship:** P_R. **All relationships:** P_R.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** The reported median LVEF difference5 (−0 to10), and the planned day30 death/transplant/LVEF hierarchical treatment comparison.

**Why context does not resolve it:** Route A category5 applies to the composite definition change. The supplied report explicitly gives another quantity and handling of deceased patients without reporting the planned net-benefit result or disclosing an amendment to that hierarchy.

**Supported alternatives and missing definition:** The median-LVEF comparison may be an additional descriptive analysis while the planned hierarchy was computed but not supplied; or it may replace the hierarchical endpoint. No net-benefit estimate, win/loss/tie counts or revision statement is present.

**Exact human question:** Was the SAP day30 Global Net Benefit analysis of death, transplantation and LVEF performed, and how does the reported median LVEF comparison with pre-death measurements relate to that prespecified hierarchical outcome?

### F-XS-005

**Observation:** Planned day60 ECMO-free and ventilation-free outcomes lack matching reported results.

**Exact locations and roles:** PLAN protocol [p.8](../../../joi250087supp1_prod_1766516490.96011.pdf#page=8), [p.14](../../../joi250087supp1_prod_1766516490.96011.pdf#page=14), [p.15](../../../joi250087supp1_prod_1766516490.96011.pdf#page=15), [p.53](../../../joi250087supp1_prod_1766516490.96011.pdf#page=53), [p.59](../../../joi250087supp1_prod_1766516490.96011.pdf#page=59), [p.60](../../../joi250087supp1_prod_1766516490.96011.pdf#page=60), [p.99](../../../joi250087supp1_prod_1766516490.96011.pdf#page=99), [p.105](../../../joi250087supp1_prod_1766516490.96011.pdf#page=105), [p.106](../../../joi250087supp1_prod_1766516490.96011.pdf#page=106); PLAN [SAP p.4, secondary endpoints](../../../joi250087supp2_prod_1766516490.96511.pdf#page=4), [p.7, ECMO analysis](../../../joi250087supp2_prod_1766516490.96511.pdf#page=7), [p.8, mechanical ventilation analysis](../../../joi250087supp2_prod_1766516490.96511.pdf#page=8). REPORT [main p.1, Main Outcomes and Measures](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=1) identifies ECMO- and ventilation-free days as secondary outcomes; [p.3, Outcomes](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=3) expressly calls the day30/day60 windows predefined. REPORT [main p.6, Table2](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=6) and [supplement p.5, eTable3](../../../joi250087supp3_prod_1766516490.97011.pdf#page=5) give day30 free-day outcomes. All supplied REPORT pages were searched through the complete maps; no day60 free-day result appears.

**Printed values/statements:** Day30 ECMO-free days24 (IQR0–26) versus23 (12–26), difference1 (95% CI−1 to4). Day30 ventilation-free days6 (3–11) versus6 (3–13), difference−0 (−3 to2). Both plan documents specify corresponding day60 windows. The report's mortality and stay outcomes at day60 are different quantities and cannot supply free days.

**Comparison logic:** Match the outcome, window and analysis set. The reported day30 distributions do not represent the planned day60 distributions. Both outcomes occur in the abstract and therefore meet the scope definition of key secondary. The observation is based on explicit planned windows and complete supplied-result coverage, rather than a general preference for additional outputs. No numerical rounding comparison is applicable.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed primary relationship:** P_R. **All relationships:** P_R.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** The planned day60 ECMO-free and ventilation-free outcomes; the supplied extractable free-day results cover day30 only.

**Why context does not resolve it:** Route A category5 covers planned key secondary analyses not reported. The report confirms the planned day60 windows and supplies no result or disclosed removal for either day60 free-day outcome.

**Supported alternatives and missing definition:** The day60 outcomes may have been computed but omitted from supplied results, or their windows may have been revised. Complete day60 summary/contrast outputs or an outcome-specific revision statement are absent.

**Exact human question:** Where are the prespecified day60 ECMO-free and ventilation-free results, or what disclosed change accounts for reporting only day30 free-day outcomes?

### F-XS-006

**Observation:** The supplied adjusted secondary and recurrent-event analyses lack matching reported model outputs.

**Exact locations and roles:** PLAN [SAP p.7, secondary analyses](../../../joi250087supp2_prod_1766516490.96511.pdf#page=7), [p.8, support and safety analyses](../../../joi250087supp2_prod_1766516490.96511.pdf#page=8), [p.9, AE/SAE analyses](../../../joi250087supp2_prod_1766516490.96511.pdf#page=9); protocol PLAN [p.35](../../../joi250087supp1_prod_1766516490.96011.pdf#page=35), [p.37](../../../joi250087supp1_prod_1766516490.96011.pdf#page=37), [p.81](../../../joi250087supp1_prod_1766516490.96011.pdf#page=81), [p.82](../../../joi250087supp1_prod_1766516490.96011.pdf#page=82), [p.83](../../../joi250087supp1_prod_1766516490.96011.pdf#page=83), [p.84](../../../joi250087supp1_prod_1766516490.96011.pdf#page=84), [p.127](../../../joi250087supp1_prod_1766516490.96011.pdf#page=127), [p.128](../../../joi250087supp1_prod_1766516490.96011.pdf#page=128), [p.129](../../../joi250087supp1_prod_1766516490.96011.pdf#page=129), [p.130](../../../joi250087supp1_prod_1766516490.96011.pdf#page=130). REPORT [main p.1, outcomes/results](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=1), [p.4, methods and secondary results](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=4), [p.6, Table2/footnotes](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=6), [p.7, Table3](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=7); REPORT supplement [p.5](../../../joi250087supp3_prod_1766516490.97011.pdf#page=5), [p.6](../../../joi250087supp3_prod_1766516490.97011.pdf#page=6), [p.11](../../../joi250087supp3_prod_1766516490.97011.pdf#page=11), [p.13](../../../joi250087supp3_prod_1766516490.97011.pdf#page=13), [p.16](../../../joi250087supp3_prod_1766516490.97011.pdf#page=16), [p.17](../../../joi250087supp3_prod_1766516490.97011.pdf#page=17). Complete REPORT coverage finds no secondary adjusted Cox, general-linear-model or Poisson treatment output.

**Printed values/statements:** SAP specifies etiology-adjusted Cox for mortality, ICU/hospital stay and MACE; etiology-adjusted general linear models for ECMO, organ failure, catecholamine, ventilation and RRT duration/free days; adjusted Poisson models permitting recurrent drug reactions and etiology-adjusted Poisson AE/SAE event counts. Report supplies fixed-time mortality RR1.11 (0.70–1.75), ECMO median difference−1 (−2 to1), ICU RMST difference−1 (−5 to3), hospital RMST difference−7 (−12 to−2), organ-free-day median difference−2 (−10 to4), ventilation-free-day difference−0 (−3 to2), MACE RRs1.00/0.95 and log-rank P=.87/.94, ventricular-arrhythmia RR2.06 (0.97–4.37) and patient-risk difference9.2 (0.4–18.1), plus patient counts and an SAE-frequency histogram. No model-based adjusted secondary estimate is identified. P-value omission for secondary table rows is expressly attributed to multiple testing; adjusted effects are also absent.

**Comparison logic:** Compare planned and reported model, covariates, outcome and effect quantity. A crude RR is not an adjusted Cox HR; a median/RMST difference is not the planned adjusted regression output; a patient risk is not the recurrent-event count effect. The report does not claim that these differing numerical measures reproduce one another. The issue is absent planned model outputs, not a crude-versus-adjusted arithmetic mismatch. Shared absence of the explicitly planned adjusted secondary outputs is consolidated as one pattern. No numeric half-unit interval or relative discrepancy applies.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed primary relationship:** P_R. **All relationships:** P_R.

**Qualifying route:** Route A, category 5. Mortality, ECMO duration/free days, ICU stay, organ-failure-free days, ventilation-free days and serious adverse events appear in the abstract and are key secondary under the supplied definition. The remaining occurrences extend the same absent-output pattern and independently concern explicit report-versus-plan analysis specifications.

**Affected result or extracted value:** The secondary treatment comparisons above and the adjustment/model labels extracted with them, especially the abstract mortality, ECMO, ICU and adverse-event results.

**Why context does not resolve it:** Route A category5 covers planned key secondary analyses not reported. Table footnotes clearly define the displayed crude/summary measures, so the planned adjusted model outputs cannot simply be read out of them. Multiple-testing concerns explain omitted P values but do not identify an amendment removing the planned adjusted models.

**Supported alternatives and missing definition:** The models may have been fitted but their outputs not supplied; the reported unadjusted quantities may replace them; or an undisclosed analysis revision may have removed them. The supplied materials lack the adjusted treatment coefficients/effects and an outcome-specific statement about their omission.

**Exact human question:** Were the SAP's adjusted secondary Cox, general-linear and recurrent-event Poisson analyses performed, and where are their treatment-effect outputs or the disclosed revisions accounting for their absence from the supplied report?

### F-XS-007

**Observation:** The fourth reported predefined etiologic subgroup is “other,” whereas the protocol's predefined subgroup list specifies post-cardiac-arrest patients.

**Exact locations and roles:** PLAN protocol [p.8](../../../joi250087supp1_prod_1766516490.96011.pdf#page=8), [p.14](../../../joi250087supp1_prod_1766516490.96011.pdf#page=14), [p.15](../../../joi250087supp1_prod_1766516490.96011.pdf#page=15), [p.53](../../../joi250087supp1_prod_1766516490.96011.pdf#page=53), [p.59](../../../joi250087supp1_prod_1766516490.96011.pdf#page=59), [p.60](../../../joi250087supp1_prod_1766516490.96011.pdf#page=60), [p.99](../../../joi250087supp1_prod_1766516490.96011.pdf#page=99), [p.105](../../../joi250087supp1_prod_1766516490.96011.pdf#page=105), [p.106](../../../joi250087supp1_prod_1766516490.96011.pdf#page=106) list acute MI, myocarditis, post-cardiac surgery, post-cardiac arrest. PLAN [protocol p.107, allocation](../../../joi250087supp1_prod_1766516490.96011.pdf#page=107) separately lists “other causes” as the fourth minimization category. The entire PLAN [SAP pp.1–9](../../../joi250087supp2_prod_1766516490.96511.pdf#page=1), including [p.6 primary adjustment](../../../joi250087supp2_prod_1766516490.96511.pdf#page=6), has no subgroup-analysis prescription. REPORT [main p.4, Statistical Analysis](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=4) calls the subgroup analyses predefined and equates them with a minimization factor; [p.7, Figure3](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=7) and REPORT [supplement p.18, eFigure9](../../../joi250087supp3_prod_1766516490.97011.pdf#page=18) show “other.” REPORT [supplement p.9, eTable6](../../../joi250087supp3_prod_1766516490.97011.pdf#page=9) enumerates the other causes.

**Printed values/statements:** The other-group sHR is1.61 (95% CI0.78–3.33), based on levosimendan15/21 successes and placebo12/21. Other causes comprise dilated cardiomyopathy, acute arrhythmia, cardiac arrest before ECMO, Takotsubo, valvular disease and miscellaneous diagnoses. Cardiac-arrest counts are only5/21 versus1/21 within that category. The common three predefined subgroup labels reconcile; the fourth does not.

**Comparison logic:** Item-by-item subgroup-list comparison distinguishes a specified analysis subgroup from a minimization/adjustment category. The broader other-cause subgroup is not identical to post-arrest. An allocation factor alone does not prescribe a subgroup treatment-effect analysis. The report calls this subgroup analysis predefined, but the supplied prospective subgroup list contains a different fourth population. This is a population/prespecification comparison, not a numerical rounding comparison.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed primary relationship:** P_R. **All relationships:** P_R.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** The primary-outcome sHR1.61 (0.78–3.33) in other etiologies, its prespecified-subgroup attribution, and the planned post-cardiac-arrest subgroup analysis.

**Why context does not resolve it:** Route A category5 covers an analysis described as prespecified that the supplied plan does not contain. The report's other group includes six diagnoses and42 patients; the post-arrest subset has6 patients. These are different populations, not abbreviated names for one group.

**Supported alternatives and missing definition:** An analysis-plan amendment may have substituted the minimization-category subgroup; the report may have intended “predefined allocation categories” rather than prespecified subgroup analyses; or a post-arrest analysis may have been performed but omitted. No supplied amendment states that substitution.

**Exact human question:** Which supplied prospective specification prespecified the other-etiology subgroup analysis, and did it replace or supplement the protocol's post-cardiac-arrest subgroup analysis?

## Excluded observations

Only apparent issues that were considered and not emitted appear below. Reconciled checks remain in the relationship table. Each row has one reason code.

| Location | Observation | Reason code |
|---|---|---|
| [REPORT main pp.1/4](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=4) versus [REPORT supplement p.11](../../../joi250087supp3_prod_1766516490.97011.pdf#page=11) | Day60 mortality P=.78 versus log-rank P=.56 arose from comparison of a fixed-time categorical result with a separately named time-to-event test. The source states categorical tests and log-rank separately; these are not copies of one matched test. | NOT_REPRODUCED |
| [REPORT main p.6](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=6) versus [REPORT supplement p.16](../../../joi250087supp3_prod_1766516490.97011.pdf#page=16) | ICU RMST18 versus17.5: half-unit intervals[17.5,18.5] and[17.45,17.55] overlap; gap0, relative discrepancy0. | ROUNDING_OR_DISPLAY_PRECISION |
| [REPORT main pp.1/4](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=4) versus [REPORT main p.8](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=8) | Full-dose uptake93%/96% versus discussion “more than95%.” Weighted displayed percentages yield94.522%, with input interval[94.022%,95.022%]; even a comparison to printed95% has overlapping half-unit intervals and gap0. No actual per-arm numerator is supplied. | ROUNDING_OR_DISPLAY_PRECISION |
| [REPORT main p.4](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=4) | Subgroups described with “minimization stratification factor” although center was also a factor: the immediately referenced Figure3 clearly displays the etiology categories. This center-subgroup wording is distinct from the primary fitted-model conflict in F-XS-001. | TERMINOLOGY_OR_WORDING |
| [PLAN SAP p.8](../../../joi250087supp2_prod_1766516490.96511.pdf#page=8) | The RRT paragraph calls the zero-day death assignment “ventilatory-free days”; the paragraph expressly identifies RRT duration and RRT-free days. This wording alone attributes no printed RRT value to ventilation. | TERMINOLOGY_OR_WORDING |
| [PLAN SAP p.8](../../../joi250087supp2_prod_1766516490.96511.pdf#page=8) | Wins−Losses/total-comparisons formula lacks grouping parentheses. The named net-benefit definition and win/loss/tie paragraph identify the intended proportion; no numerical calculation is printed to establish a conflicting quantity. | NOTATION_OR_TYPOGRAPHY |
| [PLAN protocol p.106](../../../joi250087supp1_prod_1766516490.96011.pdf#page=106), [PLAN SAP p.7](../../../joi250087supp2_prod_1766516490.96511.pdf#page=7), [REPORT main p.3](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=3) | Hemodynamic improvement was replaced by descriptive mean-BP evolution. The final SAP explicitly labels the revision and gives its rationale; the report repeats it. No primary/key-secondary outcome or undisclosed status/composite change is identified. | CONTEXT_RESOLVES |
| [PLAN protocol p.128](../../../joi250087supp1_prod_1766516490.96011.pdf#page=128), [PLAN SAP p.5](../../../joi250087supp2_prod_1766516490.96511.pdf#page=5), [REPORT supplement p.3](../../../joi250087supp3_prod_1766516490.97011.pdf#page=3) | Protocol consent-withdrawal/no-analysis exception versus SAP all-randomized language would affect an analysis size only if someone invoked the exception. The report prints zero declined continuation consents and all205 in primary analysis. | CONDITIONAL_OR_UNREPORTED |
| [PLAN protocol p.124](../../../joi250087supp1_prod_1766516490.96011.pdf#page=124), [PLAN SAP p.4](../../../joi250087supp2_prod_1766516490.96511.pdf#page=4), [REPORT main p.3](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=3) | General AE/SAE surveillance through60days versus report predefined drug-event assessment at30days. Different safety categories/windows are expressly described; no supplied label proves that a printed identical event count was truncated from a60-day definition. | CONDITIONAL_OR_UNREPORTED |
| [PLAN protocol p.114](../../../joi250087supp1_prod_1766516490.96011.pdf#page=114) versus [REPORT supplement p.2](../../../joi250087supp3_prod_1766516490.97011.pdf#page=2) | The report omits the older-than48-hour low-flow episode consciousness-recovery proviso while reproducing the current48-hour resuscitation exclusion. No quantitative analysis-set size or statistical decision rule is affected in supplied results. | OUT_OF_FOCUS |
| [PLAN protocol p.133](../../../joi250087supp1_prod_1766516490.96011.pdf#page=133) versus [REPORT supplement p.2](../../../joi250087supp3_prod_1766516490.97011.pdf#page=2) | The report's other-interventional-trial exclusion does not state the protocol's IMPULMACS co-enrollment exception. The supplied results establish no change in a counted analysis population or statistical decision rule. | OUT_OF_FOCUS |
| [PLAN protocol p.115, exclusion23](../../../joi250087supp1_prod_1766516490.96011.pdf#page=115) versus [REPORT supplement p.2](../../../joi250087supp3_prod_1766516490.97011.pdf#page=2) | Hypervitaminosis exclusion is absent from the report list. This clinical eligibility description is not linked to a difference in reported analysis-population size or a statistical decision rule. | OUT_OF_FOCUS |
| [PLAN protocol p.115, exclusion24](../../../joi250087supp1_prod_1766516490.96011.pdf#page=115) versus [REPORT supplement p.2](../../../joi250087supp3_prod_1766516490.97011.pdf#page=2) | Severe hypercalcemia/hypercalciuria or predisposing-condition exclusion is absent from the report list. No numerical analysis-population size or statistical decision rule changes in the supplied evidence. | OUT_OF_FOCUS |

## Scope closure and limitations

This part contains120 completed relationship groups,7 findings and13 excluded observations. The fresh [remaining cross-source shard](parts/cross_source_remaining.md) completes three additional groups: vitamin A/retinoid eligibility, administrative/version calendars and sites, and administrative REPORT sources. Its0 findings and3 exclusions give the complete stage union123 groups,7 findings and16 exclusions; the coordinator merges its excluded rows into this table after handoff. No primary or secondary result remains unchecked in this part. All194 source pages were mapped by the fresh evidence-mapping stages; this checker read both complete maps and reproduced its findings against exact supplied locations.

Limits: no raw participant records or supplied workbook/CSV/Office source; no exact plotted coordinates; no numerical bootstrap algorithm or replications; no fit objects/model coefficients beyond printed summaries; no prospective subgroup amendment beyond the supplied bundle. These limits are named where relevant and do not authorize extrapolation. Reusable renderer/version metadata are incomplete, and reused OCR is only a locator. Fresh derivatives listed above use the recorded fallback engine. Independent screening and exact-source recheck remain subsequent workflow stages.


# Cross-source consistency checker: three remaining relationship groups

Runtime canonical ID: `/root/cross_source_remaining`. This disjoint shard covers only (1) protocol exclusion criterion 25 and its report counterpart, (2) administrative calendars/sites and the tracked monthly safety-extraction text at the assigned locations, and (3) the collaborator roster and data-sharing statement. The other 120 matched groups belong to the first cross-source checker. QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read completely. Source roles follow content.

Evidence: fresh direct-source sorted native text from PyMuPDF 1.26.4 using the recorded bundled fallback; fresh 200 dpi CPU source renders for DOC-002 pp.69,100,115 and DOC-004 p.2; source-derived page images for protocol pp.149,153 and SAP p.3. Native derivatives are locators; the eligibility comparison and tracked-deletion readings were visually confirmed. No web, external literature, or legacy conclusions were used.

## Assigned relationship coverage

| Group | Exact scope and roles | Check and result | Status |
|---|---|---|---|
| Remaining group 1 | PLAN DOC-002 pp.69,100,115; REPORT DOC-004 p.2; REPORT DOC-001 p.2 as completeness context | Criterion 25 was compared item by item, rather than by list summary: concurrent vitamin A/retinoids appears in both later protocol versions but is absent from the report list described as complete. The omission is excluded below because this assigned clinical eligibility restriction is not linked to a statistical analysis-population definition/size or a reported quantitative value. Other eligibility criteria belong to the first checker. | COMPLETE |
| Remaining group 2 | PLAN DOC-002 pp.10,55,101,149,153; PLAN DOC-003 p.3; REPORT DOC-001 p.2 | Sites/calendars were matched by version and planned versus actual meaning. Administrative differences are excluded below. The monthly paragraph on p.149 is visibly struck through; it is not an active additional monthly rule conflicting with quarterly extraction. On p.153, 24+12 and 26+12 are struck through and replaced by 36+3 and 38+3, consistent with p.101. Treatment and participant follow-up are distinct from the recruitment calendar. No finding about a planned statistical decision rule results from these tracked deletions. | COMPLETE |
| Remaining group 3 | REPORT DOC-005 pp.1–3; REPORT DOC-006 p.1 | All roster pages contain collaborator names, institutions, locations and contributions, without result quantities or prospective statistical specifications. The sharing statement prints Data available: No and bibliographic/registry identifiers, without an outcome, model, denominator, analysis set, or statistical decision rule. No applicable matched quantitative or planned result exists. This is a coverage record, not an excluded observation. | COMPLETE |

## Findings

No finding meets the inclusion threshold in this assigned shard.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| PLAN [DOC-002 p.69, exclusion 25 and section 6.2](../../../joi250087supp1_prod_1766516490.96011.pdf#page=69), [p.100, summary exclusion 25](../../../joi250087supp1_prod_1766516490.96011.pdf#page=100), [p.115, exclusion 25 and section 6.2](../../../joi250087supp1_prod_1766516490.96011.pdf#page=115) versus REPORT [DOC-004 p.2, eAppendix Patients](../../../joi250087supp3_prod_1766516490.97011.pdf#page=2), with REPORT [DOC-001 p.2 completeness statement](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=2) | The protocol prints criterion 25, “In combination with vitamin A or retinoids,” in both later versions and the final summary. The report exclusion list ends with CERNEVIT hypersensitivity and then consent, without that restriction, although the main article calls the list complete. This individual criterion omission is reproduced; however, it is a clinical eligibility description, with no demonstrated difference in a statistical analysis-set definition, the size of an analysis population, or a specific primary/key secondary quantitative result. Eligibility under section 6.2 alone does not establish that any enrolled participant or denominator changed. It is not a Route A category: no prespecified outcome status/composite or planned primary/key secondary analysis changes in this assigned comparison. A general population-description extraction difference does not supply the required focus-A–D link for Route B. | OUT_OF_FOCUS |
| PLAN [DOC-002 p.10](../../../joi250087supp1_prod_1766516490.96011.pdf#page=10), [p.55](../../../joi250087supp1_prod_1766516490.96011.pdf#page=55), [p.101](../../../joi250087supp1_prod_1766516490.96011.pdf#page=101) versus REPORT [DOC-001 p.2](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=2) | Protocol versions list 13 then 14 planned centers; the article describes conduct at 11 sites. These are administrative planned-versus-participating-site quantities. The compared passages do not change a reported primary/key secondary result, the analysis-population size, or a statistical decision rule. | PERIPHERAL_COMPARISON |
| PLAN [DOC-002 p.10](../../../joi250087supp1_prod_1766516490.96011.pdf#page=10), [p.55](../../../joi250087supp1_prod_1766516490.96011.pdf#page=55), [p.101](../../../joi250087supp1_prod_1766516490.96011.pdf#page=101), [p.153](../../../joi250087supp1_prod_1766516490.96011.pdf#page=153), [DOC-003 p.3](../../../joi250087supp2_prod_1766516490.96511.pdf#page=3) versus REPORT [DOC-001 p.2](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=2) | Administrative enrollment/total calendars progress from 24/26 months to 24+12/26+12 and then 36+3/38+3; SAP summary still says 24-month enrollment, and the article gives actual dates August 27, 2021–September 10, 2024, with final follow-up November 10, 2024. This calendar comparison is peripheral. The 24-hour treatment and 60-day participant follow-up are different quantities and remain distinct; the assigned comparison supplies no changed outcome window, population size, or statistical decision rule. | PERIPHERAL_COMPARISON |

The struck-through monthly extraction paragraph and replaced calendar numbers reconcile after source-image inspection and therefore are recorded only in coverage, not as excluded observations.

## Limitations and derivative record

Three assigned relationship groups are complete. Findings: 0. Excluded observations: 3. Scientific coverage gaps: 0. No supplied structured quantitative file exists. These sources do not reveal whether any participant was affected by criterion 25; that is a limitation on inference, not on the printed comparison.

Fresh derivatives are `preprocessing/cross_source_remaining-DOC002-p10.txt`, `-p55.txt`, `-p69.txt`, `-p100.txt`, `-p101.txt`, `-p115.txt`, `-p149.txt`, and `-p153.txt`; `preprocessing/cross_source_remaining-DOC001-p2.txt`; `preprocessing/cross_source_remaining-DOC004-p2.txt`; `preprocessing/cross_source_remaining-DOC005-p1-3.txt`; and `preprocessing/cross_source_remaining-DOC006-p1.txt`. Each was produced by PyMuPDF 1.26.4 sorted reading-order native extraction through the bundled missing-tool helper. Fresh source renders are `preprocessing/cross_source_remaining-DOC002-p69.png`, `-p100.png`, `-p115.png`, and `preprocessing/cross_source_remaining-DOC004-p2.png`, each PyMuPDF 1.26.4, 200 dpi, CPU. Existing protocol p.149/p.153 and SAP p.3 images were inspected without modification.
