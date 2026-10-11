# Workflow 1.6 exact-source evidence recheck

Runtime UUID: `01a12872-9b72-7460-86ab-0229340c9851`. Fresh evidence-rechecker role, `gpt-6.1-sol` / `high`. Scope: every assigned stable ID C001–C015. All IDs remain **Pending Human Adjudication**. Evidence states describe the evidence record; this artifact does not assign a human disposition or a correction.

The normative QUALITY_CONTROL_SCOPE.md and workflow_1_6/review_contract.md, current candidate ledger and current numeric/cross-source evidence were read. Original supplied PDFs were freshly read using direct Poppler text extraction; fresh source-page renders were inspected for Table1 headers, Table2 superscripts, Table5 values, rotated Table4 units, both relevant result figures and historical Table5. Reusable assets served as locators only. No source or reused artifact was changed. No web, external literature, unbundled Python extraction, OCR or GPU was used.

## Direct-source methods and derivatives

Engine: direct `pdftotext` and `pdftoppm`, Poppler 26.01.0, as recorded in tooling_record.md. Every derivative is under `review_1_6/preprocessing/`. Commands actually used:

```bash
for p in 1 4 5 6 7 8 9; do pdftotext -layout -f "$p" -l "$p" jama_flint_2019_oi_190079.pdf ".ai_paper_validation/review_1_6/preprocessing/recheck-main-p${p}-layout.txt"; done
for p in 4 7 9 10 11 12 13 14 15 17 21 29 40 41; do pdftotext -layout -f "$p" -l "$p" joi190079supp1_prod.pdf ".ai_paper_validation/review_1_6/preprocessing/recheck-plan-p${p}-layout.txt"; done
for p in 9 10; do pdftotext -layout -f "$p" -l "$p" joi190079supp2_prod.pdf ".ai_paper_validation/review_1_6/preprocessing/recheck-results-p${p}-layout.txt"; done
pdftotext -layout joi190079supp3_prod.pdf .ai_paper_validation/review_1_6/preprocessing/recheck-sharing-p1-layout.txt
for p in 1 8; do pdftotext -f "$p" -l "$p" jama_flint_2019_oi_190079.pdf ".ai_paper_validation/review_1_6/preprocessing/recheck-main-p${p}-native.txt"; done
for p in 5 6 9; do pdftoppm -r 130 -f "$p" -l "$p" -singlefile -png jama_flint_2019_oi_190079.pdf ".ai_paper_validation/review_1_6/preprocessing/recheck-main-p${p}"; done
for p in 9 10; do pdftoppm -r 130 -f "$p" -l "$p" -singlefile -png joi190079supp2_prod.pdf ".ai_paper_validation/review_1_6/preprocessing/recheck-results-p${p}"; done
pdftoppm -r 130 -f 29 -l 29 -singlefile -png joi190079supp1_prod.pdf .ai_paper_validation/review_1_6/preprocessing/recheck-plan-p29
pdftoppm -r 120 -f 8 -l 8 -singlefile -png jama_flint_2019_oi_190079.pdf .ai_paper_validation/review_1_6/preprocessing/recheck-main-p8
```

Coverage of this recheck: 24 distinct physical PDF pages freshly extracted, seven of those freshly rendered and visually inspected; within the 32-page direct confirmation bound. Direct native text resolves the rotated Table4 layout extraction's reading order; its source render confirms the percent unit. Arithmetic was independently reproduced in JavaScript and by explicit division/sums below. No OCR/source disagreement was observed. Approximate figure readings remain approximate.

## Classification and evidence-state summary

| ID | Primary category | Relationship type | All relationships | Compared document roles | Review domain | Evidence state |
|---|---|---|---|---|---|---|
| C001 | Denominator, proportion, or total inconsistency | S_W | S_W | REPORT / REPORT | statistical_results | recorded_candidate |
| C002 | Denominator, proportion, or total inconsistency | S_W | S_W | REPORT / REPORT | statistical_results | recorded_candidate |
| C003 | Measure, label, or scale inconsistency | S_W | S_W | REPORT / REPORT | report_internal_inconsistency | recorded_candidate |
| C004 | Measure, label, or scale inconsistency | S_W | S_W | REPORT / REPORT; PLAN corroboration only | report_internal_inconsistency | recorded_candidate |
| C005 | Measure, label, or scale inconsistency | S_C | S_C, S_W | REPORT main / REPORT main / REPORT results supplement | report_internal_inconsistency | recorded_candidate |
| C006 | Denominator, proportion, or total inconsistency | S_W | S_W | REPORT / REPORT | statistical_results | recorded_candidate |
| C007 | Denominator, proportion, or total inconsistency | S_W | S_W | REPORT / REPORT | statistical_results | recorded_candidate |
| C008 | Denominator, proportion, or total inconsistency | S_W | S_W | REPORT / REPORT | statistical_results | recorded_candidate |
| C009 | Measure, label, or scale inconsistency | S_C | S_C | REPORT main / REPORT results supplement | report_internal_inconsistency | record_input_error |
| C010 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN / PLAN | plan_material | recorded_candidate |
| C011 | Measure, label, or scale inconsistency | P_P | P_P | PLAN / PLAN; REPORT corroboration only | plan_material | recorded_candidate |
| C012 | Denominator, proportion, or total inconsistency | P_P | P_P | PLAN historical / PLAN | plan_material | recorded_candidate |
| C013 | Denominator, proportion, or total inconsistency | P_P | P_P | PLAN historical / PLAN historical | plan_material | recorded_candidate |
| C014 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN / PLAN | plan_material | recorded_candidate |
| C015 | Measure, label, or scale inconsistency | P_R | P_R | REPORT / PLAN | protocol_report | recorded_candidate |

