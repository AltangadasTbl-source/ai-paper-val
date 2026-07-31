# Statistical Consistency Candidates — DOC-001 / DOC-004

## Scope

- **Audited documents:** DOC-001, `jama_parsons_2020_oi_190140.pdf` (main article), and DOC-004, `joi190140supp3_prod.pdf` (results supplement).
- **Not audited:** DOC-002 protocol, DOC-003 SAP, and DOC-005 administrative material.
- **Method boundary:** This check uses only reported point estimates, 95% CIs, P values, column/footnote labels, and their repetition across these two documents. It does not infer unreported modeling assumptions or use CI symmetry.

## Candidate 1 — Repeated 24-month energy between-group P value is incompatible

- **Status/category/severity:** Candidate; Statistical reporting inconsistency; Moderate.
- **Issue statement:** The main article and the results supplement print the same 24-month energy-change inputs for the intervention-versus-control contrast, but report non-overlapping P-value statements for that contrast.
- **Main-article evidence:** DOC-001, `jama_parsons_2020_oi_190140.pdf`, PDF p. 7 (printed p. 146), Table 2, row **Energy, kcal/d**, **24-Month Change / Between-Group Difference**: intervention change **−250.01** (95% CI, **−315.43 to −184.59**); control change **−130.3** (95% CI, **−195.08 to −65.52**); between-group change **−119.71** (95% CI, **−211.78 to −27.65**), **P = .01**. Table footnote d labels this comparison “Changes in intervention compared with changes in control.”
- **Supplement evidence:** DOC-004, `joi190140supp3_prod.pdf`, PDF p. 2, **eTable**, row **Energy (kcal/day)**, **24-month**: intervention change **−250.01** (95% CI, **−315.43, −184.59**) and control change **−130.3** (95% CI, printed **--195.08, −65.52**); the intervention 24-month **p-value† is < 0.001**. The eTable footnote defines † as “changes in intervention compared to changes in control” and says “p-values based on a mixed model analysis.”
- **Reported-versus-comparator check:** \(−250.01 − (−130.30) = −119.71\) kcal/day, exactly the DOC-001 reported between-group estimate and with the same direction. Thus the p-value† in DOC-004 is labeled for the same displayed contrast as DOC-001’s between-group P value.
- **Why this is a discrepancy:** A P value displayed as **.01** cannot also be **<.001** under ordinary rounding/reporting: `.01` represents a value around one hundredth (even a broad two-decimal rounding interval is 0.005 to <0.015), whereas `<.001` is below 0.001. This conclusion does not rely on CI symmetry. Both values are below .05, so the significance direction agrees, but the reported strength of evidence does not.
- **Bounded impact:** The documents disagree on the numerical P value for one reported dietary contrast; this does not reverse the stated direction or the binary .05 significance interpretation.
- **Human verification:**
  1. In DOC-001 p. 7, verify that `.01` is in the 24-month Energy **Between-Group Difference P Value** column.
  2. In DOC-004 p. 2, verify that `< 0.001` is the Energy 24-month **p-value†**, with † defined as the intervention-versus-control change comparison.
  3. Confirm whether a different prespecified analysis population/model was intended despite the identical displayed change estimates; a documented different analysis would resolve the apparent repeated-result inconsistency.

## Candidate 2 — Supplementary eTable reports a 95% CI excluding zero with P = .15 for its labelled within-group contrast

