# Independent inclusion screen — statistical pass 2 — Workflow 1.6.2

Runtime ID: 01a129d7-7723-7a51-85ed-fef5e15acf20. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN. This screener is distinct from the initial screener and both statistical agents. Assigned scope: the complete finding F-ST2-001 in checkers/statistical_pass_2.md, including every cited source location and consolidation against the current ledger. QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read completely, together with the current tooling record, ledger, initial screening, mechanical recheck and complete statistical-pass-2 artifact. No legacy scientific conclusions or external evidence were consulted. No source or reused artifact was modified.

## Row for coordinator append

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-ST2-001 | statistics_pass_2 | pass_2 | INCLUDE | MEETS_THRESHOLD | PENDING |

F-ST2-001: Route A, category 4 qualifies because the empirical arm-CI root-sum-square rule reproduces every earlier WOMAC total-pain time point in the same display but leaves 24-week endpoint discrepancies above .05 after all display allowances; consolidate this retained occurrence with the already included C012 interval-width pattern.

The coordinator should append this row to the sole canonical screening table and replace PENDING with the existing C012. This stage assigns no new stable ID. INCLUDE preserves the independently qualifying new finding and all new locations rather than omitting them under a duplicate reason.

## Exact source confirmation

All locations below have role REPORT by content: they describe results or the analyses producing those results in the completed trial. PLAN material is not part of this finding.

