# Statistical Consistency Review — Pass 1

- **Runtime agent ID:** `/root/statistics_pass_1`
- **Model / reasoning effort:** `gpt-5.6-terra` / `high`
- **Scope:** all 30 stable relationships in `statistics/relationship_inventory.md` (`S001` through `S030`).
- **Completion:** every assigned relationship is recorded as `PASS_1_COMPLETE` in the inventory.
- **Covered S IDs:** S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030.

## Checks performed

For every applicable relationship, this pass checked point-estimate containment, interval ordering, sign/direction, effect measure and scale labels, and matched repetitions. Interval/P-value/test/statistic/SE compatibility was checked only when the direct source supplied compatible inferential definitions. The main and result supplement use Bayesian posterior probabilities and 95% credible intervals; they do not give conventional P values, test statistics, SEs, degrees of freedom, or a sufficient variance rule for those results. The post-hoc GEE table is explicitly frequentist and was not treated as a posterior analysis.

No P value was printed as `P = 0`, `p = 0.000`, or equivalent. Zero outcome estimates and zero-width credible intervals were assessed only as reported outcome estimates; no display-zero candidate was emitted.

## Pass-1 candidate records

### P1-01 — Matched primary CNRT-switch credible intervals differ by location

- **Primary category:** Statistical reporting inconsistency
- **Sources:** [main abstract p. 1](<../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1>) prints RD 6%, 95% CrI 6%-11%; [main Results p. 5](<../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=5>) prints 6% (2%-11%); [Supplement 2 eTable 4 p. 21](<../../../joi240036supp2_prod_1716416466.01349.pdf#page=21>) prints 6% (2%-10%).
- **Rule:** matched population, time point, switch-versus-continuation contrast, effect measure, and interval level should reproduce the same printed interval absent a stated distinction.
- **Observation:** the lower and upper endpoints vary across the three locations.
- **Missing definition / human question:** does a location-specific model, posterior summary, or revision explain the different endpoints?

### P1-02 — Primary varenicline-switch sign and direction are inconsistent

- **Primary category:** Statistical reporting inconsistency
- **Sources:** [main abstract p. 1](<../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1>) and [Results p. 5](<../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=5>) print switch-to-CNRT versus continuation RD -3% (-4% to -1%) while stating continuation was worse than switching; [Supplement 2 eTable 4 p. 21](<../../../joi240036supp2_prod_1716416466.01349.pdf#page=21>) labels the same switch-versus-stay contrast as +3% (1%-4%).
- **Rule:** with a switch-minus-continuation label, 0% versus 3% gives a negative direction; the narrative and matching table must identify a compatible direction/reference.
- **Observation:** the main negative RD, benefit wording, and eTable positive ARD cannot all describe the same labelled contrast.
- **Missing definition / human question:** which reference orientation and narrative direction are intended for this contrast?

### P1-03 — Primary increased-varenicline CrI upper endpoint differs

- **Primary category:** Statistical reporting inconsistency
- **Sources:** [main abstract p. 1](<../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1>) and [Results p. 5](<../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=5>) print RD 18% (13%-24%); [Supplement 2 eTable 4 p. 21](<../../../joi240036supp2_prod_1716416466.01349.pdf#page=21>) prints 18% (13%-23%).
- **Rule:** matched contrast repetition should agree in its reported 95% CrI.
- **Observation:** the upper endpoint differs by one percentage point.
- **Missing definition / human question:** was a different posterior summary or a transcription revision used?

### P1-04 — Primary abstainer-comparison CrI lower endpoint differs

- **Primary category:** Statistical reporting inconsistency
- **Sources:** [main Results p. 7](<../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=7>) prints RD 6% (-5% to 16%); [Supplement 2 eTable 4 p. 21](<../../../joi240036supp2_prod_1716416466.01349.pdf#page=21>) prints 6% (-4% to 16%).
- **Rule:** matched CNRT-versus-varenicline phase-1-abstainer comparison should retain the same interval endpoints.
- **Observation:** the lower endpoint differs.
- **Missing definition / human question:** does a separately defined analysis explain the one-point difference?

### P1-05 — EOT+30 CNRT-switch cell estimate and CrI are non-containing/reversed in detailed narrative

- **Primary category:** Statistical reporting inconsistency
- **Sources:** [detailed narrative, Supplement 2 p. 10](<../../../joi240036supp2_prod_1716416466.01349.pdf#page=10>) prints 1.0% (7.0%-1.3%); matching [eFigure 2 p. 15](<../../../joi240036supp2_prod_1716416466.01349.pdf#page=15>) prints 10% (7%-13%).
- **Rule:** a probability estimate should lie within an increasing credible interval; matched cell repetitions should agree.
- **Observation:** 1.0 is not contained in 7.0-1.3 and the endpoints are decreasing; the matched eFigure reports a different, coherent cell.
- **Missing definition / human question:** is the detailed narrative missing digits or otherwise transcribed incorrectly?

### P1-06 — EOT+30 increased-CNRT cell CrI is non-containing/reversed in detailed narrative

- **Primary category:** Statistical reporting inconsistency
- **Sources:** [detailed narrative p. 10](<../../../joi240036supp2_prod_1716416466.01349.pdf#page=10>) prints 8.0% (5.0%-1.1%); [eFigure 2 p. 15](<../../../joi240036supp2_prod_1716416466.01349.pdf#page=15>) prints 8% (5%-11%).
- **Rule:** point containment, endpoint order, and matched cell repetition.
- **Observation:** 8.0 is not contained in 5.0-1.1; the figure gives an ordered, containing interval with a different upper endpoint.
- **Missing definition / human question:** is `1.1%` a source typographic error for the figure’s `11%`?

### P1-07 — EOT+30 CNRT-switch ARD CrI is non-containing/reversed in detailed narrative

- **Primary category:** Statistical reporting inconsistency
- **Sources:** [detailed narrative p. 10](<../../../joi240036supp2_prod_1716416466.01349.pdf#page=10>) prints ARD 6.0% (3.0%-1.0%); [eTable 9 p. 33](<../../../joi240036supp2_prod_1716416466.01349.pdf#page=33>) prints 6% (3%-10%).
- **Rule:** RD must lie within increasing CrI and matched contrast reports should agree.
- **Observation:** 6.0 is not contained in 3.0-1.0; the eTable gives 3%-10%.
- **Missing definition / human question:** is the narrative upper endpoint missing a digit?

### P1-08 — EOT+30 increased-varenicline cell/RD CrI repeatedly non-containing in detailed narrative

- **Primary category:** Statistical reporting inconsistency
- **Sources:** [Supplement 2 pp. 10-11](<../../../joi240036supp2_prod_1716416466.01349.pdf#page=10>) repeatedly print 8.0% (5.0%-1.1%) for the cell and ARD; [eFigure 2 p. 15](<../../../joi240036supp2_prod_1716416466.01349.pdf#page=15>) and [eTable 9 p. 33](<../../../joi240036supp2_prod_1716416466.01349.pdf#page=33>) print 8% (5%-11%).
- **Rule:** containment/order and exact matched repetition.
- **Observation:** the detailed interval excludes 8.0 and reverses endpoints at each occurrence.
- **Missing definition / human question:** are all repeated `1.1%` strings intended to be `11%`?

### P1-09 — EOT+30 phase-1-abstainer ARD magnitude differs in detailed narrative

- **Primary category:** Statistical reporting inconsistency
- **Sources:** [detailed narrative p. 11](<../../../joi240036supp2_prod_1716416466.01349.pdf#page=11>) prints ARD 1.1% (-1.0%-22%); [eTable 11 p. 35](<../../../joi240036supp2_prod_1716416466.01349.pdf#page=35>) prints 11% (-1%-22%).
- **Rule:** exact matched contrast repetition and compatibility with 67% versus 56% displayed cells.
- **Observation:** the narrative point estimate differs by a factor of ten from the eTable and cell difference.
- **Missing definition / human question:** is the narrative decimal placement unintended?

### P1-10 — Six-month phase-1-abstainer narrative ARD/CrI conflicts with eTable and its own containment

- **Primary category:** Statistical reporting inconsistency
- **Sources:** [detailed narrative p. 12](<../../../joi240036supp2_prod_1716416466.01349.pdf#page=12>) prints ARD 1.0% (-1.3%-1.1%) and calls it a varenicline benefit; [eTable 11 p. 35](<../../../joi240036supp2_prod_1716416466.01349.pdf#page=35>) prints 1% (-11%-12%).
- **Rule:** the estimate must be contained in an ordered interval; matched repetition and direction/reference must agree.
- **Observation:** positive 1.0 is outside -1.3 to -1.1; the printed narrative interval differs in scale and direction from eTable 11.
- **Missing definition / human question:** what interval and reference orientation were intended in the narrative?

### P1-11 — Protocol Figure 2 varenicline-response beta parameters do not reproduce paired printed probability

- **Primary category:** Statistical reporting inconsistency
- **Sources:** [Protocol Figure 2 p. 32](<../../../joi240036supp1_prod_1716416466.00349.pdf#page=32>) pairs `0.50, 0.40-0.60` with `Beta(a=785,b=869)`.
- **Rule:** where the figure says its probability parameters correspond to the printed beta distribution, the beta mean is `a/(a+b)`.
- **Diagnostic calculation:** `785/(785+869) = 0.4746`, not 0.50. This is a labelled diagnostic calculation, not a reconstructed P value.
- **Observation:** the paired mean label and supplied beta parameters do not reproduce one another.
- **Missing definition / human question:** does the beta distribution encode a distinct quantity or is one printed Figure 2 input incorrect?

### P1-12 — Protocol Table 3 labels the third Aim-2 planned effect inconsistently with its value and defined contrast

- **Primary category:** Measure, label, or scale inconsistency
- **Sources:** [Protocol Table 3 p. 34](<../../../joi240036supp1_prod_1716416466.00349.pdf#page=34>) labels both the first and third Aim-2 rows `VAR vs. NPL`; the third has estimate 0.195 (0.119-0.269). [Protocol Table 2 p. 33](<../../../joi240036supp1_prod_1716416466.00349.pdf#page=33>) gives 0.399 for NPL-to-VAR and 0.204 for NPL-to-NPL+, whose difference is 0.195; [Protocol p. 29](<../../../joi240036supp1_prod_1716416466.00349.pdf#page=29>) defines the third Aim-2 contrast as VAR versus NPL+.
- **Rule:** a planned-effect label must identify the contrast represented by its displayed value and defined formula.
- **Observation:** the third label duplicates the first comparator, whereas its value/formula correspond to VAR versus NPL+.
- **Missing definition / human question:** is the Table 3 third-row comparator label intended to be `VAR vs. NPL+`?

## Limitations

- The source supplies no conventional P values, test statistics, standard errors, degrees of freedom, test sidedness, covariance, or variance-estimator details for the Bayesian result relationships; those compatibility calculations were not inferred.
- The protocol is a planned-analysis source and does not supply a version crosswalk proving identity with every published analysis specification.
- All listed items are candidate consistency issues pending human adjudication. No severity, validity, acceptance, rejection, correction, or final disposition is assigned here.
