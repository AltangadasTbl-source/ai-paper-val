# Stable Candidate Ledger

All candidates are **Pending Human Adjudication**. Stable IDs were assigned only after merging genuine duplicates that concern the same printed statement, comparator, and consistency rule. Similar nearby labels were retained separately when they concern different parameters. This ledger contains the complete uncapped checker union.

## C001 — Abstract sex percentage conflicts with the enrolled sex count

- **Category:** Denominator, proportion, or total inconsistency
- **Provenance:** NUM001; CROSS-001.
- **Exact source locations:** DOC-001 [PDF p. 1](../../jama_stunnenberg_2018_oi_180136.pdf#page=1), Abstract Results; DOC-001 [PDF p. 4](../../jama_stunnenberg_2018_oi_180136.pdf#page=4), Baseline Data.
- **Printed evidence and comparator:** The abstract states that among 30 enrolled patients, `22%` were men. The enrolled-population narrative states `22 men and 8 women`.
- **Rule/calculation:** `22/30 × 100 = 73.33%`, not 22%; `22+8=30`.
- **Alternative and human question:** The abstract may have intended `22 men` or approximately `73% men`. Confirm the intended field and denominator against the enrollment data/proof.

## C002 — INQoL IQR endpoints exceed the stated 0-to-100 scale

- **Category:** Measure, label, or scale inconsistency
- **Provenance:** NUM002.
- **Exact source location:** DOC-001 [PDF p. 5](../../jama_stunnenberg_2018_oi_180136.pdf#page=5), Table 1 and footnote f; the scale statement is repeated in Table 2 on DOC-001 pp. 7-8.
- **Printed evidence and comparator:** CLCN1 INQoL is `84.0 (74.5-110.3)` and SCN4A is `98.0 (56.0-120.0)`, while the footnote states a scale from 0 to 100.
- **Rule/calculation:** Quantiles of a quantity bounded at 100 cannot be 110.3 or 120.0; the excesses are 10.3 and 20.0 points.
- **Alternative and human question:** The footnote may state the wrong/incomplete composite range, or the displayed values may use another scoring convention. Confirm the intended INQoL composite scale.

## C003 — Table 2 secondary-outcome contrast header is opposite to the displayed effect signs

- **Category:** Measure, label, or scale inconsistency
- **Provenance:** NUM003; STAT1-001.
- **Exact source locations:** DOC-001 [PDF p. 7](../../jama_stunnenberg_2018_oi_180136.pdf#page=7) and [PDF p. 8](../../jama_stunnenberg_2018_oi_180136.pdf#page=8), Table 2 secondary-outcome header and rows.
- **Printed evidence and comparator:** The header says `Treatment Effect (Placebo-Mexiletine)`. Repeated rows follow mexiletine minus placebo: INQoL `-21.44-(-7.22)=-14.22`; first handgrip `-2.39-0.46=-2.85`; SF-36 physical changes also have the mexiletine-minus-placebo sign.
- **Rule/calculation:** Reversing a subtraction reverses its sign; rounding cannot reconcile the repeated sign direction with the printed header.
- **Alternative and human question:** The header may be reversed, or an undocumented coding convention may be intended. Confirm the treatment-effect direction used for the non-IVR rows.

## C004 — Placebo “Any” adverse-reaction percentage does not reconcile with the apparent denominator

- **Category:** Denominator, proportion, or total inconsistency
- **Provenance:** NUM004.
- **Exact source locations:** DOC-003 [PDF p. 6](../../joi180136supp2_prod.pdf#page=6), eTable 4; DOC-001 [PDF p. 8](../../jama_stunnenberg_2018_oi_180136.pdf#page=8), Adverse Events.
- **Printed evidence and comparator:** eTable 4 gives placebo `Any 2 (6%)`, while surrounding pairs and the main text establish an apparent denominator of 30: 21/30=70%, 27/30=90%, 3/30=10%, and 1/30 is displayed as 3%.
- **Rule/calculation:** `2/30 × 100 = 6.67%`, ordinarily displayed as 7%, not 6%.
- **Alternative and human question:** A distinct placebo exposure denominator or truncation could yield 6%, but neither is printed. Confirm the denominator and rounding convention for this row.

## C005 — Bayesian parameter prose swaps `mu_mex[i]` and `mu_plac[i]` treatment labels

- **Category:** Measure, label, or scale inconsistency
- **Provenance:** NUM005; CROSS-003; STAT1-006.
- **Exact source locations:** DOC-003 [PDF p. 11](../../joi180136supp2_prod.pdf#page=11), eMethods 2 code and parameter dictionary; [PDF p. 13](../../joi180136supp2_prod.pdf#page=13), eMethods 3 code; [PDF p. 14](../../joi180136supp2_prod.pdf#page=14), eMethods 3 parameter dictionary.
- **Printed evidence and comparator:** The code models `Stiff_Plac` with `mu_plac` and `Stiff_Mex` with `mu_mex`; the adjacent prose describes `mu_mex[i]` as placebo and `mu_plac[i]` as mexiletine.
- **Rule/calculation:** A parameter’s treatment label must agree with the displayed likelihood/data mapping and `mu.plac-mu.mex` contrast.
- **Alternative and human question:** The two prose rows may be transposed rather than the executed code being reversed. Confirm the authoritative mapping from analysis files/output.

## C006 — `diff_CLCN1` is described as an SCN4A contrast

- **Category:** Measure, label, or scale inconsistency
- **Provenance:** NUM006; CROSS-005; STAT1-007.
- **Exact source locations:** DOC-003 [PDF p. 13](../../joi180136supp2_prod.pdf#page=13), eMethods 3 code; DOC-003 [PDF p. 14](../../joi180136supp2_prod.pdf#page=14), parameter dictionary.
- **Printed evidence and comparator:** Code defines `diff_CLCN1 <- mu.plac_CLCN1 - mu.mex_CLCN1`, but the prose describes `diff_CLCN1` as `mu.plac-mu.mex for SCN4A patients`.
- **Rule/calculation:** The genotype in the parameter description must match its code-defined components and suffix.
- **Alternative and human question:** The prose may contain a copy-forward label. Confirm whether the row should identify CLCN1 patients and whether analysis outputs used the correct mapping.

## C007 — `sigma.mex` is described as placebo-period variability

- **Category:** Measure, label, or scale inconsistency
- **Provenance:** NUM007; CROSS-004.
- **Exact source locations:** DOC-003 [PDF p. 11](../../joi180136supp2_prod.pdf#page=11), eMethods 2 code; [PDF p. 12](../../joi180136supp2_prod.pdf#page=12), eMethods 2 parameter dictionary; [PDF p. 13](../../joi180136supp2_prod.pdf#page=13), eMethods 3 code; [PDF p. 14](../../joi180136supp2_prod.pdf#page=14), eMethods 3 parameter dictionary.
- **Printed evidence and comparator:** Both prose dictionaries define `sigma.mex` as the standard deviation during placebo treatment, while the likelihood/data names and paired `mu.mex` labels associate `.mex` with mexiletine.
- **Rule/calculation:** Treatment identity is categorical; the parameter label and displayed model mapping must agree.
- **Alternative and human question:** This may be a repeated documentation error; unseen files could impose another constraint. Confirm the intended treatment-period meaning of `sigma.mex`.

## C008 — Main text prints `CLNC1` for the matched `CLCN1` genotype subgroup

- **Category:** Measure, label, or scale inconsistency
- **Provenance:** CROSS-002.
- **Exact source locations:** DOC-001 [PDF p. 4](../../jama_stunnenberg_2018_oi_180136.pdf#page=4), Primary Outcome; [PDF p. 5](../../jama_stunnenberg_2018_oi_180136.pdf#page=5), Table 1/Figure 2; [PDF p. 6](../../jama_stunnenberg_2018_oi_180136.pdf#page=6), Figure 3; DOC-003 [PDF p. 4](../../joi180136supp2_prod.pdf#page=4), eTable 2 footnote.
- **Printed evidence and comparator:** The p. 4 narrative assigns the 3.84 (95% CrI 2.52-5.16; n=16) result to `CLNC1`; matched displays and the gene definition use `CLCN1`.
- **Rule/calculation:** Identical population, estimate, interval, and n identify the same subgroup, but the gene-symbol character order differs.
- **Alternative and human question:** This is likely a local transposition. Confirm the intended gene symbol in the narrative result.

## C009 — SF-36 mental-component P value conflicts with the dependent-t 95% CI

- **Category:** Statistical reporting inconsistency
- **Provenance:** STAT1-002; relationship S010.
- **Exact source locations:** DOC-001 [PDF p. 7](../../jama_stunnenberg_2018_oi_180136.pdf#page=7), Table 2; [PDF p. 3](../../jama_stunnenberg_2018_oi_180136.pdf#page=3), dependent-t method; [PDF p. 4](../../jama_stunnenberg_2018_oi_180136.pdf#page=4), two-sided P-value convention.
- **Printed evidence and comparator:** Effect 6.78, 95% CI 1.64 to 11.92, `P=.001`; Table 2 states N=27 and a dependent t test for non-IVR secondary outcomes, with two-sided P values.
- **Rule/calculation:** With df=26, CI half-width 5.14 implies SE about 2.50, t about 2.71, and two-sided P about .012, not .001.
- **Alternative and human question:** The row-specific paired n, CI construction, or inferential procedure could differ from the table-level description but is not supplied. Confirm which P value, CI, analysis n, or test is intended.

## C010 — SCN4A fifth handgrip-action-myotonia P value conflicts with its 95% CI

- **Category:** Statistical reporting inconsistency
- **Provenance:** STAT1-003; relationship S013.
- **Exact source locations:** DOC-001 [PDF p. 7](../../jama_stunnenberg_2018_oi_180136.pdf#page=7), Table 2 row; [PDF p. 8](../../jama_stunnenberg_2018_oi_180136.pdf#page=8), Table 2 footnotes; [PDF p. 3](../../jama_stunnenberg_2018_oi_180136.pdf#page=3), dependent-t method; [PDF p. 4](../../jama_stunnenberg_2018_oi_180136.pdf#page=4), two-sided P-value convention.
- **Printed evidence and comparator:** SCN4A effect -1.96, 95% CI -3.41 to 0.51, `P=.009`; subgroup n=11 and dependent t test are stated.
- **Rule/calculation:** The printed interval crosses zero. Using df=10 and its half-width gives |t| about 2.23 and two-sided P about .05, not .009.
- **Alternative and human question:** An endpoint sign, P value, subgroup n, or test/CI definition may be misprinted or differ from the table-level rule. Confirm the intended inferential fields.

## C011 — SCN4A fifth transient-paresis estimate, interval, and P value do not form a compatible dependent-t result

- **Category:** Statistical reporting inconsistency
- **Provenance:** STAT1-004; relationship S019.
- **Exact source locations:** DOC-001 [PDF p. 7](../../jama_stunnenberg_2018_oi_180136.pdf#page=7), Table 2 row; [PDF p. 6](../../jama_stunnenberg_2018_oi_180136.pdf#page=6), narrative repetition; [PDF p. 8](../../jama_stunnenberg_2018_oi_180136.pdf#page=8), Table 2 footnotes; [PDF p. 3](../../jama_stunnenberg_2018_oi_180136.pdf#page=3), dependent-t method; [PDF p. 4](../../jama_stunnenberg_2018_oi_180136.pdf#page=4), two-sided P-value convention.
- **Printed evidence and comparator:** SCN4A effect 13.71, 95% CI -1.96 to 25.47, `P=.02`; subgroup n=11 and dependent t test are stated.
- **Rule/calculation:** The interval crosses zero although the two-sided P is below .05, and its midpoint is 11.755 rather than the printed point estimate 13.71. Under df=10, the displayed half-width gives an approximate two-sided P near .05.
- **Alternative and human question:** The lower endpoint may have a sign/transcription problem, or the P value, n, or CI procedure may differ from the table-level description. Confirm the source analysis output for this row.

## C012 — Myotonic-discharge P value conflicts with the dependent-t 95% CI

- **Category:** Statistical reporting inconsistency
- **Provenance:** STAT1-005; relationship S021.
- **Exact source locations:** DOC-001 [PDF p. 8](../../jama_stunnenberg_2018_oi_180136.pdf#page=8), Table 2 continuation and footnotes; [PDF p. 3](../../jama_stunnenberg_2018_oi_180136.pdf#page=3), dependent-t method; [PDF p. 4](../../jama_stunnenberg_2018_oi_180136.pdf#page=4), two-sided P-value convention.
- **Printed evidence and comparator:** Effect 0.67, 95% CI 0.23 to 1.11, `P<.001`; Table 2 states N=27 and dependent t tests for non-IVR secondary outcomes.
- **Rule/calculation:** With df=26, half-width 0.44 implies SE about 0.214, t about 3.13, and two-sided P about .004, not below .001.
- **Alternative and human question:** The row-specific n or test/CI computation may differ but is not printed. Confirm the intended P value, interval, analysis n, and procedure.

## C013 — First handgrip placebo-period interval is reversed and excludes its estimate

- **Category:** Statistical reporting inconsistency
- **Provenance:** STAT2-001; relationship S012.
- **Exact source location:** DOC-001 [PDF p. 7](../../jama_stunnenberg_2018_oi_180136.pdf#page=7), Table 2, first-attempt handgrip action myotonia, placebo-period change.
- **Printed evidence and comparator:** The row prints `0.46 (-0.30 to -1.23)`.
- **Rule/calculation:** The first endpoint -0.30 is greater than the second endpoint -1.23, and the point estimate 0.46 lies outside either ordering of those endpoints. A displayed interval must be ordered and contain its corresponding estimate.
- **Alternative and human question:** The endpoints may be transposed, or an endpoint sign/value or point estimate may be misprinted. Confirm the authoritative estimate and interval.

## C014 — Mean Timed Up&Go placebo-period estimate lies outside its interval

- **Category:** Statistical reporting inconsistency
- **Provenance:** STAT2-002; relationship S015.
- **Exact source location:** DOC-001 [PDF p. 7](../../jama_stunnenberg_2018_oi_180136.pdf#page=7), Table 2, mean Timed Up&Go placebo-period change.
- **Printed evidence and comparator:** The row prints `0.07 (-0.67 to 0.01)`.
- **Rule/calculation:** The point estimate 0.07 exceeds the displayed upper endpoint 0.01 and is therefore outside its stated interval.
- **Alternative and human question:** The estimate sign/value or an interval endpoint may belong to a different result. Confirm the authoritative estimate and interval.

## Registration summary

- Stable candidates registered: 14 (`C001`-`C014`).
- Every candidate remains `Pending Human Adjudication`.
- No candidate is based on a coherent display-zero P value.
