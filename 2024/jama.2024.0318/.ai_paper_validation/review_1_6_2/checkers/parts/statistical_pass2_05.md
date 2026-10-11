# Statistical pass 2 — part 05

Runtime agent: root/statistical_pass2_extra_c. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN. Exact disjoint scope: S173, S174, S175, S176, S177, S178, S179, S180, S181, S182, S183, S184, S185, S186, S187, S188, S189, S190, S191, S192, S193, S194, S195, S196, S197. Every assigned relationship was revisited after reading the complete current ledger, initial screening log, mechanical recheck and all 53 original checker exclusions in statistics/pass2_shared_context.md. Scope and review contract were read completely. New findings: 0. New excluded observations: 0. All candidates retain Pending Human Adjudication.

## Direct-source and rule checks

All owned results are eTable 5 adverse events through 12 years in REPORT DOC-003, with MED N=96 and SURG N=166. Exact source [p19](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19) and [p20](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=20) were visually reread on unchanged current CPU Poppler 26.01.0 images preprocessing/stat_extra_source19.png and preprocessing/stat_extra_source20.png. Page 20 footnote a specifies n (%) and footnote b names chi-squared or Fisher's exact tests. REPORT [p6](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=6) repeats this family; REPORT [p5](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=5) says secondary results are hypothesis generating without multiple-testing adjustment. Their existing CPU renderings were reread; no new derivative was made.

Every event count is within its group denominator, every reconstructed nonevent count is nonnegative, and every percentage overlaps its own one-decimal half-unit band after exact 100n/N arithmetic. The two columns represent participant counts, so adding categories is not a unique-participant total: no claim of mutually exclusive adverse-event categories is supplied. The full original counts, percentages, diagnostics, printed-P bands and PASS_1_COMPLETE facts are preserved in statistics/parts/pass2_05_inventory.md alongside each PASS_2_COMPLETE addition.

The table below lists every owned relationship and its check facts. P diagnostics reuse source-confirmed deterministic JavaScript numerical proofs from pass 1. Pearson denotes the non-continuity-corrected chi-square(1) reconstruction from the 2-by-2 table. Fisher denotes the probability-ordering hypergeometric diagnostic, not an inferred assertion about authors' sidedness, ordering, software option or row-specific selection. A method permitted by the stated family matches each printed P under the workflow's display-precision rule. No cell has a confidence interval, coefficient, OR, standard error or printed test statistic; interval containment, endpoint order, interval-P agreement and coefficient sign are therefore not applicable. No source claim of superiority, noninferiority, equivalence, interim stopping or sample-size reproduction is attached to these rows.

## Relationship-by-relationship pass 2 checks

