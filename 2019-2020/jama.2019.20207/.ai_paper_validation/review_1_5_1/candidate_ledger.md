# Stable Candidate Ledger

All records are **Pending Human Adjudication**. Stable IDs were assigned after merging only proposals about the same printed values/statements, comparator, and consistency rule. No candidate is an AI validity decision or correction.

## C001 — Randomization age-stratum boundary differs across the main article and final support documents

- **Status:** Pending Human Adjudication
- **Category:** Cross-document numeric inconsistency
- **Linked relationships:** N004; S004
- **Checker provenance:** numeric NP-02; cross-source Proposal A; statistical pass 1 SP1-P01
- **Exact source locations:** `jama_parsons_2020_oi_190140.pdf#page=2`; `joi190140supp1_prod.pdf#page=2`; `joi190140supp1_prod.pdf#page=5`; `joi190140supp1_prod.pdf#page=40`; `joi190140supp2_prod.pdf#page=2`; `joi190140supp2_prod.pdf#page=5`
- **Direct evidence:** The main article prints age strata `<70` versus `>=70`. Protocol Update 10 states that this was corrected to `<=70` versus `>70`; the final schema and SAP use `<=70` versus `>70`.
- **Comparator and rule:** The same randomization/adjustment factor should assign the boundary age consistently. Exactly age 70 is assigned to opposite strata.
- **Calculation:** Set comparison: `{age <70}/{age >=70}` versus `{age <=70}/{age >70}` differs only at age 70; zero tolerance.
- **Alternative source-grounded interpretations:** The article may describe historic implementation, or the correction may not have propagated to article text. The package lacks randomization-system records.
- **Exact human question:** Which boundary was used for randomization and the adjusted Cox analysis, and should the main article or support sources be version-qualified?

## C002 — Eligibility age/Gleason boundary differs across the main article, protocol, and SAP

- **Status:** Pending Human Adjudication
- **Category:** Analysis-unit or population inconsistency
- **Linked relationships:** N003
- **Checker provenance:** numeric NP-01; cross-source Proposal B
- **Exact source locations:** `jama_parsons_2020_oi_190140.pdf#page=2`; `joi190140supp1_prod.pdf#page=5`; `joi190140supp1_prod.pdf#page=15`; `joi190140supp1_prod.pdf#page=16`; `joi190140supp2_prod.pdf#page=1`
- **Direct evidence:** The article allows grade group 1 below age 70 and grade group 2 or less at age 70 or older. The protocol/SAP use Gleason <=6 at age <=70 and <=7 (3+4) only above age 70.
- **Comparator and rule:** Matched eligibility definitions should classify the boundary age consistently; the printed rules allow different pathology grades at exactly age 70.
- **Calculation:** `<70/>=70` versus `<=70/>70` differs at age 70, where the stated permissible pathology category changes.
- **Alternative source-grounded interpretations:** The documents may represent different protocol versions. No participant-level eligibility record resolves which rule governed the analysis.
- **Exact human question:** Which age-specific pathology eligibility rule applied to participants exactly age 70, and should the documents be reconciled or version-labeled?

## C003 — Composite-progression age-boundary comparator requires version confirmation

- **Status:** Pending Human Adjudication
- **Category:** Measure, label, or scale inconsistency
- **Linked relationships:** N006; S009
- **Checker provenance:** numeric NP-03
- **Exact source locations:** `jama_parsons_2020_oi_190140.pdf#page=3`; `joi190140supp1_prod.pdf#page=31`; `joi190140supp2_prod.pdf#page=1`; `joi190140supp2_prod.pdf#page=2`
- **Direct evidence:** The article, protocol p. 31, and SAP p. 2 progression-endpoint statements all use `<70` versus `>=70`. The separate `<=70` versus `>70` statement on SAP p. 1 is an eligibility definition, not the cited endpoint comparator. The initial opposite-boundary comparison was not reproduced from the cited endpoint pages.
- **Comparator and rule:** Matched composite-endpoint definitions should use the same boundary; on the supplied cited pages they do. A different versioned endpoint definition would need an exact source location before an opposite age-70 assignment could be reproduced.
- **Calculation:** All cited endpoint partitions assign age 70 to the `>=70` pathology-threshold group; the recheck did not reproduce a boundary-set difference.
- **Alternative source-grounded interpretations:** Another versioned endpoint definition may exist outside the cited supplied pages, or the initial comparison may have carried the eligibility boundary into the endpoint definition. No event-level classification or alternate endpoint version is supplied.
- **Exact human question:** Is there another supplied or governing versioned progression-endpoint definition using `<=70` versus `>70`, or did the reported endpoint use the matching `<70` versus `>=70` definitions printed on the cited pages?

