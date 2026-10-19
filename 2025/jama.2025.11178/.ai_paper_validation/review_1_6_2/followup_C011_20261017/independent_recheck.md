# C011 focused independent source recheck

Scope: C011 only, including all three subset blocks and all three time points in eTable 8. This follow-up preserves every existing candidate and artifact. Status remains Pending Human Adjudication.

## Source inspection and direct observations

The supplied results supplement `joi250046supp4_prod_1755300121.15587.pdf` was visually inspected through its existing CPU-rendered page images at `preprocessing/stat1_reports/doc005_p4.png`, `doc005_p7.png`, `doc005_p8.png`, `doc005_p9.png`, `doc005_p13.png`, and `doc005_p14.png`. These images show the exact printed pages; OCR and extracted text were not treated as final authority. No new extraction or rendering was necessary.

| Source location | Source content matched | Significance for C011 |
|---|---|---|
| [PDF p.4, Adjustment](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4) | Additional predictors significant at the 0.10 level in both missingness and outcome models were added to the imputation and estimation models for the main analysis. The base set contains pain severity, age, sex, site, residency, multisite pain, and mental health conditions. | Distinguishes the base set from additional selected predictors. |
| [PDF p.7, eTable 2, FINAL VARIABLES SELECTED](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7) | The final additional variables for imputation and estimation models are education and unemployment. | Both variables were selected for the full primary analysis. |
| [PDF p.8, eTable 3](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8) | The fitted primary imputation model contains education rows and a Not employed row. | Selection is corroborated by fitted-model reporting. |
| [PDF p.9, eTable 4](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9) | The fitted primary estimation model contains education rows and Not employed (vs. Employed), alongside the base variables. | Both variables appear in the actual reported full primary estimation model. |
| [PDF p.13, Protocol Change Subset Analyses](../../../joi250046supp4_prod_1755300121.15587.pdf#page=13) | eTable 8 presents “the results of the primary analysis restricting to subsets of the randomized population”. | The wording connects the subset results to the primary analysis. |
| [PDF p.14, eTable 8 footnote b](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14) | “Adjustment variables: Sex, age, site, rural vs. urban residence, more than 1 musculoskeletal pain condition, presence of mental health diagnosis, and pain severity at baseline.” | Seven base factors are listed; education and employment are absent from this list. The footnote applies to all nine rows below. |

## Complete affected-location check

The following nine row locations were visually found and matched on PDF p.14. Values are the printed adjusted RRs for painTRAINER versus usual care, health coach versus usual care, and health coach versus painTRAINER, respectively. They identify every affected result; they are not claims of numeric inconsistency.

| Subset | Time | PT vs UC RR | HC vs UC RR | HC vs PT RR | Shared adjustment footnote |
|---|---|---:|---:|---:|---|
| Randomized prior to 8/9/2021 | 3 months | 0.96 | 1.34 | 1.39 | b: seven base factors; education/employment not named |
| Randomized prior to 8/9/2021 | 6 months | 1.31 | 1.29 | 0.98 | b: same |
| Randomized prior to 8/9/2021 | 12 months | 1.59 | 1.84 | 1.16 | b: same |
| Enhancement to painTRAINER, randomized after 8/9/2021 | 3 months | 1.37 | 1.60 | 1.17 | b: same |
| Enhancement to painTRAINER, randomized after 8/9/2021 | 6 months | 1.53 | 1.72 | 1.13 | b: same |
| Enhancement to painTRAINER, randomized after 8/9/2021 | 12 months | 1.29 | 1.33 | 1.03 | b: same |
| Reminder letters added, randomized after 3/31/2022 | 3 months | 1.54 | 1.67 | 1.08 | b: same |
| Reminder letters added, randomized after 3/31/2022 | 6 months | 1.67 | 1.90 | 1.14 | b: same |
| Reminder letters added, randomized after 3/31/2022 | 12 months | 1.46 | 1.49 | 1.02 | b: same |

## Separate recheck fields

- **Location found:** Yes; p.4 and pp.7–9 establish the full primary covariate specification and fitted models; pp.13–14 establish attribution and the subset adjustment list. All nine subset rows were inspected.
- **Source value/text matched:** Yes; education and unemployment are explicitly selected and fitted in the full analysis; eTable 8 names seven base factors.
- **Comparator matched:** Yes, at the level of primary-analysis method attribution and reported covariate membership. These are different populations, so their numerical results are not duplicate estimates required to agree.
- **Consistency rule applicable:** Statistical-method reporting logic, focus area C. Calling results the primary analysis restricted to subsets leaves unclear whether the same selected covariates were retained when its shared footnote lists only the base factors. This is a bounded specification/comparability question, not proof that a fitted subset model omitted either predictor.
- **Calculation/logical comparison reproduced:** The two membership descriptions differ by education and employment. No arithmetic comparison is needed to establish that printed difference.
- **Display-precision interval check:** Not applicable to categorical model membership. None of the nine subset RRs is claimed to disagree arithmetically with the full-cohort RR. No rounding-based numeric finding is asserted for C011.
- **Necessary inputs available:** Sufficient to reproduce the reported specification difference and full-model inclusion; insufficient to establish the actual subset design matrices, selected-variable lists, or resulting numerical impact.
- **Exact missing inputs/definitions:** Whether footnote b is exhaustive; subset-specific imputation and estimation design matrices or equivalent complete specifications; whether selection was repeated in each subset; whether the additional variables were retained, reselected, or deliberately omitted; and a model comparison holding the subset and all other procedures fixed.
- **Source-grounded alternative interpretation:** Footnote b may abbreviate a broader adjustment set. Alternatively, restricting the population may have involved refitting or repeating the described selection procedure; that can yield a different selected set while following the same overall procedure. The printed materials do not distinguish these explanations.
- **Direct observation versus inference:** Direct: full fitted models include education/employment, and the subset footnote does not name them. Inference not established: those terms were absent from the actual subset fits, or their absence generated any particular RR/CI/NNT. Silence in eTable 8 does not establish that imputation or IPW was absent.
- **Exact remaining human question:** For each of the three eTable 8 subsets, what complete covariate sets and missing-data procedures produced the nine rows? Does footnote b abbreviate the specification, or did the subset models use a changed/reselected set, and how does that relate to the statement “primary analysis restricting to subsets”?

## Classification and evidence state

- **Document roles:** REPORT at every compared location, because all describe implemented analyses and results in the non-plan results supplement. The phrase protocol changes does not make this retrospective result description PLAN material.
- **Primary relationship:** S_W. **All relationships:** S_W. Both sides are within the same report document; no P_R, P_P, or S_C relationship is established for C011.
- **Review domain:** statistical_results, because the observation concerns statistical model specification and comparability. Existing classification is confirmed without correction.
- **Evidence state:** reproduced. The determining fact is the source-confirmed difference between the full primary model's explicit selected/fitted education and employment terms and the subset results' primary-analysis attribution plus seven-factor footnote. This evidence state describes reproduction of the reported specification discrepancy only; it does not establish actual omitted terms or a numerical contradiction.

## Downstream implications and boundaries

The immediate consequence is incomplete model comparability and reproducibility for eTable 8. A data extractor could code the subset results as adjusted for education/employment or as adjusted only for the seven base factors depending on which description is followed. The affected numerical results include adjusted percentages, RRs, confidence intervals, and derived NNTs, but their sensitivity to either predictor cannot be quantified from these materials.

For example, the full primary 3-month painTRAINER-versus-usual-care RR is 1.28 (1.06–1.55) on p.9; the post-enhancement subset RR is 1.37 (1.11–1.69) on p.14. The populations differ, so this contrast cannot isolate an education/employment adjustment effect. It is not evidence that C011 changes statistical significance or the trial's main conclusion. The subset results also overlap participants with the full-cohort results and must not be treated as independent studies in evidence synthesis.

Page 13 expressly states that the enhancement analysis was prespecified and that the reminder-letter analysis was post hoc. That disclosure is context, not an additional C011 discrepancy.
