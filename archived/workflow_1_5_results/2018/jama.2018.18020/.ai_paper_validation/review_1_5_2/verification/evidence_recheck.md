# Evidence Recheck of Stable Candidates C001-C014

This artifact records a source-first mechanical recheck of every stable ID in `candidate_ledger.md`. The supplied PDFs are the authority; fresh native/layout text and rendered pages were used only to locate and visually align printed material. Every ID remains **Pending Human Adjudication**. No source was modified, no old audit derivative was consulted, and no additional derivative was required.

## C001 — Abstract sex percentage conflicts with the enrolled sex count

- **Cited location found:** DOC-001 [PDF p. 1](../../../jama_stunnenberg_2018_oi_180136.pdf#page=1), Abstract Results; DOC-001 [PDF p. 4](../../../jama_stunnenberg_2018_oi_180136.pdf#page=4), Baseline Data.
- **Source printed value/text matched:** The abstract prints `Among 30 enrolled patients ... 22% men`. The Baseline Data paragraph prints `Twenty-two men and 8 women ... were enrolled`.
- **Comparator matched:** Both statements describe the enrolled population of 30. The p. 4 counts also sum to the abstract denominator.
- **Consistency rule applicable:** A count, percentage, and denominator reported for the same population must be arithmetically compatible and must identify the same field.
- **Calculation or logical comparison reproduced:** `22 + 8 = 30`; `22 / 30 × 100 = 73.333...%`. Conversely, `22% × 30 = 6.6`, which is not an integer patient count and does not match 22 men.
- **Necessary inputs available:** Enrolled total, enrolled male count, enrolled female count, and abstract percentage are all printed.
- **Exact missing inputs or definitions:** The supplied package does not include the enrollment-level sex dataset, manuscript proof history, or an author statement identifying whether the intended abstract field was a count or a percentage.
- **Source-grounded alternative interpretation:** `22% men` may be a local field-formatting error in which `22 men` was intended, or the intended percentage may have been approximately `73% men`.
- **Direct observation versus inferred explanation:** The two printed statements and arithmetic are direct observations. The possible loss of the word `men` or substitution of a percent sign is an inferred explanation.
- **Exact remaining human question:** In the authoritative enrollment data and proof, should the abstract report `22 men`, approximately `73% men`, or a different count/denominator?

## C002 — INQoL IQR endpoints exceed the stated 0-to-100 scale

- **Cited location found:** DOC-001 [PDF p. 5](../../../jama_stunnenberg_2018_oi_180136.pdf#page=5), Table 1 INQoL row and footnote f; the same scale definition appears in the Methods on [PDF p. 3](../../../jama_stunnenberg_2018_oi_180136.pdf#page=3) and in Table 2 footnote g on [PDF p. 8](../../../jama_stunnenberg_2018_oi_180136.pdf#page=8).
- **Source printed value/text matched:** Table 1 prints CLCN1 `84.0 (74.5-110.3)` and SCN4A `98.0 (56.0-120.0)` for the INQoL composite score. Footnote f prints `Scale, 0 to 100` and identifies higher scores as greater disease burden.
- **Comparator matched:** The row label is the INQoL composite score, and the row-specific footnote and Methods use that same measure name and 0-to-100 range.
- **Consistency rule applicable:** A quantile of a quantity bounded above by 100 cannot exceed 100 when the same scoring definition is applied.
- **Calculation or logical comparison reproduced:** The reported upper IQR endpoints exceed the printed maximum by `110.3 - 100 = 10.3` points and `120.0 - 100 = 20.0` points.
- **Necessary inputs available:** Both upper IQR endpoints, the row label, and the scale endpoints are printed.
- **Exact missing inputs or definitions:** The package lacks item-level INQoL responses, the scoring worksheet or algorithm used for these values, unrounded subgroup summaries, and a definition of any alternative composite scoring convention.
- **Source-grounded alternative interpretation:** The 0-to-100 footnote may be incomplete for the composite actually tabulated, or the row values may have been calculated on a summed or otherwise transformed scale that was not described.
- **Direct observation versus inferred explanation:** Values above 100 and the stated maximum of 100 are direct observations. An incomplete footnote or alternate scoring convention is an inferred explanation.
- **Exact remaining human question:** What was the authoritative scoring range and calculation convention for the INQoL composite values in Table 1, and which printed field should be changed to reflect it?

## C003 — Table 2 secondary-outcome contrast header is opposite to the displayed effect signs

- **Cited location found:** DOC-001 [PDF p. 7](../../../jama_stunnenberg_2018_oi_180136.pdf#page=7), Table 2 change-score block and the header `Treatment Effect (Placebo-Mexiletine)`; [PDF p. 8](../../../jama_stunnenberg_2018_oi_180136.pdf#page=8) contains the table continuation and footnotes.
- **Source printed value/text matched:** In the p. 7 change-score block, placebo and mexiletine changes are respectively `-7.22` and `-21.44` for INQoL, `0.46` and `-2.39` for first handgrip action myotonia, `1.04` and `8.66` for SF-36 physical, and `-1.85` and `4.77` for SF-36 mental. The printed effects are `-14.22`, `-2.85`, `7.81`, and `6.78`.
- **Comparator matched:** The explicit header assigns placebo minus mexiletine to the same effect column that contains those values. The p. 8 continuation has a level comparison rather than another change-score example; it does not remove the p. 7 header-to-row sign conflict.
- **Consistency rule applicable:** Reversing a subtraction reverses its sign. A fixed contrast label must agree with the sign direction used by the rows beneath it.
- **Calculation or logical comparison reproduced:** Mexiletine minus placebo gives `-21.44 - (-7.22) = -14.22` and `-2.39 - 0.46 = -2.85`, exactly matching the printed effects. For SF-36, `8.66 - 1.04 = 7.62` and `4.77 - (-1.85) = 6.62`, directionally matching the positive printed effects; paired calculations from unrounded patient data can explain the small magnitude differences. Placebo minus mexiletine gives the opposite sign in all four examples.
- **Necessary inputs available:** The contrast header, both period-change columns, effect signs, and multiple independent rows are printed.
- **Exact missing inputs or definitions:** The package lacks the unrounded paired change data, a statistical output table defining the coded contrast, and an explicit statement that a favorable-direction convention overrides the printed subtraction order.
- **Source-grounded alternative interpretation:** The header may have been intended to read `Mexiletine-Placebo`; alternatively, the effect column may use an undocumented outcome-direction convention rather than one fixed subtraction.
- **Direct observation versus inferred explanation:** The header, row values, and exact sign reversals are direct observations. A reversed header or undocumented convention is an inferred explanation.
- **Exact remaining human question:** What contrast was actually computed for the Table 2 change-score block, and should the header, effect signs, or an explanatory note state that direction?

## C004 — Placebo “Any” adverse-reaction percentage does not reconcile with the apparent denominator

- **Cited location found:** DOC-003 [PDF p. 6](../../../joi180136supp2_prod.pdf#page=6), eTable 4; DOC-001 [PDF p. 8](../../../jama_stunnenberg_2018_oi_180136.pdf#page=8), Adverse Events and Mexiletine Drug Levels. A preliminary derivative locator placed this comparator on p. 9; the coordinator repaired the canonical ledger to physical PDF p. 8.
- **Source printed value/text matched:** eTable 4 prints placebo `Any 2 (6%)`. It prints mexiletine `Any 27 (90%)`, gastrointestinal discomfort `21 (70%)`, and dosage reduction `3 (10%)`; several other counts of 1 and 2 are displayed as 3% and 7%. The main article prints gastrointestinal discomfort in `21 of 30 patients (70%)` during mexiletine periods.
- **Comparator matched:** The surrounding eTable values and main-text `21 of 30` identify 30 as the apparent patient denominator. Within eTable 4, mexiletine counts of 2 are displayed as 7%, while the placebo `Any` count of 2 is displayed as 6%.
- **Consistency rule applicable:** A count and whole-number percentage must reconcile with the applicable denominator and a consistently applied rounding rule.
- **Calculation or logical comparison reproduced:** `2 / 30 × 100 = 6.666...%`, which rounds to 7% to the nearest whole percent; `21/30 = 70%`, `27/30 = 90%`, and `3/30 = 10%`. A denominator of 31 would give `2/31 × 100 = 6.45%`, which can round to 6%.
- **Necessary inputs available:** The count/percentage pair, multiple neighboring count/percentage pairs, the main-text denominator for gastrointestinal discomfort, and the reported 31 treatment sets among completers on DOC-001 p. 4 are available.
- **Exact missing inputs or definitions:** eTable 4 does not print a denominator for either column, the unit of tabulation for `Any` is not explicitly stated as patient versus treatment-set exposure, and no rounding or truncation rule is supplied. Handling of dropouts and repeated treatment sets in the adverse-reaction denominator is also absent.
- **Source-grounded alternative interpretation:** Placebo `Any` may use 31 treatment-set exposures rather than 30 patients, or the percentage may have been truncated. Either interpretation requires a denominator or rounding convention not printed in eTable 4.
- **Direct observation versus inferred explanation:** `2 (6%)`, the neighboring pairs, and `21 of 30 (70%)` are direct observations. A distinct denominator of 31 or truncation is an inferred explanation.
- **Exact remaining human question:** What exact denominator, analysis unit, and rounding rule produced placebo `Any 2 (6%)`, and were they different from those used for the neighboring rows?

## C005 — Bayesian parameter prose swaps `mu_mex[i]` and `mu_plac[i]` treatment labels

- **Cited location found:** DOC-003 [PDF p. 11](../../../joi180136supp2_prod.pdf#page=11), eMethods 2 code and parameter dictionary; [PDF p. 13](../../../joi180136supp2_prod.pdf#page=13), eMethods 3 code; [PDF p. 14](../../../joi180136supp2_prod.pdf#page=14), eMethods 3 parameter dictionary.
- **Source printed value/text matched:** Both code blocks map `Stiff_Plac[i,t]` to `mu_plac[i]` and `Stiff_Mex[i,t]` to `mu_mex[i]`. Both prose dictionaries describe `mu_mex[i]` as the mean during placebo and `mu_plac[i]` as the mean during mexiletine.
- **Comparator matched:** The real-data definitions identify `Stiff_Plac` as placebo and `Stiff_Mex` as mexiletine. The population parameters `mu.plac` and `mu.mex`, plus `mu.plac - mu.mex`, use the same code-side treatment mapping.
- **Consistency rule applicable:** A parameter's treatment label must agree with the likelihood's data-to-parameter mapping and with the consistently named population parameters.
- **Calculation or logical comparison reproduced:** The likelihood gives `Stiff_Plac -> mu_plac` and `Stiff_Mex -> mu_mex`; substituting the prose labels would instead make placebo observations estimate a parameter described as mexiletine and vice versa. The printed `diff_patient <- mu_plac[i] - mu_mex[i]` is coherent only with the code-side mapping.
- **Necessary inputs available:** The likelihood assignments, real-data definitions, individual-parameter prose, population-parameter prose, and contrast definition are all printed for both models.
- **Exact missing inputs or definitions:** The package lacks the executed WinBUGS model files, run logs, model object names, and posterior output linking the published estimates to a particular code version.
- **Source-grounded alternative interpretation:** The two adjacent individual-parameter prose rows may simply be transposed while the displayed code and population-level definitions retain their intended mapping.
- **Direct observation versus inferred explanation:** The opposite mappings in code and prose are direct observations. A prose-only row transposition and an unaffected executed analysis are inferred explanations.
- **Exact remaining human question:** Which mapping appears in the authoritative executed analysis files, and are only the two prose definitions transposed?

## C006 — `diff_CLCN1` is described as an SCN4A contrast

- **Cited location found:** DOC-003 [PDF p. 13](../../../joi180136supp2_prod.pdf#page=13), eMethods 3 code; [PDF p. 14](../../../joi180136supp2_prod.pdf#page=14), parameter dictionary.
- **Source printed value/text matched:** The code prints `diff_CLCN1 <- mu.plac_CLCN1 - mu.mex_CLCN1`. The dictionary prints `diff_CLCN1 mu.plac - mu.mex for SCN4A patients`.
- **Comparator matched:** The code suffix and both component parameters identify CLCN1, while the prose row identifies SCN4A. The immediately preceding `diff_SCN4A` dictionary row already describes the SCN4A contrast.
- **Consistency rule applicable:** A named genotype contrast must describe the same genotype as its code-defined components and suffix.
- **Calculation or logical comparison reproduced:** Substitution of the code-defined components yields the CLCN1 placebo-minus-mexiletine population contrast; it cannot yield the SCN4A contrast stated in the prose row.
- **Necessary inputs available:** The genotype coding (`1=CLCN1, 0=SCN4A`), subgroup means, code-defined contrasts, and both dictionary rows are printed.
- **Exact missing inputs or definitions:** The package lacks executed model output or a downstream parameter-to-result export showing which label was used outside the displayed code.
- **Source-grounded alternative interpretation:** The `diff_CLCN1` prose row may be a copy-forward of the preceding SCN4A description, with the code and parameter name retaining the intended CLCN1 mapping.
- **Direct observation versus inferred explanation:** The CLCN1 code components and SCN4A prose label are direct observations. A copy-forward documentation error with unaffected analysis is an inferred explanation.
- **Exact remaining human question:** Should the `diff_CLCN1` dictionary row identify CLCN1 patients, and did every downstream output retain that mapping?

## C007 — `sigma.mex` is described as placebo-period variability

- **Cited location found:** DOC-003 [PDF p. 11](../../../joi180136supp2_prod.pdf#page=11) and [PDF p. 12](../../../joi180136supp2_prod.pdf#page=12), eMethods 2 code/dictionary; [PDF p. 13](../../../joi180136supp2_prod.pdf#page=13) and [PDF p. 14](../../../joi180136supp2_prod.pdf#page=14), eMethods 3 code/dictionary.
- **Source printed value/text matched:** In both models, `tau.mex <- 1/(sigma.mex*sigma.mex)`, `mu_mex` is modeled with `tau.mex`, and mexiletine data are modeled with `mu_mex`. Both dictionaries describe `sigma.mex` as variability `during placebo treatment`.
- **Comparator matched:** The parallel `sigma.plac` row is also described as placebo variability, whereas `mu.mex` and `mu.mex_SCN4A`/`mu.mex_CLCN1` are explicitly described as mexiletine-period means.
- **Consistency rule applicable:** The treatment identity of a variability parameter must agree with the likelihood branch and mean parameters whose precision it defines.
- **Calculation or logical comparison reproduced:** `tau.mex = 1/sigma.mex^2` is the precision used for `mu_mex`; `mu_mex` is the latent mean used for `Stiff_Mex`. The displayed model chain therefore associates `sigma.mex` with the mexiletine branch, not the placebo branch.
- **Necessary inputs available:** Both model code blocks, both parameter dictionaries, the real-data treatment definitions, and the parallel `.plac` branch are printed.
- **Exact missing inputs or definitions:** Executed model files, model compilation logs, posterior parameter names, and downstream exports are not supplied.
- **Source-grounded alternative interpretation:** The placebo wording may be a repeated copy-forward from the `sigma.plac` description, while `sigma.mex` remained attached to the mexiletine branch in code.
- **Direct observation versus inferred explanation:** The code chain and placebo prose wording are direct observations. A repeated documentation-only error is an inferred explanation.
- **Exact remaining human question:** What treatment period was `sigma.mex` intended to represent in the executed models and reported output, and should both dictionaries say mexiletine?

## C008 — Main text prints `CLNC1` for the matched `CLCN1` genotype subgroup

- **Cited location found:** DOC-001 [PDF p. 4](../../../jama_stunnenberg_2018_oi_180136.pdf#page=4), Baseline Data and Primary Outcome Measure; [PDF p. 5](../../../jama_stunnenberg_2018_oi_180136.pdf#page=5), Table 1/Figure 2; [PDF p. 6](../../../jama_stunnenberg_2018_oi_180136.pdf#page=6), Figure 3 caption; DOC-003 [PDF p. 4](../../../joi180136supp2_prod.pdf#page=4), eTable 2 footnote.
- **Source printed value/text matched:** The p. 4 result assigns `3.84 (95% CrI, 2.52 to 5.16)` and `n=16` to `CLNC1`. On the same page, Baseline Data names the skeletal muscle chloride channel gene `CLCN1`; Figures 2-3 use `CLCN1` for the n=16 subgroup, and the supplement defines `CLCN1` as the skeletal muscle chloride channel gene.
- **Comparator matched:** The result's estimate, interval, subgroup size, genotype context, and neighboring SCN4A result align with the CLCN1 subgroup shown in the figures and definitions.
- **Consistency rule applicable:** The same genotype subgroup must use one gene symbol; transposing the middle characters creates a different string.
- **Calculation or logical comparison reproduced:** Character comparison gives `CLNC1` versus `CLCN1`; the third and fourth characters are transposed. The matched subgroup size remains `n=16` in the narrative and figures.
- **Necessary inputs available:** The narrative result, same-page gene definition, subgroup size, figure labels, and supplement definition are printed.
- **Exact missing inputs or definitions:** The package lacks the manuscript proof record or author erratum record identifying the intended symbol in that sentence.
- **Source-grounded alternative interpretation:** `CLNC1` is consistent with a local character transposition in a sentence otherwise referring to the CLCN1 subgroup.
- **Direct observation versus inferred explanation:** The two distinct strings and matched subgroup context are direct observations. A local typographical transposition is an inferred explanation.
- **Exact remaining human question:** Should the p. 4 Primary Outcome sentence read `CLCN1`, and does the authoritative proof/source file support that symbol?

## C009 — SF-36 mental-component P value conflicts with the dependent-t 95% CI

- **Cited location found:** DOC-001 [PDF p. 7](../../../jama_stunnenberg_2018_oi_180136.pdf#page=7), Table 2 SF-36 mental-component row; [PDF p. 3](../../../jama_stunnenberg_2018_oi_180136.pdf#page=3) and [PDF p. 4](../../../jama_stunnenberg_2018_oi_180136.pdf#page=4), Statistical Analysis continuation stating dependent t tests for other secondary outcomes and two-sided P values.
- **Source printed value/text matched:** The row prints effect `6.78`, 95% CI `1.64 to 11.92`, and `P=.001`. Table 2 is headed `N=27`; footnote a assigns dependent t tests to non-IVR secondary outcomes.
- **Comparator matched:** The estimate is exactly the interval midpoint, and the printed method, confidence level, sidedness, and table-level N provide the conventional paired-t comparator.
- **Consistency rule applicable:** For the same two-sided dependent-t result, the estimate, symmetric 95% CI, test statistic, degrees of freedom, and P value must be mutually compatible.
- **Calculation or logical comparison reproduced:** With `df=27-1=26`, `t(0.975,26)=2.0555`. The half-width is `(11.92-1.64)/2=5.14`; `SE=5.14/2.0555=2.5006`; `t=6.78/2.5006=2.7114`; the two-sided P value is approximately `.0117`, not `.001`.
- **Necessary inputs available:** Effect, both CI endpoints, confidence level, table-level N, dependent-t label, and two-sided convention are printed.
- **Exact missing inputs or definitions:** The row-specific complete-pair count, raw paired differences, unrounded estimate/CI/P, exact CI-construction implementation, and statistical output are absent.
- **Source-grounded alternative interpretation:** A row-specific analyzed n, a CI or P value produced by a different procedure, or a transcription in one inferential field could exist, but the table does not identify such a departure.
- **Direct observation versus inferred explanation:** The row fields and table/method labels are direct observations. `df=26` assumes the printed N=27 represents 27 complete pairs for this row; the numerical diagnostic is conditional on that table-level assignment. Any different procedure is inferred.
- **Exact remaining human question:** What were the row-specific paired n, unrounded estimate/SE, CI procedure, test statistic, and P value in the authoritative output, and which printed inferential field reflects them?

## C010 — SCN4A fifth handgrip-action-myotonia P value conflicts with its 95% CI

- **Cited location found:** DOC-001 [PDF p. 7](../../../jama_stunnenberg_2018_oi_180136.pdf#page=7), Table 2 fifth handgrip-action-myotonia SCN4A row; [PDF p. 8](../../../jama_stunnenberg_2018_oi_180136.pdf#page=8), Table 2 footnote a; [PDF p. 3](../../../jama_stunnenberg_2018_oi_180136.pdf#page=3), dependent-t method; [PDF p. 4](../../../jama_stunnenberg_2018_oi_180136.pdf#page=4), two-sided P-value convention.
- **Source printed value/text matched:** The SCN4A row prints effect `-1.96`, 95% CI `-3.41 to 0.51`, and `P=.009`. Footnote a prints subgroup `n=11` for the dependent-t treatment effects.
- **Comparator matched:** The row-specific estimate, CI, P value, subgroup n, and test label occupy the same SCN4A row; the adjacent genotype-interaction P value `.04` is separately labeled.
- **Consistency rule applicable:** A conventional two-sided dependent-t 95% CI and two-sided P value for one contrast must imply the same null comparison, and a symmetric t interval must center on its point estimate.
- **Calculation or logical comparison reproduced:** The printed CI crosses zero and has midpoint `(-3.41+0.51)/2=-1.45`, not `-1.96`. Using its half-width `1.96`, `df=10`, and `t(0.975,10)=2.2281` gives `SE=0.8797`, `|t|=2.2281`, and two-sided `P=.0500`, not `.009`.
- **Necessary inputs available:** Effect, CI endpoints, P value, subgroup n, confidence level, test label, and sidedness are printed.
- **Exact missing inputs or definitions:** The exact complete-pair count for this row, raw paired differences, unrounded fields, statistical output, and any nonstandard CI/P implementation are absent.
- **Source-grounded alternative interpretation:** One CI endpoint, the P value, the subgroup n, or the row's method label may be a transcription; the table supplies no separate rule that reconciles the printed set.
- **Direct observation versus inferred explanation:** The zero-crossing interval, off-center midpoint, and `.009` are direct observations. `df=10` and the diagnostic P value follow from applying the printed n=11 dependent-t description; a transcription explanation is inferred.
- **Exact remaining human question:** What exact SCN4A paired sample, estimate, SE, CI endpoints, test statistic, and P value appear in the authoritative fifth-attempt handgrip output?

## C011 — SCN4A fifth transient-paresis estimate, interval, and P value do not form a compatible dependent-t result

- **Cited location found:** DOC-001 [PDF p. 7](../../../jama_stunnenberg_2018_oi_180136.pdf#page=7), Table 2 fifth transient-paresis SCN4A row; [PDF p. 8](../../../jama_stunnenberg_2018_oi_180136.pdf#page=8), Table 2 footnote a; [PDF p. 6](../../../jama_stunnenberg_2018_oi_180136.pdf#page=6), narrative repetition of the same estimate and interval; [PDF p. 3](../../../jama_stunnenberg_2018_oi_180136.pdf#page=3), dependent-t method; [PDF p. 4](../../../jama_stunnenberg_2018_oi_180136.pdf#page=4), two-sided P-value convention.
- **Source printed value/text matched:** Table 2 prints effect `13.71`, 95% CI `-1.96 to 25.47`, and `P=.02` for SCN4A. The p. 6 narrative repeats `13.71 [95% CI, -1.96 to 25.47]`; footnote a prints SCN4A `n=11` for dependent-t effects.
- **Comparator matched:** The effect, CI, P value, subgroup n, and test label refer to the same fifth transient-paresis subgroup row. The separately printed genotype-interaction P value `<.001` is not used as the row P value.
- **Consistency rule applicable:** A conventional two-sided dependent-t 95% CI must center on its estimate and agree with the two-sided test of zero.
- **Calculation or logical comparison reproduced:** The interval crosses zero and has midpoint `(-1.96+25.47)/2=11.755`, not `13.71`. Its half-width is `13.715`; with `df=10`, `SE=13.715/2.2281=6.1554`, `t=13.71/6.1554=2.2273`, and two-sided `P≈.0501`, not `.02`.
- **Necessary inputs available:** Effect, both endpoints, P value, subgroup n, test family, confidence level, and two-sided convention are printed.
- **Exact missing inputs or definitions:** Raw paired differences, row-specific complete cases, unrounded values, output tables, and exact CI/P implementation are not supplied.
- **Source-grounded alternative interpretation:** If the lower endpoint were positive `1.96`, the interval midpoint would be `13.715`, almost exactly the printed effect. That sign alternative is consistent with a local endpoint transcription, although the rounded dependent-t diagnostic would still require the authoritative output to assess `P=.02`.
- **Direct observation versus inferred explanation:** The repeated negative lower endpoint, off-center interval, zero crossing, and `.02` are direct observations. A missing plus sign or another inferential-field transcription is an inferred explanation.
- **Exact remaining human question:** What are the authoritative lower CI endpoint, row-specific paired n, SE/test statistic, and P value for the SCN4A fifth transient-paresis contrast?

## C012 — Myotonic-discharge P value conflicts with the dependent-t 95% CI

- **Cited location found:** DOC-001 [PDF p. 8](../../../jama_stunnenberg_2018_oi_180136.pdf#page=8), Table 2 continuation myotonic-discharge row and footnotes; [PDF p. 3](../../../jama_stunnenberg_2018_oi_180136.pdf#page=3), dependent-t method; [PDF p. 4](../../../jama_stunnenberg_2018_oi_180136.pdf#page=4), two-sided P-value convention.
- **Source printed value/text matched:** The row prints placebo mean `2.52 (0.89)`, mexiletine mean `1.85 (1.13)`, effect `0.67`, 95% CI `0.23 to 1.11`, and `P<.001`. Table 2 is headed `N=27`, and footnote a assigns dependent t tests to non-IVR secondary outcomes.
- **Comparator matched:** `2.52-1.85=0.67` matches the effect, so the row direction and point estimate are internally aligned; the inferential comparator is its own CI and printed two-sided dependent-t method.
- **Consistency rule applicable:** A two-sided dependent-t 95% CI and two-sided P value for the same effect and sample must correspond to the same standard error and test statistic.
- **Calculation or logical comparison reproduced:** The estimate is the interval midpoint. With `df=26`, half-width `(1.11-0.23)/2=0.44`, `SE=0.44/2.0555=0.2141`, `t=0.67/0.2141=3.1300`, and two-sided `P≈.0043`, not below `.001`.
- **Necessary inputs available:** Period means, effect, CI endpoints, confidence level, table-level N, dependent-t label, and two-sided convention are printed.
- **Exact missing inputs or definitions:** The row-specific complete-pair count, paired-difference SD, raw pairs, unrounded result fields, exact test/CI implementation, and output are absent.
- **Source-grounded alternative interpretation:** The P value may arise from a different analysis or sample than the printed CI, or one inferential field may be transcribed; no such row-specific departure is stated.
- **Direct observation versus inferred explanation:** The means, estimate, interval, P threshold, and method labels are direct observations. `df=26` follows from treating the Table 2 N=27 as complete paired observations for this row; any different procedure or sample is inferred.
- **Exact remaining human question:** What row-specific paired n, paired-difference SD/SE, test statistic, CI method, and exact P value appear in the authoritative myotonic-discharge analysis output?

## C013 — First handgrip placebo-period interval is reversed and excludes its estimate

- **Cited location found:** DOC-001 [PDF p. 7](../../../jama_stunnenberg_2018_oi_180136.pdf#page=7), Table 2, Handgrip action myotonia, First attempt, Change Placebo Period column.
- **Source printed value/text matched:** The row prints placebo-period change `0.46 (-0.30 to -1.23)`. In the same row, the mexiletine-period change is `-2.39 (-4.22 to -0.55)` and the treatment effect is `-2.85 (-5.28 to -0.42)`.
- **Comparator matched:** The estimate `0.46` and endpoints `-0.30` and `-1.23` occupy the same placebo-period change cell. The adjacent mexiletine and treatment-effect cells are aligned to the same first-attempt handgrip row.
- **Consistency rule applicable:** A displayed interval must have a lower endpoint no greater than its upper endpoint and must contain its corresponding point estimate.
- **Calculation or logical comparison reproduced:** As printed, `-0.30 > -1.23`, so the endpoints are reversed. Reordering them to `-1.23 to -0.30` still leaves `0.46` outside the interval because `0.46 > -0.30`. The row arithmetic `-2.39 - 0.46 = -2.85` exactly reproduces the printed treatment effect and independently supports the printed placebo estimate under the Table 2 change-score direction.
- **Necessary inputs available:** The placebo estimate, both interval endpoints, column header, row label, mexiletine estimate, and treatment-effect estimate are printed and visually aligned.
- **Exact missing inputs or definitions:** The package lacks the raw paired placebo changes, row-specific complete-pair count, standard error, unrounded estimate and interval, CI calculation output, and proof history for this cell.
- **Source-grounded alternative interpretation:** Reversing the endpoints alone cannot reconcile the cell. If the second endpoint were positive `1.23`, the ordered interval `-0.30 to 1.23` would contain `0.46`; alternatively, another endpoint value may have been intended. The exact treatment-effect arithmetic makes an interval-field transcription more source-compatible than changing `0.46`, but that remains an inference without the analysis output.
- **Direct observation versus inferred explanation:** The reversed endpoints, the position of `0.46` outside either ordering, and exact row arithmetic are direct observations. A missing positive sign or another interval transcription is an inferred explanation.
- **Exact remaining human question:** What exact placebo-period first-handgrip estimate, lower and upper CI endpoints, standard error, and paired n appear in the authoritative analysis output?

## C014 — Mean Timed Up&Go placebo-period estimate lies outside its interval

- **Cited location found:** DOC-001 [PDF p. 7](../../../jama_stunnenberg_2018_oi_180136.pdf#page=7), Table 2, Timed Up&Go, Mean, Change Placebo Period column.
- **Source printed value/text matched:** The row prints placebo-period change `0.07 (-0.67 to 0.01)`. The same row prints mexiletine-period change `-1.05 (-1.48 to -0.62)` and treatment effect `-1.12 (-2.07 to -0.18)`.
- **Comparator matched:** The estimate `0.07` and interval `-0.67 to 0.01` occupy the same placebo-period change cell. The adjacent mexiletine and treatment-effect fields are aligned to the same mean Timed Up&Go row.
- **Consistency rule applicable:** A point estimate must lie within its corresponding displayed interval when both summarize the same result.
- **Calculation or logical comparison reproduced:** The interval is ordered, but `0.07 > 0.01`, so the estimate exceeds the upper endpoint by `0.06`. The change-score arithmetic `-1.05 - 0.07 = -1.12` exactly reproduces the printed treatment effect, supporting the printed `0.07` estimate under the Table 2 direction.
- **Necessary inputs available:** The placebo estimate, both endpoints, row and column labels, mexiletine estimate, and treatment-effect estimate are printed and visually aligned.
- **Exact missing inputs or definitions:** The package lacks raw paired changes, the row-specific complete-pair count, standard error, unrounded estimate and interval, exact CI output, and manuscript proof history for this cell.
- **Source-grounded alternative interpretation:** The upper endpoint may contain a missing digit or other transcription because the point estimate participates exactly in the printed treatment-effect arithmetic. A negative estimate `-0.07` would lie within the printed interval, but with the rounded mexiletine change it would imply `-1.05 - (-0.07) = -0.98`, not the printed `-1.12`; therefore an estimate-sign explanation would require at least one additional field difference.
- **Direct observation versus inferred explanation:** The estimate's position above the interval, the `0.06` gap, and the exact row arithmetic are direct observations. A missing endpoint digit or estimate-sign transcription is an inferred explanation.
- **Exact remaining human question:** What exact placebo-period mean Timed Up&Go estimate, CI endpoints, standard error, and paired n appear in the authoritative analysis output?

## Recheck summary

- **Stable-ID scope:** 14/14 IDs covered (`C001`-`C014`), with one section per ID.
- **Appended-ID recheck:** Complete for both newly registered IDs (`C013` and `C014`) against DOC-001 physical PDF p. 7.
- **Source-location count:** 14/14 candidate locations resolved to supplied-source pages; the preliminary C004 locator defect was repaired in the canonical ledger (DOC-001 physical PDF p. 8).
- **Source printed-field match count:** 14/14 candidate statements were found as currently registered.
- **Comparator match count:** 14/14 comparators were located and matched to the same population, row, parameter, measure, or result cell as applicable.
- **Calculation/logical-comparison count:** 14/14 candidate rules were mechanically reproduced from the supplied fields. The four dependent-t diagnostics use the table-level N/subgroup n and are explicitly conditional where row-specific complete-pair counts are not printed; C013-C014 use direct interval ordering/containment and same-row arithmetic.
- **Unresolved items:** Each ID retains the exact human question stated in its section. Common missing material is row-level data, unrounded statistical output, executed Bayesian model files/output, explicit adverse-event denominators, and the INQoL scoring definition.
- **Derivative/source handling:** Fresh derivatives were used as locators only. No additional preprocessing derivative was created.
