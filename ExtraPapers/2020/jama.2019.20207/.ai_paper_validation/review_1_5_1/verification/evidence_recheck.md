# Mechanical Evidence Recheck

This artifact records a separate source-page recheck for every stable candidate ID in the current ledger. The supplied PDFs were inspected at the cited PDF pages. Native text and locally rendered pages under `preprocessing/evidence_recheck/` were used only to locate and read the source pages. The observations below do not constitute an adjudication or prescribe a change.

## C001 — Randomization age-stratum boundary differs across the main article and final support documents

- **Cited location found:** Yes. The relevant statements were found in `jama_parsons_2020_oi_190140.pdf#page=2`, `joi190140supp1_prod.pdf#page=2`, `joi190140supp1_prod.pdf#page=5`, `joi190140supp1_prod.pdf#page=40`, `joi190140supp2_prod.pdf#page=2`, and `joi190140supp2_prod.pdf#page=5`.
- **Source printed value/text matched:** Yes. The main article prints randomization stratified by age “<70 years vs ≥70 years.”
- **Comparator printed value/text matched:** Yes. Supplement 1 PDF page 2 says the age stratification factor was corrected from “< 70 years vs. ≥ 70 years” to “≤ 70 years vs. > 70 years.” Supplement 1 PDF pages 5 and 40 print `≤70` versus `>70` in the schema and final randomization section. Supplement 2 PDF page 2 prints `≤70; >70` for randomization, and PDF page 5 prints `≤70; >70` for the adjusted Cox covariate.
- **Consistency rule applicable:** Yes. When the documents refer to the same age stratification factor, the boundary should place a participant of a given age in the same stratum, or the documents should state why the definitions differ.
- **Calculation or logical comparison reproduced:** The main partition assigns age 70 to the `≥70` stratum. The final protocol/SAP partition assigns age 70 to the `≤70` stratum. The sets differ only for participants exactly age 70; zero numeric tolerance is relevant to this boundary comparison.
- **Necessary inputs available and exact missing inputs or definitions:** The printed partitions, the protocol correction notice, the final protocol schema, and the SAP adjustment definition are available. Missing are the randomization-system configuration and audit trail, participant age values at randomization, the Cox-model code or covariate encoding, and a statement identifying whether the article describes the implemented or an earlier definition.
- **Source-grounded alternative interpretation:** The article could be describing an earlier operational partition while Update 10 documents a later correction, or the correction could have changed documentation without changing an already configured randomization system. The supplied package does not distinguish these possibilities.
- **Direct observation:** The source pages print opposite assignments for exactly age 70, and the protocol notice explicitly calls one boundary a correction.
- **Inferred explanation:** Failure to propagate a correction into the article, or a difference between documentation and the randomization system, is an explanation inferred from the printed conflict; neither mechanism is directly documented.
- **Exact remaining human question:** Which age boundary was actually used in the randomization system and in the reported adjusted Cox analysis for participants exactly age 70, and which document version describes that implementation?

## C002 — Eligibility age/Gleason boundary differs across the main article, protocol, and SAP

- **Cited location found:** Yes. The relevant text was found in `jama_parsons_2020_oi_190140.pdf#page=2`, `joi190140supp1_prod.pdf#page=5`, `joi190140supp1_prod.pdf#page=15`, `joi190140supp1_prod.pdf#page=16`, and `joi190140supp2_prod.pdf#page=1`. Supplement 1 PDF page 15 begins the eligibility section; the exact age/Gleason rule is printed on PDF page 16.
- **Source printed value/text matched:** Yes. The article requires grade group 1 for participants younger than 70 years and grade group 2 or less for participants aged 70 years and older.
- **Comparator printed value/text matched:** Yes. The final protocol schema and section 4.1.10 require Gleason score `≤6` for men `≤70` and `≤(3+4)=7` for men `>70`. The SAP PDF page 1 prints the same `≤70` and `>70` eligibility split.
- **Consistency rule applicable:** Yes. These are matched age-specific pathology eligibility rules, so a participant at the boundary age should have one stated permissible pathology threshold or a version-specific explanation.
- **Calculation or logical comparison reproduced:** At age 70, the article places a participant in the older category and permits grade group 2 or less, while the protocol/SAP place that participant in the `≤70` category and permit only Gleason score `≤6` (grade group 1). The category assignments therefore differ at exactly age 70.
- **Necessary inputs available and exact missing inputs or definitions:** The printed eligibility rules and the final protocol version date are available. Missing are the governing eligibility version for each enrolled participant, participant-level ages and baseline pathology, screening/registration records, and any statement that version-qualifies the article rule.
- **Source-grounded alternative interpretation:** The article and support documents could describe eligibility rules from different protocol versions. The package does not state that the differing age-70 assignments are version-specific.
- **Direct observation:** The article and support documents print different eligibility categories and pathology allowances for exactly age 70.
- **Inferred explanation:** A protocol-version difference or incomplete propagation into the article is inferred; the supplied sources do not document which mechanism occurred.
- **Exact remaining human question:** Which age-specific pathology eligibility rule governed participants exactly age 70, and what protocol version was used to screen them?