- [Main p6, Table 2 WOMAC total pain at 24 weeks](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6): krill modeled change −87 (95% CI −110 to −63), placebo modeled change −83 (−106 to −59), between-group difference 3.0 (−24 to 31), P=.81. The table prints the same outcome's range in its surrounding definitions and identifies baseline adjustment for WOMAC total pain in the footnote.
- [Results p5, eTable 4 WOMAC total pain, all six time points](../../../joi240048supp3_prod_1727199125.83025.pdf#page=5): the 24-week row repeats the two changes and their intervals, with difference 3 (−24 to 31), P=.81; all five earlier total-pain rows were read independently and are transcribed below.
- [Main p4, Statistical Analyses](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4) and [main p7, methods continuation](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7): primary and secondary outcomes use a longitudinal mixed model; changes within groups and differences in changes are linear combinations of estimated coefficients. The described model includes treatment, month, their interaction, conditional baseline adjustment, participant/center random intercepts and a month random slope.
- [Results p6, eTable 4 adjustment footnote and metabolic rows](../../../joi240048supp3_prod_1727199125.83025.pdf#page=6): adjustment includes baseline where the baseline difference criterion is met, explicitly listing WOMAC total pain among adjusted outcomes. Glucose12 and its neighboring glucose/lipid witnesses were independently read to assess consolidation with C012.

The main and supplementary WOMAC copies agree with each other. The finding compares arm/contrast intervals against a reproducing rule within a report display; it does not allege a cross-report copy discrepancy. The total-pain result is a secondary outcome, but this is a reproduced within-display statistical-method conflict in always-register category 4, rather than a peripheral comparison of secondary outcome copies.

## Independent numerical reproduction

The empirical diagnostic uses the arm-CI half-widths hK and hP and computes a contrast half-width as sqrt(hK squared + hP squared). Each arm endpoint receives its own half-unit interval. This diagnostic is supported by the other rows of the same display; it is not an assertion that the unpublished fitted model has zero covariance, identical degrees of freedom or a particular critical value.

The independently read supplementary same-outcome witnesses are:

| WOMAC total-pain week | Krill change and CI | Placebo change and CI | Printed difference and CI | Recomputed half-width envelope | Printed half-width envelope |
|---|---|---|---|---|---|
| 4 | −33 (−45, −20) | −38 (−50, −25) | −5 (−23, 13) | [16.970563, 18.384776] | [17.5, 18.5] |
| 8 | −50 (−64, −37) | −53 (−67, −40) | −3 (−22, 16) | [18.384776, 19.798990] | [18.5, 19.5] |
| 12 | −54 (−69, −40) | −57 (−72, −43) | −3 (−24, 18) | [19.798990, 21.213203] | [20.5, 21.5] |
| 16 | −67 (−83, −51) | −68 (−84, −52) | −1 (−24, 22) | [21.920310, 23.334524] | [22.5, 23.5] |
| 20 | −72 (−90, −54) | −67 (−85, −49) | 5 (−21, 30) | [24.748737, 26.162951] | [25, 26] |
| 24 | −87 (−110, −63) | −83 (−106, −59) | 3 (−24, 31) | [32.526912, 33.941125] | [27, 28] |

All five earlier width envelopes overlap their printed counterparts; the 24-week width envelopes are disjoint. This is not an assumption imposed solely on a single isolated row. As additional within-main witnesses, Table 2 weight-bearing24 has arm half-widths 9.5/9.5 and root-sum-square 13.435 versus printed 13; non-weight-bearing24 has half-widths 8.5/8 and root-sum-square 11.673 versus printed 12; function24 has half-widths 58.5/57.5 and root-sum-square 82.027 versus printed 82. Their endpoint allowances admit these widths, supporting the same rule within the main display as well.

For WOMAC total24, integer endpoint allowances ±.5 yield hK and hP each in [23,24], hence combined width [32.5269119,33.9411255]. The main difference 3.0 allows [2.95,3.05]. Centering the diagnostic on that printed difference gives lower endpoint [−30.9911255,−29.4769119] and upper endpoint [35.4769119,36.9911255]. The printed limits allow [−24.5,−23.5] and [30.5,31.5]. The residual gaps are 4.9769119/24=.2073713 and 3.9769119/31=.1282875, both greater than .05.

Using the supplementary integer estimate's wider [2.5,3.5] allowance still gives lower endpoint [−31.4411255,−29.0269119] and upper endpoint [35.0269119,37.4411255]. Residual gaps are 4.5269119/24=.1886213 and 3.5269119/31=.1137714. Thus neither copy reconciles under any of the displayed allowances. No final replacement interval is proposed.

The point-contrast algebra itself reconciles within precision: placebo-minus-krill changes allow [3,5], which overlaps the main printed estimate allowance [2.95,3.05]. The CI contains zero and P=.81 is nonsignificant. No interval-null/P conflict is claimed, and an approximate exact P calculation is not substituted for an unreported producing test.

## Inclusion and classification

**Qualifying route:** Route A, category 4. Exact printed values are confirmed and a method reproducing other rows fails to reproduce this interval above the prescribed display-precision threshold. Category 4 explicitly makes the unreported producing method a human question rather than a CONDITIONAL_OR_UNREPORTED exclusion. Unchanged nonsignificance does not make the extracted interval or its precision unchanged.

**Affected result or extracted value:** The 24-week WOMAC total-pain between-group confidence interval, particularly its width and the precision used in evidence synthesis; the already registered glucose12 interval remains an affected occurrence of the same retained pattern.

**Proposed review domain:** statistical_results. **Primary relationship type:** S_W. **All relationships:** S_W. **Compared document roles:** REPORT results glucose12/WOMAC24 contrast intervals vs REPORT results arm intervals and reproducing adjacent rows, with REPORT main WOMAC24 within-display occurrence. The main and supplement agree on their WOMAC values; agreement between copies and a common pattern across reports do not add a conflicting S_C relationship. No precedence change is needed.

**Classification ambiguity:** Exact row-specific covariance, critical values, degrees of freedom and variance/marginalization conventions are absent. These affect scientific explanation, not the content-based REPORT assignment or the within-display relationship.

## Consolidation with C012

Expand C012 rather than assign a new stable ID. This is the same narrowly defined repeated pattern: modeled continuous-treatment contrast intervals do not follow the empirical root-sum-square arm-width rule that reproduces neighboring rows of results eTable 4. Both glucose12 and WOMAC24 retain compatible point subtraction and null/P interpretation; the issue in each is the contrast interval's precision under this identical reproducing rule. Glucose is wider and WOMAC narrower than that rule, but direction of width discrepancy does not establish independent causes or a different rule.

The current C012 notes that glucose12's entire contrast tuple matches hsCRP12. That is an observed repetition and a possible explanatory clue, not proof of a separate production cause. WOMAC's baseline adjustment and glucose's unadjusted status likewise do not establish distinct causes: WOMAC's five earlier rows share the same baseline-adjusted outcome and reproduce the rule. The sources disclose no independently established mechanism requiring separate candidates. This consolidation follows the one-issue/pattern requirement without discarding either observation or asserting that their actual production mechanism is identical.

This interval-width pattern remains separate from C008's modeled point-contrast identity failures, which use a different rule and retain their own already registered tuples. The pass-2 observations of additional width signals in those C008 tuples remain attached there; this screen does not re-emit them or suppress an assigned ID.

Suggested expanded descriptive title: Repeated contrast intervals differ from a reproducing display-width rule. Retain F-ST1-002 and add F-ST2-001 to C012's finding provenance. Retain every existing glucose source, calculation, alternative and question. Add main pp4/6/7 and results pp5/6; preserve all five WOMAC witness rows and both copies' endpoint calculations. The canonical recheck must mechanically inspect the expanded WOMAC occurrence before the final report. This stage does not set the final expanded evidence state or inclusion-audit field.

## Source-grounded alternatives and remaining human question

A row-specific arm covariance, different critical value/degrees of freedom, variance calculation or marginalization could explain WOMAC24, despite the empirical rule reproducing every earlier same-outcome row. A shared-coefficient model can generate nonzero covariance between estimated arm changes; none is assumed absent. The glucose tuple repetition could reflect another analysis or coincidental repeated output. The exact model output and interval conventions needed to distinguish these alternatives are not supplied. Observed rule departures are separated from these inferred explanations; no preferred analysis, mechanism or final correction is assigned.

Remaining question for the expanded issue: Which row-specific covariance, critical value and interval calculation produced the glucose12 and WOMAC24 contrast intervals, and why do these intervals differ from the arm-width rule reproducing adjacent rows of the same displays?

## Completeness, provenance and limits

One of one assigned findings screened: one INCLUDE, zero SCREENED_OUT, one included occurrence consolidated into one existing issue, zero proposed new stable IDs. Counts for every screened-out reason code are zero. No source location or finding remains unexamined. All eventual candidates remain Pending Human Adjudication.

Authoritative current-source CPU images independently viewed: preprocessing/statistical_pass_1/main-p06.png, result-p05.png and result-p06.png, direct Poppler 26.01.0 renders whose source/engine/CPU provenance is recorded in their originating artifact. Main methods pp4/7 were reread directly using pdftotext -f N -l N -layout SOURCE -, Poppler 26.01.0. No new derivative was needed or written. Arithmetic was independently computed from the printed values with JavaScript Math.hypot and ordinary interval arithmetic; all inputs, bounds and residual gaps are printed above. No OCR, fallback engine, external literature or Python extraction/orchestration was used. Missing producing covariance/critical values are bounded interpretation limits, not source-coverage gaps.
