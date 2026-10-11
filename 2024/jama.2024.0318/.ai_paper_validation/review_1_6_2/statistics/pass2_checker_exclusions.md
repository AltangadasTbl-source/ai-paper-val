# Complete checker exclusions for statistical pass 2

This current-run locator preserves every original checker exclusion row verbatim. The second statistical pass must reread the cited source locations against all route A categories and the display-precision rule. No scientific decision is added here.


## numeric_consistency.md — original exclusion table

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 p3 Figure1 N026 | Arm branches193+122=315 versus parent305. Half-unit sum[314,316], parent[304.5,305.5]; relative gap8.5/305=.027869≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p1/p3 cohort summary and p4 Table1 N004/N029/N044 | White177/262=67.5573% versus67.2%. Relative discrepancy below.05 even before allowing half-unit counts; rounded input intervals overlap printed interval. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p4 Table1 β-blockers N066 | B30/166=18.0723% versus18.2%; half-unit ratio interval[17.7177,18.4290] overlaps[18.15,18.25]. Explicit subgroup35 denominator also supports30/165=18.1818%. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p3 HbA1c and p6 Table2 N031 | Raw B7.2−8.7=−1.5 versus modeled table−1.6; half-unit difference interval[−1.6,−1.4] overlaps[−1.65,−1.55]. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p4 Table1 triglycerides and urine albumin:creatinine N059/N061 | Mean(SD) label accompanies two-ended parenthetic ranges; field reader recognizes range-format summaries; no source-grounded numeric contradiction or result-changing quantity is established. | TERMINOLOGY_OR_WORDING |

## numeric_consistency.md — original exclusion table

| Location | Observation | Reason code |
|---|---|---|
| DOC-001 p6 Table2 fasting-glucose change row | MED point change lacks the percent sign printed on its interval and other cells; footnoteb explicitly specifies relative percent change and fixes the unit without changing a number. | NOTATION_OR_TYPOGRAPHY |
| DOC-003 pp15–16 eTable2 footnotesa–c | Several footnotes say year7 while the title, all value columns and footnotee say year12; this footnote template wording does not change the printed values or leave their visit unidentified. | CONTEXT_RESOLVES |
| DOC-003 p18 eTable4 Calcium difference SE | Printed SE0.0 at one decimal can represent a small positive value below0.05; groupSE0.04/0.03 and P.03 therefore do not establish an exact-zero-SE contradiction. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 p6 Table2 and DOC-003 pp15–16 eTable2 raw summaries versus adjusted changes/ORs | Arithmetic of marginal baseline/visit means and crude percentages differs from some model estimates; footnotes and supplementary mixed-model/GEE specifications identify the estimates as model-based. | MODEL_VERSUS_CRUDE |

## numeric_consistency.md — original exclusion table