## C003 — Composite-progression pathology boundary differs at exactly age 70

- **Cited location found:** Yes. The cited material was found in `jama_parsons_2020_oi_190140.pdf#page=3`, `joi190140supp1_prod.pdf#page=31`, `joi190140supp2_prod.pdf#page=1`, and `joi190140supp2_prod.pdf#page=2`.
- **Source printed value/text matched:** Yes. The article defines pathology progression as ISUP grade group above 1 for those younger than 70 years and grade group greater than 2 for those aged 70 years and older.
- **Comparator printed value/text matched:** The cited support-source endpoint comparator does not print the claimed `≤70` versus `>70` pathology-progression split. Supplement 1 PDF page 31 prints repeat-biopsy Gleason sum `≥7` for men younger than 70 and `≥4+3=7` for men 70 years or older. Supplement 2 PDF page 2 likewise prints `<70` and `≥70` for the progression criterion. Supplement 2 PDF page 1 prints `≤70` and `>70`, but that statement defines baseline eligibility rather than the progression endpoint.
- **Consistency rule applicable:** Yes. Matched definitions of the same composite-endpoint component should use the same age partition and equivalent pathology thresholds. Applied to the exact cited endpoint text, the age partitions agree.
- **Calculation or logical comparison reproduced:** The article, final protocol endpoint, and SAP endpoint all place exactly age 70 in the older progression-threshold group. Article grade group `>2` corresponds to the protocol/SAP threshold of Gleason pattern `4+3` or higher for that group. The claimed opposite age-70 endpoint assignment is not reproduced from the cited endpoint statements.
- **Necessary inputs available and exact missing inputs or definitions:** The article, protocol, and SAP endpoint definitions are available. Missing is any supplied endpoint definition that uses `≤70` versus `>70`, if one exists, plus event-level classifications and the implemented endpoint code.
- **Source-grounded alternative interpretation:** The `≤70` versus `>70` text on Supplement 2 PDF page 1 can be read as an eligibility definition, not as the composite-progression definition. A comparison that carries that eligibility boundary into the endpoint would compare two different rules.
- **Direct observation:** The exact cited endpoint statements use `<70` versus `≥70`; the separate eligibility statement uses `≤70` versus `>70`.
- **Inferred explanation:** Conflation of the eligibility boundary with the progression-endpoint boundary is a possible explanation for the ledger wording, but the production history is not supplied.
- **Exact remaining human question:** Is there another supplied, versioned progression-endpoint definition that assigns exactly age 70 to the `≤70` threshold group, or did the reported endpoint use the matching `<70` versus `≥70` definitions printed on the cited endpoint pages?

## C004 — Fourth counseling phase is printed as 16 months versus 17 months

