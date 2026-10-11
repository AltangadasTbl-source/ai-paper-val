# Statistical consistency pass 1 — main shard

- Runtime ID: /root/statistics_pass_1_main.
- Named preset: qc16_statistical_consistency_reviewer.
- Model and effort: gpt-6.1-sol / high.
- Start mode: FRESH_SPAWN.
- Exact source scope: DOC-001 jama_huffman_2018_oi_170166.pdf, physical pp.1-12, REPORT.
- Exact relationship scope: S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080.
- Relationships completed: 80 groups; every internal interval/point/graphical cell included.
- Local discovery records: 10, STAT-M01 through STAT-M10. Stable C IDs are assigned only by the coordinator.
- All records remain Pending Human Adjudication.

## Coverage and source procedure

Every relationship has an explicit PASS_1_COMPLETE entry in statistics/relationship_inventory.md. All estimates lie inside their own ordered displayed intervals. Every binary adjusted RD sign agrees with the accompanying OR direction within its model. Every subgroup forest estimate/interval agrees with its numeric row and favors-direction label. The graph scope contains 60 points and 60 CI bars, checked visually rather than replaced with inferred counts or binomial intervals.

Full interval scope: Table1 27 difference intervals; Table2 38 estimable intervals plus four nonestimable cells; Table3 40 intervals; Figure3 28 intervals. These are 133 distinct table/forest interval cells, plus 60 graphical bars. Abstract and narrative repetitions are checked separately under S001, S051, S064 and S079; background uncertainty under S080. Every no-candidate group is explicitly retained in the inventory. There is no finding cap.

Direct PDF text was inspected using pdftotext -layout selected pages with Poppler25.03.0; reusable native/layout and source-bound DOC-001 pp.6-9 images served as locators and visual evidence. A fresh targeted page2 render confirms the Key Points wording: command pdftoppm -f 2 -l 2 -singlefile -scale-to 1800 -png jama_huffman_2018_oi_170166.pdf .ai_paper_validation/review_1_6/preprocessing/stat-main-p2. Engine Poppler25.03.0; derivative preprocessing/stat-main-p2.png; exact source DOC-001p2. No other new extraction/OCR was required. No source or reused artifact was modified.

Each discovery below records every compared location and document role by content. All discrepancies concern REPORT locations within the main article. Where DOC-004eTable7 is mentioned it corroborates the intended distinction between odds ratio and risk difference; it is not a conflicting comparator and creates no extra discrepancy relationship.

## STAT-M01 — Inpatient beta-blocker risk-difference CI upper bound differs in prose

- Relationships: S034, S051.
- Compared location A: DOC-001 REPORT, Table2 inpatient beta-blocker row, jama_huffman_2018_oi_170166.pdf#page=6.
- Compared location B: DOC-001 REPORT, Participants/process paragraph, last paragraph of physical p6, jama_huffman_2018_oi_170166.pdf#page=6.
- Exact source values: Table2 adjusted difference6.25% (95%CI4.10 to8.40); prose adjusted risk difference6.25% (95%CI4.10%-8.10%). OR1.46 (1.29-1.65) repeats identically.
- Direct observation: the same printed intervention-versus-control process effect has different upper CI endpoints.
- Reproducible rule/calculation: after outcome, adjustment, contrast and population matching, repeated CI endpoints should agree at the same displayed precision. 8.40-8.10=0.30 percentage points. Under ordinary rounding to two decimals the respective rounding bands do not overlap; no such rounding rule is presumed necessary for observing the printed difference.
- Definitions available: Table2 hospital/time adjustment and eligible participants; same process paragraph explicitly references Table2.
- Missing inputs: full fitted-model output, CI algorithm and any undisclosed alternative analysis for prose.
- Alternative source-grounded interpretation: a prose transcription error, table transcription error, or an unlabelled alternative output. Package evidence does not identify which.
- Human question: which upper endpoint belongs to the reported adjusted inpatient beta-blocker result, and did the prose intentionally use a different analysis?
- Potential reuse: a reader extracting the CI from prose versus table could record a different upper bound; no conclusion effect is asserted.
- Candidate status: Pending Human Adjudication.

## STAT-M02 — Discharge beta-blocker adjusted risk difference differs in prose

- Relationships: S047, S051.
- Compared location A: DOC-001 REPORT, Table2 discharge beta-blocker row, jama_huffman_2018_oi_170166.pdf#page=6.
- Compared location B: DOC-001 REPORT, process paragraph describing discharge beta-blocker use, jama_huffman_2018_oi_170166.pdf#page=7.
- Exact source values: Table2 adjusted difference6.69% (95%CI4.43 to8.95); prose adjusted risk difference6.63% (95%CI4.43%-8.95%). The same eligible discharge process is described.
- Direct observation: repeated point estimates differ; CI bounds agree.
- Reproducible rule/calculation: matched same-result point estimates at two decimals should agree. 6.69-6.63=0.06 percentage points. CI midpoint (4.43+8.95)/2=6.69 is a descriptive diagnostic, not proof of a Wald CI or proof that the table is the intended estimate.
- Missing inputs: fitted-model output, CI construction and any unreported alternate analysis.
- Alternative source-grounded interpretation: one occurrence may be a transcription error; asymmetric intervals are possible, so midpoint equality does not decide the intended result.
- Human question: which point estimate is intended for this adjusted risk difference, and are the table and prose meant to repeat exactly the same result?
- Candidate status: Pending Human Adjudication.