All provisional categories, roles, primary/all relationship codes and derived domains are confirmed. C009 receives an evidence-state distinction because its comparison assumes an unestablished additive estimand alignment; its permanent registration and classification remain. Counts: 14 recorded_candidate, 1 record_input_error, 0 not_reproduced, 0 repaired_residual. These counts do not assert that all recorded candidates will receive the same human decision.

## C001 — Hyperlipidemia percentages and arm denominators

- **Location found:** Yes. [Main PDF p.5, Table1 headers and hyperlipidemia row](../../../jama_flint_2019_oi_190079.pdf#page=5), freshly extracted and rendered.
- **Source value/text matched:** Yes. Olanzapine n=64 with 18 (29.0%); placebo n=62 with 19 (29.7%). Original source render confirms cell-to-arm placement.
- **Comparator matched:** Yes. The same table's column denominators are 64 and 62; no hyperlipidemia-specific reduced n or denominator footnote is shown.
- **Consistency rule applicable:** With the printed column denominators, percentage equals count/n times100, allowing nearest one-decimal rounding tolerance of 0.05 percentage point.
- **Calculation reproduced:** 100×18/64=28.125%→28.1%; 100×19/62=30.645161%→30.6%. Opposite denominators give 100×18/62=29.032258%→29.0% and 100×19/64=29.6875%→29.7%.
- **Necessary inputs available:** Both counts, arm assignments, column n and printed percentages. Exact missing inputs/definitions: actual cell-specific denominator and intended arm/count assignment are absent; rounding convention is not expressly stated.
- **Source-grounded alternative interpretation:** Missing O data could give an O denominator62, but a P count19 at29.7% needs approximately64, above its printed total62. Counts, percentages or assignments could differ in the underlying data.
- **Direct observation versus inferred explanation:** Printed values fail the stated-header calculation. Swapped denominators are only a reproducible diagnostic, not an established production mechanism.
- **Classification confirmation:** Both locations are REPORT results within one article; primary/all S_W, denominator category, statistical_results. No correction to classification. Ambiguity: unprinted row denominator/assignment.
- **Evidence state:** `recorded_candidate`. Determining recheck fact: source confirms both cells and headers, and ordinary division does not reproduce the printed percentages under those headers.
- **Exact remaining human question:** Which counts, percentages, arm placements and cell-specific denominators were intended for the hyperlipidemia row?

## C002 — Two placebo participants absent from listed living arrangements

- **Location found:** Yes. [Main PDF p.5, Table1 living-arrangement block and placebo header](../../../jama_flint_2019_oi_190079.pdf#page=5), source text and render.
- **Source value/text matched:** Yes. With others49 (79.0%), alone10 (16.1%), senior residence1 (1.6%); placebo n62. No missing/other row or living-arrangement reduced n is printed.
- **Comparator matched:** Yes. Column n62 is the table population. O counts46+17+1 under n64 are corroboration only.
- **Consistency rule applicable:** Integer category sum equals the population only if the block is intended as exhaustive. The source supports an observable accounting deficit but does not explicitly define exhaustiveness.
- **Calculation reproduced:** 49+10+1=60, leaving62−60=2. Printed percentages sum96.7%; the two-person fraction is100×2/62=3.225806%. Each displayed category's percentage independently agrees with denominator62.
- **Necessary inputs available:** Counts, displayed percentages and header n. Exact missing inputs/definitions: missing or unlisted statuses, whether these categories exhaust all participants, and intended handling of missingness.
- **Source-grounded alternative interpretation:** Two participants may have missing or unlisted living-arrangement data. An intentionally incomplete block would reconcile the totals operationally, although that status is unprinted.
- **Direct observation versus inferred explanation:** Total60 versus62 is direct arithmetic. A reporting defect from non-exhaustiveness is conditional; no assignment of the two people is inferred.
- **Classification confirmation:** REPORT header and REPORT categories inside one table; primary/all S_W, denominator category, statistical_results. No correction. Ambiguity: exhaustiveness/missingness.
- **Evidence state:** `recorded_candidate`. Determining recheck fact: the source reproduces the registered two-person accounting gap; its interpretation remains conditional on the named missing definition.
- **Exact remaining human question:** Were the two unaccounted placebo participants missing or in an unlisted category, and were62 and the three displayed categories intended as a complete distribution?

## C003 — DKEFS color-word row points to Barnes footnote

- **Location found:** Yes. [Main PDF p.6, Table2 DKEFS color-word row and footnotes h/i](../../../jama_flint_2019_oi_190079.pdf#page=6), fresh render inspected specifically for superscripts.
- **Source value/text matched:** Yes. Color-word interference condition3 final weighted scaled score bears superscript i; means8.6 (2.9), n60 and7.6 (2.8), n58. Barnes row has no i marker.
- **Comparator matched:** Yes. Footnote i defines Barnes global clinical assessment range0–5, higher worse. Footnote h explicitly defines both DKEFS tasks as scaled1–19, higher better.
- **Consistency rule applicable:** A row's attached scale footnote must identify its measure and accommodate its displayed means.
- **Calculation reproduced:** 8.6−5=3.6 and7.6−5=2.6; both exceed the attached maximum even allowing0.05 rounding. Both are within the DKEFS1–19 range.
- **Necessary inputs available:** Superscript attachment, row values, named measure, both footnotes. Exact missing input: intended marker association, rather than a numerical measurement definition.
- **Source-grounded alternative interpretation:** Footnote h may implicitly cover both DKEFS rows, with i displaced from Barnes. Cognitive values can be correct while their printed marker is inconsistent.
- **Direct observation versus inferred explanation:** Marker i is visibly attached to DKEFS; its text names Barnes. A displaced marker is an explanation, not an assigned correction.
- **Classification confirmation:** REPORT row versus REPORT footnotes in one article; primary/all S_W, measure category, report_internal_inconsistency. No correction. Ambiguity: intended placement.
- **Evidence state:** `recorded_candidate`. Determining fact: direct image confirms i rather than h, and the attached construct/range differs from the named row.
- **Exact remaining human question:** Which marker was intended on the color-word row, and where should the Barnes scale footnote apply?

## C004 — UKU operational criterion contains out-of-range score4

- **Location found:** Yes. [Main PDF p.4, Other Measures of Tolerability](../../../jama_flint_2019_oi_190079.pdf#page=4); supporting [plan p.15, lines709–710](../../../joi190079supp1_prod.pdf#page=15).
- **Source value/text matched:** Yes. Main report states0–3 on each of48items, then2-point increase or a score of3 or4 with an increase from baseline, excluding the separately defined weight items.
- **Comparator matched:** Yes. Range and threshold concern the same UKU item system in the same paragraph. Plan's score3 is supporting corroboration only; its complete adverse-event rule is not equated to the report's whole rule.
- **Consistency rule applicable:** A supposedly attainable score under the stated integer range cannot exceed3.
- **Logical comparison reproduced:** 4>3 by1; score4 is absent from the declared set{0,1,2,3}. The score3 branch remains attainable.
- **Necessary inputs available:** Range and operational branch. Exact missing inputs/definitions: implemented item codes, any recoding and intended criterion wording.
- **Source-grounded alternative interpretation:** The extra4 may be an unattainable, redundant branch with no effect on counts. A1–4 recoding could explain4 only with an additional definition absent here.
- **Direct observation versus inferred explanation:** Printed rule contains4 while range ends3. No adverse-event frequency is inferred incorrect.
- **Classification confirmation:** Substantive discrepancy is REPORT range versus REPORT rule: primary/all S_W, measure category, report_internal_inconsistency. PLAN merely supports the upper attainable code and does not create P_R. No correction. Ambiguity: possible recoding/redundancy.
- **Evidence state:** `recorded_candidate`. Determining fact: direct source reproduces the incompatible printed range and score4 branch.
- **Exact remaining human question:** What UKU item codes and adverse-effect threshold were actually used, and what does4 denote in this paragraph?

## C005 — HbA1c coefficient unit differs from outcome unit

- **Location found:** Yes. [Main p.1 abstract](../../../jama_flint_2019_oi_190079.pdf#page=1), [p.7 secondary outcomes](../../../jama_flint_2019_oi_190079.pdf#page=7), [p.8 Table4](../../../jama_flint_2019_oi_190079.pdf#page=8) and [results supplement p.9 eFigure8](../../../joi190079supp2_prod.pdf#page=9). Rotated Table4 and eFigure8 freshly rendered.
- **Source value/text matched:** Yes. Daily HbA1c estimate−0.0002mg/dL and95%CI−0.0021 to0.0016 occur in abstract and narrative; adjustedP=.99 in narrative. Table4 prints HbA1c,% and eFigure8 prints HbA1c(%) against Day.
- **Comparator matched:** Yes. Main narrative expressly identifies eFigures1–8 as trajectories of those same metabolic variables. Raw Table4 means are corroborating response units, not a matched coefficient estimator.
- **Consistency rule applicable:** A response slope retains the outcome dimension per time unless a response transformation is supplied; percent and mg/dL are different dimensions.
- **Logical comparison reproduced:** The two directly printed response-unit labels differ. No conversion or recalculation of a model slope from raw changes is required; no response-concentration conversion is supplied.
- **Necessary inputs available:** Coefficient, CI, time label and response-unit labels. Exact missing inputs/definitions: any separate concentration-valued HbA1c response/transform and the intended coefficient/CI unit.
- **Source-grounded alternative interpretation:** A separate transformed response could have been modeled, but no such response conversion appears in the compared content. Main text's quadratic-time warning prevents treating252days times the daily coefficient as a cumulative linear difference; that does not itself resolve the dimension mismatch.
- **Direct observation versus inferred explanation:** Printed units differ. A copied unit or response transformation is explanatory speculation only; values/significance are not recomputed.
- **Classification confirmation:** Main coefficient versus main Table4 is S_W; main coefficient versus separate results REPORT eFigure8 is S_C. Both are substantive; primary S_C by precedence, all S_C,S_W; measure category, report_internal_inconsistency. No correction. Ambiguity: unprinted response transform.
- **Evidence state:** `recorded_candidate`. Determining fact: exact source labels retain mg/dL versus% for the identified HbA1c response.
- **Exact remaining human question:** What response dimension/transformation was used for the HbA1c model, and what unit belongs to its daily coefficient and interval?

## C006 — Hospitalization11 of34 and printed32.3%

- **Location found:** Yes. [Main p.8 opening continuation](../../../jama_flint_2019_oi_190079.pdf#page=8), fresh text/render; [main p.7 Table3](../../../jama_flint_2019_oi_190079.pdf#page=7) corroborates numerator11.
- **Source value/text matched:** Yes. Placebo11 (32.3%) of34 relapse participants required psychiatric hospitalization; adjacent O6 (46.2%) of13.
- **Comparator matched:** Yes. Numerator11, denominator34 and percentage32.3 are all explicit in the same sentence, not inferred from unrelated populations.
- **Consistency rule applicable:** Nearest one-decimal percentage rounding of an explicit fraction.
- **Calculation reproduced:** 100×11/34=32.352941176%→32.4%; printed32.3 differs0.052941176 point,0.002941176 above its upper rounding boundary32.35. Adjacent100×6/13=46.153846%→46.2%.
- **Necessary inputs available:** All count/percent inputs. Exact missing definition: whether a different rounding/truncation convention was intended for this value.
- **Source-grounded alternative interpretation:** Truncation to one decimal produces32.3; the adjacent fraction is nearest-rounded. An intentional convention remains possible, not documented.
- **Direct observation versus inferred explanation:** The values are directly printed; ordinary rounding is a derived check. No clinical difference is inferred.
- **Classification confirmation:** Same REPORT sentence with same REPORT corroboration; primary/all S_W, denominator category, statistical_results. No correction. Ambiguity: display convention.
- **Evidence state:** `recorded_candidate`. Determining fact: direct source confirms11/34 and32.3; nearest rounding reproduces32.4.
- **Exact remaining human question:** Was truncation intended here, or what count/percentage/display convention should reconcile this explicit fraction?

## C007 — Total-cholesterol unadjusted difference and arm counts

- **Location found:** Yes. [Main p.9 Table5, total-cholesterol row, headers and difference heading](../../../jama_flint_2019_oi_190079.pdf#page=9), fresh text/render.
- **Source value/text matched:** Yes. O9 (14.1%), n64; P6 (9.7%), n62; absolute unadjusted difference4.3%,95%CI−8 to17.2. Endpoint is at least one value above both baseline and240mg/dL.
- **Comparator matched:** Yes. Numerators, denominators, outcome and difference belong to the same row and table. The heading specifies unadjusted.
- **Consistency rule applicable:** Unadjusted O-minus-P risk difference from displayed group counts, with nearest one-decimal rounding.
- **Calculation reproduced:** 100×(9/64−6/62)=4.385080645 percentage points→4.4; printed4.3 differs0.085080645point, beyond0.05. Printed14.1−9.7 also equals4.4. CI contains the estimate and is not challenged.
- **Necessary inputs available:** Counts, headers, percentages and unadjusted label. Exact missing inputs/definitions: any different endpoint-specific denominator, unadjusted estimator definition or intentional truncation rule.
- **Source-grounded alternative interpretation:** Truncation could yield4.3, or another unprinted denominator/estimator could be involved. No adjustment or CI method is inferred.
- **Direct observation versus inferred explanation:** Printed counts and difference are direct; the arithmetic discrepancy is derived. A production mechanism is unknown.
- **Classification confirmation:** Same REPORT table, primary/all S_W, denominator category, statistical_results. No correction. Ambiguity: estimator/display convention.
- **Evidence state:** `recorded_candidate`. Determining fact: source values match and the explicit unadjusted count difference lies outside the printed estimate's nearest-rounding interval.
- **Exact remaining human question:** Which total-cholesterol denominators, estimator and display rule produced4.3 under the unadjusted heading?

## C008 — LDL unadjusted difference and arm counts

- **Location found:** Yes. [Main p.9 Table5, LDL row and headers](../../../jama_flint_2019_oi_190079.pdf#page=9), fresh text/render.
- **Source value/text matched:** Yes. O9 (14.1%), n64; P6 (9.7%), n62; difference4.3%,95%CI−8 to17.2. LDL endpoint threshold is160mg/dL and above baseline.
- **Comparator matched:** Yes. This independently named outcome has its own row; cholesterol's identical numerical inputs do not establish that the LDL participants are identical.
- **Consistency rule applicable:** Same unadjusted O-minus-P count-difference rule, applied independently to LDL.
- **Calculation reproduced:** 100×(9/64−6/62)=4.385080645points→4.4;14.1−9.7=4.4. Printed4.3 is0.085080645point away, outside0.05 tolerance. No CI reconstruction is performed.
- **Necessary inputs available:** All displayed arithmetic inputs and outcome identity. Exact missing inputs/definitions: LDL-specific alternative denominator/estimator and display convention.
- **Source-grounded alternative interpretation:** Intentional truncation or an unprinted estimator could explain4.3. Duplicate counts across different outcomes are possible and are not independently treated as an error.
- **Direct observation versus inferred explanation:** Row values are direct; unadjusted fraction subtraction is reproduced; participant overlap is unknown.
- **Classification confirmation:** Internal REPORT discrepancy, primary/all S_W, denominator category, statistical_results. No correction. Ambiguity: estimator/display convention. Permanent ID remains distinct from C007.
- **Evidence state:** `recorded_candidate`. Determining fact: exact LDL row inputs reproduce4.38508 rather than a nearest-rounded4.3.
- **Exact remaining human question:** Which LDL-specific denominator, unadjusted estimator and rounding rule produced4.3?

## C009 — SAS weekly points label and plotted trajectories require an estimand mapping

- **Location found:** Yes. [Main p.7 Extrapyramidal Measures](../../../jama_flint_2019_oi_190079.pdf#page=7), [results supplement p.10 eFigure9](../../../joi190079supp2_prod.pdf#page=10), and model definition on [main p.4](../../../jama_flint_2019_oi_190079.pdf#page=4) continuing on [p.5](../../../jama_flint_2019_oi_190079.pdf#page=5). The Poisson definition begins on physical p.4, a locator clarification to the ledger's p.5-only support reference.
- **Source value/text matched:** Yes. Weekly change contrast0.022points,95%CI0.009–0.036, adjustedP=.009; figure Week0–36 and SAS Total Score. Fresh render gives approximate O.56→.73 and P.685→.40. No exact coordinates are printed.
- **Comparator matched:** Outcome, randomized groups and time range match; the main narrative identifies eFigure9 as this variable's trajectory. An identical additive coefficient/response-scale estimand is not established. Poisson mixed effects with overdispersion is printed; link/back-transformation is not.
- **Consistency rule applicable:** Only conditionally: an additive constant score-scale slope contrast reproduces difference-of-changes/time if that coefficient and those means represent the same additive estimand. The package does not establish this essential alignment.
- **Calculation reproduced:** From approximate endpoints,[(.73−.56)−(.40−.685)]/36=.012638889points/week;±.02 per endpoint gives about.010417–.014861. .022×36=.792 differs from graphical.455. Alternative log-scale diagnostic,[ln(.73/.56)−ln(.40/.685)]/36=.022307279/week. Neither diagnostic establishes the actual link or fitted coefficient.
- **Necessary inputs available:** Printed coefficient/label, axes and approximate graphical means. Exact missing inputs/definitions: response link, coefficient scale, any back-transformation, exact plotted means, covariate/reference population, marginal versus conditional estimand, and whether weekly change is constant additive.
- **Source-grounded alternative interpretation:** A link-scale or other nonlinear/conditional coefficient can yield the same trajectories while differing from endpoint-average additive slope. The log diagnostic illustrates this possibility but is not supplied-source proof of a log link. Figure reading precision is another limitation.
- **Direct observation versus inferred explanation:** Labels/axis titles are direct; endpoint readings and calculations are approximate/derived. The additive comparison's assumption is unestablished. Significance and clinical effect are not recalculated.
- **Classification confirmation:** The registered comparison remains main REPORT versus a different results REPORT, primary/all S_C; measure category, report_internal_inconsistency. The model paragraph supports interpretation and adds no separate S_W discrepancy. No classification correction. Ambiguity: unmatched scale/estimand mapping.
- **Evidence state:** `record_input_error`. Determining fact: the registered numerical mismatch requires an unsupported alignment of response-scale endpoint-average slope with the reported coefficient. Direct inspection confirms the inputs but cannot establish that alignment or settle whether the points label has a residual discrepancy. This is not a claim that the printed label is correct and is not `not_reproduced`.
- **Exact remaining human question:** What link, response/coefficient scale, reference population and estimand generated0.022 and the eFigure9 means, and does “points” correctly express that coefficient after any transformation?

## C010 — Acute recruitment82 versus98 per site

- **Location found:** Yes. [Plan p.21, lines995–997](../../../joi190079supp1_prod.pdf#page=21), [p.17 Table4](../../../joi190079supp1_prod.pdf#page=17), [p.7 overview/Figure1](../../../joi190079supp1_prod.pdf#page=7), fresh direct text.
- **Source value/text matched:** Yes. Four sites each recruit82 patients in Human Subjects; Table4 each recruits98 acutely ill participants and randomizes44; overall392 acute and176 randomized.
- **Comparator matched:** Same proposed study, all four sites, acute recruitment. Actual article recruitment and later revised randomized target are not comparator values.
- **Consistency rule applicable:** Equally contributing acute site targets should multiply to the same overall target, unless a population/version difference is supplied.
- **Calculation reproduced:** 4×82=328;4×98=392; difference64 total and16 per site.44×4=176 separately reconciles.
- **Necessary inputs available:** Site counts, target numbers and phase labels. Exact missing inputs/definitions: a documented revision/version or subgroup distinguishing82 from98.
- **Source-grounded alternative interpretation:** Earlier targets may remain embedded in the bound bundle, or82 could describe a different recruitment subgroup. Compared paragraphs do not supply either boundary.
- **Direct observation versus inferred explanation:** Printed targets differ; arithmetic is exact; no realized enrollment discrepancy is inferred.
- **Classification confirmation:** Prospective PLAN versus PLAN within one bundle, primary/all P_P; numeric category, plan_material. No correction. Ambiguity: embedded version/population difference.
- **Evidence state:** `recorded_candidate`. Determining fact: exact prospective targets reproduce328 versus392 under the same printed four-site recruitment framing.
- **Exact remaining human question:** Do82 and98 refer to the same acute recruitment target, and what amendment/version or population definition reconciles them?

## C011 — MMSE24 heading labels a different entry phase

- **Location found:** Yes. [Plan p.9, line438 and lines439–444](../../../joi190079supp1_prod.pdf#page=9), continued on [p.10 line445](../../../joi190079supp1_prod.pdf#page=10); [p.7 overview](../../../joi190079supp1_prod.pdf#page=7) and [p.11 footnoteH](../../../joi190079supp1_prod.pdf#page=11).
- **Source value/text matched:** Yes. Heading says MMSE Score≥24 to Enter the Stabilization Phase; operational paragraph applies MMSE<24 at end of stabilization to RCT exclusion, with exceptions. Overview assigns≥24 to RCT entry; footnoteH schedules MMSE at end stabilization.
- **Comparator matched:** Same numeric cognitive threshold and prospective entry-phase framing. Whether two gates were intended is not explicitly stated.
- **Consistency rule applicable:** A threshold heading should identify the phase governed by the accompanying operational definition. Stabilization entry and RCT entry are distinct labels, ordinarily8weeks apart.
- **Logical comparison reproduced:** The heading names entry into stabilization, while paragraph/overview and scheduled assessment name its end and entry into RCT. Numeric threshold24 itself agrees.
- **Necessary inputs available:** Threshold, heading, operational passage and ordinary phase duration. Exact missing definition: whether the heading is shorthand or an additional separate stabilization-entry gate exists.
- **Source-grounded alternative interpretation:** There might be two cognitive gates, or the heading may be imprecise. The package does not show an asserted score/count effect; exceptions are explicitly described.
- **Direct observation versus inferred explanation:** Entry-phase labels differ directly. No eligibility number, MMSE measurement or participant classification is inferred to differ.
- **Classification confirmation:** PLAN heading versus PLAN operational wording, primary/all P_P, measure category, plan_material. Main report corroborates RCT-entry timing only and does not add P_R. No correction. Ambiguity: two gates versus heading shorthand.
- **Evidence state:** `recorded_candidate`. Determining fact: source confirms the registered concrete phase label mismatch for the numeric cutoff, without establishing a count consequence.
- **Exact remaining human question:** Is24 required at stabilization entry, RCT entry or both, and which phase should the heading identify?

## C012 — Historical35% has different denominator wording

- **Location found:** Yes. [Plan p.4 lines175–177](../../../joi190079supp1_prod.pdf#page=4) and [p.15 lines728–732](../../../joi190079supp1_prod.pdf#page=15), fresh direct text.
- **Source value/text matched:** Yes. Historical account: approximately35% of relapses occurred following discontinuation in persons continuing antidepressant. Power section:15% of maintained participants relapse,35% placebo-group relapse, and calls35% following olanzapine discontinuation the same rate reported by Aronson.
- **Comparator matched:** The same citation is explicitly invoked for the35% assumption; participant-risk framing and fraction-of-relapses wording differ. The package does not contain the underlying historical study's denominator data.
- **Consistency rule applicable:** A fraction of all relapses and a risk among discontinuing participants are different measures unless the source supplies a denominator mapping or separately identified estimates.
- **Logical comparison reproduced:** Let D be relapses following discontinuation,R all relapses,E exposed discontinuers. Printed first passage impliesD/R≈.35; participant-risk framing impliesD/E≈.35. Equality is not established by sharing35%.35−15=20points remains arithmetically coherent.
- **Necessary inputs available:** Exact phrasing, percentage and common citation. Exact missing inputs/definitions: historical R,D,E counts, actual denominator and whether both35% measures were reported.
- **Source-grounded alternative interpretation:** First passage may compress the denominator or historical data may contain two identical percentages. No external source is consulted or historical risk reconstructed.
- **Direct observation versus inferred explanation:** Denominator framing differs directly; symbolic quantities explain the measure identity issue rather than assert unknown historical counts.
- **Classification confirmation:** Both historical/background and prospective framing are PLAN by content; primary/all P_P, denominator category, plan_material. No correction. Ambiguity: actual historical measure/denominator.
- **Evidence state:** `recorded_candidate`. Determining fact: exact passages reproduce the same35% citation with different printed denominator framing; missing historical inputs leave the named question.
- **Exact remaining human question:** What denominator does the supplied historical35% describe, and is that the same participant-risk quantity used in the power rationale?

## C013 — Historical Week6 completion totals differ across partitions

- **Location found:** Yes. [Plan p.29 Table5](../../../joi190079supp1_prod.pdf#page=29), fresh text and render.
- **Source value/text matched:** Yes. Week6:Asian n12/75.0%,Black n29/75.9%,White n218/74.8%; Hispanic n30/80.0%,not Hispanic n229/73.8%. Headings are randomized participants and percent completers Week6/Week12.
- **Comparator matched:** Race12+29+218=259 and ethnicity30+229=259; common historical study/endpoint. The table suggests complete partitions but raw person-level alignment is absent.
- **Consistency rule applicable:** If each row uses printed randomized n and the same Week6 completion definition, nearest-one-decimal percentages must correspond to integer numerators and exhaustive partitions must give the same total.
- **Calculation reproduced:** Rounding bins uniquely permit9/12→75.0%,22/29→75.9%,163/218→74.8%;24/30→80.0%,169/229→73.8%. Totals194 versus193. Each bin width in persons is.001n≤.229, preventing a second integer. Week12 permits6+15+121=142 and16+126=142, a coherent control.
- **Necessary inputs available:** All denominator and percentage cells. Exact missing inputs/definitions: raw completer counts/flags, confirmation of identical classification sets, any missingness or row-specific denominator convention.
- **Source-grounded alternative interpretation:** Different missing-status treatment/denominators or completion definitions could break partition identity; none is printed. A row percentage/count could differ in the underlying record, without identifying which.
- **Direct observation versus inferred explanation:** n/percent cells are direct; unique integer numerators and totals are derived. Historical completion records are not current trial results.
- **Classification confirmation:** Historical/background table remains PLAN; primary/all P_P, denominator category, plan_material. No correction. Ambiguity: matched person-level denominator/flags.
- **Evidence state:** `recorded_candidate`. Determining fact: exact source cells uniquely imply194 versus193 under the table's common denominator/endpoint framing and conventional rounding; definitions needed for an alternative remain named.
- **Exact remaining human question:** Do all five rows partition the same259 participants with the printed denominators and Week6 completion rule, and what raw numerators reconcile194 versus193?

## C014 — Exposure maximum20 and authorized extended pathway

- **Location found:** Yes. [Plan p.41 lines2067–2070](../../../joi190079supp1_prod.pdf#page=41), [p.10 Table1](../../../joi190079supp1_prod.pdf#page=10), [p.11 footnotesA/D](../../../joi190079supp1_prod.pdf#page=11), [p.7 lines326–332](../../../joi190079supp1_prod.pdf#page=7), [p.40 lines2043–2054](../../../joi190079supp1_prod.pdf#page=40); [pp.13](../../../joi190079supp1_prod.pdf#page=13) and [14](../../../joi190079supp1_prod.pdf#page=14) provide repeated duration wording.
- **Source value/text matched:** Yes. Minimum10/max20weeks sertraline beforeRCT; acute4–12weeks after starting study medications;8week stabilization continuing open-label sertraline/olanzapine. Steering Committee may authorize two additional weekly stabilization visits for qualifying near-remitters, requiring two consecutive weeks meeting final criteria.
- **Comparator matched:** Prospective pre-RCT treatment clock and sequential study phases. The maximum-extension calculation applies only to a participant completing12acute weeks and the authorized extension on continued treatment; no such actual participant is documented.
- **Consistency rule applicable:** An unqualified exception-inclusive maximum should accommodate every authorized sequential treatment pathway. Whether the printed maximum is intended to exclude the exception is missing.
- **Calculation reproduced:** Ordinary course4–12+8=12–20weeks. Authorized extended maximum12+8+2=22weeks,2weeks beyond20. Minimum10 is satisfied by12 if it is a loose lower bound; the lower endpoint alone does not establish an operational contradiction.
- **Necessary inputs available:** Durations, explicit two-visit extension, continuing-treatment wording and stated exposure range. Exact missing inputs/definitions: exception-inclusive versus ordinary-course scope of the range, whether extension can follow12acute weeks, and any interruption/different sertraline clock.
- **Source-grounded alternative interpretation:** Appendix range may summarize only the ordinary course.10 may be a conservative lower bound. Neither interpretation is explicitly marked in the range sentence.
- **Direct observation versus inferred explanation:** Durations and extension permission are direct.22weeks is conditional pathway arithmetic, not observed exposure or a protocol violation. The10versus12 component is expressly weaker.
- **Classification confirmation:** All content is prospective PLAN within the bundle; primary/all P_P, numeric category, plan_material. No correction. Ambiguity: ordinary versus exception-inclusive range and exposure clock.
- **Evidence state:** `recorded_candidate`. Determining fact: direct source confirms authorized two-week extension in addition to4–12+8 ordinary phases and an unqualified printed max20; conditional22week pathway remains registered pending its named scope definition.
- **Exact remaining human question:** Does max20 intentionally exclude the authorized extension, and can a12week acute participant continue sertraline through the additional two weeks? Is minimum10 merely a lower bound or an attainable shortest course?

## C015 — HDRS endpoint description lacks five-point-rise qualifier

- **Location found:** Yes. [Main p.4 primary outcome](../../../jama_flint_2019_oi_190079.pdf#page=4), [plan p.12 lines554–557](../../../joi190079supp1_prod.pdf#page=12); [plan p.7 near-remission definition](../../../joi190079supp1_prod.pdf#page=7). [Main p.6](../../../jama_flint_2019_oi_190079.pdf#page=6) reports13/64 and34/62 for the endpoint but is not a discrepant count comparator.
- **Source value/text matched:** Yes. Main criterion includes17-itemHDRS≥18 among at least one of listed criteria. Plan's corresponding HAM-D criterion requires≥18 and mean absolute increase5points on at least one visit relative to RCT entry, with a preferred two-visit duration. Near-remission permits11–15.
- **Comparator matched:** Same numerical depression relapse criterion within the shared primary endpoint; the report is a summary and the plan gives operational detail. Applied rules/person-level consequences are not established by the aggregate results.
- **Consistency rule applicable:** Threshold≥18 alone and threshold≥18 plus rise≥5 are numerically distinct endpoint definitions when baseline14–15 is allowed.
- **Logical comparison reproduced:** Illustrative15→18 has rise3: it meets18alone but not rise5.14→18 has rise4. For baseline≤13, reaching18 implies rise≥5. These are examples, not observed cases. Other relapse branches could independently establish the endpoint.
- **Necessary inputs available:** Both printed threshold statements and allowed near-remission values. Exact missing inputs/definitions: rule actually applied, how “mean absolute increase” was operationalized, any disclosed operative amendment, and patient scores/other relapse criteria needed to test count impact.
- **Source-grounded alternative interpretation:** Main prose may compress a fully applied plan rule; an operative amendment or different implementation is possible. No aggregate count contradiction or violation is inferred.
- **Direct observation versus inferred explanation:** Numerical qualifier differs directly in the definitions. Hypothetical classification examples demonstrate scope; actual13/34 events are not reassigned.
- **Classification confirmation:** Main results/methods REPORT versus prospective PLAN definition; primary/all P_R, measure category, protocol_report. No correction. Ambiguity: summary omission versus operative rule.
- **Evidence state:** `recorded_candidate`. Determining fact: exact sources reproduce the omitted five-point qualifier for the numerical endpoint definition; applied-rule/count consequences remain explicitly unresolved.
- **Exact remaining human question:** Was the five-point qualifier applied to the reported endpoint, and did any participant meet≥18 without that rise and without another relapse criterion? What operative rule/amendment resolves the wording difference?

## DOC-004 administrative role recommendation

[Data Sharing Statement p.1](../../../joi190079supp3_prod.pdf#page=1) was directly extracted. It states data availability with publication, approved researchers/purpose, investigator support, proposal approval and signed access agreement. These are prospective access/operational conditions rather than numeric research findings. Under the normative prospective-operational-document rule, **PLAN is the better content-based package role**. Administrative sharing documents are not explicitly named among normative examples, so retain this bounded role ambiguity in source_inventory.md. An alternative REPORT treatment would classify the publication's administrative end matter, but its title/supplement number alone cannot decide. It enters no stable candidate and changes no discrepancy relationship or quantitative count. This recommendation is not an additional candidate.

## Completion and limitations

C001–C015 all have separately recorded location, source value, comparator, rule, reproduced comparison, available/missing inputs, alternative interpretation, direct/inferred distinction, classification, determining evidence-state fact and exact remaining human question. No IDs were deleted, merged, renumbered or suppressed. No evidence mismatch was silently repaired. C009's p.4 model starting location is clarified; its numeric transcription is unchanged. The other registered locations/values are confirmed.

Limitations are candidate-specific definitions/underlying inputs, not source inspection gaps: category missingness(C002); intended footnote/coding(C003/C004); HbA1c response units(C005); rounding/estimator conventions(C006–C008); link/estimand/exact plot values(C009); plan versions/phase labels(C010/C011); historical denominators/completion flags(C012/C013); exposure-clock/extension scope(C014); implemented endpoint and participant criteria(C015). All registered comparisons received exact-source inspection. Every candidate remains Pending Human Adjudication.
