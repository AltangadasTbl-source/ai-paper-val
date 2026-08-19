# Quantitative Quality-Control Consistency Review — Workflow 1.5.1

## Pending Human Adjudication

Every observation in this report is **Pending Human Adjudication**. These are source-grounded quantitative reporting quality-control candidates, not determinations about validity, authorship, or correction. Small preventable defects can matter for downstream evidence extraction; this report does not claim that any issue propagated, changed a conclusion, or caused serious harm.

## Executive Quality-Control Summary

Complete coverage identified 13 stable candidate consistency issues: three cross-document definition or schedule comparisons, three denominator/total displays, one measure-label comparison, and six repeated-table comparisons. All 84 supplied PDF pages were mapped. No candidate arises solely from a displayed zero P value; no supplied source displayed `P = 0`, `p = 0.000`, or equivalent.

## Package and Reused-Evidence Provenance

The supplied package contains five direct PDF sources: the 9-page main article, 60-page protocol, 11-page statistical analysis plan, 3-page results supplement, and 1-page administrative statement. Pre-existing usable page-level extraction covered main-article pages 1-9 and results-supplement pages 1-3 (12 pages); the remaining 72 pages were mapped directly from source. Direct sources remained authoritative; reusable text, OCR, rendered pages, and document maps were used only as provenance, mapping, or transcription aids.

Source and reuse inventories: [source inventory](<review_1_5_1/source_inventory.md>), [reused-evidence inventory](<review_1_5_1/evidence_asset_inventory.md>), [source hashes](<review_1_5_1/source_hashes_before.sha256>), and [reused-artifact hashes](<review_1_5_1/reused_artifact_hashes_before.sha256>).

## Scope, Complete Coverage, and Exclusions

| Source | Units | Reusable | Fresh-required | Mapped | Status |
|---|---:|---:|---:|---:|---|
| `jama_parsons_2020_oi_190140.pdf` | 9 | 9 | 0 | 9 | COMPLETE |
| `joi190140supp1_prod.pdf` | 60 | 0 | 60 | 60 | COMPLETE |
| `joi190140supp2_prod.pdf` | 11 | 0 | 11 | 11 | COMPLETE |
| `joi190140supp3_prod.pdf` | 3 | 3 | 0 | 3 | COMPLETE |
| `joi190140supp4_prod.pdf` | 1 | 0 | 1 | 1 | COMPLETE |
| **Total** | **84** | **12** | **72** | **84** | **COMPLETE** |

The review covered numeric, denominator, inferential-statistical, cross-document, measure/label, and rate/count relationships. It excluded broad methodological, clinical, misconduct, raw-data, and conclusion-validity audits. The coverage manifest records every source and review shard: [coverage manifest](<review_1_5_1/coverage_manifest.md>).

## Quantitative and Statistical Relationship Coverage

The canonical inventories contain 31 numeric/reporting relationships (`N001`-`N031`) and 17 inferential-statistical relationships (`S001`-`S017`). Numeric and cross-source checks completed their full assigned scope. Statistical pass 1 and the distinct statistical pass 2 each marked all 17 `S` relationships complete. The pass-2 review added C013 and narrowed the source-comparator statements for C003, C009, and C010; it did not suppress any stable ID. The two statistical reviewers had distinct fresh runtime IDs: `root/statistical_pass_1` and `root/statistical_pass_2`.

Artifacts: [numeric relationships](<review_1_5_1/relationships/numeric_relationship_inventory.md>), [statistical relationships](<review_1_5_1/statistics/relationship_inventory.md>), [pass 1](<review_1_5_1/checkers/statistical_pass_1.md>), [pass 2](<review_1_5_1/checkers/statistical_pass_2.md>), [mechanical recheck](<review_1_5_1/verification/evidence_recheck.md>), and [quality audit](<review_1_5_1/quality/evidence_quality_audit.md>).

## Candidate Index