## STAT-M03 — Discharge beta-blocker adjusted odds ratio differs in prose

- Relationships: S047, S051.
- Compared location A: DOC-001 REPORT, Table2 discharge beta-blocker row, jama_huffman_2018_oi_170166.pdf#page=6.
- Compared location B: DOC-001 REPORT, discharge beta-blocker process paragraph, jama_huffman_2018_oi_170166.pdf#page=7.
- Exact source values: Table2 OR1.48 (95%CI1.30-1.68); prose adjusted OR1.47 (95%CI1.30-1.68).
- Direct observation: same displayed odds-ratio result differs by0.01 while both interval bounds agree.
- Rule/calculation: match outcome, contrast, discharge eligibility and hospital/time adjustment before comparing printed estimates;1.48-1.47=0.01. Both estimates remain within the CI, so this is a repetition issue rather than containment.
- Missing inputs: unrounded estimate, rounding algorithm, fitted-model output and any alternative output alignment.
- Alternative source-grounded interpretation: a transcription difference, or a last-digit rounding difference at a boundary under different rounding procedures. The package does not state an identical rounding algorithm, so a rounding explanation cannot be excluded solely from adjacent final digits.
- Human question: which printed OR is intended, or was a distinct rounding procedure/output used in prose?
- Candidate status: Pending Human Adjudication.

## STAT-M04 — Table2 describes odds ratios as differences in marginal effects

- Relationships: S002 and binary Table2 rows S030, S031, S032, S033, S034, S035, S036, S038, S039, S041, S043, S044, S045, S046, S047, S048, S049.
- Compared location A: DOC-001 REPORT, Table2 right-column heading 'Odds Ratio or β-Coefficient (95% CI)' and binary effect cells, jama_huffman_2018_oi_170166.pdf#page=6.
- Compared location B: DOC-001 REPORT, Table2 footnote b, jama_huffman_2018_oi_170166.pdf#page=6.
- Exact source statement: 'Odds ratios and β-coefficients represent effect of intervention compared with control and are calculated as the difference in marginal effects (intervention group minus control group)' in the labelled mixed-effects logistic/quantile model.
- Comparator: Table2 prints distinct difference and odds-ratio columns, e.g. prehospital aspirin difference3.80% versus OR1.40; prose labels these as risk difference and OR respectively on p6.
- Direct observation: the footnote gives the difference-in-marginal-effects calculation to the odds ratios, whereas the column and narrative call them odds ratios.
- Rule/calculation: a risk difference is a subtraction on the probability scale, with null0; an odds ratio is a ratio on the odds scale, with null1. The column values3.80% and1.40 are properly different quantities, so their inequality itself is not an arithmetic error. The discrepancy is the footnote's effect-measure definition. A log-odds contrast could equal log(OR), not the labelled OR itself; no underlying model transformation is assumed.
- Corroboration only: DOC-004 REPORT eTable7 footnote, joi170166supp3_prod.pdf#page=23, explicitly assigns difference in marginal effects to risk difference while odds ratios represent the intervention effect. This supports a possible omitted phrase in main but is not a discrepant source.
- Missing inputs: intended footnote wording and precise reporting transformation for coefficients.
- Alternative interpretation: the wording may have omitted 'risk differences' or mistakenly attached the calculation phrase to ORs; this does not establish that the fitted numerical ORs are wrong.
- Human question: which quantity does the difference-in-marginal-effects phrase define, and how should the printed OR column be distinguished from that quantity?
- Candidate status: Pending Human Adjudication.

## STAT-M05 — Table3 describes odds ratios as differences in marginal effects

- Relationships: S002, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061.
- Compared location A: DOC-001 REPORT, Table3 cluster-adjusted/primary odds-ratio headings and cells, jama_huffman_2018_oi_170166.pdf#page=7.
- Compared location B: DOC-001 REPORT, Table3 footnote a, jama_huffman_2018_oi_170166.pdf#page=7.
- Exact source statement: 'Odds ratios represent effect of intervention compared with control and are calculated as the difference in marginal effects (intervention group minus control group)' in mixed-effects logistic regression.
- Comparator: Table3 separately displays risk-difference and OR columns. Primary MACE difference-0.09% versus OR0.98; primary analysis prose p7 explicitly labels these risk difference and odds ratio.
- Direct observation: the footnote attributes a subtraction-of-marginal-effects calculation to the labelled odds ratios.
- Rule/calculation: subtraction on the probability scale has null0; ratio on odds scale has null1. The printed RD and OR are not required to be equal. The mismatch is between the definition statement and measure labels, independently of p-value conventions or covariance.
- Corroboration only: DOC-004 REPORT eTable7 footnote on joi170166supp3_prod.pdf#page=23 differentiates odds ratios and marginal risk differences; it is not a conflicting comparator for this candidate.
- Missing inputs: intended wording and model-derived marginalization output.
- Alternative interpretation: the phrase may be intended to define the difference columns rather than ORs, with omitted text; no numerical model error is inferred.
- Human question: does this footnote intend to define the risk-difference columns, and what definition was intended for the OR columns?
- Candidate status: Pending Human Adjudication.

