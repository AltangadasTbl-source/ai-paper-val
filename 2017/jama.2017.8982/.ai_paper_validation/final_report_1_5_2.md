# Quantitative Quality-Control Consistency Review: Moon et al. Paper Package

## Pending Human Adjudication Notice

All five observations in this report are **Pending Human Adjudication**. They are reproducible quantitative reporting quality-control candidates, not findings of paper invalidity, a correction, severity, author intent, or conclusion change.

## Executive Quality-Control Summary

Fresh, source-first processing of the complete supplied package identified **5** stable candidate consistency issues: one cross-document percentage discrepancy, one displayed fraction/percentage discrepancy, two unlabeled reduced-denominator issues, and one non-equivalent age-threshold label. Every direct source unit, mapped quantitative relationship, and mapped statistical relationship was covered. No candidate is based solely on a display-zero P value.

Small preventable reporting defects can matter when values, denominators, or eligibility labels are copied into later evidence extraction. The supplied package does not establish propagation, clinical harm, or a change to any study conclusion.

## Package and Fresh-Processing Provenance

This review used only the supplied direct scientific sources and excluded prior audit derivatives as evidence inputs. The sources were read without modification:

| Source ID | Supplied source | Role | PDF pages | SHA-256 |
|---|---|---|---:|---|
| DOC-001 | [jama_moon_2017_oi_170077.pdf](<../jama_moon_2017_oi_170077.pdf#page=1>) | Main article | 9 | `f4734692348aff9419889b4ee0dbc47a27be820629a51e20e1480a48ed2af037` |
| DOC-002 | [joi170077supp1_prod.pdf](<../joi170077supp1_prod.pdf#page=1>) | Trial protocol | 21 | `6f65a0d07d4ebfe501f80e5add4bbd01fca5eaa77c1308327e9930b48171bcf8` |
| DOC-003 | [joi170077supp2_prod.pdf](<../joi170077supp2_prod.pdf#page=1>) | Results supplement | 12 | `8f17d4eb453ca6de44de42dc428db4d9ead3b7c7f200f1bad2337f667a0ba3ff` |

Fresh processing created native and layout text for every page and a 200-dpi rendering for every page. Native/layout text was usable for all result-relevant material, so targeted CPU OCR was not required. DOC-002 PDF p. 21 was visually confirmed as page-number-only. The fresh evidence-asset inventory, coverage manifest, relationship inventories, recheck, and quality audit are retained under `review_1_5_2/`.

## Scope, Complete Coverage, and Exclusions

The complete direct-source scope was 42 PDF pages: 9 main-article pages, 21 protocol pages, and 12 supplement pages. Source coverage was complete: 42 of 42 fresh-required units were mapped, with zero reusable units. The 16-row coverage manifest completed the source inventory, fresh assets, disjoint main/support evidence mapping, numeric checking, cross-source checking, candidate registration, evidence recheck, two statistical passes, quality audit, and this report.

The review assessed numeric, denominator/proportion/total, inferential-statistical, cross-document, measure/label/scale, and rate/count consistency. It did not perform a raw-data, broad methodology, clinical, misconduct, novelty, or conclusion-validity audit, and it used no external literature.

## Quantitative and Statistical Relationship Coverage

The fresh numeric relationship inventory contains **64** relationships: N001–N043 from the main article and N1001–N1021 from the protocol and supplement. All 64 were mapped and checked.

The fresh statistical relationship inventory contains **29** relationships: S001–S017 and S1001–S1012. Statistical pass 1 and statistical pass 2 each completed all 29 relationships. They were performed by distinct freshly spawned `gpt-5.6-terra` agents at high reasoning effort. The two passes found no display-zero P-value record, and no candidate was registered from display-zero notation.

## Candidate Index

| Stable ID | Category | Candidate statement | Primary evidence |
|---|---|---|---|
| [C001](#c001--matched-205291-room-sharing-result-is-printed-as-both-704-and-705) | Cross-document numeric inconsistency | The same 205/291 control room-sharing result is printed as 70.4% and 70.5%. | Main Table 3 p. 7; supplement eTable 5 p. 9 |
| [C002](#c002--etable-2-reports-9171263-as-727-while-the-printed-fraction-supports-726) | Numeric or arithmetic inconsistency | eTable 2 prints 917/1263 as 72.7%, while the fraction supports 72.6% at one decimal. | Supplement eTable 2 p. 3 |
| [C003](#c003--etable-2-uses-reduced-education-and-marital-status-denominators-without-labeling-them) | Denominator, proportion, or total inconsistency | eTable 2 uses reduced education and marital-status denominators without labeling them. | Supplement eTable 2 p. 3 |
| [C004](#c004--etable-3-percentages-use-several-reduced-denominators-despite-full-group-n-headings) | Denominator, proportion, or total inconsistency | eTable 3 percentages use several reduced denominators despite full group-N headings and no missingness labels. | Supplement eTable 3 p. 5 |
| [C005](#c005--linked-etable-5-and-efigure-use-60-versus-60-days-for-the-same-display-population) | Measure, label, or scale inconsistency | Linked eTable 5 and eFigure use non-equivalent infant-age thresholds, ≥60 versus >60 days. | Supplement eTable 5 pp. 9–10; eFigure p. 11 |

## Candidate Evidence Cards

## C001 — Matched 205/291 room-sharing result is printed as both 70.4% and 70.5%

**Status:** Pending Human Adjudication

**Candidate statement:** The same printed room-sharing-without-bed-sharing control result, 205/291, has two different one-decimal percentage displays.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [jama_moon_2017_oi_170077.pdf — PDF p. 7, Table 3](<../jama_moon_2017_oi_170077.pdf#page=7>), Room Sharing Without Bed Sharing, BF NQI/BF mHealth control arm; [joi170077supp2_prod.pdf — PDF p. 9, eTable 5](<../joi170077supp2_prod.pdf#page=9>), Sleep Location, all-race Breastfeeding/Breastfeeding control row.

**Source evidence:** Main Table 3 prints `205/291 (70.4)`; supplement eTable 5 prints `N=291` and `205 (70.5%)` for the matched result.

**Reported-versus-comparator:** The matched outcome, all-race control group, age criterion, numerator, denominator, raw measure, and one-decimal display are printed as 70.4% versus 70.5%.

**Reasoning procedure:** A single printed numerator/denominator under the same ordinary one-decimal rounding rule should yield one displayed percentage. The calculation is diagnostic and does not assert the table-production mechanism.

**Calculation:** `205 / 291 × 100 = 70.446735%`, which rounds to 70.4% to one decimal under round-to-nearest.

**Alternative source-grounded interpretations:** An unreported rounding, weighting, export, or transcription difference may exist. No supplied source identifies a different denominator or population for the supplement row.

**Mechanical evidence recheck:** Both locations, printed values, shared 205/291 fraction, matched labels, and calculation were mechanically re-read from the supplied PDFs. Production calculation and export rules are not supplied.

**Quality-control relevance:** The printed values do not reconcile under the stated matched-display rule and require confirmation of the intended percentage.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy either 70.4% or 70.5% for the same printed 205/291 result. The supplied package does not establish that either value has propagated or changed a conclusion.

**Human verification steps:** Confirm whether both displays were generated from the identical unweighted 205/291 result and production rounding rule; then identify the intended displayed percentage.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — eTable 2 reports 917/1263 as 72.7% while the printed fraction supports 72.6%

**Status:** Pending Human Adjudication

**Candidate statement:** eTable 2 prints 917 of 1263 respondents as 72.7%, although the displayed fraction yields 72.6% to one decimal under ordinary nearest rounding.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [joi170077supp2_prod.pdf — PDF p. 3, eTable 2](<../joi170077supp2_prod.pdf#page=3>), respondent infant age 8–11 weeks; [jama_moon_2017_oi_170077.pdf — PDF p. 5, Table 1](<../jama_moon_2017_oi_170077.pdf#page=5>), four 8–11-week arm counts; [jama_moon_2017_oi_170077.pdf — PDF p. 8](<../jama_moon_2017_oi_170077.pdf#page=8>), narrative 72.6% statement.

**Source evidence:** eTable 2 declares respondent `N=1263` and prints `917 (72.7%)`. Main Table 1 prints counts 205, 214, 262, and 236, which sum to 917. The main narrative prints 72.6% with wording of 8 to 12 weeks.

**Reported-versus-comparator:** The eTable’s 917/1263 is printed as 72.7%; the direct fraction check gives 72.6% to one decimal. The narrative percentage is supportive, but its 8-to-12-week wording is not assumed identical to the tabular 8–11-week label.

**Reasoning procedure:** Check the printed count against the displayed eTable denominator and stated one-decimal precision. The direct within-eTable calculation is independent of the narrative wording.

**Calculation:** `205 + 214 + 262 + 236 = 917`; `917 / 1263 × 100 = 72.604909%`, which rounds to 72.6% to one decimal.

**Alternative source-grounded interpretations:** An unreported denominator, weighting, age-bin boundary, or export rule may have been used. The table’s production basis and the narrative endpoint meaning are not supplied.

**Mechanical evidence recheck:** The supplement row and respondent heading were found on PDF p. 3; PDF p. 4 contains continuation rows. The count, denominator, four Table 1 counts, and narrative wording were rechecked at the cited pages.

**Quality-control relevance:** The printed fraction and displayed one-decimal percentage require confirmation of the intended denominator and presentation.

**Potential downstream evidence impact:** If confirmed, a data extractor could record 72.7% rather than the fraction-derived 72.6% for 917 of 1263 respondents. The package does not establish propagation or conclusion change.

**Human verification steps:** Confirm the denominator and production basis for the eTable 2 cell and clarify whether the narrative’s 8-to-12-week wording denotes the table’s 8–11-week bin.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — eTable 2 uses reduced education and marital-status denominators without labeling them

**Status:** Pending Human Adjudication

**Candidate statement:** eTable 2 headings show respondent/nonrespondent/total Ns of 1263/337/1600, but education and marital-status percentages reproduce smaller, unlabeled variable-specific bases.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [joi170077supp2_prod.pdf — PDF p. 3, eTable 2](<../joi170077supp2_prod.pdf#page=3>), column headings and education/marital-status rows.

**Source evidence:** Education counts sum to 1258/336/1594 and marital-status counts sum to 1248/332/1580, while headings give 1263/337/1600. No missing/unknown row or row-specific N is printed for these blocks.

**Reported-versus-comparator:** The full heading Ns are presented with category rows whose totals and percentages instead track reduced bases.

**Reasoning procedure:** Reconcile exhaustive-looking category totals with the displayed column Ns and use discriminating percentage cells to test whether the printed percentages use the full or reduced bases.

**Calculation:** Education leaves 5/1/6 observations unaccounted for and marital status leaves 15/5/20. `88/1258 = 7.00%`; `640/1248 = 51.28%`, matching the printed values, whereas `640/1263 = 50.67%` does not match 51.3%.

**Alternative source-grounded interpretations:** Variable-specific missing observations or complete-case denominators may explain the reduced bases, but the table does not label them.

**Mechanical evidence recheck:** Headings, category counts, percentages, and the absence of a missing/unknown row or row-specific N were mechanically re-read from the cited supplied PDF page. Missing-data definitions are not supplied.

**Quality-control relevance:** The displayed denominator basis cannot be fully reconstructed from the table, creating a reproducible denominator-disclosure question.

**Potential downstream evidence impact:** If confirmed, a secondary user could mistakenly use the full respondent-status Ns as the education or marital-status percentage bases. The package does not show that this has occurred.

**Human verification steps:** Confirm the variable-specific nonmissing denominators and missing counts for each respondent-status column and determine whether the table should disclose them.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — eTable 3 percentages use several reduced denominators despite full group-N headings

**Status:** Pending Human Adjudication

**Candidate statement:** eTable 3 prints group Ns of 417/387/421/379, while selected race/ethnicity, education, and marital-status percentages reproduce reduced, unlabeled variable-specific totals.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [joi170077supp2_prod.pdf — PDF p. 5, eTable 3](<../joi170077supp2_prod.pdf#page=5>), group headings and Race/Ethnicity, Mother’s Education, and Marital Status rows.

**Source evidence:** Group headings give N=417/387/421/379. Race/ethnicity, education, and marital-status blocks contain selected category totals below those Ns without a missing/unknown category or row-specific N.

**Reported-versus-comparator:** Full group headings are displayed alongside percentage cells that align with reduced category totals rather than the heading Ns.

**Reasoning procedure:** Reconcile category sums with group headings, then test discriminating cells against full and reduced denominators at the printed precision.

**Calculation:** Race/ethnicity BF/BF totals 416 rather than 417: `155/416 = 37.26%` gives 37.3%, while `155/417 = 37.17%` gives 37.2%. SS/SS education totals 377 rather than 379: `87/377 = 23.08%` gives 23.1%, while `87/379 = 22.96%` gives 23.0%. Marital totals include 414, 419, and 377 versus headings 417, 421, and 379.

**Alternative source-grounded interpretations:** Variable-specific missing data could explain the reduced denominators, but the supplied table does not identify the missing values or bases.

**Mechanical evidence recheck:** The group headings, affected row counts, printed percentages, and lack of missing/row-N labels were mechanically re-read from the cited supplied PDF page. Variable-specific missingness definitions are unavailable.

**Quality-control relevance:** The full displayed Ns and apparent percentage bases do not reconcile without an unprinted denominator definition.

**Potential downstream evidence impact:** If confirmed, a secondary user could reconstruct affected eTable 3 percentages with the displayed full group Ns instead of the apparent variable-specific bases. The package does not establish downstream use or conclusion change.

**Human verification steps:** Confirm the nonmissing Ns and missing counts for each affected eTable 3 group-variable block and determine whether row-specific bases should be disclosed.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Linked eTable 5 and eFigure use ≥60 versus >60 days for the same display population

**Status:** Pending Human Adjudication

**Candidate statement:** Reciprocally linked eTable 5 and eFigure labels use non-equivalent age thresholds: `≥60 days` and `>60 days`.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [joi170077supp2_prod.pdf — PDF p. 9, eTable 5 title](<../joi170077supp2_prod.pdf#page=9>); [joi170077supp2_prod.pdf — PDF p. 10, eTable 5 continuation](<../joi170077supp2_prod.pdf#page=10>); [joi170077supp2_prod.pdf — PDF p. 11, eFigure title and note](<../joi170077supp2_prod.pdf#page=11>).

**Source evidence:** eTable 5 says outcomes are reported when the infant was `≥60 days` old and directs readers to the eFigure for graphical frequency data. The eFigure says `>60 days` old and directs readers to eTable 5 for sample sizes.

**Reported-versus-comparator:** `age ≥ 60` includes records at exactly 60 days, while `age > 60` excludes them; the linked displays do not state a population distinction.

**Reasoning procedure:** Compare the printed inequality symbols in linked table/figure displays and apply their direct set-inclusion meaning. No aggregate arithmetic is required.

**Calculation:** `age ≥ 60` equals `age > 60` plus any records with `age = 60`; the labels are not logically equivalent unless no exactly-60-day records existed or a symbol was used informally.

**Alternative source-grounded interpretations:** The figure’s strict symbol may be informal shorthand, or the displays may use distinct populations. Neither explanation is stated in the supplied package.

**Mechanical evidence recheck:** The eTable title, reciprocal cross-reference, eFigure title, and eFigure reference to eTable sample sizes were mechanically re-read on the cited supplied PDF pages. The operational filter and count of exactly-60-day records are not supplied.

**Quality-control relevance:** A non-equivalent eligibility label in linked displays can change the population definition that a reader records, even though the package does not establish that any underlying values differ.

**Potential downstream evidence impact:** If confirmed, a data extractor could record either an inclusive or strict 60-day eligibility rule for the linked displays. The supplied package does not establish that the underlying data differ or that a downstream conclusion changed.

**Human verification steps:** Confirm the operational age filter used for both displays, determine whether any exactly-60-day records existed, and identify the intended labels.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

These observations are framed as bounded data-extraction risks only. If a candidate is confirmed, a systematic review, meta-analysis, guideline, or other evidence product could copy the affected percentage, denominator, or age-threshold label. This review has no supplied evidence that any such copying occurred, that an estimate changed, or that a clinical or other conclusion changed.

## Limitations and Missing Definitions

- This review is limited to quantitative reporting consistency in the three supplied PDFs and not to raw data, broad methodology, clinical practice, misconduct, novelty, or conclusion validity.
- The package does not provide C001/C002 table-production calculation, weighting, export, or rounding rules. For C002, it also does not define whether narrative `8 to 12 weeks` denotes the tabular `8–11 weeks` bin.
- C003/C004 lack printed variable-specific nonmissing denominators, missing-observation counts/categories, and exact complete-case percentage rules.
- C005 lacks the operational age filter, the number of exactly-60-day infants, and confirmation that eTable and eFigure use identical filtered records.
- Full statistical reconstruction is constrained by absent raw logistic estimates, standard errors/test statistics, covariance, working correlation, variance estimator, degrees of freedom, sidedness, conversion details, and a common CI/P inversion rule. Planned Bonferroni and reported Hochberg descriptions are not treated as interchangeable result comparators.
- Aggregate source documents cannot establish downstream propagation or conclusion change.

## Human Adjudication Checklist

- Confirm each printed value, label, numerator, denominator, and source location against the supplied PDF page.
- Determine the applicable table-production, rounding, weighting, denominator, or eligibility-definition rule.
- Record the human determination only in the five blank adjudication fields on the applicable card.
- If a presentation change is warranted, document it through the appropriate human editorial or author-contact process; this report does not assign a correction.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and Source Integrity

- **Profile:** 1.5.2
- **Evidence reuse:** NONE; prior audit derivatives were excluded from the evidence chain.
- **Direct sources:** 3 supplied PDFs.
- **Total source units:** 42
- **Fresh-source units:** 42
- **Mapped source units:** 42
- **Source hash status:** UNCHANGED; all three recomputed SHA-256 values match `source_hashes_before.sha256` and `source_hashes_after.sha256`.
- **Source coverage status:** 3 of 3 direct-source rows COMPLETE; 42 of 42 units mapped.
- **Native/layout/OCR status:** 42 native-page and 42 layout-page fresh text assets; 42 rendered pages at 200 dpi; OCR units 0 because usable native/layout text covered all result-relevant content.
- **Coverage-manifest status:** COMPLETE; all 16 disjoint rows are complete and each contains one plain relative artifact path.

### Agent Execution

| Stage | Agent ID | Model | Reasoning effort | Start mode | Primary artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | `run_state.md` |
| fresh_source_preprocessor | root:fresh_preprocessing | gpt-5.6-terra | medium | FRESH_SPAWN | `evidence_asset_inventory.md` |
| main_quantitative_mapper | root:main_mapping | gpt-5.6-terra | medium | FRESH_SPAWN | `extraction/main_quantitative_evidence.md` |
| support_quantitative_mapper | root:support_mapping | gpt-5.6-terra | medium | FRESH_SPAWN | `extraction/support_quantitative_evidence.md` |
| numeric_consistency_reviewer | root:numeric_review | gpt-5.6-terra | medium | FRESH_SPAWN | `checkers/numeric_consistency.md` |
| cross_source_consistency_reviewer | root:cross_source_review | gpt-5.6-terra | medium | FRESH_SPAWN | `checkers/cross_source_consistency.md` |
| statistics_pass_1 | root:statistical_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | `checkers/statistical_pass_1.md` |
| evidence_rechecker | root:evidence_recheck | gpt-5.6-sol | high | FRESH_SPAWN | `verification/evidence_recheck.md` |
| statistics_pass_2 | root:statistical_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | `checkers/statistical_pass_2.md` |
| quality_control_auditor | root:quality_audit | gpt-5.6-sol | high | FRESH_SPAWN | `quality/evidence_quality_audit.md` |
| report_generator | root:report_generation | gpt-5.6-terra | medium | FRESH_SPAWN | `report_generation.md` |

Both statistical passes covered all 29 relationships and used distinct fresh `gpt-5.6-terra` high-effort runtime agents.

### Performance

- **Target basis:** Three supplied PDFs totaling 42 fresh pages: a concise 9-page main randomized-trial article, a 21-page protocol with result-defining methods and planned analyses, and a 12-page results supplement containing multiple quantitative tables and a figure. Native text tools are available, no Office conversion is required, and the package needs parallel main/support mapping plus complete two-pass statistical review.
- **Total source units:** 42
- **Fresh-source units:** 42
- **Target elapsed minutes:** 30-45
- **Started UTC:** 2026-08-20T16:54:31Z
- **Finished UTC:** 2026-08-20T17:31:25Z
- **Observed elapsed minutes:** 36.9
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token Accounting and Cost

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Agents | Unavailable records | Known input tokens | Known output tokens | Known total tokens | Known cost USD | Complete estimated cost USD |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-5.6-sol | 3 | 3 | 0 | 0 | 0 | 0.000000 | __ |
| gpt-5.6-terra | 8 | 8 | 0 | 0 | 0 | 0.000000 | __ |

The runtime exposed no authoritative response-level token counts for the coordinator or any specialist, so all 11 manifested agents are recorded as `UNAVAILABLE` with exact `__` token fields rather than estimates. The zero totals above are known subtotals only; the complete token count is explicitly incomplete. Cached-input and cache-write counts are input subsets, and reasoning counts are output subsets; none is added again to total tokens. Dollar amounts are token-only API-equivalent estimates under the pricing snapshot dated 2026-08-18, not an invoice. Per-agent detail is retained in `review_1_5_2/token_usage_ledger.csv` and `review_1_5_2/token_usage_summary.md`.
