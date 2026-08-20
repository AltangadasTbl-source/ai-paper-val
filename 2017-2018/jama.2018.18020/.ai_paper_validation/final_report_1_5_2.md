# Quantitative Reporting Quality-Control Consistency Review

## Pending Human Adjudication

All 14 registered observations in this report are **Pending Human Adjudication**. They are quantitative reporting quality-control candidates, not corrections, conclusions about validity, or determinations of importance.

## Executive Quality-Control Summary

Fresh, source-first review of all supplied scientific sources registered 14 distinct candidates (C001-C014). The candidates concern arithmetic compatibility, measure labels and scales, and statistical-result fields. They were mechanically rechecked against exact supplied-PDF locations. No candidate is based solely on a coherent display-zero P value.

## Package and Fresh-Processing Provenance

The direct scientific source set comprised four supplied PDFs: the main article, protocol, quantitative supplement, and data-sharing statement. Fresh native and layout text were prepared for all pages; all pages were rendered for visual alignment; no OCR was required. No old audit derivative was used as evidence.

## Scope, Complete Coverage, and Exclusions

All 83 direct PDF-page units were mapped: DOC-001 10/10, DOC-002 55/55, DOC-003 17/17, and DOC-004 1/1. The review covers reported numeric, denominator, inferential-statistical, cross-document, label/scale, and rate/count relationships. It excludes broad clinical, design, novelty, misconduct, raw-data, and external-literature auditing.

## Quantitative and Statistical Relationship Coverage

The complete fresh mapping contains 57 numeric/reporting relationships (35 main and 22 support) and 56 inferential-statistical relationships (22 main and 34 support). Numeric review completed 57/57 relationships; cross-source review completed the combined 113 relationships. Independent statistical pass 1 completed 56/56 relationships, and independent statistical pass 2 completed 56/56 relationships and appended C013-C014. Every stable candidate received mechanical source evidence recheck and evidence-quality audit.

## Candidate Index

| ID | Candidate | Category |
|---|---|---|
| C001 | Abstract sex percentage conflicts with enrolled sex count | Denominator, proportion, or total inconsistency |
| C002 | INQoL IQR endpoints exceed stated scale | Measure, label, or scale inconsistency |
| C003 | Table 2 contrast header is opposite displayed effect signs | Measure, label, or scale inconsistency |
| C004 | Placebo `Any` adverse-reaction percentage does not reconcile with apparent denominator | Denominator, proportion, or total inconsistency |
| C005 | Bayesian `mu_mex[i]`/`mu_plac[i]` prose treatment labels are swapped | Measure, label, or scale inconsistency |
| C006 | `diff_CLCN1` is described as an SCN4A contrast | Measure, label, or scale inconsistency |
| C007 | `sigma.mex` is described as placebo-period variability | Measure, label, or scale inconsistency |
| C008 | Main text prints `CLNC1` for matched `CLCN1` subgroup | Measure, label, or scale inconsistency |
| C009 | SF-36 mental-component P value conflicts with dependent-t CI | Statistical reporting inconsistency |
| C010 | SCN4A fifth handgrip P value conflicts with CI | Statistical reporting inconsistency |
| C011 | SCN4A fifth transient-paresis fields are incompatible | Statistical reporting inconsistency |
| C012 | Myotonic-discharge P value conflicts with dependent-t CI | Statistical reporting inconsistency |
| C013 | First handgrip placebo-period interval is reversed and excludes estimate | Statistical reporting inconsistency |
| C014 | Mean Timed Up&Go placebo-period estimate lies outside interval | Statistical reporting inconsistency |

## Candidate Evidence Cards

## C001 — Abstract sex percentage conflicts with the enrolled sex count

**Candidate statement:** The abstract's `22% men` is incompatible with its enrolled total and the later count of 22 men and 8 women.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 1](<../jama_stunnenberg_2018_oi_180136.pdf#page=1>), Abstract Results; [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 4](<../jama_stunnenberg_2018_oi_180136.pdf#page=4>), Baseline Data.

**Source evidence:** The abstract prints 30 enrolled patients and `22% men`; Baseline Data prints 22 men and 8 women.

**Reported-versus-comparator:** Reported `22% men` versus comparator 22/30 men.

**Reasoning procedure:** Match the same enrolled population across the two locations and test count/percentage compatibility.

**Calculation:** `22 + 8 = 30`; `22/30 × 100 = 73.33%`; `22% × 30 = 6.6`, not 22 patients.