## STAT-M06 — Tobacco-counselling greater-than95% claim versus94.7% table value

- Relationships: S051, S061.
- Compared location A: DOC-001 REPORT, process paragraph immediately above Primary Analysis, jama_huffman_2018_oi_170166.pdf#page=7.
- Compared location B: DOC-001 REPORT, Table3 tobacco cessation advice row, jama_huffman_2018_oi_170166.pdf#page=7.
- Exact source statement: 'Rates of discharge second antiplatelet use and tobacco cessation counseling were high (>95%) and similar between groups.'
- Exact comparator: tobacco advice control3526 (96.0%), intervention2618 (94.7%); footnote e limits the tobacco row to discharged baseline smokers.
- Direct observation: intervention tobacco-counselling94.7% is below the stated>95% threshold.
- Rule/calculation:94.7<95, with gap0.3 percentage points to95; one-decimal rounding cannot turn an underlying percentage rounding to94.7 into>95. Literal> is retained, rather than replaced with 'approximately'.
- Missing inputs: whether prose>95% was intended to apply separately to both measures and both groups, or to some other summary not labelled.
- Alternative interpretation: 'high' may be an approximate characterization or the threshold may have been intended for discharge second antiplatelet alone. Main text grammatically attaches the parenthesis to both listed measures.
- Human question: does>95% apply to tobacco counselling in each group, and if so how does that claim relate to intervention94.7%?
- Inferential distinction: the adjusted tobacco effect has null-containing intervals, so 'similar' is not the registered discrepancy.
- Candidate status: Pending Human Adjudication.

## STAT-M07 — Door-to-balloon adjusted difference versus beta under shared effect definition

- Relationship: S040.
- Compared location A: DOC-001 REPORT, Table2 door-to-balloon time row, Difference,% column6.18 (95%CI-4.78 to17.14), jama_huffman_2018_oi_170166.pdf#page=6.
- Compared location B: DOC-001 REPORT, same row beta-coefficient13.00 (95%CI3.64-22.36), footnotes b/c, jama_huffman_2018_oi_170166.pdf#page=6.
- Source context: outcome is median door-to-balloon time in minutes, control65/intervention77; b defines beta as intervention-minus-control difference in marginal effects from a hospital/time-adjusted model, c labels the second estimate beta.
- Direct observation: the printed adjusted estimates are6.18 and13.00 with different intervals, under the same row/model heading and a shared calculation footnote.
- Conditional rule/calculation: if both represent the same untransformed intervention-minus-control quantile contrast,13.00-6.18=6.82 and they cannot be the same point estimate at printed precision. This identity premise is conditional; no model or estimand mapping is inferred from statistical convention. The table itself supplies the shared difference wording but gives a percent heading for one column.
- Missing definitions: exact estimand, scale, adjustment/marginalization transformation and percent-change denominator for each column. No source explains a percent transformation or distinct time estimands.
- Alternative source-grounded interpretation:6.18 could be a percent or distinct marginal summary and13.00 a minute coefficient; alternatively one entry or its label may differ from the intended output. The two columns may be coherent once the missing mapping is supplied.
- Human question: which estimand and scale does each adjusted time entry represent, and does the footnote intend the same intervention-minus-control quantile contrast for both?
- Inferential limit: one CI includes0 and the other excludes0, but this is not asserted as a same-test incompatibility without compatible variance/estimand definitions.
- Candidate status: Pending Human Adjudication.

## STAT-M08 — Door-to-needle adjusted difference versus beta under shared effect definition

- Relationship: S042.
- Compared location A: DOC-001 REPORT, Table2 door-to-needle time row, Difference,% column0.40 (95%CI-5.23 to6.03), jama_huffman_2018_oi_170166.pdf#page=6.
- Compared location B: DOC-001 REPORT, same row beta-coefficient5.00 (95%CI-5.20-15.20), footnotes b/c, jama_huffman_2018_oi_170166.pdf#page=6.
- Source context: median time in minutes, control44/intervention45; b attributes the difference-in-marginal-effects calculation to beta and c labels the beta coefficient.
- Direct observation: adjusted entries0.40 and5.00 differ despite a shared row/model heading/calculation description.
- Conditional rule/calculation: if both intend the same untransformed intervention-minus-control time quantile contrast,5.00-0.40=4.60; printed precision cannot make them identical. That identity premise is conditional on the supplied definitions, not inferred from convention.
- Missing definitions: column-specific estimand, scale, covariance/variance construction, transformation and any percent-change denominator.
- Alternative interpretation: percent/marginal and minute/coefficient summaries could differ coherently; missing labelling rather than a numerical discrepancy could explain the two values.
- Human question: what estimand and scale generates each entry, and is the common difference definition intended for both?
- Inferential limit: both intervals include0; no P or same-test inference is reconstructed.
- Candidate status: Pending Human Adjudication.