## C004 — Fourth counseling phase is printed as 16 months versus 17 months

- **Status:** Pending Human Adjudication
- **Category:** Cross-document numeric inconsistency
- **Linked relationships:** N005
- **Checker provenance:** cross-source Proposal C
- **Exact source locations:** `jama_parsons_2020_oi_190140.pdf#page=3`; `joi190140supp1_prod.pdf#page=5`; `joi190140supp1_prod.pdf#page=29`
- **Direct evidence:** The article states 8 calls over 16 months in phase 4; the protocol twice states 8 calls over 17 months after the first three phases span 7 months.
- **Comparator and rule:** Matched descriptions of the same 24-month, 22-call intervention schedule should agree on phase duration.
- **Calculation:** Article durations `1+2+4+16=23` months; protocol durations `1+2+4+17=24` months.
- **Alternative source-grounded interpretations:** Phase-boundary conventions may differ or the article may summarize actual delivery, but the package does not state this.
- **Exact human question:** Was phase 4 intended or delivered over 16 or 17 months, and is there a documented overlap convention?

## C005 — Per-protocol completion percentages do not reproduce from the stated arm denominators

- **Status:** Pending Human Adjudication
- **Category:** Denominator, proportion, or total inconsistency
- **Linked relationships:** N010; N012
- **Checker provenance:** numeric NP-04
- **Exact source locations:** `jama_parsons_2020_oi_190140.pdf#page=4`; `jama_parsons_2020_oi_190140.pdf#page=5`
- **Direct evidence:** After referring to 443 participants (226 intervention; 217 control), the article reports 183 (81.7%) and 171 (79.5%) meeting per-protocol criteria.
- **Comparator and rule:** Printed percentages should reproduce from their stated or immediately linked denominators.
- **Calculation:** `183/226=80.97%`, displayed as 81.0%, not 81.7%; `171/217=78.80%`, displayed as 78.8%, not 79.5%. The listed noncompletion counts independently leave 183 and 171.
- **Alternative source-grounded interpretations:** Unreported denominators of about 224 and 215 may have been used, or the introductory phrase may not define the percentage denominators.
- **Exact human question:** What denominators produced 81.7% and 79.5%, and should the denominators or percentages be clarified?

## C006 — Table 1 PSA categories do not exhaust the printed PSA denominators

- **Status:** Pending Human Adjudication
- **Category:** Denominator, proportion, or total inconsistency
- **Linked relationships:** N011
- **Checker provenance:** numeric NP-05
- **Exact source locations:** `jama_parsons_2020_oi_190140.pdf#page=5`
- **Direct evidence:** Table 1 gives PSA denominators 224 and 217 but displays only 0-2.5 ng/mL counts 25/30 and >2.5-5 ng/mL counts 99/98, without an explicit remainder row or partial-distribution note.
- **Comparator and rule:** Categories presented under a stated denominator require either reconciliation or a stated nonexhaustive scope.
- **Calculation:** `25+99=124`, leaving 100 of 224; `30+98=128`, leaving 89 of 217.
- **Alternative source-grounded interpretations:** Participants with PSA >5 to <10 may be intentionally omitted, consistent with eligibility, but the table does not label the distribution partial.
- **Exact human question:** Are higher PSA categories intentionally omitted, and should a remainder category or partial-display note be added?

