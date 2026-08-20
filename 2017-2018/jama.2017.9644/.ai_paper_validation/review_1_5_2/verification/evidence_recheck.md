# Mechanical Evidence Recheck

## Scope and method

This artifact mechanically rechecks every stable candidate ID in `candidate_ledger.md`: C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, and C013. Each cited location was inspected in the direct supplied PDF. Fresh text, layout, and rendered-page assets were used only to locate and read the direct-source content. No legacy audit derivative or external source was used. Calculations below use the printed inputs and ordinary one-decimal percentage rounding. Every ID remains **Pending Human Adjudication**.

## C001 — Figure 2 combines a percentage axis with count-like embedded labels without stating the embedded unit

- **Cited location found:** Yes. [Main article — PDF p. 7, Figure 2A-B](../../../jama_lapergue_2017_oi_170084.pdf#page=7) contains both horizontal axes, group labels, internal segment labels, and the mTICI legend.
- **Source printed value/text matched:** Yes. Both horizontal axes run from 0 to 100 and are labelled `Patients, %`. Figure 2A prints contact-aspiration values `8, 2, 18, 92, 72` for `n=192` and stent-retriever values `5, 5, 22, 84, 73` for `n=189`. Figure 2B prints `26, 6, 39, 66, 55` and `20, 9, 32, 61, 67` for the same group totals.
- **Comparator matched:** Yes. [Main article — PDF p. 6, Table 2](../../../jama_lapergue_2017_oi_170084.pdf#page=6) prints end-of-all-procedure mTICI 2b/3 counts `164/192` and `157/189`, and first-line mTICI 2b/3 counts `121/192` and `128/189`.
- **Consistency rule applicable:** Yes. A display using percentage-scaled geometry and count-valued internal annotations should distinguish the annotation unit sufficiently for a reader to know whether an internal integer is a count or a percentage.
- **Calculation or logical comparison reproduced:** Figure 2A gives `8+2+18+92+72=192` and `5+5+22+84+73=189`; its mTICI 2b/3 segments give `92+72=164` and `84+73=157`. Figure 2B gives `26+6+39+66+55=192` and `20+9+32+61+67=189`; its mTICI 2b/3 segments give `66+55=121` and `61+67=128`. Thus the internal labels reproduce counts while the bar geometry and axis use percentages.
- **Necessary inputs available:** The axis wording, scale, group totals, segment labels, legend, and matched Table 2 numerators are available. The figure does not include an explicit `No.`, `n`, or equivalent definition for the internal labels; the production figure-data specification is not supplied.
- **Source-grounded alternative interpretation:** Figure 2 can be read as an intentional 100%-stacked chart whose geometry represents percentages and whose embedded labels provide counts. Under that reading, the numerical content reconciles exactly.
- **Direct observation versus inferred explanation:** Directly observed are the percentage-axis wording, group totals, internal integers, and Table 2 values. The conclusion that a reader may not recognize the embedded values as counts, and the possibility that this was an intentional production convention, are inferences.
- **Exact remaining human question:** Was Figure 2 intentionally designed with percentage-scaled bars and unlabelled count annotations, and should the internal values be explicitly identified as counts?

## C002 — eTable frontline stent header does not identify how n=175 relates to the main flow totals

- **Cited location found:** Yes. [Supplement 2 — PDF p. 4, eTable](../../../joi170084supp2_prod.pdf#page=4) is titled `Detail of Thrombectomy Devices Used in Frontline and Rescue Strategies According to the Assigned Groups` and prints `Stent Retriever First (n=175)` for the frontline strategy. [Main article — PDF p. 4, Figure 1](../../../jama_lapergue_2017_oi_170084.pdf#page=4) prints the randomized and received-treatment flow.
- **Source printed value/text matched:** Yes. The eTable frontline headers are aspiration first `n=174` and stent retriever first `n=175`. Its stent-assigned frontline device entries sum to 186 device entries, including five aspiration-device entries and 181 stent-retriever entries.
- **Comparator matched:** Yes. Figure 1 prints 189 randomized to receive stent retriever, 170 who received stent retriever as randomized, and 19 who did not: 12 spontaneous clot lyses, 1 groin access failure, 5 mistakenly treated in the contact-aspiration group, and 1 extracranial stenting without stent retriever.
- **Consistency rule applicable:** Yes. A treatment-labelled column header containing `n` should state or make recoverable whether it counts randomized participants, recipients of the assigned treatment, participants receiving any frontline thrombectomy device, or another population. Device-row counts should not be treated as a participant partition unless the source states that rows are mutually exclusive.
- **Calculation or logical comparison reproduced:** `175` differs from both `189` randomized and `170` who received stent retriever as randomized. It also reconstructs exactly as `189-12-1-1=175`, excluding participants without a frontline thrombectomy device while retaining the five assigned-stent participants treated with contact aspiration. The five aspiration-device entries in the eTable stent-assigned column are consistent with those five crossovers. The device rows sum to 186, so their sum is not the participant header total.
- **Necessary inputs available:** The randomized count, nonreceipt components, crossover count, eTable title/header, and device counts are available. Missing are an explicit eTable denominator definition, a statement whether a participant can contribute to multiple frontline device rows, and participant-level device mapping.
- **Source-grounded alternative interpretation:** The eTable may use assigned-group columns and count participants who underwent any frontline device procedure: 174 in the aspiration-assigned group and 175 in the stent-assigned group. This arithmetic reconciles with Figure 1 even though the abbreviated header `Stent Retriever First` can be read as actual receipt of the assigned stent treatment.
- **Direct observation versus inferred explanation:** Directly observed are all header, flow, and device-row values and labels. The interpretation that `n=175` represents participants with any frontline device procedure is inferred from the exact flow arithmetic and the five aspiration-device entries; the eTable does not state it explicitly.
- **Exact remaining human question:** Does `Stent Retriever First (n=175)` mean stent-assigned participants who underwent any frontline device procedure, and if so should the column header or footnote define that population explicitly?

## C003 — Protocol and publication report different design sample sizes

- **Cited location found:** Yes. [Protocol — PDF p. 7, section 5.3](../../../joi170084supp1_prod.pdf#page=7) contains the protocol calculation. [Main article — PDF p. 3, Statistical Analysis](../../../jama_lapergue_2017_oi_170084.pdf#page=3) contains the published calculation.
- **Source printed value/text matched:** Yes. Protocol V1.1 prints control and experimental rates of 70% and 85%, a two-sided 5% alpha risk, 90% power, and 161 participants per arm, 322 total. The protocol describes the increase as 21%, which is compatible with the relative increase `(85-70)/70=21.4%`.
- **Comparator matched:** Yes. The article prints 70% for stent retriever, a 15% absolute increase for contact aspiration, two-sided alpha `.05`, 90% power, a 15% spontaneous-revascularization/catheterization-failure assumption, and 190 per group, 380 total.
- **Consistency rule applicable:** Yes. Different design sample sizes for the same trial should be traceable to differing assumptions or to a controlling amendment/version record; absent that provenance, the supplied documents leave the design transition unresolved.
- **Calculation or logical comparison reproduced:** `161*2=322` and `190*2=380`; the total difference is `380-322=58`, or 29 per group. The supplied premises share the 70%/85% rates, two-sided alpha, and 90% power. The publication adds an explicit 15% spontaneous-revascularization/catheterization-failure assumption not stated in the protocol calculation.
- **Necessary inputs available:** The two printed target totals, allocation, rates, alpha, power, and publication failure assumption are available. Missing are the complete formula/variance and attrition handling used for each calculation, an approved amendment or later protocol version, the finalized statistical analysis plan mentioned in protocol section 5.2, and its timing relative to database lock.
- **Source-grounded alternative interpretation:** A later controlling document may have added the publication's 15% failure allowance or otherwise revised the target from 322 to 380 before enrollment or analysis. No such document is supplied.
- **Direct observation versus inferred explanation:** The two calculations and their printed premises are direct observations. An authorized later amendment, and the reason for the 58-participant increase, are inferred possibilities rather than supplied facts.
- **Exact remaining human question:** Which approved protocol amendment or finalized statistical analysis plan governed the trial's sample size, and does it document the change from 322 to 380 participants?

## C004 — Protocol and publication report different primary analysis methods

- **Cited location found:** Yes. [Protocol — PDF p. 6](../../../joi170084supp1_prod.pdf#page=6) states that a detailed statistical analysis plan would be finalized before database lock; [protocol — PDF p. 7, Primary objective](../../../joi170084supp1_prod.pdf#page=7) prints the planned primary method. [Main article — PDF p. 3, Statistical Analysis](../../../jama_lapergue_2017_oi_170084.pdf#page=3) prints the published primary method. [Supplement 2 — PDF p. 2](../../../joi170084supp2_prod.pdf#page=2) describes related mixed-logistic and marginal-risk-difference methods for secondary binary outcomes.
- **Source printed value/text matched:** Yes. Protocol V1.1 states a chi-square comparison, absolute and relative rate differences with 95% confidence intervals, a center-stratified analysis, and a Breslow-Day test for center-by-treatment interaction.
- **Comparator matched:** Yes. The article states that primary-outcome rates were compared using mixed logistic regression with prior IV thrombolysis as a fixed effect and center as a random effect, producing an adjusted odds ratio and marginal-probability absolute and relative risk differences. Supplement 2 confirms the same model/effect family for secondary binary outcomes and describes bootstrap confidence intervals for their risk differences.
- **Consistency rule applicable:** Yes. A change in the prespecified primary test/model, covariate adjustment, and center handling should be traceable to the controlling protocol amendment or final statistical analysis plan.
- **Calculation or logical comparison reproduced:** This is a method-identity comparison rather than a numerical recalculation. Chi-square plus center stratification/Breslow-Day is not the same primary analysis specification as a mixed logistic model with IV thrombolysis fixed and center random effects. Both concern the same trial's primary outcome analysis.
- **Necessary inputs available:** The planned and published model descriptions, primary endpoint context, and protocol statement that a later detailed plan would exist are available. Missing are the finalized statistical analysis plan, amendment/version history, approval and finalization dates, database-lock date, and a document identifying which analysis specification controlled.
- **Source-grounded alternative interpretation:** The publication may implement a pre-database-lock finalized statistical analysis plan or approved amendment anticipated by protocol section 5.2. The supplied package does not include that controlling document.
- **Direct observation versus inferred explanation:** The different printed analysis specifications are direct observations. Whether the mixed model was prospectively authorized, when it was selected, and why it superseded the protocol method are not directly observed.
- **Exact remaining human question:** Was the mixed-logistic primary analysis prespecified in an approved controlling document finalized before database lock, and how did that document supersede protocol V1.1's chi-square/center-stratified plan?

## C005 — Stent intracranial-hemorrhage percentage does not match 85/188

- **Cited location found:** Yes. [Main article — PDF p. 8, Table 3](../../../jama_lapergue_2017_oi_170084.pdf#page=8), stent-retriever `Intracranial hemorrhage at 24 h` row.
- **Source printed value/text matched:** Yes. The row prints `85/188 (46.2)`.
- **Comparator matched:** Yes. The comparator is the printed fraction `85/188` under the table heading `No./Total (%)`; [main article — PDF p. 7](../../../jama_lapergue_2017_oi_170084.pdf#page=7) separately repeats 85 patients and 46.2% without printing a denominator.
- **Consistency rule applicable:** Yes. Under `No./Total (%)`, the parenthesized percentage should equal numerator divided by denominator times 100, rounded to one decimal.
- **Calculation or logical comparison reproduced:** `85/188*100=45.212766%`, which rounds to `45.2%`, not `46.2%`; the displayed difference is 1.0 percentage point. `85/184*100=46.195652%`, which rounds to `46.2%`.
- **Necessary inputs available:** All inputs needed to test the printed within-row identity are available. Missing are the intended row denominator, row-level analysis-population definition, and participant-level event/availability data needed to identify which printed element governs.
- **Source-grounded alternative interpretation:** Table 3 prints denominator 184 for the nearby stent intraventricular and remote-intracranial-hemorrhage rows, and page 7 repeats 85 patients (46.2%). An intended denominator of 184 would reconcile the repeated numerator and percentage, but the source does not state that denominator for this row.
- **Direct observation versus inferred explanation:** The fraction, percentage, narrative repetition, and nearby 184 denominators are direct observations. A denominator substitution or transcription mechanism is inferred.
- **Exact remaining human question:** What denominator produced 46.2% for 85 stent-group events, and which row element reflects the intended analysis population?

## C006 — Stent hemorrhagic-infarction percentage does not match 49/188

- **Cited location found:** Yes. [Main article — PDF p. 8, Table 3](../../../jama_lapergue_2017_oi_170084.pdf#page=8), stent-retriever `Hemorrhagic infarction` row.
- **Source printed value/text matched:** Yes. The row prints `49/188 (26.6)`.
- **Comparator matched:** Yes. The comparator is the same-row printed fraction `49/188` under `No./Total (%)`.
- **Consistency rule applicable:** Yes. The printed percentage should reproduce from the same-row fraction under ordinary one-decimal rounding.
- **Calculation or logical comparison reproduced:** `49/188*100=26.063830%`, which rounds to `26.1%`, not `26.6%`; the displayed difference is 0.5 percentage point. `49/184*100=26.630435%`, which rounds to `26.6%`.
- **Necessary inputs available:** The fraction and percentage needed for the identity check are available. Missing are the intended denominator and row-level analysis-population/availability data.
- **Source-grounded alternative interpretation:** The same stent column prints denominator 184 for two nearby hemorrhage rows; if 184 was intended here, the displayed 26.6% would reconcile. The row itself prints 188.
- **Direct observation versus inferred explanation:** The printed values and nearby 184 denominators are direct observations. Whether 184 was intended for this row is inferred.
- **Exact remaining human question:** Is this row's intended denominator 188 or 184, and which printed percentage corresponds to the intended denominator?

## C007 — Stent hemorrhagic-infarction type 1 percentage does not match 24/188

- **Cited location found:** Yes. [Main article — PDF p. 8, Table 3](../../../jama_lapergue_2017_oi_170084.pdf#page=8), stent-retriever `Hemorrhagic infarction, Type 1` row.
- **Source printed value/text matched:** Yes. The row prints `24/188 (13.0)`.
- **Comparator matched:** Yes. The comparator is the same-row printed fraction `24/188` under `No./Total (%)`.
- **Consistency rule applicable:** Yes. The printed percentage should reproduce from the same-row fraction under ordinary one-decimal rounding.
- **Calculation or logical comparison reproduced:** `24/188*100=12.765957%`, which rounds to `12.8%`, not `13.0%`; the displayed difference is 0.2 percentage point. `24/184*100=13.043478%`, which rounds to `13.0%`.
- **Necessary inputs available:** The displayed numerator, denominator, and percentage are available. Missing are the intended denominator and the row-level definition of available core-laboratory observations.
- **Source-grounded alternative interpretation:** The displayed percentage is compatible with denominator 184, which appears elsewhere in the same stent hemorrhage column, but 184 is not printed on this row.
- **Direct observation versus inferred explanation:** The row values and nearby denominator pattern are directly observed. An intended denominator of 184 is inferred.
- **Exact remaining human question:** Which denominator defines the stent Type 1 hemorrhagic-infarction population, and should the row's fraction and percentage use that same denominator?

## C008 — Stent hemorrhagic-infarction type 2 percentage does not match 25/188

- **Cited location found:** Yes. [Main article — PDF p. 8, Table 3](../../../jama_lapergue_2017_oi_170084.pdf#page=8), stent-retriever `Hemorrhagic infarction, Type 2` row.
- **Source printed value/text matched:** Yes. The row prints `25/188 (13.6)`.
- **Comparator matched:** Yes. The comparator is the same-row printed fraction `25/188` under `No./Total (%)`.
- **Consistency rule applicable:** Yes. The printed percentage should reproduce from the same-row fraction under ordinary one-decimal rounding.
- **Calculation or logical comparison reproduced:** `25/188*100=13.297872%`, which rounds to `13.3%`, not `13.6%`; the displayed difference is 0.3 percentage point. `25/184*100=13.586957%`, which rounds to `13.6%`.
- **Necessary inputs available:** The displayed numerator, denominator, and percentage are available. Missing are the intended denominator and row-level analysis-population/availability data.
- **Source-grounded alternative interpretation:** The displayed percentage is compatible with denominator 184, which is printed elsewhere in the same stent hemorrhage column, but this row prints 188.
- **Direct observation versus inferred explanation:** The row values and nearby denominator pattern are direct observations. An intended 184 denominator is inferred.
- **Exact remaining human question:** Which denominator defines the stent Type 2 hemorrhagic-infarction population, and which percentage is intended under that denominator?

## C009 — Stent parenchymal-hematoma percentage does not match 33/188

- **Cited location found:** Yes. [Main article — PDF p. 8, Table 3](../../../jama_lapergue_2017_oi_170084.pdf#page=8), stent-retriever `Parenchymal hematoma` row.
- **Source printed value/text matched:** Yes. The row prints `33/188 (17.4)`.
- **Comparator matched:** Yes. The comparator is the same-row printed fraction `33/188` under `No./Total (%)`; the two indented stent components print 19 and 14, which sum to the displayed total numerator 33.
- **Consistency rule applicable:** Yes. The percentage should reproduce from the same-row fraction under one-decimal rounding, while the component-count identity can be checked separately.
- **Calculation or logical comparison reproduced:** `19+14=33`. However, `33/188*100=17.553191%`, which rounds to `17.6%`, not `17.4%`; the displayed difference is 0.2 percentage point. The nearby alternative denominator does not resolve it: `33/184*100=17.934783%`, which rounds to `17.9%`.
- **Necessary inputs available:** The parent and component numerators, printed denominator, and percentage are available. Missing are any row-specific denominator other than 188, participant-level event data, and the intended source for 17.4%.
- **Source-grounded alternative interpretation:** The total numerator may intentionally equal the two printed component counts while the percentage derives from a different, unprinted row denominator or from a different table version. Neither denominator 188 printed on this row nor 184 printed nearby reproduces 17.4%.
- **Direct observation versus inferred explanation:** The parent/component identity, row fraction, percentage, and nearby denominator are direct observations. A version-mixing or unprinted-denominator explanation is inferred and is not established by the package.
- **Exact remaining human question:** What numerator and denominator generated 17.4% for total parenchymal hematoma, and how should that result reconcile with the printed component total `19+14=33`?

## C010 — Stent parenchymal-hematoma type 1 percentage does not match 19/188

- **Cited location found:** Yes. [Main article — PDF p. 8, Table 3](../../../jama_lapergue_2017_oi_170084.pdf#page=8), stent-retriever `Parenchymal hematoma, Type 1` row.
- **Source printed value/text matched:** Yes. The row prints `19/188 (10.3)`.
- **Comparator matched:** Yes. The comparator is the same-row printed fraction `19/188` under `No./Total (%)`.
- **Consistency rule applicable:** Yes. The printed percentage should reproduce from the same-row fraction under ordinary one-decimal rounding.
- **Calculation or logical comparison reproduced:** `19/188*100=10.106383%`, which rounds to `10.1%`, not `10.3%`; the displayed difference is 0.2 percentage point. `19/184*100=10.326087%`, which rounds to `10.3%`.
- **Necessary inputs available:** The printed numerator, denominator, and percentage are available. Missing are the intended denominator and row-level analysis-population/availability data.
- **Source-grounded alternative interpretation:** Denominator 184 is printed for two nearby stent hemorrhage rows and would reproduce 10.3%, but this row prints 188.
- **Direct observation versus inferred explanation:** The row values and nearby denominator are direct observations. Whether the denominator should be 184 is inferred.
- **Exact remaining human question:** Which denominator defines the stent Type 1 parenchymal-hematoma population, and which row percentage corresponds to it?

## C011 — Stent parenchymal-hematoma type 2 percentage does not match 14/188

- **Cited location found:** Yes. [Main article — PDF p. 8, Table 3](../../../jama_lapergue_2017_oi_170084.pdf#page=8), stent-retriever `Parenchymal hematoma, Type 2` row.
- **Source printed value/text matched:** Yes. The row prints `14/188 (7.6)`.
- **Comparator matched:** Yes. The comparator is the same-row printed fraction `14/188` under `No./Total (%)`.
- **Consistency rule applicable:** Yes. The printed percentage should reproduce from the same-row fraction under ordinary one-decimal rounding.
- **Calculation or logical comparison reproduced:** `14/188*100=7.446809%`, which rounds to `7.4%`, not `7.6%`; the displayed difference is 0.2 percentage point. `14/184*100=7.608696%`, which rounds to `7.6%`.
- **Necessary inputs available:** The printed numerator, denominator, and percentage are available. Missing are the intended denominator and row-level analysis-population/availability data.
- **Source-grounded alternative interpretation:** Denominator 184 is printed for nearby stent hemorrhage rows and would reproduce 7.6%, but this row prints 188.
- **Direct observation versus inferred explanation:** The row values and nearby denominator are direct observations. Whether 184 was intended is inferred.
- **Exact remaining human question:** Which denominator defines the stent Type 2 parenchymal-hematoma population, and which percentage is intended under that denominator?

## C012 — Stent symptomatic-intracranial-hemorrhage percentage does not match 12/188

- **Cited location found:** Yes. [Main article — PDF p. 8, Table 3](../../../jama_lapergue_2017_oi_170084.pdf#page=8), stent-retriever `Symptomatic intracranial hemorrhage at 24 h` row.
- **Source printed value/text matched:** Yes. The row prints `12/188 (6.5)`.
- **Comparator matched:** Yes. The comparator is the same-row printed fraction `12/188`; [main article — PDF p. 7](../../../jama_lapergue_2017_oi_170084.pdf#page=7) separately repeats 12 patients and 6.5% without a denominator.
- **Consistency rule applicable:** Yes. Under `No./Total (%)`, the percentage should reproduce from the same-row fraction under ordinary one-decimal rounding.
- **Calculation or logical comparison reproduced:** `12/188*100=6.382979%`, which rounds to `6.4%`, not `6.5%`; the displayed difference is 0.1 percentage point. `12/184*100=6.521739%`, which rounds to `6.5%`.
- **Necessary inputs available:** The within-row values and narrative repetition are available. Missing are the intended denominator, the exact available core-laboratory population for this row, and participant-level event data.
- **Source-grounded alternative interpretation:** The same stent column prints denominator 184 for nearby hemorrhage rows, and page 7 repeats 12 patients (6.5%). An intended denominator of 184 would reconcile that repeated numerator and percentage, but Table 3 prints 188.
- **Direct observation versus inferred explanation:** The row values, narrative repetition, and nearby denominator are direct observations. A denominator substitution is inferred.
- **Exact remaining human question:** What denominator produced 6.5% for 12 stent-group symptomatic hemorrhages, and which row element reflects the intended analysis population?

## C013 — Stent subarachnoid-hemorrhage percentage does not match 13/188

- **Cited location found:** Yes. [Main article — PDF p. 8, Table 3](../../../jama_lapergue_2017_oi_170084.pdf#page=8), stent-retriever `Subarachnoid hemorrhage` row.
- **Source printed value/text matched:** Yes. The row prints `13/188 (7.1)`.
- **Comparator matched:** Yes. The comparator is the same-row printed fraction `13/188`; [main article — PDF p. 7](../../../jama_lapergue_2017_oi_170084.pdf#page=7) reports a pooled 26 subarachnoid-hemorrhage events, and Table 3 prints 13 in each group, giving `13+13=26`.
- **Consistency rule applicable:** Yes. The within-row percentage should reproduce from its printed fraction under one-decimal rounding; the pooled count identity is a separate applicable check.
- **Calculation or logical comparison reproduced:** `13+13=26`, so the pooled narrative count reconciles. However, `13/188*100=6.914894%`, which rounds to `6.9%`, not `7.1%`; the displayed difference is 0.2 percentage point. `13/184*100=7.065217%`, which rounds to `7.1%`.
- **Necessary inputs available:** The group numerator, printed denominator, percentage, and pooled comparator are available. Missing are the intended stent denominator and row-level analysis-population/availability data.
- **Source-grounded alternative interpretation:** Denominator 184 is printed for nearby stent hemorrhage rows and would reproduce 7.1%. The numerator is independently supported by the pooled narrative total, but the row itself prints denominator 188.
- **Direct observation versus inferred explanation:** The row values, pooled total, and nearby denominator are direct observations. An intended denominator of 184 is inferred.
- **Exact remaining human question:** Which denominator defines the stent subarachnoid-hemorrhage population, and should the within-row fraction and percentage be aligned while preserving the source-supported numerator 13?

## Recheck completeness and limitations

- **Stable IDs covered:** C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013.
- **Coverage:** 13/13 stable candidate IDs, including nine separate Table 3 within-row percentage calculations.
- **Direct-source locations covered:** main article PDF pp. 3, 4, 6, 7, and 8; protocol PDF pp. 6 and 7; Supplement 2 PDF pp. 2 and 4.
- **Remaining evidence limitations:** No production specification defines Figure 2's internal label unit; no explicit eTable frontline denominator definition or participant-level device mapping is supplied; no protocol amendment/final statistical analysis plan and version chronology are supplied; no participant-level Table 3 event/availability data or row-specific denominator definitions are supplied.
- **Disposition boundary:** This mechanical recheck records source facts and reproducible comparisons only. It does not delete, merge, renumber, adjudicate, or prescribe a source change for any stable ID.