## STAT-M09 — Key Points duplicates negation in the statistical-significance statement

- Relationship: S001.
- Compared location A: DOC-001 REPORT, Key Points Findings, jama_huffman_2018_oi_170166.pdf#page=2.
- Compared location B: DOC-001 REPORT, abstract Results, jama_huffman_2018_oi_170166.pdf#page=1; primary analysis narrative, jama_huffman_2018_oi_170166.pdf#page=7.
- Exact source A: 'a difference that did not reach not statistical significance after adjustment for cluster and temporal trends.'
- Exact source B: abstract 'was not statistically significant after adjustment'; primary text states 'was not statistically significant after further adjustment for temporal trends.'
- Matched numerical result: primary RD-0.09% (-1.32 to1.14), OR0.98 (0.80-1.21).
- Direct observation: Key Points prints two negations, 'did not' and 'not statistical significance', where the other matched-result statements use one negation.
- Rule/logical diagnostic: literally negating a nonsignificance phrase can invert or obscure the nonsignificance interpretation. This is an ambiguity in a supplied statistical-result label; it is not a reanalysis or claim that the result is significant.
- Missing inputs: intended edited wording. No unreported model definition is needed to observe the duplicated source word.
- Alternative source-grounded interpretation: this is an accidental duplicated 'not' and the intended meaning is the same nonsignificant result as abstract/main text. Key Points Meaning also says the intervention did not reduce the MACE rate.
- Human question: is the duplicated negation intended, or should the Key Points significance statement express the same nonsignificance as the matched abstract/main result?
- Source confirmation: direct page2 native/layout and fresh Poppler page2 raster show the two occurrences.
- Candidate status: Pending Human Adjudication.

## STAT-M10 — Percentage heading over the two minute-based adjusted time rows

- Relationships: S040, S042.
- Compared location A: DOC-001 REPORT, Table2 common 'Difference, % (95% CI)' heading, jama_huffman_2018_oi_170166.pdf#page=6.
- Compared location B: DOC-001 REPORT, Table2 door-to-balloon and door-to-needle row labels 'median (IQR), min', together with footnote b difference-in-marginal-effects definition, jama_huffman_2018_oi_170166.pdf#page=6.
- Exact values under the percent heading: door-to-balloon6.18 (-4.78 to17.14); door-to-needle0.40 (-5.23 to6.03). Second time-effect column is beta, explicitly flagged by c.
- Direct observation: one common percent effect heading covers outcomes explicitly labelled in minutes; the source does not specify a transformation/denominator that turns the defined time difference into a percentage.
- Conditional label rule: an untransformed difference of minute-valued outcomes has minute units, whereas a relative percent effect requires an explicitly identifiable dimensionless transformation or baseline. No assumption is made that the source actually used untransformed differences.
- Missing definitions: whether the common percent heading applies to time rows or only binary process rows; the time-difference scale and any relative-change transformation/baseline.
- Alternative interpretation: the heading may be a common template with an implicit exception for time rows, or the difference column may indeed be percent-valued with a missing transformation definition. The beta point-estimate identity questions in STAT-M07/08 remain separate printed-value/comparator relationships.
- Human question: are these two entries in minutes or percent, and if percent, what supplied estimand/transformation does the label designate?
- Candidate status: Pending Human Adjudication.

## Missing definitions and diagnostic boundaries

S079 is not turned into a CI/P candidate. Main P<.001 accompanies troponin medians1.3 versus4.6; eTable1 difference3.3 (95%CI0.1 to6.5) is compatible in direction. The exact test, sidedness, CI method and troponin-specific denominators are not supplied. A normal-tail approximation from CI width would answer a different, unsupported same-test assumption. No such numerical approximation is presented as a contradiction. Numeric reviewer NUM17 independently records Figure1 lost-box total275 versus main incomplete295; neither group count is a troponin measurement denominator.

S064 expanded MACE point estimates are lower; the source calls findings hypothesis-generating and allows chance. Its primary RD interval includes0 and printed OR upper bound is1.00. No explicit source claim of statistically significant time-adjusted benefit was found, and a rounded endpoint does not establish exact tail probability; no candidate is emitted solely from this combination.

Table1 creatinine0.0 (0.0 to0.0) is coherent rounding at one decimal, not proof of an exact zero-width underlying interval. No coherent display-zero P value appears in assigned main results. If encountered, its coverage label is DISPLAY_ZERO_NOT_CANDIDATE and it is not registered unless an independent source contradiction exists.