- **Status/category/severity:** Candidate, **Uncertain pending model-output confirmation**; Statistical reporting inconsistency; Moderate.
- **Issue statement:** In the result supplement, the 24-month control-group vegetable-juice change is reported with a 95% CI entirely below the null value, but the P value printed in the same labelled within-group column is .15.
- **Evidence:** DOC-004, `joi190140supp3_prod.pdf`, PDF p. 2, **eTable**, row **Vegetable juice (servings/day)**, control **24-month** columns: mean change **−0.1** (95% CI, **−0.13, −0.06**) and **p-value* = 0.15**. The eTable footnote defines `*` as “within-group changes, values at each follow-up compared to baseline” and states that “p-values [are] based on a mixed model analysis.”
- **Reported-versus-comparator check:** The null for a mean change is **0 servings/day**. The printed interval has upper bound **−0.06**, so it excludes 0 by 0.06 servings/day; the printed P value **.15** is greater than .05.
- **Why this is a candidate, not a conclusive error:** If the displayed 95% CI and P value are output for the same two-sided mixed-model within-group contrast indicated by the table labels, exclusion of 0 corresponds to P < .05, contrary to P = .15. The table explicitly connects the P values to a mixed model but does not explicitly state how its CIs were constructed; therefore the common contrast/model linkage must be checked before treating this as confirmed. No CI-symmetry assumption was used.
- **Bounded impact:** At face value, the CI conveys a statistically nonzero reduction while the P value conveys a nonsignificant within-control change; this affects only this supplementary correlative outcome, not the primary progression outcome.
- **Human verification:**
  1. Verify the control 24-month Vegetable juice cell and its adjacent `p-value*` cell on DOC-004 p. 2.
  2. Verify from the analysis output whether that 95% CI and P value use the same model, contrast, and sidedness.
  3. If they do, recompute or inspect the intended P value; if not, annotate the distinct CI method/estimand and reject this candidate.

## Candidate 3 — Repeated 12-month red-meat within-group P values differ across the article and supplement

- **Status/category/severity:** Candidate; Statistical reporting inconsistency; Low.
- **Issue statement:** For identical displayed 12-month red-meat change estimates and CIs, the main article and eTable give different within-group P values in both arms.
- **Main-article evidence:** DOC-001, `jama_parsons_2020_oi_190140.pdf`, PDF p. 7 (printed p. 146), Table 2, row **Red meat, g/d**, **12-Month Change**: intervention **−11.54** (95% CI, **−19.03 to −4.06**), **P = .003**; control **−9.83** (95% CI, **−17.26 to −2.41**), **P < .001**. These are within-group P-value columns under Table 2 footnote c (“For within-group changes, values at each follow-up compared with baseline.”).
- **Supplement evidence:** DOC-004, `joi190140supp3_prod.pdf`, PDF p. 2, **eTable**, row **Red meat (gm/day)**, **12-month**: intervention **−11.54** (95% CI, **−19.03, −4.06**), **p-value* = 0.001**; control **−9.83** (95% CI, **−17.26, −2.41**), **p-value* = 0.01**. The `*` footnote has the same within-group baseline-to-follow-up definition.
- **Reported-versus-comparator check:** The point estimates and both CI endpoints agree across the two tables to their displayed precision, while the P values differ: intervention `.003` versus `.001`, and control `<.001` versus `.01`. Standard three-decimal rounding intervals for `.003` and `.001` do not overlap; `<.001` also cannot denote a value that rounds to `.01`.
- **Bounded impact:** All four printed P-value statements are below .05 and each repeated CI excludes 0, so the discrepant decimal reporting does not change the reported direction or binary significance conclusion for this correlative outcome.
- **Human verification:**
  1. Verify the two 12-month within-group P-value cells in the DOC-001 Table 2 red-meat row.
  2. Verify the corresponding two `p-value*` cells and `*` footnote in the DOC-004 eTable.
  3. Check whether the two tables intentionally used distinct analysis populations or degrees-of-freedom methods; if so, label the outputs accordingly. If not, correct/reconcile the repeated P values.

## Exclusions

- No candidate was raised for the main primary-outcome HRs, their 95% CIs, or their P values: all reported HR CIs include the null HR of 1 and their P values exceed .05.
- A DOC-001/DOC-004 24-month deep-yellow-vegetable P-value difference (`.004` versus `.003`) was not retained because adjacent three-decimal rounded displays can meet at a rounding boundary and the package does not identify a common unrounded value/model output.