- **Cited location found:** Yes. The schedule text was found in `jama_parsons_2020_oi_190140.pdf#page=3`, `joi190140supp1_prod.pdf#page=5`, and `joi190140supp1_prod.pdf#page=29`.
- **Source printed value/text matched:** Yes. The article prints the fourth phase as 8 calls over 16 months.
- **Comparator printed value/text matched:** Yes. The protocol schema says the first three phases are completed in 7 months and the fourth continues for 17 months; it also prints 8 calls over a 17-month period. Protocol section 8.6 repeats 17 months and 8 calls.
- **Consistency rule applicable:** Yes. Matched descriptions of the same four-phase, 22-call, 24-month intervention should use the same phase duration unless different timing conventions or actual-versus-planned schedules are identified.
- **Calculation or logical comparison reproduced:** The article’s printed phase durations sum to `1+2+4+16=23` months. The protocol states that the first three phases occupy 7 months and phase 4 occupies 17 months, giving `7+17=24` months. Both descriptions total `6+4+4+8=22` calls.
- **Necessary inputs available and exact missing inputs or definitions:** Phase call counts, phase durations, and the stated 24-month program duration are available. Missing are exact phase start/end anchors, whether adjacent phase boundary months are counted inclusively, and call-delivery logs that distinguish intended from actual timing.
- **Source-grounded alternative interpretation:** The article could use a different boundary-counting convention, or it could summarize actual delivery rather than the planned protocol schedule. Neither distinction is printed on the cited pages.
- **Direct observation:** The same fourth phase is printed as 16 months in the article and 17 months twice in the final protocol.
- **Inferred explanation:** An inclusive-boundary convention or transcription difference is inferred, not documented.
- **Exact remaining human question:** Was phase 4 planned and delivered over 16 or 17 months, and did any explicit phase-boundary convention make both descriptions refer to the same 24-month schedule?

## C005 — Per-protocol completion percentages do not reproduce from the stated arm denominators

- **Cited location found:** Yes. The numerator/percentage statement begins in `jama_parsons_2020_oi_190140.pdf#page=4` and continues into `jama_parsons_2020_oi_190140.pdf#page=5`, where the noncompletion reasons are printed.
- **Source printed value/text matched:** Yes. The article states that the primary analysis set contained 443 participants, 226 intervention and 217 control, followed by 183 (81.7%) and 171 (79.5%) meeting the study’s per-protocol criteria.
- **Comparator printed value/text matched:** Yes. The immediately linked arm denominators are 226 and 217. The next page prints noncompletion counts of 36, 4, 1, and 2 for intervention and 34, 4, 3, and 5 for control.
- **Consistency rule applicable:** Yes. A displayed percentage should equal its numerator divided by its stated or clearly linked denominator, subject to ordinary rounding; if another denominator is used, that denominator needs a definition.
- **Calculation or logical comparison reproduced:** `183/226=80.97%`, which rounds to 81.0%, not 81.7%. `171/217=78.80%`, which rounds to 78.8%, not 79.5%. The reason counts reconcile the numerators: `226-(36+4+1+2)=183` and `217-(34+4+3+5)=171`. The printed percentages imply denominators near 224 and 215: `183/224=81.70%` and `171/215=79.53%`.
- **Necessary inputs available and exact missing inputs or definitions:** The analysis-set arm totals, completion numerators, displayed percentages, and noncompletion counts are available. Missing are the denominators actually used for 81.7% and 79.5%, the identities/reasons for any two-participant denominator reduction in each arm, and a definition connecting those denominators to per-protocol eligibility.
- **Source-grounded alternative interpretation:** The percentages may use unprinted evaluable denominators of 224 and 215 rather than the analysis-set denominators of 226 and 217. The cited text does not define such denominators.
- **Direct observation:** The printed percentages do not reproduce from 226 and 217, although the printed noncompletion counts reproduce the completion numerators.
- **Inferred explanation:** Use of smaller unreported denominators is inferred from reverse calculation; it is not directly stated.
- **Exact remaining human question:** What exact denominators and participant exclusions produced 183 (81.7%) and 171 (79.5%)?

## C006 — Table 1 PSA categories do not exhaust the printed PSA denominators