Secondary modelling and covariance details are insufficient to demand identical CI null crossing for RD and OR. None of the main realized test statistics or SEs is printed. The reviewer does not infer sidedness, degrees of freedom, covariance, variance estimator, multiplicity, denominator, model or estimand mapping from convention.

## Completion

Pass1 is complete for every S001-S080 record and all its constituent cells/repetitions/graphical bars. Ten local candidate records retain exact supplied locations and document roles, direct observations, conditional diagnostics where required, named missing definitions, alternatives and human questions. The coordinator will merge genuine duplicates across lanes and assign stableCIDs; pass2 requires a different fresh high-effort agent after the full ledger/recheck. No severity, validity, evidence state, disposition or correction is assigned here.


# Coordinator canonical merge: complete support pass 1

Complete main and support statistical coverage is 161 stable relationships; the appended support part is disjoint. Each original agent part is preserved with its runtime identifier. No local candidate is removed by this merge. Source-link traversal depth is normalized below.

# Statistical pass 1 — complete support shard

Agent /root/statistics_pass_1_support, fresh gpt-6.1-sol/high execution. Scope DOC-002 protocol32pages, DOC-003 SAP9pages, DOC-004 mixed bundle27pages: all68pages considered through the complete source-linked support map; every support inference, PLAN definition, historical OR, percentile display and REPORT graphical CI group checked. Main quantitative map read only for exact matching locators/definitions. Own stable records S201-S281:81records containing all135explicit numeric interval cells. Local candidates2, STAT-S01/STAT-S02. No count cap was applied. Inventory: statistics/parts/support_relationship_inventory.md.

## Procedure and source authority

Read QUALITY_CONTROL_SCOPE.md, PERFORMANCE_PROFILE.md, complete review contract/report specification/settings, routing/tooling/source inventory/coverage, full support map and all annex table cells. No old checker, candidate ledger, disposition or final-report conclusions were used. Existing native/layout source-bound extraction and rendered pages served as locators. Direct pdftotext25.03.0 to stdout confirmed DOC-004 p17andp1 against current PDF. Current main pp3and7were consulted only for matching statistical definitions. Source-bound full-page images DOC-004 p5andpp24-27 were visually reviewed; all graphical groups and their point/interval ordering, zero reference, axes and caption directions were considered. Existing image engine/provenance is in evidence_asset_inventory.md. No new derivative, OCR, Python helper or GPU invocation was needed.

Applied checks: point-estimate containment, ordered endpoints, OR positive scale/null1, RD/continuous-difference null0, contrast/reference direction, narrative direction, confidence level and model labels, complete repeated rows/cells, matching across tables/prose/figures after population/model/estimand matching. Every explicit numeric estimate is within its displayed interval and every endpoint pair is ordered. Missing inferential definitions are named in the inventory; none automatically becomes a candidate. P/CI/test/statistic/SE reconciliation is unavailable where supplied evidence lacks the same test, sidedness, estimator, covariance or measurement n. No convention-only reconstruction was used.

No support source displays a zero P value. Display zeros would be DISPLAY_ZERO_NOT_CANDIDATE in otherwise coherent results; no probability was derived to criticize such notation. Zero event points, collapsed rounded intervals, rounded null1limits and zero risk differences are different quantities and were checked in their own context.

## Record-by-record pass coverage

Every row below is a completed check, including definition-only/no-applicable-test records. Its full values, locations, model and specific limitations are preserved under the same stable ID in the companion inventory. Shared table-level rules apply to every constituent cell.