**Alternative source-grounded interpretations:** The abstract may have intended `22 men` or approximately `73% men`; enrollment-level data and proof history are unavailable.

**Mechanical evidence recheck:** Both printed statements, their common denominator, and the arithmetic were reproduced in the fresh evidence recheck.

**Quality-control relevance:** The candidate concerns a basic demographic count/percentage field for the same enrolled population.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy an incorrect sex distribution into a systematic review or evidence table; no propagation or conclusion change is asserted.

**Human verification steps:** Check authoritative enrollment data and manuscript proof to determine the intended abstract count, percentage, and denominator.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — INQoL IQR endpoints exceed the stated 0-to-100 scale

**Candidate statement:** Table 1 reports INQoL upper IQR endpoints above the table's stated maximum of 100.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 5](<../jama_stunnenberg_2018_oi_180136.pdf#page=5>), Table 1 and footnote f; [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 8](<../jama_stunnenberg_2018_oi_180136.pdf#page=8>), Table 2 footnote g.

**Source evidence:** CLCN1 is `84.0 (74.5-110.3)` and SCN4A is `98.0 (56.0-120.0)` while the footnote states `Scale, 0 to 100`.

**Reported-versus-comparator:** Reported upper endpoints 110.3 and 120.0 versus stated upper scale bound 100.

**Reasoning procedure:** Apply the printed bound to quantiles of the identically named INQoL composite score.

**Calculation:** `110.3 - 100 = 10.3` and `120.0 - 100 = 20.0`; a bounded score's quantile cannot exceed its bound.

**Alternative source-grounded interpretations:** The footnote may be incomplete or the displayed values may use an undocumented summed/transformed scale.

**Mechanical evidence recheck:** The row values, measure identity, and 0-to-100 statements were visually and textually matched.

**Quality-control relevance:** The candidate concerns whether the printed baseline distribution and its scale can be interpreted together.

**Potential downstream evidence impact:** If confirmed, an extractor could copy an incorrect scale or baseline distribution into a review; no downstream use is assumed.

**Human verification steps:** Verify the authoritative INQoL scoring algorithm, range, and unrounded subgroup summaries.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Table 2 secondary-outcome contrast header is opposite to the displayed effect signs