## C007 — Narrative calls gram-per-day cruciferous values “servings”

- **Status:** Pending Human Adjudication
- **Category:** Measure, label, or scale inconsistency
- **Linked relationships:** N015; N017
- **Checker provenance:** numeric NP-06; cross-source Proposal D
- **Exact source locations:** `jama_parsons_2020_oi_190140.pdf#page=5`; `jama_parsons_2020_oi_190140.pdf#page=7`; `joi190140supp3_prod.pdf#page=2`
- **Direct evidence:** The narrative says “cruciferous servings” while printing 43.10 g/d versus 6.44 g/d. Table 2 and the eTable label those values `Cruciferous, g/d`; a separate servings/day row has 0.71 versus 0.12.
- **Comparator and rule:** A measure label should agree with its displayed unit and the matched table row.
- **Calculation:** Exact-value matching identifies 43.10 and 6.44 as the g/day row, not the distinct servings/day row.
- **Alternative source-grounded interpretations:** “Servings” may be colloquial while the adjacent g/d unit identifies the intended measure.
- **Exact human question:** Should the narrative label be changed to a grams/day cruciferous-vegetable measure?

## C008 — Pilot total of 74 does not match table arm counts totaling 68

- **Status:** Pending Human Adjudication
- **Category:** Denominator, proportion, or total inconsistency
- **Linked relationships:** N020; S008
- **Checker provenance:** numeric NP-07
- **Exact source locations:** `joi190140supp1_prod.pdf#page=12`
- **Direct evidence:** The protocol describes a randomized pilot of 74 men and a 2:1 allocation, while Table 1 headers give intervention n=45 and control n=23.
- **Comparator and rule:** A table nested in a stated study population needs a denominator/population definition when its arm counts do not equal the stated total.
- **Calculation:** `45+23=68`, six fewer than 74.
- **Alternative source-grounded interpretations:** The table may use a six-month complete-case subset, but no footnote states that denominator.
- **Exact human question:** Do n=45 and n=23 represent an evaluable subset, and what accounts for the other six participants?

## C009 — Energy 24-month between-group P value differs between Table 2 and the eTable

- **Status:** Pending Human Adjudication
- **Category:** Cross-document numeric inconsistency
- **Linked relationships:** N017; S005; S017
- **Checker provenance:** statistical pass 1 SP1-P02
- **Exact source locations:** `jama_parsons_2020_oi_190140.pdf#page=7`; `joi190140supp3_prod.pdf#page=2`
- **Direct evidence:** Main Table 2 prints the 24-month change contrast -119.71 (95% CI -211.78 to -27.65), P=.01. The eTable prints component changes -250.01 and -130.3, whose subtraction reproduces -119.71, and the same labeled cross-group comparison prints P<.001; it does not print the full contrast or interval.
- **Comparator and rule:** The same estimate, interval, time, contrast, and model-labeled test should not have incompatible repeated P values.
- **Calculation:** Diagnostic only: interval-implied SE is about 46.97, |z| about 2.55, two-sided normal tail about .011. This does not replace the reported model.
- **Alternative source-grounded interpretations:** One P value may come from a different unreported test or production version, but no distinction is labeled.
- **Exact human question:** Which P value is the intended 24-month energy change-contrast result?

## C010 — Deep-yellow vegetables 24-month between-group P value differs across repeated tables

- **Status:** Pending Human Adjudication
- **Category:** Cross-document numeric inconsistency
- **Linked relationships:** N017; S005; S017
- **Checker provenance:** statistical pass 1 SP1-P03
- **Exact source locations:** `jama_parsons_2020_oi_190140.pdf#page=7`; `joi190140supp3_prod.pdf#page=2`
- **Direct evidence:** Main Table 2 prints the 24-month change contrast 0.14 (95% CI 0.05 to 0.23), P=.004. The eTable prints the same labeled cross-group P comparison as .003 but does not print the contrast or interval; its control component is 0.06 rather than the main table's 0.05, separately tracked in C013.
- **Comparator and rule:** Matched repeated P values should agree to the displayed precision.
- **Calculation:** Diagnostic only: interval-implied SE about .046 and two-sided normal tail about .0023; unreported model details prevent selecting a value.
- **Alternative source-grounded interpretations:** Different rounding from an unprinted P value is possible only if the sources used differing underlying outputs or conventions; neither is labeled.
- **Exact human question:** Which rounded P value is intended for this 24-month contrast?