| ID | Checked relationship | Pass result |
|---|---|---|
| S201 | Sample-size/power/ICC/allowance definitions and repetitions | PASS_1_COMPLETE; no reconstructed power |
| S202 | ITT and assigned exposure / random effects | PASS_1_COMPLETE; no realized test |
| S203 | Missing-data/complete-case/imputation definitions | PASS_1_COMPLETE; measurement n and imputation specifications absent |
| S204 | Primary hospital/time model and GRACE sensitivity | PASS_1_COMPLETE; distinct fitted models retained |
| S205 | Prespecified subgroup definitions, age65boundary | PASS_1_COMPLETE; no inferred membership/test |
| S206 | Secondary clinical/process definitions/model labels | PASS_1_COMPLETE; disclosed inpatient statin omission retained |
| S207 | QoL/economics/concordance/implementation analyses | PASS_1_COMPLETE; no numeric inference supplied |
| S208 | Interim/final z and alpha thresholds | PASS_1_COMPLETE; no realized statistics or inferred spending implementation |
| S209 | Historical OR1.01(.92,1.10) | PASS_1_COMPLETE; contained/ordered/null-compatible |
| S210 | R3M/percentile schematic definitions | PASS_1_COMPLETE; percentiles distinguished from CI |
| S211 | Toolkit all-MI composite panel1 | PASS_1_COMPLETE; all five percentiles/annotations/months |
| S212 | Toolkit STEMI composite panel2 | PASS_1_COMPLETE; all five percentiles/annotations/months |
| S213 | Toolkit NSTEMI composite panel3 | PASS_1_COMPLETE; all five percentiles/annotations/months |
| S214 | Toolkit discharge composite panel4 | PASS_1_COMPLETE; all five percentiles/annotations/months |
| S215 | Toolkit arrival aspirin panel5 | PASS_1_COMPLETE; all five percentiles/annotations/months |
| S216 | Toolkit discharge aspirin panel6 | PASS_1_COMPLETE; all five percentiles/annotations/months |
| S217 | Toolkit discharge beta-blocker panel7 | PASS_1_COMPLETE; all five percentiles/annotations/months |
| S218 | Toolkit ECG panel18 labels/percentiles | PASS_1_COMPLETE; label/timeframe numeric lane implications retained |
| S219 | Other toolkit graphs/definitions/checklists | PASS_1_COMPLETE; no inferential CI/P/SE/statistic supplied |
| S220 | eTable1age | PASS_1_COMPLETE; contained/ordered; STAT-S01 shared footnote |
| S221 | eTable1male | PASS_1_COMPLETE; contained/ordered; STAT-S01 shared footnote |
| S222 | eTable1tobacco | PASS_1_COMPLETE; contained/ordered; STAT-S01 shared footnote |
| S223 | eTable1diabetes | PASS_1_COMPLETE; contained/ordered; STAT-S01 shared footnote |
| S224 | eTable1transfer | PASS_1_COMPLETE; contained/ordered; STAT-S01 shared footnote |
| S225 | eTable1uninsured | PASS_1_COMPLETE; contained/ordered; STAT-S01 shared footnote |
| S226 | eTable1STEMI | PASS_1_COMPLETE; contained/ordered; STAT-S01 shared footnote |
| S227 | eTable1symptom-door | PASS_1_COMPLETE; contained/ordered; rounding-compatible20vs21; STAT-S01 |
| S228 | eTable1weight | PASS_1_COMPLETE; contained/ordered; STAT-S01 shared footnote |
| S229 | eTable1SBP | PASS_1_COMPLETE; contained/ordered; STAT-S01 shared footnote |
| S230 | eTable1heart rate | PASS_1_COMPLETE; contained/ordered; STAT-S01 shared footnote |
| S231 | eTable1troponin | PASS_1_COMPLETE; contained/ordered; main P<.001same-test mapping absent; STAT-S01 |
| S232 | eTable1LDL | PASS_1_COMPLETE; contained/ordered; STAT-S01 shared footnote |
| S233 | eTable1triglycerides | PASS_1_COMPLETE; contained/ordered; STAT-S01 shared footnote |
| S234 | eTable1creatinine | PASS_1_COMPLETE; contained/ordered; rounding-compatible0vs.1; STAT-S01 |
| S235 | eTable1glucose | PASS_1_COMPLETE; contained/ordered; STAT-S01 shared footnote |
| S236 | eTable1hemoglobin | PASS_1_COMPLETE; contained/ordered; STAT-S01 shared footnote |
| S237 | eTable2age arms and contrast | PASS_1_COMPLETE; all3CIs contained/ordered |
| S238 | eTable2male arms and contrast | PASS_1_COMPLETE; all3CIs contained/ordered |
| S239 | eTable2tobacco arms and contrast | PASS_1_COMPLETE; all3CIs contained/ordered |
| S240 | eTable2diabetes arms and contrast | PASS_1_COMPLETE; all3CIs contained/ordered |
| S241 | eTable2transfer arms and contrast | PASS_1_COMPLETE; all3CIs contained/ordered |
| S242 | eTable2uninsured arms and contrast | PASS_1_COMPLETE; all3CIs contained/ordered |
| S243 | eTable2STEMI arms and contrast | PASS_1_COMPLETE; all3CIs contained/ordered |
| S244 | eTable2symptom-door arms and contrast | PASS_1_COMPLETE; all3CIs contained/ordered |
| S245 | eTable2weight arms and contrast | PASS_1_COMPLETE; all3CIs contained/ordered |
| S246 | eTable2SBP arms and contrast | PASS_1_COMPLETE; all3CIs contained/ordered |
| S247 | eTable2heart rate arms and contrast | PASS_1_COMPLETE; all3CIs contained/ordered |
| S248 | eTable2troponin arms and contrast | PASS_1_COMPLETE; all3CIs contained/ordered |
| S249 | eTable2LDL arms and contrast | PASS_1_COMPLETE; all3CIs contained/ordered |
| S250 | eTable2triglycerides arms and contrast | PASS_1_COMPLETE; all3CIs contained/ordered; rounding-compatible121/121/diff1 |
| S251 | eTable2creatinine arms and contrast | PASS_1_COMPLETE; all3CIs contained/ordered; display collapse coherent |
| S252 | eTable2glucose arms and contrast | PASS_1_COMPLETE; all3CIs contained/ordered |
| S253 | eTable2hemoglobin arms and contrast | PASS_1_COMPLETE; all3CIs contained/ordered |
| S254 | eTable5MACE fourmodels | PASS_1_COMPLETE; all4OR/CIs contained/ordered |
| S255 | eTable5mortality fourmodels | PASS_1_COMPLETE; all4OR/CIs contained/ordered |
| S256 | eTable5CVDmortality fourmodels | PASS_1_COMPLETE; all4OR/CIs contained/ordered; shared rounded rows not independent error |
| S257 | eTable5inhospitalmortality fourmodels | PASS_1_COMPLETE; all4OR/CIs contained/ordered |
| S258 | eTable5reinfarction fourmodels | PASS_1_COMPLETE; all4OR/CIs contained/ordered |
| S259 | eTable5stroke fourmodels | PASS_1_COMPLETE; all4OR/CIs contained/ordered |
| S260 | eTable5bleeding fourmodels | PASS_1_COMPLETE; all4OR/CIs contained/ordered |
| S261 | eTable5inpatient medication fourmodels | PASS_1_COMPLETE; all4OR/CIs contained/ordered; eligible composite denominator retained |
| S262 | eTable5discharge medication fourmodels | PASS_1_COMPLETE; all4OR/CIs contained/ordered |
| S263 | eTable5cessation fourmodels | PASS_1_COMPLETE; all4OR/CIs contained/ordered |
| S264 | eTable6MACE | PASS_1_COMPLETE; OR/CI contained/ordered |
| S265 | eTable6mortality | PASS_1_COMPLETE; OR/CI contained/ordered |
| S266 | eTable6CVDmortality | PASS_1_COMPLETE; OR/CI contained/ordered |
| S267 | eTable6inhospitalmortality | PASS_1_COMPLETE; OR/CI contained/ordered |
| S268 | eTable6reinfarction | PASS_1_COMPLETE; OR/CI contained/ordered |
| S269 | eTable6stroke | PASS_1_COMPLETE; OR/CI contained/ordered |
| S270 | eTable6bleeding | PASS_1_COMPLETE; OR/CI contained/ordered |
| S271 | eTable6inpatient medication | PASS_1_COMPLETE; OR/CI contained/ordered; no inferred duration unit |
| S272 | eTable6discharge medication | PASS_1_COMPLETE; OR/CI contained/ordered |
| S273 | eTable6cessation | PASS_1_COMPLETE; OR/CI contained/ordered |
| S274 | eTable7expandedMACE twoRD/twoOR models | PASS_1_COMPLETE; all4CIs contained/ordered/directions coherent; rounded nulls coherent |
| S275 | eTable7HF twoRD/twoOR models | PASS_1_COMPLETE; all4CIs contained/ordered/directions coherent |
| S276 | eTable7shock twoRD/twoOR models | PASS_1_COMPLETE; all4CIs contained/ordered/directions coherent |
| S277 | eTable7arrest twoRD/twoOR models | PASS_1_COMPLETE; all4CIs contained/ordered/directions coherent; adjustment may reverse crude sign |
| S278 | eFigure1A all hospital residual CIbars and index/caption | PASS_1_COMPLETE; visual containment/order; STAT-S02 label/direction |
| S279 | eFigure1B all hospital difference bubbles | PASS_1_COMPLETE; control-minus-intervention decrease direction coherent |
| S280 | eFigure2A all30cohort-step groups | PASS_1_COMPLETE; every hospital point/CIbar visually considered |
| S281 | eFigure2B all30cohort-step groups | PASS_1_COMPLETE; every hospital point/CIbar visually considered |