- **Cited location found:** Yes. Table 1 is present in `jama_parsons_2020_oi_190140.pdf#page=5`.
- **Source printed value/text matched:** Yes. The table prints serum PSA denominators `n=224` and `n=217`, with rows 0–2.5 ng/mL containing 25 and 30 participants and >2.5–5 ng/mL containing 99 and 98 participants.
- **Comparator printed value/text matched:** Yes. No additional PSA category or footnote identifying a partial display appears under those rows before the table ends.
- **Consistency rule applicable:** The reconciliation rule applies if the displayed rows are intended as an exhaustive categorical distribution. If the rows are intentionally partial, the missing requirement is a source definition or label stating that scope.
- **Calculation or logical comparison reproduced:** Intervention counts sum to `25+99=124`, leaving `224-124=100` participants; the shown rows cover 55.4% and leave 44.6%. Control counts sum to `30+98=128`, leaving `217-128=89`; the shown rows cover 59.0% and leave 41.0%. As corroborating package context, `joi190140supp2_prod.pdf#page=5` defines a third baseline PSA category, `>5 but less than 10`.
- **Necessary inputs available and exact missing inputs or definitions:** The table denominators, displayed counts, percentages, and the SAP’s third-category definition are available. Missing are the >5 to <10 counts for Table 1 and an explicit statement of whether the article intentionally displays only part of the PSA distribution.
- **Source-grounded alternative interpretation:** The remainders may be participants in the SAP-defined `>5 but less than 10` category, consistent with the study’s PSA eligibility ceiling. The article table does not print that row.
- **Direct observation:** The two printed PSA rows do not sum to the denominators, and no article-table note labels the rows as nonexhaustive.
- **Inferred explanation:** Assignment of the remainders to the >5 to <10 category is inferred from the SAP category definition; the participant counts are not supplied.
- **Exact remaining human question:** Are the 100 intervention and 89 control participants the omitted >5 to <10 ng/mL category, and was Table 1 intended to be a partial or an exhaustive PSA distribution?

## C007 — Narrative calls gram-per-day cruciferous values “servings”

- **Cited location found:** Yes. The narrative is in `jama_parsons_2020_oi_190140.pdf#page=5`, Table 2 is in `jama_parsons_2020_oi_190140.pdf#page=7`, and the eTable is in `joi190140supp3_prod.pdf#page=2`.
- **Source printed value/text matched:** Yes. The narrative says “cruciferous servings” and then reports 43.10 g/d versus 6.44 g/d with the corresponding confidence intervals.
- **Comparator printed value/text matched:** Yes. Table 2 labels 43.10 and 6.44 as `Cruciferous, g/d`; its separate `Cruciferous, servings/d` row prints 0.71 and 0.12. The eTable likewise prints 43.1 and 6.44 under `Cruciferous vegetables (gm/day)` and 0.71 and 0.12 under a separate servings/day row.
- **Consistency rule applicable:** Yes. A narrative measure label should identify the same quantity and unit as the matched table values, especially when a distinct servings/day measure is also reported.
- **Calculation or logical comparison reproduced:** Exact value and confidence-interval matching maps narrative 43.10 (35.21 to 50.99) and 6.44 (−1.39 to 14.26) to the grams/day row. The servings/day row has different values, 0.71 (0.60 to 0.83) and 0.12 (0.01 to 0.23).
- **Necessary inputs available and exact missing inputs or definitions:** The narrative wording, units, table row labels, values, and intervals are available. No conversion factor or serving-size definition is needed to identify the matched row. Missing is only the editorial intent behind the noun “servings.”
- **Source-grounded alternative interpretation:** “Servings” may be used colloquially to refer to the dietary item while the immediately following `g/d` unit supplies the quantitative measure. The presence of a separate servings/day row makes the two formal measures distinguishable.
- **Direct observation:** The narrative noun says servings, while its values and units exactly match the grams/day row rather than the separate servings/day row.
- **Inferred explanation:** Colloquial wording or a label carryover is inferred; no editorial history is supplied.
- **Exact remaining human question:** Was the narrative intended to refer to cruciferous vegetable intake in grams/day or to the separately reported servings/day measure?

## C008 — Pilot total of 74 does not match table arm counts totaling 68

