# Numeric Consistency Review

## Completed scope

This checker reviewed all 70 relationships in `relationships/numeric_relationship_inventory.md` across DOC-001 PDF pp. 1-10, DOC-002 PDF pp. 1-45, and DOC-003 PDF pp. 1-36. Source-linked current PDFs are the authority. Current layout text and renders were used only to locate and transcribe. The review applied arithmetic; total, subgroup-sum, numerator, denominator, percentage, missingness, population, rounding, interval endpoint/order, measure/label/scale, unit, reference-group, rate/risk/proportion/count, repeated-value, and participant-flow checks when a concrete reported numerical relationship existed.

## Applied rules

- **Integer identities:** exact equality is required (tolerance 0).
- **Raw count percentages:** for a displayed whole percentage, an absolute difference no greater than 0.5 percentage point is compatible with rounding; no alternative denominator is assumed unless printed.
- **Intervals:** lower endpoint must not exceed upper endpoint; a direct matched-source endpoint comparison uses tolerance 0 at the printed precision.
- **Displayed model estimates:** a Bayesian posterior probability, CrI, or ARD is not forced to equal an unadjusted fraction. A conflict is recorded only where the source prints a matched result, a direct arithmetic identity, or a named reference scale that fails.
- **Nested detection thresholds:** for the same simulated result set, a requirement of posterior benefit greater than 0.85 is a subset of a requirement greater than 0.80; the detection probability must therefore be no greater at 0.85. Tolerance 0 for the ordering rule.
- **Rate versus count:** event `N` and IPW estimated rate are separate measures; they were not added or compared as if they were the same quantity.
- **Display zero:** no P-value display-zero candidate was generated. The 0% outcome cells are reported proportions/counts, not P values.

## Candidate consistency issues

### Main Table sex counts exceed both printed denominators

**Exact source locations:** [DOC-001 p. 5](<../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=5>), Baseline Measures and Demographics Table, Sex rows.

**Printed inputs:** Each column is headed `n = 245`. CNRT prints female `105 (42.9)` and male `145 (57.1)`; varenicline prints female `105 (42.9)` and male `145 (57.1)`.

**Rule and calculation:** Sex is presented as a two-category count of participants in each stated `n=245` column. CNRT: 105 + 145 = 250, difference from 245 = +5. Varenicline: 105 + 145 = 250, difference from 245 = +5. Tolerance: 0 participants for a displayed mutually exclusive count total. The printed percentages separately sum to 100.0% in each column, and 105/245=42.9% while 145/245=59.2%, not 57.1%.

**Direct observation versus inference:** Direct observation is the two `n=245` headers and the printed sex cells. The arithmetic failure is a direct derivation. An inferred production explanation is not assigned.

**Alternative source-grounded interpretations:** The male count could be intended as 140, because 140/245=57.1% and 105+140=245; alternatively a column denominator or one count could have been printed incorrectly. The supplied source does not resolve which.

**Quality-control relevance:** A baseline sex count is directly reusable in tabular extraction and denominator summaries.

**Human question:** Which printed element should govern the Table sex distribution in each treatment arm: the denominator, the female count/percentage, or the male count/percentage?

### Main-article flow total does not equal its two printed initial branches

**Exact source locations:** [DOC-001 p. 4](<../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=4>), Results flow narrative; [DOC-001 p. 6](<../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=6>), Figure 2; [DOC-001 p. 1](<../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1>), abstract.

**Printed inputs:** Results/Figure 2 state `491 Randomized`; Figure 2 immediately branches to `245 Randomized to receive CNRT` and `245 Randomized to receive 2-mg varenicline`. The Figure footnote says one CNRT participant was assigned to the wrong phase-2 condition and excluded from all analyses. The abstract and Results analysis population state 490.

**Rule and calculation:** A two-branch initial randomization total equals the sum of its displayed branches: 245 + 245 = 490, not 491. Difference = 1 participant. Tolerance: 0 participants. The stated later analysis exclusion explains 490 analyzed but does not identify a third initial-randomization branch or make the two printed branches sum to 491.