## STAT-S01 — eTable 1 contrast footnote does not identify the displayed comparison

**Candidate statement:** eTable1 presents complete-follow-up and missing-follow-up columns, but its difference95%CI footnote defines intervention-minus-control. The displayed differences align with missing-minus-complete summaries, a different grouping from the stated treatment contrast.

**Relationships:** S220,S221,S222,S223,S224,S225,S226,S227,S228,S229,S230,S231,S232,S233,S234,S235,S236.

**Compared locations and content roles:** REPORT DOC-004 [p17 title/column headers](../../../joi170166supp3_prod.pdf#page=17) versus REPORT DOC-004 [p17 difference header and footnote a](../../../joi170166supp3_prod.pdf#page=17). No PLAN location is a conflicting comparator. Shared footnote yields one candidate, not17row candidates.

**Printed evidence:** Title “Baseline Characteristics in ACS QUIK Patients by Complete and Missing Follow-up”; columns “Complete Follow Up n=21079”, “Missing Follow Up n=295”; footnote “Difference = intervention minus control”. Age60.6(12.1) versus60.0(11.6), difference-.6(-2.0to.8); male75.8%vs71.2%, difference-4.6(-9.8to.6); tobacco30.8%vs42.4%, difference11.6(5.9to17.3).

**Rule and calculation:** A contrast label must identify the displayed groups. Direct arithmetic60.0-60.6=-.6,71.2-75.8=-4.6 and42.4-30.8=11.6matches the displayed follow-up-group difference. The figure n21079/295 are follow-up populations; treatment groups elsewhere are10066/11308, reinforcing that these are distinct groupings without importing those elsewhere values as a discrepancy.

**Direct observation versus diagnostic inference:** Contradictory grouping labels are printed directly. Arithmetic supports the follow-up interpretation. A copied footnote is a possible explanation, not a finding about how it was produced. No CI/Ptest reconstruction is needed.

**Source-grounded alternatives / missing definitions:** Table headers could be wrong or the footnote could name the wrong contrast; summary-based differences may use unrounded values, which explains small precision differences but cannot make treatment labels identify follow-up status. Variable-specific n, test and CI method are absent, so they are not asserted.

**Exact human question:** Does the difference column represent missing-follow-up minus complete-follow-up, and should the footnote or group labels be revised to identify the actual comparison?

**Direct-source check:** Current DOC-004 p17was freshly extracted with direct Poppler pdftotext25.03.0; all quoted labels/selected values matched. Formal stable-ID evidence-state assignment is reserved for the fresh rechecker. Candidate remains Pending Human Adjudication; no severity, scientific validity, acceptance or correction assigned.

## STAT-S02 — residual subtraction label and directional caption differ

**Candidate statement:** The supplement index names eFigure1A residuals “Expected – Observed”, while the p24caption describes negative/left residuals as lower-than-mean MACE and positive/right residuals as higher-than-mean MACE. Under the caption's mean-rate reference, this direction corresponds to observed-minus-reference, the opposite subtraction order.

**Relationship:** S278.

**Compared locations and content roles:** REPORT DOC-004 [index p1, eFigure1A line](../../../joi170166supp3_prod.pdf#page=1) versus REPORT DOC-004 [p24 axis and explanatory caption](../../../joi170166supp3_prod.pdf#page=24). Both are REPORT parts of the same mixed bundle; PLAN toolkit content is not a comparator.

**Printed evidence:** Index “Residual of 30-Day Major Adverse Cardiovascular Event Rate (Expected – Observed) by Individual Hospitals”. P24caption says residuals are calculated from predicted MACE rates from the cluster/time-adjusted multilevel logistic model, represent hospital departures from the mean MACE rate at residual0, and left hospitals have MACE lower than mean/right hospitals higher. Graphic residual axis increases from approximately-3to2with hospitals ordered from negative left to positive right.

**Rule and calculation:** For a common expected/reference rate Eand observed rate O, O<E implies E-O>0, whereas the caption assigns a below-reference hospital a negative residual. Conversely O>E implies E-O<0, whereas caption assigns higher-rate hospitals positive residuals. This is an algebraic sign comparison of the printed subtraction label and the printed directional meaning; it does not infer any particular hospital's numeric rate or residual from raster coordinates.

**Direct observation versus diagnostic inference:** Subtraction order and directional prose are supplied. The exact prediction/reference mapping is not supplied. Applying expected-minus-observed algebra to the caption's stated mean reference is a conditional diagnostic; it does not prove whether index, caption or model-output label is the erroneous component.

**Source-grounded alternatives / missing definitions:** “Residual” may mean fitted hospital random effect on log-odds scale rather than arithmetic risk difference; the caption could express its direction correctly while the index names another residual. Expected may be a hospital-specific prediction rather than the mean reference; that distinction would itself require readers to know why the index and caption refer to different quantities. Missing definitions: residual formula, model link/scale, which prediction includes/excludes hospital random effects, and expected reference. The source index/caption does not disclose a change of residual definition.

**Exact human question:** What residual was actually plotted, what are its scale and reference, and which subtraction/direction description correctly identifies that plotted quantity?

**Direct-source check:** Current DOC-004 p1was freshly extracted with direct Poppler pdftotext25.03.0; p24source-bound full-page raster was visually inspected and caption/axis confirmed. Formal stable-ID evidence-state assignment belongs to the fresh rechecker. Candidate remains Pending Human Adjudication; no severity, scientific validity, acceptance or correction assigned.

## Bounded limitations and handoff

No coverage gap in assigned inferential scope. Exact hospital point/CI numbers are not printed in graphics; source CI algorithm/variance/df/covariance/test details are absent for support result tables. Toolkit instructional tick typography is low resolution; metric percentiles and direction were visually readable, tiny schematic metric digits are not exact transcriptions. Source-bound p10age55-64all-hospital28%correction affects no inference. Main pass1owns the main troponin Prelationship; same-test P<.001vs eTable1CIcompatibility is not established. Planned and actual sample sizes, models and populations are kept distinct. Future pass2must revisit all81records with complete cross-lane ledger and mechanical recheck. This pass1agent must not be reused for pass2.
