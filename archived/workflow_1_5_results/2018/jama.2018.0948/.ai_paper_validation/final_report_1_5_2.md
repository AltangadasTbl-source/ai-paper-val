# Quantitative Quality-Control Consistency Review — JAMA 2018 Paper Package

> # Pending Human Adjudication
>
> All seven candidates are quantitative reporting quality-control candidates, not findings of validity, correction, severity, acceptance, exclusion, or paper-level conclusion change. Each requires human adjudication.

## 3. Executive Quality-Control Summary

**Stable candidate count:** 7.

Fresh source-first processing covered all 69/69 direct PDF-page units, 88/88 numeric/reporting relationships, and 45/45 statistical relationships. Both independent statistical passes completed all 45 relationships. Seven distinct source-grounded reporting-consistency candidates were registered, mechanically rechecked, and retained in stable ledger order. Small preventable reporting defects can matter when downstream evidence products extract values or definitions; this review does not claim propagation, changed conclusions, or harm.

## 4. Package and Fresh-Processing Provenance

Only the four supplied PDFs and current, manifested Workflow 1.5.2 artifacts were used as evidence. Source hashes matched before and after review. No web material, external literature, source modification, or legacy audit derivative was used as evidence.

| Source ID | Direct source | Pages | SHA-256 |
|---|---|---:|---|
| DOC-001 | [jama_parshuram_2018_oi_180015.pdf — PDF p. 1](<../jama_parshuram_2018_oi_180015.pdf#page=1>) | 11 | `92c3a3edd598a1073e39f8d0733352b3aea3bec30731b9ef0326e68f2e6088ba` |
| DOC-002 | [joi180015supp1_prod.pdf — PDF p. 1](<../joi180015supp1_prod.pdf#page=1>) | 37 | `67409a1493b032cb49b26a4444e37eabeb2a432d2d0b5576914baac310490306` |
| DOC-003 | [joi180015supp2_prod.pdf — PDF p. 1](<../joi180015supp2_prod.pdf#page=1>) | 7 | `6dab9fdc7fa6ca0da2031d5a483a58ba8ad9a3b0c6c4e7c45eb17708535465a4` |
| DOC-004 | [joi180015supp3_prod.pdf — PDF p. 1](<../joi180015supp3_prod.pdf#page=1>) | 14 | `3b58616d0af25610fe9e4bab11ac42c7e38dae588e3d965ec306b8e5b55d1eb3` |

## 5. Scope, Complete Coverage, and Exclusions

The review addressed numeric, denominator/proportion/total, inferential-statistical, cross-document numeric, effect-measure/label/scale, and rate-versus-count consistency. The four source rows were complete: 69 total units, 0 reusable units, 69 fresh-required units, and 69 mapped units.

| Source | Total | Reusable | Fresh-required | Mapped | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 | 11 | 0 | 11 | 11 | COMPLETE |
| DOC-002 | 37 | 0 | 37 | 37 | COMPLETE |
| DOC-003 | 7 | 0 | 7 | 7 | COMPLETE |
| DOC-004 | 14 | 0 | 14 | 14 | COMPLETE |
| **Total** | **69** | **0** | **69** | **69** | **COMPLETE** |

Unmanifested material from the superseded tool-limited run was excluded, including `preprocessing/tool_and_page_status.md`, `statistics/parts/main_statistical_relationships.md`, `statistics/parts/support_statistical_relationships.md`, and `checkers/candidate_parts/*.md`. Those preserved files did not define the evidence chain or constrain this report. No broad methodology, clinical, misconduct, raw-data, or validity audit was undertaken. No candidate was created from a display-zero P value; `<.0001` was treated as threshold notation.

## 6. Quantitative and Statistical Relationship Coverage

| Coverage domain | Complete coverage |
|---|---:|
| Numeric/reporting relationships | 88/88 N IDs |
| Statistical relationships, pass 1 | 45/45 S IDs (`PASS_1_COMPLETE`) |
| Statistical relationships, pass 2 | 45/45 S IDs (`PASS_2_COMPLETE`) |
| Stable candidates mechanically rechecked | 7/7 |

The two distinct fresh statistical reviewers were `root/statistics_pass_1` and `root/statistics_pass_2`, each `gpt-5.6-terra` with high reasoning effort. Pass 2 reconsidered every S relationship, all seven ledger IDs, and every recheck fact; it did not delete, merge, rank, or adjudicate an ID.

## 7. Candidate Index

| Stable ID | Candidate statement | Category | Status |
|---|---|---|---|
| C001 | Inclusive versus exclusive fluid threshold in the SCD definition | Measure, label, or scale inconsistency | Pending Human Adjudication |
| C002 | Mortality absolute-risk-reduction percent/unit conflict | Cross-document numeric inconsistency | Pending Human Adjudication |
| C003 | Cardiac-arrest events assigned incompatible resuscitation-scale categories | Measure, label, or scale inconsistency | Pending Human Adjudication |
| C004 | Preventability threshold excludes and includes rating 4 | Measure, label, or scale inconsistency | Pending Human Adjudication |
| C005 | The same SCDE reference count is labelled annual and two-year | Denominator, proportion, or total inconsistency | Pending Human Adjudication |
| C006 | Stat-call absolute reduction does not reproduce from the printed inputs | Numeric or arithmetic inconsistency | Pending Human Adjudication |
| C007 | Urgent PICU admission rates do not match printed counts and denominators at conventional rounding | Denominator, proportion, or total inconsistency | Pending Human Adjudication |

## 8. Candidate Evidence Cards

All cards below are **Pending Human Adjudication**.

## C001 — Inclusive versus exclusive fluid threshold in the SCD definition

**Candidate statement:** The same SCD fluid component is printed with inclusive and exclusive 60 mL/kg thresholds.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [main article — PDF p. 4](<../jama_parshuram_2018_oi_180015.pdf#page=4>); [Supplement 1 Table 5 — PDF p. 24](<../joi180015supp1_prod.pdf#page=24>); [Supplement 3 eTable 1 — PDF p. 6](<../joi180015supp3_prod.pdf#page=6>).

**Source evidence:** The article says `60 mL/kg or greater` within 12 hours; Supplement 1 and Supplement 3 say `>60 mL/kg` for the matched component.

**Reported-versus-comparator:** `x >= 60` versus `x > 60` on the same unit and 12-hour window.

**Reasoning procedure:** Compare the boundary operators at the exact threshold.

**Calculation:** At `x = 60`, `x >= 60` is true and `x > 60` is false; Table 5 also leaves 60 outside its printed `<60` and `>60` bands.

**Alternative source-grounded interpretations:** The article may paraphrase a strict operational rule, or the support sources may retain a strict sign while an inclusive rule was applied; supplied sources do not decide.

**Mechanical evidence recheck:** 7/7 recheck confirmed all three passages and the corrected Supplement 3 locator on PDF page 6; event-level boundary cases and rounding instructions are absent.

**Quality-control relevance:** Outcome-definition boundaries should be harmonized across the article and supplements.

**Potential downstream evidence impact:** If confirmed, an extractor could copy different SCD fluid-boundary definitions; no actual downstream use or effect is asserted.

**Human verification steps:** Obtain the operational adjudication and rounding rule for cumulative fluid exactly equal to 60 mL/kg.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Mortality absolute-risk-reduction percent/unit conflict

**Candidate statement:** A matched mortality planning reduction is printed as `0.9%` at one location but as `0.9 per 1,000`/`0.09%` elsewhere.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [Supplement 1 — PDF p. 1](<../joi180015supp1_prod.pdf#page=1>), [p. 14](<../joi180015supp1_prod.pdf#page=14>), [p. 29](<../joi180015supp1_prod.pdf#page=29>); [main article — PDF p. 4](<../jama_parshuram_2018_oi_180015.pdf#page=4>).

**Source evidence:** The matched 18% reduction from 5.1 deaths/1,000 is `0.9 per 1,000` and `0.09%` at matched locations, while Supplement 1 p. 29 says `0.9%`.

**Reported-versus-comparator:** `0.9%` versus the corresponding `0.9 per 1,000 = 0.09%`.

**Reasoning procedure:** Reproduce the relative-to-absolute conversion on a common scale.

**Calculation:** `5.1 × 0.178 = 0.9078` per 1,000 = `0.09078%`, conventionally `0.09%`; `0.9%` equals 9 per 1,000 and is tenfold larger.

**Alternative source-grounded interpretations:** P. 29 may have intended `0.09%` or `0.9 per 1,000`; the package does not establish editorial intent.

**Mechanical evidence recheck:** All four page locations and printed values were rechecked; baseline, relative reduction, and units suffice for the conversion, but an editorial record is absent.

**Quality-control relevance:** A planning absolute reduction requires a consistent unit and percentage representation.

**Potential downstream evidence impact:** If confirmed, a planning absolute reduction or unit could be copied into evidence extraction; no propagation or conclusion change is claimed.

**Human verification steps:** Verify the intended p. 29 unit against the calculation record and harmonize matched planning statements.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Cardiac-arrest events assigned incompatible resuscitation-scale categories

**Candidate statement:** Cardiac-arrest events are described as categories 6/7 but a Table 6 legend calls events including cardiac arrest 4/5.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [Supplement 1 — PDF p. 11](<../joi180015supp1_prod.pdf#page=11>), [Table 5 — PDF p. 24](<../joi180015supp1_prod.pdf#page=24>), [Table 6 legend — PDF p. 27](<../joi180015supp1_prod.pdf#page=27>).

**Source evidence:** P. 11 defines cardiac arrest without preceding DNR as 6 or 7; Table 5 maps CPR to 6 and death to 7; Table 6 names events including cardiac arrest as scale 4 or 5.

**Reported-versus-comparator:** `{4,5}` versus `{6,7}` under the named seven-category Children’s Resuscitation Intensity Scale.

**Reasoning procedure:** Compare discrete sets, while retaining the limitation that p. 27 does not name its scale.

**Calculation:** `{4,5} ∩ {6,7} = ∅`; the labels cannot reconcile under one unchanged scale.

**Alternative source-grounded interpretations:** P. 27 could refer to a different, undefined scale; a residual or transcription explanation is inferential.

**Mechanical evidence recheck:** The three passages were found as cited; a Table-6-specific scale definition, abstraction manual, and version history are absent.

**Quality-control relevance:** Category labels should identify a single interpretable scale for the same event class.

**Potential downstream evidence impact:** If confirmed, an extractor could copy incompatible cardiac-arrest category codes; no altered event selection or downstream use is asserted.

**Human verification steps:** Identify the scale intended in Table 6 and the operational category codes used for cardiac-arrest events.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Preventability threshold excludes and includes rating 4

**Candidate statement:** The preventability definition says `>4` while nearby and cross-source descriptions include rating 4.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [Supplement 1 — PDF p. 11](<../joi180015supp1_prod.pdf#page=11>), [Table 7 — PDF p. 28](<../joi180015supp1_prod.pdf#page=28>); [Supplement 3 eTable 1 — PDF p. 6](<../joi180015supp3_prod.pdf#page=6>); [main article — PDF p. 7](<../jama_parshuram_2018_oi_180015.pdf#page=7>).

**Source evidence:** P. 11 prints `>4` but immediately includes ratings 4, 5, and 6; Table 7 says 4 or more, Supplement 3 says 4–6, and the article describes rating 4 as more than likely preventable.

**Reported-versus-comparator:** `>4` versus `>=4` on the stated six-point scale.

**Reasoning procedure:** Evaluate the stated boundary at rating 4.

**Calculation:** `4 > 4` is false, whereas `4 >= 4` is true; the printed definitions classify rating 4 differently.

**Alternative source-grounded interpretations:** Table 7/final reporting may state the operative rule, or p. 11 may reflect a stricter intended threshold; sources do not decide.

**Mechanical evidence recheck:** All locations resolved, including corrected Supplement 3 PDF page 6; operational instructions and rating-level event data are absent.

**Quality-control relevance:** The outcome threshold should be consistently expressed across definitions and results.

**Potential downstream evidence impact:** If confirmed, a reviewer could extract different potentially-preventable threshold definitions; no count change or propagation is claimed.

**Human verification steps:** Verify the applied rule for rating 4 from adjudication instructions and reporting records.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — The same SCDE reference count is labelled annual and two-year

**Candidate statement:** The same 1,052 urgent ICU/PICU admission count is labelled annual and as a two-year total.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [Supplement 1 — PDF p. 14](<../joi180015supp1_prod.pdf#page=14>) and [PDF p. 30](<../joi180015supp1_prod.pdf#page=30>).

**Source evidence:** P. 14 says 1,052 urgent ICU admissions per year; p. 30 says 1,052 urgent PICU admissions occurred in two years after 31 January 2007.

**Reported-versus-comparator:** One identical reference count with annual versus two-year period labels.

**Reasoning procedure:** Match the four-hospital count and compare its stated observation period and rate-planning basis.

**Calculation:** If unannualized over two years, `1052 / 2 = 526` per year. Diagnostic reconstruction using printed assumptions is `1052 × .40 / (55,963 × 4) × 1,000 = 1.88`, approximately 2 per 1,000; this does not establish an exact patient-day denominator.

**Alternative source-grounded interpretations:** P. 14 may annualize another dataset, or p. 30 may describe a broader window; no year-stratified data or exact patient-days are supplied.

**Mechanical evidence recheck:** Both source passages were found. The two-year values approximately reproduce the planning rate, but exact period-specific denominators are absent.

**Quality-control relevance:** Counts used in planning must retain a clear observation period and matched denominator.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy the period or rate input inconsistently; no downstream use is asserted.

**Human verification steps:** Obtain the period-specific admission and patient-day denominators supporting 1,052 and the planning rate.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Stat-call absolute reduction does not reproduce from the printed inputs

**Candidate statement:** The printed stat-call absolute reduction does not reproduce from the displayed baseline rate and relative reduction.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [Supplement 1 — PDF p. 30](<../joi180015supp1_prod.pdf#page=30>).

**Source evidence:** The paragraph prints 8.13 calls/1,000 patient-days, maximum relative risk reduction 0.181, and a corresponding absolute reduction of 1.45 calls/1,000 patient-days.

**Reported-versus-comparator:** Printed `1.45` versus the product of printed inputs.

**Reasoning procedure:** Multiply the baseline rate by the relative reduction and test displayed-value rounding bounds.

**Calculation:** `8.13 × .181 = 1.47153`, conventionally 1.47. Display bounds `8.125 × .1805 = 1.4665625` through values below `8.135 × .1815 = 1.4765025` do not overlap the `1.445` to below `1.455` range displaying as 1.45.

**Alternative source-grounded interpretations:** More precise undisplayed inputs, a transcription step, or a nonstandard display method could explain the value; none is supplied.

**Mechanical evidence recheck:** The complete matched statement was confirmed on p. 30. Unrounded power-calculation inputs and output are absent.

**Quality-control relevance:** Planning arithmetic should be reproducible from reported inputs or explain the use of hidden precision.

**Potential downstream evidence impact:** If confirmed, an extractor could copy a planned stat-call absolute reduction; no impact on trial results or downstream use is asserted.

**Human verification steps:** Retrieve the precise power-calculation inputs/output and the documented rounding method.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Urgent PICU admission rates do not match the printed counts and denominators at conventional rounding

**Candidate statement:** Two printed urgent-PICU rates do not conventionally round from the displayed numerator and denominators.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [Supplement 1 — PDF p. 30](<../joi180015supp1_prod.pdf#page=30>).

**Source evidence:** The four-hospital table prints 1,052 unplanned PICU admissions, 7,300 PICU discharges, 55,963 hospital discharges, 14.5%, and 18 per 1,000.

**Reported-versus-comparator:** Printed `14.5%` and `18 per 1,000` versus rates calculated from the displayed integers.

**Reasoning procedure:** Calculate each rate and compare conventional nearest-display rounding; retain undefined alternative denominator/display conventions.

**Calculation:** `1052/7300 × 100 = 14.4109589%`, conventionally 14.4%; `1052/55963 × 1,000 = 18.7977778`, conventionally 19. The printed denominators fall outside the respective nearest-rounding denominator ranges 7,231–7,280 and 56,865–60,114.

**Alternative source-grounded interpretations:** Undisplayed denominators, weighting, extraction history, or a display convention could explain one or both rates; truncation could explain 18 but not 14.5 from 14.4109589.

**Mechanical evidence recheck:** The table and paragraph were confirmed on p. 30; no alternative denominators or documented rounding rule is supplied.

**Quality-control relevance:** Printed numerator, denominator, rate, and rounding convention should be mutually interpretable.

**Potential downstream evidence impact:** If confirmed, an extractor could copy either urgent-PICU rate; no propagation or changed conclusion is asserted.

**Human verification steps:** Verify the source denominators, weighting, and display convention that produced both printed rates.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## 9. Downstream Evidence-Chain Considerations

If a candidate is confirmed, a systematic review, meta-analysis, guideline, or data extractor could copy the affected threshold, category code, period, rate, unit, or planned effect. This is a bounded quality-control rationale only; the supplied package does not establish actual propagation, a conclusion change, or harm.

## 10. Limitations and Missing Definitions

Fresh native/layout text was readable, with rendered pages used where complex layout required visual confirmation. The package lacks event-level data, operational adjudication manuals, document-version history, exact four-hospital patient-day denominators, original power-calculation outputs, a documented table-rounding convention, and full adjusted-model covariance information. These absences limit resolution of the human questions but not reproduction of the printed comparisons. No external evidence was used.

## 11. Human Adjudication Checklist

- Confirm each cited passage against the linked supplied PDF page.
- Obtain operational definitions, calculation records, source denominators, and version history where requested in each card.
- Determine validity, importance, and action only through the blank human-adjudication fields in each card.
- Preserve stable IDs and document any decision outside this report’s quality-control record.

## 12. Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

Fresh inventory, source coverage, coverage manifest, relationship inventories, checkers, ledger, recheck, and quality audit form the current evidence chain. Hashes matched before/after review; all 69 direct source units mapped. The versioned detail artifacts are under `review_1_5_2/`.

### Agent execution

| Stage | Agent ID | Model | Effort | Start mode |
|---|---|---|---|---|
| coordinator | root | gpt-5.6-sol | high | CURRENT_SESSION |
| fresh preprocessing | root/fresh_preprocessing | gpt-5.6-terra | medium | FRESH_SPAWN |
| main mapping | root/main_mapping | gpt-5.6-terra | medium | FRESH_SPAWN |
| support mapping protocol | root/support_mapping_protocol | gpt-5.6-terra | medium | FRESH_SPAWN |
| support mapping results | root/support_mapping_results | gpt-5.6-terra | medium | FRESH_SPAWN |
| numeric checks | root/numeric_review | gpt-5.6-terra | medium | FRESH_SPAWN |
| cross-source checks | root/cross_source_review | gpt-5.6-terra | medium | FRESH_SPAWN |
| statistical pass 1 | root/statistics_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN |
| evidence recheck | root/evidence_recheck | gpt-5.6-sol | high | FRESH_SPAWN |
| statistical pass 2 | root/statistics_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN |
| evidence quality | root/quality_audit | gpt-5.6-sol | high | FRESH_SPAWN |
| report generation | root/report_generation | gpt-5.6-terra | medium | FRESH_SPAWN |

### Performance profile

- **Target basis:** Four supplied PDFs contain 69 total pages, all requiring fresh extraction and mapping; the package is smaller than the 102-page calibration package but includes a 37-page protocol and multiple result-bearing supplements, so the comparable 35–50 minute planning band remains bounded and appropriate.
- **Total source units:** 69
- **Fresh-source units:** 69
- **Target elapsed minutes:** 35-50
- **Started UTC:** 2026-08-24T01:51:31Z
- **Finished UTC:** 2026-08-24T02:38:54Z
- **Observed elapsed minutes:** 47.4
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token accounting and token-only API-equivalent cost

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Token accounting summary |
|---|---|
| gpt-5.6-sol | 3 agents; 0 known tokens; 3 unavailable usage records; incomplete runtime usage |
| gpt-5.6-terra | 9 agents; 0 known tokens; 9 unavailable usage records; incomplete runtime usage |

Amounts are token-only API-equivalent estimates under the dated pricing snapshot, not invoices. Cached input/cache-write counts are input subsets and reasoning counts are output subsets; they are not added again to total tokens. Per-agent detail is in `review_1_5_2/token_usage_summary.md`.