**Direct observation versus inference:** Direct observation is the Figure total, two branch counts, exclusion footnote, and 490 analysis statements. The conclusion that the displayed flow identity does not close is arithmetic. It is not inferred that any person was absent from the trial.

**Alternative source-grounded interpretations:** The 491 total may be a typographical total, one branch may be 246, or the excluded participant may have been counted in a way the diagram does not show. The package does not determine which.

**Quality-control relevance:** Participant totals and randomization denominators are routinely carried into trial-flow and risk-of-bias extraction.

**Human question:** What was the intended initial-randomization denominator and allocation that yields the reported 491 while preserving the stated analytic population of 490?

### Abstract and full Results give different CNRT rescue RD lower CrI endpoints

**Exact source locations:** [DOC-001 p. 1](<../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1>), abstract CNRT nonabstainer paragraph; [DOC-001 p. 5](<../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=5>), Smoking Cessation End of Phase 2.

**Printed inputs:** For the CNRT nonabstainer alternatives versus CNRT continuation, the abstract gives RD 6%, 95% CrI `6% to 11%`. Results gives RD 6%, 95% CrI `2% to 11%`.

**Rule and calculation:** Matched outcome, population (CNRT week-6 nonabstainers), comparator (continuation), estimate (6% RD), and confidence level should have the same printed interval unless a distinct estimator or contrast is named. Lower endpoints differ: 6% versus 2%; difference 4 percentage points. Tolerance: 0 at printed whole-percent precision.

**Direct observation versus inference:** Both interval strings are directly observed. The matching is based on the shared stated population, alternatives, reference, estimate, and interval level.

**Alternative source-grounded interpretations:** The abstract could have intended one particular contrast while Results summarizes both; however both locations say each alternative has an RD of 6%, and neither distinguishes an alternate model or interval calculation.

**Quality-control relevance:** The lower CrI controls whether the reported estimate has a nonzero lower bound and can affect evidence-table extraction.

**Human question:** Which lower CrI endpoint, 2% or 6%, is the intended interval for each CNRT rescue-versus-continuation RD?

### Protocol Figure 2 beta parameters do not reproduce the displayed varenicline response probability or interval

