# C007 bounded source re-exploration and record comparison

This is a targeted re-exploration requested on 2026-10-21, not a new complete Workflow 1.6.2 run. Existing review artifacts remain unchanged. Every new local artifact is confined to this directory. C007 remains Pending Human Adjudication.

## Approach and source authority

The existing ledger was first used only to identify C007 and its source locations. The coordinator then inspected the supplied source passages, compared finite adjustment lists, searched the complete newly extracted main article and results supplement, and only afterward compared the detailed historical checker, screening, recheck, audit and final-report records. A separate fresh evidence-rechecker agent, `/root/c007_source_independent`, was assigned source-only exploration and instructed not to read historical candidate conclusions. Its separate output is `independent_source_check.md`.

Direct Poppler `pdftotext -layout` produced `main_layout.txt`, `plan_layout.txt`, and `results_supp_layout.txt`. The plan extraction has an unusable character mapping and was not treated as readable source evidence. Direct Poppler `pdftoppm` produced targeted CPU page renders; no new OCR or fallback environment was needed. Current direct-tool availability differs from that recorded for the historical run. Source-page visual inspection, rather than the encoded plan extraction, establishes the SAP wording.

## Independent observations

1. PLAN: Supplement 1, PDF p.92, printed SAP p.15, section 35 `Sensitivity Analyses` / section 36 `Adjusted Analyses`, lines 2919-2928. The fully adjusted models explicitly include sociodemographic variables alongside tobacco use form and other baseline characteristics, with education and smoking duration as examples. Site is a random effect. This clause is under the sensitivity heading; section 30 `Primary outcome Analysis` appears separately on PDF p.91, printed SAP p.14. The precise description is a planned adjusted/sensitivity analysis relevant to the primary outcome, rather than a claim that the entire primary analysis is absent.
2. REPORT: Main article PDF p.3, printed p.338, right column `Statistical Analysis`. A mixed-effects model is described with fixed effects for intervention and covariates selected post hoc: age, sex, education, occupation, smoking duration; clusters have random effects. The paragraph also explicitly says that relevant sociodemographic covariates were selected post hoc in the primary analysis. Tobacco-use form has no identified counterpart in the reported list.
3. REPORT: Main article PDF p.4, printed p.339, `Primary Outcome`, repeats the same five covariates and attaches adjusted RR 3.2 (95% CI 2.2-5.2) to them.
4. REPORT: Main article PDF p.6, printed p.341, Table 2 footnote a, repeats that five-variable post hoc adjustment list. The table's CO<10 ppm ITT primary row contains adjusted RR 3.2 (95% CI 2.2-5.2).
5. REPORT: Results supplement PDF p.14, eTable 9 footnote e, repeats age, sex, education, occupation, smoking duration. Its preceding PDF p.13 gives the death-excluded CO<10 ppm adjusted RR 3.1 (95% CI 1.9-6.5). This is an additional occurrence of the same adjustment-description pattern.
6. REPORT: Main article PDF p.5, Table 1, separately records smoking type, concurrent smokeless tobacco use and smoking duration. These are distinct descriptive fields; no supplied mapping establishes that smoking duration represents tobacco-use form in the fitted model. The exact intended coding of the planned form variable is not established.
7. The finite lists agree across the REPORT passages. This is a PLAN-to-REPORT comparison, supporting `P_R` / `protocol_report`, rather than a conflict between two REPORT documents.

## Comparison with existing records

| Record | C007 observation |
|---|---|
| checkers/cross_source_consistency.md, F-XS-003 | Identifies the planned tobacco-form covariate and its absent reported counterpart. |
| checkers/statistical_pass_1.md, F-ST1-005 / S090 | Independently identifies the same planned fully adjusted sensitivity-analysis comparison. |
| screening/inclusion_screen.md, lines 19 and 34 | Both findings are INCLUDE / MEETS_THRESHOLD and map to C007; one candidate represents the shared issue. |
| candidate_ledger.md, C007 starting line 345 | `protocol_report`, `P_R`, `reproduced`, inclusion audit `CONFIRMED`, Route A category 5. |
| verification/evidence_recheck.md, C007 starting line 203 | Confirms the cited plan and report passages; explicitly distinguishes absent reporting from demonstrated exclusion in fitted code. |
| checkers/statistical_pass_2.md, S090 at line 324 | PASS_2_COMPLETE; retains existing C007 without a new duplicate finding. Formula, variable alias and planned-model output remain absent. |
| quality/evidence_quality_audit.md, C007 starting line 209 | CONFIRMED inclusion audit; confines potential impact to adjustment/prespecification metadata and establishes no actual fitted omission or changed conclusion. |
| final_report_1_6_2.md, C007 starting line 512 | Retains C007 with the same classification, evidence state, audit and finding provenance. |

Paths in the record table are relative to `.ai_paper_validation/review_1_6_2/`, except `final_report_1_6_2.md`, which is in `.ai_paper_validation/`.

## Interpretation and limitations

The reproduced observation is a mismatch between an explicit SAP adjustment specification and the repeatedly reported finite post hoc covariate list, together with no identified separate counterpart for the SAP model in the supplied report materials. It does not establish that tobacco-use form was absent from fitted code, that its omission caused bias, or that a particular corrected estimate exists. Possibilities include a description omission, variable alias/combination, or a model amendment; the package does not identify the operative mapping.

The supplied SAP states the specification. Its future-tense language alone does not independently establish when the analysis plan was finalized relative to outcome-data access. The primary/sensitivity heading distinction should be preserved when explaining the existing registration.

The relevant review domain is `protocol_report`, so a downstream analysis conditional on `statistical_results` is not triggered. Nonetheless, an extractor could attach unsupported planned-adjustment or prespecification metadata to RR 3.2 or the death-excluded RR 3.1. Actual changes to those estimates, their CI, evidence-synthesis weights, statistical significance, or clinical conclusions cannot be quantified from this discrepancy. Reported RR 3.0 versus adjusted RR 3.2 does not isolate the tobacco-form contribution because a matching model pair with and without that term is absent. The original counts and denominators are not altered by the covariate-list comparison.

## Source integrity

Direct source SHA-256 values were read and subsequently checked against the existing before-hash list; all three passed:

- Main: `08d435cbc9ce99ba2e85de0a0edb7ee8e5015f3970a42550420ac3f9ae4cf103`
- Plan supplement: `0dcbfdf53363088fa65146d05d2f0e58b9c9f2fa001c9d60232207bbdec440a1`
- Results supplement: `a2b6c06f49f22bf3c5557b7943804c7598154d2e7ca40e7fcbad4dc32bed25e6`

No external evidence, raw data, new candidate ID, adjudication, or alteration of any original review record was used.