- **Cited location found:** Yes. The pilot description and Table 1 are both in `joi190140supp1_prod.pdf#page=12`.
- **Source printed value/text matched:** Yes. The protocol describes a randomized controlled clinical pilot trial of 74 men and states that two participants were randomized to intervention for every one randomized to comparison.
- **Comparator printed value/text matched:** Yes. The six-month dietary table prints intervention `n=45` and control `n=23` without a footnote defining those values as a subset.
- **Consistency rule applicable:** The total-to-arm reconciliation rule applies if the table arm counts represent all randomized pilot participants. If the table is restricted to evaluable dietary records, the needed rule input is an explicit denominator definition and participant accounting.
- **Calculation or logical comparison reproduced:** `45+23=68`, which is 6 fewer than 74. The printed arm ratio is `45/23=1.96`, approximately the stated 2:1 allocation, but the ratio does not explain the six-person difference.
- **Necessary inputs available and exact missing inputs or definitions:** The pilot total, allocation ratio, table arm counts, and six-month table context are available. Missing are the original randomized arm counts, six-month evaluability/completion criteria, arm-specific missingness, and the disposition of the six participants absent from the table counts.
- **Source-grounded alternative interpretation:** Because the table summarizes baseline and six-month dietary recall values, `n=45` and `n=23` may be the participants with evaluable paired dietary data rather than all randomized participants. No table note states that restriction.
- **Direct observation:** The stated pilot total is 74, while the table headers sum to 68.
- **Inferred explanation:** Complete-case or paired-recall restriction is inferred from the table’s six-month context; the source does not explicitly define the table denominator.
- **Exact remaining human question:** What population do `n=45` and `n=23` represent, and what are the arm assignments and reasons for absence of the other six randomized participants?

## C009 — Energy 24-month between-group P value differs between Table 2 and the eTable

- **Cited location found:** Yes. The main result is in `jama_parsons_2020_oi_190140.pdf#page=7`, and the eTable result is in `joi190140supp3_prod.pdf#page=2`.
- **Source printed value/text matched:** Yes. Main Table 2 prints 24-month energy changes of −250.01 kcal/d and −130.3 kcal/d, a between-group difference of −119.71 (95% CI, −211.78 to −27.65), and `P=.01`.
- **Comparator printed value/text matched:** The eTable prints the same two component changes and prints `P<.001` in the 24-month `p-value†` column, whose footnote defines changes in intervention compared with changes in control. It does not itself print the −119.71 contrast estimate or its confidence interval. The current narrowed ledger accurately identifies that distinction.
- **Consistency rule applicable:** Yes. The time point, measure, component changes, mixed-model label, and cross-group contrast semantics match closely enough for the repeated cross-group P values to require a defined distinction if they come from different tests or versions.
- **Calculation or logical comparison reproduced:** From the eTable components, `−250.01−(−130.3)=−119.71`, exactly reproducing the main-table contrast. As a diagnostic only, the main interval gives `SE≈(−27.65−(−211.78))/(2×1.96)=46.97`; `|−119.71|/46.97≈2.55`, with an approximate two-sided normal tail of 0.011, near `.01` rather than `<.001`. This diagnostic does not replace the mixed-model test.
- **Necessary inputs available and exact missing inputs or definitions:** The displayed component changes, main contrast and interval, P values, time point, units, and mixed-model footnotes are available. Missing are unrounded estimates, covariance terms, degrees of freedom, exact test statistic, contrast matrix, sidedness implementation beyond the article’s general two-sided statement, analytic dataset/version, and confirmation that both P values were exported from the same fitted model.
- **Source-grounded alternative interpretation:** The eTable `p-value†` may derive from a different production version, dataset, or unreported contrast/test even though its footnote describes the same cross-group change comparison. No such distinction is labeled.
- **Direct observation:** The main table prints `.01`; the eTable prints `<.001` for a cross-group 24-month energy comparison whose displayed component changes reproduce the main contrast.
- **Inferred explanation:** A production-version or test-definition difference is inferred; the source pages do not state it.
- **Exact remaining human question:** What exact model, contrast, dataset, and unrounded output produced each 24-month energy cross-group P value, and which output was intended for this result?

## C010 — Deep-yellow vegetables 24-month between-group P value differs across repeated tables

