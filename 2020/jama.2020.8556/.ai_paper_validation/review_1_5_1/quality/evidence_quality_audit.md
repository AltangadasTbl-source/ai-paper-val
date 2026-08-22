# Evidence Quality Audit

## Audit scope and coverage status

This audit covers the complete source-coverage ledger, all 16 coverage-manifest rows, both quantitative evidence maps, the canonical numeric inventory `N001` through `N071`, the canonical statistical inventory `S001` through `S093`, every numeric, cross-source, and statistical checker output, both statistical passes, the stable candidate ledger, the mechanical evidence recheck, and the execution manifest. Direct source pages cited by candidates were inspected at their physical PDF page locations. Reused extraction was treated only as a locator or transcription aid.

- **Audit status:** Complete for the artifacts available at the evidence-quality stage, with coordinator repairs listed below.
- **Direct-source closure:** Four source rows, 100 PDF-page units, 23 reusable-backed units, 77 fresh-required units, and 100 mapped units. Every row satisfies reusable plus fresh-required equals total, mapped equals total, and `COMPLETE` status.
- **Manifest structure:** Every one of the 16 manifest rows contains one undecorated relative artifact path. After this audit artifact is written, 15 paths resolve. The report-generation path does not yet resolve because report generation remains pending.
- **Numeric relationship closure:** `N001` through `N071` are contiguous and all 71 receive an explicit numeric-checker record.
- **Statistical relationship closure:** `S001` through `S093` are contiguous and all 93 receive explicit `PASS_1_COMPLETE` and `PASS_2_COMPLETE` records.
- **Independent statistical runs:** `root/statistical_pass_1` and `root/statistical_pass_2` are distinct fresh runtime IDs. Both execution-manifest rows record `gpt-5.6-terra`, high reasoning effort, `FRESH_SPAWN`, and one primary artifact.
- **Execution-manifest closure at this stage:** The manifest has 10 unique agent IDs, records the current coordinator exactly once, and records every specialist used through the evidence-quality stage exactly once with one primary artifact. A report-generator row is not yet expected because that stage remains pending; it must be added if a new runtime is spawned.
- **Discovery boundary:** The source inventory, evidence maps, inventories, checkers, and candidate registration state complete assigned scopes and no candidate-count boundary. No evidence indicates that a top-N boundary or an old candidate list controlled discovery.
- **Display-zero rule:** Neither statistical inventory nor either pass records `P = 0`, `p = 0.000`, or equivalent. No stable candidate mentions a display-zero P value, so no independent-contradiction field is triggered.
- **Stable-ID identity at this stage:** The candidate ledger, evidence recheck, and this quality audit each contain exactly `C001`, `C002`, `C003`, `C004`, `C005`, `C006`, `C007`, and `C008`. The final report is not yet available, so four-artifact identity remains an open completion check.
- **Categories and tone:** Every candidate uses one category exactly permitted by `QUALITY_CONTROL_SCOPE.md`. The language remains neutral and every candidate remains `Pending Human Adjudication`. No candidate is assigned an adjudicative outcome or priority label.

## Report-card field audit