| Location | Observation | Reason code |
|---|---|---|
| [PLAN p9](../../../joi240004supp1_prod_1721756962.80052.pdf#page=9), [PLAN p16](../../../joi240004supp1_prod_1721756962.80052.pdf#page=16) | BMI<35 prevalence35% versus one third: even treating one third as33.333%, printed35% lower bound34.5 gives gap1.1667/35=.03333≤.05; approximate prevalence does not reproduce beyond display threshold. | ROUNDING_OR_DISPLAY_PRECISION |
| [PLAN pp32–33](../../../joi240004supp1_prod_1721756962.80052.pdf#page=32), TableA4p33 | RYGB narrative150cm Roux limb exceptBWH75cm/approx50cm BP limb versusCROSSROADS table100–150cm/30–50cm describes historical operative ranges; it changes no primary/key-secondary result, analysis population, randomized-intervention dose/duration, or statistical decision rule. | PERIPHERAL_COMPARISON |
| [PLAN p35](../../../joi240004supp1_prod_1721756962.80052.pdf#page=35), TableA5 | Plain layout readsrho=0.11 by adjoiningrho=.1 and superscriptfootnote1. Footnote1 and surrounding autocorrelation range make the readingrho=.1 immediately clear; no numerical source substitution reproduced. | NOT_REPRODUCED |
| [PLAN p28](../../../joi240004supp1_prod_1721756962.80052.pdf#page=28), control-power paragraph | A specific extrapolation from75/63/48% and52/38/22% to39/11% would require assuming a fitted slope/intercept or which historical points define the assumed linear log-odds curves. They are not printed, and the year7 values are simulation assumptions rather than count-derived results; no unique arithmetic conflict reproduced here. The explicit trend claim remains assigned to statistical review. | CONDITIONAL_OR_UNREPORTED |
| [PLAN p35](../../../joi240004supp1_prod_1721756962.80052.pdf#page=35), detectable weight difference | Central delta.43–.47×residualSD6% gives2.58–2.82%, including statedapproximately2.8%; mandated rounded-input interval2.3375–3.0875% overlaps printed2.8±.05%. An apparent challenge that2.8 must equal.43×6 has zero interval gap. | ROUNDING_OR_DISPLAY_PRECISION |

## cross_source_consistency.md — original exclusion table

| Location | Observation | Reason code |
|---|---|---|
| Mainp4Table1 vs supplementp14eTable1 | Repeated descriptive baseline medians/IQRs,rounding and cohort-table summaries differ in some cells; these are cross-copy baseline descriptors, not primary/key results or within-display count discrepancies. | PERIPHERAL_COMPARISON |
| Mainp5Figure2 contributor rows vs supplementp12eFigure5 and medicationp10eFigure3 | Visit-specific observation counts differ across outcomes; no matched analysis-set total discrepancy follows. | PERIPHERAL_COMPARISON |
| Mainp7Figure3 contributor rows vs mainp6Table2 headers and medication narrative | Different outcome-specific measurement availability versus group headers; does not assert a different enrolled population. | PERIPHERAL_COMPARISON |
| Mainp1/p4 remissionOR3.4[1.3,9.2] vs mainp6OR3.39[1.25,9.17] | Rounded copies overlap respective half-unit intervals; relative gaps≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| Mainp8 remission51/18/6 vs mainp1/p4 50.8/18.2/6.2 | Discussion rounded percentages; half-unit intervals overlap or residual discrepancy≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| Mainp4 narrativeHbA1c≤6.5 vs mainp6Table2HbA1c<6.5 | Equality-symbol difference in adjacent explanation of same explicitly labeled table row; no different numerical result supplied. | NOTATION_OR_TYPOGRAPHY |
| Supplementp13eFigure6BMI>35 vs mainp7BMI≥35 | Figure inequality symbol omits equality while complementaryBMI<35 group and same caption values identify the intended split immediately. | NOTATION_OR_TYPOGRAPHY |
| Supplementpp15–16eTable2 year12 title/values vs year7 wording in footnotes | Reused year7 wording in footnotes; title,year12 column heads and special12year remission footnote identify the visit immediately, with no conflicting counterpart value beyond separately emittedP issue. | CONTEXT_RESOLVES |
| Mainp6/eTable2 modeled changes vs raw baseline/follow-up differences or crudeOR | AdjustedLS/GEE estimates need not equal crude summary differences or odds ratios. | MODEL_VERSUS_CRUDE |
| Protocolp17 original age≥20 vs mainp2/supplementp3 age18–65 | Historical parent-eligibility age boundaries differ; no supplied count identifies enrolled18/19yearolds or an analysis-population size change, and this is not a primary/key endpoint or decision-rule discrepancy. | PERIPHERAL_COMPARISON |
| Protocolp17 general anesthesia “or” exercise vs supplementp3 anesthesia/exercise criteria | Parent cohorts comprise surgical and lifestyle arms; descriptions do not identify a different quantitative analysis set. | TERMINOLOGY_OR_WORDING |
| Protocolp17 BMI>27 vs report BMI27–45 shorthand | Original range shorthand differs at boundary symbol; no different population count/result is attributed. | TERMINOLOGY_OR_WORDING |
| Protocolp17 pregnancy screening+baseline vs supplementp3 baseline only, willingness/compliance omitted in shortened report list | Abbreviated original-trial summary omits details; no conflicting enrolled analysis-population or outcome count supplied. | CONDITIONAL_OR_UNREPORTED |
| Protocolpp7,16 “up to13” vs report through12 | Prospective maximum follow-up description and final available report window do not replace the7year primary endpoint. | CONTEXT_RESOLVES |
| Protocolpp16–17 additional7year vs fiveyear common data-collection wording | Follow-up calendar/administrative duration varies within protocol; no change to primary7year decision rule or randomized intervention duration established. | PERIPHERAL_COMPARISON |
| Protocolp27 power325 initiated vs appendixp55 sum325 and other sections302/316 | Prospective/historical availability snapshots and final enrollment taken at different times; not conflicting final analysis-set counts. | PERIPHERAL_COMPARISON |
| Protocolp32/33 surgical counts192 vs final original-assignment/enrolled procedure counts | Planning completed-surgery snapshot and reported later assignment/enrollment sets are different quantities. | PERIPHERAL_COMPARISON |
| Protocolpp32–33 RYGB limb narrative75/150 vs tableUW100–150cm/BPlimb30–50 | Surgical construction range/approximation does not change primary/key analysis or intervention duration/dose statement in report. | PERIPHERAL_COMPARISON |
| Protocolp31 exploratory four-arm analysis vs supplementp4 “secondary analysis” | Same planned nonprimary model and four comparisons; “secondary analysis” does not designate a different outcome status or claim additional prespecification. | TERMINOLOGY_OR_WORDING |
| Protocolp29 QoL percent change vs p18change wording | QoL is nonkey and not relied on for a reported primary/key estimate; no finalQoL number conflicts. | PERIPHERAL_COMPARISON |
| Protocol secondaryrelapse/QoL/UKPDS and ancillarycostutility vs complete report | Unreported nonkey outcomes/other-paper ancillary analyses; no claim of primary/key designation or substitution; omission alone beyond mandated primary/key analysis scope. | CONDITIONAL_OR_UNREPORTED |
| Protocol exploratory taxonomy/predictor models vs report | Additional exploratory analyses absent from package; no report claim that such absent analysis was prespecified/performed. | CONDITIONAL_OR_UNREPORTED |
| Protocolp31 Bonferroni vs supplementp4 unspecified multiplicity adjustment | Report says pairwise adjustment; missing named adjustment detail alone supplies no conflicting rule/value. | CONDITIONAL_OR_UNREPORTED |
| Protocol residual covarianceAIC vs report random-intercept description | Unreported residual-covariance selection does not itself contradict printed primary model/value. | CONDITIONAL_OR_UNREPORTED |
| Protocolp36SAS9.3 vs reportSAS9.4 | Software release difference does not by itself conflict with quantitative analysis/model. | OUT_OF_FOCUS |
| Protocolp1Version6b vs footerVersion6 | Cover/footer version abbreviation; no distinct supplied statistical version or conflicting analysis inferred. | PERIPHERAL_COMPARISON |
| Mainp7 GI excess statement and supplementeTable5 nauseaP=.054 | “More” denotes higher printed counts, not explicit statistically significant nausea comparison;P applies its own event row. | CONTEXT_RESOLVES |
| Mainp7 nonsignificantSBP/LDL at7y vs supplementeFigure5 overallP=.16/.83 | Apparent alternativeP values compare overall trajectories rather than7year contrasts; the result direction reconciles after model/time matching. | NOT_REPRODUCED |

## statistical_pass_1.md — original exclusion table

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC001 Table2/DOC003 eTable2, all model estimates; DOC001 Figures2/3 and DOC003 eFigures2/3/5/6 | Crude changes/odds from raw means, percentages or contributor counts differ from adjusted LS/GEE estimates; modeled baseline loss points may differ from raw zero-change values. Source does not identify those estimates as crude. | MODEL_VERSUS_CRUDE |
| REPORT DOC003 pp15-16 eTable2 footnotes | Several copied footnotes say year7 although the table heading, columns and remission footnote identify year12; the immediate display establishes the intended visit. | CONTEXT_RESOLVES |
| REPORT DOC001 p4 narrative versus p6 glycemic-threshold row | Narrative HbA1c≤6.5 versus table HbA1c<6.5 symbol in the same matched P=.002 result; no changed printed value or boundary-subgroup result supplied. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC003 p13 eFigure6 caption versus DOC001 p7/SAP BMI analysis | BMI>35 caption versus ≥35 complement of <35 analysis; no affected boundary participant or changed result identified. | NOTATION_OR_TYPOGRAPHY |
| PLAN DOC002 pp26-27 A1 | Both gamma^T Z and b_i represent fixed-site terms, but the source explicitly permits coefficient constraints for identifiability. This is distinct from the emitted power variance-component comparison. | CONTEXT_RESOLVES |
| REPORT DOC003 pp5-6 GEE missingness assertion | General MAR handling cannot be reconstructed from GEE/sandwich description alone without the outcome/observed-case mechanism or missingness-weight implementation. No raw mechanism or conflicting numeric estimate is supplied; the concern depends on an unstated mechanism. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC002 p28 glycemic-control power projection | Diagnostic ordinary linear fit of logits to75/63/48% preliminary surgery rates predicts about34% atyear7 rather than assumed39%; source does not specify a fit to those points or require them as exact constraints. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC002 pp18,27,31-36 and61-63; complete REPORT DOC001/DOC003 | No supplied report results for non-key QOL/UKPDS/BMI, descriptive relapse, exploratory taxonomy/predictor models or ancillary ICER; absence alone does not establish missing primary/key-secondary analysis or a prespecification claim. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC002 p35 TableA5 footnote | Common SD is described as a covariance diagonal element; nearby SD6% and standardized-effect definition make the intended dispersion quantity clear without a changed printed estimate. | TERMINOLOGY_OR_WORDING |
| REPORT DOC003 p18 eTable4 calcium/albumin | Calcium contrast SE0.0 is one-decimal rounding, not established zero variance; albumin point/SE rounded inputs permit P=.72. These apparent point/SE/test mismatches vanish under complete display intervals. | ROUNDING_OR_DISPLAY_PRECISION |

## statistical_pass_1.md — original exclusion table

| Location | Observation | Reason code |
|---|---|---|
| DOC-003 REPORT p17 eTable3 hypoalbuminemia SG; p19 eTable5 diabetes-related foot ulcers, colon polyps, pneumonia and cellulitis; S147, S152, S165, S180, S181 | Consolidated apparent last-digit count-to-test diagnostic discrepancy: S147 Hypoalbuminemia SG: printed 0.60, Pearson diagnostic 0.594845193, half-unit-band gap 0.000154807, relative 0.000258011; S152 Diabetes related foot ulcers: printed 0.65, Fisher diagnostic 0.655177098, half-unit-band gap 0.000177098, relative 0.000272459; S165 Colon polyps: printed 0.46, Pearson diagnostic 0.465275185, half-unit-band gap 0.000275185, relative 0.000598229; S180 Pneumonia: printed 0.23, Pearson diagnostic 0.224655379, half-unit-band gap 0.000344621, relative 0.001498352; S181 Cellulitis: printed 0.53, Pearson diagnostic 0.535380032, half-unit-band gap 0.000380032, relative 0.000717041. All gaps are far below 0.05 after the printed P half-unit interval, and none involves a confidence interval or a contradictory stated test conclusion. | ROUNDING_OR_DISPLAY_PRECISION |