- **Cited location found:** Yes. The relevant rows are in `jama_parsons_2020_oi_190140.pdf#page=7` and `joi190140supp3_prod.pdf#page=2`.
- **Source printed value/text matched:** Yes. Main Table 2 prints 24-month changes of 0.19 and 0.05 servings/d, a between-group difference of 0.14 (95% CI, 0.05 to 0.23), and `P=.004`.
- **Comparator printed value/text matched:** The eTable prints 0.19 for intervention, 0.06 for control, and `P=.003` in the 24-month cross-group `p-value†` column. It does not print the 0.14 contrast or its interval. Thus, the P comparator is present and the displayed control component also differs by 0.01; the current narrowed ledger records both facts and tracks the component mismatch separately as C013.
- **Consistency rule applicable:** Yes. The rows identify the same measure, time point, intervention-versus-control change comparison, and mixed-model context. Repeated displayed P values should agree at the stated precision unless a differing output or convention is identified.
- **Calculation or logical comparison reproduced:** The main components give `0.19−0.05=0.14`. The eTable’s rounded components give `0.19−0.06=0.13`; unrounded components could still produce the main contrast, but they are absent. As a diagnostic only, the main interval gives `SE≈(0.23−0.05)/(2×1.96)=0.0459`; `0.14/0.0459≈3.05`, with an approximate two-sided normal tail of 0.0023. The model-specific test may differ from this diagnostic.
- **Necessary inputs available and exact missing inputs or definitions:** The main contrast, interval, P value, component changes, eTable component changes, eTable P value, and footnotes are available. Missing are unrounded component and contrast estimates, exact model/test output, covariance, degrees of freedom, contrast matrix, analytic dataset/version, and the reason the control change is printed as 0.05 versus 0.06.
- **Source-grounded alternative interpretation:** Separate production outputs or different rounding inputs could account for both the 0.01 component difference and the P-value difference. The sources do not label a different model or population.
- **Direct observation:** The main table prints `.004` and the eTable prints `.003` for the labeled cross-group comparison; the eTable does not print the same contrast estimate/interval, and its rounded control component differs.
- **Inferred explanation:** Rounding from different underlying outputs or a production-version difference is inferred, not documented.
- **Exact remaining human question:** Which unrounded component estimates, contrast, model output, and P value were intended for the 24-month deep-yellow-vegetable comparison?

## C011 — Intervention red-meat 12-month within-group P value differs across repeated tables

- **Cited location found:** Yes. The matched red-meat rows are in `jama_parsons_2020_oi_190140.pdf#page=7` and `joi190140supp3_prod.pdf#page=2`.
- **Source printed value/text matched:** Yes. Main Table 2 prints intervention 12-month change −11.54 g/d (95% CI, −19.03 to −4.06) with `P=.003`.
- **Comparator printed value/text matched:** Yes. The eTable prints the same change and confidence interval with `P=.001` in the within-group `p-value*` column. Both footnotes define the within-group result as follow-up compared with baseline and identify mixed-model P values.
- **Consistency rule applicable:** Yes. Matched repeated values for the same arm, time, measure, contrast, and model-labeled test should have the same displayed P value unless a differing test or output is defined.
- **Calculation or logical comparison reproduced:** As a diagnostic only, `SE≈(−4.06−(−19.03))/(2×1.96)=3.82`; `|−11.54|/3.82≈3.02`, with an approximate two-sided normal tail of 0.0025, which ordinarily displays as `.003`. This does not establish the exact mixed-model P value.
- **Necessary inputs available and exact missing inputs or definitions:** The estimate, interval, both P values, time, arm, unit, and footnote semantics are available. Missing are unrounded estimate/interval endpoints, exact test statistic, degrees of freedom, covariance/model output, analytic dataset/version, and any source statement that the tables use different tests.
- **Source-grounded alternative interpretation:** The two tables may reflect different production outputs or unreported inferential conventions despite identical displayed estimate and interval. No distinction is labeled.
- **Direct observation:** Identical displayed estimate and interval are paired with `.003` in the main table and `.001` in the eTable.
- **Inferred explanation:** A production-version or inferential-convention difference is inferred; it is not stated in the package.
- **Exact remaining human question:** What exact mixed-model output and test definition produced each intervention 12-month red-meat P value, and which output was intended for the repeated result?

## C012 — Control red-meat 12-month within-group P value differs across repeated tables