| ID | Category | Candidate |
|---|---|---|
| C001 | Cross-document numeric inconsistency | Randomization age-stratum boundary differs |
| C002 | Analysis-unit or population inconsistency | Eligibility age/Gleason boundary differs |
| C003 | Measure, label, or scale inconsistency | Composite-progression comparator requires version confirmation |
| C004 | Cross-document numeric inconsistency | Fourth counseling phase is 16 versus 17 months |
| C005 | Denominator, proportion, or total inconsistency | Per-protocol percentages do not reproduce |
| C006 | Denominator, proportion, or total inconsistency | PSA categories do not exhaust displayed denominators |
| C007 | Measure, label, or scale inconsistency | Narrative calls gram-per-day values “servings” |
| C008 | Denominator, proportion, or total inconsistency | Pilot total 74 versus table total 68 |
| C009 | Cross-document numeric inconsistency | Energy 24-month cross-group P value differs |
| C010 | Cross-document numeric inconsistency | Deep-yellow-vegetable cross-group P value differs |
| C011 | Cross-document numeric inconsistency | Intervention red-meat P value differs |
| C012 | Cross-document numeric inconsistency | Control red-meat P value differs |
| C013 | Cross-document numeric inconsistency | Deep-yellow-vegetable control change differs |

## Candidate Evidence Cards

## C001 — Randomization age-stratum boundary differs across the main article and final support documents