## C011 — Intervention red-meat 12-month within-group P value differs across repeated tables

- **Status:** Pending Human Adjudication
- **Category:** Cross-document numeric inconsistency
- **Linked relationships:** N017; S005; S017
- **Checker provenance:** statistical pass 1 SP1-P04
- **Exact source locations:** `jama_parsons_2020_oi_190140.pdf#page=7`; `joi190140supp3_prod.pdf#page=2`
- **Direct evidence:** Both sources print intervention change -11.54 g/d (95% CI -19.03 to -4.06) for the same within-group contrast. Table 2 prints P=.003; the eTable prints P=.001.
- **Comparator and rule:** Matched repeated P values should agree to displayed precision.
- **Calculation:** Diagnostic only: interval-implied SE about 3.82 and two-sided normal tail about .0025.
- **Alternative source-grounded interpretations:** Different unreported inferential conventions could exist, but the tables label the same mixed-model semantics.
- **Exact human question:** Which P value is intended for the intervention arm’s 12-month red-meat change?

## C012 — Control red-meat 12-month within-group P value differs across repeated tables

- **Status:** Pending Human Adjudication
- **Category:** Cross-document numeric inconsistency
- **Linked relationships:** N017; S005; S017
- **Checker provenance:** statistical pass 1 SP1-P05
- **Exact source locations:** `jama_parsons_2020_oi_190140.pdf#page=7`; `joi190140supp3_prod.pdf#page=2`
- **Direct evidence:** Both sources print control change -9.83 g/d (95% CI -17.26 to -2.41) for the same within-group contrast. Table 2 prints P<.001; the eTable prints P=.01.
- **Comparator and rule:** A matched repeated result should not be printed both below .001 and as .01.
- **Calculation:** Diagnostic only: interval-implied SE about 3.79 and two-sided normal tail about .010.
- **Alternative source-grounded interpretations:** A production-version or test-definition difference is possible, but the sources supply no differing label.
- **Exact human question:** Which P value is intended for the control arm’s 12-month red-meat change?

## C013 — Deep-yellow vegetables 24-month control change differs across repeated tables

- **Status:** Pending Human Adjudication
- **Category:** Cross-document numeric inconsistency
- **Linked relationships:** N017; S005; S017
- **Checker provenance:** statistical pass 2 SP2-P01
- **Exact source locations:** `jama_parsons_2020_oi_190140.pdf#page=7`; `joi190140supp3_prod.pdf#page=2`
- **Direct evidence:** Main Table 2 prints the control-group 24-month change as 0.05 servings/day (95% CI -0.02 to 0.11); the eTable prints 0.06 with the same interval for the same control/time/measure row.
- **Comparator and rule:** Repeated component estimates for the same arm, time point, measure, and interval should agree at displayed precision or identify a differing output/rounding basis.
- **Calculation:** The displayed values differ by 0.01 servings/day. The main contrast uses `0.19-0.05=0.14`; the eTable components give `0.19-0.06=0.13`, subject to absent unrounded values.
- **Alternative source-grounded interpretations:** Different unrounded component estimates could round differently while sharing the printed interval, or the tables may reflect different production outputs; neither distinction is labeled.
- **Exact human question:** Which control-group component estimate and underlying unrounded output were intended for the 24-month deep-yellow-vegetable row?

## Stable set summary

- Stable candidates: C001; C002; C003; C004; C005; C006; C007; C008; C009; C010; C011; C012; C013.
- Count: 13.
- Every record remains Pending Human Adjudication.