**Candidate statement:** The Table 2 header states placebo minus mexiletine, whereas repeated displayed change rows follow mexiletine minus placebo.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 7](<../jama_stunnenberg_2018_oi_180136.pdf#page=7>), Table 2 header and change-score rows; [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 8](<../jama_stunnenberg_2018_oi_180136.pdf#page=8>), Table 2 footnotes.

**Source evidence:** The header says `Treatment Effect (Placebo-Mexiletine)`; effects include -14.22 and -2.85 under rows whose period changes are -7.22/-21.44 and 0.46/-2.39.

**Reported-versus-comparator:** Printed placebo-minus-mexiletine header versus row arithmetic consistent with mexiletine-minus-placebo.

**Reasoning procedure:** Recalculate direction from both period-change columns and compare it with the fixed header.

**Calculation:** `-21.44 - (-7.22) = -14.22`; `-2.39 - 0.46 = -2.85`; reversing the subtraction reverses both signs.

**Alternative source-grounded interpretations:** The header may be reversed, or an undocumented favorable-direction convention may be applied; unrounded paired data are absent.

**Mechanical evidence recheck:** Header, multiple row values, and repeated sign direction were reproduced; small SF-36 magnitude differences may reflect paired unrounded data.

**Quality-control relevance:** Contrast direction is essential to correctly label treatment effects.

**Potential downstream evidence impact:** If confirmed, a reviewer could invert an extracted effect direction during synthesis; no such extraction is claimed.

**Human verification steps:** Inspect analysis output to establish the computed contrast and decide whether header, signs, or a note is intended.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Placebo “Any” adverse-reaction percentage does not reconcile with the apparent denominator

**Candidate statement:** eTable 4's placebo `Any 2 (6%)` is not compatible with the apparent 30-patient denominator and neighboring nearest-whole-percent displays.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [joi180136supp2_prod.pdf — PDF p. 6](<../joi180136supp2_prod.pdf#page=6>), eTable 4; [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 8](<../jama_stunnenberg_2018_oi_180136.pdf#page=8>), Adverse Events.

**Source evidence:** eTable 4 prints placebo `Any 2 (6%)`, mexiletine `Any 27 (90%)`, and count-2 rows displayed as 7%; main text prints 21 of 30 patients (70%).

**Reported-versus-comparator:** Reported 2 (6%) versus the apparent 30-patient denominator and surrounding count/percentage convention.

**Reasoning procedure:** Compare the same adverse-event table's count/percentage pairs with the supplied main-text patient denominator.

**Calculation:** `2/30 × 100 = 6.67%`, ordinarily 7%; a denominator of 31 gives 6.45%, which can round to 6%.

**Alternative source-grounded interpretations:** The row may use 31 treatment-set exposures or truncation; eTable 4 does not print a denominator, unit, or rounding rule.

**Mechanical evidence recheck:** The count, percentage, neighboring pairs, and 21/30 comparator were all reproduced at the exact printed locations.

**Quality-control relevance:** The observation is conditional on a missing denominator/rounding definition and is retained as such.

**Potential downstream evidence impact:** If confirmed, an adverse-event rate could be copied incorrectly into evidence extraction; no use or harm is asserted.

**Human verification steps:** Verify eTable 4's analysis unit, denominator, treatment-set handling, and rounding convention.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Bayesian parameter prose swaps `mu_mex[i]` and `mu_plac[i]` treatment labels

**Candidate statement:** The displayed Bayesian-code mappings and adjacent prose assign opposite treatment meanings to `mu_mex[i]` and `mu_plac[i]`.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [joi180136supp2_prod.pdf — PDF p. 11](<../joi180136supp2_prod.pdf#page=11>), eMethods 2 code/dictionary; [joi180136supp2_prod.pdf — PDF p. 13](<../joi180136supp2_prod.pdf#page=13>), eMethods 3 code; [joi180136supp2_prod.pdf — PDF p. 14](<../joi180136supp2_prod.pdf#page=14>), eMethods 3 dictionary.

**Source evidence:** Code maps `Stiff_Plac` to `mu_plac` and `Stiff_Mex` to `mu_mex`; dictionaries describe `mu_mex[i]` as placebo and `mu_plac[i]` as mexiletine.

**Reported-versus-comparator:** Prose treatment labels versus likelihood/data-to-parameter mappings and named population parameters.

**Reasoning procedure:** Follow each treatment-specific data branch through the printed likelihood and compare it with the dictionary label.

**Calculation:** `Stiff_Plac -> mu_plac` and `Stiff_Mex -> mu_mex`; `diff_patient <- mu_plac[i] - mu_mex[i]` follows that code mapping.

**Alternative source-grounded interpretations:** Two prose rows may be transposed while executed code/output remained correct; executed files and logs are not supplied.

**Mechanical evidence recheck:** Both eMethods code blocks and dictionaries reproduce the same code/prose mismatch.

**Quality-control relevance:** Treatment labels affect interpretation and reproducibility of model parameters.

**Potential downstream evidence impact:** If confirmed, model documentation could be copied with reversed treatment meanings; no execution error is asserted.

**Human verification steps:** Compare the authoritative executed model files, run logs, and output mapping with the published dictionary.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — `diff_CLCN1` is described as an SCN4A contrast

**Candidate statement:** The dictionary describes `diff_CLCN1` as SCN4A although its displayed code components are CLCN1.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [joi180136supp2_prod.pdf — PDF p. 13](<../joi180136supp2_prod.pdf#page=13>), eMethods 3 code; [joi180136supp2_prod.pdf — PDF p. 14](<../joi180136supp2_prod.pdf#page=14>), parameter dictionary.

**Source evidence:** Code defines `diff_CLCN1 <- mu.plac_CLCN1 - mu.mex_CLCN1`; the dictionary says `mu.plac-mu.mex for SCN4A patients`.

**Reported-versus-comparator:** SCN4A prose description versus the CLCN1 parameter suffix and both CLCN1 code components.

**Reasoning procedure:** Compare categorical genotype identity in the printed name, components, and dictionary row.

**Calculation:** Substituting the displayed components produces the CLCN1 placebo-minus-mexiletine contrast, not an SCN4A contrast.

**Alternative source-grounded interpretations:** The row may be a copy-forward of the preceding SCN4A description; executed output is unavailable.

**Mechanical evidence recheck:** The code, genotype coding, and both adjacent dictionary rows were matched.

**Quality-control relevance:** The candidate concerns subgroup-effect identification in model documentation.

**Potential downstream evidence impact:** If confirmed, a subgroup contrast could be misidentified during model reproduction or evidence extraction; no such use is claimed.

**Human verification steps:** Verify the executed parameter-to-output mapping and intended dictionary label.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — `sigma.mex` is described as placebo-period variability

**Candidate statement:** Both parameter dictionaries describe `sigma.mex` as placebo variability despite the displayed mexiletine model branch.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [joi180136supp2_prod.pdf — PDF p. 11](<../joi180136supp2_prod.pdf#page=11>), eMethods 2 code; [joi180136supp2_prod.pdf — PDF p. 12](<../joi180136supp2_prod.pdf#page=12>), eMethods 2 dictionary; [joi180136supp2_prod.pdf — PDF p. 13](<../joi180136supp2_prod.pdf#page=13>), eMethods 3 code; [joi180136supp2_prod.pdf — PDF p. 14](<../joi180136supp2_prod.pdf#page=14>), eMethods 3 dictionary.

**Source evidence:** `tau.mex <- 1/(sigma.mex*sigma.mex)` is used with `mu_mex` and `Stiff_Mex`, while prose calls `sigma.mex` placebo-period variability.

**Reported-versus-comparator:** Placebo wording versus `.mex` likelihood branch, mean parameter, and parallel `.plac` parameter.

**Reasoning procedure:** Follow the variance-to-precision-to-mean-to-data chain for the named treatment branch.

**Calculation:** `tau.mex = 1/sigma.mex^2` supplies precision for `mu_mex`, which is used for `Stiff_Mex`.

**Alternative source-grounded interpretations:** The wording may be repeated copy-forward text while code remains correct; executed models/logs are not supplied.

**Mechanical evidence recheck:** Both code/dictionary pairs show the same category-label mismatch.

**Quality-control relevance:** Variance-component treatment identity affects accurate interpretation and reproduction.

**Potential downstream evidence impact:** If confirmed, variance-component documentation could be copied with the wrong period identity; no downstream consequence is assumed.

**Human verification steps:** Check compiled model files, posterior parameter names, and downstream exports for the intended period identity.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — Main text prints `CLNC1` for the matched `CLCN1` genotype subgroup

**Candidate statement:** A main-text subgroup result is labeled `CLNC1` while matched displays and the supplement identify CLCN1.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 4](<../jama_stunnenberg_2018_oi_180136.pdf#page=4>), Primary Outcome; [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 5](<../jama_stunnenberg_2018_oi_180136.pdf#page=5>), Table 1/Figure 2; [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 6](<../jama_stunnenberg_2018_oi_180136.pdf#page=6>), Figure 3; [joi180136supp2_prod.pdf — PDF p. 4](<../joi180136supp2_prod.pdf#page=4>), eTable 2 footnote.

**Source evidence:** Page 4 assigns 3.84 (95% CrI 2.52-5.16; n=16) to `CLNC1`; matched displays and gene definition use `CLCN1`.

**Reported-versus-comparator:** `CLNC1` in narrative versus `CLCN1` in matched subgroup displays with identical estimate, interval, and n.

**Reasoning procedure:** Match subgroup identity using population, estimate, interval, sample size, and gene-definition context.

**Calculation:** The numeric keys 3.84, 2.52-5.16, and n=16 identify one subgroup; only the gene-symbol character order differs.

**Alternative source-grounded interpretations:** This may be a local typographical transposition; supplied evidence does not establish an effect on analysis.

**Mechanical evidence recheck:** Exact physical pages and matching quantitative keys were reproduced.

**Quality-control relevance:** The mismatch is in a subgroup label attached to a reported quantitative result.

**Potential downstream evidence impact:** If confirmed, a subgroup label could be copied incorrectly into a review or evidence table; no propagation is asserted.

**Human verification steps:** Verify the intended gene symbol in the narrative against the authoritative subgroup definition and result output.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C009 — SF-36 mental-component P value conflicts with the dependent-t 95% CI

**Candidate statement:** The SF-36 mental-component effect, CI, P value, and printed dependent-t context do not reconcile under the table-level N=27 assumption.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 7](<../jama_stunnenberg_2018_oi_180136.pdf#page=7>), Table 2; [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 3](<../jama_stunnenberg_2018_oi_180136.pdf#page=3>), dependent-t method; [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 4](<../jama_stunnenberg_2018_oi_180136.pdf#page=4>), two-sided P-value convention.

**Source evidence:** The row reports effect 6.78, 95% CI 1.64 to 11.92, and `P=.001`; Table 2 states N=27 and dependent t tests for non-IVR secondary outcomes.

**Reported-versus-comparator:** Reported `.001` versus CI-derived two-sided diagnostic under df=26.

**Reasoning procedure:** Use CI half-width, printed effect, table-level paired-N assumption, and stated two-sided dependent-t method as a conditional reconciliation check.

**Calculation:** Half-width `5.14` gives SE about `5.14/2.056 = 2.50`; `t ≈ 6.78/2.50 = 2.71`; two-sided P is about `.012`, not `.001`.

**Alternative source-grounded interpretations:** Row-specific paired n, CI construction, or inferential procedure could differ but are not supplied.

**Mechanical evidence recheck:** The row fields and method/sidedness statements were matched; the N/df assumption is explicitly conditional.

**Quality-control relevance:** The candidate tests compatibility among reported inferential fields, not clinical interpretation.

**Potential downstream evidence impact:** If confirmed, an effect/CI/P result set could be extracted inconsistently into a review; no synthesis consequence is asserted.

**Human verification steps:** Obtain row-specific complete-pair n, unrounded estimate/SE, CI method, statistic, and authoritative P value.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C010 — SCN4A fifth handgrip-action-myotonia P value conflicts with its 95% CI

**Candidate statement:** The SCN4A fifth handgrip effect, zero-crossing CI, and `P=.009` do not reconcile under the printed subgroup dependent-t context.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 7](<../jama_stunnenberg_2018_oi_180136.pdf#page=7>), Table 2 row; [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 8](<../jama_stunnenberg_2018_oi_180136.pdf#page=8>), Table 2 footnotes; [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 3](<../jama_stunnenberg_2018_oi_180136.pdf#page=3>), method; [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 4](<../jama_stunnenberg_2018_oi_180136.pdf#page=4>), sidedness.

**Source evidence:** The row prints -1.96, 95% CI -3.41 to 0.51, `P=.009`; subgroup n=11 and dependent t test are stated.

**Reported-versus-comparator:** Reported `.009` versus a CI that crosses zero and the conditional df=10 diagnostic.

**Reasoning procedure:** Check interval containment/centering and infer an approximate SE from the printed CI under the stated subgroup-N convention.

**Calculation:** CI half-width 1.96 with df=10 gives SE about `1.96/2.228 = 0.88`; `|t| ≈ 1.96/0.88 = 2.23`, two-sided P about `.05`.

**Alternative source-grounded interpretations:** A P value, endpoint, subgroup n, or CI/test definition may differ from the table-level rule.

**Mechanical evidence recheck:** The effect, interval, P value, footnote, method, and sidedness were reproduced exactly.

**Quality-control relevance:** The candidate concerns coherence of a printed subgroup inferential result.

**Potential downstream evidence impact:** If confirmed, this subgroup effect/CI/P combination could be extracted inaccurately; no downstream use is asserted.

**Human verification steps:** Verify complete-pair n, paired observations, unrounded SE/statistic, CI, and P from source analysis output.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C011 — SCN4A fifth transient-paresis estimate, interval, and P value do not form a compatible dependent-t result

**Candidate statement:** The SCN4A fifth transient-paresis estimate, interval, and P value are mutually incompatible under the printed dependent-t context.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 7](<../jama_stunnenberg_2018_oi_180136.pdf#page=7>), Table 2 row; [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 6](<../jama_stunnenberg_2018_oi_180136.pdf#page=6>), narrative repetition; [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 8](<../jama_stunnenberg_2018_oi_180136.pdf#page=8>), footnotes; [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 3](<../jama_stunnenberg_2018_oi_180136.pdf#page=3>), method; [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 4](<../jama_stunnenberg_2018_oi_180136.pdf#page=4>), sidedness.

**Source evidence:** The row prints 13.71, 95% CI -1.96 to 25.47, and `P=.02`; subgroup n=11 and dependent t test are stated.

**Reported-versus-comparator:** Reported estimate/CI/P versus interval midpoint, zero crossing, and conditional df=10 diagnostic.

**Reasoning procedure:** Test CI centering and sign compatibility, then calculate a conditional interval-width diagnostic.

**Calculation:** Midpoint is `(-1.96 + 25.47)/2 = 11.755`, not 13.71; CI crosses zero; half-width 13.715 gives a two-sided diagnostic near `.05`, not `.02`.

**Alternative source-grounded interpretations:** A lower-endpoint sign/transcription, P value, n, or procedure may be different; raw output is absent.

**Mechanical evidence recheck:** The direct PDF confirms the row's `.02`, interval, and repeated narrative estimate at the recorded pages.

**Quality-control relevance:** The candidate is a row-specific statistical reporting consistency check.

**Potential downstream evidence impact:** If confirmed, this subgroup inferential result could be copied inconsistently into later evidence products; no conclusion change is claimed.

**Human verification steps:** Check authoritative paired-output fields: lower endpoint, estimate, complete-pair n, SE/statistic, and P value.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C012 — Myotonic-discharge P value conflicts with the dependent-t 95% CI

**Candidate statement:** The myotonic-discharge effect, CI, and `P<.001` do not reconcile under the printed N=27 dependent-t context.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 8](<../jama_stunnenberg_2018_oi_180136.pdf#page=8>), Table 2 continuation and footnotes; [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 3](<../jama_stunnenberg_2018_oi_180136.pdf#page=3>), dependent-t method; [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 4](<../jama_stunnenberg_2018_oi_180136.pdf#page=4>), two-sided convention.

**Source evidence:** The row reports effect 0.67, 95% CI 0.23 to 1.11, and `P<.001`; Table 2 states N=27 and dependent t tests for non-IVR outcomes.

**Reported-versus-comparator:** Reported `P<.001` versus a CI-derived two-sided diagnostic under df=26.

**Reasoning procedure:** Derive conditional SE and t from effect and CI half-width using the printed method and table-level N.

**Calculation:** Half-width `.44` gives SE about `.44/2.056 = .214`; `t ≈ .67/.214 = 3.13`; two-sided P about `.004`, not below `.001`.

**Alternative source-grounded interpretations:** Row-specific n, paired-difference variability, or exact CI/P calculation may differ but are not printed.

**Mechanical evidence recheck:** The result fields and method statements were matched; the complete-pair-N assumption is retained as conditional.

**Quality-control relevance:** The candidate concerns consistency among reported inferential fields.

**Potential downstream evidence impact:** If confirmed, an extractor could copy an incompatible effect/CI/P set; no downstream action is asserted.

**Human verification steps:** Verify row-specific n, paired-difference SE, statistic, CI method, and exact P value.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C013 — First handgrip placebo-period interval is reversed and excludes its estimate

**Candidate statement:** The first-attempt handgrip placebo-period cell prints an interval in reverse order that also excludes its printed point estimate.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 7](<../jama_stunnenberg_2018_oi_180136.pdf#page=7>), Table 2 first-attempt handgrip action-myotonia placebo-period change.

**Source evidence:** The cell prints `0.46 (-0.30 to -1.23)`.

**Reported-versus-comparator:** Printed estimate 0.46 versus printed endpoints -0.30 and -1.23.

**Reasoning procedure:** Check endpoint ordering and whether the stated point estimate belongs to the displayed interval.

**Calculation:** `-0.30 > -1.23`; even when ordered as -1.23 to -0.30, 0.46 is outside. The same row gives `-2.39 - 0.46 = -2.85` for the observed treatment-effect direction.

**Alternative source-grounded interpretations:** Endpoints may be transposed, or an endpoint sign/value or point estimate may be misprinted.

**Mechanical evidence recheck:** The cell and same-row arithmetic were read from the physical p. 7 table.

**Quality-control relevance:** This is a direct interval-ordering and estimate-containment check independent of unavailable raw data.

**Potential downstream evidence impact:** If confirmed, a placebo-period summary or interval could be copied incorrectly into evidence extraction; no propagation is claimed.

**Human verification steps:** Verify authoritative placebo estimate, interval endpoints, SE, and paired sample size.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C014 — Mean Timed Up&Go placebo-period estimate lies outside its interval

**Candidate statement:** The mean Timed Up&Go placebo-period estimate exceeds the upper endpoint of its printed interval.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 7](<../jama_stunnenberg_2018_oi_180136.pdf#page=7>), Table 2 mean Timed Up&Go placebo-period change.

**Source evidence:** The cell prints `0.07 (-0.67 to 0.01)`.

**Reported-versus-comparator:** Printed estimate 0.07 versus ordered interval -0.67 to 0.01.

**Reasoning procedure:** Test whether the stated estimate is contained between the printed endpoints.

**Calculation:** `0.07 > 0.01`; the estimate exceeds the printed upper endpoint by `0.06`. Same-row arithmetic gives `-1.05 - 0.07 = -1.12` under the observed table direction.

**Alternative source-grounded interpretations:** An endpoint digit, estimate sign/value, or other table field may be transcribed incorrectly.

**Mechanical evidence recheck:** The physical p. 7 cell, containment failure, and same-row arithmetic were reproduced.

**Quality-control relevance:** This is a direct estimate-containment consistency check.

**Potential downstream evidence impact:** If confirmed, a placebo-period estimate or interval could be copied incorrectly into later evidence products; no downstream use is asserted.

**Human verification steps:** Verify the authoritative estimate, endpoints, SE, and paired sample size in source analysis output.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If confirmed by human adjudication, the candidates identify fields that a systematic review, meta-analysis, guideline, or data extractor could copy: participant characteristics, baseline scales, treatment-effect direction, adverse-event rates, subgroup labels, model parameter definitions, and effect/interval/P-value sets. The supplied package does not show that any field was propagated, changed a conclusion, or caused harm.

## Limitations and Missing Definitions

The review is confined to the four supplied PDFs and uses no external literature or prior audit derivatives. Raw paired observations, row-specific complete-pair counts, unrounded estimates and standard errors, covariance data, executed Bayesian model files/logs, the eTable 4 denominator/rounding definition, and an authoritative INQoL scoring worksheet are unavailable. C009-C012 use explicitly conditional reconciliation diagnostics; C013-C014 are direct ordering/containment checks. Figure geometry was not converted into invented numerical precision. This is not a broad methodology, clinical, raw-data-validity, or misconduct audit.

## Human Adjudication Checklist

- Review each card against the linked supplied PDF page and the named comparator.
- Obtain missing authoritative outputs or definitions where the card identifies them.
- Record validity, importance, action, initials, and notes in that card's blank fields.
- Keep candidate IDs stable and preserve the distinction between direct observations and alternative explanations.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and Source Integrity

Source SHA-256 values were recorded before review in `review_1_5_2/source_hashes_before.sha256` and recomputed unchanged after final assembly. Fresh assets comprise native text, layout text, metadata, and 83 rendered pages; native/layout text was usable for every page and CPU OCR was not required.

### Agent Execution

The execution manifest records the coordinator plus fresh preprocessing, main/support mapping, numeric, cross-source, two independent statistical-pass, recheck, quality-audit, and report-generation agents. Statistical passes 1 and 2 are distinct fresh `gpt-5.6-terra` high-effort executions and each covers all 56 statistical relationships.

### Reproducibility Performance

- **Target basis:** Four supplied scientific PDF sources totaling 83 pages: a 10-page main article, a 55-page protocol, a 17-page quantitative supplement with tables, figures, and Bayesian model specifications, and a 1-page data-sharing statement. All 83 units require fresh extraction and mapping; native PDF text is expected for most units, while result-relevant visual tables/figures require targeted rendering and OCR only if native/layout text proves unusable. This is smaller than the 102-page calibration package but retains substantial cross-document and statistical-review complexity.
- **Total source units:** 83
- **Fresh-source units:** 83
- **Target elapsed minutes:** 30-45
- **Started UTC:** 2026-08-20T18:02:32Z
- **Finished UTC:** 2026-08-20T18:45:43Z
- **Observed elapsed minutes:** 43.2
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token Accounting and Cost

The runtime did not expose authoritative response-level token counts for the coordinator or any specialist. Every manifested execution is therefore recorded as `UNAVAILABLE` with exact `__` token fields. Known subtotals are zero because no authoritative token counts were exposed; this is not an estimate that usage was zero. Cached input and cache-write counts are input subsets; reasoning is an output subset and is not added again to total tokens. Any monetary values are token-only API-equivalent estimates under the 2026-08-18 pricing snapshot, not an invoice.

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Total tokens | Known token cost (USD) | Notes |
|---|---:|---:|---|
| gpt-5.6-sol | 0 | 0.000000 | 3 agents; authoritative runtime usage unavailable. |
| gpt-5.6-terra | 0 | 0.000000 | 8 agents; authoritative runtime usage unavailable. |

Per-agent detail is recorded in `review_1_5_2/token_usage_summary.md` and `review_1_5_2/token_usage_summary.json`.