**Candidate statement:** The printed randomization/adjustment age boundary assigns exactly age 70 to opposite strata across the article and final support documents. **Pending Human Adjudication.**

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [main article — PDF p. 2](<../jama_parsons_2020_oi_190140.pdf#page=2>); [protocol — PDF p. 2](<../joi190140supp1_prod.pdf#page=2>), [p. 5](<../joi190140supp1_prod.pdf#page=5>), and [p. 40](<../joi190140supp1_prod.pdf#page=40>); [SAP — PDF p. 2](<../joi190140supp2_prod.pdf#page=2>) and [p. 5](<../joi190140supp2_prod.pdf#page=5>).

**Source evidence:** The article prints `<70` versus `>=70`; Protocol Update 10, the final protocol schema, and the SAP print `<=70` versus `>70`.

**Reported-versus-comparator:** `<70`/`>=70` versus `<=70`/`>70` for the matched randomization/adjustment factor.

**Reasoning procedure:** Compare boundary-set membership for the same labelled factor; the only changed membership is exactly age 70.

**Calculation:** `{age <70}/{age >=70}` and `{age <=70}/{age >70}` differ at age 70; zero tolerance.

**Alternative source-grounded interpretations:** The article may retain historic implementation text, or a correction may not have propagated; randomization-system records are absent.

**Mechanical evidence recheck:** Cited pages and printed comparators were found and matched; the set comparison reproduced. Direct observation is the differing printed boundary; any implementation explanation is inferred. Missing input: randomization-system and adjusted-Cox encoding.

**Quality-control relevance:** A matched stratification definition should identify the boundary consistently.

**Potential downstream evidence impact:** If confirmed, an extractor could copy a different age-stratification definition for trial design or adjusted analysis; propagation or conclusion change is not asserted.

**Human verification steps:** Check the randomization configuration, amendment implementation, and adjusted-model stratum coding for participants exactly age 70.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Eligibility age/Gleason boundary differs across the main article, protocol, and SAP

**Candidate statement:** Eligibility rules print different age-70 pathology allowances. **Pending Human Adjudication.**

**Category:** Analysis-unit or population inconsistency

**Exact source locations:** [main article — PDF p. 2](<../jama_parsons_2020_oi_190140.pdf#page=2>); [protocol — PDF p. 5](<../joi190140supp1_prod.pdf#page=5>), [p. 15](<../joi190140supp1_prod.pdf#page=15>), and [p. 16](<../joi190140supp1_prod.pdf#page=16>); [SAP — PDF p. 1](<../joi190140supp2_prod.pdf#page=1>).

**Source evidence:** The article allows grade group 1 below 70 and grade group 2 or less at 70 or older; protocol/SAP use Gleason `<=6` at age `<=70` and `<=7 (3+4)` only above 70.

**Reported-versus-comparator:** Article `<70`/`>=70` eligibility wording versus protocol/SAP `<=70`/`>70` wording.

**Reasoning procedure:** Compare the stated pathology allowance at the shared boundary age.

**Calculation:** The partitions differ at age 70, where the stated permissible pathology category changes.

**Alternative source-grounded interpretations:** Documents may represent distinct versions; no participant-level screening or eligibility record identifies the governing rule.

**Mechanical evidence recheck:** Locations and statements were matched; the boundary comparison reproduced. Direct observation is the printed rule difference; version history is inferred. Missing input: governing protocol and participant-level application.

**Quality-control relevance:** Eligibility/population definitions should be version-qualified when a boundary changes a stated pathology allowance.

**Potential downstream evidence impact:** If confirmed, an extractor could code a different eligibility population; no downstream use or conclusion effect is claimed.

**Human verification steps:** Identify the governing eligibility version and review classifications for participants exactly age 70.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Composite-progression age-boundary comparator requires version confirmation

**Candidate statement:** The proposed opposite composite-progression age boundary was not reproduced on the cited endpoint pages; a version-confirmation question remains. **Pending Human Adjudication.**

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [main article — PDF p. 3](<../jama_parsons_2020_oi_190140.pdf#page=3>); [protocol — PDF p. 31](<../joi190140supp1_prod.pdf#page=31>); [SAP — PDF p. 1](<../joi190140supp2_prod.pdf#page=1>) and [p. 2](<../joi190140supp2_prod.pdf#page=2>).

**Source evidence:** The article, protocol p. 31, and SAP p. 2 use `<70`/`>=70` in progression-endpoint statements. SAP p. 1 uses `<=70`/`>70` for eligibility, not the cited endpoint comparator.

**Reported-versus-comparator:** Cited endpoint partitions match; the nonmatching SAP p. 1 statement is an eligibility definition.

**Reasoning procedure:** Match endpoint purpose before comparing age partitions; do not transfer an eligibility boundary into an endpoint definition.

**Calculation:** Each cited endpoint partition assigns age 70 to the `>=70` pathology-threshold group; no endpoint boundary-set difference was reproduced.

**Alternative source-grounded interpretations:** Another versioned endpoint definition may exist but is not supplied; the initial comparison may have conflated eligibility with endpoint wording.

**Mechanical evidence recheck:** All cited pages and statements were found. The endpoint comparator did not reproduce; direct observation is the matching endpoint text and separate eligibility text. Missing input: an alternate endpoint version, event classifications, or implementation code.

**Quality-control relevance:** Endpoint labels and definitions should remain distinct from eligibility definitions.

**Potential downstream evidence impact:** If a distinct governing endpoint version is confirmed, an extractor could need a version-qualified endpoint definition; no endpoint, estimate, or conclusion difference is demonstrated.

**Human verification steps:** Determine whether another governing progression-endpoint version uses `<=70`/`>70`, or confirm that the cited matching `<70`/`>=70` definitions governed the analysis.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Fourth counseling phase is printed as 16 months versus 17 months

**Candidate statement:** The same intervention schedule prints phase 4 as 16 months in the article and 17 months in the protocol. **Pending Human Adjudication.**

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [main article — PDF p. 3](<../jama_parsons_2020_oi_190140.pdf#page=3>); [protocol — PDF p. 5](<../joi190140supp1_prod.pdf#page=5>) and [p. 29](<../joi190140supp1_prod.pdf#page=29>).

**Source evidence:** The article states eight calls over 16 months; the protocol twice states eight calls over 17 months within the 24-month, 22-call schedule.

**Reported-versus-comparator:** `16 months` versus `17 months` for the fourth phase.

**Reasoning procedure:** Reconcile printed phase durations and call counts for the matched schedule.

**Calculation:** Article: `1+2+4+16=23` months. Protocol: `1+2+4+17=24` months. Both list `6+4+4+8=22` calls.

**Alternative source-grounded interpretations:** Inclusive or overlapping phase boundaries, or planned versus delivered schedules, could explain the wording; neither is documented.

**Mechanical evidence recheck:** All locations and values were matched; arithmetic reproduced. Direct observation is the duration discrepancy; a boundary convention is inferred. Missing inputs: phase anchors, convention, and delivery logs.

**Quality-control relevance:** Matched intervention descriptions should reconcile duration and total schedule.

**Potential downstream evidence impact:** If confirmed, an intervention-characteristics extractor could copy an inconsistent maintenance-phase duration; no outcome effect is claimed.

**Human verification steps:** Confirm intended/delivered phase duration and document any boundary convention.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Per-protocol completion percentages do not reproduce from the stated arm denominators

**Candidate statement:** The printed completion percentages do not reproduce from the immediately linked arm totals. **Pending Human Adjudication.**

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [main article — PDF p. 4](<../jama_parsons_2020_oi_190140.pdf#page=4>) and [PDF p. 5](<../jama_parsons_2020_oi_190140.pdf#page=5>).

**Source evidence:** The article links 183 (81.7%) and 171 (79.5%) meeting per-protocol criteria to arm totals 226 and 217; listed noncompletion counts independently leave 183 and 171.

**Reported-versus-comparator:** `183 (81.7%)` of 226 and `171 (79.5%)` of 217 versus the displayed arithmetic.

**Reasoning procedure:** Divide each printed numerator by its immediately linked arm total and compare at one decimal place.

**Calculation:** `183/226=80.97%` (81.0% to one decimal), not 81.7%; `171/217=78.80%` (78.8%), not 79.5%.

**Alternative source-grounded interpretations:** Unreported denominators near 224 and 215 may have been used, or the narrative arm totals may not be the percentage denominators.

**Mechanical evidence recheck:** Cited text, numerators, denominators, and noncompletion counts were found; arithmetic reproduced. The denominator linkage is direct; alternate denominators are inferred. Missing input: actual percentage denominators and exclusions.

**Quality-control relevance:** Percentages should be reproducible from stated or clearly identified denominators.

**Potential downstream evidence impact:** If confirmed, adherence or fidelity extraction could copy percentages without reproducible denominators; no primary-conclusion effect is claimed.

**Human verification steps:** Provide the exact denominators, exclusions, and intended displayed percentages.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Table 1 PSA categories do not exhaust the printed PSA denominators

**Candidate statement:** Table 1 displays two PSA categories that leave unlabelled remainders under the printed denominators. **Pending Human Adjudication.**

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [main article — PDF p. 5](<../jama_parsons_2020_oi_190140.pdf#page=5>); [SAP — PDF p. 5](<../joi190140supp2_prod.pdf#page=5>).

**Source evidence:** Table 1 gives PSA denominators 224 and 217, with displayed counts 25/30 for 0-2.5 ng/mL and 99/98 for >2.5-5 ng/mL. The SAP lists a planned >5 to <10 category but Table 1 does not display it.

**Reported-versus-comparator:** Displayed category totals versus the printed PSA denominators.

**Reasoning procedure:** Sum displayed categories; apply exhaustion only conditionally because the table does not state whether its distribution is partial.

**Calculation:** Intervention `25+99=124`, leaving `224-124=100`; control `30+98=128`, leaving `217-128=89`.

**Alternative source-grounded interpretations:** The omitted remainders may be the SAP’s >5 to <10 category, or the Table 1 display may be intentionally partial.

**Mechanical evidence recheck:** Page, counts, and denominators were matched; sums reproduced. The remainders are direct arithmetic; assigning them to the third category is inferred. Missing input: whether categories were intended as exhaustive.

**Quality-control relevance:** A display under stated denominators should identify whether it is exhaustive or partial.

**Potential downstream evidence impact:** If confirmed, baseline-distribution extraction could omit an unlabelled PSA category; no conclusion effect is claimed.

**Human verification steps:** Confirm the scope of the Table 1 PSA display and label any remainder category or partial-display rule.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Narrative calls gram-per-day cruciferous values “servings”

**Candidate statement:** Narrative wording calls values labelled grams/day elsewhere “cruciferous servings.” **Pending Human Adjudication.**

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [main article — PDF p. 5](<../jama_parsons_2020_oi_190140.pdf#page=5>) and [PDF p. 7](<../jama_parsons_2020_oi_190140.pdf#page=7>); [results supplement — PDF p. 2](<../joi190140supp3_prod.pdf#page=2>).

**Source evidence:** Narrative values 43.10 g/d and 6.44 g/d match the `Cruciferous, g/d` row; a distinct servings/day row shows 0.71 and 0.12.

**Reported-versus-comparator:** Narrative “servings” label versus matched `g/d` table values.

**Reasoning procedure:** Match the exact values and intervals to their formal table row, without assuming a conversion.

**Calculation:** Exact-value matching maps 43.10 and 6.44 to grams/day, not to the separate servings/day row.

**Alternative source-grounded interpretations:** “Servings” may be colloquial, while adjacent `g/d` identifies the formal measure.

**Mechanical evidence recheck:** Pages, values, units, and comparison rows were found; identity matching reproduced. Editorial intent is not supplied.

**Quality-control relevance:** Narrative measure labels should agree with the unit and matched table row.

**Potential downstream evidence impact:** If confirmed, an extractor could code grams/day as servings/day; no primary-outcome conclusion effect is claimed.

**Human verification steps:** Confirm which formal cruciferous measure the narrative intended to identify.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — Pilot total of 74 does not match table arm counts totaling 68

**Candidate statement:** A 74-man pilot description and table arm headers total 68 without a subset definition. **Pending Human Adjudication.**

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [protocol — PDF p. 12](<../joi190140supp1_prod.pdf#page=12>).

**Source evidence:** The protocol describes a 74-man randomized pilot with 2:1 allocation; table headers are intervention `n=45` and control `n=23` without a subset footnote.

**Reported-versus-comparator:** Pilot total `74` versus table total `45+23`.

**Reasoning procedure:** Compare the printed population total with arm-header arithmetic, preserving the absent population definition.

**Calculation:** `45+23=68`, six fewer than 74; `45/23=1.96`, approximately 2:1 but not a disposition account.

**Alternative source-grounded interpretations:** The table may represent an evaluable paired-dietary subset; no footnote supplies that definition.

**Mechanical evidence recheck:** Source wording and headers were found; arithmetic reproduced. The 74/68 difference is direct; complete-case explanation is inferred. Missing inputs: original arm totals, completion criteria, and disposition of six participants.

**Quality-control relevance:** A table nested in a stated population needs a denominator/population definition when totals differ.

**Potential downstream evidence impact:** If confirmed, an extractor could conflate randomized and evaluable pilot populations; no main-trial conclusion effect is claimed.

**Human verification steps:** State what `n=45` and `n=23` represent and account for the six-person difference.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C009 — Energy 24-month between-group P value differs between Table 2 and the eTable

**Candidate statement:** The labelled 24-month energy cross-group P value is `.01` in Table 2 and `<.001` in the eTable. **Pending Human Adjudication.**

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [main article — PDF p. 7](<../jama_parsons_2020_oi_190140.pdf#page=7>); [results supplement — PDF p. 2](<../joi190140supp3_prod.pdf#page=2>).

**Source evidence:** Main Table 2 prints components -250.01 and -130.3 kcal/day, contrast -119.71 (95% CI -211.78 to -27.65), and `P=.01`. The eTable prints the same components and labelled cross-group `P<.001`; it does not print the full contrast or interval.

**Reported-versus-comparator:** Table 2 cross-group `P=.01` versus eTable labelled cross-group `P<.001`, with matching displayed components.

**Reasoning procedure:** Match time, measure, components, and labelled cross-group semantics; do not attribute a contrast or interval to the eTable when it does not print them.

**Calculation:** `-250.01-(-130.3)=-119.71`. An interval-based normal calculation is diagnostic only and cannot replace the mixed-model output.

**Alternative source-grounded interpretations:** Different unreported test, model output, analytic version, or production version may exist; none is labelled.

**Mechanical evidence recheck:** Both pages, components, and P values were found. The main contrast/interval is direct; the eTable omission of them was confirmed. Matching is direct at the components and P-value-column level. Missing inputs: unrounded output, covariance, degrees of freedom, contrast matrix, and model definition.

**Quality-control relevance:** Matched repeated inferential reporting should distinguish any different test or output.

**Potential downstream evidence impact:** If confirmed, a secondary-outcome extractor or meta-analytic dataset could copy different P-value metadata for the labelled comparison; no conclusion change is claimed.

**Human verification steps:** Retrieve the exact 24-month energy model output, contrast definition, analytic version, and intended P value.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C010 — Deep-yellow vegetables 24-month between-group P value differs across repeated tables

**Candidate statement:** The labelled 24-month deep-yellow-vegetable cross-group P value is `.004` in Table 2 and `.003` in the eTable. **Pending Human Adjudication.**

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [main article — PDF p. 7](<../jama_parsons_2020_oi_190140.pdf#page=7>); [results supplement — PDF p. 2](<../joi190140supp3_prod.pdf#page=2>).

**Source evidence:** Main Table 2 prints intervention/control changes 0.19/0.05 servings/day, contrast 0.14 (95% CI 0.05 to 0.23), and `P=.004`. The eTable prints 0.19/0.06 and labelled cross-group `P=.003`; it does not print the contrast or interval. C013 separately tracks the 0.05/0.06 component difference.

**Reported-versus-comparator:** Main cross-group `P=.004` versus eTable labelled cross-group `P=.003`.

**Reasoning procedure:** Match the labelled cross-group P-value semantics and time point; retain the eTable’s absent contrast/interval and do not merge its separate component mismatch with this P-value comparison.

**Calculation:** Main displayed components: `0.19-0.05=0.14`; eTable components: `0.19-0.06=0.13`. An interval-based normal calculation is diagnostic only.

**Alternative source-grounded interpretations:** Unrounded components, a distinct output, or different production conventions could explain the values; none is labelled.

**Mechanical evidence recheck:** Both P values and eTable components were found; the eTable did not print the 0.14 contrast or its interval. The P-value comparator is direct; component arithmetic is separate and C013 retains the component candidate. Missing inputs: unrounded estimates, exact model output, covariance, degrees of freedom, and rounding convention.

**Quality-control relevance:** Repeated cross-group P values should agree at displayed precision or identify different output conventions.

**Potential downstream evidence impact:** If confirmed, an extractor could copy inconsistent P-value metadata; no primary-outcome conclusion effect is claimed.

**Human verification steps:** Confirm intended unrounded components, contrast, model output, and cross-group P value; adjudicate C013 separately.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C011 — Intervention red-meat 12-month within-group P value differs across repeated tables

**Candidate statement:** Matching intervention-arm 12-month red-meat results print `.003` in Table 2 and `.001` in the eTable. **Pending Human Adjudication.**

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [main article — PDF p. 7](<../jama_parsons_2020_oi_190140.pdf#page=7>); [results supplement — PDF p. 2](<../joi190140supp3_prod.pdf#page=2>).

**Source evidence:** Both sources print intervention change -11.54 g/day (95% CI -19.03 to -4.06) for the same within-group mixed-model contrast, paired with `.003` and `.001`.

**Reported-versus-comparator:** Table 2 `P=.003` versus eTable `P=.001` for the matched intervention result.

**Reasoning procedure:** Match arm, time, unit, estimate, interval, and within-group semantics.

**Calculation:** Identical displayed estimate and interval establish the matched result. An interval-based normal calculation is diagnostic only.

**Alternative source-grounded interpretations:** Different unreported inferential conventions or production versions could exist, but no difference is labelled.

**Mechanical evidence recheck:** Both pages, result values, intervals, and P values were matched; logical comparison reproduced. Missing inputs: test statistic, degrees of freedom, covariance, unrounded output, and analytic version.

**Quality-control relevance:** Repeated P values for a matched result should agree or state their distinct test definition.

**Potential downstream evidence impact:** If confirmed, a secondary-outcome extractor could copy different intervention-arm P-value metadata; no conclusion effect is claimed.

**Human verification steps:** Provide the model output and test definition that produced each displayed P value.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C012 — Control red-meat 12-month within-group P value differs across repeated tables

**Candidate statement:** Matching control-arm 12-month red-meat results print `<.001` in Table 2 and `.01` in the eTable. **Pending Human Adjudication.**

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [main article — PDF p. 7](<../jama_parsons_2020_oi_190140.pdf#page=7>); [results supplement — PDF p. 2](<../joi190140supp3_prod.pdf#page=2>).

**Source evidence:** Both sources print control change -9.83 g/day (95% CI -17.26 to -2.41) for the same within-group mixed-model contrast, paired with `<.001` and `.01`.

**Reported-versus-comparator:** Table 2 `P<.001` versus eTable `P=.01` for the matched control result.

**Reasoning procedure:** Match arm, time, unit, estimate, interval, and within-group semantics; `<.001` is an inequality display, not a display-zero P value.

**Calculation:** Identical displayed estimate and interval establish the repeated result. An interval-based normal calculation is diagnostic only.

**Alternative source-grounded interpretations:** A production-version or test-definition difference is possible but not printed.

**Mechanical evidence recheck:** Both pages and all printed comparison values were found; logical comparison reproduced. Missing inputs: exact test output, degrees of freedom, covariance, unrounded output, and analytic version.

**Quality-control relevance:** A matched repeated inferential result should not be reported with materially different thresholded P values without explanation.

**Potential downstream evidence impact:** If confirmed, an extractor could copy different control-arm P-value reporting; no conclusion effect is claimed.

**Human verification steps:** Identify the exact mixed-model output and intended displayed P value for the control arm.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C013 — Deep-yellow vegetables 24-month control change differs across repeated tables

**Candidate statement:** The repeated 24-month control change is 0.05 servings/day in Table 2 and 0.06 in the eTable, with the same printed interval. **Pending Human Adjudication.**

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [main article — PDF p. 7](<../jama_parsons_2020_oi_190140.pdf#page=7>); [results supplement — PDF p. 2](<../joi190140supp3_prod.pdf#page=2>).

**Source evidence:** Main Table 2 prints control change 0.05 servings/day (95% CI -0.02 to 0.11); the eTable prints 0.06 with the same interval for the same control/time/measure row.

**Reported-versus-comparator:** Main control component `0.05` versus eTable control component `0.06`, both with interval `-0.02 to 0.11`.

**Reasoning procedure:** Match arm, time point, measure, and interval; retain this component comparison separately from C010’s cross-group P-value comparison.

**Calculation:** `0.06-0.05=0.01` servings/day. Main components give `0.19-0.05=0.14`; eTable components give `0.19-0.06=0.13`, subject to unavailable unrounded values.

**Alternative source-grounded interpretations:** Different unrounded component estimates could round differently while sharing the printed interval, or tables may reflect different production outputs; neither is labelled.

**Mechanical evidence recheck:** Both pages, values, and the corrected source-matched interval `-0.02 to 0.11` were found; subtraction reproduced. The 0.01 difference is direct; unrounded-output explanation is inferred. Missing inputs: unrounded estimates, model output, analytic version, and rounding convention.

**Quality-control relevance:** Repeated component estimates should agree at displayed precision or identify their different basis.

**Potential downstream evidence impact:** If confirmed, an extractor could copy a different component estimate and derive a different displayed subtraction; no conclusion effect is claimed.

**Human verification steps:** Confirm the intended control estimate, unrounded output, table version, and its relation to C010.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If confirmed, these observations could affect fields copied into evidence tables: eligibility and stratification definitions, intervention schedules, denominators, baseline distributions, measure units, component estimates, and P-value metadata. This is a bounded possibility for future data extractors, systematic reviews, meta-analyses, guidelines, and related evidence products. The supplied package does not establish propagation, conclusion change, or harm.

## Limitations and Missing Definitions

The package lacks randomization configuration, participant-level eligibility and endpoint classifications, phase anchors/call logs, several percentage and table-population denominators, editorial intent, unrounded mixed-model output, covariance/contrast matrices, degrees of freedom, and table-production records. A pre-existing results-supplement rendered page lacked a truthful page identity and was excluded; other assets covered that source page. Dense tables required direct PDF confirmation. No structured Office, workbook, or CSV source was supplied. Full detail is in [limitations](<review_1_5_1/limitations.md>).

## Human Adjudication Checklist

For each candidate, verify the cited source pages, determine whether compared statements refer to the same population/time/contrast/version, obtain missing governing definitions or model output where needed, select any action under local editorial or data-governance procedures, and complete the card’s five blank adjudication fields. Do not infer a final correction from this report alone.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

All five direct PDFs were inventoried and their source-unit coverage closed at 84/84 mapped units. Reused artifacts were separately inventoried and hashed before scientific mapping. Candidate pages were mechanically rechecked against direct PDF evidence. The canonical durable artifacts linked above preserve the source mapping, relationship inventories, checker provenance, recheck, and quality audit.

### Agent execution

| Stage | Agent ID | Model | Reasoning effort | Start mode | Primary artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | `run_state.md` |
| reuse_asset_curator | root/reuse_asset_curator | gpt-5.6-terra | medium | FRESH_SPAWN | `evidence_asset_inventory.md` |
| main_quantitative_mapper | root/main_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | `extraction/main_quantitative_evidence.md` |
| support_quantitative_mapper_1 | root/support_mapper_1 | gpt-5.6-terra | medium | FRESH_SPAWN | `parts/support_doc002_p001_p030.md` |
| support_quantitative_mapper_2 | root/support_mapper_2 | gpt-5.6-terra | medium | FRESH_SPAWN | `parts/support_doc002_p031_p060.md` |
| support_quantitative_mapper_3 | root/support_mapper_3 | gpt-5.6-terra | medium | FRESH_SPAWN | `parts/support_docs003_005.md` |
| numeric_consistency_reviewer | root/numeric_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | `checkers/numeric_consistency.md` |
| cross_source_consistency_reviewer | root/cross_source_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | `checkers/cross_source_consistency.md` |
| statistics_pass_1 | root/statistical_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | `checkers/statistical_pass_1.md` |
| evidence_rechecker | root/evidence_rechecker | gpt-5.6-sol | high | FRESH_SPAWN | `verification/evidence_recheck.md` |
| statistics_pass_2 | root/statistical_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | `checkers/statistical_pass_2.md` |
| evidence_quality_auditor | root/quality_auditor | gpt-5.6-sol | high | FRESH_SPAWN | `quality/evidence_quality_audit.md` |
| report_generator | root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN | `parts/report_generation_record.md` |

The complete one-row-per-agent record is the authoritative [agent execution manifest](<review_1_5_1/agent_execution_manifest.md>).

### Performance profile

- **Target basis:** Five supplied PDFs totaling 84 page units, with an initially identified 12-page reusable extraction footprint and 72 pages requiring fresh native/layout mapping; the package is smaller than the 102-page calibration package but has a similar high fresh-source proportion and includes one long 60-page support document.
- **Total source units:** 84
- **Fresh-source units:** 72
- **Target elapsed minutes:** 30-45
- **Started UTC:** 2026-08-18T23:17:52Z
- **Finished UTC:** 2026-08-19T00:12:34Z
- **Observed elapsed minutes:** 54.7
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Full direct-source mapping of 72 previously uncovered protocol/SAP/administrative pages; pass-2 registration and direct recheck of appended C013; cross-artifact evidence and link repairs identified by the quality audit

### Token accounting and cost

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Input tokens | Output tokens | Total tokens | Known token cost (USD) | Complete estimated token cost (USD) |
|---|---:|---:|---:|---:|---:|
| `gpt-5.6-sol` | 0 | 0 | 0 | 0.000000 | __ |
| `gpt-5.6-terra` | 0 | 0 | 0 | 0.000000 | __ |

The runtime did not expose authoritative response-level token counts for the coordinator or specialist agents, so each manifested agent has an `UNAVAILABLE` ledger row and no estimate was fabricated. The displayed zeros are known accounted tokens only, not a complete package-token estimate. Cached input and cache-write counts are input subsets, and reasoning tokens are output subsets; they are not added again to total tokens. Amounts are token-only API-equivalent estimates under the 2026-08-18 pricing snapshot, not invoices. Per-agent detail is in the [token usage summary](<review_1_5_1/token_usage_summary.md>).