| S ID | REPORT source page and adverse event | MED / SURG event counts | Printed P | Compatible family diagnostic | Precision and inferential check |
|---|---|---|---|---|---|
| S173 | p19 Concussion/contusion/head injury | 2/96 / 13/166 | .058 | Fisher .058118926 | Percentages 2.1/7.8 reconcile; P gap 0; higher SURG frequency; PASS_2_COMPLETE. |
| S174 | p19 Neuropathy | 7/96 / 11/166 | .84 | Pearson .837505113 | Percentages 7.3/6.6 reconcile; P gap 0; lower SURG frequency; PASS_2_COMPLETE. |
| S175 | p19 Memory loss/cognitive dysfunction | 3/96 / 6/166 | .83 | Pearson .833986425 | Percentages 3.1/3.6 reconcile; P gap 0; higher SURG frequency; PASS_2_COMPLETE. |
| S176 | p19 Cataracts | 12/96 / 20/166 | .91 | Pearson .914304578 | Percentages 12.5/12.0 reconcile; P gap 0; lower SURG frequency; PASS_2_COMPLETE. |
| S177 | p19 Blurred or double vision | 7/96 / 11/166 | .84 | Pearson .837505113 | Percentages 7.3/6.6 reconcile; P gap 0; lower SURG frequency; PASS_2_COMPLETE. |
| S178 | p19 Glaucoma | 5/96 / 4/166 | .23 | Pearson .230748010 | Percentages 5.2/2.4 reconcile; P gap 0; lower SURG frequency; PASS_2_COMPLETE. |
| S179 | p19 Upper respiratory infection | 18/96 / 43/166 | .19 | Pearson .186805764 | Percentages 18.8/25.9 reconcile; P gap 0; higher SURG frequency; PASS_2_COMPLETE. |
| S180 | p19 Pneumonia | 3/96 / 11/166 | .23 | Pearson .224655379 | Percentages 3.1/6.6 reconcile; P-band gap .000344621/.23=.001498352 <=.05; original exclusion retained; PASS_2_COMPLETE. |
| S181 | p19 Cellulitis | 5/96 / 6/166 | .53 | Pearson .535380032 | Percentages 5.2/3.6 reconcile; P-band gap .000380032/.53=.000717041 <=.05; original exclusion retained; PASS_2_COMPLETE. |
| S182 | p20 Systemic infection/sepsis | 0/96 / 2/166 | .53 | Fisher .533912433 | Percentages 0.0/1.2 reconcile; P gap 0; higher SURG frequency; PASS_2_COMPLETE. |
| S183 | p20 Osteomyelitis | 1/96 / 1/166 | 1.00 | Fisher 1.000000000 | Percentages 1.0/.6 reconcile; P gap 0; lower SURG frequency despite equal counts; PASS_2_COMPLETE. |
| S184 | p20 COVID-19 | 1/96 / 1/166 | 1.00 | Fisher 1.000000000 | Percentages 1.0/.6 reconcile; P gap 0; lower SURG frequency despite equal counts; PASS_2_COMPLETE. |
| S185 | p20 Severe hyperglycemia | 8/96 / 14/166 | .98 | Pearson .977475853 | Percentages 8.3/8.4 reconcile; P gap 0; higher SURG frequency; PASS_2_COMPLETE. |
| S186 | p20 Hyperparathyroidism | 0/96 / 2/166 | .53 | Fisher .533912433 | Percentages 0.0/1.2 reconcile; P gap 0; higher SURG frequency; PASS_2_COMPLETE. |
| S187 | p20 Dehydration | 2/96 / 14/166 | .058 | Fisher .057707361 | Percentages 2.1/8.4 reconcile; P gap 0; permitted Fisher matches, although Pearson diagnostic .038611502 differs at .05; no CI or Pearson-only claim; PASS_2_COMPLETE. |
| S188 | p20 Hypokalemia | 2/96 / 8/166 | .33 | Fisher .333797872 | Percentages 2.1/4.8 reconcile; P gap 0; higher SURG frequency; PASS_2_COMPLETE. |
| S189 | p20 Hyperkalemia | 1/96 / 0/166 | .37 | Fisher .366412214 | Percentages 1.0/0.0 reconcile; P gap 0; lower SURG frequency; PASS_2_COMPLETE. |
| S190 | p20 Hypercalcemia | 0/96 / 1/166 | 1.00 | Fisher 1.000000000 | Percentages 0.0/.6 reconcile; P gap 0; higher SURG frequency; PASS_2_COMPLETE. |
| S191 | p20 Back pain | 18/96 / 36/166 | .57 | Pearson .571250294 | Percentages 18.8/21.7 reconcile; P gap 0; higher SURG frequency; PASS_2_COMPLETE. |
| S192 | p20 Osteoarthritis | 8/96 / 6/166 | .10 | Pearson .101756273 | Percentages 8.3/3.6 reconcile; P gap 0; lower SURG frequency; PASS_2_COMPLETE. |
| S193 | p20 Renal insufficiency | 2/96 / 4/166 | 1.00 | Fisher 1.000000000 | Percentages 2.1/2.4 reconcile; P gap 0; higher SURG frequency; PASS_2_COMPLETE. |
| S194 | p20 Acute renal failure | 1/96 / 2/166 | 1.00 | Fisher 1.000000000 | Percentages 1.0/1.2 reconcile; P gap 0; higher SURG frequency; PASS_2_COMPLETE. |
| S195 | p20 Allergy/intolerance to medication or supplement | 5/96 / 9/166 | .94 | Pearson .941021321 | Percentages 5.2/5.4 reconcile; P gap 0; higher SURG frequency; PASS_2_COMPLETE. |
| S196 | p20 Alcohol abuse | 2/96 / 7/166 | .49 | Fisher .493005380 | Percentages 2.1/4.2 reconcile; P gap 0; higher SURG frequency; PASS_2_COMPLETE. |
| S197 | p20 Abdominal wall hernia | 1/96 / 6/166 | .43 | Fisher .428302162 | Percentages 1.0/3.6 reconcile; P gap 0; higher SURG frequency; PASS_2_COMPLETE. |

## Ledger, source and exclusion implications

The complete screened ledger and exact-source recheck were used to distinguish within-report reproduction from the already registered prospective vascular/safety test mapping. PLAN [p34](../../../../joi240004supp1_prod_1721756962.80052.pdf#page=34) specifies CMH for vascular events and the same manner for safety. Its current CPU rendering confirms that event strata are not named. Broad chi-squared terminology, Fisher substitution for sparse rows and composite-versus-individual-result mapping remain source-grounded alternatives. Compatibility of the observed row tests does not supply the missing strata or the prospective mapping. That already screened issue is not re-emitted. Other registered primary scale, model, sensitivity, remission, mortality and baseline count issues do not create a new contradiction in the owned adverse-event rows.

The S180/S181 passages of the original consolidated last-digit exclusion were independently compared with the exact printed cells and their full P-value bands. Relative gaps .001498352 and .000717041 are below .05, with no printed interval, estimate/test incompatibility, or contrary significance claim. Route A category 1 is consequently absent; these original exclusions remain ROUNDING_OR_DISPLAY_PRECISION. Route A categories 2–4 are not reproduced after the source and precision checks, and the route A category 5 prospective mapping is already screened. No newly relevant global exclusion is identified from this owned source scope. The primary fresh pass-2 agent owns the final global exclusion findings, including direct rereading of unrelated cited source locations.

S187 specifically prevents an inferred Pearson-only claim: the Pearson diagnostic would cross .05, but a Fisher diagnostic permitted by the printed family reproduces .058. Both original diagnostics remain recorded. No interval or printed claim requires Pearson here, so this is a reconciled family check rather than an excluded apparent issue.

## New findings

None.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|

There are no new apparent issues decided against inclusion. Previously recorded S180/S181 precision exclusions are retained in their original consolidated row and are not duplicated here. Checks that reconcile are documented in the relationship records and table above.

## Limitations and closure

Exact row-specific test selection, Fisher sidedness/probability ordering/software options, CMH strata and stratified event counts remain unreported. No CI, coefficient, standard error or test statistic is supplied for these rows. These named limits prevent asserting a specific author software option or reproducing a planned CMH test; they do not create a scientific source-coverage gap. The 25 count/denominator/percentage/P relationships and all applicable direction, method, source and screened-ledger implications are reviewed. All 25 original PASS_1_COMPLETE records are preserved and all 25 receive PASS_2_COMPLETE in statistics/parts/pass2_05_inventory.md. No source, reusable asset, shared packet, canonical inventory, ledger or screening file was modified.