- **Cited location found:** Yes. The matched red-meat rows are in `jama_parsons_2020_oi_190140.pdf#page=7` and `joi190140supp3_prod.pdf#page=2`.
- **Source printed value/text matched:** Yes. Main Table 2 prints control 12-month change −9.83 g/d (95% CI, −17.26 to −2.41) with `P<.001`.
- **Comparator printed value/text matched:** Yes. The eTable prints the same change and confidence interval with `P=.01` in the within-group `p-value*` column. Both tables define the within-group comparison as follow-up versus baseline and state that P values are based on a mixed-model analysis.
- **Consistency rule applicable:** Yes. The same arm, time, measure, estimate, interval, and contrast semantics should not carry both `<.001` and `.01` without a defined test or output difference.
- **Calculation or logical comparison reproduced:** As a diagnostic only, `SE≈(−2.41−(−17.26))/(2×1.96)=3.79`; `|−9.83|/3.79≈2.60`, with an approximate two-sided normal tail of 0.0095, near `.01`. This diagnostic is not a substitute for the reported mixed-model analysis.
- **Necessary inputs available and exact missing inputs or definitions:** The identical estimate and interval, both P values, arm, time, unit, and footnote semantics are available. Missing are the exact test statistic, degrees of freedom, covariance/model output, unrounded values, analytic dataset/version, and any definition of different tests between the tables.
- **Source-grounded alternative interpretation:** One table may contain a P value from another result or production version, or the two P values may use different unreported tests. The supplied pages do not identify such a distinction.
- **Direct observation:** The repeated estimate and interval are paired with `<.001` in the main table and `.01` in the eTable.
- **Inferred explanation:** A carried-over P value, production-version difference, or test-definition difference is inferred; none is directly documented.
- **Exact remaining human question:** What exact mixed-model output produced the control arm’s 12-month red-meat P value, and which test and displayed value were intended for this repeated result?

## C013 — Deep-yellow vegetables 24-month control change differs across repeated tables

- **Cited location found:** Yes. The main Table 2 row is in `jama_parsons_2020_oi_190140.pdf#page=7`, and the repeated eTable row is in `joi190140supp3_prod.pdf#page=2`.
- **Source printed value/text matched:** Yes. Table 2 prints the deep-yellow-vegetable control-group 24-month change as 0.05 servings/d with 95% CI −0.02 to 0.11, matching the corrected current ledger.
- **Comparator printed value/text matched:** Yes. The eTable prints 0.06 servings/day with the same displayed 95% CI, −0.02 to 0.11, for the deep-yellow-vegetable control group at 24 months.
- **Consistency rule applicable:** Yes. A repeated component estimate for the same arm, time point, measure, unit, and displayed interval should agree at two-decimal precision unless the sources identify different populations, models, unrounded outputs, or production versions.
- **Calculation or logical comparison reproduced:** The displayed component estimates differ by `0.06−0.05=0.01` servings/day. Main Table 2 prints intervention change 0.19 and control change 0.05, whose displayed subtraction is `0.19−0.05=0.14`, matching its printed between-group difference of 0.14. The eTable components give `0.19−0.06=0.13`; it does not print a between-group point estimate, and absent unrounded values prevent an exact reconstruction beyond the displayed arithmetic.
- **Necessary inputs available and exact missing inputs or definitions:** The source and comparator point estimates, identical displayed intervals, arm, time point, measure, unit, and mixed-model table context are available. Missing are the unrounded component estimates and interval endpoints, exact mixed-model outputs, analytic dataset and production version for each table, rounding convention, and any statement that the repeated rows intentionally use different outputs.
- **Source-grounded alternative interpretation:** Separately generated outputs could contain slightly different unrounded control estimates that display as 0.05 and 0.06 while their interval endpoints display identically. The tables could also reflect different production versions. Neither source page labels such a distinction.
- **Direct observation:** The main table prints 0.05 and the eTable prints 0.06 for the same labeled control-group 24-month change; both source pages print the interval as −0.02 to 0.11.
- **Inferred explanation:** Different unrounded model outputs, rounding inputs, or production versions are possible explanations inferred from the repeated rows; none is directly documented.
- **Exact remaining human question:** Which unrounded control-group estimate, model output, analytic version, and displayed value were intended for the 24-month deep-yellow-vegetable row, and how does that component correspond to the adjacent cross-group result?

## Recheck Scope Summary

- Stable candidate IDs rechecked separately: C001; C002; C003; C004; C005; C006; C007; C008; C009; C010; C011; C012; C013.
- Direct supplied-source files inspected: `jama_parsons_2020_oi_190140.pdf`, `joi190140supp1_prod.pdf`, `joi190140supp2_prod.pdf`, and `joi190140supp3_prod.pdf`.
- Exact unresolved inputs are stated within each candidate section; no candidate ID was removed or renumbered.