**Exact source location:** [DOC-002 p. 32](<../../joi240036supp1_prod_1716416466.00349.pdf#page=32>), Figure 2, Varenicline 2 mg response at week 6.

**Printed inputs:** The figure prints response `0.50, 0.40-0.60` and `~Beta(a=785,b=869)`.

**Rule and calculation:** For a Beta(a,b) distribution, mean = a/(a+b). 785/(785+869) = 0.4746, which rounds to 0.47 at two decimals, not 0.50. Its approximate standard deviation is sqrt(ab/((a+b)^2(a+b+1))) = 0.0123; a central 95% normal diagnostic interval is approximately 0.451-0.499, not 0.40-0.60. Tolerance: plus or minus 0.005 for the displayed two-decimal mean and zero for a direct stated-parameter identity; the observed mean difference is 0.0254.

**Direct observation versus inference:** The label and beta parameters are direct observations. The beta mean and approximate interval are reproducible diagnostics from the printed parameters; the normal interval is not claimed as the source's method.

**Alternative source-grounded interpretations:** The displayed 0.50/0.40-0.60 may be the intended elicited prior while either beta parameter is mistyped; the beta distribution may instead have been intended for a different response quantity. No source definition resolves this.

**Quality-control relevance:** This is a planning-parameter/label consistency issue, not an observed result; it can affect interpretation or reproduction of the simulation design.

**Human question:** Which Figure 2 item is authoritative for the planned varenicline week-6 response prior: the displayed 0.50 (0.40-0.60) or Beta(785,869)?

### Protocol Table 3 Aim-1 power increases at a more stringent posterior threshold

**Exact source location:** [DOC-002 p. 34](<../../joi240036supp1_prod_1716416466.00349.pdf#page=34>), Table 3, Effect of Treatment Phase I Responders / Aim 1.

**Printed inputs:** Detection power is 0.948 at posterior threshold 0.80, 0.980 at 0.85, 0.974 at 0.90, and 0.963 at 0.95.

**Rule and calculation:** For a common simulation set and the printed nested conditions `Pr(theta>0)>t`, detections at t=0.85 must be a subset of detections at t=0.80. Thus power(0.85) <= power(0.80). Printed 0.980 - 0.948 = +0.032, contrary to the required nonincreasing order. Tolerance: 0 for the ordering identity.

**Direct observation versus inference:** The four values and thresholds are direct observations. Nested-event monotonicity is a mathematical property of the stated threshold rule. This does not infer a particular corrected value.

**Alternative source-grounded interpretations:** The values may be misordered, transcribed from different simulation summaries, or the column heading may use a different calculation not specified in the source. Other Table 3 rows are nonincreasing, but that is contextual rather than a correction.

**Quality-control relevance:** Predictive power at a stated decision threshold is a reproducibility input for the protocol’s sample-size rationale.

**Human question:** Were the Aim-1 power values attached to the intended posterior thresholds, and if so what nonnested definition permits 0.980 at 0.85 after 0.948 at 0.80?

### Protocol Table 3 duplicates an Aim-2 comparator label inconsistent with its displayed effect

**Exact source locations:** [DOC-002 p. 34](<../../joi240036supp1_prod_1716416466.00349.pdf#page=34>), Table 3 Aim 2; [DOC-002 p. 33](<../../joi240036supp1_prod_1716416466.00349.pdf#page=33>), Table 2; [DOC-002 p. 29](<../../joi240036supp1_prod_1716416466.00349.pdf#page=29>), Aim-2 contrast ordering.

**Printed inputs:** Table 3 labels both its first and third Aim-2 effects `VAR vs. NPL`. The first is 0.370 (0.309-0.431); the third is 0.195 (0.119-0.269). Table 2 gives NPL nonresponders: VAR 0.399, NPL+ 0.204, NPL 0.029. The protocol text gives the third Aim-2 contrast as VAR versus NPL+.

**Rule and calculation:** 0.399 - 0.029 = 0.370, matching the first `VAR vs NPL` row. 0.399 - 0.204 = 0.195, matching the third row and the printed third contrast order `VAR versus NPL+`. Tolerance: 0.001, the displayed three-decimal precision.

**Direct observation versus inference:** Labels and values are directly printed. The arithmetic match and contrast mapping are direct derivations from printed Table 2 and the protocol’s stated contrast order.

**Alternative source-grounded interpretations:** Table 3’s third label may be an abbreviation with an unprinted definition, or Table 2 values may be from a different average; neither is indicated. The duplicated label leaves the contrast ambiguous.

**Quality-control relevance:** Comparator labels determine which planned effect and predictive power a reader would extract.

**Human question:** Should the third Aim-2 Table 3 label read `VAR vs. NPL+` rather than the second occurrence of `VAR vs. NPL`?

### Supplement narrative misprints the EOT+30 CNRT-switch probability and both interval endpoints

**Exact source locations:** [DOC-003 p. 10](<../../joi240036supp2_prod_1716416466.01349.pdf#page=10>), Secondary Outcome Detailed Analysis; [DOC-003 p. 15](<../../joi240036supp2_prod_1716416466.01349.pdf#page=15>), EFigure 2.

**Printed inputs:** The p. 10 narrative lists the CNRT-switch-to-varenicline value as `1.0% (7.0%-1.3%)`. EFigure 2 for the matched CNRT nonabstainer/switch-to-VAR cell prints `5/51`, `10%`, `7%-13%`.

**Rule and calculation:** 5/51 = 9.80%, which rounds to 10%, and EFigure 2 provides the named same outcome/timepoint. Narrative 1.0% differs by 9.0 percentage points and its upper endpoint 1.3% differs from 13% by 11.7 percentage points. The lower/upper ordering 7.0% to 1.3% also fails. Tolerance: 0 at printed one-decimal precision for matched values; no rounding can produce these changes.

**Direct observation versus inference:** Both printed strings are direct. Fraction-to-percent rounding and interval order are direct checks. No correction is assumed.

**Alternative source-grounded interpretations:** The narrative could have lost a terminal digit or misplaced a decimal, but an alternative estimator is not named.

**Quality-control relevance:** This alters the reported secondary outcome magnitude and makes the printed interval invalidly ordered.

**Human question:** What probability and 95% CrI should the p. 10 narrative report for the CNRT nonabstainer switch-to-varenicline EOT+30 cell?

### Supplement narrative truncates the EOT+30 CNRT+ upper CrI endpoint

**Exact source locations:** [DOC-003 p. 10](<../../joi240036supp2_prod_1716416466.01349.pdf#page=10>); [DOC-003 p. 15](<../../joi240036supp2_prod_1716416466.01349.pdf#page=15>), EFigure 2.

**Printed inputs:** Narrative: CNRT+ `8.0% (5.0%-1.1%)`. EFigure 2: `4/50`, `8%`, `5%-11%`.

**Rule and calculation:** 4/50=8%. The matched EFigure interval is 5%-11%; the narrative interval is 5.0%-1.1%, whose lower endpoint exceeds its upper endpoint. Tolerance: 0 at displayed precision.

**Direct observation versus inference:** The discrepancy and ordering failure are direct comparisons. No correction is asserted.

**Alternative source-grounded interpretations:** A missing second `1` or decimal-placement error is possible; no separate estimator is identified.

**Quality-control relevance:** The narrative secondary-outcome interval is not interpretable as printed.

**Human question:** Is the narrative CNRT+ EOT+30 CrI intended to be 5%-11%, as shown in EFigure 2?

### Supplement narrative truncates the EOT+30 CNRT-switch ARD upper CrI endpoint

**Exact source locations:** [DOC-003 p. 10](<../../joi240036supp2_prod_1716416466.01349.pdf#page=10>); [DOC-003 p. 33](<../../joi240036supp2_prod_1716416466.01349.pdf#page=33>), ETable 9.

**Printed inputs:** Narrative ARD for switching to varenicline versus CNRT continuation: `6.0% (3.0%-1.0%)`. ETable 9 prints `6% (3%-10%)` for CNRT VAR (switch) relative to continue at EOT+30.

**Rule and calculation:** These are matched population, outcome, timepoint, comparator, ARD, and CrI. The upper endpoint differs, 1.0% versus 10%, and the narrative interval is reversed. Tolerance: 0 at displayed precision.

**Direct observation versus inference:** The two strings and their matching headers are direct observations; endpoint comparison is direct.

**Alternative source-grounded interpretations:** A dropped zero is plausible, but no alternative interval construction is identified.

**Quality-control relevance:** The RD interval is a reusable comparative-effect estimate.

**Human question:** Is 10% the intended upper CrI endpoint for the EOT+30 CNRT-switch ARD?

### Supplement repeats an incorrect upper CrI endpoint for the EOT+30 VAR+ relationship

**Exact source locations:** [DOC-003 pp. 10-11](<../../joi240036supp2_prod_1716416466.01349.pdf#page=10>) and [p. 11](<../../joi240036supp2_prod_1716416466.01349.pdf#page=11>), VAR+ detailed narrative; [DOC-003 p. 15](<../../joi240036supp2_prod_1716416466.01349.pdf#page=15>), EFigure 2; [DOC-003 p. 33](<../../joi240036supp2_prod_1716416466.01349.pdf#page=33>), ETable 9.

**Printed inputs:** Narrative prints VAR+ `8.0% (5.0%-1.1%)` and repeats ARD `8.0% (5.0%-1.1%)`. EFigure 2 prints `3/39`, `8%`, `5%-11%`; ETable 9 prints ARD `8% (5%-11%)`.

**Rule and calculation:** 3/39=7.69%, rounding to 8%. Both matched comparator sources give 5%-11%, while narrative gives 5.0%-1.1%, a reversed interval. Tolerance: 0 at displayed precision.

**Direct observation versus inference:** Repeated narrative and comparator strings are direct observations. The fraction and ordering check are direct derivations.

**Alternative source-grounded interpretations:** A shared transcription or rendering defect could explain the repetitions; no distinct analysis or interval type is named.

**Quality-control relevance:** Repetition can propagate a wrong interval into secondary-outcome extraction.

**Human question:** Should every VAR+ EOT+30 narrative CrI and ARD CrI ending `1.1%` instead end `11%`?

### Supplement understates the EOT+30 abstainer ARD by a factor of ten

**Exact source locations:** [DOC-003 p. 11](<../../joi240036supp2_prod_1716416466.01349.pdf#page=11>), Abstainers narrative; [DOC-003 p. 35](<../../joi240036supp2_prod_1716416466.01349.pdf#page=35>), ETable 11.

**Printed inputs:** Narrative: posterior probability 97%, `ARD = 1.1% (-1.0%-22%)` for benefit of CNRT continuation. ETable 11: EOT+30 ARD for CNRT vs VAR `11% (-1%-22%)`, probability 97%.

**Rule and calculation:** The named outcome, abstainer population, treatments, timepoint, posterior probability, and CrI endpoints match; the point estimate differs 1.1% versus 11%. Difference 9.9 percentage points. Tolerance: 0 at printed precision.

**Direct observation versus inference:** The comparison is direct. No alternative correction is inferred.

**Alternative source-grounded interpretations:** The narrative may contain decimal placement error, or the table may have a typographical whole-number error; the package does not choose.

**Quality-control relevance:** This changes the reported magnitude of an abstainer secondary outcome.

**Human question:** Is the EOT+30 abstainer ARD 11% as printed in ETable 11, or 1.1% as printed in the narrative?

### Supplement cites the compliance table instead of the ARD table for the six-month CNRT-switch comparison

**Exact source locations:** [DOC-003 p. 11](<../../joi240036supp2_prod_1716416466.01349.pdf#page=11>), six-month CNRT nonabstainers narrative; [DOC-003 p. 31](<../../joi240036supp2_prod_1716416466.01349.pdf#page=31>), ETable 7; [DOC-003 p. 33](<../../joi240036supp2_prod_1716416466.01349.pdf#page=33>), ETable 9.

**Printed inputs:** Narrative attributes the switch ARD `1.0% (-2.0%-3.0%)` and posterior probability 66% to `E-Table 7`. ETable 7 is Phase 1 Visit and Medication Compliance. ETable 9 contains the CNRT switch 6-month ARD `1% (-2%-3%)` and probability 66%.

**Rule and calculation:** A cited table for a stated ARD/probability should contain that result and measure. ETable 7 contains compliance means/medians, not ARDs; ETable 9 contains the exact printed ARD/probability. Tolerance: exact measure/table identity.

**Direct observation versus inference:** Table titles, narrative reference, and ETable 9 values are direct observations. The mismatch is a direct label/reference comparison.

**Alternative source-grounded interpretations:** `E-Table 7` may be a cross-reference numbering error; no evidence says there is another ETable 7.

**Quality-control relevance:** Incorrect table citations impair verification and can lead readers to extract compliance values instead of comparative outcomes.

**Human question:** Should the six-month CNRT-switch ARD narrative cite ETable 9 instead of ETable 7?

### Supplement six-month abstainer narrative interval and direction/reference wording do not reconcile with matched sources

**Exact source locations:** [DOC-003 p. 12](<../../joi240036supp2_prod_1716416466.01349.pdf#page=12>), six-month abstainers narrative; [DOC-003 p. 16](<../../joi240036supp2_prod_1716416466.01349.pdf#page=16>), EFigure 3; [DOC-003 p. 35](<../../joi240036supp2_prod_1716416466.01349.pdf#page=35>), ETable 11.

**Printed inputs:** Narrative: CNRT 39% (30%-48%) and VAR 40% (33%-47%), posterior probability 55%, `ARD = 1.0% (-1.3%-1.1%)`, described as small benefit of varenicline. EFigure 3 has the same 39% versus 40%. ETable 11 header says `ARD For CNRT vs. VAR`, with `1% (-11%-12%)`, probability 56%.

**Rule and calculation:** The printed narrative interval -1.3% to -1.1% is entirely negative and does not contain its positive point estimate +1.0%; it is also not the ETable 11 interval -11% to 12%. From the printed EFigure percentages, VAR minus CNRT is +1 percentage point, while CNRT minus VAR is -1 percentage point. Therefore the table’s `CNRT vs. VAR` label, its positive 1%, and the narrative direction cannot all describe the same signed ARD. Tolerance: 0 for endpoint containment and direct sign/reference agreement.

**Direct observation versus inference:** The printed values, table header, and narrative direction are direct. The raw 40%-39%=+1 percentage-point calculation is a diagnostic from displayed rounded values; it is not substituted for the Bayesian ARD.

**Alternative source-grounded interpretations:** The narrative interval may have lost digits (`-13%` and `11%`), the table header or sign may be reversed, or the ARD may use a differently signed modelled contrast. The source does not state a separate contrast definition here.

**Quality-control relevance:** Direction, reference group, and interval all control interpretation of a comparative secondary outcome.

**Human question:** What are the intended signed contrast, reference group, and 95% CrI for six-month continuous abstinence among phase-1 abstainers?

### ETable 3 reverses count and percentage in one `n (%)` cell

**Exact source location:** [DOC-003 p. 19](<../../joi240036supp2_prod_1716416466.01349.pdf#page=19>), ETable 3, Race and ethnicity `Other`, VAR nonabstainer to CNRT column (N=41).

**Printed inputs:** The table heading is `n (%)`. The cell prints `4.9 (2)`. Other populated cells in the row and table use count followed by percentage, for example `2 (2.2)` and `1 (2.0)`.

**Rule and calculation:** Under `n (%)`, a count must be an integer. `4.9` cannot be a participant count; 2/41*100=4.878%, which rounds to 4.9%. Thus the printed cell order is percentage followed by count, contrary to the row/table label. Tolerance: exact label/order identity; rounding tolerance for 2/41 is plus or minus 0.05 percentage point at one-decimal precision and passes after reversing order.

**Direct observation versus inference:** The label and `4.9 (2)` are direct. The calculation establishes why the values are compatible only in the reversed order.

**Alternative source-grounded interpretations:** The column could use a special unstated `%(n)` convention for this one cell, but surrounding cells do not. The source lacks a cell-specific note.

**Quality-control relevance:** Reversed count/percentage ordering can corrupt automated extraction and subgroup totals.

**Human question:** Should the ETable 3 cell be printed `2 (4.9)` to conform with its `n (%)` label?

### ETable 4 reverses the sign of the varenicline-to-CNRT switch contrast relative to the main results

**Exact source locations:** [DOC-003 p. 21](<../../joi240036supp2_prod_1716416466.01349.pdf#page=21>), ETable 4; [DOC-001 p. 1](<../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1>), abstract; [DOC-001 p. 5](<../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=5>), Results; [DOC-001 p. 7](<../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=7>), Figure 3.

**Printed inputs:** ETable 4 labels `Varenicline-Non-Abst. -->CNRT (switch) vs. Varenicline-(stay)` and prints ARD `3%`, 95% CrI `1%` to `4%`, NNT 39. The abstract/Results state switch to CNRT relative to continuation had RD `-3%` (CrI `-4% to -1%`). Figure 3 prints 0/41=0% for switch and 2/77=3% for continuation.

**Rule and calculation:** With the ETable 4 printed order switch minus stay, raw displayed percentages give 0%-3%=-3 percentage points, agreeing with the main-paper signed RD and not +3%. The ETable 4 interval is likewise positive while the main interval is negative. Tolerance: 0 for sign and reference-group identity.

**Direct observation versus inference:** The labels and estimates are direct. The raw difference is a diagnostic corroborated by the direct main-paper matched signed RD; it is not substituted for a modelled ARD.

**Alternative source-grounded interpretations:** ETable 4 may use an unstated beneficial-direction absolute value or reversed subtraction despite its `switch vs stay` wording; the NNT column might motivate a magnitude display. Neither convention is stated, and its interval remains directionally inconsistent with the named contrast.

**Quality-control relevance:** A reversed signed contrast can invert a treatment comparison in evidence synthesis.

**Human question:** Is ETable 4 intended to report a signed switch-minus-stay ARD of -3% (-4% to -1%), or an explicitly labelled absolute magnitude of 3%?

### ETable 3 employment rows reverse the declared `n (%)` order

**Exact source location:** [DOC-003 p. 19](<../../joi240036supp2_prod_1716416466.01349.pdf#page=19>), ETable 3, Employment rows.

**Printed inputs:** The heading is `Employment, n (%)`. All populated cells print a decimal percentage first and an integer in parentheses, including Employed `72.2 (39)` and Unemployed `27.8 (15)` under N=54, and `74.5 (38)` and `25.5 (13)` under N=51.

**Rule and calculation:** Under `n (%)`, the count occupies the first position and must be an integer. Here 39/54=72.2%, 15/54=27.8%, 38/51=74.5%, and 13/51=25.5%, so the values are consistently printed as `% (n)` instead. Tolerance is the displayed one-decimal rounding.

**Direct observation versus inference:** The heading, cells, and arithmetic are direct observations. Whether the heading or all cell orders are the production error is unresolved.

**Alternative source-grounded interpretations:** The intended heading may be `Employment, % (n)`, or the cells may need systematic reordering to count followed by percent.

**Quality-control relevance:** Reversed measure order can cause automated and manual extractors to treat percentages as counts across an entire baseline variable.

**Human question:** Should the employment heading be `% (n)`, or should every employment cell be reordered to `n (%)`?

### ETable 3 employment totals omit one participant in two columns

**Exact source location:** [DOC-003 p. 19](<../../joi240036supp2_prod_1716416466.01349.pdf#page=19>), ETable 3, Employment rows under CNRT+ N=50 and VAR+ N=39.

**Printed inputs:** CNRT+ prints Employed `80 (40)` and Unemployed `18 (9)`; VAR+ prints `69.2 (27)` and `28.2 (11)`, using the section's percentage(count) orientation despite its label.

**Rule and calculation:** With only Employed and Unemployed displayed, counts should reconcile to the header N or a missing/unreported group should be identified. CNRT+: 40+9=49, one below 50, and 80%+18%=98%. VAR+: 27+11=38, one below 39, and 69.2%+28.2%=97.4%.

**Direct observation versus inference:** Header Ns, cells, and shortfalls are direct observations. Missing employment data are a plausible but unprinted explanation.

**Alternative source-grounded interpretations:** One participant in each column may have missing employment status, the header N may not be the employment denominator, or one cell may be incomplete. No employment-specific footnote resolves the choice.

**Quality-control relevance:** Unstated missingness changes the denominator used for baseline percentage extraction and subgroup totals.

**Human question:** Do the two one-participant shortfalls represent missing employment data, and what denominator should govern the printed employment percentages?

## Non-candidate completed checks

- DOC-001 CNRT and varenicline phase-2 branch counts sum exactly to 191 and 157, respectively. The abstract 47%, 33%, and 34% parentheticals use different stated allocation/analysis constructs and were not treated as an arithmetic total.
- DOC-001 Figure 2 exclusions reconcile: 1052 declined plus 688 ineligible equals 1740 excluded; the detailed declined and ineligible component sums also reconcile.
- DOC-001 and DOC-003 raw count-to-percentage outcome values round correctly; modelled RDs were not rejected for small differences from rounded raw percentages.
- DOC-003 ETable 8 denominators 50 and 42 describe compliance populations and do not by themselves contradict outcome-analysis denominators 90 and 77, which include imputed continuation nonattenders.
- DOC-003 adverse-event `N` values and IPW estimated rates were kept on separate scales. No rate was misread as a count.
- No person-time, incidence-rate denominator, or conventional P-value display-zero relationship was printed that generated a candidate.

## Counts and limitations

- Relationships checked: 72.
- Distinct candidate consistency issues: 17.
- Direct-source confirmation was completed for every candidate location named above. The source PDFs provide no raw datasets, no protocol-to-publication version crosswalk, and no definition that resolves the identified alternative reference/sign conventions. Those absences are preserved as human questions rather than filled by inference.