The current canonical candidate ledger is a registration artifact, not the final evidence-card artifact. For every `C` ID below, the ledger has the exact `Category` label but does not yet have the other exact report-card labels required by `report_spec.md`: `Candidate statement`, `Exact source locations`, `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Alternative source-grounded interpretations`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields`. Much of the substantive content exists under different ledger labels and in the recheck; the report generator must place it under the exact required labels without changing the stable ID set.

For every final evidence card, the human-adjudication block must be exactly:

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

No existing ledger or recheck entry contains a populated human-adjudication subfield. Final-report conformity cannot be confirmed until that artifact exists.

## C001 — Person-day totals do not reconcile with stated mean follow-up days

- **Status:** Pending Human Adjudication.
- **Evidence support and pagination:** The cited values are visibly present on [the main article, physical PDF page 4](<../../../jama_butler_2020_oi_200054.pdf#page=4>). The page prints both arm totals, both per-participant means, 155 randomized per arm, and 152/153 in the primary analysis. The page citation is truthful.
- **Missing report-card fields:** All exact fields identified in the report-card field audit above except `Category`.
- **Rule, assumptions, and alternative:** The total-equals-mean-times-participant-count rule is applicable only if the total and mean use the same participant set and day definition. The recheck states this condition and names the missing participant, day-inclusion, missing-day, weighting, and unrounded-mean definitions. It does not assume an unreported denominator.
- **Arithmetic:** The ledger and recheck correctly reproduce `39,798/155 = 256.7613`, `37,974/155 = 244.9935`, `39,798/152 = 261.8289`, and `37,974/153 = 248.1961`. The numeric checker contains a secondary arithmetic transcription in its tolerance paragraph: `37,974 - 242.9 x 155` is `324.5`, not `325.5`. This does not alter the candidate relationship.
- **Duplicate-relationship check:** No stable candidate duplicates this total/mean identity. `N010` is the sole registered relationship basis.
- **Conclusion and downstream wording:** The ledger does not claim a paper-level conclusion change. The final card should bound downstream impact to possible copying of the person-time total, mean follow-up, or exposure denominator if the candidate is confirmed.
- **Coordinator repair:** Correct the numeric checker's `325.5` to `324.5`; preserve the conditional same-population/day-definition wording in the final card.

## C002 — Administration-method percentage conflicts with its printed fraction

- **Status:** Pending Human Adjudication.
- **Evidence support and pagination:** The attached percentage and fraction are visibly present in the Intervention Fidelity paragraph on [the main article, physical PDF page 4](<../../../jama_butler_2020_oi_200054.pdf#page=4>). The citation is truthful, and the same sentence supplies the two other route counts and percentages.
- **Missing report-card fields:** All exact fields identified in the report-card field audit above except `Category`.
- **Rule, assumptions, and alternative:** No unreported model assumption is needed for the printed fraction identity. A different eligible-dose denominator is a source-grounded alternative only as a missing definition; it is not treated as established.
- **Arithmetic:** `68,356/73,302 x 100 = 93.2525716%`, which rounds to `93.3%`. The candidate ledger and numeric checker incorrectly transcribe the unrounded result as `93.2539%`; the evidence recheck gives the reproducible value `93.2526%`. The three counts sum to `73,302`, and the other two displayed percentages reproduce to one decimal.
- **Duplicate-relationship check:** No stable candidate duplicates this route-percentage identity. It is distinct from C003, which concerns the median and IQR in the neighboring text.
- **Conclusion and downstream wording:** The final card should limit downstream impact to possible copying of the administration-route percentage or fraction; it should not infer an effect on the trial conclusion.
- **Coordinator repair:** Replace `93.2539%` with `93.2526%` in `candidate_ledger.md` and `checkers/numeric_consistency.md`. Retain the rounded comparator `93.3%`.

## C003 — Adherence median is below its IQR and conflicts across main and supplement

- **Status:** Pending Human Adjudication.
- **Evidence support and pagination:** The main median and IQR are visible on [the main article, physical PDF page 4](<../../../jama_butler_2020_oi_200054.pdf#page=4>), and the supplement median with the identical IQR is visible on [Supplement 2, physical PDF page 5](<../../../joi200054supp2_prod.pdf#page=5>). Both citations are truthful.
- **Missing report-card fields:** All exact fields identified in the report-card field audit above except `Category`.
- **Rule, assumptions, and alternative:** The within-main ordering check is independent of cross-source population identity: a conventional median cannot lie below its lower quartile. Equality of the two cross-source summaries is definition-limited because the supplement does not explicitly name the descriptive-adherence population. The recheck correctly separates those two bases and names the missing population, record-inclusion, and quantile definitions.
- **Arithmetic:** `93.56% - 93.3% = 0.26` percentage points and `97.8% - 93.3% = 4.5` percentage points. Display precision cannot reverse the within-main ordering.
- **Duplicate-relationship check:** The pre-registration merge of `NC-N011-02` and `XSC-001` is a genuine duplicate merge because both concern the same two medians, shared IQR, and ordering/cross-source rule. C003 and C008 both cite `S080`, but they concern different printed quantities and different rules: adherence median/IQR versus CACE coefficient/interval/P-value compatibility.
- **Conclusion and downstream wording:** The final card should bound impact to possible copying of the pooled adherence median or its use as CACE context. It should not state that the CACE or paper conclusion is wrong.
- **Coordinator repair:** In the final card, present the independently sufficient within-main ordering first and the definition-limited cross-source comparison second.

## C004 — Nonprophylactic-antibiotic percentages conflict with printed counts and denominators

- **Status:** Pending Human Adjudication.
- **Evidence support and pagination:** The overall and arm-specific values are visible on [the main article, physical PDF page 5](<../../../jama_butler_2020_oi_200054.pdf#page=5>). The alternative 152/153 primary-analysis denominator context is printed on [physical PDF page 4](<../../../jama_butler_2020_oi_200054.pdf#page=4>). Both page references are truthful.
- **Missing report-card fields:** All exact fields identified in the report-card field audit above except `Category`.
- **Rule, assumptions, and alternative:** The explicit `/155` fraction checks need no unreported assumption. The alternative denominators are diagnostic because the source does not define them as outcome-specific denominators, and their arm order is opposite the printed primary-analysis counts.
- **Arithmetic:** `97/155 = 62.5806%`, `105/155 = 67.7419%`, and `202/310 = 65.1613%`, rather than the displayed `63.4%`, `69.1%`, and `66.2%`. The alternatives reproduce at one decimal: `97/153 = 63.3987%`, `105/152 = 69.0789%`, and `202/305 = 66.2295%`.
- **Duplicate-relationship check:** No other stable candidate addresses these antibiotic-exposure fractions.
- **Conclusion and downstream wording:** The final card should limit downstream impact to possible extraction of the descriptive antibiotic-exposure percentages, counts, or denominators.
- **Coordinator repair:** Add main-article physical PDF page 4 to the final card's exact locations whenever the 152/153 alternative-denominator explanation is retained; the current ledger cites only page 5 while relying on page 4 for that context.

## C005 — Three-month oral-candidiasis ARD conflicts with printed proportions and supplement

- **Status:** Pending Human Adjudication.
- **Evidence support and pagination:** The main fractions and ARD are visible on [the main article, physical PDF page 7](<../../../jama_butler_2020_oi_200054.pdf#page=7>), and the matched fractions and difference are visible on [Supplement 2, physical PDF page 8](<../../../joi200054supp2_prod.pdf#page=8>). Both citations are truthful.
- **Missing report-card fields:** All exact fields identified in the report-card field audit above except `Category`.
- **Rule, assumptions, and alternative:** The raw proportion difference is directly reproducible. The main ARD must not be assumed to be crude because its estimator and direction are not stated. The candidate properly leaves an adjusted or model-derived contrast as an alternative and asks for its estimator, population, direction, and variance method.
- **Arithmetic:** `88/113 = 77.8761%` and `80/105 = 76.1905%`; probiotic minus placebo is `+1.6856` percentage points and the reverse is `-1.6856`. Neither direction rounds to `-0.2%`. The supplement's `0.02` proportion-scale difference is compatible with the raw fractions. The main interval midpoint is `-0.2%`, so the main interval is internally centered while its relationship to the fractions remains unresolved.
- **Duplicate-relationship check:** C005 is distinct from the matched odds-ratio endpoint issue in C006. Statistical pass 1's decision not to infer an ARD sign from an unnamed reference does not suppress C005, because the arithmetic was checked in both directions and the supplement repeats the same fractions with a different displayed difference.
- **Conclusion and downstream wording:** The final card should bound impact to extraction of the three-month oral-candidiasis difference estimate and interval. It should not infer a changed microbiology or paper conclusion.
- **Coordinator repair:** Preserve the distinction between the direct fraction arithmetic and the unresolved possibility of an adjusted main ARD.

## C006 — Matched B animalis interval has two different lower endpoints

- **Status:** Pending Human Adjudication.
- **Evidence support and pagination:** The main endpoint is visible on [the main article, physical PDF page 5](<../../../jama_butler_2020_oi_200054.pdf#page=5>), and the supplement endpoint is visible on [Supplement 2, physical PDF page 8](<../../../joi200054supp2_prod.pdf#page=8>). Both citations are truthful.
- **Missing report-card fields:** All exact fields identified in the report-card field audit above except `Category`.
- **Rule, assumptions, and alternative:** Population, time point, counts, effect measure, point estimate, upper endpoint, and P display match. The only necessary assumption is that the repeated records are intended to report the same model result; the possibility of different unrounded output or document versions remains explicit.
- **Arithmetic:** The two lower endpoints differ by `5.95 - 5.94 = 0.01`. Both are printed to two decimals and therefore cannot be identical displayed endpoints.
- **Duplicate-relationship check:** `S004` and `S085` are two locations for the same relationship and were correctly registered as one stable candidate. No other stable candidate duplicates this endpoint transcription check.
- **Conclusion and downstream wording:** The final card should describe a bounded risk that a data extractor may copy one of two lower endpoints. It should not imply a change in the effect direction or paper conclusion.
- **Coordinator repair:** Keep the conclusion limited to a matched-reporting discrepancy and retain the version/output alternative.

## C007 — eTable 4 percentage does not reproduce from 20/119

- **Status:** Pending Human Adjudication.
- **Evidence support and pagination:** The cell `20/119 (16.0)` and its adjacent category rows are visible on [Supplement 2, physical PDF page 7](<../../../joi200054supp2_prod.pdf#page=7>). The citation is truthful.
- **Missing report-card fields:** All exact fields identified in the report-card field audit above except `Category`.
- **Rule, assumptions, and alternative:** The cell fraction identity needs no model assumption. Selecting whether the numerator, denominator, or percentage is intended requires the unsupplied underlying tabulation, so the alternatives remain diagnostic.
- **Arithmetic:** `20/119 x 100 = 16.8067%`, which rounds to `16.8%`, not `16.0%`. A supportable same-cell corroboration is omitted from the ledger and recheck: the four placebo three-month category numerators sum to `20 + 20 + 38 + 42 = 120` against the common printed denominator `119`, while their displayed percentages sum to `16.8 + 16.0 + 31.9 + 35.3 = 100.0%`. This supports checking the repeated `20/119` entry but does not establish which element is intended.
- **Duplicate-relationship check:** The fraction/percentage mismatch and the category-total tension arise from the same printed cell and should remain one stable candidate. The adjacent `20/119 (16.8)` row is a comparator, not a separate candidate.
- **Conclusion and downstream wording:** The final card should limit downstream impact to copying this ordinal-candidiasis table cell or category distribution.
- **Coordinator repair:** Add the category-numerator and percentage-sum calculation to C007 as corroborating evidence without creating, merging, or suppressing a stable ID.

## C008 — CACE coefficient, confidence interval, and P value need reconciliation

- **Status:** Pending Human Adjudication.
- **Evidence support and pagination:** The CACE model and positive `x100` presentation rule are visible on [Supplement 2, physical PDF page 3](<../../../joi200054supp2_prod.pdf#page=3>); the printed coefficient, interval, and P value are visible on [Supplement 2, physical PDF page 5](<../../../joi200054supp2_prod.pdf#page=5>); and the two-sided 95% convention is visible on [Supplement 1, physical PDF page 52](<../../../joi200054supp1_prod.pdf#page=52>), internally labeled SAP page 8 of 31. The physical PDF pagination is truthful.
- **Missing report-card fields:** All exact fields identified in the report-card field audit above except `Category`.
- **Rule, assumptions, and alternative:** The off-center printed interval is a direct observation. Compatibility with the P value is conditional on a common symmetric Wald construction on the displayed linear coefficient scale. The ledger and recheck correctly name missing unrounded outputs, standard error, cluster count, degrees of freedom, small-sample correction, CI construction, test statistic, and common-output status. They do not present the diagnostic as a reconstruction of the unreported analysis.
- **Arithmetic:** The midpoint is `(-0.20 + 0.41)/2 = 0.105`, not `0.01`; endpoint distances from `0.01` are `0.21` and `0.40`; half-width is `0.305`. The conditional normal-Wald diagnostics in the recheck are arithmetically reproducible. Multiplication by positive `100` preserves symmetry and does not by itself explain the shifted midpoint.
- **Duplicate-relationship check:** C008 is distinct from C003 despite shared relationship `S080`: C008 concerns the CACE coefficient, interval, and P value, while C003 concerns the descriptive adherence median and IQR.
- **Conclusion and downstream wording:** The final card should bound impact to possible extraction or interpretation of the CACE coefficient, interval, and P value. It must not state that an unreported inferential method is wrong or that the paper conclusion changes.
- **Coordinator repair:** Retain the word `conditional` wherever CI/P compatibility is discussed and include the named missing inferential definitions in the final card.

## Coordinator repair register

1. In `candidate_ledger.md` and `checkers/numeric_consistency.md`, change the C002/`NC-N011-01` unrounded calculation from `93.2539%` to `93.2526%`.
2. In `checkers/numeric_consistency.md`, change the C001/`NC-N010-01` placebo total discrepancy from `325.5` days to `324.5` days.
3. When C004's alternate 152/153 denominators are discussed, add main-article physical PDF page 4 to the exact source locations.
4. Add C007's `120`-versus-`119` category-numerator sum and `100.0%` displayed-percentage sum as corroborating evidence within the same stable card.
5. Generate every final report card with all exact labels and the five exact `__` human-adjudication placeholders; include all eight stable IDs without deletion, renumbering, merging, ranking, or suppression.
6. After this handoff, change the `evidence_quality` manifest row from `ASSIGNED` to `COMPLETE`. After report generation, enumerate `C001, C002, C003, C004, C005, C006, C007, C008` in the report-generation scope, change its status to `COMPLETE`, and confirm its single artifact path resolves.

## Residual limitations and completion checks

- The final Markdown and HTML reports were not present during this audit. Their ID set, exact field labels, local evidence links, bounded downstream wording, conclusion-impact wording, and blank human-adjudication placeholders remain for the post-generation check.
- Final source/reused-artifact hash comparison, token ledger identity, report rendering, and mechanical validator output occur after this evidence-quality stage and are outside the currently available evidence set.
- Candidate-specific participant sets, underlying tabulations, unrounded model outputs, and inferential construction details remain unavailable exactly as named in the evidence recheck. These limitations do not create a direct-source coverage gap.
- Canonical audit artifact: `quality/evidence_quality_audit.md`.
